#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Manual Supplementation Analyzer
Phân tích và phân loại thuốc theo mức độ ưu tiên để bổ sung thủ công
"""

import json
import sys
from pathlib import Path
from typing import Dict, List, Set, Any
from collections import defaultdict
from datetime import datetime

# Add project root to path
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    from drugs.drug_database import DRUG_DATABASE
    from drugs.field_validator import STANDARD_14_FIELDS, ADDITIONAL_8_FIELDS
except ImportError:
    sys.path.insert(0, str(Path(__file__).parent))
    from drug_database import DRUG_DATABASE
    from field_validator import STANDARD_14_FIELDS, ADDITIONAL_8_FIELDS


def load_audit_data() -> Dict[str, Any]:
    """Load dữ liệu audit từ các file JSON"""
    audit_file = Path(__file__).parent / "comprehensive_drug_audit.json"
    summary_file = Path(__file__).parent / "final_audit_summary.json"
    
    audit_data = {}
    summary_data = {}
    
    if audit_file.exists():
        with open(audit_file, 'r', encoding='utf-8') as f:
            audit_data = json.load(f)
    
    if summary_file.exists():
        with open(summary_file, 'r', encoding='utf-8') as f:
            summary_data = json.load(f)
    
    return audit_data, summary_data


def categorize_drugs_by_priority(audit_data: Dict[str, Any], summary_data: Dict[str, Any]) -> Dict[str, Dict[str, Any]]:
    """
    Phân loại thuốc theo mức độ ưu tiên:
    - P0: Thiếu field bắt buộc quan trọng (pregnancy, dosage)
    - P1: Thiếu field bắt buộc khác (side_effects, contraindications, interactions)
    - P2: Field bắt buộc rỗng (storage)
    - P3: Field khuyến nghị rỗng (có thể bỏ qua)
    """
    priority_drugs = {
        "P0": defaultdict(list),  # Highest priority
        "P1": defaultdict(list),
        "P2": defaultdict(list),
        "P3": defaultdict(list)
    }
    
    missing_fields = audit_data.get("missing_critical_fields", {})
    format_errors = audit_data.get("format_errors", {})
    field_completeness = summary_data.get("field_completeness", {})
    
    # P0: pregnancy và dosage (field bắt buộc quan trọng nhất)
    if "pregnancy" in missing_fields:
        for drug in missing_fields["pregnancy"]:
            priority_drugs["P0"]["pregnancy"].append(drug)
    
    if "dosage" in missing_fields:
        for drug in missing_fields["dosage"]:
            priority_drugs["P0"]["dosage"].append(drug)
    
    # P1: side_effects, contraindications, interactions
    if "side_effects" in missing_fields:
        for drug in missing_fields["side_effects"]:
            priority_drugs["P1"]["side_effects"].append(drug)
    
    if "contraindications" in missing_fields:
        for drug in missing_fields["contraindications"]:
            priority_drugs["P1"]["contraindications"].append(drug)
    
    # Check interactions from field_completeness
    if "interactions" in field_completeness:
        interactions_data = field_completeness["interactions"]
        if interactions_data.get("empty", 0) > 0:
            # Get drugs with empty interactions from audit
            if "interactions" in missing_fields:
                for drug in missing_fields.get("interactions", []):
                    priority_drugs["P1"]["interactions"].append(drug)
    
    # P2: storage (field bắt buộc nhưng có thể rỗng)
    if "storage" in field_completeness:
        storage_data = field_completeness["storage"]
        if storage_data.get("empty", 0) > 0:
            # Find drugs with empty storage
            for drug_name, drug_data in DRUG_DATABASE.items():
                if isinstance(drug_data, dict):
                    storage = drug_data.get("storage", "")
                    if not storage or storage.strip() == "" or storage == "Đang cập nhật":
                        priority_drugs["P2"]["storage"].append(drug_name)
    
    # P3: Field khuyến nghị rỗng
    additional_fields = ["pregnancy_lactation", "administration_instructions", "references", "black_box_warnings"]
    for field in additional_fields:
        if field in field_completeness:
            field_data = field_completeness[field]
            if field_data.get("empty", 0) > 0:
                # Find drugs with empty field
                for drug_name, drug_data in DRUG_DATABASE.items():
                    if isinstance(drug_data, dict):
                        field_value = drug_data.get(field)
                        if field_value is None or (isinstance(field_value, str) and (not field_value.strip() or field_value == "Đang cập nhật")):
                            priority_drugs["P3"][field].append(drug_name)
    
    # Convert defaultdict to regular dict
    result = {}
    for priority, fields in priority_drugs.items():
        result[priority] = dict(fields)
    
    return result


def get_drug_info(drug_name: str) -> Dict[str, Any]:
    """Lấy thông tin về thuốc"""
    drug_data = DRUG_DATABASE.get(drug_name, {})
    if not isinstance(drug_data, dict):
        return {}
    
    return {
        "name": drug_name,
        "group": drug_data.get("group", "Unknown"),
        "vietnamese_name": drug_data.get("vietnamese_name", ""),
        "administration": drug_data.get("administration", []),
        "indications": drug_data.get("indications", [])
    }


def create_priority_report(priority_drugs: Dict[str, Dict[str, List[str]]]) -> Dict[str, Any]:
    """Tạo báo cáo chi tiết về thuốc cần bổ sung"""
    report = {
        "analysis_date": datetime.now().isoformat(),
        "total_drugs": len(DRUG_DATABASE),
        "priorities": {},
        "summary": {
            "P0": 0,
            "P1": 0,
            "P2": 0,
            "P3": 0
        }
    }
    
    for priority in ["P0", "P1", "P2", "P3"]:
        priority_data = priority_drugs.get(priority, {})
        report["priorities"][priority] = {}
        
        total_drugs_in_priority = set()
        
        for field, drugs in priority_data.items():
            drug_details = []
            for drug_name in drugs:
                drug_info = get_drug_info(drug_name)
                drug_details.append({
                    "name": drug_name,
                    "group": drug_info.get("group", "Unknown"),
                    "vietnamese_name": drug_info.get("vietnamese_name", ""),
                    "missing_field": field
                })
                total_drugs_in_priority.add(drug_name)
            
            report["priorities"][priority][field] = {
                "count": len(drugs),
                "drugs": drug_details
            }
        
        report["summary"][priority] = len(total_drugs_in_priority)
    
    return report


def generate_markdown_report(report: Dict[str, Any], output_file: Path):
    """Tạo báo cáo markdown"""
    md_content = f"""# Báo Cáo Phân tích Thuốc Cần Bổ sung Thủ Công

**Ngày phân tích:** {report['analysis_date']}  
**Tổng số thuốc:** {report['total_drugs']}

---

## Tổng Quan

- **P0 (Ưu tiên cao nhất):** {report['summary']['P0']} thuốc
- **P1 (Ưu tiên cao):** {report['summary']['P1']} thuốc
- **P2 (Ưu tiên trung bình):** {report['summary']['P2']} thuốc
- **P3 (Ưu tiên thấp):** {report['summary']['P3']} thuốc

---

## Chi Tiết Theo Mức độ Ưu tiên

"""
    
    priority_names = {
        "P0": "P0 - Ưu tiên Cao Nhất (Field Bắt Buộc Quan Trọng)",
        "P1": "P1 - Ưu tiên Cao (Field Bắt Buộc Khác)",
        "P2": "P2 - Ưu tiên Trung Bình (Field Bắt Buộc Rỗng)",
        "P3": "P3 - Ưu tiên Thấp (Field Khuyến Nghị)"
    }
    
    for priority in ["P0", "P1", "P2", "P3"]:
        md_content += f"### {priority_names[priority]}\n\n"
        
        priority_data = report["priorities"].get(priority, {})
        if not priority_data:
            md_content += "*Không có thuốc nào*\n\n"
            continue
        
        for field, field_data in priority_data.items():
            count = field_data["count"]
            drugs = field_data["drugs"]
            
            md_content += f"#### Field: `{field}` ({count} thuốc)\n\n"
            
            # Group by drug group
            by_group = defaultdict(list)
            for drug in drugs:
                group = drug.get("group", "Unknown")
                by_group[group].append(drug)
            
            for group, group_drugs in sorted(by_group.items()):
                md_content += f"**{group}:**\n"
                for drug in group_drugs:
                    vietnamese = drug.get("vietnamese_name", "")
                    if vietnamese:
                        md_content += f"- {drug['name']} ({vietnamese})\n"
                    else:
                        md_content += f"- {drug['name']}\n"
                md_content += "\n"
            
            md_content += "\n"
    
    md_content += """---

## Hướng dẫn Sử Dụng

1. Bắt đầu với P0 (ưu tiên cao nhất)
2. Sử dụng script `manual_supplementation_helper.py` để bổ sung từng thuốc
3. Kiểm tra thông tin từ nguồn đáng tin cậy trước khi bổ sung
4. Đánh dấu "BỎ QUA" nếu không tìm thấy thông tin đáng tin cậy

---

**Xem chi tiết JSON:** `manual_supplementation_priority.json`
"""
    
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(md_content)


def main():
    """Main function"""
    print("Đang phân tích thuốc cần bổ sung thủ công...")
    
    # Load audit data
    audit_data, summary_data = load_audit_data()
    
    if not audit_data and not summary_data:
        print("⚠️  Không tìm thấy file audit. Chạy comprehensive_drug_audit.py trước.")
        return
    
    # Categorize drugs by priority
    priority_drugs = categorize_drugs_by_priority(audit_data, summary_data)
    
    # Create detailed report
    report = create_priority_report(priority_drugs)
    
    # Save JSON report
    json_output = Path(__file__).parent / "manual_supplementation_priority.json"
    with open(json_output, 'w', encoding='utf-8') as f:
        json.dump(report, f, ensure_ascii=False, indent=2)
    print(f"✅ Đã lưu báo cáo JSON: {json_output}")
    
    # Generate markdown report
    md_output = Path(__file__).parent / "manual_supplementation_report.md"
    generate_markdown_report(report, md_output)
    print(f"✅ Đã tạo báo cáo Markdown: {md_output}")
    
    # Print summary
    print("\n" + "="*60)
    print("TỔNG KẾT")
    print("="*60)
    print(f"P0 (Ưu tiên cao nhất): {report['summary']['P0']} thuốc")
    print(f"P1 (Ưu tiên cao):     {report['summary']['P1']} thuốc")
    print(f"P2 (Ưu tiên trung bình): {report['summary']['P2']} thuốc")
    print(f"P3 (Ưu tiên thấp):   {report['summary']['P3']} thuốc")
    print("="*60)
    
    # Show P0 details
    if report['summary']['P0'] > 0:
        print("\n🔴 P0 - ƯU TIÊN CAO NHẤT:")
        p0_data = report['priorities']['P0']
        for field, field_data in p0_data.items():
            print(f"  - {field}: {field_data['count']} thuốc")
            if field_data['count'] <= 10:
                for drug in field_data['drugs']:
                    print(f"    • {drug['name']}")


if __name__ == "__main__":
    main()
