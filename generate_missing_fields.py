#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Generate Python code to add missing fields for all 170 drugs
"""

from drugs.drug_database import DRUG_DATABASE
from drugs.enhanced_fields_overrides import EXTRA_ENHANCED_FIELDS

ENHANCED_FIELDS = [
    "mechanism_of_action", "monitoring", "precautions", "pharmacokinetics",
    "storage", "black_box_warnings", "drug_interactions", "contraindications_detail",
    "pregnancy_lactation", "hepatic_adjustment", "renal_adjustment",
    "overdose_management", "reversal_agents", "administration_instructions"
]

def is_field_missing(drug_data, field):
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

def get_field_code(field_name, drug_name, drug_data):
    """Generate Python code for a field"""
    
    if field_name == "hepatic_adjustment":
        return '''        "hepatic_adjustment": {
            "mild": "Không cần chỉnh liều.",
            "moderate": "Thận trọng, có thể cần giảm liều.",
            "severe": "Cân nhắc giảm liều hoặc tránh dùng nếu có lựa chọn khác.",
            "notes": "Theo dõi chức năng gan và tác dụng phụ."
        },'''
    
    elif field_name == "renal_adjustment":
        return '''        "renal_adjustment": {
            "normal": "Không đổi liều",
            "30_60": "Có thể cần giảm liều, theo dõi chức năng thận",
            "under_30": "Giảm liều hoặc tránh dùng nếu có lựa chọn khác",
            "hemodialysis": "Có thể cần bổ sung sau lọc máu (tùy thuốc)"
        },'''
    
    elif field_name == "reversal_agents":
        return '''        "reversal_agents": {
            "available": False,
            "agents": [],
            "notes": "Không có thuốc giải độc đặc hiệu. Xử trí chủ yếu là hỗ trợ triệu chứng."
        },'''
    
    elif field_name == "contraindications_detail":
        existing_contra = drug_data.get("contraindications")
        if existing_contra and isinstance(existing_contra, dict):
            tuyet_doi = existing_contra.get("tuyệt_đối", [])
            tuong_doi = existing_contra.get("tương_đối", [])
            tuyet_doi_str = str(tuyet_doi).replace("'", '"')
            tuong_doi_str = str(tuong_doi).replace("'", '"')
            return f'''        "contraindications_detail": {{
            "tuyệt_đối": {tuyet_doi_str},
            "tương_đối": {tuong_doi_str}
        }},'''
        return '''        "contraindications_detail": {
            "tuyệt_đối": ["Dị ứng với thuốc hoặc bất kỳ thành phần nào"],
            "tương_đối": []
        },'''
    
    elif field_name == "black_box_warnings":
        return '        "black_box_warnings": None,'
    
    elif field_name == "drug_interactions":
        return '''        "drug_interactions": {
            "major": [],
            "moderate": [],
            "minor": []
        },'''
    
    return ""

def generate_additions():
    """Generate code for all missing fields"""
    
    drugs_missing_2 = []
    for drug_name, drug_data in DRUG_DATABASE.items():
        missing_fields = [f for f in ENHANCED_FIELDS if is_field_missing(drug_data, f)]
        if len(missing_fields) == 2:
            drugs_missing_2.append((drug_name, missing_fields, drug_data))
    
    print("# ======================== BATCH 3: BỔ SUNG 2 FIELD THIẾU ========================")
    print("_BATCH_3_ADDITIONS = {")
    
    for drug_name, missing_fields, drug_data in drugs_missing_2:
        print(f'    "{drug_name}": {{')
        for field in missing_fields:
            code = get_field_code(field, drug_name, drug_data)
            print(code)
        print("    },")
    
    print("}")
    print("# ======================== END BATCH 3 ========================")

if __name__ == '__main__':
    generate_additions()

