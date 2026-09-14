import React, { useState, useEffect } from 'react';
import { 
  Network, 
  Cpu, 
  Database, 
  Server, 
  Brain,
  BookOpen, 
  CheckCircle2, 
  Layers, 
  BarChart3, 
  Search,
  GraduationCap
} from 'lucide-react';
import { allSubjectsMeta } from '../data/subjects';
import { getSubjectProgressSummary } from '../utils/quizStorage';

interface SubjectsHubProps {
  onSelectSubject: (subjectId: string, initialTab?: 'notes' | 'quiz', lectureId?: string) => void;
  cnLectureIds: string[];
}

export const SubjectsHub: React.FC<SubjectsHubProps> = ({
  onSelectSubject,
  cnLectureIds
}) => {
  const [searchQuery, setSearchQuery] = useState('');
  const [cnProgress, setCnProgress] = useState<{ answeredQuestions: number; submittedQuestions: number }>({
    answeredQuestions: 0,
    submittedQuestions: 0
  });

  // Calculate user's saved quiz progress from browser local storage
  useEffect(() => {
    const stats = getSubjectProgressSummary('computer-networks', cnLectureIds);
    setCnProgress(stats);
  }, [cnLectureIds]);

  const getSubjectIcon = (iconName: string) => {
    switch (iconName) {
      case 'Network':
        return <Network className="w-5 h-5" />;
      case 'Brain':
        return <Brain className="w-5 h-5" />;
      case 'Cpu':
        return <Cpu className="w-5 h-5" />;
      case 'Database':
        return <Database className="w-5 h-5" />;
      case 'Server':
        return <Server className="w-5 h-5" />;
      default:
        return <Layers className="w-5 h-5" />;
    }
  };

  // Only display active subjects with real content (no upcoming/placeholders)
  const activeSubjects = allSubjectsMeta.filter(s => s.status === 'active');
  const totalNotes = activeSubjects.reduce((acc, s) => acc + s.lecturesCount, 0);
  const totalQuizzes = activeSubjects.reduce((acc, s) => acc + s.questionsCount, 0);

  const filteredSubjects = activeSubjects.filter(subject => 
    subject.title.toLowerCase().includes(searchQuery.toLowerCase()) ||
    subject.shortDescription.toLowerCase().includes(searchQuery.toLowerCase()) ||
    subject.featuredTopics.some(t => t.toLowerCase().includes(searchQuery.toLowerCase()))
  );

  return (
    <div className="w-full max-w-5xl mx-auto px-4 sm:px-6 lg:px-8 py-8 space-y-6">
      
      {/* Sleek Hero Column / Header Island (Refined & Minimalist, Not Overdone) */}
      <div className="rounded-2xl bg-[var(--bg-island)] border border-[var(--border-island)] p-6 sm:p-8 transition-colors shadow-xs">
        <div className="flex flex-col md:flex-row md:items-center justify-between gap-6">
          
          <div className="space-y-2 max-w-xl">
            <div className="inline-flex items-center gap-2 px-2.5 py-1 rounded-md bg-[var(--bg-island-subtle)] border border-[var(--border-island)] text-[var(--text-muted)] text-xs font-semibold">
              <GraduationCap className="w-3.5 h-3.5" /> Scaler School of Technology
            </div>
            <h1 className="text-2xl sm:text-3xl font-extrabold text-[var(--text-heading)] tracking-tight">
              Engineering Study Portal
            </h1>
            <p className="text-xs sm:text-sm text-[var(--text-muted)] leading-relaxed">
              University lecture notes, hardware architecture references, and interactive examination quizzes with persistent local browser storage.
            </p>
          </div>

          {/* Quick Metrics (Hero Column) */}
          <div className="grid grid-cols-3 gap-2.5 md:w-80 shrink-0">
            <div className="p-3 rounded-xl bg-[var(--bg-island-subtle)] border border-[var(--border-island)] text-center">
              <div className="text-lg font-bold text-[var(--text-heading)]">{totalNotes}</div>
              <div className="text-[10px] text-[var(--text-muted)] uppercase tracking-wider font-medium mt-0.5">Notes</div>
            </div>
            <div className="p-3 rounded-xl bg-[var(--bg-island-subtle)] border border-[var(--border-island)] text-center">
              <div className="text-lg font-bold text-[var(--text-heading)]">{totalQuizzes}</div>
              <div className="text-[10px] text-[var(--text-muted)] uppercase tracking-wider font-medium mt-0.5">Quizzes</div>
            </div>
            <div className="p-3 rounded-xl bg-[var(--bg-island-subtle)] border border-[var(--border-island)] text-center">
              <div className="text-lg font-bold text-[var(--text-heading)]">100%</div>
              <div className="text-[10px] text-[var(--text-muted)] uppercase tracking-wider font-medium mt-0.5">Offline</div>
            </div>
          </div>

        </div>
      </div>

      {/* Subjects Header & Filter */}
      <div className="flex flex-col sm:flex-row sm:items-center justify-between gap-4 pt-2">
        <div className="flex items-center gap-2">
          <h2 className="text-lg font-bold text-[var(--text-heading)]">
            Available Subjects
          </h2>
          <span className="text-xs font-mono font-semibold px-2.5 py-0.5 rounded-full bg-[var(--bg-island-subtle)] border border-[var(--border-island)] text-[var(--text-muted)]">
            {filteredSubjects.length} Subject{filteredSubjects.length !== 1 ? 's' : ''}
          </span>
        </div>

        {/* Search / Filter */}
        <div className="relative w-full sm:w-64">
          <Search className="absolute left-3 top-1/2 -translate-y-1/2 w-4 h-4 text-[var(--text-muted)]" />
          <input
            type="text"
            placeholder="Search subjects or topics..."
            value={searchQuery}
            onChange={(e) => setSearchQuery(e.target.value)}
            className="w-full pl-9 pr-4 py-2 text-xs rounded-xl bg-[var(--bg-island)] border border-[var(--border-island)] text-[var(--text-heading)] placeholder-[var(--text-muted)] focus:outline-none focus:ring-1 focus:ring-[var(--border-island)] transition-all"
          />
        </div>
      </div>

      {/* Active Subjects List */}
      <div className="grid gap-4">
        {filteredSubjects.map((subject) => {
          const completionPercent = Math.min(
            100, 
            Math.round((cnProgress.answeredQuestions / subject.questionsCount) * 100)
          );

          return (
            <div 
              key={subject.id}
              className="rounded-2xl bg-[var(--bg-island)] border border-[var(--border-island)] p-6 sm:p-8 transition-colors shadow-xs"
            >
              <div className="flex flex-col md:flex-row md:items-start justify-between gap-6">
                
                {/* Left: Subject Info */}
                <div className="space-y-4 flex-1">
                  <div className="flex items-center gap-3.5">
                    <div className="w-12 h-12 rounded-xl bg-[var(--bg-island-subtle)] border border-[var(--border-island)] text-[var(--text-heading)] flex items-center justify-center shrink-0 shadow-xs">
                      {getSubjectIcon(subject.iconName)}
                    </div>
                    <div>
                      <div className="flex items-center gap-2 flex-wrap">
                        <h3 className="text-xl sm:text-2xl font-bold text-[var(--text-heading)]">
                          {subject.title}
                        </h3>
                        <span className="text-[11px] font-mono font-semibold px-2 py-0.5 rounded-md bg-[var(--bg-island-subtle)] border border-[var(--border-island)] text-[var(--text-muted)]">
                          {subject.code || subject.term}
                        </span>
                      </div>
                      <p className="text-xs sm:text-sm text-[var(--text-body)] mt-1 leading-relaxed max-w-2xl">
                        {subject.shortDescription}
                      </p>
                    </div>
                  </div>

                  {/* Topic Badges */}
                  <div className="flex flex-wrap gap-1.5 pt-1">
                    {subject.featuredTopics.map((topic, idx) => (
                      <span 
                        key={idx}
                        className="px-2.5 py-1 text-[11px] font-medium rounded-lg bg-[var(--bg-island-subtle)] border border-[var(--border-island)] text-[var(--text-muted)]"
                      >
                        {topic}
                      </span>
                    ))}
                  </div>

                  {/* Stats Bar */}
                  <div className="flex items-center gap-6 pt-2 text-xs text-[var(--text-muted)]">
                    <div>
                      <span className="font-bold text-[var(--text-heading)]">{subject.lecturesCount}</span> Markdown Notes
                    </div>
                    <span>•</span>
                    <div>
                      <span className="font-bold text-[var(--text-heading)]">{subject.questionsCount}</span> Quiz Questions
                    </div>
                  </div>
                </div>

                {/* Right: Progress & Direct Actions */}
                <div className="md:w-72 shrink-0 space-y-4 pt-2 md:pt-0">
                  {/* Progress tracker */}
                  <div className="p-4 rounded-xl bg-[var(--bg-island-subtle)] border border-[var(--border-island)] space-y-2">
                    <div className="flex items-center justify-between text-xs font-semibold">
                      <span className="text-[var(--text-muted)] flex items-center gap-1.5">
                        <BarChart3 className="w-3.5 h-3.5" /> Progress
                      </span>
                      <span className="text-[var(--text-heading)] font-bold">
                        {subject.questionsCount > 0 ? `${completionPercent}%` : 'Notes Ready'}
                      </span>
                    </div>
                    <div className="w-full h-1.5 rounded-full bg-[var(--border-island)] overflow-hidden">
                      <div 
                        className="h-full bg-[var(--text-heading)] rounded-full transition-all duration-300"
                        style={{ width: `${subject.questionsCount > 0 ? completionPercent : 100}%` }}
                      />
                    </div>
                    <div className="flex justify-between text-[10px] text-[var(--text-muted)]">
                      {subject.questionsCount > 0 ? (
                        <>
                          <span>{cnProgress.answeredQuestions} answered</span>
                          <span>{subject.questionsCount} total</span>
                        </>
                      ) : (
                        <span>Quizzes in preparation</span>
                      )}
                    </div>
                  </div>

                  {/* Direct Action Buttons: Pure Black & White in Midnight */}
                  <div className="grid grid-cols-2 gap-2.5">
                    <button
                      onClick={() => onSelectSubject(subject.id, 'notes')}
                      className="py-2.5 px-3 rounded-xl text-xs font-bold bg-[var(--btn-primary-bg)] text-[var(--btn-primary-text)] hover:opacity-90 transition-all flex items-center justify-center gap-1.5 cursor-pointer shadow-xs"
                    >
                      <BookOpen className="w-3.5 h-3.5" /> Notes
                    </button>

                    <button
                      onClick={() => onSelectSubject(subject.id, 'quiz')}
                      className="py-2.5 px-3 rounded-xl text-xs font-bold bg-[var(--btn-secondary-bg)] border border-[var(--btn-secondary-border)] text-[var(--btn-secondary-text)] hover:opacity-90 transition-all flex items-center justify-center gap-1.5 cursor-pointer shadow-xs"
                    >
                      <CheckCircle2 className="w-3.5 h-3.5" /> Quizzes
                    </button>
                  </div>
                </div>

              </div>
            </div>
          );
        })}

        {filteredSubjects.length === 0 && (
          <div className="text-center py-12 rounded-2xl bg-[var(--bg-island)] border border-[var(--border-island)] text-[var(--text-muted)] text-sm">
            No subjects matching "{searchQuery}"
          </div>
        )}
      </div>

    </div>
  );
};
