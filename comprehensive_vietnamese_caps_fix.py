"""
Script quét và sửa toàn diện lỗi viết hoa tiếng Việt
Tìm và sửa: Thần Kinh → Thần kinh, Tiêu Hóa → Tiêu hóa, Tùy Chỉnh → tùy chỉnh
"""

import re
import os
from pathlib import Path
from collections import defaultdict

# Các pattern cần sửa (sai → đúng)
FIXES = {
    # Category names - chỉ viết hoa chữ cái đầu từ đầu tiên
    'category="Thần Kinh"': 'category="Thần kinh"',
    "category='Thần Kinh'": "category='Thần kinh'",
    'category="Tiêu Hóa"': 'category="Tiêu hóa"',
    "category='Tiêu Hóa'": "category='Tiêu hóa'",
    
    # Từ thông thường - viết thường
    '"Tùy Chỉnh"': '"tùy chỉnh"',
    "'Tùy Chỉnh'": "'tùy chỉnh'",
    'Tùy Chỉnh': 'tùy chỉnh',  # Trong context không phải proper noun
    
    # Các pattern khác có thể có
    ' "Thần Kinh"': ' "Thần kinh"',
    " 'Thần Kinh'": " 'Thần kinh'",
    ' "Tiêu Hóa"': ' "Tiêu hóa"',
    " 'Tiêu Hóa'": " 'Tiêu hóa'",
}

# Thư mục cần quét
DIRECTORIES = [
    "scores",
    "drugs",
    "pages",
    "config",
    "components",
    "critical_care",
    "protocols",
    "antibiotics",
]

# File extensions cần quét
EXTENSIONS = [".py", ".md"]

# Files/patterns cần bỏ qua
IGNORE_PATTERNS = [
    "__pycache__",
    ".git",
    "node_modules",
    "venv",
    "env",
    ".pytest_cache",
    "backups",
    "comprehensive_vietnamese_caps_fix.py",  # Không sửa chính script này
]

def should_process_file(file_path: Path) -> bool:
    """Kiểm tra xem file có nên được xử lý không"""
    file_str = str(file_path)
    
    # Bỏ qua nếu trong ignore patterns
    for pattern in IGNORE_PATTERNS:
        if pattern in file_str:
            return False
    
    # Chỉ xử lý các file có extension phù hợp
    return file_path.suffix in EXTENSIONS

def find_errors_in_file(file_path: Path) -> list:
    """Tìm các lỗi viết hoa trong file"""
    errors = []
    
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
            lines = content.split('\n')
    except Exception as e:
        print(f"❌ Lỗi đọc file {file_path}: {e}")
        return errors
    
    for line_num, line in enumerate(lines, 1):
        for wrong, correct in FIXES.items():
            if wrong in line:
                # Kiểm tra context - không sửa nếu là trong comment đặc biệt
                # Nhưng vẫn báo lỗi để review
                errors.append({
                    'line': line_num,
                    'wrong': wrong,
                    'correct': correct,
                    'context': line.strip()[:100],
                    'file': str(file_path)
                })
    
    return errors

def fix_errors_in_file(file_path: Path, dry_run: bool = False) -> tuple[int, list]:
    """
    Sửa lỗi viết hoa trong file
    Returns: (số lần thay thế, danh sách các thay đổi)
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
    except Exception as e:
        print(f"❌ Lỗi đọc file {file_path}: {e}")
        return 0, []
    
    original_content = content
    changes = []
    total_replacements = 0
    
    # Thay thế các cụm từ dài trước (để tránh thay thế nhầm)
    # Sắp xếp theo độ dài giảm dần
    sorted_fixes = sorted(FIXES.items(), key=lambda x: len(x[0]), reverse=True)
    
    for wrong, correct in sorted_fixes:
        count = content.count(wrong)
        if count > 0:
            content = content.replace(wrong, correct)
            total_replacements += count
            changes.append(f"  - '{wrong}' → '{correct}' ({count} lần)")
    
    # Ghi file nếu có thay đổi và không phải dry run
    if content != original_content and not dry_run:
        try:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
            return total_replacements, changes
        except Exception as e:
            print(f"❌ Lỗi ghi file {file_path}: {e}")
            return 0, []
    
    return total_replacements, changes

def scan_all_files(dry_run: bool = True):
    """Quét tất cả files và tìm lỗi"""
    all_errors = []
    files_with_errors = defaultdict(list)
    
    print("🔍 Đang quét các lỗi viết hoa tiếng Việt...\n")
    
    for directory in DIRECTORIES:
        dir_path = Path(directory)
        if not dir_path.exists():
            print(f"⚠️  Thư mục không tồn tại: {directory}")
            continue
        
        print(f"📂 Quét thư mục: {directory}")
        
        for file_path in dir_path.rglob("*"):
            if file_path.is_file() and should_process_file(file_path):
                errors = find_errors_in_file(file_path)
                if errors:
                    all_errors.extend(errors)
                    files_with_errors[str(file_path)] = errors
    
    return all_errors, files_with_errors

def main():
    """Main function"""
    print("=" * 70)
    print("🔧 KIỂM TRA VÀ SỬA LỖI VIẾT HOA TIẾNG VIỆT")
    print("=" * 70)
    print()
    
    # Bước 1: Quét và hiển thị lỗi
    all_errors, files_with_errors = scan_all_files(dry_run=True)
    
    if not all_errors:
        print("✅ Không tìm thấy lỗi viết hoa!")
        return
    
    print(f"\n📊 Tìm thấy {len(all_errors)} lỗi trong {len(files_with_errors)} files:\n")
    
    # Hiển thị tóm tắt theo file
    for file_path, errors in sorted(files_with_errors.items()):
        print(f"📄 {file_path}")
        print(f"   Có {len(errors)} lỗi:")
        for error in errors[:5]:  # Hiển thị 5 lỗi đầu
            print(f"   - Dòng {error['line']}: {error['wrong']} → {error['correct']}")
            print(f"     Context: {error['context']}")
        if len(errors) > 5:
            print(f"   ... và {len(errors) - 5} lỗi khác")
        print()
    
    # Bước 2: Hỏi xác nhận trước khi sửa
    print("=" * 70)
    response = input("Bạn có muốn sửa tự động các lỗi này? (yes/no): ").strip().lower()
    
    if response not in ['yes', 'y', 'có', 'co']:
        print("❌ Đã hủy. Không có thay đổi nào được thực hiện.")
        return
    
    # Bước 3: Sửa lỗi
    print("\n🔧 Đang sửa lỗi...\n")
    
    total_files = 0
    total_changes = 0
    files_changed = []
    
    for directory in DIRECTORIES:
        dir_path = Path(directory)
        if not dir_path.exists():
            continue
        
        for file_path in dir_path.rglob("*"):
            if file_path.is_file() and should_process_file(file_path):
                if str(file_path) in files_with_errors:
                    total_files += 1
                    replacements, changes = fix_errors_in_file(file_path, dry_run=False)
                    
                    if replacements > 0:
                        total_changes += replacements
                        files_changed.append((file_path, replacements, changes))
                        print(f"✅ {file_path}: {replacements} thay đổi")
                        for change in changes[:3]:  # Chỉ hiển thị 3 thay đổi đầu
                            print(change)
                        if len(changes) > 3:
                            print(f"   ... và {len(changes) - 3} thay đổi khác")
    
    # Tóm tắt
    print()
    print("=" * 70)
    print("📊 TÓM TẮT")
    print("=" * 70)
    print(f"Tổng số file đã sửa: {len(files_changed)}")
    print(f"Tổng số thay đổi: {total_changes}")
    print()
    
    if files_changed:
        print("📝 Các file đã sửa:")
        for file_path, count, _ in files_changed[:20]:  # Hiển thị 20 file đầu
            print(f"  - {file_path} ({count} thay đổi)")
        if len(files_changed) > 20:
            print(f"  ... và {len(files_changed) - 20} file khác")
    
    print()
    print("✅ Hoàn thành!")

if __name__ == "__main__":
    main()
