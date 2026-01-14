#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Fix Syntax Errors Using AST
Sử dụng AST để tìm và sửa lỗi syntax chính xác hơn
"""

import ast
import re
from pathlib import Path
import shutil
from datetime import datetime


def find_syntax_errors(file_path: Path):
    """Tìm lỗi syntax trong file"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        try:
            ast.parse(content)
            return None  # Không có lỗi
        except SyntaxError as e:
            return {
                'line': e.lineno,
                'offset': e.offset,
                'text': e.text,
                'msg': str(e)
            }
    except Exception as e:
        return {'error': str(e)}


def fix_common_patterns(content: str) -> tuple[str, int]:
    """Sửa các pattern lỗi phổ biến"""
    fixes = 0
    original = content
    
    # Pattern 1: ],field' -> ],\n        'field'
    patterns = [
        (r"\],interactions'", r"],\n        'interactions'"),
        (r"\],pregnancy'", r"],\n        'pregnancy'"),
        (r"\],storage'", r"],\n        'storage'"),
        (r"\],monitoring'", r"],\n        'monitoring'"),
        (r"\],precautions'", r"],\n        'precautions'"),
        (r"\],pharmacokinetics'", r"],\n        'pharmacokinetics'"),
        (r"\],mechanism_of_action'", r"],\n        'mechanism_of_action'"),
        (r"\],contraindications'", r"],\n        'contraindications'"),
        (r"\],dosage'", r"],\n        'dosage'"),
        (r"\],side_effects'", r"],\n        'side_effects'"),
        (r"\],indications'", r"],\n        'indications'"),
        (r"\],administration'", r"],\n        'administration'"),
        (r"\],vietnamese_name'", r"],\n        'vietnamese_name'"),
        (r"\],tương_đối'", r"],\n        'tương_đối'"),
        (r"\],tuyệt_đối'", r"],\n        'tuyệt_đối'"),
        (r"\],moderate'", r"],\n        'moderate'"),
        (r"\],minor'", r"],\n        'minor'"),
        (r"\],severe'", r"],\n        'severe'"),
        (r"\},hepatic_adjustment'", r"},\n        'hepatic_adjustment'"),
        (r"\},renal_adjustment'", r"},\n        'renal_adjustment'"),
        (r"\},storage'", r"},\n        'storage'"),
        (r"\},monitoring'", r"},\n        'monitoring'"),
        (r"\},overdose_management'", r"},\n        'overdose_management'"),
        (r"\},black_box_warnings'", r"},\n        'black_box_warnings'"),
        (r"\},contraindications'", r"},\n        'contraindications'"),
        (r"\},pregnancy_lactation'", r"},\n        'pregnancy_lactation'"),
        (r"\}\]\},contraindications'", r"}]},\n        'contraindications'"),
        (r"\}\]\},storage'", r"}]},\n        'storage'"),
        (r"\}\]\},monitoring'", r"}]},\n        'monitoring'"),
        (r"\}\]\},hepatic_adjustment'", r"}]},\n        'hepatic_adjustment'"),
        (r"\}\]\},renal_adjustment'", r"}]},\n        'renal_adjustment'"),
        (r"('group':\s*'[^']+'),vietnamese_name'", r"\1,\n        'vietnamese_name'"),
        (r"('group':\s*'[^']+'),,", r"\1,"),
        (r"\],,", r"],"),
        (r"\},,", r"},"),
    ]
    
    for pattern, replacement in patterns:
        new_content = re.sub(pattern, replacement, content)
        if new_content != content:
            fixes += 1
            content = new_content
    
    return content, fixes


def fix_file(file_path: Path) -> int:
    """Sửa lỗi trong file"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        original_content = content
        total_fixes = 0
        
        # Thử parse để xem có lỗi không
        error_info = find_syntax_errors(file_path)
        
        if error_info and 'error' not in error_info:
            # Có lỗi syntax, thử sửa
            content, fixes = fix_common_patterns(content)
            total_fixes += fixes
            
            # Kiểm tra lại sau khi sửa
            if content != original_content:
                # Backup
                backup_dir = file_path.parent / ".backups"
                backup_dir.mkdir(exist_ok=True)
                timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
                backup_path = backup_dir / f"{file_path.stem}_ast_fix_{timestamp}{file_path.suffix}"
                shutil.copy2(file_path, backup_path)
                
                # Write
                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write(content)
                
                # Kiểm tra lại
                new_error = find_syntax_errors(file_path)
                if new_error and 'error' not in new_error:
                    # Vẫn còn lỗi
                    return -total_fixes  # Trả về số âm để đánh dấu vẫn còn lỗi
                else:
                    return total_fixes
        
        return 0
        
    except Exception as e:
        print(f"Error fixing {file_path}: {e}")
        return 0


def main():
    """Main function"""
    print("="*70)
    print("SỬA LỖI SYNTAX SỬ DỤNG AST")
    print("="*70)
    
    modules_dir = Path(__file__).parent / "drug_modules"
    
    total_fixes = 0
    files_fixed = []
    files_still_error = []
    
    # Ưu tiên sửa biguanides.py trước
    biguanides_file = modules_dir / "diabetes" / "biguanides.py"
    if biguanides_file.exists():
        print(f"\n🔧 Đang sửa {biguanides_file.name}...")
        fixes = fix_file(biguanides_file)
        if fixes > 0:
            print(f"✅ {biguanides_file.name}: Sửa {fixes} lỗi")
            files_fixed.append(str(biguanides_file))
            total_fixes += fixes
        elif fixes < 0:
            print(f"⚠️  {biguanides_file.name}: Đã sửa {abs(fixes)} lỗi nhưng vẫn còn lỗi")
            files_still_error.append(str(biguanides_file))
    
    # Sửa các file khác
    for py_file in modules_dir.rglob("*.py"):
        if py_file.name.startswith("__") or "backup" in str(py_file).lower():
            continue
        
        if py_file == biguanides_file:
            continue  # Đã sửa rồi
        
        fixes = fix_file(py_file)
        if fixes > 0:
            print(f"✅ {py_file.name}: Sửa {fixes} lỗi")
            files_fixed.append(str(py_file))
            total_fixes += fixes
        elif fixes < 0:
            print(f"⚠️  {py_file.name}: Đã sửa {abs(fixes)} lỗi nhưng vẫn còn lỗi")
            files_still_error.append(str(py_file))
    
    print("\n" + "="*70)
    print("TỔNG KẾT")
    print("="*70)
    print(f"Đã sửa {total_fixes} lỗi trong {len(files_fixed)} file")
    if files_still_error:
        print(f"⚠️  {len(files_still_error)} file vẫn còn lỗi sau khi sửa")
    print("="*70)


if __name__ == "__main__":
    main()
