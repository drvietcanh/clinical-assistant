"""Enhanced Fields Schema - Extended Fields (8 fields)"""

EXTENDED_FIELDS = {
    "drug_interactions": {'type': 'dict', 'required': False, 'description':
    'Tương tác thuốc chi tiết với mức độ và cơ chế', 'format':
    'Dictionary với các key: major, moderate, minor', 'structure': {'major':
    'List of dict - Tương tác nghiêm trọng (cần tránh hoặc điều chỉnh)',
    'moderate': 'List of dict - Tương tác trung bình (cần theo dõi)',
    'minor': 'List of dict - Tương tác nhẹ (ít quan trọng)'},
    'item_structure': {'drug': 'Tên thuốc tương tác', 'mechanism':
    'Cơ chế tương tác', 'effect': 'Hậu quả của tương tác', 'management':
    'Cách xử trí'}, 'examples': [{'major': [{'drug': 'Warfarin',
    'mechanism': 'Ức chế chuyển hóa warfarin qua CYP2C9', 'effect':
    'Tăng nguy cơ chảy máu, tăng INR', 'management':
    'Giảm liều warfarin, theo dõi INR thường xuyên'}], 'moderate': [],
    'minor': []}]},
    "contraindications": {'type': 'dict', 'required': False, 'description':
    'Chống chỉ định phân loại thành tuyệt đối và tương đối', 'format':
    'Dictionary với tuyệt_đối và tương_đối', 'guidelines': [
    'tuyệt_đối: Chống chỉ định tuyệt đối (không được dùng)',
    'tương_đối: Chống chỉ định tương đối (dùng với thận trọng)',
    'Nếu không có, có thể để None hoặc rỗng'], 'examples': [{'tuyệt_đối': [
    'Dị ứng với thuốc (phản vệ)', 'Tam cá nguyệt 2-3 thai kỳ',
    'Suy thận nặng (CrCl <15)'], 'tương_đối': [
    'Suy thận trung bình (CrCl 15-30) - giảm liều',
    'Suy gan - dùng với thận trọng']}]},
    "pregnancy_lactation": {'type': 'dict', 'required': False, 'description':
    'Thông tin về thai kỳ và cho con bú', 'structure': {'fda_category':
    'A/B/C/D/X - FDA Pregnancy Category', 'pregnancy_details':
    'Chi tiết về sử dụng trong thai kỳ', 'lactation': {'safety':
    'Compatible/Incompatible/Caution', 'details':
    'Chi tiết về bài tiết vào sữa mẹ', 'recommendation':
    'Khuyến nghị sử dụng'}}, 'examples': [{'fda_category': 'B',
    'pregnancy_details':
    'An toàn trong thai kỳ, không có bằng chứng dị tật thai nhi',
    'lactation': {'safety': 'Compatible', 'details':
    'Thuốc bài tiết ít vào sữa mẹ, nồng độ thấp', 'recommendation':
    'Có thể dùng an toàn khi cho con bú'}}]},
    "hepatic_adjustment": {'type': 'dict', 'required': False, 'description':
    'Điều chỉnh liều cho bệnh nhân suy gan', 'structure': {'mild':
    'Điều chỉnh cho suy gan nhẹ (Child-Pugh A)', 'moderate':
    'Điều chỉnh cho suy gan trung bình (Child-Pugh B)', 'severe':
    'Điều chỉnh cho suy gan nặng (Child-Pugh C)', 'notes':
    'Ghi chú thêm về chuyển hóa qua gan'}, 'examples': [{'mild':
    'Không đổi', 'moderate': 'Giảm liều 25-50%', 'severe':
    'Tránh hoặc giảm liều mạnh', 'notes':
    'Thuốc chuyển hóa chủ yếu qua gan (CYP3A4)'}]},
    "overdose_management": {'type': 'dict', 'required': False, 'description': 'Xử trí quá liều',
    'structure': {'symptoms': 'List các triệu chứng quá liều', 'antidote':
    "Antidote nếu có (hoặc 'Không có')", 'treatment':
    'List các bước xử trí', 'monitoring': 'Theo dõi cần thiết'}, 'examples':
    [{'symptoms': ['Buồn nôn, nôn', 'Chóng mặt', 'Hạ huyết áp',
    'Nhịp tim chậm'], 'antidote': 'Không có antidote đặc hiệu', 'treatment':
    ['Rửa dạ dày nếu mới uống <1 giờ', 'Supportive care',
    'Theo dõi ECG, huyết áp', 'Dopamine/norepinephrine nếu hạ huyết áp'],
    'monitoring': 'ECG, huyết áp, nhịp tim liên tục'}]},
    "reversal_agents": {'type': 'dict or None', 'required': False, 'description':
    'Chất đối kháng/antidote cho thuốc (nếu có)', 'format':
    'None nếu không có, hoặc dict với available và agents', 'structure': {
    'available': 'True/False', 'agents':
    'List of dict với name, indication, dose, notes'}, 'examples': [{
    'available': True, 'agents': [{'name': 'Vitamin K', 'indication':
    'Đảo ngược tác dụng chống đông', 'dose': '1-10mg PO/IV tùy mức độ',
    'notes': 'PO tác dụng chậm hơn IV (12-24h vs 6-12h)'}, {'name':
    'Prothrombin Complex Concentrate (PCC)', 'indication':
    'Chảy máu nặng, cấp cứu', 'dose': '25-50 IU/kg IV'}]}, None]},
    "administration_instructions": {'type': 'dict', 'required': False, 'description':
    'Hướng dẫn dùng thuốc chi tiết', 'structure': {'oral': {'with_food':
    'Uống với/không thức ăn', 'timing': 'Thời điểm uống (trước/sau ăn)'},
    'iv': {'reconstitution': 'Cách pha', 'infusion_rate': 'Tốc độ truyền',
    'compatibility': 'List dịch tương thích', 'incompatibility':
    'List dịch không tương thích', 'notes': 'Ghi chú'}}, 'examples': [{
    'oral': {'with_food': 'Uống với thức ăn để giảm kích ứng dạ dày',
    'timing': 'Trước ăn 30 phút để hấp thu tốt nhất'}, 'iv': {
    'reconstitution': 'Pha với 50-100ml NS hoặc D5W', 'infusion_rate':
    'Truyền trong 30-60 phút', 'compatibility': ['NS', 'D5W',
    "Ringer's Lactate"], 'incompatibility': ['Amphotericin B', 'Vancomycin'
    ], 'notes': 'Không pha cùng aminoglycoside'}}]},
    "references": {'type': 'dict', 'required': False, 'description':
    'Tài liệu tham khảo và nguồn thông tin', 'structure': {
    'primary_sources': 'List các nguồn chính', 'last_updated':
    'Ngày cập nhật (YYYY-MM-DD)', 'evidence_level': 'Mức độ chứng cứ'},
    'examples': [{'primary_sources': ['FDA Drug Label - Metformin',
    'UpToDate - Metformin Drug Information',
    "Goodman & Gilman's Pharmacological Basis of Therapeutics, 14th ed"],
    'last_updated': '2024-01-15', 'evidence_level':
    'High (FDA-approved, extensive clinical data)'}]},
}
