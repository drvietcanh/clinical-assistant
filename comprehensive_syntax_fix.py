"""
Comprehensive syntax error fixer - fixes all types of syntax errors systematically
"""
import ast
import re
from pathlib import Path

def analyze_file_structure(file_path):
    """Analyze file structure to understand the issue"""
    with open(file_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    
    issues = []
    for i, line in enumerate(lines, 1):
        # Check for blank lines with indentation
        if not line.strip() and len(line.rstrip()) > 0:
            issues.append(f"Line {i}: Blank line with indentation")
        
        # Check for trailing whitespace before closing braces/brackets
        if re.search(r'[ \t]+$', line) and (line.strip().endswith('}') or line.strip().endswith(']')):
            issues.append(f"Line {i}: Trailing whitespace before closing brace/bracket")
    
    return issues, lines

def fix_indentation_issues(lines):
    """Fix indentation issues systematically"""
    fixed_lines = []
    in_dict = False
    dict_level = 0
    
    for i, line in enumerate(lines):
        original_line = line
        
        # Remove indentation from blank lines
        if not line.strip():
            fixed_lines.append('\n')
            continue
        
        # Check if we're starting a new dictionary entry
        if re.match(r'^\s*"[^"]+":\s*\{', line) or re.match(r"^\s*'[^']+':\s*\{", line):
            # This is a dictionary key, should be at base level (4 spaces) or nested appropriately
            stripped = line.lstrip()
            if stripped.startswith('"') or stripped.startswith("'"):
                # Calculate proper indentation based on context
                # If previous line ended with }, we're at the same level
                if i > 0 and fixed_lines and fixed_lines[-1].strip().endswith('},'):
                    # Same level as previous entry
                    indent_level = len(fixed_lines[-1]) - len(fixed_lines[-1].lstrip())
                    if fixed_lines[-1].strip().endswith('},'):
                        # We're in the same dictionary, same indent
                        proper_indent = ' ' * indent_level
                    else:
                        proper_indent = ' ' * 4  # Default for top-level entries
                else:
                    proper_indent = ' ' * 4  # Default
                
                # Only fix if current indentation is clearly wrong
                current_indent = len(line) - len(line.lstrip())
                if current_indent > 8 and i > 0:  # Suspiciously over-indented
                    line = proper_indent + stripped
                    fixed_lines.append(line)
                    continue
        
        fixed_lines.append(line)
    
    return fixed_lines

def fix_comprehensive(file_path):
    """Comprehensive fix for all syntax issues"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
            lines = f.readlines()
        
        original_content = content
        original_lines = lines.copy()
        fixed = False
        
        # Step 1: Remove indentation from blank lines
        new_lines = []
        for line in lines:
            if not line.strip() and len(line.rstrip()) > 0:
                # Blank line with whitespace - remove it
                new_lines.append('\n')
                fixed = True
            else:
                new_lines.append(line)
        
        if fixed:
            lines = new_lines
            content = ''.join(lines)
        
        # Step 2: Fix missing commas after closing braces/brackets
        # Pattern: } or ] followed by newline and then a field name
        patterns = [
            # } followed by newline and field (missing comma)
            (r'(\})\s*\n\s*(["\'](?:drug_interactions|overdose_management|reversal_agents|administration_instructions|pregnancy_lactation|hepatic_adjustment|contraindications|black_box_warnings|guideline_tags|references|renal_adjustment|group|vietnamese_name|administration|indications|contraindications|dosage|side_effects|interactions|pregnancy|mechanism_of_action|monitoring|precautions|pharmacokinetics|storage)["\']\s*:)', r'\1,\n        \2'),
            # ] followed by newline and field (missing comma)
            (r'(\])\s*\n\s*(["\'](?:drug_interactions|overdose_management|reversal_agents|administration_instructions|pregnancy_lactation|hepatic_adjustment|contraindications|black_box_warnings|guideline_tags|references|renal_adjustment|group|vietnamese_name|administration|indications|contraindications|dosage|side_effects|interactions|pregnancy|mechanism_of_action|monitoring|precautions|pharmacokinetics|storage)["\']\s*:)', r'\1,\n        \2'),
            # } followed by space and field on same line (missing comma)
            (r'(\})\s+(["\'](?:drug_interactions|overdose_management|reversal_agents|administration_instructions|pregnancy_lactation|hepatic_adjustment|contraindications|black_box_warnings|guideline_tags|references|renal_adjustment|group|vietnamese_name|administration|indications|contraindications|dosage|side_effects|interactions|pregnancy|mechanism_of_action|monitoring|precautions|pharmacokinetics|storage)["\']\s*:)', r'\1,\n        \2'),
            # ] followed by space and field on same line (missing comma)
            (r'(\])\s+(["\'](?:drug_interactions|overdose_management|reversal_agents|administration_instructions|pregnancy_lactation|hepatic_adjustment|contraindications|black_box_warnings|guideline_tags|references|renal_adjustment|group|vietnamese_name|administration|indications|contraindications|dosage|side_effects|interactions|pregnancy|mechanism_of_action|monitoring|precautions|pharmacokinetics|storage)["\']\s*:)', r'\1,\n        \2'),
        ]
        
        for pattern, replacement in patterns:
            new_content = re.sub(pattern, replacement, content)
            if new_content != content:
                content = new_content
                fixed = True
        
        # Step 3: Fix dictionary entry indentation issues
        # Look for entries that are over-indented
        lines = content.splitlines(keepends=True)
        new_lines = []
        for i, line in enumerate(lines):
            # Check if this is a dictionary key entry
            if re.match(r'^\s+["\'][^"\']+["\']\s*:\s*\{', line):
                # Check previous line
                if i > 0:
                    prev_line = lines[i-1]
                    # If previous line ends with }, and this is a new entry at same level
                    if prev_line.strip().endswith('},') or prev_line.strip().endswith('}'):
                        # This entry should be at the same indentation as the previous entry
                        # Find the previous entry's indentation
                        prev_entry_indent = None
                        for j in range(i-1, max(0, i-10), -1):
                            if re.match(r'^\s+["\'][^"\']+["\']\s*:\s*\{', lines[j]):
                                prev_entry_indent = len(lines[j]) - len(lines[j].lstrip())
                                break
                        
                        if prev_entry_indent is not None:
                            current_indent = len(line) - len(line.lstrip())
                            if current_indent != prev_entry_indent:
                                # Fix indentation
                                stripped = line.lstrip()
                                line = ' ' * prev_entry_indent + stripped
                                fixed = True
            
            new_lines.append(line)
        
        if fixed:
            content = ''.join(new_lines)
        
        # Step 4: Validate with AST
        try:
            ast.parse(content)
            if content != original_content:
                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write(content)
                return True, "Fixed"
            else:
                return False, "No changes needed"
        except SyntaxError as e:
            # If still has errors, try more aggressive fixes
            return False, f"Still has syntax error: {e.msg} at line {e.lineno}"
    
    except Exception as e:
        return False, f"Error: {str(e)}"

def main():
    """Main function to fix all syntax errors"""
    base_path = Path("drugs/drug_modules")
    
    print("Comprehensive syntax error fixing...\n")
    
    # First, find all files with syntax errors
    error_files = []
    for py_file in sorted(base_path.rglob("*.py")):
        if py_file.name == "__init__.py" or py_file.name.endswith(".backup"):
            continue
        
        try:
            with open(py_file, 'r', encoding='utf-8') as f:
                content = f.read()
            ast.parse(content)
        except SyntaxError:
            error_files.append(py_file)
    
    if not error_files:
        print("No syntax errors found!")
        return
    
    print(f"Found {len(error_files)} file(s) with syntax errors:\n")
    
    for file_path in error_files:
        print(f"Fixing: {file_path}")
        issues, lines = analyze_file_structure(file_path)
        if issues:
            print(f"  Issues found: {len(issues)}")
            for issue in issues[:3]:  # Show first 3
                print(f"    - {issue}")
        
        fixed, message = fix_comprehensive(file_path)
        if fixed:
            print(f"  ✓ {message}")
        else:
            print(f"  ✗ {message}")
        
        # Verify fix
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            ast.parse(content)
            print(f"  ✓ Verified: No syntax errors remaining")
        except SyntaxError as e:
            print(f"  ✗ Still has error: {e.msg} at line {e.lineno}")
        print()

if __name__ == "__main__":
    main()

