#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Comprehensive field checker and reporter
Generates detailed report of missing fields with file locations
"""

from drugs.drug_database import DRUG_DATABASE
from pathlib import Path
import json
import re

ALLOW_EMPTY_PATH_SUBSTRINGS = [
    "drugs/drug_modules/nutrition/vitamins.py",
    "drugs/drug_modules/supportive/vitamin_b12s.py",
    "drugs/drug_modules/supportive/vitamin_ds.py",
    "drugs/drug_modules/supportive/irons.py",
    "drugs/drug_modules/supportive/antihistamine_h1_antagonist_",
    "drugs/drug_modules/supportive/sedatives_anesthetics_icu.py",
    "drugs/drug_modules/supportive/neuromuscular_blockers.py",
    "drugs/drug_modules/vaccines/",
    "drugs/drug_modules/emergency/fluids.py",
]


def _normalize_path(path: str) -> str:
    return path.replace("\\", "/")


def _is_allow_empty(path: str) -> bool:
    norm = _normalize_path(path)
    return any(sub in norm for sub in ALLOW_EMPTY_PATH_SUBSTRINGS)


def find_drug_file(drug_name: str) -> str:
    """Find which file contains a drug (supports single/double quotes)"""
    modules_path = Path("drugs/drug_modules")

    for py_file in modules_path.rglob("*.py"):
        if py_file.name == "__init__.py":
            continue

        try:
            content = py_file.read_text(encoding="utf-8")
            pattern = r"[\"']" + re.escape(drug_name) + r"[\"']\s*:"
            if re.search(pattern, content):
                return py_file.as_posix()
        except Exception:
            continue

    return "Unknown"

def check_all_fields():
    """Comprehensive field check with file locations"""
    
    ENHANCED_FIELDS = [
        "mechanism_of_action",
        "monitoring",
        "precautions",
        "pharmacokinetics",
        "storage",
        "black_box_warnings",
        "drug_interactions",
        "contraindications_detail",
        "pregnancy_lactation",
        "hepatic_adjustment",
        "renal_adjustment",
        "overdose_management",
        "reversal_agents",
        "administration_instructions",
    ]
    
    priority_fields = ["renal_adjustment", "drug_interactions", "contraindications_detail", "reversal_agents"]
    
    results = {field: [] for field in ENHANCED_FIELDS}
    drug_locations = {}
    
    for drug_name, drug_data in DRUG_DATABASE.items():
        if drug_data is None or not isinstance(drug_data, dict):
            continue
        
        # Find file location
        file_path = find_drug_file(drug_name)
        drug_locations[drug_name] = file_path
        
        # Check each field
        for field in ENHANCED_FIELDS:
            if field not in drug_data:
                results[field].append(
                    {"drug": drug_name, "file": file_path, "reason": "missing"}
                )
            elif drug_data[field] is None:
                results[field].append(
                    {"drug": drug_name, "file": file_path, "reason": "null"}
                )
            elif (
                isinstance(drug_data[field], (list, dict))
                and len(drug_data[field]) == 0
                and not _is_allow_empty(file_path)
            ):
                results[field].append(
                    {"drug": drug_name, "file": file_path, "reason": "empty"}
                )
    
    # Print summary
    print("=" * 80)
    print("COMPREHENSIVE FIELD CHECK REPORT")
    print("=" * 80)
    print(f"\nTotal drugs: {len(DRUG_DATABASE)}")
    
    print("\n" + "=" * 80)
    print("PRIORITY FIELDS SUMMARY")
    print("=" * 80)
    
    for field in priority_fields:
        missing = results[field]
        print(f"\n{field}: {len(missing)} drugs missing")
        if len(missing) > 0:
            # Group by file
            by_file = {}
            for item in missing:
                file_path = item["file"]
                if file_path not in by_file:
                    by_file[file_path] = []
                by_file[file_path].append(item["drug"])
            
            print(f"  Files affected: {len(by_file)}")
            # Show top 5 files with most missing
            sorted_files = sorted(by_file.items(), key=lambda x: len(x[1]), reverse=True)[:5]
            for file_path, drugs in sorted_files:
                print(f"    {file_path}: {len(drugs)} drugs")
                if len(drugs) <= 5:
                    print(f"      {', '.join(drugs)}")
                else:
                    print(f"      {', '.join(drugs[:5])}...")
    
    # Save detailed report
    report = {
        "total_drugs": len(DRUG_DATABASE),
        "fields": {field: results[field] for field in ENHANCED_FIELDS},
        "drug_locations": drug_locations
    }
    
    with open("comprehensive_field_report.json", "w", encoding="utf-8") as f:
        json.dump(report, f, ensure_ascii=False, indent=2)
    
    print(f"\nDetailed report saved to: comprehensive_field_report.json")
    
    return results

if __name__ == '__main__':
    check_all_fields()
