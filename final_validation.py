"""
Validation cuối cùng
Kiểm tra tất cả thuốc load được, field đầy đủ, không có lỗi import
"""
import sys
import traceback
from pathlib import Path
from typing import Dict, List, Any

def test_imports():
    """Kiểm tra imports"""
    print("="*60)
    print("KIEM TRA IMPORTS")
    print("="*60)
    
    errors = []
    warnings = []
    
    # Test main modules
    modules_to_test = [
        'CARDIOVASCULAR_DRUGS',
        'DIABETES_DRUGS',
        'GASTROINTESTINAL_DRUGS',
        'ANALGESICS_DRUGS',
        'RESPIRATORY_DRUGS',
        'NEUROLOGICAL_DRUGS',
        'HEMATOLOGY_DRUGS',
        'SUPPORTIVE_DRUGS',
        'ANTIMICROBIAL_DRUGS',
        'METABOLIC_DRUGS',
        'ENDOCRINOLOGY_DRUGS',
        'ONCOLOGY_DRUGS',
        'EMERGENCY_DRUGS',
        'UROLOGY_DRUGS',
        'DERMATOLOGY_DRUGS',
        'OPHTHALMOLOGY_DRUGS',
        'OBSTETRICS_GYNECOLOGY_DRUGS',
        'ENT_ORAL_NASAL_COMBINATIONS_DRUGS',
        'MISCELLANEOUS_DRUGS',
    ]
    
    try:
        from drugs.drug_modules import ALL_DRUGS
        print(f"✓ ALL_DRUGS imported: {len(ALL_DRUGS)} drugs")
    except Exception as e:
        errors.append(f"Failed to import ALL_DRUGS: {e}")
        print(f"✗ Failed to import ALL_DRUGS: {e}")
    
    for module_name in modules_to_test:
        try:
            module = __import__(f'drugs.drug_modules', fromlist=[module_name])
            drugs = getattr(module, module_name)
            count = len(drugs) if isinstance(drugs, dict) else 0
            print(f"✓ {module_name}: {count} drugs")
        except Exception as e:
            errors.append(f"Failed to import {module_name}: {e}")
            print(f"✗ Failed to import {module_name}: {e}")
    
    try:
        from drugs.drug_database import DRUG_DATABASE
        print(f"✓ DRUG_DATABASE imported: {len(DRUG_DATABASE)} drugs")
    except Exception as e:
        errors.append(f"Failed to import DRUG_DATABASE: {e}")
        print(f"✗ Failed to import DRUG_DATABASE: {e}")
    
    return len(errors) == 0, errors, warnings

def test_drug_loading():
    """Kiểm tra tất cả thuốc load được"""
    print("\n" + "="*60)
    print("KIEM TRA LOAD THUOC")
    print("="*60)
    
    errors = []
    warnings = []
    
    try:
        from drugs.drug_database import DRUG_DATABASE
        
        total_drugs = len(DRUG_DATABASE)
        print(f"Total drugs loaded: {total_drugs}")
        
        # Kiểm tra một số thuốc mẫu
        sample_drugs = list(DRUG_DATABASE.keys())[:10]
        for drug_name in sample_drugs:
            drug_data = DRUG_DATABASE[drug_name]
            if not isinstance(drug_data, dict):
                errors.append(f"{drug_name}: Not a dict")
            elif 'group' not in drug_data:
                warnings.append(f"{drug_name}: Missing 'group' field")
            else:
                print(f"✓ {drug_name}: OK")
        
        if total_drugs < 700:
            warnings.append(f"Total drugs ({total_drugs}) seems low, expected ~700+")
        
    except Exception as e:
        errors.append(f"Failed to load drugs: {e}")
        traceback.print_exc()
    
    return len(errors) == 0, errors, warnings

def test_field_completeness():
    """Kiểm tra field đầy đủ"""
    print("\n" + "="*60)
    print("KIEM TRA FIELD DAY DU")
    print("="*60)
    
    from drugs.field_validator import get_field_validator
    from drugs.drug_database import DRUG_DATABASE
    
    validator = get_field_validator()
    
    # Validate một số thuốc mẫu
    sample_drugs = list(DRUG_DATABASE.keys())[:20]
    results = {}
    
    for drug_name in sample_drugs:
        drug_data = DRUG_DATABASE[drug_name]
        result = validator.validate_all_fields(drug_data)
        results[drug_name] = result
        
        if result['valid']:
            print(f"✓ {drug_name}: Valid")
        else:
            missing = len(result['missing_standard_fields'])
            if missing > 0:
                print(f"⚠ {drug_name}: Missing {missing} standard fields")
            else:
                print(f"✓ {drug_name}: Valid (warnings only)")
    
    # Thống kê
    valid_count = sum(1 for r in results.values() if r['valid'])
    total_count = len(results)
    
    print(f"\nValidation summary: {valid_count}/{total_count} drugs are valid")
    
    return valid_count == total_count, [], []

def test_index_system():
    """Kiểm tra hệ thống index"""
    print("\n" + "="*60)
    print("KIEM TRA HE THONG INDEX")
    print("="*60)
    
    errors = []
    
    try:
        from drugs.drug_index_system import get_drug_index
        
        index = get_drug_index()
        stats = index.get_statistics()
        
        print(f"✓ Index loaded: {stats['total_drugs']} drugs")
        print(f"✓ Modules: {stats['total_modules']}")
        print(f"✓ Groups: {stats['total_groups']}")
        
        # Test search
        results = index.search("metformin")
        if results:
            print(f"✓ Search works: Found {len(results)} results for 'metformin'")
        else:
            warnings = ["Search returned no results"]
        
    except Exception as e:
        errors.append(f"Index system error: {e}")
        traceback.print_exc()
    
    return len(errors) == 0, errors, []

def test_manager_tool():
    """Kiểm tra manager tool"""
    print("\n" + "="*60)
    print("KIEM TRA MANAGER TOOL")
    print("="*60)
    
    errors = []
    
    try:
        from drugs.drug_manager_tool import get_drug_manager
        
        manager = get_drug_manager()
        
        # Test find file
        files = manager.find_drug_file("Metformin")
        if files:
            print(f"✓ Find file works: Found {len(files)} file(s)")
        else:
            warnings = ["Find file returned no results"]
        
        # Test suggest placement
        new_drug = {
            "group": "Cardiovascular - ACE Inhibitor",
            "indications": ["Hypertension"]
        }
        suggestion = manager.suggest_placement(new_drug)
        print(f"✓ Suggest placement works: {suggestion['module']}")
        
        # Test duplicates
        duplicates = manager.find_duplicates()
        if duplicates:
            print(f"⚠ Found {len(duplicates)} duplicate drugs")
        else:
            print(f"✓ No duplicates found")
        
    except Exception as e:
        errors.append(f"Manager tool error: {e}")
        traceback.print_exc()
    
    return len(errors) == 0, errors, []

def main():
    """Hàm chính"""
    import io
    if sys.platform == 'win32':
        sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')
    
    print("BAT DAU VALIDATION CUOI CUNG")
    print("="*60)
    
    all_passed = True
    all_errors = []
    all_warnings = []
    
    # Test imports
    passed, errors, warnings = test_imports()
    all_passed = all_passed and passed
    all_errors.extend(errors)
    all_warnings.extend(warnings)
    
    # Test drug loading
    passed, errors, warnings = test_drug_loading()
    all_passed = all_passed and passed
    all_errors.extend(errors)
    all_warnings.extend(warnings)
    
    # Test field completeness
    passed, errors, warnings = test_field_completeness()
    all_passed = all_passed and passed
    all_errors.extend(errors)
    all_warnings.extend(warnings)
    
    # Test index system
    passed, errors, warnings = test_index_system()
    all_passed = all_passed and passed
    all_errors.extend(errors)
    all_warnings.extend(warnings)
    
    # Test manager tool
    passed, errors, warnings = test_manager_tool()
    all_passed = all_passed and passed
    all_errors.extend(errors)
    all_warnings.extend(warnings)
    
    # Summary
    print("\n" + "="*60)
    print("TOM TAT VALIDATION")
    print("="*60)
    
    if all_passed:
        print("✓ TẤT CẢ KIỂM TRA ĐÃ PASS")
    else:
        print("✗ CÓ LỖI TRONG KIỂM TRA")
    
    if all_errors:
        print(f"\nErrors ({len(all_errors)}):")
        for error in all_errors[:10]:
            print(f"  - {error}")
    
    if all_warnings:
        print(f"\nWarnings ({len(all_warnings)}):")
        for warning in all_warnings[:10]:
            print(f"  - {warning}")
    
    print("="*60)
    
    return 0 if all_passed else 1

if __name__ == "__main__":
    sys.exit(main())

