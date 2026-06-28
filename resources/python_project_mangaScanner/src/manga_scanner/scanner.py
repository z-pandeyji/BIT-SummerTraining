"""High-level scanning workflow."""

from __future__ import annotations

from pathlib import Path

from manga_scanner.loaders import SUPPORTED_ARCHIVE_EXTENSIONS, SUPPORTED_IMAGE_EXTENSIONS, load_pages
from manga_scanner.models import MangaScan, OcrEngine, PageInput, PageScan
from manga_scanner.ocr import NullOcrEngine


def _source_type(path: Path) -> str:
    if path.is_dir():
        return "folder"
    suffix = path.suffix.lower()
    if suffix in SUPPORTED_IMAGE_EXTENSIONS:
        return "image"
    if suffix in SUPPORTED_ARCHIVE_EXTENSIONS:
        return "archive"
    if suffix == ".pdf":
        return "pdf"
    return "unknown"


def _scan_page(page: PageInput, ocr_engine: OcrEngine) -> PageScan:
    text_blocks = tuple(block.strip() for block in ocr_engine.recognize(page) if block.strip())

    warnings: list[str] = []
    if not text_blocks:
        warnings.append("No OCR text detected.")
    if page.height >= page.width * 2.5:
        warnings.append("Long vertical manhwa-style page.")

    return PageScan(
        page_number=page.page_number,
        source_name=page.source_name,
        width=page.width,
        height=page.height,
        text_blocks=text_blocks,
        warnings=tuple(warnings),
    )


def scan_source(path: str | Path, ocr_engine: OcrEngine | None = None) -> MangaScan:
    """Load pages, run OCR, and return a complete scan result."""

    source = Path(path)
    engine = ocr_engine or NullOcrEngine()
    pages = load_pages(source)
    page_scans = tuple(_scan_page(page, engine) for page in pages)

    return MangaScan(
        title=source.stem if source.is_file() else source.name,
        source_path=source,
        source_type=_source_type(source),
        pages=page_scans,
    )
