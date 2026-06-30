# Progress Checklist

Tick each item as you complete it.

## Setup

- [x] Python 3.9 or newer works
- [x] Virtual environment is activated
- [x] `python -m pip install -e ".[dev]"` completed
- [x] `pytest --collect-only -q` shows tests

## Stage 1: Sorting

- [x] `pytest tests/test_sorting.py -v` passes
- [x] `pytest tests/test_sorting_extended.py -v` passes
- [x] I can explain natural sorting

## Stage 2: Loading

- [x] Single image loading works
- [x] Folder loading works
- [x] CBZ/ZIP loading works
- [x] PDF loading works
- [x] Empty/corrupt/unsupported inputs raise correct errors
- [x] Loader tests pass

## Stage 3: Scanning

- [x] OCR engine is called once per page
- [x] Blank OCR text is removed
- [x] Blank page warning works
- [x] Long vertical page warning works
- [x] Scanner tests pass

## Stage 4: Markdown

- [x] Markdown title and metadata work
- [x] Page sections work
- [x] OCR text list works
- [x] Warning section works
- [x] Markdown escaping works
- [x] Markdown tests pass

## Stage 5: CLI

- [x] `manga-scan samples/image_folder --output folder_scan.md` works
- [x] `manga-scan samples/demo_cbz.zip --output cbz_scan.md` works
- [x] `manga-scan samples/demo.pdf --output pdf_scan.md` works
- [x] CLI tests pass

## Final

- [x] `pytest` passes
- [x] I filled `IMPLEMENTATION_NOTES.md`
- [x] I can explain every TODO I completed
