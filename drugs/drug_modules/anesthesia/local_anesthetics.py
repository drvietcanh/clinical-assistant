"""
Local Anesthetics (Amides & Esters)
"""

LOCAL_ANESTHETICS = {
    "Lidocaine": {
        "group": "Anesthesia - Local Anesthetic (Amide)",
        "vietnamese_name": "Lidocaine, Xylocaine",
        "brand_names": {
            "common": ["Xylocaine"],
            "vietnam": ["Lidocaine", "Xylocaine", "Lidocain"]
        },
        "administration": ["Injection (Subcutaneous, IV)", "Topical", "Spray"],
        "indications": [
            "Gây tê tại chỗ (Infiltration anesthesia)",
            "Gây tê vùng (Regional block)",
            "Chống loạn nhịp tim (IV) - Nhóm 1b",
            "Giảm đau khi tiêm Propofol (mixed)"
        ],
        "contraindications": {
            "absolute": [
                "Dị ứng với nhóm Amide",
                "Hội chứng Adams-Stokes, Hội chứng Wolff-Parkinson-White (cho đường IV)",
                "Block tim nặng (nếu không có máy tạo nhịp)"
            ]
        },
        "dosage": {
            "infiltration_max": "4.5 mg/kg (không có Epinephrine). Tối đa 300 mg.",
            "infiltration_with_epi": "7 mg/kg (có Epinephrine). Tối đa 500 mg. (Epinephrine làm co mạch, giảm hấp thu, kéo dài tác dụng).",
            "iv_arrhythmia": "1-1.5 mg/kg bolus.",
            "notes": "Epinephrine KHÔNG dùng cho ngón tay, ngón chân, dương vật, mũi, tai (nguy cơ hoại tử)."
        },
        "side_effects": [
            "Ngộ độc thuốc tê (LAST - Local Anesthetic Systemic Toxicity):",
            "  - Thần kinh: Tê quanh miệng, vị kim loại, ù tai -> Co giật -> Hôn mê.",
            "  - Tim mạch: Tụt HA, Loạn nhịp, Ngừng tim.",
            "Dị ứng (hiếm với nhóm Amide, thường do chất bảo quản Paraben)"
        ],
        "mechanism_of_action": "Chẹn kênh Natri điện thế, ngăn chặn dẫn truyền xung động thần kinh.",
        "monitoring": ["Dấu hiệu ngộ độc thần kinh trung ương (quan trọng)", "Huyết áp, Nhịp tim"],
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
       
antidote": "Lipid Emulsion 20% (Intralipid) - Cứu cánh trong ngộ độc thuốc tê toàn thân (LAST)."
    },

    "Bupivacaine":     {
        "group": "Anesthesia - Local Anesthetic (Amide)",
        "vietnamese_name": "Bupivacaine, Marcaine",
        "brand_names": {
            "common": [
                "Marcaine",
                "Sensorcaine"
    ],
            "vietnam": [
                "Bupivacaine",
                "Marcaine"
    ],
        },
        "administration": [
            "Injection (Infiltration, Epidural, Spinal, Nerve block)"
    ],
        "indications": [
            "Gây tê vùng (Regional anesthesia) - Tác dụng dài",
            "Gây tê tủy sống (Spinal), Ngoài màng cứng (Epidural)",
            "Giảm đau sau mổ"
    ],
        "contraindications": {
            "absolute": [
                "Dị ứng nhóm Amide",
                "Gây tê vùng tĩnh mạch (IVRA - Bier block) - CHỐNG CHỈ ĐỊNH TUYỆT ĐỐI do độc tính tim cao."
    ],
        },
        "dosage": {
            "max_dose": "2 mg/kg. Tối đa 175 mg (không có Epi) hoặc 225 mg (có Epi) mỗi lần dùng.",
            "spinal": "10-20 mg (tùy tỷ trọng - hyperbaric/isobaric).",
            "notes": "Độc tính trên tim cao hơn Lidocaine nhiều. Gây rung thất khó điều trị.",
        },
        "side_effects": [
            "Độc tính tim (Cardiotoxicity) - Nguy hiểm nhất: Rung thất, Ngừng tim khó cấp cứu.",
            "LAST (như Lidocaine nhưng nặng nề hơn về tim mạch)",
            "Hạ huyết áp (khi gây tê tủy sống/NMC)"
    ],
        "mechanism_of_action": "Chẹn kênh Natri (mạnh hơn và kéo dài hơn Lidocaine).",
        "antidote": "Lipid Emulsion 20% (Intralipid) - Bắt buộc phải có sẵn khi dùng Bupivacaine.",
        "interactions": [],
        "pregnancy": "",
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
    },
    "Levobupivacaine":     {
        "group": "Anesthesia - Local Anesthetic (Amide)",
        "vietnamese_name": "Levobupivacaine, Chirocaine",
        "brand_names": {
            "common": [
                "Chirocaine"
    ],
            "vietnam": [
                "Levobupivacaine",
                "Chirocaine"
    ],
        },
        "administration": [
            "Injection"
    ],
        "indications": [
            "Tương tự Bupivacaine nhưng ít độc tính trên tim và thần kinh hơn."
    ],
        "dosage": {
            "max_dose": "2 mg/kg. Tối đa 150 mg.",
            "notes": "Là đồng phân tả tuyền (S-enantiomer) của Bupivacaine. An toàn hơn Bupivacaine.",
        },
        "antidote": "Lipid Emulsion 20%.",
        "side_effects": [],
        "contraindications": [],
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
