"""Script kiem tra cac thuoc con thieu fields"""
import sys
import os
sys.path.insert(0, os.path.dirname(__file__))

from kiem_tra_fields_tat_ca_thuoc_v3 import load_all_drugs, check_drug_fields

all_drugs = load_all_drugs()
results = []

for name, data in sorted(all_drugs.items()):
    result = check_drug_fields(name, data)
    if result and not result['has_all_fields']:
        results.append(result)

results.sort(key=lambda x: x['total_missing'], reverse=True)

print(f"\nTong so thuoc thieu fields: {len(results)}")
print("\n20 thuoc thieu nhieu fields nhat:")
for i, r in enumerate(results[:20], 1):
    print(f"{i}. {r['drug_name']}:")
    print(f"   Thieu {r['total_missing']} fields")
    if r['missing_required']:
        print(f"   Required: {', '.join(r['missing_required'])}")
    if r['missing_optional']:
        print(f"   Optional: {', '.join(r['missing_optional'])}")
    print()

