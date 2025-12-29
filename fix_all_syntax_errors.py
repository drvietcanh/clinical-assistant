"""
Comprehensive script to find and fix all syntax errors
Fixes missing commas after dict/list blocks
"""
import re
from pathlib import Path

def fix_all_missing_commas(file_path):
    """Fix all missing comma patterns"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            lines = f.readlines()
        
        original_lines = lines.copy()
        fixed = False
        
        for i in range(len(lines) - 1):
            line = lines[i]
            next_line = lines[i + 1] if i + 1 < len(lines) else ""
            
            # Pattern 1: Line ends with ] or } and next line starts with "field" or 'field' without comma
            if re.search(r'\]\s*$', line) or re.search(r'\}\s*$', line):
                # Check if next line starts with a field name (quoted)
                if re.match(r'\s*["\'](?:drug_interactions|overdose_management|reversal_agents|administration_instructions|pregnancy_lactation|hepatic_adjustment|contraindications|black_box_warnings|guideline_tags|references)["\']\s*:', next_line):
                    # Add comma to current line
                    lines[i] = line.rstrip() + ',\n'
                    fixed = True
            
            # Pattern 2: Line has ] or } followed by "field" on same line
            if re.search(r'(\]|\})\s+["\'](?:drug_interactions|overdose_management|reversal_agents|administration_instructions|pregnancy_lactation|hepatic_adjustment|contraindications|black_box_warnings|guideline_tags|references)["\']\s*:', line):
                lines[i] = re.sub(r'(\]|\})\s+(["\'][^"\']+["\']\s*:)', r'\1,\n        \2', line)
                fixed = True
        
        if fixed:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.writelines(lines)
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
    
    if fix_all_missing_commas(py_file):
        fixed_files.append(str(py_file))
        print(f"Fixed: {py_file}")

print(f"\nTotal fixed: {len(fixed_files)} files")

