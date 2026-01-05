"""
Phân tích chi tiết các biến thể cấu trúc field
Tìm tất cả các cấu trúc khác nhau của các field quan trọng
"""
import sys
import json
import ast
from pathlib import Path
from typing import Dict, List, Set, Any
from collections import defaultdict
import io

sys.path.insert(0, str(Path.cwd()))

if sys.platform == 'win32':
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')

def get_string_value(node):
    """Lấy giá trị string từ AST node"""
    if isinstance(node, ast.Constant) and isinstance(node.value, str):
        return node.value
    elif hasattr(node, 's'):
        return node.s
    return None

def extract_dict_keys(node: ast.Dict) -> Set[str]:
    """Trích xuất tất cả keys của dict"""
    keys = set()
    for key_node in node.keys:
        key = get_string_value(key_node)
        if key:
            keys.add(key)
    return keys

def extract_field_structure(drug_name: str, field_name: str, value_node: ast.AST) -> Dict[str, Any]:
    """Trích xuất cấu trúc của một field"""
    structure = {
        'drug': drug_name,
        'field': field_name,
        'type': type(value_node).__name__
    }
    
    if isinstance(value_node, ast.Dict):
        keys = extract_dict_keys(value_node)
        structure['keys'] = sorted(list(keys))
        structure['key_count'] = len(keys)
        
        # Kiểm tra nested dicts
        nested_keys = {}
        for key_node, value_node_nested in zip(value_node.keys, value_node.values):
            key = get_string_value(key_node)
            if key and isinstance(value_node_nested, ast.Dict):
                nested_keys[key] = sorted(list(extract_dict_keys(value_node_nested)))
        if nested_keys:
            structure['nested_keys'] = nested_keys
            
    elif isinstance(value_node, ast.List):
        structure['length'] = len(value_node.elts)
        structure['is_empty'] = len(value_node.elts) == 0
    elif isinstance(value_node, (ast.Constant, ast.Str, ast.NameConstant)):
        if isinstance(value_node, ast.Constant):
            value = value_node.value
        elif hasattr(value_node, 's'):
            value = value_node.s
        elif isinstance(value_node, ast.NameConstant):
            value = value_node.value
        else:
            value = None
        structure['value_type'] = type(value).__name__ if value is not None else "None"
        structure['is_empty'] = (isinstance(value, str) and not value.strip()) or value is None or value == ""
    
    return structure

def analyze_specific_fields():
    """Phân tích các field quan trọng có thể có cấu trúc khác nhau"""
    base_path = Path("drugs/drug_modules")
    
    # Các field cần phân tích chi tiết
    target_fields = [
        'pregnancy_lactation',
        'hepatic_adjustment',
        'overdose_management',
        'contraindications',
        'drug_interactions',
        'administration_instructions',
        'references'
    ]
    
    field_structures = {field: defaultdict(list) for field in target_fields}
    
    def scan_directory(directory: Path):
        """Quét đệ quy một thư mục"""
        for item in sorted(directory.iterdir()):
            if item.name == '__init__.py' or item.name == '__pycache__' or item.name.endswith('.pyc'):
                continue
            
            if item.is_file() and item.suffix == '.py':
                try:
                    with open(item, 'r', encoding='utf-8') as f:
                        content = f.read()
                    
                    tree = ast.parse(content)
                    
                    for node in ast.walk(tree):
                        if isinstance(node, ast.Assign):
                            for target in node.targets:
                                if isinstance(target, ast.Name) and (target.id.endswith('_DRUGS') or target.id.isupper()):
                                    if isinstance(node.value, ast.Dict):
                                        for key_node, value_node in zip(node.value.keys, node.value.values):
                                            drug_name = get_string_value(key_node)
                                            if drug_name and isinstance(value_node, ast.Dict):
                                                # Phân tích từng field
                                                for field_key_node, field_value_node in zip(value_node.keys, value_node.values):
                                                    field_name = get_string_value(field_key_node)
                                                    if field_name in target_fields:
                                                        structure = extract_field_structure(
                                                            drug_name, field_name, field_value_node
                                                        )
                                                        structure['file'] = str(item)
                                                        # Tạo key để nhóm các cấu trúc giống nhau
                                                        if isinstance(field_value_node, ast.Dict):
                                                            keys_str = json.dumps(sorted(list(extract_dict_keys(field_value_node))), sort_keys=True)
                                                            structure_key = f"dict_keys:{keys_str}"
                                                        elif isinstance(field_value_node, ast.List):
                                                            structure_key = "list"
                                                        else:
                                                            structure_key = f"other:{structure.get('value_type', 'unknown')}"
                                                        
                                                        field_structures[field_name][structure_key].append(structure)
                except Exception as e:
                    print(f"Error reading {item}: {e}")
                    continue
            elif item.is_dir():
                scan_directory(item)
    
    scan_directory(base_path)
    
    return field_structures

def main():
    print("="*60)
    print("PHAN TICH CHI TIET CAU TRUC FIELD")
    print("="*60)
    
    print("\nDang quet tat ca file...")
    field_structures = analyze_specific_fields()
    
    report = {}
    
    for field_name, structures in field_structures.items():
        print(f"\n{field_name}: {len(structures)} cau truc khac nhau")
        report[field_name] = {}
        
        for structure_key, examples in structures.items():
            count = len(examples)
            print(f"  - {structure_key}: {count} thuoc")
            
            # Lấy ví dụ
            sample = examples[0] if examples else {}
            report[field_name][structure_key] = {
                'count': count,
                'structure': {
                    'type': sample.get('type'),
                    'keys': sample.get('keys'),
                    'nested_keys': sample.get('nested_keys'),
                    'key_count': sample.get('key_count'),
                },
                'examples': examples[:3]  # 3 ví dụ đầu
            }
    
    # Lưu báo cáo
    with open('field_structure_detailed_analysis.json', 'w', encoding='utf-8') as f:
        json.dump(report, f, indent=2, ensure_ascii=False)
    
    print(f"\nDa luu: field_structure_detailed_analysis.json")
    print("="*60)

if __name__ == "__main__":
    main()

