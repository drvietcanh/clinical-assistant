#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script to find drugs missing exactly 2 enhanced fields
"""

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

def find_drugs_missing_2_fields():
    """Find all drugs missing exactly 2 fields"""
    
    drugs_missing_2 = []
    
    for drug_name, drug_data in DRUG_DATABASE.items():
        missing_fields = [f for f in ENHANCED_FIELDS if is_field_missing(drug_data, f)]
        
        if len(missing_fields) == 2:
            drugs_missing_2.append({
                'name': drug_name,
                'missing': missing_fields
            })
    
    print("=" * 80)
    print(f"TÌM THUỐC THIẾU ĐÚNG 2 FIELD")
    print("=" * 80)
    print(f"\nTổng số thuốc trong database: {len(DRUG_DATABASE)}")
    print(f"Số thuốc thiếu đúng 2 field: {len(drugs_missing_2)}")
    
    if drugs_missing_2:
        print("\n" + "=" * 80)
        print("DANH SÁCH THUỐC THIẾU ĐÚNG 2 FIELD:")
        print("=" * 80)
        
        for i, drug in enumerate(drugs_missing_2, 1):
            print(f"{i:3d}. {drug['name']:<40} - Thiếu: {', '.join(drug['missing'])}")
    
    return drugs_missing_2

if __name__ == '__main__':
    try:
        drugs = find_drugs_missing_2_fields()
        print(f"\n\nTổng cộng: {len(drugs)} thuốc cần bổ sung 2 field")
    except Exception as e:
        print(f"Error: {e}")
        import traceback
        traceback.print_exc()


