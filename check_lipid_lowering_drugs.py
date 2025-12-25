#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Kiểm tra các thuốc hạ lipid máu mới trong database
"""

from drugs.drug_database import DRUG_DATABASE

# Danh sách thuốc hạ lipid máu cần kiểm tra
LIPID_DRUGS = {
    "Icosapent ethyl": "Omega-3 liều cao (EPA)",
    "Omega-3 acid ethyl esters": "Omega-3 hỗn hợp (EPA/DHA)",
    "Niacin": "Vitamin B3 (Nicotinic acid)",
    "Ezetimibe": "Ức chế hấp thu cholesterol",
    "Bempedoic acid": "ATP-Citrate Lyase Inhibitor",
    "Alirocumab": "PCSK9 Inhibitor (mAb)",
    "Evolocumab": "PCSK9 Inhibitor (mAb)",
    "Inclisiran": "PCSK9 Inhibitor (siRNA)",
    "Volanesorsen": "Ức chế Apo C-III (antisense)",
    "Olezarsen": "Ức chế Apo C-III (antisense)",
}

print("=" * 100)
print("KIỂM TRA CÁC THUỐC HẠ LIPID MÁU MỚI")
print("=" * 100)
print(f"\nTổng số thuốc trong database: {len(DRUG_DATABASE)}")
print()

# Kiểm tra từng thuốc
found_drugs = []
missing_drugs = []
partial_matches = []

for drug_name, description in LIPID_DRUGS.items():
    # Kiểm tra exact match
    if drug_name in DRUG_DATABASE:
        found_drugs.append((drug_name, description))
    else:
        # Kiểm tra partial match (case-insensitive)
        found_partial = False
        for db_drug in DRUG_DATABASE.keys():
            if drug_name.lower() in db_drug.lower() or db_drug.lower() in drug_name.lower():
                partial_matches.append((drug_name, db_drug, description))
                found_partial = True
                break
        
        if not found_partial:
            missing_drugs.append((drug_name, description))

# In kết quả
print("=" * 100)
print("KẾT QUẢ KIỂM TRA")
print("=" * 100)

if found_drugs:
    print(f"\n✅ THUỐC ĐÃ CÓ TRONG DATABASE ({len(found_drugs)} thuốc):")
    for drug, desc in found_drugs:
        drug_data = DRUG_DATABASE[drug]
        has_enhanced = "mechanism_of_action" in drug_data
        enhanced_status = "✓ Có enhanced fields" if has_enhanced else "⚠ Chưa có enhanced fields"
        print(f"   {drug:<30} - {desc:<40} {enhanced_status}")

if partial_matches:
    print(f"\n⚠️  THUỐC CÓ THỂ TRÙNG LẶP ({len(partial_matches)} thuốc):")
    for proposed, existing, desc in partial_matches:
        print(f"   {proposed:<30} - Có thể là: {existing:<30} ({desc})")

if missing_drugs:
    print(f"\n❌ THUỐC CHƯA CÓ TRONG DATABASE ({len(missing_drugs)} thuốc):")
    for drug, desc in missing_drugs:
        print(f"   {drug:<30} - {desc}")

# Thống kê enhanced fields cho các thuốc đã có
print("\n" + "=" * 100)
print("CHI TIẾT ENHANCED FIELDS CHO CÁC THUỐC ĐÃ CÓ")
print("=" * 100)

required_fields = ['mechanism_of_action', 'monitoring', 'precautions', 
                  'pharmacokinetics', 'storage', 'black_box_warnings']

for drug, desc in found_drugs:
    drug_data = DRUG_DATABASE[drug]
    print(f"\n📋 {drug} ({desc}):")
    
    # Kiểm tra required fields
    present_fields = [f for f in required_fields if f in drug_data]
    missing_fields = [f for f in required_fields if f not in drug_data]
    
    if len(present_fields) == len(required_fields):
        print(f"   ✅ Đầy đủ 6 fields cơ bản")
    else:
        print(f"   ⚠️  Thiếu {len(missing_fields)} fields: {', '.join(missing_fields)}")
    
    # Kiểm tra optional fields
    optional_fields = ['drug_interactions', 'contraindications', 'pregnancy_lactation',
                      'hepatic_adjustment', 'overdose_management', 'reversal_agents',
                      'administration_instructions', 'references']
    present_optional = [f for f in optional_fields if f in drug_data]
    print(f"   Optional fields: {len(present_optional)}/{len(optional_fields)}")

# Tổng kết
print("\n" + "=" * 100)
print("TỔNG KẾT")
print("=" * 100)
print(f"✅ Đã có: {len(found_drugs)}/{len(LIPID_DRUGS)} thuốc")
print(f"⚠️  Có thể trùng: {len(partial_matches)} thuốc")
print(f"❌ Chưa có: {len(missing_drugs)} thuốc")

if missing_drugs:
    print(f"\n💡 Đề xuất: Thêm {len(missing_drugs)} thuốc còn thiếu vào database")
    print("   - Niacin (Vitamin B3) - quan trọng nhưng ít dùng do tác dụng phụ")
    print("   - Volanesorsen - thuốc mới cho hội chứng Chylomicronemia gia đình")
    print("   - Olezarsen - thuốc mới cho hội chứng Chylomicronemia gia đình")

