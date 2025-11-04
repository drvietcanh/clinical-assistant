#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script to track progress of Phase 2 (8 optional fields)
"""

from drugs.drug_database import DRUG_DATABASE

OPTIONAL_FIELDS = [
    'drug_interactions',
    'contraindications',  # Note: needs to be dict, not list
    'pregnancy_lactation',
    'hepatic_adjustment',
    'overdose_management',
    'reversal_agents',
    'administration_instructions',
    'references'
]

def check_phase2_progress():
    """Check progress of Phase 2"""
    
    total = len(DRUG_DATABASE)
    completed = []
    in_progress = []
    not_started = []
    
    for name, data in DRUG_DATABASE.items():
        # Check if has all 8 optional fields with correct format
        has_all = True
        field_count = 0
        
        for field in OPTIONAL_FIELDS:
            if field in data:
                # Special check for contraindications - must be dict
                if field == 'contraindications':
                    if isinstance(data[field], dict):
                        field_count += 1
                    else:
                        has_all = False
                else:
                    field_count += 1
            else:
                has_all = False
        
        if has_all:
            completed.append(name)
        elif field_count >= 4:
            in_progress.append(name)
        else:
            not_started.append(name)
    
    print("=" * 80)
    print("THEO DÕI TIẾN TRÌNH PHASE 2 - 8 FIELDS TÙY CHỌN")
    print("=" * 80)
    
    print(f"\n📊 TỔNG QUAN:")
    print(f"   - Tổng số thuốc: {total}")
    print(f"   - ✅ Hoàn thành: {len(completed)} ({len(completed)*100//total}%)")
    print(f"   - 🔄 Đang làm: {len(in_progress)} ({len(in_progress)*100//total}%)")
    print(f"   - ⏳ Chưa bắt đầu: {len(not_started)} ({len(not_started)*100//total}%)")
    
    if completed:
        print(f"\n✅ THUỐC ĐÃ HOÀN THÀNH ({len(completed)}):")
        for name in sorted(completed):
            print(f"   - {name}")
    
    if in_progress:
        print(f"\n🔄 THUỐC ĐANG LÀM ({len(in_progress)}):")
        for name in sorted(in_progress)[:10]:
            field_count = sum(1 for f in OPTIONAL_FIELDS if f in DRUG_DATABASE[name] and 
                            (f != 'contraindications' or isinstance(DRUG_DATABASE[name][f], dict)))
            print(f"   - {name} ({field_count}/8 fields)")
        if len(in_progress) > 10:
            print(f"   ... và {len(in_progress) - 10} thuốc khác")
    
    # Chi tiết từng field
    print(f"\n📋 CHI TIẾT TỪNG FIELD:")
    for field in OPTIONAL_FIELDS:
        count = 0
        for data in DRUG_DATABASE.values():
            if field in data:
                if field == 'contraindications':
                    if isinstance(data[field], dict):
                        count += 1
                else:
                    count += 1
        print(f"   - {field}: {count}/{total} ({count*100//total}%)")
    
    return {
        'completed': completed,
        'in_progress': in_progress,
        'not_started': not_started
    }

if __name__ == '__main__':
    check_phase2_progress()

