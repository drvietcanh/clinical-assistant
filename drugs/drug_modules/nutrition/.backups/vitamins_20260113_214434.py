"""
Vitamins & Minerals (Dinh dưỡng & Khoáng chất)
"""

VITAMINS_DRUGS = {
    "Thiamine (Vitamin B1)":     {
        "group": "Nutrition - Vitamin B",
        "vietnamese_name": "Vitamin B1, Thiamine",
        "brand_names": {
            "common": [
                "Vitamin B1"
    ],
            "vietnam": [
                "Vitamin B1 250mg",
                "Vinpharlife B1"
    ],
        },
        "administration": [
            "PO",
            "IV",
            "IM"
    ],
        "indications": [
            "Bệnh Beriberi (tê phù)",
            "Hội chứng Wernicke-Korsakoff (người nghiện rượu)",
            "Dự phòng thiếu hụt B1 ở người nghiện rượu (trước khi truyền đường)"
    ],
        "dosage": {
            "wernicke_treatment": "500 mg IV mỗi 8 giờ x 2-3 ngày. (Pha loãng truyền chậm).",
            "prophylaxis_alcohol_withdrawal": "100 mg PO/IV/IM hàng ngày.",
            "notes": """Rất quan trọng: Phải tiêm B1 TRƯỚC khi truyền Glucose cho người nghiện rượu để tránh làm nặng thêm bệnh não Wernicke.""",
        },
        "side_effects": [
            "Phản ứng dị ứng (hiếm, chủ yếu tiêm nhanh)",
            "Đau tại chỗ tiêm"
    ],
        "storage": "Tránh ánh sáng.",
        "contraindications": [],
        "interactions": [],
        "pregnancy": "A - Không có nguy cơ trong các nghiên cứu có đối chứng""mechanism_of_action": "",
        "monitoring": [],
        "precautions": [],
        "pharmacokinetics": {
        },
        "black_box_warnings": None,
        "drug_interactions": {
            "major": [],
            "moderate": [],
            "minor": [],
        },
        "contraindications_detail": {
            "tuyệt_đối": [],
            "tương_đối": [],
        },
        "pregnancy_lactation": {
            "fda_category": "",
            "pregnancy_details": "",
            "lactation": {
                "safety": "",
                "details": "",
                "recommendation": "",
            },
        },
        "hepatic_adjustment": {
            "mild": "",
            "moderate": "",
            "severe": "",
            "notes": "",
        },
        "renal_adjustment": {
            "normal": "Không cần chỉnh liều.",
            "30_60": "Không cần chỉnh liều đáng kể; dùng thận trọng nếu suy thận trung bình.",
            "under_30": "Thận trọng; cân nhắc giảm liều nếu dùng kéo dài.",
            "dialysis": "Có thể dùng; không cần chỉnh liều đáng kể, theo dõi lâm sàng.",
            "notes": "Thiamine được thải trừ một phần qua thận nhưng an toàn ở đa số bệnh nhân; điều chỉnh chủ yếu dựa trên lâm sàng.",
        },
        "overdose_management": {
            "symptoms": [],
            "antidote": "",
            "treatment": [],
            "monitoring": "",
        },
        "reversal_agents": {
            "available": False,
            "agents": [],
            "notes": "Không có antidote đặc hiệu; xử trí quá liều chủ yếu là hỗ trợ và điều trị triệu chứng.",
        },
        "administration_instructions": {
            "oral": {
                "with_food": "Có thể uống cùng hoặc không cùng thức ăn; thường dùng trước khi truyền glucose ở bệnh nhân nghiện rượu.",
                "timing": "Dùng đúng liều, ưu tiên trước truyền glucose trong hội chứng Wernicke-Korsakoff.",
            },
        },
        "references": {
            "primary_sources": [],
            "last_updated": "",
            "evidence_level": "",
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
    "Pyridoxine (Vitamin B6)":     {
        "group": "Nutrition - Vitamin B",
        "vietnamese_name": "Vitamin B6, Pyridoxine",
        "brand_names": {
            "vietnam": [
                "Vitamin B6"
    ],
        },
        "administration": [
            "PO",
            "IV",
            "IM"
    ],
        "indications": [
            "Dự phòng bệnh thần kinh ngoại biên do Isoniazid (INH)",
            "Ngộ độc Isoniazid (liều cao)",
            "Nôn nghén (thai kỳ)"
    ],
        "dosage": {
            "inh_prophylaxis": "10-25 mg/ngày (tối đa 50mg).",
            "inh_poisoning": "Liều ngang bằng lượng INH đã uống (gram-for-gram). Nếu không rõ, dùng 5g IV.",
            "pregnancy_nausea": "10-25 mg mỗi 8 giờ.",
        },
        "side_effects": [
            "Bệnh thần kinh ngoại biên (nếu dùng liều >200mg/ngày kéo dài) - Paradoxical effect"
    ],
        "pregnancy": "A",
        "contraindications": [],
        "interactions": [],
        "mechanism_of_action": "",
        "monitoring": [],
        "precautions": [],
        "pharmacokinetics": {
        },
        "storage": "",
        "black_box_warnings": None,
        "drug_interactions": {
            "major": [],
            "moderate": [],
            "minor": [],
        },
        "contraindications_detail": {
            "tuyệt_đối": [],
            "tương_đối": [],
        },
        "pregnancy_lactation": {
            "fda_category": "",
            "pregnancy_details": "",
            "lactation": {
                "safety": "",
                "details": "",
                "recommendation": "",
            },
        },
        "hepatic_adjustment": {
            "mild": "",
            "moderate": "",
            "severe": "",
            "notes": "",
        },
        "renal_adjustment": {
            "normal": "Không cần chỉnh liều.",
            "30_60": "Không cần chỉnh liều đáng kể; dùng thận trọng nếu suy thận trung bình.",
            "under_30": "Thận trọng; cân nhắc giảm liều nếu dùng kéo dài.",
            "dialysis": "Có thể dùng; không cần chỉnh liều đáng kể, theo dõi lâm sàng.",
            "notes": "Pyridoxine thải trừ chủ yếu qua thận nhưng an toàn ở đa số bệnh nhân; điều chỉnh chủ yếu dựa trên lâm sàng.",
        },
        "overdose_management": {
            "symptoms": [],
            "antidote": "",
            "treatment": [],
            "monitoring": "",
        },
        "reversal_agents": {
            "available": False,
            "agents": [],
            "notes": "Không có antidote đặc hiệu; xử trí quá liều chủ yếu là hỗ trợ và điều trị triệu chứng.",
        },
        "administration_instructions": {
            "oral": {
                "with_food": "Có thể uống cùng hoặc không cùng thức ăn.",
                "timing": "Thường dùng 1–3 lần/ngày tùy chỉ định (dự phòng, điều trị, nôn nghén).",
            },
        },
        "references": {
            "primary_sources": [
                "FDA Drug Label - Pyridoxine (Vitamin B6)",
                "UpToDate - Pyridoxine: Drug information",
                "WHO Essential Medicines List"
            ],
            "last_updated": "2025-02-05",
            "evidence_level": "A"
        },
        "risk_flags": {
            "high_alert": False,
            "narrow_therapeutic_index": False,
            "bleeding_risk": False,
            "organ_toxicity": ["neurologic"],
            "qt_prolongation": False,
            "hepatotoxicity": False,
            "nephrotoxicity": False,
            "requires_monitoring": ["Neurologic symptoms (high doses)"]
        },
        "guideline_tags": [
            "FDA Drug Information",
            "UpToDate Drug Information",
            "WHO Essential Medicines List"
        ]
    },
    "Cyanocobalamin (Vitamin B12)":     {
        "group": "Nutrition - Vitamin B",
        "vietnamese_name": "Vitamin B12",
        "brand_names": {
            "vietnam": [
                "Vitamin B12 1000mcg"
    ],
        },
        "administration": [
            "IM",
            "SC",
            "PO",
            "Intranasal"
    ],
        "indications": [
            "Thiếu máu hồng cầu to (Pernicious anemia)",
            "Thiếu hụt B12 (người ăn chay trường, cắt dạ dày)",
            "Ngộ độc Cyanide (dạng Hydroxocobalamin)"
    ],
        "dosage": {
            "deficiency_treatment": "1000 mcg IM mỗi ngày x 1 tuần, sau đó 1 tuần/lần x 4 tuần, sau đó 1 tháng/lần.",
            "notes": "Oral absorption kém ở người thiếu yếu tố nội tại (Pernicious anemia) -> Bắt buộc tiêm.",
        },
        "side_effects": [],
        "contraindications": [],
        "interactions": [],
        "pregnancy": "A - Không có nguy cơ trong các nghiên cứu có đối chứng""mechanism_of_action": "",
        "monitoring": [],
        "precautions": [],
        "pharmacokinetics": {
        },
        "storage": "",
        "black_box_warnings": None,
        "drug_interactions": {
            "major": [],
            "moderate": [],
            "minor": [],
        },
        "contraindications_detail": {
            "tuyệt_đối": [],
            "tương_đối": [],
        },
        "pregnancy_lactation": {
            "fda_category": "",
            "pregnancy_details": "",
            "lactation": {
                "safety": "",
                "details": "",
                "recommendation": "",
            },
        },
        "hepatic_adjustment": {
            "mild": "",
            "moderate": "",
            "severe": "",
            "notes": "",
        },
        "renal_adjustment": {
            "normal": "Không cần chỉnh liều.",
            "30_60": "Không cần chỉnh liều đáng kể; dùng thận trọng nếu suy thận trung bình.",
            "under_30": "Thận trọng; cân nhắc giảm liều nếu dùng kéo dài.",
            "dialysis": "Có thể dùng; không cần chỉnh liều đáng kể, theo dõi lâm sàng.",
            "notes": "Vitamin B12 tương đối an toàn ở bệnh nhân suy thận; điều chỉnh chủ yếu dựa trên lâm sàng.",
        },
        "overdose_management": {
            "symptoms": [],
            "antidote": "",
            "treatment": [],
            "monitoring": "",
        },
        "reversal_agents": {
            "available": False,
            "agents": [],
            "notes": "Không có antidote đặc hiệu; xử trí quá liều chủ yếu là hỗ trợ và điều trị triệu chứng.",
        },
        "administration_instructions": {
            "oral": {
                "with_food": "Có thể uống cùng hoặc không cùng thức ăn.",
                "timing": "Dùng đều hàng ngày hoặc theo lịch tiêm/đường uống do bác sĩ chỉ định.",
            },
        },
        "references": {
            "primary_sources": [],
            "last_updated": "",
            "evidence_level": "",
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
    "Vitamin C (Ascorbic Acid)":     {
        "group": "Nutrition - Vitamin",
        "vietnamese_name": "Vitamin C, Ascorbic Acid",
        "brand_names": {
            "common": [
                "Laroscorbine"
    ],
            "vietnam": [
                "Vitamin C 500mg/1g",
                "Ceplin"
    ],
        },
        "administration": [
            "PO",
            "IV",
            "IM"
    ],
        "indications": [
            "Bệnh Scorbut (Scurvy)",
            "Hỗ trợ mau lành vết thương",
            "Methemoglobinemia (thay thế Methylene Blue nếu chống chỉ định dung nạp kém hơn)"
    ],
        "contraindications": [
            "Sỏi thận oxalate (liều cao)",
            "Thiếu G6PD (liều cao IV gây tan máu)"
    ],
        "dosage": {
            "scurvy": "100-250 mg x 1-2 lần/ngày.",
            "notes": "Liều cao acid hóa nước tiểu -> tăng nguy cơ sỏi oxalate.",
        },
        "side_effects": [],
        "interactions": [],
        "pregnancy": "",
        "mechanism_of_action": "",
        "monitoring": [],
        "precautions": [],
        "pharmacokinetics": {
        },
        "storage": "",
        "black_box_warnings": None,
        "drug_interactions": {
            "major": [],
            "moderate": [],
            "minor": [],
        },
        "contraindications_detail": {
            "tuyệt_đối": [
                "Sỏi thận oxalate đang hoạt động (liều cao).",
            ],
            "tương_đối": [
                "Tiền sử sỏi thận oxalate.",
                "Thiếu G6PD (nguy cơ tan máu với liều cao đường IV).",
            ],
        },
        "pregnancy_lactation": {
            "fda_category": "",
            "pregnancy_details": "",
            "lactation": {
                "safety": "",
                "details": "",
                "recommendation": "",
            },
        },
        "hepatic_adjustment": {
            "mild": "",
            "moderate": "",
            "severe": "",
            "notes": "",
        },
        "renal_adjustment": {
            "normal": "Không cần chỉnh liều ở bệnh nhân chức năng thận bình thường.",
            "30_60": "Dùng thận trọng với liều cao kéo dài; theo dõi nguy cơ sỏi thận.",
            "under_30": "Thận trọng, tránh liều rất cao kéo dài; cân nhắc giảm liều.",
            "dialysis": "Dùng thận trọng, theo dõi nguy cơ tích lũy và sỏi thận.",
            "notes": "Vitamin C liều cao có thể tăng nguy cơ sỏi oxalate, đặc biệt ở bệnh nhân suy thận.",
        },
        "overdose_management": {
            "symptoms": [],
            "antidote": "",
            "treatment": [],
            "monitoring": "",
        },
        "reversal_agents": {
            "available": False,
            "agents": [],
            "notes": "Không có antidote đặc hiệu; xử trí quá liều chủ yếu là hỗ trợ, ngừng thuốc, bù dịch và theo dõi sỏi thận/tan máu.",
        },
        "administration_instructions": {
            "oral": {
                "with_food": "Có thể uống cùng thức ăn để giảm kích ứng dạ dày khi dùng liều cao.",
                "timing": "Chia liều trong ngày nếu dùng liều cao; tránh dùng liều rất cao kéo dài nếu có tiền sử sỏi thận.",
            },
        },
        "references": {
            "primary_sources": [],
            "last_updated": "",
            "evidence_level": "",
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
    "Vitamin D3 (Cholecalciferol)":     {
        "group": "Nutrition - Vitamin",
        "vietnamese_name": "Vitamin D3",
        "brand_names": {
            "vietnam": [
                "Aquadetrim",
                "D3 B.O.N"
    ],
        },
        "administration": [
            "PO",
            "IM"
    ],
        "indications": [
            "Loãng xương (Osteoporosis) - phối hợp Calci",
            "Còi xương (Rickets)",
            "Thiếu Vitamin D"
    ],
        "dosage": {
            "osteoporosis": "800-1000 IU/ngày (kèm Calci 1000-1200mg).",
            "deficiency_treatment": "50,000 IU mỗi tuần x 8 tuần (liều tải), sau đó duy trì.",
            "notes": """Cần chức năng thận để chuyển hóa thành dạng hoạt động (Calcitriol). Nếu suy thận nặng -> dùng Calcitriol.""",
        },
        "monitoring": [
            "Nồng độ 25(OH)D máu",
            "Calci máu"
        ],
        "side_effects": [],
        "contraindications": [],
        "interactions": [],
        "pregnancy": "",
        "mechanism_of_action": "",
        "precautions": [],
        "pharmacokinetics": {
        },
        "storage": "",
        "black_box_warnings": None,
        "drug_interactions": {
            "major": [],
            "moderate": [],
            "minor": [],
        },
        "contraindications_detail": {
            "tuyệt_đối": [],
            "tương_đối": [],
        },
        "pregnancy_lactation": {
            "fda_category": "",
            "pregnancy_details": "",
            "lactation": {
                "safety": "",
                "details": "",
                "recommendation": "",
            },
        },
        "hepatic_adjustment": {
            "mild": "",
            "moderate": "",
            "severe": "",
            "notes": "",
        },
        "renal_adjustment": {
            "normal": "Không cần chỉnh liều ở bệnh nhân chức năng thận bình thường.",
            "30_60": "Thận trọng khi dùng liều tải cao kéo dài; theo dõi calci và chức năng thận.",
            "under_30": "Thận trọng; cân nhắc giảm liều và theo dõi calci, đặc biệt nếu phối hợp calcium.",
            "dialysis": "Thận trọng; ưu tiên dạng hoạt chất (calcitriol) nếu suy thận nặng.",
            "notes": "Vitamin D3 cần chức năng thận để chuyển hóa thành dạng hoạt động; suy thận nặng có thể cần dùng calcitriol thay thế.",
        },
        "overdose_management": {
            "symptoms": [],
            "antidote": "",
            "treatment": [],
            "monitoring": "",
        },
        "reversal_agents": {
            "available": False,
            "agents": [],
            "notes": "Không có antidote đặc hiệu; xử trí quá liều chủ yếu là ngừng thuốc, điều trị tăng calci máu và hỗ trợ.",
        },
        "administration_instructions": {
            "oral": {
                "with_food": "Thường dùng cùng thức ăn hoặc theo lịch hàng ngày/tuần theo chỉ định.",
                "timing": "Tuân thủ liều nạp và liều duy trì; không tự ý tăng liều để tránh tăng calci máu.",
            },
        },
        "references": {
            "primary_sources": [
                "FDA Drug Label - Vitamin D3 (Cholecalciferol)",
                "UpToDate - Vitamin D: Drug information",
                "Endocrine Society Guidelines - Vitamin D Deficiency"
            ],
            "last_updated": "2025-02-05",
            "evidence_level": "A"
        },
        "risk_flags": {
            "high_alert": False,
            "narrow_therapeutic_index": False,
            "bleeding_risk": False,
            "organ_toxicity": ["renal"],
            "qt_prolongation": False,
            "hepatotoxicity": False,
            "nephrotoxicity": False,
            "requires_monitoring": ["Serum 25(OH)D", "Serum calcium", "Renal function"]
        },
        "guideline_tags": [
            "FDA Drug Information",
            "UpToDate Drug Information",
            "Endocrine Society Guidelines - Vitamin D Deficiency"
        ]
    },
}
