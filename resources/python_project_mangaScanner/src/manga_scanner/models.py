from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path
from typing import Protocol, Sequence

from PIL import Image


@dataclass(frozen=True)
class PageInput:
    page_number: int
    source_name: str
    image: Image.Image
    width: int
    height: int


@dataclass(frozen=True)
class PageScan:
    page_number: int
    source_name: str
    width: int
    height: int
    text_blocks: tuple[str, ...] = field(default_factory=tuple)
    warnings: tuple[str, ...] = field(default_factory=tuple)


@dataclass(frozen=True)
class MangaScan:
    title: str
    source_path: Path
    source_type: str
    pages: tuple[PageScan, ...] = field(default_factory=tuple)


class OcrEngine(Protocol):
    def recognize(self, page: PageInput) -> Sequence[str]:
        pass