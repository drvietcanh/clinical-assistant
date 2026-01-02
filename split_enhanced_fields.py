"""
Script để chia nhỏ file enhanced_fields_overrides.py
"""
import re
from pathlib import Path
from collections import defaultdict

# Mapping categories từ section comments
SECTION_TO_CATEGORY = {
    'CARDIOVASCULAR': 'cardiovascular',
    'GASTROINTESTINAL': 'gastrointestinal',
    'EMERGENCY': 'emergency',
    'ANTIBIOTICS': 'antimicrobial',
    'DIABETES': 'diabetes',
    'HEMATOLOGY': 'hematology',
    'ANALGESICS': 'analgesics',
    'ONCOLOGY': 'oncology',
    'NEUROLOGY': 'neurological',
    'NEUROLOGICAL': 'neurological',
    'RESPIRATORY': 'respiratory',
}

def find_category_from_section(section_line):
    """Tìm category từ section comment"""
    for key, category in SECTION_TO_CATEGORY.items():
        if key in section_line.upper():
            return category
    return 'other'

def extract_drug_entries(content):
    """Extract các drug entries từ content"""
    lines = content.split('\n')
    
    # Tìm start của dict
    start_idx = None
    for i, line in enumerate(lines):
        if 'EXTRA_ENHANCED_FIELDS' in line and '=' in line:
            start_idx = i
            break
    
    if start_idx is None:
        return []
    
    # Tìm tất cả section comments và drug entries
    sections = []
    current_section = None
    current_category = 'other'
    current_start = start_idx + 1
    
    i = start_idx + 1
    while i < len(lines):
        line = lines[i]
        
        # Tìm section comment
        if re.match(r'^\s*#\s*=+.*=+\s*$', line):
            # Lưu section trước đó
            if current_section is not None:
                sections.append({
                    'category': current_category,
                    'start': current_start,
                    'end': i - 1,
                    'section_line': current_section
                })
            
            # Bắt đầu section mới
            current_section = line
            current_category = find_category_from_section(line)
            current_start = i + 1
        
        # Tìm .update({ pattern
        elif '.update({' in line:
            # Lưu section trước đó
            if current_section is not None:
                sections.append({
                    'category': current_category,
                    'start': current_start,
                    'end': i - 1,
                    'section_line': current_section
                })
            
            # Tìm end của update block (})
            update_start = i
            brace_count = 0
            found_open = False
            for j in range(i, len(lines)):
                for char in lines[j]:
                    if char == '{':
                        brace_count += 1
                        found_open = True
                    elif char == '}':
                        brace_count -= 1
                        if found_open and brace_count == 0:
                            # Tìm category từ context trước đó
                            # Tìm section comment gần nhất
                            for k in range(j, max(j-50, 0), -1):
                                if re.match(r'^\s*#\s*=+.*=+\s*$', lines[k]):
                                    current_category = find_category_from_section(lines[k])
                                    break
                            
                            sections.append({
                                'category': current_category,
                                'start': update_start,
                                'end': j,
                                'section_line': 'update_block'
                            })
                            i = j
                            current_section = None
                            current_start = j + 1
                            break
                if found_open and brace_count == 0:
                    break
            continue
        
        # Tìm end của dict chính
        elif i > start_idx and line.strip() == '}' and 'EXTRA_ENHANCED_FIELDS' not in content[max(0, i-20):i]:
            # Lưu section cuối cùng
            if current_section is not None:
                sections.append({
                    'category': current_category,
                    'start': current_start,
                    'end': i - 1,
                    'section_line': current_section
                })
            break
        
        i += 1
    
    return sections, lines

def main():
    file_path = Path('drugs/enhanced_fields_overrides.py')
    content = file_path.read_text(encoding='utf-8')
    lines = content.split('\n')
    
    # Extract header
    header_lines = []
    for i, line in enumerate(lines):
        if 'EXTRA_ENHANCED_FIELDS' in line and '=' in line:
            header_lines = lines[:i+1]
            break
    
    header = '\n'.join(header_lines) + '\n'
    
    # Extract sections
    print("Extracting sections...")
    sections, all_lines = extract_drug_entries(content)
    print(f"Found {len(sections)} sections")
    
    # Group by category
    entries_by_category = defaultdict(list)
    for section in sections:
        category = section['category']
        block_lines = all_lines[section['start']:section['end']+1]
        block_text = '\n'.join(block_lines)
        entries_by_category[category].append({
            'section_line': section['section_line'],
            'block': block_text
        })
    
    # Tạo thư mục
    enhanced_fields_dir = Path('drugs/enhanced_fields')
    enhanced_fields_dir.mkdir(exist_ok=True)
    
    # Tạo các file theo category
    category_files = {}
    for category, entries in sorted(entries_by_category.items()):
        print(f"\nCreating {category}.py with {len(entries)} sections...")
        
        file_content = f'''"""
Enhanced fields overrides - {category.title()}
"""
from typing import Any, Dict


{category.upper()}_ENHANCED_FIELDS: Dict[str, Dict[str, Any]] = {{
'''
        
        for entry in entries:
            if entry['section_line'] != 'update_block':
                file_content += f"    {entry['section_line']}\n"
            file_content += entry['block']
            # Đảm bảo có dấu phẩy nếu cần
            if not entry['block'].rstrip().endswith(',') and not entry['block'].rstrip().endswith('{'):
                file_content += ','
            file_content += '\n\n'
        
        file_content += '}\n'
        
        file_path = enhanced_fields_dir / f'{category}.py'
        file_path.write_text(file_content, encoding='utf-8')
        category_files[category] = f'{category.upper()}_ENHANCED_FIELDS'
        print(f"  Created {file_path}")
    
    # Tạo __init__.py
    print("\nCreating __init__.py...")
    init_content = '''"""
Enhanced fields overrides
Combines all enhanced fields from category-specific files
"""
from typing import Any, Dict

'''
    
    # Import statements
    for category in sorted(category_files.keys()):
        init_content += f'from .{category} import {category_files[category]}\n'
    
    init_content += '\n# Combine all enhanced fields\n'
    init_content += 'EXTRA_ENHANCED_FIELDS: Dict[str, Dict[str, Any]] = {\n'
    
    for category in sorted(category_files.keys()):
        init_content += f'    **{category_files[category]},\n'
    
    init_content += '}\n\n'
    init_content += '__all__ = ["EXTRA_ENHANCED_FIELDS"]\n'
    
    init_path = enhanced_fields_dir / '__init__.py'
    init_path.write_text(init_content, encoding='utf-8')
    print(f"  Created {init_path}")
    
    # Update file gốc
    print("\nUpdating enhanced_fields_overrides.py for backward compatibility...")
    new_content = f'''"""
Enhanced fields overrides for specific drugs.
Backward compatibility: imports from enhanced_fields module
"""

from .enhanced_fields import EXTRA_ENHANCED_FIELDS

__all__ = ["EXTRA_ENHANCED_FIELDS"]
'''
    
    overrides_path = Path('drugs/enhanced_fields_overrides.py')
    overrides_path.write_text(new_content, encoding='utf-8')
    print(f"  Updated {overrides_path}")
    
    print("\nDone!")

if __name__ == '__main__':
    main()

