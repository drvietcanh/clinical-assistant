"""
Script quét sâu để tìm các lỗi viết hoa tiếng Việt còn sót lại
Tìm các pattern: từ có chữ cái đầu viết hoa + từ tiếp theo cũng viết hoa (sai quy tắc)
"""

import re
import os
from pathlib import Path
from collections import defaultdict

# Pattern để tìm các từ tiếng Việt viết hoa sai
# Tìm: Chữ Hoa + chữ thường + khoảng trắng + Chữ Hoa (ví dụ: "Điều Trị", "Phân Loại")
VIETNAMESE_CAP_PATTERN = re.compile(
    r'\b([A-ZÀÁẢÃẠĂẰẮẲẴẶÂẦẤẨẪẬĐÈÉẺẼẸÊỀẾỂỄỆÌÍỈĨỊÒÓỎÕỌÔỒỐỔỖỘƠỜỚỞỠỢÙÚỦŨỤƯỪỨỬỮỰỲÝỶỸỴ]'
    r'[a-zàáảãạăằắẳẵặâầấẩẫậđèéẻẽẹêềếểễệìíỉĩịòóỏõọôồốổỗộơờớởỡợùúủũụưừứửữựỳýỷỹỵ]+)\s+'
    r'([A-ZÀÁẢÃẠĂẰẮẲẴẶÂẦẤẨẪẬĐÈÉẺẼẸÊỀẾỂỄỆÌÍỈĨỊÒÓỎÕỌÔỒỐỔỖỘƠỜỚỞỠỢÙÚỦŨỤƯỪỨỬỮỰỲÝỶỸỴ]'
    r'[a-zàáảãạăằắẳẵặâầấẩẫậđèéẻẽẹêềếểễệìíỉĩịòóỏõọôồốổỗộơờớởỡợùúủũụưừứửữựỳýỷỹỵ]+)'
)

# Các từ ngoại lệ (tên riêng, thuật ngữ đặc biệt được phép viết hoa)
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
    'CD', 'PUD', 'GI', 'GU', 'GU', 'GU', 'GU', 'GU', 'GU', 'GU',
    'tPA', 'MT', 'FMT', 'IV', 'PO', 'IM', 'SC', 'SQ', 'ID', 'IO',
    'PR', 'SL', 'NG', 'OG', 'ET', 'TT', 'GT', 'JT', 'PICC', 'CVC',
    'A-line', 'C-line', 'Swan', 'Ganz', 'PA', 'CVP', 'PCWP', 'CO',
    'CI', 'SV', 'SVI', 'SVV', 'PPV', 'PVI', 'SVRI', 'PVRI', 'LVSWI',
    'RVSWI', 'DO2', 'VO2', 'O2ER', 'ScvO2', 'SvO2', 'Lactate',
    'pH', 'pCO2', 'pO2', 'HCO3', 'BE', 'SaO2', 'SpO2', 'FiO2',
    'PEEP', 'CPAP', 'BiPAP', 'PSV', 'PCV', 'VCV', 'PRVC', 'APRV',
    'SIMV', 'CMV', 'AC', 'MMV', 'PAV', 'NAVA', 'ASV', 'BiVent',
    'DuoPAP', 'HFOV', 'ECMO', 'VAD', 'IABP', 'CRRT', 'HD', 'PD',
    'SLED', 'CVVH', 'CVVHD', 'CVVHDF', 'TPN', 'EN', 'PN', 'NG',
    'PEG', 'J', 'G', 'RBC', 'PRBC', 'FFP', 'PLT', 'PLTs', 'Cryo',
    'Albumin', 'NS', 'LR', 'D5W', 'D10W', 'D50W', 'NS', '1/2NS',
    '3/4NS', 'Plasma', 'Lyte', 'KCl', 'NaCl', 'CaCl', 'MgSO4',
    'NaHCO3', 'KPhos', 'NaPhos', 'Mg', 'Ca', 'K', 'Na', 'Cl',
    'HCO3', 'CO2', 'BUN', 'Cr', 'Glucose', 'Lactate', 'Albumin',
    'Total', 'Protein', 'Bilirubin', 'Direct', 'Indirect', 'ALT',
    'AST', 'ALP', 'GGT', 'LDH', 'CK', 'CK-MB', 'Troponin', 'I',
    'T', 'BNP', 'NT-proBNP', 'ProBNP', 'CRP', 'ESR', 'Procalcitonin',
    'WBC', 'RBC', 'Hgb', 'Hct', 'MCV', 'MCH', 'MCHC', 'RDW', 'PLT',
    'MPV', 'Neut', 'Lymph', 'Mono', 'Eos', 'Baso', 'Bands', 'Blasts',
    'PT', 'PTT', 'aPTT', 'INR', 'Fibrinogen', 'D-dimer', 'FDP',
    'ATIII', 'Protein', 'C', 'S', 'Lupus', 'Anticoagulant', 'Factor',
    'V', 'VIII', 'IX', 'XI', 'XII', 'XIII', 'vWF', 'Ristocetin',
    'Coombs', 'Direct', 'Indirect', 'DAT', 'IAT', 'Eluate', 'Antibody',
    'Screen', 'Panel', 'Crossmatch', 'Type', 'Screen', 'ABO', 'Rh',
    'D', 'C', 'c', 'E', 'e', 'K', 'k', 'Fya', 'Fyb', 'Jka', 'Jkb',
    'M', 'N', 'S', 's', 'Lea', 'Leb', 'P1', 'Lua', 'Lub', 'Vel',
    'Lan', 'Jr', 'a', 'Co', 'a', 'Yt', 'a', 'Yt', 'b', 'Xg', 'a',
    'Scianna', 'Dombrock', 'Colton', 'LW', 'Chido', 'Rodgers', 'Knops',
    'Cromer', 'JMH', 'Indian', 'Ok', 'a', 'Raph', 'GIL', 'ABCB6',
    'MAM', 'PEL', 'ABO', 'A1', 'A2', 'B', 'O', 'AB', 'Rh', 'D',
    'Weak', 'D', 'Partial', 'D', 'Del', 'C', 'c', 'E', 'e', 'Cw',
    'Cx', 'V', 'VS', 'hr', 'B', 'hr', 'S', 'hr', 's', 'U', 'K',
    'k', 'Kp', 'a', 'Kp', 'b', 'Js', 'a', 'Js', 'b', 'Ko', 'KEL',
    'Fy', 'a', 'Fy', 'b', 'Fy', 'x', 'Fy', 'Fy3', 'Fy4', 'Fy5',
    'Fy6', 'Jk', 'a', 'Jk', 'b', 'Jk3', 'Jk', 'a', 'b', '-', 'Di',
    'a', 'Di', 'b', 'Yt', 'a', 'Yt', 'b', 'Xg', 'a', 'Co', 'a',
    'Co', 'b', 'LW', 'a', 'LW', 'b', 'LW', 'ab', 'Ch', 'a', 'Ch',
    'Rg', 'a', 'Rg', 'Kn', 'a', 'Kn', 'b', 'Kn', 'c', 'McC', 'a',
    'McC', 'b', 'Sl', 'a', 'Sl', 'b', 'Yk', 'a', 'Cr', 'a', 'Cr',
    'b', 'Tc', 'a', 'Tc', 'b', 'Tc', 'c', 'JMH', 'Ok', 'a', 'Raph',
    'GIL', 'ABCB6', 'MAM', 'PEL', 'ABO', 'A1', 'A2', 'B', 'O', 'AB'
}

# Các cụm từ phổ biến cần viết hoa đúng (từ đầu viết hoa, các từ sau viết thường)
COMMON_PHRASES = {
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
    'đi đại tiện', 'đi tiểu tiện', 'lên xuống', 'cầu thang', 'tắm rửa',
    'mặc quần áo', 'ăn uống', 'liều tính được', 'chi tiết', 'kết quả',
    'diễn giải', 'lưu ý', 'thang đo', 'tính toán', 'mẹo sử dụng',
    'sử dụng', 'tình huống', 'truy cập', 'độ nhạy', 'kháng sinh',
    'phòng ngừa', 'tái phát', 'bổ sung', 'điện giải', 'truyền dịch',
    'bù dịch', 'giảm đau', 'an thần', 'kích động', 'dân số',
    'suy tim', 'suy thận', 'suy gan', 'suy giảm miễn dịch',
    'phụ nữ có thai', 'trẻ em', 'người cao tuổi', 'người lớn',
    'cấp cứu', 'hồi sức', 'bảng tỷ lệ tử vong theo điểm',
    'mức độ nguy cơ', 'triệu chứng chính', 'chọn mức độ chức năng',
    'những sai lầm thường gặp', 'hướng dẫn đánh giá',
    'bảng phân loại nguy cơ', 'các trường hợp đặc biệt',
    'tự chăm sóc cá nhân', 'kiểm soát đại tiện', 'kiểm soát tiểu tiện',
    'làm theo lệnh', 'mất điều hòa chi', 'vận động tay', 'vận động chân',
    'mức độ ý thức', 'câu hỏi định hướng', 'ý nghĩa lâm sàng',
    'xuất huyết nội sọ', 'xuất huyết não thất', 'vị trí dưới lề',
    'thể tích máu tụ', 'điều trị bổ sung', 'điều trị nguyên nhân',
    'điều trị chính', 'phòng ngừa ban đầu', 'phòng ngừa tái phát',
    'nhập thông số', 'giá trị tham chiếu', 'thuốc gây kéo dài',
    'kiến thức bổ sung', 'so sánh các công thức', 'cách đo chính xác',
    'nguyên nhân kéo dài', 'quản lý kéo dài', 'thông tin bệnh nhân',
    'thông số lâm sàng', 'chi tiết điểm', 'tái can thiệp',
    'khuyến cáo điều trị', 'tình huống lâm sàng', 'truy cập nhanh',
    'thông số bệnh nhân', 'tra cứu', 'kiểm tra tương thích',
    'thuốc khác đang truyền', 'đánh giá ban đầu', 'đánh giá mức độ nặng',
    'đánh giá đáp ứng', 'tiêu chuẩn xét nghiệm', 'nguyên nhân thường gặp'
}

DIRECTORIES = [
    "protocols", "pages", "scores", "labs", "critical_care",
    "antibiotics", "drugs", "components", "ventilator", "diagnosis"
]

IGNORE_PATTERNS = [
    "__pycache__", ".git", "node_modules", "venv", "env", ".pytest_cache",
    "check_", "fix_", "test_", "find_", "vietnamese_", "quick_fix_", "deep_scan_"
]


def should_process_file(file_path: Path) -> bool:
    file_str = str(file_path)
    for pattern in IGNORE_PATTERNS:
        if pattern in file_str:
            return False
    return file_path.suffix == ".py"


def is_exception(word):
    """Kiểm tra xem từ có phải là ngoại lệ không"""
    return word.upper() in EXCEPTIONS or word in EXCEPTIONS


def find_capitalization_errors(content, file_path):
    """Tìm các lỗi viết hoa trong nội dung"""
    errors = []
    lines = content.split('\n')
    
    for line_num, line in enumerate(lines, 1):
        # Chỉ kiểm tra trong strings và markdown
        if not ('st.markdown' in line or 'st.subheader' in line or 
                'st.header' in line or '"' in line or "'" in line):
            continue
        
        # Tìm các pattern viết hoa sai
        matches = VIETNAMESE_CAP_PATTERN.finditer(line)
        
        for match in matches:
            word1 = match.group(1)
            word2 = match.group(2)
            full_match = match.group(0)
            
            # Bỏ qua nếu là ngoại lệ
            if is_exception(word1) or is_exception(word2):
                continue
            
            # Bỏ qua nếu là đầu câu hoặc sau dấu chấm
            start_pos = match.start()
            before = line[max(0, start_pos-5):start_pos]
            if before.strip() in ['', '.', '!', '?', ':', ';', '-', '–', '—']:
                continue
            
            # Kiểm tra xem có phải là cụm từ phổ biến không
            phrase = f"{word1.lower()} {word2.lower()}"
            if phrase in COMMON_PHRASES:
                # Đây là lỗi - từ thứ 2 không nên viết hoa
                corrected = f"{word1} {word2.lower()}"
                errors.append({
                    'line': line_num,
                    'text': full_match,
                    'corrected': corrected,
                    'context': line.strip()[:150]
                })
    
    return errors


def main():
    import sys
    
    dry_run = True
    if len(sys.argv) > 1 and sys.argv[1] == "--apply":
        dry_run = False
        print("⚠️  CHẾ ĐỘ SỬA FILE - Các thay đổi sẽ được lưu!\n")
    else:
        print("🔍 CHẾ ĐỘ DRY RUN - Chỉ báo cáo, không sửa file\n")
        print("💡 Để áp dụng thay đổi, chạy: python deep_scan_vietnamese_caps.py --apply\n")
    
    print("=" * 70)
    print("🔍 QUÉT SÂU LỖI VIẾT HOA TIẾNG VIỆT")
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
                            for error in reversed(errors):  # Sửa từ cuối lên
                                # Tìm và thay thế
                                pattern = re.escape(error['text'])
                                content = re.sub(pattern, error['corrected'], content, count=1)
                            
                            # Ghi file
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

