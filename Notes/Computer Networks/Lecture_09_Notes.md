# Lecture 9: DNS and Internet Applications
## Student Notes — SST Computer Networks (Term 5)

---

## 🎯 Learning Objectives

By the end of this lecture, you should be able to:
- Explain the architectural evolution from centralized `HOSTS.TXT` to the modern **distributed, hierarchical Domain Name System (DNS)**.
- Dissect the **12-byte DNS message header** down to individual bit flags (QR, Opcode, AA, TC, RD, RA, RCODE) and understand why UDP 53 vs. TCP 53 is used.
- Trace the complete recursive resolution lifecycle from browser cache, OS resolver, Root DNS Anycast instances, TLD nameservers, to Authoritative servers.
- Master all major DNS record types (**A, AAAA, CNAME, MX, TXT, NS, PTR, SOA, SRV, CAA**) and understand the apex CNAME limitation.
- Analyze security threats including **Kaminsky DNS Cache Poisoning**, and explain how **DNSSEC** (RRSIG, DNSKEY, DS) and encrypted transports (**DoH, DoT, ECH**) establish verifiable trust.
- Contrast the architectural evolution of the Web across **HTTP/1.0, HTTP/1.1, HTTP/2 (multiplexed binary framing), and HTTP/3 (QUIC over UDP)**, focusing on Head-of-Line (HoL) blocking.
- Master HTTP semantics: methods (Safe vs. Idempotent), response status codes (1xx–5xx), headers, and caching mechanisms (`Cache-Control`, `ETag`, `304 Not Modified`).
- Dissect state management on the stateless web: Cookies (`HttpOnly`, `Secure`, `SameSite`), server-side sessions, and stateless **JSON Web Tokens (JWT)**.
- Execute and interpret real-world network diagnostics using `dig +trace`, `dig +dnssec`, `nslookup`, and `curl -Iv`.

---

## 1. Why DNS? The Architectural Imperative

Computers, routers, and network switches operate strictly on numerical Layer 3 addresses (such as `142.250.195.46` or `2607:f8b0:4005:805::200e`). However, humans are notoriously bad at remembering 32-bit or 128-bit numerical strings. We navigate using semantic, memorable domain names like `scaler.com` or `google.com`.

### The Historical Failure of `HOSTS.TXT`
In the early ARPANET era (1970s–early 1980s), name resolution was managed via a single flat file called `HOSTS.TXT`, maintained centrally by the Stanford Research Institute (SRI-NIC):
1. **Network administrators emailed changes** to SRI-NIC.
2. SRI updated the master `HOSTS.TXT`.
3. Every computer across the ARPANET periodically ran FTP to download the entire updated file.

By 1983, this centralized model collapsed due to three fatal scalability bottlenecks:
- **Bandwidth & Processing Collapse**: Distributing an ever-growing multi-megabyte file to thousands of nodes created catastrophic network congestion.
- **Name Collisions**: A flat namespace meant no two organizations could use the name `mail` or `server`.
- **Zero Real-Time Consistency**: Changes took days or weeks to propagate globally.

In response, **Paul Mockapetris invented DNS in 1983 (RFC 882 & RFC 883, superseded by RFC 1034 & 1035)**: a globally distributed, hierarchically delegated, decentralized database with autonomous caching.

### Fundamental Capabilities Provided by DNS
1. **Decoupling Identity from Location**: A company can migrate servers from AWS us-east-1 to Google Cloud europe-west without changing its domain name. Only the DNS pointer changes.
2. **Load Balancing (Round-Robin DNS)**: A single domain name can return multiple `A` records. Client resolvers rotate through them to distribute traffic across server clusters.
3. **Geo-Steering & Anycast (CDNs)**: Authoritative nameservers detect the client resolver's IP (via EDNS Client Subnet) and return the IP address of the geographically closest edge cache (Cloudflare, Akamai, Fastly).
4. **Fault Tolerance & Failover**: Health checks can dynamically withdraw failed IP addresses from DNS pools with short TTLs.

---

## 2. The Global DNS Hierarchy

DNS organizes the global namespace into an **inverted tree structure** starting at the invisible **Root Zone** (represented by a single dot `.`).

```
                              . (Root Zone)
                             /      |      \
                           /        |        \
                        .com       .org       .in (Top-Level Domains - TLDs)
                        /             \          \
                 scaler.com       wikipedia.org   iitb.ac.in (Second-Level Domains)
                  /      \              \
            www.scaler  api.scaler   en.wikipedia (Subdomains / Hosts)
```

### The Three-Tier Server Architecture

| Tier | Controlled By | Responsibility | Concrete Examples |
| :--- | :--- | :--- | :--- |
| **Root Servers (`.`)** | ICANN, IANA, 12 independent operators | Points resolvers to the authoritative TLD nameservers for `.com`, `.net`, `.org`, `.edu`, ccTLDs. | 13 logical root server identities (`a.root-servers.net` to `m.root-servers.net`). |
| **TLD Servers** | Registries (Verisign for `.com`/`.net`, PIR for `.org`, NIXI for `.in`) | Holds records for all registered domains under that TLD; delegates to the domain's authoritative NS. | `a.gtld-servers.net` (Verisign) |
| **Authoritative Servers** | Domain owners, DNS hosts (Cloudflare, Route53, GoDaddy) | Stores the definitive, ground-truth resource records (`A`, `AAAA`, `MX`, `TXT`) for specific domains. | `ns1.scaler.com`, `ns-123.awsdns.org` |

### How Do 13 Root Servers Serve the Entire Planet? (BGP Anycast)
A common misconception is that there are only 13 physical root computers. In reality, while there are **13 logical IP addresses** (`A` through `M`, limited originally by the 512-byte UDP DNS packet boundary):
- Every single logical root server identity uses **BGP Anycast routing**.
- Over **1,700+ physical server instances** distributed across hundreds of data centers in over 130 countries announce the exact same 13 IP addresses into the global BGP routing table.
- When your ISP queries `198.41.0.4` (`a.root-servers.net`), BGP routes the query to the nearest physical instance in your city or region.

---

## 3. The 12-Byte DNS Message Header & Protocol Mechanics

DNS messages (both queries and responses) share a standardized binary format defined in RFC 1035:

```
 0                   1                   2                   3
 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
|       Transaction ID (16 bits)        |QR|   Opcode  |AA|TC|RD|RA|   Z   | RCODE |
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
|                    QDCOUNT (Question Count)                   |
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
|                    ANCOUNT (Answer Count)                     |
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
|                  NSCOUNT (Authority Name Server)              |
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
|                    ARCOUNT (Additional Records)               |
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
```

### Detailed Field Breakdown:
1. **Transaction ID (16 bits)**: Generated randomly by the client to match incoming responses with outgoing requests.
2. **QR (Query/Response Flag - 1 bit)**: `0` = Query, `1` = Response.
3. **Opcode (4 bits)**: `0` = Standard Query (QUERY), `1` = Inverse Query (IQUERY), `2` = Server Status (STATUS).
4. **AA (Authoritative Answer - 1 bit)**: Set to `1` in responses if the responding server is the authoritative source for the domain, rather than returning a cached answer.
5. **TC (Truncation Flag - 1 bit)**: Set to `1` if the message exceeded the transport payload limit (512 bytes over classical UDP). When a client receives `TC=1`, **it immediately retries the query over TCP port 53**.
6. **RD (Recursion Desired - 1 bit)**: Set by the client asking the server to recursively resolve the domain fully if it doesn't have the answer locally.
7. **RA (Recursion Available - 1 bit)**: Set by the server denoting whether it supports recursive resolution.
8. **RCODE (Response Code - 4 bits)**:
   - `0` (**NoError**): Successful query.
   - `1` (**FormErr**): Format error; server could not understand request.
   - `2` (**ServFail**): Server failure; unable to process due to internal nameserver error.
   - `3` (**NXDOMAIN**): Non-Existent Domain; authoritative nameserver confirms domain does not exist.
   - `5` (**Refused**): Server refuses to answer (e.g. open resolver policy denying outside queries).

### UDP vs. TCP Port 53: When is Each Used?
- **UDP Port 53**: Used for standard lightweight queries and replies. Fast, 0-RTT connectionless overhead.
- **TCP Port 53**:
  1. Fallback when responses exceed MTU/buffer size (`TC=1`).
  2. **Zone Transfers (AXFR / IXFR)**: Full synchronization of zone files between primary and secondary nameservers (requires reliable, ordered streaming).
  3. **DNSSEC**: Cryptographic signatures (`RRSIG`) and public keys (`DNSKEY`) frequently push packet sizes well above 1,500 bytes.

---

## 4. DNS Resolution: Complete Step-by-Step Lifecycle

Consider what happens when you type `www.scaler.com` into your browser:

```
[Browser] ──► [OS Resolver Cache] ──► [Local Recursive Resolver (e.g., 8.8.8.8 / ISP)]
                                               │
                                      (1) Query Root '.'
                                               ▼
                                      [Root DNS Server]
                                               │
                                      (2) Referral to '.com'
                                               ▼
                                      [TLD DNS Server (.com)]
                                               │
                                      (3) Referral to 'ns1.scaler.com'
                                               ▼
                                      [Authoritative DNS Server]
                                               │
                                      (4) Answer: A 104.18.2.35
                                               ▼
[Browser] ◄── [OS Resolver Cache] ◄── [Recursive Resolver (Caches answer)]
```

### Trace Walkthrough:
1. **Client Browser Cache**: Chrome/Firefox checks its internal memory cache (`chrome://net-internals/#dns`). If present and TTL is active, IP is returned in sub-millisecond time.
2. **OS Resolver Cache & `hosts` file**: The operating system checks `getaddrinfo()` cache and `/etc/hosts` (or `C:\Windows\System32\drivers\etc\hosts`).
3. **Recursive Resolver Query**: Client sends a recursive query (`RD=1`) to its configured DNS server (e.g. ISP DNS or Cloudflare `1.1.1.1` or Google `8.8.8.8`).
4. **Resolver Iterative Search**:
   - Resolver checks its own cache. If a cache miss occurs, it performs **iterative queries** (`RD=0`):
   - **Step A (Root)**: Queries one of the 13 Root hints (`a.root-servers.net`). Root replies with a **Referral** pointing to the `.com` TLD servers and their glue IP addresses.
   - **Step B (TLD)**: Queries `.com` TLD server (`a.gtld-servers.net`). The TLD server replies with a **Referral** pointing to `ns1.scaler.com` and `ns2.scaler.com`.
   - **Step C (Authoritative)**: Queries `ns1.scaler.com`. The authoritative server returns the final **Answer**: `www.scaler.com A 104.18.2.35` with `TTL = 300`.
5. **Caching & Final Connection**: Recursive resolver stores the answer in cache for 300 seconds and returns it to the client. Client connects to IP `104.18.2.35`.

### TTL (Time to Live) Tradeoffs
$$\text{Low TTL (60s)} \implies \text{Fast failover \& rapid migration}, \text{ BUT higher DNS traffic and higher query latency.}$$
$$\text{High TTL (86400s)} \implies \text{Extremely fast cached queries \& low DNS load}, \text{ BUT changes take up to 24 hours to propagate.}$$

---

## 5. Master DNS Record Encyclopedia

| Record Type | RFC | Full Name | Semantic Function | Real-World Example |
| :--- | :--- | :--- | :--- | :--- |
| **A** | 1035 | IPv4 Address | Maps a hostname directly to a 32-bit IPv4 address. | `scaler.com. IN A 104.18.2.35` |
| **AAAA** | 3596 | IPv6 Address | Maps a hostname to a 128-bit IPv6 address ("quad-A"). | `scaler.com. IN AAAA 2606:4700::6812:223` |
| **CNAME** | 1035 | Canonical Name | Creates an alias pointing one domain name to another domain name. | `www.scaler.com. IN CNAME scaler.com.` |
| **MX** | 1035 | Mail Exchange | Directs incoming email for a domain to mail servers, ordered by integer priority. | `scaler.com. IN MX 10 mail.scaler.com.`<br>`scaler.com. IN MX 20 backupmail.scaler.com.` |
| **NS** | 1035 | Name Server | Delegates a DNS zone to authoritative nameservers. | `scaler.com. IN NS ns1.digitalocean.com.` |
| **TXT** | 1035 | Text Record | Stores human/machine-readable text used for domain verification and email authentication. | `scaler.com. IN TXT "v=spf1 include:_spf.google.com ~all"` |
| **PTR** | 1035 | Pointer Record | Reverse DNS lookup: maps an IP address back to a hostname under `.in-addr.arpa`. | `35.2.18.104.in-addr.arpa. IN PTR scaler.com.` |
| **SOA** | 1035 | Start of Authority | Defines core zone metadata: Primary NS, admin email, Serial number, and refresh/retry/expire timers. | `scaler.com. IN SOA ns1.scaler.com. admin.scaler.com. (2026101801 7200 3600 1209600 3600)` |
| **SRV** | 2782 | Service Record | Locates specific services: defines priority, weight, port, and target hostname. | `_sip._tcp.scaler.com. IN SRV 10 60 5060 sipserver.scaler.com.` |
| **CAA** | 6844 | Cert Authority Auth | Restricts which Certificate Authorities (e.g. Let's Encrypt, DigiCert) are permitted to issue SSL/TLS certificates. | `scaler.com. IN CAA 0 issue "letsencrypt.org"` |

### The CNAME Apex Problem (`@` Zone Apex)
Per RFC 1034, **if a CNAME record exists for a node, no other data records of any type may exist for that node**:
- If you placed a CNAME at the root apex (`scaler.com CNAME cdn.provider.com`), you could not have `SOA` or `NS` records at `scaler.com`.
- This would break DNS delegation entirely!
- **Modern Solution**: Modern DNS providers implement proprietary pseudo-records like **ALIAS** (DNS Made Easy), **ANAME** (Namecheap), or **CNAME Flattening** (Cloudflare), where the authoritative nameserver dynamically resolves the target CNAME to IP addresses on the fly and returns pure `A`/`AAAA` answers.

---

## 6. DNS Security: Attacks & Defenses

Because DNS was conceived in an era of implicit trust, classical DNS queries and responses are completely unauthenticated and unencrypted plaintext.

```
       Attacker
     ┌───────────┐
     │ Injects   │
     │ Spoofed IP│
     └─────┬─────┘
           │ (Races with Authoritative Server)
           ▼
[Client] ◄── [Poisoned Resolver Cache] ◄── [Legitimate Authoritative Server (Arrived late)]
```

### 1. Kaminsky DNS Cache Poisoning Attack (2008)
Dan Kaminsky uncovered a critical flaw in recursive resolvers:
1. Attacker queries a target resolver for non-existent subdomains: `random123.example.com`.
2. Resolver sends queries to `example.com` authoritative nameservers.
3. Attacker floods the resolver with thousands of spoofed responses claiming to be `example.com`, guessing the 16-bit **Transaction ID** ($2^{16} = 65,536$ possibilities).
4. The spoofed response includes a poisoned `NS` record in the Authority section: `example.com NS attacker-controlled-ns.com`.
5. Once a guessed ID matches, the resolver permanently stores the attacker's nameserver in cache, hijacking all traffic for the entire domain!

**Mitigations**:
- **Source Port Randomization (SPR)**: Resolvers randomize UDP source port across ephemeral range ($1024 - 65535$). An attacker must guess both 16-bit Transaction ID and 16-bit Source Port: $2^{32} \approx 4.3 \text{ billion combinations}$, rendering brute-force mathematically infeasible.
- **0x20 Bit Encoding**: Randomizes case in domain query (`wWw.sCaLeR.cOm`). Authoritative servers echo the casing back; mismatched responses are discarded.

### 2. DNSSEC (Domain Name System Security Extensions)
DNSSEC adds **cryptographic digital signatures** to DNS records to guarantee authenticity and integrity:
- **RRSIG**: Cryptographic signature generated over a set of identical records (RRset).
- **DNSKEY**: Public key used by resolvers to verify `RRSIG`.
- **DS (Delegation Signer)**: SHA-256 fingerprint of the child's `DNSKEY` stored in the parent zone, forming a cryptographic **Chain of Trust** anchored in the ICANN Root Zone Key.
- Resolvers verify signatures up the hierarchy: if records are tampered with in transit, the signature check fails and the resolver returns `SERVFAIL` rather than poisoned data.

### 3. Encrypted DNS: DoT and DoH
While DNSSEC prevents spoofing, it does **not** provide privacy (queries remain plaintext to local ISPs and network eavesdroppers).
- **DoT (DNS over TLS - RFC 7858)**: Encapsulates DNS over TLS on dedicated TCP port **853**.
- **DoH (DNS over HTTPS - RFC 8484)**: Transmits DNS queries inside standard HTTPS `POST` or `GET` packets over TCP port **443** (indistinguishable from ordinary web traffic, preventing ISP censorship).

---

## 7. Real-World DNS CLI Masterclass

### 1. Tracing the Global Delegation Chain (`dig +trace`)
```bash
$ dig +trace www.scaler.com

.                       518400  IN      NS      a.root-servers.net.
...
;; Received 525 bytes from 192.168.1.1#53 in 12 ms (Answer from local resolver)

com.                    172800  IN      NS      a.gtld-servers.net.
...
;; Received 837 bytes from 198.41.0.4#53(a.root-servers.net) in 38 ms (Answer from Root)

scaler.com.             172800  IN      NS      ns1.cloudflare.com.
scaler.com.             172800  IN      NS      ns2.cloudflare.com.
;; Received 352 bytes from 192.5.6.30#53(a.gtld-servers.net) in 45 ms (Answer from TLD)

www.scaler.com.         300     IN      A       104.18.2.35
www.scaler.com.         300     IN      A       104.18.3.35
;; Received 78 bytes from 172.64.32.1#53(ns1.cloudflare.com) in 15 ms (Authoritative!)
```

### 2. Inspecting DNSSEC Authentication (`dig +dnssec`)
```bash
$ dig +dnssec scaler.com A

;; flags: qr rd ra ad; QUERY: 1, ANSWER: 2, AUTHORITY: 0, ADDITIONAL: 1
;; -> The 'ad' flag (Authenticated Data) confirms cryptographic verification passed!
scaler.com.             300     IN      A       104.18.2.35
scaler.com.             300     IN      RRSIG   A 13 2 300 20261020... (Ed25519 Signature)
```

---

## 8. HTTP Protocol Architecture: Evolution from 1.0 to 3

The **HyperText Transfer Protocol (HTTP)** is an Application Layer protocol that operates on top of transport streams.

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                             HTTP Evolution                                  │
├─────────────────┬─────────────────┬────────────────────┬────────────────────┤
│ HTTP/1.0 (1996) │ HTTP/1.1 (1997) │   HTTP/2 (2015)    │   HTTP/3 (2022)    │
│ 1 TCP per asset │ Keep-Alive      │ Binary Multiplexing│ QUIC over UDP      │
│ No Host header  │ Chunked transfer│ HPACK Compression  │ 0-RTT handshakes   │
│ Massive latency │ App-level HoL   │ TCP-level HoL      │ Zero HoL Blocking  │
└─────────────────┴─────────────────┴────────────────────┴────────────────────┘
```

### 1. HTTP/1.0 vs. HTTP/1.1: The Battle Against Latency
- In **HTTP/1.0**, every single resource (HTML, CSS, 20 images) required an independent TCP connection:
  $$\text{Latency} = 20 \times (3\text{-way TCP handshake} + \text{TLS Handshake} + \text{HTTP Transfer})$$
- In **HTTP/1.1 (RFC 2616)**, persistent connections became default:
  - `Connection: keep-alive`: Reuses a single TCP socket for multiple sequential requests.
  - **Head-of-Line (HoL) Blocking**: In HTTP/1.1, requests on a single socket must complete in strict FIFO order. If a large video download stalls on request #1, requests #2 and #3 cannot be served. Browsers mitigated this by opening 6 parallel TCP connections per host.

### 2. HTTP/2: Binary Framing & True Multiplexing (RFC 7540)
HTTP/2 abandoned plaintext ASCII on the wire in favor of an optimized **Binary Framing Layer**:
- **Streams, Messages & Frames**: A single TCP connection carries multiple bidirectional streams simultaneously. Streams are broken down into independent binary frames (`HEADERS`, `DATA`, `SETTINGS`).
- **Zero Application HoL**: Resources interleave on the wire. A large image download doesn't block a small CSS stylesheet.
- **HPACK Compression**: Headers are indexed and compressed against a shared client-server dictionary, reducing header overhead from ~800 bytes to ~20 bytes.
- **The Remaining Flaw (TCP HoL Blocking)**: Because HTTP/2 runs over a single TCP stream, if a single IP packet drops on the physical wire, TCP's sliding window freezes **all streams** until the lost packet is retransmitted.

### 3. HTTP/3: The QUIC Revolution over UDP (RFC 9114)
HTTP/3 completely eliminates TCP, running over **QUIC (Quick UDP Internet Connections)**:
- Runs over **UDP port 443**.
- **Independent Stream Isolation**: Streams exist natively at the transport layer. A lost packet on Stream 3 drops throughput on Stream 3 only; Streams 1 and 2 proceed with zero delay.
- **0-RTT Connection Establishment**: Combines cryptographic TLS 1.3 handshake with transport parameters in a single round-trip.
- **Connection Migration**: Connections are identified by a 64-bit **Connection ID**, not by `(Source IP, Source Port)`. If a user steps out of Wi-Fi onto 5G, the TCP socket does not break; the QUIC session continues seamlessly.

---

## 9. HTTP Semantics: Methods, Status Codes & State

### HTTP Methods: The Safety & Idempotence Matrix

$$\text{Safe} \iff \text{Operation does not mutate server state (Read-only)}.$$
$$\text{Idempotent} \iff f(f(x)) = f(x) \text{ (Calling 10 times produces identical server state as calling once)}.$$

| Method | Request Body | Safe? | Idempotent? | REST Architectural Role |
| :--- | :--- | :--- | :--- | :--- |
| **GET** | No | **Yes** | **Yes** | Read and retrieve resource representation. |
| **HEAD** | No | **Yes** | **Yes** | Retrieve identical headers to GET, but omit body (cache checks). |
| **POST** | Yes | No | No | Create new subordinate resource, append data, execute actions. |
| **PUT** | Yes | No | **Yes** | Complete replacement of target resource at URI. |
| **PATCH** | Yes | No | No | Partial modification / delta update to resource. |
| **DELETE**| No | No | **Yes** | Remove target resource. |
| **OPTIONS**| No | **Yes** | **Yes** | CORS preflight check; returns `Allow: GET, POST, OPTIONS`. |

### Master Status Code Breakdown

```
1xx Informational ──► 101 Switching Protocols (WebSockets upgrade)
2xx Success       ──► 200 OK, 201 Created (POST), 204 No Content (DELETE)
3xx Redirection   ──► 301 Moved Permanently (SEO permanent), 302 Found (Temporary), 304 Not Modified (Cache Hit!)
4xx Client Error  ──► 400 Bad Request, 401 Unauthorized (Unauthenticated), 403 Forbidden, 404 Not Found, 429 Too Many Requests
5xx Server Error  ──► 500 Internal Error, 502 Bad Gateway (Upstream crashed), 503 Unavailable, 504 Gateway Timeout
```

### State on the Stateless Web: Cookies vs. Sessions vs. JWTs
Because HTTP is inherently stateless, state must be explicitly maintained across requests:

```
┌─────────────────────────┬─────────────────────────┬─────────────────────────┐
│     Client Cookie       │   Server-Side Session   │   JSON Web Token (JWT)  │
├─────────────────────────┼─────────────────────────┼─────────────────────────┤
│ Stored in browser store │ State kept in DB/Redis  │ Stateless crypto token  │
│ Sent via 'Cookie:' hdr  │ Cookie holds Session ID │ Sent in 'Authorization:'│
│ Max size ~4096 bytes    │ Scalable server memory  │ Verified via signature  │
└─────────────────────────┴─────────────────────────┴─────────────────────────┘
```

### Crucial Cookie Security Attributes:
1. `HttpOnly`: Prevents client-side JavaScript (`document.cookie`) from reading the cookie, mitigating **XSS (Cross-Site Scripting)** session theft.
2. `Secure`: Instructs browser to transmit the cookie strictly over encrypted TLS connections (HTTPS).
3. `SameSite`:
   - `SameSite=Strict`: Cookie is never sent on cross-site requests (immune to **CSRF - Cross-Site Request Forgery**).
   - `SameSite=Lax`: Cookie is sent when navigating top-level from external sites (clicking external link), balancing UX and CSRF safety.
   - `SameSite=None`: Requires `Secure`; allows third-party tracking/iframe contexts.

---

## 📌 Summary Checklist & Exam Cram Notes

1. **DNS Architecture**: Hierarchical inverted tree (`.` $\rightarrow$ TLD $\rightarrow$ 2nd Level $\rightarrow$ Host). 13 logical root server identities routed globally via BGP Anycast.
2. **DNS Message Header**: 12 bytes fixed. Crucial flags: `QR` (0=query, 1=response), `AA` (Authoritative), `TC` (Truncation $\implies$ fallback to TCP), `RD` (Recursion desired), `RCODE=3` (`NXDOMAIN`).
3. **Transport Choice**: Port 53 UDP for standard queries under 512 bytes; Port 53 TCP for Zone Transfers (`AXFR`), DNSSEC large payloads, or truncated packets (`TC=1`).
4. **Key Records**: `A` (IPv4), `AAAA` (IPv6), `CNAME` (Alias - cannot coexist at apex `@`), `MX` (Mail), `TXT` (SPF/DKIM/DMARC verification), `PTR` (Reverse), `CAA` (Cert control).
5. **DNS Security**: Kaminsky attack poisoned recursive resolvers by spoofing Transaction IDs; mitigated by Source Port Randomization (SPR) and cryptographic validation via **DNSSEC** (`RRSIG`, `DNSKEY`, `DS`).
6. **HTTP Evolution**: HTTP/1.1 introduced persistent keep-alive connections; HTTP/2 introduced binary stream multiplexing over TCP; HTTP/3 implemented QUIC over UDP to eliminate TCP-level Head-of-Line blocking and support 0-RTT handshakes.
7. **HTTP Semantics**: `GET`/`HEAD` are safe and idempotent. `PUT`/`DELETE` are idempotent but unsafe. `POST`/`PATCH` are neither safe nor idempotent.
8. **Stateless Web**: Sessions store state server-side; Cookies persist session tokens in browsers; `HttpOnly` blocks XSS and `SameSite=Strict/Lax` blocks CSRF.

---

## 🧠 Practice Problems & Self-Check Questions

1. A network engineer runs `dig +trace api.scaler.com` and observes that the response contains `TC=1`. What immediate protocol action will the local resolver take, and why?
2. Why is configuring a `CNAME` record at the apex of a domain (`@` / `scaler.com`) explicitly prohibited by RFC 1034? What architectural problems would result?
3. Contrast how Head-of-Line (HoL) blocking manifests in HTTP/1.1 vs. HTTP/2. How does HTTP/3 over QUIC resolve both?
4. A web application returns `Set-Cookie: auth_token=xyz123; Path=/; Domain=.example.com; Secure`. What critical security vulnerability exists in this configuration, and which attribute is missing to prevent session hijacking via XSS?
5. During a DNS cache poisoning attack, why is guessing only the 16-bit Transaction ID insufficient against modern resolvers implementing RFC 5452?
6. An API endpoint `DELETE /v1/users/42` is called. The first call returns `204 No Content`. If the client immediately repeats the exact same call, what status code should be returned, and is the `DELETE` method idempotent?
