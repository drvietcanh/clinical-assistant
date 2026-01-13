"""
Guidelines Module Configuration
-------------------------------

High‑level configuration for the Guidelines / Guideline Tracker module.

This wraps the lower‑level helpers in `guidelines.data` so that
page code can work with a simple, Scores‑like config API.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Dict, List

from .data import get_category_list, get_organization_list


@dataclass(frozen=True)
class GuidelineCategory:
    id: str
    name: str
    icon: str


@dataclass(frozen=True)
class GuidelineOrganization:
    id: str
    name: str
    icon: str


def get_guideline_categories() -> List[GuidelineCategory]:
    """Return list of high‑level guideline categories."""

    categories: List[GuidelineCategory] = []
    for raw in get_category_list():
        # Simple heuristic: first emoji if present
        icon = "📋"
        name = raw
        if raw and raw[0].isascii() is False:
            # Likely emoji prefix like '❤️ Cardiology'
            icon = raw.split(" ", 1)[0]
            name = raw[len(icon) :].strip()
        categories.append(
            GuidelineCategory(
                id=raw,
                name=name,
                icon=icon,
            )
        )
    return categories


def get_guideline_organizations() -> List[GuidelineOrganization]:
    """Return list of organizations (ESC, AHA/ACC, IDSA, KDIGO, etc.)."""

    orgs: List[GuidelineOrganization] = []
    for raw in get_organization_list():
        icon = "🏥"
        name = raw
        orgs.append(
            GuidelineOrganization(
                id=raw,
                name=name,
                icon=icon,
            )
        )
    return orgs


__all__ = [
    "GuidelineCategory",
    "GuidelineOrganization",
    "get_guideline_categories",
    "get_guideline_organizations",
]

