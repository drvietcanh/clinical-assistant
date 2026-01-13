"""
Validate All Drugs
Kiểm tra validation cho tất cả thuốc sau khi bổ sung fields
"""

import sys
from pathlib import Path
from typing import Dict, List, Any
from collections import defaultdict
import json
from datetime import datetime

sys.path.insert(0, str(Path(__file__).parent.parent))

try:
    from drugs.drug_database import DRUG_DATABASE, TOTAL_DRUGS
    from drugs.field_validator import FieldValidator, ALL_FIELDS_WITH_COMMON
except ImportError:
    sys.path.insert(0, str(Path(__file__).parent))
    from drug_database import DRUG_DATABASE, TOTAL_DRUGS
    from field_validator import FieldValidator, ALL_FIELDS_WITH_COMMON


def validate_all_drugs() -> Dict[str, Any]:
    """
    Validate tất cả thuốc
    
    Returns:
        Validation results summary
    """
    print(f"Validating {TOTAL_DRUGS} drugs...")
    
    validator = FieldValidator()
    results = {}
    summary = {
        "total_drugs": TOTAL_DRUGS,
        "valid_drugs": 0,
        "invalid_drugs": 0,
        "drugs_with_errors": [],
        "drugs_with_warnings": [],
        "error_types": defaultdict(int),
        "warning_types": defaultdict(int),
    }
    
    for drug_name, drug_data in DRUG_DATABASE.items():
        if not isinstance(drug_data, dict):
            continue
        
        validation_result = validator.validate_all_fields(drug_data)
        results[drug_name] = validation_result
        
        if validation_result["valid"]:
            summary["valid_drugs"] += 1
        else:
            summary["invalid_drugs"] += 1
            summary["drugs_with_errors"].append({
                "drug": drug_name,
                "errors": validation_result["errors"]
            })
        
        if validation_result["warnings"]:
            summary["drugs_with_warnings"].append({
                "drug": drug_name,
                "warnings": validation_result["warnings"]
            })
        
        # Count error types
        for error in validation_result["errors"]:
            error_type = error.split(":")[0] if ":" in error else error
            summary["error_types"][error_type] += 1
        
        # Count warning types
        for warning in validation_result["warnings"]:
            warning_type = warning.split(":")[0] if ":" in warning else warning
            summary["warning_types"][warning_type] += 1
    
    return {
        "validation_date": datetime.now().isoformat(),
        "summary": summary,
        "detailed_results": results
    }


def print_validation_summary(validation: Dict[str, Any]):
    """Print validation summary"""
    print("\n" + "="*80)
    print("DRUG VALIDATION SUMMARY")
    print("="*80)
    
    summary = validation["summary"]
    print(f"Total drugs: {summary['total_drugs']}")
    print(f"Valid drugs: {summary['valid_drugs']} ({summary['valid_drugs']/summary['total_drugs']*100:.1f}%)")
    print(f"Invalid drugs: {summary['invalid_drugs']} ({summary['invalid_drugs']/summary['total_drugs']*100:.1f}%)")
    print(f"Drugs with warnings: {len(summary['drugs_with_warnings'])} ({len(summary['drugs_with_warnings'])/summary['total_drugs']*100:.1f}%)")
    
    if summary["error_types"]:
        print("\n" + "-"*80)
        print("ERROR TYPES")
        print("-"*80)
        for error_type, count in sorted(summary["error_types"].items(), key=lambda x: x[1], reverse=True):
            print(f"  {error_type}: {count}")
    
    if summary["warning_types"]:
        print("\n" + "-"*80)
        print("WARNING TYPES (Top 10)")
        print("-"*80)
        for warning_type, count in sorted(summary["warning_types"].items(), key=lambda x: x[1], reverse=True)[:10]:
            print(f"  {warning_type}: {count}")
    
    if summary["drugs_with_errors"]:
        print("\n" + "-"*80)
        print("DRUGS WITH ERRORS (First 20)")
        print("-"*80)
        for drug_info in summary["drugs_with_errors"][:20]:
            print(f"\n  {drug_info['drug']}:")
            for error in drug_info["errors"][:3]:
                print(f"    - {error}")
            if len(drug_info["errors"]) > 3:
                print(f"    ... and {len(drug_info['errors']) - 3} more errors")


def main():
    """Main function"""
    print("="*80)
    print("VALIDATE ALL DRUGS")
    print("="*80)
    
    # Validate all drugs
    validation = validate_all_drugs()
    
    # Print summary
    print_validation_summary(validation)
    
    # Export results
    output_path = Path(__file__).parent / "validation_results.json"
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(validation, f, ensure_ascii=False, indent=2)
    
    print(f"\nDetailed validation results exported to: {output_path}")
    print("\n" + "="*80)
    print("Validation complete!")
    print("="*80)


if __name__ == "__main__":
    main()
