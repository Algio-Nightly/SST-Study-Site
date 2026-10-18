"""
Lecture 10 Quiz: Transport Layer: TCP, UDP & Sockets
20 Advanced Multi-Correct MCQs (5 options each, 2 to 5 correct answers)
"""

QUIZ_L10 = {
    "topicId": "lecture-10",
    "lectureNumber": 10,
    "title": "TCP, UDP & Socket Programming Master Quiz",
    "description": "20 rigorous multi-correct questions covering transport demultiplexing, TCP header bitfields, 11-state FSM, TIME_WAIT & 2MSL, SYN cookies, sliding window flow control, AIMD congestion control, BDP calculations, BBR, and socket programming.",
    "estimatedMinutes": 35,
    "questions": [
        {
            "id": "l10-q01",
            "type": "multi_choice",
            "question": "Which of the following statements correctly describe how the operating system kernel demultiplexes incoming transport-layer packets to application socket descriptors?",
            "options": [
                {"id": "A", "text": "A TCP connection is uniquely demultiplexed using a 4-tuple: `(Source IP, Source Port, Destination IP, Destination Port)`."},
                {"id": "B", "text": "A connectionless UDP socket is demultiplexed primarily based on a 2-tuple: `(Destination IP, Destination Port)`."},
                {"id": "C", "text": "A server daemon listening on `0.0.0.0:8080` accepts TCP connections on all local network interfaces (including loopback `127.0.0.1` and Ethernet `eth0`)."},
                {"id": "D", "text": "A server daemon listening on `127.0.0.1:8080` can receive TCP SYN packets arriving from an external client over the local area network if port forwarding is enabled on the client."},
                {"id": "E", "text": "Two distinct external clients connecting from different IP addresses can simultaneously establish TCP connections to the exact same server IP and port (`198.51.100.1:443`)."}
            ],
            "correctOptionIds": ["A", "B", "C", "E"],
            "explanation": "Statements A, B, C, and E are correct. A & B: TCP requires the full 4-tuple for stateful demuxing, while UDP typically routes based on destination socket address. C: `0.0.0.0` (INADDR_ANY) binds to all local interfaces. E: Different client source IPs create distinct 4-tuples, allowing millions of concurrent connections to the same server port. D is false: Sockets bound strictly to loopback (`127.0.0.1`) only accept packets routed through the loopback interface (`lo`); external frames addressed to other interfaces are immediately rejected or dropped.",
            "difficulty": "medium",
            "subtopic": "Socket Demultiplexing & Bind Addresses"
        },
        {
            "id": "l10-q02",
            "type": "multi_choice",
            "question": "In the standard 20-to-60 byte TCP header (RFC 793), which of the following statements regarding the header fields and bit representations are accurate?",
            "options": [
                {"id": "A", "text": "The `Data Offset` field is 4 bits wide and specifies the length of the TCP header in units of 32-bit (4-byte) words."},
                {"id": "B", "text": "The minimum legal value of the `Data Offset` field is 5 (representing a minimum header size of $5 \\times 4 = 20\\text{ bytes}$ without options)."},
                {"id": "C", "text": "The maximum legal value of the `Data Offset` field is 15, limiting the maximum possible TCP header size to $15 \\times 4 = 60\\text{ bytes}$."},
                {"id": "D", "text": "The TCP header contains a 16-bit `Checksum` field that covers only the TCP header and ignores the payload data to maximize throughput."},
                {"id": "E", "text": "The `Window Size` field is 16 bits wide and advertises the number of bytes the receiver is currently willing to accept (receive window `rwnd`)."}
            ],
            "correctOptionIds": ["A", "B", "C", "E"],
            "explanation": "Statements A, B, C, and E are correct. Data Offset is 4 bits ($0 - 15$) counting 32-bit words, dictating a range from $20\\text{ bytes}$ ($5 \\times 4$) up to $60\\text{ bytes}$ ($15 \\times 4$) (A, B, C). Window size is 16 bits advertising `rwnd` (E). D is false: Unlike IPv4's header-only checksum, the TCP checksum covers the pseudo-header, the entire TCP header, AND the payload data.",
            "difficulty": "hard",
            "subtopic": "TCP Header Binary Structure"
        },
        {
            "id": "l10-q03",
            "type": "multi_choice",
            "question": "Regarding TCP Sequence Numbers and Acknowledgment Numbers, which of the following rules are mathematically and operationally correct?",
            "options": [
                {"id": "A", "text": "TCP sequence numbers count bytes in the data stream, NOT individual packets or segments."},
                {"id": "B", "text": "The `SYN` and `FIN` control flags each logically consume exactly one sequence number in the stream sequence space."},
                {"id": "C", "text": "An acknowledgment number `Ack = K` confirms that the receiver has successfully received all contiguous stream bytes up to $K - 1$, and expects byte $K$ next (cumulative acknowledgment)."},
                {"id": "D", "text": "Pure `ACK` packets carrying zero data payload consume one sequence number in the stream sequence space."},
                {"id": "E", "text": "If a host sends a segment with `Seq = 1000` carrying a payload of 500 bytes, the next sequential data byte sent by this host will begin at `Seq = 1500`."}
            ],
            "correctOptionIds": ["A", "B", "C", "E"],
            "explanation": "Statements A, B, C, and E are correct. TCP is a byte-stream protocol where sequence numbers track byte offsets (A). SYN and FIN occupy one slot in the sequence space to guarantee their reliable delivery and acknowledgment (B). ACKs are cumulative, indicating the next expected byte (C). Next sequence number is $\\text{Seq} + \\text{Length} = 1000 + 500 = 1500$ (E). D is false: Pure ACKs carrying no payload or SYN/FIN consume zero sequence space; the sequence number does not advance.",
            "difficulty": "hard",
            "subtopic": "Sequence Numbers & Cumulative ACKs"
        },
        {
            "id": "l10-q04",
            "type": "multi_choice",
            "question": "During the TCP Three-Way Handshake, which of the following TCP options (RFC 793, RFC 7323, RFC 2018) can be legitimately negotiated in the SYN and SYN-ACK segments?",
            "options": [
                {"id": "A", "text": "Maximum Segment Size (MSS): Informs the remote peer of the largest payload (excluding IP/TCP headers) the sending host can receive without fragmentation."},
                {"id": "B", "text": "Window Scale (WSCALE): Defines a logarithmic left-shift multiplier ($0 - 14$) applied to the 16-bit Window field, allowing window sizes up to $1\\text{ GiB}$."},
                {"id": "C", "text": "Selective Acknowledgment Permitted (SACK-Permitted): Enables the receiver to report non-contiguous blocks of received data to avoid retransmitting already-received segments."},
                {"id": "D", "text": "TCP Timestamps (TSopt): Transmits a timestamp value (TSval) and timestamp echo reply (TSecr) to enable accurate RTT measurement and Protection Against Wrapped Sequences (PAWS)."},
                {"id": "E", "text": "Diffie-Hellman Key Exchange (DHKEY): Directly encrypts the TCP payload with AES-256 without requiring TLS."}
            ],
            "correctOptionIds": ["A", "B", "C", "D"],
            "explanation": "Statements A, B, C, and D are standard TCP handshake options defined in RFCs. MSS (A), Window Scaling (B), SACK-Permitted (C), and Timestamps (D) are all negotiated in SYN packets. E is false: Standard TCP does not contain a native Diffie-Hellman encryption option; encryption is handled by higher-layer TLS records (or experimental TCP-AO/tcpcrypt).",
            "difficulty": "hard",
            "subtopic": "TCP Options & Handshake Negotiation"
        },
        {
            "id": "l10-q05",
            "type": "multi_choice",
            "question": "In a TCP SYN Flood attack and its defense via Cryptographic SYN Cookies (RFC 4987), which of the following statements are correct?",
            "options": [
                {"id": "A", "text": "A SYN Flood exhausts the server's kernel memory by forcing it to allocate a Transmission Control Block (TCB) for each spoofed SYN in its half-open connection table (SYN Queue)."},
                {"id": "B", "text": "When SYN Cookies are activated, the server refuses to allocate any kernel memory or state table entry upon receiving a SYN packet."},
                {"id": "C", "text": "The server encodes a cryptographic hash of the 4-tuple, a timestamp counter, and an MSS index into the 32-bit Initial Sequence Number (ISN) of the SYN-ACK."},
                {"id": "D", "text": "When the legitimate client completes the handshake by sending an ACK with `Ack = ISN + 1`, the server recalculates the hash from `Ack - 1` and reconstructs the connection state only then."},
                {"id": "E", "text": "SYN Cookies eliminate the need for the final ACK in the TCP three-way handshake."}
            ],
            "correctOptionIds": ["A", "B", "C", "D"],
            "explanation": "Statements A, B, C, and D accurately capture SYN Flood attacks and SYN Cookie defense. Attackers exploit half-open TCB state allocation (A). SYN Cookies eliminate server state upon SYN receipt (B). State is encoded inside the 32-bit ISN using cryptographic hashes and timestamps (C). The connection is verified and allocated only when the client returns ACK containing `ISN + 1` (D). E is false: The client's final ACK is essential because it contains the cookie to be verified.",
            "difficulty": "hard",
            "subtopic": "SYN Flood & Cryptographic SYN Cookies"
        },
        {
            "id": "l10-q06",
            "type": "multi_choice",
            "question": "Trace the TCP 11-State Finite State Machine (FSM). Which of the following transitions and state assignments are correct?",
            "options": [
                {"id": "A", "text": "A client sending a SYN packet transitions from `CLOSED` to `SYN_SENT`."},
                {"id": "B", "text": "A server receiving a SYN while in `LISTEN` transmits a SYN-ACK and transitions to `SYN_RCVD`."},
                {"id": "C", "text": "The side that receives a FIN packet while in `ESTABLISHED` automatically transmits an ACK and transitions to `CLOSE_WAIT`."},
                {"id": "D", "text": "The active closer transitions from `FIN_WAIT_1` to `FIN_WAIT_2` upon receiving an ACK for its FIN."},
                {"id": "E", "text": "A socket transitions directly from `LISTEN` to `TIME_WAIT` when an incoming connection is rejected."}
            ],
            "correctOptionIds": ["A", "B", "C", "D"],
            "explanation": "Statements A, B, C, and D are classical TCP FSM transitions specified in RFC 793. CLOSED $\\rightarrow$ SYN_SENT on active open (A). LISTEN $\\rightarrow$ SYN_RCVD on receiving SYN (B). ESTABLISHED $\\rightarrow$ CLOSE_WAIT on passive close upon receiving FIN (C). FIN_WAIT_1 $\\rightarrow$ FIN_WAIT_2 upon receiving ACK for FIN (D). E is false: Rejection sends a RST; a listening socket never transitions to TIME_WAIT.",
            "difficulty": "hard",
            "subtopic": "TCP Finite State Machine Transitions"
        },
        {
            "id": "l10-q07",
            "type": "multi_choice",
            "question": "Why does the active closer of a TCP connection enter the `TIME_WAIT` state, and why is its duration standardized to $2\\text{MSL}$ (Maximum Segment Lifetime, typically 60 seconds)?",
            "options": [
                {"id": "A", "text": "To ensure the final ACK sent by the active closer reaches the passive closer; if the ACK is lost, the passive closer retransmits its FIN, which the host in TIME_WAIT can still acknowledge."},
                {"id": "B", "text": "To allow any duplicate segments wandering through the Internet from the old connection to expire and dissipate before a new socket can reuse the identical 4-tuple."},
                {"id": "C", "text": "MSL represents the maximum time a packet can survive in the network (traditionally estimated as 30 or 120 seconds); waiting $2\\text{MSL}$ covers the round trip of a delayed FIN and its retransmitted ACK."},
                {"id": "D", "text": "To allow the server CPU to cool down following intensive data processing."},
                {"id": "E", "text": "In Linux, enabling `net.ipv4.tcp_tw_reuse = 1` allows outgoing client connections to safely reuse sockets in `TIME_WAIT` if TCP timestamps confirm the new packet is fresh."}
            ],
            "correctOptionIds": ["A", "B", "C", "E"],
            "explanation": "Statements A, B, C, and E are correct. TIME_WAIT ensures reliable termination: acknowledging retransmitted FINs if the final ACK is lost (A), and draining old wandering packets to avoid corrupting new connection incarnations (B & C). Linux allows timestamp-verified reuse via `tcp_tw_reuse` (E). D is humorous and false.",
            "difficulty": "medium",
            "subtopic": "TIME_WAIT State & 2MSL Mechanics"
        },
        {
            "id": "l10-q08",
            "type": "multi_choice",
            "question": "A production backend server exhibits thousands of connections stuck in `CLOSE_WAIT` and begins crashing with `Too many open files`. An SRE investigates. Which of the following statements are correct?",
            "options": [
                {"id": "A", "text": "The connections entered `CLOSE_WAIT` because the remote client actively initiated a connection close by sending a FIN, and the local kernel acknowledged it."},
                {"id": "B", "text": "A socket remains in `CLOSE_WAIT` until the local application process explicitly calls `close(sockfd)` on the socket descriptor."},
                {"id": "C", "text": "Massive accumulation of `CLOSE_WAIT` connections represents an application bug (e.g., leaked connection handles or missing `finally` blocks) rather than a network error."},
                {"id": "D", "text": "This issue can be permanently resolved by setting `net.ipv4.tcp_tw_reuse = 1` in `/etc/sysctl.conf`."},
                {"id": "E", "text": "Each unclosed socket in `CLOSE_WAIT` retains an open file descriptor in the operating system, eventually exhausting the process file descriptor limit (`RLIMIT_NOFILE`)."}
            ],
            "correctOptionIds": ["A", "B", "C", "E"],
            "explanation": "Statements A, B, C, and E are correct. `CLOSE_WAIT` indicates the kernel is waiting on the *local* program to invoke `close()` after the remote side closed (A & B). It is an application leak defect that burns file descriptors until exhaustion (C & E). D is false: `tcp_tw_reuse` applies strictly to `TIME_WAIT` on active closers; kernel sysctls cannot force an application to release leaked `CLOSE_WAIT` descriptors.",
            "difficulty": "hard",
            "subtopic": "CLOSE_WAIT SRE Post-Mortem"
        },
        {
            "id": "l10-q09",
            "type": "multi_choice",
            "question": "Which of the following principles govern TCP Sliding Window Flow Control?",
            "options": [
                {"id": "A", "text": "Flow control protects the receiving application from being overwhelmed by a sender transmitting data faster than the receiver can process it."},
                {"id": "B", "text": "The receiver advertises its available buffer space via the `rwnd` (Receive Window) field in every TCP header."},
                {"id": "C", "text": "The sender is constrained to transmit no more than $\\min(\\text{cwnd}, \\text{rwnd})$ unacknowledged bytes in flight."},
                {"id": "D", "text": "Flow control automatically measures network router buffer queues and throttles transmission based on drop rates in intermediate switches."},
                {"id": "E", "text": "When an application reads bytes from its socket receive buffer using `read()` or `recv()`, the available `rwnd` increases, which the kernel announces via a Window Update."}
            ],
            "correctOptionIds": ["A", "B", "C", "E"],
            "explanation": "Statements A, B, C, and E are correct. Flow control is an end-to-end receiver-protection mechanism (A). The receiver advertises `rwnd` (B), sender limits flight size to $\\min(\\text{cwnd}, \\text{rwnd})$ (C), and draining the buffer via `read()` opens the window (E). D is false: Throttling based on intermediate network congestion is the domain of Congestion Control (`cwnd`), not Flow Control (`rwnd`).",
            "difficulty": "medium",
            "subtopic": "Sliding Window Flow Control"
        },
        {
            "id": "l10-q10",
            "type": "multi_choice",
            "question": "What happens during a TCP Zero Window condition, and how does TCP prevent deadlock?",
            "options": [
                {"id": "A", "text": "A Zero Window occurs when the receiver's application buffer is completely full, causing the receiver to advertise `rwnd = 0`."},
                {"id": "B", "text": "Upon receiving `rwnd = 0`, the sender must immediately cease transmitting new data segments."},
                {"id": "C", "text": "To prevent deadlock if the subsequent Window Update packet is lost, the sender arms a Persist Timer."},
                {"id": "D", "text": "When the Persist Timer expires, the sender transmits a Zero Window Probe (ZWP) containing a 1-byte payload to force the receiver to reply with its current `rwnd`."},
                {"id": "E", "text": "A Zero Window condition automatically aborts the TCP connection and resets the socket state to `CLOSED`."}
            ],
            "correctOptionIds": ["A", "B", "C", "D"],
            "explanation": "Statements A, B, C, and D are correct. A full buffer advertises `rwnd = 0` (A), halting data transmission (B). If the receiver later frees space and sends an ACK advertising `rwnd > 0`, but that ACK is lost in transit, both sides would wait forever (deadlock). The Persist Timer solves this by sending periodic 1-byte Zero Window Probes (C & D). E is false: A Zero Window pauses transmission gracefully; it does not abort the connection.",
            "difficulty": "hard",
            "subtopic": "Zero Window & Persist Timer"
        },
        {
            "id": "l10-q11",
            "type": "multi_choice",
            "question": "Which of the following statements regarding Silly Window Syndrome (SWS) and its remedies are correct?",
            "options": [
                {"id": "A", "text": "Silly Window Syndrome occurs when data is exchanged in tiny segments (e.g., 1 byte of payload inside 40 bytes of IP/TCP headers), drastically degrading protocol efficiency."},
                {"id": "B", "text": "Receiver-side SWS avoidance (Clark's Solution) dictates that the receiver must not advertise a small window update until buffer space is at least $\\min(\\text{MSS}, \\text{Buffer Size} / 2)$."},
                {"id": "C", "text": "Sender-side SWS avoidance is implemented via Nagle's Algorithm: If there is unacknowledged data in flight, buffer small outgoing chunks until a full MSS accumulates or all previous data is acknowledged."},
                {"id": "D", "text": "Disabling Nagle's Algorithm using the `TCP_NODELAY` socket option is critical for low-latency interactive applications like multiplayer online gaming or SSH keystrokes."},
                {"id": "E", "text": "Nagle's Algorithm and TCP Delayed ACKs can interact destructively, inducing an artificial 40ms to 200ms latency penalty on small request-response patterns."}
            ],
            "correctOptionIds": ["A", "B", "C", "D", "E"],
            "explanation": "ALL FIVE statements (A, B, C, D, and E) are correct! SWS generates massive header overhead for tiny payloads (A). Clark's solution prevents receivers from advertising microscopic window updates (B). Nagle's algorithm buffers small outgoing writes at the sender (C). Low-latency systems disable Nagle via `TCP_NODELAY` (D). Nagle waiting for an ACK while the receiver delays its ACK (Delayed ACK algorithm) causes the famous Nagle-Delayed ACK deadlock inducing ~40-200ms delays (E).",
            "difficulty": "hard",
            "subtopic": "Silly Window Syndrome & Nagle Algorithm"
        },
        {
            "id": "l10-q12",
            "type": "multi_choice",
            "question": "Which of the following characteristics accurately define Additive Increase, Multiplicative Decrease (AIMD) in classical TCP Congestion Control?",
            "options": [
                {"id": "A", "text": "During Congestion Avoidance, if all transmitted segments in a window are successfully acknowledged, `cwnd` increases by approximately 1 MSS per Round-Trip Time (RTT)."},
                {"id": "B", "text": "Mathematically, the per-ACK additive update rule is: $\\text{cwnd} \\leftarrow \\text{cwnd} + \\frac{\\text{MSS} \\times \\text{MSS}}{\\text{cwnd}}$."},
                {"id": "C", "text": "Upon detecting packet loss via a retransmission timeout (RTO), `cwnd` is cut multiplicatively in half while `ssthresh` drops to 1."},
                {"id": "D", "text": "Upon detecting packet loss, the multiplicative decrease cuts the sending rate drastically, ensuring rapid network queue drain and preventing congestion collapse."},
                {"id": "E", "text": "AIMD is mathematically proven to converge distributed competing flows to both efficiency and Pareto fairness across a shared bottleneck link."}
            ],
            "correctOptionIds": ["A", "B", "D", "E"],
            "explanation": "Statements A, B, D, and E are correct. In congestion avoidance, AIMD increases `cwnd` linearly by 1 MSS per RTT (A), which on an ACK-by-ACK basis is $\\Delta = \\frac{\\text{MSS}^2}{\\text{cwnd}}$ (B). Multiplicative decrease cuts sending rate sharply upon loss (D). Chiu & Jain (1989) proved AIMD converges competing flows to fairness and efficiency (E). C is false: On an RTO, `ssthresh` is set to $\\text{cwnd} / 2$, but `cwnd` collapses to 1 MSS (not cut in half).",
            "difficulty": "hard",
            "subtopic": "AIMD Congestion Control Dynamics"
        },
        {
            "id": "l10-q13",
            "type": "multi_choice",
            "question": "Which of the following statements regarding TCP Slow Start are correct?",
            "options": [
                {"id": "A", "text": "Despite its name, Slow Start increases the Congestion Window (`cwnd`) exponentially with respect to time, doubling `cwnd` every Round-Trip Time (RTT)."},
                {"id": "B", "text": "For every incoming acknowledgment (ACK) that confirms new data, `cwnd` increases by 1 MSS: $\\text{cwnd} \\leftarrow \\text{cwnd} + \\text{MSS}$."},
                {"id": "C", "text": "Slow Start begins with an initial window (`IW`), which in modern Linux kernels defaults to 10 MSS (RFC 6928)."},
                {"id": "D", "text": "The connection terminates Slow Start and transitions to Congestion Avoidance when `cwnd >= ssthresh`."},
                {"id": "E", "text": "Slow Start continues growing exponentially forever until the physical fiber optic cable melts."}
            ],
            "correctOptionIds": ["A", "B", "C", "D"],
            "explanation": "Statements A, B, C, and D are correct. Slow start doubles `cwnd` every RTT by adding 1 MSS per ACK received (A & B). Linux modern IW is 10 segments (C). When `cwnd` reaches the slow start threshold (`ssthresh`), it shifts to linear congestion avoidance (D). E is humorous and false; slow start halts at `ssthresh` or upon packet loss.",
            "difficulty": "medium",
            "subtopic": "TCP Slow Start Mechanics"
        },
        {
            "id": "l10-q14",
            "type": "multi_choice",
            "question": "How do Fast Retransmit and Fast Recovery (RFC 5681) optimize TCP performance compared to timeout-based retransmission?",
            "options": [
                {"id": "A", "text": "When a single segment is lost in a sequence, out-of-order segments arriving at the receiver generate immediate Duplicate ACKs."},
                {"id": "B", "text": "Upon receiving exactly 3 Duplicate ACKs (4 identical ACKs total), the sender concludes a packet was lost rather than merely reordered."},
                {"id": "C", "text": "Fast Retransmit sends the missing segment immediately without waiting for the Retransmission Timer (RTO) to expire."},
                {"id": "D", "text": "Fast Recovery prevents collapsing `cwnd` to 1 MSS; it sets $\\text{ssthresh} = \\text{cwnd}/2$, inflates `cwnd` for subsequent dup ACKs, and resumes Congestion Avoidance once the loss is cleared."},
                {"id": "E", "text": "Fast Retransmit switches the connection to UDP for 30 seconds."}
            ],
            "correctOptionIds": ["A", "B", "C", "D"],
            "explanation": "Statements A, B, C, and D are correct. Out-of-order packets trigger duplicate ACKs (A). 3 duplicate ACKs trigger Fast Retransmit (B), retransmitting without waiting for RTO (C). Fast Recovery maintains pipeline throughput by setting `ssthresh` and halving window rather than collapsing to 1 MSS (D). E is absurd.",
            "difficulty": "medium",
            "subtopic": "Fast Retransmit & Fast Recovery"
        },
        {
            "id": "l10-q15",
            "type": "multi_choice",
            "question": "A 10 Gbps transatlantic link has a Round-Trip Time (RTT) of $80\\text{ ms}$. Which of the following calculations and observations regarding the Bandwidth-Delay Product (BDP) are correct?",
            "options": [
                {"id": "A", "text": "The Bandwidth-Delay Product is $\\text{BDP} = 10\\text{ Gbps} \\times 0.080\\text{ s} = 800\\text{ Megabits} = 100\\text{ Megabytes}$ ($100\\text{ MB}$)."},
                {"id": "B", "text": "Without the TCP Window Scale option, the maximum window size allowed by the 16-bit header field is $65,535\\text{ bytes}$ ($\\approx 64\\text{ KB}$)."},
                {"id": "C", "text": "Without Window Scaling, the maximum achievable throughput on this 10 Gbps link is approximately $\\frac{65,535\\text{ bytes} \\times 8}{0.080\\text{ s}} \\approx 6.55\\text{ Mbps}$ (less than $0.1\\%$ of link capacity!)."},
                {"id": "D", "text": "To fully saturate this 10 Gbps pipe, the sender and receiver TCP socket buffers must be tuned to at least $100\\text{ MB}$."},
                {"id": "E", "text": "The Window Scale option can never scale the window beyond 64 KB because IPv4 routers drop scaled packets."}
            ],
            "correctOptionIds": ["A", "B", "C", "D"],
            "explanation": "Statements A, B, C, and D are mathematically exact. $\\text{BDP} = 10\\times 10^9 \\times 0.080 = 800\\times 10^6\\text{ bits} = 100\\text{ MB}$ (A). Standard 16-bit window caps at $65,535\\text{ bytes}$ (B). Maximum unscaled throughput is $\\frac{65535 \\times 8}{0.08} = 6.55\\text{ Mbps}$ (C). Sockets must scale to BDP ($100\\text{ MB}$) to saturate pipe (D). E is false: RFC 7323 Window Scale shifts up to 14 bits, enabling windows up to $1\\text{ GiB}$.",
            "difficulty": "hard",
            "subtopic": "BDP & Window Scale Mathematics"
        },
        {
            "id": "l10-q16",
            "type": "multi_choice",
            "question": "How does Google's BBR (Bottleneck Bandwidth and RTT) congestion control fundamentally differ from classical loss-based algorithms like Reno and Cubic?",
            "options": [
                {"id": "A", "text": "Loss-based algorithms (Reno, Cubic) treat packet loss as the primary indicator of congestion, driving buffers to overflow and creating severe bufferbloat."},
                {"id": "B", "text": "BBR models the physical network by independently measuring two parameters: Maximum Bottleneck Bandwidth ($BtlBw$) and Minimum Round-Trip Propagation Delay ($RTprop$)."},
                {"id": "C", "text": "BBR operates around the Kleinrock optimal operating point, keeping the inflight data equal to exactly $1\\text{ BDP}$ to maximize throughput while minimizing queuing delay."},
                {"id": "D", "text": "On lossy wireless or transcontinental networks with non-congestion random packet loss (e.g., $1\\%$ RF loss), Cubic's throughput collapses dramatically while BBR maintains high throughput."},
                {"id": "E", "text": "BBR requires specialized hardware upgrades on every intermediate router along the path to function."}
            ],
            "correctOptionIds": ["A", "B", "C", "D"],
            "explanation": "Statements A, B, C, and D accurately describe BBR. Loss-based congestion control fills buffers until drops occur, causing bufferbloat (A). BBR models physical $BtlBw$ and $RTprop$ (B) and aims for Kleinrock's optimal operating point (C). Because BBR does not interpret shallow packet loss as congestion, it dramatically outperforms Cubic on lossy wireless/long-haul links (D). E is false: BBR is purely an end-host sender algorithm requiring zero changes on intermediate routers.",
            "difficulty": "hard",
            "subtopic": "BBR vs Loss-Based Congestion Control"
        },
        {
            "id": "l10-q17",
            "type": "multi_choice",
            "question": "Which of the following principles govern Jacobson's algorithm for calculating TCP's Retransmission Timeout (RTO)?",
            "options": [
                {"id": "A", "text": "RTO cannot be a static constant; it must adapt dynamically to changing network latency by tracking Smoothed Round-Trip Time (SRTT) and Round-Trip Time Variation (RTTVAR)."},
                {"id": "B", "text": "The classic Jacobson/Karn formula computes: $\\text{RTO} = \\text{SRTT} + 4 \\times \\text{RTTVAR}$."},
                {"id": "C", "text": "When a timeout occurs, Karn's Algorithm dictates that the host must back off the timer exponentially (doubling RTO: $\\text{RTO} \\leftarrow 2 \\times \\text{RTO}$) for subsequent retries."},
                {"id": "D", "text": "Karn's Algorithm stipulates that RTT measurements must NOT be sampled from retransmitted segments because of ambiguity over which transmission generated the ACK."},
                {"id": "E", "text": "In Linux, the RTO timer is fixed at exactly $10\\text{ milliseconds}$ under all conditions."}
            ],
            "correctOptionIds": ["A", "B", "C", "D"],
            "explanation": "Statements A, B, C, and D are correct. Jacobson's algorithm computes $\\text{RTO} = \\text{SRTT} + 4 \\times \\text{RTTVAR}$ (A & B). Karn's algorithm enforces exponential backoff on timeouts (C) and forbids sampling RTT from retransmitted segments to prevent acknowledgment ambiguity (D). E is false: Linux default initial RTO is 1000ms (1s), with dynamic adaptation bounded between `TCP_RTO_MIN` (200ms) and `TCP_RTO_MAX` (120s).",
            "difficulty": "hard",
            "subtopic": "RTO Calculation & Karn's Algorithm"
        },
        {
            "id": "l10-q18",
            "type": "multi_choice",
            "question": "Which of the following statements regarding the User Datagram Protocol (UDP - RFC 768) are technically correct?",
            "options": [
                {"id": "A", "text": "UDP has a fixed 8-byte header containing only four fields: Source Port, Destination Port, Length, and Checksum."},
                {"id": "B", "text": "UDP preserves message boundaries; each `sendto()` call by an application corresponds to exactly one discrete datagram received by `recvfrom()`."},
                {"id": "C", "text": "In IPv4, computing the UDP Checksum is technically optional (can be set to 0), but in IPv6, the UDP checksum is strictly mandatory."},
                {"id": "D", "text": "The UDP checksum calculation incorporates an IP 'pseudo-header' containing the Source IP, Destination IP, Protocol (17), and UDP Length to catch misrouted packets."},
                {"id": "E", "text": "UDP guarantees in-order delivery of packets using 8-bit segment identifiers."}
            ],
            "correctOptionIds": ["A", "B", "C", "D"],
            "explanation": "Statements A, B, C, and D are correct. UDP header is 8 bytes (A). UDP preserves datagram boundaries, unlike TCP's unstructured byte stream (B). IPv4 UDP checksum is optional ($0$ = disabled), but IPv6 mandates it (C). The checksum covers an IP pseudo-header (D). E is false: UDP provides zero ordering, reliability, or sequence numbers.",
            "difficulty": "medium",
            "subtopic": "UDP Protocol Characteristics"
        },
        {
            "id": "l10-q19",
            "type": "multi_choice",
            "question": "When inspecting sockets on a Linux system using `ss -tulpn` and `ss -ti`, which of the following interpretations are correct?",
            "options": [
                {"id": "A", "text": "For a socket in the `LISTEN` state, `Send-Q` represents the maximum backlog limit of the accept queue (set by `listen(fd, backlog)` and `net.core.somaxconn`)."},
                {"id": "B", "text": "For a socket in the `LISTEN` state, `Recv-Q` represents the number of established connections currently waiting in the accept queue for the application to invoke `accept()`."},
                {"id": "C", "text": "For a socket in the `ESTABLISHED` state, `Recv-Q` represents data bytes received from the network and buffered in the kernel that have NOT yet been read by the application."},
                {"id": "D", "text": "For a socket in the `ESTABLISHED` state, `Send-Q` represents data bytes sent by the application but NOT yet acknowledged by the remote peer."},
                {"id": "E", "text": "`ss` executes by locking `/proc/net/tcp` in memory, making it much slower than legacy `netstat`."}
            ],
            "correctOptionIds": ["A", "B", "C", "D"],
            "explanation": "Statements A, B, C, and D are correct. `Recv-Q` and `Send-Q` have dual meanings: In LISTEN, they represent the current accept queue depth and maximum accept queue limit (A & B). In ESTABLISHED, they represent unread received bytes and unacknowledged outbound bytes (C & D). E is false: `ss` uses Netlink kernel sockets (`NETLINK_INET_DIAG`) for $O(1)$ zero-copy dumps, whereas legacy `netstat` parsed `/proc/net/tcp`.",
            "difficulty": "hard",
            "subtopic": "Kernel Socket Metrics & ss Diagnostics"
        },
        {
            "id": "l10-q20",
            "type": "multi_choice",
            "question": "Which of the following statements regarding network socket programming and POSIX system calls are technically accurate?",
            "options": [
                {"id": "A", "text": "The `listen(sockfd, backlog)` system call puts a stream socket into passive listening mode and defines the size of the pending connection backlog queue."},
                {"id": "B", "text": "The `accept(sockfd, ...)` call extracts the first connection on the pending queue, creates a brand-new socket descriptor for that specific connection, and returns it."},
                {"id": "C", "text": "Setting `SO_REUSEADDR` allows a server daemon to bind to a local port even if existing connections on that port are currently lingering in the `TIME_WAIT` state."},
                {"id": "D", "text": "Setting `SO_REUSEPORT` allows multiple independent processes or threads on the same host to bind to the exact same IP and port, with the kernel automatically load balancing incoming connections."},
                {"id": "E", "text": "The `epoll` system call on Linux provides $O(1)$ I/O event multiplexing scalable to hundreds of thousands of concurrent file descriptors, overcoming the $O(N)$ scanning bottlenecks of `select()`."}
            ],
            "correctOptionIds": ["A", "B", "C", "D", "E"],
            "explanation": "ALL FIVE statements (A, B, C, D, and E) are technically correct! `listen()` sets backlog (A). `accept()` returns a new active descriptor per client (B). `SO_REUSEADDR` overcomes TIME_WAIT bind failure (C). `SO_REUSEPORT` enables multi-process kernel port sharding (D). `epoll` (epoll_create/epoll_ctl/epoll_wait) provides $O(1)$ event notifications, powering high-concurrency systems like NGINX and Node.js (E).",
            "difficulty": "hard",
            "subtopic": "POSIX Socket Programming & High Concurrency"
        }
    ]
}
