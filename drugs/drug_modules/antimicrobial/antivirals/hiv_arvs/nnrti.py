"""
HIV Antiretrovirals - Nnrti
"""
from typing import Dict, Any


NNRTI_ARVS: Dict[str, Dict[str, Any]] = {
        "Efavirenz (EFV)": {
            "group": "Antiviral - Non-nucleoside reverse transcriptase inhibitor (NNRTI)",
            "vietnamese_name": "Efavirenz (EFV)",
            "administration": ["PO"],
            "indications": [
                "Điều trị HIV-1 kết hợp đa thuốc (phác đồ NNRTI cổ điển).",
            ],
            "contraindications": [
                "Dị ứng với efavirenz.",
                "Dùng đồng thời với midazolam, triazolam, ergot (tương tác CYP3A).",
            ],
            "dosage": {
                "standard": "600mg PO mỗi tối, uống lúc đói (giảm chóng mặt/mất ngủ).",
                "hepatic_mild": "Không cần chỉnh; theo dõi men gan.",
                "notes": "Tránh uống cùng bữa nhiều mỡ (tăng hấp thu và tác dụng phụ thần kinh).",
            },
            "renal_adjustment": {
                "normal": "Không cần chỉnh (chuyển hóa gan).",
                "30_60": "Không cần chỉnh.",
                "under_30": "Không cần chỉnh.",
            },
            "side_effects": [
                "Chóng mặt, mất ngủ, ác mộng, thay đổi tâm trạng (thường giảm sau 2–4 tuần).",
                "Phát ban, có thể hội chứng Stevens-Johnson (hiếm).",
                "Tăng men gan, tăng lipid nhẹ.",
            ],
            "interactions": [
                "Cảm ứng và ức chế CYP3A4/CYP2B6 (phức tạp): ảnh hưởng nhiều thuốc (rifampin, azole, statin, CCB, thuốc an thần).",
            ],
            "pregnancy": "Khuyến cáo tránh trong quý 1 do dữ liệu dị tật ống thần kinh cũ; hiện có thể dùng nếu lợi ích vượt trội (WHO cho phép).",
            "risk_flags": {
                "high_alert": False,
                "narrow_therapeutic_index": False,
                "organ_toxicity": {"hepatic": True, "neuropsychiatric": True},
                "icu_critical_care_only": False,
                "look_alike_sound_alike": []
            },
            "guideline_tags": [
                "WHO 2024 HIV",
                "DHHS/CDC HIV 2024"
            ],
            "mechanism_of_action": (
                "Gắn vào vị trí allosteric của HIV-1 reverse transcriptase, "
                "gây biến đổi cấu hình và ức chế sao chép DNA virus (không cạnh tranh nucleoside)."
            ),
            "monitoring": [
                "HIV RNA, CD4 theo phác đồ.",
                "Men gan, lipid máu.",
                "Triệu chứng thần kinh/tâm thần trong 2–4 tuần đầu.",
                "Phát ban/Stevens-Johnson (hiếm).",
            ],
            "precautions": [
                "Dùng buổi tối, lúc đói để giảm tác dụng phụ thần kinh.",
                "Thận trọng ở bệnh nhân rối loạn tâm thần, động kinh (có thể làm nặng).",
                "Tránh phối hợp thuốc chuyển hóa qua CYP3A/CYP2B6 có cửa sổ hẹp trừ khi giám sát.",
            ],
            "pharmacokinetics": {
                "half_life": "40–55 giờ (dài, cho phép 1 lần/ngày).",
                "onset": "Nồng độ đỉnh ~3–5 giờ.",
                "duration": "1 lần/ngày; tác dụng phụ thần kinh thường giảm sau 2–4 tuần.",
                "protein_binding": "~99%.",
                "clearance": "Chuyển hóa gan (CYP2B6, CYP3A4); bài tiết qua phân/nhẹ qua thận.",
            },
            "storage": "Bảo quản 20–25°C, tránh ẩm.",
            "black_box_warnings": None,
            "drug_interactions": {
                "major": [
                    {
                        "drug": "Midazolam, triazolam, ergot derivatives",
                        "mechanism": "Ức chế/ cảm ứng CYP3A gây thay đổi nồng độ lớn.",
                        "effect": "Nguy cơ độc tính hoặc giảm hiệu lực thuốc nền.",
                        "management": "Chống chỉ định phối hợp.",
                    }
                ],
                "moderate": [
                    {
                        "drug": "Rifampin, rifabutin",
                        "mechanism": "Cảm ứng CYP; giảm nồng độ EFV.",
                        "effect": "Nguy cơ thất bại điều trị.",
                        "management": "Cân nhắc tăng liều EFV lên 800mg với rifampin; theo dõi tải lượng virus.",
                    },
                    {
                        "drug": "Voriconazole",
                        "mechanism": "EFV cảm ứng CYP, giảm nồng độ voriconazole; voriconazole ức chế CYP, tăng EFV.",
                        "effect": "Giảm hiệu lực voriconazole, tăng độc tính EFV.",
                        "management": "Tránh phối hợp hoặc điều chỉnh liều theo khuyến cáo (tăng voriconazole, giảm EFV).",
                    },
                ],
                "minor": [],
            },
            "contraindications_detail": {
                "tuyệt_đối": [
                    "Quá mẫn với efavirenz.",
                    "Dùng cùng midazolam, triazolam, ergot alkaloids.",
                ],
                "tương_đối": [
                    "Tiền sử rối loạn tâm thần, động kinh.",
                    "Bệnh gan mạn (HBV/HCV đồng nhiễm) – theo dõi men gan.",
                ],
            },
            "pregnancy_lactation": {
                "fda_category": "D (cũ); hiện WHO cho phép nếu lợi ích vượt trội sau tư vấn.",
                "pregnancy_details": "Tránh quý 1 nếu có lựa chọn khác; có thể dùng từ quý 2 trở đi hoặc khi lợi ích vượt nguy cơ.",
                "lactation": {
                    "safety": "Caution",
                    "details": "Bài tiết vào sữa; WHO cho phép tiếp tục điều trị khi cho bú.",
                    "recommendation": "Theo dõi trẻ về an thần/phát ban; ưu tiên phác đồ INSTI nếu sẵn có.",
                },
            },
            "hepatic_adjustment": {
                "mild": "Không cần chỉnh, theo dõi men gan.",
                "moderate": "Thận trọng, theo dõi men gan chặt; cân nhắc thuốc khác nếu ALT/AST cao.",
                "severe": "Tránh nếu xơ gan Child-Pugh B/C do dữ liệu hạn chế và nguy cơ tích lũy.",
                "notes": "Chuyển hóa gan mạnh qua CYP2B6/3A4.",
            },
            "overdose_management": {
                "symptoms": [
                    "Tăng tác dụng phụ thần kinh (ảo giác, lú lẫn), chóng mặt nặng.",
                    "Buồn nôn, nôn.",
                ],
                "antidote": "Không có antidote đặc hiệu.",
                "treatment": [
                    "Than hoạt nếu uống quá liều sớm.",
                    "Hỗ trợ triệu chứng, theo dõi thần kinh và men gan.",
                ],
                "monitoring": "Dấu hiệu thần kinh, men gan, ECG nếu nguy cơ kéo dài QT (hiếm).",
            },
            "reversal_agents": {
                "available": False,
                "agents": [],
                "notes": "Không có antidote đặc hiệu. Điều trị quá liều chủ yếu là than hoạt nếu uống quá liều sớm, hỗ trợ triệu chứng, theo dõi thần kinh và men gan."
            },
            "administration_instructions": {
                "oral": {
                    "with_food": "Uống lúc đói hoặc bữa ít chất béo để giảm tác dụng phụ thần kinh.",
                    "timing": "Uống buổi tối trước khi ngủ để hạn chế chóng mặt/ác mộng.",
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

        "Efavirenz/Tenofovir disoproxil fumarate/Emtricitabine (EFV/TDF/FTC)": {
            "group": "Antiviral - Single tablet regimen (NNRTI + NRTI backbone)",
            "vietnamese_name": "Efavirenz/TDF/FTC (Atripla và tương đương)",
            "administration": ["PO"],
            "indications": [
                "Điều trị HIV-1 người lớn (phác đồ cổ điển NNRTI, không còn first-line ưu tiên)."
            ],
            "contraindications": [
                "Dị ứng thành phần.",
                "Dùng đồng thời midazolam/triazolam/ergot (EFV tương tác).",
                "CrCl <50 mL/phút (cần chỉnh TDF/FTC đơn lẻ; FDC không chỉnh được)."
            ],
            "dosage": {
                "standard": "EFV 600mg + TDF 300mg + FTC 200mg PO mỗi tối, uống lúc đói để giảm tác dụng phụ thần kinh.",
                "notes": "Không thích hợp nếu cần chỉnh liều TDF/FTC do thận."
            },
            "renal_adjustment": {
                "normal": "Không cần chỉnh.",
                "30_60": "Không dùng FDC; chuyển sang thành phần đơn lẻ để chỉnh liều.",
                "under_30": "Tránh."
            },
            "side_effects": [
                "Chóng mặt, ác mộng, mất ngủ (EFV, thường giảm sau 2–4 tuần).",
                "Phát ban, tăng men gan.",
                "Tăng creatinine/phospho giảm (TDF), giảm mật độ xương."
            ],
            "interactions": [
                "EFV cảm ứng/ức chế CYP3A/2B6: tương tác nhiều thuốc (rifampin, azole, statin, CCB, thuốc an thần).",
                "TDF độc thận; tăng nguy cơ với thuốc độc thận."
            ],
            "pregnancy": "Tránh quý 1 nếu có lựa chọn khác; có thể dùng từ quý 2 trở đi.",
            "risk_flags": {
                "high_alert": False,
                "narrow_therapeutic_index": False,
                "organ_toxicity": {"hepatic": True, "neuropsychiatric": True, "renal": True, "bone": True},
                "icu_critical_care_only": False,
                "look_alike_sound_alike": ["TDF vs TAF"]
            },
            "guideline_tags": [
                "WHO 2024 HIV (NNRTI legacy option)",
                "DHHS/CDC HIV 2024"
            ],
            "mechanism_of_action": "NNRTI (EFV) ức chế allosteric RT + NRTI (TDF/FTC) ức chế cạnh tranh, kết thúc chuỗi DNA HIV.",
            "monitoring": [
                "HIV RNA, CD4.",
                "Men gan, lipid.",
                "Triệu chứng thần kinh/tâm thần 2–4 tuần đầu.",
                "Creatinine/eGFR, phospho, mật độ xương nếu nguy cơ cao."
            ],
            "precautions": [
                "Uống buổi tối, lúc đói để giảm tác dụng phụ thần kinh.",
                "Tránh ở người rối loạn tâm thần/động kinh nếu có lựa chọn khác.",
                "Không dùng FDC nếu cần chỉnh liều TDF/FTC vì suy thận."
            ],
            "pharmacokinetics": {
                "half_life": "EFV 40–55h; TDF ~17h; FTC 10h huyết tương.",
                "onset": "Cmax EFV 3–5h.",
                "duration": "1 lần/ngày.",
                "protein_binding": "EFV ~99%; TDF <1%; FTC <4%.",
                "clearance": "EFV gan (CYP2B6/3A4); TDF/FTC thận."
            },
            "storage": "20–25°C, khô ráo.",
            "black_box_warnings": "Toan lactic/gan to nhiễm mỡ (NRTI, hiếm); cảnh báo thần kinh EFV; bùng phát HBV khi ngừng.",
            "drug_interactions": {
                "major": [
                    {
                        "drug": "Midazolam, triazolam, ergot",
                        "mechanism": "EFV ức chế/cảm ứng CYP3A gây thay đổi nồng độ lớn.",
                        "effect": "Nguy cơ độc tính/giảm hiệu lực.",
                        "management": "Chống chỉ định phối hợp."
                    }
                ],
                "moderate": [
                    {
                        "drug": "Rifampin",
                        "mechanism": "Cảm ứng CYP, giảm EFV; EFV cũng cảm ứng CYP.",
                        "effect": "Giảm nồng độ; có thể cần EFV 800mg theo guideline.",
                        "management": "Cân nhắc tăng liều EFV và theo dõi virus."
                    },
                    {
                        "drug": "Voriconazole",
                        "mechanism": "Tương tác hai chiều CYP3A/CYP2B6.",
                        "effect": "Giảm voriconazole, tăng EFV.",
                        "management": "Tránh hoặc chỉnh liều theo khuyến cáo."
                    }
                ],
                "minor": []
            },
            "contraindications_detail": {
                "tuyệt_đối": [
                    "Quá mẫn thành phần.",
                    "Phối hợp midazolam/triazolam/ergot."
                ],
                "tương_đối": [
                    "Rối loạn tâm thần/động kinh.",
                    "CrCl <50 (không dùng FDC; cần dạng đơn lẻ chỉnh liều)."
                ]
            },
            "pregnancy_lactation": {
                "fda_category": "D (cũ); hiện WHO cho phép sau quý 1 khi lợi ích vượt trội",
                "pregnancy_details": "Tránh quý 1 nếu có lựa chọn khác; có thể dùng từ quý 2.",
                "lactation": {
                    "safety": "Caution",
                    "details": "Bài tiết vào sữa; theo dõi trẻ về an thần/phát ban.",
                    "recommendation": "Cân nhắc INSTI-first nếu sẵn có."
                }
            },
            "hepatic_adjustment": {
                "mild": "Không cần chỉnh, theo dõi men gan.",
                "moderate": "Thận trọng; theo dõi chặt.",
                "severe": "Tránh do thiếu dữ liệu/tăng nguy cơ tích lũy.",
                "notes": "EFV chuyển hóa gan; TDF/FTC thận."
            },
            "overdose_management": {
                "symptoms": ["Tăng tác dụng phụ thần kinh EFV, buồn nôn, chóng mặt; nguy cơ độc thận (TDF)."],
                "antidote": "Không có.",
                "treatment": [
                    "Than hoạt nếu mới uống.",
                    "Hỗ trợ triệu chứng; theo dõi thần kinh và thận."
                ],
                "monitoring": "Men gan, creatinine, triệu chứng thần kinh."
            },
            "reversal_agents": None,
            "administration_instructions": {
                "oral": {
                    "with_food": "Uống lúc đói/bữa ít mỡ để giảm tác dụng phụ thần kinh (EFV).",
                    "timing": "1 lần/ngày buổi tối."
                }
            },
            "references": {
                "primary_sources": [
                    "WHO 2024 HIV (NNRTI legacy)",
                    "DHHS/CDC HIV Treatment Guidelines"
                ],
                "last_updated": "2025-12-24",
                "evidence_level": "Guideline-based (legacy option)"
            }
        },

        "Rilpivirine (RPV)": {
            "group": "Antiviral - Non-nucleoside reverse transcriptase inhibitor (NNRTI)",
            "vietnamese_name": "Rilpivirine (RPV)",
            "administration": ["PO"],
            "indications": [
                "Điều trị HIV-1 (tải lượng ban đầu ≤100.000 copies/mL, CD4 >200) kết hợp backbone NRTI.",
                "Dạng LAI khi phối hợp cabotegravir (không đề cập chi tiết tại đây)."
            ],
            "contraindications": [
                "Dị ứng với rilpivirine.",
                "Dùng đồng thời rifampin, carbamazepine, phenytoin, St. John’s wort (cảm ứng CYP3A mạnh).",
                "Dùng đồng thời PPIs liều chuẩn/cao (giảm hấp thu)."
            ],
            "dosage": {
                "standard": "25mg PO mỗi ngày, uống cùng bữa ăn.",
                "notes": "Cần bữa ăn (≥390 kcal) để tăng hấp thu; tránh PPI, antacid/H2 tách thời gian."
            },
            "renal_adjustment": {
                "normal": "Không cần chỉnh.",
                "30_60": "Không cần chỉnh; thận trọng.",
                "under_30": "Thận trọng; theo dõi do dữ liệu hạn chế."
            },
            "side_effects": [
                "Đau đầu, buồn nôn.",
                "Mất ngủ, trầm cảm (hiếm).",
                "Tăng QT nhẹ trên ECG (hiếm)."
            ],
            "interactions": [
                "Cảm ứng CYP3A (rifampin, carbamazepine, phenytoin, St. John’s wort): giảm nồng độ → tránh.",
                "PPI/antacid/H2: giảm hấp thu do tăng pH.",
                "Macrolide/azole/clarithromycin: có thể tăng nồng độ (ức chế CYP3A)."
            ],
            "pregnancy": "Có thể dùng; INSTI-first vẫn ưu tiên.",
            "risk_flags": {
                "high_alert": False,
                "narrow_therapeutic_index": False,
                "organ_toxicity": {"hepatic": True, "cardiac": True},
                "icu_critical_care_only": False,
                "look_alike_sound_alike": []
            },
            "guideline_tags": [
                "WHO 2024 HIV (NNRTI alternative)",
                "DHHS/CDC HIV 2024"
            ],
            "mechanism_of_action": "NNRTI gắn allosteric vào HIV-1 RT, ức chế sao chép và kết thúc chuỗi DNA virus.",
            "monitoring": [
                "HIV RNA, CD4.",
                "Men gan.",
                "Triệu chứng trầm cảm/mất ngủ.",
                "ECG nếu có yếu tố kéo dài QT hoặc phối hợp thuốc kéo dài QT."
            ],
            "precautions": [
                "Uống cùng bữa ăn đủ calo; tránh PPI, tách antacid/H2.",
                "Không dùng nếu tải lượng ban đầu cao >100k hoặc CD4 <200 (tăng nguy cơ thất bại).",
                "Tránh cảm ứng CYP3A mạnh."
            ],
            "pharmacokinetics": {
                "half_life": "45 giờ.",
                "onset": "Cmax ~4–5 giờ (uống với thức ăn).",
                "duration": "1 lần/ngày.",
                "protein_binding": "~99%.",
                "clearance": "Gan (CYP3A)."
            },
            "storage": "20–25°C, tránh ẩm.",
            "black_box_warnings": None,
            "drug_interactions": {
                "major": [
                    {
                        "drug": "Rifampin, carbamazepine, phenytoin, St. John’s wort",
                        "mechanism": "Cảm ứng CYP3A → giảm AUC RPV.",
                        "effect": "Thất bại điều trị.",
                        "management": "CHỐNG CHỈ ĐỊNH."
                    },
                    {
                        "drug": "Proton pump inhibitors (omeprazole, etc.)",
                        "mechanism": "Tăng pH dạ dày giảm hấp thu RPV.",
                        "effect": "Giảm AUC, thất bại điều trị.",
                        "management": "CHỐNG CHỈ ĐỊNH với PPI."
                    }
                ],
                "moderate": [
                    {
                        "drug": "H2 blockers (ranitidine, famotidine)",
                        "mechanism": "Tăng pH, giảm hấp thu.",
                        "effect": "Giảm AUC.",
                        "management": "Uống H2 ≥12h trước hoặc ≥4h sau RPV."
                    },
                    {
                        "drug": "Antacid chứa Al/Mg/Ca",
                        "mechanism": "Tăng pH, chelat.",
                        "effect": "Giảm hấp thu.",
                        "management": "Uống antacid ≥2h trước hoặc ≥4h sau RPV."
                    }
                ],
                "minor": []
            },
            "contraindications_detail": {
                "tuyệt_đối": [
                    "Quá mẫn.",
                    "Dùng rifampin/carbamazepine/phenytoin/St. John’s wort.",
                    "Dùng PPI."
                ],
                "tương_đối": [
                    "QT kéo dài hoặc thuốc kéo dài QT.",
                    "CD4 <200 hoặc tải lượng >100k.",
                    "Suy gan trung bình-nặng."
                ]
            },
            "pregnancy_lactation": {
                "fda_category": "Not classified",
                "pregnancy_details": "Có thể cân nhắc; INSTI-first ưu tiên.",
                "lactation": {
                    "safety": "Caution",
                    "details": "Dữ liệu hạn chế.",
                    "recommendation": "Đánh giá lợi ích/nguy cơ."
                }
            },
            "hepatic_adjustment": {
                "mild": "Không cần chỉnh.",
                "moderate": "Thận trọng.",
                "severe": "Tránh do dữ liệu hạn chế.",
                "notes": "Chuyển hóa gan CYP3A."
            },
            "overdose_management": {
                "symptoms": ["Buồn nôn, nhức đầu, kéo dài QT (hiếm)."],
                "antidote": "Không có.",
                "treatment": [
                    "Điều trị hỗ trợ; than hoạt nếu mới uống.",
                    "Theo dõi ECG nếu nghi kéo dài QT."
                ],
                "monitoring": "ECG, men gan, triệu chứng thần kinh/tâm lý."
            },
            "reversal_agents": {
                "available": False,
                "agents": [],
                "notes": "Không có antidote đặc hiệu. Điều trị quá liều chủ yếu là điều trị hỗ trợ, than hoạt nếu mới uống, theo dõi ECG nếu nghi kéo dài QT."
            },
            "administration_instructions": {
                "oral": {
                    "with_food": "PHẢI uống cùng bữa ăn đủ calo.",
                    "timing": "1 lần/ngày; tách antacid/H2 theo khuyến cáo."
                }
            },
            "references": {
                "primary_sources": [
                    "DHHS/CDC HIV Treatment Guidelines",
                    "WHO 2024 HIV (NNRTI alternative)"
                ],
                "last_updated": "2025-12-24",
                "evidence_level": "High – guideline-based"
            }
        },

}

__all__ = ['NNRTI_ARVS']
