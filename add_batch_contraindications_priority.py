#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script bổ sung contraindications_detail cho các thuốc ưu tiên (ICU/Emergency/Phổ biến)
Batch Priority: 15 thuốc quan trọng nhất
"""

from drugs.drug_database import DRUG_DATABASE

# Chọn 15 thuốc quan trọng từ danh sách thiếu
CONTRAINDICATIONS_DATA = {
    "Digoxin": {
        "contraindications_detail": {
            "tuyệt_đối": [
                "Dị ứng với digoxin hoặc digitalis glycosides",
                "Block nhĩ-thất độ 2-3 không có máy tạo nhịp",
                "Hội chứng Wolff-Parkinson-White (WPW) với rung nhĩ",
                "Rối loạn nhịp thất nặng (ventricular fibrillation, ventricular tachycardia không kiểm soát)",
            ],
            "tương_đối": [
                "Suy thận mức độ vừa-nặng (cần giảm liều và theo dõi nồng độ)",
                "Suy tim cấp mất bù (cần ổn định trước khi dùng)",
                "Hạ kali máu, hạ magie máu (tăng nguy cơ độc tính)",
                "Nhịp tim chậm <60 lần/phút (trừ khi có máy tạo nhịp)",
            ],
        },
    },
    "Fentanyl": {
        "contraindications_detail": {
            "tuyệt_đối": [
                "Dị ứng với fentanyl hoặc opioid",
                "Suy hô hấp nặng không có hỗ trợ thở máy",
                "Bệnh nhân đang dùng MAO inhibitors (trong vòng 14 ngày)",
            ],
            "tương_đối": [
                "Suy hô hấp mạn tính, COPD nặng (cần thận trọng, theo dõi sát)",
                "Tăng áp lực nội sọ, chấn thương sọ não",
                "Suy gan nặng (giảm chuyển hóa, tăng nguy cơ tích tụ)",
                "Phụ nữ có thai (category C, tránh dùng kéo dài)",
            ],
        },
    },
    "Hydromorphone": {
        "contraindications_detail": {
            "tuyệt_đối": [
                "Dị ứng với hydromorphone hoặc opioid",
                "Suy hô hấp nặng không có hỗ trợ thở máy",
                "Tắc ruột cơ học, liệt ruột",
            ],
            "tương_đối": [
                "Suy hô hấp mạn tính, COPD nặng",
                "Tăng áp lực nội sọ",
                "Suy gan nặng (giảm chuyển hóa)",
                "Suy thận nặng (tích tụ chất chuyển hóa)",
            ],
        },
    },
    "Insulin Regular": {
        "contraindications_detail": {
            "tuyệt_đối": [
                "Dị ứng với insulin hoặc bất kỳ thành phần nào",
                "Hạ đường huyết nặng đang diễn ra",
            ],
            "tương_đối": [
                "Suy thận nặng (cần điều chỉnh liều, theo dõi sát)",
                "Suy gan nặng (giảm chuyển hóa glucose, tăng nguy cơ hạ đường huyết)",
                "Bệnh nhân không có khả năng tự theo dõi đường huyết",
            ],
        },
    },
    "Nitroglycerin": {
        "contraindications_detail": {
            "tuyệt_đối": [
                "Dị ứng với nitroglycerin hoặc nitrate",
                "Hạ huyết áp nặng (systolic <90 mmHg)",
                "Thiếu máu cơ tim cấp do hẹp động mạch chủ nặng",
                "Viêm màng ngoài tim co thắt",
                "Đang dùng phosphodiesterase-5 inhibitors (sildenafil, tadalafil, vardenafil) - nguy cơ hạ huyết áp đe dọa tính mạng",
            ],
            "tương_đối": [
                "Hạ huyết áp nhẹ-vừa (theo dõi sát, có thể cần giảm liều)",
                "Thiếu máu nặng (giảm tải oxy)",
                "Tăng áp lực nội sọ",
                "Suy thận nặng (tích tụ chất chuyển hóa)",
            ],
        },
    },
    "Phenylephrine": {
        "contraindications_detail": {
            "tuyệt_đối": [
                "Dị ứng với phenylephrine",
                "Tăng huyết áp nặng không kiểm soát",
                "Bệnh mạch vành không ổn định, nhồi máu cơ tim cấp",
            ],
            "tương_đối": [
                "Tăng huyết áp vừa (theo dõi sát)",
                "Bệnh mạch vành, rối loạn nhịp tim",
                "Cường giáp (tăng nhạy cảm với catecholamine)",
                "Bệnh nhân đang dùng MAO inhibitors",
            ],
        },
    },
    "Vasopressin": {
        "contraindications_detail": {
            "tuyệt_đối": [
                "Dị ứng với vasopressin",
            ],
            "tương_đối": [
                "Bệnh mạch vành (có thể gây co mạch vành, thiếu máu cơ tim)",
                "Bệnh mạch máu ngoại biên nặng",
                "Suy thận nặng (giảm tưới máu thận)",
                "Hạ natri máu nặng (vasopressin có thể làm nặng thêm)",
            ],
        },
    },
    "Milrinone": {
        "contraindications_detail": {
            "tuyệt_đối": [
                "Dị ứng với milrinone",
                "Rối loạn nhịp thất nặng không kiểm soát",
            ],
            "tương_đối": [
                "Hạ huyết áp nặng (milrinone có thể gây giãn mạch)",
                "Rối loạn nhịp nhĩ hoặc thất (tăng nguy cơ)",
                "Suy thận nặng (giảm thải trừ, tăng nguy cơ tích tụ)",
                "Bệnh mạch vành không ổn định",
            ],
        },
    },
    "Nesiritide": {
        "contraindications_detail": {
            "tuyệt_đối": [
                "Dị ứng với nesiritide",
                "Hạ huyết áp nặng (systolic <90 mmHg)",
                "Sốc tim",
            ],
            "tương_đối": [
                "Hạ huyết áp vừa (theo dõi sát)",
                "Bệnh mạch vành không ổn định",
                "Suy thận nặng (giảm thải trừ)",
                "Hẹp van động mạch chủ nặng",
            ],
        },
    },
    "Clevidipine": {
        "contraindications_detail": {
            "tuyệt_đối": [
                "Dị ứng với clevidipine hoặc soy/egg (chứa trong dung dịch)",
                "Suy gan nặng",
            ],
            "tương_đối": [
                "Suy thận nặng (theo dõi sát)",
                "Bệnh mạch vành không ổn định (có thể gây phản xạ nhịp nhanh)",
                "Hạ huyết áp nhẹ-vừa (theo dõi sát)",
            ],
        },
    },
    "Nitroprusside": {
        "contraindications_detail": {
            "tuyệt_đối": [
                "Dị ứng với nitroprusside",
                "Thiếu máu cơ tim cấp do hẹp động mạch chủ nặng",
                "Thiếu hụt bẩm sinh cytochrome b5 reductase (nguy cơ nhiễm độc cyanide)",
            ],
            "tương_đối": [
                "Suy thận nặng (tích tụ thiocyanate, nguy cơ độc tính)",
                "Suy gan nặng (giảm chuyển hóa cyanide)",
                "Thiếu vitamin B12 (tăng nguy cơ nhiễm độc cyanide)",
                "Tăng áp lực nội sọ",
            ],
        },
    },
    "Rocuronium": {
        "contraindications_detail": {
            "tuyệt_đối": [
                "Dị ứng với rocuronium hoặc aminosteroid neuromuscular blocking agents",
            ],
            "tương_đối": [
                "Bệnh nhược cơ (myasthenia gravis) - cần giảm liều mạnh",
                "Rối loạn chức năng thần kinh cơ khác",
                "Suy thận nặng (kéo dài thời gian tác dụng)",
                "Suy gan nặng (kéo dài thời gian tác dụng)",
            ],
        },
    },
    "Succinylcholine": {
        "contraindications_detail": {
            "tuyệt_đối": [
                "Dị ứng với succinylcholine",
                "Tiền sử hoặc nguy cơ tăng kali máu nặng (bỏng nặng, chấn thương lớn, liệt tủy sống, bệnh cơ)",
                "Bệnh nhược cơ (myasthenia gravis) - có thể gây block kéo dài",
                "Rối loạn di truyền pseudocholinesterase (block kéo dài, nguy cơ ngừng thở)",
            ],
            "tương_đối": [
                "Tăng nhãn áp (có thể làm tăng áp lực nội nhãn)",
                "Tăng áp lực nội sọ",
                "Bệnh cơ di truyền (malignant hyperthermia, Duchenne muscular dystrophy)",
                "Suy gan nặng (giảm chuyển hóa)",
            ],
        },
    },
    "Vecuronium": {
        "contraindications_detail": {
            "tuyệt_đối": [
                "Dị ứng với vecuronium hoặc aminosteroid neuromuscular blocking agents",
            ],
            "tương_đối": [
                "Bệnh nhược cơ (myasthenia gravis) - cần giảm liều mạnh",
                "Rối loạn chức năng thần kinh cơ khác",
                "Suy thận nặng (kéo dài thời gian tác dụng)",
                "Suy gan nặng (kéo dài thời gian tác dụng)",
            ],
        },
    },
    "Thiopental": {
        "contraindications_detail": {
            "tuyệt_đối": [
                "Dị ứng với thiopental hoặc barbiturate",
                "Porphyria cấp (có thể gây cơn porphyria)",
                "Suy hô hấp nặng không có hỗ trợ thở máy",
            ],
            "tương_đối": [
                "Suy hô hấp mạn tính",
                "Suy tim nặng (có thể gây hạ huyết áp)",
                "Suy gan nặng (kéo dài thời gian tác dụng)",
                "Suy thận nặng (tích tụ)",
            ],
        },
    },
}

def generate_code():
    """Tạo code để thêm vào enhanced_fields_overrides.py"""
    code = "\n# ======================== BATCH PRIORITY: CONTRAINDICATIONS_DETAIL ========================\n"
    code += "# Bổ sung contraindications_detail cho 15 thuốc ưu tiên (ICU/Emergency/Phổ biến)\n"
    code += "# Generated automatically by add_batch_contraindications_priority.py\n\n"
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
    code += "# ======================== END BATCH PRIORITY ========================\n"
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

