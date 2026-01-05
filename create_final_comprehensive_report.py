"""
Tạo báo cáo chi tiết duy nhất về tất cả các field của tất cả thuốc
Sử dụng dữ liệu từ comprehensive_field_check_report.json
"""
import json
from pathlib import Path
from datetime import datetime
from collections import defaultdict

# Đọc báo cáo đã có (tạo mới nếu chưa có)
try:
    with open('comprehensive_field_check_report.json', 'r', encoding='utf-8') as f:
        report_data = json.load(f)
except FileNotFoundError:
    print("File comprehensive_field_check_report.json chua co. Dang tao moi...")
    import subprocess
    subprocess.run(['python', 'check_all_drug_fields_comprehensive.py'], check=True)
    with open('comprehensive_field_check_report.json', 'r', encoding='utf-8') as f:
        report_data = json.load(f)

stats = report_data['statistics']
all_drugs = report_data['all_drugs']

# Tạo báo cáo markdown
md = f"""# Báo Cáo Chi Tiết Về Các Field Của Tất Cả Thuốc

**Ngày tạo:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
**Tổng số thuốc:** {stats['total_drugs']}

## Tổng Quan

### Thống Kê Field Chuẩn (14 field)

- **Thuốc có đủ 14 field chuẩn:** {stats['drugs_with_all_14_fields']} ({stats['drugs_with_all_14_fields']/stats['total_drugs']*100:.1f}%)
- **Thuốc thiếu field chuẩn:** {stats['total_drugs'] - stats['drugs_with_all_14_fields']} ({(stats['total_drugs'] - stats['drugs_with_all_14_fields'])/stats['total_drugs']*100:.1f}%)

### Thống Kê Field Bổ Sung (8 field)

- **Thuốc có đủ 22 field (14 + 8):** {stats['drugs_with_all_22_fields']} ({stats['drugs_with_all_22_fields']/stats['total_drugs']*100:.1f}%)
- **Thuốc thiếu field bổ sung:** {stats['total_drugs'] - stats['drugs_with_all_22_fields']} ({(stats['total_drugs'] - stats['drugs_with_all_22_fields'])/stats['total_drugs']*100:.1f}%)

## Thống Kê Theo Field

### 14 Field Chuẩn

"""
STANDARD_14_FIELDS = [
    "group", "vietnamese_name", "administration", "indications", "dosage",
    "side_effects", "contraindications", "interactions", "pregnancy",
    "mechanism_of_action", "monitoring", "precautions", "pharmacokinetics", "storage"
]

ADDITIONAL_8_FIELDS = [
    "black_box_warnings", "drug_interactions", "pregnancy_lactation",
    "hepatic_adjustment", "overdose_management", "reversal_agents",
    "administration_instructions", "references"
]

# Field chuẩn
for field in STANDARD_14_FIELDS:
    present = stats['field_statistics'].get(field, 0)
    missing = stats['missing_field_statistics'].get(field, 0)
    empty = stats['empty_field_statistics'].get(field, 0)
    present_rate = present / stats['total_drugs'] * 100
    
    md += f"- **`{field}`**: {present} có ({present_rate:.1f}%), {missing} thiếu, {empty} rỗng\n"

md += "\n### 8 Field Bổ Sung\n\n"

# Field bổ sung
for field in ADDITIONAL_8_FIELDS:
    present = stats['field_statistics'].get(field, 0)
    missing = stats['missing_field_statistics'].get(field, 0)
    empty = stats['empty_field_statistics'].get(field, 0)
    present_rate = present / stats['total_drugs'] * 100
    
    md += f"- **`{field}`**: {present} có ({present_rate:.1f}%), {missing} thiếu, {empty} rỗng\n"

# Tìm thuốc thiếu nhiều field nhất
drugs_missing = []
for drug_name, drug_info in all_drugs.items():
    missing_standard = drug_info.get('missing_standard_fields', [])
    missing_additional = drug_info.get('missing_additional_fields', [])
    total_missing = len(missing_standard) + len(missing_additional)
    
    if total_missing > 0:
        # Lấy thông tin từ field_details hoặc DRUG_DATABASE
        from drugs.drug_database import DRUG_DATABASE
        drug_data = DRUG_DATABASE.get(drug_name, {})
        
        # Lấy từ field_details nếu có
        field_details = drug_info.get('field_details', {})
        vietnamese_name = ''
        group = ''
        
        if 'vietnamese_name' in field_details and field_details['vietnamese_name'].get('exists'):
            # Cần parse từ AST, nhưng tạm thời dùng từ DRUG_DATABASE
            vietnamese_name = drug_data.get('vietnamese_name', '')
        else:
            vietnamese_name = drug_data.get('vietnamese_name', '')
        
        if 'group' in field_details and field_details['group'].get('exists'):
            group = drug_data.get('group', '')
        else:
            group = drug_data.get('group', '')
        
        drugs_missing.append({
            'name': drug_name,
            'file': drug_info.get('file', ''),
            'vietnamese_name': vietnamese_name,
            'group': group,
            'missing_standard': missing_standard,
            'missing_additional': missing_additional,
            'total_missing': total_missing,
            'field_count': drug_info.get('field_count', 0),
        })

drugs_missing.sort(key=lambda x: x['total_missing'], reverse=True)

md += f"""
## Chi Tiết Từng Thuốc

### Thuốc Thiếu Nhiều Field Nhất (Top 100)

"""
for i, drug in enumerate(drugs_missing[:100], 1):
    md += f"""
#### {i}. {drug['name']}

- **Tên tiếng Việt:** {drug['vietnamese_name']}
- **Nhóm:** {drug['group']}
- **File:** `{drug['file']}`
- **Tổng số field:** {drug['field_count']}
- **Tổng field thiếu:** {drug['total_missing']}
"""
    if drug['missing_standard']:
        md += f"- **Thiếu field chuẩn ({len(drug['missing_standard'])}):** {', '.join(drug['missing_standard'])}\n"
    if drug['missing_additional']:
        md += f"- **Thiếu field bổ sung ({len(drug['missing_additional'])}):** {', '.join(drug['missing_additional'])}\n"

# Thống kê theo module
md += f"""
## Thống Kê Theo Module

"""
module_stats = defaultdict(lambda: {'total': 0, 'all_14': 0, 'all_22': 0})
for drug_name, drug_info in all_drugs.items():
    file_path = drug_info.get('file', '')
    if file_path:
        # Extract module from path
        parts = Path(file_path).parts
        if len(parts) >= 3:
            module = parts[2]  # drugs/drug_modules/MODULE
        else:
            module = 'unknown'
    else:
        module = 'unknown'
    
    module_stats[module]['total'] += 1
    if len(drug_info.get('missing_standard_fields', [])) == 0:
        module_stats[module]['all_14'] += 1
    if len(drug_info.get('missing_standard_fields', [])) == 0 and len(drug_info.get('missing_additional_fields', [])) == 0:
        module_stats[module]['all_22'] += 1

for module, mstats in sorted(module_stats.items(), key=lambda x: x[1]['total'], reverse=True):
    md += f"- **{module}**: {mstats['total']} thuốc, {mstats['all_14']} có đủ 14 field ({mstats['all_14']/mstats['total']*100:.1f}%), {mstats['all_22']} có đủ 22 field ({mstats['all_22']/mstats['total']*100:.1f}%)\n"

md += f"""
## Tổng Kết

- **Tổng số thuốc:** {stats['total_drugs']}
- **Thuốc có đủ 14 field chuẩn:** {stats['drugs_with_all_14_fields']} ({stats['drugs_with_all_14_fields']/stats['total_drugs']*100:.1f}%)
- **Thuốc có đủ 22 field:** {stats['drugs_with_all_22_fields']} ({stats['drugs_with_all_22_fields']/stats['total_drugs']*100:.1f}%)
- **Thuốc thiếu field chuẩn:** {stats['total_drugs'] - stats['drugs_with_all_14_fields']} ({(stats['total_drugs'] - stats['drugs_with_all_14_fields'])/stats['total_drugs']*100:.1f}%)
- **Thuốc thiếu field bổ sung:** {stats['total_drugs'] - stats['drugs_with_all_22_fields']} ({(stats['total_drugs'] - stats['drugs_with_all_22_fields'])/stats['total_drugs']*100:.1f}%)

## Lưu Ý

Báo cáo này được tạo tự động từ dữ liệu hiện tại trong hệ thống.
Để cập nhật báo cáo, chạy lại script `check_all_drug_fields_comprehensive.py` và sau đó chạy `create_final_comprehensive_report.py`.
"""

# Lưu báo cáo
with open('DRUG_FIELDS_REPORT.md', 'w', encoding='utf-8') as f:
    f.write(md)

# Lưu JSON (sử dụng dữ liệu từ comprehensive_field_check_report.json)
with open('DRUG_FIELDS_REPORT.json', 'w', encoding='utf-8') as f:
    json.dump({
        'statistics': stats,
        'drugs': all_drugs,
        'generated_at': datetime.now().isoformat()
    }, f, indent=2, ensure_ascii=False)

print("="*60)
print("DA TAO BAO CAO CHI TIET")
print("="*60)
print(f"Tong so thuoc: {stats['total_drugs']}")
print(f"Co du 14 field chuan: {stats['drugs_with_all_14_fields']} ({stats['drugs_with_all_14_fields']/stats['total_drugs']*100:.1f}%)")
print(f"Co du 22 field: {stats['drugs_with_all_22_fields']} ({stats['drugs_with_all_22_fields']/stats['total_drugs']*100:.1f}%)")
print(f"\nDa luu:")
print(f"  - DRUG_FIELDS_REPORT.md")
print(f"  - DRUG_FIELDS_REPORT.json")
print("="*60)

