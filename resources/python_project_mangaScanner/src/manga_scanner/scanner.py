"""High-level scan orchestration."""

from __future__ import annotations

from pathlib import Path

from manga_scanner.loaders import load_pages
from manga_scanner.models import MangaScan, OcrEngine, PageScan
from manga_scanner.ocr import NullOcrEngine

MANHWA_HEIGHT_THRESHOLD = 500


def _source_type(path: Path) -> str:
    if path.is_dir():
        return "folder"
    suffix = path.suffix.lower()
    if suffix == ".pdf":
        return "pdf"
    if suffix in {".cbz", ".zip"}:
        return "archive"
    return "image"


def scan_source(path: str | Path, ocr_engine: OcrEngine | None = None) -> MangaScan:
    """Scan a source and return OCR-ready Markdown data."""
    path = Path(path)
    engine = ocr_engine or NullOcrEngine()
    pages_input = load_pages(path)

    source_type = _source_type(path)
    title = path.stem if path.is_file() else path.name

    page_scans = []
    for page in pages_input:
        raw_blocks = engine.recognize(page)
        text_blocks = tuple(b.strip() for b in raw_blocks if b.strip())

        warnings = []
        if not text_blocks:
            warnings.append("No OCR text detected.")
        if page.height >= MANHWA_HEIGHT_THRESHOLD:
            warnings.append("Long vertical manhwa-style page.")

        page_scans.append(PageScan(
            page_number=page.page_number,
            source_name=page.source_name,
            width=page.width,
            height=page.height,
            text_blocks=text_blocks,
            warnings=tuple(warnings),
        ))

    return MangaScan(
        title=title,
        source_path=path,
        source_type=source_type,
        pages=tuple(page_scans),
    )
