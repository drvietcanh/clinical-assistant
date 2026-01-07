#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script to comprehensively check for missing fields in drug database
"""

from drugs.drug_database import DRUG_DATABASE
from pathlib import Path
import re

# 14 enhanced fields
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

# Allow empty content for supportive/vitamin-style modules (keys must still exist)
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
    """Find which file contains a drug (supports single/double quotes)."""
    modules_path = Path("drugs/drug_modules")

    for py_file in modules_path.rglob("*.py"):
        if py_file.name == "__init__.py":
            continue

        try:
            text = py_file.read_text(encoding="utf-8")
            pattern = r"[\"']" + re.escape(drug_name) + r"[\"']\s*:"
            if re.search(pattern, text):
                return py_file.as_posix()
        except Exception:
            continue

    return "Unknown"

def is_field_empty(value):
    """Check if field is empty"""
    if value is None:
        return True
    if isinstance(value, str):
        return not value.strip()
    if isinstance(value, (list, dict)):
        return len(value) == 0
    return False

def check_missing_fields():
    """Check all drugs for missing enhanced fields"""
    
    results = {field: [] for field in ENHANCED_FIELDS}

    for drug_name, drug_data in DRUG_DATABASE.items():
        if drug_data is None:
            print(f"WARNING: {drug_name} has None data")
            continue

        if not isinstance(drug_data, dict):
            print(f"WARNING: {drug_name} data is not a dict: {type(drug_data)}")
            continue

        file_path = find_drug_file(drug_name)
        allow_empty = _is_allow_empty(file_path)

        for field in ENHANCED_FIELDS:
            if field not in drug_data:
                results[field].append(drug_name)
            elif is_field_empty(drug_data[field]) and not allow_empty:
                results[field].append(drug_name)
    
    print("=" * 80)
    print("KIỂM TRA 14 ENHANCED FIELDS")
    print("=" * 80)
    print(f"\nTổng số thuốc trong database: {len(DRUG_DATABASE)}")
    
    print("\n" + "=" * 80)
    print("THỐNG KÊ THIẾU FIELD")
    print("=" * 80)
    
    for field in ENHANCED_FIELDS:
        missing_count = len(results[field])
        percentage = (missing_count / len(DRUG_DATABASE)) * 100
        status = "✓" if missing_count == 0 else "✗"
        print(f"{status} {field:<35} | Thiếu: {missing_count:3d} ({percentage:5.1f}%)")
        if missing_count > 0 and missing_count <= 10:
            print(f"   Ví dụ: {', '.join(results[field][:5])}")
    
    # Summary
    print("\n" + "=" * 80)
    print("TÓM TẮT")
    print("=" * 80)
    
    total_missing = sum(len(results[field]) for field in ENHANCED_FIELDS)
    if total_missing == 0:
        print("✓ Tất cả các field đã đầy đủ!")
    else:
        print(f"Cần bổ sung {total_missing} field cho các thuốc")
        print("\nCác field cần ưu tiên:")
        priority_fields = ["renal_adjustment", "drug_interactions", "contraindications_detail", "reversal_agents"]
        for field in priority_fields:
            if len(results[field]) > 0:
                print(f"  - {field}: {len(results[field])} thuốc")
    
    return results

if __name__ == '__main__':
    try:
        results = check_missing_fields()
    except Exception as e:
        print(f"Error: {e}")
        import traceback
        traceback.print_exc()
