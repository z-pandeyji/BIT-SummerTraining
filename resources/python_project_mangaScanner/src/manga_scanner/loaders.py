from __future__ import annotations

from pathlib import Path
import zipfile
from PIL import Image
import fitz  # PyMuPDF
import io

from manga_scanner.models import PageInput
from manga_scanner.errors import (
    SourceNotFoundError,
    UnsupportedSourceError,
    EmptySourceError,
    CorruptSourceError,
)
from manga_scanner.sorting import natural_sort_key

SUPPORTED_IMAGE_EXTENSIONS = {".png", ".jpg", ".jpeg", ".webp"}
SUPPORTED_ARCHIVE_EXTENSIONS = {".cbz", ".zip"}


def _is_image_file(path: Path) -> bool:
    return path.suffix.lower() in SUPPORTED_IMAGE_EXTENSIONS


def load_pages(path: str | Path) -> list[PageInput]:
    path = Path(path)

    # 1. exists check
    if not path.exists():
        raise SourceNotFoundError(str(path))

    # ---------------- IMAGE FILE ----------------
    if path.is_file() and _is_image_file(path):
        try:
            img = Image.open(path).convert("RGB")
        except Exception:
            raise CorruptSourceError(str(path))

        return [
            PageInput(
                page_number=1,
                source_name=path.name,
                image=img,
                width=img.width,
                height=img.height,
            )
        ]

    # ---------------- ARCHIVE (ZIP/CBZ) ----------------
    if path.is_file() and path.suffix.lower() in SUPPORTED_ARCHIVE_EXTENSIONS:
        try:
            with zipfile.ZipFile(path, "r") as zf:

                names = [
                    n for n in zf.namelist()
                    if not n.endswith("/") and Path(n).suffix.lower() in SUPPORTED_IMAGE_EXTENSIONS
                ]

                if not names:
                    raise EmptySourceError(str(path))

                names = sorted(
                    names,
                    key=lambda n: natural_sort_key(Path(n).name)
                )

                pages = []

                for i, name in enumerate(names, start=1):
                    try:
                        data = zf.read(name)
                        img = Image.open(io.BytesIO(data)).convert("RGB")
                    except Exception:
                        raise CorruptSourceError(str(path))

                    pages.append(
                        PageInput(
                            page_number=i,
                            source_name=name,
                            image=img,
                            width=img.width,
                            height=img.height,
                        )
                    )

                return pages

        except zipfile.BadZipFile:
            raise CorruptSourceError(str(path))

    # ---------------- FOLDER ----------------
    if path.is_dir():
        files = [
            p for p in path.iterdir()
            if p.is_file() and _is_image_file(p)
        ]

        files = sorted(files, key=lambda p: natural_sort_key(p.name))

        if not files:
            raise EmptySourceError(str(path))

        pages = []
        for i, file in enumerate(files, start=1):
            try:
                img = Image.open(file).convert("RGB")
            except Exception:
                raise CorruptSourceError(str(file))

            pages.append(
                PageInput(
                    page_number=i,
                    source_name=file.name,
                    image=img,
                    width=img.width,
                    height=img.height,
                )
            )

        return pages

    # ---------------- PDF ----------------
    if path.is_file() and path.suffix.lower() == ".pdf":
        try:
            doc = fitz.open(path)
        except Exception:
            raise CorruptSourceError(str(path))

        pages = []

        for i, page in enumerate(doc, start=1):
            pix = page.get_pixmap()
            img = Image.frombytes("RGB", [pix.width, pix.height], pix.samples)

            pages.append(
                PageInput(
                    page_number=i,
                    source_name=f"page-{i}",
                    image=img,
                    width=img.width,
                    height=img.height,
                )
            )

        if not pages:
            raise EmptySourceError(str(path))

        return pages

    # ---------------- UNSUPPORTED ----------------
    raise UnsupportedSourceError(str(path))