import React, { useState, useRef, useEffect } from 'react';
import { 
  Network, 
  Search, 
  Sun, 
  Moon, 
  Sparkles,
  BookOpen, 
  CheckCircle2, 
  Menu, 
  X,
  ExternalLink,
  ChevronDown,
  Palette
} from 'lucide-react';
import type { Lecture } from '../data/notesData';
import type { ThemeMode } from '../types/theme';
import { AVAILABLE_THEMES } from '../types/theme';

interface NavbarProps {
  currentLecture: Lecture;
  activeTab: 'notes' | 'quiz';
  setActiveTab: (tab: 'notes' | 'quiz') => void;
  theme: ThemeMode;
  setTheme: (theme: ThemeMode) => void;
  onOpenSearch: () => void;
  isSidebarOpen: boolean;
  setIsSidebarOpen: (open: boolean) => void;
}

export const Navbar: React.FC<NavbarProps> = ({
  currentLecture,
  activeTab,
  setActiveTab,
  theme,
  setTheme,
  onOpenSearch,
  isSidebarOpen,
  setIsSidebarOpen
}) => {
  const [isThemeMenuOpen, setIsThemeMenuOpen] = useState(false);
  const themeMenuRef = useRef<HTMLDivElement>(null);

  // Close theme menu on outside click
  useEffect(() => {
    const handleClickOutside = (event: MouseEvent) => {
      if (themeMenuRef.current && !themeMenuRef.current.contains(event.target as Node)) {
        setIsThemeMenuOpen(false);
      }
    };
    document.addEventListener('mousedown', handleClickOutside);
    return () => document.removeEventListener('mousedown', handleClickOutside);
  }, []);

  const getThemeIcon = (t: ThemeMode) => {
    switch (t) {
      case 'charcoal':
        return <Moon className="w-4 h-4 text-zinc-100" />;
      case 'midnight':
        return <Sparkles className="w-4 h-4 text-blue-400" />;
      case 'light':
        return <Sun className="w-4 h-4 text-amber-500" />;
    }
  };

  const isDarkNav = theme === 'charcoal' || theme === 'midnight';

  return (
    <header className="sticky top-0 z-40 border-b border-[var(--border-nav)] bg-[var(--bg-nav)]/95 backdrop-blur transition-colors text-[var(--text-nav)]">
      <div className="w-full px-4 sm:px-6 lg:px-8 h-16 flex items-center justify-between gap-4">
        
        {/* Left: Mobile Toggle & Brand */}
        <div className="flex items-center gap-3">
          <button
            onClick={() => setIsSidebarOpen(!isSidebarOpen)}
            className="p-2 text-[var(--text-nav)] hover:bg-[var(--bg-nav-input)] rounded-xl lg:hidden cursor-pointer"
            title="Toggle Sidebar"
          >
            {isSidebarOpen ? <X className="w-5 h-5" /> : <Menu className="w-5 h-5" />}
          </button>

          <div className="flex items-center gap-2.5">
            <div className={`w-9 h-9 rounded-xl flex items-center justify-center font-bold shadow-md ${
              isDarkNav ? 'bg-white text-zinc-950' : 'bg-zinc-900 text-white'
            }`}>
              <Network className="w-5 h-5" />
            </div>
            <div>
              <div className="flex items-center gap-2">
                <span className="font-extrabold tracking-tight text-base sm:text-lg text-[var(--text-nav)]">
                  SST Computer Networks
                </span>
                <span className="hidden sm:inline-block px-2 py-0.5 text-[11px] font-bold bg-[var(--bg-nav-input)] text-[var(--text-nav)] rounded-full border border-[var(--border-nav-input)]">
                  Term 5
                </span>
              </div>
              <p className="text-xs text-zinc-400 hidden sm:block">
                Interactive University Notes & High-Bandwidth Quizzes
              </p>
            </div>
          </div>
        </div>

        {/* Center: Active Mode Tabs */}
        <div className="flex items-center bg-[var(--bg-nav-input)] p-1 rounded-xl border border-[var(--border-nav-input)]">
          <button
            onClick={() => setActiveTab('notes')}
            className={`flex items-center gap-1.5 px-3.5 py-1.5 rounded-lg text-xs sm:text-sm font-semibold transition-all cursor-pointer ${
              activeTab === 'notes'
                ? isDarkNav
                  ? 'bg-white text-zinc-950 shadow-sm font-bold'
                  : 'bg-zinc-900 text-white shadow-sm font-bold'
                : 'text-zinc-400 hover:text-white'
            }`}
          >
            <BookOpen className="w-4 h-4" />
            <span>Notes (L{currentLecture.number.toString().padStart(2, '0')})</span>
          </button>
          <button
            onClick={() => setActiveTab('quiz')}
            className={`flex items-center gap-1.5 px-3.5 py-1.5 rounded-lg text-xs sm:text-sm font-semibold transition-all cursor-pointer ${
              activeTab === 'quiz'
                ? isDarkNav
                  ? 'bg-white text-zinc-950 shadow-sm font-bold'
                  : 'bg-zinc-900 text-white shadow-sm font-bold'
                : 'text-zinc-400 hover:text-white'
            }`}
          >
            <CheckCircle2 className="w-4 h-4" />
            <span>Topic Quiz</span>
          </button>
        </div>

        {/* Right: Search, Theme Selector, External Links */}
        <div className="flex items-center gap-2.5">
          {/* Search Trigger */}
          <button
            onClick={onOpenSearch}
            className="flex items-center gap-2 px-3 py-1.5 text-xs sm:text-sm bg-[var(--bg-nav-input)] hover:opacity-90 rounded-xl border border-[var(--border-nav-input)] transition-all cursor-pointer text-[var(--text-nav-input)]"
            title="Search notes (Ctrl + K)"
          >
            <Search className="w-4 h-4 text-zinc-400" />
            <span className="hidden md:inline font-medium">Search...</span>
            <kbd className="hidden md:inline-block px-1.5 py-0.5 text-[10px] font-mono font-semibold bg-[#121214] border border-[#2c2c34] rounded text-zinc-400">
              Ctrl K
            </kbd>
          </button>

          {/* Interswappable Theme Switcher with Dropdown */}
          <div className="relative" ref={themeMenuRef}>
            <button
              onClick={() => setIsThemeMenuOpen(!isThemeMenuOpen)}
              className="flex items-center gap-1.5 px-3 py-1.5 rounded-xl border border-[var(--border-nav-input)] bg-[var(--bg-nav-input)] hover:opacity-90 text-[var(--text-nav-input)] transition-all text-xs font-semibold cursor-pointer"
              title="Change Theme"
            >
              <Palette className="w-3.5 h-3.5 text-zinc-400" />
              <span className="hidden sm:inline">
                {AVAILABLE_THEMES.find(t => t.id === theme)?.badge || 'Theme'}
              </span>
              <ChevronDown className={`w-3 h-3 text-zinc-400 transition-transform ${isThemeMenuOpen ? 'rotate-180' : ''}`} />
            </button>

            {isThemeMenuOpen && (
              <div className="absolute right-0 mt-2 w-56 p-1.5 rounded-2xl bg-[#1c1c21] border border-[#2c2c34] shadow-2xl z-50 animate-in fade-in zoom-in-95 duration-150 text-white">
                <div className="px-3 py-1.5 text-[10px] font-bold text-zinc-400 uppercase tracking-wider border-b border-[#282830] mb-1">
                  Interswappable Themes
                </div>
                {AVAILABLE_THEMES.map((item) => {
                  const isCurrent = item.id === theme;
                  return (
                    <button
                      key={item.id}
                      onClick={() => {
                        setTheme(item.id);
                        setIsThemeMenuOpen(false);
                      }}
                      className={`w-full text-left px-3 py-2 rounded-xl text-xs flex items-center justify-between transition-colors cursor-pointer ${
                        isCurrent
                          ? 'bg-white text-zinc-950 font-bold'
                          : 'text-zinc-300 hover:bg-[#25252b]'
                      }`}
                    >
                      <div className="flex items-center gap-2">
                        {getThemeIcon(item.id)}
                        <span>{item.name}</span>
                      </div>
                      {isCurrent && (
                        <span className="text-[10px] font-bold uppercase tracking-wider">Active</span>
                      )}
                    </button>
                  );
                })}
              </div>
            )}
          </div>

          {/* Quick Toggle Button (Cycles directly: Charcoal -> Midnight -> Light) */}
          <button
            onClick={() => {
              if (theme === 'charcoal') setTheme('midnight');
              else if (theme === 'midnight') setTheme('light');
              else setTheme('charcoal');
            }}
            className="p-2 bg-[var(--bg-nav-input)] hover:opacity-90 rounded-xl border border-[var(--border-nav-input)] transition-colors cursor-pointer text-[var(--text-nav-input)]"
            title={`Current: ${theme}. Click to quick-cycle theme.`}
          >
            {getThemeIcon(theme)}
          </button>

          {/* Source Link */}
          <a
            href="https://github.com/ayushsharmasst/Computer-Networks-Notes.git"
            target="_blank"
            rel="noreferrer"
            className="hidden sm:flex items-center gap-1 px-3 py-1.5 text-xs bg-[var(--bg-nav-input)] hover:opacity-90 rounded-xl transition-colors border border-[var(--border-nav-input)] text-[var(--text-nav-input)]"
            title="Original Repository"
          >
            <span>GitHub</span>
            <ExternalLink className="w-3 h-3 text-zinc-400" />
          </a>
        </div>

      </div>
    </header>
  );
};
