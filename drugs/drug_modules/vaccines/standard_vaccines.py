"""
Standard Vaccines (Vắc xin tiêm chủng & dịch vụ)
"""

STANDARD_VACCINES = {
    "VAT (Tetanus Vaccine)":     {
        "group": "Vaccines - Tetanus (Uốn ván)",
        "vietnamese_name": "Vắc xin Uốn ván hấp phụ (VAT)",
        "brand_names": {
            "common": [
                "VAT",
                "Tetavax"
    ],
            "vietnam": [
                "VAT (IVAC)",
                "Tetavax (Pháp)"
    ],
        },
        "administration": [
            "IM (Cơ Delta)"
    ],
        "indications": [
            "Dự phòng uốn ván cho người bị thương có nguy cơ",
            "Tiêm chủng mở rộng cho phụ nữ mang thai và người lớn"
    ],
        "contraindications": {
            "absolute": [
                "Dị ứng nặng với liều tiêm trước",
                "Đang sốt cao hoặc bệnh cấp tính (hoãn tiêm)"
    ],
        },
        "dosage": {
            "wound_management": "0.5 ml IM. (Kết hợp SAT/HTIG nếu vết thương bẩn và chưa tiêm đủ liều).",
            "pregnancy": "Lịch tiêm 2-5 mũi tùy tiền sử. Mũi 2 cách mũi 1 ít nhất 1 tháng, trước sinh 1 tháng.",
            "notes": "Lắc kỹ trước khi tiêm.",
        },
        "side_effects": [
            "Sưng đau tại chỗ tiêm (thường gặp)",
            "Sốt nhẹ",
            "Sốc phản vệ (hiếm)"
    ],
        "storage": "2-8 độ C. Không được đông băng.",
        "interactions": [],
        "pregnancy": "",
        "mechanism_of_action": "",
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
        "overdose_management": {
            "symptoms": [],
            "antidote": "",
            "treatment": [],
            "monitoring": "",
        },
        "reversal_agents": None,
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
    "Verorab (Rabies Vaccine)":     {
        "group": "Vaccines - Rabies (Dại)",
        "vietnamese_name": "Vắc xin phòng Dại (Verorab, Abhayrab)",
        "brand_names": {
            "common": [
                "Verorab",
                "Abhayrab",
                "Indirab"
    ],
            "vietnam": [
                "Verorab (Pháp)",
                "Abhayrab (Ấn Độ)"
    ],
        },
        "administration": [
            "IM (Cơ Delta) - KHÔNG tiêm mông",
            "Tiêm trong da (ID)"
    ],
        "indications": [
            "Dự phòng sau phơi nhiễm (PEP) - Khi bị chó/mèo cắn/cào",
            "Dự phòng trước phơi nhiễm (PrEP) - Người nguy cơ cao (thú y)"
    ],
        "contraindications": {
            "pep_post_exposure": "KHÔNG CÓ CHỐNG CHỈ ĐỊNH TUYỆT ĐỐI VỚI ĐIỀU TRỊ DỰ PHÒNG SAU PHƠI NHIỄM (vì bệnh Dại tử vong 100%).",
            "prep_pre_exposure": "Dị ứng nặng, sốt cao (hoãn)",
        },
        "dosage": {
            "pep_im_essen": "Lịch 5 mũi (Ngày 0, 3, 7, 14, 28). 0.5 ml/lần.",
            "pep_id_thai_red_cross": "Lịch 2-2-2-0-2 (Ngày 0, 3, 7, 28). Tiêm 2 điểm 0.1 ml mỗi lần.",
            "notes": "Nếu vết thương độ III (chảy máu, niêm mạc): CẦN PHỐI HỢP HUYẾT THANH KHÁNG DẠI (SAR).",
        },
        "side_effects": [
            "Đau tại chỗ, sốt, mệt mỏi.",
            "Phản ứng phụ hiếm gặp: Hội chứng Guillain-Barre (rất hiếm)."
    ],
        "storage": "2-8 độ C. Hoàn nguyên xong dùng ngay.",
        "interactions": [],
        "pregnancy": "",
        "mechanism_of_action": "",
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
        "overdose_management": {
            "symptoms": [],
            "antidote": "",
            "treatment": [],
            "monitoring": "",
        },
        "reversal_agents": None,
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
    "Influenza Vaccine":     {
        "group": "Vaccines - Influenza (Cúm)",
        "vietnamese_name": "Vắc xin Cúm (Vaxigrip, Influvac)",
        "brand_names": {
            "common": [
                "Vaxigrip Tetra",
                "Influvac Tetra",
                "GC Flu"
    ],
            "vietnam": [
                "Vaxigrip Tetra (Pháp)",
                "Influvac Tetra (Hà Lan)",
                "Ivacflu-S (Việt Nam)"
    ],
        },
        "administration": [
            "IM (Cơ Delta) hoặc SC sâu"
    ],
        "indications": [
            "Phòng ngừa cúm mùa (người lớn và trẻ em >6 tháng)"
    ],
        "contraindications": [
            "Dị ứng nặng với trứng gà (Ovalbumin) - thận trọng hoặc chống chỉ định tùy loại",
            "Hội chứng Guillain-Barre sau tiêm cúm trước đó (trong vòng 6 tuần)",
            "Đang sốt cao"
    ],
        "dosage": {
            "adult_child": "0.5 ml IM. Tiêm nhắc lại hàng năm.",
            "child_6m_9y_first_time": "2 mũi cách nhau 4 tuần (nếu lần đầu tiêm cúm).",
        },
        "side_effects": [
            "Đau tại chỗ, sốt nhẹ, đau cơ."
    ],
        "storage": "2-8 độ C.",
        "interactions": [],
        "pregnancy": "",
        "mechanism_of_action": "",
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
        "overdose_management": {
            "symptoms": [],
            "antidote": "",
            "treatment": [],
            "monitoring": "",
        },
        "reversal_agents": None,
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
    "Hepatitis B Vaccine":     {
        "group": "Vaccines - Hepatitis B (Viêm gan B)",
        "vietnamese_name": "Vắc xin Viêm gan B (Engerix B, Euvax B)",
        "brand_names": {
            "common": [
                "Engerix B",
                "Euvax B",
                "Heberbiovac HB"
    ],
            "vietnam": [
                "Gene-HBvax (Việt Nam)",
                "Engerix B (Bỉ)",
                "Euvax B (Hàn Quốc)"
    ],
        },
        "administration": [
            "IM (Cơ Delta - người lớn; Đùi - trẻ em)"
    ],
        "indications": [
            "Phòng ngừa viêm gan B (Sơ sinh, người lớn chưa có miễn dịch)"
    ],
        "dosage": {
            "adult": "Lịch 0-1-6 tháng (3 mũi). 1 ml (20mcg).",
            "newborn": "Tiêm trong 24h đầu sau sinh. Nếu mẹ HBsAg(+), tiêm cùng kháng huyết thanh (HBIg).",
        },
        "side_effects": [
            "Đau tại chỗ, sốt nhẹ."
    ],
        "storage": "2-8 độ C. Không để đông băng.",
        "contraindications": [],
        "interactions": [],
        "pregnancy": "",
        "mechanism_of_action": "",
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
        "overdose_management": {
            "symptoms": [],
            "antidote": "",
            "treatment": [],
            "monitoring": "",
        },
        "reversal_agents": None,
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
