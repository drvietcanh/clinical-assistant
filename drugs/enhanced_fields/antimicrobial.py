"""
Enhanced fields overrides - Antimicrobial
"""
from typing import Any, Dict


ANTIMICROBIAL_ENHANCED_FIELDS: Dict[str, Dict[str, Any]] = {
        # ======================== ANTIBIOTICS: GLYCOPEPTIDES =======================
        "Vancomycin": {
            "contraindications": {
                "tuyệt_đối": [
                    "Dị ứng với vancomycin hoặc bất kỳ thành phần nào",
                ],
                "tương_đối": [
                    "Suy thận nặng (CrCl <10) - thận trọng, cần điều chỉnh liều và TDM",
                    "Độc thận đang hoạt động",
                    "Độc thính giác đang hoạt động",
                ],
            },
            "pregnancy_lactation": {
                "fda_category": "C",
                "pregnancy_details": (
                    "Sử dụng nếu lợi ích vượt trội nguy cơ. Vancomycin có thể qua nhau thai. "
                    "Dữ liệu hạn chế nhưng được sử dụng rộng rãi trong nhiễm khuẩn nặng ở thai kỳ. "
                    "Theo dõi chức năng thận và thính giác của mẹ."
                ),
                "lactation": {
                    "safety": "Caution",
                    "details": "Bài tiết vào sữa mẹ với lượng nhỏ. Có thể gây tiêu chảy hoặc phát ban ở trẻ.",
                    "recommendation": "Có thể dùng khi cho con bú nhưng theo dõi trẻ về tiêu chảy, phát ban. Cân nhắc ngừng cho bú tạm thời nếu có triệu chứng.",
                },
            },
            "hepatic_adjustment": {
                "mild": "Không cần chỉnh liều.",
                "moderate": "Không cần chỉnh liều.",
                "severe": "Không cần chỉnh liều.",
                "notes": "Vancomycin không chuyển hóa đáng kể qua gan, thải trừ chủ yếu qua thận.",
            },
            "overdose_management": {
                "symptoms": [
                    "Độc thận (nephrotoxicity) - tăng creatinine, suy thận cấp",
                    "Độc thính giác (ototoxicity) - điếc, ù tai",
                    "Red man syndrome - đỏ bừng mặt, cổ, ngực, hạ huyết áp (nếu truyền quá nhanh)",
                    "Giảm bạch cầu, giảm tiểu cầu (hiếm, khi dùng kéo dài)",
                ],
                "antidote": "Không có antidote đặc hiệu.",
                "treatment": [
                    "Ngừng vancomycin ngay lập tức",
                    "Đo nồng độ vancomycin (trough và peak nếu có thể)",
                    "Đo chức năng thận (creatinine, eGFR) ngay",
                    "Nếu độc thận:",
                    "  - Truyền dịch tích cực để duy trì lượng nước tiểu",
                    "  - Theo dõi chức năng thận hàng ngày",
                    "  - Hemodialysis nếu suy thận cấp nặng (vancomycin có thể được lọc)",
                    "Nếu red man syndrome:",
                    "  - Ngừng truyền ngay",
                    "  - Diphenhydramine (antihistamine) nếu cần",
                    "  - Theo dõi huyết áp",
                    "  - Truyền lại chậm hơn (ít nhất 60 phút) sau khi triệu chứng hết",
                    "Theo dõi thính giác nếu có triệu chứng",
                    "Theo dõi công thức máu nếu dùng kéo dài",
                ],
                "monitoring": "Nồng độ vancomycin (trough), creatinine, eGFR, lượng nước tiểu, thính giác, công thức máu, dấu hiệu red man syndrome.",
            },
            "reversal_agents": {
                "available": False,
                "agents": [],
                "notes": "Không có thuốc giải độc đặc hiệu. Hemodialysis có thể loại bỏ một phần vancomycin nhưng không khuyến cáo thường quy.",
            },
            "administration_instructions": {
                "iv": {
                    "reconstitution": "Pha trong NaCl 0.9% hoặc D5W, nồng độ không quá 5 mg/ml.",
                    "infusion_rate": "Truyền IV trong ít nhất 60 phút (liều chuẩn) để tránh red man syndrome. Không truyền quá nhanh.",
                    "notes": "TDM BẮT BUỘC. Điều chỉnh liều theo chức năng thận và nồng độ trough. Tránh dùng với thuốc độc thận khác.",
                },
                "oral": {
                    "with_food": "Có thể uống với hoặc không có thức ăn.",
                    "timing": "Uống 4 lần/ngày, cách đều.",
                    "notes": "Chỉ dùng đường uống cho viêm đại tràng do C. difficile. Không hấp thu qua đường tiêu hóa, chỉ tác dụng tại chỗ.",
                },
            },
            "risk_flags": {
                "high_alert": True,
                "narrow_therapeutic_index": True,
                "icu_critical_care_only": False,
                "bleeding_risk": False,
                "organ_toxicity": {"renal": "High", "auditory": "High"},
                "qt_prolongation": False,
                "hepatotoxicity": False,
                "nephrotoxicity": True,
                "requires_monitoring": [
                    "Vancomycin trough level - CRITICAL (target 10-20 mcg/ml)",
                    "Renal function (creatinine, eGFR) - CRITICAL",
                    "Urine output",
                    "Auditory function (hearing loss risk)",
                    "Complete blood count (if prolonged use)",
                    "Signs of red man syndrome (if rapid infusion)"
                ],
                "look_alike_sound_alike": ["Vancomycin", "Vancocin"]
            },
            "guideline_tags": [
                "IDSA MRSA Infection Guidelines",
                "IDSA Healthcare-Associated Pneumonia Guidelines",
                "IDSA Skin and Soft Tissue Infection Guidelines",
                "IDSA Clostridium difficile Infection Guidelines",
                "ASHP Guidelines - Vancomycin Therapeutic Monitoring",
                "FDA Drug Label - Vancomycin (nephrotoxicity and ototoxicity warnings)"
            ]
        },

        # ======================== ANTIBIOTICS: AMINOGLYCOSIDES ======================
        "Gentamicin": {
            "contraindications": {
                "tuyệt_đối": [
                    "Dị ứng với aminoglycoside",
                    "Myasthenia gravis",
                ],
                "tương_đối": [
                    "Suy thận nặng (CrCl <10) - thận trọng, cần điều chỉnh liều và TDM",
                    "Độc thận đang hoạt động",
                    "Độc thính giác đang hoạt động",
                    "Độc tiền đình đang hoạt động",
                ],
            },
            "pregnancy_lactation": {
                "fda_category": "D",
                "pregnancy_details": (
                    "Độc thai nhi. Gentamicin có thể qua nhau thai và gây độc thính giác ở thai nhi. "
                    "CHỈ dùng trong thai kỳ nếu lợi ích vượt trội nguy cơ (nhiễm khuẩn đe dọa tính mạng). "
                    "Theo dõi chức năng thận và thính giác của mẹ."
                ),
                "lactation": {
                    "safety": "Caution",
                    "details": "Bài tiết vào sữa mẹ với lượng nhỏ. Có thể gây độc thính giác ở trẻ.",
                    "recommendation": "Thận trọng khi cho con bú. Cân nhắc ngừng cho bú tạm thời hoặc đổi thuốc khác.",
                },
            },
            "hepatic_adjustment": {
                "mild": "Không cần chỉnh liều.",
                "moderate": "Không cần chỉnh liều.",
                "severe": "Không cần chỉnh liều.",
                "notes": "Gentamicin không chuyển hóa qua gan, thải trừ chủ yếu qua thận.",
            },
            "overdose_management": {
                "symptoms": [
                    "Độc thận (nephrotoxicity) - tăng creatinine, suy thận cấp",
                    "Độc thính giác (ototoxicity) - điếc không hồi phục, ù tai",
                    "Độc tiền đình (vestibular toxicity) - chóng mặt, mất thăng bằng",
                    "Block thần kinh-cơ (neuromuscular blockade) - suy hô hấp, nguy hiểm tính mạng",
                ],
                "antidote": "Calcium gluconate hoặc calcium chloride cho neuromuscular blockade. Neostigmine có thể giúp.",
                "treatment": [
                    "Ngừng gentamicin ngay lập tức",
                    "Đo nồng độ gentamicin (peak và trough) ngay",
                    "Đo chức năng thận (creatinine, eGFR) ngay",
                    "Nếu độc thận:",
                    "  - Truyền dịch tích cực để duy trì lượng nước tiểu",
                    "  - Theo dõi chức năng thận hàng ngày",
                    "  - Hemodialysis nếu suy thận cấp nặng (gentamicin có thể được lọc)",
                    "Nếu neuromuscular blockade:",
                    "  - Đảm bảo đường thở, hỗ trợ hô hấp",
                    "  - Calcium gluconate 1-3g IV hoặc calcium chloride",
                    "  - Neostigmine (nếu cần)",
                    "Theo dõi thính giác và tiền đình",
                    "Theo dõi điện giải (natri, kali, magie)",
                ],
                "monitoring": "Nồng độ gentamicin (peak, trough), creatinine, eGFR, lượng nước tiểu, thính giác, tiền đình, điện giải, dấu hiệu neuromuscular blockade.",
            },
            "reversal_agents": {
                "available": True,
                "agents": ["Calcium gluconate", "Calcium chloride", "Neostigmine (cho neuromuscular blockade)"],
                "notes": "Calcium có thể đối kháng neuromuscular blockade. Neostigmine có thể giúp. Hemodialysis có thể loại bỏ gentamicin nhưng không khuyến cáo thường quy.",
            },
            "administration_instructions": {
                "iv": {
                    "reconstitution": "Pha trong NaCl 0.9% hoặc D5W.",
                    "infusion_rate": "Truyền IV trong 30-60 phút (liều một lần/ngày) hoặc tiêm IV bolus.",
                    "notes": "TDM BẮT BUỘC. Điều chỉnh liều theo chức năng thận. Liều một lần/ngày được ưa chuộng. Không pha trộn với beta-lactams.",
                },
                "im": {
                    "site": "Tiêm sâu vào cơ (mông, đùi).",
                    "notes": "TDM BẮT BUỘC. Điều chỉnh liều theo chức năng thận.",
                },
            },
            "risk_flags": {
                "high_alert": True,
                "narrow_therapeutic_index": True,
                "icu_critical_care_only": False,
                "bleeding_risk": False,
                "organ_toxicity": {"renal": "High", "auditory": "High", "vestibular": "High", "neuromuscular": "Moderate"},
                "qt_prolongation": False,
                "hepatotoxicity": False,
                "nephrotoxicity": True,
                "requires_monitoring": [
                    "Gentamicin peak and trough levels - CRITICAL",
                    "Renal function (creatinine, eGFR) - CRITICAL",
                    "Urine output",
                    "Auditory function (hearing loss risk)",
                    "Vestibular function (dizziness, balance)",
                    "Signs of neuromuscular blockade (respiratory depression)",
                    "Electrolytes (sodium, potassium, magnesium)"
                ],
                "look_alike_sound_alike": ["Gentamicin", "Tobramycin", "Amikacin"]
            },
            "guideline_tags": [
                "IDSA Healthcare-Associated Pneumonia Guidelines",
                "IDSA Complicated Urinary Tract Infection Guidelines",
                "IDSA Complicated Intra-abdominal Infection Guidelines",
                "ASHP Guidelines - Aminoglycoside Therapeutic Monitoring",
                "FDA Drug Label - Gentamicin (nephrotoxicity, ototoxicity, neuromuscular blockade warnings)"
            ]
        },

        "Amikacin": {
            "contraindications": {
                "tuyệt_đối": [
                    "Dị ứng với aminoglycoside",
                    "Myasthenia gravis",
                ],
                "tương_đối": [
                    "Suy thận nặng (CrCl <10) - thận trọng, cần điều chỉnh liều và TDM",
                    "Độc thận đang hoạt động",
                    "Độc thính giác đang hoạt động",
                ],
            },
            "drug_interactions": {
                "major": [
                    {
                        "drug": "Vancomycin",
                        "mechanism": "Cả hai đều độc thận, tác dụng cộng dồn",
                        "effect": "Tăng nguy cơ độc thận nặng",
                        "management": "Tránh dùng đồng thời nếu có thể. Nếu bắt buộc, theo dõi chức năng thận sát, TDM cho cả hai.",
                    },
                    {
                        "drug": "Furosemide",
                        "mechanism": "Tăng độc thận và độc thính giác",
                        "effect": "Tăng nguy cơ độc thận và độc thính giác",
                        "management": "Tránh dùng đồng thời nếu có thể.",
                    },
                ],
                "moderate": [
                    {
                        "drug": "Beta-lactams",
                        "mechanism": "Beta-lactams có thể bất hoạt amikacin khi pha chung",
                        "effect": "Giảm hiệu quả kháng khuẩn",
                        "management": "Không pha trộn. Truyền riêng, cách xa.",
                    },
                ],
                "minor": [],
            },
            "pregnancy_lactation": {
                "fda_category": "D",
                "pregnancy_details": (
                    "Độc thai nhi. Amikacin có thể qua nhau thai và gây độc thính giác ở thai nhi. "
                    "CHỈ dùng trong thai kỳ nếu lợi ích vượt trội nguy cơ (nhiễm khuẩn đe dọa tính mạng)."
                ),
                "lactation": {
                    "safety": "Caution",
                    "details": "Bài tiết vào sữa mẹ. Có thể gây độc thính giác ở trẻ.",
                    "recommendation": "Thận trọng khi cho con bú. Cân nhắc ngừng cho bú tạm thời hoặc đổi thuốc khác.",
                },
            },
            "hepatic_adjustment": {
                "mild": "Không cần chỉnh liều.",
                "moderate": "Không cần chỉnh liều.",
                "severe": "Không cần chỉnh liều.",
                "notes": "Amikacin không chuyển hóa qua gan, thải trừ chủ yếu qua thận.",
            },
            "overdose_management": {
                "symptoms": [
                    "Độc thận (nephrotoxicity)",
                    "Độc thính giác (ototoxicity)",
                    "Độc tiền đình (vestibular toxicity)",
                    "Block thần kinh-cơ (neuromuscular blockade)",
                ],
                "antidote": "Calcium gluconate cho neuromuscular blockade.",
                "treatment": [
                    "Ngừng amikacin ngay",
                    "Đo nồng độ amikacin (peak, trough)",
                    "Đo chức năng thận",
                    "Truyền dịch nếu độc thận",
                    "Calcium gluconate nếu neuromuscular blockade",
                    "Hemodialysis nếu cần",
                ],
                "monitoring": "Nồng độ amikacin, creatinine, eGFR, thính giác, tiền đình.",
            },
            "reversal_agents": {
                "available": True,
                "agents": ["Calcium gluconate", "Calcium chloride"],
                "notes": "Calcium có thể đối kháng neuromuscular blockade.",
            },
            "administration_instructions": {
                "iv": {
                    "reconstitution": "Pha trong NaCl 0.9% hoặc D5W.",
                    "infusion_rate": "Truyền IV trong 30-60 phút (liều một lần/ngày) hoặc tiêm IV bolus.",
                    "notes": "TDM BẮT BUỘC. Điều chỉnh liều theo chức năng thận. Không pha trộn với beta-lactams.",
                },
                "im": {
                    "site": "Tiêm sâu vào cơ.",
                    "notes": "TDM BẮT BUỘC. Điều chỉnh liều theo chức năng thận.",
                },
            },
            "risk_flags": {
                "high_alert": True,
                "narrow_therapeutic_index": True,
                "icu_critical_care_only": False,
                "bleeding_risk": False,
                "organ_toxicity": {"renal": "High", "auditory": "High", "vestibular": "High", "neuromuscular": "Moderate"},
                "qt_prolongation": False,
                "hepatotoxicity": False,
                "nephrotoxicity": True,
                "requires_monitoring": [
                    "Amikacin peak and trough levels - CRITICAL",
                    "Renal function (creatinine, eGFR) - CRITICAL",
                    "Urine output",
                    "Auditory function (hearing loss risk)",
                    "Vestibular function (dizziness, balance)",
                    "Signs of neuromuscular blockade (respiratory depression)",
                    "Electrolytes (sodium, potassium, magnesium)"
                ],
                "look_alike_sound_alike": ["Amikacin", "Gentamicin", "Tobramycin"]
            },
            "guideline_tags": [
                "IDSA Healthcare-Associated Pneumonia Guidelines",
                "IDSA Complicated Urinary Tract Infection Guidelines",
                "IDSA Multidrug-Resistant Gram-Negative Infection Guidelines",
                "ASHP Guidelines - Aminoglycoside Therapeutic Monitoring",
                "FDA Drug Label - Amikacin (nephrotoxicity, ototoxicity warnings)"
            ]
        },

        # ======================== ANTIBIOTICS: AMINOGLYCOSIDES (continued) =========
        "Tobramycin": {
            "contraindications": {
                "tuyệt_đối": [
                    "Dị ứng với aminoglycoside",
                    "Myasthenia gravis",
                ],
                "tương_đối": [
                    "Suy thận nặng (CrCl <10) - thận trọng, cần điều chỉnh liều và TDM",
                    "Độc thận đang hoạt động",
                    "Độc thính giác đang hoạt động",
                ],
            },
            "pregnancy_lactation": {
                "fda_category": "D",
                "pregnancy_details": (
                    "Độc thai nhi. Tobramycin có thể qua nhau thai và gây độc thính giác ở thai nhi. "
                    "CHỈ dùng trong thai kỳ nếu lợi ích vượt trội nguy cơ (nhiễm khuẩn đe dọa tính mạng)."
                ),
                "lactation": {
                    "safety": "Caution",
                    "details": "Bài tiết vào sữa mẹ. Có thể gây độc thính giác ở trẻ.",
                    "recommendation": "Thận trọng khi cho con bú. Cân nhắc ngừng cho bú tạm thời hoặc đổi thuốc khác.",
                },
            },
            "hepatic_adjustment": {
                "mild": "Không cần chỉnh liều.",
                "moderate": "Không cần chỉnh liều.",
                "severe": "Không cần chỉnh liều.",
                "notes": "Tobramycin không chuyển hóa qua gan, thải trừ chủ yếu qua thận.",
            },
            "overdose_management": {
                "symptoms": [
                    "Độc thận (nephrotoxicity)",
                    "Độc thính giác (ototoxicity)",
                    "Độc tiền đình (vestibular toxicity)",
                    "Block thần kinh-cơ (neuromuscular blockade)",
                ],
                "antidote": "Calcium gluconate cho neuromuscular blockade.",
                "treatment": [
                    "Ngừng tobramycin ngay",
                    "Đo nồng độ tobramycin (peak, trough)",
                    "Đo chức năng thận",
                    "Truyền dịch nếu độc thận",
                    "Calcium gluconate nếu neuromuscular blockade",
                    "Hemodialysis nếu cần",
                ],
                "monitoring": "Nồng độ tobramycin, creatinine, eGFR, thính giác, tiền đình.",
            },
            "reversal_agents": {
                "available": True,
                "agents": ["Calcium gluconate", "Calcium chloride"],
                "notes": "Calcium có thể đối kháng neuromuscular blockade.",
            },
            "administration_instructions": {
                "iv": {
                    "reconstitution": "Pha trong NaCl 0.9% hoặc D5W.",
                    "infusion_rate": "Truyền IV trong 30-60 phút (liều một lần/ngày) hoặc tiêm IV bolus.",
                    "notes": "TDM BẮT BUỘC. Điều chỉnh liều theo chức năng thận. Không pha trộn với beta-lactams.",
                },
                "im": {
                    "site": "Tiêm sâu vào cơ.",
                    "notes": "TDM BẮT BUỘC. Điều chỉnh liều theo chức năng thận.",
                },
                "inhaled": {
                    "notes": "Dạng hít cho bệnh nhân xơ nang (CF) để điều trị nhiễm Pseudomonas mãn tính.",
                },
            },
            "risk_flags": {
                "high_alert": True,
                "narrow_therapeutic_index": True,
                "icu_critical_care_only": False,
                "bleeding_risk": False,
                "organ_toxicity": {"renal": "High", "auditory": "High", "vestibular": "High", "neuromuscular": "Moderate"},
                "qt_prolongation": False,
                "hepatotoxicity": False,
                "nephrotoxicity": True,
                "requires_monitoring": [
                    "Tobramycin peak and trough levels - CRITICAL",
                    "Renal function (creatinine, eGFR) - CRITICAL",
                    "Urine output",
                    "Auditory function (hearing loss risk)",
                    "Vestibular function (dizziness, balance)",
                    "Signs of neuromuscular blockade (respiratory depression)",
                    "Electrolytes (sodium, potassium, magnesium)"
                ],
                "look_alike_sound_alike": ["Tobramycin", "Gentamicin", "Amikacin"]
            },
            "guideline_tags": [
                "IDSA Healthcare-Associated Pneumonia Guidelines",
                "IDSA Complicated Urinary Tract Infection Guidelines",
                "IDSA Cystic Fibrosis Pulmonary Infection Guidelines",
                "ASHP Guidelines - Aminoglycoside Therapeutic Monitoring",
                "FDA Drug Label - Tobramycin (nephrotoxicity, ototoxicity warnings)"
            ]
        },

        # ======================== ANTIBIOTICS: POLYMYXINS ==========================
        "Colistin": {
            "contraindications": {
                "tuyệt_đối": [
                    "Dị ứng với colistin hoặc polymyxin",
                    "Myasthenia gravis - CHỐNG CHỈ ĐỊNH",
                ],
                "tương_đối": [
                    "Suy thận nặng (CrCl <30) - thận trọng, cần điều chỉnh liều",
                    "Suy thận cấp - thận trọng",
                    "Độc thận đang hoạt động",
                    "Độc thần kinh đang hoạt động",
                ],
            },
            "pregnancy_lactation": {
                "fda_category": "C",
                "pregnancy_details": (
                    "Sử dụng nếu lợi ích vượt trội nguy cơ. Colistin có thể qua nhau thai. "
                    "Độc thận và độc thần kinh cao. CHỈ dùng khi không còn lựa chọn khác (MDR Gram-âm đe dọa tính mạng)."
                ),
                "lactation": {
                    "safety": "Caution",
                    "details": "Bài tiết vào sữa mẹ. Có thể gây độc tính ở trẻ.",
                    "recommendation": "Thận trọng khi cho con bú. Cân nhắc ngừng cho bú tạm thời hoặc đổi thuốc khác.",
                },
            },
            "hepatic_adjustment": {
                "mild": "Không cần chỉnh liều.",
                "moderate": "Không cần chỉnh liều.",
                "severe": "Không cần chỉnh liều.",
                "notes": "Colistin không chuyển hóa đáng kể qua gan, thải trừ chủ yếu qua thận.",
            },
            "overdose_management": {
                "symptoms": [
                    "Độc thận (nephrotoxicity) - tăng creatinine, suy thận cấp",
                    "Độc thần kinh (neurotoxicity) - tê bì, yếu cơ, co giật",
                    "Block thần kinh-cơ (neuromuscular blockade) - suy hô hấp, nguy hiểm tính mạng",
                ],
                "antidote": "Calcium gluconate cho neuromuscular blockade.",
                "treatment": [
                    "Ngừng colistin ngay",
                    "Đo chức năng thận ngay",
                    "Nếu độc thận: truyền dịch tích cực, theo dõi chức năng thận, hemodialysis nếu cần",
                    "Nếu neuromuscular blockade: đảm bảo đường thở, hỗ trợ hô hấp, calcium gluconate",
                    "Theo dõi dấu hiệu độc thần kinh",
                ],
                "monitoring": "Creatinine, eGFR, BUN, dấu hiệu độc thần kinh, chức năng hô hấp, điện giải.",
            },
            "reversal_agents": {
                "available": True,
                "agents": ["Calcium gluconate", "Calcium chloride"],
                "notes": "Calcium có thể đối kháng neuromuscular blockade.",
            },
            "administration_instructions": {
                "iv": {
                    "reconstitution": "Pha trong NaCl 0.9% hoặc D5W.",
                    "infusion_rate": "Truyền IV trong 30-60 phút.",
                    "notes": "Điều chỉnh liều theo chức năng thận. Theo dõi chức năng thận hàng ngày. Tránh dùng với aminoglycosides hoặc thuốc giãn cơ.",
                },
                "inhaled": {
                    "notes": "Dạng hít cho bệnh nhân xơ nang (CF) để điều trị nhiễm Pseudomonas mãn tính.",
                },
            },
        },

        # ======================== ANTIBIOTICS: LIPOPEPTIDES ========================
        "Daptomycin": {
            "contraindications": {
                "tuyệt_đối": [
                    "Dị ứng với daptomycin",
                    "Viêm cơ (myositis) - CHỐNG CHỈ ĐỊNH",
                ],
                "tương_đối": [
                    "Suy thận nặng (CrCl <30) - cần điều chỉnh liều",
                    "Đang dùng statin hoặc fibrate - tăng nguy cơ viêm cơ",
                ],
            },
            "pregnancy_lactation": {
                "fda_category": "B",
                "pregnancy_details": (
                    "Sử dụng nếu lợi ích vượt trội nguy cơ. Dữ liệu hạn chế nhưng được sử dụng rộng rãi. "
                    "Theo dõi CPK và chức năng thận của mẹ."
                ),
                "lactation": {
                    "safety": "Caution",
                    "details": "Chưa rõ có bài tiết vào sữa mẹ hay không. Thận trọng khi cho con bú.",
                    "recommendation": "Thận trọng khi cho con bú. Cân nhắc ngừng cho bú tạm thời hoặc đổi thuốc khác.",
                },
            },
            "hepatic_adjustment": {
                "mild": "Không cần chỉnh liều.",
                "moderate": "Không cần chỉnh liều.",
                "severe": "Không cần chỉnh liều.",
                "notes": "Daptomycin không chuyển hóa đáng kể qua gan, thải trừ chủ yếu qua thận.",
            },
            "overdose_management": {
                "symptoms": [
                    "Viêm cơ (myositis) - tăng CPK, đau cơ, yếu cơ, rhabdomyolysis",
                    "Độc thận (nephrotoxicity) - tăng creatinine",
                ],
                "antidote": "Không có antidote đặc hiệu.",
                "treatment": [
                    "Ngừng daptomycin ngay",
                    "Đo CPK ngay",
                    "Nếu CPK >5x ULN hoặc có triệu chứng viêm cơ → DỪNG NGAY",
                    "Đo chức năng thận",
                    "Truyền dịch tích cực nếu rhabdomyolysis",
                    "Theo dõi CPK và chức năng thận hàng ngày",
                ],
                "monitoring": "CPK (bắt buộc), creatinine, eGFR, triệu chứng viêm cơ (đau cơ, yếu cơ, nước tiểu sẫm màu).",
            },
            "reversal_agents": {
                "available": False,
                "agents": [],
                "notes": "Không có thuốc giải độc đặc hiệu. Ngừng thuốc là biện pháp chính.",
            },
            "administration_instructions": {
                "iv": {
                    "reconstitution": "Pha trong NaCl 0.9%.",
                    "infusion_rate": "Truyền IV trong 30 phút.",
                    "notes": "CPK monitoring BẮT BUỘC. Điều chỉnh liều theo chức năng thận. DỪNG NGAY nếu CPK >5x ULN hoặc có triệu chứng viêm cơ. CHỐNG CHỈ ĐỊNH trong viêm phổi.",
                },
            },
        },

        # ======================== ANTIBIOTICS: CEPHALOSPORINS ======================
        "Cefazolin": {
            "contraindications": {
                "tuyệt_đối": [
                    "Dị ứng cephalosporin hoặc beta-lactam (phản ứng type I)",
                ],
                "tương_đối": [
                    "Dị ứng penicillin (phản ứng chéo ~5-10%)",
                    "Suy thận nặng (CrCl <10) - cần điều chỉnh liều",
                ],
            },
            "drug_interactions": {
                "major": [],
                "moderate": [
                    {
                        "drug": "Probenecid",
                        "mechanism": "Ức chế bài tiết ống thận, tăng nồng độ cefazolin",
                        "effect": "Tăng nồng độ cefazolin",
                        "management": "Có thể cần giảm liều cefazolin.",
                    },
                    {
                        "drug": "Warfarin",
                        "mechanism": "Có thể ảnh hưởng hệ vi khuẩn đường ruột",
                        "effect": "Có thể tăng INR",
                        "management": "Theo dõi INR khi dùng cefazolin.",
                    },
                ],
                "minor": [],
            },
            "pregnancy_lactation": {
                "fda_category": "B",
                "pregnancy_details": "An toàn trong thai kỳ. Cephalosporins được sử dụng rộng rãi trong thai kỳ.",
                "lactation": {
                    "safety": "Compatible",
                    "details": "Bài tiết vào sữa mẹ ở nồng độ thấp. An toàn khi cho con bú.",
                    "recommendation": "Có thể dùng khi cho con bú.",
                },
            },
            "hepatic_adjustment": {
                "mild": "Không cần chỉnh liều.",
                "moderate": "Không cần chỉnh liều.",
                "severe": "Không cần chỉnh liều.",
                "notes": "Cefazolin không chuyển hóa qua gan, thải trừ chủ yếu qua thận.",
            },
            "overdose_management": {
                "symptoms": ["Co giật (hiếm)", "Suy thận cấp (hiếm)", "Phản ứng dị ứng"],
                "antidote": "Không có antidote đặc hiệu.",
                "treatment": [
                    "Ngừng cefazolin ngay",
                    "Điều trị hỗ trợ triệu chứng",
                    "Hemodialysis có thể loại bỏ một phần",
                ],
                "monitoring": "Chức năng thận, dấu hiệu dị ứng, co giật.",
            },
            "reversal_agents": {
                "available": False,
                "agents": [],
                "notes": "Không có thuốc giải độc đặc hiệu.",
            },
            "administration_instructions": {
                "iv": {
                    "reconstitution": "Pha trong NaCl 0.9% hoặc D5W.",
                    "infusion_rate": "Tiêm IV bolus hoặc truyền trong 30 phút.",
                    "notes": "Điều chỉnh liều theo chức năng thận. Không pha trộn với aminoglycosides.",
                },
                "im": {
                    "site": "Tiêm sâu vào cơ.",
                    "notes": "Điều chỉnh liều theo chức năng thận.",
                },
            },
        },

        "Cefuroxime": {
            "contraindications": {
                "tuyệt_đối": [
                    "Dị ứng cephalosporin hoặc beta-lactam",
                ],
                "tương_đối": [
                    "Dị ứng penicillin (phản ứng chéo ~5-10%)",
                    "Suy thận nặng (CrCl <10) - cần điều chỉnh liều",
                ],
            },
            "drug_interactions": {
                "major": [],
                "moderate": [
                    {
                        "drug": "Probenecid",
                        "mechanism": "Tăng nồng độ cefuroxime",
                        "effect": "Tăng nồng độ cefuroxime",
                        "management": "Có thể cần giảm liều.",
                    },
                    {
                        "drug": "Warfarin",
                        "mechanism": "Có thể tăng INR",
                        "effect": "Tăng INR",
                        "management": "Theo dõi INR.",
                    },
                ],
                "minor": [],
            },
            "pregnancy_lactation": {
                "fda_category": "B",
                "pregnancy_details": "An toàn trong thai kỳ.",
                "lactation": {
                    "safety": "Compatible",
                    "details": "Bài tiết vào sữa mẹ ở nồng độ thấp.",
                    "recommendation": "Có thể dùng khi cho con bú.",
                },
            },
            "hepatic_adjustment": {
                "mild": "Không cần chỉnh liều.",
                "moderate": "Không cần chỉnh liều.",
                "severe": "Không cần chỉnh liều.",
                "notes": "Cefuroxime không chuyển hóa qua gan, thải trừ chủ yếu qua thận.",
            },
            "overdose_management": {
                "symptoms": ["Co giật (hiếm)", "Suy thận cấp (hiếm)"],
                "antidote": "Không có antidote đặc hiệu.",
                "treatment": ["Ngừng cefuroxime", "Điều trị hỗ trợ", "Hemodialysis nếu cần"],
                "monitoring": "Chức năng thận, dấu hiệu dị ứng.",
            },
            "reversal_agents": {
                "available": False,
                "agents": [],
                "notes": "Không có thuốc giải độc đặc hiệu.",
            },
            "administration_instructions": {
                "oral": {
                    "with_food": "Uống với thức ăn để tăng hấp thu.",
                    "timing": "Uống 2 lần/ngày.",
                    "notes": "Tránh antacid trong 2 giờ.",
                },
                "iv": {
                    "reconstitution": "Pha trong NaCl 0.9% hoặc D5W.",
                    "infusion_rate": "Truyền trong 30 phút.",
                    "notes": "Điều chỉnh liều theo chức năng thận.",
                },
            },
        },

        "Cefaclor": {
            "contraindications": {
                "tuyệt_đối": ["Dị ứng cephalosporin hoặc beta-lactam"],
                "tương_đối": ["Dị ứng penicillin", "Suy thận nặng"],
            },
            "drug_interactions": {
                "major": [],
                "moderate": [
                    {"drug": "Probenecid", "mechanism": "Tăng nồng độ", "effect": "Tăng nồng độ", "management": "Có thể cần giảm liều."},
                    {"drug": "Warfarin", "mechanism": "Có thể tăng INR", "effect": "Tăng INR", "management": "Theo dõi INR."},
                ],
                "minor": [],
            },
            "pregnancy_lactation": {
                "fda_category": "B",
                "pregnancy_details": "An toàn trong thai kỳ.",
                "lactation": {"safety": "Compatible", "details": "Bài tiết vào sữa mẹ ở nồng độ thấp.", "recommendation": "Có thể dùng khi cho con bú."},
            },
            "hepatic_adjustment": {"mild": "Không cần chỉnh liều.", "moderate": "Không cần chỉnh liều.", "severe": "Không cần chỉnh liều.", "notes": "Cefaclor không chuyển hóa qua gan, thải trừ chủ yếu qua thận."},
            "overdose_management": {
                "symptoms": ["Co giật (hiếm)", "Suy thận cấp (hiếm)"],
                "antidote": "Không có antidote đặc hiệu.",
                "treatment": ["Ngừng cefaclor", "Điều trị hỗ trợ"],
                "monitoring": "Chức năng thận, dấu hiệu dị ứng.",
            },
            "reversal_agents": {"available": False, "agents": [], "notes": "Không có thuốc giải độc đặc hiệu."},
            "administration_instructions": {
                "oral": {
                    "with_food": "Có thể uống với hoặc không có thức ăn.",
                    "timing": "Uống 2-3 lần/ngày.",
                    "notes": "Điều chỉnh liều theo chức năng thận.",
                },
            },
        },

        "Cefdinir": {
            "contraindications": {
                "tuyệt_đối": ["Dị ứng cephalosporin hoặc beta-lactam"],
                "tương_đối": ["Dị ứng penicillin", "Suy thận nặng"],
            },
            "drug_interactions": {
                "major": [],
                "moderate": [
                    {"drug": "Probenecid", "mechanism": "Tăng nồng độ", "effect": "Tăng nồng độ", "management": "Có thể cần giảm liều."},
                    {"drug": "Warfarin", "mechanism": "Có thể tăng INR", "effect": "Tăng INR", "management": "Theo dõi INR."},
                    {"drug": "Antacid, sắt", "mechanism": "Giảm hấp thu", "effect": "Giảm hấp thu", "management": "Cách 2 giờ."},
                ],
                "minor": [],
            },
            "pregnancy_lactation": {
                "fda_category": "B",
                "pregnancy_details": "An toàn trong thai kỳ.",
                "lactation": {"safety": "Compatible", "details": "Bài tiết vào sữa mẹ ở nồng độ thấp.", "recommendation": "Có thể dùng khi cho con bú."},
            },
            "hepatic_adjustment": {"mild": "Không cần chỉnh liều.", "moderate": "Không cần chỉnh liều.", "severe": "Không cần chỉnh liều.", "notes": "Cefdinir không chuyển hóa qua gan, thải trừ chủ yếu qua thận."},
            "overdose_management": {
                "symptoms": ["Co giật (hiếm)", "Suy thận cấp (hiếm)"],
                "antidote": "Không có antidote đặc hiệu.",
                "treatment": ["Ngừng cefdinir", "Điều trị hỗ trợ"],
                "monitoring": "Chức năng thận, dấu hiệu dị ứng.",
            },
            "reversal_agents": {"available": False, "agents": [], "notes": "Không có thuốc giải độc đặc hiệu."},
            "administration_instructions": {
                "oral": {
                    "with_food": "Có thể uống với hoặc không có thức ăn.",
                    "timing": "Uống 1-2 lần/ngày.",
                    "notes": "Tránh antacid và sắt trong 2 giờ. Điều chỉnh liều theo chức năng thận.",
                },
            },
        },

        "Cefepime": {
            "contraindications": {
                "tuyệt_đối": ["Dị ứng cephalosporin hoặc beta-lactam"],
                "tương_đối": ["Dị ứng penicillin", "Suy thận nặng"],
            },
            "drug_interactions": {
                "major": [],
                "moderate": [
                    {"drug": "Probenecid", "mechanism": "Tăng nồng độ", "effect": "Tăng nồng độ", "management": "Có thể cần giảm liều."},
                    {"drug": "Warfarin", "mechanism": "Có thể tăng INR", "effect": "Tăng INR", "management": "Theo dõi INR."},
                ],
                "minor": [],
            },
            "pregnancy_lactation": {
                "fda_category": "B",
                "pregnancy_details": "An toàn trong thai kỳ.",
                "lactation": {"safety": "Compatible", "details": "Bài tiết vào sữa mẹ ở nồng độ thấp.", "recommendation": "Có thể dùng khi cho con bú."},
            },
            "hepatic_adjustment": {"mild": "Không cần chỉnh liều.", "moderate": "Không cần chỉnh liều.", "severe": "Không cần chỉnh liều.", "notes": "Cefepime không chuyển hóa qua gan, thải trừ chủ yếu qua thận."},
            "overdose_management": {
                "symptoms": ["Co giật (hiếm)", "Suy thận cấp (hiếm)"],
                "antidote": "Không có antidote đặc hiệu.",
                "treatment": ["Ngừng cefepime", "Điều trị hỗ trợ", "Hemodialysis nếu cần"],
                "monitoring": "Chức năng thận, dấu hiệu dị ứng, co giật.",
            },
            "reversal_agents": {"available": False, "agents": [], "notes": "Không có thuốc giải độc đặc hiệu."},
            "administration_instructions": {
                "iv": {
                    "reconstitution": "Pha trong NaCl 0.9% hoặc D5W.",
                    "infusion_rate": "Truyền trong 30 phút.",
                    "notes": "Điều chỉnh liều theo chức năng thận.",
                },
            },
        },

        "Cefixime": {
            "contraindications": {
                "tuyệt_đối": ["Dị ứng cephalosporin hoặc beta-lactam"],
                "tương_đối": ["Dị ứng penicillin", "Suy thận nặng"],
            },
            "drug_interactions": {
                "major": [],
                "moderate": [
                    {"drug": "Probenecid", "mechanism": "Tăng nồng độ", "effect": "Tăng nồng độ", "management": "Có thể cần giảm liều."},
                    {"drug": "Warfarin", "mechanism": "Có thể tăng INR", "effect": "Tăng INR", "management": "Theo dõi INR."},
                ],
                "minor": [],
            },
            "pregnancy_lactation": {
                "fda_category": "B",
                "pregnancy_details": "An toàn trong thai kỳ.",
                "lactation": {"safety": "Compatible", "details": "Bài tiết vào sữa mẹ ở nồng độ thấp.", "recommendation": "Có thể dùng khi cho con bú."},
            },
            "hepatic_adjustment": {"mild": "Không cần chỉnh liều.", "moderate": "Không cần chỉnh liều.", "severe": "Không cần chỉnh liều.", "notes": "Cefixime không chuyển hóa qua gan, thải trừ chủ yếu qua thận."},
            "overdose_management": {
                "symptoms": ["Co giật (hiếm)", "Suy thận cấp (hiếm)"],
                "antidote": "Không có antidote đặc hiệu.",
                "treatment": ["Ngừng cefixime", "Điều trị hỗ trợ"],
                "monitoring": "Chức năng thận, dấu hiệu dị ứng.",
            },
            "reversal_agents": {"available": False, "agents": [], "notes": "Không có thuốc giải độc đặc hiệu."},
            "administration_instructions": {
                "oral": {
                    "with_food": "Có thể uống với hoặc không có thức ăn.",
                    "timing": "Uống 1-2 lần/ngày.",
                    "notes": "Điều chỉnh liều theo chức năng thận.",
                },
            },
        },

        "Cefotaxime": {
            "contraindications": {
                "tuyệt_đối": ["Dị ứng cephalosporin hoặc beta-lactam"],
                "tương_đối": ["Dị ứng penicillin", "Suy thận nặng"],
            },
            "drug_interactions": {
                "major": [],
                "moderate": [
                    {"drug": "Probenecid", "mechanism": "Tăng nồng độ", "effect": "Tăng nồng độ", "management": "Có thể cần giảm liều."},
                    {"drug": "Warfarin", "mechanism": "Có thể tăng INR", "effect": "Tăng INR", "management": "Theo dõi INR."},
                ],
                "minor": [],
            },
            "pregnancy_lactation": {
                "fda_category": "B",
                "pregnancy_details": "An toàn trong thai kỳ.",
                "lactation": {"safety": "Compatible", "details": "Bài tiết vào sữa mẹ ở nồng độ thấp.", "recommendation": "Có thể dùng khi cho con bú."},
            },
            "hepatic_adjustment": {"mild": "Không cần chỉnh liều.", "moderate": "Không cần chỉnh liều.", "severe": "Không cần chỉnh liều.", "notes": "Cefotaxime không chuyển hóa qua gan, thải trừ chủ yếu qua thận."},
            "overdose_management": {
                "symptoms": ["Co giật (hiếm)", "Suy thận cấp (hiếm)"],
                "antidote": "Không có antidote đặc hiệu.",
                "treatment": ["Ngừng cefotaxime", "Điều trị hỗ trợ", "Hemodialysis nếu cần"],
                "monitoring": "Chức năng thận, dấu hiệu dị ứng, co giật.",
            },
            "reversal_agents": {"available": False, "agents": [], "notes": "Không có thuốc giải độc đặc hiệu."},
            "administration_instructions": {
                "iv": {
                    "reconstitution": "Pha trong NaCl 0.9% hoặc D5W.",
                    "infusion_rate": "Truyền trong 30 phút.",
                    "notes": "Điều chỉnh liều theo chức năng thận.",
                },
            },
        },

        "Ceftazidime": {
            "contraindications": {
                "tuyệt_đối": ["Dị ứng cephalosporin hoặc beta-lactam"],
                "tương_đối": ["Dị ứng penicillin", "Suy thận nặng"],
            },
            "drug_interactions": {
                "major": [],
                "moderate": [
                    {"drug": "Probenecid", "mechanism": "Tăng nồng độ", "effect": "Tăng nồng độ", "management": "Có thể cần giảm liều."},
                    {"drug": "Warfarin", "mechanism": "Có thể tăng INR", "effect": "Tăng INR", "management": "Theo dõi INR."},
                ],
                "minor": [],
            },
            "pregnancy_lactation": {
                "fda_category": "B",
                "pregnancy_details": "An toàn trong thai kỳ.",
                "lactation": {"safety": "Compatible", "details": "Bài tiết vào sữa mẹ ở nồng độ thấp.", "recommendation": "Có thể dùng khi cho con bú."},
            },
            "hepatic_adjustment": {"mild": "Không cần chỉnh liều.", "moderate": "Không cần chỉnh liều.", "severe": "Không cần chỉnh liều.", "notes": "Ceftazidime không chuyển hóa qua gan, thải trừ chủ yếu qua thận."},
            "overdose_management": {
                "symptoms": ["Co giật (hiếm)", "Suy thận cấp (hiếm)"],
                "antidote": "Không có antidote đặc hiệu.",
                "treatment": ["Ngừng ceftazidime", "Điều trị hỗ trợ", "Hemodialysis nếu cần"],
                "monitoring": "Chức năng thận, dấu hiệu dị ứng, co giật.",
            },
            "reversal_agents": {"available": False, "agents": [], "notes": "Không có thuốc giải độc đặc hiệu."},
            "administration_instructions": {
                "iv": {
                    "reconstitution": "Pha trong NaCl 0.9% hoặc D5W.",
                    "infusion_rate": "Truyền trong 30 phút.",
                    "notes": "Điều chỉnh liều theo chức năng thận. Có thể dùng với calcium (khác ceftriaxone).",
                },
            },
        },

        "Amoxicillin": {
            "pregnancy_lactation": {
                "fda_category": "B",
                "pregnancy_details": (
                    "Được xem là an toàn khi sử dụng trong thai kỳ. Không có bằng chứng về quái thai hoặc độc tính lên thai nhi "
                    "trong các nghiên cứu trên động vật và người."
                ),
                "lactation": {
                    "safety": "Compatible",
                    "details": "Bài tiết vào sữa mẹ với lượng nhỏ. Có thể gây tiêu chảy hoặc phát ban nhẹ ở trẻ, nhưng thường an toàn.",
                    "recommendation": "Có thể sử dụng. Theo dõi trẻ về tiêu chảy hoặc nấm miệng (tưa miệng).",
                },
            },
            "hepatic_adjustment": {
                "mild": "Không cần chỉnh liều.",
                "moderate": "Không cần chỉnh liều.",
                "severe": "Không cần chỉnh liều.",
                "notes": "Chuyển hóa gan thấp; thải trừ chủ yếu qua thận.",
            },
        },

        # ======================== ANTIBIOTICS: BETA-LACTAMS (Penicillins) ==========
        "Dicloxacillin": {
            "contraindications": {
                "tuyệt_đối": ["Dị ứng penicillin hoặc beta-lactam"],
                "tương_đối": ["Dị ứng cephalosporin (phản ứng chéo)", "Suy thận nặng"],
            },
            "drug_interactions": {
                "major": [],
                "moderate": [
                    {"drug": "Probenecid", "mechanism": "Tăng nồng độ", "effect": "Tăng nồng độ", "management": "Có thể cần giảm liều."},
                    {"drug": "Warfarin", "mechanism": "Có thể tăng INR", "effect": "Tăng INR", "management": "Theo dõi INR."},
                ],
                "minor": [],
            },
            "pregnancy_lactation": {
                "fda_category": "B",
                "pregnancy_details": "An toàn trong thai kỳ.",
                "lactation": {"safety": "Compatible", "details": "Bài tiết vào sữa mẹ ở nồng độ thấp.", "recommendation": "Có thể dùng khi cho con bú."},
            },
            "hepatic_adjustment": {"mild": "Không cần chỉnh liều.", "moderate": "Không cần chỉnh liều.", "severe": "Không cần chỉnh liều.", "notes": "Dicloxacillin không chuyển hóa qua gan, thải trừ chủ yếu qua thận."},
            "overdose_management": {
                "symptoms": ["Co giật (hiếm)", "Suy thận cấp (hiếm)"],
                "antidote": "Không có antidote đặc hiệu.",
                "treatment": ["Ngừng dicloxacillin", "Điều trị hỗ trợ"],
                "monitoring": "Chức năng thận, dấu hiệu dị ứng.",
            },
            "reversal_agents": {"available": False, "agents": [], "notes": "Không có thuốc giải độc đặc hiệu."},
            "administration_instructions": {
                "oral": {
                    "with_food": "Uống với thức ăn để giảm kích ứng dạ dày.",
                    "timing": "Uống 4 lần/ngày.",
                    "notes": "Điều chỉnh liều theo chức năng thận.",
                },
            },
        },

        "Nafcillin": {
            "contraindications": {
                "tuyệt_đối": ["Dị ứng penicillin hoặc beta-lactam"],
                "tương_đối": ["Dị ứng cephalosporin", "Suy gan nặng"],
            },
            "drug_interactions": {
                "major": [],
                "moderate": [
                    {"drug": "Warfarin", "mechanism": "Có thể tăng INR", "effect": "Tăng INR", "management": "Theo dõi INR."},
                ],
                "minor": [],
            },
            "pregnancy_lactation": {
                "fda_category": "B",
                "pregnancy_details": "An toàn trong thai kỳ.",
                "lactation": {"safety": "Compatible", "details": "Bài tiết vào sữa mẹ ở nồng độ thấp.", "recommendation": "Có thể dùng khi cho con bú."},
            },
            "hepatic_adjustment": {
                "mild": "Không cần chỉnh liều.",
                "moderate": "Thận trọng (thải trừ qua mật).",
                "severe": "Thận trọng, có thể cần giảm liều.",
                "notes": "Nafcillin thải trừ chủ yếu qua mật, không cần điều chỉnh thận.",
            },
            "overdose_management": {
                "symptoms": ["Co giật (hiếm)", "Suy gan cấp (hiếm)"],
                "antidote": "Không có antidote đặc hiệu.",
                "treatment": ["Ngừng nafcillin", "Điều trị hỗ trợ"],
                "monitoring": "Chức năng gan, dấu hiệu dị ứng.",
            },
            "reversal_agents": {"available": False, "agents": [], "notes": "Không có thuốc giải độc đặc hiệu."},
            "administration_instructions": {
                "iv": {
                    "reconstitution": "Pha trong NaCl 0.9% hoặc D5W.",
                    "infusion_rate": "Truyền trong 30-60 phút.",
                    "notes": "Thải trừ qua mật, không cần điều chỉnh thận.",
                },
            },
        },

        "Oxacillin": {
            "contraindications": {
                "tuyệt_đối": ["Dị ứng penicillin hoặc beta-lactam"],
                "tương_đối": ["Dị ứng cephalosporin", "Suy gan nặng"],
            },
            "drug_interactions": {
                "major": [],
                "moderate": [
                    {"drug": "Warfarin", "mechanism": "Có thể tăng INR", "effect": "Tăng INR", "management": "Theo dõi INR."},
                ],
                "minor": [],
            },
            "pregnancy_lactation": {
                "fda_category": "B",
                "pregnancy_details": "An toàn trong thai kỳ.",
                "lactation": {"safety": "Compatible", "details": "Bài tiết vào sữa mẹ ở nồng độ thấp.", "recommendation": "Có thể dùng khi cho con bú."},
            },
            "hepatic_adjustment": {
                "mild": "Không cần chỉnh liều.",
                "moderate": "Thận trọng (thải trừ qua mật).",
                "severe": "Thận trọng, có thể cần giảm liều.",
                "notes": "Oxacillin thải trừ chủ yếu qua mật, không cần điều chỉnh thận.",
            },
            "overdose_management": {
                "symptoms": ["Co giật (hiếm)", "Suy gan cấp (hiếm)"],
                "antidote": "Không có antidote đặc hiệu.",
                "treatment": ["Ngừng oxacillin", "Điều trị hỗ trợ"],
                "monitoring": "Chức năng gan, dấu hiệu dị ứng.",
            },
            "reversal_agents": {"available": False, "agents": [], "notes": "Không có thuốc giải độc đặc hiệu."},
            "administration_instructions": {
                "iv": {
                    "reconstitution": "Pha trong NaCl 0.9% hoặc D5W.",
                    "infusion_rate": "Truyền trong 30-60 phút.",
                    "notes": "Thải trừ qua mật, không cần điều chỉnh thận.",
                },
            },
        },

        # ======================== ANTIBIOTICS: TETRACYCLINES =======================
        "Tigecycline": {
            "contraindications": {
                "tuyệt_đối": ["Dị ứng tigecycline hoặc tetracycline"],
                "tương_đối": ["Có thai (category D)", "Trẻ <8 tuổi", "Suy gan nặng"],
            },
            "pregnancy_lactation": {
                "fda_category": "D",
                "pregnancy_details": "CHỐNG CHỈ ĐỊNH trong thai kỳ. Gây độc thai nhi, đặc biệt răng và xương.",
                "lactation": {"safety": "Caution", "details": "Bài tiết vào sữa mẹ. Có thể gây độc tính ở trẻ.", "recommendation": "Thận trọng khi cho con bú. Cân nhắc ngừng cho bú tạm thời."},
            },
            "hepatic_adjustment": {
                "mild": "Không cần chỉnh liều.",
                "moderate": "Giảm liều khởi đầu 50%.",
                "severe": "CHỐNG CHỈ ĐỊNH hoặc giảm liều mạnh.",
                "notes": "Tigecycline chuyển hóa qua gan. Suy gan làm tăng nồng độ đáng kể.",
            },
            "overdose_management": {
                "symptoms": ["Buồn nôn, nôn", "Tăng men gan", "Viêm tụy (hiếm)"],
                "antidote": "Không có antidote đặc hiệu.",
                "treatment": ["Ngừng tigecycline", "Điều trị hỗ trợ", "Theo dõi chức năng gan"],
                "monitoring": "Chức năng gan, dấu hiệu viêm tụy.",
            },
            "reversal_agents": {"available": False, "agents": [], "notes": "Không có thuốc giải độc đặc hiệu."},
            "administration_instructions": {
                "iv": {
                    "reconstitution": "Pha trong NaCl 0.9% hoặc D5W.",
                    "infusion_rate": "Truyền IV trong 60 phút.",
                    "notes": "Điều chỉnh liều theo chức năng gan. CHỐNG CHỈ ĐỊNH trong thai kỳ và trẻ <8 tuổi.",
                },
            },
        },

        # ======================== ANTIBIOTICS – AMINOGLYCOSIDES & VANCOMYCIN ========================
        "5-Fluorouracil": {
            "availability_vietnam": {
                "status": "common",
                "level_of_care": ["provincial", "central"],
                "insurance_coverage": "bhyt_full",
                "brand_examples": ["5-FU injection"],
                "notes": "Có mặt rộng rãi tại các trung tâm ung bướu cho điều trị ung thư đường tiêu hoá và các phác đồ khác.",
            },
        },

        "Carboplatin": {
            "availability_vietnam": {
                "status": "common",
                "level_of_care": ["provincial", "central"],
                "insurance_coverage": "bhyt_full",
                "brand_examples": ["Carboplatin injection"],
                "notes": "Dùng trong nhiều phác đồ hóa trị; thường sẵn có tại khoa ung bướu.",
            },
        },

        "Cisplatin": {
            "availability_vietnam": {
                "status": "common",
                "level_of_care": ["provincial", "central"],
                "insurance_coverage": "bhyt_full",
                "brand_examples": ["Cisplatin injection"],
                "notes": "Thuốc hoá trị nền tảng cho nhiều loại ung thư; cần monitor thận, điện giải và buồn nôn/nôn.",
            },
        },

        "Cyclophosphamide": {
            "availability_vietnam": {
                "status": "common",
                "level_of_care": ["provincial", "central"],
                "insurance_coverage": "bhyt_full",
                "brand_examples": ["Cyclophosphamide injection", "Cyclophosphamide tablets"],
                "notes": "Dùng trong ung thư và bệnh lý tự miễn; có ở các trung tâm lớn.",
            },
        },

        "Ifosfamide": {
            "availability_vietnam": {
                "status": "limited",
                "level_of_care": ["central"],
                "insurance_coverage": "bhyt_partial",
                "brand_examples": ["Ifosfamide injection"],
                "notes": "Thường chỉ có tại trung tâm ung bướu tuyến cuối; cần theo dõi chặt độc tính thần kinh và bàng quang.",
            },
        },

        "Doxorubicin": {
            "availability_vietnam": {
                "status": "common",
                "level_of_care": ["provincial", "central"],
                "insurance_coverage": "bhyt_full",
                "brand_examples": ["Doxorubicin injection"],
                "notes": "Hóa chất chính trong nhiều phác đồ (ví dụ CHOP); cần monitor độc tính tim và tuỷ xương.",
            },
        },

        "Docetaxel": {
            "availability_vietnam": {
                "status": "common",
                "level_of_care": ["provincial", "central"],
                "insurance_coverage": "bhyt_full",
                "brand_examples": ["Taxotere"],
                "notes": "Dùng trong ung thư vú, phổi và một số ung thư khác; thường có tại các trung tâm ung bướu.",
            },
        },

        "Paclitaxel": {
            "availability_vietnam": {
                "status": "common",
                "level_of_care": ["provincial", "central"],
                "insurance_coverage": "bhyt_full",
                "brand_examples": ["Paclitaxel injection"],
                "notes": "Thuốc chuẩn trong nhiều phác đồ; cần chuẩn bị phòng sốc phản vệ do thuốc.",
            },
        },

        "Gemcitabine": {
            "availability_vietnam": {
                "status": "common",
                "level_of_care": ["provincial", "central"],
                "insurance_coverage": "bhyt_full",
                "brand_examples": ["Gemcitabine injection"],
                "notes": "Dùng trong ung thư tụy, phổi, bàng quang...; phổ biến ở trung tâm ung thư.",
            },
        },

        "Irinotecan": {
            "availability_vietnam": {
                "status": "common",
                "level_of_care": ["provincial", "central"],
                "insurance_coverage": "bhyt_full",
                "brand_examples": ["Irinotecan injection"],
                "notes": "Thường dùng trong phác đồ ung thư đại trực tràng; cần theo dõi tiêu chảy và suy tuỷ.",
            },
        },

        "Azathioprine": {
            "availability_vietnam": {
                "status": "common",
                "level_of_care": ["provincial", "central"],
                "insurance_coverage": "bhyt_full",
                "brand_examples": ["Azathioprine tablets"],
                "notes": "Dùng trong ghép tạng và bệnh tự miễn; thường có tại khoa nội miễn dịch/thận.",
            },
        },

        "Cyclosporine": {
            "availability_vietnam": {
                "status": "common",
                "level_of_care": ["provincial", "central"],
                "insurance_coverage": "bhyt_full",
                "brand_examples": ["Sandimmun", "Cyclosporine STADA"],
                "notes": "Thuốc nền tảng trong ghép tạng và một số bệnh tự miễn; cần monitor nồng độ thuốc và chức năng thận.",
            },
        },

        "Tacrolimus": {
            "availability_vietnam": {
                "status": "common",
                "level_of_care": ["central"],
                "insurance_coverage": "bhyt_full",
                "brand_examples": ["Prograf", "Advagraf"],
                "notes": "Chủ yếu dùng tại trung tâm ghép tạng; yêu cầu monitor nồng độ thuốc và độc tính thận/gan.",
            },
        },

        "Mycophenolate": {
            "availability_vietnam": {
                "status": "common",
                "level_of_care": ["central"],
                "insurance_coverage": "bhyt_full",
                "brand_examples": ["Cellcept", "Myfortic"],
                "notes": "Dùng rộng rãi trong ghép tạng và bệnh tự miễn khó trị; thường ở bệnh viện tuyến cuối.",
            },
        },

        "Carbamazepine": {
            "availability_vietnam": {
                "status": "common",
                "level_of_care": ["district", "provincial", "central"],
                "insurance_coverage": "bhyt_full",
                "brand_examples": ["Tegretol", "Carbamazepine STADA"],
                "notes": "Thuốc kinh điển điều trị động kinh và đau dây V; dễ tiếp cận.",
            },
        },

        "Phenytoin": {
            "availability_vietnam": {
                "status": "common",
                "level_of_care": ["district", "provincial", "central"],
                "insurance_coverage": "bhyt_full",
                "brand_examples": ["Dilantin", "Phenytoin STADA"],
                "notes": "Dùng trong động kinh và điều trị cơn co giật cấp; có cả dạng PO và IV.",
            },
        },

        "Valproate": {
            "availability_vietnam": {
                "status": "common",
                "level_of_care": ["district", "provincial", "central"],
                "insurance_coverage": "bhyt_full",
                "brand_examples": ["Depakine", "Sodium Valproate STADA"],
                "notes": "Thuốc phổ biến điều trị động kinh và rối loạn khí sắc; cần monitor men gan và tiểu cầu.",
            },
        },

        "Phenobarbital": {
            "availability_vietnam": {
                "status": "common",
                "level_of_care": ["district", "provincial", "central"],
                "insurance_coverage": "bhyt_full",
                "brand_examples": ["Phenobarbital tablets/injection"],
                "notes": "Được sử dụng nhiều ở tuyến cơ sở cho động kinh; chi phí rẻ nhưng nhiều tác dụng phụ.",
            },
        },

        "Ethosuximide": {
            "availability_vietnam": {
                "status": "limited",
                "level_of_care": ["central"],
                "insurance_coverage": "bhyt_partial",
                "brand_examples": [],
                "notes": "Chủ yếu dùng cho co giật vắng ý thức; thường chỉ có tại trung tâm thần kinh/nhi khoa lớn.",
            },
        },

        "Topiramate": {
            "availability_vietnam": {
                "status": "common",
                "level_of_care": ["provincial", "central"],
                "insurance_coverage": "bhyt_full",
                "brand_examples": ["Topamax"],
                "notes": "Dùng cho động kinh và dự phòng migraine; thường có ở bệnh viện tuyến trên.",
            },
        },

        "Lamotrigine": {
            "availability_vietnam": {
                "status": "limited",
                "level_of_care": ["provincial", "central"],
                "insurance_coverage": "bhyt_partial",
                "brand_examples": ["Lamictal"],
                "notes": "Có tại một số bệnh viện lớn; cần khởi liều chậm để tránh hội chứng Stevens–Johnson.",
            },
        },

        "Levetiracetam": {
            "availability_vietnam": {
                "status": "common",
                "level_of_care": ["provincial", "central"],
                "insurance_coverage": "bhyt_full",
                "brand_examples": ["Keppra"],
                "notes": "Được sử dụng ngày càng nhiều do profile an toàn tốt; có cả dạng PO và IV.",
            },
        },

        "Lacosamide": {
            "availability_vietnam": {
                "status": "limited",
                "level_of_care": ["central"],
                "insurance_coverage": "bhyt_partial",
                "brand_examples": ["Vimpat"],
                "notes": "Thường chỉ có tại trung tâm động kinh/chuyên khoa thần kinh tuyến cuối.",
            },
        },

        "Zonisamide": {
            "availability_vietnam": {
                "status": "rare",
                "level_of_care": ["central"],
                "insurance_coverage": "no_bhyt",
                "brand_examples": [],
                "notes": "Thuốc mới hơn; chỉ có ở một số ít trung tâm động kinh, chủ yếu dạng nhập khẩu.",
            },
        },

        "Perampanel": {
            "availability_vietnam": {
                "status": "rare",
                "level_of_care": ["central"],
                "insurance_coverage": "no_bhyt",
                "brand_examples": [],
                "notes": "Thuốc chống động kinh thế hệ mới; hiện diện hạn chế tại Việt Nam.",
            },
        },

        "Oxcarbazepine": {
            "availability_vietnam": {
                "status": "limited",
                "level_of_care": ["provincial", "central"],
                "insurance_coverage": "bhyt_partial",
                "brand_examples": ["Trileptal"],
                "notes": "Thường có ở bệnh viện tuyến trên; dùng thay thế carbamazepine trong một số trường hợp.",
            },
        },

        "Gabapentin": {
            "availability_vietnam": {
                "status": "common",
                "level_of_care": ["provincial", "central"],
                "insurance_coverage": "bhyt_full",
                "brand_examples": ["Neurontin", "Gabapentin STADA"],
                "notes": "Dùng trong đau thần kinh và động kinh; khá phổ biến.",
            },
        },

        "Pregabalin": {
            "availability_vietnam": {
                "status": "common",
                "level_of_care": ["provincial", "central", "private"],
                "insurance_coverage": "bhyt_partial",
                "brand_examples": ["Lyrica"],
                "notes": "Được dùng nhiều cho đau thần kinh; phổ biến tại cơ sở tư nhân và bệnh viện tuyến trên.",
            },
        },

        "Primidone": {
            "availability_vietnam": {
                "status": "rare",
                "level_of_care": ["central"],
                "insurance_coverage": "no_bhyt",
                "brand_examples": [],
                "notes": "Ít gặp; nếu có thường ở trung tâm thần kinh/chuyên khoa.",
            },
        },

        "Theophylline": {
            "availability_vietnam": {
                "status": "common",
                "level_of_care": ["district", "provincial", "central"],
                "insurance_coverage": "bhyt_full",
                "brand_examples": ["Theophylline retard", "Aminophylline injection"],
                "notes": "Vẫn được sử dụng trong hen/COPD ở một số nơi; cần lưu ý khoảng điều trị hẹp và tương tác thuốc.",
            },
        },

    # ======================== BATCH 3: ANTIBIOTICS ========================
        "Cefazolin": {
            "contraindications_detail": {
                "tuyệt_đối": [
                    "Dị ứng với cefazolin hoặc cephalosporin",
                    "Tiền sử phản ứng phản vệ với beta-lactam",
                ],
                "tương_đối": [
                    "Dị ứng với penicillin - thận trọng (phản ứng chéo 5-10%)",
                    "Suy thận nặng (CrCl <30) - giảm liều",
                    "Có thai - thận trọng",
                    "Đang cho con bú - thận trọng",
                ],
            },
            "risk_flags": {
                "high_alert": False,
                "narrow_therapeutic_index": False,
                "icu_critical_care_only": False,
                "bleeding_risk": False,
                "organ_toxicity": {"renal": "Low (with high doses or prolonged use)"},
                "qt_prolongation": False,
                "hepatotoxicity": False,
                "nephrotoxicity": False,
                "requires_monitoring": [
                    "Renal function (CrCl) - adjust dose if CrCl <30",
                    "Signs of allergic reaction (rash, anaphylaxis)",
                    "Complete blood count (if prolonged use)"
                ],
                "look_alike_sound_alike": ["Cefazolin", "Cefuroxime", "Ceftriaxone"]
            },
            "guideline_tags": [
                "IDSA Surgical Site Infection Prevention Guidelines",
                "ASHP Guidelines - Surgical Prophylaxis",
                "AHA/ACC Infective Endocarditis Prophylaxis Guidelines",
                "FDA Drug Label - Cefazolin"
            ]
        },

        # ======================== PRIORITY ANTIBIOTICS - RISK FLAGS & GUIDELINE TAGS ========================
        "Amoxicillin": {
            "risk_flags": {
                "high_alert": False,
                "narrow_therapeutic_index": False,
                "icu_critical_care_only": False,
                "bleeding_risk": False,
                "organ_toxicity": {"hepatic": "Low (rare)"},
                "qt_prolongation": False,
                "hepatotoxicity": False,
                "nephrotoxicity": False,
                "requires_monitoring": [
                    "Signs of allergic reaction (rash, anaphylaxis) - CRITICAL",
                    "Diarrhea (C. difficile risk)",
                    "Renal function (if high doses or prolonged use)"
                ],
                "look_alike_sound_alike": ["Amoxicillin", "Ampicillin", "Amoxicillin-clavulanate"]
            },
            "guideline_tags": [
                "IDSA Community-Acquired Pneumonia Guidelines",
                "IDSA Acute Otitis Media Guidelines",
                "IDSA Sinusitis Guidelines",
                "WHO Guidelines - Common Infections",
                "FDA Drug Label - Amoxicillin"
            ]
        },

        "Ceftriaxone": {
            "risk_flags": {
                "high_alert": False,
                "narrow_therapeutic_index": False,
                "icu_critical_care_only": False,
                "bleeding_risk": "Moderate (can cause hypoprothrombinemia, especially with vitamin K deficiency)",
                "organ_toxicity": {"hepatic": "Low", "renal": "Low"},
                "qt_prolongation": False,
                "hepatotoxicity": False,
                "nephrotoxicity": False,
                "requires_monitoring": [
                    "Signs of allergic reaction (rash, anaphylaxis)",
                    "PT/INR (bleeding risk, especially in malnourished patients)",
                    "Complete blood count",
                    "Renal function (CrCl) - adjust dose if CrCl <10",
                    "Biliary sludge/pseudolithiasis (especially in children)"
                ],
                "look_alike_sound_alike": ["Ceftriaxone", "Ceftazidime", "Cefotaxime"]
            },
            "guideline_tags": [
                "IDSA Community-Acquired Pneumonia Guidelines",
                "IDSA Meningitis Guidelines",
                "IDSA Gonorrhea Treatment Guidelines",
                "WHO Guidelines - Sexually Transmitted Infections",
                "FDA Drug Label - Ceftriaxone"
            ]
        },

        "Azithromycin": {
            "risk_flags": {
                "high_alert": False,
                "narrow_therapeutic_index": False,
                "icu_critical_care_only": False,
                "bleeding_risk": False,
                "organ_toxicity": {"hepatic": "Low", "cardiac": "Moderate (QT prolongation)"},
                "qt_prolongation": True,
                "hepatotoxicity": False,
                "nephrotoxicity": False,
                "requires_monitoring": [
                    "ECG (QT prolongation risk, especially with other QT-prolonging drugs)",
                    "Signs of allergic reaction",
                    "Hepatic function (if prolonged use)",
                    "Hearing loss (rare, with high doses or prolonged use)"
                ],
                "look_alike_sound_alike": ["Azithromycin", "Clarithromycin", "Erythromycin"]
            },
            "guideline_tags": [
                "IDSA Community-Acquired Pneumonia Guidelines",
                "IDSA Acute Otitis Media Guidelines",
                "IDSA Sexually Transmitted Infections Guidelines",
                "AHA/ACC Infective Endocarditis Prophylaxis Guidelines",
                "FDA Drug Label - Azithromycin (QT prolongation warning)"
            ]
        },

        "Ciprofloxacin": {
            "risk_flags": {
                "high_alert": False,
                "narrow_therapeutic_index": False,
                "icu_critical_care_only": False,
                "bleeding_risk": False,
                "organ_toxicity": {"tendon": "Moderate (tendonitis, tendon rupture)", "cardiac": "Moderate (QT prolongation)", "hepatic": "Low"},
                "qt_prolongation": True,
                "hepatotoxicity": False,
                "nephrotoxicity": False,
                "requires_monitoring": [
                    "ECG (QT prolongation risk)",
                    "Signs of tendonitis/tendon rupture (especially Achilles tendon)",
                    "Signs of peripheral neuropathy",
                    "Signs of CNS effects (seizures, confusion)",
                    "Hepatic function (if prolonged use)"
                ],
                "look_alike_sound_alike": ["Ciprofloxacin", "Levofloxacin", "Moxifloxacin"]
            },
            "guideline_tags": [
                "FDA Black Box Warning - Tendonitis and Tendon Rupture",
                "FDA Black Box Warning - Peripheral Neuropathy",
                "IDSA Urinary Tract Infection Guidelines",
                "IDSA Complicated Intra-abdominal Infection Guidelines",
                "WHO Guidelines - Antimicrobial Resistance"
            ]
        },

        "Metronidazole": {
            "risk_flags": {
                "high_alert": False,
                "narrow_therapeutic_index": False,
                "icu_critical_care_only": False,
                "bleeding_risk": False,
                "organ_toxicity": {"neurologic": "Moderate (peripheral neuropathy, encephalopathy)", "hepatic": "Low"},
                "qt_prolongation": False,
                "hepatotoxicity": False,
                "nephrotoxicity": False,
                "requires_monitoring": [
                    "Signs of peripheral neuropathy (numbness, tingling)",
                    "Signs of CNS effects (seizures, encephalopathy)",
                    "Complete blood count (leukopenia, thrombocytopenia)",
                    "Hepatic function (if prolonged use)",
                    "Disulfiram-like reaction (if alcohol consumed)"
                ],
                "look_alike_sound_alike": ["Metronidazole", "Mebendazole"]
            },
            "guideline_tags": [
                "IDSA Clostridium difficile Infection Guidelines",
                "IDSA Complicated Intra-abdominal Infection Guidelines",
                "IDSA Bacterial Vaginosis Guidelines",
                "WHO Guidelines - Anaerobic Infections",
                "FDA Drug Label - Metronidazole (alcohol interaction warning)"
            ]
        },

        "Doxycycline": {
            "risk_flags": {
                "high_alert": False,
                "narrow_therapeutic_index": False,
                "icu_critical_care_only": False,
                "bleeding_risk": False,
                "organ_toxicity": {"hepatic": "Low", "esophageal": "Moderate (esophagitis, ulceration)"},
                "qt_prolongation": False,
                "hepatotoxicity": False,
                "nephrotoxicity": False,
                "requires_monitoring": [
                    "Signs of photosensitivity (sunburn, rash)",
                    "Signs of esophageal irritation (take with plenty of water, avoid lying down)",
                    "Hepatic function (if prolonged use)",
                    "Intracranial hypertension (headache, vision changes) - rare"
                ],
                "look_alike_sound_alike": ["Doxycycline", "Tetracycline", "Minocycline"]
            },
            "guideline_tags": [
                "IDSA Community-Acquired Pneumonia Guidelines",
                "IDSA Tick-borne Disease Guidelines (Lyme, Rickettsia)",
                "IDSA Sexually Transmitted Infections Guidelines",
                "WHO Guidelines - Malaria Prophylaxis",
                "FDA Drug Label - Doxycycline (photosensitivity warning)"
            ]
        },

        "Ampicillin": {
            "risk_flags": {
                "high_alert": False,
                "narrow_therapeutic_index": False,
                "icu_critical_care_only": False,
                "bleeding_risk": False,
                "organ_toxicity": {"hepatic": "Low"},
                "qt_prolongation": False,
                "hepatotoxicity": False,
                "nephrotoxicity": False,
                "requires_monitoring": [
                    "Signs of allergic reaction (rash, anaphylaxis) - CRITICAL",
                    "Diarrhea (C. difficile risk)",
                    "Complete blood count (if prolonged use)"
                ],
                "look_alike_sound_alike": ["Ampicillin", "Amoxicillin", "Ampicillin-sulbactam"]
            },
            "guideline_tags": [
                "IDSA Meningitis Guidelines",
                "IDSA Endocarditis Guidelines",
                "WHO Guidelines - Common Infections",
                "FDA Drug Label - Ampicillin"
            ]
        },

        "Cefepime": {
            "risk_flags": {
                "high_alert": False,
                "narrow_therapeutic_index": False,
                "icu_critical_care_only": False,
                "bleeding_risk": False,
                "organ_toxicity": {"renal": "Low", "neurologic": "Moderate (neurotoxicity, especially in renal impairment)"},
                "qt_prolongation": False,
                "hepatotoxicity": False,
                "nephrotoxicity": False,
                "requires_monitoring": [
                    "Signs of allergic reaction",
                    "Neurologic symptoms (seizures, confusion, myoclonus) - especially if CrCl <60",
                    "Renal function (CrCl) - adjust dose if CrCl <60",
                    "Complete blood count"
                ],
                "look_alike_sound_alike": ["Cefepime", "Ceftazidime", "Cefpirome"]
            },
            "guideline_tags": [
                "IDSA Healthcare-Associated Pneumonia Guidelines",
                "IDSA Febrile Neutropenia Guidelines",
                "IDSA Complicated Urinary Tract Infection Guidelines",
                "FDA Drug Label - Cefepime (neurotoxicity warning)"
            ]
        },

        "Ceftazidime": {
            "risk_flags": {
                "high_alert": False,
                "narrow_therapeutic_index": False,
                "icu_critical_care_only": False,
                "bleeding_risk": False,
                "organ_toxicity": {"renal": "Low"},
                "qt_prolongation": False,
                "hepatotoxicity": False,
                "nephrotoxicity": False,
                "requires_monitoring": [
                    "Signs of allergic reaction",
                    "Renal function (CrCl) - adjust dose if CrCl <50",
                    "Complete blood count"
                ],
                "look_alike_sound_alike": ["Ceftazidime", "Ceftriaxone", "Cefepime"]
            },
            "guideline_tags": [
                "IDSA Healthcare-Associated Pneumonia Guidelines",
                "IDSA Complicated Urinary Tract Infection Guidelines",
                "IDSA Pseudomonas aeruginosa Infection Guidelines",
                "FDA Drug Label - Ceftazidime"
            ]
        },

        "Clarithromycin": {
            "risk_flags": {
                "high_alert": False,
                "narrow_therapeutic_index": False,
                "icu_critical_care_only": False,
                "bleeding_risk": False,
                "organ_toxicity": {"hepatic": "Low", "cardiac": "Moderate (QT prolongation)"},
                "qt_prolongation": True,
                "hepatotoxicity": False,
                "nephrotoxicity": False,
                "requires_monitoring": [
                    "ECG (QT prolongation risk, especially with other QT-prolonging drugs)",
                    "Signs of allergic reaction",
                    "Hepatic function (if prolonged use)",
                    "Hearing loss (rare, with high doses)"
                ],
                "look_alike_sound_alike": ["Clarithromycin", "Azithromycin", "Erythromycin"]
            },
            "guideline_tags": [
                "IDSA Community-Acquired Pneumonia Guidelines",
                "IDSA Helicobacter pylori Treatment Guidelines",
                "AHA/ACC Infective Endocarditis Prophylaxis Guidelines",
                "FDA Drug Label - Clarithromycin (QT prolongation warning)"
            ]
        },

        "Erythromycin": {
            "risk_flags": {
                "high_alert": False,
                "narrow_therapeutic_index": False,
                "icu_critical_care_only": False,
                "bleeding_risk": False,
                "organ_toxicity": {"hepatic": "Moderate (cholestatic hepatitis)", "cardiac": "Moderate (QT prolongation)"},
                "qt_prolongation": True,
                "hepatotoxicity": True,
                "nephrotoxicity": False,
                "requires_monitoring": [
                    "ECG (QT prolongation risk)",
                    "Hepatic function (cholestatic hepatitis risk)",
                    "Signs of allergic reaction",
                    "Hearing loss (rare, with high doses)"
                ],
                "look_alike_sound_alike": ["Erythromycin", "Azithromycin", "Clarithromycin"]
            },
            "guideline_tags": [
                "IDSA Community-Acquired Pneumonia Guidelines",
                "AHA/ACC Infective Endocarditis Prophylaxis Guidelines",
                "FDA Drug Label - Erythromycin (QT prolongation and hepatotoxicity warnings)"
            ]
        },

        "Tetracycline": {
            "risk_flags": {
                "high_alert": False,
                "narrow_therapeutic_index": False,
                "icu_critical_care_only": False,
                "bleeding_risk": False,
                "organ_toxicity": {"hepatic": "Low", "renal": "Moderate (worsens renal function)", "esophageal": "Moderate"},
                "qt_prolongation": False,
                "hepatotoxicity": False,
                "nephrotoxicity": True,
                "requires_monitoring": [
                    "Renal function (contraindicated in renal impairment)",
                    "Signs of photosensitivity",
                    "Signs of esophageal irritation",
                    "Hepatic function (if prolonged use)"
                ],
                "look_alike_sound_alike": ["Tetracycline", "Doxycycline", "Minocycline"]
            },
            "guideline_tags": [
                "IDSA Acne Treatment Guidelines",
                "IDSA Sexually Transmitted Infections Guidelines",
                "FDA Drug Label - Tetracycline (renal impairment and photosensitivity warnings)"
            ]
        },

        "Minocycline": {
            "risk_flags": {
                "high_alert": False,
                "narrow_therapeutic_index": False,
                "icu_critical_care_only": False,
                "bleeding_risk": False,
                "organ_toxicity": {"hepatic": "Low", "autoimmune": "Moderate (drug-induced lupus, autoimmune hepatitis)"},
                "qt_prolongation": False,
                "hepatotoxicity": False,
                "nephrotoxicity": False,
                "requires_monitoring": [
                    "Signs of photosensitivity",
                    "Signs of autoimmune reactions (lupus-like syndrome, hepatitis)",
                    "Hepatic function (autoimmune hepatitis risk)",
                    "Complete blood count (autoimmune cytopenias)"
                ],
                "look_alike_sound_alike": ["Minocycline", "Doxycycline", "Tetracycline"]
            },
            "guideline_tags": [
                "IDSA Acne Treatment Guidelines",
                "IDSA Sexually Transmitted Infections Guidelines",
                "FDA Drug Label - Minocycline (autoimmune reactions warning)"
            ]
        },

        "Amoxicillin-clavulanate": {
            "risk_flags": {
                "high_alert": False,
                "narrow_therapeutic_index": False,
                "icu_critical_care_only": False,
                "bleeding_risk": False,
                "organ_toxicity": {"hepatic": "Moderate (hepatitis, especially with prolonged use)"},
                "qt_prolongation": False,
                "hepatotoxicity": True,
                "nephrotoxicity": False,
                "requires_monitoring": [
                    "Signs of allergic reaction (rash, anaphylaxis) - CRITICAL",
                    "Hepatic function (hepatitis risk, especially with prolonged use)",
                    "Diarrhea (C. difficile risk)",
                    "Complete blood count (if prolonged use)"
                ],
                "look_alike_sound_alike": ["Amoxicillin-clavulanate", "Amoxicillin", "Ampicillin-sulbactam"]
            },
            "guideline_tags": [
                "IDSA Community-Acquired Pneumonia Guidelines",
                "IDSA Complicated Skin and Soft Tissue Infection Guidelines",
                "IDSA Complicated Intra-abdominal Infection Guidelines",
                "FDA Drug Label - Amoxicillin-clavulanate (hepatitis warning)"
            ]
        },

        "Cephalexin": {
            "risk_flags": {
                "high_alert": False,
                "narrow_therapeutic_index": False,
                "icu_critical_care_only": False,
                "bleeding_risk": False,
                "organ_toxicity": {"renal": "Low"},
                "qt_prolongation": False,
                "hepatotoxicity": False,
                "nephrotoxicity": False,
                "requires_monitoring": [
                    "Signs of allergic reaction (rash, anaphylaxis)",
                    "Diarrhea (C. difficile risk)",
                    "Renal function (if high doses or prolonged use)"
                ],
                "look_alike_sound_alike": ["Cephalexin", "Cefadroxil", "Cefaclor"]
            },
            "guideline_tags": [
                "IDSA Skin and Soft Tissue Infection Guidelines",
                "IDSA Urinary Tract Infection Guidelines",
                "FDA Drug Label - Cephalexin"
            ]
        },

        "Clindamycin": {
            "risk_flags": {
                "high_alert": False,
                "narrow_therapeutic_index": False,
                "icu_critical_care_only": False,
                "bleeding_risk": False,
                "organ_toxicity": {"gastrointestinal": "High (C. difficile colitis)"},
                "qt_prolongation": False,
                "hepatotoxicity": False,
                "nephrotoxicity": False,
                "requires_monitoring": [
                    "Diarrhea (C. difficile colitis risk) - CRITICAL",
                    "Signs of allergic reaction (rash, anaphylaxis)",
                    "Complete blood count (if prolonged use)"
                ],
                "look_alike_sound_alike": ["Clindamycin", "Clarithromycin", "Lincomycin"]
            },
            "guideline_tags": [
                "IDSA Skin and Soft Tissue Infection Guidelines",
                "IDSA Clostridium difficile Infection Guidelines (risk factor)",
                "IDSA Odontogenic Infection Guidelines",
                "FDA Drug Label - Clindamycin (C. difficile warning)"
            ]
        },

        "Levofloxacin": {
            "risk_flags": {
                "high_alert": False,
                "narrow_therapeutic_index": False,
                "icu_critical_care_only": False,
                "bleeding_risk": False,
                "organ_toxicity": {"tendon": "Moderate (tendonitis, tendon rupture)", "cardiac": "Moderate (QT prolongation)", "hepatic": "Low"},
                "qt_prolongation": True,
                "hepatotoxicity": False,
                "nephrotoxicity": False,
                "requires_monitoring": [
                    "ECG (QT prolongation risk)",
                    "Signs of tendonitis/tendon rupture (especially Achilles tendon)",
                    "Signs of peripheral neuropathy",
                    "Signs of CNS effects (seizures, confusion)",
                    "Hepatic function (if prolonged use)"
                ],
                "look_alike_sound_alike": ["Levofloxacin", "Ciprofloxacin", "Moxifloxacin"]
            },
            "guideline_tags": [
                "FDA Black Box Warning - Tendonitis and Tendon Rupture",
                "FDA Black Box Warning - Peripheral Neuropathy",
                "IDSA Community-Acquired Pneumonia Guidelines",
                "IDSA Complicated Urinary Tract Infection Guidelines",
                "WHO Guidelines - Antimicrobial Resistance"
            ]
        },

        "Moxifloxacin": {
            "risk_flags": {
                "high_alert": False,
                "narrow_therapeutic_index": False,
                "icu_critical_care_only": False,
                "bleeding_risk": False,
                "organ_toxicity": {"tendon": "Moderate (tendonitis, tendon rupture)", "cardiac": "High (QT prolongation)", "hepatic": "Moderate (hepatitis)"},
                "qt_prolongation": True,
                "hepatotoxicity": True,
                "nephrotoxicity": False,
                "requires_monitoring": [
                    "ECG (QT prolongation risk) - CRITICAL",
                    "Signs of tendonitis/tendon rupture",
                    "Hepatic function (hepatitis risk)",
                    "Signs of peripheral neuropathy",
                    "Signs of CNS effects"
                ],
                "look_alike_sound_alike": ["Moxifloxacin", "Levofloxacin", "Ciprofloxacin"]
            },
            "guideline_tags": [
                "FDA Black Box Warning - Tendonitis and Tendon Rupture",
                "FDA Black Box Warning - QT Prolongation",
                "FDA Black Box Warning - Hepatotoxicity",
                "IDSA Community-Acquired Pneumonia Guidelines",
                "IDSA Complicated Skin and Soft Tissue Infection Guidelines"
            ]
        },

        # ======================== SESSION 2: CARBAPENEMS & OTHER PRIORITY ANTIBIOTICS ========================
        "Meropenem": {
            "risk_flags": {
                "high_alert": False,
                "narrow_therapeutic_index": False,
                "icu_critical_care_only": False,
                "bleeding_risk": False,
                "organ_toxicity": {"neurologic": "Moderate (seizures, especially in renal impairment or high doses)", "renal": "Low"},
                "qt_prolongation": False,
                "hepatotoxicity": False,
                "nephrotoxicity": False,
                "requires_monitoring": [
                    "Signs of allergic reaction (rash, anaphylaxis)",
                    "Neurologic symptoms (seizures, confusion) - especially if CrCl <50 or high doses",
                    "Renal function (CrCl) - adjust dose if CrCl <50",
                    "Complete blood count (if prolonged use)",
                    "Diarrhea (C. difficile risk)"
                ],
                "look_alike_sound_alike": ["Meropenem", "Imipenem/cilastatin", "Ertapenem"]
            },
            "guideline_tags": [
                "IDSA Healthcare-Associated Pneumonia Guidelines",
                "IDSA Complicated Intra-abdominal Infection Guidelines",
                "IDSA Febrile Neutropenia Guidelines",
                "IDSA Meningitis Guidelines",
                "FDA Drug Label - Meropenem (seizure warning)"
            ]
        },

        "Imipenem/cilastatin": {
            "risk_flags": {
                "high_alert": False,
                "narrow_therapeutic_index": False,
                "icu_critical_care_only": False,
                "bleeding_risk": False,
                "organ_toxicity": {"neurologic": "High (seizures, especially in renal impairment or high doses)", "renal": "Low"},
                "qt_prolongation": False,
                "hepatotoxicity": False,
                "nephrotoxicity": False,
                "requires_monitoring": [
                    "Signs of allergic reaction (rash, anaphylaxis)",
                    "Neurologic symptoms (seizures, confusion) - CRITICAL, especially if CrCl <50 or high doses",
                    "Renal function (CrCl) - adjust dose if CrCl <50",
                    "Complete blood count (if prolonged use)",
                    "Diarrhea (C. difficile risk)"
                ],
                "look_alike_sound_alike": ["Imipenem/cilastatin", "Meropenem", "Ertapenem"]
            },
            "guideline_tags": [
                "IDSA Healthcare-Associated Pneumonia Guidelines",
                "IDSA Complicated Intra-abdominal Infection Guidelines",
                "IDSA Febrile Neutropenia Guidelines",
                "FDA Black Box Warning - Seizures (especially in patients with CNS disorders or renal impairment)",
                "FDA Drug Label - Imipenem/cilastatin"
            ]
        },

        "Ertapenem": {
            "risk_flags": {
                "high_alert": False,
                "narrow_therapeutic_index": False,
                "icu_critical_care_only": False,
                "bleeding_risk": False,
                "organ_toxicity": {"neurologic": "Low (lower seizure risk than imipenem)", "renal": "Low"},
                "qt_prolongation": False,
                "hepatotoxicity": False,
                "nephrotoxicity": False,
                "requires_monitoring": [
                    "Signs of allergic reaction (rash, anaphylaxis)",
                    "Neurologic symptoms (seizures, confusion) - lower risk than imipenem",
                    "Renal function (CrCl) - adjust dose if CrCl <30",
                    "Complete blood count (if prolonged use)",
                    "Diarrhea (C. difficile risk)"
                ],
                "look_alike_sound_alike": ["Ertapenem", "Meropenem", "Imipenem/cilastatin"]
            },
            "guideline_tags": [
                "IDSA Complicated Intra-abdominal Infection Guidelines",
                "IDSA Complicated Skin and Soft Tissue Infection Guidelines",
                "IDSA Complicated Urinary Tract Infection Guidelines",
                "IDSA Community-Acquired Pneumonia Guidelines",
                "FDA Drug Label - Ertapenem"
            ]
        },

        "Trimethoprim/sulfamethoxazole": {
            "risk_flags": {
                "high_alert": False,
                "narrow_therapeutic_index": False,
                "icu_critical_care_only": False,
                "bleeding_risk": False,
                "organ_toxicity": {"renal": "Moderate (crystalluria, acute kidney injury)", "hepatic": "Moderate (hepatitis)", "hematologic": "Moderate (agranulocytosis, thrombocytopenia)"},
                "qt_prolongation": False,
                "hepatotoxicity": True,
                "nephrotoxicity": True,
                "requires_monitoring": [
                    "Signs of allergic reaction (rash, Stevens-Johnson syndrome, toxic epidermal necrolysis) - CRITICAL",
                    "Renal function (creatinine, eGFR) - crystalluria risk",
                    "Hepatic function (hepatitis risk)",
                    "Complete blood count (agranulocytosis, thrombocytopenia risk)",
                    "Hyperkalemia (especially in renal impairment or high doses)",
                    "Hyponatremia (especially in elderly)"
                ],
                "look_alike_sound_alike": ["Trimethoprim/sulfamethoxazole", "Cotrimoxazole", "Sulfamethoxazole/trimethoprim"]
            },
            "guideline_tags": [
                "IDSA Urinary Tract Infection Guidelines",
                "IDSA Pneumocystis jirovecii Pneumonia Guidelines",
                "IDSA Stenotrophomonas maltophilia Infection Guidelines",
                "FDA Black Box Warning - Severe Skin Reactions (Stevens-Johnson syndrome, toxic epidermal necrolysis)",
                "FDA Drug Label - Trimethoprim/sulfamethoxazole"
            ]
        },

        "Linezolid": {
            "risk_flags": {
                "high_alert": False,
                "narrow_therapeutic_index": False,
                "icu_critical_care_only": False,
                "bleeding_risk": False,
                "organ_toxicity": {"hematologic": "High (thrombocytopenia, anemia, leukopenia)", "neurologic": "Moderate (peripheral neuropathy, optic neuropathy)", "serotonin": "Moderate (serotonin syndrome with serotonergic drugs)"},
                "qt_prolongation": False,
                "hepatotoxicity": False,
                "nephrotoxicity": False,
                "requires_monitoring": [
                    "Complete blood count - CRITICAL (thrombocytopenia, anemia, leukopenia)",
                    "Signs of peripheral neuropathy (numbness, tingling)",
                    "Vision changes (optic neuropathy risk)",
                    "Signs of serotonin syndrome (if used with serotonergic drugs)",
                    "Lactic acidosis (rare but serious)"
                ],
                "look_alike_sound_alike": ["Linezolid", "Lincosamides"]
            },
            "guideline_tags": [
                "IDSA Vancomycin-Resistant Enterococcus (VRE) Infection Guidelines",
                "IDSA Methicillin-Resistant Staphylococcus aureus (MRSA) Infection Guidelines",
                "IDSA Skin and Soft Tissue Infection Guidelines",
                "FDA Black Box Warning - Myelosuppression (thrombocytopenia, anemia, leukopenia)",
                "FDA Black Box Warning - Peripheral and Optic Neuropathy",
                "FDA Drug Label - Linezolid"
            ]
        },

        "Daptomycin": {
            "risk_flags": {
                "high_alert": False,
                "narrow_therapeutic_index": False,
                "icu_critical_care_only": False,
                "bleeding_risk": False,
                "organ_toxicity": {"musculoskeletal": "High (rhabdomyolysis, myopathy)", "renal": "Moderate (rhabdomyolysis-related AKI)"},
                "qt_prolongation": False,
                "hepatotoxicity": False,
                "nephrotoxicity": False,
                "requires_monitoring": [
                    "Creatine phosphokinase (CPK) - CRITICAL (rhabdomyolysis risk)",
                    "Renal function (creatinine, eGFR) - rhabdomyolysis-related AKI",
                    "Signs of myopathy (muscle pain, weakness)",
                    "Signs of allergic reaction (rash, eosinophilic pneumonia)"
                ],
                "look_alike_sound_alike": ["Daptomycin", "Daptomycin"]
            },
            "guideline_tags": [
                "IDSA Vancomycin-Resistant Enterococcus (VRE) Infection Guidelines",
                "IDSA Methicillin-Resistant Staphylococcus aureus (MRSA) Infection Guidelines",
                "IDSA Skin and Soft Tissue Infection Guidelines",
                "IDSA Bacteremia and Endocarditis Guidelines",
                "FDA Black Box Warning - Rhabdomyolysis",
                "FDA Drug Label - Daptomycin"
            ]
        },

        "Colistin": {
            "risk_flags": {
                "high_alert": True,
                "narrow_therapeutic_index": True,
                "icu_critical_care_only": True,
                "bleeding_risk": False,
                "organ_toxicity": {"renal": "High", "neurologic": "High (neuropathy, neuromuscular blockade)", "respiratory": "Moderate (if inhaled)"},
                "qt_prolongation": False,
                "hepatotoxicity": False,
                "nephrotoxicity": True,
                "requires_monitoring": [
                    "Renal function (creatinine, eGFR) - CRITICAL",
                    "Urine output",
                    "Signs of neurotoxicity (numbness, tingling, weakness)",
                    "Signs of neuromuscular blockade (respiratory depression) - CRITICAL",
                    "Respiratory function (if inhaled form)"
                ],
                "look_alike_sound_alike": ["Colistin", "Colistimethate"]
            },
            "guideline_tags": [
                "IDSA Multidrug-Resistant Gram-Negative Infection Guidelines",
                "IDSA Healthcare-Associated Pneumonia Guidelines",
                "IDSA Complicated Urinary Tract Infection Guidelines",
                "FDA Drug Label - Colistin (nephrotoxicity and neurotoxicity warnings)"
            ]
        },

        # ======================== SESSION 3: ANTIFUNGALS & ANTIVIRALS ========================
        "Fluconazole": {
            "risk_flags": {
                "high_alert": False,
                "narrow_therapeutic_index": False,
                "icu_critical_care_only": False,
                "bleeding_risk": False,
                "organ_toxicity": {"hepatic": "Low", "cardiac": "Moderate (QT prolongation at high doses)"},
                "qt_prolongation": True,
                "hepatotoxicity": False,
                "nephrotoxicity": False,
                "requires_monitoring": [
                    "Hepatic function (hepatitis risk, especially with prolonged use)",
                    "ECG (QT prolongation risk at high doses or with other QT-prolonging drugs)",
                    "Signs of allergic reaction (rash, Stevens-Johnson syndrome)",
                    "Renal function (if high doses or prolonged use)"
                ],
                "look_alike_sound_alike": ["Fluconazole", "Voriconazole", "Itraconazole"]
            },
            "guideline_tags": [
                "IDSA Candidiasis Treatment Guidelines",
                "IDSA Cryptococcosis Treatment Guidelines",
                "IDSA Coccidioidomycosis Treatment Guidelines",
                "FDA Drug Label - Fluconazole (QT prolongation and hepatotoxicity warnings)"
            ]
        },

        "Voriconazole": {
            "risk_flags": {
                "high_alert": True,
                "narrow_therapeutic_index": True,
                "icu_critical_care_only": False,
                "bleeding_risk": False,
                "organ_toxicity": {"hepatic": "High", "visual": "High (photophobia, blurred vision, color vision changes)", "cardiac": "Moderate (QT prolongation)", "dermatologic": "High (photosensitivity, skin cancer risk)"},
                "qt_prolongation": True,
                "hepatotoxicity": True,
                "nephrotoxicity": False,
                "requires_monitoring": [
                    "Voriconazole trough level - CRITICAL (TDM recommended, target 1-5.5 mcg/ml)",
                    "Hepatic function (ALT, AST, bilirubin) - CRITICAL",
                    "Visual function (photophobia, blurred vision, color vision changes)",
                    "ECG (QT prolongation risk)",
                    "Skin examination (photosensitivity, skin cancer risk)",
                    "Signs of allergic reaction (rash, Stevens-Johnson syndrome)"
                ],
                "look_alike_sound_alike": ["Voriconazole", "Fluconazole", "Itraconazole"]
            },
            "guideline_tags": [
                "IDSA Invasive Aspergillosis Treatment Guidelines",
                "IDSA Invasive Candidiasis Treatment Guidelines",
                "IDSA Scedosporium and Fusarium Infection Guidelines",
                "FDA Black Box Warning - Hepatotoxicity",
                "FDA Black Box Warning - Visual Disturbances",
                "FDA Drug Label - Voriconazole (TDM recommended)"
            ]
        },

        "Amphotericin B": {
            "risk_flags": {
                "high_alert": True,
                "narrow_therapeutic_index": True,
                "icu_critical_care_only": False,
                "bleeding_risk": False,
                "organ_toxicity": {"renal": "High", "hepatic": "Moderate", "hematologic": "Moderate (anemia)", "cardiac": "Moderate (arrhythmias, especially with rapid infusion)"},
                "qt_prolongation": False,
                "hepatotoxicity": False,
                "nephrotoxicity": True,
                "requires_monitoring": [
                    "Renal function (creatinine, eGFR, BUN) - CRITICAL",
                    "Urine output",
                    "Electrolytes (potassium, magnesium) - CRITICAL (hypokalemia, hypomagnesemia)",
                    "Complete blood count (anemia)",
                    "Hepatic function (hepatitis risk)",
                    "ECG (arrhythmias, especially with rapid infusion)",
                    "Infusion reactions (fever, chills, rigors, hypotension) - CRITICAL",
                    "Signs of allergic reaction (anaphylaxis)"
                ],
                "look_alike_sound_alike": ["Amphotericin B", "Amphotericin B lipid complex", "Liposomal amphotericin B"]
            },
            "guideline_tags": [
                "IDSA Invasive Candidiasis Treatment Guidelines",
                "IDSA Invasive Aspergillosis Treatment Guidelines",
                "IDSA Cryptococcosis Treatment Guidelines",
                "IDSA Mucormycosis Treatment Guidelines",
                "FDA Black Box Warning - Nephrotoxicity",
                "FDA Drug Label - Amphotericin B (infusion reactions and nephrotoxicity warnings)"
            ]
        },

        "Acyclovir": {
            "risk_flags": {
                "high_alert": False,
                "narrow_therapeutic_index": False,
                "icu_critical_care_only": False,
                "bleeding_risk": False,
                "organ_toxicity": {"renal": "High (crystalluria, acute kidney injury, especially with rapid IV infusion or dehydration)", "neurologic": "Moderate (neurotoxicity, especially in renal impairment)"},
                "qt_prolongation": False,
                "hepatotoxicity": False,
                "nephrotoxicity": True,
                "requires_monitoring": [
                    "Renal function (creatinine, eGFR) - CRITICAL, especially with IV high-dose therapy",
                    "Urine output",
                    "Signs of crystalluria (crystal formation in urine)",
                    "Neurologic symptoms (confusion, hallucinations, seizures) - especially in renal impairment",
                    "Hydration status (maintain adequate hydration to prevent crystalluria)"
                ],
                "look_alike_sound_alike": ["Acyclovir", "Valacyclovir", "Ganciclovir"]
            },
            "guideline_tags": [
                "IDSA Herpes Simplex Virus (HSV) Infection Guidelines",
                "IDSA Varicella-Zoster Virus (VZV) Infection Guidelines",
                "IDSA Encephalitis Guidelines",
                "FDA Drug Label - Acyclovir (nephrotoxicity and neurotoxicity warnings)"
            ]
        },

        "Valacyclovir": {
            "risk_flags": {
                "high_alert": False,
                "narrow_therapeutic_index": False,
                "icu_critical_care_only": False,
                "bleeding_risk": False,
                "organ_toxicity": {"renal": "Moderate (crystalluria, acute kidney injury, especially with high doses or renal impairment)", "neurologic": "Moderate (neurotoxicity, especially in renal impairment)"},
                "qt_prolongation": False,
                "hepatotoxicity": False,
                "nephrotoxicity": True,
                "requires_monitoring": [
                    "Renal function (creatinine, eGFR) - especially with high doses or renal impairment",
                    "Urine output",
                    "Signs of crystalluria",
                    "Neurologic symptoms (confusion, hallucinations, seizures) - especially in renal impairment",
                    "Hydration status (maintain adequate hydration)"
                ],
                "look_alike_sound_alike": ["Valacyclovir", "Acyclovir", "Famciclovir"]
            },
            "guideline_tags": [
                "IDSA Herpes Simplex Virus (HSV) Infection Guidelines",
                "IDSA Varicella-Zoster Virus (VZV) Infection Guidelines",
                "IDSA Genital Herpes Guidelines",
                "FDA Drug Label - Valacyclovir (nephrotoxicity and neurotoxicity warnings)"
            ]
        },

        "Oseltamivir": {
            "risk_flags": {
                "high_alert": False,
                "narrow_therapeutic_index": False,
                "icu_critical_care_only": False,
                "bleeding_risk": False,
                "organ_toxicity": {"neuropsychiatric": "Moderate (especially in children/adolescents - confusion, hallucinations, self-injury)", "gastrointestinal": "Moderate (nausea, vomiting)"},
                "qt_prolongation": False,
                "hepatotoxicity": False,
                "nephrotoxicity": False,
                "requires_monitoring": [
                    "Neuropsychiatric symptoms (especially in children/adolescents) - confusion, hallucinations, abnormal behavior, self-injury",
                    "Gastrointestinal symptoms (nausea, vomiting)",
                    "Signs of allergic reaction (rash, anaphylaxis)"
                ],
                "look_alike_sound_alike": ["Oseltamivir", "Zanamivir", "Peramivir"]
            },
            "guideline_tags": [
                "IDSA Influenza Treatment Guidelines",
                "CDC Influenza Antiviral Treatment Guidelines",
                "WHO Influenza Treatment Guidelines",
                "FDA Drug Label - Oseltamivir (neuropsychiatric events warning, especially in children)"
            ]
        },

}
