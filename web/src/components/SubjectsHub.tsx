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
import { allSubjectsMeta, getSubjectData } from '../data/subjects';
import { getSubjectProgressSummary, getSubjectNotesProgressSummary } from '../utils/quizStorage';

interface SubjectProgressData {
  notesDone: number;
  notesTotal: number;
  notesPercent: number;
  quizAnswered: number;
  quizTotal: number;
  quizPercent: number;
}

interface SubjectsHubProps {
  onSelectSubject: (subjectId: string, initialTab?: 'notes' | 'quiz', lectureId?: string) => void;
  cnLectureIds?: string[];
}

export const SubjectsHub: React.FC<SubjectsHubProps> = ({
  onSelectSubject
}) => {
  const [searchQuery, setSearchQuery] = useState('');
  const [progressMap, setProgressMap] = useState<Record<string, SubjectProgressData>>({});

  // Calculate per-subject progress for both lecture notes and quizzes from browser storage
  const refreshProgress = () => {
    const activeSubs = allSubjectsMeta.filter(s => s.status === 'active');
    const newMap: Record<string, SubjectProgressData> = {};

    for (const sub of activeSubs) {
      const subData = getSubjectData(sub.id);
      const lectureIds = subData ? subData.lectures.map(l => l.id) : [];

      const quizStats = getSubjectProgressSummary(sub.id, lectureIds);
      const notesStats = getSubjectNotesProgressSummary(sub.id, lectureIds);

      const notesTotal = sub.lecturesCount || lectureIds.length;
      const notesPercent = notesTotal > 0 
        ? Math.min(100, Math.round((notesStats.doneCount / notesTotal) * 100)) 
        : 0;

      const quizTotal = sub.questionsCount || 0;
      const quizPercent = quizTotal > 0 
        ? Math.min(100, Math.round((quizStats.answeredQuestions / quizTotal) * 100)) 
        : 0;

      newMap[sub.id] = {
        notesDone: notesStats.doneCount,
        notesTotal,
        notesPercent,
        quizAnswered: quizStats.answeredQuestions,
        quizTotal,
        quizPercent
      };
    }

    setProgressMap(newMap);
  };

  useEffect(() => {
    refreshProgress();
    window.addEventListener('focus', refreshProgress);
    return () => window.removeEventListener('focus', refreshProgress);
  }, []);

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

  const totalNotesDone = Object.values(progressMap).reduce((acc, p) => acc + p.notesDone, 0);
  const totalQuizAnswered = Object.values(progressMap).reduce((acc, p) => acc + p.quizAnswered, 0);

  const filteredSubjects = activeSubjects.filter(subject => 
    subject.title.toLowerCase().includes(searchQuery.toLowerCase()) ||
    subject.shortDescription.toLowerCase().includes(searchQuery.toLowerCase()) ||
    subject.featuredTopics.some(t => t.toLowerCase().includes(searchQuery.toLowerCase()))
  );

  return (
    <div className="w-full max-w-5xl mx-auto px-4 sm:px-6 lg:px-8 py-8 space-y-6">
      
      {/* Sleek Hero Column / Header Island */}
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
              <div className="text-lg font-bold text-[var(--text-heading)]">
                {totalNotesDone} / {totalNotes}
              </div>
              <div className="text-[10px] text-[var(--text-muted)] uppercase tracking-wider font-medium mt-0.5">Notes Done</div>
            </div>
            <div className="p-3 rounded-xl bg-[var(--bg-island-subtle)] border border-[var(--border-island)] text-center">
              <div className="text-lg font-bold text-[var(--text-heading)]">
                {totalQuizAnswered} / {totalQuizzes}
              </div>
              <div className="text-[10px] text-[var(--text-muted)] uppercase tracking-wider font-medium mt-0.5">MCQs Done</div>
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
          const stats = progressMap[subject.id] || {
            notesDone: 0,
            notesTotal: subject.lecturesCount,
            notesPercent: 0,
            quizAnswered: 0,
            quizTotal: subject.questionsCount,
            quizPercent: 0
          };

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
                <div className="md:w-80 shrink-0 space-y-4 pt-2 md:pt-0">
                  {/* Progress Tracker Card with Both Notes & Quizzes */}
                  <div className="p-4 rounded-xl bg-[var(--bg-island-subtle)] border border-[var(--border-island)] space-y-3.5">
                    
                    {/* 1. Lecture Notes Progress Bar */}
                    <div className="space-y-1.5">
                      <div className="flex items-center justify-between text-xs font-semibold">
                        <span className="text-[var(--text-muted)] flex items-center gap-1.5">
                          <BookOpen className="w-3.5 h-3.5 text-emerald-400" /> Notes Progress
                        </span>
                        <span className="text-[var(--text-heading)] font-bold">
                          {stats.notesPercent}%
                        </span>
                      </div>
                      <div className="w-full h-1.5 rounded-full bg-[var(--border-island)] overflow-hidden">
                        <div 
                          className="h-full bg-emerald-500 rounded-full transition-all duration-300"
                          style={{ width: `${stats.notesPercent}%` }}
                        />
                      </div>
                      <div className="flex justify-between text-[10px] text-[var(--text-muted)]">
                        <span>{stats.notesDone} of {stats.notesTotal} completed</span>
                        <span>{stats.notesTotal - stats.notesDone} remaining</span>
                      </div>
                    </div>

                    {/* 2. Interactive Quizzes Progress Bar */}
                    <div className="space-y-1.5 pt-2.5 border-t border-[var(--border-island)]">
                      <div className="flex items-center justify-between text-xs font-semibold">
                        <span className="text-[var(--text-muted)] flex items-center gap-1.5">
                          <BarChart3 className="w-3.5 h-3.5 text-sky-400" /> Quiz Progress
                        </span>
                        <span className="text-[var(--text-heading)] font-bold">
                          {stats.quizTotal > 0 ? `${stats.quizPercent}%` : 'Notes Ready'}
                        </span>
                      </div>
                      <div className="w-full h-1.5 rounded-full bg-[var(--border-island)] overflow-hidden">
                        <div 
                          className="h-full bg-sky-500 rounded-full transition-all duration-300"
                          style={{ width: `${stats.quizTotal > 0 ? stats.quizPercent : 100}%` }}
                        />
                      </div>
                      <div className="flex justify-between text-[10px] text-[var(--text-muted)]">
                        {stats.quizTotal > 0 ? (
                          <>
                            <span>{stats.quizAnswered} answered</span>
                            <span>{stats.quizTotal} total MCQs</span>
                          </>
                        ) : (
                          <span>Quizzes in preparation</span>
                        )}
                      </div>
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
