"""Utility helpers for the DIRC module."""

from __future__ import annotations

from typing import Dict, Tuple, Union


def summarize_result(value: float, unit: str) -> Dict[str, Union[float, str]]:
    """Return a standardized result dict for UI rendering."""
    return {"value": value, "unit": unit}


def safe_validate(fn, *args, **kwargs) -> Tuple[bool, str]:
    """Run a validation function and capture any ValueError as (ok, message)."""
    try:
        fn(*args, **kwargs)
        return True, "Valid"
    except ValueError as exc:
        return False, str(exc)


