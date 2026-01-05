"""
Anesthesia Induction Agents
"""

INDUCTION_AGENTS = {
    "Propofol": {
        "group": "Anesthesia - Induction Agent (IV)",
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
        "monitoring": ["Huyết áp (dễ tụt HA)", "Hô hấp (SpO2, EtCO2)", "Dấu hiệu PRIS nếu truyền lâu"]
    },

    "Ketamine": {
        "group": "Anesthesia - Dissociative Anesthetic",
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
        "monitoring": ["Huyết áp (có thể tăng)", "Nhịp tim", "Trạng thái tâm thần khi tỉnh"]
    },

    "Etomidate": {
        "group": "Anesthesia - Induction Agent",
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
        "monitoring": ["Huyết áp", "Dấu hiệu suy thượng thận (nếu dùng truyền liên tục - Không khuyến cáo)"]
    }
}
