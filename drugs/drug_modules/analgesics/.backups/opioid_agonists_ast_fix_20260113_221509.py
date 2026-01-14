"""Analgesic and Pain Medications
Active module - contains all analgesic drug data"""

# Opioid Agonists

OPIOID_AGONISTS_DRUGS = {
    "Buprenorphine":     {
        "group": "Analgesic - Opioid Partial Agonist",
        "vietnamese_name": "Buprenorphine, Subutex, Suboxone (với naloxone)",
        "administration": [
            "SL",
            "IV",
            "IM",
            "TD"
    ],
        "indications": [
            "Đau nặng",
            "Cai nghiện opioid (maintenance therapy)",
            "Đau mạn tính"
    ],
        "contraindications": {
            "tuyệt_đối": [
                "Dị ứng buprenorphine hoặc opioid",
                "Ngộ độc cấp tính rượu, thuốc an thần, opioid",
                "Suy hô hấp nặng",
                "Dùng MAO inhibitor trong vòng 14 ngày"
    ],
            "tương_đối": [
                "Suy thận nặng - không cần điều chỉnh liều",
                "Suy gan nặng - thận trọng"
    ],
        },
        "dosage": {
            "adult_pain_sl": "200-400mcg SL mỗi 6-8 giờ",
            "adult_pain_iv_im": "300mcg IV/IM mỗi 6-8 giờ",
            "adult_pain_td": "5-20mcg/giờ TD patch, thay mỗi 7 ngày",
            "adult_maintenance": "2-32mg/ngày SL (cai nghiện opioid)",
            "notes": """Partial agonist - tác dụng giảm đau nhưng ít ức chế hô hấp hơn opioid full agonist. Ceiling effect. Dùng cho cai nghiện opioid.""",
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "Không đổi",
            "under_30": "Không đổi",
        },
        "side_effects": [
            "Buồn nôn, nôn",
            "Táo bón",
            "Buồn ngủ",
            "Ức chế hô hấp (ít hơn morphine)",
            "Nguy cơ nghiện/lệ thuộc (thấp hơn morphine)",
            "Ngứa"
    ],
        "interactions": [
            "Benzodiazepine: tăng nguy cơ ức chế hô hấp",
            "MAO inhibitor: chống chỉ định",
            "CYP3A4 inhibitors: tăng nồng độ buprenorphine"
    ],
        "pregnancy": "C",
        "mechanism_of_action": """Opioid partial agonist (mu-opioid receptor). Gắn với mu-opioid receptor nhưng không kích hoạt hoàn toàn → tác dụng giảm đau nhưng ít ức chế hô hấp hơn opioid full agonist (như morphine). Có ceiling effect (đạt hiệu quả tối đa ở liều nhất định, không tăng thêm khi tăng liều). Buprenorphine cũng là kappa-opioid receptor antagonist. Được dùng cho đau nặng và cai nghiện opioid (maintenance therapy) do nguy cơ nghiện thấp hơn và ít ức chế hô hấp hơn.""",
        "monitoring": [
            "Nhịp thở và độ bão hòa oxy (SpO2) - ít nguy cơ hơn morphine nhưng vẫn cần theo dõi",
            "Mức độ đau",
            "Mức độ ý thức",
            "Dấu hiệu nghiện/lệ thuộc (thấp hơn morphine)"
    ],
        "precautions": [
            "Partial agonist → ít ức chế hô hấp hơn morphine nhưng vẫn có nguy cơ",
            "Ceiling effect → không tăng hiệu quả khi tăng liều quá mức",
            "CHỐNG CHỈ ĐỊNH với MAO inhibitor",
            "Tránh dùng với benzodiazepine, rượu (tăng nguy cơ ức chế hô hấp)",
            "Naloxone ít hiệu quả với buprenorphine (do affinity cao)",
            "Dùng cho cai nghiện: phải được quản lý bởi chương trình điều trị chuyên khoa"
    ],
        "pharmacokinetics": {
            "half_life": "24-60 giờ (dài)",
            "onset": "30-60 phút (SL), 10-15 phút (IV/IM)",
            "duration": "6-8 giờ (đau), dài hơn (cai nghiện)",
            "protein_binding": "96%",
            "clearance": "Gan (chuyển hóa qua CYP3A4), thận (thải trừ)",
        },
        "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm. Bảo quản an toàn, tránh xa tầm tay trẻ em.",
        "black_box_warnings": """Nguy cơ nghiện, lạm dụng, và lệ thuộc (thấp hơn morphine). Nguy cơ ức chế hô hấp (ít hơn morphine nhưng vẫn có). Naloxone ít hiệu quả với buprenorphine do affinity cao.""",
        "drug_interactions": {
            "major": [
    {
                    "drug": "Benzodiazepine, thuốc an thần, rượu",
                    "mechanism": "Tăng ức chế hệ thần kinh trung ương",
                    "effect": "Tăng nguy cơ ức chế hô hấp nặng",
                    "management": "TRÁNH DÙNG ĐỒNG THỜI. Nếu phải dùng, theo dõi hô hấp chặt chẽ.",
                },
    {
                    "drug": "MAO inhibitors",
                    "mechanism": "Tăng nguy cơ phản ứng nghiêm trọng",
                    "effect": "Nguy cơ phản ứng nghiêm trọng",
                    "management": "CHỐNG CHỈ ĐỊNH.",
                }
                ],
            "moderate": [],
            "minor": [],
        },
        "pregnancy_lactation": {
            "fda_category": "C",
            "pregnancy_details": """Category C. Có thể dùng nếu lợi ích > nguy cơ. Khi dùng cho cai nghiện opioid trong thai kỳ: có thể giảm nguy cơ hội chứng cai ở trẻ sơ sinh.""",
            "lactation": {
                "safety": "Caution",
                "details": "Buprenorphine bài tiết vào sữa mẹ. Có thể gây tác dụng phụ ở trẻ.",
                "recommendation": "Thận trọng khi cho con bú.",
            },
        },
        "hepatic_adjustment": {
            "mild": "Không đổi",
            "moderate": "Thận trọng",
            "severe": "Thận trọng (chuyển hóa qua gan)",
            "notes": "Buprenorphine chuyển hóa ở gan qua CYP3A4. Suy gan có thể ảnh hưởng đến chuyển hóa.",
        },
        "overdose_management": {
            "symptoms": [
                "Ức chế hô hấp nặng (ít hơn morphine nhưng vẫn có)",
                "Buồn ngủ sâu, hôn mê",
                "Đồng tử co nhỏ (miosis)",
                "Hạ huyết áp"
    ],
            "antidote": "Naloxone (Narcan) - nhưng ít hiệu quả hơn với morphine do buprenorphine có affinity cao",
            "treatment": [
                "Đánh giá đường thở, hô hấp, tuần hoàn. Hỗ trợ hô hấp ngay lập tức",
                "Naloxone: 0.4-2mg IV/IM/SC, có thể lặp lại, nhưng có thể cần liều cao hơn do affinity buprenorphine cao",
                "Theo dõi liên tục: ý thức, hô hấp (nhịp thở, SpO2), tim mạch",
                "Hỗ trợ hô hấp: thở máy nếu suy hô hấp nặng",
                "Theo dõi ít nhất 24 giờ do half-life dài"
    ],
            "monitoring": """Theo dõi liên tục: ý thức, hô hấp (nhịp thở, SpO2), tim mạch. Theo dõi ít nhất 24 giờ do half-life dài.""",
        },
        "reversal_agents": {
            "available": True,
            "agents": [
    {
                    "agent": "Naloxone (Narcan)",
                    "mechanism": "Opioid antagonist",
                    "indication": "Quá liều buprenorphine",
                    "dose": "0.4-2mg IV/IM/SC, có thể lặp lại, nhưng có thể cần liều cao hơn",
                    "caution": "Naloxone ít hiệu quả với buprenorphine do buprenorphine có affinity cao với mu-opioid receptor.",
                }
                ],
        },
        "administration_instructions": {
            "sublingual": {
                "with_food": "Đặt dưới lưỡi, để tan tự nhiên. Không nuốt.",
                "timing": """Đau: 200-400mcg SL mỗi 6-8 giờ. Cai nghiện: 2-32mg/ngày SL, phải được quản lý bởi chương trình điều trị chuyên khoa.""",
            },
            "iv": {
                "reconstitution": "Pha với NS hoặc D5W",
                "infusion_rate": "Tiêm IV chậm (2-3 phút)",
                "compatibility": [
                    "NS",
                    "D5W"
    ],
                "incompatibility": [],
                "notes": "300mcg IV/IM mỗi 6-8 giờ. Theo dõi hô hấp chặt chẽ.",
            },
        },
        "references": {
            "primary_sources": [
                "FDA Drug Label - Buprenorphine (Subutex, Suboxone)",
                "UpToDate - Buprenorphine: Drug information",
                "SAMHSA Guidelines"
    ],
            "last_updated": "2025-02-18",
            "evidence_level": "High - FDA-approved",
        },
        "contraindications_detail": {
            "tuyệt_đối": [
                "Dị ứng với buprenorphine hoặc opioid",
                "Suy hô hấp nặng không có hỗ trợ thở máy",
                "Đang dùng MAO inhibitors (trong vòng 14 ngày)"
    ],
            "tương_đối": [
                "Suy hô hấp mạn tính, COPD nặng",
                "Suy gan nặng (giảm chuyển hóa)",
                "Tăng áp lực nội sọ",
                "Phụ nữ có thai (category C)"
    ],
        },
            "risk_flags": {
                "high_alert": True,
                "narrow_therapeutic_index": False,
                "bleeding_risk": False,
                "organ_toxicity": [],
                "qt_prolongation": False,
                "hepatotoxicity": False,
                "nephrotoxicity": False,
                "requires_monitoring": ["Respiratory rate", "Sedation", "Constipation"],
            },
            "guideline_tags": [
                "CDC 2022 Opioid Prescribing Guidelines",
                "FDA Black Box Warning - Opioid addiction, abuse, misuse",
            ]
    },
    "Hydrocodone": {'group': 'Analgesic - Opioid Agonist',
        "pregnancy": "C - Nguy cơ không thể loại trừ. Tránh trong thai kỳ nếu có thể",
        'vietnamese_name': 'Hydrocodone, Vicodin (với acetaminophen)',
        'administration': ['PO'],
        'indications': [
        'Đau trung bình đến nặng',
        'Ho (dạng syrup, liều thấp)'],
        'contraindications': [
        'Ngộ độc cấp tính rượu, thuốc an thần, opioid',
        'Suy hô hấp nặng', 'Tắc ruột', 'Dị ứng'],
        'dosage': {
        'adult_pain': '5-10mg mỗi 4-6 giờ (thường kết hợp với acetaminophen)',
        'adult_max': '60mg/ngày', 'adult_cough':
        '5mg mỗi 4-6 giờ (dạng syrup)', 'notes':
        'Opioid yếu đến trung bình. Thường dùng kết hợp với acetaminophen (Vicodin) hoặc ibuprofen. Có tác dụng giảm ho ở liều thấp.'
        },
        'renal_adjustment': {'normal': 'Không đổi', '30_60': 'Thận trọng',
        'under_30': 'Giảm liều 25-50%'},
        'side_effects': [
        'Buồn nôn, nôn', 'Chóng mặt', 'Buồn ngủ', 'Táo bón',
        'Ức chế hô hấp (liều cao)', 'Nguy cơ nghiện/lệ thuộc',
        'Ngộ độc gan (nếu dùng với acetaminophen liều cao)'],
        'interactions': [
        'Thuốc an thần: tăng tác dụng an thần và ức chế hô hấp',
        'MAO inhibitor: tăng nguy cơ phản ứng nghiêm trọng',
        'CYP2D6 inhibitors: giảm chuyển hóa thành hydromorphone (active metabolite)'
        ],
        'mechanism_of_action':
        'Opioid mu-receptor agonist, tác dụng yếu đến trung bình (mạnh hơn codeine nhưng yếu hơn morphine). Hydrocodone được chuyển hóa qua CYP2D6 thành hydromorphone (active metabolite mạnh hơn). Giảm đau thông qua kích thích opioid receptors ở não và tủy sống. Cũng có tác dụng giảm ho ở liều thấp. Thường dùng kết hợp với acetaminophen (Vicodin) hoặc ibuprofen để tăng hiệu quả và giảm liều opioid. Nguy cơ nghiện/lệ thuộc, đặc biệt khi dùng kéo dài.'
        , 'monitoring': [
        'Mức độ đau (thang điểm đau)',
        'Nhịp thở và độ bão hòa oxy (SpO2) - nguy cơ ức chế hô hấp',
        'Mức độ ý thức',
        'Dấu hiệu nghiện/lệ thuộc',
        'Chức năng gan (nếu dùng với acetaminophen)',
        'Chức năng thận (điều chỉnh liều ở suy thận nặng)'],
        'precautions': [
        'Nguy cơ ức chế hô hấp - đặc biệt ở liều cao, người cao tuổi, suy hô hấp',
        'Nguy cơ nghiện/lệ thuộc - chỉ dùng khi thực sự cần thiết, không dùng kéo dài'
        'Không dùng với rượu, benzodiazepine, thuốc an thần (tăng nguy cơ ức chế hô hấp)'
        'Ngộ độc gan - nếu dùng với acetaminophen, không vượt quá 4g acetaminophen/ngày'
        , 'Giảm liều ở suy thận nặng (CrCl < 30)',
        'Giảm liều ở suy gan nặng (giảm chuyển hóa)',
        'Người cao tuổi: giảm liều (tăng nhạy cảm)',
        'Không dùng cho trẻ em < 12 tuổi (nguy cơ ức chế hô hấp)',
        'Thận trọng với CYP2D6 poor metabolizers (giảm hiệu quả)'],
        'pharmacokinetics': {
        'half_life': '3.8 giờ (hydrocodone), 2.6 giờ (hydromorphone metabolite)',
        'onset': '30-60 phút (PO)', 'duration': '4-6 giờ', 'protein_binding':
        '36%', 'clearance': 'Gan (chuyển hóa qua CYP2D6 và CYP3A4), thận (thải trừ)', 'metabolism':
        'Gan (CYP2D6 → hydromorphone active metabolite, CYP3A4 → norhydrocodone), thận (thải trừ)'
        },storage':
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
        'TRÁNH DÙNG với MAO inhibitor.'}],
        'moderate': [{'drug':
        'CYP2D6 inhibitors (paroxetine, fluoxetine, quinidine)', 'mechanism':
        'Ức chế chuyển hóa hydrocodone thành hydromorphone', 'effect':
        'Giảm hiệu quả giảm đau (giảm active metabolite)', 'management':
        'Có thể cần tăng liều hydrocodone hoặc dùng opioid khác không phụ thuộc CYP2D6.'
        }, {'drug': 'CYP3A4 inhibitors (ketoconazole, clarithromycin)',
        'mechanism': 'Ức chế chuyển hóa hydrocodone', 'effect':
        'Tăng nồng độ hydrocodone, tăng tác dụng phụ', 'management':
        'Giảm liều hydrocodone. Theo dõi tác dụng phụ.'}],
        'minor': []},contraindications': {'tuyệt_đối': [
        'Dị ứng hydrocodone hoặc opioid',
        'Ngộ độc cấp tính rượu, thuốc an thần, opioid',
        'Suy hô hấp nặng',
        'Tắc ruột',
        'Dùng với MAO inhibitor'],
        'tương_đối': [
        'Suy hô hấp nhẹ đến trung bình - thận trọng, giảm liều',
        'Suy thận nặng (CrCl <30) - giảm liều 25-50%',
        'Suy gan nặng - giảm liều, thận trọng',
        'Người cao tuổi - giảm liều (tăng nhạy cảm)',
        'CYP2D6 poor metabolizers - giảm hiệu quả',
        'Mang thai (category C) - thận trọng, có thể gây withdrawal ở trẻ sơ sinh'
        ],pregnancy_details':
        'Category C. Có thể dùng khi cần thiết nhưng thận trọng. Có thể gây withdrawal ở trẻ sơ sinh nếu dùng gần cuối thai kỳ.'
        , 'lactation': {'safety': 'Compatible with monitoring', 'details':
        'Hydrocodone bài tiết vào sữa mẹ ở nồng độ thấp. Có thể gây tác dụng phụ ở trẻ (buồn ngủ, bú kém).'
        , 'recommendation':
        'Có thể cho con bú nhưng cần theo dõi trẻ về dấu hiệu tác dụng phụ (buồn ngủ, bú kém, ức chế hô hấp).'
        }},
        'hepatic_adjustment': {'mild': 'Không đổi', 'moderate':
        'Thận trọng, giảm liều 25-50%', 'severe':
        'Giảm liều 50%, thận trọng', 'notes':
        'Hydrocodone chuyển hóa ở gan qua CYP2D6 và CYP3A4. Suy gan làm giảm chuyển hóa, tăng nguy cơ tích lũy và tác dụng phụ.'
        },overdose_management': {'symptoms': [
        'Ức chế hô hấp nặng (triệu chứng chính, có thể tử vong)',
        'Buồn ngủ sâu, hôn mê', 'Đồng tử co nhỏ (miosis)',
        'Hạ huyết áp, nhịp tim chậm', 'Táo bón nặng',
        'Ngộ độc gan (nếu dùng với acetaminophen liều cao)'],antidote':
        'Naloxone (Narcan) - opioid antagonist, đảo ngược ức chế hô hấp', 'treatment': [
        'Đánh giá đường thở, hô hấp, tuần hoàn. Hỗ trợ hô hấp ngay lập tức (quan trọng nhất)'
        'Naloxone: 0.4-2mg IV/IM/SC, có thể lặp lại mỗi 2-3 phút nếu cần (tối đa 10mg)'
        'Theo dõi liên tục: ý thức, hô hấp (nhịp thở, SpO2), tim mạch',
        'Hỗ trợ hô hấp: thở máy nếu suy hô hấp nặng',
        'Điều trị hạ huyết áp: truyền dịch, vasopressors nếu cần',
        'Nếu có ngộ độc acetaminophen: điều trị với N-acetylcysteine (NAC)',
        'Theo dõi ít nhất 4-6 giờ sau liều naloxone cuối (do half-life naloxone ngắn hơn hydrocodone)'
        ],
        'monitoring':
        'Theo dõi liên tục: ý thức, hô hấp (nhịp thở, SpO2), tim mạch (huyết áp, nhịp tim), nhiệt độ cơ thể. Theo dõi ít nhất 4-6 giờ sau liều naloxone cuối.'
        },reversal_agents': {'available': True, 'agents': [{'agent':
        'Naloxone (Narcan)', 'mechanism':
        'Opioid antagonist, đảo ngược tác dụng opioid', 'indication':
        'Quá liều opioid gây ức chế hô hấp', 'dose':
        '0.4-2mg IV/IM/SC, có thể lặp lại mỗi 2-3 phút nếu cần (tối đa 10mg)',
        'caution':
        'Half-life ngắn (30-90 phút) nên có thể cần lặp lại. Theo dõi ít nhất 4-6 giờ sau liều cuối.'
        }],notes':
        'Naloxone là antidote đặc hiệu cho quá liều opioid. Đảo ngược ức chế hô hấp nhanh chóng. Tuy nhiên, half-life ngắn nên có thể cần lặp lại.'
        },administration_instructions': {'oral': {'with_food':
        'Có thể uống với thức ăn hoặc không (hấp thu tốt)', 'timing':
        'Mỗi 4-6 giờ. Thường dùng kết hợp với acetaminophen (Vicodin) hoặc ibuprofen. Liều tối đa: 60mg/ngày.'
        },iv': {'reconstitution': 'Không có dạng IV', 'infusion_rate': 'N/A',
        'compatibility': [],incompatibility': []}},references': {'primary_sources': [
        'FDA Drug Label - Vicodin (Hydrocodone/Acetaminophen)',
        'UpToDate - Hydrocodone: Drug information'],evidence_level': 'High - FDA approved'
        },risk_flags': {
            'high_alert': True,
            'narrow_therapeutic_index': False,
            'bleeding_risk': False,
            'organ_toxicity': [],qt_prolongation': False,
            'hepatotoxicity': False,
            'nephrotoxicity': False,
            'requires_monitoring': ['Respiratory rate', 'Sedation', 'Constipation']
        },guideline_tags': [
            'CDC 2022 Opioid Prescribing Guidelines',
            'FDA Black Box Warning - Opioid addiction, abuse, misuse',
            'ISMP High Alert Medications - Opioids'
        ]
    },
    "Tapentadol":     {
        "group": "Analgesic - Opioid Agonist (Dual Mechanism)",
        "vietnamese_name": "Tapentadol, Nucynta",
        "administration": [
            "PO"
    ],
        "indications": [
            "Đau trung bình đến nặng",
            "Đau mạn tính",
            "Đau sau phẫu thuật",
            "Đau do ung thư"
    ],
        "contraindications": {
            "tuyệt_đối": [
                "Dị ứng tapentadol hoặc opioid",
                "Ngộ độc cấp tính rượu, thuốc an thần, opioid",
                "Suy hô hấp nặng",
                "Dùng MAO inhibitor trong vòng 14 ngày",
                "Tắc ruột cơ học",
                "Suy gan nặng",
                "Trẻ em <18 tuổi"
    ],
            "tương_đối": [
                "Suy thận nặng - không khuyến cáo",
                "Suy gan trung bình - thận trọng"
    ],
        },
        "dosage": {
            "adult_po": "50-100mg mỗi 4-6 giờ (tối đa 600mg/ngày)",
            "adult_elderly": "Liều thấp hơn (50mg mỗi 6 giờ)",
            "notes": """Opioid mu-receptor agonist + norepinephrine reuptake inhibitor. Ít tác dụng phụ hơn morphine. Ít táo bón hơn.""",
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "Thận trọng, có thể giảm liều",
            "under_30": "Không khuyến cáo",
        },
        "side_effects": [
            "Buồn nôn, nôn",
            "Chóng mặt",
            "Buồn ngủ",
            "Ức chế hô hấp (ít hơn morphine)",
            "Táo bón (ít hơn morphine)",
            "Nguy cơ nghiện/lệ thuộc (thấp hơn morphine)"
    ],
        "interactions": [
            "MAO inhibitor: chống chỉ định",
            "SSRI/SNRI: tăng nguy cơ hội chứng serotonin",
            "Benzodiazepine: tăng nguy cơ ức chế hô hấp"
    ],
        "pregnancy": "C",
        "mechanism_of_action": """Opioid mu-receptor agonist + norepinephrine reuptake inhibitor. Tác dụng kép: (1) Opioid mu-receptor agonist → giảm đau giống morphine, (2) Norepinephrine reuptake inhibitor → tăng norepinephrine → tăng tác dụng giảm đau. Kết quả: hiệu quả giảm đau tương đương morphine nhưng ít tác dụng phụ hơn (ít ức chế hô hấp, ít táo bón, ít nghiện). Thuốc mới, được dùng cho đau trung bình đến nặng.""",
        "monitoring": [
            "Nhịp thở và độ bão hòa oxy (SpO2) - ít nguy cơ hơn morphine nhưng vẫn cần theo dõi",
            "Mức độ đau",
            "Mức độ ý thức",
            "Dấu hiệu hội chứng serotonin (khi dùng với SSRI/SNRI)"
    ],
        "precautions": [
            "Ít tác dụng phụ hơn morphine (ít ức chế hô hấp, ít táo bón)",
            "CHỐNG CHỈ ĐỊNH với MAO inhibitor",
            "Thận trọng với SSRI/SNRI (nguy cơ hội chứng serotonin)",
            "Tránh dùng với benzodiazepine, rượu (tăng nguy cơ ức chế hô hấp)",
            "Nguy cơ nghiện/lệ thuộc thấp hơn morphine nhưng vẫn có",
            "Không dùng cho trẻ em <18 tuổi"
    ],
        "pharmacokinetics": {
            "half_life": "4 giờ",
            "onset": "30-60 phút (PO)",
            "duration": "4-6 giờ",
            "protein_binding": "20%",
            "clearance": "Gan (chuyển hóa qua glucuronidation, không qua CYP450), thận (thải trừ)",
        },
        "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm. Bảo quản an toàn, tránh xa tầm tay trẻ em.",
        "black_box_warnings": """Nguy cơ nghiện, lạm dụng, và lệ thuộc (thấp hơn morphine). Nguy cơ ức chế hô hấp (ít hơn morphine nhưng vẫn có).""",
        "drug_interactions": {
            "major": [
    {
                    "drug": "MAO inhibitors",
                    "mechanism": "Tăng nguy cơ phản ứng nghiêm trọng",
                    "effect": "Nguy cơ phản ứng nghiêm trọng",
                    "management": "CHỐNG CHỈ ĐỊNH.",
                },
    {
                    "drug": "SSRI/SNRI",
                    "mechanism": "Tăng nồng độ serotonin",
                    "effect": "Tăng nguy cơ hội chứng serotonin",
                    "management": "Thận trọng. Theo dõi dấu hiệu hội chứng serotonin.",
                }
                ],
            "moderate": [],
            "minor": [],
        },
        "pregnancy_lactation": {
            "fda_category": "C",
            "pregnancy_details": "Category C. Có thể dùng nếu lợi ích > nguy cơ.",
            "lactation": {
                "safety": "Caution",
                "details": "Tapentadol bài tiết vào sữa mẹ. Có thể gây tác dụng phụ ở trẻ.",
                "recommendation": "Thận trọng khi cho con bú.",
            },
        },
        "hepatic_adjustment": {
            "mild": "Không đổi",
            "moderate": "Thận trọng",
            "severe": "CHỐNG CHỈ ĐỊNH",
            "notes": "Tapentadol chuyển hóa ở gan qua glucuronidation. Suy gan nặng là chống chỉ định.",
        },
        "overdose_management": {
            "symptoms": [
                "Ức chế hô hấp nặng (ít hơn morphine nhưng vẫn có)",
                "Buồn ngủ sâu, hôn mê",
                "Đồng tử co nhỏ (miosis)",
                "Hạ huyết áp",
                "Hội chứng serotonin (nếu dùng với SSRI/SNRI)"
    ],
            "antidote": "Naloxone (Narcan) - opioid antagonist, đảo ngược tác dụng opioid",
            "treatment": [
                "Đánh giá đường thở, hô hấp, tuần hoàn. Hỗ trợ hô hấp ngay lập tức",
                "Naloxone: 0.4-2mg IV/IM/SC, có thể lặp lại mỗi 2-3 phút",
                "Nếu hội chứng serotonin: cyproheptadine",
                "Theo dõi liên tục: ý thức, hô hấp (nhịp thở, SpO2), tim mạch",
                "Hỗ trợ hô hấp: thở máy nếu suy hô hấp nặng"
    ],
            "monitoring": """Theo dõi liên tục: ý thức, hô hấp (nhịp thở, SpO2), tim mạch. Theo dõi ít nhất 4-6 giờ sau liều naloxone cuối.""",
        },
        "reversal_agents": {
            "available": True,
            "agents": [
    {
                    "agent": "Naloxone (Narcan)",
                    "mechanism": "Opioid antagonist, đảo ngược tác dụng opioid",
                    "indication": "Quá liều tapentadol gây ức chế hô hấp",
                    "dose": "0.4-2mg IV/IM/SC, có thể lặp lại mỗi 2-3 phút",
                }
                ],
        },
        "administration_instructions": {
            "oral": {
                "with_food": "Có thể uống với thức ăn hoặc không",
                "timing": "50-100mg mỗi 4-6 giờ. Liều tối đa: 600mg/ngày. Người cao tuổi: 50mg mỗi 6 giờ.",
            },
        },
        "references": {
            "primary_sources": [
                "FDA Drug Label - Tapentadol (Nucynta)",
                "UpToDate - Tapentadol: Drug information"
    ],
            "last_updated": "2025-02-18",
            "evidence_level": "High - FDA-approved",
        },
            "risk_flags": {
                "high_alert": True,
                "narrow_therapeutic_index": False,
                "bleeding_risk": False,
                "organ_toxicity": [],
                "qt_prolongation": False,
                "hepatotoxicity": False,
                "nephrotoxicity": False,
                "requires_monitoring": ["Respiratory rate", "Sedation", "Constipation"],
            },
            "guideline_tags": [
                "CDC 2022 Opioid Prescribing Guidelines",
                "FDA Black Box Warning - Opioid addiction, abuse, misuse",
            ]
    },
}
