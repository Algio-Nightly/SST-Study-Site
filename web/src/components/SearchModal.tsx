import React, { useState, useEffect, useRef } from 'react';
import { Search, X, BookOpen, ChevronRight, Hash } from 'lucide-react';
import { lecturesData } from '../data/notesData';
import type { Lecture } from '../data/notesData';

interface SearchModalProps {
  isOpen: boolean;
  onClose: () => void;
  onSelectLecture: (lectureId: string, headingId?: string) => void;
}

interface SearchResult {
  lecture: Lecture;
  headingMatch?: { id: string; title: string };
}

export const SearchModal: React.FC<SearchModalProps> = ({
  isOpen,
  onClose,
  onSelectLecture
}) => {
  const [query, setQuery] = useState('');
  const [selectedIndex, setSelectedIndex] = useState(0);
  const inputRef = useRef<HTMLInputElement>(null);

  useEffect(() => {
    if (isOpen) {
      setTimeout(() => inputRef.current?.focus(), 50);
      setQuery('');
      setSelectedIndex(0);
    }
  }, [isOpen]);

  // Global Esc & Ctrl+K handler
  useEffect(() => {
    const handleKeyDown = (e: KeyboardEvent) => {
      if ((e.ctrlKey || e.metaKey) && e.key.toLowerCase() === 'k') {
        e.preventDefault();
      }
      if (e.key === 'Escape' && isOpen) {
        onClose();
      }
    };
    window.addEventListener('keydown', handleKeyDown);
    return () => window.removeEventListener('keydown', handleKeyDown);
  }, [isOpen, onClose]);

  if (!isOpen) return null;

  // Search matching
  const results: SearchResult[] = [];
  const q = query.trim().toLowerCase();

  if (q.length > 0) {
    lecturesData.forEach((lec) => {
      // Check title or subtitle
      if (
        lec.title.toLowerCase().includes(q) ||
        lec.subtitle.toLowerCase().includes(q) ||
        lec.category.toLowerCase().includes(q) ||
        `lecture ${lec.number}`.includes(q)
      ) {
        results.push({ lecture: lec });
      }

      // Check headings
      lec.headings.forEach((h) => {
        if (h.title.toLowerCase().includes(q)) {
          results.push({ lecture: lec, headingMatch: h });
        }
      });
    });
  }

  const handleSelect = (item: SearchResult) => {
    onSelectLecture(item.lecture.id, item.headingMatch?.id);
    onClose();
  };

  const handleKeyDown = (e: React.KeyboardEvent) => {
    if (e.key === 'ArrowDown') {
      e.preventDefault();
      setSelectedIndex((prev) => (prev + 1) % Math.max(1, results.length));
    } else if (e.key === 'ArrowUp') {
      e.preventDefault();
      setSelectedIndex((prev) => (prev - 1 + results.length) % Math.max(1, results.length));
    } else if (e.key === 'Enter' && results[selectedIndex]) {
      e.preventDefault();
      handleSelect(results[selectedIndex]);
    }
  };

  return (
    <div className="fixed inset-0 z-50 flex items-start justify-center pt-20 px-4 bg-black/60 backdrop-blur-xs">
      <div 
        onClick={(e) => e.stopPropagation()}
        className="w-full max-w-xl rounded-2xl bg-white dark:bg-[#1c1c21] border border-zinc-200 dark:border-[#2c2c34] shadow-2xl overflow-hidden animate-in fade-in zoom-in-95 duration-150"
      >
        {/* Search Input */}
        <div className="flex items-center px-4 border-b border-zinc-200 dark:border-[#2c2c34]">
          <Search className="w-5 h-5 text-zinc-400 shrink-0 mr-3" />
          <input
            ref={inputRef}
            type="text"
            placeholder="Search notes, protocols, subnetting, algorithms..."
            value={query}
            onChange={(e) => {
              setQuery(e.target.value);
              setSelectedIndex(0);
            }}
            onKeyDown={handleKeyDown}
            className="w-full py-4 bg-transparent text-zinc-900 dark:text-white placeholder-zinc-400 focus:outline-none text-sm sm:text-base font-medium"
          />
          <button
            onClick={onClose}
            className="p-1.5 rounded-lg text-zinc-400 hover:text-zinc-600 dark:hover:text-zinc-200 cursor-pointer"
          >
            <X className="w-4 h-4" />
          </button>
        </div>

        {/* Results List */}
        <div className="max-h-96 overflow-y-auto p-2">
          {q.length === 0 ? (
            <div className="py-8 text-center text-xs text-zinc-400">
              Type keywords such as "OSI", "Subnetting", "Dijkstra", "RIP", or "BGP"
            </div>
          ) : results.length === 0 ? (
            <div className="py-8 text-center text-xs text-zinc-400">
              No matching lecture sections found for "{query}"
            </div>
          ) : (
            results.slice(0, 15).map((item, idx) => {
              const isSelected = idx === selectedIndex;
              return (
                <button
                  key={`${item.lecture.id}-${item.headingMatch?.id || 'main'}-${idx}`}
                  onClick={() => handleSelect(item)}
                  className={`w-full text-left p-3 rounded-xl transition-colors flex items-center justify-between gap-2 cursor-pointer ${
                    isSelected
                      ? 'bg-zinc-900 text-white dark:bg-white dark:text-zinc-950 font-bold shadow-sm'
                      : 'hover:bg-zinc-100 dark:hover:bg-[#25252b] text-zinc-800 dark:text-zinc-200'
                  }`}
                >
                  <div className="flex items-center gap-3 min-w-0">
                    <div className={`p-1.5 rounded-lg shrink-0 ${
                      isSelected 
                        ? 'bg-zinc-800 text-zinc-100 dark:bg-zinc-900 dark:text-white' 
                        : 'bg-zinc-100 dark:bg-[#282830] text-zinc-500 dark:text-zinc-400'
                    }`}>
                      {item.headingMatch ? <Hash className="w-4 h-4" /> : <BookOpen className="w-4 h-4" />}
                    </div>

                    <div className="truncate">
                      <div className="text-xs sm:text-sm font-semibold truncate">
                        {item.headingMatch ? item.headingMatch.title : item.lecture.title}
                      </div>
                      <div className={`text-[11px] truncate ${
                        isSelected ? 'text-zinc-300 dark:text-zinc-700' : 'text-zinc-400'
                      }`}>
                        Lecture {item.lecture.number} • {item.lecture.category}
                      </div>
                    </div>
                  </div>

                  <ChevronRight className={`w-4 h-4 shrink-0 ${isSelected ? 'text-white dark:text-zinc-950' : 'text-zinc-400'}`} />
                </button>
              );
            })
          )}
        </div>

        {/* Footer shortcuts */}
        <div className="px-4 py-2.5 bg-zinc-50 dark:bg-[#141417] border-t border-zinc-200 dark:border-[#2c2c34] flex items-center justify-between text-[11px] text-zinc-400 font-mono">
          <span>Navigate with ↑ ↓ and Enter</span>
          <span>Esc to close</span>
        </div>
      </div>
    </div>
  );
};
