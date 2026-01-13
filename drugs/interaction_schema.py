"""
Unified interaction schema utilities.

Provides enums, normalization, and validation helpers so the interaction
database stays consistent across legacy and new entries.
"""

from __future__ import annotations

from typing import Dict, List, Optional, Tuple

# Canonical enums
SEVERITY_VALUES: Tuple[str, ...] = (
    "Contraindicated",
    "Major",
    "Moderate",
    "Minor",
)

ONSET_VALUES: Tuple[str, ...] = (
    "rapid",           # minutes-hours
    "delayed",         # days-weeks
    "accumulation",    # requires dose accumulation
    "unknown",
)

MECHANISM_VALUES: Tuple[str, ...] = (
    "pharmacodynamic",
    "pharmacokinetic",
    "mixed",
    "unknown",
)

EVIDENCE_LEVELS: Tuple[str, ...] = (
    "high",      # guideline / RCT / boxed warning
    "moderate",  # cohort / case-control / strong PK data
    "low",       # case reports / theoretical
)

DEFAULT_MONITORING: List[str] = []
DEFAULT_SPECIAL_POPULATIONS: List[str] = []


def _ensure_list(value) -> List[str]:
    if value is None:
        return []
    if isinstance(value, (list, tuple, set)):
        return [str(v) for v in value]
    return [str(value)]


def normalize_interaction_record(
    record: Dict,
    drug1: Optional[str] = None,
    drug2: Optional[str] = None,
) -> Dict:
    """
    Return a normalized copy of a raw interaction record.
    Ensures required keys exist and optional keys have predictable shapes.
    """
    if not isinstance(record, dict):
        return {}

    normalized = dict(record)  # shallow copy

    if drug1:
        normalized.setdefault("drug1", drug1)
    if drug2:
        normalized.setdefault("drug2", drug2)

    severity = normalized.get("severity", "")
    if severity not in SEVERITY_VALUES:
        normalized["severity"] = "Unknown"

    # Optional fields with defaults
    normalized.setdefault("onset", "unknown")
    if normalized["onset"] not in ONSET_VALUES:
        normalized["onset"] = "unknown"

    normalized.setdefault("mechanism_type", "unknown")
    if normalized["mechanism_type"] not in MECHANISM_VALUES:
        normalized["mechanism_type"] = "unknown"

    normalized.setdefault("management", "")
    normalized.setdefault("monitoring", DEFAULT_MONITORING.copy())
    normalized.setdefault("special_populations", DEFAULT_SPECIAL_POPULATIONS.copy())
    normalized.setdefault("evidence_level", "moderate")
    if normalized["evidence_level"] not in EVIDENCE_LEVELS:
        normalized["evidence_level"] = "moderate"

    # Normalize references to list[str]
    normalized["references"] = _ensure_list(normalized.get("references"))

    # Clinical significance/effect naming varies across legacy data
    if "effect" not in normalized and "description" in normalized:
        normalized["effect"] = normalized["description"]
    normalized.setdefault("description", normalized.get("effect", ""))

    return normalized


def validate_interaction_record(
    record: Dict,
    pair: Tuple[str, str],
) -> List[str]:
    """Return a list of validation errors for a single interaction record."""
    errors: List[str] = []

    if not isinstance(record, dict):
        errors.append(f"{pair}: record is not a dict")
        return errors

    severity = record.get("severity")
    if severity not in SEVERITY_VALUES:
        errors.append(f"{pair}: invalid severity '{severity}'")

    if not record.get("management"):
        errors.append(f"{pair}: missing management guidance")

    if not record.get("mechanism"):
        errors.append(f"{pair}: missing mechanism description")

    # References can be string or list
    refs = record.get("references")
    if refs is None or (isinstance(refs, (list, tuple, set)) and len(refs) == 0):
        errors.append(f"{pair}: missing references")

    onset = record.get("onset", "unknown")
    if onset not in ONSET_VALUES:
        errors.append(f"{pair}: onset should be one of {ONSET_VALUES}")

    evidence = record.get("evidence_level", "moderate")
    if evidence not in EVIDENCE_LEVELS:
        errors.append(f"{pair}: evidence_level should be one of {EVIDENCE_LEVELS}")

    return errors


def validate_interactions_db(interactions_db: Dict[Tuple[str, str], Dict]) -> Dict[str, List[str]]:
    """
    Validate an interaction mapping. Returns a summary dict with errors and stats.
    """
    all_errors: List[str] = []
    severity_count = {sev: 0 for sev in SEVERITY_VALUES}
    severity_count["Unknown"] = 0

    for pair, record in interactions_db.items():
        errors = validate_interaction_record(record, pair)
        all_errors.extend(errors)

        severity = record.get("severity", "Unknown")
        if severity not in severity_count:
            severity_count["Unknown"] += 1
        else:
            severity_count[severity] += 1

    return {
        "errors": all_errors,
        "total": len(interactions_db),
        "severity_breakdown": severity_count,
    }


__all__ = [
    "SEVERITY_VALUES",
    "ONSET_VALUES",
    "MECHANISM_VALUES",
    "EVIDENCE_LEVELS",
    "normalize_interaction_record",
    "validate_interaction_record",
    "validate_interactions_db",
]
