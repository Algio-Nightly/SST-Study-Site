import React, { useState } from 'react';
import ReactMarkdown from 'react-markdown';
import remarkGfm from 'remark-gfm';
import remarkMath from 'remark-math';
import rehypeKatex from 'rehype-katex';
import rehypeHighlight from 'rehype-highlight';
import { 
  Check, 
  Copy, 
  Sparkles, 
  Clock, 
  BookOpen, 
  CheckCircle2,
  Bookmark
} from 'lucide-react';
import type { Lecture } from '../data/notesData';

interface MarkdownViewerProps {
  lecture: Lecture;
  onOpenQuiz: () => void;
  status?: { isDone?: boolean; isReview?: boolean };
  onToggleDone?: () => void;
  onToggleReview?: () => void;
}

const CodeBlock = ({ inline, className, children, ...props }: any) => {
  const [copied, setCopied] = useState(false);
  const match = /language-(\w+)/.exec(className || '');
  const codeText = String(children).replace(/\n$/, '');

  const handleCopy = () => {
    navigator.clipboard.writeText(codeText);
    setCopied(true);
    setTimeout(() => setCopied(false), 2000);
  };

  // Rule: Small code with only one ` on either side is inline. Only multiline blocks become boxed cards.
  const hasMultipleLines = codeText.includes('\n');
  const isBlock = !inline && hasMultipleLines;

  if (isBlock) {
    const lang = match ? match[1].toUpperCase() : 'CODE / DIAGRAM';
    return (
      <div className="relative group my-6 rounded-2xl overflow-hidden border border-zinc-200 dark:border-[#2c2c34] bg-zinc-950 shadow-xl not-prose">
        <div className="flex items-center justify-between px-4 py-2.5 bg-zinc-900 border-b border-zinc-800 text-xs text-zinc-300 font-mono select-none">
          <span className="font-bold tracking-wider text-white flex items-center gap-2">
            <span className="w-2 h-2 rounded-full bg-emerald-400 inline-block" />
            {lang}
          </span>
          <button
            onClick={handleCopy}
            className="flex items-center gap-1.5 py-1 px-3 rounded-lg bg-white/10 hover:bg-white/20 text-white transition-colors text-xs font-sans font-medium cursor-pointer"
            title="Copy code"
          >
            {copied ? (
              <>
                <Check className="w-3.5 h-3.5 text-emerald-400" />
                <span className="text-emerald-400 font-semibold">Copied!</span>
              </>
            ) : (
              <>
                <Copy className="w-3.5 h-3.5 text-zinc-400" />
                <span>Copy</span>
              </>
            )}
          </button>
        </div>
        <pre className="p-4 overflow-x-auto text-xs sm:text-sm leading-relaxed font-mono text-zinc-100 bg-[#121214] m-0">
          <code className={className} {...props}>
            {children}
          </code>
        </pre>
      </div>
    );
  }

  // Strictly inline for small single-backtick code: `lo`, `eth0`, `dev eth1`, etc.
  return (
    <code className="inline-code-badge" {...props}>
      {children}
    </code>
  );
};

export const MarkdownViewer: React.FC<MarkdownViewerProps> = ({ 
  lecture, 
  onOpenQuiz,
  status,
  onToggleDone,
  onToggleReview
}) => {
  const isExtended = lecture.number >= 2 && lecture.number <= 8;

  return (
    <div className="w-full">
      
      {/* Header Banner inside Middle Island */}
      <div className="mb-8 p-6 sm:p-8 rounded-2xl bg-[var(--bg-island-subtle)] border border-[var(--border-island)] shadow-xs">
        <div className="flex flex-wrap items-center justify-between gap-4 mb-3">
          <span className="text-xs font-bold uppercase tracking-wider text-[var(--text-muted)] bg-[var(--bg-island)] px-3 py-1 rounded-full border border-[var(--border-island)]">
            {lecture.category}
          </span>
          <div className="flex flex-wrap items-center gap-2">
            {isExtended && (
              <span className="flex items-center gap-1.5 px-3 py-1 rounded-full text-xs font-semibold bg-[var(--bg-island)] text-[var(--text-heading)] border border-[var(--border-island)]">
                <Sparkles className="w-3.5 h-3.5 fill-current" /> Enhanced & Extended
              </span>
            )}

            {/* Mark for Review Toggle Button */}
            <button
              onClick={onToggleReview}
              className={`flex items-center gap-1.5 px-3.5 py-1.5 rounded-full text-xs font-semibold border transition-all cursor-pointer ${
                status?.isReview
                  ? 'bg-amber-500/15 text-amber-400 border-amber-500/40 shadow-xs'
                  : 'bg-[var(--bg-island)] text-[var(--text-muted)] border-[var(--border-island)] hover:text-[var(--text-heading)]'
              }`}
              title={status?.isReview ? 'Marked for review (click to unmark)' : 'Mark this lecture for review'}
            >
              <Bookmark className={`w-3.5 h-3.5 ${status?.isReview ? 'fill-current text-amber-400' : ''}`} />
              <span>{status?.isReview ? 'For Review' : 'Mark for Review'}</span>
            </button>

            {/* Mark as Done Toggle Button */}
            <button
              onClick={onToggleDone}
              className={`flex items-center gap-1.5 px-3.5 py-1.5 rounded-full text-xs font-bold border transition-all cursor-pointer ${
                status?.isDone
                  ? 'bg-emerald-500/20 text-emerald-400 border-emerald-500/40 shadow-xs'
                  : 'bg-[var(--bg-island)] text-[var(--text-muted)] border-[var(--border-island)] hover:text-[var(--text-heading)]'
              }`}
              title={status?.isDone ? 'Marked as done (click to unmark)' : 'Mark this lecture as done'}
            >
              <CheckCircle2 className={`w-3.5 h-3.5 ${status?.isDone ? 'text-emerald-400' : ''}`} />
              <span>{status?.isDone ? 'Completed' : 'Mark as Done'}</span>
            </button>

            {/* Topic Quiz Button */}
            <button
              onClick={onOpenQuiz}
              className="flex items-center gap-1.5 px-4 py-1.5 rounded-full text-xs font-bold bg-[var(--btn-primary-bg)] text-[var(--btn-primary-text)] hover:opacity-90 shadow-sm transition-all cursor-pointer"
            >
              <CheckCircle2 className="w-3.5 h-3.5" /> Topic Quiz
            </button>
          </div>
        </div>

        <h1 className="text-2xl sm:text-3xl lg:text-4xl font-extrabold text-[var(--text-heading)] tracking-tight mb-2">
          {lecture.title}
        </h1>
        <p className="text-sm sm:text-base text-[var(--text-body)] mb-4">
          {lecture.subtitle}
        </p>

        <div className="flex flex-wrap items-center gap-4 text-xs font-medium text-[var(--text-muted)] pt-3 border-t border-[var(--border-island)]">
          <span className="flex items-center gap-1.5">
            <Clock className="w-3.5 h-3.5" /> ~{lecture.readTimeMin} min read
          </span>
          <span>•</span>
          <span className="flex items-center gap-1.5">
            <BookOpen className="w-3.5 h-3.5" /> {lecture.wordCount.toLocaleString()} words
          </span>
          <span>•</span>
          <span>SST Curriculum</span>
        </div>
      </div>

      {/* Main Markdown Content with isolated Table & Code overflow containers */}
      <article className="markdown-body prose dark:prose-invert max-w-none prose-headings:scroll-mt-24 prose-headings:font-bold prose-h1:text-2xl prose-h2:text-xl prose-h2:border-b prose-h2:border-[var(--border-island)] prose-h2:pb-2 prose-h3:text-lg prose-img:rounded-xl text-[var(--text-body)]">
        <ReactMarkdown
          remarkPlugins={[remarkGfm, remarkMath]}
          rehypePlugins={[rehypeKatex, rehypeHighlight]}
          components={{
            pre: ({ children }) => <>{children}</>,
            code: CodeBlock,
            table: ({ children, ...props }) => (
              <div className="w-full my-6 overflow-x-auto rounded-xl border border-[var(--border-island)] bg-[var(--bg-island-subtle)] shadow-xs not-prose">
                <table className="w-full text-left border-collapse text-xs sm:text-sm text-[var(--text-body)]" {...props}>
                  {children}
                </table>
              </div>
            ),
            thead: ({ children, ...props }) => (
              <thead className="bg-[var(--bg-island)] text-[var(--text-heading)] border-b border-[var(--border-island)]" {...props}>
                {children}
              </thead>
            ),
            th: ({ children, ...props }) => (
              <th className="px-4 py-3 font-bold uppercase tracking-wider text-xs border-r last:border-r-0 border-[var(--border-island)] text-[var(--text-heading)]" {...props}>
                {children}
              </th>
            ),
            td: ({ children, ...props }) => (
              <td className="px-4 py-2.5 border-b border-r last:border-r-0 border-[var(--border-island)] text-[var(--text-body)] leading-normal" {...props}>
                {children}
              </td>
            ),
            tr: ({ children, ...props }) => (
              <tr className="hover:bg-[var(--bg-island)] transition-colors" {...props}>
                {children}
              </tr>
            ),
            h1: ({ children, ...props }) => {
              const slug = String(children).toLowerCase().replace(/[^a-z0-9]+/g, '-').replace(/(^-|-$)/g, '');
              return (
                <h1 id={slug} className="text-2xl sm:text-3xl font-extrabold mt-8 mb-4 tracking-tight text-[var(--text-heading)]" {...props}>
                  {children}
                </h1>
              );
            },
            h2: ({ children, ...props }) => {
              const slug = String(children).toLowerCase().replace(/[^a-z0-9]+/g, '-').replace(/(^-|-$)/g, '');
              return (
                <h2 id={slug} className="text-xl sm:text-2xl font-bold mt-8 mb-3 pb-2 border-b border-[var(--border-island)] tracking-tight text-[var(--text-heading)]" {...props}>
                  {children}
                </h2>
              );
            },
            h3: ({ children, ...props }) => {
              const slug = String(children).toLowerCase().replace(/[^a-z0-9]+/g, '-').replace(/(^-|-$)/g, '');
              return (
                <h3 id={slug} className="text-lg sm:text-xl font-semibold mt-6 mb-2 text-[var(--text-heading)]" {...props}>
                  {children}
                </h3>
              );
            }
          }}
        >
          {lecture.content}
        </ReactMarkdown>
      </article>

      {/* Bottom Study Progress & Quiz Callouts */}
      <div className="mt-16 space-y-4">
        {/* Lecture Study Status Card */}
        <div className="p-6 rounded-2xl bg-[var(--bg-island-subtle)] border border-[var(--border-island)] shadow-md flex flex-col sm:flex-row items-center justify-between gap-4">
          <div>
            <h4 className="text-sm sm:text-base font-bold text-[var(--text-heading)]">
              Lecture Study Status
            </h4>
            <p className="text-xs text-[var(--text-muted)] mt-0.5">
              Keep track of which lectures you've mastered and which need another review.
            </p>
          </div>

          <div className="flex items-center gap-3 w-full sm:w-auto">
            <button
              onClick={onToggleReview}
              className={`flex-1 sm:flex-initial flex items-center justify-center gap-2 px-4 py-2.5 rounded-xl text-xs font-semibold border transition-all cursor-pointer ${
                status?.isReview
                  ? 'bg-amber-500/15 text-amber-400 border-amber-500/40 shadow-xs'
                  : 'bg-[var(--bg-island)] text-[var(--text-muted)] border-[var(--border-island)] hover:text-[var(--text-heading)]'
              }`}
            >
              <Bookmark className={`w-4 h-4 ${status?.isReview ? 'fill-current text-amber-400' : ''}`} />
              <span>{status?.isReview ? 'Marked for Review' : 'Mark for Review'}</span>
            </button>

            <button
              onClick={onToggleDone}
              className={`flex-1 sm:flex-initial flex items-center justify-center gap-2 px-5 py-2.5 rounded-xl text-xs font-bold border transition-all cursor-pointer ${
                status?.isDone
                  ? 'bg-emerald-500/20 text-emerald-400 border-emerald-500/40 shadow-xs'
                  : 'bg-[var(--btn-secondary-bg)] text-[var(--btn-secondary-text)] border-[var(--btn-secondary-border)] hover:opacity-90'
              }`}
            >
              <CheckCircle2 className="w-4 h-4 text-emerald-400" />
              <span>{status?.isDone ? 'Completed' : 'Mark as Done'}</span>
            </button>
          </div>
        </div>

        {/* Bottom Quiz Callout */}
        <div className="p-6 sm:p-8 rounded-2xl bg-[var(--bg-island-subtle)] text-[var(--text-heading)] shadow-xl flex flex-col sm:flex-row items-center justify-between gap-6 border border-[var(--border-island)]">
          <div>
            <span className="text-xs font-semibold uppercase tracking-wider text-[var(--text-muted)] flex items-center gap-1 mb-1">
              <Sparkles className="w-3.5 h-3.5" /> Interactive Practice Available
            </span>
            <h3 className="text-lg sm:text-xl font-bold text-[var(--text-heading)]">Ready to test your knowledge?</h3>
            <p className="text-xs sm:text-sm text-[var(--text-muted)] mt-1.5 max-w-xl">
              Reinforce key concepts with comprehensive practice questions covering this topic. Includes instant feedback and detailed explanations.
            </p>
          </div>
          <button
            onClick={onOpenQuiz}
            className="w-full sm:w-auto px-6 py-3 rounded-xl font-bold text-xs sm:text-sm bg-[var(--btn-primary-bg)] text-[var(--btn-primary-text)] hover:opacity-90 transition-all flex items-center justify-center gap-2 shrink-0 cursor-pointer shadow-md"
          >
            <CheckCircle2 className="w-4 h-4" /> Start Lecture Quiz
          </button>
        </div>
      </div>

    </div>
  );
};
