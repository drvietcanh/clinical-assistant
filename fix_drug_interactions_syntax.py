"""
Script to fix drug_interactions syntax errors in drug module files.
Fixes the pattern: }], 'mechanism': to }], 'moderate': [
"""
import os
import re
import glob

def fix_file(filepath):
    """Fix drug_interactions syntax in a file"""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    original_content = content
    
    # Pattern 1: }], 'mechanism': (should be }], 'moderate': [)
    # But we need to be careful - we need to check if it's inside drug_interactions
    # and wrap the following interactions properly
    
    # Find all occurrences of }], 'mechanism': that appear after 'major': [...]
    pattern = r"(\}\],\s*)'mechanism':"
    
    def replace_func(match):
        # Check if this is inside a drug_interactions structure
        # by looking backwards for 'major': [
        before = content[:match.start()]
        # Find the last occurrence of 'major': [ before this
        major_pos = before.rfind("'major': [")
        if major_pos == -1:
            major_pos = before.rfind('"major": [')
        
        if major_pos != -1:
            # This is likely a drug_interactions structure
            # Replace with 'moderate': [
            return match.group(1) + "'moderate': ["
        else:
            # Not sure, return as is
            return match.group(0)
    
    content = re.sub(pattern, replace_func, content)
    
    # Now we need to wrap the interactions that follow into proper dict format
    # This is more complex, so let's do a simpler fix:
    # Replace }], 'mechanism': with }], 'moderate': [
    # Then manually check each file
    
    if content != original_content:
        # Backup
        backup_path = filepath + '.backup_syntax_fix'
        with open(backup_path, 'w', encoding='utf-8') as f:
            f.write(original_content)
        
        # Write fixed content
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        
        print(f"Fixed: {filepath}")
        return True
    return False

# Find all files with the pattern
files_to_fix = []
for root, dirs, files in os.walk('drugs/drug_modules'):
    for file in files:
        if file.endswith('.py'):
            filepath = os.path.join(root, file)
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
                if "}], 'mechanism':" in content:
                    files_to_fix.append(filepath)

print(f"Found {len(files_to_fix)} files to fix")

# Fix each file (but this script needs manual review for each)
# For now, let's just fix the immediate blocker
if files_to_fix:
    print("\nFiles that need fixing:")
    for f in files_to_fix:
        print(f"  - {f}")
    print("\nNote: This script provides a starting point, but each file may need manual review.")




