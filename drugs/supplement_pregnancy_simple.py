#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Simple Pregnancy Supplementation
Bổ sung pregnancy categories đơn giản - cập nhật DRUG_DATABASE và file nguồn
"""

import json
import sys
import re
from pathlib import Path
from typing import Dict, List, Any, Optional
from datetime import datetime
import shutil

# Add project root to path
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    from drugs.drug_database import DRUG_DATABASE
except ImportError:
    sys.path.insert(0, str(Path(__file__).parent))
    from drug_database import DRUG_DATABASE

# Import pregnancy categories từ file trước
from supplement_pregnancy_auto import PREGNANCY_CATEGORIES


def update_drug_database():
    """Cập nhật DRUG_DATABASE với pregnancy categories"""
    updated = []
    not_found = []
    
    for drug_name, category in PREGNANCY_CATEGORIES.items():
        if drug_name in DRUG_DATABASE:
            drug_data = DRUG_DATABASE[drug_name]
            if isinstance(drug_data, dict):
                # Check if already has pregnancy
                current_preg = drug_data.get("pregnancy", "")
                if not current_preg or current_preg.strip() == "" or current_preg == "Đang cập nhật":
                    drug_data["pregnancy"] = category
                    updated.append(drug_name)
                    print(f"✅ {drug_name}: Đã cập nhật pregnancy")
                else:
                    print(f"⏭️  {drug_name}: Đã có pregnancy = {current_preg[:50]}")
        else:
            not_found.append(drug_name)
    
    return updated, not_found


def find_and_update_in_file(file_path: Path, drug_name: str, field: str, value: str) -> bool:
    """Tìm và cập nhật field trong file Python"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            lines = f.readlines()
        
        # Find drug entry
        drug_pattern = rf'"{re.escape(drug_name)}"\s*:\s*\{{'
        in_drug = False
        brace_count = 0
        start_line = -1
        
        for i, line in enumerate(lines):
            if re.search(drug_pattern, line):
                in_drug = True
                start_line = i
                brace_count = line.count('{') - line.count('}')
                continue
            
            if in_drug:
                brace_count += line.count('{') - line.count('}')
                
                # Check if field exists
                field_pattern = rf'"{re.escape(field)}"\s*:'
                if re.search(field_pattern, line):
                    # Update existing field
                    # Find the value part
                    colon_pos = line.find(':')
                    if colon_pos != -1:
                        # Replace the value
                        value_part = line[colon_pos+1:].strip()
                        # Remove trailing comma if exists
                        if value_part.endswith(','):
                            new_line = line[:colon_pos+1] + f' {json.dumps(value, ensure_ascii=False)},\n'
                        else:
                            new_line = line[:colon_pos+1] + f' {json.dumps(value, ensure_ascii=False)}\n'
                        lines[i] = new_line
                        # Write back
                        with open(file_path, 'w', encoding='utf-8') as f:
                            f.writelines(lines)
                        return True
                
                if brace_count <= 0:
                    # End of drug entry, insert field before closing brace
                    # Find a good place to insert (after last field before closing brace)
                    insert_line = i - 1
                    while insert_line > start_line:
                        if lines[insert_line].strip() and not lines[insert_line].strip().startswith('}'):
                            # Insert after this line
                            indent = len(lines[insert_line]) - len(lines[insert_line].lstrip())
                            new_line = ' ' * indent + f'"{field}": {json.dumps(value, ensure_ascii=False)},\n'
                            lines.insert(insert_line + 1, new_line)
                            # Write back
                            with open(file_path, 'w', encoding='utf-8') as f:
                                f.writelines(lines)
                            return True
                        insert_line -= 1
                    break
        
        return False
        
    except Exception as e:
        print(f"Error: {e}")
        return False


def find_drug_file(drug_name: str) -> Optional[Path]:
    """Tìm file chứa thuốc"""
    modules_dir = Path(__file__).parent / "drug_modules"
    
    for py_file in modules_dir.rglob("*.py"):
        if py_file.name.startswith("__"):
            continue
        try:
            with open(py_file, 'r', encoding='utf-8') as f:
                content = f.read()
                if f'"{drug_name}"' in content:
                    return py_file
        except:
            continue
    
    return None


def main():
    """Main function"""
    print("="*70)
    print("BỔ SUNG PREGNANCY CATEGORIES")
    print("="*70)
    
    # Step 1: Update DRUG_DATABASE
    print("\nBước 1: Cập nhật DRUG_DATABASE...")
    updated, not_found = update_drug_database()
    
    print(f"\n✅ Đã cập nhật {len(updated)} thuốc trong DRUG_DATABASE")
    if not_found:
        print(f"⚠️  {len(not_found)} thuốc không tìm thấy trong DRUG_DATABASE")
    
    # Step 2: Update source files
    print("\nBước 2: Cập nhật file nguồn...")
    
    results = {
        "updated_files": [],
        "not_found_files": [],
        "errors": []
    }
    
    for drug_name in updated:
        category = PREGNANCY_CATEGORIES[drug_name]
        
        # Find file
        file_path = find_drug_file(drug_name)
        if not file_path:
            results["not_found_files"].append(drug_name)
            print(f"⚠️  {drug_name}: Không tìm thấy file")
            continue
        
        # Backup
        backup_dir = file_path.parent / ".backups"
        backup_dir.mkdir(exist_ok=True)
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        backup_path = backup_dir / f"{file_path.stem}_{timestamp}{file_path.suffix}"
        shutil.copy2(file_path, backup_path)
        
        # Update
        success = find_and_update_in_file(file_path, drug_name, "pregnancy", category)
        
        if success:
            results["updated_files"].append({
                "drug": drug_name,
                "file": str(file_path),
                "backup": str(backup_path)
            })
            print(f"✅ {drug_name}: Đã cập nhật file {file_path.name}")
        else:
            results["errors"].append({
                "drug": drug_name,
                "file": str(file_path),
                "error": "Không thể cập nhật"
            })
            print(f"❌ {drug_name}: Lỗi khi cập nhật file")
    
    # Save results
    results_file = Path(__file__).parent / "pregnancy_supplement_simple_results.json"
    with open(results_file, 'w', encoding='utf-8') as f:
        json.dump(results, f, ensure_ascii=False, indent=2)
    
    print("\n" + "="*70)
    print("TỔNG KẾT")
    print("="*70)
    print(f"Đã cập nhật file: {len(results['updated_files'])} thuốc")
    print(f"Không tìm thấy file: {len(results['not_found_files'])} thuốc")
    print(f"Lỗi: {len(results['errors'])} thuốc")
    print("="*70)
    print(f"\nKết quả chi tiết: {results_file}")
    print("\n⚠️  LƯU Ý: Các thay đổi trong DRUG_DATABASE chỉ tồn tại trong memory.")
    print("   Cần restart Python để reload từ file nguồn đã cập nhật.")


if __name__ == "__main__":
    main()
