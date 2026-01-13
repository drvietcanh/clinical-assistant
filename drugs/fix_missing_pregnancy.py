"""
Fix Missing Pregnancy Field
Sửa missing pregnancy field cho các thuốc thiếu
"""

import sys
from pathlib import Path
from typing import Dict, List, Optional, Any
import json
from datetime import datetime

sys.path.insert(0, str(Path(__file__).parent.parent))

try:
    from drugs.drug_database import DRUG_DATABASE
    from drugs.field_validator import FieldValidator
except ImportError:
    sys.path.insert(0, str(Path(__file__).parent))
    from drug_database import DRUG_DATABASE
    from field_validator import FieldValidator


def extract_pregnancy_from_lactation(pregnancy_lactation: Any) -> Optional[str]:
    """Extract pregnancy field from pregnancy_lactation"""
    if isinstance(pregnancy_lactation, dict):
        fda_category = pregnancy_lactation.get("fda_category", "")
        pregnancy_details = pregnancy_lactation.get("pregnancy_details", "")
        
        if fda_category:
            # Format: "Category - Description"
            if pregnancy_details:
                return f"{fda_category} - {pregnancy_details[:100]}"  # Limit length
            else:
                return fda_category
        elif pregnancy_details:
            # Try to extract category from details
            for cat in ["A", "B", "C", "D", "X"]:
                if cat in pregnancy_details.upper():
                    return f"{cat} - {pregnancy_details[:100]}"
            return pregnancy_details[:150]
    elif isinstance(pregnancy_lactation, str):
        # If it's a string, try to extract category
        for cat in ["A", "B", "C", "D", "X"]:
            if cat in pregnancy_lactation.upper():
                return pregnancy_lactation[:150]
        return pregnancy_lactation[:150]
    
    return None


def get_default_pregnancy_by_group(group: str) -> str:
    """Get default pregnancy category based on drug group"""
    group_lower = group.lower() if group else ""
    
    # ACE inhibitors, ARBs - Category D
    if any(x in group_lower for x in ["ace inhibitor", "arb", "angiotensin"]):
        return "D - Chống chỉ định trong thai kỳ"
    
    # Statins - Category X
    if "statin" in group_lower:
        return "X - Chống chỉ định trong thai kỳ"
    
    # Warfarin, anticoagulants - Category D/X
    if any(x in group_lower for x in ["warfarin", "anticoagulant", "coumarin"]):
        return "D - Chống chỉ định trong thai kỳ (nguy cơ dị tật)"
    
    # Retinoids - Category X
    if "retinoid" in group_lower or "isotretinoin" in group_lower:
        return "X - Chống chỉ định tuyệt đối trong thai kỳ"
    
    # Methotrexate - Category X
    if "methotrexate" in group_lower:
        return "X - Chống chỉ định trong thai kỳ"
    
    # Most antibiotics - Category B/C
    if "antibiotic" in group_lower or "antimicrobial" in group_lower:
        return "B/C - Thận trọng trong thai kỳ"
    
    # PPIs - Category B
    if "ppi" in group_lower or "proton pump" in group_lower:
        return "B - Có thể sử dụng trong thai kỳ"
    
    # Insulin - Category B
    if "insulin" in group_lower:
        return "B - An toàn trong thai kỳ"
    
    # Metformin - Category B
    if "metformin" in group_lower or "biguanide" in group_lower:
        return "B - Có thể sử dụng trong thai kỳ"
    
    # Default - Category C
    return "C - Thận trọng trong thai kỳ, cân nhắc lợi ích/nguy cơ"


def fix_missing_pregnancy(dry_run: bool = True) -> Dict[str, Any]:
    """
    Fix missing pregnancy field for all drugs
    
    Args:
        dry_run: If True, don't modify data, just report
    
    Returns:
        Summary of fixes
    """
    print("="*80)
    print("FIX MISSING PREGNANCY FIELD")
    print("="*80)
    if dry_run:
        print("DRY RUN MODE - No changes will be made")
    print()
    
    validator = FieldValidator()
    results = {
        "fixed_from_lactation": [],
        "fixed_from_group": [],
        "already_has": [],
        "still_missing": [],
        "invalid_entry": [],
    }
    
    for drug_name, drug_data in DRUG_DATABASE.items():
        if not isinstance(drug_data, dict):
            # Check if this is the invalid "references" entry
            if drug_name == "references":
                results["invalid_entry"].append(drug_name)
            continue
        
        # Check if pregnancy field exists and is not empty
        has_pregnancy = "pregnancy" in drug_data and drug_data["pregnancy"]
        if isinstance(drug_data.get("pregnancy"), str) and drug_data["pregnancy"].strip():
            has_pregnancy = True
        
        if has_pregnancy:
            results["already_has"].append(drug_name)
            continue
        
        # Try to extract from pregnancy_lactation
        pregnancy_value = None
        if "pregnancy_lactation" in drug_data:
            pregnancy_value = extract_pregnancy_from_lactation(drug_data["pregnancy_lactation"])
        
        if pregnancy_value:
            if not dry_run:
                drug_data["pregnancy"] = pregnancy_value
            results["fixed_from_lactation"].append({
                "drug": drug_name,
                "value": pregnancy_value
            })
        else:
            # Use default based on group
            group = drug_data.get("group", "")
            default_pregnancy = get_default_pregnancy_by_group(group)
            if not dry_run:
                drug_data["pregnancy"] = default_pregnancy
            results["fixed_from_group"].append({
                "drug": drug_name,
                "group": group,
                "value": default_pregnancy
            })
    
    # Summary
    print("-"*80)
    print("SUMMARY")
    print("-"*80)
    print(f"Total drugs checked: {len(DRUG_DATABASE)}")
    print(f"Already have pregnancy field: {len(results['already_has'])}")
    print(f"Fixed from pregnancy_lactation: {len(results['fixed_from_lactation'])}")
    print(f"Fixed from group/default: {len(results['fixed_from_group'])}")
    print(f"Invalid entries found: {len(results['invalid_entry'])}")
    
    if results["invalid_entry"]:
        print(f"\n⚠️  Invalid entries: {', '.join(results['invalid_entry'])}")
    
    if results["fixed_from_lactation"]:
        print(f"\n✅ Fixed from pregnancy_lactation ({len(results['fixed_from_lactation'])} drugs):")
        for item in results["fixed_from_lactation"][:10]:
            print(f"  - {item['drug']}: {item['value'][:60]}...")
        if len(results["fixed_from_lactation"]) > 10:
            print(f"  ... and {len(results['fixed_from_lactation']) - 10} more")
    
    if results["fixed_from_group"]:
        print(f"\n✅ Fixed from group/default ({len(results['fixed_from_group'])} drugs):")
        for item in results["fixed_from_group"][:10]:
            print(f"  - {item['drug']} ({item['group'][:40]}): {item['value'][:60]}...")
        if len(results["fixed_from_group"]) > 10:
            print(f"  ... and {len(results['fixed_from_group']) - 10} more")
    
    if not dry_run:
        # Validate after fixing
        print("\n" + "-"*80)
        print("VALIDATION AFTER FIXING")
        print("-"*80)
        validation_errors = []
        for drug_name, drug_data in DRUG_DATABASE.items():
            if not isinstance(drug_data, dict):
                continue
            validation_result = validator.validate_all_fields(drug_data)
            if not validation_result["valid"]:
                for error in validation_result["errors"]:
                    if "pregnancy" in error.lower():
                        validation_errors.append((drug_name, error))
        
        if validation_errors:
            print(f"⚠️  Still have {len(validation_errors)} pregnancy-related errors:")
            for drug_name, error in validation_errors[:10]:
                print(f"  - {drug_name}: {error}")
        else:
            print("✅ All pregnancy fields are now valid!")
    
    return results


def main():
    """Main function"""
    import argparse
    
    parser = argparse.ArgumentParser(description="Fix missing pregnancy field")
    parser.add_argument("--dry-run", action="store_true", default=True,
                       help="Dry run mode (don't modify files)")
    parser.add_argument("--execute", action="store_true",
                       help="Actually fix the fields (overrides --dry-run)")
    parser.add_argument("--output", default="fix_pregnancy_report.json",
                       help="Output report file")
    
    args = parser.parse_args()
    dry_run = not args.execute
    
    results = fix_missing_pregnancy(dry_run=dry_run)
    
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
        print("\n⚠️  This was a DRY RUN. Use --execute to actually fix the fields.")
    else:
        print("\n✅ Changes have been applied to DRUG_DATABASE.")
        print("⚠️  Note: You need to save changes to source files manually.")


if __name__ == "__main__":
    main()
