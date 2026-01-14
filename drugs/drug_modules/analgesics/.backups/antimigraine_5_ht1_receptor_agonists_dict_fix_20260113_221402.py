"""Analgesic and Pain Medications
Active module - contains all analgesic drug data"""

# Antimigraine (5-HT1 Receptor Agonist)s

ANTIMIGRAINE_5_HT1_RECEPTOR_AGONISTS_DRUGS = {
    "Lasmiditan": {
        "group": "Analgesic - Antimigraine (5-HT1F Receptor Agonist)",
        "vietnamese_name": "Lasmiditan, Reyvow",
        "administration": ["PO"],
        "indications": [
            "Điều trị cấp tính cơn migraine (acute migraine treatment) ở người lớn",
            "Migraine có tiền triệu (aura) hoặc không"
        ],
        "contraindications": [
            "Dị ứng lasmiditan hoặc bất kỳ thành phần nào",
            "Suy gan nặng (Child-Pugh C) - CHỐNG CHỈ ĐỊNH",
            "Dùng với rượu (alcohol) - CHỐNG CHỈ ĐỊNH (tăng nguy cơ buồn ngủ, suy giảm nhận thức)"
        ],
        "dosage": {
            "adult_standard": "50-100mg PO x 1 liều khi có cơn migraine",
            "adult_max": "200mg PO x 1 liều (liều tối đa)",
            "adult_repeat": "Có thể lặp lại sau 2 giờ nếu cần (tối đa 200mg/24 giờ)",
            "notes": "Lasmiditan là 5-HT1F receptor agonist, điều trị cấp tính cơn migraine. Dùng khi có cơn migraine, không dùng để phòng ngừa. Uống với hoặc không thức ăn. KHÔNG lái xe hoặc vận hành máy móc trong ít nhất 8 giờ sau khi dùng."
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "Không đổi",
            "under_30": "Thận trọng, giảm liều nếu cần"
        },
        "side_effects": [
            "Buồn ngủ (somnolence) - phổ biến, nghiêm trọng",
            "Chóng mặt (dizziness) - phổ biến",
            "Mệt mỏi (fatigue) - phổ biến",
            "Buồn nôn",
            "Cảm giác tê, ngứa ran (paresthesia) - phổ biến",
            "Suy giảm nhận thức (cognitive impairment) - phổ biến",
            "Lo lắng (anxiety) - hiếm",
            "Tăng transaminase (hiếm)",
            "Dị ứng (hiếm)"
        ],
        "interactions": [
            "Rượu (alcohol): CHỐNG CHỈ ĐỊNH - tăng nguy cơ buồn ngủ, suy giảm nhận thức",
            "CNS depressants (benzodiazepine, opioid, barbiturate): tăng nguy cơ buồn ngủ, suy giảm nhận thức",
            "CYP3A4 inhibitors: tăng nồng độ lasmiditan",
            "CYP3A4 inducers: giảm nồng độ lasmiditan"
        ],
        "pregnancy": "C - Thận trọng",
        "mechanism_of_action": "Lasmiditan là 5-HT1F receptor agonist (selective serotonin receptor agonist). Khác với triptans (5-HT1B/1D receptor agonists), lasmiditan chỉ kích thích 5-HT1F receptors. 5-HT1F receptors có mặt trên các terminal thần kinh trigeminal, ức chế phóng thích chất trung gian gây viêm (CGRP, substance P) từ dây thần kinh trigeminal. Giảm đau migraine thông qua ức chế viêm thần kinh. KHÔNG gây co mạch (ưu điểm so với triptan - không có 5-HT1B receptor activation). ĐẶC ĐIỂM: (1) 5-HT1F receptor agonist (khác với triptan - 5-HT1B/1D), (2) KHÔNG gây co mạch (ưu điểm so với triptan), (3) Dùng khi có cơn migraine, không dùng để phòng ngừa, (4) Buồn ngủ và suy giảm nhận thức phổ biến, nghiêm trọng - KHÔNG lái xe trong ít nhất 8 giờ, (5) CHỐNG CHỈ ĐỊNH với rượu và ở suy gan nặng, (6) Uống với hoặc không thức ăn.",
        "monitoring": [
            "Đáp ứng điều trị: giảm đau migraine trong 2 giờ",
            "Buồn ngủ, chóng mặt, mệt mỏi - phổ biến, nghiêm trọng",
            "Suy giảm nhận thức - phổ biến",
            "Chức năng gan (ALT, AST) - hiếm, nhưng CHỐNG CHỈ ĐỊNH ở suy gan nặng",
            "Dấu hiệu dị ứng (phát ban, khó thở, phù mạch)"
        ],
        "precautions": [
            "CHỐNG CHỈ ĐỊNH với rượu (alcohol) - tăng nguy cơ buồn ngủ, suy giảm nhận thức",
            "CHỐNG CHỈ ĐỊNH ở suy gan nặng (Child-Pugh C)",
            "KHÔNG lái xe hoặc vận hành máy móc trong ít nhất 8 giờ sau khi dùng - buồn ngủ và suy giảm nhận thức phổ biến, nghiêm trọng",
            "Dùng khi có cơn migraine, không dùng để phòng ngừa",
            "Có thể lặp lại sau 2 giờ nếu cần (tối đa 200mg/24 giờ)",
            "Uống với hoặc không thức ăn",
            "Thận trọng khi dùng với CNS depressants - tăng nguy cơ buồn ngủ, suy giảm nhận thức",
            "Thận trọng khi dùng với CYP3A4 inhibitors - tăng nồng độ"
        ],
        "pharmacokinetics": {
            "half_life": "5.7 giờ",
            "onset": "1-2 giờ",
            "duration": "4-6 giờ",
            "protein_binding": "55-60%",
            "metabolism": "Chuyển hóa ở gan (CYP3A4, UGT)",
            "clearance": "Thải trừ qua gan (70%) và thận (30%)"
        },
        "storage": "Bảo quản ở nhiệt độ phòng (20-25°C), tránh ẩm, tránh ánh sáng.",
        "black_box_warnings": "KHÔNG lái xe hoặc vận hành máy móc trong ít nhất 8 giờ sau khi dùng. Lasmiditan gây buồn ngủ và suy giảm nhận thức phổ biến, nghiêm trọng. CHỐNG CHỈ ĐỊNH với rượu (alcohol). CHỐNG CHỈ ĐỊNH ở suy gan nặng (Child-Pugh C).",
        "drug_interactions": {
            "major": [
                {
                    "drug": "Rượu (Alcohol)",
                    "mechanism": "Cả hai đều ức chế CNS, tác dụng cộng dồn",
                    "effect": "Tăng nguy cơ buồn ngủ, suy giảm nhận thức nặng, đe dọa tính mạng",
                    "management": "CHỐNG CHỈ ĐỊNH TUYỆT ĐỐI. Không dùng lasmiditan với rượu hoặc trong 8 giờ sau khi uống rượu."
                },
                {
                    "drug": "CNS Depressants (Benzodiazepine, Opioid, Barbiturate)",
                    "mechanism": "Cả hai đều ức chế CNS, tác dụng cộng dồn",
                    "effect": "Tăng nguy cơ buồn ngủ, suy giảm nhận thức nặng",
                    "management": "TRÁNH DÙNG CÙNG. Nếu bắt buộc, theo dõi chặt chẽ. KHÔNG lái xe trong ít nhất 8 giờ."
                }
            ],
            "moderate": [
                {
                    "drug": "CYP3A4 Inhibitors (Ketoconazole, Clarithromycin, Itraconazole)",
                    "mechanism": "Ức chế CYP3A4, tăng nồng độ lasmiditan",
                    "effect": "Tăng nồng độ lasmiditan, tăng nguy cơ tác dụng phụ (buồn ngủ, suy giảm nhận thức)",
                    "management": "Thận trọng. Có thể cần giảm liều lasmiditan. Theo dõi dấu hiệu buồn ngủ, suy giảm nhận thức."
                }
            ],
            "minor": []
        },
        "contraindications": {
            "tuyệt_đối": [
                "Dị ứng lasmiditan hoặc bất kỳ thành phần nào",
                "Dùng với rượu (alcohol) - CHỐNG CHỈ ĐỊNH (tăng nguy cơ buồn ngủ, suy giảm nhận thức nặng)",
                "Suy gan nặng (Child-Pugh C) - CHỐNG CHỈ ĐỊNH"
            ],
            "tương_đối": [
                "Suy gan nhẹ đến trung bình - thận trọng, giảm liều nếu cần",
                "Suy thận nặng - thận trọng, giảm liều nếu cần",
                "Dùng với CNS depressants - tăng nguy cơ buồn ngủ, suy giảm nhận thức",
                "Có thai (category C) - thận trọng"
            ]
        },
        "pregnancy_lactation": {
            "fda_category": "C",
            "pregnancy_details": "Lasmiditan là thuốc phân loại C. Không có nghiên cứu đầy đủ trên phụ nữ có thai. Có thể dùng khi lợi ích vượt quá nguy cơ, đặc biệt khi không có lựa chọn khác.",
            "lactation": {
                "safety": "Compatible with Caution",
                "details": "Lasmiditan bài tiết vào sữa mẹ. Thận trọng khi cho con bú.",
                "recommendation": "Có thể dùng khi cho con bú, nhưng thận trọng. Theo dõi trẻ về dấu hiệu buồn ngủ, suy giảm nhận thức."
            }
        },
        "hepatic_adjustment": {
            "mild": "Không cần điều chỉnh liều",
            "moderate": "Thận trọng, giảm liều nếu cần",
            "severe": "CHỐNG CHỈ ĐỊNH. Lasmiditan chuyển hóa ở gan, tích lũy ở suy gan nặng.",
            "notes": "Lasmiditan chuyển hóa ở gan (CYP3A4, UGT) và thải trừ qua gan (70%). Suy gan nặng có thể làm tích lũy lasmiditan, tăng nguy cơ tác dụng phụ (buồn ngủ, suy giảm nhận thức). CHỐNG CHỈ ĐỊNH ở suy gan nặng (Child-Pugh C)."
        },
        "overdose_management": {
            "symptoms": [
                "Buồn ngủ nặng",
                "Suy giảm nhận thức nặng",
                "Chóng mặt nặng",
                "Tăng transaminase"
            ],
            "antidote": "Không có antidote đặc hiệu. Điều trị hỗ trợ.",
            "treatment": [
                "Ngừng ngay lasmiditan",
                "Theo dõi dấu hiệu sinh tồn",
                "KHÔNG lái xe hoặc vận hành máy móc trong ít nhất 8 giờ",
                "Theo dõi: Dấu hiệu sinh tồn, chức năng gan"
            ],
            "monitoring": "Theo dõi dấu hiệu sinh tồn, chức năng gan (ALT, AST), dấu hiệu buồn ngủ, suy giảm nhận thức trong ít nhất 8-12 giờ."
        },
        "contraindications_detail": {
            "tuyệt_đối": [
                "Dị ứng lasmiditan hoặc bất kỳ thành phần nào",
                "Dùng với rượu (alcohol) - CHỐNG CHỈ ĐỊNH (tăng nguy cơ buồn ngủ, suy giảm nhận thức nặng)",
                "Suy gan nặng (Child-Pugh C) - CHỐNG CHỈ ĐỊNH"
            ],
            "tương_đối": [
                "Suy gan nhẹ đến trung bình - thận trọng, giảm liều nếu cần",
                "Suy thận nặng - thận trọng, giảm liều nếu cần",
                "Dùng với CNS depressants - tăng nguy cơ buồn ngủ, suy giảm nhận thức",
                "Có thai (category C) - thận trọng"
            ]
        },
        "reversal_agents": {"available": False, "agents": [], "notes": "Không có antidote đặc hiệu. Điều trị chủ yếu là hỗ trợ và điều trị triệu chứng. Ngừng thuốc ngay. Theo dõi tim mạch và triệu chứng thần kinh."},
        "administration_instructions": {
            "oral": {
                "with_food": "Có thể uống với hoặc không thức ăn. Hấp thu không bị ảnh hưởng bởi thức ăn.",
                "timing": "50-100mg PO x 1 liều khi có cơn migraine. Có thể lặp lại sau 2 giờ nếu cần (tối đa 200mg/24 giờ). Dùng ngay khi có triệu chứng migraine. QUAN TRỌNG: KHÔNG lái xe hoặc vận hành máy móc trong ít nhất 8 giờ sau khi dùng."
            }
        },
        "references": {
            "primary_sources": [
                "FDA Drug Label - Lasmiditan (Reyvow)",
                "UpToDate - Lasmiditan: Drug Information",
                "Medscape - Lasmiditan Drug Reference",
                "AHS Guidelines - Acute Migraine Treatment"
            ],
            "last_updated": "2025-02-18",
            "evidence_level": "A - Dựa trên FDA drug labels, clinical guidelines"
        },
        "risk_flags": {
            "high_alert": False,
            "narrow_therapeutic_index": False,
            "bleeding_risk": False,
            "organ_toxicity": ["neurological", "hepatic"],
            "qt_prolongation": False,
            "hepatotoxicity": True,
            "nephrotoxicity": False,
            "requires_monitoring": ["LFT", "Cognitive function", "Driving ability"]
        },
        "guideline_tags": [
            "AHS Guidelines - Acute Migraine Treatment",
            "FDA Black Box Warning - Driving Impairment",
            "FDA Drug Information",
            "UpToDate Drug Information"
        ]
    },
    "Rizatriptan": {'group': 'Analgesic - Antimigraine (5-HT1 Receptor Agonist)',
        "pregnancy": "C - Nguy cơ không thể loại trừ. Thận trọng trong thai kỳ",
        'vietnamese_name': 'Rizatriptan, Maxalt', 'administration': ['PO',
        'ODT'],
        'indications': [
        'Migraine có tiền triệu (aura) hoặc không', 'Cluster headache'],
        'contraindications': ['Bệnh mạch vành', 'Nhồi máu cơ tim',
        'Đau thắt ngực không ổn định', 'Đột quỵ, TIA',
        'Bệnh mạch máu ngoại biên', 'Tăng huyết áp không kiểm soát',
        'Dùng MAO inhibitor trong 14 ngày', 'Dùng ergotamine trong 24 giờ'],
        'dosage': {'adult_po': '5-10mg, có thể lặp sau 2 giờ (tối đa 30mg/ngày)',
        'adult_odt': '5-10mg ODT, có thể lặp sau 2 giờ (tối đa 30mg/ngày)',
        'notes':
        'Dùng ngay khi có triệu chứng migraine. Nếu dùng với propranolol: giảm liều 50% (5mg thay vì 10mg)'},
        'renal_adjustment': {'normal': 'Không đổi', '30_60': 'Không đổi',
        'under_30': 'Thận trọng'},
        'side_effects': [
        'Đau ngực, khó thở (tương tự đau thắt ngực)', 'Nhức đầu', 'Chóng mặt',
        'Buồn nôn', 'Yếu, mệt mỏi', 'Nguy cơ đau tim (hiếm nhưng nguy hiểm)'],
        'interactions': [
        'Ergotamine/Dihydroergotamine: chống chỉ định (trong 24 giờ)',
        'MAO inhibitor: chống chỉ định (trong 14 ngày)',
        'Propranolol: tăng nồng độ rizatriptan (giảm liều rizatriptan 50%)',
        'SSRI/SNRI: tăng nguy cơ hội chứng serotonin'],
        'mechanism_of_action':
        '5-HT1B/1D receptor agonist (selective serotonin receptor agonist, triptan). Tương tự sumatriptan nhưng có tác dụng nhanh hơn và hiệu quả hơn. Kích thích 5-HT1B receptors ở mạch máu não → co mạch (giảm giãn mạch trong migraine). Kích thích 5-HT1D receptors → ức chế phóng thích chất trung gian gây viêm (CGRP, substance P) từ dây thần kinh trigeminal. Giảm đau migraine thông qua cả hai cơ chế: co mạch và ức chế viêm thần kinh. Tác dụng nhanh (30-60 phút PO). Có dạng ODT (orally disintegrating tablet) - thuận tiện hơn, không cần nước.'
        , 'monitoring': [
        'Đáp ứng lâm sàng (giảm đau migraine, triệu chứng)',
        'Dấu hiệu co mạch: đau ngực, khó thở, đau cổ, hàm (có thể giống đau thắt ngực)'
        , 'Dấu hiệu bệnh mạch vành: đau ngực, khó thở, đau lan (nguy hiểm)',
        'Huyết áp (có thể tăng nhẹ)',
        'Dấu hiệu hội chứng serotonin: kích động, tăng thân nhiệt, tăng phản xạ (nếu dùng với SSRI/SNRI)'
        , 'Tương tác với propranolol (tăng nồng độ, cần giảm liều 50%)'],
        'precautions': [
        'Dùng ngay khi có triệu chứng migraine (không chờ đến khi đau nặng)',
        'Không dùng để phòng ngừa - chỉ dùng để cắt cơn',
        'CHỐNG CHỈ ĐỊNH trong bệnh mạch vành, nhồi máu cơ tim, đột quỵ, TIA, bệnh mạch máu ngoại biên'
        , 'CHỐNG CHỈ ĐỊNH trong tăng huyết áp không kiểm soát',
        'Không dùng với ergotamine/dihydroergotamine trong 24 giờ - tăng nguy cơ co mạch nặng'
        'Không dùng với MAO inhibitor trong 14 ngày - tăng nguy cơ tác dụng phụ',
        'Nếu dùng với propranolol: GIẢM LIỀU RIZATRIPTAN 50% (5mg thay vì 10mg) - propranolol tăng nồng độ rizatriptan'
        , 'Thận trọng khi dùng với SSRI/SNRI - tăng nguy cơ hội chứng serotonin',
        'Nếu đau ngực, khó thở → ngừng ngay và đánh giá',
        'Không vượt quá liều tối đa (30mg/ngày)',
        'Dạng ODT: đặt trên lưỡi, không cần nước, thuận tiện hơn'],
        'pharmacokinetics': {
        'half_life': '2-3 giờ', 'onset': 'PO: 30-60 phút; ODT: 30-60 phút',
        'duration': '2-4 giờ', 'protein_binding': '14%', 'metabolism':
        'Gan (chuyển hóa qua MAO-A, một phần qua CYP2D6)', 'clearance':
        'Gan (chuyển hóa), thận (thải trừ). Propranolol ức chế MAO-A, tăng nồng độ rizatriptan.'},storage':
        'Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm, tránh ánh sáng. Dạng ODT: bảo quản trong bao bì kín, tránh ẩm.'
        , 'black_box_warnings':
        'Nguy cơ co mạch nghiêm trọng, có thể gây nhồi máu cơ tim, đột quỵ, thiếu máu cục bộ, có thể tử vong. CHỐNG CHỈ ĐỊNH trong bệnh mạch vành, nhồi máu cơ tim, đột quỵ, TIA, bệnh mạch máu ngoại biên, tăng huyết áp không kiểm soát. Không dùng với ergotamine trong 24 giờ. Nếu có đau ngực, khó thở → ngừng ngay và đánh giá.'
        , 'drug_interactions': {'major': [{'drug':
        'Ergotamine, Dihydroergotamine', 'mechanism':
        'Cả hai đều gây co mạch, tăng nguy cơ co mạch nghiêm trọng', 'effect':
        'Tăng nguy cơ co mạch nghiêm trọng, nhồi máu cơ tim, đột quỵ, thiếu máu cục bộ'
        , 'management':
        'CHỐNG CHỈ ĐỊNH - không dùng với ergotamine/dihydroergotamine trong 24 giờ.'}, {
        'drug': 'MAO Inhibitors (Phenelzine, Tranylcypromine)', 'mechanism':
        'Ức chế MAO-A (chuyển hóa rizatriptan), tăng nồng độ rizatriptan',
        'effect': 'Tăng nguy cơ tác dụng phụ, co mạch nghiêm trọng', 'management':
        'CHỐNG CHỈ ĐỊNH - không dùng với MAO inhibitor trong 14 ngày.'}, {'drug':
        'Propranolol', 'mechanism': 'Ức chế MAO-A, tăng nồng độ rizatriptan',
        'effect': 'Tăng nồng độ rizatriptan, tăng tác dụng phụ', 'management':
        'GIẢM LIỀU RIZATRIPTAN 50% (5mg thay vì 10mg) khi dùng với propranolol.'}],
        'moderate': [{'drug': 'SSRI/SNRI (Fluoxetine, Sertraline, Venlafaxine)',
        'mechanism': 'Cả hai đều tăng serotonin, tăng nguy cơ hội chứng serotonin',
        'effect': 'Tăng nguy cơ hội chứng serotonin (kích động, tăng thân nhiệt, tăng phản xạ)'
        , 'management':
        'Thận trọng, theo dõi dấu hiệu hội chứng serotonin. Có thể cần tránh dùng cùng.'}],
        'minor': []},contraindications': {'tuyệt_đối': [
        'Dị ứng với rizatriptan hoặc các thành phần khác',
        'Bệnh mạch vành (CAD)', 'Nhồi máu cơ tim',
        'Đau thắt ngực không ổn định', 'Đột quỵ, TIA',
        'Bệnh mạch máu ngoại biên', 'Tăng huyết áp không kiểm soát',
        'Dùng MAO inhibitor trong 14 ngày',
        'Dùng ergotamine/dihydroergotamine trong 24 giờ'],
        'tương_đối': [
        'Bệnh tim mạch khác (suy tim, loạn nhịp) - thận trọng, đánh giá tim mạch trước'
        , 'Tăng huyết áp đã kiểm soát - thận trọng',
        'Tiền sử đau thắt ngực - thận trọng',
        'Dùng với SSRI/SNRI - tăng nguy cơ hội chứng serotonin',
        'Dùng với propranolol - giảm liều rizatriptan 50%',
        'Suy thận nặng - thận trọng']},pregnancy_lactation': {'fda_category':
        'C', 'pregnancy_details':
        'Rizatriptan là thuốc phân loại C. Các nghiên cứu trên động vật cho thấy có thể có tác dụng phụ trên thai nhi, nhưng không có nghiên cứu đầy đủ trên người. Rizatriptan được sử dụng trong thai kỳ để điều trị migraine và có vẻ an toàn. Tuy nhiên, có nguy cơ co mạch có thể ảnh hưởng đến thai nhi. Có thể được dùng khi lợi ích vượt quá nguy cơ, nhưng thận trọng.'
        , 'lactation': {'safety': 'Compatible', 'details':
        'Rizatriptan bài tiết vào sữa mẹ với nồng độ thấp. Không có báo cáo về tác dụng phụ ở trẻ bú mẹ.'
        , 'recommendation': 'Có thể dùng an toàn khi cho con bú.'}},hepatic_adjustment': {'mild': 'Không đổi', 'moderate':
        'Thận trọng - rizatriptan chuyển hóa qua gan (MAO-A, CYP2D6), có thể tích lũy'
        , 'severe': 'Thận trọng - có thể tích lũy, tăng tác dụng phụ', 'notes':
        'Rizatriptan chuyển hóa qua gan (MAO-A, một phần CYP2D6). Ở suy gan, có thể tích lũy và tăng tác dụng phụ. Theo dõi chặt chẽ tác dụng phụ. Có thể cần giảm liều.'},overdose_management': {'symptoms': ['Co mạch nghiêm trọng',
        'Nhồi máu cơ tim', 'Đột quỵ', 'Thiếu máu cục bộ', 'Đau ngực nặng',
        'Khó thở nặng', 'Tăng huyết áp nghiêm trọng',
        'Hội chứng serotonin (nếu dùng với SSRI/SNRI)', 'Kích động, lú lẫn'],antidote':
        'Không có antidote đặc hiệu. Nitroglycerin có thể được dùng để giãn mạch, nhưng thận trọng.'
        , 'treatment': ['Ngừng ngay rizatriptan',
        'Hỗ trợ hô hấp nếu cần (oxy, thở máy nếu suy hô hấp)',
        'Theo dõi tim mạch liên tục (ECG, huyết áp, SpO2)',
        'Điều trị nhồi máu cơ tim nếu có (theo protocol)',
        'Điều trị đột quỵ nếu có (theo protocol)',
        'Nitroglycerin để giãn mạch (thận trọng, có thể gây hạ huyết áp)',
        'Điều trị hội chứng serotonin nếu có (dantrolene, benzodiazepine)',
        'Hỗ trợ tim mạch nếu cần (IV fluids, vasopressors nếu hạ huyết áp)',
        'Theo dõi và điều trị triệu chứng'],
        'monitoring':
        'Theo dõi liên tục: ECG, huyết áp, SpO2, dấu hiệu co mạch, dấu hiệu nhồi máu cơ tim, dấu hiệu đột quỵ, dấu hiệu hội chứng serotonin. Theo dõi ít nhất 24 giờ do thời gian bán thải (2-3 giờ) và nguy cơ biến chứng.'
        },reversal_agents': {'available': True, 'agents': [{'agent':
        'Nitroglycerin', 'mechanism': 'Giãn mạch, đối kháng tác dụng co mạch',
        'indication': 'Quá liều gây co mạch nghiêm trọng, đau ngực', 'caution':
        'Thận trọng, có thể gây hạ huyết áp. Chỉ dùng khi có co mạch nghiêm trọng.'}],notes':
        'Không có antidote đặc hiệu. Nitroglycerin có thể được dùng để giãn mạch trong trường hợp quá liều nghiêm trọng, nhưng thận trọng. Điều trị chủ yếu là hỗ trợ và điều trị triệu chứng.'},administration_instructions': {'oral': {'with_food':
        'Có thể uống với hoặc không thức ăn', 'timing':
        'Dùng ngay khi có triệu chứng migraine. Không dùng để phòng ngừa. Có thể lặp sau 2 giờ nếu cần (tối đa 30mg/ngày). Nếu dùng với propranolol: giảm liều 50% (5mg thay vì 10mg).'
        },iv': None, 'odt': {'technique':
        'Dạng ODT (orally disintegrating tablet): Đặt trên lưỡi, để tan tự nhiên, không cần nước. Nuốt nước bọt sau khi tan.'
        , 'timing':
        'Dùng ngay khi có triệu chứng migraine. Có thể lặp sau 2 giờ nếu cần (tối đa 30mg/ngày). Nếu dùng với propranolol: giảm liều 50% (5mg thay vì 10mg).'
        , 'notes':
        'Thuận tiện hơn dạng uống thông thường, không cần nước. Bảo quản trong bao bì kín, tránh ẩm.'}},references': {'primary_sources': ['FDA Label: Maxalt (Rizatriptan)',
        'UpToDate: Triptans for acute migraine',
        'American Headache Society Guidelines',
        "Goodman & Gilman's The Pharmacological Basis of Therapeutics",
        'Micromedex: Rizatriptan'],evidence_level':
        'High - FDA approved, multiple RCTs, clinical guidelines'}},
    
    "Sumatriptan": {'group': 'Analgesic - Antimigraine (5-HT1 Receptor Agonist)',
        "pregnancy": "C - Nguy cơ không thể loại trừ. Thận trọng trong thai kỳ",
        'vietnamese_name': 'Sumatriptan, Imitrex', 'administration': ['PO',
        'SC', 'Nasal'],
        'indications': [
        'Migraine có tiền triệu (aura) hoặc không', 'Cluster headache'],
        'contraindications': ['Bệnh mạch vành', 'Nhồi máu cơ tim',
        'Đau thắt ngực không ổn định', 'Đột quỵ, TIA',
        'Bệnh mạch máu ngoại biên', 'Tăng huyết áp không kiểm soát',
        'Dùng MAO inhibitor trong 14 ngày', 'Dùng ergotamine trong 24 giờ'],
        'dosage': {'adult_po':
        '25-100mg, có thể lặp sau 2 giờ (tối đa 200mg/ngày)', 'adult_sc':
        '6mg SC, có thể lặp sau 1 giờ (tối đa 12mg/ngày)', 'adult_nasal':
        '5-20mg xịt mũi, có thể lặp sau 2 giờ (tối đa 40mg/ngày)', 'notes':
        'Dùng ngay khi có triệu chứng migraine. Không dùng để phòng ngừa'},
        'renal_adjustment': {'normal': 'Không đổi', '30_60': 'Không đổi',
        'under_30': 'Thận trọng'},
        'side_effects': [
        'Cảm giác nóng, đỏ, ngứa (SC injection)',
        'Đau ngực, khó thở (tương tự đau thắt ngực)', 'Nhức đầu', 'Chóng mặt',
        'Buồn nôn', 'Co thắt cơ', 'Yếu, mệt mỏi',
        'Nguy cơ đau tim (hiếm nhưng nguy hiểm)'],
        'interactions': [
        'Ergotamine/Dihydroergotamine: chống chỉ định (trong 24 giờ)',
        'MAO inhibitor: chống chỉ định (trong 14 ngày)',
        'SSRI/SNRI: tăng nguy cơ hội chứng serotonin',
        'Thuốc ức chế CYP2D6: tăng nồng độ sumatriptan'],
        'mechanism_of_action':
        '5-HT1B/1D receptor agonist (selective serotonin receptor agonist, triptan). Kích thích 5-HT1B receptors ở mạch máu não → co mạch (giảm giãn mạch trong migraine). Kích thích 5-HT1D receptors → ức chế phóng thích chất trung gian gây viêm (CGRP, substance P) từ dây thần kinh trigeminal. Giảm đau migraine thông qua cả hai cơ chế: co mạch và ức chế viêm thần kinh. Tác dụng nhanh (10-30 phút SC, 30-60 phút PO).'
        , 'monitoring': ['Đáp ứng lâm sàng (giảm đau migraine, triệu chứng)',
        'Dấu hiệu co mạch: đau ngực, khó thở, đau cổ, hàm (có thể giống đau thắt ngực)'
        , 'Dấu hiệu bệnh mạch vành: đau ngực, khó thở, đau lan (nguy hiểm)',
        'Huyết áp (có thể tăng nhẹ)',
        'Dấu hiệu hội chứng serotonin: kích động, tăng thân nhiệt, tăng phản xạ (nếu dùng với SSRI/SNRI)'
        , 'Dấu hiệu quá liều: co mạch nặng, thiếu máu cục bộ'],
        'precautions':
        ['Dùng ngay khi có triệu chứng migraine (không chờ đến khi đau nặng)',
        'Không dùng để phòng ngừa - chỉ dùng để cắt cơn',
        'CHỐNG CHỈ ĐỊNH trong bệnh mạch vành, nhồi máu cơ tim, đột quỵ, TIA, bệnh mạch máu ngoại biên'
        , 'CHỐNG CHỈ ĐỊNH trong tăng huyết áp không kiểm soát',
        'Không dùng với ergotamine/dihydroergotamine trong 24 giờ - tăng nguy cơ co mạch nặng'
        'Không dùng với MAO inhibitor trong 14 ngày - tăng nguy cơ tác dụng phụ',
        'Thận trọng khi dùng với SSRI/SNRI - tăng nguy cơ hội chứng serotonin',
        'Nếu đau ngực, khó thở → ngừng ngay và đánh giá',
        'Không vượt quá liều tối đa (200mg/ngày PO, 12mg/ngày SC, 40mg/ngày nasal)'
        'Nếu không đáp ứng sau 2 liều → không dùng thêm, đánh giá lại chẩn đoán'
        ],onset':
        'SC: 10-15 phút; PO: 30-60 phút; Nasal: 15-30 phút', 'duration':
        '2-4 giờ', 'protein_binding': '14-21%', 'metabolism':
        'Gan (chuyển hóa qua MAO-A, một phần qua CYP2D6)', 'clearance':
        'Gan (chuyển hóa), thận (thải trừ)'},storage':
        'Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm, tránh ánh sáng. Dạng SC: bảo quản trong tủ lạnh, để ở nhiệt độ phòng trước khi dùng.'
        , 'black_box_warnings':
        'Nguy cơ co mạch nghiêm trọng, có thể gây nhồi máu cơ tim, đột quỵ, thiếu máu cục bộ, có thể tử vong. CHỐNG CHỈ ĐỊNH trong bệnh mạch vành, nhồi máu cơ tim, đột quỵ, TIA, bệnh mạch máu ngoại biên, tăng huyết áp không kiểm soát. Không dùng với ergotamine trong 24 giờ. Nếu có đau ngực, khó thở → ngừng ngay và đánh giá.'
        , 'drug_interactions': {'major': [{'drug':
        'Ergotamine, Dihydroergotamine', 'mechanism':
        'Cả hai đều gây co mạch, tăng nguy cơ co mạch nghiêm trọng', 'effect':
        'Tăng nguy cơ co mạch nghiêm trọng, nhồi máu cơ tim, đột quỵ, thiếu máu cục bộ'
        , 'management':
        'CHỐNG CHỈ ĐỊNH - không dùng với ergotamine/dihydroergotamine trong 24 giờ.'
        }, {'drug': 'MAO Inhibitors (Phenelzine, Tranylcypromine)', 'mechanism':
        'Ức chế MAO-A (chuyển hóa sumatriptan), tăng nồng độ sumatriptan',
        'effect': 'Tăng nguy cơ tác dụng phụ, co mạch nghiêm trọng',
        'management':
        'CHỐNG CHỈ ĐỊNH - không dùng với MAO inhibitor trong 14 ngày.'}],
        'moderate': [{'drug': 'SSRI/SNRI (Fluoxetine, Sertraline, Venlafaxine)',
        'mechanism':
        'Cả hai đều tăng serotonin, tăng nguy cơ hội chứng serotonin', 'effect':
        'Tăng nguy cơ hội chứng serotonin (kích động, tăng thân nhiệt, tăng phản xạ)'
        , 'management':
        'Thận trọng, theo dõi dấu hiệu hội chứng serotonin. Có thể cần tránh dùng cùng.'
        }, {'drug': 'Thuốc ức chế CYP2D6', 'mechanism':
        'Giảm chuyển hóa sumatriptan, tăng nồng độ', 'effect':
        'Tăng tác dụng phụ, tăng nguy cơ co mạch', 'management':
        'Thận trọng, theo dõi tác dụng phụ. Có thể cần giảm liều sumatriptan.'}
        ],minor': []},contraindications': {'tuyệt_đối': [
        'Dị ứng với sumatriptan hoặc các thành phần khác',
        'Bệnh mạch vành (CAD)', 'Nhồi máu cơ tim',
        'Đau thắt ngực không ổn định', 'Đột quỵ, TIA',
        'Bệnh mạch máu ngoại biên', 'Tăng huyết áp không kiểm soát',
        'Dùng MAO inhibitor trong 14 ngày',
        'Dùng ergotamine/dihydroergotamine trong 24 giờ'],
        'tương_đối': [
        'Bệnh tim mạch khác (suy tim, loạn nhịp) - thận trọng, đánh giá tim mạch trước'
        , 'Tăng huyết áp đã kiểm soát - thận trọng',
        'Tiền sử đau thắt ngực - thận trọng',
        'Dùng với SSRI/SNRI - tăng nguy cơ hội chứng serotonin',
        'Suy thận nặng - thận trọng']},pregnancy_lactation': {'fda_category':
        'C', 'pregnancy_details':
        'Sumatriptan là thuốc phân loại C. Các nghiên cứu trên động vật cho thấy có thể có tác dụng phụ trên thai nhi, nhưng không có nghiên cứu đầy đủ trên người. Sumatriptan được sử dụng trong thai kỳ để điều trị migraine và có vẻ an toàn. Tuy nhiên, có nguy cơ co mạch có thể ảnh hưởng đến thai nhi. Có thể được dùng khi lợi ích vượt quá nguy cơ, nhưng thận trọng.'
        , 'lactation': {'safety': 'Compatible', 'details':
        'Sumatriptan bài tiết vào sữa mẹ với nồng độ thấp. Không có báo cáo về tác dụng phụ ở trẻ bú mẹ.'
        , 'recommendation': 'Có thể dùng an toàn khi cho con bú.'}},hepatic_adjustment': {'mild': 'Không đổi', 'moderate':
        'Thận trọng - sumatriptan chuyển hóa qua gan (MAO-A, CYP2D6), có thể tích lũy'
        , 'severe': 'Thận trọng - có thể tích lũy, tăng tác dụng phụ', 'notes':
        'Sumatriptan chuyển hóa qua gan (MAO-A, một phần CYP2D6). Ở suy gan, có thể tích lũy và tăng tác dụng phụ. Theo dõi chặt chẽ tác dụng phụ. Có thể cần giảm liều.'
        },overdose_management': {'symptoms': ['Co mạch nghiêm trọng',
        'Nhồi máu cơ tim', 'Đột quỵ', 'Thiếu máu cục bộ', 'Đau ngực nặng',
        'Khó thở nặng', 'Tăng huyết áp nghiêm trọng',
        'Hội chứng serotonin (nếu dùng với SSRI/SNRI)', 'Kích động, lú lẫn'],antidote':
        'Không có antidote đặc hiệu. Nitroglycerin có thể được dùng để giãn mạch, nhưng thận trọng.'
        , 'treatment': ['Ngừng ngay sumatriptan',
        'Hỗ trợ hô hấp nếu cần (oxy, thở máy nếu suy hô hấp)',
        'Theo dõi tim mạch liên tục (ECG, huyết áp, SpO2)',
        'Điều trị nhồi máu cơ tim nếu có (theo protocol)',
        'Điều trị đột quỵ nếu có (theo protocol)',
        'Nitroglycerin để giãn mạch (thận trọng, có thể gây hạ huyết áp)',
        'Điều trị hội chứng serotonin nếu có (dantrolene, benzodiazepine)',
        'Hỗ trợ tim mạch nếu cần (IV fluids, vasopressors nếu hạ huyết áp)',
        'Theo dõi và điều trị triệu chứng'],
        'monitoring':
        'Theo dõi liên tục: ECG, huyết áp, SpO2, dấu hiệu co mạch, dấu hiệu nhồi máu cơ tim, dấu hiệu đột quỵ, dấu hiệu hội chứng serotonin. Theo dõi ít nhất 24 giờ do thời gian bán thải (2 giờ) và nguy cơ biến chứng.'
        },reversal_agents': {'available': True, 'agents': [{'agent':
        'Nitroglycerin', 'mechanism': 'Giãn mạch, đối kháng tác dụng co mạch',
        'indication': 'Quá liều gây co mạch nghiêm trọng, đau ngực', 'caution':
        'Thận trọng, có thể gây hạ huyết áp. Chỉ dùng khi có co mạch nghiêm trọng.'
        }],notes':
        'Không có antidote đặc hiệu. Nitroglycerin có thể được dùng để giãn mạch trong trường hợp quá liều nghiêm trọng, nhưng thận trọng. Điều trị chủ yếu là hỗ trợ và điều trị triệu chứng.'
        },administration_instructions': {'oral': {'with_food':
        'Có thể uống với hoặc không thức ăn', 'timing':
        'Dùng ngay khi có triệu chứng migraine. Không dùng để phòng ngừa. Có thể lặp sau 2 giờ nếu cần (tối đa 200mg/ngày).'
        },iv': None, 'sc': {'technique':
        'Dạng SC: Tiêm dưới da, thường ở đùi hoặc cánh tay. Liều: 6mg SC.',
        'timing':
        'Dùng ngay khi có triệu chứng migraine. Có thể lặp sau 1 giờ nếu cần (tối đa 12mg/ngày).'
        , 'notes':
        'Tác dụng nhanh nhất (10-15 phút). Bảo quản trong tủ lạnh, để nhiệt độ phòng trước khi dùng.'
        },nasal': {'technique':
        'Dạng xịt mũi: Xịt vào một bên mũi, nhắm mắt và miệng khi xịt.',
        'timing':
        'Dùng ngay khi có triệu chứng migraine. Có thể lặp sau 2 giờ nếu cần (tối đa 40mg/ngày).'
        , 'notes':
        'Tác dụng nhanh (15-30 phút). Có thể gây vị đắng trong miệng.'}},references': {'primary_sources': ['FDA Label: Imitrex (Sumatriptan)',
        'UpToDate: Triptans for acute migraine',
        'American Headache Society Guidelines',
        "Goodman & Gilman's The Pharmacological Basis of Therapeutics",
        'Micromedex: Sumatriptan'],evidence_level':
        'High - FDA approved, multiple RCTs, clinical guidelines'
        }
}

__all__ = ['ANTIMIGRAINE_5_HT1_RECEPTOR_AGONISTS_DRUGS']
