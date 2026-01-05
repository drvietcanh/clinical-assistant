"""
Script hỗ trợ bổ sung field cho thuốc
- Load thuốc từ file
- Bổ sung field với template
- Preview và apply
- Backup và rollback
"""
import sys
import json
import ast
import shutil
import re
from pathlib import Path
from typing import Dict, List, Optional, Any, Tuple
import io

# Setup path
sys.path.insert(0, str(Path.cwd()))

from drugs.field_standardizer import get_field_standardizer
from drugs.field_validator import get_field_validator, STANDARD_14_FIELDS, ADDITIONAL_8_FIELDS

# Setup encoding for Windows
if sys.platform == 'win32':
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')

def format_drug_dict(drug_data: Dict, indent_level: int = 4) -> str:
    """
    Format drug dict thành string Python code
    
    Args:
        drug_data: Dict chứa dữ liệu thuốc
        indent_level: Số spaces indent
    
    Returns:
        String Python code
    """
    indent = ' ' * indent_level
    lines = ['{']
    
    for key, value in drug_data.items():
        key_str = json.dumps(key, ensure_ascii=False)
        
        if isinstance(value, dict):
            value_str = format_drug_dict(value, indent_level + 4)
            lines.append(f'{indent}{key_str}: {value_str},')
        elif isinstance(value, list):
            if value and isinstance(value[0], dict):
                # List of dicts
                items = []
                for item in value:
                    items.append(format_drug_dict(item, indent_level + 8))
                value_str = '[\n' + ',\n'.join(items) + f'\n{indent}    ]'
            else:
                # Simple list
                value_str = json.dumps(value, ensure_ascii=False, indent=indent + '    ')
            lines.append(f'{indent}{key_str}: {value_str},')
        elif isinstance(value, str):
            # Multi-line string handling
            if '\n' in value or len(value) > 100:
                # Use triple quotes for long strings
                escaped = value.replace('"""', '\\"\\"\\"')
                lines.append(f'{indent}{key_str}: """{escaped}""",')
            else:
                value_str = json.dumps(value, ensure_ascii=False)
                lines.append(f'{indent}{key_str}: {value_str},')
        elif isinstance(value, tuple):
            # Convert tuple to string representation
            if all(isinstance(item, str) for item in value):
                # String tuple - use parentheses
                items = ', '.join(json.dumps(item, ensure_ascii=False) for item in value)
                lines.append(f'{indent}{key_str}: ({items}),')
            else:
                value_str = json.dumps(list(value), ensure_ascii=False)
                lines.append(f'{indent}{key_str}: {value_str},')
        elif value is None:
            lines.append(f'{indent}{key_str}: None,')
        elif isinstance(value, bool):
            lines.append(f'{indent}{key_str}: {str(value)},')
        else:
            # Use Python literal representation for numbers
            if isinstance(value, (int, float)):
                lines.append(f'{indent}{key_str}: {value},')
            else:
                value_str = json.dumps(value, ensure_ascii=False)
                lines.append(f'{indent}{key_str}: {value_str},')
    
    lines.append(' ' * (indent_level - 4) + '}')
    return '\n'.join(lines)

def load_drug_from_file(file_path: Path, drug_name: str) -> Optional[Dict]:
    """
    Load một thuốc từ file bằng cách import module
    
    Args:
        file_path: Đường dẫn file
        drug_name: Tên thuốc
    
    Returns:
        Dict chứa dữ liệu thuốc hoặc None
    """
    try:
        # Convert to module path - handle both relative and absolute paths
        file_str = str(file_path).replace('\\', '/')
        
        # Remove .py extension
        if file_str.endswith('.py'):
            file_str = file_str[:-3]
        
        # Convert to module path
        if file_str.startswith('drugs/'):
            module_path = file_str.replace('/', '.')
        elif 'drugs/' in file_str:
            # Extract part after drugs/
            idx = file_str.find('drugs/')
            module_path = file_str[idx:].replace('/', '.')
        else:
            # Assume it's relative to drugs/
            module_path = 'drugs.' + file_str.replace('/', '.')
        
        # Import module
        module = __import__(module_path, fromlist=['*'])
        
        # Find _DRUGS variable or similar patterns
        for attr_name in dir(module):
            # Try _DRUGS pattern first
            if attr_name.endswith('_DRUGS'):
                drugs_dict = getattr(module, attr_name)
                if isinstance(drugs_dict, dict) and drug_name in drugs_dict:
                    return drugs_dict[drug_name].copy()
            # Try other patterns (e.g., LOCAL_ANESTHETICS, MIGRAINE_TRIPTANS)
            elif attr_name.isupper() and not attr_name.startswith('_'):
                drugs_dict = getattr(module, attr_name)
                if isinstance(drugs_dict, dict) and drug_name in drugs_dict:
                    return drugs_dict[drug_name].copy()
    except Exception as e:
        print(f"Error loading {drug_name} from {file_path}: {e}")
        import traceback
        traceback.print_exc()
    
    return None

def find_drug_in_file(file_path: Path, drug_name: str) -> Optional[Tuple[int, int]]:
    """
    Tìm vị trí của thuốc trong file
    
    Returns:
        (start_line, end_line) hoặc None
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            lines = f.readlines()
        
        # Tìm dòng chứa drug name
        for i, line in enumerate(lines):
            # Tìm pattern: "Drug Name": {
            pattern = rf'["\']{re.escape(drug_name)}["\']\s*:'
            if re.search(pattern, line):
                start_line = i
                
                # Tìm kết thúc của dict
                indent = len(line) - len(line.lstrip())
                brace_count = 0
                in_string = False
                string_char = None
                
                for j in range(i, len(lines)):
                    current_line = lines[j]
                    current_indent = len(current_line) - len(current_line.lstrip()) if current_line.strip() else indent
                    
                    # Count braces (skip in strings)
                    for char in current_line:
                        if char in ('"', "'") and (j == i or lines[j-1][-2:] != '\\'):
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
                    
                    # Check if we've closed all braces and moved to next item
                    if brace_count == 0 and j > i:
                        # Check if next non-empty line is at same or less indent
                        for k in range(j + 1, len(lines)):
                            if lines[k].strip():
                                next_indent = len(lines[k]) - len(lines[k].lstrip())
                                if next_indent <= indent:
                                    return (start_line, k - 1)
                                break
                        return (start_line, j)
                
                return (start_line, len(lines) - 1)
    except Exception as e:
        print(f"Error finding drug in file: {e}")
    
    return None

def update_drug_in_file(file_path: Path, drug_name: str, updated_drug_data: Dict, 
                        dry_run: bool = True) -> bool:
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
            lines = content.split('\n')
        
        # Tìm vị trí thuốc
        position = find_drug_in_file(file_path, drug_name)
        if not position:
            print(f"  Khong tim thay {drug_name} trong file")
            return False
        
        start_line, end_line = position
        
        # Format updated drug
        drug_code = format_drug_dict(updated_drug_data, indent_level=4)
        # Indent to proper level
        indent = len(lines[start_line]) - len(lines[start_line].lstrip())
        indented_code = '\n'.join(' ' * indent + line if line.strip() else line 
                                for line in drug_code.split('\n'))
        
        # Tạo nội dung mới
        new_lines = (
            lines[:start_line] +
            [f'{" " * indent}"{drug_name}": {indented_code},'] +
            lines[end_line + 1:]
        )
        
        if dry_run:
            print(f"  [DRY RUN] Would update {drug_name} in {file_path}")
            print(f"  Lines {start_line + 1}-{end_line + 1} would be replaced")
            return True
        
        # Backup
        backup_file = file_path.with_suffix('.py.backup')
        if not backup_file.exists():
            shutil.copy2(file_path, backup_file)
            print(f"  Da backup: {backup_file}")
        
        # Write
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write('\n'.join(new_lines))
        
        print(f"  Da cap nhat {drug_name} trong {file_path}")
        return True
        
    except Exception as e:
        print(f"Error updating {drug_name} in {file_path}: {e}")
        import traceback
        traceback.print_exc()
        return False

def add_standard_fields(drug_name: str, file_path: str, dry_run: bool = True) -> Dict[str, Any]:
    """
    Bổ sung field chuẩn với template
    
    Args:
        drug_name: Tên thuốc
        file_path: Đường dẫn file
        dry_run: Chỉ preview, không apply
    
    Returns:
        Dict chứa thông tin kết quả
    """
    file_path_obj = Path(file_path)
    
    # Load drug
    drug_data = load_drug_from_file(file_path_obj, drug_name)
    if not drug_data:
        return {'success': False, 'error': 'Cannot load drug'}
    
    # Get standardizer
    standardizer = get_field_standardizer()
    
    # Add missing standard fields
    updated = standardizer.add_missing_fields(drug_data, include_additional=False, use_templates=True)
    
    # Check what was added
    added_fields = [f for f in STANDARD_14_FIELDS if f not in drug_data and f in updated]
    
    if not added_fields:
        return {'success': True, 'message': 'No fields to add', 'added_fields': []}
    
    # Update file
    success = update_drug_in_file(file_path_obj, drug_name, updated, dry_run=dry_run)
    
    return {
        'success': success,
        'added_fields': added_fields,
        'drug_name': drug_name,
        'file': str(file_path)
    }

def add_additional_fields(drug_name: str, file_path: str, dry_run: bool = True) -> Dict[str, Any]:
    """
    Bổ sung field bổ sung
    
    Args:
        drug_name: Tên thuốc
        file_path: Đường dẫn file
        dry_run: Chỉ preview, không apply
    
    Returns:
        Dict chứa thông tin kết quả
    """
    file_path_obj = Path(file_path)
    
    # Load drug
    drug_data = load_drug_from_file(file_path_obj, drug_name)
    if not drug_data:
        return {'success': False, 'error': 'Cannot load drug'}
    
    # Get standardizer
    standardizer = get_field_standardizer()
    
    # Add missing additional fields
    updated = standardizer.add_missing_fields(drug_data, include_additional=True, use_templates=True)
    
    # Check what was added
    added_fields = [f for f in ADDITIONAL_8_FIELDS if f not in drug_data and f in updated]
    
    if not added_fields:
        return {'success': True, 'message': 'No fields to add', 'added_fields': []}
    
    # Update file
    success = update_drug_in_file(file_path_obj, drug_name, updated, dry_run=dry_run)
    
    return {
        'success': success,
        'added_fields': added_fields,
        'drug_name': drug_name,
        'file': str(file_path)
    }

def add_all_missing_fields(drug_name: str, file_path: str, dry_run: bool = True) -> Dict[str, Any]:
    """
    Bổ sung tất cả field thiếu
    
    Args:
        drug_name: Tên thuốc
        file_path: Đường dẫn file
        dry_run: Chỉ preview, không apply
    
    Returns:
        Dict chứa thông tin kết quả
    """
    file_path_obj = Path(file_path)
    
    # Load drug
    drug_data = load_drug_from_file(file_path_obj, drug_name)
    if not drug_data:
        return {'success': False, 'error': 'Cannot load drug'}
    
    # Get standardizer
    standardizer = get_field_standardizer()
    
    # Add all missing fields
    updated = standardizer.add_missing_fields(drug_data, include_additional=True, use_templates=True)
    
    # Check what was added
    all_missing = [f for f in STANDARD_14_FIELDS + ADDITIONAL_8_FIELDS 
                   if f not in drug_data and f in updated]
    
    if not all_missing:
        return {'success': True, 'message': 'No fields to add', 'added_fields': []}
    
    # Update file
    success = update_drug_in_file(file_path_obj, drug_name, updated, dry_run=dry_run)
    
    # Validate
    validator = get_field_validator()
    validation_result = validator.validate_all_fields(updated)
    
    return {
        'success': success,
        'added_fields': all_missing,
        'validation': validation_result,
        'drug_name': drug_name,
        'file': str(file_path)
    }

def preview_changes(drug_name: str, file_path: str) -> Dict[str, Any]:
    """
    Preview thay đổi trước khi apply
    
    Args:
        drug_name: Tên thuốc
        file_path: Đường dẫn file
    
    Returns:
        Dict chứa preview
    """
    file_path_obj = Path(file_path)
    
    # Load drug
    drug_data = load_drug_from_file(file_path_obj, drug_name)
    if not drug_data:
        return {'success': False, 'error': 'Cannot load drug'}
    
    # Get validator
    validator = get_field_validator()
    validation = validator.validate_all_fields(drug_data)
    
    # Get standardizer
    standardizer = get_field_standardizer()
    
    # Preview with standard fields
    updated_standard = standardizer.add_missing_fields(drug_data, include_additional=False, use_templates=True)
    added_standard = [f for f in STANDARD_14_FIELDS if f not in drug_data and f in updated_standard]
    
    # Preview with all fields
    updated_all = standardizer.add_missing_fields(drug_data, include_additional=True, use_templates=True)
    added_additional = [f for f in ADDITIONAL_8_FIELDS if f not in drug_data and f in updated_all]
    
    return {
        'success': True,
        'drug_name': drug_name,
        'file': str(file_path),
        'current_validation': validation,
        'missing_standard_fields': validation.get('missing_standard_fields', []),
        'missing_additional_fields': validation.get('missing_additional_fields', []),
        'would_add_standard': added_standard,
        'would_add_additional': added_additional,
    }

if __name__ == "__main__":
    # Test
    import sys
    
    if len(sys.argv) < 3:
        print("Usage: python add_fields_helper.py <drug_name> <file_path> [dry_run]")
        print("Example: python add_fields_helper.py 'Levobupivacaine' 'drugs/drug_modules/anesthesia/local_anesthetics.py'")
        sys.exit(1)
    
    drug_name = sys.argv[1]
    file_path = sys.argv[2]
    dry_run = len(sys.argv) < 4 or sys.argv[3].lower() != 'apply'
    
    print("="*60)
    print("PREVIEW CHANGES")
    print("="*60)
    preview = preview_changes(drug_name, file_path)
    if preview['success']:
        print(f"\nDrug: {preview['drug_name']}")
        print(f"File: {preview['file']}")
        print(f"\nMissing standard fields: {len(preview['missing_standard_fields'])}")
        for field in preview['missing_standard_fields']:
            print(f"  - {field}")
        print(f"\nMissing additional fields: {len(preview['missing_additional_fields'])}")
        for field in preview['missing_additional_fields']:
            print(f"  - {field}")
        print(f"\nWould add standard fields: {len(preview['would_add_standard'])}")
        for field in preview['would_add_standard']:
            print(f"  - {field}")
        print(f"\nWould add additional fields: {len(preview['would_add_additional'])}")
        for field in preview['would_add_additional']:
            print(f"  - {field}")
    
    if dry_run:
        print("\n" + "="*60)
        print("DRY RUN - No changes made")
        print("="*60)
        print("\nTo apply changes, run with 'apply' as third argument:")
        print(f"python add_fields_helper.py '{drug_name}' '{file_path}' apply")
    else:
        print("\n" + "="*60)
        print("APPLYING CHANGES")
        print("="*60)
        result = add_all_missing_fields(drug_name, file_path, dry_run=False)
        if result['success']:
            print(f"\nSuccess! Added {len(result['added_fields'])} fields")
            print(f"Added fields: {', '.join(result['added_fields'])}")
        else:
            print(f"\nError: {result.get('error', 'Unknown error')}")

