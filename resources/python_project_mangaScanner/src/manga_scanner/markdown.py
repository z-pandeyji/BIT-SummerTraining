"""Markdown rendering for scanner results."""

from __future__ import annotations

from manga_scanner.models import MangaScan


def render_markdown(scan: MangaScan) -> str:
    def esc(text: str) -> str:
        return (
            text.replace("\\", "\\\\")
                .replace("*", "\\*")
                .replace(".", "\\.")
        )

    md = f"# {esc(scan.title)}\n\n"

    md += f"- Source: `{scan.source_path}`\n"
    md += f"- Type: {scan.source_type}\n"
    md += f"- Pages: {len(scan.pages)}\n\n"

    for page in scan.pages:
        md += f"## Page {page.page_number}\n\n"

        md += f"- Source page: `{page.source_name}`\n"
        md += f"- Dimensions: {page.width} x {page.height}\n\n"

        md += "### OCR Text\n\n"

        if page.text_blocks:
            for i, text in enumerate(page.text_blocks, 1):
                md += f"{i}. {esc(text)}\n"
        else:
            md += "_No text detected._\n"

        md += "\n"

        if page.warnings:
            md += "### Warnings\n\n"
            for w in page.warnings:
                md += f"- {esc(w)}\n"

        md += "\n"

    return md