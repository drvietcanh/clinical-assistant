"""
ARBs - Angiotensin Receptor Blockers
"""

ARBS = {
    "Azilsartan medoxomil": {
        "group": "Cardiovascular - ARB (Angiotensin Receptor Blocker)",
        "vietnamese_name": "Azilsartan medoxomil, Edarbi",
        "administration": ["PO"],
        "indications": [
            "Tăng huyết áp (đặc biệt khi cần kiểm soát mạnh, 24 giờ)"
        ],
        "contraindications": [
            "Dị ứng với azilsartan hoặc ARB",
            "Có thai",
            "Hẹp động mạch thận 2 bên hoặc hẹp đơn thận còn lại"
        ],
        "dosage": {
            "adult_htn_initial": "40mg x 1 lần/ngày",
            "adult_htn_max": "80mg x 1 lần/ngày",
            "notes": "Có thể dùng đơn trị hoặc phối hợp với thiazide/thiazide-like (chlorthalidone, HCTZ). Không khuyến cáo ở suy gan nặng hoặc eGFR rất thấp nếu không theo dõi sát."
        },
        "renal_adjustment": {
            "normal": "Không cần chỉnh liều",
            "30_60": "Không cần chỉnh liều, theo dõi creatinine/kali",
            "under_30": "Thận trọng, cân nhắc liều thấp hơn và theo dõi sát"
        },
        "side_effects": [
            "Chóng mặt",
            "Hạ huyết áp (đặc biệt khi có lợi tiểu hoặc giảm thể tích)",
            "Tăng kali máu (nhưng tương tự ARB khác)",
            "Mệt mỏi",
            "Suy thận cấp (hiếm, đặc biệt trong hẹp ĐM thận, mất nước)"
        ],
        "interactions": [
            "Kali bổ sung và lợi tiểu giữ kali (spironolactone, eplerenone, amiloride, triamterene): tăng nguy cơ tăng kali máu",
            "NSAID: giảm hiệu quả hạ huyết áp, tăng nguy cơ suy thận",
            "Lithium: tăng nồng độ lithium"
        ],
        "pregnancy": "D - Chống chỉ định trong thai kỳ",
        "mechanism_of_action": "Azilsartan medoxomil là prodrug, thủy phân ở ruột và gan thành azilsartan (hoạt chất). Azilsartan ức chế chọn lọc thụ thể angiotensin II type 1 (AT1), ngăn vasoconstriction và tiết aldosterone. Các nghiên cứu cho thấy azilsartan có thể hạ huyết áp 24 giờ mạnh hơn một số ARB khác (olmesartan, valsartan) ở liều tương đương.",
        "monitoring": [
            "Huyết áp (bao gồm huyết áp 24h nếu có thể)",
            "Creatinine, BUN trước điều trị và 1-2 tuần sau khi bắt đầu/ tăng liều",
            "Kali máu định kỳ",
            "Dấu hiệu chóng mặt, ngất (hạ huyết áp quá mức)"
        ],
        "precautions": [
            "Khởi đầu liều thấp ở người cao tuổi, bệnh nhân đang dùng lợi tiểu hoặc giảm thể tích.",
            "Tránh phối hợp triple blockade RAAS (ACEI + ARB + aliskiren) trừ khi có chỉ định đặc biệt và theo dõi rất sát.",
            "Ngừng thuốc trước khi mang thai hoặc ngay khi phát hiện mang thai.",
            "Thận trọng khi phối hợp với NSAID, đặc biệt ở bệnh nhân suy thận, người cao tuổi, giảm thể tích."
        ],
        "pharmacokinetics": {
            "half_life": "11-13 giờ",
            "onset": "2-3 giờ",
            "duration": "≥24 giờ (cho phép dùng 1 lần/ngày)",
            "protein_binding": ">99%",
            "metabolism": "Chuyển hóa chủ yếu qua gan (CYP2C9) thành các chất chuyển hóa ít hoạt tính",
            "clearance": "Thải trừ qua phân (55%) và thận (42%)"
        },
        "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm, tránh ánh sáng.",
        "black_box_warnings": "CHỐNG CHỈ ĐỊNH trong thai kỳ: ARB (bao gồm azilsartan) có thể gây dị tật và tử vong thai nhi (thiểu ối, bất thường sọ, suy thận thai). Ngừng ngay khi phát hiện có thai.",
        "drug_interactions": {
            "major": [
                {
                    "drug": "Kali bổ sung, Lợi tiểu giữ kali",
                    "mechanism": "Giảm thải trừ kali, tác dụng cộng hưởng",
                    "effect": "Tăng kali máu nặng, nguy cơ loạn nhịp",
                    "management": "Tránh nếu có thể, hoặc theo dõi kali chặt chẽ và chỉnh liều."
                },
                {
                    "drug": "NSAIDs",
                    "mechanism": "Giảm prostaglandin thận, giảm lưu lượng máu thận",
                    "effect": "Giảm hiệu quả hạ huyết áp, tăng nguy cơ suy thận cấp.",
                    "management": "Hạn chế phối hợp lâu dài; theo dõi creatinine và kali khi bắt đầu/ thay đổi liều."
                }
            ],
            "moderate": [
                {
                    "drug": "Lithium",
                    "mechanism": "Giảm thải trừ lithium qua thận",
                    "effect": "Tăng nồng độ lithium, nguy cơ độc tính",
                    "management": "Theo dõi nồng độ lithium; cân nhắc giảm liều hoặc tránh phối hợp."
                },
                {
                    "drug": "Diuretics",
                    "mechanism": "Hiệp đồng giảm thể tích và RAAS",
                    "effect": "Hạ huyết áp quá mức, suy thận cấp",
                    "management": "Khởi đầu liều thấp azilsartan và/hoặc giảm liều lợi tiểu, theo dõi huyết áp/creatinine."
                }
            ],
            "minor": []
        },
        "contraindications": {
            "tuyệt_đối": [
                "Dị ứng azilsartan hoặc ARB",
                "Có thai",
                "Hẹp động mạch thận 2 bên hoặc hẹp thận độc nhất",
            ],
            "tương_đối": [
                "Suy thận nặng",
                "Giảm thể tích tuần hoàn (mất nước, dùng liều cao lợi tiểu)",
                "Tăng kali máu",
                "Suy gan trung bình-nặng"
            ]
        },
        "pregnancy_lactation": {
            "fda_category": "D",
            "pregnancy_details": "CHỐNG CHỈ ĐỊNH tuyệt đối trong thai kỳ. Nguy cơ dị tật và tử vong thai nhi cao nhất trong tam cá nguyệt 2-3.",
            "lactation": {
                "safety": "Caution",
                "details": "Chưa rõ bài tiết vào sữa; thận trọng nếu dùng cho mẹ cho con bú.",
                "recommendation": "Nếu cần ARB ở mẹ cho con bú, ưu tiên ARB đã có dữ liệu nhiều hơn; nếu dùng azilsartan, theo dõi trẻ."
            }
        },
        "hepatic_adjustment": {
            "mild": "Thường không cần chỉnh liều",
            "moderate": "Thận trọng, có thể khởi đầu liều thấp hơn (20mg/ngày)",
            "severe": "Không khuyến cáo (thiếu dữ liệu)",
            "notes": "Chuyển hóa qua CYP2C9; suy gan có thể tăng nồng độ thuốc."
        },
        "overdose_management": {
            "symptoms": [
                "Hạ huyết áp nặng",
                "Nhịp tim chậm hoặc nhanh phản xạ",
                "Suy thận cấp",
                "Tăng kali máu"
            ],
            "antidote": "Không có antidote đặc hiệu",
            "treatment": [
                "Đặt bệnh nhân nằm, nâng chân, truyền dịch (NaCl 0.9%)",
                "Vasopressor (norepinephrine) nếu tụt HA dai dẳng",
                "Điều trị tăng kali máu nếu có",
                "Theo dõi huyết áp, nhịp tim, creatinine, điện giải"
            ],
            "monitoring": "Huyết áp, nhịp tim, chức năng thận, điện giải (đặc biệt kali)."
        },
        "reversal_agents": {
            "available": False,
            "agents": []
        },
        "administration_instructions": {
            "oral": {
                "with_food": "Có thể uống với hoặc không thức ăn.",
                "timing": "Uống 1 lần/ngày, cùng giờ mỗi ngày. Khởi đầu 40mg, tăng lên 80mg nếu cần và dung nạp tốt."
            }
        },
        "references": {
            "primary_sources": [
                "FDA Drug Label - Edarbi (azilsartan medoxomil)",
                "UpToDate - Azilsartan: Drug information",
                "RCTs so sánh azilsartan với valsartan/olmesartan trong tăng huyết áp",
                "ACC/AHA Hypertension Guidelines 2024"
            ],
            "last_updated": "2025-02-18",
            "evidence_level": "High – FDA-approved, nhiều RCT chứng minh hiệu quả hạ huyết áp 24 giờ mạnh"
        },
        "risk_flags": {
            "high_alert": False,
            "narrow_therapeutic_index": False,
            "icu_critical_care_only": False,
            "bleeding_risk": "Low",
            "organ_toxicity": {"metabolic": "Moderate (hyperkalemia)", "renal": "Moderate"}
        },
        "guideline_tags": [
            "ACC/AHA Guidelines - Hypertension",
            "KDIGO Guidelines - Chronic Kidney Disease",
            "WHO Essential Medicines List"
        ],
        "last_updated": "2025-02-18",
    },
    "Candesartan": {
        "group": "Cardiovascular - ARB (Angiotensin Receptor Blocker)",
        "vietnamese_name": "Candesartan, Atacand",
        "administration": ["PO"],
        "indications": [
            "Tăng huyết áp",
            "Suy tim (không dung nạp ACE inhibitor)",
            "Bảo vệ thận trong đái tháo đường"
        ],
        "contraindications": [
            "Dị ứng ARB",
            "Có thai",
            "Hẹp động mạch thận 2 bên"
        ],
        "dosage": {
            "adult_htn": "8-32mg x 1 lần/ngày",
            "adult_heart_failure": "4mg x 1 lần/ngày, tăng đến 32mg x 1 lần/ngày",
            "notes": "Ít gây ho hơn ACE inhibitor. Khởi đầu 8mg/ngày."
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "Liều khởi đầu 4mg/ngày",
            "under_30": "Thận trọng, theo dõi sát"
        },
        "side_effects": [
            "Ít tác dụng phụ hơn ACE inhibitor",
            "Ho ít hơn ACE inhibitor",
            "Tăng kali máu (ít hơn ACE)",
            "Hạ huyết áp",
            "Chóng mặt"
        ],
        "interactions": [
            "Kali: tăng kali máu",
            "NSAID: giảm hiệu quả",
            "Lithium: tăng nồng độ lithium"
        ],
        "pregnancy": "D",
        "mechanism_of_action": "Candesartan là prodrug (candesartan cilexetil), chuyển hóa thành candesartan (hoạt chất) trong đường tiêu hóa. Ức chế thụ thể angiotensin II type 1 (AT1), ngăn chặn tác dụng của angiotensin II (giãn mạch, giảm aldosterone). Ít gây ho hơn ACE inhibitor vì không ảnh hưởng đến bradykinin.",
        "monitoring": [
            "Creatinine, BUN sau 1-2 tuần khi bắt đầu",
            "Kali máu định kỳ",
            "Huyết áp",
            "Dấu hiệu phù mạch (hiếm hơn ACE inhibitor)"
        ],
        "precautions": [
            "Khởi đầu với liều thấp (8mg/ngày), tăng dần",
            "Ưu điểm: ít gây ho hơn ACE inhibitor",
            "Theo dõi sát creatinine khi bắt đầu",
            "Tránh dùng với NSAID",
            "Ngừng ngay nếu có phù mạch"
        ],
        "pharmacokinetics": {
            "half_life": "9 giờ",
            "onset": "2-4 giờ",
            "duration": "24 giờ",
            "protein_binding": ">99%",
            "metabolism": "Candesartan cilexetil chuyển hóa thành candesartan trong đường tiêu hóa",
            "clearance": "Chủ yếu qua thận (60%) và gan (40%)"
        },
        "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm",
        "black_box_warnings": "Chống chỉ định trong thai kỳ - có thể gây dị tật thai nhi và tử vong thai nhi.",
        "references": {
            "primary_sources": [
                "FDA Drug Label - Atacand (candesartan)",
                "UpToDate - Candesartan: Drug Information",
                "CHARM Study - The Lancet"
            ],
            "last_updated": "2025-02-18",
            "evidence_level": "High - CHARM Study showing benefit in heart failure"
        },
        "risk_flags": {
            "high_alert": False,
            "narrow_therapeutic_index": False,
            "icu_critical_care_only": False,
            "bleeding_risk": "Low",
            "organ_toxicity": {"metabolic": "Moderate (hyperkalemia)", "renal": "Moderate"}
        },
        "guideline_tags": [
            "ACC/AHA/HFSA Guidelines - Heart Failure with Reduced Ejection Fraction",
            "ESC Guidelines - Heart Failure",
            "CHARM Study - Heart Failure",
            "ACC/AHA Guidelines - Hypertension",
            "WHO Essential Medicines List"
        ],
        "last_updated": "2025-02-18",
        "drug_interactions": {
            "major": [],
            "moderate": [],
            "minor": []
        },
        "pregnancy_lactation": {
            "fda_category": "",
            "pregnancy_details": "",
            "lactation_details": ""
        },
        "hepatic_adjustment": {
            "mild": "",
            "moderate": "",
            "severe": ""
        },
        "overdose_management": {
            "symptoms": [],
            "treatment": "",
            "antidote": None
        },
        "reversal_agents": {
            "available": False,
            "agents": [],
            "notes": ""
        },
        "administration_instructions": {
            "preparation": "",
            "administration": "",
            "monitoring": []
        },
    },

    "Irbesartan": {
        "group": "Cardiovascular - ARB (Angiotensin Receptor Blocker)",
        "vietnamese_name": "Irbesartan, Avapro",
        "administration": ["PO"],
        "indications": [
            "Tăng huyết áp",
            "Bảo vệ thận trong đái tháo đường type 2 với protein niệu",
            "Bệnh thận đái tháo đường"
        ],
        "contraindications": [
            "Dị ứng ARB",
            "Có thai",
            "Hẹp động mạch thận 2 bên"
        ],
        "dosage": {
            "adult_htn": "150-300mg x 1 lần/ngày",
            "adult_diabetic_nephropathy": "300mg x 1 lần/ngày",
            "notes": "Ít gây ho hơn ACE inhibitor. Khởi đầu 150mg/ngày."
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "Liều khởi đầu 75mg/ngày",
            "under_30": "Thận trọng, theo dõi sát"
        },
        "side_effects": [
            "Ít tác dụng phụ hơn ACE inhibitor",
            "Ho ít hơn ACE inhibitor",
            "Tăng kali máu (ít hơn ACE)",
            "Hạ huyết áp",
            "Chóng mặt",
            "Mệt mỏi"
        ],
        "interactions": [
            "Kali: tăng kali máu",
            "NSAID: giảm hiệu quả",
            "Lithium: tăng nồng độ lithium"
        ],
        "pregnancy": "D",
        "mechanism_of_action": "Ức chế thụ thể angiotensin II type 1 (AT1), ngăn chặn tác dụng của angiotensin II (giãn mạch, giảm aldosterone). Ít gây ho hơn ACE inhibitor vì không ảnh hưởng đến bradykinin. Không phải prodrug (tác dụng trực tiếp). Đặc biệt hiệu quả trong bảo vệ thận ở bệnh nhân đái tháo đường type 2 với protein niệu.",
        "monitoring": [
            "Creatinine, BUN sau 1-2 tuần khi bắt đầu",
            "Kali máu định kỳ",
            "Huyết áp",
            "Protein niệu (nếu dùng cho bệnh thận đái tháo đường)",
            "eGFR (nếu dùng cho bệnh thận đái tháo đường)"
        ],
        "precautions": [
            "Khởi đầu với liều thấp (150mg/ngày), tăng dần",
            "Ưu điểm: ít gây ho hơn ACE inhibitor",
            "Theo dõi sát creatinine khi bắt đầu",
            "Tránh dùng với NSAID",
            "Ngừng ngay nếu có phù mạch",
            "Đặc biệt hiệu quả trong bệnh thận đái tháo đường với protein niệu"
        ],
        "pharmacokinetics": {
            "half_life": "11-15 giờ",
            "onset": "1-2 giờ",
            "duration": "24 giờ",
            "protein_binding": "90%",
            "metabolism": "Chuyển hóa qua gan (CYP2C9)",
            "clearance": "Chủ yếu qua gan (80%) và thận (20%)"
        },
        "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm",
        "black_box_warnings": "Chống chỉ định trong thai kỳ - có thể gây dị tật thai nhi và tử vong thai nhi.",
        "references": {
            "primary_sources": [
                "FDA Drug Label - Avapro (irbesartan)",
                "UpToDate - Irbesartan: Drug Information",
                "IRMA-2 Study - The New England Journal of Medicine",
                "IDNT Study - The New England Journal of Medicine"
            ],
            "last_updated": "2025-02-18",
            "evidence_level": "High - IRMA-2, IDNT studies showing benefit in diabetic nephropathy"
        },
        "risk_flags": {
            "high_alert": False,
            "narrow_therapeutic_index": False,
            "icu_critical_care_only": False,
            "bleeding_risk": "Low",
            "organ_toxicity": {"metabolic": "Moderate (hyperkalemia)", "renal": "Moderate"}
        },
        "guideline_tags": [
            "KDIGO Guidelines - Diabetic Kidney Disease",
            "IRMA-2 Study - Diabetic Nephropathy",
            "IDNT Study - Diabetic Nephropathy",
            "ACC/AHA Guidelines - Hypertension",
            "WHO Essential Medicines List"
        ],
        "last_updated": "2025-02-18",
        "drug_interactions": {
            "major": [],
            "moderate": [],
            "minor": []
        },
        "pregnancy_lactation": {
            "fda_category": "",
            "pregnancy_details": "",
            "lactation_details": ""
        },
        "hepatic_adjustment": {
            "mild": "",
            "moderate": "",
            "severe": ""
        },
        "overdose_management": {
            "symptoms": [],
            "treatment": "",
            "antidote": None
        },
        "reversal_agents": {
            "available": False,
            "agents": [],
            "notes": ""
        },
        "administration_instructions": {
            "preparation": "",
            "administration": "",
            "monitoring": []
        },
    },

    "Losartan": {
        "group": "Cardiovascular - ARB (Angiotensin Receptor Blocker)",
        "vietnamese_name": "Losartan, Cozaar",
        "administration": ["PO"],
        "indications": [
            "Tăng huyết áp",
            "Suy tim (không dung nạp ACE inhibitor)",
            "Bảo vệ thận trong đái tháo đường"
        ],
        "contraindications": [
            "Dị ứng ARB",
            "Có thai",
            "Hẹp động mạch thận 2 bên"
        ],
        "dosage": {
            "adult_htn": "50-100mg x 1-2 lần/ngày",
            "adult_heart_failure": "25-50mg x 1 lần/ngày, tăng đến 50-100mg x 1 lần/ngày",
            "notes": "Ít gây ho hơn ACE inhibitor"
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "Liều khởi đầu 25mg/ngày",
            "under_30": "Thận trọng, theo dõi sát"
        },
        "side_effects": [
            "Ít tác dụng phụ hơn ACE inhibitor",
            "Ho ít hơn ACE inhibitor",
            "Tăng kali máu (ít hơn ACE)",
            "Hạ huyết áp"
        ],
        "interactions": [
            "Kali: tăng kali máu",
            "NSAID: giảm hiệu quả"
        ],
        "pregnancy": "D",
        "risk_flags": {
            "high_alert": False,
            "narrow_therapeutic_index": False,
            "icu_critical_care_only": False,
            "bleeding_risk": "Low",
            "organ_toxicity": ["hyperkalemia", "renal_impairment", "angioedema"]
        },
        "guideline_tags": [
            "ACC/AHA/HFSA HFrEF ARB Class I/IIa (ACEi intolerant)",
            "ESC HFrEF ARB Class I/IIa (ACEi intolerant)"
        ],
        "mechanism_of_action": "Losartan là prodrug, chuyển hóa thành EXP-3174 (hoạt chất) trong gan. Ức chế thụ thể angiotensin II type 1 (AT1), ngăn chặn tác dụng của angiotensin II (giãn mạch, giảm aldosterone). Ít gây ho hơn ACE inhibitor vì không ảnh hưởng đến bradykinin",
        "monitoring": [
            "Creatinine, BUN sau 1-2 tuần khi bắt đầu",
            "Kali máu định kỳ (ít hơn ACE inhibitor)",
            "Huyết áp",
            "Ít phải theo dõi ho khan (không gây ho như ACE inhibitor)"
        ],
        "precautions": [
            "Khởi đầu với liều thấp (25-50mg), tăng dần",
            "Ưu điểm: ít gây ho hơn ACE inhibitor (thay thế tốt cho bệnh nhân không dung nạp ACE inhibitor)",
            "Vẫn có thể gây tăng kali máu và suy thận cấp (nhưng ít hơn ACE inhibitor)",
            "Theo dõi sát creatinine khi bắt đầu",
            "Tránh dùng với NSAID (giảm hiệu quả, tăng nguy cơ suy thận)",
            "Ngừng ngay nếu có phù mạch (hiếm hơn ACE inhibitor nhưng vẫn có thể xảy ra)"
        ],
        "pharmacokinetics": {
            "half_life": "Losartan: 2 giờ; EXP-3174 (active): 6-9 giờ",
            "onset": "1 giờ",
            "duration": "24 giờ",
            "protein_binding": "98.7%",
            "clearance": "Gan (chuyển hóa), thận (EXP-3174)"
        },
        "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm, tránh ánh sáng",
        "black_box_warnings": "Chống chỉ định trong thai kỳ - có thể gây dị tật thai nhi và tử vong thai nhi",
        "drug_interactions": {
            "major": [
                {
                    "drug": "Kali bổ sung, Kali-sparing diuretics (spironolactone, eplerenone, amiloride, triamterene)",
                    "mechanism": "Tác dụng hiệp đồng tăng kali máu",
                    "effect": "Tăng kali máu nghiêm trọng, có thể gây rối loạn nhịp tim",
                    "management": "Thận trọng. Theo dõi kali máu thường xuyên. Tránh dùng cùng nếu có thể."
                },
                {
                    "drug": "NSAIDs (ibuprofen, naproxen, diclofenac)",
                    "mechanism": "Giảm tác dụng giãn mạch, giảm lưu lượng máu thận",
                    "effect": "Giảm hiệu quả hạ huyết áp, tăng nguy cơ suy thận cấp",
                    "management": "Thận trọng. Theo dõi chức năng thận, huyết áp. Tránh dùng lâu dài cùng."
                }
            ],
            "moderate": [
                {
                    "drug": "Lithium",
                    "mechanism": "ARB giảm thải trừ lithium qua thận",
                    "effect": "Tăng nồng độ lithium, tăng nguy cơ độc tính",
                    "management": "Theo dõi nồng độ lithium. Giảm liều lithium nếu cần."
                },
                {
                    "drug": "Diuretics (furosemide, hydrochlorothiazide)",
                    "mechanism": "Tác dụng hiệp đồng hạ huyết áp",
                    "effect": "Tăng nguy cơ hạ huyết áp quá mức",
                    "management": "Thận trọng khi bắt đầu. Có thể cần giảm liều diuretic."
                }
            ],
            "minor": [
                {
                    "drug": "Rifampin",
                    "mechanism": "CYP2C9 inducer làm giảm chuyển hóa losartan",
                    "effect": "Giảm hiệu quả hạ huyết áp",
                    "management": "Theo dõi huyết áp. Có thể cần tăng liều losartan."
                }
            ]
        },
        "contraindications": {
            "tuyệt_đối": [
                "Dị ứng ARB",
                "Có thai",
                "Hẹp động mạch thận 2 bên",
                "Phù mạch trước đây với ARB"
            ],
            "tương_đối": [
                "Suy thận nặng (CrCl <10) - không dùng",
                "Suy thận trung bình (CrCl 10-30) - giảm liều, theo dõi sát",
                "Tăng kali máu - điều chỉnh trước khi dùng",
                "Hẹp động mạch thận 1 bên - thận trọng",
                "Dùng kali-sparing diuretics - tăng nguy cơ tăng kali máu",
                "Dùng NSAID - tăng nguy cơ suy thận"
            ]
        },
        "pregnancy_lactation": {
            "fda_category": "D",
            "pregnancy_details": "CHỐNG CHỈ ĐỊNH TUYỆT ĐỐI trong thai kỳ. Có thể gây dị tật thai nhi (dị tật thận, xương sọ, phổi), thiểu ối, chậm phát triển thai nhi, và tử vong thai nhi. Nguy cơ cao nhất trong 3 tháng đầu và 3 tháng cuối. Ngừng ngay khi phát hiện có thai.",
            "lactation": {
                "safety": "Compatible",
                "details": "Losartan và EXP-3174 bài tiết vào sữa mẹ ở nồng độ thấp. Nồng độ trong máu trẻ bú mẹ thường rất thấp. Không có báo cáo về tác dụng phụ nghiêm trọng ở trẻ bú mẹ.",
                "recommendation": "Có thể dùng khi cho con bú. Theo dõi trẻ nếu có dấu hiệu bất thường."
            }
        },
        "hepatic_adjustment": {
            "mild": "Không đổi",
            "moderate": "Thận trọng, có thể giảm liều (chuyển hóa qua gan)",
            "severe": "Giảm liều 50% (chuyển hóa qua gan)",
            "notes": "Losartan là prodrug chuyển hóa thành EXP-3174 trong gan (CYP2C9). Suy gan có thể làm giảm chuyển hóa thành hoạt chất. EXP-3174 thải qua thận."
        },
        "overdose_management": {
            "symptoms": [
                "Hạ huyết áp nghiêm trọng",
                "Nhịp tim chậm",
                "Suy thận cấp",
                "Tăng kali máu",
                "Phù mạch (hiếm)"
            ],
            "antidote": "Không có antidote đặc hiệu. Điều trị hỗ trợ",
            "treatment": [
                "Điều trị hạ huyết áp: Truyền dịch (normal saline), nâng chân, nếu cần: dopamine, norepinephrine",
                "Rửa dạ dày nếu uống trong vòng 1-2 giờ",
                "Than hoạt tính",
                "Theo dõi huyết áp, nhịp tim, chức năng thận, điện giải",
                "Điều trị tăng kali máu nếu có: Calcium gluconate, insulin + glucose, sodium bicarbonate",
                "Nếu có phù mạch: Epinephrine, corticosteroids, antihistamines",
                "Hỗ trợ hô hấp và tuần hoàn nếu cần",
                "Theo dõi ít nhất 12-24 giờ (do half-life của EXP-3174: 6-9 giờ)"
            ],
            "monitoring": "Huyết áp, nhịp tim, chức năng thận (creatinine, BUN), điện giải (kali), dấu hiệu phù mạch, ý thức"
        },
        "reversal_agents": {
            "available": False,
            "agents": []
        },
        "administration_instructions": {
            "oral": {
                "with_food": "Có thể uống với hoặc không có thức ăn. Không ảnh hưởng đáng kể đến hấp thu.",
                "timing": "Uống 1-2 lần/ngày (do half-life của EXP-3174: 6-9 giờ). Khởi đầu với liều thấp (25-50mg), tăng dần. Uống đúng giờ mỗi ngày. Ưu điểm: ít gây ho hơn ACE inhibitor."
            },
            "iv": {
                "reconstitution": "Không có dạng IV",
                "infusion_rate": "N/A",
                "compatibility": [],
                "incompatibility": [],
                "notes": "Chỉ có dạng uống"
            }
        },
        "pediatric_dosing": {
            "neonates": "Không khuyến cáo cho trẻ <6 tuổi (dữ liệu hạn chế)",
            "infants": "Không khuyến cáo cho trẻ <6 tuổi (dữ liệu hạn chế)",
            "children": "6-16 tuổi: 0.7mg/kg/ngày x 1 lần (tối đa 50mg/ngày). Chỉ dùng cho tăng huyết áp. Theo dõi huyết áp, chức năng thận, kali máu",
            "adolescents": "25-50mg x 1 lần/ngày, tăng dần đến 50-100mg/ngày nếu cần. Liều người lớn",
            "notes": "Dữ liệu hạn chế ở trẻ em. Chỉ dùng cho tăng huyết áp ở trẻ ≥6 tuổi. Khởi đầu với liều thấp, tăng dần. Theo dõi huyết áp, chức năng thận, kali máu"
        },
        "geriatric_dosing": {
            "considerations": "Người cao tuổi nhạy cảm hơn với tác dụng hạ huyết áp. Suy thận phổ biến hơn",
            "dose_adjustment": "Khởi đầu với liều thấp hơn (25mg x 1 lần/ngày). Tăng dần chậm hơn. Điều chỉnh theo CrCl",
            "monitoring": "Theo dõi huyết áp sát hơn (nguy cơ hạ huyết áp quá mức). Theo dõi chức năng thận, kali máu thường xuyên"
        },
        "brand_names": {
            "vietnam": ["Cozaar", "Losartan Stada", "Losartan", "Losar"],
            "common": ["Cozaar", "Losartan"]
        },
        "cost_estimate": {
            "unit": "VND",
            "range": "15,000 - 40,000 VND/viên (tùy hàm lượng và thương hiệu)",
            "note": "Giá thay đổi theo thương hiệu và nhà thuốc. Losartan generic thường rẻ hơn (15,000-25,000 VND/viên 50mg)."
        },
        "references": {
            "primary_sources": [
                "FDA Drug Label - Cozaar (losartan)",
                "UpToDate - Losartan: Drug information",
                "ELITE-2 Study - The Lancet",
                "LIFE Study - The Lancet",
                "American Heart Association/American College of Cardiology guidelines"
            ],
            "last_updated": "2025-02-18",
            "evidence_level": "High - Multiple large RCTs (ELITE-2, LIFE) and extensive clinical experience"
        },
        "risk_flags": {
            "high_alert": False,
            "narrow_therapeutic_index": False,
            "icu_critical_care_only": False,
            "bleeding_risk": "Low",
            "organ_toxicity": {"metabolic": "Moderate (hyperkalemia)", "renal": "Moderate"}
        },
        "guideline_tags": [
            "ACC/AHA/HFSA Guidelines - Heart Failure with Reduced Ejection Fraction",
            "ESC Guidelines - Heart Failure",
            "ACC/AHA Guidelines - Hypertension",
            "KDIGO Guidelines - Chronic Kidney Disease",
            "WHO Essential Medicines List"
        ],
        "last_updated": "2025-02-18",
    },
    
    "Olmesartan": {
        "group": "Cardiovascular - ARB (Angiotensin Receptor Blocker)",
        "vietnamese_name": "Olmesartan, Benicar",
        "administration": ["PO"],
        "indications": [
            "Tăng huyết áp",
            "Bảo vệ thận trong đái tháo đường"
        ],
        "contraindications": [
            "Dị ứng ARB",
            "Có thai",
            "Hẹp động mạch thận 2 bên"
        ],
        "dosage": {
            "adult_htn": "20-40mg x 1 lần/ngày",
            "notes": "Ít gây ho hơn ACE inhibitor. Khởi đầu 20mg/ngày."
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "Liều khởi đầu 20mg/ngày",
            "under_30": "Thận trọng, theo dõi sát"
        },
        "side_effects": [
            "Ít tác dụng phụ hơn ACE inhibitor",
            "Ho ít hơn ACE inhibitor",
            "Tăng kali máu (ít hơn ACE)",
            "Hạ huyết áp",
            "Chóng mặt",
            "Sprue-like enteropathy (hiếm nhưng có thể nghiêm trọng)"
        ],
        "interactions": [
            "Kali: tăng kali máu",
            "NSAID: giảm hiệu quả",
            "Lithium: tăng nồng độ lithium"
        ],
        "pregnancy": "D",
        "mechanism_of_action": "Ức chế thụ thể angiotensin II type 1 (AT1), ngăn chặn tác dụng của angiotensin II (giãn mạch, giảm aldosterone). Ít gây ho hơn ACE inhibitor vì không ảnh hưởng đến bradykinin. Không phải prodrug (tác dụng trực tiếp).",
        "monitoring": [
            "Creatinine, BUN sau 1-2 tuần khi bắt đầu",
            "Kali máu định kỳ",
            "Huyết áp",
            "Dấu hiệu tiêu chảy mãn tính, giảm cân (sprue-like enteropathy)"
        ],
        "precautions": [
            "Khởi đầu với liều thấp (20mg/ngày), tăng dần",
            "Ưu điểm: ít gây ho hơn ACE inhibitor",
            "Theo dõi sát creatinine khi bắt đầu",
            "Tránh dùng với NSAID",
            "Ngừng ngay nếu có phù mạch",
            "Theo dõi dấu hiệu sprue-like enteropathy (tiêu chảy mãn tính, giảm cân) - ngừng thuốc nếu có"
        ],
        "pharmacokinetics": {
            "half_life": "13 giờ",
            "onset": "1-2 giờ",
            "duration": "24 giờ",
            "protein_binding": "99%",
            "metabolism": "Chuyển hóa ít (không qua CYP)",
            "clearance": "Chủ yếu qua phân (60%) và thận (40%)"
        },
        "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm",
        "black_box_warnings": "Chống chỉ định trong thai kỳ - có thể gây dị tật thai nhi và tử vong thai nhi. Sprue-like enteropathy - ngừng ngay nếu có tiêu chảy mãn tính, giảm cân.",
        "references": {
            "primary_sources": [
                "FDA Drug Label - Benicar (olmesartan)",
                "UpToDate - Olmesartan: Drug Information"
            ],
            "last_updated": "2025-02-18",
            "evidence_level": "High"
        },
        "risk_flags": {
            "high_alert": False,
            "narrow_therapeutic_index": False,
            "icu_critical_care_only": False,
            "bleeding_risk": "Low",
            "organ_toxicity": {"metabolic": "Moderate (hyperkalemia)", "renal": "Moderate", "gastrointestinal": "Moderate (sprue-like enteropathy)"}
        },
        "guideline_tags": [
            "ACC/AHA Guidelines - Hypertension",
            "KDIGO Guidelines - Chronic Kidney Disease",
            "WHO Essential Medicines List"
        ],
        "last_updated": "2025-02-18",
        "drug_interactions": {
            "major": [],
            "moderate": [],
            "minor": []
        },
        "pregnancy_lactation": {
            "fda_category": "",
            "pregnancy_details": "",
            "lactation_details": ""
        },
        "hepatic_adjustment": {
            "mild": "",
            "moderate": "",
            "severe": ""
        },
        "overdose_management": {
            "symptoms": [],
            "treatment": "",
            "antidote": None
        },
        "reversal_agents": {
            "available": False,
            "agents": [],
            "notes": ""
        },
        "administration_instructions": {
            "preparation": "",
            "administration": "",
            "monitoring": []
        },
    },

    "Telmisartan": {
        "group": "Cardiovascular - ARB (Angiotensin Receptor Blocker)",
        "vietnamese_name": "Telmisartan, Micardis",
        "administration": ["PO"],
        "indications": [
            "Tăng huyết áp",
            "Giảm nguy cơ tim mạch ở bệnh nhân có nguy cơ cao",
            "Bảo vệ thận trong đái tháo đường"
        ],
        "contraindications": [
            "Dị ứng ARB",
            "Có thai",
            "Hẹp động mạch thận 2 bên"
        ],
        "dosage": {
            "adult_htn": "40-80mg x 1 lần/ngày",
            "adult_high_risk": "80mg x 1 lần/ngày",
            "notes": "Dùng 1 lần/ngày. Half-life dài (24 giờ). Có thể dùng với hoặc không thức ăn."
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "Liều khởi đầu 20mg/ngày",
            "under_30": "Thận trọng, liều khởi đầu 20mg/ngày"
        },
        "side_effects": [
            "Ít tác dụng phụ hơn ACE inhibitor",
            "Ho ít hơn ACE inhibitor",
            "Tăng kali máu (ít hơn ACE)",
            "Hạ huyết áp",
            "Chóng mặt",
            "Đau lưng (hiếm)"
        ],
        "interactions": [
            "Kali: tăng kali máu",
            "NSAID: giảm hiệu quả",
            "Digoxin: có thể tăng nồng độ digoxin"
        ],
        "pregnancy": "D",
        "risk_flags": {
            "high_alert": False,
            "narrow_therapeutic_index": False,
            "icu_critical_care_only": False,
            "bleeding_risk": "Low",
            "organ_toxicity": ["hyperkalemia", "renal_impairment", "angioedema"]
        },
        "guideline_tags": [
            "ACC/AHA/HFSA HFrEF ARB Class I/IIa (ACEi intolerant)",
            "ESC HFrEF ARB Class I/IIa (ACEi intolerant)"
        ],
        "mechanism_of_action": "Telmisartan ức chế thụ thể angiotensin II type 1 (AT1), ngăn chặn tác dụng của angiotensin II (giãn mạch, giảm aldosterone). Không phải prodrug (khác với losartan), tác dụng trực tiếp. Ít gây ho hơn ACE inhibitor vì không ảnh hưởng đến bradykinin. Đặc điểm: half-life dài nhất trong các ARB (24 giờ), cho phép dùng 1 lần/ngày. Có tác dụng kích hoạt PPAR-gamma (peroxisome proliferator-activated receptor gamma) nhẹ, có thể có lợi ích chuyển hóa.",
        "monitoring": [
            "Creatinine, BUN sau 1-2 tuần khi bắt đầu",
            "Kali máu định kỳ (ít hơn ACE inhibitor)",
            "Huyết áp",
            "Ít phải theo dõi ho khan (không gây ho như ACE inhibitor)"
        ],
        "precautions": [
            "Khởi đầu với liều thấp (20-40mg), tăng dần",
            "Ưu điểm: ít gây ho hơn ACE inhibitor, half-life dài (dùng 1 lần/ngày)",
            "Vẫn có thể gây tăng kali máu và suy thận cấp (nhưng ít hơn ACE inhibitor)",
            "Theo dõi sát creatinine khi bắt đầu",
            "Tránh dùng với NSAID (giảm hiệu quả, tăng nguy cơ suy thận)",
            "Ngừng ngay nếu có phù mạch (hiếm hơn ACE inhibitor nhưng vẫn có thể xảy ra)"
        ],
        "pharmacokinetics": {
            "half_life": "24 giờ (dài nhất trong các ARB)",
            "onset": "3 giờ",
            "duration": "24 giờ (dùng 1 lần/ngày)",
            "protein_binding": ">99%",
            "metabolism": "Chuyển hóa ít (glucuronidation)",
            "clearance": "Chủ yếu qua phân (97%), một phần qua thận (3%)"
        },
        "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm, tránh ánh sáng",
        "black_box_warnings": "Chống chỉ định trong thai kỳ - có thể gây dị tật thai nhi và tử vong thai nhi",
        "drug_interactions": {
            "major": [
                {
                    "drug": "Kali bổ sung, Kali-sparing diuretics (spironolactone, eplerenone, amiloride, triamterene)",
                    "mechanism": "Tác dụng hiệp đồng tăng kali máu",
                    "effect": "Tăng kali máu nghiêm trọng, có thể gây rối loạn nhịp tim",
                    "management": "Thận trọng. Theo dõi kali máu thường xuyên. Tránh dùng cùng nếu có thể."
                },
                {
                    "drug": "NSAIDs (ibuprofen, naproxen, diclofenac)",
                    "mechanism": "Giảm tác dụng giãn mạch, giảm lưu lượng máu thận",
                    "effect": "Giảm hiệu quả hạ huyết áp, tăng nguy cơ suy thận cấp",
                    "management": "Thận trọng. Theo dõi chức năng thận, huyết áp. Tránh dùng lâu dài cùng."
                }
            ],
            "moderate": [
                {
                    "drug": "Digoxin",
                    "mechanism": "Telmisartan có thể tăng nồng độ digoxin",
                    "effect": "Tăng nồng độ digoxin, tăng nguy cơ độc tính",
                    "management": "Theo dõi nồng độ digoxin. Giảm liều digoxin nếu cần."
                },
                {
                    "drug": "Lithium",
                    "mechanism": "ARB giảm thải trừ lithium qua thận",
                    "effect": "Tăng nồng độ lithium, tăng nguy cơ độc tính",
                    "management": "Theo dõi nồng độ lithium. Giảm liều lithium nếu cần."
                }
            ],
            "minor": []
        },
        "contraindications": {
            "tuyệt_đối": [
                "Dị ứng telmisartan hoặc ARB",
                "Có thai",
                "Hẹp động mạch thận 2 bên",
                "Phù mạch trước đây với ARB"
            ],
            "tương_đối": [
                "Suy thận nặng (CrCl <10) - không dùng",
                "Suy thận trung bình (CrCl 10-30) - giảm liều, theo dõi sát",
                "Tăng kali máu - điều chỉnh trước khi dùng",
                "Hẹp động mạch thận 1 bên - thận trọng",
                "Dùng kali-sparing diuretics - tăng nguy cơ tăng kali máu",
                "Dùng NSAID - tăng nguy cơ suy thận"
            ]
        },
        "pregnancy_lactation": {
            "fda_category": "D",
            "pregnancy_details": "CHỐNG CHỈ ĐỊNH TUYỆT ĐỐI trong thai kỳ. Có thể gây dị tật thai nhi (dị tật thận, xương sọ, phổi), thiểu ối, chậm phát triển thai nhi, và tử vong thai nhi. Nguy cơ cao nhất trong 3 tháng đầu và 3 tháng cuối. Ngừng ngay khi phát hiện có thai.",
            "lactation": {
                "safety": "Compatible",
                "details": "Telmisartan bài tiết vào sữa mẹ ở nồng độ thấp. Nồng độ trong máu trẻ bú mẹ thường rất thấp. Không có báo cáo về tác dụng phụ nghiêm trọng ở trẻ bú mẹ.",
                "recommendation": "Có thể dùng khi cho con bú. Theo dõi trẻ nếu có dấu hiệu bất thường."
            }
        },
        "hepatic_adjustment": {
            "mild": "Không đổi",
            "moderate": "Thận trọng, có thể giảm liều nhẹ",
            "severe": "Giảm liều 50% hoặc tránh dùng",
            "notes": "Telmisartan chuyển hóa ít qua gan (glucuronidation), thải trừ chủ yếu qua phân (97%). Suy gan có thể ảnh hưởng nhẹ đến dược động học. Thận trọng ở suy gan nặng."
        },
        "overdose_management": {
            "symptoms": [
                "Hạ huyết áp nghiêm trọng",
                "Nhịp tim chậm",
                "Suy thận cấp",
                "Tăng kali máu",
                "Phù mạch (hiếm)"
            ],
            "antidote": "Không có antidote đặc hiệu. Điều trị hỗ trợ",
            "treatment": [
                "Điều trị hạ huyết áp: Truyền dịch (normal saline), nâng chân, nếu cần: dopamine, norepinephrine",
                "Rửa dạ dày nếu uống trong vòng 1-2 giờ",
                "Than hoạt tính",
                "Theo dõi huyết áp, nhịp tim, chức năng thận, điện giải",
                "Điều trị tăng kali máu nếu có: Calcium gluconate, insulin + glucose, sodium bicarbonate",
                "Nếu có phù mạch: Epinephrine, corticosteroids, antihistamines",
                "Hỗ trợ hô hấp và tuần hoàn nếu cần",
                "Theo dõi ít nhất 24 giờ (do half-life dài: 24 giờ)"
            ],
            "monitoring": "Huyết áp, nhịp tim, chức năng thận (creatinine, BUN), điện giải (kali), dấu hiệu phù mạch, ý thức"
        },
        "reversal_agents": {
            "available": False,
            "agents": []
        },
        "administration_instructions": {
            "oral": {
                "with_food": "Có thể uống với hoặc không có thức ăn. Không ảnh hưởng đáng kể đến hấp thu.",
                "timing": "Uống 1 lần/ngày (do half-life dài: 24 giờ). Khởi đầu với liều thấp (20-40mg), tăng dần. Uống đúng giờ mỗi ngày. Ưu điểm: compliance tốt hơn do chỉ uống 1 lần/ngày."
            },
            "iv": {
                "reconstitution": "Không có dạng IV",
                "infusion_rate": "N/A",
                "compatibility": [],
                "incompatibility": [],
                "notes": "Chỉ có dạng uống"
            }
        },
        "pediatric_dosing": {
            "neonates": "Không khuyến cáo cho trẻ <18 tuổi (dữ liệu hạn chế).",
            "infants": "Không khuyến cáo cho trẻ <18 tuổi (dữ liệu hạn chế).",
            "children": "Không khuyến cáo cho trẻ <18 tuổi (dữ liệu hạn chế).",
            "adolescents": "≥18 tuổi: Liều người lớn. 40-80mg x 1 lần/ngày.",
            "notes": "Dữ liệu hạn chế ở trẻ em. Chỉ dùng cho tăng huyết áp ở trẻ ≥18 tuổi. Khởi đầu với liều thấp, tăng dần. Theo dõi huyết áp, chức năng thận, kali máu"
        },
        "geriatric_dosing": {
            "considerations": "Người cao tuổi nhạy cảm hơn với tác dụng hạ huyết áp. Suy thận phổ biến hơn.",
            "dose_adjustment": "Khởi đầu với liều thấp hơn (20mg x 1 lần/ngày). Tăng dần chậm hơn. Điều chỉnh theo CrCl",
            "monitoring": "Theo dõi huyết áp sát hơn (nguy cơ hạ huyết áp quá mức). Theo dõi chức năng thận, kali máu thường xuyên"
        },
        "brand_names": {
            "vietnam": ["Micardis", "Telmisartan", "Telmisartan Stada"],
            "common": ["Micardis", "Telmisartan"]
        },
        "cost_estimate": {
            "unit": "VND",
            "range": "20,000 - 60,000 VND/viên (tùy hàm lượng và thương hiệu)",
            "note": "Giá thay đổi theo thương hiệu và nhà thuốc. Telmisartan generic thường rẻ hơn (20,000-40,000 VND/viên 40mg). Micardis (brand) thường đắt hơn (40,000-60,000 VND/viên 40mg)."
        },
        "references": {
            "primary_sources": [
                "FDA Drug Label - Micardis (telmisartan)",
                "UpToDate - Telmisartan: Drug information",
                "ONTARGET Study - The New England Journal of Medicine",
                "TRANSCEND Study - The Lancet",
                "American Heart Association/American College of Cardiology guidelines"
            ],
            "last_updated": "2025-02-18",
            "evidence_level": "High - Multiple large RCTs (ONTARGET, TRANSCEND) and extensive clinical experience"
        },
        "risk_flags": {
            "high_alert": False,
            "narrow_therapeutic_index": False,
            "icu_critical_care_only": False,
            "bleeding_risk": "Low",
            "organ_toxicity": {"metabolic": "Moderate (hyperkalemia)", "renal": "Moderate"}
        },
        "guideline_tags": [
            "ACC/AHA Guidelines - Hypertension",
            "ONTARGET Study - Cardiovascular Risk Reduction",
            "TRANSCEND Study - Cardiovascular Risk Reduction",
            "KDIGO Guidelines - Chronic Kidney Disease",
            "WHO Essential Medicines List"
        ],
        "last_updated": "2025-02-18",
    },

    "Valsartan": {
        "group": "Cardiovascular - ARB (Angiotensin Receptor Blocker)",
        "vietnamese_name": "Valsartan, Diovan",
        "administration": ["PO"],
        "indications": [
            "Tăng huyết áp",
            "Suy tim (không dung nạp ACE inhibitor)",
            "Sau nhồi máu cơ tim",
            "Bảo vệ thận trong đái tháo đường"
        ],
        "contraindications": [
            "Dị ứng ARB",
            "Có thai",
            "Hẹp động mạch thận 2 bên"
        ],
        "dosage": {
            "adult_htn": "80-320mg x 1 lần/ngày",
            "adult_heart_failure": "40mg x 2 lần/ngày, tăng đến 160mg x 2 lần/ngày",
            "adult_post_mi": "20mg x 2 lần/ngày, tăng đến 160mg x 2 lần/ngày",
            "notes": "Ít gây ho hơn ACE inhibitor"
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "Liều khởi đầu 40mg/ngày",
            "under_30": "Thận trọng, theo dõi sát"
        },
        "side_effects": [
            "Ít tác dụng phụ hơn ACE inhibitor",
            "Ho ít hơn ACE inhibitor",
            "Tăng kali máu (ít hơn ACE)",
            "Hạ huyết áp",
            "Chóng mặt"
        ],
        "interactions": [
            "Kali: tăng kali máu",
            "NSAID: giảm hiệu quả",
            "Lithium: tăng nồng độ lithium"
        ],
        "pregnancy": "D - Chống chỉ định trong thai kỳ",
        "risk_flags": {
            "high_alert": False,
            "narrow_therapeutic_index": False,
            "icu_critical_care_only": False,
            "bleeding_risk": "Low",
            "organ_toxicity": ["hyperkalemia", "renal_impairment", "angioedema"]
        },
        "guideline_tags": [
            "ACC/AHA/HFSA HFrEF ARB Class I/IIa (ACEi intolerant)",
            "ESC HFrEF ARB Class I/IIa (ACEi intolerant)"
        ],
        "mechanism_of_action": "Ức chế thụ thể angiotensin II type 1 (AT1), ngăn chặn tác dụng của angiotensin II (giãn mạch, giảm aldosterone). Ít gây ho hơn ACE inhibitor vì không ảnh hưởng đến bradykinin.",
        "monitoring": [
            "Creatinine, BUN sau 1-2 tuần khi bắt đầu",
            "Kali máu định kỳ",
            "Huyết áp",
            "Dấu hiệu phù mạch (hiếm hơn ACE inhibitor)"
        ],
        "precautions": [
            "Khởi đầu với liều thấp, tăng dần",
            "Ưu điểm: ít gây ho hơn ACE inhibitor",
            "Theo dõi sát creatinine khi bắt đầu",
            "Tránh dùng với NSAID",
            "Ngừng ngay nếu có phù mạch"
        ],
        "pharmacokinetics": {
            "half_life": "6 giờ",
            "onset": "2 giờ",
            "duration": "24 giờ",
            "protein_binding": "95%",
            "metabolism": "Chuyển hóa ít",
            "clearance": "Chủ yếu qua thận (70%), cần điều chỉnh thận"
        },
        "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm",
        "black_box_warnings": "Chống chỉ định trong thai kỳ - có thể gây dị tật thai nhi và tử vong thai nhi.",
        "references": {
            "primary_sources": [
                "FDA Drug Label - Valsartan (Diovan)",
                "UpToDate - Valsartan: Drug Information",
                "VALIANT Trial - The New England Journal of Medicine"
            ],
            "last_updated": "2025-02-18",
            "evidence_level": "A"
        },
        "risk_flags": {
            "high_alert": False,
            "narrow_therapeutic_index": False,
            "icu_critical_care_only": False,
            "bleeding_risk": "Low",
            "organ_toxicity": {"metabolic": "Moderate (hyperkalemia)", "renal": "Moderate"}
        },
        "guideline_tags": [
            "ACC/AHA/HFSA Guidelines - Heart Failure with Reduced Ejection Fraction",
            "ESC Guidelines - Heart Failure",
            "ACC/AHA Guidelines - Hypertension",
            "VALIANT Trial - Post-Myocardial Infarction",
            "WHO Essential Medicines List"
        ],
        "last_updated": "2025-02-18",
        "drug_interactions": {
            "major": [],
            "moderate": [],
            "minor": []
        },
        "pregnancy_lactation": {
            "fda_category": "",
            "pregnancy_details": "",
            "lactation_details": ""
        },
        "hepatic_adjustment": {
            "mild": "",
            "moderate": "",
            "severe": ""
        },
        "overdose_management": {
            "symptoms": [],
            "treatment": "",
            "antidote": None
        },
        "reversal_agents": {
            "available": False,
            "agents": [],
            "notes": ""
        },
        "administration_instructions": {
            "preparation": "",
            "administration": "",
            "monitoring": []
        },
    },

}

__all__ = ['ARBS']
