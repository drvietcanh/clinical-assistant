#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Fix Format Errors - Detailed
Sửa lỗi format chi tiết: chuyển string thành dict cho các field cần dict
"""

import sys
from pathlib import Path
from typing import Dict, List, Any
import json
import re

# Add project root to path
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    from drugs.drug_database import DRUG_DATABASE
except ImportError:
    sys.path.insert(0, str(Path(__file__).parent))
    from drug_database import DRUG_DATABASE


def convert_pregnancy_lactation_string(value: str) -> Dict[str, Any]:
    """Chuyển đổi pregnancy_lactation từ string sang dict"""
    # Try to extract FDA category
    fda_category = "C"
    for cat in ["A", "B", "C", "D", "X"]:
        if f"category {cat}" in value.lower() or f"category {cat.lower()}" in value.lower():
            fda_category = cat
            break
        elif value.upper().startswith(cat):
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


def convert_hepatic_adjustment_string(value: str) -> Dict[str, Any]:
    """Chuyển đổi hepatic_adjustment từ string sang dict"""
    return {
        "mild": value if value else "Thận trọng",
        "moderate": value if value else "Giảm liều",
        "severe": value if value else "CHỐNG CHỈ ĐỊNH",
        "notes": value if value else "Điều chỉnh liều theo chức năng gan"
    }


def convert_overdose_management_string(value: str) -> Dict[str, Any]:
    """Chuyển đổi overdose_management từ string sang dict"""
    return {
        "symptoms": ["Triệu chứng quá liều"],
        "antidote": "Không có antidote đặc hiệu",
        "treatment": [value if value else "Điều trị hỗ trợ"],
        "monitoring": "Theo dõi dấu hiệu sống và triệu chứng"
    }


def convert_administration_instructions_string(value: str) -> Dict[str, Any]:
    """Chuyển đổi administration_instructions từ string sang dict"""
    return {
        "oral": {
            "with_food": value if value else "Theo chỉ định của bác sĩ",
            "timing": "Theo chỉ định"
        }
    }


def fix_format_errors_detailed(dry_run: bool = True) -> Dict[str, Any]:
    """Sửa lỗi format chi tiết"""
    print("=" * 80)
    print("SỬA LỖI FORMAT CHI TIẾT")
    print("=" * 80)
    if dry_run:
        print("DRY RUN MODE - Không sửa dữ liệu")
    print()
    
    results = {
        "total_checked": 0,
        "fixed": [],
        "needs_manual_review": [],
    }
    
    conversion_functions = {
        "pregnancy_lactation": convert_pregnancy_lactation_string,
        "hepatic_adjustment": convert_hepatic_adjustment_string,
        "overdose_management": convert_overdose_management_string,
        "administration_instructions": convert_administration_instructions_string,
    }
    
    for drug_name, drug_data in DRUG_DATABASE.items():
        if not isinstance(drug_data, dict):
            continue
        
        results["total_checked"] += 1
        drug_fixed = []
        
        for field, convert_func in conversion_functions.items():
            if field not in drug_data:
                continue
            
            value = drug_data[field]
            
            # Check if it's a string but should be dict
            if isinstance(value, str) and value.strip() and value != "Đang cập nhật":
                if not dry_run:
                    drug_data[field] = convert_func(value)
                drug_fixed.append(field)
        
        if drug_fixed:
            results["fixed"].append({
                "drug": drug_name,
                "fields": drug_fixed
            })
    
    print(f"✅ Đã sửa format: {len(results['fixed'])} thuốc")
    print()
    
    if results["fixed"]:
        print("📋 Danh sách thuốc đã sửa:")
        for item in results["fixed"][:20]:
            print(f"  - {item['drug']}: {', '.join(item['fields'])}")
        if len(results["fixed"]) > 20:
            print(f"  ... và {len(results['fixed']) - 20} thuốc khác")
    
    return results


def main():
    """Main function"""
    import argparse
    
    parser = argparse.ArgumentParser(description="Sửa lỗi format chi tiết")
    parser.add_argument("--dry-run", action="store_true", default=True,
                       help="Dry run mode")
    parser.add_argument("--execute", action="store_true",
                       help="Thực sự sửa")
    
    args = parser.parse_args()
    dry_run = not args.execute
    
    results = fix_format_errors_detailed(dry_run=dry_run)
    
    if dry_run:
        print("\n⚠️  Đây là DRY RUN. Sử dụng --execute để thực sự sửa.")
    else:
        print("\n✅ Đã sửa lỗi format cho các field.")


if __name__ == "__main__":
    main()
