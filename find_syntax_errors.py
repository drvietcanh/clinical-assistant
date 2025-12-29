"""
Script to find all remaining syntax errors in drug modules
"""
import ast
import sys
from pathlib import Path

def check_syntax(file_path):
    """Check if file has syntax errors"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Try to parse
        try:
            ast.parse(content)
            return None  # No error
        except SyntaxError as e:
            return {
                'file': str(file_path),
                'line': e.lineno,
                'offset': e.offset,
                'message': e.msg,
                'text': e.text
            }
    except Exception as e:
        return {
            'file': str(file_path),
            'error': str(e)
        }

# Find all Python files
base_path = Path("drugs/drug_modules")
errors = []

print("Dang kiem tra syntax errors...\n")

for py_file in sorted(base_path.rglob("*.py")):
    if py_file.name == "__init__.py" or py_file.name.endswith(".backup"):
        continue
    
    result = check_syntax(py_file)
    if result:
        errors.append(result)
        print(f"ERROR: {result['file']}")
        if 'line' in result:
            print(f"  Line {result['line']}, offset {result['offset']}: {result['message']}")
            if result['text']:
                print(f"  Text: {result['text'].strip()}")
        else:
            print(f"  Error: {result.get('error', 'Unknown')}")
        print()

print(f"\nTong cong: {len(errors)} file co loi syntax")

if errors:
    print("\nDanh sach file co loi:")
    for err in errors:
        print(f"  - {err['file']}")
