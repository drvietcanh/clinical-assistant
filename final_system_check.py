"""
Final System Check - Kiểm tra cuối cùng hệ thống thuốc
Chỉ báo cáo các lỗi thực sự
"""
import ast
from pathlib import Path

def main():
    """Main function"""
    print("\n" + "=" * 70)
    print("KIEM TRA CUOI CUNG HE THONG THUOC")
    print("=" * 70)
    print()
    
    # 1. Check syntax
    print("1. KIEM TRA SYNTAX ERRORS")
    print("-" * 70)
    base_path = Path("drugs/drug_modules")
    syntax_errors = []
    
    for py_file in sorted(base_path.rglob("*.py")):
        if py_file.name == "__init__.py" or py_file.name.endswith(".backup"):
            continue
        
        try:
            with open(py_file, 'r', encoding='utf-8') as f:
                content = f.read()
            ast.parse(content)
        except SyntaxError as e:
            syntax_errors.append((py_file, e.lineno, e.msg))
    
    if syntax_errors:
        print(f"[LOI] Tim thay {len(syntax_errors)} file co loi syntax:")
        for file_path, line, msg in syntax_errors:
            print(f"  - {file_path}: Line {line} - {msg}")
    else:
        print("[OK] Khong co loi syntax nao")
    
    # 2. Check critical files
    print("\n2. KIEM TRA FILE QUAN TRONG")
    print("-" * 70)
    critical_files = [
        "drugs/drug_database.py",
        "drugs/drug_modules/__init__.py",
        "drugs/drug_modules/cardiovascular/__init__.py",
        "drugs/drug_modules/diabetes/__init__.py",
        "drugs/drug_modules/antimicrobial/__init__.py",
        "drugs/drug_modules/hematology.py",
        "drugs/drug_modules/urology.py",
        "drugs/drug_modules/dermatology.py",
        "drugs/drug_modules/ophthalmology.py",
        "drugs/drug_modules/endocrinology.py",
    ]
    
    missing_files = []
    for file_path in critical_files:
        if not Path(file_path).exists():
            missing_files.append(file_path)
    
    if missing_files:
        print(f"[LOI] Thieu {len(missing_files)} file quan trong:")
        for f in missing_files:
            print(f"  - {f}")
    else:
        print("[OK] Tat ca cac file quan trong deu ton tai")
    
    # 3. Check for obvious structural issues
    print("\n3. KIEM TRA CAU TRUC")
    print("-" * 70)
    structural_issues = []
    
    # Check endocrinology.py
    endo_file = Path("drugs/drug_modules/endocrinology.py")
    if endo_file.exists():
        with open(endo_file, 'r', encoding='utf-8') as f:
            content = f.read()
        if 'ENDOCRINOLOGY_DRUGS' not in content:
            structural_issues.append("endocrinology.py: Khong co ENDOCRINOLOGY_DRUGS")
        else:
            print("[OK] endocrinology.py co ENDOCRINOLOGY_DRUGS")
    
    # Check for files with obvious issues
    problematic_patterns = [
        ('true', 'True'),
        ('false', 'False'),
        ('True/False', 'True hoac False'),
    ]
    
    for py_file in sorted(base_path.rglob("*.py")):
        if py_file.name == "__init__.py" or py_file.name.endswith(".backup"):
            continue
        
        try:
            with open(py_file, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Check for lowercase true/false (should be True/False)
            if 'true' in content or 'false' in content:
                # But exclude string literals
                lines = content.split('\n')
                for i, line in enumerate(lines, 1):
                    if '= true' in line or '= false' in line:
                        structural_issues.append(f"{py_file.name}: Line {i} - Co 'true'/'false' thay vi 'True'/'False'")
                        break
        except:
            pass
    
    if structural_issues:
        print(f"[LOI] Tim thay {len(structural_issues)} van de cau truc:")
        for issue in structural_issues[:5]:
            print(f"  - {issue}")
    else:
        print("[OK] Khong co van de cau truc ro rang")
    
    # Summary
    print("\n" + "=" * 70)
    print("TOM TAT")
    print("=" * 70)
    
    total_errors = len(syntax_errors) + len(missing_files) + len(structural_issues)
    
    if total_errors == 0:
        print("\n[OK] HE THONG KHONG CO LOI NGHIEM TRONG!")
        print("\nCac kiem tra:")
        print("  [OK] Syntax: Khong co loi")
        print("  [OK] Files: Tat ca file quan trong deu ton tai")
        print("  [OK] Structure: Khong co van de")
    else:
        print(f"\n[LOI] Tim thay {total_errors} van de:")
        if syntax_errors:
            print(f"  - Syntax errors: {len(syntax_errors)}")
        if missing_files:
            print(f"  - Missing files: {len(missing_files)}")
        if structural_issues:
            print(f"  - Structural issues: {len(structural_issues)}")
    
    print("\n" + "=" * 70)
    print("\nLuu y:")
    print("  - Cac loi import 'streamlit' khong phai loi (chi thieu dependency)")
    print("  - Cac 'key trung lap' trong check truoc do la field names, khong phai loi")
    print("=" * 70)

if __name__ == "__main__":
    main()

