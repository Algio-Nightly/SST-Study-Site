import sys
from pathlib import Path
from pypdf import PdfReader
import json

# Force UTF-8 output
sys.stdout.reconfigure(encoding='utf-8')

notes_dir = Path(r"c:\Scaler School of Technology\Computer Networks\Handwritten Notes")
pdfs = sorted(notes_dir.glob("*.pdf"))

results = {}
for pdf in pdfs:
    reader = PdfReader(pdf)
    file_pages = []
    total_text = ""
    for idx, page in enumerate(reader.pages):
        text = page.extract_text() or ""
        file_pages.append({"page": idx + 1, "text": text.strip()})
        if text.strip():
            total_text += f"\n--- Page {idx+1} ---\n" + text.strip()
            
    results[pdf.name] = {
        "page_count": len(reader.pages),
        "has_text": len(total_text.strip()) > 0,
        "text_length": len(total_text),
        "content": total_text
    }
    print(f"[{pdf.name}] {len(reader.pages)} pages, text chars: {len(total_text)}")

out_path = Path("tooling/handwritten_extracted.json")
out_path.write_text(json.dumps(results, indent=2, ensure_ascii=False), encoding="utf-8")
print(f"\nSaved extracted content to {out_path}")
