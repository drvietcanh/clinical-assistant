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

}

__all__ = ["CARDIOVASCULAR_FIXED_DOSE_COMBINATIONS"]

