#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Final Audit Summary
Tạo báo cáo tổng kết cuối cùng về tình trạng dữ liệu thuốc
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
    from drugs.field_validator import STANDARD_14_FIELDS, ADDITIONAL_8_FIELDS
except ImportError:
    sys.path.insert(0, str(Path(__file__).parent))
    from drug_database import DRUG_DATABASE
    from field_validator import STANDARD_14_FIELDS, ADDITIONAL_8_FIELDS


def generate_final_summary() -> Dict[str, Any]:
    """Tạo báo cáo tổng kết cuối cùng"""
    print("=" * 80)
    print("BÁO CÁO TỔNG KẾT CUỐI CÙNG")
    print("=" * 80)
    print()
    
    summary = {
        "audit_date": datetime.now().isoformat(),
        "total_drugs": len(DRUG_DATABASE),
        "field_completeness": {},
        "critical_fields_status": {},
        "recommendations": [],
    }
    
    # Check field completeness
    all_fields = STANDARD_14_FIELDS + ADDITIONAL_8_FIELDS
    
    for field in all_fields:
        present_count = 0
        empty_count = 0
        
        for drug_name, drug_data in DRUG_DATABASE.items():
            if not isinstance(drug_data, dict):
                continue
            
            if field in drug_data:
                value = drug_data[field]
                if value is None:
                    empty_count += 1
                elif isinstance(value, str) and not value.strip():
                    empty_count += 1
                elif isinstance(value, (list, dict)) and len(value) == 0:
                    empty_count += 1
                else:
                    present_count += 1
            else:
                empty_count += 1
        
        total = present_count + empty_count
        completeness = (present_count / total * 100) if total > 0 else 0
        
        summary["field_completeness"][field] = {
            "present": present_count,
            "empty": empty_count,
            "completeness_percent": round(completeness, 2)
        }
    
    # Check critical fields
    critical_fields = ["group", "vietnamese_name", "administration", "indications", 
                      "dosage", "side_effects", "contraindications", "pregnancy"]
    
    for field in critical_fields:
        missing = []
        for drug_name, drug_data in DRUG_DATABASE.items():
            if not isinstance(drug_data, dict):
                continue
            if field not in drug_data or not drug_data.get(field):
                missing.append(drug_name)
        
        summary["critical_fields_status"][field] = {
            "missing_count": len(missing),
            "missing_drugs": missing[:10]  # Sample
        }
    
    # Print summary
    print("📊 ĐỘ HOÀN THIỆN FIELD:")
    print("-" * 80)
    for field, stats in summary["field_completeness"].items():
        print(f"{field:30s}: {stats['completeness_percent']:6.2f}% ({stats['present']}/{stats['present'] + stats['empty']})")
    
    print()
    print("🔴 FIELD QUAN TRỌNG:")
    print("-" * 80)
    for field, stats in summary["critical_fields_status"].items():
        status = "✅" if stats["missing_count"] == 0 else f"⚠️  {stats['missing_count']} thiếu"
        print(f"{field:30s}: {status}")
        if stats["missing_count"] > 0 and stats["missing_count"] <= 5:
            for drug in stats["missing_drugs"]:
                print(f"  - {drug}")
    
    # Recommendations
    if summary["critical_fields_status"]["pregnancy"]["missing_count"] > 0:
        summary["recommendations"].append(
            f"Cần bổ sung field pregnancy cho {summary['critical_fields_status']['pregnancy']['missing_count']} thuốc"
        )
    
    if summary["field_completeness"]["storage"]["completeness_percent"] < 90:
        summary["recommendations"].append(
            f"Cần bổ sung field storage cho nhiều thuốc hơn"
        )
    
    print()
    print("💡 KHUYẾN NGHỊ:")
    print("-" * 80)
    for rec in summary["recommendations"]:
        print(f"  - {rec}")
    
    return summary


def main():
    """Main function"""
    summary = generate_final_summary()
    
    # Export
    output_path = project_root / "drugs" / "final_audit_summary.json"
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(summary, f, ensure_ascii=False, indent=2)
    print(f"\n✅ Đã xuất báo cáo: {output_path}")


if __name__ == "__main__":
    main()
