"""
Mood Stabilizers
"""

MOOD_STABILIZERS_DRUGS = {
    "Lithium":     {
        "group": "Psychiatry - Mood Stabilizer",
        "vietnamese_name": "Lithium carbonate, LiCO3",
        "brand_names": {
            "common": [
                "Lithobid",
                "Eskalith"
    ],
            "vietnam": [
                "Lithium Carbonate"
    ],
        },
        "administration": [
            "PO"
    ],
        "indications": [
            "Rối loạn lưỡng cực (Cơn mania cấp & Dự phòng)",
            "Chống trầm cảm bổ trợ (Augmentation)",
            "Giảm nguy cơ tự sát"
    ],
        "contraindications": {
            "absolute": [
                "Suy thận nặng",
                "Bệnh tim mạch nặng",
                "Mất nước/Rối loạn điện giải nặng",
                "Hạ Natri máu"
    ],
            "relative": [
                "Bệnh vảy nến (làm nặng thêm)",
                "Suy giáp (cần theo dõi)"
    ],
        },
        "dosage": {
            "adult_bipolar_acute": "1800 mg/ngày (chia liều). Đích nồng độ máu: 0.8-1.2 mEq/L.",
            "adult_bipolar_maintenance": "900-1200 mg/ngày. Đích nồng độ máu: 0.6-1.0 mEq/L.",
            "notes": "Khoảng điều trị HẸP. Bắt buộc theo dõi nồng độ thuốc trong máu (TDM).",
        },
        "renal_adjustment": {
            "crcl_10_50": "Giảm 50-75% liều.",
            "crcl_under_10": "Chống chỉ định.",
            "notes": "Lithium thải trừ presque hoàn toàn qua thận.",
        },
        "hepatic_adjustment": {
            "mild": "",
            "moderate": "",
            "severe": "",
            "notes": "Không cần chỉnh liều (không chuyển hóa qua gan).",
        },
        "side_effects": [
            "Run tay (Tremor) - Rất thường gặp",
            "Đái tháo nhạt do thận (Polyuria/Polydipsia)",
            "Suy giáp, Bướu cổ",
            "Tăng cân",
            "Buồn nôn, tiêu chảy"
    ],
        "interactions": [
            "NSAIDs (Ibuprofen, Naproxen) -> Tăng nồng độ Lithium (Ngộ độc).",
            "ACE Inhibitors / ARBs -> Tăng nồng độ Lithium.",
            "Thuốc lợi tiểu (Thiazides, Furosemide) -> Tăng nồng độ Lithium.",
            "Caffeine -> Giảm nồng độ Lithium."
    ],
        "pregnancy_lactation": {
            "fda_category": "D",
            "pregnancy_details": "Nguy cơ dị tật tim (Ebstein's anomaly). Cân nhắc lợi ích/nguy cơ.",
            "lactation": {
                "safety": "Unsafe",
                "details": "Bài tiết nhiều vào sữa. Chống chỉ định hoặc theo dõi sát.",
                "recommendation": "",
            },
        },
        "pharmacokinetics": {
            "half_life": "18-24 giờ (kéo dài ở người già/suy thận)",
            "excretion": "Thận (95%)",
        },
        "monitoring": [
            "Nồng độ Lithium (TDM): 5-7 ngày sau khi đổi liều. Định kỳ 3-6 tháng.",
            "Chức năng thận (Creatinine, Bun)",
            "Tuyến giáp (TSH, T4)",
            "Điện giải đồ (Na+)"
    ],
        "black_box_warnings": """Độc tính Lithium liên quan chặt chẽ đến nồng độ huyết thanh. Ngộ độc có thể xảy ra ở liều gần với liều điều trị.""",
        "risk_flags": {
            "high_alert": True,
            "narrow_therapeutic_index": True,
            "bleeding_risk": False,
            "organ_toxicity": ["renal", "endocrine", "neurological"],
            "qt_prolongation": False,
            "hepatotoxicity": False,
            "nephrotoxicity": True,
            "requires_monitoring": ["Lithium level (TDM - CRITICAL)", "Creatinine", "BUN", "TSH", "T4", "Sodium"]
        },
        "guideline_tags": [
            "FDA Black Box Warning - Lithium Toxicity (Narrow Therapeutic Index)",
            "ISMP High Alert Medications",
            "APA Guidelines - Bipolar Disorder",
            "WHO Essential Medicines List"
        ],
        "pregnancy": "",
        "mechanism_of_action": "",
        "precautions": [],
        "storage": "",
        "drug_interactions": {
            "major": [],
            "moderate": [],
            "minor": [],
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
    "Valproic Acid":     {
        "group": "Psychiatry - Mood Stabilizer / Anticonvulsant",
        "vietnamese_name": "Valproic acid, Sodium Valproate, Depakine",
        "brand_names": {
            "common": [
                "Depakote",
                "Depakene"
    ],
            "vietnam": [
                "Depakine",
                "Encorate"
    ],
        },
        "administration": [
            "PO",
            "IV"
    ],
        "indications": [
            "Rối loạn lưỡng cực (Mania)",
            "Động kinh (Cục bộ, Toàn thể, Vắng ý thức)",
            "Dự phòng đau đầu Migraine"
    ],
        "dosage": {
            "adult_mania": "Khởi đầu 10-15 mg/kg/ngày. Tăng nhanh đến hiệu quả lâm sàng. Tối đa 60 mg/kg/ngày.",
            "target_level": "50-100 mcg/mL (Động kinh), 50-125 mcg/mL (Mania).",
        },
        "renal_adjustment": {
            "normal": "Không đổi",
        },
        "hepatic_adjustment": {
            "mild": "",
            "moderate": "",
            "severe": "",
            "notes": "CHỐNG CHỈ ĐỊNH ở bệnh gan nặng / suy gan cấp.",
        },
        "side_effects": [
            "Rụng tóc (thường hồi phục)",
            "Tăng cân",
            "Run tay",
            "Giảm tiểu cầu",
            "Tăng NH3 máu (Hyperammonemia) -> Bệnh não"
    ],
        "interactions": [
            "Lamotrigine: Valproate ức chế chuyển hóa Lamotrigine -> Tăng nguy cơ dị ứng da nặng (SJS/TEN).",
            "Carbamazepine/Phenytoin: Tương tác phức tạp."
    ],
        "pregnancy_lactation": {
            "fda_category": "D (X nếu dùng Migraine)",
            "pregnancy_details": "Gây dị tật ống thần kinh (Spina bifida) & Giảm IQ trẻ. TRÁNH DÙNG nếu có thể.",
            "lactation": {
                "safety": "Compatible",
                "details": "An toàn hơn so với thai kỳ.",
                "recommendation": "",
            },
        },
        "monitoring": [
            "Chức năng gan (AST/ALT) - Bắt buộc",
            "Công thức máu (Tiểu cầu)",
            "Nồng độ Valproate",
            "NH3 máu (nếu thay đổi ý thức)"
    ],
        "black_box_warnings": "Độc tính gan (tử vong); Viêm tụy cấp (tử vong); Quái thai (Dị tật bẩm sinh).",
        "risk_flags": {
            "high_alert": True,
            "narrow_therapeutic_index": False,
            "bleeding_risk": False,
            "organ_toxicity": ["hepatic", "pancreatic", "hematologic"],
            "qt_prolongation": False,
            "hepatotoxicity": True,
            "nephrotoxicity": False,
            "requires_monitoring": ["Liver function (AST/ALT - CRITICAL)", "CBC (platelets)", "Valproate level", "NH3 (if altered mental status)"]
        },
        "guideline_tags": [
            "FDA Black Box Warning - Hepatotoxicity (Fatal)",
            "FDA Black Box Warning - Acute Pancreatitis (Fatal)",
            "FDA Black Box Warning - Teratogenicity",
            "ISMP High Alert Medications",
            "APA Guidelines - Bipolar Disorder",
            "AAN Guidelines - Epilepsy Treatment"
        ],
        "contraindications": [],
        "pregnancy": "",
        "mechanism_of_action": "",
        "precautions": [],
        "pharmacokinetics": {
        },
        "storage": "",
        "drug_interactions": {
            "major": [],
            "moderate": [],
            "minor": [],
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
    "Carbamazepine":     {
        "group": "Psychiatry - Mood Stabilizer / Anticonvulsant",
        "vietnamese_name": "Carbamazepine, Tegretol",
        "brand_names": {
            "vietnam": [
                "Tegretol",
                "Carbatol"
    ],
        },
        "administration": [
            "PO"
    ],
        "indications": [
            "Rối loạn lưỡng cực (Mania cấp & duy trì)",
            "Động kinh (Cục bộ)",
            "Đau dây thần kinh V (Trigeminal Neuralgia)"
    ],
        "dosage": {
            "adult_bipolar": "200 mg x 2 lần/ngày -> Tăng mỗi tuần 200mg. Đích 800-1200 mg/ngày.",
            "target_level": "4-12 mcg/mL.",
        },
        "side_effects": [
            "Mẩn ngứa/Dị ứng da (Nguy cơ SJS/TEN - HLA-B*1502)",
            "Giảm bạch cầu, Suy tủy",
            "Hạ Natri máu (SIADH)",
            "Rối loạn tiền đình (Chóng mặt, nhìn đôi)"
    ],
        "interactions": [
            "Là chất CẢM ỨNG MẠNH CYP3A4 -> Làm GIẢM nồng độ rất nhiều thuốc khác (Thuốc tránh thai, Warfarin, Antipsychotics...)",
            "Tự cảm ứng chuyển hóa chính nó (Auto-induction): Nồng độ giảm sau vài tuần điều trị."
    ],
        "monitoring": [
            "HLA-B*1502 (người Á Đông trước khi dùng) -> SJS risk.",
            "Công thức máu, Gan, Natri máu."
    ],
        "black_box_warnings": "Phản ứng da nghiêm trọng (SJS/TEN), Suy tủy xương (Aplastic Anemia/Agranulocytosis).",
        "contraindications": [],
        "pregnancy": "",
        "mechanism_of_action": "",
        "precautions": [],
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
            "icu_critical_care_only": False,
            "bleeding_risk": None,
            "organ_toxicity": {"dermatologic": "Black Box Warning (SJS/TEN - fatal)", "hematologic": "Black Box Warning (aplastic anemia, agranulocytosis)", "hepatic": "Hepatotoxicity", "endocrine": "SIADH (hyponatremia)"},
            "qt_prolongation": False,
            "hepatotoxicity": "Rare but serious",
            "nephrotoxicity": False,
            "requires_monitoring": ["HLA-B*1502 (Asian patients - before starting)", "CBC (aplastic anemia, agranulocytosis - Black Box Warning)", "Liver function", "Sodium (SIADH)", "SJS/TEN signs"],
            "look_alike_sound_alike": ["Carbamazepine", "Oxcarbazepine"]
        },
        "guideline_tags": [
            "FDA Black Box Warning - Stevens-Johnson Syndrome/TEN",
            "FDA Black Box Warning - Aplastic Anemia/Agranulocytosis",
            "APA Guidelines - Bipolar Disorder",
            "AAN Guidelines - Epilepsy Treatment",
            "ILAE Guidelines - Antiepileptic Drugs"
        ],
        "last_updated": "2025-02-18",
    },
    "Lamotrigine":     {
        "group": "Psychiatry - Mood Stabilizer / Anticonvulsant",
        "vietnamese_name": "Lamotrigine, Lamictal",
        "administration": [
            "PO"
    ],
        "indications": [
            "Rối loạn lưỡng cực (Dự phòng trầm cảm)",
            "Động kinh"
    ],
        "dosage": {
            "adult_bipolar": "Titration rất chậm: Tuần 1-2: 25mg/ngày. Tuần 3-4: 50mg/ngày. Đích 200mg/ngày.",
            "with_valproate": "Dùng 1/2 liều (Bắt đầu 25mg mỗi 2 ngày).",
            "with_carbamazepine": "Dùng gấp đôi liều.",
        },
        "side_effects": [
            "Phát ban da lành tính (10%)",
            "Hội chứng Stevens-Johnson (SJS) - Hiếm nhưng nguy hiểm"
    ],
        "black_box_warnings": "Phát ban da nghiêm trọng (SJS/TEN), cần ngừng thuốc ngay khi có dấu hiệu phát ban đầu tiên.",
        "contraindications": [],
        "interactions": [],
        "pregnancy": "",
        "mechanism_of_action": "",
        "monitoring": [],
        "precautions": [],
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
            "icu_critical_care_only": False,
            "bleeding_risk": None,
            "organ_toxicity": {"dermatologic": "Black Box Warning (SJS/TEN - fatal, requires slow titration)"},
            "qt_prolongation": False,
            "hepatotoxicity": False,
            "nephrotoxicity": False,
            "requires_monitoring": ["SJS/TEN signs (Black Box Warning - stop immediately if rash)", "Slow titration required (especially with valproate)"],
            "look_alike_sound_alike": ["Lamotrigine", "Lamivudine"]
        },
        "guideline_tags": [
            "FDA Black Box Warning - Stevens-Johnson Syndrome/TEN",
            "APA Guidelines - Bipolar Disorder",
            "AAN Guidelines - Epilepsy Treatment",
            "ILAE Guidelines - Antiepileptic Drugs"
        ],
        "last_updated": "2025-02-18",
    },
}
