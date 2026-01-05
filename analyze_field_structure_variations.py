"""
Phân tích các biến thể cấu trúc field trong hệ thống thuốc
Tìm các field có cấu trúc khác nhau giữa các thuốc
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

def extract_dict_structure(node: ast.Dict, max_depth: int = 3, current_depth: int = 0) -> Dict[str, Any]:
    """Trích xuất cấu trúc của dict"""
    if current_depth >= max_depth:
        return {"_max_depth_reached": True}
    
    structure = {}
    for key_node, value_node in zip(node.keys, node.values):
        key = get_string_value(key_node)
        if key:
            if isinstance(value_node, ast.Dict):
                structure[key] = extract_dict_structure(value_node, max_depth, current_depth + 1)
            elif isinstance(value_node, ast.List):
                structure[key] = {"_type": "list", "_length": len(value_node.elts)}
            elif isinstance(value_node, (ast.Constant, ast.Str, ast.NameConstant)):
                if isinstance(value_node, ast.Constant):
                    value = node.value
                elif hasattr(value_node, 's'):
                    value = value_node.s
                elif isinstance(value_node, ast.NameConstant):
                    value = value_node.value
                else:
                    value = None
                structure[key] = {"_type": type(value).__name__ if value is not None else "None"}
            else:
                structure[key] = {"_type": "unknown"}
    
    return structure

def analyze_field_structures():
    """Phân tích cấu trúc của các field trong tất cả thuốc"""
    base_path = Path("drugs/drug_modules")
    field_structures = defaultdict(lambda: defaultdict(int))
    field_examples = defaultdict(list)
    
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
                                                    if field_name:
                                                        # Lấy cấu trúc
                                                        if isinstance(field_value_node, ast.Dict):
                                                            structure = extract_dict_structure(field_value_node)
                                                            structure_str = json.dumps(structure, sort_keys=True)
                                                            field_structures[field_name][structure_str] += 1
                                                            
                                                            if len(field_examples[field_name]) < 5:
                                                                field_examples[field_name].append({
                                                                    'drug': drug_name,
                                                                    'file': str(item),
                                                                    'structure': structure
                                                                })
                                                        elif isinstance(field_value_node, ast.List):
                                                            field_structures[field_name]['_type_list'] += 1
                                                        else:
                                                            field_structures[field_name]['_type_other'] += 1
                except Exception as e:
                    print(f"Error reading {item}: {e}")
                    continue
            elif item.is_dir():
                scan_directory(item)
    
    scan_directory(base_path)
    
    return field_structures, field_examples

def main():
    print("="*60)
    print("PHAN TICH CAU TRUC FIELD")
    print("="*60)
    
    print("\nDang quet tat ca file...")
    field_structures, field_examples = analyze_field_structures()
    
    print(f"\nTim thay {len(field_structures)} field co cau truc")
    
    # Tìm các field có nhiều cấu trúc khác nhau
    print("\n" + "="*60)
    print("CAC FIELD CO NHIEU CAU TRUC KHAC NHAU")
    print("="*60)
    
    variations = []
    for field_name, structures in field_structures.items():
        if len(structures) > 1:
            variations.append({
                'field': field_name,
                'variation_count': len(structures),
                'structures': structures,
                'examples': field_examples.get(field_name, [])
            })
    
    variations.sort(key=lambda x: x['variation_count'], reverse=True)
    
    for var in variations[:20]:
        print(f"\n{var['field']}: {var['variation_count']} cau truc khac nhau")
        for i, (struct_str, count) in enumerate(list(var['structures'].items())[:3], 1):
            print(f"  {i}. {count} thuoc: {struct_str[:100]}...")
    
    # Lưu báo cáo
    report = {
        'field_variations': variations,
        'all_structures': dict(field_structures),
        'examples': dict(field_examples)
    }
    
    with open('field_structure_variations.json', 'w', encoding='utf-8') as f:
        json.dump(report, f, indent=2, ensure_ascii=False)
    
    print(f"\nDa luu: field_structure_variations.json")
    print("="*60)

if __name__ == "__main__":
    main()

