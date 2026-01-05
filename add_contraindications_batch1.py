#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script bổ sung contraindications_detail cho các thuốc ICU/emergency quan trọng
Batch 1: 7 thuốc ICU/emergency
"""

from drugs.drug_database import DRUG_DATABASE

# Dữ liệu contraindications_detail cho các thuốc ICU/emergency
CONTRAINDICATIONS_DATA = {
    "Alteplase": {
        "contraindications_detail": {
            "tuyệt_đối": [
                "Dị ứng với alteplase hoặc bất kỳ thành phần nào",
                "Xuất huyết nội sọ đang hoạt động",
                "Tiền sử đột quỵ xuất huyết",
                "Chấn thương đầu hoặc phẫu thuật đầu gần đây (3 tháng)",
                "Xuất huyết tiêu hóa hoặc tiết niệu trong 21 ngày",
                "Rối loạn đông máu",
                "Huyết áp tâm thu >185 mmHg hoặc tâm trương >110 mmHg không kiểm soát được",
            ],
            "tương_đối": [
                "Tuổi >80 tuổi - tăng nguy cơ xuất huyết",
                "Điểm NIHSS >25 - nguy cơ cao",
                "Điều trị kháng đông trong 48 giờ",
                "Tiểu cầu <100,000/mm³",
                "INR >1.7 hoặc PT >15 giây",
                "Đường huyết <50 mg/dL hoặc >400 mg/dL",
                "Đột quỵ nhẹ hoặc TIA trong 3 tháng",
            ],
        },
    },
    "Aspirin": {
        "contraindications_detail": {
            "tuyệt_đối": [
                "Dị ứng với aspirin hoặc NSAID",
                "Tiền sử hen suyễn do aspirin",
                "Xuất huyết tiêu hóa đang hoạt động",
                "Loét dạ dày tá tràng đang hoạt động",
                "Rối loạn đông máu (hemophilia, von Willebrand)",
                "Suy gan nặng",
                "Suy thận nặng (CrCl <30)",
                "Trẻ em <16 tuổi (nguy cơ hội chứng Reye)",
            ],
            "tương_đối": [
                "Tiền sử loét dạ dày tá tràng",
                "Đang dùng thuốc chống đông",
                "Suy thận vừa (CrCl 30-60)",
                "Suy gan vừa",
                "Có thai (3 tháng cuối)",
                "Đang cho con bú",
                "Gout - có thể làm tăng acid uric",
            ],
        },
    },
    "Epinephrine": {
        "contraindications_detail": {
            "tuyệt_đối": [
                "Dị ứng với epinephrine hoặc bất kỳ thành phần nào",
                "Rối loạn nhịp tim nặng không kiểm soát được",
                "Phẫu thuật tim gần đây",
            ],
            "tương_đối": [
                "Bệnh tim mạch nặng",
                "Tăng huyết áp nặng",
                "Đái tháo đường",
                "Cường giáp",
                "Glaucoma góc đóng",
                "Bệnh mạch máu ngoại biên",
                "Người cao tuổi - tăng nhạy cảm",
            ],
        },
    },
    "Morphine": {
        "contraindications_detail": {
            "tuyệt_đối": [
                "Dị ứng với morphine hoặc opioid",
                "Suy hô hấp nặng không có hỗ trợ thở máy",
                "Hen suyễn nặng không kiểm soát",
                "Tắc ruột cơ học",
                "Tăng áp lực nội sọ",
                "Ức chế hô hấp nặng",
            ],
            "tương_đối": [
                "Suy hô hấp vừa",
                "Suy gan nặng",
                "Suy thận nặng (CrCl <30)",
                "Người cao tuổi - giảm liều",
                "Có thai - nguy cơ ức chế hô hấp ở trẻ sơ sinh",
                "Đang cho con bú",
                "Tiền sử lạm dụng chất",
                "Bệnh động kinh",
            ],
        },
    },
    "Metformin": {
        "contraindications_detail": {
            "tuyệt_đối": [
                "Dị ứng với metformin",
                "Suy thận nặng (CrCl <30 mL/min)",
                "Nhiễm toan lactic",
                "Suy gan nặng",
                "Suy tim nặng cần điều trị bằng thuốc",
                "Nhiễm trùng nặng hoặc mất nước nặng",
            ],
            "tương_đối": [
                "Suy thận vừa (CrCl 30-45) - giảm liều",
                "Suy gan vừa - thận trọng",
                "Người cao tuổi >80 tuổi - giảm liều",
                "Nghiện rượu",
                "Phẫu thuật lớn hoặc thủ thuật có cản quang - tạm ngừng",
                "Có thai - thận trọng",
                "Đang cho con bú - thận trọng",
            ],
        },
    },
    "Naloxone": {
        "contraindications_detail": {
            "tuyệt_đối": [
                "Dị ứng với naloxone hoặc bất kỳ thành phần nào",
            ],
            "tương_đối": [
                "Bệnh nhân phụ thuộc opioid - có thể gây hội chứng cai nghiện nặng",
                "Bệnh tim mạch - có thể gây rối loạn nhịp tim",
                "Có thai - thận trọng",
                "Đang cho con bú - thận trọng",
            ],
        },
    },
    "Flumazenil": {
        "contraindications_detail": {
            "tuyệt_đối": [
                "Dị ứng với flumazenil hoặc benzodiazepine",
                "Bệnh nhân phụ thuộc benzodiazepine - nguy cơ co giật",
                "Đang dùng thuốc gây co giật (TCA, bupropion)",
            ],
            "tương_đối": [
                "Bệnh nhân có tiền sử co giật",
                "Tổn thương não",
                "Có thai - thận trọng",
                "Đang cho con bú - thận trọng",
                "Suy gan nặng - thời gian tác dụng kéo dài",
            ],
        },
    },
}

# Code để thêm vào enhanced_fields_overrides.py
def generate_code():
    """Tạo code để thêm vào enhanced_fields_overrides.py"""
    code = "\n# ======================== BATCH 1: ICU/EMERGENCY DRUGS ========================\n"
    code += "# Bổ sung contraindications_detail cho các thuốc ICU/emergency quan trọng\n\n"
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
    code += "# ======================== END BATCH 1 ========================\n"
    
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




