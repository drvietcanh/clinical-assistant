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
    "Chăm Sóc Điều Dưỡng": "Chăm sóc điều dưỡng",
    "Hướng Dẫn Sử Dụng": "Hướng dẫn sử dụng",
    "Khi Nào Đánh Giá": "Khi nào đánh giá",
    "Cách Đánh Giá": "Cách đánh giá",
    "Đánh Giá Đau": "Đánh giá đau",
    "Diễn Giải": "Diễn giải",
    "Diễn Giải Kết Quả": "Diễn giải kết quả",
    "Diễn Giải SOFA-2": "Diễn giải SOFA-2",
    "Diễn Giải MODS": "Diễn giải MODS",
    "Lưu Ý": "Lưu ý",
    "Lưu Ý Quan Trọng": "Lưu ý quan trọng",
    "Lưu Ý Y Khoa": "Lưu ý y khoa",
    "Lưu Ý Đặc Biệt": "Lưu ý đặc biệt",
    "Lưu Ý Điều Trị": "Lưu ý điều trị",
    "Thang Đo": "Thang đo",
    "Tính Toán Gần Đây": "Tính toán gần đây",
    "Mẹo Sử Dụng": "Mẹo sử dụng",
    "Tài Liệu Tham Khảo": "Tài liệu tham khảo",
    "Thông Tin Bổ Sung": "Thông tin bổ sung",
    "Thông Tin Bệnh Nhân": "Thông tin bệnh nhân",
    "Thông Tin Lâm Sàng": "Thông tin lâm sàng",
    "Thông Tin Thêm": "Thông tin thêm",
    "Thông Tin Về": "Thông tin về",
    "Khuyến Nghị Xử Trí": "Khuyến nghị xử trí",
    "Khuyến Nghị Điều Trị": "Khuyến nghị điều trị",
    "Khuyến Nghị Điều Chỉnh": "Khuyến nghị điều chỉnh",
    "Phân Tích Chi tiết": "Phân tích chi tiết",
    "Phân Tích Từng": "Phân tích từng",
    "Phân Tích &": "Phân tích &",
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
    "Điều Chỉnh Theo Nhịp Tim": "Điều chỉnh theo nhịp tim",
    "Nhập Thông Số": "Nhập thông số",
    "Nhịp Tim": "Nhịp tim",
    "Phân Tích": "Phân tích",
    "Giá Trị Tham Chiếu": "Giá trị tham chiếu",
    "Giá Trị": "Giá trị",
    "Tham Chiếu": "Tham chiếu",
    "Thuốc Gây Kéo Dài": "Thuốc gây kéo dài",
    "Thường Gặp": "Thường gặp",
    "Kiến Thức Bổ Sung": "Kiến thức bổ sung",
    "So Sánh Các Công Thức": "So sánh các công thức",
    "So Sánh": "So sánh",
    "Cách Đo QT Interval Chính Xác": "Cách đo QT Interval chính xác",
    "Cách Đo Chính Xác": "Cách đo chính xác",
    "Nguyên Nhân Kéo Dài": "Nguyên nhân kéo dài",
    "Quản Lý Kéo Dài QT Do Thuốc": "Quản lý kéo dài QT do thuốc",
    "Thông Tin Bệnh Nhân": "Thông tin bệnh nhân",
    "Khuyến Cáo": "Khuyến cáo",
    "Tài Liệu Tham Khảo": "Tài liệu tham khảo",
    "Thông Số Lâm Sàng": "Thông số lâm sàng",
    "Chi Tiết Điểm": "Chi tiết điểm",
    "Nguy Cơ Tử Vong": "Nguy cơ tử vong",
    "Tái Can Thiệp": "Tái can thiệp",
    "Khuyến Cáo Điều Trị": "Khuyến cáo điều trị",
    "Sử Dụng": "Sử dụng",
    "Tình Huống Lâm Sàng": "Tình huống lâm sàng",
    "Truy Cập Nhanh": "Truy cập nhanh",
    "Thông Số Bệnh Nhân": "Thông số bệnh nhân",
    "Triệu Chứng": "Triệu chứng",
    "Tra Cứu & Dữ Liệu Kháng Sinh": "Tra cứu & Dữ liệu kháng sinh",
    "Độ Nhạy": "Độ nhạy",
    "Tỷ Lệ Kháng Thuốc": "Tỷ lệ kháng thuốc",
    "Ưu Tiên": "Ưu tiên",
    "Kiểm Tra Tương Thích": "Kiểm tra tương thích",
    "Thuốc Khác Đang Truyền": "Thuốc khác đang truyền",
    "Dịch Truyền": "Dịch truyền",
    "Cấp Cứu & Hồi Sức": "Cấp cứu & Hồi sức",
    "Đánh Giá Ban Đầu": "Đánh giá ban đầu",
    "Đánh Giá Mức Độ Nặng": "Đánh giá mức độ nặng",
    "Đánh Giá Đáp Ứng": "Đánh giá đáp ứng",
    "Đánh Giá &": "Đánh giá &",
    "Tiêu Chuẩn Xét Nghiệm": "Tiêu chuẩn xét nghiệm",
    "Triệu Chứng &": "Triệu chứng &",
    "Nguyên Nhân Thường Gặp": "Nguyên nhân thường gặp",
    "Mở Mắt": "Mở mắt",
    "Lời Nói": "Lời nói",
    "Vận Động": "Vận động",
    "Giải Thích": "Giải thích",
    "Ý Nghĩa Lâm Sàng": "Ý nghĩa lâm sàng",
    "Hạng Mục": "Hạng mục",
    "Mức Độ Ý Thức": "Mức độ ý thức",
    "Câu Hỏi Định Hướng": "Câu hỏi định hướng",
    "Làm Theo Lệnh": "Làm theo lệnh",
    "Vận Nhãn": "Vận nhãn",
    "Thị Trường": "Thị trường",
    "Liệt Mặt": "Liệt mặt",
    "Vận Động Tay": "Vận động tay",
    "Vận Động Chân": "Vận động chân",
    "Mất Điều Hòa Chi": "Mất điều hòa chi",
    "Cảm Giác": "Cảm giác",
    "Ngôn Ngữ": "Ngôn ngữ",
    "Khó Phát Âm": "Khó phát âm",
    "Bỏ Qua": "Bỏ qua",
    "Không Chú Ý": "Không chú ý",
    "Tiên Lượng": "Tiên lượng",
    "Xuất Huyết Nội Sọ": "Xuất huyết nội sọ",
    "Xuất Huyết Não Thất": "Xuất huyết não thất",
    "Vị Trí Dưới Lề": "Vị trí dưới lề",
    "Thể Tích Máu Tụ": "Thể tích máu tụ",
    "Bảng Tỷ Lệ Tử Vong Theo Điểm": "Bảng tỷ lệ tử vong theo điểm",
    "Mức Độ Nguy Cơ": "Mức độ nguy cơ",
    "Tỷ Lệ Tử Vong": "Tỷ lệ tử vong",
    "Triệu Chứng Chính": "Triệu chứng chính",
    "Tử Vong": "Tử vong",
    "Chọn Mức Độ Chức Năng": "Chọn mức độ chức năng",
    "Mô Tả": "Mô tả",
    "Đi Lại": "Đi lại",
    "Tự Chăm Sóc": "Tự chăm sóc",
    "Độc Lập": "Độc lập",
    "Những Sai Lầm Thường Gặp": "Những sai lầm thường gặp",
    "Hướng Dẫn Đánh Giá": "Hướng dẫn đánh giá",
    "Bảng Phân Loại Nguy Cơ": "Bảng phân loại nguy cơ",
    "Các Trường Hợp Đặc Biệt": "Các trường hợp đặc biệt",
    "Đi Đại Tiện": "Đi đại tiện",
    "Đi Tiểu Tiện": "Đi tiểu tiện",
    "Tự Chăm Sóc Cá Nhân": "Tự chăm sóc cá nhân",
    "Lên Xuống Cầu Thang": "Lên xuống cầu thang",
    "Tắm Rửa": "Tắm rửa",
    "Mặc Quần Áo": "Mặc quần áo",
    "Kiểm Soát Đại Tiện": "Kiểm soát đại tiện",
    "Kiểm Soát Tiểu Tiện": "Kiểm soát tiểu tiện",
    "Ăn Uống": "Ăn uống",
    
    # Từ đơn lẻ (cần cẩn thận với context)
    "Chi Tiết": "Chi tiết",
    "Kết Quả": "Kết quả",
    "Đánh Giá": "Đánh giá",
    "Thông Tin": "Thông tin",
    "Khuyến Nghị": "Khuyến nghị",
    "Phân Tích": "Phân tích",
    "Quyết Định": "Quyết định",
    "Tiêu Chí": "Tiêu chí",
    "Tiêu Chuẩn": "Tiêu chuẩn",
    "Thành Phần": "Thành phần",
    "Tham Khảo": "Tham khảo",
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

