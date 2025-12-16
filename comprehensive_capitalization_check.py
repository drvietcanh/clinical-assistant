"""
Script kiểm tra toàn diện lỗi viết hoa trong codebase
Bao gồm:
1. Lỗi viết hoa tiếng Việt (ví dụ: "Phòng Ngừa" → "Phòng ngừa")
2. Inconsistent capitalization trong string literals
3. Variable naming inconsistencies
4. Comments với capitalization sai
"""

import re
import os
from pathlib import Path
from collections import defaultdict

# Pattern để tìm các từ tiếng Việt viết hoa sai
# Tìm: Chữ Hoa + chữ thường + khoảng trắng + Chữ Hoa (trong bất kỳ context nào)
VIETNAMESE_CAP_PATTERN = re.compile(
    r'\b([A-ZÀÁẢÃẠĂẰẮẲẴẶÂẦẤẨẪẬĐÈÉẺẼẸÊỀẾỂỄỆÌÍỈĨỊÒÓỎÕỌÔỒỐỔỖỘƠỜỚỞỠỢÙÚỦŨỤƯỪỨỬỮỰỲÝỶỸỴ]'
    r'[a-zàáảãạăằắẳẵặâầấẩẫậđèéẻẽẹêềếểễệìíỉĩịòóỏõọôồốổỗộơờớởỡợùúủũụưừứửữựỳýỷỹỵ]+)\s+'
    r'([A-ZÀÁẢÃẠĂẰẮẲẴẶÂẦẤẨẪẬĐÈÉẺẼẸÊỀẾỂỄỆÌÍỈĨỊÒÓỎÕỌÔỒỐỔỖỘƠỜỚỞỠỢÙÚỦŨỤƯỪỨỬỮỰỲÝỶỸỴ]'
    r'[a-zàáảãạăằắẳẵặâầấẩẫậđèéẻẽẹêềếểễệìíỉĩịòóỏõọôồốổỗộơờớởỡợùúủũụưừứửữựỳýỷỹỵ]+)'
)

# Các cụm từ tiếng Việt phổ biến - từ thứ 2 trở đi KHÔNG nên viết hoa (trừ đầu câu)
COMMON_VIETNAMESE_PHRASES = {
    # 2 từ
    'điều trị', 'chẩn đoán', 'theo dõi', 'phân loại', 'phân tầng',
    'đánh giá', 'xử trí', 'quản lý', 'chỉ định', 'triệu chứng',
    'dấu hiệu', 'tiêu chuẩn', 'tiêu chí', 'nguyên nhân', 'mục tiêu',
    'hỗ trợ', 'tài liệu', 'tham khảo', 'đặc biệt', 'thường gặp',
    'nguy cơ', 'mức độ', 'thông tin', 'khuyến cáo', 'khuyến nghị',
    'phân tích', 'quyết định', 'thành phần', 'tham chiếu', 'giá trị',
    'nhịp tim', 'thông số', 'điều chỉnh', 'so sánh', 'cảnh báo',
    'ưu tiên', 'kiểm tra', 'kiểm soát', 'dịch truyền', 'mở mắt',
    'lời nói', 'vận động', 'giải thích', 'ý nghĩa', 'hạng mục',
    'câu hỏi', 'vận nhãn', 'thị trường', 'liệt mặt', 'cảm giác',
    'ngôn ngữ', 'khó phát âm', 'bỏ qua', 'không chú ý', 'tiên lượng',
    'xuất huyết', 'vị trí', 'thể tích', 'tỷ lệ', 'tử vong',
    'mô tả', 'đi lại', 'tự chăm sóc', 'độc lập', 'hướng dẫn',
    'phòng ngừa', 'tái phát', 'bổ sung', 'điện giải', 'truyền dịch',
    'bù dịch', 'giảm đau', 'an thần', 'kích động', 'dân số',
    'suy tim', 'suy thận', 'suy gan', 'cấp cứu', 'hồi sức',
    'kháng sinh', 'người lớn', 'phụ nữ có thai', 'trẻ em',
    'người cao tuổi', 'suy giảm miễn dịch',
    
    # 3+ từ
    'điều trị bổ sung', 'điều trị nguyên nhân', 'điều trị chính',
    'phòng ngừa ban đầu', 'phòng ngừa tái phát', 'tái phát lần',
    'điều chỉnh theo nhịp tim', 'nhập thông số', 'giá trị tham chiếu',
    'thuốc gây kéo dài', 'kiến thức bổ sung', 'so sánh các công thức',
    'cách đo chính xác', 'nguyên nhân kéo dài', 'quản lý kéo dài',
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
    'thể tích máu tụ', 'điều trị sau giai đoạn cấp', 'chuẩn bị thuốc',
    'chuẩn bị nội soi', 'cai rượu cấp', 'giao thức cấp cứu điện giải',
    'máy tính giao thức', 'giải thích chuyên sâu các thuật ngữ',
    'suy thận cấp', 'suy thận cấp tiền thận', 'phân tích chi tiết',
    'phân tích từng', 'quyết định phẫu thuật', 'quyết định điều trị',
    'quyết định lâm sàng', 'tiêu chí áp dụng', 'tiêu chí chẩn đoán',
    'tiêu chí dương tính', 'tiêu chí nhập icu', 'tiêu chí lâm sàng',
    'tiêu chuẩn chẩn đoán', 'tiêu chuẩn xuất viện', 'thành phần dung dịch',
    'thông tin bổ sung', 'thông tin lâm sàng', 'thông tin thêm',
    'thông tin về', 'khuyến nghị xử trí', 'khuyến nghị điều chỉnh',
    'chi tiết điểm số', 'chi tiết tính điểm', 'chi tiết tính toán',
    'chi tiết từng biến số', 'chi tiết từng thành phần',
    'chi tiết từng tiêu chí', 'chi tiết đánh giá', 'chăm sóc điều dưỡng',
    'hướng dẫn sử dụng', 'khi nào đánh giá', 'cách đánh giá',
    'đánh giá đau', 'diễn giải kết quả', 'diễn giải sofa-2',
    'diễn giải mods', 'lưu ý quan trọng', 'lưu ý y khoa',
    'lưu ý đặc biệt', 'lưu ý điều trị', 'thang đánh giá',
    'tính toán gần đây', 'mẹo sử dụng', 'tài liệu tham khảo',
    'đi đại tiện', 'đi tiểu tiện', 'lên xuống', 'cầu thang',
    'tắm rửa', 'mặc quần áo', 'ăn uống', 'liều tính được',
}

# Các từ viết tắt và ngoại lệ (luôn viết hoa)
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

# Pattern để tìm các biến có tên không nhất quán
VARIABLE_PATTERN = re.compile(r'\b([a-z_][a-z0-9_]*[A-Z][a-zA-Z0-9_]*|[A-Z][a-z0-9_]*[A-Z][a-z0-9_]*)\b')

# Pattern để tìm string literals với capitalization có vấn đề
STRING_PATTERN = re.compile(r'["\']([^"\']+)["\']')

DIRECTORIES = [
    "protocols", "pages", "scores", "labs", "critical_care",
    "antibiotics", "drugs", "components", "ventilator", "diagnosis",
    "utils", "config"
]

IGNORE_PATTERNS = [
    "__pycache__", ".git", "node_modules", "venv", "env", ".pytest_cache",
    "check_", "fix_", "test_", "find_", "vietnamese_", "quick_fix_",
    "deep_scan_", "ultra_deep_", "comprehensive_scan_", "comprehensive_capitalization"
]


def should_process_file(file_path: Path) -> bool:
    """Kiểm tra xem file có nên được xử lý không"""
    file_str = str(file_path)
    for pattern in IGNORE_PATTERNS:
        if pattern in file_str:
            return False
    return file_path.suffix == ".py"


def is_exception(word):
    """Kiểm tra xem từ có phải là ngoại lệ không"""
    return word.upper() in EXCEPTIONS or word in EXCEPTIONS


def is_start_of_sentence(line, pos):
    """Kiểm tra xem có phải là đầu câu không"""
    before = line[max(0, pos-20):pos].strip()
    if not before:
        return True
    # Kiểm tra các ký tự kết thúc câu
    return before[-1] in ['.', '!', '?', ':', ';', '\n', '\r', '(', '[', '{']


def is_in_string_context(line, pos):
    """Kiểm tra xem có phải trong string context không"""
    before = line[max(0, pos-100):pos]
    after = line[pos:min(len(line), pos+100)]
    
    # Đếm số lượng dấu ngoặc kép và đơn
    single_quotes_before = before.count("'") - before.count("\\'")
    double_quotes_before = before.count('"') - before.count('\\"')
    single_quotes_after = after.count("'") - after.count("\\'")
    double_quotes_after = after.count('"') - after.count('\\"')
    
    # Nếu số lượng dấu ngoặc kép/đơn là lẻ, thì đang trong string
    in_single = single_quotes_before % 2 == 1
    in_double = double_quotes_before % 2 == 1
    
    # Kiểm tra các context đặc biệt
    in_markdown = 'st.markdown' in before or 'st.subheader' in before or 'st.header' in before
    in_fstring = 'f"' in before or "f'" in before or 'f"""' in before or "f'''" in before
    
    return in_single or in_double or in_markdown or in_fstring


def find_vietnamese_capitalization_errors(content, file_path):
    """Tìm các lỗi viết hoa tiếng Việt"""
    errors = []
    lines = content.split('\n')
    
    for line_num, line in enumerate(lines, 1):
        # Tìm tất cả các pattern viết hoa sai
        matches = VIETNAMESE_CAP_PATTERN.finditer(line)
        
        for match in matches:
            word1 = match.group(1)
            word2 = match.group(2)
            full_match = match.group(0)
            start_pos = match.start()
            
            # Bỏ qua nếu là ngoại lệ
            if is_exception(word1) or is_exception(word2):
                continue
            
            # Bỏ qua nếu là đầu câu (được phép viết hoa)
            if is_start_of_sentence(line, start_pos):
                continue
            
            # Chỉ kiểm tra trong string context
            if not is_in_string_context(line, start_pos):
                continue
            
            # Kiểm tra xem có phải là cụm từ phổ biến không
            phrase = f"{word1.lower()} {word2.lower()}"
            
            if phrase in COMMON_VIETNAMESE_PHRASES:
                # Đây là lỗi - từ thứ 2 không nên viết hoa (trừ đầu câu)
                corrected = f"{word1} {word2.lower()}"
                
                errors.append({
                    'type': 'vietnamese_capitalization',
                    'line': line_num,
                    'text': full_match,
                    'corrected': corrected,
                    'context': line.strip()[:150],
                    'phrase': phrase
                })
    
    return errors


def find_inconsistent_variable_names(content, file_path):
    """Tìm các biến có tên không nhất quán (mixedCase trong snake_case codebase)"""
    errors = []
    lines = content.split('\n')
    
    for line_num, line in enumerate(lines, 1):
        # Bỏ qua comment lines
        if line.strip().startswith('#'):
            continue
        
        # Tìm các biến có mixedCase
        matches = VARIABLE_PATTERN.finditer(line)
        
        for match in matches:
            var_name = match.group(1)
            start_pos = match.start()
            
            # Bỏ qua nếu là class name (PascalCase)
            if var_name[0].isupper() and var_name[1:].islower():
                continue
            
            # Bỏ qua nếu là constant (ALL_CAPS)
            if var_name.isupper() and '_' in var_name:
                continue
            
            # Bỏ qua nếu là trong string
            if is_in_string_context(line, start_pos):
                continue
            
            # Tìm mixedCase (camelCase trong snake_case codebase)
            if '_' not in var_name and var_name[0].islower() and any(c.isupper() for c in var_name[1:]):
                # Đề xuất chuyển sang snake_case
                corrected = ''.join(['_' + c.lower() if c.isupper() else c for c in var_name]).lstrip('_')
                
                errors.append({
                    'type': 'variable_naming',
                    'line': line_num,
                    'text': var_name,
                    'corrected': corrected,
                    'context': line.strip()[:150]
                })
    
    return errors


def find_string_capitalization_errors(content, file_path):
    """Tìm các lỗi capitalization trong string literals"""
    errors = []
    lines = content.split('\n')
    
    for line_num, line in enumerate(lines, 1):
        # Tìm các string literals
        string_matches = re.finditer(r'["\']([^"\']+)["\']', line)
        
        for match in string_matches:
            string_content = match.group(1)
            start_pos = match.start()
            
            # Bỏ qua nếu là f-string với code
            if 'f"' in line[max(0, start_pos-10):start_pos] or "f'" in line[max(0, start_pos-10):start_pos]:
                continue
            
            # Kiểm tra các pattern viết hoa sai trong string
            vietnamese_matches = VIETNAMESE_CAP_PATTERN.finditer(string_content)
            
            for vn_match in vietnamese_matches:
                word1 = vn_match.group(1)
                word2 = vn_match.group(2)
                full_match = vn_match.group(0)
                
                # Bỏ qua nếu là ngoại lệ
                if is_exception(word1) or is_exception(word2):
                    continue
                
                # Kiểm tra xem có phải là cụm từ phổ biến không
                phrase = f"{word1.lower()} {word2.lower()}"
                
                if phrase in COMMON_VIETNAMESE_PHRASES:
                    # Kiểm tra xem có phải đầu câu không
                    vn_start = vn_match.start()
                    before_in_string = string_content[max(0, vn_start-20):vn_start].strip()
                    
                    if not before_in_string or before_in_string[-1] in ['.', '!', '?', ':', ';', '\n']:
                        continue  # Đầu câu, được phép viết hoa
                    
                    corrected = f"{word1} {word2.lower()}"
                    
                    errors.append({
                        'type': 'string_capitalization',
                        'line': line_num,
                        'text': full_match,
                        'corrected': corrected,
                        'context': line.strip()[:150],
                        'phrase': phrase
                    })
    
    return errors


def scan_file(file_path):
    """Quét một file và tìm tất cả các lỗi"""
    all_errors = {
        'vietnamese_capitalization': [],
        'variable_naming': [],
        'string_capitalization': []
    }
    
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Tìm các loại lỗi khác nhau
        all_errors['vietnamese_capitalization'] = find_vietnamese_capitalization_errors(content, file_path)
        all_errors['variable_naming'] = find_inconsistent_variable_names(content, file_path)
        all_errors['string_capitalization'] = find_string_capitalization_errors(content, file_path)
        
    except Exception as e:
        print(f"❌ Lỗi khi đọc {file_path}: {e}")
    
    return all_errors


def main():
    import sys
    
    dry_run = True
    if len(sys.argv) > 1 and sys.argv[1] == "--apply":
        dry_run = False
        print("⚠️  CHẾ ĐỘ SỬA FILE - Các thay đổi sẽ được lưu!\n")
    else:
        print("🔍 CHẾ ĐỘ DRY RUN - Chỉ báo cáo, không sửa file\n")
        print("💡 Để áp dụng thay đổi, chạy: python comprehensive_capitalization_check.py --apply\n")
    
    print("=" * 80)
    print("🔍 KIỂM TRA TOÀN DIỆN LỖI VIẾT HOA")
    print("=" * 80)
    print()
    
    total_files = 0
    files_with_errors = defaultdict(list)
    total_errors = defaultdict(int)
    
    for directory in DIRECTORIES:
        dir_path = Path(directory)
        if not dir_path.exists():
            continue
        
        print(f"📂 Quét thư mục: {directory}")
        
        for file_path in dir_path.rglob("*"):
            if file_path.is_file() and should_process_file(file_path):
                total_files += 1
                
                errors = scan_file(file_path)
                
                has_errors = False
                for error_type, error_list in errors.items():
                    if error_list:
                        has_errors = True
                        total_errors[error_type] += len(error_list)
                
                if has_errors:
                    files_with_errors[file_path] = errors
                    
                    if not dry_run:
                        # Sửa lỗi trong file
                        try:
                            with open(file_path, 'r', encoding='utf-8') as f:
                                content = f.read()
                            
                            # Sửa các lỗi theo thứ tự ngược lại để không ảnh hưởng đến vị trí
                            for error_type in ['vietnamese_capitalization', 'string_capitalization']:
                                for error in reversed(errors[error_type]):
                                    pattern = re.escape(error['text'])
                                    content = re.sub(pattern, error['corrected'], content, count=1)
                            
                            with open(file_path, 'w', encoding='utf-8') as f:
                                f.write(content)
                            
                            total_fixed = sum(len(errors[et]) for et in ['vietnamese_capitalization', 'string_capitalization'])
                            print(f"✅ {file_path}: {total_fixed} lỗi đã sửa")
                        except Exception as e:
                            print(f"❌ Lỗi khi sửa {file_path}: {e}")
                    else:
                        total_errors_in_file = sum(len(error_list) for error_list in errors.values())
                        print(f"📝 {file_path}: {total_errors_in_file} lỗi")
                        for error_type, error_list in errors.items():
                            if error_list:
                                print(f"   - {error_type}: {len(error_list)} lỗi")
                                for error in error_list[:2]:
                                    print(f"     Dòng {error['line']}: '{error['text']}' → '{error['corrected']}'")
                                if len(error_list) > 2:
                                    print(f"     ... và {len(error_list) - 2} lỗi khác")
    
    print()
    print("=" * 80)
    print("📊 TÓM TẮT")
    print("=" * 80)
    print(f"Tổng số file đã quét: {total_files}")
    print(f"Tổng số file có lỗi: {len(files_with_errors)}")
    print()
    
    if total_errors:
        print("📝 Chi tiết lỗi theo loại:")
        for error_type, count in total_errors.items():
            print(f"   - {error_type}: {count} lỗi")
    
    print()
    
    if files_with_errors:
        print("📄 Các file có lỗi (top 20):")
        for idx, (file_path, errors) in enumerate(list(files_with_errors.items())[:20]):
            total = sum(len(error_list) for error_list in errors.values())
            print(f"  {idx+1}. {file_path} ({total} lỗi)")
        if len(files_with_errors) > 20:
            print(f"  ... và {len(files_with_errors) - 20} file khác")
    
    print()
    if dry_run:
        print("💡 Chạy với --apply để áp dụng các thay đổi")
    else:
        print("✅ Hoàn thành!")


if __name__ == "__main__":
    main()

