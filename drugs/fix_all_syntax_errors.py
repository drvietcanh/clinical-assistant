#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Fix All Syntax Errors
Tự động sửa tất cả lỗi syntax do batch_update gây ra
"""

import re
from pathlib import Path
import shutil
from datetime import datetime


def fix_syntax_errors_in_file(file_path: Path) -> int:
    """Sửa lỗi syntax trong file"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        original_content = content
        fixes = 0
        
        # Pattern 1: Dòng chỉ có dấu phẩy và whitespace
        pattern1 = r'^\s*,\s*$'
        lines = content.split('\n')
        new_lines = []
        for i, line in enumerate(lines):
            if re.match(pattern1, line):
                # Check if next line is a field
                if i + 1 < len(lines) and ('"' in lines[i+1] or "'" in lines[i+1]):
                    # Skip this line (remove it)
                    fixes += 1
                    continue
            new_lines.append(line)
        content = '\n'.join(new_lines)
        
        # Pattern 2: "pregnancy": "..." "field_name": (missing comma and newline)
        pattern2 = r'"pregnancy":\s*"([^"]+)"("([a-z_]+)":\s*[{[])'
        def replace2(match):
            nonlocal fixes
            fixes += 1
            pregnancy_value = match.group(1)
            next_field = match.group(2)
            # Get indent from previous line
            return f'"pregnancy": "{pregnancy_value}",\n        {next_field}'
        
        content = re.sub(pattern2, replace2, content)
        
        # Pattern 3: "pregnancy": "..." "field_name": """ (triple quotes)
        pattern3 = r'"pregnancy":\s*"([^"]+)"("([a-z_]+)":\s*""")'
        def replace3(match):
            nonlocal fixes
            fixes += 1
            pregnancy_value = match.group(1)
            next_field = match.group(2)
            return f'"pregnancy": "{pregnancy_value}",\n        {next_field}'
        
        content = re.sub(pattern3, replace3, content)
        
        # Pattern 4: "pregnancy": "..." trong string không đóng (single quotes) - skip for now
        # This is complex and may cause issues
        
        if content != original_content:
            # Backup
            backup_dir = file_path.parent / ".backups"
            backup_dir.mkdir(exist_ok=True)
            timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
            backup_path = backup_dir / f"{file_path.stem}_final_fix_{timestamp}{file_path.suffix}"
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
    print("SỬA TẤT CẢ LỖI SYNTAX")
    print("="*70)
    
    modules_dir = Path(__file__).parent / "drug_modules"
    
    total_fixes = 0
    files_fixed = []
    
    # Only process .py files, skip backups
    for py_file in modules_dir.rglob("*.py"):
        if py_file.name.startswith("__") or "backup" in str(py_file).lower():
            continue
        
        fixes = fix_syntax_errors_in_file(py_file)
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
