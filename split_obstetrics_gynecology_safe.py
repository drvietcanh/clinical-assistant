"""
Thuật toán tách obstetrics_gynecology.py thành subfolder - Phiên bản an toàn
Sử dụng cách load module trực tiếp để lấy dữ liệu, tránh lỗi parsing
"""
import sys
import shutil
import json
from pathlib import Path
from typing import Dict, List, Tuple
from collections import defaultdict

def categorize_drug_by_group(drug_name: str, drug_data: Dict) -> str:
    """
    Phân loại thuốc theo group
    
    Returns:
        category: contraceptives, hormone_replacement, fertility_drugs, 
                 vaginal_medications, uterotonics, other_obgyn
    """
    group = drug_data.get('group', '').lower()
    
    # Uterotonics (theo note trong file, nên ở emergency nhưng hiện tại ở đây)
    if 'uterotonic' in group or 'ergot' in group or 'prostaglandin' in group:
        if 'methylergonovine' in drug_name.lower() or 'carboprost' in drug_name.lower() or 'dinoprostone' in drug_name.lower():
            return 'uterotonics'
    
    # Contraceptives
    if 'contraceptive' in group or 'contraception' in group:
        if 'emergency' in group:
            return 'contraceptives'  # Emergency contraception vẫn là contraceptive
        return 'contraceptives'
    
    # Hormone replacement
    if 'hormone' in group or 'estrogen' in group or 'progesterone' in group or 'progestin' in group:
        if 'replacement' in group or 'hrt' in group:
            return 'hormone_replacement'
        # Progestin replacement therapy
        if 'replacement therapy' in group:
            return 'hormone_replacement'
    
    # Fertility drugs
    if 'fertility' in group or 'ovulation' in group or 'ivf' in group or 'luteal' in group:
        return 'fertility_drugs'
    
    # Vaginal medications
    if 'vaginal' in group or 'antifungal' in group or 'candidiasis' in group or 'bacterial vaginosis' in group or 'bv' in group:
        return 'vaginal_medications'
    
    # Default
    return 'other_obgyn'

def load_drugs_from_module() -> Dict[str, Dict]:
    """
    Load thuốc từ module trực tiếp (an toàn nhất)
    
    Returns:
        Dict {drug_name: drug_data}
    """
    try:
        # Import module
        sys.path.insert(0, str(Path.cwd()))
        from drugs.drug_modules.obstetrics_gynecology import OBSTETRICS_GYNECOLOGY_DRUGS
        
        return dict(OBSTETRICS_GYNECOLOGY_DRUGS)
    except Exception as e:
        print(f"Error loading module: {e}")
        import traceback
        traceback.print_exc()
        return {}

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

def split_obstetrics_gynecology_safe():
    """
    Tách obstetrics_gynecology.py thành subfolder - Thuật toán an toàn
    """
    source_file = Path("drugs/drug_modules/obstetrics_gynecology.py")
    target_dir = Path("drugs/drug_modules/obstetrics_gynecology")
    
    if not source_file.exists():
        print(f"File not found: {source_file}")
        return False
    
    print("="*60)
    print("THUAT TOAN TACH FILE AN TOAN")
    print("="*60)
    
    # Bước 1: Load thuốc từ module (an toàn nhất)
    print("\nBuoc 1: Dang load thuoc tu module...")
    all_drugs = load_drugs_from_module()
    
    if not all_drugs:
        print("Khong the load thuoc tu module!")
        return False
    
    print(f"Da load {len(all_drugs)} thuoc")
    
    # Bước 2: Phân loại thuốc
    print("\nBuoc 2: Dang phan loai thuoc...")
    categories = defaultdict(list)
    
    for drug_name, drug_data in all_drugs.items():
        category = categorize_drug_by_group(drug_name, drug_data)
        categories[category].append((drug_name, drug_data))
        print(f"  {drug_name} -> {category}")
    
    print(f"\nPhan loai hoan thanh:")
    for category, drugs in categories.items():
        print(f"  {category}: {len(drugs)} thuoc")
    
    # Bước 3: Tạo thư mục
    print("\nBuoc 3: Dang tao thu muc...")
    target_dir.mkdir(exist_ok=True)
    print(f"Da tao: {target_dir}")
    
    # Bước 4: Tạo file cho từng category
    print("\nBuoc 4: Dang tao file cho tung category...")
    
    file_mappings = {
        'contraceptives': ('contraceptives.py', 'CONTRACEPTIVES_DRUGS'),
        'hormone_replacement': ('hormone_replacement.py', 'HORMONE_REPLACEMENT_DRUGS'),
        'fertility_drugs': ('fertility_drugs.py', 'FERTILITY_DRUGS'),
        'vaginal_medications': ('vaginal_medications.py', 'VAGINAL_MEDICATIONS_DRUGS'),
        'uterotonics': ('uterotonics.py', 'UTEROTONICS_DRUGS'),
        'other_obgyn': ('other_obgyn.py', 'OTHER_OBGYN_DRUGS'),
    }
    
    header = '''"""
Obstetrics and Gynecology Medications
{category_description}
"""
from typing import Dict, Any

'''
    
    category_descriptions = {
        'contraceptives': 'Contraceptive medications',
        'hormone_replacement': 'Hormone replacement therapy',
        'fertility_drugs': 'Fertility and ovulation medications',
        'vaginal_medications': 'Vaginal medications (antifungals, antibacterials)',
        'uterotonics': 'Uterotonic medications (Note: Should be in emergency module)',
        'other_obgyn': 'Other obstetrics and gynecology medications',
    }
    
    created_vars = {}
    
    for category, (filename, var_name) in file_mappings.items():
        if not categories[category]:
            continue
        
        filepath = target_dir / filename
        
        # Tạo nội dung file
        content = header.format(category_description=category_descriptions[category])
        content += f"{var_name}: Dict[str, Dict[str, Any]] = {{\n"
        
        for drug_name, drug_data in categories[category]:
            # Format drug entry
            drug_code = format_drug_dict(drug_data, indent_level=4)
            # Indent to proper level
            indented_code = '\n'.join('    ' + line if line.strip() else line 
                                    for line in drug_code.split('\n'))
            content += f'    "{drug_name}": {indented_code},\n\n'
        
        content += "}\n\n"
        content += f"__all__ = ['{var_name}']\n"
        
        # Ghi file
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        
        created_vars[category] = var_name
        print(f"  Da tao: {filepath} ({len(categories[category])} thuoc)")
    
    # Bước 5: Tạo __init__.py
    print("\nBuoc 5: Dang tao __init__.py...")
    
    init_content = '''"""
Obstetrics and Gynecology Drugs
Combines all OB/GYN drugs from category-specific files
"""
from typing import Dict, Any

'''
    
    for category, (filename, var_name) in file_mappings.items():
        if category in created_vars:
            module_name = filename[:-3]  # Remove .py
            init_content += f"from .{module_name} import {var_name}\n"
    
    init_content += "\n# Combine all OB/GYN drugs\n"
    init_content += "OBSTETRICS_GYNECOLOGY_DRUGS: Dict[str, Dict[str, Any]] = {\n"
    
    for var_name in created_vars.values():
        init_content += f"    **{var_name},\n"
    
    init_content += "}\n\n"
    init_content += "__all__ = ['OBSTETRICS_GYNECOLOGY_DRUGS']\n"
    
    init_file = target_dir / "__init__.py"
    with open(init_file, 'w', encoding='utf-8') as f:
        f.write(init_content)
    
    print(f"  Da tao: {init_file}")
    
    # Bước 6: Backup file cũ
    print("\nBuoc 6: Dang backup file cu...")
    backup_file = source_file.with_suffix('.py.backup')
    shutil.copy2(source_file, backup_file)
    print(f"  Da backup: {backup_file}")
    
    # Bước 7: Tạo wrapper file mới
    print("\nBuoc 7: Dang tao wrapper file...")
    
    wrapper_content = '''"""
Obstetrics and Gynecology Medications
Backward compatibility: imports from obstetrics_gynecology module
"""

from .obstetrics_gynecology import OBSTETRICS_GYNECOLOGY_DRUGS

__all__ = ['OBSTETRICS_GYNECOLOGY_DRUGS']
'''
    
    with open(source_file, 'w', encoding='utf-8') as f:
        f.write(wrapper_content)
    
    print(f"  Da cap nhat: {source_file} (wrapper)")
    
    # Bước 8: Test import
    print("\nBuoc 8: Dang test import...")
    try:
        # Clear cache
        import importlib
        if 'drugs.drug_modules.obstetrics_gynecology' in sys.modules:
            del sys.modules['drugs.drug_modules.obstetrics_gynecology']
        if 'drugs.drug_modules.obstetrics_gynecology.obstetrics_gynecology' in sys.modules:
            del sys.modules['drugs.drug_modules.obstetrics_gynecology.obstetrics_gynecology']
        
        # Test import
        from drugs.drug_modules.obstetrics_gynecology import OBSTETRICS_GYNECOLOGY_DRUGS
        count = len(OBSTETRICS_GYNECOLOGY_DRUGS)
        
        if count == len(all_drugs):
            print(f"  ✓ Import thanh cong: {count} thuoc")
            print("  ✓ So luong thuoc khop!")
        else:
            print(f"  ⚠ Import thanh cong nhung so luong khac: {count} vs {len(all_drugs)}")
        
        # Test một số thuốc
        sample_drugs = list(OBSTETRICS_GYNECOLOGY_DRUGS.keys())[:3]
        for drug_name in sample_drugs:
            drug_data = OBSTETRICS_GYNECOLOGY_DRUGS[drug_name]
            if 'group' in drug_data:
                print(f"  ✓ {drug_name}: OK")
            else:
                print(f"  ⚠ {drug_name}: Thieu field 'group'")
        
        return True
        
    except Exception as e:
        print(f"  ✗ Import that bai: {e}")
        import traceback
        traceback.print_exc()
        
        # Restore backup
        print("\nDang khoi phuc file backup...")
        shutil.copy2(backup_file, source_file)
        print("  Da khoi phuc file goc")
        
        return False

def main():
    """Hàm chính"""
    import io
    if sys.platform == 'win32':
        sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')
    
    print("BAT DAU TACH FILE OBSTETRICS_GYNECOLOGY.PY")
    print("Su dung thuat toan an toan - load tu module truc tiep")
    print()
    
    if split_obstetrics_gynecology_safe():
        print("\n" + "="*60)
        print("HOAN THANH! File da duoc tach thanh cong.")
        print("="*60)
    else:
        print("\n" + "="*60)
        print("CO LOI! File goc da duoc khoi phuc tu backup.")
        print("="*60)
        return 1
    
    return 0

if __name__ == "__main__":
    sys.exit(main())

