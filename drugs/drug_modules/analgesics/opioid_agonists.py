"""Analgesic and Pain Medications
Active module - contains all analgesic drug data"""

# Opioid Agonists

OPIOID_AGONISTS_DRUGS = {
    "Tramadol": {'group': 'Analgesic - Opioid Agonist', 'vietnamese_name':
        'Tramadol, Tramal', 'administration': ['PO', 'IV', 'IM'], 'indications':
        ['Đau trung bình đến nặng', 'Đau sau phẫu thuật', 'Đau mạn tính'],
        'contraindications': ['Ngộ độc cấp tính rượu, thuốc an thần, opioid',
        'Dùng MAO inhibitor trong 14 ngày', 'Co giật không kiểm soát',
        'Suy hô hấp nặng'], 'dosage': {'adult_po':
        '50-100mg mỗi 4-6 giờ (tối đa 400mg/ngày)', 'adult_iv_im':
        '50-100mg mỗi 4-6 giờ', 'elderly': 'Liều thấp hơn (25-50mg)', 'notes':
        'Nguy cơ co giật, đặc biệt với SSRI'}, 'side_effects': ['Buồn nôn, nôn',
        'Chóng mặt', 'Buồn ngủ', 'Co giật (đặc biệt với SSRI)',
        'Hội chứng serotonin (với SSRI)', 'Táo bón',
        'Nguy cơ nghiện (thấp hơn opioid mạnh)'], 'interactions': [
        'SSRI/SNRI: tăng nguy cơ co giật và hội chứng serotonin',
        'MAO inhibitor: chống chỉ định', 'Thuốc an thần: tăng tác dụng an thần',
        'Quinidine: tăng nồng độ tramadol'], 'pregnancy': 'C',
        'mechanism_of_action':
        'Opioid tổng hợp, tác dụng kép. Vừa là opioid mu-receptor agonist (yếu hơn morphine) vừa ức chế tái hấp thu serotonin và norepinephrine. Giảm đau thông qua cả hai cơ chế. Độc tính opioid thấp hơn morphine nhưng vẫn có nguy cơ ức chế hô hấp và nghiện. Được dùng trong đau vừa đến nặng. Có nguy cơ co giật, đặc biệt khi dùng liều cao hoặc với các thuốc làm giảm ngưỡng co giật.'
        , 'monitoring': ['Mức độ đau (thang điểm đau)',
        'Nhịp thở và độ bão hòa oxy (SpO2) - nguy cơ ức chế hô hấp',
        'Mức độ ý thức',
        'Co giật (nguy cơ tăng ở liều cao, dùng với SSRI/SNRI, hoặc bệnh nhân có tiền sử co giật)'
        ,
        'Hội chứng serotonin (khi dùng với SSRI/SNRI: kích động, sốt, run, cứng cơ)'
        , 'Dấu hiệu nghiện/lệ thuộc',
        'Chức năng thận (điều chỉnh liều ở suy thận nặng)',
        'Chức năng gan (giảm liều ở suy gan nặng)'], 'precautions': [
        'Nguy cơ co giật - tăng ở: liều cao (>400mg/ngày), dùng với SSRI/SNRI, MAOI, tricyclic antidepressant, bệnh nhân có tiền sử co giật'
        ,
        'KHÔNG dùng với MAOI (nguy cơ hội chứng serotonin nặng, có thể tử vong)',
        'Thận trọng với SSRI/SNRI (nguy cơ hội chứng serotonin và co giật)',
        'Nguy cơ ức chế hô hấp - thấp hơn morphine nhưng vẫn có',
        'Không dùng với rượu, benzodiazepine, thuốc an thần (tăng nguy cơ ức chế hô hấp)'
        ,
        'Nguy cơ nghiện/lệ thuộc - chỉ dùng khi thực sự cần thiết, không dùng kéo dài'
        , 'Giảm liều ở suy thận nặng (CrCl < 30)',
        'Giảm liều ở suy gan nặng (giảm chuyển hóa)',
        'Liều tối đa: 400mg/ngày (để giảm nguy cơ co giật)',
        'Người cao tuổi: giảm liều (tăng nhạy cảm)',
        'Không dùng cho trẻ em < 12 tuổi (nguy cơ ức chế hô hấp)'],
        'pharmacokinetics': {'half_life':
        '6 giờ (tramadol), 7 giờ (active metabolite O-desmethyltramadol)',
        'onset': '1 giờ (PO)', 'duration': '4-6 giờ', 'protein_binding': '20%',
        'metabolism':
        'Gan (CYP2D6, CYP3A4) → active metabolite O-desmethyltramadol',
        'clearance': 'Chủ yếu qua thận, cần điều chỉnh ở suy thận nặng'},
        'storage':
        'Bảo quản ở nhiệt độ phòng (20-25°C), tránh ẩm. Viên nén: tránh ẩm, để xa tầm tay trẻ em.'
        , 'black_box_warnings':
        'Nguy cơ nghiện, lạm dụng, và lệ thuộc - chỉ dùng khi thực sự cần thiết. Nguy cơ ức chế hô hấp nặng có thể dẫn đến tử vong, đặc biệt khi dùng với benzodiazepine, rượu, hoặc thuốc an thần khác. Nguy cơ co giật tăng ở liều cao và khi dùng với SSRI/SNRI. Nguy cơ hội chứng serotonin khi dùng với MAOI hoặc SSRI/SNRI, có thể tử vong.'
        , 'drug_interactions': {'major': [{'drug':
        'MAO inhibitors (phenelzine, tranylcypromine, selegiline)', 'mechanism':
        'Ức chế chuyển hóa serotonin, tăng nguy cơ hội chứng serotonin',
        'effect': 'Hội chứng serotonin nghiêm trọng, có thể tử vong',
        'management':
        'CHỐNG CHỈ ĐỊNH TUYỆT ĐỐI. Ngừng MAOI ít nhất 14 ngày trước khi dùng tramadol'
        }, {'drug':
        'SSRI/SNRI (fluoxetine, sertraline, venlafaxine, duloxetine)',
        'mechanism': 'Tăng nồng độ serotonin, giảm ngưỡng co giật', 'effect':
        'Tăng nguy cơ co giật và hội chứng serotonin', 'management':
        'Tránh dùng hoặc dùng với thận trọng. Giảm liều tramadol. Theo dõi dấu hiệu co giật và hội chứng serotonin'
        }], 'moderate': [{'drug': 'Benzodiazepine, rượu, thuốc an thần',
        'mechanism': 'Tăng ức chế hệ thần kinh trung ương', 'effect':
        'Tăng nguy cơ ức chế hô hấp nặng, có thể tử vong', 'management':
        'Tránh dùng đồng thời. Nếu phải dùng, giảm liều và theo dõi hô hấp chặt chẽ'
        }, {'drug': 'Quinidine, fluoxetine, paroxetine', 'mechanism':
        'Ức chế CYP2D6, giảm chuyển hóa tramadol thành O-desmethyltramadol',
        'effect': 'Giảm hiệu quả giảm đau (do giảm active metabolite)',
        'management':
        'Cân nhắc dùng opioid khác không phụ thuộc CYP2D6 nếu cần'}], 'minor':
        [{'drug': 'Carbamazepine, phenytoin', 'mechanism':
        'Cảm ứng CYP3A4, tăng chuyển hóa tramadol', 'effect':
        'Giảm hiệu quả tramadol', 'management': 'Có thể cần tăng liều tramadol'
        }]}, 'contraindications': {'tuyệt_đối': [
        'Dùng MAO inhibitor trong vòng 14 ngày',
        'Ngộ độc cấp tính rượu, thuốc an thần, opioid',
        'Co giật không kiểm soát', 'Suy hô hấp nặng hoặc suy hô hấp cấp tính',
        'Dị ứng tramadol'], 'tương_đối': [
        'Suy thận nặng (CrCl <30) - giảm liều 50%',
        'Suy gan nặng - giảm liều 50%',
        'Dùng SSRI/SNRI - tăng nguy cơ co giật và hội chứng serotonin',
        'Tiền sử co giật - tăng nguy cơ',
        'Trẻ em <12 tuổi - nguy cơ ức chế hô hấp', 'Người cao tuổi - giảm liều'
        ]}, 'pregnancy_lactation': {'fda_category': 'C', 'pregnancy_details':
        'Có thể dùng nếu lợi ích > nguy cơ. Nguy cơ ức chế hô hấp ở trẻ sơ sinh nếu dùng gần ngày sinh. Có thể gây hội chứng cai ở trẻ sơ sinh nếu dùng kéo dài trong thai kỳ. Tránh dùng trong 3 tháng cuối nếu có thể.'
        , 'lactation': {'safety': 'Caution', 'details':
        'Tramadol và O-desmethyltramadol bài tiết vào sữa mẹ. Nồng độ trong sữa mẹ tương đương khoảng 0.1% liều mẹ. Có thể gây ức chế hô hấp và buồn ngủ ở trẻ bú mẹ.'
        , 'recommendation':
        'Thận trọng khi cho con bú. Nếu dùng, theo dõi trẻ sát (dấu hiệu ức chế hô hấp, buồn ngủ). Tránh dùng liều cao hoặc kéo dài.'
        }}, 'hepatic_adjustment': {'mild': 'Không đổi', 'moderate':
        'Giảm liều 25-50%', 'severe': 'Giảm liều 50% hoặc tránh dùng', 'notes':
        'Tramadol chuyển hóa ở gan qua CYP2D6 và CYP3A4 thành O-desmethyltramadol (active metabolite). Suy gan làm giảm chuyển hóa, tăng nguy cơ tích lũy và tác dụng phụ.'
        }, 'overdose_management': {'symptoms': [
        'Ức chế hô hấp nặng (thở chậm, ngừng thở)', 'Giảm ý thức, hôn mê',
        'Co giật (đặc biệt ở liều cao hoặc với SSRI/SNRI)',
        'Hội chứng serotonin (nếu dùng với SSRI/SNRI: kích động, sốt, run, cứng cơ)'
        , 'Hạ huyết áp', 'Nhịp tim chậm', 'Táo bón nặng'], 'antidote':
        'Naloxone (opioid antagonist) - có thể đảo ngược một phần tác dụng opioid nhưng không đảo ngược co giật hoặc hội chứng serotonin'
        , 'treatment': ['Đảm bảo đường thở, hỗ trợ hô hấp (thở máy nếu cần)',
        'Naloxone: 0.4-2mg IV, có thể lặp lại mỗi 2-3 phút đến khi đáp ứng (tối đa 10mg)'
        ,
        'Nếu co giật: benzodiazepine (diazepam, lorazepam) hoặc phenobarbital',
        'Nếu hội chứng serotonin: cyproheptadine, dantrolene nếu cần',
        'Than hoạt tính nếu uống trong vòng 1-2 giờ (nhưng cần cẩn thận về nguy cơ hôn mê)'
        , 'Truyền dịch, hỗ trợ huyết động nếu hạ huyết áp',
        'Theo dõi liên tục: hô hấp, ý thức, ECG'], 'monitoring':
        'Nhịp thở, SpO2, ý thức, ECG, huyết áp, nhịp tim liên tục. Theo dõi ít nhất 24 giờ do half-life dài của active metabolite (7 giờ)'
        }, 'reversal_agents': {'available': True, 'agents': [{'name':
        'Naloxone', 'indication':
        'Đảo ngược tác dụng opioid (ức chế hô hấp, giảm ý thức)', 'dose':
        '0.4-2mg IV, lặp lại mỗi 2-3 phút đến khi đáp ứng (tối đa 10mg). Có thể dùng IM/SC nếu không có IV'
        , 'notes':
        'Naloxone chỉ đảo ngược tác dụng opioid, KHÔNG đảo ngược co giật hoặc hội chứng serotonin. Half-life ngắn (1 giờ) nên có thể cần truyền liên tục nếu quá liều nặng.'
        }]}, 'administration_instructions': {'oral': {'with_food':
        'Có thể dùng với hoặc không có thức ăn. Uống với thức ăn có thể giảm buồn nôn'
        , 'timing': 'Mỗi 4-6 giờ khi cần. Liều tối đa: 400mg/ngày'}, 'iv': {
        'reconstitution': 'Pha với 50-100ml NS hoặc D5W', 'infusion_rate':
        'Truyền trong 15-30 phút. Hoặc tiêm trực tiếp IV chậm (2-3 phút)',
        'compatibility': ['NS', 'D5W', "Ringer's Lactate"], 'incompatibility':
        [], 'notes':
        'Theo dõi hô hấp chặt chẽ khi dùng IV. Có thể gây co giật ở liều cao.'},
        'im': {'notes': 'Tiêm bắp sâu. Có thể gây đau tại chỗ tiêm.'}},
        'references': {'primary_sources': ['FDA Drug Label - Ultram (tramadol)',
        'UpToDate - Tramadol: Drug information',
        'Lexicomp - Tramadol monograph',
        "Goodman & Gilman's Pharmacological Basis of Therapeutics, 14th ed"],
        'last_updated': '2025-01-06', 'evidence_level':
        'High - FDA-approved, extensive clinical data'}},
    "Hydrocodone": {'group': 'Analgesic - Opioid Agonist',
        'vietnamese_name': 'Hydrocodone, Vicodin (với acetaminophen)',
        'administration': ['PO'], 'indications': [
        'Đau trung bình đến nặng',
        'Ho (dạng syrup, liều thấp)'], 'contraindications': [
        'Ngộ độc cấp tính rượu, thuốc an thần, opioid',
        'Suy hô hấp nặng', 'Tắc ruột', 'Dị ứng'], 'dosage': {
        'adult_pain': '5-10mg mỗi 4-6 giờ (thường kết hợp với acetaminophen)',
        'adult_max': '60mg/ngày', 'adult_cough':
        '5mg mỗi 4-6 giờ (dạng syrup)', 'notes':
        'Opioid yếu đến trung bình. Thường dùng kết hợp với acetaminophen (Vicodin) hoặc ibuprofen. Có tác dụng giảm ho ở liều thấp.'
        }, 'renal_adjustment': {'normal': 'Không đổi', '30_60': 'Thận trọng',
        'under_30': 'Giảm liều 25-50%'}, 'side_effects': [
        'Buồn nôn, nôn', 'Chóng mặt', 'Buồn ngủ', 'Táo bón',
        'Ức chế hô hấp (liều cao)', 'Nguy cơ nghiện/lệ thuộc',
        'Ngộ độc gan (nếu dùng với acetaminophen liều cao)'], 'interactions': [
        'Thuốc an thần: tăng tác dụng an thần và ức chế hô hấp',
        'MAO inhibitor: tăng nguy cơ phản ứng nghiêm trọng',
        'CYP2D6 inhibitors: giảm chuyển hóa thành hydromorphone (active metabolite)'
        ], 'pregnancy': 'C', 'mechanism_of_action':
        'Opioid mu-receptor agonist, tác dụng yếu đến trung bình (mạnh hơn codeine nhưng yếu hơn morphine). Hydrocodone được chuyển hóa qua CYP2D6 thành hydromorphone (active metabolite mạnh hơn). Giảm đau thông qua kích thích opioid receptors ở não và tủy sống. Cũng có tác dụng giảm ho ở liều thấp. Thường dùng kết hợp với acetaminophen (Vicodin) hoặc ibuprofen để tăng hiệu quả và giảm liều opioid. Nguy cơ nghiện/lệ thuộc, đặc biệt khi dùng kéo dài.'
        , 'monitoring': [
        'Mức độ đau (thang điểm đau)',
        'Nhịp thở và độ bão hòa oxy (SpO2) - nguy cơ ức chế hô hấp',
        'Mức độ ý thức',
        'Dấu hiệu nghiện/lệ thuộc',
        'Chức năng gan (nếu dùng với acetaminophen)',
        'Chức năng thận (điều chỉnh liều ở suy thận nặng)'], 'precautions': [
        'Nguy cơ ức chế hô hấp - đặc biệt ở liều cao, người cao tuổi, suy hô hấp',
        'Nguy cơ nghiện/lệ thuộc - chỉ dùng khi thực sự cần thiết, không dùng kéo dài'
        ,
        'Không dùng với rượu, benzodiazepine, thuốc an thần (tăng nguy cơ ức chế hô hấp)'
        ,
        'Ngộ độc gan - nếu dùng với acetaminophen, không vượt quá 4g acetaminophen/ngày'
        , 'Giảm liều ở suy thận nặng (CrCl < 30)',
        'Giảm liều ở suy gan nặng (giảm chuyển hóa)',
        'Người cao tuổi: giảm liều (tăng nhạy cảm)',
        'Không dùng cho trẻ em < 12 tuổi (nguy cơ ức chế hô hấp)',
        'Thận trọng với CYP2D6 poor metabolizers (giảm hiệu quả)'], 'pharmacokinetics': {
        'half_life': '3.8 giờ (hydrocodone), 2.6 giờ (hydromorphone metabolite)',
        'onset': '30-60 phút (PO)', 'duration': '4-6 giờ', 'protein_binding':
        '36%', 'metabolism':
        'Gan (CYP2D6 → hydromorphone active metabolite, CYP3A4 → norhydrocodone), thận (thải trừ)'
        }, 'storage':
        'Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm, tránh ánh sáng. Bảo quản an toàn, tránh xa tầm tay trẻ em (nguy cơ ngộ độc).'
        , 'black_box_warnings':
        'Nguy cơ nghiện, lệ thuộc, và lạm dụng. Có thể gây ức chế hô hấp nghiêm trọng, đặc biệt ở liều cao hoặc khi dùng với thuốc an thần. Ngộ độc gan có thể xảy ra nếu dùng với acetaminophen liều cao (>4g/ngày).'
        , 'drug_interactions': {'major': [{'drug':
        'Thuốc an thần (benzodiazepine, rượu, barbiturates)', 'mechanism':
        'Tác dụng hiệp đồng ức chế CNS', 'effect':
        'Tăng ức chế hô hấp nghiêm trọng, có thể tử vong', 'management':
        'TRÁNH DÙNG chung. Nếu phải dùng, giảm liều cả hai và theo dõi chặt chẽ hô hấp.'
        }, {'drug': 'MAO inhibitors', 'mechanism':
        'Tăng giải phóng serotonin và catecholamine', 'effect':
        'Nguy cơ phản ứng nghiêm trọng (tăng huyết áp, hội chứng serotonin)', 'management':
        'TRÁNH DÙNG với MAO inhibitor.'}], 'moderate': [{'drug':
        'CYP2D6 inhibitors (paroxetine, fluoxetine, quinidine)', 'mechanism':
        'Ức chế chuyển hóa hydrocodone thành hydromorphone', 'effect':
        'Giảm hiệu quả giảm đau (giảm active metabolite)', 'management':
        'Có thể cần tăng liều hydrocodone hoặc dùng opioid khác không phụ thuộc CYP2D6.'
        }, {'drug': 'CYP3A4 inhibitors (ketoconazole, clarithromycin)',
        'mechanism': 'Ức chế chuyển hóa hydrocodone', 'effect':
        'Tăng nồng độ hydrocodone, tăng tác dụng phụ', 'management':
        'Giảm liều hydrocodone. Theo dõi tác dụng phụ.'}], 'minor': []},
        'contraindications': {'tuyệt_đối': [
        'Dị ứng hydrocodone hoặc opioid',
        'Ngộ độc cấp tính rượu, thuốc an thần, opioid',
        'Suy hô hấp nặng',
        'Tắc ruột',
        'Dùng với MAO inhibitor'], 'tương_đối': [
        'Suy hô hấp nhẹ đến trung bình - thận trọng, giảm liều',
        'Suy thận nặng (CrCl <30) - giảm liều 25-50%',
        'Suy gan nặng - giảm liều, thận trọng',
        'Người cao tuổi - giảm liều (tăng nhạy cảm)',
        'CYP2D6 poor metabolizers - giảm hiệu quả',
        'Mang thai (category C) - thận trọng, có thể gây withdrawal ở trẻ sơ sinh'
        ]}, 'pregnancy_lactation': {'fda_category': 'C', 'pregnancy_details':
        'Category C. Có thể dùng khi cần thiết nhưng thận trọng. Có thể gây withdrawal ở trẻ sơ sinh nếu dùng gần cuối thai kỳ.'
        , 'lactation': {'safety': 'Compatible with monitoring', 'details':
        'Hydrocodone bài tiết vào sữa mẹ ở nồng độ thấp. Có thể gây tác dụng phụ ở trẻ (buồn ngủ, bú kém).'
        , 'recommendation':
        'Có thể cho con bú nhưng cần theo dõi trẻ về dấu hiệu tác dụng phụ (buồn ngủ, bú kém, ức chế hô hấp).'
        }}, 'hepatic_adjustment': {'mild': 'Không đổi', 'moderate':
        'Thận trọng, giảm liều 25-50%', 'severe':
        'Giảm liều 50%, thận trọng', 'notes':
        'Hydrocodone chuyển hóa ở gan qua CYP2D6 và CYP3A4. Suy gan làm giảm chuyển hóa, tăng nguy cơ tích lũy và tác dụng phụ.'
        }, 'overdose_management': {'symptoms': [
        'Ức chế hô hấp nặng (triệu chứng chính, có thể tử vong)',
        'Buồn ngủ sâu, hôn mê', 'Đồng tử co nhỏ (miosis)',
        'Hạ huyết áp, nhịp tim chậm', 'Táo bón nặng',
        'Ngộ độc gan (nếu dùng với acetaminophen liều cao)'], 'antidote':
        'Naloxone (Narcan) - opioid antagonist, đảo ngược ức chế hô hấp', 'treatment': [
        'Đánh giá đường thở, hô hấp, tuần hoàn. Hỗ trợ hô hấp ngay lập tức (quan trọng nhất)'
        ,
        'Naloxone: 0.4-2mg IV/IM/SC, có thể lặp lại mỗi 2-3 phút nếu cần (tối đa 10mg)'
        ,
        'Theo dõi liên tục: ý thức, hô hấp (nhịp thở, SpO2), tim mạch',
        'Hỗ trợ hô hấp: thở máy nếu suy hô hấp nặng',
        'Điều trị hạ huyết áp: truyền dịch, vasopressors nếu cần',
        'Nếu có ngộ độc acetaminophen: điều trị với N-acetylcysteine (NAC)',
        'Theo dõi ít nhất 4-6 giờ sau liều naloxone cuối (do half-life naloxone ngắn hơn hydrocodone)'
        ], 'monitoring':
        'Theo dõi liên tục: ý thức, hô hấp (nhịp thở, SpO2), tim mạch (huyết áp, nhịp tim), nhiệt độ cơ thể. Theo dõi ít nhất 4-6 giờ sau liều naloxone cuối.'
        }, 'reversal_agents': {'available': True, 'agents': [{'agent':
        'Naloxone (Narcan)', 'mechanism':
        'Opioid antagonist, đảo ngược tác dụng opioid', 'indication':
        'Quá liều opioid gây ức chế hô hấp', 'dose':
        '0.4-2mg IV/IM/SC, có thể lặp lại mỗi 2-3 phút nếu cần (tối đa 10mg)',
        'caution':
        'Half-life ngắn (30-90 phút) nên có thể cần lặp lại. Theo dõi ít nhất 4-6 giờ sau liều cuối.'
        }], 'notes':
        'Naloxone là antidote đặc hiệu cho quá liều opioid. Đảo ngược ức chế hô hấp nhanh chóng. Tuy nhiên, half-life ngắn nên có thể cần lặp lại.'
        }, 'administration_instructions': {'oral': {'with_food':
        'Có thể uống với thức ăn hoặc không (hấp thu tốt)', 'timing':
        'Mỗi 4-6 giờ. Thường dùng kết hợp với acetaminophen (Vicodin) hoặc ibuprofen. Liều tối đa: 60mg/ngày.'
        }, 'iv': {'reconstitution': 'Không có dạng IV', 'infusion_rate': 'N/A',
        'compatibility': [], 'incompatibility': [], 'notes': 'Chỉ có dạng uống'}},
        'references': {'primary_sources': [
        'FDA Drug Label - Vicodin (Hydrocodone/Acetaminophen)',
        'UpToDate - Hydrocodone: Drug information'], 'last_updated': '2025-02-05',
        'evidence_level': 'High - FDA approved'}}}

__all__ = ['OPIOID_AGONISTS_DRUGS']
