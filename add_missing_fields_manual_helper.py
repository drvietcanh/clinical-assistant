"""
Script hỗ trợ bổ sung các fields còn thiếu với template rỗng
Chỉ thêm template, không điền thông tin - người dùng sẽ điền thủ công sau
"""
import re
import ast
from pathlib import Path
from typing import Dict, List, Set, Tuple

ENHANCED_FIELDS_TEMPLATES = {
    "mechanism_of_action": '        "mechanism_of_action": "",',
    "monitoring": '        "monitoring": [],',
    "precautions": '        "precautions": [],',
    "pharmacokinetics": '''        "pharmacokinetics": {
            "half_life": "",
            "onset": "",
            "duration": "",
            "protein_binding": "",
            "clearance": ""
        },''',
    "storage": '        "storage": "",',
    "black_box_warnings": '        "black_box_warnings": None,',
    "drug_interactions": '''        "drug_interactions": {
            "major": [],
            "moderate": [],
            "minor": []
        },''',
    "pregnancy_lactation": '''        "pregnancy_lactation": {
            "fda_category": "",
            "pregnancy_details": "",
            "lactation_details": ""
        },''',
    "hepatic_adjustment": '''        "hepatic_adjustment": {
            "mild": "",
            "moderate": "",
            "severe": ""
        },''',
    "overdose_management": '''        "overdose_management": {
            "symptoms": [],
            "treatment": "",
            "antidote": None
        },''',
    "reversal_agents": '''        "reversal_agents": {
            "available": False,
            "agents": [],
            "notes": ""
        },''',
    "administration_instructions": '''        "administration_instructions": {
            "preparation": "",
            "administration": "",
            "monitoring": []
        },''',
    "references": '''        "references": {
            "primary": [],
            "guidelines": [],
            "other": []
        },''',
}

EXTENDED_FIELDS_TEMPLATES = {
    "side_effects": '        "side_effects": [],',
    "contraindications": '        "contraindications": [],',
    "interactions": '        "interactions": [],',
    "pregnancy": '        "pregnancy": "",',
}

def get_string_value(node):
    if isinstance(node, ast.Constant) and isinstance(node.value, str):
        return node.value
    elif hasattr(node, 's'):
        return node.s
    return None

def extract_dict_keys(node: ast.Dict) -> Set[str]:
    keys = set()
    for key_node in node.keys:
        key = get_string_value(key_node)
        if key:
            keys.add(key)
    return keys

def find_drug_section(content: str, drug_name: str) -> Tuple[int, int]:
    """Tìm vị trí của một thuốc trong content"""
    pattern = rf'["\']{re.escape(drug_name)}["\']\s*:\s*\{{'
    match = re.search(pattern, content)
    
    if not match:
        return None, None
    
    start_pos = match.end() - 1
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
                    return start_pos, i + 1
        
        i += 1
    
    return None, None

def check_field_exists(content: str, drug_start: int, drug_end: int, field_name: str) -> bool:
    """Kiểm tra xem field đã tồn tại chưa"""
    drug_section = content[drug_start:drug_end]
    pattern = rf'["\']{re.escape(field_name)}["\']\s*:'
    return bool(re.search(pattern, drug_section))

def add_fields_to_drug_manual(
    file_path: Path,
    drug_name: str,
    missing_fields: List[str],
    field_templates: Dict[str, str]
) -> bool:
    """Thêm các field còn thiếu vào một thuốc"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
            lines = content.splitlines(keepends=True)
        
        start_pos, end_pos = find_drug_section(content, drug_name)
        if start_pos is None:
            print(f"  [LOI] Khong tim thay thuoc {drug_name} trong {file_path.name}")
            return False
        
        start_line = content[:start_pos].count('\n')
        end_line = content[:end_pos].count('\n')
        
        fields_to_add = []
        for field in missing_fields:
            if not check_field_exists(content, start_pos, end_pos, field):
                if field in field_templates:
                    fields_to_add.append((field, field_templates[field]))
        
        if not fields_to_add:
            print(f"  [SKIP] {drug_name}: Tat ca field da co san")
            return False
        
        print(f"  [INFO] {drug_name}: Se them {len(fields_to_add)} fields")
        
        # Tìm vị trí chèn (trước dòng đóng })
        insert_line = end_line - 1
        
        # Tìm dòng cuối cùng có nội dung
        while insert_line > start_line:
            line = lines[insert_line].strip()
            if line and line != '}' and not line.startswith('#'):
                if not line.endswith(',') and not line.endswith('{'):
                    lines[insert_line] = lines[insert_line].rstrip() + ',\n'
                break
            insert_line -= 1
        
        # Tạo code cho các field mới
        new_fields = []
        for field, template in fields_to_add:
            new_fields.append(template)
        
        if not new_fields:
            return False
        
        # Chèn vào
        insert_pos = insert_line + 1
        new_code = '\n'.join(new_fields) + '\n'
        lines.insert(insert_pos, new_code)
        
        # Ghi lại
        with open(file_path, 'w', encoding='utf-8') as f:
            f.writelines(lines)
        
        print(f"  [OK] Da them {len(fields_to_add)} fields vao {drug_name}")
        return True
        
    except Exception as e:
        print(f"  [LOI] {file_path.name} - {drug_name}: {e}")
        return False

def main():
    """Main function - chỉ xử lý các file chính, không phải backup"""
    print("\n" + "=" * 70)
    print("BO SUNG FIELDS CON THIEU (MANUAL HELPER)")
    print("=" * 70)
    print()
    
    # Danh sách các thuốc cần bổ sung (từ báo cáo)
    drugs_to_fix = [
        # ACE/ARB
        ("Lisinopril", "drugs/drug_modules/cardiovascular/ace_arb.py",
         ["pregnancy", "pregnancy_lactation", "hepatic_adjustment", "overdose_management",
          "administration_instructions", "pharmacokinetics", "storage", "references"]),
        ("Enalapril", "drugs/drug_modules/cardiovascular/ace_arb.py",
         ["pregnancy", "pregnancy_lactation", "hepatic_adjustment", "overdose_management",
          "administration_instructions", "pharmacokinetics", "storage", "references",
          "precautions", "black_box_warnings", "monitoring"]),
        ("Losartan", "drugs/drug_modules/cardiovascular/ace_arb.py",
         ["pregnancy", "pregnancy_lactation", "hepatic_adjustment", "overdose_management",
          "administration_instructions", "pharmacokinetics", "storage", "references"]),
        ("Valsartan", "drugs/drug_modules/cardiovascular/ace_arb.py",
         ["pregnancy", "pregnancy_lactation", "hepatic_adjustment", "overdose_management",
          "administration_instructions", "pharmacokinetics", "storage", "references",
          "precautions", "black_box_warnings", "monitoring", "mechanism_of_action"]),
        ("Telmisartan", "drugs/drug_modules/cardiovascular/ace_arb.py",
         ["pregnancy", "pregnancy_lactation", "hepatic_adjustment", "overdose_management",
          "administration_instructions", "pharmacokinetics", "storage", "references",
          "precautions", "black_box_warnings", "monitoring"]),
        # Oncology
        ("Cisplatin", "drugs/drug_modules/oncology/chemotherapy.py",
         ["pregnancy", "pregnancy_lactation", "hepatic_adjustment", "overdose_management",
          "administration_instructions", "pharmacokinetics", "storage", "references",
          "drug_interactions", "reversal_agents"]),
        ("Carboplatin", "drugs/drug_modules/oncology/chemotherapy.py",
         ["pregnancy", "pregnancy_lactation", "hepatic_adjustment", "overdose_management",
          "administration_instructions", "pharmacokinetics", "storage", "references",
          "drug_interactions", "reversal_agents"]),
    ]
    
    all_templates = {**ENHANCED_FIELDS_TEMPLATES, **EXTENDED_FIELDS_TEMPLATES}
    
    fixed_count = 0
    for drug_name, file_path_str, missing_fields in drugs_to_fix:
        file_path = Path(file_path_str)
        if not file_path.exists():
            print(f"  [LOI] File khong ton tai: {file_path}")
            continue
        
        print(f"\n[DANG XU LY] {drug_name} trong {file_path.name}")
        success = add_fields_to_drug_manual(file_path, drug_name, missing_fields, all_templates)
        if success:
            fixed_count += 1
    
    print("\n" + "=" * 70)
    print("TOM TAT")
    print("=" * 70)
    print(f"\nDa xu ly: {fixed_count}/{len(drugs_to_fix)} thuoc")
    print("\nLuu y: Cac fields da duoc them voi template trong.")
    print("Ban can dien thong tin chi tiet vao cac template nay.")

if __name__ == "__main__":
    main()
