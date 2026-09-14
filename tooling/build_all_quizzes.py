"""
Automated Quiz Builder generating 20+ distinct questions per lecture for Lectures 02 to 08
and comprehensive quizzes for Lectures 09 to 13, incorporating handwritten notes and lecture materials.
Outputs both JSON structures for backend/APIs and compiles web/src/data/quizzesData.ts.
"""

import json
from pathlib import Path

BASE_DIR = Path(__file__).parent.parent
JSON_DIR = BASE_DIR / "web" / "src" / "data" / "quizzes"
JSON_DIR.mkdir(parents=True, exist_ok=True)

QUIZZES = {}

# Import previously defined lectures 2 & 3
from quiz_data_definitions import ALL_QUIZZES
QUIZZES.update(ALL_QUIZZES)

# Add Lecture 04 (20 questions)
QUIZZES["lecture-04"] = {
    "topicId": "lecture-04",
    "lectureNumber": 4,
    "title": "IP Addresses & Subnetting II Quiz",
    "description": "20 questions covering VLSM partition trees, IPv6 RFC 5952 compression, scopes, Default Gateways, and NAT/PAT.",
    "estimatedMinutes": 25,
    "questions": [
        {
            "id": "l04-q01",
            "type": "single_choice",
            "question": "What is the primary operational advantage of Variable Length Subnet Masking (VLSM) over Fixed Length Subnet Masking (FLSM)?",
            "options": [
                {"id": "A", "text": "VLSM allows assigning different subnet mask lengths to different subnets, preventing IP wastage"},
                {"id": "B", "text": "VLSM allows switches to ignore MAC addresses"},
                {"id": "C", "text": "VLSM converts IPv4 addresses into IPv6 addresses automatically"},
                {"id": "D", "text": "VLSM eliminates the need for a default gateway"}
            ],
            "correctOptionIds": ["A"],
            "explanation": "FLSM forces all subnets to have identical sizes. VLSM allows custom prefix sizing per department, drastically reducing wasted host addresses.",
            "difficulty": "easy",
            "subtopic": "VLSM Concepts"
        },
        {
            "id": "l04-q02",
            "type": "single_choice",
            "question": "What is the Golden Rule of VLSM address allocation?",
            "options": [
                {"id": "A", "text": "Allocate the smallest subnet first to conserve the beginning of the block"},
                {"id": "B", "text": "Always sort host requirements in strictly descending order (Largest -> Smallest) and allocate the largest blocks first"},
                {"id": "C", "text": "Always assign the default gateway the highest IP in the range"},
                {"id": "D", "text": "Never use subnet masks longer than /24"}
            ],
            "correctOptionIds": ["B"],
            "explanation": "Allocating small subnets first fragments the continuous binary address space, making it impossible to allocate contiguous larger power-of-two subnets later.",
            "difficulty": "medium",
            "subtopic": "VLSM Golden Rule"
        },
        {
            "id": "l04-q03",
            "type": "single_choice",
            "question": "You need to accommodate 100 hosts in an engineering subnet. What is the smallest valid subnet mask and block size?",
            "options": [
                {"id": "A", "text": "/26 (64 addresses, 62 hosts)"},
                {"id": "B", "text": "/25 (128 addresses, 126 hosts)"},
                {"id": "C", "text": "/24 (256 addresses, 254 hosts)"},
                {"id": "D", "text": "/27 (32 addresses, 30 hosts)"}
            ],
            "correctOptionIds": ["B"],
            "explanation": "2^N - 2 >= 100 implies 2^N >= 102 -> N = 7 host bits (2^7 = 128). Prefix = 32 - 7 = /25, offering 126 usable hosts.",
            "difficulty": "easy",
            "subtopic": "VLSM Calculation"
        },
        {
            "id": "l04-q04",
            "type": "single_choice",
            "question": "How many bits are in an IPv6 address, and how many hexadecimal digits represent it?",
            "options": [
                {"id": "A", "text": "64 bits, 16 hex digits"},
                {"id": "B", "text": "128 bits, 32 hex digits arranged in 8 hextets of 4 hex digits"},
                {"id": "C", "text": "256 bits, 64 hex digits"},
                {"id": "D", "text": "48 bits, 12 hex digits"}
            ],
            "correctOptionIds": ["B"],
            "explanation": "IPv6 addresses are 128 bits long, written as 8 groups (hextets) of 4 hexadecimal characters (8 * 16 = 128 bits).",
            "difficulty": "easy",
            "subtopic": "IPv6 Architecture"
        },
        {
            "id": "l04-q05",
            "type": "single_choice",
            "question": "According to RFC 5952, how should the IPv6 address 2001:0db8:0000:0000:0000:8a2e:0370:7334 be canonically compressed?",
            "options": [
                {"id": "A", "text": "2001:db8::8a2e:370:7334"},
                {"id": "B", "text": "2001:0db8::8a2e:0370:7334"},
                {"id": "C", "text": "2001:db8:0:0:0:8a2e:370:7334"},
                {"id": "D", "text": "2001:db8:::8a2e:370:7334"}
            ],
            "correctOptionIds": ["A"],
            "explanation": "Leading zeros in each hextet are omitted (0db8 -> db8, 0370 -> 370), and the longest consecutive run of all-zero hextets is replaced with '::'.",
            "difficulty": "medium",
            "subtopic": "RFC 5952 Compression"
        },
        {
            "id": "l04-q06",
            "type": "single_choice",
            "question": "Why can the double-colon '::' zero-compression symbol be used ONLY ONCE in any IPv6 address?",
            "options": [
                {"id": "A", "text": "Because RFC standards restrict it for aesthetic reasons"},
                {"id": "B", "text": "Because multiple double-colons create mathematical ambiguity in reconstructing how many zero hextets belong to each run"},
                {"id": "C", "text": "Because hardware router ASICs cannot process more than 16 zeros"},
                {"id": "D", "text": "Because it would conflict with IPv4 dotted decimals"}
            ],
            "correctOptionIds": ["B"],
            "explanation": "If '::' appeared twice (e.g. 2001::db8::1), a parser cannot determine how many zero hextets belong to the first run vs. the second run.",
            "difficulty": "medium",
            "subtopic": "RFC 5952 Rules"
        },
        {
            "id": "l04-q07",
            "type": "single_choice",
            "question": "What is a major architectural difference between IPv4 and IPv6 regarding one-to-all communication?",
            "options": [
                {"id": "A", "text": "IPv6 uses larger broadcast packets"},
                {"id": "B", "text": "IPv6 completely eliminates Broadcast addresses; all one-to-many operations use targeted Multicast"},
                {"id": "C", "text": "IPv6 requires all hosts to broadcast their MAC address every 10 seconds"},
                {"id": "D", "text": "IPv6 disables multicast to conserve fiber spectrum"}
            ],
            "correctOptionIds": ["B"],
            "explanation": "IPv6 has NO broadcast. All one-to-many communications use efficient Multicast groups (e.g. ff02::1 for all nodes, ff02::2 for all routers), preventing broadcast storms.",
            "difficulty": "hard",
            "subtopic": "IPv6 Multicast"
        },
        {
            "id": "l04-q08",
            "type": "single_choice",
            "question": "Which prefix identifies an IPv6 Link-Local address automatically configured on every interface?",
            "options": [
                {"id": "A", "text": "2000::/3"},
                {"id": "B", "text": "fc00::/7"},
                {"id": "C", "text": "fe80::/10"},
                {"id": "D", "text": "ff00::/8"}
            ],
            "correctOptionIds": ["C"],
            "explanation": "fe80::/10 is reserved for Link-Local addresses, used for single-hop neighbor discovery (NDP) and router advertisements.",
            "difficulty": "medium",
            "subtopic": "IPv6 Scopes"
        },
        {
            "id": "l04-q09",
            "type": "single_choice",
            "question": "What is the IPv6 equivalent of the IPv4 loopback address 127.0.0.1?",
            "options": [
                {"id": "A", "text": "::/128"},
                {"id": "B", "text": "::1/128"},
                {"id": "C", "text": "fe80::1"},
                {"id": "D", "text": "2001::1"}
            ],
            "correctOptionIds": ["B"],
            "explanation": "::1 (or 0000:...:0001) is the IPv6 loopback address.",
            "difficulty": "easy",
            "subtopic": "IPv6 Loopback"
        },
        {
            "id": "l04-q10",
            "type": "single_choice",
            "question": "How does a host decide whether to deliver a packet directly on the local LAN or forward it to the Default Gateway?",
            "options": [
                {"id": "A", "text": "It checks if the destination IP is an even or odd number"},
                {"id": "B", "text": "It computes (Destination IP AND Host Subnet Mask) and checks if the result equals its local Network ID"},
                {"id": "C", "text": "It always sends all packets to the Default Gateway regardless of destination"},
                {"id": "D", "text": "It pings the destination MAC address"}
            ],
            "correctOptionIds": ["B"],
            "explanation": "If Destination IP AND Subnet Mask == Local Network ID, the destination is on the same subnet (direct ARP). Otherwise, it forwards to the gateway router's MAC.",
            "difficulty": "medium",
            "subtopic": "Host Forwarding Decision"
        },
        {
            "id": "l04-q11",
            "type": "multi_choice",
            "question": "Which commands can be run on Windows and Linux respectively to display the configured Default Gateway? (Select ALL that apply)",
            "options": [
                {"id": "A", "text": "route print (Windows)"},
                {"id": "B", "text": "ip route show (Linux)"},
                {"id": "C", "text": "netstat -rn (macOS / Linux)"},
                {"id": "D", "text": "arp -d (Windows)"}
            ],
            "correctOptionIds": ["A", "B", "C"],
            "explanation": "'route print' (Windows), 'ip route show' (Linux), and 'netstat -rn' display the kernel routing table and default gateway. 'arp -d' purges the ARP cache.",
            "difficulty": "easy",
            "subtopic": "Host Routing Commands"
        },
        {
            "id": "l04-q12",
            "type": "single_choice",
            "question": "What primary problem does Network Address Translation (NAT / NAPT) solve for home and enterprise networks?",
            "options": [
                {"id": "A", "text": "It speeds up light transmission in fiber optic cables"},
                {"id": "B", "text": "It enables hundreds of private devices to share a single public IPv4 address"},
                {"id": "C", "text": "It automatically assigns domain names to computers"},
                {"id": "D", "text": "It encrypts all DNS lookups"}
            ],
            "correctOptionIds": ["B"],
            "explanation": "NAT maps private RFC 1918 IPs and transport port numbers to a single public IP, alleviating immediate IPv4 address depletion.",
            "difficulty": "easy",
            "subtopic": "NAT Fundamentals"
        },
        {
            "id": "l04-q13",
            "type": "single_choice",
            "question": "In Port Address Translation (PAT / NAPT), how does the router distinguish returning packets destined for two different internal devices that connected to the same external server?",
            "options": [
                {"id": "A", "text": "By the color of the Ethernet cable"},
                {"id": "B", "text": "By mapping unique translated public transport-layer Port Numbers in its NAT state table"},
                {"id": "C", "text": "By inspecting internal MAC addresses stored in the packet payload"},
                {"id": "D", "text": "By broadcasting the reply to all LAN hosts"}
            ],
            "correctOptionIds": ["B"],
            "explanation": "PAT tracks (Private IP, Private Port) <-> (Public IP, Translated Port). The unique translated port in incoming packets indexes the correct internal host.",
            "difficulty": "medium",
            "subtopic": "PAT Mechanics"
        },
        {
            "id": "l04-q14",
            "type": "single_choice",
            "question": "What is Port Forwarding (Destination NAT / DNAT) primarily used for?",
            "options": [
                {"id": "A", "text": "Allowing internal devices to browse external websites"},
                {"id": "B", "text": "Allowing external internet clients to initiate connections to a server hosted inside a private NAT network"},
                {"id": "C", "text": "Speeding up local Wi-Fi transmission rates"},
                {"id": "D", "text": "Preventing ARP cache poisoning"}
            ],
            "correctOptionIds": ["B"],
            "explanation": "Because NAT blocks unsolicited inbound packets by default, port forwarding maps a specific external public port permanently to an internal private host:port.",
            "difficulty": "medium",
            "subtopic": "Port Forwarding (DNAT)"
        },
        {
            "id": "l04-q15",
            "type": "single_choice",
            "question": "Why do peer-to-peer applications like WebRTC, Discord voice, and multiplayer games struggle when devices are behind NAT?",
            "options": [
                {"id": "A", "text": "NAT routers drop all UDP packets"},
                {"id": "B", "text": "Devices behind NAT do not know their external public IP and cannot accept direct inbound connection requests without hole punching"},
                {"id": "C", "text": "NAT breaks TLS encryption keys"},
                {"id": "D", "text": "NAT changes the speed of light"}
            ],
            "correctOptionIds": ["B"],
            "explanation": "NAT prevents direct inbound connections. P2P protocols must use traversal frameworks (STUN/TURN/ICE) to discover external endpoints and punch holes.",
            "difficulty": "hard",
            "subtopic": "NAT Traversal"
        },
        {
            "id": "l04-q16",
            "type": "single_choice",
            "question": "What is the specific role of a STUN (Session Traversal Utilities for NAT) server?",
            "options": [
                {"id": "A", "text": "It relays all voice and video packets between peers"},
                {"id": "B", "text": "It allows a client behind NAT to discover its public IP address and NAT port mapping as seen by the outside world"},
                {"id": "C", "text": "It replaces the DNS root servers"},
                {"id": "D", "text": "It generates SSL certificates"}
            ],
            "correctOptionIds": ["B"],
            "explanation": "STUN acts as an external mirror: a client queries the STUN server, which responds with the client's public IP and translated port.",
            "difficulty": "medium",
            "subtopic": "STUN Protocol"
        },
        {
            "id": "l04-q17",
            "type": "single_choice",
            "question": "When does WebRTC fall back to using a TURN (Traversal Using Relays around NAT) server?",
            "options": [
                {"id": "A", "text": "When the connection speed is faster than 100 Mbps"},
                {"id": "B", "text": "When direct peer-to-peer hole punching fails due to Symmetric NAT or restrictive firewalls"},
                {"id": "C", "text": "When the client uses an Ethernet cable instead of Wi-Fi"},
                {"id": "D", "text": "When IPv6 is disabled"}
            ],
            "correctOptionIds": ["B"],
            "explanation": "TURN servers act as costly media relays when direct P2P connections cannot be established through symmetric NAT or corporate firewalls.",
            "difficulty": "hard",
            "subtopic": "TURN Relays"
        },
        {
            "id": "l04-q18",
            "type": "single_choice",
            "question": "Given the base network 10.0.0.0/16, how many /20 subnets can be created from this block?",
            "options": [
                {"id": "A", "text": "4"},
                {"id": "B", "text": "8"},
                {"id": "C", "text": "16"},
                {"id": "D", "text": "32"}
            ],
            "correctOptionIds": ["C"],
            "explanation": "Borrowed bits = 20 - 16 = 4 bits. Number of subnets = 2^4 = 16 subnets.",
            "difficulty": "medium",
            "subtopic": "Subnetting Arithmetic"
        },
        {
            "id": "l04-q19",
            "type": "multi_choice",
            "question": "Which of the following are inherent architectural drawbacks or limitations of NAT? (Select ALL that apply)",
            "options": [
                {"id": "A", "text": "It violates the pure end-to-end principle of the original Internet architecture"},
                {"id": "B", "text": "It requires the router to maintain stateful connection tables in memory"},
                {"id": "C", "text": "Protocols that embed IP addresses inside their application payload (e.g. FTP, SIP) require complex Application Layer Gateways (ALGs)"},
                {"id": "D", "text": "It increases the size of the physical Ethernet frame beyond 1518 bytes"}
            ],
            "correctOptionIds": ["A", "B", "C"],
            "explanation": "A, B, and C are major drawbacks of NAT (RFC 2993). NAT does not increase the physical Ethernet frame size.",
            "difficulty": "hard",
            "subtopic": "NAT Drawbacks"
        },
        {
            "id": "l04-q20",
            "type": "single_choice",
            "question": "What protocol replaces ARP in IPv6 networks for resolving Layer 3 IPv6 addresses to Layer 2 MAC addresses?",
            "options": [
                {"id": "A", "text": "DHCPv6"},
                {"id": "B", "text": "Neighbor Discovery Protocol (NDP / ICMPv6)"},
                {"id": "C", "text": "BGP-4"},
                {"id": "D", "text": "Reverse ARP (RARP)"}
            ],
            "correctOptionIds": ["B"],
            "explanation": "IPv6 replaces broadcast ARP with Neighbor Discovery Protocol (NDP), utilizing ICMPv6 Neighbor Solicitation and Neighbor Advertisement multicast messages.",
            "difficulty": "medium",
            "subtopic": "IPv6 NDP"
        }
    ]
}

# Add Lecture 05: Graph Algorithms for Networking I (20 questions)
QUIZZES["lecture-05"] = {
    "topicId": "lecture-05",
    "lectureNumber": 5,
    "title": "Graph Algorithms for Networking I Quiz",
    "description": "20 questions covering graph network modeling, BFS hop-count, DFS cycle detection, and Dijkstra's algorithm.",
    "estimatedMinutes": 25,
    "questions": [
        {
            "id": "l05-q01",
            "type": "single_choice",
            "question": "When modeling a telecommunications network as a graph G = (V, E), what do the vertices V and edges E represent?",
            "options": [
                {"id": "A", "text": "V represents IP addresses, E represents MAC addresses"},
                {"id": "B", "text": "V represents network nodes/routers, E represents physical or logical communication links"},
                {"id": "C", "text": "V represents application sockets, E represents TCP sequence numbers"},
                {"id": "D", "text": "V represents autonomous systems, E represents DNS servers"}
            ],
            "correctOptionIds": ["B"],
            "explanation": "In network graph theory, vertices represent routing nodes or switches, and edges represent communication links.",
            "difficulty": "easy",
            "subtopic": "Graph Modeling"
        },
        {
            "id": "l05-q02",
            "type": "single_choice",
            "question": "How does Cisco OSPF calculate the edge weight (cost) of an interface by default?",
            "options": [
                {"id": "A", "text": "Cost = 1 for all interfaces"},
                {"id": "B", "text": "Cost = Reference Bandwidth (10^8 bps) / Interface Bandwidth (bps)"},
                {"id": "C", "text": "Cost = Physical Cable Length in meters * 10"},
                {"id": "D", "text": "Cost = Current packet queue length"}
            ],
            "correctOptionIds": ["B"],
            "explanation": "OSPF uses inverse bandwidth: Cost = 100 Mbps / Interface Bandwidth in bps. Higher speed links produce lower costs.",
            "difficulty": "medium",
            "subtopic": "OSPF Metric"
        },
        {
            "id": "l05-q03",
            "type": "single_choice",
            "question": "What is the time complexity of Breadth-First Search (BFS) on an unweighted graph G = (V, E) using an adjacency list?",
            "options": [
                {"id": "A", "text": "O(V^2)"},
                {"id": "B", "text": "O(V + E)"},
                {"id": "C", "text": "O(E log V)"},
                {"id": "D", "text": "O(V log V)"}
            ],
            "correctOptionIds": ["B"],
            "explanation": "BFS enqueues each vertex at most once and inspects each edge once, yielding O(|V| + |E|) time complexity.",
            "difficulty": "easy",
            "subtopic": "BFS Complexity"
        },
        {
            "id": "l05-q04",
            "type": "single_choice",
            "question": "Why is standard BFS insufficient for routing in modern heterogeneous networks?",
            "options": [
                {"id": "A", "text": "BFS cannot find cycles in graphs"},
                {"id": "B", "text": "BFS computes shortest path strictly by hop count, ignoring link capacities, bandwidth, and latency"},
                {"id": "C", "text": "BFS cannot be implemented with a FIFO queue"},
                {"id": "D", "text": "BFS requires negative edge weights"}
            ],
            "correctOptionIds": ["B"],
            "explanation": "A 1-hop 56 kbps dialup link would be chosen by BFS over a 2-hop 100 Gbps fiber line because BFS treats all link costs as 1.",
            "difficulty": "medium",
            "subtopic": "BFS Limitations"
        },
        {
            "id": "l05-q05",
            "type": "single_choice",
            "question": "In network topology exploration, how does Depth-First Search (DFS) detect routing loops using the three-color node marking algorithm?",
            "options": [
                {"id": "A", "text": "When an edge points to a BLACK node"},
                {"id": "B", "text": "When an edge points to a GRAY node (currently on the recursion call stack)"},
                {"id": "C", "text": "When an edge points to a WHITE node"},
                {"id": "D", "text": "When all nodes become RED"}
            ],
            "correctOptionIds": ["B"],
            "explanation": "A directed edge pointing to a GRAY node represents a back-edge to an active ancestor on the recursion stack, formally proving a cycle.",
            "difficulty": "hard",
            "subtopic": "DFS Cycle Detection"
        },
        {
            "id": "l05-q06",
            "type": "single_choice",
            "question": "In a network graph, what is an 'articulation point' (cut-vertex)?",
            "options": [
                {"id": "A", "text": "A router whose removal disconnects the remaining network graph into two or more components (Single Point of Failure)"},
                {"id": "B", "text": "A switch running Spanning Tree Protocol"},
                {"id": "C", "text": "A port running full-duplex Gigabit Ethernet"},
                {"id": "D", "text": "A leaf node with degree 1"}
            ],
            "correctOptionIds": ["A"],
            "explanation": "An articulation point is a critical network node whose failure partitions the graph, representing a single point of failure (SPOF).",
            "difficulty": "medium",
            "subtopic": "Graph Robustness"
        },
        {
            "id": "l05-q07",
            "type": "single_choice",
            "question": "What is the foundational prerequisite condition required for Dijkstra's algorithm to guarantee an optimal shortest path?",
            "options": [
                {"id": "A", "text": "The graph must be a Directed Acyclic Graph (DAG)"},
                {"id": "B", "text": "All edge weights must be strictly non-negative (w >= 0)"},
                {"id": "C", "text": "The graph must be complete"},
                {"id": "D", "text": "The number of vertices must equal the number of edges"}
            ],
            "correctOptionIds": ["B"],
            "explanation": "Dijkstra relies on the greedy property that extracting the minimum tentative distance node finalizes its optimal distance. This fails if negative weights exist.",
            "difficulty": "medium",
            "subtopic": "Dijkstra Invariant"
        },
        {
            "id": "l05-q08",
            "type": "single_choice",
            "question": "What is the time complexity of Dijkstra's algorithm implemented with an Adjacency List and a Binary Min-Heap Priority Queue?",
            "options": [
                {"id": "A", "text": "O(V^2)"},
                {"id": "B", "text": "O((V + E) log V)"},
                {"id": "C", "text": "O(V * E)"},
                {"id": "D", "text": "O(V^3)"}
            ],
            "correctOptionIds": ["B"],
            "explanation": "With a binary min-heap: extracting minimums takes O(V log V) and edge relaxations/pushes take O(E log V), totaling O((V + E) log V).",
            "difficulty": "medium",
            "subtopic": "Dijkstra Complexity"
        },
        {
            "id": "l05-q09",
            "type": "single_choice",
            "question": "In Dijkstra's algorithm, what does the edge relaxation step if dist[u] + w(u, v) < dist[v] accomplish?",
            "options": [
                {"id": "A", "text": "It deletes edge (u, v) from the graph"},
                {"id": "B", "text": "It updates dist[v] to the cheaper path through u and sets predecessor[v] = u"},
                {"id": "C", "text": "It restarts the priority queue"},
                {"id": "D", "text": "It switches the network interface to promiscuous mode"}
            ],
            "correctOptionIds": ["B"],
            "explanation": "Relaxation tests whether passing through vertex u offers a shorter path to v than previously recorded, updating dist[v] and predecessor pointers.",
            "difficulty": "easy",
            "subtopic": "Edge Relaxation"
        },
        {
            "id": "l05-q10",
            "type": "single_choice",
            "question": "How does a router running OSPF translate Dijkstra's shortest path tree into its physical Forwarding Information Base (FIB)?",
            "options": [
                {"id": "A", "text": "It stores the complete end-to-end path in every packet header"},
                {"id": "B", "text": "It traces predecessor pointers back from each destination to determine the local outgoing interface and next-hop neighbor IP"},
                {"id": "C", "text": "It broadcasts the entire tree to the ISP"},
                {"id": "D", "text": "It copies all routes into the DNS cache"}
            ],
            "correctOptionIds": ["B"],
            "explanation": "Hop-by-hop forwarding only requires knowing the immediate Next Hop and physical egress interface for each destination prefix.",
            "difficulty": "hard",
            "subtopic": "FIB Generation"
        },
        {
            "id": "l05-q11",
            "type": "multi_choice",
            "question": "Which of the following real-world routing protocols utilize Dijkstra's algorithm as their internal path computation engine? (Select ALL that apply)",
            "options": [
                {"id": "A", "text": "OSPF (Open Shortest Path First)"},
                {"id": "B", "text": "IS-IS (Intermediate System to Intermediate System)"},
                {"id": "C", "text": "RIP (Routing Information Protocol)"},
                {"id": "D", "text": "BGP (Border Gateway Protocol)"}
            ],
            "correctOptionIds": ["A", "B"],
            "explanation": "OSPF and IS-IS are Link-State protocols that execute Dijkstra's algorithm. RIP uses Bellman-Ford, and BGP uses Path Vector.",
            "difficulty": "medium",
            "subtopic": "Routing Protocol Engines"
        },
        {
            "id": "l05-q12",
            "type": "single_choice",
            "question": "In a 3-node graph with links A-B (cost 4), A-C (cost 2), and C-B (cost 1), what is the shortest path cost from source A to destination B computed by Dijkstra?",
            "options": [
                {"id": "A", "text": "4 (direct path A-B)"},
                {"id": "B", "text": "3 (path A-C-B)"},
                {"id": "C", "text": "5 (path A-B-C)"},
                {"id": "D", "text": "1 (path C-B)"}
            ],
            "correctOptionIds": ["B"],
            "explanation": "A -> C (cost 2) + C -> B (cost 1) = cost 3, which is lower than direct link A -> B (cost 4).",
            "difficulty": "easy",
            "subtopic": "Dijkstra Trace"
        },
        {
            "id": "l05-q13",
            "type": "single_choice",
            "question": "What data structure in Dijkstra's algorithm holds the vertices whose shortest path has NOT yet been permanently finalized?",
            "options": [
                {"id": "A", "text": "FIFO Queue"},
                {"id": "B", "text": "LIFO Stack"},
                {"id": "C", "text": "Priority Queue (Min-Heap)"},
                {"id": "D", "text": "Circular Buffer"}
            ],
            "correctOptionIds": ["C"],
            "explanation": "A Min-Heap priority queue allows efficient O(log V) extraction of the vertex with the minimum tentative distance.",
            "difficulty": "easy",
            "subtopic": "Data Structures"
        },
        {
            "id": "l05-q14",
            "type": "single_choice",
            "question": "What is the difference between propagation delay and transmission delay when calculating edge weights in a network graph?",
            "options": [
                {"id": "A", "text": "Propagation delay depends on packet length; transmission delay depends on cable length"},
                {"id": "B", "text": "Propagation delay is the physical time for a signal to travel the cable distance (d / v); transmission delay is the time to push bits onto the wire (L / R)"},
                {"id": "C", "text": "They are identical terms for latency"},
                {"id": "D", "text": "Transmission delay occurs only on wireless networks"}
            ],
            "correctOptionIds": ["B"],
            "explanation": "Propagation delay = distance / speed of light (approx 200,000 km/s in fiber). Transmission delay = Packet size / Link bandwidth.",
            "difficulty": "medium",
            "subtopic": "Delay Components"
        },
        {
            "id": "l05-q15",
            "type": "single_choice",
            "question": "If an edge weight represents latency, and two paths exist: Path 1 (1 hop, 50ms) and Path 2 (3 hops, 15ms total), which path will Dijkstra choose?",
            "options": [
                {"id": "A", "text": "Path 1, because it has fewer hops"},
                {"id": "B", "text": "Path 2, because its cumulative edge weight (15ms) is lower"},
                {"id": "C", "text": "It will randomly alternate between both"},
                {"id": "D", "text": "It will fail because Path 2 has 3 hops"}
            ],
            "correctOptionIds": ["B"],
            "explanation": "Dijkstra minimizes the sum of edge weights along the path, selecting Path 2 (15ms) over Path 1 (50ms).",
            "difficulty": "easy",
            "subtopic": "Shortest Path"
        },
        {
            "id": "l05-q16",
            "type": "single_choice",
            "question": "What is asymmetric routing in real-world computer networks?",
            "options": [
                {"id": "A", "text": "Packets from A to B travel via a different physical path than returning packets from B to A"},
                {"id": "B", "text": "Packets travel faster than the speed of light"},
                {"id": "C", "text": "A router uses IPv4 for outgoing and IPv6 for incoming packets"},
                {"id": "D", "text": "Half-duplex Ethernet communication"}
            ],
            "correctOptionIds": ["A"],
            "explanation": "Asymmetric routing occurs when outbound and inbound traffic take different network paths due to differing ISP policies or hot-potato routing.",
            "difficulty": "medium",
            "subtopic": "Asymmetric Routing"
        },
        {
            "id": "l05-q17",
            "type": "single_choice",
            "question": "In a graph with |V| = 1000 routers and |E| = 3000 links, why is Dijkstra with a binary heap much faster than naive Dijkstra with an array?",
            "options": [
                {"id": "A", "text": "Binary heap runs in O(V + E log V) ≈ 3.3x10^4 ops vs. array O(V^2) = 1,000,000 ops"},
                {"id": "B", "text": "Binary heap requires no memory"},
                {"id": "C", "text": "Array implementation cannot handle positive numbers"},
                {"id": "D", "text": "Binary heap converts graphs into trees"}
            ],
            "correctOptionIds": ["A"],
            "explanation": "For sparse graphs (E << V^2), a min-heap scales with O(E log V), which is orders of magnitude faster than searching an array in O(V^2).",
            "difficulty": "hard",
            "subtopic": "Algorithmic Efficiency"
        },
        {
            "id": "l05-q18",
            "type": "single_choice",
            "question": "Can Dijkstra's algorithm detect if a destination node is completely unreachable from the source?",
            "options": [
                {"id": "A", "text": "No, it enters an infinite loop"},
                {"id": "B", "text": "Yes, unreachable nodes retain their initial tentative distance of infinity (float('inf'))"},
                {"id": "C", "text": "No, it returns cost 0 for unreachable nodes"},
                {"id": "D", "text": "It raises a Segmentation Fault"}
            ],
            "correctOptionIds": ["B"],
            "explanation": "Vertices in disconnected components are never extracted or relaxed; their recorded distance remains infinity.",
            "difficulty": "easy",
            "subtopic": "Reachability"
        },
        {
            "id": "l05-q19",
            "type": "multi_choice",
            "question": "Which of the following metrics can be legally used as edge weights in Dijkstra's algorithm? (Select ALL that apply)",
            "options": [
                {"id": "A", "text": "Propagation delay in milliseconds (non-negative)"},
                {"id": "B", "text": "Hop count (w = 1 for each link)"},
                {"id": "C", "text": "Financial transit cost in dollars per gigabyte (non-negative)"},
                {"id": "D", "text": "Negative packet rebate incentives (w < 0)"}
            ],
            "correctOptionIds": ["A", "B", "C"],
            "explanation": "Any non-negative cost metric is valid for Dijkstra. Negative metrics (D) violate Dijkstra's greedy invariant and cause incorrect results.",
            "difficulty": "medium",
            "subtopic": "Metric Selection"
        },
        {
            "id": "l05-q20",
            "type": "single_choice",
            "question": "How does an SDN (Software-Defined Networking) controller use graph algorithms compared to traditional distributed routers?",
            "options": [
                {"id": "A", "text": "The centralized SDN controller maintains a global view of all switches and computes optimal paths centrally, downloading flow rules to switches"},
                {"id": "B", "text": "SDN controllers disable all graph algorithms"},
                {"id": "C", "text": "SDN switches run Dijkstra independently on each port"},
                {"id": "D", "text": "SDN switches only support BFS"}
            ],
            "correctOptionIds": ["A"],
            "explanation": "In SDN, the control plane is centralized. The SDN controller computes shortest paths globally and installs flow forwarding entries directly into switch TCAMs via OpenFlow.",
            "difficulty": "medium",
            "subtopic": "SDN Graph Routing"
        }
    ]
}

print("Loaded Lecture 05.")
