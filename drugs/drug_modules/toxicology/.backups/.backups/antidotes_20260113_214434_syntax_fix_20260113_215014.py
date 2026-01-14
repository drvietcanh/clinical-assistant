"""
Toxicology Antidotes (Thuốc giải độc)
"""

ANTIDOTES = {
    "Acetylcysteine":     {
        "group": "Toxicology - Antidote (Paracetamol)",
        "vietnamese_name": "Acetylcysteine, NAC",
        "brand_names": {
            "common": [
                "Acetadote",
                "Mucomyst"
    ],
            "vietnam": [
                "Acetylcysteine",
                "Mitux",
                "Acemuc (dạng uống)"
    ],
        },
        "administration": [
            "IV (Truyền tĩnh mạch)",
            "PO (Uống)"
    ],
        "indications": [
            "Ngộ độc Paracetamol (Acetaminophen) - Chỉ định hàng đầu",
            "Tiêu nhầy (Mucolytic) - liều thấp",
            "Dự phòng bệnh thận do thuốc cản quang (tranh cãi)"
    ],
        "contraindications": [
            "Dị ứng/Phản vệ với Acetylcysteine (Có thể dùng thận trọng nếu lợi ích > nguy cơ)"
    ],
        "dosage": {
            "antidote_iv_prescott": "Phác đồ 21 giờ: 150 mg/kg (1h) -> 50 mg/kg (4h) -> 100 mg/kg (16h).",
            "antidote_po_72h": "140 mg/kg (tải) -> 70 mg/kg mỗi 4h x 17 liều.",
            "notes": "Dùng càng sớm càng tốt (tốt nhất trong vòng 8-10h sau uống Paracetamol).",
        },
        "side_effects": [
            "Phản ứng phản vệ (Anaphylactoid reaction): Đỏ da, ngứa, tụt HA (thường xảy ra khi truyền IV liều tải quá nhanh). Xử trí: Tạm ngừng, kháng Histamin, truyền chậm lại.",
            "Buồn nôn/Nôn (đặc biệt dạng uống - mùi trứng thối)."
    ],
        "mechanism_of_action": """Cung cấp Cysteine để tổng hợp Glutathione, giúp trung hòa chất chuyển hóa độc hại của Paracetamol (NAPQI).""",
        "monitoring": [
            "Men gan (ALT/AST)",
            "PT/INR",
            "Dấu hiệu phản vệ"
    ],
        "interactions": [],
        "pregnancy": "B - Không có bằng chứng về nguy cơ ở người",
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
            "high_alert": True,
            "narrow_therapeutic_index": False,
            "bleeding_risk": False,
            "organ_toxicity": ["hepatic"],
            "qt_prolongation": False,
            "hepatotoxicity": False,
            "nephrotoxicity": False,
            "requires_monitoring": ["LFT", "PT/INR"]
        },
        "guideline_tags": [
            "FDA Drug Label - Acetylcysteine (Acetadote)",
            "Paracetamol Overdose Guidelines",
            "ISMP High Alert Medications - Emergency Medications"
        ]
    },
    "Atropine":     {
        "group": "Toxicology - Antidote (Organophosphate/Carbamate)",
        "vietnamese_name": "Atropine Sulfate",
        "brand_names": {
            "common": [
                "Atropine"
    ],
            "vietnam": [
                "Atropine"
    ],
        },
        "administration": [
            "IV",
            "IM",
            "SC"
    ],
        "indications": [
            "Ngộ độc Phospho hữu cơ (Organophosphate) và Carbamate",
            "Nhịp chậm có triệu chứng (Symptomatic Bradycardia)",
            "Tiền mê (giảm tiết)"
    ],
        "dosage": {
            "antidote_op_poisoning": """Người lớn: 1-5 mg IV mỗi 5-15 phút cho đến khi có dấu hiệu thấm Atropin (Da khô, đồng tử giãn, phổi hết ran ẩm). Liều có thể rất cao (hàng trăm mg).""",
            "bradycardia": "0.5-1 mg IV mỗi 3-5 phút (max 3 mg).",
            "notes": "Quan trọng nhất là đánh giá tình trạng phổi (hết ran ẩm).",
        },
        "side_effects": [
            "Khô miệng, Mắt nhìn mờ (do giãn đồng tử)",
            "Tim nhanh, Bí tiểu, Táo bón",
            "Loạn thần (Anticholinergic delirium)"
    ],
        "mechanism_of_action": "Đối kháng cạnh tranh với Acetylcholine tại thụ thể Muscarinic.",
        "monitoring": [
            "Nhịp tim",
            "Nghe phổi (Ran ẩm)",
            "Đồng tử"
    ],
        "contraindications": [],
        "interactions": [],
        "pregnancy": "",
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
            "high_alert": True,
            "narrow_therapeutic_index": False,
            "bleeding_risk": False,
            "organ_toxicity": [],
            "qt_prolongation": False,
            "hepatotoxicity": False,
            "nephrotoxicity": False,
            "requires_monitoring": ["ECG", "Vital Signs", "Respiratory"]
        },
        "guideline_tags": [
            "ACLS Guidelines 2020 - American Heart Association",
            "Organophosphate Poisoning Guidelines",
            "ISMP High Alert Medications - Emergency Medications"
        ]
    },
    "Pralidoxime":     {
        "group": "Toxicology - Antidote (Organophosphate)",
        "vietnamese_name": "Pralidoxime, PAM",
        "brand_names": {
            "common": [
                "Protopam"
    ],
            "vietnam": [
                "Pralidoxime",
                "PAM"
    ],
        },
        "administration": [
            "IV (Truyền tĩnh mạch chậm)"
    ],
        "indications": [
            "Ngộ độc Phospho hữu cơ (Organophosphate) - Phối hợp với Atropine",
            "KHÔNG dùng cho ngộ độc Carbamate (tranh cãi, thường không khuyến cáo)"
    ],
        "dosage": {
            "loading": "1-2 g IV truyền trong 15-30 phút.",
            "maintenance": "Truyền liên tục 8 mg/kg/giờ hoặc tiêm nhắc lại 1g mỗi 1h (nếu cần).",
            "notes": "Dùng sớm trong 24-48h đầu (trước khi enzyme bị lão hóa).",
        },
        "mechanism_of_action": "Tái hoạt hóa enzyme Acetylcholinesterase bị ức chế bởi Phospho hữu cơ.",
        "monitoring": [
            "Cơ lực",
            "Hô hấp"
    ],
        "side_effects": [],
        "contraindications": [],
        "interactions": [],
        "pregnancy": "C - Nguy cơ không thể loại trừ",
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
                "high_alert": True,
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
    "Vitamin K1":     {
        "group": "Toxicology - Antidote (Warfarin/Rodenticide)",
        "vietnamese_name": "Vitamin K1, Phytomenadione",
        "brand_names": {
            "common": [
                "Mephyton"
    ],
            "vietnam": [
                "Vitamin K1",
                "Vinphytton"
    ],
        },
        "administration": [
            "IV (Rất chậm)",
            "PO",
            "SC (Ít dùng)"
    ],
        "indications": [
            "Ngộ độc thuốc diệt chuột nhóm kháng Vitamin K (Warfarin, Superwarfarin)",
            "Quá liều Warfarin gây chảy máu hoặc INR quá cao",
            "Dự phòng xuất huyết não ở trẻ sơ sinh"
    ],
        "dosage": {
            "warfarin_reversal_bleeding": "10 mg IV chậm (kết hợp Plasma tươi/PCC).",
            "warfarin_high_inr_no_bleeding": "2.5-5 mg PO (uống).",
            "rodenticide_poisoning": "Liều cao kéo dài (50-100 mg/ngày) vì Superwarfarin thải trừ rất chậm (vài tháng).",
            "notes": "IV Vitamin K1 có nguy cơ phản vệ cao -> Tiêm RẤT CHẬM hoặc pha truyền.",
        },
        "side_effects": [
            "Phản vệ (IV nhanh)",
            "Đau tại chỗ tiêm"
    ],
        "monitoring": [
            "INR (thường xuyên)"
    ],
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
    "Ethanol":     {
        "group": "Toxicology - Antidote (Methanol/Ethylene Glycol)",
        "vietnamese_name": "Ethanol 20% (Rượu uống)",
        "brand_names": {
            "vietnam": [
                "Rượu trắng (nếu cấp cứu không có Ethanol y tế)",
                "Ethanol 20% pha chế"
    ],
        },
        "administration": [
            "PO (Uống/SND)",
            "IV (ít có chế phẩm sẵn)"
    ],
        "indications": [
            "Ngộ độc Methanol (Cồn công nghiệp) hoặc Ethylene Glycol"
    ],
        "dosage": {
            "loading": "0.8 g/kg (tương đương 4 ml/kg rượu 20% hoặc 2 ml/kg rượu 40% - Vodka).",
            "maintenance": "0.1-0.15 g/kg/giờ. Tăng liều nếu đang lọc máu.",
            "target": "Nồng độ Ethanol máu 100-150 mg/dL.",
            "notes": "Cạnh tranh chuyển hóa với Methanol, ngăn tạo ra Acid Formic độc hại.",
        },
        "monitoring": [
            "Nồng độ Ethanol máu",
            "Khí máu (Toan chuyển hóa)",
            "Khoảng trống Anion/Osmol"
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
            "high_alert": True,
            "narrow_therapeutic_index": False,
            "bleeding_risk": False,
            "organ_toxicity": ["hepatic", "metabolic"],
            "qt_prolongation": False,
            "hepatotoxicity": False,
            "nephrotoxicity": False,
            "requires_monitoring": ["Ethanol Levels", "Arterial Blood Gas", "Electrolytes"]
        },
        "guideline_tags": [
            "Methanol/Ethylene Glycol Poisoning Guidelines",
            "FDA Drug Information",
            "ISMP High Alert Medications - Emergency Medications"
        ]
    },
}
