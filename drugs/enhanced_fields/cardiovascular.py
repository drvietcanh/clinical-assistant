"""
Enhanced fields overrides - Cardiovascular
"""
from typing import Any, Dict


CARDIOVASCULAR_ENHANCED_FIELDS: Dict[str, Dict[str, Any]] = {
        # ======================== CARDIOVASCULAR: CENTRAL AGONISTS ========================
        "Clonidine": {
            "contraindications": {
                "tuyệt_đối": [
                    "Dị ứng clonidine",
                    "Block nhĩ thất độ 2–3 hoặc sick sinus syndrome không có máy tạo nhịp",
                ],
                "tương_đối": [
                    "Huyết áp thấp, nhịp tim chậm",
                    "Suy thận vừa–nặng",
                    "Đang dùng beta-blocker (tăng nguy cơ rebound hypertension khi ngừng clonidine)",
                ],
            },
            "drug_interactions": {
                "major": [
                    {
                        "drug": "Beta-blocker",
                        "mechanism": "Tăng nguy cơ nhịp tim chậm, block AV và rebound hypertension khi ngừng clonidine đột ngột",
                        "effect": "Hạ huyết áp, nhịp chậm nặng hoặc tăng huyết áp bật lại",
                        "management": "Nếu cần ngừng, NGỪNG beta-blocker vài ngày trước rồi mới giảm dần clonidine; theo dõi huyết áp, nhịp tim sát.",
                    }
                ],
                "moderate": [
                    {
                        "drug": "Tricyclic antidepressants (TCA)",
                        "mechanism": "Giảm đáp ứng của thụ thể alpha-2 trung ương",
                        "effect": "Giảm tác dụng hạ huyết áp của clonidine",
                        "management": "Theo dõi huyết áp, có thể cần tăng liều clonidine hoặc đổi nhóm.",
                    },
                    {
                        "drug": "Thuốc an thần, rượu, benzodiazepine",
                        "mechanism": "Tác dụng cộng hợp ức chế thần kinh trung ương",
                        "effect": "Tăng buồn ngủ, chóng mặt, tụt huyết áp tư thế",
                        "management": "Giảm liều, tránh lái xe/vận hành máy; theo dõi triệu chứng.",
                    },
                ],
                "minor": [],
            },
            "pregnancy_lactation": {
                "fda_category": "C",
                "pregnancy_details": (
                    "Dữ liệu hạn chế. Có thể dùng nếu lợi ích vượt trội nguy cơ, đặc biệt khi các lựa chọn an toàn hơn không hiệu quả. "
                    "Tránh ngừng đột ngột trong thai kỳ vì rebound hypertension có thể nguy hiểm cho mẹ và thai."
                ),
                "lactation": {
                    "safety": "Caution",
                    "details": "Bài tiết một lượng nhỏ vào sữa mẹ; có thể gây buồn ngủ, hạ huyết áp ở trẻ.",
                    "recommendation": "Theo dõi sát trẻ (bú kém, ngủ nhiều, nhịp tim chậm); cân nhắc đổi thuốc nếu xuất hiện triệu chứng.",
                },
            },
            "hepatic_adjustment": {
                "mild": "Không cần chỉnh liều nhưng theo dõi huyết áp và nhịp tim.",
                "moderate": "Thận trọng, cân nhắc liều khởi đầu thấp hơn.",
                "severe": "Thiếu dữ liệu; cân nhắc thuốc khác nếu có thể.",
                "notes": "Clonidine chuyển hóa một phần ở gan, song thải trừ qua thận cũng quan trọng.",
            },
            "overdose_management": {
                "symptoms": [
                    "Hạ huyết áp nặng",
                    "Nhịp tim chậm",
                    "Buồn ngủ, hôn mê",
                    "Suy hô hấp (hiếm)",
                    "Rebound hypertension sau pha đầu ức chế",
                ],
                "antidote": "Không có antidote đặc hiệu.",
                "treatment": [
                    "Đảm bảo đường thở, hỗ trợ hô hấp nếu cần.",
                    "Truyền dịch tĩnh mạch, dùng thuốc vận mạch nếu hạ huyết áp nặng.",
                    "Atropine cho nhịp tim chậm có triệu chứng.",
                    "Than hoạt tính nếu uống trong vòng 1–2 giờ (nếu bệnh nhân tỉnh/được bảo vệ đường thở).",
                ],
                "monitoring": "Theo dõi huyết áp, nhịp tim, ý thức, ECG liên tục cho đến khi ổn định.",
            },
            "reversal_agents": {
                "available": False,
                "agents": [],
                "notes": "Không có thuốc giải độc đặc hiệu; xử trí chủ yếu là hỗ trợ huyết động và hô hấp.",
            },
            "administration_instructions": {
                "oral": {
                    "with_food": "Có thể dùng cùng hoặc không cùng thức ăn.",
                    "timing": "Uống đều đặn mỗi ngày, cùng thời điểm; không tự ý ngừng đột ngột.",
                    "notes": "Nếu quên liều, uống ngay khi nhớ ra trừ khi gần liều kế tiếp. Không gộp liều.",
                },
                "transdermal": {
                    "site": "Dán lên vùng da sạch, khô, không kích ứng (thường vùng ngực/lưng trên).",
                    "frequency": "Thay patch mỗi 7 ngày, thay đổi vị trí dán để tránh kích ứng.",
                    "notes": "Không cắt patch. Đảm bảo patch dính chắc, tránh nguồn nhiệt trực tiếp.",
                },
            },
        },

        "Methyldopa": {
            "contraindications": {
                "tuyệt_đối": [
                    "Dị ứng methyldopa",
                    "Bệnh gan hoạt động hoặc tiền sử viêm gan do methyldopa",
                    "Dùng đồng thời MAO inhibitors",
                    "Pheochromocytoma",
                ],
                "tương_đối": [
                    "Thiếu máu tán huyết tự miễn",
                    "Suy thận vừa–nặng",
                    "Trầm cảm nặng",
                ],
            },
            "drug_interactions": {
                "major": [
                    {
                        "drug": "MAO inhibitors",
                        "mechanism": "Tăng tích tụ catecholamine và serotonin",
                        "effect": "Nguy cơ cơn tăng huyết áp hoặc hội chứng serotonin",
                        "management": "CHỐNG CHỈ ĐỊNH; cần ngừng MAOI trước khi dùng methyldopa.",
                    }
                ],
                "moderate": [
                    {
                        "drug": "Sắt đường uống",
                        "mechanism": "Giảm hấp thu methyldopa khi dùng cùng lúc",
                        "effect": "Giảm hiệu quả hạ huyết áp",
                        "management": "Dùng cách nhau ít nhất 2 giờ.",
                    },
                    {
                        "drug": "NSAID",
                        "mechanism": "Giảm tổng hợp prostaglandin thận",
                        "effect": "Giảm hiệu quả hạ huyết áp, tăng nguy cơ suy thận",
                        "management": "Theo dõi huyết áp và chức năng thận; hạn chế NSAID kéo dài.",
                    },
                ],
                "minor": [],
            },
            "pregnancy_lactation": {
                "fda_category": "B",
                "pregnancy_details": (
                    "Là một trong các thuốc ưu tiên điều trị tăng huyết áp thai kỳ, với dữ liệu an toàn lâu dài. "
                    "Theo dõi chức năng gan và huyết học định kỳ trong thai kỳ."
                ),
                "lactation": {
                    "safety": "Compatible",
                    "details": "Bài tiết lượng nhỏ vào sữa; thường an toàn cho trẻ bú mẹ.",
                    "recommendation": "Có thể dùng, nhưng theo dõi trẻ về buồn ngủ hoặc chậm bú.",
                },
            },
            "hepatic_adjustment": {
                "mild": "Thận trọng, theo dõi men gan.",
                "moderate": "Giảm liều và theo dõi ALT/AST định kỳ.",
                "severe": "Tránh dùng do nguy cơ độc gan.",
                "notes": "Methyldopa có thể gây viêm gan miễn dịch; cần ngừng thuốc nếu men gan tăng rõ hoặc xuất hiện triệu chứng gan.",
            },
            "overdose_management": {
                "symptoms": [
                    "Hạ huyết áp nặng",
                    "Buồn ngủ, lú lẫn",
                    "Nhịp tim chậm",
                    "Ngất",
                ],
                "antidote": "Không có antidote đặc hiệu.",
                "treatment": [
                    "Nằm đầu thấp, truyền dịch tĩnh mạch.",
                    "Vasopressor nếu hạ huyết áp không đáp ứng dịch.",
                    "Theo dõi ECG, huyết áp liên tục.",
                ],
                "monitoring": "Huyết áp, nhịp tim, ý thức trong ít nhất 24 giờ hoặc cho đến khi ổn định.",
            },
            "reversal_agents": {
                "available": False,
                "agents": [],
                "notes": "Không có thuốc giải độc; điều trị hỗ trợ là chính.",
            },
            "administration_instructions": {
                "oral": {
                    "with_food": "Có thể dùng cùng thức ăn để giảm buồn nôn.",
                    "timing": "Chia 2–4 lần/ngày; có thể ưu tiên liều cao hơn vào buổi tối do gây buồn ngủ.",
                    "notes": "Không ngừng đột ngột nếu dùng kéo dài; giảm liều từ từ.",
                },
                "iv": {
                    "reconstitution": "Pha trong NaCl 0.9%, dùng ngay sau pha.",
                    "infusion_rate": "Tiêm/truyền chậm trong 30 phút.",
                    "notes": "Theo dõi huyết áp sát trong và sau khi truyền.",
                },
            },
        },

        # ======================== CARDIOVASCULAR: ARBs & RELATED ==========================
        "Valsartan": {
            "contraindications": {
                "tuyệt_đối": [
                    "Dị ứng với valsartan hoặc ARB",
                    "Có thai (đặc biệt tam cá nguyệt 2–3)",
                    "Hẹp động mạch thận 2 bên hoặc hẹp động mạch thận thận độc nhất",
                ],
                "tương_đối": [
                    "Tăng kali máu",
                    "Suy thận (eGFR <30 mL/phút/1.73m²)",
                    "Hạ huyết áp thể tích (mất nước, dùng lợi tiểu liều cao)",
                ],
            },
            "pregnancy_lactation": {
                "fda_category": "D (X ở T2/T3)",
                "pregnancy_details": (
                    "CHỐNG CHỈ ĐỊNH trong thai kỳ, đặc biệt tam cá nguyệt 2–3, vì nguy cơ suy thận thai, vô niệu, thiểu ối, "
                    "dị tật sọ, tử vong thai. Ngừng valsartan ngay khi phát hiện có thai."
                ),
                "lactation": {
                    "safety": "Caution",
                    "details": "Chưa rõ dữ liệu ở người; bài tiết một phần vào sữa động vật.",
                    "recommendation": "Ưu tiên thuốc khác an toàn hơn nếu cho con bú sơ sinh/sinh non.",
                },
            },
            "hepatic_adjustment": {
                "mild": "Không cần chỉnh liều.",
                "moderate": "Thận trọng, cân nhắc liều khởi đầu thấp hơn.",
                "severe": "Tránh dùng hoặc giảm liều mạnh, theo dõi creatinine và kali sát.",
                "notes": "Valsartan thải trừ chủ yếu qua mật; suy gan có thể tăng nồng độ thuốc.",
            },
            "overdose_management": {
                "symptoms": [
                    "Hạ huyết áp nặng",
                    "Choáng, chóng mặt",
                    "Suy thận cấp (tăng creatinine)",
                ],
                "antidote": "Không có antidote đặc hiệu.",
                "treatment": [
                    "Đặt bệnh nhân ở tư thế đầu thấp, truyền dịch tĩnh mạch.",
                    "Vasopressor nếu không đáp ứng với dịch.",
                    "Theo dõi chức năng thận và điện giải.",
                ],
                "monitoring": "Huyết áp, nhịp tim, creatinine, kali trong 24–48 giờ.",
            },
            "reversal_agents": {
                "available": False,
                "agents": [],
                "notes": "Không có thuốc giải độc; hỗ trợ tuần hoàn và thận.",
            },
            "administration_instructions": {
                "oral": {
                    "with_food": "Có thể dùng cùng hoặc không cùng thức ăn.",
                    "timing": "Dùng 1–2 lần/ngày, cố định thời điểm.",
                    "notes": "Theo dõi huyết áp, creatinine và kali sau khi bắt đầu hoặc tăng liều.",
                }
            },
            "drug_interactions": {
                "major": [
                    {
                        "drug": "Kali, thuốc lợi tiểu giữ kali, bổ sung kali",
                        "mechanism": "Tăng giữ kali do ức chế hệ RAA",
                        "effect": "Tăng nguy cơ tăng kali máu nặng",
                        "management": "Tránh phối hợp hoặc theo dõi kali máu sát; điều chỉnh liều.",
                    }
                ],
                "moderate": [
                    {
                        "drug": "NSAID",
                        "mechanism": "Giảm tổng hợp prostaglandin thận",
                        "effect": "Giảm hiệu quả hạ huyết áp, tăng nguy cơ suy thận",
                        "management": "Hạn chế NSAID kéo dài; theo dõi creatinine.",
                    },
                    {
                        "drug": "Lithium",
                        "mechanism": "Giảm thải trừ lithium qua thận",
                        "effect": "Tăng nồng độ lithium, nguy cơ ngộ độc",
                        "management": "Nếu bắt buộc phối hợp, theo dõi nồng độ lithium sát, chỉnh liều.",
                    },
                ],
                "minor": [],
            },
        },

        "Olmesartan": {
            "contraindications": {
                "tuyệt_đối": [
                    "Dị ứng với olmesartan hoặc ARB",
                    "Có thai",
                ],
                "tương_đối": [
                    "Hẹp động mạch thận 2 bên",
                    "Suy thận nặng",
                    "Tiêu chảy mạn, giảm cân không rõ nguyên nhân (sprue-like enteropathy)",
                ],
            },
            "pregnancy_lactation": {
                "fda_category": "D (X ở T2/T3)",
                "pregnancy_details": "CHỐNG CHỈ ĐỊNH trong thai kỳ (đặc biệt T2/T3). Ngừng ngay khi phát hiện có thai.",
                "lactation": {
                    "safety": "Caution",
                    "details": "Thiếu dữ liệu ở người; bài tiết vào sữa động vật.",
                    "recommendation": "Ưu tiên thuốc khác an toàn hơn trong cho con bú.",
                },
            },
            "hepatic_adjustment": {
                "mild": "Không cần chỉnh liều.",
                "moderate": "Thận trọng với liều khởi đầu thấp.",
                "severe": "Tránh dùng hoặc giám sát chặt.",
                "notes": "Chuyển hóa qua gan ít nhưng thải trừ qua mật có thể bị ảnh hưởng.",
            },
            "overdose_management": {
                "symptoms": ["Hạ huyết áp", "Choáng", "Suy thận cấp"],
                "antidote": "Không có antidote đặc hiệu.",
                "treatment": [
                    "Truyền dịch tĩnh mạch.",
                    "Vasopressor nếu cần.",
                    "Theo dõi creatinine, điện giải.",
                ],
                "monitoring": "Huyết áp, nhịp tim, chức năng thận trong 24–48 giờ.",
            },
            "reversal_agents": {"available": False, "agents": [], "notes": "Điều trị hỗ trợ."},
            "administration_instructions": {
                "oral": {
                    "with_food": "Không phụ thuộc thức ăn.",
                    "timing": "1 lần/ngày, có thể tăng liều sau 2 tuần.",
                    "notes": "Theo dõi tiêu chảy mạn, sụt cân (sprue-like enteropathy).",
                }
            },
            "drug_interactions": {
                "major": [
                    {
                        "drug": "Kali, lợi tiểu giữ kali",
                        "mechanism": "Tăng giữ kali",
                        "effect": "Tăng kali máu",
                        "management": "Theo dõi điện giải, tránh phối hợp không cần thiết.",
                    }
                ],
                "moderate": [
                    {
                        "drug": "NSAID",
                        "mechanism": "Giảm tưới máu thận",
                        "effect": "Suy thận cấp, giảm hiệu quả hạ huyết áp",
                        "management": "Hạn chế NSAID, theo dõi creatinine.",
                    }
                ],
                "minor": [],
            },
        },

        "Candesartan": {
            "contraindications": {
                "tuyệt_đối": [
                    "Dị ứng candesartan hoặc ARB",
                    "Có thai",
                ],
                "tương_đối": [
                    "Hẹp động mạch thận 2 bên",
                    "Tăng kali máu",
                    "Suy thận nặng",
                ],
            },
            "pregnancy_lactation": {
                "fda_category": "D (X ở T2/T3)",
                "pregnancy_details": "CHỐNG CHỈ ĐỊNH trong thai kỳ; đặc biệt T2/T3.",
                "lactation": {
                    "safety": "Caution",
                    "details": "Thiếu dữ liệu; cân nhắc ngừng cho bú hoặc đổi thuốc.",
                    "recommendation": "Ưu tiên thuốc an toàn hơn cho mẹ cho con bú.",
                },
            },
            "hepatic_adjustment": {
                "mild": "Không cần chỉnh liều.",
                "moderate": "Thận trọng, khởi đầu liều thấp.",
                "severe": "Tránh dùng hoặc giám sát chặt.",
                "notes": "Một phần thải trừ qua gan; suy gan có thể tăng nồng độ thuốc.",
            },
            "overdose_management": {
                "symptoms": ["Hạ huyết áp", "Choáng", "Suy thận"],
                "antidote": "Không có antidote đặc hiệu.",
                "treatment": [
                    "Truyền dịch, nâng huyết áp.",
                    "Vasopressor nếu cần.",
                    "Theo dõi chức năng thận, điện giải.",
                ],
                "monitoring": "Huyết áp, nhịp tim, creatinine, kali.",
            },
            "reversal_agents": {"available": False, "agents": [], "notes": "Hỗ trợ triệu chứng."},
            "administration_instructions": {
                "oral": {
                    "with_food": "Không phụ thuộc thức ăn.",
                    "timing": "1 lần/ngày; có thể chia 2 lần nếu cần.",
                    "notes": "Theo dõi creatinine và kali sau khi bắt đầu hoặc tăng liều.",
                }
            },
            "drug_interactions": {
                "major": [
                    {
                        "drug": "Lợi tiểu giữ kali/bổ sung kali",
                        "mechanism": "Tăng giữ kali",
                        "effect": "Tăng kali máu",
                        "management": "Theo dõi điện giải, điều chỉnh hoặc tránh phối hợp.",
                    }
                ],
                "moderate": [
                    {
                        "drug": "NSAID",
                        "mechanism": "Giảm tưới máu thận",
                        "effect": "Suy thận cấp, giảm hiệu quả hạ huyết áp",
                        "management": "Hạn chế NSAID, theo dõi creatinine.",
                    },
                    {
                        "drug": "Lithium",
                        "mechanism": "Giảm thải trừ lithium",
                        "effect": "Tăng độc tính lithium",
                        "management": "Theo dõi lithium máu, điều chỉnh liều.",
                    },
                ],
                "minor": [],
            },
        },

        "Irbesartan": {
            "contraindications": {
                "tuyệt_đối": [
                    "Dị ứng irbesartan hoặc ARB",
                    "Có thai",
                ],
                "tương_đối": [
                    "Hẹp động mạch thận 2 bên",
                    "Tăng kali máu",
                    "Suy thận nặng",
                ],
            },
            "pregnancy_lactation": {
                "fda_category": "D (X ở T2/T3)",
                "pregnancy_details": "CHỐNG CHỈ ĐỊNH trong thai kỳ; ngừng ngay khi phát hiện có thai.",
                "lactation": {
                    "safety": "Caution",
                    "details": "Thiếu dữ liệu; bài tiết vào sữa động vật.",
                    "recommendation": "Cân nhắc thuốc an toàn hơn nếu cho con bú.",
                },
            },
            "hepatic_adjustment": {
                "mild": "Không cần chỉnh liều.",
                "moderate": "Thận trọng.",
                "severe": "Thiếu dữ liệu; tránh dùng nếu có thể.",
                "notes": "Irbesartan chuyển hóa qua gan (CYP2C9).",
            },
            "overdose_management": {
                "symptoms": ["Hạ huyết áp", "Choáng", "Suy thận"],
                "antidote": "Không có antidote đặc hiệu.",
                "treatment": ["Truyền dịch", "Vasopressor nếu cần", "Theo dõi chức năng thận, điện giải."],
                "monitoring": "Huyết áp, creatinine, kali.",
            },
            "reversal_agents": {"available": False, "agents": [], "notes": "Điều trị hỗ trợ."},
            "administration_instructions": {
                "oral": {
                    "with_food": "Không phụ thuộc thức ăn.",
                    "timing": "1 lần/ngày.",
                    "notes": "Theo dõi huyết áp, chức năng thận và kali sau khi bắt đầu hoặc tăng liều.",
                }
            },
            "drug_interactions": {
                "major": [
                    {
                        "drug": "Lợi tiểu giữ kali/bổ sung kali",
                        "mechanism": "Tăng giữ kali",
                        "effect": "Tăng kali máu",
                        "management": "Theo dõi điện giải, tránh liều cao phối hợp.",
                    }
                ],
                "moderate": [
                    {
                        "drug": "NSAID",
                        "mechanism": "Giảm tưới máu thận",
                        "effect": "Suy thận cấp, giảm hiệu quả hạ huyết áp",
                        "management": "Hạn chế NSAID, theo dõi creatinine.",
                    }
                ],
                "minor": [],
            },
        },

        # ======================== CARDIOVASCULAR: STATINS ==========================
        "Simvastatin": {
            "contraindications": {
                "tuyệt_đối": [
                    "Bệnh gan hoạt động (active liver disease) - tăng men gan kéo dài, viêm gan",
                    "Có thai (pregnancy) - FDA category X, gây dị tật thai nhi",
                    "Cho con bú (lactation) - bài tiết vào sữa mẹ",
                    "Tiêu cơ vân đang hoạt động (active myopathy/rhabdomyolysis)",
                    "Dị ứng với simvastatin hoặc bất kỳ thành phần nào",
                    "Dùng cùng cyclosporine, itraconazole, ketoconazole (tăng nguy cơ tiêu cơ vân nghiêm trọng)",
                    "Dùng grapefruit juice",
                ],
                "tương_đối": [
                    "Suy thận - thận trọng, giảm liều nếu cần",
                    "Suy gan - thận trọng, theo dõi men gan thường xuyên",
                    "Uống rượu nhiều - tăng nguy cơ viêm gan",
                    "Người cao tuổi - tăng nguy cơ đau cơ, tiêu cơ vân",
                    "Đái tháo đường - statins có thể tăng đường huyết nhẹ",
                    "Bệnh tuyến giáp - tăng nguy cơ đau cơ",
                    "Dùng cùng thuốc ức chế CYP3A4 - giảm liều simvastatin",
                    "Liều cao (>40mg/ngày) - tăng nguy cơ tiêu cơ vân",
                ],
            },
            "pregnancy_lactation": {
                "fda_category": "X",
                "pregnancy_details": (
                    "CHỐNG CHỈ ĐỊNH trong thai kỳ. Simvastatin gây dị tật thai nhi, đặc biệt trong tam cá nguyệt đầu tiên. "
                    "Statins ức chế tổng hợp cholesterol, cần thiết cho sự phát triển của thai nhi. Có thể gây dị tật bẩm sinh, chậm phát triển. "
                    "Phụ nữ trong độ tuổi sinh đẻ phải dùng biện pháp tránh thai hiệu quả. Phải ngừng simvastatin ít nhất 1-2 tháng trước khi có thai. "
                    "Nếu có thai khi đang dùng, ngừng ngay lập tức."
                ),
                "lactation": {
                    "safety": "Incompatible",
                    "details": "Simvastatin bài tiết vào sữa mẹ. Có thể gây tác dụng phụ trên trẻ bú mẹ. Chưa có dữ liệu đầy đủ về an toàn. Statins có thể ảnh hưởng đến sự phát triển của trẻ.",
                    "recommendation": "CHỐNG CHỈ ĐỊNH khi cho con bú. Ngừng simvastatin hoặc ngừng cho con bú. Cân nhắc thuốc thay thế nếu cần.",
                },
            },
            "hepatic_adjustment": {
                "mild": "Không đổi liều. Theo dõi men gan thường xuyên.",
                "moderate": "Thận trọng. Giảm liều hoặc dùng liều thấp hơn. Theo dõi men gan mỗi 3-6 tháng. Ngừng nếu ALT >3 lần ULN.",
                "severe": "CHỐNG CHỈ ĐỊNH. Không dùng ở bệnh nhân suy gan nặng hoặc bệnh gan hoạt động.",
                "notes": "Simvastatin chuyển hóa qua gan (CYP3A4) - extensive first-pass metabolism. Suy gan có thể làm tăng nồng độ simvastatin và tăng nguy cơ độc tính. Kiểm tra men gan trước điều trị. Ngừng nếu ALT >3 lần ULN hoặc có dấu hiệu viêm gan.",
            },
            "overdose_management": {
                "symptoms": [
                    "Tiêu cơ vân (rhabdomyolysis) - triệu chứng chính và nguy hiểm nhất",
                    "Đau cơ dữ dội, yếu cơ",
                    "Nước tiểu sẫm màu (myoglobinuria)",
                    "Suy thận cấp (do myoglobin)",
                    "Tăng men gan (ALT, AST)",
                    "Tăng CK (creatine kinase)",
                    "Mệt mỏi, buồn nôn",
                    "Rối loạn tiêu hóa",
                ],
                "antidote": "Không có antidote đặc hiệu. Điều trị hỗ trợ: ngừng simvastatin, truyền dịch tích cực để phòng suy thận, lọc máu nếu cần",
                "treatment": [
                    "Ngừng simvastatin ngay lập tức",
                    "Đo CK, men gan, chức năng thận ngay",
                    "Nếu có tiêu cơ vân:",
                    "  - Truyền dịch tích cực (normal saline 1-2L/giờ) để duy trì lượng nước tiểu >100-200ml/giờ",
                    "  - Kiềm hóa nước tiểu (sodium bicarbonate) để giảm độc tính myoglobin trên thận",
                    "  - Theo dõi chức năng thận (creatinine, BUN, lượng nước tiểu)",
                    "  - Hemodialysis nếu suy thận cấp, tăng kali máu, hoặc quá tải dịch",
                    "  - Theo dõi điện giải (natri, kali, canxi, phosphate)",
                    "Điều trị hỗ trợ:",
                    "  - Điều chỉnh rối loạn điện giải",
                    "  - Hỗ trợ hô hấp và tuần hoàn nếu cần",
                    "  - Giảm đau (opioids) nếu đau cơ nặng",
                    "Theo dõi CK, men gan, chức năng thận hàng ngày cho đến khi ổn định",
                    "Theo dõi ít nhất 24-48 giờ do half-life 2-3 giờ (nhưng tác dụng kéo dài)",
                ],
                "monitoring": "CK, ALT, AST, creatinine, BUN, kali, canxi, phosphate, lượng nước tiểu, ECG (nếu có rối loạn điện giải), dấu hiệu suy thận",
            },
            "reversal_agents": {
                "available": False,
                "agents": [],
                "notes": "Không có thuốc giải độc đặc hiệu. Điều trị hỗ trợ là chính.",
            },
            "administration_instructions": {
                "oral": {
                    "with_food": "Có thể uống với hoặc không có thức ăn. Không ảnh hưởng đáng kể đến hấp thu.",
                    "timing": "Uống 1 lần/ngày vào BUỔI TỐI (cholesterol được tổng hợp nhiều vào ban đêm). Uống cùng một giờ mỗi ngày để nhớ. TRÁNH grapefruit juice hoàn toàn.",
                },
            },
        },

        # ======================== CARDIOVASCULAR: PCSK9 INHIBITORS ==================
        "Alirocumab": {
            "contraindications": {
                "tuyệt_đối": [
                    "Dị ứng với alirocumab hoặc bất kỳ thành phần nào",
                    "Dị ứng với protein tái tổ hợp",
                ],
                "tương_đối": [
                    "Suy gan nặng - chưa có dữ liệu đầy đủ",
                    "Suy thận nặng - không cần chỉnh liều nhưng thận trọng",
                ],
            },
            "hepatic_adjustment": {
                "mild": "Không cần chỉnh liều.",
                "moderate": "Thận trọng, chưa có dữ liệu đầy đủ.",
                "severe": "Thiếu dữ liệu; cân nhắc thuốc khác nếu có thể.",
                "notes": "Alirocumab là monoclonal antibody, không chuyển hóa qua gan nhưng thải trừ qua hệ thống reticuloendothelial.",
            },
            "reversal_agents": {
                "available": False,
                "agents": [],
                "notes": "Không có thuốc giải độc đặc hiệu. Half-life rất dài (17-20 ngày), tác dụng sẽ giảm dần theo thời gian.",
            },
        },

        "Evolocumab": {
            "contraindications": {
                "tuyệt_đối": [
                    "Dị ứng với evolocumab hoặc bất kỳ thành phần nào",
                    "Dị ứng với protein tái tổ hợp",
                ],
                "tương_đối": [
                    "Suy gan nặng - chưa có dữ liệu đầy đủ",
                    "Suy thận nặng - không cần chỉnh liều nhưng thận trọng",
                ],
            },
            "hepatic_adjustment": {
                "mild": "Không cần chỉnh liều.",
                "moderate": "Thận trọng, chưa có dữ liệu đầy đủ.",
                "severe": "Thiếu dữ liệu; cân nhắc thuốc khác nếu có thể.",
                "notes": "Evolocumab là monoclonal antibody, không chuyển hóa qua gan nhưng thải trừ qua hệ thống reticuloendothelial.",
            },
            "reversal_agents": {
                "available": False,
                "agents": [],
                "notes": "Không có thuốc giải độc đặc hiệu. Half-life rất dài (11-17 ngày), tác dụng sẽ giảm dần theo thời gian.",
            },
        },

        "Inclisiran": {
            "contraindications": {
                "tuyệt_đối": [
                    "Dị ứng với inclisiran hoặc bất kỳ thành phần nào",
                ],
                "tương_đối": [
                    "Suy gan nặng - chưa có dữ liệu đầy đủ",
                    "Suy thận nặng - không cần chỉnh liều nhưng thận trọng",
                ],
            },
            "hepatic_adjustment": {
                "mild": "Không cần chỉnh liều.",
                "moderate": "Thận trọng, chưa có dữ liệu đầy đủ.",
                "severe": "Thiếu dữ liệu; cân nhắc thuốc khác nếu có thể.",
                "notes": "Inclisiran là siRNA, không chuyển hóa qua gan nhưng thải trừ qua hệ thống nội bào.",
            },
            "reversal_agents": {
                "available": False,
                "agents": [],
                "notes": "Không có thuốc giải độc đặc hiệu. Tác dụng kéo dài 6 tháng sau liều thứ 2.",
            },
        },

        # ======================== CARDIOVASCULAR: DIURETICS ========================
        "Bumetanide": {
            "contraindications": {
                "tuyệt_đối": [
                    "Vô niệu",
                    "Mất nước nặng",
                    "Hạ kali máu nặng",
                    "Dị ứng sulfonamide",
                ],
                "tương_đối": [
                    "Suy thận nặng - có thể cần liều cao hơn nhưng thận trọng",
                    "Suy gan nặng - thận trọng",
                    "Đang dùng digoxin - tăng nguy cơ ngộ độc digoxin",
                ],
            },
            "drug_interactions": {
                "major": [
                    {
                        "drug": "Digoxin",
                        "mechanism": "Bumetanide gây hạ kali máu, tăng nguy cơ ngộ độc digoxin",
                        "effect": "Tăng nguy cơ rối loạn nhịp tim do digoxin",
                        "management": "Theo dõi kali máu sát, bù kali nếu cần. Theo dõi nồng độ digoxin.",
                    },
                    {
                        "drug": "Aminoglycosides",
                        "mechanism": "Tăng độc tính thính giác",
                        "effect": "Tăng nguy cơ điếc",
                        "management": "Tránh dùng đồng thời nếu có thể. Theo dõi thính giác nếu bắt buộc.",
                    },
                ],
                "moderate": [
                    {
                        "drug": "NSAID",
                        "mechanism": "Giảm tổng hợp prostaglandin thận",
                        "effect": "Giảm hiệu quả bumetanide",
                        "management": "Theo dõi đáp ứng, có thể cần tăng liều bumetanide.",
                    },
                    {
                        "drug": "Lithium",
                        "mechanism": "Giảm thải trừ lithium",
                        "effect": "Tăng nồng độ lithium, nguy cơ độc tính",
                        "management": "Theo dõi nồng độ lithium sát, điều chỉnh liều.",
                    },
                ],
                "minor": [],
            },
            "pregnancy_lactation": {
                "fda_category": "C",
                "pregnancy_details": "Sử dụng nếu lợi ích vượt trội nguy cơ. Có thể gây hạ kali máu và mất nước ở mẹ.",
                "lactation": {
                    "safety": "Compatible",
                    "details": "Bài tiết vào sữa mẹ với lượng nhỏ. Thường an toàn cho trẻ bú mẹ.",
                    "recommendation": "Có thể dùng khi cho con bú. Theo dõi trẻ về các triệu chứng bất thường (hiếm).",
                },
            },
            "hepatic_adjustment": {
                "mild": "Không cần chỉnh liều.",
                "moderate": "Thận trọng, theo dõi chức năng gan.",
                "severe": "Thận trọng, có thể cần giảm liều.",
                "notes": "Bumetanide chuyển hóa một phần qua gan, thải trừ qua cả thận và gan.",
            },
            "overdose_management": {
                "symptoms": [
                    "Mất nước nặng",
                    "Hạ kali máu nặng",
                    "Hạ natri máu",
                    "Suy thận cấp",
                    "Điếc (IV liều cao)",
                    "Rối loạn điện giải",
                ],
                "antidote": "Không có antidote đặc hiệu.",
                "treatment": [
                    "Ngừng bumetanide ngay",
                    "Đo điện giải (K, Na, Cl) ngay",
                    "Bù dịch (normal saline) nếu mất nước",
                    "Bù kali nếu hạ kali máu",
                    "Theo dõi chức năng thận",
                    "Theo dõi cân bằng dịch vào-ra",
                ],
                "monitoring": "Điện giải (K, Na, Cl), creatinine, BUN, cân bằng dịch, thính giác (nếu IV liều cao).",
            },
            "reversal_agents": {
                "available": False,
                "agents": [],
                "notes": "Không có thuốc giải độc đặc hiệu. Điều trị hỗ trợ là chính.",
            },
            "administration_instructions": {
                "oral": {
                    "with_food": "Có thể uống với hoặc không có thức ăn.",
                    "timing": "Uống 1-2 lần/ngày, thường vào buổi sáng và/hoặc buổi trưa.",
                    "notes": "Theo dõi điện giải sát, đặc biệt kali. Bù kali nếu cần.",
                },
                "iv": {
                    "reconstitution": "Pha trong NaCl 0.9% hoặc D5W.",
                    "infusion_rate": "Tiêm IV bolus hoặc truyền liên tục 0.1-0.2mg/giờ.",
                    "notes": "Theo dõi điện giải sát. Tránh liều cao ở bệnh nhân suy thận (nguy cơ điếc).",
                },
            },
        },

        "Torsemide": {
            "contraindications": {
                "tuyệt_đối": [
                    "Vô niệu",
                    "Mất nước nặng",
                    "Hạ kali máu nặng",
                    "Dị ứng sulfonamide",
                ],
                "tương_đối": [
                    "Suy thận nặng - có thể cần liều cao hơn nhưng thận trọng",
                    "Suy gan nặng - thận trọng",
                    "Đang dùng digoxin - tăng nguy cơ ngộ độc digoxin",
                ],
            },
            "drug_interactions": {
                "major": [
                    {
                        "drug": "Digoxin",
                        "mechanism": "Torsemide gây hạ kali máu, tăng nguy cơ ngộ độc digoxin",
                        "effect": "Tăng nguy cơ rối loạn nhịp tim do digoxin",
                        "management": "Theo dõi kali máu sát, bù kali nếu cần. Theo dõi nồng độ digoxin.",
                    },
                    {
                        "drug": "Aminoglycosides",
                        "mechanism": "Tăng độc tính thính giác",
                        "effect": "Tăng nguy cơ điếc",
                        "management": "Tránh dùng đồng thời nếu có thể. Theo dõi thính giác nếu bắt buộc.",
                    },
                ],
                "moderate": [
                    {
                        "drug": "NSAID",
                        "mechanism": "Giảm tổng hợp prostaglandin thận",
                        "effect": "Giảm hiệu quả torsemide",
                        "management": "Theo dõi đáp ứng, có thể cần tăng liều torsemide.",
                    },
                    {
                        "drug": "Lithium",
                        "mechanism": "Giảm thải trừ lithium",
                        "effect": "Tăng nồng độ lithium, nguy cơ độc tính",
                        "management": "Theo dõi nồng độ lithium sát, điều chỉnh liều.",
                    },
                ],
                "minor": [],
            },
            "pregnancy_lactation": {
                "fda_category": "B",
                "pregnancy_details": "An toàn hơn bumetanide trong thai kỳ. Sử dụng nếu lợi ích vượt trội nguy cơ.",
                "lactation": {
                    "safety": "Compatible",
                    "details": "Bài tiết vào sữa mẹ với lượng nhỏ. Thường an toàn cho trẻ bú mẹ.",
                    "recommendation": "Có thể dùng khi cho con bú. Theo dõi trẻ về các triệu chứng bất thường (hiếm).",
                },
            },
            "hepatic_adjustment": {
                "mild": "Không cần chỉnh liều.",
                "moderate": "Thận trọng, theo dõi chức năng gan.",
                "severe": "Thận trọng, có thể cần giảm liều.",
                "notes": "Torsemide chuyển hóa một phần qua gan, thải trừ qua cả thận và gan.",
            },
            "overdose_management": {
                "symptoms": [
                    "Mất nước nặng",
                    "Hạ kali máu nặng",
                    "Hạ natri máu",
                    "Suy thận cấp",
                    "Điếc (IV liều cao)",
                    "Rối loạn điện giải",
                ],
                "antidote": "Không có antidote đặc hiệu.",
                "treatment": [
                    "Ngừng torsemide ngay",
                    "Đo điện giải (K, Na, Cl) ngay",
                    "Bù dịch (normal saline) nếu mất nước",
                    "Bù kali nếu hạ kali máu",
                    "Theo dõi chức năng thận",
                    "Theo dõi cân bằng dịch vào-ra",
                ],
                "monitoring": "Điện giải (K, Na, Cl), creatinine, BUN, cân bằng dịch, thính giác (nếu IV liều cao).",
            },
            "reversal_agents": {
                "available": False,
                "agents": [],
                "notes": "Không có thuốc giải độc đặc hiệu. Điều trị hỗ trợ là chính.",
            },
            "administration_instructions": {
                "oral": {
                    "with_food": "Có thể uống với hoặc không có thức ăn.",
                    "timing": "Uống 1 lần/ngày, thường vào buổi sáng (thời gian bán hủy dài hơn furosemide).",
                    "notes": "Theo dõi điện giải sát, đặc biệt kali. Bù kali nếu cần.",
                },
                "iv": {
                    "reconstitution": "Pha trong NaCl 0.9% hoặc D5W.",
                    "infusion_rate": "Tiêm IV bolus hoặc truyền liên tục 0.2-0.4mg/giờ.",
                    "notes": "Theo dõi điện giải sát. Tránh liều cao ở bệnh nhân suy thận (nguy cơ điếc).",
                },
            },
        },

        # ======================== CARDIOVASCULAR: TRIGLYCERIDE LOWERING ============
        "Icosapent ethyl": {
            "overdose_management": {
                "symptoms": ["Rối loạn tiêu hóa", "Chảy máu (nếu dùng với thuốc chống đông)"],
                "antidote": "Không có antidote đặc hiệu.",
                "treatment": ["Ngừng icosapent ethyl", "Điều trị hỗ trợ triệu chứng"],
                "monitoring": "Dấu hiệu chảy máu, rối loạn tiêu hóa.",
            },
            "reversal_agents": {"available": False, "agents": [], "notes": "Không có thuốc giải độc đặc hiệu."},
            "administration_instructions": {
                "oral": {
                    "with_food": "Uống với thức ăn để tăng hấp thu và giảm tác dụng phụ tiêu hóa.",
                    "timing": "Uống 2 lần/ngày, tổng 4g/ngày.",
                    "notes": "Không dùng quá 4g/ngày. Theo dõi dấu hiệu chảy máu nếu dùng với thuốc chống đông.",
                },
            },
        },

        "Omega-3 acid ethyl esters": {
            "overdose_management": {
                "symptoms": ["Rối loạn tiêu hóa", "Chảy máu (nếu dùng với thuốc chống đông)"],
                "antidote": "Không có antidote đặc hiệu.",
                "treatment": ["Ngừng omega-3", "Điều trị hỗ trợ triệu chứng"],
                "monitoring": "Dấu hiệu chảy máu, rối loạn tiêu hóa.",
            },
            "reversal_agents": {"available": False, "agents": [], "notes": "Không có thuốc giải độc đặc hiệu."},
            "administration_instructions": {
                "oral": {
                    "with_food": "Uống với thức ăn để tăng hấp thu và giảm tác dụng phụ tiêu hóa.",
                    "timing": "Uống 1-2 lần/ngày tùy liều.",
                    "notes": "Theo dõi dấu hiệu chảy máu nếu dùng với thuốc chống đông.",
                },
            },
        },

        "Pemafibrate": {
            "overdose_management": {
                "symptoms": ["Tăng men gan", "Đau cơ", "Suy thận cấp"],
                "antidote": "Không có antidote đặc hiệu.",
                "treatment": ["Ngừng pemafibrate", "Điều trị hỗ trợ", "Theo dõi chức năng gan, thận"],
                "monitoring": "Chức năng gan, thận, CK, dấu hiệu sỏi mật.",
            },
            "reversal_agents": {"available": False, "agents": [], "notes": "Không có thuốc giải độc đặc hiệu."},
            "administration_instructions": {
                "oral": {
                    "with_food": "Uống với thức ăn để tăng hấp thu.",
                    "timing": "Uống 2 lần/ngày, tổng 0.4-0.8mg/ngày.",
                    "notes": "CHỐNG CHỈ ĐỊNH ở suy thận nặng (eGFR <30). Theo dõi CK nếu có đau cơ.",
                },
            },
        },

    # ======================== BATCH 2: CARDIOVASCULAR DRUGS ========================
        "Atenolol": {
            "contraindications_detail": {
                "tuyệt_đối": [
                    "Dị ứng với atenolol hoặc beta-blocker",
                    "Suy tim nặng không được điều trị",
                    "Block nhĩ thất độ 2-3 không có máy tạo nhịp",
                    "Sick sinus syndrome không có máy tạo nhịp",
                    "Nhịp tim chậm nặng (<50 bpm)",
                    "Sốc tim",
                    "Hen suyễn nặng hoặc COPD nặng",
                ],
                "tương_đối": [
                    "Suy tim vừa - cần điều trị trước",
                    "Nhịp tim chậm vừa (50-60 bpm)",
                    "Block nhĩ thất độ 1",
                    "Bệnh mạch máu ngoại biên",
                    "Đái tháo đường - che dấu triệu chứng hạ đường huyết",
                    "Cường giáp - không dùng đơn độc",
                    "Suy thận nặng (CrCl <30) - giảm liều",
                    "Có thai - thận trọng",
                    "Đang cho con bú - thận trọng",
                ],
            },
        },

        "Bisoprolol": {
            "contraindications_detail": {
                "tuyệt_đối": [
                    "Dị ứng với bisoprolol hoặc beta-blocker",
                    "Suy tim nặng không được điều trị",
                    "Block nhĩ thất độ 2-3 không có máy tạo nhịp",
                    "Sick sinus syndrome không có máy tạo nhịp",
                    "Nhịp tim chậm nặng (<50 bpm)",
                    "Sốc tim",
                    "Hen suyễn nặng hoặc COPD nặng",
                ],
                "tương_đối": [
                    "Suy tim vừa - cần điều trị trước",
                    "Nhịp tim chậm vừa (50-60 bpm)",
                    "Block nhĩ thất độ 1",
                    "Bệnh mạch máu ngoại biên",
                    "Đái tháo đường - che dấu triệu chứng hạ đường huyết",
                    "Cường giáp - không dùng đơn độc",
                    "Suy thận nặng (CrCl <30) - giảm liều",
                    "Suy gan nặng - giảm liều",
                    "Có thai - thận trọng",
                    "Đang cho con bú - thận trọng",
                ],
            },
        },

        "Carvedilol": {
            "contraindications_detail": {
                "tuyệt_đối": [
                    "Dị ứng với carvedilol hoặc beta-blocker",
                    "Suy tim nặng không được điều trị (NYHA IV)",
                    "Block nhĩ thất độ 2-3 không có máy tạo nhịp",
                    "Sick sinus syndrome không có máy tạo nhịp",
                    "Nhịp tim chậm nặng (<50 bpm)",
                    "Sốc tim",
                    "Hen suyễn nặng hoặc COPD nặng",
                    "Suy gan nặng",
                ],
                "tương_đối": [
                    "Suy tim vừa - bắt đầu với liều thấp",
                    "Nhịp tim chậm vừa (50-60 bpm)",
                    "Block nhĩ thất độ 1",
                    "Hạ huyết áp tư thế",
                    "Bệnh mạch máu ngoại biên",
                    "Đái tháo đường - che dấu triệu chứng hạ đường huyết",
                    "Suy thận nặng (CrCl <30) - giảm liều",
                    "Suy gan vừa - giảm liều",
                    "Có thai - thận trọng",
                    "Đang cho con bú - thận trọng",
                ],
            },
        },

        "Nifedipine": {
            "contraindications_detail": {
                "tuyệt_đối": [
                    "Dị ứng với nifedipine hoặc dihydropyridine",
                    "Sốc tim",
                    "Hẹp van động mạch chủ nặng",
                    "Suy tim nặng không được điều trị",
                ],
                "tương_đối": [
                    "Suy tim vừa - thận trọng",
                    "Hạ huyết áp",
                    "Suy gan nặng - giảm liều",
                    "Suy thận nặng - thận trọng",
                    "Có thai - thận trọng, có thể gây hạ huyết áp",
                    "Đang cho con bú - thận trọng",
                    "Người cao tuổi - tăng nhạy cảm",
                ],
            },
        },

        "Diltiazem": {
            "contraindications_detail": {
                "tuyệt_đối": [
                    "Dị ứng với diltiazem",
                    "Sick sinus syndrome không có máy tạo nhịp",
                    "Block nhĩ thất độ 2-3 không có máy tạo nhịp",
                    "Suy tim nặng (EF <30%)",
                    "Sốc tim",
                    "Hạ huyết áp nặng (SBP <90 mmHg)",
                ],
                "tương_đối": [
                    "Suy tim vừa - thận trọng",
                    "Nhịp tim chậm",
                    "Block nhĩ thất độ 1",
                    "Suy gan nặng - giảm liều",
                    "Suy thận nặng - thận trọng",
                    "Có thai - thận trọng",
                    "Đang cho con bú - thận trọng",
                ],
            },
        },

        "Verapamil": {
            "contraindications_detail": {
                "tuyệt_đối": [
                    "Dị ứng với verapamil",
                    "Sick sinus syndrome không có máy tạo nhịp",
                    "Block nhĩ thất độ 2-3 không có máy tạo nhịp",
                    "Suy tim nặng (EF <30%)",
                    "Sốc tim",
                    "Hạ huyết áp nặng (SBP <90 mmHg)",
                ],
                "tương_đối": [
                    "Suy tim vừa - thận trọng",
                    "Nhịp tim chậm",
                    "Block nhĩ thất độ 1",
                    "Suy gan nặng - giảm liều đáng kể",
                    "Suy thận nặng - thận trọng",
                    "Có thai - thận trọng",
                    "Đang cho con bú - thận trọng",
                ],
            },
        },

        "Hydrochlorothiazide": {
            "contraindications_detail": {
                "tuyệt_đối": [
                    "Dị ứng với hydrochlorothiazide hoặc sulfonamide",
                    "Vô niệu",
                    "Suy thận nặng (CrCl <30)",
                    "Hạ kali máu nặng không điều chỉnh được",
                    "Tăng calci máu nặng",
                ],
                "tương_đối": [
                    "Suy thận vừa (CrCl 30-60) - thận trọng",
                    "Hạ kali máu - cần bổ sung kali",
                    "Tăng calci máu vừa",
                    "Gout - có thể làm tăng acid uric",
                    "Đái tháo đường - có thể làm tăng đường huyết",
                    "Suy gan - nguy cơ hôn mê gan",
                    "Có thai - thận trọng, có thể gây giảm thể tích",
                    "Đang cho con bú - thận trọng",
                ],
            },
        },

        "Spironolactone": {
            "contraindications_detail": {
                "tuyệt_đối": [
                    "Dị ứng với spironolactone",
                    "Suy thận nặng (CrCl <30)",
                    "Tăng kali máu",
                    "Vô niệu",
                    "Bệnh Addison",
                ],
                "tương_đối": [
                    "Suy thận vừa (CrCl 30-60) - thận trọng, theo dõi kali",
                    "Đang dùng kali bổ sung hoặc thuốc giữ kali",
                    "Đái tháo đường - tăng nguy cơ tăng kali máu",
                    "Suy gan - nguy cơ hôn mê gan",
                    "Có thai - thận trọng, có thể gây dị tật",
                    "Đang cho con bú - thận trọng",
                    "Người cao tuổi - tăng nguy cơ tăng kali máu",
                ],
            },
        },

        "Captopril": {
            "contraindications_detail": {
                "tuyệt_đối": [
                    "Dị ứng với captopril hoặc ACE inhibitor",
                    "Tiền sử phù mạch do ACE inhibitor",
                    "Có thai (2-3 tháng giữa và cuối)",
                    "Hẹp động mạch thận hai bên",
                    "Hẹp động mạch thận một bên với thận độc nhất",
                ],
                "tương_đối": [
                    "Suy thận nặng (CrCl <30) - giảm liều",
                    "Suy gan nặng - thận trọng",
                    "Hạ huyết áp",
                    "Tăng kali máu",
                    "Đang dùng thuốc giữ kali hoặc kali bổ sung",
                    "Có thai (3 tháng đầu) - thận trọng",
                    "Đang cho con bú - thận trọng",
                    "Người cao tuổi - tăng nhạy cảm",
                ],
            },
        },

}
