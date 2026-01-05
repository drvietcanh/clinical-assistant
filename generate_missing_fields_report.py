"""
Tạo báo cáo chi tiết về thuốc cần thêm field
Tập trung vào field chuẩn (quan trọng hơn)
"""
import json
from pathlib import Path
from collections import defaultdict

# Đọc báo cáo đã có
with open('comprehensive_field_check_report.json', 'r', encoding='utf-8') as f:
    report = json.load(f)

# Phân loại thuốc theo số field thiếu
drugs_missing_standard = []
drugs_missing_additional_only = []

for drug_name, drug_info in report['all_drugs'].items():
    missing_standard = drug_info.get('missing_standard_fields', [])
    missing_additional = drug_info.get('missing_additional_fields', [])
    
    if missing_standard:
        drugs_missing_standard.append({
            'name': drug_name,
            'file': drug_info['file'],
            'missing_standard': missing_standard,
            'missing_additional': missing_additional,
            'missing_count': len(missing_standard) + len(missing_additional),
        })
    elif missing_additional:
        drugs_missing_additional_only.append({
            'name': drug_name,
            'file': drug_info['file'],
            'missing_additional': missing_additional,
        })

# Sắp xếp theo số field thiếu
drugs_missing_standard.sort(key=lambda x: x['missing_count'], reverse=True)

# Tạo báo cáo
output = {
    'summary': {
        'total_drugs': len(report['all_drugs']),
        'drugs_missing_standard_fields': len(drugs_missing_standard),
        'drugs_missing_additional_only': len(drugs_missing_additional_only),
    },
    'drugs_missing_standard_fields': drugs_missing_standard,
    'drugs_missing_additional_only': drugs_missing_additional_only[:50],  # Top 50
}

# Lưu JSON
with open('drugs_need_fields_report.json', 'w', encoding='utf-8') as f:
    json.dump(output, f, indent=2, ensure_ascii=False)

# Tạo markdown report
md_content = f"""# Báo Cáo Thuốc Cần Thêm Field

**Ngày tạo:** {report['check_date']}

## Tổng Quan

- **Tổng số thuốc:** {output['summary']['total_drugs']}
- **Thuốc thiếu field chuẩn:** {output['summary']['drugs_missing_standard_fields']} ({output['summary']['drugs_missing_standard_fields']/output['summary']['total_drugs']*100:.1f}%)
- **Thuốc chỉ thiếu field bổ sung:** {output['summary']['drugs_missing_additional_only']}

## ⚠️ ƯU TIÊN CAO - Thuốc Thiếu Field Chuẩn

Các thuốc này **CẦN BỔ SUNG NGAY** vì thiếu field chuẩn (quan trọng):

"""
# Top 30 thuốc thiếu nhiều field nhất
for i, drug in enumerate(drugs_missing_standard[:30], 1):
    md_content += f"""
### {i}. {drug['name']} (thiếu {drug['missing_count']} field)

- **File:** `{drug['file']}`
- **Thiếu field chuẩn ({len(drug['missing_standard'])}):** {', '.join(drug['missing_standard'])}
"""
    if drug['missing_additional']:
        md_content += f"- **Thiếu field bổ sung ({len(drug['missing_additional'])}):** {', '.join(drug['missing_additional'][:5])}"
        if len(drug['missing_additional']) > 5:
            md_content += f" và {len(drug['missing_additional']) - 5} field khác"
    md_content += "\n"

md_content += f"""
## 📋 Thống Kê Theo Field Chuẩn Thiếu

"""
# Thống kê field chuẩn nào thiếu nhiều nhất
field_missing_count = defaultdict(int)
for drug in drugs_missing_standard:
    for field in drug['missing_standard']:
        field_missing_count[field] += 1

for field, count in sorted(field_missing_count.items(), key=lambda x: x[1], reverse=True):
    md_content += f"- `{field}`: {count} thuốc thiếu\n"

md_content += f"""
## 📊 Thống Kê Theo Module

"""
# Thống kê theo module
module_stats = defaultdict(lambda: {'total': 0, 'missing_standard': 0})
for drug in drugs_missing_standard:
    module = drug['file'].split('\\')[2] if '\\' in drug['file'] else 'unknown'
    module_stats[module]['total'] += 1
    module_stats[module]['missing_standard'] += 1

for module, stats in sorted(module_stats.items(), key=lambda x: x[1]['missing_standard'], reverse=True):
    md_content += f"- **{module}**: {stats['missing_standard']} thuốc thiếu field chuẩn\n"

md_content += f"""
## ✅ Thuốc Chỉ Thiếu Field Bổ Sung (Ưu Tiên Thấp)

Các thuốc này đã có đủ 14 field chuẩn, chỉ thiếu field bổ sung (có thể bổ sung sau):

"""
for i, drug in enumerate(drugs_missing_additional_only[:20], 1):
    md_content += f"{i}. **{drug['name']}** - Thiếu: {', '.join(drug['missing_additional'][:5])}\n"
    if len(drug['missing_additional']) > 5:
        md_content += f"   và {len(drug['missing_additional']) - 5} field khác\n"

md_content += f"""
## 🎯 Kế Hoạch Bổ Sung

### Giai Đoạn 1: Field Chuẩn (Ưu Tiên Cao)
- Bổ sung field chuẩn cho {len(drugs_missing_standard)} thuốc
- Tập trung vào các field thiếu nhiều nhất:
  - `pharmacokinetics`: {field_missing_count.get('pharmacokinetics', 0)} thuốc
  - `storage`: {field_missing_count.get('storage', 0)} thuốc
  - `pregnancy`: {field_missing_count.get('pregnancy', 0)} thuốc
  - `precautions`: {field_missing_count.get('precautions', 0)} thuốc
  - `contraindications`: {field_missing_count.get('contraindications', 0)} thuốc

### Giai Đoạn 2: Field Bổ Sung (Ưu Tiên Trung Bình)
- Bổ sung field bổ sung cho các thuốc đã có đủ field chuẩn
- Tập trung vào các field quan trọng:
  - `drug_interactions`: 71 thuốc
  - `overdose_management`: 71 thuốc
  - `hepatic_adjustment`: 69 thuốc
  - `references`: 66 thuốc

## 📝 Lưu Ý

1. **Field chuẩn là bắt buộc** - Cần bổ sung ngay
2. **Field bổ sung là khuyến nghị** - Có thể bổ sung sau
3. Sử dụng `FieldStandardizer` để tự động bổ sung field với template
4. Kiểm tra lại sau khi bổ sung bằng `FieldValidator`
"""

# Lưu markdown
with open('drugs_need_fields_report.md', 'w', encoding='utf-8') as f:
    f.write(md_content)

print("="*60)
print("BAO CAO THUOC CAN THEM FIELD")
print("="*60)
print(f"Tong so thuoc: {output['summary']['total_drugs']}")
print(f"Thuoc thieu field chuan: {output['summary']['drugs_missing_standard_fields']}")
print(f"Thuoc chi thieu field bo sung: {output['summary']['drugs_missing_additional_only']}")
print("\nTop 10 field chuan thieu nhieu nhat:")
for field, count in sorted(field_missing_count.items(), key=lambda x: x[1], reverse=True)[:10]:
    print(f"  - {field}: {count} thuoc")
print("\nDa luu:")
print("  - drugs_need_fields_report.json")
print("  - drugs_need_fields_report.md")
print("="*60)

