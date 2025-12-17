"""
Script sửa triệt để các lỗi viết hoa tiếng Việt trong codebase
Tìm kiếm sâu và sửa tất cả các file Python
"""

import os
import re
from pathlib import Path

# Dictionary chứa các lỗi viết hoa cần sửa
CAPITALIZATION_FIXES = {
    # ========== CÁC LỖI MỚI CẦN SỬA ==========
    "Hạ Thân Nhiệt": "Hạ thân nhiệt",
    "Đánh giá Nguy cơ": "Đánh giá nguy cơ",
    "Triệu chứng Lâm sàng": "Triệu chứng lâm sàng",
    "Phác đồ Điều trị": "Phác đồ điều trị",
    "Phương Pháp Làm Ấm": "Phương pháp làm ấm",
    "Ngừng tim Do Hạ Thân Nhiệt": "Ngừng tim do hạ thân nhiệt",
    "Sốc Nhiễm Trùng": "Sốc nhiễm trùng",
    "Sốc Giảm Thể tích": "Sốc giảm thể tích",
    
    # ========== CÁC BIẾN THỂ KHÁC ==========
    "Đánh giá Nguy cơ &": "Đánh giá nguy cơ &",
    "Đánh giá Nguy cơ Tự Tử": "Đánh giá nguy cơ tự tử",
    "Đánh giá Nguy cơ Chảy máu": "Đánh giá nguy cơ chảy máu",
    "Đánh giá Nguy cơ Đột quỵ": "Đánh giá nguy cơ đột quỵ",
    "Đánh giá Nguy cơ Trong": "Đánh giá nguy cơ trong",
    "Đánh giá Nguy cơ ACS": "Đánh giá nguy cơ ACS",
    "Đánh giá Nguy cơ VTE": "Đánh giá nguy cơ VTE",
    "Đánh giá Nguy cơ xuất huyết": "Đánh giá nguy cơ xuất huyết",
    "Đánh giá Nguy cơ tử vong": "Đánh giá nguy cơ tử vong",
    "Đánh giá Nguy cơ tim mạch": "Đánh giá nguy cơ tim mạch",
    "Đánh giá Nguy cơ biến chứng": "Đánh giá nguy cơ biến chứng",
    "Đánh giá Nguy cơ đặt nội khí quản": "Đánh giá nguy cơ đặt nội khí quản",
    "Đánh giá Nguy cơ té ngã": "Đánh giá nguy cơ té ngã",
    "Đánh giá Nguy cơ loét tì đè": "Đánh giá nguy cơ loét tì đè",
    "Đánh giá Nguy cơ rối loạn nhịp": "Đánh giá nguy cơ rối loạn nhịp",
    "Đánh giá Nguy cơ đột quỵ": "Đánh giá nguy cơ đột quỵ",
    "Đánh giá Nguy cơ bệnh tim mạch": "Đánh giá nguy cơ bệnh tim mạch",
    "Đánh giá Nguy cơ tiền phẫu": "Đánh giá nguy cơ tiền phẫu",
    "Đánh giá Nguy cơ VTE sau phẫu thuật": "Đánh giá nguy cơ VTE sau phẫu thuật",
    "Đánh giá Nguy cơ bằng": "Đánh giá nguy cơ bằng",
    "Đánh giá Nguy cơ cần can thiệp": "Đánh giá nguy cơ cần can thiệp",
    "Đánh giá Nguy cơ lạm dụng": "Đánh giá nguy cơ lạm dụng",
    "Đánh giá Nguy cơ theo liều": "Đánh giá nguy cơ theo liều",
    "Đánh giá Nguy cơ với": "Đánh giá nguy cơ với",
    
    "Triệu chứng Lâm Sàng": "Triệu chứng lâm sàng",  # Biến thể với S hoa
    "Các Triệu chứng Lâm sàng": "Các triệu chứng lâm sàng",
    
    "Phác đồ Điều trị theo mức độ": "Phác đồ điều trị theo mức độ",
    "Phác đồ điều trị chuẩn": "Phác đồ điều trị chuẩn",  # Đã đúng nhưng kiểm tra
    "phác đồ điều trị": "phác đồ điều trị",  # Giữ nguyên nếu đã viết thường
    
    "Phương pháp làm ấm": "Phương pháp làm ấm",  # Kiểm tra xem có cần sửa không
}

# Thư mục gốc của project
ROOT_DIR = Path(__file__).parent

# Các thư mục cần bỏ qua
IGNORE_DIRS = {
    '.git', '__pycache__', 'node_modules', '.venv', 'venv', 
    'env', '.idea', '.vscode', 'build', 'dist', '.pytest_cache'
}

# Các file cần bỏ qua
IGNORE_FILES = {
    'fix_capitalization_errors.py',  # Không sửa chính file script này
    'vietnamese_capitalization_fixes.py',  # File config
    'fast_vietnamese_caps_checker.py',  # File checker
}


def should_process_file(file_path: Path) -> bool:
    """Kiểm tra xem file có nên được xử lý không"""
    # Chỉ xử lý file Python
    if not file_path.suffix == '.py':
        return False
    
    # Bỏ qua file trong ignore list
    if file_path.name in IGNORE_FILES:
        return False
    
    # Bỏ qua file trong thư mục ignore
    for part in file_path.parts:
        if part in IGNORE_DIRS:
            return False
    
    return True


def fix_capitalization_in_text(text: str) -> tuple[str, int]:
    """
    Sửa các lỗi viết hoa trong text
    Trả về (text đã sửa, số lần sửa)
    """
    fixes_count = 0
    fixed_text = text
    
    # Sắp xếp các pattern theo độ dài giảm dần để tránh sửa nhầm
    sorted_fixes = sorted(CAPITALIZATION_FIXES.items(), key=lambda x: len(x[0]), reverse=True)
    
    for pattern, replacement in sorted_fixes:
        # Đếm số lần xuất hiện trước khi thay thế
        count = fixed_text.count(pattern)
        if count > 0:
            fixed_text = fixed_text.replace(pattern, replacement)
            fixes_count += count
    
    return fixed_text, fixes_count


def process_file(file_path: Path) -> tuple[bool, int]:
    """
    Xử lý một file
    Trả về (có thay đổi không, số lần sửa)
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            original_text = f.read()
        
        fixed_text, fixes_count = fix_capitalization_in_text(original_text)
        
        if fixes_count > 0:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(fixed_text)
            return True, fixes_count
        
        return False, 0
    
    except Exception as e:
        print(f"❌ Lỗi khi xử lý {file_path}: {e}")
        return False, 0


def main():
    """Hàm chính"""
    print("🔍 Đang tìm kiếm các file Python...")
    
    python_files = []
    for root, dirs, files in os.walk(ROOT_DIR):
        # Bỏ qua các thư mục ignore
        dirs[:] = [d for d in dirs if d not in IGNORE_DIRS]
        
        for file in files:
            file_path = Path(root) / file
            if should_process_file(file_path):
                python_files.append(file_path)
    
    print(f"📁 Tìm thấy {len(python_files)} file Python\n")
    
    total_fixes = 0
    modified_files = []
    
    print("🔧 Đang sửa các lỗi viết hoa...\n")
    
    for file_path in python_files:
        modified, fixes_count = process_file(file_path)
        if modified:
            modified_files.append((file_path, fixes_count))
            total_fixes += fixes_count
            print(f"✅ {file_path.relative_to(ROOT_DIR)}: {fixes_count} lần sửa")
    
    print(f"\n{'='*60}")
    print(f"📊 TỔNG KẾT:")
    print(f"   - Tổng số file đã sửa: {len(modified_files)}")
    print(f"   - Tổng số lần sửa: {total_fixes}")
    print(f"{'='*60}\n")
    
    if modified_files:
        print("📝 Danh sách file đã sửa:")
        for file_path, count in modified_files:
            print(f"   - {file_path.relative_to(ROOT_DIR)} ({count} lần)")
    else:
        print("✅ Không tìm thấy lỗi viết hoa nào cần sửa!")


if __name__ == "__main__":
    main()

