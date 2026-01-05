"""
Final comprehensive syntax fix for all drug module files
Fixes all patterns of syntax errors introduced during automated field addition
"""
import re
from pathlib import Path

def fix_file(file_path):
    """Fix all syntax errors in a file"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        original_content = content
        changes = []
        
        # Fix 1: Missing comma after guideline_tags closing bracket before evidence_level
        pattern1 = r'(\]\s*)\n\s*(["\']?)evidence_level'
        if re.search(pattern1, content):
            content = re.sub(pattern1, r'\1,\n            "evidence_level"', content)
            changes.append("Fixed missing comma before evidence_level")
        
        # Fix 2: Text after closing bracket of guideline_tags (leftover text)
        pattern2 = r'(\]\s*)([^"\n\]]+?)(["\']\s*[,\}])'
        def repl2(m):
            # Only fix if it looks like leftover text (not valid Python)
            text = m.group(2).strip()
            if text and not text.startswith('"') and not text.startswith("'"):
                changes.append(f"Fixed leftover text: {text[:30]}")
                return m.group(1) + m.group(3)
            return m.group(0)
        content = re.sub(pattern2, repl2, content)
        
        # Fix 3: Missing comma after guideline_tags before closing brace
        pattern3 = r'(\]\s*)\n\s*(\}\s*\})'
        if re.search(pattern3, content):
            content = re.sub(pattern3, r'\1\n        \2', content)
            changes.append("Fixed missing structure after guideline_tags")
        
        # Fix 4: Unterminated evidence_level strings before risk_flags
        pattern4 = r'"evidence_level":\s*"([^"]*?),([^"]*?)\s*\n\s*"risk_flags"'
        if re.search(pattern4, content):
            content = re.sub(pattern4, r'"evidence_level": "\1,\2",\n            "risk_flags"', content)
            changes.append("Fixed unterminated evidence_level")
        
        # Fix 5: Fix malformed structure like 'evidence_level': 'text'}}
        pattern5 = r"(['\"])evidence_level['\"]:\s*['\"]([^'\"]*?)['\"]\s*\}\}\}"
        if re.search(pattern5, content):
            content = re.sub(pattern5, r'"evidence_level": "\2"\n        }\n    }', content)
            changes.append("Fixed malformed evidence_level structure")
        
        if content != original_content:
            # Create backup
            backup_path = str(file_path) + ".final_syntax_fix_backup"
            with open(backup_path, 'w', encoding='utf-8') as f:
                f.write(original_content)
            
            # Write fixed content
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
            
            return True, changes
        else:
            return False, []
            
    except Exception as e:
        return False, [f"Error: {str(e)}"]

def main():
    """Fix syntax errors in all drug module files"""
    drugs_dir = Path("drugs/drug_modules")
    
    fixed_files = []
    error_files = []
    
    # Focus on files that are likely to have errors
    target_files = [
        "analgesics/opioid_agonists.py",
        "analgesics/nsaids.py",
        "analgesics/opioid_agonist_strongs.py",
        # Add more if needed
    ]
    
    for target in target_files:
        file_path = drugs_dir / target
        if file_path.exists():
            success, changes = fix_file(file_path)
            if success:
                fixed_files.append((str(file_path), changes))
                print(f"✅ Fixed: {file_path.name} - {', '.join(changes)}")
            elif changes and "Error" in changes[0]:
                error_files.append((str(file_path), changes[0]))
                print(f"❌ Error in {file_path.name}: {changes[0]}")
    
    # Also check all files for common patterns
    print("\nScanning all files for syntax errors...")
    for file_path in sorted(drugs_dir.rglob("*.py")):
        if file_path.name == "__init__.py" or file_path.name.endswith(".backup"):
            continue
        
        # Skip if already fixed
        if any(str(file_path).endswith(t) for t in target_files):
            continue
        
        success, changes = fix_file(file_path)
        if success:
            fixed_files.append((str(file_path), changes))
            print(f"✅ Fixed: {file_path.name}")
    
    print(f"\nFixed {len(fixed_files)} files")
    if error_files:
        print(f"Errors in {len(error_files)} files")

if __name__ == "__main__":
    main()

