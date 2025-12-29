"""
Comprehensive system check - Kiểm tra toàn bộ hệ thống thuốc
Tìm tất cả các loại lỗi: syntax, import, data quality, structure
"""
import ast
import sys
from pathlib import Path
from typing import List, Dict, Tuple

def check_syntax_errors() -> List[Dict]:
    """Kiểm tra lỗi syntax"""
    print("=" * 70)
    print("1. KIEM TRA SYNTAX ERRORS")
    print("=" * 70)
    
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
                'type': 'syntax',
                'line': e.lineno,
                'message': e.msg,
                'text': e.text
            })
    
    if errors:
        print(f"\n[LOI] Tim thay {len(errors)} file co loi syntax:")
        for err in errors:
            print(f"  - {err['file']}: Line {err['line']} - {err['message']}")
    else:
        print("\n[OK] Khong co loi syntax nao")
    
    return errors

def check_import_errors() -> List[Dict]:
    """Kiểm tra lỗi import"""
    print("\n" + "=" * 70)
    print("2. KIEM TRA IMPORT ERRORS")
    print("=" * 70)
    
    errors = []
    
    # Try to import main modules
    modules_to_check = [
        'drugs.drug_database',
        'drugs.drug_modules',
        'drugs.drug_modules.cardiovascular',
        'drugs.drug_modules.diabetes',
        'drugs.drug_modules.gastrointestinal',
        'drugs.drug_modules.analgesics',
        'drugs.drug_modules.respiratory',
        'drugs.drug_modules.neurological',
        'drugs.drug_modules.hematology',
        'drugs.drug_modules.supportive',
        'drugs.drug_modules.antimicrobial',
        'drugs.drug_modules.metabolic',
        'drugs.drug_modules.endocrinology',
        'drugs.drug_modules.oncology',
        'drugs.drug_modules.emergency',
        'drugs.drug_modules.urology',
        'drugs.drug_modules.dermatology',
        'drugs.drug_modules.ophthalmology',
        'drugs.drug_modules.obstetrics_gynecology',
        'drugs.drug_modules.ent_oral_nasal_combinations',
        'drugs.drug_modules.miscellaneous',
    ]
    
    for module_name in modules_to_check:
        try:
            __import__(module_name)
        except ImportError as e:
            errors.append({
                'module': module_name,
                'type': 'import',
                'message': str(e)
            })
        except SyntaxError as e:
            errors.append({
                'module': module_name,
                'type': 'import_syntax',
                'line': e.lineno,
                'message': e.msg
            })
        except Exception as e:
            errors.append({
                'module': module_name,
                'type': 'import_error',
                'message': str(e)
            })
    
    if errors:
        print(f"\n[LOI] Tim thay {len(errors)} loi import:")
        for err in errors:
            print(f"  - {err['module']}: {err['message']}")
    else:
        print("\n[OK] Tat ca cac module import thanh cong")
    
    return errors

def check_drug_database_structure() -> List[Dict]:
    """Kiểm tra cấu trúc database"""
    print("\n" + "=" * 70)
    print("3. KIEM TRA CAU TRUC DRUG DATABASE")
    print("=" * 70)
    
    errors = []
    
    try:
        # Try to load drug database
        sys.path.insert(0, str(Path.cwd()))
        from drugs.drug_database import DRUG_DATABASE
        
        if not DRUG_DATABASE:
            errors.append({
                'type': 'structure',
                'message': 'DRUG_DATABASE is empty'
            })
        else:
            drug_count = len(DRUG_DATABASE)
            print(f"\n[OK] DRUG_DATABASE co {drug_count} thuoc")
            
            # Check for required fields
            required_fields = ['group', 'vietnamese_name', 'administration', 'indications', 'dosage']
            missing_fields = []
            
            for drug_name, drug_data in list(DRUG_DATABASE.items())[:10]:  # Check first 10
                if not isinstance(drug_data, dict):
                    errors.append({
                        'drug': drug_name,
                        'type': 'structure',
                        'message': f'Drug data is not a dictionary: {type(drug_data)}'
                    })
                    continue
                
                for field in required_fields:
                    if field not in drug_data:
                        missing_fields.append((drug_name, field))
            
            if missing_fields:
                print(f"\n[WARNING] Tim thay {len(missing_fields)} thuoc thieu field bat buoc (trong 10 thuoc dau tien)")
                for drug, field in missing_fields[:5]:
                    print(f"  - {drug}: thieu '{field}'")
            
    except ImportError as e:
        errors.append({
            'type': 'import',
            'message': f'Cannot import DRUG_DATABASE: {e}'
        })
    except Exception as e:
        errors.append({
            'type': 'structure',
            'message': f'Error checking database structure: {e}'
        })
    
    if errors:
        print(f"\n[LOI] Tim thay {len(errors)} loi cau truc")
    else:
        print("\n[OK] Cau truc database hop le")
    
    return errors

def check_file_structure() -> List[Dict]:
    """Kiểm tra cấu trúc file"""
    print("\n" + "=" * 70)
    print("4. KIEM TRA CAU TRUC FILE")
    print("=" * 70)
    
    errors = []
    base_path = Path("drugs/drug_modules")
    
    # Check for required __init__.py files
    required_init_files = [
        "drugs/drug_modules/__init__.py",
        "drugs/drug_modules/cardiovascular/__init__.py",
        "drugs/drug_modules/diabetes/__init__.py",
        "drugs/drug_modules/gastrointestinal/__init__.py",
        "drugs/drug_modules/analgesics/__init__.py",
        "drugs/drug_modules/respiratory/__init__.py",
        "drugs/drug_modules/neurological/__init__.py",
        "drugs/drug_modules/hematology/__init__.py",
        "drugs/drug_modules/supportive/__init__.py",
        "drugs/drug_modules/antimicrobial/__init__.py",
        "drugs/drug_modules/metabolic/__init__.py",
        "drugs/drug_modules/endocrinology/__init__.py",
        "drugs/drug_modules/oncology/__init__.py",
        "drugs/drug_modules/emergency/__init__.py",
        "drugs/drug_modules/urology/__init__.py",
        "drugs/drug_modules/dermatology/__init__.py",
        "drugs/drug_modules/ophthalmology/__init__.py",
        "drugs/drug_modules/obstetrics_gynecology/__init__.py",
        "drugs/drug_modules/ent_oral_nasal_combinations/__init__.py",
        "drugs/drug_modules/miscellaneous/__init__.py",
    ]
    
    missing_files = []
    for file_path in required_init_files:
        if not Path(file_path).exists():
            missing_files.append(file_path)
    
    if missing_files:
        errors.append({
            'type': 'file_structure',
            'message': f'Missing {len(missing_files)} __init__.py files',
            'files': missing_files
        })
        print(f"\n[LOI] Thieu {len(missing_files)} file __init__.py:")
        for f in missing_files[:5]:
            print(f"  - {f}")
    else:
        print("\n[OK] Tat ca cac file __init__.py deu ton tai")
    
    return errors

def check_duplicate_drugs() -> List[Dict]:
    """Kiểm tra thuốc trùng lặp"""
    print("\n" + "=" * 70)
    print("5. KIEM TRA THUOC TRUNG LAP")
    print("=" * 70)
    
    errors = []
    
    try:
        sys.path.insert(0, str(Path.cwd()))
        from drugs.drug_database import DRUG_DATABASE
        
        # Check for exact duplicates
        seen = {}
        duplicates = []
        
        for drug_name, drug_data in DRUG_DATABASE.items():
            # Create a simple hash of key fields
            key_fields = (
                drug_data.get('group', ''),
                drug_data.get('vietnamese_name', ''),
                str(drug_data.get('administration', []))
            )
            
            if key_fields in seen:
                duplicates.append({
                    'drug1': seen[key_fields],
                    'drug2': drug_name,
                    'type': 'duplicate'
                })
            else:
                seen[key_fields] = drug_name
        
        if duplicates:
            errors.extend(duplicates)
            print(f"\n[WARNING] Tim thay {len(duplicates)} cap thuoc co the trung lap:")
            for dup in duplicates[:5]:
                print(f"  - {dup['drug1']} va {dup['drug2']}")
        else:
            print("\n[OK] Khong co thuoc trung lap")
            
    except Exception as e:
        errors.append({
            'type': 'duplicate_check',
            'message': f'Error checking duplicates: {e}'
        })
    
    return errors

def main():
    """Main function"""
    print("\n" + "=" * 70)
    print("KIEM TRA TOAN BO HE THONG THUOC")
    print("=" * 70)
    print()
    
    all_errors = []
    
    # Run all checks
    all_errors.extend(check_syntax_errors())
    all_errors.extend(check_import_errors())
    all_errors.extend(check_drug_database_structure())
    all_errors.extend(check_file_structure())
    all_errors.extend(check_duplicate_drugs())
    
    # Summary
    print("\n" + "=" * 70)
    print("TOM TAT")
    print("=" * 70)
    
    if all_errors:
        error_types = {}
        for err in all_errors:
            err_type = err.get('type', 'unknown')
            error_types[err_type] = error_types.get(err_type, 0) + 1
        
        print(f"\n[LOI] Tong cong: {len(all_errors)} loi")
        print("\nPhan loai loi:")
        for err_type, count in sorted(error_types.items()):
            print(f"  - {err_type}: {count} loi")
    else:
        print("\n[OK] HE THONG KHONG CO LOI NAO!")
        print("  Tat ca cac kiem tra deu thanh cong.")
    
    print("\n" + "=" * 70)

if __name__ == "__main__":
    main()

