import { useState, useEffect } from 'react';
import { lecturesData } from './data/notesData';
import { quizzesRegistry } from './data/quizzesData';
import { getSubjectData, getSubjectMeta } from './data/subjects';
import type { ThemeMode } from './types/theme';
import { loadAllSubjectLectureStatuses, saveLectureStatus } from './utils/quizStorage';
import { Navbar } from './components/Navbar';
import { Sidebar } from './components/Sidebar';
import { MarkdownViewer } from './components/MarkdownViewer';
import { TableOfContents } from './components/TableOfContents';
import { QuizEngine } from './components/QuizEngine';
import { SearchModal } from './components/SearchModal';
import { SubjectsHub } from './components/SubjectsHub';

export function App() {
  // Navigation view: 'hub' (Main Page) or 'subject' (3-island learning view)
  const [currentView, setCurrentView] = useState<'hub' | 'subject'>(() => {
    if (typeof window !== 'undefined' && window.location.hash.includes('subject')) {
      return 'subject';
    }
    return 'hub';
  });

  const [currentSubjectId, setCurrentSubjectId] = useState<string>('computer-networks');
  const [selectedLectureId, setSelectedLectureId] = useState<string>('lecture-02');
  const [activeTab, setActiveTab] = useState<'notes' | 'quiz'>('notes');
  
  // Default to 'oled-slate' (Sleek dark theme with pitch-black page and subtle slate cards)
  const [theme, setTheme] = useState<ThemeMode>(() => {
    const saved = localStorage.getItem('sst_theme') as ThemeMode;
    if (saved && (saved === 'oled-slate' || saved === 'midnight' || saved === 'light')) {
      return saved;
    }
    return 'oled-slate';
  });

  const [isSidebarOpen, setIsSidebarOpen] = useState<boolean>(false);
  const [isSearchOpen, setIsSearchOpen] = useState<boolean>(false);

  // Sync theme to root html element and localStorage
  useEffect(() => {
    localStorage.setItem('sst_theme', theme);
    const root = document.documentElement;

    root.classList.remove('dark', 'theme-light', 'theme-midnight', 'theme-oled-slate');
    root.setAttribute('data-theme', theme);

    if (theme === 'light') {
      root.classList.add('theme-light');
    } else if (theme === 'midnight') {
      root.classList.add('dark', 'theme-midnight');
    } else {
      // oled-slate (default)
      root.classList.add('dark', 'theme-oled-slate');
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

  // Hash-based URL routing synchronization for sharing and refresh
  useEffect(() => {
    const syncFromHash = () => {
      const hash = window.location.hash;
      if (hash.startsWith('#/subject/')) {
        const parts = hash.replace('#/subject/', '').split('?');
        const subId = parts[0] || 'computer-networks';
        setCurrentSubjectId(subId);
        setCurrentView('subject');

        const sData = getSubjectData(subId);
        const fallbackLec = sData?.lectures[0]?.id || 'lecture-01';

        if (parts[1]) {
          const params = new URLSearchParams(parts[1]);
          const lec = params.get('lecture');
          const tab = params.get('tab') as 'notes' | 'quiz' | null;
          setSelectedLectureId(lec || fallbackLec);
          if (tab && (tab === 'notes' || tab === 'quiz')) setActiveTab(tab);
        } else {
          setSelectedLectureId(fallbackLec);
        }
      } else {
        setCurrentView('hub');
      }
    };

    syncFromHash();
    window.addEventListener('hashchange', syncFromHash);
    return () => window.removeEventListener('hashchange', syncFromHash);
  }, []);

  // Update hash when navigating inside a subject
  const updateHash = (view: 'hub' | 'subject', subId: string, lecId: string, tab: 'notes' | 'quiz') => {
    if (view === 'hub') {
      window.location.hash = '#/';
    } else {
      window.location.hash = `#/subject/${subId}?lecture=${lecId}&tab=${tab}`;
    }
  };

  const currentSubjectData = getSubjectData(currentSubjectId);
  const currentSubjectMeta = getSubjectMeta(currentSubjectId);

  const lectures = currentSubjectData?.lectures || lecturesData;
  const quizzes = currentSubjectData?.quizzes || quizzesRegistry;

  const currentLecture = lectures.find(l => l.id === selectedLectureId) || lectures[0];
  const currentQuiz = quizzes[selectedLectureId];

  const handleSelectSubject = (subjectId: string, initialTab: 'notes' | 'quiz' = 'notes', lectureId?: string) => {
    setCurrentSubjectId(subjectId);
    setCurrentView('subject');
    setActiveTab(initialTab);
    const subData = getSubjectData(subjectId);
    const defaultLec = subData?.lectures[0]?.id || 'lecture-01';
    const targetLec = lectureId || defaultLec;
    setSelectedLectureId(targetLec);
    updateHash('subject', subjectId, targetLec, initialTab);
    window.scrollTo({ top: 0, behavior: 'smooth' });
  };

  const handleNavigateToHub = () => {
    setCurrentView('hub');
    updateHash('hub', currentSubjectId, selectedLectureId, activeTab);
    window.scrollTo({ top: 0, behavior: 'smooth' });
  };

  const handleSelectLecture = (lectureId: string, headingId?: string) => {
    setSelectedLectureId(lectureId);
    setCurrentView('subject');
    updateHash('subject', currentSubjectId, lectureId, activeTab);
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

  const handleTabChange = (newTab: 'notes' | 'quiz') => {
    setActiveTab(newTab);
    updateHash('subject', currentSubjectId, selectedLectureId, newTab);
  };

  const [lectureStatuses, setLectureStatuses] = useState<Record<string, { isDone?: boolean; isReview?: boolean }>>(() => {
    return loadAllSubjectLectureStatuses(currentSubjectId);
  });

  // Keep lecture statuses in sync when switching subjects
  useEffect(() => {
    setLectureStatuses(loadAllSubjectLectureStatuses(currentSubjectId));
  }, [currentSubjectId]);

  const handleToggleLectureDone = (lectureId: string) => {
    const current = lectureStatuses[lectureId]?.isDone;
    const updated = saveLectureStatus(currentSubjectId, lectureId, { isDone: !current });
    setLectureStatuses({ ...updated });
  };

  const handleToggleLectureReview = (lectureId: string) => {
    const current = lectureStatuses[lectureId]?.isReview;
    const updated = saveLectureStatus(currentSubjectId, lectureId, { isReview: !current });
    setLectureStatuses({ ...updated });
  };

  return (
    <div className="min-h-screen flex flex-col bg-[var(--bg-page)] text-[var(--text-body)] transition-colors duration-200">
      
      {/* Top Navbar */}
      <Navbar
        currentView={currentView}
        onNavigateToHub={handleNavigateToHub}
        currentSubjectTitle={currentSubjectMeta?.title || 'Computer Networks'}
        currentLecture={currentLecture}
        activeTab={activeTab}
        setActiveTab={handleTabChange}
        theme={theme}
        setTheme={setTheme}
        onOpenSearch={() => setIsSearchOpen(true)}
        isSidebarOpen={isSidebarOpen}
        setIsSidebarOpen={setIsSidebarOpen}
      />

      {/* Main View Router */}
      {currentView === 'hub' ? (
        <div className="flex-1 flex flex-col bg-[var(--bg-page)] transition-colors duration-200">
          <SubjectsHub
            onSelectSubject={handleSelectSubject}
            cnLectureIds={lectures.map(l => l.id)}
          />
        </div>
      ) : (
        /* Main 3-Island Layout spanning full page width for Subject View */
        <div className="w-full px-3 sm:px-4 lg:px-6 py-4 flex-1 flex gap-4 lg:gap-6 items-start bg-[var(--bg-page)] transition-colors duration-200">
          
          {/* Left Island: Course Navigation (Sticky Dark Block) */}
          <Sidebar
            lectures={lectures}
            quizzes={quizzes}
            subjectTitle={currentSubjectMeta?.title}
            currentLectureId={selectedLectureId}
            onSelectLecture={handleSelectLecture}
            isOpen={isSidebarOpen}
            onCloseMobile={() => setIsSidebarOpen(false)}
            lectureStatuses={lectureStatuses}
          />

          {/* Center Island: Main Content (Largest Dark Block) */}
          <main className="flex-1 min-w-0 bg-[var(--bg-island)] border border-[var(--border-island)] rounded-2xl shadow-xl p-6 sm:p-10 transition-colors overflow-hidden">
            {activeTab === 'notes' ? (
              <MarkdownViewer
                lecture={currentLecture}
                onOpenQuiz={() => handleTabChange('quiz')}
                status={lectureStatuses[currentLecture.id]}
                onToggleDone={() => handleToggleLectureDone(currentLecture.id)}
                onToggleReview={() => handleToggleLectureReview(currentLecture.id)}
              />
            ) : (
              <QuizEngine
                subjectId={currentSubjectId}
                quiz={currentQuiz}
                lecture={currentLecture}
                onBackToNotes={() => handleTabChange('notes')}
              />
            )}
          </main>

          {/* Right Island: Table of Contents (Sticky Dark Block) */}
          {activeTab === 'notes' && (
            <TableOfContents headings={currentLecture.headings} />
          )}

        </div>
      )}

      {/* Global Search Modal */}
      <SearchModal
        isOpen={isSearchOpen}
        onClose={() => setIsSearchOpen(false)}
        onSelectLecture={handleSelectLecture}
        lectures={lectures}
      />

    </div>
  );
}

export default App;
