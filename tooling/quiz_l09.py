"""
Lecture 09 Quiz: DNS & Internet Applications
20 Advanced Multi-Correct MCQs (5 options each, 2 to 5 correct answers)
"""

QUIZ_L09 = {
    "topicId": "lecture-09",
    "lectureNumber": 9,
    "title": "DNS & Internet Applications Master Quiz",
    "description": "20 rigorous multi-correct questions covering DNS binary headers, zone apex CNAME constraints, Kaminsky cache poisoning, DNSSEC cryptographic chains, DoT/DoH, EDNS0, HTTP/1.1 vs HTTP/2 vs HTTP/3, and web security headers.",
    "estimatedMinutes": 35,
    "questions": [
        {
            "id": "l09-q01",
            "type": "multi_choice",
            "question": "Which of the following statements regarding the global DNS root architecture and query resolution models are correct?",
            "options": [
                {"id": "A", "text": "The 13 logical root server identities (a.root-servers.net to m.root-servers.net) are announced via BGP Anycast from over 1,700 physical instances across the globe."},
                {"id": "B", "text": "In a recursive query, the contacted server assumes the burden of iteratively walking the DNS hierarchy until the final answer or an error is returned to the client."},
                {"id": "C", "text": "If a recursive resolver at 8.8.8.8 becomes unreachable, the client OS stub resolver automatically assumes the iterative resolution burden and walks root servers directly."},
                {"id": "D", "text": "Root nameservers do not hold authoritative records for second-level domain names like scaler.com; they return referrals to the appropriate Top-Level Domain (TLD) nameservers."},
                {"id": "E", "text": "In an iterative query, if the queried server does not know the answer, it returns a delegation pointing to another nameserver lower in the hierarchy."}
            ],
            "correctOptionIds": ["A", "B", "D", "E"],
            "explanation": "Statements A, B, D, and E are correct. A: BGP Anycast broadcasts the 13 logical IP addresses from hundreds of locations. B: A recursive query delegates full resolution to the resolver. D: Root servers only maintain delegations to TLD nameservers (and glue records). E: Iterative queries return referrals (delegations). C is false: Standard OS stub resolvers (like Linux getaddrinfo or Windows DNS Client) lack iterative walk logic; if their configured recursive resolver fails, resolution fails unless an alternative resolver IP is configured.",
            "difficulty": "hard",
            "subtopic": "DNS Hierarchy & Resolution"
        },
        {
            "id": "l09-q02",
            "type": "multi_choice",
            "question": "In the 12-byte fixed binary DNS message header (RFC 1035), which of the following bitfields and their interpretations are correct?",
            "options": [
                {"id": "A", "text": "The `QR` (Query/Response) bit is set to 0 for a query and set to 1 for a response."},
                {"id": "B", "text": "The `AA` (Authoritative Answer) bit is only valid in responses and indicates that the responding server is authoritative for the queried domain zone."},
                {"id": "C", "text": "The `TC` (Truncation) bit is set when the response length exceeds the transport limit (512 bytes for classical UDP), prompting the client to retry over TCP."},
                {"id": "D", "text": "The `RD` (Recursion Desired) bit is set by the authoritative nameserver to indicate that it resolved the query recursively on behalf of the client."},
                {"id": "E", "text": "An `RCODE` of 3 indicates `NXDOMAIN` (Non-Existent Domain), signifying that the domain name does not exist according to the authoritative server."}
            ],
            "correctOptionIds": ["A", "B", "C", "E"],
            "explanation": "Statements A, B, C, and E are correct. A: QR=0 query, QR=1 response. B: AA=1 proves the answer came from an authoritative source, not a cached relay. C: TC=1 signals UDP packet truncation (>512 bytes without EDNS0), instructing the client to fall back to TCP port 53. E: RCODE 3 is NXDOMAIN. D is false: The RD bit is set by the *client* in the query to request recursion; the server indicates whether recursion was provided using the `RA` (Recursion Available) bit.",
            "difficulty": "hard",
            "subtopic": "DNS Header Anatomy"
        },
        {
            "id": "l09-q03",
            "type": "multi_choice",
            "question": "According to RFC 1034 / RFC 2181, why can a CNAME record NOT coexist with other record types at the zone apex (`scaler.com`), and how do modern DNS providers work around this limitation?",
            "options": [
                {"id": "A", "text": "A CNAME record mandates that no other record type (such as SOA, NS, or MX) can exist for that exact node name."},
                {"id": "B", "text": "Because the zone apex must contain SOA and NS records to be a valid DNS zone, placing a CNAME at the apex violates RFC specifications."},
                {"id": "C", "text": "Cloudflare and Route 53 implement synthetic proprietary records (e.g., CNAME Flattening, ANAME, or ALIAS) that resolve the target dynamically and serve synthesized A/AAAA records at the apex."},
                {"id": "D", "text": "CNAME records at the apex are forbidden because BGP routers cannot parse text strings during FIB lookup."},
                {"id": "E", "text": "If an apex had a CNAME and an MX record, mail delivery servers might look up the CNAME target and deliver mail to the wrong host entirely."}
            ],
            "correctOptionIds": ["A", "B", "C", "E"],
            "explanation": "Statements A, B, C, and E are correct. RFC 1034 Section 3.6.2 dictates that if a CNAME exists at a node, no other data may exist at that node. Because every zone apex MUST have SOA and NS records, a standard CNAME cannot legally exist at the apex (A and B). Modern DNS providers bypass this using CNAME Flattening / ALIAS records, where the nameserver queries the canonical alias on the backend and returns synthesized A/AAAA records to the client (C). Without this, mail lookups for the apex would follow the CNAME instead of evaluating MX records (E). D is false because BGP operates at Layer 3 and does not process DNS records.",
            "difficulty": "hard",
            "subtopic": "Zone Apex & CNAME Mechanics"
        },
        {
            "id": "l09-q04",
            "type": "multi_choice",
            "question": "Which of the following are technically accurate regarding reverse DNS lookups and PTR records?",
            "options": [
                {"id": "A", "text": "For IPv4 address `192.0.2.45`, the corresponding reverse DNS query domain is `45.2.0.192.in-addr.arpa`."},
                {"id": "B", "text": "The octets are reversed because DNS trees are evaluated from right to left (broadest to narrowest), whereas IP addresses are written from left to right (network to host)."},
                {"id": "C", "text": "For IPv6 addresses, PTR lookups reverse every individual hexadecimal nibble (separated by dots) under the `ip6.arpa` domain."},
                {"id": "D", "text": "SMTP mail transfer agents (MTAs) frequently reject incoming email if the sender's IP address does not have a matching valid reverse PTR record (Forward-Confirmed reverse DNS)."},
                {"id": "E", "text": "A PTR record query is handled directly by the client's local ARP cache without making network requests."}
            ],
            "correctOptionIds": ["A", "B", "C", "D"],
            "explanation": "Statements A, B, C, and D are correct. A & B: IPv4 reverse lookups reverse octets under `in-addr.arpa` so hierarchical DNS delegation matches IP subnetting. C: IPv6 reverses each 4-bit nibble under `ip6.arpa`. D: FCrDNS is a foundational anti-spam mechanism used by major mail providers (Gmail, Outlook). E is false: ARP maps IP to MAC at Layer 2 on a local broadcast domain, whereas PTR is a Layer 7 DNS query traversing the global DNS tree.",
            "difficulty": "medium",
            "subtopic": "Reverse DNS & PTR Records"
        },
        {
            "id": "l09-q05",
            "type": "multi_choice",
            "question": "Team A configures a DNS TTL of 30 seconds for `api.scaler.com`, while Team B configures a TTL of 86400 seconds (1 day) for `docs.scaler.com`. Which of the following consequences are true?",
            "options": [
                {"id": "A", "text": "When Team A migrates their API to a new public IP, the vast majority of clients worldwide will discover the new IP address within ~30 seconds."},
                {"id": "B", "text": "Team B's authoritative nameservers will experience significantly lower query volume than Team A's nameservers for an equivalent number of active users."},
                {"id": "C", "text": "Team B's web visitors will suffer slower page load times on every repeat visit because of the high TTL."},
                {"id": "D", "text": "If Team B suffers a catastrophic server failure and updates their DNS record, many clients will continue attempting to connect to the dead IP address for up to 24 hours."},
                {"id": "E", "text": "The DNS TTL directly dictates how long the client's browser maintains its TCP socket in the ESTABLISHED state."}
            ],
            "correctOptionIds": ["A", "B", "D"],
            "explanation": "Statements A, B, and D are correct. A low TTL allows rapid failover and IP migration (A), but generates massive query load on authoritative nameservers (B). A high TTL caches answers extensively, making emergency migrations slow to propagate (D). C is false: High TTL improves client performance on repeat visits because cached DNS lookups take 0 ms. E is false: DNS TTL governs caching of the name-to-IP binding; it has zero relationship with TCP Keep-Alive or socket lifecycle.",
            "difficulty": "medium",
            "subtopic": "DNS TTL & Caching Dynamics"
        },
        {
            "id": "l09-q06",
            "type": "multi_choice",
            "question": "In the landmark Dan Kaminsky DNS Cache Poisoning attack (2008), how did the attacker overcome the historical limitations of traditional DNS spoofing?",
            "options": [
                {"id": "A", "text": "The attacker queried pseudo-random nonexistent subdomains (e.g., `random123.target.com`) to guarantee recursive cache misses on every attempt."},
                {"id": "B", "text": "Because each query was for a unique name, the target resolver immediately forwarded an iterative query upstream, eliminating the need to wait for the TTL to expire."},
                {"id": "C", "text": "The attacker flooded the resolver with forged responses containing a guessed 16-bit Transaction ID along with malicious NS delegation records in the Authority section."},
                {"id": "D", "text": "Once a forged response matching the Transaction ID was accepted, the resolver cached the attacker's nameserver as authoritative for the entire `target.com` zone."},
                {"id": "E", "text": "The attack succeeded by cracking the RSA-4096 private key of the ICANN Root Zone."}
            ],
            "correctOptionIds": ["A", "B", "C", "D"],
            "explanation": "Statements A, B, C, and D accurately describe Kaminsky DNS cache poisoning. Prior to Kaminsky, attackers had to wait for a cached record's TTL to expire before attempting to spoof it. Kaminsky queried nonexistent names (`rand1.bank.com`, `rand2.bank.com`), triggering continuous iterative upstream queries while flooding forged responses with candidate Transaction IDs and fake Authority/Additional NS glue records (A, B, C). Winning the race poisoned the entire domain delegation (D). E is completely false; DNS at the time was unencrypted and unsigned, requiring no cryptographic cracking.",
            "difficulty": "hard",
            "subtopic": "Kaminsky DNS Cache Poisoning"
        },
        {
            "id": "l09-q07",
            "type": "multi_choice",
            "question": "Which of the following mechanisms serve as direct defensive countermeasures against DNS Cache Poisoning attacks?",
            "options": [
                {"id": "A", "text": "Source Port Randomization (SPR): Randomizing the client UDP source port across ~64,000 ephemeral ports increases the attacker's search space from $2^{16}$ to $\\approx 2^{32}$ combinations."},
                {"id": "B", "text": "DNS Bailiwick Rules: Resolvers strictly reject out-of-domain records (e.g., rejecting an authoritative NS record for `bank.com` returned by a nameserver authoritative only for `attacker.com`)."},
                {"id": "C", "text": "0x20 Bit Encoding: Randomizing upper and lower case letters in the queried domain name (e.g., `sCaLeR.cOm`) and requiring the response to mirror the exact casing."},
                {"id": "D", "text": "Deploying DNSSEC to cryptographically sign resource record sets with digital signatures."},
                {"id": "E", "text": "Increasing the Ethernet MTU to 9000 bytes to force all DNS queries over IPv6."}
            ],
            "correctOptionIds": ["A", "B", "C", "D"],
            "explanation": "Statements A, B, C, and D are authentic defensive measures against DNS cache poisoning. SPR (RFC 5452) combines a 16-bit Transaction ID with ~16 bits of ephemeral port entropy, requiring $\\approx 4\\text{ billion}$ spoofed packets to win (A). Bailiwick rules prevent rogue delegations (B). 0x20 encoding adds entropy via case preservation (C). DNSSEC provides unforgeable cryptographic authenticity (D). E is irrelevant and unrelated to DNS security.",
            "difficulty": "hard",
            "subtopic": "DNS Spoofing Countermeasures"
        },
        {
            "id": "l09-q08",
            "type": "multi_choice",
            "question": "Which of the following statements correctly describe the cryptographic architecture of DNSSEC (RFC 4033 - RFC 4035)?",
            "options": [
                {"id": "A", "text": "DNSSEC encrypts DNS query and response payloads so that on-path eavesdroppers cannot inspect domain names."},
                {"id": "B", "text": "Resource Record Sets (RRsets) of the same name and type are bundled together and digitally signed with a Zone-Signing Key (ZSK) to produce an `RRSIG` record."},
                {"id": "C", "text": "The public Zone-Signing Key (ZSK) is signed by the Key-Signing Key (KSK) within the zone's `DNSKEY` record."},
                {"id": "D", "text": "A cryptographic hash of the child zone's public KSK is published in the parent zone as a Delegation Signer (`DS`) record, establishing the chain of trust."},
                {"id": "E", "text": "The Root Zone KSK serves as the global Trust Anchor pre-configured into validating recursive resolvers."}
            ],
            "correctOptionIds": ["B", "C", "D", "E"],
            "explanation": "Statements B, C, D, and E are correct. DNSSEC secures integrity and authentication via a hierarchical chain of trust: RRsets are signed by ZSK to create RRSIG (B); ZSK is signed by KSK (C); parent zones store the DS hash of the child KSK (D); the Root KSK is the Trust Anchor (E). A is completely false: DNSSEC does NOT provide confidentiality or encryption; DNS payloads remain in plaintext.",
            "difficulty": "hard",
            "subtopic": "DNSSEC Architecture"
        },
        {
            "id": "l09-q09",
            "type": "multi_choice",
            "question": "How do NSEC and NSEC3 records solve the problem of 'Authenticated Denial of Existence' in DNSSEC without requiring online private key signing for every nonexistent domain?",
            "options": [
                {"id": "A", "text": "An `NSEC` record defines a signed range asserting that no names exist lexicographically between two existing domain records (e.g., asserting no record exists between `alpha.example.com` and `charlie.example.com`)."},
                {"id": "B", "text": "A major vulnerability of classical `NSEC` is 'Zone Walking', which allows adversaries to enumerate every subdomain in a private zone simply by following consecutive NSEC links."},
                {"id": "C", "text": "An `NSEC3` record prevents zone enumeration by hashing domain names using salted iterations of SHA-1 before creating the signed range."},
                {"id": "D", "text": "NSEC records automatically decrypt TLS traffic passing through recursive resolvers."},
                {"id": "E", "text": "Both NSEC and NSEC3 allow validating resolvers to cryptographically verify that an `NXDOMAIN` response was genuinely authorized by the zone owner."}
            ],
            "correctOptionIds": ["A", "B", "C", "E"],
            "explanation": "Statements A, B, C, and E are correct. Because nameservers cannot sign non-existent names offline in advance, NSEC provides signed spans of lexicographical gaps (A). However, this permits zone walking (B). NSEC3 mitigates zone walking by hashing domain names (C). Validating resolvers verify NXDOMAIN authenticity using these signed proofs (E). D is nonsense.",
            "difficulty": "hard",
            "subtopic": "DNSSEC Authenticated Denial of Existence"
        },
        {
            "id": "l09-q10",
            "type": "multi_choice",
            "question": "Compare DNS over TLS (DoT - RFC 7858) and DNS over HTTPS (DoH - RFC 8484). Which of the following statements are technically accurate?",
            "options": [
                {"id": "A", "text": "DoT runs over dedicated TCP port 853, making it straightforward for enterprise firewalls to inspect, permit, or block."},
                {"id": "B", "text": "DoH encapsulates DNS queries inside HTTP/2 or HTTP/3 streams over standard TCP/UDP port 443, making it blend seamlessly with regular encrypted web traffic."},
                {"id": "C", "text": "Both DoT and DoH provide end-to-end transport confidentiality and integrity, preventing local network eavesdroppers from viewing queried domains."},
                {"id": "D", "text": "Neither DoT nor DoH prevents the upstream recursive resolver (e.g., Cloudflare or Google) from logging client queries."},
                {"id": "E", "text": "DoT eliminates the need for TCP handshakes by operating exclusively over raw ICMP."}
            ],
            "correctOptionIds": ["A", "B", "C", "D"],
            "explanation": "Statements A, B, C, and D are correct. DoT operates on port 853 (A), while DoH blends over port 443 (B). Both encrypt the last mile between client and resolver, preventing local sniffing/tampering (C), but the upstream resolver itself still sees all queries in plaintext unless Oblivious DoH (ODoH) is deployed (D). E is false; DoT uses TCP and TLS.",
            "difficulty": "medium",
            "subtopic": "Encrypted DNS: DoT & DoH"
        },
        {
            "id": "l09-q11",
            "type": "multi_choice",
            "question": "Which of the following are true regarding the EDNS0 Client Subnet (ECS) extension (RFC 7871)?",
            "options": [
                {"id": "A", "text": "ECS enables recursive resolvers to append the client's network prefix (typically a /24 for IPv4 or /56 for IPv6) to the query sent to authoritative nameservers."},
                {"id": "B", "text": "Authoritative nameservers for CDNs use ECS data to return an Anycast or Edge IP address topologically closest to the client rather than the resolver."},
                {"id": "C", "text": "ECS completely resolves all privacy concerns because it replaces the client's MAC address with a random UUID."},
                {"id": "D", "text": "ECS reduces the cache efficiency of public recursive resolvers because identical queries from clients on different subnets generate separate cached entries."},
                {"id": "E", "text": "ECS operates as an option inside an OPT pseudo-resource record, expanding standard DNS capabilities without breaking backward compatibility."}
            ],
            "correctOptionIds": ["A", "B", "D", "E"],
            "explanation": "Statements A, B, D, and E are correct. ECS transmits client subnet prefixes to authoritative nameservers (A), allowing CDNs to optimize routing for the user instead of the resolver's location (B). However, this increases cache fragmentation on resolvers (D) and introduces privacy trade-offs. ECS utilizes the EDNS0 OPT record (E). C is false; ECS transmits IP prefix information, which actually raises privacy concerns rather than eliminating them.",
            "difficulty": "hard",
            "subtopic": "EDNS0 Client Subnet (ECS)"
        },
        {
            "id": "l09-q12",
            "type": "multi_choice",
            "question": "A Start of Authority (SOA) record contains several critical timing parameters. Which of the following mappings and behavioral rules are correct?",
            "options": [
                {"id": "A", "text": "`Serial`: A revision number that secondary nameservers compare against their local copy; an incremented serial triggers zone transfer (AXFR/IXFR)."},
                {"id": "B", "text": "`Refresh`: The interval at which secondary nameservers poll the primary nameserver to inspect the serial number."},
                {"id": "C", "text": "`Retry`: The time a secondary nameserver waits before re-attempting a failed zone refresh."},
                {"id": "D", "text": "`Minimum TTL`: Under RFC 2308, this field defines the duration that downstream resolvers may cache a negative response (NXDOMAIN / NODATA)."},
                {"id": "E", "text": "`Expire`: The time after which a secondary nameserver drops its cached zone records if it cannot establish contact with the primary."}
            ],
            "correctOptionIds": ["A", "B", "C", "D", "E"],
            "explanation": "ALL FIVE statements (A, B, C, D, and E) are technically correct! The SOA record governs secondary zone replication and negative caching. Serial tracks versions (A), Refresh sets polling cadence (B), Retry dictates retry timing on failure (C), Minimum TTL dictates RFC 2308 negative caching (D), and Expire dictates when secondary zone data becomes invalid if primary remains unreachable (E).",
            "difficulty": "hard",
            "subtopic": "SOA Record Anatomy"
        },
        {
            "id": "l09-q13",
            "type": "multi_choice",
            "question": "Which of the following are valid rules regarding DNS Mail Exchange (MX) records?",
            "options": [
                {"id": "A", "text": "Each MX record contains a numeric preference value (priority); lower numeric values indicate higher priority."},
                {"id": "B", "text": "An MX record must point directly to a canonical domain name with an A or AAAA record, NOT directly to an IP address or a CNAME alias."},
                {"id": "C", "text": "If two MX records have identical priority values, sending mail servers must perform round-robin or randomized load sharing between them."},
                {"id": "D", "text": "Higher numeric priority MX records are contacted first, and lower numbers serve strictly as fallbacks."},
                {"id": "E", "text": "If a domain has no MX record, sending MTAs fall back to querying the domain's A record directly."}
            ],
            "correctOptionIds": ["A", "B", "C", "E"],
            "explanation": "Statements A, B, C, and E are correct. A & D: Lower numbers have higher priority (e.g., priority 10 is preferred over priority 20; D is false). B: RFC 2181 Section 10.3 mandates MX targets must point to domain names with A/AAAA records, never CNAMEs or raw IPs. C: Equal priority values share traffic. E: Standard SMTP fallback attempts delivery to the domain's A record if no MX records exist.",
            "difficulty": "medium",
            "subtopic": "MX Record Protocol Rules"
        },
        {
            "id": "l09-q14",
            "type": "multi_choice",
            "question": "Which of the following security mechanisms utilize DNS TXT records to authenticate and protect email domains?",
            "options": [
                {"id": "A", "text": "Sender Policy Framework (SPF): Lists authorized IP addresses and subnets permitted to send email on behalf of the domain (e.g., `v=spf1 ip4:198.51.100.0/24 -all`)."},
                {"id": "B", "text": "DomainKeys Identified Mail (DKIM): Publishes the sender's public cryptographic key under a selector subdomain so receiving MTAs can verify digital signatures on email headers."},
                {"id": "C", "text": "Domain-based Message Authentication, Reporting, and Conformance (DMARC): Specifies enforcement policies (`p=reject`, `p=quarantine`) when SPF or DKIM alignment checks fail."},
                {"id": "D", "text": "Certificate Authority Authorization (CAA): Published as TXT records to specify which CAs can issue SSL certificates."},
                {"id": "E", "text": "Google Site Verification: Proves administrative ownership of a domain to search engines and cloud platforms via arbitrary verification tokens."}
            ],
            "correctOptionIds": ["A", "B", "C", "E"],
            "explanation": "Statements A, B, C, and E are correct. SPF, DKIM, and DMARC form the email authentication triad and all use DNS TXT records (A, B, C). Domain verification tokens also rely on TXT records (E). D is false: While CAA governs certificate issuance, it has its own dedicated DNS Resource Record type (Type 257 - CAA), not a TXT record.",
            "difficulty": "medium",
            "subtopic": "TXT Records & Email Security"
        },
        {
            "id": "l09-q15",
            "type": "multi_choice",
            "question": "Which major architectural enhancements were introduced in HTTP/1.1 (RFC 2616 / RFC 7230) compared to legacy HTTP/1.0?",
            "options": [
                {"id": "A", "text": "Mandatory `Host` header: Allows multiple virtual hosts with distinct domain names to share a single public IP address."},
                {"id": "B", "text": "Persistent Connections (`Connection: keep-alive` by default): Allows multiple HTTP request/response cycles over a single underlying TCP connection."},
                {"id": "C", "text": "Chunked Transfer Encoding (`Transfer-Encoding: chunked`): Allows streaming dynamically generated responses without knowing the `Content-Length` upfront."},
                {"id": "D", "text": "Binary framing layer that splits messages into interleaved frames with 31-bit stream identifiers."},
                {"id": "E", "text": "Pipelining: Allowing clients to send multiple requests without waiting for intermediate responses (though limited by Head-of-Line blocking)."}
            ],
            "correctOptionIds": ["A", "B", "C", "E"],
            "explanation": "Statements A, B, C, and E are hallmark features introduced in HTTP/1.1. Host headers enabled modern multi-tenant virtual hosting (A). Keep-Alive became default (B). Chunked transfer enabled dynamic streaming (C). Pipelining was introduced (E). D is false: Binary framing with interleaved stream identifiers was introduced in HTTP/2, not HTTP/1.1.",
            "difficulty": "medium",
            "subtopic": "HTTP/1.1 Core Enhancements"
        },
        {
            "id": "l09-q16",
            "type": "multi_choice",
            "question": "How does HTTP/2 (RFC 7540 / RFC 9113) fundamentally overcome the application-layer limitations of HTTP/1.1?",
            "options": [
                {"id": "A", "text": "It introduces a binary framing layer, breaking communication into discrete frames (e.g., HEADERS, DATA, SETTINGS, RST_STREAM)."},
                {"id": "B", "text": "It multiplexes multiple independent bidirectional streams concurrently over a single TCP connection, eliminating application-layer Head-of-Line blocking."},
                {"id": "C", "text": "It compresses header fields using HPACK, maintaining static and dynamic indexing tables between client and server to eliminate redundant header transmission."},
                {"id": "D", "text": "It replaces TCP with UDP at the transport layer to eliminate transport packet loss."},
                {"id": "E", "text": "It supports stream prioritization and server push, allowing servers to send critical assets before the client explicitly parses and requests them."}
            ],
            "correctOptionIds": ["A", "B", "C", "E"],
            "explanation": "Statements A, B, C, and E are correct. HTTP/2 uses binary framing (A), multiplexes streams across a single TCP socket (B), compresses headers via HPACK (C), and supports stream dependencies and server push (E). D is false: HTTP/2 still runs strictly over TCP; replacing TCP with UDP is the defining innovation of HTTP/3 (QUIC).",
            "difficulty": "hard",
            "subtopic": "HTTP/2 Binary Framing & Multiplexing"
        },
        {
            "id": "l09-q17",
            "type": "multi_choice",
            "question": "Despite HTTP/2's application-layer multiplexing, what transport-layer limitations motivated the development of HTTP/3 over QUIC (RFC 9000 / RFC 9114)?",
            "options": [
                {"id": "A", "text": "TCP Head-of-Line (HoL) Blocking: If a single TCP segment is dropped on a lossy connection, the kernel TCP stack stalls ALL interleaved HTTP/2 streams until the missing segment is retransmitted."},
                {"id": "B", "text": "Slow Connection Establishment: Establishing an HTTPS session over TCP requires 1 RTT for TCP SYN/ACK plus 1 RTT for TLS 1.3 (total 2 RTTs), whereas QUIC completes transport and cryptographic negotiation in 1 RTT (or 0-RTT)."},
                {"id": "C", "text": "Connection Migration: When a mobile device shifts between Wi-Fi and 5G cellular, its IP address changes; TCP drops the connection, whereas QUIC uses a 64-bit Connection ID to persist the session without interruption."},
                {"id": "D", "text": "Middlebox Ossification: Routers and firewalls that drop unknown TCP options or interfere with TCP headers can be bypassed because QUIC encapsulates its transport state entirely inside encrypted UDP payloads."},
                {"id": "E", "text": "QUIC eliminates the need for congestion control algorithms, allowing clients to send unlimited data without packet drops."}
            ],
            "correctOptionIds": ["A", "B", "C", "D"],
            "explanation": "Statements A, B, C, and D accurately summarize the engineering imperatives behind QUIC and HTTP/3. TCP packet loss stalls all multiplexed streams at the kernel layer (A). TCP+TLS handshakes require sequential round-trips (B). IP changes break TCP 4-tuples, while QUIC Connection IDs survive network changes (C). UDP encapsulation evades legacy middlebox tampering (D). E is completely false: QUIC implements robust congestion control (Cubic, BBR, NewReno) in userspace.",
            "difficulty": "hard",
            "subtopic": "HTTP/3 & QUIC Protocol Imperatives"
        },
        {
            "id": "l09-q18",
            "type": "multi_choice",
            "question": "Which of the following statements regarding HTTP Cookie security attributes are technically correct?",
            "options": [
                {"id": "A", "text": "The `HttpOnly` flag prevents client-side scripts from reading the cookie via `document.cookie`, mitigating credential theft via Cross-Site Scripting (XSS)."},
                {"id": "B", "text": "The `Secure` flag instructs the browser to transmit the cookie only over encrypted connections (HTTPS), preventing transmission over plaintext HTTP."},
                {"id": "C", "text": "`SameSite=Strict` blocks the cookie from being sent on any cross-site request, even when a user clicks an external link navigating to the target website."},
                {"id": "D", "text": "`SameSite=Lax` allows the cookie to be sent on top-level safe GET navigations initiated from external sites, while blocking it on cross-site POST requests to defend against CSRF."},
                {"id": "E", "text": "Setting `SameSite=None` automatically enables end-to-end RSA encryption of the cookie payload."}
            ],
            "correctOptionIds": ["A", "B", "C", "D"],
            "explanation": "Statements A, B, C, and D are correct. `HttpOnly` blocks JavaScript DOM access (A). `Secure` mandates HTTPS (B). `SameSite=Strict` suppresses the cookie on all cross-origin requests including link clicks (C). `SameSite=Lax` allows safe top-level GET navigations while preventing CSRF on state-changing requests (D). E is false: `SameSite=None` simply allows third-party cross-site transmission (and requires the `Secure` flag in modern browsers); it does not encrypt the cookie body.",
            "difficulty": "medium",
            "subtopic": "HTTP Cookie Security Attributes"
        },
        {
            "id": "l09-q19",
            "type": "multi_choice",
            "question": "Which of the following statements accurately characterize HTTP caching directives and conditional validation mechanisms?",
            "options": [
                {"id": "A", "text": "`Cache-Control: no-cache` does NOT mean 'do not cache'; it means the client/proxy may cache the response, but MUST revalidate with the origin server before serving it."},
                {"id": "B", "text": "`Cache-Control: no-store` strictly forbids any cache (browser or intermediate proxy) from storing any part of the request or response on disk or memory."},
                {"id": "C", "text": "An `ETag` (Entity Tag) acts as a content fingerprint; clients transmit it back in the `If-None-Match` header to perform conditional validation."},
                {"id": "D", "text": "When a conditional GET validation succeeds (the content has not changed), the origin server replies with `304 Not Modified` and transmits zero body payload bytes."},
                {"id": "E", "text": "The `Expires` header takes strict mathematical precedence over the `Cache-Control: max-age` directive in modern HTTP/1.1 and HTTP/2 clients."}
            ],
            "correctOptionIds": ["A", "B", "C", "D"],
            "explanation": "Statements A, B, C, and D are correct. A: `no-cache` forces revalidation. B: `no-store` bans caching entirely for sensitive data. C: ETags enable conditional requests via `If-None-Match`. D: 304 Not Modified returns headers only with empty body, saving bandwidth. E is false: RFC 7234 Section 5.3 explicitly states that `Cache-Control: max-age` completely overrides `Expires`.",
            "difficulty": "medium",
            "subtopic": "HTTP Caching & Conditional Revalidation"
        },
        {
            "id": "l09-q20",
            "type": "multi_choice",
            "question": "Which of the following statements regarding modern web performance, TLS termination, and application architecture are true?",
            "options": [
                {"id": "A", "text": "Server Name Indication (SNI) is an extension to the TLS protocol that includes the target hostname in the ClientHello message, allowing one server IP to host multiple TLS certificates."},
                {"id": "B", "text": "Encrypted Client Hello (ECH) encrypts the SNI extension using a public key published in the domain's DNS `HTTPS` / `SVCB` resource record, preventing network eavesdroppers from discovering the destination domain."},
                {"id": "C", "text": "HTTP Strict Transport Security (HSTS) preload lists compiled into web browsers eliminate the initial unencrypted HTTP redirect, mitigating SSL-stripping attacks."},
                {"id": "D", "text": "SSL Offloading at an edge load balancer decrypts incoming TLS traffic, allowing backend application microservices to communicate over internal networks without cryptographic overhead."},
                {"id": "E", "text": "Content Delivery Networks (CDNs) employ Anycast BGP routing to terminate client TCP and TLS handshakes at topologically adjacent Edge Points of Presence (PoPs), minimizing Round-Trip Time."}
            ],
            "correctOptionIds": ["A", "B", "C", "D", "E"],
            "explanation": "ALL FIVE statements (A, B, C, D, and E) are true! SNI allows virtual hosting on HTTPS (A). ECH encrypts SNI using DNS HTTPS records (B). HSTS preload prevents initial HTTP downgrade (C). SSL offloading terminates TLS at the edge (D). Anycast CDNs terminate TCP/TLS handshakes close to the user, drastically cutting latency (E).",
            "difficulty": "hard",
            "subtopic": "Web Architecture & Security Synthesis"
        }
    ]
}
