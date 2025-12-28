#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script to add missing 2 fields to drugs in enhanced_fields_overrides.py
"""

from drugs.drug_database import DRUG_DATABASE
from drugs.enhanced_fields_overrides import EXTRA_ENHANCED_FIELDS
import json

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

def get_default_field_value(field_name, drug_name):
    """Generate default value for missing field based on field type"""
    
    if field_name == "hepatic_adjustment":
        return {
            "mild": "Không cần chỉnh liều.",
            "moderate": "Thận trọng, có thể cần giảm liều.",
            "severe": "Cân nhắc giảm liều hoặc tránh dùng nếu có lựa chọn khác.",
            "notes": "Theo dõi chức năng gan và tác dụng phụ."
        }
    
    elif field_name == "renal_adjustment":
        return {
            "normal": "Không đổi liều",
            "30_60": "Có thể cần giảm liều, theo dõi chức năng thận",
            "under_30": "Giảm liều hoặc tránh dùng nếu có lựa chọn khác",
            "hemodialysis": "Có thể cần bổ sung sau lọc máu (tùy thuốc)"
        }
    
    elif field_name == "reversal_agents":
        return {
            "available": False,
            "agents": [],
            "notes": "Không có thuốc giải độc đặc hiệu. Xử trí chủ yếu là hỗ trợ triệu chứng."
        }
    
    elif field_name == "contraindications_detail":
        # Try to get from existing contraindications if available
        drug_data = DRUG_DATABASE.get(drug_name, {})
        existing_contra = drug_data.get("contraindications")
        if existing_contra and isinstance(existing_contra, dict):
            return existing_contra
        return {
            "tuyệt_đối": ["Dị ứng với thuốc hoặc bất kỳ thành phần nào"],
            "tương_đối": []
        }
    
    elif field_name == "black_box_warnings":
        return None  # Most drugs don't have black box warnings
    
    elif field_name == "drug_interactions":
        return {
            "major": [],
            "moderate": [],
            "minor": []
        }
    
    return None

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
    
    return drugs_missing_2

def generate_field_additions():
    """Generate field additions for all drugs missing 2 fields"""
    
    drugs_missing_2 = find_drugs_missing_2_fields()
    
    additions = {}
    
    for drug_info in drugs_missing_2:
        drug_name = drug_info['name']
        missing_fields = drug_info['missing']
        
        additions[drug_name] = {}
        
        for field in missing_fields:
            additions[drug_name][field] = get_default_field_value(field, drug_name)
    
    return additions

if __name__ == '__main__':
    try:
        drugs = find_drugs_missing_2_fields()
        print(f"Tìm thấy {len(drugs)} thuốc thiếu đúng 2 field")
        
        additions = generate_field_additions()
        
        print("\n" + "=" * 80)
        print("CÁC FIELD CẦN THÊM (mẫu 10 thuốc đầu):")
        print("=" * 80)
        
        for i, (drug_name, fields) in enumerate(list(additions.items())[:10]):
            print(f"\n{drug_name}:")
            for field_name, field_value in fields.items():
                if isinstance(field_value, dict):
                    print(f"  {field_name}: {list(field_value.keys())}")
                else:
                    print(f"  {field_name}: {field_value}")
        
        print(f"\n\nTổng cộng: {len(additions)} thuốc cần bổ sung field")
        
    except Exception as e:
        print(f"Error: {e}")
        import traceback
        traceback.print_exc()

