from __future__ import annotations

from manga_scanner.models import MangaScan


def _escape(text: str, escape_dot: bool = True) -> str:
    if not text:
        return ""
    
    # Strict backslash escaping
    text = text.replace("\\", "\\\\")
    
    chars = "*_[]#-.`" if escape_dot else "*_[]#-"
    for ch in chars:
        text = text.replace(ch, "\\" + ch)

    return text


def render_markdown(scan: MangaScan) -> str:
    lines = []

    lines.append(f"# {_escape(scan.title, escape_dot=True)}")
    lines.append("")

    # Windows paths handling (.as_posix() forward slash ke liye)
    source_p = scan.source_path.as_posix() if hasattr(scan.source_path, "as_posix") else str(scan.source_path)
    lines.append(f"- Source: `{_escape(source_p, escape_dot=False)}`")
    lines.append(f"- Type: {_escape(scan.source_type, escape_dot=True)}")
    lines.append(f"- Pages: {len(scan.pages)}")
    lines.append("")

    for page in scan.pages:
        lines.append(f"## Page {page.page_number}")
        lines.append("")

        lines.append(f"- Source page: `{_escape(page.source_name, escape_dot=False)}`")
        lines.append(f"- Dimensions: {page.width} x {page.height}")
        lines.append("")

        lines.append("### OCR Text")
        lines.append("")

        if page.text_blocks:
            for i, text in enumerate(page.text_blocks, start=1):
                lines.append(f"{i}. {_escape(text, escape_dot=True)}")
            lines.append("")
        else:
            lines.append("_No text detected._")
            lines.append("")

        if page.warnings:
            lines.append("### Warnings")
            lines.append("")
            for warning in page.warnings:
                lines.append(f"- {_escape(warning, escape_dot=True)}")
            lines.append("")

    # Standard Markdown specification: Hamesha single newline par end hona chahiye
    return "\n".join(lines).rstrip() + "\n"