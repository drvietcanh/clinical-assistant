"""
Test chi tiết việc thêm field cho một thuốc cụ thể
"""
import re
from pathlib import Path

ENHANCED_FIELDS_TEMPLATES = {
    "references": '''        "references": {
            "primary": [],
            "guidelines": [],
            "other": []
        },''',
}

def find_drug_section(content: str, drug_name: str):
    """Tìm vị trí của một thuốc trong content"""
    # Pattern: "DrugName": { ... }
    pattern = rf'["\']{re.escape(drug_name)}["\']\s*:\s*\{{'
    match = re.search(pattern, content)
    
    if not match:
        return None, None
    
    start_pos = match.end() - 1  # Vị trí của {
    
    # Tìm vị trí kết thúc của dict
    brace_count = 0
    in_string = False
    string_char = None
    i = start_pos
    
    while i < len(content):
        char = content[i]
        
        # Xử lý string
        if char in ['"', "'"]:
            # Kiểm tra escape
            if i > 0 and content[i-1] == '\\':
                i += 1
                continue
            
            if not in_string:
                in_string = True
                string_char = char
            elif char == string_char:
                in_string = False
                string_char = None
        
        if not in_string:
            if char == '{':
                brace_count += 1
            elif char == '}':
                brace_count -= 1
                if brace_count == 0:
                    return start_pos, i + 1
        
        i += 1
    
    return None, None

def check_field_exists(content: str, drug_start: int, drug_end: int, field_name: str) -> bool:
    """Kiểm tra xem field đã tồn tại chưa"""
    drug_section = content[drug_start:drug_end]
    pattern = rf'["\']{re.escape(field_name)}["\']\s*:'
    return bool(re.search(pattern, drug_section))

# Test với Losartan/Hydrochlorothiazide
drug_name = "Losartan/Hydrochlorothiazide"
file_path = Path("drugs/drug_modules/cardiovascular/fixed_dose_combinations.py")

print("=" * 70)
print(f"TEST CHI TIET: {drug_name}")
print("=" * 70)
print()

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Tìm drug section
start_pos, end_pos = find_drug_section(content, drug_name)

if start_pos is None:
    print("[LOI] Khong tim thay drug section")
else:
    print(f"[OK] Tim thay drug section:")
    print(f"  Start position: {start_pos}")
    print(f"  End position: {end_pos}")
    print(f"  Length: {end_pos - start_pos}")
    
    drug_section = content[start_pos:end_pos]
    print(f"\nDrug section length: {len(drug_section)} characters")
    # Không in nội dung để tránh lỗi encoding
    
    # Kiểm tra field "references"
    has_references = check_field_exists(content, start_pos, end_pos, "references")
    print(f"\nField 'references' da ton tai: {has_references}")
    
    # Kiểm tra các field khác
    all_fields = ["group", "vietnamese_name", "administration", "indications", "dosage", "references"]
    print("\nCac field hien co:")
    for field in all_fields:
        exists = check_field_exists(content, start_pos, end_pos, field)
        print(f"  - {field}: {'Co' if exists else 'Khong'}")

