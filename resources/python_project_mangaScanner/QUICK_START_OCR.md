# Quick Start Guide - Real OCR

## 🚀 Get Started in 3 Steps

### Step 1: Navigate to Project
```bash
cd "E:\Summer training\BIT-SummerTraining\resources\python_project_mangaScanner"
```

### Step 2: Try Without OCR (Fast)
```bash
manga-scan samples\image_folder --output test_no_ocr.md
notepad test_no_ocr.md
```

**You'll see:**
```markdown
### OCR Text

_No text detected._
```

### Step 3: Try With OCR (Real Text Detection)
```bash
manga-scan samples\image_folder --output test_with_ocr.md --ocr
notepad test_with_ocr.md
```

**You'll see actual text:**
```markdown
### OCR Text

1. Folder page
2. Synthetic BIT Training sample
```

---

## ✨ That's It!

You now have a working OCR scanner that can:
- ✅ Scan images, PDFs, and archives
- ✅ Detect text in 80+ languages
- ✅ Generate beautiful Markdown reports

## 📖 Next Steps

- Read `REAL_OCR_GUIDE.md` for advanced usage
- Try with your own files
- Use different languages with `--lang` flag

## 💡 Pro Tips

**Fast preview:**
```bash
manga-scan your_file.pdf
```
(No --output means print to screen)

**Full OCR scan:**
```bash
manga-scan your_file.pdf --output result.md --ocr
```

**Japanese manga:**
```bash
manga-scan manga.cbz --output result.md --ocr --lang ja
```

**Korean manhwa:**
```bash
manga-scan manhwa.pdf --output result.md --ocr --lang ko
```

---

**Enjoy your Real OCR Scanner!** 🎉
