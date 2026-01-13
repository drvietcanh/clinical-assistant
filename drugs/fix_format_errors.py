#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Fix Format Errors
Sửa lỗi format cho các field có type sai (chuyển string thành dict)
"""

import sys
from pathlib import Path
from typing import Dict, List, Any
import json
from datetime import datetime

# Add project root to path
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    from drugs.drug_database import DRUG_DATABASE
    from drugs.field_validator import FIELD_TYPES
except ImportError:
    sys.path.insert(0, str(Path(__file__).parent))
    from drug_database import DRUG_DATABASE
    from field_validator import FIELD_TYPES


def convert_string_to_dict(field_name: str, value: str) -> Dict[str, Any]:
    """Chuyển đổi string thành dict structure phù hợp"""
    if field_name == "administration_instructions":
        return {
            "oral": {
                "with_food": value if value else "Theo chỉ định của bác sĩ",
                "timing": "Theo chỉ định"
            }
        }
    elif field_name == "pregnancy_lactation":
        # Try to extract FDA category from string
        fda_category = "C"
        if "category" in value.lower() or "fda" in value.lower():
            # Try to find category
            for cat in ["A", "B", "C", "D", "X"]:
                if cat in value.upper():
                    fda_category = cat
                    break
        
        return {
            "fda_category": fda_category,
            "pregnancy_details": value if value else "Đang cập nhật",
            "lactation": {
                "safety": "Unknown",
                "details": "Đang cập nhật",
                "recommendation": "Tham khảo ý kiến bác sĩ"
            }
        }
    elif field_name == "overdose_management":
        return {
            "symptoms": ["Triệu chứng quá liều"],
            "antidote": "Không có antidote đặc hiệu",
            "treatment": [value if value else "Điều trị hỗ trợ"],
            "monitoring": "Theo dõi dấu hiệu sống và triệu chứng"
        }
    elif field_name == "hepatic_adjustment":
        return {
            "mild": value if value else "Thận trọng",
            "moderate": value if value else "Giảm liều",
            "severe": value if value else "CHỐNG CHỈ ĐỊNH",
            "notes": "Điều chỉnh liều theo chức năng gan"
        }
    else:
        return {"value": value}


def fix_format_errors(dry_run: bool = True) -> Dict[str, Any]:
    """Sửa lỗi format cho các thuốc"""
    print("=" * 80)
    print("SỬA LỖI FORMAT")
    print("=" * 80)
    if dry_run:
        print("DRY RUN MODE - Không sửa dữ liệu")
    print()
    
    results = {
        "total_checked": 0,
        "format_errors_found": [],
        "fixed": [],
        "needs_manual_review": [],
    }
    
    # Fields that should be dict but might be string
    dict_fields = [
        "administration_instructions",
        "pregnancy_lactation",
        "overdose_management",
        "hepatic_adjustment",
    ]
    
    for drug_name, drug_data in DRUG_DATABASE.items():
        if not isinstance(drug_data, dict):
            continue
        
        results["total_checked"] += 1
        drug_errors = []
        
        for field in dict_fields:
            if field not in drug_data:
                continue
            
            value = drug_data[field]
            expected_type = FIELD_TYPES.get(field)
            
            # Check if type is wrong
            if expected_type and isinstance(expected_type, tuple):
                if not any(isinstance(value, t) for t in expected_type):
                    if isinstance(value, str) and value.strip():
                        drug_errors.append({
                            "field": field,
                            "current_type": "str",
                            "expected_type": "dict",
                            "value": value[:100] if len(value) > 100 else value
                        })
            elif expected_type and not isinstance(value, expected_type):
                if isinstance(value, str) and value.strip():
                    drug_errors.append({
                        "field": field,
                        "current_type": "str",
                        "expected_type": "dict",
                        "value": value[:100] if len(value) > 100 else value
                    })
        
        if drug_errors:
            results["format_errors_found"].append({
                "drug": drug_name,
                "errors": drug_errors
            })
            
            # Try to fix automatically
            can_fix = True
            for error in drug_errors:
                field = error["field"]
                value = drug_data[field]
                
                if isinstance(value, str) and value.strip() and value != "Đang cập nhật":
                    if not dry_run:
                        drug_data[field] = convert_string_to_dict(field, value)
                    results["fixed"].append({
                        "drug": drug_name,
                        "field": field
                    })
                else:
                    can_fix = False
            
            if not can_fix:
                results["needs_manual_review"].append({
                    "drug": drug_name,
                    "errors": drug_errors
                })
    
    print(f"📋 Tìm thấy {len(results['format_errors_found'])} thuốc có lỗi format")
    print(f"✅ Có thể sửa tự động: {len(results['fixed'])} field")
    print(f"⚠️  Cần xem xét thủ công: {len(results['needs_manual_review'])} thuốc")
    print()
    
    if results["fixed"]:
        print("📋 Danh sách field đã được sửa:")
        fixed_by_drug = {}
        for item in results["fixed"]:
            drug = item["drug"]
            if drug not in fixed_by_drug:
                fixed_by_drug[drug] = []
            fixed_by_drug[drug].append(item["field"])
        
        for drug, fields in list(fixed_by_drug.items())[:20]:
            print(f"  - {drug}: {', '.join(fields)}")
        if len(fixed_by_drug) > 20:
            print(f"  ... và {len(fixed_by_drug) - 20} thuốc khác")
    
    return results


def export_fix_report(results: Dict[str, Any], output_file: str = "format_fix_report.json"):
    """Xuất báo cáo"""
    output_path = project_root / "drugs" / output_file
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(results, f, ensure_ascii=False, indent=2)
    print(f"\n✅ Đã xuất báo cáo: {output_path}")


def main():
    """Main function"""
    import argparse
    
    parser = argparse.ArgumentParser(description="Sửa lỗi format")
    parser.add_argument("--dry-run", action="store_true", default=True,
                       help="Dry run mode")
    parser.add_argument("--execute", action="store_true",
                       help="Thực sự sửa")
    
    args = parser.parse_args()
    dry_run = not args.execute
    
    results = fix_format_errors(dry_run=dry_run)
    export_fix_report(results)
    
    if dry_run:
        print("\n⚠️  Đây là DRY RUN. Sử dụng --execute để thực sự sửa.")
    else:
        print("\n✅ Đã sửa lỗi format cho các field có thể tự động.")
        print("⚠️  Cần xem xét thủ công các thuốc còn lại.")


if __name__ == "__main__":
    main()
