"""Enhanced Fields Schema - Basic Fields (6 fields)"""

BASIC_FIELDS = {
    "mechanism_of_action": {'type': 'string', 'required': True, 'description':
    'Cơ chế tác dụng của thuốc', 'format':
    'Mô tả chi tiết cách thuốc hoạt động ở cấp độ phân tử, tế bào, hoặc cơ quan'
    , 'guidelines': [
    'Bắt đầu với thuốc tác động lên receptor/enzyme/target nào',
    'Mô tả chuỗi phản ứng dẫn đến hiệu quả điều trị',
    'Nếu là prodrug, mô tả quá trình chuyển hóa thành chất hoạt động',
    'Độ dài: 50-200 từ (đủ chi tiết nhưng không quá dài)',
    'Ngôn ngữ: Tiếng Việt, dễ hiểu cho bác sĩ lâm sàng'], 'examples': [
    'Ức chế angiotensin converting enzyme (ACE), giảm chuyển angiotensin I thành angiotensin II, giảm aldosterone, gây giãn mạch và giảm huyết áp'
    ,
    'Ức chế sản xuất glucose ở gan, tăng nhạy cảm với insulin ở mô ngoại vi, giảm hấp thu glucose ở ruột'
    ,
    'Ức chế enzyme cyclooxygenase (COX-1 và COX-2), giảm sản xuất prostaglandin, dẫn đến giảm đau, hạ sốt, chống viêm'
    ]},
    "monitoring": {'type': 'list of strings', 'required': True, 'description':
    'Các thông số cần theo dõi khi dùng thuốc', 'format':
    'Danh sách các xét nghiệm, dấu hiệu lâm sàng cần monitor', 'guidelines':
    ['Liệt kê theo tần suất và mức độ quan trọng',
    'Bao gồm: xét nghiệm lab, dấu hiệu lâm sàng, tác dụng phụ cần theo dõi',
    'Có thể có 3-10 mục tùy thuộc vào độ phức tạp của thuốc',
    'Sắp xếp: quan trọng nhất → ít quan trọng hơn',
    'Định dạng: "Tên xét nghiệm/chỉ số - tần suất - mục đích"'], 'examples':
    [['Creatinine, BUN sau 1-2 tuần khi bắt đầu', 'Kali máu định kỳ',
    'Huyết áp', 'Ho khan (tác dụng phụ thường gặp)',
    'Dấu hiệu phù mạch (sưng mặt, lưỡi, họng - cấp cứu)'], [
    'HbA1c mỗi 3 tháng', 'Đường huyết đói và sau ăn',
    'Creatinine, eGFR mỗi 3-6 tháng', 'Vitamin B12 mỗi 1-2 năm',
    'Lactate nếu nghi ngờ nhiễm toan lactic (đau cơ, khó thở, đau bụng)'],
    ['INR mỗi 1-2 ngày khi bắt đầu, sau đó mỗi 1-4 tuần',
    'Dấu hiệu chảy máu (chảy máu cam, xuất huyết dưới da, nôn ra máu, phân đen)'
    , 'Chức năng gan (ALT, AST) định kỳ']]},
    "precautions": {'type': 'list of strings', 'required': True, 'description':
    'Các lưu ý và thận trọng khi sử dụng thuốc', 'format':
    'Danh sách các điểm cần lưu ý khi kê đơn, sử dụng, hoặc theo dõi',
    'guidelines': [
    'Bao gồm: cách dùng, liều khởi đầu, điều kiện đặc biệt, tương tác quan trọng'
    , 'Tập trung vào các điểm thực hành lâm sàng', 'Có thể có 4-8 mục',
    'Sắp xếp: quan trọng nhất → ít quan trọng hơn',
    'Định dạng: "Hành động cụ thể - lý do hoặc hậu quả"'], 'examples': [[
    'Khởi đầu với liều thấp (5-10mg), tăng dần',
    'Ưu điểm: dùng 1 lần/ngày (compliance tốt hơn)',
    'Theo dõi sát creatinine khi bắt đầu (có thể tăng nhẹ)',
    'Tránh dùng với NSAID (giảm hiệu quả, tăng nguy cơ suy thận)',
    'Ngừng ngay nếu có phù mạch (có thể nguy hiểm tính mạng)'], [
    'Ngừng 48h trước và sau khi dùng thuốc cản quang',
    'Theo dõi nhiễm toan lactic ở bệnh nhân suy tim, suy gan, suy thận',
    'Bổ sung vitamin B12 nếu dùng lâu dài',
    'Tránh rượu (tăng nguy cơ nhiễm toan lactic)'], [
    'Khởi đầu với liều thấp, tăng dần theo INR',
    'Tương tác với nhiều thuốc và thức ăn (vitamin K)',
    'Cần giáo dục bệnh nhân về chế độ ăn và dấu hiệu chảy máu',
    'Không ngừng đột ngột (tăng nguy cơ huyết khối)']]},
    "pharmacokinetics": {'type': 'dict', 'required': True, 'description':
    'Thông tin dược động học của thuốc', 'format':
    'Dictionary với các key chuẩn', 'structure': {'half_life':
    "string - Thời gian bán thải (vd: '6.2 giờ', '12 giờ (dài)')", 'onset':
    "string - Thời gian bắt đầu tác dụng (vd: '1 giờ', '15-30 phút')",
    'duration': "string - Thời gian tác dụng (vd: '10-12 giờ', '24 giờ')",
    'protein_binding':
    "string - Tỷ lệ gắn protein (vd: '25-30%', 'Minimal', '>95%')",
    'clearance':
    "string - Đường thải trừ (vd: 'Thận (chủ yếu)', 'Gan qua CYP3A4', 'Thận 60%, gan 40%')"
    }, 'guidelines': [
    'Các key có thể có: half_life, onset, duration, protein_binding, clearance'
    ,
    'Có thể thêm các key khác nếu cần: metabolism, distribution, bioavailability'
    , 'Nếu không có thông tin chính xác, dùng "Không rõ" hoặc ước lượng',
    'Định dạng: string ngắn gọn, dễ hiểu'], 'examples': [{'half_life':
    '6.2 giờ', 'onset': '1-2 giờ', 'duration': '10-12 giờ',
    'protein_binding': 'Minimal', 'clearance': 'Thận (chủ yếu)'}, {
    'half_life': '12 giờ (dài)', 'onset': '1 giờ', 'duration':
    '24 giờ (dài nhất trong các ACE inhibitor)', 'protein_binding': '25%',
    'clearance': 'Thận (100%), không chuyển hóa qua gan'}, {'half_life':
    '36 giờ (rất dài)', 'onset': '2-4 giờ', 'duration': '72 giờ',
    'protein_binding': '>99%', 'clearance': 'Gan qua CYP2C9, CYP3A4'}]},
    "storage": {'type': 'string', 'required': True, 'description':
    'Điều kiện bảo quản thuốc', 'format':
    'Mô tả ngắn gọn điều kiện bảo quản', 'guidelines': [
    'Bao gồm: nhiệt độ, ánh sáng, độ ẩm, các điều kiện đặc biệt',
    'Độ dài: 1-2 câu ngắn gọn',
    'Định dạng chuẩn: "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm, tránh ánh sáng"'
    ], 'examples': ['Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm',
    'Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm, tránh ánh sáng',
    'Bảo quản ở nhiệt độ 2-8°C (tủ lạnh), không đông lạnh',
    'Bảo quản ở nhiệt độ phòng, bảo vệ khỏi ánh sáng, đóng chặt nắp']},
    "black_box_warnings": {'type': 'string or None', 'required': True, 'description':
    'Cảnh báo hộp đen (Black Box Warning) - cảnh báo nghiêm trọng nhất',
    'format': 'String mô tả cảnh báo hoặc None nếu không có', 'guidelines':
    ['Chỉ điền nếu thuốc có Black Box Warning chính thức (FDA)',
    'Nếu không có Black Box Warning nhưng có cảnh báo quan trọng, mô tả ngắn gọn'
    , 'Nếu không có cảnh báo nghiêm trọng, dùng None',
    'Độ dài: 1-2 câu, ngắn gọn và rõ ràng',
    'Bắt đầu với vấn đề nghiêm trọng nhất'], 'examples': [
    'Nhiễm toan lactic - có thể tử vong. Nguy cơ cao ở suy thận, suy tim, suy gan, nhiễm trùng nặng'
    ,
    'Chống chỉ định trong thai kỳ - có thể gây dị tật thai nhi và tử vong thai nhi. Phù mạch có thể đe dọa tính mạng'
    , None,
    'Tăng nguy cơ nhiễm trùng nghiêm trọng, ung thư hạch, và các tác dụng phụ nghiêm trọng khác. Cần theo dõi chặt chẽ'
    ]},
}
