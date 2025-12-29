"""
Script đếm tất cả thuốc trong tất cả file
"""
import sys
import os
import re
sys.path.insert(0, '.')

from tim_kiem_bo_sung_fields_thuoc import scan_directory_recursive, load_module_direct

# Scan toàn bộ thư mục drugs
all_drugs = {}
base_path = 'drugs'
drug_file_map = scan_directory_recursive(base_path, all_drugs)

print("=" * 70)
print("TONG KET DEM TAT CA THUOC")
print("=" * 70)
print()
print(f"Tong so thuoc tim thay: {len(all_drugs)}")
print()

# Đếm theo file
file_counts = {}
for drug_name, filepath in drug_file_map.items():
    if filepath not in file_counts:
        file_counts[filepath] = 0
    file_counts[filepath] += 1

# Sắp xếp theo số lượng
sorted_files = sorted(file_counts.items(), key=lambda x: x[1], reverse=True)

print("Top 20 file chua nhieu thuoc nhat:")
print("-" * 70)
for i, (filepath, count) in enumerate(sorted_files[:20], 1):
    rel_path = os.path.relpath(filepath, base_path)
    print(f"{i:2d}. {rel_path:60s} {count:3d} thuoc")

print()
print("=" * 70)
print(f"TONG CONG: {len(all_drugs)} thuoc tu {len(file_counts)} file")
print("=" * 70)

