#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Fix All Remaining Comma Errors
Sửa tất cả các lỗi thiếu dấu phẩy còn lại
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
        
        # Pattern 1: ],precautions' -> ],\n        'precautions'
        pattern1 = r"\],precautions'"
        def replace1(match):
            nonlocal fixes
            fixes += 1
            return "],\n        'precautions'"
        
        content = re.sub(pattern1, replace1, content)
        
        # Pattern 2: ],pharmacokinetics' -> ],\n        'pharmacokinetics'
        pattern2 = r"\],pharmacokinetics'"
        def replace2(match):
            nonlocal fixes
            fixes += 1
            return "],\n        'pharmacokinetics'"
        
        content = re.sub(pattern2, replace2, content)
        
        # Pattern 3: ],storage' -> ],\n        'storage'
        pattern3 = r"\],storage'"
        def replace3(match):
            nonlocal fixes
            fixes += 1
            return "],\n        'storage'"
        
        content = re.sub(pattern3, replace3, content)
        
        # Pattern 4: ],monitoring' -> ],\n        'monitoring'
        pattern4 = r"\],monitoring'"
        def replace4(match):
            nonlocal fixes
            fixes += 1
            return "],\n        'monitoring'"
        
        content = re.sub(pattern4, replace4, content)
        
        # Pattern 5: ],mechanism_of_action' -> ],\n        'mechanism_of_action'
        pattern5 = r"\],mechanism_of_action'"
        def replace5(match):
            nonlocal fixes
            fixes += 1
            return "],\n        'mechanism_of_action'"
        
        content = re.sub(pattern5, replace5, content)
        
        # Pattern 6: ],contraindications_brief' -> ],\n        'contraindications_brief'
        pattern6 = r"\],contraindications_brief'"
        def replace6(match):
            nonlocal fixes
            fixes += 1
            return "],\n        'contraindications_brief'"
        
        content = re.sub(pattern6, replace6, content)
        
        # Pattern 7: 'group': '...',vietnamese_name' -> 'group': '...',\n        'vietnamese_name'
        pattern7 = r"('group':\s*'[^']+'),vietnamese_name'"
        def replace7(match):
            nonlocal fixes
            fixes += 1
            return match.group(1) + ",\n        'vietnamese_name'"
        
        content = re.sub(pattern7, replace7, content)
        
        # Pattern 8: '...'],indications' -> '...'],\n        'indications'
        pattern8 = r"('[^']+']),indications'"
        def replace8(match):
            nonlocal fixes
            fixes += 1
            return match.group(1) + ",\n        'indications'"
        
        content = re.sub(pattern8, replace8, content)
        
        # Pattern 9: ],vietnamese_name' -> ],\n        'vietnamese_name'
        pattern9 = r"\],vietnamese_name'"
        def replace9(match):
            nonlocal fixes
            fixes += 1
            return "],\n        'vietnamese_name'"
        
        content = re.sub(pattern9, replace9, content)
        
        # Pattern 10: ', 'vietnamese_name': -> 'vietnamese_name':
        pattern10 = r",\s*'\s*'vietnamese_name':"
        def replace10(match):
            nonlocal fixes
            fixes += 1
            return ",\n        'vietnamese_name':"
        
        content = re.sub(pattern10, replace10, content)
        
        # Pattern 11: '...'],administration' -> '...'],\n        'administration'
        pattern11 = r"('[^']+']),administration'"
        def replace11(match):
            nonlocal fixes
            fixes += 1
            return match.group(1) + ",\n        'administration'"
        
        content = re.sub(pattern11, replace11, content)
        
        # Pattern 12: ],administration' -> ],\n        'administration'
        pattern12 = r"\],administration'"
        def replace12(match):
            nonlocal fixes
            fixes += 1
            return "],\n        'administration'"
        
        content = re.sub(pattern12, replace12, content)
        
        if content != original_content:
            # Backup
            backup_dir = file_path.parent / ".backups"
            backup_dir.mkdir(exist_ok=True)
            timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
            backup_path = backup_dir / f"{file_path.stem}_comma_fix_{timestamp}{file_path.suffix}"
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
    print("SỬA TẤT CẢ CÁC LỖI THIẾU DẤU PHẨY CÒN LẠI")
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
