#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script bổ sung contraindications_detail cho các thuốc kháng sinh quan trọng
Batch 3: 10 thuốc kháng sinh phổ biến
"""

from drugs.drug_database import DRUG_DATABASE

# Dữ liệu contraindications_detail cho các thuốc kháng sinh
CONTRAINDICATIONS_DATA = {
    "Amoxicillin": {
        "contraindications_detail": {
            "tuyệt_đối": [
                "Dị ứng với amoxicillin hoặc penicillin",
                "Tiền sử phản ứng phản vệ với beta-lactam",
            ],
            "tương_đối": [
                "Dị ứng với cephalosporin - thận trọng (phản ứng chéo)",
                "Bệnh bạch cầu đơn nhân nhiễm trùng - tăng nguy cơ phát ban",
                "Suy thận nặng (CrCl <30) - giảm liều",
                "Có thai - thận trọng, nhưng an toàn tương đối",
                "Đang cho con bú - thận trọng",
            ],
        },
    },
    "Amoxicillin/Clavulanate": {
        "contraindications_detail": {
            "tuyệt_đối": [
                "Dị ứng với amoxicillin, clavulanate hoặc penicillin",
                "Tiền sử phản ứng phản vệ với beta-lactam",
                "Tiền sử viêm gan do amoxicillin/clavulanate",
            ],
            "tương_đối": [
                "Dị ứng với cephalosporin - thận trọng",
                "Bệnh bạch cầu đơn nhân nhiễm trùng - tăng nguy cơ phát ban",
                "Suy gan - tăng nguy cơ viêm gan",
                "Suy thận nặng (CrCl <30) - giảm liều",
                "Có thai - thận trọng",
                "Đang cho con bú - thận trọng",
            ],
        },
    },
    "Ampicillin": {
        "contraindications_detail": {
            "tuyệt_đối": [
                "Dị ứng với ampicillin hoặc penicillin",
                "Tiền sử phản ứng phản vệ với beta-lactam",
            ],
            "tương_đối": [
                "Dị ứng với cephalosporin - thận trọng",
                "Bệnh bạch cầu đơn nhân nhiễm trùng - tăng nguy cơ phát ban",
                "Suy thận nặng (CrCl <30) - giảm liều",
                "Có thai - thận trọng",
                "Đang cho con bú - thận trọng",
            ],
        },
    },
    "Cefazolin": {
        "contraindications_detail": {
            "tuyệt_đối": [
                "Dị ứng với cefazolin hoặc cephalosporin",
                "Tiền sử phản ứng phản vệ với beta-lactam",
            ],
            "tương_đối": [
                "Dị ứng với penicillin - thận trọng (phản ứng chéo 5-10%)",
                "Suy thận nặng (CrCl <30) - giảm liều",
                "Có thai - thận trọng",
                "Đang cho con bú - thận trọng",
            ],
        },
    },
    "Ceftriaxone": {
        "contraindications_detail": {
            "tuyệt_đối": [
                "Dị ứng với ceftriaxone hoặc cephalosporin",
                "Tiền sử phản ứng phản vệ với beta-lactam",
                "Trẻ sơ sinh <28 ngày tuổi có tăng bilirubin - nguy cơ vàng da nhân",
            ],
            "tương_đối": [
                "Dị ứng với penicillin - thận trọng",
                "Suy gan nặng - thận trọng",
                "Suy thận nặng (CrCl <30) - không cần giảm liều nhưng thận trọng",
                "Bệnh túi mật - có thể gây sỏi mật giả",
                "Có thai - thận trọng",
                "Đang cho con bú - thận trọng",
            ],
        },
    },
    "Ciprofloxacin": {
        "contraindications_detail": {
            "tuyệt_đối": [
                "Dị ứng với ciprofloxacin hoặc quinolone",
                "Trẻ em <18 tuổi (trừ trường hợp đặc biệt) - nguy cơ tổn thương sụn",
                "Có thai - nguy cơ tổn thương sụn thai nhi",
            ],
            "tương_đối": [
                "Suy thận nặng (CrCl <30) - giảm liều",
                "Suy gan nặng - thận trọng",
                "Bệnh nhân có tiền sử co giật",
                "Bệnh nhân có tiền sử rối loạn tâm thần",
                "Đang dùng thuốc kéo dài QT - tăng nguy cơ rối loạn nhịp",
                "Đang cho con bú - thận trọng",
                "Người cao tuổi - tăng nguy cơ tác dụng phụ",
            ],
        },
    },
    "Levofloxacin": {
        "contraindications_detail": {
            "tuyệt_đối": [
                "Dị ứng với levofloxacin hoặc quinolone",
                "Trẻ em <18 tuổi (trừ trường hợp đặc biệt)",
                "Có thai - nguy cơ tổn thương sụn",
            ],
            "tương_đối": [
                "Suy thận nặng (CrCl <30) - giảm liều",
                "Bệnh nhân có tiền sử co giật",
                "Bệnh nhân có tiền sử rối loạn tâm thần",
                "Đang dùng thuốc kéo dài QT - tăng nguy cơ rối loạn nhịp",
                "Đang cho con bú - thận trọng",
                "Người cao tuổi - tăng nguy cơ tác dụng phụ",
            ],
        },
    },
    "Azithromycin": {
        "contraindications_detail": {
            "tuyệt_đối": [
                "Dị ứng với azithromycin hoặc macrolide",
            ],
            "tương_đối": [
                "Suy gan nặng - thận trọng",
                "Suy thận nặng (CrCl <30) - thận trọng",
                "Rối loạn nhịp tim - tăng nguy cơ kéo dài QT",
                "Đang dùng thuốc kéo dài QT",
                "Bệnh nhân có tiền sử rối loạn nhịp tim",
                "Có thai - thận trọng",
                "Đang cho con bú - thận trọng",
            ],
        },
    },
    "Clarithromycin": {
        "contraindications_detail": {
            "tuyệt_đối": [
                "Dị ứng với clarithromycin hoặc macrolide",
            ],
            "tương_đối": [
                "Suy gan nặng - giảm liều",
                "Suy thận nặng (CrCl <30) - giảm liều",
                "Rối loạn nhịp tim - tăng nguy cơ kéo dài QT",
                "Đang dùng thuốc kéo dài QT",
                "Bệnh nhân có tiền sử rối loạn nhịp tim",
                "Có thai - thận trọng",
                "Đang cho con bú - thận trọng",
            ],
        },
    },
    "Doxycycline": {
        "contraindications_detail": {
            "tuyệt_đối": [
                "Dị ứng với doxycycline hoặc tetracycline",
                "Trẻ em <8 tuổi - nguy cơ đổi màu răng vĩnh viễn",
                "Có thai (2-3 tháng giữa và cuối) - nguy cơ đổi màu răng và ức chế phát triển xương",
            ],
            "tương_đối": [
                "Suy gan nặng - thận trọng",
                "Suy thận nặng (CrCl <30) - không cần giảm liều nhưng thận trọng",
                "Có thai (3 tháng đầu) - thận trọng",
                "Đang cho con bú - thận trọng",
                "Trẻ em 8-12 tuổi - chỉ khi lợi ích > nguy cơ",
            ],
        },
    },
}

# Code để thêm vào enhanced_fields_overrides.py
def generate_code():
    """Tạo code để thêm vào enhanced_fields_overrides.py"""
    code = "\n# ======================== BATCH 3: ANTIBIOTICS ========================\n"
    code += "# Bổ sung contraindications_detail cho các thuốc kháng sinh quan trọng\n\n"
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
    # Kiểm tra các thuốc có trong database không
    print("Kiểm tra các thuốc trong database:")
    for drug_name in CONTRAINDICATIONS_DATA.keys():
        if drug_name in DRUG_DATABASE:
            has_field = "contraindications_detail" in DRUG_DATABASE[drug_name]
            print(f"  ✅ {drug_name}: {'Đã có' if has_field else 'THIẾU'} contraindications_detail")
        else:
            print(f"  ❌ {drug_name}: Không tìm thấy trong database")
    
    print("\n" + "="*80)
    print("Code để thêm vào enhanced_fields_overrides.py:")
    print("="*80)
    print(generate_code())

