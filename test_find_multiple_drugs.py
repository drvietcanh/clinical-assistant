"""
Test tìm file cho nhiều thuốc
"""
import sys
from pathlib import Path
sys.path.insert(0, str(Path.cwd()))
from add_missing_fields_simple import find_drug_file
from check_missing_fields_final import load_all_drugs, check_drug_fields

# Load drugs
print("Dang load drugs...")
all_drugs = load_all_drugs()

# Lấy 10 thuốc đầu tiên thiếu enhanced fields
drugs_to_test = []
for drug_name, fields in all_drugs.items():
    if 'group' not in fields and 'vietnamese_name' not in fields:
        continue
    
    is_field_name = (
        drug_name.islower() and 
        '_' in drug_name and 
        drug_name.count('_') >= 2 and
        drug_name not in ['iv', 'po', 'im', 'sc']
    )
    
    if is_field_name:
        continue
    
    result = check_drug_fields(drug_name, fields)
    if result['missing_enhanced']:
        drugs_to_test.append((drug_name, result['missing_enhanced']))
        if len(drugs_to_test) >= 10:
            break

print(f"\nTest tim file cho {len(drugs_to_test)} thuoc:")
print("=" * 70)

for drug_name, missing_fields in drugs_to_test:
    file_path = find_drug_file(drug_name)
    if file_path:
        print(f"[OK] {drug_name}: {file_path.name}")
    else:
        print(f"[LOI] {drug_name}: Khong tim thay file")

