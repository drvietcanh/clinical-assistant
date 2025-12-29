"""
Script kiểm tra field cải tiến - nhận diện field chính xác hơn
Cải thiện để nhận diện field ngay cả khi cấu trúc hơi khác
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

# Các biến thể có thể có của field names (để nhận diện linh hoạt hơn)
FIELD_VARIANTS = {
    "references": ["references", "reference", "refs"],
    "administration_instructions": ["administration_instructions", "admin_instructions", "instructions"],
    "drug_interactions": ["drug_interactions", "interactions", "drug_interaction"],
    "pregnancy_lactation": ["pregnancy_lactation", "pregnancy", "lactation"],
    "hepatic_adjustment": ["hepatic_adjustment", "hepatic_dose", "liver_adjustment"],
    "overdose_management": ["overdose_management", "overdose", "poisoning"],
    "reversal_agents": ["reversal_agents", "antidote", "antidotes"],
}

def extract_dict_keys(node: ast.Dict) -> Set[str]:
    """Trích xuất các keys từ AST Dict node"""
    keys = set()
    for key_node in node.keys:
        key = get_string_value(key_node)
        if key:
            keys.add(key)
    return keys

def get_string_value(node):
    """Lấy giá trị string từ AST node"""
    if isinstance(node, ast.Constant) and isinstance(node.value, str):
        return node.value
    elif hasattr(node, 's'):  # ast.Str (deprecated)
        return node.s
    return None

def check_field_exists_flexible(fields: Set[str], field_name: str) -> bool:
    """Kiểm tra field có tồn tại không (linh hoạt hơn)"""
    # Kiểm tra trực tiếp
    if field_name in fields:
        return True
    
    # Kiểm tra các biến thể
    if field_name in FIELD_VARIANTS:
        for variant in FIELD_VARIANTS[field_name]:
            if variant in fields:
                return True
    
    return False

def find_drug_dicts_in_ast_improved(tree: ast.AST, content: str) -> Dict[str, Set[str]]:
    """Tìm tất cả drug dictionaries trong AST và trích xuất keys (cải tiến)"""
    drugs = {}
    
    # Find all assignments to _DRUGS variables
    for node in ast.walk(tree):
        if isinstance(node, ast.Assign):
            for target in node.targets:
                if isinstance(target, ast.Name) and target.id.endswith('_DRUGS'):
                    if isinstance(node.value, ast.Dict):
                        # This is a drug dictionary - iterate through top-level keys only
                        for key_node, value_node in zip(node.value.keys, node.value.values):
                            drug_name = get_string_value(key_node)
                            
                            if drug_name and isinstance(value_node, ast.Dict):
                                # Check if this looks like a drug entry (has 'group' or 'vietnamese_name')
                                value_keys = extract_dict_keys(value_node)
                                
                                # Only consider it a drug if it has drug-like fields
                                # AND the drug name doesn't look like a field name
                                is_field_name = (
                                    drug_name.islower() and 
                                    '_' in drug_name and 
                                    drug_name.count('_') >= 2 and
                                    drug_name not in ['iv', 'po', 'im', 'sc']  # exceptions
                                )
                                
                                if ('group' in value_keys or 'vietnamese_name' in value_keys) and not is_field_name:
                                    # This is a real drug entry
                                    # Cải thiện: cũng kiểm tra bằng regex trong content để đảm bảo
                                    # Tìm vị trí của drug trong content
                                    pattern = rf'["\']{re.escape(drug_name)}["\']\s*:\s*\{{'
                                    match = re.search(pattern, content)
                                    if match:
                                        # Tìm section của drug và kiểm tra field bằng regex (backup method)
                                        start_pos = match.end() - 1
                                        # Tìm vị trí kết thúc của dict
                                        brace_count = 0
                                        in_string = False
                                        string_char = None
                                        i = start_pos
                                        
                                        while i < len(content) and i < start_pos + 10000:  # Giới hạn để tránh quá dài
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
                                                        
                                                        # Kiểm tra field bằng regex (backup)
                                                        for field in ENHANCED_FIELDS:
                                                            if field not in value_keys:
                                                                # Kiểm tra bằng regex
                                                                field_pattern = rf'["\']{re.escape(field)}["\']\s*:'
                                                                if re.search(field_pattern, drug_section):
                                                                    value_keys.add(field)  # Thêm vào nếu tìm thấy
                                                        break
                                            i += 1
                                    
                                    drugs[drug_name] = value_keys
    
    return drugs

def check_drug_fields(drug_name: str, fields: Set[str]) -> Dict:
    """Kiểm tra fields của một thuốc (sử dụng logic linh hoạt)"""
    result = {
        'drug_name': drug_name,
        'missing_core': [],
        'missing_extended': [],
        'missing_enhanced': [],
        'total_missing': 0
    }
    
    for field in CORE_FIELDS:
        if not check_field_exists_flexible(fields, field):
            result['missing_core'].append(field)
            result['total_missing'] += 1
    
    for field in EXTENDED_FIELDS:
        if not check_field_exists_flexible(fields, field):
            result['missing_extended'].append(field)
    
    for field in ENHANCED_FIELDS:
        if not check_field_exists_flexible(fields, field):
            result['missing_enhanced'].append(field)
    
    return result

def load_all_drugs_improved() -> Dict[str, Set[str]]:
    """Load tất cả drugs từ các file module (phiên bản cải tiến)"""
    all_drugs = {}
    base_path = Path("drugs/drug_modules")
    
    files_processed = 0
    files_with_errors = 0
    
    for py_file in sorted(base_path.rglob("*.py")):
        if py_file.name == "__init__.py" or py_file.name.endswith(".backup"):
            continue
        
        try:
            with open(py_file, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Parse AST
            try:
                tree = ast.parse(content)
                file_drugs = find_drug_dicts_in_ast_improved(tree, content)
                
                # If AST method didn't find drugs, try regex fallback
                if not file_drugs:
                    # Regex fallback: find "DrugName": { ... }
                    pattern = r'^\s+["\']([^"\']+)["\']\s*:\s*\{'
                    drug_matches = re.finditer(pattern, content, re.MULTILINE)
                    
                    for match in drug_matches:
                        drug_name = match.group(1)
                        # Filter out field names
                        if drug_name and (drug_name[0].isupper() or not '_' in drug_name or drug_name.count('_') < 2):
                            if drug_name not in all_drugs:
                                # Find fields for this drug using regex
                                fields = set()
                                
                                # Find the dict for this drug
                                start = match.end() - 1
                                drug_section = content[max(0, start-100):min(len(content), start+5000)]
                                
                                for field in CORE_FIELDS + EXTENDED_FIELDS + ENHANCED_FIELDS:
                                    # Check if field appears in this drug's section
                                    field_pattern = rf'["\']{re.escape(field)}["\']\s*:'
                                    if re.search(field_pattern, drug_section):
                                        fields.add(field)
                                
                                file_drugs[drug_name] = fields
                
                all_drugs.update(file_drugs)
                files_processed += 1
                
            except SyntaxError:
                files_with_errors += 1
                pass
                
        except Exception as e:
            files_with_errors += 1
            pass
    
    print(f"  Da xu ly {files_processed} files")
    if files_with_errors > 0:
        print(f"  Co {files_with_errors} files bi loi (bo qua)")
    
    return all_drugs

def main():
    """Main function"""
    print("\n" + "=" * 70)
    print("KIEM TRA THIEU FIELD (PHIEN BAN CAI TIEN)")
    print("=" * 70)
    print()
    
    print("Dang doc cac file module...")
    all_drugs = load_all_drugs_improved()
    
    total_drugs = len(all_drugs)
    print(f"Tim thay {total_drugs} thuoc")
    print()
    
    if not all_drugs:
        print("[LOI] Khong tim thay thuoc nao")
        return
    
    # Kiểm tra fields
    all_results = []
    drugs_with_missing_core = []
    drugs_with_missing_extended = []
    drugs_with_missing_enhanced = []
    
    for drug_name, fields in all_drugs.items():
        result = check_drug_fields(drug_name, fields)
        all_results.append(result)
        
        if result['missing_core']:
            drugs_with_missing_core.append(result)
        
        if result['missing_extended']:
            drugs_with_missing_extended.append(result)
        
        if result['missing_enhanced']:
            drugs_with_missing_enhanced.append(result)
    
    # Báo cáo
    print("=" * 70)
    print("1. THIEU CORE FIELDS (Nghiem trong)")
    print("=" * 70)
    
    if drugs_with_missing_core:
        print(f"\n[LOI] Tim thay {len(drugs_with_missing_core)} thuoc thieu core fields:")
        print()
        
        by_field = defaultdict(list)
        for result in drugs_with_missing_core:
            for field in result['missing_core']:
                by_field[field].append(result['drug_name'])
        
        for field in CORE_FIELDS:
            if field in by_field:
                count = len(by_field[field])
                print(f"  - {field}: {count} thuoc thieu ({count*100//total_drugs if total_drugs > 0 else 0}%)")
    else:
        print("\n[OK] Tat ca thuoc deu co day du core fields")
    
    print("\n" + "=" * 70)
    print("2. THIEU EXTENDED FIELDS")
    print("=" * 70)
    
    if drugs_with_missing_extended:
        print(f"\n[WARNING] Tim thay {len(drugs_with_missing_extended)} thuoc thieu extended fields:")
        print()
        
        by_field = defaultdict(list)
        for result in drugs_with_missing_extended:
            for field in result['missing_extended']:
                by_field[field].append(result['drug_name'])
        
        for field in EXTENDED_FIELDS:
            if field in by_field:
                count = len(by_field[field])
                print(f"  - {field}: {count} thuoc thieu ({count*100//total_drugs if total_drugs > 0 else 0}%)")
    else:
        print("\n[OK] Tat ca thuoc deu co day du extended fields")
    
    print("\n" + "=" * 70)
    print("3. THIEU ENHANCED FIELDS (13 fields)")
    print("=" * 70)
    
    if drugs_with_missing_enhanced:
        print(f"\n[INFO] Tim thay {len(drugs_with_missing_enhanced)} thuoc thieu enhanced fields:")
        print()
        
        by_field = defaultdict(list)
        for result in drugs_with_missing_enhanced:
            for field in result['missing_enhanced']:
                by_field[field].append(result['drug_name'])
        
        sorted_fields = sorted(by_field.items(), key=lambda x: len(x[1]), reverse=True)
        
        print("Top enhanced fields bi thieu nhieu nhat:")
        for field, drugs in sorted_fields:
            count = len(drugs)
            pct = count*100//total_drugs if total_drugs > 0 else 0
            print(f"  - {field}: {count} thuoc thieu ({pct}%)")
    else:
        print("\n[OK] Tat ca thuoc deu co day du enhanced fields")
    
    # Thống kê tổng hợp
    print("\n" + "=" * 70)
    print("TOM TAT")
    print("=" * 70)
    
    total_missing_core = sum(len(r['missing_core']) for r in all_results)
    total_missing_extended = sum(len(r['missing_extended']) for r in all_results)
    total_missing_enhanced = sum(len(r['missing_enhanced']) for r in all_results)
    
    print(f"\nTong so thuoc: {total_drugs}")
    print(f"\nThieu core fields:")
    print(f"  - So thuoc thieu: {len(drugs_with_missing_core)} ({len(drugs_with_missing_core)*100//total_drugs if total_drugs > 0 else 0}%)")
    print(f"  - Tong so field thieu: {total_missing_core}")
    
    print(f"\nThieu extended fields:")
    print(f"  - So thuoc thieu: {len(drugs_with_missing_extended)} ({len(drugs_with_missing_extended)*100//total_drugs if total_drugs > 0 else 0}%)")
    print(f"  - Tong so field thieu: {total_missing_extended}")
    
    print(f"\nThieu enhanced fields:")
    print(f"  - So thuoc thieu: {len(drugs_with_missing_enhanced)} ({len(drugs_with_missing_enhanced)*100//total_drugs if total_drugs > 0 else 0}%)")
    print(f"  - Tong so field thieu: {total_missing_enhanced}")
    
    print("\n" + "=" * 70)
    print("GHI CHU: Script nay da duoc cai tien de nhan dien field chinh xac hon")
    print("Bang cach kiem tra ca AST va regex, nhan dien field ngay ca khi")
    print("cau truc hoi khac mot chut.")
    print("=" * 70)

if __name__ == "__main__":
    main()

