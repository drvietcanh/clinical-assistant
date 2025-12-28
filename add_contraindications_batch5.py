#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script bổ sung contraindications_detail cho các thuốc nội tiết và tim mạch phổ biến
Batch 5: 14 thuốc quan trọng
"""

from drugs.drug_database import DRUG_DATABASE

# Dữ liệu contraindications_detail cho các thuốc
CONTRAINDICATIONS_DATA = {
    "Levothyroxine": {
        "contraindications_detail": {
            "tuyệt_đối": [
                "Dị ứng với levothyroxine",
                "Cường giáp không được điều trị",
                "Nhồi máu cơ tim cấp",
                "Viêm cơ tim",
            ],
            "tương_đối": [
                "Bệnh tim mạch - bắt đầu với liều thấp",
                "Suy thượng thận - cần điều trị trước",
                "Đái tháo đường - có thể cần điều chỉnh liều insulin",
                "Có thai - cần tăng liều",
                "Đang cho con bú - thận trọng",
                "Người cao tuổi - bắt đầu với liều thấp",
            ],
        },
    },
    "Methimazole": {
        "contraindications_detail": {
            "tuyệt_đối": [
                "Dị ứng với methimazole",
            ],
            "tương_đối": [
                "Suy gan nặng - thận trọng",
                "Giảm bạch cầu - nguy cơ agranulocytosis",
                "Có thai (3 tháng đầu) - thận trọng, có thể gây dị tật",
                "Đang cho con bú - thận trọng",
                "Người cao tuổi - tăng nguy cơ tác dụng phụ",
            ],
        },
    },
    "Propylthiouracil": {
        "contraindications_detail": {
            "tuyệt_đối": [
                "Dị ứng với propylthiouracil",
            ],
            "tương_đối": [
                "Suy gan nặng - nguy cơ viêm gan",
                "Giảm bạch cầu - nguy cơ agranulocytosis",
                "Có thai (3 tháng đầu) - thận trọng",
                "Đang cho con bú - thận trọng",
                "Người cao tuổi - tăng nguy cơ tác dụng phụ",
            ],
        },
    },
    "Hydrocortisone": {
        "contraindications_detail": {
            "tuyệt_đối": [
                "Dị ứng với hydrocortisone hoặc corticosteroid",
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
    "Dexamethasone": {
        "contraindications_detail": {
            "tuyệt_đối": [
                "Dị ứng với dexamethasone hoặc corticosteroid",
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
    "Amlodipine": {
        "contraindications_detail": {
            "tuyệt_đối": [
                "Dị ứng với amlodipine hoặc dihydropyridine",
                "Sốc tim",
                "Hẹp van động mạch chủ nặng",
            ],
            "tương_đối": [
                "Suy tim nặng - thận trọng",
                "Hạ huyết áp",
                "Suy gan nặng - giảm liều",
                "Suy thận nặng - không cần giảm liều nhưng thận trọng",
                "Có thai - thận trọng",
                "Đang cho con bú - thận trọng",
                "Người cao tuổi - tăng nhạy cảm",
            ],
        },
    },
    "Metoprolol": {
        "contraindications_detail": {
            "tuyệt_đối": [
                "Dị ứng với metoprolol hoặc beta-blocker",
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
                "Suy gan nặng - giảm liều",
                "Có thai - thận trọng",
                "Đang cho con bú - thận trọng",
            ],
        },
    },
    "Propranolol": {
        "contraindications_detail": {
            "tuyệt_đối": [
                "Dị ứng với propranolol hoặc beta-blocker",
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
                "Suy gan nặng - giảm liều",
                "Có thai - thận trọng",
                "Đang cho con bú - thận trọng",
            ],
        },
    },
    "Furosemide": {
        "contraindications_detail": {
            "tuyệt_đối": [
                "Dị ứng với furosemide hoặc sulfonamide",
                "Vô niệu",
                "Hạ kali máu nặng không điều chỉnh được",
                "Hạ natri máu nặng",
            ],
            "tương_đối": [
                "Suy thận nặng - có thể cần tăng liều",
                "Suy gan nặng - nguy cơ hôn mê gan",
                "Hạ kali máu - cần bổ sung kali",
                "Hạ natri máu",
                "Hạ magie máu",
                "Gout - có thể làm tăng acid uric",
                "Đái tháo đường - có thể làm tăng đường huyết",
                "Có thai - thận trọng",
                "Đang cho con bú - thận trọng",
            ],
        },
    },
    "Atorvastatin": {
        "contraindications_detail": {
            "tuyệt_đối": [
                "Dị ứng với atorvastatin hoặc statin",
                "Bệnh gan đang hoạt động",
                "Tăng men gan không giải thích được (>3 lần ULN)",
                "Có thai",
                "Đang cho con bú",
            ],
            "tương_đối": [
                "Suy gan vừa - thận trọng",
                "Suy thận nặng - thận trọng",
                "Rối loạn cơ - tăng nguy cơ tiêu cơ vân",
                "Đang dùng thuốc ức chế CYP3A4 mạnh",
                "Nghiện rượu",
                "Người cao tuổi - tăng nguy cơ tác dụng phụ",
            ],
        },
    },
    "Simvastatin": {
        "contraindications_detail": {
            "tuyệt_đối": [
                "Dị ứng với simvastatin hoặc statin",
                "Bệnh gan đang hoạt động",
                "Tăng men gan không giải thích được (>3 lần ULN)",
                "Có thai",
                "Đang cho con bú",
            ],
            "tương_đối": [
                "Suy gan vừa - thận trọng",
                "Suy thận nặng - thận trọng",
                "Rối loạn cơ - tăng nguy cơ tiêu cơ vân",
                "Đang dùng thuốc ức chế CYP3A4 mạnh",
                "Nghiện rượu",
                "Người cao tuổi - tăng nguy cơ tác dụng phụ",
            ],
        },
    },
    "Valsartan": {
        "contraindications_detail": {
            "tuyệt_đối": [
                "Dị ứng với valsartan hoặc ARB",
                "Có thai (2-3 tháng giữa và cuối)",
                "Hẹp động mạch thận hai bên",
                "Hẹp động mạch thận một bên với thận độc nhất",
            ],
            "tương_đối": [
                "Suy thận nặng (CrCl <30) - thận trọng",
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
    "Ramipril": {
        "contraindications_detail": {
            "tuyệt_đối": [
                "Dị ứng với ramipril hoặc ACE inhibitor",
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
    "Perindopril": {
        "contraindications_detail": {
            "tuyệt_đối": [
                "Dị ứng với perindopril hoặc ACE inhibitor",
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
    code = "\n# ======================== BATCH 5: ENDOCRINE & CARDIOVASCULAR ========================\n"
    code += "# Bổ sung contraindications_detail cho các thuốc nội tiết và tim mạch phổ biến\n\n"
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
    code += "# ======================== END BATCH 5 ========================\n"
    
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

