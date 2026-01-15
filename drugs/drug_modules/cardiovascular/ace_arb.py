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
            "adult_htn": "Khởi đầu 10mg PO x 1 lần/ngày. Tối đa 40mg/ngày.",
            "adult_heart_failure": "Khởi đầu 2.5-5mg PO x 1 lần/ngày, tăng dần đến 20-40mg/ngày.",
            "adult_start": "10mg PO x 1 lần/ngày (tăng huyết áp), 2.5-5mg PO x 1 lần/ngày (suy tim)",
            "adult_usual": "10-40mg PO x 1 lần/ngày (tăng huyết áp), 20-40mg PO x 1 lần/ngày (suy tim)",
            "adult_max": "40mg/ngày",
            "elderly": "Khởi đầu 2.5-5mg PO x 1 lần/ngày, tăng dần. Người cao tuổi nhạy cảm hơn với tác dụng phụ.",
            "renal_adjustment_dosage": {
                "normal": "10mg PO x 1 lần/ngày, tăng dần đến 40mg/ngày",
                "30_60": "5-10mg PO x 1 lần/ngày, thận trọng tăng dần",
                "under_30": "2.5-5mg PO x 1 lần/ngày, thận trọng tăng dần",
                "dialysis": "2.5-5mg PO x 1 lần/ngày sau mỗi lần lọc máu"
            },
            "administration_route": "PO",
            "frequency": "1 lần/ngày",
            "with_food": "Không cần uống cùng thức ăn",
            "notes": "Uống buổi sáng. Không cần uống cùng thức ăn. Thải trừ qua thận, cần điều chỉnh liều ở suy thận."
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
        "mechanism_of_action": "Lisinopril là ACE inhibitor (Angiotensin Converting Enzyme inhibitor) không chứa nhóm sulfhydryl, có tác dụng kéo dài. Cơ chế tác dụng: (1) Ức chế ACE enzyme chuyển đổi Angiotensin I thành Angiotensin II - một peptide gây co mạch mạnh. Giảm Angiotensin II dẫn đến giãn mạch ngoại vi, giảm sức cản mạch máu hệ thống (SVR), và giảm huyết áp. (2) Giảm sản xuất Aldosterone từ tuyến thượng thận, dẫn đến tăng bài tiết natri và nước qua thận, giảm thể tích máu. (3) Giảm phân hủy Bradykinin (một peptide giãn mạch) do ACE cũng là enzyme phân hủy bradykinin. Tăng bradykinin góp phần giãn mạch nhưng cũng gây ho khan (tác dụng phụ đặc trưng của ACE-I). (4) Bảo vệ tim và thận: Giảm hậu gánh tim, giảm protein niệu, làm chậm tiến triển bệnh thận đái tháo đường. Lisinopril không chuyển hóa, thải trừ hoàn toàn qua thận dưới dạng nguyên chất.",
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
            "symptoms": [
                "Hạ huyết áp nghiêm trọng (có thể gây sốc)",
                "Tăng Kali máu (hyperkalemia) - có thể gây rối loạn nhịp tim",
                "Suy thận cấp (đặc biệt ở bệnh nhân hẹp động mạch thận)",
                "Chóng mặt, ngất",
                "Nhịp tim chậm (bradycardia) - phản ứng với hạ huyết áp",
                "Rối loạn nhịp tim (do tăng kali máu)"
            ],
            "antidote": "Không có antidote đặc hiệu cho ACE inhibitors",
            "treatment": [
                "Ngừng thuốc ngay lập tức",
                "Điều trị hạ huyết áp: Nằm đầu thấp, bù dịch IV (normal saline hoặc lactated Ringer's), nếu cần: dopamine hoặc norepinephrine",
                "Điều trị tăng kali máu: Nếu K+ > 5.5 mEq/L: Calcium gluconate/calcium chloride IV (bảo vệ tim), Insulin + glucose IV (chuyển kali vào tế bào), Sodium bicarbonate IV (nếu có nhiễm toan), Furosemide (nếu chức năng thận bình thường), Hemodialysis nếu tăng kali nặng không đáp ứng",
                "Theo dõi chức năng thận: Creatinine, BUN, nước tiểu",
                "Lọc máu (hemodialysis): Có thể cần thiết để loại bỏ lisinopril và điều chỉnh kali máu nếu quá liều nghiêm trọng"
            ],
            "monitoring": "Huyết áp liên tục, kali máu (mỗi 1-2 giờ), creatinine/BUN, ECG (theo dõi rối loạn nhịp do tăng kali), dấu hiệu sinh tồn, cân bằng dịch vào-ra"
        },
        "administration_instructions": {
            "oral": {
                "with_food": "Có thể uống với hoặc không thức ăn. Hấp thu không bị ảnh hưởng đáng kể bởi thức ăn.",
                "timing": "Uống 1 lần/ngày vào buổi sáng, cùng giờ mỗi ngày để duy trì nồng độ ổn định. Không cần uống cùng thức ăn. Uống nguyên viên với nước, không nghiền hoặc nhai viên nén.",
                "notes": "Uống đều đặn hàng ngày. Không ngừng đột ngột. Nếu quên liều, uống ngay khi nhớ ra, nhưng nếu gần đến liều tiếp theo thì bỏ qua liều đã quên và tiếp tục lịch trình bình thường."
            },
            "iv": {
                "reconstitution": "Không áp dụng - Lisinopril chỉ có dạng uống",
                "infusion_rate": "Không áp dụng",
                "compatibility": [],
                "incompatibility": [],
                "notes": "Lisinopril không có dạng tiêm. Nếu cần ACE inhibitor dạng IV, dùng Enalaprilat."
            }
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
            "primary_sources": [
                "FDA Drug Label - Lisinopril (Prinivil, Zestril)",
                "UpToDate - Lisinopril: Drug information",
                "Micromedex - Lisinopril",
                "Lexicomp - Lisinopril"
            ],
            "last_updated": "2025-01-20",
            "evidence_level": "A - Dựa trên FDA labeling, UpToDate, và các guidelines chính thức (AHA/ACC, KDIGO)"
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
            "Tăng huyết áp (Hypertension)",
            "Suy tim (Heart Failure) - NYHA class II-IV",
            "Sau nhồi máu cơ tim (Post-MI) - Giảm tử vong và suy tim",
            "Bệnh thận đái tháo đường (Diabetic nephropathy) - Giảm protein niệu",
            "Cơn tăng huyết áp cấp cứu (dạng IV - Enalaprilat)"
        ],
        "dosage": {
            "adult_htn": "Khởi đầu 5mg PO x 1-2 lần/ngày. Tối đa 40mg/ngày.",
            "adult_heart_failure": "Khởi đầu 2.5mg PO x 2 lần/ngày, tăng dần đến 10-20mg x 2 lần/ngày.",
            "adult_start": "5mg PO x 1-2 lần/ngày (tăng huyết áp), 2.5mg PO x 2 lần/ngày (suy tim)",
            "adult_usual": "10-20mg PO x 2 lần/ngày (tăng huyết áp), 10-20mg PO x 2 lần/ngày (suy tim)",
            "adult_max": "40mg/ngày",
            "adult_iv": "Enalaprilat 1.25mg IV mỗi 6 giờ cho cấp cứu tăng huyết áp",
            "elderly": "Khởi đầu 2.5mg PO x 1 lần/ngày, tăng dần. Người cao tuổi nhạy cảm hơn với tác dụng phụ.",
            "renal_adjustment_dosage": {
                "normal": "5-10mg PO x 1-2 lần/ngày, tăng dần đến 40mg/ngày",
                "30_60": "2.5-5mg PO x 1-2 lần/ngày, thận trọng tăng dần",
                "under_30": "2.5mg PO x 1 lần/ngày, thận trọng tăng dần",
                "dialysis": "2.5mg PO x 1 lần/ngày sau mỗi lần lọc máu"
            },
            "administration_route": "PO, IV (Enalaprilat)",
            "frequency": "1-2 lần/ngày (PO), mỗi 6 giờ (IV)",
            "with_food": "Không cần uống cùng thức ăn",
            "notes": "Có dạng IV (Enalaprilat) cho cấp cứu tăng huyết áp. Thải trừ qua thận, cần điều chỉnh liều ở suy thận."
        },
        "side_effects": [
            "Ho khan (10-20%) - Tác dụng phụ đặc trưng của ACE-I, do tăng bradykinin",
            "Hạ huyết áp (đặc biệt liều đầu hoặc IV)",
            "Tăng Kali máu (Hyperkalemia) - Đặc biệt khi dùng với thuốc giữ kali",
            "Suy thận cấp (ở bệnh nhân hẹp động mạch thận 2 bên)",
            "Phù mạch (Angioedema) - Hiếm nhưng nguy hiểm, có thể gây tắc nghẽn đường thở",
            "Chóng mặt, mệt mỏi",
            "Đau đầu",
            "Rash (phát ban)"
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
        "mechanism_of_action": "Enalapril là ACE inhibitor (Angiotensin Converting Enzyme inhibitor) dạng prodrug, được chuyển hóa trong gan thành Enalaprilat - chất hoạt tính. Cơ chế tác dụng tương tự Lisinopril: (1) Ức chế ACE enzyme chuyển đổi Angiotensin I thành Angiotensin II - một peptide gây co mạch mạnh. Giảm Angiotensin II dẫn đến giãn mạch ngoại vi, giảm sức cản mạch máu hệ thống (SVR), và giảm huyết áp. (2) Giảm sản xuất Aldosterone từ tuyến thượng thận, dẫn đến tăng bài tiết natri và nước qua thận, giảm thể tích máu. (3) Giảm phân hủy Bradykinin (một peptide giãn mạch) do ACE cũng là enzyme phân hủy bradykinin. Tăng bradykinin góp phần giãn mạch nhưng cũng gây ho khan (tác dụng phụ đặc trưng của ACE-I). (4) Bảo vệ tim và thận: Giảm hậu gánh tim, giảm protein niệu, làm chậm tiến triển bệnh thận đái tháo đường. ĐẶC ĐIỂM: Enalapril là prodrug (cần chuyển hóa thành Enalaprilat), có dạng IV (Enalaprilat) cho cấp cứu tăng huyết áp với tác dụng nhanh (15 phút). Thải trừ qua thận.",
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
            "symptoms": [
                "Hạ huyết áp nghiêm trọng (có thể gây sốc) - đặc biệt với dạng IV",
                "Tăng Kali máu (hyperkalemia) - có thể gây rối loạn nhịp tim",
                "Suy thận cấp (đặc biệt ở bệnh nhân hẹp động mạch thận)",
                "Chóng mặt, ngất",
                "Nhịp tim chậm (bradycardia) - phản ứng với hạ huyết áp",
                "Rối loạn nhịp tim (do tăng kali máu)"
            ],
            "antidote": "Không có antidote đặc hiệu cho ACE inhibitors",
            "treatment": [
                "Ngừng thuốc ngay lập tức",
                "Điều trị hạ huyết áp: Nằm đầu thấp, bù dịch IV (normal saline hoặc lactated Ringer's), nếu cần: dopamine hoặc norepinephrine",
                "Điều trị tăng kali máu: Nếu K+ > 5.5 mEq/L: Calcium gluconate/calcium chloride IV (bảo vệ tim), Insulin + glucose IV (chuyển kali vào tế bào), Sodium bicarbonate IV (nếu có nhiễm toan), Furosemide (nếu chức năng thận bình thường), Hemodialysis nếu tăng kali nặng không đáp ứng",
                "Theo dõi chức năng thận: Creatinine, BUN, nước tiểu",
                "Lọc máu (hemodialysis): Có thể cần thiết để loại bỏ enalaprilat và điều chỉnh kali máu nếu quá liều nghiêm trọng"
            ],
            "monitoring": "Huyết áp liên tục (đặc biệt với dạng IV), kali máu (mỗi 1-2 giờ), creatinine/BUN, ECG (theo dõi rối loạn nhịp do tăng kali), dấu hiệu sinh tồn, cân bằng dịch vào-ra"
        },
        "administration_instructions": {
            "oral": {
                "with_food": "Có thể uống với hoặc không thức ăn. Hấp thu không bị ảnh hưởng đáng kể bởi thức ăn.",
                "timing": "Uống 1-2 lần/ngày (tùy liều), cùng giờ mỗi ngày để duy trì nồng độ ổn định. Không cần uống cùng thức ăn. Uống nguyên viên với nước, không nghiền hoặc nhai viên nén.",
                "notes": "Uống đều đặn hàng ngày. Không ngừng đột ngột. Nếu quên liều, uống ngay khi nhớ ra, nhưng nếu gần đến liều tiếp theo thì bỏ qua liều đã quên và tiếp tục lịch trình bình thường."
            },
            "iv": {
                "reconstitution": "Enalaprilat: Pha loãng trong 50ml D5W, normal saline, hoặc lactated Ringer's",
                "infusion_rate": "1.25mg IV bolus trong 5 phút, hoặc truyền trong 50ml dịch trong 15-30 phút. Có thể lặp lại mỗi 6 giờ nếu cần.",
                "compatibility": ["D5W", "Normal saline", "Lactated Ringer's"],
                "incompatibility": [],
                "notes": "Dạng IV (Enalaprilat) dùng cho cấp cứu tăng huyết áp. Tác dụng nhanh (15 phút). Theo dõi huyết áp chặt chẽ. Không dùng quá 48 giờ."
            }
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
            "primary_sources": [
                "FDA Drug Label - Enalapril (Vasotec), Enalaprilat IV",
                "UpToDate - Enalapril: Drug information",
                "Micromedex - Enalapril",
                "Lexicomp - Enalapril"
            ],
            "last_updated": "2025-01-20",
            "evidence_level": "A - Dựa trên FDA labeling, UpToDate, và các guidelines chính thức (AHA/ACC, KDIGO)"
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
            "adult_htn": "Khởi đầu 50mg PO x 1 lần/ngày. Tối đa 100mg/ngày.",
            "adult_heart_failure": "Khởi đầu 25mg PO x 1 lần/ngày, tăng dần đến 50-100mg/ngày.",
            "adult_start": "50mg PO x 1 lần/ngày (tăng huyết áp), 25mg PO x 1 lần/ngày (suy tim)",
            "adult_usual": "50-100mg PO x 1 lần/ngày (tăng huyết áp), 50-100mg PO x 1 lần/ngày (suy tim)",
            "adult_max": "100mg/ngày",
            "elderly": "Khởi đầu 25mg PO x 1 lần/ngày, tăng dần. Người cao tuổi nhạy cảm hơn với tác dụng phụ.",
            "renal_adjustment_dosage": {
                "normal": "50mg PO x 1 lần/ngày, tăng dần đến 100mg/ngày",
                "30_60": "25-50mg PO x 1 lần/ngày, thận trọng tăng dần",
                "under_30": "25mg PO x 1 lần/ngày, thận trọng tăng dần",
                "dialysis": "25mg PO x 1 lần/ngày sau mỗi lần lọc máu"
            },
            "administration_route": "PO",
            "frequency": "1 lần/ngày",
            "with_food": "Không cần uống cùng thức ăn",
            "notes": "KHÔNG gây ho khan (ưu điểm so với ACE-I). Thải trừ qua thận, cần điều chỉnh liều ở suy thận."
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
        "mechanism_of_action": "Losartan là ARB (Angiotensin Receptor Blocker) đầu tiên được phê duyệt, chẹn chọn lọc thụ thể Angiotensin II type 1 (AT1 receptor). Cơ chế tác dụng: (1) Chẹn cạnh tranh với Angiotensin II tại AT1 receptor trên mạch máu, tim, thận, và tuyến thượng thận. Ngăn cản Angiotensin II gắn vào receptor, dẫn đến giãn mạch ngoại vi, giảm sức cản mạch máu hệ thống (SVR), và giảm huyết áp. (2) Giảm sản xuất Aldosterone từ tuyến thượng thận, dẫn đến tăng bài tiết natri và nước qua thận, giảm thể tích máu. (3) Giảm hậu gánh tim, giảm protein niệu, làm chậm tiến triển bệnh thận đái tháo đường. (4) Bảo vệ tim và thận tương tự ACE-I. ĐẶC ĐIỂM QUAN TRỌNG: Losartan KHÔNG ức chế ACE, do đó KHÔNG làm tăng bradykinin → KHÔNG gây ho khan (ưu điểm lớn so với ACE-I). Losartan là prodrug, được chuyển hóa trong gan (CYP2C9, CYP3A4) thành EXP-3174 - chất chuyển hóa hoạt tính có tác dụng mạnh hơn và thời gian bán hủy dài hơn (6-9 giờ). Thải trừ qua thận và phân.",
        "monitoring": [
            "Huyết áp - Sau 1-2 tuần điều trị",
            "Kali máu - Sau 1-2 tuần điều trị",
            "Creatinine, eGFR - Sau 1-2 tuần điều trị",
            "Dấu hiệu phù mạch (hiếm hơn ACE-I)"
        ],
        "precautions": [
            "Kiểm tra Kali, Creatinine sau 1-2 tuần điều trị",
            "Tránh thai - Gây quái thai (ngừng ngay nếu mang thai)",
            "KHÔNG gây ho khan - Ưu điểm lớn so với ACE-I, dùng thay thế khi không dung nạp ho",
            "Nguy cơ phù mạch - Hiếm hơn ACE-I nhưng vẫn có thể xảy ra, ngừng thuốc ngay nếu sưng môi, lưỡi, khó thở",
            "Thận trọng ở suy thận, tăng Kali máu",
            "Tránh dùng NSAIDs",
            "Losartan chuyển hóa qua gan thành chất hoạt tính, cần điều chỉnh liều ở suy gan"
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
            "symptoms": [
                "Hạ huyết áp nghiêm trọng (có thể gây sốc)",
                "Tăng Kali máu (hyperkalemia) - có thể gây rối loạn nhịp tim",
                "Suy thận cấp (đặc biệt ở bệnh nhân hẹp động mạch thận)",
                "Chóng mặt, ngất",
                "Nhịp tim chậm (bradycardia) - phản ứng với hạ huyết áp",
                "Rối loạn nhịp tim (do tăng kali máu)"
            ],
            "antidote": "Không có antidote đặc hiệu cho ARBs",
            "treatment": [
                "Ngừng thuốc ngay lập tức",
                "Điều trị hạ huyết áp: Nằm đầu thấp, bù dịch IV (normal saline hoặc lactated Ringer's), nếu cần: dopamine hoặc norepinephrine",
                "Điều trị tăng kali máu: Nếu K+ > 5.5 mEq/L: Calcium gluconate/calcium chloride IV (bảo vệ tim), Insulin + glucose IV (chuyển kali vào tế bào), Sodium bicarbonate IV (nếu có nhiễm toan), Furosemide (nếu chức năng thận bình thường), Hemodialysis nếu tăng kali nặng không đáp ứng",
                "Theo dõi chức năng thận: Creatinine, BUN, nước tiểu",
                "Lọc máu (hemodialysis): Có thể cần thiết để loại bỏ losartan và chất chuyển hóa hoạt tính (EXP-3174) nếu quá liều nghiêm trọng"
            ],
            "monitoring": "Huyết áp liên tục, kali máu (mỗi 1-2 giờ), creatinine/BUN, ECG (theo dõi rối loạn nhịp do tăng kali), dấu hiệu sinh tồn, cân bằng dịch vào-ra"
        },
        "administration_instructions": {
            "oral": {
                "with_food": "Có thể uống với hoặc không thức ăn. Hấp thu không bị ảnh hưởng đáng kể bởi thức ăn.",
                "timing": "Uống 1 lần/ngày vào buổi sáng, cùng giờ mỗi ngày để duy trì nồng độ ổn định. Không cần uống cùng thức ăn. Uống nguyên viên với nước, không nghiền hoặc nhai viên nén.",
                "notes": "Uống đều đặn hàng ngày. Không ngừng đột ngột. Nếu quên liều, uống ngay khi nhớ ra, nhưng nếu gần đến liều tiếp theo thì bỏ qua liều đã quên và tiếp tục lịch trình bình thường."
            },
            "iv": {
                "reconstitution": "Không áp dụng - Losartan chỉ có dạng uống",
                "infusion_rate": "Không áp dụng",
                "compatibility": [],
                "incompatibility": [],
                "notes": "Losartan không có dạng tiêm."
            }
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
            "primary_sources": [
                "FDA Drug Label - Losartan (Cozaar)",
                "UpToDate - Losartan: Drug information",
                "Micromedex - Losartan",
                "Lexicomp - Losartan"
            ],
            "last_updated": "2025-01-20",
            "evidence_level": "A - Dựa trên FDA labeling, UpToDate, và các guidelines chính thức (AHA/ACC, KDIGO)"
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
            "Tăng huyết áp (Hypertension)",
            "Suy tim (Heart Failure) - NYHA class II-IV",
            "Sau nhồi máu cơ tim (Post-MI) - Giảm tử vong và suy tim",
            "Bệnh thận đái tháo đường (Diabetic nephropathy) - Giảm protein niệu"
        ],
        "dosage": {
            "adult_htn": "Khởi đầu 80-160mg PO x 1 lần/ngày. Tối đa 320mg/ngày.",
            "adult_heart_failure": "Khởi đầu 40mg PO x 2 lần/ngày, tăng dần đến 160mg x 2 lần/ngày.",
            "adult_start": "80-160mg PO x 1 lần/ngày (tăng huyết áp), 40mg PO x 2 lần/ngày (suy tim)",
            "adult_usual": "160-320mg PO x 1 lần/ngày (tăng huyết áp), 80-160mg PO x 2 lần/ngày (suy tim)",
            "adult_max": "320mg/ngày",
            "elderly": "Khởi đầu 80mg PO x 1 lần/ngày, tăng dần. Người cao tuổi nhạy cảm hơn với tác dụng phụ.",
            "renal_adjustment_dosage": {
                "normal": "80-160mg PO x 1 lần/ngày, tăng dần đến 320mg/ngày",
                "30_60": "80mg PO x 1 lần/ngày, thận trọng tăng dần",
                "under_30": "80mg PO x 1 lần/ngày, thận trọng tăng dần",
                "dialysis": "80mg PO x 1 lần/ngày sau mỗi lần lọc máu"
            },
            "administration_route": "PO",
            "frequency": "1-2 lần/ngày",
            "with_food": "Không cần uống cùng thức ăn",
            "notes": "KHÔNG gây ho khan (ưu điểm so với ACE-I). Thải trừ qua thận, cần điều chỉnh liều ở suy thận."
        },
        "side_effects": [
            "KHÔNG gây ho khan (khác ACE-I) - Ưu điểm lớn",
            "Hạ huyết áp",
            "Tăng Kali máu (Hyperkalemia) - Đặc biệt khi dùng với thuốc giữ kali",
            "Suy thận cấp (ở bệnh nhân hẹp động mạch thận 2 bên)",
            "Phù mạch (Angioedema) - Hiếm hơn ACE-I",
            "Chóng mặt, mệt mỏi",
            "Đau đầu",
            "Rash (phát ban)"
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
        "mechanism_of_action": "Valsartan là ARB (Angiotensin Receptor Blocker), chẹn chọn lọc thụ thể Angiotensin II type 1 (AT1 receptor). Cơ chế tác dụng tương tự Losartan: (1) Chẹn cạnh tranh với Angiotensin II tại AT1 receptor trên mạch máu, tim, thận, và tuyến thượng thận. Ngăn cản Angiotensin II gắn vào receptor, dẫn đến giãn mạch ngoại vi, giảm sức cản mạch máu hệ thống (SVR), và giảm huyết áp. (2) Giảm sản xuất Aldosterone từ tuyến thượng thận, dẫn đến tăng bài tiết natri và nước qua thận, giảm thể tích máu. (3) Giảm hậu gánh tim, giảm protein niệu, làm chậm tiến triển bệnh thận đái tháo đường. (4) Bảo vệ tim và thận tương tự ACE-I. ĐẶC ĐIỂM: Valsartan KHÔNG ức chế ACE, do đó KHÔNG làm tăng bradykinin → KHÔNG gây ho khan (ưu điểm lớn so với ACE-I). Valsartan có thời gian bán hủy dài hơn Losartan (6 giờ so với 2 giờ cho losartan, nhưng chất chuyển hóa hoạt tính của losartan có half-life 6-9 giờ). Chuyển hóa qua gan (CYP2C9), thải trừ qua thận và phân.",
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
            "symptoms": [
                "Hạ huyết áp nghiêm trọng (có thể gây sốc)",
                "Tăng Kali máu (hyperkalemia) - có thể gây rối loạn nhịp tim",
                "Suy thận cấp (đặc biệt ở bệnh nhân hẹp động mạch thận)",
                "Chóng mặt, ngất",
                "Nhịp tim chậm (bradycardia) - phản ứng với hạ huyết áp",
                "Rối loạn nhịp tim (do tăng kali máu)"
            ],
            "antidote": "Không có antidote đặc hiệu cho ARBs",
            "treatment": [
                "Ngừng thuốc ngay lập tức",
                "Điều trị hạ huyết áp: Nằm đầu thấp, bù dịch IV (normal saline hoặc lactated Ringer's), nếu cần: dopamine hoặc norepinephrine",
                "Điều trị tăng kali máu: Nếu K+ > 5.5 mEq/L: Calcium gluconate/calcium chloride IV (bảo vệ tim), Insulin + glucose IV (chuyển kali vào tế bào), Sodium bicarbonate IV (nếu có nhiễm toan), Furosemide (nếu chức năng thận bình thường), Hemodialysis nếu tăng kali nặng không đáp ứng",
                "Theo dõi chức năng thận: Creatinine, BUN, nước tiểu",
                "Lọc máu (hemodialysis): Có thể cần thiết để loại bỏ valsartan nếu quá liều nghiêm trọng"
            ],
            "monitoring": "Huyết áp liên tục, kali máu (mỗi 1-2 giờ), creatinine/BUN, ECG (theo dõi rối loạn nhịp do tăng kali), dấu hiệu sinh tồn, cân bằng dịch vào-ra"
        },
        "administration_instructions": {
            "oral": {
                "with_food": "Có thể uống với hoặc không thức ăn. Hấp thu không bị ảnh hưởng đáng kể bởi thức ăn.",
                "timing": "Uống 1-2 lần/ngày (tùy liều), cùng giờ mỗi ngày để duy trì nồng độ ổn định. Không cần uống cùng thức ăn. Uống nguyên viên với nước, không nghiền hoặc nhai viên nén.",
                "notes": "Uống đều đặn hàng ngày. Không ngừng đột ngột. Nếu quên liều, uống ngay khi nhớ ra, nhưng nếu gần đến liều tiếp theo thì bỏ qua liều đã quên và tiếp tục lịch trình bình thường."
            },
            "iv": {
                "reconstitution": "Không áp dụng - Valsartan chỉ có dạng uống",
                "infusion_rate": "Không áp dụng",
                "compatibility": [],
                "incompatibility": [],
                "notes": "Valsartan không có dạng tiêm."
            }
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
            "primary_sources": [
                "FDA Drug Label - Valsartan (Diovan)",
                "UpToDate - Valsartan: Drug information",
                "Micromedex - Valsartan",
                "Lexicomp - Valsartan"
            ],
            "last_updated": "2025-01-20",
            "evidence_level": "A - Dựa trên FDA labeling, UpToDate, và các guidelines chính thức (AHA/ACC, KDIGO)"
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
            "Tăng huyết áp (Hypertension)",
            "Giảm nguy cơ tim mạch ở bệnh nhân tăng huyết áp có nguy cơ cao",
            "Bệnh thận đái tháo đường (Diabetic nephropathy) - Giảm protein niệu"
        ],
        "dosage": {
            "adult_htn": "Khởi đầu 40mg PO x 1 lần/ngày. Tối đa 80mg/ngày.",
            "adult_start": "40mg PO x 1 lần/ngày",
            "adult_usual": "40-80mg PO x 1 lần/ngày",
            "adult_max": "80mg/ngày",
            "elderly": "Khởi đầu 20mg PO x 1 lần/ngày, tăng dần. Người cao tuổi nhạy cảm hơn với tác dụng phụ.",
            "renal_adjustment_dosage": {
                "normal": "40mg PO x 1 lần/ngày, tăng dần đến 80mg/ngày",
                "30_60": "20-40mg PO x 1 lần/ngày, thận trọng tăng dần",
                "under_30": "20mg PO x 1 lần/ngày, thận trọng tăng dần",
                "dialysis": "20mg PO x 1 lần/ngày sau mỗi lần lọc máu"
            },
            "administration_route": "PO",
            "frequency": "1 lần/ngày",
            "with_food": "Không cần uống cùng thức ăn",
            "notes": "KHÔNG gây ho khan (ưu điểm so với ACE-I). Tác dụng kéo dài nhất trong nhóm ARB (half-life 24h). Thải trừ chủ yếu qua gan, một phần qua thận."
        },
        "side_effects": [
            "KHÔNG gây ho khan (khác ACE-I) - Ưu điểm lớn",
            "Hạ huyết áp",
            "Tăng Kali máu (Hyperkalemia) - Đặc biệt khi dùng với thuốc giữ kali",
            "Suy thận cấp (ở bệnh nhân hẹp động mạch thận 2 bên)",
            "Phù mạch (Angioedema) - Hiếm hơn ACE-I",
            "Chóng mặt, mệt mỏi",
            "Đau đầu",
            "Rash (phát ban)"
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
        "mechanism_of_action": "Telmisartan là ARB (Angiotensin Receptor Blocker) có thời gian bán hủy dài nhất trong nhóm ARB (24 giờ). Cơ chế tác dụng: (1) Chẹn cạnh tranh với Angiotensin II tại AT1 receptor trên mạch máu, tim, thận, và tuyến thượng thận. Ngăn cản Angiotensin II gắn vào receptor, dẫn đến giãn mạch ngoại vi, giảm sức cản mạch máu hệ thống (SVR), và giảm huyết áp. (2) Giảm sản xuất Aldosterone từ tuyến thượng thận, dẫn đến tăng bài tiết natri và nước qua thận, giảm thể tích máu. (3) Giảm hậu gánh tim, giảm protein niệu, làm chậm tiến triển bệnh thận đái tháo đường. (4) Bảo vệ tim và thận tương tự ACE-I. ĐẶC ĐIỂM QUAN TRỌNG: Telmisartan KHÔNG ức chế ACE, do đó KHÔNG làm tăng bradykinin → KHÔNG gây ho khan (ưu điểm lớn so với ACE-I). Telmisartan có thời gian bán hủy dài nhất trong nhóm ARB (24 giờ), cho phép dùng 1 lần/ngày và duy trì tác dụng ổn định. Telmisartan có thêm tác dụng kích hoạt PPAR-gamma (Peroxisome Proliferator-Activated Receptor gamma) - tương tự thiazolidinediones như Pioglitazone, dẫn đến cải thiện nhẹ insulin resistance và glucose metabolism. Điều này có thể có lợi ở bệnh nhân đái tháo đường type 2. Thải trừ chủ yếu qua gan (glucuronidation), một phần qua thận.",
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
            "symptoms": [
                "Hạ huyết áp nghiêm trọng (có thể gây sốc)",
                "Tăng Kali máu (hyperkalemia) - có thể gây rối loạn nhịp tim",
                "Suy thận cấp (đặc biệt ở bệnh nhân hẹp động mạch thận)",
                "Chóng mặt, ngất",
                "Nhịp tim chậm (bradycardia) - phản ứng với hạ huyết áp",
                "Rối loạn nhịp tim (do tăng kali máu)"
            ],
            "antidote": "Không có antidote đặc hiệu cho ARBs",
            "treatment": [
                "Ngừng thuốc ngay lập tức",
                "Điều trị hạ huyết áp: Nằm đầu thấp, bù dịch IV (normal saline hoặc lactated Ringer's), nếu cần: dopamine hoặc norepinephrine",
                "Điều trị tăng kali máu: Nếu K+ > 5.5 mEq/L: Calcium gluconate/calcium chloride IV (bảo vệ tim), Insulin + glucose IV (chuyển kali vào tế bào), Sodium bicarbonate IV (nếu có nhiễm toan), Furosemide (nếu chức năng thận bình thường), Hemodialysis nếu tăng kali nặng không đáp ứng",
                "Theo dõi chức năng thận: Creatinine, BUN, nước tiểu",
                "Lọc máu (hemodialysis): Có thể cần thiết để loại bỏ telmisartan nếu quá liều nghiêm trọng (telmisartan thải trừ chủ yếu qua gan, nhưng vẫn có thể cần lọc máu)"
            ],
            "monitoring": "Huyết áp liên tục, kali máu (mỗi 1-2 giờ), creatinine/BUN, ECG (theo dõi rối loạn nhịp do tăng kali), dấu hiệu sinh tồn, cân bằng dịch vào-ra"
        },
        "administration_instructions": {
            "oral": {
                "with_food": "Có thể uống với hoặc không thức ăn. Hấp thu không bị ảnh hưởng đáng kể bởi thức ăn.",
                "timing": "Uống 1 lần/ngày vào buổi sáng, cùng giờ mỗi ngày để duy trì nồng độ ổn định. Không cần uống cùng thức ăn. Uống nguyên viên với nước, không nghiền hoặc nhai viên nén.",
                "notes": "Uống đều đặn hàng ngày. Không ngừng đột ngột. Nếu quên liều, uống ngay khi nhớ ra, nhưng nếu gần đến liều tiếp theo thì bỏ qua liều đã quên và tiếp tục lịch trình bình thường. Telmisartan có half-life dài (24h), nên có thể uống vào bất kỳ thời điểm nào trong ngày."
            },
            "iv": {
                "reconstitution": "Không áp dụng - Telmisartan chỉ có dạng uống",
                "infusion_rate": "Không áp dụng",
                "compatibility": [],
                "incompatibility": [],
                "notes": "Telmisartan không có dạng tiêm."
            }
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
            "primary_sources": [
                "FDA Drug Label - Telmisartan (Micardis)",
                "UpToDate - Telmisartan: Drug information",
                "Micromedex - Telmisartan",
                "Lexicomp - Telmisartan"
            ],
            "last_updated": "2025-01-20",
            "evidence_level": "A - Dựa trên FDA labeling, UpToDate, và các guidelines chính thức (AHA/ACC, KDIGO)"
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
