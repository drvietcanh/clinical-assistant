#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Fix All Remaining Errors
Sửa tất cả các lỗi syntax còn lại
"""

import re
from pathlib import Path
import shutil
from datetime import datetime


def fix_file(file_path: Path) -> int:
    """Sửa tất cả lỗi trong file"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        original_content = content
        fixes = 0
        
        # Pattern 1: "pregnancy": "..." "field_name": (missing comma)
        pattern1 = r'"pregnancy":\s*"([^"]+)"("([a-z_]+)":\s*[{"\[""\'])'
        def replace1(match):
            nonlocal fixes
            fixes += 1
            pregnancy_value = match.group(1)
            next_field = match.group(2)
            return f'"pregnancy": "{pregnancy_value}",\n        {next_field}'
        
        content = re.sub(pattern1, replace1, content)
        
        # Pattern 2: ', 'vietnamese_name': (pregnancy inserted in middle of string)
        # Find: '... "pregnancy": "..." ...'
        pattern2 = r"('([^']*))\"pregnancy\":\s*\"([^\"]+)\"([^']*')"
        def replace2(match):
            nonlocal fixes
            fixes += 1
            before = match.group(1)
            after = match.group(4)
            pregnancy_value = match.group(3)
            # Extract indent
            indent_match = re.match(r'^\s*', before)
            indent = indent_match.group(0) if indent_match else '        '
            # Close the string before, add pregnancy, then continue string
            before_clean = before.rstrip().rstrip("'")
            after_clean = after.lstrip().lstrip("'")
            return f"{before_clean}',\n{indent}\"pregnancy\": \"{pregnancy_value}\",\n{indent}'{after_clean}"
        
        content = re.sub(pattern2, replace2, content)
        
        # Pattern 3: Remove orphan commas with quotes
        lines = content.split('\n')
        new_lines = []
        for i, line in enumerate(lines):
            stripped = line.strip()
            # Skip lines that are just comma with quote
            if stripped in [",", "',", "',"]:
                if i + 1 < len(lines):
                    next_line = lines[i + 1].strip()
                    if next_line.startswith('"') or (next_line.startswith("'") and ':' in next_line):
                        fixes += 1
                        continue
            new_lines.append(line)
        content = '\n'.join(new_lines)
        
        if content != original_content:
            # Backup
            backup_dir = file_path.parent / ".backups"
            backup_dir.mkdir(exist_ok=True)
            timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
            backup_path = backup_dir / f"{file_path.stem}_final_fix_{timestamp}{file_path.suffix}"
            shutil.copy2(file_path, backup_path)
            
            # Write
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
    print("SỬA TẤT CẢ LỖI CÒN LẠI")
    print("="*70)
    
    # Get list of files with errors from find_syntax_errors
    modules_dir = Path(__file__).parent / "drug_modules"
    
    total_fixes = 0
    files_fixed = []
    
    for py_file in modules_dir.rglob("*.py"):
        if py_file.name.startswith("__") or "backup" in str(py_file).lower():
            continue
        
        fixes = fix_file(py_file)
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
