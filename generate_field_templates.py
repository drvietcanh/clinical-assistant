#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script tạo template cho các enhanced fields thiếu
"""

import json
from typing import Dict, List

def load_validation_report():
    """Đọc báo cáo validation"""
    try:
        with open('drug_validation_report.json', 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        print("❌ Không tìm thấy drug_validation_report.json")
        print("   Vui lòng chạy comprehensive_drug_validation.py trước")
        return None

def get_missing_drugs_by_field(report: Dict) -> Dict[str, List[str]]:
    """Lấy danh sách thuốc thiếu từng field"""
    missing_by_field = {}
    warnings_by_drug = report.get("warnings_by_drug", {})
    
    for drug, warnings in warnings_by_drug.items():
        for warning in warnings:
            if "Thiếu enhanced field:" in warning:
                field = warning.split("Thiếu enhanced field: ")[1].strip()
                if field not in missing_by_field:
                    missing_by_field[field] = []
                if drug not in missing_by_field[field]:
                    missing_by_field[field].append(drug)
            elif "Enhanced field rỗng:" in warning:
                field = warning.split("Enhanced field rỗng: ")[1].strip()
                if field not in missing_by_field:
                    missing_by_field[field] = []
                if drug not in missing_by_field[field]:
                    missing_by_field[field].append(drug)
    
    return missing_by_field

def generate_template(field_name: str) -> str:
    """Tạo template cho một field"""
    templates = {
        "contraindications_detail": '''"contraindications_detail": {
    "tuyệt_đối": [
        "Dị ứng thuốc",
        "Chống chỉ định cụ thể"
    ],
    "tương_đối": [
        "Thận trọng trong trường hợp",
        "Cần điều chỉnh liều"
    ]
}''',
        "reversal_agents": '''"reversal_agents": {
    "available": True,  # hoặc False nếu không có
    "agents": [
        {
            "name": "Tên thuốc giải độc",
            "dose": "Liều dùng",
            "route": "Đường dùng",
            "notes": "Ghi chú"
        }
    ]
}''',
        "black_box_warnings": '''"black_box_warnings": "Cảnh báo đặc biệt quan trọng về an toàn. Mô tả chi tiết các nguy cơ nghiêm trọng."''',
        "drug_interactions": '''"drug_interactions": {
    "major": [
        {
            "drug": "Tên thuốc",
            "mechanism": "Cơ chế tương tác",
            "effect": "Tác dụng",
            "management": "Cách xử lý"
        }
    ],
    "moderate": [],
    "minor": []
}''',
        "pregnancy_lactation": '''"pregnancy_lactation": {
    "fda_category": "X",  # A, B, C, D, hoặc X
    "pregnancy_details": "Chi tiết về sử dụng trong thai kỳ",
    "lactation": {
        "safety": "Compatible/Incompatible/Unknown",
        "details": "Chi tiết về sử dụng khi cho con bú",
        "recommendation": "Khuyến nghị"
    }
}''',
        "hepatic_adjustment": '''"hepatic_adjustment": {
    "mild": "Không đổi hoặc giảm liều X%",
    "moderate": "Giảm liều X%",
    "severe": "Không dùng hoặc giảm liều X%",
    "notes": "Ghi chú thêm"
}''',
        "renal_adjustment": '''"renal_adjustment": {
    "normal": "Không đổi",
    "30_60": "Giảm liều X%",
    "under_30": "Giảm liều X% hoặc không dùng",
    "notes": "Ghi chú thêm"
}''',
        "overdose_management": '''"overdose_management": {
    "symptoms": [
        "Triệu chứng 1",
        "Triệu chứng 2"
    ],
    "antidote": "Tên antidote hoặc 'Không có antidote đặc hiệu'",
    "treatment": [
        "Bước điều trị 1",
        "Bước điều trị 2"
    ],
    "monitoring": "Theo dõi các dấu hiệu sinh tồn và triệu chứng"
}''',
        "administration_instructions": '''"administration_instructions": {
    "oral": {
        "with_food": "Uống với thức ăn hoặc không",
        "timing": "Thời điểm uống"
    },
    "iv": {
        "reconstitution": "Cách pha",
        "infusion_rate": "Tốc độ truyền",
        "compatibility": ["Thuốc tương thích"],
        "incompatibility": ["Thuốc không tương thích"],
        "notes": "Ghi chú thêm"
    }
}'''
    }
    
    return templates.get(field_name, f'"{field_name}": "Template chưa có sẵn"')

def generate_templates_file(report: Dict):
    """Tạo file template cho tất cả fields thiếu"""
    missing_by_field = get_missing_drugs_by_field(report)
    field_completion = report["field_completion"]
    
    output = []
    output.append("# 📋 Templates Cho Enhanced Fields")
    output.append("")
    output.append("File này chứa templates để bổ sung các enhanced fields thiếu.")
    output.append("")
    output.append("---")
    output.append("")
    
    # Sắp xếp theo số lượng thiếu
    sorted_fields = sorted(
        field_completion.items(),
        key=lambda x: x[1]["missing"],
        reverse=True
    )
    
    for field, data in sorted_fields:
        if data["missing"] > 0:
            missing_count = data["missing"]
            missing_drugs = missing_by_field.get(field, [])[:10]  # 10 đầu tiên
            
            output.append(f"## {field}")
            output.append("")
            output.append(f"**Thiếu:** {missing_count} thuốc ({100-data['percentage']:.1f}%)")
            output.append("")
            output.append("**Template:**")
            output.append("```python")
            output.append(generate_template(field))
            output.append("```")
            output.append("")
            
            if missing_drugs:
                output.append("**Ví dụ thuốc cần bổ sung (10 đầu tiên):**")
                for drug in missing_drugs:
                    output.append(f"- {drug}")
                output.append("")
            
            output.append("---")
            output.append("")
    
    # Tạo file
    with open('field_templates.md', 'w', encoding='utf-8') as f:
        f.write('\n'.join(output))
    
    print("✅ Đã tạo file: field_templates.md")
    
    # Tạo file Python với templates
    py_output = []
    py_output.append('"""')
    py_output.append('Templates cho enhanced fields')
    py_output.append('Generated by generate_field_templates.py')
    py_output.append('"""')
    py_output.append("")
    py_output.append("FIELD_TEMPLATES = {")
    
    for field, data in sorted_fields:
        if data["missing"] > 0:
            template = generate_template(field)
            # Escape quotes
            template = template.replace('"', '\\"').replace('\n', '\\n')
            py_output.append(f'    "{field}": """{template}""",')
    
    py_output.append("}")
    
    with open('field_templates.py', 'w', encoding='utf-8') as f:
        f.write('\n'.join(py_output))
    
    print("✅ Đã tạo file: field_templates.py")

def main():
    """Hàm chính"""
    print("Đang tạo templates...")
    
    report = load_validation_report()
    if not report:
        return
    
    generate_templates_file(report)
    
    print("\n💡 Sử dụng:")
    print("   - Xem field_templates.md để biết template cho từng field")
    print("   - Import field_templates.py để sử dụng trong code")

if __name__ == '__main__':
    main()

