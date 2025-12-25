#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script để kiểm tra danh sách thuốc cần thêm và so sánh với database hiện tại
"""

from drugs.drug_database import DRUG_DATABASE

# Danh sách thuốc đề xuất thêm (từ kế hoạch)
PROPOSED_DRUGS = {
    # Phase 1: ICU/Cấp Cứu (Ưu tiên cao nhất)
    "Phase 1 - ICU/Cấp Cứu": [
        "Phenylephrine",
        "Milrinone",
        "Succinylcholine",
        "Rocuronium",
        "Vecuronium",
        "Cisatracurium",
        "Fosphenytoin",
        "Thiopental",
    ],
    
    # Phase 2: Kháng Sinh Bổ Sung
    "Phase 2 - Kháng Sinh": [
        "Aztreonam",
        "Teicoplanin",
        "Polymyxin B",
        "Fosfomycin",
        "Nitrofurantoin",
        "Fidaxomicin",
        "Doripenem",
    ],
    
    # Phase 3: Tim Mạch Bổ Sung
    "Phase 3 - Tim Mạch": [
        "Sotalol",
        "Dofetilide",
        "Nesiritide",
        "Nitroprusside",
        "Clevidipine",
    ],
    
    # Phase 4: Chuyên Khoa
    "Phase 4 - Obstetrics/Gynecology": [
        "Methylergonovine",
        "Carboprost",
        "Dinoprostone",
    ],
    "Phase 4 - Dermatology": [
        "Hydrocortisone topical",
        "Clobetasol",
        "Tacrolimus topical",
        "Pimecrolimus",
    ],
    "Phase 4 - Ophthalmology": [
        "Timolol eye drops",
        "Latanoprost",
        "Brinzolamide",
    ],
    "Phase 4 - Urology": [
        "Tamsulosin",
        "Finasteride",
        "Sildenafil",
        "Tadalafil",
    ],
    
    # Phase 5: Thuốc Mới
    "Phase 5 - Thuốc Mới": [
        "Dostarlimab",
    ],
}

def check_drugs_status():
    """Kiểm tra trạng thái các thuốc đề xuất"""
    
    print("=" * 100)
    print("KIỂM TRA DANH SÁCH THUỐC ĐỀ XUẤT THÊM")
    print("=" * 100)
    print(f"\nTổng số thuốc trong database hiện tại: {len(DRUG_DATABASE)}")
    print()
    
    all_proposed = []
    drugs_already_exist = []
    drugs_to_add = []
    
    for phase, drugs in PROPOSED_DRUGS.items():
        all_proposed.extend(drugs)
    
    print("=" * 100)
    print("PHÂN TÍCH THEO TỪNG PHASE")
    print("=" * 100)
    
    for phase, drugs in PROPOSED_DRUGS.items():
        print(f"\n📋 {phase}:")
        print(f"   Tổng số thuốc đề xuất: {len(drugs)}")
        
        existing = []
        missing = []
        
        for drug in drugs:
            # Kiểm tra exact match
            if drug in DRUG_DATABASE:
                existing.append(drug)
                drugs_already_exist.append(drug)
            else:
                # Kiểm tra partial match (case-insensitive)
                found = False
                for db_drug in DRUG_DATABASE.keys():
                    if drug.lower() in db_drug.lower() or db_drug.lower() in drug.lower():
                        existing.append(f"{drug} (có thể là: {db_drug})")
                        found = True
                        break
                
                if not found:
                    missing.append(drug)
                    drugs_to_add.append(drug)
        
        if existing:
            print(f"   ✅ Đã có ({len(existing)}):")
            for drug in existing:
                print(f"      - {drug}")
        
        if missing:
            print(f"   ❌ Chưa có ({len(missing)}):")
            for drug in missing:
                print(f"      - {drug}")
    
    print("\n" + "=" * 100)
    print("TỔNG KẾT")
    print("=" * 100)
    print(f"\nTổng số thuốc đề xuất: {len(all_proposed)}")
    print(f"Thuốc đã có trong database: {len(drugs_already_exist)}")
    print(f"Thuốc cần thêm: {len(drugs_to_add)}")
    
    if drugs_to_add:
        print(f"\n📝 DANH SÁCH THUỐC CẦN THÊM ({len(drugs_to_add)} thuốc):")
        for i, drug in enumerate(sorted(drugs_to_add), 1):
            print(f"   {i:>3}. {drug}")
    
    # Thống kê theo ưu tiên
    print("\n" + "=" * 100)
    print("THỐNG KÊ THEO ĐỘ ƯU TIÊN")
    print("=" * 100)
    
    priority_stats = {
        "Phase 1 - ICU/Cấp Cứu": {"total": 0, "missing": 0},
        "Phase 2 - Kháng Sinh": {"total": 0, "missing": 0},
        "Phase 3 - Tim Mạch": {"total": 0, "missing": 0},
        "Phase 4": {"total": 0, "missing": 0},
        "Phase 5 - Thuốc Mới": {"total": 0, "missing": 0},
    }
    
    for phase, drugs in PROPOSED_DRUGS.items():
        if "Phase 1" in phase:
            key = "Phase 1 - ICU/Cấp Cứu"
        elif "Phase 2" in phase:
            key = "Phase 2 - Kháng Sinh"
        elif "Phase 3" in phase:
            key = "Phase 3 - Tim Mạch"
        elif "Phase 4" in phase:
            key = "Phase 4"
        elif "Phase 5" in phase:
            key = "Phase 5 - Thuốc Mới"
        else:
            continue
        
        priority_stats[key]["total"] += len(drugs)
        for drug in drugs:
            if drug not in DRUG_DATABASE:
                priority_stats[key]["missing"] += 1
    
    for phase, stats in priority_stats.items():
        if stats["total"] > 0:
            percentage = (stats["missing"] / stats["total"]) * 100
            print(f"\n{phase}:")
            print(f"   Tổng: {stats['total']} thuốc")
            print(f"   Cần thêm: {stats['missing']} thuốc ({percentage:.1f}%)")
    
    return {
        "total_proposed": len(all_proposed),
        "already_exist": len(drugs_already_exist),
        "to_add": len(drugs_to_add),
        "drugs_to_add_list": sorted(drugs_to_add),
        "priority_stats": priority_stats
    }

if __name__ == "__main__":
    try:
        results = check_drugs_status()
        
        print("\n" + "=" * 100)
        print("KẾT THÚC KIỂM TRA")
        print("=" * 100)
        print(f"\n💡 Gợi ý: Bắt đầu với Phase 1 (ICU/Cấp Cứu) - {results['priority_stats']['Phase 1 - ICU/Cấp Cứu']['missing']} thuốc cần thêm")
        print(f"   Xem kế hoạch chi tiết tại: docs/DRUG_ADDITION_PLAN.md")
        
    except Exception as e:
        print(f"❌ Lỗi: {e}")
        import traceback
        traceback.print_exc()

