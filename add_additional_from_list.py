"""Bổ sung field bổ sung từ danh sách"""
import sys
import json
from pathlib import Path
import io

sys.path.insert(0, str(Path.cwd()))

from add_fields_helper import add_additional_fields

if sys.platform == 'win32' and not isinstance(sys.stdout, io.TextIOWrapper):
    try:
        sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')
    except:
        pass

# Load danh sách
with open('drugs_missing_additional_list.json', 'r', encoding='utf-8') as f:
    drugs = json.load(f)

print("="*60)
print(f"BAT DAU BO SUNG FIELD BO SUNG")
print(f"Tong so thuoc: {len(drugs)}")
print("="*60)

success = 0
failed = 0
skipped = 0

for i, drug_info in enumerate(drugs, 1):
    drug_name = drug_info['name']
    file_path = drug_info['file']
    missing = drug_info['missing']
    
    print(f"\n[{i}/{len(drugs)}] {drug_name}")
    print(f"  File: {file_path}")
    print(f"  Thieu {len(missing)} field: {', '.join(missing[:3])}")
    if len(missing) > 3:
        print(f"  ... va {len(missing) - 3} field khac")
    
    try:
        result = add_additional_fields(drug_name, file_path, dry_run=False)
        if result['success'] and result.get('added_fields'):
            success += 1
            print(f"  ✓ Da bo sung {len(result['added_fields'])} field")
        else:
            skipped += 1
            print(f"  - Khong bo sung duoc")
    except Exception as e:
        failed += 1
        print(f"  ✗ Loi: {e}")

print("\n" + "="*60)
print("KET QUA")
print("="*60)
print(f"Thanh cong: {success}")
print(f"Loi/Bo qua: {failed + skipped}")
print(f"Tong: {len(drugs)}")

