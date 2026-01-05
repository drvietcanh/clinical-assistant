"""
Fix all remaining syntax errors - comprehensive approach
"""
import re
from pathlib import Path

def fix_file(file_path):
    """Fix all syntax errors in a file"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            lines = f.readlines()
        
        original_lines = lines.copy()
        fixed = False
        
        # Fix pattern: ] text" at end of guideline_tags
        for i, line in enumerate(lines):
            # Look for pattern: ] some text"
            match = re.search(r'(\]\s*)([^"]+)"', line)
            if match and 'guideline_tags' in ''.join(lines[max(0, i-5):i+1]):
                # This is leftover text after guideline_tags closing bracket
                lines[i] = match.group(1) + '\n'
                fixed = True
        
        # Fix pattern: unterminated evidence_level strings
        for i, line in enumerate(lines):
            if '"evidence_level"' in line and i + 1 < len(lines):
                # Check if next line starts with "risk_flags" without closing quote
                if '"risk_flags"' in lines[i+1] and not line.rstrip().endswith('"'):
                    # Find where the string should end
                    # Look for the pattern: "evidence_level": "text,
                    match = re.search(r'"evidence_level":\s*"([^"]*?),', line)
                    if match:
                        # The string is unterminated, close it
                        lines[i] = line.rstrip() + '",\n'
                        fixed = True
        
        if fixed:
            # Create backup
            backup_path = str(file_path) + ".remaining_fix_backup"
            with open(backup_path, 'w', encoding='utf-8') as f:
                f.writelines(original_lines)
            
            # Write fixed content
            with open(file_path, 'w', encoding='utf-8') as f:
                f.writelines(lines)
            
            return True
        else:
            return False
            
    except Exception as e:
        print(f"Error in {file_path}: {e}")
        return False

def main():
    """Fix all remaining syntax errors"""
    # Focus on antiarrhythmics.py which has the most errors
    file_path = Path("drugs/drug_modules/cardiovascular/antiarrhythmics.py")
    
    if fix_file(file_path):
        print(f"✅ Fixed: {file_path.name}")
    else:
        print(f"⏭️  No changes needed: {file_path.name}")

if __name__ == "__main__":
    main()

