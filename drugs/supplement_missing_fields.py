"""
Supplement Missing Fields Script
Bổ sung các field thiếu cho thuốc trong database
"""

import sys
from pathlib import Path
from typing import Dict, List, Set, Optional, Any
import copy
import json
from datetime import datetime

# Add parent directory to path
sys.path.insert(0, str(Path(__file__).parent.parent))

try:
    from drugs.drug_database import DRUG_DATABASE
    from drugs.field_validator import (
        STANDARD_14_FIELDS,
        ADDITIONAL_8_FIELDS,
        ALL_FIELDS,
    )
    from drugs.field_standardizer import FieldStandardizer
except ImportError:
    sys.path.insert(0, str(Path(__file__).parent))
    from drug_database import DRUG_DATABASE
    from field_validator import (
        STANDARD_14_FIELDS,
        ADDITIONAL_8_FIELDS,
        ALL_FIELDS,
    )
    from field_standardizer import FieldStandardizer

# Additional common fields
ADDITIONAL_COMMON_FIELDS = [
    "renal_adjustment",
    "contraindications_detail",
]

ALL_FIELDS_INCLUDING_COMMON = ALL_FIELDS + ADDITIONAL_COMMON_FIELDS


# Default templates for fields
FIELD_TEMPLATES = {
    "black_box_warnings": None,  # Will be set to None if not applicable
    "drug_interactions": {
        "major": [],
        "moderate": [],
        "minor": [],
    },
    "pregnancy_lactation": {
        "fda_category": "",
        "pregnancy_details": "",
        "lactation": {
            "safety": "",
            "details": "",
            "recommendation": ""
        }
    },
    "hepatic_adjustment": {
        "mild": "Thường không cần chỉnh liều",
        "moderate": "Thận trọng, có thể cần giảm liều",
        "severe": "Thận trọng, giảm liều hoặc tránh dùng",
        "notes": ""
    },
    "overdose_management": {
        "symptoms": [],
        "antidote": "Không có antidote đặc hiệu",
        "treatment": [],
        "monitoring": ""
    },
    "reversal_agents": {
        "available": False,
        "agents": [],
        "notes": ""
    },
    "administration_instructions": {},
    "references": {
        "primary_sources": [],
        "last_updated": "",
        "evidence_level": ""
    },
    "renal_adjustment": {
        "normal": "Không cần chỉnh liều",
        "30_60": "Thận trọng, có thể cần giảm liều",
        "under_30": "Thận trọng, giảm liều",
        "dialysis": "Thận trọng, giảm liều",
        "notes": ""
    },
    "contraindications_detail": {
        "tuyệt_đối": [],
        "tương_đối": []
    },
}


def is_field_empty(field_value: Any) -> bool:
    """Check if a field value is considered empty"""
    if field_value is None:
        return True
    if isinstance(field_value, str):
        return field_value.strip() == "" or field_value.strip() == "Đang cập nhật"
    if isinstance(field_value, list):
        return len(field_value) == 0 or (len(field_value) == 1 and isinstance(field_value[0], str) and field_value[0].strip() == "Đang cập nhật")
    if isinstance(field_value, dict):
        if len(field_value) == 0:
            return True
        # Check if all values are empty/placeholder
        all_empty = True
        for v in field_value.values():
            if isinstance(v, str) and v.strip() and v.strip() != "Đang cập nhật":
                all_empty = False
                break
            elif isinstance(v, (list, dict)) and len(v) > 0:
                # Check if list/dict has real content
                if isinstance(v, list):
                    if any(isinstance(item, str) and item.strip() and item.strip() != "Đang cập nhật" for item in v):
                        all_empty = False
                        break
                elif isinstance(v, dict):
                    if any(str(val).strip() and str(val).strip() != "Đang cập nhật" for val in v.values()):
                        all_empty = False
                        break
            elif not isinstance(v, (str, list, dict)) and v:
                all_empty = False
                break
        return all_empty
    return False


def convert_contraindications_to_detail(contraindications: Any) -> Dict[str, List[str]]:
    """Convert simple contraindications list to detailed format"""
    if isinstance(contraindications, dict):
        if "tuyệt_đối" in contraindications or "tương_đối" in contraindications:
            return contraindications
        # If it's a dict but not in the right format, try to extract
        return {
            "tuyệt_đối": [],
            "tương_đối": []
        }
    elif isinstance(contraindications, list):
        # Assume all are absolute contraindications
        return {
            "tuyệt_đối": contraindications.copy(),
            "tương_đối": []
        }
    else:
        return {
            "tuyệt_đối": [],
            "tương_đối": []
        }


def supplement_drug_fields(drug_name: str, drug_data: Dict[str, Any], 
                          dry_run: bool = True) -> Dict[str, Any]:
    """
    Supplement missing fields for a single drug
    
    Args:
        drug_name: Name of the drug
        drug_data: Drug data dictionary
        dry_run: If True, don't modify the data, just return what would be added
    
    Returns:
        Dict with information about what was added/modified
    """
    if not isinstance(drug_data, dict):
        return {
            "drug_name": drug_name,
            "error": "Not a valid drug dict",
            "added_fields": [],
            "modified_fields": [],
            "total_changes": 0,
            "changes": {}
        }
    
    added_fields = []
    modified_fields = []
    changes = {}
    
    # Check and add missing fields
    for field in ALL_FIELDS_INCLUDING_COMMON:
        if field not in drug_data:
            # Field is missing
            if field in FIELD_TEMPLATES:
                template = FIELD_TEMPLATES[field]
                if not dry_run:
                    drug_data[field] = copy.deepcopy(template)
                added_fields.append(field)
                changes[field] = "added"
            else:
                # No template, use default based on type
                if field in STANDARD_14_FIELDS:
                    if field in ["group", "vietnamese_name", "pregnancy", "mechanism_of_action", "storage"]:
                        default_value = ""
                    elif field in ["administration", "indications", "side_effects", "monitoring", "precautions"]:
                        default_value = []
                    elif field == "dosage":
                        default_value = {}
                    elif field == "pharmacokinetics":
                        default_value = {}
                    elif field == "contraindications":
                        default_value = []
                    elif field == "interactions":
                        default_value = []
                    else:
                        default_value = ""
                    
                    if not dry_run:
                        drug_data[field] = default_value
                    added_fields.append(field)
                    changes[field] = "added"
        
        elif is_field_empty(drug_data[field]):
            # Field exists but is empty
            if field in FIELD_TEMPLATES:
                template = FIELD_TEMPLATES[field]
                if not dry_run:
                    drug_data[field] = copy.deepcopy(template)
                modified_fields.append(field)
                changes[field] = "replaced_empty"
            elif field == "contraindications_detail":
                # Try to convert from contraindications
                if "contraindications" in drug_data:
                    detail = convert_contraindications_to_detail(drug_data["contraindications"])
                    if not dry_run:
                        drug_data[field] = detail
                    modified_fields.append(field)
                    changes[field] = "converted_from_contraindications"
    
    # Special handling for contraindications_detail
    if "contraindications_detail" not in drug_data or is_field_empty(drug_data.get("contraindications_detail")):
        if "contraindications" in drug_data and not is_field_empty(drug_data["contraindications"]):
            detail = convert_contraindications_to_detail(drug_data["contraindications"])
            if not dry_run:
                drug_data["contraindications_detail"] = detail
            if "contraindications_detail" not in added_fields and "contraindications_detail" not in modified_fields:
                if "contraindications_detail" not in drug_data:
                    added_fields.append("contraindications_detail")
                else:
                    modified_fields.append("contraindications_detail")
                changes["contraindications_detail"] = "converted_from_contraindications"
    
    return {
        "drug_name": drug_name,
        "added_fields": added_fields,
        "modified_fields": modified_fields,
        "total_changes": len(added_fields) + len(modified_fields),
        "changes": changes
    }


def supplement_all_drugs(dry_run: bool = True, 
                         target_fields: Optional[List[str]] = None) -> Dict[str, Any]:
    """
    Supplement missing fields for all drugs
    
    Args:
        dry_run: If True, don't modify data, just report
        target_fields: If provided, only supplement these fields
    
    Returns:
        Summary of changes
    """
    print(f"Supplementing fields for {len(DRUG_DATABASE)} drugs...")
    if dry_run:
        print("DRY RUN MODE - No changes will be made")
    if target_fields:
        print(f"Target fields: {', '.join(target_fields)}")
    
    results = {}
    total_added = 0
    total_modified = 0
    drugs_changed = 0
    
    fields_to_check = target_fields if target_fields else ALL_FIELDS_INCLUDING_COMMON
    
    for drug_name, drug_data in DRUG_DATABASE.items():
        result = supplement_drug_fields(drug_name, drug_data, dry_run=dry_run)
        results[drug_name] = result
        
        if result["total_changes"] > 0:
            drugs_changed += 1
            total_added += len(result["added_fields"])
            total_modified += len(result["modified_fields"])
    
    return {
        "total_drugs": len(DRUG_DATABASE),
        "drugs_changed": drugs_changed,
        "total_fields_added": total_added,
        "total_fields_modified": total_modified,
        "dry_run": dry_run,
        "results": results
    }


def main():
    """Main function"""
    import argparse
    
    parser = argparse.ArgumentParser(description="Supplement missing drug fields")
    parser.add_argument("--dry-run", action="store_true", default=True,
                       help="Dry run mode (don't modify files)")
    parser.add_argument("--execute", action="store_true",
                       help="Actually modify the database (overrides --dry-run)")
    parser.add_argument("--fields", nargs="+",
                       help="Specific fields to supplement (default: all)")
    parser.add_argument("--output", default="supplement_report.json",
                       help="Output report file")
    
    args = parser.parse_args()
    
    dry_run = not args.execute
    
    print("="*80)
    print("SUPPLEMENT MISSING FIELDS")
    print("="*80)
    
    # Supplement fields
    summary = supplement_all_drugs(dry_run=dry_run, target_fields=args.fields)
    
    # Print summary
    print("\n" + "-"*80)
    print("SUMMARY")
    print("-"*80)
    print(f"Total drugs: {summary['total_drugs']}")
    print(f"Drugs changed: {summary['drugs_changed']}")
    print(f"Fields added: {summary['total_fields_added']}")
    print(f"Fields modified: {summary['total_fields_modified']}")
    
    if dry_run:
        print("\nThis was a DRY RUN. Use --execute to actually make changes.")
    else:
        print("\nChanges have been applied to DRUG_DATABASE.")
        print("Note: You need to save the changes to files manually.")
    
    # Export report
    output_path = Path(__file__).parent / args.output
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(summary, f, ensure_ascii=False, indent=2)
    print(f"\nReport exported to: {output_path}")
    
    # Show top drugs that need attention
    print("\n" + "-"*80)
    print("TOP 20 DRUGS WITH MOST MISSING FIELDS")
    print("-"*80)
    sorted_results = sorted(
        [(name, result) for name, result in summary["results"].items() if result["total_changes"] > 0],
        key=lambda x: x[1]["total_changes"],
        reverse=True
    )
    
    for i, (drug_name, result) in enumerate(sorted_results[:20], 1):
        print(f"{i}. {drug_name}: {result['total_changes']} changes "
              f"(+{len(result['added_fields'])} added, ~{len(result['modified_fields'])} modified)")


if __name__ == "__main__":
    main()
