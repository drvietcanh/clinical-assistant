"""
Hematology Drugs - Other Hematology
"""
from typing import Dict, Any


OTHER_HEMATOLOGY_DRUGS: Dict[str, Dict[str, Any]] = {
        "Emicizumab": {
            "group": "Hematology - Bispecific Monoclonal Antibody",
            "vietnamese_name": "Emicizumab, Hemlibra",
            "administration": ["SC"],
            "indications": [
                "Hemophilia A (với hoặc không có chất ức chế factor VIII)",
                "Phòng ngừa chảy máu ở bệnh nhân hemophilia A"
            ],
            "contraindications": [
                "Dị ứng emicizumab hoặc bất kỳ thành phần nào",
                "Đang có huyết khối đang hoạt động"
            ],
            "dosage": {
                "adult_loading": "3mg/kg SC tuần 1, 2, 4",
                "adult_maintenance": "1.5mg/kg SC mỗi tuần, hoặc 3mg/kg SC mỗi 2 tuần, hoặc 6mg/kg SC mỗi 4 tuần",
                "notes": "Tiêm dưới da (SC) ở vùng bụng, đùi, hoặc cánh tay. Có thể tự tiêm sau khi được hướng dẫn."
            },
            "renal_adjustment": {
                "normal": "Không cần chỉnh liều",
                "30_60": "Không cần chỉnh liều",
                "under_30": "Không cần chỉnh liều"
            },
            "side_effects": [
                "Phản ứng tại chỗ tiêm (đau, đỏ, ngứa) - phổ biến",
                "Nhức đầu",
                "Mệt mỏi",
                "Buồn nôn",
                "Tăng nguy cơ huyết khối (thrombosis) - hiếm nhưng nghiêm trọng, đặc biệt khi dùng với activated prothrombin complex concentrate (aPCC)",
                "Dị ứng (hiếm)"
            ],
            "interactions": [
                "Activated prothrombin complex concentrate (aPCC): tăng nguy cơ huyết khối nghiêm trọng",
                "Recombinant factor VIIa: có thể tăng nguy cơ huyết khối"
            ],
        "pregnancy": "C",
            "mechanism_of_action": (
                "Emicizumab là bispecific monoclonal antibody (humanized) gắn đồng thời với factor IXa và factor X. "
                "Trong hemophilia A, thiếu factor VIII dẫn đến không thể hình thành phức hợp tenase (factor VIIIa/factor IXa) "
                "cần thiết để kích hoạt factor X thành factor Xa, dẫn đến rối loạn đông máu và chảy máu. "
                "Emicizumab bắt chước chức năng của factor VIIIa bằng cách gắn với factor IXa và factor X, "
                "tạo thành phức hợp tương tự tenase mà không cần factor VIII. "
                "Dẫn đến: kích hoạt factor X thành factor Xa, hình thành thrombin, và đông máu bình thường. "
                "Emicizumab được dùng để phòng ngừa chảy máu ở bệnh nhân hemophilia A, "
                "đặc biệt hiệu quả ở bệnh nhân có chất ức chế factor VIII (kháng thể kháng factor VIII) "
                "vì các thuốc thay thế factor VIII truyền thống không hiệu quả ở những bệnh nhân này. "
                "Emicizumab có half-life dài, cho phép dùng 1-4 tuần một lần (tùy phác đồ)."
            ),
            "monitoring": [
                "Tần suất và mức độ nghiêm trọng của chảy máu (theo dõi nhật ký chảy máu)",
                "Phản ứng tại chỗ tiêm",
                "Dấu hiệu huyết khối (đau ngực, khó thở, đau chân, sưng chân) - đặc biệt khi dùng với aPCC",
                "Dấu hiệu dị ứng (phát ban, khó thở, phù mạch)",
                "Chức năng gan (ALT, AST) - theo dõi định kỳ"
            ],
            "precautions": [
                "NGUY CƠ HUYẾT KHỐI - đặc biệt khi dùng với activated prothrombin complex concentrate (aPCC), "
                "cần theo dõi chặt chẽ dấu hiệu huyết khối",
                "Tránh dùng aPCC với emicizumab nếu có thể - nếu cần dùng, dùng liều thấp nhất và theo dõi chặt chẽ",
                "Có thể tự tiêm sau khi được hướng dẫn đúng cách",
                "Không dùng để điều trị cấp tính chảy máu nặng (cần dùng factor VIII hoặc bypassing agents)",
                "Thận trọng ở bệnh nhân có tiền sử huyết khối",
                "Có thể mất vài tuần để đạt hiệu quả đầy đủ"
            ],
            "pharmacokinetics": {
                "half_life": "~4-5 tuần (rất dài, cho phép dùng 1-4 tuần một lần)",
                "onset": "Vài tuần (tác dụng chậm)",
                "duration": "Dài (do half-life rất dài)",
                "protein_binding": "IgG4 bispecific monoclonal antibody",
                "metabolism": "Chuyển hóa qua hệ thống reticuloendothelial (RES)",
                "clearance": "Không phụ thuộc gan thận đáng kể"
            },
            "storage": "Bảo quản trong tủ lạnh (2-8°C), tránh đông lạnh, tránh ánh sáng. Có thể để ở nhiệt độ phòng (≤25°C) tối đa 7 ngày. Không làm nóng hoặc lắc mạnh.",
            "black_box_warnings": (
                "NGUY CƠ HUYẾT KHỐI - đặc biệt khi dùng với activated prothrombin complex concentrate (aPCC). "
                "Có báo cáo huyết khối tĩnh mạch sâu (DVT), thuyên tắc phổi (PE), và huyết khối động mạch. "
                "Tránh dùng aPCC với emicizumab nếu có thể. Nếu cần dùng, dùng liều thấp nhất và theo dõi chặt chẽ dấu hiệu huyết khối."
            ),
            "risk_flags": {
                "high_alert": True,
                "narrow_therapeutic_index": False,
                "bleeding_risk": False,
                "organ_toxicity": ["cardiovascular"],
                "qt_prolongation": False,
                "hepatotoxicity": False,
                "nephrotoxicity": False,
                "requires_monitoring": ["Signs of thrombosis (Black Box Warning - especially with aPCC)", "Injection site reactions", "Allergic reactions", "Liver function (ALT, AST)"]
            },
            "guideline_tags": [
                "FDA Black Box Warning - Thrombosis Risk (especially with aPCC)",
                "ASH Guidelines - Hemophilia A Treatment",
                "WHO Essential Medicines List"
            ],
            "drug_interactions": {
                "major": [
                    {
                        "drug": "Activated prothrombin complex concentrate (aPCC, FEIBA)",
                        "mechanism": "Tăng nguy cơ huyết khối khi dùng với emicizumab",
                        "effect": "Tăng nguy cơ huyết khối nghiêm trọng (DVT, PE, huyết khối động mạch)",
                        "management": "Tránh dùng nếu có thể. Nếu cần dùng, dùng liều thấp nhất (≤50 U/kg/24h) và theo dõi chặt chẽ dấu hiệu huyết khối."
                    },
                    {
                        "drug": "Recombinant factor VIIa (rFVIIa)",
                        "mechanism": "Có thể tăng nguy cơ huyết khối",
                        "effect": "Tăng nguy cơ huyết khối",
                        "management": "Thận trọng. Theo dõi chặt chẽ dấu hiệu huyết khối."
                    }
                ],
                "moderate": [],
                "minor": []
            },
            "contraindications_detail": {
                "tuyệt_đối": [
                    "Dị ứng emicizumab hoặc bất kỳ thành phần nào",
                    "Đang có huyết khối đang hoạt động"
                ],
                "tương_đối": [
                    "Tiền sử huyết khối - tăng nguy cơ huyết khối",
                    "Đang dùng aPCC - tăng nguy cơ huyết khối nghiêm trọng"
                ]
            },
            "pregnancy_lactation": {
                "fda_category": "C",
                "pregnancy_details": "Dữ liệu hạn chế. Có thể dùng trong thai kỳ khi lợi ích vượt trội nguy cơ. Theo dõi chặt chẽ.",
                "lactation": {
                    "safety": "Unknown",
                    "details": "Chưa rõ bài tiết vào sữa mẹ. Kháng thể lớn, hấp thu qua đường tiêu hóa trẻ có thể hạn chế.",
                    "recommendation": "Cân nhắc ngừng cho bú hoặc không dùng thuốc."
                }
            },
            "hepatic_adjustment": {
                "mild": "Không cần chỉnh liều",
                "moderate": "Không cần chỉnh liều",
                "severe": "Không cần chỉnh liều",
                "notes": "Emicizumab chuyển hóa qua RES, không phụ thuộc gan đáng kể."
            },
            "overdose_management": {
                "symptoms": [
                    "Tăng nguy cơ huyết khối",
                    "Phản ứng tại chỗ tiêm nặng hơn",
                    "Dị ứng (hiếm)"
                ],
                "antidote": "Không có antidote đặc hiệu. Điều trị hỗ trợ.",
                "treatment": [
                    "Theo dõi dấu hiệu huyết khối chặt chẽ",
                    "Xử trí huyết khối nếu có (anticoagulation, thrombectomy nếu cần)",
                    "Xử trí phản ứng dị ứng nếu có (antihistamine, corticosteroid, epinephrine nếu cần)"
                ],
                "monitoring": "Dấu hiệu huyết khối, phản ứng tại chỗ tiêm, dấu hiệu dị ứng"
            },
            "reversal_agents": {
                "available": False,
                "agents": []
            },
            "administration_instructions": {
                "sc": {
                    "reconstitution": "Dùng trực tiếp từ bút tiêm hoặc ống tiêm đã pha sẵn.",
                    "injection_site": "Vùng bụng, đùi, hoặc cánh tay. Thay đổi vị trí tiêm mỗi lần.",
                    "injection_technique": "Tiêm dưới da (SC), không tiêm vào cơ hoặc tĩnh mạch.",
                    "notes": "Có thể tự tiêm sau khi được hướng dẫn. Lưu trữ trong tủ lạnh, để ở nhiệt độ phòng 30 phút trước khi tiêm. Phác đồ: 3mg/kg tuần 1, 2, 4 (loading), sau đó 1.5mg/kg/tuần, 3mg/kg/2 tuần, hoặc 6mg/kg/4 tuần (maintenance)."
                }
            },
            "references": {
                "primary_sources": [
                    "FDA Drug Label - Emicizumab (Hemlibra)",
                    "UpToDate - Emicizumab: Drug information",
                    "Lexicomp - Emicizumab monograph",
                    "ASH Guidelines - Hemophilia A"
                ],
                "last_updated": "2025-02-18",
                "evidence_level": "A - FDA-approved, large RCTs showing benefit in hemophilia A prevention"
            }
        },    "Besremi": {
        "group": "Hematology - Long-Acting Interferon Alpha",
        "vietnamese_name": "Ropeginterferon alfa-2b, Besremi",
        "administration": ["SC"],
        "indications": [
            "Đa hồng cầu nguyên phát (polycythemia vera) ở người lớn"
        ],
        "contraindications": [
            "Dị ứng ropeginterferon hoặc bất kỳ thành phần nào",
            "Suy gan nặng (Child-Pugh C)",
            "Suy thận nặng (CrCl <30ml/phút)",
            "Bệnh tự miễn nặng đang hoạt động",
            "Trầm cảm nặng hoặc ý định tự tử"
        ],
        "dosage": {
            "adult_initial": "100 mcg SC mỗi 2 tuần, tăng dần đến 500 mcg SC mỗi 2 tuần",
            "adult_maintenance": "250-500 mcg SC mỗi 2 tuần",
            "notes": "Tiêm dưới da mỗi 2 tuần. Bắt đầu với liều thấp và tăng dần. FDA phê duyệt 11/12/2021. Dạng long-acting, chỉ cần tiêm 1 lần/2 tuần."
        },
        "renal_adjustment": {
            "normal": "Không cần chỉnh liều",
            "30_60": "Thận trọng, có thể cần giảm liều",
            "under_30": "CHỐNG CHỈ ĐỊNH (CrCl <30ml/phút)"
        },
        "side_effects": [
            "Cúm-like symptoms (sốt, ớn lạnh, mệt mỏi, đau cơ) - phổ biến, đặc biệt khi bắt đầu điều trị",
            "Giảm bạch cầu, tiểu cầu - phổ biến",
            "Tăng men gan (ALT, AST) - phổ biến",
            "Rối loạn tâm thần (trầm cảm, lo âu, kích động) - phổ biến, có thể nghiêm trọng",
            "Rối loạn tuyến giáp (cường giáp, suy giáp) - phổ biến",
            "Phản ứng tại chỗ tiêm (đau, đỏ, sưng) - phổ biến",
            "Buồn nôn, nôn - phổ biến",
            "Rụng tóc - phổ biến",
            "Nhiễm trùng - phổ biến",
            "Tự miễn (autoimmune disorders) - hiếm nhưng nghiêm trọng"
        ],
        "interactions": [
            "Thuốc ức chế tủy xương: tăng nguy cơ giảm bạch cầu, tiểu cầu",
            "Thuốc độc gan: tăng nguy cơ độc gan",
            "Theophylline: tăng nồng độ theophylline",
            "Warfarin: tăng tác dụng chống đông"
        ],
        "pregnancy": "C",
        "mechanism_of_action": "Ropeginterferon alfa-2b là long-acting interferon alpha-2b, được pegylated để kéo dài thời gian tác dụng. Interferon alpha là cytokine tự nhiên có tác dụng điều hòa miễn dịch và ức chế tăng sinh tế bào. Trong polycythemia vera, tăng sinh tế bào máu bất thường → tăng số lượng hồng cầu, bạch cầu, tiểu cầu. Ropeginterferon kích hoạt các thụ thể interferon → ức chế tăng sinh tế bào máu → giảm số lượng hồng cầu, bạch cầu, tiểu cầu → kiểm soát polycythemia vera. Dạng long-acting cho phép tiêm 1 lần/2 tuần thay vì 3 lần/tuần như interferon alpha thông thường. Dẫn đến: kiểm soát polycythemia vera và giảm nhu cầu phlebotomy. Ropeginterferon được FDA phê duyệt 11/12/2021 để điều trị polycythemia vera ở người lớn.",
        "monitoring": [
            "Công thức máu (CBC) - QUAN TRỌNG: giảm bạch cầu, tiểu cầu phổ biến, theo dõi trước và định kỳ",
            "Chức năng gan (ALT, AST) - tăng men gan phổ biến, theo dõi trước và định kỳ",
            "Chức năng thận (creatinine, BUN) - CHỐNG CHỈ ĐỊNH ở suy thận nặng",
            "Tâm thần - rối loạn tâm thần phổ biến, theo dõi dấu hiệu trầm cảm, lo âu, kích động",
            "Chức năng tuyến giáp (TSH, T4) - rối loạn tuyến giáp phổ biến, theo dõi định kỳ",
            "Dấu hiệu nhiễm trùng - tăng nguy cơ nhiễm trùng",
            "Dấu hiệu tự miễn - hiếm nhưng nghiêm trọng",
            "Đáp ứng điều trị (số lượng hồng cầu, nhu cầu phlebotomy)"
        ],
        "precautions": [
            "RỐI LOẠN TÂM THẦN - phổ biến, có thể nghiêm trọng. Theo dõi dấu hiệu trầm cảm, lo âu, kích động, ý định tự tử. Ngừng ngay nếu có ý định tự tử.",
            "GIẢM BẠCH CẦU, TIỂU CẦU - phổ biến, theo dõi CBC trước và định kỳ. Có thể cần giảm liều hoặc ngừng tạm thời.",
            "Tăng men gan - phổ biến, theo dõi chức năng gan. Có thể cần giảm liều hoặc ngừng nếu tăng nặng.",
            "CHỐNG CHỈ ĐỊNH ở suy gan nặng (Child-Pugh C)",
            "CHỐNG CHỈ ĐỊNH ở suy thận nặng (CrCl <30ml/phút)",
            "Rối loạn tuyến giáp - phổ biến, theo dõi chức năng tuyến giáp định kỳ",
            "Tự miễn - hiếm nhưng nghiêm trọng, theo dõi dấu hiệu",
            "Cúm-like symptoms - phổ biến khi bắt đầu, thường giảm sau vài tuần",
            "Cần tiêm mỗi 2 tuần - tuân thủ điều trị quan trọng"
        ],
        "pharmacokinetics": {
            "half_life": "~60-80 giờ (dài hơn interferon alpha thông thường ~4-5 giờ)",
            "onset": "Vài tuần đến vài tháng",
            "duration": "2 tuần (dùng 1 lần/2 tuần)",
            "protein_binding": "Không rõ",
            "metabolism": "Chuyển hóa qua gan và thận",
            "clearance": "Thải trừ qua thận"
        },
        "storage": "Bảo quản trong tủ lạnh (2-8°C), tránh đông lạnh. Có thể để ở nhiệt độ phòng (≤25°C) tối đa 30 ngày.",
        "black_box_warnings": "RỐI LOẠN TÂM THẦN - có thể gây trầm cảm, lo âu, kích động, ý định tự tử. Theo dõi chặt chẽ. Ngừng ngay nếu có ý định tự tử. GIẢM BẠCH CẦU, TIỂU CẦU - có thể gây giảm bạch cầu, tiểu cầu nghiêm trọng. Tăng men gan - có thể gây tăng men gan nghiêm trọng. CHỐNG CHỈ ĐỊNH ở suy gan nặng và suy thận nặng.",
        "drug_interactions": {
            "major": [],
            "moderate": [
                {
                    "drug": "Thuốc ức chế tủy xương (chemotherapy, zidovudine)",
                    "mechanism": "Tác dụng cộng dồn ức chế tủy xương",
                    "effect": "Tăng nguy cơ giảm bạch cầu, tiểu cầu",
                    "management": "Thận trọng. Theo dõi CBC chặt chẽ."
                },
                {
                    "drug": "Thuốc độc gan (acetaminophen, isoniazid)",
                    "mechanism": "Tác dụng cộng dồn độc gan",
                    "effect": "Tăng nguy cơ độc gan",
                    "management": "Thận trọng. Theo dõi chức năng gan chặt chẽ."
                },
                {
                    "drug": "Theophylline",
                    "mechanism": "Interferon làm giảm chuyển hóa theophylline",
                    "effect": "Tăng nồng độ theophylline",
                    "management": "Thận trọng. Theo dõi nồng độ theophylline."
                },
                {
                    "drug": "Warfarin",
                    "mechanism": "Interferon tăng tác dụng chống đông",
                    "effect": "Tăng nguy cơ chảy máu",
                    "management": "Thận trọng. Theo dõi INR chặt chẽ."
                }
            ],
            "minor": []
        },
        "contraindications_detail": {
            "tuyệt_đối": [
                "Dị ứng ropeginterferon hoặc bất kỳ thành phần nào",
                "Suy gan nặng (Child-Pugh C) - CHỐNG CHỈ ĐỊNH",
                "Suy thận nặng (CrCl <30ml/phút) - CHỐNG CHỈ ĐỊNH",
                "Trầm cảm nặng hoặc ý định tự tử - CHỐNG CHỈ ĐỊNH"
            ],
            "tương_đối": [
                "Bệnh tự miễn đang hoạt động - thận trọng",
                "Tiền sử rối loạn tâm thần - thận trọng",
                "Suy gan nhẹ đến trung bình - thận trọng",
                "Suy thận nhẹ đến trung bình - thận trọng"
            ]
        },
        "pregnancy_lactation": {
            "fda_category": "C",
            "pregnancy_details": "Ropeginterferon là FDA category C. Có nguy cơ cho thai nhi. Chỉ dùng khi lợi ích > nguy cơ. Tránh thai hiệu quả trong điều trị.",
            "lactation": {
                "safety": "Unknown",
                "details": "Chưa biết có bài tiết vào sữa mẹ hay không. Interferon có thể bài tiết vào sữa mẹ.",
                "recommendation": "Không dùng khi cho con bú."
            }
        },
        "hepatic_adjustment": {
            "mild": "Thận trọng",
            "moderate": "Thận trọng",
            "severe": "CHỐNG CHỈ ĐỊNH (Child-Pugh C)",
            "notes": "Ropeginterferon chuyển hóa qua gan. CHỐNG CHỈ ĐỊNH ở suy gan nặng. Theo dõi chức năng gan chặt chẽ."
        },
        "overdose_management": {
            "symptoms": [
                "Cúm-like symptoms nặng",
                "Giảm bạch cầu, tiểu cầu nặng",
                "Tăng men gan nặng",
                "Rối loạn tâm thần nặng"
            ],
            "antidote": "Không có antidote đặc hiệu",
            "treatment": [
                "Ngừng ropeginterferon",
                "Điều trị hỗ trợ",
                "Theo dõi CBC, chức năng gan",
                "Điều trị rối loạn tâm thần nếu cần"
            ],
            "monitoring": "Dấu hiệu sinh tồn, CBC, chức năng gan, dấu hiệu rối loạn tâm thần"
        },
        "reversal_agents": {
            "available": False,
            "agents": []
        },
        "administration_instructions": {
            "sc": {
                "reconstitution": "Dạng tiêm sẵn (pre-filled syringe)",
                "injection_site": "Vùng bụng, đùi, hoặc cánh tay. Thay đổi vị trí tiêm mỗi lần.",
                "notes": "Tiêm dưới da mỗi 2 tuần. Bắt đầu với 100 mcg, tăng dần đến 250-500 mcg. Có thể tự tiêm sau khi được hướng dẫn. Bảo quản trong tủ lạnh, để ở nhiệt độ phòng 30 phút trước khi tiêm."
            }
        },
        "references": {
            "primary_sources": [
                "FDA Drug Label - Ropeginterferon alfa-2b (Besremi)",
                "FDA Approval Date: 11/12/2021",
                "FDA-approved use: To treat polycythemia vera",
                "UpToDate - Ropeginterferon: Drug information",
                "NCCN Guidelines - Myeloproliferative Neoplasms"
            ],
            "last_updated": "2025-02-18",
            "evidence_level": "A - FDA-approved 11/12/2021"
        },
        "risk_flags": {
            "high_alert": True,
            "narrow_therapeutic_index": False,
            "bleeding_risk": False,
            "organ_toxicity": ["Hematologic (myelosuppression)", "Hepatic (elevated transaminases)", "Psychiatric (depression, anxiety, agitation)"],
            "qt_prolongation": False,
            "hepatotoxicity": True,
            "nephrotoxicity": False,
            "requires_monitoring": ["CBC - CRITICAL (before and periodically)", "Hepatic function (ALT, AST) - CRITICAL (before and periodically)", "Renal function (creatinine, BUN) - CRITICAL", "Psychiatric symptoms (depression, anxiety, agitation, suicidal ideation) - CRITICAL", "Thyroid function (TSH, T4) - periodically", "Signs of infection", "Signs of autoimmune disorders"]
        },
        "guideline_tags": [
            "NCCN Guidelines - Myeloproliferative Neoplasms",
            "FDA Black Box Warning - Ropeginterferon and Psychiatric Disorders",
            "FDA Drug Information - Ropeginterferon (Besremi)"
        ],
        "last_updated": "2025-02-18"
    },    "Rezurock": {
        "group": "Hematology - ROCK2 Inhibitor",
        "vietnamese_name": "Belumosudil, Rezurock",
        "administration": ["PO"],
        "indications": [
            "Bệnh ghép chống chủ mạn tính (chronic graft-versus-host disease, cGVHD) sau khi thất bại với ít nhất 2 liệu pháp hệ thống trước đó"
        ],
        "contraindications": [
            "Dị ứng belumosudil hoặc bất kỳ thành phần nào"
        ],
        "dosage": {
            "adult_200mg": "200mg PO x 1 lần/ngày",
            "adult_400mg": "400mg PO x 1 lần/ngày (nếu không đáp ứng với 200mg)",
            "notes": "Uống với thức ăn. Bắt đầu với 200mg/ngày, tăng lên 400mg/ngày nếu không đáp ứng. FDA phê duyệt 7/16/2021."
        },
        "renal_adjustment": {
            "normal": "Không cần chỉnh liều",
            "30_60": "Không cần chỉnh liều",
            "under_30": "Thận trọng, dữ liệu hạn chế"
        },
        "side_effects": [
            "Tăng men gan (ALT, AST) - phổ biến, có thể nghiêm trọng",
            "Buồn nôn - phổ biến",
            "Tiêu chảy - phổ biến",
            "Mệt mỏi - phổ biến",
            "Nhiễm trùng - phổ biến, có thể nghiêm trọng",
            "Giảm bạch cầu, tiểu cầu - phổ biến",
            "Phát ban - phổ biến",
            "Đau cơ, đau khớp - phổ biến",
            "Viêm phổi kẽ (interstitial lung disease - ILD) - hiếm nhưng NGUY HIỂM"
        ],
        "interactions": [
            "CYP3A4 inhibitors (ketoconazole, clarithromycin): tăng nồng độ belumosudil - giảm liều belumosudil",
            "CYP3A4 inducers (rifampin, carbamazepine): giảm nồng độ belumosudil - tránh dùng",
            "P-gp inhibitors: tăng nồng độ belumosudil - thận trọng"
        ],
        "pregnancy": "D",
        "mechanism_of_action": "Belumosudil là ROCK2 (Rho-associated coiled-coil containing protein kinase 2) inhibitor. ROCK2 là enzyme quan trọng trong signaling pathway của tế bào T. Trong cGVHD, tế bào T của người cho (donor) tấn công các mô của người nhận (recipient) → viêm và tổn thương mô. Belumosudil ức chế ROCK2 → ức chế signaling của tế bào T → giảm hoạt động của tế bào T → giảm viêm và tổn thương mô trong cGVHD. Dẫn đến: cải thiện triệu chứng và giảm mức độ nghiêm trọng của cGVHD. Belumosudil được FDA phê duyệt 7/16/2021 để điều trị cGVHD sau khi thất bại với ít nhất 2 liệu pháp hệ thống trước đó.",
        "monitoring": [
            "Chức năng gan (ALT, AST) - QUAN TRỌNG: tăng men gan phổ biến, theo dõi trước điều trị và mỗi 2 tuần trong 2 tháng đầu",
            "Công thức máu (CBC) - giảm bạch cầu, tiểu cầu phổ biến",
            "Dấu hiệu viêm phổi kẽ (ILD) - ho, khó thở - QUAN TRỌNG",
            "Nhiễm trùng - tăng nguy cơ nhiễm trùng, đặc biệt nhiễm trùng cơ hội",
            "Đáp ứng điều trị (triệu chứng cGVHD, mức độ nghiêm trọng)"
        ],
        "precautions": [
            "TĂNG MEN GAN - phổ biến, có thể nghiêm trọng. Theo dõi chức năng gan trước điều trị và mỗi 2 tuần trong 2 tháng đầu. Ngừng hoặc giảm liều nếu ALT/AST >5x ULN.",
            "VIÊM PHỔI KẼ (ILD) - hiếm nhưng NGUY HIỂM. Ngừng ngay nếu có dấu hiệu ILD.",
            "Nhiễm trùng - tăng nguy cơ nhiễm trùng, đặc biệt nhiễm trùng cơ hội, theo dõi dấu hiệu",
            "Giảm bạch cầu, tiểu cầu - phổ biến, theo dõi CBC",
            "CHỐNG CHỈ ĐỊNH trong thai kỳ (category D)",
            "Thận trọng với CYP3A4 inhibitors và inducers",
            "Uống với thức ăn để tăng hấp thu"
        ],
        "pharmacokinetics": {
            "half_life": "~19 giờ",
            "onset": "Vài tuần đến vài tháng",
            "duration": "Ngắn (cần dùng hàng ngày)",
            "protein_binding": "~99%",
            "metabolism": "Chủ yếu qua CYP3A4",
            "clearance": "Thải trừ qua phân (80%) và nước tiểu (20%)"
        },
        "storage": "Bảo quản ở nhiệt độ phòng (20-25°C), tránh ẩm, tránh ánh sáng",
        "black_box_warnings": "TĂNG MEN GAN - có thể gây tăng men gan nghiêm trọng. Theo dõi chức năng gan trước điều trị và mỗi 2 tuần trong 2 tháng đầu. VIÊM PHỔI KẼ (ILD) - có thể gây viêm phổi kẽ nghiêm trọng. NHIỄM TRÙNG - tăng nguy cơ nhiễm trùng nghiêm trọng. CHỐNG CHỈ ĐỊNH trong thai kỳ (category D).",
        "drug_interactions": {
            "major": [
                {
                    "drug": "Strong CYP3A4 inhibitors (ketoconazole, itraconazole, clarithromycin, ritonavir)",
                    "mechanism": "Ức chế CYP3A4 → giảm chuyển hóa belumosudil",
                    "effect": "Tăng nồng độ belumosudil, tăng nguy cơ tác dụng phụ",
                    "management": "Giảm liều belumosudil xuống 200mg x 1 lần/ngày."
                },
                {
                    "drug": "Strong CYP3A4 inducers (rifampin, carbamazepine, phenytoin, St. John's wort)",
                    "mechanism": "Cảm ứng CYP3A4 → tăng chuyển hóa belumosudil",
                    "effect": "Giảm nồng độ belumosudil, giảm hiệu quả",
                    "management": "TRÁNH dùng đồng thời. Nếu không thể tránh, theo dõi đáp ứng lâm sàng chặt chẽ."
                }
            ],
            "moderate": [
                {
                    "drug": "P-gp inhibitors (verapamil, diltiazem, cyclosporine)",
                    "mechanism": "Ức chế P-gp → giảm thải trừ belumosudil",
                    "effect": "Tăng nồng độ belumosudil, tăng nguy cơ tác dụng phụ",
                    "management": "Thận trọng. Theo dõi tác dụng phụ."
                }
            ],
            "minor": []
        },
        "contraindications_detail": {
            "tuyệt_đối": [
                "Dị ứng belumosudil hoặc bất kỳ thành phần nào",
                "Có thai (category D) - CHỐNG CHỈ ĐỊNH"
            ],
            "tương_đối": [
                "Suy gan nặng - thận trọng",
                "Suy thận nặng - thận trọng",
                "Nhiễm trùng đang hoạt động - thận trọng"
            ]
        },
        "pregnancy_lactation": {
            "fda_category": "D",
            "pregnancy_details": "CHỐNG CHỈ ĐỊNH trong thai kỳ. Belumosudil là FDA category D - có nguy cơ cho thai nhi, gây dị tật thai nhi.",
            "lactation": {
                "safety": "Unknown",
                "details": "Chưa biết có bài tiết vào sữa mẹ hay không.",
                "recommendation": "Không dùng khi cho con bú."
            }
        },
        "hepatic_adjustment": {
            "mild": "Không đổi",
            "moderate": "Thận trọng",
            "severe": "Thận trọng, dữ liệu hạn chế",
            "notes": "Belumosudil chuyển hóa chủ yếu qua CYP3A4 ở gan. Thận trọng ở suy gan. Theo dõi chức năng gan chặt chẽ."
        },
        "overdose_management": {
            "symptoms": [
                "Tăng men gan nặng",
                "Tiêu chảy nặng",
                "Buồn nôn nặng",
                "Viêm phổi kẽ nặng"
            ],
            "antidote": "Không có antidote đặc hiệu",
            "treatment": [
                "Ngừng belumosudil",
                "Theo dõi chức năng gan",
                "Điều trị ILD nếu có",
                "Điều trị hỗ trợ"
            ],
            "monitoring": "Dấu hiệu sinh tồn, chức năng gan, dấu hiệu ILD"
        },
        "reversal_agents": {
            "available": False,
            "agents": []
        },
        "administration_instructions": {
            "oral": {
                "with_food": "Uống với thức ăn để tăng hấp thu",
                "timing": "Uống 1 lần/ngày, 200mg hoặc 400mg mỗi lần. Uống cùng thời điểm mỗi ngày."
            }
        },
        "references": {
            "primary_sources": [
                "FDA Drug Label - Belumosudil (Rezurock)",
                "FDA Approval Date: 7/16/2021",
                "FDA-approved use: To treat chronic graft-versus-host disease after failure of at least two prior lines of systemic therapy",
                "UpToDate - Belumosudil: Drug information",
                "NCCN Guidelines - Hematopoietic Cell Transplantation"
            ],
            "last_updated": "2025-02-18",
            "evidence_level": "A - FDA-approved 7/16/2021"
        },
        "risk_flags": {
            "high_alert": True,
            "narrow_therapeutic_index": False,
            "bleeding_risk": False,
            "organ_toxicity": ["Hepatic (elevated transaminases)", "Pulmonary (interstitial lung disease - ILD)"],
            "qt_prolongation": False,
            "hepatotoxicity": True,
            "nephrotoxicity": False,
            "requires_monitoring": ["Hepatic function (ALT, AST) - CRITICAL (before treatment and every 2 weeks for first 2 months)", "CBC", "Signs of ILD - CRITICAL", "Signs of infection - CRITICAL", "Treatment response"]
        },
        "guideline_tags": [
            "NCCN Guidelines - Hematopoietic Cell Transplantation",
            "FDA Black Box Warning - Belumosudil and Hepatotoxicity",
            "FDA Black Box Warning - Belumosudil and ILD",
            "FDA Drug Information - Belumosudil (Rezurock)"
        ],
        "last_updated": "2025-02-18"
    },    "Empaveli": {
        "group": "Hematology - Complement C3 Inhibitor",
        "vietnamese_name": "Pegcetacoplan, Empaveli",
        "administration": ["SC"],
        "indications": [
            "Tan máu kịch phát ban đêm (paroxysmal nocturnal hemoglobinuria, PNH) ở người lớn"
        ],
        "contraindications": [
            "Dị ứng pegcetacoplan hoặc bất kỳ thành phần nào",
            "Nhiễm trùng Neisseria meningitidis đang hoạt động hoặc chưa được tiêm phòng"
        ],
        "dosage": {
            "adult_loading": "1080mg SC x 2 lần/tuần (liều đầu tiên)",
            "adult_maintenance": "1080mg SC x 2 lần/tuần",
            "notes": "Tiêm dưới da 2 lần/tuần. Có thể tự tiêm sau khi được hướng dẫn. FDA phê duyệt 5/14/2021. CẦN TIÊM PHÒNG Neisseria meningitidis trước khi bắt đầu điều trị."
        },
        "renal_adjustment": {
            "normal": "Không cần chỉnh liều",
            "30_60": "Không cần chỉnh liều",
            "under_30": "Không cần chỉnh liều"
        },
        "side_effects": [
            "Phản ứng tại chỗ tiêm (đau, đỏ, sưng) - phổ biến",
            "Nhiễm trùng - phổ biến, có thể nghiêm trọng",
            "Nhiễm trùng Neisseria meningitidis - hiếm nhưng NGUY HIỂM, có thể tử vong",
            "Buồn nôn - phổ biến",
            "Tiêu chảy - phổ biến",
            "Đau bụng - phổ biến",
            "Mệt mỏi - phổ biến",
            "Đau đầu - phổ biến",
            "Dị ứng (hiếm)"
        ],
        "interactions": [
            "Không có tương tác dược động học quan trọng",
            "Vaccine sống: có thể làm giảm đáp ứng vaccine"
        ],
        "pregnancy": "C",
        "mechanism_of_action": "Pegcetacoplan là complement C3 inhibitor, là peptide gắn với polyethylene glycol (PEG) để kéo dài thời gian tác dụng. Trong PNH, thiếu các protein bảo vệ trên bề mặt hồng cầu (CD55, CD59) → hồng cầu dễ bị tấn công bởi complement system → tan máu. Pegcetacoplan ức chế C3 (thành phần trung tâm của complement cascade) → ngăn chặn complement cascade → giảm tan máu. Dẫn đến: giảm tan máu và cải thiện thiếu máu trong PNH. Pegcetacoplan được FDA phê duyệt 5/14/2021 để điều trị PNH ở người lớn. Đặc điểm: (1) Ức chế C3 (khác với eculizumab ức chế C5), (2) Dạng SC, tiện lợi hơn so với IV, (3) CẦN TIÊM PHÒNG Neisseria meningitidis trước điều trị.",
        "monitoring": [
            "Công thức máu (CBC) - đánh giá đáp ứng điều trị (giảm tan máu)",
            "LDH (lactate dehydrogenase) - marker tan máu, theo dõi định kỳ",
            "Haptoglobin - marker tan máu, theo dõi định kỳ",
            "Dấu hiệu nhiễm trùng - tăng nguy cơ nhiễm trùng, đặc biệt Neisseria meningitidis",
            "Phản ứng tại chỗ tiêm",
            "Dấu hiệu dị ứng"
        ],
        "precautions": [
            "NHIỄM TRÙNG Neisseria meningitidis - hiếm nhưng NGUY HIỂM, có thể tử vong. CẦN TIÊM PHÒNG Neisseria meningitidis trước khi bắt đầu điều trị. Theo dõi dấu hiệu nhiễm trùng (sốt, đau đầu, cứng cổ, phát ban).",
            "Tăng nguy cơ nhiễm trùng - do ức chế complement, theo dõi dấu hiệu nhiễm trùng",
            "Phản ứng tại chỗ tiêm - phổ biến, thay đổi vị trí tiêm mỗi lần",
            "Cần tiêm 2 lần/tuần - tuân thủ điều trị quan trọng",
            "Có thể tự tiêm sau khi được hướng dẫn",
            "Không ngừng đột ngột - có thể gây tan máu nặng"
        ],
        "pharmacokinetics": {
            "half_life": "~8-10 ngày",
            "onset": "Vài tuần",
            "duration": "3-4 ngày (dùng 2 lần/tuần)",
            "protein_binding": "Không rõ",
            "metabolism": "Chuyển hóa qua protease",
            "clearance": "Thải trừ qua thận"
        },
        "storage": "Bảo quản trong tủ lạnh (2-8°C), tránh đông lạnh. Có thể để ở nhiệt độ phòng (≤25°C) tối đa 30 ngày.",
        "black_box_warnings": "NHIỄM TRÙNG Neisseria meningitidis - có thể gây nhiễm trùng Neisseria meningitidis nghiêm trọng, có thể tử vong. CẦN TIÊM PHÒNG Neisseria meningitidis trước khi bắt đầu điều trị. Theo dõi dấu hiệu nhiễm trùng (sốt, đau đầu, cứng cổ, phát ban).",
        "drug_interactions": {
            "major": [],
            "moderate": [
                {
                    "drug": "Vaccine sống",
                    "mechanism": "Pegcetacoplan ức chế complement, có thể ảnh hưởng đến đáp ứng miễn dịch",
                    "effect": "Giảm đáp ứng vaccine",
                    "management": "Thận trọng. Hoàn thành tiêm phòng trước khi bắt đầu điều trị nếu có thể."
                }
            ],
            "minor": []
        },
        "contraindications_detail": {
            "tuyệt_đối": [
                "Dị ứng pegcetacoplan hoặc bất kỳ thành phần nào",
                "Nhiễm trùng Neisseria meningitidis đang hoạt động"
            ],
            "tương_đối": [
                "Chưa được tiêm phòng Neisseria meningitidis - CẦN tiêm phòng trước điều trị",
                "Nhiễm trùng đang hoạt động - thận trọng"
            ]
        },
        "pregnancy_lactation": {
            "fda_category": "C",
            "pregnancy_details": "Pegcetacoplan là FDA category C. Có nguy cơ cho thai nhi. Chỉ dùng khi lợi ích > nguy cơ.",
            "lactation": {
                "safety": "Unknown",
                "details": "Chưa biết có bài tiết vào sữa mẹ hay không. Peptide lớn, hấp thu qua đường tiêu hóa trẻ có thể hạn chế.",
                "recommendation": "Thận trọng khi cho con bú."
            }
        },
        "hepatic_adjustment": {
            "mild": "Không đổi",
            "moderate": "Không đổi",
            "severe": "Không đổi",
            "notes": "Pegcetacoplan chuyển hóa qua protease, không phụ thuộc gan đáng kể."
        },
        "overdose_management": {
            "symptoms": [
                "Phản ứng tại chỗ tiêm nặng",
                "Nhiễm trùng nặng",
                "Dị ứng nặng"
            ],
            "antidote": "Không có antidote đặc hiệu",
            "treatment": [
                "Ngừng pegcetacoplan",
                "Điều trị nhiễm trùng nếu có",
                "Điều trị phản ứng dị ứng nếu có",
                "Điều trị hỗ trợ"
            ],
            "monitoring": "Dấu hiệu sinh tồn, dấu hiệu nhiễm trùng, phản ứng tại chỗ tiêm, dấu hiệu dị ứng"
        },
        "reversal_agents": {
            "available": False,
            "agents": []
        },
        "administration_instructions": {
            "sc": {
                "reconstitution": "Dạng tiêm sẵn (pre-filled syringe)",
                "injection_site": "Vùng bụng, đùi, hoặc cánh tay. Thay đổi vị trí tiêm mỗi lần.",
                "notes": "Tiêm dưới da 2 lần/tuần, 1080mg mỗi lần. Có thể tự tiêm sau khi được hướng dẫn. Bảo quản trong tủ lạnh, để ở nhiệt độ phòng 30 phút trước khi tiêm. CẦN TIÊM PHÒNG Neisseria meningitidis trước khi bắt đầu điều trị."
            }
        },
        "references": {
            "primary_sources": [
                "FDA Drug Label - Pegcetacoplan (Empaveli)",
                "FDA Approval Date: 5/14/2021",
                "FDA-approved use: To treat paroxysmal nocturnal hemoglobinuria",
                "UpToDate - Pegcetacoplan: Drug information",
                "ASH Guidelines - Paroxysmal Nocturnal Hemoglobinuria"
            ],
            "last_updated": "2025-02-18",
            "evidence_level": "A - FDA-approved 5/14/2021"
        },
        "risk_flags": {
            "high_alert": True,
            "narrow_therapeutic_index": False,
            "bleeding_risk": False,
            "organ_toxicity": ["Infectious (Neisseria meningitidis infection - rare but serious)"],
            "qt_prolongation": False,
            "hepatotoxicity": False,
            "nephrotoxicity": False,
            "requires_monitoring": ["CBC (assess treatment response)", "LDH, haptoglobin (markers of hemolysis)", "Signs of infection - CRITICAL (especially Neisseria meningitidis)", "Injection site reactions"]
        },
        "guideline_tags": [
            "ASH Guidelines - Paroxysmal Nocturnal Hemoglobinuria",
            "FDA Black Box Warning - Pegcetacoplan and Neisseria meningitidis Infection",
            "FDA Drug Information - Pegcetacoplan (Empaveli)"
        ],
        "last_updated": "2025-02-18"
    },







    "Vonjo": {
                "group": "FDA Approved 2022",
                "vietnamese_name": "Pacritinib, Vonjo",
                "administration": [
                        "PO",
                ],
                "indications": [
                        "To treat intermediate or high-risk primary or secondary myelofibrosis in adults with low platelets",
                ],
                "contraindications": [
                        "Dị ứng pacritinib hoặc bất kỳ thành phần nào",
                ],
                "dosage": {
                        "adult_standard": "Theo chỉ định của bác sĩ",
                        "notes": "FDA phê duyệt 2022. To treat intermediate or high-risk primary or secondary myelofibrosis in adults with low platelets",
                },
                "renal_adjustment": {
                        "normal": "Không cần chỉnh liều",
                        "30_60": "Thận trọng",
                        "under_30": "Thận trọng, dữ liệu hạn chế",
                },
                "side_effects": [
                        "Cần bổ sung thông tin từ tài liệu FDA",
                ],
                "interactions": [
                        "Cần bổ sung thông tin từ tài liệu FDA",
                ],
                "pregnancy": "C",
                "mechanism_of_action": "Pacritinib được FDA phê duyệt 2022 để to treat intermediate or high-risk primary or secondary myelofibrosis in adults with low platelets. Cần bổ sung thông tin chi tiết về cơ chế tác dụng.",
                "monitoring": [
                        "Theo dõi đáp ứng điều trị",
                        "Theo dõi tác dụng phụ",
                ],
                "precautions": [
                        "Dị ứng pacritinib",
                        "Cần bổ sung thông tin từ tài liệu FDA",
                ],
                "pharmacokinetics": {
                        "half_life": "Cần bổ sung",
                        "onset": "Cần bổ sung",
                        "duration": "Cần bổ sung",
                        "protein_binding": "Cần bổ sung",
                        "metabolism": "Cần bổ sung",
                        "clearance": "Cần bổ sung",
                },
                "storage": "Bảo quản theo hướng dẫn của nhà sản xuất",
                "black_box_warnings": "Cần kiểm tra tài liệu FDA",
                "drug_interactions": {
                        "major": [],
                        "moderate": [],
                        "minor": [],
                },
                "contraindications_detail": {
                        "tuyệt_đối": [
                                "Dị ứng pacritinib hoặc bất kỳ thành phần nào",
                        ],
                        "tương_đối": [],
                },
                "pregnancy_lactation": {
                        "fda_category": "C",
                        "pregnancy_details": "Cần bổ sung thông tin từ tài liệu FDA",
                        "lactation": {
                                "safety": "Unknown",
                                "details": "Chưa biết có bài tiết vào sữa mẹ hay không",
                                "recommendation": "Thận trọng khi cho con bú",
                        },
                },
                "hepatic_adjustment": {
                        "mild": "Không đổi",
                        "moderate": "Thận trọng",
                        "severe": "Thận trọng, dữ liệu hạn chế",
                        "notes": "Cần bổ sung thông tin từ tài liệu FDA",
                },
                "overdose_management": {
                        "symptoms": [
                                "Cần bổ sung",
                        ],
                        "antidote": "Không có antidote đặc hiệu",
                        "treatment": [
                                "Điều trị hỗ trợ",
                        ],
                        "monitoring": "Theo dõi dấu hiệu sinh tồn",
                },
                "reversal_agents": {
                        "available": False,
                        "agents": [],
                },
                "administration_instructions": {
                        "oral": {
                                "with_food": "Cần bổ sung",
                                "timing": "Cần bổ sung",
                        },
                },
                "references": {
                        "primary_sources": [
                                "FDA Drug Label - Pacritinib (Vonjo)",
                                "FDA Approval Date: 2022",
                                "FDA-approved use: To treat intermediate or high-risk primary or secondary myelofibrosis in adults with low platelets",
                        ],
                        "last_updated": "2026-01-15",
                        "evidence_level": "A - FDA-approved 2022",
                },
                "risk_flags": {
                        "high_alert": False,
                        "narrow_therapeutic_index": False,
                        "bleeding_risk": False,
                        "organ_toxicity": [],
                        "qt_prolongation": False,
                        "hepatotoxicity": False,
                        "nephrotoxicity": False,
                        "requires_monitoring": [
                                "Clinical response",
                                "Adverse effects",
                        ],
                },
                "guideline_tags": [
                        "FDA Drug Information - Pacritinib (Vonjo)",
                ],
                "last_updated": "2026-01-15",
        },
    "Hympavzi": {
                "group": "FDA Approved 2024",
                "vietnamese_name": "Marstacimab, Hympavzi",
                "administration": [
                        "PO",
                ],
                "indications": [
                        "To prevent or reduce bleeding episodes related to hemophilia A or B",
                ],
                "contraindications": [
                        "Dị ứng marstacimab hoặc bất kỳ thành phần nào",
                ],
                "dosage": {
                        "adult_standard": "Theo chỉ định của bác sĩ",
                        "notes": "FDA phê duyệt 2024. To prevent or reduce bleeding episodes related to hemophilia A or B",
                },
                "renal_adjustment": {
                        "normal": "Không cần chỉnh liều",
                        "30_60": "Thận trọng",
                        "under_30": "Thận trọng, dữ liệu hạn chế",
                },
                "side_effects": [
                        "Cần bổ sung thông tin từ tài liệu FDA",
                ],
                "interactions": [
                        "Cần bổ sung thông tin từ tài liệu FDA",
                ],
                "pregnancy": "C",
                "mechanism_of_action": "Marstacimab được FDA phê duyệt 2024 để to prevent or reduce bleeding episodes related to hemophilia a or b. Cần bổ sung thông tin chi tiết về cơ chế tác dụng.",
                "monitoring": [
                        "Theo dõi đáp ứng điều trị",
                        "Theo dõi tác dụng phụ",
                ],
                "precautions": [
                        "Dị ứng marstacimab",
                        "Cần bổ sung thông tin từ tài liệu FDA",
                ],
                "pharmacokinetics": {
                        "half_life": "Cần bổ sung",
                        "onset": "Cần bổ sung",
                        "duration": "Cần bổ sung",
                        "protein_binding": "Cần bổ sung",
                        "metabolism": "Cần bổ sung",
                        "clearance": "Cần bổ sung",
                },
                "storage": "Bảo quản theo hướng dẫn của nhà sản xuất",
                "black_box_warnings": "Cần kiểm tra tài liệu FDA",
                "drug_interactions": {
                        "major": [],
                        "moderate": [],
                        "minor": [],
                },
                "contraindications_detail": {
                        "tuyệt_đối": [
                                "Dị ứng marstacimab hoặc bất kỳ thành phần nào",
                        ],
                        "tương_đối": [],
                },
                "pregnancy_lactation": {
                        "fda_category": "C",
                        "pregnancy_details": "Cần bổ sung thông tin từ tài liệu FDA",
                        "lactation": {
                                "safety": "Unknown",
                                "details": "Chưa biết có bài tiết vào sữa mẹ hay không",
                                "recommendation": "Thận trọng khi cho con bú",
                        },
                },
                "hepatic_adjustment": {
                        "mild": "Không đổi",
                        "moderate": "Thận trọng",
                        "severe": "Thận trọng, dữ liệu hạn chế",
                        "notes": "Cần bổ sung thông tin từ tài liệu FDA",
                },
                "overdose_management": {
                        "symptoms": [
                                "Cần bổ sung",
                        ],
                        "antidote": "Không có antidote đặc hiệu",
                        "treatment": [
                                "Điều trị hỗ trợ",
                        ],
                        "monitoring": "Theo dõi dấu hiệu sinh tồn",
                },
                "reversal_agents": {
                        "available": False,
                        "agents": [],
                },
                "administration_instructions": {
                        "oral": {
                                "with_food": "Cần bổ sung",
                                "timing": "Cần bổ sung",
                        },
                },
                "references": {
                        "primary_sources": [
                                "FDA Drug Label - Marstacimab (Hympavzi)",
                                "FDA Approval Date: 2024",
                                "FDA-approved use: To prevent or reduce bleeding episodes related to hemophilia A or B",
                        ],
                        "last_updated": "2026-01-15",
                        "evidence_level": "A - FDA-approved 2024",
                },
                "risk_flags": {
                        "high_alert": False,
                        "narrow_therapeutic_index": False,
                        "bleeding_risk": False,
                        "organ_toxicity": [],
                        "qt_prolongation": False,
                        "hepatotoxicity": False,
                        "nephrotoxicity": False,
                        "requires_monitoring": [
                                "Clinical response",
                                "Adverse effects",
                        ],
                },
                "guideline_tags": [
                        "FDA Drug Information - Marstacimab (Hympavzi)",
                ],
                "last_updated": "2026-01-15",
        },
    "Voydeya": {
                "group": "FDA Approved 2024",
                "vietnamese_name": "Danicopan, Voydeya",
                "administration": [
                        "PO",
                ],
                "indications": [
                        "To treat extravascular hemolysis with paroxysmal nocturnal hemoglobinuria",
                ],
                "contraindications": [
                        "Dị ứng danicopan hoặc bất kỳ thành phần nào",
                ],
                "dosage": {
                        "adult_standard": "Theo chỉ định của bác sĩ",
                        "notes": "FDA phê duyệt 2024. To treat extravascular hemolysis with paroxysmal nocturnal hemoglobinuria",
                },
                "renal_adjustment": {
                        "normal": "Không cần chỉnh liều",
                        "30_60": "Thận trọng",
                        "under_30": "Thận trọng, dữ liệu hạn chế",
                },
                "side_effects": [
                        "Cần bổ sung thông tin từ tài liệu FDA",
                ],
                "interactions": [
                        "Cần bổ sung thông tin từ tài liệu FDA",
                ],
                "pregnancy": "C",
                "mechanism_of_action": "Danicopan được FDA phê duyệt 2024 để to treat extravascular hemolysis with paroxysmal nocturnal hemoglobinuria. Cần bổ sung thông tin chi tiết về cơ chế tác dụng.",
                "monitoring": [
                        "Theo dõi đáp ứng điều trị",
                        "Theo dõi tác dụng phụ",
                ],
                "precautions": [
                        "Dị ứng danicopan",
                        "Cần bổ sung thông tin từ tài liệu FDA",
                ],
                "pharmacokinetics": {
                        "half_life": "Cần bổ sung",
                        "onset": "Cần bổ sung",
                        "duration": "Cần bổ sung",
                        "protein_binding": "Cần bổ sung",
                        "metabolism": "Cần bổ sung",
                        "clearance": "Cần bổ sung",
                },
                "storage": "Bảo quản theo hướng dẫn của nhà sản xuất",
                "black_box_warnings": "Cần kiểm tra tài liệu FDA",
                "drug_interactions": {
                        "major": [],
                        "moderate": [],
                        "minor": [],
                },
                "contraindications_detail": {
                        "tuyệt_đối": [
                                "Dị ứng danicopan hoặc bất kỳ thành phần nào",
                        ],
                        "tương_đối": [],
                },
                "pregnancy_lactation": {
                        "fda_category": "C",
                        "pregnancy_details": "Cần bổ sung thông tin từ tài liệu FDA",
                        "lactation": {
                                "safety": "Unknown",
                                "details": "Chưa biết có bài tiết vào sữa mẹ hay không",
                                "recommendation": "Thận trọng khi cho con bú",
                        },
                },
                "hepatic_adjustment": {
                        "mild": "Không đổi",
                        "moderate": "Thận trọng",
                        "severe": "Thận trọng, dữ liệu hạn chế",
                        "notes": "Cần bổ sung thông tin từ tài liệu FDA",
                },
                "overdose_management": {
                        "symptoms": [
                                "Cần bổ sung",
                        ],
                        "antidote": "Không có antidote đặc hiệu",
                        "treatment": [
                                "Điều trị hỗ trợ",
                        ],
                        "monitoring": "Theo dõi dấu hiệu sinh tồn",
                },
                "reversal_agents": {
                        "available": False,
                        "agents": [],
                },
                "administration_instructions": {
                        "oral": {
                                "with_food": "Cần bổ sung",
                                "timing": "Cần bổ sung",
                        },
                },
                "references": {
                        "primary_sources": [
                                "FDA Drug Label - Danicopan (Voydeya)",
                                "FDA Approval Date: 2024",
                                "FDA-approved use: To treat extravascular hemolysis with paroxysmal nocturnal hemoglobinuria",
                        ],
                        "last_updated": "2026-01-15",
                        "evidence_level": "A - FDA-approved 2024",
                },
                "risk_flags": {
                        "high_alert": False,
                        "narrow_therapeutic_index": False,
                        "bleeding_risk": False,
                        "organ_toxicity": [],
                        "qt_prolongation": False,
                        "hepatotoxicity": False,
                        "nephrotoxicity": False,
                        "requires_monitoring": [
                                "Clinical response",
                                "Adverse effects",
                        ],
                },
                "guideline_tags": [
                        "FDA Drug Information - Danicopan (Voydeya)",
                ],
                "last_updated": "2026-01-15",
        },
    "Qfitlia": {
                "group": "FDA Approved 2025",
                "vietnamese_name": "Fitusiran, Qfitlia",
                "administration": [
                        "PO",
                ],
                "indications": [
                        "To prevent or reduce the frequency of bleeding episodes in hemophilia A or B",
                ],
                "contraindications": [
                        "Dị ứng fitusiran hoặc bất kỳ thành phần nào",
                ],
                "dosage": {
                        "adult_standard": "Theo chỉ định của bác sĩ",
                        "notes": "FDA phê duyệt 2025. To prevent or reduce the frequency of bleeding episodes in hemophilia A or B",
                },
                "renal_adjustment": {
                        "normal": "Không cần chỉnh liều",
                        "30_60": "Thận trọng",
                        "under_30": "Thận trọng, dữ liệu hạn chế",
                },
                "side_effects": [
                        "Cần bổ sung thông tin từ tài liệu FDA",
                ],
                "interactions": [
                        "Cần bổ sung thông tin từ tài liệu FDA",
                ],
                "pregnancy": "C",
                "mechanism_of_action": "Fitusiran được FDA phê duyệt 2025 để to prevent or reduce the frequency of bleeding episodes in hemophilia a or b. Cần bổ sung thông tin chi tiết về cơ chế tác dụng.",
                "monitoring": [
                        "Theo dõi đáp ứng điều trị",
                        "Theo dõi tác dụng phụ",
                ],
                "precautions": [
                        "Dị ứng fitusiran",
                        "Cần bổ sung thông tin từ tài liệu FDA",
                ],
                "pharmacokinetics": {
                        "half_life": "Cần bổ sung",
                        "onset": "Cần bổ sung",
                        "duration": "Cần bổ sung",
                        "protein_binding": "Cần bổ sung",
                        "metabolism": "Cần bổ sung",
                        "clearance": "Cần bổ sung",
                },
                "storage": "Bảo quản theo hướng dẫn của nhà sản xuất",
                "black_box_warnings": "Cần kiểm tra tài liệu FDA",
                "drug_interactions": {
                        "major": [],
                        "moderate": [],
                        "minor": [],
                },
                "contraindications_detail": {
                        "tuyệt_đối": [
                                "Dị ứng fitusiran hoặc bất kỳ thành phần nào",
                        ],
                        "tương_đối": [],
                },
                "pregnancy_lactation": {
                        "fda_category": "C",
                        "pregnancy_details": "Cần bổ sung thông tin từ tài liệu FDA",
                        "lactation": {
                                "safety": "Unknown",
                                "details": "Chưa biết có bài tiết vào sữa mẹ hay không",
                                "recommendation": "Thận trọng khi cho con bú",
                        },
                },
                "hepatic_adjustment": {
                        "mild": "Không đổi",
                        "moderate": "Thận trọng",
                        "severe": "Thận trọng, dữ liệu hạn chế",
                        "notes": "Cần bổ sung thông tin từ tài liệu FDA",
                },
                "overdose_management": {
                        "symptoms": [
                                "Cần bổ sung",
                        ],
                        "antidote": "Không có antidote đặc hiệu",
                        "treatment": [
                                "Điều trị hỗ trợ",
                        ],
                        "monitoring": "Theo dõi dấu hiệu sinh tồn",
                },
                "reversal_agents": {
                        "available": False,
                        "agents": [],
                },
                "administration_instructions": {
                        "oral": {
                                "with_food": "Cần bổ sung",
                                "timing": "Cần bổ sung",
                        },
                },
                "references": {
                        "primary_sources": [
                                "FDA Drug Label - Fitusiran (Qfitlia)",
                                "FDA Approval Date: 2025",
                                "FDA-approved use: To prevent or reduce the frequency of bleeding episodes in hemophilia A or B",
                        ],
                        "last_updated": "2026-01-15",
                        "evidence_level": "A - FDA-approved 2025",
                },
                "risk_flags": {
                        "high_alert": False,
                        "narrow_therapeutic_index": False,
                        "bleeding_risk": False,
                        "organ_toxicity": [],
                        "qt_prolongation": False,
                        "hepatotoxicity": False,
                        "nephrotoxicity": False,
                        "requires_monitoring": [
                                "Clinical response",
                                "Adverse effects",
                        ],
                },
                "guideline_tags": [
                        "FDA Drug Information - Fitusiran (Qfitlia)",
                ],
                "last_updated": "2026-01-15",
        },
    "Wayrilz": {
                "group": "FDA Approved 2025",
                "vietnamese_name": "Rilzabrutinib, Wayrilz",
                "administration": [
                        "PO",
                ],
                "indications": [
                        "To treat persistent or chronic immune thrombocytopenia that has not sufficiently responded to immunoglobulins, anti-D therapy, or corticosteroids",
                ],
                "contraindications": [
                        "Dị ứng rilzabrutinib hoặc bất kỳ thành phần nào",
                ],
                "dosage": {
                        "adult_standard": "Theo chỉ định của bác sĩ",
                        "notes": "FDA phê duyệt 2025. To treat persistent or chronic immune thrombocytopenia that has not sufficiently responded to immunoglobulins, anti-D therapy, or corticosteroids",
                },
                "renal_adjustment": {
                        "normal": "Không cần chỉnh liều",
                        "30_60": "Thận trọng",
                        "under_30": "Thận trọng, dữ liệu hạn chế",
                },
                "side_effects": [
                        "Cần bổ sung thông tin từ tài liệu FDA",
                ],
                "interactions": [
                        "Cần bổ sung thông tin từ tài liệu FDA",
                ],
                "pregnancy": "C",
                "mechanism_of_action": "Rilzabrutinib được FDA phê duyệt 2025 để to treat persistent or chronic immune thrombocytopenia that has not sufficiently responded to immunoglobulins, anti-d therapy, or corticosteroids. Cần bổ sung thông tin chi tiết về cơ chế tác dụng.",
                "monitoring": [
                        "Theo dõi đáp ứng điều trị",
                        "Theo dõi tác dụng phụ",
                ],
                "precautions": [
                        "Dị ứng rilzabrutinib",
                        "Cần bổ sung thông tin từ tài liệu FDA",
                ],
                "pharmacokinetics": {
                        "half_life": "Cần bổ sung",
                        "onset": "Cần bổ sung",
                        "duration": "Cần bổ sung",
                        "protein_binding": "Cần bổ sung",
                        "metabolism": "Cần bổ sung",
                        "clearance": "Cần bổ sung",
                },
                "storage": "Bảo quản theo hướng dẫn của nhà sản xuất",
                "black_box_warnings": "Cần kiểm tra tài liệu FDA",
                "drug_interactions": {
                        "major": [],
                        "moderate": [],
                        "minor": [],
                },
                "contraindications_detail": {
                        "tuyệt_đối": [
                                "Dị ứng rilzabrutinib hoặc bất kỳ thành phần nào",
                        ],
                        "tương_đối": [],
                },
                "pregnancy_lactation": {
                        "fda_category": "C",
                        "pregnancy_details": "Cần bổ sung thông tin từ tài liệu FDA",
                        "lactation": {
                                "safety": "Unknown",
                                "details": "Chưa biết có bài tiết vào sữa mẹ hay không",
                                "recommendation": "Thận trọng khi cho con bú",
                        },
                },
                "hepatic_adjustment": {
                        "mild": "Không đổi",
                        "moderate": "Thận trọng",
                        "severe": "Thận trọng, dữ liệu hạn chế",
                        "notes": "Cần bổ sung thông tin từ tài liệu FDA",
                },
                "overdose_management": {
                        "symptoms": [
                                "Cần bổ sung",
                        ],
                        "antidote": "Không có antidote đặc hiệu",
                        "treatment": [
                                "Điều trị hỗ trợ",
                        ],
                        "monitoring": "Theo dõi dấu hiệu sinh tồn",
                },
                "reversal_agents": {
                        "available": False,
                        "agents": [],
                },
                "administration_instructions": {
                        "oral": {
                                "with_food": "Cần bổ sung",
                                "timing": "Cần bổ sung",
                        },
                },
                "references": {
                        "primary_sources": [
                                "FDA Drug Label - Rilzabrutinib (Wayrilz)",
                                "FDA Approval Date: 2025",
                                "FDA-approved use: To treat persistent or chronic immune thrombocytopenia that has not sufficiently responded to immunoglobulins, anti-D therapy, or corticosteroids",
                        ],
                        "last_updated": "2026-01-15",
                        "evidence_level": "A - FDA-approved 2025",
                },
                "risk_flags": {
                        "high_alert": False,
                        "narrow_therapeutic_index": False,
                        "bleeding_risk": False,
                        "organ_toxicity": [],
                        "qt_prolongation": False,
                        "hepatotoxicity": False,
                        "nephrotoxicity": False,
                        "requires_monitoring": [
                                "Clinical response",
                                "Adverse effects",
                        ],
                },
                "guideline_tags": [
                        "FDA Drug Information - Rilzabrutinib (Wayrilz)",
                ],
                "last_updated": "2026-01-15",
        },
}

__all__ = ['OTHER_HEMATOLOGY_DRUGS']
