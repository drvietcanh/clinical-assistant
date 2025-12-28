"""
Script quét cực kỳ chi tiết để tìm các lỗi viết hoa tiếng Việt còn sót lại
Tìm các pattern: cụm từ 3+ từ, trong comments, docstrings, và các trường hợp đặc biệt
"""

import re
import os
from pathlib import Path
from collections import defaultdict

# Pattern để tìm các cụm từ 3+ từ viết hoa sai
VIETNAMESE_MULTI_WORD_PATTERN = re.compile(
    r'\b([A-ZÀÁẢÃẠĂẰẮẲẴẶÂẦẤẨẪẬĐÈÉẺẼẸÊỀẾỂỄỆÌÍỈĨỊÒÓỎÕỌÔỒỐỔỖỘƠỜỚỞỠỢÙÚỦŨỤƯỪỨỬỮỰỲÝỶỸỴ]'
    r'[a-zàáảãạăằắẳẵặâầấẩẫậđèéẻẽẹêềếểễệìíỉĩịòóỏõọôồốổỗộơờớởỡợùúủũụưừứửữựỳýỷỹỵ]+)\s+'
    r'([A-ZÀÁẢÃẠĂẰẮẲẴẶÂẦẤẨẪẬĐÈÉẺẼẸÊỀẾỂỄỆÌÍỈĨỊÒÓỎÕỌÔỒỐỔỖỘƠỜỚỞỠỢÙÚỦŨỤƯỪỨỬỮỰỲÝỶỸỴ]'
    r'[a-zàáảãạăằắẳẵặâầấẩẫậđèéẻẽẹêềếểễệìíỉĩịòóỏõọôồốổỗộơờớởỡợùúủũụưừứửữựỳýỷỹỵ]+)\s+'
    r'([A-ZÀÁẢÃẠĂẰẮẲẴẶÂẦẤẨẪẬĐÈÉẺẼẸÊỀẾỂỄỆÌÍỈĨỊÒÓỎÕỌÔỒỐỔỖỘƠỜỚỞỠỢÙÚỦŨỤƯỪỨỬỮỰỲÝỶỸỴ]'
    r'[a-zàáảãạăằắẳẵặâầấẩẫậđèéẻẽẹêềếểễệìíỉĩịòóỏõọôồốổỗộơờớởỡợùúủũụưừứửữựỳýỷỹỵ]+)'
)

# Pattern để tìm các cụm từ 2 từ trong các context đặc biệt
VIETNAMESE_TWO_WORD_PATTERN = re.compile(
    r'\b([A-ZÀÁẢÃẠĂẰẮẲẴẶÂẦẤẨẪẬĐÈÉẺẼẸÊỀẾỂỄỆÌÍỈĨỊÒÓỎÕỌÔỒỐỔỖỘƠỜỚỞỠỢÙÚỦŨỤƯỪỨỬỮỰỲÝỶỸỴ]'
    r'[a-zàáảãạăằắẳẵặâầấẩẫậđèéẻẽẹêềếểễệìíỉĩịòóỏõọôồốổỗộơờớởỡợùúủũụưừứửữựỳýỷỹỵ]+)\s+'
    r'([A-ZÀÁẢÃẠĂẰẮẲẴẶÂẦẤẨẪẬĐÈÉẺẼẸÊỀẾỂỄỆÌÍỈĨỊÒÓỎÕỌÔỒỐỔỖỘƠỜỚỞỠỢÙÚỦŨỤƯỪỨỬỮỰỲÝỶỸỴ]'
    r'[a-zàáảãạăằắẳẵặâầấẩẫậđèéẻẽẹêềếểễệìíỉĩịòóỏõọôồốổỗộơờớởỡợùúủũụưừứửữựỳýỷỹỵ]+)'
)

# Các cụm từ 3+ từ phổ biến cần viết hoa đúng
COMMON_3PLUS_WORD_PHRASES = {
    'điều trị bổ sung', 'điều trị nguyên nhân', 'điều trị chính',
    'phòng ngừa ban đầu', 'phòng ngừa tái phát', 'tái phát lần',
    'điều chỉnh theo nhịp tim', 'nhập thông số', 'giá trị tham chiếu',
    'thuốc gây kéo dài', 'kiến thức bổ sung', 'so sánh các công thức',
    'cách đo chính xác', 'nguyên nhân kéo dài', 'quản lý kéo dài qt do thuốc',
    'thông tin bệnh nhân', 'khuyến cáo điều trị', 'tình huống lâm sàng',
    'truy cập nhanh', 'thông số bệnh nhân', 'tra cứu dữ liệu kháng sinh',
    'kiểm tra tương thích', 'thuốc khác đang truyền', 'đánh giá ban đầu',
    'đánh giá mức độ nặng', 'đánh giá đáp ứng', 'tiêu chuẩn xét nghiệm',
    'nguyên nhân thường gặp', 'bảng tỷ lệ tử vong theo điểm',
    'mức độ nguy cơ', 'triệu chứng chính', 'chọn mức độ chức năng',
    'những sai lầm thường gặp', 'hướng dẫn đánh giá',
    'bảng phân loại nguy cơ', 'các trường hợp đặc biệt',
    'tự chăm sóc cá nhân', 'kiểm soát đại tiện', 'kiểm soát tiểu tiện',
    'làm theo lệnh', 'mất điều hòa chi', 'vận động tay', 'vận động chân',
    'mức độ ý thức', 'câu hỏi định hướng', 'ý nghĩa lâm sàng',
    'xuất huyết nội sọ', 'xuất huyết não thất', 'vị trí dưới lề',
    'thể tích máu tụ', 'phụ nữ có thai', 'suy giảm miễn dịch',
    'điều trị sau giai đoạn cấp', 'chuẩn bị thuốc', 'chuẩn bị nội soi',
    'cai rượu cấp', 'giao thức cấp cứu điện giải', 'máy tính giao thức',
    'giải thích chuyên sâu các thuật ngữ', 'suy thận cấp',
    'suy thận cấp tiền thận', 'phân tích chi tiết', 'phân tích từng',
    'quyết định phẫu thuật', 'quyết định điều trị', 'quyết định lâm sàng',
    'tiêu chí áp dụng', 'tiêu chí chẩn đoán', 'tiêu chí dương tính',
    'tiêu chí nhập icu', 'tiêu chí lâm sàng', 'tiêu chuẩn chẩn đoán',
    'tiêu chuẩn xuất viện', 'thành phần dung dịch', 'thông tin bổ sung',
    'thông tin lâm sàng', 'thông tin thêm', 'thông tin về',
    'khuyến nghị xử trí', 'khuyến nghị điều chỉnh', 'chi tiết điểm số',
    'chi tiết tính điểm', 'chi tiết tính toán', 'chi tiết từng biến số',
    'chi tiết từng thành phần', 'chi tiết từng tiêu chí', 'chi tiết đánh giá',
    'chăm sóc điều dưỡng', 'hướng dẫn sử dụng', 'khi nào đánh giá',
    'cách đánh giá', 'đánh giá đau', 'diễn giải kết quả',
    'diễn giải sofa-2', 'diễn giải mods', 'lưu ý quan trọng',
    'lưu ý y khoa', 'lưu ý đặc biệt', 'lưu ý điều trị',
    'thang đánh giá', 'tính toán gần đây', 'mẹo sử dụng',
    'tài liệu tham khảo', 'thông tin bệnh nhân', 'thông tin lâm sàng',
    'thông tin thêm', 'thông tin về', 'khuyến nghị xử trí',
    'khuyến nghị điều chỉnh', 'phân tích chi tiết', 'phân tích từng',
    'quyết định phẫu thuật', 'quyết định điều trị', 'quyết định lâm sàng'
}

# Các từ ngoại lệ
EXCEPTIONS = {
    'ICU', 'ECG', 'CT', 'MRI', 'CPR', 'ABC', 'PE', 'DVT', 'ARDS', 'MODS',
    'SOFA', 'APACHE', 'GCS', 'NIHSS', 'MAP', 'SBP', 'DBP', 'HR', 'RR',
    'BMI', 'BSA', 'GFR', 'CrCl', 'INR', 'PT', 'PTT', 'aPTT', 'DIC',
    'HHS', 'DKA', 'TLS', 'RA', 'IBD', 'CDIFF', 'CURB', 'PSI', 'MASCC',
    'Wells', 'Grace', 'TIMI', 'CRUSADE', 'CHA2DS2', 'HAS', 'BLED',
    'Hunt', 'Hess', 'Fisher', 'Bishop', 'Parkland', 'Epworth', 'GAD',
    'PHQ', 'MOCA', 'Braden', 'Glasgow', 'Blatchford', 'AIMS', 'BISAP',
    'MELD', 'Child', 'Pugh', 'Ranson', 'Balthazar', 'APACHE', 'SAPS',
    'LODS', 'MODS', 'NEWS', 'MEWS', 'QSOFA', 'SIRS', 'PESI', 'Wells',
    'Centor', 'Four', 'T', 'RIFLE', 'KDIGO', 'AKI', 'TBI', 'ICH',
    'AIS', 'AF', 'VT', 'SVT', 'PE', 'DVT', 'ACS', 'MI', 'STEMI',
    'NSTEMI', 'UA', 'CHF', 'COPD', 'ASTHMA', 'GERD', 'IBD', 'UC',
    'CD', 'PUD', 'GI', 'GU', 'tPA', 'MT', 'FMT', 'IV', 'PO', 'IM',
    'SC', 'SQ', 'ID', 'IO', 'PR', 'SL', 'NG', 'OG', 'ET', 'TT', 'GT',
    'JT', 'PICC', 'CVC', 'A-line', 'C-line', 'Swan', 'Ganz', 'PA',
    'CVP', 'PCWP', 'CO', 'CI', 'SV', 'SVI', 'SVV', 'PPV', 'PVI',
    'SVRI', 'PVRI', 'LVSWI', 'RVSWI', 'DO2', 'VO2', 'O2ER', 'ScvO2',
    'SvO2', 'Lactate', 'pH', 'pCO2', 'pO2', 'HCO3', 'BE', 'SaO2',
    'SpO2', 'FiO2', 'PEEP', 'CPAP', 'BiPAP', 'PSV', 'PCV', 'VCV',
    'PRVC', 'APRV', 'SIMV', 'CMV', 'AC', 'MMV', 'PAV', 'NAVA', 'ASV',
    'BiVent', 'DuoPAP', 'HFOV', 'ECMO', 'VAD', 'IABP', 'CRRT', 'HD',
    'PD', 'SLED', 'CVVH', 'CVVHD', 'CVVHDF', 'TPN', 'EN', 'PN', 'NG',
    'PEG', 'J', 'G', 'RBC', 'PRBC', 'FFP', 'PLT', 'PLTs', 'Cryo',
    'Albumin', 'NS', 'LR', 'D5W', 'D10W', 'D50W', 'NS', '1/2NS',
    '3/4NS', 'Plasma', 'Lyte', 'KCl', 'NaCl', 'CaCl', 'MgSO4',
    'NaHCO3', 'KPhos', 'NaPhos', 'Mg', 'Ca', 'K', 'Na', 'Cl',
    'HCO3', 'CO2', 'BUN', 'Cr', 'Glucose', 'Lactate', 'Albumin',
    'Total', 'Protein', 'Bilirubin', 'Direct', 'Indirect', 'ALT',
    'AST', 'ALP', 'GGT', 'LDH', 'CK', 'CK-MB', 'Troponin', 'I',
    'T', 'BNP', 'NT-proBNP', 'ProBNP', 'CRP', 'ESR', 'Procalcitonin',
    'WBC', 'RBC', 'Hgb', 'Hct', 'MCV', 'MCH', 'MCHC', 'RDW', 'PLT',
    'MPV', 'Neut', 'Lymph', 'Mono', 'Eos', 'Baso', 'Bands', 'Blasts'
}

DIRECTORIES = [
    "protocols", "pages", "scores", "labs", "critical_care",
    "antibiotics", "drugs", "components", "ventilator", "diagnosis"
]

IGNORE_PATTERNS = [
    "__pycache__", ".git", "node_modules", "venv", "env", ".pytest_cache",
    "check_", "fix_", "test_", "find_", "vietnamese_", "quick_fix_",
    "deep_scan_", "ultra_deep_"
]


def should_process_file(file_path: Path) -> bool:
    file_str = str(file_path)
    for pattern in IGNORE_PATTERNS:
        if pattern in file_str:
            return False
    return file_path.suffix == ".py"


def is_exception(word):
    return word.upper() in EXCEPTIONS or word in EXCEPTIONS


def find_errors_in_line(line, line_num):
    """Tìm các lỗi viết hoa trong một dòng"""
    errors = []
    
    # Tìm cụm từ 3+ từ
    matches_3plus = VIETNAMESE_MULTI_WORD_PATTERN.finditer(line)
    for match in matches_3plus:
        word1 = match.group(1)
        word2 = match.group(2)
        word3 = match.group(3)
        full_match = match.group(0)
        
        if is_exception(word1) or is_exception(word2) or is_exception(word3):
            continue
        
        phrase = f"{word1.lower()} {word2.lower()} {word3.lower()}"
        if phrase in COMMON_3PLUS_WORD_PHRASES:
            corrected = f"{word1} {word2.lower()} {word3.lower()}"
            errors.append({
                'line': line_num,
                'text': full_match,
                'corrected': corrected,
                'context': line.strip()[:150]
            })
    
    # Tìm cụm từ 2 từ trong các context đặc biệt (comments, docstrings)
    matches_2 = VIETNAMESE_TWO_WORD_PATTERN.finditer(line)
    for match in matches_2:
        word1 = match.group(1)
        word2 = match.group(2)
        full_match = match.group(0)
        
        if is_exception(word1) or is_exception(word2):
            continue
        
        # Chỉ kiểm tra trong comments hoặc docstrings
        if '#' in line or '"""' in line or "'''" in line:
            phrase = f"{word1.lower()} {word2.lower()}"
            # Kiểm tra xem có phải là cụm từ phổ biến không
            common_phrases_2 = [
                'điều trị', 'chẩn đoán', 'theo dõi', 'phân loại',
                'phân tầng', 'đánh giá', 'xử trí', 'quản lý',
                'chỉ định', 'triệu chứng', 'dấu hiệu', 'tiêu chuẩn',
                'tiêu chí', 'nguyên nhân', 'mục tiêu', 'hỗ trợ',
                'tài liệu', 'tham khảo', 'đặc biệt', 'thường gặp',
                'nguy cơ', 'mức độ', 'thông tin', 'khuyến cáo',
                'khuyến nghị', 'phân tích', 'quyết định', 'thành phần',
                'tham chiếu', 'giá trị', 'nhịp tim', 'thông số',
                'điều chỉnh', 'so sánh', 'cảnh báo', 'ưu tiên',
                'kiểm tra', 'kiểm soát', 'dịch truyền', 'mở mắt',
                'lời nói', 'vận động', 'giải thích', 'ý nghĩa',
                'hạng mục', 'câu hỏi', 'vận nhãn', 'thị trường',
                'liệt mặt', 'cảm giác', 'ngôn ngữ', 'khó phát âm',
                'bỏ qua', 'không chú ý', 'tiên lượng', 'xuất huyết',
                'vị trí', 'thể tích', 'tỷ lệ', 'tử vong', 'mô tả',
                'đi lại', 'tự chăm sóc', 'độc lập', 'hướng dẫn',
                'phòng ngừa', 'tái phát', 'bổ sung', 'điện giải',
                'truyền dịch', 'bù dịch', 'giảm đau', 'an thần',
                'kích động', 'dân số', 'suy tim', 'suy thận',
                'suy gan', 'cấp cứu', 'hồi sức', 'kháng sinh'
            ]
            
            if phrase in common_phrases_2:
                corrected = f"{word1} {word2.lower()}"
                errors.append({
                    'line': line_num,
                    'text': full_match,
                    'corrected': corrected,
                    'context': line.strip()[:150]
                })
    
    return errors


def find_capitalization_errors(content, file_path):
    """Tìm các lỗi viết hoa trong nội dung"""
    errors = []
    lines = content.split('\n')
    
    for line_num, line in enumerate(lines, 1):
        line_errors = find_errors_in_line(line, line_num)
        errors.extend(line_errors)
    
    return errors


def main():
    import sys
    
    dry_run = True
    if len(sys.argv) > 1 and sys.argv[1] == "--apply":
        dry_run = False
        print("⚠️  CHẾ ĐỘ SỬA FILE - Các thay đổi sẽ được lưu!\n")
    else:
        print("🔍 CHẾ ĐỘ DRY RUN - Chỉ báo cáo, không sửa file\n")
        print("💡 Để áp dụng thay đổi, chạy: python ultra_deep_scan_vietnamese_caps.py --apply\n")
    
    print("=" * 70)
    print("🔍 QUÉT CỰC KỲ CHI TIẾT LỖI VIẾT HOA TIẾNG VIỆT")
    print("=" * 70)
    print()
    
    total_files = 0
    files_with_errors = []
    total_errors = 0
    
    for directory in DIRECTORIES:
        dir_path = Path(directory)
        if not dir_path.exists():
            continue
        
        print(f"📂 Quét thư mục: {directory}")
        
        for file_path in dir_path.rglob("*"):
            if file_path.is_file() and should_process_file(file_path):
                total_files += 1
                
                try:
                    with open(file_path, 'r', encoding='utf-8') as f:
                        content = f.read()
                    
                    errors = find_capitalization_errors(content, file_path)
                    
                    if errors:
                        files_with_errors.append((file_path, errors))
                        total_errors += len(errors)
                        
                        if not dry_run:
                            # Sửa lỗi trong file
                            for error in reversed(errors):
                                pattern = re.escape(error['text'])
                                content = re.sub(pattern, error['corrected'], content, count=1)
                            
                            with open(file_path, 'w', encoding='utf-8') as f:
                                f.write(content)
                            print(f"✅ {file_path}: {len(errors)} lỗi đã sửa")
                        else:
                            print(f"📝 {file_path}: {len(errors)} lỗi")
                            for error in errors[:3]:
                                print(f"   Dòng {error['line']}: '{error['text']}' → '{error['corrected']}'")
                            if len(errors) > 3:
                                print(f"   ... và {len(errors) - 3} lỗi khác")
                
                except Exception as e:
                    print(f"❌ Lỗi khi xử lý {file_path}: {e}")
    
    print()
    print("=" * 70)
    print("📊 TÓM TẮT")
    print("=" * 70)
    print(f"Tổng số file đã quét: {total_files}")
    print(f"Tổng số file có lỗi: {len(files_with_errors)}")
    print(f"Tổng số lỗi: {total_errors}")
    print()
    
    if files_with_errors:
        print("📝 Các file có lỗi:")
        for file_path, errors in files_with_errors[:20]:
            print(f"  - {file_path} ({len(errors)} lỗi)")
        if len(files_with_errors) > 20:
            print(f"  ... và {len(files_with_errors) - 20} file khác")
    
    print()
    if dry_run:
        print("💡 Chạy với --apply để áp dụng các thay đổi")
    else:
        print("✅ Hoàn thành!")


if __name__ == "__main__":
    main()

