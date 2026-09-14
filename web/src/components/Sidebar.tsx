import React, { useState } from 'react';
import { 
  Sparkles, 
  Clock, 
  CheckCircle, 
  HelpCircle, 
  Filter,
  X
} from 'lucide-react';
import { lecturesData } from '../data/notesData';
import { quizzesRegistry } from '../data/quizzesData';

interface SidebarProps {
  currentLectureId: string;
  onSelectLecture: (id: string) => void;
  isOpen: boolean;
  onCloseMobile: () => void;
}

export const Sidebar: React.FC<SidebarProps> = ({
  currentLectureId,
  onSelectLecture,
  isOpen,
  onCloseMobile
}) => {
  const [filterQuery, setFilterQuery] = useState('');

  const filteredLectures = lecturesData.filter((lec) => 
    lec.title.toLowerCase().includes(filterQuery.toLowerCase()) ||
    lec.category.toLowerCase().includes(filterQuery.toLowerCase()) ||
    `lecture ${lec.number}`.includes(filterQuery.toLowerCase())
  );

  const categories = Array.from(new Set(lecturesData.map(l => l.category)));

  return (
    <>
      {/* Mobile backdrop */}
      {isOpen && (
        <div 
          onClick={onCloseMobile}
          className="fixed inset-0 bg-black/60 backdrop-blur-xs z-40 lg:hidden"
        />
      )}

      {/* Sidebar Island Card: Dedicated Block */}
      <aside
        className={`fixed lg:sticky top-20 left-4 z-40 lg:z-10 w-72 sm:w-80 shrink-0 self-start bg-[var(--bg-island)] border border-[var(--border-island)] rounded-2xl shadow-xl flex flex-col h-[calc(100vh-6rem)] transition-all duration-200 ease-in-out ${
          isOpen ? 'translate-x-0' : '-translate-x-[115%] lg:translate-x-0'
        }`}
      >
        {/* Island Header & Filter */}
        <div className="p-4 border-b border-[var(--border-island)]">
          <div className="flex items-center justify-between mb-3">
            <span className="text-xs font-bold uppercase tracking-wider text-[var(--text-muted)]">
              Modules ({lecturesData.length})
            </span>
            <div className="flex items-center gap-1.5">
              <span className="text-[10px] font-semibold text-emerald-400 bg-emerald-500/10 border border-emerald-500/30 px-2 py-0.5 rounded-full flex items-center gap-1">
                <Sparkles className="w-3 h-3 text-emerald-400" /> L2–L8 Deep
              </span>
              <button
                onClick={onCloseMobile}
                className="p-1 text-zinc-400 hover:text-white lg:hidden cursor-pointer"
              >
                <X className="w-4 h-4" />
              </button>
            </div>
          </div>

          <div className="relative">
            <input
              type="text"
              placeholder="Search lectures..."
              value={filterQuery}
              onChange={(e) => setFilterQuery(e.target.value)}
              className="w-full text-xs px-3 py-2 pl-8 rounded-xl bg-[var(--bg-island-subtle)] border border-[var(--border-island)] text-[var(--text-heading)] placeholder-zinc-400 focus:outline-none focus:ring-2 focus:ring-zinc-400/40 font-medium"
            />
            <Filter className="w-3.5 h-3.5 text-zinc-400 absolute left-2.5 top-2.5" />
          </div>
        </div>

        {/* Scrollable Lecture List */}
        <div className="flex-1 overflow-y-auto p-3 space-y-4">
          {categories.map((cat) => {
            const catLectures = filteredLectures.filter(l => l.category === cat);
            if (catLectures.length === 0) return null;

            return (
              <div key={cat} className="space-y-1">
                <div className="px-2.5 py-1 text-[10px] font-bold text-[var(--text-muted)] uppercase tracking-wider">
                  {cat}
                </div>

                {catLectures.map((lecture) => {
                  const isSelected = lecture.id === currentLectureId;
                  const isExtended = lecture.number >= 2 && lecture.number <= 8;
                  const quizInfo = quizzesRegistry[lecture.id];
                  const qCount = quizInfo?.questions?.length || 0;

                  return (
                    <button
                      key={lecture.id}
                      onClick={() => {
                        onSelectLecture(lecture.id);
                        onCloseMobile();
                      }}
                      className={`w-full text-left group p-2.5 rounded-xl transition-all relative flex flex-col gap-1 cursor-pointer ${
                        isSelected
                          ? 'bg-[var(--btn-primary-bg)] text-[var(--btn-primary-text)] font-bold shadow-md'
                          : 'hover:bg-[var(--bg-island-subtle)] text-[var(--text-body)]'
                      }`}
                    >
                      <div className="flex items-center justify-between gap-1.5">
                        <div className="flex items-center gap-2 min-w-0">
                          <span
                            className={`text-[11px] font-mono font-bold px-1.5 py-0.5 rounded ${
                              isSelected
                                ? 'bg-zinc-900 text-white dark:bg-zinc-900 dark:text-white'
                                : 'bg-[var(--bg-island-subtle)] text-[var(--text-muted)] border border-[var(--border-island)]'
                            }`}
                          >
                            L{lecture.number.toString().padStart(2, '0')}
                          </span>
                          <span className="text-xs font-semibold truncate leading-tight">
                            {lecture.title.replace(/^Lecture\s+\d+:\s*/, '')}
                          </span>
                        </div>
                        {isExtended && (
                          <span
                            title="Extended with in-depth explanations, formulas & diagrams"
                            className={`shrink-0 p-0.5 rounded ${
                              isSelected
                                ? 'text-amber-500'
                                : 'text-amber-400'
                            }`}
                          >
                            <Sparkles className="w-3.5 h-3.5 fill-current" />
                          </span>
                        )}
                      </div>

                      {/* Metadata */}
                      <div
                        className={`flex items-center gap-3 text-[11px] pl-7 ${
                          isSelected
                            ? 'opacity-80'
                            : 'text-[var(--text-muted)]'
                        }`}
                      >
                        <span className="flex items-center gap-1">
                          <Clock className="w-3 h-3" />
                          {lecture.readTimeMin}m
                        </span>

                        <span className="flex items-center gap-1">
                          {qCount > 0 ? (
                            <>
                              <CheckCircle className={`w-3 h-3 ${isSelected ? 'text-emerald-700 dark:text-emerald-400' : 'text-emerald-400'}`} />
                              <span>{qCount} MCQs</span>
                            </>
                          ) : (
                            <>
                              <HelpCircle className="w-3 h-3 opacity-60" />
                              <span>Quiz Ready</span>
                            </>
                          )}
                        </span>
                      </div>
                    </button>
                  );
                })}
              </div>
            );
          })}
        </div>

        {/* Island Footer */}
        <div className="p-3 border-t border-[var(--border-island)] text-[11px] text-[var(--text-muted)] text-center font-medium">
          SST Term 5 • Computer Networks
        </div>
      </aside>
    </>
  );
};
