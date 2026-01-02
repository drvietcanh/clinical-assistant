"""
Script đơn giản để chia nhỏ file enhanced_fields_overrides.py
Dựa trên section comments
"""
import re
from pathlib import Path
from collections import defaultdict

# Mapping categories
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

def find_category(section_line):
    """Tìm category từ section comment"""
    section_upper = section_line.upper()
    for key, category in SECTION_TO_CATEGORY.items():
        if key in section_upper:
            return category
    return 'other'

def main():
    file_path = Path('drugs/enhanced_fields_overrides.py')
    content = file_path.read_text(encoding='utf-8')
    lines = content.split('\n')
    
    # Tìm header
    header_end = 0
    for i, line in enumerate(lines):
        if 'EXTRA_ENHANCED_FIELDS' in line and '=' in line and '{' in line:
            header_end = i + 1
            break
    
    header = '\n'.join(lines[:header_end])
    
    # Tìm tất cả section comments và .update() blocks
    sections = []
    i = header_end
    
    while i < len(lines):
        line = lines[i]
        
        # Tìm section comment
        if re.match(r'^\s*#\s*=+.*=+\s*$', line):
            section_line = line
            category = find_category(section_line)
            start = i
            
            # Tìm end: section comment tiếp theo, .update({, hoặc } cuối
            end = i + 1
            for j in range(i + 1, len(lines)):
                if (re.match(r'^\s*#\s*=+.*=+\s*$', lines[j]) or 
                    '.update({' in lines[j] or
                    (lines[j].strip() == '}' and j > i + 10)):
                    end = j
                    break
            
            sections.append({
                'category': category,
                'section_line': section_line,
                'start': start,
                'end': end,
                'is_update': False
            })
            i = end
            continue
        
        # Tìm .update({ block
        elif '.update({' in line:
            update_start = i
            # Tìm category từ section comment gần nhất
            category = 'other'
            for k in range(i, max(i-50, header_end), -1):
                if re.match(r'^\s*#\s*=+.*=+\s*$', lines[k]):
                    category = find_category(lines[k])
                    break
            
            # Tìm end của update block (})
            brace_count = 0
            found_open = False
            update_end = i
            for j in range(i, len(lines)):
                for char in lines[j]:
                    if char == '{':
                        brace_count += 1
                        found_open = True
                    elif char == '}':
                        brace_count -= 1
                        if found_open and brace_count == 0:
                            update_end = j + 1
                            break
                if found_open and brace_count == 0:
                    break
            
            sections.append({
                'category': category,
                'section_line': line,
                'start': update_start,
                'end': update_end,
                'is_update': True
            })
            i = update_end
            continue
        
        i += 1
    
    print(f"Found {len(sections)} sections")
    
    # Group by category
    entries_by_category = defaultdict(list)
    for section in sections:
        category = section['category']
        block_lines = lines[section['start']:section['end']]
        block_text = '\n'.join(block_lines)
        entries_by_category[category].append({
            'section_line': section['section_line'],
            'block': block_text,
            'is_update': section['is_update']
        })
    
    # Tạo thư mục
    enhanced_fields_dir = Path('drugs/enhanced_fields')
    enhanced_fields_dir.mkdir(exist_ok=True)
    
    # Tạo các file
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
            if not entry['is_update']:
                # Section comment + block
                file_content += entry['block'] + '\n'
            else:
                # .update() block - cần extract nội dung trong {}
                update_block = entry['block']
                # Tìm nội dung trong .update({ ... })
                match = re.search(r'\.update\(\s*\{([\s\S]*)\}\s*\)', update_block)
                if match:
                    inner_content = match.group(1)
                    file_content += inner_content + '\n'
        
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
    print("\nUpdating enhanced_fields_overrides.py...")
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

