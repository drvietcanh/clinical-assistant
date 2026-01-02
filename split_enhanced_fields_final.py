"""
Script để chia nhỏ file enhanced_fields_overrides.py
Extract đúng từng drug entry
"""
import re
from pathlib import Path
from collections import defaultdict

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
    section_upper = section_line.upper()
    for key, category in SECTION_TO_CATEGORY.items():
        if key in section_upper:
            return category
    return 'other'

def extract_drug_entry(lines, start_idx):
    """Extract một drug entry hoàn chỉnh từ start_idx"""
    # Tìm drug name
    drug_name_match = re.search(r'"([^"]+)":\s*\{', lines[start_idx])
    if not drug_name_match:
        return None, start_idx
    
    drug_name = drug_name_match.group(1)
    
    # Tìm end của entry: dấu }, ở cùng level
    brace_count = 0
    found_open = False
    end_idx = start_idx
    
    for i in range(start_idx, len(lines)):
        for char in lines[i]:
            if char == '{':
                brace_count += 1
                found_open = True
            elif char == '}':
                brace_count -= 1
                if found_open and brace_count == 0:
                    # Kiểm tra xem có dấu phẩy sau không
                    end_idx = i
                    # Tìm dòng kết thúc (có thể có }, hoặc },)
                    if i + 1 < len(lines) and lines[i+1].strip() == '':
                        end_idx = i + 1
                    elif ',' in lines[i] and lines[i].strip().endswith(','):
                        end_idx = i
                    break
        if found_open and brace_count == 0:
            break
    
    if end_idx <= start_idx:
        return None, start_idx
    
    entry_block = '\n'.join(lines[start_idx:end_idx+1])
    return {'name': drug_name, 'block': entry_block, 'start': start_idx, 'end': end_idx}, end_idx + 1

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
    
    # Tìm tất cả section comments và drug entries
    current_category = 'other'
    current_section = None
    drug_entries = []
    
    i = header_end
    while i < len(lines):
        line = lines[i]
        
        # Section comment
        if re.match(r'^\s*#\s*=+.*=+\s*$', line):
            current_section = line
            current_category = find_category(line)
            i += 1
            continue
        
        # .update({ block - skip và tìm category từ section trước
        elif '.update({' in line:
            # Extract nội dung trong .update({ ... })
            update_start = i
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
            
            # Extract các drug entries trong update block
            update_lines = lines[update_start+1:update_end-1]  # Bỏ .update({ và })
            update_i = 0
            while update_i < len(update_lines):
                if re.search(r'"([^"]+)":\s*\{', update_lines[update_i]):
                    entry, next_idx = extract_drug_entry(update_lines, update_i)
                    if entry:
                        entry['category'] = current_category
                        entry['section'] = current_section
                        drug_entries.append(entry)
                    update_i = next_idx
                else:
                    update_i += 1
            
            i = update_end
            continue
        
        # Drug entry
        elif re.search(r'"([^"]+)":\s*\{', line):
            entry, next_idx = extract_drug_entry(lines, i)
            if entry:
                entry['category'] = current_category
                entry['section'] = current_section
                drug_entries.append(entry)
            i = next_idx
            continue
        
        # End of main dict
        elif line.strip() == '}' and i > header_end + 10:
            break
        
        i += 1
    
    print(f"Found {len(drug_entries)} drug entries")
    
    # Group by category
    entries_by_category = defaultdict(list)
    for entry in drug_entries:
        category = entry['category']
        entries_by_category[category].append(entry)
    
    # Tạo thư mục
    enhanced_fields_dir = Path('drugs/enhanced_fields')
    enhanced_fields_dir.mkdir(exist_ok=True)
    
    # Tạo các file
    category_files = {}
    for category, entries in sorted(entries_by_category.items()):
        print(f"\nCreating {category}.py with {len(entries)} drugs...")
        
        file_content = f'''"""
Enhanced fields overrides - {category.title()}
"""
from typing import Any, Dict


{category.upper()}_ENHANCED_FIELDS: Dict[str, Dict[str, Any]] = {{
'''
        
        # Group entries by section
        current_section = None
        for entry in entries:
            if entry['section'] and entry['section'] != current_section:
                current_section = entry['section']
                file_content += f"    {current_section}\n"
            
            # Add entry với indent
            entry_lines = entry['block'].split('\n')
            indented = ['    ' + l if l.strip() else l for l in entry_lines]
            file_content += '\n'.join(indented) + '\n'
        
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

