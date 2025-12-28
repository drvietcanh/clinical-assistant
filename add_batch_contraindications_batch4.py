#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script bổ sung contraindications_detail cho các thuốc quan trọng (Batch 4)
15 thuốc tiếp theo: Kháng sinh, Tim mạch, Ung thư, Thần kinh
"""

from drugs.drug_database import DRUG_DATABASE

CONTRAINDICATIONS_DATA = {
    "Hydrocodone": {
        "contraindications_detail": {
            "tuyệt_đối": [
                "Dị ứng với hydrocodone hoặc opioid",
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
    "Hydroxyzine": {
        "contraindications_detail": {
            "tuyệt_đối": [
                "Dị ứng với hydroxyzine hoặc piperazine",
                "Phụ nữ có thai sớm (category C)",
            ],
            "tương_đối": [
                "Suy gan nặng",
                "Suy thận nặng",
                "Bệnh tim",
                "Glaucoma góc đóng",
            ],
        },
    },
    "Indapamide": {
        "contraindications_detail": {
            "tuyệt_đối": [
                "Dị ứng với indapamide hoặc sulfonamide",
                "Suy thận nặng (eGFR <30 mL/min)",
                "Tăng kali máu nặng",
            ],
            "tương_đối": [
                "Suy gan nặng",
                "Suy thận vừa (theo dõi điện giải)",
                "Đái tháo đường",
                "Gout",
            ],
        },
    },
    "Indomethacin": {
        "contraindications_detail": {
            "tuyệt_đối": [
                "Dị ứng với indomethacin hoặc NSAID",
                "Loét dạ dày tá tràng tiến triển",
                "Suy thận nặng",
                "Suy tim nặng",
            ],
            "tương_đối": [
                "Suy thận vừa",
                "Suy gan vừa",
                "Tăng huyết áp",
                "Bệnh mạch vành",
            ],
        },
    },
    "Irbesartan": {
        "contraindications_detail": {
            "tuyệt_đối": [
                "Dị ứng với irbesartan hoặc ARB",
                "Phụ nữ có thai (tháng 2-3, category D)",
                "Hẹp động mạch thận hai bên hoặc một bên ở bệnh nhân một thận",
            ],
            "tương_đối": [
                "Suy thận nặng (theo dõi chức năng thận)",
                "Hạ huyết áp",
                "Tăng kali máu",
            ],
        },
    },
    "Isosorbide mononitrate": {
        "contraindications_detail": {
            "tuyệt_đối": [
                "Dị ứng với isosorbide mononitrate hoặc nitrate",
                "Hạ huyết áp nặng (systolic <90 mmHg)",
                "Thiếu máu cơ tim cấp do hẹp động mạch chủ nặng",
                "Đang dùng phosphodiesterase-5 inhibitors",
            ],
            "tương_đối": [
                "Hạ huyết áp nhẹ-vừa",
                "Thiếu máu nặng",
                "Tăng áp lực nội sọ",
            ],
        },
    },
    "Isradipine": {
        "contraindications_detail": {
            "tuyệt_đối": [
                "Dị ứng với isradipine hoặc dihydropyridine calcium channel blocker",
            ],
            "tương_đối": [
                "Hạ huyết áp nặng",
                "Suy gan nặng",
                "Suy tim nặng",
            ],
        },
    },
    "Ivabradine": {
        "contraindications_detail": {
            "tuyệt_đối": [
                "Dị ứng với ivabradine",
                "Nhịp tim chậm <60 lần/phút",
                "Suy tim cấp",
                "Hạ huyết áp nặng",
            ],
            "tương_đối": [
                "Suy thận nặng (CrCl <15 mL/min)",
                "Suy gan vừa-nặng",
                "Rối loạn nhịp tim",
            ],
        },
    },
    "Ketoprofen": {
        "contraindications_detail": {
            "tuyệt_đối": [
                "Dị ứng với ketoprofen hoặc NSAID",
                "Loét dạ dày tá tràng tiến triển",
                "Suy thận nặng",
                "Suy tim nặng",
            ],
            "tương_đối": [
                "Suy thận vừa",
                "Suy gan vừa",
                "Tăng huyết áp",
                "Bệnh mạch vành",
            ],
        },
    },
    "Ketorolac": {
        "contraindications_detail": {
            "tuyệt_đối": [
                "Dị ứng với ketorolac hoặc NSAID",
                "Loét dạ dày tá tràng tiến triển",
                "Suy thận nặng",
                "Chảy máu đang hoạt động",
                "Phẫu thuật bắc cầu động mạch vành",
            ],
            "tương_đối": [
                "Suy thận vừa",
                "Suy gan vừa",
                "Người cao tuổi (>65 tuổi)",
                "Rối loạn đông máu",
            ],
        },
    },
    "Labetalol": {
        "contraindications_detail": {
            "tuyệt_đối": [
                "Dị ứng với labetalol hoặc beta-blocker",
                "Block nhĩ-thất độ 2-3 không có máy tạo nhịp",
                "Suy tim mất bù cấp",
                "Hen phế quản nặng",
            ],
            "tương_đối": [
                "Nhịp tim chậm",
                "Hạ huyết áp",
                "Suy tim vừa",
                "COPD vừa",
            ],
        },
    },
    "Lacosamide": {
        "contraindications_detail": {
            "tuyệt_đối": [
                "Dị ứng với lacosamide",
            ],
            "tương_đối": [
                "Suy thận nặng (CrCl <30 mL/min, cần điều chỉnh liều)",
                "Suy gan nặng",
                "Rối loạn nhịp tim",
                "Bệnh tim",
            ],
        },
    },
    "Lisinopril": {
        "contraindications_detail": {
            "tuyệt_đối": [
                "Dị ứng với lisinopril hoặc ACE inhibitor",
                "Phụ nữ có thai (tháng 2-3, category D)",
                "Phù mạch do ACE inhibitor trước đó",
                "Hẹp động mạch thận hai bên hoặc một bên ở bệnh nhân một thận",
            ],
            "tương_đối": [
                "Suy thận nặng (theo dõi chức năng thận)",
                "Hạ huyết áp",
                "Tăng kali máu",
                "Bệnh mô liên kết",
            ],
        },
    },
    "Losartan": {
        "contraindications_detail": {
            "tuyệt_đối": [
                "Dị ứng với losartan hoặc ARB",
                "Phụ nữ có thai (tháng 2-3, category D)",
                "Hẹp động mạch thận hai bên hoặc một bên ở bệnh nhân một thận",
            ],
            "tương_đối": [
                "Suy thận nặng (theo dõi chức năng thận)",
                "Hạ huyết áp",
                "Tăng kali máu",
            ],
        },
    },
    "Lovastatin": {
        "contraindications_detail": {
            "tuyệt_đối": [
                "Dị ứng với lovastatin hoặc statin",
                "Bệnh gan hoạt động",
                "Phụ nữ có thai hoặc cho con bú",
                "Đang dùng thuốc ức chế CYP3A4 mạnh (cyclosporine, itraconazole, ketoconazole)",
            ],
            "tương_đối": [
                "Suy gan vừa",
                "Suy thận nặng",
                "Rối loạn chức năng tuyến giáp",
                "Tiền sử bệnh cơ",
            ],
        },
    },
}

def generate_code():
    """Tạo code để thêm vào enhanced_fields_overrides.py"""
    code = "\n# ======================== BATCH 4: CONTRAINDICATIONS_DETAIL ========================\n"
    code += "# Bổ sung contraindications_detail cho 15 thuốc quan trọng (Kháng sinh, Tim mạch, Ung thư, Thần kinh)\n"
    code += "# Generated automatically by add_batch_contraindications_batch4.py\n\n"
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
    code += "# ======================== END BATCH 4 ========================\n"
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

