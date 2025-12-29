"""
Script debug để tìm file chứa một số thuốc cụ thể
"""
import re
from pathlib import Path
import sys
sys.path.insert(0, str(Path.cwd()))

from check_missing_fields_final import load_all_drugs, check_drug_fields

def find_drug_file(drug_name: str) -> Path:
    """Tìm file chứa một thuốc"""
    base_path = Path("drugs/drug_modules")
    
    for py_file in sorted(base_path.rglob("*.py")):
        if py_file.name == "__init__.py" or py_file.name.endswith(".backup"):
            continue
        
        try:
            with open(py_file, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Kiểm tra xem drug có trong file không
            pattern = rf'["\']{re.escape(drug_name)}["\']\s*:\s*\{{'
            if re.search(pattern, content):
                # Kiểm tra xem có phải là drug thực sự (có 'group' hoặc 'vietnamese_name')
                # Tìm vị trí của drug
                match = re.search(pattern, content)
                if match:
                    start_pos = match.end() - 1
                    # Tìm vị trí kết thúc của dict
                    brace_count = 0
                    in_string = False
                    string_char = None
                    i = start_pos
                    
                    while i < len(content):
                        char = content[i]
                        
                        if char in ['"', "'"]:
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
                                    drug_section = content[start_pos:i+1]
                                    if '"group"' in drug_section or '"vietnamese_name"' in drug_section:
                                        return py_file
                                    break
                        i += 1
        except Exception as e:
            pass
    
    return None

# Load tat ca thuoc
all_drugs = load_all_drugs()
print(f"Tong so thuoc: {len(all_drugs)}")

# Tim cac thuoc thieu enhanced fields
drugs_to_fix = []

for drug_name, fields in all_drugs.items():
    # Loc bo cac field names
    is_field_name = (
        drug_name.islower() and 
        '_' in drug_name and 
        drug_name.count('_') >= 2 and
        drug_name not in ['iv', 'po', 'im', 'sc']
    )
    
    if is_field_name or 'group' not in fields and 'vietnamese_name' not in fields:
        continue
    
    result = check_drug_fields(drug_name, fields)
    if result['missing_enhanced']:
        drugs_to_fix.append((drug_name, result['missing_enhanced']))

print(f"\nTim thay {len(drugs_to_fix)} thuoc thieu enhanced fields")

# Kiem tra 10 thuoc dau tien
print("\nKiem tra 10 thuoc dau tien:")
for i, (drug_name, missing_fields) in enumerate(drugs_to_fix[:10], 1):
    file_path = find_drug_file(drug_name)
    if file_path:
        print(f"{i}. {drug_name}: Tim thay trong {file_path.name}")
    else:
        print(f"{i}. {drug_name}: KHONG TIM THAY FILE")
        # Thu tim bang cach khac
        base_path = Path("drugs/drug_modules")
        found_any = False
        for py_file in sorted(base_path.rglob("*.py")):
            if py_file.name == "__init__.py":
                continue
            try:
                with open(py_file, 'r', encoding='utf-8') as f:
                    content = f.read()
                if drug_name in content:
                    print(f"   (Nhung tim thay '{drug_name}' trong {py_file.name})")
                    found_any = True
            except:
                pass
        if not found_any:
            print(f"   (Khong tim thay '{drug_name}' trong bat ky file nao)")

