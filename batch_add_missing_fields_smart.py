#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Smart batch addition of missing fields
- Copies from existing fields where possible
- Uses templates for missing data
- Updates files directly
"""

import ast
import re
from pathlib import Path
from typing import Dict, List, Optional
import json

def find_drug_file_location(drug_name: str) -> Optional[Path]:
    """Find which file contains a drug"""
    modules_path = Path("drugs/drug_modules")
    
    for py_file in modules_path.rglob("*.py"):
        if py_file.name == "__init__.py":
            continue
        
        try:
            with open(py_file, 'r', encoding='utf-8') as f:
                content = f.read()
                # Look for drug name as key in dictionary
                pattern = f'"{drug_name}"' + r'\s*:'
                if re.search(pattern, content):
                    return py_file
        except Exception as e:
            continue
    
    return None

def get_drug_data_from_file(file_path: Path, drug_name: str) -> Optional[Dict]:
    """Extract drug data from file"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Try to parse as Python AST
        try:
            tree = ast.parse(content)
            for node in ast.walk(tree):
                if isinstance(node, ast.Dict):
                    # Look for drug name in keys
                    for i, key in enumerate(node.keys):
                        if isinstance(key, ast.Constant) and key.value == drug_name:
                            # Found the drug, but extracting dict is complex
                            # Use regex instead
                            break
        except:
            pass
        
        # Use regex to find drug dict
        pattern = rf'"{drug_name}"\s*:\s*\{{(.*?)\n\s*\}}'
        match = re.search(pattern, content, re.DOTALL)
        if match:
            # This is complex, so we'll use a different approach
            pass
        
        # Import the module and get data
        import sys
        import importlib.util
        
        spec = importlib.util.spec_from_file_location("drug_module", file_path)
        if spec and spec.loader:
            module = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(module)
            
            # Find drug in module
            for attr_name in dir(module):
                attr = getattr(module, attr_name)
                if isinstance(attr, dict) and drug_name in attr:
                    return attr[drug_name]
    except Exception as e:
        print(f"Error getting drug data from {file_path}: {e}")
    
    return None

def add_contraindications_detail_from_existing(drug_data: Dict, file_path: Path, drug_name: str) -> bool:
    """Add contraindications_detail by copying from contraindications if it's a dict"""
    if "contraindications_detail" in drug_data and drug_data["contraindications_detail"]:
        return False  # Already exists
    
    contraindications = drug_data.get("contraindications")
    if isinstance(contraindications, dict):
        # Copy structure
        new_field = f'''"contraindications_detail": {{
    "tuyệt_đối": {json.dumps(contraindications.get("tuyệt_đối", []), ensure_ascii=False, indent=8)},
    "tương_đối": {json.dumps(contraindications.get("tương_đối", []), ensure_ascii=False, indent=8)}
}}'''
        return add_field_to_file(file_path, drug_name, "contraindications_detail", new_field)
    elif isinstance(contraindications, list):
        # Convert list to dict format
        new_field = f'''"contraindications_detail": {{
    "tuyệt_đối": {json.dumps(contraindications, ensure_ascii=False, indent=8)},
    "tương_đối": []
}}'''
        return add_field_to_file(file_path, drug_name, "contraindications_detail", new_field)
    
    return False

def add_drug_interactions_from_existing(drug_data: Dict, file_path: Path, drug_name: str) -> bool:
    """Add drug_interactions by copying from drug_interactions_detail if exists"""
    if "drug_interactions" in drug_data and drug_data["drug_interactions"]:
        return False  # Already exists
    
    interactions_detail = drug_data.get("drug_interactions_detail")
    if isinstance(interactions_detail, dict):
        # Copy structure
        new_field = f'''"drug_interactions": {{
    "major": {json.dumps(interactions_detail.get("major", []), ensure_ascii=False, indent=8)},
    "moderate": {json.dumps(interactions_detail.get("moderate", []), ensure_ascii=False, indent=8)},
    "minor": {json.dumps(interactions_detail.get("minor", []), ensure_ascii=False, indent=8)}
}}'''
        return add_field_to_file(file_path, drug_name, "drug_interactions", new_field)
    
    return False

def add_field_to_file(file_path: Path, drug_name: str, field_name: str, field_content: str) -> bool:
    """Add a field to a drug in a Python file"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            lines = f.readlines()
        
        # Find drug definition
        drug_line_idx = None
        for i, line in enumerate(lines):
            if f'"{drug_name}"' in line and ':' in line:
                drug_line_idx = i
                break
        
        if drug_line_idx is None:
            return False
        
        # Check if field already exists for this drug
        in_drug_section = False
        brace_count = 0
        for i in range(drug_line_idx, len(lines)):
            line = lines[i]
            if f'"{drug_name}"' in line:
                in_drug_section = True
                brace_count = 0
            
            if in_drug_section:
                for char in line:
                    if char == '{':
                        brace_count += 1
                    elif char == '}':
                        brace_count -= 1
                        if brace_count == 0:
                            # End of drug section
                            break
                
                if f'"{field_name}"' in line or f"'{field_name}'" in line:
                    return False  # Field already exists
        
        # Find insertion point (before closing brace of drug dict)
        insert_idx = None
        in_drug = False
        brace_count = 0
        
        for i in range(drug_line_idx, len(lines)):
            line = lines[i]
            if f'"{drug_name}"' in line:
                in_drug = True
                brace_count = 0
            
            if in_drug:
                for char in line:
                    if char == '{':
                        brace_count += 1
                    elif char == '}':
                        brace_count -= 1
                        if brace_count == 0 and in_drug:
                            # Found closing brace of drug dict
                            insert_idx = i
                            break
                
                if insert_idx:
                    break
        
        if insert_idx is None:
            return False
        
        # Get indentation from previous line
        prev_line = lines[insert_idx - 1] if insert_idx > 0 else ""
        indent = len(prev_line) - len(prev_line.lstrip())
        field_indent = ' ' * (indent + 4)
        
        # Format field content with proper indentation
        field_lines = field_content.split('\n')
        formatted_lines = []
        for line in field_lines:
            if line.strip():
                formatted_lines.append(field_indent + line.lstrip())
            else:
                formatted_lines.append('')
        
        # Add comma to previous line if needed
        if insert_idx > 0:
            prev_line_stripped = lines[insert_idx - 1].rstrip()
            if prev_line_stripped and not prev_line_stripped.endswith(',') and not prev_line_stripped.endswith('{'):
                lines[insert_idx - 1] = prev_line_stripped + ',\n'
        
        # Insert field
        formatted_field = ',\n'.join(formatted_lines)
        lines.insert(insert_idx, formatted_field + ',\n')
        
        # Write back
        with open(file_path, 'w', encoding='utf-8') as f:
            f.writelines(lines)
        
        return True
    except Exception as e:
        print(f"Error adding field to {file_path}: {e}")
        import traceback
        traceback.print_exc()
        return False

def main():
    """Main function"""
    from drugs.drug_database import DRUG_DATABASE
    
    print("=" * 80)
    print("BATCH ADD MISSING FIELDS - SMART MODE")
    print("=" * 80)
    
    # Process contraindications_detail first (can copy from contraindications)
    print("\n1. Processing contraindications_detail...")
    processed = 0
    for drug_name, drug_data in list(DRUG_DATABASE.items())[:10]:  # Test with first 10
        if drug_data is None or not isinstance(drug_data, dict):
            continue
        
        if "contraindications_detail" in drug_data and drug_data["contraindications_detail"]:
            continue
        
        file_path = find_drug_file_location(drug_name)
        if file_path:
            if add_contraindications_detail_from_existing(drug_data, file_path, drug_name):
                processed += 1
                print(f"  ✓ Added contraindications_detail to {drug_name}")
    
    print(f"\nProcessed {processed} drugs")
    print("\nNote: This is a test run. Review changes before processing all drugs.")

if __name__ == '__main__':
    main()
