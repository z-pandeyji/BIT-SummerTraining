"""Sorting helpers for manga page filenames."""

from __future__ import annotations
import re

def natural_sort_key(value: str) -> tuple[object, ...]:
    parts = re.split(r'(\d+)', value)

    result = []

    for part in parts:
        if part.isdigit():
            result.append(int(part))
        else:
            result.append(part.lower())

    return tuple(result)

    ##raise NotImplementedError("TODO: implement natural_sort_key")
