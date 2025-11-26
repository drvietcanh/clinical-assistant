"""
Script để quét và tìm các lỗi viết hoa tiếng Việt
Tìm các pattern: "Chữ Hoa chữ thường" (ví dụ: "Phòng ngừa" nên là "Phòng Ngừa")
"""

import re
import os
from pathlib import Path

# Các cụm từ tiếng Việt phổ biến cần viết hoa TẤT CẢ các từ
# Format: (từ đầu, từ thứ 2, ...) - tất cả đều phải viết hoa
COMMON_PHRASES = [
    ("phòng", "ngừa"),           # Phòng Ngừa
    ("phụ", "nữ", "có", "thai"), # Phụ Nữ Có Thai
    ("suy", "thận"),             # Suy Thận
    ("suy", "gan"),              # Suy Gan
    ("suy", "tim"),              # Suy Tim
    ("suy", "giảm", "miễn", "dịch"), # Suy Giảm Miễn Dịch
    ("trẻ", "em"),               # Trẻ Em
    ("người", "cao", "tuổi"),    # Người Cao Tuổi
    ("người", "lớn"),            # Người Lớn
    ("điều", "chỉnh"),           # Điều Chỉnh
    ("điều", "trị"),             # Điều Trị
    ("theo", "dõi"),             # Theo Dõi
    ("chỉ", "định"),             # Chỉ Định
    ("mục", "tiêu"),             # Mục Tiêu
    ("nguyên", "nhân"),         # Nguyên Nhân
    ("triệu", "chứng"),         # Triệu Chứng
    ("tiêu", "chuẩn"),          # Tiêu Chuẩn
    ("xuất", "viện"),           # Xuất Viện
    ("chẩn", "đoán"),           # Chẩn Đoán
    ("phương", "pháp"),         # Phương Pháp
    ("dấu", "hiệu"),            # Dấu Hiệu
    ("cảnh", "báo"),             # Cảnh Báo
    ("tái", "phát"),             # Tái Phát
    ("hồi", "sức", "hỗ", "trợ"), # Hồi Sức Hỗ Trợ
    ("hỗ", "trợ"),              # Hỗ Trợ
    ("bổ", "sung"),              # Bổ Sung
    ("điện", "giải"),            # Điện Giải
    ("truyền", "dịch"),          # Truyền Dịch
    ("bù", "dịch"),              # Bù Dịch
    ("kháng", "sinh"),           # Kháng Sinh
    ("đánh", "giá"),             # Đánh Giá
    ("phân", "loại"),            # Phân Loại
    ("phân", "tầng"),            # Phân Tầng
    ("nguy", "cơ"),              # Nguy Cơ
    ("mức", "độ"),               # Mức Độ
    ("xử", "trí"),               # Xử Trí
    ("đặc", "biệt"),             # Đặc Biệt
    ("dân", "số"),               # Dân Số
    ("quản", "lý"),              # Quản Lý
    ("kiểm", "soát"),            # Kiểm Soát
    ("giảm", "đau"),             # Giảm Đau
    ("an", "thần"),              # An Thần
    ("kích", "động"),            # Kích Động
    ("điều", "trị", "bổ", "sung"), # Điều Trị Bổ Sung
    ("điều", "trị", "nguyên", "nhân"), # Điều Trị Nguyên Nhân
    ("điều", "trị", "chính"),   # Điều Trị Chính
    ("phòng", "ngừa", "ban", "đầu"), # Phòng Ngừa Ban Đầu
    ("phòng", "ngừa", "tái", "phát"), # Phòng Ngừa Tái Phát
    ("tái", "phát", "lần"),      # Tái Phát Lần
    ("điều", "chỉnh", "theo", "nhịp", "tim"), # Điều Chỉnh Theo Nhịp Tim
    ("nhập", "thông", "số"),     # Nhập Thông Số
    ("nhịp", "tim"),             # Nhịp Tim
    ("phân", "tích"),            # Phân Tích
    ("giá", "trị", "tham", "chiếu"), # Giá Trị Tham Chiếu
    ("giá", "trị"),              # Giá Trị
    ("tham", "chiếu"),           # Tham Chiếu
    ("thuốc", "gây", "kéo", "dài"), # Thuốc Gây Kéo Dài
    ("thường", "gặp"),           # Thường Gặp
    ("kiến", "thức", "bổ", "sung"), # Kiến Thức Bổ Sung
    ("so", "sánh", "các", "công", "thức"), # So Sánh Các Công Thức
    ("so", "sánh"),              # So Sánh
    ("cách", "đo", "chính", "xác"), # Cách Đo Chính Xác
    ("nguyên", "nhân", "kéo", "dài"), # Nguyên Nhân Kéo Dài
    ("quản", "lý", "kéo", "dài", "qt", "do", "thuốc"), # Quản Lý Kéo Dài QT Do Thuốc
    ("thông", "tin", "bệnh", "nhân"), # Thông Tin Bệnh Nhân
    ("khuyến", "cáo"),           # Khuyến Cáo
    ("tài", "liệu", "tham", "khảo"), # Tài Liệu Tham Khảo
    ("thông", "số", "lâm", "sàng"), # Thông Số Lâm Sàng
    ("chi", "tiết", "điểm"),     # Chi Tiết Điểm
    ("nguy", "cơ", "tử", "vong"), # Nguy Cơ Tử Vong
    ("tái", "can", "thiệp"),     # Tái Can Thiệp
    ("khuyến", "cáo", "điều", "trị"), # Khuyến Cáo Điều Trị
    ("mẹo", "sử", "dụng"),      # Mẹo Sử Dụng
    ("sử", "dụng"),             # Sử Dụng
    ("tính", "toán", "gần", "đây"), # Tính Toán Gần Đây
    ("tình", "huống", "lâm", "sàng"), # Tình Huống Lâm Sàng
    ("truy", "cập", "nhanh"),   # Truy Cập Nhanh
    ("thông", "số", "bệnh", "nhân"), # Thông Số Bệnh Nhân
    ("tra", "cứu", "dữ", "liệu", "kháng", "sinh"), # Tra Cứu & Dữ Liệu Kháng Sinh
    ("độ", "nhạy"),             # Độ Nhạy
    ("tỷ", "lệ", "kháng", "thuốc"), # Tỷ Lệ Kháng Thuốc
    ("ưu", "tiên"),             # Ưu Tiên
    ("kiểm", "tra", "tương", "thích"), # Kiểm Tra Tương Thích
    ("thuốc", "khác", "đang", "truyền"), # Thuốc Khác Đang Truyền
    ("dịch", "truyền"),         # Dịch Truyền
    ("mở", "mắt"),              # Mở Mắt
    ("lời", "nói"),             # Lời Nói
    ("vận", "động"),           # Vận Động
    ("giải", "thích"),         # Giải Thích
    ("ý", "nghĩa", "lâm", "sàng"), # Ý Nghĩa Lâm Sàng
    ("hạng", "mục"),           # Hạng Mục
    ("mức", "độ", "ý", "thức"), # Mức Độ Ý Thức
    ("câu", "hỏi", "định", "hướng"), # Câu Hỏi Định Hướng
    ("làm", "theo", "lệnh"),   # Làm Theo Lệnh
    ("vận", "nhãn"),           # Vận Nhãn
    ("thị", "trường"),         # Thị Trường
    ("liệt", "mặt"),           # Liệt Mặt
    ("vận", "động", "tay"),    # Vận Động Tay
    ("vận", "động", "chân"),   # Vận Động Chân
    ("mất", "điều", "hòa", "chi"), # Mất Điều Hòa Chi
    ("cảm", "giác"),           # Cảm Giác
    ("ngôn", "ngữ"),           # Ngôn Ngữ
    ("khó", "phát", "âm"),     # Khó Phát Âm
    ("bỏ", "qua"),             # Bỏ Qua
    ("không", "chú", "ý"),     # Không Chú Ý
    ("tiên", "lượng"),         # Tiên Lượng
    ("xuất", "huyết", "nội", "sọ"), # Xuất Huyết Nội Sọ
    ("xuất", "huyết", "não", "thất"), # Xuất Huyết Não Thất
    ("vị", "trí", "dưới", "lề"), # Vị Trí Dưới Lề
    ("thể", "tích", "máu", "tụ"), # Thể Tích Máu Tụ
    ("bảng", "tỷ", "lệ", "tử", "vong", "theo", "điểm"), # Bảng Tỷ Lệ Tử Vong Theo Điểm
    ("mức", "độ", "nguy", "cơ"), # Mức Độ Nguy Cơ
    ("tỷ", "lệ", "tử", "vong"), # Tỷ Lệ Tử Vong
    ("triệu", "chứng", "chính"), # Triệu Chứng Chính
    ("tử", "vong"),              # Tử Vong
    ("chọn", "mức", "độ", "chức", "năng"), # Chọn Mức Độ Chức Năng
    ("mô", "tả"),                  # Mô Tả
    ("đi", "lại"),                 # Đi Lại
    ("tự", "chăm", "sóc"),         # Tự Chăm Sóc
    ("độc", "lập"),                # Độc Lập
    ("những", "sai", "lầm", "thường", "gặp"), # Những Sai Lầm Thường Gặp
    ("hướng", "dẫn", "đánh", "giá"), # Hướng Dẫn Đánh Giá
    ("bảng", "phân", "loại", "nguy", "cơ"), # Bảng Phân Loại Nguy Cơ
    ("các", "trường", "hợp", "đặc", "biệt"), # Các Trường Hợp Đặc Biệt
    ("đi", "đại", "tiện"),        # Đi Đại Tiện
    ("đi", "tiểu", "tiện"),       # Đi Tiểu Tiện
    ("tự", "chăm", "sóc", "cá", "nhân"), # Tự Chăm Sóc Cá Nhân
    ("lên", "xuống", "cầu", "thang"), # Lên Xuống Cầu Thang
    ("tắm", "rửa"),              # Tắm Rửa
    ("mặc", "quần", "áo"),        # Mặc Quần Áo
    ("kiểm", "soát", "đại", "tiện"), # Kiểm Soát Đại Tiện
    ("kiểm", "soát", "tiểu", "tiện"), # Kiểm Soát Tiểu Tiện
    ("ăn", "uống"),               # Ăn Uống
    ("liều", "tính", "được"),      # Liều Tính Được
]

# Pattern để tìm các từ có chữ cái đầu viết hoa
CAPITALIZED_WORD_PATTERN = r'\b[A-ZÀÁẢÃẠĂẰẮẲẴẶÂẦẤẨẪẬĐÈÉẺẼẸÊỀẾỂỄỆÌÍỈĨỊÒÓỎÕỌÔỒỐỔỖỘƠỜỚỞỠỢÙÚỦŨỤƯỪỨỬỮỰỲÝỶỸỴ][a-zàáảãạăằắẳẵặâầấẩẫậđèéẻẽẹêềếểễệìíỉĩịòóỏõọôồốổỗộơờớởỡợùúủũụưừứửữựỳýỷỹỵ\s]+'

def find_capitalization_errors(file_path):
    """Tìm các lỗi viết hoa trong file"""
    errors = []
    
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
            lines = content.split('\n')
            
        for line_num, line in enumerate(lines, 1):
            # Chỉ kiểm tra trong markdown headers và bold text
            if 'st.markdown' in line or 'st.subheader' in line or 'st.header' in line:
                # Tìm text trong dấu ngoặc kép hoặc markdown
                # Pattern: "### ..." hoặc "**...**" hoặc '...'
                text_patterns = [
                    r'###\s+(.+?)(?:\n|$)',  # ### Header
                    r'\*\*(.+?)\*\*',        # **Bold**
                    r'"([^"]+)"',            # "Text"
                    r"'([^']+)'",            # 'Text'
                ]
                
                for pattern in text_patterns:
                    matches = re.finditer(pattern, line)
                    for match in matches:
                        text = match.group(1)
                        if not text:
                            continue
                        
                        # Kiểm tra từng cụm từ phổ biến
                        for phrase in COMMON_PHRASES:
                            if len(phrase) < 2:
                                continue
                            
                            # Tạo pattern để tìm cụm từ này
                            # Ví dụ: tìm "phòng ngừa" (có thể viết hoa một phần)
                            phrase_pattern = r'\b'
                            for i, word in enumerate(phrase):
                                if i > 0:
                                    phrase_pattern += r'\s+'
                                # Cho phép chữ cái đầu viết hoa hoặc thường
                                phrase_pattern += f'[{word[0].upper()}{word[0].lower()}]{re.escape(word[1:])}'
                            phrase_pattern += r'\b'
                            
                            phrase_match = re.search(phrase_pattern, text, re.IGNORECASE)
                            if phrase_match:
                                matched_text = phrase_match.group(0)
                                words = matched_text.split()
                                
                                # Kiểm tra xem có từ nào không viết hoa đúng không
                                # Tất cả các từ trong cụm đều phải viết hoa chữ cái đầu
                                expected_words = [w.capitalize() for w in phrase]
                                actual_words = words[:len(phrase)]
                                
                                # So sánh từng từ
                                has_error = False
                                corrected = []
                                for i, (actual, expected) in enumerate(zip(actual_words, expected_words)):
                                    # Chuẩn hóa để so sánh (bỏ dấu)
                                    actual_normalized = actual.lower()
                                    expected_normalized = expected.lower()
                                    
                                    if actual_normalized == expected_normalized:
                                        # Kiểm tra viết hoa
                                        if actual[0].islower() and expected[0].isupper():
                                            has_error = True
                                            corrected.append(expected)
                                        else:
                                            corrected.append(actual)
                                    else:
                                        corrected.append(actual)
                                
                                if has_error:
                                    # Tìm vị trí trong line
                                    start_pos = line.find(matched_text)
                                    errors.append({
                                        'line': line_num,
                                        'text': matched_text,
                                        'expected': ' '.join(corrected),
                                        'context': line.strip()[:150],
                                        'phrase': ' '.join(phrase)
                                    })
                                    break  # Chỉ báo lỗi một lần cho mỗi cụm từ
                                    
    except Exception as e:
        print(f"Error reading {file_path}: {e}")
    
    return errors

def scan_directory(directory='protocols'):
    """Quét toàn bộ thư mục"""
    all_errors = []
    
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith('.py'):
                file_path = Path(root) / file
                errors = find_capitalization_errors(file_path)
                if errors:
                    all_errors.append({
                        'file': str(file_path),
                        'errors': errors
                    })
    
    return all_errors

def main():
    print("🔍 Đang quét các lỗi viết hoa tiếng Việt...\n")
    
    errors = scan_directory('protocols')
    
    if not errors:
        print("✅ Không tìm thấy lỗi viết hoa!")
        return
    
    print(f"📊 Tìm thấy {len(errors)} file có lỗi:\n")
    
    for file_info in errors:
        print(f"📄 {file_info['file']}")
        print(f"   Có {len(file_info['errors'])} lỗi:\n")
        
        for error in file_info['errors']:
            print(f"   Dòng {error['line']}: {error['text']}")
            if 'suggestion' in error:
                print(f"   💡 Gợi ý: {error['suggestion']}")
            print(f"   📝 Context: {error['context']}")
            print()

if __name__ == '__main__':
    main()

