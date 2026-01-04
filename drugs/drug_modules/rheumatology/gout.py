"""
Gout & Hyperuricemia Drugs (Thuốc điều trị Gout & Tăng acid uric)
"""

GOUT_DRUGS = {
    "Allopurinol":     {
        "group": "Rheumatology - Gout (Xanthine Oxidase Inhibitor)",
        "vietnamese_name": "Allopurinol, Zyloric",
        "brand_names": {
            "common": [
                "Zyloprim"
    ],
            "vietnam": [
                "Allopurinol 100/300mg",
                "Zyloric",
                "Sadapron"
    ],
        },
        "administration": [
            "PO"
    ],
        "indications": [
            "Gout mạn tính (hạ acid uric máu)",
            "Tăng acid uric do hóa trị ung thư",
            "Sỏi thận do acid uric"
    ],
        "contraindications": [
            "Quá mẫn với Allopurinol (đặc biệt: người mang gen HLA-B*5801)",
            "Cơn Gout cấp đang diễn tiến (không khởi trị lúc này, nhưng nếu đang dùng thì tiếp tục)"
    ],
        "dosage": {
            "gout_maintenance": "Khởi đầu 100 mg/ngày. Tăng dần mỗi 2-4 tuần đến 300 mg/ngày (max 800 mg).",
            "renal_impairment_crcl_10_20": "200 mg/ngày.",
            "renal_impairment_crcl_under_10": "100 mg/ngày.",
            "notes": """Quan trọng: Cần sàng lọc gen HLA-B*5801 ở người Việt Nam/Á Đông trước khi dùng để tránh hội chứng Steven-Johnson.""",
        },
        "side_effects": [
            "Dị ứng da (nhẹ đến nghiêm trọng - SJS/TEN)",
            "Khởi phát cơn Gout cấp khi mới bắt đầu điều trị (nên phối hợp Colchicine/NSAID trong 3-6 tháng đầu)"
    ],
        "mechanism_of_action": "Ức chế Xanthine Oxidase, enzyme chuyển hóa Hypoxanthine -> Xanthine -> Acid Uric.",
        "monitoring": [
            "Acid uric máu (Target <6 mg/dL)",
            "Chức năng thận",
            "Dấu hiệu dị ứng da"
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
            "primary_sources": [
                "FDA Drug Label - Allopurinol (Zyloprim)",
                "ACR Guidelines - Gout Management",
                "UpToDate - Allopurinol: Drug Information"
            ],
            "last_updated": "2025-02-18",
            "evidence_level": "High - FDA approved, ACR guidelines"
        },
        "risk_flags": {
            "high_alert": True,
            "narrow_therapeutic_index": False,
            "icu_critical_care_only": False,
            "bleeding_risk": None,
            "organ_toxicity": {"dermatologic": "Black Box Warning - Severe skin reactions (SJS/TEN - HLA-B*5801 carriers, especially Asians)", "hepatic": "Hepatotoxicity (rare)", "renal": "Nephrotoxicity (rare)"},
            "qt_prolongation": False,
            "hepatotoxicity": "Rare",
            "nephrotoxicity": "Rare",
            "requires_monitoring": ["Black Box Warning - HLA-B*5801 screening (especially Asians - SJS/TEN risk)", "Skin reactions (Black Box Warning - SJS/TEN signs, stop immediately)", "Serum uric acid (target <6 mg/dL)", "Renal function (dose adjustment required)", "Hepatic function (hepatotoxicity risk)", "Azathioprine/mercaptopurine interaction (contraindicated - severe myelosuppression)"],
            "look_alike_sound_alike": ["Allopurinol", "Allopurinol"]
        },
        "guideline_tags": [
            "FDA Black Box Warning - Severe Skin Reactions (SJS/TEN - HLA-B*5801 carriers)",
            "ACR Guidelines - Gout Management",
            "WHO Essential Medicines List"
        ],
        "last_updated": "2025-02-18"
    },
    "Colchicine":     {
        "group": "Rheumatology - Gout (Anti-inflammatory)",
        "vietnamese_name": "Colchicine",
        "brand_names": {
            "common": [
                "Colcrys"
    ],
            "vietnam": [
                "Colchicine 1mg",
                "Colgout"
    ],
        },
        "administration": [
            "PO"
    ],
        "indications": [
            "Cơn Gout cấp (Acute Gout)",
            "Dự phòng cơn Gout cấp khi bắt đầu dùng Allopurinol/Febuxostat",
            "Sốt Địa Trung Hải (Familial Mediterranean Fever)"
    ],
        "contraindications": [
            "Suy thận nặng + Suy gan nặng (CCĐ tuyệt đối)",
            "Dùng chung chất ức chế P-gp/CYP3A4 mạnh (Clarithromycin, Ketoconazole) ở người suy thận/gan"
    ],
        "dosage": {
            "acute_gout": """1.2 mg (ưu tiên) hoặc 1 mg ngay khi có triệu chứng, sau đó 0.6 mg (hoặc 0.5mg) sau 1 giờ. Tổng liều ngày đầu không quá 1.8 mg.""",
            "prophylaxis": "0.5-0.6 mg x 1-2 lần/ngày.",
            "notes": "Liều cao (Uống mỗi 2h đến khi tiêu chảy) KHÔNG CÒN ĐƯỢC KHUYẾN CÁO do độc tính cao.",
        },
        "side_effects": [
            "Tiêu chảy (chắc chắn xảy ra nếu liều cao)",
            "Suy tủy (hiếm, dùng lâu dài)",
            "Độc tính cơ"
    ],
        "mechanism_of_action": "Ức chế sự di cư của bạch cầu trung tính vào ổ viêm bằng cách gắn vào tubulin.",
        "monitoring": [
            "Công thức máu, CK (nếu đau cơ)",
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
            "primary_sources": [
                "FDA Drug Label - Colchicine (Colcrys)",
                "ACR Guidelines - Gout Management",
                "UpToDate - Colchicine: Drug Information"
            ],
            "last_updated": "2025-02-18",
            "evidence_level": "High - FDA approved, ACR guidelines"
        },
        "risk_flags": {
            "high_alert": True,
            "narrow_therapeutic_index": True,
            "icu_critical_care_only": False,
            "bleeding_risk": None,
            "organ_toxicity": {"gastrointestinal": "Severe diarrhea (dose-limiting toxicity)", "hematologic": "Bone marrow suppression (rare, long-term use)", "musculoskeletal": "Myopathy (rare, long-term use)", "renal": "Nephrotoxicity (with renal/hepatic impairment + P-gp/CYP3A4 inhibitors)"},
            "qt_prolongation": False,
            "hepatotoxicity": False,
            "nephrotoxicity": True,
            "requires_monitoring": ["CBC (bone marrow suppression risk with long-term use)", "CK (myopathy risk with long-term use)", "Renal function (nephrotoxicity risk, especially with P-gp/CYP3A4 inhibitors)", "Hepatic function (hepatotoxicity risk, especially with P-gp/CYP3A4 inhibitors)", "P-gp/CYP3A4 interactions (clarithromycin, ketoconazole - contraindicated with renal/hepatic impairment)", "GI symptoms (diarrhea - dose-limiting)"],
            "look_alike_sound_alike": ["Colchicine", "Colestipol"]
        },
        "guideline_tags": [
            "FDA Black Box Warning - Fatal Drug Interactions (P-gp/CYP3A4 inhibitors with renal/hepatic impairment)",
            "ACR Guidelines - Gout Management",
            "WHO Essential Medicines List"
        ],
        "last_updated": "2025-02-18"
    },
    "Febuxostat":     {
        "group": "Rheumatology - Gout (Xanthine Oxidase Inhibitor)",
        "vietnamese_name": "Febuxostat, Feburic",
        "brand_names": {
            "common": [
                "Uloric"
    ],
            "vietnam": [
                "Feburic 80mg",
                "Febus"
    ],
        },
        "administration": [
            "PO"
    ],
        "indications": [
            "Gout mạn tính (Khi không dung nạp hoặc không đáp ứng Allopurinol)",
            "Không cần chỉnh liều ở suy thận nhẹ-trung bình"
    ],
        "contraindications": [
            "Dùng chung với Azathioprine hoặc Mercaptopurine (CCĐ tuyệt đối)"
    ],
        "dosage": {
            "maintenance": "40 mg hoặc 80 mg x 1 lần/ngày.",
            "notes": """Cảnh báo an toàn về tim mạch (Cardiovascular death risk) cao hơn Allopurinol (FDA Boxed Warning cũ - nay đã giảm nhẹ nhưng vẫn cần thận trọng).""",
        },
        "mechanism_of_action": "Ức chế chọn lọc Xanthine Oxidase (Mạnh hơn Allopurinol).",
        "monitoring": [
            "Men gan",
            "Acid uric máu"
    ],
        "side_effects": [],
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
            "organ_toxicity": ["cardiovascular", "hepatic"],
            "qt_prolongation": False,
            "hepatotoxicity": True,
            "nephrotoxicity": False,
            "requires_monitoring": ["Cardiovascular events (Black Box Warning - increased risk of cardiovascular death vs allopurinol)", "Liver function (ALT, AST - hepatotoxicity risk)", "Serum uric acid", "Azathioprine/mercaptopurine interactions (contraindicated)"]
        },
        "guideline_tags": [
            "FDA Black Box Warning - Cardiovascular Death Risk (higher than allopurinol)",
            "FDA Black Box Warning - Azathioprine/Mercaptopurine Interaction (contraindicated)",
            "ACR Guidelines - Gout Management"
        ],
    },
}
