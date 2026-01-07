#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script để bổ sung các fields còn thiếu cho GLP-1 agonists
"""

import re

# Template cho renal_adjustment (GLP-1 agonists)
RENAL_ADJUSTMENT_TEMPLATE = '''        "renal_adjustment": {
            "normal": "Không cần chỉnh liều",
            "30_60": "Có thể dùng nhưng thận trọng. Theo dõi chức năng thận.",
            "under_30": "Thận trọng, có thể cần giảm liều. GLP-1 agonists thải trừ qua thận một phần.",
            "dialysis": "Thận trọng. Không có dữ liệu đầy đủ về an toàn ở bệnh nhân lọc máu.",
            "notes": "GLP-1 agonists thải trừ một phần qua thận. Suy thận có thể làm tăng nồng độ thuốc. Cần theo dõi chức năng thận và điều chỉnh liều nếu cần."
        },'''

# Template cho drug_interactions (GLP-1 agonists)
DRUG_INTERACTIONS_TEMPLATE = '''        "drug_interactions": {
            "major": [],
            "moderate": [
                {
                    "drug": "Insulin, Sulfonylureas",
                    "mechanism": "GLP-1 agonists tăng tiết insulin, có thể tăng nguy cơ hạ đường huyết",
                    "effect": "Tăng nguy cơ hạ đường huyết",
                    "management": "Giảm liều insulin hoặc sulfonylurea khi bắt đầu GLP-1 agonist. Theo dõi đường huyết chặt chẽ."
                }
            ],
            "minor": [
                {
                    "drug": "Thuốc uống (nói chung)",
                    "mechanism": "GLP-1 agonists làm chậm làm rỗng dạ dày, có thể ảnh hưởng hấp thu thuốc uống",
                    "effect": "Có thể giảm hấp thu hoặc làm chậm tác dụng của thuốc uống",
                    "management": "Theo dõi tác dụng của thuốc uống. Có thể cần điều chỉnh liều hoặc thời gian uống."
                },
                {
                    "drug": "Warfarin",
                    "mechanism": "GLP-1 agonists có thể ảnh hưởng nhẹ đến chuyển hóa warfarin",
                    "effect": "Có thể thay đổi INR nhẹ",
                    "management": "Theo dõi INR khi bắt đầu hoặc thay đổi liều GLP-1 agonist."
                }
            ]
        },'''

# Template cho reversal_agents (GLP-1 agonists)
REVERSAL_AGENTS_TEMPLATE = '''        "reversal_agents": {
            "available": False,
            "agents": [],
            "notes": "Không có antidote đặc hiệu. Điều trị quá liều chủ yếu là hỗ trợ: ngừng thuốc, điều chỉnh đường huyết nếu hạ đường huyết, điều trị viêm tụy nếu có."
        },'''

# Template cho contraindications_detail (GLP-1 agonists)
def get_contraindications_detail_template(drug_name):
    return f'''        "contraindications_detail": {{
            "tuyệt_đối": [
                "Tiền sử ung thư tuyến giáp tủy (MTC) hoặc hội chứng u nội tiết đa tuyến type 2 (MEN 2)",
                "Tiền sử viêm tụy cấp",
                "Đái tháo đường type 1",
                "Nhiễm toan ceton do đái tháo đường",
                "Dị ứng với {drug_name} hoặc bất kỳ thành phần nào"
            ],
            "tương_đối": [
                "Suy thận - thận trọng, có thể cần giảm liều",
                "Suy gan - thận trọng, theo dõi chức năng gan",
                "Bệnh nhân cao tuổi - tăng nguy cơ buồn nôn, mất nước",
                "Bệnh nhân có bệnh dạ dày - tăng nguy cơ buồn nôn, nôn",
                "Phụ nữ có thai - không có dữ liệu đầy đủ về an toàn"
            ]
        }},'''

def add_fields_to_drug(content, drug_name):
    """Thêm các fields còn thiếu cho một GLP-1 agonist"""
    
    # Tìm vị trí của drug
    pattern = rf'    "{drug_name}":\s+\{{'
    match = re.search(pattern, content)
    if not match:
        print(f"Không tìm thấy {drug_name}")
        return content
    
    start_pos = match.start()
    
    # Tìm vị trí kết thúc của drug
    next_drug_pattern = r'\n    "[^"]+":\s+\{'
    next_match = re.search(next_drug_pattern, content[start_pos + 100:])
    if next_match:
        end_pos = start_pos + 100 + next_match.start()
    else:
        end_pos = len(content)
    
    drug_section = content[start_pos:end_pos]
    
    # Kiểm tra xem đã có các fields chưa
    has_contraindications_detail = '"contraindications_detail"' in drug_section
    has_renal_adjustment = '"renal_adjustment"' in drug_section
    has_drug_interactions = '"drug_interactions"' in drug_section and '"major": [' in drug_section
    has_reversal_agents = '"reversal_agents"' in drug_section and '"reversal_agents": {' in drug_section
    
    if has_contraindications_detail and has_renal_adjustment and has_drug_interactions and has_reversal_agents:
        print(f"{drug_name}: Đã có đầy đủ fields")
        return content
    
    # Bổ sung contraindications_detail (sau contraindications)
    if not has_contraindications_detail:
        contraindications_pattern = r'"contraindications":\s+\[[^\]]+\],'
        contraindications_match = re.search(contraindications_pattern, drug_section)
        if contraindications_match:
            insert_pos = start_pos + contraindications_match.end()
            drug_name_short = drug_name.lower()
            new_field = get_contraindications_detail_template(drug_name_short)
            content = content[:insert_pos] + "\n" + new_field + content[insert_pos:]
            print(f"{drug_name}: Đã thêm contraindications_detail")
            end_pos += len(new_field) + 1
            drug_section = content[start_pos:end_pos]
    
    # Bổ sung renal_adjustment (sau hepatic_adjustment)
    if not has_renal_adjustment:
        hepatic_pattern = r'"hepatic_adjustment":\s+\{[^}]+\},'
        hepatic_match = re.search(hepatic_pattern, drug_section, re.DOTALL)
        if hepatic_match:
            insert_pos = start_pos + hepatic_match.end()
            content = content[:insert_pos] + "\n" + RENAL_ADJUSTMENT_TEMPLATE + content[insert_pos:]
            print(f"{drug_name}: Đã thêm renal_adjustment")
            end_pos += len(RENAL_ADJUSTMENT_TEMPLATE) + 1
            drug_section = content[start_pos:end_pos]
    
    # Bổ sung drug_interactions (thay thế nếu rỗng)
    if not has_drug_interactions:
        interactions_pattern = r'"drug_interactions":\s+\{[^}]+\},'
        interactions_match = re.search(interactions_pattern, drug_section, re.DOTALL)
        if interactions_match:
            old_interactions = interactions_match.group(0)
            if '"major": []' in old_interactions:
                insert_pos = start_pos + interactions_match.start()
                content = content[:insert_pos] + DRUG_INTERACTIONS_TEMPLATE.rstrip(',') + content[insert_pos + interactions_match.end():]
                print(f"{drug_name}: Đã cập nhật drug_interactions")
    
    # Bổ sung reversal_agents (thay thế nếu None)
    if not has_reversal_agents:
        reversal_pattern = r'"reversal_agents":\s+None,'
        reversal_match = re.search(reversal_pattern, drug_section)
        if reversal_match:
            insert_pos = start_pos + reversal_match.start()
            content = content[:insert_pos] + REVERSAL_AGENTS_TEMPLATE.rstrip(',') + content[insert_pos + reversal_match.end():]
            print(f"{drug_name}: Đã cập nhật reversal_agents")
    
    return content

def main():
    file_path = "drugs/drug_modules/diabetes/glp1_agonists.py"
    
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()
    
    # Danh sách các GLP-1 agonists
    drugs = ["Liraglutide", "Semaglutide", "Dulaglutide", "Exenatide"]
    
    # Bổ sung fields cho từng drug (theo thứ tự ngược)
    for drug_name in reversed(drugs):
        content = add_fields_to_drug(content, drug_name)
    
    # Lưu file
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(content)
    
    print("\n✅ Đã hoàn thành bổ sung fields cho tất cả GLP-1 agonists")

if __name__ == "__main__":
    main()
