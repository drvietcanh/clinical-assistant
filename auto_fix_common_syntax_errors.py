"""
Script to automatically fix common syntax errors in drug_modules files
"""
import os
import re
import shutil
from pathlib import Path

def fix_file(filepath):
    """Fix common syntax errors in a file"""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        original_content = content
        changes = []
        
        # Fix 1: Missing 'indications': key before list
        # Pattern: 'administration': [...],\n        'string1', 'string2', ...], 'contraindications':
        pattern1 = r"('administration':\s*\[[^\]]+\],\s*\n\s*)'([^']+)',\s*'([^']+)'"
        if re.search(pattern1, content):
            # Try to find and fix missing 'indications': key
            lines = content.split('\n')
            for i, line in enumerate(lines):
                if "'administration':" in line and i + 1 < len(lines):
                    next_line = lines[i + 1]
                    if next_line.strip().startswith("'") and "'indications':" not in content[max(0, i-5):i+5]:
                        # Check if this looks like indications
                        if any(keyword in next_line for keyword in ['Thiếu', 'Bệnh', 'Dự phòng', 'Sau phẫu thuật']):
                            # Find where the list ends
                            for j in range(i+1, min(i+10, len(lines))):
                                if "], 'contraindications':" in lines[j]:
                                    # Insert 'indications': before the first string
                                    lines[j] = lines[j].replace("], 'contraindications':", "], 'indications': [")
                                    # Find the closing bracket and add it before contraindications
                                    for k in range(j-1, max(i, j-10), -1):
                                        if lines[k].strip().endswith("'") and not lines[k].strip().startswith("'"):
                                            # This is likely the last item in the list
                                            lines[k] = lines[k].rstrip() + "], 'contraindications':"
                                            break
                                    content = '\n'.join(lines)
                                    changes.append("Fixed missing 'indications': key")
                                    break
                            break
        
        # Fix 2: Missing 'drug': key in drug_interactions
        # Pattern: }], 'mechanism': (should be }, {'drug': '...', 'mechanism':)
        pattern2 = r"(\}\],\s*)'mechanism':"
        if re.search(pattern2, content):
            content = re.sub(
                pattern2,
                r"\1{'drug': 'Unknown', 'mechanism':",
                content
            )
            changes.append("Fixed missing 'drug': key in drug_interactions")
        
        # Fix 3: Extra closing braces
        # Count braces and fix if unbalanced
        open_braces = content.count('{')
        close_braces = content.count('}')
        
        if close_braces > open_braces:
            # Try to find and remove extra closing braces at the end
            lines = content.split('\n')
            # Check last few lines for extra }
            for i in range(len(lines)-1, max(len(lines)-5, 0), -1):
                if lines[i].strip() == '}' and close_braces > open_braces:
                    # Check if removing this would balance
                    test_content = '\n'.join(lines[:i] + lines[i+1:])
                    if test_content.count('{') == test_content.count('}'):
                        content = test_content
                        changes.append("Removed extra closing brace")
                        break
        
        if content != original_content:
            # Create backup
            backup_path = filepath + '.auto_fix_backup'
            shutil.copy2(filepath, backup_path)
            
            # Write fixed content
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)
            
            return True, changes
        else:
            return False, []
    
    except Exception as e:
        return False, [f"Error: {str(e)}"]

def main():
    """Main function"""
    drug_modules_dir = Path("drugs/drug_modules")
    fixed_count = 0
    error_count = 0
    
    print("Auto-fixing common syntax errors...")
    print("=" * 60)
    
    for py_file in drug_modules_dir.rglob("*.py"):
        if py_file.name.endswith('.backup') or py_file.name.endswith('.pyc'):
            continue
        
        fixed, changes = fix_file(str(py_file))
        if fixed:
            fixed_count += 1
            print(f"\n✅ Fixed: {py_file}")
            for change in changes:
                print(f"   - {change}")
        elif changes and "Error" in changes[0]:
            error_count += 1
            print(f"\n❌ Error in {py_file}: {changes[0]}")
    
    print("\n" + "=" * 60)
    print(f"Fixed: {fixed_count} files")
    if error_count > 0:
        print(f"Errors: {error_count} files")
    print("\nNote: Backups created with .auto_fix_backup extension")

if __name__ == "__main__":
    main()
