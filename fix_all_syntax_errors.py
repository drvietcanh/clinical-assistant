"""
Comprehensive fix for all syntax errors in drug files
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
        
        # Fix 1: Unterminated evidence_level strings before risk_flags
        pattern1 = r'"evidence_level":\s*"([^"]*?),\s*\n\s*"risk_flags"'
        def repl1(m):
            return f'"evidence_level": "{m.group(1)}",\n            "risk_flags"'
        new_content = re.sub(pattern1, repl1, content)
        if new_content != content:
            changes.append("Fixed unterminated evidence_level before risk_flags")
            content = new_content
        
        # Fix 2: Text after closing bracket of guideline_tags
        pattern2 = r'(\]\s*)và dữ liệu lâm sàng từ nhiều nguồn"'
        new_content = re.sub(pattern2, r'\1', content)
        if new_content != content:
            changes.append("Fixed leftover text after guideline_tags")
            content = new_content
        
        # Fix 3: Unterminated evidence_level with "High - Multiple RCTs"
        pattern3 = r'"evidence_level":\s*"High - Multiple RCTs \(([^"]*?),\s*\n\s*"risk_flags"'
        def repl3(m):
            return f'"evidence_level": "High - Multiple RCTs ({m.group(1)}",\n            "risk_flags"'
        new_content = re.sub(pattern3, repl3, content)
        if new_content != content:
            changes.append("Fixed unterminated evidence_level with RCTs")
            content = new_content
        
        # Fix 4: Any other unterminated evidence_level
        pattern4 = r'"evidence_level":\s*"([^"]*?),\s*\n\s*"risk_flags"'
        def repl4(m):
            return f'"evidence_level": "{m.group(1)}",\n            "risk_flags"'
        new_content = re.sub(pattern4, repl4, content)
        if new_content != content:
            changes.append("Fixed other unterminated evidence_level")
            content = new_content
        
        if content != original_content:
            # Create backup
            backup_path = str(file_path) + ".comprehensive_fix_backup"
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
    """Fix syntax errors in all drug files"""
    drugs_dir = Path("drugs/drug_modules")
    
    fixed_files = []
    error_files = []
    
    for file_path in sorted(drugs_dir.rglob("*.py")):
        if file_path.name == "__init__.py" or file_path.name.endswith(".backup"):
            continue
        
        success, changes = fix_file(file_path)
        if success:
            fixed_files.append((str(file_path), changes))
            print(f"✅ Fixed: {file_path.name} - {', '.join(changes)}")
        elif changes and "Error" in changes[0]:
            error_files.append((str(file_path), changes[0]))
            print(f"❌ Error in {file_path.name}: {changes[0]}")
    
    print(f"\nFixed {len(fixed_files)} files")
    if error_files:
        print(f"Errors in {len(error_files)} files")

if __name__ == "__main__":
    main()
