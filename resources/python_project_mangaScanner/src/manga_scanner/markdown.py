"""Markdown rendering for scanner results."""

from __future__ import annotations

from pathlib import PurePosixPath

from manga_scanner.models import MangaScan


MARKDOWN_SPECIAL_CHARS = "\\`*_{}[]()#+-.!"


def _escape_markdown(value: str) -> str:
    return "".join(f"\\{char}" if char in MARKDOWN_SPECIAL_CHARS else char for char in value)


def _format_path(path: object) -> str:
    return PurePosixPath(str(path).replace("\\", "/")).as_posix()


def render_markdown(scan: MangaScan) -> str:
    """Render a deterministic Markdown report.

    Expected format:
    - ``# <title>``
    - Source metadata bullets
    - One ``## Page N`` section per page
    - Dimensions, OCR text, and warnings
    - Escape Markdown-sensitive text where needed

    TODO: Implement Markdown rendering.
    """

    lines = [
        f"# {_escape_markdown(scan.title)}",
        "",
        f"- Source: `{_format_path(scan.source_path)}`",
        f"- Type: {scan.source_type}",
        f"- Pages: {len(scan.pages)}",
    ]

    for page in scan.pages:
        lines.extend(
            [
                "",
                f"## Page {page.page_number}",
                "",
                f"- Source page: `{page.source_name}`",
                f"- Dimensions: {page.width} x {page.height}",
                "",
                "### OCR Text",
                "",
            ]
        )

        if page.text_blocks:
            lines.extend(
                f"{index}. {_escape_markdown(text)}"
                for index, text in enumerate(page.text_blocks, 1)
            )
        else:
            lines.append("_No text detected._")

        if page.warnings:
            lines.extend(["", "### Warnings", ""])
            lines.extend(f"- {_escape_markdown(warning)}" for warning in page.warnings)

    return "\n".join(lines) + "\n"
