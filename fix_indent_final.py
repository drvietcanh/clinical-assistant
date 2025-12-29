"""
Fix indent error in short_acting_beta_2_agonist_sabas.py
"""
with open('drugs/drug_modules/respiratory/short_acting_beta_2_agonist_sabas.py', 'r', encoding='utf-8') as f:
    lines = f.readlines()

# Find the problematic line and check context
for i, line in enumerate(lines):
    if i == 45:  # Line 46 (0-indexed)
        print(f"Line {i+1}: {repr(line)}")
        print(f"Line {i}: {repr(lines[i-1])}")
        print(f"Line {i-1}: {repr(lines[i-2])}")
        
        # Check if there's a blank line with spaces before this
        if i > 0 and lines[i-1].strip() == '' and lines[i-1].startswith('    '):
            print("Found blank line with indent before line 46")
            # Remove the blank line
            lines.pop(i-1)
            print("Removed blank line")
            break

with open('drugs/drug_modules/respiratory/short_acting_beta_2_agonist_sabas.py', 'w', encoding='utf-8') as f:
    f.writelines(lines)

print("Fixed!")

