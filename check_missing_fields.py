"""
Kiểm tra toàn bộ các thuốc xem có thiếu field nào không
"""
import sys
from pathlib import Path
from collections import defaultdict
from typing import Dict, List, Set

# Thêm path để import
sys.path.insert(0, str(Path.cwd()))

try:
    from drugs.drug_database import DRUG_DATABASE
except ImportError as e:
    print(f"Loi import DRUG_DATABASE: {e}")
    print("Dang thu load truc tiep...")
    # Thử load trực tiếp
    import importlib.util
    spec = importlib.util.spec_from_file_location("drug_database", Path("drugs/drug_database.py"))
    drug_db_module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(drug_db_module)
    DRUG_DATABASE = drug_db_module.DRUG_DATABASE

# Định nghĩa các field
CORE_FIELDS = [
    "group",
    "vietnamese_name", 
    "administration",
    "indications",
    "dosage"
]

EXTENDED_FIELDS = [
    "side_effects",
    "contraindications",
    "interactions",
    "pregnancy"
]

ENHANCED_FIELDS = [
    "mechanism_of_action",
    "monitoring",
    "precautions",
    "pharmacokinetics",
    "storage",
    "black_box_warnings",
    "drug_interactions",
    "contraindications",  # Note: có thể là dict hoặc list
    "pregnancy_lactation",
    "hepatic_adjustment",
    "overdose_management",
    "reversal_agents",
    "administration_instructions",
    "references"
]

# Meta fields (tùy chọn nhưng nên có)
META_FIELDS = [
    "risk_flags",
    "guideline_tags",
    "availability_vietnam"
]

def check_drug_fields(drug_name: str, drug_data: Dict) -> Dict:
    """Kiểm tra fields của một thuốc"""
    result = {
        'drug_name': drug_name,
        'missing_core': [],
        'missing_extended': [],
        'missing_enhanced': [],
        'missing_meta': [],
        'empty_fields': [],
        'total_missing': 0
    }
    
    # Kiểm tra core fields
    for field in CORE_FIELDS:
        if field not in drug_data:
            result['missing_core'].append(field)
            result['total_missing'] += 1
        elif not drug_data[field] or drug_data[field] == "":
            result['empty_fields'].append(field)
            result['total_missing'] += 1
    
    # Kiểm tra extended fields
    for field in EXTENDED_FIELDS:
        if field not in drug_data:
            result['missing_extended'].append(field)
        elif not drug_data[field] or drug_data[field] == "":
            result['empty_fields'].append(field)
    
    # Kiểm tra enhanced fields
    for field in ENHANCED_FIELDS:
        if field not in drug_data:
            result['missing_enhanced'].append(field)
        elif drug_data[field] is None:
            result['missing_enhanced'].append(field)  # None được coi là thiếu
        elif isinstance(drug_data[field], (str, list, dict)) and not drug_data[field]:
            result['empty_fields'].append(field)
    
    # Kiểm tra meta fields
    for field in META_FIELDS:
        if field not in drug_data:
            result['missing_meta'].append(field)
    
    return result

def main():
    """Main function"""
    print("\n" + "=" * 70)
    print("KIEM TRA THIEU FIELD TRONG TOAN BO THUOC")
    print("=" * 70)
    print()
    
    if not DRUG_DATABASE:
        print("[LOI] Khong the load DRUG_DATABASE")
        return
    
    total_drugs = len(DRUG_DATABASE)
    print(f"Tong so thuoc: {total_drugs}")
    print()
    
    # Kiểm tra từng thuốc
    all_results = []
    drugs_with_missing_core = []
    drugs_with_missing_extended = []
    drugs_with_missing_enhanced = []
    drugs_with_empty_fields = []
    
    field_missing_count = defaultdict(int)
    
    for drug_name, drug_data in DRUG_DATABASE.items():
        result = check_drug_fields(drug_name, drug_data)
        all_results.append(result)
        
        if result['missing_core']:
            drugs_with_missing_core.append(result)
            for field in result['missing_core']:
                field_missing_count[f"core_{field}"] += 1
        
        if result['missing_extended']:
            drugs_with_missing_extended.append(result)
            for field in result['missing_extended']:
                field_missing_count[f"extended_{field}"] += 1
        
        if result['missing_enhanced']:
            drugs_with_missing_enhanced.append(result)
            for field in result['missing_enhanced']:
                field_missing_count[f"enhanced_{field}"] += 1
        
        if result['empty_fields']:
            drugs_with_empty_fields.append(result)
    
    # Báo cáo
    print("=" * 70)
    print("1. THIEU CORE FIELDS (Nghiem trong)")
    print("=" * 70)
    
    if drugs_with_missing_core:
        print(f"\n[LOI] Tim thay {len(drugs_with_missing_core)} thuoc thieu core fields:")
        print()
        
        # Nhóm theo field
        by_field = defaultdict(list)
        for result in drugs_with_missing_core:
            for field in result['missing_core']:
                by_field[field].append(result['drug_name'])
        
        for field in CORE_FIELDS:
            if field in by_field:
                count = len(by_field[field])
                print(f"  - {field}: {count} thuoc thieu")
                if count <= 10:
                    for drug in by_field[field]:
                        print(f"    + {drug}")
                else:
                    for drug in by_field[field][:5]:
                        print(f"    + {drug}")
                    print(f"    ... va {count - 5} thuoc khac")
    else:
        print("\n[OK] Tat ca thuoc deu co day du core fields")
    
    print("\n" + "=" * 70)
    print("2. THIEU EXTENDED FIELDS")
    print("=" * 70)
    
    if drugs_with_missing_extended:
        print(f"\n[WARNING] Tim thay {len(drugs_with_missing_extended)} thuoc thieu extended fields:")
        print()
        
        by_field = defaultdict(list)
        for result in drugs_with_missing_extended:
            for field in result['missing_extended']:
                by_field[field].append(result['drug_name'])
        
        for field in EXTENDED_FIELDS:
            if field in by_field:
                count = len(by_field[field])
                print(f"  - {field}: {count} thuoc thieu ({count*100//total_drugs}%)")
    else:
        print("\n[OK] Tat ca thuoc deu co day du extended fields")
    
    print("\n" + "=" * 70)
    print("3. THIEU ENHANCED FIELDS (14 fields)")
    print("=" * 70)
    
    if drugs_with_missing_enhanced:
        print(f"\n[INFO] Tim thay {len(drugs_with_missing_enhanced)} thuoc thieu enhanced fields:")
        print()
        
        by_field = defaultdict(list)
        for result in drugs_with_missing_enhanced:
            for field in result['missing_enhanced']:
                by_field[field].append(result['drug_name'])
        
        # Sắp xếp theo số lượng thiếu
        sorted_fields = sorted(by_field.items(), key=lambda x: len(x[1]), reverse=True)
        
        print("Top 10 enhanced fields bi thieu nhieu nhat:")
        for field, drugs in sorted_fields[:10]:
            count = len(drugs)
            print(f"  - {field}: {count} thuoc thieu ({count*100//total_drugs}%)")
    else:
        print("\n[OK] Tat ca thuoc deu co day du enhanced fields")
    
    print("\n" + "=" * 70)
    print("4. FIELD RONG (co field nhung gia tri rong)")
    print("=" * 70)
    
    if drugs_with_empty_fields:
        print(f"\n[WARNING] Tim thay {len(drugs_with_empty_fields)} thuoc co field rong:")
        
        by_field = defaultdict(int)
        for result in drugs_with_empty_fields:
            for field in result['empty_fields']:
                by_field[field] += 1
        
        sorted_fields = sorted(by_field.items(), key=lambda x: x[1], reverse=True)
        for field, count in sorted_fields[:10]:
            print(f"  - {field}: {count} thuoc co gia tri rong")
    else:
        print("\n[OK] Khong co field rong nao")
    
    # Thống kê tổng hợp
    print("\n" + "=" * 70)
    print("TOM TAT")
    print("=" * 70)
    
    total_missing_core = sum(len(r['missing_core']) for r in all_results)
    total_missing_extended = sum(len(r['missing_extended']) for r in all_results)
    total_missing_enhanced = sum(len(r['missing_enhanced']) for r in all_results)
    
    print(f"\nTong so thuoc: {total_drugs}")
    print(f"\nThieu core fields:")
    print(f"  - So thuoc thieu: {len(drugs_with_missing_core)} ({len(drugs_with_missing_core)*100//total_drugs}%)")
    print(f"  - Tong so field thieu: {total_missing_core}")
    
    print(f"\nThieu extended fields:")
    print(f"  - So thuoc thieu: {len(drugs_with_missing_extended)} ({len(drugs_with_missing_extended)*100//total_drugs}%)")
    print(f"  - Tong so field thieu: {total_missing_extended}")
    
    print(f"\nThieu enhanced fields:")
    print(f"  - So thuoc thieu: {len(drugs_with_missing_enhanced)} ({len(drugs_with_missing_enhanced)*100//total_drugs}%)")
    print(f"  - Tong so field thieu: {total_missing_enhanced}")
    
    # Top 10 thuốc thiếu nhiều field nhất
    print("\n" + "=" * 70)
    print("TOP 10 THUOC THIEU NHIEU FIELD NHAT")
    print("=" * 70)
    
    sorted_drugs = sorted(all_results, key=lambda x: x['total_missing'], reverse=True)
    for i, result in enumerate(sorted_drugs[:10], 1):
        missing = result['missing_core'] + result['missing_extended'] + result['missing_enhanced']
        if missing:
            print(f"\n{i}. {result['drug_name']}: Thieu {len(missing)} fields")
            if result['missing_core']:
                print(f"   Core: {', '.join(result['missing_core'])}")
            if result['missing_extended']:
                print(f"   Extended: {', '.join(result['missing_extended'][:3])}")
            if result['missing_enhanced']:
                print(f"   Enhanced: {len(result['missing_enhanced'])} fields")
    
    print("\n" + "=" * 70)

if __name__ == "__main__":
    main()

