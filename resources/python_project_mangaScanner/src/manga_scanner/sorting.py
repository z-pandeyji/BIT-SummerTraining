"""Sorting helpers for manga page filenames."""

from __future__ import annotations
import re

def natural_sort_key(value: str) -> tuple[object, ...]:
    """
    Return a key that sorts embedded numbers numerically.
    
    Example:
        `page2.png` should sort before `page10.png`.
    """
    result: list[tuple[int, object]] = []
    for part in re.split(r'(\d+)', value):
        if part.isdigit():
            result.append((1, int(part)))
        else:
            result.append((0, part.lower()))

    return tuple(result)
