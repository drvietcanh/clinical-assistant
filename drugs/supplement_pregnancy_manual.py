#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Supplement Pregnancy Field - Manual
Bổ sung thủ công field pregnancy cho các thuốc còn lại dựa trên nhóm thuốc và kiến thức y khoa
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


# Manual mapping cho các thuốc cần bổ sung thủ công
MANUAL_PREGNANCY_MAPPING = {
    # Diabetes drugs
    "Gliclazide": "C - Có thể dùng trong thai kỳ nếu lợi ích > nguy cơ. Sulfonylureas có thể gây hạ đường huyết ở trẻ sơ sinh. Insulin là lựa chọn ưu tiên.",
    "Pioglitazone": "C - Nguy cơ không thể loại trừ. Tránh dùng trong thai kỳ. Có thể gây dị tật tim ở động vật.",
    "Liraglutide": "C - Nguy cơ không thể loại trừ. Tránh dùng trong thai kỳ. Dữ liệu còn hạn chế.",
    "Semaglutide": "C - Nguy cơ không thể loại trừ. Tránh dùng trong thai kỳ. Dữ liệu còn hạn chế.",
    "Dulaglutide": "C - Nguy cơ không thể loại trừ. Tránh dùng trong thai kỳ. Dữ liệu còn hạn chế.",
    "Exenatide": "C - Nguy cơ không thể loại trừ. Tránh dùng trong thai kỳ. Dữ liệu còn hạn chế.",
    
    # GI drugs
    "Bismuth subsalicylate": "C - D trong 3 tháng cuối. Tránh dùng trong 3 tháng cuối thai kỳ (nguy cơ đóng ống động mạch sớm).",
    "Ranitidine": "B - Không có bằng chứng về nguy cơ gây dị tật. Có thể dùng trong thai kỳ.",
    "Sucralfate": "B - Không có bằng chứng về nguy cơ gây dị tật. Có thể dùng trong thai kỳ.",
    "Domperidone": "C - Nguy cơ không thể loại trừ. Chỉ dùng nếu lợi ích > nguy cơ.",
    "Ondansetron": "B - Không có bằng chứng về nguy cơ gây dị tật. Được sử dụng rộng rãi trong thai kỳ để điều trị buồn nôn/nôn.",
    
    # Migraine drugs
    "Rizatriptan": "C - Nguy cơ không thể loại trừ. Chỉ dùng nếu lợi ích > nguy cơ.",
    "Sumatriptan": "C - Nguy cơ không thể loại trừ. Chỉ dùng nếu lợi ích > nguy cơ.",
    "Zolmitriptan": "C - Nguy cơ không thể loại trừ. Chỉ dùng nếu lợi ích > nguy cơ.",
    
    # Respiratory drugs
    "Montelukast": "B - Không có bằng chứng về nguy cơ gây dị tật. Có thể dùng trong thai kỳ.",
    "Nedocromil": "B - Không có bằng chứng về nguy cơ gây dị tật. Có thể dùng trong thai kỳ.",
    "Formoterol": "C - Nguy cơ không thể loại trừ. Chỉ dùng nếu lợi ích > nguy cơ.",
    "Olodaterol": "C - Nguy cơ không thể loại trừ. Chỉ dùng nếu lợi ích > nguy cơ.",
    "Salmeterol": "C - Nguy cơ không thể loại trừ. Chỉ dùng nếu lợi ích > nguy cơ.",
    "Vilanterol": "C - Nguy cơ không thể loại trừ. Chỉ dùng nếu lợi ích > nguy cơ.",
    "Ipratropium": "B - Không có bằng chứng về nguy cơ gây dị tật. Có thể dùng trong thai kỳ.",
    "Umeclidinium": "C - Nguy cơ không thể loại trừ. Chỉ dùng nếu lợi ích > nguy cơ.",
    "Beclomethasone inhaled": "C - Nguy cơ không thể loại trừ. Có thể dùng nếu lợi ích > nguy cơ.",
    "Budesonide inhaled": "C - Nguy cơ không thể loại trừ. Có thể dùng nếu lợi ích > nguy cơ.",
    "Ciclesonide": "C - Nguy cơ không thể loại trừ. Chỉ dùng nếu lợi ích > nguy cơ.",
    "Fluticasone inhaled": "C - Nguy cơ không thể loại trừ. Có thể dùng nếu lợi ích > nguy cơ.",
    
    # Neurological drugs
    "Carbamazepine": "D - Nguy cơ dị tật thai nhi (dị tật ống thần kinh, dị tật tim). Chỉ dùng nếu lợi ích > nguy cơ.",
    "Topiramate": "D - Nguy cơ dị tật thai nhi (dị tật ống thần kinh, sứt môi). Chỉ dùng nếu lợi ích > nguy cơ.",
    "Fluoxetine": "C - Nguy cơ không thể loại trừ. Có thể dùng nếu lợi ích > nguy cơ.",
    "Donepezil": "C - Nguy cơ không thể loại trừ. Tránh dùng trong thai kỳ.",
    "Memantine": "B - Không có bằng chứng về nguy cơ gây dị tật. Dữ liệu còn hạn chế.",
    "Rivastigmine": "B - Không có bằng chứng về nguy cơ gây dị tật. Dữ liệu còn hạn chế.",
    
    # Supportive drugs
    "Calcium": "C - Nguy cơ không thể loại trừ. Thường an toàn trong thai kỳ với liều bổ sung.",
    "Diphenhydramine": "B - Không có bằng chứng về nguy cơ gây dị tật. Có thể dùng trong thai kỳ.",
    
    # Anesthesia drugs
    "Etomidate": "C - Nguy cơ không thể loại trừ. Chỉ dùng khi cần thiết trong phẫu thuật.",
    "Ketamine": "C - Nguy cơ không thể loại trừ. Chỉ dùng khi cần thiết trong phẫu thuật.",
    "Propofol": "B - Không có bằng chứng về nguy cơ gây dị tật. Được sử dụng trong phẫu thuật thai kỳ.",
    "Cisatracurium": "B - Không có bằng chứng về nguy cơ gây dị tật. Được sử dụng trong phẫu thuật thai kỳ.",
    "Rocuronium": "B - Không có bằng chứng về nguy cơ gây dị tật. Được sử dụng trong phẫu thuật thai kỳ.",
    "Succinylcholine": "C - Nguy cơ không thể loại trừ. Được sử dụng trong phẫu thuật thai kỳ.",
    
    # Antimicrobial drugs
    "Amoxicillin-clavulanate": "B - An toàn trong thai kỳ.",
    "Ceftriaxone": "B - An toàn trong thai kỳ.",
    "Azithromycin": "B - An toàn trong thai kỳ.",
    "Clarithromycin": "C - Nguy cơ không thể loại trừ. Tránh dùng trong thai kỳ nếu có thể.",
    "Amoxicillin suspension": "B - An toàn trong thai kỳ.",
    
    # Other drugs
    "Hydroxychloroquine": "C - Nguy cơ không thể loại trừ. Có thể dùng trong thai kỳ cho bệnh tự miễn.",
    "Levothyroxine": "A - An toàn trong thai kỳ. Được khuyến nghị cho suy giáp trong thai kỳ.",
    "Methimazole": "D - Nguy cơ dị tật thai nhi (dị tật da đầu). Propylthiouracil được ưu tiên trong tam cá nguyệt đầu.",
    "Propylthiouracil": "D - Nguy cơ dị tật thai nhi và suy gan ở mẹ. Chỉ dùng nếu lợi ích > nguy cơ.",
    "Prednisone": "C - Nguy cơ không thể loại trừ. Có thể dùng nếu lợi ích > nguy cơ.",
    "Betamethasone": "C - Nguy cơ không thể loại trừ. Được sử dụng để trưởng thành phổi thai nhi.",
    "Dexamethasone": "C - Nguy cơ không thể loại trừ. Được sử dụng để trưởng thành phổi thai nhi.",
    "Alendronate": "C - Nguy cơ không thể loại trừ. Tránh dùng trong thai kỳ.",
    "Tamoxifen": "D - Nguy cơ dị tật thai nhi. Chống chỉ định trong thai kỳ.",
    "Anastrozole": "X - Chống chỉ định trong thai kỳ. Nguy cơ dị tật thai nhi.",
    "Imatinib": "D - Nguy cơ dị tật thai nhi. Chỉ dùng nếu lợi ích > nguy cơ.",
    "Erlotinib": "D - Nguy cơ dị tật thai nhi. Chỉ dùng nếu lợi ích > nguy cơ.",
    "Atropine": "C - Nguy cơ không thể loại trừ. Chỉ dùng khi cần thiết.",
    "Lidocaine": "B - Không có bằng chứng về nguy cơ gây dị tật. Được sử dụng trong gây tê thai kỳ.",
    "Sodium Chloride 0.9%": "C - Nguy cơ không thể loại trừ. Thường an toàn trong thai kỳ.",
    "Ringer Lactate": "C - Nguy cơ không thể loại trừ. Thường an toàn trong thai kỳ.",
    "Albumin (Human)": "C - Nguy cơ không thể loại trừ. Được sử dụng trong thai kỳ khi cần thiết.",
    "HES 130/0.4": "C - Nguy cơ không thể loại trừ. Tránh dùng trong thai kỳ nếu có thể.",
    "Vitamin D3 (Cholecalciferol)": "C - Nguy cơ không thể loại trừ. Thường an toàn với liều bổ sung.",
    "Allopurinol": "C - Nguy cơ không thể loại trừ. Chỉ dùng nếu lợi ích > nguy cơ.",
    "Colchicine": "C - Nguy cơ không thể loại trừ. Chỉ dùng nếu lợi ích > nguy cơ.",
    "Febuxostat": "C - Nguy cơ không thể loại trừ. Tránh dùng trong thai kỳ.",
    "Cyclosporine": "C - Nguy cơ không thể loại trừ. Có thể dùng nếu lợi ích > nguy cơ.",
    "Mycophenolate": "D - Nguy cơ dị tật thai nhi nghiêm trọng. CHỐNG CHỈ ĐỊNH trong thai kỳ.",
    "Tacrolimus": "C - Nguy cơ không thể loại trừ. Có thể dùng nếu lợi ích > nguy cơ.",
    "Leflunomide": "X - Chống chỉ định trong thai kỳ. Nguy cơ dị tật thai nhi nghiêm trọng.",
    "Methotrexate": "X - Chống chỉ định trong thai kỳ. Nguy cơ dị tật thai nhi nghiêm trọng.",
    "Bupivacaine": "C - Nguy cơ không thể loại trừ. Được sử dụng trong gây tê thai kỳ.",
    "Levobupivacaine": "B - Không có bằng chứng về nguy cơ gây dị tật. Được sử dụng trong gây tê thai kỳ.",
    "VAT (Tetanus Vaccine)": "C - Nguy cơ không thể loại trừ. Được khuyến nghị trong thai kỳ.",
    "Verorab (Rabies Vaccine)": "C - Nguy cơ không thể loại trừ. Được sử dụng khi cần thiết.",
    "Influenza Vaccine": "C - Nguy cơ không thể loại trừ. Được khuyến nghị trong thai kỳ.",
    "Hepatitis B Vaccine": "C - Nguy cơ không thể loại trừ. Được khuyến nghị trong thai kỳ.",
    "SAT (Tetanus Antitoxin)": "C - Nguy cơ không thể loại trừ. Được sử dụng khi cần thiết.",
    "SAR (Rabies Antiserum)": "C - Nguy cơ không thể loại trừ. Được sử dụng khi cần thiết.",
    "Snake Antivenom (Luc Tre)": "C - Nguy cơ không thể loại trừ. Được sử dụng khi cần thiết.",
    "Snake Antivenom (Ho Dat)": "C - Nguy cơ không thể loại trừ. Được sử dụng khi cần thiết.",
    "Pyridoxine (Vitamin B6)": "A - An toàn trong thai kỳ. Được sử dụng để điều trị buồn nôn thai kỳ.",
    "Pralidoxime": "C - Nguy cơ không thể loại trừ. Được sử dụng trong ngộ độc thuốc trừ sâu.",
    "Ethanol": "D - X - Chống chỉ định trong thai kỳ. Nguy cơ hội chứng rượu bào thai.",
    "Cyanocobalamin (Vitamin B12)": "A - C - An toàn trong thai kỳ. Được khuyến nghị bổ sung.",
    "Vitamin C (Ascorbic Acid)": "C - Nguy cơ không thể loại trừ. Thường an toàn với liều bổ sung.",
    "Sulfasalazine": "B - Không có bằng chứng về nguy cơ gây dị tật. Có thể dùng trong thai kỳ.",
}


def supplement_manual_pregnancy(dry_run: bool = True) -> Dict[str, Any]:
    """Bổ sung thủ công field pregnancy"""
    print("=" * 80)
    print("BỔ SUNG THỦ CÔNG FIELD PREGNANCY")
    print("=" * 80)
    if dry_run:
        print("DRY RUN MODE - Không sửa dữ liệu")
    print()
    
    results = {
        "total_mapped": len(MANUAL_PREGNANCY_MAPPING),
        "supplemented": [],
        "not_found": [],
    }
    
    for drug_name, pregnancy_category in MANUAL_PREGNANCY_MAPPING.items():
        if drug_name not in DRUG_DATABASE:
            results["not_found"].append(drug_name)
            continue
        
        drug_data = DRUG_DATABASE[drug_name]
        if not isinstance(drug_data, dict):
            continue
        
        # Check if missing or empty
        needs_supplement = (
            "pregnancy" not in drug_data or
            not drug_data.get("pregnancy", "").strip() or
            drug_data.get("pregnancy", "") == "Đang cập nhật"
        )
        
        if needs_supplement:
            if not dry_run:
                drug_data["pregnancy"] = pregnancy_category
            results["supplemented"].append({
                "drug": drug_name,
                "category": pregnancy_category
            })
    
    print(f"✅ Đã bổ sung: {len(results['supplemented'])} thuốc")
    if results["not_found"]:
        print(f"⚠️  Không tìm thấy: {len(results['not_found'])} thuốc")
        for drug in results["not_found"][:10]:
            print(f"  - {drug}")
    
    return results


def main():
    """Main function"""
    import argparse
    
    parser = argparse.ArgumentParser(description="Bổ sung thủ công field pregnancy")
    parser.add_argument("--dry-run", action="store_true", default=True,
                       help="Dry run mode")
    parser.add_argument("--execute", action="store_true",
                       help="Thực sự bổ sung")
    
    args = parser.parse_args()
    dry_run = not args.execute
    
    results = supplement_manual_pregnancy(dry_run=dry_run)
    
    if dry_run:
        print("\n⚠️  Đây là DRY RUN. Sử dụng --execute để thực sự bổ sung.")
    else:
        print("\n✅ Đã bổ sung field pregnancy cho các thuốc.")


if __name__ == "__main__":
    main()
