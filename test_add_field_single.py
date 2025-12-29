"""
Test thêm field cho một thuốc cụ thể
"""
import sys
from pathlib import Path
sys.path.insert(0, str(Path.cwd()))
from add_missing_fields_simple import add_fields_to_drug, find_drug_file
from check_missing_fields_final import load_all_drugs, check_drug_fields

# Test với Entecavir (thiếu 2 fields)
drug_name = "Entecavir"

print("=" * 70)
print(f"TEST: {drug_name}")
print("=" * 70)

# Load và kiểm tra
all_drugs = load_all_drugs()
if drug_name in all_drugs:
    fields = all_drugs[drug_name]
    result = check_drug_fields(drug_name, fields)
    print(f"\nMissing enhanced fields: {result['missing_enhanced']}")
    
    # Tìm file
    file_path = find_drug_file(drug_name)
    if file_path:
        print(f"File: {file_path}")
        
        # Thử thêm field (dry-run)
        success = add_fields_to_drug(
            file_path, 
            drug_name, 
            result['missing_enhanced'],
            dry_run=True
        )
        print(f"\nResult: {'Success' if success else 'Failed'}")
    else:
        print("Khong tim thay file")
else:
    print("Khong tim thay thuoc trong danh sach")

