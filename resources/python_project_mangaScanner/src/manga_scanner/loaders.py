"""Load manga/manhwa pages from folders, CBZ/ZIP archives, and PDFs."""

from __future__ import annotations


import fitz 
from pathlib import Path

import zipfile
from io import BytesIO

from PIL import Image
from manga_scanner.models import PageInput
from manga_scanner.errors import (
    SourceNotFoundError,
    UnsupportedSourceError,
    EmptySourceError,
)
from manga_scanner.sorting import natural_sort_key

SUPPORTED_IMAGE_EXTENSIONS = {".png", ".jpg", ".jpeg", ".webp"}
SUPPORTED_ARCHIVE_EXTENSIONS = {".cbz", ".zip"}
def load_pages(path: str | Path) -> list[PageInput]:
    path = Path(path)

    if not path.exists():
        raise SourceNotFoundError(str(path))

    files = []

    if path.is_dir():
        files = [
            f for f in path.iterdir()
            if f.suffix.lower() in SUPPORTED_IMAGE_EXTENSIONS
        ]

    else:
        ext = path.suffix.lower()

        if ext in SUPPORTED_IMAGE_EXTENSIONS:
            files = [path]

        elif ext in SUPPORTED_ARCHIVE_EXTENSIONS:
            result = []

            with zipfile.ZipFile(path, "r") as archive:
                names = [
                    name
                    for name in archive.namelist()
                    if Path(name).suffix.lower() in SUPPORTED_IMAGE_EXTENSIONS
                ]

                names.sort(key=natural_sort_key)

                for i, name in enumerate(names, 1):
                    with archive.open(name) as fp:
                        img = Image.open(BytesIO(fp.read()))
                        img.load()

                    result.append(
                        PageInput(
                            page_number=i,
                            source_name=name,   # IMPORTANT
                            image=img,
                            width=img.width,
                            height=img.height,
                        )
                    )
            

            return result

        elif ext == ".pdf":
            result = []

            pdf = fitz.open(path)

            for i in range(len(pdf)):
                page = pdf[i]
                pix = page.get_pixmap()

                img = Image.frombytes(
                    "RGB",
                    (pix.width, pix.height),
                    pix.samples
                )

                result.append(
                    PageInput(
                        page_number=i + 1,
                        source_name=f"page-{i + 1}",
                        image=img,
                        width=img.width,
                        height=img.height,
                    )
                )

            pdf.close()
            return result

        else:
            raise UnsupportedSourceError(str(path))
    if not files:
        raise EmptySourceError("No readable pages found")

    files.sort(key=lambda f: natural_sort_key(f.name))

    result = []

    for i, f in enumerate(files, 1):
        img = Image.open(BytesIO(fp.read()))
        img.load()
        img = img.convert("RGB")


        result.append(
            PageInput(
                page_number=i,
                source_name=f.name,
                image=img,
                width=img.width,
                height=img.height,
            )
        )

    return result
    