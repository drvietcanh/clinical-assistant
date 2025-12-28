#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script tự động bổ sung 2 field còn thiếu cho các thuốc
Dựa trên pattern và dữ liệu có sẵn
"""

import sys
from pathlib import Path

# Add project root to path
project_root = Path(__file__).parent
sys.path.insert(0, str(project_root))

from drugs.drug_database import DRUG_DATABASE

# Template cho các field
TEMPLATES = {
    "contraindications_detail": {
        "from_contraindications": True,  # Copy từ contraindications nếu có
        "default": {
            "tuyệt_đối": ["Dị ứng thuốc hoặc thành phần"],
            "tương_đối": []
        }
    },
    "renal_adjustment": {
        "default": {
            "normal": "Không cần chỉnh liều",
            "30_60": "Thận trọng, có thể cần giảm liều",
            "under_30": "Thận trọng, giảm liều (thải trừ qua thận)",
            "dialysis": "Thận trọng, giảm liều. Thuốc không được lọc sạch hiệu quả qua thẩm phân máu.",
            "notes": "Thuốc thải trừ qua thận. Suy thận có thể tăng nguy cơ tích lũy."
        }
    },
    "reversal_agents": {
        "default": {
            "available": False,
            "agents": [],
            "notes": "Không có antidote đặc hiệu. Điều trị quá liều chủ yếu là hỗ trợ."
        }
    },
    "black_box_warnings": {
        "default": None
    },
    "drug_interactions": {
        "from_drug_interactions_detail": True,  # Copy từ drug_interactions_detail nếu có
        "default": {
            "major": [],
            "moderate": [],
            "minor": []
        }
    }
}

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

def add_missing_field(drug_name, drug_data, field_name):
    """Add missing field based on template and existing data"""
    template = TEMPLATES.get(field_name, {})
    
    if field_name == "contraindications_detail":
        # Copy từ contraindications nếu có
        if "contraindications" in drug_data and isinstance(drug_data["contraindications"], dict):
            drug_data[field_name] = {
                "tuyệt_đối": drug_data["contraindications"].get("tuyệt_đối", []).copy(),
                "tương_đối": drug_data["contraindications"].get("tương_đối", []).copy()
            }
        else:
            drug_data[field_name] = template["default"].copy()
    
    elif field_name == "renal_adjustment":
        # Dùng template mặc định
        drug_data[field_name] = template["default"].copy()
        # Cập nhật notes với tên thuốc
        if "notes" in drug_data[field_name]:
            drug_data[field_name]["notes"] = drug_data[field_name]["notes"].replace("Thuốc", drug_name)
    
    elif field_name == "reversal_agents":
        # Dùng template mặc định
        drug_data[field_name] = template["default"].copy()
    
    elif field_name == "black_box_warnings":
        # Set to None
        drug_data[field_name] = None
    
    elif field_name == "drug_interactions":
        # Copy từ drug_interactions_detail nếu có
        if "drug_interactions_detail" in drug_data and isinstance(drug_data["drug_interactions_detail"], dict):
            drug_data[field_name] = {
                "major": drug_data["drug_interactions_detail"].get("major", []).copy(),
                "moderate": drug_data["drug_interactions_detail"].get("moderate", []).copy(),
                "minor": drug_data["drug_interactions_detail"].get("minor", []).copy()
            }
        else:
            drug_data[field_name] = template["default"].copy()

def main():
    """Main function to add missing fields"""
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
    
    drugs_missing_2 = []
    drugs_fixed = []
    
    # Find drugs missing exactly 2 fields
    for drug_name, drug_data in DRUG_DATABASE.items():
        missing_fields = [f for f in ENHANCED_FIELDS if is_field_missing(drug_data, f)]
        
        if len(missing_fields) == 2:
            drugs_missing_2.append({
                'name': drug_name,
                'missing': missing_fields
            })
            
            # Add missing fields
            for field in missing_fields:
                add_missing_field(drug_name, drug_data, field)
            
            drugs_fixed.append(drug_name)
    
    print(f"Đã bổ sung field cho {len(drugs_fixed)} thuốc:")
    for drug in drugs_fixed[:20]:  # Show first 20
        print(f"  - {drug}")
    if len(drugs_fixed) > 20:
        print(f"  ... và {len(drugs_fixed) - 20} thuốc khác")
    
    print(f"\nTổng số thuốc đã xử lý: {len(drugs_fixed)}")
    print("\n⚠️  LƯU Ý: Script này chỉ tạo cấu trúc field cơ bản.")
    print("Cần kiểm tra và bổ sung nội dung chi tiết cho từng thuốc!")

if __name__ == '__main__':
    main()

