"""
Lecture 13 Quiz: The Complete Internet Journey (URL to Rendered Response)
20 Advanced Multi-Correct MCQs (5 options each, 2 to 5 correct answers)
"""

QUIZ_L13 = {
    "topicId": "lecture-13",
    "lectureNumber": 13,
    "title": "The Complete Internet Journey Capstone Quiz",
    "description": "20 rigorous multi-correct questions synthesizing the entire course: 802.11 link establishment, DHCP/ARP bootstrapping, HSTS preload, global recursive DNS walk, BGP Anycast, NAT/PAT, TCP options, TLS 1.3 ECDHE key exchange, HTTP/2 vs HTTP/3 QUIC, reverse proxy ingress, and browser rendering pipeline.",
    "estimatedMinutes": 40,
    "questions": [
        {
            "id": "l13-q01",
            "type": "multi_choice",
            "question": "Before any IP traffic can flow, a client laptop connects to an encrypted 802.11 Wi-Fi network. Which of the following statements regarding link establishment and the 4-Way WPA2/WPA3 Handshake are correct?",
            "options": [
                {"id": "A", "text": "The laptop scans for 802.11 Beacon frames broadcasting the SSID, sends an Association Request, and receives an Association Response."},
                {"id": "B", "text": "Both the client and the Access Point independently derive the Pairwise Master Key (PMK) from the Wi-Fi pre-shared key (passphrase)."},
                {"id": "C", "text": "The client and AP execute a 4-way EAPOL handshake, exchanging nonces ($ANonce$ and $SNonce$) to derive the Pairwise Transient Key (PTK)."},
                {"id": "D", "text": "The Wi-Fi pre-shared passphrase is sent in plaintext across the radio link so the Access Point can verify it against its internal database."},
                {"id": "E", "text": "The derived PTK is used to encrypt all subsequent Layer 2 802.11 data frames using AES-CCMP or GCMP."}
            ],
            "correctOptionIds": ["A", "B", "C", "E"],
            "explanation": "Statements A, B, C, and E are correct. The client associates via beacons/probes (A), both sides derive PMK locally (B), exchange nonces to derive PTK via EAPOL (C), and encrypt L2 frames with AES (E). D is false: The passphrase/PMK is NEVER sent over the air; the 4-way handshake proves knowledge of the key mathematically without exposing it.",
            "difficulty": "hard",
            "subtopic": "Wi-Fi Link Attachment & 4-Way Handshake"
        },
        {
            "id": "l13-q02",
            "type": "multi_choice",
            "question": "Immediately following Layer 2 link establishment, the laptop bootstraps its IP configuration. Which of the following events occur during DHCP and Gratuitous ARP?",
            "options": [
                {"id": "A", "text": "The laptop broadcasts a DHCP Discover over UDP (Source: `0.0.0.0:68`, Destination: `255.255.255.255:67`)."},
                {"id": "B", "text": "The local router responds with a DHCP Offer proposing an IP address (`192.168.1.5`), Subnet Mask (`/24`), Default Gateway (`192.168.1.1`), and DNS servers."},
                {"id": "C", "text": "After committing the lease via Request and Ack, the client sends a Gratuitous ARP asking: 'Who has 192.168.1.5? Tell 192.168.1.5'."},
                {"id": "D", "text": "If another host on the LAN responds to the Gratuitous ARP, an IP collision is detected, and the client declines the lease (`DHCPDECLINE`)."},
                {"id": "E", "text": "The DHCP Discover frame is routed across 5 transoceanic BGP backbone routers to reach ICANN headquarters."}
            ],
            "correctOptionIds": ["A", "B", "C", "D"],
            "explanation": "Statements A, B, C, and D accurately represent host network bootstrapping. DHCP Discover broadcasts from 0.0.0.0 (A). Offer provides IP, mask, gateway, and DNS (B). Gratuitous ARP verifies IP uniqueness before assignment (C & D). E is absurd: DHCP Discover is a local broadcast contained strictly within the local LAN.",
            "difficulty": "medium",
            "subtopic": "DHCP Bootstrapping & Gratuitous ARP"
        },
        {
            "id": "l13-q03",
            "type": "multi_choice",
            "question": "A user types `https://scaler.com` into the browser omnibox. Which of the following occur during URL parsing and HSTS evaluation before any network packets are sent?",
            "options": [
                {"id": "A", "text": "The browser URI parser extracts the scheme (`https`), hostname (`scaler.com`), implicit port (443), and root path (`/`)."},
                {"id": "B", "text": "The browser checks its internal hardcoded HSTS (HTTP Strict Transport Security) Preload List."},
                {"id": "C", "text": "If `scaler.com` is present in the HSTS preload list, even if the user typed `http://`, the browser internally upgrades the request to `https://` (307 Internal Redirect) without transmitting an unencrypted request over the wire."},
                {"id": "D", "text": "HSTS preloading protects users against SSL-Stripping Man-in-the-Middle attacks on public networks."},
                {"id": "E", "text": "The browser executes a physical ping to the root DNS server before parsing the URL text."}
            ],
            "correctOptionIds": ["A", "B", "C", "D"],
            "explanation": "Statements A, B, C, and D are correct. The browser parses URI components (A), checks the HSTS Preload database (B), performs client-side 307 internal redirection to HTTPS (C), completely neutralizing SSL-stripping attacks (D). E is nonsense.",
            "difficulty": "medium",
            "subtopic": "URL Parsing & HSTS Preload Protection"
        },
        {
            "id": "l13-q04",
            "type": "multi_choice",
            "question": "Before initiating network communication, the browser evaluates its multi-tier cache. Which of the following cache mechanisms and behaviors are correct?",
            "options": [
                {"id": "A", "text": "The browser queries the Service Worker Cache (if registered) and the Memory Cache before checking the persistent Disk Cache."},
                {"id": "B", "text": "If a cached resource is fresh according to its `Cache-Control: max-age`, the browser serves it directly from disk, completing the request in $0\\text{ ms}$ with zero network traffic."},
                {"id": "C", "text": "If a cached resource is stale, the browser sends a Conditional GET request containing `If-None-Match: <ETag>` and/or `If-Modified-Since`."},
                {"id": "D", "text": "If the resource has not changed on the server, the server replies with `304 Not Modified` with zero body bytes, prompting the browser to render the cached body."},
                {"id": "E", "text": "A response marked `Cache-Control: no-cache` can never be stored on the client's hard disk."}
            ],
            "correctOptionIds": ["A", "B", "C", "D"],
            "explanation": "Statements A, B, C, and D are correct. Multi-tier cache checks Service Worker $\\rightarrow$ Memory $\\rightarrow$ Disk (A). Fresh cache hits require 0 network packets (B). Stale entries trigger conditional validation via `If-None-Match` (C), returning `304 Not Modified` with empty body on match (D). E is false: `no-cache` CAN be stored on disk, but must be revalidated before use; `no-store` is the directive that forbids disk storage.",
            "difficulty": "medium",
            "subtopic": "Browser Cache Evaluation & Conditional Revalidation"
        },
        {
            "id": "l13-q05",
            "type": "multi_choice",
            "question": "On a cold DNS cache miss, the recursive resolver walks the global DNS hierarchy to resolve `www.scaler.com`. Which of the following steps occur during this iterative walk?",
            "options": [
                {"id": "A", "text": "The resolver queries a Root Nameserver (`.` zone), which responds with a referral (NS records) to the `.com` Top-Level Domain (TLD) nameservers along with glue records."},
                {"id": "B", "text": "The resolver queries the `.com` TLD nameserver, which responds with a referral to Scaler's authoritative nameservers (e.g., Cloudflare nameservers)."},
                {"id": "C", "text": "The resolver queries Scaler's authoritative nameserver, which returns the final A/AAAA record (`104.21.48.12`) with a TTL."},
                {"id": "D", "text": "The Root Nameserver responds with the final HTML webpage of Scaler."},
                {"id": "E", "text": "The recursive resolver caches intermediate NS and final A records according to their TTLs to accelerate subsequent queries from other clients."}
            ],
            "correctOptionIds": ["A", "B", "C", "E"],
            "explanation": "Statements A, B, C, and E are correct. The iterative walk progresses: Root $\\rightarrow$ TLD referral (A) $\\rightarrow$ Authoritative referral (B) $\\rightarrow$ Final A record (C). Caching intermediate delegations accelerates future queries (E). D is absurd: Root servers handle DNS delegation records, not HTML web pages.",
            "difficulty": "medium",
            "subtopic": "Global Iterative DNS Resolution Walk"
        },
        {
            "id": "l13-q06",
            "type": "multi_choice",
            "question": "How does the EDNS0 Client Subnet (ECS) extension (RFC 7871) interact with Content Delivery Networks (CDNs) during the DNS resolution phase?",
            "options": [
                {"id": "A", "text": "Without ECS, an authoritative CDN nameserver only sees the IP address of the recursive resolver (e.g., Google 8.8.8.8), potentially returning a server edge location close to the resolver rather than the user."},
                {"id": "B", "text": "With ECS, the recursive resolver includes the client's network prefix (e.g., `/24`) inside the DNS query payload."},
                {"id": "C", "text": "The CDN's authoritative nameserver uses the client's subnet to look up its Anycast Edge topology and returns the IP of the Point of Presence (PoP) nearest to the actual user."},
                {"id": "D", "text": "ECS completely hides the client's existence from the authoritative nameserver by encrypting the DNS query with Tor."},
                {"id": "E", "text": "ECS enables CDNs to deliver lower round-trip latency and higher throughput for client web assets."}
            ],
            "correctOptionIds": ["A", "B", "C", "E"],
            "explanation": "Statements A, B, C, and E are correct. Without ECS, GeoDNS misroutes users if their recursive resolver is geographically distant (A). ECS forwards the user's /24 prefix (B), enabling CDNs to direct the user to the closest edge PoP (C & E). D is false: ECS exposes subnet information, which is why it has privacy implications.",
            "difficulty": "hard",
            "subtopic": "EDNS0 Client Subnet & CDN Geo-Routing"
        },
        {
            "id": "l13-q07",
            "type": "multi_choice",
            "question": "During DNS resolution, if DNSSEC validation is enabled on the recursive resolver, which cryptographic checks are executed to verify the authenticity of `scaler.com`?",
            "options": [
                {"id": "A", "text": "The resolver verifies the `RRSIG` digital signature over the A record RRset using the public Zone-Signing Key (`ZSK`) published in the zone's `DNSKEY` record."},
                {"id": "B", "text": "The resolver verifies the signature over the `DNSKEY` record using the Key-Signing Key (`KSK`)."},
                {"id": "C", "text": "The resolver verifies that a hash of the child zone's KSK matches the Delegation Signer (`DS`) record published by the parent `.com` zone."},
                {"id": "D", "text": "This chain of cryptographic verification continues upward until it reaches the Root Zone Trust Anchor pre-configured in the resolver software."},
                {"id": "E", "text": "DNSSEC decrypts the HTTPS content before the browser sees it."}
            ],
            "correctOptionIds": ["A", "B", "C", "D"],
            "explanation": "Statements A, B, C, and D are correct. DNSSEC authenticates via a strict cryptographic chain of trust: RRSIG verified by ZSK (A), ZSK verified by KSK (B), KSK verified by parent DS record (C), terminating at the Root Trust Anchor (D). E is false: DNSSEC validates DNS records; it has nothing to do with decrypting HTTPS application content.",
            "difficulty": "hard",
            "subtopic": "DNSSEC Cryptographic Chain of Trust"
        },
        {
            "id": "l13-q08",
            "type": "multi_choice",
            "question": "Once the destination IP (`104.21.48.12`) is known, the laptop's OS kernel makes a local routing decision. Which of the following statements are correct?",
            "options": [
                {"id": "A", "text": "The kernel evaluates its local Forwarding Information Base (FIB) and determines that `104.21.48.12` does not belong to the local subnet `192.168.1.0/24`."},
                {"id": "B", "text": "The kernel applies Longest Prefix Match (LPM) and selects the default route: `0.0.0.0/0 via 192.168.1.1 dev wlan0`."},
                {"id": "C", "text": "The kernel checks its ARP cache for the MAC address of the default gateway (`192.168.1.1`)."},
                {"id": "D", "text": "If the gateway's MAC is missing from the ARP cache, the kernel broadcasts an ARP Request (`who-has 192.168.1.1`) and temporarily buffers the outgoing TCP SYN packet."},
                {"id": "E", "text": "The kernel broadcasts an ARP Request across the Internet asking for the MAC address of `104.21.48.12`."}
            ],
            "correctOptionIds": ["A", "B", "C", "D"],
            "explanation": "Statements A, B, C, and D are correct. The kernel determines destination is remote (A), selects default route via 192.168.1.1 (B), checks ARP cache for gateway MAC (C), and buffers packet if an ARP broadcast probe is needed (D). E is false: ARP never crosses router boundaries; the host ARPs for its local default gateway, not the remote public IP.",
            "difficulty": "medium",
            "subtopic": "Host FIB Lookup & Gateway ARP Resolution"
        },
        {
            "id": "l13-q09",
            "type": "multi_choice",
            "question": "As the packet traverses multiple router hops from the client laptop to the server, which of the following rules govern Layer 2 and Layer 3 header encapsulation?",
            "options": [
                {"id": "A", "text": "The Source IP (`192.168.1.5`, prior to NAT) and Destination IP (`104.21.48.12`) remain intact across end-to-end routing."},
                {"id": "B", "text": "At every intermediate router hop, the old Layer 2 Ethernet frame header is stripped, and a new Layer 2 frame header with new Source and Destination MAC addresses is synthesized."},
                {"id": "C", "text": "Each router decrements the IPv4 `TTL` field by at least 1; if TTL reaches 0, the packet is discarded and an `ICMP Type 11, Code 0` (Time Exceeded) message is generated."},
                {"id": "D", "text": "Each router recalculates the IPv4 Header Checksum because the TTL field changed."},
                {"id": "E", "text": "MAC addresses remain unchanged from the laptop all the way to the server."}
            ],
            "correctOptionIds": ["A", "B", "C", "D"],
            "explanation": "Statements A, B, C, and D are foundational principles of packet forwarding. IPs remain end-to-end (A). L2 MAC headers are rebuilt at each hop (B). Routers decrement TTL (C) and recalculate the IPv4 header checksum (D). E is the classic misconception: MAC addresses are strictly hop-local and change at every router.",
            "difficulty": "medium",
            "subtopic": "L2 vs L3 Hop-by-Hop Transformations"
        },
        {
            "id": "l13-q010",
            "type": "multi_choice",
            "question": "When the outgoing packet reaches the home router's WAN interface, which operations are performed by the Network Address and Port Translation (NAPT) engine?",
            "options": [
                {"id": "A", "text": "The private Source IP `192.168.1.5` is rewritten to the router's public WAN IP address (e.g., `203.0.113.45`)."},
                {"id": "B", "text": "The ephemeral Source Port `52410` is mapped to an available port in the router's public pool (e.g., `18204`)."},
                {"id": "C", "text": "A bidirectional state mapping `(192.168.1.5:52410 ⟷ 203.0.113.45:18204 ⟷ 104.21.48.12:443)` is committed to the NAT table."},
                {"id": "D", "text": "The TCP checksum is recomputed because the Source IP and Source Port in the TCP pseudo-header were rewritten."},
                {"id": "E", "text": "The home router drops the packet if it contains TLS encryption."}
            ],
            "correctOptionIds": ["A", "B", "C", "D"],
            "explanation": "Statements A, B, C, and D are correct. NAPT rewrites Source IP (A), maps Source Port (B), stores state for return packets (C), and recomputes the L4 TCP checksum (D). E is false: NAT operates transparently on IP/TCP headers and is oblivious to encrypted payload.",
            "difficulty": "medium",
            "subtopic": "NAPT / PAT Gateway Operations"
        },
        {
            "id": "l13-q011",
            "type": "multi_choice",
            "question": "Across the Internet backbone, which protocols and architectural components guide the packet between the user's ISP and Cloudflare (AS 13335)?",
            "options": [
                {"id": "A", "text": "Within the ISP's internal network, Interior Gateway Protocols (IGP) like OSPF or IS-IS compute shortest paths across core routers."},
                {"id": "B", "text": "At network boundaries, Border Gateway Protocol (BGP-4) exchanges routing information between Autonomous Systems (ASNs)."},
                {"id": "C", "text": "Traffic between ISPs frequently exchanges at Internet Exchange Points (IXPs) via settlement-free peering agreements or paid transit through Tier-1 carriers."},
                {"id": "D", "text": "BGP uses the `AS_PATH` attribute to enforce economic routing policies and guarantee loop-free inter-domain routing."},
                {"id": "E", "text": "The Internet backbone uses a single central computer in Washington D.C. that computes every packet's path in real time."}
            ],
            "correctOptionIds": ["A", "B", "C", "D"],
            "explanation": "Statements A, B, C, and D accurately describe Internet WAN routing. Intra-ISP uses OSPF/IS-IS (A). Inter-AS uses BGP (B). Traffic exchanges at IXPs and Tier-1 transit backbones (C). BGP uses `AS_PATH` to prevent loops and enforce commercial policies (D). E is absurd.",
            "difficulty": "medium",
            "subtopic": "Autonomous Systems & BGP Routing"
        },
        {
            "id": "l13-q012",
            "type": "multi_choice",
            "question": "Cloudflare announces the IP address `104.21.48.12` using BGP Anycast. Which of the following statements regarding Anycast routing are correct?",
            "options": [
                {"id": "A", "text": "The exact same IP prefix (`104.21.48.0/24`) is announced simultaneously from over 300 physical data centers around the world."},
                {"id": "B", "text": "Upstream BGP routers route client packets to the topologically closest data center based on BGP metrics (such as shortest `AS_PATH`)."},
                {"id": "C", "text": "Anycast naturally distributes Distributed Denial of Service (DDoS) attack traffic across hundreds of edge locations, absorbing volumetric floods close to the attack source."},
                {"id": "D", "text": "Anycast requires that every data center worldwide have an identical physical MAC address."},
                {"id": "E", "text": "If a specific Anycast data center goes offline, withdrawing its BGP route advertisement causes global Internet routers to automatically converge to the next-closest healthy data center."}
            ],
            "correctOptionIds": ["A", "B", "C", "E"],
            "explanation": "Statements A, B, C, and E are correct. Anycast announces the same IP from hundreds of locations (A), BGP routes to the topologically closest PoP (B), absorbs DDoS across the edge (C), and provides automatic failover upon BGP route withdrawal (E). D is false: MAC addresses are link-local and have zero relationship with BGP Anycast routing.",
            "difficulty": "hard",
            "subtopic": "BGP Anycast Mechanics"
        },
        {
            "id": "l13-q013",
            "type": "multi_choice",
            "question": "When the client establishes a TCP connection to the server on port 443, which of the following events take place during the TCP Three-Way Handshake?",
            "options": [
                {"id": "A", "text": "The client transmits a TCP segment with `Flags: [SYN]`, an initial sequence number `Seq = X`, and options including MSS (1460), Window Scale, and SACK-Permitted."},
                {"id": "B", "text": "The server replies with `Flags: [SYN, ACK]`, `Seq = Y`, and cumulative acknowledgment `Ack = X + 1`."},
                {"id": "C", "text": "The client completes the handshake by transmitting `Flags: [ACK]`, with `Ack = Y + 1`, transitioning the socket to `ESTABLISHED`."},
                {"id": "D", "text": "In modern TLS 1.3 implementations, the client's final TCP ACK segment can piggyback the TLS `ClientHello` payload in the same physical packet to save time."},
                {"id": "E", "text": "The TCP handshake completes in exactly zero seconds because TCP operates at the speed of sound."}
            ],
            "correctOptionIds": ["A", "B", "C", "D"],
            "explanation": "Statements A, B, C, and D accurately represent modern TCP handshake mechanics. SYN sent with options (A). SYN-ACK received with Ack=X+1 (B). Final ACK establishes connection (C). In TLS 1.3, the client can piggyback its ClientHello on the ACK packet (D). E is absurd.",
            "difficulty": "medium",
            "subtopic": "TCP Handshake & Piggybacking"
        },
        {
            "id": "l13-q014",
            "type": "multi_choice",
            "question": "Which of the following statements accurately characterize the TLS 1.3 Handshake (RFC 8446) compared to legacy TLS 1.2?",
            "options": [
                {"id": "A", "text": "TLS 1.3 completes full cryptographic negotiation, server authentication, and key exchange in exactly **1 RTT** (down from 2 RTTs in TLS 1.2)."},
                {"id": "B", "text": "In the `ClientHello`, the client includes a `Key Share` containing its ephemeral Diffie-Hellman public key (e.g., using curve X25519) alongside supported cipher suites and SNI."},
                {"id": "C", "text": "The server selects a cipher suite (e.g., `TLS_AES_256_GCM_SHA384`), replies with `ServerHello` containing its own `Key Share`, and immediately begins encrypting subsequent handshake messages."},
                {"id": "D", "text": "All handshake messages following `ServerHello` (including the EncryptedExtensions, Server Certificate, CertificateVerify, and Finished) are encrypted under handshake traffic keys."},
                {"id": "E", "text": "TLS 1.3 requires the client to upload its private key to the server for escrow."}
            ],
            "correctOptionIds": ["A", "B", "C", "D"],
            "explanation": "Statements A, B, C, and D are correct. TLS 1.3 cuts handshake latency to 1 RTT (A). Client speculates on curve and sends Key Share in first message (B). Server responds with its Key Share (C) and encrypts all subsequent handshake messages including certificates (D). E is false: Private keys are NEVER shared.",
            "difficulty": "hard",
            "subtopic": "TLS 1.3 1-RTT Handshake Architecture"
        },
        {
            "id": "l13-q015",
            "type": "multi_choice",
            "question": "How does Ephemeral Elliptic Curve Diffie-Hellman (ECDHE) provide **Forward Secrecy** in TLS 1.3?",
            "options": [
                {"id": "A", "text": "Both client and server generate temporary (ephemeral) private scalars ($a$ and $b$) specifically for this unique session and discard them immediately after key derivation."},
                {"id": "B", "text": "Both sides independently compute the identical shared secret point $K = a \\cdot B = b \\cdot A$ on the elliptic curve without ever transmitting the secret across the wire."},
                {"id": "C", "text": "An adversary eavesdropping on the network sees only public points $A$ and $B$, but cannot compute $K$ without solving the Elliptic Curve Discrete Logarithm Problem (ECDLP)."},
                {"id": "D", "text": "Even if the server's long-term RSA/ECDSA private signing key is stolen by an attacker years later, past recorded encrypted sessions CANNOT be decrypted."},
                {"id": "E", "text": "Forward secrecy allows the client to predict the server's future IP addresses."}
            ],
            "correctOptionIds": ["A", "B", "C", "D"],
            "explanation": "Statements A, B, C, and D describe the mathematical foundation of Forward Secrecy. Ephemeral keys are discarded after session derivation (A). Both sides derive the shared secret $K$ via ECDH (B). Eavesdroppers cannot compute $K$ due to the hardness of ECDLP (C). Compromise of the long-term identity certificate does not expose past session keys (D). E is nonsense.",
            "difficulty": "hard",
            "subtopic": "ECDHE Cryptography & Forward Secrecy"
        },
        {
            "id": "l13-q016",
            "type": "multi_choice",
            "question": "Once TLS is established, the application exchanges web data. Compare the transmission mechanics of HTTP/2 vs HTTP/3 (QUIC):",
            "options": [
                {"id": "A", "text": "In HTTP/2, requests and responses are split into binary frames (HEADERS, DATA) multiplexed across independent streams over a single TCP socket."},
                {"id": "B", "text": "HTTP/2 uses HPACK compression to index and compress repeated HTTP header fields."},
                {"id": "C", "text": "In HTTP/2, if a single TCP packet is dropped, all streams stall (TCP Head-of-Line blocking) until the lost packet is retransmitted and acknowledged."},
                {"id": "D", "text": "HTTP/3 runs over QUIC (UDP port 443), where individual streams are truly independent at the transport layer, completely eliminating Head-of-Line blocking."},
                {"id": "E", "text": "HTTP/3 supports 0-RTT connection resumption and connection migration via 64-bit Connection IDs when shifting from Wi-Fi to cellular data."}
            ],
            "correctOptionIds": ["A", "B", "C", "D", "E"],
            "explanation": "ALL FIVE statements (A, B, C, D, and E) are technically correct! HTTP/2 uses binary frames (A) and HPACK (B), but suffers from TCP Head-of-Line blocking upon packet drops (C). HTTP/3 over QUIC uses UDP to provide true stream independence (D), 0-RTT resumption, and Connection ID migration across networks (E).",
            "difficulty": "hard",
            "subtopic": "HTTP/2 vs HTTP/3 QUIC Synthesis"
        },
        {
            "id": "l13-q017",
            "type": "multi_choice",
            "question": "At Cloudflare's Edge Point of Presence (PoP), the incoming request reaches an edge reverse proxy. Which of the following operations take place?",
            "options": [
                {"id": "A", "text": "The Edge server terminates the client's TCP connection and TLS session (SSL Offloading)."},
                {"id": "B", "text": "The proxy inspects the request path and query parameters against its edge cache (Cache Hit vs. Cache Miss)."},
                {"id": "C", "text": "On a cache miss, the proxy forwards the request over a persistent backend tunnel to Scaler's origin infrastructure."},
                {"id": "D", "text": "The proxy injects provenance headers, including `X-Forwarded-For: <Client_Public_IP>` and `X-Forwarded-Proto: https`, so backend services know the real client identity."},
                {"id": "E", "text": "The reverse proxy permanently deletes the user's hard drive."}
            ],
            "correctOptionIds": ["A", "B", "C", "D"],
            "explanation": "Statements A, B, C, and D represent standard edge reverse proxy architecture. The proxy terminates TLS (A), checks edge cache (B), forwards cache misses to origin (C), and enriches headers with `X-Forwarded-For` and `X-Forwarded-Proto` (D). E is absurd.",
            "difficulty": "medium",
            "subtopic": "Edge Reverse Proxy & Header Enrichment"
        },
        {
            "id": "l13-q018",
            "type": "multi_choice",
            "question": "Inside the origin data center, the request enters a Kubernetes cluster. Which of the following components participate in fulfilling the request?",
            "options": [
                {"id": "A", "text": "An Ingress Controller (e.g., Envoy or NGINX) terminates origin TLS and routes traffic based on Layer 7 path rules (`/courses`)."},
                {"id": "B", "text": "A Service Mesh sidecar proxy (e.g., Istio Envoy) handles internal mutual TLS (mTLS), observability tracing, and traffic routing to target application pods."},
                {"id": "C", "text": "The application pod queries an in-memory distributed cache (Redis / Memcached) for course metadata, achieving sub-millisecond read latency on cache hits."},
                {"id": "D", "text": "On cache misses, the application executes parameterized SQL queries against a primary/replica relational database (e.g., PostgreSQL)."},
                {"id": "E", "text": "Kubernetes requires that all database tables be written in raw binary assembly language."}
            ],
            "correctOptionIds": ["A", "B", "C", "D"],
            "explanation": "Statements A, B, C, and D accurately represent modern containerized microservice architectures. Ingress routes by L7 path (A). Service mesh provides mTLS and tracing (B). Redis provides fast cache hits (C), with PostgreSQL handling durable queries on miss (D). E is false.",
            "difficulty": "medium",
            "subtopic": "Kubernetes Ingress & Microservice Plumbing"
        },
        {
            "id": "l13-q019",
            "type": "multi_choice",
            "question": "As response bytes return to the client browser, which of the following stages occur during the Critical Rendering Path?",
            "options": [
                {"id": "A", "text": "The browser kernel reconstructs the in-order byte stream via TCP reassembly and decrypts TLS records using hardware AES-NI instructions."},
                {"id": "B", "text": "The browser decompressor decodes the compressed HTML byte stream (e.g., Brotli or gzip)."},
                {"id": "C", "text": "The HTML tokenizer incrementally parses tags, constructing the Document Object Model (DOM) tree."},
                {"id": "D", "text": "External stylesheets are fetched and parsed into the CSS Object Model (CSSOM) tree; DOM and CSSOM are merged to construct the Render Tree."},
                {"id": "E", "text": "The browser executes Layout (calculating box geometry) and Paint/Composite, rasterizing pixels onto GPU surfaces."}
            ],
            "correctOptionIds": ["A", "B", "C", "D", "E"],
            "explanation": "ALL FIVE statements (A, B, C, D, and E) accurately trace the client rendering pipeline! TCP reassembly & TLS decryption (A), Brotli decompression (B), HTML tokenization to DOM (C), CSSOM generation & Render Tree assembly (D), and Layout/Paint/Composite to screen pixels (E).",
            "difficulty": "hard",
            "subtopic": "Critical Rendering Path & HTML Pipeline"
        },
        {
            "id": "l13-q020",
            "type": "multi_choice",
            "question": "When the user closes the browser tab or the server keep-alive idle timer expires, which of the following actions gracefully terminate the session?",
            "options": [
                {"id": "A", "text": "The client initiates a 4-Way TCP connection teardown by transmitting a segment with the `FIN` control flag set."},
                {"id": "B", "text": "The server acknowledges the client's FIN with an `ACK`, entering the `CLOSE_WAIT` state while the client enters `FIN_WAIT_2`."},
                {"id": "C", "text": "The server closes its half of the connection by transmitting its own `FIN`, which the client acknowledges with a final `ACK`."},
                {"id": "D", "text": "The client enters the `TIME_WAIT` state for $2\\text{MSL} = 60\\text{ seconds}$ to ensure late-arriving packets dissipate and the final ACK was reliably delivered."},
                {"id": "E", "text": "The home router's stateful NAT table cleans up and reaps the ephemeral port mapping entry."}
            ],
            "correctOptionIds": ["A", "B", "C", "D", "E"],
            "explanation": "ALL FIVE statements (A, B, C, D, and E) are correct! Active close starts with FIN (A). Server replies with ACK entering CLOSE_WAIT (B). Server sends FIN, client ACKs (C). Initiator waits in TIME_WAIT for 2MSL (D). Router NAT table entry is reaped (E).",
            "difficulty": "hard",
            "subtopic": "Connection Teardown & Lifecycle Completion"
        }
    ]
}
