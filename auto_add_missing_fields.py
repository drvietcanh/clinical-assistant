"""
Script tự động bổ sung field thiếu cho thuốc
Sử dụng FieldStandardizer để bổ sung field với template
"""
import sys
import json
import ast
import shutil
from pathlib import Path
from typing import Dict, List
from collections import defaultdict

# Import standardizer
sys.path.insert(0, str(Path.cwd()))
from drugs.field_standardizer import get_field_standardizer

def load_drug_from_file(file_path: str, drug_name: str) -> Dict:
    """Load một thuốc từ file"""
    try:
        # Import module và lấy drug
        module_path = file_path.replace('\\', '/').replace('.py', '').replace('drugs/', '')
        module_name = module_path.replace('/', '.')
        
        # Try to import
        module = __import__(module_name, fromlist=['*'])
        
        # Find _DRUGS variable
        for attr_name in dir(module):
            if attr_name.endswith('_DRUGS'):
                drugs_dict = getattr(module, attr_name)
                if isinstance(drugs_dict, dict) and drug_name in drugs_dict:
                    return drugs_dict[drug_name]
    except Exception as e:
        print(f"Error loading {drug_name} from {file_path}: {e}")
    
    return None

def update_drug_in_file(file_path: Path, drug_name: str, updated_drug_data: Dict, dry_run: bool = True) -> bool:
    """
    Cập nhật thuốc trong file
    
    Args:
        file_path: Đường dẫn file
        drug_name: Tên thuốc
        updated_drug_data: Dữ liệu thuốc đã cập nhật
        dry_run: Chỉ xem, không thay đổi file
    
    Returns:
        True nếu thành công
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Parse AST
        tree = ast.parse(content)
        
        # Tìm drug entry
        for node in ast.walk(tree):
            if isinstance(node, ast.Assign):
                for target in node.targets:
                    if isinstance(target, ast.Name) and target.id.endswith('_DRUGS'):
                        if isinstance(node.value, ast.Dict):
                            # Tìm drug trong dict
                            for i, (key_node, value_node) in enumerate(zip(node.value.keys, node.value.values)):
                                current_drug_name = None
                                if isinstance(key_node, ast.Constant):
                                    current_drug_name = key_node.value
                                elif hasattr(key_node, 's'):
                                    current_drug_name = key_node.s
                                
                                if current_drug_name == drug_name:
                                    # Tìm vị trí trong source
                                    lines = content.split('\n')
                                    drug_start_line = key_node.lineno - 1
                                    
                                    # Tìm kết thúc
                                    indent = len(lines[drug_start_line]) - len(lines[drug_start_line].lstrip())
                                    brace_count = 0
                                    drug_end_line = drug_start_line
                                    
                                    for j in range(drug_start_line, len(lines)):
                                        line = lines[j]
                                        brace_count += line.count('{') - line.count('}')
                                        if brace_count == 0 and j > drug_start_line:
                                            current_indent = len(line) - len(line.lstrip()) if line.strip() else indent
                                            if current_indent <= indent:
                                                drug_end_line = j
                                                break
                                    
                                    # Format updated drug
                                    from split_obstetrics_gynecology_safe import format_drug_dict
                                    updated_code = format_drug_dict(updated_drug_data, indent_level=4)
                                    indented_code = '\n'.join('    ' + line if line.strip() else line 
                                                            for line in updated_code.split('\n'))
                                    
                                    # Replace
                                    if not dry_run:
                                        new_lines = (
                                            lines[:drug_start_line] +
                                            [f'    "{drug_name}": {indented_code},'] +
                                            lines[drug_end_line+1:]
                                        )
                                        
                                        # Backup
                                        backup_file = file_path.with_suffix('.py.backup')
                                        if not backup_file.exists():
                                            shutil.copy2(file_path, backup_file)
                                        
                                        # Write
                                        with open(file_path, 'w', encoding='utf-8') as f:
                                            f.write('\n'.join(new_lines))
                                        
                                        return True
                                    else:
                                        print(f"  [DRY RUN] Would update {drug_name} in {file_path}")
                                        return True
    except Exception as e:
        print(f"Error updating {drug_name} in {file_path}: {e}")
        import traceback
        traceback.print_exc()
    
    return False

def main():
    """Hàm chính"""
    import io
    if sys.platform == 'win32':
        sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')
    
    print("="*60)
    print("KIEM TRA THUOC CAN THEM FIELD")
    print("="*60)
    
    # Đọc báo cáo
    with open('drugs_need_fields_report.json', 'r', encoding='utf-8') as f:
        report = json.load(f)
    
    standardizer = get_field_standardizer()
    
    # Phân loại
    drugs_missing_standard = report['drugs_missing_standard_fields']
    
    print(f"\nTim thay {len(drugs_missing_standard)} thuoc thieu field chuan")
    print(f"\nTop 10 thuoc thieu nhieu field nhat:")
    for i, drug in enumerate(drugs_missing_standard[:10], 1):
        print(f"{i}. {drug['name']}: thieu {drug['missing_count']} field")
        print(f"   - Field chuan: {len(drug['missing_standard'])}")
        print(f"   - Field bo sung: {len(drug['missing_additional'])}")
        print(f"   - File: {drug['file']}")
    
    # Thống kê field thiếu
    print(f"\nThong ke field chuan thieu nhieu nhat:")
    field_count = defaultdict(int)
    for drug in drugs_missing_standard:
        for field in drug['missing_standard']:
            field_count[field] += 1
    
    for field, count in sorted(field_count.items(), key=lambda x: x[1], reverse=True)[:10]:
        print(f"  - {field}: {count} thuoc")
    
    print(f"\n" + "="*60)
    print("KET LUAN")
    print("="*60)
    print(f"Co {len(drugs_missing_standard)} thuoc CAN BO SUNG field chuan ngay")
    print(f"Co {len(report['drugs_missing_additional_only'])} thuoc chi thieu field bo sung (uu tien thap hon)")
    print(f"\nSu dung FieldStandardizer de tu dong bo sung field voi template:")
    print(f"  from drugs.field_standardizer import get_field_standardizer")
    print(f"  standardizer = get_field_standardizer()")
    print(f"  standardized = standardizer.add_missing_fields(drug_data, include_additional=False)")
    print("="*60)

if __name__ == "__main__":
    main()
