"""
Fix all remaining syntax errors - find and fix all patterns
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
        
        # Fix pattern: ] text" (leftover text after closing bracket)
        pattern1 = r'(\]\s*)([^"\n]+)"'
        def repl1(m):
            if 'guideline_tags' in content[max(0, content.find(m.group(0))-200):content.find(m.group(0))+50]:
                changes.append("Fixed leftover text after guideline_tags")
                return m.group(1) + '\n'
            return m.group(0)
        content = re.sub(pattern1, repl1, content)
        
        # Fix pattern: missing comma after guideline_tags closing bracket before evidence_level
        pattern2 = r'(\]\s*)\n\s*"evidence_level"'
        if re.search(pattern2, content):
            content = re.sub(pattern2, r'\1,\n            "evidence_level"', content)
            changes.append("Fixed missing comma after guideline_tags")
        
        if content != original_content:
            # Create backup
            backup_path = str(file_path) + ".final_fix_backup"
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
    """Fix all remaining syntax errors"""
    drugs_dir = Path("drugs/drug_modules")
    
    fixed_files = []
    
    for file_path in sorted(drugs_dir.rglob("*.py")):
        if file_path.name == "__init__.py" or file_path.name.endswith(".backup"):
            continue
        
        success, changes = fix_file(file_path)
        if success:
            fixed_files.append((str(file_path), changes))
            print(f"✅ Fixed: {file_path.name} - {', '.join(changes)}")
    
    print(f"\nFixed {len(fixed_files)} files")

if __name__ == "__main__":
    main()

