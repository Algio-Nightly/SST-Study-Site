"""
Lecture 11 Quiz: NAT, DHCP & Local Network Communication
20 Advanced Multi-Correct MCQs (5 options each, 2 to 5 correct answers)
"""

QUIZ_L11 = {
    "topicId": "lecture-11",
    "lectureNumber": 11,
    "title": "NAT, DHCP & Local Networks Master Quiz",
    "description": "20 rigorous multi-correct questions covering the End-to-End Principle, 28-byte ARP packet format, Gratuitous ARP, ARP spoofing & DAI, NAPT/PAT state tables, Cone vs Symmetric NAT, STUN/TURN/ICE, DHCP DORA and lease timers (T1/T2), Option 82, and container networking.",
    "estimatedMinutes": 35,
    "questions": [
        {
            "id": "l11-q01",
            "type": "multi_choice",
            "question": "Which of the following statements correctly represent the classical 'End-to-End Principle' (Saltzer, Reed, and Clark, 1981) and how Network Address Translation (NAT) impacts it?",
            "options": [
                {"id": "A", "text": "The End-to-End Principle asserts that communication functions should be implemented at the end hosts rather than inside intermediate network nodes unless strictly necessary for performance."},
                {"id": "B", "text": "Under pure End-to-End architecture, intermediate routers maintain zero per-flow connection state, providing stateless, survivable packet forwarding."},
                {"id": "C", "text": "NAT fundamentally violates the End-to-End Principle by forcing stateful connection tracking and packet rewriting into intermediate middleboxes."},
                {"id": "D", "text": "NAT breaks peer-to-peer protocols (such as SIP, WebRTC, and BitTorrent) because hosts behind NAT cannot advertise their private IP addresses to external peers for incoming connections."},
                {"id": "E", "text": "The End-to-End Principle was originally designed to prevent routers from running OSPF routing algorithms."}
            ],
            "correctOptionIds": ["A", "B", "C", "D"],
            "explanation": "Statements A, B, C, and D are correct. Saltzer's End-to-End principle placed intelligence and state at endpoints while keeping the core simple and stateless (A & B). NAT violates this by creating stateful flow tables inside routers (C), breaking incoming peer-to-peer connections and protocols embedding IP addresses in payloads (D). E is false; OSPF is an interior routing protocol and completely unrelated to the end-to-end principle.",
            "difficulty": "medium",
            "subtopic": "End-to-End Principle & Middleboxes"
        },
        {
            "id": "l11-q02",
            "type": "multi_choice",
            "question": "In the standard 28-byte Address Resolution Protocol (ARP - RFC 826) packet format for IPv4 over Ethernet, which of the following fields and values are accurate?",
            "options": [
                {"id": "A", "text": "Hardware Type (HTYPE): Set to `0x0001` to denote Ethernet."},
                {"id": "B", "text": "Protocol Type (PTYPE): Set to `0x0800` to denote the IPv4 protocol."},
                {"id": "C", "text": "Hardware Length (HLEN) is 6 bytes (MAC address length), and Protocol Length (PLEN) is 4 bytes (IPv4 address length)."},
                {"id": "D", "text": "Opcode (OPER): Set to `0x0001` for an ARP Request and `0x0002` for an ARP Reply."},
                {"id": "E", "text": "ARP packets include an 8-bit TTL field decremented by intermediate switches across VLANs."}
            ],
            "correctOptionIds": ["A", "B", "C", "D"],
            "explanation": "Statements A, B, C, and D are exact specifications of the 28-byte ARP header (HTYPE=1, PTYPE=0x0800, HLEN=6, PLEN=4, Opcode 1=Request, Opcode 2=Reply). E is false: ARP is a Layer 2 protocol encapsulated directly inside Ethernet frames (EtherType `0x0806`); it has no TTL field and does not route across Layer 3 boundaries.",
            "difficulty": "hard",
            "subtopic": "ARP Header Binary Format"
        },
        {
            "id": "l11-q03",
            "type": "multi_choice",
            "question": "Why is an ARP Request transmitted as a broadcast frame, while an ARP Reply is transmitted as a unicast frame?",
            "options": [
                {"id": "A", "text": "The requester does not know the target's MAC address; therefore, the Layer 2 Ethernet destination MAC must be set to the broadcast address `FF:FF:FF:FF:FF:FF`."},
                {"id": "B", "text": "Every host on the local broadcast domain receives the ARP Request and inspects the Target IP field."},
                {"id": "C", "text": "The responder already learned the requester's MAC address from the Sender Hardware Address (SHA) field in the incoming ARP Request."},
                {"id": "D", "text": "Because the responder knows the requester's exact MAC address, it sends the ARP Reply directly as a unicast frame to avoid unnecessary network flooding."},
                {"id": "E", "text": "Switches forward the ARP Request frame to all ports worldwide across the public Internet."}
            ],
            "correctOptionIds": ["A", "B", "C", "D"],
            "explanation": "Statements A, B, C, and D accurately explain the ARP exchange dynamics. The request must broadcast ($FF:FF:FF:FF:FF:FF$) because the target MAC is unknown (A & B). However, the request includes the sender's MAC, allowing the target to cache the requester and reply via efficient unicast (C & D). E is false: Broadcast frames are strictly bounded within the local Layer 2 broadcast domain.",
            "difficulty": "medium",
            "subtopic": "ARP Broadcast vs Unicast Mechanics"
        },
        {
            "id": "l11-q04",
            "type": "multi_choice",
            "question": "A Gratuitous ARP (GARP) is an ARP packet sent where the Sender IP and Target IP are identical. Which of the following are legitimate production use cases of Gratuitous ARP?",
            "options": [
                {"id": "A", "text": "IP Address Conflict Detection: Upon interface bring-up, a host sends a GARP probe; if another device responds, an IP conflict exists and the host flags an error."},
                {"id": "B", "text": "High Availability Failover (VRRP / CARP / Keepalived): When a primary router crashes, the standby router assumes the Virtual IP (VIP) and broadcasts a GARP to instantly update all client ARP caches with its MAC address."},
                {"id": "C", "text": "Virtual Machine Live Migration: When a VM moves between physical hypervisors, a GARP notifies the physical switch fabric to update its CAM (Content Addressable Memory) MAC learning tables."},
                {"id": "D", "text": "NIC Teaming / Bonding: When an active network interface fails, the backup NIC sends a GARP to associate the existing MAC/IP with the new physical switch port."},
                {"id": "E", "text": "To bypass the need for TLS certificates during HTTPS handshakes."}
            ],
            "correctOptionIds": ["A", "B", "C", "D"],
            "explanation": "Statements A, B, C, and D are foundational networking use cases for Gratuitous ARP. GARP detects IP duplicates (A), updates client ARP caches during router failover (B), refreshes switch CAM tables during VM live migration (C), and coordinates NIC bonding failover (D). E is completely unrelated.",
            "difficulty": "hard",
            "subtopic": "Gratuitous ARP Applications"
        },
        {
            "id": "l11-q05",
            "type": "multi_choice",
            "question": "Which of the following architectural vulnerabilities allow ARP Poisoning / ARP Spoofing attacks to succeed on a local network?",
            "options": [
                {"id": "A", "text": "ARP is stateless and entirely unauthenticated; hosts accept ARP Replies without verifying cryptographic signatures or verifying whether an ARP Request was ever sent."},
                {"id": "B", "text": "An attacker can transmit unsolicited ARP Replies claiming that the default gateway's IP address maps to the attacker's own MAC address."},
                {"id": "C", "text": "Once poisoned, victim hosts transmit all outbound Internet traffic to the attacker's MAC, enabling Man-in-the-Middle (MITM) eavesdropping and packet tampering."},
                {"id": "D", "text": "ARP poisoning allows an attacker to decrypt AES-256 encrypted TLS traffic without obtaining the private key."},
                {"id": "E", "text": "An attacker can poison the default gateway's ARP cache simultaneously to intercept bidirectional traffic flows."}
            ],
            "correctOptionIds": ["A", "B", "C", "E"],
            "explanation": "Statements A, B, C, and E are correct. ARP has no cryptographic authentication and caches unsolicited replies (A & B). Poisoning both victim and gateway positions the attacker as a full L2 Man-in-the-Middle (C & E). D is false: L2 ARP spoofing intercepts raw frames, but TLS payload remains encrypted unless the attacker also compromises CA certificates or executes SSL stripping.",
            "difficulty": "medium",
            "subtopic": "ARP Spoofing & MITM Attacks"
        },
        {
            "id": "l11-q06",
            "type": "multi_choice",
            "question": "How do enterprise switches mitigate ARP spoofing and rogue DHCP servers using DHCP Snooping and Dynamic ARP Inspection (DAI)?",
            "options": [
                {"id": "A", "text": "DHCP Snooping designates switch ports as either 'Trusted' (connected to legitimate DHCP servers/uplinks) or 'Untrusted' (access ports connected to regular end users)."},
                {"id": "B", "text": "The switch drops any incoming DHCP Offer or DHCP Ack packets arriving on Untrusted ports, preventing rogue DHCP servers from hijacking client gateways or DNS configurations."},
                {"id": "C", "text": "The switch listens to valid DHCP exchanges on untrusted ports and dynamically constructs a `DHCP Snooping Binding Database` mapping `(MAC, IP, VLAN, Port, Lease Time)`."},
                {"id": "D", "text": "Dynamic ARP Inspection (DAI) inspects all ARP packets arriving on untrusted ports, verifying them against the DHCP Snooping Binding Database; mismatched or spoofed ARPs are dropped."},
                {"id": "E", "text": "DHCP Snooping automatically blocks all IPv6 traffic by resetting the switch CPU."}
            ],
            "correctOptionIds": ["A", "B", "C", "D"],
            "explanation": "Statements A, B, C, and D describe the standard enterprise L2 security architecture. DHCP Snooping classifies ports as trusted/untrusted (A), blocks rogue DHCP responses (B), and builds the binding database (C). DAI leverages this database to validate and filter ARP packets at hardware line speed (D). E is false.",
            "difficulty": "hard",
            "subtopic": "DHCP Snooping & Dynamic ARP Inspection"
        },
        {
            "id": "l11-q07",
            "type": "multi_choice",
            "question": "In Network Address and Port Translation (NAPT / PAT), what exact modifications are performed by the NAT router when an internal host (`192.168.1.5:54321`) transmits a packet to an external server (`93.184.216.34:443`)?",
            "options": [
                {"id": "A", "text": "The router replaces the private Source IP (`192.168.1.5`) with the router's public WAN IP address (e.g., `203.0.113.10`)."},
                {"id": "B", "text": "The router allocates an available source port from its public pool (e.g., `10045`) and rewrites the Source Port field."},
                {"id": "C", "text": "The router records the 5-tuple translation `(192.168.1.5:54321 ⟷ 203.0.113.10:10045 ⟷ 93.184.216.34:443)` into its internal NAT state table."},
                {"id": "D", "text": "The router decrements the IPv4 TTL and recomputes both the IPv4 Header Checksum and the TCP Checksum (because the IP addresses and TCP ports in the pseudo-header changed)."},
                {"id": "E", "text": "The Destination IP address is rewritten to `0.0.0.0`."}
            ],
            "correctOptionIds": ["A", "B", "C", "D"],
            "explanation": "Statements A, B, C, and D are accurate steps in NAPT. Source IP is replaced by WAN IP (A). Source Port is mapped (B). State table stores mapping for reverse translation (C). TTL is decremented, and both IP and L4 checksums MUST be recalculated because IP and port values changed (D). E is absurd.",
            "difficulty": "hard",
            "subtopic": "NAPT / PAT State Mechanics"
        },
        {
            "id": "l11-q08",
            "type": "multi_choice",
            "question": "Which of the following are consequences and limitations of NAT Port Address Translation (PAT)?",
            "options": [
                {"id": "A", "text": "A single public IPv4 address has an ephemeral port range limit ($2^{16} = 65,535$ ports), theoretically capping concurrent outbound translations per public IP."},
                {"id": "B", "text": "In Carrier-Grade NAT (CGNAT / RFC 6598), ISPs place multiple households behind a shared public IPv4 pool using the `100.64.0.0/10` shared address space."},
                {"id": "C", "text": "Under heavy traffic, rapid connection churn can exhaust the NAT port pool, causing new outbound connections to fail with port allocation errors."},
                {"id": "D", "text": "NAT completely eliminates the need for firewalls because translation headers cannot be read by hackers."},
                {"id": "E", "text": "Port translation requires the NAT device to maintain state in RAM; if the router crashes and reboots, all active connections across the NAT are broken."}
            ],
            "correctOptionIds": ["A", "B", "C", "E"],
            "explanation": "Statements A, B, C, and E are correct. Port limits cap capacity per IP (A). CGNAT uses `100.64.0.0/10` to conserve public IPs (B). High churn causes port exhaustion (C). NAT is stateful, so reboots destroy active connections (E). D is false: NAT is not a substitute for a true stateful firewall.",
            "difficulty": "medium",
            "subtopic": "PAT Port Limitations & CGNAT"
        },
        {
            "id": "l11-q09",
            "type": "multi_choice",
            "question": "In the taxonomy of NAT behaviors (RFC 3489 / RFC 4787), which of the following statements regarding Cone NAT vs. Symmetric NAT are correct?",
            "options": [
                {"id": "A", "text": "In a Full Cone NAT (One-to-One NAT), once an internal address/port (`IP_i:Port_i`) is mapped to an external port (`IP_e:Port_e`), ANY external host can send packets to `IP_e:Port_e` and they will be delivered to the internal host."},
                {"id": "B", "text": "In an Address-Restricted Cone NAT, an external host can send packets to `IP_e:Port_e` ONLY if the internal host previously sent a packet to that external host's IP address."},
                {"id": "C", "text": "In a Port-Restricted Cone NAT, an external host can send packets ONLY if the internal host previously sent a packet to that external host's exact IP and port."},
                {"id": "D", "text": "In a Symmetric NAT, the router assigns a DIFFERENT public source port for every distinct destination IP/port combination that the internal host connects to."},
                {"id": "E", "text": "Direct peer-to-peer UDP hole punching succeeds consistently between two endpoints when both endpoints are located behind Symmetric NATs."}
            ],
            "correctOptionIds": ["A", "B", "C", "D"],
            "explanation": "Statements A, B, C, and D are correct definitions of the classical NAT types. Full Cone accepts from anyone (A). Address-Restricted checks remote IP (B). Port-Restricted checks remote IP and port (C). Symmetric NAT allocates a unique external port for every unique destination target (D). E is false: When both peers are behind Symmetric NATs, UDP hole punching fails because neither peer can predict the port allocated for the other; a TURN relay is mandatory.",
            "difficulty": "hard",
            "subtopic": "Cone NAT vs Symmetric NAT"
        },
        {
            "id": "l11-q10",
            "type": "multi_choice",
            "question": "Which of the following are true regarding STUN (Session Traversal Utilities for NAT - RFC 5389)?",
            "options": [
                {"id": "A", "text": "A STUN client transmits a Binding Request to an external STUN server on the public Internet."},
                {"id": "B", "text": "The STUN server inspects the source IP and source port of the incoming UDP packet and reflects them back in a `XOR-MAPPED-ADDRESS` attribute in the Binding Response."},
                {"id": "C", "text": "STUN allows an internal client to discover its own public reflexive IP address and external port allocation."},
                {"id": "D", "text": "STUN provides a universal solution that enables direct peer-to-peer media streaming even when both peers are behind Symmetric NATs."},
                {"id": "E", "text": "STUN packets are lightweight UDP datagrams containing a 20-byte fixed header with a Magic Cookie (`0x2112A442`)."}
            ],
            "correctOptionIds": ["A", "B", "C", "E"],
            "explanation": "Statements A, B, C, and E are accurate. STUN sends binding requests (A), reflects the public reflexive socket address via `XOR-MAPPED-ADDRESS` (B), discovering client public endpoints (C). STUN uses a 20-byte header with magic cookie `0x2112A442` (E). D is false: STUN cannot traverse Symmetric NAT combinations, which require TURN relays.",
            "difficulty": "hard",
            "subtopic": "STUN Protocol Architecture"
        },
        {
            "id": "l11-q11",
            "type": "multi_choice",
            "question": "When STUN-based hole punching fails, how does TURN (Traversal Using Relays around NAT - RFC 5766) ensure reliable multimedia communication (e.g., in WebRTC)?",
            "options": [
                {"id": "A", "text": "TURN provides an external relay server that allocates a public IP and port on behalf of the client."},
                {"id": "B", "text": "Both peers transmit their encrypted audio/video media packets directly to the TURN server, which forwards them to the remote peer."},
                {"id": "C", "text": "TURN guarantees connection success in 100% of network topologies, regardless of symmetric NATs or restrictive enterprise firewalls."},
                {"id": "D", "text": "TURN introduces server bandwidth costs and added packet latency because all media streams must traverse the relay instead of flowing peer-to-peer."},
                {"id": "E", "text": "TURN modifies the intermediate ISP router's BGP tables to eliminate the NAT gateway."}
            ],
            "correctOptionIds": ["A", "B", "C", "D"],
            "explanation": "Statements A, B, C, and D are correct. TURN acts as an always-working fallback relay (A), forwarding packets between clients (B). It guarantees connectivity in all NAT topologies (C), but incurs bandwidth costs and relay latency (D). E is false.",
            "difficulty": "medium",
            "subtopic": "TURN Relay Architecture"
        },
        {
            "id": "l11-q12",
            "type": "multi_choice",
            "question": "In WebRTC, how does the Interactive Connectivity Establishment (ICE - RFC 8445) framework orchestrate connection setup?",
            "options": [
                {"id": "A", "text": "ICE systematically gathers three types of candidates: Host candidates (local physical/virtual IPs), Server Reflexive candidates (STUN-discovered public IPs), and Relay candidates (TURN servers)."},
                {"id": "B", "text": "Peers exchange their gathered candidates via an out-of-band signaling channel (e.g., WebSockets using SDP - Session Description Protocol)."},
                {"id": "C", "text": "ICE pairs the candidates into priority-ranked candidate pairs and performs STUN connectivity checks in parallel."},
                {"id": "D", "text": "ICE always prefers direct peer-to-peer Host and Server Reflexive paths over costly TURN Relay paths whenever direct connectivity succeeds."},
                {"id": "E", "text": "ICE requires that both communicating endpoints share the exact same Wi-Fi SSID."}
            ],
            "correctOptionIds": ["A", "B", "C", "D"],
            "explanation": "Statements A, B, C, and D are correct. ICE gathers host, reflexive, and relay candidates (A), exchanges them via signaling (B), runs parallel STUN connectivity checks (C), and prioritizes direct P2P connections to avoid relay overhead (D). E is false: ICE is designed specifically for peers on completely different networks.",
            "difficulty": "hard",
            "subtopic": "ICE Framework & WebRTC"
        },
        {
            "id": "l11-q13",
            "type": "multi_choice",
            "question": "Which of the following are technically accurate regarding the Dynamic Host Configuration Protocol (DHCP - RFC 2131) DORA state machine?",
            "options": [
                {"id": "A", "text": "DHCP operates over UDP, with servers listening on port 67 and clients receiving on port 68."},
                {"id": "B", "text": "In the DHCP Discover message, the client sets Source IP to `0.0.0.0` and Destination IP to the limited broadcast address `255.255.255.255`."},
                {"id": "C", "text": "The client generates a random 32-bit Transaction ID (`xid`) in the Discover message, which the server echoes back in the Offer to allow the client to match responses."},
                {"id": "D", "text": "The DHCP Request message is broadcast on the local network so that other DHCP servers that made competing offers can retract their offered leases."},
                {"id": "E", "text": "The DHCP Ack message is sent over TCP port 443 to encrypt the network lease parameters."}
            ],
            "correctOptionIds": ["A", "B", "C", "D"],
            "explanation": "Statements A, B, C, and D are accurate. DHCP uses UDP 67/68 (A). Discover broadcasts from 0.0.0.0 to 255.255.255.255 (B). A 32-bit `xid` correlates transactions (C). Request is broadcast so competing DHCP servers release their reserved leases (D). E is false: DHCP Ack is sent over UDP, not TCP or HTTPS.",
            "difficulty": "medium",
            "subtopic": "DHCP DORA State Machine"
        },
        {
            "id": "l11-q14",
            "type": "multi_choice",
            "question": "Which of the following rules govern DHCP Lease Timers and lease renewal behavior?",
            "options": [
                {"id": "A", "text": "The total lease duration is defined by Lease Time ($T_3$, or Option 51)."},
                {"id": "B", "text": "At renewal timer $T_1 = 0.50 \\times \\text{Lease Time}$ (50%), the client attempts to renew its lease by sending a unicast DHCP Request directly to the original DHCP server."},
                {"id": "C", "text": "If the original server does not respond by rebinding timer $T_2 = 0.875 \\times \\text{Lease Time}$ (87.5%), the client broadcasts a DHCP Request to ANY available DHCP server on the network."},
                {"id": "D", "text": "If no DHCP Ack is received before $T_3 = 1.00 \\times \\text{Lease Time}$ (100%), the lease expires, the host immediately unbinds the IP address, and restarts the DORA process with a Discover."},
                {"id": "E", "text": "If the DHCP server reboots, all active client leases are immediately revoked within 50 milliseconds."}
            ],
            "correctOptionIds": ["A", "B", "C", "D"],
            "explanation": "Statements A, B, C, and D are standard RFC 2131 lease timer specifications. $T_1 = 50\\%$ unicast renewal (B). $T_2 = 87.5\\%$ broadcast rebinding (C). $T_3 = 100\\%$ expiration and lease release (D). E is false: Clients retain leased IPs until timer expiry regardless of whether the DHCP server reboots or goes offline temporarily.",
            "difficulty": "hard",
            "subtopic": "DHCP Lease Timers (T1, T2, T3)"
        },
        {
            "id": "l11-q15",
            "type": "multi_choice",
            "question": "Which of the following security threats are directly associated with DHCP deployments on unmanaged local area networks?",
            "options": [
                {"id": "A", "text": "DHCP Starvation Attack: An attacker floods the network with thousands of DHCP Discovers with forged MAC addresses, exhausting the DHCP server's entire IP address pool."},
                {"id": "B", "text": "Rogue DHCP Server Attack: An unauthorized DHCP server replies to client Discovers faster than the legitimate server, assigning a malicious default gateway or malicious DNS resolver IP to victims."},
                {"id": "C", "text": "DHCP Snooping on network switches mitigates starvation attacks by enforcing rate-limiting on DHCP packets on untrusted switch ports."},
                {"id": "D", "text": "Rogue DHCP servers can be completely neutralized by replacing all Cat6 cables with multi-mode fiber optic lines."},
                {"id": "E", "text": "A rogue DHCP server can assign its own IP address as the default gateway to perform transparent Man-in-the-Middle eavesdropping on all client web traffic."}
            ],
            "correctOptionIds": ["A", "B", "C", "E"],
            "explanation": "Statements A, B, C, and E are correct. Starvation exhausts pools (A). Rogue DHCP servers hijack gateways and DNS (B & E). Switch port rate limiting and snooping mitigate starvation (C). D is false: Cable medium has zero effect on higher-layer broadcast protocol security.",
            "difficulty": "medium",
            "subtopic": "DHCP Attacks & Defenses"
        },
        {
            "id": "l11-q16",
            "type": "multi_choice",
            "question": "How does a DHCP Relay Agent (RFC 3046 / Option 82) enable centralized DHCP servers to serve clients across multiple routed subnets?",
            "options": [
                {"id": "A", "text": "Because routers do not forward limited broadcast packets (`255.255.255.255`), a client's DHCP Discover cannot cross a router boundary on its own."},
                {"id": "B", "text": "A router interface configured as a DHCP Relay intercepts incoming client broadcast Discovers and re-encapsulates them as unicast UDP packets sent to the centralized DHCP server."},
                {"id": "C", "text": "The relay agent inserts the IP address of its receiving interface into the `giaddr` (Gateway IP Address) field of the DHCP message."},
                {"id": "D", "text": "The centralized DHCP server inspects `giaddr` to determine which subnet IP pool to allocate the client's lease from."},
                {"id": "E", "text": "The DHCP Relay Agent decrypts the client's Wi-Fi password and stores it in the router's NVRAM."}
            ],
            "correctOptionIds": ["A", "B", "C", "D"],
            "explanation": "Statements A, B, C, and D accurately capture the DHCP Relay mechanism. Routers drop L2/L3 broadcasts (A). Relay converts broadcast to unicast toward central server (B). The `giaddr` field tells the server the client's origin subnet (C & D). E is absurd.",
            "difficulty": "hard",
            "subtopic": "DHCP Relay Agent & Option 82"
        },
        {
            "id": "l11-q17",
            "type": "multi_choice",
            "question": "A typical consumer home 'Wi-Fi Router' is actually a multi-functional embedded appliance combining several distinct networking components. Which of the following components are integrated inside?",
            "options": [
                {"id": "A", "text": "A Layer 2 Ethernet Switch providing local LAN ports with hardware CAM MAC learning."},
                {"id": "B", "text": "A Wireless Access Point (AP) bridging 802.11 wireless frames onto the wired Layer 2 network."},
                {"id": "C", "text": "A Layer 3 IP Router forwarding packets between the local LAN subnet (`192.168.1.0/24`) and the ISP WAN network."},
                {"id": "D", "text": "A stateful NAPT / PAT engine and firewall translating private RFC 1918 addresses to a single public IP."},
                {"id": "E", "text": "Local network services, including an embedded DHCP server and a caching DNS forwarder/proxy (e.g., `dnsmasq`)."}
            ],
            "correctOptionIds": ["A", "B", "C", "D", "E"],
            "explanation": "ALL FIVE statements (A, B, C, D, and E) are correct! The home 'router' combines an L2 switch (A), 802.11 AP (B), L3 router (C), NAPT/firewall (D), and embedded DHCP/DNS daemons like dnsmasq (E) into a single unified chassis.",
            "difficulty": "medium",
            "subtopic": "Home Gateway Architecture"
        },
        {
            "id": "l11-q18",
            "type": "multi_choice",
            "question": "Which of the following transition mechanisms enable IPv6-only clients to communicate with legacy IPv4-only Internet services?",
            "options": [
                {"id": "A", "text": "DNS64: When an IPv6 client queries a domain that only possesses an IPv4 A record, the DNS64 resolver synthesizes an artificial AAAA record by prepending a Well-Known Prefix (e.g., `64:ff9b::/96`)."},
                {"id": "B", "text": "NAT64: The intermediate gateway intercepts the IPv6 packet addressed to the synthetic prefix, extracts the embedded IPv4 address, and translates it to an IPv4 packet using a stateful NAT pool."},
                {"id": "C", "text": "Dual Stack: Configures network interfaces and routers with both an IPv4 and an IPv6 address simultaneously, routing each protocol natively."},
                {"id": "D", "text": "Happy Eyeballs (RFC 8305): Browsers query both A and AAAA records in parallel and attempt connections to both, preferring IPv6 but falling back to IPv4 with minimal delay if IPv6 connectivity is impaired."},
                {"id": "E", "text": "NAT64 works by physically stripping the first 96 bits of fiber optic glass in the uplink cable."}
            ],
            "correctOptionIds": ["A", "B", "C", "D"],
            "explanation": "Statements A, B, C, and D are correct. DNS64 synthesizes AAAA records (A), NAT64 translates between IPv6 and IPv4 headers (B), Dual Stack runs both protocols side-by-side (C), and Happy Eyeballs minimizes user-visible latency during dual-stack transitions (D). E is humorous nonsense.",
            "difficulty": "hard",
            "subtopic": "IPv6 Transition: NAT64 & DNS64"
        },
        {
            "id": "l11-q19",
            "type": "multi_choice",
            "question": "In container platforms like Docker and Kubernetes, how does container networking utilize Linux network namespaces and NAT?",
            "options": [
                {"id": "A", "text": "Each container is assigned its own isolated Linux Network Namespace with its own independent network interfaces, routing table, and iptables rules."},
                {"id": "B", "text": "A Virtual Ethernet pair (`veth`) connects the container namespace to the host namespace, acting like a virtual patch cable with one end inside the container and the other end plugged into the `docker0` virtual bridge."},
                {"id": "C", "text": "Outbound traffic from containers to the external network undergoes source NAT via Linux iptables (`MASQUERADE` rule), rewriting the container's private IP to the host's physical IP."},
                {"id": "D", "text": "Inbound port publishing (`docker run -p 8080:80`) creates a Destination NAT (DNAT) rule in iptables, redirecting incoming packets on host port 8080 to the container's internal IP on port 80."},
                {"id": "E", "text": "Docker containers require an individual physical PCIe network card plugged into the motherboard for each running container."}
            ],
            "correctOptionIds": ["A", "B", "C", "D"],
            "explanation": "Statements A, B, C, and D accurately represent Linux container networking. Network namespaces isolate stacks (A). `veth` pairs bridge namespaces into `docker0` (B). Outbound traffic uses `iptables -j MASQUERADE` SNAT (C). Port forwarding uses `PREROUTING -j DNAT` (D). E is false; everything is virtualized in software.",
            "difficulty": "hard",
            "subtopic": "Linux Namespaces & Container NAT"
        },
        {
            "id": "l11-q20",
            "type": "multi_choice",
            "question": "Which of the following statements regarding local network plumbing and Layer 2/Layer 3 boundaries are true?",
            "options": [
                {"id": "A", "text": "Ethernet switches forward frames using MAC addresses within the same broadcast domain; routers forward packets using IP addresses across different broadcast domains."},
                {"id": "B", "text": "When a packet crosses an intermediate router hop, the source and destination IP addresses remain intact (unless NAT is applied), but the source and destination MAC addresses are replaced entirely."},
                {"id": "C", "text": "A broadcast frame with destination MAC `FF:FF:FF:FF:FF:FF` is flooded by Layer 2 switches out of every port in the same VLAN except the ingress port."},
                {"id": "D", "text": "A standard IP router will never forward an Ethernet frame with destination MAC `FF:FF:FF:FF:FF:FF` across to another subnet (broadcast boundary)."},
                {"id": "E", "text": "If a host wishes to communicate with a remote IP address outside its subnet, its ARP request asks for the MAC address of its Default Gateway, NOT the remote destination host."}
            ],
            "correctOptionIds": ["A", "B", "C", "D", "E"],
            "explanation": "ALL FIVE statements (A, B, C, D, and E) are core networking truths! Switches switch by MAC, routers route by IP (A). MACs change hop-by-hop while IPs remain constant (B). Broadcasts flood within the VLAN (C) and are dropped at router boundaries (D). For remote traffic, hosts ARP for their default gateway (E).",
            "difficulty": "medium",
            "subtopic": "Layer 2 & Layer 3 Integration"
        }
    ]
}
