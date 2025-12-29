"""
Script to find and fix syntax errors in drug modules
Finds missing commas after "references": {...}
"""
import re
from pathlib import Path

def find_and_fix_references_errors(file_path):
    """Find and fix missing comma after references"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        original_content = content
        
        # Pattern: "references": {...} followed by " (without comma)
        # Look for: "references": { ... } followed by newline and then "field_name"
        pattern = r'("references":\s*\{[^}]*\})\s*\n\s*("(?:drug_interactions|overdose_management|reversal_agents|administration_instructions|pregnancy_lactation|hepatic_adjustment|contraindications|black_box_warnings)":)'
        
        def add_comma(match):
            references_block = match.group(1)
            next_field = match.group(2)
            return references_block + ',\n        ' + next_field
        
        content = re.sub(pattern, add_comma, content, flags=re.MULTILINE | re.DOTALL)
        
        # Also check for pattern: } followed by "field" on next line
        pattern2 = r'(\})\s*\n\s*("(?:drug_interactions|overdose_management|reversal_agents|administration_instructions|pregnancy_lactation|hepatic_adjustment|contraindications|black_box_warnings|guideline_tags)":)'
        
        def add_comma2(match):
            closing_brace = match.group(1)
            next_field = match.group(2)
            # Check if this is part of references block
            if '"references"' in content[max(0, content.rfind('"references"', 0, match.start())):match.start()]:
                return closing_brace + ',\n        ' + next_field
            return match.group(0)
        
        content = re.sub(pattern2, add_comma2, content, flags=re.MULTILINE)
        
        if content != original_content:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
            return True
        return False
    except Exception as e:
        print(f"Error processing {file_path}: {e}")
        return False

# Find all Python files in drug_modules
base_path = Path("drugs/drug_modules")
fixed_files = []

for py_file in base_path.rglob("*.py"):
    if py_file.name == "__init__.py" or py_file.name.endswith(".backup"):
        continue
    
    if find_and_fix_references_errors(py_file):
        fixed_files.append(str(py_file))
        print(f"Fixed: {py_file}")

print(f"\nFixed {len(fixed_files)} files")
if fixed_files:
    print("Files fixed:")
    for f in fixed_files:
        print(f"  - {f}")

