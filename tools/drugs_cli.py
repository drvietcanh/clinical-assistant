"""
Unified Drugs CLI Entry Point
-----------------------------

This script provides a single command‑line entry for all drug‑related
maintenance tasks, wrapping the existing CLI tools in the `drugs` package.

Usage examples:

    python -m tools.drugs_cli data quality --limit 50
    python -m tools.drugs_cli data search \"vancomycin\" --fuzzy
    python -m tools.drugs_cli enhanced stats
    python -m tools.drugs_cli enhanced missing --limit 50
    python -m tools.drugs_cli core search \"metformin\" --limit 20
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path


def _ensure_project_root_on_path() -> None:
    """Add project root to sys.path so `drugs` can be imported when run directly."""

    project_root = Path(__file__).resolve().parents[1]
    sys.path.insert(0, str(project_root))


def main(argv: list[str] | None = None) -> int:
    _ensure_project_root_on_path()

    parser = argparse.ArgumentParser(
        description="Unified CLI for Drug Database maintenance and analysis"
    )
    subparsers = parser.add_subparsers(dest="group", help="Command groups")

    # Data management (quality, metrics, integrity, search, backups, ...)
    data_parser = subparsers.add_parser(
        "data",
        help="Data quality, integrity, search & backups (wraps drugs.data_management_cli)",
    )
    data_parser.add_argument(
        "args",
        nargs=argparse.REMAINDER,
        help="Arguments forwarded to drugs.data_management_cli",
    )

    # Core drug index & structure tools
    core_parser = subparsers.add_parser(
        "core",
        help="Core drug index / structure tools (wraps drugs.drug_cli)",
    )
    core_parser.add_argument(
        "args",
        nargs=argparse.REMAINDER,
        help="Arguments forwarded to drugs.drug_cli",
    )

    # Enhanced fields tools
    enhanced_parser = subparsers.add_parser(
        "enhanced",
        help="Enhanced fields tools (wraps drugs.enhanced_fields_cli)",
    )
    enhanced_parser.add_argument(
        "args",
        nargs=argparse.REMAINDER,
        help="Arguments forwarded to drugs.enhanced_fields_cli",
    )

    parsed = parser.parse_args(argv)

    if not parsed.group:
        parser.print_help()
        return 0

    if parsed.group == "data":
        from drugs import data_management_cli

        # Forward remaining args (e.g. ["quality", "--limit", "20"])
        sys.argv = ["drugs_data_management_cli"] + (parsed.args or [])
        data_management_cli.main()
        return 0

    if parsed.group == "core":
        from drugs import drug_cli

        sys.argv = ["drugs_core_cli"] + (parsed.args or [])
        drug_cli.main()
        return 0

    if parsed.group == "enhanced":
        from drugs import enhanced_fields_cli

        sys.argv = ["drugs_enhanced_cli"] + (parsed.args or [])
        enhanced_fields_cli.main()
        return 0

    parser.print_help()
    return 1


if __name__ == "__main__":
    raise SystemExit(main())

