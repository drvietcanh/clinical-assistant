#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script bổ sung contraindications_detail cho các thuốc quan trọng còn thiếu
Batch 8: 15 thuốc đa dạng (tiếp tục)
"""

from drugs.drug_database import DRUG_DATABASE

# Dữ liệu contraindications_detail cho các thuốc
CONTRAINDICATIONS_DATA = {
    "Artesunate": {
        "contraindications_detail": {
            "tuyệt_đối": [
                "Dị ứng với artesunate",
                "Có thai (3 tháng đầu)",
            ],
            "tương_đối": [
                "Suy gan nặng - thận trọng",
                "Suy thận nặng - thận trọng",
                "Bệnh tim mạch - thận trọng",
                "Có thai (3 tháng giữa và cuối) - thận trọng",
                "Đang cho con bú - thận trọng",
            ],
        },
    },
    "Artificial tears (Carboxymethylcellulose)": {
        "contraindications_detail": {
            "tuyệt_đối": [
                "Dị ứng với carboxymethylcellulose hoặc thành phần",
            ],
            "tương_đối": [
                "Nhiễm trùng mắt đang hoạt động",
                "Tổn thương giác mạc nặng",
            ],
        },
    },
    "Azelaic acid topical": {
        "contraindications_detail": {
            "tuyệt_đối": [
                "Dị ứng với azelaic acid",
            ],
            "tương_đối": [
                "Da bị kích ứng nặng",
                "Vết thương hở tại vùng điều trị",
                "Có thai - thận trọng",
                "Đang cho con bú - thận trọng",
            ],
        },
    },
    "Azelastine eye drops": {
        "contraindications_detail": {
            "tuyệt_đối": [
                "Dị ứng với azelastine",
            ],
            "tương_đối": [
                "Nhiễm trùng mắt đang hoạt động",
                "Tổn thương giác mạc",
                "Đeo kính áp tròng mềm",
                "Có thai - thận trọng",
                "Đang cho con bú - thận trọng",
            ],
        },
    },
    "Bedaquiline": {
        "contraindications_detail": {
            "tuyệt_đối": [
                "Dị ứng với bedaquiline",
                "Rối loạn nhịp tim nặng",
                "Kéo dài QTc >500 ms",
            ],
            "tương_đối": [
                "Bệnh tim mạch - tăng nguy cơ kéo dài QT",
                "Đang dùng thuốc kéo dài QT",
                "Suy gan nặng - thận trọng",
                "Suy thận nặng - thận trọng",
                "Có thai - thận trọng",
                "Đang cho con bú - thận trọng",
            ],
        },
    },
    "Bempedoic acid": {
        "contraindications_detail": {
            "tuyệt_đối": [
                "Dị ứng với bempedoic acid",
            ],
            "tương_đối": [
                "Suy gan nặng - thận trọng",
                "Suy thận nặng - thận trọng",
                "Bệnh gút - tăng nguy cơ",
                "Đứt gân - tăng nguy cơ",
                "Có thai - thận trọng",
                "Đang cho con bú - thận trọng",
            ],
        },
    },
    "Benzoyl peroxide topical": {
        "contraindications_detail": {
            "tuyệt_đối": [
                "Dị ứng với benzoyl peroxide",
            ],
            "tương_đối": [
                "Da bị kích ứng nặng",
                "Vết thương hở tại vùng điều trị",
                "Da nhạy cảm với ánh sáng",
                "Có thai - thận trọng",
                "Đang cho con bú - thận trọng",
            ],
        },
    },
    "Betamethasone": {
        "contraindications_detail": {
            "tuyệt_đối": [
                "Dị ứng với betamethasone hoặc corticosteroid",
                "Nhiễm trùng hệ thống không được điều trị",
                "Nhiễm nấm toàn thân",
            ],
            "tương_đối": [
                "Đái tháo đường - tăng đường huyết",
                "Tăng huyết áp",
                "Loãng xương",
                "Loét dạ dày tá tràng",
                "Suy tim nặng",
                "Suy gan nặng",
                "Suy thận nặng",
                "Có thai - thận trọng, có thể gây dị tật",
                "Đang cho con bú - thận trọng",
                "Trẻ em - ảnh hưởng đến tăng trưởng",
            ],
        },
    },
    "Bictegravir (BIC)": {
        "contraindications_detail": {
            "tuyệt_đối": [
                "Dị ứng với bictegravir",
            ],
            "tương_đối": [
                "Suy gan nặng - thận trọng",
                "Suy thận nặng (CrCl <30) - thận trọng",
                "Đang dùng thuốc ức chế CYP3A mạnh",
                "Có thai - thận trọng",
                "Đang cho con bú - thận trọng",
            ],
        },
    },
    "Budesonide inhaled": {
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
    "Calcitriol": {
        "contraindications_detail": {
            "tuyệt_đối": [
                "Dị ứng với calcitriol",
                "Tăng calci máu",
                "Tăng vitamin D máu",
            ],
            "tương_đối": [
                "Suy thận nặng - thận trọng",
                "Sỏi thận",
                "Bệnh tim mạch",
                "Có thai - thận trọng",
                "Đang cho con bú - thận trọng",
            ],
        },
    },
    "Ceftazidime": {
        "contraindications_detail": {
            "tuyệt_đối": [
                "Dị ứng với ceftazidime hoặc cephalosporin",
                "Tiền sử phản ứng phản vệ với beta-lactam",
            ],
            "tương_đối": [
                "Dị ứng với penicillin - thận trọng",
                "Suy thận nặng (CrCl <30) - giảm liều",
                "Suy gan nặng - thận trọng",
                "Có thai - thận trọng",
                "Đang cho con bú - thận trọng",
            ],
        },
    },
    "Ceftolozane/Tazobactam": {
        "contraindications_detail": {
            "tuyệt_đối": [
                "Dị ứng với ceftolozane, tazobactam hoặc beta-lactam",
                "Tiền sử phản ứng phản vệ với beta-lactam",
            ],
            "tương_đối": [
                "Dị ứng với penicillin - thận trọng",
                "Suy thận nặng (CrCl <30) - giảm liều",
                "Suy gan nặng - thận trọng",
                "Có thai - thận trọng",
                "Đang cho con bú - thận trọng",
            ],
        },
    },
    "Celecoxib": {
        "contraindications_detail": {
            "tuyệt_đối": [
                "Dị ứng với celecoxib hoặc sulfonamide",
                "Tiền sử hen suyễn do aspirin/NSAID",
                "Loét dạ dày tá tràng đang hoạt động",
                "Xuất huyết tiêu hóa đang hoạt động",
                "Suy tim nặng (NYHA III-IV)",
                "Có thai (3 tháng cuối)",
            ],
            "tương_đối": [
                "Tiền sử loét dạ dày tá tràng",
                "Suy thận nặng (CrCl <30) - thận trọng",
                "Suy gan nặng - thận trọng",
                "Suy tim vừa - thận trọng",
                "Tăng huyết áp không kiểm soát",
                "Đang dùng thuốc chống đông",
                "Có thai (1-2 tháng đầu và giữa) - thận trọng",
                "Đang cho con bú - thận trọng",
            ],
        },
    },
    "Chloramphenicol": {
        "contraindications_detail": {
            "tuyệt_đối": [
                "Dị ứng với chloramphenicol",
                "Ức chế tủy xương",
            ],
            "tương_đối": [
                "Suy gan nặng - thận trọng",
                "Suy thận nặng - thận trọng",
                "Trẻ sơ sinh - nguy cơ hội chứng xám",
                "Có thai - thận trọng",
                "Đang cho con bú - thận trọng",
            ],
        },
    },
}

# Code để thêm vào enhanced_fields_overrides.py
def generate_code():
    """Tạo code để thêm vào enhanced_fields_overrides.py"""
    code = "\n# ======================== BATCH 8: MIXED IMPORTANT DRUGS (CONTINUED) ========================\n"
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
    code += "# ======================== END BATCH 8 ========================\n"
    
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

