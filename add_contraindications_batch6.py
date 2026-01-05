#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script bổ sung contraindications_detail cho các thuốc hô hấp, kháng histamine và kháng virus
Batch 6: 15 thuốc quan trọng
"""

from drugs.drug_database import DRUG_DATABASE

# Dữ liệu contraindications_detail cho các thuốc
CONTRAINDICATIONS_DATA = {
    "Salbutamol": {
        "contraindications_detail": {
            "tuyệt_đối": [
                "Dị ứng với salbutamol hoặc beta-2 agonist",
            ],
            "tương_đối": [
                "Bệnh tim mạch - tăng nguy cơ rối loạn nhịp tim",
                "Tăng huyết áp không kiểm soát",
                "Đái tháo đường - có thể tăng đường huyết",
                "Cường giáp - tăng nhạy cảm",
                "Có thai - thận trọng",
                "Đang cho con bú - thận trọng",
            ],
        },
    },
    "Budesonide": {
        "contraindications_detail": {
            "tuyệt_đối": [
                "Dị ứng với budesonide hoặc corticosteroid",
                "Nhiễm trùng đường hô hấp không được điều trị",
            ],
            "tương_đối": [
                "Nhiễm lao phổi - cần điều trị trước",
                "Nhiễm nấm đường hô hấp",
                "Có thai - thận trọng",
                "Đang cho con bú - thận trọng",
                "Trẻ em - ảnh hưởng đến tăng trưởng",
            ],
        },
    },
    "Beclomethasone": {
        "contraindications_detail": {
            "tuyệt_đối": [
                "Dị ứng với beclomethasone hoặc corticosteroid",
                "Nhiễm trùng đường hô hấp không được điều trị",
            ],
            "tương_đối": [
                "Nhiễm lao phổi - cần điều trị trước",
                "Nhiễm nấm đường hô hấp",
                "Có thai - thận trọng",
                "Đang cho con bú - thận trọng",
                "Trẻ em - ảnh hưởng đến tăng trưởng",
            ],
        },
    },
    "Montelukast": {
        "contraindications_detail": {
            "tuyệt_đối": [
                "Dị ứng với montelukast",
            ],
            "tương_đối": [
                "Bệnh nhân có tiền sử rối loạn tâm thần - nguy cơ hành vi bất thường",
                "Suy gan nặng - thận trọng",
                "Có thai - thận trọng",
                "Đang cho con bú - thận trọng",
            ],
        },
    },
    "Theophylline": {
        "contraindications_detail": {
            "tuyệt_đối": [
                "Dị ứng với theophylline hoặc methylxanthine",
                "Loét dạ dày tá tràng đang hoạt động",
                "Rối loạn nhịp tim nặng",
            ],
            "tương_đối": [
                "Bệnh tim mạch - tăng nguy cơ rối loạn nhịp",
                "Suy gan nặng - giảm liều đáng kể",
                "Suy thận nặng - thận trọng",
                "Động kinh - có thể gây co giật",
                "Có thai - thận trọng",
                "Đang cho con bú - thận trọng",
            ],
        },
    },
    "Aminophylline": {
        "contraindications_detail": {
            "tuyệt_đối": [
                "Dị ứng với aminophylline hoặc theophylline",
                "Loét dạ dày tá tràng đang hoạt động",
                "Rối loạn nhịp tim nặng",
            ],
            "tương_đối": [
                "Bệnh tim mạch - tăng nguy cơ rối loạn nhịp",
                "Suy gan nặng - giảm liều đáng kể",
                "Suy thận nặng - thận trọng",
                "Động kinh - có thể gây co giật",
                "Có thai - thận trọng",
                "Đang cho con bú - thận trọng",
            ],
        },
    },
    "Diphenhydramine": {
        "contraindications_detail": {
            "tuyệt_đối": [
                "Dị ứng với diphenhydramine hoặc antihistamine",
                "Trẻ sơ sinh <2 tháng tuổi",
            ],
            "tương_đối": [
                "Bệnh nhược cơ - tăng yếu cơ",
                "Tăng nhãn áp góc đóng",
                "Loét dạ dày tá tràng",
                "Tắc nghẽn đường tiết niệu",
                "Bệnh tim mạch - tăng nguy cơ rối loạn nhịp",
                "Có thai - thận trọng",
                "Đang cho con bú - thận trọng",
                "Người cao tuổi - tăng nguy cơ tác dụng phụ",
            ],
        },
    },
    "Loratadine": {
        "contraindications_detail": {
            "tuyệt_đối": [
                "Dị ứng với loratadine",
            ],
            "tương_đối": [
                "Suy gan nặng - giảm liều",
                "Suy thận nặng - thận trọng",
                "Có thai - thận trọng",
                "Đang cho con bú - thận trọng",
            ],
        },
    },
    "Chlorpheniramine": {
        "contraindications_detail": {
            "tuyệt_đối": [
                "Dị ứng với chlorpheniramine hoặc antihistamine",
                "Trẻ sơ sinh <2 tháng tuổi",
            ],
            "tương_đối": [
                "Bệnh nhược cơ - tăng yếu cơ",
                "Tăng nhãn áp góc đóng",
                "Loét dạ dày tá tràng",
                "Tắc nghẽn đường tiết niệu",
                "Bệnh tim mạch - tăng nguy cơ rối loạn nhịp",
                "Có thai - thận trọng",
                "Đang cho con bú - thận trọng",
                "Người cao tuổi - tăng nguy cơ tác dụng phụ",
            ],
        },
    },
    "Diazepam": {
        "contraindications_detail": {
            "tuyệt_đối": [
                "Dị ứng với diazepam hoặc benzodiazepine",
                "Suy hô hấp nặng không có hỗ trợ thở máy",
                "Myasthenia gravis",
                "Glaucoma góc đóng",
            ],
            "tương_đối": [
                "Suy hô hấp vừa",
                "Suy gan nặng - giảm liều",
                "Suy thận nặng - thận trọng",
                "Người cao tuổi - tăng nhạy cảm",
                "Có thai - thận trọng, có thể gây dị tật",
                "Đang cho con bú - thận trọng",
                "Tiền sử lạm dụng chất",
            ],
        },
    },
    "Lorazepam": {
        "contraindications_detail": {
            "tuyệt_đối": [
                "Dị ứng với lorazepam hoặc benzodiazepine",
                "Suy hô hấp nặng không có hỗ trợ thở máy",
                "Myasthenia gravis",
                "Glaucoma góc đóng",
            ],
            "tương_đối": [
                "Suy hô hấp vừa",
                "Suy gan nặng - giảm liều",
                "Suy thận nặng - thận trọng",
                "Người cao tuổi - tăng nhạy cảm",
                "Có thai - thận trọng, có thể gây dị tật",
                "Đang cho con bú - thận trọng",
                "Tiền sử lạm dụng chất",
            ],
        },
    },
    "Haloperidol": {
        "contraindications_detail": {
            "tuyệt_đối": [
                "Dị ứng với haloperidol",
                "Parkinson nặng",
                "Ức chế tủy xương",
                "Đang dùng thuốc ức chế MAO",
            ],
            "tương_đối": [
                "Bệnh tim mạch - tăng nguy cơ kéo dài QT",
                "Suy gan nặng - thận trọng",
                "Suy thận nặng - thận trọng",
                "Động kinh - có thể gây co giật",
                "Có thai - thận trọng",
                "Đang cho con bú - thận trọng",
                "Người cao tuổi - tăng nguy cơ tác dụng phụ",
            ],
        },
    },
    "Risperidone": {
        "contraindications_detail": {
            "tuyệt_đối": [
                "Dị ứng với risperidone",
            ],
            "tương_đối": [
                "Bệnh tim mạch - tăng nguy cơ kéo dài QT",
                "Suy gan nặng - giảm liều",
                "Suy thận nặng - giảm liều",
                "Động kinh - có thể gây co giật",
                "Parkinson - có thể làm nặng triệu chứng",
                "Có thai - thận trọng",
                "Đang cho con bú - thận trọng",
                "Người cao tuổi - tăng nguy cơ tác dụng phụ",
            ],
        },
    },
    "Olanzapine": {
        "contraindications_detail": {
            "tuyệt_đối": [
                "Dị ứng với olanzapine",
            ],
            "tương_đối": [
                "Bệnh tim mạch - tăng nguy cơ kéo dài QT",
                "Suy gan nặng - thận trọng",
                "Suy thận nặng - thận trọng",
                "Động kinh - có thể gây co giật",
                "Đái tháo đường - tăng nguy cơ tăng đường huyết",
                "Có thai - thận trọng",
                "Đang cho con bú - thận trọng",
                "Người cao tuổi - tăng nguy cơ tác dụng phụ",
            ],
        },
    },
    "Acyclovir": {
        "contraindications_detail": {
            "tuyệt_đối": [
                "Dị ứng với acyclovir",
            ],
            "tương_đối": [
                "Suy thận nặng (CrCl <25) - giảm liều",
                "Mất nước - tăng nguy cơ độc tính thận",
                "Có thai - thận trọng",
                "Đang cho con bú - thận trọng",
                "Người cao tuổi - tăng nguy cơ độc tính thận",
            ],
        },
    },
    "Valacyclovir": {
        "contraindications_detail": {
            "tuyệt_đối": [
                "Dị ứng với valacyclovir hoặc acyclovir",
            ],
            "tương_đối": [
                "Suy thận nặng (CrCl <30) - giảm liều",
                "Mất nước - tăng nguy cơ độc tính thận",
                "Suy gan nặng - thận trọng",
                "Có thai - thận trọng",
                "Đang cho con bú - thận trọng",
                "Người cao tuổi - tăng nguy cơ độc tính thận",
            ],
        },
    },
}

# Code để thêm vào enhanced_fields_overrides.py
def generate_code():
    """Tạo code để thêm vào enhanced_fields_overrides.py"""
    code = "\n# ======================== BATCH 6: RESPIRATORY, ANTIHISTAMINE & ANTIVIRAL ========================\n"
    code += "# Bổ sung contraindications_detail cho các thuốc hô hấp, kháng histamine và kháng virus\n\n"
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
    code += "# ======================== END BATCH 6 ========================\n"
    
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




