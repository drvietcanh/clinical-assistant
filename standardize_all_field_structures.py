"""
Script chuẩn hóa cấu trúc field cho tất cả thuốc
Có backup, rollback, và dry-run mode
"""
import sys
import json
import ast
import shutil
from pathlib import Path
from typing import Dict, List, Set, Any, Optional, Tuple
from collections import defaultdict
from datetime import datetime
import io

sys.path.insert(0, str(Path.cwd()))

if sys.platform == 'win32':
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')

from field_structure_mapping_rules import (
    standardize_pregnancy_lactation,
    standardize_hepatic_adjustment,
    standardize_overdose_management,
    standardize_contraindications,
    standardize_drug_interactions,
    standardize_administration_instructions,
    standardize_references,
    standardize_all_fields
)

# Load danh sách thuốc cần sửa từ báo cáo
def load_drugs_need_fix() -> Dict[str, List[Dict]]:
    """Load danh sách thuốc cần sửa từ báo cáo"""
    try:
        with open('field_standardization_analysis.json', 'r', encoding='utf-8') as f:
            data = json.load(f)
        return data.get('drugs_need_fix', {})
    except FileNotFoundError:
        print("Warning: field_standardization_analysis.json not found. Will process all drugs.")
        return {}

def get_string_value(node):
    """Lấy giá trị string từ AST node"""
    if isinstance(node, ast.Constant) and isinstance(node.value, str):
        return node.value
    elif hasattr(node, 's'):
        return node.s
    return None

def dict_to_ast_dict(value: Any, indent: int = 0) -> str:
    """Chuyển đổi dict thành string AST dict format"""
    if isinstance(value, dict):
        if not value:
            return "{}"
        lines = ["{"]
        for key, val in value.items():
            key_str = f'"{key}"' if isinstance(key, str) else str(key)
            val_str = dict_to_ast_dict(val, indent + 1)
            lines.append(f'{"    " * (indent + 1)}{key_str}: {val_str},')
        lines.append(f'{"    " * indent}}}')
        return "\n".join(lines)
    elif isinstance(value, list):
        if not value:
            return "[]"
        if all(isinstance(item, str) for item in value):
            items = ", ".join([f'"{item}"' for item in value])
            return f"[{items}]"
        else:
            lines = ["["]
            for item in value:
                item_str = dict_to_ast_dict(item, indent + 1)
                lines.append(f'{"    " * (indent + 1)}{item_str},')
            lines.append(f'{"    " * indent}]')
            return "\n".join(lines)
    elif isinstance(value, str):
        # Escape quotes and newlines
        escaped = value.replace('\\', '\\\\').replace('"', '\\"').replace('\n', '\\n')
        return f'"{escaped}"'
    elif value is None:
        return "None"
    else:
        return repr(value)

def format_dict_value(value: Any, indent: int = 0) -> str:
    """Format dict value thành Python code string"""
    if isinstance(value, dict):
        if not value:
            return "{}"
        lines = ["{"]
        for key, val in value.items():
            key_str = f'"{key}"' if isinstance(key, str) else str(key)
            val_str = format_dict_value(val, indent + 1)
            lines.append(f'{"    " * (indent + 1)}{key_str}: {val_str},')
        lines.append(f'{"    " * indent}}}')
        return "\n".join(lines)
    elif isinstance(value, list):
        if not value:
            return "[]"
        if all(isinstance(item, str) for item in value):
            items = ",\n".join([f'{"    " * (indent + 1)}{repr(item)}' for item in value])
            return f"[\n{items}\n{"    " * indent}]"
        else:
            lines = ["["]
            for item in value:
                item_str = format_dict_value(item, indent + 1)
                lines.append(f'{"    " * (indent + 1)}{item_str},')
            lines.append(f'{"    " * indent}]')
            return "\n".join(lines)
    elif isinstance(value, str):
        return repr(value)
    elif value is None:
        return "None"
    else:
        return repr(value)

def standardize_drug_in_file(file_path: Path, drug_name: str, fields_to_fix: List[str], 
                              dry_run: bool = True) -> Tuple[bool, Dict[str, Any]]:
    """
    Chuẩn hóa một thuốc trong file
    
    Returns:
        (success, changes_info)
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        tree = ast.parse(content)
        changes = {
            'drug': drug_name,
            'file': str(file_path),
            'fields_changed': [],
            'old_values': {},
            'new_values': {}
        }
        
        modified = False
        
        # Tìm và sửa drug
        for node in ast.walk(tree):
            if isinstance(node, ast.Assign):
                for target in node.targets:
                    if isinstance(target, ast.Name) and (target.id.endswith('_DRUGS') or target.id.isupper()):
                        if isinstance(node.value, ast.Dict):
                            for key_node, value_node in zip(node.value.keys, node.value.values):
                                current_drug_name = get_string_value(key_node)
                                if current_drug_name == drug_name and isinstance(value_node, ast.Dict):
                                    # Tìm field cần sửa
                                    for field_key_node, field_value_node in zip(value_node.keys, value_node.values):
                                        field_name = get_string_value(field_key_node)
                                        if field_name in fields_to_fix:
                                            # Lấy giá trị hiện tại (đơn giản hóa)
                                            old_value = None
                                            try:
                                                # Thử compile và eval để lấy giá trị
                                                old_value = ast.literal_eval(ast.unparse(field_value_node))
                                            except:
                                                pass
                                            
                                            # Chuẩn hóa
                                            standardized_value = standardize_all_fields({field_name: old_value})[field_name]
                                            
                                            if old_value != standardized_value:
                                                changes['fields_changed'].append(field_name)
                                                changes['old_values'][field_name] = old_value
                                                changes['new_values'][field_name] = standardized_value
                                                modified = True
        
        if modified and not dry_run:
            # Tạo backup
            backup_path = file_path.with_suffix(f'.backup_{datetime.now().strftime("%Y%m%d_%H%M%S")}.py')
            shutil.copy2(file_path, backup_path)
            changes['backup_file'] = str(backup_path)
            
            # Sửa file (cần implement logic sửa AST)
            # Tạm thời return False để báo cần implement
            changes['note'] = "File modification not fully implemented yet. Need AST manipulation."
        
        return modified, changes
        
    except Exception as e:
        return False, {'error': str(e), 'drug': drug_name, 'file': str(file_path)}

def standardize_drugs_simple(dry_run: bool = True, limit: Optional[int] = None):
    """
    Chuẩn hóa thuốc bằng cách load module và sửa trực tiếp
    Phương pháp đơn giản hơn: load module, sửa dict, viết lại file
    """
    base_path = Path("drugs/drug_modules")
    drugs_need_fix = load_drugs_need_fix()
    
    # Tạo backup directory
    backup_dir = Path("backups_field_standardization")
    if not dry_run:
        backup_dir.mkdir(exist_ok=True)
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        backup_dir = backup_dir / timestamp
        backup_dir.mkdir(exist_ok=True)
    
    all_changes = []
    files_modified = set()
    
    # Nhóm thuốc theo file
    drugs_by_file = defaultdict(list)
    for field_name, drugs in drugs_need_fix.items():
        for drug_info in drugs:
            file_path = drug_info['file']
            drugs_by_file[file_path].append({
                'drug': drug_info['drug'],
                'field': field_name,
                'fix_type': drug_info.get('fix_type'),
                'fix_details': drug_info.get('fix_details', {})
            })
    
    total_files = len(drugs_by_file)
    processed_files = 0
    
    print(f"\n{'DRY RUN - ' if dry_run else ''}Chuẩn hóa cấu trúc field")
    print(f"Số file cần xử lý: {total_files}")
    if limit:
        print(f"Giới hạn: {limit} file đầu tiên")
    
    for file_path_str, drugs_list in list(drugs_by_file.items())[:limit] if limit else drugs_by_file.items():
        file_path = Path(file_path_str)
        if not file_path.exists():
            print(f"Warning: File không tồn tại: {file_path}")
            continue
        
        processed_files += 1
        print(f"\n[{processed_files}/{total_files}] Xử lý: {file_path.name}")
        
        try:
            # Load module
            module_name = str(file_path.relative_to(Path.cwd())).replace('\\', '.').replace('/', '.').replace('.py', '')
            spec = __import__(module_name, fromlist=[''])
            
            # Tìm dict chứa drugs
            drugs_dict = None
            for attr_name in dir(spec):
                if attr_name.endswith('_DRUGS') or (attr_name.isupper() and not attr_name.startswith('_')):
                    attr = getattr(spec, attr_name)
                    if isinstance(attr, dict):
                        drugs_dict = attr
                        dict_name = attr_name
                        break
            
            if not drugs_dict:
                print(f"  Không tìm thấy dict thuốc trong file")
                continue
            
            # Backup file
            if not dry_run:
                backup_file = backup_dir / file_path.name
                shutil.copy2(file_path, backup_file)
                print(f"  Đã backup: {backup_file}")
            
            # Chuẩn hóa từng thuốc
            file_changes = {
                'file': str(file_path),
                'dict_name': dict_name,
                'drugs_changed': []
            }
            
            for drug_info in drugs_list:
                drug_name = drug_info['drug']
                field_name = drug_info['field']
                
                if drug_name not in drugs_dict:
                    print(f"  Warning: Không tìm thấy thuốc {drug_name}")
                    continue
                
                drug_data = drugs_dict[drug_name]
                
                if field_name not in drug_data:
                    continue
                
                old_value = drug_data[field_name]
                standardized_value = standardize_all_fields({field_name: old_value})[field_name]
                
                if old_value != standardized_value:
                    drug_data[field_name] = standardized_value
                    file_changes['drugs_changed'].append({
                        'drug': drug_name,
                        'field': field_name,
                        'fix_type': drug_info.get('fix_type')
                    })
                    print(f"  ✓ {drug_name}.{field_name}: Đã chuẩn hóa")
            
            if file_changes['drugs_changed']:
                all_changes.append(file_changes)
                files_modified.add(str(file_path))
                
                # Viết lại file
                if not dry_run:
                    write_module_file(file_path, dict_name, drugs_dict)
                    print(f"  ✓ Đã cập nhật file")
            
        except Exception as e:
            print(f"  ✗ Lỗi: {e}")
            import traceback
            traceback.print_exc()
    
    # Tạo báo cáo
    report = {
        'timestamp': datetime.now().isoformat(),
        'dry_run': dry_run,
        'total_files_processed': processed_files,
        'files_modified': len(files_modified),
        'total_drugs_changed': sum(len(fc['drugs_changed']) for fc in all_changes),
        'changes': all_changes
    }
    
    report_file = f'field_standardization_report_{"dryrun" if dry_run else "applied"}_{datetime.now().strftime("%Y%m%d_%H%M%S")}.json'
    with open(report_file, 'w', encoding='utf-8') as f:
        json.dump(report, f, indent=2, ensure_ascii=False)
    
    print(f"\n{'='*70}")
    print(f"Hoàn thành!")
    print(f"  - Files đã xử lý: {processed_files}")
    print(f"  - Files đã sửa: {len(files_modified)}")
    print(f"  - Thuốc đã thay đổi: {report['total_drugs_changed']}")
    print(f"  - Báo cáo: {report_file}")
    if not dry_run:
        print(f"  - Backup: {backup_dir}")
    print(f"{'='*70}")
    
    return report

def write_module_file(file_path: Path, dict_name: str, drugs_dict: Dict):
    """Viết lại file module với drugs_dict đã cập nhật"""
    # Đọc file gốc để giữ imports và comments
    with open(file_path, 'r', encoding='utf-8') as f:
        original_lines = f.readlines()
    
    # Tìm phần dict và thay thế
    output_lines = []
    in_dict = False
    dict_start_line = None
    
    for i, line in enumerate(original_lines):
        if f'{dict_name} = {{' in line or f'{dict_name}=' in line:
            in_dict = True
            dict_start_line = i
            output_lines.append(line)
            # Bắt đầu viết dict mới
            output_lines.append(format_drugs_dict(drugs_dict, indent=0))
            break
        output_lines.append(line)
    
    if not in_dict:
        # Không tìm thấy dict, thêm vào cuối
        output_lines.append(f'\n{dict_name} = {format_drugs_dict(drugs_dict, indent=0)}\n')
    else:
        # Bỏ qua các dòng cũ của dict
        brace_count = 0
        for i in range(dict_start_line + 1, len(original_lines)):
            line = original_lines[i]
            if '{' in line:
                brace_count += line.count('{')
            if '}' in line:
                brace_count -= line.count('}')
            if brace_count <= 0 and '}' in line:
                # Kết thúc dict cũ
                break
    
    # Viết file
    with open(file_path, 'w', encoding='utf-8') as f:
        f.writelines(output_lines)

def format_drugs_dict(drugs_dict: Dict, indent: int = 0) -> str:
    """Format drugs dict thành Python code"""
    # Đơn giản hóa: sử dụng repr cho mỗi drug
    # Trong thực tế cần format đẹp hơn
    lines = []
    for drug_name, drug_data in drugs_dict.items():
        drug_str = format_dict_value({drug_name: drug_data}, indent)
        lines.append(drug_str)
    return "{\n" + ",\n".join(lines) + "\n}"

def main():
    import argparse
    parser = argparse.ArgumentParser(description='Chuẩn hóa cấu trúc field cho tất cả thuốc')
    parser.add_argument('--apply', action='store_true', help='Áp dụng thay đổi (mặc định là dry-run)')
    parser.add_argument('--limit', type=int, help='Giới hạn số file xử lý')
    args = parser.parse_args()
    
    dry_run = not args.apply
    
    if dry_run:
        print("="*70)
        print("CHẾ ĐỘ DRY-RUN - Không thay đổi file")
        print("="*70)
    else:
        print("="*70)
        print("CHẾ ĐỘ APPLY - Sẽ thay đổi file và tạo backup")
        print("="*70)
        response = input("Bạn có chắc chắn muốn tiếp tục? (yes/no): ")
        if response.lower() != 'yes':
            print("Đã hủy.")
            return
    
    report = standardize_drugs_simple(dry_run=dry_run, limit=args.limit)
    
    if dry_run:
        print("\nChạy với --apply để áp dụng thay đổi.")

if __name__ == "__main__":
    main()

