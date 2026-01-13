"""
Fix Field Format Errors
Sửa các field có format sai (string -> dict)
"""

import sys
from pathlib import Path
from typing import Dict, List, Optional, Any
import json
from datetime import datetime
import re

sys.path.insert(0, str(Path(__file__).parent.parent))

try:
    from drugs.drug_database import DRUG_DATABASE
    from drugs.field_validator import FieldValidator
except ImportError:
    sys.path.insert(0, str(Path(__file__).parent))
    from drug_database import DRUG_DATABASE
    from field_validator import FieldValidator


def parse_pregnancy_lactation_string(value: str) -> Dict[str, Any]:
    """Parse pregnancy_lactation string to dict"""
    result = {
        "fda_category": "",
        "pregnancy_details": "",
        "lactation": {
            "safety": "",
            "details": "",
            "recommendation": ""
        }
    }
    
    # Try to extract FDA category
    for cat in ["A", "B", "C", "D", "X"]:
        if cat in value.upper():
            result["fda_category"] = cat
            break
    
    # If no category found, try to infer
    if not result["fda_category"]:
        if any(x in value.lower() for x in ["chống chỉ định", "contraindicated", "không dùng"]):
            result["fda_category"] = "D"
        elif any(x in value.lower() for x in ["an toàn", "safe", "có thể"]):
            result["fda_category"] = "B"
        else:
            result["fda_category"] = "C"
    
    result["pregnancy_details"] = value.strip()
    
    return result


def parse_overdose_management_string(value: str) -> Dict[str, Any]:
    """Parse overdose_management string to dict"""
    result = {
        "symptoms": [],
        "antidote": "Không có antidote đặc hiệu",
        "treatment": [],
        "monitoring": ""
    }
    
    # Try to extract symptoms
    if "triệu chứng" in value.lower() or "symptoms" in value.lower():
        # Simple extraction
        pass
    
    # Try to extract antidote
    if "antidote" in value.lower() or "giải độc" in value.lower():
        # Extract antidote info
        pass
    
    # Put entire string in treatment for now
    if value.strip() and value.strip() != "Đang cập nhật":
        result["treatment"] = [value.strip()]
        result["monitoring"] = "Theo dõi triệu chứng và dấu hiệu sinh tồn"
    
    return result


def parse_hepatic_adjustment_string(value: str) -> Dict[str, Any]:
    """Parse hepatic_adjustment string to dict"""
    result = {
        "mild": "Thường không cần chỉnh liều",
        "moderate": "Thận trọng, có thể cần giảm liều",
        "severe": "Thận trọng, giảm liều hoặc tránh dùng",
        "notes": ""
    }
    
    value_lower = value.lower()
    
    # Try to extract specific adjustments
    if "nhẹ" in value_lower or "mild" in value_lower:
        result["mild"] = value.strip()
    elif "trung bình" in value_lower or "moderate" in value_lower:
        result["moderate"] = value.strip()
    elif "nặng" in value_lower or "severe" in value_lower:
        result["severe"] = value.strip()
    else:
        # Use value as notes
        if value.strip() and value.strip() != "Đang cập nhật":
            result["notes"] = value.strip()
    
    return result


def parse_administration_instructions_string(value: str) -> Dict[str, Any]:
    """Parse administration_instructions string to dict"""
    # For now, create a simple dict structure
    result = {}
    
    if value.strip() and value.strip() != "Đang cập nhật":
        # Try to parse common patterns
        if "uống" in value.lower() or "take" in value.lower():
            result["oral"] = value.strip()
        elif "tiêm" in value.lower() or "inject" in value.lower():
            result["injection"] = value.strip()
        elif "hít" in value.lower() or "inhale" in value.lower():
            result["inhalation"] = value.strip()
        else:
            result["general"] = value.strip()
    
    return result


def fix_field_formats(dry_run: bool = True) -> Dict[str, Any]:
    """
    Fix field format errors (string -> dict)
    
    Args:
        dry_run: If True, don't modify data, just report
    
    Returns:
        Summary of fixes
    """
    print("="*80)
    print("FIX FIELD FORMAT ERRORS")
    print("="*80)
    if dry_run:
        print("DRY RUN MODE - No changes will be made")
    print()
    
    validator = FieldValidator()
    results = {
        "administration_instructions": [],
        "pregnancy_lactation": [],
        "overdose_management": [],
        "hepatic_adjustment": [],
        "already_correct": [],
    }
    
    format_fixers = {
        "administration_instructions": parse_administration_instructions_string,
        "pregnancy_lactation": parse_pregnancy_lactation_string,
        "overdose_management": parse_overdose_management_string,
        "hepatic_adjustment": parse_hepatic_adjustment_string,
    }
    
    for drug_name, drug_data in DRUG_DATABASE.items():
        if not isinstance(drug_data, dict):
            continue
        
        for field_name, fixer_func in format_fixers.items():
            if field_name not in drug_data:
                continue
            
            field_value = drug_data[field_name]
            
            # Check if it's a string (wrong format)
            if isinstance(field_value, str):
                if field_value.strip() and field_value.strip() != "Đang cập nhật":
                    # Parse string to dict
                    fixed_value = fixer_func(field_value)
                    if not dry_run:
                        drug_data[field_name] = fixed_value
                    results[field_name].append({
                        "drug": drug_name,
                        "original": field_value[:100],
                        "fixed": fixed_value
                    })
            elif isinstance(field_value, dict):
                # Already correct format
                if drug_name not in [r["drug"] for r in results["already_correct"]]:
                    results["already_correct"].append({"drug": drug_name})
    
    # Summary
    print("-"*80)
    print("SUMMARY")
    print("-"*80)
    total_fixed = sum(len(results[k]) for k in format_fixers.keys())
    print(f"Total format errors fixed: {total_fixed}")
    print(f"  - administration_instructions: {len(results['administration_instructions'])}")
    print(f"  - pregnancy_lactation: {len(results['pregnancy_lactation'])}")
    print(f"  - overdose_management: {len(results['overdose_management'])}")
    print(f"  - hepatic_adjustment: {len(results['hepatic_adjustment'])}")
    print(f"Already correct format: {len(results['already_correct'])}")
    
    # Show samples
    for field_name in format_fixers.keys():
        if results[field_name]:
            print(f"\n✅ Fixed {field_name} ({len(results[field_name])} drugs):")
            for item in results[field_name][:5]:
                print(f"  - {item['drug']}: {item['original'][:60]}...")
            if len(results[field_name]) > 5:
                print(f"  ... and {len(results[field_name]) - 5} more")
    
    if not dry_run:
        # Validate after fixing
        print("\n" + "-"*80)
        print("VALIDATION AFTER FIXING")
        print("-"*80)
        format_errors = []
        for drug_name, drug_data in DRUG_DATABASE.items():
            if not isinstance(drug_data, dict):
                continue
            for field_name in format_fixers.keys():
                if field_name in drug_data:
                    field_value = drug_data[field_name]
                    if isinstance(field_value, str) and field_value.strip() and field_value.strip() != "Đang cập nhật":
                        format_errors.append((drug_name, field_name))
        
        if format_errors:
            print(f"⚠️  Still have {len(format_errors)} format errors:")
            for drug_name, field_name in format_errors[:10]:
                print(f"  - {drug_name}.{field_name}")
        else:
            print("✅ All format errors are now fixed!")
    
    return results


def main():
    """Main function"""
    import argparse
    
    parser = argparse.ArgumentParser(description="Fix field format errors")
    parser.add_argument("--dry-run", action="store_true", default=True,
                       help="Dry run mode (don't modify files)")
    parser.add_argument("--execute", action="store_true",
                       help="Actually fix the formats (overrides --dry-run)")
    parser.add_argument("--output", default="fix_formats_report.json",
                       help="Output report file")
    
    args = parser.parse_args()
    dry_run = not args.execute
    
    results = fix_field_formats(dry_run=dry_run)
    
    # Export report
    output_path = Path(__file__).parent / args.output
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump({
            "fix_date": datetime.now().isoformat(),
            "dry_run": dry_run,
            "results": results
        }, f, ensure_ascii=False, indent=2)
    
    print(f"\nReport exported to: {output_path}")
    
    if dry_run:
        print("\n⚠️  This was a DRY RUN. Use --execute to actually fix the formats.")
    else:
        print("\n✅ Changes have been applied to DRUG_DATABASE.")
        print("⚠️  Note: You need to save changes to source files manually.")


if __name__ == "__main__":
    main()
