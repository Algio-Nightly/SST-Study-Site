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
  CheckCircle2
} from 'lucide-react';
import type { Lecture } from '../data/notesData';

interface MarkdownViewerProps {
  lecture: Lecture;
  onOpenQuiz: () => void;
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

export const MarkdownViewer: React.FC<MarkdownViewerProps> = ({ lecture, onOpenQuiz }) => {
  const isExtended = lecture.number >= 2 && lecture.number <= 8;

  return (
    <div className="w-full">
      
      {/* Header Banner inside Middle Island: Dark Charcoal Card with Crisp White Typography */}
      <div className="mb-8 p-6 sm:p-8 rounded-2xl bg-zinc-50 dark:bg-[#1a1a1f] border border-zinc-200 dark:border-[#2c2c34] shadow-xs">
        <div className="flex flex-wrap items-center justify-between gap-4 mb-3">
          <span className="text-xs font-bold uppercase tracking-wider text-zinc-700 dark:text-zinc-200 bg-zinc-200/80 dark:bg-zinc-800 px-3 py-1 rounded-full border border-zinc-300 dark:border-zinc-700/60">
            {lecture.category}
          </span>
          <div className="flex items-center gap-2">
            {isExtended && (
              <span className="flex items-center gap-1.5 px-3 py-1 rounded-full text-xs font-semibold bg-emerald-500/10 text-emerald-700 dark:text-emerald-300 border border-emerald-500/30">
                <Sparkles className="w-3.5 h-3.5 text-emerald-500 dark:text-emerald-400 fill-current" /> Enhanced & Extended
              </span>
            )}
            <button
              onClick={onOpenQuiz}
              className="flex items-center gap-1.5 px-4 py-1.5 rounded-full text-xs font-bold bg-zinc-900 text-white dark:bg-white dark:text-zinc-950 hover:bg-zinc-800 dark:hover:bg-zinc-100 shadow-sm transition-all cursor-pointer"
            >
              <CheckCircle2 className="w-3.5 h-3.5" /> Topic Quiz
            </button>
          </div>
        </div>

        <h1 className="text-2xl sm:text-3xl lg:text-4xl font-extrabold text-zinc-900 dark:text-white tracking-tight mb-2">
          {lecture.title}
        </h1>
        <p className="text-sm sm:text-base text-zinc-600 dark:text-zinc-300 mb-4">
          {lecture.subtitle}
        </p>

        <div className="flex flex-wrap items-center gap-4 text-xs font-medium text-zinc-500 dark:text-zinc-400 pt-3 border-t border-zinc-200 dark:border-[#2c2c34]">
          <span className="flex items-center gap-1.5">
            <Clock className="w-3.5 h-3.5 text-emerald-500" /> ~{lecture.readTimeMin} min read
          </span>
          <span>•</span>
          <span className="flex items-center gap-1.5">
            <BookOpen className="w-3.5 h-3.5 text-emerald-500" /> {lecture.wordCount.toLocaleString()} words
          </span>
          <span>•</span>
          <span>SST Term 5 Curriculum</span>
        </div>
      </div>

      {/* Main Markdown Content with isolated Table & Code overflow containers */}
      <article className="markdown-body prose prose-zinc dark:prose-invert max-w-none prose-headings:scroll-mt-24 prose-headings:font-bold prose-h1:text-2xl prose-h2:text-xl prose-h2:border-b prose-h2:border-zinc-200 dark:prose-h2:border-[#2c2c34] prose-h2:pb-2 prose-h3:text-lg prose-a:text-emerald-500 dark:prose-a:text-emerald-400 prose-img:rounded-xl">
        <ReactMarkdown
          remarkPlugins={[remarkGfm, remarkMath]}
          rehypePlugins={[rehypeKatex, rehypeHighlight]}
          components={{
            pre: ({ children }) => <>{children}</>,
            code: CodeBlock,
            table: ({ children, ...props }) => (
              <div className="w-full my-6 overflow-x-auto rounded-xl border border-zinc-200 dark:border-[#2c2c34] bg-zinc-50/60 dark:bg-[#16161a] shadow-xs not-prose">
                <table className="w-full text-left border-collapse text-xs sm:text-sm" {...props}>
                  {children}
                </table>
              </div>
            ),
            thead: ({ children, ...props }) => (
              <thead className="bg-zinc-100/90 dark:bg-[#232328] text-zinc-900 dark:text-white border-b border-zinc-200 dark:border-[#2c2c34]" {...props}>
                {children}
              </thead>
            ),
            th: ({ children, ...props }) => (
              <th className="px-4 py-3 font-bold uppercase tracking-wider text-xs border-r last:border-r-0 border-zinc-200 dark:border-[#2c2c34] text-zinc-900 dark:text-white" {...props}>
                {children}
              </th>
            ),
            td: ({ children, ...props }) => (
              <td className="px-4 py-2.5 border-b border-r last:border-r-0 border-zinc-200/80 dark:border-[#2c2c34] text-zinc-700 dark:text-zinc-300 leading-normal" {...props}>
                {children}
              </td>
            ),
            tr: ({ children, ...props }) => (
              <tr className="hover:bg-zinc-100/60 dark:hover:bg-zinc-800/40 transition-colors" {...props}>
                {children}
              </tr>
            ),
            h1: ({ children, ...props }) => {
              const slug = String(children).toLowerCase().replace(/[^a-z0-9]+/g, '-').replace(/(^-|-$)/g, '');
              return (
                <h1 id={slug} className="text-2xl sm:text-3xl font-extrabold mt-8 mb-4 tracking-tight text-zinc-900 dark:text-white" {...props}>
                  {children}
                </h1>
              );
            },
            h2: ({ children, ...props }) => {
              const slug = String(children).toLowerCase().replace(/[^a-z0-9]+/g, '-').replace(/(^-|-$)/g, '');
              return (
                <h2 id={slug} className="text-xl sm:text-2xl font-bold mt-8 mb-3 pb-2 border-b border-zinc-200 dark:border-[#2c2c34] tracking-tight text-zinc-900 dark:text-white" {...props}>
                  {children}
                </h2>
              );
            },
            h3: ({ children, ...props }) => {
              const slug = String(children).toLowerCase().replace(/[^a-z0-9]+/g, '-').replace(/(^-|-$)/g, '');
              return (
                <h3 id={slug} className="text-lg sm:text-xl font-semibold mt-6 mb-2 text-zinc-800 dark:text-zinc-100" {...props}>
                  {children}
                </h3>
              );
            }
          }}
        >
          {lecture.content}
        </ReactMarkdown>
      </article>

      {/* Bottom Quiz Callout - Sleek Dark Card with Crisp White Button (Like the image) */}
      <div className="mt-16 p-6 sm:p-8 rounded-2xl bg-zinc-900 text-white shadow-xl flex flex-col sm:flex-row items-center justify-between gap-6 border border-zinc-800 dark:border-[#2c2c34]">
        <div>
          <span className="text-xs font-semibold uppercase tracking-wider text-emerald-400 flex items-center gap-1 mb-1">
            <Sparkles className="w-3.5 h-3.5" /> 20 Comprehensive MCQs Available
          </span>
          <h3 className="text-lg sm:text-xl font-bold text-white">Ready to test your knowledge?</h3>
          <p className="text-xs sm:text-sm text-zinc-300 mt-1.5 max-w-xl">
            Attempt the interactive multiple-choice quiz for {lecture.title.replace(/^Lecture\s+\d+:\s*/, '')}.
          </p>
        </div>
        <button
          onClick={onOpenQuiz}
          className="shrink-0 px-6 py-3 rounded-xl font-bold text-sm bg-white hover:bg-zinc-100 text-zinc-950 shadow-lg shadow-black/40 hover:scale-[1.02] transition-all cursor-pointer"
        >
          Launch Topic Quiz →
        </button>
      </div>

    </div>
  );
};
