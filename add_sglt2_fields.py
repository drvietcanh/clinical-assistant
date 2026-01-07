#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script để bổ sung các fields còn thiếu cho SGLT2 inhibitors
"""

import re

# Template cho renal_adjustment (SGLT2 inhibitors)
RENAL_ADJUSTMENT_TEMPLATE = '''        "renal_adjustment": {
            "normal": "Không cần chỉnh liều",
            "30_60": "Có thể dùng nhưng cần điều chỉnh liều. Empagliflozin: không dùng nếu eGFR <30. Dapagliflozin: không dùng nếu eGFR <25. Canagliflozin: giảm liều, không tăng lên 300mg nếu eGFR <60.",
            "under_30": "Empagliflozin: CHỐNG CHỈ ĐỊNH nếu eGFR <20. Dapagliflozin: CHỐNG CHỈ ĐỊNH nếu eGFR <25. Canagliflozin: CHỐNG CHỈ ĐỊNH nếu eGFR <30.",
            "dialysis": "CHỐNG CHỈ ĐỊNH. Không dùng khi đang lọc máu.",
            "notes": "SGLT2 inhibitors chống chỉ định ở suy thận nặng. Cần kiểm tra eGFR trước khi bắt đầu và định kỳ. Ngừng thuốc nếu eGFR giảm xuống dưới ngưỡng cho phép."
        },'''

# Template cho drug_interactions (SGLT2 inhibitors)
DRUG_INTERACTIONS_TEMPLATE = '''        "drug_interactions": {
            "major": [
                {
                    "drug": "Diuretics (Furosemide, Hydrochlorothiazide, etc.)",
                    "mechanism": "Cả hai đều tăng thải nước và natri",
                    "effect": "Tăng nguy cơ mất nước, hạ huyết áp, suy thận cấp",
                    "management": "Theo dõi huyết áp và thể tích dịch. Có thể cần giảm liều diuretic hoặc tạm ngừng SGLT2i."
                }
            ],
            "moderate": [
                {
                    "drug": "Insulin, Sulfonylureas",
                    "mechanism": "SGLT2i tăng thải glucose qua nước tiểu, có thể tăng nguy cơ hạ đường huyết",
                    "effect": "Tăng nguy cơ hạ đường huyết",
                    "management": "Giảm liều insulin hoặc sulfonylurea khi bắt đầu SGLT2i. Theo dõi đường huyết chặt chẽ."
                },
                {
                    "drug": "ACE inhibitors, ARBs",
                    "mechanism": "Cả hai đều có thể ảnh hưởng đến chức năng thận",
                    "effect": "Tăng nguy cơ suy thận cấp (hiếm)",
                    "management": "Theo dõi eGFR và creatinine khi bắt đầu hoặc thay đổi liều."
                }
            ],
            "minor": [
                {
                    "drug": "Digoxin",
                    "mechanism": "SGLT2i có thể ảnh hưởng nhẹ đến nồng độ digoxin",
                    "effect": "Tăng nhẹ nồng độ digoxin",
                    "management": "Theo dõi nồng độ digoxin nếu dùng cùng."
                }
            ]
        },'''

# Template cho reversal_agents (SGLT2 inhibitors)
REVERSAL_AGENTS_TEMPLATE = '''        "reversal_agents": {
            "available": False,
            "agents": [],
            "notes": "Không có antidote đặc hiệu. Điều trị quá liều chủ yếu là hỗ trợ: ngừng thuốc, bù dịch nếu mất nước, điều chỉnh đường huyết nếu hạ đường huyết, điều trị DKA nếu có."
        },'''

def add_fields_to_drug(content, drug_name, drug_specific_notes=""):
    """Thêm các fields còn thiếu cho một SGLT2 inhibitor"""
    
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
    has_renal_adjustment = '"renal_adjustment"' in drug_section
    has_drug_interactions = '"drug_interactions"' in drug_section and '"drug_interactions": {' in drug_section and '"major": [' in drug_section
    has_reversal_agents = '"reversal_agents"' in drug_section and '"reversal_agents": {' in drug_section
    
    if has_renal_adjustment and has_drug_interactions and has_reversal_agents:
        print(f"{drug_name}: Đã có đầy đủ fields")
        return content
    
    # Bổ sung renal_adjustment (sau hepatic_adjustment hoặc contraindications_detail)
    if not has_renal_adjustment:
        # Tìm vị trí sau hepatic_adjustment
        hepatic_pattern = r'"hepatic_adjustment":\s+\{[^}]+\},'
        hepatic_match = re.search(hepatic_pattern, drug_section, re.DOTALL)
        if hepatic_match:
            insert_pos = start_pos + hepatic_match.end()
            renal_field = RENAL_ADJUSTMENT_TEMPLATE
            if drug_specific_notes:
                # Thay thế notes nếu có
                renal_field = renal_field.replace('"notes": "SGLT2 inhibitors', f'"notes": "{drug_specific_notes}')
            content = content[:insert_pos] + "\n" + renal_field + content[insert_pos:]
            print(f"{drug_name}: Đã thêm renal_adjustment")
            # Cập nhật lại vị trí
            end_pos += len(renal_field) + 1
            drug_section = content[start_pos:end_pos]
        else:
            # Nếu không có hepatic_adjustment, tìm sau contraindications_detail
            contraindications_pattern = r'"contraindications_detail":\s+\{[^}]+\},'
            contraindications_match = re.search(contraindications_pattern, drug_section, re.DOTALL)
            if contraindications_match:
                insert_pos = start_pos + contraindications_match.end()
                content = content[:insert_pos] + "\n" + RENAL_ADJUSTMENT_TEMPLATE + content[insert_pos:]
                print(f"{drug_name}: Đã thêm renal_adjustment (sau contraindications_detail)")
    
    # Bổ sung drug_interactions (thay thế nếu rỗng)
    if not has_drug_interactions:
        # Tìm drug_interactions hiện tại
        interactions_pattern = r'"drug_interactions":\s+\{[^}]+\},'
        interactions_match = re.search(interactions_pattern, drug_section, re.DOTALL)
        if interactions_match:
            # Thay thế nếu rỗng
            old_interactions = interactions_match.group(0)
            if '"major": []' in old_interactions or '"major":[],' in old_interactions:
                insert_pos = start_pos + interactions_match.start()
                content = content[:insert_pos] + DRUG_INTERACTIONS_TEMPLATE.rstrip(',') + content[insert_pos + interactions_match.end():]
                print(f"{drug_name}: Đã cập nhật drug_interactions")
        else:
            # Thêm mới sau interactions (field cũ)
            interactions_old_pattern = r'"interactions":\s+\[[^\]]+\],'
            interactions_old_match = re.search(interactions_old_pattern, drug_section)
            if interactions_old_match:
                insert_pos = start_pos + interactions_old_match.end()
                content = content[:insert_pos] + "\n" + DRUG_INTERACTIONS_TEMPLATE + content[insert_pos:]
                print(f"{drug_name}: Đã thêm drug_interactions")
    
    # Bổ sung reversal_agents (thay thế nếu None)
    if not has_reversal_agents:
        # Tìm reversal_agents hiện tại
        reversal_pattern = r'"reversal_agents":\s+None,'
        reversal_match = re.search(reversal_pattern, drug_section)
        if reversal_match:
            # Thay thế None bằng dict
            insert_pos = start_pos + reversal_match.start()
            content = content[:insert_pos] + REVERSAL_AGENTS_TEMPLATE.rstrip(',') + content[insert_pos + reversal_match.end():]
            print(f"{drug_name}: Đã cập nhật reversal_agents")
        else:
            # Thêm mới sau overdose_management
            overdose_pattern = r'"overdose_management":\s+\{[^}]+\},'
            overdose_match = re.search(overdose_pattern, drug_section, re.DOTALL)
            if overdose_match:
                insert_pos = start_pos + overdose_match.end()
                content = content[:insert_pos] + "\n" + REVERSAL_AGENTS_TEMPLATE + content[insert_pos:]
                print(f"{drug_name}: Đã thêm reversal_agents")
    
    return content

def main():
    file_path = "drugs/drug_modules/diabetes/sglt2_inhibitors.py"
    
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()
    
    # Danh sách các SGLT2 inhibitors
    drugs = [
        ("Empagliflozin", "Empagliflozin: CHỐNG CHỈ ĐỊNH nếu eGFR <20. Không dùng khi lọc máu."),
        ("Dapagliflozin", "Dapagliflozin: CHỐNG CHỈ ĐỊNH nếu eGFR <25. Không dùng khi lọc máu."),
        ("Canagliflozin", "Canagliflozin: CHỐNG CHỈ ĐỊNH nếu eGFR <30. Không tăng liều lên 300mg nếu eGFR <60. Không dùng khi lọc máu.")
    ]
    
    # Bổ sung fields cho từng drug (theo thứ tự ngược)
    for drug_name, notes in reversed(drugs):
        content = add_fields_to_drug(content, drug_name, notes)
    
    # Lưu file
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(content)
    
    print("\n✅ Đã hoàn thành bổ sung fields cho tất cả SGLT2 inhibitors")

if __name__ == "__main__":
    main()
