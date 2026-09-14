# SST Computer Networks: Notes & Interactive Quiz Platform

A high-bandwidth, modern study platform for **Computer Networks (Term 5, Scaler School of Technology)**.

This repository organizes all course lecture notes into a dedicated `Notes/` directory, provides heavily enriched, university-grade deep dives for **Lectures 2 through 8**, and bundles a responsive **React 19 + TypeScript + Tailwind CSS** application capable of rendering notes with KaTeX math, code syntax highlighting, table of contents navigation, and hosting per-topic quizzes with support for both **Single-Choice** and **Multi-Select Multiple Choice Questions (MCQs)**.

---

## 📂 Repository Structure

```
.
├── Notes/                             # All 12 Computer Networks lecture notes
│   ├── Lecture_02_Notes.md           # [ENRICHED] Network Packets & Layered Communication (OSI vs TCP/IP, Ethernet, MTU, PMTUD)
│   ├── Lecture_03_Notes.md           # [ENRICHED] IP Addresses & Subnetting I (Binary arithmetic, CIDR, Magic Numbers, RFC 1918)
│   ├── Lecture_04_Notes.md           # [ENRICHED] IP Addresses & Subnetting II (VLSM Tree, IPv6 RFC 5952, Gateway routing, NAT/PAT)
│   ├── Lecture_05_Notes.md           # [ENRICHED] Graph Algorithms I (BFS hop count, DFS cycles, Dijkstra Priority Queue, FIB generation)
│   ├── Lecture_06_Notes.md           # [ENRICHED] Graph Algorithms II (Dijkstra negative weights, Bellman-Ford, MST, STP 802.1D)
│   ├── Lecture_07_Notes.md           # [ENRICHED] Routing & Forwarding I (Control vs Data plane, RIB vs FIB, LPM, TCAM, Packet Lifecycle)
│   ├── Lecture_08_Notes.md           # [ENRICHED] Routing & Forwarding II (Distance Vector, Count-to-Infinity, OSPF Areas, BGP Path Vector)
│   ├── Lecture_09_Notes.md           # DNS & Internet Applications
│   ├── Lecture_10_Notes.md           # Transport Layer & Socket Programming
│   ├── Lecture_11_Notes.md           # NAT, DHCP & Local Network Communication
│   ├── Lecture_12_Notes.md           # Network Troubleshooting & Diagnostics
│   ├── Lecture_13_Notes.md           # The Complete Internet Journey (URL to Response)
│   └── lectures_manifest.json        # Compiled metadata & word count manifest
│
├── web/                              # React 19 + TypeScript + Vite + Tailwind CSS App
│   ├── src/
│   │   ├── components/
│   │   │   ├── Navbar.tsx            # Course title, mode tabs, theme switcher, search trigger
│   │   │   ├── Sidebar.tsx           # Categorized modules, progress, filter & badges
│   │   │   ├── MarkdownViewer.tsx    # Markdown rendering, KaTeX math ($...$), syntax highlighting, code copy
│   │   │   ├── TableOfContents.tsx   # Sticky scrollspy navigation column
│   │   │   ├── QuizEngine.tsx        # High-bandwidth MCQ engine (Single-Choice & Multi-Select support)
│   │   │   └── SearchModal.tsx       # Global fuzzy search with keyboard navigation (Ctrl+K)
│   │   ├── data/
│   │   │   ├── notesData.ts          # Strongly-typed lecture notes bundle
│   │   │   └── quizzesData.ts        # Per-topic quiz schema & question registry
│   │   ├── types/
│   │   │   └── quiz.ts               # Type definitions for questions, options, and quiz states
│   │   ├── App.tsx                   # Main layout container & state management
│   │   └── index.css                 # Tailwind CSS & KaTeX styling
│   └── package.json
│
└── tooling/                          # Python 3.13 uv environment
    ├── pyproject.toml                # Managed uv project configuration
    ├── process_notes.py              # Validates notes, calculates read times & generates manifest
    └── generate_web_data.py          # Synchronizes Notes/ into web/src/data/notesData.ts
```

---

## 🚀 Getting Started

### 1. Launch the React Web Application

```bash
cd web
npm install
npm run dev
```
Open [http://localhost:5173](http://localhost:5173) in your browser.

To produce an optimized production build:
```bash
npm run build
npm run preview
```

### 2. Run Python Tooling with `uv`

The `tooling/` directory utilizes `uv` with Python 3.13:

```bash
# Validate lecture notes and regenerate manifest
uv run python tooling/process_notes.py

# Recompile markdown notes into TypeScript web data
uv run python tooling/generate_web_data.py
```

---

## 🧠 Interactive Quiz Architecture

The web application features an extensible **Quiz Engine** designed to host quizzes for each lecture topic:

- **Single-Choice MCQs**: Standard radio selection with immediate feedback.
- **Multi-Select MCQs**: Checkbox selection (`type: "multi_choice"`) supporting questions where multiple options are valid.
- **Explanations & References**: Detailed rationale shown upon answer verification, citing relevant lecture concepts.
- **Extensible Schema**: To add questions for any lecture, simply append entries to `web/src/data/quizzesData.ts` adhering to the `QuizQuestion` schema.

---

## 📚 Summary of Enhancements in Lectures 2–8

- **Lecture 02**: Mathematical derivation of the 64-byte minimum Ethernet frame (CSMA/CD slot time & propagation physics), byte-by-byte Ethernet II anatomy, MTU vs. MSS, IP fragmentation flags (DF, MF, Offset), and Path MTU Discovery (PMTUD).
- **Lecture 03**: Classful addressing vs. CIDR, bitwise AND hardware extraction of Network IDs, the "Magic Number" shortcut ($256 - \text{mask}$), RFC 1918 private ranges, and multi-octet worked problems.
- **Lecture 04**: Variable Length Subnet Masking (VLSM) binary partition tree, IPv6 128-bit architecture, RFC 5952 compression rules, absence of broadcast in IPv6, host routing decisions, and NAT/PAT translation tables.
- **Lecture 05**: Formal graph modeling of networks, BFS hop-count routing, DFS 3-color cycle detection, and Dijkstra’s algorithm with a Min-Heap priority queue ($O((V+E)\log V)$) yielding the Forwarding Information Base (FIB).
- **Lecture 06**: Concrete counterexample showing why Dijkstra fails on negative weights, Bellman-Ford recurrence relation and $|V|-1$ relaxation passes, negative cycle detection, Minimum Spanning Trees (Kruskal with DSU, Prim), and Spanning Tree Protocol (STP 802.1D).
- **Lecture 07**: Separation of Control Plane (Routing) and Data Plane (Forwarding), RIB vs. FIB, Longest Prefix Match (LPM), hardware TCAM parallel lookups, floating static routes, and the 9-step router forwarding pipeline.
- **Lecture 08**: Distance Vector routing (Distributed Bellman-Ford, RIP), the Count-to-Infinity loop failure, loop mitigations (Split Horizon, Poison Reverse, Hold-Down Timers), Link-State OSPF (LSAs, LSDB, Area 0, DR/BDR), and BGP Path Vector inter-domain routing with `AS_PATH`.
