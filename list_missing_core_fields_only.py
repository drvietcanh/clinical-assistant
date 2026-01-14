"""
Script để liệt kê chi tiết các thuốc thiếu CORE FIELDS trong file chính (không phải backup)
"""
import ast
import re
from pathlib import Path
from collections import defaultdict
from typing import Dict, List, Set

CORE_FIELDS = [
    "group",
    "vietnamese_name", 
    "administration",
    "indications",
    "dosage"
]

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

def find_drug_dicts_in_ast(tree: ast.AST, content: str) -> Dict[str, Dict]:
    """Tìm tất cả drug dictionaries trong AST"""
    drugs = {}
    
    for node in ast.walk(tree):
        if isinstance(node, ast.Assign):
            for target in node.targets:
                if isinstance(target, ast.Name) and target.id.endswith('_DRUGS'):
                    if isinstance(node.value, ast.Dict):
                        for key_node, value_node in zip(node.value.keys, node.value.values):
                            drug_name = get_string_value(key_node)
                            
                            if drug_name and isinstance(value_node, ast.Dict):
                                value_keys = extract_dict_keys(value_node)
                                
                                is_field_name = (
                                    drug_name.islower() and 
                                    '_' in drug_name and 
                                    drug_name.count('_') >= 2 and
                                    drug_name not in ['iv', 'po', 'im', 'sc']
                                )
                                
                                if ('group' in value_keys or 'vietnamese_name' in value_keys) and not is_field_name:
                                    drugs[drug_name] = {
                                        'fields': value_keys,
                                        'file': None
                                    }
    
    return drugs

def load_all_drugs_with_files() -> Dict[str, Dict]:
    """Load tất cả drugs với thông tin file"""
    all_drugs = {}
    base_path = Path("drugs/drug_modules")
    
    for py_file in sorted(base_path.rglob("*.py")):
        # Bỏ qua backup files và __init__.py
        if (py_file.name == "__init__.py" or 
            py_file.name.endswith(".backup") or 
            ".backups" in str(py_file)):
            continue
        
        try:
            with open(py_file, 'r', encoding='utf-8') as f:
                content = f.read()
            
            try:
                tree = ast.parse(content)
                file_drugs = find_drug_dicts_in_ast(tree, content)
                
                for drug_name in file_drugs:
                    file_drugs[drug_name]['file'] = py_file
                
                all_drugs.update(file_drugs)
                
            except SyntaxError:
                pass
                
        except Exception:
            pass
    
    return all_drugs

def check_drug_fields(drug_name: str, fields: Set[str]) -> Dict:
    """Kiểm tra fields của một thuốc"""
    result = {
        'drug_name': drug_name,
        'missing_core': [],
        'file': None
    }
    
    for field in CORE_FIELDS:
        if field not in fields:
            result['missing_core'].append(field)
    
    return result

def main():
    """Main function"""
    print("\n" + "=" * 70)
    print("LIET KE CAC THUOC THIEU CORE FIELDS (FILE CHINH)")
    print("=" * 70)
    print()
    
    print("Dang doc cac file module...")
    all_drugs = load_all_drugs_with_files()
    
    total_drugs = len(all_drugs)
    print(f"Tim thay {total_drugs} thuoc trong file chinh")
    print()
    
    if not all_drugs:
        print("[LOI] Khong tim thay thuoc nao")
        return
    
    # Kiểm tra fields
    drugs_with_missing_core = []
    
    for drug_name, drug_info in all_drugs.items():
        fields = drug_info['fields']
        result = check_drug_fields(drug_name, fields)
        result['file'] = drug_info['file']
        
        if result['missing_core']:
            drugs_with_missing_core.append(result)
    
    # Phân loại theo field
    by_field = defaultdict(list)
    for result in drugs_with_missing_core:
        for field in result['missing_core']:
            by_field[field].append(result)
    
    # Xuất kết quả
    print("=" * 70)
    print(f"TONG CONG: {len(drugs_with_missing_core)} thuoc thieu core fields")
    print("=" * 70)
    print()
    
    for field in CORE_FIELDS:
        if field in by_field:
            print(f"\n{field.upper()} ({len(by_field[field])} thuoc):")
            print("-" * 70)
            for result in by_field[field]:
                print(f"  - {result['drug_name']}")
                print(f"    File: {result['file']}")
                print(f"    Thieu: {', '.join(result['missing_core'])}")
                print()
    
    # Xuất ra file
    output_file = Path("missing_core_fields_list.txt")
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write("=" * 70 + "\n")
        f.write("DANH SACH THUOC THIEU CORE FIELDS (FILE CHINH)\n")
        f.write("=" * 70 + "\n\n")
        f.write(f"Tong cong: {len(drugs_with_missing_core)} thuoc\n\n")
        
        for field in CORE_FIELDS:
            if field in by_field:
                f.write(f"\n{field.upper()} ({len(by_field[field])} thuoc):\n")
                f.write("-" * 70 + "\n")
                for result in by_field[field]:
                    f.write(f"  - {result['drug_name']}\n")
                    f.write(f"    File: {result['file']}\n")
                    f.write(f"    Thieu: {', '.join(result['missing_core'])}\n\n")
    
    print(f"\nDa luu danh sach vao: {output_file}")

if __name__ == "__main__":
    main()
