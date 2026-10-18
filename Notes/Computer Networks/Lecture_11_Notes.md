# Lecture 11: NAT, DHCP and Local Network Communication
## Student Notes — SST Computer Networks (Term 5)

---

## 🎯 Learning Objectives

By the end of this lecture and lab module, you should be able to:
- Explain why the **End-to-End Principle (RFC 1958)** was broken by **Network Address Translation (NAT)**, and how NAT/PAT prolonged the lifespan of the IPv4 Internet.
- Trace the bit-level fields of the **28-byte ARP header** and follow the step-by-step resolution process across Layer 2 broadcast domains.
- Dissect the state table operations of **SNAT (Source NAT / Masquerading)** and **DNAT (Destination NAT / Port Forwarding)**, calculating port translations and checksum recalculations.
- Classify the four classical NAT behavior profiles (**Full-Cone, Restricted-Cone, Port-Restricted Cone, Symmetric**) and explain why symmetric NAT obstructs peer-to-peer (P2P) communication.
- Analyze P2P NAT Traversal frameworks: **STUN (RFC 5389)**, **TURN (RFC 5766)**, and **ICE (RFC 8445)** as deployed in WebRTC, Zoom, and online multiplayer gaming.
- Trace the complete **DHCP DORA** state machine (Discover, Offer, Request, Acknowledge) over UDP ports 67/68, analyzing lease timers ($T_1$, $T_2$, $T_3$), Option 82 Relay Agents, and Rogue DHCP mitigation via **DHCP Snooping**.
- Analyze local network vulnerabilities: **ARP Spoofing / Poisoning** and verify its prevention using **Dynamic ARP Inspection (DAI)**.
- Follow the hop-by-hop encapsulation and header rewriting lifecycle of a packet as it traverses private Wi-Fi, default gateways, carrier NATs, and the public internet.

---

## 1. The Architectural Conflict: The End-to-End Principle vs. Address Scarcity

The original architecture of the Internet (formulated by Saltzer, Reed, and Clark in 1984) was built upon the **End-to-End (E2E) Principle**:
> *"The network core should remain simple, dumb, and stateless, focusing solely on datagram forwarding. All complex state, intelligence, reliability, and security must reside strictly at the end hosts."*

Under this paradigm, every device on Earth was intended to possess a globally unique, publicly reachable IP address. End-to-end encryption and direct peer-to-peer communication were seamless.

### The IPv4 Exhaustion Crisis
By the mid-1990s, the explosive commercial growth of the World Wide Web threatened to completely consume the $2^{32} \approx 4.29 \text{ billion}$ IPv4 address space. The long-term architectural solution was **IPv6 (128-bit addresses)**. However, deploying IPv6 required upgrading every router, switch, operating system, and firewall worldwide.

To avert catastrophic address exhaustion while IPv6 was drafted, the IETF deployed two interim survival mechanisms:
1. **Classless Inter-Domain Routing (CIDR - 1993, RFC 1519)**: Eliminated rigid Class A/B/C address waste.
2. **Private IP Address Spaces (RFC 1918 - 1996) + NAT (RFC 1631 / 3022)**: Created reusable private network blocks shielded behind a single public address.

```
┌────────────────────────────────┬───────────────────────────────┬────────────────────────┐
│ RFC 1918 Private Range         │ CIDR Block                    │ Total Usable Addresses │
├────────────────────────────────┼───────────────────────────────┼────────────────────────┤
│ 10.0.0.0 – 10.255.255.255      │ 10.0.0.0/8 (1 Class A)        │ 16,777,216             │
│ 172.16.0.0 – 172.31.255.255    │ 172.16.0.0/12 (16 Class Bs)   │ 1,048,576              │
│ 192.168.0.0 – 192.168.255.255  │ 192.168.0.0/16 (256 Class Cs) │ 65,536                 │
└────────────────────────────────┴───────────────────────────────┴────────────────────────┘
```
> **RFC 1918 Rule**: Internet core routers are strictly hardcoded to drop any IP packet whose destination falls within these private ranges.

---

## 2. ARP: Address Resolution Protocol (RFC 826)

IP addresses provide logical Layer 3 routing across global networks. However, when an Ethernet network interface card (NIC) transmits a frame onto a local physical wire or Wi-Fi channel, it knows nothing about IP addresses. Hardware forwarding operates strictly via **48-bit MAC addresses**.

**ARP** dynamically bridges the Layer 3 logical domain to the Layer 2 physical domain.

### The 28-Byte ARP Packet Structure

```
 0                   1                   2                   3
 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
|         Hardware Type         |         Protocol Type         |
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
|  Hardware Len |  Protocol Len |           Operation           |
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
|                    Sender Hardware Address                    |
|                          (Bytes 0-3)                          |
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
|  Sender Hardware Addr (4-5)   |      Sender Protocol Addr     |
|                               |          (Bytes 0-1)          |
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
|  Sender Protocol Addr (2-3)   |    Target Hardware Address    |
|                               |          (Bytes 0-1)          |
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
|                    Target Hardware Address                    |
|                          (Bytes 2-5)                          |
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
|                    Target Protocol Address                    |
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
```

### Key Field Breakdown:
1. **Hardware Type (16 bits)**: Network protocol type (Ethernet = `0x0001`).
2. **Protocol Type (16 bits)**: Layer 3 protocol (IPv4 = `0x0800`).
3. **Hardware Length (8 bits)**: MAC address byte length = `6`.
4. **Protocol Length (8 bits)**: IPv4 address byte length = `4`.
5. **Operation Code (Opcode - 16 bits)**: `1` = ARP Request, `2` = ARP Reply, `3` = RARP Request, `4` = RARP Reply.
6. **Sender Hardware & Protocol Address**: MAC and IP of the host generating the ARP message.
7. **Target Hardware & Protocol Address**: In an ARP Request, Target MAC is set to `00:00:00:00:00:00` (unknown), while Target IP contains the destination being queried.

---

## 3. ARP Resolution Lifecycle: Broadcast vs. Unicast

```
HOST A (192.168.1.10)                                          HOST B (192.168.1.50)
MAC: AA:AA:AA:AA:AA:AA                                         MAC: BB:BB:BB:BB:BB:BB
      │                                                              │
      │ ──[ 1. ARP Request: "Who has 192.168.1.50?" ]──────────────► │
      │      Ethernet Dst: FF:FF:FF:FF:FF:FF (Broadcast)             │ (All LAN devices
      │      ARP Target MAC: 00:00:00:00:00:00                       │  inspect packet;
      │                                                              │  only B matches)
      │ ◄─[ 2. ARP Reply: "192.168.1.50 is at BB:BB:BB:BB:BB:BB" ]── │
      │      Ethernet Dst: AA:AA:AA:AA:AA:AA (Unicast)               │
      ▼                                                              ▼
Caches: 192.168.1.50 -> BB:BB:BB:BB:BB:BB                       Caches: 192.168.1.10 -> AA:AA:AA:AA:AA:AA
```

### Why Broadcast Request, but Unicast Reply?
- **The Request MUST be Broadcast (`FF:FF:FF:FF:FF:FF`)**: Host A does not know where Host B resides or what its MAC is. It must ask every switch port on the broadcast domain.
- **The Reply MUST be Unicast**: In the request, Host A included its own MAC (`AA:AA:AA:AA:AA:AA`). Host B already knows Host A's exact physical identity, so broadcasting the reply would waste CPU cycles and bandwidth on all other network devices.

### Gratuitous ARP: The Secret Weapon of Failover
A **Gratuitous ARP (GARP)** is an ARP Request or Reply sent by a host asking for **its own IP address** (`Sender IP == Target IP`):
1. **IP Conflict Detection**: Upon booting, a device broadcasts a GARP. If another machine replies, a duplicated IP address exists on the network, triggering a system alert.
2. **High-Availability Clustering (VRRP / CARP)**: When a secondary load balancer or firewall takes over from a failed primary, it broadcasts a Gratuitous ARP. All switches immediately update their CAM (MAC-address-to-port) tables, and all hosts update their ARP caches, routing traffic to the backup hardware in milliseconds.

---

## 4. ARP Spoofing (Poisoning) & Dynamic ARP Inspection (DAI)

Because classical ARP has **zero cryptographic authentication**, any host can reply to an ARP request or broadcast unsolicited replies.

```
         Attacker (Eve)
     MAC: EE:EE:EE:EE:EE:EE
         /            \
        /              \
"192.168.1.1 is at      "192.168.1.10 is at
 EE:EE:EE:EE:EE:EE"      EE:EE:EE:EE:EE:EE"
      /                  \
     ▼                    ▼
Victim (Alice)        Default Gateway (Router)
192.168.1.10          192.168.1.1
```

### The Attack Execution:
1. Attacker sends continuous spoofed ARP replies to Victim: *"192.168.1.1 (Gateway) is at my MAC `EE:EE:EE:EE:EE:EE`"*.
2. Attacker sends spoofed ARP replies to Gateway: *"192.168.1.10 (Victim) is at my MAC `EE:EE:EE:EE:EE:EE`"*.
3. Both nodes overwrite their ARP caches. All traffic between Alice and the Internet now passes through Eve, enabling eavesdropping, password sniffing, and session hijacking (**Man-in-the-Middle - MITM**).

### Enterprise Defense: Dynamic ARP Inspection (DAI)
Managed enterprise switches run **DHCP Snooping** to build a trusted binding database: `[MAC + IP + Switch Port + VLAN]`.
- When an ARP packet arrives at a switch port, the switch hardware compares the sender MAC and IP against its trusted database.
- If an unauthorized host attempts to claim another host's IP, the switch immediately drops the packet and shuts down the port (`err-disable`).

---

## 5. NAT / PAT: Port Address Translation Deep Dive

**Network Address Translation (NAT)** maps private, non-routable IP addresses (RFC 1918) to one or more publicly routable IPv4 addresses.

### The Flavors of NAT:
1. **Static NAT (1-to-1)**: A single private IP maps permanently to a single public IP. Used for public servers (web, mail).
2. **Dynamic NAT (Pool)**: Private hosts map dynamically to an available pool of public IPs. If all public IPs are in use, new connections are rejected.
3. **NAPT / PAT (Port Address Translation / NAT Overload)**: Thousands of internal private sockets map to a **single public IP** by altering Layer 4 TCP/UDP port numbers. This is the technology running inside every home router, smartphone hotspot, and cloud VPC NAT Gateway.

### PAT State Table & Header Rewriting Walkthrough

Suppose Laptop `192.168.1.5` opens an HTTPS connection to Google (`142.250.195.46:443`).
The router's public WAN IP is `203.0.113.5`.

```
LAN Host: 192.168.1.5:52341 ──► [ ROUTER (NAT Engine) ] ──► WAN Host: 142.250.195.46:443
                                     WAN IP: 203.0.113.5
```

#### Step 1: Outbound Translation (SNAT - Source NAT)
1. Laptop generates packet:
   $$\text{IP Header: } \text{Src} = 192.168.1.5, \quad \text{Dst} = 142.250.195.46$$
   $$\text{TCP Header: } \text{SrcPort} = 52341, \quad \text{DstPort} = 443$$
2. Router intercepts the packet on its LAN interface. It allocates an unused ephemeral port on its WAN interface (e.g., `10001`) and records a translation entry in its kernel state table:

| Protocol | Private Source Socket | Public Translated Socket | Destination Socket | State Timeout |
| :--- | :--- | :--- | :--- | :--- |
| **TCP** | `192.168.1.5:52341` | `203.0.113.5:10001` | `142.250.195.46:443` | 7440s (ESTABLISHED) |

3. The router's hardware/kernel rewrites the packet:
   $$\text{Src IP} \leftarrow 203.0.113.5, \quad \text{Src Port} \leftarrow 10001$$
4. **Critical Detail**: Changing the IP and Port modifies the mathematical checksum. The router **recalculates the IPv4 header checksum AND the Layer 4 TCP/UDP checksum** before transmitting the packet onto the WAN link.

#### Step 2: Inbound Return Translation
1. Google replies:
   $$\text{IP Header: } \text{Src} = 142.250.195.46, \quad \text{Dst} = 203.0.113.5$$
   $$\text{TCP Header: } \text{SrcPort} = 443, \quad \text{DstPort} = 10001$$
2. Router inspects incoming packet on WAN interface. It looks up `DstPort = 10001` in its NAT state table.
3. Matching entry found: maps back to `192.168.1.5:52341`.
4. Router rewrites:
   $$\text{Dst IP} \leftarrow 192.168.1.5, \quad \text{Dst Port} \leftarrow 52341$$
5. Router recalculates checksums and forwards the packet onto the LAN to the laptop.

---

## 6. NAT Traversal: The Peer-to-Peer Dilemma

Because NAT tables are populated strictly by **outbound** client traffic, an unsolicited inbound packet arriving at a NAT router's WAN interface has no matching entry. **The router silently drops it**.

This makes direct Peer-to-Peer communication (WebRTC, Zoom, BitTorrent, VoIP SIP, gaming lobbies) between two users behind separate NAT routers impossible without specialized traversal protocols.

```
Peer A (Behind NAT A)                                          Peer B (Behind NAT B)
Private: 192.168.1.5                                           Private: 192.168.0.8
Public:  203.0.113.5                                           Public:  198.51.100.2
        │                                                              │
        │ ──[ Inbound packet dropped: No table entry! ]──► [ NAT B ] ◄─┤
```

### The Solution: STUN, TURN, and ICE

```
                   ┌──────────────────────────────────┐
                   │    Public STUN / TURN Server     │
                   │         (35.200.10.1)            │
                   └──────┬────────────────────┬──────┘
                          │                    │
              (1) Query:  │                    │ (1) Query:
            "What is my   │                    │ "What is my
           public IP:port?"                    │public IP:port?"
                          ▼                    ▼
                   [ NAT Router A ]     [ NAT Router B ]
                          │                    │
                     [ Peer A ] ◄────────────► [ Peer B ]
                            (2) Direct P2P UDP Connection!
```

1. **STUN (Session Traversal Utilities for NAT - RFC 5389)**:
   - Peer A contacts a lightweight public STUN server.
   - The STUN server replies: *"I received your packet from public IP `203.0.113.5`, port `10001`"*.
   - Peer A now knows its own public reflexive address and shares it with Peer B via an out-of-band signaling server (WebSocket).
   - Both peers execute **UDP Hole Punching** simultaneously, punching temporary pinholes in their respective state tables to establish direct P2P transport.
2. **TURN (Traversal Using Relays around NAT - RFC 5766)**:
   - If one or both routers implement **Symmetric NAT** (allocating different external ports for different destinations), hole punching fails.
   - Both peers fall back to a **TURN relay server**, which proxies all media/voice streams between them (guaranteed connectivity, but costs server bandwidth).
3. **ICE (Interactive Connectivity Establishment - RFC 8445)**:
   - The master framework deployed in WebRTC. It gathers all candidate connection paths (Host local IP, STUN server reflexive IP, TURN relay IP) and tests them systematically to select the lowest-latency viable path.

---

## 7. DHCP: Dynamic Host Configuration Protocol (RFC 2131)

Without DHCP, an administrator would have to manually configure an IP address, Subnet Mask, Default Gateway, and DNS server on every single phone, tablet, and laptop that joins an office or home network.

### The Complete DORA State Machine

```
CLIENT (Fresh Boot: 0.0.0.0)                                    DHCP SERVER (Port 67)
Port 68
   │                                                               │
   │ ──────── 1. DHCP DISCOVER (Broadcast) ───────────────────────► │
   │          Src: 0.0.0.0:68    Dst: 255.255.255.255:67           │
   │          MAC: Client MAC    "I need an IP configuration!"     │
   │                                                               │
   │ ◄─────── 2. DHCP OFFER (Unicast or Broadcast) ─────────────── │
   │          Src: Server IP:67  Dst: Offered IP (or 255.255.255.255)
   │          Offered IP: 192.168.1.15, Mask: /24, GW: 192.168.1.1 │
   │                                                               │
   │ ──────── 3. DHCP REQUEST (Broadcast) ────────────────────────► │
   │          Src: 0.0.0.0:68    Dst: 255.255.255.255:67           │
   │          "I accept 192.168.1.15 from Server X!"               │ (Other DHCP servers
   │                                                               │  free their offers)
   │ ◄─────── 4. DHCP ACKNOWLEDGE (ACK) ────────────────────────── │
   │          "Confirmed: 192.168.1.15 is leased for 86400s"       │
   ▼                                                               ▼
BOUND State                                                    Lease Recorded
```

### Critical Protocol Questions:
- **Why is DHCP REQUEST sent as a Broadcast?**
  Multiple DHCP servers on the local LAN may respond with independent `OFFER` packets. When the client selects an offer, broadcasting its `REQUEST` containing the Server Identifier (Option 54) explicitly informs all other competing DHCP servers that their offers were declined, allowing them to return their reserved IPs back into the pool.
- **Why does DHCP run over UDP and not TCP?**
  A fresh client boot has no IP address, no subnet mask, and no gateway. TCP requires a 3-way handshake between two established IP endpoints; UDP allows connectionless datagram transmission using the dummy source `0.0.0.0` to the limited broadcast `255.255.255.255`.

### Lease Timers ($T_1$, $T_2$, $T_3$)
Every DHCP lease includes a validity duration (e.g., 24 hours):
- **$T_1$ (Renewal Timer - 50% of lease, 12 hours)**: Client sends a **unicast DHCP REQUEST** directly to the original issuing DHCP server. If the server replies with `ACK`, the lease timer resets to 24 hours.
- **$T_2$ (Rebinding Timer - 87.5% of lease, 21 hours)**: If the original server crashed or is unreachable, the client transitions to Rebind state and broadcasts a **DHCP REQUEST** to the entire LAN asking *any* available DHCP server to renew its lease.
- **$T_3$ (Expiration - 100% of lease, 24 hours)**: The lease expires immediately. The client must cease all network traffic, release the IP address, and revert to `INIT` state to execute a fresh DORA sequence.

### DHCP Relay Agents & Option 82
In enterprise networks, thousands of hosts across 50 different VLANs cannot each have a dedicated physical DHCP server.
- The router interfaces on each subnet run a **DHCP Relay Agent** (RFC 3046).
- When the router intercepts a broadcast `DISCOVER` on UDP 67, it injects **Option 82** (stamping the exact physical switch port and VLAN ID of the client), converts the broadcast into a **unicast packet**, and forwards it across the WAN to a centralized corporate DHCP cluster.

---

## 8. Real-World Linux Diagnostic Tools

```bash
# 1. View the local ARP neighbor cache
$ ip neigh show
192.168.1.1 dev wlan0 lladdr 14:91:82:3a:41:0b REACHABLE
192.168.1.120 dev wlan0 lladdr 7c:2e:bd:5a:11:02 STALE

# 2. Trace DHCP lease negotiation live on interface eth0
$ sudo dhclient -v -r eth0    # Release current lease
$ sudo dhclient -v eth0       # Execute full DORA
DHCPDISCOVER on eth0 to 255.255.255.255 port 67 interval 3
DHCPOFFER of 192.168.1.15 from 192.168.1.1
DHCPREQUEST for 192.168.1.15 on eth0 to 255.255.255.255 port 67
DHCPACK of 192.168.1.15 from 192.168.1.1
bound to 192.168.1.15 -- renewal in 41243 seconds.

# 3. Inspect active NAT connection tracking table on a Linux router
$ sudo conntrack -L -p tcp
tcp      6 7439 ESTABLISHED src=192.168.1.5 dst=142.250.195.46 sport=52341 dport=443 \
         src=142.250.195.46 dst=203.0.113.5 sport=443 dport=10001 [ASSURED] mark=0
```

---

## 📌 Summary Checklist & Exam Cram Notes

1. **End-to-End Principle**: NAT violated the architectural purity of transparent end-to-end IP delivery, but preserved IPv4 from complete exhaustion.
2. **ARP Protocol**: Maps Layer 3 IP to Layer 2 physical MAC. Requests are **Broadcast**; Replies are **Unicast**. 28-byte payload structure.
3. **Gratuitous ARP**: Host ARPs for its own IP for duplicate IP detection and high-availability gateway failover (VRRP/CARP).
4. **ARP Poisoning Defense**: Dynamic ARP Inspection (DAI) compares ARP packets against trusted DHCP Snooping bindings to drop spoofed Layer 2 frames.
5. **NAPT / PAT**: Translates thousands of internal private sockets `(Private IP, Port)` to a single public socket `(Public IP, Mapped Port)`. Requires Layer 3 and Layer 4 checksum recalculations.
6. **NAT Traversal**: STUN discovers external reflexive mappings; TURN relays data when symmetric NAT blocks direct communication; ICE tests all candidate paths.
7. **DHCP DORA**: **D**iscover (Broadcast) $\rightarrow$ **O**ffer (Unicast/Broadcast) $\rightarrow$ **R**equest (Broadcast) $\rightarrow$ **A**ck (Unicast/Broadcast). Ports: Server=67, Client=68 over UDP.
8. **DHCP Timers**: $T_1$ (50% unicast renewal) $\rightarrow$ $T_2$ (87.5% broadcast rebind) $\rightarrow$ $T_3$ (100% lease expiration).
9. **DHCP Relay**: Option 82 stamps switch circuit/VLAN information onto forwarded DHCP unicasts destined for remote centralized servers.

---

## 🧠 Practice Problems & Self-Check Questions

1. A computer boots up and broadcasts an ARP Request for `192.168.1.1`. Exactly what values are populated in the Target MAC and Target IP fields of the 28-byte ARP header?
2. In Port Address Translation (PAT), why must a router recalculate the TCP checksum in addition to the IPv4 header checksum whenever it translates an outbound packet?
3. What is the operational difference between the DHCP $T_1$ and $T_2$ timers? Why is $T_1$ transmitted as unicast while $T_2$ is transmitted as broadcast?
4. Two gamers behind different residential NAT routers attempt to establish a direct peer-to-peer voice channel. If both routers employ Symmetric NAT, why does classical STUN UDP hole-punching fail, and what protocol must be used as a fallback?
5. How does an enterprise Layer 2 switch running Dynamic ARP Inspection (DAI) verify whether an ARP reply arriving on Port 4 is legitimate or a malicious ARP spoofing attempt?
6. When a laptop moves from home Wi-Fi to a coffee shop, what happens to its existing TCP connections, and what sequence of protocols executes before it can browse the web again?
