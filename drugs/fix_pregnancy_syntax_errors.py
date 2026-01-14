#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Fix Pregnancy Syntax Errors
Tự động sửa các lỗi syntax do batch_update_pregnancy gây ra
"""

import re
from pathlib import Path
import shutil
from datetime import datetime


def fix_pregnancy_syntax_in_file(file_path: Path) -> int:
    """Sửa lỗi syntax trong file"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        original_content = content
        fixes = 0
        
        # Pattern 1: "pregnancy": "..." "field_name": {
        pattern1 = r'"pregnancy":\s*"([^"]+)"("([a-z_]+)":\s*\{)'
        def replace1(match):
            nonlocal fixes
            fixes += 1
            pregnancy_value = match.group(1)
            next_field = match.group(2)
            return f'"pregnancy": "{pregnancy_value}",\n        {next_field}'
        
        content = re.sub(pattern1, replace1, content)
        
        # Pattern 2: "pregnancy": "..." "field_name": [
        pattern2 = r'"pregnancy":\s*"([^"]+)"("([a-z_]+)":\s*\[)'
        def replace2(match):
            nonlocal fixes
            fixes += 1
            pregnancy_value = match.group(1)
            next_field = match.group(2)
            return f'"pregnancy": "{pregnancy_value}",\n        {next_field}'
        
        content = re.sub(pattern2, replace2, content)
        
        # Pattern 3: "pregnancy": "..." "field_name": """
        pattern3 = r'"pregnancy":\s*"([^"]+)"("([a-z_]+)":\s*""")'
        def replace3(match):
            nonlocal fixes
            fixes += 1
            pregnancy_value = match.group(1)
            next_field = match.group(2)
            return f'"pregnancy": "{pregnancy_value}",\n        {next_field}'
        
        content = re.sub(pattern3, replace3, content)
        
        # Pattern 4: "pregnancy": "..." "field_name": '
        pattern4 = r'"pregnancy":\s*"([^"]+)"("([a-z_]+)":\s*\')'
        def replace4(match):
            nonlocal fixes
            fixes += 1
            pregnancy_value = match.group(1)
            next_field = match.group(2)
            return f'"pregnancy": "{pregnancy_value}",\n        {next_field}'
        
        content = re.sub(pattern4, replace4, content)
        
        # Pattern 5: "pregnancy": "..." trong string không đóng
        # Tìm các trường hợp pregnancy được chèn vào giữa string
        pattern5 = r"('([^']*))\"pregnancy\":\s*\"([^\"]+)\"([^']*')"
        def replace5(match):
            nonlocal fixes
            fixes += 1
            before = match.group(1)
            after = match.group(4)
            pregnancy_value = match.group(3)
            return f"{before}',\n        \"pregnancy\": \"{pregnancy_value}\",\n        '{after}"
        
        content = re.sub(pattern5, replace5, content)
        
        if content != original_content:
            # Backup
            backup_dir = file_path.parent / ".backups"
            backup_dir.mkdir(exist_ok=True)
            timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
            backup_path = backup_dir / f"{file_path.stem}_syntax_fix_{timestamp}{file_path.suffix}"
            shutil.copy2(file_path, backup_path)
            
            # Write fixed content
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
            
            return fixes
        
        return 0
        
    except Exception as e:
        print(f"Error fixing {file_path}: {e}")
        return 0


def main():
    """Main function"""
    print("="*70)
    print("SỬA LỖI SYNTAX PREGNANCY")
    print("="*70)
    
    modules_dir = Path(__file__).parent / "drug_modules"
    
    total_fixes = 0
    files_fixed = []
    
    for py_file in modules_dir.rglob("*.py"):
        if py_file.name.startswith("__") or "backup" in py_file.name.lower():
            continue
        
        fixes = fix_pregnancy_syntax_in_file(py_file)
        if fixes > 0:
            print(f"✅ {py_file.name}: Sửa {fixes} lỗi")
            files_fixed.append(str(py_file))
            total_fixes += fixes
    
    print("\n" + "="*70)
    print("TỔNG KẾT")
    print("="*70)
    print(f"Đã sửa {total_fixes} lỗi trong {len(files_fixed)} file")
    print("="*70)


if __name__ == "__main__":
    main()
