"""
Script tối ưu để quét nhanh lỗi viết hoa tiếng Việt trong codebase y khoa
Sử dụng từ điển y khoa đầy đủ và regex tối ưu
"""

import re
import os
from pathlib import Path
from collections import defaultdict
from typing import List, Dict, Tuple
import time

# ========== TỪ ĐIỂN Y KHOA TIẾNG VIỆT ==========
# Các cụm từ y khoa phổ biến - từ thứ 2 trở đi KHÔNG nên viết hoa (trừ đầu câu)

MEDICAL_TERMS_2_WORDS = {
    # Dịch tễ / sàng lọc / tư vấn
    'phát hiện', 'phát hiện sớm', 'sàng lọc', 'tái khám', 'tư vấn',
    'giáo dục', 'giáo dục sức khỏe', 'theo dõi', 'theo dõi định kỳ',

    # Cấp cứu – hồi sức
    'ngừng tim', 'ngừng thở', 'ép tim', 'hồi sinh', 'phục hồi', 'tuần hoàn',
    'cấp cứu', 'hồi sức', 'ngừng tuần hoàn', 'đặt đường', 'đặt đường thở',
    'đặt nội khí quản', 'đặt ống nội khí quản', 'oxy liệu pháp',

    # Thuốc & kháng đông/kháng kết tập
    'kháng đông', 'kháng kết', 'kháng kết tập', 'kháng kết tập tiểu cầu',
    'tiêu sợi', 'tiêu sợi huyết', 'giải độc', 'đối kháng',
    'liều nạp', 'liều duy trì', 'liều tải',

    # Dịch truyền / điện giải
    'bù dịch', 'bù dịch nhanh', 'truyền nhanh', 'nhỏ giọt',
    'điều chỉnh', 'điều chỉnh điện giải', 'bổ sung', 'bổ sung kali',
    'bổ sung magnesi', 'điện giải',

    # Nội soi & thủ thuật
    'nội soi', 'nội soi can thiệp', 'nội soi chẩn đoán',
    'kẹp clip', 'tiêm cầm máu', 'thắt tĩnh mạch', 'can thiệp mạch',

    # Chẩn đoán hình ảnh
    'siêu âm', 'siêu âm tim', 'siêu âm bụng', 'ct ngực', 'ct bụng',
    'mri não', 'x quang', 'x quang ngực', 'dsa',

    # Hô hấp / máy thở
    'áp lực', 'áp lực đỉnh', 'áp lực bình nguyên',
    'áp lực dương', 'áp lực dương cuối thì thở ra',
    'thể tích', 'thể tích khí lưu thông', 'thể tích phút', 'thông khí phút',
    'độ giãn nở', 'độ giãn nở tĩnh', 'độ giãn nở động',

    # Tim mạch huyết động
    'cung lượng', 'cung lượng tim', 'chỉ số tim',
    'áp lực tĩnh mạch', 'áp lực tĩnh mạch trung tâm',
    'áp lực mao mạch', 'áp lực mao mạch phổi bít',
    'kháng lực mạch phổi', 'kháng lực mạch hệ thống',

    # Nội tiết – chuyển hóa
    'toan chuyển hóa', 'kiềm chuyển hóa', 'toan hô hấp', 'kiềm hô hấp',
    'khoảng trống', 'khoảng trống anion', 'nhiễm toan', 'nhiễm toan lactic',
    'hạ natri', 'hạ natri máu', 'hạ kali', 'hạ kali máu',
    'tăng kali', 'tăng kali máu',

    # Thận – lọc máu
    'lọc máu', 'lọc máu liên tục', 'lọc máu ngắt quãng',
    'siêu lọc', 'thay huyết tương', 'thay thế thận',
    'liệu pháp thay thế thận',

    # Truyền máu
    'truyền máu', 'hồng cầu', 'hồng cầu lắng', 'khối tiểu cầu',
    'huyết tương', 'huyết tương tươi', 'tươi đông lạnh',
    'tủa lạnh', 'phản ứng', 'phản ứng truyền máu',

    # Sản khoa
    'dọa sinh', 'dọa sinh non', 'chuyển dạ', 'vỡ ối',
    'băng huyết', 'băng huyết sau sinh', 'tiền sản giật', 'sản giật',
    'rau tiền đạo', 'rau bong non',

    # Nhi khoa
    'cân nặng', 'cân nặng sơ sinh', 'tính liều', 'tính liều theo cân nặng',
    'tiêm chủng', 'phác đồ tiêm chủng', 'mất nước', 'mất nước nhẹ',
    'mất nước vừa', 'mất nước nặng', 'bù dịch đường', 'bù dịch đường uống',

    # Thần kinh
    'ý thức', 'hôn mê', 'co giật', 'liệt nửa người',
    'giãn đồng tử', 'dấu màng não',

    # Nhiễm khuẩn / kháng sinh
    'nhiễm khuẩn bệnh viện', 'kháng thuốc', 'đa kháng thuốc', 'siêu kháng thuốc',
    'liều tải', 'liều duy trì',

    # Dinh dưỡng
    'nuôi ăn', 'nuôi ăn qua sonde', 'nuôi ăn tĩnh mạch',
    'tổng năng lượng', 'vi chất',

    # Tâm thần
    'lo âu', 'trầm cảm', 'hoang tưởng', 'ảo giác', 'mất ngủ',
    'thang điểm lo âu', 'thang điểm trầm cảm',

    # Điều trị & Chẩn đoán
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
    
    # Chuyên khoa
    'tim mạch', 'hô hấp', 'thần kinh', 'tiêu hóa', 'huyết học',
    'chấn thương', 'nhi khoa', 'phẫu thuật', 'thấp khớp', 'tâm thần',
    'da liễu', 'ung thư', 'sản khoa', 'tai mũi họng', 'đánh giá đau',
    'điều dưỡng', 'nhiễm khuẩn', 'thở máy', 'phác đồ', 'nội tiết',
    'sản phụ khoa', 'ngoại khoa', 'nội khoa', 'cấp cứu', 'hồi sức',
    'gây mê', 'hồi tỉnh', 'phục hồi', 'vật lý trị liệu',
    
    # Bệnh lý
    'suy tim', 'suy thận', 'suy gan', 'suy hô hấp', 'suy đa tạng',
    'sốc tim', 'sốc nhiễm khuẩn', 'sốc phản vệ', 'sốc giảm thể tích',
    'nhồi máu', 'đột quỵ', 'xuất huyết', 'chảy máu', 'tắc nghẽn',
    'viêm phổi', 'viêm gan', 'viêm thận', 'viêm ruột', 'viêm màng não',
    'nhiễm khuẩn', 'nhiễm trùng', 'nhiễm độc', 'nhiễm virus',
    'tăng huyết áp', 'hạ huyết áp', 'tăng đường huyết', 'hạ đường huyết',
    'rối loạn', 'bất thường', 'tổn thương', 'biến chứng',
    
    # Thủ thuật & Xét nghiệm
    'xét nghiệm', 'chẩn đoán hình ảnh', 'nội soi', 'sinh thiết',
    'phẫu thuật', 'mổ', 'phẫu tích', 'cắt bỏ', 'ghép tạng',
    'truyền máu', 'truyền dịch', 'truyền thuốc', 'tiêm truyền',
    'thở máy', 'thở oxy', 'hút đờm', 'đặt nội khí quản',
    'đặt catheter', 'đặt sonde', 'đặt ống thông',
    
    # Thuốc & Điều trị
    'kháng sinh', 'kháng viêm', 'giảm đau', 'hạ sốt', 'an thần',
    'gây mê', 'gây tê', 'giãn cơ', 'chống co giật',
    'chống đông', 'chống kết tập tiểu cầu', 'chống viêm',
    'điều chỉnh', 'điều trị', 'phòng ngừa', 'dự phòng',
    
    # Dấu hiệu & Triệu chứng
    'đau ngực', 'khó thở', 'ho khan', 'ho có đờm', 'sốt cao',
    'hạ thân nhiệt', 'tăng thân nhiệt', 'co giật', 'hôn mê',
    'mất ý thức', 'rối loạn ý thức', 'rối loạn nhịp tim',
    'tăng nhịp tim', 'giảm nhịp tim', 'tăng huyết áp', 'hạ huyết áp',
    
    # Đánh giá & Phân loại
    'đánh giá', 'phân loại', 'phân tầng', 'phân độ', 'phân giai đoạn',
    'mức độ', 'độ nặng', 'tiên lượng', 'nguy cơ', 'tỷ lệ',
    'thang điểm', 'bảng điểm', 'chỉ số', 'chỉ số đánh giá',
    
    # Chăm sóc
    'chăm sóc', 'điều dưỡng', 'hộ lý', 'vệ sinh', 'dinh dưỡng',
    'vật lý trị liệu', 'phục hồi chức năng', 'tái khám', 'theo dõi',
    
    # Khác
    'bệnh nhân', 'người bệnh', 'bệnh án', 'tiền sử', 'tiền căn',
    'gia đình', 'di truyền', 'yếu tố', 'nguyên nhân', 'cơ chế',
    'sinh lý bệnh', 'giải phẫu', 'sinh lý', 'bệnh học',
}

MEDICAL_TERMS_3_WORDS = {
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
    'phụ nữ có thai', 'người cao tuổi', 'suy giảm miễn dịch',
    'điều trị bổ sung', 'phòng ngừa ban đầu', 'phòng ngừa tái phát',
    'điều chỉnh theo nhịp tim', 'giá trị tham chiếu',
    'thông tin bệnh nhân', 'tình huống lâm sàng', 'truy cập nhanh',
    'đánh giá ban đầu', 'đánh giá mức độ nặng', 'tiêu chuẩn xét nghiệm',
    'mức độ nguy cơ', 'triệu chứng chính', 'chọn mức độ chức năng',
    'bảng phân loại nguy cơ', 'các trường hợp đặc biệt',
    'tự chăm sóc cá nhân', 'kiểm soát đại tiện', 'kiểm soát tiểu tiện',
    'mức độ ý thức', 'câu hỏi định hướng', 'ý nghĩa lâm sàng',
    'xuất huyết nội sọ', 'xuất huyết não thất', 'vị trí dưới lề',
    'thể tích máu tụ', 'điều trị sau giai đoạn cấp',
    'suy thận cấp', 'suy thận cấp tiền thận', 'phân tích chi tiết',
    'quyết định phẫu thuật', 'quyết định điều trị', 'quyết định lâm sàng',
    'tiêu chí áp dụng', 'tiêu chí chẩn đoán', 'tiêu chí dương tính',
    'tiêu chí nhập icu', 'tiêu chí lâm sàng', 'tiêu chuẩn chẩn đoán',
    'tiêu chuẩn xuất viện', 'thành phần dung dịch',
    'thông tin bổ sung', 'thông tin lâm sàng', 'thông tin thêm',
    'khuyến nghị xử trí', 'khuyến nghị điều chỉnh',
    'chi tiết điểm số', 'chi tiết tính điểm', 'chi tiết tính toán',
    'chi tiết từng biến số', 'chi tiết từng thành phần',
    'chi tiết từng tiêu chí', 'chi tiết đánh giá', 'chăm sóc điều dưỡng',
    'hướng dẫn sử dụng', 'cách đánh giá', 'đánh giá đau',
    'diễn giải kết quả', 'lưu ý quan trọng', 'lưu ý y khoa',
    'lưu ý đặc biệt', 'lưu ý điều trị', 'thang đánh giá',
    'tính toán gần đây', 'mẹo sử dụng', 'tài liệu tham khảo',
}

# Gộp tất cả các cụm từ
ALL_MEDICAL_TERMS = MEDICAL_TERMS_2_WORDS | MEDICAL_TERMS_3_WORDS

# Pattern regex tối ưu để tìm lỗi viết hoa
VIETNAMESE_CAP_PATTERN = re.compile(
    r'\b([A-ZÀÁẢÃẠĂẰẮẲẴẶÂẦẤẨẪẬĐÈÉẺẼẸÊỀẾỂỄỆÌÍỈĨỊÒÓỎÕỌÔỒỐỔỖỘƠỜỚỞỠỢÙÚỦŨỤƯỪỨỬỮỰỲÝỶỸỴ]'
    r'[a-zàáảãạăằắẳẵặâầấẩẫậđèéẻẽẹêềếểễệìíỉĩịòóỏõọôồốổỗộơờớởỡợùúủũụưừứửữựỳýỷỹỵ]+)\s+'
    r'([A-ZÀÁẢÃẠĂẰẮẲẴẶÂẦẤẨẪẬĐÈÉẺẼẸÊỀẾỂỄỆÌÍỈĨỊÒÓỎÕỌÔỒỐỔỖỘƠỜỚỞỠỢÙÚỦŨỤƯỪỨỬỮỰỲÝỶỸỴ]'
    r'[a-zàáảãạăằắẳẵặâầấẩẫậđèéẻẽẹêềếểễệìíỉĩịòóỏõọôồốổỗộơờớởỡợùúủũụưừứửữựỳýỷỹỵ]+)'
)

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

DIRECTORIES = [
    "protocols", "pages", "scores", "labs", "critical_care",
    "antibiotics", "drugs", "components", "ventilator", "diagnosis",
    "utils", "config"
]

IGNORE_PATTERNS = [
    "__pycache__", ".git", "node_modules", "venv", "env", ".pytest_cache",
    "check_", "fix_", "test_", "find_", "vietnamese_", "quick_fix_",
    "deep_scan_", "ultra_deep_", "comprehensive_scan_", "comprehensive_capitalization",
    "fast_vietnamese"
]


def should_process_file(file_path: Path) -> bool:
    """Kiểm tra xem file có nên được xử lý không"""
    file_str = str(file_path)
    for pattern in IGNORE_PATTERNS:
        if pattern in file_str:
            return False
    return file_path.suffix == ".py"


def is_exception(word: str) -> bool:
    """Kiểm tra xem từ có phải là ngoại lệ không"""
    return word.upper() in EXCEPTIONS or word in EXCEPTIONS


def is_start_of_sentence(line: str, pos: int) -> bool:
    """Kiểm tra xem có phải là đầu câu không"""
    before = line[max(0, pos-30):pos].strip()
    if not before:
        return True
    return before[-1] in ['.', '!', '?', ':', ';', '\n', '\r', '(', '[', '{', '"', "'"]


def is_in_string_context(line: str, pos: int) -> bool:
    """Kiểm tra xem có phải trong string context không"""
    before = line[max(0, pos-150):pos]
    after = line[pos:min(len(line), pos+150)]
    
    # Đếm số lượng dấu ngoặc kép và đơn
    single_quotes_before = before.count("'") - before.count("\\'")
    double_quotes_before = before.count('"') - before.count('\\"')
    
    # Nếu số lượng dấu ngoặc kép/đơn là lẻ, thì đang trong string
    in_single = single_quotes_before % 2 == 1
    in_double = double_quotes_before % 2 == 1
    
    # Kiểm tra các context đặc biệt
    in_markdown = any(x in before for x in ['st.markdown', 'st.subheader', 'st.header', 'st.title', 'st.caption'])
    in_fstring = any(x in before for x in ['f"', "f'", 'f"""', "f'''"])
    in_comment = line.strip().startswith('#')
    
    return (in_single or in_double or in_markdown or in_fstring) and not in_comment


def find_capitalization_errors(content: str, file_path: Path) -> List[Dict]:
    """Tìm các lỗi viết hoa trong nội dung - Tối ưu tốc độ"""
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
            
            # Kiểm tra xem có phải là cụm từ y khoa không
            phrase = f"{word1.lower()} {word2.lower()}"
            
            if phrase in ALL_MEDICAL_TERMS:
                # Đây là lỗi - từ thứ 2 không nên viết hoa (trừ đầu câu)
                corrected = f"{word1} {word2.lower()}"
                
                errors.append({
                    'line': line_num,
                    'text': full_match,
                    'corrected': corrected,
                    'context': line.strip()[:200],
                    'phrase': phrase,
                    'file': str(file_path)
                })
    
    return errors


def scan_directory(directory: str) -> List[Dict]:
    """Quét một thư mục và trả về tất cả lỗi"""
    all_errors = []
    dir_path = Path(directory)
    
    if not dir_path.exists():
        return all_errors
    
    for file_path in dir_path.rglob("*"):
        if file_path.is_file() and should_process_file(file_path):
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                errors = find_capitalization_errors(content, file_path)
                all_errors.extend(errors)
                
            except Exception as e:
                print(f"❌ Lỗi khi đọc {file_path}: {e}")
    
    return all_errors


def main():
    import sys
    
    print("=" * 80)
    print("🔍 QUÉT NHANH LỖI VIẾT HOA TIẾNG VIỆT - Y KHOA")
    print("=" * 80)
    print()
    
    start_time = time.time()
    
    all_errors = []
    for directory in DIRECTORIES:
        print(f"📂 Quét: {directory}...", end=" ", flush=True)
        errors = scan_directory(directory)
        all_errors.extend(errors)
        print(f"✅ {len(errors)} lỗi")
    
    elapsed_time = time.time() - start_time
    
    print()
    print("=" * 80)
    print("📊 KẾT QUẢ")
    print("=" * 80)
    print(f"⏱️  Thời gian quét: {elapsed_time:.2f} giây")
    print(f"📝 Tổng số lỗi: {len(all_errors)}")
    print()
    
    if all_errors:
        # Nhóm lỗi theo file
        errors_by_file = defaultdict(list)
        for error in all_errors:
            errors_by_file[error['file']].append(error)
        
        print(f"📄 Số file có lỗi: {len(errors_by_file)}")
        print()
        
        # Hiển thị top 30 file có nhiều lỗi nhất
        sorted_files = sorted(errors_by_file.items(), key=lambda x: len(x[1]), reverse=True)
        
        print("🔝 Top 30 file có nhiều lỗi nhất:")
        print("-" * 80)
        for idx, (file_path, errors) in enumerate(sorted_files[:30], 1):
            print(f"{idx:2d}. {file_path}")
            print(f"    {len(errors)} lỗi")
            # Hiển thị 3 lỗi đầu tiên
            for error in errors[:3]:
                print(f"       Dòng {error['line']}: '{error['text']}' → '{error['corrected']}'")
            if len(errors) > 3:
                print(f"       ... và {len(errors) - 3} lỗi khác")
            print()
        
        # Tạo file báo cáo
        report_file = "vietnamese_caps_report.txt"
        with open(report_file, 'w', encoding='utf-8') as f:
            f.write("=" * 80 + "\n")
            f.write("BÁO CÁO LỖI VIẾT HOA TIẾNG VIỆT\n")
            f.write("=" * 80 + "\n\n")
            f.write(f"Tổng số lỗi: {len(all_errors)}\n")
            f.write(f"Số file có lỗi: {len(errors_by_file)}\n")
            f.write(f"Thời gian quét: {elapsed_time:.2f} giây\n\n")
            
            for file_path, errors in sorted_files:
                f.write(f"\n{'='*80}\n")
                f.write(f"File: {file_path}\n")
                f.write(f"Số lỗi: {len(errors)}\n")
                f.write(f"{'-'*80}\n")
                for error in errors:
                    f.write(f"Dòng {error['line']}: '{error['text']}' → '{error['corrected']}'\n")
                    f.write(f"  Context: {error['context']}\n")
        
        print(f"💾 Báo cáo chi tiết đã lưu vào: {report_file}")
    else:
        print("✅ Không tìm thấy lỗi viết hoa!")
    
    print()
    print("=" * 80)


if __name__ == "__main__":
    main()

