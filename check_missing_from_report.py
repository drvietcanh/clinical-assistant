"""Kiểm tra thuốc thiếu field từ báo cáo"""
import json

with open('comprehensive_field_check_report.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

drugs_missing_additional = []
for drug_name, drug_info in data['all_drugs'].items():
    missing_standard = drug_info.get('missing_standard_fields', [])
    missing_additional = drug_info.get('missing_additional_fields', [])
    
    if len(missing_standard) == 0 and len(missing_additional) > 0:
        drugs_missing_additional.append({
            'name': drug_name,
            'file': drug_info.get('file', ''),
            'missing': missing_additional
        })

print(f"Found {len(drugs_missing_additional)} drugs with all standard fields but missing additional fields")
print("\nTop 20:")
for i, drug in enumerate(drugs_missing_additional[:20], 1):
    print(f"{i}. {drug['name']}")
    print(f"   File: {drug['file']}")
    print(f"   Missing {len(drug['missing'])} fields: {', '.join(drug['missing'][:5])}")
    if len(drug['missing']) > 5:
        print(f"   ... and {len(drug['missing']) - 5} more")
    print()

# Save to file
with open('drugs_missing_additional_list.json', 'w', encoding='utf-8') as f:
    json.dump(drugs_missing_additional, f, indent=2, ensure_ascii=False)

print(f"\nSaved to drugs_missing_additional_list.json")

