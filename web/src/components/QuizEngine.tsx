import React, { useState, useEffect } from 'react';
import { 
  CheckCircle2, 
  XCircle, 
  HelpCircle, 
  BookOpen, 
  ChevronRight, 
  CheckSquare, 
  CircleDot, 
  Sparkles, 
  Layers, 
  Code2, 
  Info, 
  Trash2, 
  Check, 
  AlertTriangle,
  Bookmark
} from 'lucide-react';
import type { TopicQuiz, QuizQuestion, QuizOption } from '../types/quiz';
import type { Lecture } from '../data/notesData';
import { QuizMarkdown } from './QuizMarkdown';
import { 
  loadQuizProgress, 
  saveQuizProgress, 
  clearQuizProgress 
} from '../utils/quizStorage';

interface QuizEngineProps {
  subjectId?: string;
  quiz: TopicQuiz | undefined;
  lecture: Lecture;
  onBackToNotes: () => void;
}

export const QuizEngine: React.FC<QuizEngineProps> = ({ 
  subjectId = 'computer-networks', 
  quiz, 
  lecture, 
  onBackToNotes 
}) => {
  const [selectedAnswers, setSelectedAnswers] = useState<Record<string, string[]>>({});
  const [submittedQuestions, setSubmittedQuestions] = useState<Record<string, boolean>>({});
  const [markedDoneQuestions, setMarkedDoneQuestions] = useState<Record<string, boolean>>({});
  const [markedReviewQuestions, setMarkedReviewQuestions] = useState<Record<string, boolean>>({});
  const [activeQuestionIndex, setActiveQuestionIndex] = useState<number>(0);
  const [demoMode, setDemoMode] = useState<boolean>(false);
  const [showClearConfirm, setShowClearConfirm] = useState<boolean>(false);

  // Load saved state from Local Storage on mount and lecture/subject change
  useEffect(() => {
    const saved = loadQuizProgress(subjectId, lecture.id);
    if (saved) {
      setSelectedAnswers(saved.selectedAnswers || {});
      setSubmittedQuestions(saved.submittedQuestions || {});
      setMarkedDoneQuestions(saved.markedDoneQuestions || {});
      setMarkedReviewQuestions(saved.markedReviewQuestions || {});
      setActiveQuestionIndex(saved.activeQuestionIndex || 0);
    } else {
      setSelectedAnswers({});
      setSubmittedQuestions({});
      setMarkedDoneQuestions({});
      setMarkedReviewQuestions({});
      setActiveQuestionIndex(0);
    }
  }, [subjectId, lecture.id]);

  const persistState = (
    newAnswers: Record<string, string[]>,
    newSubmitted: Record<string, boolean>,
    newIndex: number,
    newDone: Record<string, boolean> = markedDoneQuestions,
    newReview: Record<string, boolean> = markedReviewQuestions
  ) => {
    saveQuizProgress(subjectId, lecture.id, {
      selectedAnswers: newAnswers,
      submittedQuestions: newSubmitted,
      activeQuestionIndex: newIndex,
      markedDoneQuestions: newDone,
      markedReviewQuestions: newReview,
      lastUpdated: Date.now()
    });
  };

  const handleToggleDoneQuestion = (questionId: string) => {
    const updated = {
      ...markedDoneQuestions,
      [questionId]: !markedDoneQuestions[questionId]
    };
    setMarkedDoneQuestions(updated);
    persistState(selectedAnswers, submittedQuestions, activeQuestionIndex, updated, markedReviewQuestions);
  };

  const handleToggleReviewQuestion = (questionId: string) => {
    const updated = {
      ...markedReviewQuestions,
      [questionId]: !markedReviewQuestions[questionId]
    };
    setMarkedReviewQuestions(updated);
    persistState(selectedAnswers, submittedQuestions, activeQuestionIndex, markedDoneQuestions, updated);
  };

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
      const updated = {
        ...selectedAnswers,
        [questionId]: [optionId]
      };
      setSelectedAnswers(updated);
      persistState(updated, submittedQuestions, activeQuestionIndex);
    } else {
      // Multi choice toggle
      const current = selectedAnswers[questionId] || [];
      const updatedList = current.includes(optionId)
        ? current.filter(id => id !== optionId)
        : [...current, optionId].sort();
      const updated = {
        ...selectedAnswers,
        [questionId]: updatedList
      };
      setSelectedAnswers(updated);
      persistState(updated, submittedQuestions, activeQuestionIndex);
    }
  };

  const handleVerifyQuestion = (questionId: string) => {
    const updatedSubmitted = {
      ...submittedQuestions,
      [questionId]: true
    };
    setSubmittedQuestions(updatedSubmitted);
    persistState(selectedAnswers, updatedSubmitted, activeQuestionIndex);
  };

  const handleClearAll = () => {
    clearQuizProgress(subjectId, lecture.id);
    setSelectedAnswers({});
    setSubmittedQuestions({});
    setMarkedDoneQuestions({});
    setMarkedReviewQuestions({});
    setActiveQuestionIndex(0);
    setShowClearConfirm(false);
  };

  const handleSelectQuestionIndex = (idx: number) => {
    setActiveQuestionIndex(idx);
    persistState(selectedAnswers, submittedQuestions, idx);
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
    <div className="max-w-3xl mx-auto px-4 py-8 relative">
      
      {/* Clear Confirmation Modal */}
      {showClearConfirm && (
        <div className="fixed inset-0 z-50 flex items-center justify-center p-4 bg-black/70 backdrop-blur-xs animate-in fade-in duration-150">
          <div className="w-full max-w-md p-6 rounded-2xl bg-white dark:bg-[#1c1c21] border border-zinc-200 dark:border-[#2c2c34] shadow-2xl">
            <div className="flex items-center gap-3 mb-3 text-rose-500">
              <div className="p-2 rounded-xl bg-rose-500/10">
                <AlertTriangle className="w-6 h-6" />
              </div>
              <h3 className="text-lg font-bold text-zinc-900 dark:text-white">
                Clear All Quiz Answers?
              </h3>
            </div>
            <p className="text-xs sm:text-sm text-zinc-600 dark:text-zinc-300 mb-6 leading-relaxed">
              This will erase all selected options and verification statuses for <strong>{lecture.title}</strong> from browser local storage. This cannot be undone.
            </p>
            <div className="flex items-center justify-end gap-3">
              <button
                onClick={() => setShowClearConfirm(false)}
                className="px-4 py-2 rounded-xl text-xs font-semibold text-zinc-600 dark:text-zinc-300 hover:bg-zinc-100 dark:hover:bg-[#25252b] transition-colors cursor-pointer"
              >
                Cancel
              </button>
              <button
                onClick={handleClearAll}
                className="px-4 py-2 rounded-xl text-xs font-bold bg-rose-600 hover:bg-rose-700 text-white shadow-md transition-all cursor-pointer"
              >
                Yes, Clear All
              </button>
            </div>
          </div>
        </div>
      )}

      {/* Top Quiz Header */}
      <div className="mb-6 flex flex-wrap items-center justify-between gap-4 p-5 rounded-2xl bg-[var(--bg-island-subtle)] border border-[var(--border-island)] shadow-md">
        <div>
          <div className="flex items-center gap-2">
            <span className="text-xs font-bold uppercase tracking-wider text-[var(--text-muted)]">
              Lecture {quiz?.lectureNumber || lecture.number} Quiz
            </span>
            {demoMode && (
              <span className="text-[10px] font-semibold bg-[var(--bg-island)] text-[var(--text-muted)] px-2 py-0.5 rounded-full border border-[var(--border-island)]">
                Simulator Mode
              </span>
            )}
          </div>
          <h2 className="text-lg sm:text-xl font-bold text-[var(--text-heading)] mt-0.5">
            {quiz?.title || `${lecture.title} Quiz`}
          </h2>
        </div>

        <div className="flex items-center gap-2">
          <div className="hidden sm:flex items-center gap-1.5 px-2.5 py-1 rounded-md bg-[var(--bg-island)] border border-[var(--border-island)] text-[var(--text-muted)] text-[11px] font-medium">
            <Check className="w-3 h-3 text-[var(--text-heading)]" /> Saved
          </div>
          <button
            onClick={() => setShowClearConfirm(true)}
            className="flex items-center gap-1.5 px-3 py-1.5 rounded-lg text-xs font-semibold text-rose-500 hover:bg-rose-500/10 border border-rose-500/30 transition-all cursor-pointer"
            title="Clear all answers for this quiz"
          >
            <Trash2 className="w-3.5 h-3.5" /> Clear All
          </button>
          <button
            onClick={onBackToNotes}
            className="flex items-center gap-1.5 px-3.5 py-1.5 rounded-lg text-xs font-semibold bg-[var(--btn-secondary-bg)] border border-[var(--btn-secondary-border)] text-[var(--btn-secondary-text)] hover:opacity-90 transition-colors cursor-pointer"
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
            const isDoneMarked = markedDoneQuestions[q.id];
            const isReviewMarked = markedReviewQuestions[q.id];

            return (
              <button
                key={q.id}
                onClick={() => handleSelectQuestionIndex(idx)}
                className={`relative w-8 h-8 rounded-lg text-xs font-bold transition-all flex items-center justify-center cursor-pointer ${
                  isActive
                    ? 'ring-2 ring-[var(--text-heading)] bg-[var(--btn-primary-bg)] text-[var(--btn-primary-text)] font-bold'
                    : isVerified
                      ? isCorrect
                        ? 'bg-emerald-500/20 text-emerald-400 border border-emerald-500/40'
                        : 'bg-rose-500/20 text-rose-400 border border-rose-500/40'
                      : isAnswered
                        ? 'bg-[var(--bg-island-subtle)] text-[var(--text-heading)] border border-[var(--border-island)]'
                        : 'bg-[var(--bg-island)] text-[var(--text-muted)] border border-[var(--border-island)] hover:text-[var(--text-heading)]'
                }`}
              >
                {idx + 1}
                {isReviewMarked && (
                  <span
                    title="Marked for review"
                    className="absolute -top-1 -right-1 w-2.5 h-2.5 rounded-full bg-amber-400 ring-2 ring-[var(--bg-page)]"
                  />
                )}
                {isDoneMarked && (
                  <span
                    title="Marked as done"
                    className="absolute -bottom-1 -right-1 w-2.5 h-2.5 rounded-full bg-emerald-400 ring-2 ring-[var(--bg-page)]"
                  />
                )}
              </button>
            );
          })}
        </div>

        <div className="text-xs text-[var(--text-muted)] whitespace-nowrap font-medium">
          Score: <span className="font-bold text-[var(--text-heading)]">{correctCount}</span> / {questionsToRender.length}
        </div>
      </div>

      {/* Active Question Card */}
      {currentQ && (
        <div className="p-6 sm:p-8 rounded-3xl bg-[var(--bg-island-subtle)] border border-[var(--border-island)] shadow-xl">
          
          {/* Question Metadata & Status Toggles */}
          <div className="flex flex-wrap items-center justify-between gap-3 mb-4 pb-3 border-b border-[var(--border-island)]">
            <span className="text-xs font-mono font-bold text-zinc-400">
              Question {activeQuestionIndex + 1} of {questionsToRender.length}
            </span>

            <div className="flex flex-wrap items-center gap-2">
              {/* Question Level Mark for Review Toggle */}
              <button
                onClick={() => handleToggleReviewQuestion(currentQ.id)}
                className={`flex items-center gap-1.5 px-3 py-1 rounded-full text-xs font-semibold border transition-all cursor-pointer ${
                  markedReviewQuestions[currentQ.id]
                    ? 'bg-amber-500/15 text-amber-400 border-amber-500/40 shadow-xs'
                    : 'bg-[var(--bg-island)] text-[var(--text-muted)] border-[var(--border-island)] hover:text-[var(--text-heading)]'
                }`}
                title={markedReviewQuestions[currentQ.id] ? 'Marked for review (click to unmark)' : 'Mark question for review'}
              >
                <Bookmark className={`w-3.5 h-3.5 ${markedReviewQuestions[currentQ.id] ? 'fill-current text-amber-400' : ''}`} />
                <span>{markedReviewQuestions[currentQ.id] ? 'For Review' : 'Mark Review'}</span>
              </button>

              {/* Question Level Mark as Done Toggle */}
              <button
                onClick={() => handleToggleDoneQuestion(currentQ.id)}
                className={`flex items-center gap-1.5 px-3 py-1 rounded-full text-xs font-bold border transition-all cursor-pointer ${
                  markedDoneQuestions[currentQ.id]
                    ? 'bg-emerald-500/20 text-emerald-400 border-emerald-500/40 shadow-xs'
                    : 'bg-[var(--bg-island)] text-[var(--text-muted)] border-[var(--border-island)] hover:text-[var(--text-heading)]'
                }`}
                title={markedDoneQuestions[currentQ.id] ? 'Marked as done (click to unmark)' : 'Mark question as done'}
              >
                <CheckCircle2 className={`w-3.5 h-3.5 ${markedDoneQuestions[currentQ.id] ? 'text-emerald-400' : ''}`} />
                <span>{markedDoneQuestions[currentQ.id] ? 'Completed' : 'Mark Done'}</span>
              </button>

              <span
                className={`text-[11px] font-semibold uppercase px-2.5 py-0.5 rounded-full ${
                  currentQ.type === 'multi_choice'
                    ? 'bg-purple-500/10 text-purple-600 dark:text-purple-300 border border-purple-500/30'
                    : 'bg-emerald-500/10 text-emerald-600 dark:text-emerald-300 border border-emerald-500/30'
                }`}
              >
                {currentQ.type === 'multi_choice' ? 'Multi Choice' : 'Single Choice'}
              </span>

              <span className="text-[11px] font-medium text-zinc-500 dark:text-zinc-400 capitalize bg-zinc-100 dark:bg-[#25252b] px-2 py-0.5 rounded-md border border-zinc-200 dark:border-[#2e2e36]">
                {currentQ.difficulty}
              </span>
            </div>
          </div>

          {/* Question Title */}
          <div className="text-base sm:text-lg font-bold text-[var(--text-heading)] leading-snug mb-6">
            <QuizMarkdown content={currentQ.question} asSpan />
          </div>

          {currentQ.codeSnippet && (
            <div className="mb-6 rounded-2xl overflow-hidden border border-zinc-200 dark:border-[#2c2c34] bg-zinc-950 shadow-md">
              <pre className="p-4 overflow-x-auto text-xs sm:text-sm font-mono leading-relaxed text-zinc-100 m-0">
                <code>{currentQ.codeSnippet}</code>
              </pre>
            </div>
          )}

          {/* Options Group */}
          <div className="space-y-3 mb-6">
            {currentQ.options.map((opt: QuizOption) => {
              const selectedList = selectedAnswers[currentQ.id] || [];
              const isSelected = selectedList.includes(opt.id);
              const isSubmitted = submittedQuestions[currentQ.id];
              const isCorrectOption = currentQ.correctOptionIds.includes(opt.id);

              let optionStyle = 'border border-[var(--border-island)] hover:border-[var(--text-heading)] bg-[var(--bg-island)] text-[var(--text-body)]';
              if (isSelected) {
                optionStyle = 'border-2 border-[var(--text-heading)] bg-[var(--bg-island-subtle)] text-[var(--text-heading)] shadow-xs';
              }

              if (isSubmitted) {
                if (isCorrectOption) {
                  optionStyle = 'border-2 border-emerald-500 bg-emerald-500/10 text-[var(--text-heading)]';
                } else if (isSelected && !isCorrectOption) {
                  optionStyle = 'border-2 border-rose-500 bg-rose-500/10 text-[var(--text-heading)]';
                }
              }

              return (
                <button
                  key={opt.id}
                  onClick={() => handleOptionClick(currentQ.id, opt.id, currentQ.type)}
                  disabled={isSubmitted}
                  className={`w-full text-left p-4 rounded-2xl transition-all flex items-start gap-3.5 relative cursor-pointer ${optionStyle}`}
                >
                  <div className="mt-0.5 shrink-0">
                    {currentQ.type === 'multi_choice' ? (
                      <div
                        className={`w-5 h-5 rounded-md border flex items-center justify-center text-xs font-bold transition-colors ${
                          isSelected
                            ? 'bg-[var(--btn-primary-bg)] text-[var(--btn-primary-text)] border-[var(--text-heading)]'
                            : 'border-[var(--border-island)] text-transparent'
                        }`}
                      >
                        ✓
                      </div>
                    ) : (
                      <div
                        className={`w-5 h-5 rounded-full border flex items-center justify-center transition-colors ${
                          isSelected
                            ? 'border-[var(--text-heading)] bg-[var(--btn-primary-bg)] text-[var(--btn-primary-text)]'
                            : 'border-[var(--border-island)]'
                        }`}
                      >
                        {isSelected && <div className="w-2 h-2 rounded-full bg-[var(--btn-primary-text)]" />}
                      </div>
                    )}
                  </div>

                  <div className="flex-1 text-sm sm:text-base leading-relaxed font-medium">
                    <span className="font-mono font-bold mr-2 text-[var(--text-muted)] inline-block">
                      {opt.id}.
                    </span>
                    <QuizMarkdown content={opt.text} asSpan className="inline" />
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
          <div className="flex items-center justify-between pt-4 border-t border-[var(--border-island)]">
            <div>
              {!submittedQuestions[currentQ.id] ? (
                <button
                  onClick={() => handleVerifyQuestion(currentQ.id)}
                  disabled={!(selectedAnswers[currentQ.id]?.length)}
                  className="px-6 py-2.5 rounded-xl font-bold text-sm bg-[var(--btn-primary-bg)] text-[var(--btn-primary-text)] hover:opacity-90 disabled:opacity-30 disabled:cursor-not-allowed shadow-md transition-all cursor-pointer"
                >
                  Verify Answer
                </button>
              ) : (
                <span className="text-xs font-semibold text-[var(--text-muted)] flex items-center gap-1.5">
                  <Info className="w-4 h-4 text-emerald-400" /> Explanation revealed below
                </span>
              )}
            </div>

            <div className="flex items-center gap-2">
              {activeQuestionIndex > 0 && (
                <button
                  onClick={() => handleSelectQuestionIndex(activeQuestionIndex - 1)}
                  className="px-3.5 py-2 rounded-xl text-xs font-semibold bg-[var(--btn-secondary-bg)] border border-[var(--btn-secondary-border)] text-[var(--btn-secondary-text)] hover:opacity-90 transition-colors cursor-pointer"
                >
                  Previous
                </button>
              )}

              {activeQuestionIndex < questionsToRender.length - 1 && (
                <button
                  onClick={() => handleSelectQuestionIndex(activeQuestionIndex + 1)}
                  className="flex items-center gap-1 px-4 py-2 rounded-xl text-xs font-semibold bg-[var(--btn-secondary-bg)] border border-[var(--btn-secondary-border)] text-[var(--btn-secondary-text)] hover:opacity-90 transition-colors cursor-pointer"
                >
                  Next <ChevronRight className="w-3.5 h-3.5" />
                </button>
              )}
            </div>
          </div>

          {/* Explanation Accordion Card */}
          {submittedQuestions[currentQ.id] && (
            <div className="mt-6 p-5 rounded-2xl bg-[var(--bg-island)] border border-[var(--border-island)] animate-in fade-in duration-300">
              <div className="flex items-center gap-2 font-bold text-xs uppercase tracking-wider text-emerald-500 mb-2">
                <HelpCircle className="w-4 h-4" /> Explanation & Key Insight
              </div>
              <div className="text-xs sm:text-sm text-[var(--text-body)] leading-relaxed font-normal">
                <QuizMarkdown content={currentQ.explanation} />
              </div>
              {currentQ.subtopic && (
                <div className="mt-3 pt-2 border-t border-[var(--border-island)] text-[11px] text-[var(--text-muted)]">
                  Refer to subtopic: <span className="font-semibold text-[var(--text-heading)]">{currentQ.subtopic}</span> in lecture notes.
                </div>
              )}
            </div>
          )}

        </div>
      )}

    </div>
  );
};
