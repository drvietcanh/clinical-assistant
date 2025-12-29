"""
Get exact drug count by importing modules directly
Bypasses drugs package __init__ to avoid streamlit
"""
import sys
import importlib.util
from pathlib import Path

# Mock streamlit to avoid import errors
class MockStreamlit:
    def __getattr__(self, name):
        return lambda *args, **kwargs: None

sys.modules['streamlit'] = MockStreamlit()

# Now try to import drug_database
try:
    # Add current directory to path
    sys.path.insert(0, str(Path.cwd()))
    
    # Import drug_database directly
    from drugs.drug_database import DRUG_DATABASE, TOTAL_DRUGS
    
    print("=" * 70)
    print("SO LUONG THUOC CHINH XAC")
    print("=" * 70)
    print()
    print(f"Tong so thuoc trong DRUG_DATABASE: {len(DRUG_DATABASE)}")
    print(f"Tong so thuoc (TOTAL_DRUGS): {TOTAL_DRUGS}")
    print()
    
    # Also get counts by module
    from drugs.drug_modules import (
        CARDIOVASCULAR_DRUGS,
        DIABETES_DRUGS,
        GASTROINTESTINAL_DRUGS,
        ANALGESICS_DRUGS,
        RESPIRATORY_DRUGS,
        NEUROLOGICAL_DRUGS,
        HEMATOLOGY_DRUGS,
        SUPPORTIVE_DRUGS,
        ANTIMICROBIAL_DRUGS,
        METABOLIC_DRUGS,
        ENDOCRINOLOGY_DRUGS,
        ONCOLOGY_DRUGS,
        EMERGENCY_DRUGS,
        UROLOGY_DRUGS,
        DERMATOLOGY_DRUGS,
        OPHTHALMOLOGY_DRUGS,
        OBSTETRICS_GYNECOLOGY_DRUGS,
        ENT_ORAL_NASAL_COMBINATIONS_DRUGS,
        MISCELLANEOUS_DRUGS,
    )
    
    modules = {
        "Cardiovascular": CARDIOVASCULAR_DRUGS,
        "Diabetes": DIABETES_DRUGS,
        "Gastrointestinal": GASTROINTESTINAL_DRUGS,
        "Analgesics": ANALGESICS_DRUGS,
        "Respiratory": RESPIRATORY_DRUGS,
        "Neurological": NEUROLOGICAL_DRUGS,
        "Hematology": HEMATOLOGY_DRUGS,
        "Supportive": SUPPORTIVE_DRUGS,
        "Antimicrobial": ANTIMICROBIAL_DRUGS,
        "Metabolic": METABOLIC_DRUGS,
        "Endocrinology": ENDOCRINOLOGY_DRUGS,
        "Oncology": ONCOLOGY_DRUGS,
        "Emergency": EMERGENCY_DRUGS,
        "Urology": UROLOGY_DRUGS,
        "Dermatology": DERMATOLOGY_DRUGS,
        "Ophthalmology": OPHTHALMOLOGY_DRUGS,
        "Obstetrics/Gynecology": OBSTETRICS_GYNECOLOGY_DRUGS,
        "ENT/Oral/Nasal": ENT_ORAL_NASAL_COMBINATIONS_DRUGS,
        "Miscellaneous": MISCELLANEOUS_DRUGS,
    }
    
    print("SO LUONG THUOC THEO MODULE:")
    print("-" * 70)
    print(f"{'Module':<30} {'So luong':<12} {'%':<10}")
    print("-" * 70)
    
    total_by_modules = 0
    for name, drugs in sorted(modules.items(), key=lambda x: len(x[1]), reverse=True):
        count = len(drugs)
        total_by_modules += count
        percentage = (count / len(DRUG_DATABASE) * 100) if len(DRUG_DATABASE) > 0 else 0
        print(f"{name:<30} {count:<12} {percentage:>6.1f}%")
    
    print("-" * 70)
    print(f"{'TONG (tu modules)':<30} {total_by_modules:<12}")
    print()
    
    # Check for duplicates
    all_names = set()
    duplicates = []
    for name, drugs in modules.items():
        for drug_name in drugs.keys():
            if drug_name in all_names:
                duplicates.append((drug_name, name))
            else:
                all_names.add(drug_name)
    
    print("=" * 70)
    print(f"KET QUA:")
    print(f"  - Tong so thuoc trong DRUG_DATABASE: {len(DRUG_DATABASE)}")
    print(f"  - Tong so thuoc tu cac module: {total_by_modules}")
    print(f"  - So thuoc duy nhat (khong trung): {len(all_names)}")
    
    if duplicates:
        print(f"  - So thuoc trung lap: {len(duplicates)}")
        if len(duplicates) <= 20:
            print("\n  Cac thuoc trung lap:")
            for drug_name, module in duplicates:
                print(f"    - {drug_name} (trong {module})")
    else:
        print(f"  - Khong co thuoc trung lap")
    
    print("=" * 70)
    
except Exception as e:
    print(f"Loi khi import: {e}")
    import traceback
    traceback.print_exc()
    print("\nKhong the lay so luong chinh xac do loi import.")
    print("Vui long kiem tra moi truong Python co cai dat streamlit.")

