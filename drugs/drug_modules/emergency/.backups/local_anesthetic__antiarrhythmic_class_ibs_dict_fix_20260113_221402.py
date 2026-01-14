"""Emergency and ACLS Medications
Active module - contains all emergency and ACLS drug data"""

# Local Anesthetic / Antiarrhythmic (Class IB)s

LOCAL_ANESTHETIC_ANTIARRHYTHMIC_CLASS_IB_DRUGS = {
    "Lidocaine": {'group': 'Emergency - Local Anesthetic / Antiarrhythmic (Class IB)',
        'vietnamese_name': 'Lidocaine, Xylocaine', 'administration': ['IV',
        'IO', 'IT'],
        'indications': [
        'Rung thất / Nhịp nhanh thất không có mạch (khi không có amiodarone)',
        'Rối loạn nhịp thất', 'Gây tê tại chỗ', 'Gây tê vùng'],
        'contraindications': ['Dị ứng lidocaine',
        'Block nhĩ thất độ 2-3 (không có máy tạo nhịp)',
        'Hội chứng Adams-Stokes', 'Rối loạn nhịp nặng'],
        'dosage': {
        'adult_cardiac_arrest':
        '1-1.5mg/kg IV bolus, lặp lại 0.5-0.75mg/kg mỗi 5-10 phút (tối đa 3mg/kg)',
        'adult_vt_with_pulse':
        '1-1.5mg/kg IV bolus, sau đó 1-4mg/phút IV infusion',
        'pediatric_arrest': '1mg/kg IV/IO bolus', 'pediatric_infusion':
        '20-50mcg/kg/phút IV', 'notes':
        'Giảm liều ở suy tim, suy gan, người già. Theo dõi co giật, độc thần kinh'
        },
        'renal_adjustment': {'normal': 'Không đổi', '30_60': 'Không đổi',
        'under_30': 'Không đổi'},
        'side_effects': [
        'Độc thần kinh trung ương (co giật, lú lẫn, ngừng thở - với liều cao)',
        'Rối loạn nhịp tim', 'Hạ huyết áp', 'Phản ứng dị ứng (hiếm)'],
        'interactions': ['Beta-blockers: giảm chuyển hóa lidocaine',
        'Cimetidine: tăng nồng độ lidocaine', 'Phenytoin: tăng độc tính'],pregnancy': 'B - An toàn', 'mechanism_of_action':
        'Thuốc gây tê tại chỗ nhóm amide và thuốc chống loạn nhịp class IB. Ức chế kênh natri voltage-gated trong màng tế bào thần kinh và tế bào cơ tim, ngăn cản khử cực và dẫn truyền xung động thần kinh. Ở tim: ức chế dẫn truyền trong các tế bào có thời gian khử cực dài (tâm thất), giảm tự động tính, giảm nguy cơ rối loạn nhịp thất. Tác dụng nhanh, thời gian bán thải ngắn. Được dùng trong gây tê tại chỗ, giảm đau tại chỗ, và điều trị rối loạn nhịp thất.'
        , 'monitoring': ['ECG liên tục (theo dõi rối loạn nhịp)',
        'Huyết áp và nhịp tim',
        'Dấu hiệu độc tính thần kinh trung ương (chóng mặt, ù tai, co giật, mất ý thức) - dấu hiệu đầu tiên của quá liều'
        'Dấu hiệu độc tính tim mạch (block nhĩ thất, nhịp tim chậm, rung thất) - dấu hiệu muộn, nguy hiểm'
        , 'Nồng độ lidocaine trong máu (nếu dùng kéo dài hoặc liều cao)',
        'Chức năng gan (lidocaine chuyển hóa mạnh ở gan)',
        'Dấu hiệu phản ứng dị ứng (hiếm)'],
        'precautions': [
        'Độc tính thần kinh trung ương là dấu hiệu CẢNH BÁO SỚM - ngừng ngay nếu có chóng mặt, ù tai, co giật'
        'Độc tính tim mạch có thể xảy ra sau độc tính thần kinh - nguy hiểm tính mạng'
        'PHẢI điều chỉnh liều ở suy gan (giảm chuyển hóa → tích lũy → độc tính)',
        'Thận trọng ở suy tim (giảm phân bố → tăng nồng độ)',
        'Không dùng ở block nhĩ thất độ 2-3 hoặc block nhánh nếu không có máy tạo nhịp'
        'Liều gây tê tại chỗ: tuân thủ liều tối đa (không quá 4.5mg/kg không có epinephrine, 7mg/kg có epinephrine)'
        , 'Tiêm IV chậm (không quá 25-50mg/phút) để tránh độc tính',
        'Cần có sẵn thuốc chống co giật (benzodiazepine) và thiết bị hồi sức',
        'Giảm liều ở người cao tuổi (giảm chuyển hóa)'],
        'pharmacokinetics': {
        'half_life': '1.5-2 giờ (bình thường), 3-5 giờ (suy gan)', 'onset':
        'Ngay lập tức (IV), 2-5 phút (gây tê tại chỗ)', 'duration':
        '10-20 phút (IV), 1-3 giờ (gây tê tại chỗ)', 'protein_binding':
        '60-80%', 'metabolism':
        'Gan (CYP3A4, CYP1A2) - chuyển hóa mạnh thành active metabolites',
        'clearance': 'Chủ yếu qua gan, cần điều chỉnh ở suy gan'},storage':
        'Bảo quản ở nhiệt độ phòng (15-30°C), tránh ánh sáng. Dung dịch: tránh đông lạnh.'
        , 'black_box_warnings':
        'Không có black box warning. Tuy nhiên, độc tính tim mạch có thể gây block nhĩ thất, rung thất, và tử vong, đặc biệt ở suy gan hoặc quá liều. Độc tính thần kinh trung ương (co giật) là dấu hiệu cảnh báo sớm.'
        , 'drug_interactions': {'major': [{'drug':
        'Beta-blockers (Propranolol, Metoprolol, etc.)', 'mechanism':
        'Beta-blockers ức chế enzyme CYP3A4 và CYP1A2 chuyển hóa lidocaine, làm giảm chuyển hóa và tăng nồng độ lidocaine trong máu.'
        , 'effect':
        'Tăng nồng độ lidocaine, tăng nguy cơ độc tính thần kinh trung ương (co giật, lú lẫn) và độc tính tim mạch (block AV, rung thất)'
        , 'management':
        'GIẢM LIỀU lidocaine xuống 30-50% khi dùng với beta-blockers. Theo dõi chặt chẽ dấu hiệu độc tính. Kiểm tra nồng độ lidocaine trong máu nếu có thể.'
        }, {'drug': 'Cimetidine', 'mechanism':
        'Cimetidine ức chế enzyme CYP3A4 và CYP1A2 chuyển hóa lidocaine, làm giảm chuyển hóa và tăng nồng độ lidocaine trong máu.'
        , 'effect':
        'Tăng nồng độ lidocaine, tăng nguy cơ độc tính thần kinh trung ương và độc tính tim mạch'
        , 'management':
        'GIẢM LIỀU lidocaine xuống 30-50% khi dùng với cimetidine. Theo dõi chặt chẽ dấu hiệu độc tính. Có thể dùng ranitidine hoặc famotidine thay thế cimetidine.'
        }],
        'moderate': [{'drug': 'Phenytoin', 'mechanism':
        'Phenytoin có thể tăng độc tính của lidocaine (cơ chế không rõ ràng, có thể liên quan đến tác dụng trên hệ thần kinh trung ương).'
        , 'effect':
        'Tăng nguy cơ độc tính thần kinh trung ương (co giật, lú lẫn)',
        'management':
        'Thận trọng, theo dõi chặt chẽ dấu hiệu độc tính. Có thể cần giảm liều lidocaine.'
        }, {'drug': 'Amiodarone', 'mechanism':
        'Amiodarone có thể tăng độc tính tim mạch của lidocaine (cả hai đều là thuốc chống loạn nhịp, có thể tăng tác dụng phụ).'
        , 'effect': 'Tăng nguy cơ độc tính tim mạch (block AV, rung thất)',
        'management':
        'Thận trọng, theo dõi ECG chặt chẽ. Có thể cần giảm liều lidocaine.'}],
        'minor': [{'drug': 'Quinidine, Procainamide', 'mechanism':
        'Các thuốc chống loạn nhịp khác có thể tăng tác dụng phụ tim mạch.',
        'effect': 'Tăng nguy cơ độc tính tim mạch (nhẹ)', 'management':
        'Theo dõi ECG. Không cần điều chỉnh liều thường quy.'}]},
        'contraindications': {'tuyệt_đối': [
        'Dị ứng lidocaine hoặc thuốc gây tê nhóm amide',
        'Block nhĩ thất độ 2-3 không có máy tạo nhịp - có thể làm nặng block, gây nhịp chậm nặng'
        , 'Hội chứng Adams-Stokes - nguy cơ nhịp chậm nặng, ngừng tim'],
        'tương_đối': [
        'Suy gan nặng - giảm chuyển hóa, tích lũy, tăng nguy cơ độc tính',
        'Suy tim nặng - giảm phân bố, tăng nồng độ, tăng nguy cơ độc tính',
        'Người cao tuổi - giảm chuyển hóa, tăng nhạy cảm với độc tính',
        'Block nhĩ thất độ 1 - có thể làm nặng block',
        'Block nhánh - có thể làm nặng block',
        'Rối loạn nhịp nặng - có thể làm nặng rối loạn nhịp',
        'Dùng với beta-blockers hoặc cimetidine - tăng nồng độ, cần giảm liều',
        'Bệnh nhân có tiền sử co giật - tăng nguy cơ co giật']},pregnancy_lactation': {'fda_category': 'B', 'pregnancy_details':
        'Lidocaine là thuốc phân loại B. Có một số nghiên cứu trên động vật không cho thấy nguy cơ cho thai nhi. Lidocaine có thể qua nhau thai, nhưng nồng độ trong máu thai nhi thấp. Được sử dụng trong gây tê sản khoa (epidural, spinal) và được coi là an toàn. Trong cấp cứu (rối loạn nhịp thất), lợi ích vượt quá nguy cơ.'
        , 'lactation': {'safety': 'Compatible', 'details':
        'Lidocaine bài tiết vào sữa mẹ ở nồng độ thấp. Không có báo cáo về tác dụng phụ ở trẻ bú mẹ khi dùng liều điều trị. Khi dùng liều cao hoặc kéo dài, có thể cần thận trọng.'
        , 'recommendation':
        'Có thể dùng khi cho con bú. Lidocaine bài tiết vào sữa mẹ ở nồng độ thấp và không gây tác dụng phụ ở trẻ bú mẹ.'
        }},hepatic_adjustment': {'mild':
        'Giảm liều 20-30%. Lidocaine chuyển hóa mạnh ở gan (CYP3A4, CYP1A2), suy gan nhẹ có thể làm giảm chuyển hóa.'
        , 'moderate': 'Giảm liều 30-50%. Theo dõi chặt chẽ dấu hiệu độc tính.',
        'severe':
        'Giảm liều 50-70% hoặc tránh dùng. Suy gan nặng làm giảm chuyển hóa mạnh, tích lũy, tăng nguy cơ độc tính. Nếu cần dùng: dùng liều thấp, theo dõi chặt chẽ, kiểm tra nồng độ lidocaine trong máu.'
        , 'notes':
        'Lidocaine chuyển hóa mạnh ở gan (CYP3A4, CYP1A2). Suy gan làm giảm chuyển hóa, tích lũy, tăng nguy cơ độc tính. PHẢI điều chỉnh liều ở suy gan. Theo dõi chặt chẽ dấu hiệu độc tính (co giật, lú lẫn, block AV).'
        },overdose_management': {'symptoms': [
        'Độc tính thần kinh trung ương (dấu hiệu sớm):',
        '  - Chóng mặt, ù tai, nhìn mờ', '  - Lú lẫn, kích động', '  - Co giật',
        '  - Mất ý thức, ngừng thở',
        'Độc tính tim mạch (dấu hiệu muộn, nguy hiểm):',
        '  - Block nhĩ thất độ 2-3', '  - Nhịp tim chậm nặng', '  - Rung thất',
        '  - Ngừng tim', 'Hạ huyết áp',
        'Phản ứng dị ứng (hiếm): phát ban, sốc phản vệ'],antidote':
        'Không có antidote đặc hiệu cho quá liều lidocaine. Điều trị hỗ trợ và điều trị triệu chứng.'
        , 'treatment': ['Ngừng ngay lidocaine nếu đang truyền',
        'Theo dõi ECG và dấu hiệu sinh tồn liên tục',
        'Nếu độc tính thần kinh trung ương (co giật):',
        '  - Benzodiazepine (diazepam 5-10mg IV, lorazepam 2-4mg IV) - điều trị chính'
        , '  - Nếu không đáp ứng: Phenytoin, phenobarbital',
        '  - Hỗ trợ hô hấp: Thở oxy, nếu cần hỗ trợ thông khí cơ học',
        'Nếu độc tính tim mạch (block AV, nhịp chậm, rung thất):',
        '  - Nếu block AV độ 2-3 hoặc nhịp chậm nặng:',
        '    - Atropine 0.5-1mg IV (nếu không có block AV)',
        '    - Epinephrine 1mg IV (nếu ngừng tim)',
        '    - Máy tạo nhịp tạm thời nếu cần',
        '  - Nếu rung thất: Defibrillation',
        '  - Nếu ngừng tim: CPR, ACLS protocol', 'Nếu hạ huyết áp:',
        '  - Truyền dịch (NS, LR)',
        '  - Thuốc vận mạch nếu cần (epinephrine, norepinephrine)',
        'Nếu phản ứng dị ứng:', '  - Epinephrine 0.3-0.5mg IM',
        '  - Diphenhydramine 25-50mg IV',
        '  - Corticosteroid (methylprednisolone 125mg IV)',
        'Hỗ trợ hô hấp: Thở oxy, nếu cần hỗ trợ thông khí cơ học',
        'Theo dõi dấu hiệu sinh tồn: Huyết áp, nhịp tim, ECG, nhịp thở, SpO2 trong ít nhất 2-4 giờ'
        'Kiểm tra nồng độ lidocaine trong máu nếu có thể (nồng độ điều trị: 1.5-5mcg/ml, độc tính: >5-6mcg/ml)'
        ],
        'monitoring':
        'Theo dõi ECG, huyết áp, nhịp tim, nhịp thở, SpO2 liên tục trong ít nhất 2-4 giờ sau khi dùng. Theo dõi lâu hơn nếu có biến chứng (độc tính thần kinh, độc tính tim mạch). Kiểm tra nồng độ lidocaine trong máu nếu có thể.'
        },reversal_agents': {'available': False, 'agents': [],notes':
        'Không có reversal agent đặc hiệu cho lidocaine. Điều trị hỗ trợ và điều trị triệu chứng (benzodiazepine cho co giật, atropine/epinephrine cho block AV/nhịp chậm).'
        },administration_instructions': {'oral': None, 'iv': {
        'reconstitution':
        'Dùng trực tiếp từ lọ (1% = 10mg/ml, 2% = 20mg/ml). Không cần pha loãng cho bolus. Cho infusion: pha 1g (50ml 2%) trong 450ml D5W = 2mg/ml.'
        , 'infusion_rate':
        'Cardiac arrest: 1-1.5mg/kg IV bolus, lặp lại 0.5-0.75mg/kg mỗi 5-10 phút (tối đa 3mg/kg). VT with pulse: 1-1.5mg/kg IV bolus, sau đó 1-4mg/phút IV infusion. Trẻ em: 1mg/kg IV/IO bolus, sau đó 20-50mcg/kg/phút IV infusion.'
        , 'compatibility': ['NS (0.9% NaCl)', 'D5W (5% Dextrose)',
        "LR (Lactated Ringer's)"],incompatibility': [
        'Không trộn với các thuốc khác. Tiêm bolus riêng biệt hoặc dùng đường truyền riêng cho infusion.'
        ],notes':
        'QUAN TRỌNG: 1) PHẢI điều chỉnh liều ở suy gan (giảm 30-70%), 2) PHẢI điều chỉnh liều ở suy tim (giảm 20-30%), 3) PHẢI điều chỉnh liều khi dùng với beta-blockers hoặc cimetidine (giảm 30-50%), 4) Độc tính thần kinh trung ương là dấu hiệu CẢNH BÁO SỚM - ngừng ngay nếu có, 5) Tiêm IV chậm (không quá 25-50mg/phút) để tránh độc tính, 6) Theo dõi ECG chặt chẽ, 7) Giảm liều ở người cao tuổi.'
        },local_anesthesia': {'reconstitution':
        'Dùng trực tiếp từ lọ (1% = 10mg/ml, 2% = 20mg/ml). Có thể pha với epinephrine để kéo dài tác dụng và giảm hấp thu.'
        , 'max_dose':
        'Không có epinephrine: 4.5mg/kg (tối đa 300mg). Có epinephrine: 7mg/kg (tối đa 500mg).'
        , 'notes':
        'Tuân thủ liều tối đa để tránh độc tính. Không tiêm vào mạch máu. Theo dõi dấu hiệu độc tính (chóng mặt, ù tai, co giật).'
        }},references': {'primary_sources': ['FDA Drug Label - Lidocaine',
        'ACLS Guidelines 2020 - American Heart Association',
        'UpToDate - Lidocaine: Drug Information',
        'Medscape - Lidocaine Drug Reference',
        "Goodman & Gilman's The Pharmacological Basis of Therapeutics (14th ed)",
        'Lexicomp Online - Lidocaine Monograph',
        'Micromedex - Lidocaine Drug Information'],last_updated':
        '2025-02-03', 'evidence_level':
        'A - Dựa trên FDA drug labels, ACLS guidelines, và dữ liệu lâm sàng từ nhiều nguồn',
        },
        "risk_flags": {
            "high_alert": True,
            "narrow_therapeutic_index": True,
            "bleeding_risk": False,
            "organ_toxicity": ["cardiac", "hepatic"],
            "qt_prolongation": False,
            "hepatotoxicity": True,
            "nephrotoxicity": False,
            "requires_monitoring": ["ECG", "Vital Signs", "LFT"]
        },
        "guideline_tags": [
            "ACLS Guidelines 2020 - American Heart Association",
            "FDA Drug Label - Lidocaine",
            "ISMP High Alert Medications - Emergency Medications"
        ]}}

__all__ = ['LOCAL_ANESTHETIC_ANTIARRHYTHMIC_CLASS_IB_DRUGS']
