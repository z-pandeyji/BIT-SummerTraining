"""Command-line entry point for manga-scan."""

from __future__ import annotations

import argparse
from pathlib import Path

from manga_scanner.markdown import render_markdown
from manga_scanner.scanner import scan_source


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Scan manga/manhwa into Markdown.")
    parser.add_argument("input", help="Image folder, CBZ/ZIP archive, or PDF file")
    parser.add_argument(
        "--output",
        "-o",
        help="Markdown output path. Prints to stdout when omitted.",
    )
    parser.add_argument(
        "--ocr",
        action="store_true",
        help="Enable real OCR text detection (uses EasyOCR).",
    )
    parser.add_argument(
        "--lang",
        default="en",
        help="OCR language code (default: en). Examples: en, ja, ko, zh.",
    )
    return parser


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)

    # Initialize OCR engine if requested
    ocr_engine = None
    if args.ocr:
        try:
            from manga_scanner.real_ocr import EasyOCREngine
            ocr_engine = EasyOCREngine(languages=[args.lang])
        except ImportError:
            print("Error: EasyOCR not installed. Install with: pip install easyocr")
            return 1
        except Exception as e:
            print(f"Error initializing OCR: {e}")
            return 1

    # Pass ocr_engine only if not None to maintain backward compatibility
    if ocr_engine is not None:
        scan = scan_source(args.input, ocr_engine=ocr_engine)
    else:
        scan = scan_source(args.input)
    
    markdown = render_markdown(scan)
    if args.output:
        Path(args.output).write_text(markdown, encoding="utf-8")
    else:
        print(markdown, end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
