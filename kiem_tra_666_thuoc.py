"""
Script kiểm tra và đếm tất cả 666 thuốc trong database
"""
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

# Import drug_database
try:
    from drugs.drug_database import DRUG_DATABASE, TOTAL_DRUGS
    print("=" * 70)
    print("KIEM TRA SO LUONG THUOC TRONG DRUG_DATABASE")
    print("=" * 70)
    print()
    print(f"TOTAL_DRUGS (từ drug_database.py): {TOTAL_DRUGS}")
    print(f"DRUG_DATABASE length: {len(DRUG_DATABASE)}")
    print()
    
    if TOTAL_DRUGS == 666:
        print("✅ ĐÚNG! Có đúng 666 thuốc!")
    else:
        print(f"⚠️ CHƯA ĐÚNG! Có {TOTAL_DRUGS} thuốc, cần 666 thuốc")
        print(f"   Thiếu: {666 - TOTAL_DRUGS} thuốc")
    
    print()
    print("=" * 70)
    print("PHAN TICH THEO MODULE")
    print("=" * 70)
    print()
    
    # Import từng module để đếm
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
        CARDIOVASCULAR_OTHER_DRUGS,
        INFECTIOUS_OTHER_DRUGS,
        PSYCHIATRY_OTHER_DRUGS,
        ENDOCRINOLOGY_OTHER_DRUGS,
        MISCELLANEOUS_DRUGS,
    )
    
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
        "CARDIOVASCULAR_OTHER_DRUGS": CARDIOVASCULAR_OTHER_DRUGS,
        "INFECTIOUS_OTHER_DRUGS": INFECTIOUS_OTHER_DRUGS,
        "PSYCHIATRY_OTHER_DRUGS": PSYCHIATRY_OTHER_DRUGS,
        "ENDOCRINOLOGY_OTHER_DRUGS": ENDOCRINOLOGY_OTHER_DRUGS,
        "MISCELLANEOUS_DRUGS": MISCELLANEOUS_DRUGS,
    }
    
    total_count = 0
    for name, drugs in sorted(modules.items(), key=lambda x: len(x[1]), reverse=True):
        count = len(drugs)
        total_count += count
        print(f"{name:35s}: {count:3d} thuoc")
    
    print("-" * 70)
    print(f"{'TONG CONG':35s}: {total_count:3d} thuoc")
    print("=" * 70)
    
    # Kiểm tra duplicate
    all_drug_names = []
    for drugs in modules.values():
        all_drug_names.extend(drugs.keys())
    
    duplicates = []
    seen = set()
    for name in all_drug_names:
        if name in seen:
            duplicates.append(name)
        seen.add(name)
    
    if duplicates:
        print()
        print(f"⚠️ PHAT HIEN {len(duplicates)} THUOC TRUNG LAP:")
        for dup in duplicates[:10]:
            print(f"  - {dup}")
        if len(duplicates) > 10:
            print(f"  ... và {len(duplicates) - 10} thuốc khác")
    else:
        print()
        print("✅ Không có thuốc trùng lặp!")
    
except Exception as e:
    print(f"Lỗi: {e}")
    import traceback
    traceback.print_exc()

