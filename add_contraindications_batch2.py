#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script bổ sung contraindications_detail cho các thuốc tim mạch quan trọng
Batch 2: 9 thuốc tim mạch
"""

from drugs.drug_database import DRUG_DATABASE

# Dữ liệu contraindications_detail cho các thuốc tim mạch
CONTRAINDICATIONS_DATA = {
    "Atenolol": {
        "contraindications_detail": {
            "tuyệt_đối": [
                "Dị ứng với atenolol hoặc beta-blocker",
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
                "Cường giáp - không dùng đơn độc",
                "Suy thận nặng (CrCl <30) - giảm liều",
                "Có thai - thận trọng",
                "Đang cho con bú - thận trọng",
            ],
        },
    },
    "Bisoprolol": {
        "contraindications_detail": {
            "tuyệt_đối": [
                "Dị ứng với bisoprolol hoặc beta-blocker",
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
                "Cường giáp - không dùng đơn độc",
                "Suy thận nặng (CrCl <30) - giảm liều",
                "Suy gan nặng - giảm liều",
                "Có thai - thận trọng",
                "Đang cho con bú - thận trọng",
            ],
        },
    },
    "Carvedilol": {
        "contraindications_detail": {
            "tuyệt_đối": [
                "Dị ứng với carvedilol hoặc beta-blocker",
                "Suy tim nặng không được điều trị (NYHA IV)",
                "Block nhĩ thất độ 2-3 không có máy tạo nhịp",
                "Sick sinus syndrome không có máy tạo nhịp",
                "Nhịp tim chậm nặng (<50 bpm)",
                "Sốc tim",
                "Hen suyễn nặng hoặc COPD nặng",
                "Suy gan nặng",
            ],
            "tương_đối": [
                "Suy tim vừa - bắt đầu với liều thấp",
                "Nhịp tim chậm vừa (50-60 bpm)",
                "Block nhĩ thất độ 1",
                "Hạ huyết áp tư thế",
                "Bệnh mạch máu ngoại biên",
                "Đái tháo đường - che dấu triệu chứng hạ đường huyết",
                "Suy thận nặng (CrCl <30) - giảm liều",
                "Suy gan vừa - giảm liều",
                "Có thai - thận trọng",
                "Đang cho con bú - thận trọng",
            ],
        },
    },
    "Nifedipine": {
        "contraindications_detail": {
            "tuyệt_đối": [
                "Dị ứng với nifedipine hoặc dihydropyridine",
                "Sốc tim",
                "Hẹp van động mạch chủ nặng",
                "Suy tim nặng không được điều trị",
            ],
            "tương_đối": [
                "Suy tim vừa - thận trọng",
                "Hạ huyết áp",
                "Suy gan nặng - giảm liều",
                "Suy thận nặng - thận trọng",
                "Có thai - thận trọng, có thể gây hạ huyết áp",
                "Đang cho con bú - thận trọng",
                "Người cao tuổi - tăng nhạy cảm",
            ],
        },
    },
    "Diltiazem": {
        "contraindications_detail": {
            "tuyệt_đối": [
                "Dị ứng với diltiazem",
                "Sick sinus syndrome không có máy tạo nhịp",
                "Block nhĩ thất độ 2-3 không có máy tạo nhịp",
                "Suy tim nặng (EF <30%)",
                "Sốc tim",
                "Hạ huyết áp nặng (SBP <90 mmHg)",
            ],
            "tương_đối": [
                "Suy tim vừa - thận trọng",
                "Nhịp tim chậm",
                "Block nhĩ thất độ 1",
                "Suy gan nặng - giảm liều",
                "Suy thận nặng - thận trọng",
                "Có thai - thận trọng",
                "Đang cho con bú - thận trọng",
            ],
        },
    },
    "Verapamil": {
        "contraindications_detail": {
            "tuyệt_đối": [
                "Dị ứng với verapamil",
                "Sick sinus syndrome không có máy tạo nhịp",
                "Block nhĩ thất độ 2-3 không có máy tạo nhịp",
                "Suy tim nặng (EF <30%)",
                "Sốc tim",
                "Hạ huyết áp nặng (SBP <90 mmHg)",
            ],
            "tương_đối": [
                "Suy tim vừa - thận trọng",
                "Nhịp tim chậm",
                "Block nhĩ thất độ 1",
                "Suy gan nặng - giảm liều đáng kể",
                "Suy thận nặng - thận trọng",
                "Có thai - thận trọng",
                "Đang cho con bú - thận trọng",
            ],
        },
    },
    "Hydrochlorothiazide": {
        "contraindications_detail": {
            "tuyệt_đối": [
                "Dị ứng với hydrochlorothiazide hoặc sulfonamide",
                "Vô niệu",
                "Suy thận nặng (CrCl <30)",
                "Hạ kali máu nặng không điều chỉnh được",
                "Tăng calci máu nặng",
            ],
            "tương_đối": [
                "Suy thận vừa (CrCl 30-60) - thận trọng",
                "Hạ kali máu - cần bổ sung kali",
                "Tăng calci máu vừa",
                "Gout - có thể làm tăng acid uric",
                "Đái tháo đường - có thể làm tăng đường huyết",
                "Suy gan - nguy cơ hôn mê gan",
                "Có thai - thận trọng, có thể gây giảm thể tích",
                "Đang cho con bú - thận trọng",
            ],
        },
    },
    "Spironolactone": {
        "contraindications_detail": {
            "tuyệt_đối": [
                "Dị ứng với spironolactone",
                "Suy thận nặng (CrCl <30)",
                "Tăng kali máu",
                "Vô niệu",
                "Bệnh Addison",
            ],
            "tương_đối": [
                "Suy thận vừa (CrCl 30-60) - thận trọng, theo dõi kali",
                "Đang dùng kali bổ sung hoặc thuốc giữ kali",
                "Đái tháo đường - tăng nguy cơ tăng kali máu",
                "Suy gan - nguy cơ hôn mê gan",
                "Có thai - thận trọng, có thể gây dị tật",
                "Đang cho con bú - thận trọng",
                "Người cao tuổi - tăng nguy cơ tăng kali máu",
            ],
        },
    },
    "Captopril": {
        "contraindications_detail": {
            "tuyệt_đối": [
                "Dị ứng với captopril hoặc ACE inhibitor",
                "Tiền sử phù mạch do ACE inhibitor",
                "Có thai (2-3 tháng giữa và cuối)",
                "Hẹp động mạch thận hai bên",
                "Hẹp động mạch thận một bên với thận độc nhất",
            ],
            "tương_đối": [
                "Suy thận nặng (CrCl <30) - giảm liều",
                "Suy gan nặng - thận trọng",
                "Hạ huyết áp",
                "Tăng kali máu",
                "Đang dùng thuốc giữ kali hoặc kali bổ sung",
                "Có thai (3 tháng đầu) - thận trọng",
                "Đang cho con bú - thận trọng",
                "Người cao tuổi - tăng nhạy cảm",
            ],
        },
    },
}

# Code để thêm vào enhanced_fields_overrides.py
def generate_code():
    """Tạo code để thêm vào enhanced_fields_overrides.py"""
    code = "\n# ======================== BATCH 2: CARDIOVASCULAR DRUGS ========================\n"
    code += "# Bổ sung contraindications_detail cho các thuốc tim mạch quan trọng\n\n"
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




