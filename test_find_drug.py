"""Test tìm drug file"""
import re
from pathlib import Path

def find_drug_section(content: str, drug_name: str):
    """Tìm vị trí của một thuốc trong content"""
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

# Test với Gentamicin
file_path = Path("drugs/drug_modules/antimicrobial/antibiotics/aminoglycosides.py")
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

drug_name = "Gentamicin"
pattern = rf'["\']{re.escape(drug_name)}["\']\s*:\s*\{{'
match = re.search(pattern, content)
print(f"Pattern match: {match is not None}")

if match:
    print(f"Match position: {match.start()}-{match.end()}")
    print(f"Match text: {content[match.start():match.end()+50]}")
    
    drug_start, drug_end = find_drug_section(content, drug_name)
    print(f"Drug section: {drug_start} - {drug_end}")
    
    if drug_start is not None:
        drug_section = content[drug_start:drug_end]
        print(f"Has 'group': {'\"group\"' in drug_section}")
        print(f"Has 'vietnamese_name': {'\"vietnamese_name\"' in drug_section}")
        print(f"\nFirst 200 chars of section:\n{drug_section[:200]}")

