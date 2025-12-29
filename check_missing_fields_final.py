"""
Kiểm tra toàn bộ các thuốc xem có thiếu field nào không
Sử dụng AST để parse chính xác
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

def find_drug_dicts_in_ast(tree: ast.AST) -> Dict[str, Set[str]]:
    """Tìm tất cả drug dictionaries trong AST và trích xuất keys"""
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
                                # Field names are usually lowercase with underscores and multiple parts
                                is_field_name = (
                                    drug_name.islower() and 
                                    '_' in drug_name and 
                                    drug_name.count('_') >= 2 and
                                    drug_name not in ['iv', 'po', 'im', 'sc']  # exceptions
                                )
                                
                                if ('group' in value_keys or 'vietnamese_name' in value_keys) and not is_field_name:
                                    # This is a real drug entry
                                    drugs[drug_name] = value_keys
    
    return drugs

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

def load_all_drugs() -> Dict[str, Set[str]]:
    """Load tất cả drugs từ các file module"""
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
                file_drugs = find_drug_dicts_in_ast(tree)
                
                # If AST method didn't find drugs, try regex fallback
                if not file_drugs:
                    # Regex fallback: find "DrugName": { ... }
                    # Only match if it's at the start of a line (likely a drug name)
                    pattern = r'^\s+["\']([^"\']+)["\']\s*:\s*\{'
                    drug_matches = re.finditer(pattern, content, re.MULTILINE)
                    
                    for match in drug_matches:
                        drug_name = match.group(1)
                        # Filter out field names (usually lowercase with underscores)
                        # Drug names are usually capitalized or have mixed case
                        if drug_name and (drug_name[0].isupper() or not '_' in drug_name or drug_name.count('_') < 2):
                            if drug_name not in all_drugs:
                                # Find fields for this drug using regex
                                fields = set()
                                
                                # Find the dict for this drug
                                start = match.end() - 1
                                # Simple: just check if field names appear after this drug name
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
                # Skip files with syntax errors
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
    print("KIEM TRA THIEU FIELD TRONG TOAN BO THUOC")
    print("=" * 70)
    print()
    
    print("Dang doc cac file module...")
    all_drugs = load_all_drugs()
    
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
                if count <= 10:
                    for drug in by_field[field]:
                        print(f"    + {drug}")
                elif count <= 20:
                    for drug in by_field[field][:10]:
                        print(f"    + {drug}")
                    print(f"    ... va {count - 10} thuoc khac")
                else:
                    for drug in by_field[field][:5]:
                        print(f"    + {drug}")
                    print(f"    ... va {count - 5} thuoc khac")
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
    
    # Top 10 thuốc thiếu nhiều field nhất
    print("\n" + "=" * 70)
    print("TOP 10 THUOC THIEU NHIEU FIELD NHAT")
    print("=" * 70)
    
    sorted_drugs = sorted(all_results, key=lambda x: x['total_missing'], reverse=True)
    for i, result in enumerate(sorted_drugs[:10], 1):
        missing = result['missing_core'] + result['missing_extended'] + result['missing_enhanced']
        if missing:
            print(f"\n{i}. {result['drug_name']}: Thieu {len(missing)} fields")
            if result['missing_core']:
                print(f"   Core: {', '.join(result['missing_core'])}")
            if result['missing_extended']:
                print(f"   Extended: {', '.join(result['missing_extended'][:3])}")
            if result['missing_enhanced']:
                print(f"   Enhanced: {len(result['missing_enhanced'])} fields")
    
    print("\n" + "=" * 70)

if __name__ == "__main__":
    main()

