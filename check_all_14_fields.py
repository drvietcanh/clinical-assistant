#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script to check if drugs have all 14 fields (6 basic + 8 optional)
"""

from drugs.drug_database import DRUG_DATABASE

# 6 Fields cơ bản
BASIC_FIELDS = [
    'mechanism_of_action',
    'monitoring',
    'precautions',
    'pharmacokinetics',
    'storage',
    'black_box_warnings'
]

# 8 Fields tùy chọn
OPTIONAL_FIELDS = [
    'drug_interactions',
    'contraindications',  # Note: must be dict, not list
    'pregnancy_lactation',
    'hepatic_adjustment',
    'overdose_management',
    'reversal_agents',
    'administration_instructions',
    'references'
]

ALL_14_FIELDS = BASIC_FIELDS + OPTIONAL_FIELDS

def check_all_14_fields():
    """Check which drugs have all 14 fields"""
    
    total = len(DRUG_DATABASE)
    
    # Thuốc có đủ 6 fields cơ bản
    has_basic = []
    missing_basic = []
    
    for name, data in DRUG_DATABASE.items():
        has_all_basic = True
        for field in BASIC_FIELDS:
            if field not in data:
                has_all_basic = False
                break
        if has_all_basic:
            has_basic.append(name)
        else:
            missing_basic.append(name)
    
    # Thuốc có đủ 8 fields tùy chọn (trong số các thuốc đã có 6 fields cơ bản)
    has_all_14 = []
    has_6_but_missing_optional = []
    
    for name in has_basic:
        data = DRUG_DATABASE[name]
        has_all_optional = True
        
        for field in OPTIONAL_FIELDS:
            if field not in data:
                has_all_optional = False
                break
            # Special check for contraindications - must be dict
            if field == 'contraindications':
                if not isinstance(data[field], dict):
                    has_all_optional = False
                    break
        
        if has_all_optional:
            has_all_14.append(name)
        else:
            has_6_but_missing_optional.append(name)
    
    # Print results
    print("=" * 80)
    print("KIỂM TRA ĐẦY ĐỦ 14 FIELDS (6 CƠ BẢN + 8 TÙY CHỌN)")
    print("=" * 80)
    
    print(f"\n📊 TỔNG QUAN:")
    print(f"   - Tổng số thuốc: {total}")
    print(f"   - ✅ Có đủ 6 fields cơ bản: {len(has_basic)}/{total} ({len(has_basic)*100//total}%)")
    print(f"   - ✅ Có đủ 14 fields (6 cơ bản + 8 tùy chọn): {len(has_all_14)}/{total} ({len(has_all_14)*100//total}%)")
    print(f"   - ⚠️  Có 6 fields cơ bản nhưng thiếu fields tùy chọn: {len(has_6_but_missing_optional)}")
    print(f"   - ❌ Thiếu fields cơ bản: {len(missing_basic)}")
    
    if has_all_14:
        print(f"\n✅ {len(has_all_14)} THUỐC CÓ ĐỦ 14 FIELDS:")
        for name in sorted(has_all_14):
            print(f"   - {name}")
    
    if has_6_but_missing_optional:
        print(f"\n⚠️  {len(has_6_but_missing_optional)} THUỐC CÓ 6 FIELDS CƠ BẢN NHƯNG THIẾU FIELDS TÙY CHỌN:")
        for name in sorted(has_6_but_missing_optional)[:10]:
            data = DRUG_DATABASE[name]
            missing = [f for f in OPTIONAL_FIELDS if f not in data or 
                     (f == 'contraindications' and not isinstance(data.get(f), dict))]
            print(f"   - {name}: thiếu {', '.join(missing)}")
        if len(has_6_but_missing_optional) > 10:
            print(f"   ... và {len(has_6_but_missing_optional) - 10} thuốc khác")
    
    # Chi tiết từng field
    print(f"\n📋 CHI TIẾT TỪNG FIELD:")
    for field in ALL_14_FIELDS:
        count = 0
        for data in DRUG_DATABASE.values():
            if field in data:
                if field == 'contraindications':
                    if isinstance(data[field], dict):
                        count += 1
                else:
                    count += 1
        print(f"   - {field}: {count}/{total} ({count*100//total}%)")
    
    return {
        'has_all_14': has_all_14,
        'has_6_but_missing_optional': has_6_but_missing_optional,
        'missing_basic': missing_basic
    }

if __name__ == '__main__':
    check_all_14_fields()

