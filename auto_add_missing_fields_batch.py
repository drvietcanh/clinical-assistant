#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Automatically add missing enhanced fields to drugs
Uses templates and existing data where possible
"""

import ast
import re
from pathlib import Path
from typing import Dict, List, Tuple

def get_renal_adjustment_template(drug_name: str, is_renal_cleared: bool = True) -> str:
    """Generate renal_adjustment template"""
    if is_renal_cleared:
        return f'''"renal_adjustment": {{
    "normal": "Không cần chỉnh liều",
    "30_60": "Thận trọng, có thể cần giảm liều",
    "under_30": "Thận trọng, giảm liều (thải trừ qua thận)",
    "dialysis": "Thận trọng, giảm liều. {drug_name} không được lọc sạch hiệu quả qua thẩm phân máu.",
    "notes": "{drug_name} thải trừ qua thận. Suy thận có thể tăng nguy cơ tích lũy."
}}'''
    else:
        return f'''"renal_adjustment": {{
    "normal": "Không cần chỉnh liều",
    "30_60": "Không cần chỉnh liều",
    "under_30": "Thận trọng",
    "dialysis": "Không cần chỉnh liều",
    "notes": "{drug_name} không thải trừ chủ yếu qua thận."
}}'''

def get_drug_interactions_template() -> str:
    """Generate drug_interactions template"""
    return '''"drug_interactions": {
    "major": [],
    "moderate": [],
    "minor": []
}'''

def get_contraindications_detail_template() -> str:
    """Generate contraindications_detail template"""
    return '''"contraindications_detail": {
    "tuyệt_đối": [],
    "tương_đối": []
}'''

def get_reversal_agents_template() -> str:
    """Generate reversal_agents template"""
    return '''"reversal_agents": {
    "available": False,
    "agents": [],
    "notes": "Không có antidote đặc hiệu. Điều trị quá liều chủ yếu là hỗ trợ."
}'''

def find_drug_in_file(file_path: Path, drug_name: str) -> Tuple[int, int]:
    """Find drug definition in file, return (start_line, end_line)"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
            lines = content.split('\n')
            
        # Look for drug name in quotes
        pattern = f'"{drug_name}"'
        for i, line in enumerate(lines, 1):
            if pattern in line and ':' in line:
                # Found the drug definition start
                # Now find the closing brace
                brace_count = 0
                start_line = i
                in_dict = False
                
                for j in range(i - 1, len(lines)):
                    line_content = lines[j]
                    for char in line_content:
                        if char == '{':
                            brace_count += 1
                            in_dict = True
                        elif char == '}':
                            brace_count -= 1
                            if in_dict and brace_count == 0:
                                return (start_line, j + 1)
                
                return (start_line, start_line + 50)  # Fallback
    except Exception as e:
        print(f"Error finding drug in {file_path}: {e}")
    
    return (0, 0)

def add_field_to_drug(file_path: Path, drug_name: str, field_name: str, field_template: str) -> bool:
    """Add a field to a drug in a file"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Check if field already exists
        if f'"{field_name}"' in content or f"'{field_name}'" in content:
            # Check if it's for this specific drug
            drug_pattern = f'"{drug_name}"'
            if drug_pattern in content:
                # Find position after drug name
                drug_pos = content.find(drug_pattern)
                drug_section = content[drug_pos:drug_pos+5000]  # Get section around drug
                if f'"{field_name}"' in drug_section or f"'{field_name}'" in drug_section:
                    return False  # Field already exists
        
        # Find drug and add field before the closing brace
        lines = content.split('\n')
        drug_pattern = f'"{drug_name}"'
        
        for i, line in enumerate(lines):
            if drug_pattern in line and ':' in line:
                # Found drug, now find where to insert
                # Look for the last field before closing brace
                brace_count = 0
                insert_pos = i + 1
                
                for j in range(i, len(lines)):
                    current_line = lines[j]
                    for char in current_line:
                        if char == '{':
                            brace_count += 1
                        elif char == '}':
                            brace_count -= 1
                            if brace_count == 0:
                                # Found closing brace, insert before this line
                                # But first, find the last field
                                for k in range(j - 1, i, -1):
                                    if lines[k].strip() and not lines[k].strip().startswith('#'):
                                        # Found last non-empty line
                                        indent = len(lines[k]) - len(lines[k].lstrip())
                                        field_indent = ' ' * (indent + 4)
                                        field_lines = field_template.split('\n')
                                        formatted_field = ',\n'.join([field_indent + line.lstrip() for line in field_lines])
                                        
                                        # Insert before closing brace
                                        lines.insert(j, formatted_field)
                                        new_content = '\n'.join(lines)
                                        
                                        with open(file_path, 'w', encoding='utf-8') as f:
                                            f.write(new_content)
                                        return True
        
        return False
    except Exception as e:
        print(f"Error adding field to {file_path}: {e}")
        return False

def find_drug_file(drug_name: str) -> Path:
    """Find which file contains a drug"""
    modules_path = Path("drugs/drug_modules")
    
    for py_file in modules_path.rglob("*.py"):
        if py_file.name == "__init__.py":
            continue
        
        try:
            with open(py_file, 'r', encoding='utf-8') as f:
                content = f.read()
                if f'"{drug_name}"' in content:
                    return py_file
        except:
            continue
    
    return None

def main():
    """Main function to add missing fields"""
    from drugs.drug_database import DRUG_DATABASE
    
    # Get drugs missing each field
    missing_renal = []
    missing_interactions = []
    missing_contra_detail = []
    missing_reversal = []
    
    for drug_name, drug_data in DRUG_DATABASE.items():
        if drug_data is None or not isinstance(drug_data, dict):
            continue
        
        if "renal_adjustment" not in drug_data or drug_data.get("renal_adjustment") is None:
            missing_renal.append(drug_name)
        if "drug_interactions" not in drug_data or drug_data.get("drug_interactions") is None:
            missing_interactions.append(drug_name)
        if "contraindications_detail" not in drug_data or drug_data.get("contraindications_detail") is None:
            missing_contra_detail.append(drug_name)
        if "reversal_agents" not in drug_data or drug_data.get("reversal_agents") is None:
            missing_reversal.append(drug_name)
    
    print(f"Found {len(missing_renal)} drugs missing renal_adjustment")
    print(f"Found {len(missing_interactions)} drugs missing drug_interactions")
    print(f"Found {len(missing_contra_detail)} drugs missing contraindications_detail")
    print(f"Found {len(missing_reversal)} drugs missing reversal_agents")
    
    # For now, just report - manual addition is safer
    print("\nNote: Automatic field addition is complex due to file structure.")
    print("Recommendation: Use manual addition with templates from documentation.")

if __name__ == '__main__':
    main()
