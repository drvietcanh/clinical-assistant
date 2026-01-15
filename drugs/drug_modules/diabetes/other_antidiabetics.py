"""Other Antidiabetic Medications
Bromocriptine, Colesevelam - less commonly used antidiabetic drugs"""

OTHER_ANTIDIABETICS_DRUGS = {
    "Bromocriptine": {
        "group": "Diabetes - Dopamine Agonist",
        "vietnamese_name": "Bromocriptine, Cycloset",
        "administration": ["PO"],
        "indications": [
            "Đái tháo đường type 2 (ít dùng)",
            "Bệnh Parkinson",
            "Prolactinoma"
        ],
        "contraindications": [
            "Dị ứng bromocriptine",
            "Bệnh tim mạch không ổn định",
            "Tăng huyết áp không kiểm soát",
            "Bệnh mạch máu ngoại vi",
            "Có thai"
        ],
        "dosage": {
            "adult_start": "1.6mg PO x 1 lần/ngày với thức ăn vào buổi sáng",
            "adult_usual": "1.6-4.8mg PO x 1 lần/ngày với thức ăn vào buổi sáng",
            "adult_max": "4.8mg/ngày",
            "dm_t2": "Khởi đầu 1.6mg PO x 1 lần/ngày với thức ăn vào buổi sáng. Tăng dần mỗi tuần 1.6mg đến 4.8mg/ngày nếu cần và dung nạp tốt. Ít dùng cho đái tháo đường do hiệu quả hạn chế và tác dụng phụ.",
            "elderly": "Khởi đầu liều thấp hơn (0.8-1.6mg PO x 1 lần/ngày), tăng dần chậm. Người cao tuổi nhạy cảm hơn với hạ huyết áp tư thế và ngất.",
            "pediatric_dosing": {
                "neonates": "Không khuyến cáo cho trẻ em (dữ liệu hạn chế).",
                "infants": "Không khuyến cáo cho trẻ em (dữ liệu hạn chế).",
                "children": "Không khuyến cáo cho trẻ em (dữ liệu hạn chế).",
                "adolescents": "Không khuyến cáo cho trẻ em (dữ liệu hạn chế).",
                "notes": "Không có chỉ định cho đái tháo đường ở trẻ em. Dữ liệu về an toàn và hiệu quả ở trẻ em còn hạn chế."
            },
            "geriatric_dosing": {
                "considerations": "Người cao tuổi có nguy cơ cao hạ huyết áp tư thế, ngất, và chóng mặt. Bệnh tim mạch phổ biến hơn.",
                "dose_adjustment": "Khởi đầu liều thấp hơn (0.8-1.6mg PO x 1 lần/ngày). Tăng dần chậm hơn. Theo dõi chặt chẽ huyết áp và dấu hiệu ngất.",
                "monitoring": "Theo dõi huyết áp (đặc biệt hạ huyết áp tư thế), dấu hiệu ngất, và chóng mặt. Giáo dục bệnh nhân về cách đứng dậy từ từ."
            },
            "renal_adjustment_dosage": {
                "normal": "1.6-4.8mg PO x 1 lần/ngày với thức ăn vào buổi sáng (CrCl ≥60)",
                "30_60": "Không cần điều chỉnh liều. Thận trọng.",
                "under_30": "Thận trọng. Không cần điều chỉnh liều khởi đầu, nhưng theo dõi sát tác dụng phụ.",
                "dialysis": "Thận trọng. Không cần điều chỉnh liều.",
                "notes": "Bromocriptine thải trừ chủ yếu qua gan, không cần điều chỉnh liều ở suy thận. Tuy nhiên, thận trọng ở bệnh nhân suy thận nặng do các bệnh lý đi kèm."
            },
            "hepatic_adjustment_dosage": {
                "mild": "Không cần điều chỉnh liều. Theo dõi chức năng gan.",
                "moderate": "Thận trọng, có thể cần giảm liều. Theo dõi chức năng gan và tác dụng phụ.",
                "severe": "Thận trọng, có thể cần giảm liều đáng kể. Theo dõi chức năng gan và tác dụng phụ chặt chẽ.",
                "notes": "Bromocriptine chuyển hóa qua gan (CYP3A4). Suy gan có thể làm giảm chuyển hóa, tăng nồng độ bromocriptine, tăng tác dụng phụ. Cần giảm liều và theo dõi chặt chẽ."
            },
            "administration_route": "PO (uống)",
            "frequency": "1 lần/ngày",
            "with_food": "PHẢI uống với thức ăn vào buổi sáng để giảm buồn nôn và tác dụng phụ tiêu hóa.",
            "timing": "Uống 1 lần/ngày với thức ăn vào buổi sáng. Uống cùng giờ mỗi ngày. Bắt đầu với liều thấp và tăng dần.",
            "notes": "Ít dùng cho đái tháo đường. Chủ yếu dùng cho Parkinson và prolactinoma. Hiệu quả giảm đường huyết hạn chế. Nguy cơ hạ huyết áp tư thế, ngất. Uống với thức ăn vào buổi sáng. Bắt đầu với liều thấp (1.6mg) và tăng dần."
        },
        "side_effects": [
            "Buồn nôn, nôn",
            "Chóng mặt",
            "Ngất",
            "Hạ huyết áp tư thế",
            "Đau đầu",
            "Mệt mỏi"
        ],
        "interactions": [
            "Thuốc hạ huyết áp: tăng nguy cơ hạ huyết áp",
            "Erythromycin: tăng nồng độ bromocriptine",
            "Thuốc chống nôn: giảm hiệu quả bromocriptine"
        ],
        "pregnancy": "B",
        "mechanism_of_action": "Bromocriptine là chất chủ vận thụ thể dopamine D2. Cơ chế giảm đường huyết chưa rõ hoàn toàn, có thể liên quan đến điều chỉnh nhịp sinh học và giảm đề kháng insulin. Bromocriptine được FDA phê duyệt cho đái tháo đường type 2 nhưng ít được sử dụng do tác dụng phụ và hiệu quả hạn chế. Chủ yếu được sử dụng cho bệnh Parkinson và prolactinoma.",
        "monitoring": [
            "Đường huyết (HbA1c, glucose máu)",
            "Huyết áp (đặc biệt hạ huyết áp tư thế)",
            "Dấu hiệu buồn nôn, nôn",
            "Dấu hiệu ngất"
        ],
        "precautions": [
            "Ít dùng cho đái tháo đường - hiệu quả hạn chế",
            "Uống với thức ăn vào buổi sáng để giảm buồn nôn",
            "Nguy cơ hạ huyết áp tư thế - đứng dậy từ từ",
            "Nguy cơ ngất - thận trọng khi lái xe",
            "Không dùng trong thai kỳ"
        ],
        "pharmacokinetics": {
            "half_life": "~15 giờ",
            "onset": "Vài giờ",
            "duration": "12-24 giờ",
            "protein_binding": "90-96%",
            "clearance": "Gan (chuyển hóa qua CYP3A4)"
        },
        "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm",
        "black_box_warnings": None,
        "risk_flags": {
            "high_alert": False,
            "narrow_therapeutic_index": False,
            "organ_toxicity": {"cardiovascular": True},
            "icu_critical_care_only": False,
            "look_alike_sound_alike": []
        },
        "guideline_tags": [
            "ADA Guidelines (American Diabetes Association)"
        ],
        "references": {
            "primary_sources": [
                "FDA Drug Label - Cycloset (bromocriptine)",
                "ADA Guidelines"
            ],
            "last_updated": "2025-02-18",
            "evidence_level": "Moderate - FDA approved nhưng ít được sử dụng"
        },
        "black_box_warnings": None,
        "drug_interactions": {
            "major": [],
            "moderate": [
                {
                    "drug": "Erythromycin, clarithromycin",
                    "mechanism": "Ức chế CYP3A4, tăng chuyển hóa bromocriptine",
                    "effect": "Tăng nồng độ bromocriptine, tăng tác dụng phụ",
                    "management": "Thận trọng. Theo dõi tác dụng phụ."
                },
                {
                    "drug": "Thuốc hạ huyết áp",
                    "mechanism": "Tác dụng cộng dồn",
                    "effect": "Tăng nguy cơ hạ huyết áp",
                    "management": "Thận trọng. Theo dõi huyết áp."
                }
            ],
            "minor": []
        },
        "contraindications": {
            "tuyệt_đối": [
                "Dị ứng bromocriptine",
                "Bệnh tim mạch không ổn định",
                "Tăng huyết áp không kiểm soát",
                "Có thai"
            ],
            "tương_đối": [
                "Bệnh mạch máu ngoại vi - thận trọng",
                "Suy gan - thận trọng (chuyển hóa qua gan)"
            ]
        },
        "pregnancy_lactation": {
            "fda_category": "B",
            "pregnancy_details": "Category B - an toàn hơn category C. Tuy nhiên, bromocriptine ức chế prolactin và có thể ảnh hưởng đến thai kỳ. Không khuyến cáo dùng trong thai kỳ trừ khi lợi ích vượt quá nguy cơ.",
            "lactation": {
                "safety": "Compatible with monitoring",
                "details": "Bromocriptine ức chế prolactin, có thể giảm tiết sữa. Bài tiết vào sữa mẹ ở nồng độ thấp.",
                "recommendation": "Có thể dùng khi cho con bú với theo dõi. Thận trọng vì có thể giảm tiết sữa."
            }
        },
        "hepatic_adjustment": {
            "mild": "Không đổi",
            "moderate": "Thận trọng",
            "severe": "Thận trọng, có thể giảm liều",
            "notes": "Bromocriptine chuyển hóa qua gan (CYP3A4). Suy gan có thể làm giảm chuyển hóa và tăng nồng độ bromocriptine."
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "Không đổi",
            "under_30": "Thận trọng",
            "notes": "Bromocriptine thải trừ chủ yếu qua gan, không cần điều chỉnh liều ở suy thận nhẹ đến trung bình."
        },
        "overdose_management": {
            "symptoms": [
                "Buồn nôn, nôn nặng",
                "Chóng mặt, ngất",
                "Hạ huyết áp nặng",
                "Đau đầu nặng",
                "Ảo giác, lú lẫn"
            ],
            "antidote": "Không có antidote đặc hiệu",
            "treatment": [
                "Ngừng ngay bromocriptine",
                "Rửa dạ dày nếu uống trong vòng 1-2 giờ",
                "Than hoạt tính",
                "Điều trị hạ huyết áp: truyền dịch, vasopressors nếu cần",
                "Điều trị triệu chứng: chống nôn nếu cần",
                "Theo dõi huyết áp, dấu hiệu sinh tồn"
            ],
            "monitoring": "Huyết áp, dấu hiệu sinh tồn, triệu chứng thần kinh"
        },
        "reversal_agents": {
            "available": False,
            "agents": []
        },
        "administration_instructions": {
            "oral": {
                "with_food": "Uống với thức ăn vào buổi sáng để giảm buồn nôn",
                "timing": "Uống buổi sáng với thức ăn",
                "notes": "QUAN TRỌNG: Uống với thức ăn để giảm buồn nôn. Bắt đầu với liều thấp và tăng dần."
            }
        },
        "black_box_warnings": None,
},

    "Colesevelam": {
        "group": "Diabetes - Bile Acid Sequestrant",
        "vietnamese_name": "Colesevelam, Welchol",
        "administration": ["PO"],
        "indications": [
            "Đái tháo đường type 2 (chỉ định phụ)",
            "Tăng cholesterol máu (chỉ định chính)"
        ],
        "contraindications": [
            "Dị ứng colesevelam",
            "Tắc ruột",
            "Tăng triglyceride máu nặng (>500 mg/dL)",
            "Bệnh viêm ruột"
        ],
        "dosage": {
            "adult_start": "3.75g PO/ngày (6 viên 625mg hoặc 3 viên 1.875g), chia 1-2 lần với bữa ăn",
            "adult_usual": "3.75g PO/ngày, chia 1-2 lần với bữa ăn",
            "adult_max": "3.75g/ngày",
            "dm_t2": "3.75g PO/ngày (6 viên 625mg hoặc 3 viên 1.875g), chia 1-2 lần với bữa ăn. Hiệu quả giảm đường huyết nhẹ (giảm HbA1c ~0.5%). Chỉ định phụ cho đái tháo đường type 2.",
            "cholesterol": "3.75g PO/ngày, chia 1-2 lần với bữa ăn (chỉ định chính cho tăng cholesterol máu).",
            "elderly": "Không cần điều chỉnh liều đặc biệt. Người cao tuổi có thể nhạy cảm hơn với táo bón.",
            "pediatric_dosing": {
                "neonates": "Không khuyến cáo cho trẻ em (dữ liệu hạn chế).",
                "infants": "Không khuyến cáo cho trẻ em (dữ liệu hạn chế).",
                "children": "Không khuyến cáo cho trẻ em (dữ liệu hạn chế).",
                "adolescents": "Không khuyến cáo cho trẻ em (dữ liệu hạn chế).",
                "notes": "Không có chỉ định cho đái tháo đường ở trẻ em. Dữ liệu về an toàn và hiệu quả ở trẻ em còn hạn chế."
            },
            "geriatric_dosing": {
                "considerations": "Người cao tuổi có nguy cơ cao táo bón. Chức năng tiêu hóa có thể giảm.",
                "dose_adjustment": "Không cần điều chỉnh liều. Tăng chất xơ và uống nhiều nước để giảm táo bón.",
                "monitoring": "Theo dõi dấu hiệu táo bón, đầy hơi, và khó nuốt. Theo dõi lipid (triglyceride) định kỳ."
            },
            "renal_adjustment_dosage": {
                "normal": "3.75g PO/ngày, chia 1-2 lần với bữa ăn (CrCl ≥60)",
                "30_60": "Không cần điều chỉnh liều. Colesevelam không hấp thu vào máu.",
                "under_30": "Không cần điều chỉnh liều. Colesevelam không hấp thu vào máu.",
                "dialysis": "Không cần điều chỉnh liều. Colesevelam không hấp thu vào máu.",
                "notes": "Colesevelam không hấp thu vào máu, không thải trừ qua thận. Không cần điều chỉnh liều ở suy thận."
            },
            "hepatic_adjustment_dosage": {
                "mild": "Không cần điều chỉnh liều. Colesevelam không hấp thu vào máu.",
                "moderate": "Không cần điều chỉnh liều. Colesevelam không hấp thu vào máu.",
                "severe": "Không cần điều chỉnh liều. Colesevelam không hấp thu vào máu.",
                "notes": "Colesevelam không hấp thu vào máu, không chuyển hóa qua gan. Không cần điều chỉnh liều ở suy gan."
            },
            "administration_route": "PO (uống)",
            "frequency": "1-2 lần/ngày",
            "with_food": "PHẢI uống với thức ăn và nhiều nước để giảm tác dụng phụ tiêu hóa và tăng hiệu quả.",
            "timing": "Uống 1-2 lần/ngày với bữa ăn. Có thể uống 3.75g x 1 lần/ngày hoặc chia 1.875g x 2 lần/ngày. QUAN TRỌNG: Dùng cách xa các thuốc khác ít nhất 4 giờ để tránh giảm hấp thu.",
            "notes": "Uống với thức ăn và nhiều nước. Hiệu quả giảm đường huyết nhẹ (giảm HbA1c ~0.5%). Chỉ định phụ cho đái tháo đường type 2. QUAN TRỌNG: Dùng cách xa các thuốc khác (warfarin, digoxin, levothyroxine, metformin, sulfonylurea) ít nhất 4 giờ để tránh giảm hấp thu. Nguy cơ táo bón - tăng chất xơ, uống nhiều nước. Nguy cơ tăng triglyceride - theo dõi lipid."
        },
        "side_effects": [
            "Táo bón",
            "Đầy hơi, chướng bụng",
            "Buồn nôn",
            "Khó nuốt",
            "Tăng triglyceride máu"
        ],
        "interactions": [
            "Có thể giảm hấp thu nhiều thuốc: warfarin, digoxin, levothyroxine, metformin, sulfonylurea",
            "Dùng cách xa các thuốc khác ít nhất 4 giờ"
        ],
        "pregnancy": "B",
        "mechanism_of_action": "Colesevelam là chất gắn acid mật (bile acid sequestrant), gắn với acid mật trong ruột → giảm tái hấp thu acid mật → gan tăng tổng hợp acid mật từ cholesterol → giảm cholesterol máu. Cơ chế giảm đường huyết chưa rõ hoàn toàn, có thể liên quan đến tác dụng trên thụ thể FXR (farnesoid X receptor) và TGR5 (Takeda G protein-coupled receptor 5) → cải thiện độ nhạy insulin và giảm sản xuất glucose ở gan. Hiệu quả giảm đường huyết nhẹ (giảm HbA1c ~0.5%).",
        "monitoring": [
            "Đường huyết (HbA1c, glucose máu)",
            "Lipid (cholesterol, triglyceride)",
            "Dấu hiệu táo bón, đầy hơi",
            "Theo dõi tương tác với các thuốc khác"
        ],
        "precautions": [
            "Hiệu quả giảm đường huyết nhẹ (~0.5% HbA1c)",
            "Uống với thức ăn và nhiều nước",
            "Dùng cách xa các thuốc khác ít nhất 4 giờ để tránh giảm hấp thu",
            "Nguy cơ táo bón - tăng chất xơ, uống nhiều nước",
            "Nguy cơ tăng triglyceride - theo dõi lipid",
            "Không dùng nếu tắc ruột hoặc bệnh viêm ruột"
        ],
        "pharmacokinetics": {
            "half_life": "N/A (không hấp thu vào máu)",
            "onset": "Vài tuần",
            "duration": "24 giờ",
            "protein_binding": "N/A",
            "clearance": "Không hấp thu, thải qua phân"
        },
        "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm",
        "black_box_warnings": None,
        "risk_flags": {
            "high_alert": False,
            "narrow_therapeutic_index": False,
            "organ_toxicity": {},
            "icu_critical_care_only": False,
            "look_alike_sound_alike": []
        },
        "guideline_tags": [
            "ADA Guidelines (American Diabetes Association)",
            "AHA/ACC Guidelines (American Heart Association/American College of Cardiology)"
        ],
        "references": {
            "primary_sources": [
                "FDA Drug Label - Welchol (colesevelam)",
                "ADA Guidelines"
            ],
            "last_updated": "2025-02-18",
            "evidence_level": "Moderate - FDA approved nhưng hiệu quả giảm đường huyết nhẹ"
        },
        "black_box_warnings": None,
        "drug_interactions": {
            "major": [],
            "moderate": [
                {
                    "drug": "Warfarin, digoxin, levothyroxine, metformin, sulfonylurea",
                    "mechanism": "Giảm hấp thu thuốc do gắn trong ruột",
                    "effect": "Giảm nồng độ và hiệu quả của các thuốc khác",
                    "management": "Dùng cách xa các thuốc khác ít nhất 4 giờ."
                }
            ],
            "minor": []
        },
        "contraindications": {
            "tuyệt_đối": [
                "Dị ứng colesevelam",
                "Tắc ruột",
                "Tăng triglyceride máu nặng (>500 mg/dL)",
                "Bệnh viêm ruột"
            ],
            "tương_đối": [
                "Tăng triglyceride máu nhẹ đến trung bình - theo dõi",
                "Táo bón - thận trọng, tăng chất xơ, uống nhiều nước"
            ]
        },
        "pregnancy_lactation": {
            "fda_category": "B",
            "pregnancy_details": "Category B - an toàn hơn category C. Colesevelam không hấp thu vào máu, nên ít ảnh hưởng đến thai nhi.",
            "lactation": {
                "safety": "Compatible",
                "details": "Colesevelam không hấp thu vào máu, không bài tiết vào sữa mẹ.",
                "recommendation": "Có thể dùng an toàn khi cho con bú."
            }
        },
        "hepatic_adjustment": {
            "mild": "Không đổi",
            "moderate": "Không đổi",
            "severe": "Không đổi",
            "notes": "Colesevelam không hấp thu vào máu, không chuyển hóa qua gan. Không cần điều chỉnh liều ở suy gan."
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "Không đổi",
            "under_30": "Không đổi",
            "notes": "Colesevelam không hấp thu vào máu, không thải trừ qua thận. Không cần điều chỉnh liều ở suy thận."
        },
        "overdose_management": {
            "symptoms": [
                "Táo bón nặng",
                "Đầy hơi, chướng bụng",
                "Khó nuốt"
            ],
            "antidote": "Không có antidote đặc hiệu",
            "treatment": [
                "Ngừng ngay colesevelam",
                "Điều trị táo bón: tăng chất xơ, uống nhiều nước, thuốc nhuận tràng nếu cần",
                "Điều trị hỗ trợ và điều trị triệu chứng"
            ],
            "monitoring": "Theo dõi triệu chứng tiêu hóa"
        },
        "reversal_agents": {
            "available": False,
            "agents": []
        },
        "administration_instructions": {
            "oral": {
                "with_food": "Uống với thức ăn và nhiều nước",
                "timing": "Chia 1-2 lần với bữa ăn",
                "notes": "QUAN TRỌNG: 1) Uống với thức ăn và nhiều nước, 2) Dùng cách xa các thuốc khác ít nhất 4 giờ để tránh giảm hấp thu."
            }
        },
        "black_box_warnings": None,
},
}

__all__ = ['OTHER_ANTIDIABETICS_DRUGS']

