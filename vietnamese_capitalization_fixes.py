"""
Tổng hợp các lỗi viết hoa tiếng Việt để sửa triệt để
File này chứa danh sách đầy đủ các pattern cần sửa
"""

# Dictionary chứa các lỗi viết hoa: {pattern: replacement}
VIETNAMESE_CAPITALIZATION_FIXES = {
    # ========== THUẬT NGỮ Y KHOA ==========
    "Giới Tính": "Giới tính",
    "Suy Tim": "Suy tim",
    "Bệnh Phổi Mạn": "Bệnh phổi mạn",
    "Tần Số Thở": "Tần số thở",
    "Tình Trạng Tâm Thần": "Tình trạng tâm thần",
    "Cho Viêm Phổi": "Cho viêm phổi",
    "Điều trị Kháng Sinh Viêm Phổi Cộng Đồng": "Điều trị kháng sinh viêm phổi cộng đồng",
    "Phản Ứng Vận động": "Phản ứng vận động",
    "Thang Đánh giá": "Thang đánh giá",
    "Phản Ứng Lời nói": "Phản ứng lời nói",
    "Xử Trí Xuất Huyết Não": "Xử trí xuất huyết não",
    "Hạn Chế Của ICH Score": "Hạn chế của ICH Score",
    "Bệnh Toàn Thân Nghiêm Trọng": "Bệnh toàn thân nghiêm trọng",
    "Xuất Huyết Dưới Nhện": "Xuất huyết dưới nhện",
    "Khi Nào Nghi Ngờ": "Khi nào nghi ngờ",
    "Chọn Mức Độ Lâm Sàng": "Chọn mức độ lâm sàng",
    
    # ========== LAB & CLINICAL TERMS ==========
    "Huyết Học": "Huyết học",
    "Bilirubin Toàn Phần": "Bilirubin toàn phần",
    "Lâm Sàng": "Lâm sàng",
    "Cổ Chướng": "Cổ chướng",
    "Bệnh Não Gan": "Bệnh não gan",
    "Lọc Máu": "Lọc máu",
    "Bệnh Đi Kèm": "Bệnh đi kèm",
    "Bảng Nguy cơ Theo Điểm": "Bảng nguy cơ theo điểm",
    "Bệnh Gan Còn Ổn Định": "Bệnh gan còn ổn định",
    "Nước Tiểu": "Nước tiểu",
    "Cân Nặng": "Cân nặng",
    "Cân Nặng Lý Tưởng": "Cân nặng lý tưởng",
    "Cân Nặng Điều Chỉnh": "Cân nặng điều chỉnh",
    "Chỉ Số Khối Cơ Thể": "Chỉ số khối cơ thể",
    "Diện Tích Bề Mặt Cơ Thể": "Diện tích bề mặt cơ thể",
    "Toàn Phần": "toàn phần",
    "Calcium Toàn Phần": "Calcium toàn phần",
    "T4 Toàn Phần": "T4 toàn phần",
    "Công Thức Máu Toàn Phần": "Công thức máu toàn phần",
    
    # ========== PROGNOSIS & SCORING ==========
    "Tiên Lượng Viêm Tụy Cấp": "Tiên lượng viêm tụy cấp",
    "Tiêu chí Lúc Nhập Viện": "Tiêu chí lúc nhập viện",
    "Tiêu chí Ban Đầu": "Tiêu chí ban đầu",
    "Tiêu chí Sau 48 Giờ": "Tiêu chí sau 48 giờ",
    "So sánh Các Hệ Thống Tiên lượng": "So sánh các hệ thống tiên lượng",
    "So sánh Tổng Hợp": "So sánh tổng hợp",
    "Triệu chứng Lâm Sàng": "Triệu chứng lâm sàng",
    "Tiền Sử & Yếu tố nguy cơ": "Tiền sử & yếu tố nguy cơ",
    
    # ========== TREATMENT & STRATEGY ==========
    "Chiến Lược 2 Bước": "Chiến lược 2 bước",
    "Các Nguyên Nhân Khác": "Các nguyên nhân khác",
    "Nhập Thông tin 4 Thành phần": "Nhập thông tin 4 thành phần",
    "Xử Trí": "Xử trí",
    "Xử Trí & Quản lý": "Xử trí & quản lý",
    "Xử Trí - Chấn Thương Nhẹ": "Xử trí - chấn thương nhẹ",
    "Xử Trí Ngay Lập Tức": "Xử trí ngay lập tức",
    "Xử Trí Ngay Lập Tứ": "Xử trí ngay lập tức",
    
    # ========== HEMATOLOGY ==========
    "Mức Độ Giảm Tiểu Cầu": "Mức độ giảm tiểu cầu",
    "Thời Gian Xuất Hiện Giảm Tiểu Cầu": "Thời gian xuất hiện giảm tiểu cầu",
    "Huyết Khối hoặc Biến chứng Khác": "Huyết khối hoặc biến chứng khác",
    "Bắt Đầu Kháng Đông Thay Thế": "Bắt đầu kháng đông thay thế",
    "Chuyển Đổi Sang": "Chuyển đổi sang",
    "Thuốc Kháng Đông Thay Thế Cho": "Thuốc kháng đông thay thế cho",
    "Nguyên Nhân Thường gặp": "Nguyên nhân thường gặp",
    "Nguyên Nhân DIC Theo Tần Suất": "Nguyên nhân DIC theo tần suất",
    "Nhiễm Trùng (Phổ Biến Nhất": "Nhiễm trùng (phổ biến nhất",
    "Chấn Thương / Phẫu Thuật": "Chấn thương / phẫu thuật",
    "Ung Thư": "Ung thư",
    "Sản Khoa": "Sản khoa",
    "Bệnh Mạch Máu": "Bệnh mạch máu",
    "Độc Tố / Miễn Dịch": "Độc tố / miễn dịch",
    "Bệnh Gan": "Bệnh gan",
    "Phân biệt DIC với Bệnh Khác": "Phân biệt DIC với bệnh khác",
    
    # ========== TRAUMA & EMERGENCY ==========
    "Ví Dụ AIS Theo Từng Vùng": "Ví dụ AIS theo từng vùng",
    "Cho Từng Vùng": "Cho từng vùng",
    "Quy Tắc Loại Trừ Tổn Thương Cột Sống Cổ": "Quy tắc loại trừ tổn thương cột sống cổ",
    "Đau Chính Giữa Cột Sống Cổ": "Đau chính giữa cột sống cổ",
    "Rối Loạn Ý Thức": "Rối loạn ý thức",
    "Say Rượu / Ma Túy": "Say rượu / ma túy",
    "Tổn Thương Gây Mất Tập Trung": "Tổn thương gây mất tập trung",
    "Quy Tắc Quyết Định Chụp Cột Sống Cổ": "Quy tắc quyết định chụp cột sống cổ",
    "Cơ Chế Chấn Thương Nguy hiểm": "Cơ chế chấn thương nguy hiểm",
    "Yếu tố Cho Phép Đánh": "Yếu tố cho phép đánh",
    "Xoay Cổ": "Xoay cổ",
    "Loại Trừ Lâm Sàng": "Loại trừ lâm sàng",
    
    # ========== ASSESSMENT & EVALUATION ==========
    "Kết quả Đánh giá": "Kết quả đánh giá",
    "Độ Chính Xác": "Độ chính xác",
    "Độ Chính Xác Của": "Độ chính xác của",
    "Các Tình Huống Đặc Biệt": "Các tình huống đặc biệt",
    "Tình Huống": "Tình huống",
    "Tình Huống Đánh giá": "Tình huống đánh giá",
    "Áp Dụng Thành Công": "Áp dụng thành công",
    "Đánh giá Mức Độ Buồn Ngủ Ban Ngày": "Đánh giá mức độ buồn ngủ ban ngày",
    "Đánh giá Trẻ": "Đánh giá trẻ",
    "Phân tích & Khuyến nghị": "Phân tích & khuyến nghị",
    "Cải Thiện Vệ Sinh Giấc Ngủ": "Cải thiện vệ sinh giấc ngủ",
    "An Toàn Lái Xe": "An toàn lái xe",
    "Các Công Cụ Sàng Lọc Khác": "Các công cụ sàng lọc khác",
    
    # ========== INFORMATION & USAGE ==========
    "Thông tin & Cách Sử dụng": "Thông tin & cách sử dụng",
    "Nhập Dữ Liệu Lâm Sàng": "Nhập dữ liệu lâm sàng",
    "Hiện Tại": "Hiện tại",
    "Tiền Thận": "Tiền thận",
    "Sau Thận": "Sau thận",
    "Liên Quan": "Liên quan",
    "Giá trị Mã Hóa & Tính Toán": "Giá trị mã hóa & tính toán",
    "Tiên lượng Chính Xác Hơn": "Tiên lượng chính xác hơn",
    
    # ========== MEDICATION & TREATMENT ==========
    "Thuốc Chống Động Kinh": "Thuốc chống động kinh",
    "Ngừng Thuốc Chống Động Kinh": "Ngừng thuốc chống động kinh",
    "Nồng độ Thuốc Chống Động Kinh": "Nồng độ thuốc chống động kinh",
    "Phân Loại Theo Thời Gian": "Phân loại theo thời gian",
    "Nguyên Nhân & Điều trị Nguyên Nhân": "Nguyên nhân & điều trị nguyên nhân",
    "Tái Ngộ Độc": "Tái ngộ độc",
    "Ngộ Độc Nhẹ": "Ngộ độc nhẹ",
    "Tĩnh Mạch": "Tĩnh mạch",
    "Phân Loại Mức Độ": "Phân loại mức độ",
    "Phân Loại Mức Độ Đau": "Phân loại mức độ đau",
    "Phân Loại Mức Độ Chảy Máu": "Phân loại mức độ chảy máu",
    
    # ========== PATIENT DEMOGRAPHICS ==========
    "Người Cao Tuổi": "Người cao tuổi",
    "Người Cao Tuổ": "Người cao tuổi",
    "Phụ Nữ Có Thai": "Phụ nữ có thai",
    "Trẻ Em": "Trẻ em",
    
    # ========== HYPERTENSIVE EMERGENCY ==========
    "Cơn Tăng Huyết áp Cấp cứu": "Cơn tăng huyết áp cấp cứu",
    "Cơn Tăng Huyết áp Khẩn Cấp": "Cơn tăng huyết áp khẩn cấp",
    "Mục tiêu Hạ Huyết áp": "Mục tiêu hạ huyết áp",
    "Thuốc Điều trị": "Thuốc điều trị",
    "Thuốc IV Thường Dùng": "Thuốc IV thường dùng",
    
    # ========== STROKE ==========
    "Kết quả Tính Liều": "Kết quả tính liều",
    "Hướng Dẫn Pha & Truyền": "Hướng dẫn pha & truyền",
    "Thể Tích & Tốc Độ Truyền": "Thể tích & tốc độ truyền",
    "Monitoring Trong Khi Truyền": "Theo dõi trong khi truyền",
    "Chống chỉ định Điều Chỉnh Huyết áp": "Chống chỉ định điều chỉnh huyết áp",
    "Lấy Huyết Khối Cơ Học": "Lấy huyết khối cơ học",
    "Hỗ Trợ Y Tế & Quản lý Huyết áp": "Hỗ trợ y tế & quản lý huyết áp",
    "Quản lý Sốt": "Quản lý sốt",
    "Nuôi Dưỡng": "Nuôi dưỡng",
    "Dự Phòng": "Dự phòng",
    "Điều trị Sau Giai Đoạn Cấp": "Điều trị sau giai đoạn cấp",
    "Chuẩn Bị Thuốc": "Chuẩn bị thuốc",
    "Chuẩn Bị Nội Soi": "Chuẩn bị nội soi",
    
    # ========== OTHER ==========
    "Cai Rượu Cấp": "Cai rượu cấp",
    "Giao Thức Cấp cứu Điện Giải": "Giao thức cấp cứu điện giải",
    "Máy Tính Giao Thức": "Máy tính giao thức",
    "Giải thích Chuyên Sâu Các Thuật Ngữ": "Giải thích chuyên sâu các thuật ngữ",
    "Suy Thận Cấp": "Suy thận cấp",
    "Suy Thận Cấp Tiền Thận": "Suy thận cấp tiền thận",
}

# Pattern với regex để match nhiều trường hợp
REGEX_PATTERNS = [
    (r'Xử Trí[^a-zA-Z]', 'Xử trí'),
    (r'Độ Chính Xác[^a-zA-Z]', 'Độ chính xác'),
    (r'Tình Huống[^a-zA-Z]', 'Tình huống'),
    (r'Toàn Phầ[^n]', 'Toàn phần'),
]

def get_all_fixes():
    """
    Trả về dictionary chứa tất cả các pattern cần sửa
    """
    return VIETNAMESE_CAPITALIZATION_FIXES.copy()

def get_regex_patterns():
    """
    Trả về list các regex patterns
    """
    return REGEX_PATTERNS.copy()

if __name__ == "__main__":
    print(f"Tổng số pattern cần sửa: {len(VIETNAMESE_CAPITALIZATION_FIXES)}")
    print(f"Tổng số regex patterns: {len(REGEX_PATTERNS)}")
    print("\nDanh sách các pattern:")
    for i, (pattern, replacement) in enumerate(VIETNAMESE_CAPITALIZATION_FIXES.items(), 1):
        print(f"{i}. '{pattern}' → '{replacement}'")

