"""
HIV Antiretrovirals - Nrti
"""
from typing import Dict, Any


NRTI_ARVS: Dict[str, Dict[str, Any]] = {
        "Emtricitabine (FTC)": {
            "group": "Antiviral - Nucleoside reverse transcriptase inhibitor (NRTI)",
            "vietnamese_name": "Emtricitabine (FTC)",
            "administration": ["PO"],
            "indications": [
                "Điều trị HIV-1 kết hợp đa thuốc (backbone NRTI).",
                "Dự phòng trước phơi nhiễm (PrEP) khi kết hợp tenofovir (TDF hoặc TAF).",
                "Hỗ trợ điều trị HBV (hoạt tính với HBV, nhưng không dùng đơn trị).",
            ],
            "contraindications": ["Dị ứng với emtricitabine."],
            "dosage": {
                "hiv": "200mg PO mỗi ngày.",
                "prep": "200mg PO mỗi ngày khi dùng với TDF/TAF.",
                "notes": "Không dùng chung với lamivudine (3TC).",
            },
            "renal_adjustment": {
                "normal": "Không cần chỉnh.",
                "30_60": "200mg mỗi 48 giờ.",
                "under_30": "Cân nhắc giảm còn 200mg mỗi 72–96 giờ; chạy thận: sau lọc.",
            },
            "side_effects": [
                "Nhức đầu, mệt, buồn nôn (nhẹ).",
                "Tăng sắc tố lòng bàn tay/bàn chân (hiếm).",
                "Hiếm: toan lactic/gan to nhiễm mỡ.",
            ],
            "interactions": [
                "Ít qua CYP; tránh phối hợp 3TC (trùng cơ chế).",
            ],
            "pregnancy": "B: an toàn, khuyến cáo trong thai kỳ.",
            "risk_flags": {
                "high_alert": False,
                "narrow_therapeutic_index": False,
                "organ_toxicity": {"hepatic": True},
                "icu_critical_care_only": False,
                "look_alike_sound_alike": ["FTC vs 3TC"]
            },
            "guideline_tags": [
                "WHO 2024 HIV/PrEP",
                "DHHS/CDC HIV 2024"
            ],
            "mechanism_of_action": (
                "Cytidine analog; phosphoryl hóa thành FTC-TP, ức chế cạnh tranh reverse transcriptase HIV-1 "
                "và kết thúc chuỗi DNA; có hoạt tính với HBV."
            ),
            "monitoring": [
                "Creatinine/eGFR để chỉnh liều.",
                "Men gan, HBV DNA nếu đồng nhiễm HBV.",
                "HIV RNA và CD4 theo phác đồ.",
            ],
            "precautions": [
                "Không phối hợp với lamivudine.",
                "Nguy cơ bùng phát HBV khi ngừng ở bệnh nhân đồng nhiễm.",
            ],
            "pharmacokinetics": {
                "half_life": "10 giờ (huyết tương), 39 giờ (nội bào).",
                "onset": "Cmax ~1–2 giờ.",
                "duration": "Dùng 1 lần/ngày.",
                "protein_binding": "<4%.",
                "clearance": "Thận (bài tiết ống thận).",
            },
            "storage": "20–25°C, tránh ẩm.",
            "black_box_warnings": (
                "Nguy cơ toan lactic/gan to nhiễm mỡ (hiếm, nhóm NRTI). "
                "Bùng phát HBV khi ngừng ở bệnh nhân đồng nhiễm HBV."
            ),
            "drug_interactions": {
                "major": [],
                "moderate": [
                    {
                        "drug": "Lamivudine",
                        "mechanism": "Trùng cơ chế (cytidine analog).",
                        "effect": "Không tăng hiệu quả, nguy cơ kháng chéo.",
                        "management": "Không phối hợp FTC và 3TC chung phác đồ.",
                    }
                ],
                "minor": [],
            },
            "contraindications_detail": {
                "tuyệt_đối": ["Quá mẫn với emtricitabine."],
                "tương_đối": [
                    "Đồng nhiễm HBV: thận trọng khi ngừng, cần kế hoạch duy trì kháng HBV.",
                ],
            },
            "pregnancy_lactation": {
                "fda_category": "B",
                "pregnancy_details": "Được khuyến cáo trong phác đồ thai kỳ (WHO/CDC).",
                "lactation": {
                    "safety": "Caution",
                    "details": "Bài tiết vào sữa thấp; WHO cho phép tiếp tục điều trị khi cho bú.",
                    "recommendation": "Có thể tiếp tục; theo dõi chức năng thận/men gan.",
                },
            },
            "hepatic_adjustment": {
                "mild": "Không cần chỉnh.",
                "moderate": "Không cần chỉnh; theo dõi men gan nếu đồng nhiễm HBV.",
                "severe": "Dữ liệu hạn chế; theo dõi sát.",
                "notes": "Chủ yếu thải trừ qua thận.",
            },
            "overdose_management": {
                "symptoms": ["Buồn nôn, mệt; hiếm toan lactic."],
                "antidote": "Không có antidote đặc hiệu.",
                "treatment": [
                    "Ngừng thuốc, hỗ trợ triệu chứng.",
                    "Chạy thận loại bỏ một phần FTC.",
                ],
                "monitoring": "Men gan, lactate, chức năng thận.",
            },
            "reversal_agents": None,
            "administration_instructions": {
                "oral": {
                    "with_food": "Có thể uống cùng hoặc không cùng thức ăn.",
                    "timing": "1 lần/ngày; dùng cố định với nền NRTI/INSTI.",
                }
            },
            "references": {
                "primary_sources": [
                    "WHO 2024 HIV/PrEP",
                    "DHHS/CDC HIV Treatment Guidelines"
                ],
                "last_updated": "2025-12-24",
                "evidence_level": "High – guideline-based",
            },
        },

        "Lamivudine (3TC)": {
            "group": "Antiviral - Nucleoside reverse transcriptase inhibitor (NRTI)",
            "vietnamese_name": "Lamivudine (3TC)",
            "administration": ["PO"],
            "indications": [
                "Điều trị HIV-1 kết hợp đa thuốc (backbone NRTI).",
                "Điều trị HBV mạn (đơn trị ít được ưu tiên do kháng sớm).",
            ],
            "contraindications": ["Dị ứng với lamivudine."],
            "dosage": {
                "hiv": "300mg PO mỗi ngày (hoặc 150mg x 2 lần/ngày).",
                "hbv": "100mg PO mỗi ngày (liều HBV riêng).",
                "notes": "Điều chỉnh liều theo chức năng thận; giữ liều đủ khi kết hợp với DTG/TDF.",
            },
            "renal_adjustment": {
                "normal": "Không cần chỉnh.",
                "30_60": "150mg mỗi ngày.",
                "under_30": "50–100mg mỗi ngày tùy CrCl; chạy thận: 25–50mg sau lọc.",
            },
            "side_effects": [
                "Thường nhẹ: nhức đầu, buồn nôn, mệt.",
                "Hiếm: toan lactic/gan to nhiễm mỡ (nhóm NRTI).",
            ],
            "interactions": [
                "Ít tương tác qua CYP; chú ý phối hợp với emtricitabine (trùng cơ chế, không dùng chung).",
            ],
            "pregnancy": "B: an toàn, được khuyến cáo trong thai kỳ.",
            "risk_flags": {
                "high_alert": False,
                "narrow_therapeutic_index": False,
                "organ_toxicity": {"hepatic": True},
                "icu_critical_care_only": False,
                "look_alike_sound_alike": ["3TC vs FTC"]
            },
            "guideline_tags": [
                "WHO 2024 HIV",
                "DHHS/CDC HIV 2024",
                "AASLD/EASL HBV 2023-2024"
            ],
            "mechanism_of_action": (
                "Nucleoside analog cytidine; phosphoryl hóa thành 3TC-TP, "
                "ức chế cạnh tranh HIV-1 reverse transcriptase và kết thúc chuỗi DNA virus; "
                "hoạt tính với HBV."
            ),
            "monitoring": [
                "Creatinine/eGFR để chỉnh liều.",
                "Men gan (ALT/AST), HBV DNA nếu đồng nhiễm HBV.",
                "HIV RNA và CD4 theo phác đồ.",
            ],
            "precautions": [
                "Bùng phát HBV khi ngừng ở người đồng nhiễm HBV.",
                "Điều chỉnh liều theo thận để tránh tích lũy.",
            ],
            "pharmacokinetics": {
                "half_life": "10–15 giờ (huyết tương); 16–19 giờ (nội bào).",
                "onset": "Nhanh, nồng độ đỉnh 1–1.5 giờ.",
                "duration": "Dùng 1–2 lần/ngày.",
                "protein_binding": "<36%.",
                "clearance": "Thải trừ qua thận (bài tiết ống thận).",
            },
            "storage": "Bảo quản 20–25°C, tránh ẩm.",
            "black_box_warnings": (
                "Nguy cơ toan lactic và gan to nhiễm mỡ (hiếm, nhóm NRTI). "
                "Bùng phát viêm gan B khi ngừng thuốc ở bệnh nhân đồng nhiễm HBV."
            ),
            "drug_interactions": {
                "major": [],
                "moderate": [
                    {
                        "drug": "Emtricitabine",
                        "mechanism": "Trùng cơ chế và cấu trúc (cytidine analog).",
                        "effect": "Không tăng hiệu quả, nguy cơ kháng chéo.",
                        "management": "Không phối hợp 3TC và FTC chung phác đồ.",
                    }
                ],
                "minor": [],
            },
            "contraindications_detail": {
                "tuyệt_đối": ["Quá mẫn với lamivudine."],
                "tương_đối": [
                    "Đồng nhiễm HBV: thận trọng khi ngừng, cần kế hoạch duy trì thuốc kháng HBV.",
                ],
            },
            "pregnancy_lactation": {
                "fda_category": "B",
                "pregnancy_details": "Được khuyến cáo trong phác đồ thai kỳ (WHO/CDC).",
                "lactation": {
                    "safety": "Caution",
                    "details": "Bài tiết vào sữa; WHO cho phép tiếp tục điều trị khi cho bú.",
                    "recommendation": "Có thể tiếp tục; theo dõi chức năng thận và men gan.",
                },
            },
            "hepatic_adjustment": {
                "mild": "Không cần chỉnh.",
                "moderate": "Không cần chỉnh; theo dõi men gan nếu đồng nhiễm HBV.",
                "severe": "Dữ liệu hạn chế; theo dõi sát, ưu tiên duy trì để tránh bùng phát HBV.",
                "notes": "Chủ yếu thải trừ qua thận.",
            },
            "overdose_management": {
                "symptoms": ["Buồn nôn, mệt, hiếm gặp toan lactic."],
                "antidote": "Không có antidote đặc hiệu.",
                "treatment": [
                    "Ngừng thuốc, điều trị hỗ trợ, theo dõi lactate và men gan.",
                    "Chạy thận loại bỏ một phần lamivudine.",
                ],
                "monitoring": "Dấu hiệu lâm sàng, men gan, lactate, chức năng thận.",
            },
            "reversal_agents": None,
            "administration_instructions": {
                "oral": {
                    "with_food": "Có thể uống cùng hoặc không cùng thức ăn.",
                    "timing": "Uống 1 lần/ngày (hoặc 2 lần/ngày 150mg).",
                }
            },
            "references": {
                "primary_sources": [
                    "WHO Consolidated Guidelines on HIV (2024)",
                    "DHHS/CDC HIV Treatment Guidelines",
                ],
                "last_updated": "2025-12-24",
                "evidence_level": "High – guideline-based",
            },
        },

        "Tenofovir alafenamide (TAF)": {
            "group": "Antiviral - Nucleotide reverse transcriptase inhibitor (NRTI)",
            "vietnamese_name": "Tenofovir alafenamide (TAF)",
            "administration": ["PO"],
            "indications": [
                "Điều trị HIV-1 (kết hợp đa thuốc).",
                "Điều trị HBV mạn (liều HBV riêng).",
                "PrEP khi kết hợp FTC (không cho receptive vaginal sex theo nhãn cũ; cập nhật cân nhắc theo guideline mới nếu có).",
            ],
            "contraindications": ["Dị ứng với TAF."],
            "dosage": {
                "hiv": "10–25mg PO mỗi ngày tùy nền (với booster hoặc không).",
                "hbv": "25mg PO mỗi ngày, uống với thức ăn.",
                "notes": "Uống với thức ăn; không dùng đơn trị HIV.",
            },
            "renal_adjustment": {
                "normal": "Không cần chỉnh.",
                "30_60": "Không cần chỉnh; theo dõi thận.",
                "under_30": "Tránh nếu CrCl <15 không lọc; chạy thận: dữ liệu hạn chế.",
            },
            "side_effects": [
                "Buồn nôn, đau đầu.",
                "Ít ảnh hưởng mật độ xương/thận hơn TDF, nhưng vẫn cần theo dõi.",
            ],
            "interactions": [
                "P-gp inducers (rifampin, carbamazepine) giảm nồng độ.",
                "Boosted PIs/cobicistat có thể tăng phơi nhiễm TAF (theo nhãn).",
            ],
            "pregnancy": "Có thể dùng; dữ liệu đang tăng, ưu tiên TDF nếu cần bằng chứng lâu dài.",
            "risk_flags": {
                "high_alert": False,
                "narrow_therapeutic_index": False,
                "organ_toxicity": {"renal": True, "bone": True},
                "icu_critical_care_only": False,
                "look_alike_sound_alike": ["TDF vs TAF"]
            },
            "guideline_tags": [
                "WHO 2024 HIV/PrEP",
                "DHHS/CDC HIV 2024",
                "AASLD/EASL HBV 2024"
            ],
            "mechanism_of_action": (
                "Tiền chất tenofovir thế hệ mới, được hoạt hóa chủ yếu trong tế bào lympho/gan, "
                "ức chế cạnh tranh reverse transcriptase HIV-1 và HBV, gây kết thúc chuỗi DNA."
            ),
            "monitoring": [
                "Creatinine/eGFR, phospho (ít hơn TDF nhưng vẫn cần).",
                "HBV DNA, ALT nếu điều trị HBV.",
                "HIV RNA, CD4 theo phác đồ.",
            ],
            "precautions": [
                "Không dùng đơn trị HIV.",
                "Tránh cảm ứng mạnh P-gp (rifampin, carbamazepine).",
                "Theo dõi thận và xương nếu dùng kéo dài.",
                "Bùng phát HBV khi ngừng ở người đồng nhiễm.",
            ],
            "pharmacokinetics": {
                "half_life": "~0.5 giờ (huyết tương tiền thuốc); chất chuyển hóa nội bào kéo dài.",
                "onset": "Nồng độ nội bào đạt đỉnh trong vài giờ.",
                "duration": "1 lần/ngày.",
                "protein_binding": "~80%.",
                "clearance": "Gan (esterase, cathepsin A); thận thải trừ tenofovir mức thấp hơn TDF.",
            },
            "storage": "Bảo quản 20–25°C, tránh ẩm.",
            "black_box_warnings": "Bùng phát HBV khi ngừng; toan lactic/gan to nhiễm mỡ (hiếm, nhóm NRTI).",
            "drug_interactions": {
                "major": [
                    {
                        "drug": "Rifampin, carbamazepine, phenytoin, St. John’s wort",
                        "mechanism": "Cảm ứng P-gp làm giảm hấp thu/ phơi nhiễm TAF.",
                        "effect": "Giảm hiệu quả điều trị.",
                        "management": "Tránh phối hợp.",
                    }
                ],
                "moderate": [
                    {
                        "drug": "Boosted PIs/cobicistat",
                        "mechanism": "Ức chế P-gp tăng phơi nhiễm TAF.",
                        "effect": "Tăng nồng độ tenofovir; có thể tăng độc tính thận.",
                        "management": "Theo dõi chức năng thận; cân nhắc nền không booster nếu phù hợp.",
                    }
                ],
                "minor": [],
            },
            "contraindications_detail": {
                "tuyệt_đối": ["Quá mẫn TAF."],
                "tương_đối": [
                    "Suy thận nặng không lọc.",
                    "Đồng nhiễm HBV: thận trọng khi ngừng.",
                ],
            },
            "pregnancy_lactation": {
                "fda_category": "Not classified; kinh nghiệm hạn chế hơn TDF",
                "pregnancy_details": "Có thể cân nhắc; TDF vẫn là chuẩn có dữ liệu nhiều.",
                "lactation": {
                    "safety": "Caution",
                    "details": "Dữ liệu hạn chế; theo dõi trẻ.",
                    "recommendation": "Cân nhắc lợi ích/nguy cơ; TDF có dữ liệu nhiều hơn.",
                },
            },
            "hepatic_adjustment": {
                "mild": "Không cần chỉnh.",
                "moderate": "Thận trọng.",
                "severe": "Dữ liệu hạn chế; theo dõi sát.",
                "notes": "Thải chủ yếu qua thận sau chuyển hóa; suy gan có thể tăng phơi nhiễm tiền thuốc.",
            },
            "overdose_management": {
                "symptoms": ["Buồn nôn, đau đầu; lý thuyết độc thận/xương hiếm."],
                "antidote": "Không có.",
                "treatment": [
                    "Điều trị hỗ trợ; than hoạt nếu mới uống.",
                    "Theo dõi thận, điện giải.",
                ],
                "monitoring": "Creatinine, phospho, men gan.",
            },
            "reversal_agents": None,
            "administration_instructions": {
                "oral": {
                    "with_food": "Nên uống với thức ăn để tối ưu hấp thu.",
                    "timing": "1 lần/ngày; dùng cố định với nền ART.",
                }
            },
            "references": {
                "primary_sources": [
                    "WHO 2024 HIV/PrEP",
                    "DHHS/CDC HIV Guidelines",
                    "AASLD/EASL HBV 2024"
                ],
                "last_updated": "2025-12-24",
                "evidence_level": "High – guideline-based",
            },
        },

        "Tenofovir alafenamide/Emtricitabine (TAF/FTC)": {
            "group": "Antiviral - NRTI fixed-dose combination",
            "vietnamese_name": "TAF/FTC (Descovy và tương đương)",
            "administration": ["PO"],
            "indications": [
                "Điều trị HIV-1 (backbone NRTI) khi kết hợp INSTI/NNRTI/PI.",
                "PrEP (không cho receptive vaginal sex theo nhãn cũ; theo dõi cập nhật guideline)."
            ],
            "contraindications": [
                "Dị ứng với thành phần.",
                "eGFR <30 mL/phút (theo nhãn)."
            ],
            "dosage": {
                "hiv_prep": "TAF 25mg + FTC 200mg PO mỗi ngày (uống với thức ăn).",
                "notes": "Ưu tiên khi nguy cơ thận/xương cao; không dùng đơn trị HIV."
            },
            "renal_adjustment": {
                "normal": "Không cần chỉnh.",
                "30_60": "Không cần chỉnh; theo dõi thận.",
                "under_30": "Tránh nếu eGFR <30 (không lọc)."
            },
            "side_effects": [
                "Buồn nôn, đau đầu.",
                "Nguy cơ thận/xương thấp hơn TDF nhưng vẫn cần theo dõi."
            ],
            "interactions": [
                "P-gp inducers (rifampin, carbamazepine) giảm nồng độ TAF.",
                "Boosted PI/cobicistat tăng phơi nhiễm TAF; theo dõi thận."
            ],
            "pregnancy": "Có thể dùng; dữ liệu ít hơn TDF, TDF vẫn chuẩn trong thai kỳ.",
            "risk_flags": {
                "high_alert": False,
                "narrow_therapeutic_index": False,
                "organ_toxicity": {"renal": True, "bone": True},
                "icu_critical_care_only": False,
                "look_alike_sound_alike": ["TDF vs TAF"]
            },
            "guideline_tags": [
                "WHO 2024 HIV/PrEP",
                "DHHS/CDC HIV 2024"
            ],
            "mechanism_of_action": "Nucleotide + nucleoside analog ức chế reverse transcriptase HIV-1, kết thúc chuỗi DNA; hoạt tính HBV.",
            "monitoring": [
                "Creatinine/eGFR, phospho.",
                "HBV DNA/ALT nếu đồng nhiễm.",
                "HIV RNA, CD4; test HIV định kỳ trong PrEP."
            ],
            "precautions": [
                "Tránh cảm ứng mạnh P-gp.",
                "Không dùng đơn trị HIV.",
                "Theo dõi thận/xương dù nguy cơ thấp hơn TDF."
            ],
            "pharmacokinetics": {
                "half_life": "~0.5h tiền thuốc; tenofovir nội bào kéo dài.",
                "onset": "Nồng độ nội bào đạt trong vài giờ.",
                "duration": "1 lần/ngày.",
                "protein_binding": "~80% (TAF).",
                "clearance": "Gan (esterase/cathepsin A), thận thải tenofovir mức thấp."
            },
            "storage": "20–25°C, tránh ẩm.",
            "black_box_warnings": "Bùng phát HBV khi ngừng; toan lactic/gan to nhiễm mỡ (hiếm).",
            "drug_interactions": {
                "major": [
                    {
                        "drug": "Rifampin, carbamazepine, phenytoin, St. John’s wort",
                        "mechanism": "Cảm ứng P-gp giảm nồng độ TAF.",
                        "effect": "Giảm hiệu quả.",
                        "management": "Tránh."
                    }
                ],
                "moderate": [
                    {
                        "drug": "Boosted PI/cobicistat",
                        "mechanism": "Ức chế P-gp tăng phơi nhiễm TAF.",
                        "effect": "Tăng nguy cơ độc thận.",
                        "management": "Theo dõi thận; cân nhắc nền không booster."
                    }
                ],
                "minor": []
            },
            "contraindications_detail": {
                "tuyệt_đối": ["Quá mẫn thành phần."],
                "tương_đối": [
                    "eGFR <30 mL/phút.",
                    "Đồng nhiễm HBV: thận trọng khi ngừng."
                ]
            },
            "pregnancy_lactation": {
                "fda_category": "Not classified; dữ liệu hạn chế",
                "pregnancy_details": "Có thể cân nhắc; TDF nhiều bằng chứng hơn.",
                "lactation": {
                    "safety": "Caution",
                    "details": "Dữ liệu hạn chế.",
                    "recommendation": "Đánh giá lợi ích/nguy cơ."
                }
            },
            "hepatic_adjustment": {
                "mild": "Không cần chỉnh.",
                "moderate": "Thận trọng.",
                "severe": "Dữ liệu hạn chế.",
                "notes": "Thải chủ yếu qua thận sau chuyển hóa; suy gan có thể tăng phơi nhiễm tiền thuốc."
            },
            "overdose_management": {
                "symptoms": ["Buồn nôn, đau đầu; lý thuyết độc thận hiếm."],
                "antidote": "Không có.",
                "treatment": [
                    "Điều trị hỗ trợ; than hoạt nếu mới uống.",
                    "Theo dõi thận."
                ],
                "monitoring": "Creatinine, phospho, men gan."
            },
            "reversal_agents": None,
            "administration_instructions": {
                "oral": {
                    "with_food": "Nên uống với thức ăn.",
                    "timing": "1 lần/ngày."
                }
            },
            "references": {
                "primary_sources": [
                    "WHO 2024 HIV/PrEP",
                    "DHHS/CDC HIV Treatment Guidelines"
                ],
                "last_updated": "2025-12-24",
                "evidence_level": "High – guideline-based"
            }
        },

        "Tenofovir disoproxil fumarate (TDF)": {
            "group": "Antiviral - Nucleotide reverse transcriptase inhibitor (NRTI)",
            "vietnamese_name": "Tenofovir disoproxil fumarate (TDF)",
            "administration": ["PO"],
            "indications": [
                "Điều trị HIV-1 kết hợp đa thuốc (backbone NRTI).",
                "Dự phòng trước phơi nhiễm (PrEP) khi kết hợp emtricitabine/lamivudine.",
                "Điều trị viêm gan B mạn (HBV) – ưu tiên khi đồng nhiễm HIV/HBV.",
            ],
            "contraindications": [
                "Dị ứng với tenofovir hoặc tá dược.",
                "CrCl <30 mL/phút nếu không thể theo dõi sát hoặc hiệu chỉnh liều.",
            ],
            "dosage": {
                "hiv_hbv": "300mg PO mỗi ngày, uống cùng hoặc không cùng thức ăn.",
                "prep": "300mg PO mỗi ngày (thường kết hợp emtricitabine).",
                "post_exposure_prophylaxis": "300mg PO mỗi ngày, kết hợp đa thuốc trong 28 ngày.",
                "notes": "Uống nhiều nước; theo dõi CrCl và phospho mỗi 3-6 tháng.",
            },
            "renal_adjustment": {
                "normal": "Không cần chỉnh liều.",
                "30_60": "300mg mỗi 48 giờ.",
                "under_30": "Tránh dùng nếu có lựa chọn khác; nếu bắt buộc: mỗi 72–96 giờ và theo dõi sát.",
            },
            "side_effects": [
                "Tăng creatinine, giảm phospho máu; hiếm gặp hội chứng Fanconi (độc thận ống lượn gần).",
                "Giảm mật độ xương (osteopenia/osteoporosis).",
                "Buồn nôn, mệt mỏi, đau đầu nhẹ.",
            ],
            "interactions": [
                "Thuốc độc thận (aminoglycoside, NSAID liều cao): tăng nguy cơ độc thận.",
                "Didanosine: tăng nồng độ didanosine, tăng độc tính; tránh nếu có thể.",
            ],
            "pregnancy": "B: có thể dùng trong thai kỳ khi lợi ích vượt nguy cơ; an toàn trong PrEP/điều trị HIV/HBV.",
            "risk_flags": {
                "high_alert": False,
                "narrow_therapeutic_index": False,
                "organ_toxicity": {"renal": True, "bone": True},
                "icu_critical_care_only": False,
                "look_alike_sound_alike": ["TDF vs TAF"]
            },
            "guideline_tags": [
                "WHO 2024 HIV/PrEP",
                "DHHS/CDC HIV 2024",
                "AASLD/EASL HBV 2023-2024"
            ],
            "mechanism_of_action": (
                "Tiền chất nucleotide adenosine monophosphate; phosphoryl hóa thành tenofovir diphosphate, "
                "ức chế cạnh tranh HIV-1 reverse transcriptase và gây kết thúc chuỗi DNA virus. "
                "Hoạt tính với HIV-1, HBV."
            ),
            "monitoring": [
                "Creatinine, eGFR/CrCl mỗi 3-6 tháng.",
                "Phospho, dấu hiệu hội chứng Fanconi (tiểu nhiều, yếu cơ, hạ phospho).",
                "HBV DNA/HIV RNA và CD4 theo phác đồ điều trị.",
            ],
            "precautions": [
                "Độc thận ống lượn gần: tránh phối hợp nhiều thuốc độc thận; uống đủ nước.",
                "Giảm mật độ xương: cân nhắc bổ sung calcium/vitamin D, đánh giá DEXA nếu nguy cơ cao.",
                "Bùng phát HBV khi ngừng: giảm dần hoặc chuyển thuốc chống HBV nếu đồng nhiễm.",
            ],
            "pharmacokinetics": {
                "half_life": "Kỳ tế bào ~60 giờ (dạng hoạt tính); huyết tương ~17 giờ.",
                "onset": "Vài giờ sau liều đầu.",
                "duration": "Dùng 1 lần/ngày nhờ tích lũy trong tế bào.",
                "protein_binding": "<1%.",
                "clearance": "Thải trừ chủ yếu qua thận (lọc cầu thận và bài tiết ống thận).",
            },
            "storage": "Bảo quản ở 20–25°C, giữ kín, tránh ẩm.",
            "black_box_warnings": (
                "Nguy cơ toan lactic và gan to nhiễm mỡ (hiếm, lớp NRTI). "
                "Bùng phát viêm gan B nặng khi ngừng thuốc ở bệnh nhân đồng nhiễm HBV."
            ),
            "drug_interactions": {
                "major": [
                    {
                        "drug": "Didanosine",
                        "mechanism": "TDF làm tăng nồng độ didanosine và độc tính ty thể.",
                        "effect": "Tăng nguy cơ viêm tụy, nhiễm toan lactic, độc tính thần kinh.",
                        "management": "Tránh phối hợp nếu có thể; nếu bắt buộc, giảm liều didanosine và theo dõi sát.",
                    }
                ],
                "moderate": [
                    {
                        "drug": "Thuốc độc thận (NSAID liều cao, aminoglycoside, amphotericin B)",
                        "mechanism": "Tác dụng cộng dồn độc thận.",
                        "effect": "Tăng nguy cơ suy thận, hội chứng Fanconi.",
                        "management": "Tránh phối hợp; nếu dùng, theo dõi creatinine, phospho chặt chẽ.",
                    }
                ],
                "minor": [],
            },
            "contraindications_detail": {
                "tuyệt_đối": ["Quá mẫn với tenofovir."],
                "tương_đối": [
                    "CrCl <30 mL/phút hoặc đang chạy thận (cân nhắc TAF hoặc thuốc khác).",
                    "Loãng xương/giảm mật độ xương nặng.",
                ],
            },
            "pregnancy_lactation": {
                "fda_category": "B",
                "pregnancy_details": "Được khuyến cáo trong phác đồ bầu bí (WHO/CDC).",
                "lactation": {
                    "safety": "Caution",
                    "details": "Bài tiết vào sữa thấp; WHO cho phép tiếp tục điều trị khi cho bú.",
                    "recommendation": "Có thể tiếp tục nếu cần điều trị/PrEP; theo dõi chức năng thận mẹ.",
                },
            },
            "hepatic_adjustment": {
                "mild": "Không cần chỉnh liều.",
                "moderate": "Không cần chỉnh liều; thận trọng nếu đồng thời suy thận.",
                "severe": "Dữ liệu hạn chế; theo dõi sát, ưu tiên thuốc khác nếu xơ gan mất bù.",
                "notes": "Chủ yếu thải qua thận, ít chuyển hóa gan.",
            },
            "overdose_management": {
                "symptoms": [
                    "Tăng creatinine, hạ phospho, dấu hiệu Fanconi.",
                    "Buồn nôn, đau bụng, mệt mỏi.",
                ],
                "antidote": "Không có antidote đặc hiệu.",
                "treatment": [
                    "Ngừng thuốc, bù dịch, điều chỉnh điện giải (phospho, kali).",
                    "Hỗ trợ thận; lọc máu loại bỏ một phần tenofovir.",
                ],
                "monitoring": "Creatinine, phospho, điện giải, nước tiểu, dấu hiệu lâm sàng.",
            },
            "reversal_agents": None,
            "administration_instructions": {
                "oral": {
                    "with_food": "Có thể uống cùng hoặc không cùng thức ăn.",
                    "timing": "Uống 1 lần/ngày, cố định giờ để duy trì nồng độ.",
                }
            },
            "references": {
                "primary_sources": [
                    "WHO Consolidated Guidelines on HIV Prevention, Testing, Treatment (2024)",
                    "DHHS/CDC HIV Treatment Guidelines",
                    "HBV treatment guidelines (AASLD/EASL)",
                ],
                "last_updated": "2025-12-24",
                "evidence_level": "High – guideline-based",
            },
        },

        "Tenofovir disoproxil fumarate/Emtricitabine (TDF/FTC)": {
            "group": "Antiviral - NRTI fixed-dose combination",
            "vietnamese_name": "TDF/FTC (Truvada và tương đương)",
            "administration": ["PO"],
            "indications": [
                "Điều trị HIV-1 (backbone NRTI) khi kết hợp INSTI/NNRTI/PI.",
                "Dự phòng trước phơi nhiễm (PrEP).",
                "Hỗ trợ phòng lây truyền mẹ-con khi phối hợp phác đồ đầy đủ."
            ],
            "contraindications": [
                "Dị ứng với bất kỳ thành phần nào.",
                "CrCl <30 mL/phút (trừ khi có giám sát rất sát/điều chỉnh đặc biệt)."
            ],
            "dosage": {
                "hiv": "TDF 300mg + FTC 200mg PO mỗi ngày.",
                "prep": "TDF 300mg + FTC 200mg PO mỗi ngày.",
                "notes": "Uống cố định giờ; uống với nước, có thể cùng hoặc không cùng thức ăn."
            },
            "renal_adjustment": {
                "normal": "Không cần chỉnh.",
                "30_60": "Uống mỗi 48 giờ.",
                "under_30": "Tránh; chạy thận: mỗi 7 ngày sau lọc (chỉ khi buộc phải dùng, theo guideline)."
            },
            "side_effects": [
                "Buồn nôn, nhức đầu, mệt.",
                "Tăng creatinine, giảm phospho (TDF).",
                "Giảm mật độ xương (TDF)."
            ],
            "interactions": [
                "Thuốc độc thận (aminoglycoside, NSAID liều cao): tăng độc thận.",
                "Boosted PI/cobicistat: tăng phơi nhiễm TDF → tăng nguy cơ thận/xương."
            ],
            "pregnancy": "TDF/FTC được khuyến cáo an toàn trong thai kỳ và PrEP.",
            "risk_flags": {
                "high_alert": False,
                "narrow_therapeutic_index": False,
                "organ_toxicity": {"renal": True, "bone": True},
                "icu_critical_care_only": False,
                "look_alike_sound_alike": ["TDF vs TAF"]
            },
            "guideline_tags": [
                "WHO 2024 HIV/PrEP",
                "DHHS/CDC HIV 2024"
            ],
            "mechanism_of_action": (
                "Kết hợp nucleotide (TDF) và nucleoside (FTC) ức chế cạnh tranh HIV reverse transcriptase, "
                "gây kết thúc chuỗi DNA virus; có hoạt tính với HBV."
            ),
            "monitoring": [
                "Creatinine/eGFR, phospho mỗi 3–6 tháng.",
                "HBV DNA/ALT nếu đồng nhiễm.",
                "HIV RNA, CD4; xét nghiệm HIV định kỳ trong PrEP."
            ],
            "precautions": [
                "Không phối hợp thêm 3TC/FTC khác (trùng cơ chế).",
                "Theo dõi thận/xương; cân nhắc TAF/FTC nếu nguy cơ cao.",
                "Bùng phát HBV khi ngừng ở người đồng nhiễm."
            ],
            "pharmacokinetics": {
                "half_life": "TDF ~17h huyết tương; FTC 10h huyết tương, 39h nội bào.",
                "onset": "Nồng độ đỉnh 1–2h.",
                "duration": "1 lần/ngày.",
                "protein_binding": "TDF <1%; FTC <4%.",
                "clearance": "Thận (lọc cầu thận/bài tiết ống thận)."
            },
            "storage": "20–25°C, khô ráo.",
            "black_box_warnings": "Toan lactic/gan to nhiễm mỡ (nhóm NRTI, hiếm); bùng phát HBV khi ngừng.",
            "drug_interactions": {
                "major": [
                    {
                        "drug": "Thuốc độc thận (aminoglycoside, amphotericin B, cisplatin, high-dose NSAID)",
                        "mechanism": "Cộng hưởng độc thận.",
                        "effect": "Tăng nguy cơ suy thận.",
                        "management": "Tránh nếu có thể; theo dõi creatinine/eGFR sát."
                    }
                ],
                "moderate": [
                    {
                        "drug": "Boosted PI/cobicistat",
                        "mechanism": "Tăng phơi nhiễm TDF qua ức chế P-gp.",
                        "effect": "Tăng độc thận/xương.",
                        "management": "Theo dõi thận; cân nhắc TAF/FTC nếu phù hợp."
                    }
                ],
                "minor": []
            },
            "contraindications_detail": {
                "tuyệt_đối": ["Quá mẫn thành phần."],
                "tương_đối": [
                    "CrCl <30 mL/phút hoặc chạy thận (chỉ dùng nếu buộc phải và theo guideline).",
                    "Nguy cơ loãng xương cao."
                ]
            },
            "pregnancy_lactation": {
                "fda_category": "B (TDF, FTC)",
                "pregnancy_details": "Khuyến cáo dùng trong thai kỳ (điều trị/PrEP).",
                "lactation": {
                    "safety": "Compatible",
                    "details": "Bài tiết ít vào sữa; được phép tiếp tục.",
                    "recommendation": "Theo dõi trẻ sơ sinh nếu dùng kéo dài."
                }
            },
            "hepatic_adjustment": {
                "mild": "Không cần chỉnh.",
                "moderate": "Không cần chỉnh.",
                "severe": "Thận trọng; dữ liệu hạn chế.",
                "notes": "Thải qua thận; suy gan ít ảnh hưởng PK."
            },
            "overdose_management": {
                "symptoms": ["Buồn nôn, đau đầu; lý thuyết độc thận/xương."],
                "antidote": "Không có.",
                "treatment": [
                    "Điều trị hỗ trợ; theo dõi điện giải.",
                    "Lọc máu loại bỏ TDF/FTC một phần."
                ],
                "monitoring": "Creatinine, phospho, men gan, lactate."
            },
            "reversal_agents": None,
            "administration_instructions": {
                "oral": {
                    "with_food": "Có thể với hoặc không.",
                    "timing": "1 lần/ngày; PrEP cần tuân thủ liên tục."
                }
            },
            "references": {
                "primary_sources": [
                    "WHO 2024 HIV/PrEP",
                    "DHHS/CDC HIV Treatment Guidelines"
                ],
                "last_updated": "2025-12-24",
                "evidence_level": "High – guideline-based"
            }
        },

}

__all__ = ['NRTI_ARVS']
