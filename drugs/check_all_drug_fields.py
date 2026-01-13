"""
Comprehensive Drug Fields Checker
Kiểm tra toàn bộ dữ liệu thuốc và các field hiện có/thiếu
"""

import sys
from pathlib import Path
from typing import Dict, List, Set, Optional, Any
from collections import defaultdict
import json
from datetime import datetime

# Add parent directory to path
sys.path.insert(0, str(Path(__file__).parent.parent))

try:
    from drugs.drug_database import DRUG_DATABASE, TOTAL_DRUGS
    from drugs.field_validator import (
        STANDARD_14_FIELDS,
        ADDITIONAL_8_FIELDS,
        ALL_FIELDS,
        FieldValidator
    )
except ImportError as e:
    print(f"Import error: {e}")
    print("Trying alternative import...")
    sys.path.insert(0, str(Path(__file__).parent))
    from drug_database import DRUG_DATABASE, TOTAL_DRUGS
    from field_validator import (
        STANDARD_14_FIELDS,
        ADDITIONAL_8_FIELDS,
        ALL_FIELDS,
        FieldValidator
    )

# Additional fields that are commonly used but not in standard list
ADDITIONAL_COMMON_FIELDS = [
    "renal_adjustment",
    "contraindications_detail",
]

ALL_FIELDS_INCLUDING_COMMON = ALL_FIELDS + ADDITIONAL_COMMON_FIELDS


def is_field_empty(field_value: Any) -> bool:
    """Check if a field value is considered empty"""
    if field_value is None:
        return True
    if isinstance(field_value, str):
        return field_value.strip() == "" or field_value.strip() == "Đang cập nhật"
    if isinstance(field_value, list):
        return len(field_value) == 0 or (len(field_value) == 1 and isinstance(field_value[0], str) and field_value[0].strip() == "Đang cập nhật")
    if isinstance(field_value, dict):
        # Check if dict is empty or only has placeholder values
        if len(field_value) == 0:
            return True
        # Check if all values are empty/placeholder
        all_empty = True
        for v in field_value.values():
            if isinstance(v, str) and v.strip() and v.strip() != "Đang cập nhật":
                all_empty = False
                break
            elif isinstance(v, (list, dict)) and len(v) > 0:
                all_empty = False
                break
            elif not isinstance(v, (str, list, dict)) and v:
                all_empty = False
                break
        return all_empty
    return False


def check_drug_fields(drug_name: str, drug_data: Dict[str, Any]) -> Dict[str, Any]:
    """
    Check fields for a single drug
    
    Returns:
        Dict with field status information
    """
    if not isinstance(drug_data, dict):
        return {
            "drug_name": drug_name,
            "error": "Not a valid drug dict",
            "fields_present": [],
            "fields_missing": ALL_FIELDS_INCLUDING_COMMON,
            "fields_empty": ALL_FIELDS_INCLUDING_COMMON,
            "fields_with_content": [],
            "missing_standard": STANDARD_14_FIELDS,
            "missing_additional": ADDITIONAL_8_FIELDS,
            "missing_common": ADDITIONAL_COMMON_FIELDS,
            "empty_standard": [],
            "empty_additional": [],
            "empty_common": [],
            "completeness_score": 0,
            "has_all_standard": False,
            "has_all_additional": False,
        }
    
    fields_present = []
    fields_missing = []
    fields_empty = []
    fields_with_content = []
    
    # Check all standard and additional fields
    for field in ALL_FIELDS_INCLUDING_COMMON:
        if field in drug_data:
            fields_present.append(field)
            if is_field_empty(drug_data[field]):
                fields_empty.append(field)
            else:
                fields_with_content.append(field)
        else:
            fields_missing.append(field)
    
    # Count fields by category
    missing_standard = [f for f in STANDARD_14_FIELDS if f in fields_missing]
    missing_additional = [f for f in ADDITIONAL_8_FIELDS if f in fields_missing]
    missing_common = [f for f in ADDITIONAL_COMMON_FIELDS if f in fields_missing]
    
    empty_standard = [f for f in STANDARD_14_FIELDS if f in fields_empty]
    empty_additional = [f for f in ADDITIONAL_8_FIELDS if f in fields_empty]
    empty_common = [f for f in ADDITIONAL_COMMON_FIELDS if f in fields_empty]
    
    return {
        "drug_name": drug_name,
        "total_fields_checked": len(ALL_FIELDS_INCLUDING_COMMON),
        "fields_present": fields_present,
        "fields_missing": fields_missing,
        "fields_empty": fields_empty,
        "fields_with_content": fields_with_content,
        "missing_standard": missing_standard,
        "missing_additional": missing_additional,
        "missing_common": missing_common,
        "empty_standard": empty_standard,
        "empty_additional": empty_additional,
        "empty_common": empty_common,
        "completeness_score": len(fields_with_content) / len(ALL_FIELDS_INCLUDING_COMMON) * 100,
        "has_all_standard": len(missing_standard) == 0 and len(empty_standard) == 0,
        "has_all_additional": len(missing_additional) == 0 and len(empty_additional) == 0,
    }


def analyze_all_drugs() -> Dict[str, Any]:
    """
    Analyze all drugs in the database
    
    Returns:
        Comprehensive analysis report
    """
    print(f"Analyzing {TOTAL_DRUGS} drugs...")
    
    results = {}
    field_stats = defaultdict(int)
    field_missing_count = defaultdict(int)
    field_empty_count = defaultdict(int)
    field_content_count = defaultdict(int)
    
    drugs_by_completeness = defaultdict(list)
    drugs_missing_fields = defaultdict(list)
    
    for drug_name, drug_data in DRUG_DATABASE.items():
        check_result = check_drug_fields(drug_name, drug_data)
        results[drug_name] = check_result
        
        # Update statistics
        for field in check_result["fields_with_content"]:
            field_content_count[field] += 1
        
        for field in check_result["fields_missing"]:
            field_missing_count[field] += 1
        
        for field in check_result["fields_empty"]:
            field_empty_count[field] += 1
        
        # Group by completeness
        score = check_result["completeness_score"]
        completeness_bucket = int(score // 10) * 10  # 0-10, 10-20, etc.
        drugs_by_completeness[completeness_bucket].append(drug_name)
        
        # Track drugs missing specific fields
        for field in check_result["fields_missing"]:
            drugs_missing_fields[field].append(drug_name)
        for field in check_result["fields_empty"]:
            if field not in drugs_missing_fields:
                drugs_missing_fields[field].append(drug_name)
    
    # Calculate percentages
    field_percentages = {}
    for field in ALL_FIELDS_INCLUDING_COMMON:
        total = TOTAL_DRUGS
        with_content = field_content_count[field]
        missing = field_missing_count[field]
        empty = field_empty_count[field]
        
        field_percentages[field] = {
            "has_content": with_content,
            "missing": missing,
            "empty": empty,
            "has_content_pct": (with_content / total * 100) if total > 0 else 0,
            "missing_pct": (missing / total * 100) if total > 0 else 0,
            "empty_pct": (empty / total * 100) if total > 0 else 0,
        }
    
    # Find common missing patterns
    missing_patterns = defaultdict(int)
    for drug_name, result in results.items():
        missing_fields = result["fields_missing"] + result["fields_empty"]
        if len(missing_fields) > 0:
            # Create pattern key
            pattern_key = tuple(sorted(missing_fields))
            missing_patterns[pattern_key] += 1
    
    # Sort patterns by frequency
    sorted_patterns = sorted(missing_patterns.items(), key=lambda x: x[1], reverse=True)
    
    return {
        "total_drugs": TOTAL_DRUGS,
        "analysis_date": datetime.now().isoformat(),
        "field_statistics": field_percentages,
        "drugs_by_completeness": dict(drugs_by_completeness),
        "drugs_missing_fields": dict(drugs_missing_fields),
        "missing_patterns": [
            {"pattern": list(pattern), "count": count, "drugs": [
                name for name, r in results.items() 
                if set(r["fields_missing"] + r["fields_empty"]) == set(pattern)
            ][:10]}  # First 10 drugs with this pattern
            for pattern, count in sorted_patterns[:20]  # Top 20 patterns
        ],
        "summary": {
            "drugs_with_all_standard": sum(1 for r in results.values() if r["has_all_standard"]),
            "drugs_with_all_additional": sum(1 for r in results.values() if r["has_all_additional"]),
            "avg_completeness": sum(r["completeness_score"] for r in results.values()) / len(results) if results else 0,
            "drugs_100_percent": len([r for r in results.values() if r["completeness_score"] >= 100]),
            "drugs_90_plus_percent": len([r for r in results.values() if r["completeness_score"] >= 90]),
            "drugs_under_50_percent": len([r for r in results.values() if r["completeness_score"] < 50]),
        }
    }


def print_summary_report(analysis: Dict[str, Any]):
    """Print a human-readable summary report"""
    print("\n" + "="*80)
    print("DRUG FIELDS ANALYSIS REPORT")
    print("="*80)
    print(f"Analysis Date: {analysis['analysis_date']}")
    print(f"Total Drugs: {analysis['total_drugs']}")
    
    print("\n" + "-"*80)
    print("SUMMARY")
    print("-"*80)
    summary = analysis["summary"]
    print(f"Drugs with all 14 STANDARD fields: {summary['drugs_with_all_standard']} ({summary['drugs_with_all_standard']/analysis['total_drugs']*100:.1f}%)")
    print(f"Drugs with all 8 ADDITIONAL fields: {summary['drugs_with_all_additional']} ({summary['drugs_with_all_additional']/analysis['total_drugs']*100:.1f}%)")
    print(f"Average completeness score: {summary['avg_completeness']:.1f}%")
    print(f"Drugs at 100% completeness: {summary['drugs_100_percent']} ({summary['drugs_100_percent']/analysis['total_drugs']*100:.1f}%)")
    print(f"Drugs at 90%+ completeness: {summary['drugs_90_plus_percent']} ({summary['drugs_90_plus_percent']/analysis['total_drugs']*100:.1f}%)")
    print(f"Drugs under 50% completeness: {summary['drugs_under_50_percent']} ({summary['drugs_under_50_percent']/analysis['total_drugs']*100:.1f}%)")
    
    print("\n" + "-"*80)
    print("FIELD STATISTICS (sorted by missing count)")
    print("-"*80)
    field_stats = analysis["field_statistics"]
    
    # Sort by missing count
    sorted_fields = sorted(
        field_stats.items(),
        key=lambda x: x[1]["missing"] + x[1]["empty"],
        reverse=True
    )
    
    print(f"{'Field':<30} {'Has Content':<12} {'Missing':<10} {'Empty':<10} {'Total Missing':<15}")
    print("-"*80)
    for field, stats in sorted_fields:
        total_missing = stats["missing"] + stats["empty"]
        print(f"{field:<30} {stats['has_content']:<12} {stats['missing']:<10} {stats['empty']:<10} {total_missing:<15}")
    
    print("\n" + "-"*80)
    print("TOP 10 MISSING FIELD PATTERNS")
    print("-"*80)
    for i, pattern_info in enumerate(analysis["missing_patterns"][:10], 1):
        pattern = pattern_info["pattern"]
        count = pattern_info["count"]
        drugs_sample = pattern_info["drugs"]
        print(f"\n{i}. Pattern: {', '.join(pattern)}")
        print(f"   Count: {count} drugs ({count/analysis['total_drugs']*100:.1f}%)")
        if drugs_sample:
            print(f"   Sample drugs: {', '.join(drugs_sample[:5])}")
            if len(drugs_sample) > 5:
                print(f"   ... and {len(drugs_sample) - 5} more")


def export_detailed_report(analysis: Dict[str, Any], output_file: str = "drug_fields_analysis.json"):
    """Export detailed analysis to JSON file"""
    output_path = Path(__file__).parent / output_file
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(analysis, f, ensure_ascii=False, indent=2)
    print(f"\nDetailed report exported to: {output_path}")


def main():
    """Main function"""
    print("Starting comprehensive drug fields analysis...")
    
    # Analyze all drugs
    analysis = analyze_all_drugs()
    
    # Print summary
    print_summary_report(analysis)
    
    # Export detailed report
    export_detailed_report(analysis)
    
    print("\n" + "="*80)
    print("Analysis complete!")
    print("="*80)


if __name__ == "__main__":
    main()
