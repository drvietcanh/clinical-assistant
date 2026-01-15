"""Gastrointestinal Drugs
Active module - contains all gastrointestinal drug data"""

# Antiemetic (5-HT3 Antagonist)s

ANTIEMETIC_5_HT3_ANTAGONISTS_DRUGS = {
    "Ondansetron": {'group': 'Gastrointestinal - Antiemetic (5-HT3 Antagonist)',
        "pregnancy": "B - Không có bằng chứng về nguy cơ ở người. Sử dụng phổ biến trong thai kỳ",
        'vietnamese_name': 'Ondansetron, Zofran', 'administration': ['PO', 'IV',
        'IM'],
        'indications': [
        'Buồn nôn, nôn sau phẫu thuật', 'Buồn nôn, nôn do xạ trị',
        'Buồn nôn, nôn do nhiều nguyên nhân'],
        'contraindications': [
        'Dị ứng ondansetron', 'QT kéo dài', 'Dùng với apomorphine'],
        'dosage':
        {'adult_po': '8mg x 2-3 lần/ngày', 'adult_iv_im':
        '4-8mg x 2-3 lần/ngày', 'adult_chemotherapy':
        '8mg IV trước hóa trị, sau đó 8mg PO x 2 lần/ngày x 3 ngày',
        'adult_surgery': '4mg IV trước khi gây mê', 'notes':
        'Rất hiệu quả cho buồn nôn do hóa trị và phẫu thuật'},
        'renal_adjustment': {'normal': 'Không đổi', '30_60': 'Không đổi',
        'under_30': 'Không đổi'},
        'side_effects': ['QT kéo dài', 'Nhức đầu',
        'Chóng mặt', 'Táo bón', 'Mệt mỏi'],
        'interactions': [
        'Apomorphine: chống chỉ định',
        'Thuốc QT kéo dài: tăng nguy cơ loạn nhịp',
        'CYP2D6 inhibitors: tăng nồng độ ondansetron'],
        'mechanism_of_action':
        '5-HT3 (serotonin) receptor antagonist. Ức chế chọn lọc receptor 5-HT3 ở ngoại vi (dây thần kinh phế vị) và trung ương (chemoreceptor trigger zone trong area postrema). Ngăn cản tác dụng của serotonin, dẫn đến giảm nôn và buồn nôn. Được dùng trong dự phòng và điều trị nôn do hóa trị, xạ trị, và sau phẫu thuật. Hiệu quả hơn metoclopramide và không gây tác dụng phụ ngoại tháp như metoclopramide.'
        , 'monitoring': ['Tần suất nôn và buồn nôn',
        'ECG (QT kéo dài - nguy cơ rối loạn nhịp tim, đặc biệt ở liều cao)',
        'Điện giải (kali, magie) - hạ kali, hạ magie tăng nguy cơ QT kéo dài',
        'Dấu hiệu tắc ruột (ondansetron có thể che dấu triệu chứng)',
        'Chức năng gan (ALT, AST) - hiếm tăng men gan'],
        'precautions': [
        'QT kéo dài → không dùng ở bệnh nhân có QT kéo dài, rối loạn nhịp tim, hoặc dùng các thuốc kéo dài QT khác'
        'Nguy cơ tăng ở liều cao (> 16mg đơn liều), hạ kali, hạ magie, suy gan',
        'Có thể che dấu triệu chứng tắc ruột - thận trọng ở bệnh nhân có nguy cơ',
        'Giảm liều ở suy gan nặng (giảm chuyển hóa)',
        'Liều thường: 4-8mg (PO/IV), có thể lặp lại mỗi 8 giờ',
        'Liều tối đa: 32mg/ngày (để giảm nguy cơ QT kéo dài)',
        'Có thể dùng trước hóa trị/xạ trị để dự phòng',
        'An toàn trong thai kỳ (category B)'],
        'pharmacokinetics': {'half_life':
        '3-6 giờ (bình thường), kéo dài ở suy gan', 'onset':
        '30 phút (PO), ngay lập tức (IV)', 'duration': '4-8 giờ',
        'protein_binding': '70-76%', 'metabolism':
        'Gan (CYP1A2, CYP2D6, CYP3A4) - chuyển hóa mạnh', 'clearance':
        'Chủ yếu qua gan, cần điều chỉnh ở suy gan'},
        'storage':
        'Bảo quản ở nhiệt độ phòng (20-25°C), tránh ẩm. Dung dịch tiêm: bảo quản ở nhiệt độ phòng, tránh ánh sáng.'
        , 'black_box_warnings':
        'Nguy cơ QT kéo dài, có thể gây rối loạn nhịp tim nghiêm trọng (torsades de pointes), có thể tử vong. Nguy cơ tăng ở liều cao, hạ kali, hạ magie, suy gan, hoặc dùng với các thuốc kéo dài QT khác. Không dùng vượt quá liều khuyến cáo.'
        , 'drug_interactions': {'major': [{'drug': 'Apomorphine', 'mechanism':
        'Ondansetron ức chế 5-HT3 receptor, đối kháng với apomorphine',
        'effect': 'Giảm hiệu quả apomorphine, có thể gây hạ huyết áp nặng',
        'management':
        'CHỐNG CHỈ ĐỊNH dùng cùng. Không dùng ondansetron với apomorphine.'}],
        'moderate': [{'drug':
        'Thuốc kéo dài QT (amiodarone, quinolone, macrolide, haloperidol, etc.)',
        'mechanism': 'Tác dụng hiệp đồng kéo dài QT interval', 'effect':
        'Tăng nguy cơ QT kéo dài, torsades de pointes, loạn nhịp tim',
        'management':
        'Tránh dùng cùng hoặc thận trọng. Theo dõi ECG. Giảm liều ondansetron.'
        }, {'drug': 'CYP2D6 inhibitors (fluoxetine, paroxetine, quinidine)',
        'mechanism': 'Ức chế chuyển hóa ondansetron qua CYP2D6', 'effect':
        'Tăng nồng độ ondansetron, tăng nguy cơ QT kéo dài', 'management':
        'Thận trọng, giảm liều ondansetron nếu cần'}],
        'minor': []},
        'contraindications': {'tuyệt_đối': ['Dị ứng ondansetron',
        'Dùng với apomorphine - CHỐNG CHỈ ĐỊNH tuyệt đối',
        'QT kéo dài (QTc >450ms ở nam, >470ms ở nữ) - CHỐNG CHỈ ĐỊNH'],
        'tương_đối': ['Suy gan nặng - giảm liều 50% (tối đa 8mg/ngày)',
        'Hạ kali, hạ magie - tăng nguy cơ QT kéo dài, bổ sung trước khi dùng',
        'Đang dùng thuốc kéo dài QT - thận trọng, giảm liều',
        'Người già - thận trọng, giảm liều', 'Rối loạn nhịp tim - thận trọng']},
        'pregnancy_lactation': {'fda_category': 'B', 'pregnancy_details':
        'Ondansetron là FDA category B. Nghiên cứu trên động vật không cho thấy nguy cơ cho thai nhi. Một số nghiên cứu trên người không cho thấy tăng nguy cơ dị tật bẩm sinh. Có thể dùng trong thai kỳ nếu lợi ích > nguy cơ. Thường dùng để điều trị buồn nôn, nôn trong thai kỳ (hyperemesis gravidarum).'
        , 'lactation': {'safety': 'Compatible', 'details':
        'Ondansetron bài tiết vào sữa mẹ ở nồng độ thấp. An toàn khi cho con bú.',
        'recommendation': 'Có thể dùng khi cho con bú. Dùng liều thường dùng.'}
        },
        'hepatic_adjustment': {'mild': 'Không cần chỉnh liều', 'moderate':
        'Giảm liều 50% (tối đa 8mg/ngày)', 'severe':
        'Giảm liều 50% (tối đa 8mg/ngày). Ondansetron chuyển hóa ở gan qua CYP1A2, CYP2D6, CYP3A4. Suy gan nặng làm giảm chuyển hóa, tăng nồng độ, tăng nguy cơ QT kéo dài.'
        , 'notes':
        'Ondansetron chuyển hóa ở gan. Suy gan nặng làm tăng nồng độ, tăng nguy cơ QT kéo dài. Giảm liều ở suy gan trung bình và nặng.'
        },
        'overdose_management': {'symptoms': [
        'QT kéo dài, torsades de pointes, loạn nhịp tim (triệu chứng chính, có thể tử vong)'
        , 'Nhức đầu, chóng mặt', 'Buồn nôn, nôn', 'Mệt mỏi'],
        'antidote':
        'Không có antidote đặc hiệu', 'treatment': [
        'Theo dõi ECG liên tục (QT interval)',
        'Điều trị torsades de pointes nếu có: magnesium sulfate 2g IV, pacing nếu cần'
        , 'Bổ sung kali, magie nếu thiếu', 'Hỗ trợ triệu chứng',
        'Theo dõi dấu hiệu sinh tồn chặt chẽ'],
        'monitoring':
        'Theo dõi ECG liên tục (QT interval), dấu hiệu sinh tồn, điện giải'},
        'reversal_agents': None, 'administration_instructions': {'oral': {
        'with_food': 'Có thể uống với hoặc không với thức ăn', 'timing':
        'Uống 30 phút trước hóa trị/xạ trị/phẫu thuật (dự phòng) hoặc ngay khi có buồn nôn. Có thể lặp lại mỗi 8 giờ. Tối đa 32mg/ngày.'
        },
        'iv': {'reconstitution':
        'Ondansetron IV: 4-8mg pha với 50ml NaCl 0.9% hoặc dextrose 5%',
        'infusion_rate': 'Truyền trong 15 phút', 'compatibility': ['NaCl 0.9%',
        'Dextrose 5%'],
        'incompatibility': [
        'Không pha với các thuốc khác trong cùng đường truyền'],
        'notes':
        'Có thể tiêm IV trực tiếp chậm (2-5 phút) hoặc truyền. Chỉ dùng IV khi không uống được. Chuyển sang PO sớm nhất có thể.'
        }},
        'risk_flags': {
            'high_alert': True,
            'narrow_therapeutic_index': False,
            'icu_critical_care_only': False,
            'bleeding_risk': False,
            'organ_toxicity': ['cardiac'],
        'qt_prolongation': True,
            'hepatotoxicity': False,
            'nephrotoxicity': False,
            'requires_monitoring': ['ECG'], 'look_alike_sound_alike': []
        }, 'guideline_tags': [
            'FDA Black Box Warning - Nguy cơ QT kéo dài, có thể gây rối loạn nhịp tim nghiêm trọng (torsades de pointes), có thể tử vong. Nguy cơ tăng ở liều cao, hạ kali, hạ magie, suy gan.',
            'ISMP High Alert Medications',
            'ASCO Guidelines - Antiemetic therapy for chemotherapy-induced nausea and vomiting',
            'WHO Guidelines - Essential medicines for supportive care'
        ],
        'references': {'primary_sources': ['FDA Drug Label - Ondansetron',
        'UpToDate - Ondansetron: Drug information', 'Micromedex - Ondansetron',
        "Goodman & Gilman's The Pharmacological Basis of Therapeutics",
        'FDA Safety Communication - Ondansetron QT prolongation (2012)'],
        'last_updated': '2024-12-19', 'evidence_level':
        'High - FDA approved, multiple RCTs, safety warnings (QT prolongation)'},
        "reversal_agents": {
             "available": False,
             "agents": []
         },
    },
    
    "Granisetron": {
        "group": "Gastrointestinal - Antiemetic (5-HT3 Antagonist)",
        "vietnamese_name": "Granisetron, Kytril",
        "brand_names": {
            "common": ["Kytril", "Sancuso"],
            "vietnam": ["Granisetron 1mg", "Kytril"]
        },
        "administration": ["PO", "IV", "TD"],
        "indications": [
            "Buồn nôn, nôn do hóa trị (chemotherapy-induced nausea and vomiting - CINV)",
            "Buồn nôn, nôn sau phẫu thuật (postoperative nausea and vomiting - PONV)",
            "Buồn nôn, nôn do xạ trị"
        ],
        "contraindications": [
            "Dị ứng granisetron",
            "QT kéo dài (QTc >450ms ở nam, >470ms ở nữ)",
            "Dùng với apomorphine"
        ],
        "dosage": {
            "adult_po": "1-2mg PO x 2 lần/ngày (cách 12 giờ) hoặc 2mg x 1 lần/ngày",
            "adult_iv": "1mg IV x 1 lần trước hóa trị/xạ trị, có thể lặp lại sau 12 giờ nếu cần",
            "adult_transdermal": "Patch 3.1mg/24h, dán 24-48 giờ trước hóa trị, giữ trong 7 ngày",
            "adult_chemotherapy": "1mg IV trước hóa trị, sau đó 1-2mg PO x 2 lần/ngày x 3-5 ngày",
            "pediatric_po": "20mcg/kg PO x 2 lần/ngày (tối đa 2mg/liều)",
            "pediatric_iv": "20mcg/kg IV x 1 lần trước hóa trị (tối đa 1mg/liều)",
            "geriatric_dosing": "Không cần chỉnh liều, nhưng thận trọng ở người già",
            "notes": "Hiệu quả tương đương ondansetron, nhưng thời gian tác dụng dài hơn (24 giờ). Patch transdermal tiện lợi cho hóa trị nhiều ngày."
        },
        "renal_adjustment": {
            "normal": "Không cần chỉnh liều",
            "30_60": "Không cần chỉnh liều",
            "under_30": "Không cần chỉnh liều"
        },
        "side_effects": [
            "Nhức đầu",
            "Táo bón",
            "Chóng mặt",
            "Mệt mỏi",
            "QT kéo dài (ít hơn ondansetron nhưng vẫn có nguy cơ)"
        ],
        "interactions": [
            "Apomorphine: chống chỉ định",
            "Thuốc QT kéo dài: tăng nguy cơ loạn nhịp",
            "CYP3A4 inhibitors: có thể tăng nồng độ granisetron"
        ],
        "pregnancy": "B - Không có bằng chứng về nguy cơ ở người",
        "mechanism_of_action": "5-HT3 receptor antagonist. Tương tự ondansetron nhưng có thời gian bán hủy dài hơn (9-11 giờ), cho phép dùng 1-2 lần/ngày. Ức chế chọn lọc receptor 5-HT3 ở ngoại vi và trung ương, ngăn cản tác dụng của serotonin gây nôn.",
        "monitoring": [
            "Tần suất nôn và buồn nôn",
            "ECG (QT kéo dài - nguy cơ thấp hơn ondansetron nhưng vẫn cần theo dõi)",
            "Điện giải (kali, magie) nếu có nguy cơ QT kéo dài"
        ],
        "precautions": [
            "QT kéo dài → không dùng ở bệnh nhân có QT kéo dài hoặc dùng các thuốc kéo dài QT khác",
            "Nguy cơ QT kéo dài thấp hơn ondansetron nhưng vẫn cần thận trọng",
            "Patch transdermal: kiểm tra da tại vị trí dán, có thể gây kích ứng da",
            "Liều thường: 1-2mg PO/IV, có thể dùng 1-2 lần/ngày",
            "An toàn trong thai kỳ (category B)"
        ],
        "pharmacokinetics": {
            "half_life": "9-11 giờ (dài hơn ondansetron)",
            "onset": "30 phút (PO), ngay lập tức (IV)",
            "duration": "24 giờ (dài hơn ondansetron)",
            "protein_binding": "65%",
            "metabolism": "Gan (CYP3A4) - chuyển hóa chậm hơn ondansetron",
            "clearance": "Chủ yếu qua gan"
        },
        "storage": "Bảo quản ở nhiệt độ phòng (20-25°C), tránh ẩm. Patch: bảo quản ở nhiệt độ phòng, tránh ánh sáng.",
        "black_box_warnings": "Nguy cơ QT kéo dài, có thể gây rối loạn nhịp tim nghiêm trọng. Nguy cơ thấp hơn ondansetron nhưng vẫn cần thận trọng.",
        "drug_interactions": {
            "major": [
                {
                    "drug": "Apomorphine",
                    "mechanism": "Granisetron ức chế 5-HT3 receptor, đối kháng với apomorphine",
                    "effect": "Giảm hiệu quả apomorphine, có thể gây hạ huyết áp nặng",
                    "management": "CHỐNG CHỈ ĐỊNH dùng cùng."
                }
            ],
            "moderate": [
                {
                    "drug": "Thuốc kéo dài QT (amiodarone, quinolone, macrolide)",
                    "mechanism": "Tác dụng hiệp đồng kéo dài QT interval",
                    "effect": "Tăng nguy cơ QT kéo dài, loạn nhịp tim",
                    "management": "Tránh dùng cùng hoặc thận trọng. Theo dõi ECG."
                }
            ],
            "minor": []
        },
        "contraindications_detail": {
            "tuyệt_đối": [
                "Dị ứng granisetron",
                "Dùng với apomorphine - CHỐNG CHỈ ĐỊNH tuyệt đối",
                "QT kéo dài (QTc >450ms ở nam, >470ms ở nữ) - CHỐNG CHỈ ĐỊNH"
            ],
            "tương_đối": [
                "Hạ kali, hạ magie - tăng nguy cơ QT kéo dài",
                "Đang dùng thuốc kéo dài QT - thận trọng"
            ]
        },
        "pregnancy_lactation": {
            "fda_category": "B",
            "pregnancy_details": "Granisetron là FDA category B. Có thể dùng trong thai kỳ nếu lợi ích > nguy cơ.",
            "lactation": {
                "safety": "Compatible",
                "details": "Granisetron bài tiết vào sữa mẹ ở nồng độ thấp. An toàn khi cho con bú.",
                "recommendation": "Có thể dùng khi cho con bú."
            }
        },
        "hepatic_adjustment": {
            "mild": "Không cần chỉnh liều",
            "moderate": "Không cần chỉnh liều",
            "severe": "Thận trọng, có thể giảm liều",
            "notes": "Granisetron chuyển hóa ở gan qua CYP3A4. Suy gan nặng có thể làm tăng nồng độ."
        },
        "overdose_management": {
            "symptoms": [
                "QT kéo dài, loạn nhịp tim",
                "Nhức đầu, chóng mặt",
                "Buồn nôn, nôn"
            ],
            "antidote": "Không có antidote đặc hiệu",
            "treatment": [
                "Theo dõi ECG liên tục",
                "Điều trị torsades de pointes nếu có: magnesium sulfate 2g IV",
                "Bổ sung kali, magie nếu thiếu",
                "Hỗ trợ triệu chứng"
            ],
            "monitoring": "Theo dõi ECG, dấu hiệu sinh tồn, điện giải"
        },
        "reversal_agents": {
            "available": False,
            "agents": []
        },
        "administration_instructions": {
            "oral": {
                "with_food": "Có thể uống với hoặc không với thức ăn",
                "timing": "Uống 30 phút trước hóa trị/xạ trị/phẫu thuật hoặc ngay khi có buồn nôn. Có thể dùng 1-2 lần/ngày."
            },
            "iv": {
                "reconstitution": "Granisetron IV: 1mg pha với 50ml NaCl 0.9% hoặc dextrose 5%",
                "infusion_rate": "Truyền trong 5 phút hoặc tiêm IV chậm",
                "compatibility": ["NaCl 0.9%", "Dextrose 5%"],
                "incompatibility": [],
                "notes": "Có thể tiêm IV trực tiếp chậm hoặc truyền."
            },
            "transdermal": {
                "notes": "Patch 3.1mg/24h: dán 24-48 giờ trước hóa trị, giữ trong 7 ngày. Kiểm tra da tại vị trí dán."
            }
        },
        "risk_flags": {
            "high_alert": False,
            "narrow_therapeutic_index": False,
            "bleeding_risk": False,
            "organ_toxicity": [],
            "qt_prolongation": True,
            "hepatotoxicity": False,
            "nephrotoxicity": False,
            "requires_monitoring": ["ECG (if risk factors)"]
        },
        "guideline_tags": [
            "ASCO Guidelines - Antiemetic therapy for chemotherapy-induced nausea and vomiting",
            "WHO Guidelines - Essential medicines for supportive care"
        ],
        "references": {
            "primary_sources": [
                "FDA Drug Label - Granisetron",
                "UpToDate - Granisetron: Drug information",
                "ASCO Antiemetic Guidelines"
            ],
            "last_updated": "2025-01-15",
            "evidence_level": "High - FDA approved, multiple RCTs"
        },
        "cost_estimate": {
            "generic": "Trung bình",
            "brand": "Cao",
            "notes": "Có generic, giá hợp lý hơn brand name"
        }
    },
    
    "Palonosetron": {
        "group": "Gastrointestinal - Antiemetic (5-HT3 Antagonist)",
        "vietnamese_name": "Palonosetron, Aloxi",
        "brand_names": {
            "common": ["Aloxi"],
            "vietnam": ["Palonosetron 0.25mg", "Aloxi"]
        },
        "administration": ["PO", "IV"],
        "indications": [
            "Buồn nôn, nôn do hóa trị cấp tính (acute CINV)",
            "Buồn nôn, nôn do hóa trị muộn (delayed CINV - ưu thế hơn các 5-HT3 khác)",
            "Buồn nôn, nôn sau phẫu thuật (PONV)"
        ],
        "contraindications": [
            "Dị ứng palonosetron",
            "QT kéo dài (QTc >450ms ở nam, >470ms ở nữ)",
            "Dùng với apomorphine"
        ],
        "dosage": {
            "adult_po": "0.5mg PO x 1 lần trước hóa trị",
            "adult_iv": "0.25mg IV x 1 lần trước hóa trị hoặc phẫu thuật",
            "adult_chemotherapy": "0.25mg IV hoặc 0.5mg PO trước hóa trị, chỉ cần 1 liều duy nhất",
            "adult_surgery": "0.075mg IV trước khi gây mê",
            "pediatric_po": "20mcg/kg PO x 1 lần trước hóa trị (tối đa 0.5mg)",
            "pediatric_iv": "20mcg/kg IV x 1 lần trước hóa trị (tối đa 0.25mg)",
            "geriatric_dosing": "Không cần chỉnh liều, nhưng thận trọng ở người già",
            "notes": "Ưu điểm: thời gian tác dụng rất dài (5 ngày), chỉ cần 1 liều duy nhất cho cả CINV cấp và muộn. Hiệu quả tốt hơn các 5-HT3 khác cho delayed CINV."
        },
        "renal_adjustment": {
            "normal": "Không cần chỉnh liều",
            "30_60": "Không cần chỉnh liều",
            "under_30": "Không cần chỉnh liều"
        },
        "side_effects": [
            "Nhức đầu",
            "Táo bón",
            "Chóng mặt",
            "Mệt mỏi",
            "QT kéo dài (nguy cơ thấp)"
        ],
        "interactions": [
            "Apomorphine: chống chỉ định",
            "Thuốc QT kéo dài: tăng nguy cơ loạn nhịp",
            "CYP2D6 inhibitors: có thể tăng nồng độ palonosetron"
        ],
        "pregnancy": "B - Không có bằng chứng về nguy cơ ở người",
        "mechanism_of_action": "5-HT3 receptor antagonist thế hệ thứ hai. Có ái lực cao hơn và thời gian bán hủy rất dài (40 giờ) so với ondansetron và granisetron. Tác dụng kéo dài đến 5 ngày, chỉ cần 1 liều duy nhất cho cả CINV cấp và muộn. Hiệu quả tốt hơn các 5-HT3 khác cho delayed CINV.",
        "monitoring": [
            "Tần suất nôn và buồn nôn",
            "ECG (QT kéo dài - nguy cơ thấp nhưng vẫn cần theo dõi)",
            "Điện giải (kali, magie) nếu có nguy cơ QT kéo dài"
        ],
        "precautions": [
            "QT kéo dài → không dùng ở bệnh nhân có QT kéo dài hoặc dùng các thuốc kéo dài QT khác",
            "Nguy cơ QT kéo dài thấp hơn ondansetron",
            "Chỉ cần 1 liều duy nhất cho cả CINV cấp và muộn (không cần lặp lại)",
            "Liều thường: 0.25mg IV hoặc 0.5mg PO, chỉ 1 lần",
            "An toàn trong thai kỳ (category B)"
        ],
        "pharmacokinetics": {
            "half_life": "40 giờ (rất dài, dài nhất trong các 5-HT3)",
            "onset": "30 phút (PO), ngay lập tức (IV)",
            "duration": "5 ngày (rất dài)",
            "protein_binding": "62%",
            "metabolism": "Gan (CYP2D6, CYP3A4) - chuyển hóa chậm",
            "clearance": "Chủ yếu qua gan và thận"
        },
        "storage": "Bảo quản ở nhiệt độ phòng (20-25°C), tránh ẩm. Dung dịch tiêm: bảo quản ở nhiệt độ phòng, tránh ánh sáng.",
        "black_box_warnings": "Nguy cơ QT kéo dài, có thể gây rối loạn nhịp tim nghiêm trọng. Nguy cơ thấp hơn ondansetron nhưng vẫn cần thận trọng.",
        "drug_interactions": {
            "major": [
                {
                    "drug": "Apomorphine",
                    "mechanism": "Palonosetron ức chế 5-HT3 receptor, đối kháng với apomorphine",
                    "effect": "Giảm hiệu quả apomorphine, có thể gây hạ huyết áp nặng",
                    "management": "CHỐNG CHỈ ĐỊNH dùng cùng."
                }
            ],
            "moderate": [
                {
                    "drug": "Thuốc kéo dài QT (amiodarone, quinolone, macrolide)",
                    "mechanism": "Tác dụng hiệp đồng kéo dài QT interval",
                    "effect": "Tăng nguy cơ QT kéo dài, loạn nhịp tim",
                    "management": "Tránh dùng cùng hoặc thận trọng. Theo dõi ECG."
                }
            ],
            "minor": []
        },
        "contraindications_detail": {
            "tuyệt_đối": [
                "Dị ứng palonosetron",
                "Dùng với apomorphine - CHỐNG CHỈ ĐỊNH tuyệt đối",
                "QT kéo dài (QTc >450ms ở nam, >470ms ở nữ) - CHỐNG CHỈ ĐỊNH"
            ],
            "tương_đối": [
                "Hạ kali, hạ magie - tăng nguy cơ QT kéo dài",
                "Đang dùng thuốc kéo dài QT - thận trọng"
            ]
        },
        "pregnancy_lactation": {
            "fda_category": "B",
            "pregnancy_details": "Palonosetron là FDA category B. Có thể dùng trong thai kỳ nếu lợi ích > nguy cơ.",
            "lactation": {
                "safety": "Compatible",
                "details": "Palonosetron bài tiết vào sữa mẹ ở nồng độ thấp. An toàn khi cho con bú.",
                "recommendation": "Có thể dùng khi cho con bú."
            }
        },
        "hepatic_adjustment": {
            "mild": "Không cần chỉnh liều",
            "moderate": "Không cần chỉnh liều",
            "severe": "Thận trọng, có thể giảm liều",
            "notes": "Palonosetron chuyển hóa ở gan qua CYP2D6 và CYP3A4. Suy gan nặng có thể làm tăng nồng độ."
        },
        "overdose_management": {
            "symptoms": [
                "QT kéo dài, loạn nhịp tim",
                "Nhức đầu, chóng mặt",
                "Buồn nôn, nôn"
            ],
            "antidote": "Không có antidote đặc hiệu",
            "treatment": [
                "Theo dõi ECG liên tục",
                "Điều trị torsades de pointes nếu có: magnesium sulfate 2g IV",
                "Bổ sung kali, magie nếu thiếu",
                "Hỗ trợ triệu chứng"
            ],
            "monitoring": "Theo dõi ECG, dấu hiệu sinh tồn, điện giải"
        },
        "reversal_agents": {
            "available": False,
            "agents": []
        },
        "administration_instructions": {
            "oral": {
                "with_food": "Có thể uống với hoặc không với thức ăn",
                "timing": "Uống 1 giờ trước hóa trị. Chỉ cần 1 liều duy nhất cho cả CINV cấp và muộn."
            },
            "iv": {
                "reconstitution": "Palonosetron IV: 0.25mg pha với 50ml NaCl 0.9% hoặc dextrose 5%",
                "infusion_rate": "Truyền trong 30 giây hoặc tiêm IV chậm",
                "compatibility": ["NaCl 0.9%", "Dextrose 5%"],
                "incompatibility": [],
                "notes": "Có thể tiêm IV trực tiếp chậm hoặc truyền. Chỉ cần 1 liều duy nhất."
            }
        },
        "risk_flags": {
            "high_alert": False,
            "narrow_therapeutic_index": False,
            "bleeding_risk": False,
            "organ_toxicity": [],
            "qt_prolongation": True,
            "hepatotoxicity": False,
            "nephrotoxicity": False,
            "requires_monitoring": ["ECG (if risk factors)"]
        },
        "guideline_tags": [
            "ASCO Guidelines - Antiemetic therapy for chemotherapy-induced nausea and vomiting",
            "WHO Guidelines - Essential medicines for supportive care"
        ],
        "references": {
            "primary_sources": [
                "FDA Drug Label - Palonosetron",
                "UpToDate - Palonosetron: Drug information",
                "ASCO Antiemetic Guidelines"
            ],
            "last_updated": "2025-01-15",
            "evidence_level": "High - FDA approved, multiple RCTs, superior for delayed CINV"
        },
        "cost_estimate": {
            "generic": "Cao",
            "brand": "Rất cao",
            "notes": "Thuốc mới hơn, giá cao hơn ondansetron và granisetron"
        }
    }
}

__all__ = ['ANTIEMETIC_5_HT3_ANTAGONISTS_DRUGS']
