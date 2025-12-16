"""
Script tự động sửa lỗi viết hoa tiếng Việt dựa trên báo cáo
"""

import re
from pathlib import Path
from fast_vietnamese_caps_checker import (
    find_capitalization_errors, 
    should_process_file,
    DIRECTORIES
)

def fix_file(file_path: Path) -> int:
    """Sửa lỗi viết hoa trong một file và trả về số lỗi đã sửa"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        errors = find_capitalization_errors(content, file_path)
        
        if not errors:
            return 0
        
        # Sửa các lỗi theo thứ tự ngược lại để không ảnh hưởng đến vị trí
        for error in reversed(errors):
            # Escape special characters trong regex
            pattern = re.escape(error['text'])
            # Chỉ thay thế một lần để tránh thay thế nhầm
            content = re.sub(pattern, error['corrected'], content, count=1)
        
        # Ghi lại file
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        
        return len(errors)
        
    except Exception as e:
        print(f"❌ Lỗi khi sửa {file_path}: {e}")
        return 0

def main():
    import sys
    
    dry_run = True
    if len(sys.argv) > 1 and sys.argv[1] == "--apply":
        dry_run = False
        print("⚠️  CHẾ ĐỘ SỬA FILE - Các thay đổi sẽ được lưu!\n")
    else:
        print("🔍 CHẾ ĐỘ DRY RUN - Chỉ báo cáo, không sửa file\n")
        print("💡 Để áp dụng thay đổi, chạy: python auto_fix_vietnamese_caps.py --apply\n")
    
    print("=" * 80)
    print("🔧 TỰ ĐỘNG SỬA LỖI VIẾT HOA TIẾNG VIỆT")
    print("=" * 80)
    print()
    
    total_files_fixed = 0
    total_errors_fixed = 0
    
    for directory in DIRECTORIES:
        dir_path = Path(directory)
        if not dir_path.exists():
            continue
        
        print(f"📂 Xử lý: {directory}...")
        
        for file_path in dir_path.rglob("*"):
            if file_path.is_file() and should_process_file(file_path):
                errors_count = fix_file(file_path) if not dry_run else 0
                
                if not dry_run:
                    # Đếm lại để xác nhận
                    try:
                        with open(file_path, 'r', encoding='utf-8') as f:
                            content = f.read()
                        remaining_errors = find_capitalization_errors(content, file_path)
                        if remaining_errors:
                            print(f"  ⚠️  {file_path}: {len(remaining_errors)} lỗi còn lại")
                        elif errors_count > 0:
                            print(f"  ✅ {file_path}: {errors_count} lỗi đã sửa")
                            total_files_fixed += 1
                            total_errors_fixed += errors_count
                    except:
                        pass
    
    print()
    print("=" * 80)
    print("📊 TÓM TẮT")
    print("=" * 80)
    
    if dry_run:
        print("💡 Chạy với --apply để áp dụng các thay đổi")
    else:
        print(f"✅ Đã sửa {total_errors_fixed} lỗi trong {total_files_fixed} file")
    
    print()

if __name__ == "__main__":
    main()

