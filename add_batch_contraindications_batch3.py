#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script bổ sung contraindications_detail cho các thuốc quan trọng (Batch 3)
15 thuốc tiếp theo: Tim mạch, Nội tiết, Kháng sinh, Huyết học
"""

from drugs.drug_database import DRUG_DATABASE

CONTRAINDICATIONS_DATA = {
    "Codeine": {
        "contraindications_detail": {
            "tuyệt_đối": [
                "Dị ứng với codeine hoặc opioid",
                "Suy hô hấp nặng không có hỗ trợ thở máy",
                "Đang dùng MAO inhibitors (trong vòng 14 ngày)",
            ],
            "tương_đối": [
                "Suy hô hấp mạn tính, COPD nặng",
                "Tăng áp lực nội sọ",
                "Suy gan nặng (giảm chuyển hóa)",
                "Suy thận nặng",
            ],
        },
    },
    "Dipyridamole": {
        "contraindications_detail": {
            "tuyệt_đối": [
                "Dị ứng với dipyridamole",
            ],
            "tương_đối": [
                "Hạ huyết áp nặng",
                "Bệnh mạch vành không ổn định",
                "Suy tim nặng",
                "Rối loạn đông máu",
            ],
        },
    },
    "Disopyramide": {
        "contraindications_detail": {
            "tuyệt_đối": [
                "Dị ứng với disopyramide",
                "Suy tim nặng, sốc tim",
                "Block nhĩ-thất độ 2-3 không có máy tạo nhịp",
                "Suy thận nặng (eGFR <30 mL/min)",
            ],
            "tương_đối": [
                "Suy tim vừa",
                "Suy thận vừa (cần điều chỉnh liều)",
                "Bệnh mạch vành",
                "Glaucoma góc đóng",
            ],
        },
    },
    "Dofetilide": {
        "contraindications_detail": {
            "tuyệt_đối": [
                "Dị ứng với dofetilide",
                "Suy thận nặng (CrCl <20 mL/min)",
                "QT kéo dài (QTc >500 ms)",
                "Đang dùng thuốc gây kéo dài QT",
            ],
            "tương_đối": [
                "Suy thận vừa (cần điều chỉnh liều)",
                "QT kéo dài nhẹ-vừa",
                "Rối loạn điện giải (hạ kali, hạ magie)",
            ],
        },
    },
    "Doxazosin": {
        "contraindications_detail": {
            "tuyệt_đối": [
                "Dị ứng với doxazosin hoặc alpha-blocker",
            ],
            "tương_đối": [
                "Hạ huyết áp nặng",
                "Suy gan nặng",
                "Suy thận nặng",
            ],
        },
    },
    "Eplerenone": {
        "contraindications_detail": {
            "tuyệt_đối": [
                "Dị ứng với eplerenone",
                "Suy thận nặng (CrCl <30 mL/min)",
                "Tăng kali máu nặng (>5.5 mEq/L)",
                "Đang dùng thuốc ức chế CYP3A4 mạnh (ketoconazole, itraconazole)",
            ],
            "tương_đối": [
                "Suy thận vừa (theo dõi kali máu)",
                "Tăng kali máu nhẹ-vừa",
                "Suy gan nặng",
            ],
        },
    },
    "Felodipine": {
        "contraindications_detail": {
            "tuyệt_đối": [
                "Dị ứng với felodipine hoặc dihydropyridine calcium channel blocker",
            ],
            "tương_đối": [
                "Hạ huyết áp nặng",
                "Suy gan nặng (tăng nồng độ)",
                "Suy tim nặng",
            ],
        },
    },
    "Fenofibrate": {
        "contraindications_detail": {
            "tuyệt_đối": [
                "Dị ứng với fenofibrate hoặc fibrate",
                "Bệnh gan hoạt động",
                "Suy thận nặng (eGFR <30 mL/min)",
                "Bệnh túi mật",
            ],
            "tương_đối": [
                "Suy gan vừa",
                "Suy thận vừa (cần điều chỉnh liều)",
                "Rối loạn chức năng tuyến giáp",
            ],
        },
    },
    "Filgrastim": {
        "contraindications_detail": {
            "tuyệt_đối": [
                "Dị ứng với filgrastim hoặc G-CSF",
            ],
            "tương_đối": [
                "Bệnh bạch cầu cấp (AML) ở trẻ em",
                "Hội chứng rối loạn hô hấp cấp (ARDS)",
                "Lách to",
            ],
        },
    },
    "Fludrocortisone": {
        "contraindications_detail": {
            "tuyệt_đối": [
                "Dị ứng với fludrocortisone hoặc corticosteroid",
                "Nhiễm nấm hệ thống không điều trị",
            ],
            "tương_đối": [
                "Suy tim nặng",
                "Tăng huyết áp nặng",
                "Phù nề",
                "Loãng xương",
            ],
        },
    },
    "Fosphenytoin": {
        "contraindications_detail": {
            "tuyệt_đối": [
                "Dị ứng với fosphenytoin hoặc phenytoin",
                "Block nhĩ-thất độ 2-3",
            ],
            "tương_đối": [
                "Suy gan nặng (giảm chuyển hóa)",
                "Suy thận nặng",
                "Bệnh tim",
                "Rối loạn chức năng tuyến giáp",
            ],
        },
    },
    "Ganciclovir": {
        "contraindications_detail": {
            "tuyệt_đối": [
                "Dị ứng với ganciclovir",
            ],
            "tương_đối": [
                "Suy thận nặng (cần điều chỉnh liều)",
                "Giảm bạch cầu hoặc tiểu cầu nặng",
                "Suy gan nặng",
            ],
        },
    },
    "Gemfibrozil": {
        "contraindications_detail": {
            "tuyệt_đối": [
                "Dị ứng với gemfibrozil hoặc fibrate",
                "Bệnh gan hoạt động",
                "Suy thận nặng (eGFR <30 mL/min)",
                "Bệnh túi mật",
            ],
            "tương_đối": [
                "Suy gan vừa",
                "Suy thận vừa",
                "Rối loạn chức năng tuyến giáp",
            ],
        },
    },
    "Glimepiride": {
        "contraindications_detail": {
            "tuyệt_đối": [
                "Dị ứng với glimepiride hoặc sulfonylurea",
                "Đái tháo đường type 1",
                "Nhiễm toan ceton do đái tháo đường",
                "Suy thận nặng (eGFR <30 mL/min)",
            ],
            "tương_đối": [
                "Suy gan nặng (tăng nguy cơ hạ đường huyết)",
                "Suy thận vừa (cần điều chỉnh liều)",
                "Người cao tuổi (tăng nguy cơ hạ đường huyết)",
            ],
        },
    },
    "Hydralazine": {
        "contraindications_detail": {
            "tuyệt_đối": [
                "Dị ứng với hydralazine",
                "Bệnh mạch vành nặng",
                "Nhồi máu cơ tim cấp",
            ],
            "tương_đối": [
                "Suy tim nặng",
                "Bệnh mạch vành",
                "Suy gan nặng",
                "Suy thận nặng",
            ],
        },
    },
}

def generate_code():
    """Tạo code để thêm vào enhanced_fields_overrides.py"""
    code = "\n# ======================== BATCH 3: CONTRAINDICATIONS_DETAIL ========================\n"
    code += "# Bổ sung contraindications_detail cho 15 thuốc quan trọng (Tim mạch, Nội tiết, Kháng sinh, Huyết học)\n"
    code += "# Generated automatically by add_batch_contraindications_batch3.py\n\n"
    code += "EXTRA_ENHANCED_FIELDS.update({\n"
    
    for drug_name, data in CONTRAINDICATIONS_DATA.items():
        code += f'    "{drug_name}": {{\n'
        code += '        "contraindications_detail": {\n'
        code += '            "tuyệt_đối": [\n'
        for item in data["contraindications_detail"]["tuyệt_đối"]:
            code += f'                "{item}",\n'
        code += '            ],\n'
        code += '            "tương_đối": [\n'
        for item in data["contraindications_detail"]["tương_đối"]:
            code += f'                "{item}",\n'
        code += '            ],\n'
        code += '        },\n'
        code += '    },\n'
    
    code += "})\n"
    code += "# ======================== END BATCH 3 ========================\n"
    return code

if __name__ == '__main__':
    print("="*80)
    print("KIỂM TRA CÁC THUỐC TRONG DATABASE")
    print("="*80)
    for drug_name in CONTRAINDICATIONS_DATA.keys():
        if drug_name in DRUG_DATABASE:
            has_field = "contraindications_detail" in DRUG_DATABASE[drug_name]
            status = "✅ Đã có" if has_field else "❌ THIẾU"
            print(f"  {status}: {drug_name}")
        else:
            print(f"  ⚠️  {drug_name}: Không tìm thấy trong database")
    
    print("\n" + "="*80)
    print("CODE ĐỂ THÊM VÀO enhanced_fields_overrides.py:")
    print("="*80)
    print(generate_code())

