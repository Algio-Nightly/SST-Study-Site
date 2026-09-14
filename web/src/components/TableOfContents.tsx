import React, { useEffect, useState } from 'react';
import { AlignLeft, ArrowUp } from 'lucide-react';
import type { HeadingItem } from '../data/notesData';

interface TableOfContentsProps {
  headings: HeadingItem[];
}

export const TableOfContents: React.FC<TableOfContentsProps> = ({ headings }) => {
  const [activeId, setActiveId] = useState<string>('');

  useEffect(() => {
    const observer = new IntersectionObserver(
      (entries) => {
        entries.forEach((entry) => {
          if (entry.isIntersecting) {
            setActiveId(entry.target.id);
          }
        });
      },
      { rootMargin: '-80px 0% -60% 0%' }
    );

    const headingElements = document.querySelectorAll('h1[id], h2[id], h3[id]');
    headingElements.forEach((el) => observer.observe(el));

    return () => observer.disconnect();
  }, [headings]);

  const scrollToSection = (id: string) => {
    const el = document.getElementById(id);
    if (el) {
      el.scrollIntoView({ behavior: 'smooth', block: 'start' });
    }
  };

  const scrollToTop = () => {
    window.scrollTo({ top: 0, behavior: 'smooth' });
  };

  if (headings.length === 0) return null;

  return (
    <aside className="sticky top-20 w-64 xl:w-72 shrink-0 self-start hidden lg:flex flex-col bg-[var(--bg-island)] border border-[var(--border-island)] rounded-2xl shadow-xl p-4 h-[calc(100vh-6rem)]">
      
      {/* Island Header */}
      <div className="flex items-center justify-between gap-2 pb-3 mb-2 border-b border-[var(--border-island)]">
        <span className="text-xs font-bold uppercase tracking-wider text-[var(--text-muted)] flex items-center gap-1.5">
          <AlignLeft className="w-3.5 h-3.5 text-emerald-500" /> On This Page
        </span>
        <button
          onClick={scrollToTop}
          className="p-1 text-[var(--text-muted)] hover:text-[var(--text-heading)] rounded-lg hover:bg-[var(--bg-island-subtle)] transition-colors cursor-pointer"
          title="Scroll to top"
        >
          <ArrowUp className="w-3.5 h-3.5" />
        </button>
      </div>

      {/* Heading Tree Links */}
      <div className="flex-1 overflow-y-auto pr-1">
        <ul className="space-y-1 text-xs">
          {headings.map((h, i) => {
            const isActive = activeId === h.id;
            return (
              <li
                key={`${h.id}-${i}`}
                style={{ paddingLeft: `${Math.max(0, (h.level - 2) * 8)}px` }}
              >
                <button
                  onClick={() => scrollToSection(h.id)}
                  className={`text-left w-full truncate py-1.5 px-2 rounded-lg transition-colors cursor-pointer ${
                    isActive
                      ? 'bg-[var(--btn-primary-bg)] text-[var(--btn-primary-text)] font-bold shadow-xs'
                      : 'text-[var(--text-muted)] hover:text-[var(--text-heading)] hover:bg-[var(--bg-island-subtle)]'
                  }`}
                  title={h.title}
                >
                  {h.title}
                </button>
              </li>
            );
          })}
        </ul>
      </div>

      <div className="pt-3 border-t border-[var(--border-island)] text-[10px] text-[var(--text-muted)] text-center font-medium">
        {headings.length} sections outlined
      </div>
    </aside>
  );
};
