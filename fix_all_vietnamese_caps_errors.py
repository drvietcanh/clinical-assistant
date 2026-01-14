"""
Script tự động sửa tất cả các lỗi viết hoa tiếng Việt
"""

import re
from pathlib import Path
from collections import defaultdict

# Mapping các lỗi viết hoa sai → đúng
FIXES = {
    # 2 từ - chỉ từ đầu viết hoa
    'Bổ Sung': 'Bổ sung',
    'Chuyển Hóa': 'Chuyển hóa',
    'Chỉ Định': 'Chỉ định',
    'Cấp Cứu': 'Cấp cứu',
    'Gây Mê': 'Gây mê',
    'Hô Hấp': 'Hô hấp',
    'Hướng Dẫn': 'Hướng dẫn',
    'Hồi Sức': 'Hồi sức',
    'Hỗ Trợ': 'Hỗ trợ',
    'Kháng Sinh': 'Kháng sinh',
    'Kiểm Soát': 'Kiểm soát',
    'Kiểm Tra': 'Kiểm tra',
    'Miễn Dịch': 'Miễn dịch',
    'Mô Tả': 'Mô tả',
    'Mục Tiêu': 'Mục tiêu',
    'Mức Độ': 'Mức độ',
    'Nguy Cơ': 'Nguy cơ',
    'Người Lớn': 'Người lớn',
    'Nội Tiết': 'Nội tiết',
    'Phân Tích': 'Phân tích',
    'Quản Lý': 'Quản lý',
    'So Sánh': 'So sánh',
    'Suy Thận': 'Suy thận',
    'Suy Tim': 'Suy tim',
    'Tham Khảo': 'Tham khảo',
    'Theo Dõi': 'Theo dõi',
    'Thành Phần': 'Thành phần',
    'Thần Kinh': 'Thần kinh',
    'Tim Mạch': 'Tim mạch',
    'Tiêu Chuẩn': 'Tiêu chuẩn',
    'Tiêu Chảy': 'Tiêu chảy',
    'Tiêu Hóa': 'Tiêu hóa',
    'Trẻ Em': 'Trẻ em',
    'Tài Liệu': 'Tài liệu',
    'Tái Phát': 'Tái phát',
    'Tỷ Lệ': 'Tỷ lệ',
    'Ung Thư': 'Ung thư',
    'Xuất Huyết': 'Xuất huyết',
    'Điều Chỉnh': 'Điều chỉnh',
    'Độc Lập': 'Độc lập',
    'Ưu Tiên': 'Ưu tiên',
}

DIRECTORIES = [
    "scores",
    "drugs",
    "pages",
    "config",
    "components",
    "critical_care",
    "protocols",
]

IGNORE_PATTERNS = [
    "__pycache__",
    ".git",
    "node_modules",
    "venv",
    "env",
    ".pytest_cache",
    "backups",
    "find_all_vietnamese_caps_errors.py",
    "comprehensive_vietnamese_caps_fix.py",
    "fix_all_vietnamese_caps_errors.py",
]

def should_process_file(file_path: Path) -> bool:
    """Kiểm tra xem file có nên được xử lý không"""
    file_str = str(file_path)
    for pattern in IGNORE_PATTERNS:
        if pattern in file_str:
            return False
    return file_path.suffix in [".py", ".md"]

def fix_file(file_path: Path) -> tuple[int, list]:
    """Sửa lỗi viết hoa trong file"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
    except Exception as e:
        print(f"❌ Lỗi đọc file {file_path}: {e}")
        return 0, []
    
    original_content = content
    changes = []
    total_replacements = 0
    
    # Sắp xếp theo độ dài giảm dần để tránh thay thế nhầm
    sorted_fixes = sorted(FIXES.items(), key=lambda x: len(x[0]), reverse=True)
    
    for wrong, correct in sorted_fixes:
        count = content.count(wrong)
        if count > 0:
            content = content.replace(wrong, correct)
            total_replacements += count
            changes.append(f"  - '{wrong}' → '{correct}' ({count} lần)")
    
    # Ghi file nếu có thay đổi
    if content != original_content:
        try:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
            return total_replacements, changes
        except Exception as e:
            print(f"❌ Lỗi ghi file {file_path}: {e}")
            return 0, []
    
    return 0, []

def main():
    """Main function"""
    print("=" * 70)
    print("🔧 TỰ ĐỘNG SỬA TẤT CẢ CÁC LỖI VIẾT HOA TIẾNG VIỆT")
    print("=" * 70)
    print()
    
    total_files = 0
    total_changes = 0
    files_changed = []
    
    for directory in DIRECTORIES:
        dir_path = Path(directory)
        if not dir_path.exists():
            continue
        
        print(f"📂 Quét thư mục: {directory}")
        
        for file_path in dir_path.rglob("*"):
            if file_path.is_file() and should_process_file(file_path):
                total_files += 1
                replacements, changes = fix_file(file_path)
                
                if replacements > 0:
                    total_changes += replacements
                    files_changed.append((file_path, replacements, changes))
                    print(f"✅ {file_path}: {replacements} thay đổi")
                    for change in changes[:3]:  # Hiển thị 3 thay đổi đầu
                        print(change)
                    if len(changes) > 3:
                        print(f"   ... và {len(changes) - 3} thay đổi khác")
    
    # Tóm tắt
    print()
    print("=" * 70)
    print("📊 TÓM TẮT")
    print("=" * 70)
    print(f"Tổng số file đã quét: {total_files}")
    print(f"Tổng số file đã sửa: {len(files_changed)}")
    print(f"Tổng số thay đổi: {total_changes}")
    print()
    
    if files_changed:
        print("📝 Các file đã sửa:")
        for file_path, count, _ in files_changed[:30]:  # Hiển thị 30 file đầu
            print(f"  - {file_path} ({count} thay đổi)")
        if len(files_changed) > 30:
            print(f"  ... và {len(files_changed) - 30} file khác")
    
    print()
    print("✅ Hoàn thành!")

if __name__ == "__main__":
    main()
