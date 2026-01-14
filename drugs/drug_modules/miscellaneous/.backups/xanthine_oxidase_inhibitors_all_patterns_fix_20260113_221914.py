"""Miscellaneous Drugs - Metabolism, Respiratory, Analgesic, Hematology"""

# Xanthine Oxidase Inhibitors

XANTHINE_OXIDASE_INHIBITORS_DRUGS = {
    "Allopurinol": {'group': 'Metabolism - Xanthine Oxidase Inhibitor',
        'vietnamese_name':
        'Allopurinol, Zyloric', 'administration': ['PO'],
        'indications': [
        'Gout', 'Tăng acid uric máu', 'Phòng ngừa sỏi thận uric acid',
        'Hóa trị (phòng ngừa tăng acid uric)'],
        'contraindications': [
        'Có thai', 'Cho con bú'],
        'dosage': {'adult_standard':
        '100-300mg x 1 lần/ngày', 'adult_severe': '400-600mg/ngày chia 2-3 lần',
        'notes':
        'Khởi đầu với liều thấp (100mg), tăng dần. Dùng kèm colchicine khi bắt đầu để tránh cơn gout cấp'
        },
        'side_effects': ['Ban da (nặng có thể SJS/TEN - nguy hiểm)',
        'Buồn nôn', 'Đau đầu', 'Tăng men gan'],
        'interactions': [
        'Azathioprine/6-mercaptopurine: tăng độc tính (giảm liều azathioprine 75%)'
        , 'Ampicillin/Amoxicillin: tăng nguy cơ ban da',
        'Warfarin: tăng tác dụng chống đông'],
        'mechanism_of_action':
        'Xanthine oxidase inhibitor. Ức chế enzyme xanthine oxidase, enzyme chuyển hypoxanthine thành xanthine và xanthine thành acid uric. Giảm sản xuất acid uric, giảm nồng độ acid uric trong máu và nước tiểu. Được dùng để điều trị gout mạn tính và phòng ngừa tăng acid uric máu (ví dụ trong hóa trị).'
        , 'monitoring': ['Nồng độ acid uric máu (mục tiêu <6 mg/dL)',
        'Chức năng thận: creatinine, BUN (thải qua thận)',
        'Chức năng gan: ALT, AST (có thể gây tăng men gan)',
        'Dấu hiệu ban da (QUAN TRỌNG - có thể tiến triển thành SJS/TEN nếu nặng)',
        'Triệu chứng gout cấp (có thể xảy ra khi bắt đầu điều trị - cần dùng colchicine dự phòng)'
        ],
        'precautions': [
        'KHỞI ĐẦU với liều thấp (100mg/ngày), tăng dần mỗi 1-2 tuần để tránh cơn gout cấp'
        'Dùng kèm colchicine hoặc NSAID khi bắt đầu để dự phòng cơn gout cấp (1-2 tháng đầu)'
        'NGỪNG NGAY nếu có ban da - có thể tiến triển thành SJS/TEN (đe dọa tính mạng)'
        , 'Tránh dùng với ampicillin/amoxicillin (tăng nguy cơ ban da nặng)',
        'Thận trọng khi dùng với azathioprine/6-mercaptopurine (tăng độc tính - cần giảm liều 75%)'
        'Thận trọng khi dùng với warfarin (tăng tác dụng chống đông - theo dõi INR)'
        , 'Thận trọng ở bệnh nhân suy thận (giảm liều)',
        'Uống với nhiều nước để tránh sỏi thận'],
        'pharmacokinetics': {
        'half_life':
        '1-2 giờ (allopurinol), 15-18 giờ (metabolite oxypurinol - hoạt chất)',
        'onset': '1-2 tuần (giảm acid uric máu)', 'duration':
        '24 giờ (uống 1 lần/ngày)', 'protein_binding': 'Rất ít', 'clearance':
        'Thận (chủ yếu, allopurinol và oxypurinol thải qua nước tiểu). Cần giảm liều ở suy thận'
        },
        'storage':
        'Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm, tránh ánh sáng',
        'black_box_warnings':
        'Có thể gây phản ứng da nghiêm trọng (ban da, SJS, TEN) đe dọa tính mạng. Ngừng ngay nếu có ban da. Nguy cơ tăng ở bệnh nhân suy thận, dùng đồng thời với ampicillin/amoxicillin, hoặc có tiền sử dị ứng allopurinol'
        , 'drug_interactions': {
            'major': [
                {'drug': 'Azathioprine, 6-Mercaptopurine',
                 'mechanism': 'Allopurinol ức chế xanthine oxidase, enzyme chuyển hóa azathioprine và 6-mercaptopurine thành các chất không hoạt động. Ức chế enzyme này làm tăng nồng độ azathioprine/6-mercaptopurine trong máu.',
                 'effect': 'Tăng nồng độ azathioprine/6-mercaptopurine đáng kể, tăng độc tính (giảm bạch cầu, độc gan, độc tủy xương)',
                 'management': 'Giảm liều azathioprine/6-mercaptopurine 75% khi dùng với allopurinol. Theo dõi công thức máu và chức năng gan chặt chẽ. Hoặc tránh dùng đồng thời nếu có thể.'},
                {'drug': 'Ampicillin, Amoxicillin',
                 'mechanism': 'Cơ chế chưa rõ ràng, nhưng ampicillin/amoxicillin làm tăng nguy cơ phản ứng da nghiêm trọng với allopurinol.',
                 'effect': 'Tăng nguy cơ ban da nghiêm trọng, SJS, TEN (đe dọa tính mạng)',
                 'management': 'TRÁNH DÙNG đồng thời nếu có thể. Nếu bắt buộc, theo dõi sát dấu hiệu ban da. Ngừng ngay nếu có ban da.'},
                {'drug': 'Warfarin',
                 'mechanism': 'Allopurinol có thể ức chế chuyển hóa warfarin, làm tăng nồng độ warfarin.',
                 'effect': 'Tăng tác dụng chống đông, tăng INR, tăng nguy cơ chảy máu',
                 'management': 'Theo dõi INR chặt chẽ khi bắt đầu hoặc điều chỉnh liều allopurinol. Điều chỉnh liều warfarin nếu cần.'}
            ],
        'moderate': [
                {'drug': 'Theophylline',
                 'mechanism': 'Allopurinol có thể ức chế chuyển hóa theophylline, làm tăng nồng độ theophylline.',
                 'effect': 'Tăng nồng độ theophylline, tăng độc tính (nhịp tim nhanh, co giật)',
                 'management': 'Theo dõi nồng độ theophylline và điều chỉnh liều nếu cần.'},
                {'drug': 'Cyclophosphamide',
                 'mechanism': 'Allopurinol có thể ức chế chuyển hóa cyclophosphamide, làm tăng độc tính.',
                 'effect': 'Tăng độc tính cyclophosphamide',
                 'management': 'Thận trọng khi dùng đồng thời. Theo dõi công thức máu và chức năng gan, thận.'}
            ],
        'minor': []
        },
        'contraindications': {'tuyệt_đối': [
        'Dị ứng allopurinol', 'Có thai (category C)', 'Đang cho con bú',
        'Phản ứng da nghiêm trọng trước đây với allopurinol (SJS, TEN)'],
        'tương_đối': ['Suy thận (giảm liều theo CrCl)',
        'Suy gan (thận trọng, theo dõi chức năng gan)',
        'Đang dùng azathioprine/6-mercaptopurine (cần giảm liều 75%)',
        'Đang dùng ampicillin/amoxicillin (tăng nguy cơ ban da)']},contraindications_detail': {'tuyệt_đối': [
        'Dị ứng allopurinol', 'Có thai (category C)', 'Đang cho con bú',
        'Phản ứng da nghiêm trọng trước đây với allopurinol (SJS, TEN)'],
        'tương_đối': ['Suy thận (giảm liều theo CrCl)',
        'Suy gan (thận trọng, theo dõi chức năng gan)',
        'Đang dùng azathioprine/6-mercaptopurine (cần giảm liều 75%)',
        'Đang dùng ampicillin/amoxicillin (tăng nguy cơ ban da)']},
        'renal_adjustment': {
        'normal': 'Không cần chỉnh liều',
        '30_60': 'Thận trọng, giảm liều 50%',
        'under_30': 'Thận trọng, giảm liều 75% (thải trừ qua thận)',
        'dialysis': 'Thận trọng, giảm liều 75%. Allopurinol và oxypurinol không được lọc sạch hiệu quả qua thẩm phân máu.',
        'notes': 'Allopurinol và metabolite oxypurinol thải trừ chủ yếu qua thận. Suy thận làm tăng nguy cơ tích lũy oxypurinol (half-life dài 15-18 giờ). Cần giảm liều theo CrCl.'
        },
        'pregnancy_lactation': {'fda_category': 'C', 'pregnancy_details':
        'Allopurinol là category C. Không có dữ liệu đầy đủ về an toàn trong thai kỳ. Chỉ dùng nếu lợi ích > nguy cơ. Cân nhắc dùng liều thấp nhất hiệu quả.'
        , 'lactation': {'safety': 'Incompatible', 'details':
        'Allopurinol và oxypurinol bài tiết vào sữa mẹ. Không nên dùng khi cho con bú do thiếu dữ liệu về an toàn cho trẻ bú mẹ.'
        , 'recommendation':
        'KHÔNG dùng khi cho con bú. Ngừng cho con bú hoặc ngừng allopurinol.'}},
        'hepatic_adjustment': {'mild':
        'Không cần điều chỉnh liều. Theo dõi chức năng gan.', 'moderate':
        'Thận trọng, theo dõi chức năng gan. Có thể cần giảm liều nhẹ.',
        'severe':
        'Thận trọng, theo dõi chức năng gan chặt chẽ. Có thể cần giảm liều hoặc tránh dùng.'
        , 'notes':
        'Allopurinol chuyển hóa một phần qua gan. Suy gan có thể làm tăng nồng độ và độc tính. Theo dõi ALT, AST định kỳ.'
        },
        'overdose_management': {'symptoms': [
        'Ban da (có thể tiến triển thành SJS/TEN nếu nặng)', 'Buồn nôn, nôn',
        'Đau đầu', 'Tăng men gan', 'Suy thận (hiếm)', 'Phản ứng dị ứng nặng'],antidote': 'Không có antidote đặc hiệu. Điều trị hỗ trợ.', 'treatment':
        ['Ngừng allopurinol ngay lập tức',
        'Nếu có ban da: đánh giá mức độ nghiêm trọng, nếu SJS/TEN: điều trị như bỏng nặng (ICU, chăm sóc vết thương, điều trị nhiễm trùng)'
        , 'Rửa dạ dày nếu uống trong vòng 1-2 giờ',
        'Than hoạt tính nếu uống trong vòng 1-2 giờ',
        'Theo dõi chức năng gan, thận', 'Điều trị hỗ trợ: truyền dịch nếu cần',
        'Nếu SJS/TEN: điều trị tại ICU, có thể cần corticosteroid, IVIG'],
        'monitoring':
        'Dấu hiệu ban da, chức năng gan, thận, dấu hiệu dị ứng. Nếu SJS/TEN: theo dõi tại ICU.'
        },reversal_agents': {'available': False, 'agents': [],notes':
        'Không có antidote đặc hiệu. Điều trị chủ yếu là hỗ trợ và điều trị triệu chứng. Ngừng thuốc ngay nếu có dấu hiệu SJS/TEN. Hydration đầy đủ để tăng thải trừ.'},administration_instructions': {'oral': {'with_food':
        'Có thể uống với hoặc không thức ăn. Uống với thức ăn có thể giảm kích ứng dạ dày.'
        , 'timing':
        'Uống 1 lần/ngày sau bữa ăn. Uống với nhiều nước (2-3L/ngày) để tránh sỏi thận. Uống cùng thời điểm mỗi ngày.'
        },iv': {'reconstitution': 'Không có dạng IV', 'infusion_rate': 'N/A',
        'compatibility': [],incompatibility': [],
        }},references': {'primary_sources': [
        'FDA Drug Label - Allopurinol (Zyloric, Aloprim)',
        'American College of Rheumatology Guidelines - Gout Management',
        'UpToDate - Allopurinol drug information',
        "Goodman & Gilman's The Pharmacological Basis of Therapeutics (14th ed)",
        'Lexicomp Online - Allopurinol Monograph'],last_updated':
        '2024-12-19', 'evidence_level':
        'A - Dựa trên FDA drug labels, ACR guidelines, và dữ liệu lâm sàng từ nhiều nguồn'
        },risk_flags': {
            'high_alert': True,
            'narrow_therapeutic_index': False,
            'bleeding_risk': False,
            'organ_toxicity': ['Severe skin reactions (SJS/TEN - life-threatening)', 'Hepatotoxicity', 'Bone marrow suppression (rare)'],qt_prolongation': False,
            'hepatotoxicity': True,
            'nephrotoxicity': False,
            'requires_monitoring': ['Skin rash - CRITICAL (stop immediately if rash occurs)', 'Hepatic function (ALT, AST)', 'CBC if long-term use', 'Uric acid levels']
        },guideline_tags': [
            'ACR Guidelines - Gout Management',
            'FDA Black Box Warning - Allopurinol and Severe Skin Reactions',
            'EULAR Guidelines - Gout',
            'FDA Drug Safety Communication - Allopurinol and SJS/TEN',
        ]}}

__all__ = ['XANTHINE_OXIDASE_INHIBITORS_DRUGS']
