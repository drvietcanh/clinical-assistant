"""
HIV Antiretrovirals - Boosters
"""
from typing import Dict, Any


BOOSTERS_ARVS: Dict[str, Dict[str, Any]] = {
        "Cobicistat (COBI)": {
            "group": "Pharmacokinetic booster (CYP3A inhibitor)",
            "vietnamese_name": "Cobicistat",
            "administration": ["PO"],
            "indications": [
                "Tăng cường nồng độ ARV chuyển hóa qua CYP3A (elvitegravir, atazanavir, darunavir) trong các FDC/nền có COBI.",
            ],
            "contraindications": [
                "Dị ứng với cobicistat.",
                "Dùng với thuốc phụ thuộc CYP3A để thanh thải có cửa sổ hẹp (ví dụ amiodarone, dronedarone, ergot, alfuzosin, triazolam/midazolam PO).",
            ],
            "dosage": {
                "standard": "150mg PO mỗi ngày (trong FDC hoặc viên rời).",
                "notes": "Dùng cùng thuốc đích (PI/INSTI) và thức ăn nếu theo nhãn của thuốc đích.",
            },
            "renal_adjustment": {
                "normal": "Không cần chỉnh.",
                "30_60": "Không cần chỉnh; theo dõi creatinine (tăng giả do ức chế OCT2).",
                "under_30": "Theo nhãn FDC: tránh dùng nếu eGFR <30 (do TAF/FTC kèm).",
            },
            "side_effects": [
                "Buồn nôn, tiêu chảy.",
                "Tăng nhẹ creatinine (ức chế vận chuyển ống thận, không giảm GFR thực).",
                "Vàng da nhẹ nếu phối hợp atazanavir (tăng bilirubin gián tiếp).",
            ],
            "interactions": [
                "Ức chế mạnh CYP3A, P-gp, OATP1B1/3: nhiều tương tác thuốc.",
            ],
            "pregnancy": "Tránh dùng trong thai kỳ (nồng độ giảm, ưu tiên ritonavir hoặc không booster).",
            "risk_flags": {
                "high_alert": True,
                "narrow_therapeutic_index": False,
                "organ_toxicity": {"hepatic": True},
                "icu_critical_care_only": False,
                "look_alike_sound_alike": []
            },
            "guideline_tags": [
                "DHHS/CDC HIV 2024",
                "WHO 2024 HIV"
            ],
            "mechanism_of_action": (
                "Ức chế CYP3A và P-gp, làm tăng phơi nhiễm thuốc ARV mục tiêu (PI/INSTI) mà không có "
                "hoạt tính kháng virus độc lập."
            ),
            "monitoring": [
                "Creatinine (tăng giả).",
                "Men gan, bilirubin nếu dùng với atazanavir.",
                "Theo dõi tương tác thuốc (CYP3A/P-gp).",
            ],
            "precautions": [
                "Rà soát tương tác CYP3A/P-gp/OATP trước kê đơn.",
                "Tránh dùng với thuốc cửa sổ hẹp phụ thuộc CYP3A để thải trừ.",
                "Tăng creatinine giả: giải thích cho bệnh nhân, không phản ánh suy thận thật nếu eGFR ổn định.",
            ],
            "pharmacokinetics": {
                "half_life": "3–4 giờ.",
                "onset": "Cmax ~1–2 giờ.",
                "duration": "Tác dụng ức chế CYP kéo dài đủ cho liều ngày 1 lần.",
                "protein_binding": "~98%.",
                "clearance": "Gan (CYP3A).",
            },
            "storage": "20–25°C, khô ráo.",
            "black_box_warnings": None,
            "drug_interactions": {
                "major": [
                    {
                        "drug": "Amiodarone, dronedarone, ergot, alfuzosin, triazolam/midazolam PO",
                        "mechanism": "Ức chế CYP3A mạnh làm tăng phơi nhiễm thuốc cửa sổ hẹp.",
                        "effect": "Nguy cơ độc tính nặng.",
                        "management": "CHỐNG CHỈ ĐỊNH.",
                    }
                ],
                "moderate": [
                    {
                        "drug": "Statins (simvastatin, lovastatin)",
                        "mechanism": "Ức chế CYP3A tăng AUC statin.",
                        "effect": "Tăng nguy cơ tiêu cơ vân.",
                        "management": "Tránh; dùng pravastatin/rosuvastatin liều thấp và theo dõi.",
                    },
                    {
                        "drug": "DOACs (apixaban, rivaroxaban)",
                        "mechanism": "Ức chế CYP3A/P-gp tăng nồng độ DOAC.",
                        "effect": "Tăng chảy máu.",
                        "management": "Tránh hoặc giảm liều theo khuyến cáo, theo dõi chảy máu.",
                    }
                ],
                "minor": [],
            },
            "contraindications_detail": {
                "tuyệt_đối": [
                    "Quá mẫn COBI.",
                    "Phối hợp thuốc cửa sổ hẹp phụ thuộc CYP3A (amiodarone, dronedarone, ergot, alfuzosin, triazolam/midazolam PO).",
                ],
                "tương_đối": [
                    "Suy gan trung bình-nặng.",
                    "Suy thận <30 (theo FDC có TAF/FTC).",
                ],
            },
            "pregnancy_lactation": {
                "fda_category": "Not classified",
                "pregnancy_details": "Không ưu tiên trong thai kỳ do nồng độ giảm; chọn ritonavir hoặc phác đồ không cần booster.",
                "lactation": {
                    "safety": "Caution",
                    "details": "Dữ liệu hạn chế.",
                    "recommendation": "Đánh giá lợi ích/nguy cơ.",
                },
            },
            "hepatic_adjustment": {
                "mild": "Không cần chỉnh nhưng theo dõi men gan.",
                "moderate": "Thận trọng.",
                "severe": "Tránh (dữ liệu hạn chế).",
                "notes": "Chuyển hóa qua gan; ức chế CYP3A mạnh.",
            },
            "overdose_management": {
                "symptoms": ["Buồn nôn, tăng bilirubin (nếu dùng với ATV), ức chế quá mức CYP3A."],
                "antidote": "Không có.",
                "treatment": [
                    "Điều trị hỗ trợ, than hoạt nếu mới uống.",
                    "Theo dõi ECG, men gan, dấu hiệu độc tính thuốc phối hợp.",
                ],
                "monitoring": "Dấu hiệu sinh tồn, men gan, tương tác thuốc kèm.",
            },
            "reversal_agents": {
                "available": False,
                "agents": [],
                "notes": "Không có antidote đặc hiệu. Điều trị quá liều chủ yếu là điều trị hỗ trợ, than hoạt nếu mới uống, theo dõi ECG, men gan, và dấu hiệu độc tính thuốc phối hợp."
            },
            "administration_instructions": {
                "oral": {
                    "with_food": "Theo thuốc đích (đa số PI cần thức ăn).",
                    "timing": "1 lần/ngày cùng thuốc đích.",
                }
            },
            "references": {
                "primary_sources": [
                    "DHHS/CDC HIV Treatment Guidelines",
                    "WHO 2024 HIV"
                ],
                "last_updated": "2025-12-24",
                "evidence_level": "High – guideline-based",
            },
        },

        "Ritonavir (low-dose booster)": {
            "group": "Pharmacokinetic booster (CYP3A inhibitor; PI at high dose)",
            "vietnamese_name": "Ritonavir (liều thấp tăng cường PI)",
            "administration": ["PO"],
            "indications": [
                "Tăng cường nồng độ protease inhibitors (lopinavir, atazanavir, darunavir…).",
            ],
            "contraindications": [
                "Dị ứng ritonavir.",
                "Dùng với thuốc phụ thuộc CYP3A cửa sổ hẹp (amiodarone, ergot, alfuzosin, triazolam/midazolam PO…).",
            ],
            "dosage": {
                "booster": "100mg PO 1–2 lần/ngày tùy PI.",
                "notes": "Uống với thức ăn để giảm khó tiêu; không dùng như đơn trị ART.",
            },
            "renal_adjustment": {
                "normal": "Không cần chỉnh.",
                "30_60": "Không cần chỉnh.",
                "under_30": "Không cần chỉnh; theo dõi nếu kèm TDF.",
            },
            "side_effects": [
                "Buồn nôn, tiêu chảy, vị khó chịu.",
                "Tăng triglycerid/cholesterol.",
                "Tăng men gan.",
                "Thay đổi mỡ phân bố (dùng lâu, liều PI đầy đủ).",
            ],
            "interactions": [
                "Ức chế mạnh CYP3A/CYP2D6/P-gp → rất nhiều tương tác.",
            ],
            "pregnancy": "Có thể dùng; được kinh nghiệm lâu dài hơn COBI.",
            "risk_flags": {
                "high_alert": True,
                "narrow_therapeutic_index": False,
                "organ_toxicity": {"hepatic": True, "metabolic": True},
                "icu_critical_care_only": False,
                "look_alike_sound_alike": []
            },
            "guideline_tags": [
                "DHHS/CDC HIV 2024",
                "WHO 2024 HIV"
            ],
            "mechanism_of_action": (
                "Ức chế CYP3A/CYP2D6 và P-gp, tăng phơi nhiễm PI mục tiêu; liều thấp không nhằm hoạt tính kháng virus chính."
            ),
            "monitoring": [
                "Men gan, lipid (TG/LDL).",
                "Dấu hiệu tương tác thuốc (chảy máu với DOAC, an thần với benzo...).",
                "Glucose nếu dùng dài hạn (nguy cơ đề kháng insulin).",
            ],
            "precautions": [
                "Rà soát tương tác CYP3A/CYP2D6/P-gp kỹ trước kê đơn.",
                "Uống với thức ăn để giảm khó chịu tiêu hóa.",
                "Thận trọng bệnh gan, tăng TG nền.",
            ],
            "pharmacokinetics": {
                "half_life": "3–5 giờ (ức chế CYP kéo dài hơn).",
                "onset": "Cmax ~2–4 giờ.",
                "duration": "Dùng 1–2 lần/ngày tùy PI.",
                "protein_binding": "~98–99%.",
                "clearance": "Gan (CYP3A/2D6).",
            },
            "storage": "Viên: 20–25°C; dung dịch cần bảo quản lạnh sau mở (theo nhãn).",
            "black_box_warnings": None,
            "drug_interactions": {
                "major": [
                    {
                        "drug": "Amiodarone, dronedarone, ergot, alfuzosin, triazolam/midazolam PO",
                        "mechanism": "Ức chế CYP3A mạnh tăng phơi nhiễm.",
                        "effect": "Nguy cơ độc tính nặng.",
                        "management": "CHỐNG CHỈ ĐỊNH.",
                    }
                ],
                "moderate": [
                    {
                        "drug": "Statins (simvastatin, lovastatin)",
                        "mechanism": "Ức chế CYP3A tăng AUC statin.",
                        "effect": "Nguy cơ tiêu cơ vân.",
                        "management": "Tránh; dùng pravastatin/rosuvastatin liều thấp.",
                    },
                    {
                        "drug": "DOACs (apixaban, rivaroxaban)",
                        "mechanism": "Ức chế CYP3A/P-gp.",
                        "effect": "Tăng chảy máu.",
                        "management": "Tránh hoặc giảm liều/giám sát chặt.",
                    }
                ],
                "minor": [],
            },
            "contraindications_detail": {
                "tuyệt_đối": [
                    "Quá mẫn ritonavir.",
                    "Phối hợp thuốc cửa sổ hẹp phụ thuộc CYP3A.",
                ],
                "tương_đối": [
                    "Bệnh gan mạn, tăng TG/LDL nặng.",
                ],
            },
            "pregnancy_lactation": {
                "fda_category": "B",
                "pregnancy_details": "Có thể dùng liều booster; đã có kinh nghiệm trong thai kỳ hơn COBI.",
                "lactation": {
                    "safety": "Caution",
                    "details": "Bài tiết thấp vào sữa; dữ liệu hạn chế.",
                    "recommendation": "Theo dõi trẻ; cân nhắc lợi ích/nguy cơ.",
                },
            },
            "hepatic_adjustment": {
                "mild": "Thận trọng, có thể không cần chỉnh.",
                "moderate": "Thận trọng, theo dõi men gan.",
                "severe": "Tránh nếu có thể.",
                "notes": "Chuyển hóa qua gan; tăng phơi nhiễm ở suy gan.",
            },
            "overdose_management": {
                "symptoms": ["Buồn nôn, tiêu chảy, chóng mặt; lý thuyết kéo dài QT/PR ở liều cao."],
                "antidote": "Không có.",
                "treatment": [
                    "Than hoạt nếu uống gần đây.",
                    "Theo dõi ECG, điện giải, dấu hiệu sinh tồn.",
                ],
                "monitoring": "ECG, men gan, glucose, lipid.",
            },
            "reversal_agents": {
                "available": False,
                "agents": [],
                "notes": "Không có antidote đặc hiệu. Điều trị quá liều chủ yếu là than hoạt nếu uống gần đây, theo dõi ECG, điện giải, và dấu hiệu sinh tồn."
            },
            "administration_instructions": {
                "oral": {
                    "with_food": "Uống với thức ăn để giảm rối loạn tiêu hóa.",
                    "timing": "1–2 lần/ngày tùy PI nền.",
                }
            },
            "references": {
                "primary_sources": [
                    "DHHS/CDC HIV Treatment Guidelines",
                    "WHO 2024 HIV"
                ],
                "last_updated": "2025-12-24",
                "evidence_level": "High – guideline-based",
            },
        },

}

__all__ = ['BOOSTERS_ARVS']
