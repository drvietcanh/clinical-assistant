"""
Script để sửa lỗi viết hoa tiếng Việt
Sửa các cụm từ: Bảng Tham Khảo, Chi Tiết, Kết Quả, Chi Tiết Điểm Số, Diễn Giải, Lưu Ý
"""

import re
import os
from pathlib import Path

# Các cụm từ cần sửa (từ sai → từ đúng)
REPLACEMENTS = {
    # Cụm từ đầy đủ
    "Bảng Tham Khảo": "Bảng tham khảo",
    "Chi Tiết Điểm Số": "Chi tiết điểm số",
    "Chi Tiết Tính Điểm": "Chi tiết tính điểm",
    "Chi Tiết Tính Toán": "Chi tiết tính toán",
    "Chi Tiết Từng Biến Số": "Chi tiết từng biến số",
    "Chi Tiết Từng Thành Phần": "Chi tiết từng thành phần",
    "Chi Tiết Từng Tiêu Chí": "Chi tiết từng tiêu chí",
    "Chi Tiết Đánh Giá": "Chi tiết đánh giá",
    "Diễn Giải": "Diễn giải",
    "Diễn Giải Kết Quả": "Diễn giải kết quả",
    "Diễn Giải SOFA-2": "Diễn giải SOFA-2",
    "Diễn Giải MODS": "Diễn giải MODS",
    "Lưu Ý": "Lưu ý",
    "Lưu Ý Quan Trọng": "Lưu ý quan trọng",
    "Lưu Ý Y Khoa": "Lưu ý y khoa",
    "Lưu Ý Đặc Biệt": "Lưu ý đặc biệt",
    "Lưu Ý Điều Trị": "Lưu ý điều trị",
    
    # Từ đơn lẻ (cần cẩn thận với context)
    "Chi Tiết": "Chi tiết",
    "Kết Quả": "Kết quả",
}

# Thư mục cần quét
DIRECTORIES = [
    "scores",
    "critical_care",
    "protocols",
    "components",
    "drugs",
    "antibiotics",
    "labs",
    "ventilator",
    "pages",
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


def fix_capitalization_in_file(file_path: Path) -> tuple[int, list[str]]:
    """
    Sửa lỗi viết hoa trong một file
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
    sorted_replacements = sorted(REPLACEMENTS.items(), key=lambda x: len(x[0]), reverse=True)
    
    for wrong, correct in sorted_replacements:
        # Tìm tất cả các occurrences
        pattern = re.escape(wrong)
        matches = list(re.finditer(pattern, content))
        
        if matches:
            # Thay thế từ cuối lên đầu để không làm thay đổi index
            for match in reversed(matches):
                start, end = match.span()
                # Kiểm tra context - không thay thế nếu là trong comment hoặc string đặc biệt
                before = content[max(0, start-20):start]
                after = content[end:min(len(content), end+20)]
                
                # Bỏ qua nếu là trong docstring hoặc comment đặc biệt
                if '"""' in before[-50:] or "'''" in before[-50:]:
                    # Kiểm tra xem có phải là docstring không
                    continue
                
                content = content[:start] + correct + content[end:]
                changes.append(f"  - '{wrong}' → '{correct}' (dòng ~{original_content[:start].count(chr(10))+1})")
                total_replacements += 1
    
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
    print("=" * 60)
    print("🔧 SỬA LỖI VIẾT HOA TIẾNG VIỆT")
    print("=" * 60)
    print()
    
    total_files = 0
    total_changes = 0
    files_changed = []
    
    # Quét tất cả các thư mục
    for directory in DIRECTORIES:
        dir_path = Path(directory)
        if not dir_path.exists():
            print(f"⚠️  Thư mục không tồn tại: {directory}")
            continue
        
        print(f"📂 Quét thư mục: {directory}")
        
        # Quét tất cả các file
        for file_path in dir_path.rglob("*"):
            if file_path.is_file() and should_process_file(file_path):
                total_files += 1
                replacements, changes = fix_capitalization_in_file(file_path)
                
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
    print("=" * 60)
    print("📊 TÓM TẮT")
    print("=" * 60)
    print(f"Tổng số file đã quét: {total_files}")
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

