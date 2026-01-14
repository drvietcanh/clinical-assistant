#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Remove Orphan Commas
Xóa các dòng chỉ có dấu phẩy (orphan commas)
"""

import re
from pathlib import Path
import shutil
from datetime import datetime


def remove_orphan_commas(file_path: Path) -> int:
    """Xóa các dòng chỉ có dấu phẩy"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            lines = f.readlines()
        
        original_lines = lines.copy()
        new_lines = []
        fixes = 0
        
        for i, line in enumerate(lines):
            # Check if line is just comma and whitespace, or comma with quote
            stripped = line.strip()
            if stripped == ',' or stripped == "'," or stripped == "',":
                # Check context - if next line is a field, remove this line
                if i + 1 < len(lines):
                    next_line = lines[i + 1].strip()
                    # If next line starts with a quote (field name), remove this comma line
                    if next_line.startswith('"') or next_line.startswith("'"):
                        fixes += 1
                        continue  # Skip this line
                # If previous line ends with comma or closing bracket, also remove
                if i > 0:
                    prev_line = lines[i - 1].strip()
                    if prev_line.endswith(',') or prev_line.endswith(']') or prev_line.endswith('}'):
                        fixes += 1
                        continue  # Skip this line
            
            new_lines.append(line)
        
        if fixes > 0:
            # Backup
            backup_dir = file_path.parent / ".backups"
            backup_dir.mkdir(exist_ok=True)
            timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
            backup_path = backup_dir / f"{file_path.stem}_remove_commas_{timestamp}{file_path.suffix}"
            shutil.copy2(file_path, backup_path)
            
            # Write fixed content
            with open(file_path, 'w', encoding='utf-8') as f:
                f.writelines(new_lines)
            
            return fixes
        
        return 0
        
    except Exception as e:
        print(f"Error fixing {file_path}: {e}")
        return 0


def main():
    """Main function"""
    print("="*70)
    print("XÓA CÁC DÒNG CHỈ CÓ DẤU PHẨY")
    print("="*70)
    
    modules_dir = Path(__file__).parent / "drug_modules"
    
    total_fixes = 0
    files_fixed = []
    
    for py_file in modules_dir.rglob("*.py"):
        if py_file.name.startswith("__") or "backup" in str(py_file).lower():
            continue
        
        fixes = remove_orphan_commas(py_file)
        if fixes > 0:
            print(f"✅ {py_file.name}: Xóa {fixes} dòng")
            files_fixed.append(str(py_file))
            total_fixes += fixes
    
    print("\n" + "="*70)
    print("TỔNG KẾT")
    print("="*70)
    print(f"Đã xóa {total_fixes} dòng trong {len(files_fixed)} file")
    print("="*70)


if __name__ == "__main__":
    main()
