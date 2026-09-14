import React, { useState } from 'react';
import { 
  CheckCircle2, 
  XCircle, 
  HelpCircle, 
  RotateCcw, 
  BookOpen, 
  ChevronRight, 
  CheckSquare, 
  CircleDot, 
  Sparkles, 
  Layers, 
  Code2, 
  Info
} from 'lucide-react';
import type { TopicQuiz, QuizQuestion, QuizOption } from '../types/quiz';
import type { Lecture } from '../data/notesData';

interface QuizEngineProps {
  quiz: TopicQuiz | undefined;
  lecture: Lecture;
  onBackToNotes: () => void;
}

export const QuizEngine: React.FC<QuizEngineProps> = ({ quiz, lecture, onBackToNotes }) => {
  const [selectedAnswers, setSelectedAnswers] = useState<Record<string, string[]>>({});
  const [submittedQuestions, setSubmittedQuestions] = useState<Record<string, boolean>>({});
  const [activeQuestionIndex, setActiveQuestionIndex] = useState<number>(0);
  const [demoMode, setDemoMode] = useState<boolean>(false);

  // Demo fallback questions if current lecture has 0 questions
  const demoQuestions: QuizQuestion[] = [
    {
      id: 'demo-q1',
      type: 'single_choice',
      question: 'Sample Single-Choice Question: Which layer of the OSI reference model is responsible for end-to-end process-to-process communication and port multiplexing?',
      options: [
        { id: 'A', text: 'Layer 2 — Data Link Layer' },
        { id: 'B', text: 'Layer 3 — Network Layer' },
        { id: 'C', text: 'Layer 4 — Transport Layer' },
        { id: 'D', text: 'Layer 7 — Application Layer' }
      ],
      correctOptionIds: ['C'],
      explanation: 'Layer 4 (Transport Layer) uses 16-bit port numbers (e.g. TCP/UDP) to deliver segments to specific process sockets on the operating system.',
      difficulty: 'easy',
      subtopic: 'OSI Reference Model'
    },
    {
      id: 'demo-q2',
      type: 'multi_choice',
      question: 'Sample Multi-Choice Question: Which of the following IPv4 address blocks are officially reserved for private networks under RFC 1918? (Select ALL that apply)',
      options: [
        { id: 'A', text: '10.0.0.0/8' },
        { id: 'B', text: '172.16.0.0/12' },
        { id: 'C', text: '169.254.0.0/16' },
        { id: 'D', text: '192.168.0.0/16' }
      ],
      correctOptionIds: ['A', 'B', 'D'],
      explanation: 'RFC 1918 defines 10.0.0.0/8, 172.16.0.0/12, and 192.168.0.0/16 as private address blocks. 169.254.0.0/16 is APIPA / Link-Local (RFC 3927), not RFC 1918.',
      difficulty: 'medium',
      subtopic: 'RFC 1918 Private Addressing'
    }
  ];

  const hasNativeQuestions = Boolean(quiz && quiz.questions && quiz.questions.length > 0);
  const questionsToRender: QuizQuestion[] = hasNativeQuestions 
    ? (quiz?.questions || []) 
    : (demoMode ? demoQuestions : []);

  const currentQ = questionsToRender[activeQuestionIndex];

  const handleOptionClick = (questionId: string, optionId: string, type: 'single_choice' | 'multi_choice') => {
    // If already submitted, lock answer
    if (submittedQuestions[questionId]) return;

    if (type === 'single_choice') {
      setSelectedAnswers((prev) => ({
        ...prev,
        [questionId]: [optionId]
      }));
    } else {
      // Multi choice toggle
      const current = selectedAnswers[questionId] || [];
      const updated = current.includes(optionId)
        ? current.filter(id => id !== optionId)
        : [...current, optionId].sort();
      setSelectedAnswers((prev) => ({
        ...prev,
        [questionId]: updated
      }));
    }
  };

  const handleVerifyQuestion = (questionId: string) => {
    setSubmittedQuestions((prev) => ({
      ...prev,
      [questionId]: true
    }));
  };

  const handleResetQuiz = () => {
    setSelectedAnswers({});
    setSubmittedQuestions({});
    setActiveQuestionIndex(0);
  };

  // Calculate score
  let correctCount = 0;
  questionsToRender.forEach((q) => {
    const userSelected = (selectedAnswers[q.id] || []).slice().sort().join(',');
    const correct = q.correctOptionIds.slice().sort().join(',');
    if (submittedQuestions[q.id] && userSelected === correct) {
      correctCount++;
    }
  });

  // Empty state if topic has no questions and demoMode is false
  if (!hasNativeQuestions && !demoMode) {
    return (
      <div className="max-w-3xl mx-auto px-4 py-12">
        <div className="p-8 rounded-3xl bg-white dark:bg-[#1c1c21] border border-zinc-200 dark:border-[#2c2c34] shadow-2xl text-center">
          
          <div className="w-16 h-16 mx-auto rounded-2xl bg-zinc-900 dark:bg-white text-white dark:text-zinc-950 flex items-center justify-center font-bold shadow-lg mb-6">
            <Layers className="w-8 h-8" />
          </div>

          <span className="px-3 py-1 text-xs font-bold uppercase tracking-wider bg-zinc-100 dark:bg-[#25252b] text-zinc-800 dark:text-zinc-200 rounded-full border border-zinc-200 dark:border-[#383842]">
            Quiz Module Architecture Ready
          </span>

          <h2 className="text-2xl sm:text-3xl font-extrabold text-zinc-900 dark:text-white mt-4 mb-2">
            {quiz?.title || `${lecture.title} Quiz`}
          </h2>
          <p className="text-zinc-600 dark:text-zinc-300 max-w-lg mx-auto text-sm sm:text-base mb-8">
            The high-bandwidth Quiz Engine is fully architected and supports Single-Choice and Multi-Choice MCQs for each topic.
          </p>

          <div className="grid sm:grid-cols-3 gap-4 mb-8 text-left">
            <div className="p-4 rounded-xl bg-zinc-50 dark:bg-[#16161a] border border-zinc-200 dark:border-[#2e2e36]">
              <div className="flex items-center gap-2 text-zinc-900 dark:text-white font-bold text-xs mb-1">
                <CircleDot className="w-4 h-4 text-emerald-400" /> Single Choice
              </div>
              <p className="text-xs text-zinc-500 dark:text-zinc-400">
                Radio selection with instant correctness validation and rationale.
              </p>
            </div>

            <div className="p-4 rounded-xl bg-zinc-50 dark:bg-[#16161a] border border-zinc-200 dark:border-[#2e2e36]">
              <div className="flex items-center gap-2 text-zinc-900 dark:text-white font-bold text-xs mb-1">
                <CheckSquare className="w-4 h-4 text-emerald-400" /> Multi-Select MCQs
              </div>
              <p className="text-xs text-zinc-500 dark:text-zinc-400">
                Checkbox group evaluation for multi-answer questions.
              </p>
            </div>

            <div className="p-4 rounded-xl bg-zinc-50 dark:bg-[#16161a] border border-zinc-200 dark:border-[#2e2e36]">
              <div className="flex items-center gap-2 text-zinc-900 dark:text-white font-bold text-xs mb-1">
                <Code2 className="w-4 h-4 text-emerald-400" /> Code & Formula
              </div>
              <p className="text-xs text-zinc-500 dark:text-zinc-400">
                Supports embedded network snippets, CIDR math, and explanation cards.
              </p>
            </div>
          </div>

          <div className="flex flex-col sm:flex-row items-center justify-center gap-3">
            <button
              onClick={() => setDemoMode(true)}
              className="w-full sm:w-auto px-6 py-3 rounded-xl bg-zinc-900 dark:bg-white text-white dark:text-zinc-950 font-bold text-sm shadow-md hover:scale-[1.02] transition-all flex items-center justify-center gap-2 cursor-pointer"
            >
              <Sparkles className="w-4 h-4" /> Try Engine Simulator Demo
            </button>
            <button
              onClick={onBackToNotes}
              className="w-full sm:w-auto px-6 py-3 rounded-xl bg-zinc-100 dark:bg-[#25252b] hover:bg-zinc-200 dark:hover:bg-[#2e2e36] text-zinc-800 dark:text-zinc-200 font-medium text-sm transition-all flex items-center justify-center gap-2 cursor-pointer"
            >
              <BookOpen className="w-4 h-4" /> Return to Lecture Notes
            </button>
          </div>

        </div>
      </div>
    );
  }

  // Active Quiz View (Charcoal Theme: Dark Grey & White High Contrast)
  return (
    <div className="max-w-3xl mx-auto px-4 py-8">
      
      {/* Top Quiz Header */}
      <div className="mb-6 flex flex-wrap items-center justify-between gap-4 p-5 rounded-2xl bg-white dark:bg-[#1c1c21] border border-zinc-200 dark:border-[#2c2c34] shadow-md">
        <div>
          <div className="flex items-center gap-2">
            <span className="text-xs font-bold uppercase tracking-wider text-emerald-600 dark:text-emerald-400">
              Lecture {quiz?.lectureNumber || lecture.number} Quiz
            </span>
            {demoMode && (
              <span className="text-[10px] font-semibold bg-amber-100 text-amber-800 dark:bg-amber-950 dark:text-amber-300 px-2 py-0.5 rounded-full">
                Simulator Mode
              </span>
            )}
          </div>
          <h2 className="text-lg sm:text-xl font-bold text-zinc-900 dark:text-white mt-0.5">
            {quiz?.title || `${lecture.title} Quiz`}
          </h2>
        </div>

        <div className="flex items-center gap-2">
          <button
            onClick={handleResetQuiz}
            className="flex items-center gap-1.5 px-3 py-1.5 rounded-lg text-xs font-medium text-zinc-600 dark:text-zinc-300 hover:bg-zinc-100 dark:hover:bg-[#25252b] transition-colors cursor-pointer"
            title="Reset answers"
          >
            <RotateCcw className="w-3.5 h-3.5" /> Reset
          </button>
          <button
            onClick={onBackToNotes}
            className="flex items-center gap-1.5 px-3.5 py-1.5 rounded-lg text-xs font-semibold bg-zinc-100 dark:bg-[#25252b] hover:bg-zinc-200 dark:hover:bg-[#2f2f38] text-zinc-800 dark:text-zinc-200 transition-colors cursor-pointer"
          >
            <BookOpen className="w-3.5 h-3.5" /> Back to Notes
          </button>
        </div>
      </div>

      {/* Question Stepper Indicator */}
      <div className="mb-6 flex items-center justify-between gap-2">
        <div className="flex items-center gap-1.5 overflow-x-auto py-1">
          {questionsToRender.map((q, idx) => {
            const isAnswered = Boolean(selectedAnswers[q.id]?.length);
            const isVerified = submittedQuestions[q.id];
            const isCorrect = isVerified && (selectedAnswers[q.id] || []).slice().sort().join(',') === q.correctOptionIds.slice().sort().join(',');
            const isActive = idx === activeQuestionIndex;

            return (
              <button
                key={q.id}
                onClick={() => setActiveQuestionIndex(idx)}
                className={`w-8 h-8 rounded-lg text-xs font-bold transition-all flex items-center justify-center cursor-pointer ${
                  isActive
                    ? 'ring-2 ring-zinc-400 bg-zinc-900 text-white dark:bg-white dark:text-zinc-950 font-bold'
                    : isVerified
                      ? isCorrect
                        ? 'bg-emerald-500/20 text-emerald-400 border border-emerald-500/40'
                        : 'bg-rose-500/20 text-rose-400 border border-rose-500/40'
                      : isAnswered
                        ? 'bg-zinc-200 dark:bg-[#2f2f38] text-zinc-900 dark:text-zinc-100'
                        : 'bg-zinc-100 dark:bg-[#1c1c21] text-zinc-400 hover:text-zinc-700 dark:hover:text-zinc-200 border border-zinc-200 dark:border-[#2c2c34]'
                }`}
              >
                {idx + 1}
              </button>
            );
          })}
        </div>

        <div className="text-xs text-zinc-500 dark:text-zinc-400 whitespace-nowrap font-medium">
          Score: <span className="font-bold text-zinc-900 dark:text-white">{correctCount}</span> / {questionsToRender.length}
        </div>
      </div>

      {/* Active Question Card */}
      {currentQ && (
        <div className="p-6 sm:p-8 rounded-3xl bg-white dark:bg-[#1c1c21] border border-zinc-200 dark:border-[#2c2c34] shadow-2xl">
          
          {/* Question Metadata */}
          <div className="flex flex-wrap items-center justify-between gap-2 mb-4">
            <span className="text-xs font-mono font-bold text-zinc-400">
              Question {activeQuestionIndex + 1} of {questionsToRender.length}
            </span>

            <div className="flex items-center gap-2">
              <span
                className={`text-[11px] font-semibold uppercase px-2.5 py-0.5 rounded-full ${
                  currentQ.type === 'multi_choice'
                    ? 'bg-purple-500/10 text-purple-600 dark:text-purple-300 border border-purple-500/30'
                    : 'bg-emerald-500/10 text-emerald-600 dark:text-emerald-300 border border-emerald-500/30'
                }`}
              >
                {currentQ.type === 'multi_choice' ? 'Multiple Choice (Select all)' : 'Single Choice'}
              </span>

              <span className="text-[11px] font-medium text-zinc-500 dark:text-zinc-400 capitalize bg-zinc-100 dark:bg-[#25252b] px-2 py-0.5 rounded-md border border-zinc-200 dark:border-[#2e2e36]">
                {currentQ.difficulty}
              </span>
            </div>
          </div>

          {/* Question Title */}
          <h3 className="text-base sm:text-lg font-bold text-zinc-900 dark:text-white leading-snug mb-6">
            {currentQ.question}
          </h3>

          {/* Options Group */}
          <div className="space-y-3 mb-6">
            {currentQ.options.map((opt: QuizOption) => {
              const selectedList = selectedAnswers[currentQ.id] || [];
              const isSelected = selectedList.includes(opt.id);
              const isSubmitted = submittedQuestions[currentQ.id];
              const isCorrectOption = currentQ.correctOptionIds.includes(opt.id);

              let optionStyle = 'border-zinc-200 dark:border-[#2c2c34] hover:border-zinc-400 dark:hover:border-zinc-600 bg-white dark:bg-[#16161a] text-zinc-800 dark:text-zinc-200';
              if (isSelected) {
                optionStyle = 'border-zinc-900 dark:border-white bg-zinc-100/80 dark:bg-[#232329] text-zinc-950 dark:text-white shadow-xs';
              }

              if (isSubmitted) {
                if (isCorrectOption) {
                  optionStyle = 'border-emerald-500 bg-emerald-500/10 text-emerald-900 dark:text-emerald-200';
                } else if (isSelected && !isCorrectOption) {
                  optionStyle = 'border-rose-500 bg-rose-500/10 text-rose-900 dark:text-rose-200';
                }
              }

              return (
                <button
                  key={opt.id}
                  onClick={() => handleOptionClick(currentQ.id, opt.id, currentQ.type)}
                  disabled={isSubmitted}
                  className={`w-full text-left p-4 rounded-2xl border transition-all flex items-start gap-3.5 relative cursor-pointer ${optionStyle}`}
                >
                  <div className="mt-0.5 shrink-0">
                    {currentQ.type === 'multi_choice' ? (
                      <div
                        className={`w-5 h-5 rounded-md border flex items-center justify-center text-xs font-bold transition-colors ${
                          isSelected
                            ? 'bg-zinc-900 dark:bg-white text-white dark:text-zinc-950 border-zinc-900 dark:border-white'
                            : 'border-zinc-400 dark:border-zinc-600 text-transparent'
                        }`}
                      >
                        ✓
                      </div>
                    ) : (
                      <div
                        className={`w-5 h-5 rounded-full border flex items-center justify-center transition-colors ${
                          isSelected
                            ? 'border-zinc-900 dark:border-white bg-zinc-900 dark:bg-white'
                            : 'border-zinc-400 dark:border-zinc-600'
                        }`}
                      >
                        {isSelected && <div className="w-2 h-2 rounded-full bg-white dark:bg-zinc-950" />}
                      </div>
                    )}
                  </div>

                  <div className="flex-1 text-sm sm:text-base leading-relaxed font-medium">
                    <span className="font-mono font-bold mr-2 text-zinc-400">
                      {opt.id}.
                    </span>
                    {opt.text}
                  </div>

                  {isSubmitted && isCorrectOption && (
                    <CheckCircle2 className="w-5 h-5 text-emerald-500 shrink-0 mt-0.5" />
                  )}
                  {isSubmitted && isSelected && !isCorrectOption && (
                    <XCircle className="w-5 h-5 text-rose-500 shrink-0 mt-0.5" />
                  )}
                </button>
              );
            })}
          </div>

          {/* Action Bar: Check Answer & Next */}
          <div className="flex items-center justify-between pt-4 border-t border-zinc-200 dark:border-[#2c2c34]">
            <div>
              {!submittedQuestions[currentQ.id] ? (
                <button
                  onClick={() => handleVerifyQuestion(currentQ.id)}
                  disabled={!(selectedAnswers[currentQ.id]?.length)}
                  className="px-6 py-2.5 rounded-xl font-bold text-sm bg-zinc-900 dark:bg-white text-white dark:text-zinc-950 hover:bg-zinc-800 dark:hover:bg-zinc-100 disabled:opacity-30 disabled:cursor-not-allowed shadow-md hover:scale-[1.02] transition-all cursor-pointer"
                >
                  Verify Answer
                </button>
              ) : (
                <span className="text-xs font-semibold text-zinc-500 dark:text-zinc-400 flex items-center gap-1.5">
                  <Info className="w-4 h-4 text-emerald-400" /> Explanation revealed below
                </span>
              )}
            </div>

            <div className="flex items-center gap-2">
              {activeQuestionIndex > 0 && (
                <button
                  onClick={() => setActiveQuestionIndex(prev => prev - 1)}
                  className="px-3.5 py-2 rounded-xl text-xs font-semibold text-zinc-600 dark:text-zinc-300 hover:bg-zinc-100 dark:hover:bg-[#25252b] transition-colors cursor-pointer"
                >
                  Previous
                </button>
              )}

              {activeQuestionIndex < questionsToRender.length - 1 && (
                <button
                  onClick={() => setActiveQuestionIndex(prev => prev + 1)}
                  className="flex items-center gap-1 px-4 py-2 rounded-xl text-xs font-semibold bg-zinc-100 dark:bg-[#25252b] hover:bg-zinc-200 dark:hover:bg-[#2e2e36] text-zinc-900 dark:text-white transition-colors cursor-pointer"
                >
                  Next <ChevronRight className="w-3.5 h-3.5" />
                </button>
              )}
            </div>
          </div>

          {/* Explanation Accordion Card */}
          {submittedQuestions[currentQ.id] && (
            <div className="mt-6 p-5 rounded-2xl bg-zinc-50 dark:bg-[#16161a] border border-zinc-200 dark:border-[#2c2c34] animate-in fade-in duration-300">
              <div className="flex items-center gap-2 font-bold text-xs uppercase tracking-wider text-emerald-600 dark:text-emerald-400 mb-2">
                <HelpCircle className="w-4 h-4" /> Explanation & Key Insight
              </div>
              <p className="text-xs sm:text-sm text-zinc-700 dark:text-zinc-200 leading-relaxed font-normal">
                {currentQ.explanation}
              </p>
              {currentQ.subtopic && (
                <div className="mt-3 pt-2 border-t border-zinc-200 dark:border-[#282830] text-[11px] text-zinc-500 dark:text-zinc-400">
                  Refer to subtopic: <span className="font-semibold text-zinc-900 dark:text-white">{currentQ.subtopic}</span> in lecture notes.
                </div>
              )}
            </div>
          )}

        </div>
      )}

    </div>
  );
};
