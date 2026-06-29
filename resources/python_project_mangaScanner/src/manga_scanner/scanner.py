"""High-level scan orchestration."""

from __future__ import annotations

from pathlib import Path

from manga_scanner.models import MangaScan, OcrEngine, PageScan


def scan_source(path: str | Path, ocr_engine: OcrEngine | None = None) -> MangaScan:
    """Scan a source and return OCR-ready Markdown data.

    Expected behavior:
    - Use ``load_pages`` to read the source.
    - Use ``NullOcrEngine`` when ``ocr_engine`` is ``None``.
    - Strip empty OCR blocks.
    - Add a warning when a page has no OCR text.
    - Add a warning for very tall manhwa-style pages.

    TODO: Implement scan orchestration.
    """
    path = Path(path)

    if ocr_engine is None:
        from manga_scanner.ocr import NullOcrEngine
        ocr_engine = NullOcrEngine()

    from manga_scanner.loaders import load_pages

    pages = load_pages(path)
    scanned_pages = []
    ext = path.suffix.lower()
    
    if ext in [".png", ".jpg", ".jpeg", ".webp"]:
        source_type = "image"
    elif ext == ".pdf":
        source_type = "pdf"
    elif ext in [".cbz", ".zip"]:
        source_type = "archive"
    else:
        source_type = "unknown"
    
    for i, page in enumerate(pages, start=1):
        text_blocks = tuple(
            text.strip()
            for text in ocr_engine.recognize(page)
            if text.strip()
        )

        warnings = []

        if not text_blocks:
            warnings.append("No OCR text detected.")

        if page.height >= page.width * 3:
                warnings.append("Very tall page detected.")

        scanned_pages.append(
            PageScan(
                page_number=i,
                source_name=page.source_name,
                width=page.width,
                height=page.height,
                text_blocks=text_blocks,
                warnings=tuple(warnings),
            )
        )
    
        
    return MangaScan(
        title=path.stem,
        source_path=path,
        source_type=source_type,
        pages=tuple(scanned_pages),
    )
