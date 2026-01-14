#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Fix Interaction Comma Errors
Sửa các lỗi thiếu dấu phẩy trong interactions
"""

import re
from pathlib import Path
import shutil
from datetime import datetime


def fix_file(file_path: Path) -> int:
    """Sửa lỗi trong file"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        original_content = content
        fixes = 0
        
        # Pattern 1: }],moderate' -> }],\n        'moderate'
        pattern1 = r"\}\],moderate'"
        def replace1(match):
            nonlocal fixes
            fixes += 1
            return "}],\n        'moderate'"
        
        content = re.sub(pattern1, replace1, content)
        
        # Pattern 2: }],severe' -> }],\n        'severe'
        pattern2 = r"\}\],severe'"
        def replace2(match):
            nonlocal fixes
            fixes += 1
            return "}],\n        'severe'"
        
        content = re.sub(pattern2, replace2, content)
        
        # Pattern 3: }],minor' -> }],\n        'minor'
        pattern3 = r"\}\],minor'"
        def replace3(match):
            nonlocal fixes
            fixes += 1
            return "}],\n        'minor'"
        
        content = re.sub(pattern3, replace3, content)
        
        # Pattern 4: }],contraindications' -> }],\n        'contraindications'
        pattern4 = r"\}\],contraindications'"
        def replace4(match):
            nonlocal fixes
            fixes += 1
            return "}],\n        'contraindications'"
        
        content = re.sub(pattern4, replace4, content)
        
        if content != original_content:
            # Backup
            backup_dir = file_path.parent / ".backups"
            backup_dir.mkdir(exist_ok=True)
            timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
            backup_path = backup_dir / f"{file_path.stem}_interaction_fix_{timestamp}{file_path.suffix}"
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
    print("SỬA LỖI THIẾU DẤU PHẨY TRONG INTERACTIONS")
    print("="*70)
    
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
