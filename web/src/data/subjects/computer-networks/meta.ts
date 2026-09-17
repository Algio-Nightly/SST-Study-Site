import type { SubjectMetadata } from '../types';

export const computerNetworksMeta: SubjectMetadata = {
  id: 'computer-networks',
  title: 'Computer Networks',
  code: 'CS-301',
  term: 'Term 5',
  shortDescription: 'Core networking principles from Physical & Data Link framing up to BGP, TCAM Hardware LPM, and modern Transport protocols.',
  detailedDescription: 'Comprehensive Scaler School of Technology university notes enriched with deep packet-level dissections, mathematical proofs, real Linux CLI commands, and 240+ interactive examination-grade questions.',
  iconName: 'Network',
  accentColor: 'emerald',
  status: 'active',
  lecturesCount: 13,
  questionsCount: 240,
  featuredTopics: [
    'OSI 7-Layer & TCP/IP Protocol Stack',
    'Bit/Byte Stuffing & HDLC Framing',
    'MAC Sublayer, Ethernet & CSMA/CD Math',
    'IPv4/IPv6 VLSM Subnetting & CIDR',
    'Dijkstra SPF & Bellman-Ford Algorithms',
    'Spanning Tree Protocol (STP) & BPDU Elections',
    'Autonomous Systems, eBGP/iBGP Peering',
    'Hardware Forwarding: TCAM & LPM Lookups'
  ],
  instructors: ['SST Faculty & Network Engineering Team'],
  githubRepoUrl: 'https://github.com/Algio-Nightly/Computer-Networks-Study-Site.git'
};
