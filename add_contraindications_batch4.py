#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script bổ sung contraindications_detail cho các thuốc tiêu hóa và thần kinh
Batch 4: 8 thuốc quan trọng
"""

from drugs.drug_database import DRUG_DATABASE

# Dữ liệu contraindications_detail cho các thuốc
CONTRAINDICATIONS_DATA = {
    "Omeprazole": {
        "contraindications_detail": {
            "tuyệt_đối": [
                "Dị ứng với omeprazole hoặc PPI",
            ],
            "tương_đối": [
                "Suy gan nặng - giảm liều",
                "Suy thận nặng - không cần giảm liều nhưng thận trọng",
                "Loãng xương - tăng nguy cơ gãy xương khi dùng lâu dài",
                "Thiếu vitamin B12 - giảm hấp thu khi dùng lâu dài",
                "Nhiễm Clostridium difficile - tăng nguy cơ",
                "Có thai - thận trọng",
                "Đang cho con bú - thận trọng",
            ],
        },
    },
    "Pantoprazole": {
        "contraindications_detail": {
            "tuyệt_đối": [
                "Dị ứng với pantoprazole hoặc PPI",
            ],
            "tương_đối": [
                "Suy gan nặng - giảm liều",
                "Suy thận nặng - không cần giảm liều nhưng thận trọng",
                "Loãng xương - tăng nguy cơ gãy xương khi dùng lâu dài",
                "Thiếu vitamin B12 - giảm hấp thu khi dùng lâu dài",
                "Nhiễm Clostridium difficile - tăng nguy cơ",
                "Có thai - thận trọng",
                "Đang cho con bú - thận trọng",
            ],
        },
    },
    "Ranitidine": {
        "contraindications_detail": {
            "tuyệt_đối": [
                "Dị ứng với ranitidine hoặc H2 blocker",
            ],
            "tương_đối": [
                "Suy thận nặng (CrCl <50) - giảm liều",
                "Suy gan nặng - thận trọng",
                "Người cao tuổi - tăng nguy cơ tác dụng phụ",
                "Có thai - thận trọng",
                "Đang cho con bú - thận trọng",
            ],
        },
    },
    "Famotidine": {
        "contraindications_detail": {
            "tuyệt_đối": [
                "Dị ứng với famotidine hoặc H2 blocker",
            ],
            "tương_đối": [
                "Suy thận nặng (CrCl <50) - giảm liều",
                "Suy gan nặng - thận trọng",
                "Người cao tuổi - tăng nguy cơ tác dụng phụ",
                "Có thai - thận trọng",
                "Đang cho con bú - thận trọng",
            ],
        },
    },
    "Paracetamol": {
        "contraindications_detail": {
            "tuyệt_đối": [
                "Dị ứng với paracetamol",
                "Suy gan nặng",
                "Nghiện rượu nặng",
            ],
            "tương_đối": [
                "Suy gan vừa - giảm liều tối đa",
                "Suy thận nặng - thận trọng",
                "Thiếu G6PD - thận trọng",
                "Suy dinh dưỡng - tăng nguy cơ độc tính",
                "Có thai - thận trọng, nhưng an toàn tương đối",
                "Đang cho con bú - thận trọng",
            ],
        },
    },
    "Ibuprofen": {
        "contraindications_detail": {
            "tuyệt_đối": [
                "Dị ứng với ibuprofen hoặc NSAID",
                "Tiền sử hen suyễn do aspirin/NSAID",
                "Loét dạ dày tá tràng đang hoạt động",
                "Xuất huyết tiêu hóa đang hoạt động",
                "Suy tim nặng (NYHA III-IV)",
                "Có thai (3 tháng cuối) - nguy cơ đóng ống động mạch sớm",
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
                "Người cao tuổi - tăng nguy cơ tác dụng phụ",
            ],
        },
    },
    "Diclofenac": {
        "contraindications_detail": {
            "tuyệt_đối": [
                "Dị ứng với diclofenac hoặc NSAID",
                "Tiền sử hen suyễn do aspirin/NSAID",
                "Loét dạ dày tá tràng đang hoạt động",
                "Xuất huyết tiêu hóa đang hoạt động",
                "Suy tim nặng (NYHA III-IV)",
                "Suy gan nặng",
                "Suy thận nặng (CrCl <30)",
                "Có thai (3 tháng cuối) - nguy cơ đóng ống động mạch sớm",
            ],
            "tương_đối": [
                "Tiền sử loét dạ dày tá tràng",
                "Suy thận vừa (CrCl 30-60) - thận trọng",
                "Suy gan vừa - thận trọng",
                "Suy tim vừa - thận trọng",
                "Tăng huyết áp không kiểm soát",
                "Đang dùng thuốc chống đông",
                "Có thai (1-2 tháng đầu và giữa) - thận trọng",
                "Đang cho con bú - thận trọng",
                "Người cao tuổi - tăng nguy cơ tác dụng phụ",
            ],
        },
    },
    "Carbamazepine": {
        "contraindications_detail": {
            "tuyệt_đối": [
                "Dị ứng với carbamazepine",
                "Block nhĩ thất độ 2-3",
                "Suy gan nặng",
                "Tiền sử tủy xương bị ức chế",
                "Đang dùng MAO inhibitor",
            ],
            "tương_đối": [
                "Suy gan vừa - thận trọng, theo dõi chức năng gan",
                "Suy thận nặng - thận trọng",
                "Bệnh tim mạch - tăng nguy cơ block AV",
                "Bệnh nhân có tiền sử rối loạn tâm thần",
                "Glaucoma góc đóng",
                "Có thai - thận trọng, có thể gây dị tật",
                "Đang cho con bú - thận trọng",
                "Người cao tuổi - tăng nhạy cảm",
            ],
        },
    },
}

# Code để thêm vào enhanced_fields_overrides.py
def generate_code():
    """Tạo code để thêm vào enhanced_fields_overrides.py"""
    code = "\n# ======================== BATCH 4: GI & NEUROLOGICAL DRUGS ========================\n"
    code += "# Bổ sung contraindications_detail cho các thuốc tiêu hóa và thần kinh\n\n"
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

