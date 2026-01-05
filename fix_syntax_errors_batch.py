"""Script to fix common syntax errors in drug module files"""
import os
import re
from pathlib import Path

def fix_syntax_errors(file_path):
    """Fix common syntax errors in a Python file"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        original_content = content
        
        # Fix 1: ]', -> ],
        content = re.sub(r"\]',", "],", content)
        
        # Fix 2: }]', -> }],
        content = re.sub(r"\}\]',", "}],", content)
        
        # Fix 3: }', -> },
        content = re.sub(r"\}',", "},", content)
        
        # Fix 4: ]', at end of line (not followed by comma or other)
        content = re.sub(r"\]'\s*$", "],", content, flags=re.MULTILINE)
        
        if content != original_content:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
            return True
        return False
    except Exception as e:
        print(f"Error processing {file_path}: {e}")
        return False

def main():
    drug_modules_dir = Path("drugs/drug_modules")
    
    if not drug_modules_dir.exists():
        print(f"Directory {drug_modules_dir} not found")
        return
    
    fixed_count = 0
    error_count = 0
    
    # Find all Python files
    for py_file in drug_modules_dir.rglob("*.py"):
        # Skip backup files
        if ".backup" in str(py_file) or ".fix" in str(py_file):
            continue
        
        try:
            if fix_syntax_errors(py_file):
                print(f"Fixed: {py_file}")
                fixed_count += 1
        except Exception as e:
            print(f"Error with {py_file}: {e}")
            error_count += 1
    
    print(f"\nFixed {fixed_count} files")
    if error_count > 0:
        print(f"Errors: {error_count} files")

if __name__ == "__main__":
    main()

