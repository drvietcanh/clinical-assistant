"""
Test script để tìm các pattern HTML có thể gây lỗi
"""

import sys
import io
import re

# Fix encoding for Windows
if sys.platform == 'win32':
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
    sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8')

def check_html_patterns(file_path):
    """Kiểm tra các pattern HTML có thể gây lỗi"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
            lines = content.split('\n')
        
        issues = []
        
        # Pattern 1: Tìm các f-string với unsafe_allow_html mà không có escape_html
        unsafe_pattern = re.compile(r'unsafe_allow_html\s*=\s*True')
        fstring_pattern = re.compile(r'f["\']')
        
        for i, line in enumerate(lines, 1):
            # Tìm dòng có unsafe_allow_html
            if unsafe_pattern.search(line):
                # Tìm f-string trong 10 dòng trước đó
                context_start = max(0, i - 10)
                context = '\n'.join(lines[context_start:i])
                
                # Kiểm tra xem có f-string không
                if fstring_pattern.search(context):
                    # Kiểm tra xem có escape_html không
                    if 'escape_html' not in context:
                        # Nhưng bỏ qua nếu là script hoặc style tags (không cần escape)
                        if '<script' not in context.lower() and '<style' not in context.lower():
                            # Kiểm tra xem có biến nào được inject không
                            var_pattern = re.compile(r'\{[^}]*\}')
                            vars_in_context = var_pattern.findall(context)
                            
                            # Bỏ qua nếu chỉ có biến CSS/color
                            has_user_input = False
                            for var in vars_in_context:
                                var_content = var.strip('{}')
                                # Nếu có biến không phải là CSS/color
                                if not re.match(r'^#[0-9a-fA-F]+$', var_content) and \
                                   not re.match(r'^\d+$', var_content) and \
                                   'color' not in var_content.lower() and \
                                   'background' not in var_content.lower() and \
                                   'padding' not in var_content.lower() and \
                                   'margin' not in var_content.lower():
                                    has_user_input = True
                                    break
                            
                            if has_user_input:
                                issues.append({
                                    'line': i,
                                    'type': 'Potential unescaped HTML',
                                    'context': line.strip()[:100]
                                })
        
        return issues
    
    except Exception as e:
        return [{'line': 0, 'type': 'Error', 'context': str(e)}]

def main():
    """Main test function"""
    print("=" * 60)
    print("HTML PATTERN CHECK")
    print("=" * 60 + "\n")
    
    files_to_check = [
        "pages/Drug_Detail.py",
        "drugs/drug_info_components/card_components.py",
        "drugs/drug_info_components/detail_view.py",
    ]
    
    all_clean = True
    
    for file_path in files_to_check:
        print(f"\nChecking: {file_path}")
        print("-" * 60)
        
        issues = check_html_patterns(file_path)
        
        if issues:
            all_clean = False
            for issue in issues:
                if issue['type'] != 'Error':
                    print(f"⚠️  Line {issue['line']}: {issue['type']}")
                    print(f"   {issue['context']}")
                else:
                    print(f"❌ {issue['context']}")
        else:
            print("✅ No obvious HTML injection patterns found")
    
    print("\n" + "=" * 60)
    if all_clean:
        print("✅ HTML PATTERNS CHECK PASSED")
        print("   (Note: This is a basic check. Manual review recommended)")
    else:
        print("⚠️  SOME POTENTIAL ISSUES FOUND")
        print("   (Please review manually)")
    print("=" * 60)
    
    return 0 if all_clean else 1

if __name__ == "__main__":
    sys.exit(main())

