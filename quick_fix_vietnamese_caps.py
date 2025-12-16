"""
Script nhanh để quét và sửa lỗi viết hoa tiếng Việt triệt để
Quy tắc: Chỉ viết hoa chữ cái đầu câu và tên riêng, không viết hoa tất cả các từ trong cụm danh từ
"""

import re
import os
from pathlib import Path
from collections import defaultdict

# Danh sách các cụm từ phổ biến cần sửa (từ sai → từ đúng)
# Format: Tất cả các từ trong cụm danh từ chỉ viết hoa chữ cái đầu từ đầu tiên
COMMON_FIXES = {
    # Thuật ngữ y khoa
    "Điều Trị": "Điều trị",
    "Chẩn Đoán": "Chẩn đoán",
    "Theo Dõi": "Theo dõi",
    "Phân Loại": "Phân loại",
    "Phân Tầng": "Phân tầng",
    "Đánh Giá": "Đánh giá",
    "Xử Trí": "Xử trí",
    "Quản Lý": "Quản lý",
    "Chỉ Định": "Chỉ định",
    "Triệu Chứng": "Triệu chứng",
    "Dấu Hiệu": "Dấu hiệu",
    "Tiêu Chuẩn": "Tiêu chuẩn",
    "Tiêu Chí": "Tiêu chí",
    "Nguyên Nhân": "Nguyên nhân",
    "Mục Tiêu": "Mục tiêu",
    "Hỗ Trợ": "Hỗ trợ",
    "Tài Liệu Tham Khảo": "Tài liệu tham khảo",
    "Đặc Biệt": "Đặc biệt",
    "Thường Gặp": "Thường gặp",
    "Nguy Cơ": "Nguy cơ",
    "Mức Độ": "Mức độ",
    "Thông Tin": "Thông tin",
    "Khuyến Cáo": "Khuyến cáo",
    "Khuyến Nghị": "Khuyến nghị",
    "Phân Tích": "Phân tích",
    "Quyết Định": "Quyết định",
    "Thành Phần": "Thành phần",
    "Tham Khảo": "Tham khảo",
    "Tham Chiếu": "Tham chiếu",
    "Giá Trị": "Giá trị",
    "Nhịp Tim": "Nhịp tim",
    "Thông Số": "Thông số",
    "Điều Chỉnh": "Điều chỉnh",
    "So Sánh": "So sánh",
    "Cảnh Báo": "Cảnh báo",
    "Ưu Tiên": "Ưu tiên",
    "Kiểm Tra": "Kiểm tra",
    "Kiểm Soát": "Kiểm soát",
    "Dịch Truyền": "Dịch truyền",
    "Mở Mắt": "Mở mắt",
    "Lời Nói": "Lời nói",
    "Vận Động": "Vận động",
    "Giải Thích": "Giải thích",
    "Ý Nghĩa": "Ý nghĩa",
    "Hạng Mục": "Hạng mục",
    "Câu Hỏi": "Câu hỏi",
    "Vận Nhãn": "Vận nhãn",
    "Thị Trường": "Thị trường",
    "Liệt Mặt": "Liệt mặt",
    "Cảm Giác": "Cảm giác",
    "Ngôn Ngữ": "Ngôn ngữ",
    "Khó Phát Âm": "Khó phát âm",
    "Bỏ Qua": "Bỏ qua",
    "Không Chú Ý": "Không chú ý",
    "Tiên Lượng": "Tiên lượng",
    "Xuất Huyết": "Xuất huyết",
    "Vị Trí": "Vị trí",
    "Thể Tích": "Thể tích",
    "Tỷ Lệ": "Tỷ lệ",
    "Tử Vong": "Tử vong",
    "Mô Tả": "Mô tả",
    "Đi Lại": "Đi lại",
    "Tự Chăm Sóc": "Tự chăm sóc",
    "Độc Lập": "Độc lập",
    "Hướng Dẫn": "Hướng dẫn",
    "Đi Đại Tiện": "Đi đại tiện",
    "Đi Tiểu Tiện": "Đi tiểu tiện",
    "Lên Xuống": "Lên xuống",
    "Cầu Thang": "Cầu thang",
    "Tắm Rửa": "Tắm rửa",
    "Mặc Quần Áo": "Mặc quần áo",
    "Ăn Uống": "Ăn uống",
    "Liều Tính Được": "Liều tính được",
    "Chi Tiết": "Chi tiết",
    "Kết Quả": "Kết quả",
    "Diễn Giải": "Diễn giải",
    "Lưu Ý": "Lưu ý",
    "Thang Đo": "Thang đo",
    "Tính Toán": "Tính toán",
    "Mẹo Sử Dụng": "Mẹo sử dụng",
    "Sử Dụng": "Sử dụng",
    "Tình Huống": "Tình huống",
    "Truy Cập": "Truy cập",
    "Độ Nhạy": "Độ nhạy",
    "Kháng Sinh": "Kháng sinh",
    "Điều Trị Bổ Sung": "Điều trị bổ sung",
    "Điều Trị Nguyên Nhân": "Điều trị nguyên nhân",
    "Điều Trị Chính": "Điều trị chính",
    "Phòng Ngừa": "Phòng ngừa",
    "Phòng Ngừa Ban Đầu": "Phòng ngừa ban đầu",
    "Phòng Ngừa Tái Phát": "Phòng ngừa tái phát",
    "Tái Phát": "Tái phát",
    "Nhập Thông Số": "Nhập thông số",
    "Giá Trị Tham Chiếu": "Giá trị tham chiếu",
    "Thuốc Gây Kéo Dài": "Thuốc gây kéo dài",
    "Kiến Thức Bổ Sung": "Kiến thức bổ sung",
    "So Sánh Các Công Thức": "So sánh các công thức",
    "Cách Đo Chính Xác": "Cách đo chính xác",
    "Nguyên Nhân Kéo Dài": "Nguyên nhân kéo dài",
    "Quản Lý Kéo Dài": "Quản lý kéo dài",
    "Thông Tin Bệnh Nhân": "Thông tin bệnh nhân",
    "Thông Số Lâm Sàng": "Thông số lâm sàng",
    "Chi Tiết Điểm": "Chi tiết điểm",
    "Tái Can Thiệp": "Tái can thiệp",
    "Khuyến Cáo Điều Trị": "Khuyến cáo điều trị",
    "Tình Huống Lâm Sàng": "Tình huống lâm sàng",
    "Truy Cập Nhanh": "Truy cập nhanh",
    "Thông Số Bệnh Nhân": "Thông số bệnh nhân",
    "Tra Cứu": "Tra cứu",
    "Kiểm Tra Tương Thích": "Kiểm tra tương thích",
    "Thuốc Khác Đang Truyền": "Thuốc khác đang truyền",
    "Cấp Cứu": "Cấp cứu",
    "Hồi Sức": "Hồi sức",
    "Đánh Giá Ban Đầu": "Đánh giá ban đầu",
    "Đánh Giá Mức Độ Nặng": "Đánh giá mức độ nặng",
    "Đánh Giá Đáp Ứng": "Đánh giá đáp ứng",
    "Tiêu Chuẩn Xét Nghiệm": "Tiêu chuẩn xét nghiệm",
    "Nguyên Nhân Thường Gặp": "Nguyên nhân thường gặp",
    "Bảng Tỷ Lệ Tử Vong Theo Điểm": "Bảng tỷ lệ tử vong theo điểm",
    "Mức Độ Nguy Cơ": "Mức độ nguy cơ",
    "Triệu Chứng Chính": "Triệu chứng chính",
    "Chọn Mức Độ Chức Năng": "Chọn mức độ chức năng",
    "Những Sai Lầm Thường Gặp": "Những sai lầm thường gặp",
    "Hướng Dẫn Đánh Giá": "Hướng dẫn đánh giá",
    "Bảng Phân Loại Nguy Cơ": "Bảng phân loại nguy cơ",
    "Các Trường Hợp Đặc Biệt": "Các trường hợp đặc biệt",
    "Tự Chăm Sóc Cá Nhân": "Tự chăm sóc cá nhân",
    "Kiểm Soát Đại Tiện": "Kiểm soát đại tiện",
    "Kiểm Soát Tiểu Tiện": "Kiểm soát tiểu tiện",
    "Làm Theo Lệnh": "Làm theo lệnh",
    "Mất Điều Hòa Chi": "Mất điều hòa chi",
    "Vận Động Tay": "Vận động tay",
    "Vận Động Chân": "Vận động chân",
    "Mức Độ Ý Thức": "Mức độ ý thức",
    "Câu Hỏi Định Hướng": "Câu hỏi định hướng",
    "Ý Nghĩa Lâm Sàng": "Ý nghĩa lâm sàng",
    "Xuất Huyết Nội Sọ": "Xuất huyết nội sọ",
    "Xuất Huyết Não Thất": "Xuất huyết não thất",
    "Vị Trí Dưới Lề": "Vị trí dưới lề",
    "Thể Tích Máu Tụ": "Thể tích máu tụ",
    "Phụ Nữ Có Thai": "Phụ nữ có thai",
    "Trẻ Em": "Trẻ em",
    "Người Cao Tuổi": "Người cao tuổi",
    "Người Lớn": "Người lớn",
    "Suy Tim": "Suy tim",
    "Suy Thận": "Suy thận",
    "Suy Gan": "Suy gan",
    "Suy Giảm Miễn Dịch": "Suy giảm miễn dịch",
    "Bổ Sung": "Bổ sung",
    "Điện Giải": "Điện giải",
    "Truyền Dịch": "Truyền dịch",
    "Bù Dịch": "Bù dịch",
    "Đánh Giá": "Đánh giá",
    "Phân Loại": "Phân loại",
    "Xử Trí": "Xử trí",
    "Đặc Biệt": "Đặc biệt",
    "Dân Số": "Dân số",
    "Giảm Đau": "Giảm đau",
    "An Thần": "An thần",
    "Kích Động": "Kích động",
    "Điều Chỉnh Theo Nhịp Tim": "Điều chỉnh theo nhịp tim",
    "Tính Toán Gần Đây": "Tính toán gần đây",
    "Thông Tin Bổ Sung": "Thông tin bổ sung",
    "Thông Tin Lâm Sàng": "Thông tin lâm sàng",
    "Thông Tin Thêm": "Thông tin thêm",
    "Thông Tin Về": "Thông tin về",
    "Khuyến Nghị Xử Trí": "Khuyến nghị xử trí",
    "Khuyến Nghị Điều Chỉnh": "Khuyến nghị điều chỉnh",
    "Phân Tích Chi Tiết": "Phân tích chi tiết",
    "Quyết Định Phẫu Thuật": "Quyết định phẫu thuật",
    "Quyết Định Điều Trị": "Quyết định điều trị",
    "Quyết Định Lâm Sàng": "Quyết định lâm sàng",
    "Tiêu Chí Áp Dụng": "Tiêu chí áp dụng",
    "Tiêu Chí Chẩn Đoán": "Tiêu chí chẩn đoán",
    "Tiêu Chí Dương Tính": "Tiêu chí dương tính",
    "Tiêu Chí Nhập ICU": "Tiêu chí nhập ICU",
    "Tiêu Chí Lâm Sàng": "Tiêu chí lâm sàng",
    "Tiêu Chuẩn Chẩn Đoán": "Tiêu chuẩn chẩn đoán",
    "Tiêu Chuẩn Xuất Viện": "Tiêu chuẩn xuất viện",
    "Thành Phần Dung Dịch": "Thành phần dung dịch",
    "Cách Đo QT Interval Chính Xác": "Cách đo QT Interval chính xác",
    "Quản Lý Kéo Dài QT Do Thuốc": "Quản lý kéo dài QT do thuốc",
    "Tra Cứu & Dữ Liệu Kháng Sinh": "Tra cứu & Dữ liệu kháng sinh",
    "Tỷ Lệ Kháng Thuốc": "Tỷ lệ kháng thuốc",
    "Cấp Cứu & Hồi Sức": "Cấp cứu & Hồi sức",
    "Đánh Giá &": "Đánh giá &",
    "Triệu Chứng &": "Triệu chứng &",
    "Bảng Tham Khảo": "Bảng tham khảo",
    "Chi Tiết Điểm Số": "Chi tiết điểm số",
    "Chi Tiết Tính Điểm": "Chi tiết tính điểm",
    "Chi Tiết Tính Toán": "Chi tiết tính toán",
    "Chi Tiết Từng Biến Số": "Chi tiết từng biến số",
    "Chi Tiết Từng Thành Phần": "Chi tiết từng thành phần",
    "Chi Tiết Từng Tiêu Chí": "Chi tiết từng tiêu chí",
    "Chi Tiết Đánh Giá": "Chi tiết đánh giá",
    "Chăm Sóc Điều Dưỡng": "Chăm sóc điều dưỡng",
    "Hướng Dẫn Sử Dụng": "Hướng dẫn sử dụng",
    "Khi Nào Đánh Giá": "Khi nào đánh giá",
    "Cách Đánh Giá": "Cách đánh giá",
    "Đánh Giá Đau": "Đánh giá đau",
    "Diễn Giải Kết Quả": "Diễn giải kết quả",
    "Diễn Giải SOFA-2": "Diễn giải SOFA-2",
    "Diễn Giải MODS": "Diễn giải MODS",
    "Lưu Ý Quan Trọng": "Lưu ý quan trọng",
    "Lưu Ý Y Khoa": "Lưu ý y khoa",
    "Lưu Ý Đặc Biệt": "Lưu ý đặc biệt",
    "Lưu Ý Điều Trị": "Lưu ý điều trị",
    "Phân Tích Từng": "Phân tích từng",
    "Phân Tích &": "Phân tích &",
}

# Thư mục cần quét
DIRECTORIES = [
    "protocols",
    "pages",
    "scores",
    "labs",
    "critical_care",
    "antibiotics",
    "drugs",
    "components",
    "ventilator",
    "diagnosis",
]

# File extensions cần quét
EXTENSIONS = [".py"]

# Files/patterns cần bỏ qua
IGNORE_PATTERNS = [
    "__pycache__",
    ".git",
    "node_modules",
    "venv",
    "env",
    ".pytest_cache",
    "check_",
    "fix_",
    "test_",
    "find_",
    "vietnamese_",
    "quick_fix_",
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


def fix_capitalization_in_file(file_path: Path, dry_run: bool = True) -> tuple[int, list[str]]:
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
    sorted_fixes = sorted(COMMON_FIXES.items(), key=lambda x: len(x[0]), reverse=True)
    
    for wrong, correct in sorted_fixes:
        # Tìm tất cả các occurrences
        pattern = re.escape(wrong)
        matches = list(re.finditer(pattern, content))
        
        if matches:
            # Thay thế từ cuối lên đầu để không làm thay đổi index
            for match in reversed(matches):
                start, end = match.span()
                # Kiểm tra context - không thay thế nếu là trong comment hoặc string đặc biệt
                before = content[max(0, start-50):start]
                after = content[end:min(len(content), end+50)]
                
                # Bỏ qua nếu là trong docstring hoặc comment đặc biệt
                if '"""' in before[-100:] or "'''" in before[-100:]:
                    # Kiểm tra xem có phải là docstring không
                    continue
                
                # Bỏ qua nếu là trong import hoặc code Python
                if any(keyword in before[-50:] for keyword in ['import ', 'from ', 'def ', 'class ', '=']):
                    # Kiểm tra xem có phải là trong string không
                    if not (before.rstrip().endswith('"') or before.rstrip().endswith("'")):
                        continue
                
                content = content[:start] + correct + content[end:]
                line_num = original_content[:start].count('\n') + 1
                changes.append(f"  - '{wrong}' → '{correct}' (dòng {line_num})")
                total_replacements += 1
    
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


def main():
    """Main function"""
    import sys
    
    # Kiểm tra argument
    dry_run = True
    if len(sys.argv) > 1 and sys.argv[1] == "--apply":
        dry_run = False
        print("⚠️  CHẾ ĐỘ SỬA FILE - Các thay đổi sẽ được lưu!\n")
    else:
        print("🔍 CHẾ ĐỘ DRY RUN - Chỉ báo cáo, không sửa file\n")
        print("💡 Để áp dụng thay đổi, chạy: python quick_fix_vietnamese_caps.py --apply\n")
    
    print("=" * 60)
    print("🔧 SỬA LỖI VIẾT HOA TIẾNG VIỆT - QUICK FIX")
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
                replacements, changes = fix_capitalization_in_file(file_path, dry_run=dry_run)
                
                if replacements > 0:
                    total_changes += replacements
                    files_changed.append((file_path, replacements, changes))
                    if dry_run:
                        print(f"📝 {file_path}: {replacements} thay đổi")
                        for change in changes[:3]:  # Chỉ hiển thị 3 thay đổi đầu
                            print(change)
                        if len(changes) > 3:
                            print(f"   ... và {len(changes) - 3} thay đổi khác")
                    else:
                        print(f"✅ {file_path}: {replacements} thay đổi")
    
    # Tóm tắt
    print()
    print("=" * 60)
    print("📊 TÓM TẮT")
    print("=" * 60)
    print(f"Tổng số file đã quét: {total_files}")
    print(f"Tổng số file có lỗi: {len(files_changed)}")
    print(f"Tổng số thay đổi: {total_changes}")
    print()
    
    if files_changed:
        print("📝 Các file có lỗi:")
        for file_path, count, _ in files_changed[:30]:  # Hiển thị 30 file đầu
            print(f"  - {file_path} ({count} thay đổi)")
        if len(files_changed) > 30:
            print(f"  ... và {len(files_changed) - 30} file khác")
    
    print()
    if dry_run:
        print("💡 Chạy với --apply để áp dụng các thay đổi")
    else:
        print("✅ Hoàn thành!")
    print()


if __name__ == "__main__":
    main()

