import sys
from pathlib import Path
from pypdf import PdfReader

notes_dir = Path(r"c:\Scaler School of Technology\Computer Networks\Handwritten Notes")
pdfs = sorted(notes_dir.glob("*.pdf"))

print(f"Found {len(pdfs)} PDF files in {notes_dir}:")
for pdf in pdfs:
    reader = PdfReader(pdf)
    num_pages = len(reader.pages)
    sample_text = ""
    for page in reader.pages:
        txt = page.extract_text() or ""
        if txt.strip():
            sample_text += txt + "\n"
    
    print(f"\n==========================================")
    print(f"FILE: {pdf.name} ({num_pages} pages)")
    print(f"Extracted characters: {len(sample_text)}")
    if sample_text:
        print("SAMPLE PREVIEW (first 400 chars):")
        print(sample_text[:400].strip())
    else:
        print("NO DIRECT TEXT EXTRACTED (likely scanned images or drawing canvas).")
