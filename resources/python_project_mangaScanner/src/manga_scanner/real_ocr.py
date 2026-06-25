"""Real OCR implementation using EasyOCR."""

from __future__ import annotations

import warnings
from typing import Sequence

import numpy as np

from manga_scanner.models import PageInput

# Suppress EasyOCR warnings
warnings.filterwarnings("ignore")


class EasyOCREngine:
    """Real OCR engine using EasyOCR library.
    
    This engine can detect text in multiple languages from images.
    First use will download model files (~100MB).
    """

    def __init__(self, languages: list[str] | None = None, gpu: bool = False):
        """Initialize EasyOCR with specified languages.
        
        Args:
            languages: List of language codes (default: ['en'] for English)
            gpu: Use GPU acceleration if available (default: False)
        """
        import easyocr
        
        if languages is None:
            languages = ['en']  # Default to English
        
        print(f"Initializing EasyOCR with languages: {languages}")
        print("Note: First run will download model files (~100MB)...")
        
        self.reader = easyocr.Reader(languages, gpu=gpu, verbose=False)
        print("OCR engine ready!")

    def recognize(self, page: PageInput) -> Sequence[str]:
        """Extract text from a page image.
        
        Args:
            page: PageInput containing the image to process
            
        Returns:
            List of detected text strings
        """
        # Convert PIL Image to numpy array
        img_array = np.array(page.image)
        
        # Perform OCR
        results = self.reader.readtext(img_array, detail=0)
        
        # Filter out empty strings and return
        text_blocks = [text.strip() for text in results if text.strip()]
        
        return text_blocks


class TesseractOCREngine:
    """OCR engine using Tesseract (requires Tesseract installation)."""

    def __init__(self, lang: str = 'eng', tesseract_cmd: str | None = None):
        """Initialize Tesseract OCR.
        
        Args:
            lang: Language code (default: 'eng' for English)
            tesseract_cmd: Path to tesseract executable (auto-detect if None)
        """
        import pytesseract
        
        if tesseract_cmd:
            pytesseract.pytesseract.tesseract_cmd = tesseract_cmd
        
        self.lang = lang
        print(f"Tesseract OCR initialized with language: {lang}")

    def recognize(self, page: PageInput) -> Sequence[str]:
        """Extract text from a page image using Tesseract.
        
        Args:
            page: PageInput containing the image to process
            
        Returns:
            List of detected text lines
        """
        import pytesseract
        
        # Extract text from image
        text = pytesseract.image_to_string(page.image, lang=self.lang)
        
        # Split into lines and filter empty ones
        lines = [line.strip() for line in text.split('\n') if line.strip()]
        
        return lines
