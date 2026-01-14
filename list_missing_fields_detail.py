"""
Script để liệt kê chi tiết các thuốc thiếu fields
Xuất ra file để dễ theo dõi và làm thủ công
"""
import ast
import re
from pathlib import Path
from collections import defaultdict
from typing import Dict, List, Set, Any

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

def find_drug_dicts_in_ast_improved(tree: ast.AST, content: str) -> Dict[str, Dict]:
    """Tìm tất cả drug dictionaries trong AST và trích xuất thông tin chi tiết"""
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
                                
                                # Chỉ lấy thuốc thực sự (có group hoặc vietnamese_name)
                                is_field_name = (
                                    drug_name.islower() and 
                                    '_' in drug_name and 
                                    drug_name.count('_') >= 2 and
                                    drug_name not in ['iv', 'po', 'im', 'sc']
                                )
                                
                                if ('group' in value_keys or 'vietnamese_name' in value_keys) and not is_field_name:
                                    # Tìm file chứa thuốc này
                                    pattern = rf'["\']{re.escape(drug_name)}["\']\s*:\s*\{{'
                                    match = re.search(pattern, content)
                                    if match:
                                        drugs[drug_name] = {
                                            'fields': value_keys,
                                            'file': None  # Sẽ được điền sau
                                        }
    
    return drugs

def find_drug_file(drug_name: str) -> Path:
    """Tìm file chứa một thuốc"""
    base_path = Path("drugs/drug_modules")
    
    for py_file in sorted(base_path.rglob("*.py")):
        if py_file.name == "__init__.py" or py_file.name.endswith(".backup"):
            continue
        
        try:
            with open(py_file, 'r', encoding='utf-8') as f:
                content = f.read()
            
            pattern = rf'["\']{re.escape(drug_name)}["\']\s*:\s*\{{'
            if re.search(pattern, content):
                # Kiểm tra xem có phải là drug thực sự
                drug_section_start = content.find(f'"{drug_name}"') or content.find(f"'{drug_name}'")
                if drug_section_start != -1:
                    # Tìm section của drug
                    start_pos = content.find('{', drug_section_start)
                    if start_pos != -1:
                        brace_count = 0
                        in_string = False
                        string_char = None
                        i = start_pos
                        
                        while i < len(content) and i < start_pos + 10000:
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
                                        end_pos = i + 1
                                        drug_section = content[start_pos:end_pos]
                                        
                                        if ('"group"' in drug_section or "'group'" in drug_section or 
                                            '"vietnamese_name"' in drug_section or "'vietnamese_name'" in drug_section):
                                            return py_file
                                        break
                            i += 1
        except Exception:
            pass
    
    return None

def check_drug_fields(drug_name: str, fields: Set[str]) -> Dict:
    """Kiểm tra fields của một thuốc"""
    result = {
        'drug_name': drug_name,
        'missing_core': [],
        'missing_extended': [],
        'missing_enhanced': [],
        'total_missing': 0
    }
    
    for field in CORE_FIELDS:
        if field not in fields:
            result['missing_core'].append(field)
            result['total_missing'] += 1
    
    for field in EXTENDED_FIELDS:
        if field not in fields:
            result['missing_extended'].append(field)
    
    for field in ENHANCED_FIELDS:
        if field not in fields:
            result['missing_enhanced'].append(field)
    
    return result

def load_all_drugs_with_files() -> Dict[str, Dict]:
    """Load tất cả drugs với thông tin file"""
    all_drugs = {}
    base_path = Path("drugs/drug_modules")
    
    files_processed = 0
    
    for py_file in sorted(base_path.rglob("*.py")):
        if py_file.name == "__init__.py" or py_file.name.endswith(".backup"):
            continue
        
        try:
            with open(py_file, 'r', encoding='utf-8') as f:
                content = f.read()
            
            try:
                tree = ast.parse(content)
                file_drugs = find_drug_dicts_in_ast_improved(tree, content)
                
                # Gán file cho mỗi drug
                for drug_name in file_drugs:
                    file_drugs[drug_name]['file'] = py_file
                
                all_drugs.update(file_drugs)
                files_processed += 1
                
            except SyntaxError:
                pass
                
        except Exception:
            pass
    
    print(f"  Da xu ly {files_processed} files")
    
    return all_drugs

def main():
    """Main function"""
    print("\n" + "=" * 70)
    print("LIET KE CHI TIET CAC THUOC THIEU FIELDS")
    print("=" * 70)
    print()
    
    print("Dang doc cac file module...")
    all_drugs = load_all_drugs_with_files()
    
    total_drugs = len(all_drugs)
    print(f"Tim thay {total_drugs} thuoc")
    print()
    
    if not all_drugs:
        print("[LOI] Khong tim thay thuoc nao")
        return
    
    # Kiểm tra fields
    drugs_with_missing_core = []
    drugs_with_missing_extended = []
    drugs_with_missing_enhanced = []
    
    for drug_name, drug_info in all_drugs.items():
        fields = drug_info['fields']
        result = check_drug_fields(drug_name, fields)
        result['file'] = drug_info['file']
        
        if result['missing_core']:
            drugs_with_missing_core.append(result)
        
        if result['missing_extended']:
            drugs_with_missing_extended.append(result)
        
        if result['missing_enhanced']:
            drugs_with_missing_enhanced.append(result)
    
    # Xuất ra file
    output_file = Path("missing_fields_report.txt")
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write("=" * 70 + "\n")
        f.write("BAO CAO CAC THUOC THIEU FIELDS\n")
        f.write("=" * 70 + "\n\n")
        
        # Core fields
        f.write("1. THIEU CORE FIELDS (27 thuoc)\n")
        f.write("=" * 70 + "\n\n")
        
        by_field = defaultdict(list)
        for result in drugs_with_missing_core:
            for field in result['missing_core']:
                by_field[field].append(result)
        
        for field in CORE_FIELDS:
            if field in by_field:
                f.write(f"\n{field.upper()} ({len(by_field[field])} thuoc):\n")
                f.write("-" * 70 + "\n")
                for result in by_field[field]:
                    f.write(f"  - {result['drug_name']}\n")
                    f.write(f"    File: {result['file']}\n")
                    f.write(f"    Thieu: {', '.join(result['missing_core'])}\n\n")
        
        # Extended fields
        f.write("\n\n" + "=" * 70 + "\n")
        f.write("2. THIEU EXTENDED FIELDS (50 thuoc)\n")
        f.write("=" * 70 + "\n\n")
        
        by_field_ext = defaultdict(list)
        for result in drugs_with_missing_extended:
            for field in result['missing_extended']:
                by_field_ext[field].append(result)
        
        for field in EXTENDED_FIELDS:
            if field in by_field_ext:
                f.write(f"\n{field.upper()} ({len(by_field_ext[field])} thuoc):\n")
                f.write("-" * 70 + "\n")
                for result in by_field_ext[field][:20]:  # Chỉ hiển thị 20 đầu tiên
                    f.write(f"  - {result['drug_name']}\n")
                    f.write(f"    File: {result['file']}\n")
                    if len(by_field_ext[field]) > 20:
                        f.write(f"\n    ... va {len(by_field_ext[field]) - 20} thuoc khac\n")
                        break
                f.write("\n")
        
        # Enhanced fields - chỉ liệt kê top 5
        f.write("\n\n" + "=" * 70 + "\n")
        f.write("3. THIEU ENHANCED FIELDS (303 thuoc) - TOP 5 FIELD THIEU NHIEU NHAT\n")
        f.write("=" * 70 + "\n\n")
        
        by_field_enh = defaultdict(list)
        for result in drugs_with_missing_enhanced:
            for field in result['missing_enhanced']:
                by_field_enh[field].append(result)
        
        sorted_fields = sorted(by_field_enh.items(), key=lambda x: len(x[1]), reverse=True)[:5]
        
        for field, results in sorted_fields:
            f.write(f"\n{field.upper()} ({len(results)} thuoc):\n")
            f.write("-" * 70 + "\n")
            for result in results[:10]:  # Chỉ hiển thị 10 đầu tiên
                f.write(f"  - {result['drug_name']}\n")
                f.write(f"    File: {result['file']}\n")
            if len(results) > 10:
                f.write(f"\n    ... va {len(results) - 10} thuoc khac\n")
            f.write("\n")
    
    print(f"\nDa luu bao cao vao: {output_file}")
    print(f"\nTong ket:")
    print(f"  - Core fields: {len(drugs_with_missing_core)} thuoc")
    print(f"  - Extended fields: {len(drugs_with_missing_extended)} thuoc")
    print(f"  - Enhanced fields: {len(drugs_with_missing_enhanced)} thuoc")

if __name__ == "__main__":
    main()
