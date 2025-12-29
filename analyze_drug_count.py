"""
Phân tích chi tiết số lượng thuốc thực sự
Tách biệt thuốc thực sự và các entries không phải thuốc
"""
import ast
import re
from pathlib import Path
from collections import defaultdict
from typing import Dict, Set, List, Tuple

# Danh sách các giá trị KHÔNG phải thuốc (field names, giá trị đặc biệt)
NON_DRUG_ENTRIES = {
    # Field names
    'risk_flags', 'organ_toxicity', 'pediatric_dosing', 'geriatric_dosing',
    'brand_names', 'cost_estimate', 'contraindications_detail',
    'reversal_agents', 'dosage', 'renal_adjustment', 'pharmacokinetics',
    'drug_interactions', 'references', 'pregnancy_lactation',
    'hepatic_adjustment', 'overdose_management', 'administration_instructions',
    'contraindications', 'side_effects', 'interactions', 'pregnancy',
    'administration', 'indications', 'group', 'vietnamese_name',
    # Giá trị đặc biệt
    'oral', 'im', 'sc', 'inhaled', 'inhalation', 'iv', 'po',
    'normal', '30_60', 'under_30', 'mild', 'moderate', 'severe',
    'major', 'minor', 'tuyệt_đối', 'tương_đối',
}

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

def is_likely_drug(drug_name: str, value_keys: Set[str]) -> Tuple[bool, str]:
    """
    Kiểm tra xem entry có phải là thuốc thực sự không
    Trả về (is_drug, reason)
    """
    # 1. Kiểm tra nếu là field name đã biết
    if drug_name in NON_DRUG_ENTRIES:
        return False, f"Field name đã biết: {drug_name}"
    
    # 2. Kiểm tra pattern field name (lowercase với nhiều dấu gạch dưới)
    is_field_name_pattern = (
        drug_name.islower() and 
        '_' in drug_name and 
        drug_name.count('_') >= 2 and
        drug_name not in ['iv', 'po', 'im', 'sc', 'iv_bolus', 'iv_infusion']
    )
    
    if is_field_name_pattern:
        # Nhưng nếu có 'group' hoặc 'vietnamese_name', vẫn có thể là thuốc
        if 'group' not in value_keys and 'vietnamese_name' not in value_keys:
            return False, f"Pattern field name (lowercase với nhiều _): {drug_name}"
    
    # 3. Kiểm tra có field bắt buộc của thuốc
    has_group = 'group' in value_keys
    has_vietnamese_name = 'vietnamese_name' in value_keys
    has_administration = 'administration' in value_keys
    has_indications = 'indications' in value_keys
    has_dosage = 'dosage' in value_keys
    
    # Thuốc thực sự phải có ít nhất 2 trong các field: group, vietnamese_name, administration, indications
    required_fields_count = sum([has_group, has_vietnamese_name, has_administration, has_indications])
    
    if required_fields_count < 2:
        return False, f"Thiếu field bắt buộc (chỉ có {required_fields_count}/4 field: group, vietnamese_name, administration, indications)"
    
    # 4. Kiểm tra nếu chỉ có các field không phải của thuốc
    drug_specific_fields = {'group', 'vietnamese_name', 'administration', 'indications', 'dosage', 
                           'side_effects', 'contraindications', 'interactions', 'pregnancy',
                           'mechanism_of_action', 'monitoring', 'precautions', 'pharmacokinetics',
                           'storage', 'black_box_warnings', 'drug_interactions', 'pregnancy_lactation',
                           'hepatic_adjustment', 'overdose_management', 'reversal_agents',
                           'administration_instructions', 'references'}
    
    has_drug_fields = bool(value_keys & drug_specific_fields)
    if not has_drug_fields:
        return False, f"Không có field đặc trưng của thuốc"
    
    # 5. Nếu có 'group' hoặc 'vietnamese_name', chắc chắn là thuốc
    if has_group or has_vietnamese_name:
        return True, "Có group hoặc vietnamese_name"
    
    # 6. Nếu có administration và indications, có thể là thuốc
    if has_administration and has_indications:
        return True, "Có administration và indications"
    
    return False, "Không đủ tiêu chí"

def analyze_all_drugs() -> Dict[str, List]:
    """Phân tích tất cả entries và phân loại"""
    base_path = Path("drugs/drug_modules")
    
    all_entries = []
    real_drugs = []
    non_drugs = []
    
    files_processed = 0
    
    for py_file in sorted(base_path.rglob("*.py")):
        if py_file.name == "__init__.py" or py_file.name.endswith(".backup"):
            continue
        
        try:
            with open(py_file, 'r', encoding='utf-8') as f:
                content = f.read()
            
            try:
                tree = ast.parse(content)
                
                # Find all assignments to _DRUGS variables
                for node in ast.walk(tree):
                    if isinstance(node, ast.Assign):
                        for target in node.targets:
                            if isinstance(target, ast.Name) and target.id.endswith('_DRUGS'):
                                if isinstance(node.value, ast.Dict):
                                    # This is a drug dictionary
                                    for key_node, value_node in zip(node.value.keys, node.value.values):
                                        drug_name = get_string_value(key_node)
                                        
                                        if drug_name and isinstance(value_node, ast.Dict):
                                            value_keys = extract_dict_keys(value_node)
                                            
                                            is_drug, reason = is_likely_drug(drug_name, value_keys)
                                            
                                            entry_info = {
                                                'name': drug_name,
                                                'file': py_file.relative_to(base_path),
                                                'has_group': 'group' in value_keys,
                                                'has_vietnamese_name': 'vietnamese_name' in value_keys,
                                                'has_administration': 'administration' in value_keys,
                                                'has_indications': 'indications' in value_keys,
                                                'has_dosage': 'dosage' in value_keys,
                                                'field_count': len(value_keys),
                                                'reason': reason
                                            }
                                            
                                            all_entries.append(entry_info)
                                            
                                            if is_drug:
                                                real_drugs.append(entry_info)
                                            else:
                                                non_drugs.append(entry_info)
                
                files_processed += 1
                
            except SyntaxError:
                pass
                
        except Exception:
            pass
    
    print(f"Da xu ly {files_processed} files")
    
    return {
        'all': all_entries,
        'real_drugs': real_drugs,
        'non_drugs': non_drugs
    }

def main():
    """Main function"""
    print("\n" + "=" * 70)
    print("PHAN TICH CHI TIET SO LUONG THUOC THUC SU")
    print("=" * 70)
    print()
    
    print("Dang phan tich tat ca entries...")
    results = analyze_all_drugs()
    
    all_entries = results['all']
    real_drugs = results['real_drugs']
    non_drugs = results['non_drugs']
    
    print(f"\nTổng số entries tìm thấy: {len(all_entries)}")
    print(f"  - Thuốc thực sự: {len(real_drugs)}")
    print(f"  - Không phải thuốc: {len(non_drugs)}")
    print()
    
    # Phân tích các entries không phải thuốc
    print("=" * 70)
    print("PHAN TICH CAC ENTRIES KHONG PHAI THUOC")
    print("=" * 70)
    
    by_reason = defaultdict(list)
    for entry in non_drugs:
        by_reason[entry['reason']].append(entry['name'])
    
    print(f"\nPhân loại theo lý do:")
    for reason, names in sorted(by_reason.items(), key=lambda x: len(x[1]), reverse=True):
        print(f"\n  {reason}: {len(names)} entries")
        if len(names) <= 10:
            for name in names:
                print(f"    - {name}")
        else:
            for name in names[:10]:
                print(f"    - {name}")
            print(f"    ... và {len(names) - 10} entries khác")
    
    # Phân tích thuốc thực sự
    print("\n" + "=" * 70)
    print("PHAN TICH THUOC THUC SU")
    print("=" * 70)
    
    print(f"\nTổng số thuốc thực sự: {len(real_drugs)}")
    
    # Thống kê field
    has_group_count = sum(1 for d in real_drugs if d['has_group'])
    has_vietnamese_name_count = sum(1 for d in real_drugs if d['has_vietnamese_name'])
    has_administration_count = sum(1 for d in real_drugs if d['has_administration'])
    has_indications_count = sum(1 for d in real_drugs if d['has_indications'])
    has_dosage_count = sum(1 for d in real_drugs if d['has_dosage'])
    
    print(f"\nThống kê field:")
    print(f"  - Có 'group': {has_group_count} ({has_group_count*100//len(real_drugs) if real_drugs else 0}%)")
    print(f"  - Có 'vietnamese_name': {has_vietnamese_name_count} ({has_vietnamese_name_count*100//len(real_drugs) if real_drugs else 0}%)")
    print(f"  - Có 'administration': {has_administration_count} ({has_administration_count*100//len(real_drugs) if real_drugs else 0}%)")
    print(f"  - Có 'indications': {has_indications_count} ({has_indications_count*100//len(real_drugs) if real_drugs else 0}%)")
    print(f"  - Có 'dosage': {has_dosage_count} ({has_dosage_count*100//len(real_drugs) if real_drugs else 0}%)")
    
    # Phân tích theo file
    print("\n" + "=" * 70)
    print("PHAN BO THEO FILE")
    print("=" * 70)
    
    by_file = defaultdict(list)
    for drug in real_drugs:
        by_file[str(drug['file'])].append(drug['name'])
    
    print(f"\nSố lượng thuốc theo file (top 20):")
    sorted_files = sorted(by_file.items(), key=lambda x: len(x[1]), reverse=True)
    for file_path, drugs in sorted_files[:20]:
        print(f"  {file_path}: {len(drugs)} thuốc")
    
    # Lưu danh sách thuốc
    print("\n" + "=" * 70)
    print("LUU DANH SACH")
    print("=" * 70)
    
    # Lưu danh sách thuốc thực sự
    with open("real_drugs_list.txt", 'w', encoding='utf-8') as f:
        f.write(f"# DANH SACH THUOC THUC SU\n")
        f.write(f"# Tổng số: {len(real_drugs)}\n")
        f.write(f"# Ngày tạo: 2025-02-18\n\n")
        for drug in sorted(real_drugs, key=lambda x: x['name']):
            f.write(f"{drug['name']}\n")
    
    # Lưu danh sách không phải thuốc
    with open("non_drugs_list.txt", 'w', encoding='utf-8') as f:
        f.write(f"# DANH SACH ENTRIES KHONG PHAI THUOC\n")
        f.write(f"# Tổng số: {len(non_drugs)}\n")
        f.write(f"# Ngày tạo: 2025-02-18\n\n")
        for entry in sorted(non_drugs, key=lambda x: x['name']):
            f.write(f"{entry['name']} - {entry['reason']}\n")
    
    print(f"\nĐã lưu:")
    print(f"  - real_drugs_list.txt: {len(real_drugs)} thuốc")
    print(f"  - non_drugs_list.txt: {len(non_drugs)} entries")
    
    print("\n" + "=" * 70)

if __name__ == "__main__":
    main()

