"""
Enhanced fields overrides - Respiratory
"""
from typing import Any, Dict


RESPIRATORY_ENHANCED_FIELDS: Dict[str, Dict[str, Any]] = {
        # ======================== RESPIRATORY – THEOPHYLLINE ========================
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

}
