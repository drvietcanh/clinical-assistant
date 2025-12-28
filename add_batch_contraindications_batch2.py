#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script bổ sung contraindications_detail cho các thuốc quan trọng (Batch 2)
15 thuốc tiếp theo: Kháng sinh, tim mạch, thần kinh
"""

from drugs.drug_database import DRUG_DATABASE

CONTRAINDICATIONS_DATA = {
    "Cefepime": {
        "contraindications_detail": {
            "tuyệt_đối": [
                "Dị ứng với cefepime hoặc cephalosporin",
                "Dị ứng nặng với penicillin (phản ứng chéo có thể xảy ra)",
            ],
            "tương_đối": [
                "Suy thận nặng (cần điều chỉnh liều)",
                "Tiền sử viêm đại tràng do Clostridium difficile",
                "Rối loạn đông máu (cefepime có thể gây giảm prothrombin)",
            ],
        },
    },
    "Cefotaxime": {
        "contraindications_detail": {
            "tuyệt_đối": [
                "Dị ứng với cefotaxime hoặc cephalosporin",
                "Dị ứng nặng với penicillin",
            ],
            "tương_đối": [
                "Suy thận nặng (cần điều chỉnh liều)",
                "Tiền sử viêm đại tràng do C. difficile",
                "Rối loạn đông máu",
            ],
        },
    },
    "Cefuroxime": {
        "contraindications_detail": {
            "tuyệt_đối": [
                "Dị ứng với cefuroxime hoặc cephalosporin",
                "Dị ứng nặng với penicillin",
            ],
            "tương_đối": [
                "Suy thận nặng (cần điều chỉnh liều)",
                "Tiền sử viêm đại tràng do C. difficile",
            ],
        },
    },
    "Cephalexin": {
        "contraindications_detail": {
            "tuyệt_đối": [
                "Dị ứng với cephalexin hoặc cephalosporin",
                "Dị ứng nặng với penicillin",
            ],
            "tương_đối": [
                "Suy thận nặng (cần điều chỉnh liều)",
                "Tiền sử viêm đại tràng do C. difficile",
            ],
        },
    },
    "Caspofungin": {
        "contraindications_detail": {
            "tuyệt_đối": [
                "Dị ứng với caspofungin hoặc echinocandin",
            ],
            "tương_đối": [
                "Suy gan nặng (cần điều chỉnh liều)",
                "Đang dùng cyclosporine (tăng nguy cơ độc tính gan)",
            ],
        },
    },
    "Cisplatin": {
        "contraindications_detail": {
            "tuyệt_đối": [
                "Dị ứng với cisplatin hoặc platinum compounds",
                "Suy thận nặng (eGFR <30 mL/min)",
                "Giảm thính lực nặng",
            ],
            "tương_đối": [
                "Suy thận vừa (cần điều chỉnh liều và theo dõi sát)",
                "Suy tim, bệnh mạch vành",
                "Giảm bạch cầu hoặc tiểu cầu nặng",
                "Bệnh thần kinh ngoại biên",
            ],
        },
    },
    "Carboplatin": {
        "contraindications_detail": {
            "tuyệt_đối": [
                "Dị ứng với carboplatin hoặc platinum compounds",
                "Suy thận nặng (eGFR <30 mL/min)",
            ],
            "tương_đối": [
                "Suy thận vừa (cần điều chỉnh liều theo AUC)",
                "Giảm bạch cầu hoặc tiểu cầu nặng",
                "Suy gan nặng",
            ],
        },
    },
    "Baclofen": {
        "contraindications_detail": {
            "tuyệt_đối": [
                "Dị ứng với baclofen",
            ],
            "tương_đối": [
                "Suy thận nặng (tăng nguy cơ độc tính, cần giảm liều)",
                "Động kinh không kiểm soát",
                "Rối loạn tâm thần",
                "Loét dạ dày tá tràng",
            ],
        },
    },
    "Bupropion": {
        "contraindications_detail": {
            "tuyệt_đối": [
                "Dị ứng với bupropion",
                "Động kinh hoặc tiền sử động kinh",
                "Đang dùng MAO inhibitors (trong vòng 14 ngày)",
                "Rối loạn ăn uống (anorexia nervosa, bulimia nervosa)",
            ],
            "tương_đối": [
                "Tiền sử động kinh hoặc yếu tố nguy cơ co giật",
                "Chấn thương đầu, u não",
                "Rối loạn gan nặng",
                "Tăng huyết áp không kiểm soát",
            ],
        },
    },
    "Buprenorphine": {
        "contraindications_detail": {
            "tuyệt_đối": [
                "Dị ứng với buprenorphine hoặc opioid",
                "Suy hô hấp nặng không có hỗ trợ thở máy",
                "Đang dùng MAO inhibitors (trong vòng 14 ngày)",
            ],
            "tương_đối": [
                "Suy hô hấp mạn tính, COPD nặng",
                "Suy gan nặng (giảm chuyển hóa)",
                "Tăng áp lực nội sọ",
                "Phụ nữ có thai (category C)",
            ],
        },
    },
    "Candesartan": {
        "contraindications_detail": {
            "tuyệt_đối": [
                "Dị ứng với candesartan hoặc ARB",
                "Phụ nữ có thai (tháng 2-3, category D)",
                "Hẹp động mạch thận hai bên hoặc một bên ở bệnh nhân một thận",
            ],
            "tương_đối": [
                "Suy thận nặng (theo dõi chức năng thận)",
                "Hạ huyết áp",
                "Tăng kali máu",
                "Hẹp động mạch thận một bên",
            ],
        },
    },
    "Benazepril": {
        "contraindications_detail": {
            "tuyệt_đối": [
                "Dị ứng với benazepril hoặc ACE inhibitor",
                "Phụ nữ có thai (tháng 2-3, category D)",
                "Phù mạch do ACE inhibitor trước đó",
                "Hẹp động mạch thận hai bên hoặc một bên ở bệnh nhân một thận",
            ],
            "tương_đối": [
                "Suy thận nặng (theo dõi chức năng thận)",
                "Hạ huyết áp",
                "Tăng kali máu",
                "Bệnh mô liên kết (tăng nguy cơ neutropenia)",
            ],
        },
    },
    "Canagliflozin": {
        "contraindications_detail": {
            "tuyệt_đối": [
                "Dị ứng với canagliflozin hoặc SGLT2 inhibitor",
                "Suy thận nặng (eGFR <30 mL/min)",
                "Nhiễm toan ceton do đái tháo đường",
            ],
            "tương_đối": [
                "Suy thận vừa (eGFR 30-60, cần điều chỉnh liều)",
                "Suy tim nặng",
                "Nhiễm trùng đường tiết niệu tái phát",
                "Nhiễm nấm sinh dục",
            ],
        },
    },
    "Chlorpromazine": {
        "contraindications_detail": {
            "tuyệt_đối": [
                "Dị ứng với chlorpromazine hoặc phenothiazine",
                "Coma do thuốc ức chế thần kinh trung ương",
                "Giảm bạch cầu nặng",
            ],
            "tương_đối": [
                "Bệnh tim mạch nặng",
                "Động kinh",
                "Bệnh gan",
                "Parkinson",
                "Glaucoma góc đóng",
            ],
        },
    },
    "Chloroquine": {
        "contraindications_detail": {
            "tuyệt_đối": [
                "Dị ứng với chloroquine",
                "Bệnh võng mạc do chloroquine",
                "Rối loạn nhịp tim nặng",
            ],
            "tương_đối": [
                "Bệnh gan nặng",
                "Bệnh thận nặng",
                "Bệnh cơ (myopathy)",
                "Bệnh máu (porphyria)",
                "Rối loạn tâm thần",
            ],
        },
    },
}

def generate_code():
    """Tạo code để thêm vào enhanced_fields_overrides.py"""
    code = "\n# ======================== BATCH 2: CONTRAINDICATIONS_DETAIL ========================\n"
    code += "# Bổ sung contraindications_detail cho 15 thuốc quan trọng (Kháng sinh, Tim mạch, Thần kinh)\n"
    code += "# Generated automatically by add_batch_contraindications_batch2.py\n\n"
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
    code += "# ======================== END BATCH 2 ========================\n"
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

