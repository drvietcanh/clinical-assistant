"""
ACE Inhibitors and ARBs (Thuốc ức chế men chuyển và chẹn thụ thể Angiotensin)
Thuốc hạ huyết áp, suy tim, bảo vệ thận.
"""

ACE_ARB_DRUGS = {
    "Lisinopril": {
        "group": "Cardiovascular - ACE Inhibitor",
        "vietnamese_name": "Lisinopril, Zestril",
        "brand_names": {
            "common": ["Prinivil", "Zestril"],
            "vietnam": ["Lisinopril 5/10/20mg"]
        },
        "administration": ["PO"],
        "indications": [
            "Tăng huyết áp (Hypertension)",
            "Suy tim (Heart Failure)",
            "Sau nhồi máu cơ tim (Post-MI)",
            "Bệnh thận đái tháo đường (Diabetic nephropathy)"
        ],
        "dosage": {
            "hypertension": "Khởi đầu 10mg PO x 1 lần/ngày. Tối đa 40mg/ngày.",
            "heart_failure": "Khởi đầu 2.5-5mg PO x 1 lần/ngày, tăng dần đến 20-40mg/ngày.",
            "notes": "Uống buổi sáng. Không cần uống cùng thức ăn."
        },
        "side_effects": [
            "Ho khan (10-20%) - Tác dụng phụ đặc trưng của ACE-I",
            "Hạ huyết áp (đặc biệt liều đầu)",
            "Tăng Kali máu (Hyperkalemia)",
            "Suy thận cấp (ở bệnh nhân hẹp động mạch thận 2 bên)",
            "Phù mạch (Angioedema) - Hiếm nhưng nguy hiểm"
        ],
        "contraindications": [
            "Có thai (Gây quái thai, tổn thương thai nhi)",
            "Tiền sử phù mạch (Angioedema)",
            "Hẹp động mạch thận 2 bên"
        ],
        "contraindications_detail": {
            "tuyệt_đối": [
                "Có thai (Gây quái thai, tổn thương thai nhi)",
                "Tiền sử phù mạch (Angioedema)",
                "Hẹp động mạch thận 2 bên"
            ],
            "tương_đối": [
                "Suy thận - thận trọng, theo dõi creatinine",
                "Tăng Kali máu - thận trọng",
                "Bệnh nhân cao tuổi - khởi đầu liều thấp"
            ]
        },
        "interactions": [
            "Thuốc giữ Kali (Spironolactone, Amiloride), Bổ sung Kali: Tăng nguy cơ tăng Kali máu.",
            "NSAIDs: Giảm hiệu quả hạ huyết áp, tăng nguy cơ suy thận.",
            "Lithium: Tăng nồng độ Lithium."
        ],
        "pregnancy": "D - Chống chỉ định tuyệt đối trong thai kỳ. Gây quái thai, oligohydramnios, suy thận và dị tật xương thai nhi.",
        "drug_interactions": {
            "major": [
                {
                    "drug": "Spironolactone, Amiloride, Triamterene",
                    "mechanism": "Cả hai đều giữ Kali",
                    "effect": "Tăng nguy cơ tăng Kali máu nghiêm trọng",
                    "management": "Tránh dùng cùng. Nếu cần, theo dõi Kali máu thường xuyên."
                },
                {
                    "drug": "NSAIDs (Ibuprofen, Naproxen, etc.)",
                    "mechanism": "Giảm tác dụng hạ huyết áp, tăng nguy cơ suy thận",
                    "effect": "Giảm hiệu quả điều trị, suy thận cấp",
                    "management": "Tránh dùng thường xuyên. Theo dõi chức năng thận."
                }
            ],
            "moderate": [
                {
                    "drug": "Lithium",
                    "mechanism": "ACE-I giảm thải trừ Lithium",
                    "effect": "Tăng nồng độ Lithium, tăng nguy cơ độc tính",
                    "management": "Theo dõi nồng độ Lithium. Có thể cần giảm liều Lithium."
                }
            ],
            "minor": []
        },
        "renal_adjustment": {
            "normal": "Không cần chỉnh liều",
            "30_60": "Thận trọng, có thể cần giảm liều. Khởi đầu liều thấp hơn.",
            "under_30": "Thận trọng, giảm liều (thải trừ qua thận)",
            "dialysis": "Thận trọng, giảm liều. Lisinopril không được lọc sạch hiệu quả qua thẩm phân máu.",
            "notes": "Lisinopril thải trừ qua thận. Suy thận có thể tăng nguy cơ tích lũy và tăng Kali máu."
        },
        "reversal_agents": {
            "available": False,
            "agents": [],
            "notes": "Không có antidote đặc hiệu. Điều trị quá liều chủ yếu là hỗ trợ: ngừng thuốc, bù dịch nếu hạ huyết áp, điều chỉnh điện giải."
        },
        "mechanism_of_action": "Ức chế ACE (Angiotensin Converting Enzyme) → Giảm Angiotensin II → Giãn mạch, giảm huyết áp. Giảm Aldosterone → Giảm giữ nước/natri. Bảo vệ tim, thận.",
        "monitoring": [
            "Huyết áp",
            "Kali máu - Sau 1-2 tuần điều trị",
            "Creatinine, eGFR - Sau 1-2 tuần",
            "Dấu hiệu ho khan"
        ],
        "precautions": [
            "Kiểm tra Kali, Creatinine sau 1-2 tuần điều trị",
            "Tránh thai - Gây quái thai (ngừng ngay nếu mang thai)",
            "Ho khan (10-20%) - Nếu không dung nạp, chuyển sang ARB",
            "Nguy cơ phù mạch - Ngừng thuốc ngay nếu sưng môi, lưỡi, khó thở",
            "Thận trọng ở suy thận, tăng Kali máu",
            "Tránh dùng NSAIDs"
        ],
        "black_box_warnings": "Gây quái thai. Chống chỉ định ở thai kỳ.",
        "risk_flags": {
            "high_alert": True,
            "narrow_therapeutic_index": False,
            "icu_critical_care_only": False,
            "bleeding_risk": "Low",
            "organ_toxicity": {"renal": "Moderate", "pregnancy": "D - Chống chỉ định trong thai kỳ do nguy cơ gây hại cho thai nhi (oligohydramnios, thận suy, dị tật xương)"}
        },
        "guideline_tags": [
            "AHA/ACC 2017 Hypertension Guidelines",
            "AHA/ACC/HFSA 2022 Heart Failure Guidelines",
            "KDIGO 2021 Chronic Kidney Disease Guidelines",
            "ACC/AHA 2013 Post-MI Guidelines"
        ],
        "pregnancy_lactation": {
            "fda_category": "D",
            "pregnancy_details": "Chống chỉ định tuyệt đối trong thai kỳ. Gây quái thai, oligohydramnios (thiếu ối), suy thận và dị tật xương thai nhi. Ngừng ngay khi phát hiện có thai.",
            "lactation_details": "Không rõ liệu có bài tiết vào sữa mẹ. Thận trọng khi cho con bú. Có thể gây hạ huyết áp ở trẻ bú mẹ."
        },
        "hepatic_adjustment": {
            "mild": "Không cần chỉnh liều",
            "moderate": "Thận trọng, có thể cần giảm liều",
            "severe": "Thận trọng, giảm liều. Lisinopril chuyển hóa một phần qua gan."
        },
        "overdose_management": {
            "symptoms": ["Hạ huyết áp nghiêm trọng", "Tăng Kali máu", "Suy thận cấp", "Chóng mặt", "Ngất"],
            "treatment": "Ngừng thuốc ngay. Bù dịch IV nếu hạ huyết áp. Điều chỉnh Kali máu nếu tăng. Lọc máu nếu cần.",
            "antidote": None
        },
        "administration_instructions": {
            "preparation": "Viên nén, uống nguyên viên với nước",
            "administration": "Uống buổi sáng, có thể uống trước hoặc sau ăn. Không cần uống cùng thức ăn.",
            "monitoring": ["Huyết áp sau 1-2 tuần", "Kali máu sau 1-2 tuần", "Creatinine sau 1-2 tuần"]
        },
        "pharmacokinetics": {
            "half_life": "12 giờ",
            "onset": "1 giờ (đạt đỉnh sau 6-8 giờ)",
            "duration": "24 giờ",
            "protein_binding": "25%",
            "clearance": "Thải trừ qua thận (không chuyển hóa). Suy thận kéo dài thời gian bán hủy."
        },
        "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm. Giữ trong bao bì gốc.",
        "references": {
            "primary": ["FDA Label - Lisinopril", "Micromedex - Lisinopril"],
            "guidelines": ["AHA/ACC 2017 Hypertension Guidelines", "AHA/ACC/HFSA 2022 Heart Failure Guidelines", "KDIGO 2021 CKD Guidelines"],
            "other": []
        },
    },

    "Enalapril": {
        "group": "Cardiovascular - ACE Inhibitor",
        "vietnamese_name": "Enalapril, Vasotec",
        "brand_names": {
            "common": ["Vasotec"],
            "vietnam": ["Enalapril 5/10mg"]
        },
        "administration": ["PO", "IV"],
        "indications": [
            "Tương tự Lisinopril"
        ],
        "dosage": {
            "hypertension": "Khởi đầu 5mg PO x 1-2 lần/ngày. Tối đa 40mg/ngày.",
            "heart_failure": "Khởi đầu 2.5mg PO x 2 lần/ngày, tăng dần."
        },
        "side_effects": [
            "Tương tự Lisinopril"
        ],
        "contraindications": [
            "Có thai (Gây quái thai, tổn thương thai nhi)",
            "Tiền sử phù mạch (Angioedema)",
            "Hẹp động mạch thận 2 bên"
        ],
        "contraindications_detail": {
            "tuyệt_đối": [
                "Có thai (Gây quái thai, tổn thương thai nhi)",
                "Tiền sử phù mạch (Angioedema)",
                "Hẹp động mạch thận 2 bên"
            ],
            "tương_đối": [
                "Suy thận - thận trọng, theo dõi creatinine",
                "Tăng Kali máu - thận trọng",
                "Bệnh nhân cao tuổi - khởi đầu liều thấp"
            ]
        },
        "interactions": [
            "Thuốc giữ Kali (Spironolactone, Amiloride), Bổ sung Kali: Tăng nguy cơ tăng Kali máu.",
            "NSAIDs: Giảm hiệu quả hạ huyết áp, tăng nguy cơ suy thận.",
            "Lithium: Tăng nồng độ Lithium."
        ],
        "pregnancy": "D - Chống chỉ định tuyệt đối trong thai kỳ. Gây quái thai, oligohydramnios, suy thận và dị tật xương thai nhi.",
        "drug_interactions": {
            "major": [
                {
                    "drug": "Spironolactone, Amiloride, Triamterene",
                    "mechanism": "Cả hai đều giữ Kali",
                    "effect": "Tăng nguy cơ tăng Kali máu nghiêm trọng",
                    "management": "Tránh dùng cùng. Nếu cần, theo dõi Kali máu thường xuyên."
                },
                {
                    "drug": "NSAIDs (Ibuprofen, Naproxen, etc.)",
                    "mechanism": "Giảm tác dụng hạ huyết áp, tăng nguy cơ suy thận",
                    "effect": "Giảm hiệu quả điều trị, suy thận cấp",
                    "management": "Tránh dùng thường xuyên. Theo dõi chức năng thận."
                }
            ],
            "moderate": [
                {
                    "drug": "Lithium",
                    "mechanism": "ACE-I giảm thải trừ Lithium",
                    "effect": "Tăng nồng độ Lithium, tăng nguy cơ độc tính",
                    "management": "Theo dõi nồng độ Lithium. Có thể cần giảm liều Lithium."
                }
            ],
            "minor": []
        },
        "renal_adjustment": {
            "normal": "Không cần chỉnh liều",
            "30_60": "Thận trọng, có thể cần giảm liều. Khởi đầu liều thấp hơn.",
            "under_30": "Thận trọng, giảm liều (thải trừ qua thận)",
            "dialysis": "Thận trọng, giảm liều. Enalapril không được lọc sạch hiệu quả qua thẩm phân máu.",
            "notes": "Enalapril thải trừ qua thận. Suy thận có thể tăng nguy cơ tích lũy và tăng Kali máu."
        },
        "reversal_agents": {
            "available": False,
            "agents": [],
            "notes": "Không có antidote đặc hiệu. Điều trị quá liều chủ yếu là hỗ trợ: ngừng thuốc, bù dịch nếu hạ huyết áp, điều chỉnh điện giải."
        },
        "mechanism_of_action": "Tương tự Lisinopril. Có dạng IV (Enalaprilat) cho cấp cứu tăng huyết áp.",
        "risk_flags": {
            "high_alert": True,
            "narrow_therapeutic_index": False,
            "icu_critical_care_only": False,
            "bleeding_risk": "Low",
            "organ_toxicity": {"renal": "Moderate", "pregnancy": "D - Chống chỉ định trong thai kỳ do nguy cơ gây hại cho thai nhi (oligohydramnios, thận suy, dị tật xương)"}
        },
        "guideline_tags": [
            "AHA/ACC 2017 Hypertension Guidelines",
            "AHA/ACC/HFSA 2022 Heart Failure Guidelines",
            "KDIGO 2021 Chronic Kidney Disease Guidelines",
            "ACC/AHA 2013 Post-MI Guidelines"
        ],
        "pregnancy_lactation": {
            "fda_category": "D",
            "pregnancy_details": "Chống chỉ định tuyệt đối trong thai kỳ. Gây quái thai, oligohydramnios (thiếu ối), suy thận và dị tật xương thai nhi. Ngừng ngay khi phát hiện có thai.",
            "lactation_details": "Không rõ liệu có bài tiết vào sữa mẹ. Thận trọng khi cho con bú. Có thể gây hạ huyết áp ở trẻ bú mẹ."
        },
        "hepatic_adjustment": {
            "mild": "Không cần chỉnh liều",
            "moderate": "Thận trọng, có thể cần giảm liều",
            "severe": "Thận trọng, giảm liều. Enalapril chuyển hóa qua gan thành enalaprilat."
        },
        "overdose_management": {
            "symptoms": ["Hạ huyết áp nghiêm trọng", "Tăng Kali máu", "Suy thận cấp", "Chóng mặt", "Ngất"],
            "treatment": "Ngừng thuốc ngay. Bù dịch IV nếu hạ huyết áp. Điều chỉnh Kali máu nếu tăng. Lọc máu nếu cần.",
            "antidote": None
        },
        "administration_instructions": {
            "preparation": "Viên nén PO hoặc dung dịch IV (Enalaprilat)",
            "administration": "PO: Uống buổi sáng, có thể uống trước hoặc sau ăn. IV: Enalaprilat 1.25mg mỗi 6 giờ cho cấp cứu tăng huyết áp.",
            "monitoring": ["Huyết áp sau 1-2 tuần", "Kali máu sau 1-2 tuần", "Creatinine sau 1-2 tuần"]
        },
        "pharmacokinetics": {
            "half_life": "11 giờ (Enalaprilat - chất chuyển hóa hoạt tính)",
            "onset": "1 giờ PO (đạt đỉnh sau 4-6 giờ), 15 phút IV",
            "duration": "24 giờ",
            "protein_binding": "50-60%",
            "clearance": "Chuyển hóa qua gan thành Enalaprilat (hoạt tính), thải trừ qua thận."
        },
        "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm. Giữ trong bao bì gốc.",
        "references": {
            "primary": ["FDA Label - Enalapril", "Micromedex - Enalapril"],
            "guidelines": ["AHA/ACC 2017 Hypertension Guidelines", "AHA/ACC/HFSA 2022 Heart Failure Guidelines", "KDIGO 2021 CKD Guidelines"],
            "other": []
        },
        "precautions": [
            "Kiểm tra Kali, Creatinine sau 1-2 tuần điều trị",
            "Tránh thai - Gây quái thai (ngừng ngay nếu mang thai)",
            "Ho khan (10-20%) - Nếu không dung nạp, chuyển sang ARB",
            "Nguy cơ phù mạch - Ngừng thuốc ngay nếu sưng môi, lưỡi, khó thở",
            "Thận trọng ở suy thận, tăng Kali máu",
            "Tránh dùng NSAIDs"
        ],
        "black_box_warnings": "Gây quái thai. Chống chỉ định ở thai kỳ.",
        "monitoring": [
            "Huyết áp",
            "Kali máu - Sau 1-2 tuần điều trị",
            "Creatinine, eGFR - Sau 1-2 tuần",
            "Dấu hiệu ho khan"
        ],
    },

    "Losartan": {
        "group": "Cardiovascular - ARB (Angiotensin Receptor Blocker)",
        "vietnamese_name": "Losartan, Cozaar",
        "brand_names": {
            "common": ["Cozaar"],
            "vietnam": ["Losartan 50/100mg"]
        },
        "administration": ["PO"],
        "indications": [
            "Tăng huyết áp",
            "Suy tim",
            "Bệnh thận đái tháo đường",
            "Phòng ngừa đột quỵ (ở tăng huyết áp + phì đại thất trái)"
        ],
        "dosage": {
            "hypertension": "Khởi đầu 50mg PO x 1 lần/ngày. Tối đa 100mg/ngày.",
            "heart_failure": "Khởi đầu 25mg PO x 1 lần/ngày, tăng dần đến 50-100mg/ngày."
        },
        "side_effects": [
            "KHÔNG gây ho khan (khác ACE-I) - Ưu điểm lớn",
            "Hạ huyết áp",
            "Tăng Kali máu",
            "Suy thận cấp",
            "Phù mạch (Hiếm hơn ACE-I)"
        ],
        "contraindications": [
            "Có thai (Gây quái thai)",
            "Hẹp động mạch thận 2 bên"
        ],
        "contraindications_detail": {
            "tuyệt_đối": [
                "Có thai (Gây quái thai)",
                "Hẹp động mạch thận 2 bên"
            ],
            "tương_đối": [
                "Suy thận - thận trọng, theo dõi creatinine",
                "Tăng Kali máu - thận trọng",
                "Bệnh nhân cao tuổi - khởi đầu liều thấp"
            ]
        },
        "interactions": [
            "Thuốc giữ Kali (Spironolactone, Amiloride), Bổ sung Kali: Tăng nguy cơ tăng Kali máu.",
            "NSAIDs: Giảm hiệu quả hạ huyết áp, tăng nguy cơ suy thận.",
            "Lithium: Tăng nồng độ Lithium."
        ],
        "pregnancy": "D - Chống chỉ định tuyệt đối trong thai kỳ. Gây quái thai, oligohydramnios, suy thận và dị tật xương thai nhi.",
        "drug_interactions": {
            "major": [
                {
                    "drug": "Spironolactone, Amiloride, Triamterene",
                    "mechanism": "Cả hai đều giữ Kali",
                    "effect": "Tăng nguy cơ tăng Kali máu nghiêm trọng",
                    "management": "Tránh dùng cùng. Nếu cần, theo dõi Kali máu thường xuyên."
                },
                {
                    "drug": "NSAIDs (Ibuprofen, Naproxen, etc.)",
                    "mechanism": "Giảm tác dụng hạ huyết áp, tăng nguy cơ suy thận",
                    "effect": "Giảm hiệu quả điều trị, suy thận cấp",
                    "management": "Tránh dùng thường xuyên. Theo dõi chức năng thận."
                }
            ],
            "moderate": [
                {
                    "drug": "Lithium",
                    "mechanism": "ARB có thể giảm thải trừ Lithium",
                    "effect": "Tăng nồng độ Lithium, tăng nguy cơ độc tính",
                    "management": "Theo dõi nồng độ Lithium. Có thể cần giảm liều Lithium."
                }
            ],
            "minor": []
        },
        "renal_adjustment": {
            "normal": "Không cần chỉnh liều",
            "30_60": "Thận trọng, có thể cần giảm liều. Khởi đầu liều thấp hơn.",
            "under_30": "Thận trọng, giảm liều (thải trừ qua thận)",
            "dialysis": "Thận trọng, giảm liều. Losartan không được lọc sạch hiệu quả qua thẩm phân máu.",
            "notes": "Losartan thải trừ qua thận. Suy thận có thể tăng nguy cơ tích lũy và tăng Kali máu."
        },
        "reversal_agents": {
            "available": False,
            "agents": [],
            "notes": "Không có antidote đặc hiệu. Điều trị quá liều chủ yếu là hỗ trợ: ngừng thuốc, bù dịch nếu hạ huyết áp, điều chỉnh điện giải."
        },
        "mechanism_of_action": "Chẹn thụ thể Angiotensin II (AT1) → Giãn mạch, giảm huyết áp. Tác dụng tương tự ACE-I nhưng KHÔNG gây ho khan. Thường dùng thay thế ACE-I khi không dung nạp ho.",
        "monitoring": [
            "Huyết áp",
            "Kali máu",
            "Creatinine, eGFR"
        ],
        "precautions": [
            "Tương tự ACE-I",
            "KHÔNG gây ho khan - Ưu điểm lớn so với ACE-I",
            "Dùng thay thế ACE-I khi không dung nạp ho",
            "Tránh thai - Gây quái thai"
        ],
        "black_box_warnings": "Gây quái thai. Chống chỉ định ở thai kỳ.",
        "risk_flags": {
            "high_alert": True,
            "narrow_therapeutic_index": False,
            "icu_critical_care_only": False,
            "bleeding_risk": "Low",
            "organ_toxicity": {"renal": "Moderate", "pregnancy": "D - Chống chỉ định trong thai kỳ do nguy cơ gây hại cho thai nhi (oligohydramnios, thận suy, dị tật xương)"}
        },
        "guideline_tags": [
            "AHA/ACC 2017 Hypertension Guidelines",
            "AHA/ACC/HFSA 2022 Heart Failure Guidelines",
            "KDIGO 2021 Chronic Kidney Disease Guidelines",
            "AHA/ASA 2021 Stroke Prevention Guidelines"
        ],
        "pregnancy_lactation": {
            "fda_category": "D",
            "pregnancy_details": "Chống chỉ định tuyệt đối trong thai kỳ. Gây quái thai, oligohydramnios (thiếu ối), suy thận và dị tật xương thai nhi. Ngừng ngay khi phát hiện có thai.",
            "lactation_details": "Không rõ liệu có bài tiết vào sữa mẹ. Thận trọng khi cho con bú. Có thể gây hạ huyết áp ở trẻ bú mẹ."
        },
        "hepatic_adjustment": {
            "mild": "Không cần chỉnh liều",
            "moderate": "Thận trọng, có thể cần giảm liều",
            "severe": "Thận trọng, giảm liều. Losartan chuyển hóa qua gan thành chất chuyển hóa hoạt tính."
        },
        "overdose_management": {
            "symptoms": ["Hạ huyết áp nghiêm trọng", "Tăng Kali máu", "Suy thận cấp", "Chóng mặt", "Ngất"],
            "treatment": "Ngừng thuốc ngay. Bù dịch IV nếu hạ huyết áp. Điều chỉnh Kali máu nếu tăng. Lọc máu nếu cần.",
            "antidote": None
        },
        "administration_instructions": {
            "preparation": "Viên nén, uống nguyên viên với nước",
            "administration": "Uống buổi sáng, có thể uống trước hoặc sau ăn. Không cần uống cùng thức ăn.",
            "monitoring": ["Huyết áp sau 1-2 tuần", "Kali máu sau 1-2 tuần", "Creatinine sau 1-2 tuần"]
        },
        "pharmacokinetics": {
            "half_life": "2 giờ (Losartan), 6-9 giờ (chất chuyển hóa hoạt tính)",
            "onset": "1 giờ (đạt đỉnh sau 1 giờ)",
            "duration": "24 giờ",
            "protein_binding": "98.7%",
            "clearance": "Chuyển hóa qua gan (CYP2C9, CYP3A4) thành chất chuyển hóa hoạt tính, thải trừ qua thận và phân."
        },
        "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm. Giữ trong bao bì gốc.",
        "references": {
            "primary": ["FDA Label - Losartan", "Micromedex - Losartan"],
            "guidelines": ["AHA/ACC 2017 Hypertension Guidelines", "AHA/ACC/HFSA 2022 Heart Failure Guidelines", "KDIGO 2021 CKD Guidelines"],
            "other": []
        },
    },

    "Valsartan": {
        "group": "Cardiovascular - ARB",
        "vietnamese_name": "Valsartan, Diovan",
        "brand_names": {
            "common": ["Diovan"],
            "vietnam": ["Valsartan 80/160mg"]
        },
        "administration": ["PO"],
        "indications": [
            "Tương tự Losartan"
        ],
        "dosage": {
            "hypertension": "Khởi đầu 80-160mg PO x 1 lần/ngày. Tối đa 320mg/ngày.",
            "heart_failure": "Khởi đầu 40mg PO x 2 lần/ngày, tăng dần đến 160mg x 2 lần/ngày."
        },
        "side_effects": [
            "Tương tự Losartan"
        ],
        "contraindications": [
            "Có thai (Gây quái thai)",
            "Hẹp động mạch thận 2 bên"
        ],
        "contraindications_detail": {
            "tuyệt_đối": [
                "Có thai (Gây quái thai)",
                "Hẹp động mạch thận 2 bên"
            ],
            "tương_đối": [
                "Suy thận - thận trọng, theo dõi creatinine",
                "Tăng Kali máu - thận trọng",
                "Bệnh nhân cao tuổi - khởi đầu liều thấp"
            ]
        },
        "interactions": [
            "Thuốc giữ Kali (Spironolactone, Amiloride), Bổ sung Kali: Tăng nguy cơ tăng Kali máu.",
            "NSAIDs: Giảm hiệu quả hạ huyết áp, tăng nguy cơ suy thận."
        ],
        "pregnancy": "D - Chống chỉ định tuyệt đối trong thai kỳ. Gây quái thai, oligohydramnios, suy thận và dị tật xương thai nhi.",
        "drug_interactions": {
            "major": [
                {
                    "drug": "Spironolactone, Amiloride, Triamterene",
                    "mechanism": "Cả hai đều giữ Kali",
                    "effect": "Tăng nguy cơ tăng Kali máu nghiêm trọng",
                    "management": "Tránh dùng cùng. Nếu cần, theo dõi Kali máu thường xuyên."
                },
                {
                    "drug": "NSAIDs (Ibuprofen, Naproxen, etc.)",
                    "mechanism": "Giảm tác dụng hạ huyết áp, tăng nguy cơ suy thận",
                    "effect": "Giảm hiệu quả điều trị, suy thận cấp",
                    "management": "Tránh dùng thường xuyên. Theo dõi chức năng thận."
                }
            ],
            "moderate": [],
            "minor": []
        },
        "renal_adjustment": {
            "normal": "Không cần chỉnh liều",
            "30_60": "Thận trọng, có thể cần giảm liều. Khởi đầu liều thấp hơn.",
            "under_30": "Thận trọng, giảm liều (thải trừ qua thận)",
            "dialysis": "Thận trọng, giảm liều. Valsartan không được lọc sạch hiệu quả qua thẩm phân máu.",
            "notes": "Valsartan thải trừ qua thận. Suy thận có thể tăng nguy cơ tích lũy và tăng Kali máu."
        },
        "reversal_agents": {
            "available": False,
            "agents": [],
            "notes": "Không có antidote đặc hiệu. Điều trị quá liều chủ yếu là hỗ trợ: ngừng thuốc, bù dịch nếu hạ huyết áp, điều chỉnh điện giải."
        },
        "mechanism_of_action": "Chẹn thụ thể Angiotensin II (AT1) → Giãn mạch, giảm huyết áp. Tác dụng tương tự Losartan nhưng có thời gian bán hủy dài hơn.",
        "monitoring": [
            "Huyết áp",
            "Kali máu - Sau 1-2 tuần điều trị",
            "Creatinine, eGFR - Sau 1-2 tuần"
        ],
        "precautions": [
            "Kiểm tra Kali, Creatinine sau 1-2 tuần điều trị",
            "Tránh thai - Gây quái thai (ngừng ngay nếu mang thai)",
            "KHÔNG gây ho khan - Ưu điểm so với ACE-I",
            "Thận trọng ở suy thận, tăng Kali máu",
            "Tránh dùng NSAIDs"
        ],
        "black_box_warnings": "Gây quái thai. Chống chỉ định ở thai kỳ.",
        "risk_flags": {
            "high_alert": True,
            "narrow_therapeutic_index": False,
            "icu_critical_care_only": False,
            "bleeding_risk": "Low",
            "organ_toxicity": {"renal": "Moderate", "pregnancy": "D - Chống chỉ định trong thai kỳ do nguy cơ gây hại cho thai nhi"}
        },
        "guideline_tags": [
            "AHA/ACC 2017 Hypertension Guidelines",
            "AHA/ACC/HFSA 2022 Heart Failure Guidelines",
            "KDIGO 2021 Chronic Kidney Disease Guidelines"
        ],
        "pregnancy_lactation": {
            "fda_category": "D",
            "pregnancy_details": "Chống chỉ định tuyệt đối trong thai kỳ. Gây quái thai, oligohydramnios (thiếu ối), suy thận và dị tật xương thai nhi. Ngừng ngay khi phát hiện có thai.",
            "lactation_details": "Không rõ liệu có bài tiết vào sữa mẹ. Thận trọng khi cho con bú. Có thể gây hạ huyết áp ở trẻ bú mẹ."
        },
        "hepatic_adjustment": {
            "mild": "Không cần chỉnh liều",
            "moderate": "Thận trọng, có thể cần giảm liều",
            "severe": "Thận trọng, giảm liều. Valsartan chuyển hóa một phần qua gan."
        },
        "overdose_management": {
            "symptoms": ["Hạ huyết áp nghiêm trọng", "Tăng Kali máu", "Suy thận cấp", "Chóng mặt", "Ngất"],
            "treatment": "Ngừng thuốc ngay. Bù dịch IV nếu hạ huyết áp. Điều chỉnh Kali máu nếu tăng. Lọc máu nếu cần.",
            "antidote": None
        },
        "administration_instructions": {
            "preparation": "Viên nén, uống nguyên viên với nước",
            "administration": "Uống buổi sáng, có thể uống trước hoặc sau ăn. Không cần uống cùng thức ăn.",
            "monitoring": ["Huyết áp sau 1-2 tuần", "Kali máu sau 1-2 tuần", "Creatinine sau 1-2 tuần"]
        },
        "pharmacokinetics": {
            "half_life": "6 giờ",
            "onset": "2 giờ (đạt đỉnh sau 2-4 giờ)",
            "duration": "24 giờ",
            "protein_binding": "94-97%",
            "clearance": "Chuyển hóa qua gan (CYP2C9), thải trừ qua thận và phân."
        },
        "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm. Giữ trong bao bì gốc.",
        "references": {
            "primary": ["FDA Label - Valsartan", "Micromedex - Valsartan"],
            "guidelines": ["AHA/ACC 2017 Hypertension Guidelines", "AHA/ACC/HFSA 2022 Heart Failure Guidelines", "KDIGO 2021 CKD Guidelines"],
            "other": []
        },
    },

    "Telmisartan": {
        "group": "Cardiovascular - ARB",
        "vietnamese_name": "Telmisartan, Micardis",
        "brand_names": {
            "common": ["Micardis"],
            "vietnam": ["Telmisartan 40/80mg"]
        },
        "administration": ["PO"],
        "indications": [
            "Tương tự Losartan"
        ],
        "dosage": {
            "hypertension": "Khởi đầu 40mg PO x 1 lần/ngày. Tối đa 80mg/ngày."
        },
        "side_effects": [
            "Tương tự Losartan"
        ],
        "contraindications": [
            "Có thai (Gây quái thai)",
            "Hẹp động mạch thận 2 bên"
        ],
        "contraindications_detail": {
            "tuyệt_đối": [
                "Có thai (Gây quái thai)",
                "Hẹp động mạch thận 2 bên"
            ],
            "tương_đối": [
                "Suy thận - thận trọng, theo dõi creatinine",
                "Tăng Kali máu - thận trọng",
                "Bệnh nhân cao tuổi - khởi đầu liều thấp"
            ]
        },
        "interactions": [
            "Thuốc giữ Kali (Spironolactone, Amiloride), Bổ sung Kali: Tăng nguy cơ tăng Kali máu.",
            "NSAIDs: Giảm hiệu quả hạ huyết áp, tăng nguy cơ suy thận."
        ],
        "pregnancy": "D - Chống chỉ định tuyệt đối trong thai kỳ. Gây quái thai, oligohydramnios, suy thận và dị tật xương thai nhi.",
        "drug_interactions": {
            "major": [
                {
                    "drug": "Spironolactone, Amiloride, Triamterene",
                    "mechanism": "Cả hai đều giữ Kali",
                    "effect": "Tăng nguy cơ tăng Kali máu nghiêm trọng",
                    "management": "Tránh dùng cùng. Nếu cần, theo dõi Kali máu thường xuyên."
                },
                {
                    "drug": "NSAIDs (Ibuprofen, Naproxen, etc.)",
                    "mechanism": "Giảm tác dụng hạ huyết áp, tăng nguy cơ suy thận",
                    "effect": "Giảm hiệu quả điều trị, suy thận cấp",
                    "management": "Tránh dùng thường xuyên. Theo dõi chức năng thận."
                }
            ],
            "moderate": [],
            "minor": []
        },
        "renal_adjustment": {
            "normal": "Không cần chỉnh liều",
            "30_60": "Thận trọng, có thể cần giảm liều. Khởi đầu liều thấp hơn.",
            "under_30": "Thận trọng, giảm liều (thải trừ qua thận)",
            "dialysis": "Thận trọng, giảm liều. Telmisartan không được lọc sạch hiệu quả qua thẩm phân máu.",
            "notes": "Telmisartan thải trừ qua thận. Suy thận có thể tăng nguy cơ tích lũy và tăng Kali máu."
        },
        "reversal_agents": {
            "available": False,
            "agents": [],
            "notes": "Không có antidote đặc hiệu. Điều trị quá liều chủ yếu là hỗ trợ: ngừng thuốc, bù dịch nếu hạ huyết áp, điều chỉnh điện giải."
        },
        "mechanism_of_action": "ARB tác dụng kéo dài nhất (half-life 24h). Có thêm tác dụng PPAR-gamma (tương tự Pioglitazone) - Cải thiện insulin resistance nhẹ.",
        "risk_flags": {
            "high_alert": True,
            "narrow_therapeutic_index": False,
            "icu_critical_care_only": False,
            "bleeding_risk": "Low",
            "organ_toxicity": {"renal": "Moderate", "pregnancy": "D - Chống chỉ định trong thai kỳ do nguy cơ gây hại cho thai nhi"}
        },
        "guideline_tags": [
            "AHA/ACC 2017 Hypertension Guidelines",
            "AHA/ACC/HFSA 2022 Heart Failure Guidelines",
            "KDIGO 2021 Chronic Kidney Disease Guidelines"
        ],
        "pregnancy_lactation": {
            "fda_category": "D",
            "pregnancy_details": "Chống chỉ định tuyệt đối trong thai kỳ. Gây quái thai, oligohydramnios (thiếu ối), suy thận và dị tật xương thai nhi. Ngừng ngay khi phát hiện có thai.",
            "lactation_details": "Không rõ liệu có bài tiết vào sữa mẹ. Thận trọng khi cho con bú. Có thể gây hạ huyết áp ở trẻ bú mẹ."
        },
        "hepatic_adjustment": {
            "mild": "Không cần chỉnh liều",
            "moderate": "Thận trọng, có thể cần giảm liều",
            "severe": "Thận trọng, giảm liều. Telmisartan chuyển hóa qua gan."
        },
        "overdose_management": {
            "symptoms": ["Hạ huyết áp nghiêm trọng", "Tăng Kali máu", "Suy thận cấp", "Chóng mặt", "Ngất"],
            "treatment": "Ngừng thuốc ngay. Bù dịch IV nếu hạ huyết áp. Điều chỉnh Kali máu nếu tăng. Lọc máu nếu cần.",
            "antidote": None
        },
        "administration_instructions": {
            "preparation": "Viên nén, uống nguyên viên với nước",
            "administration": "Uống buổi sáng, có thể uống trước hoặc sau ăn. Không cần uống cùng thức ăn.",
            "monitoring": ["Huyết áp sau 1-2 tuần", "Kali máu sau 1-2 tuần", "Creatinine sau 1-2 tuần"]
        },
        "pharmacokinetics": {
            "half_life": "24 giờ (dài nhất trong nhóm ARB)",
            "onset": "3 giờ (đạt đỉnh sau 0.5-1 giờ)",
            "duration": "24 giờ",
            "protein_binding": ">99%",
            "clearance": "Chuyển hóa qua gan (glucuronidation), thải trừ qua phân (98%), thận (1%)."
        },
        "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm. Giữ trong bao bì gốc.",
        "references": {
            "primary": ["FDA Label - Telmisartan", "Micromedex - Telmisartan"],
            "guidelines": ["AHA/ACC 2017 Hypertension Guidelines", "AHA/ACC/HFSA 2022 Heart Failure Guidelines", "KDIGO 2021 CKD Guidelines"],
            "other": []
        },
        "precautions": [
            "Kiểm tra Kali, Creatinine sau 1-2 tuần điều trị",
            "Tránh thai - Gây quái thai (ngừng ngay nếu mang thai)",
            "KHÔNG gây ho khan - Ưu điểm so với ACE-I",
            "Tác dụng kéo dài nhất trong nhóm ARB",
            "Thận trọng ở suy thận, tăng Kali máu",
            "Tránh dùng NSAIDs"
        ],
        "black_box_warnings": "Gây quái thai. Chống chỉ định ở thai kỳ.",
        "monitoring": [
            "Huyết áp",
            "Kali máu - Sau 1-2 tuần điều trị",
            "Creatinine, eGFR - Sau 1-2 tuần"
        ],
    }
}
