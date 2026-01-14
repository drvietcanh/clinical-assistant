#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Batch Update Pregnancy Categories
Cập nhật hàng loạt pregnancy categories cho các thuốc
"""

import json
import sys
import re
from pathlib import Path
from typing import Dict, List, Any, Optional, Tuple
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

# Import pregnancy categories
from supplement_pregnancy_auto import PREGNANCY_CATEGORIES


def find_drug_in_file(file_path: Path, drug_name: str) -> Optional[Tuple[int, int]]:
    """Tìm vị trí của thuốc trong file (start_line, end_line)"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            lines = f.readlines()
        
        drug_pattern = rf'"{re.escape(drug_name)}"\s*:\s*\{{'
        
        for i, line in enumerate(lines):
            if re.search(drug_pattern, line):
                # Found start, find end
                brace_count = line.count('{') - line.count('}')
                start_line = i
                
                for j in range(i + 1, len(lines)):
                    brace_count += lines[j].count('{') - lines[j].count('}')
                    if brace_count <= 0:
                        return (start_line, j)
                
                return (start_line, len(lines))
        
        return None
    except Exception as e:
        print(f"Error reading {file_path}: {e}")
        return None


def update_pregnancy_in_file(file_path: Path, drug_name: str, pregnancy_value: str) -> bool:
    """Cập nhật pregnancy trong file"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Find drug entry
        drug_pattern = rf'"{re.escape(drug_name)}"\s*:\s*\{{'
        match = re.search(drug_pattern, content)
        
        if not match:
            return False
        
        start_pos = match.end()
        
        # Find closing brace
        brace_count = 1
        pos = start_pos
        while pos < len(content) and brace_count > 0:
            if content[pos] == '{':
                brace_count += 1
            elif content[pos] == '}':
                brace_count -= 1
            pos += 1
        
        drug_section = content[start_pos:pos-1]
        
        # Check if pregnancy exists
        preg_pattern = rf'"{re.escape("pregnancy")}"\s*:\s*'
        preg_match = re.search(preg_pattern, drug_section)
        
        if preg_match:
            # Update existing
            # Find the value (until comma or closing brace)
            value_start = preg_match.end()
            value_end = value_start
            in_quotes = False
            quote_char = None
            
            while value_end < len(drug_section):
                char = drug_section[value_end]
                
                if char in ['"', "'"] and (value_end == 0 or drug_section[value_end-1] != '\\'):
                    if not in_quotes:
                        in_quotes = True
                        quote_char = char
                    elif char == quote_char:
                        in_quotes = False
                        value_end += 1
                        # Check for comma or closing
                        while value_end < len(drug_section) and drug_section[value_end] in [' ', ',', '\n']:
                            value_end += 1
                        break
                
                value_end += 1
            
            # Replace
            old_value = drug_section[preg_match.start():value_end]
            new_value = f'"pregnancy": {json.dumps(pregnancy_value, ensure_ascii=False)}'
            if value_end < len(drug_section) and drug_section[value_end-1] == ',':
                new_value += ','
            
            drug_section = drug_section[:preg_match.start()] + new_value + drug_section[value_end:]
        else:
            # Insert new field
            # Find a good insertion point (after first field)
            first_comma = drug_section.find(',')
            if first_comma != -1:
                insert_pos = first_comma + 1
                # Add newline and indent
                indent_match = re.match(r'^\s*', drug_section[:first_comma])
                indent = indent_match.group(0) if indent_match else '        '
                new_field = f'\n{indent}"pregnancy": {json.dumps(pregnancy_value, ensure_ascii=False)},'
                drug_section = drug_section[:insert_pos] + new_field + drug_section[insert_pos:]
            else:
                # No comma, insert before closing brace
                indent_match = re.match(r'^\s*', drug_section)
                indent = indent_match.group(0) if indent_match else '        '
                new_field = f'\n{indent}"pregnancy": {json.dumps(pregnancy_value, ensure_ascii=False)},'
                drug_section = new_field + drug_section
        
        # Reconstruct content
        new_content = content[:start_pos] + drug_section + content[pos-1:]
        
        # Write back
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        
        return True
        
    except Exception as e:
        print(f"Error updating {drug_name} in {file_path}: {e}")
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
    print("BATCH UPDATE PREGNANCY CATEGORIES")
    print("="*70)
    
    # Load priority data
    priority_file = Path(__file__).parent / "manual_supplementation_priority.json"
    if not priority_file.exists():
        print("⚠️  Chưa có file priority. Chạy manual_supplementation_analyzer.py trước.")
        return
    
    with open(priority_file, 'r', encoding='utf-8') as f:
        priority_data = json.load(f)
    
    # Get drugs missing pregnancy
    p0_drugs = priority_data.get("priorities", {}).get("P0", {}).get("pregnancy", {}).get("drugs", [])
    
    results = {
        "updated": [],
        "not_found_file": [],
        "no_category": [],
        "errors": []
    }
    
    for drug_info in p0_drugs:
        drug_name = drug_info["name"]
        
        # Check if we have category
        if drug_name not in PREGNANCY_CATEGORIES:
            print(f"⚠️  {drug_name}: Không có category")
            results["no_category"].append(drug_name)
            continue
        
        category = PREGNANCY_CATEGORIES[drug_name]
        
        # Find file
        file_path = find_drug_file(drug_name)
        if not file_path:
            print(f"⚠️  {drug_name}: Không tìm thấy file")
            results["not_found_file"].append(drug_name)
            continue
        
        # Backup
        backup_dir = file_path.parent / ".backups"
        backup_dir.mkdir(exist_ok=True)
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        backup_path = backup_dir / f"{file_path.stem}_{timestamp}{file_path.suffix}"
        shutil.copy2(file_path, backup_path)
        
        # Update
        success = update_pregnancy_in_file(file_path, drug_name, category)
        
        if success:
            print(f"✅ {drug_name}: Đã cập nhật")
            results["updated"].append({
                "drug": drug_name,
                "file": str(file_path),
                "backup": str(backup_path),
                "category": category
            })
        else:
            print(f"❌ {drug_name}: Lỗi khi cập nhật")
            results["errors"].append({
                "drug": drug_name,
                "file": str(file_path),
                "error": "Update failed"
            })
    
    # Save results
    results_file = Path(__file__).parent / "batch_pregnancy_update_results.json"
    with open(results_file, 'w', encoding='utf-8') as f:
        json.dump(results, f, ensure_ascii=False, indent=2)
    
    print("\n" + "="*70)
    print("TỔNG KẾT")
    print("="*70)
    print(f"Đã cập nhật: {len(results['updated'])} thuốc")
    print(f"Không tìm thấy file: {len(results['not_found_file'])} thuốc")
    print(f"Không có category: {len(results['no_category'])} thuốc")
    print(f"Lỗi: {len(results['errors'])} thuốc")
    print("="*70)
    print(f"\nKết quả chi tiết: {results_file}")


if __name__ == "__main__":
    main()
