import React from 'react';
import ReactMarkdown from 'react-markdown';
import remarkGfm from 'remark-gfm';
import remarkMath from 'remark-math';
import rehypeKatex from 'rehype-katex';
import rehypeHighlight from 'rehype-highlight';

interface QuizMarkdownProps {
  content: string;
  className?: string;
  asSpan?: boolean;
}

export const QuizMarkdown: React.FC<QuizMarkdownProps> = ({
  content,
  className = '',
  asSpan = false,
}) => {
  if (!content) return null;

  return (
    <div className={`quiz-markdown-root ${asSpan ? 'inline' : 'block'} ${className}`}>
      <ReactMarkdown
        remarkPlugins={[remarkGfm, remarkMath]}
        rehypePlugins={[rehypeKatex, rehypeHighlight]}
        components={{
          // Override p when inside a button or heading to avoid invalid HTML DOM nesting
          p: ({ children }) =>
            asSpan ? (
              <span className="inline leading-relaxed">{children}</span>
            ) : (
              <p className="leading-relaxed my-1 text-inherit">{children}</p>
            ),
          pre: ({ children }) => <>{children}</>,
          code: ({ children, className: codeClass, ...props }: any) => {
            const codeString = String(children);
            const isMultiline = codeString.includes('\n');
            if (isMultiline && !asSpan) {
              return (
                <div className="my-3 rounded-xl overflow-hidden border border-zinc-200 dark:border-[#2c2c34] bg-zinc-950 shadow-md not-prose">
                  <pre className="p-3.5 overflow-x-auto text-xs sm:text-sm font-mono leading-relaxed text-zinc-100 m-0">
                    <code className={codeClass} {...props}>
                      {children}
                    </code>
                  </pre>
                </div>
              );
            }
            return (
              <code
                className="font-mono text-xs sm:text-[0.875em] px-1.5 py-0.5 rounded bg-[var(--code-inline-bg)] text-[var(--code-inline-text)] border border-[var(--code-inline-border)] font-semibold inline align-baseline"
                {...props}
              >
                {children}
              </code>
            );
          },
          strong: ({ children }) => (
            <strong className="font-bold text-[var(--text-heading)]">{children}</strong>
          ),
          em: ({ children }) => (
            <em className="italic text-[var(--text-body)]">{children}</em>
          ),
          ul: ({ children }) => (
            <ul className="list-disc list-inside my-2 space-y-1">{children}</ul>
          ),
          ol: ({ children }) => (
            <ol className="list-decimal list-inside my-2 space-y-1">{children}</ol>
          ),
          li: ({ children }) => <li className="leading-relaxed">{children}</li>,
        }}
      >
        {content}
      </ReactMarkdown>
    </div>
  );
};
