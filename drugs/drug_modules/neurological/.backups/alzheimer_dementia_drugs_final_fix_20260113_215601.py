"""Neurological Medications - Alzheimer's Disease and Dementia
Active module - contains cholinesterase inhibitors and NMDA antagonists"""

# Cholinesterase Inhibitors and NMDA Antagonists

ALZHEIMER_DEMENTIA_DRUGS = {
    "Aducanumab": {
        "group": "Neurology - Anti-amyloid Monoclonal Antibody",
        "vietnamese_name": "Aducanumab, Aduhelm",
        "administration": ["IV"],
        "indications": [
            "Bệnh Alzheimer giai đoạn sớm (mild cognitive impairment hoặc mild dementia) với bằng chứng tích tụ amyloid (PET hoặc CSF)"
        ],
        "contraindications": [
            "Dị ứng aducanumab hoặc thành phần thuốc",
            "Bệnh nhân không có bằng chứng amyloid (không nên dùng)"
        ],
        "dosage": {
            "adult_standard": "10mg/kg IV mỗi 4 tuần",
            "notes": "Truyền trong khoảng 1 giờ. Cần MRI nền (baseline) và theo dõi định kỳ để phát hiện ARIA. Liều tăng dần từ 1mg/kg → 3mg/kg → 6mg/kg → 10mg/kg."
        },
        "renal_adjustment": {
            "normal": "Không cần chỉnh liều",
            "30_60": "Không cần chỉnh liều; dữ liệu hạn chế, theo dõi",
            "under_30": "Dữ liệu hạn chế; thận trọng"
        },
        "side_effects": [
            "ARIA-E (phù mạch não liên quan amyloid) - phổ biến, có thể nghiêm trọng",
            "ARIA-H (vi xuất huyết, lắng đọng hemosiderin) - phổ biến, có thể nghiêm trọng",
            "Nhức đầu",
            "Đau tại vị trí truyền",
            "Buồn nôn",
            "Các triệu chứng giống cúm sau truyền",
            "Lú lẫn",
            "Co giật (hiếm)"
        ],
        "interactions": [
            "Thuốc chống đông/kháng tiểu cầu liều cao: có thể tăng nguy cơ xuất huyết não khi ARIA-H"
        ],
        "pregnancy": "Chưa có dữ liệu, tránh dùng nếu có thể",
        "mechanism_of_action": (
            "Aducanumab là kháng thể đơn dòng kháng amyloid-beta (human monoclonal antibody). "
            "Aducanumab gắn với các dạng amyloid-beta (monomer, oligomer, và fibril) trong não, "
            "đặc biệt ưu tiên gắn với các dạng độc hại (toxic forms) của amyloid. "
            "Bằng cách gắn với amyloid-beta, aducanumab thúc đẩy thanh thải amyloid-beta khỏi não "
            "thông qua microglia (tế bào miễn dịch trong não) và các cơ chế khác, "
            "làm giảm mảng amyloid trên PET và làm chậm suy giảm nhận thức trong Alzheimer giai đoạn sớm. "
            "Aducanumab được FDA phê duyệt năm 2021 dựa trên surrogate endpoint (giảm amyloid), "
            "mặc dù có tranh cãi về hiệu quả lâm sàng. "
            "Cơ chế này tương tự lecanemab và donanemab, nhưng aducanumab là thuốc đầu tiên được phê duyệt."
        ),
        "monitoring": [
            "MRI não trước khi bắt đầu điều trị",
            "MRI não định kỳ (ví dụ sau 3, 6, 12 tháng hoặc khi có triệu chứng) để phát hiện ARIA",
            "Triệu chứng thần kinh mới: đau đầu nặng, lú lẫn, nhìn đôi, mất thăng bằng, co giật",
            "Dấu hiệu xuất huyết nội sọ (đột ngột đau đầu, yếu liệt khu trú)"
        ],
        "precautions": [
            "Nguy cơ ARIA cao hơn ở bệnh nhân mang APOE ε4 (đặc biệt đồng hợp tử)",
            "Ngừng hoặc hoãn liều nếu phát hiện ARIA-E/ARIA-H mức độ vừa-nặng trên MRI",
            "Thận trọng khi phối hợp thuốc chống đông hoặc kháng tiểu cầu liều cao",
            "Không khuyến cáo ở bệnh Alzheimer tiến triển (moderate-severe) hoặc không có bằng chứng amyloid",
            "Liều tăng dần từ 1mg/kg → 3mg/kg → 6mg/kg → 10mg/kg để giảm nguy cơ ARIA"
        ],
        "pharmacokinetics": {
            "half_life": "Khoảng 24 ngày",
            "onset": "Giảm amyloid trên PET trong vài tháng; hiệu quả lâm sàng sau nhiều tháng",
            "duration": "Dùng duy trì lâu dài mỗi 4 tuần",
            "protein_binding": "IgG1 monoclonal antibody",
            "metabolism": "Thoái hóa thành peptide/acid amin qua RES",
            "clearance": "Không phụ thuộc gan thận đáng kể"
        },
        "storage": "Bảo quản lọ thuốc trong tủ lạnh (2–8°C), tránh đông lạnh, tránh ánh sáng. Dung dịch pha loãng dùng trong thời gian theo khuyến cáo hãng (thường ≤24 giờ ở 2–8°C).",
        "black_box_warnings": (
            "Nguy cơ ARIA (phù mạch/mikro xuất huyết não); có báo cáo xuất huyết não nghiêm trọng, "
            "đặc biệt khi dùng cùng thuốc chống đông. "
            "Cần theo dõi MRI trước và trong điều trị. "
            "Nguy cơ ARIA cao hơn ở bệnh nhân có 2 allele APOE ε4/ε4."
        ),
        "drug_interactions": {
            "major": [
                {
                    "drug": "Thuốc chống đông (warfarin, DOACs)",
                    "mechanism": "Kết hợp với ARIA-H làm tăng nguy cơ xuất huyết não",
                    "effect": "Tăng nguy cơ chảy máu nội sọ",
                    "management": "Chỉ dùng khi thật cần; cân nhắc tránh phối hợp hoặc theo dõi MRI sát"
                }
            ],
            "moderate": [
                {
                    "drug": "Kháng tiểu cầu liều cao",
                    "mechanism": "Tăng nguy cơ xuất huyết",
                    "effect": "Tăng nguy cơ vi xuất huyết/máu tụ",
                    "management": "Dùng liều thấp nhất có hiệu quả; theo dõi lâm sàng và MRI"
                }
            ],
            "minor": []
        },
        "contraindications_detail": {
            "tuyệt_đối": [
                "Dị ứng aducanumab",
                "Tiền sử phản vệ với kháng thể đơn dòng tương tự"
            ],
            "tương_đối": [
                "Tiền sử xuất huyết nội sọ",
                "Nhiều vi xuất huyết hoặc tổn thương hemosiderin lan tỏa trên MRI",
                "Đang dùng chống đông",
                "Bệnh Alzheimer không có amyloid trên PET/CSF"
            ]
        },
        "pregnancy_lactation": {
            "fda_category": "Chưa phân loại; tránh dùng",
            "pregnancy_details": "Thiếu dữ liệu trên người; về lý thuyết có thể đi qua nhau thai như IgG khác, nên tránh trừ khi lợi ích vượt trội.",
            "lactation": {
                "safety": "Không rõ",
                "details": "Chưa rõ bài tiết sữa mẹ; kháng thể lớn, hấp thu qua đường tiêu hóa trẻ có thể hạn chế.",
                "recommendation": "Cân nhắc ngừng cho bú hoặc không dùng thuốc."
            }
        },
        "hepatic_adjustment": {
            "mild": "Không cần chỉnh liều",
            "moderate": "Không cần chỉnh liều; dữ liệu hạn chế",
            "severe": "Dữ liệu hạn chế; dùng thận trọng",
            "notes": "Aducanumab chuyển hóa qua RES, không phụ thuộc gan đáng kể."
        },
        "overdose_management": {
            "symptoms": [
                "Tăng nguy cơ ARIA",
                "Triệu chứng thần kinh khu trú hoặc toàn thể"
            ],
            "antidote": "Không có antidote đặc hiệu",
            "treatment": [
                "Ngừng thuốc",
                "MRI não khẩn để tìm ARIA/ xuất huyết",
                "Điều trị hỗ trợ thần kinh, ICU nếu cần"
            ],
            "monitoring": "Triệu chứng thần kinh, MRI, dấu hiệu sinh tồn"
        },
        "reversal_agents": {
            "available": False,
            "agents": []
        },
        "administration_instructions": {
            "iv": {
                "reconstitution": "Pha loãng trong dung dịch NaCl 0.9% theo hướng dẫn hãng, đạt nồng độ khuyến cáo.",
                "infusion_rate": "Truyền tĩnh mạch trong khoảng 1 giờ; theo dõi trong và sau truyền.",
                "compatibility": ["NaCl 0.9%"],
                "incompatibility": ["Không pha lẫn thuốc khác cùng đường truyền"],
                "notes": "Theo dõi phản ứng quá mẫn, ARIA; cần MRI baseline và định kỳ. Liều tăng dần: 1mg/kg → 3mg/kg → 6mg/kg → 10mg/kg."
            }
        },
        "references": {
            "primary_sources": [
                "FDA Drug Label - Aducanumab (Aduhelm)",
                "UpToDate - Aducanumab: Drug information",
                "Lexicomp - Aducanumab monograph",
                "AAN/Alzheimer Association practice updates"
            ],
            "last_updated": "2025-02-18",
            "evidence_level": "B - FDA-approved 2021 based on surrogate endpoint (amyloid reduction), controversial clinical benefit"
        }
    },
    "Donanemab":     {
        "group": "Neurology - Anti-amyloid Monoclonal Antibody",
        "vietnamese_name": "Donanemab, Kisunla",
        "administration": [
            "IV"
    ],
        "indications": [
            "Bệnh Alzheimer giai đoạn sớm (MCI hoặc mild dementia) với bằng chứng tích tụ amyloid và tau"
    ],
        "contraindications": [
            "Dị ứng donanemab hoặc thành phần thuốc",
            "Không có bằng chứng amyloid/tau (không nên dùng)"
    ],
        "dosage": {
            "adult_standard": """Dùng IV mỗi 4 tuần, liều tăng dần theo phác đồ hãng (ví dụ 700 mg → 1400 mg mỗi 4 tuần). Có thể ngừng sau khi đạt mức giảm amyloid mục tiêu trên PET.""",
            "notes": "Cần theo đúng phác đồ từng giai đoạn; cần MRI baseline và theo dõi định kỳ ARIA.",
        },
        "renal_adjustment": {
            "normal": "Không cần chỉnh liều",
            "30_60": "Không cần chỉnh liều; theo dõi",
            "under_30": "Dữ liệu hạn chế; thận trọng",
        },
        "side_effects": [
            "ARIA-E, ARIA-H (phù/vi xuất huyết não liên quan amyloid)",
            "Nhức đầu",
            "Các triệu chứng giống cúm sau truyền",
            "Buồn nôn",
            "Phản ứng quá mẫn liên quan truyền"
    ],
        "interactions": [
            "Thuốc chống đông/kháng tiểu cầu: lý thuyết tăng nguy cơ xuất huyết khi ARIA-H"
    ],
        "pregnancy": "Chưa có dữ liệu, tránh dùng nếu có thể",
        "mechanism_of_action": """Donanemab là kháng thể đơn dòng nhắm vào dạng amyloid-beta đã biến đổi (p3) trong mảng amyloid trưởng thành. Gắn và thúc đẩy thanh thải mảng amyloid khỏi não, làm giảm tín hiệu PET và làm chậm suy giảm nhận thức trong Alzheimer giai đoạn sớm.""",
        "monitoring": [
            "MRI não trước điều trị",
            "MRI định kỳ trong năm đầu (ví dụ trước vài liều đầu) để phát hiện ARIA",
            "Triệu chứng thần kinh khu trú, co giật, thay đổi ý thức",
            "Dấu hiệu xuất huyết nội sọ"
    ],
        "precautions": [
            "ARIA là biến chứng chính; nguy cơ tăng ở APOE ε4 carriers",
            "Tạm ngừng hoặc ngừng hẳn nếu ARIA mức độ vừa-nặng hoặc có triệu chứng",
            "Thận trọng với thuốc chống đông/kháng tiểu cầu liều cao",
            "Chỉ dùng cho bệnh nhân có xác nhận amyloid (và thường cả tau) trên chẩn đoán hình ảnh/dịch não tủy"
    ],
        "pharmacokinetics": {
            "half_life": "Vài ngày đến ~2 tuần (kháng thể IgG)",
            "onset": "Giảm amyloid trên PET sau vài tháng; hiệu quả lâm sàng dần xuất hiện",
            "duration": "Hiệu ứng kéo dài sau khi dừng nếu amyloid đã giảm đáng kể",
            "protein_binding": "IgG1 monoclonal antibody",
            "metabolism": "Thoái hóa qua RES thành peptide/acid amin",
            "clearance": "Không phụ thuộc gan thận đáng kể",
        },
        "storage": """Bảo quản lọ trong tủ lạnh (2–8°C), tránh đông lạnh, tránh ánh sáng. Dung dịch pha loãng dùng trong thời gian khuyến cáo.""",
        "black_box_warnings": "ARIA (phù/ xuất huyết não) và xuất huyết nội sọ hiếm nhưng nghiêm trọng.",
        "drug_interactions": {
            "major": [
    {
                    "drug": "Thuốc chống đông đường uống",
                    "mechanism": "Giảm dự trữ đông máu trong bối cảnh ARIA-H",
                    "effect": "Tăng nguy cơ chảy máu nội sọ",
                    "management": "Tránh nếu có thể; nếu bắt buộc, theo dõi MRI/triệu chứng sát",
                }
                ],
            "moderate": [
    {
                    "drug": "Kháng tiểu cầu",
                    "mechanism": "Tăng nguy cơ xuất huyết",
                    "effect": "Tăng nguy cơ vi xuất huyết/máu tụ",
                    "management": "Dùng liều thấp nhất, theo dõi lâm sàng/MRI",
                }
                ],
            "minor": [],
        },
        "contraindications_detail": {
            "tuyệt_đối": [
                "Dị ứng donanemab",
                "Tiền sử phản vệ với kháng thể đơn dòng tương tự"
    ],
            "tương_đối": [
                "Tiền sử xuất huyết nội sọ hoặc nhiều vi xuất huyết trên MRI",
                "Đang dùng chống đông",
                "Không có bằng chứng amyloid/tau"
    ],
        },
        "pregnancy_lactation": {
            "fda_category": "Chưa phân loại; tránh dùng",
            "pregnancy_details": "Thiếu dữ liệu; cân nhắc tránh.",
            "lactation": {
                "safety": "Không rõ",
                "details": "Chưa rõ bài tiết sữa mẹ; hấp thu ở trẻ có thể thấp.",
                "recommendation": "Cân nhắc ngừng cho bú hoặc không dùng thuốc.",
            },
        },
        "hepatic_adjustment": {
            "mild": "Không cần chỉnh liều",
            "moderate": "Không cần chỉnh; dữ liệu hạn chế",
            "severe": "Thận trọng, dữ liệu hạn chế",
            "notes": "",
        },
        "overdose_management": {
            "symptoms": [
                "Gia tăng nguy cơ ARIA",
                "Triệu chứng thần kinh cấp"
    ],
            "antidote": "Không có antidote đặc hiệu",
            "treatment": [
                "Ngừng thuốc",
                "MRI não khẩn",
                "Điều trị hỗ trợ, ICU nếu cần"
    ],
            "monitoring": "Triệu chứng thần kinh, MRI, dấu hiệu sinh tồn",
        },
        "reversal_agents": {
            "available": False,
            "agents": [],
        },
        "administration_instructions": {
            "iv": {
                "reconstitution": "Pha với NaCl 0.9% theo khuyến cáo hãng.",
                "infusion_rate": "Truyền tĩnh mạch trong ≥30–60 phút (tùy liều); theo dõi trong và sau truyền.",
                "compatibility": [
                    "NaCl 0.9%"
    ],
                "incompatibility": [
                    "Không pha chung với thuốc khác"
    ],
                "notes": "Theo dõi phản ứng truyền, ARIA; cần MRI baseline và định kỳ.",
            },
        },
        "references": {
            "primary_sources": [
                "FDA Drug Label - Donanemab (Kisunla)",
                "NEJM 2024 - Phase 3 donanemab trial",
                "AAN/Alzheimer Association practice updates"
    ],
            "last_updated": "2025-02-18",
            "evidence_level": "A - FDA-approved 2024, large phase 3 RCT",
        },
    },
    "Donepezil": {'group': 'Neurology - Cholinesterase Inhibitor',
        "pregnancy": "C - Nguy cơ không thể loại trừ. Không khuyến nghị trong thai kỳ",
        'vietnamese_name': 'Donepezil, Aricept', 'administration': ['PO'],
        'indications': [
        'Bệnh Alzheimer (mild to moderate dementia)',
        'Bệnh Alzheimer (moderate to severe dementia)'], 'contraindications': [
        'Dị ứng', 'Bệnh tim nặng (block nhĩ thất, rối loạn nhịp nặng)'],
        'dosage': {'adult_mild_moderate': '5mg/ngày, tăng đến 10mg/ngày sau 4-6 tuần',
        'adult_moderate_severe': '10mg/ngày, có thể tăng đến 23mg/ngày (extended release)',
        'adult_max': '23mg/ngày (extended release)', 'notes':
        'Uống buổi tối với thức ăn. Tăng liều chậm để giảm tác dụng phụ'}, 'side_effects': [
        'Buồn nôn, nôn', 'Tiêu chảy', 'Mất ngủ', 'Chóng mặt', 'Nhức đầu',
        'Chán ăn, giảm cân', 'Co thắt cơ (muscle cramps)', 'Mệt mỏi',
        'Chậm nhịp tim (bradycardia)', 'Ngất (syncope)'], 'interactions': [
        'Anticholinergics: đối kháng tác dụng donepezil',
        'Cholinergic drugs: tăng tác dụng, tăng tác dụng phụ',
        'Succinylcholine: tăng tác dụng, tăng nguy cơ kéo dài block thần kinh cơ',
        'Beta-blockers: tăng nguy cơ chậm nhịp tim'],
        'mechanism_of_action':
        'Donepezil là thuốc ức chế cholinesterase (acetylcholinesterase inhibitor) có tính chọn lọc, không thể đảo ngược. Ức chế enzyme acetylcholinesterase ở synap thần kinh, làm giảm phân hủy acetylcholine và tăng nồng độ acetylcholine trong synap. Acetylcholine là chất dẫn truyền thần kinh quan trọng cho trí nhớ và nhận thức. Trong bệnh Alzheimer, có sự suy giảm cholinergic (giảm acetylcholine). Donepezil làm tăng nồng độ acetylcholine, cải thiện chức năng nhận thức (trí nhớ, suy nghĩ, hành vi) ở bệnh nhân Alzheimer. Tác dụng: cải thiện nhận thức, hành vi, và hoạt động hàng ngày. Donepezil có half-life dài (70 giờ), cho phép dùng 1 lần/ngày.'
        , 'monitoring': [
        'Đáp ứng điều trị: cải thiện nhận thức, hành vi, hoạt động hàng ngày (đánh giá bằng MMSE, ADAS-Cog)'
        , 'Tác dụng phụ tiêu hóa: buồn nôn, nôn, tiêu chảy (phổ biến, thường tự khỏi sau vài tuần)'
        , 'Nhịp tim: chậm nhịp tim (bradycardia) - nguy hiểm, đặc biệt ở bệnh nhân có bệnh tim'
        , 'Ngất (syncope) - có thể xảy ra do chậm nhịp tim',
        'Cân nặng: chán ăn, giảm cân - theo dõi cân nặng',
        'Giấc ngủ: mất ngủ - có thể cần dùng buổi sáng thay vì buổi tối',
        'Tương tác với anticholinergics (đối kháng), cholinergic drugs (tăng tác dụng)'], 'precautions': [
        'Uống buổi tối với thức ăn để giảm buồn nôn (tác dụng phụ phổ biến nhất)',
        'Tăng liều chậm (5mg → 10mg sau 4-6 tuần) để giảm tác dụng phụ',
        'Buồn nôn, nôn, tiêu chảy - phổ biến, thường tự khỏi sau vài tuần, có thể giảm bằng cách uống với thức ăn'
        'CHẬM NHỊP TIM (bradycardia) - nguy hiểm, đặc biệt ở bệnh nhân có bệnh tim, block nhĩ thất, dùng beta-blockers'
        , 'Ngất (syncope) - có thể xảy ra do chậm nhịp tim, thận trọng',
        'Mất ngủ - có thể cần dùng buổi sáng thay vì buổi tối',
        'Chán ăn, giảm cân - theo dõi cân nặng',
        'CHỐNG CHỈ ĐỊNH trong bệnh tim nặng (block nhĩ thất, rối loạn nhịp nặng)',
        'Thận trọng khi dùng với beta-blockers (tăng nguy cơ chậm nhịp tim)',
        'Thận trọng khi dùng với anticholinergics (đối kháng tác dụng donepezil)',
        'Thận trọng khi dùng với cholinergic drugs (tăng tác dụng, tăng tác dụng phụ)',
        'Thận trọng với bệnh nhân có tiền sử loét dạ dày (tăng acid dạ dày)',
        'Không ngừng đột ngột (có thể làm tăng triệu chứng)'], 'pharmacokinetics': {
        'half_life': '70 giờ (rất dài, cho phép dùng 1 lần/ngày)', 'onset':
        'Vài tuần (tác dụng chậm)', 'duration': 'Dài (do half-life rất dài)',
        'protein_binding': '96% (rất cao)', 'metabolism':
        'Gan (chuyển hóa qua CYP2D6, CYP3A4), thận (thải trừ)', 'clearance':
        'Gan (chuyển hóa), thận (thải trừ). Half-life rất dài (70 giờ) do gắn chặt với acetylcholinesterase.'}, 'storage':
        'Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm, tránh ánh sáng. Viên nén: bảo quản trong bao bì kín.'
        , 'black_box_warnings':
        'Nguy cơ chậm nhịp tim (bradycardia) nghiêm trọng, có thể gây ngất, block nhĩ thất, rối loạn nhịp tim. Nguy cơ tăng ở bệnh nhân có bệnh tim, dùng beta-blockers, hoặc có block nhĩ thất. CHỐNG CHỈ ĐỊNH trong bệnh tim nặng. Theo dõi nhịp tim. Nguy cơ tăng acid dạ dày, có thể làm nặng loét dạ dày.'
        , 'drug_interactions': {'major': [{'drug': 'Beta-blockers (propranolol, metoprolol)',
        'mechanism': 'Cả hai đều có thể gây chậm nhịp tim', 'effect':
        'Tăng nguy cơ chậm nhịp tim nghiêm trọng, block nhĩ thất, ngất', 'management':
        'Thận trọng. Theo dõi nhịp tim. Có thể cần giảm liều beta-blocker hoặc donepezil.'
        }, {'drug': 'Succinylcholine', 'mechanism':
        'Donepezil ức chế cholinesterase, tăng tác dụng succinylcholine', 'effect':
        'Tăng tác dụng, tăng nguy cơ kéo dài block thần kinh cơ', 'management':
        'Ngừng donepezil ít nhất 2 tuần trước phẫu thuật nếu có thể. Nếu không thể, thông báo cho bác sĩ gây mê.'
        }], 'moderate': [
        {'drug': 'Anticholinergics (atropine, scopolamine, benztropine)', 'mechanism': 'Đối kháng tác dụng cholinergic của donepezil', 'effect':
        'Giảm hiệu quả donepezil', 'management':
        'Tránh dùng chung nếu có thể. Nếu phải dùng, theo dõi đáp ứng điều trị.'}, {
        'drug': 'Cholinergic drugs (bethanechol, pilocarpine)', 'mechanism':
        'Tăng tác dụng cholinergic', 'effect': 'Tăng tác dụng phụ (buồn nôn, nôn, tiêu chảy)',
        'management': 'Thận trọng. Có thể cần giảm liều một trong hai thuốc.'}], 'minor': [
        {'drug': 'CYP2D6, CYP3A4 inhibitors', 'mechanism':
        'Ức chế chuyển hóa donepezil', 'effect': 'Tăng nồng độ donepezil, tăng tác dụng phụ',
        'management': 'Thận trọng. Có thể cần giảm liều donepezil.'}]},
        'contraindications': {'tuyệt_đối': [
        'Dị ứng donepezil hoặc các thành phần khác',
        'Bệnh tim nặng (block nhĩ thất độ II-III, rối loạn nhịp nặng)'], 'tương_đối': [
        'Bệnh tim mạch (suy tim, block nhĩ thất độ I) - tăng nguy cơ chậm nhịp tim',
        'Loét dạ dày - tăng acid dạ dày, có thể làm nặng loét',
        'Bệnh phổi (COPD, hen) - tăng co thắt phế quản',
        'Suy gan nặng - giảm chuyển hóa, tăng nguy cơ tích lũy',
        'Suy thận nặng (CrCl <30) - giảm thải trừ, tăng nguy cơ tích lũy',
        'Dùng với beta-blockers - tăng nguy cơ chậm nhịp tim',
        'Bệnh nhân lớn tuổi - tăng nguy cơ tác dụng phụ']},
        'contraindications_detail': {'tuyệt_đối': [
        'Dị ứng donepezil hoặc các thành phần khác',
        'Bệnh tim nặng (block nhĩ thất độ II-III, rối loạn nhịp nặng)'], 'tương_đối': [
        'Bệnh tim mạch (suy tim, block nhĩ thất độ I) - tăng nguy cơ chậm nhịp tim',
        'Loét dạ dày - tăng acid dạ dày, có thể làm nặng loét',
        'Bệnh phổi (COPD, hen) - tăng co thắt phế quản',
        'Suy gan nặng - giảm chuyển hóa, tăng nguy cơ tích lũy',
        'Suy thận nặng (CrCl <30) - giảm thải trừ, tăng nguy cơ tích lũy',
        'Dùng với beta-blockers - tăng nguy cơ chậm nhịp tim',
        'Bệnh nhân lớn tuổi - tăng nguy cơ tác dụng phụ']},
        'renal_adjustment': {'normal': 'Không cần chỉnh liều', '30_60': 'Thận trọng, có thể cần giảm liều',
        'under_30': 'Thận trọng, giảm liều (thải trừ qua thận)', 'dialysis': 'Thận trọng, giảm liều. Donepezil không được lọc sạch hiệu quả qua thẩm phân máu.',
        'notes': 'Donepezil thải trừ một phần qua thận. Suy thận có thể tăng nguy cơ tích lũy, đặc biệt với half-life dài (70 giờ). Giảm liều và theo dõi chặt chẽ ở suy thận.'}, 'pregnancy_lactation': {
        'fda_category': 'C', 'pregnancy_details':
        'Chứng cứ về an toàn trong thai kỳ còn hạn chế. Donepezil thường không được dùng trong thai kỳ vì bệnh Alzheimer chủ yếu ở người già. Chỉ dùng nếu lợi ích điều trị vượt trội nguy cơ.'
        , 'lactation': {'safety': 'Unknown', 'details':
        'Không có dữ liệu về bài tiết donepezil vào sữa mẹ. Thận trọng khi dùng khi cho con bú.'
        , 'recommendation':
        'Tránh dùng khi cho con bú nếu có thể. Nếu phải dùng, theo dõi trẻ sát về dấu hiệu tác dụng phụ cholinergic.'
        }}, 'hepatic_adjustment': {'mild': 'Không đổi hoặc giảm liều nhẹ',
        'moderate': 'Giảm liều 25-50%. Theo dõi chức năng gan', 'severe':
        'Giảm liều 50% hoặc tránh dùng. Theo dõi chức năng gan chặt chẽ', 'notes':
        'Donepezil chuyển hóa ở gan qua CYP2D6, CYP3A4. Suy gan làm giảm chuyển hóa, tăng nguy cơ tích lũy và tác dụng phụ.'},
        'overdose_management': {'symptoms': [
        'Triệu chứng cholinergic quá mức: buồn nôn, nôn, tiêu chảy, tăng tiết nước bọt, đổ mồ hôi'
        , 'Chậm nhịp tim (bradycardia) nghiêm trọng, block nhĩ thất',
        'Co thắt phế quản, suy hô hấp',
        'Co giật (hiếm)',
        'Hôn mê (hiếm)'],
        'treatment': [
        'Đánh giá đường thở, hô hấp, tuần hoàn. Hỗ trợ hô hấp nếu cần',
        'Rửa dạ dày nếu trong vòng 1-2 giờ sau uống (nếu bệnh nhân tỉnh táo)',
        'Than hoạt tính: 1g/kg (tối đa 50-100g) nếu trong vòng 1-2 giờ',
        'Atropine: 0.5-1mg IV (có thể lặp) để đối kháng tác dụng cholinergic',
        'Theo dõi liên tục: ý thức, hô hấp, tim mạch (nhịp tim)',
        'Xử trí chậm nhịp tim: atropine, pacemaker nếu cần',
        'Xử trí co thắt phế quản: albuterol, ipratropium',
        'Hỗ trợ hô hấp: thở máy nếu suy hô hấp'], 'monitoring':
        'Theo dõi ý thức, hô hấp, tim mạch (nhịp tim), dấu hiệu cholinergic quá mức'},
        'reversal_agents': {'available': True, 'agents': [{'agent': 'Atropine',
        'mechanism': 'Anticholinergic, đối kháng tác dụng cholinergic', 'indication':
        'Quá liều gây triệu chứng cholinergic quá mức, chậm nhịp tim', 'caution':
        'Dùng thận trọng, theo dõi nhịp tim'}], 'notes':
        'Atropine là antidote cho quá liều donepezil. Dùng để đối kháng tác dụng cholinergic quá mức.'},
        'administration_instructions': {'oral': {'with_food':
        'Uống với thức ăn để giảm buồn nôn (tác dụng phụ phổ biến nhất)', 'timing':
        'Uống 1 lần/ngày vào buổi tối với thức ăn. Có thể chuyển sang buổi sáng nếu gây mất ngủ. Tăng liều chậm (5mg → 10mg sau 4-6 tuần).'
        }, 'iv': {'reconstitution': 'Không có dạng IV', 'infusion_rate': 'N/A',
        'compatibility': [], 'incompatibility': []}},
        'references': {'primary_sources': ['Lexicomp - Donepezil',
        'UpToDate - Donepezil: Drug information',
        'FDA - Aricept (donepezil) prescribing information',
        "Goodman & Gilman's The Pharmacological Basis of Therapeutics, 13th ed."
        ], 'evidence_level':
        'A - Evidence from well-designed randomized controlled trials and systematic reviews'
        }},
    "Lecanemab":     {
        "group": "Neurology - Anti-amyloid Monoclonal Antibody",
        "vietnamese_name": "Lecanemab, Leqembi",
        "administration": [
            "IV"
    ],
        "indications": [
            "Bệnh Alzheimer giai đoạn đầu (mild cognitive impairment hoặc mild dementia) với bằng chứng tích tụ amyloid (PET hoặc CSF)"
    ],
        "contraindications": [
            "Dị ứng lecanemab hoặc thành phần thuốc",
            "Bệnh nhân không có bằng chứng amyloid (không nên dùng)"
    ],
        "dosage": {
            "adult_standard": "10 mg/kg IV mỗi 2 tuần",
            "notes": "Truyền trong khoảng 1 giờ. Cần MRI nền (baseline) và theo dõi định kỳ để phát hiện ARIA.",
        },
        "renal_adjustment": {
            "normal": "Không cần chỉnh liều",
            "30_60": "Không cần chỉnh liều; dữ liệu hạn chế, theo dõi",
            "under_30": "Dữ liệu hạn chế; thận trọng",
        },
        "side_effects": [
            "ARIA-E ( phù mạch não liên quan amyloid )",
            "ARIA-H (vi xuất huyết, lắng đọng hemosiderin)",
            "Nhức đầu",
            "Đau tại vị trí truyền",
            "Buồn nôn",
            "Các triệu chứng giống cúm sau truyền"
    ],
        "interactions": [
            "Thuốc chống đông/kháng tiểu cầu liều cao: có thể tăng nguy cơ xuất huyết não khi ARIA-H"
    ],
        "pregnancy": "Chưa có dữ liệu, tránh dùng nếu có thể",
        "mechanism_of_action": """Lecanemab là kháng thể đơn dòng người hóa, nhắm vào dạng protofibril hòa tan của amyloid-beta. Gắn kết và thúc đẩy thanh thải amyloid-beta khỏi não, làm giảm mảng amyloid trên PET và làm chậm suy giảm nhận thức trong Alzheimer giai đoạn sớm.""",
        "monitoring": [
            "MRI não trước khi bắt đầu điều trị",
            "MRI não định kỳ (ví dụ sau 3, 6, 12 tháng hoặc khi có triệu chứng) để phát hiện ARIA",
            "Triệu chứng thần kinh mới: đau đầu nặng, lú lẫn, nhìn đôi, mất thăng bằng, co giật",
            "Dấu hiệu xuất huyết nội sọ (đột ngột đau đầu, yếu liệt khu trú)"
    ],
        "precautions": [
            "Nguy cơ ARIA cao hơn ở bệnh nhân mang APOE ε4 (đặc biệt đồng hợp tử)",
            "Ngừng hoặc hoãn liều nếu phát hiện ARIA-E/ARIA-H mức độ vừa-nặng trên MRI",
            "Thận trọng khi phối hợp thuốc chống đông hoặc kháng tiểu cầu liều cao",
            "Không khuyến cáo ở bệnh Alzheimer tiến triển (moderate-severe) hoặc không có bằng chứng amyloid"
    ],
        "pharmacokinetics": {
            "half_life": "Khoảng 5–7 ngày",
            "onset": "Giảm amyloid trên PET trong vài tháng; hiệu quả lâm sàng sau nhiều tháng",
            "duration": "Dùng duy trì lâu dài mỗi 2 tuần",
            "protein_binding": "IgG1 monoclonal antibody",
            "metabolism": "Thoái hóa thành peptide/acid amin qua RES",
            "clearance": "Không phụ thuộc gan thận đáng kể",
        },
        "storage": """Bảo quản lọ thuốc trong tủ lạnh (2–8°C), tránh đông lạnh, tránh ánh sáng. Dung dịch pha loãng dùng trong thời gian theo khuyến cáo hãng (thường ≤24 giờ ở 2–8°C).""",
        "black_box_warnings": """Nguy cơ ARIA (phù mạch/mikro xuất huyết não); có báo cáo xuất huyết não nghiêm trọng, đặc biệt khi dùng cùng thuốc chống đông.""",
        "drug_interactions": {
            "major": [
    {
                    "drug": "Thuốc chống đông (warfarin, DOACs)",
                    "mechanism": "Kết hợp với ARIA-H làm tăng nguy cơ xuất huyết não",
                    "effect": "Tăng nguy cơ chảy máu nội sọ",
                    "management": "Chỉ dùng khi thật cần; cân nhắc tránh phối hợp hoặc theo dõi MRI sát",
                }
                ],
            "moderate": [
    {
                    "drug": "Kháng tiểu cầu liều cao",
                    "mechanism": "Tăng nguy cơ xuất huyết",
                    "effect": "Tăng nguy cơ vi xuất huyết/máu tụ",
                    "management": "Dùng liều thấp nhất có hiệu quả; theo dõi lâm sàng và MRI",
                }
                ],
            "minor": [],
        },
        "contraindications_detail": {
            "tuyệt_đối": [
                "Dị ứng lecanemab",
                "Tiền sử phản vệ với kháng thể đơn dòng tương tự"
    ],
            "tương_đối": [
                "Tiền sử xuất huyết nội sọ",
                "Nhiều vi xuất huyết hoặc tổn thương hemosiderin lan tỏa trên MRI",
                "Đang dùng chống đông",
                "Bệnh Alzheimer không có amyloid trên PET/CSF"
    ],
        },
        "pregnancy_lactation": {
            "fda_category": "Chưa phân loại; tránh dùng",
            "pregnancy_details": """Thiếu dữ liệu trên người; về lý thuyết có thể đi qua nhau thai như IgG khác, nên tránh trừ khi lợi ích vượt trội.""",
            "lactation": {
                "safety": "Không rõ",
                "details": "Chưa rõ bài tiết sữa mẹ; kháng thể lớn, hấp thu qua đường tiêu hóa trẻ có thể hạn chế.",
                "recommendation": "Cân nhắc ngừng cho bú hoặc không dùng thuốc.",
            },
        },
        "hepatic_adjustment": {
            "mild": "Không cần chỉnh liều",
            "moderate": "Không cần chỉnh liều; dữ liệu hạn chế",
            "severe": "Dữ liệu hạn chế; dùng thận trọng",
            "notes": "",
        },
        "overdose_management": {
            "symptoms": [
                "Tăng nguy cơ ARIA",
                "Triệu chứng thần kinh khu trú hoặc toàn thể"
    ],
            "antidote": "Không có antidote đặc hiệu",
            "treatment": [
                "Ngừng thuốc",
                "MRI não khẩn để tìm ARIA/ xuất huyết",
                "Điều trị hỗ trợ thần kinh, ICU nếu cần"
    ],
            "monitoring": "Triệu chứng thần kinh, MRI, dấu hiệu sinh tồn",
        },
        "reversal_agents": {
            "available": False,
            "agents": [],
        },
        "administration_instructions": {
            "iv": {
                "reconstitution": "Pha loãng trong dung dịch NaCl 0.9% theo hướng dẫn hãng, đạt nồng độ khuyến cáo.",
                "infusion_rate": "Truyền trong khoảng 1 giờ; theo dõi trong và sau truyền.",
                "compatibility": [
                    "NaCl 0.9%"
    ],
                "incompatibility": [
                    "Không pha lẫn thuốc khác cùng đường truyền"
    ],
                "notes": "Theo dõi phản ứng quá mẫn, ARIA; cần MRI baseline và định kỳ.",
            },
        },
        "references": {
            "primary_sources": [
                "FDA Drug Label - Lecanemab (Leqembi)",
                "NEJM 2023 - Phase 3 lecanemab trial",
                "AAN/Alzheimer Association practice updates"
    ],
            "last_updated": "2025-02-18",
            "evidence_level": "A - FDA-approved 2023, large phase 3 RCT",
        },
    },
    "Memantine": {'group': 'Neurology - NMDA Receptor Antagonist',
        "pregnancy": "B - Không có bằng chứng về nguy cơ ở người",
        'vietnamese_name': 'Memantine, Namenda', 'administration': ['PO'],
        'indications': [
        'Bệnh Alzheimer (moderate to severe dementia)',
        'Bệnh Alzheimer (có thể dùng kết hợp với donepezil)'], 'contraindications': [
        'Dị ứng', 'Suy thận nặng (CrCl <30)'], 'dosage': {'adult_standard':
        '5mg/ngày, tăng dần đến 10mg x 2 lần/ngày (tối đa 20mg/ngày)', 'adult_max':
        '20mg/ngày', 'notes':
        'Tăng liều chậm (5mg → 10mg → 15mg → 20mg, mỗi tuần tăng 5mg)'}, 'side_effects': [
        'Chóng mặt', 'Nhức đầu', 'Táo bón', 'Buồn nôn', 'Mệt mỏi',
        'Lú lẫn (hiếm, thường khi tăng liều quá nhanh)'], 'interactions': [
        'Urine alkalinizers (sodium bicarbonate, carbonic anhydrase inhibitors): giảm thải trừ memantine, tăng nồng độ',
        'Acetazolamide: giảm thải trừ memantine',
        'Cimetidine, ranitidine: có thể tăng nồng độ memantine nhẹ'],
        'mechanism_of_action':
        'Memantine là thuốc đối kháng thụ thể NMDA (N-methyl-D-aspartate receptor antagonist) không cạnh tranh, có ái lực thấp. Trong bệnh Alzheimer, có sự kích thích quá mức của thụ thể NMDA bởi glutamate (chất dẫn truyền thần kinh kích thích), dẫn đến độc tính thần kinh (excitotoxicity) và chết tế bào thần kinh. Memantine ức chế thụ thể NMDA, giảm kích thích quá mức và bảo vệ tế bào thần kinh. Khác với các thuốc đối kháng NMDA khác (như ketamine), memantine có ái lực thấp và không cạnh tranh, nên ít gây tác dụng phụ thần kinh (lú lẫn, ảo giác) hơn. Memantine được dùng trong bệnh Alzheimer moderate to severe, có thể dùng đơn độc hoặc kết hợp với donepezil. Tác dụng: cải thiện nhận thức, hành vi, và hoạt động hàng ngày.'
        , 'monitoring': [
        'Đáp ứng điều trị: cải thiện nhận thức, hành vi, hoạt động hàng ngày',
        'Tác dụng phụ thần kinh: chóng mặt, nhức đầu, lú lẫn (thường khi tăng liều quá nhanh)'
        , 'Chức năng thận (creatinine, eGFR) - điều chỉnh liều ở suy thận (quan trọng)'
        , 'Tương tác với urine alkalinizers (giảm thải trừ, tăng nồng độ)'], 'precautions': [
        'Tăng liều chậm (5mg → 10mg → 15mg → 20mg, mỗi tuần tăng 5mg) để giảm tác dụng phụ'
        'Chóng mặt, nhức đầu - phổ biến, thường tự khỏi sau vài tuần, có thể giảm bằng cách tăng liều chậm'
        , 'Lú lẫn - hiếm, thường khi tăng liều quá nhanh, giảm liều nếu có',
        'Điều chỉnh liều ở suy thận QUAN TRỌNG: CrCl 30-60: giảm liều 50%; CrCl <30: chống chỉ định'
        , 'Thận trọng khi dùng với urine alkalinizers (sodium bicarbonate, acetazolamide) - giảm thải trừ, tăng nồng độ'
        , 'Thận trọng với bệnh nhân có tiền sử co giật (memantine có thể tăng nguy cơ co giật nhẹ)'
        , 'Có thể dùng kết hợp với donepezil (tác dụng bổ sung)',
        'Không ngừng đột ngột (có thể làm tăng triệu chứng)'], 'pharmacokinetics': {
        'half_life': '60-80 giờ (rất dài, cho phép dùng 1-2 lần/ngày)', 'onset':
        'Vài tuần (tác dụng chậm)', 'duration': 'Dài (do half-life rất dài)',
        'protein_binding': '45%', 'metabolism':
        'Thận (thải trừ chủ yếu nguyên dạng, ít chuyển hóa), gan (chuyển hóa một phần)',
        'clearance':
        'Thận: thải trừ chủ yếu nguyên dạng (80%), phụ thuộc pH nước tiểu (tăng thải trừ ở pH acid, giảm ở pH kiềm). Gan: chuyển hóa một phần. Half-life rất dài (60-80 giờ).'}, 'storage':
        'Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm, tránh ánh sáng. Viên nén: bảo quản trong bao bì kín.'
        , 'black_box_warnings':
        'Không có black box warning. Tuy nhiên, cần điều chỉnh liều ở suy thận (quan trọng). Nguy cơ lú lẫn khi tăng liều quá nhanh.'
        , 'drug_interactions': {'major': [{'drug':
        'Urine alkalinizers (sodium bicarbonate, acetazolamide, carbonic anhydrase inhibitors)',
        'mechanism':
        'Tăng pH nước tiểu, giảm thải trừ memantine (memantine thải trừ nhiều hơn ở pH acid)',
        'effect': 'Tăng nồng độ memantine, tăng tác dụng phụ', 'management':
        'Giảm liều memantine 50% khi dùng với urine alkalinizers. Theo dõi tác dụng phụ.'}],
        'moderate': [{'drug': 'Cimetidine, Ranitidine', 'mechanism':
        'Có thể giảm thải trừ memantine nhẹ', 'effect': 'Tăng nhẹ nồng độ memantine',
        'management': 'Thận trọng. Có thể cần giảm liều memantine nhẹ.'}], 'minor': []},
        'contraindications': {'tuyệt_đối': [
        'Dị ứng memantine hoặc các thành phần khác',
        'Suy thận nặng (CrCl <30) - chống chỉ định do giảm thải trừ'], 'tương_đối': [
        'Suy thận (CrCl 30-60) - giảm liều 50%',
        'Suy gan nặng - giảm liều',
        'Tiền sử co giật - tăng nguy cơ co giật nhẹ',
        'Dùng với urine alkalinizers - giảm thải trừ, tăng nồng độ',
        'Bệnh nhân lớn tuổi - tăng nguy cơ tác dụng phụ']}, 'pregnancy_lactation': {
        'fda_category': 'B', 'pregnancy_details':
        'Chứng cứ về an toàn trong thai kỳ còn hạn chế. Memantine thường không được dùng trong thai kỳ vì bệnh Alzheimer chủ yếu ở người già. Chỉ dùng nếu lợi ích điều trị vượt trội nguy cơ.'
        , 'lactation': {'safety': 'Unknown', 'details':
        'Không có dữ liệu về bài tiết memantine vào sữa mẹ. Thận trọng khi dùng khi cho con bú.'
        , 'recommendation':
        'Tránh dùng khi cho con bú nếu có thể. Nếu phải dùng, theo dõi trẻ sát.'}},
        'hepatic_adjustment': {'mild': 'Không đổi hoặc giảm liều nhẹ',
        'moderate': 'Giảm liều 25-50%. Theo dõi chức năng gan', 'severe':
        'Giảm liều 50% hoặc tránh dùng. Theo dõi chức năng gan chặt chẽ', 'notes':
        'Memantine chuyển hóa một phần ở gan. Suy gan làm giảm chuyển hóa, tăng nguy cơ tích lũy. Tuy nhiên, thải trừ chủ yếu qua thận, nên suy thận quan trọng hơn.'},
        'overdose_management': {'symptoms': [
        'Triệu chứng thần kinh: chóng mặt, nhức đầu, lú lẫn, mất điều hòa (ataxia)',
        'Rối loạn tiêu hóa: buồn nôn, nôn, táo bón',
        'Co giật (hiếm)',
        'Hôn mê (hiếm)'],
        'treatment': [
        'Đánh giá đường thở, hô hấp, tuần hoàn',
        'Rửa dạ dày nếu trong vòng 1-2 giờ sau uống',
        'Than hoạt tính nếu trong vòng 1-2 giờ',
        'Theo dõi liên tục: ý thức, hô hấp, tim mạch',
        'Xử trí co giật: benzodiazepine nếu có',
        'Acid hóa nước tiểu (vitamin C, ammonium chloride) để tăng thải trừ memantine'
        , 'Hỗ trợ hô hấp nếu cần'], 'monitoring':
        'Theo dõi ý thức, hô hấp, tim mạch, dấu hiệu co giật'},
        'reversal_agents': {'available': False, 'agents': [], 'notes':
        'Không có antidote đặc hiệu. Điều trị chủ yếu là hỗ trợ và điều trị triệu chứng. Ngừng thuốc ngay. Acid hóa nước tiểu có thể tăng thải trừ.'},
        'administration_instructions': {'oral': {'with_food':
        'Có thể dùng với hoặc không có thức ăn', 'timing':
        'Chia 2 lần/ngày (sáng, tối). Tăng liều chậm: 5mg/ngày x 1 tuần → 5mg x 2 lần/ngày x 1 tuần → 10mg buổi sáng + 5mg buổi tối x 1 tuần → 10mg x 2 lần/ngày. Có thể dùng kết hợp với donepezil.'
        }, 'iv': {'reconstitution': 'Không có dạng IV', 'infusion_rate': 'N/A',
        'compatibility': [], 'incompatibility': []}},
        'references': {'primary_sources': ['Lexicomp - Memantine',
        'UpToDate - Memantine: Drug information',
        'FDA - Namenda (memantine) prescribing information',
        "Goodman & Gilman's The Pharmacological Basis of Therapeutics, 13th ed."
        ], 'evidence_level':
        'A - Evidence from well-designed randomized controlled trials and systematic reviews'
        },
        "renal_adjustment": {
             "normal": "Không đổi",
             "30_60": "Thận trọng, có thể giảm liều",
             "under_30": "Giảm liều hoặc tránh dùng",
             "notes": "Cần tra cứu thêm thông tin chi tiết về điều chỉnh liều ở suy thận."
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

    "Rivastigmine": {'group': 'Neurology - Cholinesterase Inhibitor',
        "pregnancy": "B - Không có bằng chứng về nguy cơ ở người",
        'vietnamese_name': 'Rivastigmine, Exelon', 'administration': ['PO',
        'Transdermal'], 'indications': [
        'Bệnh Alzheimer (mild to moderate dementia)',
        'Bệnh Alzheimer (moderate to severe dementia)',
        'Dementia do bệnh Parkinson'], 'contraindications': [
        'Dị ứng', 'Bệnh tim nặng (block nhĩ thất, rối loạn nhịp nặng)'],
        'dosage': {'adult_po': '1.5mg x 2 lần/ngày, tăng dần đến 6-12mg/ngày (chia 2 lần)',
        'adult_transdermal': '4.6mg/24h patch, tăng đến 9.5mg/24h patch', 'adult_max':
        '12mg/ngày (PO) hoặc 13.3mg/24h (transdermal)', 'notes':
        'Uống với thức ăn. Dạng transdermal: ít tác dụng phụ hơn'}, 'side_effects': [
        'Buồn nôn, nôn (phổ biến hơn donepezil)', 'Tiêu chảy', 'Chán ăn, giảm cân',
        'Chóng mặt', 'Nhức đầu', 'Mệt mỏi', 'Chậm nhịp tim (bradycardia)',
        'Kích ứng da (transdermal patch)'], 'interactions': [
        'Anticholinergics: đối kháng tác dụng rivastigmine',
        'Cholinergic drugs: tăng tác dụng, tăng tác dụng phụ',
        'Succinylcholine: tăng tác dụng, tăng nguy cơ kéo dài block thần kinh cơ',
        'Beta-blockers: tăng nguy cơ chậm nhịp tim'],
        'mechanism_of_action':
        'Rivastigmine là thuốc ức chế cholinesterase (acetylcholinesterase và butyrylcholinesterase inhibitor) có tính chọn lọc, không thể đảo ngược. Ức chế cả acetylcholinesterase và butyrylcholinesterase ở synap thần kinh, làm giảm phân hủy acetylcholine và tăng nồng độ acetylcholine trong synap. Khác với donepezil, rivastigmine ức chế cả butyrylcholinesterase (có thể quan trọng trong bệnh Alzheimer). Rivastigmine có half-life ngắn (1.5 giờ), nhưng tác dụng kéo dài do gắn chặt với enzyme. Có dạng uống và dạng transdermal patch (ít tác dụng phụ tiêu hóa hơn). Tác dụng: cải thiện nhận thức, hành vi, và hoạt động hàng ngày ở bệnh nhân Alzheimer và dementia do bệnh Parkinson.'
        , 'monitoring': [
        'Đáp ứng điều trị: cải thiện nhận thức, hành vi, hoạt động hàng ngày',
        'Tác dụng phụ tiêu hóa: buồn nôn, nôn, tiêu chảy (phổ biến, đặc biệt với dạng uống)'
        , 'Nhịp tim: chậm nhịp tim (bradycardia) - nguy hiểm',
        'Cân nặng: chán ăn, giảm cân - theo dõi cân nặng',
        'Kích ứng da (nếu dùng transdermal patch) - thay vị trí dán patch',
        'Tương tác với anticholinergics (đối kháng), cholinergic drugs (tăng tác dụng)'], 'precautions': [
        'Uống với thức ăn để giảm buồn nôn (tác dụng phụ phổ biến nhất, đặc biệt với dạng uống)'
        , 'Dạng transdermal patch: ít tác dụng phụ tiêu hóa hơn dạng uống - nên dùng nếu có thể'
        , 'Tăng liều chậm để giảm tác dụng phụ',
        'Buồn nôn, nôn, tiêu chảy - phổ biến hơn donepezil, thường tự khỏi sau vài tuần',
        'CHẬM NHỊP TIM (bradycardia) - nguy hiểm, đặc biệt ở bệnh nhân có bệnh tim',
        'CHỐNG CHỈ ĐỊNH trong bệnh tim nặng (block nhĩ thất, rối loạn nhịp nặng)',
        'Thận trọng khi dùng với beta-blockers (tăng nguy cơ chậm nhịp tim)',
        'Thận trọng khi dùng với anticholinergics (đối kháng tác dụng)',
        'Thận trọng với bệnh nhân có tiền sử loét dạ dày',
        'Kích ứng da (transdermal patch) - thay vị trí dán patch mỗi ngày',
        'Không ngừng đột ngột (có thể làm tăng triệu chứng)'], 'pharmacokinetics': {
        'half_life': '1.5 giờ (ngắn), nhưng tác dụng kéo dài do gắn chặt với enzyme',
        'onset': 'Vài tuần (tác dụng chậm)', 'duration':
        'Dài (do gắn chặt với enzyme, mặc dù half-life ngắn)', 'protein_binding':
        '40%', 'metabolism':
        'Gan (chuyển hóa qua esterase, không phụ thuộc CYP450), thận (thải trừ)',
        'clearance':
        'Gan (chuyển hóa qua esterase, không phụ thuộc CYP450 - ít tương tác enzyme hơn), thận (thải trừ). Half-life ngắn nhưng tác dụng kéo dài do gắn chặt với enzyme.'}, 'storage':
        'Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm, tránh ánh sáng. Viên nén: bảo quản trong bao bì kín. Transdermal patch: bảo quản trong bao bì kín, tránh nhiệt độ cao.'
        , 'black_box_warnings':
        'Nguy cơ chậm nhịp tim (bradycardia) nghiêm trọng, có thể gây ngất, block nhĩ thất, rối loạn nhịp tim. Nguy cơ tăng ở bệnh nhân có bệnh tim, dùng beta-blockers. CHỐNG CHỈ ĐỊNH trong bệnh tim nặng. Theo dõi nhịp tim. Nguy cơ tăng acid dạ dày, có thể làm nặng loét dạ dày.'
        , 'drug_interactions': {'major': [{'drug': 'Beta-blockers', 'mechanism':
        'Cả hai đều có thể gây chậm nhịp tim', 'effect':
        'Tăng nguy cơ chậm nhịp tim nghiêm trọng', 'management':
        'Thận trọng. Theo dõi nhịp tim. Có thể cần giảm liều.'}, {'drug':
        'Succinylcholine', 'mechanism':
        'Rivastigmine ức chế cholinesterase, tăng tác dụng succinylcholine', 'effect':
        'Tăng tác dụng, tăng nguy cơ kéo dài block thần kinh cơ', 'management':
        'Ngừng rivastigmine ít nhất 2 tuần trước phẫu thuật nếu có thể.'}], 'moderate': [
        {'drug': 'Anticholinergics', 'mechanism': 'Đối kháng tác dụng cholinergic',
        'effect': 'Giảm hiệu quả rivastigmine', 'management':
        'Tránh dùng chung nếu có thể.'}, {'drug': 'Cholinergic drugs', 'mechanism':
        'Tăng tác dụng cholinergic', 'effect': 'Tăng tác dụng phụ', 'management':
        'Thận trọng. Có thể cần giảm liều.'}], 'minor': []}, 'contraindications': {
        'tuyệt_đối': [
        'Dị ứng rivastigmine hoặc các thành phần khác',
        'Bệnh tim nặng (block nhĩ thất độ II-III, rối loạn nhịp nặng)'], 'tương_đối': [
        'Bệnh tim mạch - tăng nguy cơ chậm nhịp tim',
        'Loét dạ dày - tăng acid dạ dày',
        'Bệnh phổi (COPD, hen) - tăng co thắt phế quản',
        'Suy gan nặng - giảm chuyển hóa',
        'Suy thận nặng (CrCl <30) - giảm thải trừ',
        'Dùng với beta-blockers - tăng nguy cơ chậm nhịp tim']},
        'pregnancy_lactation': {'fda_category': 'B', 'pregnancy_details':
        'Chứng cứ về an toàn trong thai kỳ còn hạn chế. Rivastigmine thường không được dùng trong thai kỳ vì bệnh Alzheimer chủ yếu ở người già. Chỉ dùng nếu lợi ích điều trị vượt trội nguy cơ.'
        , 'lactation': {'safety': 'Unknown', 'details':
        'Không có dữ liệu về bài tiết rivastigmine vào sữa mẹ. Thận trọng khi dùng khi cho con bú.'
        , 'recommendation':
        'Tránh dùng khi cho con bú nếu có thể. Nếu phải dùng, theo dõi trẻ sát.'}},
        'hepatic_adjustment': {'mild': 'Không đổi hoặc giảm liều nhẹ',
        'moderate': 'Giảm liều 25-50%. Theo dõi chức năng gan', 'severe':
        'Giảm liều 50% hoặc tránh dùng. Theo dõi chức năng gan chặt chẽ', 'notes':
        'Rivastigmine chuyển hóa ở gan qua esterase (không phụ thuộc CYP450). Suy gan làm giảm chuyển hóa, tăng nguy cơ tích lũy.'},
        'overdose_management': {'symptoms': [
        'Triệu chứng cholinergic quá mức: buồn nôn, nôn, tiêu chảy, tăng tiết nước bọt'
        , 'Chậm nhịp tim (bradycardia) nghiêm trọng',
        'Co thắt phế quản, suy hô hấp', 'Co giật (hiếm)'], 'antidote':
        'Atropine (anticholinergic)', 'treatment': [
        'Đánh giá đường thở, hô hấp, tuần hoàn',
        'Rửa dạ dày nếu trong vòng 1-2 giờ sau uống',
        'Than hoạt tính nếu trong vòng 1-2 giờ',
        'Atropine: 0.5-1mg IV (có thể lặp)',
        'Theo dõi liên tục: ý thức, hô hấp, tim mạch',
        'Xử trí chậm nhịp tim: atropine, pacemaker nếu cần',
        'Hỗ trợ hô hấp nếu cần'], 'monitoring':
        'Theo dõi ý thức, hô hấp, tim mạch, dấu hiệu cholinergic quá mức'},
        'reversal_agents': {'available': True, 'agents': [{'agent': 'Atropine',
        'mechanism': 'Anticholinergic', 'indication': 'Quá liều gây triệu chứng cholinergic quá mức',
        'caution': 'Dùng thận trọng'}]},
        'administration_instructions': {'oral': {'with_food':
        'Uống với thức ăn để giảm buồn nôn', 'timing':
        'Chia 2 lần/ngày (sáng, tối) với thức ăn. Tăng liều chậm. Dạng transdermal patch: dán 1 lần/ngày, thay vị trí mỗi ngày.'
        }, 'iv': {'reconstitution': 'Không có dạng IV', 'infusion_rate': 'N/A',
        'compatibility': [], 'incompatibility': []}},
        'references': {'primary_sources': ['Lexicomp - Rivastigmine',
        'UpToDate - Rivastigmine: Drug information',
        'FDA - Exelon (rivastigmine) prescribing information',
        "Goodman & Gilman's The Pharmacological Basis of Therapeutics, 13th ed."
        ], 'evidence_level':
        'A - Evidence from well-designed randomized controlled trials and systematic reviews'
        },
        "renal_adjustment": {
             "normal": "Không đổi",
             "30_60": "Thận trọng, có thể giảm liều",
             "under_30": "Giảm liều hoặc tránh dùng",
             "notes": "Cần tra cứu thêm thông tin chi tiết về điều chỉnh liều ở suy thận."
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

__all__ = ['ALZHEIMER_DEMENTIA_DRUGS']

























