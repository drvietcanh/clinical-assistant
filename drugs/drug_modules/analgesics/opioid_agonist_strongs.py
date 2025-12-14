"""Analgesic and Pain Medications
Active module - contains all analgesic drug data"""

# Opioid Agonist (Strong)s

OPIOID_AGONIST_STRONGS_DRUGS = {
    "Morphine": {'group': 'Analgesic - Opioid Agonist (Strong)', 'vietnamese_name':
        'Morphine', 'administration': ['PO', 'IV', 'IM', 'SC'], 'indications':
        ['Đau nặng (ung thư, sau phẫu thuật)', 'Đau cấp tính nặng',
        'Đau mạn tính nặng', 'Khó thở do suy tim', 'Cơn đau do hồi sức'],
        'contraindications': ['Ngộ độc cấp tính rượu, thuốc an thần, opioid',
        'Suy hô hấp nặng', 'Hen phế quản nặng', 'Tắc ruột cơ học',
        'Tăng áp lực nội sọ', 'Suy gan nặng'], 'dosage': {'adult_po_immediate':
        '10-30mg mỗi 4 giờ khi cần', 'adult_po_extended':
        '15-30mg x 2 lần/ngày (MS Contin)', 'adult_iv':
        '2.5-5mg IV mỗi 3-4 giờ hoặc 0.8-10mg/giờ truyền liên tục',
        'adult_im_sc': '5-15mg mỗi 4 giờ', 'elderly': 'Giảm liều 25-50%',
        'notes': 'Thuốc chuẩn vàng cho đau nặng. Theo dõi hô hấp chặt chẽ'},
        'renal_adjustment': {'normal': 'Không đổi', '30_60': 'Giảm liều 25-50%',
        'under_30': 'Giảm liều 50-75%, tăng khoảng cách liều'}, 'side_effects':
        ['Ức chế hô hấp (nguy hiểm)', 'Buồn nôn, nôn',
        'Táo bón (rất thường gặp)', 'Ngứa', 'Buồn ngủ, lú lẫn',
        'Co đồng tử (miosis)', 'Hạ huyết áp', 'Ức chế tiết ADH (SIADH)',
        'Nguy cơ nghiện, lệ thuộc'], 'interactions': [
        'Thuốc an thần/Benzodiazepine: tăng nguy cơ ức chế hô hấp',
        'MAO inhibitor: nguy hiểm - tránh dùng',
        'Rượu: tăng nguy cơ ức chế hô hấp', 'Cimetidine: tăng nồng độ morphine'
        ], 'pregnancy':
        'C - D trong 3 tháng cuối (gây hội chứng cai ở trẻ sơ sinh)',
        'mechanism_of_action':
        'Opioid mu-receptor agonist mạnh. Gắn với mu-opioid receptors trong hệ thần kinh trung ương và ngoại vi, kích hoạt tín hiệu G-protein, dẫn đến giảm dẫn truyền đau, giảm nhận thức đau, an thần, và ức chế hô hấp. Tăng ngưỡng đau, giảm đáp ứng cảm xúc với đau. Tác động lên brainstem → giảm trung tâm hô hấp. Tác động lên đường tiêu hóa → giảm nhu động ruột, tăng trương lực cơ thắt.'
        , 'monitoring': [
        'Nhịp thở và độ bão hòa oxy (SpO2) liên tục - quan trọng nhất',
        'Mức độ đau (thang điểm đau)',
        'Mức độ ý thức (dấu hiệu quá liều: giảm ý thức, thở chậm)',
        'Huyết áp và nhịp tim (có thể gây hạ huyết áp, nhịp tim chậm)',
        'Co đồng tử (miosis) - dấu hiệu đặc trưng của opioid',
        'Dấu hiệu táo bón (rất thường gặp, cần dự phòng)',
        'Dấu hiệu nghiện/lệ thuộc (nếu dùng kéo dài)',
        'Chức năng thận (tích lũy ở suy thận do tích tụ active metabolite)'],
        'precautions': [
        'Nguy cơ ức chế hô hấp NẶNG - đặc biệt ở liều đầu tiên, người cao tuổi, suy thận, suy gan'
        , 'Khởi đầu với liều thấp, tăng dần theo đáp ứng',
        'Cần có naloxone sẵn sàng để đảo ngược nếu quá liều',
        'Tránh dùng với benzodiazepine, rượu, thuốc an thần (tăng nguy cơ ức chế hô hấp nặng)'
        , 'Dự phòng táo bón từ đầu (dùng thuốc nhuận tràng)',
        'Thận trọng ở suy thận (tích lũy active metabolite morphine-6-glucuronide - có thể gây ức chế hô hấp kéo dài)'
        , 'Thận trọng ở suy gan (giảm chuyển hóa)',
        'Nguy cơ nghiện/lệ thuộc nếu dùng kéo dài - cần đánh giá định kỳ',
        'Không dùng trong tăng áp lực nội sọ (tăng CO2 → tăng áp lực nội sọ)',
        'Không dùng trong tắc ruột cơ học (tăng trương lực cơ thắt)'],
        'pharmacokinetics': {'half_life': '2-4 giờ', 'onset':
        'IV: 5-10 phút; IM: 15-30 phút; PO: 30-60 phút', 'duration':
        '3-7 giờ (IV), 4-7 giờ (IM), 3-6 giờ (PO)', 'protein_binding': '20-35%',
        'clearance':
        'Chủ yếu qua thận (morphine-6-glucuronide tích lũy ở suy thận)'},
        'storage':
        'Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm, tránh ánh sáng. Để xa tầm tay trẻ em (nguy cơ quá liều).'
        , 'black_box_warnings':
        'Nguy cơ nghiện, lạm dụng, và lệ thuộc - chỉ dùng khi thực sự cần thiết. Nguy cơ ức chế hô hấp nặng có thể dẫn đến tử vong, đặc biệt khi dùng với benzodiazepine hoặc rượu. Morphine có thể gây hội chứng cai ở trẻ sơ sinh nếu dùng trong 3 tháng cuối thai kỳ.'
        , 'drug_interactions': {'major': [{'drug':
        'Benzodiazepine, thuốc an thần, rượu', 'mechanism':
        'Tăng ức chế hệ thần kinh trung ương, đặc biệt trung tâm hô hấp',
        'effect': 'Tăng nguy cơ ức chế hô hấp nặng, có thể tử vong',
        'management':
        'TRÁNH DÙNG ĐỒNG THỜI. Nếu phải dùng, giảm liều morphine, theo dõi hô hấp liên tục, có naloxone sẵn sàng'
        }, {'drug': 'MAO inhibitors', 'mechanism':
        'Tăng nguy cơ phản ứng tương tác nghiêm trọng', 'effect':
        'Có thể gây hội chứng serotonin, tăng huyết áp, nguy hiểm tính mạng',
        'management':
        'CHỐNG CHỈ ĐỊNH. Ngừng MAOI ít nhất 14 ngày trước khi dùng morphine'}],
        'moderate': [{'drug': 'Cimetidine', 'mechanism':
        'Ức chế chuyển hóa morphine qua gan', 'effect':
        'Tăng nồng độ morphine, tăng nguy cơ ức chế hô hấp', 'management':
        'Giảm liều morphine 25-50%. Theo dõi hô hấp chặt chẽ'}, {'drug':
        'Rifampin', 'mechanism': 'Cảm ứng enzyme chuyển hóa morphine', 'effect':
        'Giảm hiệu quả morphine', 'management': 'Có thể cần tăng liều morphine'
        }, {'drug': 'Phenothiazine, haloperidol', 'mechanism':
        'Tăng ức chế hệ thần kinh trung ương', 'effect':
        'Tăng nguy cơ ức chế hô hấp, hạ huyết áp', 'management':
        'Thận trọng. Giảm liều morphine, theo dõi hô hấp'}], 'minor': []},
        'contraindications': {'tuyệt_đối': ['Dị ứng morphine hoặc opioid',
        'Ngộ độc cấp tính rượu, thuốc an thần, opioid',
        'Suy hô hấp nặng hoặc suy hô hấp cấp tính',
        'Hen phế quản nặng không kiểm soát', 'Tắc ruột cơ học',
        'Tăng áp lực nội sọ (do tăng CO2)',
        'Dùng MAO inhibitor trong vòng 14 ngày'], 'tương_đối': [
        'Suy thận nặng (CrCl <30) - giảm liều 50-75%, tăng khoảng cách liều (tích lũy morphine-6-glucuronide)'
        , 'Suy gan nặng - giảm liều 25-50% (giảm chuyển hóa)',
        'Người cao tuổi - giảm liều 25-50% (tăng nhạy cảm)',
        'Trẻ em <12 tuổi - nguy cơ ức chế hô hấp',
        'Tiền sử nghiện/lạm dụng chất - nguy cơ tái nghiện',
        'Suy tim - tăng nguy cơ ức chế hô hấp',
        'Bệnh phổi tắc nghẽn mạn tính (COPD) - tăng nguy cơ ức chế hô hấp']},
        'pregnancy_lactation': {'fda_category': 'C - D trong tam cá nguyệt 3',
        'pregnancy_details':
        'Tam cá nguyệt 1-2: Có thể dùng nếu lợi ích > nguy cơ cho điều trị đau nặng. Tam cá nguyệt 3: Nguy cơ hội chứng cai ở trẻ sơ sinh nếu dùng kéo dài. Nguy cơ ức chế hô hấp ở trẻ sơ sinh nếu dùng gần ngày sinh. Tránh dùng kéo dài trong 3 tháng cuối nếu có thể.'
        , 'lactation': {'safety': 'Caution', 'details':
        'Morphine bài tiết vào sữa mẹ ở nồng độ thấp. Nồng độ trong sữa mẹ tương đương khoảng 0.8-3% liều mẹ. Có thể gây ức chế hô hấp và buồn ngủ ở trẻ bú mẹ, đặc biệt ở trẻ sơ sinh.'
        , 'recommendation':
        'Thận trọng khi cho con bú. Nếu dùng, theo dõi trẻ sát (dấu hiệu ức chế hô hấp, buồn ngủ, bú kém). Tránh dùng liều cao hoặc kéo dài. Dùng liều thấp nhất hiệu quả.'
        }}, 'hepatic_adjustment': {'mild': 'Không đổi', 'moderate':
        'Giảm liều 25-50%', 'severe': 'Giảm liều 50% hoặc tránh dùng', 'notes':
        'Morphine chuyển hóa ở gan qua glucuronidation thành morphine-6-glucuronide (active, mạnh hơn morphine) và morphine-3-glucuronide (inactive). Suy gan làm giảm chuyển hóa, tăng nguy cơ tích lũy.'
        }, 'overdose_management': {'symptoms': [
        'Ức chế hô hấp nặng (thở chậm <12 lần/phút, ngừng thở)',
        'Giảm ý thức, hôn mê', 'Co đồng tử (miosis) - dấu hiệu đặc trưng',
        'Hạ huyết áp', 'Nhịp tim chậm', 'Táo bón nặng',
        'Co giật (hiếm, ở trẻ em hoặc liều rất cao)'], 'antidote':
        'Naloxone (opioid antagonist) - đảo ngược tác dụng opioid', 'treatment':
        ['Đảm bảo đường thở, hỗ trợ hô hấp (thở máy nếu cần) - QUAN TRỌNG NHẤT',
        'Naloxone: 0.4-2mg IV, lặp lại mỗi 2-3 phút đến khi đáp ứng (tối đa 10mg)',
        'Nếu không có IV: 0.4-2mg IM/SC, có thể lặp lại',
        'Nếu quá liều nặng: có thể cần truyền naloxone liên tục (0.4-0.8mg/giờ) do half-life ngắn (1 giờ) so với morphine (2-4 giờ)'
        ,
        'Theo dõi hô hấp liên tục ít nhất 24 giờ (do half-life dài của morphine-6-glucuronide)'
        , 'Hỗ trợ huyết động: truyền dịch, vasopressor nếu hạ huyết áp',
        'Than hoạt tính nếu uống trong vòng 1-2 giờ (nhưng cần cẩn thận về nguy cơ hôn mê)'
        , 'Theo dõi ECG, huyết áp, nhịp tim liên tục'], 'monitoring':
        'Nhịp thở, SpO2, ý thức, ECG, huyết áp, nhịp tim liên tục. Theo dõi ít nhất 24 giờ do half-life dài của active metabolite morphine-6-glucuronide'
        }, 'reversal_agents': {'available': True, 'agents': [{'name':
        'Naloxone', 'indication':
        'Đảo ngược tác dụng opioid (ức chế hô hấp, giảm ý thức, hạ huyết áp)',
        'dose':
        '0.4-2mg IV, lặp lại mỗi 2-3 phút đến khi đáp ứng (tối đa 10mg). IM/SC: 0.4-2mg nếu không có IV. Truyền liên tục: 0.4-0.8mg/giờ nếu quá liều nặng'
        , 'notes':
        'Naloxone có half-life ngắn (1 giờ) so với morphine (2-4 giờ) và morphine-6-glucuronide (dài hơn). Có thể cần truyền liên tục hoặc lặp lại liều để tránh tái phát ức chế hô hấp.'
        }]}, 'administration_instructions': {'oral': {'with_food':
        'Có thể dùng với hoặc không có thức ăn. Uống với thức ăn có thể giảm buồn nôn'
        , 'timing':
        'Mỗi 4 giờ khi cần (immediate release) hoặc 2 lần/ngày (extended release MS Contin)'
        }, 'iv': {'reconstitution':
        'Pha với 50-100ml NS hoặc D5W cho truyền liên tục. Hoặc tiêm trực tiếp IV',
        'infusion_rate':
        'Tiêm IV chậm trong 2-5 phút. Truyền liên tục: 0.8-10mg/giờ (tùy liều)',
        'compatibility': ['NS', 'D5W', "Ringer's Lactate"], 'incompatibility':
        ['Alkaline solutions'], 'notes':
        'Theo dõi hô hấp chặt chẽ khi dùng IV. Cần có naloxone sẵn sàng. Khởi đầu với liều thấp, tăng dần.'
        }, 'im': {'notes':
        'Tiêm bắp sâu. Có thể gây đau tại chỗ tiêm. Tác dụng bắt đầu 15-30 phút.'
        }, 'sc': {'notes':
        'Tiêm dưới da. Có thể gây kích ứng tại chỗ. Tác dụng bắt đầu 15-30 phút.'
        }}, 'references': {'primary_sources': [
        'FDA Drug Label - Morphine sulfate',
        'UpToDate - Morphine: Drug information',
        'Lexicomp - Morphine monograph',
        "Goodman & Gilman's Pharmacological Basis of Therapeutics, 14th ed"],
        'last_updated': '2025-01-06', 'evidence_level':
        'High - FDA-approved, extensive clinical data, gold standard for severe pain'
        }},
    
    "Fentanyl": {
        "group": "Analgesic - Opioid Agonist (Strong)",
        "vietnamese_name": "Fentanyl, Duragesic",
        "administration": ["IV", "IM", "Transdermal", "Intranasal", "Buccal"],
        "indications": [
            "Đau nặng (ung thư, sau phẫu thuật)",
            "Đau mạn tính nặng (transdermal patch)",
            "Gây mê (IV)",
            "Đau cấp tính nặng (IV, intranasal, buccal)"
        ],
        "contraindications": [
            "Ngộ độc cấp tính rượu, thuốc an thần, opioid",
            "Suy hô hấp nặng",
            "Hen phế quản nặng",
            "Tắc ruột cơ học",
            "Tăng áp lực nội sọ",
            "Không dùng transdermal ở bệnh nhân chưa dùng opioid (chưa dung nạp)"
        ],
        "dosage": {
            "adult_iv_bolus": "25-100mcg IV mỗi 30-60 phút khi cần",
            "adult_iv_continuous": "25-100mcg/giờ truyền liên tục",
            "adult_transdermal": "25-100mcg/giờ patch, thay mỗi 72 giờ",
            "adult_intranasal": "100-200mcg xịt mũi khi cần",
            "adult_buccal": "100-400mcg ngậm trong miệng khi cần",
            "elderly": "Giảm liều 25-50%",
            "notes": "Mạnh gấp 50-100 lần morphine. Tác dụng nhanh nhưng ngắn (IV). Transdermal: tác dụng chậm, kéo dài."
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "Giảm liều 25-50%",
            "under_30": "Giảm liều 50-75%, tăng khoảng cách liều"
        },
        "side_effects": [
            "Ức chế hô hấp nặng (nguy hiểm, đặc biệt với transdermal patch)",
            "Buồn nôn, nôn",
            "Táo bón",
            "Ngứa",
            "Buồn ngủ, lú lẫn",
            "Co đồng tử (miosis)",
            "Hạ huyết áp",
            "Rigid chest (co cứng ngực - với IV liều cao)",
            "Nguy cơ nghiện, lệ thuộc"
        ],
        "interactions": [
            "Thuốc an thần/Benzodiazepine: tăng nguy cơ ức chế hô hấp nặng",
            "MAO inhibitor: nguy hiểm - tránh dùng",
            "Rượu: tăng nguy cơ ức chế hô hấp",
            "CYP3A4 inhibitors: tăng nồng độ fentanyl"
        ],
        "pregnancy": "C - D trong 3 tháng cuối",
        "mechanism_of_action": "Fentanyl là opioid mu-receptor agonist mạnh, mạnh gấp 50-100 lần morphine. Gắn với mu-opioid receptors trong hệ thần kinh trung ương và ngoại vi, kích hoạt tín hiệu G-protein, dẫn đến giảm dẫn truyền đau, giảm nhận thức đau, an thần, và ức chế hô hấp. Fentanyl có tác dụng nhanh (IV: 1-2 phút), ngắn (30-60 phút IV), nhưng có thể tích lũy ở mô mỡ. Transdermal patch: hấp thu chậm qua da, tác dụng kéo dài 72 giờ, nhưng có thể tích lũy và gây ức chế hô hấp kéo dài sau khi tháo patch.",
        "monitoring": [
            "Nhịp thở và độ bão hòa oxy (SpO2) liên tục - QUAN TRỌNG NHẤT, đặc biệt với transdermal patch",
            "Mức độ đau (thang điểm đau)",
            "Mức độ ý thức (dấu hiệu quá liều: giảm ý thức, thở chậm)",
            "Huyết áp và nhịp tim (có thể gây hạ huyết áp, nhịp tim chậm)",
            "Co đồng tử (miosis)",
            "Dấu hiệu rigid chest (co cứng ngực) với IV liều cao",
            "Với transdermal patch: theo dõi ít nhất 24 giờ sau khi tháo patch (có thể tích lũy)",
            "Chức năng thận (tích lũy ở suy thận)"
        ],
        "precautions": [
            "Nguy cơ ức chế hô hấp NẶNG - đặc biệt với transdermal patch (tích lũy, tác dụng kéo dài)",
            "KHÔNG dùng transdermal patch cho bệnh nhân chưa dùng opioid (chưa dung nạp) - nguy cơ ức chế hô hấp nặng",
            "Với transdermal patch: theo dõi ít nhất 24 giờ sau khi tháo patch (có thể tích lũy trong mô mỡ)",
            "Khởi đầu với liều thấp, tăng dần theo đáp ứng",
            "Cần có naloxone sẵn sàng để đảo ngược nếu quá liều",
            "Tránh dùng với benzodiazepine, rượu, thuốc an thần (tăng nguy cơ ức chế hô hấp nặng)",
            "Dự phòng táo bón từ đầu",
            "Thận trọng ở suy thận (tích lũy)",
            "Thận trọng ở suy gan (giảm chuyển hóa)",
            "Nguy cơ nghiện/lệ thuộc nếu dùng kéo dài",
            "Với IV liều cao: có thể gây rigid chest (co cứng ngực) - cần dùng muscle relaxant"
        ],
        "pharmacokinetics": {
            "half_life": "IV: 2-4 giờ; Transdermal: 17 giờ (sau khi tháo patch)",
            "onset": "IV: 1-2 phút; IM: 7-15 phút; Transdermal: 12-24 giờ; Intranasal: 5-10 phút; Buccal: 15-30 phút",
            "duration": "IV: 30-60 phút; Transdermal: 72 giờ (patch); Intranasal: 1-2 giờ; Buccal: 2-4 giờ",
            "protein_binding": "80-85%",
            "metabolism": "Gan (CYP3A4) - chuyển hóa thành norfentanyl (inactive)",
            "clearance": "Gan (chuyển hóa), thận (thải trừ). Tích lũy ở mô mỡ (đặc biệt với transdermal patch)."
        },
        "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm, tránh ánh sáng. Transdermal patch: bảo quản trong bao bì kín, tránh nhiệt độ cao. Để xa tầm tay trẻ em (nguy cơ quá liều nghiêm trọng).",
        "black_box_warnings": "Nguy cơ nghiện, lạm dụng, và lệ thuộc - chỉ dùng khi thực sự cần thiết. Nguy cơ ức chế hô hấp nặng có thể dẫn đến tử vong, đặc biệt với transdermal patch (tích lũy, tác dụng kéo dài sau khi tháo patch). KHÔNG dùng transdermal patch cho bệnh nhân chưa dùng opioid. Fentanyl có thể gây hội chứng cai ở trẻ sơ sinh nếu dùng trong 3 tháng cuối thai kỳ.",
        "drug_interactions": {
            "major": [
                {
                    "drug": "Benzodiazepine, thuốc an thần, rượu",
                    "mechanism": "Tăng ức chế hệ thần kinh trung ương, đặc biệt trung tâm hô hấp",
                    "effect": "Tăng nguy cơ ức chế hô hấp nặng, có thể tử vong",
                    "management": "TRÁNH DÙNG ĐỒNG THỜI. Nếu phải dùng, giảm liều fentanyl, theo dõi hô hấp liên tục, có naloxone sẵn sàng"
                },
                {
                    "drug": "MAO inhibitors",
                    "mechanism": "Tăng nguy cơ phản ứng tương tác nghiêm trọng",
                    "effect": "Có thể gây hội chứng serotonin, tăng huyết áp, nguy hiểm tính mạng",
                    "management": "CHỐNG CHỈ ĐỊNH. Ngừng MAOI ít nhất 14 ngày trước khi dùng fentanyl"
                },
                {
                    "drug": "CYP3A4 inhibitors (ketoconazole, itraconazole, ritonavir, clarithromycin, erythromycin)",
                    "mechanism": "Ức chế chuyển hóa fentanyl qua CYP3A4, tăng nồng độ fentanyl",
                    "effect": "Tăng nồng độ fentanyl, tăng nguy cơ ức chế hô hấp nặng",
                    "management": "Giảm liều fentanyl 50-75%. Theo dõi hô hấp chặt chẽ. Đặc biệt nguy hiểm với transdermal patch."
                }
            ],
            "moderate": [
                {
                    "drug": "CYP3A4 inducers (rifampin, carbamazepine, phenytoin)",
                    "mechanism": "Cảm ứng enzyme chuyển hóa fentanyl, giảm nồng độ",
                    "effect": "Giảm hiệu quả fentanyl",
                    "management": "Có thể cần tăng liều fentanyl"
                }
            ],
            "minor": []
        },
        "contraindications": {
            "tuyệt_đối": [
                "Dị ứng fentanyl hoặc opioid",
                "Ngộ độc cấp tính rượu, thuốc an thần, opioid",
                "Suy hô hấp nặng hoặc suy hô hấp cấp tính",
                "Hen phế quản nặng không kiểm soát",
                "Tắc ruột cơ học",
                "Tăng áp lực nội sọ (do tăng CO2)",
                "Dùng MAO inhibitor trong vòng 14 ngày",
                "Transdermal patch: bệnh nhân chưa dùng opioid (chưa dung nạp)"
            ],
            "tương_đối": [
                "Suy thận nặng (CrCl <30) - giảm liều 50-75%, tăng khoảng cách liều",
                "Suy gan nặng - giảm liều 25-50% (giảm chuyển hóa)",
                "Người cao tuổi - giảm liều 25-50% (tăng nhạy cảm)",
                "Trẻ em <12 tuổi - nguy cơ ức chế hô hấp",
                "Tiền sử nghiện/lạm dụng chất - nguy cơ tái nghiện",
                "Suy tim - tăng nguy cơ ức chế hô hấp",
                "Bệnh phổi tắc nghẽn mạn tính (COPD) - tăng nguy cơ ức chế hô hấp",
                "Dùng với CYP3A4 inhibitors - tăng nguy cơ ức chế hô hấp"
            ]
        },
        "pregnancy_lactation": {
            "fda_category": "C - D trong tam cá nguyệt 3",
            "pregnancy_details": "Tam cá nguyệt 1-2: Có thể dùng nếu lợi ích > nguy cơ cho điều trị đau nặng. Tam cá nguyệt 3: Nguy cơ hội chứng cai ở trẻ sơ sinh nếu dùng kéo dài. Nguy cơ ức chế hô hấp ở trẻ sơ sinh nếu dùng gần ngày sinh. Tránh dùng kéo dài trong 3 tháng cuối nếu có thể.",
            "lactation": {
                "safety": "Caution",
                "details": "Fentanyl bài tiết vào sữa mẹ ở nồng độ thấp. Có thể gây ức chế hô hấp và buồn ngủ ở trẻ bú mẹ, đặc biệt ở trẻ sơ sinh. Với transdermal patch: nồng độ trong sữa mẹ thấp hơn so với IV.",
                "recommendation": "Thận trọng khi cho con bú. Nếu dùng, theo dõi trẻ sát (dấu hiệu ức chế hô hấp, buồn ngủ, bú kém). Tránh dùng liều cao hoặc kéo dài. Dùng liều thấp nhất hiệu quả."
            }
        },
        "hepatic_adjustment": {
            "mild": "Không đổi",
            "moderate": "Giảm liều 25-50%",
            "severe": "Giảm liều 50% hoặc tránh dùng",
            "notes": "Fentanyl chuyển hóa ở gan qua CYP3A4 thành norfentanyl (inactive). Suy gan làm giảm chuyển hóa, tăng nguy cơ tích lũy."
        },
        "overdose_management": {
            "symptoms": [
                "Ức chế hô hấp nặng (thở chậm <12 lần/phút, ngừng thở)",
                "Giảm ý thức, hôn mê",
                "Co đồng tử (miosis)",
                "Hạ huyết áp",
                "Nhịp tim chậm",
                "Rigid chest (co cứng ngực) với IV liều cao",
                "Với transdermal patch: có thể xảy ra sau khi tháo patch (tích lũy)"
            ],
            "antidote": "Naloxone (opioid antagonist) - đảo ngược tác dụng opioid",
            "treatment": [
                "Đảm bảo đường thở, hỗ trợ hô hấp (thở máy nếu cần) - QUAN TRỌNG NHẤT",
                "Naloxone: 0.4-2mg IV, lặp lại mỗi 2-3 phút đến khi đáp ứng (tối đa 10mg)",
                "Nếu không có IV: 0.4-2mg IM/SC, có thể lặp lại",
                "Nếu quá liều nặng: có thể cần truyền naloxone liên tục (0.4-0.8mg/giờ) do half-life ngắn (1 giờ) so với fentanyl",
                "Với transdermal patch: THÁO NGAY patch, rửa da bằng nước và xà phòng",
                "Theo dõi hô hấp liên tục ít nhất 24 giờ (đặc biệt với transdermal patch do tích lũy)",
                "Hỗ trợ huyết động: truyền dịch, vasopressor nếu hạ huyết áp",
                "Nếu rigid chest: có thể cần muscle relaxant (succinylcholine)"
            ],
            "monitoring": "Nhịp thở, SpO2, ý thức, ECG, huyết áp, nhịp tim liên tục. Với transdermal patch: theo dõi ít nhất 24-48 giờ sau khi tháo patch do tích lũy."
        },
        "reversal_agents": {
            "available": True,
            "agents": [
                {
                    "name": "Naloxone",
                    "indication": "Đảo ngược tác dụng opioid (ức chế hô hấp, giảm ý thức, hạ huyết áp)",
                    "dose": "0.4-2mg IV, lặp lại mỗi 2-3 phút đến khi đáp ứng (tối đa 10mg). IM/SC: 0.4-2mg nếu không có IV. Truyền liên tục: 0.4-0.8mg/giờ nếu quá liều nặng",
                    "notes": "Naloxone có half-life ngắn (1 giờ) so với fentanyl (2-4 giờ IV, 17 giờ transdermal). Có thể cần truyền liên tục hoặc lặp lại liều để tránh tái phát ức chế hô hấp, đặc biệt với transdermal patch."
                }
            ]
        },
        "administration_instructions": {
            "oral": None,
            "iv": {
                "reconstitution": "Pha với 50-100ml NS hoặc D5W cho truyền liên tục. Hoặc tiêm trực tiếp IV",
                "infusion_rate": "Tiêm IV chậm trong 2-5 phút. Truyền liên tục: 25-100mcg/giờ (tùy liều)",
                "compatibility": ["NS", "D5W", "Ringer's Lactate"],
                "incompatibility": ["Alkaline solutions"],
                "notes": "Theo dõi hô hấp chặt chẽ khi dùng IV. Cần có naloxone sẵn sàng. Khởi đầu với liều thấp, tăng dần. Với liều cao: có thể gây rigid chest (co cứng ngực) - cần dùng muscle relaxant."
            },
            "im": {
                "notes": "Tiêm bắp sâu. Có thể gây đau tại chỗ tiêm. Tác dụng bắt đầu 7-15 phút."
            },
            "transdermal": {
                "technique": "Dán patch lên da sạch, khô, không có lông (ngực, lưng, cánh tay trên). Thay patch mỗi 72 giờ. Không cắt patch.",
                "timing": "Thay patch mỗi 72 giờ. Tác dụng bắt đầu sau 12-24 giờ. Theo dõi ít nhất 24 giờ sau khi tháo patch.",
                "after_use": "THÁO NGAY nếu có dấu hiệu quá liều. Rửa da bằng nước và xà phòng sau khi tháo patch.",
                "notes": "KHÔNG dùng cho bệnh nhân chưa dùng opioid. Tác dụng kéo dài sau khi tháo patch (tích lũy trong mô mỡ)."
            },
            "intranasal": {
                "technique": "Xịt vào một bên mũi, nhắm mắt và miệng khi xịt.",
                "timing": "Khi cần, có thể lặp lại sau 2 giờ nếu cần.",
                "notes": "Tác dụng nhanh (5-10 phút). Có thể gây vị đắng trong miệng."
            },
            "buccal": {
                "technique": "Đặt viên/băng dán trong miệng, giữa má và nướu. Để tan tự nhiên, không nhai hoặc nuốt.",
                "timing": "Khi cần, có thể lặp lại sau 4 giờ nếu cần.",
                "notes": "Tác dụng bắt đầu 15-30 phút, kéo dài 2-4 giờ."
            }
        },
        "references": {
            "primary_sources": [
                "FDA Drug Label - Fentanyl (Duragesic, Actiq, etc.)",
                "UpToDate - Fentanyl: Drug information",
                "Lexicomp - Fentanyl monograph",
                "Goodman & Gilman's Pharmacological Basis of Therapeutics, 14th ed"
            ],
            "last_updated": "2025-02-05",
            "evidence_level": "High - FDA-approved, extensive clinical data, widely used in anesthesia and pain management"
        }
    },
    "Oxycodone": {
        "group": "Analgesic - Opioid Agonist (Strong)",
        "vietnamese_name": "Oxycodone, OxyContin, Roxicodone",
        "administration": ["PO", "IV"],
        "indications": [
            "Đau nặng (ung thư, sau phẫu thuật)",
            "Đau cấp tính nặng",
            "Đau mạn tính nặng"
        ],
        "contraindications": [
            "Ngộ độc cấp tính rượu, thuốc an thần, opioid",
            "Suy hô hấp nặng",
            "Hen phế quản nặng",
            "Tắc ruột cơ học",
            "Tăng áp lực nội sọ"
        ],
        "dosage": {
            "adult_po_immediate": "5-15mg mỗi 4-6 giờ khi cần",
            "adult_po_extended": "10-20mg x 2 lần/ngày (OxyContin)",
            "adult_iv": "0.03-0.1mg/kg mỗi 3-4 giờ",
            "opioid_naive": "5mg PO mỗi 4-6 giờ",
            "opioid_tolerant": "Liều cao hơn, dựa trên liều opioid trước đó",
            "notes": "Mạnh hơn morphine khi uống (tỷ lệ 1.5:1). Theo dõi hô hấp chặt chẽ."
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "Giảm liều 25-50%",
            "under_30": "Giảm liều 50-75%, tăng khoảng cách liều"
        },
        "side_effects": [
            "Ức chế hô hấp (nguy hiểm)",
            "Buồn nôn, nôn",
            "Táo bón (rất thường gặp)",
            "Ngứa",
            "Buồn ngủ, lú lẫn",
            "Co đồng tử (miosis)",
            "Hạ huyết áp",
            "Nguy cơ nghiện, lệ thuộc"
        ],
        "interactions": [
            "Thuốc an thần/Benzodiazepine: tăng nguy cơ ức chế hô hấp",
            "MAO inhibitor: nguy hiểm - tránh dùng",
            "Rượu: tăng nguy cơ ức chế hô hấp"
        ],
        "pregnancy": "C - D trong 3 tháng cuối",
        "mechanism_of_action": "Opioid mu-receptor agonist mạnh. Tương tự morphine nhưng có sinh khả dụng uống tốt hơn (60-87% so với 20-30% của morphine). Gắn với mu-opioid receptors trong hệ thần kinh trung ương và ngoại vi, kích hoạt tín hiệu G-protein, dẫn đến giảm dẫn truyền đau, giảm nhận thức đau, an thần, và ức chế hô hấp. Oxycodone mạnh hơn morphine khi uống (tỷ lệ 1.5:1) do sinh khả dụng tốt hơn.",
        "monitoring": [
            "Nhịp thở và độ bão hòa oxy (SpO2) liên tục - quan trọng nhất",
            "Mức độ đau (thang điểm đau)",
            "Mức độ ý thức (dấu hiệu quá liều: giảm ý thức, thở chậm)",
            "Huyết áp và nhịp tim",
            "Co đồng tử (miosis)",
            "Dấu hiệu táo bón (rất thường gặp, cần dự phòng)",
            "Dấu hiệu nghiện/lệ thuộc (nếu dùng kéo dài)"
        ],
        "precautions": [
            "Nguy cơ ức chế hô hấp NẶNG - đặc biệt ở liều đầu tiên, người cao tuổi",
            "Khởi đầu với liều thấp, tăng dần theo đáp ứng",
            "Cần có naloxone sẵn sàng để đảo ngược nếu quá liều",
            "Tránh dùng với benzodiazepine, rượu, thuốc an thần",
            "Dự phòng táo bón từ đầu",
            "Nguy cơ nghiện/lệ thuộc nếu dùng kéo dài",
            "Oxycodone có nguy cơ lạm dụng cao - cần theo dõi chặt chẽ"
        ],
        "pharmacokinetics": {
            "half_life": "3-5 giờ",
            "onset": "PO: 15-30 phút; IV: 5-10 phút",
            "duration": "3-6 giờ (immediate release), 12 giờ (extended release)",
            "protein_binding": "38-45%",
            "clearance": "Gan (chuyển hóa qua CYP3A4, CYP2D6), thận (thải trừ)"
        },
        "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm, tránh ánh sáng. Để xa tầm tay trẻ em.",
        "black_box_warnings": "Nguy cơ nghiện, lạm dụng, và lệ thuộc - chỉ dùng khi thực sự cần thiết. Nguy cơ ức chế hô hấp nặng có thể dẫn đến tử vong. Oxycodone có nguy cơ lạm dụng cao - cần theo dõi chặt chẽ.",
        "drug_interactions": {
            "major": [
                {
                    "drug": "Benzodiazepine, thuốc an thần, rượu",
                    "mechanism": "Tăng ức chế hệ thần kinh trung ương",
                    "effect": "Tăng nguy cơ ức chế hô hấp nặng, có thể tử vong",
                    "management": "TRÁNH DÙNG ĐỒNG THỜI. Nếu phải dùng, giảm liều oxycodone, theo dõi hô hấp liên tục."
                }
            ],
            "moderate": [],
            "minor": []
        },
        "contraindications": {
            "tuyệt_đối": [
                "Dị ứng oxycodone hoặc opioid",
                "Ngộ độc cấp tính rượu, thuốc an thần, opioid",
                "Suy hô hấp nặng",
                "Hen phế quản nặng không kiểm soát",
                "Tắc ruột cơ học",
                "Tăng áp lực nội sọ"
            ],
            "tương_đối": [
                "Suy thận nặng - giảm liều 50-75%",
                "Suy gan nặng - giảm liều 25-50%",
                "Người cao tuổi - giảm liều 25-50%",
                "Tiền sử nghiện/lạm dụng chất - nguy cơ tái nghiện"
            ]
        },
        "pregnancy_lactation": {
            "fda_category": "C - D trong tam cá nguyệt 3",
            "pregnancy_details": "Nguy cơ hội chứng cai ở trẻ sơ sinh nếu dùng trong 3 tháng cuối. Tránh dùng kéo dài trong 3 tháng cuối nếu có thể.",
            "lactation": {
                "safety": "Caution",
                "details": "Oxycodone bài tiết vào sữa mẹ. Có thể gây ức chế hô hấp và buồn ngủ ở trẻ bú mẹ.",
                "recommendation": "Thận trọng khi dùng khi cho con bú. Theo dõi trẻ sát."
            }
        },
        "hepatic_adjustment": {
            "mild": "Không cần điều chỉnh liều",
            "moderate": "Giảm liều 25-50%",
            "severe": "Tránh dùng hoặc dùng liều rất thấp",
            "notes": "Oxycodone chuyển hóa ở gan qua CYP3A4 và CYP2D6. Suy gan làm giảm chuyển hóa, tăng nguy cơ tích lũy."
        },
        "overdose_management": {
            "symptoms": [
                "Ức chế hô hấp nặng (thở chậm, ngừng thở)",
                "Giảm ý thức, hôn mê",
                "Co đồng tử (miosis)",
                "Hạ huyết áp",
                "Nhịp tim chậm"
            ],
            "antidote": "Naloxone (opioid antagonist)",
            "treatment": [
                "Đánh giá đường thở, hô hấp, tuần hoàn. Hỗ trợ hô hấp NGAY LẬP TỨC",
                "Naloxone: 0.4-2mg IV/IM/SC, có thể lặp lại mỗi 2-3 phút nếu cần",
                "Theo dõi liên tục hô hấp, ý thức, huyết áp",
                "Hỗ trợ hô hấp: thở máy nếu suy hô hấp",
                "Điều trị hạ huyết áp: truyền dịch, vận mạch nếu cần"
            ],
            "monitoring": "Theo dõi liên tục hô hấp, ý thức, huyết áp, nhịp tim"
        },
        "reversal_agents": {
            "available": True,
            "agents": ["Naloxone"]
        },
        "administration_instructions": {
            "oral": {
                "with_food": "Có thể uống với hoặc không thức ăn. Uống với thức ăn có thể giảm buồn nôn nhẹ.",
                "timing": "Immediate release: mỗi 4-6 giờ khi cần. Extended release: x 2 lần/ngày. KHÔNG nghiền hoặc nhai extended release tablets."
            },
            "iv": {
                "infusion_rate": "Truyền chậm: 2-5 phút",
                "compatibility": ["0.9% NaCl", "D5W"],
                "notes": "Theo dõi hô hấp chặt chẽ trong khi truyền."
            }
        },
        "references": {
            "primary_sources": [
                "FDA Drug Label - Oxycodone (OxyContin, Roxicodone)",
                "UpToDate - Oxycodone: Drug information",
                "Lexicomp - Oxycodone monograph"
            ],
            "last_updated": "2025-02-05",
            "evidence_level": "High - FDA-approved, extensive clinical data"
        }
    },
    "Hydromorphone": {
        "group": "Analgesic - Opioid Agonist (Strong)",
        "vietnamese_name": "Hydromorphone, Dilaudid",
        "administration": ["PO", "IV", "IM", "SC"],
        "indications": [
            "Đau nặng (ung thư, sau phẫu thuật)",
            "Đau cấp tính nặng",
            "Đau mạn tính nặng"
        ],
        "contraindications": [
            "Ngộ độc cấp tính rượu, thuốc an thần, opioid",
            "Suy hô hấp nặng",
            "Hen phế quản nặng",
            "Tắc ruột cơ học",
            "Tăng áp lực nội sọ"
        ],
        "dosage": {
            "adult_po": "2-4mg mỗi 4-6 giờ khi cần",
            "adult_iv": "0.5-2mg mỗi 3-4 giờ hoặc 0.2-1mg/giờ truyền liên tục",
            "adult_im_sc": "1-2mg mỗi 4-6 giờ",
            "opioid_naive": "1-2mg PO hoặc 0.5mg IV",
            "opioid_tolerant": "Liều cao hơn, dựa trên liều opioid trước đó",
            "notes": "Mạnh hơn morphine (tỷ lệ 5:1). Theo dõi hô hấp chặt chẽ."
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "Giảm liều 25-50%",
            "under_30": "Giảm liều 50-75%, tăng khoảng cách liều"
        },
        "side_effects": [
            "Ức chế hô hấp (nguy hiểm)",
            "Buồn nôn, nôn",
            "Táo bón (rất thường gặp)",
            "Ngứa",
            "Buồn ngủ, lú lẫn",
            "Co đồng tử (miosis)",
            "Hạ huyết áp",
            "Nguy cơ nghiện, lệ thuộc"
        ],
        "interactions": [
            "Thuốc an thần/Benzodiazepine: tăng nguy cơ ức chế hô hấp",
            "MAO inhibitor: nguy hiểm - tránh dùng",
            "Rượu: tăng nguy cơ ức chế hô hấp"
        ],
        "pregnancy": "C - D trong 3 tháng cuối",
        "mechanism_of_action": "Opioid mu-receptor agonist mạnh. Hydromorphone là dẫn xuất của morphine, mạnh hơn morphine khoảng 5 lần (tỷ lệ 5:1). Gắn với mu-opioid receptors trong hệ thần kinh trung ương và ngoại vi, kích hoạt tín hiệu G-protein, dẫn đến giảm dẫn truyền đau, giảm nhận thức đau, an thần, và ức chế hô hấp. Hydromorphone có thời gian tác dụng ngắn hơn morphine một chút.",
        "monitoring": [
            "Nhịp thở và độ bão hòa oxy (SpO2) liên tục - quan trọng nhất",
            "Mức độ đau (thang điểm đau)",
            "Mức độ ý thức (dấu hiệu quá liều: giảm ý thức, thở chậm)",
            "Huyết áp và nhịp tim",
            "Co đồng tử (miosis)",
            "Dấu hiệu táo bón (rất thường gặp, cần dự phòng)",
            "Dấu hiệu nghiện/lệ thuộc (nếu dùng kéo dài)"
        ],
        "precautions": [
            "Nguy cơ ức chế hô hấp NẶNG - đặc biệt ở liều đầu tiên, người cao tuổi",
            "Khởi đầu với liều thấp, tăng dần theo đáp ứng",
            "Cần có naloxone sẵn sàng để đảo ngược nếu quá liều",
            "Tránh dùng với benzodiazepine, rượu, thuốc an thần",
            "Dự phòng táo bón từ đầu",
            "Nguy cơ nghiện/lệ thuộc nếu dùng kéo dài",
            "Hydromorphone mạnh hơn morphine 5 lần - cần điều chỉnh liều cẩn thận"
        ],
        "pharmacokinetics": {
            "half_life": "2-3 giờ",
            "onset": "IV: 5-10 phút; IM: 15-30 phút; PO: 30-60 phút",
            "duration": "3-4 giờ",
            "protein_binding": "8-19%",
            "clearance": "Gan (chuyển hóa), thận (thải trừ)"
        },
        "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm, tránh ánh sáng. Để xa tầm tay trẻ em.",
        "black_box_warnings": "Nguy cơ nghiện, lạm dụng, và lệ thuộc - chỉ dùng khi thực sự cần thiết. Nguy cơ ức chế hô hấp nặng có thể dẫn đến tử vong.",
        "drug_interactions": {
            "major": [
                {
                    "drug": "Benzodiazepine, thuốc an thần, rượu",
                    "mechanism": "Tăng ức chế hệ thần kinh trung ương",
                    "effect": "Tăng nguy cơ ức chế hô hấp nặng, có thể tử vong",
                    "management": "TRÁNH DÙNG ĐỒNG THỜI. Nếu phải dùng, giảm liều hydromorphone, theo dõi hô hấp liên tục."
                }
            ],
            "moderate": [],
            "minor": []
        },
        "contraindications": {
            "tuyệt_đối": [
                "Dị ứng hydromorphone hoặc opioid",
                "Ngộ độc cấp tính rượu, thuốc an thần, opioid",
                "Suy hô hấp nặng",
                "Hen phế quản nặng không kiểm soát",
                "Tắc ruột cơ học",
                "Tăng áp lực nội sọ"
            ],
            "tương_đối": [
                "Suy thận nặng - giảm liều 50-75%",
                "Suy gan nặng - giảm liều 25-50%",
                "Người cao tuổi - giảm liều 25-50%",
                "Tiền sử nghiện/lạm dụng chất - nguy cơ tái nghiện"
            ]
        },
        "pregnancy_lactation": {
            "fda_category": "C - D trong tam cá nguyệt 3",
            "pregnancy_details": "Nguy cơ hội chứng cai ở trẻ sơ sinh nếu dùng trong 3 tháng cuối. Tránh dùng kéo dài trong 3 tháng cuối nếu có thể.",
            "lactation": {
                "safety": "Caution",
                "details": "Hydromorphone bài tiết vào sữa mẹ. Có thể gây ức chế hô hấp và buồn ngủ ở trẻ bú mẹ.",
                "recommendation": "Thận trọng khi dùng khi cho con bú. Theo dõi trẻ sát."
            }
        },
        "hepatic_adjustment": {
            "mild": "Không cần điều chỉnh liều",
            "moderate": "Giảm liều 25-50%",
            "severe": "Tránh dùng hoặc dùng liều rất thấp",
            "notes": "Hydromorphone chuyển hóa ở gan. Suy gan làm giảm chuyển hóa, tăng nguy cơ tích lũy."
        },
        "overdose_management": {
            "symptoms": [
                "Ức chế hô hấp nặng (thở chậm, ngừng thở)",
                "Giảm ý thức, hôn mê",
                "Co đồng tử (miosis)",
                "Hạ huyết áp",
                "Nhịp tim chậm"
            ],
            "antidote": "Naloxone (opioid antagonist)",
            "treatment": [
                "Đánh giá đường thở, hô hấp, tuần hoàn. Hỗ trợ hô hấp NGAY LẬP TỨC",
                "Naloxone: 0.4-2mg IV/IM/SC, có thể lặp lại mỗi 2-3 phút nếu cần",
                "Theo dõi liên tục hô hấp, ý thức, huyết áp",
                "Hỗ trợ hô hấp: thở máy nếu suy hô hấp",
                "Điều trị hạ huyết áp: truyền dịch, vận mạch nếu cần"
            ],
            "monitoring": "Theo dõi liên tục hô hấp, ý thức, huyết áp, nhịp tim"
        },
        "reversal_agents": {
            "available": True,
            "agents": ["Naloxone"]
        },
        "administration_instructions": {
            "oral": {
                "with_food": "Có thể uống với hoặc không thức ăn. Uống với thức ăn có thể giảm buồn nôn nhẹ.",
                "timing": "Mỗi 4-6 giờ khi cần."
            },
            "iv": {
                "infusion_rate": "Truyền chậm: 2-5 phút",
                "compatibility": ["0.9% NaCl", "D5W"],
                "notes": "Theo dõi hô hấp chặt chẽ trong khi truyền."
            }
        },
        "references": {
            "primary_sources": [
                "FDA Drug Label - Hydromorphone (Dilaudid)",
                "UpToDate - Hydromorphone: Drug information",
                "Lexicomp - Hydromorphone monograph"
            ],
            "last_updated": "2025-02-05",
            "evidence_level": "High - FDA-approved, extensive clinical data"
        }
    }
}

__all__ = ['OPIOID_AGONIST_STRONGS_DRUGS']
