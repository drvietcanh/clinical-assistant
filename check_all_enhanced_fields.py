#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script to check all 14 enhanced fields in drug database
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

def check_enhanced_fields():
    """Check all drugs for missing enhanced fields"""
    
    results = {}
    for field in ENHANCED_FIELDS:
        results[field] = []
    
    for drug_name, drug_data in DRUG_DATABASE.items():
        for field in ENHANCED_FIELDS:
            has_field = field in drug_data and drug_data.get(field) is not None
            if not has_field:
                results[field].append(drug_name)
            else:
                # Check if it's not empty
                value = drug_data.get(field)
                if isinstance(value, str) and not value.strip():
                    results[field].append(drug_name)
                elif isinstance(value, (list, dict)) and len(value) == 0:
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
    
    # Also check risk_flags and guideline_tags
    missing_risk_flags = []
    missing_guideline_tags = []
    missing_both = []
    
    for drug_name, drug_data in DRUG_DATABASE.items():
        has_risk_flags = 'risk_flags' in drug_data and drug_data.get('risk_flags') is not None
        has_guideline_tags = 'guideline_tags' in drug_data and drug_data.get('guideline_tags') is not None
        
        if not has_risk_flags and not has_guideline_tags:
            missing_both.append(drug_name)
        elif not has_risk_flags:
            missing_risk_flags.append(drug_name)
        elif not has_guideline_tags:
            missing_guideline_tags.append(drug_name)
    
    print(f"\n✗ risk_flags{' ' * 30} | Thiếu: {len(missing_both) + len(missing_risk_flags):3d}")
    print(f"✗ guideline_tags{' ' * 28} | Thiếu: {len(missing_both) + len(missing_guideline_tags):3d}")
    print(f"✗ risk_flags + guideline_tags{' ' * 18} | Thiếu: {len(missing_both):3d}")
    
    # Summary
    print("\n" + "=" * 80)
    print("TÓM TẮT")
    print("=" * 80)
    
    all_complete = True
    for field in ENHANCED_FIELDS:
        if len(results[field]) > 0:
            all_complete = False
            break
    
    if all_complete and len(missing_both) == 0 and len(missing_risk_flags) == 0 and len(missing_guideline_tags) == 0:
        print("✓ Tất cả các field đã đầy đủ!")
    else:
        print("Các công việc cần làm:")
        print("\n1. BỔ SUNG RISK_FLAGS VÀ GUIDELINE_TAGS:")
        print(f"   - {len(missing_both)} thuốc thiếu cả hai")
        print(f"   - {len(missing_risk_flags)} thuốc chỉ thiếu risk_flags")
        print(f"   - {len(missing_guideline_tags)} thuốc chỉ thiếu guideline_tags")
        
        print("\n2. BỔ SUNG CÁC ENHANCED FIELDS CÒN THIẾU:")
        for field in ENHANCED_FIELDS:
            if len(results[field]) > 0:
                print(f"   - {field}: {len(results[field])} thuốc")
    
    return results, missing_both, missing_risk_flags, missing_guideline_tags

if __name__ == '__main__':
    try:
        results, missing_both, missing_rf, missing_gt = check_enhanced_fields()
    except Exception as e:
        print(f"Error: {e}")
        import traceback
        traceback.print_exc()

