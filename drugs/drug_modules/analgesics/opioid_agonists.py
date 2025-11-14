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
        'High - FDA-approved, extensive clinical data'}}}

__all__ = ['OPIOID_AGONISTS_DRUGS']
