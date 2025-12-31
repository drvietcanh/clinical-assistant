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
            "adult_dm": "1.6-4.8mg/ngày, uống với thức ăn vào buổi sáng",
            "notes": "Ít dùng cho đái tháo đường. Chủ yếu dùng cho Parkinson và prolactinoma."
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
            "adult_dm": "3.75g/ngày (6 viên 625mg hoặc 3 viên 1.875g), chia 1-2 lần với bữa ăn",
            "adult_cholesterol": "3.75g/ngày",
            "notes": "Uống với thức ăn và nhiều nước. Hiệu quả giảm đường huyết nhẹ."
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

