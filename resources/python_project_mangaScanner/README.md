# Manga/Manhwa Markdown Scanner

## 🎉 NEW: Real OCR Support!

This project now supports **real OCR text detection** using EasyOCR!

### Without OCR (Fast)
```bash
manga-scan samples/image_folder --output result.md
```

### With OCR (Detects Text)
```bash
manga-scan samples/image_folder --output result.md --ocr
```

---

This is a Python assignment scaffold. Students complete the TODO-marked functions so the scanner can read manga/manhwa sources and produce a Markdown report.

Start here:

```text
START_HERE.md
```

Then read:

- `PROJECT_WALKTHROUGH.md`
- `TRY_SAMPLE_INPUTS.md`
- `PROGRESS_CHECKLIST.md`
- **`REAL_OCR_GUIDE.md`** ← NEW! Real OCR usage guide

## What The Scanner Supports

- Image folders containing `.png`, `.jpg`, `.jpeg`, or `.webp` pages
- `.cbz` and `.zip` comic archives
- PDF files rendered into page images
- Pluggable OCR through a simple `OcrEngine` interface
- Markdown output with source metadata, page dimensions, OCR text, and warnings

## Student Setup

Python 3.9 or newer is required.

### Basic Installation (Without OCR)
```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install -e ".[dev]"
pytest
```

### With Real OCR Support
```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install -e ".[dev]"
python -m pip install easyocr
pytest
```

First OCR run will download models (~100MB).

Run one focused test file:

```bash
pytest tests/test_markdown.py -v
```

Run the CLI after implementing the TODOs:

```bash
python scripts/create_demo_cbz.py
manga-scan samples/demo_cbz.zip --output scan.md
```

### With OCR:

```bash
manga-scan samples/demo_cbz.zip --output scan_with_ocr.md --ocr
```

### OCR Language Support:

```bash
# English (default)
manga-scan samples/demo.pdf --output result.md --ocr

# Japanese
manga-scan samples/demo.pdf --output result.md --ocr --lang ja

# Korean
manga-scan samples/demo.pdf --output result.md --ocr --lang ko
```

See `REAL_OCR_GUIDE.md` for complete OCR documentation.

## Student Task

Complete the TODOs in:

- `src/manga_scanner/sorting.py`
- `src/manga_scanner/loaders.py`
- `src/manga_scanner/scanner.py`
- `src/manga_scanner/markdown.py`

Do not change the tests just to make them pass. Use the tests as a specification.

Before submitting, fill in `IMPLEMENTATION_NOTES.md`. Your teacher may ask you to explain your code.

## Optional Real PDF Test

Most tests generate small images/PDFs automatically. If your teacher gives you a local manga PDF path, run:

```bash
REAL_MANGA_PDF="/path/to/manga.pdf" pytest
```
