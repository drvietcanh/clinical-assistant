#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Find Syntax Errors
Tìm tất cả các lỗi syntax còn lại
"""

import ast
import sys
from pathlib import Path


def check_syntax(file_path: Path) -> list:
    """Kiểm tra syntax của file"""
    errors = []
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        try:
            ast.parse(content)
        except SyntaxError as e:
            errors.append({
                "line": e.lineno,
                "message": e.msg,
                "text": e.text
            })
    except Exception as e:
        errors.append({
            "line": 0,
            "message": str(e),
            "text": None
        })
    
    return errors


def main():
    """Main function"""
    print("="*70)
    print("TÌM LỖI SYNTAX")
    print("="*70)
    
    modules_dir = Path(__file__).parent / "drug_modules"
    
    files_with_errors = []
    
    for py_file in modules_dir.rglob("*.py"):
        if py_file.name.startswith("__") or "backup" in str(py_file).lower():
            continue
        
        errors = check_syntax(py_file)
        if errors:
            print(f"\n❌ {py_file.name}:")
            for error in errors:
                print(f"   Line {error['line']}: {error['message']}")
                if error['text']:
                    print(f"   {error['text'].strip()}")
            files_with_errors.append({
                "file": str(py_file),
                "errors": errors
            })
    
    print("\n" + "="*70)
    print("TỔNG KẾT")
    print("="*70)
    print(f"Tìm thấy {len(files_with_errors)} file có lỗi syntax")
    print("="*70)
    
    if files_with_errors:
        # Save to file
        import json
        results_file = Path(__file__).parent / "syntax_errors_found.json"
        with open(results_file, 'w', encoding='utf-8') as f:
            json.dump(files_with_errors, f, ensure_ascii=False, indent=2)
        print(f"\nKết quả chi tiết: {results_file}")


if __name__ == "__main__":
    main()
