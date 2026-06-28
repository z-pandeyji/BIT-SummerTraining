# Implementation Notes

Students must complete this file before submission.

## 1. Natural Sorting

Explain how your `natural_sort_key` handles names like `page2.png`, `page10.png`, `chapter-1-page-12.png`, and Unicode filenames.

`natural_sort_key` splits a filename wherever digits appear. Text parts are lowercased so case does not affect ordering, and digit parts are converted to integers so `page2.png` sorts before `page10.png`. Names with several numbers, like `chapter-1-page-12.png`, compare each text and number part in order. Unicode text stays as text, so filenames such as `ページ2.png` and `ページ10.png` still get their numeric pieces sorted correctly.

## 2. Page Loading

Explain how your code loads pages from:

- A folder
- A single image
- A `.cbz` or `.zip` archive
- A PDF

Also explain how your code handles empty, corrupt, or unsupported inputs.

- A folder: the loader reads only supported image files directly inside the folder, ignores subdirectories and non-image files, sorts them naturally, and returns one `PageInput` per image.
- A single image: the loader opens the file with Pillow, converts it to RGB, and stores the filename, width, height, and image object.
- A `.cbz` or `.zip` archive: the loader opens the archive without extracting it to disk, filters supported image entries, sorts them by natural page filename, and reads each image from bytes.
- A PDF: the loader opens the PDF with PyMuPDF, renders each page to a pixmap, converts it to a Pillow image, and names pages `page-1`, `page-2`, and so on.

Missing paths raise `SourceNotFoundError`. Unsupported extensions raise `UnsupportedSourceError`. Empty folders, archives, or PDFs raise `EmptySourceError`. Corrupt images, bad archives, and malformed PDFs raise `CorruptSourceError`.

## 3. Scanner Flow

Explain how `scan_source` uses the OCR engine and how it creates warnings.

`scan_source` loads the pages first, then calls the supplied OCR engine once for each page in order. If no engine is supplied, it uses `NullOcrEngine`, which returns no text. Each OCR block is stripped, and blank blocks are discarded. A page gets `No OCR text detected.` when no text remains, and it gets `Long vertical manhwa-style page.` when its height is at least 2.5 times its width.

## 4. Markdown Rendering

Explain how your Markdown output stays deterministic and why Markdown escaping is needed.

The Markdown renderer builds the report in a fixed order: title, source metadata, then page sections in scan order. Each page section always includes the source page name, dimensions, and OCR text area, and warnings are listed only when present. Markdown-sensitive characters are escaped in titles, OCR text, and warnings so text like `*hero*`, `[title]`, or `panel #1` is shown literally instead of being interpreted as Markdown formatting.

## 5. Debugging Log

Write 5-10 bullet points describing test failures you fixed while working.

- Confirmed that `pytest` was not available on PATH and used `.venv\Scripts\python.exe -m pytest` instead.
- Worked around Windows temp-directory permission errors by running pytest with `--basetemp=.pytest_tmp`.
- Fixed Markdown source paths so reports use deterministic forward slashes on Windows.
- Fixed archive sorting so nested archive entries are ordered by page filename, not by folder name first.
- Corrected a local sorting test typo where the expected result had a filename that was not in the input.
- Verified image, folder, archive, PDF, scanner, Markdown, and CLI behavior with the full test suite.
- Generated sample inputs and created `folder_scan.md`, `cbz_scan.md`, and `pdf_scan.md` with the CLI.

## 6. AI Usage

If you used AI, paste the three most useful prompts and explain what you changed after reading the answer.

- Prompt: "complete the task." I used the project notes and tests to identify that the assignment meant finishing the scanner stages and final submission files.
- Prompt: "Read the open walkthrough, checklist, implementation notes, and tests, then complete the remaining TODO behavior." After reviewing the answer and code, I kept the implementation scoped to sorting, loading, scanning, Markdown rendering, CLI verification, and notes.
- Prompt: "Run the full tests and fix the failures." After reading the failures, I changed archive sorting, normalized Markdown paths, and corrected the impossible local test expectation.
