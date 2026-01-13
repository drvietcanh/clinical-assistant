#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Supplement Missing Fields
Bổ sung các field quan trọng còn thiếu: contraindications, side_effects, dosage
"""

import sys
from pathlib import Path
from typing import Dict, List, Any
import json

# Add project root to path
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    from drugs.drug_database import DRUG_DATABASE
except ImportError:
    sys.path.insert(0, str(Path(__file__).parent))
    from drug_database import DRUG_DATABASE


# Default values based on drug groups
DEFAULT_CONTRANDICATIONS = {
    "Statin": ["Có thai", "Cho con bú", "Bệnh gan hoạt động", "Dị ứng statin"],
    "SGLT2 Inhibitor": ["Có thai", "Suy thận nặng (eGFR <30)", "Dị ứng"],
    "GLP-1 Agonist": ["Có thai", "Dị ứng", "Tiền sử viêm tụy", "U tủy thượng thận"],
    "Sulfonylurea": ["Đái tháo đường type 1", "Nhiễm toan ceton", "Dị ứng"],
    "TZD": ["Có thai", "Suy tim", "Dị ứng"],
    "H2 Antagonist": ["Dị ứng"],
    "PPI": ["Dị ứng"],
    "Antiemetic": ["Dị ứng"],
    "Triptan": ["Bệnh mạch vành", "Đau thắt ngực không ổn định", "Nhồi máu cơ tim", "Đột quỵ", "TIA", "Bệnh mạch máu ngoại biên", "Tăng huyết áp không kiểm soát"],
    "Antihistamine": ["Dị ứng", "Glaucoma góc đóng", "Bí tiểu"],
    "DMARD": ["Có thai", "Cho con bú", "Dị ứng"],
    "Anticonvulsant": ["Dị ứng"],
    "SSRI": ["Dùng MAOI", "Dị ứng"],
}


DEFAULT_SIDE_EFFECTS = {
    "Statin": ["Đau cơ", "Yếu cơ", "Tăng men gan", "Rhabdomyolysis (hiếm)"],
    "SGLT2 Inhibitor": ["Nhiễm trùng đường tiết niệu", "Nhiễm trùng sinh dục", "Hạ đường huyết (khi dùng với insulin/sulfonylurea)", "Mất nước"],
    "GLP-1 Agonist": ["Buồn nôn", "Nôn", "Tiêu chảy", "Giảm cảm giác ngon miệng", "Viêm tụy (hiếm)"],
    "Sulfonylurea": ["Hạ đường huyết", "Tăng cân", "Ban da"],
    "TZD": ["Tăng cân", "Phù", "Suy tim", "Gãy xương"],
    "H2 Antagonist": ["Đau đầu", "Chóng mặt", "Tiêu chảy", "Táo bón"],
    "PPI": ["Đau đầu", "Tiêu chảy", "Táo bón", "Nhiễm trùng đường tiêu hóa"],
    "Antiemetic": ["Đau đầu", "Chóng mặt", "Buồn ngủ"],
    "Triptan": ["Cảm giác nóng, ngứa, tê", "Đau ngực", "Mệt mỏi", "Chóng mặt"],
    "Antihistamine": ["Buồn ngủ", "Khô miệng", "Chóng mặt"],
    "DMARD": ["Buồn nôn", "Đau đầu", "Rối loạn tiêu hóa"],
    "Anticonvulsant": ["Chóng mặt", "Buồn ngủ", "Mệt mỏi"],
    "SSRI": ["Buồn nôn", "Đau đầu", "Mất ngủ", "Giảm ham muốn"],
    "Inhaled Corticosteroid": ["Nấm miệng", "Khàn tiếng", "Ho"],
    "LABA": ["Run tay", "Nhịp tim nhanh", "Đau đầu"],
    "LAMA": ["Khô miệng", "Táo bón", "Bí tiểu"],
    "Supportive": ["Dị ứng (hiếm)"],
    "Anesthesia": ["Ức chế hô hấp", "Hạ huyết áp"],
    "Antimicrobial": ["Dị ứng", "Rối loạn tiêu hóa"],
}


def get_default_contraindications(drug_data: Dict[str, Any]) -> List[str]:
    """Lấy contraindications mặc định dựa trên group"""
    group = drug_data.get("group", "").lower()
    
    for key, value in DEFAULT_CONTRANDICATIONS.items():
        if key.lower() in group:
            return value
    
    return ["Dị ứng"]


def get_default_side_effects(drug_data: Dict[str, Any]) -> List[str]:
    """Lấy side_effects mặc định dựa trên group"""
    group = drug_data.get("group", "").lower()
    
    for key, value in DEFAULT_SIDE_EFFECTS.items():
        if key.lower() in group:
            return value
    
    return ["Dị ứng (hiếm)"]


def supplement_missing_fields(dry_run: bool = True) -> Dict[str, Any]:
    """Bổ sung các field còn thiếu"""
    print("=" * 80)
    print("BỔ SUNG FIELD CÒN THIẾU")
    print("=" * 80)
    if dry_run:
        print("DRY RUN MODE - Không sửa dữ liệu")
    print()
    
    results = {
        "contraindications_added": [],
        "side_effects_added": [],
        "dosage_added": [],
    }
    
    for drug_name, drug_data in DRUG_DATABASE.items():
        if not isinstance(drug_data, dict):
            continue
        
        # Check contraindications
        if "contraindications" not in drug_data or not drug_data.get("contraindications"):
            if not dry_run:
                drug_data["contraindications"] = get_default_contraindications(drug_data)
            results["contraindications_added"].append(drug_name)
        
        # Check side_effects
        if "side_effects" not in drug_data or not drug_data.get("side_effects"):
            if not dry_run:
                drug_data["side_effects"] = get_default_side_effects(drug_data)
            results["side_effects_added"].append(drug_name)
        
        # Check dosage
        if "dosage" not in drug_data or not drug_data.get("dosage"):
            if not dry_run:
                drug_data["dosage"] = {
                    "adult": "Theo chỉ định của bác sĩ",
                    "notes": "Đang cập nhật"
                }
            results["dosage_added"].append(drug_name)
    
    print(f"✅ Đã bổ sung contraindications: {len(results['contraindications_added'])} thuốc")
    print(f"✅ Đã bổ sung side_effects: {len(results['side_effects_added'])} thuốc")
    print(f"✅ Đã bổ sung dosage: {len(results['dosage_added'])} thuốc")
    
    return results


def main():
    """Main function"""
    import argparse
    
    parser = argparse.ArgumentParser(description="Bổ sung field còn thiếu")
    parser.add_argument("--dry-run", action="store_true", default=True,
                       help="Dry run mode")
    parser.add_argument("--execute", action="store_true",
                       help="Thực sự bổ sung")
    
    args = parser.parse_args()
    dry_run = not args.execute
    
    results = supplement_missing_fields(dry_run=dry_run)
    
    if dry_run:
        print("\n⚠️  Đây là DRY RUN. Sử dụng --execute để thực sự bổ sung.")
    else:
        print("\n✅ Đã bổ sung các field còn thiếu.")


if __name__ == "__main__":
    main()
