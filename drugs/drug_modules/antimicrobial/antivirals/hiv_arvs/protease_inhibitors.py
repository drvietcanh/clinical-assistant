"""
HIV Antiretrovirals - Protease Inhibitors
"""
from typing import Dict, Any


PROTEASE_INHIBITORS_ARVS: Dict[str, Dict[str, Any]] = {
        "Atazanavir (boosted with ritonavir/cobicistat)": {
            "group": "Antiviral - Protease inhibitor (boosted)",
            "vietnamese_name": "Atazanavir (tăng cường ritonavir/cobicistat)",
            "administration": ["PO"],
            "indications": [
                "Điều trị HIV-1 ở người lớn/thanh thiếu niên, luôn dùng kèm booster (RTV/COBI) + backbone NRTI."
            ],
            "contraindications": [
                "Dị ứng với atazanavir.",
                "Dùng đồng thời PPI liều cao (giảm hấp thu), rifampin (cảm ứng mạnh), thuốc phụ thuộc CYP3A cửa sổ hẹp (amiodarone, ergot, alfuzosin, triazolam/midazolam PO).",
                "Tiền sử sỏi mật/sỏi thận nặng: thận trọng."
            ],
            "dosage": {
                "naive": "Atazanavir 300mg + ritonavir 100mg PO mỗi ngày với thức ăn.",
                "with_cobicistat": "Atazanavir 300mg + cobicistat 150mg PO mỗi ngày với thức ăn.",
                "experienced_without_resistance": "300/100mg QD; nếu dùng tenofovir cần booster bắt buộc.",
                "notes": "Luôn uống với thức ăn để tăng hấp thu; tránh PPI liều chuẩn/cao, H2/antacid cần tách thời gian."
            },
            "renal_adjustment": {
                "normal": "Không cần chỉnh.",
                "30_60": "Không cần chỉnh; theo dõi bilirubin/gan.",
                "under_30": "Không cần chỉnh; thận trọng nếu dùng TDF (độc thận)."
            },
            "side_effects": [
                "Tăng bilirubin gián tiếp (vàng da, vàng mắt không do gan), vàng da thường thoáng qua.",
                "Buồn nôn, tiêu chảy.",
                "Sỏi mật/sỏi thận (ít gặp).",
                "Tăng PR, hiếm block AV.",
                "Tăng men gan."
            ],
            "interactions": [
                "Ức chế CYP3A (qua booster) → nhiều tương tác (statin, DOAC, benzo).",
                "Thuốc tăng pH dạ dày (PPI/H2/antacid) giảm hấp thu atazanavir.",
                "Inducer mạnh (rifampin, carbamazepine) giảm nồng độ → tránh."
            ],
            "pregnancy": "Có thể dùng; ưu tiên ritonavir booster. Tránh PPI, quản lý H2/antacid theo khuyến cáo.",
            "risk_flags": {
                "high_alert": True,
                "narrow_therapeutic_index": False,
                "organ_toxicity": {"hepatic": True, "cardiac": True, "biliary": True},
                "icu_critical_care_only": False,
                "look_alike_sound_alike": []
            },
            "guideline_tags": [
                "DHHS/CDC HIV 2024",
                "WHO 2024 HIV",
                "IAS-USA 2024"
            ],
            "mechanism_of_action": "PI ức chế protease HIV-1, ngăn cắt polyprotein Gag-Pol; cần booster ức chế CYP3A để đạt nồng độ.",
            "monitoring": [
                "HIV RNA, CD4.",
                "Bilirubin toàn phần/trực tiếp (tăng gián tiếp thường gặp).",
                "Men gan.",
                "ECG nếu có yếu tố kéo dài PR/block AV.",
                "Lipid/glucose (ít ảnh hưởng hơn một số PI khác)."
            ],
            "precautions": [
                "Luôn dùng với booster + thức ăn.",
                "Tránh PPI; H2 uống ≥12h trước hoặc ≥4h sau; antacid cách 2h.",
                "Theo dõi vàng da; tư vấn tính chất lành tính do tăng bilirubin gián tiếp.",
                "Rà soát tương tác CYP3A/P-gp (statin/DOAC/benzo/antiarrhythmic)."
            ],
            "pharmacokinetics": {
                "half_life": "~7 giờ (boosted).",
                "onset": "Cmax 2.5–3 giờ với thức ăn.",
                "duration": "1 lần/ngày.",
                "protein_binding": "~86%.",
                "clearance": "Gan (CYP3A); cần booster."
            },
            "storage": "20–25°C, tránh ẩm.",
            "black_box_warnings": None,
            "drug_interactions": {
                "major": [
                    {
                        "drug": "Rifampin; amiodarone/dronedarone/ergot/alfuzosin/triazolam/midazolam PO",
                        "mechanism": "Cảm ứng mạnh giảm AUC hoặc ức chế CYP3A tăng độc tính.",
                        "effect": "Thất bại điều trị hoặc độc tính nặng.",
                        "management": "CHỐNG CHỈ ĐỊNH."
                    },
                    {
                        "drug": "Proton pump inhibitors (omeprazole, etc.)",
                        "mechanism": "Tăng pH giảm hấp thu atazanavir.",
                        "effect": "Giảm nồng độ, thất bại điều trị.",
                        "management": "Tránh; nếu bất khả, dùng H2/antacid theo khuyến cáo."
                    }
                ],
                "moderate": [
                    {
                        "drug": "H2 blockers",
                        "mechanism": "Tăng pH dạ dày.",
                        "effect": "Giảm AUC.",
                        "management": "Dùng atazanavir với thức ăn ≥2h trước hoặc ≥10–12h sau H2; theo nhãn.",
                    },
                    {
                        "drug": "Antacid/chelator",
                        "mechanism": "Tăng pH/chelat.",
                        "effect": "Giảm hấp thu.",
                        "management": "Cách 2h trước hoặc sau atazanavir.",
                    },
                    {
                        "drug": "Statins (simvastatin/lovastatin)",
                        "mechanism": "Ức chế CYP3A tăng AUC statin.",
                        "effect": "Nguy cơ tiêu cơ vân.",
                        "management": "Tránh; dùng pravastatin/rosuvastatin liều thấp."
                    }
                ],
                "minor": []
            },
            "contraindications_detail": {
                "tuyệt_đối": [
                    "Quá mẫn.",
                    "Phối hợp rifampin hoặc thuốc cửa sổ hẹp phụ thuộc CYP3A.",
                    "PPI liều chuẩn/cao."
                ],
                "tương_đối": [
                    "Block AV, kéo dài PR.",
                    "Tiền sử sỏi mật/thận.",
                    "Suy gan."
                ]
            },
            "pregnancy_lactation": {
                "fda_category": "Not classified",
                "pregnancy_details": "Có thể dùng; ưu tiên ritonavir booster; tránh PPI, quản lý H2/antacid đúng cách.",
                "lactation": {
                    "safety": "Caution",
                    "details": "Dữ liệu hạn chế.",
                    "recommendation": "Đánh giá lợi ích/nguy cơ."
                }
            },
            "hepatic_adjustment": {
                "mild": "Không cần chỉnh; theo dõi men gan/bilirubin.",
                "moderate": "Thận trọng.",
                "severe": "Tránh do dữ liệu hạn chế.",
                "notes": "Chuyển hóa qua gan CYP3A; tăng phơi nhiễm ở suy gan."
            },
            "overdose_management": {
                "symptoms": ["Buồn nôn, vàng da (bilirubin tăng), rối loạn dẫn truyền (kéo dài PR)."],
                "antidote": "Không có.",
                "treatment": [
                    "Than hoạt nếu mới uống.",
                    "Theo dõi ECG, bilirubin, men gan.",
                    "Điều trị hỗ trợ."
                ],
                "monitoring": "ECG, men gan, bilirubin."
            },
            "reversal_agents": {
                "available": False,
                "agents": [],
                "notes": "Không có antidote đặc hiệu. Điều trị quá liều chủ yếu là than hoạt nếu mới uống, theo dõi ECG, bilirubin, và men gan, điều trị hỗ trợ."
            },
            "administration_instructions": {
                "oral": {
                    "with_food": "PHẢI uống với thức ăn.",
                    "timing": "1 lần/ngày cùng booster; tránh/giãn antacid/H2/PPI theo hướng dẫn."
                }
            },
            "references": {
                "primary_sources": [
                    "DHHS/CDC HIV Treatment Guidelines",
                    "WHO 2024 HIV",
                    "IAS-USA 2024"
                ],
                "last_updated": "2025-12-24",
                "evidence_level": "High – guideline-based"
            }
        },

        "Darunavir (boosted with ritonavir/cobicistat)": {
            "group": "Antiviral - Protease inhibitor (boosted)",
            "vietnamese_name": "Darunavir (tăng cường ritonavir hoặc cobicistat)",
            "administration": ["PO"],
            "indications": [
                "Điều trị HIV-1 ở người lớn/thanh thiếu niên, first-line hoặc salvage, luôn dùng kèm booster (RTV/COBI) + backbone NRTI."
            ],
            "contraindications": [
                "Dị ứng sulfonamide (thận trọng/có thể chống chỉ định nếu nặng).",
                "Dùng cùng thuốc phụ thuộc CYP3A cửa sổ hẹp (amiodarone, ergot, alfuzosin, triazolam/midazolam PO)."
            ],
            "dosage": {
                "naive": "Darunavir 800mg + ritonavir 100mg PO mỗi ngày (với thức ăn).",
                "experienced_with_resistance": "Darunavir 600mg + ritonavir 100mg PO x 2 lần/ngày.",
                "with_cobicistat": "Darunavir 800mg + cobicistat 150mg PO mỗi ngày (FDC/cùng viên), với thức ăn.",
                "notes": "Luôn dùng với booster; uống với thức ăn để tăng hấp thu và giảm khó chịu tiêu hóa."
            },
            "renal_adjustment": {
                "normal": "Không cần chỉnh.",
                "30_60": "Không cần chỉnh; theo dõi nếu dùng TDF backbone.",
                "under_30": "Không cần chỉnh; lưu ý thành phần nền (TDF) nếu có."
            },
            "side_effects": [
                "Buồn nôn, tiêu chảy, đau đầu.",
                "Tăng men gan; phát ban (do thành phần sulfonamide).",
                "Tăng lipid, tăng glucose (hiếm hơn một số PI khác)."
            ],
            "interactions": [
                "Ức chế mạnh CYP3A (qua booster) → rất nhiều tương tác (statin, DOAC, benzo, kháng loạn nhịp).",
                "Inducers mạnh (rifampin, carbamazepine) giảm nồng độ darunavir → tránh."
            ],
            "pregnancy": "Có thể dùng; kinh nghiệm với ritonavir nhiều hơn cobicistat trong thai kỳ.",
            "risk_flags": {
                "high_alert": True,
                "narrow_therapeutic_index": False,
                "organ_toxicity": {"hepatic": True, "metabolic": True},
                "icu_critical_care_only": False,
                "look_alike_sound_alike": []
            },
            "guideline_tags": [
                "DHHS/CDC HIV 2024",
                "WHO 2024 HIV",
                "IAS-USA 2024"
            ],
            "mechanism_of_action": "PI ức chế protease HIV-1, ngăn cắt polyprotein Gag-Pol, tạo virion không trưởng thành; cần booster ức chế CYP3A để đạt nồng độ điều trị.",
            "monitoring": [
                "HIV RNA, CD4.",
                "Men gan (ALT/AST, bilirubin).",
                "Lipid (TG/LDL), glucose.",
                "Dấu hiệu phát ban/ quá mẫn sulfonamide."
            ],
            "precautions": [
                "Luôn dùng với booster + thức ăn.",
                "Rà soát tương tác CYP3A/P-gp kỹ (statin, DOAC, benzo, kháng loạn nhịp).",
                "Thận trọng tiền sử dị ứng sulfonamide.",
                "Theo dõi men gan ở viêm gan đồng nhiễm HBV/HCV."
            ],
            "pharmacokinetics": {
                "half_life": "~15 giờ khi boosted QD; ~7–8 giờ BID.",
                "onset": "Cmax 2.5–4 giờ (với thức ăn).",
                "duration": "QD hoặc BID tùy kháng.",
                "protein_binding": "~95%.",
                "clearance": "Gan (CYP3A); cần booster để đạt nồng độ."
            },
            "storage": "20–25°C, tránh ẩm.",
            "black_box_warnings": None,
            "drug_interactions": {
                "major": [
                    {
                        "drug": "Amiodarone, dronedarone, ergot, alfuzosin, triazolam/midazolam PO",
                        "mechanism": "Ức chế CYP3A (booster) tăng phơi nhiễm thuốc cửa sổ hẹp.",
                        "effect": "Nguy cơ độc tính nặng.",
                        "management": "CHỐNG CHỈ ĐỊNH."
                    },
                    {
                        "drug": "Rifampin",
                        "mechanism": "Cảm ứng CYP3A mạnh giảm nồng độ darunavir.",
                        "effect": "Thất bại điều trị.",
                        "management": "CHỐNG CHỈ ĐỊNH."
                    }
                ],
                "moderate": [
                    {
                        "drug": "Statins (simvastatin, lovastatin)",
                        "mechanism": "Ức chế CYP3A tăng AUC statin.",
                        "effect": "Nguy cơ tiêu cơ vân.",
                        "management": "Tránh; dùng pravastatin/rosuvastatin liều thấp."
                    },
                    {
                        "drug": "DOACs (apixaban, rivaroxaban)",
                        "mechanism": "Ức chế CYP3A/P-gp tăng nồng độ.",
                        "effect": "Tăng chảy máu.",
                        "management": "Tránh hoặc giảm liều/giám sát theo khuyến cáo."
                    }
                ],
                "minor": []
            },
            "contraindications_detail": {
                "tuyệt_đối": [
                    "Quá mẫn darunavir/sulfonamide nặng.",
                    "Phối hợp thuốc cửa sổ hẹp phụ thuộc CYP3A.",
                    "Phối hợp rifampin."
                ],
                "tương_đối": [
                    "Bệnh gan mạn; đồng nhiễm HBV/HCV.",
                    "Tăng lipid nặng."
                ]
            },
            "pregnancy_lactation": {
                "fda_category": "Not classified (PI; kinh nghiệm với RTV hơn COBI)",
                "pregnancy_details": "Có thể dùng; ưu tiên ritonavir booster trong thai kỳ.",
                "lactation": {
                    "safety": "Caution",
                    "details": "Dữ liệu hạn chế.",
                    "recommendation": "Đánh giá lợi ích/nguy cơ."
                }
            },
            "hepatic_adjustment": {
                "mild": "Không cần chỉnh; theo dõi men gan.",
                "moderate": "Thận trọng; có thể tăng phơi nhiễm.",
                "severe": "Tránh do thiếu dữ liệu và nguy cơ tích lũy.",
                "notes": "Chuyển hóa gan qua CYP3A; booster làm tăng AUC."
            },
            "overdose_management": {
                "symptoms": ["Buồn nôn, nôn, chóng mặt; lý thuyết kéo dài PR/QT khi ức chế CYP quá mức."],
                "antidote": "Không có.",
                "treatment": [
                    "Than hoạt nếu mới uống.",
                    "Điều trị hỗ trợ; theo dõi ECG, men gan."
                ],
                "monitoring": "ECG, men gan, dấu hiệu tương tác thuốc kèm."
            },
            "reversal_agents": {
                "available": False,
                "agents": [],
                "notes": "Không có antidote đặc hiệu. Điều trị quá liều chủ yếu là than hoạt nếu mới uống, điều trị hỗ trợ, theo dõi ECG và men gan."
            },
            "administration_instructions": {
                "oral": {
                    "with_food": "PHẢI uống với thức ăn để tăng hấp thu.",
                    "timing": "QD (naive) hoặc BID (kháng); dùng kèm booster cùng lúc."
                }
            },
            "references": {
                "primary_sources": [
                    "DHHS/CDC HIV Treatment Guidelines",
                    "WHO 2024 HIV",
                    "IAS-USA 2024"
                ],
                "last_updated": "2025-12-24",
                "evidence_level": "High – guideline-based"
            }
        },

}

__all__ = ['PROTEASE_INHIBITORS_ARVS']
