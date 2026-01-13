#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Supplement Pregnancy Field
Hỗ trợ bổ sung field pregnancy cho các thuốc còn thiếu
Sử dụng mapping dựa trên nhóm thuốc và FDA categories chuẩn
"""

import sys
from pathlib import Path
from typing import Dict, List, Any, Optional
import json
from datetime import datetime

# Add project root to path
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    from drugs.drug_database import DRUG_DATABASE
except ImportError:
    sys.path.insert(0, str(Path(__file__).parent))
    from drug_database import DRUG_DATABASE


# FDA Pregnancy Categories mapping dựa trên nhóm thuốc
PREGNANCY_CATEGORIES_BY_GROUP = {
    # ACE Inhibitors và ARBs - Category D
    "ACE Inhibitor": "D - Chống chỉ định trong thai kỳ. Có thể gây dị tật và tử vong thai nhi.",
    "ARB": "D - Chống chỉ định trong thai kỳ. Có thể gây dị tật và tử vong thai nhi.",
    
    # Statins - Category X
    "Statin": "X - Chống chỉ định trong thai kỳ và phụ nữ có thể mang thai.",
    
    # Metformin - Category B
    "Biguanide": "B - Không có bằng chứng về nguy cơ gây dị tật. Có thể dùng trong thai kỳ.",
    
    # Insulin - Category B
    "Insulin": "B - An toàn trong thai kỳ. Được khuyến nghị cho đái tháo đường thai kỳ.",
    
    # PPIs - Category B/C
    "PPI": "B - Không có bằng chứng về nguy cơ gây dị tật. Có thể dùng trong thai kỳ.",
    
    # Opioids - Category C/D
    "Opioid": "C - Nguy cơ không thể loại trừ. Chỉ dùng nếu lợi ích > nguy cơ.",
    
    # NSAIDs - Category C/D (D trong 3 tháng cuối)
    "NSAID": "C - D trong 3 tháng cuối. Tránh dùng trong 3 tháng cuối thai kỳ.",
    
    # Corticosteroids - Category C
    "Corticosteroid": "C - Nguy cơ không thể loại trừ. Có thể dùng nếu lợi ích > nguy cơ.",
    
    # Antibiotics - Varies
    "Penicillin": "B - An toàn trong thai kỳ.",
    "Cephalosporin": "B - An toàn trong thai kỳ.",
    "Macrolide": "B - An toàn trong thai kỳ (trừ clarithromycin - C).",
    "Tetracycline": "D - Chống chỉ định trong thai kỳ (ảnh hưởng răng và xương).",
    "Fluoroquinolone": "C - Tránh dùng trong thai kỳ.",
    
    # Antiepileptics - Category D
    "Anticonvulsant": "D - Nguy cơ dị tật thai nhi. Chỉ dùng nếu lợi ích > nguy cơ.",
    
    # Antidepressants - Category C/D
    "SSRI": "C - Nguy cơ không thể loại trừ. Có thể dùng nếu lợi ích > nguy cơ.",
    
    # Antihistamines - Category B
    "Antihistamine": "B - Không có bằng chứng về nguy cơ gây dị tật.",
}


def get_pregnancy_category_from_group(drug_data: Dict[str, Any]) -> Optional[str]:
    """Lấy pregnancy category dựa trên group của thuốc"""
    group = drug_data.get("group", "").lower()
    
    # Check mappings
    for key, category in PREGNANCY_CATEGORIES_BY_GROUP.items():
        if key.lower() in group:
            return category
    
    # Default based on group keywords
    if "ace" in group or "inhibitor" in group:
        return "D - Chống chỉ định trong thai kỳ."
    elif "arb" in group or "angiotensin" in group:
        return "D - Chống chỉ định trong thai kỳ."
    elif "statin" in group:
        return "X - Chống chỉ định trong thai kỳ."
    elif "metformin" in group or "biguanide" in group:
        return "B - Không có bằng chứng về nguy cơ gây dị tật."
    elif "insulin" in group:
        return "B - An toàn trong thai kỳ."
    elif "ppi" in group or "proton pump" in group:
        return "B - Không có bằng chứng về nguy cơ gây dị tật."
    elif "opioid" in group:
        return "C - Nguy cơ không thể loại trừ."
    elif "nsaid" in group:
        return "C - D trong 3 tháng cuối."
    elif "corticosteroid" in group or "steroid" in group:
        return "C - Nguy cơ không thể loại trừ."
    elif "penicillin" in group:
        return "B - An toàn trong thai kỳ."
    elif "cephalosporin" in group or "cef" in group:
        return "B - An toàn trong thai kỳ."
    elif "tetracycline" in group:
        return "D - Chống chỉ định trong thai kỳ."
    elif "fluoroquinolone" in group or "quinolone" in group:
        return "C - Tránh dùng trong thai kỳ."
    elif "anticonvulsant" in group or "antiepileptic" in group:
        return "D - Nguy cơ dị tật thai nhi."
    elif "ssri" in group or "antidepressant" in group:
        return "C - Nguy cơ không thể loại trừ."
    elif "antihistamine" in group:
        return "B - Không có bằng chứng về nguy cơ gây dị tật."
    
    return None


def supplement_pregnancy_fields(dry_run: bool = True) -> Dict[str, Any]:
    """Bổ sung field pregnancy cho các thuốc còn thiếu"""
    print("=" * 80)
    print("BỔ SUNG FIELD PREGNANCY")
    print("=" * 80)
    if dry_run:
        print("DRY RUN MODE - Không sửa dữ liệu")
    print()
    
    results = {
        "total_checked": 0,
        "missing_pregnancy": [],
        "supplemented": [],
        "needs_manual_review": [],
    }
    
    # Find drugs missing pregnancy field
    for drug_name, drug_data in DRUG_DATABASE.items():
        if not isinstance(drug_data, dict):
            continue
        
        results["total_checked"] += 1
        
        # Check if missing or empty
        if "pregnancy" not in drug_data:
            results["missing_pregnancy"].append(drug_name)
        elif isinstance(drug_data["pregnancy"], str) and not drug_data["pregnancy"].strip():
            results["missing_pregnancy"].append(drug_name)
        elif drug_data["pregnancy"] == "Đang cập nhật":
            results["missing_pregnancy"].append(drug_name)
    
    print(f"📋 Tìm thấy {len(results['missing_pregnancy'])} thuốc thiếu field pregnancy")
    print()
    
    # Try to supplement based on group
    for drug_name in results["missing_pregnancy"]:
        drug_data = DRUG_DATABASE[drug_name]
        category = get_pregnancy_category_from_group(drug_data)
        
        if category:
            if not dry_run:
                drug_data["pregnancy"] = category
            results["supplemented"].append({
                "drug": drug_name,
                "category": category,
                "group": drug_data.get("group", "Unknown")
            })
        else:
            results["needs_manual_review"].append({
                "drug": drug_name,
                "group": drug_data.get("group", "Unknown")
            })
    
    print(f"✅ Có thể bổ sung tự động: {len(results['supplemented'])} thuốc")
    print(f"⚠️  Cần xem xét thủ công: {len(results['needs_manual_review'])} thuốc")
    print()
    
    if results["supplemented"]:
        print("📋 Danh sách thuốc sẽ được bổ sung:")
        for item in results["supplemented"][:20]:
            print(f"  - {item['drug']}: {item['category'][:50]}...")
        if len(results["supplemented"]) > 20:
            print(f"  ... và {len(results['supplemented']) - 20} thuốc khác")
        print()
    
    if results["needs_manual_review"]:
        print("⚠️  Thuốc cần xem xét thủ công:")
        for item in results["needs_manual_review"][:20]:
            print(f"  - {item['drug']} ({item['group']})")
        if len(results["needs_manual_review"]) > 20:
            print(f"  ... và {len(results['needs_manual_review']) - 20} thuốc khác")
    
    return results


def export_supplement_report(results: Dict[str, Any], output_file: str = "pregnancy_supplement_report.json"):
    """Xuất báo cáo"""
    output_path = project_root / "drugs" / output_file
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(results, f, ensure_ascii=False, indent=2)
    print(f"\n✅ Đã xuất báo cáo: {output_path}")


def main():
    """Main function"""
    import argparse
    
    parser = argparse.ArgumentParser(description="Bổ sung field pregnancy")
    parser.add_argument("--dry-run", action="store_true", default=True,
                       help="Dry run mode")
    parser.add_argument("--execute", action="store_true",
                       help="Thực sự bổ sung")
    
    args = parser.parse_args()
    dry_run = not args.execute
    
    results = supplement_pregnancy_fields(dry_run=dry_run)
    export_supplement_report(results)
    
    if dry_run:
        print("\n⚠️  Đây là DRY RUN. Sử dụng --execute để thực sự bổ sung.")
    else:
        print("\n✅ Đã bổ sung field pregnancy cho các thuốc có thể tự động.")
        print("⚠️  Cần xem xét thủ công các thuốc còn lại.")


if __name__ == "__main__":
    main()
