"""
Osteoporosis Drugs (Thuốc loãng xương)
"""

OSTEOPOROSIS_DRUGS = {
    "Alendronate":     {
        "group": "Rheumatology - Bisphosphonate (Oral)",
        "vietnamese_name": "Alendronate, Fosamax",
        "brand_names": {
            "common": [
                "Fosamax"
    ],
            "vietnam": [
                "Fosamax 70mg",
                "Alendronate Stada"
    ],
        },
        "administration": [
            "PO"
    ],
        "indications": [
            "Điều trị loãng xương ở phụ nữ mãn kinh",
            "Loãng xương do Corticoid",
            "Bệnh Paget xương"
    ],
        "contraindications": [
            "Bất thường thực quản (hẹp, không giãn)",
            "Không thể đứng hoặc ngồi thẳng trong ít nhất 30 phút",
            "Hạ Calci máu",
            "Suy thận nặng (CrCl < 35 ml/phút)"
    ],
        "dosage": {
            "treatment": "70 mg uống 1 lần/tuần (dạng phối hợp Vitamin D rất phổ biến).",
            "prevention": "35 mg uống 1 lần/tuần.",
            "notes": """Phải uống vào buổi sáng, bụng đói, với 1 ly nước đầy. Không nằm trong 30 phút sau uống để tránh loét thực quản.""",
        },
        "side_effects": [
            "Kích ứng thực quản, loét thực quản (nghiêm trọng)",
            "Hoại tử xương hàm (Osteonecrosis of the jaw - ONJ) - hiếm gặp, thường ở liều cao hoặc ung thư",
            "Gãy xương đùi không điển hình (dùng lâu dài)"
    ],
        "mechanism_of_action": "Ức chế hoạt động của hủy cốt bào (Osteoclasts), giảm tiêu xương.",
        "monitoring": [
            "Mật độ xương (DEXA scan)",
            "Calci, Vitamin D",
            "Chức năng thận"
    ],
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
            "organ_toxicity": ["gastrointestinal", "skeletal"],
            "qt_prolongation": False,
            "hepatotoxicity": False,
            "nephrotoxicity": False,
            "requires_monitoring": ["Esophageal symptoms (Black Box Warning - esophageal ulceration)", "Bone density (DEXA scan)", "Calcium, Vitamin D", "Renal function", "ONJ signs (osteonecrosis of jaw - rare)", "Atypical femur fractures (long-term use)"]
        },
        "guideline_tags": [
            "FDA Black Box Warning - Esophageal Ulceration",
            "FDA Black Box Warning - Osteonecrosis of Jaw (ONJ)",
            "FDA Black Box Warning - Atypical Femur Fractures (long-term use)",
            "ACR Guidelines - Osteoporosis",
            "WHO Essential Medicines List"
        ],
    },
    "Zoledronic Acid":     {
        "group": "Rheumatology - Bisphosphonate (IV)",
        "vietnamese_name": "Zoledronic Acid, Aclasta, Zometa",
        "brand_names": {
            "common": [
                "Reclast",
                "Zometa"
    ],
            "vietnam": [
                "Aclasta 5mg/100ml",
                "Zometa 4mg (cho ung thư)"
    ],
        },
        "administration": [
            "IV (Truyền tĩnh mạch)"
    ],
        "indications": [
            "Loãng xương ở phụ nữ mãn kinh (Aclasta - 1 năm/1 lần)",
            "Tăng Calci máu do ung thư (Zometa)",
            "Đa u tủy xương (Multiple Myeloma)"
    ],
        "dosage": {
            "osteoporosis": "5 mg truyền tĩnh mạch (ít nhất 15 phút) mỗi 1 năm/lần.",
            "hypercalcemia_cancer": "4 mg truyền tĩnh mạch.",
            "notes": """Bệnh nhân phải được bù đủ nước trước khi truyền. Có thể gây hội chứng giả cúm (sốt, đau cơ) trong 1-3 ngày sau truyền.""",
        },
        "side_effects": [
            "Sốt, đau cơ (Hội chứng giả cúm)",
            "Suy thận cấp (nếu truyền nhanh hoặc thiếu nước)",
            "Hoại tử xương hàm"
    ],
        "renal_adjustment": {
            "crcl_under_35": "Chống chỉ định (với loãng xương).",
        },
        "monitoring": [
            "Creatinine trước mỗi lần truyền",
            "Calci máu"
    ],
        "contraindications": [],
        "interactions": [],
        "pregnancy": "D - Có bằng chứng về nguy cơ. Không khuyến nghị trong thai kỳ",
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
            "organ_toxicity": ["renal", "skeletal"],
            "qt_prolongation": False,
            "hepatotoxicity": False,
            "nephrotoxicity": True,
            "requires_monitoring": ["Renal function (creatinine - Black Box Warning - acute renal failure if rapid infusion or dehydration)", "Calcium (hypocalcemia risk)", "Flu-like syndrome (fever, myalgia - common)", "ONJ signs (osteonecrosis of jaw - Black Box Warning)", "Atypical femur fractures (long-term use - Black Box Warning)"]
        },
        "guideline_tags": [
            "FDA Black Box Warning - Renal Impairment (acute renal failure if rapid infusion or dehydration)",
            "FDA Black Box Warning - Osteonecrosis of Jaw (ONJ)",
            "FDA Black Box Warning - Atypical Femur Fractures (long-term use)",
            "ACR Guidelines - Osteoporosis",
            "WHO Essential Medicines List"
        ],
    },
}
