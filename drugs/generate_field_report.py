"""
Generate Detailed Field Report
Tạo báo cáo chi tiết về trạng thái fields của từng thuốc
"""

import sys
from pathlib import Path
from typing import Dict, List, Set, Optional, Any
import json
from datetime import datetime

# Add parent directory to path
sys.path.insert(0, str(Path(__file__).parent.parent))

try:
    from drugs.drug_database import DRUG_DATABASE, TOTAL_DRUGS
    from drugs.field_validator import (
        STANDARD_14_FIELDS,
        ADDITIONAL_8_FIELDS,
        ALL_FIELDS,
    )
    from drugs.check_all_drug_fields import (
        check_drug_fields,
        is_field_empty,
        ALL_FIELDS_INCLUDING_COMMON,
    )
except ImportError:
    sys.path.insert(0, str(Path(__file__).parent))
    from drug_database import DRUG_DATABASE, TOTAL_DRUGS
    from field_validator import (
        STANDARD_14_FIELDS,
        ADDITIONAL_8_FIELDS,
        ALL_FIELDS,
    )
    from check_all_drug_fields import (
        check_drug_fields,
        is_field_empty,
        ALL_FIELDS_INCLUDING_COMMON,
    )


def generate_detailed_report(output_file: str = "drug_fields_detailed_report.md") -> str:
    """
    Generate a detailed markdown report
    
    Returns:
        Path to the generated report file
    """
    print("Generating detailed field report...")
    
    # Analyze all drugs
    drug_results = {}
    field_missing_drugs = {field: [] for field in ALL_FIELDS_INCLUDING_COMMON}
    field_empty_drugs = {field: [] for field in ALL_FIELDS_INCLUDING_COMMON}
    
    for drug_name, drug_data in DRUG_DATABASE.items():
        result = check_drug_fields(drug_name, drug_data)
        drug_results[drug_name] = result
        
        # Track which drugs are missing/empty for each field
        for field in result["fields_missing"]:
            field_missing_drugs[field].append(drug_name)
        for field in result["fields_empty"]:
            field_empty_drugs[field].append(drug_name)
    
    # Generate markdown report
    report_lines = []
    report_lines.append("# Báo Cáo Chi Tiết Trạng Thái Fields - Tất cả Thuốc")
    report_lines.append("")
    report_lines.append(f"**Ngày tạo:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    report_lines.append(f"**Tổng số thuốc:** {TOTAL_DRUGS}")
    report_lines.append("")
    
    # Summary section
    report_lines.append("## Tổng Quan")
    report_lines.append("")
    
    drugs_with_all_standard = sum(1 for r in drug_results.values() if r["has_all_standard"])
    drugs_with_all_additional = sum(1 for r in drug_results.values() if r["has_all_additional"])
    avg_completeness = sum(r["completeness_score"] for r in drug_results.values()) / len(drug_results) if drug_results else 0
    
    report_lines.append(f"- **Thuốc có đủ 14 STANDARD fields:** {drugs_with_all_standard} ({drugs_with_all_standard/TOTAL_DRUGS*100:.1f}%)")
    report_lines.append(f"- **Thuốc có đủ 8 ADDITIONAL fields:** {drugs_with_all_additional} ({drugs_with_all_additional/TOTAL_DRUGS*100:.1f}%)")
    report_lines.append(f"- **Độ hoàn thiện trung bình:** {avg_completeness:.1f}%")
    report_lines.append("")
    
    # Field statistics section
    report_lines.append("## Thống Kê Theo Field")
    report_lines.append("")
    report_lines.append("| Field | Có Nội Dung | Thiếu | Rỗng | Tổng Thiếu/Rỗng | % Có Nội Dung |")
    report_lines.append("|-------|-------------|-------|------|-----------------|---------------|")
    
    # Calculate statistics
    field_stats = {}
    for field in ALL_FIELDS_INCLUDING_COMMON:
        missing_count = len(field_missing_drugs[field])
        empty_count = len(field_empty_drugs[field])
        has_content_count = TOTAL_DRUGS - missing_count - empty_count
        total_missing_empty = missing_count + empty_count
        
        field_stats[field] = {
            "has_content": has_content_count,
            "missing": missing_count,
            "empty": empty_count,
            "total_missing_empty": total_missing_empty,
            "percentage": (has_content_count / TOTAL_DRUGS * 100) if TOTAL_DRUGS > 0 else 0
        }
    
    # Sort by total missing/empty
    sorted_fields = sorted(
        field_stats.items(),
        key=lambda x: x[1]["total_missing_empty"],
        reverse=True
    )
    
    for field, stats in sorted_fields:
        report_lines.append(
            f"| {field} | {stats['has_content']} | {stats['missing']} | {stats['empty']} | "
            f"{stats['total_missing_empty']} | {stats['percentage']:.1f}% |"
        )
    
    report_lines.append("")
    
    # Drugs missing specific fields
    report_lines.append("## Danh Sách Thuốc Thiếu/Rỗng Field")
    report_lines.append("")
    
    for field, stats in sorted_fields[:10]:  # Top 10 fields with most missing
        if stats["total_missing_empty"] > 0:
            report_lines.append(f"### {field}")
            report_lines.append("")
            report_lines.append(f"**Tổng thiếu/rỗng:** {stats['total_missing_empty']} thuốc")
            report_lines.append("")
            
            # List drugs missing this field
            missing_list = field_missing_drugs[field][:20]
            empty_list = field_empty_drugs[field][:20]
            
            if missing_list:
                report_lines.append("**Thuốc thiếu field:**")
                report_lines.append("")
                for drug in missing_list:
                    report_lines.append(f"- {drug}")
                if len(field_missing_drugs[field]) > 20:
                    report_lines.append(f"- ... và {len(field_missing_drugs[field]) - 20} thuốc khác")
                report_lines.append("")
            
            if empty_list:
                report_lines.append("**Thuốc có field nhưng rỗng:**")
                report_lines.append("")
                for drug in empty_list:
                    report_lines.append(f"- {drug}")
                if len(field_empty_drugs[field]) > 20:
                    report_lines.append(f"- ... và {len(field_empty_drugs[field]) - 20} thuốc khác")
                report_lines.append("")
            
            report_lines.append("---")
            report_lines.append("")
    
    # Drugs by completeness
    report_lines.append("## Thuốc Theo Độ Hoàn Thiện")
    report_lines.append("")
    
    # Group by completeness ranges
    completeness_ranges = {
        "100%": [],
        "90-99%": [],
        "80-89%": [],
        "70-79%": [],
        "60-69%": [],
        "50-59%": [],
        "<50%": [],
    }
    
    for drug_name, result in drug_results.items():
        score = result["completeness_score"]
        if score >= 100:
            completeness_ranges["100%"].append((drug_name, score))
        elif score >= 90:
            completeness_ranges["90-99%"].append((drug_name, score))
        elif score >= 80:
            completeness_ranges["80-89%"].append((drug_name, score))
        elif score >= 70:
            completeness_ranges["70-79%"].append((drug_name, score))
        elif score >= 60:
            completeness_ranges["60-69%"].append((drug_name, score))
        elif score >= 50:
            completeness_ranges["50-59%"].append((drug_name, score))
        else:
            completeness_ranges["<50%"].append((drug_name, score))
    
    for range_name, drugs in completeness_ranges.items():
        if drugs:
            report_lines.append(f"### {range_name} ({len(drugs)} thuốc)")
            report_lines.append("")
            # Sort by score descending
            drugs_sorted = sorted(drugs, key=lambda x: x[1], reverse=True)
            for drug_name, score in drugs_sorted[:30]:  # Top 30 in each range
                missing_count = len(drug_results[drug_name]["fields_missing"]) + len(drug_results[drug_name]["fields_empty"])
                report_lines.append(f"- **{drug_name}** ({score:.1f}%) - Thiếu/rỗng {missing_count} fields")
            if len(drugs_sorted) > 30:
                report_lines.append(f"- ... và {len(drugs_sorted) - 30} thuốc khác")
            report_lines.append("")
    
    # Priority action items
    report_lines.append("## Ưu tiên Hành Động")
    report_lines.append("")
    report_lines.append("### Priority 1: Bổ sung STANDARD fields thiếu")
    report_lines.append("")
    
    standard_fields_missing = [
        (field, len(field_missing_drugs[field]) + len(field_empty_drugs[field]))
        for field in STANDARD_14_FIELDS
        if len(field_missing_drugs[field]) + len(field_empty_drugs[field]) > 0
    ]
    standard_fields_missing.sort(key=lambda x: x[1], reverse=True)
    
    for field, count in standard_fields_missing:
        report_lines.append(f"- **{field}**: {count} thuốc cần bổ sung")
    
    report_lines.append("")
    report_lines.append("### Priority 2: Bổ sung Safety fields")
    report_lines.append("")
    
    safety_fields = ["black_box_warnings", "contraindications_detail", "overdose_management", "reversal_agents"]
    for field in safety_fields:
        count = len(field_missing_drugs[field]) + len(field_empty_drugs[field])
        if count > 0:
            report_lines.append(f"- **{field}**: {count} thuốc cần bổ sung")
    
    report_lines.append("")
    report_lines.append("### Priority 3: Bổ sung Điều chỉnh Liều")
    report_lines.append("")
    
    dosing_fields = ["renal_adjustment", "hepatic_adjustment"]
    for field in dosing_fields:
        count = len(field_missing_drugs[field]) + len(field_empty_drugs[field])
        if count > 0:
            report_lines.append(f"- **{field}**: {count} thuốc cần bổ sung")
    
    report_lines.append("")
    report_lines.append("---")
    report_lines.append("")
    report_lines.append("*Báo cáo được tạo tự động bởi generate_field_report.py*")
    
    # Write report
    output_path = Path(__file__).parent / output_file
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write('\n'.join(report_lines))
    
    print(f"Detailed report generated: {output_path}")
    return str(output_path)


def main():
    """Main function"""
    import argparse
    
    parser = argparse.ArgumentParser(description="Generate detailed field report")
    parser.add_argument("--output", default="drug_fields_detailed_report.md",
                       help="Output report file")
    
    args = parser.parse_args()
    
    print("="*80)
    print("GENERATE DETAILED FIELD REPORT")
    print("="*80)
    
    report_path = generate_detailed_report(output_file=args.output)
    
    print("\n" + "="*80)
    print(f"Report generated successfully: {report_path}")
    print("="*80)


if __name__ == "__main__":
    main()
