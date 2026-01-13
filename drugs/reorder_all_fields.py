"""
Reorder All Fields
Sắp xếp lại thứ tự fields theo chuẩn cho tất cả thuốc
"""

import sys
from pathlib import Path
from typing import Dict, List, Any
import json
from datetime import datetime
from collections import OrderedDict

sys.path.insert(0, str(Path(__file__).parent.parent))

try:
    from drugs.drug_database import DRUG_DATABASE
    from drugs.field_validator import (
        STANDARD_14_FIELDS,
        ADDITIONAL_8_FIELDS,
        ALL_FIELDS_WITH_COMMON,
    )
    from drugs.field_standardizer import FieldStandardizer
except ImportError:
    sys.path.insert(0, str(Path(__file__).parent))
    from drug_database import DRUG_DATABASE
    from field_validator import (
        STANDARD_14_FIELDS,
        ADDITIONAL_8_FIELDS,
        ALL_FIELDS_WITH_COMMON,
    )
    from field_standardizer import FieldStandardizer


def reorder_drug_fields(drug_data: Dict[str, Any]) -> Dict[str, Any]:
    """Reorder fields according to standard order"""
    ordered = OrderedDict()
    
    # Add standard fields in order
    for field in STANDARD_14_FIELDS:
        if field in drug_data:
            ordered[field] = drug_data[field]
    
    # Add additional fields in order
    for field in ADDITIONAL_8_FIELDS:
        if field in drug_data:
            ordered[field] = drug_data[field]
    
    # Add common fields
    for field in ["renal_adjustment", "contraindications_detail"]:
        if field in drug_data:
            ordered[field] = drug_data[field]
    
    # Add any other fields not in standard list
    for key, value in drug_data.items():
        if key not in ordered:
            ordered[key] = value
    
    return dict(ordered)


def reorder_all_fields(dry_run: bool = True) -> Dict[str, Any]:
    """
    Reorder fields for all drugs
    
    Args:
        dry_run: If True, don't modify data, just report
    
    Returns:
        Summary of reordering
    """
    print("="*80)
    print("REORDER ALL FIELDS")
    print("="*80)
    if dry_run:
        print("DRY RUN MODE - No changes will be made")
    print()
    
    standardizer = FieldStandardizer()
    results = {
        "reordered": [],
        "already_ordered": [],
        "total_drugs": 0,
    }
    
    for drug_name, drug_data in DRUG_DATABASE.items():
        if not isinstance(drug_data, dict):
            continue
        
        results["total_drugs"] += 1
        
        # Check current order
        current_keys = list(drug_data.keys())
        standard_keys = [k for k in ALL_FIELDS_WITH_COMMON if k in current_keys]
        
        # Check if order is correct
        is_ordered = True
        last_pos = -1
        for field in ALL_FIELDS_WITH_COMMON:
            if field in current_keys:
                current_pos = current_keys.index(field)
                if current_pos < last_pos:
                    is_ordered = False
                    break
                last_pos = current_pos
        
        if is_ordered:
            results["already_ordered"].append(drug_name)
        else:
            # Reorder
            reordered_data = reorder_drug_fields(drug_data)
            if not dry_run:
                # Clear and rebuild
                drug_data.clear()
                drug_data.update(reordered_data)
            results["reordered"].append(drug_name)
    
    # Summary
    print("-"*80)
    print("SUMMARY")
    print("-"*80)
    print(f"Total drugs: {results['total_drugs']}")
    print(f"Already ordered: {len(results['already_ordered'])}")
    print(f"Reordered: {len(results['reordered'])}")
    
    if results["reordered"]:
        print(f"\n✅ Reordered {len(results['reordered'])} drugs:")
        for drug_name in results["reordered"][:20]:
            print(f"  - {drug_name}")
        if len(results["reordered"]) > 20:
            print(f"  ... and {len(results['reordered']) - 20} more")
    
    return results


def main():
    """Main function"""
    import argparse
    
    parser = argparse.ArgumentParser(description="Reorder all drug fields")
    parser.add_argument("--dry-run", action="store_true", default=True,
                       help="Dry run mode (don't modify files)")
    parser.add_argument("--execute", action="store_true",
                       help="Actually reorder fields (overrides --dry-run)")
    parser.add_argument("--output", default="reorder_fields_report.json",
                       help="Output report file")
    
    args = parser.parse_args()
    dry_run = not args.execute
    
    results = reorder_all_fields(dry_run=dry_run)
    
    # Export report
    output_path = Path(__file__).parent / args.output
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump({
            "reorder_date": datetime.now().isoformat(),
            "dry_run": dry_run,
            "results": results
        }, f, ensure_ascii=False, indent=2)
    
    print(f"\nReport exported to: {output_path}")
    
    if dry_run:
        print("\n⚠️  This was a DRY RUN. Use --execute to actually reorder fields.")
    else:
        print("\n✅ Changes have been applied to DRUG_DATABASE.")
        print("⚠️  Note: You need to save changes to source files manually.")


if __name__ == "__main__":
    main()
