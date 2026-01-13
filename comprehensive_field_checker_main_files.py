"""
Script kiểm tra toàn diện tất cả field trong file chính (không phải backup)
Kiểm tra Core, Extended, Enhanced fields và các field khác
"""
import ast
import re
from pathlib import Path
from collections import defaultdict
from typing import Dict, Set, List

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

# Các field khác thường có
OTHER_COMMON_FIELDS = [
    "renal_adjustment",
    "contraindications_detail",
    "brand_names",
    "cost_estimate",
    "risk_flags",
    "guideline_tags"
]

ALL_FIELDS = CORE_FIELDS + EXTENDED_FIELDS + ENHANCED_FIELDS + OTHER_COMMON_FIELDS

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
                                
                                # Chỉ lấy thuốc thực sự (có group hoặc vietnamese_name)
                                is_field_name = (
                                    drug_name.islower() and 
                                    '_' in drug_name and 
                                    drug_name.count('_') >= 2 and
                                    drug_name not in ['iv', 'po', 'im', 'sc']
                                )
                                
                                if ('group' in value_keys or 'vietnamese_name' in value_keys) and not is_field_name:
                                    drugs[drug_name] = {
                                        'fields': value_keys,
                                        'file': None  # Sẽ được điền sau
                                    }
    
    return drugs

def check_drug_fields(drug_name: str, fields: Set[str]) -> Dict:
    """Kiểm tra fields của một thuốc"""
    result = {
        'drug_name': drug_name,
        'missing_core': [],
        'missing_extended': [],
        'missing_enhanced': [],
        'missing_other_common': [],
        'all_fields': list(fields),
        'duplicate_fields': []
    }
    
    # Kiểm tra core fields
    for field in CORE_FIELDS:
        if field not in fields:
            result['missing_core'].append(field)
    
    # Kiểm tra extended fields
    for field in EXTENDED_FIELDS:
        if field not in fields:
            result['missing_extended'].append(field)
    
    # Kiểm tra enhanced fields
    for field in ENHANCED_FIELDS:
        if field not in fields:
            result['missing_enhanced'].append(field)
    
    # Kiểm tra other common fields
    for field in OTHER_COMMON_FIELDS:
        if field not in fields:
            result['missing_other_common'].append(field)
    
    # Kiểm tra trùng lặp (nếu có field xuất hiện nhiều lần trong dict)
    field_counts = {}
    for field in fields:
        field_counts[field] = field_counts.get(field, 0) + 1
    
    result['duplicate_fields'] = [f for f, count in field_counts.items() if count > 1]
    
    return result

def load_all_drugs_from_main_files() -> Dict[str, Dict]:
    """Load tất cả drugs từ file chính (không phải backup)"""
    all_drugs = {}
    base_path = Path("drugs/drug_modules")
    
    files_processed = 0
    files_with_errors = []
    
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
                
                # Gán file cho mỗi drug
                for drug_name in file_drugs:
                    file_drugs[drug_name]['file'] = py_file
                
                all_drugs.update(file_drugs)
                files_processed += 1
                
            except SyntaxError as e:
                files_with_errors.append((py_file, str(e)))
                
        except Exception as e:
            files_with_errors.append((py_file, str(e)))
    
    print(f"  Đã xử lý {files_processed} files")
    if files_with_errors:
        print(f"  Cảnh báo: {len(files_with_errors)} files có lỗi:")
        for file, error in files_with_errors[:5]:
            print(f"    - {file.name}: {error[:100]}")
    
    return all_drugs

def main():
    """Main function"""
    print("\n" + "=" * 80)
    print("KIỂM TRA TOÀN DIỆN CÁC FIELD TRONG FILE CHÍNH")
    print("=" * 80)
    print()
    
    print("Đang đọc các file module chính (không phải backup)...")
    all_drugs = load_all_drugs_from_main_files()
    
    total_drugs = len(all_drugs)
    print(f"Tìm thấy {total_drugs} thuốc trong file chính")
    print()
    
    if not all_drugs:
        print("[LỖI] Không tìm thấy thuốc nào")
        return
    
    # Kiểm tra fields
    drugs_with_missing_core = []
    drugs_with_missing_extended = []
    drugs_with_missing_enhanced = []
    drugs_with_duplicates = []
    
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
        
        if result['duplicate_fields']:
            drugs_with_duplicates.append(result)
    
    # Xuất kết quả
    output_file = Path("comprehensive_fields_report.txt")
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write("=" * 80 + "\n")
        f.write("BÁO CÁO KIỂM TRA TOÀN DIỆN CÁC FIELD\n")
        f.write("=" * 80 + "\n\n")
        
        f.write(f"Tổng số thuốc kiểm tra: {total_drugs}\n")
        f.write(f"Thuốc thiếu Core fields: {len(drugs_with_missing_core)}\n")
        f.write(f"Thuốc thiếu Extended fields: {len(drugs_with_missing_extended)}\n")
        f.write(f"Thuốc thiếu Enhanced fields: {len(drugs_with_missing_enhanced)}\n")
        f.write(f"Thuốc có field trùng lặp: {len(drugs_with_duplicates)}\n")
        f.write("\n" + "=" * 80 + "\n\n")
        
        # Core fields
        if drugs_with_missing_core:
            f.write("1. THIẾU CORE FIELDS\n")
            f.write("=" * 80 + "\n\n")
            by_field = defaultdict(list)
            for result in drugs_with_missing_core:
                for field in result['missing_core']:
                    by_field[field].append(result)
            
            for field in CORE_FIELDS:
                if field in by_field:
                    f.write(f"{field.upper()} ({len(by_field[field])} thuốc):\n")
                    f.write("-" * 80 + "\n")
                    for r in by_field[field]:
                        f.write(f"  - {r['drug_name']}\n")
                        f.write(f"    File: {r['file']}\n")
                    f.write("\n")
        else:
            f.write("1. CORE FIELDS: ✅ Tất cả đầy đủ\n\n")
        
        # Extended fields
        if drugs_with_missing_extended:
            f.write("\n" + "=" * 80 + "\n")
            f.write("2. THIẾU EXTENDED FIELDS\n")
            f.write("=" * 80 + "\n\n")
            by_field = defaultdict(list)
            for result in drugs_with_missing_extended:
                for field in result['missing_extended']:
                    by_field[field].append(result)
            
            for field in EXTENDED_FIELDS:
                if field in by_field:
                    f.write(f"{field.upper()} ({len(by_field[field])} thuốc):\n")
                    f.write("-" * 80 + "\n")
                    for r in by_field[field][:20]:  # Chỉ hiển thị 20 đầu tiên
                        f.write(f"  - {r['drug_name']}\n")
                        f.write(f"    File: {r['file']}\n")
                    if len(by_field[field]) > 20:
                        f.write(f"    ... và {len(by_field[field]) - 20} thuốc khác\n")
                    f.write("\n")
        else:
            f.write("2. EXTENDED FIELDS: ✅ Tất cả đầy đủ\n\n")
        
        # Enhanced fields
        if drugs_with_missing_enhanced:
            f.write("\n" + "=" * 80 + "\n")
            f.write("3. THIẾU ENHANCED FIELDS\n")
            f.write("=" * 80 + "\n\n")
            by_field = defaultdict(list)
            for result in drugs_with_missing_enhanced:
                for field in result['missing_enhanced']:
                    by_field[field].append(result)
            
            # Sắp xếp theo số lượng thiếu
            sorted_fields = sorted(by_field.items(), key=lambda x: len(x[1]), reverse=True)
            
            for field, results in sorted_fields:
                f.write(f"{field.upper()} ({len(results)} thuốc):\n")
                f.write("-" * 80 + "\n")
                for r in results[:15]:  # Chỉ hiển thị 15 đầu tiên
                    f.write(f"  - {r['drug_name']}\n")
                    f.write(f"    File: {r['file']}\n")
                if len(results) > 15:
                    f.write(f"    ... và {len(results) - 15} thuốc khác\n")
                f.write("\n")
        else:
            f.write("3. ENHANCED FIELDS: ✅ Tất cả đầy đủ\n\n")
        
        # Duplicate fields
        if drugs_with_duplicates:
            f.write("\n" + "=" * 80 + "\n")
            f.write("4. FIELD TRÙNG LẶP\n")
            f.write("=" * 80 + "\n\n")
            for r in drugs_with_duplicates:
                f.write(f"  - {r['drug_name']}\n")
                f.write(f"    File: {r['file']}\n")
                f.write(f"    Field trùng: {', '.join(r['duplicate_fields'])}\n\n")
        else:
            f.write("4. FIELD TRÙNG LẶP: ✅ Không có\n\n")
    
    print(f"\nĐã lưu báo cáo vào: {output_file}")
    print(f"\nTổng kết:")
    print(f"  - Core fields: {len(drugs_with_missing_core)} thuốc thiếu")
    print(f"  - Extended fields: {len(drugs_with_missing_extended)} thuốc thiếu")
    print(f"  - Enhanced fields: {len(drugs_with_missing_enhanced)} thuốc thiếu")
    print(f"  - Field trùng lặp: {len(drugs_with_duplicates)} thuốc")
    
    return {
        'total_drugs': total_drugs,
        'missing_core': len(drugs_with_missing_core),
        'missing_extended': len(drugs_with_missing_extended),
        'missing_enhanced': len(drugs_with_missing_enhanced),
        'duplicates': len(drugs_with_duplicates),
        'details': {
            'missing_core': drugs_with_missing_core,
            'missing_extended': drugs_with_missing_extended,
            'missing_enhanced': drugs_with_missing_enhanced,
            'duplicates': drugs_with_duplicates
        }
    }

if __name__ == "__main__":
    main()
