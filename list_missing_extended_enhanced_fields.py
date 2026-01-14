"""
Script để liệt kê các thuốc thiếu extended và enhanced fields trong file chính
"""
import ast
import re
from pathlib import Path
from collections import defaultdict
from typing import Dict, Set

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

def find_drug_dicts_in_ast(tree: ast.AST) -> Dict[str, Set[str]]:
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
                                    drugs[drug_name] = value_keys
    
    return drugs

def load_all_drugs_with_files() -> Dict[str, Dict]:
    all_drugs = {}
    base_path = Path("drugs/drug_modules")
    
    for py_file in sorted(base_path.rglob("*.py")):
        if (py_file.name == "__init__.py" or 
            py_file.name.endswith(".backup") or 
            ".backups" in str(py_file)):
            continue
        
        try:
            with open(py_file, 'r', encoding='utf-8') as f:
                content = f.read()
            
            try:
                tree = ast.parse(content)
                file_drugs = find_drug_dicts_in_ast(tree)
                
                for drug_name, fields in file_drugs.items():
                    all_drugs[drug_name] = {
                        'fields': fields,
                        'file': py_file
                    }
                
            except SyntaxError:
                pass
                
        except Exception:
            pass
    
    return all_drugs

def main():
    print("\n" + "=" * 70)
    print("LIET KE THUOC THIEU EXTENDED & ENHANCED FIELDS")
    print("=" * 70)
    print()
    
    print("Dang doc cac file module...")
    all_drugs = load_all_drugs_with_files()
    
    total_drugs = len(all_drugs)
    print(f"Tim thay {total_drugs} thuoc trong file chinh")
    print()
    
    # Kiểm tra extended fields
    drugs_with_missing_extended = []
    drugs_with_missing_enhanced = []
    
    for drug_name, drug_info in all_drugs.items():
        fields = drug_info['fields']
        
        missing_extended = [f for f in EXTENDED_FIELDS if f not in fields]
        missing_enhanced = [f for f in ENHANCED_FIELDS if f not in fields]
        
        if missing_extended:
            drugs_with_missing_extended.append({
                'drug_name': drug_name,
                'file': drug_info['file'],
                'missing': missing_extended
            })
        
        if missing_enhanced:
            drugs_with_missing_enhanced.append({
                'drug_name': drug_name,
                'file': drug_info['file'],
                'missing': missing_enhanced
            })
    
    # Phân loại theo field
    by_field_ext = defaultdict(list)
    for result in drugs_with_missing_extended:
        for field in result['missing']:
            by_field_ext[field].append(result)
    
    by_field_enh = defaultdict(list)
    for result in drugs_with_missing_enhanced:
        for field in result['missing']:
            by_field_enh[field].append(result)
    
    # Xuất kết quả
    print("=" * 70)
    print(f"EXTENDED FIELDS: {len(drugs_with_missing_extended)} thuoc thieu")
    print("=" * 70)
    
    for field in EXTENDED_FIELDS:
        if field in by_field_ext:
            print(f"\n{field}: {len(by_field_ext[field])} thuoc")
            if len(by_field_ext[field]) <= 10:
                for r in by_field_ext[field]:
                    print(f"  - {r['drug_name']} ({r['file'].name})")
    
    print("\n" + "=" * 70)
    print(f"ENHANCED FIELDS: {len(drugs_with_missing_enhanced)} thuoc thieu")
    print("=" * 70)
    
    sorted_enh = sorted(by_field_enh.items(), key=lambda x: len(x[1]), reverse=True)
    for field, results in sorted_enh[:10]:  # Top 10
        print(f"\n{field}: {len(results)} thuoc")
        if len(results) <= 5:
            for r in results:
                print(f"  - {r['drug_name']} ({r['file'].name})")
    
    # Xuất ra file
    output_file = Path("missing_extended_enhanced_fields.txt")
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write("=" * 70 + "\n")
        f.write("DANH SACH THUOC THIEU EXTENDED & ENHANCED FIELDS\n")
        f.write("=" * 70 + "\n\n")
        
        f.write(f"EXTENDED FIELDS: {len(drugs_with_missing_extended)} thuoc\n")
        f.write("-" * 70 + "\n\n")
        for field in EXTENDED_FIELDS:
            if field in by_field_ext:
                f.write(f"{field.upper()} ({len(by_field_ext[field])} thuoc):\n")
                for r in by_field_ext[field][:20]:
                    f.write(f"  - {r['drug_name']}\n")
                    f.write(f"    File: {r['file']}\n")
                if len(by_field_ext[field]) > 20:
                    f.write(f"    ... va {len(by_field_ext[field]) - 20} thuoc khac\n")
                f.write("\n")
        
        f.write("\n" + "=" * 70 + "\n")
        f.write(f"ENHANCED FIELDS: {len(drugs_with_missing_enhanced)} thuoc\n")
        f.write("=" * 70 + "\n\n")
        
        for field, results in sorted_enh:
            f.write(f"{field.upper()} ({len(results)} thuoc):\n")
            for r in results[:15]:
                f.write(f"  - {r['drug_name']}\n")
                f.write(f"    File: {r['file']}\n")
            if len(results) > 15:
                f.write(f"    ... va {len(results) - 15} thuoc khac\n")
            f.write("\n")
    
    print(f"\nDa luu danh sach vao: {output_file}")

if __name__ == "__main__":
    main()
