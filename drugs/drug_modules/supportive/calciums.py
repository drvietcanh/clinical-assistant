"""Supportive Care Medications (Vitamins, Corticosteroids, Antihistamines)
Active module - contains all supportive care drug data"""

# Calciums

CALCIUMS_DRUGS = {
    "Calcium": {'group': 'Vitamins/Supplements - Calcium', 'vietnamese_name':
        'Calcium, Calcium carbonate, Calcium citrate', 'administration': ['PO'],
        'indications': ['Thiếu calci', 'Loãng xương (kết hợp với vitamin D)',
        'Hạ calci máu', 'Dự phòng loãng xương', 'Có thai, cho con bú'],
        'contraindications': ['Tăng calci máu', 'Tăng calci niệu',
        'Sỏi thận calci', 'Suy thận nặng', 'Suy tim (calcium carbonate)'],
        'dosage': {'adult_daily_requirement':
        '1,000-1,200mg nguyên tố calci/ngày', 'adult_calcium_carbonate':
        '500-1,000mg x 2-3 lần/ngày (40% nguyên tố calci)',
        'adult_calcium_citrate':
        '500-1,000mg x 2-3 lần/ngày (21% nguyên tố calci)',
        'adult_hypocalcemia': '1-2g nguyên tố calci/ngày chia 2-3 lần',
        'adult_osteoporosis':
        '1,000-1,200mg nguyên tố calci/ngày (với vitamin D)', 'notes':
        'Calcium citrate hấp thu tốt hơn, không cần acid dạ dày. Uống với thức ăn'
        }, 'renal_adjustment': {'normal': 'Không đổi', '30_60':
        'Thận trọng, giảm liều', 'under_30':
        'Tránh dùng hoặc giảm liều (tăng nguy cơ tăng calci máu)'},
        'side_effects': ['Táo bón', 'Đầy hơi', 'Buồn nôn',
        'Tăng calci máu (quá liều)', 'Sỏi thận (quá liều)',
        'Giảm hấp thu sắt, kẽm'], 'interactions': [
        'Sắt: giảm hấp thu sắt - cách 2 giờ',
        'Tetracycline/Quinolone: giảm hấp thu kháng sinh - cách 2 giờ',
        'Thyroxine: giảm hấp thu thyroxine - cách 4 giờ',
        'Digoxin: tăng nguy cơ loạn nhịp',
        'Thiazide diuretics: tăng nguy cơ tăng calci máu',
        'Vitamin D: tăng hấp thu calci'],
        'mechanism_of_action':
        'Calcium là khoáng chất thiết yếu cho nhiều chức năng sinh học. Trong xương: calcium là thành phần chính của hydroxyapatite, tạo cấu trúc và độ bền của xương. Trong máu: calcium ion (Ca2+) tham gia vào quá trình đông máu (cần thiết cho cascade đông máu), co cơ (bao gồm cơ tim và cơ trơn), dẫn truyền thần kinh, và giải phóng hormone. Calcium được hấp thu ở ruột non (chủ yếu ở tá tràng) nhờ vitamin D (calcitriol) và parathyroid hormone (PTH). Hấp thu phụ thuộc vào dạng muối: calcium citrate hấp thu tốt hơn calcium carbonate vì không cần acid dạ dày. Nồng độ calcium trong máu được điều hòa chặt chẽ bởi PTH, calcitonin, và vitamin D thông qua hấp thu ở ruột, tái hấp thu ở thận, và giải phóng từ xương.'
        , 'monitoring': [
        'Nồng độ calcium trong máu (ionized calcium hoặc total calcium với albumin) - theo dõi tăng calci máu'
        ,
        'Nồng độ phosphate trong máu (tăng calci máu có thể kèm hạ phosphate)',
        'Creatinine và eGFR - theo dõi chức năng thận (quan trọng vì tăng calci máu có thể gây suy thận)'
        , 'Nồng độ PTH (parathyroid hormone) nếu có triệu chứng tăng calci máu',
        '25(OH)D và 1,25(OH)2D nếu nghi ngờ liên quan đến vitamin D',
        'Dấu hiệu lâm sàng tăng calci máu: buồn nôn, nôn, táo bón, yếu cơ, rối loạn tâm thần, sỏi thận'
        , 'DEXA scan (mật độ xương) nếu dùng để điều trị loãng xương',
        'Sỏi thận (siêu âm) nếu có triệu chứng hoặc dùng liều cao'],
        'precautions': ['Uống với thức ăn để tăng hấp thu và giảm tác dụng phụ',
        'Chia liều (không uống quá 500-600mg nguyên tố calci mỗi lần) để tăng hấp thu'
        ,
        'Calcium citrate hấp thu tốt hơn calcium carbonate, đặc biệt ở người già hoặc dùng PPI (không cần acid dạ dày)'
        ,
        'Cách xa các thuốc khác ít nhất 2 giờ: sắt, tetracycline, quinolone, thyroxine (giảm hấp thu)'
        ,
        'Thận trọng ở bệnh nhân suy thận (tăng nguy cơ tăng calci máu, sỏi thận)',
        'Thận trọng ở bệnh nhân có tiền sử sỏi thận calci (tăng calci niệu)',
        'Thận trọng ở bệnh nhân suy tim (calcium carbonate có thể gây đầy hơi, táo bón)'
        ,
        'Kết hợp với vitamin D để tăng hấp thu và hiệu quả (đặc biệt trong điều trị loãng xương)'
        , 'Uống nhiều nước để giảm nguy cơ sỏi thận',
        'Theo dõi triệu chứng tăng calci máu: buồn nôn, nôn, táo bón, yếu cơ'],
        'pharmacokinetics': {'half_life':
        'Không áp dụng (calcium là khoáng chất, không có half-life như thuốc)',
        'onset': 'Bắt đầu tác dụng sau vài giờ đến vài ngày', 'duration':
        'Liên tục khi dùng đều đặn', 'protein_binding':
        'Khoảng 40-50% calcium trong máu gắn với albumin, phần còn lại là ionized (Ca2+) - dạng hoạt động'
        , 'clearance':
        'Thận: bài tiết qua nước tiểu (tái hấp thu ở ống thận dưới tác dụng của PTH). Xương: lưu trữ dài hạn. Ruột: bài tiết qua phân (phần không hấp thu).'
        }, 'storage':
        'Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm, tránh ánh sáng trực tiếp. Để nơi khô ráo, tránh xa tầm tay trẻ em.'
        , 'black_box_warnings': None, 'contraindications_detail': {
        'tuyệt_đối': [
        'Tăng calci máu (hypercalcemia) - calcium làm nặng thêm',
        'Tăng calci niệu (hypercalciuria) nặng - tăng nguy cơ sỏi thận',
        'Sỏi thận calci đang hoạt động - tăng nguy cơ tái phát',
        'Suy thận nặng với tăng calci máu'], 'tương_đối': [
        'Suy thận nặng - tăng nguy cơ tăng calci máu, sỏi thận',
        'Sỏi thận calci (tiền sử) - thận trọng, theo dõi calci niệu',
        'Bệnh sarcoidosis - tăng nhạy cảm với calcium, tăng nguy cơ tăng calci máu'
        ,
        'Bệnh cường cận giáp (hyperparathyroidism) - có thể làm nặng tăng calci máu'
        , 'Dùng thiazide diuretics - tăng nguy cơ tăng calci máu',
        'Suy tim - calcium carbonate có thể gây đầy hơi, táo bón']}, 'drug_interactions': {'major': [{'drug':
        'Levothyroxine', 'mechanism':
        'Calcium gắn với levothyroxine trong ruột, tạo phức hợp không hấp thu được, giảm hấp thu levothyroxine.'
        , 'effect':
        'Giảm hấp thu levothyroxine 30-50%, giảm hiệu quả điều trị suy giáp',
        'management':
        'Cách ít nhất 4 giờ giữa calcium và levothyroxine. Uống levothyroxine sáng đói, calcium sau bữa ăn.'
        }, {'drug': 'Tetracycline, Doxycycline, Minocycline', 'mechanism':
        'Calcium gắn với tetracycline trong ruột, tạo phức hợp không hấp thu được, giảm hấp thu cả hai.'
        , 'effect':
        'Giảm hấp thu cả calcium và tetracycline, giảm hiệu quả điều trị',
        'management':
        'Cách ít nhất 2 giờ giữa calcium và tetracycline. Uống calcium trước, tetracycline sau.'
        }, {'drug': 'Quinolone (Ciprofloxacin, Levofloxacin, Moxifloxacin)',
        'mechanism':
        'Calcium gắn với quinolone trong ruột, tạo phức hợp không hấp thu được, giảm hấp thu cả hai.'
        , 'effect':
        'Giảm hấp thu cả calcium và quinolone, giảm hiệu quả điều trị',
        'management':
        'Cách ít nhất 2 giờ giữa calcium và quinolone. Uống calcium trước, quinolone sau.'
        }], 'moderate': [
        {'drug': 'Digoxin', 'mechanism':
        'Calcium có thể tăng tác dụng của digoxin trên tim, tăng nguy cơ loạn nhịp.'
        , 'effect': 'Tăng nguy cơ loạn nhịp tim do digoxin', 'management':
        'Thận trọng. Theo dõi nồng độ digoxin và ECG. Tránh tăng calci máu.'},
        {'drug': 'Thiazide diuretics (Hydrochlorothiazide, Chlorthalidone)',
        'mechanism':
        'Thiazide diuretics giảm bài tiết calcium qua thận, kết hợp với bổ sung calcium, dẫn đến tăng calci máu.'
        , 'effect': 'Tăng nguy cơ tăng calci máu, sỏi thận', 'management':
        'Theo dõi nồng độ calcium trong máu chặt chẽ. Có thể cần giảm liều calcium hoặc thiazide.'
        }, {'drug': 'Sắt (Iron)', 'mechanism':
        'Calcium gắn với sắt trong ruột, giảm hấp thu sắt.', 'effect':
        'Giảm hấp thu sắt, giảm hiệu quả điều trị thiếu máu', 'management':
        'Cách ít nhất 2 giờ giữa calcium và sắt. Uống sắt khi bụng đói, calcium sau bữa ăn.'
        }], 'minor': [
        {'drug': 'Vitamin D', 'mechanism':
        'Vitamin D tăng hấp thu calcium từ ruột.', 'effect':
        'Tăng hấp thu calcium (tác dụng mong muốn khi dùng kết hợp)',
        'management':
        'Kết hợp calcium và vitamin D là phổ biến và an toàn. Theo dõi nồng độ calcium để tránh tăng calci máu.'
        }]}, 'contraindications': {'tuyệt_đối': [
        'Tăng calci máu (hypercalcemia) - calcium làm nặng thêm',
        'Tăng calci niệu (hypercalciuria) nặng - tăng nguy cơ sỏi thận',
        'Sỏi thận calci đang hoạt động - tăng nguy cơ tái phát',
        'Suy thận nặng với tăng calci máu'], 'tương_đối': [
        'Suy thận nặng - tăng nguy cơ tăng calci máu, sỏi thận',
        'Sỏi thận calci (tiền sử) - thận trọng, theo dõi calci niệu',
        'Bệnh sarcoidosis - tăng nhạy cảm với calcium, tăng nguy cơ tăng calci máu'
        ,
        'Bệnh cường cận giáp (hyperparathyroidism) - có thể làm nặng tăng calci máu'
        , 'Dùng thiazide diuretics - tăng nguy cơ tăng calci máu',
        'Suy tim - calcium carbonate có thể gây đầy hơi, táo bón']},
        'pregnancy_lactation': {'fda_category': 'A', 'pregnancy_details':
        'Calcium an toàn và cần thiết trong thai kỳ. Thiếu calcium trong thai kỳ có thể gây loãng xương ở mẹ, chậm phát triển xương ở thai nhi, và các biến chứng khác. Nhu cầu calcium tăng trong thai kỳ. Khuyến cáo: 1,000-1,300 mg nguyên tố calci/ngày trong thai kỳ. Phụ nữ thiếu calcium cần bổ sung đủ. Kết hợp với vitamin D để tăng hấp thu.'
        , 'lactation': {'safety': 'Compatible', 'details':
        'Calcium bài tiết vào sữa mẹ. Nồng độ calcium trong sữa mẹ tương đối ổn định và không phụ thuộc nhiều vào nồng độ calcium của mẹ (do điều hòa từ xương). Tuy nhiên, thiếu calcium ở mẹ có thể ảnh hưởng đến sức khỏe mẹ (loãng xương).'
        , 'recommendation':
        'Có thể dùng khi cho con bú. Khuyến cáo: 1,000-1,300 mg nguyên tố calci/ngày khi cho con bú. Phụ nữ thiếu calcium cần bổ sung đủ để đảm bảo sức khỏe mẹ.'
        }}, 'hepatic_adjustment': {'mild':
        'Không cần điều chỉnh liều. Calcium không chuyển hóa ở gan.',
        'moderate':
        'Không cần điều chỉnh liều. Calcium không chuyển hóa ở gan.', 'severe':
        'Không cần điều chỉnh liều. Calcium không chuyển hóa ở gan. Tuy nhiên, suy gan nặng có thể ảnh hưởng đến albumin (protein binding của calcium).'
        , 'notes':
        'Calcium không chuyển hóa ở gan. Suy gan không ảnh hưởng đáng kể đến nồng độ calcium. Tuy nhiên, suy gan nặng có thể ảnh hưởng đến albumin, ảnh hưởng đến protein binding của calcium (nhưng không ảnh hưởng đến ionized calcium - dạng hoạt động).'
        }, 'overdose_management': {'symptoms': [
        'Tăng calci máu (hypercalcemia): buồn nôn, nôn, táo bón, yếu cơ, rối loạn tâm thần, hôn mê'
        , 'Tăng calci niệu (hypercalciuria): sỏi thận, đau thắt lưng, tiểu máu',
        'Suy thận: do tăng calci máu và sỏi thận',
        'Loạn nhịp tim: do tăng calci máu (đặc biệt với digoxin)',
        'Tổn thương thận vĩnh viễn (nếu không điều trị)',
        'Tử vong (trong trường hợp quá liều nghiêm trọng)'], 'antidote':
        'Không có antidote đặc hiệu. Điều trị hỗ trợ và giảm calci máu.',
        'treatment': ['Ngừng calcium ngay lập tức',
        'Ngừng bổ sung vitamin D nếu đang dùng', 'Điều trị tăng calci máu:',
        '  - Truyền dịch muối đẳng trương (0.9% NaCl) để tăng bài tiết calcium qua thận'
        ,
        '  - Furosemide (lợi tiểu) để tăng bài tiết calcium (sau khi đã bù dịch)',
        '  - Calcitonin (giảm giải phóng calcium từ xương) nếu tăng calci máu nặng'
        ,
        '  - Bisphosphonates (pamidronate, zoledronate) nếu tăng calci máu nặng, kháng với điều trị khác'
        ,
        '  - Glucocorticoid (prednisone) để giảm hấp thu calcium ở ruột (trong một số trường hợp)'
        , '  - Hemodialysis nếu tăng calci máu rất nặng và suy thận',
        'Theo dõi nồng độ calcium trong máu thường xuyên (mỗi 6-12 giờ)',
        'Theo dõi chức năng thận (creatinine, eGFR)',
        'Theo dõi ECG (loạn nhịp tim do tăng calci máu, đặc biệt với digoxin)',
        'Điều trị sỏi thận nếu có'], 'monitoring':
        'Nồng độ calcium trong máu (ionized và total), phosphate, creatinine, eGFR, ECG, dấu hiệu lâm sàng tăng calci máu.'
        }, 'reversal_agents': {'available': False, 'agents': [], 'notes':
        'Không có antidote đặc hiệu. Điều trị chủ yếu là hỗ trợ và điều trị triệu chứng. Ngừng thuốc ngay. Điều chỉnh calci máu nếu tăng calci máu (hydration, loop diuretics, calcitonin, bisphosphonates nếu cần).'},
        'administration_instructions': {'oral': {'with_food':
        'Nên uống với thức ăn để tăng hấp thu và giảm tác dụng phụ (táo bón, đầy hơi).'
        , 'timing':
        'Uống 2-3 lần/ngày, chia liều (không uống quá 500-600mg nguyên tố calci mỗi lần) để tăng hấp thu. Cách xa các thuốc khác ít nhất 2-4 giờ: sắt (2 giờ), tetracycline, quinolone (2 giờ), levothyroxine (4 giờ).'
        }, 'iv': {'reconstitution':
        'Calcium chủ yếu dùng đường uống. IV chỉ dùng trong trường hợp hạ calci máu cấp tính.'
        , 'infusion_rate':
        'Truyền chậm (không quá 0.5-1 mEq/phút). Không truyền nhanh (tăng nguy cơ loạn nhịp tim).'
        , 'compatibility': ['Normal saline (0.9% NaCl), D5W'],
        'incompatibility': [
        'Không trộn với bicarbonate, phosphate (tạo kết tủa)'], 'notes':
        'Calcium IV chỉ dùng trong trường hợp hạ calci máu cấp tính. Truyền chậm, theo dõi ECG. Không trộn với bicarbonate hoặc phosphate.'
        }}, 'references': {'primary_sources': [
        'FDA Drug Label - Calcium (Calcium carbonate, Calcium citrate)',
        'Institute of Medicine (IOM) - Dietary Reference Intakes for Calcium and Vitamin D'
        , 'National Osteoporosis Foundation Guidelines - Calcium and Vitamin D',
        'UpToDate - Calcium supplementation',
        "Goodman & Gilman's The Pharmacological Basis of Therapeutics (14th ed)"
        ], 'evidence_level':
        'A - Dựa trên FDA drug labels, IOM/NOF guidelines, và dữ liệu lâm sàng'},
        "black_box_warnings": None,
        "risk_flags": {
            "high_alert": False,
            "narrow_therapeutic_index": False,
            "bleeding_risk": False,
            "organ_toxicity": ["Hypercalcemia (with overdose)", "Nephrolithiasis (with overdose)"],
            "qt_prolongation": False,
            "hepatotoxicity": False,
            "nephrotoxicity": False,
            "requires_monitoring": ["Serum calcium (ionized and total)", "Phosphate", "Creatinine, eGFR", "PTH (if hypercalcemia)", "24h calcium urine (if hypercalciuria)", "Clinical signs of hypercalcemia"]
        },
        "guideline_tags": [
            "IOM Guidelines - Dietary Reference Intakes for Calcium and Vitamin D",
            "NOF Guidelines - Calcium and Vitamin D for Osteoporosis",
            "FDA Drug Information - Calcium",
            "UpToDate - Calcium supplementation"
        ],
}}

__all__ = ['CALCIUMS_DRUGS']
