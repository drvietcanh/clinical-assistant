"""
Anesthesia Induction Agents
"""

INDUCTION_AGENTS = {
    "Propofol": {
        "group": "Anesthesia - Induction Agent (IV)",

        "pregnancy": "B - Không có bằng chứng về nguy cơ ở người",
        "vietnamese_name": "Propofol, Diprivan",
        "brand_names": {
            "common": ["Diprivan"],
            "vietnam": ["Propofol", "Diprivan", "Propofol-Lipuro"]
        },
        "administration": ["IV"],
        "indications": [
            "Khởi mê (Induction) và duy trì mê (Maintenance)",
            "An thần (Sedation) cho thủ thuật hoặc thở máy ICU"
        ],
        "contraindications": {
            "absolute": [
                "Dị ứng với Propofol hoặc thành phần (dầu đậu nành, trứng)",
                "Rối loạn chuyển hóa chất béo nặng"
            ]
        },
        "contraindications_detail": {
            "tuyệt_đối": [
                "Dị ứng với Propofol hoặc thành phần (dầu đậu nành, trứng, lecithin)",
                "Rối loạn chuyển hóa chất béo nặng",
                "Sốc nặng không kiểm soát được"
            ],
            "tương_đối": [
                "Suy gan nặng - thận trọng, có thể cần giảm liều",
                "Suy thận nặng - thận trọng, theo dõi chức năng thận",
                "Bệnh nhân cao tuổi - giảm liều, tăng nguy cơ tụt huyết áp",
                "Bệnh nhân có bệnh tim mạch - tăng nguy cơ tụt huyết áp",
                "Phụ nữ có thai - thận trọng, chỉ dùng khi thực sự cần thiết"
            ]
        },
        "dosage": {
            "induction_adult": "2-2.5 mg/kg IV (người già/suy kiệt: 1-1.5 mg/kg). Tiêm chậm 40mg/10s.",
            "maintenance_anesthesia": "100-200 mcg/kg/phút (6-12 mg/kg/giờ).",
            "sedation_icu": "5-50 mcg/kg/phút (0.3-3 mg/kg/giờ).",
            "notes": "Giảm liều ở người già, huyết động không ổn định. Gây đau khi tiêm (có thể mixed Lidocaine)."
        },
        "side_effects": [
            "Tụt huyết áp (đặc biệt khi tiêm nhanh hoặc giảm thể tích tuần hoàn)",
            "Ngừng thở (Apnea) - cần hỗ trợ hô hấp ngay",
            "Hội chứng truyền Propofol (PRIS) - hiếm gặp nhưng tử vong cao (dùng liều cao kéo dài >48h): Toan chuyển hóa, Rhabdomyolysis, Suy tim.",
            "Đau tại chỗ tiêm"
        ],
        "pharmacokinetics": {
            "onset": "Rất nhanh (30-45 giấy)",
            "duration": "Ngắn (3-10 phút)",
            "metabolism": "Gan (nhanh)",
            "elimination": "Thận"
        },
        "is_vesicant": False,
        "monitoring": ["Huyết áp (dễ tụt HA)", "Hô hấp (SpO2, EtCO2)", "Dấu hiệu PRIS nếu truyền lâu"],
        "renal_adjustment": {
            "normal": "Không cần chỉnh liều",
            "30_60": "Không cần chỉnh liều. Propofol chủ yếu chuyển hóa qua gan.",
            "under_30": "Không cần chỉnh liều. Propofol chủ yếu chuyển hóa qua gan.",
            "dialysis": "Không cần chỉnh liều. Propofol không được lọc sạch qua thẩm phân máu.",
            "notes": "Propofol chủ yếu chuyển hóa qua gan. Không cần điều chỉnh liều ở suy thận. Tuy nhiên, cần thận trọng ở bệnh nhân suy thận nặng do tăng nguy cơ tụt huyết áp."
        },
        "drug_interactions": {
            "major": [
                {
                    "drug": "Benzodiazepines, Opioids",
                    "mechanism": "Tăng cường tác dụng an thần và ức chế hô hấp",
                    "effect": "Tăng nguy cơ ức chế hô hấp, tụt huyết áp",
                    "management": "Giảm liều Propofol khi dùng cùng. Theo dõi hô hấp và huyết áp chặt chẽ."
                }
            ],
            "moderate": [
                {
                    "drug": "Thuốc ức chế CYP450 (Cimetidine, Erythromycin)",
                    "mechanism": "Ức chế chuyển hóa Propofol",
                    "effect": "Tăng nồng độ Propofol, kéo dài tác dụng",
                    "management": "Giảm liều Propofol khi dùng cùng."
                }
            ],
            "minor": []
        },
        "reversal_agents": {
            "available": False,
            "agents": [],
            "notes": "Không có antidote đặc hiệu. Điều trị quá liều chủ yếu là hỗ trợ: ngừng thuốc, hỗ trợ hô hấp, điều chỉnh huyết áp. Flumazenil không có tác dụng với Propofol."
        }
    },

    "Ketamine": {
        "group": "Anesthesia - Dissociative Anesthetic",

        "pregnancy": "C - Nguy cơ không thể loại trừ",
        "vietnamese_name": "Ketamine, Ketalar",
        "brand_names": {
            "common": ["Ketalar"],
            "vietnam": ["Ketamine", "Ketalar"]
        },
        "administration": ["IV", "IM"],
        "indications": [
            "Khởi mê (đặc biệt bệnh nhân hen phế quản hoặc sốc - do kích thích giao cảm)",
            "Giảm đau (Analgesia) liều thấp",
            "An thần cho thủ thuật (Procedural Sedation)"
        ],
        "contraindications": {
            "absolute": [
                "Tăng huyết áp nặng không kiểm soát",
                "Phình mạch não, tăng áp lực nội sọ (tranh cãi, nhưng thường thận trọng)",
                "Tâm thần phân liệt (có thể gây ảo giác)"
            ]
        },
        "contraindications_detail": {
            "tuyệt_đối": [
                "Tăng huyết áp nặng không kiểm soát",
                "Phình mạch não, tăng áp lực nội sọ (tranh cãi, nhưng thường thận trọng)",
                "Tâm thần phân liệt (có thể gây ảo giác)",
                "Dị ứng với Ketamine"
            ],
            "tương_đối": [
                "Suy gan - thận trọng, có thể cần giảm liều",
                "Suy thận - thận trọng, theo dõi chức năng thận",
                "Bệnh nhân cao tuổi - thận trọng với tác dụng tâm thần",
                "Bệnh nhân có bệnh tim mạch - thận trọng với tác dụng tăng huyết áp",
                "Phụ nữ có thai - thận trọng, chỉ dùng khi thực sự cần thiết"
            ]
        },
        "dosage": {
            "induction_iv": "1-2 mg/kg IV.",
            "induction_im": "4-6 mg/kg IM.",
            "analgesia_iv": "0.1-0.3 mg/kg IV.",
            "sedation": "0.5-1 mg/kg IV.",
            "notes": "Có thể gây tăng tiết đàm nhớt (dùng kèm Atropine/Glycopyrrolate)."
        },
        "side_effects": [
            "Tăng nhịp tim, Tăng huyết áp (tác dụng giống giao cảm)",
            "Ảo giác, ác mộng (Emergence reactions) - giảm bằng Benzodiazepines",
            "Tăng áp lực nội sọ (nhẹ)",
            "Tăng tiết nước bọt"
        ],
        "mechanism_of_action": "NMDA Receptor Antagonist. Gây mê phân ly (Dissociative anesthesia) - bệnh nhân có thể mở mắt nhưng không nhận thức đau.",
        "monitoring": ["Huyết áp (có thể tăng)", "Nhịp tim", "Trạng thái tâm thần khi tỉnh"],
        "renal_adjustment": {
            "normal": "Không cần chỉnh liều",
            "30_60": "Không cần chỉnh liều. Ketamine chủ yếu chuyển hóa qua gan.",
            "under_30": "Không cần chỉnh liều. Ketamine chủ yếu chuyển hóa qua gan.",
            "dialysis": "Không cần chỉnh liều. Ketamine không được lọc sạch qua thẩm phân máu.",
            "notes": "Ketamine chủ yếu chuyển hóa qua gan. Không cần điều chỉnh liều ở suy thận."
        },
        "drug_interactions": {
            "major": [
                {
                    "drug": "Benzodiazepines",
                    "mechanism": "Giảm ảo giác và ác mộng khi tỉnh",
                    "effect": "Giảm tác dụng phụ tâm thần của Ketamine",
                    "management": "Có thể dùng cùng để giảm ảo giác. Thường dùng Midazolam trước hoặc sau Ketamine."
                }
            ],
            "moderate": [
                {
                    "drug": "Thuốc ức chế CYP450",
                    "mechanism": "Ức chế chuyển hóa Ketamine",
                    "effect": "Tăng nồng độ Ketamine, kéo dài tác dụng",
                    "management": "Giảm liều Ketamine khi dùng cùng."
                }
            ],
            "minor": []
        },
        "reversal_agents": {
            "available": False,
            "agents": [],
            "notes": "Không có antidote đặc hiệu. Điều trị quá liều chủ yếu là hỗ trợ: ngừng thuốc, hỗ trợ hô hấp nếu cần. Benzodiazepines có thể giúp giảm ảo giác."
        }
    },

    "Etomidate": {
        "group": "Anesthesia - Induction Agent",

        "pregnancy": "C - Nguy cơ không thể loại trừ",
        "vietnamese_name": "Etomidate, Amidate",
        "brand_names": {
            "common": ["Amidate"],
            "vietnam": ["Etomidate", "Lipuro"]
        },
        "administration": ["IV"],
        "indications": [
            "Khởi mê (đặc biệt bệnh nhân tim mạch, huyết động không ổn định - ít ảnh hưởng huyết áp)"
        ],
        "contraindications": {
            "absolute": [
                "Dị ứng",
                "Suy vỏ thượng thận (Adrenal suppression) - Etomidate ức chế tổng hợp Cortisol"
            ]
        },
        "contraindications_detail": {
            "tuyệt_đối": [
                "Dị ứng với Etomidate",
                "Suy vỏ thượng thận (Adrenal suppression) - Etomidate ức chế tổng hợp Cortisol",
                "Sốc nhiễm khuẩn - CHỐNG CHỈ ĐỊNH do ức chế tổng hợp Cortisol"
            ],
            "tương_đối": [
                "Suy gan - thận trọng, có thể cần giảm liều",
                "Suy thận - thận trọng, theo dõi chức năng thận",
                "Bệnh nhân cao tuổi - thận trọng",
                "Phụ nữ có thai - thận trọng, chỉ dùng khi thực sự cần thiết"
            ]
        },
        "dosage": {
            "induction": "0.2-0.3 mg/kg IV.",
            "notes": "Tiêm chậm. Rất ổn định huyết động."
        },
        "side_effects": [
            "Ức chế vỏ thượng thận (dù chỉ 1 liều) - thận trọng ở bệnh nhân Sốc nhiễm khuẩn",
            "Myoclonus (Rung giật cơ) khi khởi mê",
            "Buồn nôn/Nôn sau mổ (PONV) - tỷ lệ cao",
            "Đau tại chỗ tiêm"
        ],
        "mechanism_of_action": "GABA Modulator.",
        "monitoring": ["Huyết áp", "Dấu hiệu suy thượng thận (nếu dùng truyền liên tục - Không khuyến cáo)"],
        "renal_adjustment": {
            "normal": "Không cần chỉnh liều",
            "30_60": "Không cần chỉnh liều. Etomidate chủ yếu chuyển hóa qua gan.",
            "under_30": "Không cần chỉnh liều. Etomidate chủ yếu chuyển hóa qua gan.",
            "dialysis": "Không cần chỉnh liều. Etomidate không được lọc sạch qua thẩm phân máu.",
            "notes": "Etomidate chủ yếu chuyển hóa qua gan. Không cần điều chỉnh liều ở suy thận."
        },
        "drug_interactions": {
            "major": [],
            "moderate": [
                {
                    "drug": "Thuốc ức chế CYP450",
                    "mechanism": "Ức chế chuyển hóa Etomidate",
                    "effect": "Tăng nồng độ Etomidate, kéo dài tác dụng",
                    "management": "Giảm liều Etomidate khi dùng cùng."
                }
            ],
            "minor": []
        },
        "reversal_agents": {
            "available": False,
            "agents": [],
            "notes": "Không có antidote đặc hiệu. Điều trị quá liều chủ yếu là hỗ trợ: ngừng thuốc, hỗ trợ hô hấp nếu cần. Có thể cần bổ sung Corticosteroid nếu có dấu hiệu suy thượng thận."
        }
    }
}
