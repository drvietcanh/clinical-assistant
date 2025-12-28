#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script to add missing 2 fields for drugs (Batch 1)
Focus on first 30 drugs missing exactly 2 fields
"""

# List of drugs and their missing fields (first 30 from the list)
DRUGS_TO_UPDATE = [
    # 1-10
    ("Ramipril", ["contraindications_detail", "reversal_agents"]),
    ("Perindopril", ["contraindications_detail", "reversal_agents"]),
    ("Valsartan", ["contraindications_detail", "reversal_agents"]),
    ("Metoprolol", ["contraindications_detail", "renal_adjustment"]),
    ("Nebivolol", ["black_box_warnings", "contraindications_detail"]),
    ("Propranolol", ["contraindications_detail", "renal_adjustment"]),
    ("Atorvastatin", ["contraindications_detail", "renal_adjustment"]),
    ("Simvastatin", ["contraindications_detail", "renal_adjustment"]),
    ("Pravastatin", ["contraindications_detail", "renal_adjustment"]),
    ("Fluvastatin", ["contraindications_detail", "renal_adjustment"]),
    # 11-20
    ("Pitavastatin", ["contraindications_detail", "renal_adjustment"]),
    ("Ezetimibe", ["black_box_warnings", "contraindications_detail"]),
    ("Amiodarone", ["contraindications_detail", "renal_adjustment"]),
    ("Flecainide", ["contraindications_detail", "renal_adjustment"]),
    ("Propafenone", ["contraindications_detail", "renal_adjustment"]),
    ("Dronedarone", ["contraindications_detail", "renal_adjustment"]),
    ("Procainamide", ["contraindications_detail", "renal_adjustment"]),
    ("Adenosine", ["black_box_warnings", "contraindications_detail"]),
    ("Ibutilide", ["contraindications_detail", "renal_adjustment"]),
    ("Amlodipine", ["contraindications_detail", "renal_adjustment"]),
    # 21-30
    ("Furosemide", ["contraindications_detail", "renal_adjustment"]),
    ("Bumetanide", ["contraindications_detail", "renal_adjustment"]),
    ("Torsemide", ["contraindications_detail", "renal_adjustment"]),
    ("Chlorthalidone", ["contraindications_detail", "renal_adjustment"]),
    ("Warfarin", ["contraindications_detail", "renal_adjustment"]),
    ("Clopidogrel", ["contraindications_detail", "renal_adjustment"]),
    ("Ticagrelor", ["contraindications_detail", "renal_adjustment"]),
    ("Prasugrel", ["contraindications_detail", "renal_adjustment"]),
    ("Enoxaparin", ["contraindications_detail", "renal_adjustment"]),
    ("Rivaroxaban", ["contraindications_detail", "renal_adjustment"]),
]

# Template functions for each field type
def get_contraindications_detail_template(drug_name, drug_category=""):
    """Generate contraindications_detail template"""
    return {
        "tuyệt_đối": [
            f"Dị ứng {drug_name.lower()}",
        ],
        "tương_đối": [
            "Suy thận nặng (cần điều chỉnh liều)",
            "Suy gan nặng (thận trọng)",
        ],
    }

def get_reversal_agents_template(drug_name):
    """Generate reversal_agents template"""
    return {
        "available": False,
        "agents": [],
        "notes": "Không có thuốc giải độc đặc hiệu; điều trị hỗ trợ triệu chứng.",
    }

def get_renal_adjustment_template(drug_name):
    """Generate renal_adjustment template"""
    return {
        "normal": "Không đổi liều",
        "30_60": "Có thể cần giảm liều, theo dõi chức năng thận",
        "under_30": "Giảm liều hoặc tránh dùng nếu có lựa chọn khác",
        "hemodialysis": "Có thể cần bổ sung sau lọc máu (tùy thuốc)",
    }

def get_black_box_warnings_template(drug_name):
    """Generate black_box_warnings template"""
    return None  # Most drugs don't have black box warnings

def get_drug_interactions_template(drug_name):
    """Generate drug_interactions template"""
    return {
        "major": [],
        "moderate": [],
        "minor": [],
    }

# Generate the update code
print("# ======================== BATCH 1: 30 DRUGS ========================")
print("EXTRA_ENHANCED_FIELDS.update({")

for drug_name, missing_fields in DRUGS_TO_UPDATE:
    print(f'    "{drug_name}": {{')
    
    for field in missing_fields:
        if field == "contraindications_detail":
            template = get_contraindications_detail_template(drug_name)
            print(f'        "contraindications_detail": {{')
            print(f'            "tuyệt_đối": {template["tuyệt_đối"]},')
            print(f'            "tương_đối": {template["tương_đối"]},')
            print(f'        }},')
        elif field == "reversal_agents":
            template = get_reversal_agents_template(drug_name)
            print(f'        "reversal_agents": {{')
            print(f'            "available": {template["available"]},')
            print(f'            "agents": {template["agents"]},')
            print(f'            "notes": "{template["notes"]}",')
            print(f'        }},')
        elif field == "renal_adjustment":
            template = get_renal_adjustment_template(drug_name)
            print(f'        "renal_adjustment": {{')
            print(f'            "normal": "{template["normal"]}",')
            print(f'            "30_60": "{template["30_60"]}",')
            print(f'            "under_30": "{template["under_30"]}",')
            print(f'            "hemodialysis": "{template["hemodialysis"]}",')
            print(f'        }},')
        elif field == "black_box_warnings":
            template = get_black_box_warnings_template(drug_name)
            print(f'        "black_box_warnings": {template},')
        elif field == "drug_interactions":
            template = get_drug_interactions_template(drug_name)
            print(f'        "drug_interactions": {{')
            print(f'            "major": {template["major"]},')
            print(f'            "moderate": {template["moderate"]},')
            print(f'            "minor": {template["minor"]},')
            print(f'        }},')
    
    print("    },")

print("})")
print("# ======================== END BATCH 1 ========================")


