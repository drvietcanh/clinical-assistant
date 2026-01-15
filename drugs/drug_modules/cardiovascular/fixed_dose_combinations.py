"""
Fixed-Dose Combination Drugs for Hypertension
ACE/ARB + Diuretic, ARB + CCB, ACE + CCB combinations
"""

CARDIOVASCULAR_FIXED_DOSE_COMBINATIONS = {
    "Amlodipine/Olmesartan": {
        "group": "Cardiovascular - CCB + ARB (Fixed-Dose Combination)",
        "vietnamese_name": "Amlodipine/Olmesartan, Azor",
        "administration": ["PO"],
        "indications": [
            "Tăng huyết áp (khi cần phối hợp CCB và ARB).",
        ],
        "contraindications": [
            "Dị ứng với amlodipine, olmesartan, hoặc dihydropyridine.",
            "Có thai (ARB chống chỉ định trong thai kỳ).",
        ],
        "dosage": {
            "adult_initial": "Amlodipine 5mg/Olmesartan 20mg PO mỗi ngày.",
            "adult_maintenance": "Amlodipine 5mg/Olmesartan 40mg hoặc Amlodipine 10mg/Olmesartan 40mg PO mỗi ngày.",
            "notes": "Uống 1 lần/ngày, có thể uống với hoặc không thức ăn.",
        },
        "renal_adjustment": {
            "normal": "Không cần chỉnh liều.",
            "30_60": "Không cần chỉnh liều.",
            "under_30": "Thận trọng, có thể cần giảm liều olmesartan.",
        },
        "side_effects": [
            "Phù chân (do amlodipine).",
            "Chóng mặt, hạ huyết áp.",
            "Đau đầu.",
        ],
        "interactions": [],
        "pregnancy": "D: chống chỉ định trong thai kỳ (ARB).",
        "mechanism_of_action": (
            "Amlodipine là CCB dihydropyridine, ức chế kênh calci L-type, giãn mạch ngoại vi. "
            "Olmesartan là ARB, ức chế thụ thể AT1 của angiotensin II, giãn mạch. "
            "Phối hợp hai thuốc có tác dụng hiệp đồng giảm huyết áp."
        ),
        "monitoring": [
            "Huyết áp trước và trong điều trị.",
            "Creatinine, eGFR trước và trong điều trị.",
            "Dấu hiệu phù chân.",
        ],
        "precautions": [
            "Chống chỉ định trong thai kỳ - ARB có thể gây dị tật thai nhi.",
            "Nguy cơ phù chân (do amlodipine).",
            "Nguy cơ suy thận cấp - theo dõi creatinine chặt chẽ.",
        ],
        "pharmacokinetics": {
            "half_life": "Amlodipine: ~30-50 giờ; Olmesartan: ~13 giờ.",
            "onset": "Giảm huyết áp trong vài giờ đến vài ngày.",
            "duration": "24 giờ (dùng 1 lần/ngày).",
            "protein_binding": "Amlodipine: ~98%; Olmesartan: ~99%.",
            "clearance": "Amlodipine: chuyển hóa ở gan; Olmesartan: không chuyển hóa, thải qua phân và nước tiểu.",
        },
        "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm, tránh ánh sáng.",
        "black_box_warnings": (
            "Chống chỉ định trong thai kỳ: ARB có thể gây dị tật thai nhi và tử vong thai nhi. "
            "Ngừng ngay khi phát hiện có thai."
        ),
        "drug_interactions": {
            "major": [],
            "moderate": [],
            "minor": [],
        },
        "contraindications_detail": {
            "tuyệt_đối": [
                "Dị ứng với amlodipine, olmesartan, hoặc dihydropyridine.",
                "Có thai hoặc có thể mang thai.",
            ],
            "tương_đối": [
                "Suy thận nặng (CrCl <30) - thận trọng.",
            ],
        },
        "pregnancy_lactation": {
            "fda_category": "D",
            "pregnancy_details": "Chống chỉ định trong thai kỳ. ARB có thể gây dị tật thai nhi.",
            "lactation": {
                "safety": "Caution",
                "details": "Amlodipine và olmesartan đều bài tiết vào sữa mẹ.",
                "recommendation": "Thận trọng khi cho con bú.",
            },
        },
        "hepatic_adjustment": {
            "mild": "Không cần chỉnh liều.",
            "moderate": "Thận trọng.",
            "severe": "Thận trọng, có thể cần giảm liều.",
            "notes": "Amlodipine chuyển hóa ở gan; olmesartan không chuyển hóa qua gan.",
        },
        "overdose_management": {
            "symptoms": ["Hạ huyết áp nặng."],
            "antidote": "Không có antidote đặc hiệu.",
            "treatment": ["Điều trị hạ huyết áp: bù dịch, norepinephrine nếu cần."],
            "monitoring": "Huyết áp, dấu hiệu sinh tồn.",
        },
        "reversal_agents": None,
        "administration_instructions": {
            "oral": {
                "with_food": "Có thể uống với hoặc không thức ăn.",
                "timing": "Uống 1 lần/ngày, cùng giờ mỗi ngày.",
            },
        },
        "references": {
            "primary_sources": ["FDA Drug Label - Azor (amlodipine/olmesartan)", "ACC/AHA Guidelines 2024"],
            "last_updated": "2025-02-18",
            "evidence_level": "High – FDA-approved",
        },
        "risk_flags": {
            "high_alert": True,
            "narrow_therapeutic_index": False,
            "icu_critical_care_only": False,
            "bleeding_risk": "Low",
            "organ_toxicity": {"renal": "Moderate", "pregnancy": "High (teratogenic)"}
        },
        "guideline_tags": [
            "AHA/ACC 2017 Hypertension Guidelines",
            "AHA/ACC 2024 Hypertension Management Update",
            "ESC/ESH 2023 Hypertension Guidelines"
        ],
    },
    "Amlodipine/Valsartan": {
        "group": "Cardiovascular - CCB + ARB (Fixed-Dose Combination)",
        "vietnamese_name": "Amlodipine/Valsartan, Exforge",
        "administration": ["PO"],
        "indications": [
            "Tăng huyết áp (khi cần phối hợp CCB và ARB).",
        ],
        "contraindications": [
            "Dị ứng với amlodipine, valsartan, hoặc dihydropyridine.",
            "Có thai (ARB chống chỉ định trong thai kỳ).",
            "Hẹp động mạch chủ nặng.",
        ],
        "dosage": {
            "adult_initial": "Amlodipine 5mg/Valsartan 160mg PO mỗi ngày.",
            "adult_maintenance": "Amlodipine 5mg/Valsartan 320mg hoặc Amlodipine 10mg/Valsartan 320mg PO mỗi ngày.",
            "notes": "Uống 1 lần/ngày, có thể uống với hoặc không thức ăn.",
        },
        "renal_adjustment": {
            "normal": "Không cần chỉnh liều.",
            "30_60": "Không cần chỉnh liều.",
            "under_30": "Thận trọng, có thể cần giảm liều valsartan.",
        },
        "side_effects": [
            "Phù chân (do amlodipine).",
            "Chóng mặt, hạ huyết áp.",
            "Đỏ mặt, nhức đầu (do amlodipine).",
            "Tăng creatinin máu (do valsartan).",
        ],
        "interactions": [
            "NSAIDs: tăng nguy cơ suy thận cấp.",
        ],
        "pregnancy": "D: chống chỉ định trong thai kỳ (ARB).",
        "mechanism_of_action": (
            "Amlodipine là CCB (Calcium Channel Blocker) dihydropyridine, ức chế kênh calci L-type, "
            "dẫn đến giãn mạch ngoại vi và giảm huyết áp. Valsartan là ARB, ức chế thụ thể AT1 của angiotensin II, "
            "dẫn đến giãn mạch và giảm huyết áp. "
            "Phối hợp hai thuốc có tác dụng hiệp đồng giảm huyết áp và giảm phù chân (ARB đối kháng tác dụng phụ của CCB)."
        ),
        "monitoring": [
            "Huyết áp trước và trong điều trị.",
            "Creatinine, eGFR trước và trong điều trị.",
            "Dấu hiệu phù chân.",
        ],
        "precautions": [
            "Chống chỉ định trong thai kỳ - ARB có thể gây dị tật thai nhi.",
            "Nguy cơ phù chân (do amlodipine) - có thể giảm khi phối hợp với ARB.",
            "Nguy cơ suy thận cấp - theo dõi creatinine chặt chẽ.",
        ],
        "pharmacokinetics": {
            "half_life": "Amlodipine: ~30-50 giờ; Valsartan: ~6 giờ.",
            "onset": "Giảm huyết áp trong vài giờ đến vài ngày.",
            "duration": "24 giờ (dùng 1 lần/ngày).",
            "protein_binding": "Amlodipine: ~98%; Valsartan: ~95%.",
            "clearance": "Amlodipine: chuyển hóa ở gan; Valsartan: chủ yếu thải qua phân.",
        },
        "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm, tránh ánh sáng.",
        "black_box_warnings": (
            "Chống chỉ định trong thai kỳ: ARB có thể gây dị tật thai nhi và tử vong thai nhi. "
            "Ngừng ngay khi phát hiện có thai."
        ),
        "drug_interactions": {
            "major": [
                {
                    "drug": "NSAIDs",
                    "mechanism": "Tăng nguy cơ suy thận cấp.",
                    "effect": "Suy thận cấp.",
                    "management": "Thận trọng. Theo dõi chức năng thận.",
                },
            ],
            "moderate": [],
            "minor": [],
        },
        "contraindications_detail": {
            "tuyệt_đối": [
                "Dị ứng với amlodipine, valsartan, hoặc dihydropyridine.",
                "Có thai hoặc có thể mang thai.",
                "Hẹp động mạch chủ nặng.",
            ],
            "tương_đối": [
                "Suy thận nặng (CrCl <30) - thận trọng.",
            ],
        },
        "pregnancy_lactation": {
            "fda_category": "D",
            "pregnancy_details": "Chống chỉ định trong thai kỳ. ARB có thể gây dị tật thai nhi.",
            "lactation": {
                "safety": "Caution",
                "details": "Amlodipine và valsartan đều bài tiết vào sữa mẹ.",
                "recommendation": "Thận trọng khi cho con bú.",
            },
        },
        "hepatic_adjustment": {
            "mild": "Không cần chỉnh liều.",
            "moderate": "Thận trọng.",
            "severe": "Thận trọng, có thể cần giảm liều.",
            "notes": "Amlodipine chuyển hóa ở gan; valsartan chuyển hóa một phần qua gan.",
        },
        "overdose_management": {
            "symptoms": ["Hạ huyết áp nặng.", "Phù chân nặng."],
            "antidote": "Không có antidote đặc hiệu.",
            "treatment": ["Điều trị hạ huyết áp: bù dịch, norepinephrine nếu cần."],
            "monitoring": "Huyết áp, dấu hiệu sinh tồn.",
        },
        "reversal_agents": None,
        "administration_instructions": {
            "oral": {
                "with_food": "Có thể uống với hoặc không thức ăn.",
                "timing": "Uống 1 lần/ngày, cùng giờ mỗi ngày.",
            },
        },
        "references": {
            "primary_sources": ["FDA Drug Label - Exforge (amlodipine/valsartan)", "ACC/AHA Guidelines 2024"],
            "last_updated": "2025-02-18",
            "evidence_level": "High – FDA-approved",
        },
        "risk_flags": {
            "high_alert": True,
            "narrow_therapeutic_index": False,
            "icu_critical_care_only": False,
            "bleeding_risk": "Low",
            "organ_toxicity": {"renal": "Moderate", "pregnancy": "High (teratogenic)"}
        },
        "guideline_tags": [
            "AHA/ACC 2017 Hypertension Guidelines",
            "AHA/ACC 2024 Hypertension Management Update",
            "ESC/ESH 2023 Hypertension Guidelines"
        ],
    },

    "Lisinopril/Hydrochlorothiazide": {
        "group": "Cardiovascular - ACE Inhibitor + Diuretic (Fixed-Dose Combination)",
        "vietnamese_name": "Lisinopril/HCTZ, Zestoretic, Prinzide",
        "administration": ["PO"],
        "indications": [
            "Tăng huyết áp (khi cần phối hợp ACE inhibitor và diuretic).",
        ],
        "contraindications": [
            "Dị ứng với lisinopril, hydrochlorothiazide, hoặc sulfonamide.",
            "Có thai (ACE inhibitor chống chỉ định trong thai kỳ).",
            "Hẹp động mạch thận hai bên.",
            "Suy thận nặng (CrCl <30 ml/min).",
            "Hạ kali máu nặng.",
        ],
        "dosage": {
            "adult_initial": "Lisinopril 10mg/HCTZ 12.5mg PO mỗi ngày.",
            "adult_maintenance": "Lisinopril 20mg/HCTZ 12.5mg hoặc Lisinopril 20mg/HCTZ 25mg PO mỗi ngày.",
            "notes": "Uống 1 lần/ngày, có thể uống với hoặc không thức ăn. Điều chỉnh liều dựa trên đáp ứng huyết áp.",
        },
        "renal_adjustment": {
            "normal": "Không cần chỉnh liều.",
            "30_60": "Thận trọng, cân nhắc giảm liều hoặc dùng đơn trị.",
            "under_30": "Không dùng nếu CrCl <30 ml/min.",
        },
        "side_effects": [
            "Ho khan (do ACE inhibitor).",
            "Hạ huyết áp, chóng mặt.",
            "Hạ kali máu (do HCTZ).",
            "Tăng creatinin máu, suy thận cấp.",
            "Phù mạch (hiếm nhưng nghiêm trọng).",
            "Tăng đường huyết, tăng acid uric máu (do HCTZ).",
        ],
        "interactions": [
            "NSAIDs: tăng nguy cơ suy thận cấp.",
            "Kali-sparing diuretics, kali bổ sung: tăng nguy cơ tăng kali máu.",
            "Lithium: tăng nồng độ lithium.",
        ],
        "pregnancy": "D: chống chỉ định trong thai kỳ (ACE inhibitor).",
        "mechanism_of_action": (
            "Lisinopril là ACE inhibitor, ức chế enzyme chuyển đổi angiotensin (ACE), "
            "giảm sản xuất angiotensin II, dẫn đến giãn mạch và giảm huyết áp. "
            "Hydrochlorothiazide là thiazide diuretic, ức chế tái hấp thu natri và nước ở ống lượn xa, "
            "dẫn đến lợi tiểu và giảm thể tích tuần hoàn. "
            "Phối hợp hai thuốc có tác dụng hiệp đồng giảm huyết áp mạnh hơn từng thuốc đơn trị."
        ),
        "monitoring": [
            "Huyết áp trước và trong điều trị.",
            "Creatinine, eGFR (CrCl) trước và trong điều trị - QUAN TRỌNG.",
            "Điện giải (Na+, K+, Cl-) trước và trong điều trị - đặc biệt kali máu.",
            "Dấu hiệu hạ huyết áp, chóng mặt.",
            "Dấu hiệu phù mạch (sưng mặt, môi, lưỡi, họng) - nguy hiểm.",
        ],
        "precautions": [
            "QUAN TRỌNG: Chống chỉ định trong thai kỳ - ACE inhibitor có thể gây dị tật thai nhi.",
            "Nguy cơ suy thận cấp - theo dõi creatinine chặt chẽ, đặc biệt khi bắt đầu hoặc tăng liều.",
            "Nguy cơ hạ kali máu - theo dõi kali máu, có thể cần bổ sung kali hoặc dùng kali-sparing diuretic.",
            "Nguy cơ phù mạch - ngừng ngay nếu có triệu chứng, điều trị bằng epinephrine.",
            "Không dùng nếu CrCl <30 ml/min.",
            "Thận trọng ở bệnh nhân suy tim, bệnh mạch vành.",
        ],
        "pharmacokinetics": {
            "half_life": "Lisinopril: ~12 giờ; HCTZ: ~6-15 giờ.",
            "onset": "Giảm huyết áp trong vài giờ đến vài ngày.",
            "duration": "24 giờ (dùng 1 lần/ngày).",
            "protein_binding": "Lisinopril: ~25%; HCTZ: ~40%.",
            "clearance": "Lisinopril: thải qua thận; HCTZ: thải qua thận.",
        },
        "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm, tránh ánh sáng.",
        "black_box_warnings": (
            "Chống chỉ định trong thai kỳ: ACE inhibitor có thể gây dị tật thai nhi và tử vong thai nhi. "
            "Ngừng ngay khi phát hiện có thai. Phù mạch: có thể xảy ra và đe dọa tính mạng."
        ),
        "drug_interactions": {
            "major": [
                {
                    "drug": "NSAIDs (ibuprofen, naproxen, diclofenac)",
                    "mechanism": "NSAIDs giảm tác dụng giãn mạch của ACE inhibitor và giảm lưu lượng máu thận.",
                    "effect": "Tăng nguy cơ suy thận cấp, giảm hiệu quả hạ huyết áp.",
                    "management": "Thận trọng. Theo dõi chức năng thận chặt chẽ. Có thể cần giảm liều hoặc tránh NSAIDs.",
                },
                {
                    "drug": "Kali-sparing diuretics (spironolactone, eplerenone), Kali bổ sung",
                    "mechanism": "ACE inhibitor giảm bài tiết kali, HCTZ tăng bài tiết kali, nhưng tổng thể có thể tăng kali máu.",
                    "effect": "Tăng nguy cơ tăng kali máu, rối loạn nhịp tim.",
                    "management": "Thận trọng. Theo dõi kali máu chặt chẽ. Thường không nên dùng cùng kali-sparing diuretics.",
                },
            ],
            "moderate": [
                {
                    "drug": "Lithium",
                    "mechanism": "ACE inhibitor và HCTZ đều có thể tăng nồng độ lithium.",
                    "effect": "Tăng nguy cơ độc tính lithium.",
                    "management": "Thận trọng. Theo dõi nồng độ lithium chặt chẽ. Có thể cần giảm liều lithium.",
                },
            ],
            "minor": [],
        },
        "contraindications_detail": {
            "tuyệt_đối": [
                "Dị ứng với lisinopril, hydrochlorothiazide, hoặc sulfonamide.",
                "Có thai hoặc có thể mang thai.",
                "Hẹp động mạch thận hai bên.",
                "Suy thận nặng (CrCl <30 ml/min).",
                "Hạ kali máu nặng.",
            ],
            "tương_đối": [
                "Suy thận trung bình (CrCl 30-60) - thận trọng.",
                "Suy tim nặng - thận trọng.",
                "Bệnh mạch vành - thận trọng.",
                "Tiền sử phù mạch - tránh dùng.",
            ],
        },
        "pregnancy_lactation": {
            "fda_category": "D",
            "pregnancy_details": (
                "Chống chỉ định trong thai kỳ. ACE inhibitor có thể gây dị tật thai nhi, "
                "suy thận thai nhi, giảm nước ối, và tử vong thai nhi. Ngừng ngay khi phát hiện có thai."
            ),
            "lactation": {
                "safety": "Caution",
                "details": "Lisinopril và HCTZ đều bài tiết vào sữa mẹ.",
                "recommendation": "Thận trọng khi cho con bú. Cân nhắc ngừng cho con bú hoặc ngừng thuốc.",
            },
        },
        "hepatic_adjustment": {
            "mild": "Không cần chỉnh liều.",
            "moderate": "Thận trọng.",
            "severe": "Thận trọng, có thể cần giảm liều.",
            "notes": "Lisinopril không chuyển hóa qua gan; HCTZ không chuyển hóa đáng kể qua gan.",
        },
        "overdose_management": {
            "symptoms": [
                "Hạ huyết áp nặng, sốc.",
                "Hạ kali máu, hạ natri máu.",
                "Suy thận cấp.",
            ],
            "antidote": "Không có antidote đặc hiệu.",
            "treatment": [
                "Điều trị hạ huyết áp: bù dịch, norepinephrine nếu cần.",
                "Điều trị hạ kali máu: bổ sung kali IV nếu cần.",
                "Điều trị suy thận cấp: bù dịch, theo dõi chức năng thận.",
            ],
            "monitoring": "Huyết áp, điện giải, chức năng thận, dấu hiệu sinh tồn.",
        },
        "reversal_agents": None,
        "administration_instructions": {
            "oral": {
                "with_food": "Có thể uống với hoặc không thức ăn.",
                "timing": "Uống 1 lần/ngày, cùng giờ mỗi ngày.",
            },
        },
        "references": {
            "primary_sources": [
                "FDA Drug Label - Zestoretic (lisinopril/HCTZ)",
                "ACC/AHA Hypertension Guidelines 2024",
            ],
            "last_updated": "2025-02-18",
            "evidence_level": "High – FDA-approved",
        },
        "risk_flags": {
            "high_alert": True,
            "narrow_therapeutic_index": False,
            "icu_critical_care_only": False,
            "bleeding_risk": "Low",
            "organ_toxicity": {"renal": "Moderate", "pregnancy": "High (teratogenic)", "metabolic": "Moderate (hypokalemia)"}
        },
        "guideline_tags": [
            "AHA/ACC 2017 Hypertension Guidelines",
            "AHA/ACC 2024 Hypertension Management Update",
            "ESC/ESH 2023 Hypertension Guidelines"
        ],
    },

    "Losartan/Hydrochlorothiazide": {
        "group": "Cardiovascular - ARB + Diuretic (Fixed-Dose Combination)",
        "vietnamese_name": "Losartan/HCTZ, Hyzaar",
        "administration": ["PO"],
        "indications": [
            "Tăng huyết áp (khi cần phối hợp ARB và diuretic).",
        ],
        "contraindications": [
            "Dị ứng với losartan, hydrochlorothiazide, hoặc sulfonamide.",
            "Có thai (ARB chống chỉ định trong thai kỳ).",
            "Suy thận nặng (CrCl <30 ml/min).",
            "Hạ kali máu nặng.",
        ],
        "dosage": {
            "adult_initial": "Losartan 50mg/HCTZ 12.5mg PO mỗi ngày.",
            "adult_maintenance": "Losartan 100mg/HCTZ 12.5mg hoặc Losartan 100mg/HCTZ 25mg PO mỗi ngày.",
            "notes": "Uống 1 lần/ngày, có thể uống với hoặc không thức ăn.",
        },
        "renal_adjustment": {
            "normal": "Không cần chỉnh liều.",
            "30_60": "Thận trọng, cân nhắc giảm liều.",
            "under_30": "Không dùng nếu CrCl <30 ml/min.",
        },
        "side_effects": [
            "Chóng mặt, hạ huyết áp.",
            "Hạ kali máu (do HCTZ).",
            "Tăng creatinin máu.",
            "Tăng đường huyết, tăng acid uric máu (do HCTZ).",
        ],
        "interactions": [
            "NSAIDs: tăng nguy cơ suy thận cấp.",
            "Kali-sparing diuretics: tăng nguy cơ tăng kali máu.",
        ],
        "pregnancy": "D: chống chỉ định trong thai kỳ (ARB).",
        "mechanism_of_action": (
            "Losartan là ARB (Angiotensin Receptor Blocker), ức chế thụ thể AT1 của angiotensin II, "
            "dẫn đến giãn mạch và giảm huyết áp. Hydrochlorothiazide là thiazide diuretic, "
            "ức chế tái hấp thu natri và nước ở ống lượn xa. "
            "Phối hợp hai thuốc có tác dụng hiệp đồng giảm huyết áp."
        ),
        "monitoring": [
            "Huyết áp trước và trong điều trị.",
            "Creatinine, eGFR trước và trong điều trị.",
            "Điện giải (Na+, K+) trước và trong điều trị.",
        ],
        "precautions": [
            "Chống chỉ định trong thai kỳ - ARB có thể gây dị tật thai nhi.",
            "Nguy cơ suy thận cấp - theo dõi creatinine chặt chẽ.",
            "Nguy cơ hạ kali máu - theo dõi kali máu.",
            "Không dùng nếu CrCl <30 ml/min.",
        ],
        "pharmacokinetics": {
            "half_life": "Losartan: ~2 giờ (losartan), ~6-9 giờ (metabolite); HCTZ: ~6-15 giờ.",
            "onset": "Giảm huyết áp trong vài giờ đến vài ngày.",
            "duration": "24 giờ (dùng 1 lần/ngày).",
            "protein_binding": "Losartan: ~99%; HCTZ: ~40%.",
            "clearance": "Losartan: chuyển hóa ở gan; HCTZ: thải qua thận.",
        },
        "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm, tránh ánh sáng.",
        "black_box_warnings": (
            "Chống chỉ định trong thai kỳ: ARB có thể gây dị tật thai nhi và tử vong thai nhi. "
            "Ngừng ngay khi phát hiện có thai."
        ),
        "drug_interactions": {
            "major": [
                {
                    "drug": "NSAIDs",
                    "mechanism": "Tăng nguy cơ suy thận cấp.",
                    "effect": "Suy thận cấp, giảm hiệu quả hạ huyết áp.",
                    "management": "Thận trọng. Theo dõi chức năng thận.",
                },
            ],
            "moderate": [],
            "minor": [],
        },
        "contraindications_detail": {
            "tuyệt_đối": [
                "Dị ứng với losartan, HCTZ, hoặc sulfonamide.",
                "Có thai hoặc có thể mang thai.",
                "Suy thận nặng (CrCl <30 ml/min).",
                "Hạ kali máu nặng.",
            ],
            "tương_đối": [
                "Suy thận trung bình (CrCl 30-60) - thận trọng.",
            ],
        },
        "pregnancy_lactation": {
            "fda_category": "D",
            "pregnancy_details": "Chống chỉ định trong thai kỳ. ARB có thể gây dị tật thai nhi.",
            "lactation": {
                "safety": "Caution",
                "details": "Losartan và HCTZ đều bài tiết vào sữa mẹ.",
                "recommendation": "Thận trọng khi cho con bú.",
            },
        },
        "hepatic_adjustment": {
            "mild": "Không cần chỉnh liều.",
            "moderate": "Thận trọng.",
            "severe": "Thận trọng, có thể cần giảm liều.",
            "notes": "Losartan chuyển hóa ở gan; HCTZ không chuyển hóa đáng kể qua gan.",
        },
        "overdose_management": {
            "symptoms": ["Hạ huyết áp nặng.", "Hạ kali máu."],
            "antidote": "Không có antidote đặc hiệu.",
            "treatment": ["Điều trị hạ huyết áp: bù dịch.", "Điều trị hạ kali máu: bổ sung kali IV nếu cần."],
            "monitoring": "Huyết áp, điện giải, chức năng thận.",
        },
        "reversal_agents": None,
        "administration_instructions": {
            "oral": {
                "with_food": "Có thể uống với hoặc không thức ăn.",
                "timing": "Uống 1 lần/ngày, cùng giờ mỗi ngày.",
            },
        },
        "references": {
            "primary_sources": ["FDA Drug Label - Hyzaar (losartan/HCTZ)", "ACC/AHA Guidelines 2024"],
            "last_updated": "2025-02-18",
            "evidence_level": "High – FDA-approved",
        },
        "risk_flags": {
            "high_alert": True,
            "narrow_therapeutic_index": False,
            "icu_critical_care_only": False,
            "bleeding_risk": "Low",
            "organ_toxicity": {"renal": "Moderate", "pregnancy": "High (teratogenic)", "metabolic": "Moderate (hypokalemia)"}
        },
        "guideline_tags": [
            "AHA/ACC 2017 Hypertension Guidelines",
            "AHA/ACC 2024 Hypertension Management Update",
            "ESC/ESH 2023 Hypertension Guidelines"
        ],
    },

    "Enalapril/Hydrochlorothiazide": {
        "group": "Cardiovascular - ACE Inhibitor + Diuretic (Fixed-Dose Combination)",
        "vietnamese_name": "Enalapril/HCTZ, Vaseretic",
        "administration": ["PO"],
        "indications": [
            "Tăng huyết áp (khi cần phối hợp ACE inhibitor và diuretic).",
        ],
        "contraindications": [
            "Dị ứng với enalapril, hydrochlorothiazide, hoặc sulfonamide.",
            "Có thai (ACE inhibitor chống chỉ định trong thai kỳ).",
            "Hẹp động mạch thận hai bên.",
            "Suy thận nặng (CrCl <30 ml/min).",
            "Hạ kali máu nặng.",
        ],
        "dosage": {
            "adult_initial": "Enalapril 5mg/HCTZ 12.5mg PO mỗi ngày.",
            "adult_maintenance": "Enalapril 10mg/HCTZ 12.5mg hoặc Enalapril 10mg/HCTZ 25mg PO mỗi ngày.",
            "notes": "Uống 1-2 lần/ngày tùy liều, có thể uống với hoặc không thức ăn. Điều chỉnh liều dựa trên đáp ứng huyết áp.",
        },
        "renal_adjustment": {
            "normal": "Không cần chỉnh liều.",
            "30_60": "Thận trọng, cân nhắc giảm liều hoặc dùng đơn trị.",
            "under_30": "Không dùng nếu CrCl <30 ml/min.",
        },
        "side_effects": [
            "Ho khan (do ACE inhibitor).",
            "Hạ huyết áp, chóng mặt.",
            "Hạ kali máu (do HCTZ).",
            "Tăng creatinin máu, suy thận cấp.",
            "Phù mạch (hiếm nhưng nghiêm trọng).",
            "Tăng đường huyết, tăng acid uric máu (do HCTZ).",
        ],
        "interactions": [
            "NSAIDs: tăng nguy cơ suy thận cấp.",
            "Kali-sparing diuretics, kali bổ sung: tăng nguy cơ tăng kali máu.",
            "Lithium: tăng nồng độ lithium.",
        ],
        "pregnancy": "D: chống chỉ định trong thai kỳ (ACE inhibitor).",
        "mechanism_of_action": (
            "Enalapril là ACE inhibitor, ức chế enzyme chuyển đổi angiotensin (ACE), "
            "giảm sản xuất angiotensin II, dẫn đến giãn mạch và giảm huyết áp. "
            "Hydrochlorothiazide là thiazide diuretic, ức chế tái hấp thu natri và nước ở ống lượn xa, "
            "dẫn đến lợi tiểu và giảm thể tích tuần hoàn. "
            "Phối hợp hai thuốc có tác dụng hiệp đồng giảm huyết áp mạnh hơn từng thuốc đơn trị."
        ),
        "monitoring": [
            "Huyết áp trước và trong điều trị.",
            "Creatinine, eGFR (CrCl) trước và trong điều trị - QUAN TRỌNG.",
            "Điện giải (Na+, K+, Cl-) trước và trong điều trị - đặc biệt kali máu.",
            "Dấu hiệu hạ huyết áp, chóng mặt.",
            "Dấu hiệu phù mạch (sưng mặt, môi, lưỡi, họng) - nguy hiểm.",
        ],
        "precautions": [
            "QUAN TRỌNG: Chống chỉ định trong thai kỳ - ACE inhibitor có thể gây dị tật thai nhi.",
            "Nguy cơ suy thận cấp - theo dõi creatinine chặt chẽ, đặc biệt khi bắt đầu hoặc tăng liều.",
            "Nguy cơ hạ kali máu - theo dõi kali máu, có thể cần bổ sung kali hoặc dùng kali-sparing diuretic.",
            "Nguy cơ phù mạch - ngừng ngay nếu có triệu chứng, điều trị bằng epinephrine.",
            "Không dùng nếu CrCl <30 ml/min.",
            "Thận trọng ở bệnh nhân suy tim, bệnh mạch vành.",
        ],
        "pharmacokinetics": {
            "half_life": "Enalapril: ~11 giờ; Enalaprilat: ~30-35 giờ; HCTZ: ~6-15 giờ.",
            "onset": "Giảm huyết áp trong vài giờ đến vài ngày.",
            "duration": "12-24 giờ (dùng 1-2 lần/ngày).",
            "protein_binding": "Enalapril: ~50-60%; HCTZ: ~40%.",
            "clearance": "Enalapril: thải qua thận; HCTZ: thải qua thận.",
        },
        "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm, tránh ánh sáng.",
        "black_box_warnings": (
            "Chống chỉ định trong thai kỳ: ACE inhibitor có thể gây dị tật thai nhi và tử vong thai nhi. "
            "Ngừng ngay khi phát hiện có thai. Phù mạch: có thể xảy ra và đe dọa tính mạng."
        ),
        "drug_interactions": {
            "major": [
                {
                    "drug": "NSAIDs (ibuprofen, naproxen, diclofenac)",
                    "mechanism": "NSAIDs giảm tác dụng giãn mạch của ACE inhibitor và giảm lưu lượng máu thận.",
                    "effect": "Tăng nguy cơ suy thận cấp, giảm hiệu quả hạ huyết áp.",
                    "management": "Thận trọng. Theo dõi chức năng thận chặt chẽ. Có thể cần giảm liều hoặc tránh NSAIDs.",
                },
                {
                    "drug": "Kali-sparing diuretics (spironolactone, eplerenone), Kali bổ sung",
                    "mechanism": "ACE inhibitor giảm bài tiết kali, HCTZ tăng bài tiết kali, nhưng tổng thể có thể tăng kali máu.",
                    "effect": "Tăng nguy cơ tăng kali máu, rối loạn nhịp tim.",
                    "management": "Thận trọng. Theo dõi kali máu chặt chẽ. Thường không nên dùng cùng kali-sparing diuretics.",
                },
            ],
            "moderate": [
                {
                    "drug": "Lithium",
                    "mechanism": "ACE inhibitor và HCTZ đều có thể tăng nồng độ lithium.",
                    "effect": "Tăng nguy cơ độc tính lithium.",
                    "management": "Thận trọng. Theo dõi nồng độ lithium chặt chẽ. Có thể cần giảm liều lithium.",
                },
            ],
            "minor": [],
        },
        "contraindications_detail": {
            "tuyệt_đối": [
                "Dị ứng với enalapril, hydrochlorothiazide, hoặc sulfonamide.",
                "Có thai hoặc có thể mang thai.",
                "Hẹp động mạch thận hai bên.",
                "Suy thận nặng (CrCl <30 ml/min).",
                "Hạ kali máu nặng.",
            ],
            "tương_đối": [
                "Suy thận trung bình (CrCl 30-60) - thận trọng.",
                "Suy tim nặng - thận trọng.",
                "Bệnh mạch vành - thận trọng.",
                "Tiền sử phù mạch - tránh dùng.",
            ],
        },
        "pregnancy_lactation": {
            "fda_category": "D",
            "pregnancy_details": (
                "Chống chỉ định trong thai kỳ. ACE inhibitor có thể gây dị tật thai nhi, "
                "suy thận thai nhi, giảm nước ối, và tử vong thai nhi. Ngừng ngay khi phát hiện có thai."
            ),
            "lactation": {
                "safety": "Caution",
                "details": "Enalapril và HCTZ đều bài tiết vào sữa mẹ.",
                "recommendation": "Thận trọng khi cho con bú. Cân nhắc ngừng cho con bú hoặc ngừng thuốc.",
            },
        },
        "hepatic_adjustment": {
            "mild": "Không cần chỉnh liều.",
            "moderate": "Thận trọng.",
            "severe": "Thận trọng, có thể cần giảm liều.",
            "notes": "Enalapril chuyển hóa một phần qua gan; HCTZ không chuyển hóa đáng kể qua gan.",
        },
        "overdose_management": {
            "symptoms": [
                "Hạ huyết áp nặng, sốc.",
                "Hạ kali máu, hạ natri máu.",
                "Suy thận cấp.",
            ],
            "antidote": "Không có antidote đặc hiệu.",
            "treatment": [
                "Điều trị hạ huyết áp: bù dịch, norepinephrine nếu cần.",
                "Điều trị hạ kali máu: bổ sung kali IV nếu cần.",
                "Điều trị suy thận cấp: bù dịch, theo dõi chức năng thận.",
            ],
            "monitoring": "Huyết áp, điện giải, chức năng thận, dấu hiệu sinh tồn.",
        },
        "reversal_agents": None,
        "administration_instructions": {
            "oral": {
                "with_food": "Có thể uống với hoặc không thức ăn.",
                "timing": "Uống 1-2 lần/ngày tùy liều, cùng giờ mỗi ngày.",
            },
        },
        "references": {
            "primary_sources": [
                "FDA Drug Label - Vaseretic (enalapril/HCTZ)",
                "ACC/AHA Hypertension Guidelines 2024",
            ],
            "last_updated": "2025-02-18",
            "evidence_level": "High – FDA-approved",
        },
        "risk_flags": {
            "high_alert": True,
            "narrow_therapeutic_index": False,
            "icu_critical_care_only": False,
            "bleeding_risk": "Low",
            "organ_toxicity": {"renal": "Moderate", "pregnancy": "High (teratogenic)", "metabolic": "Moderate (hypokalemia)"}
        },
        "guideline_tags": [
            "AHA/ACC 2017 Hypertension Guidelines",
            "AHA/ACC 2024 Hypertension Management Update",
            "ESC/ESH 2023 Hypertension Guidelines"
        ],
    },

    "Valsartan/Hydrochlorothiazide": {
        "group": "Cardiovascular - ARB + Diuretic (Fixed-Dose Combination)",
        "vietnamese_name": "Valsartan/HCTZ, Diovan HCT",
        "administration": ["PO"],
        "indications": [
            "Tăng huyết áp (khi cần phối hợp ARB và diuretic).",
        ],
        "contraindications": [
            "Dị ứng với valsartan, hydrochlorothiazide, hoặc sulfonamide.",
            "Có thai (ARB chống chỉ định trong thai kỳ).",
            "Suy thận nặng (CrCl <30 ml/min).",
            "Hạ kali máu nặng.",
        ],
        "dosage": {
            "adult_initial": "Valsartan 80mg/HCTZ 12.5mg PO mỗi ngày.",
            "adult_maintenance": "Valsartan 160mg/HCTZ 12.5mg hoặc Valsartan 160mg/HCTZ 25mg PO mỗi ngày.",
            "notes": "Uống 1 lần/ngày, có thể uống với hoặc không thức ăn.",
        },
        "renal_adjustment": {
            "normal": "Không cần chỉnh liều.",
            "30_60": "Thận trọng, cân nhắc giảm liều.",
            "under_30": "Không dùng nếu CrCl <30 ml/min.",
        },
        "side_effects": [
            "Chóng mặt, hạ huyết áp.",
            "Hạ kali máu (do HCTZ).",
            "Tăng creatinin máu.",
            "Tăng đường huyết, tăng acid uric máu (do HCTZ).",
        ],
        "interactions": [
            "NSAIDs: tăng nguy cơ suy thận cấp.",
            "Kali-sparing diuretics: tăng nguy cơ tăng kali máu.",
        ],
        "pregnancy": "D: chống chỉ định trong thai kỳ (ARB).",
        "mechanism_of_action": (
            "Valsartan là ARB (Angiotensin Receptor Blocker), ức chế thụ thể AT1 của angiotensin II, "
            "dẫn đến giãn mạch và giảm huyết áp. Hydrochlorothiazide là thiazide diuretic, "
            "ức chế tái hấp thu natri và nước ở ống lượn xa. "
            "Phối hợp hai thuốc có tác dụng hiệp đồng giảm huyết áp."
        ),
        "monitoring": [
            "Huyết áp trước và trong điều trị.",
            "Creatinine, eGFR trước và trong điều trị.",
            "Điện giải (Na+, K+) trước và trong điều trị.",
        ],
        "precautions": [
            "Chống chỉ định trong thai kỳ - ARB có thể gây dị tật thai nhi.",
            "Nguy cơ suy thận cấp - theo dõi creatinine chặt chẽ.",
            "Nguy cơ hạ kali máu - theo dõi kali máu.",
            "Không dùng nếu CrCl <30 ml/min.",
        ],
        "pharmacokinetics": {
            "half_life": "Valsartan: ~6 giờ; HCTZ: ~6-15 giờ.",
            "onset": "Giảm huyết áp trong vài giờ đến vài ngày.",
            "duration": "24 giờ (dùng 1 lần/ngày).",
            "protein_binding": "Valsartan: ~95%; HCTZ: ~40%.",
            "clearance": "Valsartan: chủ yếu thải qua phân; HCTZ: thải qua thận.",
        },
        "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm, tránh ánh sáng.",
        "black_box_warnings": (
            "Chống chỉ định trong thai kỳ: ARB có thể gây dị tật thai nhi và tử vong thai nhi. "
            "Ngừng ngay khi phát hiện có thai."
        ),
        "drug_interactions": {
            "major": [
                {
                    "drug": "NSAIDs",
                    "mechanism": "Tăng nguy cơ suy thận cấp.",
                    "effect": "Suy thận cấp, giảm hiệu quả hạ huyết áp.",
                    "management": "Thận trọng. Theo dõi chức năng thận.",
                },
            ],
            "moderate": [],
            "minor": [],
        },
        "contraindications_detail": {
            "tuyệt_đối": [
                "Dị ứng với valsartan, HCTZ, hoặc sulfonamide.",
                "Có thai hoặc có thể mang thai.",
                "Suy thận nặng (CrCl <30 ml/min).",
                "Hạ kali máu nặng.",
            ],
            "tương_đối": [
                "Suy thận trung bình (CrCl 30-60) - thận trọng.",
            ],
        },
        "pregnancy_lactation": {
            "fda_category": "D",
            "pregnancy_details": "Chống chỉ định trong thai kỳ. ARB có thể gây dị tật thai nhi.",
            "lactation": {
                "safety": "Caution",
                "details": "Valsartan và HCTZ đều bài tiết vào sữa mẹ.",
                "recommendation": "Thận trọng khi cho con bú.",
            },
        },
        "hepatic_adjustment": {
            "mild": "Không cần chỉnh liều.",
            "moderate": "Thận trọng.",
            "severe": "Thận trọng, có thể cần giảm liều.",
            "notes": "Valsartan chuyển hóa một phần qua gan; HCTZ không chuyển hóa đáng kể qua gan.",
        },
        "overdose_management": {
            "symptoms": ["Hạ huyết áp nặng.", "Hạ kali máu."],
            "antidote": "Không có antidote đặc hiệu.",
            "treatment": ["Điều trị hạ huyết áp: bù dịch.", "Điều trị hạ kali máu: bổ sung kali IV nếu cần."],
            "monitoring": "Huyết áp, điện giải, chức năng thận.",
        },
        "reversal_agents": None,
        "administration_instructions": {
            "oral": {
                "with_food": "Có thể uống với hoặc không thức ăn.",
                "timing": "Uống 1 lần/ngày, cùng giờ mỗi ngày.",
            },
        },
        "references": {
            "primary_sources": ["FDA Drug Label - Diovan HCT (valsartan/HCTZ)", "ACC/AHA Guidelines 2024"],
            "last_updated": "2025-02-18",
            "evidence_level": "High – FDA-approved",
        },
        "risk_flags": {
            "high_alert": True,
            "narrow_therapeutic_index": False,
            "icu_critical_care_only": False,
            "bleeding_risk": "Low",
            "organ_toxicity": {"renal": "Moderate", "pregnancy": "High (teratogenic)", "metabolic": "Moderate (hypokalemia)"}
        },
        "guideline_tags": [
            "AHA/ACC 2017 Hypertension Guidelines",
            "AHA/ACC 2024 Hypertension Management Update",
            "ESC/ESH 2023 Hypertension Guidelines"
        ],
    },

    "Benazepril/Hydrochlorothiazide": {
        "group": "Cardiovascular - ACE Inhibitor + Diuretic (Fixed-Dose Combination)",
        "vietnamese_name": "Benazepril/HCTZ, Lotensin HCT",
        "administration": ["PO"],
        "indications": [
            "Tăng huyết áp (khi cần phối hợp ACE inhibitor và diuretic).",
        ],
        "contraindications": [
            "Dị ứng với benazepril, hydrochlorothiazide, hoặc sulfonamide.",
            "Có thai (ACE inhibitor chống chỉ định trong thai kỳ).",
            "Hẹp động mạch thận hai bên.",
            "Suy thận nặng (CrCl <30 ml/min).",
            "Hạ kali máu nặng.",
        ],
        "dosage": {
            "adult_initial": "Benazepril 10mg/HCTZ 12.5mg PO mỗi ngày.",
            "adult_maintenance": "Benazepril 20mg/HCTZ 12.5mg hoặc Benazepril 20mg/HCTZ 25mg PO mỗi ngày.",
            "notes": "Uống 1 lần/ngày, có thể uống với hoặc không thức ăn.",
        },
        "renal_adjustment": {
            "normal": "Không cần chỉnh liều.",
            "30_60": "Thận trọng, cân nhắc giảm liều hoặc dùng đơn trị.",
            "under_30": "Không dùng nếu CrCl <30 ml/min.",
        },
        "side_effects": [
            "Ho khan (do ACE inhibitor).",
            "Hạ huyết áp, chóng mặt.",
            "Hạ kali máu (do HCTZ).",
            "Tăng creatinin máu, suy thận cấp.",
            "Phù mạch (hiếm nhưng nghiêm trọng).",
            "Tăng đường huyết, tăng acid uric máu (do HCTZ).",
        ],
        "interactions": [
            "NSAIDs: tăng nguy cơ suy thận cấp.",
            "Kali-sparing diuretics, kali bổ sung: tăng nguy cơ tăng kali máu.",
            "Lithium: tăng nồng độ lithium.",
        ],
        "pregnancy": "D: chống chỉ định trong thai kỳ (ACE inhibitor).",
        "mechanism_of_action": (
            "Benazepril là ACE inhibitor, ức chế enzyme chuyển đổi angiotensin (ACE), "
            "giảm sản xuất angiotensin II, dẫn đến giãn mạch và giảm huyết áp. "
            "Hydrochlorothiazide là thiazide diuretic, ức chế tái hấp thu natri và nước ở ống lượn xa, "
            "dẫn đến lợi tiểu và giảm thể tích tuần hoàn. "
            "Phối hợp hai thuốc có tác dụng hiệp đồng giảm huyết áp mạnh hơn từng thuốc đơn trị."
        ),
        "monitoring": [
            "Huyết áp trước và trong điều trị.",
            "Creatinine, eGFR (CrCl) trước và trong điều trị - QUAN TRỌNG.",
            "Điện giải (Na+, K+, Cl-) trước và trong điều trị - đặc biệt kali máu.",
            "Dấu hiệu hạ huyết áp, chóng mặt.",
            "Dấu hiệu phù mạch (sưng mặt, môi, lưỡi, họng) - nguy hiểm.",
        ],
        "precautions": [
            "QUAN TRỌNG: Chống chỉ định trong thai kỳ - ACE inhibitor có thể gây dị tật thai nhi.",
            "Nguy cơ suy thận cấp - theo dõi creatinine chặt chẽ, đặc biệt khi bắt đầu hoặc tăng liều.",
            "Nguy cơ hạ kali máu - theo dõi kali máu, có thể cần bổ sung kali hoặc dùng kali-sparing diuretic.",
            "Nguy cơ phù mạch - ngừng ngay nếu có triệu chứng, điều trị bằng epinephrine.",
            "Không dùng nếu CrCl <30 ml/min.",
            "Thận trọng ở bệnh nhân suy tim, bệnh mạch vành.",
        ],
        "pharmacokinetics": {
            "half_life": "Benazepril: ~10-11 giờ; Benazeprilat: ~10-11 giờ; HCTZ: ~6-15 giờ.",
            "onset": "Giảm huyết áp trong vài giờ đến vài ngày.",
            "duration": "24 giờ (dùng 1 lần/ngày).",
            "protein_binding": "Benazepril: ~97%; HCTZ: ~40%.",
            "clearance": "Benazepril: thải qua cả gan và thận; HCTZ: thải qua thận.",
        },
        "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm, tránh ánh sáng.",
        "black_box_warnings": (
            "Chống chỉ định trong thai kỳ: ACE inhibitor có thể gây dị tật thai nhi và tử vong thai nhi. "
            "Ngừng ngay khi phát hiện có thai. Phù mạch: có thể xảy ra và đe dọa tính mạng."
        ),
        "drug_interactions": {
            "major": [
                {
                    "drug": "NSAIDs (ibuprofen, naproxen, diclofenac)",
                    "mechanism": "NSAIDs giảm tác dụng giãn mạch của ACE inhibitor và giảm lưu lượng máu thận.",
                    "effect": "Tăng nguy cơ suy thận cấp, giảm hiệu quả hạ huyết áp.",
                    "management": "Thận trọng. Theo dõi chức năng thận chặt chẽ. Có thể cần giảm liều hoặc tránh NSAIDs.",
                },
                {
                    "drug": "Kali-sparing diuretics (spironolactone, eplerenone), Kali bổ sung",
                    "mechanism": "ACE inhibitor giảm bài tiết kali, HCTZ tăng bài tiết kali, nhưng tổng thể có thể tăng kali máu.",
                    "effect": "Tăng nguy cơ tăng kali máu, rối loạn nhịp tim.",
                    "management": "Thận trọng. Theo dõi kali máu chặt chẽ. Thường không nên dùng cùng kali-sparing diuretics.",
                },
            ],
            "moderate": [
                {
                    "drug": "Lithium",
                    "mechanism": "ACE inhibitor và HCTZ đều có thể tăng nồng độ lithium.",
                    "effect": "Tăng nguy cơ độc tính lithium.",
                    "management": "Thận trọng. Theo dõi nồng độ lithium chặt chẽ. Có thể cần giảm liều lithium.",
                },
            ],
            "minor": [],
        },
        "contraindications_detail": {
            "tuyệt_đối": [
                "Dị ứng với benazepril, hydrochlorothiazide, hoặc sulfonamide.",
                "Có thai hoặc có thể mang thai.",
                "Hẹp động mạch thận hai bên.",
                "Suy thận nặng (CrCl <30 ml/min).",
                "Hạ kali máu nặng.",
            ],
            "tương_đối": [
                "Suy thận trung bình (CrCl 30-60) - thận trọng.",
                "Suy tim nặng - thận trọng.",
                "Bệnh mạch vành - thận trọng.",
                "Tiền sử phù mạch - tránh dùng.",
            ],
        },
        "pregnancy_lactation": {
            "fda_category": "D",
            "pregnancy_details": (
                "Chống chỉ định trong thai kỳ. ACE inhibitor có thể gây dị tật thai nhi, "
                "suy thận thai nhi, giảm nước ối, và tử vong thai nhi. Ngừng ngay khi phát hiện có thai."
            ),
            "lactation": {
                "safety": "Caution",
                "details": "Benazepril và HCTZ đều bài tiết vào sữa mẹ.",
                "recommendation": "Thận trọng khi cho con bú. Cân nhắc ngừng cho con bú hoặc ngừng thuốc.",
            },
        },
        "hepatic_adjustment": {
            "mild": "Không cần chỉnh liều.",
            "moderate": "Thận trọng.",
            "severe": "Thận trọng, có thể cần giảm liều.",
            "notes": "Benazepril thải qua cả gan và thận; HCTZ không chuyển hóa đáng kể qua gan.",
        },
        "overdose_management": {
            "symptoms": [
                "Hạ huyết áp nặng, sốc.",
                "Hạ kali máu, hạ natri máu.",
                "Suy thận cấp.",
            ],
            "antidote": "Không có antidote đặc hiệu.",
            "treatment": [
                "Điều trị hạ huyết áp: bù dịch, norepinephrine nếu cần.",
                "Điều trị hạ kali máu: bổ sung kali IV nếu cần.",
                "Điều trị suy thận cấp: bù dịch, theo dõi chức năng thận.",
            ],
            "monitoring": "Huyết áp, điện giải, chức năng thận, dấu hiệu sinh tồn.",
        },
        "reversal_agents": None,
        "administration_instructions": {
            "oral": {
                "with_food": "Có thể uống với hoặc không thức ăn.",
                "timing": "Uống 1 lần/ngày, cùng giờ mỗi ngày.",
            },
        },
        "references": {
            "primary_sources": [
                "FDA Drug Label - Lotensin HCT (benazepril/HCTZ)",
                "ACC/AHA Hypertension Guidelines 2024",
            ],
            "last_updated": "2025-02-18",
            "evidence_level": "High – FDA-approved",
        },
        "risk_flags": {
            "high_alert": True,
            "narrow_therapeutic_index": False,
            "icu_critical_care_only": False,
            "bleeding_risk": "Low",
            "organ_toxicity": {"renal": "Moderate", "pregnancy": "High (teratogenic)", "metabolic": "Moderate (hypokalemia)"}
        },
        "guideline_tags": [
            "AHA/ACC 2017 Hypertension Guidelines",
            "AHA/ACC 2024 Hypertension Management Update",
            "ESC/ESH 2023 Hypertension Guidelines"
        ],
    },

    "Ramipril/Hydrochlorothiazide": {
        "group": "Cardiovascular - ACE Inhibitor + Diuretic (Fixed-Dose Combination)",
        "vietnamese_name": "Ramipril/HCTZ, Altace HCT",
        "administration": ["PO"],
        "indications": [
            "Tăng huyết áp (khi cần phối hợp ACE inhibitor và diuretic).",
        ],
        "contraindications": [
            "Dị ứng với ramipril, hydrochlorothiazide, hoặc sulfonamide.",
            "Có thai (ACE inhibitor chống chỉ định trong thai kỳ).",
            "Hẹp động mạch thận hai bên.",
            "Suy thận nặng (CrCl <30 ml/min).",
            "Hạ kali máu nặng.",
        ],
        "dosage": {
            "adult_initial": "Ramipril 2.5mg/HCTZ 12.5mg PO mỗi ngày.",
            "adult_maintenance": "Ramipril 5mg/HCTZ 12.5mg hoặc Ramipril 5mg/HCTZ 25mg PO mỗi ngày.",
            "notes": "Uống 1 lần/ngày, có thể uống với hoặc không thức ăn.",
        },
        "renal_adjustment": {
            "normal": "Không cần chỉnh liều.",
            "30_60": "Thận trọng, cân nhắc giảm liều hoặc dùng đơn trị.",
            "under_30": "Không dùng nếu CrCl <30 ml/min.",
        },
        "side_effects": [
            "Ho khan (do ACE inhibitor).",
            "Hạ huyết áp, chóng mặt.",
            "Hạ kali máu (do HCTZ).",
            "Tăng creatinin máu, suy thận cấp.",
            "Phù mạch (hiếm nhưng nghiêm trọng).",
            "Tăng đường huyết, tăng acid uric máu (do HCTZ).",
        ],
        "interactions": [
            "NSAIDs: tăng nguy cơ suy thận cấp.",
            "Kali-sparing diuretics, kali bổ sung: tăng nguy cơ tăng kali máu.",
            "Lithium: tăng nồng độ lithium.",
        ],
        "pregnancy": "D: chống chỉ định trong thai kỳ (ACE inhibitor).",
        "mechanism_of_action": (
            "Ramipril là ACE inhibitor, ức chế enzyme chuyển đổi angiotensin (ACE), "
            "giảm sản xuất angiotensin II, dẫn đến giãn mạch và giảm huyết áp. "
            "Hydrochlorothiazide là thiazide diuretic, ức chế tái hấp thu natri và nước ở ống lượn xa, "
            "dẫn đến lợi tiểu và giảm thể tích tuần hoàn. "
            "Phối hợp hai thuốc có tác dụng hiệp đồng giảm huyết áp mạnh hơn từng thuốc đơn trị."
        ),
        "monitoring": [
            "Huyết áp trước và trong điều trị.",
            "Creatinine, eGFR (CrCl) trước và trong điều trị - QUAN TRỌNG.",
            "Điện giải (Na+, K+, Cl-) trước và trong điều trị - đặc biệt kali máu.",
            "Dấu hiệu hạ huyết áp, chóng mặt.",
            "Dấu hiệu phù mạch (sưng mặt, môi, lưỡi, họng) - nguy hiểm.",
        ],
        "precautions": [
            "QUAN TRỌNG: Chống chỉ định trong thai kỳ - ACE inhibitor có thể gây dị tật thai nhi.",
            "Nguy cơ suy thận cấp - theo dõi creatinine chặt chẽ, đặc biệt khi bắt đầu hoặc tăng liều.",
            "Nguy cơ hạ kali máu - theo dõi kali máu, có thể cần bổ sung kali hoặc dùng kali-sparing diuretic.",
            "Nguy cơ phù mạch - ngừng ngay nếu có triệu chứng, điều trị bằng epinephrine.",
            "Không dùng nếu CrCl <30 ml/min.",
            "Thận trọng ở bệnh nhân suy tim, bệnh mạch vành.",
        ],
        "pharmacokinetics": {
            "half_life": "Ramipril: ~13-17 giờ; Ramiprilat: ~13-17 giờ; HCTZ: ~6-15 giờ.",
            "onset": "Giảm huyết áp trong vài giờ đến vài ngày.",
            "duration": "24 giờ (dùng 1 lần/ngày).",
            "protein_binding": "Ramipril: ~73%; HCTZ: ~40%.",
            "clearance": "Ramipril: thải qua thận; HCTZ: thải qua thận.",
        },
        "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm, tránh ánh sáng.",
        "black_box_warnings": (
            "Chống chỉ định trong thai kỳ: ACE inhibitor có thể gây dị tật thai nhi và tử vong thai nhi. "
            "Ngừng ngay khi phát hiện có thai. Phù mạch: có thể xảy ra và đe dọa tính mạng."
        ),
        "drug_interactions": {
            "major": [
                {
                    "drug": "NSAIDs (ibuprofen, naproxen, diclofenac)",
                    "mechanism": "NSAIDs giảm tác dụng giãn mạch của ACE inhibitor và giảm lưu lượng máu thận.",
                    "effect": "Tăng nguy cơ suy thận cấp, giảm hiệu quả hạ huyết áp.",
                    "management": "Thận trọng. Theo dõi chức năng thận chặt chẽ. Có thể cần giảm liều hoặc tránh NSAIDs.",
                },
                {
                    "drug": "Kali-sparing diuretics (spironolactone, eplerenone), Kali bổ sung",
                    "mechanism": "ACE inhibitor giảm bài tiết kali, HCTZ tăng bài tiết kali, nhưng tổng thể có thể tăng kali máu.",
                    "effect": "Tăng nguy cơ tăng kali máu, rối loạn nhịp tim.",
                    "management": "Thận trọng. Theo dõi kali máu chặt chẽ. Thường không nên dùng cùng kali-sparing diuretics.",
                },
            ],
            "moderate": [
                {
                    "drug": "Lithium",
                    "mechanism": "ACE inhibitor và HCTZ đều có thể tăng nồng độ lithium.",
                    "effect": "Tăng nguy cơ độc tính lithium.",
                    "management": "Thận trọng. Theo dõi nồng độ lithium chặt chẽ. Có thể cần giảm liều lithium.",
                },
            ],
            "minor": [],
        },
        "contraindications_detail": {
            "tuyệt_đối": [
                "Dị ứng với ramipril, hydrochlorothiazide, hoặc sulfonamide.",
                "Có thai hoặc có thể mang thai.",
                "Hẹp động mạch thận hai bên.",
                "Suy thận nặng (CrCl <30 ml/min).",
                "Hạ kali máu nặng.",
            ],
            "tương_đối": [
                "Suy thận trung bình (CrCl 30-60) - thận trọng.",
                "Suy tim nặng - thận trọng.",
                "Bệnh mạch vành - thận trọng.",
                "Tiền sử phù mạch - tránh dùng.",
            ],
        },
        "pregnancy_lactation": {
            "fda_category": "D",
            "pregnancy_details": (
                "Chống chỉ định trong thai kỳ. ACE inhibitor có thể gây dị tật thai nhi, "
                "suy thận thai nhi, giảm nước ối, và tử vong thai nhi. Ngừng ngay khi phát hiện có thai."
            ),
            "lactation": {
                "safety": "Caution",
                "details": "Ramipril và HCTZ đều bài tiết vào sữa mẹ.",
                "recommendation": "Thận trọng khi cho con bú. Cân nhắc ngừng cho con bú hoặc ngừng thuốc.",
            },
        },
        "hepatic_adjustment": {
            "mild": "Không cần chỉnh liều.",
            "moderate": "Thận trọng.",
            "severe": "Thận trọng, có thể cần giảm liều.",
            "notes": "Ramipril thải qua thận; HCTZ không chuyển hóa đáng kể qua gan.",
        },
        "overdose_management": {
            "symptoms": [
                "Hạ huyết áp nặng, sốc.",
                "Hạ kali máu, hạ natri máu.",
                "Suy thận cấp.",
            ],
            "antidote": "Không có antidote đặc hiệu.",
            "treatment": [
                "Điều trị hạ huyết áp: bù dịch, norepinephrine nếu cần.",
                "Điều trị hạ kali máu: bổ sung kali IV nếu cần.",
                "Điều trị suy thận cấp: bù dịch, theo dõi chức năng thận.",
            ],
            "monitoring": "Huyết áp, điện giải, chức năng thận, dấu hiệu sinh tồn.",
        },
        "reversal_agents": None,
        "administration_instructions": {
            "oral": {
                "with_food": "Có thể uống với hoặc không thức ăn.",
                "timing": "Uống 1 lần/ngày, cùng giờ mỗi ngày.",
            },
        },
        "references": {
            "primary_sources": [
                "FDA Drug Label - Altace HCT (ramipril/HCTZ)",
                "ACC/AHA Hypertension Guidelines 2024",
            ],
            "last_updated": "2025-02-18",
            "evidence_level": "High – FDA-approved",
        },
        "risk_flags": {
            "high_alert": True,
            "narrow_therapeutic_index": False,
            "icu_critical_care_only": False,
            "bleeding_risk": "Low",
            "organ_toxicity": {"renal": "Moderate", "pregnancy": "High (teratogenic)", "metabolic": "Moderate (hypokalemia)"}
        },
        "guideline_tags": [
            "AHA/ACC 2017 Hypertension Guidelines",
            "AHA/ACC 2024 Hypertension Management Update",
            "ESC/ESH 2023 Hypertension Guidelines"
        ],
    },

    "Perindopril/Amlodipine": {
        "group": "Cardiovascular - ACE Inhibitor + CCB (Fixed-Dose Combination)",
        "vietnamese_name": "Perindopril/Amlodipine, Prestalia",
        "administration": ["PO"],
        "indications": [
            "Tăng huyết áp (khi cần phối hợp ACE inhibitor và CCB).",
        ],
        "contraindications": [
            "Dị ứng với perindopril, amlodipine, hoặc dihydropyridine.",
            "Có thai (ACE inhibitor chống chỉ định trong thai kỳ).",
            "Hẹp động mạch thận hai bên.",
        ],
        "dosage": {
            "adult_initial": "Perindopril 3.5mg/Amlodipine 2.5mg PO mỗi ngày.",
            "adult_maintenance": "Perindopril 7mg/Amlodipine 5mg hoặc Perindopril 14mg/Amlodipine 10mg PO mỗi ngày.",
            "notes": "Uống 1 lần/ngày, có thể uống với hoặc không thức ăn.",
        },
        "renal_adjustment": {
            "normal": "Không cần chỉnh liều.",
            "30_60": "Thận trọng, có thể cần giảm liều perindopril.",
            "under_30": "Thận trọng, giảm liều perindopril.",
        },
        "side_effects": [
            "Ho khan (do ACE inhibitor).",
            "Phù chân (do amlodipine).",
            "Chóng mặt, hạ huyết áp.",
            "Đau đầu.",
            "Tăng creatinin máu.",
            "Phù mạch (hiếm nhưng nghiêm trọng).",
        ],
        "interactions": [
            "NSAIDs: tăng nguy cơ suy thận cấp.",
            "Kali-sparing diuretics, kali bổ sung: tăng nguy cơ tăng kali máu.",
        ],
        "pregnancy": "D: chống chỉ định trong thai kỳ (ACE inhibitor).",
        "mechanism_of_action": (
            "Perindopril là ACE inhibitor, ức chế enzyme chuyển đổi angiotensin (ACE), "
            "giảm sản xuất angiotensin II, dẫn đến giãn mạch và giảm huyết áp. "
            "Amlodipine là CCB dihydropyridine, ức chế kênh calci L-type, giãn mạch ngoại vi. "
            "Phối hợp hai thuốc có tác dụng hiệp đồng giảm huyết áp và giảm phù chân (ACE inhibitor đối kháng tác dụng phụ của CCB)."
        ),
        "monitoring": [
            "Huyết áp trước và trong điều trị.",
            "Creatinine, eGFR trước và trong điều trị.",
            "Dấu hiệu phù chân.",
            "Dấu hiệu phù mạch (sưng mặt, môi, lưỡi, họng) - nguy hiểm.",
        ],
        "precautions": [
            "Chống chỉ định trong thai kỳ - ACE inhibitor có thể gây dị tật thai nhi.",
            "Nguy cơ phù chân (do amlodipine) - có thể giảm khi phối hợp với ACE inhibitor.",
            "Nguy cơ suy thận cấp - theo dõi creatinine chặt chẽ.",
            "Nguy cơ phù mạch - ngừng ngay nếu có triệu chứng.",
        ],
        "pharmacokinetics": {
            "half_life": "Perindopril: ~17 giờ; Perindoprilat: ~17 giờ; Amlodipine: ~30-50 giờ.",
            "onset": "Giảm huyết áp trong vài giờ đến vài ngày.",
            "duration": "24 giờ (dùng 1 lần/ngày).",
            "protein_binding": "Perindopril: ~60%; Amlodipine: ~98%.",
            "clearance": "Perindopril: thải qua thận; Amlodipine: chuyển hóa ở gan.",
        },
        "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm, tránh ánh sáng.",
        "black_box_warnings": (
            "Chống chỉ định trong thai kỳ: ACE inhibitor có thể gây dị tật thai nhi và tử vong thai nhi. "
            "Ngừng ngay khi phát hiện có thai. Phù mạch: có thể xảy ra và đe dọa tính mạng."
        ),
        "drug_interactions": {
            "major": [
                {
                    "drug": "NSAIDs",
                    "mechanism": "Tăng nguy cơ suy thận cấp.",
                    "effect": "Suy thận cấp, giảm hiệu quả hạ huyết áp.",
                    "management": "Thận trọng. Theo dõi chức năng thận.",
                },
            ],
            "moderate": [],
            "minor": [],
        },
        "contraindications_detail": {
            "tuyệt_đối": [
                "Dị ứng với perindopril, amlodipine, hoặc dihydropyridine.",
                "Có thai hoặc có thể mang thai.",
                "Hẹp động mạch thận hai bên.",
            ],
            "tương_đối": [
                "Suy thận nặng (CrCl <30) - thận trọng.",
            ],
        },
        "pregnancy_lactation": {
            "fda_category": "D",
            "pregnancy_details": "Chống chỉ định trong thai kỳ. ACE inhibitor có thể gây dị tật thai nhi.",
            "lactation": {
                "safety": "Caution",
                "details": "Perindopril và amlodipine đều bài tiết vào sữa mẹ.",
                "recommendation": "Thận trọng khi cho con bú.",
            },
        },
        "hepatic_adjustment": {
            "mild": "Không cần chỉnh liều.",
            "moderate": "Thận trọng.",
            "severe": "Thận trọng, có thể cần giảm liều.",
            "notes": "Perindopril thải qua thận; amlodipine chuyển hóa ở gan.",
        },
        "overdose_management": {
            "symptoms": ["Hạ huyết áp nặng.", "Phù chân nặng."],
            "antidote": "Không có antidote đặc hiệu.",
            "treatment": ["Điều trị hạ huyết áp: bù dịch, norepinephrine nếu cần."],
            "monitoring": "Huyết áp, dấu hiệu sinh tồn.",
        },
        "reversal_agents": None,
        "administration_instructions": {
            "oral": {
                "with_food": "Có thể uống với hoặc không thức ăn.",
                "timing": "Uống 1 lần/ngày, cùng giờ mỗi ngày.",
            },
        },
        "references": {
            "primary_sources": ["FDA Drug Label - Prestalia (perindopril/amlodipine)", "ACC/AHA Guidelines 2024"],
            "last_updated": "2025-02-18",
            "evidence_level": "High – FDA-approved",
        },
        "risk_flags": {
            "high_alert": True,
            "narrow_therapeutic_index": False,
            "icu_critical_care_only": False,
            "bleeding_risk": "Low",
            "organ_toxicity": {"renal": "Moderate", "pregnancy": "High (teratogenic)"}
        },
        "guideline_tags": [
            "AHA/ACC 2017 Hypertension Guidelines",
            "AHA/ACC 2024 Hypertension Management Update",
            "ESC/ESH 2023 Hypertension Guidelines"
        ],
    },

    "Telmisartan/Hydrochlorothiazide": {
        "group": "Cardiovascular - ARB + Diuretic (Fixed-Dose Combination)",
        "vietnamese_name": "Telmisartan/HCTZ, Micardis HCT",
        "administration": ["PO"],
        "indications": [
            "Tăng huyết áp (khi cần phối hợp ARB và diuretic).",
        ],
        "contraindications": [
            "Dị ứng với telmisartan, hydrochlorothiazide, hoặc sulfonamide.",
            "Có thai (ARB chống chỉ định trong thai kỳ).",
            "Suy thận nặng (CrCl <30 ml/min).",
            "Hạ kali máu nặng.",
        ],
        "dosage": {
            "adult_initial": "Telmisartan 40mg/HCTZ 12.5mg PO mỗi ngày.",
            "adult_maintenance": "Telmisartan 80mg/HCTZ 12.5mg hoặc Telmisartan 80mg/HCTZ 25mg PO mỗi ngày.",
            "notes": "Uống 1 lần/ngày, có thể uống với hoặc không thức ăn.",
        },
        "renal_adjustment": {
            "normal": "Không cần chỉnh liều.",
            "30_60": "Thận trọng, cân nhắc giảm liều.",
            "under_30": "Không dùng nếu CrCl <30 ml/min.",
        },
        "side_effects": [
            "Chóng mặt, hạ huyết áp.",
            "Hạ kali máu (do HCTZ).",
            "Tăng creatinin máu.",
            "Tăng đường huyết, tăng acid uric máu (do HCTZ).",
        ],
        "interactions": [
            "NSAIDs: tăng nguy cơ suy thận cấp.",
            "Kali-sparing diuretics: tăng nguy cơ tăng kali máu.",
        ],
        "pregnancy": "D: chống chỉ định trong thai kỳ (ARB).",
        "mechanism_of_action": (
            "Telmisartan là ARB (Angiotensin Receptor Blocker), ức chế thụ thể AT1 của angiotensin II, "
            "dẫn đến giãn mạch và giảm huyết áp. Hydrochlorothiazide là thiazide diuretic, "
            "ức chế tái hấp thu natri và nước ở ống lượn xa. "
            "Phối hợp hai thuốc có tác dụng hiệp đồng giảm huyết áp."
        ),
        "monitoring": [
            "Huyết áp trước và trong điều trị.",
            "Creatinine, eGFR trước và trong điều trị.",
            "Điện giải (Na+, K+) trước và trong điều trị.",
        ],
        "precautions": [
            "Chống chỉ định trong thai kỳ - ARB có thể gây dị tật thai nhi.",
            "Nguy cơ suy thận cấp - theo dõi creatinine chặt chẽ.",
            "Nguy cơ hạ kali máu - theo dõi kali máu.",
            "Không dùng nếu CrCl <30 ml/min.",
        ],
        "pharmacokinetics": {
            "half_life": "Telmisartan: ~24 giờ; HCTZ: ~6-15 giờ.",
            "onset": "Giảm huyết áp trong vài giờ đến vài ngày.",
            "duration": "24 giờ (dùng 1 lần/ngày).",
            "protein_binding": "Telmisartan: ~99.5%; HCTZ: ~40%.",
            "clearance": "Telmisartan: không chuyển hóa, thải qua phân; HCTZ: thải qua thận.",
        },
        "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm, tránh ánh sáng.",
        "black_box_warnings": (
            "Chống chỉ định trong thai kỳ: ARB có thể gây dị tật thai nhi và tử vong thai nhi. "
            "Ngừng ngay khi phát hiện có thai."
        ),
        "drug_interactions": {
            "major": [
                {
                    "drug": "NSAIDs",
                    "mechanism": "Tăng nguy cơ suy thận cấp.",
                    "effect": "Suy thận cấp, giảm hiệu quả hạ huyết áp.",
                    "management": "Thận trọng. Theo dõi chức năng thận.",
                },
            ],
            "moderate": [],
            "minor": [],
        },
        "contraindications_detail": {
            "tuyệt_đối": [
                "Dị ứng với telmisartan, HCTZ, hoặc sulfonamide.",
                "Có thai hoặc có thể mang thai.",
                "Suy thận nặng (CrCl <30 ml/min).",
                "Hạ kali máu nặng.",
            ],
            "tương_đối": [
                "Suy thận trung bình (CrCl 30-60) - thận trọng.",
            ],
        },
        "pregnancy_lactation": {
            "fda_category": "D",
            "pregnancy_details": "Chống chỉ định trong thai kỳ. ARB có thể gây dị tật thai nhi.",
            "lactation": {
                "safety": "Caution",
                "details": "Telmisartan và HCTZ đều bài tiết vào sữa mẹ.",
                "recommendation": "Thận trọng khi cho con bú.",
            },
        },
        "hepatic_adjustment": {
            "mild": "Không cần chỉnh liều.",
            "moderate": "Thận trọng.",
            "severe": "Thận trọng, có thể cần giảm liều.",
            "notes": "Telmisartan không chuyển hóa qua gan; HCTZ không chuyển hóa đáng kể qua gan.",
        },
        "overdose_management": {
            "symptoms": ["Hạ huyết áp nặng.", "Hạ kali máu."],
            "antidote": "Không có antidote đặc hiệu.",
            "treatment": ["Điều trị hạ huyết áp: bù dịch.", "Điều trị hạ kali máu: bổ sung kali IV nếu cần."],
            "monitoring": "Huyết áp, điện giải, chức năng thận.",
        },
        "reversal_agents": None,
        "administration_instructions": {
            "oral": {
                "with_food": "Có thể uống với hoặc không thức ăn.",
                "timing": "Uống 1 lần/ngày, cùng giờ mỗi ngày.",
            },
        },
        "references": {
            "primary_sources": ["FDA Drug Label - Micardis HCT (telmisartan/HCTZ)", "ACC/AHA Guidelines 2024"],
            "last_updated": "2025-02-18",
            "evidence_level": "High – FDA-approved",
        },
        "risk_flags": {
            "high_alert": True,
            "narrow_therapeutic_index": False,
            "icu_critical_care_only": False,
            "bleeding_risk": "Low",
            "organ_toxicity": {"renal": "Moderate", "pregnancy": "High (teratogenic)", "metabolic": "Moderate (hypokalemia)"}
        },
        "guideline_tags": [
            "AHA/ACC 2017 Hypertension Guidelines",
            "AHA/ACC 2024 Hypertension Management Update",
            "ESC/ESH 2023 Hypertension Guidelines"
        ],
    },

    "Irbesartan/Hydrochlorothiazide": {
        "group": "Cardiovascular - ARB + Diuretic (Fixed-Dose Combination)",
        "vietnamese_name": "Irbesartan/HCTZ, Avalide",
        "administration": ["PO"],
        "indications": [
            "Tăng huyết áp (khi cần phối hợp ARB và diuretic).",
        ],
        "contraindications": [
            "Dị ứng với irbesartan, hydrochlorothiazide, hoặc sulfonamide.",
            "Có thai (ARB chống chỉ định trong thai kỳ).",
            "Suy thận nặng (CrCl <30 ml/min).",
            "Hạ kali máu nặng.",
        ],
        "dosage": {
            "adult_initial": "Irbesartan 150mg/HCTZ 12.5mg PO mỗi ngày.",
            "adult_maintenance": "Irbesartan 300mg/HCTZ 12.5mg hoặc Irbesartan 300mg/HCTZ 25mg PO mỗi ngày.",
            "notes": "Uống 1 lần/ngày, có thể uống với hoặc không thức ăn.",
        },
        "renal_adjustment": {
            "normal": "Không cần chỉnh liều.",
            "30_60": "Thận trọng, cân nhắc giảm liều.",
            "under_30": "Không dùng nếu CrCl <30 ml/min.",
        },
        "side_effects": [
            "Chóng mặt, hạ huyết áp.",
            "Hạ kali máu (do HCTZ).",
            "Tăng creatinin máu.",
            "Tăng đường huyết, tăng acid uric máu (do HCTZ).",
        ],
        "interactions": [
            "NSAIDs: tăng nguy cơ suy thận cấp.",
            "Kali-sparing diuretics: tăng nguy cơ tăng kali máu.",
        ],
        "pregnancy": "D: chống chỉ định trong thai kỳ (ARB).",
        "mechanism_of_action": (
            "Irbesartan là ARB (Angiotensin Receptor Blocker), ức chế thụ thể AT1 của angiotensin II, "
            "dẫn đến giãn mạch và giảm huyết áp. Hydrochlorothiazide là thiazide diuretic, "
            "ức chế tái hấp thu natri và nước ở ống lượn xa. "
            "Phối hợp hai thuốc có tác dụng hiệp đồng giảm huyết áp."
        ),
        "monitoring": [
            "Huyết áp trước và trong điều trị.",
            "Creatinine, eGFR trước và trong điều trị.",
            "Điện giải (Na+, K+) trước và trong điều trị.",
        ],
        "precautions": [
            "Chống chỉ định trong thai kỳ - ARB có thể gây dị tật thai nhi.",
            "Nguy cơ suy thận cấp - theo dõi creatinine chặt chẽ.",
            "Nguy cơ hạ kali máu - theo dõi kali máu.",
            "Không dùng nếu CrCl <30 ml/min.",
        ],
        "pharmacokinetics": {
            "half_life": "Irbesartan: ~11-15 giờ; HCTZ: ~6-15 giờ.",
            "onset": "Giảm huyết áp trong vài giờ đến vài ngày.",
            "duration": "24 giờ (dùng 1 lần/ngày).",
            "protein_binding": "Irbesartan: ~90%; HCTZ: ~40%.",
            "clearance": "Irbesartan: chuyển hóa ở gan; HCTZ: thải qua thận.",
        },
        "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm, tránh ánh sáng.",
        "black_box_warnings": (
            "Chống chỉ định trong thai kỳ: ARB có thể gây dị tật thai nhi và tử vong thai nhi. "
            "Ngừng ngay khi phát hiện có thai."
        ),
        "drug_interactions": {
            "major": [
                {
                    "drug": "NSAIDs",
                    "mechanism": "Tăng nguy cơ suy thận cấp.",
                    "effect": "Suy thận cấp, giảm hiệu quả hạ huyết áp.",
                    "management": "Thận trọng. Theo dõi chức năng thận.",
                },
            ],
            "moderate": [],
            "minor": [],
        },
        "contraindications_detail": {
            "tuyệt_đối": [
                "Dị ứng với irbesartan, HCTZ, hoặc sulfonamide.",
                "Có thai hoặc có thể mang thai.",
                "Suy thận nặng (CrCl <30 ml/min).",
                "Hạ kali máu nặng.",
            ],
            "tương_đối": [
                "Suy thận trung bình (CrCl 30-60) - thận trọng.",
            ],
        },
        "pregnancy_lactation": {
            "fda_category": "D",
            "pregnancy_details": "Chống chỉ định trong thai kỳ. ARB có thể gây dị tật thai nhi.",
            "lactation": {
                "safety": "Caution",
                "details": "Irbesartan và HCTZ đều bài tiết vào sữa mẹ.",
                "recommendation": "Thận trọng khi cho con bú.",
            },
        },
        "hepatic_adjustment": {
            "mild": "Không cần chỉnh liều.",
            "moderate": "Thận trọng.",
            "severe": "Thận trọng, có thể cần giảm liều.",
            "notes": "Irbesartan chuyển hóa ở gan; HCTZ không chuyển hóa đáng kể qua gan.",
        },
        "overdose_management": {
            "symptoms": ["Hạ huyết áp nặng.", "Hạ kali máu."],
            "antidote": "Không có antidote đặc hiệu.",
            "treatment": ["Điều trị hạ huyết áp: bù dịch.", "Điều trị hạ kali máu: bổ sung kali IV nếu cần."],
            "monitoring": "Huyết áp, điện giải, chức năng thận.",
        },
        "reversal_agents": None,
        "administration_instructions": {
            "oral": {
                "with_food": "Có thể uống với hoặc không thức ăn.",
                "timing": "Uống 1 lần/ngày, cùng giờ mỗi ngày.",
            },
        },
        "references": {
            "primary_sources": ["FDA Drug Label - Avalide (irbesartan/HCTZ)", "ACC/AHA Guidelines 2024"],
            "last_updated": "2025-02-18",
            "evidence_level": "High – FDA-approved",
        },
        "risk_flags": {
            "high_alert": True,
            "narrow_therapeutic_index": False,
            "icu_critical_care_only": False,
            "bleeding_risk": "Low",
            "organ_toxicity": {"renal": "Moderate", "pregnancy": "High (teratogenic)", "metabolic": "Moderate (hypokalemia)"}
        },
        "guideline_tags": [
            "AHA/ACC 2017 Hypertension Guidelines",
            "AHA/ACC 2024 Hypertension Management Update",
            "ESC/ESH 2023 Hypertension Guidelines"
        ],
    },

    "Candesartan/Hydrochlorothiazide": {
        "group": "Cardiovascular - ARB + Diuretic (Fixed-Dose Combination)",
        "vietnamese_name": "Candesartan/HCTZ, Atacand HCT",
        "administration": ["PO"],
        "indications": [
            "Tăng huyết áp (khi cần phối hợp ARB và diuretic).",
        ],
        "contraindications": [
            "Dị ứng với candesartan, hydrochlorothiazide, hoặc sulfonamide.",
            "Có thai (ARB chống chỉ định trong thai kỳ).",
            "Suy thận nặng (CrCl <30 ml/min).",
            "Hạ kali máu nặng.",
        ],
        "dosage": {
            "adult_initial": "Candesartan 16mg/HCTZ 12.5mg PO mỗi ngày.",
            "adult_maintenance": "Candesartan 32mg/HCTZ 12.5mg hoặc Candesartan 32mg/HCTZ 25mg PO mỗi ngày.",
            "notes": "Uống 1 lần/ngày, có thể uống với hoặc không thức ăn.",
        },
        "renal_adjustment": {
            "normal": "Không cần chỉnh liều.",
            "30_60": "Thận trọng, cân nhắc giảm liều.",
            "under_30": "Không dùng nếu CrCl <30 ml/min.",
        },
        "side_effects": [
            "Chóng mặt, hạ huyết áp.",
            "Hạ kali máu (do HCTZ).",
            "Tăng creatinin máu.",
            "Tăng đường huyết, tăng acid uric máu (do HCTZ).",
        ],
        "interactions": [
            "NSAIDs: tăng nguy cơ suy thận cấp.",
            "Kali-sparing diuretics: tăng nguy cơ tăng kali máu.",
        ],
        "pregnancy": "D: chống chỉ định trong thai kỳ (ARB).",
        "mechanism_of_action": (
            "Candesartan là ARB (Angiotensin Receptor Blocker), ức chế thụ thể AT1 của angiotensin II, "
            "dẫn đến giãn mạch và giảm huyết áp. Hydrochlorothiazide là thiazide diuretic, "
            "ức chế tái hấp thu natri và nước ở ống lượn xa. "
            "Phối hợp hai thuốc có tác dụng hiệp đồng giảm huyết áp."
        ),
        "monitoring": [
            "Huyết áp trước và trong điều trị.",
            "Creatinine, eGFR trước và trong điều trị.",
            "Điện giải (Na+, K+) trước và trong điều trị.",
        ],
        "precautions": [
            "Chống chỉ định trong thai kỳ - ARB có thể gây dị tật thai nhi.",
            "Nguy cơ suy thận cấp - theo dõi creatinine chặt chẽ.",
            "Nguy cơ hạ kali máu - theo dõi kali máu.",
            "Không dùng nếu CrCl <30 ml/min.",
        ],
        "pharmacokinetics": {
            "half_life": "Candesartan: ~9 giờ; HCTZ: ~6-15 giờ.",
            "onset": "Giảm huyết áp trong vài giờ đến vài ngày.",
            "duration": "24 giờ (dùng 1 lần/ngày).",
            "protein_binding": "Candesartan: ~99%; HCTZ: ~40%.",
            "clearance": "Candesartan: thải qua thận và gan; HCTZ: thải qua thận.",
        },
        "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm, tránh ánh sáng.",
        "black_box_warnings": (
            "Chống chỉ định trong thai kỳ: ARB có thể gây dị tật thai nhi và tử vong thai nhi. "
            "Ngừng ngay khi phát hiện có thai."
        ),
        "drug_interactions": {
            "major": [
                {
                    "drug": "NSAIDs",
                    "mechanism": "Tăng nguy cơ suy thận cấp.",
                    "effect": "Suy thận cấp, giảm hiệu quả hạ huyết áp.",
                    "management": "Thận trọng. Theo dõi chức năng thận.",
                },
            ],
            "moderate": [],
            "minor": [],
        },
        "contraindications_detail": {
            "tuyệt_đối": [
                "Dị ứng với candesartan, HCTZ, hoặc sulfonamide.",
                "Có thai hoặc có thể mang thai.",
                "Suy thận nặng (CrCl <30 ml/min).",
                "Hạ kali máu nặng.",
            ],
            "tương_đối": [
                "Suy thận trung bình (CrCl 30-60) - thận trọng.",
            ],
        },
        "pregnancy_lactation": {
            "fda_category": "D",
            "pregnancy_details": "Chống chỉ định trong thai kỳ. ARB có thể gây dị tật thai nhi.",
            "lactation": {
                "safety": "Caution",
                "details": "Candesartan và HCTZ đều bài tiết vào sữa mẹ.",
                "recommendation": "Thận trọng khi cho con bú.",
            },
        },
        "hepatic_adjustment": {
            "mild": "Không cần chỉnh liều.",
            "moderate": "Thận trọng.",
            "severe": "Thận trọng, có thể cần giảm liều.",
            "notes": "Candesartan thải qua cả gan và thận; HCTZ không chuyển hóa đáng kể qua gan.",
        },
        "overdose_management": {
            "symptoms": ["Hạ huyết áp nặng.", "Hạ kali máu."],
            "antidote": "Không có antidote đặc hiệu.",
            "treatment": ["Điều trị hạ huyết áp: bù dịch.", "Điều trị hạ kali máu: bổ sung kali IV nếu cần."],
            "monitoring": "Huyết áp, điện giải, chức năng thận.",
        },
        "reversal_agents": None,
        "administration_instructions": {
            "oral": {
                "with_food": "Có thể uống với hoặc không thức ăn.",
                "timing": "Uống 1 lần/ngày, cùng giờ mỗi ngày.",
            },
        },
        "references": {
            "primary_sources": ["FDA Drug Label - Atacand HCT (candesartan/HCTZ)", "ACC/AHA Guidelines 2024"],
            "last_updated": "2025-02-18",
            "evidence_level": "High – FDA-approved",
        },
        "risk_flags": {
            "high_alert": True,
            "narrow_therapeutic_index": False,
            "icu_critical_care_only": False,
            "bleeding_risk": "Low",
            "organ_toxicity": {"renal": "Moderate", "pregnancy": "High (teratogenic)", "metabolic": "Moderate (hypokalemia)"}
        },
        "guideline_tags": [
            "AHA/ACC 2017 Hypertension Guidelines",
            "AHA/ACC 2024 Hypertension Management Update",
            "ESC/ESH 2023 Hypertension Guidelines"
        ],
    },

    "Olmesartan/Hydrochlorothiazide": {
        "group": "Cardiovascular - ARB + Diuretic (Fixed-Dose Combination)",
        "vietnamese_name": "Olmesartan/HCTZ, Benicar HCT",
        "administration": ["PO"],
        "indications": [
            "Tăng huyết áp (khi cần phối hợp ARB và diuretic).",
        ],
        "contraindications": [
            "Dị ứng với olmesartan, hydrochlorothiazide, hoặc sulfonamide.",
            "Có thai (ARB chống chỉ định trong thai kỳ).",
            "Suy thận nặng (CrCl <30 ml/min).",
            "Hạ kali máu nặng.",
        ],
        "dosage": {
            "adult_initial": "Olmesartan 20mg/HCTZ 12.5mg PO mỗi ngày.",
            "adult_maintenance": "Olmesartan 40mg/HCTZ 12.5mg hoặc Olmesartan 40mg/HCTZ 25mg PO mỗi ngày.",
            "notes": "Uống 1 lần/ngày, có thể uống với hoặc không thức ăn.",
        },
        "renal_adjustment": {
            "normal": "Không cần chỉnh liều.",
            "30_60": "Thận trọng, cân nhắc giảm liều.",
            "under_30": "Không dùng nếu CrCl <30 ml/min.",
        },
        "side_effects": [
            "Chóng mặt, hạ huyết áp.",
            "Hạ kali máu (do HCTZ).",
            "Tăng creatinin máu.",
            "Tăng đường huyết, tăng acid uric máu (do HCTZ).",
        ],
        "interactions": [
            "NSAIDs: tăng nguy cơ suy thận cấp.",
            "Kali-sparing diuretics: tăng nguy cơ tăng kali máu.",
        ],
        "pregnancy": "D: chống chỉ định trong thai kỳ (ARB).",
        "mechanism_of_action": (
            "Olmesartan là ARB (Angiotensin Receptor Blocker), ức chế thụ thể AT1 của angiotensin II, "
            "dẫn đến giãn mạch và giảm huyết áp. Hydrochlorothiazide là thiazide diuretic, "
            "ức chế tái hấp thu natri và nước ở ống lượn xa. "
            "Phối hợp hai thuốc có tác dụng hiệp đồng giảm huyết áp."
        ),
        "monitoring": [
            "Huyết áp trước và trong điều trị.",
            "Creatinine, eGFR trước và trong điều trị.",
            "Điện giải (Na+, K+) trước và trong điều trị.",
        ],
        "precautions": [
            "Chống chỉ định trong thai kỳ - ARB có thể gây dị tật thai nhi.",
            "Nguy cơ suy thận cấp - theo dõi creatinine chặt chẽ.",
            "Nguy cơ hạ kali máu - theo dõi kali máu.",
            "Không dùng nếu CrCl <30 ml/min.",
        ],
        "pharmacokinetics": {
            "half_life": "Olmesartan: ~13 giờ; HCTZ: ~6-15 giờ.",
            "onset": "Giảm huyết áp trong vài giờ đến vài ngày.",
            "duration": "24 giờ (dùng 1 lần/ngày).",
            "protein_binding": "Olmesartan: ~99%; HCTZ: ~40%.",
            "clearance": "Olmesartan: không chuyển hóa, thải qua phân và nước tiểu; HCTZ: thải qua thận.",
        },
        "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm, tránh ánh sáng.",
        "black_box_warnings": (
            "Chống chỉ định trong thai kỳ: ARB có thể gây dị tật thai nhi và tử vong thai nhi. "
            "Ngừng ngay khi phát hiện có thai."
        ),
        "drug_interactions": {
            "major": [
                {
                    "drug": "NSAIDs",
                    "mechanism": "Tăng nguy cơ suy thận cấp.",
                    "effect": "Suy thận cấp, giảm hiệu quả hạ huyết áp.",
                    "management": "Thận trọng. Theo dõi chức năng thận.",
                },
            ],
            "moderate": [],
            "minor": [],
        },
        "contraindications_detail": {
            "tuyệt_đối": [
                "Dị ứng với olmesartan, HCTZ, hoặc sulfonamide.",
                "Có thai hoặc có thể mang thai.",
                "Suy thận nặng (CrCl <30 ml/min).",
                "Hạ kali máu nặng.",
            ],
            "tương_đối": [
                "Suy thận trung bình (CrCl 30-60) - thận trọng.",
            ],
        },
        "pregnancy_lactation": {
            "fda_category": "D",
            "pregnancy_details": "Chống chỉ định trong thai kỳ. ARB có thể gây dị tật thai nhi.",
            "lactation": {
                "safety": "Caution",
                "details": "Olmesartan và HCTZ đều bài tiết vào sữa mẹ.",
                "recommendation": "Thận trọng khi cho con bú.",
            },
        },
        "hepatic_adjustment": {
            "mild": "Không cần chỉnh liều.",
            "moderate": "Thận trọng.",
            "severe": "Thận trọng, có thể cần giảm liều.",
            "notes": "Olmesartan không chuyển hóa qua gan; HCTZ không chuyển hóa đáng kể qua gan.",
        },
        "overdose_management": {
            "symptoms": ["Hạ huyết áp nặng.", "Hạ kali máu."],
            "antidote": "Không có antidote đặc hiệu.",
            "treatment": ["Điều trị hạ huyết áp: bù dịch.", "Điều trị hạ kali máu: bổ sung kali IV nếu cần."],
            "monitoring": "Huyết áp, điện giải, chức năng thận.",
        },
        "reversal_agents": None,
        "administration_instructions": {
            "oral": {
                "with_food": "Có thể uống với hoặc không thức ăn.",
                "timing": "Uống 1 lần/ngày, cùng giờ mỗi ngày.",
            },
        },
        "references": {
            "primary_sources": ["FDA Drug Label - Benicar HCT (olmesartan/HCTZ)", "ACC/AHA Guidelines 2024"],
            "last_updated": "2025-02-18",
            "evidence_level": "High – FDA-approved",
        },
        "risk_flags": {
            "high_alert": True,
            "narrow_therapeutic_index": False,
            "icu_critical_care_only": False,
            "bleeding_risk": "Low",
            "organ_toxicity": {"renal": "Moderate", "pregnancy": "High (teratogenic)", "metabolic": "Moderate (hypokalemia)"}
        },
        "guideline_tags": [
            "AHA/ACC 2017 Hypertension Guidelines",
            "AHA/ACC 2024 Hypertension Management Update",
            "ESC/ESH 2023 Hypertension Guidelines"
        ],
    },

    "Losartan/Amlodipine": {
        "group": "Cardiovascular - ARB + CCB (Fixed-Dose Combination)",
        "vietnamese_name": "Losartan/Amlodipine, Twynsta",
        "administration": ["PO"],
        "indications": [
            "Tăng huyết áp (khi cần phối hợp ARB và CCB).",
        ],
        "contraindications": [
            "Dị ứng với losartan, amlodipine, hoặc dihydropyridine.",
            "Có thai (ARB chống chỉ định trong thai kỳ).",
        ],
        "dosage": {
            "adult_initial": "Losartan 50mg/Amlodipine 5mg PO mỗi ngày.",
            "adult_maintenance": "Losartan 100mg/Amlodipine 5mg hoặc Losartan 100mg/Amlodipine 10mg PO mỗi ngày.",
            "notes": "Uống 1 lần/ngày, có thể uống với hoặc không thức ăn.",
        },
        "renal_adjustment": {
            "normal": "Không cần chỉnh liều.",
            "30_60": "Không cần chỉnh liều.",
            "under_30": "Thận trọng, có thể cần giảm liều losartan.",
        },
        "side_effects": [
            "Phù chân (do amlodipine).",
            "Chóng mặt, hạ huyết áp.",
            "Đau đầu.",
            "Tăng creatinin máu.",
        ],
        "interactions": [
            "NSAIDs: tăng nguy cơ suy thận cấp.",
        ],
        "pregnancy": "D: chống chỉ định trong thai kỳ (ARB).",
        "mechanism_of_action": (
            "Losartan là ARB, ức chế thụ thể AT1 của angiotensin II, giãn mạch. "
            "Amlodipine là CCB dihydropyridine, ức chế kênh calci L-type, giãn mạch ngoại vi. "
            "Phối hợp hai thuốc có tác dụng hiệp đồng giảm huyết áp và giảm phù chân (ARB đối kháng tác dụng phụ của CCB)."
        ),
        "monitoring": [
            "Huyết áp trước và trong điều trị.",
            "Creatinine, eGFR trước và trong điều trị.",
            "Dấu hiệu phù chân.",
        ],
        "precautions": [
            "Chống chỉ định trong thai kỳ - ARB có thể gây dị tật thai nhi.",
            "Nguy cơ phù chân (do amlodipine) - có thể giảm khi phối hợp với ARB.",
            "Nguy cơ suy thận cấp - theo dõi creatinine chặt chẽ.",
        ],
        "pharmacokinetics": {
            "half_life": "Losartan: ~2 giờ (losartan), ~6-9 giờ (metabolite); Amlodipine: ~30-50 giờ.",
            "onset": "Giảm huyết áp trong vài giờ đến vài ngày.",
            "duration": "24 giờ (dùng 1 lần/ngày).",
            "protein_binding": "Losartan: ~99%; Amlodipine: ~98%.",
            "clearance": "Losartan: chuyển hóa ở gan; Amlodipine: chuyển hóa ở gan.",
        },
        "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm, tránh ánh sáng.",
        "black_box_warnings": (
            "Chống chỉ định trong thai kỳ: ARB có thể gây dị tật thai nhi và tử vong thai nhi. "
            "Ngừng ngay khi phát hiện có thai."
        ),
        "drug_interactions": {
            "major": [
                {
                    "drug": "NSAIDs",
                    "mechanism": "Tăng nguy cơ suy thận cấp.",
                    "effect": "Suy thận cấp.",
                    "management": "Thận trọng. Theo dõi chức năng thận.",
                },
            ],
            "moderate": [],
            "minor": [],
        },
        "contraindications_detail": {
            "tuyệt_đối": [
                "Dị ứng với losartan, amlodipine, hoặc dihydropyridine.",
                "Có thai hoặc có thể mang thai.",
            ],
            "tương_đối": [
                "Suy thận nặng (CrCl <30) - thận trọng.",
            ],
        },
        "pregnancy_lactation": {
            "fda_category": "D",
            "pregnancy_details": "Chống chỉ định trong thai kỳ. ARB có thể gây dị tật thai nhi.",
            "lactation": {
                "safety": "Caution",
                "details": "Losartan và amlodipine đều bài tiết vào sữa mẹ.",
                "recommendation": "Thận trọng khi cho con bú.",
            },
        },
        "hepatic_adjustment": {
            "mild": "Không cần chỉnh liều.",
            "moderate": "Thận trọng.",
            "severe": "Thận trọng, có thể cần giảm liều.",
            "notes": "Losartan và amlodipine đều chuyển hóa ở gan.",
        },
        "overdose_management": {
            "symptoms": ["Hạ huyết áp nặng.", "Phù chân nặng."],
            "antidote": "Không có antidote đặc hiệu.",
            "treatment": ["Điều trị hạ huyết áp: bù dịch, norepinephrine nếu cần."],
            "monitoring": "Huyết áp, dấu hiệu sinh tồn.",
        },
        "reversal_agents": None,
        "administration_instructions": {
            "oral": {
                "with_food": "Có thể uống với hoặc không thức ăn.",
                "timing": "Uống 1 lần/ngày, cùng giờ mỗi ngày.",
            },
        },
        "references": {
            "primary_sources": ["FDA Drug Label - Twynsta (losartan/amlodipine)", "ACC/AHA Guidelines 2024"],
            "last_updated": "2025-02-18",
            "evidence_level": "High – FDA-approved",
        },
        "risk_flags": {
            "high_alert": True,
            "narrow_therapeutic_index": False,
            "icu_critical_care_only": False,
            "bleeding_risk": "Low",
            "organ_toxicity": {"renal": "Moderate", "pregnancy": "High (teratogenic)"}
        },
        "guideline_tags": [
            "AHA/ACC 2017 Hypertension Guidelines",
            "AHA/ACC 2024 Hypertension Management Update",
            "ESC/ESH 2023 Hypertension Guidelines"
        ],
    },

    "Telmisartan/Amlodipine": {
        "group": "Cardiovascular - ARB + CCB (Fixed-Dose Combination)",
        "vietnamese_name": "Telmisartan/Amlodipine, Twynsta",
        "administration": ["PO"],
        "indications": [
            "Tăng huyết áp (khi cần phối hợp ARB và CCB).",
        ],
        "contraindications": [
            "Dị ứng với telmisartan, amlodipine, hoặc dihydropyridine.",
            "Có thai (ARB chống chỉ định trong thai kỳ).",
        ],
        "dosage": {
            "adult_initial": "Telmisartan 40mg/Amlodipine 5mg PO mỗi ngày.",
            "adult_maintenance": "Telmisartan 80mg/Amlodipine 5mg hoặc Telmisartan 80mg/Amlodipine 10mg PO mỗi ngày.",
            "notes": "Uống 1 lần/ngày, có thể uống với hoặc không thức ăn.",
        },
        "renal_adjustment": {
            "normal": "Không cần chỉnh liều.",
            "30_60": "Không cần chỉnh liều.",
            "under_30": "Thận trọng, có thể cần giảm liều telmisartan.",
        },
        "side_effects": [
            "Phù chân (do amlodipine).",
            "Chóng mặt, hạ huyết áp.",
            "Đau đầu.",
            "Tăng creatinin máu.",
        ],
        "interactions": [
            "NSAIDs: tăng nguy cơ suy thận cấp.",
        ],
        "pregnancy": "D: chống chỉ định trong thai kỳ (ARB).",
        "mechanism_of_action": (
            "Telmisartan là ARB, ức chế thụ thể AT1 của angiotensin II, giãn mạch. "
            "Amlodipine là CCB dihydropyridine, ức chế kênh calci L-type, giãn mạch ngoại vi. "
            "Phối hợp hai thuốc có tác dụng hiệp đồng giảm huyết áp và giảm phù chân (ARB đối kháng tác dụng phụ của CCB)."
        ),
        "monitoring": [
            "Huyết áp trước và trong điều trị.",
            "Creatinine, eGFR trước và trong điều trị.",
            "Dấu hiệu phù chân.",
        ],
        "precautions": [
            "Chống chỉ định trong thai kỳ - ARB có thể gây dị tật thai nhi.",
            "Nguy cơ phù chân (do amlodipine) - có thể giảm khi phối hợp với ARB.",
            "Nguy cơ suy thận cấp - theo dõi creatinine chặt chẽ.",
        ],
        "pharmacokinetics": {
            "half_life": "Telmisartan: ~24 giờ; Amlodipine: ~30-50 giờ.",
            "onset": "Giảm huyết áp trong vài giờ đến vài ngày.",
            "duration": "24 giờ (dùng 1 lần/ngày).",
            "protein_binding": "Telmisartan: ~99.5%; Amlodipine: ~98%.",
            "clearance": "Telmisartan: không chuyển hóa, thải qua phân; Amlodipine: chuyển hóa ở gan.",
        },
        "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm, tránh ánh sáng.",
        "black_box_warnings": (
            "Chống chỉ định trong thai kỳ: ARB có thể gây dị tật thai nhi và tử vong thai nhi. "
            "Ngừng ngay khi phát hiện có thai."
        ),
        "drug_interactions": {
            "major": [
                {
                    "drug": "NSAIDs",
                    "mechanism": "Tăng nguy cơ suy thận cấp.",
                    "effect": "Suy thận cấp.",
                    "management": "Thận trọng. Theo dõi chức năng thận.",
                },
            ],
            "moderate": [],
            "minor": [],
        },
        "contraindications_detail": {
            "tuyệt_đối": [
                "Dị ứng với telmisartan, amlodipine, hoặc dihydropyridine.",
                "Có thai hoặc có thể mang thai.",
            ],
            "tương_đối": [
                "Suy thận nặng (CrCl <30) - thận trọng.",
            ],
        },
        "pregnancy_lactation": {
            "fda_category": "D",
            "pregnancy_details": "Chống chỉ định trong thai kỳ. ARB có thể gây dị tật thai nhi.",
            "lactation": {
                "safety": "Caution",
                "details": "Telmisartan và amlodipine đều bài tiết vào sữa mẹ.",
                "recommendation": "Thận trọng khi cho con bú.",
            },
        },
        "hepatic_adjustment": {
            "mild": "Không cần chỉnh liều.",
            "moderate": "Thận trọng.",
            "severe": "Thận trọng, có thể cần giảm liều.",
            "notes": "Telmisartan không chuyển hóa qua gan; amlodipine chuyển hóa ở gan.",
        },
        "overdose_management": {
            "symptoms": ["Hạ huyết áp nặng.", "Phù chân nặng."],
            "antidote": "Không có antidote đặc hiệu.",
            "treatment": ["Điều trị hạ huyết áp: bù dịch, norepinephrine nếu cần."],
            "monitoring": "Huyết áp, dấu hiệu sinh tồn.",
        },
        "reversal_agents": None,
        "administration_instructions": {
            "oral": {
                "with_food": "Có thể uống với hoặc không thức ăn.",
                "timing": "Uống 1 lần/ngày, cùng giờ mỗi ngày.",
            },
        },
        "references": {
            "primary_sources": ["FDA Drug Label - Twynsta (telmisartan/amlodipine)", "ACC/AHA Guidelines 2024"],
            "last_updated": "2025-02-18",
            "evidence_level": "High – FDA-approved",
        },
        "risk_flags": {
            "high_alert": True,
            "narrow_therapeutic_index": False,
            "icu_critical_care_only": False,
            "bleeding_risk": "Low",
            "organ_toxicity": {"renal": "Moderate", "pregnancy": "High (teratogenic)"}
        },
        "guideline_tags": [
            "AHA/ACC 2017 Hypertension Guidelines",
            "AHA/ACC 2024 Hypertension Management Update",
            "ESC/ESH 2023 Hypertension Guidelines"
        ],
    },

    "Atenolol/Chlorthalidone": {
        "group": "Cardiovascular - Beta-blocker + Diuretic (Fixed-Dose Combination)",
        "vietnamese_name": "Atenolol/Chlorthalidone, Tenoretic",
        "administration": ["PO"],
        "indications": [
            "Tăng huyết áp (khi cần phối hợp beta-blocker và diuretic).",
        ],
        "contraindications": [
            "Dị ứng với atenolol, chlorthalidone, hoặc sulfonamide.",
            "Hen phế quản nặng, COPD nặng.",
            "Block nhĩ thất độ 2-3.",
            "Suy tim cấp.",
            "Nhịp tim chậm nặng (<50 bpm).",
            "Suy thận nặng (CrCl <30 ml/min).",
            "Hạ kali máu nặng.",
        ],
        "dosage": {
            "adult_initial": "Atenolol 50mg/Chlorthalidone 25mg PO mỗi ngày.",
            "adult_maintenance": "Atenolol 50mg/Chlorthalidone 25mg hoặc Atenolol 100mg/Chlorthalidone 25mg PO mỗi ngày.",
            "notes": "Uống 1 lần/ngày, có thể uống với hoặc không thức ăn.",
        },
        "renal_adjustment": {
            "normal": "Không cần chỉnh liều.",
            "30_60": "Thận trọng, giảm liều atenolol 50%.",
            "under_30": "Không dùng nếu CrCl <30 ml/min.",
        },
        "side_effects": [
            "Mệt mỏi, lạnh tay chân (do beta-blocker).",
            "Nhịp tim chậm.",
            "Hạ kali máu (do chlorthalidone).",
            "Hạ huyết áp, chóng mặt.",
            "Tăng đường huyết, tăng acid uric máu (do chlorthalidone).",
            "Rối loạn cương dương (do beta-blocker).",
        ],
        "interactions": [
            "Verapamil, Diltiazem: tăng nguy cơ block AV, nhịp tim chậm.",
            "Insulin, thuốc hạ đường huyết: tăng nguy cơ hạ đường huyết, che dấu triệu chứng hạ đường huyết.",
            "Digoxin: tăng nguy cơ block AV.",
        ],
        "pregnancy": "D: chống chỉ định trong thai kỳ (beta-blocker có thể gây chậm phát triển thai nhi).",
        "mechanism_of_action": (
            "Atenolol là beta-1 selective blocker, ức chế thụ thể beta-1 ở tim, giảm nhịp tim và co bóp cơ tim, "
            "giảm cung lượng tim và giảm huyết áp. Chlorthalidone là thiazide-like diuretic, "
            "ức chế tái hấp thu natri và nước ở ống lượn xa, dẫn đến lợi tiểu và giảm thể tích tuần hoàn. "
            "Phối hợp hai thuốc có tác dụng hiệp đồng giảm huyết áp."
        ),
        "monitoring": [
            "Huyết áp trước và trong điều trị.",
            "Nhịp tim - nhịp tim chậm phổ biến.",
            "Điện giải (Na+, K+) trước và trong điều trị - đặc biệt kali máu.",
            "Đường huyết - chlorthalidone có thể tăng đường huyết.",
            "Chức năng thận (creatinine, eGFR) - atenolol thải qua thận.",
        ],
        "precautions": [
            "CHỐNG CHỈ ĐỊNH trong hen phế quản nặng, COPD nặng - có thể gây co thắt phế quản.",
            "CHỐNG CHỈ ĐỊNH trong block AV độ 2-3 - có thể làm nặng block.",
            "CHỐNG CHỈ ĐỊNH trong suy tim cấp - có thể làm nặng suy tim.",
            "KHÔNG ngừng đột ngột - phải giảm liều dần trong 1-2 tuần (rebound hypertension, đau thắt ngực).",
            "Nguy cơ hạ kali máu - theo dõi kali máu, có thể cần bổ sung kali.",
            "Nguy cơ che dấu triệu chứng hạ đường huyết ở bệnh nhân đái tháo đường.",
            "Không dùng nếu CrCl <30 ml/min.",
        ],
        "pharmacokinetics": {
            "half_life": "Atenolol: ~6-7 giờ; Chlorthalidone: ~40-60 giờ (rất dài).",
            "onset": "Giảm huyết áp trong vài giờ đến vài ngày.",
            "duration": "24 giờ (dùng 1 lần/ngày).",
            "protein_binding": "Atenolol: ~5-15%; Chlorthalidone: ~75%.",
            "clearance": "Atenolol: thải qua thận; Chlorthalidone: thải qua thận.",
        },
        "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm, tránh ánh sáng.",
        "black_box_warnings": (
            "KHÔNG ngừng đột ngột: Có thể gây rebound hypertension, đau thắt ngực, nhồi máu cơ tim. "
            "Phải giảm liều dần trong 1-2 tuần. Chống chỉ định trong thai kỳ: Beta-blocker có thể gây chậm phát triển thai nhi."
        ),
        "drug_interactions": {
            "major": [
                {
                    "drug": "Verapamil, Diltiazem (CCB non-dihydropyridine)",
                    "mechanism": "Cả hai đều làm chậm dẫn truyền AV và giảm nhịp tim.",
                    "effect": "Tăng nguy cơ block AV độ 2-3, nhịp tim chậm nghiêm trọng, suy tim.",
                    "management": "Thận trọng. Theo dõi ECG, nhịp tim chặt chẽ. Tránh dùng cùng nếu có thể.",
                },
            ],
            "moderate": [
                {
                    "drug": "Digoxin",
                    "mechanism": "Cả hai đều làm chậm dẫn truyền AV.",
                    "effect": "Tăng nguy cơ block AV.",
                    "management": "Thận trọng. Theo dõi ECG, nhịp tim.",
                },
                {
                    "drug": "Insulin, thuốc hạ đường huyết",
                    "mechanism": "Beta-blocker che dấu triệu chứng hạ đường huyết (nhịp tim nhanh, run), chlorthalidone có thể tăng đường huyết.",
                    "effect": "Tăng nguy cơ hạ đường huyết không được phát hiện, hoặc tăng đường huyết.",
                    "management": "Thận trọng. Theo dõi đường huyết chặt chẽ. Theo dõi các triệu chứng hạ đường huyết khác (đổ mồ hôi, lú lẫn).",
                },
            ],
            "minor": [],
        },
        "contraindications_detail": {
            "tuyệt_đối": [
                "Dị ứng với atenolol, chlorthalidone, hoặc sulfonamide.",
                "Hen phế quản nặng, COPD nặng.",
                "Block nhĩ thất độ 2-3.",
                "Suy tim cấp.",
                "Nhịp tim chậm nặng (<50 bpm).",
                "Suy thận nặng (CrCl <30 ml/min).",
                "Hạ kali máu nặng.",
            ],
            "tương_đối": [
                "Suy tim mạn tính - thận trọng, có thể dùng ở suy tim mạn tính được điều trị.",
                "Suy thận trung bình (CrCl 30-60) - thận trọng, giảm liều atenolol.",
                "Đái tháo đường - thận trọng, che dấu triệu chứng hạ đường huyết.",
                "Bệnh mạch vành - thận trọng, không ngừng đột ngột.",
            ],
        },
        "pregnancy_lactation": {
            "fda_category": "D",
            "pregnancy_details": (
                "Chống chỉ định trong thai kỳ. Beta-blocker có thể gây chậm phát triển thai nhi, "
                "nhịp tim chậm ở thai nhi, hạ đường huyết ở trẻ sơ sinh. Ngừng ngay khi phát hiện có thai."
            ),
            "lactation": {
                "safety": "Caution",
                "details": "Atenolol và chlorthalidone đều bài tiết vào sữa mẹ.",
                "recommendation": "Thận trọng khi cho con bú. Cân nhắc ngừng cho con bú hoặc ngừng thuốc.",
            },
        },
        "hepatic_adjustment": {
            "mild": "Không cần chỉnh liều.",
            "moderate": "Không cần chỉnh liều.",
            "severe": "Không cần chỉnh liều.",
            "notes": "Atenolol và chlorthalidone đều thải qua thận, không chuyển hóa đáng kể qua gan.",
        },
        "overdose_management": {
            "symptoms": [
                "Nhịp tim chậm nghiêm trọng, block AV.",
                "Hạ huyết áp nặng.",
                "Hạ kali máu.",
                "Suy tim cấp.",
            ],
            "antidote": "Atropine cho nhịp tim chậm, Glucagon cho beta-blocker overdose.",
            "treatment": [
                "Điều trị nhịp tim chậm: Atropine 0.5-1mg IV, nếu cần: pacemaker tạm thời.",
                "Điều trị hạ huyết áp: Truyền dịch, glucagon 1-5mg IV (cho beta-blocker overdose), nếu cần: dopamine, norepinephrine.",
                "Điều trị hạ kali máu: Bổ sung kali IV nếu cần.",
                "Theo dõi ECG liên tục.",
            ],
            "monitoring": "ECG, nhịp tim, huyết áp, điện giải, chức năng thận.",
        },
        "reversal_agents": {
            "available": True,
            "agents": ["Atropine (cho nhịp tim chậm)", "Glucagon (cho beta-blocker overdose)"]
        },
        "administration_instructions": {
            "oral": {
                "with_food": "Có thể uống với hoặc không thức ăn.",
                "timing": "Uống 1 lần/ngày, cùng giờ mỗi ngày. KHÔNG ngừng đột ngột - phải giảm liều dần trong 1-2 tuần.",
            },
        },
        "references": {
            "primary_sources": [
                "FDA Drug Label - Tenoretic (atenolol/chlorthalidone)",
                "ACC/AHA Hypertension Guidelines 2024",
            ],
            "last_updated": "2025-02-18",
            "evidence_level": "High – FDA-approved",
        },
        "risk_flags": {
            "high_alert": True,
            "narrow_therapeutic_index": False,
            "icu_critical_care_only": False,
            "bleeding_risk": "Low",
            "organ_toxicity": {"cardiovascular": "High (bradycardia, AV block)", "metabolic": "Moderate (hypokalemia, hyperglycemia)"}
        },
        "guideline_tags": [
            "AHA/ACC 2017 Hypertension Guidelines",
            "AHA/ACC 2024 Hypertension Management Update",
            "ESC/ESH 2023 Hypertension Guidelines"
        ],
    },

    "Metoprolol/Hydrochlorothiazide": {
        "group": "Cardiovascular - Beta-blocker + Diuretic (Fixed-Dose Combination)",
        "vietnamese_name": "Metoprolol/HCTZ, Lopressor HCT",
        "administration": ["PO"],
        "indications": [
            "Tăng huyết áp (khi cần phối hợp beta-blocker và diuretic).",
        ],
        "contraindications": [
            "Dị ứng với metoprolol, hydrochlorothiazide, hoặc sulfonamide.",
            "Hen phế quản nặng, COPD nặng.",
            "Block nhĩ thất độ 2-3.",
            "Suy tim cấp.",
            "Nhịp tim chậm nặng (<50 bpm).",
            "Suy thận nặng (CrCl <30 ml/min).",
            "Hạ kali máu nặng.",
        ],
        "dosage": {
            "adult_initial": "Metoprolol 50mg/HCTZ 25mg PO x 1-2 lần/ngày.",
            "adult_maintenance": "Metoprolol 100mg/HCTZ 25mg x 1-2 lần/ngày hoặc Metoprolol 100mg/HCTZ 50mg x 1-2 lần/ngày.",
            "notes": "Uống 1-2 lần/ngày tùy liều, có thể uống với hoặc không thức ăn.",
        },
        "renal_adjustment": {
            "normal": "Không cần chỉnh liều.",
            "30_60": "Thận trọng, có thể cần giảm liều.",
            "under_30": "Không dùng nếu CrCl <30 ml/min.",
        },
        "side_effects": [
            "Mệt mỏi, lạnh tay chân (do beta-blocker).",
            "Nhịp tim chậm.",
            "Hạ kali máu (do HCTZ).",
            "Hạ huyết áp, chóng mặt.",
            "Tăng đường huyết, tăng acid uric máu (do HCTZ).",
            "Rối loạn cương dương (do beta-blocker).",
        ],
        "interactions": [
            "Verapamil, Diltiazem: tăng nguy cơ block AV, nhịp tim chậm.",
            "Insulin, thuốc hạ đường huyết: tăng nguy cơ hạ đường huyết, che dấu triệu chứng hạ đường huyết.",
            "Digoxin: tăng nguy cơ block AV.",
        ],
        "pregnancy": "D: chống chỉ định trong thai kỳ (beta-blocker có thể gây chậm phát triển thai nhi).",
        "mechanism_of_action": (
            "Metoprolol là beta-1 selective blocker, ức chế thụ thể beta-1 ở tim, giảm nhịp tim và co bóp cơ tim, "
            "giảm cung lượng tim và giảm huyết áp. Hydrochlorothiazide là thiazide diuretic, "
            "ức chế tái hấp thu natri và nước ở ống lượn xa, dẫn đến lợi tiểu và giảm thể tích tuần hoàn. "
            "Phối hợp hai thuốc có tác dụng hiệp đồng giảm huyết áp."
        ),
        "monitoring": [
            "Huyết áp trước và trong điều trị.",
            "Nhịp tim - nhịp tim chậm phổ biến.",
            "Điện giải (Na+, K+) trước và trong điều trị - đặc biệt kali máu.",
            "Đường huyết - HCTZ có thể tăng đường huyết.",
            "Chức năng thận (creatinine, eGFR).",
        ],
        "precautions": [
            "CHỐNG CHỈ ĐỊNH trong hen phế quản nặng, COPD nặng - có thể gây co thắt phế quản.",
            "CHỐNG CHỈ ĐỊNH trong block AV độ 2-3 - có thể làm nặng block.",
            "CHỐNG CHỈ ĐỊNH trong suy tim cấp - có thể làm nặng suy tim.",
            "KHÔNG ngừng đột ngột - phải giảm liều dần trong 1-2 tuần (rebound hypertension, đau thắt ngực).",
            "Nguy cơ hạ kali máu - theo dõi kali máu, có thể cần bổ sung kali.",
            "Nguy cơ che dấu triệu chứng hạ đường huyết ở bệnh nhân đái tháo đường.",
            "Không dùng nếu CrCl <30 ml/min.",
        ],
        "pharmacokinetics": {
            "half_life": "Metoprolol: ~3-7 giờ (immediate release), ~24 giờ (extended release); HCTZ: ~6-15 giờ.",
            "onset": "Giảm huyết áp trong vài giờ đến vài ngày.",
            "duration": "12-24 giờ tùy dạng (immediate release: 1-2 lần/ngày, extended release: 1 lần/ngày).",
            "protein_binding": "Metoprolol: ~12%; HCTZ: ~40%.",
            "clearance": "Metoprolol: chuyển hóa ở gan; HCTZ: thải qua thận.",
        },
        "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm, tránh ánh sáng.",
        "black_box_warnings": (
            "KHÔNG ngừng đột ngột: Có thể gây rebound hypertension, đau thắt ngực, nhồi máu cơ tim. "
            "Phải giảm liều dần trong 1-2 tuần. Chống chỉ định trong thai kỳ: Beta-blocker có thể gây chậm phát triển thai nhi."
        ),
        "drug_interactions": {
            "major": [
                {
                    "drug": "Verapamil, Diltiazem (CCB non-dihydropyridine)",
                    "mechanism": "Cả hai đều làm chậm dẫn truyền AV và giảm nhịp tim.",
                    "effect": "Tăng nguy cơ block AV độ 2-3, nhịp tim chậm nghiêm trọng, suy tim.",
                    "management": "Thận trọng. Theo dõi ECG, nhịp tim chặt chẽ. Tránh dùng cùng nếu có thể.",
                },
            ],
            "moderate": [
                {
                    "drug": "Digoxin",
                    "mechanism": "Cả hai đều làm chậm dẫn truyền AV.",
                    "effect": "Tăng nguy cơ block AV.",
                    "management": "Thận trọng. Theo dõi ECG, nhịp tim.",
                },
                {
                    "drug": "Insulin, thuốc hạ đường huyết",
                    "mechanism": "Beta-blocker che dấu triệu chứng hạ đường huyết (nhịp tim nhanh, run), HCTZ có thể tăng đường huyết.",
                    "effect": "Tăng nguy cơ hạ đường huyết không được phát hiện, hoặc tăng đường huyết.",
                    "management": "Thận trọng. Theo dõi đường huyết chặt chẽ. Theo dõi các triệu chứng hạ đường huyết khác (đổ mồ hôi, lú lẫn).",
                },
            ],
            "minor": [],
        },
        "contraindications_detail": {
            "tuyệt_đối": [
                "Dị ứng với metoprolol, hydrochlorothiazide, hoặc sulfonamide.",
                "Hen phế quản nặng, COPD nặng.",
                "Block nhĩ thất độ 2-3.",
                "Suy tim cấp.",
                "Nhịp tim chậm nặng (<50 bpm).",
                "Suy thận nặng (CrCl <30 ml/min).",
                "Hạ kali máu nặng.",
            ],
            "tương_đối": [
                "Suy tim mạn tính - thận trọng, có thể dùng ở suy tim mạn tính được điều trị.",
                "Suy thận trung bình (CrCl 30-60) - thận trọng.",
                "Đái tháo đường - thận trọng, che dấu triệu chứng hạ đường huyết.",
                "Bệnh mạch vành - thận trọng, không ngừng đột ngột.",
            ],
        },
        "pregnancy_lactation": {
            "fda_category": "D",
            "pregnancy_details": (
                "Chống chỉ định trong thai kỳ. Beta-blocker có thể gây chậm phát triển thai nhi, "
                "nhịp tim chậm ở thai nhi, hạ đường huyết ở trẻ sơ sinh. Ngừng ngay khi phát hiện có thai."
            ),
            "lactation": {
                "safety": "Caution",
                "details": "Metoprolol và HCTZ đều bài tiết vào sữa mẹ.",
                "recommendation": "Thận trọng khi cho con bú. Cân nhắc ngừng cho con bú hoặc ngừng thuốc.",
            },
        },
        "hepatic_adjustment": {
            "mild": "Không cần chỉnh liều.",
            "moderate": "Thận trọng, có thể cần giảm liều metoprolol.",
            "severe": "Thận trọng, giảm liều metoprolol.",
            "notes": "Metoprolol chuyển hóa ở gan; HCTZ không chuyển hóa đáng kể qua gan.",
        },
        "overdose_management": {
            "symptoms": [
                "Nhịp tim chậm nghiêm trọng, block AV.",
                "Hạ huyết áp nặng.",
                "Hạ kali máu.",
                "Suy tim cấp.",
            ],
            "antidote": "Atropine cho nhịp tim chậm, Glucagon cho beta-blocker overdose.",
            "treatment": [
                "Điều trị nhịp tim chậm: Atropine 0.5-1mg IV, nếu cần: pacemaker tạm thời.",
                "Điều trị hạ huyết áp: Truyền dịch, glucagon 1-5mg IV (cho beta-blocker overdose), nếu cần: dopamine, norepinephrine.",
                "Điều trị hạ kali máu: Bổ sung kali IV nếu cần.",
                "Theo dõi ECG liên tục.",
            ],
            "monitoring": "ECG, nhịp tim, huyết áp, điện giải, chức năng thận.",
        },
        "reversal_agents": {
            "available": True,
            "agents": ["Atropine (cho nhịp tim chậm)", "Glucagon (cho beta-blocker overdose)"]
        },
        "administration_instructions": {
            "oral": {
                "with_food": "Có thể uống với hoặc không thức ăn.",
                "timing": "Uống 1-2 lần/ngày tùy liều, cùng giờ mỗi ngày. KHÔNG ngừng đột ngột - phải giảm liều dần trong 1-2 tuần.",
            },
        },
        "references": {
            "primary_sources": [
                "FDA Drug Label - Lopressor HCT (metoprolol/HCTZ)",
                "ACC/AHA Hypertension Guidelines 2024",
            ],
            "last_updated": "2025-02-18",
            "evidence_level": "High – FDA-approved",
        },
        "risk_flags": {
            "high_alert": True,
            "narrow_therapeutic_index": False,
            "icu_critical_care_only": False,
            "bleeding_risk": "Low",
            "organ_toxicity": {"cardiovascular": "High (bradycardia, AV block)", "metabolic": "Moderate (hypokalemia, hyperglycemia)"}
        },
        "guideline_tags": [
            "AHA/ACC 2017 Hypertension Guidelines",
            "AHA/ACC 2024 Hypertension Management Update",
            "ESC/ESH 2023 Hypertension Guidelines"
        ],
    },

    "Bisoprolol/Hydrochlorothiazide": {
        "group": "Cardiovascular - Beta-blocker + Diuretic (Fixed-Dose Combination)",
        "vietnamese_name": "Bisoprolol/HCTZ, Ziac",
        "administration": ["PO"],
        "indications": [
            "Tăng huyết áp (khi cần phối hợp beta-blocker và diuretic).",
        ],
        "contraindications": [
            "Dị ứng với bisoprolol, hydrochlorothiazide, hoặc sulfonamide.",
            "Hen phế quản nặng, COPD nặng.",
            "Block nhĩ thất độ 2-3.",
            "Suy tim cấp.",
            "Nhịp tim chậm nặng (<50 bpm).",
            "Suy thận nặng (CrCl <30 ml/min).",
            "Hạ kali máu nặng.",
        ],
        "dosage": {
            "adult_initial": "Bisoprolol 2.5mg/HCTZ 6.25mg PO mỗi ngày.",
            "adult_maintenance": "Bisoprolol 5mg/HCTZ 6.25mg hoặc Bisoprolol 10mg/HCTZ 6.25mg PO mỗi ngày.",
            "notes": "Uống 1 lần/ngày, có thể uống với hoặc không thức ăn.",
        },
        "renal_adjustment": {
            "normal": "Không cần chỉnh liều.",
            "30_60": "Thận trọng, có thể cần giảm liều.",
            "under_30": "Không dùng nếu CrCl <30 ml/min.",
        },
        "side_effects": [
            "Mệt mỏi, lạnh tay chân (do beta-blocker).",
            "Nhịp tim chậm.",
            "Hạ kali máu (do HCTZ).",
            "Hạ huyết áp, chóng mặt.",
            "Tăng đường huyết, tăng acid uric máu (do HCTZ).",
            "Rối loạn cương dương (do beta-blocker).",
        ],
        "interactions": [
            "Verapamil, Diltiazem: tăng nguy cơ block AV, nhịp tim chậm.",
            "Insulin, thuốc hạ đường huyết: tăng nguy cơ hạ đường huyết, che dấu triệu chứng hạ đường huyết.",
            "Digoxin: tăng nguy cơ block AV.",
        ],
        "pregnancy": "D: chống chỉ định trong thai kỳ (beta-blocker có thể gây chậm phát triển thai nhi).",
        "mechanism_of_action": (
            "Bisoprolol là beta-1 selective blocker, ức chế thụ thể beta-1 ở tim, giảm nhịp tim và co bóp cơ tim, "
            "giảm cung lượng tim và giảm huyết áp. Hydrochlorothiazide là thiazide diuretic, "
            "ức chế tái hấp thu natri và nước ở ống lượn xa, dẫn đến lợi tiểu và giảm thể tích tuần hoàn. "
            "Phối hợp hai thuốc có tác dụng hiệp đồng giảm huyết áp."
        ),
        "monitoring": [
            "Huyết áp trước và trong điều trị.",
            "Nhịp tim - nhịp tim chậm phổ biến.",
            "Điện giải (Na+, K+) trước và trong điều trị - đặc biệt kali máu.",
            "Đường huyết - HCTZ có thể tăng đường huyết.",
            "Chức năng thận (creatinine, eGFR).",
        ],
        "precautions": [
            "CHỐNG CHỈ ĐỊNH trong hen phế quản nặng, COPD nặng - có thể gây co thắt phế quản.",
            "CHỐNG CHỈ ĐỊNH trong block AV độ 2-3 - có thể làm nặng block.",
            "CHỐNG CHỈ ĐỊNH trong suy tim cấp - có thể làm nặng suy tim.",
            "KHÔNG ngừng đột ngột - phải giảm liều dần trong 1-2 tuần (rebound hypertension, đau thắt ngực).",
            "Nguy cơ hạ kali máu - theo dõi kali máu, có thể cần bổ sung kali.",
            "Nguy cơ che dấu triệu chứng hạ đường huyết ở bệnh nhân đái tháo đường.",
            "Không dùng nếu CrCl <30 ml/min.",
        ],
        "pharmacokinetics": {
            "half_life": "Bisoprolol: ~9-12 giờ; HCTZ: ~6-15 giờ.",
            "onset": "Giảm huyết áp trong vài giờ đến vài ngày.",
            "duration": "24 giờ (dùng 1 lần/ngày).",
            "protein_binding": "Bisoprolol: ~30%; HCTZ: ~40%.",
            "clearance": "Bisoprolol: thải qua cả gan và thận (50-50%); HCTZ: thải qua thận.",
        },
        "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm, tránh ánh sáng.",
        "black_box_warnings": (
            "KHÔNG ngừng đột ngột: Có thể gây rebound hypertension, đau thắt ngực, nhồi máu cơ tim. "
            "Phải giảm liều dần trong 1-2 tuần. Chống chỉ định trong thai kỳ: Beta-blocker có thể gây chậm phát triển thai nhi."
        ),
        "drug_interactions": {
            "major": [
                {
                    "drug": "Verapamil, Diltiazem (CCB non-dihydropyridine)",
                    "mechanism": "Cả hai đều làm chậm dẫn truyền AV và giảm nhịp tim.",
                    "effect": "Tăng nguy cơ block AV độ 2-3, nhịp tim chậm nghiêm trọng, suy tim.",
                    "management": "Thận trọng. Theo dõi ECG, nhịp tim chặt chẽ. Tránh dùng cùng nếu có thể.",
                },
            ],
            "moderate": [
                {
                    "drug": "Digoxin",
                    "mechanism": "Cả hai đều làm chậm dẫn truyền AV.",
                    "effect": "Tăng nguy cơ block AV.",
                    "management": "Thận trọng. Theo dõi ECG, nhịp tim.",
                },
                {
                    "drug": "Insulin, thuốc hạ đường huyết",
                    "mechanism": "Beta-blocker che dấu triệu chứng hạ đường huyết (nhịp tim nhanh, run), HCTZ có thể tăng đường huyết.",
                    "effect": "Tăng nguy cơ hạ đường huyết không được phát hiện, hoặc tăng đường huyết.",
                    "management": "Thận trọng. Theo dõi đường huyết chặt chẽ. Theo dõi các triệu chứng hạ đường huyết khác (đổ mồ hôi, lú lẫn).",
                },
            ],
            "minor": [],
        },
        "contraindications_detail": {
            "tuyệt_đối": [
                "Dị ứng với bisoprolol, hydrochlorothiazide, hoặc sulfonamide.",
                "Hen phế quản nặng, COPD nặng.",
                "Block nhĩ thất độ 2-3.",
                "Suy tim cấp.",
                "Nhịp tim chậm nặng (<50 bpm).",
                "Suy thận nặng (CrCl <30 ml/min).",
                "Hạ kali máu nặng.",
            ],
            "tương_đối": [
                "Suy tim mạn tính - thận trọng, có thể dùng ở suy tim mạn tính được điều trị.",
                "Suy thận trung bình (CrCl 30-60) - thận trọng.",
                "Đái tháo đường - thận trọng, che dấu triệu chứng hạ đường huyết.",
                "Bệnh mạch vành - thận trọng, không ngừng đột ngột.",
            ],
        },
        "pregnancy_lactation": {
            "fda_category": "D",
            "pregnancy_details": (
                "Chống chỉ định trong thai kỳ. Beta-blocker có thể gây chậm phát triển thai nhi, "
                "nhịp tim chậm ở thai nhi, hạ đường huyết ở trẻ sơ sinh. Ngừng ngay khi phát hiện có thai."
            ),
            "lactation": {
                "safety": "Caution",
                "details": "Bisoprolol và HCTZ đều bài tiết vào sữa mẹ.",
                "recommendation": "Thận trọng khi cho con bú. Cân nhắc ngừng cho con bú hoặc ngừng thuốc.",
            },
        },
        "hepatic_adjustment": {
            "mild": "Không cần chỉnh liều.",
            "moderate": "Thận trọng, có thể cần giảm liều bisoprolol.",
            "severe": "Thận trọng, giảm liều bisoprolol.",
            "notes": "Bisoprolol thải qua cả gan và thận (50-50%); HCTZ không chuyển hóa đáng kể qua gan.",
        },
        "overdose_management": {
            "symptoms": [
                "Nhịp tim chậm nghiêm trọng, block AV.",
                "Hạ huyết áp nặng.",
                "Hạ kali máu.",
                "Suy tim cấp.",
            ],
            "antidote": "Atropine cho nhịp tim chậm, Glucagon cho beta-blocker overdose.",
            "treatment": [
                "Điều trị nhịp tim chậm: Atropine 0.5-1mg IV, nếu cần: pacemaker tạm thời.",
                "Điều trị hạ huyết áp: Truyền dịch, glucagon 1-5mg IV (cho beta-blocker overdose), nếu cần: dopamine, norepinephrine.",
                "Điều trị hạ kali máu: Bổ sung kali IV nếu cần.",
                "Theo dõi ECG liên tục.",
            ],
            "monitoring": "ECG, nhịp tim, huyết áp, điện giải, chức năng thận.",
        },
        "reversal_agents": {
            "available": True,
            "agents": ["Atropine (cho nhịp tim chậm)", "Glucagon (cho beta-blocker overdose)"]
        },
        "administration_instructions": {
            "oral": {
                "with_food": "Có thể uống với hoặc không thức ăn.",
                "timing": "Uống 1 lần/ngày, cùng giờ mỗi ngày. KHÔNG ngừng đột ngột - phải giảm liều dần trong 1-2 tuần.",
            },
        },
        "references": {
            "primary_sources": [
                "FDA Drug Label - Ziac (bisoprolol/HCTZ)",
                "ACC/AHA Hypertension Guidelines 2024",
            ],
            "last_updated": "2025-02-18",
            "evidence_level": "High – FDA-approved",
        },
        "risk_flags": {
            "high_alert": True,
            "narrow_therapeutic_index": False,
            "icu_critical_care_only": False,
            "bleeding_risk": "Low",
            "organ_toxicity": {"cardiovascular": "High (bradycardia, AV block)", "metabolic": "Moderate (hypokalemia, hyperglycemia)"}
        },
        "guideline_tags": [
            "AHA/ACC 2017 Hypertension Guidelines",
            "AHA/ACC 2024 Hypertension Management Update",
            "ESC/ESH 2023 Hypertension Guidelines"
        ],
    },

    "Metoprolol/Amlodipine": {
        "group": "Cardiovascular - Beta-blocker + CCB (Fixed-Dose Combination)",
        "vietnamese_name": "Metoprolol/Amlodipine",
        "administration": ["PO"],
        "indications": [
            "Tăng huyết áp (khi cần phối hợp beta-blocker và CCB).",
        ],
        "contraindications": [
            "Dị ứng với metoprolol, amlodipine, hoặc dihydropyridine.",
            "Hen phế quản nặng, COPD nặng.",
            "Block nhĩ thất độ 2-3.",
            "Suy tim cấp.",
            "Nhịp tim chậm nặng (<50 bpm).",
        ],
        "dosage": {
            "adult_initial": "Metoprolol 25mg/Amlodipine 5mg PO x 1-2 lần/ngày.",
            "adult_maintenance": "Metoprolol 50mg/Amlodipine 5mg x 1-2 lần/ngày hoặc Metoprolol 50mg/Amlodipine 10mg x 1-2 lần/ngày.",
            "notes": "Uống 1-2 lần/ngày tùy liều, có thể uống với hoặc không thức ăn.",
        },
        "renal_adjustment": {
            "normal": "Không cần chỉnh liều.",
            "30_60": "Thận trọng, có thể cần giảm liều.",
            "under_30": "Thận trọng, có thể cần giảm liều.",
        },
        "side_effects": [
            "Mệt mỏi, lạnh tay chân (do beta-blocker).",
            "Nhịp tim chậm.",
            "Phù chân (do amlodipine).",
            "Hạ huyết áp, chóng mặt.",
            "Rối loạn cương dương (do beta-blocker).",
        ],
        "interactions": [
            "Verapamil, Diltiazem: tăng nguy cơ block AV, nhịp tim chậm (không dùng với amlodipine nhưng cần lưu ý).",
            "Digoxin: tăng nguy cơ block AV.",
        ],
        "pregnancy": "D: chống chỉ định trong thai kỳ (beta-blocker có thể gây chậm phát triển thai nhi).",
        "mechanism_of_action": (
            "Metoprolol là beta-1 selective blocker, ức chế thụ thể beta-1 ở tim, giảm nhịp tim và co bóp cơ tim, "
            "giảm cung lượng tim và giảm huyết áp. Amlodipine là CCB dihydropyridine, ức chế kênh calci L-type, "
            "giãn mạch ngoại vi và giảm huyết áp. "
            "Phối hợp hai thuốc có tác dụng hiệp đồng giảm huyết áp. Beta-blocker đối kháng nhịp tim nhanh phản ứng của CCB."
        ),
        "monitoring": [
            "Huyết áp trước và trong điều trị.",
            "Nhịp tim - nhịp tim chậm phổ biến.",
            "Dấu hiệu phù chân.",
            "ECG - theo dõi block AV nếu có triệu chứng.",
        ],
        "precautions": [
            "CHỐNG CHỈ ĐỊNH trong hen phế quản nặng, COPD nặng - có thể gây co thắt phế quản.",
            "CHỐNG CHỈ ĐỊNH trong block AV độ 2-3 - có thể làm nặng block.",
            "CHỐNG CHỈ ĐỊNH trong suy tim cấp - có thể làm nặng suy tim.",
            "KHÔNG ngừng đột ngột - phải giảm liều dần trong 1-2 tuần (rebound hypertension, đau thắt ngực).",
            "Nguy cơ phù chân (do amlodipine).",
        ],
        "pharmacokinetics": {
            "half_life": "Metoprolol: ~3-7 giờ (immediate release), ~24 giờ (extended release); Amlodipine: ~30-50 giờ.",
            "onset": "Giảm huyết áp trong vài giờ đến vài ngày.",
            "duration": "12-24 giờ tùy dạng metoprolol.",
            "protein_binding": "Metoprolol: ~12%; Amlodipine: ~98%.",
            "clearance": "Metoprolol: chuyển hóa ở gan; Amlodipine: chuyển hóa ở gan.",
        },
        "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm, tránh ánh sáng.",
        "black_box_warnings": (
            "KHÔNG ngừng đột ngột: Có thể gây rebound hypertension, đau thắt ngực, nhồi máu cơ tim. "
            "Phải giảm liều dần trong 1-2 tuần. Chống chỉ định trong thai kỳ: Beta-blocker có thể gây chậm phát triển thai nhi."
        ),
        "drug_interactions": {
            "major": [
                {
                    "drug": "Verapamil, Diltiazem (CCB non-dihydropyridine)",
                    "mechanism": "Cả hai đều làm chậm dẫn truyền AV và giảm nhịp tim.",
                    "effect": "Tăng nguy cơ block AV độ 2-3, nhịp tim chậm nghiêm trọng, suy tim.",
                    "management": "Thận trọng. Theo dõi ECG, nhịp tim chặt chẽ. Tránh dùng cùng nếu có thể.",
                },
            ],
            "moderate": [
                {
                    "drug": "Digoxin",
                    "mechanism": "Cả hai đều làm chậm dẫn truyền AV.",
                    "effect": "Tăng nguy cơ block AV.",
                    "management": "Thận trọng. Theo dõi ECG, nhịp tim.",
                },
            ],
            "minor": [],
        },
        "contraindications_detail": {
            "tuyệt_đối": [
                "Dị ứng với metoprolol, amlodipine, hoặc dihydropyridine.",
                "Hen phế quản nặng, COPD nặng.",
                "Block nhĩ thất độ 2-3.",
                "Suy tim cấp.",
                "Nhịp tim chậm nặng (<50 bpm).",
            ],
            "tương_đối": [
                "Suy tim mạn tính - thận trọng, có thể dùng ở suy tim mạn tính được điều trị.",
                "Bệnh mạch vành - thận trọng, không ngừng đột ngột.",
            ],
        },
        "pregnancy_lactation": {
            "fda_category": "D",
            "pregnancy_details": (
                "Chống chỉ định trong thai kỳ. Beta-blocker có thể gây chậm phát triển thai nhi, "
                "nhịp tim chậm ở thai nhi, hạ đường huyết ở trẻ sơ sinh. Ngừng ngay khi phát hiện có thai."
            ),
            "lactation": {
                "safety": "Caution",
                "details": "Metoprolol và amlodipine đều bài tiết vào sữa mẹ.",
                "recommendation": "Thận trọng khi cho con bú. Cân nhắc ngừng cho con bú hoặc ngừng thuốc.",
            },
        },
        "hepatic_adjustment": {
            "mild": "Không cần chỉnh liều.",
            "moderate": "Thận trọng, có thể cần giảm liều metoprolol.",
            "severe": "Thận trọng, giảm liều metoprolol.",
            "notes": "Metoprolol và amlodipine đều chuyển hóa ở gan.",
        },
        "overdose_management": {
            "symptoms": [
                "Nhịp tim chậm nghiêm trọng, block AV.",
                "Hạ huyết áp nặng.",
                "Phù chân nặng.",
                "Suy tim cấp.",
            ],
            "antidote": "Atropine cho nhịp tim chậm, Glucagon cho beta-blocker overdose.",
            "treatment": [
                "Điều trị nhịp tim chậm: Atropine 0.5-1mg IV, nếu cần: pacemaker tạm thời.",
                "Điều trị hạ huyết áp: Truyền dịch, glucagon 1-5mg IV (cho beta-blocker overdose), nếu cần: dopamine, norepinephrine.",
                "Theo dõi ECG liên tục.",
            ],
            "monitoring": "ECG, nhịp tim, huyết áp, dấu hiệu sinh tồn.",
        },
        "reversal_agents": {
            "available": True,
            "agents": ["Atropine (cho nhịp tim chậm)", "Glucagon (cho beta-blocker overdose)"]
        },
        "administration_instructions": {
            "oral": {
                "with_food": "Có thể uống với hoặc không thức ăn.",
                "timing": "Uống 1-2 lần/ngày tùy liều, cùng giờ mỗi ngày. KHÔNG ngừng đột ngột - phải giảm liều dần trong 1-2 tuần.",
            },
        },
        "references": {
            "primary_sources": [
                "FDA Drug Label - Metoprolol/Amlodipine",
                "ACC/AHA Hypertension Guidelines 2024",
            ],
            "last_updated": "2025-02-18",
            "evidence_level": "High – FDA-approved",
        },
        "risk_flags": {
            "high_alert": True,
            "narrow_therapeutic_index": False,
            "icu_critical_care_only": False,
            "bleeding_risk": "Low",
            "organ_toxicity": {"cardiovascular": "High (bradycardia, AV block)"}
        },
        "guideline_tags": [
            "AHA/ACC 2017 Hypertension Guidelines",
            "AHA/ACC 2024 Hypertension Management Update",
            "ESC/ESH 2023 Hypertension Guidelines"
        ],
    },

    "Amlodipine/Indapamide": {
        "group": "Cardiovascular - CCB + Diuretic (Fixed-Dose Combination)",
        "vietnamese_name": "Amlodipine/Indapamide",
        "administration": ["PO"],
        "indications": [
            "Tăng huyết áp (khi cần phối hợp CCB và diuretic).",
        ],
        "contraindications": [
            "Dị ứng với amlodipine, indapamide, hoặc dihydropyridine.",
            "Suy thận nặng (CrCl <30 ml/min).",
            "Hạ kali máu nặng.",
        ],
        "dosage": {
            "adult_initial": "Amlodipine 5mg/Indapamide 1.25mg PO mỗi ngày.",
            "adult_maintenance": "Amlodipine 5mg/Indapamide 2.5mg hoặc Amlodipine 10mg/Indapamide 2.5mg PO mỗi ngày.",
            "notes": "Uống 1 lần/ngày, có thể uống với hoặc không thức ăn.",
        },
        "renal_adjustment": {
            "normal": "Không cần chỉnh liều.",
            "30_60": "Thận trọng, cân nhắc giảm liều hoặc dùng đơn trị.",
            "under_30": "Không dùng nếu CrCl <30 ml/min.",
        },
        "side_effects": [
            "Phù chân (do amlodipine).",
            "Hạ kali máu (do indapamide).",
            "Chóng mặt, hạ huyết áp.",
            "Tăng đường huyết, tăng acid uric máu (do indapamide).",
            "Đau đầu.",
        ],
        "interactions": [
            "Kali-sparing diuretics: tăng nguy cơ tăng kali máu (ít hơn với indapamide so với HCTZ).",
        ],
        "pregnancy": "C: thận trọng trong thai kỳ.",
        "mechanism_of_action": (
            "Amlodipine là CCB dihydropyridine, ức chế kênh calci L-type, giãn mạch ngoại vi và giảm huyết áp. "
            "Indapamide là thiazide-like diuretic, ức chế tái hấp thu natri và nước ở ống lượn xa, "
            "dẫn đến lợi tiểu và giảm thể tích tuần hoàn. "
            "Phối hợp hai thuốc có tác dụng hiệp đồng giảm huyết áp."
        ),
        "monitoring": [
            "Huyết áp trước và trong điều trị.",
            "Điện giải (Na+, K+) trước và trong điều trị - đặc biệt kali máu.",
            "Dấu hiệu phù chân.",
            "Chức năng thận (creatinine, eGFR).",
        ],
        "precautions": [
            "Nguy cơ phù chân (do amlodipine).",
            "Nguy cơ hạ kali máu - theo dõi kali máu, có thể cần bổ sung kali.",
            "Không dùng nếu CrCl <30 ml/min.",
            "Thận trọng ở bệnh nhân đái tháo đường - indapamide có thể tăng đường huyết.",
        ],
        "pharmacokinetics": {
            "half_life": "Amlodipine: ~30-50 giờ; Indapamide: ~14-18 giờ.",
            "onset": "Giảm huyết áp trong vài giờ đến vài ngày.",
            "duration": "24 giờ (dùng 1 lần/ngày).",
            "protein_binding": "Amlodipine: ~98%; Indapamide: ~71-79%.",
            "clearance": "Amlodipine: chuyển hóa ở gan; Indapamide: thải qua thận.",
        },
        "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm, tránh ánh sáng.",
        "black_box_warnings": "Không có black box warning.",
        "drug_interactions": {
            "major": [],
            "moderate": [],
            "minor": [],
        },
        "contraindications_detail": {
            "tuyệt_đối": [
                "Dị ứng với amlodipine, indapamide, hoặc dihydropyridine.",
                "Suy thận nặng (CrCl <30 ml/min).",
                "Hạ kali máu nặng.",
            ],
            "tương_đối": [
                "Suy thận trung bình (CrCl 30-60) - thận trọng.",
            ],
        },
        "pregnancy_lactation": {
            "fda_category": "C",
            "pregnancy_details": "Category C. Thận trọng trong thai kỳ. Có thể dùng nếu lợi ích > nguy cơ.",
            "lactation": {
                "safety": "Caution",
                "details": "Amlodipine và indapamide đều bài tiết vào sữa mẹ.",
                "recommendation": "Thận trọng khi cho con bú.",
            },
        },
        "hepatic_adjustment": {
            "mild": "Không cần chỉnh liều.",
            "moderate": "Thận trọng.",
            "severe": "Thận trọng, có thể cần giảm liều.",
            "notes": "Amlodipine chuyển hóa ở gan; indapamide thải qua thận.",
        },
        "overdose_management": {
            "symptoms": ["Hạ huyết áp nặng.", "Hạ kali máu.", "Phù chân nặng."],
            "antidote": "Không có antidote đặc hiệu.",
            "treatment": [
                "Điều trị hạ huyết áp: bù dịch, norepinephrine nếu cần.",
                "Điều trị hạ kali máu: bổ sung kali IV nếu cần.",
            ],
            "monitoring": "Huyết áp, điện giải, chức năng thận.",
        },
        "reversal_agents": None,
        "administration_instructions": {
            "oral": {
                "with_food": "Có thể uống với hoặc không thức ăn.",
                "timing": "Uống 1 lần/ngày, cùng giờ mỗi ngày.",
            },
        },
        "references": {
            "primary_sources": [
                "FDA Drug Label - Amlodipine/Indapamide",
                "ACC/AHA Hypertension Guidelines 2024",
            ],
            "last_updated": "2025-02-18",
            "evidence_level": "High – FDA-approved",
        },
        "risk_flags": {
            "high_alert": False,
            "narrow_therapeutic_index": False,
            "icu_critical_care_only": False,
            "bleeding_risk": "Low",
            "organ_toxicity": {"metabolic": "Moderate (hypokalemia)"}
        },
        "guideline_tags": [
            "AHA/ACC 2017 Hypertension Guidelines",
            "AHA/ACC 2024 Hypertension Management Update",
            "ESC/ESH 2023 Hypertension Guidelines"
        ],
    },

    "Perindopril/Indapamide": {
        "group": "Cardiovascular - ACE Inhibitor + Diuretic (Fixed-Dose Combination)",
        "vietnamese_name": "Perindopril/Indapamide, Coversyl Plus",
        "administration": ["PO"],
        "indications": [
            "Tăng huyết áp (khi cần phối hợp ACE inhibitor và diuretic).",
        ],
        "contraindications": [
            "Dị ứng với perindopril, indapamide, hoặc sulfonamide.",
            "Có thai (ACE inhibitor chống chỉ định trong thai kỳ).",
            "Hẹp động mạch thận hai bên.",
            "Suy thận nặng (CrCl <30 ml/min).",
            "Hạ kali máu nặng.",
        ],
        "dosage": {
            "adult_initial": "Perindopril 4mg/Indapamide 1.25mg PO mỗi ngày.",
            "adult_maintenance": "Perindopril 8mg/Indapamide 1.25mg hoặc Perindopril 8mg/Indapamide 2.5mg PO mỗi ngày.",
            "notes": "Uống 1 lần/ngày, có thể uống với hoặc không thức ăn.",
        },
        "renal_adjustment": {
            "normal": "Không cần chỉnh liều.",
            "30_60": "Thận trọng, cân nhắc giảm liều hoặc dùng đơn trị.",
            "under_30": "Không dùng nếu CrCl <30 ml/min.",
        },
        "side_effects": [
            "Ho khan (do ACE inhibitor).",
            "Hạ huyết áp, chóng mặt.",
            "Hạ kali máu (do indapamide).",
            "Tăng creatinin máu, suy thận cấp.",
            "Phù mạch (hiếm nhưng nghiêm trọng).",
            "Tăng đường huyết, tăng acid uric máu (do indapamide).",
        ],
        "interactions": [
            "NSAIDs: tăng nguy cơ suy thận cấp.",
            "Kali-sparing diuretics, kali bổ sung: tăng nguy cơ tăng kali máu.",
            "Lithium: tăng nồng độ lithium.",
        ],
        "pregnancy": "D: chống chỉ định trong thai kỳ (ACE inhibitor).",
        "mechanism_of_action": (
            "Perindopril là ACE inhibitor, ức chế enzyme chuyển đổi angiotensin (ACE), "
            "giảm sản xuất angiotensin II, dẫn đến giãn mạch và giảm huyết áp. "
            "Indapamide là thiazide-like diuretic, ức chế tái hấp thu natri và nước ở ống lượn xa, "
            "dẫn đến lợi tiểu và giảm thể tích tuần hoàn. "
            "Phối hợp hai thuốc có tác dụng hiệp đồng giảm huyết áp mạnh hơn từng thuốc đơn trị."
        ),
        "monitoring": [
            "Huyết áp trước và trong điều trị.",
            "Creatinine, eGFR (CrCl) trước và trong điều trị - QUAN TRỌNG.",
            "Điện giải (Na+, K+) trước và trong điều trị - đặc biệt kali máu.",
            "Dấu hiệu hạ huyết áp, chóng mặt.",
            "Dấu hiệu phù mạch (sưng mặt, môi, lưỡi, họng) - nguy hiểm.",
        ],
        "precautions": [
            "QUAN TRỌNG: Chống chỉ định trong thai kỳ - ACE inhibitor có thể gây dị tật thai nhi.",
            "Nguy cơ suy thận cấp - theo dõi creatinine chặt chẽ, đặc biệt khi bắt đầu hoặc tăng liều.",
            "Nguy cơ hạ kali máu - theo dõi kali máu, có thể cần bổ sung kali.",
            "Nguy cơ phù mạch - ngừng ngay nếu có triệu chứng, điều trị bằng epinephrine.",
            "Không dùng nếu CrCl <30 ml/min.",
            "Thận trọng ở bệnh nhân suy tim, bệnh mạch vành.",
        ],
        "pharmacokinetics": {
            "half_life": "Perindopril: ~17 giờ; Perindoprilat: ~17 giờ; Indapamide: ~14-18 giờ.",
            "onset": "Giảm huyết áp trong vài giờ đến vài ngày.",
            "duration": "24 giờ (dùng 1 lần/ngày).",
            "protein_binding": "Perindopril: ~60%; Indapamide: ~71-79%.",
            "clearance": "Perindopril: thải qua thận; Indapamide: thải qua thận.",
        },
        "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm, tránh ánh sáng.",
        "black_box_warnings": (
            "Chống chỉ định trong thai kỳ: ACE inhibitor có thể gây dị tật thai nhi và tử vong thai nhi. "
            "Ngừng ngay khi phát hiện có thai. Phù mạch: có thể xảy ra và đe dọa tính mạng."
        ),
        "drug_interactions": {
            "major": [
                {
                    "drug": "NSAIDs (ibuprofen, naproxen, diclofenac)",
                    "mechanism": "NSAIDs giảm tác dụng giãn mạch của ACE inhibitor và giảm lưu lượng máu thận.",
                    "effect": "Tăng nguy cơ suy thận cấp, giảm hiệu quả hạ huyết áp.",
                    "management": "Thận trọng. Theo dõi chức năng thận chặt chẽ. Có thể cần giảm liều hoặc tránh NSAIDs.",
                },
                {
                    "drug": "Kali-sparing diuretics (spironolactone, eplerenone), Kali bổ sung",
                    "mechanism": "ACE inhibitor giảm bài tiết kali, indapamide tăng bài tiết kali, nhưng tổng thể có thể tăng kali máu.",
                    "effect": "Tăng nguy cơ tăng kali máu, rối loạn nhịp tim.",
                    "management": "Thận trọng. Theo dõi kali máu chặt chẽ. Thường không nên dùng cùng kali-sparing diuretics.",
                },
            ],
            "moderate": [
                {
                    "drug": "Lithium",
                    "mechanism": "ACE inhibitor và indapamide đều có thể tăng nồng độ lithium.",
                    "effect": "Tăng nguy cơ độc tính lithium.",
                    "management": "Thận trọng. Theo dõi nồng độ lithium chặt chẽ. Có thể cần giảm liều lithium.",
                },
            ],
            "minor": [],
        },
        "contraindications_detail": {
            "tuyệt_đối": [
                "Dị ứng với perindopril, indapamide, hoặc sulfonamide.",
                "Có thai hoặc có thể mang thai.",
                "Hẹp động mạch thận hai bên.",
                "Suy thận nặng (CrCl <30 ml/min).",
                "Hạ kali máu nặng.",
            ],
            "tương_đối": [
                "Suy thận trung bình (CrCl 30-60) - thận trọng.",
                "Suy tim nặng - thận trọng.",
                "Bệnh mạch vành - thận trọng.",
                "Tiền sử phù mạch - tránh dùng.",
            ],
        },
        "pregnancy_lactation": {
            "fda_category": "D",
            "pregnancy_details": (
                "Chống chỉ định trong thai kỳ. ACE inhibitor có thể gây dị tật thai nhi, "
                "suy thận thai nhi, giảm nước ối, và tử vong thai nhi. Ngừng ngay khi phát hiện có thai."
            ),
            "lactation": {
                "safety": "Caution",
                "details": "Perindopril và indapamide đều bài tiết vào sữa mẹ.",
                "recommendation": "Thận trọng khi cho con bú. Cân nhắc ngừng cho con bú hoặc ngừng thuốc.",
            },
        },
        "hepatic_adjustment": {
            "mild": "Không cần chỉnh liều.",
            "moderate": "Thận trọng.",
            "severe": "Thận trọng, có thể cần giảm liều.",
            "notes": "Perindopril thải qua thận; indapamide thải qua thận.",
        },
        "overdose_management": {
            "symptoms": [
                "Hạ huyết áp nặng, sốc.",
                "Hạ kali máu, hạ natri máu.",
                "Suy thận cấp.",
            ],
            "antidote": "Không có antidote đặc hiệu.",
            "treatment": [
                "Điều trị hạ huyết áp: bù dịch, norepinephrine nếu cần.",
                "Điều trị hạ kali máu: bổ sung kali IV nếu cần.",
                "Điều trị suy thận cấp: bù dịch, theo dõi chức năng thận.",
            ],
            "monitoring": "Huyết áp, điện giải, chức năng thận, dấu hiệu sinh tồn.",
        },
        "reversal_agents": None,
        "administration_instructions": {
            "oral": {
                "with_food": "Có thể uống với hoặc không thức ăn.",
                "timing": "Uống 1 lần/ngày, cùng giờ mỗi ngày.",
            },
        },
        "references": {
            "primary_sources": [
                "FDA Drug Label - Coversyl Plus (perindopril/indapamide)",
                "ACC/AHA Hypertension Guidelines 2024",
            ],
            "last_updated": "2025-02-18",
            "evidence_level": "High – FDA-approved",
        },
        "risk_flags": {
            "high_alert": True,
            "narrow_therapeutic_index": False,
            "icu_critical_care_only": False,
            "bleeding_risk": "Low",
            "organ_toxicity": {"renal": "Moderate", "pregnancy": "High (teratogenic)", "metabolic": "Moderate (hypokalemia)"}
        },
        "guideline_tags": [
            "AHA/ACC 2017 Hypertension Guidelines",
            "AHA/ACC 2024 Hypertension Management Update",
            "ESC/ESH 2023 Hypertension Guidelines"
        ],
    },

    "Benazepril/Amlodipine": {
        "group": "Cardiovascular - ACE Inhibitor + CCB (Fixed-Dose Combination)",
        "vietnamese_name": "Benazepril/Amlodipine, Lotrel",
        "administration": ["PO"],
        "indications": [
            "Tăng huyết áp (khi cần phối hợp ACE inhibitor và CCB).",
        ],
        "contraindications": [
            "Dị ứng với benazepril, amlodipine, hoặc dihydropyridine.",
            "Có thai (ACE inhibitor chống chỉ định trong thai kỳ).",
            "Hẹp động mạch thận hai bên.",
        ],
        "dosage": {
            "adult_initial": "Benazepril 10mg/Amlodipine 2.5mg PO mỗi ngày.",
            "adult_maintenance": "Benazepril 10mg/Amlodipine 5mg hoặc Benazepril 20mg/Amlodipine 5mg hoặc Benazepril 20mg/Amlodipine 10mg PO mỗi ngày.",
            "notes": "Uống 1 lần/ngày, có thể uống với hoặc không thức ăn.",
        },
        "renal_adjustment": {
            "normal": "Không cần chỉnh liều.",
            "30_60": "Thận trọng, có thể cần giảm liều benazepril.",
            "under_30": "Thận trọng, giảm liều benazepril.",
        },
        "side_effects": [
            "Ho khan (do ACE inhibitor).",
            "Phù chân (do amlodipine).",
            "Chóng mặt, hạ huyết áp.",
            "Đau đầu.",
            "Tăng creatinin máu.",
            "Phù mạch (hiếm nhưng nghiêm trọng).",
        ],
        "interactions": [
            "NSAIDs: tăng nguy cơ suy thận cấp.",
            "Kali-sparing diuretics, kali bổ sung: tăng nguy cơ tăng kali máu.",
        ],
        "pregnancy": "D: chống chỉ định trong thai kỳ (ACE inhibitor).",
        "mechanism_of_action": (
            "Benazepril là ACE inhibitor, ức chế enzyme chuyển đổi angiotensin (ACE), "
            "giảm sản xuất angiotensin II, dẫn đến giãn mạch và giảm huyết áp. "
            "Amlodipine là CCB dihydropyridine, ức chế kênh calci L-type, giãn mạch ngoại vi. "
            "Phối hợp hai thuốc có tác dụng hiệp đồng giảm huyết áp và giảm phù chân (ACE inhibitor đối kháng tác dụng phụ của CCB)."
        ),
        "monitoring": [
            "Huyết áp trước và trong điều trị.",
            "Creatinine, eGFR trước và trong điều trị.",
            "Dấu hiệu phù chân.",
            "Dấu hiệu phù mạch (sưng mặt, môi, lưỡi, họng) - nguy hiểm.",
        ],
        "precautions": [
            "Chống chỉ định trong thai kỳ - ACE inhibitor có thể gây dị tật thai nhi.",
            "Nguy cơ phù chân (do amlodipine) - có thể giảm khi phối hợp với ACE inhibitor.",
            "Nguy cơ suy thận cấp - theo dõi creatinine chặt chẽ.",
            "Nguy cơ phù mạch - ngừng ngay nếu có triệu chứng.",
        ],
        "pharmacokinetics": {
            "half_life": "Benazepril: ~10-11 giờ; Benazeprilat: ~10-11 giờ; Amlodipine: ~30-50 giờ.",
            "onset": "Giảm huyết áp trong vài giờ đến vài ngày.",
            "duration": "24 giờ (dùng 1 lần/ngày).",
            "protein_binding": "Benazepril: ~97%; Amlodipine: ~98%.",
            "clearance": "Benazepril: thải qua cả gan và thận; Amlodipine: chuyển hóa ở gan.",
        },
        "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm, tránh ánh sáng.",
        "black_box_warnings": (
            "Chống chỉ định trong thai kỳ: ACE inhibitor có thể gây dị tật thai nhi và tử vong thai nhi. "
            "Ngừng ngay khi phát hiện có thai. Phù mạch: có thể xảy ra và đe dọa tính mạng."
        ),
        "drug_interactions": {
            "major": [
                {
                    "drug": "NSAIDs",
                    "mechanism": "Tăng nguy cơ suy thận cấp.",
                    "effect": "Suy thận cấp, giảm hiệu quả hạ huyết áp.",
                    "management": "Thận trọng. Theo dõi chức năng thận.",
                },
            ],
            "moderate": [],
            "minor": [],
        },
        "contraindications_detail": {
            "tuyệt_đối": [
                "Dị ứng với benazepril, amlodipine, hoặc dihydropyridine.",
                "Có thai hoặc có thể mang thai.",
                "Hẹp động mạch thận hai bên.",
            ],
            "tương_đối": [
                "Suy thận nặng (CrCl <30) - thận trọng.",
            ],
        },
        "pregnancy_lactation": {
            "fda_category": "D",
            "pregnancy_details": "Chống chỉ định trong thai kỳ. ACE inhibitor có thể gây dị tật thai nhi.",
            "lactation": {
                "safety": "Caution",
                "details": "Benazepril và amlodipine đều bài tiết vào sữa mẹ.",
                "recommendation": "Thận trọng khi cho con bú.",
            },
        },
        "hepatic_adjustment": {
            "mild": "Không cần chỉnh liều.",
            "moderate": "Thận trọng.",
            "severe": "Thận trọng, có thể cần giảm liều.",
            "notes": "Benazepril thải qua cả gan và thận; amlodipine chuyển hóa ở gan.",
        },
        "overdose_management": {
            "symptoms": ["Hạ huyết áp nặng.", "Phù chân nặng."],
            "antidote": "Không có antidote đặc hiệu.",
            "treatment": ["Điều trị hạ huyết áp: bù dịch, norepinephrine nếu cần."],
            "monitoring": "Huyết áp, dấu hiệu sinh tồn.",
        },
        "reversal_agents": None,
        "administration_instructions": {
            "oral": {
                "with_food": "Có thể uống với hoặc không thức ăn.",
                "timing": "Uống 1 lần/ngày, cùng giờ mỗi ngày.",
            },
        },
        "references": {
            "primary_sources": ["FDA Drug Label - Lotrel (benazepril/amlodipine)", "ACC/AHA Guidelines 2024"],
            "last_updated": "2025-02-18",
            "evidence_level": "High – FDA-approved",
        },
        "risk_flags": {
            "high_alert": True,
            "narrow_therapeutic_index": False,
            "icu_critical_care_only": False,
            "bleeding_risk": "Low",
            "organ_toxicity": {"renal": "Moderate", "pregnancy": "High (teratogenic)"}
        },
        "guideline_tags": [
            "AHA/ACC 2017 Hypertension Guidelines",
            "AHA/ACC 2024 Hypertension Management Update",
            "ESC/ESH 2023 Hypertension Guidelines"
        ],
    },

    "Olmesartan/Amlodipine/Hydrochlorothiazide": {
        "group": "Cardiovascular - ARB + CCB + Diuretic (Fixed-Dose Triple Combination)",
        "vietnamese_name": "Olmesartan/Amlodipine/HCTZ, Tribenzor",
        "administration": ["PO"],
        "indications": [
            "Tăng huyết áp (khi cần phối hợp ARB, CCB và diuretic - không kiểm soát được với phối hợp 2 thuốc).",
        ],
        "contraindications": [
            "Dị ứng với olmesartan, amlodipine, hydrochlorothiazide, hoặc dihydropyridine.",
            "Có thai (ARB chống chỉ định trong thai kỳ).",
            "Suy thận nặng (CrCl <30 ml/min).",
            "Hạ kali máu nặng.",
        ],
        "dosage": {
            "adult_initial": "Olmesartan 20mg/Amlodipine 5mg/HCTZ 12.5mg PO mỗi ngày.",
            "adult_maintenance": "Olmesartan 40mg/Amlodipine 5mg/HCTZ 12.5mg hoặc Olmesartan 40mg/Amlodipine 10mg/HCTZ 25mg PO mỗi ngày.",
            "notes": "Uống 1 lần/ngày, có thể uống với hoặc không thức ăn. Chỉ dùng khi không kiểm soát được với phối hợp 2 thuốc.",
        },
        "renal_adjustment": {
            "normal": "Không cần chỉnh liều.",
            "30_60": "Thận trọng, cân nhắc giảm liều.",
            "under_30": "Không dùng nếu CrCl <30 ml/min.",
        },
        "side_effects": [
            "Phù chân (do amlodipine).",
            "Chóng mặt, hạ huyết áp.",
            "Hạ kali máu (do HCTZ).",
            "Tăng creatinin máu.",
            "Tăng đường huyết, tăng acid uric máu (do HCTZ).",
            "Đau đầu.",
        ],
        "interactions": [
            "NSAIDs: tăng nguy cơ suy thận cấp.",
            "Kali-sparing diuretics: tăng nguy cơ tăng kali máu.",
        ],
        "pregnancy": "D: chống chỉ định trong thai kỳ (ARB).",
        "mechanism_of_action": (
            "Olmesartan là ARB, ức chế thụ thể AT1 của angiotensin II, giãn mạch. "
            "Amlodipine là CCB dihydropyridine, ức chế kênh calci L-type, giãn mạch ngoại vi. "
            "Hydrochlorothiazide là thiazide diuretic, ức chế tái hấp thu natri và nước ở ống lượn xa. "
            "Phối hợp ba thuốc có tác dụng hiệp đồng giảm huyết áp mạnh, dùng khi không kiểm soát được với phối hợp 2 thuốc."
        ),
        "monitoring": [
            "Huyết áp trước và trong điều trị.",
            "Creatinine, eGFR trước và trong điều trị.",
            "Điện giải (Na+, K+) trước và trong điều trị.",
            "Dấu hiệu phù chân.",
        ],
        "precautions": [
            "Chống chỉ định trong thai kỳ - ARB có thể gây dị tật thai nhi.",
            "Chỉ dùng khi không kiểm soát được với phối hợp 2 thuốc.",
            "Nguy cơ suy thận cấp - theo dõi creatinine chặt chẽ.",
            "Nguy cơ hạ kali máu - theo dõi kali máu.",
            "Nguy cơ phù chân (do amlodipine).",
            "Không dùng nếu CrCl <30 ml/min.",
        ],
        "pharmacokinetics": {
            "half_life": "Olmesartan: ~13 giờ; Amlodipine: ~30-50 giờ; HCTZ: ~6-15 giờ.",
            "onset": "Giảm huyết áp trong vài giờ đến vài ngày.",
            "duration": "24 giờ (dùng 1 lần/ngày).",
            "protein_binding": "Olmesartan: ~99%; Amlodipine: ~98%; HCTZ: ~40%.",
            "clearance": "Olmesartan: không chuyển hóa, thải qua phân và nước tiểu; Amlodipine: chuyển hóa ở gan; HCTZ: thải qua thận.",
        },
        "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm, tránh ánh sáng.",
        "black_box_warnings": (
            "Chống chỉ định trong thai kỳ: ARB có thể gây dị tật thai nhi và tử vong thai nhi. "
            "Ngừng ngay khi phát hiện có thai."
        ),
        "drug_interactions": {
            "major": [
                {
                    "drug": "NSAIDs",
                    "mechanism": "Tăng nguy cơ suy thận cấp.",
                    "effect": "Suy thận cấp, giảm hiệu quả hạ huyết áp.",
                    "management": "Thận trọng. Theo dõi chức năng thận.",
                },
            ],
            "moderate": [],
            "minor": [],
        },
        "contraindications_detail": {
            "tuyệt_đối": [
                "Dị ứng với olmesartan, amlodipine, HCTZ, hoặc dihydropyridine.",
                "Có thai hoặc có thể mang thai.",
                "Suy thận nặng (CrCl <30 ml/min).",
                "Hạ kali máu nặng.",
            ],
            "tương_đối": [
                "Suy thận trung bình (CrCl 30-60) - thận trọng.",
            ],
        },
        "pregnancy_lactation": {
            "fda_category": "D",
            "pregnancy_details": "Chống chỉ định trong thai kỳ. ARB có thể gây dị tật thai nhi.",
            "lactation": {
                "safety": "Caution",
                "details": "Olmesartan, amlodipine và HCTZ đều bài tiết vào sữa mẹ.",
                "recommendation": "Thận trọng khi cho con bú.",
            },
        },
        "hepatic_adjustment": {
            "mild": "Không cần chỉnh liều.",
            "moderate": "Thận trọng.",
            "severe": "Thận trọng, có thể cần giảm liều.",
            "notes": "Olmesartan không chuyển hóa qua gan; amlodipine chuyển hóa ở gan; HCTZ không chuyển hóa đáng kể qua gan.",
        },
        "overdose_management": {
            "symptoms": ["Hạ huyết áp nặng.", "Hạ kali máu.", "Phù chân nặng."],
            "antidote": "Không có antidote đặc hiệu.",
            "treatment": ["Điều trị hạ huyết áp: bù dịch.", "Điều trị hạ kali máu: bổ sung kali IV nếu cần."],
            "monitoring": "Huyết áp, điện giải, chức năng thận.",
        },
        "reversal_agents": None,
        "administration_instructions": {
            "oral": {
                "with_food": "Có thể uống với hoặc không thức ăn.",
                "timing": "Uống 1 lần/ngày, cùng giờ mỗi ngày.",
            },
        },
        "references": {
            "primary_sources": ["FDA Drug Label - Tribenzor (olmesartan/amlodipine/HCTZ)", "ACC/AHA Guidelines 2024"],
            "last_updated": "2025-02-18",
            "evidence_level": "High – FDA-approved",
        },
        "risk_flags": {
            "high_alert": True,
            "narrow_therapeutic_index": False,
            "icu_critical_care_only": False,
            "bleeding_risk": "Low",
            "organ_toxicity": {"renal": "Moderate", "pregnancy": "High (teratogenic)", "metabolic": "Moderate (hypokalemia)"}
        },
        "guideline_tags": [
            "AHA/ACC 2017 Hypertension Guidelines",
            "AHA/ACC 2024 Hypertension Management Update",
            "ESC/ESH 2023 Hypertension Guidelines"
        ],
    },

    "Valsartan/Amlodipine/Hydrochlorothiazide": {
        "group": "Cardiovascular - ARB + CCB + Diuretic (Fixed-Dose Triple Combination)",
        "vietnamese_name": "Valsartan/Amlodipine/HCTZ, Exforge HCT",
        "administration": ["PO"],
        "indications": [
            "Tăng huyết áp (khi cần phối hợp ARB, CCB và diuretic - không kiểm soát được với phối hợp 2 thuốc).",
        ],
        "contraindications": [
            "Dị ứng với valsartan, amlodipine, hydrochlorothiazide, hoặc dihydropyridine.",
            "Có thai (ARB chống chỉ định trong thai kỳ).",
            "Suy thận nặng (CrCl <30 ml/min).",
            "Hạ kali máu nặng.",
        ],
        "dosage": {
            "adult_initial": "Valsartan 160mg/Amlodipine 5mg/HCTZ 12.5mg PO mỗi ngày.",
            "adult_maintenance": "Valsartan 160mg/Amlodipine 10mg/HCTZ 12.5mg hoặc Valsartan 320mg/Amlodipine 10mg/HCTZ 25mg PO mỗi ngày.",
            "notes": "Uống 1 lần/ngày, có thể uống với hoặc không thức ăn. Chỉ dùng khi không kiểm soát được với phối hợp 2 thuốc.",
        },
        "renal_adjustment": {
            "normal": "Không cần chỉnh liều.",
            "30_60": "Thận trọng, cân nhắc giảm liều.",
            "under_30": "Không dùng nếu CrCl <30 ml/min.",
        },
        "side_effects": [
            "Phù chân (do amlodipine).",
            "Chóng mặt, hạ huyết áp.",
            "Hạ kali máu (do HCTZ).",
            "Tăng creatinin máu.",
            "Tăng đường huyết, tăng acid uric máu (do HCTZ).",
            "Đau đầu.",
        ],
        "interactions": [
            "NSAIDs: tăng nguy cơ suy thận cấp.",
            "Kali-sparing diuretics: tăng nguy cơ tăng kali máu.",
        ],
        "pregnancy": "D: chống chỉ định trong thai kỳ (ARB).",
        "mechanism_of_action": (
            "Valsartan là ARB, ức chế thụ thể AT1 của angiotensin II, giãn mạch. "
            "Amlodipine là CCB dihydropyridine, ức chế kênh calci L-type, giãn mạch ngoại vi. "
            "Hydrochlorothiazide là thiazide diuretic, ức chế tái hấp thu natri và nước ở ống lượn xa. "
            "Phối hợp ba thuốc có tác dụng hiệp đồng giảm huyết áp mạnh, dùng khi không kiểm soát được với phối hợp 2 thuốc."
        ),
        "monitoring": [
            "Huyết áp trước và trong điều trị.",
            "Creatinine, eGFR trước và trong điều trị.",
            "Điện giải (Na+, K+) trước và trong điều trị.",
            "Dấu hiệu phù chân.",
        ],
        "precautions": [
            "Chống chỉ định trong thai kỳ - ARB có thể gây dị tật thai nhi.",
            "Chỉ dùng khi không kiểm soát được với phối hợp 2 thuốc.",
            "Nguy cơ suy thận cấp - theo dõi creatinine chặt chẽ.",
            "Nguy cơ hạ kali máu - theo dõi kali máu.",
            "Nguy cơ phù chân (do amlodipine).",
            "Không dùng nếu CrCl <30 ml/min.",
        ],
        "pharmacokinetics": {
            "half_life": "Valsartan: ~6 giờ; Amlodipine: ~30-50 giờ; HCTZ: ~6-15 giờ.",
            "onset": "Giảm huyết áp trong vài giờ đến vài ngày.",
            "duration": "24 giờ (dùng 1 lần/ngày).",
            "protein_binding": "Valsartan: ~95%; Amlodipine: ~98%; HCTZ: ~40%.",
            "clearance": "Valsartan: chủ yếu thải qua phân; Amlodipine: chuyển hóa ở gan; HCTZ: thải qua thận.",
        },
        "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm, tránh ánh sáng.",
        "black_box_warnings": (
            "Chống chỉ định trong thai kỳ: ARB có thể gây dị tật thai nhi và tử vong thai nhi. "
            "Ngừng ngay khi phát hiện có thai."
        ),
        "drug_interactions": {
            "major": [
                {
                    "drug": "NSAIDs",
                    "mechanism": "Tăng nguy cơ suy thận cấp.",
                    "effect": "Suy thận cấp, giảm hiệu quả hạ huyết áp.",
                    "management": "Thận trọng. Theo dõi chức năng thận.",
                },
            ],
            "moderate": [],
            "minor": [],
        },
        "contraindications_detail": {
            "tuyệt_đối": [
                "Dị ứng với valsartan, amlodipine, HCTZ, hoặc dihydropyridine.",
                "Có thai hoặc có thể mang thai.",
                "Suy thận nặng (CrCl <30 ml/min).",
                "Hạ kali máu nặng.",
            ],
            "tương_đối": [
                "Suy thận trung bình (CrCl 30-60) - thận trọng.",
            ],
        },
        "pregnancy_lactation": {
            "fda_category": "D",
            "pregnancy_details": "Chống chỉ định trong thai kỳ. ARB có thể gây dị tật thai nhi.",
            "lactation": {
                "safety": "Caution",
                "details": "Valsartan, amlodipine và HCTZ đều bài tiết vào sữa mẹ.",
                "recommendation": "Thận trọng khi cho con bú.",
            },
        },
        "hepatic_adjustment": {
            "mild": "Không cần chỉnh liều.",
            "moderate": "Thận trọng.",
            "severe": "Thận trọng, có thể cần giảm liều.",
            "notes": "Valsartan chuyển hóa một phần qua gan; amlodipine chuyển hóa ở gan; HCTZ không chuyển hóa đáng kể qua gan.",
        },
        "overdose_management": {
            "symptoms": ["Hạ huyết áp nặng.", "Hạ kali máu.", "Phù chân nặng."],
            "antidote": "Không có antidote đặc hiệu.",
            "treatment": ["Điều trị hạ huyết áp: bù dịch.", "Điều trị hạ kali máu: bổ sung kali IV nếu cần."],
            "monitoring": "Huyết áp, điện giải, chức năng thận.",
        },
        "reversal_agents": None,
        "administration_instructions": {
            "oral": {
                "with_food": "Có thể uống với hoặc không thức ăn.",
                "timing": "Uống 1 lần/ngày, cùng giờ mỗi ngày.",
            },
        },
        "references": {
            "primary_sources": ["FDA Drug Label - Exforge HCT (valsartan/amlodipine/HCTZ)", "ACC/AHA Guidelines 2024"],
            "last_updated": "2025-02-18",
            "evidence_level": "High – FDA-approved",
        },
        "risk_flags": {
            "high_alert": True,
            "narrow_therapeutic_index": False,
            "icu_critical_care_only": False,
            "bleeding_risk": "Low",
            "organ_toxicity": {"renal": "Moderate", "pregnancy": "High (teratogenic)", "metabolic": "Moderate (hypokalemia)"}
        },
        "guideline_tags": [
            "AHA/ACC 2017 Hypertension Guidelines",
            "AHA/ACC 2024 Hypertension Management Update",
            "ESC/ESH 2023 Hypertension Guidelines"
        ],
    },

    "Perindopril/Amlodipine/Indapamide": {
        "group": "Cardiovascular - ACE Inhibitor + CCB + Diuretic (Fixed-Dose Triple Combination)",
        "vietnamese_name": "Perindopril/Amlodipine/Indapamide, Coveram Plus",
        "administration": ["PO"],
        "indications": [
            "Tăng huyết áp (khi cần phối hợp ACE inhibitor, CCB và diuretic - không kiểm soát được với phối hợp 2 thuốc).",
        ],
        "contraindications": [
            "Dị ứng với perindopril, amlodipine, indapamide, hoặc dihydropyridine.",
            "Có thai (ACE inhibitor chống chỉ định trong thai kỳ).",
            "Hẹp động mạch thận hai bên.",
            "Suy thận nặng (CrCl <30 ml/min).",
            "Hạ kali máu nặng.",
        ],
        "dosage": {
            "adult_initial": "Perindopril 4mg/Amlodipine 5mg/Indapamide 1.25mg PO mỗi ngày.",
            "adult_maintenance": "Perindopril 8mg/Amlodipine 5mg/Indapamide 1.25mg hoặc Perindopril 8mg/Amlodipine 10mg/Indapamide 2.5mg PO mỗi ngày.",
            "notes": "Uống 1 lần/ngày, có thể uống với hoặc không thức ăn. Chỉ dùng khi không kiểm soát được với phối hợp 2 thuốc.",
        },
        "renal_adjustment": {
            "normal": "Không cần chỉnh liều.",
            "30_60": "Thận trọng, cân nhắc giảm liều hoặc dùng đơn trị.",
            "under_30": "Không dùng nếu CrCl <30 ml/min.",
        },
        "side_effects": [
            "Ho khan (do ACE inhibitor).",
            "Phù chân (do amlodipine).",
            "Chóng mặt, hạ huyết áp.",
            "Hạ kali máu (do indapamide).",
            "Tăng creatinin máu, suy thận cấp.",
            "Phù mạch (hiếm nhưng nghiêm trọng).",
            "Tăng đường huyết, tăng acid uric máu (do indapamide).",
        ],
        "interactions": [
            "NSAIDs: tăng nguy cơ suy thận cấp.",
            "Kali-sparing diuretics, kali bổ sung: tăng nguy cơ tăng kali máu.",
            "Lithium: tăng nồng độ lithium.",
        ],
        "pregnancy": "D: chống chỉ định trong thai kỳ (ACE inhibitor).",
        "mechanism_of_action": (
            "Perindopril là ACE inhibitor, ức chế enzyme chuyển đổi angiotensin (ACE), "
            "giảm sản xuất angiotensin II, dẫn đến giãn mạch và giảm huyết áp. "
            "Amlodipine là CCB dihydropyridine, ức chế kênh calci L-type, giãn mạch ngoại vi. "
            "Indapamide là thiazide-like diuretic, ức chế tái hấp thu natri và nước ở ống lượn xa. "
            "Phối hợp ba thuốc có tác dụng hiệp đồng giảm huyết áp mạnh, dùng khi không kiểm soát được với phối hợp 2 thuốc."
        ),
        "monitoring": [
            "Huyết áp trước và trong điều trị.",
            "Creatinine, eGFR (CrCl) trước và trong điều trị - QUAN TRỌNG.",
            "Điện giải (Na+, K+) trước và trong điều trị - đặc biệt kali máu.",
            "Dấu hiệu phù chân.",
            "Dấu hiệu phù mạch (sưng mặt, môi, lưỡi, họng) - nguy hiểm.",
        ],
        "precautions": [
            "QUAN TRỌNG: Chống chỉ định trong thai kỳ - ACE inhibitor có thể gây dị tật thai nhi.",
            "Chỉ dùng khi không kiểm soát được với phối hợp 2 thuốc.",
            "Nguy cơ suy thận cấp - theo dõi creatinine chặt chẽ, đặc biệt khi bắt đầu hoặc tăng liều.",
            "Nguy cơ hạ kali máu - theo dõi kali máu, có thể cần bổ sung kali.",
            "Nguy cơ phù mạch - ngừng ngay nếu có triệu chứng, điều trị bằng epinephrine.",
            "Nguy cơ phù chân (do amlodipine).",
            "Không dùng nếu CrCl <30 ml/min.",
        ],
        "pharmacokinetics": {
            "half_life": "Perindopril: ~17 giờ; Perindoprilat: ~17 giờ; Amlodipine: ~30-50 giờ; Indapamide: ~14-18 giờ.",
            "onset": "Giảm huyết áp trong vài giờ đến vài ngày.",
            "duration": "24 giờ (dùng 1 lần/ngày).",
            "protein_binding": "Perindopril: ~60%; Amlodipine: ~98%; Indapamide: ~71-79%.",
            "clearance": "Perindopril: thải qua thận; Amlodipine: chuyển hóa ở gan; Indapamide: thải qua thận.",
        },
        "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm, tránh ánh sáng.",
        "black_box_warnings": (
            "Chống chỉ định trong thai kỳ: ACE inhibitor có thể gây dị tật thai nhi và tử vong thai nhi. "
            "Ngừng ngay khi phát hiện có thai. Phù mạch: có thể xảy ra và đe dọa tính mạng."
        ),
        "drug_interactions": {
            "major": [
                {
                    "drug": "NSAIDs (ibuprofen, naproxen, diclofenac)",
                    "mechanism": "NSAIDs giảm tác dụng giãn mạch của ACE inhibitor và giảm lưu lượng máu thận.",
                    "effect": "Tăng nguy cơ suy thận cấp, giảm hiệu quả hạ huyết áp.",
                    "management": "Thận trọng. Theo dõi chức năng thận chặt chẽ. Có thể cần giảm liều hoặc tránh NSAIDs.",
                },
                {
                    "drug": "Kali-sparing diuretics (spironolactone, eplerenone), Kali bổ sung",
                    "mechanism": "ACE inhibitor giảm bài tiết kali, indapamide tăng bài tiết kali, nhưng tổng thể có thể tăng kali máu.",
                    "effect": "Tăng nguy cơ tăng kali máu, rối loạn nhịp tim.",
                    "management": "Thận trọng. Theo dõi kali máu chặt chẽ. Thường không nên dùng cùng kali-sparing diuretics.",
                },
            ],
            "moderate": [
                {
                    "drug": "Lithium",
                    "mechanism": "ACE inhibitor và indapamide đều có thể tăng nồng độ lithium.",
                    "effect": "Tăng nguy cơ độc tính lithium.",
                    "management": "Thận trọng. Theo dõi nồng độ lithium chặt chẽ. Có thể cần giảm liều lithium.",
                },
            ],
            "minor": [],
        },
        "contraindications_detail": {
            "tuyệt_đối": [
                "Dị ứng với perindopril, amlodipine, indapamide, hoặc dihydropyridine.",
                "Có thai hoặc có thể mang thai.",
                "Hẹp động mạch thận hai bên.",
                "Suy thận nặng (CrCl <30 ml/min).",
                "Hạ kali máu nặng.",
            ],
            "tương_đối": [
                "Suy thận trung bình (CrCl 30-60) - thận trọng.",
                "Suy tim nặng - thận trọng.",
                "Bệnh mạch vành - thận trọng.",
                "Tiền sử phù mạch - tránh dùng.",
            ],
        },
        "pregnancy_lactation": {
            "fda_category": "D",
            "pregnancy_details": (
                "Chống chỉ định trong thai kỳ. ACE inhibitor có thể gây dị tật thai nhi, "
                "suy thận thai nhi, giảm nước ối, và tử vong thai nhi. Ngừng ngay khi phát hiện có thai."
            ),
            "lactation": {
                "safety": "Caution",
                "details": "Perindopril, amlodipine và indapamide đều bài tiết vào sữa mẹ.",
                "recommendation": "Thận trọng khi cho con bú. Cân nhắc ngừng cho con bú hoặc ngừng thuốc.",
            },
        },
        "hepatic_adjustment": {
            "mild": "Không cần chỉnh liều.",
            "moderate": "Thận trọng.",
            "severe": "Thận trọng, có thể cần giảm liều.",
            "notes": "Perindopril thải qua thận; amlodipine chuyển hóa ở gan; indapamide thải qua thận.",
        },
        "overdose_management": {
            "symptoms": [
                "Hạ huyết áp nặng, sốc.",
                "Hạ kali máu, hạ natri máu.",
                "Suy thận cấp.",
                "Phù chân nặng.",
            ],
            "antidote": "Không có antidote đặc hiệu.",
            "treatment": [
                "Điều trị hạ huyết áp: bù dịch, norepinephrine nếu cần.",
                "Điều trị hạ kali máu: bổ sung kali IV nếu cần.",
                "Điều trị suy thận cấp: bù dịch, theo dõi chức năng thận.",
            ],
            "monitoring": "Huyết áp, điện giải, chức năng thận, dấu hiệu sinh tồn.",
        },
        "reversal_agents": None,
        "administration_instructions": {
            "oral": {
                "with_food": "Có thể uống với hoặc không thức ăn.",
                "timing": "Uống 1 lần/ngày, cùng giờ mỗi ngày.",
            },
        },
        "references": {
            "primary_sources": [
                "FDA Drug Label - Coveram Plus (perindopril/amlodipine/indapamide)",
                "ACC/AHA Hypertension Guidelines 2024",
            ],
            "last_updated": "2025-02-18",
            "evidence_level": "High – FDA-approved",
        },
        "risk_flags": {
            "high_alert": True,
            "narrow_therapeutic_index": False,
            "icu_critical_care_only": False,
            "bleeding_risk": "Low",
            "organ_toxicity": {"renal": "Moderate", "pregnancy": "High (teratogenic)", "metabolic": "Moderate (hypokalemia)"}
        },
        "guideline_tags": [
            "AHA/ACC 2017 Hypertension Guidelines",
            "AHA/ACC 2024 Hypertension Management Update",
            "ESC/ESH 2023 Hypertension Guidelines"
        ],
    },

    "Amlodipine/Atorvastatin": {
        "group": "Cardiovascular - CCB + Statin (Fixed-Dose Combination)",
        "vietnamese_name": "Amlodipine/Atorvastatin, Caduet",
        "administration": ["PO"],
        "indications": [
            "Tăng huyết áp và tăng cholesterol máu (khi cần phối hợp CCB và statin).",
            "Phòng ngừa biến cố tim mạch ở bệnh nhân có cả tăng huyết áp và rối loạn lipid máu.",
        ],
        "contraindications": [
            "Dị ứng với amlodipine, atorvastatin, hoặc dihydropyridine.",
            "Bệnh gan hoạt động (active liver disease) - chống chỉ định cho statin.",
            "Có thai hoặc có thể mang thai (statin chống chỉ định trong thai kỳ - FDA category X).",
            "Cho con bú.",
            "Tiêu cơ vân đang hoạt động (active myopathy/rhabdomyolysis).",
        ],
        "dosage": {
            "adult_initial": "Amlodipine 5mg/Atorvastatin 10mg PO mỗi ngày.",
            "adult_maintenance": "Các liều có sẵn: Amlodipine 5mg/Atorvastatin 10mg, 5mg/20mg, 5mg/40mg, 5mg/80mg, 10mg/10mg, 10mg/20mg, 10mg/40mg, 10mg/80mg PO mỗi ngày.",
            "notes": "Uống 1 lần/ngày, có thể uống với hoặc không thức ăn. Điều chỉnh liều dựa trên đáp ứng huyết áp và lipid profile. Atorvastatin có thể uống bất kỳ lúc nào trong ngày.",
        },
        "renal_adjustment": {
            "normal": "Không cần chỉnh liều.",
            "30_60": "Không cần chỉnh liều cho cả hai thành phần.",
            "under_30": "Thận trọng, có thể cần giảm liều atorvastatin.",
        },
        "side_effects": [
            "Phù chân (do amlodipine).",
            "Đau cơ, viêm cơ (do atorvastatin) - phổ biến (~5%).",
            "Tan rã cơ (Rhabdomyolysis) - hiếm nhưng nguy hiểm (do atorvastatin).",
            "Tăng men gan (ALT, AST) - do atorvastatin.",
            "Chóng mặt, hạ huyết áp (do amlodipine).",
            "Đau đầu.",
            "Đái tháo đường mới khởi phát (tăng đường huyết nhẹ) - do atorvastatin.",
            "Rối loạn tiêu hóa.",
        ],
        "interactions": [
            "Grapefruit juice: Tăng nồng độ atorvastatin (tránh uống).",
            "Fibrate (Gemfibrozil): Tăng nguy cơ tan rã cơ (tránh dùng chung).",
            "Azole antifungals, Macrolide: Tăng nồng độ atorvastatin.",
            "Warfarin: Tăng INR (do atorvastatin).",
            "Cyclosporine: Tăng nồng độ atorvastatin, giới hạn liều atorvastatin 10mg/ngày.",
        ],
        "pregnancy": "X: chống chỉ định trong thai kỳ (statin gây quái thai).",
        "mechanism_of_action": (
            "Amlodipine là CCB dihydropyridine, ức chế kênh calci L-type, giãn mạch ngoại vi và giảm huyết áp. "
            "Atorvastatin là statin (HMG-CoA reductase inhibitor), ức chế enzyme tổng hợp cholesterol ở gan, "
            "giảm LDL cholesterol (30-50%), tăng HDL cholesterol (5-10%), và ổn định mảng xơ vữa. "
            "Phối hợp hai thuốc điều trị đồng thời tăng huyết áp và rối loạn lipid máu, phòng ngừa biến cố tim mạch."
        ),
        "monitoring": [
            "Huyết áp trước và trong điều trị.",
            "Lipid profile (LDL, HDL, Triglyceride) - Sau 4-12 tuần điều trị, sau đó định kỳ.",
            "Men gan (ALT, AST) - Trước điều trị, sau đó nếu có triệu chứng hoặc định kỳ.",
            "CK (Creatine Kinase) - Nếu có đau cơ hoặc triệu chứng nghi ngờ tiêu cơ vân.",
            "Đường huyết - Định kỳ ở bệnh nhân có nguy cơ đái tháo đường.",
            "Dấu hiệu phù chân.",
        ],
        "precautions": [
            "QUAN TRỌNG: Chống chỉ định trong thai kỳ - Statin gây quái thai (FDA category X). Ngừng ngay khi phát hiện có thai.",
            "CHỐNG CHỈ ĐỊNH trong bệnh gan hoạt động - Statin có thể làm nặng bệnh gan.",
            "Ngừng thuốc nếu đau cơ nặng hoặc CK >10x bình thường (nghi ngờ tan rã cơ).",
            "Nguy cơ phù chân (do amlodipine).",
            "Nguy cơ tăng đường huyết nhẹ (do atorvastatin) - theo dõi đường huyết.",
            "Tránh grapefruit juice - tăng nồng độ atorvastatin.",
            "Thận trọng khi dùng chung với Fibrate - tăng nguy cơ tiêu cơ vân.",
        ],
        "pharmacokinetics": {
            "half_life": "Amlodipine: ~30-50 giờ; Atorvastatin: ~14 giờ (hoạt tính kéo dài 20-30 giờ do chất chuyển hóa).",
            "onset": "Giảm huyết áp trong vài giờ đến vài ngày (amlodipine); Giảm cholesterol trong vài tuần (atorvastatin).",
            "duration": "24 giờ (dùng 1 lần/ngày).",
            "protein_binding": "Amlodipine: ~98%; Atorvastatin: >98%.",
            "clearance": "Amlodipine: chuyển hóa ở gan; Atorvastatin: chuyển hóa mạnh qua gan bởi CYP3A4, thải chủ yếu qua mật và phân.",
        },
        "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm, tránh ánh sáng.",
        "black_box_warnings": (
            "Chống chỉ định trong thai kỳ: Statin gây quái thai và có thể gây dị tật thai nhi. "
            "Ngừng ngay khi phát hiện có thai. Chống chỉ định trong bệnh gan hoạt động. "
            "Rhabdomyolysis: Có thể gây tiêu cơ vân dẫn đến suy thận cấp."
        ),
        "drug_interactions": {
            "major": [
                {
                    "drug": "Gemfibrozil (Fibrate)",
                    "mechanism": "Hiệp đồng độc cơ, tăng nguy cơ tiêu cơ vân.",
                    "effect": "Tăng nguy cơ tiêu cơ vân nghiêm trọng, suy thận cấp.",
                    "management": "Tránh dùng chung. Nếu cần hạ triglyceride, cân nhắc fenofibrate với liều thấp và theo dõi chặt chẽ.",
                },
                {
                    "drug": "Cyclosporine",
                    "mechanism": "Ức chế CYP3A4 và OATP1B1, tăng nồng độ atorvastatin.",
                    "effect": "Tăng nguy cơ tiêu cơ vân.",
                    "management": "Giới hạn liều atorvastatin 10mg/ngày hoặc tránh dùng.",
                },
                {
                    "drug": "Azole antifungals (Ketoconazole, Itraconazole), Macrolide (Clarithromycin, Erythromycin)",
                    "mechanism": "Ức chế CYP3A4, tăng nồng độ atorvastatin.",
                    "effect": "Tăng nguy cơ tiêu cơ vân.",
                    "management": "Thận trọng. Giảm liều atorvastatin hoặc tránh dùng nếu có thể.",
                },
            ],
            "moderate": [
                {
                    "drug": "Warfarin",
                    "mechanism": "Atorvastatin có thể tăng tác dụng của warfarin.",
                    "effect": "Tăng INR, tăng nguy cơ chảy máu.",
                    "management": "Theo dõi INR chặt chẽ khi bắt đầu hoặc thay đổi liều atorvastatin.",
                },
                {
                    "drug": "Grapefruit juice",
                    "mechanism": "Ức chế CYP3A4, tăng nồng độ atorvastatin.",
                    "effect": "Tăng nguy cơ tác dụng phụ của atorvastatin.",
                    "management": "Tránh uống grapefruit juice hoặc giảm lượng uống.",
                },
            ],
            "minor": [],
        },
        "contraindications_detail": {
            "tuyệt_đối": [
                "Dị ứng với amlodipine, atorvastatin, hoặc dihydropyridine.",
                "Bệnh gan hoạt động (active liver disease) - tăng men gan kéo dài, viêm gan.",
                "Có thai hoặc có thể mang thai - Statin gây quái thai (FDA category X).",
                "Cho con bú - Statin bài tiết vào sữa mẹ.",
                "Tiêu cơ vân đang hoạt động (active myopathy/rhabdomyolysis).",
            ],
            "tương_đối": [
                "Suy gan - thận trọng, theo dõi men gan thường xuyên.",
                "Suy thận nặng (CrCl <30) - thận trọng, có thể cần giảm liều atorvastatin.",
                "Người cao tuổi - tăng nguy cơ đau cơ, tiêu cơ vân.",
                "Đái tháo đường - statins có thể tăng đường huyết nhẹ.",
                "Bệnh tuyến giáp - tăng nguy cơ đau cơ.",
                "Uống rượu nhiều - tăng nguy cơ viêm gan.",
            ],
        },
        "pregnancy_lactation": {
            "fda_category": "X",
            "pregnancy_details": (
                "CHỐNG CHỈ ĐỊNH trong thai kỳ. Statin can thiệp vào tổng hợp cholesterol cần thiết cho sự phát triển của thai nhi, "
                "có thể gây dị tật thai nhi. Ngưng thuốc ngay lập tức nếu phát hiện có thai."
            ),
            "lactation": {
                "safety": "Avoid",
                "details": "Atorvastatin có khả năng bài tiết vào sữa mẹ và gây ảnh hưởng đến chuyển hóa lipid của trẻ.",
                "recommendation": "Không sử dụng. Ngưng cho con bú hoặc ngưng thuốc.",
            },
        },
        "hepatic_adjustment": {
            "mild": "Không cần chỉnh liều.",
            "moderate": "Thận trọng, giảm liều atorvastatin.",
            "severe": "CHỐNG CHỈ ĐỊNH (bệnh gan hoạt động).",
            "notes": "Amlodipine chuyển hóa ở gan; Atorvastatin chuyển hóa mạnh qua gan bởi CYP3A4. Chống chỉ định trong bệnh gan hoạt động.",
        },
        "overdose_management": {
            "symptoms": [
                "Hạ huyết áp nặng (do amlodipine).",
                "Phù chân nặng (do amlodipine).",
                "Đau cơ nặng, tiêu cơ vân (do atorvastatin).",
                "Suy thận cấp (do tiêu cơ vân).",
            ],
            "antidote": "Không có antidote đặc hiệu.",
            "treatment": [
                "Điều trị hạ huyết áp: Bù dịch, norepinephrine nếu cần.",
                "Điều trị tiêu cơ vân: Truyền dịch tích cực, điều chỉnh điện giải, theo dõi chức năng thận.",
                "Theo dõi CK, creatinine, men gan.",
            ],
            "monitoring": "Huyết áp, CK, creatinine, men gan (ALT, AST), điện giải, dấu hiệu sinh tồn.",
        },
        "reversal_agents": None,
        "administration_instructions": {
            "oral": {
                "with_food": "Có thể uống với hoặc không thức ăn.",
                "timing": "Uống 1 lần/ngày, cùng giờ mỗi ngày. Atorvastatin có thể uống bất kỳ lúc nào trong ngày.",
            },
        },
        "references": {
            "primary_sources": [
                "FDA Drug Label - Caduet (amlodipine/atorvastatin)",
                "ACC/AHA Hypertension Guidelines 2024",
                "ACC/AHA 2018 Cholesterol Guidelines",
            ],
            "last_updated": "2025-02-18",
            "evidence_level": "High – FDA-approved",
        },
        "risk_flags": {
            "high_alert": True,
            "narrow_therapeutic_index": False,
            "icu_critical_care_only": False,
            "bleeding_risk": "Low",
            "organ_toxicity": {"hepatic": "High", "musculoskeletal": "High (rhabdomyolysis)", "pregnancy": "High (teratogenic)"}
        },
        "guideline_tags": [
            "AHA/ACC 2017 Hypertension Guidelines",
            "AHA/ACC 2024 Hypertension Management Update",
            "ESC/ESH 2023 Hypertension Guidelines",
            "ACC/AHA 2018 Cholesterol Guidelines",
            "ESC/EAS Guidelines for Dyslipidaemias 2019"
        ],
    },

    "Simvastatin/Ezetimibe": {
        "group": "Cardiovascular - Statin + Cholesterol Absorption Inhibitor (Fixed-Dose Combination)",
        "vietnamese_name": "Simvastatin/Ezetimibe, Vytorin",
        "administration": ["PO"],
        "indications": [
            "Tăng cholesterol máu (khi cần phối hợp statin và ezetimibe để giảm LDL-C hiệu quả hơn).",
            "Tăng cholesterol máu gia đình (familial hypercholesterolemia).",
            "Phòng ngừa biến cố tim mạch ở bệnh nhân có nguy cơ cao (sau ACS, CKD).",
        ],
        "contraindications": [
            "Dị ứng với simvastatin, ezetimibe, hoặc bất kỳ thành phần nào.",
            "Bệnh gan hoạt động (active liver disease).",
            "Có thai hoặc có thể mang thai (statin chống chỉ định trong thai kỳ - FDA category X).",
            "Cho con bú.",
            "Tiêu cơ vân đang hoạt động (active myopathy/rhabdomyolysis).",
            "Dùng cùng cyclosporine, itraconazole, ketoconazole, hoặc grapefruit juice.",
        ],
        "dosage": {
            "adult_initial": "Simvastatin 10mg/Ezetimibe 10mg PO mỗi ngày.",
            "adult_maintenance": "Simvastatin 20mg/Ezetimibe 10mg, Simvastatin 40mg/Ezetimibe 10mg, hoặc Simvastatin 80mg/Ezetimibe 10mg PO mỗi ngày.",
            "notes": "Uống 1 lần/ngày vào buổi tối, có thể uống với hoặc không thức ăn. Liều simvastatin 80mg không khuyến cáo trừ khi bệnh nhân đã ổn định với liều này trên 12 tháng mà không có bệnh cơ.",
        },
        "renal_adjustment": {
            "normal": "Không cần chỉnh liều.",
            "30_60": "Không cần chỉnh liều.",
            "under_30": "Thận trọng, có thể cần giảm liều simvastatin.",
        },
        "side_effects": [
            "Đau cơ, viêm cơ (do simvastatin) - phổ biến (~5%).",
            "Tan rã cơ (Rhabdomyolysis) - hiếm nhưng nguy hiểm (do simvastatin, đặc biệt liều 80mg).",
            "Tăng men gan (ALT, AST) - do simvastatin.",
            "Rối loạn tiêu hóa (tiêu chảy, đau bụng) - do ezetimibe, nhẹ.",
            "Đau khớp, mệt mỏi.",
            "Đái tháo đường mới khởi phát (tăng đường huyết nhẹ) - do simvastatin.",
        ],
        "interactions": [
            "Grapefruit juice: Tăng nồng độ simvastatin (tránh uống).",
            "Cyclosporine: Tăng nồng độ simvastatin, chống chỉ định dùng chung.",
            "Azole antifungals (Ketoconazole, Itraconazole): Tăng nồng độ simvastatin, chống chỉ định dùng chung.",
            "Macrolide (Clarithromycin, Erythromycin): Tăng nồng độ simvastatin, chống chỉ định dùng chung.",
            "Amiodarone: Giới hạn Simvastatin ≤20mg/ngày.",
            "Diltiazem, Verapamil: Giới hạn Simvastatin ≤10mg/ngày.",
            "Fibrate (Gemfibrozil): Tăng nguy cơ tan rã cơ (tránh dùng chung).",
            "Cholestyramine: Giảm hấp thu ezetimibe - dùng cách xa ít nhất 2 giờ.",
        ],
        "pregnancy": "X: chống chỉ định trong thai kỳ (statin gây quái thai).",
        "mechanism_of_action": (
            "Simvastatin là statin (HMG-CoA reductase inhibitor), ức chế enzyme tổng hợp cholesterol ở gan, "
            "giảm LDL cholesterol (30-50%), tăng HDL cholesterol (5-10%). "
            "Ezetimibe là chất ức chế hấp thu cholesterol, ức chế protein NPC1L1 ở ruột non, "
            "giảm hấp thu cholesterol từ thức ăn và từ mật, giảm thêm LDL cholesterol (15-20%). "
            "Phối hợp hai thuốc có tác dụng cộng dồn, giảm LDL-C hiệu quả hơn từng thuốc đơn trị (~50-60% giảm LDL-C)."
        ),
        "monitoring": [
            "Lipid profile (LDL, HDL, Triglyceride, Total cholesterol) - Sau 4-12 tuần điều trị, sau đó định kỳ.",
            "Men gan (ALT, AST) - Trước điều trị, sau đó nếu có triệu chứng hoặc định kỳ.",
            "CK (Creatine Kinase) - Nếu có đau cơ hoặc triệu chứng nghi ngờ tiêu cơ vân.",
            "Đường huyết - Định kỳ ở bệnh nhân có nguy cơ đái tháo đường.",
            "Dấu hiệu rối loạn tiêu hóa (tiêu chảy, đau bụng) - nhẹ.",
        ],
        "precautions": [
            "QUAN TRỌNG: Chống chỉ định trong thai kỳ - Statin gây quái thai (FDA category X). Ngừng ngay khi phát hiện có thai.",
            "CHỐNG CHỈ ĐỊNH trong bệnh gan hoạt động - Statin có thể làm nặng bệnh gan.",
            "CHỐNG CHỈ ĐỊNH dùng cùng cyclosporine, azole antifungals, macrolide, hoặc grapefruit juice.",
            "Ngừng thuốc nếu đau cơ nặng hoặc CK >10x bình thường (nghi ngờ tan rã cơ).",
            "Liều simvastatin 80mg KHÔNG khuyến cáo trừ khi bệnh nhân đã ổn định với liều này trên 12 tháng mà không có bệnh cơ.",
            "Giảm LDL-C hiệu quả hơn từng thuốc đơn trị (~50-60% giảm LDL-C).",
            "Tránh grapefruit juice - tăng nồng độ simvastatin.",
            "Dùng cách xa cholestyramine ít nhất 2 giờ (giảm hấp thu ezetimibe).",
            "Thận trọng khi dùng với fibrate - tăng nguy cơ tiêu cơ vân.",
        ],
        "pharmacokinetics": {
            "half_life": "Simvastatin: ~3 giờ; Ezetimibe: ~22 giờ (ezetimibe), ~24 giờ (ezetimibe-glucuronide).",
            "onset": "Giảm cholesterol trong vài tuần.",
            "duration": "24 giờ (dùng 1 lần/ngày).",
            "protein_binding": "Simvastatin: ~95%; Ezetimibe: >90%.",
            "clearance": "Simvastatin: chuyển hóa mạnh qua gan bởi CYP3A4, thải chủ yếu qua phân và nước tiểu; Ezetimibe: chuyển hóa ở ruột và gan thành ezetimibe-glucuronide, thải chủ yếu qua phân.",
        },
        "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm, tránh ánh sáng.",
        "black_box_warnings": (
            "Chống chỉ định trong thai kỳ: Statin gây quái thai và có thể gây dị tật thai nhi. "
            "Ngừng ngay khi phát hiện có thai. Chống chỉ định trong bệnh gan hoạt động. "
            "Rhabdomyolysis: Có thể gây tiêu cơ vân dẫn đến suy thận cấp. "
            "Simvastatin 80mg: Không khuyến cáo trừ khi bệnh nhân đã ổn định với liều này trên 12 tháng mà không có bệnh cơ."
        ),
        "drug_interactions": {
            "major": [
                {
                    "drug": "Cyclosporine",
                    "mechanism": "Ức chế CYP3A4 và OATP1B1, tăng nồng độ simvastatin.",
                    "effect": "Tăng nguy cơ tiêu cơ vân nghiêm trọng.",
                    "management": "CHỐNG CHỈ ĐỊNH dùng chung.",
                },
                {
                    "drug": "Azole antifungals (Ketoconazole, Itraconazole)",
                    "mechanism": "Ức chế CYP3A4, tăng nồng độ simvastatin.",
                    "effect": "Tăng nguy cơ tiêu cơ vân nghiêm trọng.",
                    "management": "CHỐNG CHỈ ĐỊNH dùng chung.",
                },
                {
                    "drug": "Macrolide (Clarithromycin, Erythromycin)",
                    "mechanism": "Ức chế CYP3A4, tăng nồng độ simvastatin.",
                    "effect": "Tăng nguy cơ tiêu cơ vân nghiêm trọng.",
                    "management": "CHỐNG CHỈ ĐỊNH dùng chung.",
                },
                {
                    "drug": "Gemfibrozil (Fibrate)",
                    "mechanism": "Hiệp đồng độc cơ, tăng nguy cơ tiêu cơ vân.",
                    "effect": "Tăng nguy cơ tiêu cơ vân nghiêm trọng, suy thận cấp.",
                    "management": "Tránh dùng chung. Nếu cần hạ triglyceride, cân nhắc fenofibrate với liều thấp và theo dõi chặt chẽ.",
                },
            ],
            "moderate": [
                {
                    "drug": "Amiodarone",
                    "mechanism": "Ức chế CYP3A4, tăng nồng độ simvastatin.",
                    "effect": "Tăng nguy cơ tiêu cơ vân.",
                    "management": "Giới hạn Simvastatin ≤20mg/ngày. Theo dõi CK và triệu chứng đau cơ.",
                },
                {
                    "drug": "Diltiazem, Verapamil (CCB non-dihydropyridine)",
                    "mechanism": "Ức chế CYP3A4, tăng nồng độ simvastatin.",
                    "effect": "Tăng nguy cơ tiêu cơ vân.",
                    "management": "Giới hạn Simvastatin ≤10mg/ngày. Theo dõi CK và triệu chứng đau cơ.",
                },
                {
                    "drug": "Grapefruit juice",
                    "mechanism": "Ức chế CYP3A4, tăng nồng độ simvastatin.",
                    "effect": "Tăng nguy cơ tác dụng phụ của simvastatin.",
                    "management": "Tránh uống grapefruit juice hoặc giảm lượng uống.",
                },
                {
                    "drug": "Cholestyramine, Colestipol, Colesevelam",
                    "mechanism": "Cholestyramine giảm hấp thu ezetimibe.",
                    "effect": "Giảm nồng độ ezetimibe, giảm hiệu quả.",
                    "management": "Dùng cách xa ít nhất 2 giờ. Dùng ezetimibe trước hoặc sau cholestyramine ít nhất 2 giờ.",
                },
            ],
            "minor": [],
        },
        "contraindications_detail": {
            "tuyệt_đối": [
                "Dị ứng với simvastatin, ezetimibe, hoặc bất kỳ thành phần nào.",
                "Bệnh gan hoạt động (active liver disease) - tăng men gan kéo dài, viêm gan.",
                "Có thai hoặc có thể mang thai - Statin gây quái thai (FDA category X).",
                "Cho con bú - Statin bài tiết vào sữa mẹ.",
                "Tiêu cơ vân đang hoạt động (active myopathy/rhabdomyolysis).",
                "Dùng cùng cyclosporine, itraconazole, ketoconazole, hoặc grapefruit juice.",
            ],
            "tương_đối": [
                "Suy gan - thận trọng, theo dõi men gan thường xuyên.",
                "Suy thận nặng (CrCl <30) - thận trọng, có thể cần giảm liều simvastatin.",
                "Người cao tuổi - tăng nguy cơ đau cơ, tiêu cơ vân.",
                "Đái tháo đường - statins có thể tăng đường huyết nhẹ.",
                "Bệnh tuyến giáp - tăng nguy cơ đau cơ.",
                "Uống rượu nhiều - tăng nguy cơ viêm gan.",
            ],
        },
        "pregnancy_lactation": {
            "fda_category": "X",
            "pregnancy_details": (
                "CHỐNG CHỈ ĐỊNH trong thai kỳ. Statin can thiệp vào tổng hợp cholesterol cần thiết cho sự phát triển của thai nhi, "
                "có thể gây dị tật thai nhi. Ngưng thuốc ngay lập tức nếu phát hiện có thai."
            ),
            "lactation": {
                "safety": "Avoid",
                "details": "Simvastatin có khả năng bài tiết vào sữa mẹ và gây ảnh hưởng đến chuyển hóa lipid của trẻ.",
                "recommendation": "Không sử dụng. Ngưng cho con bú hoặc ngưng thuốc.",
            },
        },
        "hepatic_adjustment": {
            "mild": "Không cần chỉnh liều.",
            "moderate": "Thận trọng, giảm liều simvastatin.",
            "severe": "CHỐNG CHỈ ĐỊNH (bệnh gan hoạt động).",
            "notes": "Simvastatin chuyển hóa mạnh qua gan bởi CYP3A4; Ezetimibe chuyển hóa ở ruột và gan. Chống chỉ định trong bệnh gan hoạt động.",
        },
        "overdose_management": {
            "symptoms": [
                "Đau cơ nặng, tiêu cơ vân (do simvastatin).",
                "Suy thận cấp (do tiêu cơ vân).",
                "Tăng men gan.",
                "Rối loạn tiêu hóa (do ezetimibe).",
            ],
            "antidote": "Không có antidote đặc hiệu.",
            "treatment": [
                "Ngừng thuốc ngay lập tức.",
                "Điều trị tiêu cơ vân: Truyền dịch tích cực, điều chỉnh điện giải, theo dõi chức năng thận.",
                "Theo dõi CK, creatinine, men gan.",
                "Điều trị hỗ trợ.",
            ],
            "monitoring": "CK, creatinine, men gan (ALT, AST), điện giải, lipid profile, triệu chứng lâm sàng.",
        },
        "reversal_agents": None,
        "administration_instructions": {
            "oral": {
                "with_food": "Có thể uống với hoặc không thức ăn.",
                "timing": "Uống 1 lần/ngày vào buổi tối, cùng giờ mỗi ngày. Dùng cách xa cholestyramine ít nhất 2 giờ.",
            },
        },
        "references": {
            "primary_sources": [
                "FDA Drug Label - Vytorin (simvastatin/ezetimibe)",
                "IMPROVE-IT Study - New England Journal of Medicine (2015) - Ezetimibe + Simvastatin trong ACS",
                "SHARP Study - The Lancet (2011) - Ezetimibe + Simvastatin trong CKD",
                "ACC/AHA 2018 Cholesterol Guidelines",
            ],
            "last_updated": "2025-02-18",
            "evidence_level": "High – FDA-approved, Multiple large RCTs (IMPROVE-IT, SHARP) showing cardiovascular benefit",
        },
        "risk_flags": {
            "high_alert": True,
            "narrow_therapeutic_index": False,
            "icu_critical_care_only": False,
            "bleeding_risk": "Low",
            "organ_toxicity": {"hepatic": "High", "musculoskeletal": "High (rhabdomyolysis)", "pregnancy": "High (teratogenic)"}
        },
        "guideline_tags": [
            "ACC/AHA 2018 Cholesterol Guidelines",
            "ACC/AHA 2024 Cholesterol Management Update",
            "ESC/EAS 2019 Dyslipidemia Guidelines",
            "KDIGO 2013 Lipid Management in CKD"
        ],
    },

    "Rosuvastatin/Ezetimibe": {
        "group": "Cardiovascular - Statin + Cholesterol Absorption Inhibitor (Fixed-Dose Combination)",
        "vietnamese_name": "Rosuvastatin/Ezetimibe",
        "administration": ["PO"],
        "indications": [
            "Tăng cholesterol máu (khi cần phối hợp statin và ezetimibe để giảm LDL-C hiệu quả hơn).",
            "Tăng cholesterol máu gia đình (familial hypercholesterolemia).",
            "Phòng ngừa biến cố tim mạch ở bệnh nhân có nguy cơ cao.",
        ],
        "contraindications": [
            "Dị ứng với rosuvastatin, ezetimibe, hoặc bất kỳ thành phần nào.",
            "Bệnh gan hoạt động (active liver disease).",
            "Có thai hoặc có thể mang thai (statin chống chỉ định trong thai kỳ - FDA category X).",
            "Cho con bú.",
            "Tiêu cơ vân đang hoạt động (active myopathy/rhabdomyolysis).",
        ],
        "dosage": {
            "adult_initial": "Rosuvastatin 5mg/Ezetimibe 10mg PO mỗi ngày.",
            "adult_maintenance": "Rosuvastatin 10mg/Ezetimibe 10mg, Rosuvastatin 20mg/Ezetimibe 10mg, hoặc Rosuvastatin 40mg/Ezetimibe 10mg PO mỗi ngày.",
            "notes": "Uống 1 lần/ngày, có thể uống với hoặc không thức ăn. Rosuvastatin có thể uống bất kỳ lúc nào trong ngày.",
        },
        "renal_adjustment": {
            "normal": "Không cần chỉnh liều.",
            "30_60": "Không cần chỉnh liều.",
            "under_30": "Thận trọng, giảm liều rosuvastatin (không quá 10mg/ngày).",
        },
        "side_effects": [
            "Đau cơ, viêm cơ (do rosuvastatin) - phổ biến (~5%).",
            "Tan rã cơ (Rhabdomyolysis) - hiếm nhưng nguy hiểm (do rosuvastatin).",
            "Tăng men gan (ALT, AST) - do rosuvastatin.",
            "Rối loạn tiêu hóa (tiêu chảy, đau bụng) - do ezetimibe, nhẹ.",
            "Đau khớp, mệt mỏi.",
            "Đái tháo đường mới khởi phát (tăng đường huyết nhẹ) - do rosuvastatin.",
        ],
        "interactions": [
            "Warfarin: Tăng INR (do rosuvastatin).",
            "Fibrate (Gemfibrozil): Tăng nguy cơ tan rã cơ (tránh dùng chung).",
            "Cholestyramine: Giảm hấp thu ezetimibe - dùng cách xa ít nhất 2 giờ.",
            "Cyclosporine: Tăng nồng độ rosuvastatin, giới hạn liều rosuvastatin 5mg/ngày.",
        ],
        "pregnancy": "X: chống chỉ định trong thai kỳ (statin gây quái thai).",
        "mechanism_of_action": (
            "Rosuvastatin là statin (HMG-CoA reductase inhibitor), ức chế enzyme tổng hợp cholesterol ở gan, "
            "giảm LDL cholesterol (40-60%), tăng HDL cholesterol (5-10%). "
            "Ezetimibe là chất ức chế hấp thu cholesterol, ức chế protein NPC1L1 ở ruột non, "
            "giảm hấp thu cholesterol từ thức ăn và từ mật, giảm thêm LDL cholesterol (15-20%). "
            "Phối hợp hai thuốc có tác dụng cộng dồn, giảm LDL-C hiệu quả hơn từng thuốc đơn trị (~60-70% giảm LDL-C)."
        ),
        "monitoring": [
            "Lipid profile (LDL, HDL, Triglyceride, Total cholesterol) - Sau 4-12 tuần điều trị, sau đó định kỳ.",
            "Men gan (ALT, AST) - Trước điều trị, sau đó nếu có triệu chứng hoặc định kỳ.",
            "CK (Creatine Kinase) - Nếu có đau cơ hoặc triệu chứng nghi ngờ tiêu cơ vân.",
            "Đường huyết - Định kỳ ở bệnh nhân có nguy cơ đái tháo đường.",
            "Dấu hiệu rối loạn tiêu hóa (tiêu chảy, đau bụng) - nhẹ.",
        ],
        "precautions": [
            "QUAN TRỌNG: Chống chỉ định trong thai kỳ - Statin gây quái thai (FDA category X). Ngừng ngay khi phát hiện có thai.",
            "CHỐNG CHỈ ĐỊNH trong bệnh gan hoạt động - Statin có thể làm nặng bệnh gan.",
            "Ngừng thuốc nếu đau cơ nặng hoặc CK >10x bình thường (nghi ngờ tan rã cơ).",
            "Giảm LDL-C hiệu quả hơn từng thuốc đơn trị (~60-70% giảm LDL-C).",
            "Rosuvastatin ít tương tác thuốc hơn simvastatin (không chuyển hóa qua CYP3A4).",
            "Dùng cách xa cholestyramine ít nhất 2 giờ (giảm hấp thu ezetimibe).",
            "Thận trọng khi dùng với fibrate - tăng nguy cơ tiêu cơ vân.",
        ],
        "pharmacokinetics": {
            "half_life": "Rosuvastatin: ~19 giờ; Ezetimibe: ~22 giờ (ezetimibe), ~24 giờ (ezetimibe-glucuronide).",
            "onset": "Giảm cholesterol trong vài tuần.",
            "duration": "24 giờ (dùng 1 lần/ngày).",
            "protein_binding": "Rosuvastatin: ~88%; Ezetimibe: >90%.",
            "clearance": "Rosuvastatin: chuyển hóa một phần qua gan (CYP2C9), thải chủ yếu qua phân và nước tiểu; Ezetimibe: chuyển hóa ở ruột và gan thành ezetimibe-glucuronide, thải chủ yếu qua phân.",
        },
        "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm, tránh ánh sáng.",
        "black_box_warnings": (
            "Chống chỉ định trong thai kỳ: Statin gây quái thai và có thể gây dị tật thai nhi. "
            "Ngừng ngay khi phát hiện có thai. Chống chỉ định trong bệnh gan hoạt động. "
            "Rhabdomyolysis: Có thể gây tiêu cơ vân dẫn đến suy thận cấp."
        ),
        "drug_interactions": {
            "major": [
                {
                    "drug": "Gemfibrozil (Fibrate)",
                    "mechanism": "Hiệp đồng độc cơ, tăng nguy cơ tiêu cơ vân.",
                    "effect": "Tăng nguy cơ tiêu cơ vân nghiêm trọng, suy thận cấp.",
                    "management": "Tránh dùng chung. Nếu cần hạ triglyceride, cân nhắc fenofibrate với liều thấp và theo dõi chặt chẽ.",
                },
            ],
            "moderate": [
                {
                    "drug": "Cyclosporine",
                    "mechanism": "Ức chế OATP1B1, tăng nồng độ rosuvastatin.",
                    "effect": "Tăng nguy cơ tiêu cơ vân.",
                    "management": "Giới hạn liều rosuvastatin 5mg/ngày. Theo dõi CK và triệu chứng đau cơ.",
                },
                {
                    "drug": "Warfarin",
                    "mechanism": "Rosuvastatin có thể tăng tác dụng của warfarin.",
                    "effect": "Tăng INR, tăng nguy cơ chảy máu.",
                    "management": "Theo dõi INR chặt chẽ khi bắt đầu hoặc thay đổi liều rosuvastatin.",
                },
                {
                    "drug": "Cholestyramine, Colestipol, Colesevelam",
                    "mechanism": "Cholestyramine giảm hấp thu ezetimibe.",
                    "effect": "Giảm nồng độ ezetimibe, giảm hiệu quả.",
                    "management": "Dùng cách xa ít nhất 2 giờ. Dùng ezetimibe trước hoặc sau cholestyramine ít nhất 2 giờ.",
                },
            ],
            "minor": [],
        },
        "contraindications_detail": {
            "tuyệt_đối": [
                "Dị ứng với rosuvastatin, ezetimibe, hoặc bất kỳ thành phần nào.",
                "Bệnh gan hoạt động (active liver disease) - tăng men gan kéo dài, viêm gan.",
                "Có thai hoặc có thể mang thai - Statin gây quái thai (FDA category X).",
                "Cho con bú - Statin bài tiết vào sữa mẹ.",
                "Tiêu cơ vân đang hoạt động (active myopathy/rhabdomyolysis).",
            ],
            "tương_đối": [
                "Suy gan - thận trọng, theo dõi men gan thường xuyên.",
                "Suy thận nặng (CrCl <30) - thận trọng, giảm liều rosuvastatin (không quá 10mg/ngày).",
                "Người cao tuổi - tăng nguy cơ đau cơ, tiêu cơ vân.",
                "Đái tháo đường - statins có thể tăng đường huyết nhẹ.",
                "Bệnh tuyến giáp - tăng nguy cơ đau cơ.",
                "Uống rượu nhiều - tăng nguy cơ viêm gan.",
            ],
        },
        "pregnancy_lactation": {
            "fda_category": "X",
            "pregnancy_details": (
                "CHỐNG CHỈ ĐỊNH trong thai kỳ. Statin can thiệp vào tổng hợp cholesterol cần thiết cho sự phát triển của thai nhi, "
                "có thể gây dị tật thai nhi. Ngưng thuốc ngay lập tức nếu phát hiện có thai."
            ),
            "lactation": {
                "safety": "Avoid",
                "details": "Rosuvastatin có khả năng bài tiết vào sữa mẹ và gây ảnh hưởng đến chuyển hóa lipid của trẻ.",
                "recommendation": "Không sử dụng. Ngưng cho con bú hoặc ngưng thuốc.",
            },
        },
        "hepatic_adjustment": {
            "mild": "Không cần chỉnh liều.",
            "moderate": "Thận trọng, giảm liều rosuvastatin.",
            "severe": "CHỐNG CHỈ ĐỊNH (bệnh gan hoạt động).",
            "notes": "Rosuvastatin chuyển hóa một phần qua gan (CYP2C9); Ezetimibe chuyển hóa ở ruột và gan. Chống chỉ định trong bệnh gan hoạt động.",
        },
        "overdose_management": {
            "symptoms": [
                "Đau cơ nặng, tiêu cơ vân (do rosuvastatin).",
                "Suy thận cấp (do tiêu cơ vân).",
                "Tăng men gan.",
                "Rối loạn tiêu hóa (do ezetimibe).",
            ],
            "antidote": "Không có antidote đặc hiệu.",
            "treatment": [
                "Ngừng thuốc ngay lập tức.",
                "Điều trị tiêu cơ vân: Truyền dịch tích cực, điều chỉnh điện giải, theo dõi chức năng thận.",
                "Theo dõi CK, creatinine, men gan.",
                "Điều trị hỗ trợ.",
            ],
            "monitoring": "CK, creatinine, men gan (ALT, AST), điện giải, lipid profile, triệu chứng lâm sàng.",
        },
        "reversal_agents": None,
        "administration_instructions": {
            "oral": {
                "with_food": "Có thể uống với hoặc không thức ăn.",
                "timing": "Uống 1 lần/ngày, cùng giờ mỗi ngày. Rosuvastatin có thể uống bất kỳ lúc nào trong ngày. Dùng cách xa cholestyramine ít nhất 2 giờ.",
            },
        },
        "references": {
            "primary_sources": [
                "FDA Drug Label - Rosuvastatin/Ezetimibe",
                "ACC/AHA 2018 Cholesterol Guidelines",
            ],
            "last_updated": "2025-02-18",
            "evidence_level": "High – FDA-approved",
        },
        "risk_flags": {
            "high_alert": True,
            "narrow_therapeutic_index": False,
            "icu_critical_care_only": False,
            "bleeding_risk": "Low",
            "organ_toxicity": {"hepatic": "High", "musculoskeletal": "High (rhabdomyolysis)", "pregnancy": "High (teratogenic)"}
        },
        "guideline_tags": [
            "ACC/AHA 2018 Cholesterol Guidelines",
            "ACC/AHA 2024 Cholesterol Management Update",
            "ESC/EAS 2019 Dyslipidemia Guidelines"
        ],
    },

    "Bempedoic acid/Ezetimibe": {
        "group": "Cardiovascular - ACL Inhibitor + Cholesterol Absorption Inhibitor (Fixed-Dose Combination)",
        "vietnamese_name": "Bempedoic acid/Ezetimibe, Nexlizet",
        "administration": ["PO"],
        "indications": [
            "Tăng cholesterol máu tiên phát hoặc tăng cholesterol máu gia đình (heterozygous).",
            "Dự phòng biến cố tim mạch ở bệnh nhân không dung nạp statin hoặc cần giảm LDL-C thêm.",
            "Kết hợp để tăng hiệu quả giảm LDL-C (~38-40% giảm LDL-C).",
        ],
        "contraindications": [
            "Dị ứng với bempedoic acid, ezetimibe, hoặc bất kỳ thành phần nào.",
            "Bệnh gút đang hoạt động hoặc tăng acid uric máu không kiểm soát.",
            "Có thai hoặc có thể mang thai (FDA category X).",
        ],
        "dosage": {
            "adult_initial": "Bempedoic acid 180mg/Ezetimibe 10mg PO mỗi ngày.",
            "adult_maintenance": "Bempedoic acid 180mg/Ezetimibe 10mg PO mỗi ngày.",
            "notes": "Uống bất kỳ lúc nào, có thể uống với hoặc không thức ăn. Có thể dùng cùng hoặc không cùng statin.",
        },
        "renal_adjustment": {
            "normal": "Không cần chỉnh liều.",
            "30_60": "Không cần chỉnh liều.",
            "under_30": "Thận trọng, dữ liệu hạn chế; không khuyến cáo nếu eGFR <30.",
        },
        "side_effects": [
            "Tăng acid uric máu, bệnh gút (phổ biến - ~2%).",
            "Tăng men gan (ALT, AST).",
            "Đau cơ, đau khớp (ít hơn statin).",
            "Rối loạn tiêu hóa (tiêu chảy, đau bụng) - do ezetimibe, nhẹ.",
            "Nhiễm trùng đường hô hấp trên.",
            "Đau lưng.",
        ],
        "interactions": [
            "Simvastatin >20mg/ngày: tăng nguy cơ đau cơ, tăng CK (giảm liều simvastatin xuống ≤20mg/ngày).",
            "Pravastatin >40mg/ngày: tăng nguy cơ đau cơ (giảm liều pravastatin xuống ≤40mg/ngày).",
            "Cholestyramine: giảm hấp thu ezetimibe - dùng cách xa ít nhất 2 giờ.",
        ],
        "pregnancy": "X: Chống chỉ định trong thai kỳ.",
        "mechanism_of_action": (
            "Bempedoic acid là tiền thuốc, được chuyển hóa thành bempedoyl-CoA trong gan, "
            "ức chế ATP-citrate lyase (ACL), enzyme quan trọng trong tổng hợp cholesterol ở gan, "
            "giảm LDL-C (~18-25% khi dùng đơn trị). "
            "Ezetimibe là chất ức chế hấp thu cholesterol, ức chế protein NPC1L1 ở ruột non, "
            "giảm hấp thu cholesterol từ thức ăn và từ mật, giảm thêm LDL cholesterol (15-20%). "
            "Phối hợp hai thuốc có tác dụng cộng dồn, giảm LDL-C hiệu quả (~38-40% giảm LDL-C). "
            "Ít gây đau cơ hơn statin (bempedoic acid chỉ hoạt động ở gan)."
        ),
        "monitoring": [
            "Lipid profile (LDL-C, HDL-C, TG, Total cholesterol) sau 4-8 tuần, sau đó mỗi 3-6 tháng.",
            "Acid uric máu trước và trong điều trị (mỗi 3-6 tháng) - nguy cơ tăng acid uric và bệnh gút.",
            "Men gan (ALT, AST) trước và trong điều trị (mỗi 3-6 tháng).",
            "CK nếu có đau cơ (đặc biệt khi dùng với simvastatin/pravastatin).",
            "Dấu hiệu bệnh gút (đau khớp, sưng khớp) - đặc biệt ở người có tiền sử gút.",
        ],
        "precautions": [
            "QUAN TRỌNG: Chống chỉ định trong thai kỳ - FDA category X. Ngừng ngay khi phát hiện có thai.",
            "Tăng acid uric máu và bệnh gút: theo dõi acid uric máu, điều trị dự phòng nếu cần.",
            "Tăng men gan: theo dõi ALT, AST; ngừng nếu tăng >3x ULN.",
            "Giảm liều simvastatin xuống ≤20mg/ngày khi dùng với bempedoic acid.",
            "Giảm liều pravastatin xuống ≤40mg/ngày khi dùng với bempedoic acid.",
            "Ít gây đau cơ hơn statin (do bempedoic acid chỉ hoạt động ở gan).",
            "Có thể dùng cùng hoặc không cùng statin.",
            "Dùng cách xa cholestyramine ít nhất 2 giờ (giảm hấp thu ezetimibe).",
        ],
        "pharmacokinetics": {
            "half_life": "Bempedoic acid: ~21 giờ; Ezetimibe: ~22 giờ (ezetimibe), ~24 giờ (ezetimibe-glucuronide).",
            "onset": "Giảm LDL-C trong 2-4 tuần.",
            "duration": "24 giờ (dùng 1 lần/ngày).",
            "protein_binding": "Bempedoic acid: >99%; Ezetimibe: >90%.",
            "clearance": "Bempedoic acid: chuyển hóa ở gan thành bempedoyl-CoA (dạng hoạt tính), thải qua thận và phân; Ezetimibe: chuyển hóa ở ruột và gan thành ezetimibe-glucuronide, thải chủ yếu qua phân.",
        },
        "storage": "Bảo quản ở nhiệt độ phòng (20-25°C), tránh ẩm, tránh ánh sáng.",
        "black_box_warnings": (
            "Tăng acid uric máu và bệnh gút: có thể gây bệnh gút, đặc biệt ở người có tiền sử gút. "
            "Theo dõi acid uric máu và điều trị dự phòng nếu cần. Chống chỉ định trong thai kỳ: FDA category X."
        ),
        "drug_interactions": {
            "major": [
                {
                    "drug": "Simvastatin >20mg/ngày",
                    "mechanism": "Bempedoic acid ức chế OATP1B1, làm giảm thải trừ simvastatin, tăng nồng độ simvastatin.",
                    "effect": "Tăng nguy cơ đau cơ, tăng CK, tiêu cơ vân.",
                    "management": "GIẢM LIỀU SIMVASTATIN XUỐNG ≤20MG/NGÀY khi dùng với bempedoic acid. Theo dõi CK và triệu chứng đau cơ.",
                },
                {
                    "drug": "Pravastatin >40mg/ngày",
                    "mechanism": "Bempedoic acid ức chế OATP1B1, làm giảm thải trừ pravastatin, tăng nồng độ pravastatin.",
                    "effect": "Tăng nguy cơ đau cơ, tăng CK.",
                    "management": "GIẢM LIỀU PRAVASTATIN XUỐNG ≤40MG/NGÀY khi dùng với bempedoic acid. Theo dõi CK và triệu chứng đau cơ.",
                },
            ],
            "moderate": [
                {
                    "drug": "Cholestyramine, Colestipol, Colesevelam",
                    "mechanism": "Cholestyramine giảm hấp thu ezetimibe.",
                    "effect": "Giảm nồng độ ezetimibe, giảm hiệu quả.",
                    "management": "Dùng cách xa ít nhất 2 giờ. Dùng ezetimibe trước hoặc sau cholestyramine ít nhất 2 giờ.",
                },
            ],
            "minor": [],
        },
        "contraindications_detail": {
            "tuyệt_đối": [
                "Dị ứng với bempedoic acid, ezetimibe, hoặc bất kỳ thành phần nào.",
                "Bệnh gút đang hoạt động.",
                "Tăng acid uric máu không kiểm soát.",
                "Có thai hoặc có thể mang thai - FDA category X.",
            ],
            "tương_đối": [
                "Tiền sử bệnh gút - tăng nguy cơ tái phát, cần điều trị dự phòng.",
                "Suy thận nặng (eGFR <30) - thận trọng, dữ liệu hạn chế.",
                "Suy gan nặng - thận trọng.",
            ],
        },
        "pregnancy_lactation": {
            "fda_category": "X",
            "pregnancy_details": (
                "Chống chỉ định trong thai kỳ. Bempedoic acid có thể gây hại cho thai nhi. "
                "Phụ nữ trong độ tuổi sinh đẻ phải sử dụng biện pháp tránh thai hiệu quả khi dùng bempedoic acid."
            ),
            "lactation": {
                "safety": "Incompatible",
                "details": "Chưa rõ bài tiết vào sữa mẹ. Không khuyến cáo dùng khi cho con bú.",
                "recommendation": "Ngừng cho con bú hoặc ngừng thuốc.",
            },
        },
        "hepatic_adjustment": {
            "mild": "Không cần chỉnh liều.",
            "moderate": "Thận trọng, theo dõi men gan.",
            "severe": "Không khuyến cáo, dữ liệu hạn chế.",
            "notes": "Bempedoic acid chuyển hóa ở gan thành dạng hoạt tính; Ezetimibe chuyển hóa ở ruột và gan. Suy gan có thể ảnh hưởng đến chuyển hóa.",
        },
        "overdose_management": {
            "symptoms": [
                "Tăng acid uric máu, bệnh gút.",
                "Tăng men gan.",
                "Đau cơ (nếu dùng với simvastatin/pravastatin liều cao).",
                "Rối loạn tiêu hóa.",
            ],
            "antidote": "Không có antidote đặc hiệu.",
            "treatment": [
                "Ngừng bempedoic acid/ezetimibe nếu cần.",
                "Điều trị bệnh gút: NSAID, colchicine, hoặc allopurinol nếu cần.",
                "Theo dõi men gan, CK.",
                "Điều trị hỗ trợ.",
            ],
            "monitoring": "Acid uric máu, men gan, CK, lipid profile, triệu chứng lâm sàng.",
        },
        "reversal_agents": None,
        "administration_instructions": {
            "oral": {
                "with_food": "Uống bất kỳ lúc nào, có thể uống với hoặc không thức ăn.",
                "timing": "Uống 1 lần/ngày, cùng giờ mỗi ngày. Có thể dùng cùng hoặc không cùng statin. Dùng cách xa cholestyramine ít nhất 2 giờ.",
            },
        },
        "references": {
            "primary_sources": [
                "FDA Drug Label - Nexlizet (bempedoic acid + ezetimibe)",
                "CLEAR Outcomes trial - Bempedoic acid cardiovascular outcomes",
                "ACC/AHA Guidelines - Cholesterol Management 2024",
            ],
            "last_updated": "2025-02-18",
            "evidence_level": "High – FDA-approved, large RCT (CLEAR Outcomes)",
        },
        "risk_flags": {
            "high_alert": False,
            "narrow_therapeutic_index": False,
            "icu_critical_care_only": False,
            "bleeding_risk": "Low",
            "organ_toxicity": {"hepatic": "Moderate", "metabolic": "Moderate (hyperuricemia, gout)"}
        },
        "guideline_tags": [
            "ACC/AHA 2018 Cholesterol Guidelines",
            "ACC/AHA 2024 Cholesterol Management Update",
            "ESC/EAS 2019 Dyslipidemia Guidelines"
        ],
    },

}

__all__ = ["CARDIOVASCULAR_FIXED_DOSE_COMBINATIONS"]

