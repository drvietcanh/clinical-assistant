"""
DMARDs - Disease-Modifying Antirheumatic Drugs
Thuốc điều trị bệnh thấp khớp, Lupus, bệnh tự miễn.
"""

DMARDS_DRUGS = {
    "Methotrexate":     {
        "group": "Rheumatology - DMARD (Immunosuppressant)",
        "vietnamese_name": "Methotrexate",
        "brand_names": {
            "common": [
                "Trexall",
                "Rheumatrex"
    ],
            "vietnam": [
                "Methotrexate 2.5mg"
    ],
        },
        "administration": [
            "PO",
            "SC",
            "IM"
    ],
        "indications": [
            "Viêm khớp dạng thấp (Rheumatoid Arthritis) - Thuốc đầu tay",
            "Viêm khớp vảy nến (Psoriatic Arthritis)",
            "Lupus ban đỏ hệ thống (SLE)",
            "Viêm da vảy nến (Psoriasis)",
            "Ung thư (Leukemia, Lymphoma) - Liều cao"
    ],
        "contraindications": [
            "Có thai (Gây quái thai nghiêm trọng)",
            "Cho con bú",
            "Suy gan nặng",
            "Suy thận nặng",
            "Suy tủy xương",
            "Nghiện rượu"
    ],
        "dosage": {
            "ra_low_dose": "7.5-25mg PO/SC/IM x 1 lần/tuần (không phải mỗi ngày!).",
            "psoriasis": "10-25mg x 1 lần/tuần.",
            "notes": """QUAN TRỌNG: Uống 1 lần/TUẦN, không phải mỗi ngày! Bổ sung Folic Acid 1mg/ngày (trừ ngày uống MTX) để giảm tác dụng phụ.""",
        },
        "side_effects": [
            "Buồn nôn, nôn (phổ biến)",
            "Loét miệng (Stomatitis)",
            "Suy tủy xương (Giảm bạch cầu, tiểu cầu, hồng cầu)",
            "Độc gan (Xơ gan nếu dùng lâu dài)",
            "Viêm phổi do Methotrexate (MTX pneumonitis) - Hiếm nhưng nguy hiểm",
            "Rụng tóc",
            "Nhiễm trùng (do ức chế miễn dịch)"
    ],
        "interactions": [
            "NSAIDs (liều cao): Tăng độc tính MTX (giảm thải trừ qua thận).",
            "Trimethoprim/Sulfamethoxazole: Tăng độc tính MTX.",
            "PPI (Omeprazole): Tăng nồng độ MTX.",
            "Rượu: Tăng nguy cơ độc gan."
    ],
        "mechanism_of_action": """Chất đối kháng Folic Acid, ức chế dihydrofolate reductase (DHFR) → Ức chế tổng hợp DNA → Ức chế tế bào phân chia nhanh (lymphocyte, tế bào ung thư). Liều thấp (RA): Chống viêm, ức chế miễn dịch.""",
        "monitoring": [
            "Công thức máu (CBC) - Mỗi 2-4 tuần khi bắt đầu, sau đó mỗi 8-12 tuần",
            "Men gan (ALT, AST) - Mỗi 2-4 tuần khi bắt đầu, sau đó mỗi 8-12 tuần",
            "Chức năng thận (Creatinine, eGFR)",
            "Dấu hiệu nhiễm trùng",
            "Dấu hiệu viêm phổi (ho, khó thở)"
    ],
        "precautions": [
            "TUYỆT ĐỐI TRÁNH THAI - Gây quái thai nghiêm trọng (tránh thai ≥3 tháng sau ngừng thuốc)",
            "Uống 1 lần/TUẦN, không phải mỗi ngày (sai lầm phổ biến → ngộ độc)",
            "Bổ sung Folic Acid 1mg/ngày (trừ ngày uống MTX) để giảm tác dụng phụ",
            "Tránh rượu (tăng nguy cơ độc gan)",
            "Ngừng thuốc nếu nhiễm trùng nặng",
            "Theo dõi men gan, công thức máu định kỳ"
    ],
        "black_box_warnings": """Gây quái thai nghiêm trọng. Độc tủy xương, độc gan, độc phổi có thể gây tử vong. Chỉ dùng cho bệnh nhân có thể tuân thủ theo dõi chặt chẽ.""",
        "risk_flags": {
            "high_alert": True,
            "narrow_therapeutic_index": False,
            "icu_critical_care_only": False,
            "bleeding_risk": "High (thrombocytopenia)",
            "organ_toxicity": {"teratogenic": "Black Box Warning - Teratogenicity (severe birth defects)", "hematologic": "Black Box Warning - Bone marrow suppression (may be fatal)", "hepatic": "Black Box Warning - Hepatotoxicity (cirrhosis with long-term use)", "pulmonary": "Black Box Warning - Pneumonitis (rare but fatal)", "renal": "Nephrotoxicity (rare)", "gastrointestinal": "Mucositis, stomatitis"},
            "qt_prolongation": False,
            "hepatotoxicity": True,
            "nephrotoxicity": "Rare",
            "requires_monitoring": ["Black Box Warning - Pregnancy test (teratogenicity)", "CBC (Black Box Warning - bone marrow suppression, every 2-4 weeks initially, then every 8-12 weeks)", "Hepatic function (ALT, AST - Black Box Warning for hepatotoxicity, every 2-4 weeks initially, then every 8-12 weeks)", "Renal function (creatinine, eGFR - nephrotoxicity risk)", "Pulmonary symptoms (Black Box Warning - pneumonitis signs: cough, dyspnea)", "Folic acid supplementation (1mg/day except MTX day - reduces side effects)", "Weekly dosing (NOT daily - common error leads to overdose)", "NSAID/trimethoprim-sulfamethoxazole interactions (increase MTX toxicity)"],
            "look_alike_sound_alike": ["Methotrexate", "Metformin"]
        },
        "guideline_tags": [
            "FDA Black Box Warning - Teratogenicity (severe birth defects)",
            "FDA Black Box Warning - Bone Marrow Suppression (may be fatal)",
            "FDA Black Box Warning - Hepatotoxicity (cirrhosis with long-term use)",
            "FDA Black Box Warning - Pneumonitis (rare but fatal)",
            "ACR Guidelines - Rheumatoid Arthritis",
            "ACR Guidelines - Psoriatic Arthritis",
            "WHO Essential Medicines List"
        ],
        "last_updated": "2025-02-18",
        "pregnancy": "",
        "pharmacokinetics": {
        },
        "storage": "",
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
    "Hydroxychloroquine":     {
        "group": "Rheumatology - DMARD (Antimalarial)",
        "vietnamese_name": "Hydroxychloroquine",
        "brand_names": {
            "common": [
                "Plaquenil"
    ],
            "vietnam": [
                "Plaquenil 200mg"
    ],
        },
        "administration": [
            "PO"
    ],
        "indications": [
            "Lupus ban đỏ hệ thống (SLE) - Thuốc nền",
            "Viêm khớp dạng thấp (RA) - Nhẹ đến trung bình",
            "Sốt rét (Malaria) - Dự phòng và điều trị"
    ],
        "dosage": {
            "sle_ra": "200-400mg/ngày (≤5mg/kg/ngày dựa trên cân nặng lý tưởng).",
            "malaria_prophylaxis": "400mg x 1 lần/tuần.",
            "notes": "Uống với thức ăn để giảm buồn nôn. Tác dụng chậm (2-6 tháng).",
        },
        "side_effects": [
            "Buồn nôn, tiêu chảy (phổ biến, nhẹ)",
            "Độc võng mạc (Retinopathy) - Hiếm nhưng nghiêm trọng, không hồi phục",
            "Phát ban da",
            "Đau đầu",
            "Rối loạn nhịp tim (QT prolongation) - Hiếm"
    ],
        "interactions": [
            "Thuốc kéo dài QT (Azithromycin, Amiodarone): Tăng nguy cơ rối loạn nhịp tim.",
            "Digoxin: Tăng nồng độ digoxin.",
            "Insulin, Sulfonylurea: Tăng nguy cơ hạ đường huyết."
    ],
        "mechanism_of_action": """Cơ chế chưa rõ hoàn toàn. Ức chế miễn dịch, chống viêm bằng cách: Ức chế Toll-like receptors (TLR), giảm sản xuất cytokine, ổn định lysosome. An toàn hơn Methotrexate.""",
        "monitoring": [
            "Khám mắt (Ophthalmology) - Trước điều trị (baseline), sau đó mỗi năm (phát hiện độc võng mạc)",
            "Không cần theo dõi xét nghiệm máu thường xuyên (khác Methotrexate)",
            "ECG (nếu có nguy cơ QT prolongation)"
    ],
        "precautions": [
            "Nguy cơ độc võng mạc - Khám mắt định kỳ mỗi năm",
            "Liều ≤5mg/kg/ngày (dựa trên cân nặng lý tưởng) để giảm nguy cơ độc võng mạc",
            "Tác dụng chậm (2-6 tháng) - Cần kiên nhẫn",
            "An toàn hơn Methotrexate - Ít tác dụng phụ",
            "Có thể dùng trong thai kỳ (Category C, an toàn hơn MTX)"
    ],
        "contraindications": [],
        "pregnancy": "",
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
    "Sulfasalazine":     {
        "group": "Rheumatology - DMARD",
        "vietnamese_name": "Sulfasalazine",
        "brand_names": {
            "common": [
                "Azulfidine"
    ],
            "vietnam": [
                "Sulfasalazine 500mg"
    ],
        },
        "administration": [
            "PO"
    ],
        "indications": [
            "Viêm khớp dạng thấp (RA)",
            "Viêm khớp cột sống dính khớp (Ankylosing Spondylitis)",
            "Bệnh viêm ruột (IBD - Ulcerative Colitis)"
    ],
        "dosage": {
            "ra": "Khởi đầu 500mg x 2 lần/ngày, tăng dần đến 1000mg x 2 lần/ngày (2-3g/ngày).",
            "notes": "Uống với thức ăn. Tăng liều từ từ để giảm buồn nôn.",
        },
        "side_effects": [
            "Buồn nôn, nôn (phổ biến)",
            "Đau đầu",
            "Phát ban da",
            "Giảm số lượng tinh trùng (Oligospermia) - Hồi phục sau ngừng thuốc",
            "Suy tủy (Hiếm)",
            "Độc gan (Hiếm)"
    ],
        "mechanism_of_action": """Chuyển hóa thành Sulfapyridine (kháng khuẩn) và 5-ASA (chống viêm). Cơ chế chống viêm ở RA chưa rõ hoàn toàn.""",
        "monitoring": [
            "Công thức máu (CBC) - Định kỳ",
            "Men gan (ALT, AST)",
            "Dấu hiệu dị ứng"
    ],
        "precautions": [
            "Dị ứng Sulfa - Chống chỉ định",
            "Giảm số lượng tinh trùng - Thông báo nam giới",
            "Uống với thức ăn, tăng liều từ từ"
    ],
        "contraindications": [],
        "interactions": [],
        "pregnancy": "",
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
            "organ_toxicity": ["hematologic", "hepatic", "reproductive"],
            "qt_prolongation": False,
            "hepatotoxicity": True,
            "nephrotoxicity": False,
            "requires_monitoring": ["CBC (bone marrow suppression - rare)", "Liver function (ALT, AST - hepatotoxicity rare)", "Allergic reactions (sulfa allergy - contraindicated)", "Sperm count (oligospermia - reversible)"]
        },
        "guideline_tags": [
            "ACR Guidelines - Rheumatoid Arthritis",
            "ACR Guidelines - Ankylosing Spondylitis",
            "WHO Essential Medicines List"
        ],
    },
    "Leflunomide":     {
        "group": "Rheumatology - DMARD",
        "vietnamese_name": "Leflunomide",
        "brand_names": {
            "common": [
                "Arava"
    ],
            "vietnam": [
                "Arava 10/20mg"
    ],
        },
        "administration": [
            "PO"
    ],
        "indications": [
            "Viêm khớp dạng thấp (RA)",
            "Viêm khớp vảy nến (Psoriatic Arthritis)"
    ],
        "dosage": {
            "ra": "Loading dose: 100mg/ngày x 3 ngày (tùy chọn). Duy trì: 10-20mg/ngày.",
            "notes": "Tác dụng nhanh hơn Methotrexate nếu dùng loading dose.",
        },
        "side_effects": [
            "Tiêu chảy (phổ biến)",
            "Tăng huyết áp",
            "Rụng tóc",
            "Độc gan",
            "Gây quái thai (tương tự Methotrexate)",
            "Nhiễm trùng"
    ],
        "mechanism_of_action": "Ức chế dihydroorotate dehydrogenase (DHODH) → Ức chế tổng hợp pyrimidine → Ức chế lymphocyte.",
        "monitoring": [
            "Men gan (ALT, AST) - Mỗi tháng trong 6 tháng đầu",
            "Huyết áp",
            "Công thức máu (CBC)"
    ],
        "precautions": [
            "TUYỆT ĐỐI TRÁNH THAI - Gây quái thai",
            "Thải trừ rất chậm (có thể còn trong cơ thể 2 năm)",
            "Nếu cần mang thai: Phải làm washout với Cholestyramine",
            "Theo dõi men gan chặt chẽ"
    ],
        "black_box_warnings": "Gây quái thai nghiêm trọng. Độc gan nghiêm trọng.",
        "contraindications": [],
        "interactions": [],
        "pregnancy": "",
        "pharmacokinetics": {
        },
        "storage": "",
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
            "organ_toxicity": ["hepatic", "teratogenic"],
            "qt_prolongation": False,
            "hepatotoxicity": True,
            "nephrotoxicity": False,
            "requires_monitoring": ["Black Box Warning - Pregnancy test (teratogenicity)", "Liver function (ALT, AST - Black Box Warning for hepatotoxicity, monthly for first 6 months)", "Blood pressure (hypertension)", "CBC (bone marrow suppression rare)", "Washout with cholestyramine if pregnancy needed (very slow elimination - up to 2 years)"]
        },
        "guideline_tags": [
            "FDA Black Box Warning - Teratogenicity (severe birth defects)",
            "FDA Black Box Warning - Hepatotoxicity (severe)",
            "ACR Guidelines - Rheumatoid Arthritis",
            "ACR Guidelines - Psoriatic Arthritis"
        ],
    },
}
