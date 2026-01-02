"""
HIV Antiretrovirals - Integrase Inhibitors
"""
from typing import Dict, Any


INTEGRASE_INHIBITORS_ARVS: Dict[str, Dict[str, Any]] = {
        "Bictegravir (BIC)": {
            "group": "Antiviral - Integrase strand transfer inhibitor (INSTI)",
            "vietnamese_name": "Bictegravir (BIC)",
            "administration": ["PO"],
            "indications": [
                "Điều trị HIV-1 first-line (trong FDC bictegravir/emtricitabine/tenofovir alafenamide).",
            ],
            "contraindications": [
                "Dị ứng với bictegravir.",
                "Dùng đồng thời rifampin (giảm mạnh nồng độ).",
            ],
            "dosage": {
                "standard": "50mg PO mỗi ngày (thường trong FDC).",
                "notes": "Tránh rifampin; antacid/Fe/Ca cần tách liều.",
            },
            "renal_adjustment": {
                "normal": "Không cần chỉnh.",
                "30_60": "Không cần chỉnh.",
                "under_30": "Tránh nếu eGFR <30 khi dùng chung TAF/FTC (theo nhãn FDC).",
            },
            "side_effects": [
                "Buồn nôn, nhức đầu.",
                "Tăng nhẹ creatinine (ức chế OCT2, không giảm GFR thực).",
                "Tăng cân nhẹ.",
            ],
            "interactions": [
                "Rifampin (chống chỉ định), rifabutin (cân nhắc).",
                "Antacid/Fe/Ca: giảm hấp thu, cần tách liều.",
                "Carbamazepine/phenytoin: cảm ứng, giảm nồng độ.",
            ],
            "pregnancy": "Có thể dùng; dữ liệu đang tăng, DTG có nhiều bằng chứng hơn.",
            "risk_flags": {
                "high_alert": False,
                "narrow_therapeutic_index": False,
                "organ_toxicity": {"hepatic": True},
                "icu_critical_care_only": False,
                "look_alike_sound_alike": []
            },
            "guideline_tags": [
                "WHO 2024 HIV",
                "DHHS/CDC HIV 2024",
                "IAS-USA 2024"
            ],
            "mechanism_of_action": (
                "Ức chế integrase strand transfer của HIV-1, ngăn tích hợp DNA virus vào DNA vật chủ."
            ),
            "monitoring": [
                "HIV RNA, CD4.",
                "Creatinine (tăng nhẹ giả tạo).",
                "Men gan nếu đồng nhiễm HBV/HCV.",
            ],
            "precautions": [
                "Tách liều với antacid/Fe/Ca (uống BIC 2 giờ trước hoặc 6 giờ sau).",
                "Tránh rifampin; thận trọng với rifabutin/rifapentine.",
                "Theo dõi tăng cân dài hạn.",
            ],
            "pharmacokinetics": {
                "half_life": "17 giờ.",
                "onset": "Cmax ~2–4 giờ.",
                "duration": "1 lần/ngày.",
                "protein_binding": "~99%.",
                "clearance": "UGT1A1/CYP3A.",
            },
            "storage": "Bảo quản 20–25°C, tránh ẩm.",
            "black_box_warnings": None,
            "drug_interactions": {
                "major": [
                    {
                        "drug": "Rifampin",
                        "mechanism": "Cảm ứng UGT/CYP mạnh, giảm AUC >75%.",
                        "effect": "Thất bại điều trị.",
                        "management": "CHỐNG CHỈ ĐỊNH.",
                    }
                ],
                "moderate": [
                    {
                        "drug": "Antacid/Fe/Ca",
                        "mechanism": "Tạo phức chelat, giảm hấp thu.",
                        "effect": "Giảm AUC.",
                        "management": "Uống BIC 2h trước hoặc 6h sau; hoặc dùng cùng với bữa ăn chứa Fe/Ca được phép theo nhãn.",
                    },
                    {
                        "drug": "Carbamazepine/phenytoin",
                        "mechanism": "Cảm ứng UGT/CYP.",
                        "effect": "Giảm nồng độ BIC.",
                        "management": "Tránh nếu có thể; chọn INSTI khác/điều chỉnh nền.",
                    }
                ],
                "minor": [],
            },
            "contraindications_detail": {
                "tuyệt_đối": ["Quá mẫn", "Rifampin phối hợp"],
                "tương_đối": [
                    "Dùng thuốc cảm ứng mạnh khác (carbamazepine, phenytoin).",
                    "Suy gan trung bình-nặng (dữ liệu hạn chế).",
                ],
            },
            "pregnancy_lactation": {
                "fda_category": "Not classified; dữ liệu đang tăng",
                "pregnancy_details": "Có thể cân nhắc; DTG có bằng chứng rộng hơn.",
                "lactation": {
                    "safety": "Caution",
                    "details": "Dữ liệu hạn chế.",
                    "recommendation": "Đánh giá lợi ích/nguy cơ; theo dõi trẻ.",
                },
            },
            "hepatic_adjustment": {
                "mild": "Không cần chỉnh.",
                "moderate": "Thận trọng.",
                "severe": "Dữ liệu hạn chế; cân nhắc tránh.",
                "notes": "Chuyển hóa qua gan UGT1A1/CYP3A.",
            },
            "overdose_management": {
                "symptoms": ["Buồn nôn, đau đầu; độc tính nặng hiếm."],
                "antidote": "Không có.",
                "treatment": [
                    "Điều trị hỗ trợ; than hoạt nếu mới uống.",
                ],
                "monitoring": "Dấu hiệu sinh tồn, men gan.",
            },
            "reversal_agents": {
                "available": False,
                "agents": [],
                "notes": "Không có antidote đặc hiệu. Điều trị quá liều chủ yếu là điều trị hỗ trợ, than hoạt nếu mới uống."
            },
            "administration_instructions": {
                "oral": {
                    "with_food": "Có thể với hoặc không.",
                    "timing": "1 lần/ngày; tách antacid/Fe/Ca nếu dạng chelat.",
                }
            },
            "references": {
                "primary_sources": [
                    "WHO 2024 HIV",
                    "DHHS/CDC HIV Treatment Guidelines",
                    "IAS-USA 2024"
                ],
                "last_updated": "2025-12-24",
                "evidence_level": "High – guideline-based",
            },
        },

        "Bictegravir/Emtricitabine/Tenofovir alafenamide (BIC/FTC/TAF)": {
            "group": "Antiviral - Single tablet regimen (INSTI + NRTI backbone)",
            "vietnamese_name": "Bictegravir/Emtricitabine/Tenofovir alafenamide (Biktarvy)",
            "administration": ["PO"],
            "indications": [
                "Điều trị HIV-1 first-line cho người lớn/thanh thiếu niên đủ điều kiện (eGFR ≥30)."
            ],
            "contraindications": [
                "Dị ứng thành phần.",
                "Dùng rifampin (cảm ứng mạnh).",
                "eGFR <30 mL/phút."
            ],
            "dosage": {
                "standard": "BIC 50mg + FTC 200mg + TAF 25mg PO mỗi ngày.",
                "notes": "Không cần booster; tách antacid/Fe/Ca nếu dạng chelat."
            },
            "renal_adjustment": {
                "normal": "Không cần chỉnh.",
                "30_60": "Không cần chỉnh.",
                "under_30": "Tránh (theo nhãn)."
            },
            "side_effects": [
                "Buồn nôn, nhức đầu.",
                "Tăng nhẹ creatinine (BIC ức chế OCT2).",
                "Tăng cân nhẹ.",
                "Hiếm: độc thận/xương (TAF thấp hơn TDF)."
            ],
            "interactions": [
                "Rifampin: chống chỉ định.",
                "Antacid/Fe/Ca: giảm hấp thu BIC, cần tách liều.",
                "Carbamazepine/phenytoin: cảm ứng, giảm nồng độ."
            ],
            "pregnancy": "Có thể dùng; DTG có bằng chứng rộng hơn, nhưng BIC đang được chấp nhận dần.",
            "risk_flags": {
                "high_alert": False,
                "narrow_therapeutic_index": False,
                "organ_toxicity": {"renal": True, "bone": True, "hepatic": True},
                "icu_critical_care_only": False,
                "look_alike_sound_alike": []
            },
            "guideline_tags": [
                "WHO 2024 HIV",
                "DHHS/CDC HIV 2024",
                "IAS-USA 2024"
            ],
            "mechanism_of_action": "INSTI (BIC) chặn tích hợp + NRTI backbone (FTC/TAF) ức chế RT và kết thúc chuỗi DNA HIV.",
            "monitoring": [
                "HIV RNA, CD4.",
                "Creatinine/eGFR (tăng nhẹ giả tạo; theo dõi thực thận).",
                "Men gan nếu đồng nhiễm HBV/HCV."
            ],
            "precautions": [
                "Tách antacid/Fe/Ca (BIC 2h trước hoặc 6h sau; có thể dùng cùng bữa ăn chứa Fe/Ca).",
                "Tránh rifampin; thận trọng với rifabutin/rifapentine.",
                "Theo dõi thận/xương dù nguy cơ thấp hơn TDF."
            ],
            "pharmacokinetics": {
                "half_life": "BIC ~17h; FTC 10h; TAF tiền thuốc ngắn, hoạt tính nội bào dài.",
                "onset": "Cmax 1–4h.",
                "duration": "1 lần/ngày.",
                "protein_binding": "BIC ~99%; TAF ~80%; FTC <4%.",
                "clearance": "BIC qua UGT1A1/CYP3A; FTC/TAF thải thận (tenofovir) + gan."
            },
            "storage": "20–25°C, tránh ẩm.",
            "black_box_warnings": "Bùng phát HBV khi ngừng; toan lactic/gan to nhiễm mỡ (nhóm NRTI, hiếm).",
            "drug_interactions": {
                "major": [
                    {
                        "drug": "Rifampin",
                        "mechanism": "Cảm ứng mạnh UGT/CYP, giảm AUC BIC >75%.",
                        "effect": "Thất bại điều trị.",
                        "management": "CHỐNG CHỈ ĐỊNH."
                    }
                ],
                "moderate": [
                    {
                        "drug": "Antacid/Fe/Ca",
                        "mechanism": "Tạo phức chelat giảm hấp thu BIC.",
                        "effect": "Giảm hiệu quả.",
                        "management": "Uống BIC/FTC/TAF 2h trước hoặc 6h sau; bữa ăn chứa Fe/Ca được phép."
                    },
                    {
                        "drug": "Carbamazepine/phenytoin",
                        "mechanism": "Cảm ứng UGT/CYP.",
                        "effect": "Giảm nồng độ.",
                        "management": "Tránh nếu có thể."
                    }
                ],
                "minor": []
            },
            "contraindications_detail": {
                "tuyệt_đối": ["Quá mẫn", "Rifampin", "eGFR <30 mL/phút"],
                "tương_đối": [
                    "Thuốc cảm ứng mạnh khác (carbamazepine, phenytoin).",
                    "Suy gan trung bình-nặng (dữ liệu hạn chế)."
                ]
            },
            "pregnancy_lactation": {
                "fda_category": "Not classified",
                "pregnancy_details": "Có thể dùng; dữ liệu đang tăng. DTG có bằng chứng rộng hơn.",
                "lactation": {
                    "safety": "Caution",
                    "details": "Dữ liệu hạn chế.",
                    "recommendation": "Đánh giá lợi ích/nguy cơ."
                }
            },
            "hepatic_adjustment": {
                "mild": "Không cần chỉnh.",
                "moderate": "Thận trọng.",
                "severe": "Dữ liệu hạn chế; cân nhắc tránh.",
                "notes": "BIC chuyển hóa gan; FTC/TAF ít bị ảnh hưởng."
            },
            "overdose_management": {
                "symptoms": ["Buồn nôn, đau đầu; độc tính nặng hiếm."],
                "antidote": "Không có.",
                "treatment": [
                    "Điều trị hỗ trợ; than hoạt nếu mới uống."
                ],
                "monitoring": "Dấu hiệu sinh tồn, men gan, creatinine."
            },
            "reversal_agents": None,
            "administration_instructions": {
                "oral": {
                    "with_food": "Có thể với hoặc không.",
                    "timing": "1 lần/ngày; tách antacid/Fe/Ca nếu dạng chelat."
                }
            },
            "references": {
                "primary_sources": [
                    "WHO 2024 HIV",
                    "DHHS/CDC HIV Treatment Guidelines",
                    "IAS-USA 2024"
                ],
                "last_updated": "2025-12-24",
                "evidence_level": "High – guideline-based"
            }
        },

        "Cabotegravir + Rilpivirine (Long-acting IM)": {
            "group": "Antiviral - Long-acting INSTI + NNRTI (injectable)",
            "vietnamese_name": "Cabotegravir + Rilpivirine tiêm dài hạn",
            "administration": ["IM"],
            "indications": [
                "Điều trị duy trì HIV-1 ở người đã ức chế virus ổn định (VL <50 copies/mL), không có kháng CAB/RPV, không thất bại điều trị gần đây."
            ],
            "contraindications": [
                "Dị ứng với cabotegravir hoặc rilpivirine.",
                "Dùng đồng thời rifampin, carbamazepine, phenytoin, St. John’s wort (cảm ứng mạnh).",
                "Dùng đồng thời PPI (giảm hấp thu RPV nếu dùng lead-in oral; với IM không áp dụng nhưng cần thận trọng chuyển đổi)."
            ],
            "dosage": {
                "oral_lead_in_optional": "Cabotegravir 30mg PO + RPV 25mg PO mỗi ngày x ~28 ngày (tùy phác đồ).",
                "loading_im": "600mg CAB IM + 900mg RPV IM (mông đối bên) ngày 1.",
                "maintenance_im": "400mg CAB IM + 600mg RPV IM mỗi 1 tháng; hoặc 600/900mg mỗi 2 tháng theo phác đồ nhãn.",
                "missed_dose": "Nếu trễ, dùng oral bridging CAB 30mg + RPV 25mg hàng ngày cho đến khi tiêm lại.",
                "notes": "Tiêm sâu bắp (ventrogluteal). Cần lịch hẹn đều đặn; đánh giá kháng trước khi chuyển."
            },
            "renal_adjustment": {
                "normal": "Không cần chỉnh.",
                "30_60": "Không cần chỉnh; theo dõi.",
                "under_30": "Dữ liệu hạn chế; thận trọng."
            },
            "side_effects": [
                "Phản ứng tại chỗ tiêm (đau, sưng, đỏ).",
                "Sốt nhẹ, mệt, đau đầu.",
                "Tăng men gan hiếm.",
                "Hiếm: kéo dài QT (RPV)."
            ],
            "interactions": [
                "Cảm ứng UGT/CYP3A (rifampin, carbamazepine, phenytoin, St. John’s wort): giảm nồng độ CAB/RPV.",
                "RPV tương tác pH: tránh PPI nếu dùng lead-in hoặc oral bridge; antacid/H2 tách thời gian.",
                "CYP3A inhibitors mạnh có thể tăng RPV (ít ý nghĩa lâm sàng với IM nhưng lưu ý)."
            ],
            "pregnancy": "Dữ liệu hạn chế; cân nhắc chuyển sang phác đồ uống đã biết an toàn.",
            "risk_flags": {
                "high_alert": False,
                "narrow_therapeutic_index": False,
                "organ_toxicity": {"hepatic": True, "cardiac": True},
                "icu_critical_care_only": False,
                "look_alike_sound_alike": []
            },
            "guideline_tags": [
                "DHHS/CDC HIV 2024",
                "WHO 2024 HIV",
                "IAS-USA 2024"
            ],
            "mechanism_of_action": "Cabotegravir ức chế integrase; rilpivirine ức chế allosteric RT; dạng tiêm depot phóng thích kéo dài duy trì ức chế virus.",
            "monitoring": [
                "HIV RNA định kỳ; kiểm tra VL trước chuyển và sau liều đầu.",
                "Men gan.",
                "ECG nếu có nguy cơ QT (RPV).",
                "Theo dõi phản ứng tại chỗ tiêm."
            ],
            "precautions": [
                "Chỉ dùng cho người đã ức chế virus, không có kháng CAB/RPV.",
                "Tuân thủ lịch tiêm; nếu trễ cần bridge bằng đường uống.",
                "Tránh inducer mạnh UGT/CYP3A; quản lý pH với RPV khi dùng đường uống bridge/lead-in.",
                "Đánh giá thai kỳ; cân nhắc phác đồ uống nếu cần."
            ],
            "pharmacokinetics": {
                "half_life": "CAB IM ~5–12 tuần; RPV IM ~13–28 tuần (tùy cá thể).",
                "onset": "Nồng độ đạt mức điều trị sau liều tải IM; oral lead-in giúp đánh giá dung nạp.",
                "duration": "Duy trì 4–8 tuần tùy lịch.",
                "protein_binding": "CAB >99%; RPV ~99%.",
                "clearance": "CAB: UGT1A1; RPV: CYP3A; thải chậm do depot."
            },
            "storage": "Bảo quản lọ/bơm tiêm theo nhãn; tránh đông lạnh, lắc nhẹ trước tiêm.",
            "black_box_warnings": None,
            "drug_interactions": {
                "major": [
                    {
                        "drug": "Rifampin, carbamazepine, phenytoin, St. John’s wort",
                        "mechanism": "Cảm ứng UGT/CYP3A làm giảm nồng độ kéo dài.",
                        "effect": "Thất bại điều trị.",
                        "management": "CHỐNG CHỈ ĐỊNH."
                    }
                ],
                "moderate": [
                    {
                        "drug": "PPI (nếu oral lead-in/bridge)",
                        "mechanism": "Tăng pH giảm hấp thu RPV.",
                        "effect": "Giảm AUC RPV đường uống.",
                        "management": "Tránh PPI trong giai đoạn oral; H2/antacid tách thời gian."
                    }
                ],
                "minor": []
            },
            "contraindications_detail": {
                "tuyệt_đối": [
                    "Quá mẫn.",
                    "Dùng inducer mạnh (rifampin, carbamazepine, phenytoin, St. John’s wort)."
                ],
                "tương_đối": [
                    "Nguy cơ QT hoặc thuốc kéo dài QT (do RPV).",
                    "Suy gan trung bình-nặng.",
                    "Thai kỳ (dữ liệu hạn chế)."
                ]
            },
            "pregnancy_lactation": {
                "fda_category": "Not classified",
                "pregnancy_details": "Dữ liệu hạn chế; cân nhắc phác đồ uống an toàn hơn.",
                "lactation": {
                    "safety": "Caution",
                    "details": "Dữ liệu hạn chế.",
                    "recommendation": "Đánh giá lợi ích/nguy cơ."
                }
            },
            "hepatic_adjustment": {
                "mild": "Không cần chỉnh; theo dõi men gan.",
                "moderate": "Thận trọng.",
                "severe": "Tránh; dữ liệu hạn chế.",
                "notes": "CYP3A/UGT chuyển hóa; kéo dài phơi nhiễm ở suy gan có thể xảy ra."
            },
            "overdose_management": {
                "symptoms": ["Tăng phản ứng tại chỗ tiêm, nhức đầu, kéo dài QT (RPV, hiếm)."],
                "antidote": "Không có.",
                "treatment": [
                    "Điều trị hỗ trợ; do depot nên không loại bỏ nhanh được.",
                    "Theo dõi ECG nếu nghi kéo dài QT."
                ],
                "monitoring": "ECG, men gan, triệu chứng lâm sàng."
            },
            "reversal_agents": {
                "available": False,
                "agents": [],
                "notes": "Không có antidote đặc hiệu. Điều trị quá liều chủ yếu là điều trị hỗ trợ. Với dạng IM: không thể loại bỏ nhanh do depot, cần theo dõi lâu dài. Với dạng oral: than hoạt nếu mới uống, theo dõi ECG và men gan."
            },
            "administration_instructions": {
                "oral": {
                    "with_food": "Lead-in/bridge: uống cùng thức ăn (RPV cần bữa ăn).",
                    "timing": "1 lần/ngày trong giai đoạn lead-in/bridge."
                },
                "im": {
                    "site": "Tiêm sâu bắp vùng mông (ventrogluteal), hai bên luân phiên.",
                    "timing": "Liều tải ngày 1; duy trì mỗi 1 hoặc 2 tháng tùy phác đồ.",
                    "notes": "Không tiêm IV/subcut; đảm bảo lịch hẹn đều đặn."
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

        "Dolutegravir (DTG)": {
            "group": "Antiviral - Integrase strand transfer inhibitor (INSTI)",
            "vietnamese_name": "Dolutegravir (DTG)",
            "administration": ["PO"],
            "indications": [
                "Điều trị HIV-1 kết hợp đa thuốc (first-line ưu tiên).",
                "Phác đồ PEP khi cần INSTI (kết hợp TDF/3TC).",
            ],
            "contraindications": ["Dị ứng với dolutegravir."],
            "dosage": {
                "standard": "50mg PO mỗi ngày.",
                "with_rifampin": "50mg PO x 2 lần/ngày (do cảm ứng UGT/CYP3A).",
                "insti_resistance": "50mg PO x 2 lần/ngày khi nghi ngờ/kháng INSTI.",
                "notes": "Uống cách antacid/iron/calcium ít nhất 2 giờ trước hoặc 6 giờ sau.",
            },
            "renal_adjustment": {
                "normal": "Không cần chỉnh.",
                "30_60": "Không cần chỉnh.",
                "under_30": "Không cần chỉnh; thận trọng nếu chạy thận (dữ liệu hạn chế).",
            },
            "side_effects": [
                "Mất ngủ, đau đầu (thường nhẹ).",
                "Tăng nhẹ creatinine do ức chế OCT2 (không giảm GFR thực).",
                "Tăng cân (nhẹ-moderate) khi dùng dài hạn.",
                "Hiếm: tăng men gan, phản ứng quá mẫn.",
            ],
            "interactions": [
                "Rifampin: giảm nồng độ DTG (cần tăng liều).",
                "Antacid chứa Al/Mg, sắt, calcium: giảm hấp thu (uống cách thời gian).",
                "Carbamazepine/phenytoin: cảm ứng, giảm nồng độ DTG.",
            ],
            "pregnancy": "Safe/Preferred: WHO khuyến cáo DTG cho phụ nữ mang thai và tuổi sinh sản.",
            "risk_flags": {
                "high_alert": False,
                "narrow_therapeutic_index": False,
                "organ_toxicity": {"hepatic": True},
                "icu_critical_care_only": False,
                "look_alike_sound_alike": []
            },
            "guideline_tags": [
                "WHO 2024 HIV",
                "DHHS/CDC HIV 2024",
                "IAS-USA 2024"
            ],
            "mechanism_of_action": (
                "Ức chế integrase strand transfer của HIV-1, ngăn tích hợp DNA virus vào DNA vật chủ, "
                "từ đó ngăn sao chép và sản sinh virion mới."
            ),
            "monitoring": [
                "HIV RNA, CD4 theo phác đồ.",
                "Creatinine (tăng nhẹ giả tạo), men gan nếu viêm gan đồng nhiễm.",
                "Tương tác thuốc khi dùng cùng rifampin/antacid.",
            ],
            "precautions": [
                "Tách liều với antacid/iron/calcium để tránh giảm hấp thu.",
                "Điều chỉnh liều khi dùng với rifampin hoặc các chất cảm ứng mạnh.",
                "Theo dõi tăng cân dài hạn.",
            ],
            "pharmacokinetics": {
                "half_life": "14 giờ.",
                "onset": "Nồng độ đỉnh ~2–3 giờ.",
                "duration": "Dùng 1 lần/ngày nhờ half-life dài.",
                "protein_binding": "~99%.",
                "clearance": "Chuyển hóa qua UGT1A1 (chủ yếu) và CYP3A.",
            },
            "storage": "Bảo quản 20–25°C, tránh ẩm.",
            "black_box_warnings": None,
            "drug_interactions": {
                "major": [
                    {
                        "drug": "Rifampin",
                        "mechanism": "Cảm ứng UGT1A1/CYP3A làm giảm nồng độ DTG.",
                        "effect": "Nguy cơ thất bại điều trị.",
                        "management": "Tăng liều DTG lên 50mg x 2 lần/ngày khi dùng cùng.",
                    }
                ],
                "moderate": [
                    {
                        "drug": "Antacid chứa Al/Mg, sắt, calcium",
                        "mechanism": "Tạo phức chelat, giảm hấp thu DTG.",
                        "effect": "Giảm AUC, nguy cơ thất bại điều trị.",
                        "management": "Uống DTG trước antacid 2 giờ hoặc sau 6 giờ.",
                    },
                    {
                        "drug": "Carbamazepine, phenytoin, phenobarbital",
                        "mechanism": "Cảm ứng UGT/CYP3A.",
                        "effect": "Giảm nồng độ DTG.",
                        "management": "Tránh nếu có thể; nếu dùng, cân nhắc tăng liều và theo dõi tải lượng virus.",
                    },
                ],
                "minor": [],
            },
            "contraindications_detail": {
                "tuyệt_đối": ["Quá mẫn với dolutegravir."],
                "tương_đối": [
                    "Đang dùng rifampin/cảm ứng mạnh (cần chỉnh liều).",
                    "Suy gan trung bình-nặng: thận trọng, dữ liệu hạn chế.",
                ],
            },
            "pregnancy_lactation": {
                "fda_category": "Not classified (preferred in pregnancy per WHO).",
                "pregnancy_details": "DTG được khuyến cáo do hiệu quả cao, khởi phát nhanh, ít tương tác.",
                "lactation": {
                    "safety": "Caution",
                    "details": "Bài tiết thấp vào sữa; có thể tiếp tục điều trị theo khuyến cáo WHO.",
                    "recommendation": "Theo dõi trẻ, duy trì tuân thủ liều.",
                },
            },
            "hepatic_adjustment": {
                "mild": "Không cần chỉnh.",
                "moderate": "Thận trọng, theo dõi men gan.",
                "severe": "Dữ liệu hạn chế; cân nhắc INSTI khác/giảm liều và theo dõi sát.",
                "notes": "Chuyển hóa qua gan; tăng phơi nhiễm ở suy gan nặng chưa rõ.",
            },
            "overdose_management": {
                "symptoms": ["Buồn nôn, đau đầu, mất ngủ; hiếm khi độc tính nặng."],
                "antidote": "Không có antidote đặc hiệu.",
                "treatment": [
                    "Điều trị hỗ trợ, than hoạt nếu uống quá liều gần đây.",
                    "Theo dõi ECG, dấu hiệu sinh tồn; DTG gắn protein cao, lọc máu ít hiệu quả.",
                ],
                "monitoring": "Dấu hiệu lâm sàng, men gan, tải lượng virus (sau ổn định).",
            },
            "reversal_agents": {
                "available": False,
                "agents": [],
                "notes": "Không có antidote đặc hiệu. Điều trị quá liều chủ yếu là điều trị hỗ trợ, than hoạt nếu uống quá liều gần đây, theo dõi ECG và dấu hiệu sinh tồn. DTG gắn protein cao, lọc máu ít hiệu quả."
            },
            "administration_instructions": {
                "oral": {
                    "with_food": "Có thể uống cùng hoặc không cùng thức ăn.",
                    "timing": "1 lần/ngày; nếu dùng antacid/Fe/Ca, tách liều 2 giờ trước hoặc 6 giờ sau.",
                }
            },
            "references": {
                "primary_sources": [
                    "WHO Consolidated Guidelines on HIV (2024)",
                    "DHHS/CDC HIV Treatment Guidelines",
                    "IAS-USA HIV treatment recommendations",
                ],
                "last_updated": "2025-12-24",
                "evidence_level": "High – guideline-based",
            },
        },

}

__all__ = ['INTEGRASE_INHIBITORS_ARVS']
