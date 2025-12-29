"""
Tự động bổ sung các field còn thiếu cho các thuốc
Có chế độ dry-run để xem trước, và chế độ thực thi để sửa file
"""
import ast
import re
from pathlib import Path
from collections import defaultdict
from typing import Dict, List, Set, Tuple, Optional
import shutil
from datetime import datetime

# Định nghĩa các field
CORE_FIELDS = [
    "group",
    "vietnamese_name", 
    "administration",
    "indications",
    "dosage"
]

EXTENDED_FIELDS = [
    "side_effects",
    "contraindications",
    "interactions",
    "pregnancy"
]

ENHANCED_FIELDS = [
    "mechanism_of_action",
    "monitoring",
    "precautions",
    "pharmacokinetics",
    "storage",
    "black_box_warnings",
    "drug_interactions",
    "pregnancy_lactation",
    "hepatic_adjustment",
    "overdose_management",
    "reversal_agents",
    "administration_instructions",
    "references"
]

# Templates cho các field
FIELD_TEMPLATES = {
    "group": "",  # Phải điền thủ công
    "vietnamese_name": "",  # Phải điền thủ công
    "administration": [],  # List rỗng
    "indications": [],  # List rỗng
    "dosage": {},  # Dict rỗng
    "side_effects": [],
    "contraindications": [],
    "interactions": [],
    "pregnancy": "",
    "mechanism_of_action": "",
    "monitoring": [],
    "precautions": [],
    "pharmacokinetics": {
        "half_life": "",
        "onset": "",
        "duration": "",
        "protein_binding": "",
        "clearance": ""
    },
    "storage": "",
    "black_box_warnings": None,
    "drug_interactions": {
        "major": [],
        "moderate": [],
        "minor": []
    },
    "pregnancy_lactation": {
        "fda_category": "",
        "pregnancy_details": "",
        "lactation_details": ""
    },
    "hepatic_adjustment": {
        "mild": "",
        "moderate": "",
        "severe": ""
    },
    "overdose_management": {
        "symptoms": [],
        "treatment": "",
        "antidote": None
    },
    "reversal_agents": {
        "available": False,
        "agents": [],
        "notes": ""
    },
    "administration_instructions": {
        "preparation": "",
        "administration": "",
        "monitoring": []
    },
    "references": {
        "primary": [],
        "guidelines": [],
        "other": []
    }
}

def get_string_value(node):
    """Lấy giá trị string từ AST node"""
    if isinstance(node, ast.Constant) and isinstance(node.value, str):
        return node.value
    elif hasattr(node, 's'):  # ast.Str (deprecated)
        return node.s
    return None

def extract_dict_keys(node: ast.Dict) -> Set[str]:
    """Trích xuất các keys từ AST Dict node"""
    keys = set()
    for key_node in node.keys:
        key = get_string_value(key_node)
        if key:
            keys.add(key)
    return keys

def find_drug_in_file(file_path: Path, drug_name: str) -> Optional[Tuple[int, int, Dict]]:
    """Tìm một thuốc trong file và trả về vị trí, fields hiện có"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
            lines = content.splitlines(keepends=True)
        
        tree = ast.parse(content)
        
        # Tìm drug trong AST
        for node in ast.walk(tree):
            if isinstance(node, ast.Assign):
                for target in node.targets:
                    if isinstance(target, ast.Name) and target.id.endswith('_DRUGS'):
                        if isinstance(node.value, ast.Dict):
                            for key_node, value_node in zip(node.value.keys, node.value.values):
                                found_name = get_string_value(key_node)
                                
                                if found_name == drug_name and isinstance(value_node, ast.Dict):
                                    # Tìm vị trí trong file
                                    for i, line in enumerate(lines):
                                        if f'"{drug_name}"' in line or f"'{drug_name}'" in line:
                                            # Tìm vị trí kết thúc của dict này
                                            start_line = i
                                            end_line = find_dict_end(lines, start_line)
                                            fields = extract_dict_keys(value_node)
                                            return (start_line, end_line, fields)
    except:
        pass
    
    return None

def find_dict_end(lines: List[str], start_line: int) -> int:
    """Tìm dòng kết thúc của dictionary bắt đầu từ start_line"""
    brace_count = 0
    in_string = False
    string_char = None
    
    for i in range(start_line, len(lines)):
        line = lines[i]
        for char in line:
            if char in ['"', "'"] and (i == 0 or (i > 0 and lines[i-1][-1] != '\\')):
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
                        return i
    
    return len(lines) - 1

def generate_field_code(field_name: str, template: any, indent: str = "        ") -> str:
    """Tạo code Python cho một field"""
    if template is None:
        return f'{indent}"{field_name}": None'
    elif isinstance(template, dict):
        lines = [f'{indent}"{field_name}": {{']
        for key, value in template.items():
            if isinstance(value, dict):
                lines.append(f'{indent}    "{key}": {{')
                for k, v in value.items():
                    if isinstance(v, list):
                        lines.append(f'{indent}        "{k}": [],')
                    elif isinstance(v, str):
                        lines.append(f'{indent}        "{k}": "",')
                    elif v is None:
                        lines.append(f'{indent}        "{k}": None,')
                    else:
                        lines.append(f'{indent}        "{k}": {repr(v)},')
                lines.append(f'{indent}    }},')
            elif isinstance(value, list):
                lines.append(f'{indent}    "{key}": [],')
            elif isinstance(value, str):
                lines.append(f'{indent}    "{key}": "",')
            elif value is None:
                lines.append(f'{indent}    "{key}": None,')
            else:
                lines.append(f'{indent}    "{key}": {repr(value)},')
        lines.append(f'{indent}}},')
        return '\n'.join(lines)
    elif isinstance(template, list):
        return f'{indent}"{field_name}": [],'
    elif isinstance(template, str):
        return f'{indent}"{field_name}": "",'
    else:
        return f'{indent}"{field_name}": {repr(template)},'

def add_missing_fields_to_file(
    file_path: Path, 
    drug_name: str, 
    missing_fields: List[str],
    dry_run: bool = True
) -> bool:
    """Thêm các field còn thiếu vào một thuốc trong file"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            lines = f.readlines()
        
        # Tìm vị trí của drug
        drug_info = find_drug_in_file(file_path, drug_name)
        if not drug_info:
            return False
        
        start_line, end_line, existing_fields = drug_info
        
        # Tìm vị trí chèn (trước dòng đóng dict)
        insert_line = end_line - 1
        
        # Tạo code cho các field mới
        new_fields_code = []
        for field in missing_fields:
            if field in FIELD_TEMPLATES:
                template = FIELD_TEMPLATES[field]
                field_code = generate_field_code(field, template)
                new_fields_code.append(field_code)
        
        if not new_fields_code:
            return False
        
        if dry_run:
            print(f"\n  [DRY-RUN] Se them vao {file_path.name}:")
            print(f"    Drug: {drug_name}")
            print(f"    Fields: {', '.join(missing_fields)}")
            return True
        
        # Thực sự thêm vào file
        # Tìm dòng cuối cùng của dict (trước })
        while insert_line >= start_line:
            line = lines[insert_line].strip()
            if line and not line.startswith('#'):
                # Đây là dòng cuối cùng có nội dung
                break
            insert_line -= 1
        
        # Thêm comma vào dòng cuối nếu chưa có
        if insert_line >= 0:
            last_line = lines[insert_line].rstrip()
            if not last_line.endswith(',') and not last_line.endswith('{'):
                lines[insert_line] = last_line + ',\n'
        
        # Chèn các field mới
        insert_pos = insert_line + 1
        new_code = '\n'.join(new_fields_code) + '\n'
        lines.insert(insert_pos, new_code)
        
        # Ghi lại file
        with open(file_path, 'w', encoding='utf-8') as f:
            f.writelines(lines)
        
        return True
        
    except Exception as e:
        print(f"  [LOI] Khong the them field vao {file_path.name}: {e}")
        return False

def find_drug_file(drug_name: str) -> Optional[Path]:
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
                # Kiểm tra xem có phải là drug thực sự không
                tree = ast.parse(content)
                for node in ast.walk(tree):
                    if isinstance(node, ast.Assign):
                        for target in node.targets:
                            if isinstance(target, ast.Name) and target.id.endswith('_DRUGS'):
                                if isinstance(node.value, ast.Dict):
                                    for key_node, value_node in zip(node.value.keys, node.value.values):
                                        found_name = get_string_value(key_node)
                                        if found_name == drug_name and isinstance(value_node, ast.Dict):
                                            value_keys = extract_dict_keys(value_node)
                                            # Chỉ trả về nếu có drug-like fields
                                            if 'group' in value_keys or 'vietnamese_name' in value_keys:
                                                return py_file
        except:
            pass
    
    return None

def main():
    """Main function"""
    print("\n" + "=" * 70)
    print("TU DONG BO SUNG FIELD CON THIEU CHO THUOC")
    print("=" * 70)
    print()
    
    print("Chon che do:")
    print("  1. Dry-run (xem truoc, khong sua file)")
    print("  2. Thuc thi (sua file thuc su)")
    print("  3. Chi bo sung core fields")
    print("  4. Chi bo sung extended fields")
    print("  5. Chi bo sung enhanced fields")
    print("  6. Bo sung tat ca")
    
    choice = input("\nNhap lua chon (1-6, mac dinh 1): ").strip() or "1"
    
    dry_run = choice == "1"
    add_core = choice in ["3", "6"]
    add_extended = choice in ["4", "6"]
    add_enhanced = choice in ["5", "6"]
    
    if choice == "2":
        add_core = add_extended = add_enhanced = True
    
    if not (add_core or add_extended or add_enhanced):
        print("Khong co field nao duoc chon. Thoat.")
        return
    
    print("\nDang tim cac thuoc thieu field...")
    
    # Load danh sách thuốc thiếu field (sử dụng logic từ check_missing_fields_final.py)
    # Để đơn giản, tôi sẽ tạo một hàm helper
    from check_missing_fields_final import load_all_drugs, check_drug_fields
    
    all_drugs = load_all_drugs()
    print(f"Tim thay {len(all_drugs)} thuoc")
    
    # Tìm các thuốc thiếu field
    drugs_to_fix = []
    
    for drug_name, fields in all_drugs.items():
        result = check_drug_fields(drug_name, fields)
        missing = []
        
        if add_core and result['missing_core']:
            missing.extend(result['missing_core'])
        if add_extended and result['missing_extended']:
            missing.extend(result['missing_extended'])
        if add_enhanced and result['missing_enhanced']:
            missing.extend(result['missing_enhanced'])
        
        if missing:
            drugs_to_fix.append((drug_name, missing))
    
    if not drugs_to_fix:
        print("\n[OK] Khong co thuoc nao thieu field can bo sung!")
        return
    
    print(f"\nTim thay {len(drugs_to_fix)} thuoc can bo sung field")
    
    if dry_run:
        print("\n[DRY-RUN MODE] Se hien thi cac thay doi se duoc thuc hien:")
    else:
        confirm = input(f"\nBan co chac muon sua {len(drugs_to_fix)} thuoc? (yes/no): ").strip().lower()
        if confirm != 'yes':
            print("Da huy.")
            return
        
        # Backup
        backup_dir = Path("backups") / datetime.now().strftime("%Y%m%d_%H%M%S")
        backup_dir.mkdir(parents=True, exist_ok=True)
        print(f"\nDang tao backup tai: {backup_dir}")
    
    # Xử lý từng thuốc
    fixed_count = 0
    failed_count = 0
    
    for drug_name, missing_fields in drugs_to_fix[:50]:  # Giới hạn 50 thuốc đầu tiên
        file_path = find_drug_file(drug_name)
        
        if not file_path:
            print(f"\n[WARNING] Khong tim thay file chua thuoc: {drug_name}")
            failed_count += 1
            continue
        
        if not dry_run:
            # Backup file
            backup_file = backup_dir / f"{file_path.name}.backup"
            shutil.copy2(file_path, backup_file)
        
        success = add_missing_fields_to_file(file_path, drug_name, missing_fields, dry_run)
        
        if success:
            fixed_count += 1
            if not dry_run:
                print(f"  [OK] Da them {len(missing_fields)} fields vao {drug_name} trong {file_path.name}")
        else:
            failed_count += 1
    
    # Tóm tắt
    print("\n" + "=" * 70)
    print("TOM TAT")
    print("=" * 70)
    print(f"\nDa xu ly: {fixed_count + failed_count} thuoc")
    print(f"  - Thanh cong: {fixed_count}")
    print(f"  - That bai: {failed_count}")
    
    if not dry_run and fixed_count > 0:
        print(f"\nBackup duoc luu tai: {backup_dir}")
        print("Ban co the restore neu can.")
    
    print("\n" + "=" * 70)

if __name__ == "__main__":
    main()
