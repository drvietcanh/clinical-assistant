#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Create Content Gap List
Tạo danh sách chi tiết các thuốc cần bổ sung nội dung field, phân loại theo mức độ ưu tiên
"""

import sys
from pathlib import Path
from typing import Dict, List, Any, Set
from collections import defaultdict
import json
from datetime import datetime

# Add project root to path
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    from drugs.drug_database import DRUG_DATABASE, TOTAL_DRUGS
    from drugs.field_validator import (
        STANDARD_14_FIELDS,
        ADDITIONAL_8_FIELDS,
        ADDITIONAL_COMMON_FIELDS,
    )
except ImportError:
    sys.path.insert(0, str(Path(__file__).parent))
    from drug_database import DRUG_DATABASE, TOTAL_DRUGS
    from field_validator import (
        STANDARD_14_FIELDS,
        ADDITIONAL_8_FIELDS,
        ADDITIONAL_COMMON_FIELDS,
    )


def find_drug_file(drug_name: str) -> str:
    """Tìm file chứa thuốc"""
    drug_modules_path = project_root / "drugs" / "drug_modules"
    if not drug_modules_path.exists():
        return "Unknown"
    
    for py_file in drug_modules_path.rglob("*.py"):
        if py_file.name == "__init__.py":
            continue
        
        try:
            with open(py_file, 'r', encoding='utf-8') as f:
                content = f.read()
                pattern = rf'"{re.escape(drug_name)}"\s*:'
                if re.search(pattern, content):
                    return str(py_file.relative_to(project_root))
        except:
            continue
    
    return "Unknown"


def is_field_empty(field_value: Any) -> bool:
    """Kiểm tra field có rỗng không"""
    if field_value is None:
        return True
    if isinstance(field_value, str):
        return not field_value.strip() or field_value.strip() == "Đang cập nhật"
    if isinstance(field_value, (list, dict)):
        return len(field_value) == 0
    return False


def analyze_drug_content(drug_name: str, drug_data: Dict[str, Any]) -> Dict[str, Any]:
    """Phân tích nội dung của một thuốc"""
    analysis = {
        "drug_name": drug_name,
        "file_path": find_drug_file(drug_name),
        "missing_standard_fields": [],
        "missing_additional_fields": [],
        "empty_standard_fields": [],
        "empty_additional_fields": [],
        "completeness": 0,
        "priority": "Low",
    }
    
    # Check STANDARD fields
    for field in STANDARD_14_FIELDS:
        if field not in drug_data:
            analysis["missing_standard_fields"].append(field)
        elif is_field_empty(drug_data[field]):
            analysis["empty_standard_fields"].append(field)
    
    # Check ADDITIONAL fields
    for field in ADDITIONAL_8_FIELDS:
        if field not in drug_data:
            analysis["missing_additional_fields"].append(field)
        elif is_field_empty(drug_data[field]):
            analysis["empty_additional_fields"].append(field)
    
    # Check COMMON fields
    missing_common = []
    empty_common = []
    for field in ADDITIONAL_COMMON_FIELDS:
        if field not in drug_data:
            missing_common.append(field)
        elif is_field_empty(drug_data[field]):
            empty_common.append(field)
    
    # Calculate completeness
    total_fields = len(STANDARD_14_FIELDS) + len(ADDITIONAL_8_FIELDS)
    has_fields = (
        total_fields 
        - len(analysis["missing_standard_fields"])
        - len(analysis["missing_additional_fields"])
        - len(analysis["empty_standard_fields"])
        - len(analysis["empty_additional_fields"])
    )
    analysis["completeness"] = int((has_fields / total_fields) * 100)
    
    # Determine priority
    total_missing = (
        len(analysis["missing_standard_fields"]) +
        len(analysis["empty_standard_fields"])
    )
    
    if analysis["completeness"] < 50:
        analysis["priority"] = "Priority 1"
    elif analysis["completeness"] < 80:
        analysis["priority"] = "Priority 2"
    elif total_missing > 0:
        analysis["priority"] = "Priority 3"
    else:
        analysis["priority"] = "Low"
    
    return analysis


def create_content_gap_list() -> Dict[str, Any]:
    """Tạo danh sách khoảng trống nội dung"""
    print("=" * 80)
    print("TẠO DANH SÁCH KHOẢNG TRỐNG NỘI DUNG")
    print("=" * 80)
    print(f"Tổng số thuốc: {TOTAL_DRUGS}")
    print()
    
    all_analyses = {}
    priority_1 = []
    priority_2 = []
    priority_3 = []
    low_priority = []
    
    # Analyze all drugs
    for drug_name, drug_data in DRUG_DATABASE.items():
        if not isinstance(drug_data, dict):
            continue
        
        analysis = analyze_drug_content(drug_name, drug_data)
        all_analyses[drug_name] = analysis
        
        if analysis["priority"] == "Priority 1":
            priority_1.append(drug_name)
        elif analysis["priority"] == "Priority 2":
            priority_2.append(drug_name)
        elif analysis["priority"] == "Priority 3":
            priority_3.append(drug_name)
        else:
            low_priority.append(drug_name)
        
        if len(all_analyses) % 50 == 0:
            print(f"Đã phân tích {len(all_analyses)}/{TOTAL_DRUGS} thuốc...")
    
    # Create summary
    summary = {
        "total_drugs": TOTAL_DRUGS,
        "priority_1_count": len(priority_1),
        "priority_2_count": len(priority_2),
        "priority_3_count": len(priority_3),
        "low_priority_count": len(low_priority),
        "field_statistics": defaultdict(int),
    }
    
    # Field statistics
    for analysis in all_analyses.values():
        for field in analysis["missing_standard_fields"]:
            summary["field_statistics"][f"missing_{field}"] += 1
        for field in analysis["empty_standard_fields"]:
            summary["field_statistics"][f"empty_{field}"] += 1
        for field in analysis["missing_additional_fields"]:
            summary["field_statistics"][f"missing_{field}"] += 1
        for field in analysis["empty_additional_fields"]:
            summary["field_statistics"][f"empty_{field}"] += 1
    
    result = {
        "analysis_date": datetime.now().isoformat(),
        "summary": summary,
        "priority_1_drugs": priority_1,
        "priority_2_drugs": priority_2,
        "priority_3_drugs": priority_3,
        "low_priority_drugs": low_priority,
        "detailed_analyses": all_analyses,
    }
    
    return result


def print_summary(result: Dict[str, Any]):
    """In tóm tắt"""
    summary = result["summary"]
    
    print("\n" + "=" * 80)
    print("TÓM TẮT")
    print("=" * 80)
    
    print(f"\n📊 Phân loại theo Ưu tiên:")
    print(f"  🔴 Priority 1 (<50% hoàn thiện): {summary['priority_1_count']} thuốc")
    print(f"  🟡 Priority 2 (50-80% hoàn thiện): {summary['priority_2_count']} thuốc")
    print(f"  🟢 Priority 3 (>80% hoàn thiện): {summary['priority_3_count']} thuốc")
    print(f"  ⚪ Low Priority (đã đầy đủ): {summary['low_priority_count']} thuốc")
    
    print(f"\n❌ Field thiếu/rỗng nhiều nhất:")
    field_stats = sorted(
        summary["field_statistics"].items(),
        key=lambda x: x[1],
        reverse=True
    )[:15]
    for field, count in field_stats:
        print(f"  {field}: {count} thuốc")
    
    print(f"\n🔴 Priority 1 Drugs (cần bổ sung nhiều nhất):")
    for drug in result["priority_1_drugs"][:20]:
        analysis = result["detailed_analyses"][drug]
        missing = len(analysis["missing_standard_fields"]) + len(analysis["empty_standard_fields"])
        print(f"  - {drug}: {analysis['completeness']}% hoàn thiện, thiếu {missing} STANDARD fields")
    if len(result["priority_1_drugs"]) > 20:
        print(f"  ... và {len(result['priority_1_drugs']) - 20} thuốc khác")


def export_gap_list(result: Dict[str, Any], output_file: str = "drugs_needing_content.json"):
    """Xuất danh sách ra file"""
    output_path = project_root / "drugs" / output_file
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(result, f, ensure_ascii=False, indent=2)
    print(f"\n✅ Đã xuất danh sách: {output_path}")
    
    # Also create human-readable report
    report_path = project_root / "drugs" / "drugs_needing_content_report.txt"
    with open(report_path, 'w', encoding='utf-8') as f:
        f.write("=" * 80 + "\n")
        f.write("DANH SÁCH THUỐC CẦN BỔ SUNG NỘI DUNG FIELD\n")
        f.write("=" * 80 + "\n\n")
        f.write(f"Ngày tạo: {result['analysis_date']}\n")
        f.write(f"Tổng số thuốc: {result['summary']['total_drugs']}\n\n")
        
        f.write("PHÂN LOẠI THEO ƯU TIÊN:\n")
        f.write(f"  Priority 1 (<50%): {result['summary']['priority_1_count']} thuốc\n")
        f.write(f"  Priority 2 (50-80%): {result['summary']['priority_2_count']} thuốc\n")
        f.write(f"  Priority 3 (>80%): {result['summary']['priority_3_count']} thuốc\n")
        f.write(f"  Low Priority: {result['summary']['low_priority_count']} thuốc\n\n")
        
        f.write("PRIORITY 1 DRUGS (Cần bổ sung nhiều nhất):\n")
        f.write("-" * 80 + "\n")
        for drug_name in result["priority_1_drugs"]:
            analysis = result["detailed_analyses"][drug_name]
            f.write(f"\n{drug_name}:\n")
            f.write(f"  File: {analysis['file_path']}\n")
            f.write(f"  Độ hoàn thiện: {analysis['completeness']}%\n")
            if analysis["missing_standard_fields"]:
                f.write(f"  Thiếu STANDARD fields: {', '.join(analysis['missing_standard_fields'])}\n")
            if analysis["empty_standard_fields"]:
                f.write(f"  Rỗng STANDARD fields: {', '.join(analysis['empty_standard_fields'])}\n")
            if analysis["missing_additional_fields"]:
                f.write(f"  Thiếu ADDITIONAL fields: {', '.join(analysis['missing_additional_fields'])}\n")
            if analysis["empty_additional_fields"]:
                f.write(f"  Rỗng ADDITIONAL fields: {', '.join(analysis['empty_additional_fields'])}\n")
    
    print(f"✅ Đã xuất báo cáo: {report_path}")


def main():
    """Main function"""
    print("Bắt đầu tạo danh sách khoảng trống nội dung...\n")
    
    # Create gap list
    result = create_content_gap_list()
    
    # Print summary
    print_summary(result)
    
    # Export
    export_gap_list(result)
    
    print("\n" + "=" * 80)
    print("HOÀN THÀNH")
    print("=" * 80)


if __name__ == "__main__":
    import re
    main()
