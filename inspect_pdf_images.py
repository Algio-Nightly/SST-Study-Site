from pathlib import Path
from pypdf import PdfReader
import json

notes_dir = Path(r"c:\Scaler School of Technology\Computer Networks\Handwritten Notes")
pdfs = sorted(notes_dir.glob("*.pdf"))

summary = {}
for pdf in pdfs:
    reader = PdfReader(pdf)
    text_content = []
    image_count = 0
    for idx, page in enumerate(reader.pages):
        t = page.extract_text() or ""
        if t.strip():
            text_content.append(f"--- Page {idx+1} ---\n{t.strip()}")
        image_count += len(page.images)
        
    summary[pdf.name] = {
        "pages": len(reader.pages),
        "text_pages": len(text_content),
        "total_images": image_count,
        "text": "\n\n".join(text_content)
    }

output_path = Path("tooling/pdf_summary.json")
output_path.write_text(json.dumps(summary, indent=2, ensure_ascii=False), encoding="utf-8")
print("Saved summary to tooling/pdf_summary.json")
for k, v in summary.items():
    print(f"{k}: {v['pages']} pages, {v['text_pages']} text pages, {v['total_images']} images, text len: {len(v['text'])}")
