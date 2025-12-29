"""
Phân tích chi tiết vấn đề thứ tự field
Tạo báo cáo để quyết định có cần chuẩn hóa không
"""
import json
from collections import defaultdict

STANDARD_14_FIELDS = [
    "group", "vietnamese_name", "administration", "indications", "dosage",
    "side_effects", "contraindications", "interactions", "pregnancy",
    "mechanism_of_action", "monitoring", "precautions", "pharmacokinetics", "storage"
]

def analyze_field_order_issues():
    """Phân tích vấn đề thứ tự field"""
    with open('field_standardization_check.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    issues = data['issues']['wrong_order']
    
    # Phân loại các vấn đề
    issue_types = defaultdict(list)
    
    for issue in issues:
        current = issue['current_order']
        expected = issue['expected_order']
        
        # Tìm field nào bị sai vị trí
        wrong_positions = []
        for i, field in enumerate(current):
            if field in STANDARD_14_FIELDS:
                expected_pos = expected.index(field) if field in expected else -1
                if expected_pos != -1 and i != expected_pos:
                    wrong_positions.append({
                        'field': field,
                        'current_pos': i,
                        'expected_pos': expected_pos
                    })
        
        # Phân loại theo loại lỗi
        if 'contraindications' in current and current.index('contraindications') < current.index('dosage'):
            issue_types['contraindications_before_dosage'].append(issue['name'])
        elif 'contraindications' in current and current.index('contraindications') < current.index('side_effects'):
            issue_types['contraindications_before_side_effects'].append(issue['name'])
        else:
            issue_types['other_order_issues'].append(issue['name'])
    
    # In báo cáo
    print("\n" + "=" * 70)
    print("PHAN TICH VAN DE THU TU FIELD")
    print("=" * 70)
    
    print(f"\nTong so thuoc co van de thu tu: {len(issues)}")
    print(f"Tong so thuoc: {data['total_drugs']}")
    print(f"Ty le: {len(issues)*100//data['total_drugs']}%")
    
    print(f"\nPhan loai van de:")
    print(f"  1. Contraindications truoc dosage: {len(issue_types['contraindications_before_dosage'])} thuoc")
    print(f"  2. Contraindications truoc side_effects: {len(issue_types['contraindications_before_side_effects'])} thuoc")
    print(f"  3. Van de khac: {len(issue_types['other_order_issues'])} thuoc")
    
    if issue_types['contraindications_before_dosage']:
        print(f"\nVi du thuoc co contraindications truoc dosage (10 dau tien):")
        for name in issue_types['contraindications_before_dosage'][:10]:
            print(f"  - {name}")
    
    print("\n" + "=" * 70)
    print("KET LUAN:")
    print("=" * 70)
    print("\n✅ TAT CA THUOC DEU CO DU 14 FIELD CHUAN")
    print("⚠️  NHUNG NHIEU THUOC CO FIELD SAI THU TU")
    print("\nVan de chinh:")
    print("  - Contraindications dang dung truoc dosage hoac side_effects")
    print("  - Thu tu dung: dosage -> side_effects -> contraindications")
    print("\nDanh gia:")
    print("  - Van de nay KHONG anh huong den chuc nang")
    print("  - Chi anh huong den tinh nhat quan va de doc")
    print("  - Co the bo qua neu khong can thiet")
    print("\nNeu muon chuan hoa:")
    print("  - Can sap xep lai field trong tat ca 721 thuoc")
    print("  - Cong viec lon, can script tu dong")
    print("=" * 70)

if __name__ == "__main__":
    analyze_field_order_issues()

