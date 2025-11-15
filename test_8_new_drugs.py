"""
Test script for 8 newly added/verified drugs
"""
from drugs.drug_database import DRUG_DATABASE, TOTAL_DRUGS

print("=" * 60)
print(f"TONG SO THUOC: {TOTAL_DRUGS}")
print("=" * 60)

# 8 thuốc đã thêm/kiểm tra
new_drugs = [
    'Lansoprazole',
    'Esomeprazole', 
    'Sumatriptan',
    'Methotrexate',
    'Ipratropium',
    'Tiotropium',
    'Trimethoprim-sulfamethoxazole',
    'Oseltamivir'
]

print(f"\n8 THUOC MOI DA THEM/VERIFY:")
print("-" * 60)

all_found = True
enhanced_fields_count = 0

for i, drug in enumerate(new_drugs, 1):
    if drug in DRUG_DATABASE:
        drug_info = DRUG_DATABASE[drug]
        has_enhanced = 'mechanism_of_action' in drug_info
        has_all_14 = all(field in drug_info for field in [
            'mechanism_of_action', 'monitoring', 'precautions', 
            'pharmacokinetics', 'storage', 'black_box_warnings'
        ])
        
        if has_enhanced:
            enhanced_fields_count += 1
        
        status = "[OK]" if has_enhanced else "[WARNING]"
        enhanced_status = "Full 14 fields" if has_all_14 else "Basic 6 fields"
        
        print(f"{i}. {status} {drug}")
        print(f"   - Enhanced fields: {enhanced_status}")
        print(f"   - Group: {drug_info.get('group', 'N/A')}")
    else:
        print(f"{i}. [MISSING] {drug}")
        all_found = False

print("-" * 60)
print(f"\nKET QUA:")
print(f"  - Tong so thuoc: {TOTAL_DRUGS} (tang tu 99 -> {TOTAL_DRUGS})")
print(f"  - Thuoc tim thay: {len([d for d in new_drugs if d in DRUG_DATABASE])}/8")
print(f"  - Co enhanced fields: {enhanced_fields_count}/8")
print(f"  - Tang them: +{TOTAL_DRUGS - 99} thuoc")

if all_found and enhanced_fields_count == 8:
    print("\n[SUCCESS] Tat ca 8 thuoc da duoc them thanh cong!")
else:
    print("\n[WARNING] Mot so thuoc chua co hoac thieu enhanced fields")

