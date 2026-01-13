"""
Comprehensive Field Fix
Script tổng hợp để sửa tất cả các vấn đề về fields
"""

import sys
from pathlib import Path
from typing import Dict, List, Any
import json
from datetime import datetime

sys.path.insert(0, str(Path(__file__).parent.parent))

try:
    from drugs.drug_database import DRUG_DATABASE
    from drugs.check_all_drug_fields import check_drug_fields, ALL_FIELDS_INCLUDING_COMMON
    from drugs.validate_all_drugs import validate_all_drugs
except ImportError:
    sys.path.insert(0, str(Path(__file__).parent))
    from drug_database import DRUG_DATABASE
    from check_all_drug_fields import check_drug_fields, ALL_FIELDS_INCLUDING_COMMON
    from validate_all_drugs import validate_all_drugs


def create_comprehensive_report() -> Dict[str, Any]:
    """Tạo báo cáo tổng hợp về trạng thái fields"""
    
    print("="*80)
    print("COMPREHENSIVE FIELD ANALYSIS REPORT")
    print("="*80)
    print()
    
    # Check all drugs
    print("Checking all drugs...")
    drug_results = {}
    field_stats = {field: {"missing": 0, "empty": 0, "has_content": 0} 
                   for field in ALL_FIELDS_INCLUDING_COMMON}
    
    for drug_name, drug_data in DRUG_DATABASE.items():
        result = check_drug_fields(drug_name, drug_data)
        drug_results[drug_name] = result
        
        for field in ALL_FIELDS_INCLUDING_COMMON:
            if field in result["fields_missing"]:
                field_stats[field]["missing"] += 1
            elif field in result["fields_empty"]:
                field_stats[field]["empty"] += 1
            elif field in result["fields_with_content"]:
                field_stats[field]["has_content"] += 1
    
    # Validation
    print("Running validation...")
    validation = validate_all_drugs()
    
    # Summary
    total_drugs = len(DRUG_DATABASE)
    drugs_with_all_standard = sum(1 for r in drug_results.values() if r["has_all_standard"])
    drugs_with_all_additional = sum(1 for r in drug_results.values() if r["has_all_additional"])
    avg_completeness = sum(r["completeness_score"] for r in drug_results.values()) / len(drug_results) if drug_results else 0
    
    # Priority fields to fix
    priority_fields = {
        "critical_errors": [],
        "safety_fields": [],
        "dosing_adjustments": [],
    }
    
    # Critical: Missing STANDARD fields
    for field in ["pregnancy"]:
        if field_stats[field]["missing"] + field_stats[field]["empty"] > 0:
            priority_fields["critical_errors"].append({
                "field": field,
                "missing": field_stats[field]["missing"],
                "empty": field_stats[field]["empty"],
                "total": field_stats[field]["missing"] + field_stats[field]["empty"]
            })
    
    # Safety fields
    for field in ["reversal_agents", "contraindications_detail", "black_box_warnings", "overdose_management"]:
        if field_stats[field]["missing"] + field_stats[field]["empty"] > 0:
            priority_fields["safety_fields"].append({
                "field": field,
                "missing": field_stats[field]["missing"],
                "empty": field_stats[field]["empty"],
                "total": field_stats[field]["missing"] + field_stats[field]["empty"]
            })
    
    # Dosing adjustments
    for field in ["renal_adjustment", "hepatic_adjustment"]:
        if field_stats[field]["missing"] + field_stats[field]["empty"] > 0:
            priority_fields["dosing_adjustments"].append({
                "field": field,
                "missing": field_stats[field]["missing"],
                "empty": field_stats[field]["empty"],
                "total": field_stats[field]["missing"] + field_stats[field]["empty"]
            })
    
    # Sort by total
    for key in priority_fields:
        priority_fields[key].sort(key=lambda x: x["total"], reverse=True)
    
    report = {
        "report_date": datetime.now().isoformat(),
        "total_drugs": total_drugs,
        "summary": {
            "drugs_with_all_standard": drugs_with_all_standard,
            "drugs_with_all_standard_pct": (drugs_with_all_standard / total_drugs * 100) if total_drugs > 0 else 0,
            "drugs_with_all_additional": drugs_with_all_additional,
            "drugs_with_all_additional_pct": (drugs_with_all_additional / total_drugs * 100) if total_drugs > 0 else 0,
            "avg_completeness": avg_completeness,
            "valid_drugs": validation["summary"]["valid_drugs"],
            "invalid_drugs": validation["summary"]["invalid_drugs"],
        },
        "field_statistics": field_stats,
        "priority_fields": priority_fields,
        "validation_summary": validation["summary"],
    }
    
    # Print summary
    print("\n" + "-"*80)
    print("SUMMARY")
    print("-"*80)
    print(f"Total drugs: {total_drugs}")
    print(f"Drugs with all 14 STANDARD fields: {drugs_with_all_standard} ({report['summary']['drugs_with_all_standard_pct']:.1f}%)")
    print(f"Drugs with all 8 ADDITIONAL fields: {drugs_with_all_additional} ({report['summary']['drugs_with_all_additional_pct']:.1f}%)")
    print(f"Average completeness: {avg_completeness:.1f}%")
    print(f"Valid drugs: {validation['summary']['valid_drugs']} ({validation['summary']['valid_drugs']/total_drugs*100:.1f}%)")
    print(f"Invalid drugs: {validation['summary']['invalid_drugs']} ({validation['summary']['invalid_drugs']/total_drugs*100:.1f}%)")
    
    print("\n" + "-"*80)
    print("PRIORITY FIELDS TO FIX")
    print("-"*80)
    
    if priority_fields["critical_errors"]:
        print("\n🔴 CRITICAL ERRORS:")
        for item in priority_fields["critical_errors"]:
            print(f"  - {item['field']}: {item['total']} drugs ({item['missing']} missing, {item['empty']} empty)")
    
    if priority_fields["safety_fields"]:
        print("\n🟡 SAFETY FIELDS:")
        for item in priority_fields["safety_fields"]:
            print(f"  - {item['field']}: {item['total']} drugs ({item['missing']} missing, {item['empty']} empty)")
    
    if priority_fields["dosing_adjustments"]:
        print("\n🟢 DOSING ADJUSTMENTS:")
        for item in priority_fields["dosing_adjustments"]:
            print(f"  - {item['field']}: {item['total']} drugs ({item['missing']} missing, {item['empty']} empty)")
    
    return report


def main():
    """Main function"""
    print("Creating comprehensive field analysis report...")
    
    report = create_comprehensive_report()
    
    # Export report
    output_path = Path(__file__).parent / "comprehensive_field_report.json"
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(report, f, ensure_ascii=False, indent=2)
    
    print(f"\n✅ Report exported to: {output_path}")
    print("\n" + "="*80)
    print("Next steps:")
    print("1. Run fix_missing_pregnancy.py --execute to fix pregnancy fields")
    print("2. Run fix_field_formats.py --execute to fix format errors")
    print("3. Run supplement_missing_fields.py --execute to add missing fields")
    print("4. Update source files manually or use update scripts")
    print("="*80)


if __name__ == "__main__":
    main()
