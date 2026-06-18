"""Sorting helpers for manga page filenames."""
import re

def natural_sort_key(value: str) -> tuple:
    """Return a key that sorts embedded numbers numerically."""
    return tuple(int(text) if text.isdigit() else text.lower() for text in re.split(r'(\d+)', value))

def natural_sort(l: list) -> list:
    """Is function ka use karke list ko natural order me sort karte hain."""
    return sorted(l, key=natural_sort_key)