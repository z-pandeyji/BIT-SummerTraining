"""Markdown rendering for scanner results."""

from __future__ import annotations

from manga_scanner.models import MangaScan


def render_markdown(scan: MangaScan) -> str:
    lines = [
        f"# {scan.title}",
        "",
        f"- Source: {scan.source_path}",
        f"- Type: {scan.source_type}",
        f"- Pages: {len(scan.pages)}",
        "",
    ]

    for page in scan.pages:
        lines.append(f"## Page {page.page_number}")
        lines.append("")
        lines.append(f"- Source Name: {page.source_name}")
        lines.append(f"- Dimensions: {page.width}x{page.height}")
        lines.append("")

        if page.text_blocks:
            lines.append("### OCR Text")
            lines.append("")
            for text in page.text_blocks:
                lines.append(text)
            lines.append("")

        if page.warnings:
            lines.append("### Warnings")
            lines.append("")
            for warning in page.warnings:
                lines.append(f"- {warning}")
            lines.append("")

    return "\n".join(lines)
    """Render a deterministic Markdown report.

    Expected format:
    - ``# <title>``
    - Source metadata bullets
    - One ``## Page N`` section per page
    - Dimensions, OCR text, and warnings
    - Escape Markdown-sensitive text where needed

    TODO: Implement Markdown rendering.
    """
