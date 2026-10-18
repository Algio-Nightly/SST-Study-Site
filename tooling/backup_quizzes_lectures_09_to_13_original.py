"""
Comprehensive Quiz Definitions for Lectures 09 through 13
Each lecture contains 20 distinct questions (Single-Choice and Multi-Choice MCQs)
integrating all lecture notes and real-world networking scenarios.
"""

from typing import Dict, Any

def get_lectures_09_to_13_quizzes() -> Dict[str, Any]:
    q = {}

    # =========================================================================
    # --- LECTURE 09: DNS & Internet Applications ---
    # =========================================================================
    q["lecture-09"] = {
        "topicId": "lecture-09",
        "lectureNumber": 9,
        "title": "DNS & Internet Applications Quiz",
        "description": "20 questions covering DNS hierarchy, query resolution, record types (A, AAAA, CNAME, MX, TXT, PTR), URL parsing, HTTP protocol, status codes, and cookies.",
        "estimatedMinutes": 25,
        "questions": [
            {
                "id": "l09-q01",
                "type": "single_choice",
                "question": "What is the primary motivation for using the Domain Name System (DNS) instead of relying directly on hardcoded IP addresses?",
                "options": [
                    {"id": "A", "text": "DNS encrypts all web traffic by default using TLS"},
                    {"id": "B", "text": "Domain names decouple service identity from volatile physical IP addresses, enabling load balancing and seamless IP renumbering"},
                    {"id": "C", "text": "IP addresses cannot be routed across continental fiber lines"},
                    {"id": "D", "text": "Domain names eliminate the need for Layer 3 IP routing"}
                ],
                "correctOptionIds": ["B"],
                "explanation": "DNS decouples human-readable identifiers from underlying numeric IP addresses. This allows servers to migrate IPs, distribute traffic across geo-distributed servers (CDNs), and provide failover without breaking bookmarks or client code.",
                "difficulty": "easy",
                "subtopic": "DNS Motivation"
            },
            {
                "id": "l09-q02",
                "type": "single_choice",
                "question": "In the hierarchical DNS tree structure, which tier is responsible for knowing the authoritative nameservers of Top-Level Domains like .com, .org, and .edu?",
                "options": [
                    {"id": "A", "text": "Authoritative Nameservers"},
                    {"id": "B", "text": "Root Nameservers (represented by the trailing dot '.')"},
                    {"id": "C", "text": "Local Recursive Resolvers"},
                    {"id": "D", "text": "Client OS Stub Resolvers"}
                ],
                "correctOptionIds": ["B"],
                "explanation": "The Root Nameservers sit at the apex of the DNS hierarchy (denoted by the invisible trailing dot in fully qualified domain names like `example.com.`). They maintain delegations to the TLD nameservers.",
                "difficulty": "easy",
                "subtopic": "DNS Hierarchy"
            },
            {
                "id": "l09-q03",
                "type": "single_choice",
                "question": "How are the 13 logical root server IP addresses (a.root-servers.net through m.root-servers.net) scaled globally to handle billions of queries without collapsing?",
                "options": [
                    {"id": "A", "text": "Using BGP Anycast routing to broadcast the same 13 IP addresses from hundreds of physical data centers worldwide"},
                    {"id": "B", "text": "By storing all internet domain records on a single quantum supercomputer in Virginia"},
                    {"id": "C", "text": "By forcing client web browsers to execute DNS root queries locally"},
                    {"id": "D", "text": "By assigning each root server a unique 64-bit IPv8 address"}
                ],
                "correctOptionIds": ["A"],
                "explanation": "Through BGP Anycast, the same 13 logical IP addresses are announced by over 1,500 physical server instances distributed across the globe. Border routers direct DNS queries to the topologically nearest physical instance.",
                "difficulty": "medium",
                "subtopic": "DNS Root & Anycast"
            },
            {
                "id": "l09-q04",
                "type": "single_choice",
                "question": "What is the fundamental difference between a 'Recursive Query' and an 'Iterative Query' in DNS resolution?",
                "options": [
                    {"id": "A", "text": "Recursive queries use TCP; iterative queries use UDP"},
                    {"id": "B", "text": "In a recursive query, the contacted server assumes responsibility to find the final answer; in an iterative query, the server returns the best referral (next nameserver) it knows"},
                    {"id": "C", "text": "Recursive queries only resolve IPv6 addresses; iterative queries resolve IPv4"},
                    {"id": "D", "text": "Iterative queries repeat infinitely until the client manually interrupts them"}
                ],
                "correctOptionIds": ["B"],
                "explanation": "A recursive query asks the resolver: 'Please do whatever work is necessary to bring me the final IP.' An iterative query asks: 'If you don't know the exact answer, give me the IP of the next nameserver down the tree who might know.'",
                "difficulty": "medium",
                "subtopic": "Recursive vs Iterative Queries"
            },
            {
                "id": "l09-q05",
                "type": "single_choice",
                "question": "Which DNS record type maps an IPv6 host address to a domain name?",
                "options": [
                    {"id": "A", "text": "A record"},
                    {"id": "B", "text": "AAAA record (Quad-A)"},
                    {"id": "C", "text": "CNAME record"},
                    {"id": "D", "text": "PTR record"}
                ],
                "correctOptionIds": ["B"],
                "explanation": "An 'A' record maps a hostname to a 32-bit IPv4 address, whereas a 'AAAA' (Quad-A) record maps a hostname to a 128-bit IPv6 address.",
                "difficulty": "easy",
                "subtopic": "DNS Record Types"
            },
            {
                "id": "l09-q06",
                "type": "single_choice",
                "question": "Why is it forbidden by RFC standards to define a CNAME record at the root apex of a domain (e.g. at 'example.com' without a subdomain prefix)?",
                "options": [
                    {"id": "A", "text": "Because CNAME records cannot coexist with other essential record types like SOA and NS at the zone apex"},
                    {"id": "B", "text": "Because CNAME records exceed 1500 bytes"},
                    {"id": "C", "text": "Because CNAME records can only point to numeric IP addresses"},
                    {"id": "D", "text": "Because root apex names can only contain letters, not dots"}
                ],
                "correctOptionIds": ["A"],
                "explanation": "RFC 1034 states that if a CNAME record exists for a node, no other data records can exist for that node. Because a zone apex MUST contain SOA and NS records, a CNAME cannot be placed at the naked apex domain.",
                "difficulty": "hard",
                "subtopic": "CNAME & Apex Restriction"
            },
            {
                "id": "l09-q07",
                "type": "single_choice",
                "question": "Which DNS record type is specifically used by mail transfer agents (MTAs) to route emails to the destination organization's mail servers?",
                "options": [
                    {"id": "A", "text": "TXT record"},
                    {"id": "B", "text": "MX record"},
                    {"id": "C", "text": "PTR record"},
                    {"id": "D", "text": "SRV record"}
                ],
                "correctOptionIds": ["B"],
                "explanation": "MX (Mail Exchanger) records specify the mail servers responsible for accepting emails for a domain, along with priority values for failover.",
                "difficulty": "easy",
                "subtopic": "DNS Record Types"
            },
            {
                "id": "l09-q08",
                "type": "multi_choice",
                "question": "For what security and verification purposes are DNS TXT records widely utilized in modern cloud infrastructure? (Select ALL that apply)",
                "options": [
                    {"id": "A", "text": "SPF (Sender Policy Framework) to prevent email spoofing"},
                    {"id": "B", "text": "DKIM (DomainKeys Identified Mail) public cryptographic key publication"},
                    {"id": "C", "text": "Domain ownership verification for SSL/TLS certificates and Google Search Console"},
                    {"id": "D", "text": "Translating MAC addresses into IPv4 addresses"}
                ],
                "correctOptionIds": ["A", "B", "C"],
                "explanation": "TXT records hold arbitrary text attributes, commonly used for email validation (SPF, DKIM, DMARC) and verifying administrative domain ownership. Translating MAC to IP is handled by ARP/RARP, not DNS TXT.",
                "difficulty": "medium",
                "subtopic": "DNS TXT Applications"
            },
            {
                "id": "l09-q09",
                "type": "single_choice",
                "question": "What is the function of the TTL (Time to Live) field returned in a DNS resource record?",
                "options": [
                    {"id": "A", "text": "It specifies the number of router hops the packet can survive before being dropped"},
                    {"id": "B", "text": "It dictates the number of seconds intermediate recursive resolvers and clients may cache the record before querying authoritative servers again"},
                    {"id": "C", "text": "It defines the server's session timeout in minutes"},
                    {"id": "D", "text": "It specifies the lifespan of the domain registration at the registrar"}
                ],
                "correctOptionIds": ["B"],
                "explanation": "DNS TTL tells caching resolvers how long (in seconds) the answer remains fresh. A lower TTL allows faster propagation of IP changes during migrations, while a higher TTL reduces DNS query traffic.",
                "difficulty": "easy",
                "subtopic": "DNS Caching & TTL"
            },
            {
                "id": "l09-q10",
                "type": "single_choice",
                "question": "In the URL `https://api.scaler.com:8443/v1/students?sort=desc#results`, what constitutes the 'query string' component?",
                "options": [
                    {"id": "A", "text": "api.scaler.com"},
                    {"id": "B", "text": ":8443"},
                    {"id": "C", "text": "sort=desc"},
                    {"id": "D", "text": "#results"}
                ],
                "correctOptionIds": ["C"],
                "explanation": "The URL anatomy is: scheme (`https`), host (`api.scaler.com`), port (`8443`), path (`/v1/students`), query string (`sort=desc`, starting after `?`), and fragment identifier (`results`, starting after `#`).",
                "difficulty": "easy",
                "subtopic": "URL Decomposition"
            },
            {
                "id": "l09-q11",
                "type": "single_choice",
                "question": "Why is the fragment identifier (e.g. `#section2` in `https://example.com/docs#section2`) NEVER transmitted over the wire to the web server in an HTTP GET request?",
                "options": [
                    {"id": "A", "text": "Because HTTP headers cannot contain the '#' character"},
                    {"id": "B", "text": "Because fragments are strictly client-side browser instructions to scroll to or anchor on a specific element after parsing the HTML"},
                    {"id": "C", "text": "Because TLS encryption strips fragment identifiers for security reasons"},
                    {"id": "D", "text": "Because routers drop packets with hashtag symbols"}
                ],
                "correctOptionIds": ["B"],
                "explanation": "Fragment identifiers designate internal anchors within a resource. The web browser processes them locally after receiving the full document; hence, the browser omits the fragment when making the HTTP request.",
                "difficulty": "medium",
                "subtopic": "URL Fragments"
            },
            {
                "id": "l09-q12",
                "type": "single_choice",
                "question": "What is the fundamental difference between an HTTP method being 'Safe' versus being 'Idempotent'?",
                "options": [
                    {"id": "A", "text": "Safe methods use HTTPS; idempotent methods use HTTP"},
                    {"id": "B", "text": "Safe methods do not alter server state (read-only); Idempotent methods can alter state, but executing them multiple times produces the identical side-effect as executing them once"},
                    {"id": "C", "text": "Idempotent methods are read-only; safe methods can delete records"},
                    {"id": "D", "text": "Safe methods run in O(1) time; idempotent methods run in O(N) time"}
                ],
                "correctOptionIds": ["B"],
                "explanation": "Safe methods (like GET, HEAD) do not mutate resource state. Idempotent methods (like PUT, DELETE, GET) can modify state, but repeating identical requests N times leaves the server in the exact same state as 1 request.",
                "difficulty": "medium",
                "subtopic": "HTTP Method Semantics"
            },
            {
                "id": "l09-q13",
                "type": "multi_choice",
                "question": "Which of the following HTTP methods are classified as Idempotent according to RFC 9110? (Select ALL that apply)",
                "options": [
                    {"id": "A", "text": "GET"},
                    {"id": "B", "text": "PUT"},
                    {"id": "C", "text": "DELETE"},
                    {"id": "D", "text": "POST"}
                ],
                "correctOptionIds": ["A", "B", "C"],
                "explanation": "GET (safe and idempotent), PUT (replacing a resource repeatedly yields the same resource state), and DELETE (deleting resource X repeatedly leaves it deleted) are idempotent. POST is typically NOT idempotent (e.g. creating new orders).",
                "difficulty": "medium",
                "subtopic": "HTTP Idempotence"
            },
            {
                "id": "l09-q14",
                "type": "single_choice",
                "question": "What is the key difference between HTTP PUT and HTTP PATCH?",
                "options": [
                    {"id": "A", "text": "PUT is for web pages; PATCH is for mobile apps"},
                    {"id": "B", "text": "PUT replaces the entire target resource with the uploaded payload; PATCH applies partial modifications/deltas to the existing resource"},
                    {"id": "C", "text": "PUT is non-idempotent; PATCH is strictly idempotent"},
                    {"id": "D", "text": "PUT requires authentication; PATCH is anonymous"}
                ],
                "correctOptionIds": ["B"],
                "explanation": "PUT represents a full replacement: any omitted fields are typically cleared or set to defaults. PATCH provides instructions to partially mutate only specific fields without modifying the rest.",
                "difficulty": "easy",
                "subtopic": "PUT vs PATCH"
            },
            {
                "id": "l09-q15",
                "type": "single_choice",
                "question": "What does an HTTP 301 Moved Permanently status code instruct a web browser and search engine crawler to do differently compared to a 302 Found?",
                "options": [
                    {"id": "A", "text": "301 instructs clients and search engines to permanently cache the redirect and update links/SEO rankings to the new URI; 302 is temporary and should not be cached permanently"},
                    {"id": "B", "text": "301 means the page has an error; 302 means the page is successful"},
                    {"id": "C", "text": "301 disables TLS encryption on the new location"},
                    {"id": "D", "text": "301 requires entering a new username and password"}
                ],
                "correctOptionIds": ["A"],
                "explanation": "301 signifies permanent relocation; browsers cache it aggressively and search engines transfer page rank to the new URL. 302 is a temporary redirection, so search engines keep indexing the original URL.",
                "difficulty": "medium",
                "subtopic": "HTTP Status Codes"
            },
            {
                "id": "l09-q16",
                "type": "single_choice",
                "question": "What is the architectural difference between an HTTP 401 Unauthorized and an HTTP 403 Forbidden status code?",
                "options": [
                    {"id": "A", "text": "401 means the client must provide authentication credentials (unauthenticated); 403 means the identity is known but the user lacks permission to access the resource (unauthorized)"},
                    {"id": "B", "text": "401 is a server error; 403 is a client error"},
                    {"id": "C", "text": "401 is returned only over HTTP; 403 is returned only over HTTPS"},
                    {"id": "D", "text": "401 indicates that the server's database is offline"}
                ],
                "correctOptionIds": ["A"],
                "explanation": "401 implies 'who are you? Please log in.' 403 implies 'I know who you are, but you do not have permission to touch this resource.'",
                "difficulty": "medium",
                "subtopic": "HTTP Status Codes"
            },
            {
                "id": "l09-q17",
                "type": "single_choice",
                "question": "What is the critical security vulnerability prevented by setting the 'HttpOnly' flag on a Set-Cookie header?",
                "options": [
                    {"id": "A", "text": "Man-in-the-middle sniffing of packets over open Wi-Fi"},
                    {"id": "B", "text": "Session hijacking via Cross-Site Scripting (XSS) where malicious JavaScript accesses `document.cookie`"},
                    {"id": "C", "text": "SQL Injection attacks on the backend database"},
                    {"id": "D", "text": "Denial of Service attacks against the web server"}
                ],
                "correctOptionIds": ["B"],
                "explanation": "The `HttpOnly` flag prevents client-side scripts (like JavaScript running via XSS) from reading the cookie via `document.cookie`, mitigating cookie theft and session hijacking.",
                "difficulty": "medium",
                "subtopic": "Cookie Security Flags"
            },
            {
                "id": "l09-q18",
                "type": "single_choice",
                "question": "What is the purpose of the 'SameSite=Strict' cookie attribute?",
                "options": [
                    {"id": "A", "text": "It forces the cookie to only be transmitted over HTTPS connections"},
                    {"id": "B", "text": "It prevents the browser from sending the cookie on ANY cross-site request (mitigating Cross-Site Request Forgery / CSRF)"},
                    {"id": "C", "text": "It expires the cookie after strictly 5 minutes"},
                    {"id": "D", "text": "It prevents users from logging in on mobile devices"}
                ],
                "correctOptionIds": ["B"],
                "explanation": "`SameSite=Strict` guarantees the cookie is never sent in third-party contexts (e.g. following links from external sites or embedded iframes), eliminating CSRF vulnerabilities for authenticated state.",
                "difficulty": "hard",
                "subtopic": "CSRF & SameSite"
            },
            {
                "id": "l09-q19",
                "type": "single_choice",
                "question": "In a modern stateless web application using JWT (JSON Web Tokens) for sessions, where is the session state primarily stored?",
                "options": [
                    {"id": "A", "text": "In a centralized Redis database on the server"},
                    {"id": "B", "text": "Directly inside the cryptographically signed JWT payload held and presented by the client"},
                    {"id": "C", "text": "In the router's ARP table"},
                    {"id": "D", "text": "In the DNS SOA record"}
                ],
                "correctOptionIds": ["B"],
                "explanation": "Stateless JWT tokens encode user identity and claims directly in the token payload, signed by the server's private secret. Any backend server can verify the signature without reading a centralized database.",
                "difficulty": "medium",
                "subtopic": "Sessions vs JWT"
            },
            {
                "id": "l09-q20",
                "type": "single_choice",
                "question": "How does DNS-based Round-Robin Load Balancing distribute client requests among multiple backend web servers?",
                "options": [
                    {"id": "A", "text": "The authoritative DNS server rotates the ordering of multiple IP addresses in the 'A' record answer set on each query"},
                    {"id": "B", "text": "The client router picks the server with the lowest MAC address"},
                    {"id": "C", "text": "The DNS server opens TCP connections to test each backend server's CPU load"},
                    {"id": "D", "text": "The DNS root servers route packets through a reverse proxy"}
                ],
                "correctOptionIds": ["A"],
                "explanation": "In Round-Robin DNS, multiple A records are configured for the same domain. The DNS server permutes the list on successive responses, distributing incoming connections across multiple IP addresses.",
                "difficulty": "easy",
                "subtopic": "DNS Load Balancing"
            }
        ]
    }

    # =========================================================================
    # --- LECTURE 10: TCP, UDP & Socket Programming ---
    # =========================================================================
    q["lecture-10"] = {
        "topicId": "lecture-10",
        "lectureNumber": 10,
        "title": "TCP, UDP & Socket Programming Quiz",
        "description": "20 questions covering transport layer multiplexing, ports, TCP 3-way handshake, 4-way teardown, TIME_WAIT, sliding window, congestion control, and Python socket programming.",
        "estimatedMinutes": 25,
        "questions": [
            {
                "id": "l10-q01",
                "type": "single_choice",
                "question": "While the Network Layer (IP) provides host-to-host packet delivery, what essential abstraction does the Transport Layer (Layer 4) provide?",
                "options": [
                    {"id": "A", "text": "Hop-by-hop framing across fiber cables"},
                    {"id": "B", "text": "Process-to-process communication using port numbers (demultiplexing)"},
                    {"id": "C", "text": "Global path computation using BGP"},
                    {"id": "D", "text": "Translating domain names into 32-bit integers"}
                ],
                "correctOptionIds": ["B"],
                "explanation": "The transport layer introduces port numbers, enabling multiple independent application processes on the same host to send and receive traffic concurrently over a shared network connection.",
                "difficulty": "easy",
                "subtopic": "Transport Layer Purpose"
            },
            {
                "id": "l10-q02",
                "type": "single_choice",
                "question": "What 5-tuple uniquely identifies a TCP connection on an operating system?",
                "options": [
                    {"id": "A", "text": "(Source MAC, Dest MAC, VLAN ID, TTL, Checksum)"},
                    {"id": "B", "text": "(Source IP, Source Port, Destination IP, Destination Port, Protocol/TCP)"},
                    {"id": "C", "text": "(Domain Name, URL Path, HTTP Method, User-Agent, Cookie)"},
                    {"id": "D", "text": "(Window Size, Sequence Number, Ack Number, Flags, MSS)"}
                ],
                "correctOptionIds": ["B"],
                "explanation": "A TCP socket connection is uniquely identified by its 5-tuple: `(Source IP, Source Port, Destination IP, Destination Port, Protocol)`. This allows a web server on port 80 to handle thousands of concurrent client connections simultaneously.",
                "difficulty": "easy",
                "subtopic": "Socket 5-Tuple"
            },
            {
                "id": "l10-q03",
                "type": "single_choice",
                "question": "Why does DNS primarily use UDP on port 53 for standard name queries instead of TCP?",
                "options": [
                    {"id": "A", "text": "Because UDP encrypts queries to prevent eavesdropping"},
                    {"id": "B", "text": "Because UDP has zero connection establishment overhead (1 RTT total: query and reply), minimizing latency and server memory overhead"},
                    {"id": "C", "text": "Because TCP packets cannot cross internet backbones"},
                    {"id": "D", "text": "Because UDP supports packet sizes up to 1 gigabyte"}
                ],
                "correctOptionIds": ["B"],
                "explanation": "A typical DNS query fits in a single packet. UDP avoids the 3-way handshake round-trip delay and consumes no state/memory on DNS servers, making it exceptionally fast and scalable.",
                "difficulty": "easy",
                "subtopic": "UDP vs TCP Tradeoffs"
            },
            {
                "id": "l10-q04",
                "type": "single_choice",
                "question": "What is the primary function of the TCP 3-Way Handshake?",
                "options": [
                    {"id": "A", "text": "To negotiate the symmetric encryption keys for TLS"},
                    {"id": "B", "text": "To synchronize Initial Sequence Numbers (ISNs) in both directions and exchange buffer parameters (MSS, window scale)"},
                    {"id": "C", "text": "To verify the client's email address and password"},
                    {"id": "D", "text": "To calculate the shortest path across the internet using Dijkstra"}
                ],
                "correctOptionIds": ["B"],
                "explanation": "The 3-way handshake (SYN, SYN-ACK, ACK) ensures that both endpoints agree to communicate, synchronize their initial byte sequence numbers (ISNs), and agree on options like Maximum Segment Size (MSS).",
                "difficulty": "medium",
                "subtopic": "3-Way Handshake"
            },
            {
                "id": "l10-q05",
                "type": "single_choice",
                "question": "Why does a modern TCP implementation initialize sequence numbers with pseudo-random Initial Sequence Numbers (ISNs) rather than starting every connection at sequence number 0?",
                "options": [
                    {"id": "A", "text": "To prevent delayed duplicate packets from old, terminated connections from corrupting a new connection on the same 5-tuple, and to prevent sequence number prediction attacks"},
                    {"id": "B", "text": "Because sequence number 0 is reserved for broadcast packets"},
                    {"id": "C", "text": "To speed up CRC checksum calculations"},
                    {"id": "D", "text": "Because 64-bit systems cannot represent the integer zero"}
                ],
                "correctOptionIds": ["A"],
                "explanation": "Randomized ISNs protect against TCP sequence number spoofing/session hijacking attacks and prevent stray packets delayed in internet buffers from being mistakenly accepted by subsequent connections reusing the same ports.",
                "difficulty": "hard",
                "subtopic": "TCP ISN Randomization"
            },
            {
                "id": "l10-q06",
                "type": "single_choice",
                "question": "In a SYN Flood denial-of-service attack, how does the 'SYN Cookies' technique allow a server to defend itself without exhausting memory on half-open connections?",
                "options": [
                    {"id": "A", "text": "It blocks all IP addresses that send SYN packets"},
                    {"id": "B", "text": "It avoids allocating any kernel memory for the TCB (Transmission Control Block); instead, it encodes the connection state into the server's Initial Sequence Number (ISN) and reconstructs state upon receiving the client's final ACK"},
                    {"id": "C", "text": "It automatically shifts the server from port 80 to port 443"},
                    {"id": "D", "text": "It delegates connection handling to the client's gateway router"}
                ],
                "correctOptionIds": ["B"],
                "explanation": "SYN cookies encode cryptographic state (MSS, timestamp, secret key) into the 32-bit ISN of the SYN-ACK packet. The server allocates zero state in RAM until the client sends a valid ACK containing that cookie incremented by 1.",
                "difficulty": "hard",
                "subtopic": "SYN Flood & SYN Cookies"
            },
            {
                "id": "l10-q07",
                "type": "single_choice",
                "question": "Why does closing a TCP connection typically require a 4-Way Handshake (FIN, ACK, FIN, ACK) rather than a 3-way exchange?",
                "options": [
                    {"id": "A", "text": "Because TCP connections are full-duplex; one endpoint can finish transmitting data (sending FIN) while still receiving data from the peer (half-closed state)"},
                    {"id": "B", "text": "Because Ethernet requires 4 frames to compute CRC"},
                    {"id": "C", "text": "Because routers must acknowledge every disconnection"},
                    {"id": "D", "text": "Because the client and server must exchange TLS certificates again"}
                ],
                "correctOptionIds": ["A"],
                "explanation": "TCP is bidirectional (full-duplex). When host A sends a FIN, it only closes its own sending half-stream. Host B acknowledges with an ACK, but may continue sending pending data until it independently issues its own FIN.",
                "difficulty": "medium",
                "subtopic": "TCP 4-Way Teardown"
            },
            {
                "id": "l10-q08",
                "type": "single_choice",
                "question": "Why must the active closer of a TCP connection remain in the `TIME_WAIT` state for a duration of 2 * MSL (Maximum Segment Lifetime, typically 60-120 seconds)?",
                "options": [
                    {"id": "A", "text": "To allow the CPU to cool down after high throughput"},
                    {"id": "B", "text": "To guarantee that the final ACK was received by the peer (and retransmit it if a stray FIN arrives), and to ensure all delayed duplicate segments from the old connection drain from the network"},
                    {"id": "C", "text": "To keep the port locked permanently so nobody can reuse it"},
                    {"id": "D", "text": "To wait for DNS caches to expire"}
                ],
                "correctOptionIds": ["B"],
                "explanation": "If the final ACK is lost, the peer will retransmit its FIN. Being in TIME_WAIT allows the host to resend the ACK. Furthermore, 2*MSL ensures all phantom segments in flight dissipate before the socket 5-tuple can be safely reopened.",
                "difficulty": "hard",
                "subtopic": "TIME_WAIT Justification"
            },
            {
                "id": "l10-q09",
                "type": "single_choice",
                "question": "What does a Cumulative Acknowledgment number of `ACK = 5001` signify in TCP?",
                "options": [
                    {"id": "A", "text": "Byte 5001 has been received with an error"},
                    {"id": "B", "text": "All contiguous bytes up to byte 5000 have been successfully received, and the receiver expects byte 5001 next"},
                    {"id": "C", "text": "Only byte 5001 has been received"},
                    {"id": "D", "text": "The sender must reset the window to 5001 bytes"}
                ],
                "correctOptionIds": ["B"],
                "explanation": "TCP acknowledgments are cumulative: an ACK value of N indicates that all bytes up to N - 1 have been received in order, and the receiver is anticipating byte N.",
                "difficulty": "easy",
                "subtopic": "Cumulative ACK"
            },
            {
                "id": "l10-q10",
                "type": "single_choice",
                "question": "What major inefficiency of basic cumulative ACKs does Selective Acknowledgment (SACK, RFC 2018) solve?",
                "options": [
                    {"id": "A", "text": "It eliminates the need for sequence numbers entirely"},
                    {"id": "B", "text": "When a single segment is lost in a large burst, SACK explicitly informs the sender which non-contiguous blocks arrived, avoiding retransmission of already received data"},
                    {"id": "C", "text": "It converts TCP into UDP when packets are lost"},
                    {"id": "D", "text": "It increases maximum packet payload to 64 KB"}
                ],
                "correctOptionIds": ["B"],
                "explanation": "Without SACK, if segment 2 is lost in a train of 10 segments, the sender might have to retransmit all segments from 2 through 10 (Go-Back-N). SACK allows the receiver to specify exact discontinuous ranges (e.g. 3-10 received), retransmitting only segment 2.",
                "difficulty": "medium",
                "subtopic": "TCP SACK"
            },
            {
                "id": "l10-q11",
                "type": "single_choice",
                "question": "What is the difference between TCP Flow Control and TCP Congestion Control?",
                "options": [
                    {"id": "A", "text": "Flow control protects the receiving host from being overwhelmed; Congestion control protects the intermediate network routers/links from being overloaded"},
                    {"id": "B", "text": "Flow control operates in hardware; congestion control operates in software"},
                    {"id": "C", "text": "Flow control uses cwnd; congestion control uses rwnd"},
                    {"id": "D", "text": "Flow control is for UDP; congestion control is for TCP"}
                ],
                "correctOptionIds": ["A"],
                "explanation": "Flow Control is end-to-end: the receiver advertises `rwnd` to prevent buffer overflow on its own NIC/RAM. Congestion Control is sender-driven: the sender throttles `cwnd` based on packet loss or latency to prevent choking intermediate routers.",
                "difficulty": "medium",
                "subtopic": "Flow Control vs Congestion Control"
            },
            {
                "id": "l10-q12",
                "type": "single_choice",
                "question": "At any given instant, what is the maximum number of unacknowledged in-flight bytes a TCP sender is permitted to transmit?",
                "options": [
                    {"id": "A", "text": "cwnd + rwnd"},
                    {"id": "B", "text": "min(cwnd, rwnd)"},
                    {"id": "C", "text": "max(cwnd, rwnd)"},
                    {"id": "D", "text": "MSS * 65535"}
                ],
                "correctOptionIds": ["B"],
                "explanation": "The effective transmission window is the minimum of the receiver's advertised buffer window (`rwnd`) and the network's estimated congestion window (`cwnd`): `Effective Window = min(cwnd, rwnd)`.",
                "difficulty": "easy",
                "subtopic": "Effective Window Equation"
            },
            {
                "id": "l10-q13",
                "type": "single_choice",
                "question": "During the TCP Slow Start phase, how does the Congestion Window (cwnd) grow upon receiving ACKs?",
                "options": [
                    {"id": "A", "text": "Linearly: cwnd += 1 MSS per Round Trip Time (RTT)"},
                    {"id": "B", "text": "Exponentially: cwnd doubles every RTT (increasing by 1 MSS for every valid ACK received)"},
                    {"id": "C", "text": "It remains strictly constant until timeout"},
                    {"id": "D", "text": "It halves every RTT"}
                ],
                "correctOptionIds": ["B"],
                "explanation": "Despite its misleading name, 'Slow Start' ramps up aggressively: for each ACK received, cwnd increases by 1 MSS, effectively doubling the congestion window every Round Trip Time (RTT) until reaching `ssthresh`.",
                "difficulty": "medium",
                "subtopic": "TCP Slow Start"
            },
            {
                "id": "l10-q14",
                "type": "single_choice",
                "question": "What triggers TCP Fast Retransmit without waiting for the full retransmission timeout (RTO) timer to expire?",
                "options": [
                    {"id": "A", "text": "Arrival of 3 duplicate ACKs for the same sequence number"},
                    {"id": "B", "text": "Receipt of an ICMP Destination Unreachable message"},
                    {"id": "C", "text": "A manual keyboard interrupt by the user"},
                    {"id": "D", "text": "A decrease in the receiver's window size to zero"}
                ],
                "correctOptionIds": ["A"],
                "explanation": "When three duplicate ACKs (4 identical ACKs total) arrive at the sender, it deduces that later packets reached the receiver and only one segment was dropped in between, triggering an immediate Fast Retransmit without waiting for the slow RTO timer.",
                "difficulty": "medium",
                "subtopic": "Fast Retransmit"
            },
            {
                "id": "l10-q15",
                "type": "single_choice",
                "question": "What is the primary operational difference between loss-based congestion control (like TCP Reno/CUBIC) and modern delay-based/model-based congestion control like Google's BBR?",
                "options": [
                    {"id": "A", "text": "BBR only runs over UDP"},
                    {"id": "B", "text": "Loss-based algorithms intentionally fill router queue buffers until packets drop (causing bufferbloat); BBR measures bottleneck bandwidth and min-RTT to operate at optimal queue capacity without filling buffers"},
                    {"id": "C", "text": "Loss-based algorithms require hardware router modifications"},
                    {"id": "D", "text": "BBR disables retransmissions completely"}
                ],
                "correctOptionIds": ["B"],
                "explanation": "Reno and CUBIC treat packet loss as the congestion signal, which fills up intermediate router buffers (bufferbloat) and inflates latency. BBR (Bottleneck Bandwidth and RTT) models the physical pipe to keep queues empty and throughput maximum.",
                "difficulty": "hard",
                "subtopic": "BBR Congestion Control"
            },
            {
                "id": "l10-q16",
                "type": "single_choice",
                "question": "In Python's `socket` module, what is the correct socket family and type to create a streaming TCP socket over IPv4?",
                "options": [
                    {"id": "A", "text": "socket.socket(socket.AF_INET, socket.SOCK_DGRAM)"},
                    {"id": "B", "text": "socket.socket(socket.AF_INET, socket.SOCK_STREAM)"},
                    {"id": "C", "text": "socket.socket(socket.AF_INET6, socket.SOCK_RAW)"},
                    {"id": "D", "text": "socket.socket(socket.AF_PACKET, socket.SOCK_STREAM)"}
                ],
                "correctOptionIds": ["B"],
                "explanation": "`AF_INET` designates IPv4 addressing, and `SOCK_STREAM` specifies a reliable, ordered, two-way byte stream (TCP). (`SOCK_DGRAM` creates a UDP socket).",
                "difficulty": "easy",
                "subtopic": "Python Socket API"
            },
            {
                "id": "l10-q17",
                "type": "single_choice",
                "question": "In a Python TCP server, what does `server_socket.accept()` return when a client connects?",
                "options": [
                    {"id": "A", "text": "An integer representing the client's PID"},
                    {"id": "B", "text": "A tuple of `(conn, address)` where `conn` is a brand-new socket object dedicated to communicating with that specific client, and `address` is `(ip, port)`"},
                    {"id": "C", "text": "The raw bytes received from the client"},
                    {"id": "D", "text": "The server's own IP address"}
                ],
                "correctOptionIds": ["B"],
                "explanation": "`accept()` blocks until a client connects, then returns a new dedicated connection socket for that client's stream and a tuple containing the client's remote `(ip, port)`. The listening socket continues accepting other incoming connections.",
                "difficulty": "medium",
                "subtopic": "Socket accept() Lifecycle"
            },
            {
                "id": "l10-q18",
                "type": "single_choice",
                "question": "Why is it recommended in Python network code to use `conn.sendall(data)` instead of `conn.send(data)` when transmitting large payloads?",
                "options": [
                    {"id": "A", "text": "`send()` compresses data; `sendall()` does not"},
                    {"id": "B", "text": "`send()` may transmit only a partial slice of the byte buffer if the socket send buffer is full; `sendall()` loops internally until the entire buffer has been transmitted or an error occurs"},
                    {"id": "C", "text": "`send()` is only for UDP; `sendall()` is for TCP"},
                    {"id": "D", "text": "`send()` requires root privileges"}
                ],
                "correctOptionIds": ["B"],
                "explanation": "`send()` returns the number of bytes actually sent, which may be less than `len(data)` if kernel buffers are constrained. `sendall()` continues sending data from the buffer until all bytes are delivered.",
                "difficulty": "medium",
                "subtopic": "send() vs sendall()"
            },
            {
                "id": "l10-q19",
                "type": "single_choice",
                "question": "What socket option must be configured with `setsockopt` to prevent the common `OSError: [Errno 98] Address already in use` error when restarting a development server?",
                "options": [
                    {"id": "A", "text": "socket.SO_KEEPALIVE"},
                    {"id": "B", "text": "socket.SO_REUSEADDR"},
                    {"id": "C", "text": "socket.SO_BROADCAST"},
                    {"id": "D", "text": "socket.TCP_NODELAY"}
                ],
                "correctOptionIds": ["B"],
                "explanation": "`SO_REUSEADDR` allows the socket to forcibly bind to a local port that is currently in the `TIME_WAIT` state from a recently closed connection.",
                "difficulty": "medium",
                "subtopic": "SO_REUSEADDR Socket Option"
            },
            {
                "id": "l10-q20",
                "type": "multi_choice",
                "question": "Why is TCP described as a 'Byte Stream' protocol rather than a 'Message/Packet' protocol? (Select ALL that apply)",
                "options": [
                    {"id": "A", "text": "TCP does not preserve application message boundaries; two separate `send()` calls can be merged into a single segment by Nagle's algorithm"},
                    {"id": "B", "text": "A single large `send()` call can be fragmented across multiple TCP segments"},
                    {"id": "C", "text": "The application must implement its own framing (delimiters like `\\n` or length prefixes) to parse discrete messages"},
                    {"id": "D", "text": "TCP sends raw machine instructions directly to the router CPU"}
                ],
                "correctOptionIds": ["A", "B", "C"],
                "explanation": "TCP is a continuous unstructured pipe of bytes. It does not know or care where application messages begin or end. It can coalesce small packets or split large ones arbitrarily. Applications must frame their messages explicitly.",
                "difficulty": "hard",
                "subtopic": "TCP Stream Semantics"
            }
        ]
    }

    # =========================================================================
    # --- LECTURE 11: NAT, DHCP & Local Network Communication ---
    # =========================================================================
    q["lecture-11"] = {
        "topicId": "lecture-11",
        "lectureNumber": 11,
        "title": "NAT, DHCP & Local Communication Quiz",
        "description": "20 questions covering ARP requests/replies, gratuitous ARP, ARP spoofing, DHCP DORA lifecycle, NAT/PAT translation tables, SNAT vs DNAT, and home gateway architecture.",
        "estimatedMinutes": 25,
        "questions": [
            {
                "id": "l11-q01",
                "type": "single_choice",
                "question": "What is the core purpose of the Address Resolution Protocol (ARP) in IPv4 networking?",
                "options": [
                    {"id": "A", "text": "To translate domain names into 32-bit IP addresses"},
                    {"id": "B", "text": "To dynamically resolve a known Layer 3 IP address to a physical Layer 2 MAC address on the local broadcast link"},
                    {"id": "C", "text": "To route packets across multiple Autonomous Systems"},
                    {"id": "D", "text": "To assign IP addresses to new Wi-Fi devices automatically"}
                ],
                "correctOptionIds": ["B"],
                "explanation": "IP operates at Layer 3, but NICs on local Ethernet/Wi-Fi links communicate strictly via Layer 2 MAC addresses. ARP maps the target IP to its corresponding 48-bit MAC address.",
                "difficulty": "easy",
                "subtopic": "ARP Fundamentals"
            },
            {
                "id": "l11-q02",
                "type": "single_choice",
                "question": "What are the Layer 2 and Layer 3 destination addresses of an ARP Request frame searching for IP 192.168.1.1?",
                "options": [
                    {"id": "A", "text": "L2 Dest: FF:FF:FF:FF:FF:FF (Broadcast), Target IP: 192.168.1.1"},
                    {"id": "B", "text": "L2 Dest: 00:00:00:00:00:00, Target IP: 255.255.255.255"},
                    {"id": "C", "text": "L2 Dest: Gateway MAC, Target IP: 0.0.0.0"},
                    {"id": "D", "text": "L2 Dest: 01:00:5E:00:00:01 (Multicast), Target IP: 127.0.0.1"}
                ],
                "correctOptionIds": ["A"],
                "explanation": "Because the sender does not know the target's MAC, it broadcasts the frame to `FF:FF:FF:FF:FF:FF`. Every host on the switch receives it, but only the host configured with target IP 192.168.1.1 responds.",
                "difficulty": "medium",
                "subtopic": "ARP Request Addressing"
            },
            {
                "id": "l11-q03",
                "type": "single_choice",
                "question": "How is an ARP Reply transmitted back to the inquiring host?",
                "options": [
                    {"id": "A", "text": "As a Layer 2 Broadcast to FF:FF:FF:FF:FF:FF"},
                    {"id": "B", "text": "As a Layer 2 Unicast frame addressed directly to the inquiring host's MAC address"},
                    {"id": "C", "text": "Through a DNS pointer query"},
                    {"id": "D", "text": "Via the default gateway router"}
                ],
                "correctOptionIds": ["B"],
                "explanation": "The ARP Request contained the sender's own MAC address. The target machine simply sends a direct unicast Layer 2 Ethernet frame back to that MAC address.",
                "difficulty": "easy",
                "subtopic": "ARP Reply"
            },
            {
                "id": "l11-q04",
                "type": "single_choice",
                "question": "What Linux command shown in lecture demonstrations manually adds a static ARP mapping to interface `eth1`?",
                "options": [
                    {"id": "A", "text": "ip route add 10.0.0.2 dev eth1"},
                    {"id": "B", "text": "sudo ip neigh add 10.0.0.2 lladdr aa:bb:cc:dd:ee:ff dev eth1"},
                    {"id": "C", "text": "ifconfig eth1 hw ether aa:bb:cc:dd:ee:ff"},
                    {"id": "D", "text": "ping -c 1 10.0.0.2"}
                ],
                "correctOptionIds": ["B"],
                "explanation": "As covered in handwritten lecture notes, `ip neigh add <IP> lladdr <MAC> dev <interface>` manipulates the kernel neighbor/ARP cache table directly.",
                "difficulty": "medium",
                "subtopic": "Linux ip neigh Command"
            },
            {
                "id": "l11-q05",
                "type": "single_choice",
                "question": "What is a 'Gratuitous ARP' and what is its primary legitimate network function?",
                "options": [
                    {"id": "A", "text": "An ARP query sent to hack neighbor routers"},
                    {"id": "B", "text": "An unprompted ARP broadcast where a host announces its own IP-to-MAC mapping, used for IP conflict detection and updating switch MAC tables during failover (CARP/VRRP)"},
                    {"id": "C", "text": "An ARP reply that is rejected due to invalid checksums"},
                    {"id": "D", "text": "A request to renew a DHCP lease"}
                ],
                "correctOptionIds": ["B"],
                "explanation": "A Gratuitous ARP occurs when a host broadcasts an ARP announcement for its own IP. If another host replies, an IP collision is detected. During high-availability failovers (VRRP), backup servers broadcast Gratuitous ARPs so switches immediately point traffic to their port.",
                "difficulty": "hard",
                "subtopic": "Gratuitous ARP"
            },
            {
                "id": "l11-q06",
                "type": "single_choice",
                "question": "In an ARP Spoofing (Poisoning) attack, what vulnerability in the ARP protocol is exploited by the attacker?",
                "options": [
                    {"id": "A", "text": "ARP uses 1024-bit RSA keys that are easily factored"},
                    {"id": "B", "text": "ARP is completely stateless and unauthenticated; hosts accept unsolicited ARP replies and overwrite their ARP cache without verification"},
                    {"id": "C", "text": "ARP packets are limited to 64 bytes"},
                    {"id": "D", "text": "ARP operates exclusively over Wi-Fi, never wired cables"}
                ],
                "correctOptionIds": ["B"],
                "explanation": "ARP lacks cryptographic authentication. A malicious host on the LAN can broadcast fake ARP replies claiming the Default Gateway's IP has the attacker's MAC address, intercepting all outbound internet traffic.",
                "difficulty": "medium",
                "subtopic": "ARP Spoofing"
            },
            {
                "id": "l11-q07",
                "type": "single_choice",
                "question": "What is the correct chronological 4-step sequence of messages in the DHCP address allocation process (DORA)?",
                "options": [
                    {"id": "A", "text": "Discover -> Offer -> Request -> Acknowledge"},
                    {"id": "B", "text": "Dial -> Open -> Receive -> Accept"},
                    {"id": "C", "text": "Determine -> Option -> Route -> Assign"},
                    {"id": "D", "text": "Detect -> Order -> Register -> Authorize"}
                ],
                "correctOptionIds": ["A"],
                "explanation": "DHCP DORA sequence: 1. Discover (Client broadcasts looking for servers), 2. Offer (Server offers IP/subnet/gateway), 3. Request (Client formally requests offered IP), 4. Acknowledge (Server commits lease).",
                "difficulty": "easy",
                "subtopic": "DHCP DORA"
            },
            {
                "id": "l11-q08",
                "type": "single_choice",
                "question": "When a brand-new host without an IP boots up and sends a DHCP Discover packet, what are its Source IP and Destination IP addresses?",
                "options": [
                    {"id": "A", "text": "Src IP: 127.0.0.1, Dst IP: 192.168.1.1"},
                    {"id": "B", "text": "Src IP: 0.0.0.0, Dst IP: 255.255.255.255 (Limited Broadcast)"},
                    {"id": "C", "text": "Src IP: 169.254.0.1, Dst IP: 8.8.8.8"},
                    {"id": "D", "text": "Src IP: 0.0.0.0, Dst IP: 224.0.0.1"}
                ],
                "correctOptionIds": ["B"],
                "explanation": "Because the host has no assigned IP address yet, it uses `0.0.0.0` as source. To reach any listening DHCP server on the local subnet without knowing their IPs, it broadcasts to `255.255.255.255` on UDP port 67.",
                "difficulty": "medium",
                "subtopic": "DHCP Discover Packet"
            },
            {
                "id": "l11-q09",
                "type": "multi_choice",
                "question": "Which crucial network configuration parameters are standardly provided to a client computer in a DHCP Acknowledge (ACK) message? (Select ALL that apply)",
                "options": [
                    {"id": "A", "text": "Assigned Client IPv4 Address and Subnet Mask"},
                    {"id": "B", "text": "Default Gateway (Router) IP Address"},
                    {"id": "C", "text": "DNS Server IP Addresses (e.g. 1.1.1.1, 8.8.8.8)"},
                    {"id": "D", "text": "The client's CPU clock frequency"}
                ],
                "correctOptionIds": ["A", "B", "C"],
                "explanation": "DHCP delivers the complete network setup: client IP, subnet mask, default gateway IP, DNS server IPs, domain search suffixes, and lease duration. (CPU clock is internal hardware).",
                "difficulty": "easy",
                "subtopic": "DHCP Configuration Options"
            },
            {
                "id": "l11-q10",
                "type": "single_choice",
                "question": "At what point during its lease lifetime does a DHCP client first attempt to renew its IP lease with the issuing DHCP server (Timer T1)?",
                "options": [
                    {"id": "A", "text": "At 10% of the lease time"},
                    {"id": "B", "text": "At 50% of the lease time (via unicast DHCP Request)"},
                    {"id": "C", "text": "At 87.5% of the lease time"},
                    {"id": "D", "text": "Only after the lease completely reaches 0 seconds"}
                ],
                "correctOptionIds": ["B"],
                "explanation": "At T1 (50% of lease time), the client sends a unicast DHCP Request directly to the server that granted the lease. If no response is received by T2 (87.5%), it falls back to broadcasting to any available DHCP server.",
                "difficulty": "medium",
                "subtopic": "DHCP Lease Timers"
            },
            {
                "id": "l11-q11",
                "type": "single_choice",
                "question": "If a Windows or macOS client is set to DHCP but fails to contact any DHCP server, what address block does it automatically assign to itself (APIPA)?",
                "options": [
                    {"id": "A", "text": "10.0.0.0/8"},
                    {"id": "B", "text": "192.168.0.0/16"},
                    {"id": "C", "text": "169.254.0.0/16 (Link-Local)"},
                    {"id": "D", "text": "127.0.0.0/8 (Loopback)"}
                ],
                "correctOptionIds": ["C"],
                "explanation": "When DHCP fails, the OS falls back to APIPA (Automatic Private IP Addressing) using the RFC 3927 link-local range `169.254.x.x`. This allows ad-hoc LAN communication between hosts, but has no internet connectivity.",
                "difficulty": "easy",
                "subtopic": "APIPA Link-Local"
            },
            {
                "id": "l11-q12",
                "type": "single_choice",
                "question": "What is the primary distinction between Static NAT and Dynamic PAT (Port Address Translation / NAT Overload)?",
                "options": [
                    {"id": "A", "text": "Static NAT is only for IPv6; PAT is for IPv4"},
                    {"id": "B", "text": "Static NAT maps one private IP to one dedicated public IP (1:1); PAT multiplexes thousands of private IP hosts onto a single shared public IP using unique Layer 4 port numbers (M:1)"},
                    {"id": "C", "text": "PAT requires dedicated hardware fiber cables"},
                    {"id": "D", "text": "Static NAT does not alter the IP header"}
                ],
                "correctOptionIds": ["B"],
                "explanation": "Static NAT does a fixed 1:1 mapping (useful for hosting public servers). PAT (Network Address Port Translation / NAT Overload) allows an entire home or corporate office to share a single public IP by tracking ephemeral port numbers.",
                "difficulty": "easy",
                "subtopic": "NAT vs PAT"
            },
            {
                "id": "l11-q13",
                "type": "single_choice",
                "question": "When Host A (192.168.1.50:52134) sends a packet to a web server (93.184.216.34:80) through a PAT gateway with public IP 203.0.113.1, how does the router rewrite the packet headers?",
                "options": [
                    {"id": "A", "text": "It leaves Source IP as 192.168.1.50 and changes Destination IP to 203.0.113.1"},
                    {"id": "B", "text": "It replaces Source IP 192.168.1.50 with 203.0.113.1 and maps Source Port 52134 to an allocated translation port (e.g. 40001)"},
                    {"id": "C", "text": "It changes Destination Port to 52134"},
                    {"id": "D", "text": "It strips the IP header completely"}
                ],
                "correctOptionIds": ["B"],
                "explanation": "The NAT router replaces the private Inside Local IP:Port (`192.168.1.50:52134`) with its own Inside Global IP and an assigned ephemeral port (`203.0.113.1:40001`), recording this mapping in its active NAT state table.",
                "difficulty": "medium",
                "subtopic": "PAT Packet Rewriting"
            },
            {
                "id": "l11-q14",
                "type": "single_choice",
                "question": "Why does standard outbound PAT make it fundamentally impossible for external clients on the public internet to initiate an unsolicited direct connection to a private server inside a LAN?",
                "options": [
                    {"id": "A", "text": "Because fiber optic cables are unidirectional"},
                    {"id": "B", "text": "Because the NAT router only forwards inbound packets that match an existing active translation entry created by previous outbound traffic"},
                    {"id": "C", "text": "Because private hosts do not have MAC addresses"},
                    {"id": "D", "text": "Because public IP packets cannot carry TCP headers"}
                ],
                "correctOptionIds": ["B"],
                "explanation": "PAT is stateful: incoming packets from the WAN are dropped unless their destination port matches an active outbound session previously initiated by an internal host. Without an existing entry, the router does not know which internal host should receive the packet.",
                "difficulty": "medium",
                "subtopic": "NAT Inbound Blocking"
            },
            {
                "id": "l11-q15",
                "type": "single_choice",
                "question": "What configuration technique allows external users on the internet to connect to an internal web server (192.168.1.100:8080) through a home router with a single public IP?",
                "options": [
                    {"id": "A", "text": "Port Forwarding (Destination NAT / DNAT)"},
                    {"id": "B", "text": "Subnet Mask Inversion"},
                    {"id": "C", "text": "Gratuitous ARP spoofing"},
                    {"id": "D", "text": "Disabling the router's DNS server"}
                ],
                "correctOptionIds": ["A"],
                "explanation": "Port Forwarding (DNAT) adds a static rule to the router's NAT table: any incoming packet on public port 80 (or custom port) is automatically translated and forwarded to internal private IP `192.168.1.100:8080`.",
                "difficulty": "easy",
                "subtopic": "Port Forwarding / DNAT"
            },
            {
                "id": "l11-q16",
                "type": "single_choice",
                "question": "Why does NAT break end-to-end peer-to-peer (P2P) protocols like WebRTC, BitTorrent, and VoIP, requiring protocols like STUN, TURN, and ICE?",
                "options": [
                    {"id": "A", "text": "Because P2P software cannot run over Ethernet"},
                    {"id": "B", "text": "Because neither peer knows its own externally reachable public IP/port, and neither can receive unsolicited incoming connection requests through the other peer's NAT firewall"},
                    {"id": "C", "text": "Because NAT routers throttle all UDP traffic to 1 kbps"},
                    {"id": "D", "text": "Because P2P requires classful Class A IP addresses"}
                ],
                "correctOptionIds": ["B"],
                "explanation": "In P2P, both hosts are behind NATs. Neither host can accept incoming connections from the other because neither NAT table contains a pre-existing entry. STUN/TURN servers help peers discover their public mappings and relay traffic.",
                "difficulty": "hard",
                "subtopic": "NAT Traversal & STUN"
            },
            {
                "id": "l11-q17",
                "type": "multi_choice",
                "question": "A typical home 'Wi-Fi router' purchased at retail is actually an integrated appliance combining which of the following physical network functions? (Select ALL that apply)",
                "options": [
                    {"id": "A", "text": "Layer 3 Router & NAT Gateway"},
                    {"id": "B", "text": "Multi-port Layer 2 Ethernet Switch & 802.11 Wireless Access Point"},
                    {"id": "C", "text": "Stateful Firewall & DHCP Server"},
                    {"id": "D", "text": "Autonomous System BGP Tier-1 Transit Core"}
                ],
                "correctOptionIds": ["A", "B", "C"],
                "explanation": "A consumer router integrates: an AP (Wi-Fi), a 4-port switch (L2 LAN), a router (L3 WAN/LAN), a DHCP server, a DNS proxy/caching resolver, and a NAT/SPI firewall. It is NOT a Tier-1 BGP internet backbone transit router.",
                "difficulty": "easy",
                "subtopic": "Home Router Architecture"
            },
            {
                "id": "l11-q18",
                "type": "single_choice",
                "question": "When a router performs NAT on an IP packet, what additional Layer 3 and Layer 4 header modifications MUST it recalculate?",
                "options": [
                    {"id": "A", "text": "It only changes the IP; no checksums are affected"},
                    {"id": "B", "text": "It must recalculate the IPv4 Header Checksum AND the TCP/UDP checksum (since TCP/UDP checksums include a pseudo-header containing source and destination IPs)"},
                    {"id": "C", "text": "It must recalculate the TLS cryptographic signature"},
                    {"id": "D", "text": "It must increment the TTL by 5"}
                ],
                "correctOptionIds": ["B"],
                "explanation": "Modifying the IP address alters the IPv4 header, requiring a new IPv4 header checksum. Furthermore, TCP and UDP compute their checksums over a 'pseudo-header' that includes the source and destination IP addresses, requiring L4 checksum recomputation.",
                "difficulty": "hard",
                "subtopic": "NAT Checksum Invalidation"
            },
            {
                "id": "l11-q19",
                "type": "single_choice",
                "question": "What is the purpose of a 'Default Gateway' configured on an office workstation?",
                "options": [
                    {"id": "A", "text": "It is the router interface on the local subnet to which all non-local outbound traffic (packets with destination IPs outside the local subnet) must be forwarded"},
                    {"id": "B", "text": "It is the DNS server that stores all web passwords"},
                    {"id": "C", "text": "It acts as a physical power supply for the Ethernet switch"},
                    {"id": "D", "text": "It translates IPv4 addresses into ASCII text"}
                ],
                "correctOptionIds": ["A"],
                "explanation": "When a host's subnet mask evaluation reveals that the destination IP is on an external network, the host encapsulates the packet into a frame addressed to the MAC address of its Default Gateway router.",
                "difficulty": "easy",
                "subtopic": "Default Gateway Role"
            },
            {
                "id": "l11-q20",
                "type": "single_choice",
                "question": "What happens if a DHCP server accidentally assigns an IP address that is already statically configured on another device on the same LAN?",
                "options": [
                    {"id": "A", "text": "The router reboots automatically"},
                    {"id": "B", "text": "An IP conflict occurs; packets intended for that IP oscillate between the two devices depending on whose ARP reply reaches switches last, causing erratic connection drops"},
                    {"id": "C", "text": "Bandwidth doubles because two machines share the traffic"},
                    {"id": "D", "text": "The switch converts all unicast traffic to fiber optics"}
                ],
                "correctOptionIds": ["B"],
                "explanation": "Two devices claiming the same IP will both respond to ARP requests for that IP. Switches and routers will continuously flap their ARP/CAM entries between the two MAC addresses, causing severe packet loss and broken TCP sessions.",
                "difficulty": "medium",
                "subtopic": "IP Conflict & ARP Thrashing"
            }
        ]
    }

    # =========================================================================
    # --- LECTURE 12: Network Troubleshooting ---
    # =========================================================================
    q["lecture-12"] = {
        "topicId": "lecture-12",
        "lectureNumber": 12,
        "title": "Network Troubleshooting Quiz",
        "description": "20 questions covering systematic bottom-up troubleshooting, CLI diagnostic tools (ping, traceroute, dig, netstat/ss, tcpdump, wireshark), MTU black holes, and packet loss diagnosis.",
        "estimatedMinutes": 25,
        "questions": [
            {
                "id": "l12-q01",
                "type": "single_choice",
                "question": "When diagnosing a total network outage on an enterprise computer, why is the 'Bottom-Up' troubleshooting methodology (Layer 1 -> Layer 7) standard industry practice?",
                "options": [
                    {"id": "A", "text": "Because higher layers are completely dependent on the health of lower layers; debugging application code or DNS is useless if the physical Ethernet cable is unplugged or the link is down"},
                    {"id": "B", "text": "Because Layer 1 commands run faster in Linux"},
                    {"id": "C", "text": "Because Layer 7 protocols do not use IP addresses"},
                    {"id": "D", "text": "Because physical layer cables can only be checked via SSH"}
                ],
                "correctOptionIds": ["A"],
                "explanation": "Network layering is strictly hierarchical: Layer 7 depends on Layer 4, which depends on Layer 3, which depends on Layer 2 and Layer 1. Verifying link lights, interface states, and local subnet reachability first eliminates basic underlying failures immediately.",
                "difficulty": "easy",
                "subtopic": "Bottom-Up Methodology"
            },
            {
                "id": "l12-q02",
                "type": "single_choice",
                "question": "What ICMP message types are exchanged during a successful `ping 8.8.8.8` execution?",
                "options": [
                    {"id": "A", "text": "Type 3 (Destination Unreachable) and Type 11 (Time Exceeded)"},
                    {"id": "B", "text": "Type 8 (Echo Request) and Type 0 (Echo Reply)"},
                    {"id": "C", "text": "Type 5 (Redirect) and Type 13 (Timestamp)"},
                    {"id": "D", "text": "Type 1 (SYN) and Type 2 (ACK)"}
                ],
                "correctOptionIds": ["B"],
                "explanation": "The client transmits an ICMP Type 8 Code 0 (Echo Request). The remote host replies with an ICMP Type 0 Code 0 (Echo Reply).",
                "difficulty": "easy",
                "subtopic": "ICMP & Ping"
            },
            {
                "id": "l12-q03",
                "type": "single_choice",
                "question": "A user can ping `142.250.195.46` successfully with 15ms latency, but running `ping google.com` fails with 'Name or service not known'. At which layer is the problem located?",
                "options": [
                    {"id": "A", "text": "Layer 1 — The physical Ethernet cable is disconnected"},
                    {"id": "B", "text": "Layer 2 — The switch MAC address table is full"},
                    {"id": "C", "text": "Layer 7 / Application — DNS resolution failure (misconfigured DNS server in /etc/resolv.conf or unreachable DNS)"},
                    {"id": "D", "text": "Layer 3 — The default gateway has crashed"}
                ],
                "correctOptionIds": ["C"],
                "explanation": "Pinging the raw IP works, proving Layer 1, 2, and 3 routing to the internet are fully functional. Failure to ping the hostname proves the failure is specifically within DNS resolution.",
                "difficulty": "easy",
                "subtopic": "DNS vs IP Connectivity"
            },
            {
                "id": "l12-q04",
                "type": "single_choice",
                "question": "How does `traceroute` (or Windows `tracert`) identify each successive intermediate router along an internet path?",
                "options": [
                    {"id": "A", "text": "It queries the BGP routing table of the destination host"},
                    {"id": "B", "text": "It sends probe packets with increasing TTL values (TTL=1, TTL=2, TTL=3...); each successive router decrements TTL to 0, discards the packet, and sends back an ICMP Type 11 (Time Exceeded) message revealing its own IP"},
                    {"id": "C", "text": "It inspects the local switch's STP spanning tree topology"},
                    {"id": "D", "text": "It forces every router to append its hostname to the TCP payload"}
                ],
                "correctOptionIds": ["B"],
                "explanation": "When an IP packet's TTL drops to 0, RFC 792 dictates that the router must drop it and generate an ICMP Type 11 Code 0 (Time Exceeded) back to the sender. The source IP of that ICMP packet reveals the router's identity at that specific hop distance.",
                "difficulty": "medium",
                "subtopic": "Traceroute Mechanics"
            },
            {
                "id": "l12-q05",
                "type": "single_choice",
                "question": "In a traceroute output, what does a hop displaying `* * * Request timed out` typically indicate?",
                "options": [
                    {"id": "A", "text": "The entire internet connection is severed at that point"},
                    {"id": "B", "text": "That specific intermediate router (or firewall) is configured to ignore or rate-limit ICMP TTL-exceeded messages, or drops inbound probe traffic, even while forwarding normal transit traffic"},
                    {"id": "C", "text": "The destination server has crashed"},
                    {"id": "D", "text": "The client computer has run out of RAM"}
                ],
                "correctOptionIds": ["B"],
                "explanation": "Asterisks simply mean that no ICMP response was received within the timeout. Many core carrier routers drop or deprioritize ICMP generation to protect their CPUs while still forwarding data-plane transit packets at full line rate.",
                "difficulty": "medium",
                "subtopic": "Interpreting Traceroute Asterisks"
            },
            {
                "id": "l12-q06",
                "type": "single_choice",
                "question": "What is an 'MTU Black Hole' and how does it manifest to an end-user?",
                "options": [
                    {"id": "A", "text": "An astronomical anomaly that swallows data centers"},
                    {"id": "B", "text": "A network path where an intermediate link has a lower MTU (e.g. 1420 bytes on a VPN tunnel), but an intermediate firewall drops ICMP 'Fragmentation Needed' packets, causing small packets (ping, handshake) to work while large data packets hang indefinitely"},
                    {"id": "C", "text": "A damaged RJ-45 cable that only transmits half-duplex signals"},
                    {"id": "D", "text": "A DNS server that returns 0.0.0.0 for all queries"}
                ],
                "correctOptionIds": ["B"],
                "explanation": "If a router cannot forward a packet because packet size > MTU and the DF (Don't Fragment) flag is set, it drops the packet and generates ICMP Type 3 Code 4. If a firewall blocks this ICMP packet, Path MTU Discovery (PMTUD) fails: small packets (SYN, ACK) work, but HTTP responses with large payloads hang forever.",
                "difficulty": "hard",
                "subtopic": "PMTUD Black Hole"
            },
            {
                "id": "l12-q07",
                "type": "single_choice",
                "question": "What `ping` command flag combination can be used on Linux to diagnose an MTU black hole by enforcing Don't Fragment (DF)?",
                "options": [
                    {"id": "A", "text": "ping -c 4 -M do -s 1472 <destination_ip>"},
                    {"id": "B", "text": "ping -t 64 -v 1500 <destination_ip>"},
                    {"id": "C", "text": "ping --tcp --force-mtu <destination_ip>"},
                    {"id": "D", "text": "ping -a -b -c <destination_ip>"}
                ],
                "correctOptionIds": ["A"],
                "explanation": "On Linux, `-M do` sets the DF bit, and `-s 1472` sets the ICMP payload size (1472 payload + 8 ICMP header + 20 IP header = 1500 byte IP packet). If this fails, the MTU on the path is smaller than 1500.",
                "difficulty": "hard",
                "subtopic": "MTU CLI Diagnosis"
            },
            {
                "id": "l12-q08",
                "type": "single_choice",
                "question": "What modern Linux command has replaced legacy `netstat` to inspect active listening TCP ports, socket states, and associated process IDs?",
                "options": [
                    {"id": "A", "text": "route -n"},
                    {"id": "B", "text": "ss (Socket Statistics, e.g. `ss -tulpn`)"},
                    {"id": "C", "text": "arp -a"},
                    {"id": "D", "text": "ifconfig -a"}
                ],
                "correctOptionIds": ["B"],
                "explanation": "`ss` (from the `iproute2` suite) queries socket information directly from kernel netlink interfaces, making it orders of magnitude faster than `netstat` (which read `/proc/net/tcp` line by line).",
                "difficulty": "easy",
                "subtopic": "Modern Diagnostic Tools (ss)"
            },
            {
                "id": "l12-q09",
                "type": "single_choice",
                "question": "What is the primary diagnostic utility to query DNS records in-depth, inspect response flags, and follow iterative delegations directly from root servers (`+trace`)?",
                "options": [
                    {"id": "A", "text": "dig (Domain Information Groper)"},
                    {"id": "B", "text": "ping"},
                    {"id": "C", "text": "traceroute"},
                    {"id": "D", "text": "telnet"}
                ],
                "correctOptionIds": ["A"],
                "explanation": "`dig` is the standard tool used by network administrators. It reveals the exact raw DNS response, including QUESTION, ANSWER, AUTHORITY, and ADDITIONAL sections, TTLs, and DNSSEC signatures.",
                "difficulty": "easy",
                "subtopic": "DNS Troubleshooting with dig"
            },
            {
                "id": "l12-q10",
                "type": "single_choice",
                "question": "When capturing live traffic on a Linux server using `tcpdump`, what Berkeley Packet Filter (BPF) syntax captures ONLY HTTP traffic (port 80) destined to or originating from host 10.0.0.5?",
                "options": [
                    {"id": "A", "text": "tcpdump 'port 80 and host 10.0.0.5'"},
                    {"id": "B", "text": "tcpdump --filter=http://10.0.0.5"},
                    {"id": "C", "text": "tcpdump -L2 80 10.0.0.5"},
                    {"id": "D", "text": "tcpdump GET 10.0.0.5"}
                ],
                "correctOptionIds": ["A"],
                "explanation": "BPF syntax uses logical boolean operators: `tcpdump 'port 80 and host 10.0.0.5'` compiles into kernel-level bytecode that filters out all other irrelevant traffic before copying packets to userspace.",
                "difficulty": "medium",
                "subtopic": "tcpdump BPF Filtering"
            },
            {
                "id": "l12-q11",
                "type": "single_choice",
                "question": "In Wireshark, what visual indicator typically signals high packet loss or severe out-of-order delivery during a TCP session?",
                "options": [
                    {"id": "A", "text": "Packets highlighted with 'TCP Retransmission', 'TCP Dup ACK', and 'TCP Fast Retransmission' warnings"},
                    {"id": "B", "text": "All packets turn green"},
                    {"id": "C", "text": "The Wireshark window automatically closes"},
                    {"id": "D", "text": "The source IP changes to 0.0.0.0"}
                ],
                "correctOptionIds": ["A"],
                "explanation": "Wireshark's TCP expert analysis highlights retransmissions (sender timeout), duplicate ACKs (receiver signaling missing gaps), and Out-of-Order segments in distinctive black/red coloring.",
                "difficulty": "easy",
                "subtopic": "Wireshark Packet Analysis"
            },
            {
                "id": "l12-q12",
                "type": "single_choice",
                "question": "A network administrator notices that a server's link status light is amber and throughput is capped at 10 Mbps half-duplex with massive CRC collision errors on a 1 Gbps port. What is the most likely root cause?",
                "options": [
                    {"id": "A", "text": "Duplex/Speed autonegotiation mismatch or a physically damaged twisted-pair Ethernet cable (missing pins 4, 5, 7, 8)"},
                    {"id": "B", "text": "An expired TLS certificate on the server"},
                    {"id": "C", "text": "A DNS round-robin misconfiguration"},
                    {"id": "D", "text": "The server has too many open browser tabs"}
                ],
                "correctOptionIds": ["A"],
                "explanation": "Gigabit Ethernet requires all 4 twisted pairs in Cat5e/Cat6. Damaged pins or disabling autonegotiation on one side causes the link to fall back to 10/100 Mbps half-duplex, resulting in catastrophic collision errors.",
                "difficulty": "medium",
                "subtopic": "Physical/Data Link Layer Issues"
            },
            {
                "id": "l12-q13",
                "type": "single_choice",
                "question": "A host with IP `192.168.1.50/24` cannot communicate with a server on `192.168.2.10/24`. Pinging the local gateway `192.168.1.1` succeeds. What does this confirm?",
                "options": [
                    {"id": "A", "text": "Local Layer 2/3 connectivity to the default gateway is healthy; the failure lies in the router's routing table (RIB/FIB) or upstream forwarding towards 192.168.2.0/24"},
                    {"id": "B", "text": "The client computer has a broken network card"},
                    {"id": "C", "text": "The client's ARP table is corrupted"},
                    {"id": "D", "text": "The server at 192.168.2.10 is running an expired Windows license"}
                ],
                "correctOptionIds": ["A"],
                "explanation": "Successful ping to the gateway proves the local NIC, physical cable, switch port, IP configuration, and ARP mapping for the gateway are working. The failure is downstream routing or ACLs blocking traffic to the remote subnet.",
                "difficulty": "medium",
                "subtopic": "Isolating Subnet Routing Failures"
            },
            {
                "id": "l12-q14",
                "type": "single_choice",
                "question": "What is the significance of the `TIME_WAIT` count exploding to tens of thousands in `ss -s` output on a busy web server?",
                "options": [
                    {"id": "A", "text": "The server's ephemeral port range is exhausted because the server (or backend reverse proxy) is opening and rapidly closing thousands of short-lived TCP connections without connection pooling"},
                    {"id": "B", "text": "The hard drive is failing"},
                    {"id": "C", "text": "The web server has been hacked via SQL injection"},
                    {"id": "D", "text": "DNS records have expired"}
                ],
                "correctOptionIds": ["A"],
                "explanation": "When an application closes TCP connections actively at high request rates without HTTP Keep-Alive / connection pooling, sockets linger in TIME_WAIT for 2*MSL (60s). This exhausts the 65,535 ephemeral port space, causing connection errors.",
                "difficulty": "hard",
                "subtopic": "TIME_WAIT Socket Exhaustion"
            },
            {
                "id": "l12-q15",
                "type": "single_choice",
                "question": "What command on Linux displays the kernel's active IPv4 routing table, interface bindings, and default gateways?",
                "options": [
                    {"id": "A", "text": "ip route show (or `ip r`)"},
                    {"id": "B", "text": "ip link set dev eth0 up"},
                    {"id": "C", "text": "systemctl restart networking"},
                    {"id": "D", "text": "cat /etc/hosts"}
                ],
                "correctOptionIds": ["A"],
                "explanation": "`ip route show` displays the Kernel FIB, listing destination prefixes, gateways, outgoing devices, and routing metrics.",
                "difficulty": "easy",
                "subtopic": "Linux Routing Diagnostics"
            },
            {
                "id": "l12-q16",
                "type": "single_choice",
                "question": "If an engineer runs `curl -v https://example.com` and it hangs at `* Connected to example.com (93.184.216.34) port 443`, but never completes `* TLS 1.3 connection established`, what is the most likely diagnosis?",
                "options": [
                    {"id": "A", "text": "DNS failure"},
                    {"id": "B", "text": "TCP 3-way handshake succeeded, but a stateful firewall or middlebox is blocking or dropping the TLS ClientHello / ServerHello packets"},
                    {"id": "C", "text": "The client computer's keyboard is unplugged"},
                    {"id": "D", "text": "The Ethernet cable is unplugged"}
                ],
                "correctOptionIds": ["B"],
                "explanation": "`Connected to...` means the TCP 3-way handshake on port 443 completed successfully. The hang during the TLS handshake points to an SSL/TLS inspection middlebox, MTU issue dropping large certificate packets, or security firewall.",
                "difficulty": "hard",
                "subtopic": "TLS Handshake Troubleshooting"
            },
            {
                "id": "l12-q17",
                "type": "single_choice",
                "question": "What is the role of `iperf3` in network performance troubleshooting?",
                "options": [
                    {"id": "A", "text": "It scans websites for security vulnerabilities"},
                    {"id": "B", "text": "It measures pure active Layer 4 network throughput, bandwidth, jitter, and packet loss between a client and server without disk I/O bottlenecks"},
                    {"id": "C", "text": "It cracks WPA2 Wi-Fi passwords"},
                    {"id": "D", "text": "It creates DNS records"}
                ],
                "correctOptionIds": ["B"],
                "explanation": "`iperf3` generates synthetic TCP/UDP streams between two endpoints, measuring raw maximum throughput and packet loss to isolate network link capacity from disk or application bottlenecks.",
                "difficulty": "medium",
                "subtopic": "Bandwidth Testing (iperf3)"
            },
            {
                "id": "l12-q18",
                "type": "multi_choice",
                "question": "Which of the following symptoms indicate a Layer 2 Spanning Tree Protocol (STP) broadcast storm on a switched campus network? (Select ALL that apply)",
                "options": [
                    {"id": "A", "text": "Switch link activity LEDs flashing frantically in unison across all ports"},
                    {"id": "B", "text": "Switch CPU utilization reaching 100%"},
                    {"id": "C", "text": "Severe packet drop and inability of hosts to obtain DHCP leases or resolve ARP requests"},
                    {"id": "D", "text": "Automatic upgrade from IPv4 to IPv6"}
                ],
                "correctOptionIds": ["A", "B", "C"],
                "explanation": "A switching loop causes broadcast frames (like ARP or DHCP) to multiply exponentially without TTL expiration. Switches flood their backplanes, CPU maxes out processing control packets, and legitimate traffic drops to zero.",
                "difficulty": "medium",
                "subtopic": "STP Broadcast Storms"
            },
            {
                "id": "l12-q19",
                "type": "single_choice",
                "question": "What is the purpose of testing reachability to `127.0.0.1` (`ping 127.0.0.1`) during troubleshooting?",
                "options": [
                    {"id": "A", "text": "To verify that the local operating system's TCP/IP network protocol stack and loopback interface (`lo`) are functional"},
                    {"id": "B", "text": "To test whether the external internet fiber cable is unbroken"},
                    {"id": "C", "text": "To ping the nearest Google edge node"},
                    {"id": "D", "text": "To check if the Wi-Fi password is correct"}
                ],
                "correctOptionIds": ["A"],
                "explanation": "Pinging the loopback interface (`127.0.0.1`) does not send any signals out to the physical wire; it stays entirely within the OS kernel. If this fails, the local TCP/IP stack or network drivers are corrupt.",
                "difficulty": "easy",
                "subtopic": "Loopback Interface Verification"
            },
            {
                "id": "l12-q20",
                "type": "single_choice",
                "question": "When analyzing a packet capture of a broken TCP session, what does receiving an immediate packet with the `RST` (Reset) flag set by the destination port indicate?",
                "options": [
                    {"id": "A", "text": "The destination host received the packet, but no application process is actively listening on that target port (port closed)"},
                    {"id": "B", "text": "The connection was encrypted with AES-256"},
                    {"id": "C", "text": "The packet reached maximum throughput"},
                    {"id": "D", "text": "The destination host is requesting a higher window size"}
                ],
                "correctOptionIds": ["A"],
                "explanation": "When an OS receives a TCP SYN for a port where no process has bound a listening socket, the kernel rejects the connection immediately by sending a TCP packet with the `RST` flag set.",
                "difficulty": "medium",
                "subtopic": "TCP RST Interpretation"
            }
        ]
    }

    # =========================================================================
    # --- LECTURE 13: The Complete Internet Journey ---
    # =========================================================================
    q["lecture-13"] = {
        "topicId": "lecture-13",
        "lectureNumber": 13,
        "title": "The Complete Internet Journey Quiz",
        "description": "20 questions tracing an end-to-end HTTPS request from URL entry, DNS resolution, ARP, routing, TCP handshake, TLS 1.3 encryption, to HTTP response rendering.",
        "estimatedMinutes": 25,
        "questions": [
            {
                "id": "l13-q01",
                "type": "single_choice",
                "question": "When a user types `https://www.example.com` into a web browser address bar and hits Enter, what is the VERY FIRST operation executed by the browser before any network packet is dispatched?",
                "options": [
                    {"id": "A", "text": "Transmitting an ARP broadcast on the local Ethernet switch"},
                    {"id": "B", "text": "Parsing the URL string, checking the browser's internal HSTS (HTTP Strict Transport Security) preload list, and checking the local browser/OS DNS cache"},
                    {"id": "C", "text": "Opening a TCP socket to root nameserver a.root-servers.net"},
                    {"id": "D", "text": "Sending an HTTP GET request over raw IP"}
                ],
                "correctOptionIds": ["B"],
                "explanation": "Before generating packets, the browser validates the URL syntax, checks if HSTS forces HTTPS, and queries local memory caches (browser DNS cache, OS resolver cache, `/etc/hosts`).",
                "difficulty": "easy",
                "subtopic": "URL Parsing & Cache Lookup"
            },
            {
                "id": "l13-q02",
                "type": "single_choice",
                "question": "If the domain name is NOT found in the browser cache, OS cache, or hosts file, to what network entity does the operating system dispatch its DNS query?",
                "options": [
                    {"id": "A", "text": "To the Root Nameserver directly"},
                    {"id": "B", "text": "To the Recursive DNS Resolver configured in network settings (typically assigned via DHCP)"},
                    {"id": "C", "text": "To the website's web server"},
                    {"id": "D", "text": "To the local switch's MAC table"}
                ],
                "correctOptionIds": ["B"],
                "explanation": "Stub resolvers on client endpoints forward recursive queries to a designated Recursive Resolver (e.g. ISP resolver, 1.1.1.1, 8.8.8.8) that performs the full iterative resolution walk.",
                "difficulty": "easy",
                "subtopic": "Resolver Dispatch"
            },
            {
                "id": "l13-q03",
                "type": "single_choice",
                "question": "During the recursive resolver's lookup walk for `www.example.com`, which nameserver provides the referral delegation pointing to the `.com` TLD nameservers?",
                "options": [
                    {"id": "A", "text": "The Authoritative Nameserver for example.com"},
                    {"id": "B", "text": "The DNS Root Nameserver (one of the 13 anycast root clusters)"},
                    {"id": "C", "text": "The local home router"},
                    {"id": "D", "text": "The Google Web Crawler"}
                ],
                "correctOptionIds": ["B"],
                "explanation": "The Root Nameservers hold the top of the tree. When asked for `www.example.com`, the root server replies with NS records pointing to the TLD servers responsible for the `.com` zone.",
                "difficulty": "medium",
                "subtopic": "DNS Delegation Walk"
            },
            {
                "id": "l13-q04",
                "type": "single_choice",
                "question": "Once the client obtains destination IP `93.184.216.34`, how does the OS determine whether to send the frame directly to the web server or to its Default Gateway?",
                "options": [
                    {"id": "A", "text": "It checks if the server port is 443 or 80"},
                    {"id": "B", "text": "It performs a bitwise AND between destination IP and its own Subnet Mask; if the resulting network ID differs from its own local subnet, it routes via the Default Gateway"},
                    {"id": "C", "text": "It sends a ping to the web server to test distance"},
                    {"id": "D", "text": "It asks the DNS server for routing instructions"}
                ],
                "correctOptionIds": ["B"],
                "explanation": "`Local Subnet Check = (Dest IP & Subnet Mask) == (Host IP & Subnet Mask)`. If false, destination is remote, requiring forwarding to the Default Gateway.",
                "difficulty": "medium",
                "subtopic": "Local vs Remote Subnet Decision"
            },
            {
                "id": "l13-q05",
                "type": "single_choice",
                "question": "When constructing the Layer 2 Ethernet frame for an outbound packet to `93.184.216.34` via Default Gateway `192.168.1.1`, what is the destination MAC address placed in the frame header?",
                "options": [
                    {"id": "A", "text": "The MAC address of the remote web server (`93.184.216.34`)"},
                    {"id": "B", "text": "The MAC address of the local Default Gateway router (`192.168.1.1`)"},
                    {"id": "C", "text": "Broadcast MAC (FF:FF:FF:FF:FF:FF)"},
                    {"id": "D", "text": "00:00:00:00:00:00"}
                ],
                "correctOptionIds": ["B"],
                "explanation": "MAC addresses are strictly link-local and hop-by-hop. The packet retains Destination IP = `93.184.216.34`, but the Ethernet frame Destination MAC MUST be the local gateway router's MAC address.",
                "difficulty": "medium",
                "subtopic": "L2 vs L3 Addressing in Transit"
            },
            {
                "id": "l13-q06",
                "type": "single_choice",
                "question": "If the host does not have the Default Gateway's MAC address in its local memory, what protocol is triggered immediately to discover it?",
                "options": [
                    {"id": "A", "text": "BGP"},
                    {"id": "B", "text": "ARP (Address Resolution Protocol broadcast)"},
                    {"id": "C", "text": "DHCP"},
                    {"id": "D", "text": "TLS Handshake"}
                ],
                "correctOptionIds": ["B"],
                "explanation": "Before the Ethernet frame can be placed onto the wire, the host must resolve the gateway IP to a MAC address using an ARP Request broadcast.",
                "difficulty": "easy",
                "subtopic": "ARP Resolution Trigger"
            },
            {
                "id": "l13-q07",
                "type": "single_choice",
                "question": "As the Ethernet frame passes through an intermediate Layer 2 Ethernet switch on the LAN, how does the switch determine which output port to forward it to?",
                "options": [
                    {"id": "A", "text": "It inspects the Destination MAC address and looks up the corresponding port in its MAC Address Table (CAM Table)"},
                    {"id": "B", "text": "It recalculates the IP checksum"},
                    {"id": "C", "text": "It decrypts the TLS application data"},
                    {"id": "D", "text": "It queries the DNS server"}
                ],
                "correctOptionIds": ["A"],
                "explanation": "Layer 2 switches operate by inspecting the Destination MAC address and forwarding the frame out the specific port associated with that MAC in the CAM (Content Addressable Memory) table.",
                "difficulty": "easy",
                "subtopic": "Switch CAM Forwarding"
            },
            {
                "id": "l13-q08",
                "type": "multi_choice",
                "question": "When the packet reaches the Default Gateway router, what modifications are performed on the packet before it is forwarded out the WAN interface? (Select ALL that apply)",
                "options": [
                    {"id": "A", "text": "The router decrements the IPv4 Time to Live (TTL) by 1"},
                    {"id": "B", "text": "The router recalculates the IPv4 Header Checksum"},
                    {"id": "C", "text": "The router performs NAT/PAT, rewriting the private source IP/port with its public IP/port"},
                    {"id": "D", "text": "The router strips the incoming Layer 2 Ethernet frame and encapsulates the packet in a new Layer 2 frame for the WAN link"}
                ],
                "correctOptionIds": ["A", "B", "C", "D"],
                "explanation": "Every routing hop decrements TTL, updates header checksum, strips old L2 framing and encapsulates into new L2 framing. A NAT gateway additionally rewrites source IP/port.",
                "difficulty": "hard",
                "subtopic": "Router Forwarding Lifecycle"
            },
            {
                "id": "l13-q09",
                "type": "single_choice",
                "question": "In internet transit across ISP backbones, what mechanism do core routers use to perform Longest Prefix Match (LPM) lookups in nanoseconds at line rate?",
                "options": [
                    {"id": "A", "text": "Binary tree search in main DDR4 RAM"},
                    {"id": "B", "text": "Hardware TCAM (Ternary Content Addressable Memory) in application-specific integrated circuits (ASICs)"},
                    {"id": "C", "text": "Sequential linear search through an ASCII text file"},
                    {"id": "D", "text": "Python dictionaries"}
                ],
                "correctOptionIds": ["B"],
                "explanation": "TCAM allows matching across 0, 1, and 'don't care' wildcard bits in parallel across all FIB entries in a single clock cycle, enabling wire-speed forwarding.",
                "difficulty": "medium",
                "subtopic": "TCAM Hardware Forwarding"
            },
            {
                "id": "l13-q10",
                "type": "single_choice",
                "question": "Which protocol governs the inter-domain path selection between the user's ISP, transit carriers (Tier-1 providers), and the web server's hosting cloud network?",
                "options": [
                    {"id": "A", "text": "OSPF"},
                    {"id": "B", "text": "BGP (Border Gateway Protocol)"},
                    {"id": "C", "text": "RIPv2"},
                    {"id": "D", "text": "STP"}
                ],
                "correctOptionIds": ["B"],
                "explanation": "BGP is the de-facto exterior gateway routing protocol connecting autonomous systems (ASNs) across the global internet.",
                "difficulty": "easy",
                "subtopic": "BGP Internet Transit"
            },
            {
                "id": "l13-q11",
                "type": "single_choice",
                "question": "Once packets reach the web server's network and firewall, what transport layer handshake is executed to establish a reliable connection before any HTTPS data is sent?",
                "options": [
                    {"id": "A", "text": "DHCP DORA 4-way exchange"},
                    {"id": "B", "text": "TCP 3-Way Handshake (SYN, SYN-ACK, ACK)"},
                    {"id": "C", "text": "BGP Keepalive exchange"},
                    {"id": "D", "text": "ARP Who-has query"}
                ],
                "correctOptionIds": ["B"],
                "explanation": "TCP establishes a full-duplex byte stream via SYN, SYN-ACK, and ACK, establishing sequence numbers and flow control buffers.",
                "difficulty": "easy",
                "subtopic": "TCP Connection Setup"
            },
            {
                "id": "l13-q12",
                "type": "single_choice",
                "question": "In TLS 1.3, how many round trips (RTT) are required for the cryptographic handshake to establish encryption keys before application data can be sent?",
                "options": [
                    {"id": "A", "text": "3 RTTs"},
                    {"id": "B", "text": "2 RTTs"},
                    {"id": "C", "text": "1 RTT (Client sends ClientHello with Key Share; Server replies with ServerHello, Certificate, and Finished)"},
                    {"id": "D", "text": "0 RTT is mandatory for all first-time connections"}
                ],
                "correctOptionIds": ["C"],
                "explanation": "TLS 1.3 reduced the handshake from 2 RTTs (in TLS 1.2) to just 1 RTT by combining the key share (Diffie-Hellman parameters) directly inside the initial `ClientHello` message.",
                "difficulty": "medium",
                "subtopic": "TLS 1.3 Handshake Latency"
            },
            {
                "id": "l13-q13",
                "type": "single_choice",
                "question": "What is the role of the Public Key Infrastructure (PKI) and Certificate Authorities (CAs) during the TLS handshake?",
                "options": [
                    {"id": "A", "text": "They assign IP addresses to web servers"},
                    {"id": "B", "text": "They allow the client to cryptographically verify that the server's public key belongs legitimately to `example.com` by validating digital signatures against pre-installed Root CA certificates in the OS/browser trust store"},
                    {"id": "C", "text": "They compress the HTML before sending"},
                    {"id": "D", "text": "They maintain the router's BGP routing table"}
                ],
                "correctOptionIds": ["B"],
                "explanation": "The server presents a certificate signed by an intermediate CA, leading up to a trusted Root CA embedded in the client's OS trust store. This prevents Man-in-the-Middle (MITM) impersonation attacks.",
                "difficulty": "medium",
                "subtopic": "PKI & Certificate Validation"
            },
            {
                "id": "l13-q14",
                "type": "single_choice",
                "question": "Why does TLS use asymmetric public-key cryptography (like ECDHE) ONLY during the initial handshake, switching to symmetric cryptography (like AES-GCM or ChaCha20) for actual HTTP payload data?",
                "options": [
                    {"id": "A", "text": "Symmetric encryption is orders of magnitude faster and computationally cheaper on CPU hardware than asymmetric public-key operations"},
                    {"id": "B", "text": "Asymmetric encryption cannot encrypt text, only numbers"},
                    {"id": "C", "text": "Symmetric encryption keys are publicly visible on DNS servers"},
                    {"id": "D", "text": "Asymmetric encryption does not work over Wi-Fi"}
                ],
                "correctOptionIds": ["A"],
                "explanation": "Asymmetric cryptography involves heavy modular arithmetic, which would overwhelm server CPUs at gigabit speeds. Hence, asymmetric keys are used only to securely negotiate a shared symmetric key, which AES hardware instructions encrypt in nanoseconds.",
                "difficulty": "medium",
                "subtopic": "Asymmetric vs Symmetric Encryption"
            },
            {
                "id": "l13-q15",
                "type": "single_choice",
                "question": "What is the purpose of the 'Host' header sent in an HTTP/1.1 request (e.g. `Host: www.example.com`)?",
                "options": [
                    {"id": "A", "text": "It tells the router which gateway to use"},
                    {"id": "B", "text": "It allows a single web server with one IP address to host hundreds of different websites (Virtual Hosting), routing requests to the correct virtual host"},
                    {"id": "C", "text": "It specifies the user's MAC address"},
                    {"id": "D", "text": "It disables TLS encryption"}
                ],
                "correctOptionIds": ["B"],
                "explanation": "Without the `Host` header, a web server hosting multiple domains on the same IP wouldn't know which website the client wanted. RFC 2616 made `Host` mandatory for virtual hosting.",
                "difficulty": "easy",
                "subtopic": "HTTP Virtual Hosting"
            },
            {
                "id": "l13-q16",
                "type": "single_choice",
                "question": "What HTTP response header instructs the browser to cache an image asset locally for 1 year without re-requesting it from the origin server?",
                "options": [
                    {"id": "A", "text": "Cache-Control: public, max-age=31536000, immutable"},
                    {"id": "B", "text": "Set-Cookie: session=active; ttl=31536000"},
                    {"id": "C", "text": "Connection: keep-alive"},
                    {"id": "D", "text": "Content-Encoding: gzip"}
                ],
                "correctOptionIds": ["A"],
                "explanation": "`Cache-Control: max-age=31536000` sets the browser cache expiry to 31,536,000 seconds (1 year). The `immutable` attribute signals that the resource will never change, eliminating conditional revalidation requests.",
                "difficulty": "medium",
                "subtopic": "HTTP Caching Headers"
            },
            {
                "id": "l13-q17",
                "type": "single_choice",
                "question": "When the browser receives the raw HTML response body, what critical parsing operations occur to turn text into pixels on the user's screen?",
                "options": [
                    {"id": "A", "text": "Generating the DOM (Document Object Model), CSSOM (CSS Object Model), combining them into a Render Tree, executing Layout (reflow), and Painting pixels to the screen"},
                    {"id": "B", "text": "Writing the HTML directly into the router's ARP cache"},
                    {"id": "C", "text": "Transmitting an ICMP Echo Reply to the DNS root"},
                    {"id": "D", "text": "Converting the HTML into a BGP advertisement"}
                ],
                "correctOptionIds": ["A"],
                "explanation": "The browser parsing pipeline: Tokenize HTML -> DOM Tree; Parse CSS -> CSSOM Tree; Combine -> Render Tree -> Layout (compute geometry) -> Paint (rasterize pixels to GPU).",
                "difficulty": "easy",
                "subtopic": "Browser Rendering Pipeline"
            },
            {
                "id": "l13-q18",
                "type": "single_choice",
                "question": "What major performance advantage did HTTP/2 introduce over HTTP/1.1 to eliminate Head-of-Line (HoL) blocking at the application layer?",
                "options": [
                    {"id": "A", "text": "Binary framing and multiplexing of multiple concurrent request/response streams over a single shared TCP connection"},
                    {"id": "B", "text": "Switching from IP to MAC routing"},
                    {"id": "C", "text": "Eliminating all TLS encryption"},
                    {"id": "D", "text": "Increasing maximum packet MTU to 9000 bytes"}
                ],
                "correctOptionIds": ["A"],
                "explanation": "HTTP/1.1 required multiple parallel TCP connections or serial pipelining. HTTP/2 introduces binary streams, interleaving frames of multiple requests and responses concurrently over one TCP pipe.",
                "difficulty": "medium",
                "subtopic": "HTTP/2 Multiplexing"
            },
            {
                "id": "l13-q19",
                "type": "single_choice",
                "question": "Why did HTTP/3 shift its underlying transport layer from TCP to QUIC (running over UDP)?",
                "options": [
                    {"id": "A", "text": "To make web pages load without internet access"},
                    {"id": "B", "text": "To eliminate TCP-level Head-of-Line blocking (where one dropped packet stalls all multiplexed streams), and to combine the transport and cryptographic handshake into 0-RTT/1-RTT"},
                    {"id": "C", "text": "Because UDP is more secure than TCP"},
                    {"id": "D", "text": "Because TCP ports are deprecated by ICANN"}
                ],
                "correctOptionIds": ["B"],
                "explanation": "In HTTP/2 over TCP, if a single packet drops, TCP's in-order guarantee freezes all streams until retransmission completes. QUIC solves this by implementing independent stream loss recovery on top of UDP.",
                "difficulty": "hard",
                "subtopic": "HTTP/3 & QUIC"
            },
            {
                "id": "l13-q20",
                "type": "single_choice",
                "question": "When the browser finishes receiving all assets and the user closes the tab, how is the underlying TCP connection cleanly terminated?",
                "options": [
                    {"id": "A", "text": "The computer powers off"},
                    {"id": "B", "text": "Via a 4-way handshake (FIN -> ACK, FIN -> ACK), and the socket enters TIME_WAIT to ensure all delayed duplicate packets drain"},
                    {"id": "C", "text": "The switch clears its CAM table"},
                    {"id": "D", "text": "An ARP broadcast is sent to clear DNS records"}
                ],
                "correctOptionIds": ["B"],
                "explanation": "The full lifecycle concludes with TCP's full-duplex teardown: both sides independently send FIN and acknowledge with ACK, with the active closer waiting out the TIME_WAIT interval.",
                "difficulty": "easy",
                "subtopic": "End-to-End Teardown"
            }
        ]
    }

    return q

if __name__ == "__main__":
    quizzes = get_lectures_09_to_13_quizzes()
    print(f"Loaded {len(quizzes)} quiz modules for Lectures 09-13.")
    for k, v in quizzes.items():
        print(f"  {k}: {len(v['questions'])} questions")
