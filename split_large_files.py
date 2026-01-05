"""
Script để tách các file lớn thành subfolder
Bắt đầu với obstetrics_gynecology.py
"""
import ast
import json
import shutil
from pathlib import Path
from typing import Dict, List, Set, Any
from collections import defaultdict
from datetime import datetime

def get_string_value(node):
    """Lấy giá trị string từ AST node"""
    if isinstance(node, ast.Constant) and isinstance(node.value, str):
        return node.value
    elif hasattr(node, 's'):
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

def is_drug_entry(keys: Set[str]) -> bool:
    """Kiểm tra xem dict có phải là entry thuốc không"""
    required_fields = {'group', 'vietnamese_name', 'administration', 'indications'}
    return len(keys & required_fields) >= 2

def is_not_field_name(name: str) -> bool:
    """Kiểm tra xem tên có phải là field name không"""
    known_non_drugs = {
        'risk_flags', 'organ_toxicity', 'pediatric_dosing', 'geriatric_dosing',
        'brand_names', 'cost_estimate', 'contraindications_detail',
        'reversal_agents', 'dosage', 'renal_adjustment', 'pharmacokinetics',
        'drug_interactions', 'references', 'pregnancy_lactation',
        'hepatic_adjustment', 'overdose_management', 'administration_instructions',
        'contraindications', 'side_effects', 'interactions', 'pregnancy',
        'administration', 'indications', 'group', 'vietnamese_name',
    }
    if name in known_non_drugs:
        return False
    if name.islower() and name.count('_') >= 2:
        if name not in ['iv', 'po', 'im', 'sc', 'iv_bolus', 'iv_infusion']:
            return False
    return True

def get_group_from_drug(drug_dict_node: ast.Dict) -> str:
    """Lấy group từ drug entry"""
    for key_node, value_node in zip(drug_dict_node.keys, drug_dict_node.values):
        key = get_string_value(key_node)
        if key == 'group':
            group_value = get_string_value(value_node)
            if group_value:
                return group_value
    return "other"

def categorize_drugs_by_group(file_path: Path) -> Dict[str, List[Dict[str, Any]]]:
    """Phân loại thuốc theo group"""
    categories = defaultdict(list)
    
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        tree = ast.parse(content)
        
        # Tìm OBSTETRICS_GYNECOLOGY_DRUGS assignment
        for node in ast.walk(tree):
            if isinstance(node, ast.Assign):
                for target in node.targets:
                    if isinstance(target, ast.Name) and target.id.endswith('_DRUGS'):
                        if isinstance(node.value, ast.Dict):
                            for key_node, value_node in zip(node.value.keys, node.value.values):
                                drug_name = get_string_value(key_node)
                                
                                if drug_name and is_not_field_name(drug_name):
                                    if isinstance(value_node, ast.Dict):
                                        keys = extract_dict_keys(value_node)
                                        if is_drug_entry(keys):
                                            group = get_group_from_drug(value_node)
                                            
                                            # Phân loại theo group
                                            category = "other"
                                            group_lower = group.lower()
                                            
                                            if "contraceptive" in group_lower or "oral contraceptive" in group_lower:
                                                category = "contraceptives"
                                            elif "hormone" in group_lower or "estrogen" in group_lower or "progesterone" in group_lower or "hrt" in group_lower:
                                                category = "hormone_replacement"
                                            elif "fertility" in group_lower or "ovulation" in group_lower:
                                                category = "fertility_drugs"
                                            elif "antifungal" in group_lower or "candidiasis" in group_lower or "vaginal" in group_lower:
                                                category = "vaginal_medications"
                                            else:
                                                category = "other_obgyn"
                                            
                                            # Lưu drug entry (cần convert AST node thành code)
                                            drug_code = ast.get_source_segment(content, value_node)
                                            if drug_code:
                                                categories[category].append({
                                                    'name': drug_name,
                                                    'group': group,
                                                    'code': drug_code,
                                                })
    except Exception as e:
        print(f"Error processing {file_path}: {e}")
        return {}
    
    return categories

def split_obstetrics_gynecology():
    """Tách obstetrics_gynecology.py thành subfolder"""
    source_file = Path("drugs/drug_modules/obstetrics_gynecology.py")
    target_dir = Path("drugs/drug_modules/obstetrics_gynecology")
    
    if not source_file.exists():
        print(f"File not found: {source_file}")
        return
    
    # Tạo thư mục nếu chưa có
    target_dir.mkdir(exist_ok=True)
    
    # Phân loại thuốc
    print("Dang phan loai thuoc...")
    categories = categorize_drugs_by_group(source_file)
    
    print(f"Tim thay {sum(len(drugs) for drugs in categories.values())} thuoc trong {len(categories)} nhom")
    
    # Tạo file cho từng category
    file_mappings = {
        'contraceptives': 'contraceptives.py',
        'hormone_replacement': 'hormone_replacement.py',
        'fertility_drugs': 'fertility_drugs.py',
        'vaginal_medications': 'vaginal_medications.py',
        'other_obgyn': 'other_obgyn.py',
    }
    
    # Đọc file gốc để lấy header và imports
    with open(source_file, 'r', encoding='utf-8') as f:
        original_content = f.read()
    
    # Tạo header
    header = '''"""
Obstetrics and Gynecology Medications
Includes contraception and hormone therapy drugs
Note: Uterotonics are in emergency/uterotonics.py
"""
from typing import Dict, Any

'''
    
    # Tạo file cho từng category
    created_files = {}
    for category, drugs in categories.items():
        if not drugs:
            continue
        
        filename = file_mappings.get(category, f'{category}.py')
        filepath = target_dir / filename
        
        # Tạo nội dung file
        content = header
        var_name = f"{category.upper().replace('_', '_')}_DRUGS"
        content += f"{var_name}: Dict[str, Dict[str, Any]] = {{\n"
        
        for drug in drugs:
            # Format drug entry
            content += f'    "{drug["name"]}": {drug["code"]},\n\n'
        
        content += "}\n\n"
        content += f"__all__ = ['{var_name}']\n"
        
        # Ghi file
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        
        created_files[category] = var_name
        print(f"Da tao: {filepath} ({len(drugs)} thuoc)")
    
    # Tạo __init__.py
    init_content = '''"""
Obstetrics and Gynecology Drugs
Combines all OB/GYN drugs from category-specific files
"""
from typing import Dict, Any

'''
    
    for category, var_name in created_files.items():
        filename = file_mappings.get(category, f'{category}.py')
        module_name = filename[:-3]  # Remove .py
        init_content += f"from .{module_name} import {var_name}\n"
    
    init_content += "\n# Combine all OB/GYN drugs\n"
    init_content += "OBSTETRICS_GYNECOLOGY_DRUGS: Dict[str, Dict[str, Any]] = {\n"
    
    for var_name in created_files.values():
        init_content += f"    **{var_name},\n"
    
    init_content += "}\n\n"
    init_content += "__all__ = ['OBSTETRICS_GYNECOLOGY_DRUGS']\n"
    
    init_file = target_dir / "__init__.py"
    with open(init_file, 'w', encoding='utf-8') as f:
        f.write(init_content)
    
    print(f"Da tao: {init_file}")
    
    # Backup file cũ và tạo wrapper
    backup_file = source_file.with_suffix('.py.backup')
    shutil.copy2(source_file, backup_file)
    print(f"Da backup: {backup_file}")
    
    # Tạo wrapper file mới
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

def main():
    """Hàm chính"""
    import sys
    import io
    if sys.platform == 'win32':
        sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')
    
    print("Bat dau tach file obstetrics_gynecology.py...")
    split_obstetrics_gynecology()
    print("Hoan thanh!")

if __name__ == "__main__":
    main()

