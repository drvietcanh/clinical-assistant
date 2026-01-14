"""
Fluids & Colloids (Dịch truyền & Dung dịch keo)
"""

FLUIDS_DRUGS = {
    "Sodium Chloride 0.9%":     {
        "group": "Fluids - Crystalloid (Dịch tinh thể)",
        "vietnamese_name": "Nước muối sinh lý 0.9% (Normal Saline)",
        "brand_names": {
            "common": [
                "Normal Saline"
    ],
            "vietnam": [
                "Natri Clorid 0.9% (nhiều hãng)"
    ],
        },
        "administration": [
            "IV (Truyền tĩnh mạch)"
    ],
        "indications": [
            "Hồi sức dịch (Fluid resuscitation)",
            "Mất nước (Dehydration)",
            "Pha loãng thuốc",
            "Rửa vết thương"
    ],
        "contraindications": [
            "Tăng Natri máu (Hypernatremia)",
            "Thừa dịch (Fluid overload), Suy tim sung huyết nặng"
    ],
        "dosage": {
            "resuscitation_adult": "500-1000 ml bolus nhanh (nếu sốc).",
            "maintenance": "30 ml/kg/24h (hoặc theo công thức 4-2-1).",
            "notes": """Chứa Na+ 154 mEq/L, Cl- 154 mEq/L. Dùng lượng lớn gây toan chuyển hóa tăng Clo (Hyperchloremic acidosis).""",
        },
        "monitoring": [
            "Điện giải (Na, Cl)",
            "Cân bằng dịch",
            "Dấu hiệu quá tải dịch"
        ],
        "side_effects": [],
        "interactions": [],
        "pregnancy": "C - Nguy cơ không thể loại trừ. An toàn khi sử dụng đúng chỉ định""mechanism_of_action": "",
        "precautions": [],
        "pharmacokinetics": {
        },
        "storage": "",
        "black_box_warnings": None,
        "drug_interactions": {
            "major": [],
            "moderate": [],
            "minor": [],
        },
        "contraindications_detail": {
            "tuyệt_đối": [
                "Tăng natri máu nặng (hypernatremia).",
                "Quá tải dịch nặng/suy tim sung huyết mất bù.",
            ],
            "tương_đối": [
                "Suy tim, suy thận, xơ gan với cổ trướng (nguy cơ quá tải dịch).",
            ],
        },
        "pregnancy_lactation": {
            "fda_category": "",
            "pregnancy_details": "",
            "lactation": {
                "safety": "",
                "details": "",
                "recommendation": "",
            },
        },
        "hepatic_adjustment": {
            "mild": "",
            "moderate": "",
            "severe": "",
            "notes": "",
        },
        "renal_adjustment": {
            "normal": "Không cần chỉnh liều; điều chỉnh theo tình trạng huyết động và cân bằng dịch.",
            "30_60": "Thận trọng; giảm tốc độ/khối lượng truyền, theo dõi sát dấu hiệu quá tải dịch.",
            "under_30": "Thận trọng cao; ưu tiên bolus nhỏ, theo dõi lâm sàng và siêu âm tại giường.",
            "dialysis": "Thận trọng; phối hợp với đội lọc máu để điều chỉnh dịch.",
            "notes": "NaCl 0.9% có thể gây toan chuyển hóa tăng Cl nếu dùng lượng lớn, đặc biệt ở bệnh nhân suy thận.",
        },
        "overdose_management": {
            "symptoms": [],
            "antidote": "",
            "treatment": [],
            "monitoring": "",
        },
        "reversal_agents": {
            "available": False,
            "agents": [],
            "notes": "Không có antidote đặc hiệu; xử trí quá liều bằng ngừng truyền, lợi tiểu, và hỗ trợ hô hấp/tuần hoàn.",
        },
        "administration_instructions": {
            "iv": {
                "infusion_rate": "Tùy mục tiêu hồi sức; bolus nhanh trong sốc, chậm hơn trong bù dịch thông thường.",
                "notes": "Theo dõi áp lực tĩnh mạch trung tâm, siêu âm tại giường, và dấu hiệu quá tải dịch.",
            },
        },
        "references": {
            "primary_sources": [],
            "last_updated": "",
            "evidence_level": "",
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
            ]
    },
    "Ringer Lactate":     {
        "group": "Fluids - Crystalloid (Dịch tinh thể)",
        "vietnamese_name": "Dung dịch Ringer Lactate (Hartmann)",
        "brand_names": {
            "common": [
                "Lactated Ringer's",
                "Hartmann's Solution"
    ],
            "vietnam": [
                "Ringer Lactate"
    ],
        },
        "administration": [
            "IV"
    ],
        "indications": [
            "Hồi sức dịch (ưu tiên trong chấn thương, bỏng, mất máu)",
            "Mất nước"
    ],
        "contraindications": [
            "Tăng Kali máu (chứa K+ 4 mEq/L - thận trọng, không chống chỉ định tuyệt đối trừ khi K+ rất cao)",
            "Chấn thương sọ não (tranh cãi - do áp lực thẩm thấu hơi thấp hơn NS, có thể gây phù não nhẹ)"
    ],
        "dosage": {
            "resuscitation": "Tương tự NaCl 0.9%.",
            "notes": """Sinh lý hơn NaCl 0.9%. Chứa Lactate (chuyển hóa thành Bicarbonate) -> Giúp kiềm hóa máu nhẹ. KHÔNG dùng pha loãng máu (chứa Ca2+ gây đông máu nếu mixed).""",
        },
        "monitoring": [
            "Điện giải",
            "Lactate (không ảnh hưởng đáng kể lactate máu trừ khi suy gan nặng)"
        ],
        "side_effects": [],
        "interactions": [],
        "pregnancy": "C - Nguy cơ không thể loại trừ. An toàn khi sử dụng đúng chỉ định""mechanism_of_action": "",
        "precautions": [],
        "pharmacokinetics": {
        },
        "storage": "",
        "black_box_warnings": None,
        "drug_interactions": {
            "major": [],
            "moderate": [],
            "minor": [],
        },
        "contraindications_detail": {
            "tuyệt_đối": [],
            "tương_đối": [
                "Tăng kali máu đáng kể.",
                "Chấn thương sọ não nặng (tranh cãi; có thể ưu tiên NaCl 0.9%).",
                "Suy thận nặng (nguy cơ tích lũy kali).",
            ],
        },
        "pregnancy_lactation": {
            "fda_category": "",
            "pregnancy_details": "",
            "lactation": {
                "safety": "",
                "details": "",
                "recommendation": "",
            },
        },
        "hepatic_adjustment": {
            "mild": "",
            "moderate": "",
            "severe": "",
            "notes": "",
        },
        "renal_adjustment": {
            "normal": "Không cần chỉnh liều; điều chỉnh theo huyết động.",
            "30_60": "Thận trọng do chứa K+; giảm tổng lượng dịch nếu nguy cơ quá tải.",
            "under_30": "Thận trọng cao; giới hạn liều và theo dõi sát K+ và cân bằng dịch.",
            "dialysis": "Dùng thận trọng; phối hợp với đội lọc máu.",
            "notes": "Ringer Lactate chứa kali và lactate; cần thận trọng ở bệnh nhân suy thận/suy gan nặng.",
        },
        "overdose_management": {
            "symptoms": [],
            "antidote": "",
            "treatment": [],
            "monitoring": "",
        },
        "reversal_agents": {
            "available": False,
            "agents": [],
            "notes": "Không có antidote đặc hiệu; xử trí quá liều bằng ngừng truyền, lợi tiểu, và hỗ trợ hô hấp/tuần hoàn.",
        },
        "administration_instructions": {
            "iv": {
                "infusion_rate": "Tương tự NaCl 0.9%; điều chỉnh theo huyết động và cân bằng dịch.",
                "notes": "Tránh dùng để pha máu do chứa Ca2+; không phối hợp trực tiếp với chế phẩm máu.",
            },
        },
        "references": {
            "primary_sources": [],
            "last_updated": "",
            "evidence_level": "",
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
            ]
    },
    "Albumin (Human)":     {
        "group": "Fluids - Colloid (Dung dịch keo)",
        "vietnamese_name": "Albumin người (5%, 20%, 25%)",
        "brand_names": {
            "common": [
                "Albuminar",
                "Albuked"
    ],
            "vietnam": [
                "Human Albumin (Baxalta/Grifols/Biotest)"
    ],
        },
        "administration": [
            "IV"
    ],
        "indications": [
            "Giảm Albumin máu nặng có triệu chứng (phù, cổ trướng kháng trị)",
            "Hồi sức dịch trong sốc (lựa chọn hàng 2 sau tinh thể)",
            "Hội chứng gan thận (Hepatorenal syndrome) - kết hợp Terlipressin",
            "Sốc bỏng (sau 24h đầu)"
    ],
        "contraindications": [
            "Suy tim nặng (nguy cơ quá tải tuần hoàn cao)",
            "Thiếu máu nặng (cần hồng cầu hơn)"
    ],
        "dosage": {
            "hypoalbuminemia": "Albumin 20-25%: 50-100 ml (10-20g) IV chậm.",
            "hepatorenal": "1g/kg (max 100g) ngày đầu, sau đó 20-40g/ngày.",
            "notes": """Là chế phẩm máu -> Nguy cơ (dù thấp) lây nhiễm. Rất đắt tiền. Kéo nước vào lòng mạch mạnh (đặc biệt loại 20-25%).""",
        },
        "side_effects": [
            "Quá tải dịch (Pulmonary edema)",
            "Phản ứng dị ứng (hiếm)"
        ],
        "storage": "Nhiệt độ phòng (thường <30 độ C).",
        "interactions": [],
        "pregnancy": "C - Nguy cơ không thể loại trừ. An toàn khi sử dụng đúng chỉ định""mechanism_of_action": "",
        "monitoring": [],
        "precautions": [],
        "pharmacokinetics": {
        },
        "black_box_warnings": None,
        "drug_interactions": {
            "major": [],
            "moderate": [],
            "minor": [],
        },
        "contraindications_detail": {
            "tuyệt_đối": [
                "Suy tim sung huyết nặng hoặc quá tải tuần hoàn rõ rệt.",
            ],
            "tương_đối": [
                "Thiếu máu nặng cần truyền khối hồng cầu thay vì albumin đơn thuần.",
            ],
        },
        "pregnancy_lactation": {
            "fda_category": "",
            "pregnancy_details": "",
            "lactation": {
                "safety": "",
                "details": "",
                "recommendation": "",
            },
        },
        "hepatic_adjustment": {
            "mild": "",
            "moderate": "",
            "severe": "",
            "notes": "",
        },
        "renal_adjustment": {
            "normal": "Không cần chỉnh liều; điều chỉnh theo huyết động và mục tiêu lâm sàng.",
            "30_60": "Thận trọng; theo dõi dấu hiệu quá tải dịch và chức năng thận.",
            "under_30": "Thận trọng; giảm tốc độ truyền, theo dõi sát nước tiểu và dấu hiệu phù phổi.",
            "dialysis": "Thận trọng; phối hợp với đội lọc máu để tránh quá tải thể tích.",
            "notes": "Albumin kéo nước vào lòng mạch mạnh, dễ gây quá tải tuần hoàn nếu truyền nhanh/liều cao.",
        },
        "overdose_management": {
            "symptoms": [],
            "antidote": "",
            "treatment": [],
            "monitoring": "",
        },
        "reversal_agents": {
            "available": False,
            "agents": [],
            "notes": "Không có antidote đặc hiệu; xử trí quá liều bằng ngừng truyền, lợi tiểu, hỗ trợ hô hấp/tuần hoàn.",
        },
        "administration_instructions": {
            "iv": {
                "infusion_rate": "Truyền tĩnh mạch chậm, đặc biệt ở bệnh nhân suy tim/suy thận.",
                "notes": "Theo dõi sát huyết áp, nhịp tim, SpO₂, và dấu hiệu phù phổi trong và sau truyền.",
            },
        },
        "references": {
            "primary_sources": [],
            "last_updated": "",
            "evidence_level": "",
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
            ]
    },
    "HES 130/0.4":     {
        "group": "Fluids - Colloid (Cao phân tử tổng hợp)",
        "vietnamese_name": "Hydroxyethyl Starch (Voluven, HES)",
        "brand_names": {
            "common": [
                "Voluven",
                "Tetraspan"
    ],
            "vietnam": [
                "Voluven 6%",
                "Tetraspan 6%"
    ],
        },
        "administration": [
            "IV"
    ],
        "indications": [
            "Hồi sức dịch trong giảm thể tích tuần hoàn (Hypovolemia) do mất máu cấp (Chỉ dùng khi tinh thể không đủ)"
    ],
        "contraindications": [
            "Nhiễm trùng huyết (Sepsis) - CHỐNG CHỈ ĐỊNH (tăng nguy cơ tổn thương thận và tử vong)",
            "Suy thận",
            "Bỏng nặng",
            "Xuất huyết não"
    ],
        "dosage": {
            "max_dose": "Tối đa 30-50 ml/kg/ngày (tùy loại).",
            "notes": """CẢNH BÁO: Nguy cơ tổn thương thận (UKI) và rối loạn đông máu. Hạn chế sử dụng, đặc biệt ở ICU/Sepsis.""",
        },
        "black_box_warnings": """Tăng nguy cơ tử vong và tổn thương thận cần lọc máu ở bệnh nhân nhiễm trùng huyết và bệnh nhân nặng (ICU).""",
        "monitoring": [
            "Chức năng thận (Creatinine)",
            "Đông máu"
        ],
        "side_effects": [],
        "interactions": [],
        "pregnancy": "C - Nguy cơ không thể loại trừ. Thận trọng trong thai kỳ""mechanism_of_action": "",
        "precautions": [],
        "pharmacokinetics": {
        },
        "storage": "",
        "drug_interactions": {
            "major": [],
            "moderate": [],
            "minor": [],
        },
        "contraindications_detail": {
            "tuyệt_đối": [
                "Nhiễm trùng huyết (sepsis) cần hồi sức dịch.",
                "Bệnh nhân ICU nặng cần hồi sức dịch (trừ một số chỉ định rất chọn lọc).",
            ],
            "tương_đối": [
                "Suy thận cấp hoặc mạn.",
                "Bỏng nặng, xuất huyết não.",
            ],
        },
        "pregnancy_lactation": {
            "fda_category": "",
            "pregnancy_details": "",
            "lactation": {
                "safety": "",
                "details": "",
                "recommendation": "",
            },
        },
        "hepatic_adjustment": {
            "mild": "",
            "moderate": "",
            "severe": "",
            "notes": "",
        },
        "renal_adjustment": {
            "normal": "Thận trọng; dùng liều thấp nhất có hiệu quả trong thời gian ngắn nhất.",
            "30_60": "Tránh nếu có lựa chọn khác; nếu buộc phải dùng thì theo dõi sát chức năng thận và đông máu.",
            "under_30": "Tránh sử dụng do nguy cơ tổn thương thận rất cao.",
            "dialysis": "Chống chỉ định thực tế; tránh dùng.",
            "notes": "HES liên quan rõ với tăng nguy cơ tổn thương thận cấp và nhu cầu lọc máu, đặc biệt ở bệnh nhân sepsis/ICU.",
        },
        "overdose_management": {
            "symptoms": [],
            "antidote": "",
            "treatment": [],
            "monitoring": "",
        },
        "reversal_agents": {
            "available": False,
            "agents": [],
            "notes": "Không có antidote đặc hiệu; xử trí bằng ngừng truyền, hỗ trợ huyết động, điều trị rối loạn đông máu, và lọc máu nếu cần.",
        },
        "administration_instructions": {
            "iv": {
                "infusion_rate": "Truyền tĩnh mạch theo phác đồ; không vượt quá liều tối đa/ngày.",
                "notes": "Chỉ dùng khi tinh thể không đủ; tuân thủ khuyến cáo an toàn mới nhất.",
            },
        },
        "references": {
            "primary_sources": [],
            "last_updated": "",
            "evidence_level": "",
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
            ]
    },
}
