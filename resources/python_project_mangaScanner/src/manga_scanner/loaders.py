"""Load manga/manhwa pages from folders, CBZ/ZIP archives, and PDFs."""

from __future__ import annotations

from io import BytesIO
from pathlib import Path
import zipfile

import fitz
from PIL import Image, UnidentifiedImageError

from manga_scanner.errors import (
    CorruptSourceError,
    EmptySourceError,
    SourceNotFoundError,
    UnsupportedSourceError,
)
from manga_scanner.models import PageInput
from manga_scanner.sorting import natural_sort_key

SUPPORTED_IMAGE_EXTENSIONS = {".png", ".jpg", ".jpeg", ".webp"}
SUPPORTED_ARCHIVE_EXTENSIONS = {".cbz", ".zip"}


def _is_supported_image(path: str | Path) -> bool:
    return Path(path).suffix.lower() in SUPPORTED_IMAGE_EXTENSIONS


def _page_from_image(page_number: int, source_name: str, image: Image.Image) -> PageInput:
    rgb_image = image.convert("RGB")
    return PageInput(
        page_number=page_number,
        source_name=source_name,
        image=rgb_image,
        width=rgb_image.width,
        height=rgb_image.height,
    )


def _load_image_file(path: Path, page_number: int = 1, source_name: str | None = None) -> PageInput:
    try:
        with Image.open(path) as image:
            return _page_from_image(page_number, source_name or path.name, image)
    except (OSError, UnidentifiedImageError) as exc:
        raise CorruptSourceError(f"Could not read image: {path}") from exc


def _load_folder(path: Path) -> list[PageInput]:
    image_paths = sorted(
        (child for child in path.iterdir() if child.is_file() and _is_supported_image(child)),
        key=lambda child: natural_sort_key(child.name),
    )
    if not image_paths:
        raise EmptySourceError(f"No readable pages found in folder: {path}")

    return [_load_image_file(image_path, index, image_path.name) for index, image_path in enumerate(image_paths, 1)]


def _load_archive(path: Path) -> list[PageInput]:
    try:
        with zipfile.ZipFile(path) as archive:
            names = sorted(
                (
                    info.filename
                    for info in archive.infolist()
                    if not info.is_dir() and _is_supported_image(info.filename)
                ),
                key=lambda name: (natural_sort_key(Path(name).name), natural_sort_key(name)),
            )
            if not names:
                raise EmptySourceError(f"No readable pages found in archive: {path}")

            pages: list[PageInput] = []
            for index, name in enumerate(names, 1):
                try:
                    with archive.open(name) as file_obj:
                        data = file_obj.read()
                    with Image.open(BytesIO(data)) as image:
                        pages.append(_page_from_image(index, name, image))
                except (OSError, UnidentifiedImageError, zipfile.BadZipFile) as exc:
                    raise CorruptSourceError(f"Could not read image in archive {path}: {name}") from exc
            return pages
    except EmptySourceError:
        raise
    except zipfile.BadZipFile as exc:
        raise CorruptSourceError(f"Could not read archive: {path}") from exc


def _load_pdf(path: Path) -> list[PageInput]:
    try:
        document = fitz.open(path)
    except Exception as exc:  # PyMuPDF raises several exception types for malformed PDFs.
        raise CorruptSourceError(f"Could not read PDF: {path}") from exc

    try:
        if document.page_count == 0:
            raise EmptySourceError(f"No readable pages found in PDF: {path}")

        pages: list[PageInput] = []
        for index in range(document.page_count):
            page = document.load_page(index)
            pixmap = page.get_pixmap()
            mode = "RGB" if pixmap.alpha == 0 else "RGBA"
            image = Image.frombytes(mode, (pixmap.width, pixmap.height), pixmap.samples)
            pages.append(_page_from_image(index + 1, f"page-{index + 1}", image))
        return pages
    finally:
        document.close()


def load_pages(path: str | Path) -> list[PageInput]:
    """Load pages from an image folder, CBZ/ZIP archive, or PDF.

    Expected behavior:
    - Raise ``SourceNotFoundError`` when the path does not exist.
    - Raise ``UnsupportedSourceError`` for unsupported paths.
    - Raise ``EmptySourceError`` when no readable pages are found.
    - Return pages sorted by natural page order.

    TODO: Implement folder, archive, and PDF loading.
    """

    source = Path(path)
    if not source.exists():
        raise SourceNotFoundError(f"Source does not exist: {source}")

    if source.is_dir():
        return _load_folder(source)

    suffix = source.suffix.lower()
    if suffix in SUPPORTED_IMAGE_EXTENSIONS:
        return [_load_image_file(source)]
    if suffix in SUPPORTED_ARCHIVE_EXTENSIONS:
        return _load_archive(source)
    if suffix == ".pdf":
        return _load_pdf(source)

    raise UnsupportedSourceError(f"Unsupported source type: {source}")
