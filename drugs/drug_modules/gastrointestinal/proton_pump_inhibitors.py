"""Gastrointestinal Drugs
Active module - contains all gastrointestinal drug data"""

# Proton Pump Inhibitors

PROTON_PUMP_INHIBITORS_DRUGS = {
    "Omeprazole": {
        "group": "Gastrointestinal - Proton Pump Inhibitor",
        "vietnamese_name": "Omeprazole, Losec",
        "brand_names": {
            "common": ["Prilosec", "Losec"],
            "vietnam": ["Omeprazole 20mg/40mg", "Losec MUPS"]
        },
        "administration": ["PO", "IV"],
        "indications": [
            "Loét dạ dày - tá tràng (Peptic ulcer)",
            "Trào ngược dạ dày - thực quản (GERD)",
            "Diệt H. pylori (phối hợp kháng sinh)",
            "Hội chứng Zollinger-Ellison",
            "Phòng ngừa loét dạ dày do NSAID"
        ],
        "contraindications": ["Dị ứng omeprazole hoặc PPI"],
        "dosage": {
            "adult_standard": "20-40mg x 1 lần/ngày",
            "adult_gerd": "20mg x 1 lần/ngày x 4-8 tuần",
            "adult_ulcer": "20-40mg x 1 lần/ngày x 4-8 tuần",
            "adult_h_pylori": "20mg x 2 lần/ngày (kết hợp với amoxicillin + clarithromycin)",
            "adult_iv": "20-40mg IV x 1-2 lần/ngày",
            "notes": "Uống 30-60 phút trước bữa ăn. Không nhai viên (enteric-coated)."
        },
        "side_effects": [
            "Đau đầu",
            "Tiêu chảy, táo bón",
            "Đau bụng",
            "Thiếu Vitamin B12 (nếu dùng lâu dài >3 năm)",
            "Thiếu Magie (nếu dùng lâu dài)",
            "Tăng nguy cơ gãy xương (dùng lâu dài)",
            "Viêm thận kẽ (Hiếm)",
            "Nhiễm C. difficile (tăng nguy cơ)"
        ],
        "interactions": [
            "Clopidogrel: Giảm hiệu quả (tránh dùng chung, chuyển sang Pantoprazole)",
            "Warfarin: Tăng INR",
            "Methotrexate: Tăng nồng độ MTX",
            "Ketoconazole, Itraconazole: Giảm hấp thu (cần môi trường acid)"
        ],
        "mechanism_of_action": "Ức chế bơm H+/K+ ATPase ở tế bào thành dạ dày → Giảm tiết acid mạnh (90%). Tác dụng kéo dài (24h). Omeprazole ức chế CYP2C19 mạnh, có thể giảm hiệu quả clopidogrel.",
        "monitoring": [
            "Triệu chứng GERD, loét",
            "Magie máu (nếu dùng lâu dài)",
            "Vitamin B12 (nếu dùng >3 năm)",
            "Dấu hiệu nhiễm C. difficile"
        ],
        "precautions": [
            "Chỉ dùng khi có chỉ định rõ ràng - Tránh lạm dụng",
            "Dùng liều thấp nhất, thời gian ngắn nhất",
            "Uống trước ăn sáng 30-60 phút",
            "Không nhai viên (enteric-coated)",
            "Tránh dùng chung với Clopidogrel (chuyển sang Pantoprazole)",
            "Nguy cơ thiếu B12, Magie nếu dùng lâu dài",
            "Tăng nguy cơ nhiễm C. difficile"
        ],
        "pharmacokinetics": {
            "half_life": "0.5-1 giờ (ngắn), nhưng tác dụng kéo dài 24h do ức chế không thuận nghịch proton pump",
            "onset": "1-3 ngày (tác dụng đầy đủ)",
            "duration": "24 giờ",
            "protein_binding": "95%",
            "metabolism": "Gan (CYP2C19, CYP3A4) - ức chế mạnh CYP2C19",
            "clearance": "Gan (chuyển hóa), thận (thải trừ chất chuyển hóa)"
        },
        "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm, tránh ánh sáng",
        "black_box_warnings": "Có thể tăng nguy cơ gãy xương khi dùng lâu dài (≥1 năm) và liều cao. Nguy cơ nhiễm C. difficile tăng. Giảm hấp thu vitamin B12 và magnesium khi dùng lâu dài. Giảm hiệu quả clopidogrel (tránh dùng chung).",
        "hepatic_adjustment": {
            "mild": "Không cần chỉnh liều",
            "moderate": "Không cần chỉnh liều, nhưng thận trọng",
            "severe": "Thận trọng ở suy gan nặng (Child-Pugh C). Có thể giảm liều.",
            "notes": "Omeprazole chuyển hóa ở gan qua CYP2C19 và CYP3A4. Thận trọng ở suy gan nặng."
        },
        "renal_adjustment": {
            "normal": "Không cần chỉnh liều",
            "30_60": "Không cần chỉnh liều. Omeprazole chủ yếu chuyển hóa qua gan.",
            "under_30": "Không cần chỉnh liều. Omeprazole chủ yếu chuyển hóa qua gan.",
            "dialysis": "Không cần chỉnh liều. Omeprazole không được lọc sạch qua thẩm phân máu.",
            "notes": "Omeprazole chủ yếu chuyển hóa qua gan (CYP2C19, CYP3A4). Không cần điều chỉnh liều ở suy thận."
        },
        "drug_interactions": {
            "major": [
                {
                    "drug": "Clopidogrel",
                    "mechanism": "Omeprazole ức chế CYP2C19 mạnh, làm giảm chuyển hóa clopidogrel thành dạng hoạt động",
                    "effect": "Giảm hiệu quả chống kết tập tiểu cầu của clopidogrel, tăng nguy cơ biến cố tim mạch",
                    "management": "TRÁNH DÙNG CÙNG. Chuyển sang pantoprazole hoặc H2 blocker nếu cần PPI."
                }
            ],
            "moderate": [
                {
                    "drug": "Warfarin",
                    "mechanism": "Omeprazole ức chế CYP2C9, có thể ảnh hưởng đến chuyển hóa warfarin",
                    "effect": "Có thể tăng INR",
                    "management": "Theo dõi INR thường xuyên. Điều chỉnh liều warfarin nếu cần."
                },
                {
                    "drug": "Ketoconazole, Itraconazole, Posaconazole",
                    "mechanism": "PPI tăng pH dạ dày, giảm hấp thu azole antifungals (cần môi trường acid)",
                    "effect": "Giảm nồng độ azole, giảm hiệu quả điều trị",
                    "management": "Cách thời gian ít nhất 2 giờ. Hoặc dùng dạng lỏng posaconazole."
                }
            ],
            "minor": []
        },
        "contraindications_detail": {
            "tuyệt_đối": [
                "Dị ứng omeprazole hoặc PPI khác",
                "Dùng cùng atazanavir (HIV protease inhibitor) - CHỐNG CHỈ ĐỊNH tuyệt đối"
            ],
            "tương_đối": [
                "Suy gan nặng (Child-Pugh C) - thận trọng, có thể giảm liều",
                "Suy thận nặng (CrCl <30) - không cần chỉnh liều nhưng thận trọng",
                "Loãng xương - tăng nguy cơ gãy xương khi dùng lâu dài",
                "Nhiễm C. difficile - tăng nguy cơ",
                "Thiếu vitamin B12 - bổ sung nếu dùng lâu dài",
                "Thiếu magnesium - bổ sung nếu dùng lâu dài",
                "Dùng với clopidogrel - CHỐNG CHỈ ĐỊNH tương đối (tránh dùng cùng)"
            ]
        },
        "reversal_agents": {
            "available": False,
            "agents": [],
            "notes": "Không có antidote đặc hiệu. Điều trị quá liều chủ yếu là hỗ trợ triệu chứng."
        }
    },
    "Esomeprazole": {'group': 'Gastrointestinal - Proton Pump Inhibitor', 'vietnamese_name':
        'Esomeprazole, Nexium', 'administration': ['PO', 'IV'], 'indications':
        ['Loét dạ dày tá tràng', 'GERD', 'Phòng ngừa loét do stress', 'Zollinger-Ellison syndrome'],
        'contraindications': ['Dị ứng esomeprazole hoặc PPI'], 'dosage': {'adult_standard':
        '20-40mg x 1 lần/ngày', 'adult_gerd': '40mg x 1 lần/ngày', 'adult_ulcer':
        '40mg x 1 lần/ngày x 4-8 tuần', 'adult_iv': '20-40mg IV x 1-2 lần/ngày', 'notes':
        'Uống 30-60 phút trước bữa ăn. Esomeprazole là S-enantiomer của omeprazole, hiệu quả hơn'}, 'side_effects': [
        'Nhức đầu', 'Tiêu chảy', 'Đau bụng', 'Buồn nôn', 'Tương tự các PPI khác'], 'interactions': [
        'Warfarin: có thể tăng INR', 'Clopidogrel: có thể giảm hiệu quả (ức chế CYP2C19)',
        'Ketoconazole: giảm hấp thu (cách xa 2 giờ)'],
        'mechanism_of_action':
        'Proton pump inhibitor (PPI). Esomeprazole là S-enantiomer của omeprazole, có dược động học tốt hơn và hiệu quả mạnh hơn omeprazole. Ức chế H+/K+-ATPase (proton pump) ở tế bào thành dạ dày, giảm tiết acid dạ dày mạnh và kéo dài. Esomeprazole được chuyển hóa chủ yếu qua CYP2C19 và CYP3A4.',
        'monitoring': ['Đáp ứng lâm sàng: giảm triệu chứng đau, ợ nóng',
        'Mg2+ máu (nếu dùng kéo dài >3 tháng) - PPI có thể gây hạ magie máu',
        'Vitamin B12 (nếu dùng kéo dài >2 năm) - PPI giảm hấp thu B12',
        'Dấu hiệu nhiễm trùng: PPI tăng nguy cơ viêm phổi, C. difficile colitis',
        'Loãng xương: PPI dùng kéo dài có thể tăng nguy cơ gãy xương (cần monitor nếu >1 năm)'],
        'precautions': [
        'Uống 30-60 phút TRƯỚC bữa ăn (để PPI hoạt động khi proton pump được kích hoạt)',
        'KHÔNG được nhai hoặc nghiền viên bao tan trong ruột (enteric-coated)',
        'Esomeprazole là S-enantiomer của omeprazole, hiệu quả mạnh hơn và dược động học tốt hơn',
        'Dùng ngắn hạn khi có thể - tránh dùng kéo dài không cần thiết',
        'Thận trọng ở bệnh nhân loãng xương (PPI dùng kéo dài có thể tăng nguy cơ gãy xương)',
        'Thận trọng ở bệnh nhân suy thận (không cần chỉnh liều nhưng monitor)',
        'Tăng nguy cơ viêm phổi, C. difficile colitis (đặc biệt ở người già, suy giảm miễn dịch)',
        'Thận trọng với clopidogrel (ức chế CYP2C19, có thể giảm hiệu quả clopidogrel)'],
        'pharmacokinetics': {'half_life':
        '1-1.5 giờ (ngắn), nhưng tác dụng kéo dài 24h do ức chế không thuận nghịch proton pump',
        'onset': '1-3 ngày (tác dụng đầy đủ)', 'duration':
        '24 giờ (mặc dù half-life ngắn)', 'protein_binding': '97%', 'clearance':
        'Gan (CYP2C19, CYP3A4) - ít phụ thuộc CYP2C19 hơn omeprazole'}, 'storage':
        'Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm, tránh ánh sáng',
        'black_box_warnings':
        'Có thể tăng nguy cơ gãy xương hông, cổ tay, cột sống khi dùng lâu dài (≥1 năm) và liều cao. Nguy cơ nhiễm C. difficile tăng. Giảm hấp thu vitamin B12 và magnesium khi dùng lâu dài',
        'drug_interactions': {'major': [{'drug':
        'Atazanavir (HIV protease inhibitor)', 'mechanism':
        'PPI làm tăng pH dạ dày, giảm hấp thu atazanavir (cần môi trường acid)',
        'effect': 'Giảm nồng độ atazanavir, giảm hiệu quả điều trị HIV', 'management':
        'CHỐNG CHỈ ĐỊNH dùng cùng. Không dùng esomeprazole với atazanavir. Dùng H2 blocker hoặc cách thời gian 12 giờ.'}],
        'moderate': [{'drug': 'Warfarin', 'mechanism':
        'Esomeprazole ức chế CYP2C19, có thể ảnh hưởng đến chuyển hóa warfarin',
        'effect': 'Có thể tăng INR', 'management':
        'Theo dõi INR thường xuyên. Điều chỉnh liều warfarin nếu cần.'}, {'drug':
        'Clopidogrel', 'mechanism':
        'Esomeprazole ức chế CYP2C19, enzyme cần thiết để kích hoạt clopidogrel',
        'effect': 'Giảm hiệu quả clopidogrel, tăng nguy cơ huyết khối', 'management':
        'Thận trọng. Cân nhắc dùng pantoprazole thay vì esomeprazole khi cần dùng với clopidogrel. Hoặc cách thời gian.'},
        {'drug': 'Ketoconazole, Itraconazole, Posaconazole', 'mechanism':
        'PPI tăng pH dạ dày, giảm hấp thu azole antifungals (cần môi trường acid)',
        'effect': 'Giảm nồng độ azole, giảm hiệu quả điều trị', 'management':
        'Cách thời gian ít nhất 2 giờ. Hoặc dùng dạng lỏng posaconazole.'}], 'minor': []},
        'contraindications': {'tuyệt_đối': [
        'Dị ứng esomeprazole hoặc PPI khác',
        'Dùng cùng atazanavir (HIV protease inhibitor) - CHỐNG CHỈ ĐỊNH tuyệt đối'], 'tương_đối': [
        'Suy gan nặng (Child-Pugh C) - thận trọng, có thể giảm liều',
        'Suy thận nặng (CrCl <30) - không cần chỉnh liều nhưng thận trọng',
        'Loãng xương - tăng nguy cơ gãy xương khi dùng lâu dài',
        'Nhiễm C. difficile - tăng nguy cơ',
        'Thiếu vitamin B12 - bổ sung nếu dùng lâu dài',
        'Thiếu magnesium - bổ sung nếu dùng lâu dài',
        'Dùng với clopidogrel - thận trọng (có thể giảm hiệu quả clopidogrel)'],
        'pregnancy_details':
        'Esomeprazole là FDA category B. Nghiên cứu trên động vật không cho thấy nguy cơ cho thai nhi, nhưng không có nghiên cứu đầy đủ trên người. Một số nghiên cứu quan sát không cho thấy tăng nguy cơ dị tật bẩm sinh. Có thể dùng trong thai kỳ nếu lợi ích > nguy cơ.',
        'lactation': {'safety': 'Compatible', 'details':
        'Esomeprazole bài tiết vào sữa mẹ ở nồng độ rất thấp. Không có báo cáo tác dụng phụ ở trẻ bú mẹ. An toàn khi cho con bú.',
        'recommendation': 'Có thể dùng khi cho con bú. Dùng liều thường dùng (20-40mg/ngày).'}},
        'hepatic_adjustment': {'mild': 'Không cần chỉnh liều', 'moderate':
        'Không cần chỉnh liều, nhưng thận trọng', 'severe':
        'Thận trọng ở suy gan nặng (Child-Pugh C). Có thể giảm liều. Esomeprazole chuyển hóa ở gan qua CYP2C19 và CYP3A4, nhưng ít phụ thuộc CYP2C19 hơn omeprazole.',
        'notes':
        'Esomeprazole chuyển hóa ở gan nhưng ít phụ thuộc CYP2C19 hơn omeprazole. Thận trọng ở suy gan nặng.'},
        'overdose_management': {'symptoms': [
        'PPI ít gây quá liều nghiêm trọng',
        'Triệu chứng nhẹ: nhức đầu, buồn nôn, tiêu chảy, chóng mặt'], 'antidote':
        'Không có antidote đặc hiệu', 'treatment': [
        'Hỗ trợ triệu chứng', 'Theo dõi dấu hiệu sinh tồn',
        'Hầu hết trường hợp tự khỏi'], 'monitoring':
        'Theo dõi dấu hiệu sinh tồn, triệu chứng nhẹ'}, 'reversal_agents': None,
        'administration_instructions': {'oral': {'with_food':
        'Uống 30-60 phút TRƯỚC bữa ăn (quan trọng - để PPI hoạt động khi proton pump được kích hoạt)',
        'timing':
        'Uống vào buổi sáng trước bữa sáng (hoặc trước bữa tối nếu dùng 2 lần/ngày). KHÔNG được nhai hoặc nghiền viên bao tan trong ruột - phải nuốt nguyên viên.'},
        'iv': {'reconstitution':
        'Esomeprazole IV: 20-40mg pha với 100ml NaCl 0.9% hoặc dextrose 5%',
        'infusion_rate':
        'Truyền trong 10-30 phút', 'compatibility': ['NaCl 0.9%', 'Dextrose 5%'],
        'incompatibility': [
        'Không pha với các thuốc khác trong cùng đường truyền'], 'notes':
        'Chỉ dùng IV khi không uống được. Chuyển sang PO sớm nhất có thể.'}},
        'references': {'primary_sources': ['FDA Drug Label - Esomeprazole',
        'UpToDate - Proton pump inhibitors: Overview of use and adverse effects',
        'Micromedex - Esomeprazole',
        "Goodman & Gilman's The Pharmacological Basis of Therapeutics"], 'last_updated':
        '2025-02-04', 'evidence_level': 'High - FDA approved, multiple RCTs'}},
    
    "Lansoprazole": {'group': 'Gastrointestinal - Proton Pump Inhibitor', 'vietnamese_name':
        'Lansoprazole, Prevacid', 'administration': ['PO'], 'indications':
        ['Loét dạ dày tá tràng', 'GERD', 'Phòng ngừa loét do stress', 'Zollinger-Ellison syndrome'],
        'contraindications': ['Dị ứng lansoprazole hoặc PPI'], 'dosage': {'adult_standard':
        '15-30mg x 1 lần/ngày', 'adult_gerd': '30mg x 1 lần/ngày', 'adult_ulcer':
        '30mg x 1 lần/ngày x 4-8 tuần', 'notes':
        'Uống 30 phút trước bữa ăn. Có thể mở viên nang và trộn với nước táo nếu cần'}, 'side_effects': [
        'Nhức đầu', 'Tiêu chảy', 'Đau bụng', 'Buồn nôn', 'Tương tự các PPI khác'], 'interactions': [
        'Warfarin: có thể tăng INR', 'Theophylline: tăng nồng độ theophylline',
        'Ketoconazole: giảm hấp thu (cách xa 2 giờ)'],
        'mechanism_of_action':
        'Proton pump inhibitor (PPI). Ức chế H+/K+-ATPase (proton pump) ở tế bào thành dạ dày, giảm tiết acid dạ dày mạnh và kéo dài. Lansoprazole được chuyển hóa chủ yếu qua CYP2C19 và CYP3A4. Tương tự omeprazole nhưng có thể có tương tác ít hơn với một số thuốc.',
        'monitoring': ['Đáp ứng lâm sàng: giảm triệu chứng đau, ợ nóng',
        'Mg2+ máu (nếu dùng kéo dài >3 tháng) - PPI có thể gây hạ magie máu',
        'Vitamin B12 (nếu dùng kéo dài >2 năm) - PPI giảm hấp thu B12',
        'Dấu hiệu nhiễm trùng: PPI tăng nguy cơ viêm phổi, C. difficile colitis',
        'Loãng xương: PPI dùng kéo dài có thể tăng nguy cơ gãy xương (cần monitor nếu >1 năm)'],
        'precautions': [
        'Uống 30 phút TRƯỚC bữa ăn (để PPI hoạt động khi proton pump được kích hoạt)',
        'KHÔNG được nhai hoặc nghiền viên bao tan trong ruột (enteric-coated)',
        'Có thể mở viên nang và trộn với nước táo nếu bệnh nhân không nuốt được viên',
        'Dùng ngắn hạn khi có thể - tránh dùng kéo dài không cần thiết',
        'Thận trọng ở bệnh nhân loãng xương (PPI dùng kéo dài có thể tăng nguy cơ gãy xương)',
        'Thận trọng ở bệnh nhân suy thận (không cần chỉnh liều nhưng monitor)',
        'Tăng nguy cơ viêm phổi, C. difficile colitis (đặc biệt ở người già, suy giảm miễn dịch)'],
        'pharmacokinetics': {'half_life':
        '1-2 giờ (ngắn), nhưng tác dụng kéo dài 24h do ức chế không thuận nghịch proton pump',
        'onset': '1-3 ngày (tác dụng đầy đủ)', 'duration':
        '24 giờ (mặc dù half-life ngắn)', 'protein_binding': '97%', 'clearance':
        'Gan (CYP2C19, CYP3A4)'}, 'storage':
        'Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm, tránh ánh sáng',
        'black_box_warnings':
        'Có thể tăng nguy cơ gãy xương hông, cổ tay, cột sống khi dùng lâu dài (≥1 năm) và liều cao. Nguy cơ nhiễm C. difficile tăng. Giảm hấp thu vitamin B12 và magnesium khi dùng lâu dài',
        'drug_interactions': {'major': [{'drug':
        'Atazanavir (HIV protease inhibitor)', 'mechanism':
        'PPI làm tăng pH dạ dày, giảm hấp thu atazanavir (cần môi trường acid)',
        'effect': 'Giảm nồng độ atazanavir, giảm hiệu quả điều trị HIV', 'management':
        'CHỐNG CHỈ ĐỊNH dùng cùng. Không dùng lansoprazole với atazanavir. Dùng H2 blocker hoặc cách thời gian 12 giờ.'}],
        'moderate': [{'drug': 'Warfarin', 'mechanism':
        'Lansoprazole ức chế CYP2C19, có thể ảnh hưởng đến chuyển hóa warfarin',
        'effect': 'Có thể tăng INR', 'management':
        'Theo dõi INR thường xuyên. Điều chỉnh liều warfarin nếu cần.'}, {'drug':
        'Ketoconazole, Itraconazole, Posaconazole', 'mechanism':
        'PPI tăng pH dạ dày, giảm hấp thu azole antifungals (cần môi trường acid)',
        'effect': 'Giảm nồng độ azole, giảm hiệu quả điều trị', 'management':
        'Cách thời gian ít nhất 2 giờ. Hoặc dùng dạng lỏng posaconazole.'}, {'drug':
        'Theophylline', 'mechanism':
        'Lansoprazole có thể ức chế chuyển hóa theophylline, tăng nồng độ',
        'effect': 'Tăng nồng độ theophylline, tăng độc tính', 'management':
        'Theo dõi nồng độ theophylline và điều chỉnh liều nếu cần.'}], 'minor': []},
        'contraindications': {'tuyệt_đối': [
        'Dị ứng lansoprazole hoặc PPI khác',
        'Dùng cùng atazanavir (HIV protease inhibitor) - CHỐNG CHỈ ĐỊNH tuyệt đối'], 'tương_đối': [
        'Suy gan nặng (Child-Pugh C) - thận trọng, có thể giảm liều',
        'Suy thận nặng (CrCl <30) - không cần chỉnh liều nhưng thận trọng',
        'Loãng xương - tăng nguy cơ gãy xương khi dùng lâu dài',
        'Nhiễm C. difficile - tăng nguy cơ',
        'Thiếu vitamin B12 - bổ sung nếu dùng lâu dài',
        'Thiếu magnesium - bổ sung nếu dùng lâu dài'],
        'pregnancy_details':
        'Lansoprazole là FDA category B. Nghiên cứu trên động vật không cho thấy nguy cơ cho thai nhi, nhưng không có nghiên cứu đầy đủ trên người. Một số nghiên cứu quan sát không cho thấy tăng nguy cơ dị tật bẩm sinh. Có thể dùng trong thai kỳ nếu lợi ích > nguy cơ.',
        'lactation': {'safety': 'Compatible', 'details':
        'Lansoprazole bài tiết vào sữa mẹ ở nồng độ rất thấp. Không có báo cáo tác dụng phụ ở trẻ bú mẹ. An toàn khi cho con bú.',
        'recommendation': 'Có thể dùng khi cho con bú. Dùng liều thường dùng (15-30mg/ngày).'}},
        'hepatic_adjustment': {'mild': 'Không cần chỉnh liều', 'moderate':
        'Không cần chỉnh liều, nhưng thận trọng', 'severe':
        'Thận trọng ở suy gan nặng (Child-Pugh C). Có thể giảm liều. Lansoprazole chuyển hóa ở gan qua CYP2C19 và CYP3A4.',
        'notes':
        'Lansoprazole chuyển hóa ở gan. Suy gan có thể làm giảm chuyển hóa, tăng nồng độ. Thận trọng ở suy gan nặng.'},
        'overdose_management': {'symptoms': [
        'PPI ít gây quá liều nghiêm trọng',
        'Triệu chứng nhẹ: nhức đầu, buồn nôn, tiêu chảy, chóng mặt'], 'antidote':
        'Không có antidote đặc hiệu', 'treatment': [
        'Hỗ trợ triệu chứng', 'Theo dõi dấu hiệu sinh tồn',
        'Hầu hết trường hợp tự khỏi'], 'monitoring':
        'Theo dõi dấu hiệu sinh tồn, triệu chứng nhẹ'}, 'reversal_agents': None,
        'administration_instructions': {'oral': {'with_food':
        'Uống 30 phút TRƯỚC bữa ăn (quan trọng - để PPI hoạt động khi proton pump được kích hoạt)',
        'timing':
        'Uống vào buổi sáng trước bữa sáng. KHÔNG được nhai hoặc nghiền viên bao tan trong ruột - phải nuốt nguyên viên. Có thể mở viên nang và trộn với nước táo nếu bệnh nhân không nuốt được viên.'},
        'iv': {'reconstitution': 'Không có dạng IV', 'infusion_rate': 'N/A',
        'compatibility': [], 'incompatibility': []}},
        'references': {'primary_sources': ['FDA Drug Label - Lansoprazole',
        'UpToDate - Proton pump inhibitors: Overview of use and adverse effects',
        'Micromedex - Lansoprazole',
        "Goodman & Gilman's The Pharmacological Basis of Therapeutics"], 'last_updated':
        '2025-02-04', 'evidence_level': 'High - FDA approved, multiple RCTs'}},
    "Pantoprazole": {'group': 'Gastrointestinal - Proton Pump Inhibitor', 'vietnamese_name':
        'Pantoprazole, Pantoloc', 'administration': ['PO', 'IV'], 'indications':
        ['Loét dạ dày tá tràng', 'GERD', 'Phòng ngừa loét do stress'],
        'contraindications': ['Dị ứng'], 'dosage': {'adult_po':
        '40mg x 1-2 lần/ngày', 'adult_iv': '40mg x 1-2 lần/ngày', 'notes':
        'Ít tương tác hơn omeprazole với clopidogrel'}, 'side_effects': [
        'Nhức đầu', 'Tiêu chảy', 'Tương tự omeprazole'], 'interactions': [
        'Ít tương tác hơn omeprazole'], 'mechanism_of_action':
        'Proton pump inhibitor (PPI). Ức chế H+/K+-ATPase (proton pump) ở tế bào thành dạ dày, giảm tiết acid dạ dày mạnh và kéo dài. Khác với H2 blockers, PPI ức chế bước cuối cùng của quá trình tiết acid, nên hiệu quả hơn. Pantoprazole ít tương tác với CYP450 hơn omeprazole.'
        , 'monitoring': ['Đáp ứng lâm sàng: giảm triệu chứng đau, ợ nóng',
        'Mg2+ máu (nếu dùng kéo dài >3 tháng) - PPI có thể gây hạ magie máu',
        'Vitamin B12 (nếu dùng kéo dài >2 năm) - PPI giảm hấp thu B12',
        'Dấu hiệu nhiễm trùng: PPI tăng nguy cơ viêm phổi, C. difficile colitis',
        'Loãng xương: PPI dùng kéo dài có thể tăng nguy cơ gãy xương (cần monitor nếu >1 năm)'
        ], 'precautions': [
        'Uống 30-60 phút TRƯỚC bữa ăn (để PPI hoạt động khi proton pump được kích hoạt)'
        ,
        'KHÔNG được nhai hoặc nghiền viên bao tan trong ruột (enteric-coated)',
        'Pantoprazole ưu điểm: ít tương tác với CYP450 hơn omeprazole, ít ảnh hưởng đến clopidogrel hơn'
        , 'Dùng ngắn hạn khi có thể - tránh dùng kéo dài không cần thiết',
        'Thận trọng ở bệnh nhân loãng xương (PPI dùng kéo dài có thể tăng nguy cơ gãy xương)'
        ,
        'Thận trọng ở bệnh nhân suy thận (không cần chỉnh liều nhưng monitor)',
        'Tăng nguy cơ viêm phổi, C. difficile colitis (đặc biệt ở người già, suy giảm miễn dịch)'
        ], 'pharmacokinetics': {'half_life':
        '1 giờ (ngắn), nhưng tác dụng kéo dài 24h do ức chế không thuận nghịch proton pump'
        , 'onset': '1-3 ngày (tác dụng đầy đủ)', 'duration':
        '24 giờ (mặc dù half-life ngắn)', 'protein_binding': '98%', 'clearance':
        'Gan (CYP2C19, CYP3A4) - ít tương tác hơn omeprazole'}, 'storage':
        'Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm, tránh ánh sáng',
        'black_box_warnings':
        'Có thể tăng nguy cơ gãy xương hông, cổ tay, cột sống khi dùng lâu dài (≥1 năm) và liều cao. Nguy cơ nhiễm C. difficile tăng. Giảm hấp thu vitamin B12 và magnesium khi dùng lâu dài'
        , 'drug_interactions': {'major': [{'drug':
        'Atazanavir (HIV protease inhibitor)', 'mechanism':
        'PPI làm tăng pH dạ dày, giảm hấp thu atazanavir (cần môi trường acid)',
        'effect': 'Giảm nồng độ atazanavir, giảm hiệu quả điều trị HIV',
        'management':
        'CHỐNG CHỈ ĐỊNH dùng cùng. Không dùng pantoprazole với atazanavir. Dùng H2 blocker hoặc cách thời gian 12 giờ.'
        }, {'drug': 'Warfarin', 'mechanism':
        'Pantoprazole ít ức chế CYP450 hơn omeprazole, nhưng vẫn có thể tương tác nhẹ'
        , 'effect': 'Có thể tăng INR nhẹ', 'management':
        'Theo dõi INR thường xuyên. Pantoprazole ít ảnh hưởng hơn omeprazole.'},
        {'drug': 'Ketoconazole, Itraconazole, Posaconazole', 'mechanism':
        'PPI tăng pH dạ dày, giảm hấp thu azole antifungals (cần môi trường acid)',
        'effect': 'Giảm nồng độ azole, giảm hiệu quả điều trị', 'management':
        'Cách thời gian ít nhất 2 giờ. Hoặc dùng dạng lỏng posaconazole.'}, {
        'drug': 'Iron salts (ferrous sulfate, ferrous fumarate)', 'mechanism':
        'PPI giảm acid dạ dày, giảm chuyển Fe3+ thành Fe2+', 'effect':
        'Giảm hấp thu sắt', 'management':
        'Cách thời gian ít nhất 2 giờ. Hoặc dùng sắt dạng chelate.'}, {'drug':
        'Vitamin B12 (cobalamin)', 'mechanism':
        'PPI giảm acid dạ dày, giảm tách B12 khỏi protein thức ăn', 'effect':
        'Giảm hấp thu B12 sau 2-3 năm dùng PPI', 'management':
        'Bổ sung B12 định kỳ nếu dùng lâu dài (>2 năm).'}], 'minor': [{'drug':
        'Clopidogrel', 'mechanism':
        'Pantoprazole ít ức chế CYP2C19 hơn omeprazole', 'effect':
        'Ít ảnh hưởng đến clopidogrel hơn omeprazole, nhưng vẫn thận trọng',
        'management':
        'Pantoprazole là lựa chọn tốt hơn omeprazole khi cần dùng với clopidogrel. Vẫn nên tránh dùng cùng nếu có thể.'
        }]},         'contraindications': ['Dị ứng'],
        'contraindications_detail': {'tuyệt_đối': [
        'Dị ứng pantoprazole hoặc PPI khác',
        'Dùng cùng atazanavir (HIV protease inhibitor) - CHỐNG CHỈ ĐỊNH tuyệt đối'
        ], 'tương_đối': [
        'Suy gan nặng (Child-Pugh C) - thận trọng, có thể giảm liều',
        'Suy thận nặng (CrCl <30) - không cần chỉnh liều nhưng thận trọng',
        'Loãng xương - tăng nguy cơ gãy xương khi dùng lâu dài',
        'Nhiễm C. difficile - tăng nguy cơ',
        'Thiếu vitamin B12 - bổ sung nếu dùng lâu dài',
        'Thiếu magnesium - bổ sung nếu dùng lâu dài']}, 'pregnancy_lactation':
        {'fda_category': 'B', 'pregnancy_details':
        'Pantoprazole là FDA category B. Nghiên cứu trên động vật không cho thấy nguy cơ cho thai nhi, nhưng không có nghiên cứu đầy đủ trên người. Một số nghiên cứu quan sát không cho thấy tăng nguy cơ dị tật bẩm sinh. Có thể dùng trong thai kỳ nếu lợi ích > nguy cơ. An toàn hơn omeprazole (category C) trong thai kỳ.'
        , 'lactation': {'safety': 'Compatible', 'details':
        'Pantoprazole bài tiết vào sữa mẹ ở nồng độ rất thấp. Không có báo cáo tác dụng phụ ở trẻ bú mẹ. An toàn khi cho con bú.'
        , 'recommendation':
        'Có thể dùng khi cho con bú. Dùng liều thường dùng (40mg/ngày).'}},
        'hepatic_adjustment': {'mild': 'Không cần chỉnh liều', 'moderate':
        'Không cần chỉnh liều, nhưng thận trọng', 'severe':
        'Thận trọng ở suy gan nặng (Child-Pugh C). Có thể giảm liều. Pantoprazole chuyển hóa ở gan qua CYP2C19 và CYP3A4, nhưng ít phụ thuộc vào CYP2C19 hơn omeprazole.'
        , 'notes':
        'Pantoprazole ít tương tác với CYP450 hơn omeprazole, nên ít ảnh hưởng hơn ở suy gan. Tuy nhiên, vẫn thận trọng ở suy gan nặng.'
        }, 'renal_adjustment': {'normal': 'Không cần chỉnh liều',
        '30_60': 'Không cần chỉnh liều. Pantoprazole chủ yếu chuyển hóa qua gan.',
        'under_30': 'Không cần chỉnh liều. Pantoprazole chủ yếu chuyển hóa qua gan.',
        'dialysis': 'Không cần chỉnh liều. Pantoprazole không được lọc sạch qua thẩm phân máu.',
        'notes': 'Pantoprazole chủ yếu chuyển hóa qua gan (CYP2C19, CYP3A4). Không cần điều chỉnh liều ở suy thận.'}, 'overdose_management': {'symptoms': [
        'PPI ít gây quá liều nghiêm trọng',
        'Triệu chứng nhẹ: nhức đầu, buồn nôn, tiêu chảy, chóng mặt'],
        'antidote': 'Không có antidote đặc hiệu', 'treatment': [
        'Hỗ trợ triệu chứng', 'Theo dõi dấu hiệu sinh tồn',
        'Hầu hết trường hợp tự khỏi'], 'monitoring':
        'Theo dõi dấu hiệu sinh tồn, triệu chứng nhẹ'}, 'reversal_agents': {'available': False, 'agents': [],
        'notes': 'Không có antidote đặc hiệu. Điều trị quá liều chủ yếu là hỗ trợ triệu chứng.'},
        'administration_instructions': {'oral': {'with_food':
        'Uống 30-60 phút TRƯỚC bữa ăn (quan trọng - để PPI hoạt động khi proton pump được kích hoạt)'
        , 'timing':
        'Uống vào buổi sáng trước bữa sáng (hoặc trước bữa tối nếu dùng 2 lần/ngày). KHÔNG được nhai hoặc nghiền viên bao tan trong ruột - phải nuốt nguyên viên.'
        }, 'iv': {'reconstitution':
        'Pantoprazole IV: 40mg pha với 100ml NaCl 0.9% hoặc dextrose 5%',
        'infusion_rate':
        'Truyền trong 15 phút (IV bolus) hoặc 30 phút (infusion)',
        'compatibility': ['NaCl 0.9%', 'Dextrose 5%'], 'incompatibility': [
        'Không pha với các thuốc khác trong cùng đường truyền'], 'notes':
        'Chỉ dùng IV khi không uống được. Chuyển sang PO sớm nhất có thể.'}},
        'pediatric_dosing': {
        'neonates': 'Không khuyến cáo cho trẻ <1 tuổi (dữ liệu hạn chế)',
        'infants': '1-12 tháng: 0.5-1mg/kg/ngày chia 1-2 lần. Chỉ dùng khi thực sự cần thiết. Theo dõi chặt chẽ',
        'children': '1-16 tuổi: 0.7-1.4mg/kg/ngày chia 1-2 lần (tối đa 40mg/ngày). Chỉ dùng cho GERD nặng hoặc loét dạ dày. Uống 30-60 phút trước bữa ăn',
        'adolescents': '40mg x 1-2 lần/ngày. Liều người lớn. Uống 30-60 phút trước bữa ăn',
        'notes': 'Dùng cho GERD và loét dạ dày ở trẻ em. Khởi đầu với liều thấp, tăng dần. Uống 30-60 phút trước bữa ăn. Ưu điểm: ít tương tác với CYP450 hơn omeprazole. Theo dõi triệu chứng, vitamin B12, magnesium nếu dùng lâu dài'
    }, 'geriatric_dosing': {
        'considerations': 'Người cao tuổi có thể nhạy cảm hơn với tác dụng phụ. Tăng nguy cơ nhiễm C. difficile, gãy xương, thiếu B12 và magnesium khi dùng lâu dài',
        'dose_adjustment': 'Khởi đầu với liều thấp hơn (20-40mg x 1 lần/ngày). Tăng dần nếu cần. Dùng liều thấp nhất có hiệu quả, thời gian ngắn nhất',
        'monitoring': 'Theo dõi triệu chứng, vitamin B12, magnesium thường xuyên hơn nếu dùng lâu dài. Cảnh báo về nguy cơ nhiễm C. difficile, gãy xương'
    }, 'brand_names': {
        'vietnam': ['Pantoloc', 'Pantoprazole Stada', 'Pantoprazole', 'Controloc'],
        'common': ['Pantoloc', 'Protonix', 'Pantoprazole']
    }, 'cost_estimate': {
        'unit': 'VND',
        'range': '8,000 - 30,000 VND/viên (tùy hàm lượng và thương hiệu)',
        'note': 'Giá thay đổi theo thương hiệu và nhà thuốc. Pantoprazole generic thường rẻ hơn (8,000-20,000 VND/viên 40mg).'
    }, 'references': {'primary_sources': ['FDA Drug Label - Pantoprazole',
        'UpToDate - Proton pump inhibitors: Overview of use and adverse effects',
        'Micromedex - Pantoprazole',
        "Goodman & Gilman's The Pharmacological Basis of Therapeutics",
        'JAMA - Pantoprazole vs omeprazole and clopidogrel interaction (2010)'],
        'last_updated': '2024-12-19', 'evidence_level':
        'High - FDA approved, multiple RCTs'}},
    "Rabeprazole": {
        "group": "Gastrointestinal - Proton Pump Inhibitor",
        "vietnamese_name": "Rabeprazole, Pariet, Aciphex",
        "administration": ["PO"],
        "indications": [
            "Loét dạ dày tá tràng",
            "GERD",
            "Hội chứng Zollinger-Ellison",
            "Diệt H. pylori (kết hợp với kháng sinh)"
        ],
        "contraindications": [
            "Dị ứng rabeprazole"
        ],
        "contraindications_detail": {
            "tuyệt_đối": [
                "Dị ứng rabeprazole hoặc PPI khác",
                "Dùng cùng atazanavir (HIV protease inhibitor) - CHỐNG CHỈ ĐỊNH tuyệt đối"
            ],
            "tương_đối": [
                "Suy gan nặng (Child-Pugh C) - thận trọng, có thể giảm liều",
                "Suy thận nặng (CrCl <30) - không cần chỉnh liều nhưng thận trọng",
                "Loãng xương - tăng nguy cơ gãy xương khi dùng lâu dài",
                "Nhiễm C. difficile - tăng nguy cơ",
                "Thiếu vitamin B12 - bổ sung nếu dùng lâu dài",
                "Thiếu magnesium - bổ sung nếu dùng lâu dài"
            ]
        },
        "dosage": {
            "adult_po": "20mg x 1-2 lần/ngày",
            "adult_gerd": "20mg x 1 lần/ngày x 4-8 tuần",
            "adult_ulcer": "20mg x 1 lần/ngày x 4-8 tuần",
            "adult_h_pylori": "20mg x 2 lần/ngày (kết hợp với amoxicillin + clarithromycin)",
            "notes": "Uống 30-60 phút trước bữa ăn. Ít phụ thuộc CYP2C19 hơn omeprazole."
        },
        "renal_adjustment": {
            "normal": "Không cần chỉnh liều",
            "30_60": "Không cần chỉnh liều. Rabeprazole chủ yếu chuyển hóa qua gan.",
            "under_30": "Không cần chỉnh liều. Rabeprazole chủ yếu chuyển hóa qua gan.",
            "dialysis": "Không cần chỉnh liều. Rabeprazole không được lọc sạch qua thẩm phân máu.",
            "notes": "Rabeprazole chủ yếu chuyển hóa qua gan (CYP3A4 chủ yếu, ít phụ thuộc CYP2C19). Không cần điều chỉnh liều ở suy thận."
        },
        "side_effects": [
            "Nhức đầu",
            "Tiêu chảy",
            "Buồn nôn",
            "Đau bụng",
            "Tăng men gan (hiếm)"
        ],
        "interactions": [
            "Warfarin: có thể tăng INR nhẹ",
            "Ketoconazole/Itraconazole: giảm hấp thu",
            "Atazanavir: giảm hấp thu (chống chỉ định)"
        ],
        "pregnancy": "B - An toàn",
        "mechanism_of_action": "Proton pump inhibitor (PPI). Ức chế H+/K+-ATPase (proton pump) ở tế bào thành dạ dày, giảm tiết acid dạ dày mạnh và kéo dài. Rabeprazole được chuyển hóa chủ yếu qua CYP3A4, ít phụ thuộc CYP2C19 hơn omeprazole. Ưu điểm: ít bị ảnh hưởng bởi polymorphism CYP2C19, hiệu quả ổn định hơn.",
        "monitoring": [
            "Đáp ứng lâm sàng: giảm triệu chứng đau, ợ nóng",
            "Mg2+ máu (nếu dùng kéo dài >3 tháng)",
            "Vitamin B12 (nếu dùng kéo dài >2 năm)",
            "Dấu hiệu nhiễm trùng: viêm phổi, C. difficile",
            "Loãng xương (nếu dùng >1 năm)"
        ],
        "precautions": [
            "Uống 30-60 phút TRƯỚC bữa ăn",
            "KHÔNG được nhai hoặc nghiền viên bao tan trong ruột",
            "Ít phụ thuộc CYP2C19 hơn omeprazole - hiệu quả ổn định hơn",
            "Dùng ngắn hạn khi có thể",
            "Thận trọng ở bệnh nhân loãng xương",
            "Tăng nguy cơ viêm phổi, C. difficile colitis"
        ],
        "pharmacokinetics": {
            "half_life": "1-2 giờ (ngắn), nhưng tác dụng kéo dài 24h",
            "onset": "1-3 ngày (tác dụng đầy đủ)",
            "duration": "24 giờ",
            "protein_binding": "96%",
            "metabolism": "Gan (CYP3A4 chủ yếu, ít phụ thuộc CYP2C19)",
            "clearance": "Gan, ít bị ảnh hưởng bởi polymorphism CYP2C19"
        },
        "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm, tránh ánh sáng",
        "black_box_warnings": "Có thể tăng nguy cơ gãy xương khi dùng lâu dài (≥1 năm) và liều cao. Nguy cơ nhiễm C. difficile tăng.",
        "references": {
            "primary_sources": [
                "FDA Drug Label - Rabeprazole",
                "UpToDate - Rabeprazole: Drug Information",
                "Medscape - Rabeprazole Drug Reference"
            ],
            "last_updated": "2025-02-05",
            "evidence_level": "A"
        },
        "drug_interactions": {
                  "major": [
                      {
                          "drug": "Warfarin: có thể tăng INR nhẹ",
                          "mechanism": "Tăng nguy cơ chảy máu"
                      }
                  ],
                  "moderate": [],
                  "minor": [
                      {
                          "drug": "Ketoconazole/Itraconazole: giảm hấp thu",
                          "mechanism": "Tương tác lâm sàng"
                      },
                      {
                          "drug": "Atazanavir: giảm hấp thu (chống chỉ định)",
                          "mechanism": "Tương tác lâm sàng"
                      }
                  ]
              },
              "pregnancy_lactation": {
                  "fda_category": "B - An toàn",
                  "pregnancy_details": "Category B - An toàn - Cần tra cứu thêm thông tin chi tiết về sử dụng trong thai kỳ.",
                  "lactation": {
                      "safety": "Use with caution",
                      "details": "Cần tra cứu thêm thông tin chi tiết về bài tiết vào sữa mẹ.",
                      "recommendation": "Thận trọng khi cho con bú, tra cứu thêm thông tin."
                  }
              },
              "hepatic_adjustment": {
                  "mild": "Không đổi",
                  "moderate": "Thận trọng",
                  "severe": "Thận trọng, có thể giảm liều",
                  "notes": "Cần tra cứu thêm thông tin chi tiết về điều chỉnh liều ở suy gan."
              },
              "overdose_management": {
                  "symptoms": [
                      "Cần tra cứu thêm thông tin về triệu chứng quá liều"
                  ],
                  "antidote": "Không có antidote đặc hiệu",
                  "treatment": [
                      "Ngừng ngay thuốc",
                      "Rửa dạ dày nếu uống trong vòng 1-2 giờ (nếu phù hợp)",
                      "Than hoạt tính",
                      "Điều trị hỗ trợ và điều trị triệu chứng",
                      "Theo dõi dấu hiệu sinh tồn"
                  ],
                  "monitoring": "Theo dõi dấu hiệu sinh tồn, triệu chứng lâm sàng"
              },
              "reversal_agents": {
                  "available": False,
                  "agents": [],
                  "notes": "Không có antidote đặc hiệu. Điều trị quá liều chủ yếu là hỗ trợ triệu chứng."
              },
              "administration_instructions": {
                  "oral": {
                      "with_food": "Có thể uống với hoặc không có thức ăn (trừ khi có chỉ định khác)",
                      "timing": "Theo chỉ định của bác sĩ",
                      "notes": "Cần tra cứu thêm thông tin chi tiết về cách dùng."
                  }
              },
},
}

__all__ = ['PROTON_PUMP_INHIBITORS_DRUGS']
