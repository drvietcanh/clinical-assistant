#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
List Drugs Missing Pregnancy Field
Liệt kê các thuốc thiếu field pregnancy
"""

import re
from pathlib import Path
from collections import defaultdict


def check_drug_file(file_path: Path) -> list:
    """Kiểm tra file và trả về danh sách thuốc thiếu pregnancy"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        missing_drugs = []
        
        # Tìm tất cả các drug entries
        # Pattern: "DrugName": { ... }
        drug_pattern = r'"([^"]+)":\s*\{'
        drugs = re.findall(drug_pattern, content)
        
        for drug_name in drugs:
            # Tìm entry của drug này
            drug_entry_pattern = rf'"{re.escape(drug_name)}":\s*\{{([^}}]+(?:\{{[^}}]*\}}[^}}]*)*)\}}'
            match = re.search(drug_entry_pattern, content, re.DOTALL)
            
            if match:
                drug_content = match.group(1)
                # Kiểm tra xem có "pregnancy" không
                if '"pregnancy"' not in drug_content and "'pregnancy'" not in drug_content:
                    missing_drugs.append(drug_name)
        
        return missing_drugs
        
    except Exception as e:
        print(f"Error checking {file_path}: {e}")
        return []


def main():
    """Main function"""
    print("="*70)
    print("LIỆT KÊ CÁC THUỐC THIẾU FIELD PREGNANCY")
    print("="*70)
    
    modules_dir = Path(__file__).parent / "drug_modules"
    
    # Bỏ qua biguanides.py
    skip_files = {'biguanides.py'}
    
    all_missing = []
    by_file = defaultdict(list)
    
    for py_file in modules_dir.rglob("*.py"):
        if py_file.name.startswith("__") or "backup" in str(py_file).lower():
            continue
        
        if py_file.name in skip_files:
            continue
        
        missing = check_drug_file(py_file)
        if missing:
            all_missing.extend(missing)
            by_file[py_file.name] = missing
            print(f"\n📄 {py_file.name}: {len(missing)} thuốc")
            for drug in missing[:5]:  # Chỉ hiển thị 5 đầu tiên
                print(f"   - {drug}")
            if len(missing) > 5:
                print(f"   ... và {len(missing) - 5} thuốc khác")
    
    print("\n" + "="*70)
    print("TỔNG KẾT")
    print("="*70)
    print(f"Tổng số thuốc thiếu field pregnancy: {len(all_missing)}")
    print(f"Số file có thuốc thiếu: {len(by_file)}")
    print("="*70)
    
    # Lưu vào file
    output_file = Path(__file__).parent / "missing_pregnancy_drugs.txt"
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write("DANH SÁCH THUỐC THIẾU FIELD PREGNANCY\n")
        f.write("="*70 + "\n\n")
        for file_name, drugs in sorted(by_file.items()):
            f.write(f"{file_name}:\n")
            for drug in drugs:
                f.write(f"  - {drug}\n")
            f.write("\n")
    
    print(f"\n✅ Đã lưu danh sách vào: {output_file}")


if __name__ == "__main__":
    main()
