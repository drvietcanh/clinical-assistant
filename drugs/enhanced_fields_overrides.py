"""
Enhanced fields overrides for specific drugs.

Mục tiêu:
- Bổ sung hoặc chuẩn hóa đủ 14 fields (6 cơ bản + 8 tùy chọn) cho một số thuốc
  còn thiếu field tùy chọn trong database gốc.

Lưu ý:
- Chỉ thêm/cập nhật các field còn thiếu; không thay đổi các field đã dùng ổn định.
- Đặc biệt chuẩn hóa 'contraindications' về dạng dict thay vì list.
"""

from typing import Any, Dict


EXTRA_ENHANCED_FIELDS: Dict[str, Dict[str, Any]] = {
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
    # ======================== GASTROINTESTINAL: H2 ANTAGONISTS ==================
    "Famotidine": {
        "contraindications": {
            "tuyệt_đối": [
                "Dị ứng với famotidine hoặc bất kỳ thành phần nào",
            ],
            "tương_đối": [
                "Suy thận nặng - cần giảm liều 50%",
                "Suy gan nặng - thận trọng",
            ],
        },
        "drug_interactions": {
            "major": [],
            "moderate": [
                {
                    "drug": "Ketoconazole, Itraconazole",
                    "mechanism": "Famotidine giảm acid dạ dày, giảm hấp thu azole antifungals",
                    "effect": "Giảm hấp thu azole, giảm hiệu quả",
                    "management": "Dùng cách nhau ít nhất 2 giờ. Hoặc dùng PPI thay thế.",
                },
            ],
            "minor": [
                {
                    "drug": "Warfarin",
                    "mechanism": "Tương tác tối thiểu với warfarin",
                    "effect": "Tăng nhẹ nguy cơ xuất huyết",
                    "management": "Theo dõi INR khi dùng famotidine.",
                },
            ],
        },
        "pregnancy_lactation": {
            "fda_category": "B",
            "pregnancy_details": "An toàn trong thai kỳ. Dữ liệu lâm sàng tốt, không có bằng chứng về dị tật thai nhi.",
            "lactation": {
                "safety": "Compatible",
                "details": "Bài tiết lượng nhỏ vào sữa; thường an toàn cho trẻ bú mẹ.",
                "recommendation": "Có thể dùng khi cho con bú. Theo dõi trẻ về các triệu chứng bất thường (hiếm).",
            },
        },
        "hepatic_adjustment": {
            "mild": "Không cần chỉnh liều.",
            "moderate": "Thận trọng, theo dõi men gan.",
            "severe": "Thận trọng, có thể cần giảm liều.",
            "notes": "Famotidine chuyển hóa ít qua gan, thải trừ chủ yếu qua thận.",
        },
        "overdose_management": {
            "symptoms": [
                "Nhức đầu",
                "Chóng mặt",
                "Rối loạn tiêu hóa",
                "Rối loạn nhịp tim (hiếm)",
            ],
            "antidote": "Không có antidote đặc hiệu.",
            "treatment": [
                "Điều trị hỗ trợ triệu chứng",
                "Theo dõi huyết áp, nhịp tim",
                "Than hoạt tính nếu uống trong vòng 1-2 giờ",
            ],
            "monitoring": "Huyết áp, nhịp tim, dấu hiệu sốc (hiếm).",
        },
        "reversal_agents": {
            "available": False,
            "agents": [],
            "notes": "Không có thuốc giải độc đặc hiệu. Điều trị hỗ trợ là chính.",
        },
        "administration_instructions": {
            "oral": {
                "with_food": "Có thể uống với hoặc không có thức ăn. Không ảnh hưởng đáng kể đến hấp thu.",
                "timing": "Uống 1-2 lần/ngày, có thể trước bữa ăn hoặc trước khi đi ngủ.",
                "notes": "Điều chỉnh liều theo chức năng thận. Tránh dùng cùng với thuốc cần acid để hấp thu (cách 2 giờ).",
            },
            "iv": {
                "reconstitution": "Pha trong NaCl 0.9% hoặc D5W, dùng ngay sau pha.",
                "infusion_rate": "Tiêm/truyền chậm trong ít nhất 2 phút.",
                "notes": "Theo dõi huyết áp, nhịp tim trong và sau khi truyền.",
            },
        },
    },
    # ======================== EMERGENCY: VASOPRESSORS ==========================
    "Norepinephrine": {
        "contraindications": {
            "tuyệt_đối": [],
            "tương_đối": [
                "Thiếu máu cục bộ mô (nếu có thể tránh)",
                "Rối loạn nhịp tim nặng",
                "Pheochromocytoma",
            ],
        },
        "drug_interactions": {
            "major": [
                {
                    "drug": "MAO inhibitors (MAOIs)",
                    "mechanism": "MAOIs ức chế chuyển hóa norepinephrine, tăng nồng độ",
                    "effect": "Tăng tác dụng mạnh, tăng huyết áp nặng, nguy cơ cơn tăng huyết áp",
                    "management": "Giảm liều norepinephrine xuống 50-75% khi dùng với MAOI. Theo dõi huyết áp sát.",
                },
                {
                    "drug": "Tricyclic antidepressants (TCA)",
                    "mechanism": "TCA ức chế tái hấp thu norepinephrine, tăng tác dụng",
                    "effect": "Tăng tác dụng mạnh, tăng huyết áp",
                    "management": "Giảm liều norepinephrine. Theo dõi huyết áp sát.",
                },
            ],
            "moderate": [
                {
                    "drug": "Beta-blockers",
                    "mechanism": "Block beta-receptors, tăng tác dụng alpha (co mạch)",
                    "effect": "Tăng huyết áp nặng, giảm nhịp tim",
                    "management": "Thận trọng. Theo dõi huyết áp và nhịp tim sát.",
                },
            ],
            "minor": [],
        },
        "pregnancy_lactation": {
            "fda_category": "C",
            "pregnancy_details": "An toàn trong cấp cứu. Dữ liệu hạn chế nhưng được sử dụng rộng rãi trong sốc thai kỳ.",
            "lactation": {
                "safety": "Compatible",
                "details": "Half-life rất ngắn (1-2 phút), không bài tiết vào sữa đáng kể.",
                "recommendation": "Có thể dùng khi cho con bú.",
            },
        },
        "hepatic_adjustment": {
            "mild": "Không cần chỉnh liều.",
            "moderate": "Không cần chỉnh liều.",
            "severe": "Không cần chỉnh liều.",
            "notes": "Norepinephrine bị bất hoạt nhanh bởi MAO và COMT, không phụ thuộc chức năng gan.",
        },
        "overdose_management": {
            "symptoms": [
                "Tăng huyết áp nặng",
                "Co mạch ngoại vi mạnh",
                "Hoại tử mô (nếu rò rỉ ngoài mạch)",
                "Rối loạn nhịp tim",
                "Giảm tưới máu thận, suy thận cấp",
            ],
            "antidote": "Phentolamine (alpha-blocker) để đối kháng tác dụng alpha.",
            "treatment": [
                "Ngừng truyền norepinephrine ngay lập tức",
                "Nếu rò rỉ ngoài mạch: tiêm phentolamine 5-10mg pha loãng quanh vị trí rò rỉ để giảm co mạch",
                "Phentolamine IV nếu tăng huyết áp nặng",
                "Theo dõi huyết áp, nhịp tim, tưới máu mô liên tục",
                "Truyền dịch nếu cần",
            ],
            "monitoring": "Huyết áp, nhịp tim, ECG, lactate máu, chức năng thận, tưới máu mô (da, thận, chi).",
        },
        "reversal_agents": {
            "available": True,
            "agents": ["Phentolamine (alpha-blocker)"],
            "notes": "Phentolamine có thể đối kháng tác dụng alpha của norepinephrine. Ngừng truyền là biện pháp chính.",
        },
        "administration_instructions": {
            "iv": {
                "reconstitution": "Pha 4mg trong 250ml D5W = 16 mcg/ml. Hoặc pha theo hướng dẫn nhà sản xuất.",
                "infusion_rate": "Truyền liên tục qua bơm tiêm điện, điều chỉnh theo huyết áp. Khởi đầu 0.05-0.1 mcg/kg/phút.",
                "notes": "TUYỆT ĐỐI phải truyền qua đường tĩnh mạch trung tâm (nguy cơ hoại tử nếu rò rỉ). Theo dõi huyết áp liên tục (arterial line nếu có thể).",
            },
        },
    },
    "Dopamine": {
        "contraindications": {
            "tuyệt_đối": [
                "Pheochromocytoma",
            ],
            "tương_đối": [
                "Rối loạn nhịp tim nặng",
                "Thiếu máu cục bộ mô",
            ],
        },
        "drug_interactions": {
            "major": [
                {
                    "drug": "MAO inhibitors (MAOIs)",
                    "mechanism": "MAOIs ức chế chuyển hóa dopamine, tăng nồng độ",
                    "effect": "Tăng tác dụng mạnh, tăng huyết áp nặng",
                    "management": "Giảm liều dopamine xuống 50-75% khi dùng với MAOI. Theo dõi huyết áp sát.",
                },
            ],
            "moderate": [
                {
                    "drug": "Beta-blockers",
                    "mechanism": "Block beta-receptors, tăng tác dụng alpha (ở liều cao)",
                    "effect": "Tăng huyết áp nặng",
                    "management": "Thận trọng. Theo dõi huyết áp và nhịp tim sát.",
                },
            ],
            "minor": [],
        },
        "pregnancy_lactation": {
            "fda_category": "C",
            "pregnancy_details": "An toàn trong cấp cứu. Dữ liệu hạn chế nhưng được sử dụng rộng rãi.",
            "lactation": {
                "safety": "Compatible",
                "details": "Half-life rất ngắn (1-2 phút), không bài tiết vào sữa đáng kể.",
                "recommendation": "Có thể dùng khi cho con bú.",
            },
        },
        "hepatic_adjustment": {
            "mild": "Không cần chỉnh liều.",
            "moderate": "Không cần chỉnh liều.",
            "severe": "Không cần chỉnh liều.",
            "notes": "Dopamine bị bất hoạt nhanh bởi MAO và COMT, không phụ thuộc chức năng gan.",
        },
        "overdose_management": {
            "symptoms": [
                "Rối loạn nhịp tim nặng",
                "Tăng huyết áp nặng (liều cao)",
                "Co mạch ngoại vi (liều cao)",
                "Hoại tử mô (nếu rò rỉ ngoài mạch)",
            ],
            "antidote": "Không có antidote đặc hiệu. Ngừng truyền là biện pháp chính.",
            "treatment": [
                "Ngừng truyền dopamine ngay lập tức",
                "Nếu rò rỉ ngoài mạch: tiêm phentolamine 5-10mg pha loãng quanh vị trí rò rỉ",
                "Theo dõi huyết áp, nhịp tim, ECG liên tục",
                "Điều trị rối loạn nhịp tim nếu cần",
            ],
            "monitoring": "Huyết áp, nhịp tim, ECG, tưới máu mô, dấu hiệu hoại tử.",
        },
        "reversal_agents": {
            "available": False,
            "agents": [],
            "notes": "Không có thuốc giải độc đặc hiệu. Ngừng truyền là biện pháp chính.",
        },
        "administration_instructions": {
            "iv": {
                "reconstitution": "Pha 400mg trong 250ml D5W = 1600 mcg/ml. Hoặc pha theo hướng dẫn nhà sản xuất.",
                "infusion_rate": "Truyền liên tục qua bơm tiêm điện, điều chỉnh theo huyết áp và tác dụng mong muốn. Tác dụng phụ thuộc liều.",
                "notes": "Truyền qua đường tĩnh mạch trung tâm (nguy cơ hoại tử nếu rò rỉ). Theo dõi huyết áp, nhịp tim liên tục. Không dùng liều thấp cho suy thận (không có bằng chứng).",
            },
        },
    },
    "Dobutamine": {
        "contraindications": {
            "tuyệt_đối": [
                "Hẹp động mạch chủ nặng",
            ],
            "tương_đối": [
                "Rối loạn nhịp tim nặng",
                "Sốc giảm thể tích (chưa bù dịch)",
                "Bệnh mạch vành không ổn định",
            ],
        },
        "drug_interactions": {
            "major": [],
            "moderate": [
                {
                    "drug": "Beta-blockers",
                    "mechanism": "Đối kháng tác dụng beta của dobutamine",
                    "effect": "Giảm hiệu quả dobutamine",
                    "management": "Có thể cần tăng liều dobutamine. Theo dõi cung lượng tim sát.",
                },
                {
                    "drug": "MAO inhibitors",
                    "mechanism": "MAOIs ức chế chuyển hóa catecholamine",
                    "effect": "Tăng tác dụng dobutamine",
                    "management": "Giảm liều dobutamine. Theo dõi nhịp tim, huyết áp sát.",
                },
            ],
            "minor": [],
        },
        "pregnancy_lactation": {
            "fda_category": "C",
            "pregnancy_details": "An toàn trong cấp cứu. Dữ liệu hạn chế nhưng được sử dụng rộng rãi.",
            "lactation": {
                "safety": "Compatible",
                "details": "Half-life rất ngắn (2 phút), không bài tiết vào sữa đáng kể.",
                "recommendation": "Có thể dùng khi cho con bú.",
            },
        },
        "hepatic_adjustment": {
            "mild": "Không cần chỉnh liều.",
            "moderate": "Không cần chỉnh liều.",
            "severe": "Không cần chỉnh liều.",
            "notes": "Dobutamine bị bất hoạt nhanh bởi MAO và COMT, không phụ thuộc chức năng gan.",
        },
        "overdose_management": {
            "symptoms": [
                "Tăng nhịp tim nặng",
                "Rối loạn nhịp tim",
                "Hạ huyết áp (do giãn mạch)",
                "Đau ngực",
                "Thiếu máu cục bộ cơ tim",
            ],
            "antidote": "Không có antidote đặc hiệu. Beta-blocker có thể đối kháng một phần.",
            "treatment": [
                "Ngừng truyền dobutamine ngay lập tức",
                "Theo dõi huyết áp, nhịp tim, ECG liên tục",
                "Điều trị rối loạn nhịp tim nếu cần",
                "Beta-blocker nếu nhịp tim quá nhanh (thận trọng)",
                "Truyền dịch nếu hạ huyết áp",
            ],
            "monitoring": "Huyết áp, nhịp tim, ECG, cung lượng tim, dấu hiệu thiếu máu cục bộ.",
        },
        "reversal_agents": {
            "available": False,
            "agents": [],
            "notes": "Không có thuốc giải độc đặc hiệu. Beta-blocker có thể đối kháng một phần nhưng không khuyến cáo thường quy.",
        },
        "administration_instructions": {
            "iv": {
                "reconstitution": "Pha 250mg trong 250ml D5W = 1000 mcg/ml. Hoặc pha theo hướng dẫn nhà sản xuất.",
                "infusion_rate": "Truyền liên tục qua bơm tiêm điện, điều chỉnh theo cung lượng tim. Khởi đầu 2.5-5 mcg/kg/phút.",
                "notes": "Bù dịch đầy đủ trước khi dùng (tránh hạ huyết áp). Theo dõi nhịp tim, ECG liên tục. Giảm liều khi cung lượng tim đã cải thiện.",
            },
        },
    },
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
    # ======================== GASTROINTESTINAL: PPIs ===========================
    "Rabeprazole": {
        "contraindications": {
            "tuyệt_đối": ["Dị ứng rabeprazole hoặc PPI", "Dùng cùng atazanavir"],
            "tương_đối": ["Suy gan nặng", "Loãng xương", "Nhiễm C. difficile"],
        },
        "drug_interactions": {
            "major": [
                {
                    "drug": "Atazanavir",
                    "mechanism": "Giảm hấp thu atazanavir",
                    "effect": "Giảm hiệu quả điều trị HIV",
                    "management": "CHỐNG CHỈ ĐỊNH dùng cùng.",
                },
            ],
            "moderate": [
                {"drug": "Warfarin", "mechanism": "Có thể tăng INR", "effect": "Tăng INR", "management": "Theo dõi INR."},
                {"drug": "Ketoconazole, Itraconazole", "mechanism": "Giảm hấp thu", "effect": "Giảm hiệu quả", "management": "Cách 2 giờ."},
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
            "moderate": "Thận trọng.",
            "severe": "Thận trọng, có thể giảm liều.",
            "notes": "Rabeprazole chuyển hóa qua gan (CYP2C19, CYP3A4).",
        },
        "overdose_management": {
            "symptoms": ["Nhức đầu", "Buồn nôn", "Tiêu chảy"],
            "antidote": "Không có antidote đặc hiệu.",
            "treatment": ["Điều trị hỗ trợ triệu chứng"],
            "monitoring": "Dấu hiệu sinh tồn.",
        },
        "reversal_agents": {"available": False, "agents": [], "notes": "Không có thuốc giải độc đặc hiệu."},
        "administration_instructions": {
            "oral": {
                "with_food": "Uống 30-60 phút TRƯỚC bữa ăn.",
                "timing": "Uống vào buổi sáng trước bữa sáng.",
                "notes": "KHÔNG được nhai hoặc nghiền viên bao tan trong ruột.",
            },
        },
    },
    "Tegoprazan": {
        "contraindications": {
            "tuyệt_đối": ["Dị ứng tegoprazan hoặc PCAB"],
            "tương_đối": ["Suy gan nặng", "Loãng xương"],
        },
        "drug_interactions": {
            "major": [],
            "moderate": [],
            "minor": [],
        },
        "pregnancy_lactation": {
            "fda_category": "Không có dữ liệu",
            "pregnancy_details": "Thiếu dữ liệu. Thận trọng trong thai kỳ.",
            "lactation": {"safety": "Unknown", "details": "Thiếu dữ liệu.", "recommendation": "Thận trọng khi cho con bú."},
        },
        "hepatic_adjustment": {
            "mild": "Không cần chỉnh liều.",
            "moderate": "Thận trọng.",
            "severe": "Thận trọng, có thể giảm liều.",
            "notes": "Tegoprazan chuyển hóa qua gan.",
        },
        "reversal_agents": {"available": False, "agents": [], "notes": "Không có thuốc giải độc đặc hiệu."},
        "administration_instructions": {
            "oral": {
                "with_food": "Có thể uống với hoặc không có thức ăn.",
                "timing": "Uống 1 lần/ngày.",
                "notes": "PCAB (Potassium-Competitive Acid Blocker), tác dụng nhanh hơn PPI.",
            },
        },
    },
    "Vonoprazan": {
        "contraindications": {
            "tuyệt_đối": ["Dị ứng vonoprazan hoặc PCAB"],
            "tương_đối": ["Suy gan nặng", "Loãng xương"],
        },
        "drug_interactions": {
            "major": [],
            "moderate": [],
            "minor": [],
        },
        "pregnancy_lactation": {
            "fda_category": "Không có dữ liệu",
            "pregnancy_details": "Thiếu dữ liệu. Thận trọng trong thai kỳ.",
            "lactation": {"safety": "Unknown", "details": "Thiếu dữ liệu.", "recommendation": "Thận trọng khi cho con bú."},
        },
        "hepatic_adjustment": {
            "mild": "Không cần chỉnh liều.",
            "moderate": "Thận trọng.",
            "severe": "Thận trọng, có thể giảm liều.",
            "notes": "Vonoprazan chuyển hóa qua gan.",
        },
        "reversal_agents": {"available": False, "agents": [], "notes": "Không có thuốc giải độc đặc hiệu."},
        "administration_instructions": {
            "oral": {
                "with_food": "Có thể uống với hoặc không có thức ăn.",
                "timing": "Uống 1 lần/ngày.",
                "notes": "PCAB (Potassium-Competitive Acid Blocker), tác dụng nhanh hơn PPI.",
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
}


EXTRA_ENHANCED_FIELDS.update({
    "5-Fluorouracil": {
        "risk_flags": {
            "high_alert": True,
            "narrow_therapeutic_index": False,
            "look_alike_sound_alike": [],
            "organ_toxicity": {'hepatic': 'unknown', 'renal': 'unknown', 'cardiac': 'unknown', 'hematologic': 'unknown'},
            "requires_double_check": True,
            "icu_critical_care_only": False,
        },
    },
    "Adenosine": {
        "risk_flags": {
            "high_alert": True,
            "narrow_therapeutic_index": True,
            "look_alike_sound_alike": [],
            "organ_toxicity": {'hepatic': 'unknown', 'renal': 'unknown', 'cardiac': 'unknown', 'hematologic': 'unknown'},
            "requires_double_check": True,
            "icu_critical_care_only": False,
        },
    },
    "Alteplase": {
        "risk_flags": {
            "high_alert": True,
            "narrow_therapeutic_index": False,
            "look_alike_sound_alike": [],
            "organ_toxicity": {'hepatic': 'unknown', 'renal': 'unknown', 'cardiac': 'unknown', 'hematologic': 'unknown'},
            "requires_double_check": True,
            "icu_critical_care_only": False,
        },
    },
    "Amikacin": {
        "risk_flags": {
            "high_alert": False,
            "narrow_therapeutic_index": True,
            "look_alike_sound_alike": [],
            "organ_toxicity": {'hepatic': 'unknown', 'renal': 'unknown', 'cardiac': 'unknown', 'hematologic': 'unknown'},
            "requires_double_check": False,
            "icu_critical_care_only": False,
        },
    },
    "Amiodarone": {
        "risk_flags": {
            "high_alert": True,
            "narrow_therapeutic_index": True,
            "look_alike_sound_alike": [],
            "organ_toxicity": {'hepatic': 'unknown', 'renal': 'unknown', 'cardiac': 'unknown', 'hematologic': 'unknown'},
            "requires_double_check": True,
            "icu_critical_care_only": False,
        },
    },
    "Apixaban": {
        "risk_flags": {
            "high_alert": True,
            "narrow_therapeutic_index": False,
            "look_alike_sound_alike": [],
            "organ_toxicity": {'hepatic': 'unknown', 'renal': 'unknown', 'cardiac': 'unknown', 'hematologic': 'unknown'},
            "requires_double_check": True,
            "icu_critical_care_only": False,
        },
    },
    "Aspirin": {
        "risk_flags": {
            "high_alert": True,
            "narrow_therapeutic_index": False,
            "look_alike_sound_alike": [],
            "organ_toxicity": {'hepatic': 'unknown', 'renal': 'unknown', 'cardiac': 'unknown', 'hematologic': 'unknown'},
            "requires_double_check": True,
            "icu_critical_care_only": False,
        },
    },
    "Azathioprine": {
        "risk_flags": {
            "high_alert": True,
            "narrow_therapeutic_index": False,
            "look_alike_sound_alike": [],
            "organ_toxicity": {'hepatic': 'unknown', 'renal': 'unknown', 'cardiac': 'unknown', 'hematologic': 'unknown'},
            "requires_double_check": True,
            "icu_critical_care_only": False,
        },
    },
    "Carbamazepine": {
        "risk_flags": {
            "high_alert": False,
            "narrow_therapeutic_index": True,
            "look_alike_sound_alike": [],
            "organ_toxicity": {'hepatic': 'unknown', 'renal': 'unknown', 'cardiac': 'unknown', 'hematologic': 'unknown'},
            "requires_double_check": False,
            "icu_critical_care_only": False,
        },
    },
    "Carboplatin": {
        "risk_flags": {
            "high_alert": True,
            "narrow_therapeutic_index": False,
            "look_alike_sound_alike": [],
            "organ_toxicity": {'hepatic': 'unknown', 'renal': 'unknown', 'cardiac': 'unknown', 'hematologic': 'unknown'},
            "requires_double_check": True,
            "icu_critical_care_only": False,
        },
    },
    "Cisplatin": {
        "risk_flags": {
            "high_alert": True,
            "narrow_therapeutic_index": False,
            "look_alike_sound_alike": [],
            "organ_toxicity": {'hepatic': 'unknown', 'renal': 'unknown', 'cardiac': 'unknown', 'hematologic': 'unknown'},
            "requires_double_check": True,
            "icu_critical_care_only": False,
        },
    },
    "Clopidogrel": {
        "risk_flags": {
            "high_alert": True,
            "narrow_therapeutic_index": False,
            "look_alike_sound_alike": [],
            "organ_toxicity": {'hepatic': 'unknown', 'renal': 'unknown', 'cardiac': 'unknown', 'hematologic': 'unknown'},
            "requires_double_check": True,
            "icu_critical_care_only": False,
        },
    },
    "Codeine": {
        "risk_flags": {
            "high_alert": True,
            "narrow_therapeutic_index": False,
            "look_alike_sound_alike": [],
            "organ_toxicity": {'hepatic': 'unknown', 'renal': 'unknown', 'cardiac': 'unknown', 'hematologic': 'unknown'},
            "requires_double_check": True,
            "icu_critical_care_only": False,
        },
    },
    "Cyclophosphamide": {
        "risk_flags": {
            "high_alert": True,
            "narrow_therapeutic_index": False,
            "look_alike_sound_alike": [],
            "organ_toxicity": {'hepatic': 'unknown', 'renal': 'unknown', 'cardiac': 'unknown', 'hematologic': 'unknown'},
            "requires_double_check": True,
            "icu_critical_care_only": False,
        },
    },
    "Cyclosporine": {
        "risk_flags": {
            "high_alert": True,
            "narrow_therapeutic_index": False,
            "look_alike_sound_alike": [],
            "organ_toxicity": {'hepatic': 'unknown', 'renal': 'unknown', 'cardiac': 'unknown', 'hematologic': 'unknown'},
            "requires_double_check": True,
            "icu_critical_care_only": False,
        },
    },
    "Dabigatran": {
        "risk_flags": {
            "high_alert": True,
            "narrow_therapeutic_index": False,
            "look_alike_sound_alike": [],
            "organ_toxicity": {'hepatic': 'unknown', 'renal': 'unknown', 'cardiac': 'unknown', 'hematologic': 'unknown'},
            "requires_double_check": True,
            "icu_critical_care_only": False,
        },
    },
    "Digoxin": {
        "risk_flags": {
            "high_alert": False,
            "narrow_therapeutic_index": True,
            "look_alike_sound_alike": [],
            "organ_toxicity": {'hepatic': 'unknown', 'renal': 'unknown', 'cardiac': 'unknown', 'hematologic': 'unknown'},
            "requires_double_check": False,
            "icu_critical_care_only": False,
        },
    },
    "Dipyridamole": {
        "risk_flags": {
            "high_alert": True,
            "narrow_therapeutic_index": False,
            "look_alike_sound_alike": [],
            "organ_toxicity": {'hepatic': 'unknown', 'renal': 'unknown', 'cardiac': 'unknown', 'hematologic': 'unknown'},
            "requires_double_check": True,
            "icu_critical_care_only": False,
        },
    },
    "Dobutamine": {
        "risk_flags": {
            "high_alert": True,
            "narrow_therapeutic_index": False,
            "look_alike_sound_alike": [],
            "organ_toxicity": {'hepatic': 'unknown', 'renal': 'unknown', 'cardiac': 'unknown', 'hematologic': 'unknown'},
            "requires_double_check": True,
            "icu_critical_care_only": False,
        },
    },
    "Docetaxel": {
        "risk_flags": {
            "high_alert": True,
            "narrow_therapeutic_index": False,
            "look_alike_sound_alike": [],
            "organ_toxicity": {'hepatic': 'unknown', 'renal': 'unknown', 'cardiac': 'unknown', 'hematologic': 'unknown'},
            "requires_double_check": True,
            "icu_critical_care_only": False,
        },
    },
    "Dopamine": {
        "risk_flags": {
            "high_alert": True,
            "narrow_therapeutic_index": False,
            "look_alike_sound_alike": [],
            "organ_toxicity": {'hepatic': 'unknown', 'renal': 'unknown', 'cardiac': 'unknown', 'hematologic': 'unknown'},
            "requires_double_check": True,
            "icu_critical_care_only": False,
        },
    },
    "Doxorubicin": {
        "risk_flags": {
            "high_alert": True,
            "narrow_therapeutic_index": False,
            "look_alike_sound_alike": [],
            "organ_toxicity": {'hepatic': 'unknown', 'renal': 'unknown', 'cardiac': 'unknown', 'hematologic': 'unknown'},
            "requires_double_check": True,
            "icu_critical_care_only": False,
        },
    },
    "Dronedarone": {
        "risk_flags": {
            "high_alert": True,
            "narrow_therapeutic_index": True,
            "look_alike_sound_alike": [],
            "organ_toxicity": {'hepatic': 'unknown', 'renal': 'unknown', 'cardiac': 'unknown', 'hematologic': 'unknown'},
            "requires_double_check": True,
            "icu_critical_care_only": False,
        },
    },
    "Edoxaban": {
        "risk_flags": {
            "high_alert": True,
            "narrow_therapeutic_index": False,
            "look_alike_sound_alike": [],
            "organ_toxicity": {'hepatic': 'unknown', 'renal': 'unknown', 'cardiac': 'unknown', 'hematologic': 'unknown'},
            "requires_double_check": True,
            "icu_critical_care_only": False,
        },
    },
    "Enoxaparin": {
        "risk_flags": {
            "high_alert": True,
            "narrow_therapeutic_index": False,
            "look_alike_sound_alike": [],
            "organ_toxicity": {'hepatic': 'unknown', 'renal': 'unknown', 'cardiac': 'unknown', 'hematologic': 'unknown'},
            "requires_double_check": True,
            "icu_critical_care_only": False,
        },
    },
    "Epinephrine": {
        "risk_flags": {
            "high_alert": True,
            "narrow_therapeutic_index": False,
            "look_alike_sound_alike": [],
            "organ_toxicity": {'hepatic': 'unknown', 'renal': 'unknown', 'cardiac': 'unknown', 'hematologic': 'unknown'},
            "requires_double_check": True,
            "icu_critical_care_only": False,
        },
    },
    "Ethosuximide": {
        "risk_flags": {
            "high_alert": False,
            "narrow_therapeutic_index": True,
            "look_alike_sound_alike": [],
            "organ_toxicity": {'hepatic': 'unknown', 'renal': 'unknown', 'cardiac': 'unknown', 'hematologic': 'unknown'},
            "requires_double_check": False,
            "icu_critical_care_only": False,
        },
    },
    "Fentanyl": {
        "risk_flags": {
            "high_alert": True,
            "narrow_therapeutic_index": False,
            "look_alike_sound_alike": [],
            "organ_toxicity": {'hepatic': 'unknown', 'renal': 'unknown', 'cardiac': 'unknown', 'hematologic': 'unknown'},
            "requires_double_check": True,
            "icu_critical_care_only": False,
        },
    },
    "Flecainide": {
        "risk_flags": {
            "high_alert": True,
            "narrow_therapeutic_index": True,
            "look_alike_sound_alike": [],
            "organ_toxicity": {'hepatic': 'unknown', 'renal': 'unknown', 'cardiac': 'unknown', 'hematologic': 'unknown'},
            "requires_double_check": True,
            "icu_critical_care_only": False,
        },
    },
    "Fondaparinux": {
        "risk_flags": {
            "high_alert": True,
            "narrow_therapeutic_index": False,
            "look_alike_sound_alike": [],
            "organ_toxicity": {'hepatic': 'unknown', 'renal': 'unknown', 'cardiac': 'unknown', 'hematologic': 'unknown'},
            "requires_double_check": True,
            "icu_critical_care_only": False,
        },
    },
    "Gabapentin": {
        "risk_flags": {
            "high_alert": False,
            "narrow_therapeutic_index": True,
            "look_alike_sound_alike": [],
            "organ_toxicity": {'hepatic': 'unknown', 'renal': 'unknown', 'cardiac': 'unknown', 'hematologic': 'unknown'},
            "requires_double_check": False,
            "icu_critical_care_only": False,
        },
    },
    "Gemcitabine": {
        "risk_flags": {
            "high_alert": True,
            "narrow_therapeutic_index": False,
            "look_alike_sound_alike": [],
            "organ_toxicity": {'hepatic': 'unknown', 'renal': 'unknown', 'cardiac': 'unknown', 'hematologic': 'unknown'},
            "requires_double_check": True,
            "icu_critical_care_only": False,
        },
    },
    "Gentamicin": {
        "risk_flags": {
            "high_alert": False,
            "narrow_therapeutic_index": True,
            "look_alike_sound_alike": [],
            "organ_toxicity": {'hepatic': 'unknown', 'renal': 'unknown', 'cardiac': 'unknown', 'hematologic': 'unknown'},
            "requires_double_check": False,
            "icu_critical_care_only": False,
        },
    },
    "Granisetron": {
        "risk_flags": {
            "high_alert": True,
            "narrow_therapeutic_index": False,
            "look_alike_sound_alike": [],
            "organ_toxicity": {'hepatic': 'unknown', 'renal': 'unknown', 'cardiac': 'unknown', 'hematologic': 'unknown'},
            "requires_double_check": True,
            "icu_critical_care_only": False,
        },
    },
    "Heparin": {
        "risk_flags": {
            "high_alert": True,
            "narrow_therapeutic_index": False,
            "look_alike_sound_alike": [],
            "organ_toxicity": {'hepatic': 'unknown', 'renal': 'unknown', 'cardiac': 'unknown', 'hematologic': 'unknown'},
            "requires_double_check": True,
            "icu_critical_care_only": False,
        },
    },
    "Hydrocodone": {
        "risk_flags": {
            "high_alert": True,
            "narrow_therapeutic_index": False,
            "look_alike_sound_alike": [],
            "organ_toxicity": {'hepatic': 'unknown', 'renal': 'unknown', 'cardiac': 'unknown', 'hematologic': 'unknown'},
            "requires_double_check": True,
            "icu_critical_care_only": False,
        },
    },
    "Hydromorphone": {
        "risk_flags": {
            "high_alert": True,
            "narrow_therapeutic_index": False,
            "look_alike_sound_alike": [],
            "organ_toxicity": {'hepatic': 'unknown', 'renal': 'unknown', 'cardiac': 'unknown', 'hematologic': 'unknown'},
            "requires_double_check": True,
            "icu_critical_care_only": False,
        },
    },
    "Ifosfamide": {
        "risk_flags": {
            "high_alert": True,
            "narrow_therapeutic_index": False,
            "look_alike_sound_alike": [],
            "organ_toxicity": {'hepatic': 'unknown', 'renal': 'unknown', 'cardiac': 'unknown', 'hematologic': 'unknown'},
            "requires_double_check": True,
            "icu_critical_care_only": False,
        },
    },
    "Insulin": {
        "risk_flags": {
            "high_alert": True,
            "narrow_therapeutic_index": False,
            "look_alike_sound_alike": [],
            "organ_toxicity": {'hepatic': 'unknown', 'renal': 'unknown', 'cardiac': 'unknown', 'hematologic': 'unknown'},
            "requires_double_check": True,
            "icu_critical_care_only": False,
        },
    },
    "Irinotecan": {
        "risk_flags": {
            "high_alert": True,
            "narrow_therapeutic_index": False,
            "look_alike_sound_alike": [],
            "organ_toxicity": {'hepatic': 'unknown', 'renal': 'unknown', 'cardiac': 'unknown', 'hematologic': 'unknown'},
            "requires_double_check": True,
            "icu_critical_care_only": False,
        },
    },
    "Lacosamide": {
        "risk_flags": {
            "high_alert": False,
            "narrow_therapeutic_index": True,
            "look_alike_sound_alike": [],
            "organ_toxicity": {'hepatic': 'unknown', 'renal': 'unknown', 'cardiac': 'unknown', 'hematologic': 'unknown'},
            "requires_double_check": False,
            "icu_critical_care_only": False,
        },
    },
    "Lamotrigine": {
        "risk_flags": {
            "high_alert": False,
            "narrow_therapeutic_index": True,
            "look_alike_sound_alike": [],
            "organ_toxicity": {'hepatic': 'unknown', 'renal': 'unknown', 'cardiac': 'unknown', 'hematologic': 'unknown'},
            "requires_double_check": False,
            "icu_critical_care_only": False,
        },
    },
    "Levetiracetam": {
        "risk_flags": {
            "high_alert": False,
            "narrow_therapeutic_index": True,
            "look_alike_sound_alike": [],
            "organ_toxicity": {'hepatic': 'unknown', 'renal': 'unknown', 'cardiac': 'unknown', 'hematologic': 'unknown'},
            "requires_double_check": False,
            "icu_critical_care_only": False,
        },
    },
    "Lidocaine": {
        "risk_flags": {
            "high_alert": True,
            "narrow_therapeutic_index": True,
            "look_alike_sound_alike": [],
            "organ_toxicity": {'hepatic': 'unknown', 'renal': 'unknown', 'cardiac': 'unknown', 'hematologic': 'unknown'},
            "requires_double_check": True,
            "icu_critical_care_only": False,
        },
    },
    "Methotrexate": {
        "risk_flags": {
            "high_alert": True,
            "narrow_therapeutic_index": False,
            "look_alike_sound_alike": [],
            "organ_toxicity": {'hepatic': 'unknown', 'renal': 'unknown', 'cardiac': 'unknown', 'hematologic': 'unknown'},
            "requires_double_check": True,
            "icu_critical_care_only": False,
        },
    },
    "Morphine": {
        "risk_flags": {
            "high_alert": True,
            "narrow_therapeutic_index": False,
            "look_alike_sound_alike": [],
            "organ_toxicity": {'hepatic': 'unknown', 'renal': 'unknown', 'cardiac': 'unknown', 'hematologic': 'unknown'},
            "requires_double_check": True,
            "icu_critical_care_only": False,
        },
    },
    "Mycophenolate": {
        "risk_flags": {
            "high_alert": True,
            "narrow_therapeutic_index": False,
            "look_alike_sound_alike": [],
            "organ_toxicity": {'hepatic': 'unknown', 'renal': 'unknown', 'cardiac': 'unknown', 'hematologic': 'unknown'},
            "requires_double_check": True,
            "icu_critical_care_only": False,
        },
    },
    "Naloxone": {
        "risk_flags": {
            "high_alert": True,
            "narrow_therapeutic_index": False,
            "look_alike_sound_alike": [],
            "organ_toxicity": {'hepatic': 'unknown', 'renal': 'unknown', 'cardiac': 'unknown', 'hematologic': 'unknown'},
            "requires_double_check": True,
            "icu_critical_care_only": False,
        },
    },
    "Norepinephrine": {
        "risk_flags": {
            "high_alert": True,
            "narrow_therapeutic_index": False,
            "look_alike_sound_alike": [],
            "organ_toxicity": {'hepatic': 'unknown', 'renal': 'unknown', 'cardiac': 'unknown', 'hematologic': 'unknown'},
            "requires_double_check": True,
            "icu_critical_care_only": False,
        },
    },
    "Oxaliplatin": {
        "risk_flags": {
            "high_alert": True,
            "narrow_therapeutic_index": False,
            "look_alike_sound_alike": [],
            "organ_toxicity": {'hepatic': 'unknown', 'renal': 'unknown', 'cardiac': 'unknown', 'hematologic': 'unknown'},
            "requires_double_check": True,
            "icu_critical_care_only": False,
        },
    },
    "Oxcarbazepine": {
        "risk_flags": {
            "high_alert": False,
            "narrow_therapeutic_index": True,
            "look_alike_sound_alike": [],
            "organ_toxicity": {'hepatic': 'unknown', 'renal': 'unknown', 'cardiac': 'unknown', 'hematologic': 'unknown'},
            "requires_double_check": False,
            "icu_critical_care_only": False,
        },
    },
    "Oxycodone": {
        "risk_flags": {
            "high_alert": True,
            "narrow_therapeutic_index": False,
            "look_alike_sound_alike": [],
            "organ_toxicity": {'hepatic': 'unknown', 'renal': 'unknown', 'cardiac': 'unknown', 'hematologic': 'unknown'},
            "requires_double_check": True,
            "icu_critical_care_only": False,
        },
    },
    "Paclitaxel": {
        "risk_flags": {
            "high_alert": True,
            "narrow_therapeutic_index": False,
            "look_alike_sound_alike": [],
            "organ_toxicity": {'hepatic': 'unknown', 'renal': 'unknown', 'cardiac': 'unknown', 'hematologic': 'unknown'},
            "requires_double_check": True,
            "icu_critical_care_only": False,
        },
    },
    "Palonosetron": {
        "risk_flags": {
            "high_alert": True,
            "narrow_therapeutic_index": False,
            "look_alike_sound_alike": [],
            "organ_toxicity": {'hepatic': 'unknown', 'renal': 'unknown', 'cardiac': 'unknown', 'hematologic': 'unknown'},
            "requires_double_check": True,
            "icu_critical_care_only": False,
        },
    },
    "Perampanel": {
        "risk_flags": {
            "high_alert": False,
            "narrow_therapeutic_index": True,
            "look_alike_sound_alike": [],
            "organ_toxicity": {'hepatic': 'unknown', 'renal': 'unknown', 'cardiac': 'unknown', 'hematologic': 'unknown'},
            "requires_double_check": False,
            "icu_critical_care_only": False,
        },
    },
    "Phenobarbital": {
        "risk_flags": {
            "high_alert": False,
            "narrow_therapeutic_index": True,
            "look_alike_sound_alike": [],
            "organ_toxicity": {'hepatic': 'unknown', 'renal': 'unknown', 'cardiac': 'unknown', 'hematologic': 'unknown'},
            "requires_double_check": False,
            "icu_critical_care_only": False,
        },
    },
    "Phenytoin": {
        "risk_flags": {
            "high_alert": False,
            "narrow_therapeutic_index": True,
            "look_alike_sound_alike": [],
            "organ_toxicity": {'hepatic': 'unknown', 'renal': 'unknown', 'cardiac': 'unknown', 'hematologic': 'unknown'},
            "requires_double_check": False,
            "icu_critical_care_only": False,
        },
    },
    "Prasugrel": {
        "risk_flags": {
            "high_alert": True,
            "narrow_therapeutic_index": False,
            "look_alike_sound_alike": [],
            "organ_toxicity": {'hepatic': 'unknown', 'renal': 'unknown', 'cardiac': 'unknown', 'hematologic': 'unknown'},
            "requires_double_check": True,
            "icu_critical_care_only": False,
        },
    },
    "Pregabalin": {
        "risk_flags": {
            "high_alert": False,
            "narrow_therapeutic_index": True,
            "look_alike_sound_alike": [],
            "organ_toxicity": {'hepatic': 'unknown', 'renal': 'unknown', 'cardiac': 'unknown', 'hematologic': 'unknown'},
            "requires_double_check": False,
            "icu_critical_care_only": False,
        },
    },
    "Primidone": {
        "risk_flags": {
            "high_alert": False,
            "narrow_therapeutic_index": True,
            "look_alike_sound_alike": [],
            "organ_toxicity": {'hepatic': 'unknown', 'renal': 'unknown', 'cardiac': 'unknown', 'hematologic': 'unknown'},
            "requires_double_check": False,
            "icu_critical_care_only": False,
        },
    },
    "Procainamide": {
        "risk_flags": {
            "high_alert": True,
            "narrow_therapeutic_index": True,
            "look_alike_sound_alike": [],
            "organ_toxicity": {'hepatic': 'unknown', 'renal': 'unknown', 'cardiac': 'unknown', 'hematologic': 'unknown'},
            "requires_double_check": True,
            "icu_critical_care_only": False,
        },
    },
    "Propafenone": {
        "risk_flags": {
            "high_alert": True,
            "narrow_therapeutic_index": True,
            "look_alike_sound_alike": [],
            "organ_toxicity": {'hepatic': 'unknown', 'renal': 'unknown', 'cardiac': 'unknown', 'hematologic': 'unknown'},
            "requires_double_check": True,
            "icu_critical_care_only": False,
        },
    },
    "Protamine": {
        "risk_flags": {
            "high_alert": True,
            "narrow_therapeutic_index": False,
            "look_alike_sound_alike": [],
            "organ_toxicity": {'hepatic': 'unknown', 'renal': 'unknown', 'cardiac': 'unknown', 'hematologic': 'unknown'},
            "requires_double_check": True,
            "icu_critical_care_only": False,
        },
    },
    "Rivaroxaban": {
        "risk_flags": {
            "high_alert": True,
            "narrow_therapeutic_index": False,
            "look_alike_sound_alike": [],
            "organ_toxicity": {'hepatic': 'unknown', 'renal': 'unknown', 'cardiac': 'unknown', 'hematologic': 'unknown'},
            "requires_double_check": True,
            "icu_critical_care_only": False,
        },
    },
    "Tacrolimus": {
        "risk_flags": {
            "high_alert": True,
            "narrow_therapeutic_index": False,
            "look_alike_sound_alike": [],
            "organ_toxicity": {'hepatic': 'unknown', 'renal': 'unknown', 'cardiac': 'unknown', 'hematologic': 'unknown'},
            "requires_double_check": True,
            "icu_critical_care_only": False,
        },
    },
    "Theophylline": {
        "risk_flags": {
            "high_alert": False,
            "narrow_therapeutic_index": True,
            "look_alike_sound_alike": [],
            "organ_toxicity": {'hepatic': 'unknown', 'renal': 'unknown', 'cardiac': 'unknown', 'hematologic': 'unknown'},
            "requires_double_check": False,
            "icu_critical_care_only": False,
        },
    },
    "Ticagrelor": {
        "risk_flags": {
            "high_alert": True,
            "narrow_therapeutic_index": False,
            "look_alike_sound_alike": [],
            "organ_toxicity": {'hepatic': 'unknown', 'renal': 'unknown', 'cardiac': 'unknown', 'hematologic': 'unknown'},
            "requires_double_check": True,
            "icu_critical_care_only": False,
        },
    },
    "Ticlopidine": {
        "risk_flags": {
            "high_alert": True,
            "narrow_therapeutic_index": False,
            "look_alike_sound_alike": [],
            "organ_toxicity": {'hepatic': 'unknown', 'renal': 'unknown', 'cardiac': 'unknown', 'hematologic': 'unknown'},
            "requires_double_check": True,
            "icu_critical_care_only": False,
        },
    },
    "Tobramycin": {
        "risk_flags": {
            "high_alert": False,
            "narrow_therapeutic_index": True,
            "look_alike_sound_alike": [],
            "organ_toxicity": {'hepatic': 'unknown', 'renal': 'unknown', 'cardiac': 'unknown', 'hematologic': 'unknown'},
            "requires_double_check": False,
            "icu_critical_care_only": False,
        },
    },
    "Topiramate": {
        "risk_flags": {
            "high_alert": False,
            "narrow_therapeutic_index": True,
            "look_alike_sound_alike": [],
            "organ_toxicity": {'hepatic': 'unknown', 'renal': 'unknown', 'cardiac': 'unknown', 'hematologic': 'unknown'},
            "requires_double_check": False,
            "icu_critical_care_only": False,
        },
    },
    "Tramadol": {
        "risk_flags": {
            "high_alert": True,
            "narrow_therapeutic_index": False,
            "look_alike_sound_alike": [],
            "organ_toxicity": {'hepatic': 'unknown', 'renal': 'unknown', 'cardiac': 'unknown', 'hematologic': 'unknown'},
            "requires_double_check": True,
            "icu_critical_care_only": False,
        },
    },
    "Valproate": {
        "risk_flags": {
            "high_alert": False,
            "narrow_therapeutic_index": True,
            "look_alike_sound_alike": [],
            "organ_toxicity": {'hepatic': 'unknown', 'renal': 'unknown', 'cardiac': 'unknown', 'hematologic': 'unknown'},
            "requires_double_check": False,
            "icu_critical_care_only": False,
        },
    },
    "Vancomycin": {
        "risk_flags": {
            "high_alert": False,
            "narrow_therapeutic_index": True,
            "look_alike_sound_alike": [],
            "organ_toxicity": {'hepatic': 'unknown', 'renal': 'unknown', 'cardiac': 'unknown', 'hematologic': 'unknown'},
            "requires_double_check": False,
            "icu_critical_care_only": False,
        },
    },
    "Vasopressin": {
        "risk_flags": {
            "high_alert": True,
            "narrow_therapeutic_index": False,
            "look_alike_sound_alike": [],
            "organ_toxicity": {'hepatic': 'unknown', 'renal': 'unknown', 'cardiac': 'unknown', 'hematologic': 'unknown'},
            "requires_double_check": True,
            "icu_critical_care_only": False,
        },
    },
    "Vitamin K": {
        "risk_flags": {
            "high_alert": True,
            "narrow_therapeutic_index": False,
            "look_alike_sound_alike": [],
            "organ_toxicity": {'hepatic': 'unknown', 'renal': 'unknown', 'cardiac': 'unknown', 'hematologic': 'unknown'},
            "requires_double_check": True,
            "icu_critical_care_only": False,
        },
    },
    "Warfarin": {
        "risk_flags": {
            "high_alert": True,
            "narrow_therapeutic_index": False,
            "look_alike_sound_alike": [],
            "organ_toxicity": {'hepatic': 'unknown', 'renal': 'unknown', 'cardiac': 'unknown', 'hematologic': 'unknown'},
            "requires_double_check": True,
            "icu_critical_care_only": False,
        },
    },
    "Zonisamide": {
        "risk_flags": {
            "high_alert": False,
            "narrow_therapeutic_index": True,
            "look_alike_sound_alike": [],
            "organ_toxicity": {'hepatic': 'unknown', 'renal': 'unknown', 'cardiac': 'unknown', 'hematologic': 'unknown'},
            "requires_double_check": False,
            "icu_critical_care_only": False,
        },
    },
})


EXTRA_ENHANCED_FIELDS.update({
    # ======================== CARDIOVASCULAR – ACE INHIBITORS ========================
    "Enalapril": {
        "guideline_tags": {
            "who_atc": "C09AA02",
            "ahfs_category": "24.08.08 ACE Inhibitors",
            "vietnam_essential_medicines": True,
            "international_guidelines": [
                {
                    "source": "ESC 2021 Heart Failure",
                    "recommendation": "ACE inhibitor first-line therapy for HFrEF if tolerated",
                    "context": "Heart failure with reduced ejection fraction (HFrEF), NYHA II–III",
                },
                {
                    "source": "ACC/AHA 2017 Hypertension Guideline",
                    "recommendation": "One of the first-line options for hypertension",
                    "context": "Primary hypertension, non-black, with or without diabetes",
                },
            ],
            "vn_guidelines": [
                {
                    "source": "BYT – Hướng dẫn chẩn đoán và điều trị tăng huyết áp 2020",
                    "recommendation": "Một trong các lựa chọn hàng đầu điều trị tăng huyết áp",
                    "context": "Tăng huyết áp nguyên phát không biến chứng, ưu tiên bệnh nhân có đái tháo đường hoặc bệnh thận mạn",
                }
            ],
            "clinical_tags": [
                "first_line_htn",
                "hfref_mortality_benefit",
                "ckd_proteinuria_bp_control",
            ],
        },
        "availability_vietnam": {
            "status": "common",
            "level_of_care": ["district", "provincial", "central"],
            "insurance_coverage": "bhyt_full",
            "brand_examples": ["Enalapril STADA", "Renitec"],
            "notes": "Rất phổ biến trong điều trị tăng huyết áp và suy tim; thường có trong danh mục BHYT.",
        },
    },
    "Lisinopril": {
        "guideline_tags": {
            "who_atc": "C09AA03",
            "ahfs_category": "24.08.08 ACE Inhibitors",
            "vietnam_essential_medicines": True,
            "international_guidelines": [
                {
                    "source": "ESC 2021 Heart Failure",
                    "recommendation": "ACE inhibitor first-line therapy for HFrEF if ARNI not available",
                    "context": "Heart failure with reduced ejection fraction (HFrEF), NYHA II–III",
                }
            ],
            "vn_guidelines": [
                {
                    "source": "BYT – Hướng dẫn chẩn đoán và điều trị suy tim 2015",
                    "recommendation": "Thuốc nền tảng trong điều trị suy tim HFrEF cùng với beta-blocker và mineralocorticoid receptor antagonist",
                    "context": "Suy tim mạn HFrEF, NYHA II–IV",
                }
            ],
            "clinical_tags": [
                "first_line_htn",
                "hfref_mortality_benefit",
            ],
        },
        "availability_vietnam": {
            "status": "common",
            "level_of_care": ["provincial", "central"],
            "insurance_coverage": "bhyt_full",
            "brand_examples": ["Zestril", "Lisinopril STADA"],
            "notes": "Có mặt ở hầu hết bệnh viện tuyến tỉnh trở lên; một số nơi dùng Enalapril hoặc Perindopril thay thế.",
        },
    },
    "Ramipril": {
        "guideline_tags": {
            "who_atc": "C09AA05",
            "ahfs_category": "24.08.08 ACE Inhibitors",
            "vietnam_essential_medicines": False,
            "international_guidelines": [
                {
                    "source": "HOPE Study / ESC Prevention Guidelines",
                    "recommendation": "ACE inhibitor to reduce CV events in high-risk patients",
                    "context": "Secondary prevention in patients with high cardiovascular risk (coronary artery disease, diabetes, prior stroke)",
                }
            ],
            "vn_guidelines": [],
            "clinical_tags": [
                "cv_risk_reduction",
                "htn_high_risk",
            ],
        },
        "availability_vietnam": {
            "status": "limited",
            "level_of_care": ["provincial", "central", "private"],
            "insurance_coverage": "bhyt_partial",
            "brand_examples": ["Tritace", "Altace"],
            "notes": "Phổ biến hơn ở bệnh viện tuyến cuối và phòng khám tư nhân; dùng cho bệnh nhân nguy cơ tim mạch cao.",
        },
    },
    "Perindopril": {
        "guideline_tags": {
            "who_atc": "C09AA04",
            "ahfs_category": "24.08.08 ACE Inhibitors",
            "vietnam_essential_medicines": False,
            "international_guidelines": [
                {
                    "source": "EUROPA / PROGRESS Trials",
                    "recommendation": "Reduction of CV events in stable coronary artery disease and stroke prevention",
                    "context": "Stable CAD; prior stroke or TIA with hypertension",
                }
            ],
            "vn_guidelines": [],
            "clinical_tags": [
                "htn",
                "stable_coronary_disease",
                "stroke_prevention",
            ],
        },
        "availability_vietnam": {
            "status": "common",
            "level_of_care": ["district", "provincial", "central", "private"],
            "insurance_coverage": "bhyt_full",
            "brand_examples": ["Coversyl", "Perindopril STADA"],
            "notes": "Được sử dụng rộng rãi trong điều trị tăng huyết áp và phòng ngừa biến cố tim mạch.",
        },
    },

    # ======================== CARDIOVASCULAR – ARBs & MRA ========================
    "Losartan": {
        "guideline_tags": {
            "who_atc": "C09CA01",
            "ahfs_category": "24.08.06 Angiotensin II Receptor Blockers",
            "vietnam_essential_medicines": True,
            "international_guidelines": [
                {
                    "source": "ACC/AHA 2017 Hypertension Guideline",
                    "recommendation": "ARB as alternative first-line when ACE inhibitors not tolerated",
                    "context": "Primary hypertension, ACE inhibitor intolerance (e.g. cough, angioedema)",
                }
            ],
            "vn_guidelines": [
                {
                    "source": "BYT – Hướng dẫn chẩn đoán và điều trị tăng huyết áp 2020",
                    "recommendation": "Lựa chọn khi không dung nạp ACEI hoặc cần bảo vệ thận",
                    "context": "Tăng huyết áp có đái tháo đường hoặc bệnh thận mạn",
                }
            ],
            "clinical_tags": [
                "first_line_htn_alt_acei",
                "ckd_diabetic_nephropathy",
            ],
        },
        "availability_vietnam": {
            "status": "common",
            "level_of_care": ["district", "provincial", "central"],
            "insurance_coverage": "bhyt_full",
            "brand_examples": ["Losartan STADA", "Cozaar"],
            "notes": "Rất phổ biến; thường dùng cho tăng huyết áp có đái tháo đường hoặc bệnh thận mạn.",
        },
    },
    "Valsartan": {
        "guideline_tags": {
            "who_atc": "C09CA03",
            "ahfs_category": "24.08.06 Angiotensin II Receptor Blockers",
            "vietnam_essential_medicines": False,
            "international_guidelines": [
                {
                    "source": "ESC 2021 Heart Failure",
                    "recommendation": "ARB as alternative when ACEI not tolerated; part of ARNI when combined with sacubitril",
                    "context": "HFrEF patients unable to take ACEI, or ARNI where available",
                }
            ],
            "vn_guidelines": [],
            "clinical_tags": [
                "hfref_alt_acei",
                "htn",
            ],
        },
        "availability_vietnam": {
            "status": "common",
            "level_of_care": ["provincial", "central", "private"],
            "insurance_coverage": "bhyt_full",
            "brand_examples": ["Diovan", "Valsartan STADA"],
            "notes": "Được sử dụng rộng rãi, đặc biệt trong suy tim và tăng huyết áp kháng trị.",
        },
    },
    "Spironolactone": {
        "guideline_tags": {
            "who_atc": "C03DA01",
            "ahfs_category": "24.08.04 Aldosterone Antagonists",
            "vietnam_essential_medicines": True,
            "international_guidelines": [
                {
                    "source": "ESC 2021 Heart Failure",
                    "recommendation": "Mineralocorticoid receptor antagonist to reduce mortality",
                    "context": "HFrEF with persistent symptoms despite ACEI/ARB/ARNI and beta-blocker",
                }
            ],
            "vn_guidelines": [],
            "clinical_tags": [
                "hfref_mortality_benefit",
                "hyperaldosteronism",
            ],
        },
        "availability_vietnam": {
            "status": "common",
            "level_of_care": ["district", "provincial", "central"],
            "insurance_coverage": "bhyt_full",
            "brand_examples": ["Spironolactone STADA", "Aldactone"],
            "notes": "Sẵn có ở đa số bệnh viện; thường dùng trong suy tim, xơ gan cổ trướng, hội chứng cường aldosterone.",
        },
    },

    # ======================== DIABETES – METFORMIN & SGLT2 ========================
    "Metformin": {
        "guideline_tags": {
            "who_atc": "A10BA02",
            "ahfs_category": "68.20.08 Biguanides",
            "vietnam_essential_medicines": True,
            "international_guidelines": [
                {
                    "source": "ADA 2024 Standards of Care",
                    "recommendation": "Initial pharmacologic therapy for most adults with type 2 diabetes",
                    "context": "Type 2 diabetes without contraindications; often combined with lifestyle changes",
                }
            ],
            "vn_guidelines": [
                {
                    "source": "BYT – Hướng dẫn chẩn đoán và điều trị đái tháo đường typ 2",
                    "recommendation": "Thuốc đầu tay trong điều trị đái tháo đường typ 2 nếu không chống chỉ định",
                    "context": "ĐTĐ typ 2, không suy thận nặng hoặc chống chỉ định khác",
                }
            ],
            "clinical_tags": [
                "first_line_t2dm",
                "weight_neutral_or_loss",
                "low_hypoglycemia_risk",
            ],
        },
        "availability_vietnam": {
            "status": "common",
            "level_of_care": ["district", "provincial", "central", "private"],
            "insurance_coverage": "bhyt_full",
            "brand_examples": ["Metformin STADA", "Glucophage"],
            "notes": "Thuốc nền tảng trong điều trị ĐTĐ typ 2, rất dễ tiếp cận tại Việt Nam.",
        },
    },
    "Empagliflozin": {
        "guideline_tags": {
            "who_atc": "A10BK03",
            "ahfs_category": "68.20.32 Sodium-Glucose Co-Transporter 2 (SGLT2) Inhibitors",
            "vietnam_essential_medicines": False,
            "international_guidelines": [
                {
                    "source": "ADA 2024 Standards of Care",
                    "recommendation": "Preferred add-on in patients with ASCVD, HF, or CKD",
                    "context": "Type 2 diabetes with established ASCVD, HF, or CKD",
                },
                {
                    "source": "ESC 2021 Heart Failure",
                    "recommendation": "Core therapy for HFrEF regardless of diabetes",
                    "context": "Heart failure with reduced ejection fraction (HFrEF)",
                },
            ],
            "vn_guidelines": [],
            "clinical_tags": [
                "t2dm_with_ascvd",
                "hfref_mortality_benefit",
                "ckd_progression_slowing",
            ],
        },
        "availability_vietnam": {
            "status": "limited",
            "level_of_care": ["provincial", "central", "private"],
            "insurance_coverage": "bhyt_partial",
            "brand_examples": ["Jardiance"],
            "notes": "Thường có tại bệnh viện tuyến tỉnh/trung ương và phòng khám tư; chi phí cao hơn, BHYT chi trả một phần tuỳ hạng mục.",
        },
    },
    "Dapagliflozin": {
        "guideline_tags": {
            "who_atc": "A10BK01",
            "ahfs_category": "68.20.32 Sodium-Glucose Co-Transporter 2 (SGLT2) Inhibitors",
            "vietnam_essential_medicines": False,
            "international_guidelines": [
                {
                    "source": "ADA 2024 Standards of Care",
                    "recommendation": "Add-on therapy in patients with HF or CKD",
                    "context": "Type 2 diabetes with heart failure or CKD",
                },
                {
                    "source": "ESC 2021 Heart Failure",
                    "recommendation": "Core therapy for HFrEF, beneficial in HFpEF as well",
                    "context": "Heart failure (HFrEF/HFpEF), with or without diabetes",
                },
            ],
            "vn_guidelines": [],
            "clinical_tags": [
                "t2dm_with_hf",
                "hf_mortality_benefit",
                "ckd_progression_slowing",
            ],
        },
        "availability_vietnam": {
            "status": "limited",
            "level_of_care": ["provincial", "central", "private"],
            "insurance_coverage": "bhyt_partial",
            "brand_examples": ["Forxiga"],
            "notes": "Tương tự Empagliflozin, chủ yếu có ở tuyến trên và cơ sở tư nhân.",
        },
    },

    # ======================== DIABETES – INSULIN (GENERIC ENTRY) ========================
    "Insulin": {
        "guideline_tags": {
            "who_atc": "A10AB",
            "ahfs_category": "68.20.04 Insulins",
            "vietnam_essential_medicines": True,
            "international_guidelines": [
                {
                    "source": "ADA 2024 Standards of Care",
                    "recommendation": "Mandatory in type 1 diabetes; add-on in type 2 when oral therapy inadequate",
                    "context": "Type 1 diabetes; type 2 diabetes with severe hyperglycemia or catabolic symptoms",
                }
            ],
            "vn_guidelines": [
                {
                    "source": "BYT – Hướng dẫn chẩn đoán và điều trị đái tháo đường typ 1 và typ 2",
                    "recommendation": "Bắt buộc trong ĐTĐ typ 1; chỉ định khi ĐTĐ typ 2 không kiểm soát với thuốc uống",
                    "context": "ĐTĐ typ 1; ĐTĐ typ 2 thất bại điều trị bằng thuốc uống",
                }
            ],
            "clinical_tags": [
                "mandatory_t1dm",
                "add_on_t2dm_severe",
                "high_hypoglycemia_risk",
            ],
        },
        "availability_vietnam": {
            "status": "common",
            "level_of_care": ["district", "provincial", "central"],
            "insurance_coverage": "bhyt_full",
            "brand_examples": ["Insulin Mixtard", "Actrapid", "Lantus", "Levemir"],
            "notes": "Insulin nền và hỗn hợp có rộng rãi; một số analog mới có thể giới hạn tại bệnh viện tuyến trên.",
        },
    },

    # ======================== HEMATOLOGY – ANTICOAGULANTS ========================
    "Warfarin": {
        "guideline_tags": {
            "who_atc": "B01AA03",
            "ahfs_category": "20.12.04 Coumarin Anticoagulants",
            "vietnam_essential_medicines": True,
            "international_guidelines": [
                {
                    "source": "ESC 2020 Atrial Fibrillation Guideline",
                    "recommendation": "Alternative to DOACs when DOACs contraindicated or not available",
                    "context": "Non-valvular atrial fibrillation with CHA2DS2-VASc ≥2 in men / ≥3 in women",
                }
            ],
            "vn_guidelines": [],
            "clinical_tags": [
                "stroke_prevention_af",
                "vte_treatment",
                "mechanical_valve_mandatory",
            ],
        },
        "availability_vietnam": {
            "status": "common",
            "level_of_care": ["district", "provincial", "central"],
            "insurance_coverage": "bhyt_full",
            "brand_examples": ["Warfarin STADA", "Coumadin"],
            "notes": "Rất phổ biến; cần theo dõi INR chặt chẽ, thường gắn với phòng khám chống đông.",
        },
    },
    "Rivaroxaban": {
        "guideline_tags": {
            "who_atc": "B01AF01",
            "ahfs_category": "20.12.16 Direct Factor Xa Inhibitors",
            "vietnam_essential_medicines": False,
            "international_guidelines": [
                {
                    "source": "ESC 2020 Atrial Fibrillation Guideline",
                    "recommendation": "Preferred over VKAs in eligible non-valvular AF patients",
                    "context": "Non-valvular AF with CHA2DS2-VASc ≥2 in men / ≥3 in women",
                }
            ],
            "vn_guidelines": [],
            "clinical_tags": [
                "stroke_prevention_af",
                "vte_treatment",
            ],
        },
        "availability_vietnam": {
            "status": "limited",
            "level_of_care": ["provincial", "central", "private"],
            "insurance_coverage": "bhyt_partial",
            "brand_examples": ["Xarelto"],
            "notes": "Chi phí cao, chủ yếu dùng ở bệnh viện tuyến trên và cơ sở tư nhân; BHYT chi trả giới hạn.",
        },
    },
    "Apixaban": {
        "guideline_tags": {
            "who_atc": "B01AF02",
            "ahfs_category": "20.12.16 Direct Factor Xa Inhibitors",
            "vietnam_essential_medicines": False,
            "international_guidelines": [
                {
                    "source": "ESC 2020 Atrial Fibrillation Guideline",
                    "recommendation": "Preferred DOAC option with favorable bleeding profile",
                    "context": "Non-valvular AF; VTE treatment and secondary prevention",
                }
            ],
            "vn_guidelines": [],
            "clinical_tags": [
                "stroke_prevention_af",
                "vte_treatment",
                "lower_major_bleeding_risk",
            ],
        },
        "availability_vietnam": {
            "status": "limited",
            "level_of_care": ["provincial", "central", "private"],
            "insurance_coverage": "bhyt_partial",
            "brand_examples": ["Eliquis"],
            "notes": "Tương tự Rivaroxaban; thường được dùng khi cần ưu tiên an toàn chảy máu.",
        },
    },
    "Dabigatran": {
        "guideline_tags": {
            "who_atc": "B01AE07",
            "ahfs_category": "20.12.20 Direct Thrombin Inhibitors",
            "vietnam_essential_medicines": False,
            "international_guidelines": [
                {
                    "source": "ESC 2020 Atrial Fibrillation Guideline",
                    "recommendation": "DOAC alternative to VKAs for stroke prevention in AF",
                    "context": "Non-valvular AF; prevention of stroke and systemic embolism",
                }
            ],
            "vn_guidelines": [],
            "clinical_tags": [
                "stroke_prevention_af",
                "vte_treatment",
            ],
        },
        "availability_vietnam": {
            "status": "limited",
            "level_of_care": ["provincial", "central", "private"],
            "insurance_coverage": "bhyt_partial",
            "brand_examples": ["Pradaxa"],
            "notes": "Có mặt chủ yếu tại bệnh viện tuyến tỉnh/trung ương và một số cơ sở tư nhân.",
        },
    },
    "Enoxaparin": {
        "guideline_tags": {
            "who_atc": "B01AB05",
            "ahfs_category": "20.12.08 Low Molecular Weight Heparins",
            "vietnam_essential_medicines": True,
            "international_guidelines": [
                {
                    "source": "ESC / ACC Guidelines on ACS and VTE",
                    "recommendation": "Parenteral anticoagulant of choice in many ACS and VTE settings",
                    "context": "ACS management; treatment and prophylaxis of DVT/PE",
                }
            ],
            "vn_guidelines": [],
            "clinical_tags": [
                "vte_treatment",
                "vte_prophylaxis",
                "acs_management",
            ],
        },
        "availability_vietnam": {
            "status": "common",
            "level_of_care": ["district", "provincial", "central"],
            "insurance_coverage": "bhyt_full",
            "brand_examples": ["Clexane"],
            "notes": "Được dùng rộng rãi trong dự phòng và điều trị huyết khối; thường sẵn có tại các khoa nội và ngoại.",
        },
    },
})


EXTRA_ENHANCED_FIELDS.update({
    # ======================== EMERGENCY – VASOPRESSORS & ANTIARRHYTHMICS ========================
    "Epinephrine": {
        "availability_vietnam": {
            "status": "common",
            "level_of_care": ["district", "provincial", "central"],
            "insurance_coverage": "bhyt_full",
            "brand_examples": ["Adrenalin"],
            "notes": "Thuốc cấp cứu thiết yếu cho sốc phản vệ, ngừng tim; luôn có sẵn tại khoa cấp cứu và hồi sức.",
        },
    },
    "Norepinephrine": {
        "availability_vietnam": {
            "status": "common",
            "level_of_care": ["provincial", "central"],
            "insurance_coverage": "bhyt_full",
            "brand_examples": ["Norepinephrine Bitartrate"],
            "notes": "Dùng chủ yếu tại ICU/HSTC cho sốc nhiễm trùng và sốc khác; thường không có ở tuyến xã.",
        },
    },
    "Dopamine": {
        "availability_vietnam": {
            "status": "common",
            "level_of_care": ["district", "provincial", "central"],
            "insurance_coverage": "bhyt_full",
            "brand_examples": ["Dopamine hydrochloride"],
            "notes": "Vẫn được sử dụng ở nhiều bệnh viện, dù xu hướng hiện nay ưu tiên norepinephrine.",
        },
    },
    "Dobutamine": {
        "availability_vietnam": {
            "status": "common",
            "level_of_care": ["provincial", "central"],
            "insurance_coverage": "bhyt_full",
            "brand_examples": ["Dobutamine"],
            "notes": "Có sẵn tại ICU/HSTC cho suy tim cấp và sốc tim.",
        },
    },
    "Vasopressin": {
        "availability_vietnam": {
            "status": "limited",
            "level_of_care": ["provincial", "central"],
            "insurance_coverage": "bhyt_partial",
            "brand_examples": ["Vasopressin injection"],
            "notes": "Thường có tại khoa hồi sức tuyến cuối; dùng phối hợp trong sốc nặng kháng catecholamine.",
        },
    },
    "Adenosine": {
        "availability_vietnam": {
            "status": "common",
            "level_of_care": ["provincial", "central"],
            "insurance_coverage": "bhyt_full",
            "brand_examples": ["Adenocor"],
            "notes": "Thuốc cấp cứu loạn nhịp trên thất; thường có tại phòng cấp cứu, can thiệp tim mạch.",
        },
    },
    "Amiodarone": {
        "availability_vietnam": {
            "status": "common",
            "level_of_care": ["district", "provincial", "central"],
            "insurance_coverage": "bhyt_full",
            "brand_examples": ["Cordarone", "Amiodarone STADA"],
            "notes": "Rất phổ biến cho loạn nhịp thất và trên thất nặng; có cả dạng PO và IV.",
        },
    },
    "Lidocaine": {
        "availability_vietnam": {
            "status": "common",
            "level_of_care": ["district", "provincial", "central"],
            "insurance_coverage": "bhyt_full",
            "brand_examples": ["Lidocaine 2%", "Xylocaine"],
            "notes": "Luôn có cho gây tê tại chỗ; dạng IV dùng cho loạn nhịp thất thường có tại ICU/cấp cứu.",
        },
    },
    "Naloxone": {
        "availability_vietnam": {
            "status": "common",
            "level_of_care": ["district", "provincial", "central"],
            "insurance_coverage": "bhyt_full",
            "brand_examples": ["Naloxone injection"],
            "notes": "Thuốc cấp cứu quá liều opioid; nên có sẵn tại tất cả khoa cấp cứu và GMHS.",
        },
    },
    "Protamine": {
        "availability_vietnam": {
            "status": "common",
            "level_of_care": ["provincial", "central"],
            "insurance_coverage": "bhyt_full",
            "brand_examples": ["Protamine sulfate"],
            "notes": "Có tại phòng mổ, ICU, tim mạch can thiệp để đảo ngược heparin.",
        },
    },
    "Vitamin K": {
        "availability_vietnam": {
            "status": "common",
            "level_of_care": ["district", "provincial", "central"],
            "insurance_coverage": "bhyt_full",
            "brand_examples": ["Vitamin K1"],
            "notes": "Rộng rãi; dùng điều trị thiếu vitamin K và đảo ngược tác dụng warfarin.",
        },
    },

    # ======================== ANALGESICS – OPIOIDS & TRAMADOL ========================
    "Morphine": {
        "availability_vietnam": {
            "status": "common",
            "level_of_care": ["district", "provincial", "central"],
            "insurance_coverage": "bhyt_full",
            "brand_examples": ["Morphin sulphate"],
            "notes": "Thuốc gây nghiện được quản lý chặt chẽ; có ở khoa GMHS, ICU và điều trị đau.",
        },
    },
    "Fentanyl": {
        "availability_vietnam": {
            "status": "common",
            "level_of_care": ["provincial", "central"],
            "insurance_coverage": "bhyt_full",
            "brand_examples": ["Fentanyl citrate", "Durogesic patch"],
            "notes": "Dạng tiêm dùng trong GMHS và ICU; dạng miếng dán chủ yếu tại các đơn vị đau mạn tính/tuyến trên.",
        },
    },
    "Hydromorphone": {
        "availability_vietnam": {
            "status": "rare",
            "level_of_care": ["central", "private"],
            "insurance_coverage": "no_bhyt",
            "brand_examples": [],
            "notes": "Ít phổ biến; nếu có thường ở bệnh viện tuyến cuối hoặc cơ sở tư nhân chuyên sâu về giảm đau.",
        },
    },
    "Oxycodone": {
        "availability_vietnam": {
            "status": "limited",
            "level_of_care": ["central", "private"],
            "insurance_coverage": "bhyt_partial",
            "brand_examples": ["OxyContin"],
            "notes": "Có ở một số bệnh viện lớn cho điều trị đau ung thư; quản lý nghiêm ngặt như morphine.",
        },
    },
    "Codeine": {
        "availability_vietnam": {
            "status": "common",
            "level_of_care": ["district", "provincial", "central", "private"],
            "insurance_coverage": "bhyt_full",
            "brand_examples": ["Paracetamol-codeine combinations"],
            "notes": "Thường có trong các chế phẩm phối hợp giảm đau và ho; quản lý theo quy định với opioid yếu.",
        },
    },
    "Tramadol": {
        "availability_vietnam": {
            "status": "common",
            "level_of_care": ["district", "provincial", "central"],
            "insurance_coverage": "bhyt_full",
            "brand_examples": ["Tramadol STADA", "Tramal"],
            "notes": "Dùng rất phổ biến cho đau trung bình–nặng; cần lưu ý lạm dụng và tác dụng phụ thần kinh.",
        },
    },

    # ======================== ANTIBIOTICS – AMINOGLYCOSIDES & VANCOMYCIN ========================
    "Gentamicin": {
        "availability_vietnam": {
            "status": "common",
            "level_of_care": ["district", "provincial", "central"],
            "insurance_coverage": "bhyt_full",
            "brand_examples": ["Gentamicin injection"],
            "notes": "Kháng sinh kinh điển, chi phí rẻ; cần thận trọng độc tính thận và tai.",
        },
    },
    "Amikacin": {
        "availability_vietnam": {
            "status": "common",
            "level_of_care": ["district", "provincial", "central"],
            "insurance_coverage": "bhyt_full",
            "brand_examples": ["Amikacin injection"],
            "notes": "Thường dùng trong nhiễm khuẩn nặng Gram âm; thường có sẵn tại khoa hồi sức và nội.",
        },
    },
    "Tobramycin": {
        "availability_vietnam": {
            "status": "limited",
            "level_of_care": ["provincial", "central"],
            "insurance_coverage": "bhyt_full",
            "brand_examples": ["Tobramycin injection", "Nebulized formulations (tùy cơ sở)"],
            "notes": "Ít phổ biến hơn Gentamicin/Amikacin; một số trung tâm hô hấp dùng dạng hít cho bệnh nhân đặc biệt.",
        },
    },
    "Vancomycin": {
        "availability_vietnam": {
            "status": "common",
            "level_of_care": ["district", "provincial", "central"],
            "insurance_coverage": "bhyt_full",
            "brand_examples": ["Vancomycin injection"],
            "notes": "Kháng sinh quan trọng điều trị MRSA; thường yêu cầu hội chẩn nhiễm khuẩn và monitor chức năng thận.",
        },
    },
})


EXTRA_ENHANCED_FIELDS.update({
    # ======================== ONCOLOGY – CHEMO & IMMUNOSUPPRESSANTS ========================
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

    # ======================== NEUROLOGY – ANTICONVULSANTS & GABAPENTINOIDS ========================
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

    # ======================== RESPIRATORY – THEOPHYLLINE ========================
    "Theophylline": {
        "availability_vietnam": {
            "status": "common",
            "level_of_care": ["district", "provincial", "central"],
            "insurance_coverage": "bhyt_full",
            "brand_examples": ["Theophylline retard", "Aminophylline injection"],
            "notes": "Vẫn được sử dụng trong hen/COPD ở một số nơi; cần lưu ý khoảng điều trị hẹp và tương tác thuốc.",
        },
    },
})


EXTRA_ENHANCED_FIELDS.update({
    # ======================================================================
    # BỔ SUNG 8 FIELDS TÙY CHỌN CÒN THIẾU CHO 9 THUỐC ƯU TIÊN
    # ======================================================================
    # Lưu ý: nội dung ở mức an toàn/mặc định, có thể tinh chỉnh sau dựa trên guideline chi tiết.

    "Amikacin": {
        "drug_interactions": {
            "major": [],
            "moderate": [],
            "minor": [],
        },
        "contraindications": {
            "tuyệt_đối": [],
            "tương_đối": [],
        },
        "pregnancy_lactation": {
            "fda_category": "C",
            "pregnancy_details": "Chưa cập nhật chi tiết; tham khảo guideline và tài liệu nhà sản xuất trước khi dùng cho phụ nữ mang thai.",
            "lactation": {
                "safety": "Caution",
                "details": "Chưa rõ mức độ bài tiết vào sữa mẹ; cân nhắc lợi ích và nguy cơ.",
                "recommendation": "Tham khảo chuyên gia nhi/INF trước khi dùng kéo dài khi cho con bú.",
            },
        },
        "hepatic_adjustment": {
            "mild": "Không cần điều chỉnh đáng kể; chủ yếu thải trừ qua thận.",
            "moderate": "Không cần điều chỉnh đáng kể; theo dõi chức năng gan nếu dùng kéo dài.",
            "severe": "Thận trọng; ưu tiên điều chỉnh theo chức năng thận.",
            "notes": "Aminoglycoside chủ yếu thải qua thận; điều chỉnh liều dựa trên eGFR.",
        },
        "overdose_management": {
            "symptoms": [],
            "antidote": "Không có antidote đặc hiệu; điều trị hỗ trợ.",
            "treatment": [],
            "monitoring": "Theo dõi chức năng thận, thính lực và nồng độ thuốc (nếu có) trong trường hợp nghi ngờ quá liều hoặc tích luỹ.",
        },
        "reversal_agents": None,
        "administration_instructions": {
            "oral": {
                "with_food": "",
                "timing": "",
            },
            "iv": {
                "reconstitution": "Pha theo hướng dẫn nhà sản xuất; thường pha trong NaCl 0,9% hoặc D5W.",
                "infusion_rate": "Truyền chậm theo phác đồ; tránh bolus nhanh.",
                "compatibility": [],
                "incompatibility": [],
                "notes": "Theo dõi chức năng thận, nồng độ thuốc (nếu có điều kiện) để tránh độc tính.",
            },
        },
    },

    "Gentamicin": {
        "drug_interactions": {
            "major": [],
            "moderate": [],
            "minor": [],
        },
        "contraindications": {
            "tuyệt_đối": [],
            "tương_đối": [],
        },
        "pregnancy_lactation": {
            "fda_category": "C",
            "pregnancy_details": "Chưa cập nhật chi tiết; cân nhắc lợi ích/nguy cơ và tham khảo guideline khi dùng cho phụ nữ mang thai.",
            "lactation": {
                "safety": "Caution",
                "details": "Chưa rõ mức độ bài tiết vào sữa mẹ; nguy cơ toàn thân cho trẻ thường thấp do hấp thu kém qua đường tiêu hoá.",
                "recommendation": "Có thể dùng ngắn hạn với theo dõi thích hợp; tham khảo chuyên gia nếu dùng kéo dài.",
            },
        },
        "hepatic_adjustment": {
            "mild": "Không cần điều chỉnh đáng kể; chủ yếu thải trừ qua thận.",
            "moderate": "Không cần điều chỉnh đáng kể.",
            "severe": "Thận trọng; ưu tiên đánh giá và chỉnh liều theo chức năng thận.",
            "notes": "Điều chỉnh liều chủ yếu theo eGFR/CrCl; monitor nồng độ thuốc nếu có.",
        },
        "overdose_management": {
            "symptoms": [],
            "antidote": "Không có antidote đặc hiệu; điều trị hỗ trợ.",
            "treatment": [],
            "monitoring": "Theo dõi chức năng thận, thính lực, tiền đình và nồng độ thuốc trong trường hợp dùng liều cao/kéo dài.",
        },
        "reversal_agents": None,
        "administration_instructions": {
            "oral": {
                "with_food": "",
                "timing": "",
            },
            "iv": {
                "reconstitution": "Pha loãng trong NaCl 0,9% hoặc D5W theo khuyến cáo.",
                "infusion_rate": "Truyền chậm trong 30–60 phút (tuỳ phác đồ).",
                "compatibility": [],
                "incompatibility": [],
                "notes": "Không trộn chung cùng bơm tiêm với penicillin/beta-lactam khác; theo dõi chức năng thận.",
            },
        },
    },

    "Tobramycin": {
        "drug_interactions": {
            "major": [],
            "moderate": [],
            "minor": [],
        },
        "contraindications": {
            "tuyệt_đối": [],
            "tương_đối": [],
        },
        "pregnancy_lactation": {
            "fda_category": "C",
            "pregnancy_details": "Chưa cập nhật chi tiết; sử dụng khi lợi ích vượt trội nguy cơ và theo dõi sát.",
            "lactation": {
                "safety": "Caution",
                "details": "Hấp thu toàn thân thấp khi dùng dạng hít; cân nhắc nguy cơ/lợi ích.",
                "recommendation": "Tham khảo chuyên gia nếu dùng kéo dài ở phụ nữ đang cho con bú.",
            },
        },
        "hepatic_adjustment": {
            "mild": "Không cần điều chỉnh đáng kể.",
            "moderate": "Không cần điều chỉnh đáng kể.",
            "severe": "Thận trọng; ưu tiên điều chỉnh theo chức năng thận.",
            "notes": "Chủ yếu thải trừ qua thận; điều chỉnh theo eGFR.",
        },
        "overdose_management": {
            "symptoms": [],
            "antidote": "Không có antidote đặc hiệu; điều trị hỗ trợ.",
            "treatment": [],
            "monitoring": "Theo dõi chức năng thận, thính lực và nồng độ thuốc (nếu có) khi nghi ngờ tích luỹ/quá liều.",
        },
        "reversal_agents": None,
        "administration_instructions": {
            "oral": {
                "with_food": "",
                "timing": "",
            },
            "iv": {
                "reconstitution": "Pha loãng trong dung dịch truyền phù hợp (NaCl 0,9% hoặc D5W).",
                "infusion_rate": "Truyền chậm theo phác đồ; tránh bolus nhanh.",
                "compatibility": [],
                "incompatibility": [],
                "notes": "Có thể dùng dạng hít cho bệnh lý hô hấp mạn, tuỳ phác đồ từng cơ sở.",
            },
        },
    },

    "Dopamine": {
        "drug_interactions": {
            "major": [],
            "moderate": [],
            "minor": [],
        },
        "contraindications": {
            "tuyệt_đối": [],
            "tương_đối": [],
        },
        "pregnancy_lactation": {
            "fda_category": "C",
            "pregnancy_details": "Chưa cập nhật chi tiết; dùng trong bối cảnh cấp cứu khi lợi ích vượt trội nguy cơ.",
            "lactation": {
                "safety": "Caution",
                "details": "Thường dùng ngắn hạn trong ICU; dữ liệu cho con bú hạn chế.",
                "recommendation": "Không phải chỉ định điều trị kéo dài; tham khảo chuyên gia khi cần.",
            },
        },
        "hepatic_adjustment": {
            "mild": "Không cần điều chỉnh liều.",
            "moderate": "Không cần điều chỉnh liều.",
            "severe": "Thận trọng; ưu tiên chỉnh theo đáp ứng huyết động và chức năng cơ quan.",
            "notes": "Chủ yếu được chuyển hoá tại gan và thần kinh; dùng chủ yếu trong ICU với monitor liên tục.",
        },
        "overdose_management": {
            "symptoms": [],
            "antidote": "Không có antidote đặc hiệu; điều trị hỗ trợ.",
            "treatment": [],
            "monitoring": "Theo dõi huyết áp, nhịp tim, tưới máu ngoại vi, dấu hiệu thiếu máu cơ quan đích.",
        },
        "reversal_agents": None,
        "administration_instructions": {
            "oral": {
                "with_food": "",
                "timing": "",
            },
            "iv": {
                "reconstitution": "Pha trong NaCl 0,9% hoặc D5W; truyền qua bơm tiêm điện hoặc bơm truyền.",
                "infusion_rate": "Titration theo đáp ứng huyết áp và cung lượng tim.",
                "compatibility": [],
                "incompatibility": [],
                "notes": "Ưu tiên truyền qua đường tĩnh mạch trung tâm nếu dùng kéo dài; tránh thoát mạch.",
            },
        },
    },

    "Dobutamine": {
        "drug_interactions": {
            "major": [],
            "moderate": [],
            "minor": [],
        },
        "contraindications": {
            "tuyệt_đối": [],
            "tương_đối": [],
        },
        "pregnancy_lactation": {
            "fda_category": "C",
            "pregnancy_details": "Chưa cập nhật chi tiết; dùng trong bối cảnh cấp cứu tim mạch khi cần thiết.",
            "lactation": {
                "safety": "Caution",
                "details": "Dùng ngắn hạn trong ICU; dữ liệu an toàn khi cho con bú hạn chế.",
                "recommendation": "Không dùng kéo dài; đánh giá lợi ích/nguy cơ từng trường hợp.",
            },
        },
        "hepatic_adjustment": {
            "mild": "Không cần điều chỉnh liều.",
            "moderate": "Không cần điều chỉnh liều.",
            "severe": "Thận trọng; chỉnh liều theo đáp ứng lâm sàng.",
            "notes": "Chủ yếu dùng ngắn hạn trong ICU với monitor huyết động liên tục.",
        },
        "overdose_management": {
            "symptoms": [],
            "antidote": "Không có antidote đặc hiệu; điều trị hỗ trợ.",
            "treatment": [],
            "monitoring": "Theo dõi huyết áp, nhịp tim, dấu hiệu thiếu máu cơ tim hoặc loạn nhịp.",
        },
        "reversal_agents": None,
        "administration_instructions": {
            "oral": {
                "with_food": "",
                "timing": "",
            },
            "iv": {
                "reconstitution": "Pha trong dung dịch truyền thích hợp (NaCl 0,9%, D5W).",
                "infusion_rate": "Truyền liên tục với bơm tiêm điện; chỉnh liều theo cung lượng tim và huyết áp.",
                "compatibility": [],
                "incompatibility": [],
                "notes": "Theo dõi liên tục ECG, huyết áp và dấu hiệu suy tim.",
            },
        },
    },

    "Norepinephrine": {
        "drug_interactions": {
            "major": [],
            "moderate": [],
            "minor": [],
        },
        "contraindications": {
            "tuyệt_đối": [],
            "tương_đối": [],
        },
        "pregnancy_lactation": {
            "fda_category": "C",
            "pregnancy_details": "Dùng chủ yếu trong cấp cứu; cân nhắc lợi ích/nguy cơ cho mẹ và thai.",
            "lactation": {
                "safety": "Caution",
                "details": "Dùng ngắn hạn trong ICU; dữ liệu cho con bú rất hạn chế.",
                "recommendation": "Không dùng kéo dài; tham khảo chuyên gia khi cần.",
            },
        },
        "hepatic_adjustment": {
            "mild": "Không cần điều chỉnh liều.",
            "moderate": "Không cần điều chỉnh liều.",
            "severe": "Thận trọng; chỉnh liều theo đáp ứng huyết động.",
            "notes": "Truyền qua bơm tiêm điện với monitor liên tục; ưu tiên đường trung tâm.",
        },
        "overdose_management": {
            "symptoms": [],
            "antidote": "Không có antidote đặc hiệu; điều trị hỗ trợ.",
            "treatment": [],
            "monitoring": "Theo dõi huyết áp, tưới máu ngoại vi, tổn thương đầu chi và cơ quan đích khi dùng liều cao/kéo dài.",
        },
        "reversal_agents": None,
        "administration_instructions": {
            "oral": {
                "with_food": "",
                "timing": "",
            },
            "iv": {
                "reconstitution": "Pha trong NaCl 0,9% hoặc dung dịch thích hợp; truyền qua bơm tiêm điện.",
                "infusion_rate": "Titration theo MAP mục tiêu; thường truyền qua đường trung tâm.",
                "compatibility": [],
                "incompatibility": [],
                "notes": "Theo dõi chặt ECG, huyết áp xâm lấn (nếu có) và tưới máu ngoại vi.",
            },
        },
    },

    "Vasopressin": {
        "drug_interactions": {
            "major": [],
            "moderate": [],
            "minor": [],
        },
        "contraindications": {
            "tuyệt_đối": [],
            "tương_đối": [],
        },
        "pregnancy_lactation": {
            "fda_category": "C",
            "pregnancy_details": "Chưa cập nhật chi tiết; sử dụng chủ yếu trong bối cảnh cấp cứu sốc kháng catecholamine.",
            "lactation": {
                "safety": "Caution",
                "details": "Dữ liệu hạn chế; cân nhắc lợi ích/nguy cơ.",
                "recommendation": "Chỉ dùng trong ICU với thời gian ngắn.",
            },
        },
        "hepatic_adjustment": {
            "mild": "Không cần điều chỉnh liều riêng.",
            "moderate": "Không cần điều chỉnh liều riêng.",
            "severe": "Thận trọng; đánh giá toàn trạng huyết động và cơ quan đích.",
            "notes": "Thường dùng liều cố định nhỏ; monitor huyết áp và tưới máu.",
        },
        "overdose_management": {
            "symptoms": [],
            "antidote": "Không có antidote đặc hiệu; điều trị hỗ trợ.",
            "treatment": [],
            "monitoring": "Theo dõi huyết áp, natri máu, tưới máu chi và dấu hiệu thiếu máu ruột/cơ quan.",
        },
        "reversal_agents": None,
        "administration_instructions": {
            "oral": {
                "with_food": "",
                "timing": "",
            },
            "iv": {
                "reconstitution": "Pha trong dung dịch truyền phù hợp; truyền liên tục liều thấp.",
                "infusion_rate": "Tốc độ cố định hoặc titration nhỏ tuỳ phác đồ; thường dùng kèm norepinephrine.",
                "compatibility": [],
                "incompatibility": [],
                "notes": "Chỉ dùng tại ICU/HSTC với monitor huyết động chặt chẽ.",
            },
        },
    },

    "Valsartan": {
        "drug_interactions": {
            "major": [],
            "moderate": [],
            "minor": [],
        },
        "contraindications": {
            "tuyệt_đối": [],
            "tương_đối": [],
        },
        "pregnancy_lactation": {
            "fda_category": "D",
            "pregnancy_details": "Chống chỉ định trong thai kỳ do nguy cơ gây độc cho thai (giảm sản thận, thiểu ối, tử vong thai).",
            "lactation": {
                "safety": "Caution",
                "details": "Chưa có nhiều dữ liệu; nồng độ trong sữa mẹ có thể thấp nhưng cần thận trọng.",
                "recommendation": "Ưu tiên thuốc khác an toàn hơn khi cho con bú, đặc biệt với trẻ sơ sinh/nhũ nhi.",
            },
        },
        "hepatic_adjustment": {
            "mild": "Có thể không cần chỉnh liều.",
            "moderate": "Thận trọng, cân nhắc liều khởi đầu thấp hơn.",
            "severe": "Tránh dùng hoặc dùng rất thận trọng; tham khảo guideline chuyên khoa.",
            "notes": "Một phần chuyển hoá qua gan; cần lưu ý ở bệnh nhân suy gan rõ.",
        },
        "overdose_management": {
            "symptoms": [],
            "antidote": "Không có antidote đặc hiệu; điều trị hỗ trợ.",
            "treatment": [],
            "monitoring": "Theo dõi huyết áp, chức năng thận và kali máu trong trường hợp dùng liều cao/quá liều.",
        },
        "reversal_agents": None,
        "administration_instructions": {
            "oral": {
                "with_food": "Có thể uống cùng hoặc không cùng thức ăn.",
                "timing": "Uống 1–2 lần/ngày, cố định thời điểm trong ngày.",
            },
            "iv": {
                "reconstitution": "",
                "infusion_rate": "",
                "compatibility": [],
                "incompatibility": [],
                "notes": "Không có dạng tiêm tĩnh mạch thường quy.",
            },
        },
    },

    "Vancomycin": {
        "drug_interactions": {
            "major": [],
            "moderate": [],
            "minor": [],
        },
        "contraindications": {
            "tuyệt_đối": [],
            "tương_đối": [],
        },
        "pregnancy_lactation": {
            "fda_category": "B",
            "pregnancy_details": "Dữ liệu hạn chế; thường được xem là có thể chấp nhận khi cần thiết trong nhiễm trùng nặng.",
            "lactation": {
                "safety": "Compatible",
                "details": "Hấp thu qua đường tiêu hoá của trẻ kém; nồng độ toàn thân thấp.",
                "recommendation": "Thường chấp nhận được khi cho con bú, đặc biệt khi dùng đường IV; theo dõi nếu dùng kéo dài.",
            },
        },
        "hepatic_adjustment": {
            "mild": "Không cần điều chỉnh liều riêng.",
            "moderate": "Không cần điều chỉnh liều riêng.",
            "severe": "Thận trọng; điều chỉnh chủ yếu theo chức năng thận.",
            "notes": "Thải trừ chủ yếu qua thận; cần điều chỉnh liều theo eGFR và monitor nồng độ thuốc nếu có.",
        },
        "overdose_management": {
            "symptoms": [],
            "antidote": "Không có antidote đặc hiệu; điều trị hỗ trợ.",
            "treatment": [],
            "monitoring": "Theo dõi chức năng thận, nồng độ thuốc và dấu hiệu độc tính (ví dụ hội chứng đỏ da, độc tai).",
        },
        "reversal_agents": None,
        "administration_instructions": {
            "oral": {
                "with_food": "Có thể uống cùng hoặc không cùng thức ăn khi dùng điều trị C. difficile.",
                "timing": "Chia đều trong ngày theo phác đồ.",
            },
            "iv": {
                "reconstitution": "Pha theo hướng dẫn nhà sản xuất; truyền chậm để tránh phản ứng đỏ da.",
                "infusion_rate": "Thường truyền trong ≥60 phút (liều lớn có thể cần lâu hơn).",
                "compatibility": [],
                "incompatibility": [],
                "notes": "Monitor nồng độ đáy (trough) ở bệnh nhân nguy cơ cao hoặc dùng kéo dài.",
            },
        },
    },
})


__all__ = ["EXTRA_ENHANCED_FIELDS"]


