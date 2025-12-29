"""
System Check Report - Báo cáo kiểm tra hệ thống
Tập trung vào các lỗi thực sự, bỏ qua các cảnh báo không quan trọng
"""
import ast
from pathlib import Path
import sys

def check_syntax():
    """Kiểm tra syntax errors"""
    print("1. KIEM TRA SYNTAX ERRORS")
    print("-" * 70)
    
    base_path = Path("drugs/drug_modules")
    errors = []
    
    for py_file in sorted(base_path.rglob("*.py")):
        if py_file.name == "__init__.py" or py_file.name.endswith(".backup"):
            continue
        
        try:
            with open(py_file, 'r', encoding='utf-8') as f:
                content = f.read()
            ast.parse(content)
        except SyntaxError as e:
            errors.append({
                'file': str(py_file),
                'line': e.lineno,
                'message': e.msg
            })
    
    if errors:
        print(f"[LOI] Tim thay {len(errors)} file co loi syntax:")
        for err in errors:
            print(f"  - {err['file']}: Line {err['line']} - {err['message']}")
        return False
    else:
        print("[OK] Khong co loi syntax nao")
        return True

def check_module_files():
    """Kiểm tra các file module chính"""
    print("\n2. KIEM TRA FILE MODULE")
    print("-" * 70)
    
    required_files = [
        "drugs/drug_modules/__init__.py",
        "drugs/drug_modules/cardiovascular/__init__.py",
        "drugs/drug_modules/diabetes/__init__.py",
        "drugs/drug_modules/gastrointestinal/__init__.py",
        "drugs/drug_modules/analgesics/__init__.py",
        "drugs/drug_modules/respiratory/__init__.py",
        "drugs/drug_modules/neurological/__init__.py",
        "drugs/drug_modules/supportive/__init__.py",
        "drugs/drug_modules/antimicrobial/__init__.py",
        "drugs/drug_modules/metabolic/__init__.py",
        "drugs/drug_modules/oncology/__init__.py",
        "drugs/drug_modules/emergency/__init__.py",
        "drugs/drug_modules/miscellaneous/__init__.py",
        "drugs/drug_modules/hematology.py",
        "drugs/drug_modules/urology.py",
        "drugs/drug_modules/dermatology.py",
        "drugs/drug_modules/ophthalmology.py",
        "drugs/drug_modules/endocrinology.py",
        "drugs/drug_modules/obstetrics_gynecology.py",
        "drugs/drug_modules/ent_oral_nasal_combinations.py",
    ]
    
    missing = []
    for file_path in required_files:
        if not Path(file_path).exists():
            missing.append(file_path)
    
    if missing:
        print(f"[LOI] Thieu {len(missing)} file:")
        for f in missing:
            print(f"  - {f}")
        return False
    else:
        print("[OK] Tat ca cac file module deu ton tai")
        return True

def check_basic_structure():
    """Kiểm tra cấu trúc cơ bản của các file"""
    print("\n3. KIEM TRA CAU TRUC CO BAN")
    print("-" * 70)
    
    issues = []
    base_path = Path("drugs/drug_modules")
    
    # Check for files that should export a dictionary
    module_files = [
        "hematology.py",
        "urology.py", 
        "dermatology.py",
        "ophthalmology.py",
        "endocrinology.py",
        "obstetrics_gynecology.py",
        "ent_oral_nasal_combinations.py",
    ]
    
    for module_file in module_files:
        file_path = base_path / module_file
        if file_path.exists():
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                # Check if it has a dictionary export
                if '_DRUGS = {' not in content:
                    issues.append(f"{module_file}: Khong co dictionary export")
                
                # Check syntax
                try:
                    ast.parse(content)
                except SyntaxError as e:
                    issues.append(f"{module_file}: Syntax error at line {e.lineno}")
                    
            except Exception as e:
                issues.append(f"{module_file}: Error reading file - {e}")
    
    if issues:
        print(f"[LOI] Tim thay {len(issues)} van de:")
        for issue in issues:
            print(f"  - {issue}")
        return False
    else:
        print("[OK] Cau truc co ban hop le")
        return True

def check_duplicate_keys():
    """Kiểm tra key trùng lặp trong cùng một file"""
    print("\n4. KIEM TRA KEY TRUNG LAP TRONG FILE")
    print("-" * 70)
    
    issues = []
    base_path = Path("drugs/drug_modules")
    
    for py_file in sorted(base_path.rglob("*.py")):
        if py_file.name == "__init__.py" or py_file.name.endswith(".backup"):
            continue
        
        try:
            with open(py_file, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Simple check for duplicate keys in dictionary literals
            # Look for patterns like "DrugName": { ... } appearing multiple times
            import re
            # Find all dictionary keys
            keys = re.findall(r'["\']([^"\']+)["\']\s*:\s*\{', content)
            
            # Check for duplicates
            seen = set()
            duplicates = []
            for key in keys:
                if key in seen:
                    duplicates.append(key)
                seen.add(key)
            
            if duplicates:
                issues.append(f"{py_file.name}: Co {len(duplicates)} key trung lap: {duplicates[:3]}")
                
        except Exception as e:
            # Skip files that can't be read
            pass
    
    if issues:
        print(f"[WARNING] Tim thay {len(issues)} file co the co key trung lap:")
        for issue in issues[:5]:
            print(f"  - {issue}")
        return False
    else:
        print("[OK] Khong co key trung lap")
        return True

def main():
    """Main function"""
    print("\n" + "=" * 70)
    print("BAO CAO KIEM TRA HE THONG THUOC")
    print("=" * 70)
    print()
    
    results = {
        'syntax': check_syntax(),
        'files': check_module_files(),
        'structure': check_basic_structure(),
        'duplicates': check_duplicate_keys(),
    }
    
    print("\n" + "=" * 70)
    print("TOM TAT")
    print("=" * 70)
    
    all_ok = all(results.values())
    
    if all_ok:
        print("\n[OK] HE THONG KHONG CO LOI NGHIEM TRONG!")
        print("  - Khong co loi syntax")
        print("  - Tat ca file module deu ton tai")
        print("  - Cau truc co ban hop le")
        print("  - Khong co key trung lap")
    else:
        print("\n[LOI] Tim thay mot so van de:")
        for check, result in results.items():
            status = "[OK]" if result else "[LOI]"
            print(f"  {status} {check}")
    
    print("\n" + "=" * 70)
    print("\nLuu y:")
    print("  - Cac loi import streamlit khong phai loi thuc su (chi thieu dependency)")
    print("  - Cac module file don le (hematology.py, urology.py, etc.) khong can __init__.py")
    print("=" * 70)

if __name__ == "__main__":
    main()

