export type QuestionType = 'single_choice' | 'multi_choice';

export type DifficultyLevel = 'easy' | 'medium' | 'hard';

export interface QuizOption {
  id: string; // e.g. 'A', 'B', 'C', 'D'
  text: string;
  codeSnippet?: string;
}

export interface QuizQuestion {
  id: string;
  type: QuestionType;
  question: string;
  codeSnippet?: string;
  options: QuizOption[];
  correctOptionIds: string[]; // ['B'] for single, ['A', 'C'] for multi
  explanation: string;
  difficulty: DifficultyLevel;
  subtopic?: string;
}

export interface TopicQuiz {
  topicId: string;
  lectureNumber: number;
  title: string;
  description: string;
  estimatedMinutes?: number;
  questions: QuizQuestion[];
}

export interface QuizSubmissionState {
  isSubmitted: boolean;
  selectedAnswers: Record<string, string[]>; // questionId -> selectedOptionIds
  score: number;
  totalQuestions: number;
  correctCount: number;
}
