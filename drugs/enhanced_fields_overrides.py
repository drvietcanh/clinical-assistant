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

# ======================== BATCH 1: 30 DRUGS MISSING 2 FIELDS (Session 4) ========================
EXTRA_ENHANCED_FIELDS.update({
    "Ramipril": {
        "contraindications_detail": {
            "tuyệt_đối": ['Dị ứng ramipril hoặc các ACE inhibitor khác', 'Có thai (tất cả các tam cá nguyệt) - gây dị tật thai nhi', 'Hẹp động mạch thận 2 bên hoặc hẹp động mạch thận ở thận đơn độc', 'Phù mạch trước đây với ACE inhibitor'],
            "tương_đối": ['Suy thận nặng (CrCl <30) - cần giảm liều', 'Suy gan - thận trọng', 'Hẹp van động mạch chủ nặng', 'Tăng kali máu', 'Dùng với kali-sparing diuretics hoặc kali bổ sung'],
        },
        "reversal_agents": {
            "available": False,
            "agents": [],
            "notes": "Không có thuốc giải độc đặc hiệu; điều trị hỗ trợ triệu chứng.",
        },
    },
    "Perindopril": {
        "contraindications_detail": {
            "tuyệt_đối": ['Dị ứng perindopril hoặc các ACE inhibitor khác', 'Có thai (tất cả các tam cá nguyệt)', 'Hẹp động mạch thận 2 bên', 'Phù mạch trước đây với ACE inhibitor'],
            "tương_đối": ['Suy thận nặng (CrCl <30) - cần giảm liều', 'Suy gan - thận trọng', 'Tăng kali máu', 'Dùng với kali-sparing diuretics'],
        },
        "reversal_agents": {
            "available": False,
            "agents": [],
            "notes": "Không có thuốc giải độc đặc hiệu; điều trị hỗ trợ triệu chứng.",
        },
    },
    "Valsartan": {
        "contraindications_detail": {
            "tuyệt_đối": [],
            "tương_đối": [],
        },
        "reversal_agents": {
            "available": False,
            "agents": [],
            "notes": "Không có thuốc giải độc đặc hiệu; điều trị hỗ trợ triệu chứng.",
        },
    },
    "Metoprolol": {
        "contraindications_detail": {
            "tuyệt_đối": ['Hen phế quản nặng', 'Block nhĩ thất độ 2-3', 'Suy tim cấp không bù', 'Nhịp tim chậm nặng (<50 bpm)', 'Sốc tim', 'Hội chứng sick sinus (trừ khi có máy tạo nhịp)'],
            "tương_đối": ['COPD (thận trọng, có thể dùng liều thấp)', 'Đái tháo đường (che dấu triệu chứng hạ đường huyết)', 'Bệnh mạch máu ngoại biên (có thể làm nặng)', 'Suy gan (giảm chuyển hóa)', 'Dùng với verapamil/diltiazem (tăng nguy cơ block AV)'],
        },
        "renal_adjustment": {
            "normal": "Không đổi liều",
            "30_60": "Có thể cần giảm liều, theo dõi chức năng thận",
            "under_30": "Giảm liều hoặc tránh dùng nếu có lựa chọn khác",
            "hemodialysis": "Có thể cần bổ sung sau lọc máu (tùy thuốc)",
        },
    },
    "Nebivolol": {
        "black_box_warnings": None,
        "contraindications_detail": {
            "tuyệt_đối": ['Hen phế quản nặng - CHỐNG CHỈ ĐỊNH TUYỆT ĐỐI', 'Block nhĩ thất độ 2-3 - CHỐNG CHỈ ĐỊNH TUYỆT ĐỐI', 'Suy tim cấp không bù - CHỐNG CHỈ ĐỊNH TUYỆT ĐỐI', 'Nhịp tim chậm nặng (<60 bpm) - CHỐNG CHỈ ĐỊNH TUYỆT ĐỐI', 'Suy gan nặng - CHỐNG CHỈ ĐỊNH TUYỆT ĐỐI'],
            "tương_đối": ['Suy thận nặng (CrCl <30) - thận trọng, khởi đầu 2.5mg/ngày, tối đa 10mg/ngày', 'Suy thận trung bình (CrCl 30-60) - thận trọng, khởi đầu 2.5mg/ngày', 'COPD - thận trọng (selective beta-1, ít ảnh hưởng hơn non-selective)', 'Đái tháo đường - che dấu triệu chứng hạ đường huyết', 'Dùng với verapamil/diltiazem - tăng nguy cơ block nhĩ thất'],
        },
    },
    "Propranolol": {
        "contraindications_detail": {
            "tuyệt_đối": ['Hen phế quản', 'Suy tim cấp', 'Block nhĩ thất độ 2-3', 'Nhịp tim chậm nặng (<50 bpm)', 'Sốc tim', 'Hội chứng sick sinus (trừ khi có máy tạo nhịp)'],
            "tương_đối": ['COPD (thận trọng, có thể dùng liều thấp nhưng nguy cơ co thắt phế quản cao hơn)', 'Đái tháo đường (che dấu triệu chứng hạ đường huyết)', 'Bệnh mạch máu ngoại biên (có thể làm nặng)', 'Suy gan (giảm chuyển hóa, extensive first-pass)', 'Dùng với verapamil/diltiazem (tăng nguy cơ block AV)'],
        },
        "renal_adjustment": {
            "normal": "Không đổi liều",
            "30_60": "Có thể cần giảm liều, theo dõi chức năng thận",
            "under_30": "Giảm liều hoặc tránh dùng nếu có lựa chọn khác",
            "hemodialysis": "Có thể cần bổ sung sau lọc máu (tùy thuốc)",
        },
    },
    "Atorvastatin": {
        "contraindications_detail": {
            "tuyệt_đối": ['Bệnh gan hoạt động (active liver disease) - tăng men gan kéo dài, viêm gan', 'Có thai (pregnancy) - FDA category X, gây dị tật thai nhi', 'Cho con bú (lactation) - bài tiết vào sữa mẹ', 'Tiêu cơ vân đang hoạt động (active myopathy/rhabdomyolysis)', 'Dị ứng với atorvastatin hoặc bất kỳ thành phần nào', 'Dùng cùng cyclosporine, itraconazole, ketoconazole (tăng nguy cơ tiêu cơ vân nghiêm trọng)'],
            "tương_đối": ['Suy thận - thận trọng, giảm liều nếu cần', 'Suy gan - thận trọng, theo dõi men gan thường xuyên', 'Uống rượu nhiều - tăng nguy cơ viêm gan', 'Bệnh nhân Châu Á - tăng nồng độ atorvastatin, có thể cần liều thấp hơn', 'Người cao tuổi - tăng nguy cơ đau cơ, tiêu cơ vân', 'Đái tháo đường - statins có thể tăng đường huyết nhẹ', 'Bệnh tuyến giáp - tăng nguy cơ đau cơ', 'Dùng cùng thuốc ức chế CYP3A4 - giảm liều atorvastatin'],
        },
        "renal_adjustment": {
            "normal": "Không đổi liều",
            "30_60": "Có thể cần giảm liều, theo dõi chức năng thận",
            "under_30": "Giảm liều hoặc tránh dùng nếu có lựa chọn khác",
            "hemodialysis": "Có thể cần bổ sung sau lọc máu (tùy thuốc)",
        },
    },
    "Simvastatin": {
        "contraindications_detail": {
            "tuyệt_đối": ['Bệnh gan hoạt động (active liver disease) - tăng men gan kéo dài, viêm gan', 'Có thai (pregnancy) - FDA category X, gây dị tật thai nhi', 'Cho con bú (lactation) - bài tiết vào sữa mẹ', 'Tiêu cơ vân đang hoạt động (active myopathy/rhabdomyolysis)', 'Dị ứng với simvastatin hoặc bất kỳ thành phần nào', 'Dùng cùng cyclosporine, itraconazole, ketoconazole (tăng nguy cơ tiêu cơ vân nghiêm trọng)', 'Dùng grapefruit juice'],
            "tương_đối": ['Suy thận - thận trọng, giảm liều nếu cần', 'Suy gan - thận trọng, theo dõi men gan thường xuyên', 'Uống rượu nhiều - tăng nguy cơ viêm gan', 'Người cao tuổi - tăng nguy cơ đau cơ, tiêu cơ vân', 'Đái tháo đường - statins có thể tăng đường huyết nhẹ', 'Bệnh tuyến giáp - tăng nguy cơ đau cơ', 'Dùng cùng thuốc ức chế CYP3A4 - giảm liều simvastatin', 'Liều cao (>40mg/ngày) - tăng nguy cơ tiêu cơ vân'],
        },
        "renal_adjustment": {
            "normal": "Không đổi liều",
            "30_60": "Có thể cần giảm liều, theo dõi chức năng thận",
            "under_30": "Giảm liều hoặc tránh dùng nếu có lựa chọn khác",
            "hemodialysis": "Có thể cần bổ sung sau lọc máu (tùy thuốc)",
        },
    },
    "Pravastatin": {
        "contraindications_detail": {
            "tuyệt_đối": ['Bệnh gan hoạt động', 'Có thai', 'Cho con bú', 'Tiêu cơ vân đang hoạt động'],
            "tương_đối": ['Suy thận nặng - cần điều chỉnh liều', 'Dùng với cyclosporine - giảm liều', 'Dùng với gemfibrozil - tránh dùng chung'],
        },
        "renal_adjustment": {
            "normal": "Không đổi liều",
            "30_60": "Có thể cần giảm liều, theo dõi chức năng thận",
            "under_30": "Giảm liều hoặc tránh dùng nếu có lựa chọn khác",
            "hemodialysis": "Có thể cần bổ sung sau lọc máu (tùy thuốc)",
        },
    },
    "Fluvastatin": {
        "contraindications_detail": {
            "tuyệt_đối": ['Bệnh gan hoạt động', 'Có thai', 'Cho con bú', 'Tiêu cơ vân đang hoạt động'],
            "tương_đối": ['Suy thận nặng - thận trọng', 'Dùng với cyclosporine - giảm liều', 'Dùng với gemfibrozil - tránh dùng chung'],
        },
        "renal_adjustment": {
            "normal": "Không đổi liều",
            "30_60": "Có thể cần giảm liều, theo dõi chức năng thận",
            "under_30": "Giảm liều hoặc tránh dùng nếu có lựa chọn khác",
            "hemodialysis": "Có thể cần bổ sung sau lọc máu (tùy thuốc)",
        },
    },
    "Pitavastatin": {
        "contraindications_detail": {
            "tuyệt_đối": ['Bệnh gan hoạt động', 'Có thai', 'Cho con bú', 'Tiêu cơ vân đang hoạt động'],
            "tương_đối": ['Suy thận nặng - thận trọng', 'Dùng với cyclosporine - giảm liều tối đa 1mg/ngày', 'Dùng với gemfibrozil - tránh dùng chung'],
        },
        "renal_adjustment": {
            "normal": "Không đổi liều",
            "30_60": "Có thể cần giảm liều, theo dõi chức năng thận",
            "under_30": "Giảm liều hoặc tránh dùng nếu có lựa chọn khác",
            "hemodialysis": "Có thể cần bổ sung sau lọc máu (tùy thuốc)",
        },
    },
    "Ezetimibe": {
        "black_box_warnings": None,
        "contraindications_detail": {
            "tuyệt_đối": ['Dị ứng ezetimibe'],
            "tương_đối": ['Bệnh gan hoạt động (khi dùng với statin) - chống chỉ định statin, nhưng có thể dùng ezetimibe đơn trị', 'Có thai (khi dùng với statin) - statin chống chỉ định trong thai kỳ', 'Dùng với cyclosporine - giảm liều ezetimibe xuống 5mg/ngày', 'Dùng với fibrates - tăng nguy cơ sỏi mật'],
        },
    },
    "Amiodarone": {
        "contraindications_detail": {
            "tuyệt_đối": ['Block nhĩ thất độ 2-3 không có máy tạo nhịp', 'Rối loạn chức năng tuyến giáp không kiểm soát được', 'Bệnh phổi mạn tính nặng (COPD, ILD)', 'Bệnh gan nặng (Child-Pugh C)', 'Có thai (category D)', 'Hạ K+ hoặc Mg2+ nặng (tăng nguy cơ torsades de pointes)'],
            "tương_đối": ['Suy thận nặng (thận trọng, theo dõi chức năng thận)', 'Nhịp tim chậm (tăng nguy cơ block AV)', 'Bệnh phổi nhẹ (theo dõi chức năng phổi chặt chẽ)', 'Rối loạn chức năng tuyến giáp nhẹ (theo dõi TSH chặt chẽ)', 'Đang dùng warfarin hoặc digoxin (cần giảm liều)'],
        },
        "renal_adjustment": {
            "normal": "Không đổi liều",
            "30_60": "Có thể cần giảm liều, theo dõi chức năng thận",
            "under_30": "Giảm liều hoặc tránh dùng nếu có lựa chọn khác",
            "hemodialysis": "Có thể cần bổ sung sau lọc máu (tùy thuốc)",
        },
    },
    "Flecainide": {
        "contraindications_detail": {
            "tuyệt_đối": ['Bệnh tim cấu trúc (suy tim, bệnh mạch vành, bệnh van tim)', 'Block nhĩ thất độ 2-3', 'Hội chứng Brugada', 'QT kéo dài', 'Suy thận nặng (CrCl <30)'],
            "tương_đối": ['Suy thận (CrCl 30-50) - giảm liều 25-50%', 'Block nhĩ thất độ 1 - có thể làm nặng block', 'Dùng với amiodarone - tăng nồng độ flecainide', 'Dùng với beta-blockers, verapamil, diltiazem - tăng nguy cơ block AV'],
        },
        "renal_adjustment": {
            "normal": "Không đổi liều",
            "30_60": "Có thể cần giảm liều, theo dõi chức năng thận",
            "under_30": "Giảm liều hoặc tránh dùng nếu có lựa chọn khác",
            "hemodialysis": "Có thể cần bổ sung sau lọc máu (tùy thuốc)",
        },
    },
    "Propafenone": {
        "contraindications_detail": {
            "tuyệt_đối": ['Bệnh tim cấu trúc (suy tim, bệnh mạch vành, bệnh van tim)', 'Block nhĩ thất độ 2-3', 'Hội chứng Brugada', 'QT kéo dài', 'Suy gan nặng', 'Suy thận nặng (CrCl <30)'],
            "tương_đối": ['Suy gan - giảm liều 25-50%', 'Suy thận (CrCl 30-50) - giảm liều 25-50%', 'Block nhĩ thất độ 1 - có thể làm nặng block', 'Dùng với amiodarone - tăng nồng độ propafenone', 'Dùng với beta-blockers - tăng nguy cơ block AV'],
        },
        "renal_adjustment": {
            "normal": "Không đổi liều",
            "30_60": "Có thể cần giảm liều, theo dõi chức năng thận",
            "under_30": "Giảm liều hoặc tránh dùng nếu có lựa chọn khác",
            "hemodialysis": "Có thể cần bổ sung sau lọc máu (tùy thuốc)",
        },
    },
    "Dronedarone": {
        "contraindications_detail": {
            "tuyệt_đối": ['Suy tim nặng (NYHA class IV) hoặc suy tim không ổn định - CHỐNG CHỈ ĐỊNH (tăng nguy cơ tử vong)', 'Bệnh gan nặng - CHỐNG CHỈ ĐỊNH', 'Block nhĩ thất độ 2-3 không có máy tạo nhịp', 'Nhịp chậm <50 bpm', 'QT prolongation nặng', 'Dùng với CYP3A4 inhibitors mạnh'],
            "tương_đối": ['Suy tim nhẹ đến trung bình (NYHA class I-III) - thận trọng', 'Suy gan nhẹ đến trung bình - thận trọng, theo dõi chặt chẽ', 'Suy thận - tăng creatinine có thể xảy ra (không phải suy thận thực sự)', 'Dùng với digoxin - giảm liều digoxin 50%', 'Dùng với warfarin - theo dõi INR'],
        },
        "renal_adjustment": {
            "normal": "Không đổi liều",
            "30_60": "Có thể cần giảm liều, theo dõi chức năng thận",
            "under_30": "Giảm liều hoặc tránh dùng nếu có lựa chọn khác",
            "hemodialysis": "Có thể cần bổ sung sau lọc máu (tùy thuốc)",
        },
    },
    "Procainamide": {
        "contraindications_detail": {
            "tuyệt_đối": ['Dị ứng procainamide', 'Block nhĩ thất độ 2-3 không có máy tạo nhịp', 'Suy tim nặng', 'Lupus ban đỏ hệ thống đang hoạt động'],
            "tương_đối": ['Suy thận nặng - NAPA tích lũy, giảm liều', 'Suy gan nặng - thận trọng', 'Block nhĩ thất độ 1 - thận trọng', 'QT prolongation - tăng nguy cơ rối loạn nhịp tim'],
        },
        "renal_adjustment": {
            "normal": "Không đổi liều",
            "30_60": "Có thể cần giảm liều, theo dõi chức năng thận",
            "under_30": "Giảm liều hoặc tránh dùng nếu có lựa chọn khác",
            "hemodialysis": "Có thể cần bổ sung sau lọc máu (tùy thuốc)",
        },
    },
    "Adenosine": {
        "black_box_warnings": None,
        "contraindications_detail": {
            "tuyệt_đối": ['Block nhĩ thất độ 2-3 (AV block) không có máy tạo nhịp', 'Hội chứng sick sinus (sick sinus syndrome) không có máy tạo nhịp', 'Hen phế quản nặng hoặc co thắt phế quản nặng', 'Dị ứng adenosine', 'Rung nhĩ/rung thất (không phải chỉ định)'],
            "tương_đối": ['Block AV độ 1 - thận trọng, có thể làm nặng', 'Hen phế quản nhẹ đến trung bình - thận trọng, có thể gây co thắt phế quản', 'Suy tim - thận trọng, có thể gây ngừng tim kéo dài', 'Suy thận nặng - không cần điều chỉnh liều nhưng thận trọng', 'Dùng với dipyridamole - giảm liều 50-75%', 'Dùng với theophylline/caffeine - có thể không hiệu quả', 'Nhịp tim chậm (<50 bpm) - thận trọng, có thể gây ngừng tim'],
        },
    },
    "Ibutilide": {
        "contraindications_detail": {
            "tuyệt_đối": ['Dị ứng ibutilide', 'QT kéo dài (QTc >440ms) - CHỐNG CHỈ ĐỊNH', 'Torsades de pointes - CHỐNG CHỈ ĐỊNH', 'Hạ kali máu, hạ magie máu - CHỐNG CHỈ ĐỊNH (phải điều chỉnh trước)', 'Dùng với thuốc kéo dài QT - CHỐNG CHỈ ĐỊNH'],
            "tương_đối": ['Suy tim nặng - thận trọng', 'Dùng với digoxin - tăng nguy cơ rối loạn nhịp tim', 'Dùng với beta-blockers - tăng nguy cơ nhịp tim chậm'],
        },
        "renal_adjustment": {
            "normal": "Không đổi liều",
            "30_60": "Có thể cần giảm liều, theo dõi chức năng thận",
            "under_30": "Giảm liều hoặc tránh dùng nếu có lựa chọn khác",
            "hemodialysis": "Có thể cần bổ sung sau lọc máu (tùy thuốc)",
        },
    },
    "Amlodipine": {
        "contraindications_detail": {
            "tuyệt_đối": ['Dị ứng amlodipine hoặc dihydropyridine calcium channel blockers', 'Sốc tim', 'Suy tim mất bù nặng (NYHA class IV)'],
            "tương_đối": ['Hẹp van động mạch chủ nặng - có thể gây suy tim', 'Suy gan - giảm chuyển hóa, tăng nồng độ', 'Suy tim nhẹ đến trung bình - thận trọng', 'Phù ngoại biên - tác dụng phụ thường gặp nhưng không nguy hiểm'],
        },
        "renal_adjustment": {
            "normal": "Không đổi liều",
            "30_60": "Có thể cần giảm liều, theo dõi chức năng thận",
            "under_30": "Giảm liều hoặc tránh dùng nếu có lựa chọn khác",
            "hemodialysis": "Có thể cần bổ sung sau lọc máu (tùy thuốc)",
        },
    },
    "Furosemide": {
        "contraindications_detail": {
            "tuyệt_đối": ['Vô niệu', 'Mất nước nặng', 'Hạ kali máu nặng', 'Dị ứng sulfonamide', 'Dị ứng furosemide'],
            "tương_đối": ['Suy thận nặng - có thể cần liều cao hơn (nhưng thận trọng với IV liều cao - nguy cơ điếc)', 'Suy gan nặng - thận trọng (thải một phần qua gan)', 'Hạ natri máu - điều chỉnh trước khi dùng', 'Hạ magie máu - bù magie trước khi dùng', 'Dùng với digoxin - tăng nguy cơ ngộ độc digoxin', 'Dùng với aminoglycosides - tăng nguy cơ điếc', 'Dùng với lithium - tăng nồng độ lithium'],
        },
        "renal_adjustment": {
            "normal": "Không đổi liều",
            "30_60": "Có thể cần giảm liều, theo dõi chức năng thận",
            "under_30": "Giảm liều hoặc tránh dùng nếu có lựa chọn khác",
            "hemodialysis": "Có thể cần bổ sung sau lọc máu (tùy thuốc)",
        },
    },
    "Bumetanide": {
        "contraindications_detail": {
            "tuyệt_đối": ['Vô niệu', 'Mất nước nặng', 'Hạ kali máu nặng', 'Dị ứng sulfonamide'],
            "tương_đối": ['Suy thận nặng - có thể cần liều cao hơn nhưng thận trọng', 'Suy gan nặng - thận trọng', 'Đang dùng digoxin - tăng nguy cơ ngộ độc digoxin'],
        },
        "renal_adjustment": {
            "normal": "Không đổi liều",
            "30_60": "Có thể cần giảm liều, theo dõi chức năng thận",
            "under_30": "Giảm liều hoặc tránh dùng nếu có lựa chọn khác",
            "hemodialysis": "Có thể cần bổ sung sau lọc máu (tùy thuốc)",
        },
    },
    "Torsemide": {
        "contraindications_detail": {
            "tuyệt_đối": ['Vô niệu', 'Mất nước nặng', 'Hạ kali máu nặng', 'Dị ứng sulfonamide'],
            "tương_đối": ['Suy thận nặng - có thể cần liều cao hơn nhưng thận trọng', 'Suy gan nặng - thận trọng', 'Đang dùng digoxin - tăng nguy cơ ngộ độc digoxin'],
        },
        "renal_adjustment": {
            "normal": "Không đổi liều",
            "30_60": "Có thể cần giảm liều, theo dõi chức năng thận",
            "under_30": "Giảm liều hoặc tránh dùng nếu có lựa chọn khác",
            "hemodialysis": "Có thể cần bổ sung sau lọc máu (tùy thuốc)",
        },
    },
    "Chlorthalidone": {
        "contraindications_detail": {
            "tuyệt_đối": ['Dị ứng chlorthalidone hoặc sulfonamide', 'Vô niệu', 'Hạ kali máu nặng không kiểm soát', 'Suy gan nặng'],
            "tương_đối": ['Suy thận (CrCl <30) - giảm hiệu quả, tăng nguy cơ tác dụng phụ', 'Hạ kali máu - có thể làm nặng', 'Hạ natri máu - có thể làm nặng', 'Đái tháo đường - có thể tăng đường huyết', 'Gout - có thể tăng acid uric, gây cơn gout', 'Người cao tuổi - tăng nguy cơ hạ natri máu, té ngã', 'Dùng với digoxin - tăng nguy cơ ngộ độc digoxin', 'Dùng với lithium - tăng nguy cơ độc tính lithium'],
        },
        "renal_adjustment": {
            "normal": "Không đổi liều",
            "30_60": "Có thể cần giảm liều, theo dõi chức năng thận",
            "under_30": "Giảm liều hoặc tránh dùng nếu có lựa chọn khác",
            "hemodialysis": "Có thể cần bổ sung sau lọc máu (tùy thuốc)",
        },
    },
    "Warfarin": {
        "contraindications_detail": {
            "tuyệt_đối": ['Chảy máu đang hoạt động', 'Có thai (3 tháng đầu và cuối - category X)', 'Bệnh gan nặng (Child-Pugh C)', 'Thiếu protein C hoặc S bẩm sinh (tăng nguy cơ hoại tử da)', 'Không tuân thủ điều trị'],
            "tương_đối": ['Bệnh gan nhẹ-trung bình (thận trọng, theo dõi chức năng gan)', 'Suy thận nặng (thận trọng)', 'Người già (>75 tuổi - tăng nguy cơ chảy máu)', 'Tiền sử loét dạ dày tá tràng (tăng nguy cơ chảy máu)', 'Đang dùng aspirin/NSAIDs (tăng nguy cơ chảy máu)', 'Rối loạn đông máu (hemophilia, von Willebrand disease)'],
        },
        "renal_adjustment": {
            "normal": "Không đổi liều",
            "30_60": "Có thể cần giảm liều, theo dõi chức năng thận",
            "under_30": "Giảm liều hoặc tránh dùng nếu có lựa chọn khác",
            "hemodialysis": "Có thể cần bổ sung sau lọc máu (tùy thuốc)",
        },
    },
    "Clopidogrel": {
        "contraindications_detail": {
            "tuyệt_đối": ['Chảy máu đang hoạt động', 'Xuất huyết nội sọ đang hoạt động', 'Dị ứng clopidogrel'],
            "tương_đối": ['Nguy cơ chảy máu cao (loét dạ dày, xuất huyết gần đây) - thận trọng', 'Suy gan nặng - thận trọng', 'Suy thận nặng - thận trọng', 'Phẫu thuật lớn - cần ngừng trước phẫu thuật', 'Poor metabolizers CYP2C19 - có thể giảm đáp ứng, cân nhắc dùng prasugrel/ticagrelor'],
        },
        "renal_adjustment": {
            "normal": "Không đổi liều",
            "30_60": "Có thể cần giảm liều, theo dõi chức năng thận",
            "under_30": "Giảm liều hoặc tránh dùng nếu có lựa chọn khác",
            "hemodialysis": "Có thể cần bổ sung sau lọc máu (tùy thuốc)",
        },
    },
    "Ticagrelor": {
        "contraindications_detail": {
            "tuyệt_đối": ['Chảy máu đang hoạt động', 'Xuất huyết nội sọ đang hoạt động', 'Dị ứng ticagrelor', 'Dùng strong CYP3A4 inhibitors (ketoconazole, itraconazole, clarithromycin, ritonavir)'],
            "tương_đối": ['Suy gan nặng - chống chỉ định', 'Nguy cơ chảy máu cao (loét dạ dày, xuất huyết gần đây) - thận trọng', 'Tiền sử nhịp tim chậm hoặc block nhĩ thất - tăng nguy cơ bradycardia', 'Suy thận nặng - thận trọng', 'Phẫu thuật lớn - cần ngừng trước phẫu thuật'],
        },
        "renal_adjustment": {
            "normal": "Không đổi liều",
            "30_60": "Có thể cần giảm liều, theo dõi chức năng thận",
            "under_30": "Giảm liều hoặc tránh dùng nếu có lựa chọn khác",
            "hemodialysis": "Có thể cần bổ sung sau lọc máu (tùy thuốc)",
        },
    },
    "Prasugrel": {
        "contraindications_detail": {
            "tuyệt_đối": ['Chảy máu đang hoạt động', 'Tiền sử TIA hoặc đột quỵ', 'Dị ứng prasugrel'],
            "tương_đối": ['Tuổi ≥75 (trừ nguy cơ cao) - tăng nguy cơ chảy máu, cân nhắc liều 5mg/ngày', 'Cân nặng <60kg (trừ nguy cơ cao) - tăng nguy cơ chảy máu, cân nhắc liều 5mg/ngày', 'Nguy cơ chảy máu cao (loét dạ dày, xuất huyết gần đây) - thận trọng', 'Phẫu thuật lớn - cần ngừng trước phẫu thuật', 'Suy gan nặng - thận trọng', 'Suy thận nặng - thận trọng'],
        },
        "renal_adjustment": {
            "normal": "Không đổi liều",
            "30_60": "Có thể cần giảm liều, theo dõi chức năng thận",
            "under_30": "Giảm liều hoặc tránh dùng nếu có lựa chọn khác",
            "hemodialysis": "Có thể cần bổ sung sau lọc máu (tùy thuốc)",
        },
    },
    "Enoxaparin": {
        "contraindications_detail": {
            "tuyệt_đối": ['Chảy máu đang hoạt động', 'Giảm tiểu cầu do heparin (HIT) đang hoạt động hoặc tiền sử', 'Dị ứng heparin/enoxaparin'],
            "tương_đối": ['Suy thận nặng (CrCl <30) - giảm liều hoặc dùng UFH thay thế', 'Nguy cơ chảy máu cao (loét dạ dày, xuất huyết gần đây) - thận trọng', 'Phẫu thuật lớn - cần ngừng trước phẫu thuật', 'Có thai - tương đối an toàn nhưng thận trọng'],
        },
        "renal_adjustment": {
            "normal": "Không đổi liều",
            "30_60": "Có thể cần giảm liều, theo dõi chức năng thận",
            "under_30": "Giảm liều hoặc tránh dùng nếu có lựa chọn khác",
            "hemodialysis": "Có thể cần bổ sung sau lọc máu (tùy thuốc)",
        },
    },
    "Rivaroxaban": {
        "contraindications_detail": {
            "tuyệt_đối": ['Chảy máu đang hoạt động', 'Suy thận nặng (CrCl <15) - chống chỉ định', 'Dị ứng rivaroxaban', 'Dùng CYP3A4 và P-gp inhibitors mạnh (ketoconazole, ritonavir)'],
            "tương_đối": ['Suy thận (CrCl 15-50) - giảm liều (15mg x 1 lần/ngày cho AFib)', 'Nguy cơ chảy máu cao (loét dạ dày, xuất huyết gần đây) - thận trọng', 'Phẫu thuật lớn - cần ngừng trước phẫu thuật', 'Có thai - tránh dùng'],
        },
        "renal_adjustment": {
            "normal": "Không đổi liều",
            "30_60": "Có thể cần giảm liều, theo dõi chức năng thận",
            "under_30": "Giảm liều hoặc tránh dùng nếu có lựa chọn khác",
            "hemodialysis": "Có thể cần bổ sung sau lọc máu (tùy thuốc)",
        },
    },
})
# ======================== END BATCH 1 ========================

# ======================== BATCH 2: 30 DRUGS (31-60) ========================
EXTRA_ENHANCED_FIELDS.update({
    "Apixaban": {
        "contraindications_detail": {
            "tuyệt_đối": ['Chảy máu đang hoạt động', 'Suy thận nặng (CrCl <15) - chống chỉ định', 'Dị ứng apixaban', 'Dùng CYP3A4 và P-gp inhibitors mạnh (ketoconazole, ritonavir)'],
            "tương_đối": ['Suy thận (CrCl 15-30) - thận trọng, có thể cần giảm liều', 'Nguy cơ chảy máu cao (loét dạ dày, xuất huyết gần đây) - thận trọng', 'Phẫu thuật lớn - cần ngừng trước phẫu thuật', 'Có thai - tránh dùng'],
        },
        "renal_adjustment": {
            "normal": "Không đổi liều",
            "30_60": "Có thể cần giảm liều, theo dõi chức năng thận",
            "under_30": "Giảm liều hoặc tránh dùng nếu có lựa chọn khác",
            "hemodialysis": "Có thể cần bổ sung sau lọc máu (tùy thuốc)",
        },
    },
    "Dabigatran": {
        "contraindications_detail": {
            "tuyệt_đối": ['Chảy máu đang hoạt động', 'Suy thận nặng (CrCl <30) - chống chỉ định', 'Dị ứng dabigatran', 'Dùng P-gp inhibitors mạnh (ketoconazole, dronedarone)'],
            "tương_đối": ['Suy thận (CrCl 30-50) - giảm liều (110mg x 2 lần/ngày)', 'Nguy cơ chảy máu cao (loét dạ dày, xuất huyết gần đây) - thận trọng', 'Phẫu thuật lớn - cần ngừng trước phẫu thuật', 'Có thai - tránh dùng'],
        },
        "renal_adjustment": {
            "normal": "Không đổi liều",
            "30_60": "Có thể cần giảm liều, theo dõi chức năng thận",
            "under_30": "Giảm liều hoặc tránh dùng nếu có lựa chọn khác",
            "hemodialysis": "Có thể cần bổ sung sau lọc máu (tùy thuốc)",
        },
    },
    "Edoxaban": {
        "contraindications_detail": {
            "tuyệt_đối": ['Chảy máu đang hoạt động', 'Suy thận nặng (CrCl <15) - chống chỉ định', 'Dị ứng edoxaban'],
            "tương_đối": ['Suy thận (CrCl 15-50) - giảm liều xuống 30mg x 1 lần/ngày', 'Cân nặng ≤60kg - giảm liều xuống 30mg x 1 lần/ngày', 'Nguy cơ chảy máu cao (loét dạ dày, xuất huyết gần đây) - thận trọng', 'Phẫu thuật lớn - cần ngừng trước phẫu thuật', 'Có thai - tránh dùng'],
        },
        "renal_adjustment": {
            "normal": "Không đổi liều",
            "30_60": "Có thể cần giảm liều, theo dõi chức năng thận",
            "under_30": "Giảm liều hoặc tránh dùng nếu có lựa chọn khác",
            "hemodialysis": "Có thể cần bổ sung sau lọc máu (tùy thuốc)",
        },
    },
    "Alirocumab": {
        "contraindications_detail": {
            "tuyệt_đối": ['Dị ứng với alirocumab hoặc bất kỳ thành phần nào', 'Dị ứng với protein tái tổ hợp'],
            "tương_đối": ['Suy gan nặng - chưa có dữ liệu đầy đủ', 'Suy thận nặng - không cần chỉnh liều nhưng thận trọng'],
        },
        "renal_adjustment": {
            "normal": "Không đổi liều",
            "30_60": "Có thể cần giảm liều, theo dõi chức năng thận",
            "under_30": "Giảm liều hoặc tránh dùng nếu có lựa chọn khác",
            "hemodialysis": "Có thể cần bổ sung sau lọc máu (tùy thuốc)",
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
        "contraindications_detail": {
            "tuyệt_đối": ['Dị ứng với evolocumab hoặc bất kỳ thành phần nào', 'Dị ứng với protein tái tổ hợp'],
            "tương_đối": ['Suy gan nặng - chưa có dữ liệu đầy đủ', 'Suy thận nặng - không cần chỉnh liều nhưng thận trọng'],
        },
        "renal_adjustment": {
            "normal": "Không đổi liều",
            "30_60": "Có thể cần giảm liều, theo dõi chức năng thận",
            "under_30": "Giảm liều hoặc tránh dùng nếu có lựa chọn khác",
            "hemodialysis": "Có thể cần bổ sung sau lọc máu (tùy thuốc)",
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
        "contraindications_detail": {
            "tuyệt_đối": ['Dị ứng với inclisiran hoặc bất kỳ thành phần nào'],
            "tương_đối": ['Suy gan nặng - chưa có dữ liệu đầy đủ', 'Suy thận nặng - không cần chỉnh liều nhưng thận trọng'],
        },
        "renal_adjustment": {
            "normal": "Không đổi liều",
            "30_60": "Có thể cần giảm liều, theo dõi chức năng thận",
            "under_30": "Giảm liều hoặc tránh dùng nếu có lựa chọn khác",
            "hemodialysis": "Có thể cần bổ sung sau lọc máu (tùy thuốc)",
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
    "Sitagliptin": {
        "black_box_warnings": None,
        "contraindications_detail": {
            "tuyệt_đối": ['Đái tháo đường type 1', 'Nhiễm toan ceton do đái tháo đường', 'Dị ứng sitagliptin', 'Viêm tụy cấp đang diễn ra'],
            "tương_đối": ['Suy thận nặng (CrCl <30) - cần giảm liều (25mg/ngày)', 'Suy thận trung bình (CrCl 30-50) - cần giảm liều (50mg/ngày)', 'Tiền sử viêm tụy cấp - tăng nguy cơ', 'Tiền sử suy tim - tăng nhẹ nguy cơ suy tim', 'Đau khớp nghiêm trọng - ngừng thuốc nếu xảy ra'],
        },
    },
    "Linagliptin": {
        "black_box_warnings": None,
        "contraindications_detail": {
            "tuyệt_đối": ['Đái tháo đường type 1', 'Nhiễm toan ceton do đái tháo đường', 'Dị ứng linagliptin hoặc DPP-4 inhibitor'],
            "tương_đối": ['Suy thận - không cần điều chỉnh liều (ưu điểm)', 'Suy gan - thận trọng', 'Có thai - category B, an toàn'],
        },
    },
    "Saxagliptin": {
        "black_box_warnings": None,
        "contraindications_detail": {
            "tuyệt_đối": ['Đái tháo đường type 1', 'Nhiễm toan ceton do đái tháo đường', 'Dị ứng saxagliptin hoặc DPP-4 inhibitor'],
            "tương_đối": ['Suy thận - cần điều chỉnh liều (CrCl ≤50 → 2.5mg/ngày)', 'Suy gan - thận trọng', 'Có thai - category B, an toàn'],
        },
    },
    "Alogliptin": {
        "black_box_warnings": None,
        "contraindications_detail": {
            "tuyệt_đối": ['Đái tháo đường type 1', 'Nhiễm toan ceton do đái tháo đường', 'Dị ứng alogliptin hoặc DPP-4 inhibitor'],
            "tương_đối": ['Suy thận - cần điều chỉnh liều (CrCl 30-60 → 12.5mg/ngày, CrCl <30 → 6.25mg/ngày)', 'Suy gan - thận trọng', 'Có thai - category B, an toàn'],
        },
    },
    "Insulin": {
        "contraindications_detail": {
            "tuyệt_đối": ['Hạ đường huyết (hypoglycemia) - không được dùng khi đường huyết thấp', 'Dị ứng insulin hoặc bất kỳ thành phần nào trong chế phẩm insulin', 'Hôn mê do hạ đường huyết - không được dùng insulin cho đến khi hồi phục'],
            "tương_đối": ['Suy thận - giảm clearance insulin, giảm liều insulin', 'Suy gan - giảm gluconeogenesis, tăng nguy cơ hạ đường huyết, giảm liều insulin', 'Suy tim - thận trọng, có thể cần điều chỉnh liều', 'Người cao tuổi - tăng nguy cơ hạ đường huyết, cần liều thấp hơn', 'Bệnh nhân không có khả năng tự quản lý - cần người chăm sóc', 'Bệnh nhân không có khả năng nhận biết hạ đường huyết - tăng nguy cơ', 'Thai kỳ - điều chỉnh liều thường xuyên (tăng nhu cầu trong tam cá nguyệt 2-3)'],
        },
        "renal_adjustment": {
            "normal": "Không đổi liều",
            "30_60": "Có thể cần giảm liều, theo dõi chức năng thận",
            "under_30": "Giảm liều hoặc tránh dùng nếu có lựa chọn khác",
            "hemodialysis": "Có thể cần bổ sung sau lọc máu (tùy thuốc)",
        },
    },
    "Empagliflozin": {
        "black_box_warnings": None,
        "contraindications_detail": {
            "tuyệt_đối": ['Đái tháo đường type 1', 'Nhiễm toan ceton do đái tháo đường', 'Suy thận nặng (eGFR <20)', 'Đang lọc máu', 'Dị ứng empagliflozin'],
            "tương_đối": ['Nhiễm trùng đường tiết niệu tái phát - tăng nguy cơ nhiễm trùng', 'Suy tim nặng - tăng nguy cơ mất nước', 'Người cao tuổi - tăng nguy cơ mất nước, hạ huyết áp', 'Dùng diuretics - tăng nguy cơ mất nước', 'Nhiễm trùng đường sinh dục tái phát - tăng nguy cơ nhiễm trùng'],
        },
    },
    "Dapagliflozin": {
        "black_box_warnings": None,
        "contraindications_detail": {
            "tuyệt_đối": ['Đái tháo đường type 1', 'Nhiễm toan ceton do đái tháo đường', 'Suy thận nặng (eGFR <25)', 'Đang lọc máu', 'Dị ứng dapagliflozin'],
            "tương_đối": ['Nhiễm trùng đường tiết niệu tái phát - tăng nguy cơ nhiễm trùng', 'Suy tim nặng - tăng nguy cơ mất nước', 'Người cao tuổi - tăng nguy cơ mất nước, hạ huyết áp', 'Dùng diuretics - tăng nguy cơ mất nước', 'Nhiễm trùng đường sinh dục tái phát - tăng nguy cơ nhiễm trùng'],
        },
    },
    "Glibenclamide": {
        "contraindications_detail": {
            "tuyệt_đối": ['Đái tháo đường type 1', 'Nhiễm toan ceton do đái tháo đường', 'Dị ứng glibenclamide hoặc sulfonylurea', 'Suy thận nặng (CrCl <30) - tăng nguy cơ hạ đường huyết nghiêm trọng'],
            "tương_đối": ['Suy gan nặng - tăng nguy cơ hạ đường huyết', 'Người cao tuổi - tăng nguy cơ hạ đường huyết', 'Suy thận trung bình (CrCl 30-60) - giảm liều, theo dõi sát', 'Có thai - có thể gây hạ đường huyết ở trẻ sơ sinh', 'Bỏ bữa thường xuyên - tăng nguy cơ hạ đường huyết', 'Uống rượu - tăng nguy cơ hạ đường huyết nghiêm trọng', 'Dùng beta-blocker - che dấu triệu chứng hạ đường huyết'],
        },
        "renal_adjustment": {
            "normal": "Không đổi liều",
            "30_60": "Có thể cần giảm liều, theo dõi chức năng thận",
            "under_30": "Giảm liều hoặc tránh dùng nếu có lựa chọn khác",
            "hemodialysis": "Có thể cần bổ sung sau lọc máu (tùy thuốc)",
        },
    },
    "Gliclazide": {
        "contraindications_detail": {
            "tuyệt_đối": ['Đái tháo đường type 1', 'Nhiễm toan ceton do đái tháo đường', 'Dị ứng gliclazide hoặc sulfonylurea', 'Suy thận nặng (CrCl <30) - tăng nguy cơ hạ đường huyết'],
            "tương_đối": ['Suy gan nặng - tăng nguy cơ hạ đường huyết', 'Người cao tuổi - tăng nguy cơ hạ đường huyết', 'Suy thận trung bình (CrCl 30-60) - giảm liều, theo dõi sát', 'Có thai - có thể gây hạ đường huyết ở trẻ sơ sinh', 'Bỏ bữa thường xuyên - tăng nguy cơ hạ đường huyết', 'Uống rượu - tăng nguy cơ hạ đường huyết'],
        },
        "renal_adjustment": {
            "normal": "Không đổi liều",
            "30_60": "Có thể cần giảm liều, theo dõi chức năng thận",
            "under_30": "Giảm liều hoặc tránh dùng nếu có lựa chọn khác",
            "hemodialysis": "Có thể cần bổ sung sau lọc máu (tùy thuốc)",
        },
    },
    "Acarbose": {
        "black_box_warnings": None,
        "contraindications_detail": {
            "tuyệt_đối": ['Đái tháo đường type 1', 'Nhiễm toan ceton do đái tháo đường', 'Bệnh viêm ruột (Crohn, viêm loét đại tràng)', 'Tắc ruột', 'Suy gan nặng', 'Suy thận nặng (CrCl <25) - CHỐNG CHỈ ĐỊNH', 'Dị ứng acarbose'],
            "tương_đối": ['Suy thận trung bình (CrCl 25-60) - thận trọng, có thể cần giảm liều', 'Suy gan nhẹ-trung bình - thận trọng', 'Có thai - category B, an toàn'],
        },
    },
    "Miglitol": {
        "black_box_warnings": None,
        "contraindications_detail": {
            "tuyệt_đối": ['Đái tháo đường type 1', 'Nhiễm toan ceton do đái tháo đường', 'Bệnh viêm ruột (Crohn, viêm loét đại tràng)', 'Tắc ruột', 'Suy thận nặng (CrCl <25) - CHỐNG CHỈ ĐỊNH', 'Dị ứng miglitol'],
            "tương_đối": ['Suy thận trung bình (CrCl 25-60) - thận trọng, có thể cần giảm liều', 'Có thai - category B, an toàn'],
        },
    },
    "Loperamide": {
        "contraindications_detail": {
            "tuyệt_đối": ['Dị ứng loperamide', 'Tiêu chảy nhiễm khuẩn nặng (C. difficile, E. coli O157:H7) - có thể giữ vi khuẩn trong ruột', 'Viêm đại tràng giả mạc - có thể làm nặng thêm', 'Tắc ruột cơ học', 'Trẻ em <2 tuổi - nguy cơ ức chế hô hấp', 'Liều cao với CYP3A4 inhibitors - CHỐNG CHỈ ĐỊNH'],
            "tương_đối": ['Suy gan nặng - giảm liều, tăng nguy cơ tích lũy', 'Suy thận nặng - giảm liều, tăng nguy cơ tích lũy', 'Tiêu chảy nhiễm khuẩn nhẹ - thận trọng, đã điều trị kháng sinh', 'Trẻ em 2-6 tuổi - thận trọng, giảm liều', 'Đang dùng opioids - tăng nguy cơ tác dụng phụ'],
        },
        "renal_adjustment": {
            "normal": "Không đổi liều",
            "30_60": "Có thể cần giảm liều, theo dõi chức năng thận",
            "under_30": "Giảm liều hoặc tránh dùng nếu có lựa chọn khác",
            "hemodialysis": "Có thể cần bổ sung sau lọc máu (tùy thuốc)",
        },
    },
    "Bismuth subsalicylate": {
        "contraindications_detail": {
            "tuyệt_đối": ['Dị ứng aspirin hoặc salicylates', 'Trẻ em <12 tuổi - nguy cơ hội chứng Reye (nguy hiểm tính mạng)', 'Dùng aspirin hoặc thuốc chống đông (warfarin) - tăng nguy cơ chảy máu nghiêm trọng', 'Suy thận nặng - tích lũy bismuth và salicylate'],
            "tương_đối": ['Suy thận nhẹ đến trung bình - thận trọng, tích lũy bismuth và salicylate', 'Loét dạ dày - salicylate có thể kích ứng', 'Mang thai - salicylate có thể ảnh hưởng thai nhi', 'Dùng với tetracycline, quinolone - giảm hấp thu, cần cách xa 2 giờ'],
        },
        "renal_adjustment": {
            "normal": "Không đổi liều",
            "30_60": "Có thể cần giảm liều, theo dõi chức năng thận",
            "under_30": "Giảm liều hoặc tránh dùng nếu có lựa chọn khác",
            "hemodialysis": "Có thể cần bổ sung sau lọc máu (tùy thuốc)",
        },
    },
    "Cimetidine": {
        "contraindications_detail": {
            "tuyệt_đối": ['Dị ứng cimetidine hoặc H2 blocker khác'],
            "tương_đối": ['Suy thận nặng (CrCl <30) - cần giảm liều 75%', 'Suy gan nặng - thận trọng', 'Người già - tăng nguy cơ lú lẫn', 'Dùng với warfarin, theophylline, phenytoin, lidocaine - tăng nguy cơ độc tính', 'Nhiễm C. difficile - tăng nguy cơ nhẹ'],
        },
        "reversal_agents": {
            "available": False,
            "agents": [],
            "notes": "Không có thuốc giải độc đặc hiệu; điều trị hỗ trợ triệu chứng.",
        },
    },
    "Sucralfate": {
        "contraindications_detail": {
            "tuyệt_đối": ['Dị ứng sucralfate', 'Suy thận nặng (CrCl <30) - CHỐNG CHỈ ĐỊNH do tích tụ nhôm'],
            "tương_đối": ['Suy thận trung bình (CrCl 30-60) - thận trọng, giảm liều, theo dõi chức năng thận', 'Táo bón nặng - có thể làm nặng thêm', 'Đang dùng nhiều thuốc - tăng nguy cơ tương tác hấp thu'],
        },
        "reversal_agents": {
            "available": False,
            "agents": [],
            "notes": "Không có thuốc giải độc đặc hiệu; điều trị hỗ trợ triệu chứng.",
        },
    },
    "Lansoprazole": {
        "contraindications_detail": {
            "tuyệt_đối": ['Dị ứng lansoprazole hoặc PPI khác', 'Dùng cùng atazanavir (HIV protease inhibitor)'],
            "tương_đối": ['Suy gan nặng (Child-Pugh C) - giảm liều tối đa 15mg/ngày', 'Suy thận nặng (CrCl <30) - không cần chỉnh liều nhưng thận trọng', 'Loãng xương - tăng nguy cơ gãy xương khi dùng lâu dài', 'Nhiễm C. difficile - tăng nguy cơ', 'Thiếu vitamin B12 - bổ sung nếu dùng lâu dài', 'Thiếu magnesium - bổ sung nếu dùng lâu dài'],
        },
        "reversal_agents": {
            "available": False,
            "agents": [],
            "notes": "Không có thuốc giải độc đặc hiệu; điều trị hỗ trợ triệu chứng.",
        },
    },
    "Esomeprazole": {
        "contraindications_detail": {
            "tuyệt_đối": ['Dị ứng esomeprazole hoặc PPI khác', 'Dùng cùng atazanavir (HIV protease inhibitor)'],
            "tương_đối": ['Suy gan nặng (Child-Pugh C) - giảm liều tối đa 20mg/ngày', 'Suy thận nặng (CrCl <30) - không cần chỉnh liều nhưng thận trọng', 'Loãng xương - tăng nguy cơ gãy xương khi dùng lâu dài', 'Nhiễm C. difficile - tăng nguy cơ', 'Thiếu vitamin B12 - bổ sung nếu dùng lâu dài', 'Thiếu magnesium - bổ sung nếu dùng lâu dài'],
        },
        "reversal_agents": {
            "available": False,
            "agents": [],
            "notes": "Không có thuốc giải độc đặc hiệu; điều trị hỗ trợ triệu chứng.",
        },
    },
    "Metoclopramide": {
        "contraindications_detail": {
            "tuyệt_đối": ['Dị ứng metoclopramide', 'Tắc ruột cơ học', 'Xuất huyết tiêu hóa', 'Thủng dạ dày-ruột', 'Pheochromocytoma (tăng nguy cơ tăng huyết áp)', 'Rối loạn vận động (Parkinson, dystonia, tardive dyskinesia)'],
            "tương_đối": ['Suy thận (CrCl <30) - giảm liều 50-75%', 'Suy gan nặng - thận trọng, có thể giảm liều', 'Trẻ em và thanh niên - tăng nguy cơ dystonia, parkinsonism', 'Epilepsy - có thể làm nặng co giật', 'Đang dùng SSRI/SNRI - tăng nguy cơ hội chứng serotonin', 'Đang dùng antipsychotics - tăng nguy cơ rối loạn vận động'],
        },
        "reversal_agents": {
            "available": False,
            "agents": [],
            "notes": "Không có thuốc giải độc đặc hiệu; điều trị hỗ trợ triệu chứng.",
        },
    },
    "Domperidone": {
        "contraindications_detail": {
            "tuyệt_đối": ['Dị ứng domperidone', 'Chảy máu dạ dày', 'Tắc ruột cơ học', 'Prolactinoma', 'Dùng với các thuốc kéo dài QT - CHỐNG CHỈ ĐỊNH tuyệt đối', 'QT kéo dài (QTc >450ms ở nam, >470ms ở nữ) - CHỐNG CHỈ ĐỊNH'],
            "tương_đối": ['Suy thận nặng (CrCl <30) - giảm liều 50%', 'Suy gan nặng - giảm liều, tăng nguy cơ QT kéo dài', 'Hạ kali, hạ magie - tăng nguy cơ QT kéo dài', 'Người già - thận trọng, giảm liều', 'Rối loạn nhịp tim - thận trọng'],
        },
        "reversal_agents": {
            "available": False,
            "agents": [],
            "notes": "Không có thuốc giải độc đặc hiệu; điều trị hỗ trợ triệu chứng.",
        },
    },
    "Ondansetron": {
        "contraindications_detail": {
            "tuyệt_đối": ['Dị ứng ondansetron', 'Dùng với apomorphine - CHỐNG CHỈ ĐỊNH tuyệt đối', 'QT kéo dài (QTc >450ms ở nam, >470ms ở nữ) - CHỐNG CHỈ ĐỊNH'],
            "tương_đối": ['Suy gan nặng - giảm liều 50% (tối đa 8mg/ngày)', 'Hạ kali, hạ magie - tăng nguy cơ QT kéo dài, bổ sung trước khi dùng', 'Đang dùng thuốc kéo dài QT - thận trọng, giảm liều', 'Người già - thận trọng, giảm liều', 'Rối loạn nhịp tim - thận trọng'],
        },
        "reversal_agents": {
            "available": False,
            "agents": [],
            "notes": "Không có thuốc giải độc đặc hiệu; điều trị hỗ trợ triệu chứng.",
        },
    },
    "Vonoprazan": {
        "contraindications_detail": {
            "tuyệt_đối": ['Dị ứng vonoprazan hoặc PCAB'],
            "tương_đối": ['Suy gan nặng', 'Loãng xương'],
        },
        "renal_adjustment": {
            "normal": "Không đổi liều",
            "30_60": "Có thể cần giảm liều, theo dõi chức năng thận",
            "under_30": "Giảm liều hoặc tránh dùng nếu có lựa chọn khác",
            "hemodialysis": "Có thể cần bổ sung sau lọc máu (tùy thuốc)",
        },
        "hepatic_adjustment": {
            "mild": "Không cần chỉnh liều.",
            "moderate": "Thận trọng.",
            "severe": "Thận trọng, có thể giảm liều.",
            "notes": "Vonoprazan chuyển hóa qua gan.",
        },
        "reversal_agents": {
            "available": False,
            "agents": [],
            "notes": "Không có thuốc giải độc đặc hiệu.",
        },
    },
    "Tegoprazan": {
        "contraindications_detail": {
            "tuyệt_đối": ['Dị ứng tegoprazan hoặc PCAB'],
            "tương_đối": ['Suy gan nặng', 'Loãng xương'],
        },
        "renal_adjustment": {
            "normal": "Không đổi liều",
            "30_60": "Có thể cần giảm liều, theo dõi chức năng thận",
            "under_30": "Giảm liều hoặc tránh dùng nếu có lựa chọn khác",
            "hemodialysis": "Có thể cần bổ sung sau lọc máu (tùy thuốc)",
        },
        "hepatic_adjustment": {
            "mild": "Không cần chỉnh liều.",
            "moderate": "Thận trọng.",
            "severe": "Thận trọng, có thể giảm liều.",
            "notes": "Tegoprazan chuyển hóa qua gan.",
        },
        "reversal_agents": {
            "available": False,
            "agents": [],
            "notes": "Không có thuốc giải độc đặc hiệu.",
        },
    },
    "Lactulose": {
        "black_box_warnings": None,
        "drug_interactions": {
            "major": [],
            "moderate": [],
            "minor": [],
        },
    },
    "Polyethylene glycol 3350": {
        "black_box_warnings": None,
        "drug_interactions": {
            "major": [],
            "moderate": [],
            "minor": [],
        },
    },
    # ======================== PHIÊN 7: Neurological drugs ========================
    "Istradefylline": {
        "contraindications_detail": {
            "tuyệt_đối": [
                "Dị ứng với istradefylline hoặc bất kỳ thành phần nào",
            ],
            "tương_đối": [
                "Suy gan vừa-nặng - thận trọng",
                "Suy thận nặng (CrCl <30) - thận trọng",
                "Bệnh nhân cao tuổi - tăng nguy cơ tác dụng phụ",
            ],
        },
        "reversal_agents": {
            "available": False,
            "agents": [],
            "notes": "Không có thuốc giải độc đặc hiệu. Xử trí quá liều chủ yếu là hỗ trợ triệu chứng và ngừng thuốc.",
        },
    },
    "Lamotrigine": {
        "contraindications_detail": {
            "tuyệt_đối": [
                "Dị ứng với lamotrigine",
            ],
            "tương_đối": [
                "Suy thận nặng (CrCl <30) - thận trọng, có thể cần giảm liều",
                "Suy gan vừa-nặng - cần giảm liều",
                "Có thai - thận trọng, cân nhắc lợi ích/nguy cơ",
                "Đang cho con bú - thận trọng",
                "Tiền sử phát ban nặng do thuốc",
            ],
        },
        "renal_adjustment": {
            "normal": "Không đổi liều",
            "30_60": "Không đổi liều",
            "under_30": "Thận trọng, có thể cần giảm liều",
            "hemodialysis": "Có thể cần bổ sung liều sau mỗi lần lọc máu",
        },
    },
    "Levetiracetam": {
        "contraindications_detail": {
            "tuyệt_đối": [
                "Dị ứng với levetiracetam hoặc bất kỳ thành phần nào",
            ],
            "tương_đối": [
                "Suy thận nặng (CrCl <30) - cần giảm liều",
                "Suy gan nặng - thận trọng",
                "Bệnh nhân cao tuổi - tăng nguy cơ tác dụng phụ",
                "Có thai - thận trọng",
                "Đang cho con bú - thận trọng",
                "Tiền sử rối loạn tâm thần - tăng nguy cơ kích động, trầm cảm",
            ],
        },
        "reversal_agents": {
            "available": False,
            "agents": [],
            "notes": "Không có thuốc giải độc đặc hiệu. Xử trí quá liều chủ yếu là hỗ trợ triệu chứng và ngừng thuốc.",
        },
    },
    "Levodopa/Carbidopa": {
        "contraindications_detail": {
            "tuyệt_đối": [
                "Dị ứng với levodopa, carbidopa hoặc bất kỳ thành phần nào",
                "Đang dùng hoặc đã dùng MAO inhibitor không chọn lọc trong vòng 14 ngày",
                "Glaucoma góc đóng không được điều trị",
            ],
            "tương_đối": [
                "Suy thận nặng (CrCl <30) - thận trọng",
                "Suy gan vừa-nặng - thận trọng",
                "Bệnh tim mạch - thận trọng, có thể gây rối loạn nhịp tim",
                "Loét dạ dày tá tràng - thận trọng",
                "Tiền sử rối loạn tâm thần - tăng nguy cơ ảo giác, rối loạn tâm thần",
                "Có thai - thận trọng",
                "Đang cho con bú - thận trọng",
            ],
        },
        "renal_adjustment": {
            "normal": "Không đổi liều",
            "30_60": "Không đổi liều",
            "under_30": "Thận trọng, có thể cần giảm liều",
            "hemodialysis": "Không đổi liều",
        },
    },
    "Lorazepam": {
        "contraindications_detail": {
            "tuyệt_đối": [
                "Dị ứng với lorazepam hoặc benzodiazepine",
                "Bệnh nhược cơ nặng",
                "Hội chứng ngưng thở khi ngủ nặng",
                "Suy hô hấp nặng",
            ],
            "tương_đối": [
                "Suy thận nặng (CrCl <30) - thận trọng",
                "Suy gan vừa-nặng - cần giảm liều",
                "Bệnh nhân cao tuổi - tăng nguy cơ tác dụng phụ, giảm liều",
                "Có thai - tránh dùng trong tam cá nguyệt đầu, thận trọng sau đó",
                "Đang cho con bú - thận trọng",
                "Tiền sử lạm dụng chất",
                "Trầm cảm nặng - có thể tăng nguy cơ tự tử",
            ],
        },
        "renal_adjustment": {
            "normal": "Không đổi liều",
            "30_60": "Không đổi liều",
            "under_30": "Thận trọng, có thể tích tụ",
            "hemodialysis": "Không đổi liều",
        },
    },
    "Memantine": {
        "contraindications_detail": {
            "tuyệt_đối": [
                "Dị ứng với memantine hoặc bất kỳ thành phần nào",
            ],
            "tương_đối": [
                "Suy thận nặng (CrCl <30) - cần giảm liều",
                "Suy gan vừa-nặng - thận trọng",
                "Rối loạn nhịp tim, block nhĩ thất",
                "Động kinh hoặc tiền sử động kinh",
                "Có thai - thận trọng",
                "Đang cho con bú - thận trọng",
            ],
        },
        "renal_adjustment": {
            "normal": "Không đổi liều",
            "30_60": "Giảm liều 50%",
            "under_30": "Giảm liều 50%",
            "hemodialysis": "Không đổi liều",
        },
    },
    "Opicapone": {
        "contraindications_detail": {
            "tuyệt_đối": [
                "Dị ứng với opicapone hoặc bất kỳ thành phần nào",
                "Pheochromocytoma",
                "Đang dùng non-selective MAO inhibitor",
            ],
            "tương_đối": [
                "Suy gan vừa-nặng - thận trọng",
                "Suy thận nặng (CrCl <30) - thận trọng",
                "Rối loạn nhịp tim",
                "Có thai - thận trọng",
                "Đang cho con bú - thận trọng",
            ],
        },
        "reversal_agents": {
            "available": False,
            "agents": [],
            "notes": "Không có thuốc giải độc đặc hiệu. Xử trí quá liều chủ yếu là hỗ trợ triệu chứng và ngừng thuốc.",
        },
    },
    "Phenobarbital": {
        "contraindications_detail": {
            "tuyệt_đối": [
                "Dị ứng với phenobarbital hoặc barbiturate",
                "Porphyria cấp tính",
                "Suy hô hấp nặng",
            ],
            "tương_đối": [
                "Suy thận nặng (CrCl <30) - thận trọng",
                "Suy gan vừa-nặng - cần giảm liều",
                "Bệnh nhân cao tuổi - tăng nguy cơ tác dụng phụ, giảm liều",
                "Có thai - thận trọng, có thể gây dị tật bẩm sinh",
                "Đang cho con bú - thận trọng",
                "Tiền sử lạm dụng chất",
                "Trầm cảm nặng - có thể tăng nguy cơ tự tử",
            ],
        },
        "reversal_agents": {
            "available": False,
            "agents": [],
            "notes": "Không có thuốc giải độc đặc hiệu. Xử trí quá liều chủ yếu là hỗ trợ hô hấp, huyết động và ngừng thuốc.",
        },
    },
    "Phenytoin": {
        "contraindications_detail": {
            "tuyệt_đối": [
                "Dị ứng với phenytoin hoặc bất kỳ thành phần nào",
            ],
            "tương_đối": [
                "Suy thận nặng (CrCl <30) - thận trọng",
                "Suy gan vừa-nặng - cần giảm liều",
                "Bệnh nhân cao tuổi - tăng nguy cơ tác dụng phụ",
                "Có thai - thận trọng, có thể gây dị tật bẩm sinh",
                "Đang cho con bú - thận trọng",
                "Rối loạn nhịp tim, block nhĩ thất",
                "Tiền sử phát ban nặng do thuốc",
            ],
        },
        "reversal_agents": {
            "available": False,
            "agents": [],
            "notes": "Không có thuốc giải độc đặc hiệu. Xử trí quá liều chủ yếu là hỗ trợ triệu chứng, theo dõi nồng độ trong máu và ngừng thuốc.",
        },
    },
    "Piracetam": {
        "black_box_warnings": None,
        "reversal_agents": {
            "available": False,
            "agents": [],
            "notes": "Không có thuốc giải độc đặc hiệu. Xử trí quá liều chủ yếu là hỗ trợ triệu chứng.",
        },
    },
    "Pregabalin": {
        "contraindications_detail": {
            "tuyệt_đối": [
                "Dị ứng với pregabalin hoặc bất kỳ thành phần nào",
            ],
            "tương_đối": [
                "Suy thận nặng (CrCl <30) - cần giảm liều",
                "Suy gan vừa-nặng - thận trọng",
                "Bệnh nhân cao tuổi - tăng nguy cơ tác dụng phụ",
                "Có thai - thận trọng",
                "Đang cho con bú - thận trọng",
                "Tiền sử lạm dụng chất - có nguy cơ nghiện",
                "Suy tim sung huyết - thận trọng",
            ],
        },
        "reversal_agents": {
            "available": False,
            "agents": [],
            "notes": "Không có thuốc giải độc đặc hiệu. Xử trí quá liều chủ yếu là hỗ trợ triệu chứng và ngừng thuốc.",
        },
    },
    "Rimegepant": {
        "contraindications_detail": {
            "tuyệt_đối": [
                "Dị ứng với rimegepant hoặc bất kỳ thành phần nào",
                "Đang dùng thuốc ức chế CYP3A4 mạnh (ketoconazole, itraconazole, clarithromycin) - CHỐNG CHỈ ĐỊNH tuyệt đối",
            ],
            "tương_đối": [
                "Suy gan vừa-nặng - thận trọng, có thể cần giảm liều",
                "Suy thận nặng (CrCl <30) - thận trọng",
                "Bệnh tim mạch - thận trọng",
                "Có thai - thận trọng",
                "Đang cho con bú - thận trọng",
            ],
        },
        "reversal_agents": {
            "available": False,
            "agents": [],
            "notes": "Không có thuốc giải độc đặc hiệu. Xử trí quá liều chủ yếu là hỗ trợ triệu chứng và ngừng thuốc.",
        },
    },
    # ======================== PHIÊN 8: Neurological drugs ========================
    "Rivastigmine": {
        "contraindications_detail": {
            "tuyệt_đối": [
                "Dị ứng với rivastigmine hoặc bất kỳ thành phần nào",
            ],
            "tương_đối": [
                "Suy thận nặng (CrCl <30) - thận trọng",
                "Suy gan vừa-nặng - thận trọng",
                "Rối loạn nhịp tim, block nhĩ thất",
                "Bệnh phổi tắc nghẽn mạn tính (COPD) nặng",
                "Động kinh hoặc tiền sử động kinh",
                "Loét dạ dày tá tràng - thận trọng",
            ],
        },
        "renal_adjustment": {
            "normal": "Không đổi liều",
            "30_60": "Không đổi liều",
            "under_30": "Thận trọng, có thể cần giảm liều",
            "hemodialysis": "Không đổi liều",
        },
    },
    "Ropinirole": {
        "contraindications_detail": {
            "tuyệt_đối": [
                "Dị ứng với ropinirole hoặc bất kỳ thành phần nào",
            ],
            "tương_đối": [
                "Suy thận nặng (CrCl <30) - thận trọng",
                "Suy gan vừa-nặng - thận trọng",
                "Hạ huyết áp tư thế - thận trọng",
                "Rối loạn nhịp tim",
                "Tiền sử rối loạn tâm thần - tăng nguy cơ ảo giác, rối loạn tâm thần",
                "Buồn ngủ ban ngày quá mức, rối loạn giấc ngủ",
                "Có thai - thận trọng",
                "Đang cho con bú - thận trọng",
            ],
        },
        "renal_adjustment": {
            "normal": "Không đổi liều",
            "30_60": "Không đổi liều",
            "under_30": "Thận trọng, có thể cần giảm liều",
            "hemodialysis": "Không đổi liều",
        },
    },
    "Tizanidine": {
        "contraindications_detail": {
            "tuyệt_đối": [
                "Dị ứng với tizanidine hoặc bất kỳ thành phần nào",
            ],
            "tương_đối": [
                "Suy thận nặng (CrCl <30) - cần giảm liều",
                "Suy gan vừa-nặng - cần giảm liều",
                "Bệnh nhân cao tuổi - tăng nguy cơ tác dụng phụ, giảm liều",
                "Hạ huyết áp - thận trọng",
                "Có thai - thận trọng",
                "Đang cho con bú - thận trọng",
            ],
        },
        "renal_adjustment": {
            "normal": "Không đổi liều",
            "30_60": "Không đổi liều",
            "under_30": "Giảm liều, thận trọng",
            "hemodialysis": "Không đổi liều",
        },
    },
    "Topiramate": {
        "contraindications_detail": {
            "tuyệt_đối": [
                "Dị ứng với topiramate hoặc bất kỳ thành phần nào",
            ],
            "tương_đối": [
                "Suy thận nặng (CrCl <30) - cần giảm liều",
                "Suy gan vừa-nặng - thận trọng",
                "Sỏi thận - tăng nguy cơ sỏi thận",
                "Tăng nhãn áp - thận trọng",
                "Có thai - thận trọng, có thể gây dị tật bẩm sinh",
                "Đang cho con bú - thận trọng",
                "Rối loạn chuyển hóa acid-base",
            ],
        },
        "renal_adjustment": {
            "normal": "Không đổi liều",
            "30_60": "Không đổi liều",
            "under_30": "Giảm liều 50%",
            "hemodialysis": "Có thể cần bổ sung liều sau mỗi lần lọc máu",
        },
    },
    "Ubrogepant": {
        "contraindications_detail": {
            "tuyệt_đối": [
                "Dị ứng với ubrogepant hoặc bất kỳ thành phần nào",
                "Đang dùng thuốc ức chế CYP3A4 mạnh (ketoconazole, itraconazole, clarithromycin) - CHỐNG CHỈ ĐỊNH tuyệt đối",
            ],
            "tương_đối": [
                "Suy gan vừa-nặng - thận trọng, có thể cần giảm liều",
                "Suy thận nặng (CrCl <30) - thận trọng",
                "Bệnh tim mạch - thận trọng",
                "Có thai - thận trọng",
                "Đang cho con bú - thận trọng",
            ],
        },
        "reversal_agents": {
            "available": False,
            "agents": [],
            "notes": "Không có thuốc giải độc đặc hiệu. Xử trí quá liều chủ yếu là hỗ trợ triệu chứng và ngừng thuốc.",
        },
    },
    "Valproate": {
        "contraindications_detail": {
            "tuyệt_đối": [
                "Dị ứng với valproate hoặc bất kỳ thành phần nào",
                "Bệnh gan nặng hoặc rối loạn chức năng gan nặng",
                "Rối loạn chu trình urea",
                "Bệnh ty thể (mitochondrial disease)",
            ],
            "tương_đối": [
                "Suy thận nặng (CrCl <30) - thận trọng, có thể cần giảm liều",
                "Suy gan vừa - thận trọng, theo dõi chức năng gan sát",
                "Có thai - thận trọng, có thể gây dị tật bẩm sinh và giảm IQ ở trẻ",
                "Đang cho con bú - thận trọng",
                "Rối loạn đông máu - tăng nguy cơ chảy máu",
                "Tiền sử viêm tụy - tăng nguy cơ viêm tụy",
            ],
        },
        "renal_adjustment": {
            "normal": "Không đổi liều",
            "30_60": "Không đổi liều",
            "under_30": "Thận trọng, có thể cần giảm liều",
            "hemodialysis": "Có thể cần bổ sung liều sau mỗi lần lọc máu",
        },
    },
    "Vinpocetine": {
        "black_box_warnings": None,
        "reversal_agents": {
            "available": False,
            "agents": [],
            "notes": "Không có thuốc giải độc đặc hiệu. Xử trí quá liều chủ yếu là hỗ trợ triệu chứng.",
        },
    },
})
# ======================== END BATCH 2 ========================

# Auto-generated fixes from validation
# Generated by apply_auto_fixes_to_file.py

EXTRA_ENHANCED_FIELDS.update({
    "Abaloparatide": {
        "interactions": ['Chưa có báo cáo tương tác thuốc đáng kể'],
    },
    "Alirocumab": {
        "overdose_management": {
            "symptoms": ['Cần đánh giá lâm sàng'],
            "antidote": 'Không có antidote đặc hiệu',
            "treatment": ['Chưa có báo cáo quá liều. Nếu tiêm quá liều, theo dõi các tác dụng phụ và điều trị hỗ trợ.'],
            "monitoring": 'Theo dõi dấu hiệu sinh tồn và triệu chứng',
        },
        "administration_instructions": {
            "oral": {
                "with_food": 'Tiêm dưới da (bụng, đùi, hoặc cánh tay). Để ở nhiệt độ phòng 30 phút trước khi tiêm. Không lắc. Luân phiên vị trí tiêm. Có thể tự tiêm sau khi được hướng dẫn.',
                "timing": 'Theo chỉ định của bác sĩ',
            },
            "iv": {
                "reconstitution": 'N/A',
                "infusion_rate": 'N/A',
                "compatibility": [],
                "incompatibility": [],
                "notes": 'N/A',
            },
        },
    },
    "Amlodipine/Olmesartan": {
        "interactions": ['Chưa có báo cáo tương tác thuốc đáng kể'],
    },
    "Calcitonin": {
        "interactions": ['Chưa có báo cáo tương tác thuốc đáng kể'],
    },
    "Enalapril": {
        "guideline_tags": ['C09AA02', '24.08.08 ACE Inhibitors', 'vietnam_essential_medicines: True', {'source': 'ESC 2021 Heart Failure', 'recommendation': 'ACE inhibitor first-line therapy for HFrEF if tolerated', 'context': 'Heart failure with reduced ejection fraction (HFrEF), NYHA II–III'}, {'source': 'ACC/AHA 2017 Hypertension Guideline', 'recommendation': 'One of the first-line options for hypertension', 'context': 'Primary hypertension, non-black, with or without diabetes'}, {'source': 'BYT – Hướng dẫn chẩn đoán và điều trị tăng huyết áp 2020', 'recommendation': 'Một trong các lựa chọn hàng đầu điều trị tăng huyết áp', 'context': 'Tăng huyết áp nguyên phát không biến chứng, ưu tiên bệnh nhân có đái tháo đường hoặc bệnh thận mạn'}, 'first_line_htn', 'hfref_mortality_benefit', 'ckd_proteinuria_bp_control'],
    },
    "Evolocumab": {
        "overdose_management": {
            "symptoms": ['Cần đánh giá lâm sàng'],
            "antidote": 'Không có antidote đặc hiệu',
            "treatment": ['Chưa có báo cáo quá liều. Nếu tiêm quá liều, theo dõi các tác dụng phụ và điều trị hỗ trợ.'],
            "monitoring": 'Theo dõi dấu hiệu sinh tồn và triệu chứng',
        },
        "administration_instructions": {
            "oral": {
                "with_food": 'Tiêm dưới da (bụng, đùi, hoặc cánh tay). Để ở nhiệt độ phòng 30 phút trước khi tiêm. Không lắc. Luân phiên vị trí tiêm. Có thể tự tiêm sau khi được hướng dẫn.',
                "timing": 'Theo chỉ định của bác sĩ',
            },
            "iv": {
                "reconstitution": 'N/A',
                "infusion_rate": 'N/A',
                "compatibility": [],
                "incompatibility": [],
                "notes": 'N/A',
            },
        },
    },
    "Inclisiran": {
        "overdose_management": {
            "symptoms": ['Cần đánh giá lâm sàng'],
            "antidote": 'Không có antidote đặc hiệu',
            "treatment": ['Chưa có báo cáo quá liều. Nếu tiêm quá liều, theo dõi các tác dụng phụ và điều trị hỗ trợ.'],
            "monitoring": 'Theo dõi dấu hiệu sinh tồn và triệu chứng',
        },
        "administration_instructions": {
            "oral": {
                "with_food": 'Tiêm dưới da (bụng, đùi, hoặc cánh tay). Để ở nhiệt độ phòng 30 phút trước khi tiêm. Không lắc. Luân phiên vị trí tiêm. Có thể tự tiêm sau khi được hướng dẫn. Lịch tiêm: Liều đầu tiên, sau đó liều thứ 2 sau 3 tháng, sau đó mỗi 6 tháng.',
                "timing": 'Theo chỉ định của bác sĩ',
            },
            "iv": {
                "reconstitution": 'N/A',
                "infusion_rate": 'N/A',
                "compatibility": [],
                "incompatibility": [],
                "notes": 'N/A',
            },
        },
    },
    "Lisinopril": {
        "guideline_tags": ['C09AA03', '24.08.08 ACE Inhibitors', 'vietnam_essential_medicines: True', {'source': 'ESC 2021 Heart Failure', 'recommendation': 'ACE inhibitor first-line therapy for HFrEF if ARNI not available', 'context': 'Heart failure with reduced ejection fraction (HFrEF), NYHA II–III'}, {'source': 'BYT – Hướng dẫn chẩn đoán và điều trị suy tim 2015', 'recommendation': 'Thuốc nền tảng trong điều trị suy tim HFrEF cùng với beta-blocker và mineralocorticoid receptor antagonist', 'context': 'Suy tim mạn HFrEF, NYHA II–IV'}, 'first_line_htn', 'hfref_mortality_benefit'],
    },
    "Losartan": {
        "guideline_tags": ['C09CA01', '24.08.06 Angiotensin II Receptor Blockers', 'vietnam_essential_medicines: True', {'source': 'ACC/AHA 2017 Hypertension Guideline', 'recommendation': 'ARB as alternative first-line when ACE inhibitors not tolerated', 'context': 'Primary hypertension, ACE inhibitor intolerance (e.g. cough, angioedema)'}, {'source': 'BYT – Hướng dẫn chẩn đoán và điều trị tăng huyết áp 2020', 'recommendation': 'Lựa chọn khi không dung nạp ACEI hoặc cần bảo vệ thận', 'context': 'Tăng huyết áp có đái tháo đường hoặc bệnh thận mạn'}, 'first_line_htn_alt_acei', 'ckd_diabetic_nephropathy'],
    },
    "Metformin": {
        "guideline_tags": ['A10BA02', '68.20.08 Biguanides', 'vietnam_essential_medicines: True', {'source': 'ADA 2024 Standards of Care', 'recommendation': 'Initial pharmacologic therapy for most adults with type 2 diabetes', 'context': 'Type 2 diabetes without contraindications; often combined with lifestyle changes'}, {'source': 'BYT – Hướng dẫn chẩn đoán và điều trị đái tháo đường typ 2', 'recommendation': 'Thuốc đầu tay trong điều trị đái tháo đường typ 2 nếu không chống chỉ định', 'context': 'ĐTĐ typ 2, không suy thận nặng hoặc chống chỉ định khác'}, 'first_line_t2dm', 'weight_neutral_or_loss', 'low_hypoglycemia_risk'],
    },
    "Romosozumab": {
        "interactions": ['Chưa có báo cáo tương tác thuốc đáng kể'],
    },
    "Spironolactone": {
        "guideline_tags": ['C03DA01', '24.08.04 Aldosterone Antagonists', 'vietnam_essential_medicines: True', {'source': 'ESC 2021 Heart Failure', 'recommendation': 'Mineralocorticoid receptor antagonist to reduce mortality', 'context': 'HFrEF with persistent symptoms despite ACEI/ARB/ARNI and beta-blocker'}, 'hfref_mortality_benefit', 'hyperaldosteronism'],
    },
    "Tegoprazan": {
        "overdose_management": {
            "symptoms": ['Cần đánh giá lâm sàng'],
            "antidote": 'Không có antidote đặc hiệu',
            "treatment": ['Triệu chứng: Buồn nôn, nôn, đau bụng. Điều trị: Hỗ trợ, rửa dạ dày nếu mới uống.'],
            "monitoring": 'Theo dõi dấu hiệu sinh tồn và triệu chứng',
        },
        "administration_instructions": {
            "oral": {
                "with_food": 'Uống với hoặc không có thức ăn. Nuốt nguyên viên, không nhai hoặc nghiền.',
                "timing": 'Theo chỉ định của bác sĩ',
            },
            "iv": {
                "reconstitution": 'N/A',
                "infusion_rate": 'N/A',
                "compatibility": [],
                "incompatibility": [],
                "notes": 'Chỉ có dạng uống',
            },
        },
    },
    "Vonoprazan": {
        "overdose_management": {
            "symptoms": ['Cần đánh giá lâm sàng'],
            "antidote": 'Không có antidote đặc hiệu',
            "treatment": ['Triệu chứng: Buồn nôn, nôn, đau bụng. Điều trị: Hỗ trợ, rửa dạ dày nếu mới uống. Không có chất đối kháng đặc hiệu.'],
            "monitoring": 'Theo dõi dấu hiệu sinh tồn và triệu chứng',
        },
        "administration_instructions": {
            "oral": {
                "with_food": 'Uống với hoặc không có thức ăn. Không cần uống trước bữa ăn như PPI. Nuốt nguyên viên, không nhai hoặc nghiền.',
                "timing": 'Theo chỉ định của bác sĩ',
            },
            "iv": {
                "reconstitution": 'N/A',
                "infusion_rate": 'N/A',
                "compatibility": [],
                "incompatibility": [],
                "notes": 'Chỉ có dạng uống',
            },
        },
    },
})

# ======================== BATCH 1: ICU/EMERGENCY DRUGS ========================
# Bổ sung contraindications_detail cho các thuốc ICU/emergency quan trọng

EXTRA_ENHANCED_FIELDS.update({
    "Alteplase": {
        "contraindications_detail": {
            "tuyệt_đối": [
                "Dị ứng với alteplase hoặc bất kỳ thành phần nào",
                "Xuất huyết nội sọ đang hoạt động",
                "Tiền sử đột quỵ xuất huyết",
                "Chấn thương đầu hoặc phẫu thuật đầu gần đây (3 tháng)",
                "Xuất huyết tiêu hóa hoặc tiết niệu trong 21 ngày",
                "Rối loạn đông máu",
                "Huyết áp tâm thu >185 mmHg hoặc tâm trương >110 mmHg không kiểm soát được",
            ],
            "tương_đối": [
                "Tuổi >80 tuổi - tăng nguy cơ xuất huyết",
                "Điểm NIHSS >25 - nguy cơ cao",
                "Điều trị kháng đông trong 48 giờ",
                "Tiểu cầu <100,000/mm³",
                "INR >1.7 hoặc PT >15 giây",
                "Đường huyết <50 mg/dL hoặc >400 mg/dL",
                "Đột quỵ nhẹ hoặc TIA trong 3 tháng",
            ],
        },
    },
    "Aspirin": {
        "contraindications_detail": {
            "tuyệt_đối": [
                "Dị ứng với aspirin hoặc NSAID",
                "Tiền sử hen suyễn do aspirin",
                "Xuất huyết tiêu hóa đang hoạt động",
                "Loét dạ dày tá tràng đang hoạt động",
                "Rối loạn đông máu (hemophilia, von Willebrand)",
                "Suy gan nặng",
                "Suy thận nặng (CrCl <30)",
                "Trẻ em <16 tuổi (nguy cơ hội chứng Reye)",
            ],
            "tương_đối": [
                "Tiền sử loét dạ dày tá tràng",
                "Đang dùng thuốc chống đông",
                "Suy thận vừa (CrCl 30-60)",
                "Suy gan vừa",
                "Có thai (3 tháng cuối)",
                "Đang cho con bú",
                "Gout - có thể làm tăng acid uric",
            ],
        },
    },
    "Epinephrine": {
        "contraindications_detail": {
            "tuyệt_đối": [
                "Dị ứng với epinephrine hoặc bất kỳ thành phần nào",
                "Rối loạn nhịp tim nặng không kiểm soát được",
                "Phẫu thuật tim gần đây",
            ],
            "tương_đối": [
                "Bệnh tim mạch nặng",
                "Tăng huyết áp nặng",
                "Đái tháo đường",
                "Cường giáp",
                "Glaucoma góc đóng",
                "Bệnh mạch máu ngoại biên",
                "Người cao tuổi - tăng nhạy cảm",
            ],
        },
    },
    "Morphine": {
        "contraindications_detail": {
            "tuyệt_đối": [
                "Dị ứng với morphine hoặc opioid",
                "Suy hô hấp nặng không có hỗ trợ thở máy",
                "Hen suyễn nặng không kiểm soát",
                "Tắc ruột cơ học",
                "Tăng áp lực nội sọ",
                "Ức chế hô hấp nặng",
            ],
            "tương_đối": [
                "Suy hô hấp vừa",
                "Suy gan nặng",
                "Suy thận nặng (CrCl <30)",
                "Người cao tuổi - giảm liều",
                "Có thai - nguy cơ ức chế hô hấp ở trẻ sơ sinh",
                "Đang cho con bú",
                "Tiền sử lạm dụng chất",
                "Bệnh động kinh",
            ],
        },
    },
    "Metformin": {
        "contraindications_detail": {
            "tuyệt_đối": [
                "Dị ứng với metformin",
                "Suy thận nặng (CrCl <30 mL/min)",
                "Nhiễm toan lactic",
                "Suy gan nặng",
                "Suy tim nặng cần điều trị bằng thuốc",
                "Nhiễm trùng nặng hoặc mất nước nặng",
            ],
            "tương_đối": [
                "Suy thận vừa (CrCl 30-45) - giảm liều",
                "Suy gan vừa - thận trọng",
                "Người cao tuổi >80 tuổi - giảm liều",
                "Nghiện rượu",
                "Phẫu thuật lớn hoặc thủ thuật có cản quang - tạm ngừng",
                "Có thai - thận trọng",
                "Đang cho con bú - thận trọng",
            ],
        },
    },
    "Naloxone": {
        "contraindications_detail": {
            "tuyệt_đối": [
                "Dị ứng với naloxone hoặc bất kỳ thành phần nào",
            ],
            "tương_đối": [
                "Bệnh nhân phụ thuộc opioid - có thể gây hội chứng cai nghiện nặng",
                "Bệnh tim mạch - có thể gây rối loạn nhịp tim",
                "Có thai - thận trọng",
                "Đang cho con bú - thận trọng",
            ],
        },
    },
    "Flumazenil": {
        "contraindications_detail": {
            "tuyệt_đối": [
                "Dị ứng với flumazenil hoặc benzodiazepine",
                "Bệnh nhân phụ thuộc benzodiazepine - nguy cơ co giật",
                "Đang dùng thuốc gây co giật (TCA, bupropion)",
            ],
            "tương_đối": [
                "Bệnh nhân có tiền sử co giật",
                "Tổn thương não",
                "Có thai - thận trọng",
                "Đang cho con bú - thận trọng",
                "Suy gan nặng - thời gian tác dụng kéo dài",
            ],
        },
    },
})
# ======================== END BATCH 1 ========================

# ======================== BATCH 2: CARDIOVASCULAR DRUGS ========================
# Bổ sung contraindications_detail cho các thuốc tim mạch quan trọng

EXTRA_ENHANCED_FIELDS.update({
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
})
# ======================== END BATCH 2 ========================

# ======================== BATCH 3: ANTIBIOTICS ========================
# Bổ sung contraindications_detail cho Cefazolin

EXTRA_ENHANCED_FIELDS.update({
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
    },
})
# ======================== END BATCH 3 ========================

# ======================== BATCH 4: GI & NEUROLOGICAL DRUGS ========================
# Bổ sung contraindications_detail cho các thuốc tiêu hóa và thần kinh

EXTRA_ENHANCED_FIELDS.update({
    "Omeprazole": {
        "contraindications_detail": {
            "tuyệt_đối": [
                "Dị ứng với omeprazole hoặc PPI",
            ],
            "tương_đối": [
                "Suy gan nặng - giảm liều",
                "Suy thận nặng - không cần giảm liều nhưng thận trọng",
                "Loãng xương - tăng nguy cơ gãy xương khi dùng lâu dài",
                "Thiếu vitamin B12 - giảm hấp thu khi dùng lâu dài",
                "Nhiễm Clostridium difficile - tăng nguy cơ",
                "Có thai - thận trọng",
                "Đang cho con bú - thận trọng",
            ],
        },
    },
    "Pantoprazole": {
        "contraindications_detail": {
            "tuyệt_đối": [
                "Dị ứng với pantoprazole hoặc PPI",
            ],
            "tương_đối": [
                "Suy gan nặng - giảm liều",
                "Suy thận nặng - không cần giảm liều nhưng thận trọng",
                "Loãng xương - tăng nguy cơ gãy xương khi dùng lâu dài",
                "Thiếu vitamin B12 - giảm hấp thu khi dùng lâu dài",
                "Nhiễm Clostridium difficile - tăng nguy cơ",
                "Có thai - thận trọng",
                "Đang cho con bú - thận trọng",
            ],
        },
    },
    "Ranitidine": {
        "contraindications_detail": {
            "tuyệt_đối": [
                "Dị ứng với ranitidine hoặc H2 blocker",
            ],
            "tương_đối": [
                "Suy thận nặng (CrCl <50) - giảm liều",
                "Suy gan nặng - thận trọng",
                "Người cao tuổi - tăng nguy cơ tác dụng phụ",
                "Có thai - thận trọng",
                "Đang cho con bú - thận trọng",
            ],
        },
    },
    "Famotidine": {
        "contraindications_detail": {
            "tuyệt_đối": [
                "Dị ứng với famotidine hoặc H2 blocker",
            ],
            "tương_đối": [
                "Suy thận nặng (CrCl <50) - giảm liều",
                "Suy gan nặng - thận trọng",
                "Người cao tuổi - tăng nguy cơ tác dụng phụ",
                "Có thai - thận trọng",
                "Đang cho con bú - thận trọng",
            ],
        },
    },
    "Paracetamol": {
        "pregnancy_lactation": {
            "fda_category": "B",
            "pregnancy_details": (
                "Được xem là an toàn để hạ sốt và giảm đau trong tất cả các giai đoạn của thai kỳ khi dùng ở liều điều trị. "
                "Tuy nhiên, nên dùng liều thấp nhất có hiệu quả trong thời gian ngắn nhất."
            ),
            "lactation": {
                "safety": "Compatible",
                "details": "Bài tiết vào sữa mẹ với lượng nhỏ. Được Viện Nhi khoa Hoa Kỳ (AAP) xếp vào nhóm thuốc an toàn khi cho con bú.",
                "recommendation": "Có thể sử dụng. Không cần ngừng cho con bú.",
            },
        },
        "contraindications_detail": {
            "tuyệt_đối": [
                "Dị ứng với paracetamol",
                "Suy gan nặng",
                "Nghiện rượu nặng",
            ],
            "tương_đối": [
                "Suy gan vừa - giảm liều tối đa",
                "Suy thận nặng - thận trọng",
                "Thiếu G6PD - thận trọng",
                "Suy dinh dưỡng - tăng nguy cơ độc tính",
            ],
        },
    },
    "Ibuprofen": {
        "pregnancy_lactation": {
            "fda_category": "C (D trong 3 tháng cuối)",
            "pregnancy_details": (
                "FDA Category C trong 6 tháng đầu; Category D trong 3 tháng cuối (nguy cơ đóng ống động mạch sớm, thiểu niệu thai nhi, "
                "kéo dài thời gian chuyển dạ). KHÔNG DÙNG trong 3 tháng cuối thai kỳ."
            ),
            "lactation": {
                "safety": "Compatible",
                "details": "Bài tiết rất ít vào sữa mẹ (liều tương đối cho trẻ < 0.6%). AAP xếp vào nhóm an toàn.",
                "recommendation": "Có thể sử dụng. Là lựa chọn NSAID ưu tiên cho phụ nữ cho con bú.",
            },
        },
        "contraindications_detail": {
            "tuyệt_đối": [
                "Dị ứng với ibuprofen hoặc NSAID",
                "Tiền sử hen suyễn do aspirin/NSAID",
                "Loét dạ dày tá tràng đang hoạt động",
                "Xuất huyết tiêu hóa đang hoạt động",
                "Suy tim nặng (NYHA III-IV)",
                "Có thai (3 tháng cuối)",
            ],
            "tương_đối": [
                "Tiền sử loét dạ dày tá tràng",
                "Suy thận nặng (CrCl <30) - thận trọng",
                "Suy gan nặng - thận trọng",
                "Suy tim vừa - thận trọng",
                "Tăng huyết áp không kiểm soát",
                "Đang dùng thuốc chống đông",
                "Có thai (1-2 tháng đầu) - thận trọng",
                "Người cao tuổi - tăng nguy cơ tác dụng phụ",
            ],
        },
    },
    "Diclofenac": {
        "contraindications_detail": {
            "tuyệt_đối": [
                "Dị ứng với diclofenac hoặc NSAID",
                "Tiền sử hen suyễn do aspirin/NSAID",
                "Loét dạ dày tá tràng đang hoạt động",
                "Xuất huyết tiêu hóa đang hoạt động",
                "Suy tim nặng (NYHA III-IV)",
                "Suy gan nặng",
                "Suy thận nặng (CrCl <30)",
                "Có thai (3 tháng cuối) - nguy cơ đóng ống động mạch sớm",
            ],
            "tương_đối": [
                "Tiền sử loét dạ dày tá tràng",
                "Suy thận vừa (CrCl 30-60) - thận trọng",
                "Suy gan vừa - thận trọng",
                "Suy tim vừa - thận trọng",
                "Tăng huyết áp không kiểm soát",
                "Đang dùng thuốc chống đông",
                "Có thai (1-2 tháng đầu và giữa) - thận trọng",
                "Đang cho con bú - thận trọng",
                "Người cao tuổi - tăng nguy cơ tác dụng phụ",
            ],
        },
    },
    "Carbamazepine": {
        "contraindications_detail": {
            "tuyệt_đối": [
                "Dị ứng với carbamazepine",
                "Block nhĩ thất độ 2-3",
                "Suy gan nặng",
                "Tiền sử tủy xương bị ức chế",
                "Đang dùng MAO inhibitor",
            ],
            "tương_đối": [
                "Suy gan vừa - thận trọng, theo dõi chức năng gan",
                "Suy thận nặng - thận trọng",
                "Bệnh tim mạch - tăng nguy cơ block AV",
                "Bệnh nhân có tiền sử rối loạn tâm thần",
                "Glaucoma góc đóng",
                "Có thai - thận trọng, có thể gây dị tật",
                "Đang cho con bú - thận trọng",
                "Người cao tuổi - tăng nhạy cảm",
            ],
        },
    },
})
# ======================== END BATCH 4 ========================

# ======================== BATCH 5: ENDOCRINE DRUGS ========================
# Bổ sung contraindications_detail cho các thuốc nội tiết

EXTRA_ENHANCED_FIELDS.update({
    "Levothyroxine": {
        "contraindications_detail": {
            "tuyệt_đối": [
                "Dị ứng với levothyroxine",
                "Cường giáp không được điều trị",
                "Nhồi máu cơ tim cấp",
                "Viêm cơ tim",
            ],
            "tương_đối": [
                "Bệnh tim mạch - bắt đầu với liều thấp",
                "Suy thượng thận - cần điều trị trước",
                "Đái tháo đường - có thể cần điều chỉnh liều insulin",
                "Có thai - cần tăng liều",
                "Đang cho con bú - thận trọng",
                "Người cao tuổi - bắt đầu với liều thấp",
            ],
        },
    },
    "Methimazole": {
        "contraindications_detail": {
            "tuyệt_đối": [
                "Dị ứng với methimazole",
            ],
            "tương_đối": [
                "Suy gan nặng - thận trọng",
                "Giảm bạch cầu - nguy cơ agranulocytosis",
                "Có thai (3 tháng đầu) - thận trọng, có thể gây dị tật",
                "Đang cho con bú - thận trọng",
                "Người cao tuổi - tăng nguy cơ tác dụng phụ",
            ],
        },
    },
    "Propylthiouracil": {
        "contraindications_detail": {
            "tuyệt_đối": [
                "Dị ứng với propylthiouracil",
            ],
            "tương_đối": [
                "Suy gan nặng - nguy cơ viêm gan",
                "Giảm bạch cầu - nguy cơ agranulocytosis",
                "Có thai (3 tháng đầu) - thận trọng",
                "Đang cho con bú - thận trọng",
                "Người cao tuổi - tăng nguy cơ tác dụng phụ",
            ],
        },
    },
    "Hydrocortisone": {
        "contraindications_detail": {
            "tuyệt_đối": [
                "Dị ứng với hydrocortisone hoặc corticosteroid",
                "Nhiễm trùng hệ thống không được điều trị",
                "Nhiễm nấm toàn thân",
            ],
            "tương_đối": [
                "Đái tháo đường - tăng đường huyết",
                "Tăng huyết áp",
                "Loãng xương",
                "Loét dạ dày tá tràng",
                "Suy tim nặng",
                "Suy gan nặng",
                "Suy thận nặng",
                "Có thai - thận trọng, có thể gây dị tật",
                "Đang cho con bú - thận trọng",
                "Trẻ em - ảnh hưởng đến tăng trưởng",
            ],
        },
    },
    "Dexamethasone": {
        "contraindications_detail": {
            "tuyệt_đối": [
                "Dị ứng với dexamethasone hoặc corticosteroid",
                "Nhiễm trùng hệ thống không được điều trị",
                "Nhiễm nấm toàn thân",
            ],
            "tương_đối": [
                "Đái tháo đường - tăng đường huyết",
                "Tăng huyết áp",
                "Loãng xương",
                "Loét dạ dày tá tràng",
                "Suy tim nặng",
                "Suy gan nặng",
                "Suy thận nặng",
                "Có thai - thận trọng, có thể gây dị tật",
                "Đang cho con bú - thận trọng",
                "Trẻ em - ảnh hưởng đến tăng trưởng",
            ],
        },
    },
})
# ======================== END BATCH 5 ========================

# ======================== BATCH 6: ANTIHISTAMINE & ANTIVIRAL ========================
# Bổ sung contraindications_detail cho các thuốc kháng histamine và kháng virus

EXTRA_ENHANCED_FIELDS.update({
    "Diphenhydramine": {
        "contraindications_detail": {
            "tuyệt_đối": [
                "Dị ứng với diphenhydramine hoặc antihistamine",
                "Trẻ sơ sinh <2 tháng tuổi",
            ],
            "tương_đối": [
                "Bệnh nhược cơ - tăng yếu cơ",
                "Tăng nhãn áp góc đóng",
                "Loét dạ dày tá tràng",
                "Tắc nghẽn đường tiết niệu",
                "Bệnh tim mạch - tăng nguy cơ rối loạn nhịp",
                "Có thai - thận trọng",
                "Đang cho con bú - thận trọng",
                "Người cao tuổi - tăng nguy cơ tác dụng phụ",
            ],
        },
    },
    "Loratadine": {
        "contraindications_detail": {
            "tuyệt_đối": [
                "Dị ứng với loratadine",
            ],
            "tương_đối": [
                "Suy gan nặng - giảm liều",
                "Suy thận nặng - thận trọng",
                "Có thai - thận trọng",
                "Đang cho con bú - thận trọng",
            ],
        },
    },
    "Chlorpheniramine": {
        "contraindications_detail": {
            "tuyệt_đối": [
                "Dị ứng với chlorpheniramine hoặc antihistamine",
                "Trẻ sơ sinh <2 tháng tuổi",
            ],
            "tương_đối": [
                "Bệnh nhược cơ - tăng yếu cơ",
                "Tăng nhãn áp góc đóng",
                "Loét dạ dày tá tràng",
                "Tắc nghẽn đường tiết niệu",
                "Bệnh tim mạch - tăng nguy cơ rối loạn nhịp",
                "Có thai - thận trọng",
                "Đang cho con bú - thận trọng",
                "Người cao tuổi - tăng nguy cơ tác dụng phụ",
            ],
        },
    },
    "Acyclovir": {
        "contraindications_detail": {
            "tuyệt_đối": [
                "Dị ứng với acyclovir",
            ],
            "tương_đối": [
                "Suy thận nặng (CrCl <25) - giảm liều",
                "Mất nước - tăng nguy cơ độc tính thận",
                "Có thai - thận trọng",
                "Đang cho con bú - thận trọng",
                "Người cao tuổi - tăng nguy cơ độc tính thận",
            ],
        },
    },
    "Valacyclovir": {
        "contraindications_detail": {
            "tuyệt_đối": [
                "Dị ứng với valacyclovir hoặc acyclovir",
            ],
            "tương_đối": [
                "Suy thận nặng (CrCl <30) - giảm liều",
                "Mất nước - tăng nguy cơ độc tính thận",
                "Suy gan nặng - thận trọng",
                "Có thai - thận trọng",
                "Đang cho con bú - thận trọng",
                "Người cao tuổi - tăng nguy cơ độc tính thận",
            ],
        },
    },
})
# ======================== END BATCH 6 ========================

# ======================== BATCH 7: MIXED IMPORTANT DRUGS ========================
# Bổ sung contraindications_detail cho các thuốc quan trọng đa dạng

EXTRA_ENHANCED_FIELDS.update({
    "5-Fluorouracil": {
        "contraindications_detail": {
            "tuyệt_đối": [
                "Dị ứng với 5-fluorouracil",
                "Suy thận nặng (CrCl <30)",
                "Suy gan nặng",
                "Thiếu DPD (dihydropyrimidine dehydrogenase)",
                "Có thai",
                "Đang cho con bú",
            ],
            "tương_đối": [
                "Suy thận vừa (CrCl 30-60) - giảm liều",
                "Suy gan vừa - thận trọng",
                "Người cao tuổi - tăng nguy cơ độc tính",
                "Bệnh tim mạch - tăng nguy cơ thiếu máu cơ tim",
            ],
        },
    },
    "Abiraterone": {
        "contraindications_detail": {
            "tuyệt_đối": [
                "Dị ứng với abiraterone",
                "Suy gan nặng",
                "Có thai",
            ],
            "tương_đối": [
                "Suy gan vừa - thận trọng",
                "Suy thận nặng - thận trọng",
                "Bệnh tim mạch - tăng nguy cơ",
                "Đang cho con bú - thận trọng",
            ],
        },
    },
    "Acebutolol": {
        "contraindications_detail": {
            "tuyệt_đối": [
                "Dị ứng với acebutolol hoặc beta-blocker",
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
                "Suy thận nặng (CrCl <30) - giảm liều",
                "Có thai - thận trọng",
                "Đang cho con bú - thận trọng",
            ],
        },
    },
    "Aclidinium": {
        "contraindications_detail": {
            "tuyệt_đối": [
                "Dị ứng với aclidinium",
                "Tăng nhãn áp góc đóng",
            ],
            "tương_đối": [
                "Tăng nhãn áp góc mở - thận trọng",
                "Bệnh tim mạch - thận trọng",
                "Tắc nghẽn đường tiết niệu",
                "Có thai - thận trọng",
                "Đang cho con bú - thận trọng",
            ],
        },
    },
    "Acyclovir eye drops": {
        "contraindications_detail": {
            "tuyệt_đối": [
                "Dị ứng với acyclovir",
            ],
            "tương_đối": [
                "Tổn thương giác mạc nặng",
                "Nhiễm trùng mắt không được điều trị",
                "Có thai - thận trọng",
                "Đang cho con bú - thận trọng",
            ],
        },
    },
    "Acyclovir eye ointment": {
        "contraindications_detail": {
            "tuyệt_đối": [
                "Dị ứng với acyclovir",
            ],
            "tương_đối": [
                "Tổn thương giác mạc nặng",
                "Nhiễm trùng mắt không được điều trị",
                "Có thai - thận trọng",
                "Đang cho con bú - thận trọng",
            ],
        },
    },
    "Adalimumab": {
        "contraindications_detail": {
            "tuyệt_đối": [
                "Dị ứng với adalimumab",
                "Nhiễm trùng nặng đang hoạt động",
                "Suy tim nặng (NYHA III-IV)",
            ],
            "tương_đối": [
                "Nhiễm trùng vừa - cần điều trị trước",
                "Suy tim vừa - thận trọng",
                "Bệnh thần kinh đã biết",
                "Ung thư - tăng nguy cơ",
                "Có thai - thận trọng",
                "Đang cho con bú - thận trọng",
            ],
        },
    },
    "Albendazole": {
        "contraindications_detail": {
            "tuyệt_đối": [
                "Dị ứng với albendazole",
                "Có thai",
            ],
            "tương_đối": [
                "Suy gan nặng - thận trọng",
                "Suy thận nặng - thận trọng",
                "Giảm bạch cầu - nguy cơ giảm thêm",
                "Đang cho con bú - thận trọng",
            ],
        },
    },
    "Alemtuzumab": {
        "contraindications_detail": {
            "tuyệt_đối": [
                "Dị ứng với alemtuzumab",
                "Nhiễm trùng nặng đang hoạt động",
                "HIV dương tính",
            ],
            "tương_đối": [
                "Nhiễm trùng vừa - cần điều trị trước",
                "Bệnh tự miễn - tăng nguy cơ",
                "Ung thư - tăng nguy cơ",
                "Có thai - thận trọng",
                "Đang cho con bú - thận trọng",
            ],
        },
    },
    "Alfuzosin": {
        "contraindications_detail": {
            "tuyệt_đối": [
                "Dị ứng với alfuzosin",
                "Suy gan nặng",
                "Hạ huyết áp nặng",
            ],
            "tương_đối": [
                "Suy gan vừa - thận trọng",
                "Hạ huyết áp",
                "Bệnh tim mạch - thận trọng",
                "Có thai - không áp dụng",
                "Đang cho con bú - không áp dụng",
            ],
        },
    },
    "Anastrozole": {
        "contraindications_detail": {
            "tuyệt_đối": [
                "Dị ứng với anastrozole",
                "Phụ nữ tiền mãn kinh",
                "Có thai",
            ],
            "tương_đối": [
                "Suy gan nặng - thận trọng",
                "Suy thận nặng - thận trọng",
                "Loãng xương - tăng nguy cơ",
                "Đang cho con bú - không áp dụng",
            ],
        },
    },
    "Anidulafungin": {
        "contraindications_detail": {
            "tuyệt_đối": [
                "Dị ứng với anidulafungin hoặc echinocandin",
            ],
            "tương_đối": [
                "Suy gan nặng - thận trọng",
                "Suy thận nặng - không cần giảm liều",
                "Có thai - thận trọng",
                "Đang cho con bú - thận trọng",
            ],
        },
    },
    "Anifrolumab": {
        "contraindications_detail": {
            "tuyệt_đối": [
                "Dị ứng với anifrolumab",
                "Nhiễm trùng nặng đang hoạt động",
            ],
            "tương_đối": [
                "Nhiễm trùng vừa - cần điều trị trước",
                "Bệnh tự miễn khác - tăng nguy cơ",
                "Ung thư - tăng nguy cơ",
                "Có thai - thận trọng",
                "Đang cho con bú - thận trọng",
            ],
        },
    },
    "Aripiprazole": {
        "contraindications_detail": {
            "tuyệt_đối": [
                "Dị ứng với aripiprazole",
            ],
            "tương_đối": [
                "Bệnh tim mạch - tăng nguy cơ kéo dài QT",
                "Suy gan nặng - giảm liều",
                "Suy thận nặng - thận trọng",
                "Động kinh - có thể gây co giật",
                "Đái tháo đường - tăng nguy cơ tăng đường huyết",
                "Có thai - thận trọng",
                "Đang cho con bú - thận trọng",
            ],
        },
    },
    "Artemether-lumefantrine": {
        "contraindications_detail": {
            "tuyệt_đối": [
                "Dị ứng với artemether hoặc lumefantrine",
                "Rối loạn nhịp tim nặng",
                "Có thai (3 tháng đầu)",
            ],
            "tương_đối": [
                "Bệnh tim mạch - tăng nguy cơ kéo dài QT",
                "Suy gan nặng - thận trọng",
                "Suy thận nặng - thận trọng",
                "Có thai (3 tháng giữa và cuối) - thận trọng",
                "Đang cho con bú - thận trọng",
            ],
        },
    },
})
# ======================== END BATCH 7 ========================

# ======================== BATCH 8: MIXED IMPORTANT DRUGS (CONTINUED) ========================
# Bổ sung contraindications_detail cho các thuốc quan trọng đa dạng

EXTRA_ENHANCED_FIELDS.update({
    "Artesunate": {
        "contraindications_detail": {
            "tuyệt_đối": [
                "Dị ứng với artesunate",
                "Có thai (3 tháng đầu)",
            ],
            "tương_đối": [
                "Suy gan nặng - thận trọng",
                "Suy thận nặng - thận trọng",
                "Bệnh tim mạch - thận trọng",
                "Có thai (3 tháng giữa và cuối) - thận trọng",
                "Đang cho con bú - thận trọng",
            ],
        },
    },
    "Artificial tears (Carboxymethylcellulose)": {
        "contraindications_detail": {
            "tuyệt_đối": [
                "Dị ứng với carboxymethylcellulose hoặc thành phần",
            ],
            "tương_đối": [
                "Nhiễm trùng mắt đang hoạt động",
                "Tổn thương giác mạc nặng",
            ],
        },
    },
    "Azelaic acid topical": {
        "contraindications_detail": {
            "tuyệt_đối": [
                "Dị ứng với azelaic acid",
            ],
            "tương_đối": [
                "Da bị kích ứng nặng",
                "Vết thương hở tại vùng điều trị",
                "Có thai - thận trọng",
                "Đang cho con bú - thận trọng",
            ],
        },
    },
    "Azelastine eye drops": {
        "contraindications_detail": {
            "tuyệt_đối": [
                "Dị ứng với azelastine",
            ],
            "tương_đối": [
                "Nhiễm trùng mắt đang hoạt động",
                "Tổn thương giác mạc",
                "Đeo kính áp tròng mềm",
                "Có thai - thận trọng",
                "Đang cho con bú - thận trọng",
            ],
        },
    },
    "Benzoyl peroxide topical": {
        "contraindications_detail": {
            "tuyệt_đối": [
                "Dị ứng với benzoyl peroxide",
            ],
            "tương_đối": [
                "Da bị kích ứng nặng",
                "Vết thương hở tại vùng điều trị",
                "Da nhạy cảm với ánh sáng",
                "Có thai - thận trọng",
                "Đang cho con bú - thận trọng",
            ],
        },
    },
    "Betamethasone": {
        "contraindications_detail": {
            "tuyệt_đối": [
                "Dị ứng với betamethasone hoặc corticosteroid",
                "Nhiễm trùng hệ thống không được điều trị",
                "Nhiễm nấm toàn thân",
            ],
            "tương_đối": [
                "Đái tháo đường - tăng đường huyết",
                "Tăng huyết áp",
                "Loãng xương",
                "Loét dạ dày tá tràng",
                "Suy tim nặng",
                "Suy gan nặng",
                "Suy thận nặng",
                "Có thai - thận trọng, có thể gây dị tật",
                "Đang cho con bú - thận trọng",
                "Trẻ em - ảnh hưởng đến tăng trưởng",
            ],
        },
    },
    "Ceftazidime": {
        "contraindications_detail": {
            "tuyệt_đối": [
                "Dị ứng với ceftazidime hoặc cephalosporin",
                "Tiền sử phản ứng phản vệ với beta-lactam",
            ],
            "tương_đối": [
                "Dị ứng với penicillin - thận trọng",
                "Suy thận nặng (CrCl <30) - giảm liều",
                "Suy gan nặng - thận trọng",
                "Có thai - thận trọng",
                "Đang cho con bú - thận trọng",
            ],
        },
    },
    "Celecoxib": {
        "contraindications_detail": {
            "tuyệt_đối": [
                "Dị ứng với celecoxib hoặc sulfonamide",
                "Tiền sử hen suyễn do aspirin/NSAID",
                "Loét dạ dày tá tràng đang hoạt động",
                "Xuất huyết tiêu hóa đang hoạt động",
                "Suy tim nặng (NYHA III-IV)",
                "Có thai (3 tháng cuối)",
            ],
            "tương_đối": [
                "Tiền sử loét dạ dày tá tràng",
                "Suy thận nặng (CrCl <30) - thận trọng",
                "Suy gan nặng - thận trọng",
                "Suy tim vừa - thận trọng",
                "Tăng huyết áp không kiểm soát",
                "Đang dùng thuốc chống đông",
                "Có thai (1-2 tháng đầu và giữa) - thận trọng",
                "Đang cho con bú - thận trọng",
            ],
        },
    },
})
# ======================== END BATCH 8 ========================

# ======================== BATCH PRIORITY: CONTRAINDICATIONS_DETAIL ========================
# Bổ sung contraindications_detail cho 15 thuốc ưu tiên (ICU/Emergency/Phổ biến)
# Generated automatically by add_batch_contraindications_priority.py

EXTRA_ENHANCED_FIELDS.update({
    "Digoxin": {
        "contraindications_detail": {
            "tuyệt_đối": [
                "Dị ứng với digoxin hoặc digitalis glycosides",
                "Block nhĩ-thất độ 2-3 không có máy tạo nhịp",
                "Hội chứng Wolff-Parkinson-White (WPW) với rung nhĩ",
                "Rối loạn nhịp thất nặng (ventricular fibrillation, ventricular tachycardia không kiểm soát)",
            ],
            "tương_đối": [
                "Suy thận mức độ vừa-nặng (cần giảm liều và theo dõi nồng độ)",
                "Suy tim cấp mất bù (cần ổn định trước khi dùng)",
                "Hạ kali máu, hạ magie máu (tăng nguy cơ độc tính)",
                "Nhịp tim chậm <60 lần/phút (trừ khi có máy tạo nhịp)",
            ],
        },
    },
    "Fentanyl": {
        "contraindications_detail": {
            "tuyệt_đối": [
                "Dị ứng với fentanyl hoặc opioid",
                "Suy hô hấp nặng không có hỗ trợ thở máy",
                "Bệnh nhân đang dùng MAO inhibitors (trong vòng 14 ngày)",
            ],
            "tương_đối": [
                "Suy hô hấp mạn tính, COPD nặng (cần thận trọng, theo dõi sát)",
                "Tăng áp lực nội sọ, chấn thương sọ não",
                "Suy gan nặng (giảm chuyển hóa, tăng nguy cơ tích tụ)",
                "Phụ nữ có thai (category C, tránh dùng kéo dài)",
            ],
        },
    },
    "Hydromorphone": {
        "contraindications_detail": {
            "tuyệt_đối": [
                "Dị ứng với hydromorphone hoặc opioid",
                "Suy hô hấp nặng không có hỗ trợ thở máy",
                "Tắc ruột cơ học, liệt ruột",
            ],
            "tương_đối": [
                "Suy hô hấp mạn tính, COPD nặng",
                "Tăng áp lực nội sọ",
                "Suy gan nặng (giảm chuyển hóa)",
                "Suy thận nặng (tích tụ chất chuyển hóa)",
            ],
        },
    },
    "Insulin Regular": {
        "contraindications_detail": {
            "tuyệt_đối": [
                "Dị ứng với insulin hoặc bất kỳ thành phần nào",
                "Hạ đường huyết nặng đang diễn ra",
            ],
            "tương_đối": [
                "Suy thận nặng (cần điều chỉnh liều, theo dõi sát)",
                "Suy gan nặng (giảm chuyển hóa glucose, tăng nguy cơ hạ đường huyết)",
                "Bệnh nhân không có khả năng tự theo dõi đường huyết",
            ],
        },
    },
    "Nitroglycerin": {
        "contraindications_detail": {
            "tuyệt_đối": [
                "Dị ứng với nitroglycerin hoặc nitrate",
                "Hạ huyết áp nặng (systolic <90 mmHg)",
                "Thiếu máu cơ tim cấp do hẹp động mạch chủ nặng",
                "Viêm màng ngoài tim co thắt",
                "Đang dùng phosphodiesterase-5 inhibitors (sildenafil, tadalafil, vardenafil) - nguy cơ hạ huyết áp đe dọa tính mạng",
            ],
            "tương_đối": [
                "Hạ huyết áp nhẹ-vừa (theo dõi sát, có thể cần giảm liều)",
                "Thiếu máu nặng (giảm tải oxy)",
                "Tăng áp lực nội sọ",
                "Suy thận nặng (tích tụ chất chuyển hóa)",
            ],
        },
    },
    "Phenylephrine": {
        "contraindications_detail": {
            "tuyệt_đối": [
                "Dị ứng với phenylephrine",
                "Tăng huyết áp nặng không kiểm soát",
                "Bệnh mạch vành không ổn định, nhồi máu cơ tim cấp",
            ],
            "tương_đối": [
                "Tăng huyết áp vừa (theo dõi sát)",
                "Bệnh mạch vành, rối loạn nhịp tim",
                "Cường giáp (tăng nhạy cảm với catecholamine)",
                "Bệnh nhân đang dùng MAO inhibitors",
            ],
        },
    },
    "Vasopressin": {
        "contraindications_detail": {
            "tuyệt_đối": [
                "Dị ứng với vasopressin",
            ],
            "tương_đối": [
                "Bệnh mạch vành (có thể gây co mạch vành, thiếu máu cơ tim)",
                "Bệnh mạch máu ngoại biên nặng",
                "Suy thận nặng (giảm tưới máu thận)",
                "Hạ natri máu nặng (vasopressin có thể làm nặng thêm)",
            ],
        },
    },
    "Milrinone": {
        "contraindications_detail": {
            "tuyệt_đối": [
                "Dị ứng với milrinone",
                "Rối loạn nhịp thất nặng không kiểm soát",
            ],
            "tương_đối": [
                "Hạ huyết áp nặng (milrinone có thể gây giãn mạch)",
                "Rối loạn nhịp nhĩ hoặc thất (tăng nguy cơ)",
                "Suy thận nặng (giảm thải trừ, tăng nguy cơ tích tụ)",
                "Bệnh mạch vành không ổn định",
            ],
        },
    },
    "Nesiritide": {
        "contraindications_detail": {
            "tuyệt_đối": [
                "Dị ứng với nesiritide",
                "Hạ huyết áp nặng (systolic <90 mmHg)",
                "Sốc tim",
            ],
            "tương_đối": [
                "Hạ huyết áp vừa (theo dõi sát)",
                "Bệnh mạch vành không ổn định",
                "Suy thận nặng (giảm thải trừ)",
                "Hẹp van động mạch chủ nặng",
            ],
        },
    },
    "Clevidipine": {
        "contraindications_detail": {
            "tuyệt_đối": [
                "Dị ứng với clevidipine hoặc soy/egg (chứa trong dung dịch)",
                "Suy gan nặng",
            ],
            "tương_đối": [
                "Suy thận nặng (theo dõi sát)",
                "Bệnh mạch vành không ổn định (có thể gây phản xạ nhịp nhanh)",
                "Hạ huyết áp nhẹ-vừa (theo dõi sát)",
            ],
        },
    },
    "Nitroprusside": {
        "contraindications_detail": {
            "tuyệt_đối": [
                "Dị ứng với nitroprusside",
                "Thiếu máu cơ tim cấp do hẹp động mạch chủ nặng",
                "Thiếu hụt bẩm sinh cytochrome b5 reductase (nguy cơ nhiễm độc cyanide)",
            ],
            "tương_đối": [
                "Suy thận nặng (tích tụ thiocyanate, nguy cơ độc tính)",
                "Suy gan nặng (giảm chuyển hóa cyanide)",
                "Thiếu vitamin B12 (tăng nguy cơ nhiễm độc cyanide)",
                "Tăng áp lực nội sọ",
            ],
        },
    },
    "Rocuronium": {
        "contraindications_detail": {
            "tuyệt_đối": [
                "Dị ứng với rocuronium hoặc aminosteroid neuromuscular blocking agents",
            ],
            "tương_đối": [
                "Bệnh nhược cơ (myasthenia gravis) - cần giảm liều mạnh",
                "Rối loạn chức năng thần kinh cơ khác",
                "Suy thận nặng (kéo dài thời gian tác dụng)",
                "Suy gan nặng (kéo dài thời gian tác dụng)",
            ],
        },
    },
    "Succinylcholine": {
        "contraindications_detail": {
            "tuyệt_đối": [
                "Dị ứng với succinylcholine",
                "Tiền sử hoặc nguy cơ tăng kali máu nặng (bỏng nặng, chấn thương lớn, liệt tủy sống, bệnh cơ)",
                "Bệnh nhược cơ (myasthenia gravis) - có thể gây block kéo dài",
                "Rối loạn di truyền pseudocholinesterase (block kéo dài, nguy cơ ngừng thở)",
            ],
            "tương_đối": [
                "Tăng nhãn áp (có thể làm tăng áp lực nội nhãn)",
                "Tăng áp lực nội sọ",
                "Bệnh cơ di truyền (malignant hyperthermia, Duchenne muscular dystrophy)",
                "Suy gan nặng (giảm chuyển hóa)",
            ],
        },
    },
    "Vecuronium": {
        "contraindications_detail": {
            "tuyệt_đối": [
                "Dị ứng với vecuronium hoặc aminosteroid neuromuscular blocking agents",
            ],
            "tương_đối": [
                "Bệnh nhược cơ (myasthenia gravis) - cần giảm liều mạnh",
                "Rối loạn chức năng thần kinh cơ khác",
                "Suy thận nặng (kéo dài thời gian tác dụng)",
                "Suy gan nặng (kéo dài thời gian tác dụng)",
            ],
        },
    },
    "Thiopental": {
        "contraindications_detail": {
            "tuyệt_đối": [
                "Dị ứng với thiopental hoặc barbiturate",
                "Porphyria cấp (có thể gây cơn porphyria)",
                "Suy hô hấp nặng không có hỗ trợ thở máy",
            ],
            "tương_đối": [
                "Suy hô hấp mạn tính",
                "Suy tim nặng (có thể gây hạ huyết áp)",
                "Suy gan nặng (kéo dài thời gian tác dụng)",
                "Suy thận nặng (tích tụ)",
            ],
        },
    },
})
# ======================== END BATCH PRIORITY ========================

# ======================== BATCH PRIORITY: REVERSAL_AGENTS ========================
# Bổ sung reversal_agents cho Alteplase (thuốc quan trọng còn thiếu)
# Generated automatically by add_batch_reversal_agents_priority.py

EXTRA_ENHANCED_FIELDS.update({
    "Alteplase": {
        "reversal_agents": {
            "available": False,
            "agents": [],
            "notes": "Không có thuốc giải độc đặc hiệu cho alteplase. Xử trí: ngừng truyền ngay, hỗ trợ huyết động, truyền máu và các chế phẩm máu nếu chảy máu nặng. Có thể cân nhắc tranexamic acid hoặc aminocaproic acid trong trường hợp chảy máu đe dọa tính mạng (theo guideline chuyên ngành).",
        },
    },
})
# ======================== END BATCH PRIORITY ========================

# ======================== BATCH 2: CONTRAINDICATIONS_DETAIL ========================
# Bổ sung contraindications_detail cho 15 thuốc quan trọng (Kháng sinh, Tim mạch, Thần kinh)
# Generated automatically by add_batch_contraindications_batch2.py

EXTRA_ENHANCED_FIELDS.update({
    "Cefepime": {
        "contraindications_detail": {
            "tuyệt_đối": [
                "Dị ứng với cefepime hoặc cephalosporin",
                "Dị ứng nặng với penicillin (phản ứng chéo có thể xảy ra)",
            ],
            "tương_đối": [
                "Suy thận nặng (cần điều chỉnh liều)",
                "Tiền sử viêm đại tràng do Clostridium difficile",
                "Rối loạn đông máu (cefepime có thể gây giảm prothrombin)",
            ],
        },
    },
    "Cefotaxime": {
        "contraindications_detail": {
            "tuyệt_đối": [
                "Dị ứng với cefotaxime hoặc cephalosporin",
                "Dị ứng nặng với penicillin",
            ],
            "tương_đối": [
                "Suy thận nặng (cần điều chỉnh liều)",
                "Tiền sử viêm đại tràng do C. difficile",
                "Rối loạn đông máu",
            ],
        },
    },
    "Cefuroxime": {
        "contraindications_detail": {
            "tuyệt_đối": [
                "Dị ứng với cefuroxime hoặc cephalosporin",
                "Dị ứng nặng với penicillin",
            ],
            "tương_đối": [
                "Suy thận nặng (cần điều chỉnh liều)",
                "Tiền sử viêm đại tràng do C. difficile",
            ],
        },
    },
    "Cephalexin": {
        "contraindications_detail": {
            "tuyệt_đối": [
                "Dị ứng với cephalexin hoặc cephalosporin",
                "Dị ứng nặng với penicillin",
            ],
            "tương_đối": [
                "Suy thận nặng (cần điều chỉnh liều)",
                "Tiền sử viêm đại tràng do C. difficile",
            ],
        },
    },
    "Caspofungin": {
        "contraindications_detail": {
            "tuyệt_đối": [
                "Dị ứng với caspofungin hoặc echinocandin",
            ],
            "tương_đối": [
                "Suy gan nặng (cần điều chỉnh liều)",
                "Đang dùng cyclosporine (tăng nguy cơ độc tính gan)",
            ],
        },
    },
    "Cisplatin": {
        "contraindications_detail": {
            "tuyệt_đối": [
                "Dị ứng với cisplatin hoặc platinum compounds",
                "Suy thận nặng (eGFR <30 mL/min)",
                "Giảm thính lực nặng",
            ],
            "tương_đối": [
                "Suy thận vừa (cần điều chỉnh liều và theo dõi sát)",
                "Suy tim, bệnh mạch vành",
                "Giảm bạch cầu hoặc tiểu cầu nặng",
                "Bệnh thần kinh ngoại biên",
            ],
        },
    },
    "Carboplatin": {
        "contraindications_detail": {
            "tuyệt_đối": [
                "Dị ứng với carboplatin hoặc platinum compounds",
                "Suy thận nặng (eGFR <30 mL/min)",
            ],
            "tương_đối": [
                "Suy thận vừa (cần điều chỉnh liều theo AUC)",
                "Giảm bạch cầu hoặc tiểu cầu nặng",
                "Suy gan nặng",
            ],
        },
    },
    "Baclofen": {
        "contraindications_detail": {
            "tuyệt_đối": [
                "Dị ứng với baclofen",
            ],
            "tương_đối": [
                "Suy thận nặng (tăng nguy cơ độc tính, cần giảm liều)",
                "Động kinh không kiểm soát",
                "Rối loạn tâm thần",
                "Loét dạ dày tá tràng",
            ],
        },
    },
    "Bupropion": {
        "contraindications_detail": {
            "tuyệt_đối": [
                "Dị ứng với bupropion",
                "Động kinh hoặc tiền sử động kinh",
                "Đang dùng MAO inhibitors (trong vòng 14 ngày)",
                "Rối loạn ăn uống (anorexia nervosa, bulimia nervosa)",
            ],
            "tương_đối": [
                "Tiền sử động kinh hoặc yếu tố nguy cơ co giật",
                "Chấn thương đầu, u não",
                "Rối loạn gan nặng",
                "Tăng huyết áp không kiểm soát",
            ],
        },
    },
    "Buprenorphine": {
        "contraindications_detail": {
            "tuyệt_đối": [
                "Dị ứng với buprenorphine hoặc opioid",
                "Suy hô hấp nặng không có hỗ trợ thở máy",
                "Đang dùng MAO inhibitors (trong vòng 14 ngày)",
            ],
            "tương_đối": [
                "Suy hô hấp mạn tính, COPD nặng",
                "Suy gan nặng (giảm chuyển hóa)",
                "Tăng áp lực nội sọ",
                "Phụ nữ có thai (category C)",
            ],
        },
    },
    "Candesartan": {
        "contraindications_detail": {
            "tuyệt_đối": [
                "Dị ứng với candesartan hoặc ARB",
                "Phụ nữ có thai (tháng 2-3, category D)",
                "Hẹp động mạch thận hai bên hoặc một bên ở bệnh nhân một thận",
            ],
            "tương_đối": [
                "Suy thận nặng (theo dõi chức năng thận)",
                "Hạ huyết áp",
                "Tăng kali máu",
                "Hẹp động mạch thận một bên",
            ],
        },
    },
    "Benazepril": {
        "contraindications_detail": {
            "tuyệt_đối": [
                "Dị ứng với benazepril hoặc ACE inhibitor",
                "Phụ nữ có thai (tháng 2-3, category D)",
                "Phù mạch do ACE inhibitor trước đó",
                "Hẹp động mạch thận hai bên hoặc một bên ở bệnh nhân một thận",
            ],
            "tương_đối": [
                "Suy thận nặng (theo dõi chức năng thận)",
                "Hạ huyết áp",
                "Tăng kali máu",
                "Bệnh mô liên kết (tăng nguy cơ neutropenia)",
            ],
        },
    },
    "Canagliflozin": {
        "contraindications_detail": {
            "tuyệt_đối": [
                "Dị ứng với canagliflozin hoặc SGLT2 inhibitor",
                "Suy thận nặng (eGFR <30 mL/min)",
                "Nhiễm toan ceton do đái tháo đường",
            ],
            "tương_đối": [
                "Suy thận vừa (eGFR 30-60, cần điều chỉnh liều)",
                "Suy tim nặng",
                "Nhiễm trùng đường tiết niệu tái phát",
                "Nhiễm nấm sinh dục",
            ],
        },
    },
    "Chlorpromazine": {
        "contraindications_detail": {
            "tuyệt_đối": [
                "Dị ứng với chlorpromazine hoặc phenothiazine",
                "Coma do thuốc ức chế thần kinh trung ương",
                "Giảm bạch cầu nặng",
            ],
            "tương_đối": [
                "Bệnh tim mạch nặng",
                "Động kinh",
                "Bệnh gan",
                "Parkinson",
                "Glaucoma góc đóng",
            ],
        },
    },
    "Chloroquine": {
        "contraindications_detail": {
            "tuyệt_đối": [
                "Dị ứng với chloroquine",
                "Bệnh võng mạc do chloroquine",
                "Rối loạn nhịp tim nặng",
            ],
            "tương_đối": [
                "Bệnh gan nặng",
                "Bệnh thận nặng",
                "Bệnh cơ (myopathy)",
                "Bệnh máu (porphyria)",
                "Rối loạn tâm thần",
            ],
        },
    },
})
# ======================== END BATCH 2 ========================

# ======================== BATCH 3: CONTRAINDICATIONS_DETAIL ========================
# Bổ sung contraindications_detail cho 15 thuốc quan trọng (Tim mạch, Nội tiết, Kháng sinh, Huyết học)
# Generated automatically by add_batch_contraindications_batch3.py

EXTRA_ENHANCED_FIELDS.update({
    "Codeine": {
        "contraindications_detail": {
            "tuyệt_đối": [
                "Dị ứng với codeine hoặc opioid",
                "Suy hô hấp nặng không có hỗ trợ thở máy",
                "Đang dùng MAO inhibitors (trong vòng 14 ngày)",
            ],
            "tương_đối": [
                "Suy hô hấp mạn tính, COPD nặng",
                "Tăng áp lực nội sọ",
                "Suy gan nặng (giảm chuyển hóa)",
                "Suy thận nặng",
            ],
        },
    },
    "Dipyridamole": {
        "contraindications_detail": {
            "tuyệt_đối": [
                "Dị ứng với dipyridamole",
            ],
            "tương_đối": [
                "Hạ huyết áp nặng",
                "Bệnh mạch vành không ổn định",
                "Suy tim nặng",
                "Rối loạn đông máu",
            ],
        },
    },
    "Disopyramide": {
        "contraindications_detail": {
            "tuyệt_đối": [
                "Dị ứng với disopyramide",
                "Suy tim nặng, sốc tim",
                "Block nhĩ-thất độ 2-3 không có máy tạo nhịp",
                "Suy thận nặng (eGFR <30 mL/min)",
            ],
            "tương_đối": [
                "Suy tim vừa",
                "Suy thận vừa (cần điều chỉnh liều)",
                "Bệnh mạch vành",
                "Glaucoma góc đóng",
            ],
        },
    },
    "Dofetilide": {
        "contraindications_detail": {
            "tuyệt_đối": [
                "Dị ứng với dofetilide",
                "Suy thận nặng (CrCl <20 mL/min)",
                "QT kéo dài (QTc >500 ms)",
                "Đang dùng thuốc gây kéo dài QT",
            ],
            "tương_đối": [
                "Suy thận vừa (cần điều chỉnh liều)",
                "QT kéo dài nhẹ-vừa",
                "Rối loạn điện giải (hạ kali, hạ magie)",
            ],
        },
    },
    "Doxazosin": {
        "contraindications_detail": {
            "tuyệt_đối": [
                "Dị ứng với doxazosin hoặc alpha-blocker",
            ],
            "tương_đối": [
                "Hạ huyết áp nặng",
                "Suy gan nặng",
                "Suy thận nặng",
            ],
        },
    },
    "Eplerenone": {
        "contraindications_detail": {
            "tuyệt_đối": [
                "Dị ứng với eplerenone",
                "Suy thận nặng (CrCl <30 mL/min)",
                "Tăng kali máu nặng (>5.5 mEq/L)",
                "Đang dùng thuốc ức chế CYP3A4 mạnh (ketoconazole, itraconazole)",
            ],
            "tương_đối": [
                "Suy thận vừa (theo dõi kali máu)",
                "Tăng kali máu nhẹ-vừa",
                "Suy gan nặng",
            ],
        },
    },
    "Felodipine": {
        "contraindications_detail": {
            "tuyệt_đối": [
                "Dị ứng với felodipine hoặc dihydropyridine calcium channel blocker",
            ],
            "tương_đối": [
                "Hạ huyết áp nặng",
                "Suy gan nặng (tăng nồng độ)",
                "Suy tim nặng",
            ],
        },
    },
    "Fenofibrate": {
        "contraindications_detail": {
            "tuyệt_đối": [
                "Dị ứng với fenofibrate hoặc fibrate",
                "Bệnh gan hoạt động",
                "Suy thận nặng (eGFR <30 mL/min)",
                "Bệnh túi mật",
            ],
            "tương_đối": [
                "Suy gan vừa",
                "Suy thận vừa (cần điều chỉnh liều)",
                "Rối loạn chức năng tuyến giáp",
            ],
        },
    },
    "Filgrastim": {
        "contraindications_detail": {
            "tuyệt_đối": [
                "Dị ứng với filgrastim hoặc G-CSF",
            ],
            "tương_đối": [
                "Bệnh bạch cầu cấp (AML) ở trẻ em",
                "Hội chứng rối loạn hô hấp cấp (ARDS)",
                "Lách to",
            ],
        },
    },
    "Fludrocortisone": {
        "contraindications_detail": {
            "tuyệt_đối": [
                "Dị ứng với fludrocortisone hoặc corticosteroid",
                "Nhiễm nấm hệ thống không điều trị",
            ],
            "tương_đối": [
                "Suy tim nặng",
                "Tăng huyết áp nặng",
                "Phù nề",
                "Loãng xương",
            ],
        },
    },
    "Fosphenytoin": {
        "contraindications_detail": {
            "tuyệt_đối": [
                "Dị ứng với fosphenytoin hoặc phenytoin",
                "Block nhĩ-thất độ 2-3",
            ],
            "tương_đối": [
                "Suy gan nặng (giảm chuyển hóa)",
                "Suy thận nặng",
                "Bệnh tim",
                "Rối loạn chức năng tuyến giáp",
            ],
        },
    },
    "Ganciclovir": {
        "contraindications_detail": {
            "tuyệt_đối": [
                "Dị ứng với ganciclovir",
            ],
            "tương_đối": [
                "Suy thận nặng (cần điều chỉnh liều)",
                "Giảm bạch cầu hoặc tiểu cầu nặng",
                "Suy gan nặng",
            ],
        },
    },
    "Gemfibrozil": {
        "contraindications_detail": {
            "tuyệt_đối": [
                "Dị ứng với gemfibrozil hoặc fibrate",
                "Bệnh gan hoạt động",
                "Suy thận nặng (eGFR <30 mL/min)",
                "Bệnh túi mật",
            ],
            "tương_đối": [
                "Suy gan vừa",
                "Suy thận vừa",
                "Rối loạn chức năng tuyến giáp",
            ],
        },
    },
    "Glimepiride": {
        "contraindications_detail": {
            "tuyệt_đối": [
                "Dị ứng với glimepiride hoặc sulfonylurea",
                "Đái tháo đường type 1",
                "Nhiễm toan ceton do đái tháo đường",
                "Suy thận nặng (eGFR <30 mL/min)",
            ],
            "tương_đối": [
                "Suy gan nặng (tăng nguy cơ hạ đường huyết)",
                "Suy thận vừa (cần điều chỉnh liều)",
                "Người cao tuổi (tăng nguy cơ hạ đường huyết)",
            ],
        },
    },
    "Hydralazine": {
        "contraindications_detail": {
            "tuyệt_đối": [
                "Dị ứng với hydralazine",
                "Bệnh mạch vành nặng",
                "Nhồi máu cơ tim cấp",
            ],
            "tương_đối": [
                "Suy tim nặng",
                "Bệnh mạch vành",
                "Suy gan nặng",
                "Suy thận nặng",
            ],
        },
    },
})
# ======================== END BATCH 3 ========================

# ======================== BATCH 4: CONTRAINDICATIONS_DETAIL ========================
# Bổ sung contraindications_detail cho 15 thuốc quan trọng (Kháng sinh, Tim mạch, Ung thư, Thần kinh)
# Generated automatically by add_batch_contraindications_batch4.py

EXTRA_ENHANCED_FIELDS.update({
    "Hydrocodone": {
        "contraindications_detail": {
            "tuyệt_đối": [
                "Dị ứng với hydrocodone hoặc opioid",
                "Suy hô hấp nặng không có hỗ trợ thở máy",
                "Đang dùng MAO inhibitors (trong vòng 14 ngày)",
            ],
            "tương_đối": [
                "Suy hô hấp mạn tính, COPD nặng",
                "Tăng áp lực nội sọ",
                "Suy gan nặng (giảm chuyển hóa)",
                "Suy thận nặng",
            ],
        },
    },
    "Hydroxyzine": {
        "contraindications_detail": {
            "tuyệt_đối": [
                "Dị ứng với hydroxyzine hoặc piperazine",
                "Phụ nữ có thai sớm (category C)",
            ],
            "tương_đối": [
                "Suy gan nặng",
                "Suy thận nặng",
                "Bệnh tim",
                "Glaucoma góc đóng",
            ],
        },
    },
    "Indapamide": {
        "contraindications_detail": {
            "tuyệt_đối": [
                "Dị ứng với indapamide hoặc sulfonamide",
                "Suy thận nặng (eGFR <30 mL/min)",
                "Tăng kali máu nặng",
            ],
            "tương_đối": [
                "Suy gan nặng",
                "Suy thận vừa (theo dõi điện giải)",
                "Đái tháo đường",
                "Gout",
            ],
        },
    },
    "Indomethacin": {
        "contraindications_detail": {
            "tuyệt_đối": [
                "Dị ứng với indomethacin hoặc NSAID",
                "Loét dạ dày tá tràng tiến triển",
                "Suy thận nặng",
                "Suy tim nặng",
            ],
            "tương_đối": [
                "Suy thận vừa",
                "Suy gan vừa",
                "Tăng huyết áp",
                "Bệnh mạch vành",
            ],
        },
    },
    "Irbesartan": {
        "contraindications_detail": {
            "tuyệt_đối": [
                "Dị ứng với irbesartan hoặc ARB",
                "Phụ nữ có thai (tháng 2-3, category D)",
                "Hẹp động mạch thận hai bên hoặc một bên ở bệnh nhân một thận",
            ],
            "tương_đối": [
                "Suy thận nặng (theo dõi chức năng thận)",
                "Hạ huyết áp",
                "Tăng kali máu",
            ],
        },
    },
    "Isosorbide mononitrate": {
        "contraindications_detail": {
            "tuyệt_đối": [
                "Dị ứng với isosorbide mononitrate hoặc nitrate",
                "Hạ huyết áp nặng (systolic <90 mmHg)",
                "Thiếu máu cơ tim cấp do hẹp động mạch chủ nặng",
                "Đang dùng phosphodiesterase-5 inhibitors",
            ],
            "tương_đối": [
                "Hạ huyết áp nhẹ-vừa",
                "Thiếu máu nặng",
                "Tăng áp lực nội sọ",
            ],
        },
    },
    "Isradipine": {
        "contraindications_detail": {
            "tuyệt_đối": [
                "Dị ứng với isradipine hoặc dihydropyridine calcium channel blocker",
            ],
            "tương_đối": [
                "Hạ huyết áp nặng",
                "Suy gan nặng",
                "Suy tim nặng",
            ],
        },
    },
    "Ivabradine": {
        "contraindications_detail": {
            "tuyệt_đối": [
                "Dị ứng với ivabradine",
                "Nhịp tim chậm <60 lần/phút",
                "Suy tim cấp",
                "Hạ huyết áp nặng",
            ],
            "tương_đối": [
                "Suy thận nặng (CrCl <15 mL/min)",
                "Suy gan vừa-nặng",
                "Rối loạn nhịp tim",
            ],
        },
    },
    "Ketoprofen": {
        "contraindications_detail": {
            "tuyệt_đối": [
                "Dị ứng với ketoprofen hoặc NSAID",
                "Loét dạ dày tá tràng tiến triển",
                "Suy thận nặng",
                "Suy tim nặng",
            ],
            "tương_đối": [
                "Suy thận vừa",
                "Suy gan vừa",
                "Tăng huyết áp",
                "Bệnh mạch vành",
            ],
        },
    },
    "Ketorolac": {
        "contraindications_detail": {
            "tuyệt_đối": [
                "Dị ứng với ketorolac hoặc NSAID",
                "Loét dạ dày tá tràng tiến triển",
                "Suy thận nặng",
                "Chảy máu đang hoạt động",
                "Phẫu thuật bắc cầu động mạch vành",
            ],
            "tương_đối": [
                "Suy thận vừa",
                "Suy gan vừa",
                "Người cao tuổi (>65 tuổi)",
                "Rối loạn đông máu",
            ],
        },
    },
    "Labetalol": {
        "contraindications_detail": {
            "tuyệt_đối": [
                "Dị ứng với labetalol hoặc beta-blocker",
                "Block nhĩ-thất độ 2-3 không có máy tạo nhịp",
                "Suy tim mất bù cấp",
                "Hen phế quản nặng",
            ],
            "tương_đối": [
                "Nhịp tim chậm",
                "Hạ huyết áp",
                "Suy tim vừa",
                "COPD vừa",
            ],
        },
    },
    "Lacosamide": {
        "contraindications_detail": {
            "tuyệt_đối": [
                "Dị ứng với lacosamide",
            ],
            "tương_đối": [
                "Suy thận nặng (CrCl <30 mL/min, cần điều chỉnh liều)",
                "Suy gan nặng",
                "Rối loạn nhịp tim",
                "Bệnh tim",
            ],
        },
    },
    "Lisinopril": {
        "contraindications_detail": {
            "tuyệt_đối": [
                "Dị ứng với lisinopril hoặc ACE inhibitor",
                "Phụ nữ có thai (tháng 2-3, category D)",
                "Phù mạch do ACE inhibitor trước đó",
                "Hẹp động mạch thận hai bên hoặc một bên ở bệnh nhân một thận",
            ],
            "tương_đối": [
                "Suy thận nặng (theo dõi chức năng thận)",
                "Hạ huyết áp",
                "Tăng kali máu",
                "Bệnh mô liên kết",
            ],
        },
    },
    "Losartan": {
        "contraindications_detail": {
            "tuyệt_đối": [
                "Dị ứng với losartan hoặc ARB",
                "Phụ nữ có thai (tháng 2-3, category D)",
                "Hẹp động mạch thận hai bên hoặc một bên ở bệnh nhân một thận",
            ],
            "tương_đối": [
                "Suy thận nặng (theo dõi chức năng thận)",
                "Hạ huyết áp",
                "Tăng kali máu",
            ],
        },
    },
    "Lovastatin": {
        "contraindications_detail": {
            "tuyệt_đối": [
                "Dị ứng với lovastatin hoặc statin",
                "Bệnh gan hoạt động",
                "Phụ nữ có thai hoặc cho con bú",
                "Đang dùng thuốc ức chế CYP3A4 mạnh (cyclosporine, itraconazole, ketoconazole)",
            ],
            "tương_đối": [
                "Suy gan vừa",
                "Suy thận nặng",
                "Rối loạn chức năng tuyến giáp",
                "Tiền sử bệnh cơ",
            ],
        },
    },
})
# ======================== END BATCH 4 ========================

# ======================== BATCH 5: PREGNANCY & LACTATION SAFETY ========================
EXTRA_ENHANCED_FIELDS.update({
    "Metformin": {
        "pregnancy_lactation": {
            "fda_category": "B",
            "pregnancy_details": (
                "Thường được xem là an toàn và hiệu quả trong thai kỳ, đặc biệt cho đái tháo đường thai kỳ (GDM) và PCOS. "
                "Không thấy bằng chứng gây quái thai. Tuy nhiên, insulin vẫn là lựa chọn đầu tay chính thức trong nhiều hướng dẫn."
            ),
            "lactation": {
                "safety": "Compatible",
                "details": "Bài tiết vào sữa mẹ với lượng rất nhỏ (0.1-1% liều mẹ). Không ghi nhận tác dụng phụ ở trẻ bú mẹ.",
                "recommendation": "Có thể sử dụng. An toàn khi cho con bú.",
            },
        },
    },
    "Amlodipine": {
        "pregnancy_lactation": {
            "fda_category": "C",
            "pregnancy_details": (
                "Chưa có nghiên cứu đầy đủ trên người. Trên động vật có ghi nhận độc tính khi dùng liều cao. "
                "Chỉ sử dụng khi lợi ích vượt trội nguy cơ. Nifedipine hoặc Methyldopa thường được ưu tiên hơn cho tăng huyết áp thai kỳ."
            ),
            "lactation": {
                "safety": "Caution",
                "details": "Chưa rõ mức độ bài tiết vào sữa mẹ. Các thuốc chẹn kênh canxi khác (như Nifedipine) có thông tin an toàn rõ ràng hơn.",
                "recommendation": "Thận trọng. Cân nhắc chuyển sang thuốc an toàn hơn nếu có thể, hoặc theo dõi trẻ.",
            },
        },
    },
    "Atorvastatin": {
        "pregnancy_lactation": {
            "fda_category": "X",
            "pregnancy_details": (
                "CHỐNG CHỈ ĐỊNH. Statin can thiệp vào tổng hợp cholesterol cần thiết cho sự phát triển của thai nhi. "
                "Ngưng thuốc ngay lập tức nếu phát hiện có thai."
            ),
            "lactation": {
                "safety": "Avoid",
                "details": "Có khả năng bài tiết vào sữa mẹ và gây ảnh hưởng đến chuyển hóa lipid của trẻ.",
                "recommendation": "Không sử dụng. Ngưng cho con bú hoặc ngưng thuốc.",
            },
        },
    },
    "Cephalexin": {
        "pregnancy_lactation": {
            "fda_category": "B",
            "pregnancy_details": (
                "An toàn. Được sử dụng rộng rãi trong thai kỳ để điều trị nhiễm trùng tiểu và hô hấp. Không có bằng chứng gây hại."
            ),
            "lactation": {
                "safety": "Compatible",
                "details": "Bài tiết vào sữa mẹ lượng nhỏ. An toàn cho trẻ bú mẹ.",
                "recommendation": "Có thể sử dụng. Theo dõi tiêu chảy ở trẻ.",
            },
        },
    },
    "Omeprazole": {
        "pregnancy_lactation": {
            "fda_category": "C",
            "pregnancy_details": (
                "Dữ liệu lớn trên người không cho thấy nguy cơ dị tật. Tuy nhiên FDA xếp loại C do một số nghiên cứu động vật. "
                "Thường được dùng khi các thuốc kháng H2 không hiệu quả."
            ),
            "lactation": {
                "safety": "Compatible",
                "details": "Bài tiết vào sữa mẹ lượng nhỏ (khoảng 7% liều mẹ). Bị phá hủy phần lớn bởi acid dạ dày của trẻ.",
                "recommendation": "Có thể sử dụng. Được coi là an toàn.",
            },
        },
    },
    "Loratadine": {
        "pregnancy_lactation": {
            "fda_category": "B",
            "pregnancy_details": (
                "An toàn. Là lựa chọn thuốc kháng histamin thế hệ 2 ưu tiên trong thai kỳ.",
            ),
            "lactation": {
                "safety": "Compatible",
                "details": "Bài tiết vào sữa mẹ lượng rất nhỏ. AAP xếp vào nhóm thuốc an toàn.",
                "recommendation": "Có thể sử dụng.",
            },
        },
    },
})


__all__ = ["EXTRA_ENHANCED_FIELDS"]


