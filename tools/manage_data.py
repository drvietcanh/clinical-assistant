"""
Global Data Management CLI
--------------------------

Unified entry point for data / config maintenance tasks across domains
(Scores, Drugs, Guidelines, etc.).

This complements `tools/drugs_cli.py` which is drug‑specific.

Usage examples:

    python -m tools.manage_data lint
    python -m tools.manage_data summary
    python -m tools.manage_data scores-summary
    python -m tools.manage_data drugs-summary
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any, Dict


def _ensure_project_root_on_path() -> Path:
    """Add project root to sys.path and return it."""

    project_root = Path(__file__).resolve().parents[1]
    sys.path.insert(0, str(project_root))
    return project_root


def cmd_lint(_: argparse.Namespace) -> int:
    """Basic data/config lint.

    Currently this performs very lightweight checks:
    - imports key config modules
    - ensures basic structures are present

    It is intentionally conservative to avoid breaking anything.
    """

    _ensure_project_root_on_path()
    print("🔍 Linting core config/data modules...\n")

    ok = True

    # Scores config
    try:
        from scores.config import SCORES_BY_SPECIALTY  # type: ignore

        total_scores = sum(len(v) for v in SCORES_BY_SPECIALTY.values())
        print(f"  ✅ scores/config.py loaded ({total_scores} calculators)")
    except Exception as e:  # pragma: no cover - defensive
        ok = False
        print(f"  ❌ scores/config.py: {e}")

    # Drugs config
    try:
        from drugs.config import get_all_drug_tools  # type: ignore

        tools = get_all_drug_tools()
        print(f"  ✅ drugs/config.py loaded ({len(tools)} tools)")
    except Exception as e:  # pragma: no cover
        ok = False
        print(f"  ❌ drugs/config.py: {e}")

    # Critical care config
    try:
        from critical_care.config import get_all_critical_care_tools  # type: ignore

        tools = get_all_critical_care_tools()
        print(f"  ✅ critical_care/config.py loaded ({len(tools)} tools)")
    except Exception as e:  # pragma: no cover
        ok = False
        print(f"  ❌ critical_care/config.py: {e}")

    # Diagnosis config
    try:
        from diagnosis.config import get_all_diagnosis_tabs  # type: ignore

        tabs = get_all_diagnosis_tabs()
        print(f"  ✅ diagnosis/config.py loaded ({len(tabs)} tabs)")
    except Exception as e:  # pragma: no cover
        ok = False
        print(f"  ❌ diagnosis/config.py: {e}")

    # Guidelines config
    try:
        from guidelines.config import (  # type: ignore
            get_guideline_categories,
            get_guideline_organizations,
        )

        cats = get_guideline_categories()
        orgs = get_guideline_organizations()
        print(
            f"  ✅ guidelines/config.py loaded "
            f"({len(cats)} categories, {len(orgs)} organizations)"
        )
    except Exception as e:  # pragma: no cover
        ok = False
        print(f"  ❌ guidelines/config.py: {e}")

    print()
    if ok:
        print("✅ Lint completed: no issues detected in core configs.")
        return 0

    print("❌ Lint completed: some issues detected. See messages above.")
    return 1


def _safe_load_json(path: Path) -> Dict[str, Any]:
    try:
        with path.open("r", encoding="utf-8") as f:
            return json.load(f)
    except Exception:
        return {}


def cmd_summary(_: argparse.Namespace) -> int:
    """High‑level summary of key data files (counts, basic metadata)."""

    project_root = _ensure_project_root_on_path()
    print("📊 Data summary\n")

    # Example: summarize some known JSON files if present
    candidates = [
        project_root / "drug_reference_data.json",
        project_root / "drugs_list.json",
        project_root / "all_drugs_universal.json",
        project_root / "DRUG_FIELDS_REPORT.json",
        project_root / "drug_system_analysis_report.json",
    ]

    for path in candidates:
        if not path.exists():
            continue
        data = _safe_load_json(path)
        if isinstance(data, dict):
            size = len(data)
        elif isinstance(data, list):
            size = len(data)
        else:
            size = 0
        print(f"  📁 {path.name}: {size} entries")

    print("\n(Chi tiết version/last_updated sẽ được thêm dần khi chỉnh sửa các file dữ liệu lớn.)")
    return 0


def cmd_scores_summary(_: argparse.Namespace) -> int:
    """Print summary of scores per specialty."""

    _ensure_project_root_on_path()
    from scores.config import SCORES_BY_SPECIALTY  # type: ignore

    print("📊 Scores summary\n")
    total = 0
    for spec, scores in SCORES_BY_SPECIALTY.items():
        count = len(scores)
        total += count
        print(f"  {spec}: {count} calculators")
    print(f"\n  Tổng cộng: {total} calculators")
    return 0


def cmd_drugs_summary(_: argparse.Namespace) -> int:
    """Print summary of drugs from unified DRUG_DATABASE."""

    _ensure_project_root_on_path()
    from drugs.data_access import get_drug_database  # type: ignore

    db = get_drug_database()
    print("📊 Drugs summary\n")
    print(f"  Tổng số thuốc trong DRUG_DATABASE: {len(db)}")
    return 0


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Global data/config management CLI"
    )
    subparsers = parser.add_subparsers(dest="command", help="Commands")

    lint_parser = subparsers.add_parser(
        "lint",
        help="Kiểm tra nhanh các config chính (scores, drugs, critical_care, diagnosis, guidelines)",
    )
    lint_parser.set_defaults(func=cmd_lint)

    summary_parser = subparsers.add_parser(
        "summary",
        help="Tổng quan nhanh về một số file dữ liệu JSON chính",
    )
    summary_parser.set_defaults(func=cmd_summary)

    scores_parser = subparsers.add_parser(
        "scores-summary",
        help="Tóm tắt số calculators theo chuyên khoa (scores/config.py)",
    )
    scores_parser.set_defaults(func=cmd_scores_summary)

    drugs_parser = subparsers.add_parser(
        "drugs-summary",
        help="Tóm tắt số thuốc trong DRUG_DATABASE (drugs.data_access)",
    )
    drugs_parser.set_defaults(func=cmd_drugs_summary)

    return parser


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)

    if not hasattr(args, "func"):
        parser.print_help()
        return 0

    return int(args.func(args) or 0)


if __name__ == "__main__":
    raise SystemExit(main())

