"""High-level scan orchestration."""

from __future__ import annotations

from pathlib import Path

from manga_scanner.loaders import load_pages
from manga_scanner.models import MangaScan, PageScan, OcrEngine


class NullOcrEngine:
    def recognize(self, page):
        return []


def scan_source(path: str | Path, ocr_engine: OcrEngine | None = None) -> MangaScan:
    path = Path(path)

    pages = load_pages(path)

    if ocr_engine is None:
        ocr_engine = NullOcrEngine()

    page_scans = []

    for page in pages:
        text_blocks = tuple(
            text.strip()
            for text in ocr_engine.recognize(page)
            if text.strip()
        )

        warnings = []

        if not text_blocks:
            warnings.append("No OCR text detected.")

        if page.height >= page.width * 2.5:
            warnings.append("Long vertical manhwa-style page.")

        page_scans.append(
            PageScan(
                page_number=page.page_number,
                source_name=page.source_name,
                width=page.width,
                height=page.height,
                text_blocks=text_blocks,
                warnings=tuple(warnings),
            )
        )

    ext = path.suffix.lower()

    if ext in {".cbz", ".zip"}:
        source_type = "archive"
    elif ext == ".pdf":
        source_type = "pdf"
    elif path.is_file():
        source_type = "image"
    else:
        source_type = "folder"

    return MangaScan(
        title=path.stem,
        source_path=path,
        source_type=source_type,
        pages=tuple(page_scans),
    )