"""High-level scan orchestration."""

from __future__ import annotations

from pathlib import Path

from manga_scanner.loaders import load_pages
from manga_scanner.models import MangaScan, OcrEngine, PageScan
from manga_scanner.ocr import NullOcrEngine


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
        ocr_engine = NullOcrEngine()
    
    # Load pages
    page_inputs = load_pages(path)
    
    # Determine source type
    if path.is_dir():
        source_type = "folder"
        title = path.name
    elif path.suffix.lower() in {".cbz", ".zip"}:
        source_type = "archive"
        title = path.stem
    elif path.suffix.lower() == ".pdf":
        source_type = "pdf"
        title = path.stem
    else:
        source_type = "image"
        title = path.stem
    
    # Scan each page
    page_scans = []
    for page_input in page_inputs:
        # Run OCR
        ocr_result = ocr_engine.recognize(page_input)
        
        # Strip empty blocks
        text_blocks = tuple(block.strip() for block in ocr_result if block.strip())
        
        # Generate warnings
        warnings = []
        if not text_blocks:
            warnings.append("No OCR text detected.")
        
        # Check for tall manhwa-style pages (height >= 2.5x width)
        if page_input.height >= page_input.width * 2.5:
            warnings.append("Long vertical manhwa-style page.")
        
        page_scans.append(PageScan(
            page_number=page_input.page_number,
            source_name=page_input.source_name,
            width=page_input.width,
            height=page_input.height,
            text_blocks=text_blocks,
            warnings=tuple(warnings),
        ))
    
    return MangaScan(
        title=title,
        source_path=path,
        source_type=source_type,
        pages=tuple(page_scans),
    )
