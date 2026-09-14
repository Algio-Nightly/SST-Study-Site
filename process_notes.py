"""
Computer Networks Notes & Quiz Schema Processor / Validator
Uses Python 3.13 with Pydantic and markdown-it-py under uv environment.
"""

from pathlib import Path
import re
import json
from typing import List, Optional, Literal, Union
from pydantic import BaseModel, Field


class QuizOption(BaseModel):
    id: str = Field(..., description="Option identifier e.g. A, B, C, D")
    text: str = Field(..., description="The option answer text")


class QuizQuestion(BaseModel):
    id: str
    type: Literal["single_choice", "multi_choice"] = Field(
        default="single_choice",
        description="Type of question: single_choice or multi_choice"
    )
    question: str
    code_snippet: Optional[str] = None
    options: List[QuizOption]
    # For single_choice: ['A']; for multi_choice: ['A', 'C']
    correct_option_ids: List[str]
    explanation: str
    difficulty: Literal["easy", "medium", "hard"] = "medium"
    subtopic: Optional[str] = None


class TopicQuiz(BaseModel):
    topic_id: str
    topic_title: str
    lecture_number: int
    questions: List[QuizQuestion] = Field(default_factory=list)


def parse_lecture_metadata(file_path: Path):
    content = file_path.read_text(encoding="utf-8")
    lines = content.splitlines()
    
    title = "Untitled Lecture"
    subtitle = ""
    for line in lines[:10]:
        if line.startswith("# "):
            title = line.replace("# ", "").strip()
        elif line.startswith("## "):
            subtitle = line.replace("## ", "").strip()
            
    # Extract headings
    headings = []
    for line in lines:
        match = re.match(r"^(#{2,3})\s+(.*)", line)
        if match:
            level = len(match.group(1))
            h_text = match.group(2).strip()
            # Clean emojis or numbers
            headings.append({"level": level, "title": h_text})
            
    word_count = len(content.split())
    estimated_read_time_minutes = max(1, round(word_count / 200))
    
    return {
        "filename": file_path.name,
        "title": title,
        "subtitle": subtitle,
        "word_count": word_count,
        "read_time_min": estimated_read_time_minutes,
        "headings": headings
    }


def validate_all_notes(notes_dir: Path):
    md_files = sorted(notes_dir.glob("Lecture_*_Notes.md"))
    print(f"Found {len(md_files)} lecture files in {notes_dir}:")
    
    manifest = []
    for f in md_files:
        meta = parse_lecture_metadata(f)
        manifest.append(meta)
        print(f"  [OK] {f.name} - {meta['title']} ({meta['word_count']} words, ~{meta['read_time_min']} min read)")
        
    return manifest


if __name__ == "__main__":
    base_dir = Path(__file__).parent.parent
    notes_dir = base_dir / "Notes"
    
    print("=== COMPUTER NETWORKS NOTES & QUIZ VALIDATOR (UV) ===")
    manifest = validate_all_notes(notes_dir)
    
    output_path = notes_dir / "lectures_manifest.json"
    output_path.write_text(json.dumps(manifest, indent=2), encoding="utf-8")
    print(f"\nManifest successfully generated at {output_path}")
