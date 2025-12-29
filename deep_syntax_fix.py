"""
Deep syntax fixer - examines files character by character to fix issues
"""
import ast
import re
from pathlib import Path

def examine_line_structure(file_path, target_line=None):
    """Examine line structure in detail"""
    with open(file_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    
    print(f"\nExamining {file_path}:")
    start = max(0, (target_line or 1) - 5)
    end = min(len(lines), (target_line or len(lines)) + 5)
    
    for i in range(start, end):
        line = lines[i]
        line_num = i + 1
        indent = len(line) - len(line.lstrip())
        stripped = line.rstrip()
        blank = not stripped
        
        # Show special characters
        special_chars = []
        for char in line:
            if char == ' ':
                special_chars.append('·')
            elif char == '\t':
                special_chars.append('→')
            elif char == '\n':
                special_chars.append('↵')
            else:
                special_chars.append(char)
        
        marker = " <-- ERROR" if line_num == target_line else ""
        print(f"Line {line_num:3d} [{indent:2d} spaces]: {repr(line[:80])}{marker}")
        if blank and indent > 0:
            print(f"         WARNING: Blank line with {indent} spaces of indentation!")

def fix_file_deep(file_path):
    """Deep fix for syntax errors"""
    with open(file_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    
    original_lines = lines.copy()
    fixed = False
    
    # Step 1: Remove ALL whitespace from blank lines
    new_lines = []
    for i, line in enumerate(lines):
        if not line.strip():  # Blank line
            # Check if it has any whitespace
            if len(line.rstrip()) > 0:
                new_lines.append('\n')
                fixed = True
                print(f"  Fixed line {i+1}: Removed whitespace from blank line")
            else:
                new_lines.append(line)
        else:
            new_lines.append(line)
    
    lines = new_lines
    
    # Step 2: Fix indentation of dictionary entries
    # Find all dictionary key entries and ensure consistent indentation
    for i in range(len(lines)):
        line = lines[i]
        
        # Check if this is a dictionary key entry (like "DrugName": {)
        if re.match(r'^\s+["\'][^"\']+["\']\s*:\s*\{', line):
            # This is a dictionary entry
            current_indent = len(line) - len(line.lstrip())
            
            # Check previous lines to determine correct indentation
            if i > 0:
                # Look backwards for the previous dictionary entry or opening brace
                for j in range(i-1, max(0, i-20), -1):
                    prev_line = lines[j]
                    
                    # If we find a previous dictionary entry
                    if re.match(r'^\s+["\'][^"\']+["\']\s*:\s*\{', prev_line):
                        prev_indent = len(prev_line) - len(prev_line.lstrip())
                        if current_indent != prev_indent:
                            # Fix indentation
                            stripped = line.lstrip()
                            lines[i] = ' ' * prev_indent + stripped
                            fixed = True
                            print(f"  Fixed line {i+1}: Adjusted indentation from {current_indent} to {prev_indent} spaces")
                        break
                    
                    # If we find the opening brace of the main dictionary
                    if re.match(r'^\s*[A-Z_]+\s*=\s*\{', prev_line):
                        # This is the main dict, entries should be at 4 spaces
                        if current_indent != 4:
                            stripped = line.lstrip()
                            lines[i] = ' ' * 4 + stripped
                            fixed = True
                            print(f"  Fixed line {i+1}: Adjusted indentation to 4 spaces (main dict level)")
                        break
    
    # Step 3: Fix missing commas
    content = ''.join(lines)
    original_content = content
    
    # Pattern: closing brace/bracket followed by newline and field name
    patterns = [
        (r'(\})\s*\n\s*(["\'](?:drug_interactions|overdose_management|reversal_agents|administration_instructions|pregnancy_lactation|hepatic_adjustment|contraindications|black_box_warnings|guideline_tags|references|renal_adjustment|group|vietnamese_name|administration|indications|contraindications|dosage|side_effects|interactions|pregnancy|mechanism_of_action|monitoring|precautions|pharmacokinetics|storage)["\']\s*:)', r'\1,\n        \2'),
        (r'(\])\s*\n\s*(["\'](?:drug_interactions|overdose_management|reversal_agents|administration_instructions|pregnancy_lactation|hepatic_adjustment|contraindications|black_box_warnings|guideline_tags|references|renal_adjustment|group|vietnamese_name|administration|indications|contraindications|dosage|side_effects|interactions|pregnancy|mechanism_of_action|monitoring|precautions|pharmacokinetics|storage)["\']\s*:)', r'\1,\n        \2'),
    ]
    
    for pattern, replacement in patterns:
        new_content = re.sub(pattern, replacement, content)
        if new_content != content:
            content = new_content
            fixed = True
            print(f"  Fixed: Added missing comma after closing brace/bracket")
    
    # Step 4: Validate
    try:
        ast.parse(content)
        if fixed:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
            return True, "Fixed successfully"
        else:
            return False, "No issues found"
    except SyntaxError as e:
        # Show the problematic area
        lines_list = content.splitlines()
        error_line = e.lineno - 1 if e.lineno <= len(lines_list) else len(lines_list) - 1
        print(f"\n  Syntax error still present at line {e.lineno}:")
        print(f"    {e.msg}")
        if error_line >= 0:
            print(f"    Line content: {repr(lines_list[error_line][:100])}")
            if error_line > 0:
                print(f"    Previous line: {repr(lines_list[error_line-1][:100])}")
            if error_line < len(lines_list) - 1:
                print(f"    Next line: {repr(lines_list[error_line+1][:100])}")
        
        return False, f"Syntax error: {e.msg} at line {e.lineno}"

def main():
    """Main function"""
    base_path = Path("drugs/drug_modules")
    
    # Find files with syntax errors
    error_files = []
    for py_file in sorted(base_path.rglob("*.py")):
        if py_file.name == "__init__.py" or py_file.name.endswith(".backup"):
            continue
        
        try:
            with open(py_file, 'r', encoding='utf-8') as f:
                content = f.read()
            ast.parse(content)
        except SyntaxError as e:
            error_files.append((py_file, e.lineno))
    
    if not error_files:
        print("No syntax errors found!")
        return
    
    print(f"Found {len(error_files)} file(s) with syntax errors\n")
    print("=" * 70)
    
    for file_path, error_line in error_files:
        print(f"\n{'='*70}")
        print(f"File: {file_path}")
        print(f"Error at line: {error_line}")
        print(f"{'='*70}")
        
        # Examine the problematic area
        examine_line_structure(file_path, error_line)
        
        # Try to fix
        print(f"\nAttempting to fix...")
        fixed, message = fix_file_deep(file_path)
        
        if fixed:
            print(f"✓ {message}")
            # Verify
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                ast.parse(content)
                print(f"✓ Verified: No syntax errors remaining")
            except SyntaxError as e2:
                print(f"✗ Still has error: {e2.msg} at line {e2.lineno}")
        else:
            print(f"✗ {message}")

if __name__ == "__main__":
    main()

