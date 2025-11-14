"""Analgesic and Pain Medications
Active module - contains all analgesic drug data"""

# Opioid Agonist (Strong)s

OPIOID_AGONIST_(STRONG)S_DRUGS = {
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
        }}}

__all__ = ['OPIOID_AGONIST_(STRONG)S_DRUGS']
