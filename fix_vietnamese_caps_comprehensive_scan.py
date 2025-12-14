"""
Script quét và sửa triệt để các lỗi viết hoa tiếng Việt
Sử dụng file vietnamese_capitalization_fixes.py làm nguồn dữ liệu
"""

import re
from pathlib import Path
from vietnamese_capitalization_fixes import get_all_fixes, get_regex_patterns

def scan_and_fix_files(dry_run=True):
    """
    Quét và sửa các lỗi viết hoa trong toàn bộ codebase
    
    Args:
        dry_run: Nếu True, chỉ báo cáo không sửa file
    """
    fixes = get_all_fixes()
    regex_patterns = get_regex_patterns()
    
    # Tìm tất cả Python files
    files_to_check = []
    for pattern in [
        'protocols/**/*.py',
        'pages/**/*.py',
        'scores/**/*.py',
        'labs/**/*.py',
        'critical_care/**/*.py',
        'antibiotics/**/*.py',
        'drugs/**/*.py'
    ]:
        files_to_check.extend(Path('.').glob(pattern))
    
    # Loại trừ các file không cần sửa
    exclude_patterns = [
        '__init__.py',
        '__pycache__',
        '.pyc',
        'check_',
        'fix_',
        'test_',
        'find_',
        'vietnamese_',
        'TEMPLATE'
    ]
    files_to_check = [
        f for f in files_to_check
        if not any(ex in str(f) for ex in exclude_patterns)
    ]
    
    print(f"🔍 Quét {len(files_to_check)} files...\n")
    
    total_fixes = 0
    files_modified = []
    files_with_issues = []
    
    for file_path in files_to_check:
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            original_content = content
            file_fixes = []
            
            # Áp dụng các fix đơn giản
            for pattern, replacement in fixes.items():
                if pattern in content:
                    count = content.count(pattern)
                    if count > 0:
                        content = content.replace(pattern, replacement)
                        file_fixes.append((pattern, replacement, count))
            
            # Áp dụng regex patterns
            for pattern, replacement in regex_patterns:
                matches = re.findall(pattern, content)
                if matches:
                    content = re.sub(pattern, replacement, content)
                    file_fixes.append((pattern, replacement, len(matches)))
            
            # Chỉ ghi nếu có thay đổi
            if content != original_content:
                files_with_issues.append((file_path, file_fixes))
                total_fixes += sum(count for _, _, count in file_fixes)
                
                if not dry_run:
                    with open(file_path, 'w', encoding='utf-8') as f:
                        f.write(content)
                    files_modified.append(file_path)
                    print(f"✅ Đã sửa: {file_path} ({len(file_fixes)} pattern)")
                else:
                    print(f"📝 Cần sửa: {file_path} ({len(file_fixes)} pattern)")
                    for pattern, replacement, count in file_fixes:
                        print(f"   - '{pattern}' → '{replacement}' ({count} lần)")
        
        except Exception as e:
            print(f"❌ Lỗi khi xử lý {file_path}: {e}")
    
    print(f"\n{'='*60}")
    print(f"📊 TỔNG KẾT:")
    print(f"   - Files cần sửa: {len(files_with_issues)}")
    print(f"   - Tổng số lỗi: {total_fixes}")
    if not dry_run:
        print(f"   - Files đã sửa: {len(files_modified)}")
    print(f"{'='*60}\n")
    
    return files_with_issues, total_fixes

if __name__ == "__main__":
    import sys
    
    # Kiểm tra argument
    dry_run = True
    if len(sys.argv) > 1 and sys.argv[1] == "--apply":
        dry_run = False
        print("⚠️  CHẾ ĐỘ SỬA FILE - Các thay đổi sẽ được lưu!\n")
    else:
        print("🔍 CHẾ ĐỘ DRY RUN - Chỉ báo cáo, không sửa file\n")
        print("💡 Để áp dụng thay đổi, chạy: python fix_vietnamese_caps_comprehensive_scan.py --apply\n")
    
    files_with_issues, total_fixes = scan_and_fix_files(dry_run=dry_run)
    
    if files_with_issues:
        print("\n📋 CHI TIẾT CÁC FILE CẦN SỬA:")
        for file_path, fixes in files_with_issues[:10]:  # Hiển thị 10 file đầu
            print(f"\n📄 {file_path}:")
            for pattern, replacement, count in fixes[:5]:  # Hiển thị 5 pattern đầu
                print(f"   - '{pattern}' → '{replacement}' ({count}x)")
            if len(fixes) > 5:
                print(f"   ... và {len(fixes) - 5} pattern khác")
        
        if len(files_with_issues) > 10:
            print(f"\n... và {len(files_with_issues) - 10} file khác")

