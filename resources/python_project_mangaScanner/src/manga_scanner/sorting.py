"""Sorting helpers for manga page filenames."""

from __future__ import annotations


def natural_sort_key(value: str) -> tuple[object, ...]:
    """Return a key that sorts embedded numbers numerically.

    Example:
        ``page2.png`` should sort before ``page10.png``.

    TODO: Split the string into text and digit chunks. Lowercase text chunks,
    convert digit chunks to integers, and return them as a tuple.
    """
    import re
    parts = []
    for chunk in re.split(r'(\d+)', value):
        if chunk.isdigit():
            parts.append(int(chunk))
        else:
            parts.append(chunk.lower())
    return tuple(parts)
