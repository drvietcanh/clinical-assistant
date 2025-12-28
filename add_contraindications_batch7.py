#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script bổ sung contraindications_detail cho các thuốc quan trọng còn thiếu
Batch 7: 15 thuốc đa dạng
"""

from drugs.drug_database import DRUG_DATABASE

# Dữ liệu contraindications_detail cho các thuốc
CONTRAINDICATIONS_DATA = {
    "5-Fluorouracil": {
        "contraindications_detail": {
            "tuyệt_đối": [
                "Dị ứng với 5-fluorouracil",
                "Suy thận nặng (CrCl <30)",
                "Suy gan nặng",
                "Thiếu DPD (dihydropyrimidine dehydrogenase)",
                "Có thai",
                "Đang cho con bú",
            ],
            "tương_đối": [
                "Suy thận vừa (CrCl 30-60) - giảm liều",
                "Suy gan vừa - thận trọng",
                "Người cao tuổi - tăng nguy cơ độc tính",
                "Bệnh tim mạch - tăng nguy cơ thiếu máu cơ tim",
            ],
        },
    },
    "Abiraterone": {
        "contraindications_detail": {
            "tuyệt_đối": [
                "Dị ứng với abiraterone",
                "Suy gan nặng",
                "Có thai",
            ],
            "tương_đối": [
                "Suy gan vừa - thận trọng",
                "Suy thận nặng - thận trọng",
                "Bệnh tim mạch - tăng nguy cơ",
                "Đang cho con bú - thận trọng",
            ],
        },
    },
    "Acebutolol": {
        "contraindications_detail": {
            "tuyệt_đối": [
                "Dị ứng với acebutolol hoặc beta-blocker",
                "Suy tim nặng không được điều trị",
                "Block nhĩ thất độ 2-3 không có máy tạo nhịp",
                "Sick sinus syndrome không có máy tạo nhịp",
                "Nhịp tim chậm nặng (<50 bpm)",
                "Sốc tim",
                "Hen suyễn nặng hoặc COPD nặng",
            ],
            "tương_đối": [
                "Suy tim vừa - cần điều trị trước",
                "Nhịp tim chậm vừa (50-60 bpm)",
                "Block nhĩ thất độ 1",
                "Bệnh mạch máu ngoại biên",
                "Đái tháo đường - che dấu triệu chứng hạ đường huyết",
                "Suy thận nặng (CrCl <30) - giảm liều",
                "Có thai - thận trọng",
                "Đang cho con bú - thận trọng",
            ],
        },
    },
    "Aclidinium": {
        "contraindications_detail": {
            "tuyệt_đối": [
                "Dị ứng với aclidinium",
                "Tăng nhãn áp góc đóng",
            ],
            "tương_đối": [
                "Tăng nhãn áp góc mở - thận trọng",
                "Bệnh tim mạch - thận trọng",
                "Tắc nghẽn đường tiết niệu",
                "Có thai - thận trọng",
                "Đang cho con bú - thận trọng",
            ],
        },
    },
    "Acyclovir eye drops": {
        "contraindications_detail": {
            "tuyệt_đối": [
                "Dị ứng với acyclovir",
            ],
            "tương_đối": [
                "Tổn thương giác mạc nặng",
                "Nhiễm trùng mắt không được điều trị",
                "Có thai - thận trọng",
                "Đang cho con bú - thận trọng",
            ],
        },
    },
    "Acyclovir eye ointment": {
        "contraindications_detail": {
            "tuyệt_đối": [
                "Dị ứng với acyclovir",
            ],
            "tương_đối": [
                "Tổn thương giác mạc nặng",
                "Nhiễm trùng mắt không được điều trị",
                "Có thai - thận trọng",
                "Đang cho con bú - thận trọng",
            ],
        },
    },
    "Adalimumab": {
        "contraindications_detail": {
            "tuyệt_đối": [
                "Dị ứng với adalimumab",
                "Nhiễm trùng nặng đang hoạt động",
                "Suy tim nặng (NYHA III-IV)",
            ],
            "tương_đối": [
                "Nhiễm trùng vừa - cần điều trị trước",
                "Suy tim vừa - thận trọng",
                "Bệnh thần kinh đã biết",
                "Ung thư - tăng nguy cơ",
                "Có thai - thận trọng",
                "Đang cho con bú - thận trọng",
            ],
        },
    },
    "Albendazole": {
        "contraindications_detail": {
            "tuyệt_đối": [
                "Dị ứng với albendazole",
                "Có thai",
            ],
            "tương_đối": [
                "Suy gan nặng - thận trọng",
                "Suy thận nặng - thận trọng",
                "Giảm bạch cầu - nguy cơ giảm thêm",
                "Đang cho con bú - thận trọng",
            ],
        },
    },
    "Alemtuzumab": {
        "contraindications_detail": {
            "tuyệt_đối": [
                "Dị ứng với alemtuzumab",
                "Nhiễm trùng nặng đang hoạt động",
                "HIV dương tính",
            ],
            "tương_đối": [
                "Nhiễm trùng vừa - cần điều trị trước",
                "Bệnh tự miễn - tăng nguy cơ",
                "Ung thư - tăng nguy cơ",
                "Có thai - thận trọng",
                "Đang cho con bú - thận trọng",
            ],
        },
    },
    "Alfuzosin": {
        "contraindications_detail": {
            "tuyệt_đối": [
                "Dị ứng với alfuzosin",
                "Suy gan nặng",
                "Hạ huyết áp nặng",
            ],
            "tương_đối": [
                "Suy gan vừa - thận trọng",
                "Hạ huyết áp",
                "Bệnh tim mạch - thận trọng",
                "Có thai - không áp dụng",
                "Đang cho con bú - không áp dụng",
            ],
        },
    },
    "Anastrozole": {
        "contraindications_detail": {
            "tuyệt_đối": [
                "Dị ứng với anastrozole",
                "Phụ nữ tiền mãn kinh",
                "Có thai",
            ],
            "tương_đối": [
                "Suy gan nặng - thận trọng",
                "Suy thận nặng - thận trọng",
                "Loãng xương - tăng nguy cơ",
                "Đang cho con bú - không áp dụng",
            ],
        },
    },
    "Anidulafungin": {
        "contraindications_detail": {
            "tuyệt_đối": [
                "Dị ứng với anidulafungin hoặc echinocandin",
            ],
            "tương_đối": [
                "Suy gan nặng - thận trọng",
                "Suy thận nặng - không cần giảm liều",
                "Có thai - thận trọng",
                "Đang cho con bú - thận trọng",
            ],
        },
    },
    "Anifrolumab": {
        "contraindications_detail": {
            "tuyệt_đối": [
                "Dị ứng với anifrolumab",
                "Nhiễm trùng nặng đang hoạt động",
            ],
            "tương_đối": [
                "Nhiễm trùng vừa - cần điều trị trước",
                "Bệnh tự miễn khác - tăng nguy cơ",
                "Ung thư - tăng nguy cơ",
                "Có thai - thận trọng",
                "Đang cho con bú - thận trọng",
            ],
        },
    },
    "Aripiprazole": {
        "contraindications_detail": {
            "tuyệt_đối": [
                "Dị ứng với aripiprazole",
            ],
            "tương_đối": [
                "Bệnh tim mạch - tăng nguy cơ kéo dài QT",
                "Suy gan nặng - giảm liều",
                "Suy thận nặng - thận trọng",
                "Động kinh - có thể gây co giật",
                "Đái tháo đường - tăng nguy cơ tăng đường huyết",
                "Có thai - thận trọng",
                "Đang cho con bú - thận trọng",
            ],
        },
    },
    "Artemether-lumefantrine": {
        "contraindications_detail": {
            "tuyệt_đối": [
                "Dị ứng với artemether hoặc lumefantrine",
                "Rối loạn nhịp tim nặng",
                "Có thai (3 tháng đầu)",
            ],
            "tương_đối": [
                "Bệnh tim mạch - tăng nguy cơ kéo dài QT",
                "Suy gan nặng - thận trọng",
                "Suy thận nặng - thận trọng",
                "Có thai (3 tháng giữa và cuối) - thận trọng",
                "Đang cho con bú - thận trọng",
            ],
        },
    },
}

# Code để thêm vào enhanced_fields_overrides.py
def generate_code():
    """Tạo code để thêm vào enhanced_fields_overrides.py"""
    code = "\n# ======================== BATCH 7: MIXED IMPORTANT DRUGS ========================\n"
    code += "# Bổ sung contraindications_detail cho các thuốc quan trọng đa dạng\n\n"
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
    code += "# ======================== END BATCH 7 ========================\n"
    
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

