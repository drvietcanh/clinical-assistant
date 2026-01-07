#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script để bổ sung các fields còn thiếu cho tất cả insulin trong specific_insulins.py
"""

import re

# Template cho contraindications_detail
def get_contraindications_detail_template(insulin_name):
    return f'''        "contraindications_detail": {{
            "tuyệt_đối": [
                "Hạ đường huyết đang diễn ra (hypoglycemia)",
                "Dị ứng với {insulin_name} hoặc bất kỳ thành phần nào",
                "Dị ứng với insulin nói chung"
            ],
            "tương_đối": [
                "Suy thận - cần giảm liều insulin do giảm thải trừ, tăng nguy cơ hạ đường huyết",
                "Suy gan - cần giảm liều insulin do giảm chuyển hóa glucose",
                "Bệnh nhân cao tuổi - tăng nguy cơ hạ đường huyết, cần theo dõi chặt chẽ",
                "Bệnh nhân có bệnh tim mạch - thận trọng với hạ đường huyết",
                "Phụ nữ có thai - cần điều chỉnh liều theo nhu cầu tăng lên trong thai kỳ"
            ]
        }},'''

# Template cho renal_adjustment
RENAL_ADJUSTMENT_TEMPLATE = '''          "renal_adjustment": {
              "normal": "Không cần chỉnh liều",
              "30_60": "Giảm liều 25-50%. Suy thận làm giảm thải trừ insulin, tăng nguy cơ hạ đường huyết.",
              "under_30": "Giảm liều 50% hoặc hơn. Theo dõi đường huyết chặt chẽ. Tăng nguy cơ hạ đường huyết.",
              "dialysis": "Giảm liều đáng kể. Insulin được lọc một phần qua thẩm phân máu. Theo dõi đường huyết chặt chẽ trước và sau lọc máu.",
              "notes": "Insulin thải trừ qua thận. Suy thận làm giảm thải trừ insulin, tăng thời gian bán thải, tăng nguy cơ hạ đường huyết. Cần giảm liều và theo dõi đường huyết chặt chẽ."
          },'''

def get_insulin_name_from_contraindications(contraindications_text):
    """Lấy tên insulin từ contraindications"""
    # Tìm pattern "Dị ứng insulin X"
    match = re.search(r'Dị ứng insulin (\w+)', contraindications_text)
    if match:
        return match.group(1)
    return None

def add_fields_to_insulin(content, insulin_name):
    """Thêm các fields còn thiếu cho một insulin"""
    
    # Tìm vị trí của insulin
    pattern = rf'    "{insulin_name}": \{{'
    match = re.search(pattern, content)
    if not match:
        print(f"Không tìm thấy {insulin_name}")
        return content
    
    start_pos = match.start()
    
    # Tìm vị trí kết thúc của insulin (dấu }, trước insulin tiếp theo hoặc kết thúc file)
    next_insulin_pattern = r'\n    "Insulin [^"]+": \{'
    next_match = re.search(next_insulin_pattern, content[start_pos + 100:])
    if next_match:
        end_pos = start_pos + 100 + next_match.start()
    else:
        end_pos = len(content)
    
    insulin_section = content[start_pos:end_pos]
    
    # Kiểm tra xem đã có các fields chưa
    has_contraindications_detail = '"contraindications_detail"' in insulin_section
    has_renal_adjustment = '"renal_adjustment"' in insulin_section
    
    if has_contraindications_detail and has_renal_adjustment:
        print(f"{insulin_name}: Đã có đầy đủ fields")
        return content
    
    # Tìm vị trí để chèn
    # Tìm "contraindications": [...] và chèn contraindications_detail sau đó
    if not has_contraindications_detail:
        contraindications_pattern = r'("contraindications": \[[^\]]+\],)'
        contraindications_match = re.search(contraindications_pattern, insulin_section, re.DOTALL)
        if contraindications_match:
            insert_pos = start_pos + contraindications_match.end()
            # Lấy tên insulin từ contraindications
            insulin_name_short = get_insulin_name_from_contraindications(contraindications_match.group(0))
            if not insulin_name_short:
                # Fallback: lấy từ tên insulin
                insulin_name_short = insulin_name.replace("Insulin ", "").lower()
            new_field = get_contraindications_detail_template(insulin_name_short)
            content = content[:insert_pos] + "\n" + new_field + content[insert_pos:]
            print(f"{insulin_name}: Đã thêm contraindications_detail")
            # Cập nhật lại vị trí
            end_pos += len(new_field) + 1
            insulin_section = content[start_pos:end_pos]
    
    # Tìm vị trí để chèn renal_adjustment (sau hepatic_adjustment)
    if not has_renal_adjustment:
        hepatic_pattern = r'"hepatic_adjustment": \{([^}]+)\},'
        hepatic_match = re.search(hepatic_pattern, insulin_section, re.DOTALL)
        if hepatic_match:
            insert_pos = start_pos + hepatic_match.end()
            content = content[:insert_pos] + "\n" + RENAL_ADJUSTMENT_TEMPLATE + content[insert_pos:]
            print(f"{insulin_name}: Đã thêm renal_adjustment")
        else:
            # Nếu không có hepatic_adjustment, tìm vị trí khác (sau pregnancy_lactation)
            pregnancy_pattern = r'"pregnancy_lactation": \{([^}]+)\},'
            pregnancy_match = re.search(pregnancy_pattern, insulin_section, re.DOTALL)
            if pregnancy_match:
                insert_pos = start_pos + pregnancy_match.end()
                content = content[:insert_pos] + "\n" + RENAL_ADJUSTMENT_TEMPLATE + content[insert_pos:]
                print(f"{insulin_name}: Đã thêm renal_adjustment (sau pregnancy_lactation)")
    
    return content

def main():
    file_path = "drugs/drug_modules/diabetes/specific_insulins.py"
    
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()
    
    # Danh sách các insulin cần bổ sung
    insulin_list = [
        "Insulin Aspart",
        "Insulin Degludec",
        "Insulin Detemir",
        "Insulin Glargine",
        "Insulin Glulisine",
        "Insulin Lispro",
        "Insulin NPH",
        "Insulin Regular"
    ]
    
    # Bổ sung fields cho từng insulin (theo thứ tự ngược để không ảnh hưởng đến vị trí)
    for insulin in reversed(insulin_list):
        content = add_fields_to_insulin(content, insulin)
    
    # Lưu file
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(content)
    
    print("\n✅ Đã hoàn thành bổ sung fields cho tất cả insulin")

if __name__ == "__main__":
    main()
