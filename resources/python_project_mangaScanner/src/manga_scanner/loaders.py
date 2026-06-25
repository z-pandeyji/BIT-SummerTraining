"""Load manga/manhwa pages from folders, CBZ/ZIP archives, and PDFs."""

from __future__ import annotations

import re
import zipfile
from pathlib import Path

import fitz
from PIL import Image

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


def load_pages(path: str | Path) -> list[PageInput]:
    """Load pages from an image folder, CBZ/ZIP archive, or PDF.

    Expected behavior:
    - Raise ``SourceNotFoundError`` when the path does not exist.
    - Raise ``UnsupportedSourceError`` for unsupported paths.
    - Raise ``EmptySourceError`` when no readable pages are found.
    - Return pages sorted by natural page order.

    TODO: Implement folder, archive, and PDF loading.
    """
    path = Path(path)
    
    if not path.exists():
        raise SourceNotFoundError(f"Source not found: {path}")
    
    if path.is_dir():
        return _load_from_folder(path)
    elif path.suffix.lower() in SUPPORTED_IMAGE_EXTENSIONS:
        return _load_single_image(path)
    elif path.suffix.lower() in SUPPORTED_ARCHIVE_EXTENSIONS:
        return _load_from_archive(path)
    elif path.suffix.lower() == ".pdf":
        return _load_from_pdf(path)
    else:
        raise UnsupportedSourceError(f"Unsupported source: {path}")


def _load_from_folder(folder: Path) -> list[PageInput]:
    """Load images from a folder."""
    image_files = []
    for file in folder.iterdir():
        if file.is_file() and file.suffix.lower() in SUPPORTED_IMAGE_EXTENSIONS:
            image_files.append(file)
    
    if not image_files:
        raise EmptySourceError(f"No images found in folder: {folder}")
    
    image_files.sort(key=lambda p: natural_sort_key(p.name))
    
    pages = []
    for idx, img_path in enumerate(image_files, start=1):
        try:
            image = Image.open(img_path)
            # Convert to RGB if not already
            if image.mode != "RGB":
                image = image.convert("RGB")
            pages.append(PageInput(
                page_number=idx,
                source_name=img_path.name,
                image=image,
                width=image.width,
                height=image.height,
            ))
        except Exception as e:
            raise CorruptSourceError(f"Cannot load image {img_path}: {e}")
    
    return pages


def _load_single_image(path: Path) -> list[PageInput]:
    """Load a single image file."""
    try:
        image = Image.open(path)
        # Convert to RGB if not already
        if image.mode != "RGB":
            image = image.convert("RGB")
        return [PageInput(
            page_number=1,
            source_name=path.name,
            image=image,
            width=image.width,
            height=image.height,
        )]
    except Exception as e:
        raise CorruptSourceError(f"Cannot load image {path}: {e}")


def _load_from_archive(archive_path: Path) -> list[PageInput]:
    """Load images from a CBZ/ZIP archive."""
    try:
        with zipfile.ZipFile(archive_path, 'r') as zf:
            image_names = [
                name for name in zf.namelist()
                if Path(name).suffix.lower() in SUPPORTED_IMAGE_EXTENSIONS
            ]
            
            if not image_names:
                raise EmptySourceError(f"No images found in archive: {archive_path}")
            
            # Sort by filename only (the last part of the path) to handle nested structures
            image_names.sort(key=lambda name: natural_sort_key(Path(name).name))
            
            pages = []
            for idx, name in enumerate(image_names, start=1):
                with zf.open(name) as img_file:
                    image = Image.open(img_file)
                    image.load()  # Force load to avoid file handle issues
                    # Convert to RGB if not already
                    if image.mode != "RGB":
                        image = image.convert("RGB")
                    pages.append(PageInput(
                        page_number=idx,
                        source_name=name,
                        image=image,
                        width=image.width,
                        height=image.height,
                    ))
            
            return pages
    except zipfile.BadZipFile as e:
        raise CorruptSourceError(f"Corrupt archive: {archive_path}")
    except Exception as e:
        if isinstance(e, (EmptySourceError, CorruptSourceError)):
            raise
        raise CorruptSourceError(f"Cannot load archive {archive_path}: {e}")


def _load_from_pdf(pdf_path: Path) -> list[PageInput]:
    """Load pages from a PDF."""
    try:
        document = fitz.open(pdf_path)
        
        if document.page_count == 0:
            raise EmptySourceError(f"PDF has no pages: {pdf_path}")
        
        pages = []
        for page_num in range(document.page_count):
            page = document[page_num]
            pix = page.get_pixmap()
            
            # Convert pixmap to PIL Image
            img_data = pix.tobytes("png")
            from io import BytesIO
            image = Image.open(BytesIO(img_data))
            
            pages.append(PageInput(
                page_number=page_num + 1,
                source_name=f"page-{page_num + 1}",
                image=image,
                width=image.width,
                height=image.height,
            ))
        
        document.close()
        return pages
    except Exception as e:
        if isinstance(e, (EmptySourceError, CorruptSourceError)):
            raise
        raise CorruptSourceError(f"Cannot load PDF {pdf_path}: {e}")
