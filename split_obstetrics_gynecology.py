"""
Script tách obstetrics_gynecology.py thành subfolder
"""
import ast
import re
import shutil
from pathlib import Path
from typing import Dict, List, Tuple

def get_string_value(node):
    """Lấy giá trị string từ AST node"""
    if isinstance(node, ast.Constant) and isinstance(node.value, str):
        return node.value
    elif hasattr(node, 's'):
        return node.s
    return None

def extract_drug_entries_from_file(file_path: Path) -> List[Tuple[str, str, str]]:
    """Trích xuất các drug entries từ file"""
    drugs = []
    
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    try:
        tree = ast.parse(content)
    except SyntaxError as e:
        print(f"Syntax error in {file_path}: {e}")
        return []
    
    # Tìm OBSTETRICS_GYNECOLOGY_DRUGS assignment
    for node in ast.walk(tree):
        if isinstance(node, ast.Assign):
            for target in node.targets:
                if isinstance(target, ast.Name) and target.id == 'OBSTETRICS_GYNECOLOGY_DRUGS':
                    if isinstance(node.value, ast.Dict):
                        # Tìm vị trí của dict trong source
                        dict_start = node.value.lineno - 1
                        
                        # Parse từng drug entry
                        for key_node, value_node in zip(node.value.keys, node.value.values):
                            drug_name = get_string_value(key_node)
                            
                            if drug_name:
                                # Lấy group từ value_node
                                group = "other_obgyn"
                                if isinstance(value_node, ast.Dict):
                                    for k, v in zip(value_node.keys, value_node.values):
                                        if get_string_value(k) == 'group':
                                            group_str = get_string_value(v)
                                            if group_str:
                                                group_lower = group_str.lower()
                                                if "contraceptive" in group_lower:
                                                    group = "contraceptives"
                                                elif "hormone" in group_lower or "estrogen" in group_lower or "progesterone" in group_lower or "hrt" in group_lower:
                                                    group = "hormone_replacement"
                                                elif "fertility" in group_lower or "ovulation" in group_lower:
                                                    group = "fertility_drugs"
                                                elif "antifungal" in group_lower or "candidiasis" in group_lower or "vaginal" in group_lower:
                                                    group = "vaginal_medications"
                                                elif "uterotonic" in group_lower or "oxytocin" in group_lower:
                                                    group = "other_obgyn"  # Uterotonics should be in emergency
                                
                                # Lấy source code của drug entry
                                try:
                                    # Tìm vị trí trong source code
                                    lines = content.split('\n')
                                    # Tìm dòng bắt đầu của drug entry
                                    drug_start_line = key_node.lineno - 1
                                    
                                    # Tìm dòng kết thúc (dòng có }, sau drug entry)
                                    # Đơn giản: tìm từ drug_start_line đến khi gặp }, với indent phù hợp
                                    indent_level = len(lines[drug_start_line]) - len(lines[drug_start_line].lstrip())
                                    drug_end_line = drug_start_line
                                    
                                    brace_count = 0
                                    started = False
                                    for i in range(drug_start_line, len(lines)):
                                        line = lines[i]
                                        current_indent = len(line) - len(line.lstrip())
                                        
                                        if '{' in line:
                                            brace_count += line.count('{')
                                            started = True
                                        if '}' in line:
                                            brace_count -= line.count('}')
                                        
                                        if started and brace_count == 0 and current_indent <= indent_level:
                                            drug_end_line = i
                                            break
                                    
                                    # Extract drug code
                                    drug_lines = lines[drug_start_line:drug_end_line+1]
                                    drug_code = '\n'.join(drug_lines)
                                    
                                    # Remove trailing comma if exists
                                    drug_code = drug_code.rstrip()
                                    if drug_code.endswith(','):
                                        drug_code = drug_code[:-1]
                                    
                                    drugs.append((drug_name, group, drug_code))
                                except Exception as e:
                                    print(f"Error extracting {drug_name}: {e}")
                                    continue
    except Exception as e:
        print(f"Error parsing {file_path}: {e}")
        return []
    
    return drugs

def split_obstetrics_gynecology():
    """Tách obstetrics_gynecology.py thành subfolder"""
    source_file = Path("drugs/drug_modules/obstetrics_gynecology.py")
    target_dir = Path("drugs/drug_modules/obstetrics_gynecology")
    
    if not source_file.exists():
        print(f"File not found: {source_file}")
        return False
    
    # Tạo thư mục nếu chưa có
    target_dir.mkdir(exist_ok=True)
    
    # Trích xuất drug entries
    print("Dang trich xuat drug entries...")
    drugs = extract_drug_entries_from_file(source_file)
    
    if not drugs:
        print("Khong tim thay drug entries!")
        return False
    
    print(f"Tim thay {len(drugs)} thuoc")
    
    # Phân loại theo group
    categories = {
        'contraceptives': [],
        'hormone_replacement': [],
        'fertility_drugs': [],
        'vaginal_medications': [],
        'other_obgyn': [],
    }
    
    for drug_name, group, code in drugs:
        if group in categories:
            categories[group].append((drug_name, code))
        else:
            categories['other_obgyn'].append((drug_name, code))
    
    # In thống kê
    for cat, items in categories.items():
        if items:
            print(f"  {cat}: {len(items)} thuoc")
    
    # File mappings
    file_mappings = {
        'contraceptives': ('contraceptives.py', 'CONTRACEPTIVES_DRUGS'),
        'hormone_replacement': ('hormone_replacement.py', 'HORMONE_REPLACEMENT_DRUGS'),
        'fertility_drugs': ('fertility_drugs.py', 'FERTILITY_DRUGS'),
        'vaginal_medications': ('vaginal_medications.py', 'VAGINAL_MEDICATIONS_DRUGS'),
        'other_obgyn': ('other_obgyn.py', 'OTHER_OBGYN_DRUGS'),
    }
    
    # Header
    header = '''"""
Obstetrics and Gynecology Medications
Includes contraception and hormone therapy drugs
Note: Uterotonics are in emergency/uterotonics.py
"""
from typing import Dict, Any

'''
    
    # Tạo file cho từng category
    created_vars = {}
    for category, (filename, var_name) in file_mappings.items():
        if not categories[category]:
            continue
        
        filepath = target_dir / filename
        
        content = header
        content += f"{var_name}: Dict[str, Dict[str, Any]] = {{\n"
        
        for drug_name, drug_code in categories[category]:
            # Indent drug code
            indented_code = '\n'.join('    ' + line if line.strip() else line 
                                    for line in drug_code.split('\n'))
            content += f"{indented_code},\n\n"
        
        content += "}\n\n"
        content += f"__all__ = ['{var_name}']\n"
        
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        
        created_vars[category] = var_name
        print(f"Da tao: {filepath} ({len(categories[category])} thuoc)")
    
    # Tạo __init__.py
    init_content = '''"""
Obstetrics and Gynecology Drugs
Combines all OB/GYN drugs from category-specific files
"""
from typing import Dict, Any

'''
    
    for category, (filename, var_name) in file_mappings.items():
        if category in created_vars:
            module_name = filename[:-3]
            init_content += f"from .{module_name} import {var_name}\n"
    
    init_content += "\n# Combine all OB/GYN drugs\n"
    init_content += "OBSTETRICS_GYNECOLOGY_DRUGS: Dict[str, Dict[str, Any]] = {\n"
    
    for var_name in created_vars.values():
        init_content += f"    **{var_name},\n"
    
    init_content += "}\n\n"
    init_content += "__all__ = ['OBSTETRICS_GYNECOLOGY_DRUGS']\n"
    
    init_file = target_dir / "__init__.py"
    with open(init_file, 'w', encoding='utf-8') as f:
        f.write(init_content)
    
    print(f"Da tao: {init_file}")
    
    # Backup và tạo wrapper
    backup_file = source_file.with_suffix('.py.backup')
    shutil.copy2(source_file, backup_file)
    print(f"Da backup: {backup_file}")
    
    wrapper_content = '''"""
Obstetrics and Gynecology Medications
Backward compatibility: imports from obstetrics_gynecology module
"""

from .obstetrics_gynecology import OBSTETRICS_GYNECOLOGY_DRUGS

__all__ = ['OBSTETRICS_GYNECOLOGY_DRUGS']
'''
    
    with open(source_file, 'w', encoding='utf-8') as f:
        f.write(wrapper_content)
    
    print(f"Da cap nhat: {source_file} (wrapper)")
    return True

def main():
    """Hàm chính"""
    import sys
    import io
    if sys.platform == 'win32':
        sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')
    
    print("Bat dau tach file obstetrics_gynecology.py...")
    if split_obstetrics_gynecology():
        print("Hoan thanh!")
    else:
        print("Co loi xay ra!")

if __name__ == "__main__":
    main()

