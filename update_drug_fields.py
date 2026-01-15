#!/usr/bin/env python3
"""
Script to update drug fields in module files
Helps manually fill in missing fields for drugs
"""

import json
import re
from pathlib import Path
from typing import Dict, Any, Optional

BASE_DIR = Path("drugs/drug_modules")

def read_module_file(module_path: str) -> Optional[str]:
    """Read module file content"""
    full_path = BASE_DIR / module_path
    if not full_path.exists():
        print(f"❌ File không tồn tại: {full_path}")
        return None
    with open(full_path, "r", encoding="utf-8") as f:
        return f.read()

def find_drug_entry(content: str, drug_name: str) -> Optional[tuple]:
    """Find drug entry in module content"""
    # Create dict key from drug name
    dict_key = drug_name.replace(" ", "").replace("-", "").replace(".", "").replace("/", "")
    
    # Find the entry
    pattern = rf'"{re.escape(dict_key)}":\s*\{{([\s\S]*?)^\s*\}},?\s*$'
    match = re.search(pattern, content, re.MULTILINE)
    
    if match:
        start = match.start()
        end = match.end()
        return (start, end, match.group(0))
    return None

def update_field_in_entry(entry_str: str, field_name: str, new_value: Any) -> str:
    """Update a field in drug entry string"""
    # Handle different field types
    if isinstance(new_value, list):
        # Format list
        items = ",\n".join([f'                        "{item}"' for item in new_value])
        replacement = f'"{field_name}": [\n{items}\n                ]'
    elif isinstance(new_value, dict):
        # Format dict - simplified, may need more complex handling
        items = []
        for k, v in new_value.items():
            if isinstance(v, str):
                items.append(f'                        "{k}": "{v}"')
            elif isinstance(v, list):
                list_items = ", ".join([f'"{item}"' for item in v])
                items.append(f'                        "{k}": [{list_items}]')
            else:
                items.append(f'                        "{k}": {v}')
        items_str = ",\n".join(items)
        replacement = f'"{field_name}": {{\n{items_str}\n                }}'
    else:
        # String or other simple type
        escaped = str(new_value).replace('"', '\\"').replace('\n', '\\n')
        replacement = f'"{field_name}": "{escaped}"'
    
    # Find and replace the field
    pattern = rf'"{re.escape(field_name)}":\s*[^\n]*(?:\n[^\n]*)*?(?=,\s*"|\s*\n\s*"|\s*\n\s*\}})'
    match = re.search(pattern, entry_str)
    
    if match:
        return entry_str[:match.start()] + replacement + entry_str[match.end():]
    else:
        # Field not found, add it before the last closing brace
        # Find last field before closing brace
        last_field_pattern = r'(\s+)"([^"]+)":\s*[^\n]*(?:\n[^\n]*)*?(?=\s*\n\s*\})'
        last_match = re.search(last_field_pattern, entry_str)
        if last_match:
            insert_pos = last_match.end()
            return entry_str[:insert_pos] + f',\n{last_match.group(1)}{replacement}' + entry_str[insert_pos:]
    
    return entry_str

def update_drug_in_module(module_path: str, drug_name: str, updates: Dict[str, Any]) -> bool:
    """Update drug fields in module file"""
    content = read_module_file(module_path)
    if not content:
        return False
    
    # Find drug entry
    entry_info = find_drug_entry(content, drug_name)
    if not entry_info:
        print(f"⚠️  Không tìm thấy {drug_name} trong {module_path}")
        return False
    
    start, end, entry_str = entry_info
    
    # Update each field
    updated_entry = entry_str
    for field_name, new_value in updates.items():
        updated_entry = update_field_in_entry(updated_entry, field_name, new_value)
    
    # Replace in content
    new_content = content[:start] + updated_entry + content[end:]
    
    # Write back
    full_path = BASE_DIR / module_path
    with open(full_path, "w", encoding="utf-8") as f:
        f.write(new_content)
    
    print(f"✅ Đã cập nhật {drug_name} trong {module_path}")
    return True

def main():
    """Example usage"""
    print("Script hỗ trợ cập nhật field cho thuốc")
    print("Sử dụng hàm update_drug_in_module() để cập nhật")
    
    # Example: Update a drug
    # updates = {
    #     "side_effects": ["Tác dụng phụ 1", "Tác dụng phụ 2"],
    #     "mechanism_of_action": "Cơ chế tác dụng chi tiết..."
    # }
    # update_drug_in_module("miscellaneous/other.py", "Amvuttra", updates)

if __name__ == "__main__":
    main()
