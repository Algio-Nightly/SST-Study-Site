"""
Multi-Subject Notes Compiler for Scaler School of Technology Study Portal

Scans Notes/ subdirectories for each subject, strictly filtering ONLY Markdown (.md / .markdown) notes,
ignoring non-markdown files (PDFs, JSON, images), and compiles them into typed TypeScript datasets.
"""

from pathlib import Path
import re
import json

BASE_DIR = Path(__file__).parent.parent
NOTES_DIR = BASE_DIR / "Notes"
WEB_DATA_DIR = BASE_DIR / "web" / "src" / "data"
SUBJECTS_DATA_DIR = WEB_DATA_DIR / "subjects"

CATEGORIES_MAP = {
    "computer-networks": {
        2: "Foundations & Link Layer",
        3: "IP Addressing & Subnetting",
        4: "IP Addressing & Subnetting",
        5: "Graph Algorithms",
        6: "Graph Algorithms",
        7: "Routing & Forwarding",
        8: "Routing & Forwarding",
        9: "DNS & Web Applications",
        10: "Transport Layer & Sockets",
        11: "NAT, DHCP & Local Networks",
        12: "Troubleshooting & Diagnostics",
        13: "End-to-End Internet Architecture"
    },
    "classical-machine-learning": {
        1: "Foundations & Data Preparation",
        2: "Foundations & Data Preparation",
        3: "Linear Models & Optimization",
        4: "Linear Models & Optimization",
        5: "Linear Models & Optimization",
        6: "Model Complexity & Regularization",
        7: "Model Complexity & Regularization",
        8: "Classification & Non-Parametric Models",
        9: "Classification & Non-Parametric Models",
        10: "Applied Industry Labs"
    }
}

def slugify(text: str) -> str:
    text = text.lower()
    text = re.sub(r'[^a-z0-9\s-]', '', text)
    text = re.sub(r'[\s-]+', '-', text).strip('-')
    return text or "general"

def parse_markdown_note(file_path: Path, subject_id: str, index: int):
    content = file_path.read_text(encoding="utf-8", errors="replace")
    
    # Try extracting lecture number from filename (e.g. Lecture_02_Notes.md or 01_intro.md)
    num_match = re.search(r"(?:Lecture_|[Ll]ec_?|[Nn]ote_?)?(\d+)", file_path.name)
    lec_num = int(num_match.group(1)) if num_match else index
    
    lines = content.splitlines()
    title = f"Lecture {lec_num}"
    subtitle = ""
    
    for line in lines[:15]:
        if line.startswith("# ") and not title.startswith("Lecture "):
            title = line.replace("# ", "").strip()
        elif line.startswith("# ") and title.startswith("Lecture "):
            title = line.replace("# ", "").strip()
        elif line.startswith("## ") and not subtitle:
            subtitle = line.replace("## ", "").strip()
            
    if not subtitle:
        subtitle = file_path.stem.replace("_", " ")

    # Extract headings for Table of Contents
    headings = []
    for line in lines:
        match = re.match(r"^(#{2,3})\s+(.*)", line)
        if match:
            level = len(match.group(1))
            h_text = match.group(2).strip()
            h_id = slugify(h_text)
            headings.append({"id": h_id, "level": level, "title": h_text})
            
    words = len(content.split())
    read_time = max(1, round(words / 200))
    
    subj_categories = CATEGORIES_MAP.get(subject_id, {})
    category = subj_categories.get(lec_num, "General")
    
    file_id = f"lecture-{lec_num:02d}" if lec_num > 0 else slugify(file_path.stem)

    return {
        "id": file_id,
        "number": lec_num,
        "filename": file_path.name,
        "title": title,
        "subtitle": subtitle,
        "category": category,
        "wordCount": words,
        "readTimeMin": read_time,
        "headings": headings,
        "content": content
    }

def process_subject_folder(folder_path: Path):
    subject_id = slugify(folder_path.name)
    # Strictly filter ONLY Markdown files (.md or .markdown). Ignore all PDFs, JSON, images.
    md_files = sorted(
        [f for f in folder_path.iterdir() if f.is_file() and f.suffix.lower() in ('.md', '.markdown')],
        key=lambda x: [int(c) if c.isdigit() else c.lower() for c in re.split(r'(\d+)', x.name)]
    )
    
    lectures = [parse_markdown_note(f, subject_id, idx + 1) for idx, f in enumerate(md_files)]
    print(f"[{folder_path.name}] Found {len(md_files)} Markdown notes (strictly excluded {len(list(folder_path.iterdir())) - len(md_files)} non-markdown files).")
    return subject_id, lectures

def main():
    WEB_DATA_DIR.mkdir(parents=True, exist_ok=True)
    SUBJECTS_DATA_DIR.mkdir(parents=True, exist_ok=True)
    
    if not NOTES_DIR.exists():
        print(f"Notes directory {NOTES_DIR} does not exist.")
        return

    # Scan each subdirectory in Notes/
    subject_dirs = [d for d in NOTES_DIR.iterdir() if d.is_dir()]
    
    # If there are markdown files directly in Notes/, treat Notes/ as a subject
    direct_md = [f for f in NOTES_DIR.iterdir() if f.is_file() and f.suffix.lower() in ('.md', '.markdown')]
    
    all_subjects_found = {}
    
    for s_dir in subject_dirs:
        sub_id, lectures = process_subject_folder(s_dir)
        all_subjects_found[sub_id] = {
            "name": s_dir.name,
            "lectures": lectures
        }
        
        # Save to web/src/data/subjects/<subject-id>/notesData.ts
        target_dir = SUBJECTS_DATA_DIR / sub_id
        target_dir.mkdir(parents=True, exist_ok=True)
        
        ts_code = "// Auto-generated by tooling/generate_web_data.py\n"
        ts_code += "import type { Lecture } from '../../notesData';\n\n"
        ts_code += f"export const lecturesData: Lecture[] = {json.dumps(lectures, indent=2)};\n"
        
        (target_dir / "notesData.ts").write_text(ts_code, encoding="utf-8")

    # If Computer Networks is found, keep the root notesData.ts updated
    if "computer-networks" in all_subjects_found:
        cn_lectures = all_subjects_found["computer-networks"]["lectures"]
        ts_code = "// Auto-generated by tooling/generate_web_data.py\n"
        ts_code += "export interface HeadingItem {\n"
        ts_code += "  id: string;\n"
        ts_code += "  level: number;\n"
        ts_code += "  title: string;\n"
        ts_code += "}\n\n"
        ts_code += "export interface Lecture {\n"
        ts_code += "  id: string;\n"
        ts_code += "  number: number;\n"
        ts_code += "  filename: string;\n"
        ts_code += "  title: string;\n"
        ts_code += "  subtitle: string;\n"
        ts_code += "  category: string;\n"
        ts_code += "  wordCount: number;\n"
        ts_code += "  readTimeMin: number;\n"
        ts_code += "  headings: HeadingItem[];\n"
        ts_code += "  content: string;\n"
        ts_code += "  isDone?: boolean;\n"
        ts_code += "  isReview?: boolean;\n"
        ts_code += "}\n\n"
        ts_code += f"export const lecturesData: Lecture[] = {json.dumps(cn_lectures, indent=2)};\n"
        (WEB_DATA_DIR / "notesData.ts").write_text(ts_code, encoding="utf-8")
        print(f"Updated root notesData.ts with {len(cn_lectures)} Computer Networks lectures.")

    print("Multi-Subject notes generation complete.")

if __name__ == "__main__":
    main()
