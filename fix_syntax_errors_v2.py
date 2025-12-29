"""
Script to find and fix syntax errors - version 2
Fixes missing commas after guideline_tags, references, etc.
"""
import re
from pathlib import Path

def fix_missing_commas(file_path):
    """Fix missing commas after dict/list blocks"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        original_content = content
        
        # Pattern 1: ] or } followed by "field_name" without comma
        # Match: ] or } on line, then "field" on next line
        patterns = [
            # guideline_tags ] followed by "black_box_warnings"
            (r'(\])\s*\n\s*("black_box_warnings":)', r'\1,\n        \2'),
            # guideline_tags ] followed by 'black_box_warnings'  
            (r'(\])\s*\n\s*(\'black_box_warnings\':)', r'\1,\n        \2'),
            # references } followed by "field"
            (r'(\})\s*\n\s*("(?:drug_interactions|overdose_management|reversal_agents|administration_instructions|pregnancy_lactation|hepatic_adjustment|contraindications|black_box_warnings|guideline_tags)":)', r'\1,\n        \2'),
            # references } followed by 'field'
            (r'(\})\s*\n\s*(\'(?:drug_interactions|overdose_management|reversal_agents|administration_instructions|pregnancy_lactation|hepatic_adjustment|contraindications|black_box_warnings|guideline_tags)\':)', r'\1,\n        \2'),
            # ] followed by "field" on same line (no newline)
            (r'(\])\s+("(?:black_box_warnings|drug_interactions|overdose_management)":)', r'\1,\n        \2'),
            (r'(\])\s+(\'(?:black_box_warnings|drug_interactions|overdose_management)\':)', r'\1,\n        \2'),
        ]
        
        for pattern, replacement in patterns:
            content = re.sub(pattern, replacement, content, flags=re.MULTILINE)
        
        if content != original_content:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
            return True
        return False
    except Exception as e:
        print(f"Error processing {file_path}: {e}")
        return False

# Find all Python files
base_path = Path("drugs/drug_modules")
fixed_files = []

for py_file in base_path.rglob("*.py"):
    if py_file.name == "__init__.py" or py_file.name.endswith(".backup"):
        continue
    
    if fix_missing_commas(py_file):
        fixed_files.append(str(py_file))
        print(f"Fixed: {py_file}")

print(f"\nFixed {len(fixed_files)} files")

