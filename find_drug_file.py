#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script helper để tìm file chứa thuốc và hiển thị thông tin
"""

import sys
from pathlib import Path

# Add project root to path
project_root = Path(__file__).parent
sys.path.insert(0, str(project_root))

from drugs.drug_database import DRUG_DATABASE

def find_drug_file(drug_name):
    """Tìm file chứa thuốc bằng cách import và kiểm tra"""
    import importlib
    import os
    
    # Search in drug_modules
    drug_modules_path = Path("drugs/drug_modules")
    if not drug_modules_path.exists():
        print(f"❌ Không tìm thấy thư mục drugs/drug_modules")
        return None
    
    # Search recursively
    for py_file in drug_modules_path.rglob("*.py"):
        if py_file.name == "__init__.py":
            continue
        
        try:
            with open(py_file, 'r', encoding='utf-8') as f:
                content = f.read()
                if f'"{drug_name}"' in content or f"'{drug_name}'" in content:
                    return str(py_file.relative_to(project_root))
        except:
            continue
    
    return None

def show_drug_info(drug_name):
    """Hiển thị thông tin về thuốc"""
    if drug_name not in DRUG_DATABASE:
        print(f"❌ Không tìm thấy thuốc: {drug_name}")
        return
    
    drug_data = DRUG_DATABASE[drug_name]
    
    # Find file
    file_path = find_drug_file(drug_name)
    
    print("=" * 80)
    print(f"📋 THÔNG TIN THUỐC: {drug_name}")
    print("=" * 80)
    
    if file_path:
        print(f"📁 File: {file_path}")
    else:
        print(f"⚠️  Không tìm thấy file (có thể trong enhanced_fields_overrides.py)")
    
    print(f"\n📦 Nhóm: {drug_data.get('group', 'N/A')}")
    print(f"🇻🇳 Tên tiếng Việt: {drug_data.get('vietnamese_name', 'N/A')}")
    
    # Check missing fields
    ENHANCED_FIELDS = [
        "mechanism_of_action", "monitoring", "precautions", "pharmacokinetics",
        "storage", "black_box_warnings", "drug_interactions", "contraindications_detail",
        "pregnancy_lactation", "hepatic_adjustment", "renal_adjustment",
        "overdose_management", "reversal_agents", "administration_instructions"
    ]
    
    missing = []
    for field in ENHANCED_FIELDS:
        if field not in drug_data or drug_data[field] is None or \
           (isinstance(drug_data[field], (list, dict)) and len(drug_data[field]) == 0):
            missing.append(field)
    
    if missing:
        print(f"\n❌ Thiếu {len(missing)} field: {', '.join(missing)}")
    else:
        print(f"\n✅ Đã có đầy đủ 14 enhanced fields")
    
    # Check if has contraindications dict
    if "contraindications" in drug_data and isinstance(drug_data["contraindications"], dict):
        print(f"\n✅ Có 'contraindications' dict - có thể copy sang 'contraindications_detail'")
    
    # Check if has drug_interactions_detail
    if "drug_interactions_detail" in drug_data:
        print(f"✅ Có 'drug_interactions_detail' - có thể copy sang 'drug_interactions'")

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage: python find_drug_file.py <drug_name>")
        print("\nVí dụ:")
        print("  python find_drug_file.py Amoxicillin")
        print("  python find_drug_file.py 'Sertraline'")
        sys.exit(1)
    
    drug_name = sys.argv[1]
    show_drug_info(drug_name)

