"""
Comprehensive syntax fixer - finds and fixes all types of syntax errors
Approach: Multiple strategies combined for thorough fixing
"""
import ast
import re
from pathlib import Path

def fix_all_syntax_errors():
    """Comprehensive fix for all syntax errors using multiple strategies"""
    base_path = Path("drugs/drug_modules")
    fixed_files = []
    
    print("Comprehensive syntax error fixing...\n")
    print("Strategy 1: Finding all files with syntax errors\n")
    
    # Step 1: Find all files with syntax errors
    error_files = []
    for py_file in sorted(base_path.rglob("*.py")):
        if py_file.name == "__init__.py" or py_file.name.endswith(".backup"):
            continue
        
        try:
            with open(py_file, 'r', encoding='utf-8') as f:
                content = f.read()
            ast.parse(content)
        except SyntaxError as e:
            error_files.append((py_file, e))
    
    if not error_files:
        print("✓ No syntax errors found!")
        return
    
    print(f"Found {len(error_files)} file(s) with syntax errors\n")
    print("=" * 70)
    
    # Step 2: Fix each file using multiple strategies
    for file_path, error in error_files:
        print(f"\nFile: {file_path}")
        print(f"Error: {error.msg} at line {error.lineno}")
        print("-" * 70)
        
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
            lines = f.readlines()
        
        original_content = content
        fixed = False
        
        # Strategy 1: Remove whitespace from blank lines
        new_lines = []
        for i, line in enumerate(lines):
            if not line.strip() and len(line.rstrip()) > 0:
                new_lines.append('\n')
                fixed = True
            else:
                new_lines.append(line)
        
        if fixed:
            content = ''.join(new_lines)
            lines = new_lines
            print("  ✓ Removed whitespace from blank lines")
        
        # Strategy 2: Fix closing brace + comma on separate lines
        # Pattern: } on one line, }, on next line -> combine to },
        content = re.sub(r'(\})\s*\n\s*(\},)', r'\2\n', content)
        if content != ''.join(lines):
            fixed = True
            print("  ✓ Combined closing brace and comma")
            lines = content.splitlines(keepends=True)
        
        # Strategy 3: Fix missing commas after closing braces/brackets
        patterns = [
            (r'(\})\s*\n\s*(["\'](?:drug_interactions|overdose_management|reversal_agents|administration_instructions|pregnancy_lactation|hepatic_adjustment|contraindications|black_box_warnings|guideline_tags|references|renal_adjustment|group|vietnamese_name|administration|indications|contraindications|dosage|side_effects|interactions|pregnancy|mechanism_of_action|monitoring|precautions|pharmacokinetics|storage)["\']\s*:)', r'\1,\n        \2'),
            (r'(\])\s*\n\s*(["\'](?:drug_interactions|overdose_management|reversal_agents|administration_instructions|pregnancy_lactation|hepatic_adjustment|contraindications|black_box_warnings|guideline_tags|references|renal_adjustment|group|vietnamese_name|administration|indications|contraindications|dosage|side_effects|interactions|pregnancy|mechanism_of_action|monitoring|precautions|pharmacokinetics|storage)["\']\s*:)', r'\1,\n        \2'),
        ]
        
        for pattern, replacement in patterns:
            new_content = re.sub(pattern, replacement, content)
            if new_content != content:
                content = new_content
                fixed = True
                print("  ✓ Added missing commas after closing braces/brackets")
        
        # Strategy 4: Fix dictionary entry indentation
        # Ensure all dictionary entries at the same level have the same indentation
        new_lines = content.splitlines(keepends=True)
        dict_entry_pattern = re.compile(r'^\s+["\'][^"\']+["\']\s*:\s*\{')
        
        for i in range(len(new_lines)):
            line = new_lines[i]
            if dict_entry_pattern.match(line):
                # Find the main dictionary declaration
                for j in range(max(0, i-10), i):
                    if re.match(r'^\s*[A-Z_]+\s*=\s*\{', new_lines[j]):
                        # This is the main dict, entries should be at 4 spaces
                        current_indent = len(line) - len(line.lstrip())
                        if current_indent != 4:
                            stripped = line.lstrip()
                            new_lines[i] = '    ' + stripped
                            fixed = True
                            print(f"  ✓ Fixed indentation at line {i+1}")
                        break
        
        if fixed:
            content = ''.join(new_lines)
        
        # Step 3: Validate and save
        try:
            ast.parse(content)
            if content != original_content:
                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write(content)
                print(f"  ✓ File fixed and saved")
                fixed_files.append(file_path)
            else:
                print(f"  - No changes needed (error may be elsewhere)")
        except SyntaxError as e2:
            print(f"  ✗ Still has syntax error: {e2.msg} at line {e2.lineno}")
            print(f"    Manual inspection may be needed")
    
    # Final verification
    print("\n" + "=" * 70)
    print("Final verification...\n")
    
    remaining_errors = []
    for py_file in sorted(base_path.rglob("*.py")):
        if py_file.name == "__init__.py" or py_file.name.endswith(".backup"):
            continue
        
        try:
            with open(py_file, 'r', encoding='utf-8') as f:
                content = f.read()
            ast.parse(content)
        except SyntaxError as e:
            remaining_errors.append((py_file, e))
    
    if remaining_errors:
        print(f"✗ {len(remaining_errors)} file(s) still have syntax errors:")
        for file_path, error in remaining_errors:
            print(f"  - {file_path}: {error.msg} at line {error.lineno}")
    else:
        print(f"✓ All syntax errors fixed! ({len(fixed_files)} file(s) modified)")

if __name__ == "__main__":
    fix_all_syntax_errors()

