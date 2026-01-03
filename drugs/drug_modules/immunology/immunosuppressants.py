"""
Immunosuppressants (Thuốc ức chế miễn dịch)
"""

IMMUNOSUPPRESSANTS_DRUGS = {
    "Tacrolimus": {
        "group": "Immunology - Calcineurin Inhibitor",
        "vietnamese_name": "Tacrolimus, FK506",
        "brand_names": {
            "common": ["Prograf", "Advagraf"],
            "vietnam": ["Prograf", "Tacrolimus", "Advagraf (tác dụng kéo dài)"]
        },
        "administration": ["PO", "IV", "Topical"],
        "indications": [
            "Dự phòng thải ghép (gan, thận, tim, phổi)",
            "Viêm da cơ địa (Topical - Protopic)",
            "Bệnh tự miễn kháng trị (Lupus, Viêm khớp dạng thấp - off-label)"
        ],
        "dosage": {
            "transplant_maintenance": "0.03-0.05 mg/kg/ngày chia 2 lần (Prograf) hoặc 1 lần (Advagraf). Điều chỉnh theo nồng độ đáy (Trough level).",
            "atopic_dermatitis": "Bôi 0.03-0.1% x 1-2 lần/ngày.",
            "notes": "Khoảng điều trị hẹp (Narrow therapeutic index). Cần theo dõi nồng độ thuốc trong máu (TDM) nghiêm ngặt."
        },
        "side_effects": [
            "Độc tính thận (Nephrotoxicity) - Phổ biến, phụ thuộc liều",
            "Độc tính thần kinh (Run tay, co giật, đau đầu)",
            "Tăng đường huyết (Đái tháo đường sau ghép - NODAT)",
            "Tăng huyết áp",
            "Tăng Kali máu"
        ],
        "interactions": [
            "Thuốc ức chế CYP3A4 (Macrolides, Azole antifungals, Nước bưởi) -> Tăng nồng độ Tacrolimus mạnh -> Ngộ độc.",
            "Thuốc cảm ứng CYP3A4 (Rifampin, Carbamazepine, Phenytoin) -> Giảm nồng độ Tacrolimus -> Thải ghép."
        ],
        "monitoring": ["Nồng độ Tacrolimus máu (Trough)", "Chức năng thận", "Đường huyết", "Kali máu"],
        "references": {
            "primary_sources": [
                "FDA Drug Label - Tacrolimus (Prograf, Advagraf)",
                "UpToDate - Tacrolimus: Drug information",
                "KDIGO Guidelines - Kidney Transplant",
                "AST Guidelines - Solid Organ Transplant"
            ],
            "last_updated": "2025-02-05",
            "evidence_level": "High - FDA approved, extensive clinical experience"
        },
        "risk_flags": {
            "high_alert": True,
            "narrow_therapeutic_index": True,
            "icu_critical_care_only": False,
            "bleeding_risk": None,
            "organ_toxicity": {"renal": "Black Box Warning - Nephrotoxicity (may be irreversible)", "neurological": "Black Box Warning - Neurotoxicity (seizures, encephalopathy)", "metabolic": "Black Box Warning - Post-transplant diabetes mellitus (NODAT)", "oncologic": "Black Box Warning - Increased risk of infection and malignancy", "cardiovascular": "Hypertension, hyperkalemia"},
            "qt_prolongation": False,
            "hepatotoxicity": False,
            "nephrotoxicity": True,
            "requires_monitoring": ["TDM required (trough levels - Black Box Warning, narrow therapeutic index)", "Renal function (creatinine, eGFR - Black Box Warning for nephrotoxicity)", "Neurological status (seizures, encephalopathy - Black Box Warning)", "Blood glucose (Black Box Warning - post-transplant diabetes)", "Blood pressure (hypertension)", "Serum potassium (hyperkalemia)", "Infection signs (Black Box Warning - increased risk)", "Malignancy screening (Black Box Warning - increased risk)", "CYP3A4 interactions (grapefruit juice, macrolides, azole antifungals)"],
            "look_alike_sound_alike": ["Tacrolimus", "Pimecrolimus"]
        },
        "guideline_tags": [
            "FDA Black Box Warning - Nephrotoxicity (may be irreversible)",
            "FDA Black Box Warning - Neurotoxicity (seizures, encephalopathy)",
            "FDA Black Box Warning - Post-transplant Diabetes Mellitus",
            "FDA Black Box Warning - Increased Risk of Infection and Malignancy",
            "KDIGO Guidelines - Kidney Transplant",
            "AST Guidelines - Solid Organ Transplant",
            "WHO Essential Medicines List"
        ],
        "last_updated": "2025-02-18"
    },

    "Cyclosporine": {
        "group": "Immunology - Calcineurin Inhibitor",
        "vietnamese_name": "Cyclosporine, Cyclosporin A",
        "brand_names": {
            "common": ["Neoral", "Sandimmune"],
            "vietnam": ["Neoral (vi nhũ tương)", "Sandimmun"]
        },
        "administration": ["PO", "IV"],
        "indications": [
            "Dự phòng thải ghép tạng",
            "Viêm khớp dạng thấp",
            "Vảy nến nặng",
            "Hội chứng thận hư"
        ],
        "dosage": {
            "transplant": "Khởi đầu 8-12 mg/kg/ngày, giảm dần. Điều chỉnh theo nồng độ đáy.",
            "ra_psoriasis": "2.5-4 mg/kg/ngày chia 2 lần.",
            "notes": "Dạng Neoral (Modified) và Sandimmune (Non-modified) KHÔNG tương đương nhau."
        },
        "side_effects": [
            "Độc tính thận (Nephrotoxicity)",
            "Tăng huyết áp",
            "Phì đại lợi (Gingival hyperplasia)",
            "Rậm lông (Hirsutism)",
            "Tăng lipid máu"
        ],
        "features": {
             "comparison_tacrolimus": "Cyclosporine gây phì đại lợi và rậm lông, Tacrolimus gây rụng tóc và đái tháo đường nhiều hơn."
        },
        "monitoring": ["Nồng độ Cyclosporine máu", "Chức năng thận", "Huyết áp"]
    },

    "Mycophenolate": {
        "group": "Immunology - Antimetabolite",
        "vietnamese_name": "Mycophenolate Mofetil (MMF), CellCept",
        "brand_names": {
            "common": ["CellCept", "Myfortic"],
            "vietnam": ["CellCept 250/500mg", "Myfortic (Mycophenolate Sodium)"]
        },
        "administration": ["PO", "IV"],
        "indications": [
            "Dự phòng thải ghép (kết hợp Tacrolimus/Cyclosporine + Corticoid)",
            "Viêm thận Lupus (Lupus Nephritis)"
        ],
        "contraindications": [
            "Phụ nữ mang thai (Gây quái thai nghiêm trọng - REMS program)"
        ],
        "dosage": {
            "transplant_adult": "1000 mg (CellCept) hoặc 720 mg (Myfortic) x 2 lần/ngày.",
            "lupus_nephritis": "500-1500 mg x 2 lần/ngày.",
            "notes": "Myfortic là dạng bao tan trong ruột, giảm kích ứng dạ dày hơn CellCept."
        },
        "side_effects": [
            "Rối loạn tiêu hóa (Tiêu chảy, nôn) - Rất phổ biến, giới hạn liều dùng",
            "Suy tủy (Giảm bạch cầu, thiếu máu)",
            "Tăng nguy cơ nhiễm trùng (CMV, BK virus)"
        ],
        "mechanism_of_action": "Ức chế IMPDH, ức chế tổng hợp Purine de novo, ức chế chọn lọc tăng sinh tế bào Lympho T và B.",
        "monitoring": ["Công thức máu (CBC)", "Dấu hiệu nhiễm trùng"],
        "references": {
            "primary_sources": [
                "FDA Drug Label - Mycophenolate (CellCept, Myfortic)",
                "UpToDate - Mycophenolate: Drug information",
                "KDIGO Guidelines - Kidney Transplant",
                "ACR Guidelines - Lupus Nephritis"
            ],
            "last_updated": "2025-02-05",
            "evidence_level": "High - FDA approved, extensive clinical experience"
        },
        "risk_flags": {
            "high_alert": True,
            "narrow_therapeutic_index": False,
            "icu_critical_care_only": False,
            "bleeding_risk": None,
            "organ_toxicity": {"teratogenic": "Black Box Warning - Teratogenicity (severe birth defects, REMS program)", "hematologic": "Black Box Warning - Myelosuppression (neutropenia, anemia, thrombocytopenia)", "oncologic": "Black Box Warning - Increased risk of infection and malignancy", "gastrointestinal": "Severe diarrhea, nausea, vomiting (dose-limiting)"},
            "qt_prolongation": False,
            "hepatotoxicity": False,
            "nephrotoxicity": False,
            "requires_monitoring": ["Black Box Warning - Pregnancy test (REMS program, teratogenicity)", "CBC (Black Box Warning - myelosuppression)", "Infection signs (Black Box Warning - increased risk, CMV, BK virus)", "Malignancy screening (Black Box Warning - increased risk)", "GI symptoms (severe diarrhea, nausea, vomiting - dose-limiting)"],
            "look_alike_sound_alike": ["Mycophenolate", "Mycophenolate mofetil"]
        },
        "guideline_tags": [
            "FDA Black Box Warning - Teratogenicity (severe birth defects, REMS program)",
            "FDA Black Box Warning - Myelosuppression (neutropenia, anemia, thrombocytopenia)",
            "FDA Black Box Warning - Increased Risk of Infection and Malignancy",
            "KDIGO Guidelines - Kidney Transplant",
            "ACR Guidelines - Lupus Nephritis",
            "WHO Essential Medicines List"
        ],
        "last_updated": "2025-02-18"
    },

    "Sirolimus": {
        "group": "Immunology - mTOR Inhibitor",
        "vietnamese_name": "Sirolimus, Rapamycin",
        "brand_names": {
            "common": ["Rapamune"],
            "vietnam": ["Rapamune", "Sirolimus"]
        },
        "administration": ["PO", "IV"],
        "indications": [
            "Dự phòng thải ghép thận (kết hợp cyclosporine hoặc thay thế)",
            "Lymphangioleiomyomatosis (LAM)",
            "Bệnh tự miễn kháng trị (off-label)"
        ],
        "contraindications": [
            "Dị ứng sirolimus",
            "Có thai",
            "Cho con bú"
        ],
        "dosage": {
            "transplant_loading": "6mg PO x 1 lần, sau đó 2mg/ngày",
            "transplant_maintenance": "2-5mg/ngày PO, điều chỉnh theo nồng độ đáy (trough level 4-12 ng/ml)",
            "notes": "Khoảng điều trị hẹp (Narrow therapeutic index). Cần theo dõi nồng độ thuốc trong máu (TDM) nghiêm ngặt. Uống cùng thời điểm mỗi ngày."
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "Không đổi",
            "under_30": "Thận trọng, có thể cần giảm liều"
        },
        "side_effects": [
            "Tăng lipid máu (cholesterol, triglyceride) - Phổ biến",
            "Tăng huyết áp",
            "Giảm tiểu cầu, giảm bạch cầu",
            "Viêm phổi (pneumonitis) - Hiếm nhưng nghiêm trọng",
            "Phù ngoại biên",
            "Loét miệng (stomatitis)",
            "Tăng nguy cơ nhiễm trùng và ung thư",
            "Độc tính thận (khi dùng với cyclosporine)",
            "Rối loạn vết thương (wound healing)"
        ],
        "interactions": [
            "Thuốc ức chế CYP3A4 (Ketoconazole, Voriconazole, Clarithromycin, Diltiazem) -> Tăng nồng độ Sirolimus mạnh -> Ngộ độc",
            "Thuốc cảm ứng CYP3A4 (Rifampin, Carbamazepine, Phenytoin) -> Giảm nồng độ Sirolimus -> Thải ghép",
            "Cyclosporine: Tăng độc tính thận (tránh dùng cùng nếu có thể)",
            "Grapefruit juice: Tăng nồng độ Sirolimus"
        ],
        "pregnancy": "C - D (với thải ghép)",
        "mechanism_of_action": "Sirolimus là mTOR (mammalian target of rapamycin) inhibitor, ức chế tín hiệu mTOR, ngăn chặn sự tăng sinh và hoạt hóa tế bào T và B. Khác với calcineurin inhibitors (tacrolimus, cyclosporine), sirolimus không gây độc tính thận trực tiếp nhưng có thể tăng độc tính thận khi dùng với cyclosporine. Sirolimus có tác dụng chống tăng sinh mạnh, ức chế sự phát triển của tế bào ung thư và tế bào miễn dịch.",
        "monitoring": [
            "Nồng độ Sirolimus máu (Trough level) - Mục tiêu 4-12 ng/ml",
            "Chức năng thận (creatinine, eGFR)",
            "Lipid máu (cholesterol, triglyceride) - Tăng lipid phổ biến",
            "Công thức máu (CBC) - Giảm tiểu cầu, bạch cầu",
            "Dấu hiệu viêm phổi (ho, khó thở, sốt) - Pneumonitis hiếm nhưng nghiêm trọng",
            "Dấu hiệu nhiễm trùng",
            "Dấu hiệu ung thư (sàng lọc định kỳ)",
            "Huyết áp"
        ],
        "precautions": [
            "Khoảng điều trị hẹp - Cần theo dõi nồng độ máu nghiêm ngặt (TDM)",
            "Uống cùng thời điểm mỗi ngày (quan trọng cho TDM)",
            "Tránh dùng với cyclosporine nếu có thể (tăng độc tính thận)",
            "Nhiều tương tác thuốc do chuyển hóa qua CYP3A4",
            "Tăng lipid máu phổ biến - Cần điều trị statin nếu cần",
            "Viêm phổi (pneumonitis) - Ngừng ngay nếu có dấu hiệu",
            "Rối loạn vết thương - Thận trọng sau phẫu thuật",
            "Tránh dùng trong thai kỳ (gây dị tật thai nhi)"
        ],
        "pharmacokinetics": {
            "half_life": "57-63 giờ (rất dài)",
            "onset": "Vài ngày đến vài tuần",
            "duration": "24 giờ (uống 1 lần/ngày)",
            "protein_binding": "92%",
            "clearance": "Gan: chuyển hóa qua CYP3A4. Thận: bài tiết một phần. Hấp thu tốt qua đường uống nhưng bị ảnh hưởng bởi thức ăn."
        },
        "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm, tránh ánh sáng. Dạng solution: bảo quản trong tủ lạnh (2-8°C) sau khi mở.",
        "black_box_warnings": "Tăng nguy cơ nhiễm trùng và ung thư. Có thể gây viêm phổi (pneumonitis) nghiêm trọng. Tăng lipid máu phổ biến. Rối loạn vết thương sau phẫu thuật. Chống chỉ định trong thai kỳ.",
        "references": {
            "primary_sources": [
                "FDA Drug Label - Sirolimus (Rapamune)",
                "UpToDate - Sirolimus: Drug information",
                "KDIGO Guidelines - Kidney Transplant",
                "AST Guidelines - Solid Organ Transplant"
            ],
            "last_updated": "2025-02-18",
            "evidence_level": "High - FDA approved, extensive clinical experience"
        },
        "risk_flags": {
            "high_alert": True,
            "narrow_therapeutic_index": True,
            "icu_critical_care_only": False,
            "bleeding_risk": "High (thrombocytopenia)",
            "organ_toxicity": {"pulmonary": "Pneumonitis (rare but serious)", "hematologic": "Bone marrow suppression (thrombocytopenia, leukopenia)", "metabolic": "Hyperlipidemia (common)", "oncologic": "Black Box Warning - Increased risk of infection and malignancy", "renal": "Nephrotoxicity (when used with cyclosporine)", "wound_healing": "Impaired wound healing"},
            "qt_prolongation": False,
            "hepatotoxicity": False,
            "nephrotoxicity": True,
            "requires_monitoring": ["TDM required (trough levels 4-12 ng/ml - Black Box Warning, narrow therapeutic index)", "Pulmonary symptoms (pneumonitis signs - Black Box Warning, rare but serious)", "CBC (Black Box Warning - bone marrow suppression, thrombocytopenia, leukopenia)", "Lipid profile (hyperlipidemia - common)", "Renal function (nephrotoxicity risk, especially with cyclosporine)", "Infection signs (Black Box Warning - increased risk)", "Malignancy screening (Black Box Warning - increased risk)", "Wound healing (impaired wound healing risk)", "CYP3A4 interactions (grapefruit juice, macrolides, azole antifungals)"],
            "look_alike_sound_alike": ["Sirolimus", "Tacrolimus"]
        },
        "guideline_tags": [
            "FDA Black Box Warning - Increased Risk of Infection and Malignancy",
            "FDA Black Box Warning - Pneumonitis (rare but serious)",
            "KDIGO Guidelines - Kidney Transplant",
            "AST Guidelines - Solid Organ Transplant",
            "WHO Essential Medicines List"
        ],
        "last_updated": "2025-02-18"
    },

    "Everolimus": {
        "group": "Immunology - mTOR Inhibitor",
        "vietnamese_name": "Everolimus, Afinitor",
        "brand_names": {
            "common": ["Afinitor", "Zortress"],
            "vietnam": ["Afinitor", "Everolimus", "Zortress"]
        },
        "administration": ["PO"],
        "indications": [
            "Dự phòng thải ghép thận (Zortress)",
            "Ung thư thận tiến triển (Afinitor)",
            "Ung thư vú hormone receptor dương tính (Afinitor)",
            "Ung thư tụy thần kinh nội tiết (Afinitor)",
            "U xơ cứng củ (Tuberous Sclerosis Complex - Afinitor)"
        ],
        "contraindications": [
            "Dị ứng everolimus",
            "Có thai",
            "Cho con bú"
        ],
        "dosage": {
            "transplant_maintenance": "0.75mg PO x 2 lần/ngày (Zortress), điều chỉnh theo nồng độ đáy (trough level 3-8 ng/ml)",
            "oncology": "10mg PO x 1 lần/ngày (Afinitor)",
            "notes": "Khoảng điều trị hẹp (Narrow therapeutic index). Cần theo dõi nồng độ thuốc trong máu (TDM) nghiêm ngặt. Uống cùng thời điểm mỗi ngày."
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "Thận trọng, có thể cần giảm liều",
            "under_30": "Thận trọng, giảm liều"
        },
        "side_effects": [
            "Tăng lipid máu (cholesterol, triglyceride) - Phổ biến",
            "Tăng đường huyết",
            "Giảm tiểu cầu, giảm bạch cầu",
            "Viêm phổi (pneumonitis) - Hiếm nhưng nghiêm trọng",
            "Loét miệng (stomatitis)",
            "Phát ban",
            "Tăng nguy cơ nhiễm trùng và ung thư",
            "Rối loạn vết thương (wound healing)"
        ],
        "interactions": [
            "Thuốc ức chế CYP3A4 (Ketoconazole, Voriconazole, Clarithromycin, Diltiazem) -> Tăng nồng độ Everolimus mạnh -> Ngộ độc",
            "Thuốc cảm ứng CYP3A4 (Rifampin, Carbamazepine, Phenytoin) -> Giảm nồng độ Everolimus -> Thải ghép hoặc giảm hiệu quả",
            "Grapefruit juice: Tăng nồng độ Everolimus"
        ],
        "pregnancy": "D",
        "mechanism_of_action": "Everolimus là mTOR (mammalian target of rapamycin) inhibitor, tương tự sirolimus nhưng có thời gian bán thải ngắn hơn. Ức chế tín hiệu mTOR, ngăn chặn sự tăng sinh và hoạt hóa tế bào T và B. Trong ung thư, everolimus ức chế sự phát triển của tế bào ung thư và tạo mạch máu. Everolimus được sử dụng cả trong ghép tạng (Zortress) và điều trị ung thư (Afinitor).",
        "monitoring": [
            "Nồng độ Everolimus máu (Trough level) - Mục tiêu 3-8 ng/ml (transplant)",
            "Chức năng thận (creatinine, eGFR)",
            "Lipid máu (cholesterol, triglyceride) - Tăng lipid phổ biến",
            "Đường huyết - Tăng đường huyết",
            "Công thức máu (CBC) - Giảm tiểu cầu, bạch cầu",
            "Dấu hiệu viêm phổi (ho, khó thở, sốt) - Pneumonitis hiếm nhưng nghiêm trọng",
            "Dấu hiệu nhiễm trùng",
            "Dấu hiệu ung thư (sàng lọc định kỳ)",
            "Huyết áp"
        ],
        "precautions": [
            "Khoảng điều trị hẹp - Cần theo dõi nồng độ máu nghiêm ngặt (TDM)",
            "Uống cùng thời điểm mỗi ngày (quan trọng cho TDM)",
            "Nhiều tương tác thuốc do chuyển hóa qua CYP3A4",
            "Tăng lipid máu phổ biến - Cần điều trị statin nếu cần",
            "Tăng đường huyết - Theo dõi và điều trị nếu cần",
            "Viêm phổi (pneumonitis) - Ngừng ngay nếu có dấu hiệu",
            "Rối loạn vết thương - Thận trọng sau phẫu thuật",
            "Tránh dùng trong thai kỳ (gây dị tật thai nhi - Category D)"
        ],
        "pharmacokinetics": {
            "half_life": "30 giờ (ngắn hơn sirolimus)",
            "onset": "Vài ngày đến vài tuần",
            "duration": "12 giờ (uống 2 lần/ngày cho transplant)",
            "protein_binding": "74%",
            "clearance": "Gan: chuyển hóa qua CYP3A4. Thận: bài tiết một phần. Hấp thu tốt qua đường uống."
        },
        "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm, tránh ánh sáng.",
        "black_box_warnings": "Tăng nguy cơ nhiễm trùng và ung thư. Có thể gây viêm phổi (pneumonitis) nghiêm trọng. Tăng lipid máu và tăng đường huyết phổ biến. Rối loạn vết thương sau phẫu thuật. Chống chỉ định trong thai kỳ (Category D).",
        "references": {
            "primary_sources": [
                "FDA Drug Label - Everolimus (Afinitor, Zortress)",
                "UpToDate - Everolimus: Drug information",
                "KDIGO Guidelines - Kidney Transplant",
                "NCCN Guidelines - Renal Cell Carcinoma",
                "NCCN Guidelines - Breast Cancer"
            ],
            "last_updated": "2025-02-18",
            "evidence_level": "High - FDA approved, extensive clinical experience"
        },
        "risk_flags": {
            "high_alert": True,
            "narrow_therapeutic_index": True,
            "icu_critical_care_only": False,
            "bleeding_risk": "High (thrombocytopenia)",
            "organ_toxicity": {"pulmonary": "Pneumonitis (rare but serious)", "hematologic": "Bone marrow suppression (thrombocytopenia, leukopenia)", "metabolic": "Hyperlipidemia (common), hyperglycemia (common)", "oncologic": "Black Box Warning - Increased risk of infection and malignancy", "wound_healing": "Impaired wound healing"},
            "qt_prolongation": False,
            "hepatotoxicity": False,
            "nephrotoxicity": False,
            "requires_monitoring": ["TDM required (trough levels 3-8 ng/ml - Black Box Warning, narrow therapeutic index)", "Pulmonary symptoms (pneumonitis signs - Black Box Warning, rare but serious)", "CBC (Black Box Warning - bone marrow suppression, thrombocytopenia, leukopenia)", "Lipid profile (hyperlipidemia - common)", "Blood glucose (hyperglycemia - common)", "Renal function (nephrotoxicity risk)", "Infection signs (Black Box Warning - increased risk)", "Malignancy screening (Black Box Warning - increased risk)", "Wound healing (impaired wound healing risk)", "CYP3A4 interactions (grapefruit juice, macrolides, azole antifungals)"],
            "look_alike_sound_alike": ["Everolimus", "Sirolimus"]
        },
        "guideline_tags": [
            "FDA Black Box Warning - Increased Risk of Infection and Malignancy",
            "FDA Black Box Warning - Pneumonitis (rare but serious)",
            "KDIGO Guidelines - Kidney Transplant",
            "NCCN Guidelines - Renal Cell Carcinoma",
            "NCCN Guidelines - Breast Cancer",
            "WHO Essential Medicines List"
        ],
        "last_updated": "2025-02-18"
    }
}
