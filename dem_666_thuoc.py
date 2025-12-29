"""
Script dem tat ca 666 thuoc trong database
"""
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

# Import truc tiep tu drug_modules
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
    ONCOLOGY_DRUGS,
    EMERGENCY_DRUGS,
    OTHER_DRUGS,
    DERMATOLOGY_DRUGS,
    OPHTHALMOLOGY_DRUGS,
    UROLOGY_DRUGS,
    OBSTETRICS_GYNECOLOGY_DRUGS,
    ENT_ORAL_NASAL_COMBINATIONS_DRUGS,
    CARDIOVASCULAR_OTHER_DRUGS,
    INFECTIOUS_OTHER_DRUGS,
    PSYCHIATRY_OTHER_DRUGS,
    ENDOCRINOLOGY_OTHER_DRUGS,
    MISCELLANEOUS_DRUGS,
)

print("=" * 70)
print("KIEM TRA SO LUONG THUOC TRONG DATABASE")
print("=" * 70)
print()

modules = {
    "CARDIOVASCULAR_DRUGS": CARDIOVASCULAR_DRUGS,
    "DIABETES_DRUGS": DIABETES_DRUGS,
    "GASTROINTESTINAL_DRUGS": GASTROINTESTINAL_DRUGS,
    "ANALGESICS_DRUGS": ANALGESICS_DRUGS,
    "RESPIRATORY_DRUGS": RESPIRATORY_DRUGS,
    "NEUROLOGICAL_DRUGS": NEUROLOGICAL_DRUGS,
    "HEMATOLOGY_DRUGS": HEMATOLOGY_DRUGS,
    "SUPPORTIVE_DRUGS": SUPPORTIVE_DRUGS,
    "ANTIMICROBIAL_DRUGS": ANTIMICROBIAL_DRUGS,
    "METABOLIC_DRUGS": METABOLIC_DRUGS,
    "ONCOLOGY_DRUGS": ONCOLOGY_DRUGS,
    "EMERGENCY_DRUGS": EMERGENCY_DRUGS,
    "OTHER_DRUGS": OTHER_DRUGS,
    "DERMATOLOGY_DRUGS": DERMATOLOGY_DRUGS,
    "OPHTHALMOLOGY_DRUGS": OPHTHALMOLOGY_DRUGS,
    "UROLOGY_DRUGS": UROLOGY_DRUGS,
    "OBSTETRICS_GYNECOLOGY_DRUGS": OBSTETRICS_GYNECOLOGY_DRUGS,
    "ENT_ORAL_NASAL_COMBINATIONS_DRUGS": ENT_ORAL_NASAL_COMBINATIONS_DRUGS,
    "CARDIOVASCULAR_OTHER_DRUGS": CARDIOVASCULAR_OTHER_DRUGS,
    "INFECTIOUS_OTHER_DRUGS": INFECTIOUS_OTHER_DRUGS,
    "PSYCHIATRY_OTHER_DRUGS": PSYCHIATRY_OTHER_DRUGS,
    "ENDOCRINOLOGY_OTHER_DRUGS": ENDOCRINOLOGY_OTHER_DRUGS,
    "MISCELLANEOUS_DRUGS": MISCELLANEOUS_DRUGS,
}

# Merge all
all_drugs = {}
for name, drugs in modules.items():
    all_drugs.update(drugs)

total = len(all_drugs)

print(f"TONG SO THUOC: {total}")
print()

if total == 666:
    print("OK! Co dung 666 thuoc!")
elif total < 666:
    print(f"THIEU: {666 - total} thuoc")
else:
    print(f"THUA: {total - 666} thuoc")

print()
print("=" * 70)
print("PHAN TICH THEO MODULE")
print("=" * 70)
print()

total_count = 0
for name, drugs in sorted(modules.items(), key=lambda x: len(x[1]), reverse=True):
    count = len(drugs)
    total_count += count
    print(f"{name:40s}: {count:3d} thuoc")

print("-" * 70)
print(f"{'TONG CONG':40s}: {total_count:3d} thuoc")
print("=" * 70)

# Kiem tra duplicate
all_drug_names = list(all_drugs.keys())
duplicates = [name for name in all_drug_names if all_drug_names.count(name) > 1]
unique_duplicates = list(set(duplicates))

if unique_duplicates:
    print()
    print(f"PHAT HIEN {len(unique_duplicates)} THUOC TRUNG LAP:")
    for dup in unique_duplicates[:10]:
        print(f"  - {dup}")
    if len(unique_duplicates) > 10:
        print(f"  ... va {len(unique_duplicates) - 10} thuoc khac")
else:
    print()
    print("OK! Khong co thuoc trung lap!")

