import type { SubjectMetadata, SubjectData } from './types';
import { computerNetworksMeta } from './computer-networks/meta';
import { classicalMachineLearningMeta } from './classical-machine-learning/meta';
import { lecturesData as cnLectures } from '../notesData';
import { lecturesData as cmlLectures } from './classical-machine-learning/notesData';
import { quizzesRegistry as cnQuizzes } from '../quizzesData';
import { quizzesRegistry as cmlQuizzes } from './classical-machine-learning/quizzesData';

export const allSubjectsMeta: SubjectMetadata[] = [
  computerNetworksMeta,
  classicalMachineLearningMeta,
  {
    id: 'operating-systems',
    title: 'Operating Systems',
    code: 'CS-302',
    term: 'Term 5',
    shortDescription: 'Kernel architecture, virtual memory, multi-threading primitives, process scheduling, and synchronization algorithms.',
    detailedDescription: 'In-depth OS fundamentals covering CPU scheduling algorithms, POSIX semaphores, paging & multi-level page tables, file systems, and crash recovery.',
    iconName: 'Cpu',
    accentColor: 'indigo',
    status: 'coming_soon',
    lecturesCount: 14,
    questionsCount: 200,
    featuredTopics: [
      'Kernel vs User Mode & System Call Traps',
      'Virtual Memory & Multi-Level Page Tables',
      'CPU Scheduling: CFS, MLFQ, Round Robin',
      'Concurrency: Mutexes, Semaphores & Futexes',
      'Deadlock Detection & Banker\'s Algorithm',
      'Virtual File System (VFS) & Inodes'
    ]
  },
  {
    id: 'dbms',
    title: 'Database Management Systems',
    code: 'CS-204',
    term: 'Term 4',
    shortDescription: 'Relational algebra, storage engines, indexing mechanisms, transaction processing, and query optimization.',
    detailedDescription: 'University-grade coverage of B+ Tree internals, write-ahead logging (WAL), ARIES recovery, strict 2PL, MVCC isolation levels, and relational query trees.',
    iconName: 'Database',
    accentColor: 'amber',
    status: 'coming_soon',
    lecturesCount: 10,
    questionsCount: 150,
    featuredTopics: [
      'B+ Tree Indexing & Disk Page Layout',
      'ACID Guarantees & Serialization Anomalies',
      'Write-Ahead Logging (WAL) & ARIES Protocol',
      'Concurrency Control: Strict 2PL & MVCC',
      'Cost-Based Query Planning & Join Algorithms',
      'Normalization (1NF to BCNF)'
    ]
  },
  {
    id: 'system-design',
    title: 'Distributed Systems & System Design',
    code: 'CS-401',
    term: 'Term 6',
    shortDescription: 'Scalable cloud architectures, partition tolerance, consensus protocols, and large-scale data pipelines.',
    detailedDescription: 'High-level and low-level system design covering CAP/PACELC theorems, Paxos/Raft consensus, consistent hashing, event-driven queues, and microservices.',
    iconName: 'Server',
    accentColor: 'violet',
    status: 'coming_soon',
    lecturesCount: 8,
    questionsCount: 120,
    featuredTopics: [
      'CAP & PACELC Tradeoffs',
      'Consistent Hashing & Virtual Nodes',
      'Consensus: Raft & Paxos Algorithms',
      'Distributed Caching & Eviction Policies',
      'Message Queues & Event Streaming (Kafka)',
      'Rate Limiting & Token Bucket Algorithms'
    ]
  }
];

export function getSubjectMeta(subjectId: string): SubjectMetadata | undefined {
  return allSubjectsMeta.find(s => s.id === subjectId);
}

export function getSubjectData(subjectId: string): SubjectData | null {
  if (subjectId === 'computer-networks') {
    return {
      meta: computerNetworksMeta,
      lectures: cnLectures,
      quizzes: cnQuizzes
    };
  }
  if (subjectId === 'classical-machine-learning') {
    return {
      meta: classicalMachineLearningMeta,
      lectures: cmlLectures,
      quizzes: cmlQuizzes
    };
  }
  return null;
}
