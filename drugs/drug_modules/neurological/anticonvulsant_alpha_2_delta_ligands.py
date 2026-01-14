"""Neurological and Psychiatric Medications
Active module - contains all neurological and psychiatric drug data"""

# Anticonvulsant (Alpha-2-delta ligand)s

ANTICONVULSANT_ALPHA_2_DELTA_LIGANDS_DRUGS = {
    "Gabapentin": {'group': 'Neurology - Anticonvulsant (Alpha-2-delta ligand)',
        'vietnamese_name': 'Gabapentin, Neurontin', 'administration': ['PO'],
        'indications': ['Động kinh cục bộ',
        'Đau thần kinh (postherpetic neuralgia, diabetic neuropathy)',
        'Rối loạn lo âu', 'Hội chứng chân không yên'],
        'contraindications': [
        'Dị ứng'],
        'dosage': {'adult_epilepsy':
        '300mg x 3 lần/ngày, tăng đến 900-1800mg/ngày', 'adult_neuropathic':
        '300mg x 3 lần/ngày, tăng đến 1800-3600mg/ngày', 'adult_max':
        '3600mg/ngày (chia 3 lần)', 'notes':
        'Hấp thu giảm khi tăng liều. Uống cách xa antacids 2 giờ'},
        'renal_adjustment': {'normal': 'Không đổi', '30_60':
        '300mg x 2 lần/ngày', '15_30': '300mg x 1 lần/ngày', 'under_15':
        '300mg cách ngày'},
        'side_effects': ['Buồn ngủ', 'Chóng mặt', 'Mệt mỏi',
        'Phù ngoại biên', 'Tăng cân', 'Nhìn mờ', 'Suy giảm trí nhớ'],
        'interactions': ['Antacids: giảm hấp thu (cách xa 2 giờ)',
        'Morphine: tăng tác dụng an thần', 'Ít tương tác khác'],
        'pregnancy':
        'C', 'mechanism_of_action':
        'Gabapentin là thuốc chống động kinh và giảm đau thần kinh, có cấu trúc tương tự như GABA (gamma-aminobutyric acid) nhưng không gắn trực tiếp vào GABA receptors. Cơ chế chính xác chưa hoàn toàn rõ ràng, nhưng gabapentin gắn vào tiểu đơn vị alpha-2-delta của kênh canxi phụ thuộc điện thế (voltage-gated calcium channels) ở các terminal thần kinh. Điều này làm giảm dòng canxi vào tế bào, giảm phóng thích các chất dẫn truyền thần kinh (glutamate, noradrenaline, substance P) từ các terminal thần kinh. Dẫn đến giảm kích thích quá mức và giảm đau thần kinh. Gabapentin không ảnh hưởng đến GABA receptors, GABA uptake, hoặc GABA transaminase. Gabapentin có tác dụng chống động kinh, giảm đau thần kinh (đặc biệt đau sau zona, đau thần kinh do tiểu đường), và có thể có tác dụng an thần, giảm lo âu. Hấp thu giảm khi tăng liều do cơ chế vận chuyển bão hòa.'
        , 'monitoring': [
        'Đáp ứng điều trị (giảm cơn động kinh, giảm đau thần kinh, giảm lo âu)',
        'Tác dụng phụ thần kinh (buồn ngủ, chóng mặt, mệt mỏi, nhìn mờ, suy giảm trí nhớ) - đặc biệt khi bắt đầu hoặc tăng liều'
        , 'Phù ngoại biên (tay, chân) - có thể nặng',
        'Tăng cân - theo dõi cân nặng',
        'Chức năng thận (creatinine, eGFR) - điều chỉnh liều ở suy thận (quan trọng)'
        , 'Dấu hiệu lệ thuộc, nghiện (hiếm nhưng có thể xảy ra)',
        'Tương tác với antacids (giảm hấp thu), morphine (tăng tác dụng an thần)'
        ],
        'precautions': [
        'Điều chỉnh liều ở suy thận QUAN TRỌNG: CrCl 30-60: 300mg x 2 lần/ngày; CrCl 15-30: 300mg x 1 lần/ngày; CrCl <15: 300mg cách ngày'
        'Hấp thu giảm khi tăng liều do cơ chế vận chuyển bão hòa - không tăng liều quá nhanh'
        , 'Uống cách xa antacids ít nhất 2 giờ (giảm hấp thu)',
        'Tăng liều dần dần để giảm tác dụng phụ (bắt đầu với 300mg x 3 lần/ngày)',
        'Buồn ngủ, chóng mặt, mệt mỏi - phổ biến, thường tự khỏi sau vài tuần, tránh lái xe hoặc vận hành máy móc'
        'Phù ngoại biên - có thể nặng, cần theo dõi, có thể cần giảm liều hoặc ngừng'
        , 'Tăng cân - theo dõi, có thể cần điều chỉnh chế độ ăn',
        'Không ngừng đột ngột - giảm liều dần dần (tăng nguy cơ co giật, hội chứng cai)'
        'Thận trọng ở bệnh nhân có tiền sử lệ thuộc thuốc (có thể gây lệ thuộc, nghiện)'
        , 'Thận trọng với bệnh nhân suy giảm chức năng thận (giảm thải trừ)',
        'Tương tác với morphine - tăng tác dụng an thần, thận trọng khi dùng chung'
        , 'Có thể gây suy giảm trí nhớ, nhìn mờ - thận trọng ở người cao tuổi'],
        'pharmacokinetics': {'half_life':
        '5-7 giờ (bình thường), tăng ở suy thận (tỷ lệ với eGFR)', 'onset':
        'Vài giờ đến vài ngày', 'duration': '8-12 giờ (dùng 3 lần/ngày)',
        'protein_binding': '<3% (không gắn protein)', 'clearance':
        'Thận: bài tiết chủ yếu qua thận (100% nguyên dạng, không chuyển hóa). Không chuyển hóa ở gan. Hấp thu giảm khi tăng liều do cơ chế vận chuyển L-amino acid bão hòa ở ruột. Thời gian bán thải tăng ở suy thận (tỷ lệ với eGFR).'
        },
        'storage':
        'Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm, tránh ánh sáng. Viên nén/capsule: bảo quản trong bao bì kín. Dạng suspension: bảo quản ở nhiệt độ phòng, lắc kỹ trước khi dùng.'
        , 'black_box_warnings':
        'Nguy cơ suy hô hấp nghiêm trọng, có thể gây tử vong, khi dùng với các thuốc ức chế hệ thần kinh trung ương (opioids, benzodiazepines). Nguy cơ tăng ở bệnh nhân có bệnh hô hấp, người cao tuổi. Theo dõi chặt chẽ dấu hiệu suy hô hấp. Nguy cơ tác dụng phụ thần kinh nghiêm trọng (buồn ngủ, chóng mặt, mệt mỏi) có thể ảnh hưởng đến khả năng lái xe và vận hành máy móc.'
        , 'drug_interactions': {'major': [{'drug': 'Morphine, Opioids',
        'mechanism': 'Tăng tác dụng ức chế hệ thần kinh trung ương', 'effect':
        'Tăng nguy cơ suy hô hấp nghiêm trọng, có thể tử vong. Tăng buồn ngủ, chóng mặt.'
        , 'management':
        'Giảm liều opioid hoặc gabapentin. Theo dõi chặt chẽ dấu hiệu suy hô hấp. Cảnh báo bệnh nhân về nguy cơ.'
        }],
        'moderate': [
        {'drug': 'Antacids (aluminum, magnesium)', 'mechanism':
        'Giảm hấp thu gabapentin', 'effect':
        'Giảm nồng độ gabapentin, giảm hiệu quả', 'management':
        'Uống gabapentin cách xa antacids ít nhất 2 giờ.'}, {'drug':
        'Benzodiazepines', 'mechanism':
        'Tăng tác dụng ức chế hệ thần kinh trung ương', 'effect':
        'Tăng buồn ngủ, chóng mặt, suy hô hấp', 'management':
        'Giảm liều một trong hai thuốc. Theo dõi dấu hiệu suy hô hấp.'}, {
        'drug': 'Alcohol', 'mechanism':
        'Tăng tác dụng ức chế hệ thần kinh trung ương', 'effect':
        'Tăng buồn ngủ, chóng mặt, suy hô hấp', 'management':
        'Tránh hoặc giảm rượu. Cảnh báo bệnh nhân.'}],
        'minor': [{'drug':
        'Cimetidine', 'mechanism': 'Giảm nhẹ thải trừ qua thận', 'effect':
        'Tăng nhẹ nồng độ gabapentin', 'management':
        'Không cần điều chỉnh liều thường xuyên, nhưng theo dõi tác dụng phụ.'}
        ]},
        'contraindications': {'tuyệt_đối': [
        'Dị ứng gabapentin hoặc các thành phần khác'],
        'tương_đối': [
        'Suy thận (CrCl <30) - giảm liều đáng kể, tăng khoảng cách liều',
        'Suy thận nặng (CrCl <15) - giảm liều rất nhiều, có thể cách ngày',
        'Bệnh nhân lớn tuổi có suy thận - giảm liều thêm',
        'Mang thai (chứng cứ hạn chế) - chỉ dùng nếu lợi ích > nguy cơ',
        'Tiền sử lệ thuộc thuốc (có thể gây lệ thuộc)',
        'Bệnh hô hấp (COPD, sleep apnea) - tăng nguy cơ suy hô hấp khi dùng với opioids/benzodiazepines'
        ]},contraindications_detail': {'tuyệt_đối': [
        'Dị ứng gabapentin hoặc các thành phần khác'],
        'tương_đối': [
        'Suy thận (CrCl <30) - giảm liều đáng kể, tăng khoảng cách liều',
        'Suy thận nặng (CrCl <15) - giảm liều rất nhiều, có thể cách ngày',
        'Bệnh nhân lớn tuổi có suy thận - giảm liều thêm',
        'Mang thai (chứng cứ hạn chế) - chỉ dùng nếu lợi ích > nguy cơ',
        'Tiền sử lệ thuộc thuốc (có thể gây lệ thuộc)',
        'Bệnh hô hấp (COPD, sleep apnea) - tăng nguy cơ suy hô hấp khi dùng với opioids/benzodiazepines'
        ]},
        'reversal_agents': {'available': False, 'agents': [],
        'notes': 'Không có antidote đặc hiệu. Điều trị quá liều gabapentin chủ yếu là hỗ trợ. Lọc máu có thể hiệu quả (không gắn protein, bài tiết qua thận).'},
        'pregnancy_lactation': {'fda_category': 'C', 'pregnancy_details':
        'Chứng cứ về an toàn trong thai kỳ còn hạn chế. Một số nghiên cứu gợi ý tăng nhẹ nguy cơ dị tật bẩm sinh và kết quả thai kỳ kém, nhưng chứng cứ không rõ ràng. Chỉ dùng nếu lợi ích điều trị vượt trội nguy cơ. Nếu dùng trong thai kỳ, cần tư vấn di truyền và theo dõi chặt chẽ.'
        , 'lactation': {'safety': 'Compatible', 'details':
        'Gabapentin bài tiết vào sữa mẹ ở nồng độ thấp đến trung bình (nồng độ trong sữa mẹ khoảng 30-70% nồng độ trong huyết thanh mẹ). Nồng độ trong máu trẻ sơ sinh rất thấp (<5% nồng độ trong máu mẹ). Tác dụng phụ ở trẻ rất hiếm nhưng có thể có buồn ngủ nhẹ.'
        , 'recommendation':
        'Có thể cho con bú. Theo dõi trẻ về dấu hiệu tác dụng phụ (buồn ngủ, bú kém, chậm tăng cân).'
        }},
        'hepatic_adjustment': {'mild':
        'Không cần điều chỉnh liều (gabapentin không chuyển hóa ở gan)',
        'moderate':
        'Không cần điều chỉnh liều (gabapentin không chuyển hóa ở gan)',
        'severe':
        'Không cần điều chỉnh liều (gabapentin không chuyển hóa ở gan). Tuy nhiên, thận trọng ở bệnh nhân suy gan kèm suy thận.'
        , 'notes':
        'Gabapentin không chuyển hóa ở gan, bài tiết chủ yếu qua thận (100% nguyên dạng). Không cần điều chỉnh liều ở suy gan. Chỉ cần điều chỉnh liều ở suy thận (quan trọng).'
        },
        'overdose_management': {'symptoms': [
        'Triệu chứng thần kinh: buồn ngủ, chóng mặt, lú lẫn, mất điều hòa (ataxia), mệt mỏi'
        'Rối loạn hô hấp: suy hô hấp (hiếm, thường khi dùng với opioids/benzodiazepines)'
        , 'Rối loạn tiêu hóa: buồn nôn, nôn, tiêu chảy',
        'Triệu chứng khác: nhìn mờ, phù ngoại biên'],
        'antidote':
        'Không có antidote đặc hiệu', 'treatment': [
        'Đánh giá đường thở, hô hấp, tuần hoàn. Hỗ trợ hô hấp nếu cần (quan trọng nếu dùng với opioids)'
        , 'Rửa dạ dày nếu trong vòng 1-2 giờ sau uống (nếu bệnh nhân tỉnh táo)',
        'Than hoạt tính: 1g/kg (tối đa 50-100g) nếu trong vòng 1-2 giờ',
        'Theo dõi liên tục: ý thức, hô hấp (quan trọng)',
        'Hỗ trợ hô hấp: thở máy nếu suy hô hấp',
        'Naloxone: nếu có dùng opioids (để đảo ngược suy hô hấp do opioids)',
        'Lọc máu: có thể hiệu quả (không gắn protein, bài tiết qua thận), xem xét ở trường hợp nặng'
        ],
        'monitoring':
        'Theo dõi ý thức, hô hấp (quan trọng), dấu hiệu thần kinh. Có thể đo nồng độ gabapentin trong máu nếu có sẵn.'
        },
        'reversal_agents': None, 'administration_instructions': {'oral': {
        'with_food':
        'Có thể uống với hoặc không có thức ăn. Không ảnh hưởng đến hấp thu đáng kể.'
        , 'timing':
        'Chia liều 3 lần/ngày (sáng, trưa, tối). Uống cùng thời điểm mỗi ngày để duy trì nồng độ ổn định. Không bỏ liều. QUAN TRỌNG: Uống cách xa antacids ít nhất 2 giờ (giảm hấp thu).'
        },
        'iv': {'reconstitution': 'Không có dạng IV', 'infusion_rate': 'N/A',
        'compatibility': [],
        'incompatibility': [],
        }},
        'references': {'primary_sources': ['Lexicomp - Gabapentin',
        'UpToDate - Gabapentin: Drug information',
        'FDA - Neurontin (gabapentin) prescribing information',
        "Goodman & Gilman's The Pharmacological Basis of Therapeutics, 13th ed."
        ],
        'evidence_level':
        'A - Evidence from well-designed randomized controlled trials and systematic reviews'
        },
        'risk_flags': {
            'high_alert': False,
            'narrow_therapeutic_index': False,
            'icu_critical_care_only': False,
            'bleeding_risk': None,
            'organ_toxicity': {'respiratory': 'Black Box Warning (respiratory depression with opioids/benzodiazepines)', 'neurological': 'Suicidal ideation, withdrawal'},qt_prolongation': False,
            'hepatotoxicity': False,
            'nephrotoxicity': False,
            'requires_monitoring': ['Renal function (dose adjustment required)', 'Respiratory depression signs (with opioids/benzodiazepines)', 'Suicidal ideation', 'Withdrawal signs'],look_alike_sound_alike': ['Gabapentin', 'Pregabalin']
        },guideline_tags': [
            'FDA Black Box Warning - Respiratory Depression',
            'AAN Guidelines - Epilepsy Treatment',
            'AAN Guidelines - Neuropathic Pain',
            'ILAE Guidelines - Antiepileptic Drugs'
        ],
        'last_updated': '2025-02-18'
    },
    "Pregabalin": {'group': 'Neurology - Anticonvulsant (Alpha-2-delta ligand)',
        'vietnamese_name': 'Pregabalin, Lyrica', 'administration': ['PO'],
        'indications': [
        'Đau thần kinh (postherpetic neuralgia, diabetic neuropathy)',
        'Đau cơ xơ hóa', 'Động kinh cục bộ', 'Rối loạn lo âu tổng quát'],
        'contraindications': ['Dị ứng'],
        'dosage': {'adult_neuropathic':
        '75mg x 2 lần/ngày, tăng đến 150-300mg x 2 lần/ngày', 'adult_epilepsy':
        '75mg x 2 lần/ngày, tăng đến 150-600mg/ngày', 'adult_max': '600mg/ngày',
        'notes': 'Mạnh hơn gabapentin, hấp thu tốt hơn'},
        'renal_adjustment': {
        'normal': 'Không đổi', '30_60': 'Giảm liều 50%', '15_30':
        'Giảm liều 75%', 'under_15': 'Giảm liều 90%'},
        'side_effects': [
        'Buồn ngủ', 'Chóng mặt', 'Phù ngoại biên', 'Tăng cân', 'Nhìn mờ',
        'Suy giảm trí nhớ', 'Nguy cơ lạm dụng (controlled substance)'],
        'interactions': ['Morphine: tăng tác dụng an thần',
        'Alcohol: tăng tác dụng an thần', 'Ít tương tác khác'],
        'pregnancy':
        'C', 'mechanism_of_action':
        'Pregabalin là thuốc chống động kinh và giảm đau thần kinh, là dẫn xuất của gabapentin nhưng có cấu trúc tối ưu hơn. Pregabalin gắn vào tiểu đơn vị alpha-2-delta của kênh canxi phụ thuộc điện thế (voltage-gated calcium channels) ở các terminal thần kinh, với ái lực cao hơn gabapentin. Điều này làm giảm dòng canxi vào tế bào, giảm phóng thích các chất dẫn truyền thần kinh (glutamate, noradrenaline, substance P, CGRP) từ các terminal thần kinh. Dẫn đến giảm kích thích quá mức và giảm đau thần kinh. Khác với gabapentin, pregabalin có hấp thu tuyến tính (không bão hòa), dược động học dự đoán được, và hiệu quả mạnh hơn. Pregabalin có tác dụng chống động kinh, giảm đau thần kinh (đặc biệt đau sau zona, đau thần kinh do tiểu đường), đau cơ xơ hóa, và rối loạn lo âu. Pregabalin là controlled substance (có nguy cơ lạm dụng, nghiện).'
        , 'monitoring': [
        'Đáp ứng điều trị (giảm cơn động kinh, giảm đau thần kinh, giảm lo âu)',
        'Tác dụng phụ thần kinh (buồn ngủ, chóng mặt, mệt mỏi, nhìn mờ, suy giảm trí nhớ) - đặc biệt khi bắt đầu hoặc tăng liều'
        , 'Phù ngoại biên (tay, chân) - có thể nặng',
        'Tăng cân - theo dõi cân nặng',
        'Chức năng thận (creatinine, eGFR) - điều chỉnh liều ở suy thận (quan trọng)'
        'Dấu hiệu lạm dụng, nghiện - pregabalin là controlled substance (nguy cơ lệ thuộc, nghiện)'
        'Tương tác với morphine (tăng tác dụng an thần), alcohol (tăng tác dụng an thần)'
        ],
        'precautions': [
        'Điều chỉnh liều ở suy thận QUAN TRỌNG: CrCl 30-60: giảm liều 50%; CrCl 15-30: giảm liều 75%; CrCl <15: giảm liều 90%'
        'Nguy cơ lạm dụng, nghiện - pregabalin là controlled substance (Schedule V), có thể gây lệ thuộc, nghiện'
        'Không ngừng đột ngột - giảm liều dần dần trong ít nhất 1 tuần (tăng nguy cơ co giật, hội chứng cai, mất ngủ, lo âu)'
        'Tăng liều dần dần để giảm tác dụng phụ (bắt đầu với 75mg x 2 lần/ngày)',
        'Buồn ngủ, chóng mặt, mệt mỏi - phổ biến, thường tự khỏi sau vài tuần, tránh lái xe hoặc vận hành máy móc'
        'Phù ngoại biên - có thể nặng, cần theo dõi, có thể cần giảm liều hoặc ngừng'
        , 'Tăng cân - theo dõi, có thể cần điều chỉnh chế độ ăn',
        'Thận trọng ở bệnh nhân có tiền sử lạm dụng thuốc, nghiện (nguy cơ cao)',
        'Thận trọng với bệnh nhân suy giảm chức năng thận (giảm thải trừ)',
        'Tương tác với morphine - tăng tác dụng an thần, thận trọng khi dùng chung'
        , 'Tránh rượu - tăng tác dụng an thần, tăng nguy cơ suy hô hấp',
        'Có thể gây suy giảm trí nhớ, nhìn mờ - thận trọng ở người cao tuổi',
        'Hấp thu tốt hơn gabapentin (không bão hòa), hiệu quả mạnh hơn, dùng 2 lần/ngày'
        ],
        'pharmacokinetics': {'half_life':
        '6 giờ (bình thường), tăng ở suy thận (tỷ lệ với eGFR)', 'onset':
        'Vài giờ đến vài ngày', 'duration': '12 giờ (dùng 2 lần/ngày)',
        'protein_binding': '<1% (không gắn protein)', 'clearance':
        'Thận: bài tiết chủ yếu qua thận (90% nguyên dạng, không chuyển hóa). Không chuyển hóa ở gan. Hấp thu tuyến tính (không bão hòa như gabapentin), dự đoán được. Thời gian bán thải tăng ở suy thận (tỷ lệ với eGFR).'
        },
        'storage':
        'Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm, tránh ánh sáng. Viên nén/capsule: bảo quản trong bao bì kín. Controlled substance - cần bảo quản an toàn, tránh tiếp cận không được phép.'
        , 'black_box_warnings':
        'Nguy cơ suy hô hấp nghiêm trọng, có thể gây tử vong, khi dùng với các thuốc ức chế hệ thần kinh trung ương (opioids, benzodiazepines). Nguy cơ tăng ở bệnh nhân có bệnh hô hấp, người cao tuổi. Theo dõi chặt chẽ dấu hiệu suy hô hấp. Nguy cơ lạm dụng, nghiện - pregabalin là controlled substance (Schedule V), có thể gây lệ thuộc, nghiện. Không ngừng đột ngột - tăng nguy cơ co giật, hội chứng cai. Nguy cơ tác dụng phụ thần kinh nghiêm trọng (buồn ngủ, chóng mặt, mệt mỏi) có thể ảnh hưởng đến khả năng lái xe và vận hành máy móc.'
        , 'drug_interactions': {'major': [{'drug': 'Morphine, Opioids',
        'mechanism': 'Tăng tác dụng ức chế hệ thần kinh trung ương', 'effect':
        'Tăng nguy cơ suy hô hấp nghiêm trọng, có thể tử vong. Tăng buồn ngủ, chóng mặt.'
        , 'management':
        'Giảm liều opioid hoặc pregabalin. Theo dõi chặt chẽ dấu hiệu suy hô hấp. Cảnh báo bệnh nhân về nguy cơ.'
        }],
        'moderate': [
        {'drug': 'Benzodiazepines', 'mechanism':
        'Tăng tác dụng ức chế hệ thần kinh trung ương', 'effect':
        'Tăng buồn ngủ, chóng mặt, suy hô hấp', 'management':
        'Giảm liều một trong hai thuốc. Theo dõi dấu hiệu suy hô hấp.'}, {
        'drug': 'Alcohol', 'mechanism':
        'Tăng tác dụng ức chế hệ thần kinh trung ương', 'effect':
        'Tăng buồn ngủ, chóng mặt, suy hô hấp', 'management':
        'Tránh hoặc giảm rượu. Cảnh báo bệnh nhân về nguy cơ nghiêm trọng.'}, {
        'drug': 'Angiotensin-converting enzyme (ACE) inhibitors', 'mechanism':
        'Cả hai đều có thể gây phù ngoại biên', 'effect':
        'Tăng nguy cơ phù ngoại biên', 'management':
        'Theo dõi dấu hiệu phù. Có thể cần giảm liều hoặc ngừng một trong hai thuốc.'
        }],
        'minor': [
        {'drug': 'Benzodiazepines (anxiolytics)', 'mechanism':
        'Tăng nhẹ tác dụng an thần', 'effect': 'Tăng nhẹ buồn ngủ, chóng mặt',
        'management': 'Theo dõi tác dụng phụ. Có thể cần giảm liều.'}]},
        'contraindications': {'tuyệt_đối': [
        'Dị ứng pregabalin hoặc các thành phần khác'],
        'tương_đối': [
        'Suy thận (CrCl <30) - giảm liều đáng kể, tăng khoảng cách liều',
        'Suy thận nặng (CrCl <15) - giảm liều 90%, tăng khoảng cách liều',
        'Bệnh nhân lớn tuổi có suy thận - giảm liều thêm',
        'Mang thai (chứng cứ hạn chế) - chỉ dùng nếu lợi ích > nguy cơ',
        'Tiền sử lạm dụng thuốc, nghiện (nguy cơ cao - pregabalin là controlled substance)'
        'Bệnh hô hấp (COPD, sleep apnea) - tăng nguy cơ suy hô hấp khi dùng với opioids/benzodiazepines'
        , 'Congestive heart failure - tăng nguy cơ phù ngoại biên']},
        'pregnancy_lactation': {'fda_category': 'C', 'pregnancy_details':
        'Chứng cứ về an toàn trong thai kỳ còn hạn chế. Một số nghiên cứu gợi ý tăng nhẹ nguy cơ dị tật bẩm sinh và kết quả thai kỳ kém, nhưng chứng cứ không rõ ràng. Chỉ dùng nếu lợi ích điều trị vượt trội nguy cơ. Nếu dùng trong thai kỳ, cần tư vấn di truyền và theo dõi chặt chẽ.'
        , 'lactation': {'safety': 'Compatible', 'details':
        'Pregabalin bài tiết vào sữa mẹ ở nồng độ thấp đến trung bình (nồng độ trong sữa mẹ khoảng 50-70% nồng độ trong huyết thanh mẹ). Nồng độ trong máu trẻ sơ sinh rất thấp (<5% nồng độ trong máu mẹ). Tác dụng phụ ở trẻ rất hiếm nhưng có thể có buồn ngủ nhẹ.'
        , 'recommendation':
        'Có thể cho con bú. Theo dõi trẻ về dấu hiệu tác dụng phụ (buồn ngủ, bú kém, chậm tăng cân).'
        }},
        'hepatic_adjustment': {'mild':
        'Không cần điều chỉnh liều (pregabalin không chuyển hóa ở gan)',
        'moderate':
        'Không cần điều chỉnh liều (pregabalin không chuyển hóa ở gan)',
        'severe':
        'Không cần điều chỉnh liều (pregabalin không chuyển hóa ở gan). Tuy nhiên, thận trọng ở bệnh nhân suy gan kèm suy thận.'
        , 'notes':
        'Pregabalin không chuyển hóa ở gan, bài tiết chủ yếu qua thận (90% nguyên dạng). Không cần điều chỉnh liều ở suy gan. Chỉ cần điều chỉnh liều ở suy thận (quan trọng).'
        },
        'overdose_management': {'symptoms': [
        'Triệu chứng thần kinh: buồn ngủ, chóng mặt, lú lẫn, mất điều hòa (ataxia), mệt mỏi, hôn mê'
        'Rối loạn hô hấp: suy hô hấp (hiếm, thường khi dùng với opioids/benzodiazepines)'
        , 'Rối loạn tiêu hóa: buồn nôn, nôn, tiêu chảy',
        'Triệu chứng khác: nhìn mờ, phù ngoại biên, co giật (khi ngừng đột ngột)'
        ],
        'treatment': [
        'Đánh giá đường thở, hô hấp, tuần hoàn. Hỗ trợ hô hấp nếu cần (quan trọng nếu dùng với opioids)'
        , 'Rửa dạ dày nếu trong vòng 1-2 giờ sau uống (nếu bệnh nhân tỉnh táo)',
        'Than hoạt tính: 1g/kg (tối đa 50-100g) nếu trong vòng 1-2 giờ',
        'Theo dõi liên tục: ý thức, hô hấp (quan trọng)',
        'Hỗ trợ hô hấp: thở máy nếu suy hô hấp',
        'Naloxone: nếu có dùng opioids (để đảo ngược suy hô hấp do opioids)',
        'Xử trí co giật: benzodiazepine nếu có',
        'Lọc máu: có thể hiệu quả (không gắn protein, bài tiết qua thận), xem xét ở trường hợp nặng'
        ],
        'monitoring':
        'Theo dõi ý thức, hô hấp (quan trọng), dấu hiệu thần kinh. Có thể đo nồng độ pregabalin trong máu nếu có sẵn.'
        },
        'reversal_agents': None, 'administration_instructions': {'oral': {
        'with_food':
        'Có thể uống với hoặc không có thức ăn. Không ảnh hưởng đến hấp thu đáng kể.'
        , 'timing':
        'Chia liều 2-3 lần/ngày (thường 2 lần/ngày). Uống cùng thời điểm mỗi ngày để duy trì nồng độ ổn định. Không bỏ liều. QUAN TRỌNG: Không ngừng đột ngột - giảm liều dần dần trong ít nhất 1 tuần.'
        },
        'iv': {'reconstitution': 'Không có dạng IV', 'infusion_rate': 'N/A',
        'compatibility': [],
        'incompatibility': [],
        }},
        'references': {'primary_sources': ['Lexicomp - Pregabalin',
        'UpToDate - Pregabalin: Drug information',
        'FDA - Lyrica (pregabalin) prescribing information',
        "Goodman & Gilman's The Pharmacological Basis of Therapeutics, 13th ed."
        ],
        'evidence_level':
        'A - Evidence from well-designed randomized controlled trials and systematic reviews'
        },
        'risk_flags': {
            'high_alert': True,
            'narrow_therapeutic_index': False,
            'icu_critical_care_only': False,
            'bleeding_risk': None,
            'organ_toxicity': {'respiratory': 'Black Box Warning (respiratory depression with opioids/benzodiazepines)', 'neurological': 'Suicidal ideation, dependence (controlled substance)'},qt_prolongation': False,
            'hepatotoxicity': False,
            'nephrotoxicity': False,
            'requires_monitoring': ['Renal function (dose adjustment required)', 'Respiratory depression signs (with opioids/benzodiazepines)', 'Suicidal ideation', 'Dependence/abuse signs (controlled substance)', 'Withdrawal signs'],look_alike_sound_alike': ['Pregabalin', 'Gabapentin']
        },guideline_tags': [
            'FDA Black Box Warning - Respiratory Depression',
            'FDA Black Box Warning - Controlled Substance (Schedule V)',
            'AAN Guidelines - Epilepsy Treatment',
            'AAN Guidelines - Neuropathic Pain',
            'ILAE Guidelines - Antiepileptic Drugs'
        ],
        'last_updated': '2025-02-18',
        "reversal_agents": {
             "available": False,
             "agents": []
         },
}}

__all__ = ['ANTICONVULSANT_ALPHA_2_DELTA_LIGANDS_DRUGS']
