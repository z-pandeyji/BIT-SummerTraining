"""Load manga/manhwa pages from folders, CBZ/ZIP archives, and PDFs."""

from __future__ import annotations

from pathlib import Path
from PIL import Image

from manga_scanner.models import PageInput
from manga_scanner.errors import (
    SourceNotFoundError,
    UnsupportedSourceError,
    EmptySourceError,
)
SUPPORTED_IMAGE_EXTENSIONS = {".png", ".jpg", ".jpeg", ".webp"}
SUPPORTED_ARCHIVE_EXTENSIONS = {".cbz", ".zip"}


def load_pages(path: str | Path) -> list[PageInput]:
    path = Path(path)

    if not path.exists():
        raise SourceNotFoundError(str(path))

    if path.is_file():
      ext = path.suffix.lower()

    if (
        
        ext not in SUPPORTED_IMAGE_EXTENSIONS
        and ext not in SUPPORTED_ARCHIVE_EXTENSIONS
        and ext != ".pdf"
    ):
        raise UnsupportedSourceError(str(path))

    if ext in SUPPORTED_IMAGE_EXTENSIONS:
        image = Image.open(path)

        return [
            PageInput(
                page_number=1,
                source_name=path.name,
                image=image,
                width=image.width,
                height=image.height,
            )
        ]
    if ext in SUPPORTED_ARCHIVE_EXTENSIONS:
        return []

    if ext == ".pdf":
        return []
    raise EmptySourceError(str(path))