"""
Direct syntax fix - fixes the specific file with the error
"""
import ast
from pathlib import Path

def fix_short_acting_beta_2_agonist_sabas():
    """Fix the specific syntax error in short_acting_beta_2_agonist_sabas.py"""
    file_path = Path("drugs/drug_modules/respiratory/short_acting_beta_2_agonist_sabas.py")
    
    with open(file_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    
    print(f"Original file has {len(lines)} lines")
    
    # Check for blank lines with indentation
    fixed_lines = []
    for i, line in enumerate(lines, 1):
        # Remove all whitespace from blank lines
        if not line.strip():
            fixed_lines.append('\n')
            if len(line.rstrip()) > 0:
                print(f"  Line {i}: Removed whitespace from blank line")
        else:
            fixed_lines.append(line)
    
    # Write back and test
    content = ''.join(fixed_lines)
    
    # Try to parse
    try:
        ast.parse(content)
        print("✓ File parses correctly after removing blank line whitespace")
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        return True
    except SyntaxError as e:
        print(f"✗ Still has syntax error at line {e.lineno}: {e.msg}")
        print(f"  Problematic line: {repr(content.splitlines()[e.lineno-1][:100])}")
        
        # Try more aggressive fix: check the structure around the error
        lines_list = content.splitlines()
        error_line_idx = e.lineno - 1
        
        if error_line_idx >= 0 and error_line_idx < len(lines_list):
            error_line = lines_list[error_line_idx]
            print(f"\n  Examining area around line {e.lineno}:")
            for i in range(max(0, error_line_idx - 2), min(len(lines_list), error_line_idx + 3)):
                marker = " <-- ERROR" if i == error_line_idx else ""
                print(f"    Line {i+1}: {repr(lines_list[i][:80])}{marker}")
        
        # Try to fix: if line 46 has unexpected indent, maybe it needs to be dedented
        if e.lineno == 46:
            print("\n  Attempting fix: checking if line 46 needs dedentation...")
            # Check what the previous entry looks like
            # Line 7 is "Salbutamol": { at 4 spaces
            # Line 46 should also be at 4 spaces
            # But maybe there's a structural issue
            
            # Let's check if there's a missing comma or extra brace
            # Actually, let me try a different approach: rewrite the problematic section
            new_lines = []
            for i, line in enumerate(lines_list):
                line_num = i + 1
                if line_num == 46:
                    # This is the problematic line
                    # Check if it has too much indentation
                    stripped = line.lstrip()
                    if stripped.startswith('"') or stripped.startswith("'"):
                        # This should be at 4 spaces (same as line 7)
                        new_line = '    ' + stripped
                        if new_line != line:
                            print(f"    Fixed line {line_num}: Adjusted indentation")
                            new_lines.append(new_line)
                        else:
                            new_lines.append(line)
                    else:
                        new_lines.append(line)
                else:
                    new_lines.append(line)
            
            # Try parsing again
            new_content = '\n'.join(new_lines) + '\n' if new_lines else ''
            try:
                ast.parse(new_content)
                print("✓ Fixed by adjusting indentation!")
                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write(new_content)
                return True
            except SyntaxError as e2:
                print(f"✗ Still has error: {e2.msg} at line {e2.lineno}")
        
        return False

if __name__ == "__main__":
    print("Fixing short_acting_beta_2_agonist_sabas.py...\n")
    success = fix_short_acting_beta_2_agonist_sabas()
    
    if success:
        print("\n✓ File fixed successfully!")
        # Verify
        file_path = Path("drugs/drug_modules/respiratory/short_acting_beta_2_agonist_sabas.py")
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            ast.parse(content)
            print("✓ Verified: No syntax errors")
        except SyntaxError as e:
            print(f"✗ Verification failed: {e.msg} at line {e.lineno}")
    else:
        print("\n✗ Could not fix automatically. Manual inspection needed.")

