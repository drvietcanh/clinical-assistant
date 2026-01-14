"""
Statins - HMG-CoA Reductase Inhibitors (Thuốc hạ Cholesterol)
Thuốc điều trị rối loạn lipid máu, phòng ngừa tim mạch.
"""

STATINS_DRUGS = {
    "Atorvastatin":     {
        "group": "Cardiovascular - Statin (Lipid-lowering)",
        "vietnamese_name": "Atorvastatin, Lipitor",
        "brand_names": {
            "common": [
                "Lipitor"
    ],
            "vietnam": [
                "Atorvastatin 10/20/40mg",
                "Lipitor"
    ],
        },
        "administration": [
            "PO"
    ],
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
            "notes": "Uống buổi tối (cholesterol tổng hợp nhiều vào ban đêm). Atorvastatin có thể uống bất kỳ lúc nào.",
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
        "contraindications_detail": {
            "tuyệt_đối": [
                "Bệnh gan hoạt động (active liver disease) - tăng men gan kéo dài, viêm gan",
                "Có thai (pregnancy) - FDA category X, gây dị tật thai nhi",
                "Cho con bú (lactation) - bài tiết vào sữa mẹ",
                "Tiêu cơ vân đang hoạt động (active myopathy/rhabdomyolysis)",
                "Dị ứng với atorvastatin hoặc bất kỳ thành phần nào"
            ],
            "tương_đối": [
                "Suy thận - thận trọng, theo dõi chức năng thận",
                "Suy gan - thận trọng, theo dõi men gan thường xuyên",
                "Uống rượu nhiều - tăng nguy cơ viêm gan",
                "Người cao tuổi - tăng nguy cơ đau cơ, tiêu cơ vân",
                "Đái tháo đường - statins có thể tăng đường huyết nhẹ",
                "Bệnh tuyến giáp - tăng nguy cơ đau cơ",
                "Dùng cùng thuốc ức chế CYP3A4 - tăng nồng độ atorvastatin",
                "Dùng grapefruit juice - tăng nồng độ atorvastatin"
            ]
        },
        "interactions": [
            "Fibrate (Gemfibrozil): Tăng nguy cơ tan rã cơ (tránh dùng chung).",
            "Azole antifungals, Macrolide: Tăng nồng độ statin.",
            "Warfarin: Tăng INR.",
            "Grapefruit juice: Tăng nồng độ statin (tránh uống)."
    ],
        "mechanism_of_action": """Ức chế HMG-CoA reductase (enzyme giới hạn tốc độ tổng hợp cholesterol) → Giảm cholesterol máu (LDL ↓30-50%, HDL ↑5-10%). Ổn định mảng xơ vữa, chống viêm.""",
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
            "absorption": """Hấp thu nhanh qua đường uống (Tmax 1-2 giờ). Bioavailability thấp (~14%) do chuyển hóa qua gan lần đầu.""",
            "distribution": "Gắn kết protein huyết tương cao (>98%).",
            "metabolism": "Chuyển hóa mạnh qua gan bởi CYP3A4 thành các chất chuyển hóa có hoạt tính.",
            "excretion": "Chủ yếu qua mật (>98%) và phân. Dưới 2% qua nước tiểu.",
            "half_life": "~14 giờ (hoạt tính ức chế HMG-CoA reductase kéo dài 20-30 giờ do chất chuyển hóa).",
        },
        "storage": "Bảo quản ở nhiệt độ phòng (20-25°C). Tránh ẩm.",
        "risk_flags": {
            "high_alert": False,
            "narrow_therapeutic_index": False,
            "bleeding_risk": False,
            "organ_toxicity": [
                "Hepatotoxicity",
                "Myopathy/Rhabdomyolysis"
    ],
            "requires_monitoring": [
                "Liver function tests (ALT/AST)",
                "Creatine Kinase (if symptomatic)",
                "Lipid profile"
    ],
        },
        "guideline_tags": [
            "ACC/AHA 2018 Cholesterol Guidelines",
            "ESC/EAS Guidelines for Dyslipidaemias 2019"
    ],
        "pregnancy_lactation": {
            "fda_category": "X",
            "pregnancy_details": """CHỐNG CHỈ ĐỊNH. Statin can thiệp vào tổng hợp cholesterol cần thiết cho sự phát triển của thai nhi. Ngưng thuốc ngay lập tức nếu phát hiện có thai.""",
            "lactation": {
                "safety": "Avoid",
                "details": "Có khả năng bài tiết vào sữa mẹ và gây ảnh hưởng đến chuyển hóa lipid của trẻ.",
                "recommendation": "Không sử dụng. Ngưng cho con bú hoặc ngưng thuốc.",
            },
        },
        "pregnancy": "X - Chống chỉ định",
        "drug_interactions": {
            "major": [
                {
                    "drug": "Gemfibrozil",
                    "mechanism": "Hiệp đồng độc cơ, tăng nguy cơ tiêu cơ vân",
                    "effect": "Tăng nguy cơ tiêu cơ vân nghiêm trọng",
                    "management": "Tránh dùng chung. Nếu cần hạ triglyceride, cân nhắc fenofibrate."
                },
                {
                    "drug": "Cyclosporine",
                    "mechanism": "Ức chế CYP3A4 và OATP1B1, tăng nồng độ atorvastatin",
                    "effect": "Tăng nguy cơ tiêu cơ vân",
                    "management": "Giới hạn liều atorvastatin 10mg/ngày hoặc tránh dùng."
                },
                {
                    "drug": "Azole antifungals (Ketoconazole, Itraconazole)",
                    "mechanism": "Ức chế CYP3A4 mạnh, tăng nồng độ atorvastatin",
                    "effect": "Tăng nguy cơ độc cơ",
                    "management": "Tránh dùng cùng hoặc giảm liều atorvastatin."
                }
            ],
            "moderate": [
                {
                    "drug": "Macrolide antibiotics (Clarithromycin, Erythromycin)",
                    "mechanism": "Ức chế CYP3A4, tăng nồng độ atorvastatin",
                    "effect": "Tăng nguy cơ độc cơ",
                    "management": "Giảm liều hoặc tạm ngừng atorvastatin trong thời gian dùng kháng sinh."
                },
                {
                    "drug": "Warfarin",
                    "mechanism": "Atorvastatin có thể tăng nhẹ tác dụng chống đông",
                    "effect": "Tăng INR",
                    "management": "Theo dõi INR khi khởi atorvastatin hoặc thay đổi liều."
                },
                {
                    "drug": "Grapefruit juice",
                    "mechanism": "Ức chế CYP3A4, tăng nồng độ atorvastatin",
                    "effect": "Tăng nguy cơ độc cơ",
                    "management": "Tránh uống grapefruit juice khi dùng atorvastatin."
                }
            ],
            "minor": [
                {
                    "drug": "Niacin",
                    "mechanism": "Hiệp đồng độc cơ",
                    "effect": "Tăng nguy cơ đau cơ",
                    "management": "Theo dõi CK và triệu chứng cơ."
                }
            ],
        },
        "hepatic_adjustment": {
            "mild": "Thận trọng, theo dõi men gan",
            "moderate": "Giảm liều hoặc tránh nếu men gan tăng kéo dài",
            "severe": "CHỐNG CHỈ ĐỊNH",
            "notes": "Suy gan làm tăng nồng độ atorvastatin do giảm chuyển hóa qua gan.",
        },
        "overdose_management": {
            "symptoms": [
                "Đau cơ nặng, CK tăng, tiêu cơ vân, tăng men gan"
            ],
            "antidote": "Không có antidote đặc hiệu",
            "treatment": [
                "Ngừng atorvastatin",
                "Truyền dịch tích cực nếu nghi tiêu cơ vân; kiềm hóa nước tiểu nếu cần",
                "Theo dõi CK, men gan, creatinine",
                "Lọc máu nếu suy thận cấp do tiêu cơ vân"
            ],
            "monitoring": "CK, creatinine, AST/ALT, điện giải, lượng nước tiểu",
        },
        "renal_adjustment": {
            "normal": "Không cần chỉnh liều",
            "30_60": "Không cần chỉnh liều. Atorvastatin không thải trừ chủ yếu qua thận.",
            "under_30": "Không cần chỉnh liều. Atorvastatin không thải trừ chủ yếu qua thận.",
            "dialysis": "Không cần chỉnh liều. Atorvastatin không được lọc sạch qua thẩm phân máu.",
            "notes": "Atorvastatin chủ yếu thải trừ qua gan và mật. Không cần điều chỉnh liều ở suy thận."
        },
        "reversal_agents": {
            "available": False,
            "agents": [],
            "notes": "Không có antidote đặc hiệu. Điều trị quá liều chủ yếu là hỗ trợ: ngừng thuốc, điều trị tiêu cơ vân nếu có (truyền dịch, kiềm hóa nước tiểu), theo dõi CK và chức năng thận."
        },
        "administration_instructions": {
            "oral": {
                "with_food": "Có thể uống với hoặc không thức ăn",
                "timing": "Uống 1 lần/ngày, có thể uống bất kỳ lúc nào (khác với simvastatin phải uống buổi tối)"
            }
        },
        "references": {
            "primary_sources": [
                "FDA Drug Label - Lipitor (atorvastatin)",
                "ACC/AHA 2018 Cholesterol Guidelines",
                "ESC/EAS Guidelines for Dyslipidaemias 2019"
            ],
            "last_updated": "2025-02-18",
            "evidence_level": "A - Multiple large RCTs (PROVE-IT, TNT, IDEAL)",
        },
    },
    "Simvastatin":     {
        "group": "Cardiovascular - Statin",
        "vietnamese_name": "Simvastatin, Zocor",
        "brand_names": {
            "common": [
                "Zocor"
    ],
            "vietnam": [
                "Simvastatin 10/20/40mg"
    ],
        },
        "administration": [
            "PO"
    ],
        "indications": [
            "Tương tự Atorvastatin"
    ],
        "dosage": {
            "hypercholesterolemia": "Khởi đầu 10-20mg PO x 1 lần/tối. Tối đa 40mg/ngày (80mg không khuyến cáo do nguy cơ tan rã cơ).",
            "notes": "PHẢI uống buổi tối. Tương tác thuốc nhiều hơn Atorvastatin.",
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
        "mechanism_of_action": """Prodrug (tiền chất) thủy phân thành dạng acid beta-hydroxy có hoạt tính. Ức chế cạnh tranh HMG-CoA reductase → Giảm tổng hợp cholesterol → Tăng thụ thể LDL → Tăng thải trừ LDL.""",
        "monitoring": [
            "Lipid profile (sau 4 tuần)",
            "Liver function (ALT/AST)",
            "CK (nếu đau cơ)"
    ],
        "black_box_warnings": """Không khuyến cáo liều 80mg trừ khi bệnh nhân đã ổn định với liều này trên 12 tháng mà không có bệnh cơ. Nguy cơ bệnh cơ và tiêu cơ vân tăng cao.""",
        "pharmacokinetics": {
            "absorption": "Hấp thu tốt (~85%), nhưng bioavailability thấp (<5%) do chuyển hóa qua gan lần đầu.",
            "distribution": "Gắn kết protein huyết tương cao (~95%). Qua được hàng rào máu não.",
            "metabolism": "Chuyển hóa mạnh qua gan bởi CYP3A4.",
            "excretion": "Chủ yếu qua phân (60%) và nước tiểu (13%).",
            "half_life": "~3 giờ (ngắn).",
        },
        "storage": "Bảo quản ở 5-30°C. Tránh ánh sáng.",
        "risk_flags": {
            "high_alert": False,
            "narrow_therapeutic_index": False,
            "bleeding_risk": False,
            "organ_toxicity": [
                "Hepatotoxicity",
                "Myopathy/Rhabdomyolysis (High risk with 80mg)"
    ],
            "requires_monitoring": [
                "Liver function tests (ALT/AST)",
                "Creatine Kinase (if symptomatic)",
                "Lipid profile"
    ],
        },
        "guideline_tags": [
            "ACC/AHA 2018 Cholesterol Guidelines",
            "FDA Drug Safety Communication - Simvastatin 80mg"
    ],
        "contraindications_detail": {
            "tuyệt_đối": [
                "Bệnh gan hoạt động (active liver disease) - tăng men gan kéo dài, viêm gan",
                "Có thai (pregnancy) - FDA category X, gây dị tật thai nhi",
                "Cho con bú (lactation) - bài tiết vào sữa mẹ",
                "Tiêu cơ vân đang hoạt động (active myopathy/rhabdomyolysis)",
                "Dị ứng với simvastatin hoặc bất kỳ thành phần nào",
                "Dùng cùng cyclosporine, itraconazole, ketoconazole (tăng nguy cơ tiêu cơ vân nghiêm trọng)",
                "Dùng grapefruit juice"
    ],
            "tương_đối": [
                "Suy thận - thận trọng, giảm liều nếu cần",
                "Suy gan - thận trọng, theo dõi men gan thường xuyên",
                "Uống rượu nhiều - tăng nguy cơ viêm gan",
                "Người cao tuổi - tăng nguy cơ đau cơ, tiêu cơ vân",
                "Đái tháo đường - statins có thể tăng đường huyết nhẹ",
                "Bệnh tuyến giáp - tăng nguy cơ đau cơ",
                "Dùng cùng thuốc ức chế CYP3A4 - giảm liều simvastatin",
                "Liều cao (>40mg/ngày) - tăng nguy cơ tiêu cơ vân"
    ],
        },
        "renal_adjustment": {
            "normal": "Không đổi liều",
            "30_60": "Có thể cần giảm liều, theo dõi chức năng thận",
            "under_30": "Giảm liều hoặc tránh dùng nếu có lựa chọn khác",
            "hemodialysis": "Có thể cần bổ sung sau lọc máu (tùy thuốc)",
        },
        "contraindications": [],
        "pregnancy": "X - Chống chỉ định tuyệt đối trong thai kỳ do nguy cơ dị tật bẩm sinh",
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
    "Rosuvastatin":     {
        "group": "Cardiovascular - Statin",
        "vietnamese_name": "Rosuvastatin, Crestor",
        "brand_names": {
            "common": [
                "Crestor"
    ],
            "vietnam": [
                "Rosuvastatin 5/10/20mg",
                "Crestor"
    ],
        },
        "administration": [
            "PO"
    ],
        "indications": [
            "Tăng cholesterol máu (Hypercholesterolemia)",
            "Phòng ngừa biến cố tim mạch (Bệnh mạch vành, Đột quỵ)",
            "Hội chứng chuyển hóa"
    ],
        "dosage": {
            "hypercholesterolemia": "Khởi đầu 5-10mg PO x 1 lần/ngày. Tối đa 40mg/ngày.",
            "high_intensity": "20-40mg/ngày.",
            "notes": "Statin mạnh nhất. Có thể uống bất kỳ lúc nào. Uống với hoặc không thức ăn.",
        },
        "side_effects": [
            "Đau cơ (Myalgia) - Phổ biến",
            "Viêm cơ (Myositis) - Hiếm",
            "Tan rã cơ (Rhabdomyolysis) - Hiếm nhưng nguy hiểm",
            "Tăng men gan (ALT, AST)",
            "Tiểu đường mới khởi phát (nguy cơ tăng nhẹ)",
            "Protein niệu, tiểu máu (với liều cao 40mg)"
    ],
        "mechanism_of_action": """Statin mạnh nhất. Ức chế HMG-CoA reductase (enzyme giới hạn tốc độ tổng hợp cholesterol) → Giảm cholesterol máu (LDL ↓45-63%). Tác dụng chống viêm và ổn định mảng xơ vữa (pleiotropic effects).""",
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
        "black_box_warnings": """Nguy cơ tiêu cơ vân (rhabdomyolysis), có thể gây suy thận cấp. Chống chỉ định trong thai kỳ (Category X).""",
        "pharmacokinetics": {
            "absorption": "Bioavailability ~20%. Tmax 3-5 giờ. Thức ăn giảm nhẹ tốc độ hấp thu.",
            "distribution": "Gắn kết protein ~88%. Phân bố chủ yếu ở gan.",
            "metabolism": "Chuyển hóa ít (~10%) qua CYP2C9 (ít tương tác CYP3A4 hơn các statin khác).",
            "excretion": "Chủ yếu qua phân (90%) dạng không đổi; 10% qua nước tiểu.",
            "half_life": "~19 giờ (dài, cho phép dùng bất kỳ lúc nào).",
        },
        "storage": "Bảo quản  ở 20-25°C. Tránh ẩm.",
        "risk_flags": {
            "high_alert": False,
            "narrow_therapeutic_index": False,
            "bleeding_risk": False,
            "organ_toxicity": [
                "Hepatotoxicity",
                "Myopathy/Rhabdomyolysis",
                "Renal (proteinuria with high dose)"
    ],
            "requires_monitoring": [
                "Liver function tests (ALT/AST)",
                "Creatine Kinase (if symptomatic)",
                "Lipid profile",
                "Renal function (with 40mg dose)"
    ],
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
            "notes": "Suy gan làm tăng nồng độ rosuvastatin.",
        },
        "drug_interactions": {
            "major": [
    {
                    "drug": "Cyclosporine",
                    "mechanism": "Ức chế OATP1B1, tăng nồng độ rosuvastatin 7 lần",
                    "effect": "Nguy cơ tiêu cơ vân nghiêm trọng",
                    "management": "Giới hạn liều rosuvastatin 5mg/ngày.",
                },
    {
                    "drug": "Gemfibrozil",
                    "mechanism": "Tăng nồng độ rosuvastatin 2 lần",
                    "effect": "Tăng nguy cơ tiêu cơ vân",
                    "management": "Tránh dùng chung. Nếu cần, giới hạn rosuvastatin 10mg/ngày.",
                }
                ],
            "moderate": [
    {
                    "drug": "Warfarin",
                    "effect": "Tăng INR",
                    "management": "Theo dõi INR.",
                },
    {
                    "drug": "Thuốc kháng acid (Antacids)",
                    "effect": "Giảm hấp thu rosuvastatin",
                    "management": "Uống cách nhau 2 giờ.",
                }
                ],
            "minor": [],
        },
        "overdose_management": {
            "symptoms": [
                "Tiêu cơ vân",
                "Đau cơ",
                "Suy thận cấp"
    ],
            "antidote": "",
            "treatment": [
                "Ngừng thuốc",
                "Truyền dịch tích cực",
                "Theo dõi CK và chức năng thận"
    ],
            "monitoring": "",
        },
        "contraindications": [
            "Bệnh gan hoạt động",
            "Có thai (Gây quái thai)",
            "Cho con bú"
        ],
        "contraindications_detail": {
            "tuyệt_đối": [
                "Bệnh gan hoạt động (active liver disease) - tăng men gan kéo dài, viêm gan",
                "Có thai (pregnancy) - FDA category X, gây dị tật thai nhi",
                "Cho con bú (lactation) - bài tiết vào sữa mẹ",
                "Tiêu cơ vân đang hoạt động (active myopathy/rhabdomyolysis)",
                "Dị ứng với rosuvastatin hoặc bất kỳ thành phần nào",
                "Dùng cùng cyclosporine (trừ khi liều rosuvastatin ≤5mg/ngày)"
            ],
            "tương_đối": [
                "Suy thận nặng (ClCr <30 mL/min) - khởi đầu 5mg, tối đa 10mg/ngày",
                "Bệnh nhân châu Á - cân nhắc khởi đầu 5mg do tăng nồng độ",
                "Suy gan - thận trọng, theo dõi men gan thường xuyên",
                "Người cao tuổi - tăng nguy cơ đau cơ",
                "Đái tháo đường - statins có thể tăng đường huyết nhẹ",
                "Liều cao (40mg) - tăng nguy cơ protein niệu"
            ]
        },
        "interactions": [
            "Cyclosporine: Tăng nồng độ rosuvastatin 7 lần - Giới hạn liều 5mg/ngày.",
            "Gemfibrozil: Tăng nồng độ rosuvastatin 2 lần - Tránh dùng chung.",
            "Warfarin: Tăng INR - Theo dõi INR.",
            "Thuốc kháng acid: Giảm hấp thu - Uống cách nhau 2 giờ."
        ],
        "pregnancy": "X - Chống chỉ định",
        "pregnancy_lactation": {
            "fda_category": "X",
            "pregnancy_details": "CHỐNG CHỈ ĐỊNH. Statin can thiệp vào tổng hợp cholesterol cần thiết cho sự phát triển của thai nhi. Ngưng thuốc ngay lập tức nếu phát hiện có thai.",
            "lactation": {
                "safety": "Avoid",
                "details": "Có khả năng bài tiết vào sữa mẹ và gây ảnh hưởng đến chuyển hóa lipid của trẻ.",
                "recommendation": "Không sử dụng. Ngưng cho con bú hoặc ngưng thuốc.",
            },
        },
        "renal_adjustment": {
            "normal": "Không cần chỉnh liều",
            "30_60": "Thận trọng, khởi đầu 5-10mg. Theo dõi chức năng thận.",
            "under_30": "Khởi đầu 5mg, tối đa 10mg/ngày. Thận trọng, theo dõi chức năng thận.",
            "dialysis": "Khởi đầu 5mg, tối đa 10mg/ngày. Rosuvastatin không được lọc sạch hiệu quả qua thẩm phân máu.",
            "notes": "Rosuvastatin thải trừ một phần qua thận (10%). Cần điều chỉnh liều ở suy thận nặng."
        },
        "reversal_agents": {
            "available": False,
            "agents": [],
            "notes": "Không có antidote đặc hiệu. Điều trị quá liều chủ yếu là hỗ trợ: ngừng thuốc, điều trị tiêu cơ vân nếu có (truyền dịch, kiềm hóa nước tiểu), theo dõi CK và chức năng thận."
        },
        "administration_instructions": {
            "oral": {
                "with_food": "Có thể uống với hoặc không thức ăn",
                "timing": "Uống 1 lần/ngày, có thể uống bất kỳ lúc nào"
            }
        },
        "references": {
            "primary_sources": [],
            "last_updated": "",
            "evidence_level": "",
        },
    },
    "Pravastatin":     {
        "group": "Cardiovascular - Statin",
        "vietnamese_name": "Pravastatin, Pravachol",
        "brand_names": {
            "common": [
                "Pravachol"
    ],
            "vietnam": [
                "Pravastatin 10/20/40mg"
    ],
        },
        "administration": [
            "PO"
    ],
        "indications": [
            "Tương tự Atorvastatin"
    ],
        "dosage": {
            "hypercholesterolemia": "10-40mg PO x 1 lần/tối.",
        },
        "side_effects": [
            "Tương tự Atorvastatin nhưng ít hơn"
    ],
        "mechanism_of_action": """Statin ít tương tác thuốc nhất (không chuyển hóa qua CYP450). An toàn hơn ở bệnh nhân dùng nhiều thuốc.""",
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
            "half_life": "~1.5-2 giờ (hoạt tính), bán thải ~77 giờ.",
        },
        "storage": "Bảo quản ở 25°C. Tránh ánh sáng và ẩm.",
        "risk_flags": {
            "high_alert": False,
            "narrow_therapeutic_index": False,
            "bleeding_risk": False,
            "organ_toxicity": [
                "Hepatotoxicity",
                "Myopathy/Rhabdomyolysis"
    ],
            "requires_monitoring": [
                "Liver function tests (ALT/AST)",
                "Creatine Kinase (if symptomatic)",
                "Lipid profile"
    ],
        },
        "guideline_tags": [
            "ACC/AHA 2018 Cholesterol Guidelines"
    ],
        "contraindications_detail": {
            "tuyệt_đối": [
                "Bệnh gan hoạt động",
                "Có thai",
                "Cho con bú",
                "Tiêu cơ vân đang hoạt động"
    ],
            "tương_đối": [
                "Suy thận nặng - cần điều chỉnh liều",
                "Dùng với cyclosporine - giảm liều",
                "Dùng với gemfibrozil - tránh dùng chung"
    ],
        },
        "renal_adjustment": {
            "normal": "Không đổi liều",
            "30_60": "Có thể cần giảm liều, theo dõi chức năng thận",
            "under_30": "Giảm liều hoặc tránh dùng nếu có lựa chọn khác",
            "hemodialysis": "Có thể cần bổ sung sau lọc máu (tùy thuốc)",
        },
        "contraindications": [],
        "interactions": [],
        "pregnancy": "",
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
}
