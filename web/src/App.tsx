import { useState, useEffect } from 'react';
import { lecturesData } from './data/notesData';
import { quizzesRegistry } from './data/quizzesData';
import type { ThemeMode } from './types/theme';
import { Navbar } from './components/Navbar';
import { Sidebar } from './components/Sidebar';
import { MarkdownViewer } from './components/MarkdownViewer';
import { TableOfContents } from './components/TableOfContents';
import { QuizEngine } from './components/QuizEngine';
import { SearchModal } from './components/SearchModal';

export function App() {
  const [selectedLectureId, setSelectedLectureId] = useState<string>('lecture-02');
  const [activeTab, setActiveTab] = useState<'notes' | 'quiz'>('notes');
  
  // Default to 'charcoal' (dark charcoal islands with white space between blocks!)
  const [theme, setTheme] = useState<ThemeMode>(() => {
    const saved = localStorage.getItem('sst_theme') as ThemeMode;
    if (saved && (saved === 'charcoal' || saved === 'midnight' || saved === 'light')) {
      return saved;
    }
    return 'charcoal';
  });

  const [isSidebarOpen, setIsSidebarOpen] = useState<boolean>(false);
  const [isSearchOpen, setIsSearchOpen] = useState<boolean>(false);

  // Sync theme to root html element and localStorage
  useEffect(() => {
    localStorage.setItem('sst_theme', theme);
    const root = document.documentElement;

    if (theme === 'light') {
      root.classList.remove('dark', 'theme-charcoal', 'theme-midnight');
      root.classList.add('theme-light');
      root.setAttribute('data-theme', 'light');
    } else if (theme === 'midnight') {
      root.classList.remove('theme-light', 'theme-charcoal');
      root.classList.add('dark', 'theme-midnight');
      root.setAttribute('data-theme', 'midnight');
    } else {
      // charcoal: space between blocks is white, blocks are dark charcoal
      root.classList.remove('theme-light', 'theme-midnight');
      root.classList.add('dark', 'theme-charcoal');
      root.setAttribute('data-theme', 'charcoal');
    }
  }, [theme]);

  // Global keyboard shortcut for search (Ctrl/Cmd + K)
  useEffect(() => {
    const handleKeyDown = (e: KeyboardEvent) => {
      if ((e.ctrlKey || e.metaKey) && e.key.toLowerCase() === 'k') {
        e.preventDefault();
        setIsSearchOpen(prev => !prev);
      }
    };
    window.addEventListener('keydown', handleKeyDown);
    return () => window.removeEventListener('keydown', handleKeyDown);
  }, []);

  const currentLecture = lecturesData.find(l => l.id === selectedLectureId) || lecturesData[0];
  const currentQuiz = quizzesRegistry[selectedLectureId];

  const handleSelectLecture = (lectureId: string, headingId?: string) => {
    setSelectedLectureId(lectureId);
    if (headingId) {
      setActiveTab('notes');
      setTimeout(() => {
        const el = document.getElementById(headingId);
        if (el) {
          el.scrollIntoView({ behavior: 'smooth', block: 'start' });
        }
      }, 100);
    }
  };

  return (
    <div className="min-h-screen flex flex-col bg-[var(--bg-page)] text-[var(--text-body)] transition-colors duration-200">
      
      {/* Top Navbar */}
      <Navbar
        currentLecture={currentLecture}
        activeTab={activeTab}
        setActiveTab={setActiveTab}
        theme={theme}
        setTheme={setTheme}
        onOpenSearch={() => setIsSearchOpen(true)}
        isSidebarOpen={isSidebarOpen}
        setIsSidebarOpen={setIsSidebarOpen}
      />

      {/* Main 3-Island Layout spanning full page width */}
      {/* The background of this container (the space between the blocks) is white in Charcoal, blacker in Midnight */}
      <div className="w-full px-3 sm:px-4 lg:px-6 py-4 flex-1 flex gap-4 lg:gap-6 items-start bg-[var(--bg-page)] transition-colors duration-200">
        
        {/* Left Island: Course Navigation (Sticky Dark Block) */}
        <Sidebar
          currentLectureId={selectedLectureId}
          onSelectLecture={handleSelectLecture}
          isOpen={isSidebarOpen}
          onCloseMobile={() => setIsSidebarOpen(false)}
        />

        {/* Center Island: Main Content (Largest Dark Block) */}
        <main className="flex-1 min-w-0 bg-[var(--bg-island)] border border-[var(--border-island)] rounded-2xl shadow-xl p-6 sm:p-10 transition-colors overflow-hidden">
          {activeTab === 'notes' ? (
            <MarkdownViewer
              lecture={currentLecture}
              onOpenQuiz={() => setActiveTab('quiz')}
            />
          ) : (
            <QuizEngine
              quiz={currentQuiz}
              lecture={currentLecture}
              onBackToNotes={() => setActiveTab('notes')}
            />
          )}
        </main>

        {/* Right Island: Table of Contents (Sticky Dark Block) */}
        {activeTab === 'notes' && (
          <TableOfContents headings={currentLecture.headings} />
        )}

      </div>

      {/* Global Search Modal */}
      <SearchModal
        isOpen={isSearchOpen}
        onClose={() => setIsSearchOpen(false)}
        onSelectLecture={handleSelectLecture}
      />

    </div>
  );
}

export default App;
