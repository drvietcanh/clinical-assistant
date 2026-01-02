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
        "pharmacokinetics": {
            "absorption": "Hấp thu nhanh qua đường uống (Tmax 1-2 giờ). Bioavailability thấp (~14%) do chuyển hóa qua gan lần đầu.",
            "distribution": "Gắn kết protein huyết tương cao (>98%).",
            "metabolism": "Chuyển hóa mạnh qua gan bởi CYP3A4 thành các chất chuyển hóa có hoạt tính.",
            "excretion": "Chủ yếu qua mật (>98%) và phân. Dưới 2% qua nước tiểu.",
            "half_life": "~14 giờ (hoạt tính ức chế HMG-CoA reductase kéo dài 20-30 giờ do chất chuyển hóa)."
        },
        "storage": "Bảo quản ở nhiệt độ phòng (20-25°C). Tránh ẩm.",
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
            "Tương tác thuốc nhiều - Thận trọng",
            "Tránh dùng lượng lớn nước ép bưởi chùm (>1 lít/ngày)"
        ],
        "mechanism_of_action": "Prodrug (tiền chất) thủy phân thành dạng acid beta-hydroxy có hoạt tính. Ức chế cạnh tranh HMG-CoA reductase → Giảm tổng hợp cholesterol → Tăng thụ thể LDL → Tăng thải trừ LDL.",
        "monitoring": [
            "Lipid profile (sau 4 tuần)",
            "Liver function (ALT/AST)",
            "CK (nếu đau cơ)"
        ],
        "black_box_warnings": "Không khuyến cáo liều 80mg trừ khi bệnh nhân đã ổn định với liều này trên 12 tháng mà không có bệnh cơ. Nguy cơ bệnh cơ và tiêu cơ vân tăng cao.",
        "pharmacokinetics": {
            "absorption": "Hấp thu tốt (~85%), nhưng bioavailability thấp (<5%) do chuyển hóa qua gan lần đầu.",
            "distribution": "Gắn kết protein huyết tương cao (~95%). Qua được hàng rào máu não.",
            "metabolism": "Chuyển hóa mạnh qua gan bởi CYP3A4.",
            "excretion": "Chủ yếu qua phân (60%) và nước tiểu (13%).",
            "half_life": "~3 giờ (ngắn)."
        },
        "storage": "Bảo quản ở 5-30°C. Tránh ánh sáng.",
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
            "Tăng cholesterol máu (Hypercholesterolemia)",
            "Phòng ngừa biến cố tim mạch (Bệnh mạch vành, Đột quỵ)",
            "Hội chứng chuyển hóa"
        ],
        "dosage": {
            "hypercholesterolemia": "Khởi đầu 5-10mg PO x 1 lần/ngày. Tối đa 40mg/ngày.",
            "high_intensity": "20-40mg/ngày.",
            "notes": "Statin mạnh nhất. Có thể uống bất kỳ lúc nào. Uống với hoặc không thức ăn."
        },
        "side_effects": [
            "Đau cơ (Myalgia) - Phổ biến",
            "Viêm cơ (Myositis) - Hiếm",
            "Tan rã cơ (Rhabdomyolysis) - Hiếm nhưng nguy hiểm",
            "Tăng men gan (ALT, AST)",
            "Tiểu đường mới khởi phát (nguy cơ tăng nhẹ)",
            "Protein niệu, tiểu máu (với liều cao 40mg)"
        ],
        "mechanism_of_action": "Statin mạnh nhất. Ức chế HMG-CoA reductase (enzyme giới hạn tốc độ tổng hợp cholesterol) → Giảm cholesterol máu (LDL ↓45-63%). Tác dụng chống viêm và ổn định mảng xơ vữa (pleiotropic effects).",
        "monitoring": [
            "Lipid profile (LDL, HDL, Triglyceride) - Sau 4-12 tuần điều trị",
            "Men gan (ALT, AST) - Trước điều trị, sau đó nếu có triệu chứng",
            "CK (Creatine Kinase) - Nếu có đau cơ",
            "Protein niệu (với liều 40mg)",
            "Đường huyết"
        ],
        "precautions": [
            "Thận trọng ở bệnh nhân châu Á (cân nhắc khởi đầu 5mg)",
            "Nguy cơ protein niệu và tiểu máu với liều 40mg",
            "Thận trọng suy thận nặng (ClCr <30 mL/min) - Khởi đầu 5mg",
            "Ngừng ngay nếu CK >10x ULN hoặc nghi ngờ tan rã cơ",
            "Tránh thai - Gây quái thai"
        ],
        "black_box_warnings": "Nguy cơ tiêu cơ vân (rhabdomyolysis), có thể gây suy thận cấp. Chống chỉ định trong thai kỳ (Category X).",
        "pharmacokinetics": {
            "absorption": "Bioavailability ~20%. Tmax 3-5 giờ. Thức ăn giảm nhẹ tốc độ hấp thu.",
            "distribution": "Gắn kết protein ~88%. Phân bố chủ yếu ở gan.",
            "metabolism": "Chuyển hóa ít (~10%) qua CYP2C9 (ít tương tác CYP3A4 hơn các statin khác).",
            "excretion": "Chủ yếu qua phân (90%) dạng không đổi; 10% qua nước tiểu.",
            "half_life": "~19 giờ (dài, cho phép dùng bất kỳ lúc nào)."
        },
        "storage": "Bảo quản  ở 20-25°C. Tránh ẩm.",
        "risk_flags": {
            "high_alert": False,
            "narrow_therapeutic_index": False,
            "bleeding_risk": False,
            "organ_toxicity": ["Hepatotoxicity", "Myopathy/Rhabdomyolysis", "Renal (proteinuria with high dose)"],
            "requires_monitoring": ["Liver function tests (ALT/AST)", "Creatine Kinase (if symptomatic)", "Lipid profile", "Renal function (with 40mg dose)"]
        },
        "guideline_tags": [
            "ACC/AHA 2018 Cholesterol Guidelines",
            "ESC/EAS Guidelines for Dyslipidaemias 2019",
            "JUPITER Study"
        ],
        "hepatic_adjustment": {
            "mild": "Không đổi liều. Theo dõi men gan.",
            "moderate": "Thận trọng. Giảm liều.",
            "severe": "CHỐNG CHỈ ĐỊNH.",
            "notes": "Suy gan làm tăng nồng độ rosuvastatin."
        },
        "drug_interactions": {
            "major": [
                {
                    "drug": "Cyclosporine",
                    "mechanism": "Ức chế OATP1B1, tăng nồng độ rosuvastatin 7 lần",
                    "effect": "Nguy cơ tiêu cơ vân nghiêm trọng",
                    "management": "Giới hạn liều rosuvastatin 5mg/ngày."
                },
                {
                    "drug": "Gemfibrozil",
                    "mechanism": "Tăng nồng độ rosuvastatin 2 lần",
                    "effect": "Tăng nguy cơ tiêu cơ vân",
                    "management": "Tránh dùng chung. Nếu cần, giới hạn rosuvastatin 10mg/ngày."
                }
            ],
            "moderate": [
                {
                    "drug": "Warfarin",
                    "effect": "Tăng INR",
                    "management": "Theo dõi INR."
                },
                {
                    "drug": "Thuốc kháng acid (Antacids)",
                    "effect": "Giảm hấp thu rosuvastatin",
                    "management": "Uống cách nhau 2 giờ."
                }
            ]
        },
        "overdose_management": {
            "symptoms": ["Tiêu cơ vân", "Đau cơ", "Suy thận cấp"],
            "treatment": [
                "Ngừng thuốc",
                "Truyền dịch tích cực",
                "Theo dõi CK và chức năng thận"
            ]
        }
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
        "monitoring": [
            "Lipid profile",
            "Liver function"
        ],
        "precautions": [
            "Thận trọng suy thận (giảm liều)",
            "Tiền sử bệnh gan"
        ],
        "black_box_warnings": None,
        "pharmacokinetics": {
            "absorption": "Hấp thu nhanh (~35% hấp thu, bioavailability ~17%). Tmax 1-1.5 giờ.",
            "distribution": "Gắn kết protein ~50% (thấp nhất trong nhóm statin). Ít qua hàng rào máu não (ưa nước).",
            "metabolism": "Không chuyển hóa qua CYP450. Chuyển hóa ở dạ dày và gan.",
            "excretion": "Nước tiểu (20%) và phân (70%).",
            "half_life": "~1.5-2 giờ (hoạt tính), bán thải ~77 giờ."
        },
        "storage": "Bảo quản ở 25°C. Tránh ánh sáng và ẩm.",
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
