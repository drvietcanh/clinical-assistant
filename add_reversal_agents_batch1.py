#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script bổ sung reversal_agents cho các thuốc có antidote quan trọng
Batch 1: Thuốc ICU/emergency có antidote
"""

from drugs.drug_database import DRUG_DATABASE

# Dữ liệu reversal_agents cho các thuốc có antidote
REVERSAL_AGENTS_DATA = {
    "Warfarin": {
        "reversal_agents": {
            "available": True,
            "agents": [
                {
                    "name": "Vitamin K (Phytomenadione)",
                    "dose": "1-10 mg IV hoặc 1-5 mg uống",
                    "route": "IV hoặc uống",
                    "notes": "Dùng khi INR >10 hoặc xuất huyết. Tác dụng chậm (6-24h).",
                },
                {
                    "name": "Prothrombin Complex Concentrate (PCC)",
                    "dose": "25-50 IU/kg",
                    "route": "IV",
                    "notes": "Dùng khi xuất huyết nặng cần đảo ngược nhanh. Tác dụng ngay lập tức.",
                },
                {
                    "name": "Fresh Frozen Plasma (FFP)",
                    "dose": "10-15 mL/kg",
                    "route": "IV",
                    "notes": "Thay thế khi không có PCC. Nguy cơ dị ứng và quá tải thể tích.",
                },
            ],
            "notes": "Vitamin K cho đảo ngược chậm, PCC cho đảo ngược nhanh khi xuất huyết nặng.",
        },
    },
    "Heparin": {
        "reversal_agents": {
            "available": True,
            "agents": [
                {
                    "name": "Protamine sulfate",
                    "dose": "1 mg/100 IU heparin (tối đa 50 mg)",
                    "route": "IV chậm",
                    "notes": "Đảo ngược hoàn toàn heparin. Nguy cơ phản ứng phản vệ, đặc biệt ở bệnh nhân đã dùng trước đó.",
                },
            ],
            "notes": "Protamine đảo ngược heparin ngay lập tức. Theo dõi phản ứng phản vệ.",
        },
    },
    "Morphine": {
        "reversal_agents": {
            "available": True,
            "agents": [
                {
                    "name": "Naloxone",
                    "dose": "0.4-2 mg IV (có thể lặp lại)",
                    "route": "IV, IM, hoặc intranasal",
                    "notes": "Đảo ngược hoàn toàn tác dụng opioid. Thời gian tác dụng ngắn (30-90 phút), có thể cần lặp lại.",
                },
            ],
            "notes": "Naloxone đảo ngược ngay lập tức. Cẩn thận với bệnh nhân phụ thuộc opioid (có thể gây hội chứng cai nghiện).",
        },
    },
    "Fentanyl": {
        "reversal_agents": {
            "available": True,
            "agents": [
                {
                    "name": "Naloxone",
                    "dose": "0.4-2 mg IV (có thể lặp lại)",
                    "route": "IV, IM, hoặc intranasal",
                    "notes": "Đảo ngược tác dụng opioid. Thời gian tác dụng ngắn hơn fentanyl, có thể cần lặp lại.",
                },
            ],
            "notes": "Naloxone đảo ngược ngay lập tức. Theo dõi sát vì fentanyl có thể tích tụ trong mô.",
        },
    },
    "Midazolam": {
        "reversal_agents": {
            "available": True,
            "agents": [
                {
                    "name": "Flumazenil",
                    "dose": "0.2 mg IV, lặp lại mỗi 1 phút đến tối đa 1 mg",
                    "route": "IV",
                    "notes": "Đảo ngược tác dụng benzodiazepine. Cẩn thận với bệnh nhân phụ thuộc (nguy cơ co giật).",
                },
            ],
            "notes": "Flumazenil đảo ngược ngay lập tức. Không dùng cho bệnh nhân phụ thuộc benzodiazepine hoặc đang dùng thuốc gây co giật.",
        },
    },
    "Propofol": {
        "reversal_agents": {
            "available": False,
            "agents": [],
            "notes": "Không có thuốc giải độc đặc hiệu. Điều trị hỗ trợ: ngừng thuốc, hỗ trợ hô hấp và tuần hoàn. Thời gian tác dụng ngắn (5-10 phút).",
        },
    },
    "Digoxin": {
        "reversal_agents": {
            "available": True,
            "agents": [
                {
                    "name": "Digoxin Immune Fab (Digibind)",
                    "dose": "Số ống = (nồng độ digoxin ng/mL × cân nặng kg) / 100",
                    "route": "IV",
                    "notes": "Đảo ngược hoàn toàn digoxin. Dùng khi ngộ độc nặng hoặc rối loạn nhịp tim đe dọa tính mạng.",
                },
            ],
            "notes": "Digoxin Immune Fab là điều trị đặc hiệu cho ngộ độc digoxin nặng. Đắt tiền nhưng hiệu quả.",
        },
    },
    "Insulin": {
        "reversal_agents": {
            "available": True,
            "agents": [
                {
                    "name": "Glucose (Dextrose)",
                    "dose": "50 mL D50W IV hoặc 1 mg glucagon IM",
                    "route": "IV hoặc IM",
                    "notes": "Điều trị hạ đường huyết do quá liều insulin. Theo dõi đường huyết sát.",
                },
                {
                    "name": "Glucagon",
                    "dose": "1 mg IM hoặc IV",
                    "route": "IM hoặc IV",
                    "notes": "Kích thích giải phóng glucose từ gan. Dùng khi không thể truyền glucose IV.",
                },
            ],
            "notes": "Glucose IV là điều trị chính. Glucagon dùng khi không thể truyền IV. Theo dõi đường huyết liên tục.",
        },
    },
    "Metformin": {
        "reversal_agents": {
            "available": False,
            "agents": [],
            "notes": "Không có thuốc giải độc đặc hiệu. Điều trị nhiễm toan lactic: ngừng metformin, điều chỉnh điện giải, có thể cần lọc máu.",
        },
    },
    "Aspirin": {
        "reversal_agents": {
            "available": False,
            "agents": [],
            "notes": "Không có thuốc giải độc đặc hiệu. Điều trị hỗ trợ: rửa dạ dày nếu mới uống, điều chỉnh nhiễm toan, hỗ trợ hô hấp. Có thể cần lọc máu trong trường hợp nặng.",
        },
    },
}

# Code để thêm vào enhanced_fields_overrides.py
def generate_code():
    """Tạo code để thêm vào enhanced_fields_overrides.py"""
    code = "\n# ======================== BATCH 1: REVERSAL AGENTS ========================\n"
    code += "# Bổ sung reversal_agents cho các thuốc có antidote quan trọng\n\n"
    code += "EXTRA_ENHANCED_FIELDS.update({\n"
    
    for drug_name, data in REVERSAL_AGENTS_DATA.items():
        code += f'    "{drug_name}": {{\n'
        code += '        "reversal_agents": {\n'
        code += f'            "available": {data["reversal_agents"]["available"]},\n'
        code += '            "agents": [\n'
        for agent in data["reversal_agents"]["agents"]:
            code += '                {\n'
            code += f'                    "name": "{agent["name"]}",\n'
            code += f'                    "dose": "{agent["dose"]}",\n'
            code += f'                    "route": "{agent["route"]}",\n'
            code += f'                    "notes": "{agent["notes"]}",\n'
            code += '                },\n'
        code += '            ],\n'
        code += f'            "notes": "{data["reversal_agents"]["notes"]}",\n'
        code += '        },\n'
        code += '    },\n'
    
    code += "})\n"
    code += "# ======================== END BATCH 1 REVERSAL AGENTS ========================\n"
    
    return code

if __name__ == '__main__':
    # Kiểm tra các thuốc có trong database không
    print("Kiểm tra các thuốc trong database:")
    for drug_name in REVERSAL_AGENTS_DATA.keys():
        if drug_name in DRUG_DATABASE:
            has_field = "reversal_agents" in DRUG_DATABASE[drug_name]
            print(f"  ✅ {drug_name}: {'Đã có' if has_field else 'THIẾU'} reversal_agents")
        else:
            print(f"  ❌ {drug_name}: Không tìm thấy trong database")
    
    print("\n" + "="*80)
    print("Code để thêm vào enhanced_fields_overrides.py:")
    print("="*80)
    print(generate_code())

