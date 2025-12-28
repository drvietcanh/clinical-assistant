#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Smart script to generate missing fields for Batch 2 (drugs 31-60)
"""

from drugs.drug_database import DRUG_DATABASE

# Next 30 drugs from the list (31-60)
DRUGS_TO_UPDATE = [
    ("Apixaban", ["contraindications_detail", "renal_adjustment"]),
    ("Dabigatran", ["contraindications_detail", "renal_adjustment"]),
    ("Edoxaban", ["contraindications_detail", "renal_adjustment"]),
    ("Alirocumab", ["contraindications_detail", "renal_adjustment"]),
    ("Evolocumab", ["contraindications_detail", "renal_adjustment"]),
    ("Inclisiran", ["contraindications_detail", "renal_adjustment"]),
    ("Sitagliptin", ["black_box_warnings", "contraindications_detail"]),
    ("Linagliptin", ["black_box_warnings", "contraindications_detail"]),
    ("Saxagliptin", ["black_box_warnings", "contraindications_detail"]),
    ("Alogliptin", ["black_box_warnings", "contraindications_detail"]),
    ("Insulin", ["contraindications_detail", "renal_adjustment"]),
    ("Empagliflozin", ["black_box_warnings", "contraindications_detail"]),
    ("Dapagliflozin", ["black_box_warnings", "contraindications_detail"]),
    ("Glibenclamide", ["contraindications_detail", "renal_adjustment"]),
    ("Gliclazide", ["contraindications_detail", "renal_adjustment"]),
    ("Acarbose", ["black_box_warnings", "contraindications_detail"]),
    ("Miglitol", ["black_box_warnings", "contraindications_detail"]),
    ("Loperamide", ["contraindications_detail", "renal_adjustment"]),
    ("Bismuth subsalicylate", ["contraindications_detail", "renal_adjustment"]),
    ("Cimetidine", ["contraindications_detail", "reversal_agents"]),
    ("Sucralfate", ["contraindications_detail", "reversal_agents"]),
    ("Lansoprazole", ["contraindications_detail", "reversal_agents"]),
    ("Esomeprazole", ["contraindications_detail", "reversal_agents"]),
    ("Metoclopramide", ["contraindications_detail", "reversal_agents"]),
    ("Domperidone", ["contraindications_detail", "reversal_agents"]),
    ("Ondansetron", ["contraindications_detail", "reversal_agents"]),
    ("Vonoprazan", ["contraindications_detail", "renal_adjustment"]),
    ("Tegoprazan", ["contraindications_detail", "renal_adjustment"]),
    ("Lactulose", ["black_box_warnings", "drug_interactions"]),
    ("Polyethylene glycol 3350", ["black_box_warnings", "drug_interactions"]),
]

print("# ======================== BATCH 2: 30 DRUGS (31-60) ========================")
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
        
        elif field == "drug_interactions":
            print(f'        "drug_interactions": {{')
            print(f'            "major": [],')
            print(f'            "moderate": [],')
            print(f'            "minor": [],')
            print(f'        }},')
    
    print("    },")

print("})")
print("# ======================== END BATCH 2 ========================")

