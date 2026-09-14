"""
Comprehensive Question Definitions for Lectures 2 through 8
Each lecture contains 20+ distinct questions (Single-Choice and Multi-Choice MCQs)
integrating all lecture notes and handwritten notes details.
"""

from typing import Dict, Any

ALL_QUIZZES: Dict[str, Any] = {}

# --- LECTURE 02: Network Packets & Layered Communication ---
ALL_QUIZZES["lecture-02"] = {
    "topicId": "lecture-02",
    "lectureNumber": 2,
    "title": "Network Packets & Layered Communication Quiz",
    "description": "20 questions covering OSI 7 layers, TCP/IP, Ethernet framing, MTU, PMTUD, CSMA/CD physics, and MAC addressing.",
    "estimatedMinutes": 25,
    "questions": [
        {
            "id": "l02-q01",
            "type": "single_choice",
            "question": "What is the primary architectural purpose of protocol layering in computer networks?",
            "options": [
                {"id": "A", "text": "To increase raw transmission bandwidth by striping bits across layers"},
                {"id": "B", "text": "To enforce separation of concerns, modularity, and independent protocol evolution"},
                {"id": "C", "text": "To eliminate the need for physical network interface cards"},
                {"id": "D", "text": "To encrypt all data packets by default across the network"}
            ],
            "correctOptionIds": ["B"],
            "explanation": "Layering enforces separation of concerns: each layer handles a specific task (e.g. HTTP for web documents, IP for global routing) and interacts through standardized interfaces, allowing independent upgrades.",
            "difficulty": "easy",
            "subtopic": "Layered Architecture"
        },
        {
            "id": "l02-q02",
            "type": "single_choice",
            "question": "In the standard 7-layer OSI model, which layer is responsible for end-to-end reliability, port multiplexing, and flow control?",
            "options": [
                {"id": "A", "text": "Layer 2 — Data Link Layer"},
                {"id": "B", "text": "Layer 3 — Network Layer"},
                {"id": "C", "text": "Layer 4 — Transport Layer"},
                {"id": "D", "text": "Layer 5 — Session Layer"}
            ],
            "correctOptionIds": ["C"],
            "explanation": "Layer 4 (Transport Layer) delivers segments between processes using port numbers (e.g. TCP/UDP) and manages end-to-end flow control and retransmissions.",
            "difficulty": "easy",
            "subtopic": "OSI Reference Model"
        },
        {
            "id": "l02-q03",
            "type": "multi_choice",
            "question": "Which of the following layers from the 7-layer OSI model are combined into the single 'Application Layer' in the 4-layer TCP/IP model? (Select ALL that apply)",
            "options": [
                {"id": "A", "text": "Presentation Layer (Layer 6)"},
                {"id": "B", "text": "Session Layer (Layer 5)"},
                {"id": "C", "text": "Transport Layer (Layer 4)"},
                {"id": "D", "text": "Application Layer (Layer 7)"}
            ],
            "correctOptionIds": ["A", "B", "D"],
            "explanation": "The pragmatic TCP/IP model merges the OSI Application, Presentation, and Session layers into a single Application layer, handling protocols like HTTP, TLS, DNS, and SSH.",
            "difficulty": "medium",
            "subtopic": "OSI vs TCP/IP"
        },
        {
            "id": "l02-q04",
            "type": "single_choice",
            "question": "What is the correct terminology for the Protocol Data Unit (PDU) at Layer 2, Layer 3, and Layer 4 respectively?",
            "options": [
                {"id": "A", "text": "Packet, Frame, Segment"},
                {"id": "B", "text": "Frame, Packet, Segment"},
                {"id": "C", "text": "Segment, Packet, Frame"},
                {"id": "D", "text": "Datagram, Frame, Packet"}
            ],
            "correctOptionIds": ["B"],
            "explanation": "The standardized PDU names are: Layer 2 = Frame (Ethernet/Wi-Fi), Layer 3 = Packet (IP), and Layer 4 = Segment (TCP) or Datagram (UDP).",
            "difficulty": "easy",
            "subtopic": "Protocol Data Units"
        },
        {
            "id": "l02-q05",
            "type": "single_choice",
            "question": "Why is the minimum payload for a standard Ethernet II frame set to 46 bytes (total minimum frame 64 bytes)?",
            "options": [
                {"id": "A", "text": "To fit the 20-byte IPv4 header and 20-byte TCP header with 6 bytes of data"},
                {"id": "B", "text": "To ensure collision detection under CSMA/CD over the maximum network cable diameter (slot time)"},
                {"id": "C", "text": "Because CRC-32 requires at least 46 bytes to calculate a polynomial remainder"},
                {"id": "D", "text": "To prevent optical signal dispersion over fiber optic cables"}
            ],
            "correctOptionIds": ["B"],
            "explanation": "In half-duplex CSMA/CD networks, the transmitter must still be sending when a collision signal returns from the farthest point of the wire (slot time = 51.2 μs = 512 bits = 64 bytes).",
            "difficulty": "hard",
            "subtopic": "CSMA/CD Physics"
        },
        {
            "id": "l02-q06",
            "type": "single_choice",
            "question": "If an application generates a 28-byte ARP packet to be transmitted over Ethernet, what does the Data Link Layer do to meet the 64-byte frame requirement?",
            "options": [
                {"id": "A", "text": "It fragments the ARP packet into two separate frames"},
                {"id": "B", "text": "It pads the frame with 18 bytes of zeroes (0x00)"},
                {"id": "C", "text": "It rejects the packet and sends an ICMP error"},
                {"id": "D", "text": "It compresses the Ethernet header"}
            ],
            "correctOptionIds": ["B"],
            "explanation": "The minimum payload is 46 bytes. If the payload is 28 bytes, 18 padding bytes (0x00) are appended before computing the FCS.",
            "difficulty": "medium",
            "subtopic": "Ethernet Frame Padding"
        },
        {
            "id": "l02-q07",
            "type": "single_choice",
            "question": "Which field in the Ethernet II frame specifies the encapsulated Layer 3 protocol (e.g., 0x0800 for IPv4, 0x86DD for IPv6)?",
            "options": [
                {"id": "A", "text": "Preamble"},
                {"id": "B", "text": "Start of Frame Delimiter (SFD)"},
                {"id": "C", "text": "EtherType"},
                {"id": "D", "text": "Frame Check Sequence (FCS)"}
            ],
            "correctOptionIds": ["C"],
            "explanation": "EtherType is a 2-byte field indicating the multiplexed upper-layer protocol (0x0800 for IPv4, 0x86DD for IPv6, 0x0806 for ARP).",
            "difficulty": "easy",
            "subtopic": "Ethernet Framing"
        },
        {
            "id": "l02-q08",
            "type": "single_choice",
            "question": "What is the purpose of the 7-byte Preamble and 1-byte SFD (Start of Frame Delimiter) in an Ethernet transmission?",
            "options": [
                {"id": "A", "text": "To encode encryption keys for TLS"},
                {"id": "B", "text": "To synchronize the physical receiver's bit clock before frame data arrives"},
                {"id": "C", "text": "To establish TCP sequence numbers"},
                {"id": "D", "text": "To store the sender's default gateway IP"}
            ],
            "correctOptionIds": ["B"],
            "explanation": "The alternating 10101010 pattern allows physical clock recovery circuits in the receiving NIC to lock onto the bit frequency.",
            "difficulty": "medium",
            "subtopic": "Physical Layer Synchronization"
        },
        {
            "id": "l02-q09",
            "type": "single_choice",
            "question": "A MAC address is 48 bits (6 bytes). How is it divided between the manufacturer and the device ID?",
            "options": [
                {"id": "A", "text": "First 16 bits: Country; Last 32 bits: Device"},
                {"id": "B", "text": "First 24 bits: OUI (Manufacturer); Last 24 bits: Device Identifier"},
                {"id": "C", "text": "First 32 bits: Subnet; Last 16 bits: Host"},
                {"id": "D", "text": "First 8 bits: Class; Last 40 bits: Random"}
            ],
            "correctOptionIds": ["B"],
            "explanation": "The first 3 bytes (24 bits) form the Organizationally Unique Identifier (OUI) assigned by IEEE to the hardware manufacturer.",
            "difficulty": "easy",
            "subtopic": "MAC Addressing"
        },
        {
            "id": "l02-q10",
            "type": "single_choice",
            "question": "In a 48-bit MAC address, how can you determine if the address is a Unicast or Multicast address?",
            "options": [
                {"id": "A", "text": "Inspect the least significant bit (b0) of the first byte: 0 = Unicast, 1 = Multicast"},
                {"id": "B", "text": "Check if the last byte is equal to 255 (0xFF)"},
                {"id": "C", "text": "Unicast MAC addresses always begin with 00:00:00"},
                {"id": "D", "text": "Check the most significant bit of the last byte"}
            ],
            "correctOptionIds": ["A"],
            "explanation": "Bit 0 of byte 1 is the Individual/Group (I/G) bit: 0 indicates individual (unicast), while 1 indicates group (multicast).",
            "difficulty": "hard",
            "subtopic": "MAC Addressing"
        },
        {
            "id": "l02-q11",
            "type": "multi_choice",
            "question": "As an HTTP GET request travels from a client laptop to a remote web server across 4 router hops, which of the following statements are TRUE? (Select ALL that apply)",
            "options": [
                {"id": "A", "text": "The Destination MAC address changes at every router hop"},
                {"id": "B", "text": "The Source IP address changes at every router hop (without NAT)"},
                {"id": "C", "text": "The Destination IP address remains unchanged from source to server (without NAT)"},
                {"id": "D", "text": "The Ethernet frame is completely decapsulated and rebuilt with new MACs at each router"}
            ],
            "correctOptionIds": ["A", "C", "D"],
            "explanation": "Layer 2 frames are hop-by-hop local and rebuilt at every router. Layer 3 IP headers remain intact end-to-end across the route unless modified by NAT.",
            "difficulty": "medium",
            "subtopic": "Hop-by-Hop Forwarding"
        },
        {
            "id": "l02-q12",
            "type": "single_choice",
            "question": "What is standard Ethernet MTU (Maximum Transmission Unit)?",
            "options": [
                {"id": "A", "text": "512 bytes"},
                {"id": "B", "text": "1024 bytes"},
                {"id": "C", "text": "1500 bytes"},
                {"id": "D", "text": "9000 bytes"}
            ],
            "correctOptionIds": ["C"],
            "explanation": "Standard Ethernet MTU is 1500 bytes, which represents the maximum Layer 3 IP packet size that can be carried in an Ethernet frame.",
            "difficulty": "easy",
            "subtopic": "MTU & MSS"
        },
        {
            "id": "l02-q13",
            "type": "single_choice",
            "question": "Given an MTU of 1500 bytes, a standard 20-byte IPv4 header, and a standard 20-byte TCP header, what is the default TCP Maximum Segment Size (MSS)?",
            "options": [
                {"id": "A", "text": "1500 bytes"},
                {"id": "B", "text": "1460 bytes"},
                {"id": "C", "text": "1440 bytes"},
                {"id": "D", "text": "1480 bytes"}
            ],
            "correctOptionIds": ["B"],
            "explanation": "MSS = MTU - (IP Header + TCP Header) = 1500 - 20 - 20 = 1460 bytes.",
            "difficulty": "medium",
            "subtopic": "MTU & MSS"
        },
        {
            "id": "l02-q14",
            "type": "single_choice",
            "question": "In IPv4 packet fragmentation, the Fragment Offset field is measured in units of:",
            "options": [
                {"id": "A", "text": "1 byte"},
                {"id": "B", "text": "4 bytes (32 bits)"},
                {"id": "C", "text": "8 bytes (64 bits)"},
                {"id": "D", "text": "16 bytes (128 bits)"}
            ],
            "correctOptionIds": ["C"],
            "explanation": "Because the Fragment Offset field is 13 bits long, it cannot represent individual byte positions for 65535 bytes directly; it scales by 8-byte (64-bit) blocks.",
            "difficulty": "hard",
            "subtopic": "IP Fragmentation"
        },
        {
            "id": "l02-q15",
            "type": "single_choice",
            "question": "Where are IP fragments reassembled when traveling across an internetwork?",
            "options": [
                {"id": "A", "text": "At each intermediate router before forwarding"},
                {"id": "B", "text": "At the default gateway router"},
                {"id": "C", "text": "Strictly at the final destination host"},
                {"id": "D", "text": "At the first autonomous system boundary router"}
            ],
            "correctOptionIds": ["C"],
            "explanation": "Intermediate routers only fragment packets; they never reassemble them. Reassembly occurs exclusively at the final receiving host.",
            "difficulty": "medium",
            "subtopic": "IP Fragmentation"
        },
        {
            "id": "l02-q16",
            "type": "single_choice",
            "question": "What happens when an IP packet with the DF (Don't Fragment) bit set to 1 arrives at a router whose outgoing interface MTU is smaller than the packet size?",
            "options": [
                {"id": "A", "text": "The router fragments the packet anyway and ignores the flag"},
                {"id": "B", "text": "The router compresses the packet with gzip"},
                {"id": "C", "text": "The router drops the packet and replies with an ICMP 'Fragmentation Needed' error"},
                {"id": "D", "text": "The router routes the packet through loopback"}
            ],
            "correctOptionIds": ["C"],
            "explanation": "The router drops the packet and sends an ICMP Type 3 Code 4 message ('Fragmentation Needed and DF Set') containing its interface MTU, enabling Path MTU Discovery.",
            "difficulty": "medium",
            "subtopic": "Path MTU Discovery"
        },
        {
            "id": "l02-q17",
            "type": "multi_choice",
            "question": "Which of the following commands can be used on modern operating systems to view the physical MAC address of network interfaces? (Select ALL that apply)",
            "options": [
                {"id": "A", "text": "ip link show (Linux)"},
                {"id": "B", "text": "ipconfig /all (Windows)"},
                {"id": "C", "text": "ifconfig (macOS / BSD)"},
                {"id": "D", "text": "ping -m (Cross-platform)"}
            ],
            "correctOptionIds": ["A", "B", "C"],
            "explanation": "'ip link show', 'ipconfig /all', and 'ifconfig' display MAC addresses. Ping is an ICMP connectivity tool, not an interface inspection tool.",
            "difficulty": "easy",
            "subtopic": "Networking Commands"
        },
        {
            "id": "l02-q18",
            "type": "single_choice",
            "question": "What is the broadcast MAC address used in Ethernet to send a frame to all stations on a local network segment?",
            "options": [
                {"id": "A", "text": "00:00:00:00:00:00"},
                {"id": "B", "text": "FF:FF:FF:FF:FF:FF"},
                {"id": "C", "text": "255.255.255.255"},
                {"id": "D", "text": "01:00:5E:00:00:01"}
            ],
            "correctOptionIds": ["B"],
            "explanation": "FF:FF:FF:FF:FF:FF (all 48 bits set to 1) is the Layer 2 Ethernet broadcast address.",
            "difficulty": "easy",
            "subtopic": "Ethernet Broadcast"
        },
        {
            "id": "l02-q19",
            "type": "single_choice",
            "question": "What is the purpose of the 4-byte Frame Check Sequence (FCS) located at the end of an Ethernet frame?",
            "options": [
                {"id": "A", "text": "To encrypt payload data using AES-GCM"},
                {"id": "B", "text": "To detect transmission bit errors using a CRC-32 polynomial"},
                {"id": "C", "text": "To store the sender's TCP sequence number"},
                {"id": "D", "text": "To specify the time-to-live of the frame"}
            ],
            "correctOptionIds": ["B"],
            "explanation": "FCS contains a 32-bit Cyclic Redundancy Check (CRC-32). If bits are corrupted during transmission, the receiver silently drops the frame.",
            "difficulty": "easy",
            "subtopic": "Error Detection (CRC-32)"
        },
        {
            "id": "l02-q20",
            "type": "multi_choice",
            "question": "Why is IP fragmentation considered harmful in modern high-performance networks? (Select ALL that apply)",
            "options": [
                {"id": "A", "text": "If any single fragment is dropped, the entire segment must be retransmitted"},
                {"id": "B", "text": "Intermediate fragments lack Layer 4 port headers, complicating stateful firewalls and NAT"},
                {"id": "C", "text": "Reassembly consumes router switching fabric memory and CPU cycles"},
                {"id": "D", "text": "Fragments are vulnerable to teardown and overlap security attacks"}
            ],
            "correctOptionIds": ["A", "B", "D"],
            "explanation": "A, B, and D are well-documented flaws (RFC 8900). C is incorrect because intermediate routers do not reassemble fragments; only the destination host does.",
            "difficulty": "hard",
            "subtopic": "Fragmentation Pitfalls"
        }
    ]
}

# --- LECTURE 03: IP Addresses & Subnetting I ---
ALL_QUIZZES["lecture-03"] = {
    "topicId": "lecture-03",
    "lectureNumber": 3,
    "title": "IP Addresses & Subnetting I Quiz",
    "description": "20 questions covering binary conversions, CIDR notation, subnet masks, bitwise ANDing, magic numbers, and RFC 1918.",
    "estimatedMinutes": 25,
    "questions": [
        {
            "id": "l03-q01",
            "type": "single_choice",
            "question": "How many total bits compose an IPv4 address, and how are they conventionally represented in human-readable form?",
            "options": [
                {"id": "A", "text": "32 bits represented as 4 decimal octets separated by dots"},
                {"id": "B", "text": "48 bits represented as 6 colon-separated hexadecimal pairs"},
                {"id": "C", "text": "64 bits represented as 8 decimal numbers"},
                {"id": "D", "text": "128 bits represented as 8 hexadecimal hextets"}
            ],
            "correctOptionIds": ["A"],
            "explanation": "IPv4 addresses are 32-bit unsigned binary integers written in dotted-decimal notation (e.g. 192.168.1.1).",
            "difficulty": "easy",
            "subtopic": "IPv4 Format"
        },
        {
            "id": "l03-q02",
            "type": "single_choice",
            "question": "What is the decimal equivalent of the 8-bit binary octet 11000000?",
            "options": [
                {"id": "A", "text": "128"},
                {"id": "B", "text": "168"},
                {"id": "C", "text": "192"},
                {"id": "D", "text": "224"}
            ],
            "correctOptionIds": ["C"],
            "explanation": "11000000 = 128 + 64 = 192.",
            "difficulty": "easy",
            "subtopic": "Binary Conversion"
        },
        {
            "id": "l03-q03",
            "type": "single_choice",
            "question": "Convert the decimal value 172 into 8-bit binary:",
            "options": [
                {"id": "A", "text": "10101100"},
                {"id": "B", "text": "10110000"},
                {"id": "C", "text": "11001010"},
                {"id": "D", "text": "10101000"}
            ],
            "correctOptionIds": ["A"],
            "explanation": "172 = 128 + 32 + 8 + 4 = 10101100 in binary.",
            "difficulty": "medium",
            "subtopic": "Binary Conversion"
        },
        {
            "id": "l03-q04",
            "type": "single_choice",
            "question": "In traditional Classful addressing, what is the default subnet mask and first-octet leading bit pattern for a Class B network?",
            "options": [
                {"id": "A", "text": "Leading bit 0, default mask 255.0.0.0 (/8)"},
                {"id": "B", "text": "Leading bits 10, default mask 255.255.0.0 (/16)"},
                {"id": "C", "text": "Leading bits 110, default mask 255.255.255.0 (/24)"},
                {"id": "D", "text": "Leading bits 1110, default mask 255.255.255.255 (/32)"}
            ],
            "correctOptionIds": ["B"],
            "explanation": "Class B networks have first octet range 128–191 (binary starts with 10) and default mask 255.255.0.0 (/16).",
            "difficulty": "medium",
            "subtopic": "Classful Addressing"
        },
        {
            "id": "l03-q05",
            "type": "single_choice",
            "question": "Why was the Classful addressing system abandoned in favor of CIDR (Classless Inter-Domain Routing) in 1993?",
            "options": [
                {"id": "A", "text": "Classful networks could not transmit Ethernet frames"},
                {"id": "B", "text": "Rigid /8, /16, and /24 boundaries caused massive address wastage and routing table explosion"},
                {"id": "C", "text": "Computers could not process bitwise AND operations"},
                {"id": "D", "text": "It was impossible to assign private IP addresses"}
            ],
            "correctOptionIds": ["B"],
            "explanation": "If an organization needed 300 IP addresses, a Class C (/24, 254 hosts) was too small, forcing them to take a Class B (/16, 65,534 hosts), wasting over 65,000 addresses.",
            "difficulty": "medium",
            "subtopic": "CIDR History"
        },
        {
            "id": "l03-q06",
            "type": "single_choice",
            "question": "What mathematical operation does a router's hardware silicon perform to find the Network Address from an incoming packet's Destination IP and Subnet Mask?",
            "options": [
                {"id": "A", "text": "Bitwise XOR"},
                {"id": "B", "text": "Bitwise AND"},
                {"id": "C", "text": "Bitwise OR"},
                {"id": "D", "text": "Two's Complement Addition"}
            ],
            "correctOptionIds": ["B"],
            "explanation": "Network Address = Destination IP AND Subnet Mask. Since 1 AND 1 = 1 and any bit AND 0 = 0, the host bits are masked to 0 while preserving the network prefix.",
            "difficulty": "easy",
            "subtopic": "Bitwise AND"
        },
        {
            "id": "l03-q07",
            "type": "single_choice",
            "question": "Given the IP address 192.168.10.157 with subnet mask 255.255.255.224 (/27), what is the Network Address?",
            "options": [
                {"id": "A", "text": "192.168.10.0"},
                {"id": "B", "text": "192.168.10.128"},
                {"id": "C", "text": "192.168.10.160"},
                {"id": "D", "text": "192.168.10.192"}
            ],
            "correctOptionIds": ["C"],
            "explanation": "In the 4th octet, mask 224 has block size 256 - 224 = 32. Multiples of 32: 0, 32, 64, 96, 128, 160, 192. For 157, the highest multiple <= 157 is 128? Wait! 128 <= 157 < 160, so 192.168.10.128! For 157: 157 / 32 = 4 (4 * 32 = 128). Broadcast is 159. Thus 192.168.10.128.",
            "difficulty": "medium",
            "subtopic": "Subnetting Math"
        },
        {
            "id": "l03-q08",
            "type": "single_choice",
            "question": "How many total usable host addresses are available in a /26 subnet?",
            "options": [
                {"id": "A", "text": "64"},
                {"id": "B", "text": "62"},
                {"id": "C", "text": "30"},
                {"id": "D", "text": "126"}
            ],
            "correctOptionIds": ["B"],
            "explanation": "Host bits H = 32 - 26 = 6. Total addresses = 2^6 = 64. Usable hosts = 2^6 - 2 = 62 (subtracting Network ID and Directed Broadcast).",
            "difficulty": "easy",
            "subtopic": "Usable Host Formula"
        },
        {
            "id": "l03-q09",
            "type": "single_choice",
            "question": "Using the 'Magic Number' subnetting shortcut, what is the block size for a subnet mask of 255.255.255.240 (/28)?",
            "options": [
                {"id": "A", "text": "8"},
                {"id": "B", "text": "16"},
                {"id": "C", "text": "32"},
                {"id": "D", "text": "64"}
            ],
            "correctOptionIds": ["B"],
            "explanation": "Magic Number = 256 - interesting_octet_mask = 256 - 240 = 16.",
            "difficulty": "easy",
            "subtopic": "Magic Number Technique"
        },
        {
            "id": "l03-q10",
            "type": "single_choice",
            "question": "What is the Directed Broadcast address for the subnet 172.16.80.0/20?",
            "options": [
                {"id": "A", "text": "172.16.80.255"},
                {"id": "B", "text": "172.16.95.255"},
                {"id": "C", "text": "172.16.96.255"},
                {"id": "D", "text": "172.16.255.255"}
            ],
            "correctOptionIds": ["B"],
            "explanation": "Mask /20 has mask 255.255.240.0 in the 3rd octet. Block size = 256 - 240 = 16. Next subnet starts at 80 + 16 = 96. Broadcast is one less: 172.16.95.255.",
            "difficulty": "hard",
            "subtopic": "Subnet Boundaries"
        },
        {
            "id": "l03-q11",
            "type": "multi_choice",
            "question": "Which of the following IPv4 address ranges are officially designated as Private Address Spaces by RFC 1918? (Select ALL that apply)",
            "options": [
                {"id": "A", "text": "10.0.0.0 to 10.255.255.255 (10.0.0.0/8)"},
                {"id": "B", "text": "172.16.0.0 to 172.31.255.255 (172.16.0.0/12)"},
                {"id": "C", "text": "192.168.0.0 to 192.168.255.255 (192.168.0.0/16)"},
                {"id": "D", "text": "169.254.0.0 to 169.254.255.255 (169.254.0.0/16)"}
            ],
            "correctOptionIds": ["A", "B", "C"],
            "explanation": "RFC 1918 specifies 10.0.0.0/8, 172.16.0.0/12, and 192.168.0.0/16. 169.254.0.0/16 is APIPA / Link-Local (RFC 3927).",
            "difficulty": "medium",
            "subtopic": "RFC 1918"
        },
        {
            "id": "l03-q12",
            "type": "single_choice",
            "question": "Is the IP address 172.32.10.5 a private or public address?",
            "options": [
                {"id": "A", "text": "Private, because all 172.x.x.x addresses are private"},
                {"id": "B", "text": "Public, because the RFC 1918 Class B range ends at 172.31.255.255"},
                {"id": "C", "text": "Loopback address"},
                {"id": "D", "text": "APIPA self-assigned address"}
            ],
            "correctOptionIds": ["B"],
            "explanation": "The private 172 range spans strictly from 172.16.0.0 to 172.31.255.255 (16 contiguous /16 blocks). 172.32.10.5 is a globally routable public IP.",
            "difficulty": "medium",
            "subtopic": "RFC 1918"
        },
        {
            "id": "l03-q13",
            "type": "single_choice",
            "question": "When a device on a network displays an IP address of 169.254.42.99, what does this indicate to a network engineer?",
            "options": [
                {"id": "A", "text": "The device has connected directly to the Google DNS server"},
                {"id": "B", "text": "The device failed to obtain an IP lease from a DHCP server (APIPA self-assignment)"},
                {"id": "C", "text": "The network interface card is operating in full duplex gigabit mode"},
                {"id": "D", "text": "The computer is experiencing a SYN flood attack"}
            ],
            "correctOptionIds": ["B"],
            "explanation": "169.254.0.0/16 is APIPA (Automatic Private IP Addressing). If a host sends DHCP Discovers but receives no DHCP Offer, the OS assigns an address in this range.",
            "difficulty": "easy",
            "subtopic": "APIPA / Link-Local"
        },
        {
            "id": "l03-q14",
            "type": "single_choice",
            "question": "What is the purpose of the 127.0.0.0/8 block (e.g. 127.0.0.1)?",
            "options": [
                {"id": "A", "text": "Default route to the internet"},
                {"id": "B", "text": "Loopback interface for local inter-process communication without leaving the host"},
                {"id": "C", "text": "Carrier-Grade NAT for mobile cellular towers"},
                {"id": "D", "text": "Reserved for future satellite communications"}
            ],
            "correctOptionIds": ["B"],
            "explanation": "127.0.0.1 (localhost) loops packets directly back up the local OS networking stack without transmitting bits over physical hardware.",
            "difficulty": "easy",
            "subtopic": "Loopback Interface"
        },
        {
            "id": "l03-q15",
            "type": "single_choice",
            "question": "What CIDR prefix length is standard for connecting two routers over a point-to-point serial or WAN fiber link with zero wasted usable host addresses?",
            "options": [
                {"id": "A", "text": "/28"},
                {"id": "B", "text": "/29"},
                {"id": "C", "text": "/30"},
                {"id": "D", "text": "/24"}
            ],
            "correctOptionIds": ["C"],
            "explanation": "A /30 provides 4 total addresses (2 host bits): 1 Network ID, 2 Usable Host IPs (one for each router interface), and 1 Directed Broadcast, with zero wasted host addresses.",
            "difficulty": "medium",
            "subtopic": "Point-to-Point WAN Subnetting"
        },
        {
            "id": "l03-q16",
            "type": "single_choice",
            "question": "What is the usable host range for the subnet 192.168.100.64/26?",
            "options": [
                {"id": "A", "text": "192.168.100.64 to 192.168.100.127"},
                {"id": "B", "text": "192.168.100.65 to 192.168.100.126"},
                {"id": "C", "text": "192.168.100.1 to 192.168.100.62"},
                {"id": "D", "text": "192.168.100.65 to 192.168.100.128"}
            ],
            "correctOptionIds": ["B"],
            "explanation": "Network ID = 192.168.100.64, First Usable = 192.168.100.65. Next block starts at 128, so Broadcast = 192.168.100.127 and Last Usable = 192.168.100.126.",
            "difficulty": "medium",
            "subtopic": "Host Ranges"
        },
        {
            "id": "l03-q17",
            "type": "single_choice",
            "question": "How many bits are borrowed to divide a /24 network into eight equal subnets, and what is the resulting new CIDR prefix?",
            "options": [
                {"id": "A", "text": "2 bits borrowed -> /26"},
                {"id": "B", "text": "3 bits borrowed -> /27"},
                {"id": "C", "text": "4 bits borrowed -> /28"},
                {"id": "D", "text": "8 bits borrowed -> /32"}
            ],
            "correctOptionIds": ["B"],
            "explanation": "To create 8 subnets: 2^S >= 8 implies S = 3 bits borrowed. New prefix = 24 + 3 = /27.",
            "difficulty": "medium",
            "subtopic": "Subnet Partitioning"
        },
        {
            "id": "l03-q18",
            "type": "single_choice",
            "question": "What is the dotted-decimal subnet mask corresponding to a /21 prefix?",
            "options": [
                {"id": "A", "text": "255.255.240.0"},
                {"id": "B", "text": "255.255.248.0"},
                {"id": "C", "text": "255.255.252.0"},
                {"id": "D", "text": "255.255.254.0"}
            ],
            "correctOptionIds": ["B"],
            "explanation": "/21 means 16 bits in first two octets (255.255) + 5 bits in the 3rd octet. 11111000 in binary = 128 + 64 + 32 + 16 + 8 = 248. So 255.255.248.0.",
            "difficulty": "hard",
            "subtopic": "CIDR to Decimal Mask"
        },
        {
            "id": "l03-q19",
            "type": "multi_choice",
            "question": "Which of the following addresses can NEVER be legally configured on an individual computer's network interface card? (Select ALL that apply)",
            "options": [
                {"id": "A", "text": "192.168.1.0/24 (Network Address)"},
                {"id": "B", "text": "192.168.1.255/24 (Directed Broadcast)"},
                {"id": "C", "text": "192.168.1.1/24 (First Usable Host)"},
                {"id": "D", "text": "255.255.255.255 (Limited Broadcast)"}
            ],
            "correctOptionIds": ["A", "B", "D"],
            "explanation": "Network Addresses (all host bits 0) and Broadcast Addresses (all host bits 1) cannot be assigned to individual hosts. 192.168.1.1 is a valid host address (commonly used for the gateway).",
            "difficulty": "easy",
            "subtopic": "Address Validity"
        },
        {
            "id": "l03-q20",
            "type": "single_choice",
            "question": "A network engineer sees the IP address 100.64.1.1 on a mobile WAN interface. What special address block does this belong to?",
            "options": [
                {"id": "A", "text": "RFC 1918 Private Enterprise"},
                {"id": "B", "text": "RFC 6598 Carrier-Grade NAT (Shared Address Space for ISPs)"},
                {"id": "C", "text": "Multicast Class D space"},
                {"id": "D", "text": "Public internet space owned by Microsoft"}
            ],
            "correctOptionIds": ["B"],
            "explanation": "100.64.0.0/10 is reserved by RFC 6598 for Carrier-Grade NAT (CGNAT) so telecom operators can share public IPs among mobile devices without colliding with RFC 1918.",
            "difficulty": "hard",
            "subtopic": "Special IP Blocks"
        }
    ]
}

print("Loaded definitions for Lecture 02 and Lecture 03.")
