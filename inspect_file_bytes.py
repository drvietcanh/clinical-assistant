"""
Inspect file byte by byte to find the exact issue
"""
from pathlib import Path

file_path = Path("drugs/drug_modules/respiratory/short_acting_beta_2_agonist_sabas.py")

with open(file_path, 'rb') as f:
    raw_bytes = f.read()

with open(file_path, 'r', encoding='utf-8') as f:
    lines = f.readlines()

print("Inspecting lines 43-48:\n")
for i in range(42, min(48, len(lines))):
    line = lines[i]
    line_num = i + 1
    print(f"Line {line_num}:")
    print(f"  Raw bytes: {raw_bytes[sum(len(lines[j].encode('utf-8')) for j in range(i)):sum(len(lines[j].encode('utf-8')) for j in range(i+1))]}")
    print(f"  Repr: {repr(line)}")
    print(f"  Stripped length: {len(line.rstrip())}")
    print(f"  Leading spaces: {len(line) - len(line.lstrip())}")
    print(f"  Is blank: {not line.strip()}")
    print()

# Check specifically for blank lines with indentation between 45 and 46
if len(lines) > 45:
    line_45 = lines[44]  # 0-indexed
    line_46 = lines[45]  # 0-indexed
    
    print("Checking between line 45 and 46:")
    print(f"Line 45 ends with: {repr(line_45[-10:])}")
    print(f"Line 46 starts with: {repr(line_46[:20])}")
    
    # Check if there are any lines between them (shouldn't be, but check)
    # Actually, they're consecutive, so check the raw structure
    
    # Find the exact position in the file
    pos_45_end = sum(len(lines[i].encode('utf-8')) for i in range(45))
    pos_46_start = pos_45_end
    
    print(f"\nByte positions:")
    print(f"  After line 45: position {pos_45_end}")
    print(f"  Line 46 starts: position {pos_46_start}")
    print(f"  Bytes between: {raw_bytes[pos_45_end:pos_46_start+50]}")

