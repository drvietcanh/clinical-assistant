#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Comprehensive Drug Audit
Kiểm tra toàn diện dữ liệu thuốc để phát hiện lỗi tiềm ẩn và thiếu field quan trọng
"""

import sys
from pathlib import Path
from typing import Dict, List, Any, Set, Tuple
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
        FIELD_TYPES,
    )
except ImportError:
    sys.path.insert(0, str(Path(__file__).parent))
    from drug_database import DRUG_DATABASE, TOTAL_DRUGS
    from field_validator import (
        STANDARD_14_FIELDS,
        ADDITIONAL_8_FIELDS,
        ADDITIONAL_COMMON_FIELDS,
        FIELD_TYPES,
    )


def is_field_name(key: str) -> bool:
    """Kiểm tra xem key có phải là tên field không (không phải tên thuốc)"""
    field_names = (
        STANDARD_14_FIELDS + 
        ADDITIONAL_8_FIELDS + 
        ADDITIONAL_COMMON_FIELDS +
        ["administration_instructions", "contraindications_detail", "renal_adjustment"]
    )
    return key.lower() in [f.lower() for f in field_names]


def check_invalid_entries() -> List[str]:
    """Kiểm tra các entry không hợp lệ trong DRUG_DATABASE"""
    invalid = []
    
    for key in DRUG_DATABASE.keys():
        # Check if key is a field name, not a drug name
        if is_field_name(key):
            invalid.append(key)
        # Check if value is not a dict
        elif not isinstance(DRUG_DATABASE[key], dict):
            invalid.append(key)
    
    return invalid


def check_missing_critical_fields() -> Dict[str, List[str]]:
    """Kiểm tra các field quan trọng còn thiếu"""
    critical_fields = [
        "group", "vietnamese_name", "administration", "indications", 
        "dosage", "side_effects", "contraindications", "pregnancy"
    ]
    
    missing = defaultdict(list)
    
    for drug_name, drug_data in DRUG_DATABASE.items():
        if not isinstance(drug_data, dict):
            continue
        if is_field_name(drug_name):
            continue
        
        for field in critical_fields:
            if field not in drug_data:
                missing[field].append(drug_name)
            elif isinstance(drug_data[field], str) and not drug_data[field].strip():
                missing[field].append(drug_name)
            elif isinstance(drug_data[field], (list, dict)) and len(drug_data[field]) == 0:
                missing[field].append(drug_name)
    
    return dict(missing)


def check_format_errors() -> Dict[str, List[Tuple[str, str]]]:
    """Kiểm tra lỗi format (field có type sai)"""
    format_errors = defaultdict(list)
    
    for drug_name, drug_data in DRUG_DATABASE.items():
        if not isinstance(drug_data, dict):
            continue
        if is_field_name(drug_name):
            continue
        
        for field, expected_type in FIELD_TYPES.items():
            if field not in drug_data:
                continue
            
            value = drug_data[field]
            
            # Check type
            if isinstance(expected_type, tuple):
                if not any(isinstance(value, t) for t in expected_type):
                    format_errors[drug_name].append((
                        field, 
                        f"Expected {expected_type}, got {type(value).__name__}"
                    ))
            else:
                if not isinstance(value, expected_type):
                    # Special cases
                    if expected_type == type(None) and value is None:
                        continue
                    format_errors[drug_name].append((
                        field,
                        f"Expected {expected_type.__name__}, got {type(value).__name__}"
                    ))
    
    return dict(format_errors)


def check_empty_important_fields() -> Dict[str, List[str]]:
    """Kiểm tra các field quan trọng còn rỗng"""
    important_fields = [
        "pregnancy", "black_box_warnings", "storage", 
        "administration_instructions", "pregnancy_lactation"
    ]
    
    empty = defaultdict(list)
    
    for drug_name, drug_data in DRUG_DATABASE.items():
        if not isinstance(drug_data, dict):
            continue
        if is_field_name(drug_name):
            continue
        
        for field in important_fields:
            if field not in drug_data:
                continue
            
            value = drug_data[field]
            
            # Check if empty
            if value is None:
                if field != "black_box_warnings" and field != "reversal_agents":
                    empty[field].append(drug_name)
            elif isinstance(value, str):
                if not value.strip() or value.strip() == "Đang cập nhật":
                    empty[field].append(drug_name)
            elif isinstance(value, (list, dict)):
                if len(value) == 0:
                    empty[field].append(drug_name)
    
    return dict(empty)


def comprehensive_audit() -> Dict[str, Any]:
    """Kiểm tra toàn diện"""
    print("=" * 80)
    print("KIỂM TRA TOÀN DIỆN DỮ LIỆU THUỐC")
    print("=" * 80)
    print(f"Tổng số entries: {len(DRUG_DATABASE)}")
    print()
    
    results = {
        "audit_date": datetime.now().isoformat(),
        "total_entries": len(DRUG_DATABASE),
        "invalid_entries": [],
        "missing_critical_fields": {},
        "format_errors": {},
        "empty_important_fields": {},
        "summary": {},
    }
    
    # 1. Check invalid entries
    print("1. Kiểm tra entries không hợp lệ...")
    invalid = check_invalid_entries()
    results["invalid_entries"] = invalid
    print(f"   ✅ Tìm thấy {len(invalid)} entries không hợp lệ: {', '.join(invalid)}")
    print()
    
    # 2. Check missing critical fields
    print("2. Kiểm tra field quan trọng còn thiếu...")
    missing = check_missing_critical_fields()
    results["missing_critical_fields"] = missing
    for field, drugs in missing.items():
        print(f"   ⚠️  {field}: {len(drugs)} thuốc thiếu")
    print()
    
    # 3. Check format errors
    print("3. Kiểm tra lỗi format...")
    format_errors = check_format_errors()
    results["format_errors"] = format_errors
    print(f"   ⚠️  {len(format_errors)} thuốc có lỗi format")
    print()
    
    # 4. Check empty important fields
    print("4. Kiểm tra field quan trọng còn rỗng...")
    empty = check_empty_important_fields()
    results["empty_important_fields"] = empty
    for field, drugs in empty.items():
        print(f"   ⚠️  {field}: {len(drugs)} thuốc rỗng")
    print()
    
    # Summary
    valid_drugs = len(DRUG_DATABASE) - len(invalid)
    drugs_with_missing = len(set(
        drug for drugs in missing.values() for drug in drugs
    ))
    drugs_with_format_errors = len(format_errors)
    drugs_with_empty = len(set(
        drug for drugs in empty.values() for drug in drugs
    ))
    
    results["summary"] = {
        "valid_drugs": valid_drugs,
        "invalid_entries": len(invalid),
        "drugs_with_missing_critical_fields": drugs_with_missing,
        "drugs_with_format_errors": drugs_with_format_errors,
        "drugs_with_empty_important_fields": drugs_with_empty,
    }
    
    print("=" * 80)
    print("TÓM TẮT")
    print("=" * 80)
    print(f"Thuốc hợp lệ: {valid_drugs}")
    print(f"Entries không hợp lệ: {len(invalid)}")
    print(f"Thuốc thiếu field quan trọng: {drugs_with_missing}")
    print(f"Thuốc có lỗi format: {drugs_with_format_errors}")
    print(f"Thuốc có field quan trọng rỗng: {drugs_with_empty}")
    
    return results


def export_audit_report(results: Dict[str, Any], output_file: str = "comprehensive_drug_audit.json"):
    """Xuất báo cáo kiểm tra"""
    output_path = project_root / "drugs" / output_file
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(results, f, ensure_ascii=False, indent=2)
    print(f"\n✅ Đã xuất báo cáo: {output_path}")
    
    # Human-readable report
    report_path = project_root / "drugs" / "comprehensive_drug_audit_report.txt"
    with open(report_path, 'w', encoding='utf-8') as f:
        f.write("=" * 80 + "\n")
        f.write("BÁO CÁO KIỂM TRA TOÀN DIỆN DỮ LIỆU THUỐC\n")
        f.write("=" * 80 + "\n\n")
        f.write(f"Ngày kiểm tra: {results['audit_date']}\n")
        f.write(f"Tổng số entries: {results['total_entries']}\n\n")
        
        f.write("1. ENTRIES KHÔNG HỢP LỆ:\n")
        f.write("-" * 80 + "\n")
        if results['invalid_entries']:
            for entry in results['invalid_entries']:
                f.write(f"  - {entry}\n")
        else:
            f.write("  Không có\n")
        f.write("\n")
        
        f.write("2. THUỐC THIẾU FIELD QUAN TRỌNG:\n")
        f.write("-" * 80 + "\n")
        for field, drugs in results['missing_critical_fields'].items():
            f.write(f"\n{field} ({len(drugs)} thuốc):\n")
            for drug in drugs[:20]:
                f.write(f"  - {drug}\n")
            if len(drugs) > 20:
                f.write(f"  ... và {len(drugs) - 20} thuốc khác\n")
        f.write("\n")
        
        f.write("3. LỖI FORMAT:\n")
        f.write("-" * 80 + "\n")
        for drug, errors in list(results['format_errors'].items())[:30]:
            f.write(f"\n{drug}:\n")
            for field, error_msg in errors:
                f.write(f"  - {field}: {error_msg}\n")
        f.write("\n")
        
        f.write("4. FIELD QUAN TRỌNG CÒN RỖNG:\n")
        f.write("-" * 80 + "\n")
        for field, drugs in results['empty_important_fields'].items():
            f.write(f"\n{field} ({len(drugs)} thuốc):\n")
            for drug in drugs[:20]:
                f.write(f"  - {drug}\n")
            if len(drugs) > 20:
                f.write(f"  ... và {len(drugs) - 20} thuốc khác\n")
    
    print(f"✅ Đã xuất báo cáo text: {report_path}")


def main():
    """Main function"""
    results = comprehensive_audit()
    export_audit_report(results)


if __name__ == "__main__":
    main()
