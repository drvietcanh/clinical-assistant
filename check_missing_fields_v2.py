"""
Kiểm tra toàn bộ các thuốc xem có thiếu field nào không
Load trực tiếp từ các file module, không cần streamlit
"""
import ast
import re
from pathlib import Path
from collections import defaultdict
from typing import Dict, List, Set

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

META_FIELDS = [
    "risk_flags",
    "guideline_tags",
    "availability_vietnam"
]

def extract_drugs_from_file(file_path: Path) -> Dict:
    """Trích xuất drugs từ một file Python"""
    drugs = {}
    
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Parse AST để tìm dictionary assignments
        tree = ast.parse(content)
        
        for node in ast.walk(tree):
            if isinstance(node, ast.Assign):
                for target in node.targets:
                    if isinstance(target, ast.Name) and target.id.endswith('_DRUGS'):
                        # Đây là một drug dictionary
                        if isinstance(node.value, ast.Dict):
                            # Convert AST dict to Python dict
                            try:
                                # Eval the dictionary (safe because we control the source)
                                # Actually, better to compile and execute in a safe way
                                code = compile(ast.Expression(node.value), file_path, 'eval')
                                # But this won't work for complex structures
                                # Let's use a different approach: regex + eval
                                pass
                            except:
                                pass
    except:
        pass
    
    # Alternative: Use regex to find dictionary patterns
    # Pattern: "DrugName": { ... }
    pattern = r'["\']([^"\']+)["\']\s*:\s*\{'
    
    matches = re.finditer(pattern, content)
    for match in matches:
        drug_name = match.group(1)
        # Try to extract the dictionary
        start_pos = match.end() - 1  # Position of {
        
        # Find matching closing brace
        brace_count = 0
        in_string = False
        string_char = None
        i = start_pos
        
        while i < len(content):
            char = content[i]
            
            if char in ['"', "'"] and (i == 0 or content[i-1] != '\\'):
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
                        # Found the end
                        dict_str = content[start_pos:i+1]
                        try:
                            # Try to eval just to get structure
                            # But we need to be careful
                            # Instead, let's just parse the structure manually
                            drugs[drug_name] = parse_dict_structure(dict_str)
                            break
                        except:
                            break
            i += 1
    
    return drugs

def parse_dict_structure(dict_str: str) -> Dict:
    """Parse dictionary structure từ string (simplified)"""
    # This is a simplified parser - just check for field names
    result = {}
    
    # Check for each field
    all_fields = CORE_FIELDS + EXTENDED_FIELDS + ENHANCED_FIELDS + META_FIELDS
    
    for field in all_fields:
        # Check if field exists in the dict string
        pattern = rf'["\']?{field}["\']?\s*:'
        if re.search(pattern, dict_str):
            result[field] = True  # Field exists
        else:
            result[field] = False  # Field missing
    
    return result

def load_all_drugs() -> Dict:
    """Load tất cả drugs từ các file module"""
    all_drugs = {}
    base_path = Path("drugs/drug_modules")
    
    # Find all Python files (except __init__.py and backups)
    for py_file in sorted(base_path.rglob("*.py")):
        if py_file.name == "__init__.py" or py_file.name.endswith(".backup"):
            continue
        
        # Extract drugs from file
        file_drugs = extract_drugs_from_file(py_file)
        all_drugs.update(file_drugs)
    
    return all_drugs

def check_drug_fields_simple(drug_name: str, field_presence: Dict) -> Dict:
    """Kiểm tra fields của một thuốc (simplified)"""
    result = {
        'drug_name': drug_name,
        'missing_core': [],
        'missing_extended': [],
        'missing_enhanced': [],
        'missing_meta': [],
        'total_missing': 0
    }
    
    for field in CORE_FIELDS:
        if not field_presence.get(field, False):
            result['missing_core'].append(field)
            result['total_missing'] += 1
    
    for field in EXTENDED_FIELDS:
        if not field_presence.get(field, False):
            result['missing_extended'].append(field)
    
    for field in ENHANCED_FIELDS:
        if not field_presence.get(field, False):
            result['missing_enhanced'].append(field)
    
    for field in META_FIELDS:
        if not field_presence.get(field, False):
            result['missing_meta'].append(field)
    
    return result

def main():
    """Main function - simplified version using file parsing"""
    print("\n" + "=" * 70)
    print("KIEM TRA THIEU FIELD TRONG TOAN BO THUOC")
    print("(Phuong phap: Doc truc tiep tu file module)")
    print("=" * 70)
    print()
    
    print("Dang doc cac file module...")
    
    # Load drugs bằng cách đọc file
    all_drugs = {}
    base_path = Path("drugs/drug_modules")
    
    drug_count = 0
    files_processed = 0
    
    for py_file in sorted(base_path.rglob("*.py")):
        if py_file.name == "__init__.py" or py_file.name.endswith(".backup"):
            continue
        
        files_processed += 1
        try:
            with open(py_file, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Tìm tất cả drug names trong file
            # Pattern: "DrugName": { ... }
            pattern = r'["\']([^"\']+)["\']\s*:\s*\{'
            matches = re.findall(pattern, content)
            
            for drug_name in matches:
                if drug_name not in all_drugs:
                    # Kiểm tra field presence
                    field_presence = {}
                    
                    for field in CORE_FIELDS + EXTENDED_FIELDS + ENHANCED_FIELDS + META_FIELDS:
                        # Check if field exists for this drug
                        # Pattern: drug_name dict, then field
                        drug_pattern = rf'["\']{re.escape(drug_name)}["\']\s*:\s*\{{[^}}]*["\']{re.escape(field)}["\']\s*:'
                        field_presence[field] = bool(re.search(drug_pattern, content, re.DOTALL))
                    
                    all_drugs[drug_name] = field_presence
                    drug_count += 1
        except Exception as e:
            print(f"  Loi khi doc {py_file.name}: {e}")
    
    print(f"Da doc {files_processed} files, tim thay {drug_count} thuoc")
    print()
    
    if not all_drugs:
        print("[LOI] Khong tim thay thuoc nao")
        return
    
    # Kiểm tra fields
    all_results = []
    drugs_with_missing_core = []
    drugs_with_missing_extended = []
    drugs_with_missing_enhanced = []
    
    field_missing_count = defaultdict(int)
    
    for drug_name, field_presence in all_drugs.items():
        result = check_drug_fields_simple(drug_name, field_presence)
        all_results.append(result)
        
        if result['missing_core']:
            drugs_with_missing_core.append(result)
            for field in result['missing_core']:
                field_missing_count[f"core_{field}"] += 1
        
        if result['missing_extended']:
            drugs_with_missing_extended.append(result)
            for field in result['missing_extended']:
                field_missing_count[f"extended_{field}"] += 1
        
        if result['missing_enhanced']:
            drugs_with_missing_enhanced.append(result)
            for field in result['missing_enhanced']:
                field_missing_count[f"enhanced_{field}"] += 1
    
    total_drugs = len(all_drugs)
    
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
    print("3. THIEU ENHANCED FIELDS (14 fields)")
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
        for field, drugs in sorted_fields[:15]:
            count = len(drugs)
            print(f"  - {field}: {count} thuoc thieu ({count*100//total_drugs if total_drugs > 0 else 0}%)")
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

if __name__ == "__main__":
    main()

