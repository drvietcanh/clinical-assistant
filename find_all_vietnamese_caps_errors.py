"""
Script tìm tất cả các lỗi viết hoa tiếng Việt tương tự
Tìm các pattern: Chữ Hoa chữ thường + khoảng trắng + Chữ Hoa chữ thường
"""

import re
from pathlib import Path
from collections import defaultdict

# Các cụm từ tiếng Việt phổ biến chỉ nên viết hoa chữ cái đầu từ đầu tiên
COMMON_VIETNAMESE_PHRASES = {
    # 2 từ - chỉ từ đầu viết hoa
    'thần kinh': 'Thần kinh',
    'tiêu hóa': 'Tiêu hóa',
    'tùy chỉnh': 'tùy chỉnh',
    'điều trị': 'Điều trị',
    'chẩn đoán': 'Chẩn đoán',
    'theo dõi': 'Theo dõi',
    'phân loại': 'Phân loại',
    'phân tầng': 'Phân tầng',
    'đánh giá': 'Đánh giá',
    'xử trí': 'Xử trí',
    'quản lý': 'Quản lý',
    'chỉ định': 'Chỉ định',
    'triệu chứng': 'Triệu chứng',
    'dấu hiệu': 'Dấu hiệu',
    'tiêu chuẩn': 'Tiêu chuẩn',
    'tiêu chí': 'Tiêu chí',
    'nguyên nhân': 'Nguyên nhân',
    'mục tiêu': 'Mục tiêu',
    'hỗ trợ': 'Hỗ trợ',
    'tài liệu': 'Tài liệu',
    'tham khảo': 'Tham khảo',
    'đặc biệt': 'Đặc biệt',
    'thường gặp': 'Thường gặp',
    'nguy cơ': 'Nguy cơ',
    'mức độ': 'Mức độ',
    'thông tin': 'Thông tin',
    'khuyến cáo': 'Khuyến cáo',
    'khuyến nghị': 'Khuyến nghị',
    'phân tích': 'Phân tích',
    'quyết định': 'Quyết định',
    'thành phần': 'Thành phần',
    'tham chiếu': 'Tham chiếu',
    'giá trị': 'Giá trị',
    'nhịp tim': 'Nhịp tim',
    'thông số': 'Thông số',
    'điều chỉnh': 'Điều chỉnh',
    'so sánh': 'So sánh',
    'cảnh báo': 'Cảnh báo',
    'ưu tiên': 'Ưu tiên',
    'kiểm tra': 'Kiểm tra',
    'kiểm soát': 'Kiểm soát',
    'dịch truyền': 'Dịch truyền',
    'mở mắt': 'Mở mắt',
    'lời nói': 'Lời nói',
    'vận động': 'Vận động',
    'giải thích': 'Giải thích',
    'ý nghĩa': 'Ý nghĩa',
    'hạng mục': 'Hạng mục',
    'câu hỏi': 'Câu hỏi',
    'vận nhãn': 'Vận nhãn',
    'thị trường': 'Thị trường',
    'liệt mặt': 'Liệt mặt',
    'cảm giác': 'Cảm giác',
    'ngôn ngữ': 'Ngôn ngữ',
    'khó phát âm': 'Khó phát âm',
    'bỏ qua': 'Bỏ qua',
    'không chú ý': 'Không chú ý',
    'tiên lượng': 'Tiên lượng',
    'xuất huyết': 'Xuất huyết',
    'vị trí': 'Vị trí',
    'thể tích': 'Thể tích',
    'tỷ lệ': 'Tỷ lệ',
    'tử vong': 'Tử vong',
    'mô tả': 'Mô tả',
    'đi lại': 'Đi lại',
    'tự chăm sóc': 'Tự chăm sóc',
    'độc lập': 'Độc lập',
    'hướng dẫn': 'Hướng dẫn',
    'phòng ngừa': 'Phòng ngừa',
    'tái phát': 'Tái phát',
    'bổ sung': 'Bổ sung',
    'điện giải': 'Điện giải',
    'truyền dịch': 'Truyền dịch',
    'bù dịch': 'Bù dịch',
    'giảm đau': 'Giảm đau',
    'an thần': 'An thần',
    'kích động': 'Kích động',
    'dân số': 'Dân số',
    'suy tim': 'Suy tim',
    'suy thận': 'Suy thận',
    'suy gan': 'Suy gan',
    'cấp cứu': 'Cấp cứu',
    'hồi sức': 'Hồi sức',
    'kháng sinh': 'Kháng sinh',
    'người lớn': 'Người lớn',
    'phụ nữ có thai': 'Phụ nữ có thai',
    'trẻ em': 'Trẻ em',
    'người cao tuổi': 'Người cao tuổi',
    'suy giảm miễn dịch': 'Suy giảm miễn dịch',
    'tiêu chảy': 'Tiêu chảy',
    'nội tiết': 'Nội tiết',
    'chuyển hóa': 'Chuyển hóa',
    'huyết học': 'Huyết học',
    'ung thư': 'Ung thư',
    'hô hấp': 'Hô hấp',
    'tim mạch': 'Tim mạch',
    'truyền nhiễm': 'Truyền nhiễm',
    'miễn dịch': 'Miễn dịch',
    'gây mê': 'Gây mê',
    'hồi sức': 'Hồi sức',
    'cấp cứu': 'Cấp cứu',
}

# Pattern để tìm các từ tiếng Việt có 2 từ đều viết hoa
VIETNAMESE_DOUBLE_CAP_PATTERN = re.compile(
    r'\b([A-ZÀÁẢÃẠĂẰẮẲẴẶÂẦẤẨẪẬĐÈÉẺẼẸÊỀẾỂỄỆÌÍỈĨỊÒÓỎÕỌÔỒỐỔỖỘƠỜỚỞỠỢÙÚỦŨỤƯỪỨỬỮỰỲÝỶỸỴ][a-zàáảãạăằắẳẵặâầấẩẫậđèéẻẽẹêềếểễệìíỉĩịòóỏõọôồốổỗộơờớởỡợùúủũụưừứửữựỳýỷỹỵ]+)\s+([A-ZÀÁẢÃẠĂẰẮẲẴẶÂẦẤẨẪẬĐÈÉẺẼẸÊỀẾỂỄỆÌÍỈĨỊÒÓỎÕỌÔỒỐỔỖỘƠỜỚỞỠỢÙÚỦŨỤƯỪỨỬỮỰỲÝỶỸỴ][a-zàáảãạăằắẳẵặâầấẩẫậđèéẻẽẹêềếểễệìíỉĩịòóỏõọôồốổỗộơờớởỡợùúủũụưừứửữựỳýỷỹỵ]+)'
)

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
]

def should_process_file(file_path: Path) -> bool:
    """Kiểm tra xem file có nên được xử lý không"""
    file_str = str(file_path)
    for pattern in IGNORE_PATTERNS:
        if pattern in file_str:
            return False
    return file_path.suffix in [".py", ".md"]

def find_caps_errors_in_file(file_path: Path) -> list:
    """Tìm các lỗi viết hoa trong file"""
    errors = []
    
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
            lines = content.split('\n')
    except Exception as e:
        return errors
    
    for line_num, line in enumerate(lines, 1):
        # Tìm các pattern có 2 từ đều viết hoa
        matches = VIETNAMESE_DOUBLE_CAP_PATTERN.finditer(line)
        
        for match in matches:
            word1 = match.group(1)
            word2 = match.group(2)
            phrase = f"{word1} {word2}"
            phrase_lower = phrase.lower()
            
            # Kiểm tra xem có phải là cụm từ phổ biến không
            if phrase_lower in COMMON_VIETNAMESE_PHRASES:
                expected = COMMON_VIETNAMESE_PHRASES[phrase_lower]
                if phrase != expected:
                    # Bỏ qua nếu là trong comment hoặc string đặc biệt
                    # Nhưng vẫn báo để review
                    errors.append({
                        'line': line_num,
                        'wrong': phrase,
                        'correct': expected,
                        'context': line.strip()[:100],
                        'file': str(file_path)
                    })
    
    return errors

def main():
    """Main function"""
    print("=" * 70)
    print("🔍 TÌM TẤT CẢ CÁC LỖI VIẾT HOA TIẾNG VIỆT")
    print("=" * 70)
    print()
    
    all_errors = []
    files_with_errors = defaultdict(list)
    
    for directory in DIRECTORIES:
        dir_path = Path(directory)
        if not dir_path.exists():
            continue
        
        print(f"📂 Quét thư mục: {directory}")
        
        for file_path in dir_path.rglob("*"):
            if file_path.is_file() and should_process_file(file_path):
                errors = find_caps_errors_in_file(file_path)
                if errors:
                    all_errors.extend(errors)
                    files_with_errors[str(file_path)] = errors
    
    if not all_errors:
        print("\n✅ Không tìm thấy lỗi viết hoa!")
        return
    
    print(f"\n📊 Tìm thấy {len(all_errors)} lỗi trong {len(files_with_errors)} files:\n")
    
    # Nhóm theo loại lỗi
    error_types = defaultdict(list)
    for error in all_errors:
        error_types[error['wrong']].append(error)
    
    for wrong_phrase, errors in sorted(error_types.items()):
        print(f"\n❌ '{wrong_phrase}' → '{errors[0]['correct']}' ({len(errors)} lần)")
        for error in errors[:5]:  # Hiển thị 5 file đầu
            print(f"   📄 {error['file']}:{error['line']}")
            print(f"      {error['context']}")
        if len(errors) > 5:
            print(f"   ... và {len(errors) - 5} lần khác")
    
    print("\n" + "=" * 70)
    print(f"Tổng cộng: {len(all_errors)} lỗi trong {len(files_with_errors)} files")
    print("=" * 70)

if __name__ == "__main__":
    main()
