"""
SGLT2 Inhibitors (Thuốc ức chế SGLT2)
Nhóm thuốc mới nhất cho đái tháo đường type 2, có lợi ích tim mạch và thận đã được chứng minh.
"""

SGLT2_INHIBITORS_DRUGS = {
    "Empagliflozin":     {
        "group": "Diabetes - SGLT2 Inhibitor",
        "vietnamese_name": "Empagliflozin, Jardiance",
        "brand_names": {
            "common": [
                "Jardiance"
    ],
            "vietnam": [
                "Jardiance 10/25mg"
    ],
        },
        "administration": [
            "PO"
    ],
        "indications": [
            "Đái tháo đường type 2",
            "Suy tim (HFrEF và HFpEF) - Chỉ định mới, không cần có đái tháo đường",
            "Bệnh thận mạn (CKD) - Chỉ định mới"
    ],
        "contraindications": [
            "Đái tháo đường type 1",
            "Nhiễm toan ceton đái tháo đường (DKA)",
            "Suy thận nặng (eGFR <20)",
            "Lọc máu"
    ],
        "dosage": {
            "dm_t2": "Khởi đầu 10mg x 1 lần/sáng. Có thể tăng lên 25mg nếu cần.",
            "heart_failure": "10mg x 1 lần/ngày (không phụ thuộc đái tháo đường).",
            "notes": """Uống buổi sáng, có thể uống đói hoặc no. Tác dụng giảm đường huyết nhẹ (HbA1c ~0.5-0.8%) nhưng lợi ích tim mạch và thận rất lớn.""",
        },
        "side_effects": [
            "Nhiễm nấm âm đạo (Phụ nữ - rất phổ biến ~10%)",
            "Nhiễm trùng đường tiết niệu",
            "Đa niệu (Tiểu nhiều)",
            "Hạ huyết áp tư thế (đặc biệt khi dùng với lợi tiểu)",
            "Nhiễm toan ceton đái tháo đường (DKA) - Hiếm nhưng nguy hiểm, có thể xảy ra ngay cả khi đường huyết bình thường (euglycemic DKA)"
    ],
        "interactions": [
            "Lợi tiểu: Tăng nguy cơ mất nước, hạ huyết áp.",
            "Insulin, Sulfonylurea: Tăng nguy cơ hạ đường huyết (cần giảm liều insulin/SU)."
    ],
        "mechanism_of_action": """Ức chế SGLT2 (Sodium-Glucose Cotransporter 2) ở ống lượn gần thận, ngăn tái hấp thu glucose → Glucose thải qua nước tiểu (glucosuria) → Giảm đường huyết. Lợi ích tim mạch: Giảm tử vong tim mạch, nhập viện do suy tim (EMPA-REG OUTCOME trial). Lợi ích thận: Làm chậm tiến triển bệnh thận mạn.""",
        "monitoring": [
            "Đường huyết (HbA1c, glucose máu)",
            "Chức năng thận (eGFR, creatinine) - Trước khi bắt đầu và định kỳ",
            "Huyết áp (nguy cơ hạ huyết áp)",
            "Dấu hiệu nhiễm trùng tiết niệu, nhiễm nấm âm đạo",
            "Dấu hiệu DKA (đau bụng, buồn nôn, khó thở) - Đặc biệt khi bệnh nhân ốm, nhịn ăn, phẫu thuật"
    ],
        "precautions": [
            "Nguy cơ DKA (Diabetic Ketoacidosis) - Ngừng thuốc khi bệnh nhân ốm nặng, nhịn ăn, phẫu thuật",
            "Nguy cơ nhiễm nấm âm đạo cao ở phụ nữ - Giáo dục vệ sinh",
            "Nguy cơ hạ huyết áp - Thận trọng ở người cao tuổi, dùng lợi tiểu",
            "Không dùng cho đái tháo đường type 1 (tăng nguy cơ DKA)",
            "Giảm liều insulin/sulfonylurea khi bắt đầu dùng để tránh hạ đường huyết",
            "Lợi ích tim mạch và thận lớn hơn tác dụng giảm đường huyết"
    ],
        "black_box_warnings": None,
        "contraindications_detail": {
            "tuyệt_đối": [
                "Đái tháo đường type 1",
                "Nhiễm toan ceton do đái tháo đường",
                "Suy thận nặng (eGFR <20)",
                "Đang lọc máu",
                "Dị ứng empagliflozin"
    ],
            "tương_đối": [
                "Nhiễm trùng đường tiết niệu tái phát - tăng nguy cơ nhiễm trùng",
                "Suy tim nặng - tăng nguy cơ mất nước",
                "Người cao tuổi - tăng nguy cơ mất nước, hạ huyết áp",
                "Dùng diuretics - tăng nguy cơ mất nước",
                "Nhiễm trùng đường sinh dục tái phát - tăng nguy cơ nhiễm trùng"
    ],
        },
        "pregnancy": "C - Nguy cơ không thể loại trừ. Không khuyến nghị trong thai kỳ",
        "pharmacokinetics": {
        },
        "storage": "",
        "drug_interactions": {
            "major": [
                {
                    "drug": "Diuretics (Furosemide, Hydrochlorothiazide, etc.)",
                    "mechanism": "Cả hai đều tăng thải nước và natri",
                    "effect": "Tăng nguy cơ mất nước, hạ huyết áp, suy thận cấp",
                    "management": "Theo dõi huyết áp và thể tích dịch. Có thể cần giảm liều diuretic hoặc tạm ngừng SGLT2i."
                }
            ],
            "moderate": [
                {
                    "drug": "Insulin, Sulfonylureas",
                    "mechanism": "SGLT2i tăng thải glucose qua nước tiểu, có thể tăng nguy cơ hạ đường huyết",
                    "effect": "Tăng nguy cơ hạ đường huyết",
                    "management": "Giảm liều insulin hoặc sulfonylurea khi bắt đầu SGLT2i. Theo dõi đường huyết chặt chẽ."
                },
                {
                    "drug": "ACE inhibitors, ARBs",
                    "mechanism": "Cả hai đều có thể ảnh hưởng đến chức năng thận",
                    "effect": "Tăng nguy cơ suy thận cấp (hiếm)",
                    "management": "Theo dõi eGFR và creatinine khi bắt đầu hoặc thay đổi liều."
                }
            ],
            "minor": [
                {
                    "drug": "Digoxin",
                    "mechanism": "SGLT2i có thể ảnh hưởng nhẹ đến nồng độ digoxin",
                    "effect": "Tăng nhẹ nồng độ digoxin",
                    "management": "Theo dõi nồng độ digoxin nếu dùng cùng."
                }
            ]
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
            "normal": "Không cần chỉnh liều",
            "30_60": "Có thể dùng nhưng cần điều chỉnh liều. Không dùng nếu eGFR <30.",
            "under_30": "CHỐNG CHỈ ĐỊNH nếu eGFR <20.",
            "dialysis": "CHỐNG CHỈ ĐỊNH. Không dùng khi đang lọc máu.",
            "notes": "Empagliflozin chống chỉ định ở suy thận nặng (eGFR <20). Cần kiểm tra eGFR trước khi bắt đầu và định kỳ. Ngừng thuốc nếu eGFR giảm xuống dưới 20."
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
            "notes": "Không có antidote đặc hiệu. Điều trị quá liều chủ yếu là hỗ trợ: ngừng thuốc, bù dịch nếu mất nước, điều chỉnh đường huyết nếu hạ đường huyết, điều trị DKA nếu có."
        },
        "administration_instructions": {
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
                "organ_toxicity": ["genitourinary"],
                "qt_prolongation": False,
                "hepatotoxicity": False,
                "nephrotoxicity": False,
                "requires_monitoring": ["eGFR", "Genital/urinary infections"],
            },
            "guideline_tags": [
                "ADA 2024 Standards of Care - Diabetes",
                "AACE/ACE 2023 Type 2 Diabetes Guidelines",
                "FDA Black Box Warning - Fournier's Gangrene (rare)",
            ]
    },
    "Dapagliflozin":     {
        "group": "Diabetes - SGLT2 Inhibitor",
        "vietnamese_name": "Dapagliflozin, Forxiga",
        "brand_names": {
            "common": [
                "Forxiga",
                "Farxiga"
    ],
            "vietnam": [
                "Forxiga 5/10mg"
    ],
        },
        "administration": [
            "PO"
    ],
        "indications": [
            "Đái tháo đường type 2",
            "Suy tim (HFrEF, HFmrEF, HFpEF) - Chỉ định mới",
            "Bệnh thận mạn (CKD) - Chỉ định mới"
    ],
        "dosage": {
            "dm_t2": "Khởi đầu 5mg x 1 lần/sáng. Có thể tăng lên 10mg nếu cần.",
            "heart_failure": "10mg x 1 lần/ngày.",
            "ckd": "10mg x 1 lần/ngày.",
            "notes": "Uống buổi sáng. Tương tự Empagliflozin về cơ chế và tác dụng phụ.",
        },
        "side_effects": [
            "Nhiễm nấm âm đạo (Phụ nữ)",
            "Nhiễm trùng đường tiết niệu",
            "Đa niệu",
            "Hạ huyết áp",
            "DKA (Hiếm)"
    ],
        "mechanism_of_action": """Ức chế SGLT2 ở thận, tương tự Empagliflozin. Lợi ích tim mạch và thận đã được chứng minh (DAPA-HF, DAPA-CKD trials).""",
        "monitoring": [
            "Đường huyết, eGFR, huyết áp",
            "Dấu hiệu nhiễm trùng, DKA"
    ],
        "black_box_warnings": None,
        "contraindications_detail": {
            "tuyệt_đối": [
                "Đái tháo đường type 1",
                "Nhiễm toan ceton do đái tháo đường",
                "Suy thận nặng (eGFR <25)",
                "Đang lọc máu",
                "Dị ứng dapagliflozin"
    ],
            "tương_đối": [
                "Nhiễm trùng đường tiết niệu tái phát - tăng nguy cơ nhiễm trùng",
                "Suy tim nặng - tăng nguy cơ mất nước",
                "Người cao tuổi - tăng nguy cơ mất nước, hạ huyết áp",
                "Dùng diuretics - tăng nguy cơ mất nước",
                "Nhiễm trùng đường sinh dục tái phát - tăng nguy cơ nhiễm trùng"
    ],
        },
        "contraindications": [],
        "interactions": [],
        ',
        "pregnancy": "C - Nguy cơ không thể loại trừ. Không khuyến nghị trong thai kỳ",
        ',
        "precautions": [],
        "pharmacokinetics": {
        },
        "storage": "",
        "drug_interactions": {
            "major": [
                {
                    "drug": "Diuretics (Furosemide, Hydrochlorothiazide, etc.)",
                    "mechanism": "Cả hai đều tăng thải nước và natri",
                    "effect": "Tăng nguy cơ mất nước, hạ huyết áp, suy thận cấp",
                    "management": "Theo dõi huyết áp và thể tích dịch. Có thể cần giảm liều diuretic hoặc tạm ngừng SGLT2i."
                }
            ],
            "moderate": [
                {
                    "drug": "Insulin, Sulfonylureas",
                    "mechanism": "SGLT2i tăng thải glucose qua nước tiểu, có thể tăng nguy cơ hạ đường huyết",
                    "effect": "Tăng nguy cơ hạ đường huyết",
                    "management": "Giảm liều insulin hoặc sulfonylurea khi bắt đầu SGLT2i. Theo dõi đường huyết chặt chẽ."
                },
                {
                    "drug": "ACE inhibitors, ARBs",
                    "mechanism": "Cả hai đều có thể ảnh hưởng đến chức năng thận",
                    "effect": "Tăng nguy cơ suy thận cấp (hiếm)",
                    "management": "Theo dõi eGFR và creatinine khi bắt đầu hoặc thay đổi liều."
                }
            ],
            "minor": [
                {
                    "drug": "Digoxin",
                    "mechanism": "SGLT2i có thể ảnh hưởng nhẹ đến nồng độ digoxin",
                    "effect": "Tăng nhẹ nồng độ digoxin",
                    "management": "Theo dõi nồng độ digoxin nếu dùng cùng."
                }
            ]
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
            "normal": "Không cần chỉnh liều",
            "30_60": "Có thể dùng nhưng cần điều chỉnh liều. Không dùng nếu eGFR <30.",
            "under_30": "CHỐNG CHỈ ĐỊNH nếu eGFR <25.",
            "dialysis": "CHỐNG CHỈ ĐỊNH. Không dùng khi đang lọc máu.",
            "notes": "Dapagliflozin chống chỉ định ở suy thận nặng (eGFR <25). Cần kiểm tra eGFR trước khi bắt đầu và định kỳ. Ngừng thuốc nếu eGFR giảm xuống dưới 25."
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
            "notes": "Không có antidote đặc hiệu. Điều trị quá liều chủ yếu là hỗ trợ: ngừng thuốc, bù dịch nếu mất nước, điều chỉnh đường huyết nếu hạ đường huyết, điều trị DKA nếu có."
        },
        "administration_instructions": {
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
                "organ_toxicity": ["genitourinary"],
                "qt_prolongation": False,
                "hepatotoxicity": False,
                "nephrotoxicity": False,
                "requires_monitoring": ["eGFR", "Genital/urinary infections"],
            },
            "guideline_tags": [
                "ADA 2024 Standards of Care - Diabetes",
                "AACE/ACE 2023 Type 2 Diabetes Guidelines",
                "FDA Black Box Warning - Fournier's Gangrene (rare)",
            ]
    },
    "Canagliflozin":     {
        "group": "Diabetes - SGLT2 Inhibitor",
        "vietnamese_name": "Canagliflozin, Invokana",
        "brand_names": {
            "common": [
                "Invokana"
    ],
            "vietnam": [
                "Invokana 100/300mg"
    ],
        },
        "administration": [
            "PO"
    ],
        "indications": [
            "Đái tháo đường type 2",
            "Giảm nguy cơ biến cố tim mạch ở bệnh nhân đái tháo đường type 2 có bệnh tim mạch"
    ],
        "dosage": {
            "dm_t2": "Khởi đầu 100mg x 1 lần/sáng trước bữa ăn đầu tiên. Có thể tăng lên 300mg nếu eGFR ≥60.",
            "notes": "Uống trước bữa ăn đầu tiên trong ngày. Không tăng liều nếu eGFR <60.",
        },
        "side_effects": [
            "Nhiễm nấm âm đạo",
            "Nhiễm trùng tiết niệu",
            "Đa niệu",
            "Hạ huyết áp",
            "Tăng nguy cơ gãy xương (Cảnh báo FDA)",
            "Tăng nguy cơ cắt cụt chi dưới (Cảnh báo FDA - Hiếm)",
            "DKA"
    ],
        "mechanism_of_action": """Ức chế SGLT2, tương tự các SGLT2i khác. Lợi ích tim mạch và thận (CANVAS, CREDENCE trials). Lưu ý: Có cảnh báo về nguy cơ gãy xương và cắt cụt chi dưới (hiếm).""",
        "monitoring": [
            "Đường huyết, eGFR, huyết áp",
            "Dấu hiệu nhiễm trùng, DKA",
            "Dấu hiệu đau chân, loét chân (nguy cơ cắt cụt)"
    ],
        "black_box_warnings": """Cảnh báo FDA về tăng nguy cơ cắt cụt chi dưới (hiếm, chủ yếu ở bệnh nhân có bệnh mạch máu ngoại vi). Ngừng thuốc nếu có loét chân, nhiễm trùng chân.""",
        "contraindications_detail": {
            "tuyệt_đối": [
                "Dị ứng với canagliflozin hoặc SGLT2 inhibitor",
                "Suy thận nặng (eGFR <30 mL/min)",
                "Nhiễm toan ceton do đái tháo đường"
    ],
            "tương_đối": [
                "Suy thận vừa (eGFR 30-60, cần điều chỉnh liều)",
                "Suy tim nặng",
                "Nhiễm trùng đường tiết niệu tái phát",
                "Nhiễm nấm sinh dục"
    ],
        },
        "contraindications": [],
        "interactions": [],
        "pregnancy": "",
        "precautions": [],
        "pharmacokinetics": {
        },
        "storage": "",
        "drug_interactions": {
            "major": [
                {
                    "drug": "Diuretics (Furosemide, Hydrochlorothiazide, etc.)",
                    "mechanism": "Cả hai đều tăng thải nước và natri",
                    "effect": "Tăng nguy cơ mất nước, hạ huyết áp, suy thận cấp",
                    "management": "Theo dõi huyết áp và thể tích dịch. Có thể cần giảm liều diuretic hoặc tạm ngừng SGLT2i."
                }
            ],
            "moderate": [
                {
                    "drug": "Insulin, Sulfonylureas",
                    "mechanism": "SGLT2i tăng thải glucose qua nước tiểu, có thể tăng nguy cơ hạ đường huyết",
                    "effect": "Tăng nguy cơ hạ đường huyết",
                    "management": "Giảm liều insulin hoặc sulfonylurea khi bắt đầu SGLT2i. Theo dõi đường huyết chặt chẽ."
                },
                {
                    "drug": "ACE inhibitors, ARBs",
                    "mechanism": "Cả hai đều có thể ảnh hưởng đến chức năng thận",
                    "effect": "Tăng nguy cơ suy thận cấp (hiếm)",
                    "management": "Theo dõi eGFR và creatinine khi bắt đầu hoặc thay đổi liều."
                }
            ],
            "minor": [
                {
                    "drug": "Digoxin",
                    "mechanism": "SGLT2i có thể ảnh hưởng nhẹ đến nồng độ digoxin",
                    "effect": "Tăng nhẹ nồng độ digoxin",
                    "management": "Theo dõi nồng độ digoxin nếu dùng cùng."
                }
            ]
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
            "normal": "Không cần chỉnh liều",
            "30_60": "Có thể dùng nhưng cần điều chỉnh liều. Không tăng liều lên 300mg nếu eGFR <60.",
            "under_30": "CHỐNG CHỈ ĐỊNH nếu eGFR <30.",
            "dialysis": "CHỐNG CHỈ ĐỊNH. Không dùng khi đang lọc máu.",
            "notes": "Canagliflozin chống chỉ định ở suy thận nặng (eGFR <30). Không tăng liều lên 300mg nếu eGFR <60. Cần kiểm tra eGFR trước khi bắt đầu và định kỳ. Ngừng thuốc nếu eGFR giảm xuống dưới 30."
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
            "notes": "Không có antidote đặc hiệu. Điều trị quá liều chủ yếu là hỗ trợ: ngừng thuốc, bù dịch nếu mất nước, điều chỉnh đường huyết nếu hạ đường huyết, điều trị DKA nếu có."
        },
        "administration_instructions": {
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
                "organ_toxicity": ["genitourinary"],
                "qt_prolongation": False,
                "hepatotoxicity": False,
                "nephrotoxicity": False,
                "requires_monitoring": ["eGFR", "Genital/urinary infections"],
            },
            "guideline_tags": [
                "ADA 2024 Standards of Care - Diabetes",
                "AACE/ACE 2023 Type 2 Diabetes Guidelines",
                "FDA Black Box Warning - Fournier's Gangrene (rare)",
            ]
    },
}
