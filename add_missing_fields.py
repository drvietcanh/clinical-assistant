#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script to find drug locations and generate missing field templates
"""

import os
import re
from drugs.drug_database import DRUG_DATABASE

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
    "administration_instructions"
]

def is_field_missing(drug_data, field):
    """Check if a field is missing or empty"""
    if field not in drug_data:
        return True
    value = drug_data.get(field)
    if value is None:
        return True
    if isinstance(value, str) and not value.strip():
        return True
    if isinstance(value, (list, dict)) and len(value) == 0:
        return True
    return False

def find_drug_file(drug_name):
    """Find which file contains the drug definition"""
    drug_modules_dir = "drugs/drug_modules"
    
    # Search through all Python files in drug_modules
    for root, dirs, files in os.walk(drug_modules_dir):
        for file in files:
            if file.endswith('.py'):
                filepath = os.path.join(root, file)
                try:
                    with open(filepath, 'r', encoding='utf-8') as f:
                        content = f.read()
                        # Check if drug name appears as a key
                        # Look for patterns like "Drug Name": { or 'Drug Name': {
                        patterns = [
                            f'"{re.escape(drug_name)}"',
                            f"'{re.escape(drug_name)}'",
                        ]
                        for pattern in patterns:
                            if re.search(pattern, content):
                                return filepath
                except:
                    continue
    
    # Also check enhanced_fields_overrides.py
    if os.path.exists("drugs/enhanced_fields_overrides.py"):
        try:
            with open("drugs/enhanced_fields_overrides.py", 'r', encoding='utf-8') as f:
                content = f.read()
                patterns = [
                    f'"{re.escape(drug_name)}"',
                    f"'{re.escape(drug_name)}'",
                ]
                for pattern in patterns:
                    if re.search(pattern, content):
                        return "drugs/enhanced_fields_overrides.py"
        except:
            pass
    
    return None

def generate_field_template(field_name, drug_name, drug_data):
    """Generate a template for the missing field"""
    
    templates = {
        "black_box_warnings": lambda d, n: "None  # Không có cảnh báo hộp đen đặc biệt",
        "drug_interactions": lambda d, n: {
            "major": [],
            "moderate": [],
            "minor": []
        },
        "contraindications_detail": lambda d, n: {
            "tuyệt_đối": d.get("contraindications", []) if isinstance(d.get("contraindications"), list) else [],
            "tương_đối": []
        },
        "renal_adjustment": lambda d, n: {
            "normal": "Không cần chỉnh liều",
            "30_60": "Không cần chỉnh liều",
            "under_30": "Thận trọng, có thể cần giảm liều"
        },
        "reversal_agents": lambda d, n: {"available": False, "agents": []}
    }
    
    if field_name in templates:
        return templates[field_name](drug_data, drug_name)
    
    return None

def main():
    """Find drugs missing 2 fields and their locations"""
    
    drugs_missing_2 = []
    
    for drug_name, drug_data in DRUG_DATABASE.items():
        missing_fields = [f for f in ENHANCED_FIELDS if is_field_missing(drug_data, f)]
        
        if len(missing_fields) == 2:
            filepath = find_drug_file(drug_name)
            drugs_missing_2.append({
                'name': drug_name,
                'missing': missing_fields,
                'file': filepath
            })
    
    print("=" * 100)
    print(f"THUỐC THIẾU ĐÚNG 2 FIELD VÀ VỊ TRÍ FILE")
    print("=" * 100)
    print(f"\nTổng số: {len(drugs_missing_2)} thuốc\n")
    
    # Group by file
    by_file = {}
    for drug in drugs_missing_2:
        file = drug['file'] or "NOT FOUND"
        if file not in by_file:
            by_file[file] = []
        by_file[file].append(drug)
    
    for file, drugs in sorted(by_file.items()):
        print(f"\n{'='*100}")
        print(f"FILE: {file}")
        print(f"{'='*100}")
        for drug in drugs:
            print(f"  - {drug['name']:<50} Thiếu: {', '.join(drug['missing'])}")
    
    return drugs_missing_2

if __name__ == '__main__':
    try:
        drugs = main()
        print(f"\n\nTổng cộng: {len(drugs)} thuốc cần bổ sung")
    except Exception as e:
        print(f"Error: {e}")
        import traceback
        traceback.print_exc()

