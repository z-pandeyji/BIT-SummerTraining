"""Load manga/manhwa pages from folders, CBZ/ZIP archives, and PDFs."""

from __future__ import annotations

import io
import zipfile
from pathlib import Path

from PIL import Image, UnidentifiedImageError

from manga_scanner.errors import CorruptSourceError, EmptySourceError, SourceNotFoundError, UnsupportedSourceError
from manga_scanner.models import PageInput
from manga_scanner.sorting import natural_sort_key

SUPPORTED_IMAGE_EXTENSIONS = {".png", ".jpg", ".jpeg", ".webp"}
SUPPORTED_ARCHIVE_EXTENSIONS = {".cbz", ".zip"}


def _open_rgb(data: bytes, name: str) -> Image.Image:
    try:
        img = Image.open(io.BytesIO(data))
        img.load()
        return img.convert("RGB")
    except (UnidentifiedImageError, Exception) as exc:
        raise CorruptSourceError(f"Cannot decode image: {name}") from exc


def _make_page(image: Image.Image, number: int, name: str) -> PageInput:
    return PageInput(page_number=number, source_name=name, image=image, width=image.width, height=image.height)


def _load_folder(path: Path) -> list[PageInput]:
    files = sorted(
        [f for f in path.iterdir() if f.is_file() and f.suffix.lower() in SUPPORTED_IMAGE_EXTENSIONS],
        key=lambda f: natural_sort_key(f.name),
    )
    if not files:
        raise EmptySourceError(f"No images found in folder: {path}")
    pages = []
    for i, f in enumerate(files, 1):
        img = _open_rgb(f.read_bytes(), f.name)
        pages.append(_make_page(img, i, f.name))
    return pages


def _load_archive(path: Path) -> list[PageInput]:
    try:
        zf = zipfile.ZipFile(path)
    except zipfile.BadZipFile as exc:
        raise CorruptSourceError(f"Cannot open archive: {path}") from exc

    with zf:
        names = sorted(
            [n for n in zf.namelist() if not n.endswith("/") and Path(n).suffix.lower() in SUPPORTED_IMAGE_EXTENSIONS],
            key=lambda n: natural_sort_key(Path(n).name),
        )
        if not names:
            raise EmptySourceError(f"No images found in archive: {path}")
        pages = []
        for i, name in enumerate(names, 1):
            data = zf.read(name)
            img = _open_rgb(data, name)
            pages.append(_make_page(img, i, name))
    return pages


def _load_pdf(path: Path) -> list[PageInput]:
    try:
        import fitz  # PyMuPDF
        doc = fitz.open(str(path))
    except Exception as exc:
        raise CorruptSourceError(f"Cannot open PDF: {path}") from exc

    pages = []
    with doc:
        if doc.page_count == 0:
            raise EmptySourceError(f"No pages in PDF: {path}")
        for i in range(doc.page_count):
            page = doc.load_page(i)
            pix = page.get_pixmap()
            img = Image.frombytes("RGB", (pix.width, pix.height), pix.samples)
            pages.append(_make_page(img, i + 1, f"page-{i + 1}"))
    return pages


def _load_single_image(path: Path) -> list[PageInput]:
    try:
        img = _open_rgb(path.read_bytes(), path.name)
    except CorruptSourceError:
        raise
    return [_make_page(img, 1, path.name)]


def load_pages(path: str | Path) -> list[PageInput]:
    """Load pages from an image folder, CBZ/ZIP archive, or PDF."""
    path = Path(path)

    if not path.exists():
        raise SourceNotFoundError(str(path))

    if path.is_dir():
        return _load_folder(path)

    suffix = path.suffix.lower()

    if suffix in SUPPORTED_ARCHIVE_EXTENSIONS:
        return _load_archive(path)

    if suffix == ".pdf":
        return _load_pdf(path)

    if suffix in SUPPORTED_IMAGE_EXTENSIONS:
        return _load_single_image(path)

    raise UnsupportedSourceError(f"Unsupported file type: {path}")
