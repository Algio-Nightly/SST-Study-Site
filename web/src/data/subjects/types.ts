import type { Lecture } from '../notesData';
import type { TopicQuiz } from '../../types/quiz';

export type SubjectStatus = 'active' | 'coming_soon' | 'in_development';

export interface SubjectMetadata {
  id: string;
  title: string;
  code?: string;
  term: string;
  shortDescription: string;
  detailedDescription: string;
  iconName: string;
  accentColor: string;
  status: SubjectStatus;
  lecturesCount: number;
  questionsCount: number;
  featuredTopics: string[];
  instructors?: string[];
  githubRepoUrl?: string;
}

export interface SubjectData {
  meta: SubjectMetadata;
  lectures: Lecture[];
  quizzes: Record<string, TopicQuiz>;
}
