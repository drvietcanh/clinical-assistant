"""Gastrointestinal Drugs
Active module - contains all gastrointestinal drug data"""

# Mucosal Protectants

MUCOSAL_PROTECTANTS_DRUGS = {
    "Misoprostol": {
        "group": "Gastrointestinal - Prostaglandin E1 Analog",
        "vietnamese_name": "Misoprostol, Cytotec",
        "administration": ["PO"],
        "indications": [
            "Phòng ngừa loét dạ dày do NSAID",
            "Điều trị loét dạ dày",
            "Phá thai y tế (kết hợp với mifepristone)",
            "Gây chuyển dạ (obstetric use)"
        ],
        "contraindications": [
            "Mang thai (CHỐNG CHỈ ĐỊNH TUYỆT ĐỐI - gây sảy thai, dị tật bẩm sinh)",
            "Dị ứng misoprostol hoặc prostaglandin",
            "Bệnh viêm ruột (IBD) nặng"
        ],
        "dosage": {
            "adult_ulcer_prevention": "200mcg x 4 lần/ngày với thức ăn",
            "adult_ulcer_treatment": "200mcg x 4 lần/ngày với thức ăn",
            "adult_max": "800mcg/ngày",
            "notes": "Uống với thức ăn để giảm tác dụng phụ tiêu hóa. CHỐNG CHỈ ĐỊNH TUYỆT ĐỐI trong thai kỳ."
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "Không đổi",
            "under_30": "Không đổi"
        },
        "side_effects": [
            "Tiêu chảy (phổ biến, đặc biệt khi bắt đầu)",
            "Đau bụng",
            "Buồn nôn",
            "Đầy hơi",
            "Chảy máu âm đạo (nếu mang thai - nguy hiểm)",
            "Co thắt tử cung (nếu mang thai - gây sảy thai)"
        ],
        "interactions": [
            "NSAIDs: phòng ngừa loét do NSAID",
            "Magnesium antacid: tăng tác dụng phụ tiêu hóa",
            "Thuốc chống đông: tăng nguy cơ chảy máu"
        ],
        "pregnancy": "X - CHỐNG CHỈ ĐỊNH TUYỆT ĐỐI",
        "mechanism_of_action": "Prostaglandin E1 analog. Ức chế tiết acid dạ dày bằng cách gắn với thụ thể prostaglandin, giảm tiết acid qua cơ chế tương tự prostaglandin tự nhiên. Tăng tiết chất nhầy và bicarbonate, tăng lưu lượng máu niêm mạc dạ dày, bảo vệ niêm mạc khỏi tổn thương. Kích thích co thắt tử cung (do đó chống chỉ định trong thai kỳ). Được dùng để phòng ngừa loét dạ dày do NSAID (đặc biệt ở bệnh nhân có nguy cơ cao).",
        "monitoring": [
            "Triệu chứng tiêu hóa: tiêu chảy, đau bụng (phổ biến khi bắt đầu)",
            "Dấu hiệu loét dạ dày (nếu dùng để điều trị)",
            "Chảy máu (nếu dùng với thuốc chống đông)",
            "Dấu hiệu mang thai (CHỐNG CHỈ ĐỊNH TUYỆT ĐỐI nếu có thai)",
            "Chức năng thận (nếu dùng lâu dài)"
        ],
        "precautions": [
            "CHỐNG CHỈ ĐỊNH TUYỆT ĐỐI trong thai kỳ - gây sảy thai, dị tật bẩm sinh",
            "Phụ nữ trong độ tuổi sinh đẻ: sử dụng biện pháp tránh thai hiệu quả",
            "Tiêu chảy phổ biến khi bắt đầu - thường tự khỏi sau vài ngày",
            "Uống với thức ăn để giảm tác dụng phụ tiêu hóa",
            "Thận trọng ở bệnh nhân bệnh viêm ruột (IBD) - có thể làm nặng",
            "Thận trọng ở bệnh nhân dùng thuốc chống đông - tăng nguy cơ chảy máu",
            "Không dùng với magnesium antacid - tăng tác dụng phụ tiêu hóa",
            "Dùng đủ thời gian để phòng ngừa loét (thường 4-8 tuần)"
        ],
        "pharmacokinetics": {
            "half_life": "20-40 phút (ngắn)",
            "onset": "30 phút - 1 giờ",
            "duration": "3-6 giờ",
            "protein_binding": "80-90%",
            "metabolism": "Chuyển hóa nhanh ở gan và các mô thành misoprostol acid (có hoạt tính)",
            "clearance": "Gan (chuyển hóa), thận (thải trừ một phần)"
        },
        "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm, tránh ánh sáng",
        "black_box_warnings": "CHỐNG CHỈ ĐỊNH TUYỆT ĐỐI trong thai kỳ. Misoprostol gây co thắt tử cung và có thể gây sảy thai, sinh non, dị tật bẩm sinh. Phụ nữ trong độ tuổi sinh đẻ phải sử dụng biện pháp tránh thai hiệu quả khi dùng misoprostol.",
        "drug_interactions": {
            "major": [
                {
                    "drug": "Magnesium antacid",
                    "mechanism": "Tăng tác dụng phụ tiêu hóa của misoprostol",
                    "effect": "Tăng tiêu chảy, đau bụng",
                    "management": "Tránh dùng cùng. Cách thời gian ít nhất 2 giờ."
                }
            ],
            "moderate": [
                {
                    "drug": "Thuốc chống đông (warfarin, heparin, DOACs)",
                    "mechanism": "Tác dụng hiệp đồng tăng nguy cơ chảy máu",
                    "effect": "Tăng nguy cơ chảy máu",
                    "management": "Thận trọng. Theo dõi dấu hiệu chảy máu. Theo dõi INR nếu dùng với warfarin."
                }
            ],
            "minor": []
        },
        "contraindications": {
            "tuyệt_đối": [
                "Mang thai (CHỐNG CHỈ ĐỊNH TUYỆT ĐỐI - gây sảy thai, dị tật bẩm sinh)",
                "Dị ứng misoprostol hoặc prostaglandin",
                "Phụ nữ đang cho con bú (nếu dùng cho mục đích phá thai)"
            ],
            "tương_đối": [
                "Bệnh viêm ruột (IBD) nặng - có thể làm nặng",
                "Tiền sử bệnh tim mạch - thận trọng",
                "Dùng với thuốc chống đông - tăng nguy cơ chảy máu"
            ]
        },
        "pregnancy_lactation": {
            "fda_category": "X",
            "pregnancy_details": "Misoprostol là category X - CHỐNG CHỈ ĐỊNH TUYỆT ĐỐI trong thai kỳ. Gây co thắt tử cung, có thể gây sảy thai, sinh non, dị tật bẩm sinh (đặc biệt dị tật Moebius syndrome - liệt dây thần kinh sọ). Phụ nữ trong độ tuổi sinh đẻ phải sử dụng biện pháp tránh thai hiệu quả khi dùng misoprostol.",
            "lactation": {
                "safety": "Compatible with monitoring",
                "details": "Misoprostol bài tiết vào sữa mẹ ở nồng độ thấp. Không có báo cáo về tác dụng phụ nghiêm trọng ở trẻ bú mẹ khi dùng với liều phòng ngừa loét.",
                "recommendation": "Có thể dùng khi cho con bú với liều phòng ngừa loét. Thận trọng nếu dùng với liều cao hơn."
            }
        },
        "hepatic_adjustment": {
            "mild": "Không cần điều chỉnh liều",
            "moderate": "Không cần điều chỉnh liều",
            "severe": "Không cần điều chỉnh liều",
            "notes": "Misoprostol chuyển hóa nhanh ở gan nhưng không tích lũy. Suy gan ít ảnh hưởng."
        },
        "overdose_management": {
            "symptoms": [
                "Triệu chứng tiêu hóa: tiêu chảy nặng, đau bụng nặng",
                "Triệu chứng thần kinh: chóng mặt, nhức đầu",
                "Triệu chứng tim mạch: hạ huyết áp, nhịp tim nhanh (hiếm)",
                "Ở phụ nữ mang thai: co thắt tử cung nặng, chảy máu, sảy thai"
            ],
            "antidote": "Không có antidote đặc hiệu",
            "treatment": [
                "Hỗ trợ triệu chứng: điều trị tiêu chảy, đau bụng",
                "Bù dịch nếu tiêu chảy nặng",
                "Theo dõi dấu hiệu sinh tồn",
                "Ở phụ nữ mang thai: theo dõi sát, có thể cần can thiệp y tế"
            ],
            "monitoring": "Theo dõi triệu chứng tiêu hóa, dấu hiệu sinh tồn, dấu hiệu mang thai nếu có"
        },
        "reversal_agents": {
            "available": False,
            "agents": []
        },
        "administration_instructions": {
            "oral": {
                "with_food": "Uống với thức ăn để giảm tác dụng phụ tiêu hóa (tiêu chảy, đau bụng).",
                "timing": "Uống 4 lần/ngày với thức ăn (200mcg mỗi lần). Uống cùng thời điểm mỗi ngày. QUAN TRỌNG: Phụ nữ trong độ tuổi sinh đẻ phải sử dụng biện pháp tránh thai hiệu quả."
            }
        },
        "references": {
            "primary_sources": [
                "FDA Drug Label - Cytotec (misoprostol)",
                "UpToDate - Misoprostol: Drug information",
                "Lexicomp - Misoprostol"
            ],
            "last_updated": "2025-02-05",
            "evidence_level": "A"
        }
    },
    "Sucralfate": {'group': 'Gastrointestinal - Mucosal Protectant', 'vietnamese_name':
        'Sucralfate, Carafate', 'administration': ['PO'], 'indications': [
        'Loét dạ dày tá tràng', 'Viêm dạ dày', 'Trào ngược dạ dày thực quản',
        'Loét do stress'],
        'contraindications': [
        'Suy thận nặng (tăng nguy cơ tích tụ nhôm)'], 'dosage': {'adult_ulcer':
        '1g x 4 lần/ngày (trước bữa ăn và trước khi ngủ) hoặc 2g x 2 lần/ngày',
        'adult_maintenance': '1g x 2 lần/ngày', 'notes':
        'Uống khi bụng đói (1 giờ trước bữa ăn). Không dùng với PPI, H2 blocker, antacid (cách 2 giờ)'
        }, 'renal_adjustment': {'normal': 'Không đổi', '30_60': 'Thận trọng',
        'under_30': 'Tránh dùng (tích tụ nhôm)'}, 'side_effects': ['Táo bón',
        'Khô miệng', 'Buồn nôn', 'Đầy hơi', 'Tích tụ nhôm (suy thận)'],
        'interactions': ['PPI/H2 blocker/Antacid: giảm hiệu quả - cách 2 giờ',
        'Warfarin: có thể tăng tác dụng chống đông',
        'Phenytoin: giảm hấp thu phenytoin', 'Digoxin: giảm hấp thu digoxin',
        'Quinolone: giảm hấp thu quinolone',
        'Thyroxine: giảm hấp thu thyroxine'],
        'mechanism_of_action':
        'Phức hợp sucrose-aluminum. Tạo lớp phủ bảo vệ trên vết loét dạ dày tá tràng. Phản ứng với acid dạ dày tạo thành gel dính, bám chặt vào vết loét, tạo hàng rào bảo vệ khỏi acid, pepsin, và muối mật. Kích thích tổng hợp prostaglandin, tăng tiết chất nhầy, tăng tái tạo niêm mạc. Cũng có thể hấp phụ pepsin và muối mật. Không giảm tiết acid như PPI/H2 blocker mà bảo vệ niêm mạc trực tiếp.'
        , 'monitoring': ['Đáp ứng lâm sàng (giảm đau, lành vết loét)',
        'Dấu hiệu tích tụ nhôm: rối loạn thần kinh, xương yếu (nếu dùng lâu dài ở suy thận)'
        , 'Chức năng thận (creatinine, BUN) - đặc biệt nếu dùng lâu dài',
        'INR nếu dùng với warfarin (có thể tăng tác dụng chống đông)',
        'Dấu hiệu táo bón nặng (tác dụng phụ thường gặp)'], 'precautions': [
        'Uống khi bụng đói (1 giờ trước bữa ăn) - cần acid dạ dày để tạo gel',
        'Không dùng với PPI, H2 blocker, antacid - cách 2 giờ (chúng làm giảm acid → giảm hiệu quả sucralfate)'
        ,
        'Không dùng với các thuốc khác - cách 2 giờ (sucralfate có thể giảm hấp thu)'
        , 'Thận trọng ở suy thận (CrCl 30-60) - giảm liều',
        'Tránh dùng ở suy thận nặng (CrCl <30) - tích tụ nhôm có thể gây độc',
        'Có thể gây táo bón - dùng thuốc nhuận tràng nếu cần',
        'Không nghiền hoặc nhai viên (giảm hiệu quả)',
        'Dùng đủ 4-8 tuần để lành vết loét hoàn toàn'], 'pharmacokinetics': {
        'half_life': 'Không áp dụng (tác dụng tại chỗ, không hấp thu)', 'onset':
        '1-2 giờ', 'duration': '6 giờ (lớp phủ bảo vệ)', 'protein_binding':
        'Không áp dụng (không hấp thu)', 'clearance':
        'Không hấp thu đáng kể, thải qua phân. Nhôm có thể tích tụ ở suy thận.'
        }, 'storage': 'Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm',
        'black_box_warnings':
        'Tích tụ nhôm ở suy thận nặng có thể gây độc tính thần kinh và xương. Tránh dùng ở suy thận nặng (CrCl <30).'
        , 'drug_interactions': {'major': [], 'moderate': [{'drug':
        'PPI, H2 blocker, Antacid', 'mechanism':
        'Giảm acid dạ dày, làm giảm khả năng tạo gel của sucralfate', 'effect':
        'Giảm hiệu quả của sucralfate', 'management':
        'Cách thời gian ít nhất 2 giờ. Uống sucralfate trước PPI/H2 blocker/antacid.'
        }, {'drug': 'Warfarin', 'mechanism':
        'Sucralfate có thể tăng hấp thu warfarin hoặc tương tác khác', 'effect':
        'Có thể tăng tác dụng chống đông, tăng INR', 'management':
        'Theo dõi INR thường xuyên. Cách thời gian 2 giờ.'}, {'drug':
        'Phenytoin, Digoxin, Quinolone, Thyroxine', 'mechanism':
        'Sucralfate giảm hấp thu các thuốc này (hấp phụ hoặc chelate)',
        'effect': 'Giảm nồng độ thuốc, giảm hiệu quả điều trị', 'management':
        'Cách thời gian ít nhất 2 giờ. Uống các thuốc khác trước sucralfate.'},
        {'drug': 'Iron salts, Vitamin D, Calcium', 'mechanism':
        'Sucralfate có thể giảm hấp thu', 'effect':
        'Giảm hấp thu iron, vitamin D, calcium', 'management':
        'Cách thời gian ít nhất 2 giờ'}], 'minor': []}, 'contraindications': {
        'tuyệt_đối': ['Dị ứng sucralfate',
        'Suy thận nặng (CrCl <30) - CHỐNG CHỈ ĐỊNH do tích tụ nhôm'],
        'tương_đối': [
        'Suy thận trung bình (CrCl 30-60) - thận trọng, giảm liều, theo dõi chức năng thận'
        , 'Táo bón nặng - có thể làm nặng thêm',
        'Đang dùng nhiều thuốc - tăng nguy cơ tương tác hấp thu']},
        'pregnancy_lactation': {'fda_category': 'B', 'pregnancy_details':
        'Sucralfate là FDA category B. Nghiên cứu trên động vật không cho thấy nguy cơ cho thai nhi. Không hấp thu đáng kể, nên an toàn hơn trong thai kỳ. Có thể dùng trong thai kỳ nếu lợi ích > nguy cơ.'
        , 'lactation': {'safety': 'Compatible', 'details':
        'Sucralfate không hấp thu đáng kể, không bài tiết vào sữa mẹ. An toàn khi cho con bú.'
        , 'recommendation':
        'Có thể dùng khi cho con bú. Dùng liều thường dùng.'}},
        'hepatic_adjustment': {'mild': 'Không cần chỉnh liều', 'moderate':
        'Không cần chỉnh liều', 'severe':
        'Không cần chỉnh liều. Sucralfate không hấp thu đáng kể, không chuyển hóa ở gan.'
        , 'notes':
        'Sucralfate không hấp thu đáng kể, không cần điều chỉnh liều ở suy gan.'
        }, 'overdose_management': {'symptoms': [
        'Sucralfate ít gây quá liều nghiêm trọng do không hấp thu',
        'Triệu chứng nhẹ: táo bón nặng, buồn nôn',
        'Ở suy thận nặng: tích tụ nhôm có thể gây độc tính thần kinh, xương yếu'
        ], 'treatment': [
        'Hỗ trợ triệu chứng (điều trị táo bón nếu cần)',
        'Theo dõi dấu hiệu tích tụ nhôm ở suy thận nặng',
        'Hầu hết trường hợp tự khỏi'], 'monitoring':
        'Theo dõi dấu hiệu tích tụ nhôm ở suy thận nặng (rối loạn thần kinh, xương yếu)'
        }, 'reversal_agents': None, 'administration_instructions': {'oral': {
        'with_food':
        'Uống KHI BỤNG ĐÓI (1 giờ trước bữa ăn) - quan trọng, cần acid dạ dày để tạo gel'
        , 'timing':
        'Uống 1 giờ trước bữa ăn và trước khi đi ngủ. Không uống với PPI, H2 blocker, antacid, hoặc các thuốc khác - cách ít nhất 2 giờ. KHÔNG nghiền hoặc nhai viên - nuốt nguyên viên với nước.'
        }, 'iv': {'reconstitution': 'Sucralfate chỉ có dạng uống (PO)',
        'infusion_rate': 'N/A', 'compatibility': [], 'incompatibility': [],
        'notes': 'Sucralfate chỉ có dạng uống, không có dạng IV'}},
        'references': {'primary_sources': ['FDA Drug Label - Sucralfate',
        'UpToDate - Sucralfate: Drug information', 'Micromedex - Sucralfate',
        "Goodman & Gilman's The Pharmacological Basis of Therapeutics"],
        'last_updated': '2024-12-19', 'evidence_level':
        'High - FDA approved, multiple RCTs'},
        "reversal_agents": {
             "available": False,
             "agents": []
         },
            "risk_flags": {
                "high_alert": False,
                "narrow_therapeutic_index": False,
                "bleeding_risk": False,
                "organ_toxicity": [],
                "qt_prolongation": False,
                "hepatotoxicity": False,
                "nephrotoxicity": False,
                "requires_monitoring": [],
            },
            "guideline_tags": [
                "FDA Drug Information",
                "UpToDate Drug Information",
            ]
},
    
}

__all__ = ['MUCOSAL_PROTECTANTS_DRUGS']
