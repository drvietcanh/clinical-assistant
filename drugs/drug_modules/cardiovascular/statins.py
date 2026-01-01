"""
Statins - HMG-CoA Reductase Inhibitors (Thuốc hạ Cholesterol)
Thuốc điều trị rối loạn lipid máu, phòng ngừa tim mạch.
"""

STATINS_DRUGS = {
    "Atorvastatin": {
        "group": "Cardiovascular - Statin (Lipid-lowering)",
        "vietnamese_name": "Atorvastatin, Lipitor",
        "brand_names": {
            "common": ["Lipitor"],
            "vietnam": ["Atorvastatin 10/20/40mg", "Lipitor"]
        },
        "administration": ["PO"],
        "indications": [
            "Tăng cholesterol máu (Hypercholesterolemia)",
            "Phòng ngừa tim mạch (Bệnh mạch vành, Đột quỵ)",
            "Sau nhồi máu cơ tim (Post-MI)",
            "Đái tháo đường (Phòng ngừa biến cố tim mạch)"
        ],
        "dosage": {
            "hypercholesterolemia": "Khởi đầu 10-20mg PO x 1 lần/tối. Tối đa 80mg/ngày.",
            "high_intensity": "40-80mg/ngày (giảm LDL ≥50%).",
            "moderate_intensity": "10-20mg/ngày (giảm LDL 30-50%).",
            "notes": "Uống buổi tối (cholesterol tổng hợp nhiều vào ban đêm). Atorvastatin có thể uống bất kỳ lúc nào."
        },
        "side_effects": [
            "Đau cơ (Myalgia) - Phổ biến (~5%)",
            "Viêm cơ (Myositis) - Hiếm",
            "Tan rã cơ (Rhabdomyolysis) - Hiếm nhưng nguy hiểm (CK ↑↑↑, suy thận)",
            "Tăng men gan (ALT, AST)",
            "Đái tháo đường mới khởi phát (tăng đường huyết nhẹ)",
            "Rối loạn tiêu hóa"
        ],
        "contraindications": [
            "Bệnh gan hoạt động",
            "Có thai (Gây quái thai)",
            "Cho con bú"
        ],
        "interactions": [
            "Fibrate (Gemfibrozil): Tăng nguy cơ tan rã cơ (tránh dùng chung).",
            "Azole antifungals, Macrolide: Tăng nồng độ statin.",
            "Warfarin: Tăng INR.",
            "Grapefruit juice: Tăng nồng độ statin (tránh uống)."
        ],
        "mechanism_of_action": "Ức chế HMG-CoA reductase (enzyme giới hạn tốc độ tổng hợp cholesterol) → Giảm cholesterol máu (LDL ↓30-50%, HDL ↑5-10%). Ổn định mảng xơ vữa, chống viêm.",
        "monitoring": [
            "Lipid profile (LDL, HDL, Triglyceride) - Sau 4-12 tuần điều trị",
            "Men gan (ALT, AST) - Trước điều trị, sau đó nếu có triệu chứng",
            "CK (Creatine Kinase) - Nếu có đau cơ",
            "Đường huyết"
        ],
        "precautions": [
            "Ngừng thuốc nếu đau cơ nặng (nghi ngờ tan rã cơ)",
            "Kiểm tra CK nếu đau cơ (CK >10x bình thường → Ngừng thuốc)",
            "Tránh thai - Gây quái thai",
            "Tránh grapefruit juice",
            "Thận trọng khi dùng chung với Fibrate"
        ],
        "black_box_warnings": "Gây quái thai. Chống chỉ định ở thai kỳ và cho con bú.",
        "risk_flags": {
            "high_alert": False,
            "narrow_therapeutic_index": False,
            "bleeding_risk": False,
            "organ_toxicity": ["Hepatotoxicity", "Myopathy/Rhabdomyolysis"],
            "requires_monitoring": ["Liver function tests (ALT/AST)", "Creatine Kinase (if symptomatic)", "Lipid profile"]
        },
        "guideline_tags": [
            "ACC/AHA 2018 Cholesterol Guidelines",
            "ESC/EAS Guidelines for Dyslipidaemias 2019"
        ]
    },

    "Simvastatin": {
        "group": "Cardiovascular - Statin",
        "vietnamese_name": "Simvastatin, Zocor",
        "brand_names": {
            "common": ["Zocor"],
            "vietnam": ["Simvastatin 10/20/40mg"]
        },
        "administration": ["PO"],
        "indications": [
            "Tương tự Atorvastatin"
        ],
        "dosage": {
            "hypercholesterolemia": "Khởi đầu 10-20mg PO x 1 lần/tối. Tối đa 40mg/ngày (80mg không khuyến cáo do nguy cơ tan rã cơ).",
            "notes": "PHẢI uống buổi tối. Tương tác thuốc nhiều hơn Atorvastatin."
        },
        "side_effects": [
            "Tương tự Atorvastatin",
            "Nguy cơ tan rã cơ cao hơn (đặc biệt liều 80mg)"
        ],
        "interactions": [
            "Tương tác nhiều hơn Atorvastatin (chuyển hóa qua CYP3A4)",
            "Amiodarone: Giới hạn Simvastatin ≤20mg/ngày.",
            "Diltiazem, Verapamil: Giới hạn ≤10mg/ngày."
        ],
        "precautions": [
            "Tương tự Atorvastatin",
            "Liều 80mg KHÔNG khuyến cáo (nguy cơ tan rã cơ cao)",
            "Tương tác thuốc nhiều - Thận trọng"
        ],
        "risk_flags": {
            "high_alert": False,
            "narrow_therapeutic_index": False,
            "bleeding_risk": False,
            "organ_toxicity": ["Hepatotoxicity", "Myopathy/Rhabdomyolysis (High risk with 80mg)"],
            "requires_monitoring": ["Liver function tests (ALT/AST)", "Creatine Kinase (if symptomatic)", "Lipid profile"]
        },
        "guideline_tags": [
            "ACC/AHA 2018 Cholesterol Guidelines",
            "FDA Drug Safety Communication - Simvastatin 80mg"
        ]
    },

    "Rosuvastatin": {
        "group": "Cardiovascular - Statin",
        "vietnamese_name": "Rosuvastatin, Crestor",
        "brand_names": {
            "common": ["Crestor"],
            "vietnam": ["Rosuvastatin 5/10/20mg", "Crestor"]
        },
        "administration": ["PO"],
        "indications": [
            "Tương tự Atorvastatin"
        ],
        "dosage": {
            "hypercholesterolemia": "Khởi đầu 5-10mg PO x 1 lần/ngày. Tối đa 40mg/ngày.",
            "high_intensity": "20-40mg/ngày.",
            "notes": "Statin mạnh nhất. Có thể uống bất kỳ lúc nào."
        },
        "side_effects": [
            "Tương tự Atorvastatin"
        ],
        "mechanism_of_action": "Statin mạnh nhất. Giảm LDL hiệu quả nhất. Tương tác thuốc ít hơn Simvastatin.",
        "risk_flags": {
            "high_alert": False,
            "narrow_therapeutic_index": False,
            "bleeding_risk": False,
            "organ_toxicity": ["Hepatotoxicity", "Myopathy/Rhabdomyolysis", "Renal (proteinuria with high dose)"],
            "requires_monitoring": ["Liver function tests (ALT/AST)", "Creatine Kinase (if symptomatic)", "Lipid profile", "Renal function (with 40mg dose)"]
        },
        "guideline_tags": [
            "ACC/AHA 2018 Cholesterol Guidelines",
            "ESC/EAS Guidelines for Dyslipidaemias 2019"
        ]
    },

    "Pravastatin": {
        "group": "Cardiovascular - Statin",
        "vietnamese_name": "Pravastatin, Pravachol",
        "brand_names": {
            "common": ["Pravachol"],
            "vietnam": ["Pravastatin 10/20/40mg"]
        },
        "administration": ["PO"],
        "indications": [
            "Tương tự Atorvastatin"
        ],
        "dosage": {
            "hypercholesterolemia": "10-40mg PO x 1 lần/tối."
        },
        "side_effects": [
            "Tương tự Atorvastatin nhưng ít hơn"
        ],
        "mechanism_of_action": "Statin ít tương tác thuốc nhất (không chuyển hóa qua CYP450). An toàn hơn ở bệnh nhân dùng nhiều thuốc.",
        "risk_flags": {
            "high_alert": False,
            "narrow_therapeutic_index": False,
            "bleeding_risk": False,
            "organ_toxicity": ["Hepatotoxicity", "Myopathy/Rhabdomyolysis"],
            "requires_monitoring": ["Liver function tests (ALT/AST)", "Creatine Kinase (if symptomatic)", "Lipid profile"]
        },
        "guideline_tags": [
            "ACC/AHA 2018 Cholesterol Guidelines"
        ]
    }
}
