from pathlib import Path
import re
import zipfile
from manga_scanner.models import PageInput
from manga_scanner.exceptions import SourceNotFoundError, UnsupportedSourceError, EmptySourceError
from manga_scanner.sorting import natural_sort_key

SUPPORTED_IMAGE_EXTENSIONS = {".png", ".jpg", ".jpeg", ".webp"}
SUPPORTED_ARCHIVE_EXTENSIONS = {".cbz", ".zip"}

def load_pages(path) -> list:
    """Load pages from an image folder, CBZ/ZIP archive, or PDF."""
    path_obj = Path(path)
    
    if not path_obj.exists():
        raise SourceNotFoundError(f"Path does not exist: {path}")
        
    pages = []
    
    if path_obj.is_dir():
        for file in path_obj.iterdir():
            if file.is_file() and file.suffix.lower() in SUPPORTED_IMAGE_EXTENSIONS:
                pages.append(PageInput(path=file))
                
    elif path_obj.is_file() and path_obj.suffix.lower() in SUPPORTED_ARCHIVE_EXTENSIONS:
        if zipfile.is_zipfile(path_obj):
            with zipfile.ZipFile(path_obj, 'r') as archive:
                for name in archive.namelist():
                    if not name.startswith('__MACOSX/') and Path(name).suffix.lower() in SUPPORTED_IMAGE_EXTENSIONS:
                        pages.append(PageInput(path=path_obj, archive_path=name))
    else:
        raise UnsupportedSourceError(f"Unsupported path type: {path}")
        
    if not pages:
        raise EmptySourceError(f"No readable pages found in: {path}")
        
    return sorted(pages, key=lambda p: natural_sort_key(p.archive_path if p.archive_path else p.path.name))