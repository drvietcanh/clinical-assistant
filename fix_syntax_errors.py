"""
Fix syntax errors in drug files - unterminated strings in evidence_level
"""
import re
from pathlib import Path

def fix_file(file_path):
    """Fix unterminated strings in evidence_level fields"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        original_content = content
        
        # Fix pattern: "evidence_level": "A - Dựa trên FDA drug labels, ACC/AHA/ESC guidelines,
        # Should be: "evidence_level": "A - Dựa trên FDA drug labels, ACC/AHA/ESC guidelines",
        pattern1 = r'"evidence_level":\s*"A - Dựa trên FDA drug labels, ACC/AHA/ESC guidelines,\s*\n\s*"risk_flags"'
        replacement1 = '"evidence_level": "A - Dựa trên FDA drug labels, ACC/AHA/ESC guidelines",\n            "risk_flags"'
        content = re.sub(pattern1, replacement1, content)
        
        # Fix pattern: "evidence_level": "High - FDA approved,
        pattern2 = r'"evidence_level":\s*"High - FDA approved,\s*\n\s*"risk_flags"'
        replacement2 = '"evidence_level": "High - FDA approved",\n            "risk_flags"'
        content = re.sub(pattern2, replacement2, content)
        
        if content != original_content:
            # Create backup
            backup_path = str(file_path) + ".syntax_fix_backup"
            with open(backup_path, 'w', encoding='utf-8') as f:
                f.write(original_content)
            
            # Write fixed content
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
            
            return True, "Fixed"
        else:
            return False, "No changes needed"
            
    except Exception as e:
        return False, f"Error: {str(e)}"

def main():
    """Fix syntax errors in all drug files"""
    drugs_dir = Path("drugs/drug_modules")
    
    fixed_files = []
    error_files = []
    
    for file_path in drugs_dir.rglob("*.py"):
        if file_path.name == "__init__.py" or file_path.name.endswith(".backup"):
            continue
        
        success, message = fix_file(file_path)
        if success:
            fixed_files.append(str(file_path))
            print(f"✅ Fixed: {file_path.name}")
        elif "Error" in message:
            error_files.append((str(file_path), message))
            print(f"❌ Error in {file_path.name}: {message}")
    
    print(f"\nFixed {len(fixed_files)} files")
    if error_files:
        print(f"Errors in {len(error_files)} files")

if __name__ == "__main__":
    main()
