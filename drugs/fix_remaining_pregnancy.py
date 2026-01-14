#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Fix Remaining Pregnancy Updates
Sửa các thuốc còn lại với file đúng
"""

import json
import sys
import re
from pathlib import Path
from datetime import datetime
import shutil

# Import pregnancy categories
from supplement_pregnancy_auto import PREGNANCY_CATEGORIES

# Map drugs to correct files
DRUG_FILE_MAP = {
    "Omeprazole": "drugs/drug_modules/gastrointestinal/proton_pump_inhibitors.py",
    "Carbamazepine": "drugs/drug_modules/neurological/anticonvulsants.py",
    "Calcium": "drugs/drug_modules/supportive/calciums.py",
    "Ceftriaxone": "drugs/drug_modules/infectious_other/beta_lactams.py",
    "Prednisone": "drugs/drug_modules/endocrinology_other/corticosteroids/short_acting.py",
    "Dexamethasone": "drugs/drug_modules/endocrinology_other/corticosteroids/long_acting.py",
    "Atropine": "drugs/drug_modules/emergency/anticholinergics.py",
    "Allopurinol": "drugs/drug_modules/miscellaneous/gout_medications.py",
    "Cyclosporine": "drugs/drug_modules/immunology/immunosuppressants.py",
    "Methotrexate": "drugs/drug_modules/miscellaneous/dmards_rheumatology.py",
    "Ethanol": "drugs/drug_modules/toxicology/antidotes.py"
}


def update_pregnancy_in_file(file_path: Path, drug_name: str, pregnancy_value: str) -> bool:
    """Cập nhật pregnancy trong file"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Find drug entry
        drug_pattern = rf'"{re.escape(drug_name)}"\s*:\s*\{{'
        match = re.search(drug_pattern, content)
        
        if not match:
            print(f"  ⚠️  Không tìm thấy {drug_name} trong {file_path.name}")
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
            # Update existing - find the value
            value_start = preg_match.end()
            # Find end of value (comma or newline before next field or closing brace)
            value_end = value_start
            in_quotes = False
            quote_char = None
            
            # Try to find the end of the string value
            while value_end < len(drug_section):
                char = drug_section[value_end]
                
                if char in ['"', "'"] and (value_end == 0 or drug_section[value_end-1] != '\\'):
                    if not in_quotes:
                        in_quotes = True
                        quote_char = char
                    elif char == quote_char:
                        in_quotes = False
                        value_end += 1
                        # Skip whitespace and comma
                        while value_end < len(drug_section) and drug_section[value_end] in [' ', ',', '\n', '\r']:
                            value_end += 1
                        break
                
                value_end += 1
            
            # Replace
            old_value = drug_section[preg_match.start():value_end]
            new_value = f'"pregnancy": {json.dumps(pregnancy_value, ensure_ascii=False)}'
            # Preserve comma if it was there
            if value_end < len(drug_section) and ',' in drug_section[value_end-5:value_end]:
                new_value += ','
            
            drug_section = drug_section[:preg_match.start()] + new_value + drug_section[value_end:]
        else:
            # Insert new field - find first comma or end
            first_comma = drug_section.find(',')
            if first_comma != -1:
                insert_pos = first_comma + 1
                # Get indent
                indent_match = re.match(r'^\s*', drug_section[:first_comma])
                indent = indent_match.group(0) if indent_match else '        '
                new_field = f'\n{indent}"pregnancy": {json.dumps(pregnancy_value, ensure_ascii=False)},'
                drug_section = drug_section[:insert_pos] + new_field + drug_section[insert_pos:]
            else:
                # No comma, add before closing
                indent_match = re.match(r'^\s*', drug_section)
                indent = indent_match.group(0) if indent_match else '        '
                new_field = f'\n{indent}"pregnancy": {json.dumps(pregnancy_value, ensure_ascii=False)},'
                drug_section = new_field + drug_section
        
        # Reconstruct
        new_content = content[:start_pos] + drug_section + content[pos-1:]
        
        # Write back
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        
        return True
        
    except Exception as e:
        print(f"  ❌ Lỗi: {e}")
        return False


def main():
    """Main function"""
    print("="*70)
    print("SỬA CÁC THUỐC CÒN LẠI")
    print("="*70)
    
    results = {
        "updated": [],
        "errors": []
    }
    
    for drug_name, file_path_str in DRUG_FILE_MAP.items():
        if drug_name not in PREGNANCY_CATEGORIES:
            print(f"⚠️  {drug_name}: Không có category")
            continue
        
        category = PREGNANCY_CATEGORIES[drug_name]
        file_path = Path(file_path_str)
        
        if not file_path.exists():
            print(f"⚠️  {drug_name}: File không tồn tại: {file_path}")
            results["errors"].append({"drug": drug_name, "error": "File not found"})
            continue
        
        print(f"\n{drug_name}:")
        print(f"  File: {file_path.name}")
        
        # Backup
        backup_dir = file_path.parent / ".backups"
        backup_dir.mkdir(exist_ok=True)
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        backup_path = backup_dir / f"{file_path.stem}_{timestamp}{file_path.suffix}"
        shutil.copy2(file_path, backup_path)
        
        # Update
        success = update_pregnancy_in_file(file_path, drug_name, category)
        
        if success:
            print(f"  ✅ Đã cập nhật")
            results["updated"].append({
                "drug": drug_name,
                "file": str(file_path),
                "backup": str(backup_path)
            })
        else:
            results["errors"].append({
                "drug": drug_name,
                "file": str(file_path),
                "error": "Update failed"
            })
    
    # Save results
    results_file = Path(__file__).parent / "fix_remaining_pregnancy_results.json"
    with open(results_file, 'w', encoding='utf-8') as f:
        json.dump(results, f, ensure_ascii=False, indent=2)
    
    print("\n" + "="*70)
    print("TỔNG KẾT")
    print("="*70)
    print(f"Đã cập nhật: {len(results['updated'])} thuốc")
    print(f"Lỗi: {len(results['errors'])} thuốc")
    print("="*70)


if __name__ == "__main__":
    main()
