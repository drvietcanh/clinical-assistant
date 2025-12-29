"""
Final comprehensive script to fix all syntax errors
Fixes: ] or } followed by "field" without comma
"""
import re
from pathlib import Path

def fix_syntax_errors(file_path):
    """Fix all missing comma patterns"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        original = content
        
        # Pattern 1: ] followed by spaces and "field" or 'field' (same line)
        content = re.sub(r'(\])\s+(["\'](?:drug_interactions|overdose_management|reversal_agents|administration_instructions|pregnancy_lactation|hepatic_adjustment|contraindications|black_box_warnings|guideline_tags|references|renal_adjustment)["\']\s*:)', r'\1,\n        \2', content)
        
        # Pattern 2: } followed by spaces and "field" or 'field' (same line)
        content = re.sub(r'(\})\s+(["\'](?:drug_interactions|overdose_management|reversal_agents|administration_instructions|pregnancy_lactation|hepatic_adjustment|contraindications|black_box_warnings|guideline_tags|references|renal_adjustment)["\']\s*:)', r'\1,\n        \2', content)
        
        # Pattern 3: ] or } on line, then "field" on next line (no comma)
        content = re.sub(r'(\]|\})\s*\n\s*(["\'](?:drug_interactions|overdose_management|reversal_agents|administration_instructions|pregnancy_lactation|hepatic_adjustment|contraindications|black_box_warnings|guideline_tags|references|renal_adjustment)["\']\s*:)', r'\1,\n        \2', content)
        
        if content != original:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
            return True
        return False
    except Exception as e:
        print(f"Error: {file_path}: {e}")
        return False

# Process all Python files
base_path = Path("drugs/drug_modules")
fixed = []

for py_file in base_path.rglob("*.py"):
    if py_file.name == "__init__.py" or py_file.name.endswith(".backup"):
        continue
    
    if fix_syntax_errors(py_file):
        fixed.append(str(py_file))
        print(f"Fixed: {py_file}")

print(f"\nTotal fixed: {len(fixed)} files")

