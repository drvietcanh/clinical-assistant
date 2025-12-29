"""
Fix indent errors caused by blank lines with indentation
"""
import re
from pathlib import Path

def fix_indent_errors(file_path):
    """Fix indent errors"""
    with open(file_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    
    fixed = False
    new_lines = []
    
    for i, line in enumerate(lines):
        # Check if this is a blank line with indentation before a dict key
        if i < len(lines) - 1:
            next_line = lines[i + 1]
            # If current line is blank with spaces, and next line starts with "key": {
            if re.match(r'^\s+$', line) and re.match(r'^\s+"[^"]+":\s*\{', next_line):
                # Remove the blank line
                fixed = True
                continue
        
        new_lines.append(line)
    
    if fixed:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.writelines(new_lines)
        return True
    return False

# Fix both files
files = [
    "drugs/drug_modules/antimicrobial/antibiotics/aminoglycosides.py",
    "drugs/drug_modules/respiratory/short_acting_beta_2_agonist_sabas.py"
]

for file_path in files:
    if fix_indent_errors(file_path):
        print(f"Fixed: {file_path}")

