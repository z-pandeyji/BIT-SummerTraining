from pathlib import Path

from manga_scanner.loaders import load_pages
from manga_scanner.models import MangaScan, PageScan


class DefaultOcrEngine:
    def recognize(self, page):
        return []


def scan_source(path, ocr_engine=None):
    source = Path(path)

    # default OCR engine
    if ocr_engine is None:
        ocr_engine = DefaultOcrEngine()

    # load pages
    pages = load_pages(source)

    scanned_pages = []

    for page in pages:
        raw_text = ocr_engine.recognize(page)

        # clean OCR output
        text_blocks = tuple(
            t.strip() for t in raw_text if t.strip()
        )

        warnings = []

        # ✅ FIXED: vertical page detection
        if page.height / page.width >= 2.5:
            warnings.append("Long vertical manhwa-style page.")

        # OCR warning
        if not text_blocks:
            warnings.append("No OCR text detected.")

        scanned_pages.append(
            PageScan(
                page_number=page.page_number,
                source_name=page.source_name,
                width=page.width,
                height=page.height,
                text_blocks=text_blocks,
                warnings=tuple(warnings),
            )
        )

    # ---------------- SOURCE TYPE DETECTION ----------------
    suffix = source.suffix.lower()

    if source.is_file():
        if suffix == ".pdf":
            source_type = "pdf"
        elif suffix in [".png", ".jpg", ".jpeg", ".webp"]:
            source_type = "image"
        else:
            source_type = "archive"
    else:
        source_type = "folder"

    # ---------------- TITLE FIX ----------------
    title = source.name
    for ext in [".png", ".jpg", ".jpeg", ".webp", ".cbz", ".zip", ".pdf"]:
        if title.lower().endswith(ext):
            title = title[: -len(ext)]
            break

    # ---------------- RETURN ----------------
    return MangaScan(
        title=title,
        source_path=source,
        source_type=source_type,
        pages=tuple(scanned_pages),
    )