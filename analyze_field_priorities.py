"""
Script phân tích và ưu tiên các thuốc cần bổ sung field
Giúp lập kế hoạch bổ sung field một cách hiệu quả
"""
import sys
from pathlib import Path
from collections import defaultdict
from typing import Dict, List, Tuple

# Import từ check_missing_fields_final
sys.path.insert(0, str(Path.cwd()))
from check_missing_fields_final import load_all_drugs, check_drug_fields, ENHANCED_FIELDS

def analyze_drugs_by_priority() -> Dict[str, List[Tuple[str, int, List[str]]]]:
    """Phân tích và nhóm các thuốc theo mức độ ưu tiên"""
    print("\n" + "=" * 70)
    print("PHAN TICH VA UU TIEN CAC THUOC CAN BO SUNG FIELD")
    print("=" * 70)
    print()
    
    print("Dang doc cac file module...")
    all_drugs = load_all_drugs()
    print(f"Tim thay {len(all_drugs)} thuoc")
    print()
    
    # Phân loại thuốc
    drugs_by_priority = {
        'few_fields': [],      # Thiếu ít field (1-3) - ưu tiên cao
        'medium_fields': [],   # Thiếu vừa (4-7) - ưu tiên trung bình
        'many_fields': [],     # Thiếu nhiều (8-13) - ưu tiên thấp
        'not_drugs': []        # Không phải thuốc (field names)
    }
    
    for drug_name, fields in all_drugs.items():
        # Lọc bỏ các field names (không phải thuốc)
        if 'group' not in fields and 'vietnamese_name' not in fields:
            drugs_by_priority['not_drugs'].append(drug_name)
            continue
        
        # Lọc bỏ các field names (thường là lowercase với nhiều dấu gạch dưới)
        is_field_name = (
            drug_name.islower() and 
            '_' in drug_name and 
            drug_name.count('_') >= 2 and
            drug_name not in ['iv', 'po', 'im', 'sc']
        )
        
        if is_field_name:
            drugs_by_priority['not_drugs'].append(drug_name)
            continue
        
        # Kiểm tra fields
        result = check_drug_fields(drug_name, fields)
        missing_enhanced = result['missing_enhanced']
        
        if not missing_enhanced:
            continue  # Đã đủ field, bỏ qua
        
        missing_count = len(missing_enhanced)
        
        # Phân loại theo số lượng field thiếu
        if missing_count <= 3:
            drugs_by_priority['few_fields'].append((drug_name, missing_count, missing_enhanced))
        elif missing_count <= 7:
            drugs_by_priority['medium_fields'].append((drug_name, missing_count, missing_enhanced))
        else:
            drugs_by_priority['many_fields'].append((drug_name, missing_count, missing_enhanced))
    
    # Sắp xếp theo số lượng field thiếu (tăng dần)
    for key in ['few_fields', 'medium_fields', 'many_fields']:
        drugs_by_priority[key].sort(key=lambda x: x[1])
    
    return drugs_by_priority

def print_analysis_report(drugs_by_priority: Dict[str, List]):
    """In báo cáo phân tích"""
    print("=" * 70)
    print("BAO CAO PHAN TICH")
    print("=" * 70)
    print()
    
    # Thống kê tổng quan
    total_real_drugs = (
        len(drugs_by_priority['few_fields']) +
        len(drugs_by_priority['medium_fields']) +
        len(drugs_by_priority['many_fields'])
    )
    
    print(f"Tong so thuoc can bo sung field: {total_real_drugs}")
    print(f"  - Uu tien cao (thieu 1-3 fields): {len(drugs_by_priority['few_fields'])} thuoc")
    print(f"  - Uu tien trung binh (thieu 4-7 fields): {len(drugs_by_priority['medium_fields'])} thuoc")
    print(f"  - Uu tien thap (thieu 8-13 fields): {len(drugs_by_priority['many_fields'])} thuoc")
    print(f"  - Khong phai thuoc (bo qua): {len(drugs_by_priority['not_drugs'])} entries")
    print()
    
    # Chi tiết từng nhóm
    print("=" * 70)
    print("1. UU TIEN CAO - Thieu it field (1-3 fields)")
    print("=" * 70)
    if drugs_by_priority['few_fields']:
        print(f"\nCo {len(drugs_by_priority['few_fields'])} thuoc:")
        for i, (drug_name, count, fields) in enumerate(drugs_by_priority['few_fields'][:20], 1):
            print(f"  {i}. {drug_name}: thieu {count} fields ({', '.join(fields[:3])}{'...' if len(fields) > 3 else ''})")
        if len(drugs_by_priority['few_fields']) > 20:
            print(f"  ... va {len(drugs_by_priority['few_fields']) - 20} thuoc khac")
    else:
        print("\n[OK] Khong co thuoc nao trong nhom nay")
    
    print("\n" + "=" * 70)
    print("2. UU TIEN TRUNG BINH - Thieu vua (4-7 fields)")
    print("=" * 70)
    if drugs_by_priority['medium_fields']:
        print(f"\nCo {len(drugs_by_priority['medium_fields'])} thuoc:")
        for i, (drug_name, count, fields) in enumerate(drugs_by_priority['medium_fields'][:15], 1):
            print(f"  {i}. {drug_name}: thieu {count} fields")
        if len(drugs_by_priority['medium_fields']) > 15:
            print(f"  ... va {len(drugs_by_priority['medium_fields']) - 15} thuoc khac")
    else:
        print("\n[OK] Khong co thuoc nao trong nhom nay")
    
    print("\n" + "=" * 70)
    print("3. UU TIEN THAP - Thieu nhieu field (8-13 fields)")
    print("=" * 70)
    if drugs_by_priority['many_fields']:
        print(f"\nCo {len(drugs_by_priority['many_fields'])} thuoc:")
        for i, (drug_name, count, fields) in enumerate(drugs_by_priority['many_fields'][:10], 1):
            print(f"  {i}. {drug_name}: thieu {count} fields")
        if len(drugs_by_priority['many_fields']) > 10:
            print(f"  ... va {len(drugs_by_priority['many_fields']) - 10} thuoc khac")
    else:
        print("\n[OK] Khong co thuoc nao trong nhom nay")
    
    # Phân tích theo field
    print("\n" + "=" * 70)
    print("4. PHAN TICH THEO FIELD")
    print("=" * 70)
    
    field_stats = defaultdict(int)
    all_drugs_list = (
        drugs_by_priority['few_fields'] +
        drugs_by_priority['medium_fields'] +
        drugs_by_priority['many_fields']
    )
    
    for _, _, missing_fields in all_drugs_list:
        for field in missing_fields:
            field_stats[field] += 1
    
    print("\nSo luong thuoc thieu tung field:")
    sorted_fields = sorted(field_stats.items(), key=lambda x: x[1], reverse=True)
    for field, count in sorted_fields:
        print(f"  - {field}: {count} thuoc")

def create_batch_plan(drugs_by_priority: Dict[str, List], batch_size: int = 40):
    """Tạo kế hoạch chia batch"""
    print("\n" + "=" * 70)
    print("KE HOACH CHIA BATCH")
    print("=" * 70)
    print()
    
    # Lấy tất cả thuốc thực sự (không phải field names)
    all_real_drugs = (
        drugs_by_priority['few_fields'] +
        drugs_by_priority['medium_fields'] +
        drugs_by_priority['many_fields']
    )
    
    total = len(all_real_drugs)
    num_batches = (total + batch_size - 1) // batch_size
    
    print(f"Tong so thuoc: {total}")
    print(f"Kich thuoc batch: {batch_size}")
    print(f"So batch: {num_batches}")
    print()
    
    for i in range(num_batches):
        start = i * batch_size
        end = min(start + batch_size, total)
        batch_drugs = all_real_drugs[start:end]
        
        # Tính tổng số field cần bổ sung trong batch này
        total_fields = sum(count for _, count, _ in batch_drugs)
        
        print(f"Batch {i+1}: {len(batch_drugs)} thuoc (field {start+1}-{end})")
        print(f"  - Tong so field can bo sung: {total_fields}")
        print(f"  - Thuoc dau tien: {batch_drugs[0][0]}")
        print(f"  - Thuoc cuoi cung: {batch_drugs[-1][0]}")
        print()

def main():
    """Main function"""
    # Phân tích
    drugs_by_priority = analyze_drugs_by_priority()
    
    # In báo cáo
    print_analysis_report(drugs_by_priority)
    
    # Tạo kế hoạch batch
    create_batch_plan(drugs_by_priority, batch_size=40)
    
    # Gợi ý
    print("=" * 70)
    print("GOI Y")
    print("=" * 70)
    print()
    print("1. Bat dau voi nhom UU TIEN CAO (thieu it field)")
    print("   - De xu ly, nhanh chong")
    print("   - Tang tien do nhanh")
    print()
    print("2. Sau do xu ly nhom UU TIEN TRUNG BINH")
    print("   - Can thoi gian vua phai")
    print()
    print("3. Cuoi cung xu ly nhom UU TIEN THAP (thieu nhieu field)")
    print("   - Can kiem tra ky luong")
    print()
    print("4. De thuc thi, chay:")
    print("   python add_missing_fields_simple.py --execute")
    print()
    print("=" * 70)

if __name__ == "__main__":
    main()

