#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script to check consistency of enhanced fields across all drugs
"""

from drugs.drug_database import DRUG_DATABASE
from drugs.enhanced_fields_schema import validate_enhanced_fields

# Required fields
REQUIRED_FIELDS = [
    'mechanism_of_action',
    'monitoring',
    'precautions',
    'pharmacokinetics',
    'storage',
    'black_box_warnings'
]

def check_consistency():
    """Check consistency of enhanced fields"""
    
    print("=" * 80)
    print("KIỂM TRA TÍNH ĐỒNG NHẤT CỦA ENHANCED FIELDS")
    print("=" * 80)
    
    drugs_with_fields = []
    drugs_without_fields = []
    inconsistencies = []
    validation_errors = []
    
    for name, data in DRUG_DATABASE.items():
        # Check if drug has mechanism_of_action (indicator of enhanced fields)
        if 'mechanism_of_action' in data:
            drugs_with_fields.append(name)
            
            # Check if all required fields are present
            missing_fields = [f for f in REQUIRED_FIELDS if f not in data]
            if missing_fields:
                inconsistencies.append({
                    'drug': name,
                    'missing': missing_fields
                })
            
            # Validate enhanced fields structure
            fields = {k: data[k] for k in REQUIRED_FIELDS if k in data}
            if len(fields) == 6:
                is_valid, errors = validate_enhanced_fields(name, fields)
                if not is_valid:
                    validation_errors.extend([f"{name}: {e}" for e in errors])
        else:
            drugs_without_fields.append(name)
    
    # Print results
    print(f"\nTổng số thuốc: {len(DRUG_DATABASE)}")
    print(f"Thuốc có enhanced fields: {len(drugs_with_fields)}")
    print(f"Thuốc chưa có enhanced fields: {len(drugs_without_fields)}")
    
    if drugs_without_fields:
        print(f"\n📋 Danh sách thuốc chưa có enhanced fields ({len(drugs_without_fields)}):")
        for drug in sorted(drugs_without_fields):
            print(f"  - {drug}")
    
    if inconsistencies:
        print(f"\n⚠️  Tìm thấy {len(inconsistencies)} thuốc không đồng nhất (thiếu fields):")
        for inc in inconsistencies[:10]:
            print(f"  - {inc['drug']}: thiếu {', '.join(inc['missing'])}")
    else:
        print(f"\n✅ Tất cả {len(drugs_with_fields)} thuốc có enhanced fields đều đồng nhất!")
        print("   Tất cả đều có đủ 6 fields cơ bản:")
        for field in REQUIRED_FIELDS:
            print(f"     ✓ {field}")
    
    if validation_errors:
        print(f"\n⚠️  Tìm thấy {len(validation_errors)} lỗi validation:")
        for error in validation_errors[:10]:
            print(f"  - {error}")
        if len(validation_errors) > 10:
            print(f"  ... và {len(validation_errors) - 10} lỗi khác")
    else:
        print(f"\n✅ Tất cả enhanced fields đều hợp lệ theo schema!")
    
    # Check field types consistency
    print("\n" + "=" * 80)
    print("KIỂM TRA KIỂU DỮ LIỆU CỦA CÁC FIELDS")
    print("=" * 80)
    
    field_types = {
        'mechanism_of_action': set(),
        'monitoring': set(),
        'precautions': set(),
        'pharmacokinetics': set(),
        'storage': set(),
        'black_box_warnings': set()
    }
    
    for name, data in DRUG_DATABASE.items():
        for field in REQUIRED_FIELDS:
            if field in data:
                field_types[field].add(type(data[field]).__name__)
    
    type_issues = []
    for field, types in field_types.items():
        if len(types) > 1:
            type_issues.append(f"{field}: {', '.join(types)}")
        elif len(types) == 1:
            print(f"✅ {field}: {list(types)[0]} (đồng nhất)")
    
    if type_issues:
        print(f"\n⚠️  Tìm thấy fields có kiểu dữ liệu không đồng nhất:")
        for issue in type_issues:
            print(f"  - {issue}")
    else:
        print(f"\n✅ Tất cả fields đều có kiểu dữ liệu đồng nhất!")
    
    print("\n" + "=" * 80)
    print("KẾT LUẬN")
    print("=" * 80)
    
    if not inconsistencies and not validation_errors and not type_issues:
        print("✅ TẤT CẢ ENHANCED FIELDS ĐỀU ĐỒNG NHẤT VÀ HỢP LỆ!")
        print(f"   - {len(drugs_with_fields)}/{len(DRUG_DATABASE)} thuốc có enhanced fields")
        print(f"   - Tất cả đều có đủ 6 fields cơ bản")
        print(f"   - Tất cả đều hợp lệ theo schema")
        print(f"   - Tất cả đều có kiểu dữ liệu đồng nhất")
        return True
    else:
        print("⚠️  CÓ MỘT SỐ VẤN ĐỀ CẦN XỬ LÝ:")
        if inconsistencies:
            print(f"   - {len(inconsistencies)} thuốc thiếu fields")
        if validation_errors:
            print(f"   - {len(validation_errors)} lỗi validation")
        if type_issues:
            print(f"   - {len(type_issues)} fields có kiểu dữ liệu không đồng nhất")
        return False

if __name__ == '__main__':
    try:
        check_consistency()
    except Exception as e:
        print(f"Error: {e}")
        import traceback
        traceback.print_exc()

