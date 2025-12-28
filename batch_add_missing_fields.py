#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script to batch add missing fields to drugs
This script will help identify and add missing fields systematically
"""

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

def get_missing_fields_template(drug_name, drug_data, missing_fields):
    """Generate template code for missing fields"""
    templates = []
    
    for field in missing_fields:
        if field == "black_box_warnings":
            templates.append(f'        "black_box_warnings": "Không có cảnh báo hộp đen đặc biệt.",')
        elif field == "drug_interactions":
            templates.append('''        "drug_interactions": {
            "major": [],
            "moderate": [],
            "minor": []
        },''')
        elif field == "contraindications_detail":
            # Try to convert from contraindications list if exists
            if "contraindications" in drug_data:
                contra = drug_data["contraindications"]
                if isinstance(contra, list):
                    templates.append(f'''        "contraindications_detail": {{
            "tuyệt_đối": {contra},
            "tương_đối": []
        }},''')
                elif isinstance(contra, dict):
                    templates.append(f'''        "contraindications_detail": {{
            "tuyệt_đối": {contra.get("tuyệt_đối", [])},
            "tương_đối": {contra.get("tương_đối", [])}
        }},''')
            else:
                templates.append('''        "contraindications_detail": {
            "tuyệt_đối": [],
            "tương_đối": []
        },''')
        elif field == "renal_adjustment":
            templates.append('''        "renal_adjustment": {
            "normal": "Không cần chỉnh liều",
            "30_60": "Không cần chỉnh liều",
            "under_30": "Thận trọng, có thể cần giảm liều"
        },''')
        elif field == "reversal_agents":
            templates.append('''        "reversal_agents": {"available": False, "agents": []},''')
    
    return "\n".join(templates)

def main():
    """Find drugs missing exactly 2 fields"""
    drugs_missing_2 = []
    
    for drug_name, drug_data in DRUG_DATABASE.items():
        missing_fields = [f for f in ENHANCED_FIELDS if is_field_missing(drug_data, f)]
        
        if len(missing_fields) == 2:
            template = get_missing_fields_template(drug_name, drug_data, missing_fields)
            drugs_missing_2.append({
                'name': drug_name,
                'missing': missing_fields,
                'template': template
            })
    
    print(f"Found {len(drugs_missing_2)} drugs missing exactly 2 fields\n")
    
    # Group by missing field combination
    by_combo = {}
    for drug in drugs_missing_2:
        combo = ", ".join(sorted(drug['missing']))
        if combo not in by_combo:
            by_combo[combo] = []
        by_combo[combo].append(drug)
    
    print("Grouped by missing field combination:\n")
    for combo, drugs in sorted(by_combo.items()):
        print(f"{combo}: {len(drugs)} drugs")
        for drug in drugs[:5]:  # Show first 5
            print(f"  - {drug['name']}")
        if len(drugs) > 5:
            print(f"  ... and {len(drugs) - 5} more")
        print()

if __name__ == '__main__':
    main()

