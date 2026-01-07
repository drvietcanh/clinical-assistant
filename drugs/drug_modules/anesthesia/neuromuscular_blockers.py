"""
Anesthesia Neuromuscular Blockers (Paralytics)
"""

NEUROMUSCULAR_BLOCKERS = {
    "Succinylcholine": {
        "group": "Anesthesia - Neuromuscular Blocker (Depolarizing)",
        "vietnamese_name": "Succinylcholine, Suxamethonium",
        "brand_names": {
            "common": ["Anectine", "Quelicin"],
            "vietnam": ["Succinylcholine", "Suxamethonium"]
        },
        "administration": ["IV", "IM"],
        "indications": [
            "Đặt nội khí quản nhanh (RSI - Rapid Sequence Intubation) - thuốc lựa chọn hàng đầu do tác dụng rất nhanh.",
            "Giãn cơ ngắn hạn"
        ],
        "contraindications": {
            "absolute": [
                "Tiền sử sốt cao ác tính (Malignant Hyperthermia)",
                "Tăng Kali máu (Hyperkalemia) hoặc nguy cơ cao (bỏng nặng, chấn thương tủy, bất động lâu ngày)",
                "Bệnh cơ (Myopathies), Loạn dưỡng cơ Duchenne",
                "Tăng nhãn áp xuyên thấu (Open eye injury) - thận trọng"
            ]
        },
        "contraindications_detail": {
            "tuyệt_đối": [
                "Tiền sử sốt cao ác tính (Malignant Hyperthermia)",
                "Tăng Kali máu (Hyperkalemia) hoặc nguy cơ cao (bỏng nặng, chấn thương tủy, bất động lâu ngày)",
                "Bệnh cơ (Myopathies), Loạn dưỡng cơ Duchenne",
                "Dị ứng với Succinylcholine"
            ],
            "tương_đối": [
                "Tăng nhãn áp xuyên thấu (Open eye injury) - thận trọng",
                "Suy gan - thận trọng, có thể kéo dài tác dụng",
                "Suy thận - thận trọng, có thể kéo dài tác dụng",
                "Bệnh nhân cao tuổi - thận trọng",
                "Phụ nữ có thai - thận trọng, chỉ dùng khi thực sự cần thiết"
            ]
        },
        "dosage": {
            "intubation_iv": "1-1.5 mg/kg IV.",
            "intubation_im": "3-4 mg/kg IM (nếu không có đường truyền, tác dụng chậm hơn).",
            "notes": "Gây rung giật cơ (fasciculations) trước khi liệt cơ. Tác dụng rất nhanh (30-60s), kéo dài ngắn (4-6 phút)."
        },
        "side_effects": [
            "Tăng Kali máu (nguy hiểm ngừng tim)",
            "Nhịp chậm (Bradycardia) - đặc biệt liều lặp lại hoặc ở trẻ em",
            "Sốt cao ác tính (Malignant Hyperthermia) - hiếm gặp nhưng tử vong cao",
            "Đau cơ sau mổ",
            "Tăng áp lực nội sọ/nhãn áp/dạ dày thoáng qua"
        ],
        "mechanism_of_action": "Depolarizing blocker. Gắn vào thụ thể Acetylcholine gây khử cực kéo dài (liệt mềm).",
        "monitoring": ["Nhịp tim", "Kali máu", "Dấu hiệu sốt cao ác tính (tăng CO2 đột ngột, cứng cơ)"],
        "renal_adjustment": {
            "normal": "Không cần chỉnh liều",
            "30_60": "Không cần chỉnh liều. Succinylcholine chuyển hóa bởi pseudocholinesterase trong huyết tương.",
            "under_30": "Không cần chỉnh liều. Succinylcholine chuyển hóa bởi pseudocholinesterase trong huyết tương.",
            "dialysis": "Không cần chỉnh liều. Succinylcholine chuyển hóa bởi pseudocholinesterase trong huyết tương.",
            "notes": "Succinylcholine chuyển hóa bởi pseudocholinesterase trong huyết tương, không phụ thuộc gan/thận. Tuy nhiên, suy thận có thể làm giảm pseudocholinesterase, kéo dài tác dụng."
        },
        "drug_interactions": {
            "major": [
                {
                    "drug": "Thuốc ức chế pseudocholinesterase (Echothiophate, Neostigmine)",
                    "mechanism": "Ức chế enzyme chuyển hóa Succinylcholine",
                    "effect": "Kéo dài tác dụng liệt cơ đáng kể",
                    "management": "Tránh dùng Succinylcholine nếu đã dùng thuốc ức chế pseudocholinesterase. Dùng thuốc giãn cơ khác."
                }
            ],
            "moderate": [
                {
                    "drug": "Aminoglycosides, Magnesium",
                    "mechanism": "Tăng cường tác dụng liệt cơ",
                    "effect": "Kéo dài tác dụng liệt cơ",
                    "management": "Giảm liều Succinylcholine khi dùng cùng."
                }
            ],
            "minor": []
        },
        "reversal_agents": {
            "available": False,
            "agents": [],
            "notes": "Không có antidote đặc hiệu. Succinylcholine tự phân hủy nhanh (4-6 phút). Điều trị quá liều chủ yếu là hỗ trợ hô hấp cho đến khi thuốc hết tác dụng. Dantrolene dùng cho sốt cao ác tính."
        }
    },

    "Rocuronium": {
        "group": "Anesthesia - Neuromuscular Blocker (Non-depolarizing)",
        "vietnamese_name": "Rocuronium, Esmeron",
        "brand_names": {
            "common": ["Zemuron", "Esmeron"],
            "vietnam": ["Rocuronium", "Esmeron"]
        },
        "administration": ["IV"],
        "indications": [
            "Đặt nội khí quản (có thể dùng cho RSI liều cao nếu chống chỉ định Succinylcholine)",
            "Duy trì giãn cơ trong phẫu thuật"
        ],
        "contraindications": {
            "absolute": ["Dị ứng"]
        },
        "contraindications_detail": {
            "tuyệt_đối": [
                "Dị ứng với Rocuronium hoặc aminosteroid neuromuscular blockers"
            ],
            "tương_đối": [
                "Suy gan - thận trọng, có thể kéo dài tác dụng",
                "Suy thận - thận trọng, có thể kéo dài tác dụng",
                "Bệnh nhân cao tuổi - thận trọng",
                "Phụ nữ có thai - thận trọng, chỉ dùng khi thực sự cần thiết"
            ]
        },
        "dosage": {
            "intubation_standard": "0.6 mg/kg IV. (Tác dụng sau 90s).",
            "rsi_intubation": "1.2 mg/kg IV. (Tác dụng nhanh ~60s, tương đương Succinylcholine nhưng kéo dài lâu hơn).",
            "maintenance": "0.1-0.2 mg/kg IV.",
            "notes": "Thời gian tác dụng trung bình (30-40 phút)."
        },
        "side_effects": [
            "Dị ứng/Phản vệ (hiếm)",
            "Không gây giải phóng Histamin đáng kể (ưu điểm so với Atracurium)",
            "Không ảnh hưởng tim mạch đáng kể"
        ],
        "reversal_agents": {
            "available": True,
            "agents": [
                {
                    "agent": "Sugammadex (Bridion)",
                    "dose": "2-16 mg/kg IV tùy độ sâu của block",
                    "mechanism": "Đảo ngược chọn lọc bằng cách chelate Rocuronium",
                    "effect": "Đảo ngược nhanh và hiệu quả",
                    "notes": "Lựa chọn hàng đầu cho Rocuronium. Tác dụng nhanh, an toàn."
                },
                {
                    "agent": "Neostigmine + Atropine",
                    "dose": "Neostigmine 0.04-0.07 mg/kg + Atropine 0.02 mg/kg IV",
                    "mechanism": "Ức chế acetylcholinesterase, tăng acetylcholine",
                    "effect": "Đảo ngược block khi đã hết block sâu (TOF > 0)",
                    "notes": "Chỉ dùng khi TOF đã có ít nhất 1-2 twitches. Không hiệu quả khi block sâu."
                }
            ],
            "notes": "Sugammadex là lựa chọn hàng đầu cho Rocuronium. Neostigmine chỉ dùng khi không có Sugammadex và block đã hết sâu."
        },
        "mechanism_of_action": "Non-depolarizing (Aminosteroid). Cạnh tranh với Acetylcholine tại thụ thể Nicotinic.",
        "monitoring": ["TOF (Train-of-Four) monitoring"],
        "renal_adjustment": {
            "normal": "Không cần chỉnh liều",
            "30_60": "Không cần chỉnh liều. Rocuronium chủ yếu thải trừ qua gan và thận.",
            "under_30": "Thận trọng, có thể kéo dài tác dụng. Giảm liều nếu cần.",
            "dialysis": "Thận trọng, có thể kéo dài tác dụng. Giảm liều nếu cần.",
            "notes": "Rocuronium thải trừ qua gan (70%) và thận (30%). Suy thận có thể kéo dài tác dụng. Cần theo dõi TOF và điều chỉnh liều."
        },
        "drug_interactions": {
            "major": [
                {
                    "drug": "Aminoglycosides, Vancomycin, Magnesium",
                    "mechanism": "Tăng cường tác dụng liệt cơ",
                    "effect": "Kéo dài tác dụng liệt cơ",
                    "management": "Giảm liều Rocuronium khi dùng cùng. Theo dõi TOF chặt chẽ."
                }
            ],
            "moderate": [
                {
                    "drug": "Thuốc ức chế CYP450",
                    "mechanism": "Ức chế chuyển hóa Rocuronium",
                    "effect": "Kéo dài tác dụng liệt cơ",
                    "management": "Giảm liều Rocuronium khi dùng cùng."
                }
            ],
            "minor": []
        }
    },

    "Cisatracurium": {
        "group": "Anesthesia - Neuromuscular Blocker (Non-depolarizing)",
        "vietnamese_name": "Cisatracurium, Nimbex",
        "brand_names": {
            "common": ["Nimbex"],
            "vietnam": ["Cisatracurium", "Nimbex"]
        },
        "administration": ["IV"],
        "indications": [
            "Duy trì giãn cơ (đặc biệt bệnh nhân suy gan, suy thận)",
            "Đặt nội khí quản (không phải lựa chọn hàng đầu cho RSI)"
        ],
        "contraindications": {
            "absolute": ["Dị ứng với Cisatracurium hoặc benzylisoquinolinium neuromuscular blockers"]
        },
        "contraindications_detail": {
            "tuyệt_đối": [
                "Dị ứng với Cisatracurium hoặc benzylisoquinolinium neuromuscular blockers"
            ],
            "tương_đối": [
                "Bệnh nhân cao tuổi - thận trọng",
                "Phụ nữ có thai - thận trọng, chỉ dùng khi thực sự cần thiết"
            ]
        },
        "dosage": {
            "intubation": "0.15-0.2 mg/kg IV.",
            "maintenance": "0.03 mg/kg IV mỗi 20 phút.",
            "infusion_icu": "1-3 mcg/kg/phút.",
            "notes": "Hoffman degradation (tự phân hủy trong huyết tương), KHÔNG phụ thuộc Gan/Thận -> Lựa chọn số 1 cho bệnh nhân Suy gan/Thận."
        },
        "side_effects": [
            "Ít gây giải phóng Histamin hơn Atracurium.",
            "Dị ứng (hiếm)"
        ],
        "mechanism_of_action": "Non-depolarizing (Benzylisoquinolinium).",
        "renal_adjustment": {
            "normal": "Không cần chỉnh liều",
            "30_60": "Không cần chỉnh liều. Cisatracurium tự phân hủy qua Hoffman degradation, không phụ thuộc thận.",
            "under_30": "Không cần chỉnh liều. Cisatracurium tự phân hủy qua Hoffman degradation, không phụ thuộc thận.",
            "dialysis": "Không cần chỉnh liều. Cisatracurium tự phân hủy qua Hoffman degradation, không phụ thuộc thận.",
            "notes": "Cisatracurium tự phân hủy qua Hoffman degradation trong huyết tương, KHÔNG phụ thuộc gan/thận. Lựa chọn số 1 cho bệnh nhân suy gan/thận."
        },
        "drug_interactions": {
            "major": [
                {
                    "drug": "Aminoglycosides, Vancomycin, Magnesium",
                    "mechanism": "Tăng cường tác dụng liệt cơ",
                    "effect": "Kéo dài tác dụng liệt cơ",
                    "management": "Giảm liều Cisatracurium khi dùng cùng. Theo dõi TOF chặt chẽ."
                }
            ],
            "moderate": [],
            "minor": []
        },
        "reversal_agents": {
            "available": True,
            "agents": [
                {
                    "agent": "Neostigmine + Atropine",
                    "dose": "Neostigmine 0.04-0.07 mg/kg + Atropine 0.02 mg/kg IV",
                    "mechanism": "Ức chế acetylcholinesterase, tăng acetylcholine",
                    "effect": "Đảo ngược block khi đã hết block sâu (TOF > 0)",
                    "notes": "Chỉ dùng khi TOF đã có ít nhất 1-2 twitches. Không hiệu quả khi block sâu."
                }
            ],
            "notes": "Neostigmine là lựa chọn chính cho Cisatracurium. Chỉ dùng khi TOF đã có ít nhất 1-2 twitches. Sugammadex không có tác dụng với Cisatracurium."
        },
            "risk_flags": {
                "high_alert": False,
                "narrow_therapeutic_index": False,
                "bleeding_risk": False,
                "organ_toxicity": [],
                "qt_prolongation": False,
                "hepatotoxicity": False,
                "nephrotoxicity": False,
                "requires_monitoring": [],
            },
            "guideline_tags": [
                "FDA Drug Information",
                "UpToDate Drug Information",
            ],
            "monitoring": ["TOF monitoring"]
        }
}
