#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Find drugs missing specific fields and generate report
"""

from drugs.drug_database import DRUG_DATABASE
from collections import defaultdict
import json

def find_drugs_missing_fields():
    """Find all drugs missing priority fields"""
    
    priority_fields = {
        "renal_adjustment": [],
        "drug_interactions": [],
        "contraindications_detail": [],
        "reversal_agents": []
    }
    
    # Also track which file each drug is in
    drug_locations = {}
    
    # Try to find drug locations by searching modules
    try:
        from drugs.drug_modules import __all__
        # This is complex, so we'll just report drug names for now
    except:
        pass
    
    for drug_name, drug_data in DRUG_DATABASE.items():
        if drug_data is None or not isinstance(drug_data, dict):
            continue
            
        for field in priority_fields.keys():
            if field not in drug_data:
                priority_fields[field].append(drug_name)
            elif drug_data[field] is None:
                priority_fields[field].append(drug_name)
            elif isinstance(drug_data[field], (list, dict)) and len(drug_data[field]) == 0:
                priority_fields[field].append(drug_name)
    
    # Print report
    print("=" * 80)
    print("BÁO CÁO THUỐC THIẾU FIELD ƯU TIÊN")
    print("=" * 80)
    print(f"\nTổng số thuốc: {len(DRUG_DATABASE)}")
    
    for field, missing_drugs in priority_fields.items():
        print(f"\n{field}: {len(missing_drugs)} thuốc thiếu")
        if len(missing_drugs) > 0:
            print(f"  Ví dụ (10 đầu tiên): {', '.join(missing_drugs[:10])}")
    
    # Save to JSON for reference
    output = {
        "total_drugs": len(DRUG_DATABASE),
        "missing_fields": {field: drugs for field, drugs in priority_fields.items()}
    }
    
    with open("missing_fields_report.json", "w", encoding="utf-8") as f:
        json.dump(output, f, ensure_ascii=False, indent=2)
    
    print(f"\nĐã lưu báo cáo vào: missing_fields_report.json")
    
    return priority_fields

if __name__ == '__main__':
    find_drugs_missing_fields()
