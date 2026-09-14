"""
Complete Quiz Definitions for Lectures 06, 07, 08 and all remaining modules.
Integrates handwritten notes (ip route add, ip neigh add, interfaces lo/eth0/wlan0,
LPM tables, etc.) with 20 distinct questions per lecture.
"""

from typing import Dict, Any

def get_additional_quizzes() -> Dict[str, Any]:
    q = {}

    # --- LECTURE 06: Graph Algorithms for Networking II ---
    q["lecture-06"] = {
        "topicId": "lecture-06",
        "lectureNumber": 6,
        "title": "Graph Algorithms for Networking II Quiz",
        "description": "20 questions covering Bellman-Ford, negative weights, Minimum Spanning Trees (Kruskal/Prim), and Spanning Tree Protocol (STP).",
        "estimatedMinutes": 25,
        "questions": [
            {
                "id": "l06-q01",
                "type": "single_choice",
                "question": "Why does Dijkstra's algorithm fail to produce optimal paths when a graph contains negative edge weights?",
                "options": [
                    {"id": "A", "text": "Because priority queues cannot store negative numbers"},
                    {"id": "B", "text": "Because its greedy invariant assumes once a node is finalized, its shortest distance cannot be improved by any unexplored path"},
                    {"id": "C", "text": "Because negative numbers cause integer overflow in 32-bit CPUs"},
                    {"id": "D", "text": "Because negative weights turn undirected graphs into directed graphs"}
                ],
                "correctOptionIds": ["B"],
                "explanation": "Dijkstra greedily marks the minimum tentative node as permanently optimal. If a negative edge appears later on an alternate path, it could reduce the total cost of an already-finalized node, violating the greedy invariant.",
                "difficulty": "medium",
                "subtopic": "Dijkstra Negative Weights"
            },
            {
                "id": "l06-q02",
                "type": "single_choice",
                "question": "What occurs when a directed graph contains a negative-weight cycle reachable from the source?",
                "options": [
                    {"id": "A", "text": "The shortest path distance between nodes becomes mathematically undefined (-infinity)"},
                    {"id": "B", "text": "The graph automatically converts into a tree"},
                    {"id": "C", "text": "The cycle acts as an infinite bandwidth buffer"},
                    {"id": "D", "text": "The shortest path becomes 0"}
                ],
                "correctOptionIds": ["A"],
                "explanation": "Traversing a negative cycle repeatedly reduces the total path cost on each revolution, allowing path cost to decrease indefinitely towards -infinity.",
                "difficulty": "medium",
                "subtopic": "Negative Cycles"
            },
            {
                "id": "l06-q03",
                "type": "single_choice",
                "question": "In the Bellman-Ford algorithm, why are all edges relaxed exactly |V| - 1 times?",
                "options": [
                    {"id": "A", "text": "Because CPU clock cycles are limited to |V| - 1"},
                    {"id": "B", "text": "Because any simple shortest path without cycles in a graph of |V| vertices contains at most |V| - 1 edges"},
                    {"id": "C", "text": "To prevent memory leaks"},
                    {"id": "D", "text": "Because of Ethernet frame padding rules"}
                ],
                "correctOptionIds": ["B"],
                "explanation": "A simple path touching |V| vertices has at most |V| - 1 edges. Each relaxation pass guarantees discovery of shortest paths with one additional edge.",
                "difficulty": "hard",
                "subtopic": "Bellman-Ford Invariant"
            },
            {
                "id": "l06-q04",
                "type": "single_choice",
                "question": "How does the Bellman-Ford algorithm detect the presence of a reachable negative-weight cycle?",
                "options": [
                    {"id": "A", "text": "By checking if the source distance becomes negative"},
                    {"id": "B", "text": "By performing a |V|-th relaxation pass; if any distance dist[v] can still be decreased, a negative cycle exists"},
                    {"id": "C", "text": "By running BFS on the graph"},
                    {"id": "D", "text": "By checking if the priority queue is empty"}
                ],
                "correctOptionIds": ["B"],
                "explanation": "If all simple shortest paths are found after |V|-1 passes, a further relaxation on the |V|-th pass can only occur if a negative cycle continues to decrease path costs.",
                "difficulty": "medium",
                "subtopic": "Negative Cycle Detection"
            },
            {
                "id": "l06-q05",
                "type": "single_choice",
                "question": "What is the time complexity of the Bellman-Ford algorithm on a graph with |V| vertices and |E| edges?",
                "options": [
                    {"id": "A", "text": "O(V + E)"},
                    {"id": "B", "text": "O(V * E)"},
                    {"id": "C", "text": "O(E log V)"},
                    {"id": "D", "text": "O(V^3)"}
                ],
                "correctOptionIds": ["B"],
                "explanation": "Bellman-Ford runs |V| - 1 passes, relaxing all |E| edges in each pass, yielding O(|V| * |E|) time complexity.",
                "difficulty": "easy",
                "subtopic": "Bellman-Ford Complexity"
            },
            {
                "id": "l06-q06",
                "type": "single_choice",
                "question": "What fundamental routing protocol equation is derived directly from the distributed Bellman-Ford algorithm?",
                "options": [
                    {"id": "A", "text": "D_x(y) = min_v { c(x, v) + D_v(y) }"},
                    {"id": "B", "text": "Cost = 10^8 / Bandwidth"},
                    {"id": "C", "text": "MTU = MSS + 40"},
                    {"id": "D", "text": "2^N - 2 >= Hosts"}
                ],
                "correctOptionIds": ["A"],
                "explanation": "The Distributed Bellman-Ford equation states that router x reaches destination y with minimum cost by choosing the neighbor v that minimizes the sum of local link cost c(x,v) and v's advertised distance D_v(y).",
                "difficulty": "hard",
                "subtopic": "Distributed Bellman-Ford"
            },
            {
                "id": "l06-q07",
                "type": "single_choice",
                "question": "What is the definition of a Minimum Spanning Tree (MST)?",
                "options": [
                    {"id": "A", "text": "A tree connecting all |V| vertices using exactly |V| - 1 edges with the minimum possible total edge weight sum"},
                    {"id": "B", "text": "A tree where every node has degree 2"},
                    {"id": "C", "text": "A directed graph with no negative weights"},
                    {"id": "D", "text": "The shortest path tree from a single root node"}
                ],
                "correctOptionIds": ["A"],
                "explanation": "An MST connects all nodes in an undirected graph without cycles (using |V|-1 edges) such that the total sum of edge weights is minimized.",
                "difficulty": "easy",
                "subtopic": "MST Definition"
            },
            {
                "id": "l06-q08",
                "type": "single_choice",
                "question": "How does Kruskal's algorithm construct a Minimum Spanning Tree?",
                "options": [
                    {"id": "A", "text": "It explores nodes level-by-level using a FIFO queue"},
                    {"id": "B", "text": "It sorts all edges by weight and greedily adds the cheapest edge that does not form a cycle using Disjoint Set Union (DSU)"},
                    {"id": "C", "text": "It repeatedly relaxes all edges |V| - 1 times"},
                    {"id": "D", "text": "It begins at a random root and grows outward"}
                ],
                "correctOptionIds": ["B"],
                "explanation": "Kruskal's is an edge-centric greedy algorithm: edges are sorted in ascending order and added to the forest if their endpoints belong to different disjoint sets.",
                "difficulty": "medium",
                "subtopic": "Kruskal Algorithm"
            },
            {
                "id": "l06-q09",
                "type": "single_choice",
                "question": "What is the time complexity of Kruskal's algorithm with Disjoint Set Union (path compression and union by rank)?",
                "options": [
                    {"id": "A", "text": "O(E log E) = O(E log V)"},
                    {"id": "B", "text": "O(V^2)"},
                    {"id": "C", "text": "O(V * E)"},
                    {"id": "D", "text": "O(V^3)"}
                ],
                "correctOptionIds": ["A"],
                "explanation": "Sorting |E| edges dominates the time complexity, requiring O(|E| log |E|) = O(|E| log |V|). DSU operations run in near-linear O(E α(V)) time.",
                "difficulty": "medium",
                "subtopic": "Kruskal Complexity"
            },
            {
                "id": "l06-q10",
                "type": "single_choice",
                "question": "How does Prim's algorithm differ conceptually from Kruskal's algorithm?",
                "options": [
                    {"id": "A", "text": "Prim's grows a single connected tree vertex by vertex from an initial root, whereas Kruskal's maintains a forest of disconnected components"},
                    {"id": "B", "text": "Prim's only works on directed graphs"},
                    {"id": "C", "text": "Prim's uses Bellman-Ford internally"},
                    {"id": "D", "text": "Prim's requires negative edge weights"}
                ],
                "correctOptionIds": ["A"],
                "explanation": "Prim's algorithm is vertex-centric: it grows a continuous tree by greedily adding the cheapest cut-crossing edge connected to the existing tree.",
                "difficulty": "medium",
                "subtopic": "Prim vs Kruskal"
            },
            {
                "id": "l06-q11",
                "type": "single_choice",
                "question": "Why are physical loops in Layer 2 switched Ethernet networks catastrophic if Spanning Tree Protocol is disabled?",
                "options": [
                    {"id": "A", "text": "Because Ethernet frames lack a Time To Live (TTL) field, causing frames to circulate infinitely and trigger broadcast storms"},
                    {"id": "B", "text": "Because copper wires melt under high voltage"},
                    {"id": "C", "text": "Because IP addresses are automatically deleted"},
                    {"id": "D", "text": "Because DHCP servers stop working"}
                ],
                "correctOptionIds": ["A"],
                "explanation": "Unlike Layer 3 IP packets (which are dropped when TTL reaches 0), Layer 2 Ethernet frames have NO TTL field! A looped broadcast circulates forever, crashing the switches.",
                "difficulty": "hard",
                "subtopic": "Layer 2 Loops"
            },
            {
                "id": "l06-q12",
                "type": "single_choice",
                "question": "What is MAC table flapping (thrashing) caused by a Layer 2 loop?",
                "options": [
                    {"id": "A", "text": "A physical connector becoming loose"},
                    {"id": "B", "text": "A switch repeatedly overwriting the learned port for a MAC address as duplicate looping frames arrive alternately on different ports"},
                    {"id": "C", "text": "A network card alternating between 10 Mbps and 100 Mbps"},
                    {"id": "D", "text": "A DNS server failing to resolve a domain"}
                ],
                "correctOptionIds": ["B"],
                "explanation": "Switches learn MAC locations from the source MAC of incoming frames. When duplicate looping frames hit Port 1 then Port 2, the switch MAC table thrashes constantly, exhausting CPU.",
                "difficulty": "medium",
                "subtopic": "MAC Table Thrashing"
            },
            {
                "id": "l06-q13",
                "type": "single_choice",
                "question": "In the Spanning Tree Protocol (IEEE 802.1D), what message unit do switches exchange every 2 seconds to elect the Root Bridge and detect loops?",
                "options": [
                    {"id": "A", "text": "ICMP Echo Requests"},
                    {"id": "B", "text": "Bridge Protocol Data Units (BPDUs)"},
                    {"id": "C", "text": "OSPF Hello Packets"},
                    {"id": "D", "text": "ARP Announcements"}
                ],
                "correctOptionIds": ["B"],
                "explanation": "Switches exchange Bridge Protocol Data Units (BPDUs) to negotiate the spanning tree topology.",
                "difficulty": "easy",
                "subtopic": "STP BPDUs"
            },
            {
                "id": "l06-q14",
                "type": "single_choice",
                "question": "How is the STP Root Bridge elected among competing switches in a LAN?",
                "options": [
                    {"id": "A", "text": "The switch with the highest IP address wins"},
                    {"id": "B", "text": "The switch with the lowest Bridge ID (Priority + MAC address) wins"},
                    {"id": "C", "text": "The switch connected to the ISP router wins automatically"},
                    {"id": "D", "text": "The switch with the greatest number of physical ports wins"}
                ],
                "correctOptionIds": ["B"],
                "explanation": "The switch with the lowest Bridge ID (BID = Priority + MAC) is elected Root Bridge. Default priority is 32768, so lowest MAC breaks ties.",
                "difficulty": "medium",
                "subtopic": "Root Bridge Election"
            },
            {
                "id": "l06-q15",
                "type": "single_choice",
                "question": "What is a 'Root Port' (RP) on a non-root switch in STP?",
                "options": [
                    {"id": "A", "text": "The port that connects directly to end-user PCs"},
                    {"id": "B", "text": "The single port on the switch with the lowest cumulative path cost to the Root Bridge"},
                    {"id": "C", "text": "A port that is disabled by the network administrator"},
                    {"id": "D", "text": "A port running optical fiber"}
                ],
                "correctOptionIds": ["B"],
                "explanation": "Every non-root switch elects exactly one Root Port: the port offering the lowest total path cost back to the Root Bridge.",
                "difficulty": "medium",
                "subtopic": "STP Port Roles"
            },
            {
                "id": "l06-q16",
                "type": "single_choice",
                "question": "What happens to a switch port assigned the 'Blocking' (or Alternate) state in STP?",
                "options": [
                    {"id": "A", "text": "It turns off electrical power to the port"},
                    {"id": "B", "text": "It drops all user data frames but continues to listen to BPDUs to detect network link failures"},
                    {"id": "C", "text": "It forwards only multicast packets"},
                    {"id": "D", "text": "It acts as a DHCP server"}
                ],
                "correctOptionIds": ["B"],
                "explanation": "Blocking ports do not forward user data (breaking the loop), but listen for BPDUs so they can transition to forwarding if a primary link fails.",
                "difficulty": "medium",
                "subtopic": "STP Port States"
            },
            {
                "id": "l06-q17",
                "type": "multi_choice",
                "question": "Which of the following are valid STP port transition states in IEEE 802.1D before a port reaches the active Forwarding state? (Select ALL that apply)",
                "options": [
                    {"id": "A", "text": "Blocking"},
                    {"id": "B", "text": "Listening"},
                    {"id": "C", "text": "Learning"},
                    {"id": "D", "text": "Snooping"}
                ],
                "correctOptionIds": ["A", "B", "C"],
                "explanation": "Legacy 802.1D transitions through: Blocking -> Listening (15s) -> Learning (15s) -> Forwarding, totaling 30-50s convergence time.",
                "difficulty": "hard",
                "subtopic": "STP Convergence"
            },
            {
                "id": "l06-q18",
                "type": "single_choice",
                "question": "Under what condition is the Minimum Spanning Tree of a graph guaranteed to be strictly unique?",
                "options": [
                    {"id": "A", "text": "When the graph is bipartite"},
                    {"id": "B", "text": "When all edge weights in the graph are distinct (unique)"},
                    {"id": "C", "text": "When the graph has an odd number of vertices"},
                    {"id": "D", "text": "When all edge weights are negative"}
                ],
                "correctOptionIds": ["B"],
                "explanation": "If all edge weights in a connected graph are strictly distinct, the MST is mathematically unique.",
                "difficulty": "hard",
                "subtopic": "MST Uniqueness"
            },
            {
                "id": "l06-q19",
                "type": "single_choice",
                "question": "What is the key difference between a Shortest Path Tree (SPT) computed by Dijkstra and a Minimum Spanning Tree (MST)?",
                "options": [
                    {"id": "A", "text": "An SPT minimizes the distance from one source to all nodes; an MST minimizes the total weight of all edges across the whole graph"},
                    {"id": "B", "text": "An SPT has cycles, while an MST does not"},
                    {"id": "C", "text": "Dijkstra only works on unweighted graphs"},
                    {"id": "D", "text": "An MST requires a designated source root node"}
                ],
                "correctOptionIds": ["A"],
                "explanation": "Dijkstra optimizes point-to-point distances from a specific source. MST optimizes total global infrastructure/wire cost.",
                "difficulty": "medium",
                "subtopic": "SPT vs MST"
            },
            {
                "id": "l06-q20",
                "type": "single_choice",
                "question": "Switch A has MAC 00:1A:2B:3C:4D:5E and priority 32768. Switch B has MAC 00:1A:2B:3C:4D:5F and priority 4096. Which switch becomes the STP Root Bridge?",
                "options": [
                    {"id": "A", "text": "Switch A, because its MAC address is numerically smaller"},
                    {"id": "B", "text": "Switch B, because its Bridge Priority (4096) is lower than 32768"},
                    {"id": "C", "text": "Both switches share the Root Bridge duty"},
                    {"id": "D", "text": "Neither, the network will crash"}
                ],
                "correctOptionIds": ["B"],
                "explanation": "Bridge ID evaluates Bridge Priority first. Switch B has priority 4096 < 32768, so Switch B wins immediately; MAC addresses are only checked if priorities tie.",
                "difficulty": "easy",
                "subtopic": "Root Bridge Calculation"
            }
        ]
    }

    # --- LECTURE 07: Routing & Forwarding I ---
    q["lecture-07"] = {
        "topicId": "lecture-07",
        "lectureNumber": 7,
        "title": "Routing & Forwarding I Quiz",
        "description": "20 questions covering Control vs Data plane, RIB vs FIB, Longest Prefix Match (LPM), TCAM, and router forwarding lifecycle.",
        "estimatedMinutes": 25,
        "questions": [
            {
                "id": "l07-q01",
                "type": "single_choice",
                "question": "What is the fundamental distinction between Routing and Forwarding in computer networks?",
                "options": [
                    {"id": "A", "text": "Routing is fast in hardware; Forwarding is slow in software"},
                    {"id": "B", "text": "Routing (Control Plane) determines the end-to-end path; Forwarding (Data Plane) moves packets from input to output interfaces at wire speed"},
                    {"id": "C", "text": "Routing operates at Layer 2; Forwarding operates at Layer 4"},
                    {"id": "D", "text": "Routing is only used on home Wi-Fi routers"}
                ],
                "correctOptionIds": ["B"],
                "explanation": "Routing (Control Plane) runs distributed routing protocols on general CPUs to build the map. Forwarding (Data Plane) executes table lookups per packet in hardware ASICs.",
                "difficulty": "easy",
                "subtopic": "Control vs Data Plane"
            },
            {
                "id": "l07-q02",
                "type": "single_choice",
                "question": "What is the difference between the RIB (Routing Information Base) and the FIB (Forwarding Information Base)?",
                "options": [
                    {"id": "A", "text": "RIB contains all learned candidate routes in CPU RAM; FIB is the compiled, flattened single-best-path table installed in line card silicon memory"},
                    {"id": "B", "text": "RIB stores MAC addresses; FIB stores IP addresses"},
                    {"id": "C", "text": "RIB is located on the user PC; FIB is located in the cloud"},
                    {"id": "D", "text": "They are identical tables with different names"}
                ],
                "correctOptionIds": ["A"],
                "explanation": "The RIB holds all candidate routes from OSPF, BGP, static configs. The router compiles the best winning next-hop per prefix into the FIB for nanosecond ASIC lookups.",
                "difficulty": "medium",
                "subtopic": "RIB vs FIB"
            },
            {
                "id": "l07-q03",
                "type": "single_choice",
                "question": "What is the Longest Prefix Match (LPM) rule in IP forwarding?",
                "options": [
                    {"id": "A", "text": "The router always selects the route with the lowest metric"},
                    {"id": "B", "text": "When a destination IP matches multiple routing table entries, the router ALWAYS selects the entry with the longest prefix length (most specific mask)"},
                    {"id": "C", "text": "The router forwards to the route learned from the oldest protocol"},
                    {"id": "D", "text": "The router selects the default route 0.0.0.0/0 first"}
                ],
                "correctOptionIds": ["B"],
                "explanation": "LPM dictates that the entry matching the greatest number of contiguous network bits (most specific destination range) is selected, overriding metric and administrative distance.",
                "difficulty": "medium",
                "subtopic": "Longest Prefix Match"
            },
            {
                "id": "l07-q04",
                "type": "single_choice",
                "question": "Consider the routing table from the lecture notes:\n- 10.0.0.0/8 via 192.168.1.1 dev eth0\n- 10.10.0.0/16 via 192.168.2.1 dev eth1\n- 10.10.20.0/24 via 192.168.3.1 dev eth2\n- 10.10.20.128/25 via 192.168.4.1 dev eth3\n- 0.0.0.0/0 via 192.168.5.1 dev eth4\n\nA packet arrives destined for 10.10.20.150. Which interface will the router forward it to?",
                "options": [
                    {"id": "A", "text": "eth0 (10.0.0.0/8)"},
                    {"id": "B", "text": "eth1 (10.10.0.0/16)"},
                    {"id": "C", "text": "eth2 (10.10.20.0/24)"},
                    {"id": "D", "text": "eth3 (10.10.20.128/25)"}
                ],
                "correctOptionIds": ["D"],
                "explanation": "10.10.20.150 matches /8, /16, /24, and /25. By Longest Prefix Match, /25 (25 bits) is the longest and most specific prefix. The router forwards out eth3.",
                "difficulty": "medium",
                "subtopic": "LPM Table Lookup"
            },
            {
                "id": "l07-q05",
                "type": "single_choice",
                "question": "Using the same table from question 4, where is a packet destined for 10.10.20.50 forwarded?",
                "options": [
                    {"id": "A", "text": "eth2 (10.10.20.0/24)"},
                    {"id": "B", "text": "eth3 (10.10.20.128/25)"},
                    {"id": "C", "text": "eth4 (0.0.0.0/0)"},
                    {"id": "D", "text": "eth0 (10.0.0.0/8)"}
                ],
                "correctOptionIds": ["A"],
                "explanation": "10.10.20.50 falls into .0-.127, so it does NOT match /25 (.128-.255). Among the remaining matching entries (/8, /16, /24), /24 is the longest match (eth2).",
                "difficulty": "medium",
                "subtopic": "LPM Table Lookup"
            },
            {
                "id": "l07-q06",
                "type": "single_choice",
                "question": "Using the same table from question 4, where is a packet destined for 8.8.8.8 forwarded?",
                "options": [
                    {"id": "A", "text": "eth0"},
                    {"id": "B", "text": "eth1"},
                    {"id": "C", "text": "eth4 (0.0.0.0/0 Default Route)"},
                    {"id": "D", "text": "The packet is dropped immediately"}
                ],
                "correctOptionIds": ["C"],
                "explanation": "8.8.8.8 does not match 10.x.x.x. It matches only the default route 0.0.0.0/0, forwarding out eth4 to 192.168.5.1.",
                "difficulty": "easy",
                "subtopic": "Default Route"
            },
            {
                "id": "l07-q07",
                "type": "single_choice",
                "question": "What is the Linux command to manually add a static route for network 172.16.1.0/24 via gateway 10.0.0.2 out interface eth1 (as highlighted in the handwritten notes)?",
                "options": [
                    {"id": "A", "text": "route -n 172.16.1.0/24 10.0.0.2"},
                    {"id": "B", "text": "ip route add 172.16.1.0/24 via 10.0.0.2 dev eth1"},
                    {"id": "C", "text": "ifconfig eth1 172.16.1.0 netmask 10.0.0.2"},
                    {"id": "D", "text": "netstat add 172.16.1.0 via eth1"}
                ],
                "correctOptionIds": ["B"],
                "explanation": "The modern Linux iproute2 syntax is: 'ip route add <prefix> via <gateway> dev <interface>'.",
                "difficulty": "medium",
                "subtopic": "Static Route Commands"
            },
            {
                "id": "l07-q08",
                "type": "single_choice",
                "question": "Which Linux command manually inserts a static neighbor MAC address entry into the ARP cache table (from the handwritten notes)?",
                "options": [
                    {"id": "A", "text": "arp -s 10.0.0.2 aa:bb:cc:dd:ee:ff"},
                    {"id": "B", "text": "sudo ip neigh add 10.0.0.2 lladdr aa:bb:cc:dd:ee:ff dev eth1"},
                    {"id": "C", "text": "ip link set 10.0.0.2 address aa:bb:cc:dd:ee:ff"},
                    {"id": "D", "text": "route add -host 10.0.0.2 lladdr aa:bb"}
                ],
                "correctOptionIds": ["B"],
                "explanation": "'sudo ip neigh add <ip> lladdr <mac> dev <interface>' is the canonical iproute2 command for static neighbor table management.",
                "difficulty": "hard",
                "subtopic": "Neighbor Table Commands"
            },
            {
                "id": "l07-q09",
                "type": "multi_choice",
                "question": "According to standard Unix/Linux networking conventions (referenced in the handwritten notes), what do the interface names 'lo', 'eth0', and 'wlan0' signify? (Select ALL that apply)",
                "options": [
                    {"id": "A", "text": "lo represents the software Loopback interface"},
                    {"id": "B", "text": "eth0 represents the first wired physical Ethernet interface"},
                    {"id": "C", "text": "wlan0 represents the first Wireless Local Area Network (Wi-Fi) interface"},
                    {"id": "D", "text": "eth0 is reserved strictly for default gateway routers"}
                ],
                "correctOptionIds": ["A", "B", "C"],
                "explanation": "lo = loopback (127.0.0.1), eth0 = first Ethernet NIC, wlan0 = first Wi-Fi adapter.",
                "difficulty": "easy",
                "subtopic": "Interface Nomenclature"
            },
            {
                "id": "l07-q10",
                "type": "single_choice",
                "question": "Why is a /30 subnet typically configured on router WAN interfaces connected to an ISP (e.g. eth1 10.0.0.1/30)?",
                "options": [
                    {"id": "A", "text": "Because ISPs only support 30 Mbps bandwidth"},
                    {"id": "B", "text": "Because a /30 provides exactly 2 usable host IPs (one for the customer router, one for the ISP gateway) with zero wasted address space"},
                    {"id": "C", "text": "Because it disables ARP"},
                    {"id": "D", "text": "Because 30 is a prime number"}
                ],
                "correctOptionIds": ["B"],
                "explanation": "A /30 contains 4 IP addresses (2^2): 1 network, 2 usable hosts, 1 broadcast. Perfect for point-to-point router links without wasting public IPs.",
                "difficulty": "medium",
                "subtopic": "WAN Subnet Design"
            },
            {
                "id": "l07-q11",
                "type": "single_choice",
                "question": "What is the third bit state supported by TCAM (Ternary Content Addressable Memory) in router silicon, beyond binary 0 and 1?",
                "options": [
                    {"id": "A", "text": "Error (E)"},
                    {"id": "B", "text": "Don't Care / Wildcard (X)"},
                    {"id": "C", "text": "High Voltage (H)"},
                    {"id": "D", "text": "Float (F)"}
                ],
                "correctOptionIds": ["B"],
                "explanation": "TCAM supports 0, 1, and X (Don't Care / Masked bits), enabling single-clock-cycle parallel Longest Prefix Match lookups across 1,000,000 entries.",
                "difficulty": "medium",
                "subtopic": "TCAM Architecture"
            },
            {
                "id": "l07-q12",
                "type": "single_choice",
                "question": "What is the lookup time complexity of a hardware TCAM in an enterprise router line card?",
                "options": [
                    {"id": "A", "text": "O(1) — constant time in a single hardware clock cycle"},
                    {"id": "B", "text": "O(N) — linear scan of all routes"},
                    {"id": "C", "text": "O(log N)"},
                    {"id": "D", "text": "O(N^2)"}
                ],
                "correctOptionIds": ["A"],
                "explanation": "TCAM circuits compare the incoming destination IP against all routing entries in parallel in a single hardware cycle (typically 2-5 nanoseconds).",
                "difficulty": "medium",
                "subtopic": "TCAM Performance"
            },
            {
                "id": "l07-q13",
                "type": "single_choice",
                "question": "What data structure is commonly used in software routing engines (like the Linux kernel FIB) to perform Longest Prefix Match lookups efficiently?",
                "options": [
                    {"id": "A", "text": "Linked List"},
                    {"id": "B", "text": "Patricia / Radix Trie (bit-compressed prefix tree)"},
                    {"id": "C", "text": "Circular Ring Buffer"},
                    {"id": "D", "text": "Binary Search Tree on destination IP"}
                ],
                "correctOptionIds": ["B"],
                "explanation": "A Radix/Patricia Trie branches on bits (0 = left, 1 = right) with path compression, finding the longest matching prefix in at most 32 bit steps (O(32) = O(1)).",
                "difficulty": "hard",
                "subtopic": "Radix Trie"
            },
            {
                "id": "l07-q14",
                "type": "single_choice",
                "question": "What happens in Step 4 of the router packet forwarding lifecycle when the IPv4 TTL field is decremented to 0?",
                "options": [
                    {"id": "A", "text": "The router resets TTL to 64 and forwards the packet"},
                    {"id": "B", "text": "The router drops the packet and transmits an ICMP Type 11 (Time-to-Live Exceeded in Transit) message back to the source"},
                    {"id": "C", "text": "The router saves the packet to hard disk"},
                    {"id": "D", "text": "The router broadcasts the packet to all ports"}
                ],
                "correctOptionIds": ["B"],
                "explanation": "TTL decrementing kills looping packets. When TTL reaches 0, the packet is discarded and an ICMP Type 11 Code 0 is returned to the source.",
                "difficulty": "medium",
                "subtopic": "TTL Exceeded"
            },
            {
                "id": "l07-q15",
                "type": "single_choice",
                "question": "Why MUST a router recalculate the IPv4 Header Checksum at every single forwarding hop?",
                "options": [
                    {"id": "A", "text": "Because the source MAC address changes"},
                    {"id": "B", "text": "Because the TTL field was decremented by 1, changing the arithmetic sum of the header bits"},
                    {"id": "C", "text": "Because the TCP payload changes"},
                    {"id": "D", "text": "Because the router clock is synchronized with NTP"}
                ],
                "correctOptionIds": ["B"],
                "explanation": "The IPv4 checksum covers the entire IP header. Because TTL decreases by 1, the checksum is invalid and must be updated.",
                "difficulty": "easy",
                "subtopic": "IP Checksum Recalculation"
            },
            {
                "id": "l07-q16",
                "type": "single_choice",
                "question": "What is a 'Floating Static Route'?",
                "options": [
                    {"id": "A", "text": "A route configured without an IP address"},
                    {"id": "B", "text": "A backup static route configured with a higher Administrative Distance that only becomes active if the primary dynamic/static route fails"},
                    {"id": "C", "text": "A route used on cruise ships"},
                    {"id": "D", "text": "A route that moves across interfaces automatically"}
                ],
                "correctOptionIds": ["B"],
                "explanation": "By setting an AD higher than the primary link (e.g. AD 10 vs primary AD 1), the floating static route stays dormant until the primary link drops, achieving automatic failover.",
                "difficulty": "medium",
                "subtopic": "Floating Static Routes"
            },
            {
                "id": "l07-q17",
                "type": "single_choice",
                "question": "In Cisco IOS routing tables, what does the notation [110/20] beside an OSPF route indicate?",
                "options": [
                    {"id": "A", "text": "110 seconds remaining before timeout; 20 hops"},
                    {"id": "B", "text": "Administrative Distance = 110 (trustworthiness); Metric/Cost = 20"},
                    {"id": "C", "text": "110 packets forwarded; 20 packets dropped"},
                    {"id": "D", "text": "Port 110 mapped to Port 20"}
                ],
                "correctOptionIds": ["B"],
                "explanation": "The first number is Administrative Distance (AD), where lower AD is preferred between protocols. The second number is the internal metric/cost.",
                "difficulty": "easy",
                "subtopic": "Routing Table Notation"
            },
            {
                "id": "l07-q18",
                "type": "multi_choice",
                "question": "Which of the following actions occur during Step 9 of the router forwarding lifecycle when transmitting a packet onto the egress wire? (Select ALL that apply)",
                "options": [
                    {"id": "A", "text": "The router sets the destination MAC to the Next-Hop router's MAC address"},
                    {"id": "B", "text": "The router sets the source MAC to its own outgoing interface MAC address"},
                    {"id": "C", "text": "The router recalculates the Layer 2 CRC-32 Frame Check Sequence (FCS)"},
                    {"id": "D", "text": "The router modifies the destination IP address to match the next hop"}
                ],
                "correctOptionIds": ["A", "B", "C"],
                "explanation": "A, B, and C describe Layer 2 encapsulation. D is incorrect: destination IP is never modified by standard routers (only by NAT).",
                "difficulty": "medium",
                "subtopic": "Layer 2 Rewrite"
            },
            {
                "id": "l07-q19",
                "type": "single_choice",
                "question": "How does the diagnostic utility 'traceroute' exploit router forwarding behavior to discover each hop along an internet path?",
                "options": [
                    {"id": "A", "text": "It asks the DNS root server for the list of routers"},
                    {"id": "B", "text": "It sends sequential packets starting with TTL=1, TTL=2, TTL=3..., eliciting ICMP Time Exceeded responses from each intermediate router"},
                    {"id": "C", "text": "It inspects the BGP table on the client computer"},
                    {"id": "D", "text": "It forces routers to broadcast their MAC addresses"}
                ],
                "correctOptionIds": ["B"],
                "explanation": "Traceroute sends packets with incremental TTLs. The 1st router drops TTL=1 and replies with ICMP Time Exceeded; the 2nd router drops TTL=2, revealing their IP addresses hop-by-hop.",
                "difficulty": "medium",
                "subtopic": "Traceroute Mechanics"
            },
            {
                "id": "l07-q20",
                "type": "single_choice",
                "question": "If two adjacent routers mistakenly configure static routes pointing to each other for the same destination subnet, what happens to packets sent to that subnet?",
                "options": [
                    {"id": "A", "text": "They bounce back and forth between the two routers until their TTL reaches 0 and they are dropped"},
                    {"id": "B", "text": "They are automatically forwarded to Google DNS"},
                    {"id": "C", "text": "They are absorbed by the ARP cache"},
                    {"id": "D", "text": "The routers crash immediately"}
                ],
                "correctOptionIds": ["A"],
                "explanation": "This creates a routing loop. Packets bounce between the two routers on the physical link, decrementing TTL by 1 per hop until TTL=0, where they are discarded.",
                "difficulty": "easy",
                "subtopic": "Routing Loops"
            }
        ]
    }

    # --- LECTURE 08: Routing & Forwarding II ---
    q["lecture-08"] = {
        "topicId": "lecture-08",
        "lectureNumber": 8,
        "title": "Routing & Forwarding II Quiz",
        "description": "20 questions covering Distance Vector (RIP), Count-to-Infinity, Split Horizon, Link-State (OSPF), Areas, and BGP Path Vector.",
        "estimatedMinutes": 25,
        "questions": [
            {
                "id": "l08-q01",
                "type": "single_choice",
                "question": "Why is Distance Vector routing often characterized as 'Routing by Rumor'?",
                "options": [
                    {"id": "A", "text": "Because routers broadcast news headlines"},
                    {"id": "B", "text": "Because routers do not know the global network topology; they blindly accept distance claims advertised by immediate neighbors"},
                    {"id": "C", "text": "Because distance vector protocols use unencrypted UDP packets"},
                    {"id": "D", "text": "Because it relies on social network graphs"}
                ],
                "correctOptionIds": ["B"],
                "explanation": "Routers in Distance Vector share their whole table with neighbors. A router trusts its neighbor's reported distance without independently verifying the actual path.",
                "difficulty": "easy",
                "subtopic": "Distance Vector Paradigm"
            },
            {
                "id": "l08-q02",
                "type": "single_choice",
                "question": "In RIP (Routing Information Protocol), what is the maximum valid hop count metric, and what value represents 'Infinity' (unreachable)?",
                "options": [
                    {"id": "A", "text": "Max metric is 15; 16 represents Infinity"},
                    {"id": "B", "text": "Max metric is 255; 256 represents Infinity"},
                    {"id": "C", "text": "Max metric is 100; 101 represents Infinity"},
                    {"id": "D", "text": "Max metric is 7; 8 represents Infinity"}
                ],
                "correctOptionIds": ["A"],
                "explanation": "RIP caps networks at 15 hops to mitigate count-to-infinity delays. Metric 16 is defined as unreachable (Infinity).",
                "difficulty": "easy",
                "subtopic": "RIP Constants"
            },
            {
                "id": "l08-q03",
                "type": "single_choice",
                "question": "How frequently does a standard RIPv2 router broadcast/multicast its entire routing table to its neighbors?",
                "options": [
                    {"id": "A", "text": "Every 5 seconds"},
                    {"id": "B", "text": "Every 30 seconds"},
                    {"id": "C", "text": "Every 5 minutes"},
                    {"id": "D", "text": "Only when an administrator types a command"}
                ],
                "correctOptionIds": ["B"],
                "explanation": "RIP sends unsolicited periodic full-table updates every 30 seconds via UDP port 520 (multicast 224.0.0.9 in RIPv2).",
                "difficulty": "easy",
                "subtopic": "RIP Timers"
            },
            {
                "id": "l08-q04",
                "type": "single_choice",
                "question": "What causes the 'Count-to-Infinity' problem in Distance Vector routing?",
                "options": [
                    {"id": "A", "text": "Routers running out of memory"},
                    {"id": "B", "text": "When a destination link fails, neighbors mutually believe the other still has a path, slowly incrementing the hop count between themselves until reaching 16"},
                    {"id": "C", "text": "BGP peering sessions timing out"},
                    {"id": "D", "text": "Broadcast storms on Ethernet switches"}
                ],
                "correctOptionIds": ["B"],
                "explanation": "Router B advertises a path that depended on C. When C's link drops, C assumes B has an alternate route and updates its cost. B then updates its cost from C, ping-ponging to 16.",
                "difficulty": "medium",
                "subtopic": "Count-to-Infinity"
            },
            {
                "id": "l08-q05",
                "type": "single_choice",
                "question": "What is the core operational rule of the 'Split Horizon' loop prevention mechanism?",
                "options": [
                    {"id": "A", "text": "Split routing tables into two halves"},
                    {"id": "B", "text": "Never advertise a route back out the same interface through which it was originally learned"},
                    {"id": "C", "text": "Disable all default routes"},
                    {"id": "D", "text": "Send updates only during nighttime"}
                ],
                "correctOptionIds": ["B"],
                "explanation": "Split Horizon prevents loops by forbidding a router from advertising a route back to the neighbor that taught it that route in the first place.",
                "difficulty": "medium",
                "subtopic": "Split Horizon"
            },
            {
                "id": "l08-q06",
                "type": "single_choice",
                "question": "How does 'Poison Reverse' modify the standard Split Horizon rule?",
                "options": [
                    {"id": "A", "text": "It sends corrupt checksums"},
                    {"id": "B", "text": "Instead of suppressing the advertisement, it explicitly advertises the route back to the source with metric = 16 (Infinity / Poisoned)"},
                    {"id": "C", "text": "It resets the interface MTU to 0"},
                    {"id": "D", "text": "It floods ICMP redirects"}
                ],
                "correctOptionIds": ["B"],
                "explanation": "Poison Reverse actively advertises unreachable (hop 16) back out the ingress interface, eliminating race conditions in multi-router topologies.",
                "difficulty": "medium",
                "subtopic": "Poison Reverse"
            },
            {
                "id": "l08-q07",
                "type": "single_choice",
                "question": "What is the purpose of a 'Hold-Down Timer' in distance vector routing?",
                "options": [
                    {"id": "A", "text": "To pause packet transmission when CPU temperature rises"},
                    {"id": "B", "text": "When a route is marked down, the router ignores any new updates for that route for a stabilization window (e.g. 180s) to allow loop flushes"},
                    {"id": "C", "text": "To keep the interface link up during cable unplugging"},
                    {"id": "D", "text": "To synchronize router clocks with UTC"}
                ],
                "correctOptionIds": ["B"],
                "explanation": "Hold-down timers prevent premature acceptance of stale or looping route claims while the network topology is still stabilizing.",
                "difficulty": "medium",
                "subtopic": "Hold-Down Timers"
            },
            {
                "id": "l08-q08",
                "type": "single_choice",
                "question": "What is a 'Triggered Update' (Flash Update) in distance vector protocols?",
                "options": [
                    {"id": "A", "text": "An update sent immediately when a route metric changes, without waiting for the 30-second timer to expire"},
                    {"id": "B", "text": "An update triggered by an email alert"},
                    {"id": "C", "text": "An update containing security patches"},
                    {"id": "D", "text": "A packet sent to wake up sleeping routers"}
                ],
                "correctOptionIds": ["A"],
                "explanation": "Triggered updates accelerate convergence by broadcasting link failures the exact microsecond they occur.",
                "difficulty": "easy",
                "subtopic": "Triggered Updates"
            },
            {
                "id": "l08-q09",
                "type": "single_choice",
                "question": "How does Link-State routing (OSPF) fundamentally differ from Distance Vector routing?",
                "options": [
                    {"id": "A", "text": "Link-state routers exchange entire routing tables; distance vector routers exchange single packets"},
                    {"id": "B", "text": "Every link-state router floods local Link-State Advertisements (LSAs) so all routers build an identical Link-State Database (LSDB), then run Dijkstra independently"},
                    {"id": "C", "text": "Link-state protocols only work on Wi-Fi"},
                    {"id": "D", "text": "Distance vector uses Dijkstra; link-state uses Bellman-Ford"}
                ],
                "correctOptionIds": ["B"],
                "explanation": "Link-state routers have complete visibility of the entire topological map (LSDB) and independently compute their own shortest-path tree using Dijkstra.",
                "difficulty": "medium",
                "subtopic": "Link-State Paradigm"
            },
            {
                "id": "l08-q10",
                "type": "multi_choice",
                "question": "Which of the following are standard OSPF packet types? (Select ALL that apply)",
                "options": [
                    {"id": "A", "text": "Hello Packet (Type 1)"},
                    {"id": "B", "text": "Database Description / DBD (Type 2)"},
                    {"id": "C", "text": "Link State Request / LSR (Type 3)"},
                    {"id": "D", "text": "Link State Update / LSU (Type 4)"}
                ],
                "correctOptionIds": ["A", "B", "C", "D"],
                "explanation": "OSPF defines 5 packet types: Hello, DBD, LSR, LSU, and LSAck (Type 5).",
                "difficulty": "easy",
                "subtopic": "OSPF Packets"
            },
            {
                "id": "l08-q11",
                "type": "single_choice",
                "question": "What transport layer protocol does OSPF use to carry its control packets across intermediate links?",
                "options": [
                    {"id": "A", "text": "TCP Port 179"},
                    {"id": "B", "text": "UDP Port 520"},
                    {"id": "C", "text": "Raw IP directly using Protocol Number 89"},
                    {"id": "D", "text": "HTTP/2"}
                ],
                "correctOptionIds": ["C"],
                "explanation": "OSPF does not use TCP or UDP. It encapsulates packets directly in raw IPv4/IPv6 packets with IP Protocol Number 89.",
                "difficulty": "hard",
                "subtopic": "OSPF Encapsulation"
            },
            {
                "id": "l08-q12",
                "type": "single_choice",
                "question": "What is the mandatory central area in a hierarchical OSPF deployment to which all other areas must connect?",
                "options": [
                    {"id": "A", "text": "Area 1 (Stub Area)"},
                    {"id": "B", "text": "Area 0 (Backbone Area)"},
                    {"id": "C", "text": "Area 255 (Transit Area)"},
                    {"id": "D", "text": "Area 100 (Autonomous Area)"}
                ],
                "correctOptionIds": ["B"],
                "explanation": "Area 0 (0.0.0.0) is the core Backbone Area. All inter-area traffic must transit through Area 0 to prevent routing loops.",
                "difficulty": "easy",
                "subtopic": "OSPF Area 0"
            },
            {
                "id": "l08-q13",
                "type": "single_choice",
                "question": "What is the role of an Area Border Router (ABR) in OSPF?",
                "options": [
                    {"id": "A", "text": "A router that connects to external non-OSPF networks like BGP"},
                    {"id": "B", "text": "A router with interfaces in Area 0 and one or more standard areas, summarizing routes and confining SPF recalculations"},
                    {"id": "C", "text": "A router that operates as a DNS caching resolver"},
                    {"id": "D", "text": "A router that only forwards multicast traffic"}
                ],
                "correctOptionIds": ["B"],
                "explanation": "ABRs connect Area 0 to sub-areas. They summarize internal area topology into summary LSAs, preventing link flaps in one area from triggering SPF runs in other areas.",
                "difficulty": "medium",
                "subtopic": "ABR Role"
            },
            {
                "id": "l08-q14",
                "type": "single_choice",
                "question": "On a broadcast multi-access Ethernet network with N = 10 OSPF routers, how many adjacencies would form without DR/BDR election?",
                "options": [
                    {"id": "A", "text": "10"},
                    {"id": "B", "text": "45 (N * (N - 1) / 2)"},
                    {"id": "C", "text": "90"},
                    {"id": "D", "text": "100"}
                ],
                "correctOptionIds": ["B"],
                "explanation": "Full mesh peering requires N(N-1)/2 adjacencies. For 10 routers, that is 10*9/2 = 45 redundant adjacencies flooding duplicate LSAs.",
                "difficulty": "medium",
                "subtopic": "DR/BDR Scalability"
            },
            {
                "id": "l08-q15",
                "type": "single_choice",
                "question": "How does the election of a Designated Router (DR) and Backup Designated Router (BDR) solve this scalability bottleneck?",
                "options": [
                    {"id": "A", "text": "It turns off 8 of the 10 routers"},
                    {"id": "B", "text": "Routers form adjacencies ONLY with the DR and BDR (multicast 224.0.0.6), reducing adjacencies from O(N^2) to O(N)"},
                    {"id": "C", "text": "It switches from OSPF to RIP"},
                    {"id": "D", "text": "It enables full-duplex transmission"}
                ],
                "correctOptionIds": ["B"],
                "explanation": "All other routers (DROthers) peer only with the DR/BDR, reducing total adjacencies to 2N - 3, dramatically conserving CPU and link bandwidth.",
                "difficulty": "medium",
                "subtopic": "DR/BDR Mechanism"
            },
            {
                "id": "l08-q16",
                "type": "single_choice",
                "question": "What is an Autonomous System (AS) in the context of global internet routing?",
                "options": [
                    {"id": "A", "text": "A self-driving automobile network"},
                    {"id": "B", "text": "A collection of connected IP routing networks controlled by a single administrative entity with a unified routing policy (e.g. AS15169 for Google)"},
                    {"id": "C", "text": "A single home Wi-Fi router"},
                    {"id": "D", "text": "An artificial intelligence model that manages routers"}
                ],
                "correctOptionIds": ["B"],
                "explanation": "An Autonomous System (AS) is an administrative domain (e.g. ISP, university, tech giant) identified by a globally unique Autonomous System Number (ASN).",
                "difficulty": "easy",
                "subtopic": "Autonomous Systems"
            },
            {
                "id": "l08-q17",
                "type": "single_choice",
                "question": "What protocol is the de facto standard Exterior Gateway Protocol (EGP) routing the global internet between different Autonomous Systems?",
                "options": [
                    {"id": "A", "text": "RIPv2"},
                    {"id": "B", "text": "OSPFv3"},
                    {"id": "C", "text": "BGP-4 (Border Gateway Protocol Version 4)"},
                    {"id": "D", "text": "IS-IS"}
                ],
                "correctOptionIds": ["C"],
                "explanation": "BGP-4 is the glue of the internet, exchanging reachability and policy paths between thousands of global Autonomous Systems.",
                "difficulty": "easy",
                "subtopic": "BGP-4"
            },
            {
                "id": "l08-q18",
                "type": "single_choice",
                "question": "Why is BGP classified as a 'Path Vector' protocol rather than pure Distance Vector or Link State?",
                "options": [
                    {"id": "A", "text": "Because it routes vectors of floating point numbers"},
                    {"id": "B", "text": "Because it advertises the complete sequence of Autonomous System Numbers (AS_PATH) traversed to reach each destination prefix"},
                    {"id": "C", "text": "Because it uses vector graphics for network maps"},
                    {"id": "D", "text": "Because it runs over UDP"}
                ],
                "correctOptionIds": ["B"],
                "explanation": "Instead of advertising pure hop counts, BGP includes the entire path of ASNs in the AS_PATH attribute.",
                "difficulty": "medium",
                "subtopic": "Path Vector Concept"
            },
            {
                "id": "l08-q19",
                "type": "single_choice",
                "question": "How does BGP's AS_PATH attribute provide immediate, foolproof routing loop detection without running Dijkstra's algorithm?",
                "options": [
                    {"id": "A", "text": "If a border router receives a BGP advertisement containing its own Autonomous System Number in the AS_PATH, it immediately discards the route"},
                    {"id": "B", "text": "It checks if the AS_PATH has more than 16 hops"},
                    {"id": "C", "text": "It pings all ASNs in the path"},
                    {"id": "D", "text": "It computes a CRC-32 on the ASNs"}
                ],
                "correctOptionIds": ["A"],
                "explanation": "If a router sees its own ASN in the AS_PATH, it knows the route has already passed through its network, so accepting it would create an inter-domain loop. It drops it instantly.",
                "difficulty": "hard",
                "subtopic": "AS_PATH Loop Elimination"
            },
            {
                "id": "l08-q20",
                "type": "single_choice",
                "question": "What transport layer protocol and port number does BGP use to establish reliable peer sessions?",
                "options": [
                    {"id": "A", "text": "UDP Port 520"},
                    {"id": "B", "text": "Raw IP Protocol 89"},
                    {"id": "C", "text": "TCP Port 179"},
                    {"id": "D", "text": "TLS Port 443"}
                ],
                "correctOptionIds": ["C"],
                "explanation": "BGP relies on TCP Port 179 for point-to-point connection establishment, retransmission, and reliability.",
                "difficulty": "medium",
                "subtopic": "BGP Transport"
            }
        ]
    }

    return q

if __name__ == "__main__":
    quizzes = get_additional_quizzes()
    print(f"Loaded {len(quizzes)} quiz modules.")
