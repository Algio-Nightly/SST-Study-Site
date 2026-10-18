# Lecture 13: The Complete Internet Journey — From URL to Rendered Response
## Capstone Masterclass Notes — SST Computer Networks (Term 5)

---

## 🎯 Executive Overview & Capstone Objectives
When an engineer presses <kbd>Enter</kbd> in a browser after typing `https://www.scaler.com/courses?id=42`, they trigger one of the most intricate distributed orchestrations in human history. In less than 500 milliseconds, dozens of protocols operating across all seven OSI layers collaborate across physical radio frequencies, copper wiring, transoceanic fiber-optic backbones, BGP routing fabrics, cryptographic key exchanges, kernel network stacks, and containerized microservice architectures.

```
       ┌─────────────────────────────────────────────────────────────────────────────────┐
       │                       THE GRAND END-TO-END INTERNET JOURNEY                     │
       │                                                                                 │
       │  [L1/L2 Link & DHCP] ──▶ [L7 Browser & HSTS] ──▶ [L7/L4 Recursive DNS Walk]    │
       │           │                                                    │                │
       │           ▼                                                    ▼                │
       │  [L2 ARP Gateway] ──▶ [L3 NAT / PAT Router] ──▶ [L3 BGP Backbone & Anycast]    │
       │                                                                │                │
       │                                                                ▼                │
       │  [L7 Browser Render] ◀── [L7 Reverse Proxy & App] ◀── [L4 TCP & L6 TLS 1.3]    │
       └─────────────────────────────────────────────────────────────────────────────────┘
```

By the end of this capstone synthesis, you will be able to:
- Map every single microsecond of a web request to its precise OSI layer, protocol, and data structure.
- Understand host link establishment: 802.11 Wi-Fi 4-way handshakes, DHCP DORA leasing, and Gratuitous ARP.
- Trace the global recursive DNS resolution hierarchy across BGP Anycast root clusters, TLD registries, and EDNS0 Client Subnets.
- Dissect how NAT/PAT gateways, OSPF/IS-IS ISP backbones, and inter-domain BGP routing guide IP packets to Anycast VIPs.
- Walk through the simultaneous cryptographic and transport handshakes: TCP 3-way handshake options negotiation and TLS 1.3 Ephemeral Diffie-Hellman key derivation.
- Contrast HTTP/1.1 vs HTTP/2 binary framing vs HTTP/3 QUIC over UDP.
- Unpack Data Center ingress: Anycast POPs, SSL offloading, Reverse Proxies (NGINX/Envoy), and Kubernetes service meshes.
- Break down the browser's internal critical rendering path from decrypted HTML bytes to pixels on the screen.

---

## 1. Phase 0: Physical Attachment & Host Network Bootstrapping

Before a single HTTP packet can be conceived, the client device (e.g., a developer laptop) must join a physical network and obtain an identity.

```
Laptop                                              Access Point / Router (192.168.1.1)
  │                                                                 │
  │── 1. 802.11 Probe Request / Association ───────────────────────▶│
  │◀── 2. Association Response ─────────────────────────────────────│
  │                                                                 │
  │── 3. EAPOL 4-Way Handshake (WPA2/WPA3 Pre-Shared Key) ──────────▶│
  │◀── 4. Pairwise Transient Key (PTK) Derived ─────────────────────│
  │                                                                 │
  │── 5. DHCP Discover (UDP 67/68, L2/L3 Broadcast) ───────────────▶│
  │◀── 6. DHCP Offer (IP: 192.168.1.5, Gateway: 192.168.1.1) ───────│
  │── 7. DHCP Request ─────────────────────────────────────────────▶│
  │◀── 8. DHCP Ack (Lease Committed) ───────────────────────────────│
  │                                                                 │
  │── 9. Gratuitous ARP ("Does anyone own 192.168.1.5?") ──────────▶ (Broadcast)
  │     (No reply received ➔ IP confirmed unique)                   │
```

### 1.1 Wi-Fi Link Association & 4-Way WPA Handshake
1. **802.11 Beacon & Probe**: The laptop's wireless card scans the 2.4GHz / 5GHz / 6GHz spectrum for 802.11 Beacon frames broadcasting the SSID. It transmits an *Association Request* containing supported Modulation and Coding Schemes (MCS).
2. **The 4-Way EAPOL Handshake**: To secure the link without transmitting the Wi-Fi password over the air, the client and Access Point (AP) execute a 4-way Extensible Authentication Protocol over LAN (EAPOL) handshake.
   - Both sides independently know the **Pairwise Master Key (PMK)** derived from the Wi-Fi password via PBKDF2.
   - They exchange nonces ($ANonce$ and $SNonce$) and construct the **Pairwise Transient Key (PTK)**:
     $$\text{PTK} = \text{PRF-512}(\text{PMK}, ANonce, SNonce, \text{MAC}_{\text{AP}}, \text{MAC}_{\text{Client}})$$
   - The PTK encrypts all subsequent L2 frames using AES-CCMP or GCMP.

### 1.2 Dynamic Host Configuration (DHCP DORA)
The laptop has link-layer connectivity but lacks an IP configuration. It launches the DHCP DORA state machine over UDP:
1. **Discover**: Client broadcasts on LAN ($L2: \text{FF:FF:FF:FF:FF:FF}$, $L3: 255.255.255.255$, $Src: 0.0.0.0:68 \rightarrow Dst: 255.255.255.255:67$).
2. **Offer**: The local router (192.168.1.1) proposes IP `192.168.1.5`, Subnet Mask `/24`, Default Gateway `192.168.1.1`, and DNS resolvers `1.1.1.1` and `8.8.8.8`.
3. **Request**: Client confirms acceptance of the proposed lease.
4. **Ack**: Server binds the lease into its state table.

### 1.3 Collision Avoidance via Gratuitous ARP
Before binding `192.168.1.5` to its interface `wlan0`, the OS kernel transmits an ARP probe (Gratuitous ARP) asking: *"Who has 192.168.1.5? Tell 192.168.1.5"*. If another device replies, an IP collision is detected, and the host declines the lease (`DHCPDECLINE`). Hearing silence, the host assigns the IP.

---

## 2. Phase 1: The Browser Engine & Application Entry Point

The user types `https://www.scaler.com/courses?id=42` into the address omnibox.

### 2.1 URL Parsing & Normalization
The browser engine's URI parser decomposes the string:
- **Scheme**: `https://` $\rightarrow$ implies default TCP port `443` and mandatory TLS encryption.
- **Host / FQDN**: `www.scaler.com` $\rightarrow$ Target server name.
- **Path**: `/courses` $\rightarrow$ Resource location on server.
- **Query String**: `?id=42` $\rightarrow$ Key-value parameters passed to application handler.

### 2.2 HSTS (HTTP Strict Transport Security) Preload Check
Before checking any network socket, the browser checks its internal **HSTS Preload List** (a hardcoded database compiled directly into Chromium, Firefox, and Safari).
- If `scaler.com` is in the HSTS list, even if the user typed `http://` (plain unencrypted HTTP), the browser internally redirects to `https://` immediately (**307 Internal Redirect**).
- **Security Purpose**: Completely neutralizes SSL Stripping Man-in-the-Middle (MITM) attacks (e.g., Moxie Marlinspike's *sslstrip*) where an attacker intercepts unencrypted port 80 requests before a 301 redirect occurs.

### 2.3 Multi-Tier Browser Cache Evaluation
Before touching the network interface, the browser queries its multi-tiered cache:
1. **Service Worker Cache**: Programmable client-side JavaScript interceptor (Cache Storage API).
2. **Memory Cache**: In-process RAM cache storing active session resources.
3. **Disk Cache (HTTP/1.1 Caching Engine)**:
   - Evaluates `Cache-Control: max-age=86400, stale-while-revalidate=3600`.
   - If a valid cached copy exists and is fresh: The browser serves the document directly from disk ($0\text{ms}$ latency, no network packets).
   - If stale, the browser prepares a **Conditional GET Request** appending:
     - `If-None-Match: "a38f-5c21980"` (ETag validator)
     - `If-Modified-Since: Tue, 15 Oct 2026 12:00:00 GMT`

---

## 3. Phase 2: The Global Recursive DNS Resolution Walk

Assuming a cache miss, the browser must map the human-readable FQDN `www.scaler.com` to a routable IP address.

```
Browser ──▶ OS Stub Resolver ──▶ Local DNS Forwarder ──▶ Public Recursive Resolver
                                                           (e.g., 1.1.1.1 / 8.8.8.8)
                                                                     │
                   ┌─────────────────────────────────────────────────┼──────────────────────────────┐
                   │                                                 │                              │
                   ▼                                                 ▼                              ▼
          [1. Root Nameserver]                              [2. TLD Nameserver]         [3. Authoritative Nameserver]
         (Query: .com NS)                                  (Query: scaler.com NS)       (Query: www.scaler.com A)
         Returns: a.gtld-servers.net                       Returns: ns-cloud.com        Returns: 104.21.48.12 (TTL 300)
```

### 3.1 The Local Cache Cascade
1. **Browser DNS Cache**: Checked first (Chrome stores DNS records in memory for 60 seconds; check via `chrome://net-internals/#dns`).
2. **OS Resolver Cache**: System daemon (e.g., `systemd-resolved` on Linux, DNS Client Service on Windows).
3. **Static Hosts File**: Checked at `/etc/hosts` (Linux/macOS) or `C:\Windows\System32\drivers\etc\hosts`.
4. **Local Resolver Forwarder**: Query sent to gateway `192.168.1.1:53` via UDP, which forwards to upstream Recursive Resolver (e.g., `1.1.1.1` or ISP resolver).

### 3.2 The Global Iterative DNS Walk
The recursive resolver (`1.1.1.1`) performs an iterative resolution walk:
1. **Root Nameservers (`.` zone)**:
   - Query sent to one of the 13 Root Server identities (`a.root-servers.net` to `m.root-servers.net`).
   - Each root identity uses **BGP Anycast** across $>1,700$ physical servers worldwide.
   - Root responds with a referral to the `.com` Top-Level Domain (TLD) nameservers (`a.gtld-servers.net`).
2. **TLD Nameservers (`.com` zone)**:
   - Operated by Verisign. The resolver asks: *"Where is scaler.com?"*
   - TLD nameserver replies with **NS records** pointing to the authoritative DNS provider (e.g., Cloudflare: `ns1.cloudflare.com`) plus Glue records (their IP addresses).
3. **Authoritative Nameservers (`scaler.com` zone)**:
   - Resolver queries `ns1.cloudflare.com`: *"What is the A/AAAA record for www.scaler.com?"*
   - Cloudflare nameserver inspects **EDNS0 Client Subnet (RFC 7871)** in the query (which forwards the client's `/24` prefix) and returns the topologically closest Anycast IP:
     $$\text{A Record} = 104.21.48.12 \quad (\text{TTL } 300\text{ seconds})$$
4. **DNSSEC Validation**: If enabled, the recursive resolver verifies the cryptographic chain of trust from the Root Key-Signing Key (KSK) down through the DS records to the zone's RRSIG signature, proving the IP was not spoofed.

---

## 4. Phase 3: Layer 2 Frame Construction & Local Routing

The OS has determined the destination IP is `104.21.48.12`. It must now transmit the IP packet onto the local network link.

### 4.1 Host Routing Decision (FIB Lookup)
The kernel inspects its internal Forwarding Information Base (FIB):

```bash
# Output of 'ip route'
default via 192.168.1.1 dev wlan0 proto dhcp metric 600
192.168.1.0/24 dev wlan0 proto kernel scope link src 192.168.1.5
```
- **Evaluation**: The kernel performs a bitwise AND:
  $$104.21.48.12 \ \& \ 255.255.255.0 = 104.21.48.0 \neq 192.168.1.0$$
- Destination is **NOT on the local link**. The packet must be forwarded to the Default Gateway: `192.168.1.1`.

### 4.2 ARP / Neighbor Discovery for Gateway MAC
To build the Ethernet / 802.11 frame, the host needs the Layer 2 MAC address of `192.168.1.1`:
- **ARP Cache Hit**: The kernel queries its ARP table (`ip neighbor`). If `192.168.1.1` maps to `11:22:33:44:55:66`, the frame is constructed immediately.
- **ARP Cache Miss**: The kernel suspends the outgoing IP packet in a buffer and broadcasts an `ARP Request`:
  ```
  ARP: Who has 192.168.1.1? Tell 192.168.1.5 (Broadcast MAC: FF:FF:FF:FF:FF:FF)
  ```
  The gateway replies with its MAC address (`11:22:33:44:55:66`). The kernel populates its ARP cache and releases the buffered packet.

### 4.3 Frame Encapsulation
The host builds the complete Layer 2 frame:
```
┌─────────────────────────── Ethernet Frame ───────────────────────────┐
│ Dst MAC: 11:22:33:44:55:66 (Router Gateway)                          │
│ Src MAC: AA:BB:CC:DD:EE:FF (Laptop Interface)                        │
│ EtherType: 0x0800 (IPv4)                                             │
├─────────────────────────── IPv4 Header ──────────────────────────────┤
│ Src IP: 192.168.1.5 (Laptop Private IP)                              │
│ Dst IP: 104.21.48.12 (Server Anycast Public IP)                      │
│ Protocol: 6 (TCP), TTL: 64, DF: 1                                    │
├─────────────────────────── TCP Segment ──────────────────────────────┤
│ Src Port: 52410 (Ephemeral), Dst Port: 443 (HTTPS)                   │
│ Flags: [SYN], Seq: 284102910                                         │
└──────────────────────────────────────────────────────────────────────┘
```

---

## 5. Phase 4: Network Address Translation (NAT/PAT) & WAN Transit

The home router receives the frame on its LAN port.

```
[Laptop]                      [Home Router]                               [Internet]
192.168.1.5:52410 ──▶ [LAN Interface : WAN NAT Translation] ──▶ 203.0.113.45:18204 ──▶ 104.21.48.12:443
                      NAT Table:
                      203.0.113.45:18204 ⟷ 192.168.1.5:52410
```

### 5.1 NAPT (Port Address Translation) Execution
1. The router strips the incoming Layer 2 Ethernet header.
2. It detects the destination `104.21.48.12` routes out its WAN interface.
3. The router allocates an unused ephemeral port from its public pool (e.g., `18204`).
4. **Header Rewriting**:
   - Rewrites `Src IP: 192.168.1.5` $\rightarrow$ `203.0.113.45` (Router WAN Public IP).
   - Rewrites `Src Port: 52410` $\rightarrow$ `18204`.
   - Decrements `TTL` from $64$ to $63$.
   - **Checksum Recalculation**: Recomputes the IPv4 header checksum and TCP pseudo-header checksum.
5. The router encapsulates the packet into the WAN Layer 2 framing (e.g., PPPoE, DOCSIS cable framing, or GPON optical frame) and transmits it to the ISP's Broadband Network Gateway (BNG).

---

## 6. Phase 5: Autonomous Systems, BGP Routing, & Anycast Ingress

The packet now traverses the global Internet backbone:

```
[Home ISP (AS 1234)] 
        │ (Interior Routing: OSPF / IS-IS + MPLS Core)
        ▼
[Border Gateway Router]
        │ 
        │ eBGP Peering Session (AS-PATH: 1234 ➔ 13335)
        ▼
[Internet Exchange Point (IXP) / Tier-1 Transit (e.g., Lumen, Telia)]
        │ 
        ▼
[Cloudflare Edge Anycast POP (AS 13335)]
```

### 6.1 Inter-Domain Routing via BGP
1. Cloudflare operates Autonomous System Number **AS 13335**.
2. Cloudflare announces the IP prefix `104.21.48.0/24` via **Border Gateway Protocol (BGP)** to hundreds of Internet Exchange Points (IXPs) and Tier-1 transit providers across the planet.
3. Because multiple physical data centers announce the *exact same IP prefix*, this is **BGP Anycast**.
4. The ISP's border routers evaluate their BGP routing table, selecting the path with the shortest `AS_PATH` and optimal `LOCAL_PREF`.
5. The packet automatically routes to the **topologically nearest Cloudflare Point of Presence (PoP)** (e.g., Mumbai, Frankfurt, or San Jose) in fewer than 15 milliseconds!

---

## 7. Phase 6: Transport Handshake & TLS 1.3 Encryption

Upon arriving at Cloudflare's Anycast Edge router, the packet reaches an L4 load balancer (e.g., Unimog or Maglev) which forwards it to an edge worker server.

```
Laptop                                               Cloudflare Edge Server
  │                                                                 │
  │── 1. TCP SYN (Seq=X, MSS=1460, WScale=7, SACK) ────────────────▶│
  │◀── 2. TCP SYN-ACK (Seq=Y, Ack=X+1, MSS=1460, WScale=7) ─────────│
  │── 3. TCP ACK (Ack=Y+1) + TLS 1.3 ClientHello (Piggybacked!) ──▶│
  │      - Supported Ciphers: TLS_AES_256_GCM_SHA384                │
  │      - SNI: "www.scaler.com"                                    │
  │      - Key Share: Client ECDH Public Key (g^a)                  │
  │                                                                 │
  │◀── 4. TLS 1.3 ServerHello ──────────────────────────────────────│
  │      - Selected Cipher: TLS_AES_256_GCM_SHA384                  │
  │      - Key Share: Server ECDH Public Key (g^b)                  │
  │      {Encrypted Extensions}                                     │
  │      {Server Certificate + Chain}                               │
  │      {CertificateVerify (Signature over handshake)}             │
  │      {Finished (HMAC of handshake transcript)}                  │
  │                                                                 │
  │   [Both sides independently compute Master Secret: g^(ab)]      │
  │   [Symmetric AES-256-GCM Session Keys Derived via HKDF]         │
  │                                                                 │
  │── 5. TLS Finished + Encrypted HTTP Request ────────────────────▶│
  │      (GET /courses?id=42 HTTP/2)                                │
```

### 7.1 TCP Three-Way Handshake Options
During the initial SYN / SYN-ACK exchange, modern network stacks negotiate critical TCP performance extensions:
- **MSS (Maximum Segment Size)**: Announces largest payload host can receive without IP fragmentation (typically $1460\text{ bytes}$ for standard Ethernet).
- **Window Scaling (RFC 7323)**: Overcomes the legacy 16-bit window limit ($65,535\text{ bytes}$) by defining a scale factor of $7$ ($2^7 = 128$). Allows window sizes up to $1\text{ GiB}$, crucial for high Bandwidth-Delay Product (BDP) links.
- **SACK Permitted (RFC 2018)**: Selective Acknowledgments allow the receiver to inform the sender exactly which discontinuous blocks of data arrived, avoiding redundant retransmissions.

### 7.2 TLS 1.3 Handshake & Ephemeral Diffie-Hellman (ECDHE)
In TLS 1.3, encryption setup is reduced from 2 RTTs (in TLS 1.2) to **exactly 1 RTT**:
1. **ClientHello + Key Share**: The client guesses the server's preferred elliptic curve (e.g., **X25519**). It generates a random private scalar $a$, computes public key $A = a \cdot G$, and transmits $A$ in the very first packet along with the **Server Name Indication (SNI)** header `www.scaler.com`.
2. **ServerHello + Key Share**: The server generates random private scalar $b$, computes public key $B = b \cdot G$, and sends $B$ back.
3. **Cryptographic Secret Computation**:
   - Client computes shared point: $K = a \cdot B = a \cdot (b \cdot G)$.
   - Server computes shared point: $K = b \cdot A = b \cdot (a \cdot G)$.
   - Both arrive at identical shared secret $K$ without ever transmitting it over the wire!
4. **HKDF Key Derivation**: Both sides feed $K$ through an HMAC-based Extract-and-Expand Key Derivation Function (HKDF) to generate symmetric keys:
   $$\text{Client\_Write\_Key}, \quad \text{Server\_Write\_Key}, \quad \text{Initialization Vectors (IV)}$$
5. **Certificate Validation**: The client verifies that Cloudflare's presented X.509 certificate is signed by a trusted Root CA in its local operating system trust store (e.g., DigiCert or Let's Encrypt), has not expired, and contains `scaler.com` in its Subject Alternative Name (SAN).

---

## 8. Phase 7: Application Protocols — HTTP/1.1 vs HTTP/2 vs HTTP/3

Once the TLS record layer is established, the application transmits the HTTP request:

```
┌────────────────────────────────────────────────────────────────────────┐
│                        HTTP PROTOCOL EVOLUTION                         │
├────────────────────────────────────────────────────────────────────────┤
│ HTTP/1.1 : Text-based, Head-of-Line Blocking, 1 request per TCP socket │
│ HTTP/2   : Binary Framing, Multiplexing streams over single TCP socket │
│ HTTP/3   : QUIC over UDP, Zero Head-of-Line blocking, 0-RTT re-connect │
└────────────────────────────────────────────────────────────────────────┘
```

### 8.1 The HTTP/2 Binary Request
Under HTTP/2, the plaintext ASCII text is converted into binary frames on **Stream ID 1**:
- **HEADERS Frame**: Compressed using **HPACK** (RFC 7541). Redundant headers like `User-Agent` and `Cookie` are indexed into dynamic tables, shrinking hundreds of bytes down to single-byte indices.
- **DATA Frame**: Contains optional request body (empty for `GET`).

```http
:method: GET
:scheme: https
:authority: www.scaler.com
:path: /courses?id=42
user-agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)...
accept: text/html,application/xhtml+xml,application/xml;q=0.9
accept-encoding: gzip, deflate, br, zstd
cookie: session_token=xyz987654321
```

### 8.2 What if HTTP/3 (QUIC) is Used?
If the browser previously received an `Alt-Svc: h3=":443"` header from Scaler:
- The entire TCP + TLS 1.3 stack is replaced by **QUIC over UDP** (port 443).
- **Zero Head-of-Line Blocking**: If packet loss occurs on Stream 1, Stream 3 continues downloading images without stuttering!
- **Connection Migration**: If the user disconnects from Wi-Fi and shifts to 5G cellular, the IP changes, but QUIC's **64-bit Connection ID** allows the active video stream or download to persist seamlessly without renegotiating connections.

---

## 9. Phase 8: Data Center Ingress, Microservices, & Database

Cloudflare's edge server now acts as a **Reverse Proxy**.

```
[Client] ──TLS──▶ [Edge Anycast POP] ──Origin Tunnel──▶ [Origin Load Balancer (Envoy)]
                                                                   │
                       ┌───────────────────────────────────────────┴───────────────────────────────────────────┐
                       ▼                                           ▼                                           ▼
             [Pod: Auth Service]                         [Pod: Course Catalog]                       [Pod: Recommendation]
                       │                                           │                                           │
                       ▼                                           ▼                                           ▼
             [Redis Cache Cluster]                       [PostgreSQL Primary]                        [Elasticsearch Engine]
```

### 9.1 Edge to Origin Ingress
1. **Edge Cache Check**: Cloudflare checks if `/courses?id=42` is cached at the edge. Because it contains dynamic course data and user session cookies, it is marked as a **Cache Miss**.
2. **Origin Shield / Cloudflare Tunnel**: The edge node opens a persistent, multiplexed HTTP/2 connection over private fiber back to Scaler's origin data center (e.g., AWS us-east-1).
3. **Header Enrichment**: The proxy appends enterprise provenance headers:
   - `X-Forwarded-For: 203.0.113.45` (Real user IP)
   - `X-Forwarded-Proto: https`
   - `CF-Ray: 8d29a0f12c34-BOM` (Distributed tracing correlation ID)

### 9.2 The Kubernetes Service Mesh
1. **Ingress Gateway (Envoy / NGINX)**: Terminates origin TLS. Inspects path `/courses` and executes Layer-7 routing.
2. **Cluster IP & Service Mesh (Istio / Linkerd)**:
   - Request is routed via internal mTLS (Mutual TLS) to the `course-catalog` microservice pod.
   - The application checks **Redis** for `course:42:metadata`.
   - **Cache Hit**: Returns in $0.8\text{ms}$. (If Miss: Executes SQL query `SELECT * FROM courses WHERE id = 42` against PostgreSQL, taking $4\text{ms}$).
3. **Response Assembly**: The application serializes the HTML template with the course data, adds security headers, and streams the response bytes back to the load balancer.

---

## 10. Phase 9: Return Journey & Response Headers

The origin web server transmits an HTTP/2 response back through the proxy to the client:

```http
HTTP/2 200 OK
content-type: text/html; charset=UTF-8
content-encoding: br
cache-control: private, max-age=0, must-revalidate
etag: W/"48a2-9d8f10"
set-cookie: session_token=xyz987654321; Path=/; Secure; HttpOnly; SameSite=Lax
strict-transport-security: max-age=31536000; includeSubDomains; preload
content-security-policy: default-src 'self' https://cdn.scaler.com
server: cloudflare
cf-ray: 8d29a0f12c34-BOM

[Brotli-compressed HTML stream...]
```

### Header Anatomy & Security Significance:
- `content-encoding: br`: Payload is compressed using **Brotli** (superior compression ratio to gzip for text).
- `Strict-Transport-Security`: Forces all future connections within the next year ($31,536,000\text{ seconds}$) to use HTTPS exclusively.
- `Content-Security-Policy (CSP)`: Instructs browser to execute scripts *only* originating from trusted domains, mitigating Cross-Site Scripting (XSS).
- `Set-Cookie`:
  - `Secure`: Transmit cookie only over encrypted TLS links.
  - `HttpOnly`: Forbids JavaScript `document.cookie` access, preventing cookie theft via XSS.
  - `SameSite=Lax`: Defends against Cross-Site Request Forgery (CSRF).

---

## 11. Phase 10: Client Processing & The Critical Rendering Path

As Brotli-compressed TCP segments arrive at the laptop's Wi-Fi card:

```
[Compressed Packets] ──▶ [TCP Reassembly] ──▶ [TLS Decryption] ──▶ [Brotli Decompression]
                                                                            │
      ┌─────────────────────────────────────────────────────────────────────┘
      ▼
[Raw HTML Bytes] ──▶ [Tokenization] ──▶ [DOM Tree Generation]
                                               │
                                               ├─▶ Parse CSS ──▶ [CSSOM Tree]
                                               │                      │
                                               ▼                      ▼
                                         [Render Tree = DOM + CSSOM]
                                                      │
                                                      ▼
                                            [Layout / Reflow]
                                                      │
                                                      ▼
                                            [Painting & Compositing]
                                                      │
                                                      ▼
                                            [Pixels on Screen!]
```

1. **TCP Reassembly & Flow Control**: The kernel reconstructs the byte stream in strict sequence order, acknowledging packets via TCP cumulative ACKs.
2. **TLS Decryption**: Hardware AES-NI CPU instructions decrypt TLS records in real time.
3. **Progressive HTML Parsing**: The browser does **not** wait for the full HTML file to download. It streams bytes into an HTML tokenizer:
   - Constructs the **Document Object Model (DOM)** tree.
   - When encountering `<link rel="stylesheet">`, it initiates asynchronous subresource downloads.
   - When CSS arrives, it parses CSS rules into the **CSS Object Model (CSSOM)** tree.
4. **Render Tree Construction**: Merges DOM + CSSOM, omitting invisible elements (`display: none`).
5. **Layout (Reflow)**: Calculates exact geometric coordinates and pixel dimensions for every box on screen.
6. **Paint & Composite**: Rasterizes text, colors, borders, and shadows into GPU layers, compositing the final image onto the user's display monitor!

---

## 12. Phase 11: Connection Teardown & Lifecycle

When the tab is closed or the server's keep-alive timeout expires:

```
Laptop                                               Cloudflare Server
  │                                                                 │
  │── 1. TCP [FIN, ACK] (Seq=U, Ack=V) ────────────────────────────▶│
  │◀── 2. TCP [ACK] (Ack=U+1) ──────────────────────────────────────│
  │      (Half-Closed Connection: Server can still send data)       │
  │                                                                 │
  │◀── 3. TCP [FIN, ACK] (Seq=W, Ack=U+1) ──────────────────────────│
  │── 4. TCP [ACK] (Ack=W+1) ──────────────────────────────────────▶│
  │                                                                 │
  │   [Laptop Enters TIME_WAIT State for 2MSL = 60 Seconds]         │
  │   [NAT Router Table Entry Reaped]                               │
```

1. **The 4-Way FIN Teardown**: Each side independently closes its half of the bidirectional channel.
2. **The $2\text{MSL}$ `TIME_WAIT` Guard**: The initiator of the close (the laptop) enters `TIME_WAIT` for $2 \times \text{Maximum Segment Lifetime} = 60\text{ seconds}$. This guarantees:
   - The final ACK is retransmitted if dropped, preventing the server from hanging in `LAST_ACK`.
   - Any delayed duplicate packets wandering the Internet expire without corrupting future connections reusing the same 4-tuple.
3. **NAT Cleanup**: The home router drops the port translation entry from its state table.

---

## 13. Master Latency Budget & Timing Waterfall

Where did the time go? Here is the nanosecond-to-millisecond accounting of an end-to-end request:

```
0ms       Browser Cache Check
+1ms      Local DNS Cache Miss ➔ Send UDP Query to 1.1.1.1
+14ms     DNS Resolution Complete (Edge Anycast Resolver Hit)
+15ms     Local Routing / ARP Cache Hit
+16ms     TCP Handshake SYN Sent ──▶ Path RTT = 24ms
+40ms     TCP Handshake Established (1 RTT)
+41ms     TLS 1.3 ClientHello Sent (Key Share ECDHE)
+65ms     TLS 1.3 ServerHello Received & Session Established (1 RTT)
+66ms     HTTP/2 GET Request Sent over Encrypted Channel
+90ms     Request Arrives at Edge POP ➔ Dispatched to Origin
+115ms    Origin Gateway ➔ Kubernetes Ingress ➔ Pod Execution
+125ms    Redis Hit + PostgreSQL Execution + HTML Template Rendered
+150ms    First HTML Byte Arrives at Browser (TTFB = 150ms!)
+180ms    Full HTML Stream Ingested & Decompressed
+260ms    Critical CSS & JS Loaded via Subresource Multiplexing
+320ms    DOM / CSSOM Ready ➔ Layout & Paint Complete (First Contentful Paint)
```

$$\mathbf{\text{Total Time to Interactive (TTI)}} \approx \mathbf{320\text{ milliseconds}}$$

---

## 14. Course Synthesis: The Grand Protocol Rosetta Stone

| Phase | Protocol | OSI Layer | Encapsulated Within | Core Addressing / Identifier | Key Failure Mode |
|:---|:---|:---:|:---|:---|:---|
| **Link Join** | 802.11 / EAPOL | Layer 2 | Radio Waves | 48-bit MAC Address | Wrong Wi-Fi Password (PTK failure) |
| **IP Lease** | DHCP | Layer 7 / 3 | UDP / IP / Ethernet | Transaction ID / MAC | IP Conflict / Pool Exhaustion |
| **Gateway Find**| ARP | Layer 2 | Ethernet Frame | IPv4 ⟷ MAC Binding | ARP Poisoning / Gateway Offline |
| **Name Resolve**| DNS | Layer 7 | UDP / IP (Port 53) | Fully Qualified Domain Name | NXDOMAIN / Cache Poisoning |
| **Hop Forward** | IP | Layer 3 | Ethernet Frame | 32-bit IPv4 / 128-bit IPv6 | Routing Loop / TTL Exceeded |
| **NAT Translation**| NAPT | Layer 3/4 | IP Header | Public IP + Port Tuple | Port Exhaustion / Broken PMTUD |
| **Autonomous Routing**| BGP | Layer 3/4 | TCP (Port 179) | Autonomous System Number (ASN) | BGP Route Hijack / Flapping |
| **Transport** | TCP | Layer 4 | IP Datagram | 16-bit Port / 32-bit Seq Num | SYN Flood / Packet Drop / RST |
| **Encryption** | TLS 1.3 | Layer 6 / 4 | TCP Stream | Domain Name in SNI / Cert SAN | Expired Cert / Untrusted CA |
| **Web Protocol**| HTTP/2 | Layer 7 | TLS Record | Uniform Resource Identifier (URI)| 502 Bad Gateway / 504 Timeout |
| **Rendering** | DOM / CSSOM | Host Engine | Process Memory | CSS Selectors / DOM Nodes | Render-Blocking JavaScript |

---

## 🧠 Comprehensive Capstone Review Questions with Detailed Solutions

### 1. Why does an HTTPS request require TWO separate handshakes (TCP + TLS) in HTTP/2, but only ONE handshake in HTTP/3?
* **Solution**:
  - In HTTP/2, TCP operates at Layer 4 and TLS 1.3 operates on top of the established byte stream. TCP requires 1 RTT to synchronize sequence numbers (SYN, SYN-ACK, ACK). Only after TCP is established can the client send the TLS `ClientHello`, requiring a second RTT for cryptographic key exchange.
  - In HTTP/3, the transport protocol is **QUIC** (running over UDP). QUIC fuses the transport connection parameters (connection IDs, packet numbers) and the cryptographic parameters (TLS 1.3 keys) into a **single unified handshake**. The initial QUIC datagram contains both the transport connection request and the TLS 1.3 `ClientHello`, achieving full transport reliability and mutual encryption in **exactly 1 RTT** (or 0-RTT on resumption).

### 2. A user types `https://scaler.com`. At which points do MAC addresses change, and at which points do IP addresses change?
* **Solution**:
  - **MAC Addresses**: Change at **every single Layer-3 hop**. When the packet leaves the laptop, Dst MAC is the home router. When the home router sends it to the ISP modem, Dst MAC becomes the ISP modem. At every router in the path, the old L2 frame is stripped, and a new L2 frame with new source and destination MACs is synthesized.
  - **IP Addresses**: In pure routing, IP addresses **never change end-to-end**. However, because the user is on a private network (`192.168.1.5`), the home router's NAT gateway rewrites the Source IP to the router's public WAN IP (`203.0.113.45`). From the WAN router across the global Internet backbone to Cloudflare's Edge, the Source IP (`203.0.113.45`) and Destination IP (`104.21.48.12`) remain strictly unchanged.

### 3. If a user visits a site and receives an HTTP 304 Not Modified status, did a DNS query take place? Did a TCP handshake take place? Explain precisely.
* **Solution**:
  - **DNS Query**: If the DNS record was still cached in the browser's DNS cache or the OS cache (TTL not expired), **no DNS query took place**. If the TTL expired, a DNS query was executed to re-resolve the IP.
  - **TCP Handshake**: If an existing TCP connection to that host was still alive in the browser's connection pool via HTTP Keep-Alive, **no TCP handshake was performed** (the conditional GET was sent over the existing socket). If the socket had closed, a new TCP 3-way handshake was executed.
  - **The 304 Response**: The client transmitted a lightweight HTTP request with `If-None-Match: "<ETag>"`. The server confirmed the resource had not changed and returned `304 Not Modified` with **zero body bytes**. The browser loaded the cached body from its local disk, saving network bandwidth.

### 4. What is the fundamental security vulnerability of transmitting an HTTP request over plain Wi-Fi without WPA2/WPA3 encryption, even if the website uses HTTPS?
* **Solution**:
  - While HTTPS encrypts the HTTP payload (path, headers, cookies, body), the **outer Layer 2 and Layer 3 headers are in plaintext**.
  - On open unencrypted Wi-Fi, an eavesdropper with Wireshark in monitor mode can capture every 802.11 radio frame. They can read the user's MAC address, the server's public IP address, the packet timing, packet lengths, and the **Server Name Indication (SNI)** in the TLS `ClientHello` (unless Encrypted Client Hello / ECH is active). The attacker can deduce every single domain name the user visits!
  - WPA2/WPA3 provides link-layer encryption, ensuring that even broadcast radio waves cannot be sniffed by neighboring devices on the same physical frequency.

---

*Lecture 13 of 13 — Computer Networks, Term 5, SST*
*Congratulations on completing the entire Computer Networks curriculum!*
