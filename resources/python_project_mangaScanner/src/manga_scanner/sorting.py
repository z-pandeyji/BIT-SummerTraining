"""Sorting helpers for manga page filenames."""

from __future__ import annotations
import re


def natural_sort_key(value: str) -> tuple[object, ...]:
    """Return a key that sorts embedded numbers numerically.

    Example:
        ``page2.png`` should sort before ``page10.png``.
    """

    parts = re.split(r'(\d+)', value)

    return tuple(
        int(part) if part.isdigit() else part.lower()
        for part in parts
    )