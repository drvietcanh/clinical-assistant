#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Analyze Drug Field Order
Phân tích chi tiết thứ tự field hiện tại của tất cả thuốc
"""

import sys
from pathlib import Path
from typing import Dict, List, Any, Tuple, Optional
from collections import defaultdict
import json
from datetime import datetime
import ast
import re

# Add project root to path
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    from drugs.drug_database import DRUG_DATABASE, TOTAL_DRUGS
    from drugs.field_validator import (
        STANDARD_14_FIELDS,
        ADDITIONAL_8_FIELDS,
        ADDITIONAL_COMMON_FIELDS,
        ALL_FIELDS_WITH_COMMON,
        FieldValidator
    )
except ImportError:
    sys.path.insert(0, str(Path(__file__).parent))
    from drug_database import DRUG_DATABASE, TOTAL_DRUGS
    from field_validator import (
        STANDARD_14_FIELDS,
        ADDITIONAL_8_FIELDS,
        ADDITIONAL_COMMON_FIELDS,
        ALL_FIELDS_WITH_COMMON,
        FieldValidator
    )


def find_drug_file(drug_name: str) -> Optional[str]:
    """Tìm file chứa thuốc"""
    drug_modules_path = project_root / "drugs" / "drug_modules"
    if not drug_modules_path.exists():
        return None
    
    # Search recursively
    for py_file in drug_modules_path.rglob("*.py"):
        if py_file.name == "__init__.py":
            continue
        
        try:
            with open(py_file, 'r', encoding='utf-8') as f:
                content = f.read()
                # Check for drug name in dictionary key
                pattern = rf'["\']{re.escape(drug_name)}["\']\s*:'
                if re.search(pattern, content):
                    return str(py_file.relative_to(project_root))
        except Exception:
            continue
    
    return None


def get_field_order_from_file(file_path: str, drug_name: str) -> Optional[List[str]]:
    """Lấy thứ tự field từ file source"""
    full_path = project_root / file_path
    if not full_path.exists():
        return None
    
    try:
        with open(full_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Try to parse AST to find the drug dictionary
        try:
            tree = ast.parse(content)
            for node in ast.walk(tree):
                if isinstance(node, ast.Dict):
                    # Check if this dict contains our drug
                    for i, key_node in enumerate(node.keys):
                        if isinstance(key_node, ast.Constant) and key_node.value == drug_name:
                            # Found the drug dict, get field order
                            if i < len(node.values):
                                value_node = node.values[i]
                                if isinstance(value_node, ast.Dict):
                                    field_order = []
                                    for k in value_node.keys:
                                        if isinstance(k, ast.Constant):
                                            field_order.append(k.value)
                                    return field_order
        except:
            pass
        
        # Fallback: use regex to find field order
        pattern = rf'"{re.escape(drug_name)}"\s*:\s*\{{(.*?)\n(?=\s*["\'])'
        match = re.search(pattern, content, re.DOTALL)
        if match:
            drug_content = match.group(1)
            # Extract field names
            field_pattern = r'"([a-z_]+)"\s*:'
            fields = re.findall(field_pattern, drug_content)
            return fields if fields else None
        
    except Exception as e:
        print(f"Error reading {file_path}: {e}")
    
    return None


def analyze_drug_field_order() -> Dict[str, Any]:
    """Phân tích thứ tự field của tất cả thuốc"""
    print("=" * 80)
    print("PHÂN TÍCH THỨ TỰ FIELD CỦA TẤT CẢ THUỐC")
    print("=" * 80)
    print(f"Tổng số thuốc: {TOTAL_DRUGS}")
    print()
    
    validator = FieldValidator()
    results = {
        "analysis_date": datetime.now().isoformat(),
        "total_drugs": TOTAL_DRUGS,
        "drugs_analysis": {},
        "summary": {
            "correct_order": 0,
            "incorrect_order": 0,
            "missing_fields": defaultdict(int),
            "out_of_order_fields": defaultdict(list),
            "drugs_by_module": defaultdict(list),
            "drugs_by_completeness": defaultdict(list),
        }
    }
    
    # Analyze each drug
    for drug_name, drug_data in DRUG_DATABASE.items():
        if not isinstance(drug_data, dict):
            continue
        
        # Find source file
        file_path = find_drug_file(drug_name)
        
        # Get current field order
        current_fields = list(drug_data.keys())
        
        # Get field order from source file if possible
        source_field_order = None
        if file_path:
            source_field_order = get_field_order_from_file(file_path, drug_name)
        
        # Validate field order
        is_correct_order, out_of_order_fields = validator.validate_field_order(drug_data)
        
        # Check missing fields
        missing_standard = [f for f in STANDARD_14_FIELDS if f not in drug_data]
        missing_additional = [f for f in ADDITIONAL_8_FIELDS if f not in drug_data]
        
        # Calculate completeness
        total_standard = len(STANDARD_14_FIELDS)
        total_additional = len(ADDITIONAL_8_FIELDS)
        has_standard = total_standard - len(missing_standard)
        has_additional = total_additional - len(missing_additional)
        completeness = int((has_standard + has_additional) / (total_standard + total_additional) * 100)
        
        # Determine module from file path
        module = "Unknown"
        if file_path:
            parts = file_path.split("/")
            if "drug_modules" in parts:
                idx = parts.index("drug_modules")
                if idx + 1 < len(parts):
                    module = parts[idx + 1]
        
        # Store analysis
        drug_analysis = {
            "file_path": file_path,
            "module": module,
            "current_field_order": current_fields,
            "source_field_order": source_field_order,
            "is_correct_order": is_correct_order,
            "out_of_order_fields": out_of_order_fields,
            "missing_standard_fields": missing_standard,
            "missing_additional_fields": missing_additional,
            "completeness": completeness,
            "field_count": len(current_fields),
        }
        
        results["drugs_analysis"][drug_name] = drug_analysis
        
        # Update summary
        if is_correct_order:
            results["summary"]["correct_order"] += 1
        else:
            results["summary"]["incorrect_order"] += 1
            for field in out_of_order_fields:
                results["summary"]["out_of_order_fields"][field].append(drug_name)
        
        for field in missing_standard:
            results["summary"]["missing_fields"][field] += 1
        
        results["summary"]["drugs_by_module"][module].append(drug_name)
        results["summary"]["drugs_by_completeness"][completeness].append(drug_name)
        
        # Progress indicator
        if len(results["drugs_analysis"]) % 50 == 0:
            print(f"Đã phân tích {len(results["drugs_analysis"])}/{TOTAL_DRUGS} thuốc...")
    
    return results


def print_summary(results: Dict[str, Any]):
    """In tóm tắt kết quả phân tích"""
    summary = results["summary"]
    
    print("\n" + "=" * 80)
    print("TÓM TẮT KẾT QUẢ PHÂN TÍCH")
    print("=" * 80)
    
    print(f"\n📊 Thứ tự Field:")
    print(f"  ✅ Đúng thứ tự: {summary['correct_order']} ({summary['correct_order']/results['total_drugs']*100:.1f}%)")
    print(f"  ❌ Sai thứ tự: {summary['incorrect_order']} ({summary['incorrect_order']/results['total_drugs']*100:.1f}%)")
    
    print(f"\n📦 Phân bố theo Module:")
    for module, drugs in sorted(summary["drugs_by_module"].items(), key=lambda x: len(x[1]), reverse=True):
        print(f"  {module}: {len(drugs)} thuốc")
    
    print(f"\n📈 Phân bố theo Độ hoàn thiện:")
    completeness_levels = sorted(summary["drugs_by_completeness"].keys(), reverse=True)
    for level in completeness_levels[:10]:  # Top 10
        count = len(summary["drugs_by_completeness"][level])
        print(f"  {level}%: {count} thuốc")
    
    print(f"\n❌ Field thiếu nhiều nhất:")
    for field, count in sorted(summary["missing_fields"].items(), key=lambda x: x[1], reverse=True)[:10]:
        print(f"  {field}: {count} thuốc")
    
    print(f"\n🔄 Field sai thứ tự nhiều nhất:")
    for field, drugs in sorted(summary["out_of_order_fields"].items(), key=lambda x: len(x[1]), reverse=True)[:10]:
        print(f"  {field}: {len(drugs)} thuốc")


def export_report(results: Dict[str, Any], output_file: str = "drug_field_order_analysis.json"):
    """Xuất báo cáo ra file JSON"""
    output_path = project_root / "drugs" / output_file
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(results, f, ensure_ascii=False, indent=2)
    print(f"\n✅ Đã xuất báo cáo chi tiết: {output_path}")
    
    # Also create a human-readable summary
    summary_path = project_root / "drugs" / "drug_field_order_analysis_summary.txt"
    with open(summary_path, 'w', encoding='utf-8') as f:
        f.write("=" * 80 + "\n")
        f.write("BÁO CÁO PHÂN TÍCH THỨ TỰ FIELD THUỐC\n")
        f.write("=" * 80 + "\n\n")
        f.write(f"Ngày phân tích: {results['analysis_date']}\n")
        f.write(f"Tổng số thuốc: {results['total_drugs']}\n\n")
        
        summary = results["summary"]
        f.write(f"THỨ TỰ FIELD:\n")
        f.write(f"  ✅ Đúng thứ tự: {summary['correct_order']} ({summary['correct_order']/results['total_drugs']*100:.1f}%)\n")
        f.write(f"  ❌ Sai thứ tự: {summary['incorrect_order']} ({summary['incorrect_order']/results['total_drugs']*100:.1f}%)\n\n")
        
        f.write(f"THUỐC SAI THỨ TỰ FIELD:\n")
        incorrect_drugs = [
            (name, data) for name, data in results["drugs_analysis"].items()
            if not data["is_correct_order"]
        ]
        for drug_name, data in sorted(incorrect_drugs, key=lambda x: len(x[1]["out_of_order_fields"]), reverse=True)[:50]:
            f.write(f"  - {drug_name}: {', '.join(data['out_of_order_fields'])}\n")
            if data["file_path"]:
                f.write(f"    File: {data['file_path']}\n")
        
        f.write(f"\n\nTHUỐC THIẾU FIELD:\n")
        drugs_with_missing = [
            (name, data) for name, data in results["drugs_analysis"].items()
            if data["missing_standard_fields"] or data["missing_additional_fields"]
        ]
        for drug_name, data in sorted(drugs_with_missing, key=lambda x: len(x[1]["missing_standard_fields"]) + len(x[1]["missing_additional_fields"]), reverse=True)[:50]:
            missing = data["missing_standard_fields"] + data["missing_additional_fields"]
            f.write(f"  - {drug_name}: {', '.join(missing)}\n")
            if data["file_path"]:
                f.write(f"    File: {data['file_path']}\n")
    
    print(f"✅ Đã xuất tóm tắt: {summary_path}")


def main():
    """Main function"""
    print("Bắt đầu phân tích thứ tự field của tất cả thuốc...\n")
    
    # Analyze
    results = analyze_drug_field_order()
    
    # Print summary
    print_summary(results)
    
    # Export report
    export_report(results)
    
    print("\n" + "=" * 80)
    print("HOÀN THÀNH PHÂN TÍCH")
    print("=" * 80)


if __name__ == "__main__":
    main()
