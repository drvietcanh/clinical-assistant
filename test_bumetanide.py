"""Test tìm Bumetanide"""
import re
from pathlib import Path

def find_drug_section(content: str, drug_name: str):
    pattern = rf'["\']{re.escape(drug_name)}["\']\s*:\s*\{{'
    match = re.search(pattern, content)
    
    if not match:
        return None, None
    
    start_pos = match.end() - 1
    brace_count = 0
    in_string = False
    string_char = None
    i = start_pos
    
    while i < len(content):
        char = content[i]
        
        if char in ['"', "'"]:
            if i > 0 and content[i-1] == '\\':
                i += 1
                continue
            
            if not in_string:
                in_string = True
                string_char = char
            elif char == string_char:
                in_string = False
                string_char = None
        
        if not in_string:
            if char == '{':
                brace_count += 1
            elif char == '}':
                brace_count -= 1
                if brace_count == 0:
                    return start_pos, i + 1
        
        i += 1
    
    return None, None

def find_drug_file(drug_name: str):
    base_path = Path("drugs/drug_modules")
    
    for py_file in sorted(base_path.rglob("*.py")):
        if py_file.name == "__init__.py" or py_file.name.endswith(".backup"):
            continue
        
        try:
            with open(py_file, 'r', encoding='utf-8') as f:
                content = f.read()
            
            pattern = rf'["\']{re.escape(drug_name)}["\']\s*:\s*\{{'
            if not re.search(pattern, content):
                continue
            
            drug_start, drug_end = find_drug_section(content, drug_name)
            if drug_start is None:
                continue
            
            drug_section = content[drug_start:drug_end]
            if '"group"' in drug_section or '"vietnamese_name"' in drug_section:
                print(f"Found {drug_name} in {py_file}")
                return py_file
        except Exception as e:
            print(f"Error in {py_file}: {e}")
    
    return None

# Test
result = find_drug_file("Bumetanide")
print(f"Result: {result}")

