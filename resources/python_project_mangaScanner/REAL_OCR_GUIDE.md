# Real OCR Usage Guide

## Overview

The manga_scanner now supports **real OCR** using EasyOCR! It can detect text in images, PDFs, and archives.

## Quick Start

### Without OCR (Fast - Original Behavior)
```bash
manga-scan samples/image_folder --output result.md
```

### With OCR (Slower - Detects Real Text)
```bash
manga-scan samples/image_folder --output result.md --ocr
```

## Command Options

### Basic Usage
```bash
manga-scan <input_path> --output <output_file> --ocr
```

### Specify Language
```bash
# English (default)
manga-scan input.pdf --output result.md --ocr --lang en

# Japanese
manga-scan manga.cbz --output result.md --ocr --lang ja

# Korean
manga-scan manhwa.pdf --output result.md --ocr --lang ko

# Chinese
manga-scan comic.zip --output result.md --ocr --lang zh
```

### Multiple Languages
For multiple languages, modify the code or use English as default which works reasonably well for many scripts.

## Examples

### Scan Image Folder with OCR
```bash
cd "E:\Summer training\BIT-SummerTraining\resources\python_project_mangaScanner"
manga-scan samples\image_folder --output folder_ocr.md --ocr
```

### Scan PDF with OCR
```bash
manga-scan "C:\Users\Suraj Yadav\Desktop\manga.pdf" --output manga_ocr.md --ocr
```

### Scan CBZ Archive with OCR
```bash
manga-scan samples\demo_cbz.zip --output cbz_ocr.md --ocr
```

## Important Notes

### First Run
- The first time you use `--ocr`, it will download model files (~100MB)
- This is a **one-time download**
- Subsequent runs will be faster

### Performance
- **Without --ocr**: Fast (< 1 second)
- **With --ocr**: Slower (5-30 seconds per page depending on image size)
- OCR processing time depends on:
  - Image resolution
  - Amount of text
  - Your CPU speed

### Supported Languages
EasyOCR supports 80+ languages including:
- `en` - English
- `ja` - Japanese
- `ko` - Korean
- `zh` - Chinese (Simplified & Traditional)
- `es` - Spanish
- `fr` - French
- `de` - German
- `ar` - Arabic
- `hi` - Hindi
- And many more...

See full list: https://www.jaided.ai/easyocr/

## Comparison

### Without OCR (Null Engine)
```markdown
### OCR Text

_No text detected._

### Warnings

- No OCR text detected.
```

### With OCR (Real Detection)
```markdown
### OCR Text

1. Chapter 1: The Beginning
2. Once upon a time...
3. In a distant land...

### Warnings

(No warnings if text detected)
```

## Troubleshooting

### Error: "EasyOCR not installed"
```bash
pip install easyocr
```

### Slow First Run
This is normal - model files are being downloaded. Wait for it to complete.

### GPU Acceleration (Optional)
If you have NVIDIA GPU with CUDA:
```python
from manga_scanner.real_ocr import EasyOCREngine
ocr = EasyOCREngine(languages=['en'], gpu=True)
```

### Memory Issues
If you get memory errors with large PDFs:
- Process pages in smaller batches
- Use lower resolution images
- Close other applications

## Testing

### Test with Samples (No OCR)
```bash
python -m pytest
```

### Test Real OCR Manually
```bash
cd "E:\Summer training\BIT-SummerTraining\resources\python_project_mangaScanner"
manga-scan samples\image_folder --ocr
```

## Python API Usage

```python
from manga_scanner import scan_source, render_markdown
from manga_scanner.real_ocr import EasyOCREngine

# Create OCR engine
ocr = EasyOCREngine(languages=['en'])

# Scan with OCR
scan = scan_source('path/to/manga', ocr_engine=ocr)

# Generate report
markdown = render_markdown(scan)
print(markdown)
```

## Performance Tips

1. **Start without --ocr** to verify the input loads correctly
2. **Use --ocr only when needed** for final output
3. **Test on small samples first** before processing large files
4. **Be patient** - OCR takes time but produces accurate results

## Example Workflow

```bash
# Step 1: Quick test without OCR
manga-scan samples\image_folder --output quick_test.md

# Step 2: If looks good, run with OCR
manga-scan samples\image_folder --output final_with_ocr.md --ocr

# Step 3: View results
notepad final_with_ocr.md
```

## Summary

| Command | Speed | Text Detection |
|---------|-------|----------------|
| `manga-scan input` | ⚡ Fast | ❌ None |
| `manga-scan input --ocr` | 🐢 Slow | ✅ Real OCR |

Choose based on your needs:
- **Fast preview**: Skip `--ocr`
- **Final output with text**: Use `--ocr`
