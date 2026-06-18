"""Markdown rendering for scanner results."""

from __future__ import annotations

import re

from manga_scanner.models import MangaScan

_ESCAPE_RE = re.compile(r"([\\*_\[\]#\-\.`])")


def _esc(text: str) -> str:
    return _ESCAPE_RE.sub(r"\\\1", text)


def render_markdown(scan: MangaScan) -> str:
    lines: list[str] = []

    lines.append(f"# {_esc(scan.title)}")
    lines.append("")
    lines.append(f"- Source: `{scan.source_path.as_posix()}`")
    lines.append(f"- Type: {scan.source_type}")
    lines.append(f"- Pages: {len(scan.pages)}")

    for page in scan.pages:
        lines.append("")
        lines.append(f"## Page {page.page_number}")
        lines.append("")
        lines.append(f"- Source page: `{page.source_name}`")
        lines.append(f"- Dimensions: {page.width} x {page.height}")
        lines.append("")
        lines.append("### OCR Text")
        lines.append("")
        if page.text_blocks:
            for i, block in enumerate(page.text_blocks, 1):
                lines.append(f"{i}. {_esc(block)}")
        else:
            lines.append("_No text detected._")
        if page.warnings:
            lines.append("")
            lines.append("### Warnings")
            lines.append("")
            for warning in page.warnings:
                lines.append(f"- {_esc(warning)}")

    lines.append("")
    return "\n".join(lines)
