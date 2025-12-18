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

    # === NEW META FIELDS ===
    "risk_flags": {
        'type': 'dict',
        'required': False,
        'description': 'Các cờ cảnh báo nguy cơ (high-alert, hẹp khoảng điều trị, độc tính cơ quan, LASA...)',
        'format': 'Dictionary với các key chuẩn, ưu tiên đánh dấu nhanh các thuốc nguy cơ cao',
        'structure': {
            'high_alert': 'bool - Thuốc thuộc nhóm high-alert theo ISMP/ICU (heparin, insulin, opioid mạnh, thuốc vận mạch, chống loạn nhịp, hóa trị...)',
            'narrow_therapeutic_index': 'bool - Thuốc có khoảng điều trị hẹp (vancomycin, digoxin, phenytoin, carbamazepine, theophylline, warfarin...)',
            'look_alike_sound_alike': 'List of strings - Danh sách thuốc dễ nhầm tên hoặc dạng trình bày (LASA)',
            'organ_toxicity': {
                'hepatic': "string - Nguy cơ độc gan: 'low' / 'moderate' / 'high' / 'unknown'",
                'renal': "string - Nguy cơ độc thận: 'low' / 'moderate' / 'high' / 'unknown'",
                'cardiac': "string - Nguy cơ tim mạch: 'low' / 'moderate' / 'high' / 'qt_prolongation'",
                'hematologic': "string - Nguy cơ huyết học (giảm bạch cầu, giảm tiểu cầu, suy tủy...): 'low' / 'moderate' / 'high' / 'unknown'"
            },
            'requires_double_check': 'bool - Khuyến cáo double-check độc lập trước khi dùng (dose/route/patient)',
            'icu_critical_care_only': 'bool - Thuốc chủ yếu dùng ICU/HSTC, nên hạn chế dùng ngoài ICU',
        },
        'examples': [
            {
                'high_alert': True,
                'narrow_therapeutic_index': True,
                'look_alike_sound_alike': ['Heparin (IV)', 'Heparin flush'],
                'organ_toxicity': {
                    'hepatic': 'low',
                    'renal': 'high',
                    'cardiac': 'qt_prolongation',
                    'hematologic': 'high'
                },
                'requires_double_check': True,
                'icu_critical_care_only': True
            }
        ]
    },

    "guideline_tags": {
        'type': 'dict',
        'required': False,
        'description': 'Liên kết thuốc với guideline, phân loại ATC/AHFS và nhãn lâm sàng quan trọng',
        'format': 'Dictionary gồm các thẻ chuẩn hóa để hỗ trợ tìm kiếm theo guideline/chuyên khoa',
        'structure': {
            'who_atc': 'string - Mã ATC chính (vd: C09AA03 cho Enalapril) nếu có',
            'ahfs_category': 'string - Nhóm AHFS Drug Information (tùy chọn)',
            'vietnam_essential_medicines': 'bool - Có nằm trong Danh mục thuốc thiết yếu Việt Nam',
            'international_guidelines': 'List of dict - Liên kết đến guideline quốc tế',
            'vn_guidelines': 'List of dict - Liên kết đến guideline/hướng dẫn Bộ Y tế hoặc hội chuyên ngành trong nước',
            'clinical_tags': 'List of strings - Thẻ lâm sàng hỗ trợ filter nhanh (vd: "first_line_htn", "heart_failure_hfref", "aki_high_risk")'
        },
        'item_structure': {
            'international_guidelines': {
                'source': 'Tên guideline (vd: ESC 2021 HF, KDIGO 2012 CKD, ACC/AHA 2017 HTN)',
                'recommendation': 'Tóm tắt vai trò thuốc trong guideline (first-line / second-line / only if ...)',
                'context': 'Ngữ cảnh: bệnh lý, mức độ nặng, line điều trị'
            },
            'vn_guidelines': {
                'source': 'Tên hướng dẫn Việt Nam (vd: BYT – Hướng dẫn tăng huyết áp 2020)',
                'recommendation': 'Vai trò thuốc trong guideline Việt Nam',
                'context': 'Ngữ cảnh áp dụng tại VN (tuyến, chuyên khoa, đối tượng)'
            }
        },
        'examples': [
            {
                'who_atc': 'C09AA02',
                'ahfs_category': '24.08.08 ACE Inhibitors',
                'vietnam_essential_medicines': True,
                'international_guidelines': [
                    {
                        'source': 'ESC 2021 Heart Failure',
                        'recommendation': 'First-line therapy for HFrEF with ACE inhibitor if tolerated',
                        'context': 'Heart failure with reduced ejection fraction (NYHA II–III)'
                    }
                ],
                'vn_guidelines': [
                    {
                        'source': 'BYT – Hướng dẫn chẩn đoán và điều trị tăng huyết áp 2020',
                        'recommendation': 'Một trong các lựa chọn hàng đầu trong điều trị tăng huyết áp',
                        'context': 'Tăng huyết áp nguyên phát, không biến chứng'
                    }
                ],
                'clinical_tags': ['first_line_htn', 'hfref_mortality_benefit']
            }
        ]
    },

    "availability_vietnam": {
        'type': 'dict',
        'required': False,
        'description': 'Thông tin về mức độ sẵn có và chi trả tại Việt Nam',
        'format': 'Dictionary tóm tắt tình trạng lưu hành, tuyến sử dụng và BHYT',
        'structure': {
            'status': "string - 'common' | 'limited' | 'rare' | 'not_available' | 'unknown'",
            'level_of_care': "List of strings - Các tuyến điều trị điển hình: 'commune', 'district', 'provincial', 'central', 'private'",
            'insurance_coverage': "string - Tình trạng BHYT: 'bhyt_full' | 'bhyt_partial' | 'no_bhyt' | 'unknown'",
            'brand_examples': 'List of strings - Một số tên biệt dược phổ biến tại VN (nếu có)',
            'notes': 'string - Ghi chú thêm: yêu cầu hội chẩn, quản lý đặc biệt, giới hạn sử dụng nội trú...'
        },
        'examples': [
            {
                'status': 'common',
                'level_of_care': ['district', 'provincial', 'central'],
                'insurance_coverage': 'bhyt_full',
                'brand_examples': ['Captopril STADA', 'Capoten'],
                'notes': 'Phổ biến ở hầu hết bệnh viện, có nhiều generic. Thường có trong danh mục BHYT.'
            },
            {
                'status': 'limited',
                'level_of_care': ['provincial', 'central'],
                'insurance_coverage': 'bhyt_partial',
                'brand_examples': ['Linezolid Sandoz'],
                'notes': 'Chủ yếu tuyến cuối, thường cần hội chẩn nhiễm khuẩn để sử dụng.'
            }
        ]
    },
}
