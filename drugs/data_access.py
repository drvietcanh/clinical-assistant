"""
Drug Data Access Layer
----------------------

Centralized helper functions to read from the unified drug database.
This wraps `DRUG_DATABASE` and `DRUG_GROUPS` from `drugs.drug_database`
so that other modules don't need to import low‑level structures directly.

Over time, this module can be extended to:
- add caching
- support alternate backends (e.g. API, database)
- provide typed accessors instead of raw dicts
"""

from __future__ import annotations

from typing import Dict, Iterable, List, Optional, Tuple

from .drug_database import DRUG_DATABASE, DRUG_GROUPS


def get_drug_database() -> Dict[str, dict]:
    """Return the full in‑memory drug database.

    NOTE: This currently exposes the underlying dict directly for
    backward compatibility. Prefer using helper functions below in
    new code so that we can evolve the storage later.
    """

    return DRUG_DATABASE


def get_drug_groups() -> Dict[str, dict]:
    """Return mapping of drug groups (high‑level categories)."""

    return DRUG_GROUPS


def list_all_drug_names() -> List[str]:
    """Return sorted list of all drug names."""

    return sorted(DRUG_DATABASE.keys())


def get_drug(name: str) -> Optional[dict]:
    """Get a single drug by exact name."""

    return DRUG_DATABASE.get(name)


def iter_drugs() -> Iterable[Tuple[str, dict]]:
    """Iterate over all drugs as (name, data) pairs."""

    return DRUG_DATABASE.items()


def get_drugs_by_group(group_keywords: List[str]) -> List[Tuple[str, dict]]:
    """Return drugs whose `group` field contains any of the given keywords.

    This is a small utility used by several UIs to implement quick filters.
    """

    if not group_keywords:
        return []

    keywords_lower = [kw.lower() for kw in group_keywords]
    results: List[Tuple[str, dict]] = []

    for name, data in DRUG_DATABASE.items():
        if not isinstance(data, dict):
            continue
        group_val = data.get("group") or ""
        if not isinstance(group_val, str):
            continue
        group_lower = group_val.lower()
        if any(kw in group_lower for kw in keywords_lower):
            results.append((name, data))

    return results


def search_drugs_simple(query: str, limit: int = 50) -> List[Tuple[str, dict]]:
    """Very simple case‑insensitive substring search on drug name.

    This is NOT a replacement for the advanced search system, but provides
    a light‑weight fallback that does not depend on the full search stack.
    """

    if not query:
        return []

    q = query.lower().strip()
    results: List[Tuple[str, dict]] = []

    for name, data in DRUG_DATABASE.items():
        if q in name.lower():
            results.append((name, data))
            if len(results) >= limit:
                break

    return results


__all__ = [
    "get_drug_database",
    "get_drug_groups",
    "list_all_drug_names",
    "get_drug",
    "iter_drugs",
    "get_drugs_by_group",
    "search_drugs_simple",
]

