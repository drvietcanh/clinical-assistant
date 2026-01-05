"""
Script tách obstetrics_gynecology.py thành subfolder - Phiên bản đơn giản
Sử dụng AST để tách drug entries
"""
import ast
import re
import shutil
from pathlib import Path
from collections import defaultdict
from typing import List, Tuple

def get_string_value(node):
    """Lấy giá trị string từ AST node"""
    if isinstance(node, ast.Constant) and isinstance(node.value, str):
        return node.value
    elif hasattr(node, 's'):
        return node.s
    return None

def extract_drug_entries(content: str) -> List[Tuple[str, str, str]]:
    """Trích xuất drug entries từ content"""
    drugs = []
    
    # Pattern để tìm drug entries: "Drug Name": { ... },
    # Tìm tất cả các entry trong OBSTETRICS_GYNECOLOGY_DRUGS = { ... }
    
    # Tìm phần dictionary
    dict_match = re.search(r'OBSTETRICS_GYNECOLOGY_DRUGS\s*=\s*\{', content)
    if not dict_match:
        return []
    
    dict_start = dict_match.end()
    
    # Tìm drug entries bằng cách tìm pattern: "Drug Name": {
    pattern = r'^\s+"([^"]+)":\s*\{'
    
    lines = content.split('\n')
    in_dict = False
    brace_count = 0
    current_drug = None
    current_drug_start = None
    current_drug_lines = []
    base_indent = 0
    
    for i, line in enumerate(lines):
        # Bắt đầu từ dict_start
        if i < dict_start // 100:  # Approximate
            continue
        
        # Tìm drug entry mới
        match = re.match(pattern, line)
        if match:
            # Lưu drug cũ nếu có
            if current_drug:
                drug_code = '\n'.join(current_drug_lines)
                # Tìm group trong drug_code
                group_match = re.search(r'"group":\s*"([^"]+)"', drug_code)
                group = group_match.group(1) if group_match else "other_obgyn"
                
                # Phân loại
                category = "other_obgyn"
                group_lower = group.lower()
                if "contraceptive" in group_lower:
                    category = "contraceptives"
                elif "hormone" in group_lower or "estrogen" in group_lower or "progesterone" in group_lower or "hrt" in group_lower:
                    category = "hormone_replacement"
                elif "fertility" in group_lower or "ovulation" in group_lower:
                    category = "fertility_drugs"
                elif "antifungal" in group_lower or "candidiasis" in group_lower or "vaginal" in group_lower:
                    category = "vaginal_medications"
                
                drugs.append((current_drug, category, drug_code))
            
            # Bắt đầu drug mới
            current_drug = match.group(1)
            current_drug_start = i
            base_indent = len(line) - len(line.lstrip())
            current_drug_lines = [line]
            brace_count = line.count('{') - line.count('}')
            continue
        
        # Nếu đang trong drug entry
        if current_drug:
            current_drug_lines.append(line)
            brace_count += line.count('{') - line.count('}')
            
            # Kết thúc drug entry khi brace_count = 0 và indent về mức base
            current_indent = len(line) - len(line.lstrip()) if line.strip() else base_indent
            if brace_count == 0 and current_indent <= base_indent and '}' in line:
                # Kết thúc drug entry
                drug_code = '\n'.join(current_drug_lines)
                # Tìm group
                group_match = re.search(r'"group":\s*"([^"]+)"', drug_code)
                group = group_match.group(1) if group_match else "other_obgyn"
                
                category = "other_obgyn"
                group_lower = group.lower()
                if "contraceptive" in group_lower:
                    category = "contraceptives"
                elif "hormone" in group_lower or "estrogen" in group_lower or "progesterone" in group_lower or "hrt" in group_lower:
                    category = "hormone_replacement"
                elif "fertility" in group_lower or "ovulation" in group_lower:
                    category = "fertility_drugs"
                elif "antifungal" in group_lower or "candidiasis" in group_lower or "vaginal" in group_lower:
                    category = "vaginal_medications"
                
                drugs.append((current_drug, category, drug_code))
                current_drug = None
                current_drug_lines = []
    
    return drugs

def split_obstetrics_gynecology():
    """Tách obstetrics_gynecology.py"""
    source_file = Path("drugs/drug_modules/obstetrics_gynecology.py")
    target_dir = Path("drugs/drug_modules/obstetrics_gynecology")
    
    if not source_file.exists():
        print(f"File not found: {source_file}")
        return False
    
    # Đọc file
    with open(source_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Trích xuất drugs
    print("Dang trich xuat drug entries...")
    drugs = extract_drug_entries(content)
    
    if not drugs:
        print("Khong tim thay drug entries bang regex!")
        print("Thu cach khac: parse AST...")
        # Thử cách khác: parse AST và extract
        try:
            import ast
            tree = ast.parse(content)
            
            # Tìm OBSTETRICS_GYNECOLOGY_DRUGS
            for node in ast.walk(tree):
                if isinstance(node, ast.Assign):
                    for target in node.targets:
                        if isinstance(target, ast.Name) and target.id == 'OBSTETRICS_GYNECOLOGY_DRUGS':
                            if isinstance(node.value, ast.Dict):
                                categories = defaultdict(list)
                                
                                for key_node, value_node in zip(node.value.keys, node.value.values):
                                    drug_name = get_string_value(key_node)
                                    if not drug_name:
                                        continue
                                    
                                    # Lấy group
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
                                    
                                    # Lấy source code của drug entry
                                    try:
                                        # Tìm vị trí trong source
                                        lines = content.split('\n')
                                        drug_start = key_node.lineno - 1
                                        
                                        # Tìm kết thúc
                                        indent = len(lines[drug_start]) - len(lines[drug_start].lstrip())
                                        brace_count = 0
                                        drug_end = drug_start
                                        
                                        for i in range(drug_start, len(lines)):
                                            line = lines[i]
                                            brace_count += line.count('{') - line.count('}')
                                            if brace_count == 0 and i > drug_start:
                                                current_indent = len(line) - len(line.lstrip()) if line.strip() else indent
                                                if current_indent <= indent:
                                                    drug_end = i
                                                    break
                                        
                                        drug_code = '\n'.join(lines[drug_start:drug_end+1])
                                        # Remove trailing comma
                                        drug_code = drug_code.rstrip().rstrip(',')
                                        
                                        categories[group].append((drug_name, drug_code))
                                    except Exception as e:
                                        print(f"Error extracting {drug_name}: {e}")
                                        continue
                                
                                # Tạo thư mục
                                target_dir.mkdir(exist_ok=True)
                                
                                # File mappings
                                file_mappings = {
                                    'contraceptives': ('contraceptives.py', 'CONTRACEPTIVES_DRUGS'),
                                    'hormone_replacement': ('hormone_replacement.py', 'HORMONE_REPLACEMENT_DRUGS'),
                                    'fertility_drugs': ('fertility_drugs.py', 'FERTILITY_DRUGS'),
                                    'vaginal_medications': ('vaginal_medications.py', 'VAGINAL_MEDICATIONS_DRUGS'),
                                    'other_obgyn': ('other_obgyn.py', 'OTHER_OBGYN_DRUGS'),
                                }
                                
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
                                    
                                    file_content = header
                                    file_content += f"{var_name}: Dict[str, Dict[str, Any]] = {{\n"
                                    
                                    for drug_name, drug_code in categories[category]:
                                        # Indent drug code
                                        indented = '\n'.join('    ' + line if line.strip() else line 
                                                           for line in drug_code.split('\n'))
                                        file_content += f"{indented},\n\n"
                                    
                                    file_content += "}\n\n"
                                    file_content += f"__all__ = ['{var_name}']\n"
                                    
                                    with open(filepath, 'w', encoding='utf-8') as f:
                                        f.write(file_content)
                                    
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
                                
                                # Backup và wrapper
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
            
            # Phân loại
            categories = defaultdict(list)
            for drug_name, drug_data in OBSTETRICS_GYNECOLOGY_DRUGS.items():
                group = drug_data.get('group', '')
                group_lower = group.lower()
                
                if "contraceptive" in group_lower:
                    category = "contraceptives"
                elif "hormone" in group_lower or "estrogen" in group_lower or "progesterone" in group_lower or "hrt" in group_lower:
                    category = "hormone_replacement"
                elif "fertility" in group_lower or "ovulation" in group_lower:
                    category = "fertility_drugs"
                elif "antifungal" in group_lower or "candidiasis" in group_lower or "vaginal" in group_lower:
                    category = "vaginal_medications"
                else:
                    category = "other_obgyn"
                
                categories[category].append((drug_name, drug_data))
            
            # Tạo thư mục
            target_dir.mkdir(exist_ok=True)
            
            # File mappings
            file_mappings = {
                'contraceptives': ('contraceptives.py', 'CONTRACEPTIVES_DRUGS'),
                'hormone_replacement': ('hormone_replacement.py', 'HORMONE_REPLACEMENT_DRUGS'),
                'fertility_drugs': ('fertility_drugs.py', 'FERTILITY_DRUGS'),
                'vaginal_medications': ('vaginal_medications.py', 'VAGINAL_MEDICATIONS_DRUGS'),
                'other_obgyn': ('other_obgyn.py', 'OTHER_OBGYN_DRUGS'),
            }
            
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
                
                file_content = header
                file_content += f"{var_name}: Dict[str, Dict[str, Any]] = {{\n"
                
                for drug_name, drug_data in categories[category]:
                    # Convert dict to string representation
                    import json
                    drug_str = json.dumps({drug_name: drug_data}, indent=4, ensure_ascii=False)
                    # Remove outer braces and drug name key, keep only the value dict
                    drug_str = drug_str.split(':', 1)[1].strip()
                    drug_str = drug_str.rstrip('}').strip()
                    # Indent
                    indented = '\n'.join('    ' + line if line.strip() else line 
                                       for line in drug_str.split('\n'))
                    file_content += f'    "{drug_name}": {{\n{indented}\n    }},\n\n'
                
                file_content += "}\n\n"
                file_content += f"__all__ = ['{var_name}']\n"
                
                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(file_content)
                
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
            
            # Backup và wrapper
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
            
        except Exception as e:
            print(f"Error: {e}")
            import traceback
            traceback.print_exc()
            return False
    
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

