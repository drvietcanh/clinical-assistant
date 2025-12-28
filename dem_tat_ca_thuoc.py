"""
Script đếm tất cả thuốc trong project
"""
import sys
import os
sys.path.insert(0, '.')

from tim_kiem_bo_sung_fields_thuoc import load_module_direct

# Các file lớn cần kiểm tra
large_files = [
    'drugs/drug_modules/dermatology.py',
    'drugs/drug_modules/hematology.py',
    'drugs/drug_modules/ophthalmology.py',
    'drugs/drug_modules/urology.py',
    'drugs/drug_modules/obstetrics_gynecology.py',
    'drugs/drug_modules/ent_oral_nasal_combinations.py',
]

# Các file module chính
module_files = [
    'drugs/drug_modules/antimicrobial.py',
    'drugs/drug_modules/cardiovascular.py',
    'drugs/drug_modules/diabetes.py',
    'drugs/drug_modules/emergency.py',
    'drugs/drug_modules/gastrointestinal.py',
    'drugs/drug_modules/neurological.py',
    'drugs/drug_modules/oncology.py',
    'drugs/drug_modules/respiratory.py',
    'drugs/drug_modules/other.py',
    'drugs/drug_modules/miscellaneous.py',
    'drugs/drug_modules/supportive.py',
    'drugs/drug_modules/psychiatry_other.py',
    'drugs/drug_modules/metabolic.py',
    'drugs/drug_modules/endocrinology_other.py',
    'drugs/drug_modules/infectious_other.py',
    'drugs/drug_modules/cardiovascular_other.py',
    'drugs/drug_modules/analgesics.py',
]

all_files = large_files + module_files

print("=" * 60)
print("DEM TAT CA THUOC TRONG CAC FILE LON")
print("=" * 60)
print()

total = 0
file_counts = {}

for file_path in all_files:
    if os.path.exists(file_path):
        try:
            drugs = load_module_direct(file_path)
            count = len(drugs)
            if count > 0:
                file_counts[file_path] = count
                total += count
                print(f"{file_path}: {count} thuoc")
        except Exception as e:
            print(f"{file_path}: ERROR - {e}")

print()
print("=" * 60)
print(f"TONG SO THUOC TU CAC FILE LON: {total}")
print("=" * 60)
print()

# Sắp xếp theo số lượng
sorted_files = sorted(file_counts.items(), key=lambda x: x[1], reverse=True)
print("Top 10 file chua nhieu thuoc nhat:")
for i, (file_path, count) in enumerate(sorted_files[:10], 1):
    print(f"{i}. {os.path.basename(file_path)}: {count} thuoc")

