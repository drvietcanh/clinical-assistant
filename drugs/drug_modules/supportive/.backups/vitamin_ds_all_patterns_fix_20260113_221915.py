"""Supportive Care Medications (Vitamins, Corticosteroids, Antihistamines)
Active module - contains all supportive care drug data"""

# Vitamin Ds

VITAMIN_DS_DRUGS = {
    "Vitamin D": {'group': 'Vitamins/Supplements - Vitamin D',
        'vietnamese_name':
        'Vitamin D, Cholecalciferol (D3), Ergocalciferol (D2)',
        'administration': ['PO'],
        'indications': ['Còi xương', 'Loãng xương (kết hợp với calcium)',
        'Dự phòng thiếu vitamin D',
        'Suy giảm chức năng thận (cần dạng hoạt hóa)'],
        'contraindications': [
        'Tăng calci máu', 'Tăng calci niệu', 'Sỏi thận calci',
        'Quá liều vitamin D'],
        'dosage': {'adult_deficiency':
        '1,000-2,000 IU x 1 lần/ngày hoặc 50,000 IU x 1 lần/tuần x 8 tuần',
        'adult_maintenance': '600-800 IU x 1 lần/ngày',
        'adult_deficiency_severe':
        '50,000 IU x 1 lần/tuần x 8 tuần, sau đó 1,500-2,000 IU/ngày',
        'adult_osteoporosis': '800-1,200 IU/ngày (kết hợp với calcium)',
        'notes':
        'D3 (cholecalciferol) hiệu quả hơn D2. Theo dõi nồng độ 25(OH)D trong máu'
        },
        'renal_adjustment': {'normal': 'Không đổi', '30_60':
        'Có thể cần dạng hoạt hóa (calcitriol)', 'under_30':
        'Dùng calcitriol (dạng hoạt hóa) thay vì vitamin D thường'},
        'side_effects': ['Tăng calci máu (quá liều)', 'Tăng calci niệu',
        'Sỏi thận', 'Buồn nôn, nôn (liều cao)', 'Táo bón'],
        'interactions': [
        'Calcium: tăng hấp thu calcium',
        'Thiazide diuretics: tăng nguy cơ tăng calci máu',
        'Corticosteroid: giảm hấp thu vitamin D',
        'Cholestyramine: giảm hấp thu vitamin D'],
        'pregnancy':
        'A - An toàn, cần thiết cho thai kỳ', 'mechanism_of_action':
        'Vitamin D là hormone steroid quan trọng cho chuyển hóa calcium và phosphate. Có 2 dạng chính: D2 (ergocalciferol, từ thực vật) và D3 (cholecalciferol, từ ánh sáng mặt trời và động vật). Vitamin D được chuyển hóa thành 25(OH)D ở gan (calcidiol), sau đó thành 1,25(OH)2D (calcitriol) ở thận - đây là dạng hoạt động. Calcitriol gắn với vitamin D receptor (VDR) trong tế bào, kích hoạt biểu hiện gen, dẫn đến: tăng hấp thu calcium và phosphate ở ruột, tăng tái hấp thu calcium ở thận, và tăng giải phóng calcium từ xương (với PTH). Vitamin D cũng có vai trò trong hệ miễn dịch, tăng trưởng tế bào, và điều hòa hormone. Thiếu vitamin D gây còi xương (Trẻ em), nhuyễn xương (Người lớn), và loãng xương. Vitamin D được tổng hợp ở da nhờ ánh sáng UVB từ mặt trời, hoặc được hấp thu từ thức ăn/bổ sung.'
        , 'monitoring': [
        'Nồng độ 25(OH)D trong máu (mục tiêu: 30-50 ng/mL hoặc 75-125 nmol/L) - xét nghiệm chính để đánh giá tình trạng vitamin D'
        'Nồng độ calcium trong máu (tăng calci máu có thể xảy ra với quá liều vitamin D)'
        , 'Nồng độ phosphate trong máu',
        'Nồng độ PTH (parathyroid hormone) - tăng khi thiếu vitamin D',
        '24h calcium niệu (tăng calci niệu có thể xảy ra với quá liều)',
        'Creatinine và eGFR - theo dõi chức năng thận',
        'Dấu hiệu lâm sàng tăng calci máu: buồn nôn, nôn, táo bón, yếu cơ, rối loạn tâm thần, sỏi thận (nếu quá liều)'
        , 'DEXA scan (mật độ xương) nếu dùng để điều trị loãng xương',
        'Theo dõi đáp ứng điều trị: giảm triệu chứng còi xương/nhuyễn xương, cải thiện mật độ xương'
        ],
        'precautions': [
        'D3 (cholecalciferol) hiệu quả hơn D2 (ergocalciferol) - nên chọn D3 nếu có thể'
        'Kết hợp với calcium để tăng hiệu quả (đặc biệt trong điều trị loãng xương)'
        'Theo dõi nồng độ 25(OH)D định kỳ để điều chỉnh liều (tránh thiếu hoặc quá liều)'
        'Thận trọng ở bệnh nhân suy thận - có thể cần dùng calcitriol (dạng hoạt hóa) thay vì vitamin D thường'
        , 'Thận trọng ở bệnh nhân có tiền sử sỏi thận calci (tăng calci niệu)',
        'Thận trọng ở bệnh nhân tăng calci máu hoặc tăng calci niệu',
        'Thận trọng với thiazide diuretics (tăng nguy cơ tăng calci máu)',
        'Tránh quá liều - có thể gây tăng calci máu nghiêm trọng, sỏi thận, suy thận'
        , 'Uống nhiều nước để giảm nguy cơ sỏi thận',
        'Corticosteroid và cholestyramine có thể giảm hấp thu vitamin D',
        'Dùng với thức ăn có chất béo để tăng hấp thu (vitamin D tan trong dầu)'
        ],
        'pharmacokinetics': {'half_life':
        '25(OH)D: 2-3 tuần (dài). 1,25(OH)2D: 4-6 giờ (ngắn)', 'onset':
        'Bắt đầu tác dụng sau vài ngày đến vài tuần', 'duration':
        'Liên tục khi dùng đều đặn, tác dụng kéo dài do tích lũy',
        'protein_binding':
        '25(OH)D: gắn với vitamin D-binding protein (DBP). 1,25(OH)2D: gắn với DBP và albumin'
        , 'clearance':
        'Gan: chuyển hóa 25(OH)D thành các metabolites không hoạt động. Thận: chuyển hóa 25(OH)D thành 1,25(OH)2D (dưới tác dụng của PTH), và bài tiết các metabolites. Tích lũy trong mô mỡ (dự trữ dài hạn).'
        },
        'storage':
        'Bảo quản ở nhiệt độ phòng (15-30°C), tránh ánh sáng trực tiếp, tránh ẩm. Để nơi khô ráo, tránh xa tầm tay trẻ em. Một số dạng có thể bảo quản trong tủ lạnh (xem hướng dẫn trên nhãn).'
        , 'black_box_warnings': None, 'contraindications_detail': {
        'tuyệt_đối': [
        'Tăng calci máu (hypercalcemia) - vitamin D làm nặng thêm',
        'Tăng calci niệu (hypercalciuria) nặng - tăng nguy cơ sỏi thận',
        'Sỏi thận calci đang hoạt động - tăng nguy cơ tái phát',
        'Quá liều vitamin D đang điều trị'],
        'tương_đối': [
        'Suy thận nặng - có thể cần dùng calcitriol (dạng hoạt hóa) thay vì vitamin D thường'
        , 'Sỏi thận calci (tiền sử) - thận trọng, theo dõi calci niệu',
        'Bệnh sarcoidosis - tăng nhạy cảm với vitamin D, tăng nguy cơ tăng calci máu'
        'Bệnh cường cận giáp (hyperparathyroidism) - có thể làm nặng tăng calci máu'
        , 'Dùng thiazide diuretics - tăng nguy cơ tăng calci máu']},drug_interactions': {'major': [{'drug':
        'Thiazide diuretics (Hydrochlorothiazide, Chlorthalidone)', 'mechanism':
        'Thiazide diuretics giảm bài tiết calcium qua thận, kết hợp với vitamin D tăng hấp thu calcium, dẫn đến tăng calci máu.'
        , 'effect':
        'Tăng nguy cơ tăng calci máu nghiêm trọng, sỏi thận, suy thận',
        'management':
        'Theo dõi nồng độ calcium trong máu chặt chẽ. Có thể cần giảm liều vitamin D hoặc thiazide. Theo dõi dấu hiệu tăng calci máu.'
        }],
        'moderate': [{'drug': 'Corticosteroid', 'mechanism':
        'Corticosteroid giảm hấp thu calcium ở ruột và tăng bài tiết calcium qua thận, đối kháng với tác dụng của vitamin D.'
        , 'effect': 'Giảm hiệu quả vitamin D, giảm hấp thu calcium',
        'management':
        'Có thể cần tăng liều vitamin D khi dùng corticosteroid. Theo dõi nồng độ calcium và 25(OH)D.'
        }, {'drug': 'Cholestyramine, Colestipol, Colesevelam', 'mechanism':
        'Các resin gắn acid mật gắn với vitamin D trong ruột, giảm hấp thu.',
        'effect': 'Giảm hấp thu vitamin D, giảm hiệu quả', 'management':
        'Cách ít nhất 4 giờ giữa vitamin D và resin. Uống vitamin D trước, resin sau.'
        }],
        'minor': [{'drug': 'Calcium', 'mechanism':
        'Vitamin D tăng hấp thu calcium từ ruột.', 'effect':
        'Tăng hấp thu calcium (tác dụng mong muốn khi dùng kết hợp)',
        'management':
        'Kết hợp vitamin D và calcium là phổ biến và an toàn. Theo dõi nồng độ calcium để tránh tăng calci máu.'
        }]},
        'contraindications': {'tuyệt_đối': [
        'Tăng calci máu (hypercalcemia) - vitamin D làm nặng thêm',
        'Tăng calci niệu (hypercalciuria) nặng - tăng nguy cơ sỏi thận',
        'Sỏi thận calci đang hoạt động - tăng nguy cơ tái phát',
        'Quá liều vitamin D đang điều trị'],
        'tương_đối': [
        'Suy thận nặng - có thể cần dùng calcitriol (dạng hoạt hóa) thay vì vitamin D thường'
        , 'Sỏi thận calci (tiền sử) - thận trọng, theo dõi calci niệu',
        'Bệnh sarcoidosis - tăng nhạy cảm với vitamin D, tăng nguy cơ tăng calci máu'
        'Bệnh cường cận giáp (hyperparathyroidism) - có thể làm nặng tăng calci máu'
        , 'Dùng thiazide diuretics - tăng nguy cơ tăng calci máu']},
        'pregnancy_lactation': {'fda_category': 'A', 'pregnancy_details':
        'Vitamin D an toàn và cần thiết trong thai kỳ. Thiếu vitamin D trong thai kỳ có thể gây còi xương ở trẻ sơ sinh, chậm phát triển xương, và các biến chứng khác. Nhu cầu vitamin D tăng trong thai kỳ. Khuyến cáo: 600-800 IU/ngày trong thai kỳ. Một số phụ nữ có thể cần liều cao hơn nếu thiếu vitamin D. Theo dõi nồng độ 25(OH)D trong thai kỳ.'
        , 'lactation': {'safety': 'Compatible', 'details':
        'Vitamin D bài tiết vào sữa mẹ ở nồng độ thấp. Vitamin D trong sữa mẹ phụ thuộc vào nồng độ vitamin D của mẹ. Bổ sung vitamin D cho mẹ giúp tăng nồng độ trong sữa mẹ.'
        , 'recommendation':
        'Có thể dùng khi cho con bú. Khuyến cáo: 600-800 IU/ngày khi cho con bú. Có thể cần liều cao hơn nếu thiếu vitamin D. Theo dõi nồng độ 25(OH)D của mẹ.'
        }},
        'hepatic_adjustment': {'mild':
        'Không cần điều chỉnh liều. Vitamin D được chuyển hóa ở gan thành 25(OH)D (calcidiol), nhưng suy gan nhẹ không ảnh hưởng đáng kể.'
        , 'moderate':
        'Không cần điều chỉnh liều thường quy. Theo dõi nồng độ 25(OH)D. Chuyển hóa có thể giảm nhẹ ở suy gan trung bình.'
        , 'severe':
        'Thận trọng, theo dõi nồng độ 25(OH)D. Chuyển hóa có thể giảm ở suy gan nặng, nhưng thường không cần điều chỉnh liều.'
        , 'notes':
        'Vitamin D được chuyển hóa ở gan thành 25(OH)D (calcidiol). Suy gan có thể làm giảm chuyển hóa, nhưng thường không ảnh hưởng đáng kể đến nồng độ 25(OH)D. Theo dõi nồng độ 25(OH)D để đảm bảo đủ vitamin D.'
        },
        'overdose_management': {'symptoms': [
        'Tăng calci máu (hypercalcemia): buồn nôn, nôn, táo bón, yếu cơ, rối loạn tâm thần, hôn mê'
        , 'Tăng calci niệu (hypercalciuria): sỏi thận, đau thắt lưng, tiểu máu',
        'Suy thận: do tăng calci máu và sỏi thận',
        'Loạn nhịp tim: do tăng calci máu',
        'Tổn thương thận vĩnh viễn (nếu không điều trị)',
        'Tử vong (trong trường hợp quá liều nghiêm trọng)'],antidote':
        'Không có antidote đặc hiệu. Điều trị hỗ trợ và giảm calci máu.',
        'treatment': ['Ngừng vitamin D ngay lập tức',
        'Ngừng bổ sung calcium nếu đang dùng', 'Điều trị tăng calci máu:',
        '  - Truyền dịch muối đẳng trương (0.9% NaCl) để tăng bài tiết calcium qua thận'
        '  - Furosemide (lợi tiểu) để tăng bài tiết calcium (sau khi đã bù dịch)',
        '  - Calcitonin (giảm giải phóng calcium từ xương) nếu tăng calci máu nặng'
        '  - Bisphosphonates (pamidronate, zoledronate) nếu tăng calci máu nặng, kháng với điều trị khác'
        '  - Glucocorticoid (prednisone) để giảm hấp thu calcium ở ruột (trong một số trường hợp)'
        , '  - Hemodialysis nếu tăng calci máu rất nặng và suy thận',
        'Theo dõi nồng độ calcium trong máu thường xuyên (mỗi 6-12 giờ)',
        'Theo dõi chức năng thận (creatinine, eGFR)',
        'Theo dõi ECG (loạn nhịp tim do tăng calci máu)',
        'Điều trị sỏi thận nếu có',
        'Theo dõi ít nhất 1-2 tuần sau khi ngừng vitamin D (do tích lũy)'],
        'monitoring':
        'Nồng độ calcium trong máu (ionized và total), phosphate, creatinine, eGFR, ECG, dấu hiệu lâm sàng tăng calci máu. Theo dõi ít nhất 1-2 tuần sau khi ngừng vitamin D.'
        },reversal_agents': {'available': False, 'agents': [],notes':
        'Không có antidote đặc hiệu. Điều trị chủ yếu là hỗ trợ và điều trị triệu chứng. Ngừng thuốc ngay. Điều chỉnh calci máu nếu tăng calci máu (hydration, loop diuretics, calcitonin, bisphosphonates nếu cần).'},administration_instructions': {'oral': {'with_food':
        'Nên uống với thức ăn có chất béo để tăng hấp thu (vitamin D tan trong dầu). Có thể uống với sữa, dầu ăn, hoặc bữa ăn có chất béo.'
        , 'timing':
        'Uống 1 lần/ngày hoặc theo chỉ định. Có thể uống bất kỳ lúc nào trong ngày, nhưng nên uống cùng thời điểm mỗi ngày để dễ nhớ. Với liều cao (50,000 IU/tuần), uống 1 lần/tuần vào cùng ngày mỗi tuần.'
        },iv': {'reconstitution':
        'Vitamin D chủ yếu dùng đường uống. Nếu cần dùng IV, có thể dùng calcitriol (dạng hoạt hóa) IV trong một số trường hợp đặc biệt.'
        , 'infusion_rate': 'N/A - chủ yếu dùng đường uống', 'compatibility': [
        'N/A'],incompatibility': ['N/A'],notes':
        'Vitamin D chủ yếu dùng đường uống. Nếu cần dùng IV, cân nhắc dùng calcitriol (dạng hoạt hóa) thay thế.'
        }},references': {'primary_sources': [
        'FDA Drug Label - Vitamin D (Cholecalciferol, Ergocalciferol)',
        'Endocrine Society Clinical Practice Guidelines - Evaluation, Treatment, and Prevention of Vitamin D Deficiency'
        'Institute of Medicine (IOM) - Dietary Reference Intakes for Calcium and Vitamin D'
        , 'UpToDate - Vitamin D deficiency in adults',
        "Goodman & Gilman's The Pharmacological Basis of Therapeutics (14th ed)"
        ],evidence_level':
        'A - Dựa trên FDA drug labels, Endocrine Society guidelines, và dữ liệu lâm sàng từ nhiều nguồn'
        },
        "black_box_warnings": None,
        "risk_flags": {
            "high_alert": False,
            "narrow_therapeutic_index": False,
            "bleeding_risk": False,
            "organ_toxicity": ["Hypercalcemia (with overdose)", "Nephrolithiasis (with overdose)"],
            "qt_prolongation": False,
            "hepatotoxicity": False,
            "nephrotoxicity": False,
            "requires_monitoring": ["25(OH)D levels (target: 30-50 ng/mL)", "Serum calcium", "Phosphate", "PTH", "24h calcium urine (if hypercalciuria)", "Creatinine, eGFR", "Clinical signs of hypercalcemia"]
        },
        "guideline_tags": [
            "Endocrine Society Guidelines - Vitamin D Deficiency",
            "IOM Guidelines - Dietary Reference Intakes for Calcium and Vitamin D",
            "NOF Guidelines - Calcium and Vitamin D for Osteoporosis",
            "FDA Drug Information - Vitamin D",
            "UpToDate - Vitamin D deficiency"
        ],
}}

__all__ = ['VITAMIN_DS_DRUGS']
