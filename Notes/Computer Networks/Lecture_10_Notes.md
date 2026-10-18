# Lecture 10: TCP, UDP and Socket Programming
## Student Notes — SST Computer Networks (Term 5)

---

## 🎯 Learning Objectives

By the end of this lecture and lab module, you should be able to:
- Differentiate between **host-to-host delivery** (Network Layer / IP) and **process-to-process multiplexing** (Transport Layer) using 16-bit ports and 4-tuples.
- Dissect the **20–60 byte TCP header** down to individual bit fields: Sequence/Ack numbers, Data Offset, Flags (SYN, ACK, FIN, RST, PSH, URG, ECE, CWR), Window Size, Checksum, and TCP Options (MSS, Window Scale, SACK, Timestamps).
- Trace the complete **TCP Finite State Machine (FSM)** across all 11 states, including the 3-Way Handshake, 4-Way Teardown, and the exact mathematical rationale for **`TIME_WAIT` (2MSL)**.
- Analyze security exploits including **SYN Flood Attacks** and explain the cryptographic defense of **SYN Cookies (RFC 4987)**.
- Formulate the fundamental distinction between **Flow Control** (Receiver buffer protection via Sliding Window / `rwnd`) and **Congestion Control** (Network capacity protection via `cwnd`).
- Trace the four classical congestion control algorithms (RFC 5681): **Slow Start**, **Congestion Avoidance (AIMD)**, **Fast Retransmit (3 duplicate ACKs)**, and **Fast Recovery**, contrasting TCP Tahoe, Reno, CUBIC, and Google BBR.
- Calculate the **Bandwidth-Delay Product (BDP)** and explain why the TCP Window Scale option is required for Gigabit and 100G links.
- Write production-grade, concurrent client-server network applications in **Python** using BSD Sockets, understanding blocking vs. non-blocking I/O and `epoll`.

---

## 1. Transport Layer Fundamentals: The Multiplexing Abstraction

The Internet Protocol (Layer 3) provides **best-effort host-to-host packet delivery**. It delivers a datagram from a source IP (e.g., your laptop) to a destination IP (e.g., an AWS server). However, modern computers run hundreds of concurrent network programs simultaneously: Spotify is streaming music, Zoom is transmitting video, Chrome has 20 tabs open, and an SSH daemon is listening for administrative connections.

The **Transport Layer (Layer 4)** bridges the gap between host-to-host packet routing and **process-to-process communication**:

```
[ Process: Chrome ]    [ Process: Zoom ]    [ Process: SSH ]
      :54210                 :58921               :22
         │                      │                  │
         └──────────────┬───────┴──────────────────┘
                        ▼
            Transport Layer Multiplexing (TCP / UDP)
                        ▼
             Network Layer (IP: 192.168.1.50)
```

### Demultiplexing Keys: 2-Tuple vs. 4-Tuple
When an IP datagram arrives at a host, the operating system kernel must route the payload to the correct socket buffer:
- **UDP Demultiplexing (2-Tuple)**: Routed strictly using:
  $$\text{Key}_{\text{UDP}} = (\text{Destination IP}, \text{Destination Port})$$
  Two independent clients sending to UDP port 53 on the same server arrive in the exact same socket queue.
- **TCP Demultiplexing (4-Tuple)**: Routed using the full 4-tuple:
  $$\text{Key}_{\text{TCP}} = (\text{Source IP}, \text{Source Port}, \text{Destination IP}, \text{Destination Port})$$
  This allows a single web server listening on port 443 to maintain 100,000 distinct, isolated connection sockets simultaneously.

### Port Ranges (RFC 6335)
Ports are 16-bit unsigned integers ($0 \text{ to } 65,535$):
- **Well-Known Ports ($0 - 1023$)**: Assigned by IANA; requires root/administrator privileges to bind (e.g., SSH: 22, HTTP: 80, HTTPS: 443, DNS: 53).
- **Registered Ports ($1024 - 49151$)**: Dedicated to specific user processes and databases (e.g., MySQL: 3306, PostgreSQL: 5432, Redis: 6379, Kafka: 9092).
- **Dynamic / Ephemeral Ports ($49152 - 65535$)**: Allocated automatically by the client OS kernel for outbound client connections.

---

## 2. UDP: Lightweight, Connectionless Datagrams

The **User Datagram Protocol (UDP - RFC 768)** is a minimalist transport wrapper over IP. It provides port multiplexing and error detection, but adds zero reliability, zero ordering, and zero rate control.

### The 8-Byte UDP Header
```
 0                   1                   2                   3
 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
|          Source Port          |       Destination Port        |
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
|            Length             |           Checksum            |
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
|                             Data                              |
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
```

1. **Source Port (16 bits)**: Port of the sending process (optional; set to zero if no reply expected).
2. **Destination Port (16 bits)**: Target service port.
3. **Length (16 bits)**: Total length of UDP header + payload in bytes (minimum = 8 bytes).
4. **Checksum (16 bits)**: 16-bit one's complement sum over a **pseudo-header** (IP addresses, protocol 17, UDP length) plus the UDP packet. Protects against corrupted bits in transit.

### Why Would Anyone Choose UDP over TCP?
1. **Zero Connection Latency (0-RTT)**: Immediate transmission with zero handshake round trips.
2. **No Head-of-Line Blocking**: Packets are delivered independently. Dropping packet #1 does not halt processing of packet #2.
3. **No Congestion Control Bottlenecks**: UDP transmits at whatever speed the application requests, vital for real-time systems where late data is completely useless (e.g., VoIP voice packets or multiplayer FPS player coordinates).
4. **Broadcast & Multicast Capability**: TCP is strictly point-to-point (unicast); UDP can broadcast to `255.255.255.255` (DHCP Discover).
5. **Modern Substrate for Custom Protocols**: HTTP/3, QUIC, and WireGuard use UDP as a raw userspace multiplexing transport.

---

## 3. TCP: The Transmission Control Protocol

TCP (RFC 793, RFC 9293) transforms an unreliable, packet-dropping, out-of-order network into a **reliable, in-order, error-checked, flow-controlled, full-duplex byte stream**.

### The TCP Header (20 to 60 Bytes)

```
 0                   1                   2                   3
 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
|          Source Port          |       Destination Port        |
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
|                        Sequence Number                        |
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
|                    Acknowledgment Number                      |
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
|  Data |           |U|A|P|R|S|F|                               |
| Offset| Reserved  |R|C|S|S|Y|I|            Window             |
|       |           |G|K|H|T|N|N|                               |
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
|           Checksum            |         Urgent Pointer        |
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
|                    Options                    |    Padding    |
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
|                             data                              |
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
```

### Dissection of Core Header Fields:
1. **Sequence Number (32 bits)**:
   - TCP tracks **bytes, not packets**. The sequence number represents the byte stream index of the first data byte in this segment.
   - Initial Sequence Numbers (ISNs) are randomized to prevent session hijacking and cross-connection packet crosstalk.
2. **Acknowledgment Number (32 bits)**:
   - Valid only when the `ACK` flag is set.
   - **Cumulative Acknowledgment**: Indicates the next expected byte ($N$). It explicitly confirms receipt of all bytes up to $N - 1$.
3. **Data Offset (4 bits)**:
   - Specifies header length in 32-bit (4-byte) words. Minimum value is 5 ($5 \times 4 = 20$ bytes); maximum is 15 ($15 \times 4 = 60$ bytes).
4. **Control Flags (9 bits)**:
   - **SYN (Synchronize)**: Initiates connection establishment; synchronizes ISNs. Consumes 1 sequence number.
   - **ACK (Acknowledgment)**: Signifies that the Acknowledgment Number field is valid. Set on every packet after initial SYN.
   - **FIN (Finish)**: Sender has completed sending data; initiates graceful connection shutdown. Consumes 1 sequence number.
   - **RST (Reset)**: Abruptly tears down a connection (e.g. port closed, firewall rejection, kernel crash).
   - **PSH (Push)**: Informs receiver kernel to immediately push buffered data to application space without waiting for full buffer.
   - **URG (Urgent)**: Urgent pointer field is valid (rarely used in modern systems).
   - **ECE & CWR**: Explicit Congestion Notification flags (RFC 3168).
5. **Window Size (16 bits)**:
   - The advertised receive window (`rwnd`). Tells sender how many bytes the receiver can accept without overflowing its buffer.
6. **Checksum (16 bits)**:
   - Mandatory in TCP. Calculated over pseudo-header, TCP header, and payload.

---

## 4. TCP Connection Lifecycle: The 11-State FSM

```
      CLIENT                                               SERVER
  (CLOSED)                                                (LISTEN)
     │                                                       │
     │ ────────── 1. SYN (seq=x) ──────────────────────────► │  (SYN_RCVD)
(SYN_SENT)                                                   │
     │                                                       │
     │ ◄───────── 2. SYN-ACK (seq=y, ack=x+1) ────────────── │
     │                                                       │
(ESTABLISHED)                                                │
     │ ────────── 3. ACK (seq=x+1, ack=y+1) ───────────────► │ (ESTABLISHED)
     │                                                       │
     ╔═══════════════════════════════════════════════════════╗
     ║               FULL DUPLEX DATA EXCHANGE               ║
     ╚═══════════════════════════════════════════════════════╝
     │                                                       │
     │ ────────── 1. FIN (seq=u) ──────────────────────────► │ (CLOSE_WAIT)
(FIN_WAIT_1)                                                 │
     │ ◄───────── 2. ACK (ack=u+1) ───────────────────────── │
(FIN_WAIT_2)                                                 │ (Server drains data)
     │                                                       │
     │ ◄───────── 3. FIN (seq=w, ack=u+1) ────────────────── │ (LAST_ACK)
     │                                                       │
     │ ────────── 4. ACK (seq=u+1, ack=w+1) ───────────────► │  (CLOSED)
(TIME_WAIT)                                                  │
     │ (Wait 2 * MSL)                                        │
  (CLOSED)                                                   ▼
```

### Why 2MSL in `TIME_WAIT`? (The Mathematical Rationale)
The **Maximum Segment Lifetime (MSL)** is the maximum time an IP packet can roam across the Internet before being dropped by router TTL hop limits (standardized at 30 to 120 seconds, typically 60 seconds in Linux).

The node that initiates the active close **must remain in `TIME_WAIT` for $2 \times \text{MSL}$ (~120s)** for two critical reasons:
1. **Graceful ACK Retransmission**: If Client's final `ACK` is dropped in transit, Server will retransmit its `FIN`. If Client closed immediately, it would respond with `RST`, causing the Server to abort with a connection error instead of clean closure.
2. **Old Duplicate Packet Evaporation**: It guarantees that all delayed, reordered packets roaming the internet from the old connection die off before a new socket can reuse the same 4-tuple `(IP_src, Port_src, IP_dst, Port_dst)`.

---

## 5. Security: SYN Flood Attacks & SYN Cookies

In a standard 3-way handshake, when a server receives a `SYN`, it allocates a Transmission Control Block (TCB) in kernel memory and places the half-open connection into a **SYN Backlog Queue**.

```
Attacker ─── SYN (Spoofed IP 1) ───► [ Server Allocates TCB ] ───► (Waiting for ACK...)
Attacker ─── SYN (Spoofed IP 2) ───► [ Server Allocates TCB ] ───► (Waiting for ACK...)
Attacker ─── SYN (Spoofed IP 3) ───► [ Server Allocates TCB ] ───► (Queue Saturated!)
Legitimate Client ─── SYN ──────────► [ Server Drops: Queue Full! ]
```

### The Solution: Cryptographic SYN Cookies (RFC 4987)
With SYN Cookies enabled (`sysctl -w net.ipv4.tcp_syncookies=1`), when the backlog queue saturates, the server **does not allocate any memory**:
1. It computes a cryptographic initial sequence number $y$:
   $$y = \text{HMAC}_{K}(\text{IP}_{src}, \text{Port}_{src}, \text{IP}_{dst}, \text{Port}_{dst}, t) + \text{MSS Index}$$
2. The server responds with `SYN-ACK` containing sequence $y$ and immediately deletes all state.
3. When the client sends the final `ACK` ($ack = y + 1$), the server subtracts 1 and verifies the HMAC against current time $t$. If valid, the connection buffer is allocated on the spot.

---

## 6. Flow Control vs. Congestion Control

Students frequently confuse these two distinct feedback mechanisms:

$$\mathbf{Flow\ Control}: \text{Protects the } \mathbf{receiver's\ buffer} \text{ from being overrun by a fast sender}.$$
$$\mathbf{Congestion\ Control}: \text{Protects the } \mathbf{intermediate\ network\ links} \text{ from bufferbloat and collapse}.$$

### Flow Control: The Sliding Window
- The receiver advertises its available buffer space in every ACK via the 16-bit **Window Size** field (`rwnd`).
- Sender transmission constraint:
  $$\text{LastByteSent} - \text{LastByteAcked} \le rwnd$$
- **Zero Window & Persist Timer**: If `rwnd = 0`, sender pauses transmission. However, to avoid deadlock if the receiver's window-update ACK drops, sender starts a **Persist Timer**. When it expires, sender transmits a 1-byte **Zero Window Probe**. The receiver is forced to respond with its current `rwnd`.

---

## 7. Congestion Control & Algorithms (RFC 5681)

The sender maintains a variable called the **Congestion Window (`cwnd`)**.
The actual permitted transmission volume is:
$$W = \min(cwnd, rwnd)$$

```
  Window Size
      ▲
      │                              Congestion Avoidance (AIMD)
      │                                   /  \
      │                    ssthresh ──── /    \ (Drop! cwnd / 2)
      │             Slow Start          /      \
      │                /               /        \
      │              /                /
      │            /                 /
      │          /
      └─────────┴───────────────────┴────────────────────────► Time (RTTs)
```

### The Four Phases of TCP Reno:
1. **Slow Start**:
   - Initial $cwnd = 10 \text{ MSS}$ (per RFC 6928).
   - For every ACK received: $cwnd \leftarrow cwnd + 1 \text{ MSS}$.
   - **Growth Rate**: Exponential (doubles every RTT: $1 \rightarrow 2 \rightarrow 4 \rightarrow 8 \dots$) until $cwnd \ge ssthresh$ (Slow Start Threshold).
2. **Congestion Avoidance (Additive Increase, Multiplicative Decrease - AIMD)**:
   - When $cwnd \ge ssthresh$, linear growth kicks in.
   - For each RTT: $cwnd \leftarrow cwnd + 1 \text{ MSS}$.
   - For each received ACK: $cwnd \leftarrow cwnd + \frac{MSS \times MSS}{cwnd}$.
3. **Fast Retransmit**:
   - Out-of-order packet arrival triggers duplicate ACKs.
   - Upon receiving **3 duplicate ACKs**, sender deduces a single packet was lost. It retransmits immediately without waiting for the RTO (Retransmission Timeout) timer to expire.
4. **Fast Recovery**:
   - $ssthresh \leftarrow \frac{cwnd}{2}$.
   - Sets $cwnd \leftarrow ssthresh + 3 \text{ MSS}$ and continues linear growth rather than collapsing back to 1 MSS.

### Bandwidth-Delay Product (BDP) & Window Scaling
The capacity of a network pipe is:
$$\text{BDP} = \text{Bandwidth (bits/sec)} \times \text{RTT (sec)}$$

**The Gigabit Bottleneck**:
In classical TCP, Window Size is a 16-bit integer (max $65,535 \text{ bytes} \approx 64 \text{ KB}$).
Consider a 1 Gbps link between US and India ($\text{RTT} \approx 200 \text{ ms}$):
$$\text{BDP} = 10^9 \text{ bps} \times 0.2 \text{ s} = 200,000,000 \text{ bits} = 25 \text{ MB}$$
With a 64 KB window limit:
$$\text{Max Throughput} = \frac{65,535 \times 8 \text{ bits}}{0.2 \text{ s}} = 2.62 \text{ Mbps}$$
You achieve **2.6 Mbps on a 1 Gbps link** (0.26% efficiency)!

**The Solution**: **TCP Window Scale Option (RFC 7323)**:
Negotiated in SYN packets, it defines a left-shift multiplier ($0 \text{ to } 14$ bits), expanding the maximum window size to $65,535 \times 2^{14} \approx \mathbf{1 \text{ Gigabyte}}$, allowing TCP to saturate multi-gigabit pipes.

---

## 8. Socket Programming in Python: Hands-On Production Guide

A **BSD Socket** is the standardized operating system interface between user application code and the kernel's network stack.

### Complete Concurrent Multi-Threaded TCP Echo Server
```python
#!/usr/bin/env python3
import socket
import threading
import sys

def client_handler(conn: socket.socket, addr: tuple):
    print(f"[+] Active session established with {addr[0]}:{addr[1]}")
    try:
        while True:
            # 1. Receive data from socket buffer
            data = conn.recv(4096)
            if not data:
                # recv returns empty bytes when client performs active close (FIN)
                print(f"[-] Client {addr[0]}:{addr[1]} disconnected gracefully.")
                break
            
            message = data.decode('utf-8', errors='replace').strip()
            print(f"[{addr[0]}] Received: {message}")
            
            # 2. Echo data back
            response = f"SERVER_ECHO: {message}\n"
            conn.sendall(response.encode('utf-8'))
    except ConnectionResetError:
        print(f"[!] Client {addr[0]} aborted connection with RST.")
    finally:
        conn.close()

def run_server(host: str = '0.0.0.0', port: int = 8080):
    # AF_INET = IPv4, SOCK_STREAM = TCP
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # SO_REUSEADDR prevents 'Address already in use' during TIME_WAIT restarts
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    
    server.bind((host, port))
    server.listen(128)  # Set kernel backlog queue size
    print(f"[*] TCP Listening on {host}:{port}...")

    try:
        while True:
            conn, client_addr = server.accept()
            # Spawn worker thread for true concurrency
            t = threading.Thread(target=client_handler, args=(conn, client_addr), daemon=True)
            t.start()
    except KeyboardInterrupt:
        print("\n[*] Shutting down server socket.")
    finally:
        server.close()

if __name__ == '__main__':
    run_server()
```

### Inspecting Socket State with Linux Commands
```bash
# Display listening and established TCP sockets with process names
$ ss -tulpn

Netid  State      Recv-Q  Send-Q   Local Address:Port   Peer Address:Port   Process
tcp    LISTEN     0       128            0.0.0.0:8080        0.0.0.0:*      users:(("python3",pid=4921,fd=3))
tcp    ESTAB      0       0         192.168.1.50:8080   192.168.1.12:54210  users:(("python3",pid=4921,fd=4))

# Capture TCP handshake packets live
$ tcpdump -nnvv -i eth0 'tcp[tcpflags] & (tcp-syn|tcp-ack) != 0'
```

---

## 📌 Summary Checklist & Exam Cram Notes

1. **Multiplexing Layer**: IP provides host-to-host delivery; Transport layer provides process-to-process multiplexing using 16-bit ports and 4-tuples.
2. **UDP Protocol**: 8-byte fixed header (Source Port, Dest Port, Length, Checksum). Connectionless, lightweight, zero-overhead, supports broadcast.
3. **TCP Protocol**: Connection-oriented reliable byte-stream protocol. 20–60 byte header with 32-bit Sequence & Cumulative Acknowledgment numbers.
4. **Handshake Mechanics**: 3-Way Handshake (`SYN` $\rightarrow$ `SYN-ACK` $\rightarrow$ `ACK`) synchronizes random Initial Sequence Numbers (ISNs).
5. **Connection Teardown**: 4-Way Teardown (`FIN` $\rightarrow$ `ACK` $\rightarrow$ `FIN` $\rightarrow$ `ACK`). Active closer enters `TIME_WAIT` for $2 \times \text{MSL}$ to ensure final ACK delivery and drain duplicate packets.
6. **SYN Flood Mitigation**: Cryptographic SYN Cookies encode state in the initial sequence number, eliminating half-open backlog queue memory exhaustion.
7. **Flow vs Congestion Control**: Flow control protects receiver buffer (`rwnd` via sliding window); Congestion control protects network link queues (`cwnd` via AIMD).
8. **Congestion Algorithms**: Slow Start (exponential) $\rightarrow$ Congestion Avoidance (additive increase) $\rightarrow$ Fast Retransmit (3 duplicate ACKs) $\rightarrow$ Fast Recovery (multiplicative decrease).
9. **Bandwidth-Delay Product**: $\text{BDP} = \text{Bandwidth} \times \text{RTT}$. Modern high-speed links require the TCP Window Scale option to exceed 64 KB window limits.

---

## 🧠 Practice Problems & Self-Check Questions

1. A sender transmits TCP segments containing bytes 1001 to 2000. The receiver receives them flawlessly. What number does the receiver place in the Acknowledgment Number field of its reply?
2. Why is the TCP 3-Way Handshake necessary? Why couldn't a connection be safely established using only a 2-way exchange (`SYN` and `SYN-ACK`)?
3. What is the fundamental difference between TCP Flow Control and TCP Congestion Control? Which header field dictates flow control?
4. A network link has 10 Gbps capacity and a 50 ms Round-Trip Time. Calculate the Bandwidth-Delay Product (BDP) in megabytes. If the TCP Window Scale option is disabled, what is the maximum achievable throughput?
5. A client application crashes, and its physical machine immediately reboots. An inbound packet arrives for the old connection. What TCP control flag will the operating system kernel send back?
6. During TCP data transfer, a sender receives three identical duplicate ACKs. What does this indicate, and what algorithm does the sender immediately invoke?
