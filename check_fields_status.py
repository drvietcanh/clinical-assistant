#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script to check status of all enhanced fields
"""

from drugs.drug_database import DRUG_DATABASE
from drugs.enhanced_fields_schema import validate_enhanced_fields

# Required 6 basic fields
BASIC_FIELDS = [
    'mechanism_of_action',
    'monitoring',
    'precautions',
    'pharmacokinetics',
    'storage',
    'black_box_warnings'
]

# Optional 8 fields
OPTIONAL_FIELDS = [
    'drug_interactions',
    'contraindications',
    'pregnancy_lactation',
    'hepatic_adjustment',
    'overdose_management',
    'reversal_agents',
    'administration_instructions',
    'references'
]

def check_all_fields():
    """Check status of all fields"""
    
    total = len(DRUG_DATABASE)
    with_basic = 0
    with_optional = 0
    issues = []
    
    for name, data in DRUG_DATABASE.items():
        # Check basic fields
        has_all_basic = all(field in data for field in BASIC_FIELDS)
        if has_all_basic:
            with_basic += 1
        
        # Check optional fields
        has_all_optional = all(field in data for field in OPTIONAL_FIELDS)
        if has_all_optional:
            with_optional += 1
        
        # Check for issues
        drug_issues = []
        
        # Check if contraindications is old format (list)
        if 'contraindications' in data:
            if isinstance(data['contraindications'], list):
                drug_issues.append('contraindications là list (cũ) - cần chuyển sang dict')
        
        # Check if drug_interactions exists but wrong type
        if 'drug_interactions' in data:
            if not isinstance(data['drug_interactions'], (dict, type(None))):
                drug_issues.append(f'drug_interactions có type sai: {type(data["drug_interactions"]).__name__}')
        
        # Check validation
        if has_all_basic:
            basic_fields_data = {k: data[k] for k in BASIC_FIELDS if k in data}
            is_valid, errors = validate_enhanced_fields(name, basic_fields_data)
            if not is_valid:
                drug_issues.extend([f'Validation: {e}' for e in errors])
        
        if drug_issues:
            issues.append((name, drug_issues))
    
    # Print results
    print("=" * 80)
    print("BÁO CÁO TỔNG QUAN ENHANCED FIELDS")
    print("=" * 80)
    print(f"\nTổng số thuốc: {total}")
    print(f"Có đủ 6 fields cơ bản: {with_basic}/{total} ({with_basic*100//total}%)")
    print(f"Có đủ 14 fields (6 cơ bản + 8 tùy chọn): {with_optional}/{total} ({with_optional*100//total}%)")
    
    if issues:
        print(f"\n⚠️  Tìm thấy {len(issues)} thuốc có vấn đề:")
        for name, drug_issues in issues[:20]:
            print(f"  - {name}:")
            for issue in drug_issues:
                print(f"    • {issue}")
        if len(issues) > 20:
            print(f"  ... và {len(issues) - 20} thuốc khác")
    else:
        print("\n✅ Không có vấn đề nào!")
    
    # Count optional fields
    print("\n" + "=" * 80)
    print("THỐNG KÊ 8 FIELDS TÙY CHỌN")
    print("=" * 80)
    for field in OPTIONAL_FIELDS:
        count = sum(1 for d in DRUG_DATABASE.values() if field in d)
        print(f"{field}: {count}/{total} ({count*100//total}%)")
    
    return issues

if __name__ == '__main__':
    check_all_fields()

