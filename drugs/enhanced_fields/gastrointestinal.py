"""
Enhanced fields overrides - Gastrointestinal
"""
from typing import Any, Dict


GASTROINTESTINAL_ENHANCED_FIELDS: Dict[str, Dict[str, Any]] = {
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

}
