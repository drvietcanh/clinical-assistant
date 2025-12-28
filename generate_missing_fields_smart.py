#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Smart script to generate missing fields by using existing data when available
"""

from drugs.drug_database import DRUG_DATABASE

# First 30 drugs from the list
DRUGS_TO_UPDATE = [
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

print("# ======================== BATCH 1: 30 DRUGS (Smart Generation) ========================")
print("EXTRA_ENHANCED_FIELDS.update({")

for drug_name, missing_fields in DRUGS_TO_UPDATE:
    drug_data = DRUG_DATABASE.get(drug_name, {})
    print(f'    "{drug_name}": {{')
    
    for field in missing_fields:
        if field == "contraindications_detail":
            # Use existing contraindications if available
            if "contraindications" in drug_data and isinstance(drug_data["contraindications"], dict):
                existing = drug_data["contraindications"]
                print(f'        "contraindications_detail": {{')
                print(f'            "tuyệt_đối": {existing.get("tuyệt_đối", [])},')
                print(f'            "tương_đối": {existing.get("tương_đối", [])},')
                print(f'        }},')
            else:
                # Generic template
                print(f'        "contraindications_detail": {{')
                print(f'            "tuyệt_đối": ["Dị ứng {drug_name.lower()}"],')
                print(f'            "tương_đối": ["Suy thận nặng (cần điều chỉnh liều)", "Suy gan nặng (thận trọng)"],')
                print(f'        }},')
        
        elif field == "reversal_agents":
            # Use existing if available
            if "reversal_agents" in drug_data:
                existing = drug_data["reversal_agents"]
                if existing is None:
                    print(f'        "reversal_agents": {{')
                    print(f'            "available": False,')
                    print(f'            "agents": [],')
                    print(f'            "notes": "Không có thuốc giải độc đặc hiệu; điều trị hỗ trợ triệu chứng.",')
                    print(f'        }},')
                elif isinstance(existing, dict):
                    # Already has structure, just ensure it's complete
                    print(f'        "reversal_agents": {{')
                    print(f'            "available": {existing.get("available", False)},')
                    print(f'            "agents": {existing.get("agents", [])},')
                    print(f'            "notes": "{existing.get("notes", "Không có thuốc giải độc đặc hiệu; điều trị hỗ trợ triệu chứng.")}",')
                    print(f'        }},')
            else:
                print(f'        "reversal_agents": {{')
                print(f'            "available": False,')
                print(f'            "agents": [],')
                print(f'            "notes": "Không có thuốc giải độc đặc hiệu; điều trị hỗ trợ triệu chứng.",')
                print(f'        }},')
        
        elif field == "renal_adjustment":
            print(f'        "renal_adjustment": {{')
            print(f'            "normal": "Không đổi liều",')
            print(f'            "30_60": "Có thể cần giảm liều, theo dõi chức năng thận",')
            print(f'            "under_30": "Giảm liều hoặc tránh dùng nếu có lựa chọn khác",')
            print(f'            "hemodialysis": "Có thể cần bổ sung sau lọc máu (tùy thuốc)",')
            print(f'        }},')
        
        elif field == "black_box_warnings":
            # Use existing if available
            if "black_box_warnings" in drug_data:
                existing = drug_data["black_box_warnings"]
                if existing is None:
                    print(f'        "black_box_warnings": None,')
                elif isinstance(existing, str) and existing.strip():
                    print(f'        "black_box_warnings": "{existing}",')
                else:
                    print(f'        "black_box_warnings": None,')
            else:
                print(f'        "black_box_warnings": None,')
    
    print("    },")

print("})")
print("# ======================== END BATCH 1 ========================")


