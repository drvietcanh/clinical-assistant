"""
Create Final Summary Report
Tạo báo cáo tổng kết cuối cùng về trạng thái fields
"""

import sys
from pathlib import Path
from typing import Dict, List, Any
import json
from datetime import datetime

sys.path.insert(0, str(Path(__file__).parent.parent))

try:
    from drugs.drug_database import DRUG_DATABASE, TOTAL_DRUGS
    from drugs.field_validator import (
        STANDARD_14_FIELDS,
        ADDITIONAL_8_FIELDS,
        ALL_FIELDS_WITH_COMMON,
    )
    from drugs.check_all_drug_fields import check_drug_fields, ALL_FIELDS_INCLUDING_COMMON
except ImportError:
    sys.path.insert(0, str(Path(__file__).parent))
    from drug_database import DRUG_DATABASE, TOTAL_DRUGS
    from field_validator import (
        STANDARD_14_FIELDS,
        ADDITIONAL_8_FIELDS,
        ALL_FIELDS_WITH_COMMON,
    )
    from check_all_drug_fields import check_drug_fields, ALL_FIELDS_INCLUDING_COMMON


def create_comprehensive_summary() -> Dict[str, Any]:
    """Tạo báo cáo tổng kết toàn diện"""
    
    print("Creating comprehensive summary...")
    
    # Analyze all drugs
    drug_results = {}
    field_stats = {field: {"has": 0, "missing": 0, "empty": 0, "has_content": 0} 
                   for field in ALL_FIELDS_INCLUDING_COMMON}
    
    for drug_name, drug_data in DRUG_DATABASE.items():
        result = check_drug_fields(drug_name, drug_data)
        drug_results[drug_name] = result
        
        # Update statistics
        for field in ALL_FIELDS_INCLUDING_COMMON:
            if field in result["fields_present"]:
                field_stats[field]["has"] += 1
                if field in result["fields_with_content"]:
                    field_stats[field]["has_content"] += 1
                elif field in result["fields_empty"]:
                    field_stats[field]["empty"] += 1
            else:
                field_stats[field]["missing"] += 1
    
    # Calculate summary
    total_drugs = TOTAL_DRUGS
    drugs_with_all_standard = sum(1 for r in drug_results.values() if r["has_all_standard"])
    drugs_with_all_additional = sum(1 for r in drug_results.values() if r["has_all_additional"])
    avg_completeness = sum(r["completeness_score"] for r in drug_results.values()) / len(drug_results) if drug_results else 0
    
    # Priority fields to supplement
    priority_fields = {
        "standard_missing": [
            (field, field_stats[field]["missing"] + field_stats[field]["empty"])
            for field in STANDARD_14_FIELDS
            if field_stats[field]["missing"] + field_stats[field]["empty"] > 0
        ],
        "safety_fields": [
            (field, field_stats[field]["missing"] + field_stats[field]["empty"])
            for field in ["black_box_warnings", "contraindications_detail", "overdose_management", "reversal_agents"]
            if field_stats[field]["missing"] + field_stats[field]["empty"] > 0
        ],
        "dosing_adjustments": [
            (field, field_stats[field]["missing"] + field_stats[field]["empty"])
            for field in ["renal_adjustment", "hepatic_adjustment"]
            if field_stats[field]["missing"] + field_stats[field]["empty"] > 0
        ],
    }
    
    # Sort priorities
    for key in priority_fields:
        priority_fields[key].sort(key=lambda x: x[1], reverse=True)
    
    return {
        "generation_date": datetime.now().isoformat(),
        "total_drugs": total_drugs,
        "summary": {
            "drugs_with_all_standard": drugs_with_all_standard,
            "drugs_with_all_standard_pct": (drugs_with_all_standard / total_drugs * 100) if total_drugs > 0 else 0,
            "drugs_with_all_additional": drugs_with_all_additional,
            "drugs_with_all_additional_pct": (drugs_with_all_additional / total_drugs * 100) if total_drugs > 0 else 0,
            "avg_completeness": avg_completeness,
            "drugs_100_percent": len([r for r in drug_results.values() if r["completeness_score"] >= 100]),
            "drugs_90_plus_percent": len([r for r in drug_results.values() if r["completeness_score"] >= 90]),
            "drugs_under_50_percent": len([r for r in drug_results.values() if r["completeness_score"] < 50]),
        },
        "field_statistics": field_stats,
        "priority_fields": priority_fields,
        "top_missing_fields": sorted(
            [(field, stats["missing"] + stats["empty"]) 
             for field, stats in field_stats.items()],
            key=lambda x: x[1],
            reverse=True
        )[:10],
    }


def generate_markdown_report(summary: Dict[str, Any]) -> str:
    """Generate markdown report"""
    
    lines = []
    lines.append("# Báo Cáo Tổng Kết - Kiểm Tra và Bổ Sung Fields")
    lines.append("")
    lines.append(f"**Ngày tạo:** {summary['generation_date']}")
    lines.append(f"**Tổng số thuốc:** {summary['total_drugs']}")
    lines.append("")
    
    # Summary section
    lines.append("## Tổng Quan")
    lines.append("")
    s = summary["summary"]
    lines.append(f"- ✅ **Thuốc có đủ 14 STANDARD fields:** {s['drugs_with_all_standard']} ({s['drugs_with_all_standard_pct']:.1f}%)")
    lines.append(f"- ✅ **Thuốc có đủ 8 ADDITIONAL fields:** {s['drugs_with_all_additional']} ({s['drugs_with_all_additional_pct']:.1f}%)")
    lines.append(f"- 📊 **Độ hoàn thiện trung bình:** {s['avg_completeness']:.1f}%")
    lines.append(f"- 🎯 **Thuốc đạt 100%:** {s['drugs_100_percent']} ({s['drugs_100_percent']/summary['total_drugs']*100:.1f}%)")
    lines.append(f"- 🎯 **Thuốc đạt 90%+:** {s['drugs_90_plus_percent']} ({s['drugs_90_plus_percent']/summary['total_drugs']*100:.1f}%)")
    lines.append(f"- ⚠️ **Thuốc dưới 50%:** {s['drugs_under_50_percent']} ({s['drugs_under_50_percent']/summary['total_drugs']*100:.1f}%)")
    lines.append("")
    
    # Top missing fields
    lines.append("## Top 10 Field Thiếu Nhiều Nhất")
    lines.append("")
    lines.append("| Field | Thiếu/Rỗng | % Có Nội Dung |")
    lines.append("|-------|------------|---------------|")
    
    field_stats = summary["field_statistics"]
    for field, count in summary["top_missing_fields"]:
        stats = field_stats[field]
        has_content_pct = (stats["has_content"] / summary["total_drugs"] * 100) if summary["total_drugs"] > 0 else 0
        lines.append(f"| {field} | {count} | {has_content_pct:.1f}% |")
    
    lines.append("")
    
    # Priority actions
    lines.append("## Ưu Tiên Hành Động")
    lines.append("")
    
    priorities = summary["priority_fields"]
    
    lines.append("### Priority 1: Bổ sung STANDARD Fields")
    lines.append("")
    if priorities["standard_missing"]:
        for field, count in priorities["standard_missing"]:
            lines.append(f"- **{field}**: {count} thuốc cần bổ sung")
    else:
        lines.append("- ✅ Tất cả STANDARD fields đã có đủ")
    lines.append("")
    
    lines.append("### Priority 2: Bổ sung Safety Fields")
    lines.append("")
    for field, count in priorities["safety_fields"]:
        lines.append(f"- **{field}**: {count} thuốc cần bổ sung")
    lines.append("")
    
    lines.append("### Priority 3: Bổ sung Điều chỉnh Liều")
    lines.append("")
    for field, count in priorities["dosing_adjustments"]:
        lines.append(f"- **{field}**: {count} thuốc cần bổ sung")
    lines.append("")
    
    # Scripts available
    lines.append("## Scripts Đã Tạo")
    lines.append("")
    lines.append("### 1. `check_all_drug_fields.py`")
    lines.append("Kiểm tra toàn diện tất cả thuốc và fields")
    lines.append("```bash")
    lines.append("python drugs/check_all_drug_fields.py")
    lines.append("```")
    lines.append("")
    
    lines.append("### 2. `supplement_missing_fields.py`")
    lines.append("Bổ sung skeleton fields cho thuốc thiếu")
    lines.append("```bash")
    lines.append("# Dry-run (xem trước)")
    lines.append("python drugs/supplement_missing_fields.py --dry-run")
    lines.append("")
    lines.append("# Thực hiện (chỉ thay đổi trong memory)")
    lines.append("python drugs/supplement_missing_fields.py --execute")
    lines.append("```")
    lines.append("")
    lines.append("**Lưu ý:** Script này chỉ thay đổi DRUG_DATABASE trong memory. ")
    lines.append("Để lưu thay đổi vào files nguồn, cần cập nhật các file Python trong `drugs/drug_modules/`")
    lines.append("")
    
    lines.append("### 3. `generate_field_report.py`")
    lines.append("Tạo báo cáo markdown chi tiết")
    lines.append("```bash")
    lines.append("python drugs/generate_field_report.py")
    lines.append("```")
    lines.append("")
    
    lines.append("### 4. `validate_all_drugs.py`")
    lines.append("Validation tất cả thuốc")
    lines.append("```bash")
    lines.append("python drugs/validate_all_drugs.py")
    lines.append("```")
    lines.append("")
    
    # Next steps
    lines.append("## Bước Tiếp Theo")
    lines.append("")
    lines.append("### 1. Bổ sung Skeleton Fields")
    lines.append("")
    lines.append("Các field đã được tự động bổ sung skeleton thông qua `_ensure_enhanced_fields_on_database()` ")
    lines.append("trong `drug_database.py`. Tuy nhiên, các field này có giá trị placeholder 'Đang cập nhật'.")
    lines.append("")
    
    lines.append("### 2. Bổ sung Nội Dung Thực Tế")
    lines.append("")
    lines.append("Cần bổ sung nội dung thực tế cho các field còn thiếu/rỗng:")
    lines.append("")
    lines.append("1. **STANDARD Fields** - Ưu tiên cao nhất")
    lines.append("2. **Safety Fields** - `black_box_warnings`, `contraindications_detail`, `overdose_management`, `reversal_agents`")
    lines.append("3. **Dosing Adjustments** - `renal_adjustment`, `hepatic_adjustment`")
    lines.append("4. **Additional Fields** - `drug_interactions`, `pregnancy_lactation`, `administration_instructions`, `references`")
    lines.append("")
    
    lines.append("### 3. Cập Nhật Files Nguồn")
    lines.append("")
    lines.append("Sử dụng `drug_manager.py` để tìm file chứa từng thuốc:")
    lines.append("```python")
    lines.append("from drugs.drug_manager import find_drug_file")
    lines.append("file_path = find_drug_file('DrugName')")
    lines.append("```")
    lines.append("")
    lines.append("Sau đó cập nhật file Python tương ứng với fields mới.")
    lines.append("")
    
    lines.append("---")
    lines.append("")
    lines.append("*Báo cáo được tạo tự động bởi create_final_summary.py*")
    
    return '\n'.join(lines)


def main():
    """Main function"""
    print("="*80)
    print("CREATE FINAL SUMMARY REPORT")
    print("="*80)
    
    # Create summary
    summary = create_comprehensive_summary()
    
    # Generate markdown report
    markdown_report = generate_markdown_report(summary)
    
    # Save reports
    md_path = Path(__file__).parent / "FINAL_FIELD_SUMMARY.md"
    with open(md_path, 'w', encoding='utf-8') as f:
        f.write(markdown_report)
    
    json_path = Path(__file__).parent / "final_field_summary.json"
    with open(json_path, 'w', encoding='utf-8') as f:
        json.dump(summary, f, ensure_ascii=False, indent=2)
    
    # Print summary
    print("\n" + "-"*80)
    print("SUMMARY")
    print("-"*80)
    s = summary["summary"]
    print(f"Total drugs: {summary['total_drugs']}")
    print(f"Drugs with all 14 STANDARD fields: {s['drugs_with_all_standard']} ({s['drugs_with_all_standard_pct']:.1f}%)")
    print(f"Drugs with all 8 ADDITIONAL fields: {s['drugs_with_all_additional']} ({s['drugs_with_all_additional_pct']:.1f}%)")
    print(f"Average completeness: {s['avg_completeness']:.1f}%")
    print(f"Drugs at 100%: {s['drugs_100_percent']}")
    print(f"Drugs at 90%+: {s['drugs_90_plus_percent']}")
    
    print("\n" + "-"*80)
    print("TOP 5 MISSING FIELDS")
    print("-"*80)
    for field, count in summary["top_missing_fields"][:5]:
        print(f"  {field}: {count} drugs")
    
    print(f"\nReports saved:")
    print(f"  - {md_path}")
    print(f"  - {json_path}")
    print("\n" + "="*80)
    print("Summary generation complete!")
    print("="*80)


if __name__ == "__main__":
    main()
