"""Gastrointestinal Drugs
Active module - contains all gastrointestinal drug data"""

# Prokinetic, Antiemetics

PROKINETIC_ANTIEMETICS_DRUGS = {
    "Domperidone": {'group': 'Gastrointestinal - Prokinetic, Antiemetic',
        ',
        "pregnancy": "C - Nguy cơ không thể loại trừ. Thận trọng trong thai kỳ",
        ', 'vietnamese_name':
        'Domperidone, Motilium', 'administration': ['PO'], 'indications': [
        'Buồn nôn, nôn', 'Liệt dạ dày (gastroparesis)', 'Ợ nóng',
        'Trào ngược dạ dày thực quản'], 'contraindications': [
        'Dị ứng domperidone', 'Chảy máu dạ dày', 'Tắc ruột cơ học',
        'Prolactinoma', 'Dùng với các thuốc QT kéo dài'], 'dosage': {
        'adult_nausea': '10-20mg x 3-4 lần/ngày, uống trước bữa ăn',
        'adult_gastroparesis': '10mg x 3-4 lần/ngày trước bữa ăn', 'adult_max':
        '80mg/ngày', 'notes':
        'Không qua hàng rào máu-não nên ít tác dụng phụ thần kinh hơn metoclopramide'
        }, 'renal_adjustment': {'normal': 'Không đổi', '30_60':
        'Thận trọng, giảm liều', 'under_30': 'Thận trọng, giảm liều 50%'},
        'side_effects': ['Rối loạn kinh nguyệt', 'Tăng prolactin', 'Đau vú',
        'Chảy sữa (galactorrhea)', 'QT kéo dài (liều cao)', 'Nhức đầu'],
        'interactions': [
        'QT kéo dài: tránh dùng với thuốc QT kéo dài (amiodarone, quinolone)',
        'Ketoconazole: tăng nồng độ domperidone',
        'Erythromycin: tăng nồng độ domperidone'],
        'mechanism_of_action':
        'Dopamine D2 receptor antagonist ở ngoại vi (ruột và chemoreceptor trigger zone). Ức chế dopamine → tăng nhu động dạ dày và ruột, tăng trương lực cơ thắt dưới thực quản, tăng tốc độ làm rỗng dạ dày. Có tác dụng chống nôn do ức chế dopamine ở chemoreceptor trigger zone. KHÔNG qua hàng rào máu-não (do bị P-glycoprotein đẩy ra) → ít tác dụng phụ thần kinh hơn metoclopramide (không gây mê sảng, parkinsonism). Tăng prolactin do ức chế dopamine ở tuyến yên (dopamine ức chế tiết prolactin).'
        , 'monitoring': [
        'Đáp ứng lâm sàng (giảm buồn nôn, nôn, cải thiện làm rỗng dạ dày)',
        'ECG nếu dùng liều cao hoặc kéo dài (nguy cơ QT kéo dài)',
        'Dấu hiệu tăng prolactin: rối loạn kinh nguyệt, chảy sữa, đau vú',
        'Dấu hiệu QT kéo dài: loạn nhịp tim, chóng mặt, ngất',
        'Dấu hiệu tác dụng phụ thần kinh (hiếm nhưng có thể xảy ra nếu tích lũy)'
        ], 'precautions': [
        'Không vượt quá 80mg/ngày (tăng nguy cơ QT kéo dài)',
        'Tránh dùng với các thuốc kéo dài QT (amiodarone, quinolone, macrolide) - tăng nguy cơ loạn nhịp'
        , 'Thận trọng ở suy thận (giảm liều)',
        'Thận trọng ở suy gan (giảm liều)',
        'Theo dõi dấu hiệu tăng prolactin (rối loạn kinh nguyệt, chảy sữa)',
        'Ngừng nếu có dấu hiệu QT kéo dài hoặc loạn nhịp',
        'Ít tác dụng phụ thần kinh hơn metoclopramide (không qua hàng rào máu-não)'
        ,
        'Không dùng trong prolactinoma (tăng prolactin có thể làm tăng kích thước u)'
        ], 'pharmacokinetics': {'onset': '30-60 phút',
        'duration': '4-8 giờ', 'protein_binding': '91-93%', 'metabolism':
        'Gan (chuyển hóa qua CYP3A4), CYP1A2', 'clearance':
        'Gan (chuyển hóa), thận (thải trừ)'}, 'storage':
        'Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm, tránh ánh sáng',
        'black_box_warnings':
        'Nguy cơ QT kéo dài và loạn nhịp tim nghiêm trọng (torsades de pointes), có thể tử vong. Nguy cơ tăng ở liều cao (>80mg/ngày), suy thận, suy gan, hoặc dùng với các thuốc kéo dài QT. Không vượt quá 80mg/ngày. Tránh dùng với các thuốc kéo dài QT.'
        , 'drug_interactions': {'major': [{'drug':
        'Thuốc kéo dài QT (amiodarone, quinolone, macrolide, haloperidol, etc.)',
        'mechanism': 'Tác dụng hiệp đồng kéo dài QT interval', 'effect':
        'Tăng nguy cơ QT kéo dài, torsades de pointes, loạn nhịp tim, có thể tử vong'
        , 'management':
        'CHỐNG CHỈ ĐỊNH dùng cùng. Tránh dùng domperidone với các thuốc kéo dài QT.'
        }], 'moderate': [{'drug':
        'CYP3A4 inhibitors (ketoconazole, itraconazole, ritonavir, clarithromycin, erythromycin)'
        , 'mechanism': 'Ức chế chuyển hóa domperidone qua CYP3A4', 'effect':
        'Tăng nồng độ domperidone, tăng nguy cơ QT kéo dài', 'management':
        'Tránh dùng cùng hoặc giảm liều domperidone. Theo dõi ECG.'}, {'drug':
        'Anticholinergics', 'mechanism': 'Đối kháng tác dụng prokinetic',
        'effect': 'Giảm hiệu quả prokinetic', 'management':
        'Tránh dùng cùng nếu có thể'}], 'minor': []}, 'contraindications': {
        'tuyệt_đối': ['Dị ứng domperidone', 'Chảy máu dạ dày',
        'Tắc ruột cơ học', 'Prolactinoma',
        'Dùng với các thuốc kéo dài QT - CHỐNG CHỈ ĐỊNH tuyệt đối',
        'QT kéo dài (QTc >450ms ở nam, >470ms ở nữ) - CHỐNG CHỈ ĐỊNH'],
        'tương_đối': ['Suy thận nặng (CrCl <30) - giảm liều 50%',
        'Suy gan nặng - giảm liều, tăng nguy cơ QT kéo dài',
        'Hạ kali, hạ magie - tăng nguy cơ QT kéo dài',
        'Người già - thận trọng, giảm liều', 'Rối loạn nhịp tim - thận trọng']},
        'pregnancy_lactation': {'fda_category': 'C', 'pregnancy_details':
        'Domperidone là FDA category C. Nghiên cứu trên động vật cho thấy có thể gây độc tính cho thai nhi. Không có nghiên cứu đầy đủ trên người. Có thể dùng trong thai kỳ nếu lợi ích > nguy cơ, nhưng nên tránh trong tam cá nguyệt đầu nếu có thể.'
        , 'lactation': {'safety': 'Compatible', 'details':
        'Domperidone bài tiết vào sữa mẹ ở nồng độ thấp. Có thể dùng để tăng tiết sữa mẹ (off-label). An toàn khi cho con bú.'
        , 'recommendation':
        'Có thể dùng khi cho con bú. Dùng liều thường dùng (10-20mg x 3-4 lần/ngày).'
        }}, 'hepatic_adjustment': {'mild': 'Không cần chỉnh liều', 'moderate':
        'Thận trọng, có thể giảm liều', 'severe':
        'Giảm liều hoặc tránh dùng. Domperidone chuyển hóa ở gan qua CYP3A4. Suy gan nặng làm giảm chuyển hóa, tăng nồng độ, tăng nguy cơ QT kéo dài.'
        , 'notes':
        'Domperidone chuyển hóa ở gan. Suy gan nặng làm tăng nồng độ, tăng nguy cơ QT kéo dài. Giảm liều hoặc tránh dùng ở suy gan nặng.'
        }, 'overdose_management': {'symptoms': [
        'QT kéo dài, torsades de pointes, loạn nhịp tim (triệu chứng chính, có thể tử vong)'
        , 'Tăng prolactin: rối loạn kinh nguyệt, chảy sữa', 'Buồn nôn, nôn',
        'Nhức đầu'], 'treatment': [
        'Theo dõi ECG liên tục (QT interval)',
        'Điều trị torsades de pointes nếu có: magnesium sulfate 2g IV, pacing nếu cần'
        , 'Bổ sung kali, magie nếu thiếu', 'Hỗ trợ triệu chứng',
        'Theo dõi dấu hiệu sinh tồn chặt chẽ'], 'monitoring':
        'Theo dõi ECG liên tục (QT interval), dấu hiệu sinh tồn, điện giải'},
        'reversal_agents': None, 'administration_instructions': {'oral': {
        'with_food': 'Uống 15-30 phút TRƯỚC bữa ăn (tăng hiệu quả)', 'timing':
        'Uống 15-30 phút trước bữa ăn và trước khi đi ngủ. Không vượt quá 80mg/ngày.'
        }, 'iv': {'reconstitution': 'Domperidone chỉ có dạng uống (PO)',
        'infusion_rate': 'N/A', 'compatibility': [], 'incompatibility': [],
        'notes': 'Domperidone chỉ có dạng uống, không có dạng IV'}},
        'risk_flags': {
            'high_alert': True,
            'narrow_therapeutic_index': False,
            'icu_critical_care_only': False,
            'bleeding_risk': False,
            'organ_toxicity': ['cardiac'],
            'qt_prolongation': True,
            'hepatotoxicity': False,
            'nephrotoxicity': False,
            'requires_monitoring': ['ECG'],
            'look_alike_sound_alike': []
        },
        'guideline_tags': [
            'FDA Black Box Warning - Nguy cơ QT kéo dài và loạn nhịp tim nghiêm trọng (torsades de pointes), có thể tử vong. Không vượt quá 80mg/ngày.',
            'ISMP High Alert Medications',
            'ACG Guidelines - Gastroparesis and Nausea/Vomiting',
            'WHO Guidelines - Essential medicines for GI disorders'
        ],
        'references': {'primary_sources': [
        'FDA Drug Label - Domperidone (Note: Not FDA approved in US, available in other countries)'
        , 'UpToDate - Domperidone: Drug information',
        'Micromedex - Domperidone',
        'European Medicines Agency - Domperidone safety review',
        "Goodman & Gilman's The Pharmacological Basis of Therapeutics"],
        'last_updated': '2024-12-19', 'evidence_level':
        'High - Multiple RCTs, safety warnings (QT prolongation)'},
        "reversal_agents": {
             "available": False,
             "agents": []
         },
    "Metoclopramide": {'group': 'Gastrointestinal - Prokinetic, Antiemetic', 'vietnamese_name':
        'Metoclopramide, Primperan', 'administration': ['PO', 'IV', 'IM'],
        'indications': ['Buồn nôn, nôn', 'Liệt dạ dày',
        'Trào ngược dạ dày thực quản', 'Đau nửa đầu (kết hợp)'],
        'contraindications': ['Tắc ruột', 'Xuất huyết tiêu hóa',
        'Rối loạn vận động (Parkinson, dystonia)', 'Epilepsy'], 'dosage': {
        'adult_po': '10mg x 3-4 lần/ngày', 'adult_iv_im':
        '10mg IV/IM mỗi 6-8 giờ', 'adult_max': '60mg/ngày', 'notes':
        'Không dùng quá 12 tuần (rối loạn vận động muộn)'}, 'side_effects': [
        'Rối loạn vận động (dystonia, parkinsonism)', 'Buồn ngủ',
        'Hội chứng serotonin (với SSRI)',
        'Rối loạn vận động muộn (dùng lâu dài)'], 'interactions': [
        'SSRI/SNRI: tăng nguy cơ hội chứng serotonin',
        'Antipsychotics: tăng nguy cơ rối loạn vận động'],
        'renal_adjustment': {'normal': 'Không đổi', '30_60': 'Giảm liều 25-50%',
        'under_30': 'Giảm liều 50-75%'}, 'mechanism_of_action':
        'Dopamine D2 receptor antagonist và 5-HT3 receptor antagonist. Ức chế dopamine ở chemoreceptor trigger zone (CTZ), giảm buồn nôn, nôn. Tăng co bóp dạ dày, tăng trương lực cơ thắt môn vị, tăng nhu động ruột (prokinetic effect). Cũng ức chế 5-HT3 receptor (giống ondansetron).'
        , 'monitoring': [
        'Dấu hiệu rối loạn vận động: dystonia, parkinsonism, akathisia (xuất hiện sớm, có thể điều trị)'
        ,
        'Rối loạn vận động muộn (tardive dyskinesia) - nếu dùng >12 tuần (có thể không hồi phục)'
        ,
        'Dấu hiệu hội chứng serotonin: kích động, tăng thân nhiệt, tăng phản xạ (nếu dùng với SSRI/SNRI)'
        , 'Đáp ứng lâm sàng: giảm buồn nôn, nôn; tăng nhu động dạ dày'],
        'precautions': [
        'KHÔNG dùng quá 12 tuần - tăng nguy cơ rối loạn vận động muộn (tardive dyskinesia) có thể không hồi phục'
        ,
        'Thận trọng ở trẻ em và thanh niên - tăng nguy cơ rối loạn vận động (dystonia, parkinsonism)'
        , 'Tránh dùng ở bệnh nhân Parkinson, dystonia - làm nặng triệu chứng',
        'Thận trọng khi dùng với SSRI/SNRI - tăng nguy cơ hội chứng serotonin',
        'Thận trọng khi dùng với antipsychotics - tăng nguy cơ rối loạn vận động',
        'Tránh dùng với anticholinergics - đối kháng tác dụng prokinetic',
        'CHỐNG CHỈ ĐỊNH trong tắc ruột, xuất huyết tiêu hóa',
        'Có thể gây buồn ngủ - tránh lái xe, vận hành máy móc'],
        'pharmacokinetics': {'half_life': '5-6 giờ', 'onset':
        '1-3 phút (IV), 30-60 phút (PO)', 'duration': '1-2 giờ',
        'protein_binding': '30%', 'clearance':
        'Gan (CYP2D6), thận (30% thải nguyên dạng)'}, 'storage':
        'Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm, tránh ánh sáng',
        'black_box_warnings':
        'Rối loạn vận động muộn (tardive dyskinesia) có thể phát triển và trở thành không hồi phục. Nguy cơ tăng với thời gian điều trị và tổng liều. Ngừng ngay nếu có dấu hiệu rối loạn vận động. KHÔNG dùng quá 12 tuần'
        , 'drug_interactions': {'major': [{'drug':
        'SSRI/SNRI (fluoxetine, sertraline, venlafaxine, etc.)', 'mechanism':
        'Metoclopramide ức chế 5-HT3 receptor và có thể tăng serotonin, tác dụng hiệp đồng với SSRI/SNRI'
        , 'effect':
        'Tăng nguy cơ hội chứng serotonin (kích động, tăng thân nhiệt, tăng phản xạ, co giật)'
        , 'management':
        'Tránh dùng cùng hoặc thận trọng. Theo dõi dấu hiệu hội chứng serotonin. Ngừng ngay nếu có triệu chứng.'
        }], 'moderate': [{'drug':
        'Antipsychotics (haloperidol, chlorpromazine, risperidone, etc.)',
        'mechanism': 'Tác dụng hiệp đồng ức chế dopamine D2 receptor', 'effect':
        'Tăng nguy cơ rối loạn vận động (extrapyramidal symptoms, tardive dyskinesia)'
        , 'management':
        'Thận trọng. Tránh dùng cùng nếu có thể. Theo dõi dấu hiệu rối loạn vận động.'
        }, {'drug': 'Anticholinergics (atropine, scopolamine, benztropine)',
        'mechanism': 'Đối kháng tác dụng prokinetic của metoclopramide',
        'effect': 'Giảm hiệu quả prokinetic, có thể gây tắc ruột', 'management':
        'Tránh dùng cùng. Đối kháng tác dụng.'}, {'drug':
        'CNS depressants (alcohol, opioids, benzodiazepines)', 'mechanism':
        'Tác dụng hiệp đồng ức chế thần kinh trung ương', 'effect':
        'Tăng buồn ngủ, lú lẫn', 'management':
        'Thận trọng. Tránh lái xe, vận hành máy móc.'}], 'minor': [{'drug':
        'Paracetamol', 'mechanism': 'Tăng nhu động dạ dày', 'effect':
        'Tăng hấp thu paracetamol nhẹ', 'management':
        'Không cần điều chỉnh liều'}]}, 'contraindications': {'tuyệt_đối': [
        'Dị ứng metoclopramide', 'Tắc ruột cơ học', 'Xuất huyết tiêu hóa',
        'Thủng dạ dày-ruột', 'Pheochromocytoma (tăng nguy cơ tăng huyết áp)',
        'Rối loạn vận động (Parkinson, dystonia, tardive dyskinesia)'],
        'tương_đối': ['Suy thận (CrCl <30) - giảm liều 50-75%',
        'Suy gan nặng - thận trọng, có thể giảm liều',
        'Trẻ em và thanh niên - tăng nguy cơ dystonia, parkinsonism',
        'Epilepsy - có thể làm nặng co giật',
        'Đang dùng SSRI/SNRI - tăng nguy cơ hội chứng serotonin',
        'Đang dùng antipsychotics - tăng nguy cơ rối loạn vận động']},
        'pregnancy_lactation': {'fda_category': 'B', 'pregnancy_details':
        'Metoclopramide là FDA category B. Nghiên cứu trên động vật không cho thấy nguy cơ cho thai nhi. Một số nghiên cứu trên người không cho thấy tăng nguy cơ dị tật bẩm sinh. Có thể dùng trong thai kỳ nếu lợi ích > nguy cơ. Thường dùng để điều trị buồn nôn, nôn trong thai kỳ (hyperemesis gravidarum).'
        , 'lactation': {'safety': 'Compatible', 'details':
        'Metoclopramide bài tiết vào sữa mẹ ở nồng độ thấp. Có thể dùng để tăng tiết sữa mẹ (off-label). An toàn khi cho con bú.'
        , 'recommendation':
        'Có thể dùng khi cho con bú. Dùng liều thường dùng.'}},
        'hepatic_adjustment': {'mild': 'Không cần chỉnh liều', 'moderate':
        'Thận trọng, có thể giảm liều', 'severe':
        'Thận trọng, giảm liều. Metoclopramide chuyển hóa ở gan qua CYP2D6. Suy gan nặng làm giảm chuyển hóa.'
        , 'notes':
        'Metoclopramide chuyển hóa ở gan. Suy gan nặng làm tăng nồng độ. Thận trọng, giảm liều ở suy gan nặng.'
        }, 'overdose_management': {'symptoms': [
        'Rối loạn vận động nặng: dystonia, parkinsonism, akathisia',
        'Buồn ngủ, lú lẫn',
        'Hội chứng serotonin (nếu dùng với SSRI/SNRI): kích động, tăng thân nhiệt, co giật'
        , 'Rối loạn nhịp tim (hiếm)'], 'antidote':
        'Không có antidote đặc hiệu. Dùng diphenhydramine hoặc benztropine để điều trị dystonia.'
        , 'treatment': [
        'Điều trị rối loạn vận động: diphenhydramine 25-50mg IV/IM hoặc benztropine 1-2mg IV/IM'
        , 'Hỗ trợ triệu chứng', 'Theo dõi dấu hiệu sinh tồn',
        'Điều trị hội chứng serotonin nếu có: cyproheptadine, cooling, benzodiazepines'
        ], 'monitoring':
        'Theo dõi dấu hiệu sinh tồn, dấu hiệu rối loạn vận động, dấu hiệu hội chứng serotonin'
        }, 'reversal_agents': None, 'administration_instructions': {'oral': {
        'with_food': 'Uống 30 phút trước bữa ăn (để tăng hiệu quả prokinetic)',
        'timing':
        'Uống 30 phút trước bữa ăn và trước khi đi ngủ. Có thể uống với hoặc không với thức ăn.'
        }, 'iv': {'reconstitution':
        'Metoclopramide IV: 10mg pha với 10-20ml NaCl 0.9% hoặc dextrose 5%',
        'infusion_rate':
        'Truyền trong 15-30 phút (bolus) hoặc tiêm tĩnh mạch chậm',
        'compatibility': ['NaCl 0.9%', 'Dextrose 5%'], 'incompatibility': [
        'Không pha với các thuốc khác trong cùng đường truyền'], 'notes':
        'IV nhanh hơn PO. Chỉ dùng IV khi không uống được. Chuyển sang PO sớm nhất có thể.'
        }}, 'references': {'primary_sources': [
        'FDA Drug Label - Metoclopramide',
        'UpToDate - Metoclopramide: Drug information',
        'Micromedex - Metoclopramide',
        "Goodman & Gilman's The Pharmacological Basis of Therapeutics",
        'FDA Black Box Warning - Tardive dyskinesia risk'], 'last_updated':
        '2024-12-19', 'evidence_level':
        'High - FDA approved, multiple RCTs, black box warning'}},
}}

__all__ = ['PROKINETIC_ANTIEMETICS_DRUGS']
