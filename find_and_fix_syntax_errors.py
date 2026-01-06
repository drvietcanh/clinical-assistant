"""
Script to find all Python files with syntax errors in drug_modules
"""
import os
import subprocess
import sys

def find_syntax_errors():
    """Find all Python files with syntax errors"""
    drug_modules_dir = "drugs/drug_modules"
    errors = []
    
    for root, dirs, files in os.walk(drug_modules_dir):
        for file in files:
            if file.endswith('.py') and not file.endswith('.backup') and not file.endswith('.pyc'):
                filepath = os.path.join(root, file)
                try:
                    result = subprocess.run(
                        [sys.executable, '-m', 'py_compile', filepath],
                        capture_output=True,
                        text=True,
                        timeout=5
                    )
                    if result.returncode != 0:
                        errors.append((filepath, result.stderr))
                except Exception as e:
                    errors.append((filepath, str(e)))
    
    return errors

if __name__ == "__main__":
    print("Finding syntax errors in drug_modules...")
    errors = find_syntax_errors()
    
    if errors:
        print(f"\nFound {len(errors)} files with syntax errors:\n")
        for filepath, error in errors:
            print(f"{filepath}:")
            print(f"  {error.split(chr(10))[0] if error else 'Unknown error'}")
            print()
    else:
        print("No syntax errors found!")
