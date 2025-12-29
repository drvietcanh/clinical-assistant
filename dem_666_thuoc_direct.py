"""
Script dem tat ca 666 thuoc - import truc tiep
"""
import sys
import os
import importlib.util

# Import truc tiep tu drug_modules ma khong qua __init__.py
def load_module_direct(filepath):
    """Load module tu file Python"""
    spec = importlib.util.spec_from_file_location("module", filepath)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module

# Load cac module
base_path = "drugs/drug_modules"
modules_info = {
    "CARDIOVASCULAR_DRUGS": f"{base_path}/cardiovascular.py",
    "DIABETES_DRUGS": f"{base_path}/diabetes.py",
    "GASTROINTESTINAL_DRUGS": f"{base_path}/gastrointestinal.py",
    "ANALGESICS_DRUGS": f"{base_path}/analgesics.py",
    "RESPIRATORY_DRUGS": f"{base_path}/respiratory.py",
    "NEUROLOGICAL_DRUGS": f"{base_path}/neurological.py",
    "HEMATOLOGY_DRUGS": f"{base_path}/hematology.py",
    "SUPPORTIVE_DRUGS": f"{base_path}/supportive.py",
    "ANTIMICROBIAL_DRUGS": f"{base_path}/antimicrobial.py",
    "METABOLIC_DRUGS": f"{base_path}/metabolic.py",
    "ONCOLOGY_DRUGS": f"{base_path}/oncology.py",
    "EMERGENCY_DRUGS": f"{base_path}/emergency.py",
    "OTHER_DRUGS": f"{base_path}/other.py",
    "DERMATOLOGY_DRUGS": f"{base_path}/dermatology.py",
    "OPHTHALMOLOGY_DRUGS": f"{base_path}/ophthalmology.py",
    "UROLOGY_DRUGS": f"{base_path}/urology.py",
    "OBSTETRICS_GYNECOLOGY_DRUGS": f"{base_path}/obstetrics_gynecology.py",
    "ENT_ORAL_NASAL_COMBINATIONS_DRUGS": f"{base_path}/ent_oral_nasal_combinations.py",
    "CARDIOVASCULAR_OTHER_DRUGS": f"{base_path}/cardiovascular_other.py",
    "INFECTIOUS_OTHER_DRUGS": f"{base_path}/infectious_other.py",
    "PSYCHIATRY_OTHER_DRUGS": f"{base_path}/psychiatry_other.py",
    "ENDOCRINOLOGY_OTHER_DRUGS": f"{base_path}/endocrinology_other.py",
    "MISCELLANEOUS_DRUGS": f"{base_path}/miscellaneous.py",
}

print("=" * 70)
print("KIEM TRA SO LUONG THUOC TRONG DATABASE")
print("=" * 70)
print()

modules = {}
all_drugs = {}
errors = []

for name, filepath in modules_info.items():
    if os.path.exists(filepath):
        try:
            module = load_module_direct(filepath)
            drugs = getattr(module, name, {})
            count = len(drugs) if isinstance(drugs, dict) else 0
            modules[name] = drugs if isinstance(drugs, dict) else {}
            all_drugs.update(modules[name])
            print(f"{name:40s}: {count:3d} thuoc")
        except Exception as e:
            errors.append((name, str(e)))
            print(f"{name:40s}: ERROR - {str(e)[:50]}")
    else:
        print(f"{name:40s}: FILE NOT FOUND")

print()
print("=" * 70)
total = len(all_drugs)
print(f"TONG SO THUOC: {total}")
print("=" * 70)
print()

if total == 666:
    print("OK! Co dung 666 thuoc!")
elif total < 666:
    print(f"THIEU: {666 - total} thuoc")
else:
    print(f"THUA: {total - 666} thuoc")

if errors:
    print()
    print("=" * 70)
    print("LOI KHI LOAD:")
    print("=" * 70)
    for name, error in errors:
        print(f"{name}: {error}")

# Kiem tra duplicate
all_drug_names = list(all_drugs.keys())
duplicates = [name for name in all_drug_names if all_drug_names.count(name) > 1]
unique_duplicates = list(set(duplicates))

if unique_duplicates:
    print()
    print("=" * 70)
    print(f"PHAT HIEN {len(unique_duplicates)} THUOC TRUNG LAP:")
    print("=" * 70)
    for dup in unique_duplicates[:20]:
        print(f"  - {dup}")
    if len(unique_duplicates) > 20:
        print(f"  ... va {len(unique_duplicates) - 20} thuoc khac")

