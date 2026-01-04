"""
Other Antidepressants (Tetracyclic, NDRI, etc.)
"""

OTHER_ANTIDEPRESSANTS_DRUGS = {
    "Bupropion": {
        "group": "Psychiatry - NDRI (Norepinephrine-Dopamine Reuptake Inhibitor)",
        "vietnamese_name": "Bupropion, Wellbutrin, Zyban",
        "administration": ["PO"],
        "indications": [
            "Trầm cảm",
            "Cai thuốc lá (Zyban)",
            "Rối loạn cảm xúc theo mùa (SAD)",
            "Rối loạn tăng động giảm chú ý (ADHD) - off-label"
        ],
        "contraindications": [
            "Dùng MAO inhibitor",
            "Động kinh hoặc tiền sử động kinh",
            "Rối loạn ăn uống (chán ăn, cuồng ăn)",
            "Dị ứng bupropion",
            "Sử dụng thuốc giảm co giật ngưỡng thấp (ví dụ: benzodiazepine ngừng đột ngột)"
        ],
        "dosage": {
            "adult_depression_immediate": "100mg x 2 lần/ngày, tăng đến 100mg x 3 lần/ngày (tối đa 450mg/ngày)",
            "adult_depression_sr": "150mg x 2 lần/ngày (tối đa 400mg/ngày)",
            "adult_depression_xl": "150mg x 1 lần/ngày, tăng đến 300mg x 1 lần/ngày (tối đa 450mg/ngày)",
            "adult_smoking_cessation": "150mg x 2 lần/ngày (Zyban, SR) trong 7-12 tuần",
            "notes": "Nguy cơ co giật tăng với liều >450mg/ngày. Không chia liều quá 150mg/lần (immediate release)."
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "Thận trọng",
            "under_30": "Thận trọng, có thể giảm liều"
        },
        "side_effects": [
            "Mất ngủ (phổ biến)",
            "Khô miệng",
            "Nhức đầu",
            "Buồn nôn",
            "Chóng mặt",
            "Kích động",
            "Co giật (nguy cơ tăng với liều cao, >450mg/ngày)",
            "Tăng huyết áp (hiếm)",
            "Phát ban (hiếm)"
        ],
        "interactions": [
            "MAO inhibitors: nguy cơ tăng huyết áp nặng",
            "CYP2B6 inhibitors: tăng nồng độ bupropion",
            "Thuốc giảm ngưỡng co giật: tăng nguy cơ co giật",
            "Levodopa, amantadine: tăng nguy cơ tác dụng phụ dopaminergic"
        ],
        "pregnancy": "C",
        "mechanism_of_action": "NDRI (Norepinephrine-Dopamine Reuptake Inhibitor) - ức chế tái hấp thu norepinephrine và dopamine, tăng nồng độ các chất dẫn truyền thần kinh này trong synap. Không ảnh hưởng đến serotonin (khác với SSRIs, SNRIs). Đặc điểm: ít tác dụng phụ tình dục hơn SSRIs, không gây tăng cân (thậm chí có thể giảm cân), kích thích nhẹ (có thể gây mất ngủ). Được dùng trong điều trị trầm cảm và cai thuốc lá (giảm cảm giác thèm nicotine).",
        "monitoring": [
            "Triệu chứng trầm cảm",
            "Dấu hiệu co giật (nguy cơ tăng với liều cao, >450mg/ngày)",
            "Huyết áp (hiếm tăng huyết áp)",
            "Mất ngủ, kích động",
            "Cân nặng (có thể giảm nhẹ)",
            "Dấu hiệu nhiễm trùng (hiếm giảm bạch cầu)"
        ],
        "precautions": [
            "KHÔNG được ngừng đột ngột (nguy cơ hội chứng cai) - giảm liều dần dần",
            "Nguy cơ co giật tăng với liều >450mg/ngày - không vượt quá liều này",
            "CHỐNG CHỈ ĐỊNH ở bệnh nhân có động kinh hoặc tiền sử động kinh",
            "CHỐNG CHỈ ĐỊNH ở bệnh nhân có rối loạn ăn uống (chán ăn, cuồng ăn)",
            "Thận trọng ở bệnh nhân dùng thuốc giảm ngưỡng co giật",
            "Mất ngủ phổ biến → uống buổi sáng, tránh uống buổi tối",
            "Kích thích nhẹ → có thể gây kích động, lo âu",
            "Tránh dùng với MAO inhibitors (nguy cơ tăng huyết áp nặng)",
            "Không chia liều quá 150mg/lần (immediate release) để giảm nguy cơ co giật",
            "Cai thuốc lá: bắt đầu 1-2 tuần trước ngày bỏ thuốc, tiếp tục 7-12 tuần"
        ],
        "pharmacokinetics": {
            "half_life": "14 giờ (immediate), 21 giờ (SR), 24 giờ (XL)",
            "onset": "1-2 tuần",
            "duration": "Dài (do half-life dài)",
            "protein_binding": "84%",
            "metabolism": "Gan (chuyển hóa qua CYP2B6 thành hydroxybupropion - có hoạt tính)",
            "clearance": "Gan (chuyển hóa), thận (thải trừ một phần)"
        },
        "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm, tránh ánh sáng",
        "black_box_warnings": "Nguy cơ co giật. Nguy cơ tăng với liều >450mg/ngày, liều đơn >150mg (immediate release), tiền sử động kinh, rối loạn ăn uống, sử dụng thuốc giảm ngưỡng co giật. KHÔNG vượt quá 450mg/ngày. KHÔNG chia liều quá 150mg/lần (immediate release).",
        "drug_interactions": {
            "major": [
                {
                    "drug": "MAO inhibitors (phenelzine, tranylcypromine, selegiline)",
                    "mechanism": "Tăng giải phóng norepinephrine, nguy cơ tăng huyết áp nặng",
                    "effect": "Tăng huyết áp nặng, có thể gây đột quỵ, tử vong",
                    "management": "CHỐNG CHỈ ĐỊNH TUYỆT ĐỐI. Ngừng MAO inhibitor ít nhất 14 ngày trước khi bắt đầu bupropion."
                },
                {
                    "drug": "Thuốc giảm ngưỡng co giật (ví dụ: benzodiazepine ngừng đột ngột, rượu ngừng đột ngột)",
                    "mechanism": "Tác dụng hiệp đồng giảm ngưỡng co giật",
                    "effect": "Tăng nguy cơ co giật đáng kể",
                    "management": "CHỐNG CHỈ ĐỊNH hoặc thận trọng cực kỳ. Tránh dùng cùng."
                }
            ],
            "moderate": [
                {
                    "drug": "CYP2B6 inhibitors (ticlopidine, clopidogrel)",
                    "mechanism": "Ức chế chuyển hóa bupropion qua CYP2B6",
                    "effect": "Tăng nồng độ bupropion, tăng nguy cơ co giật",
                    "management": "Thận trọng. Giảm liều bupropion. Theo dõi dấu hiệu co giật."
                },
                {
                    "drug": "Levodopa, Amantadine",
                    "mechanism": "Tác dụng hiệp đồng dopaminergic",
                    "effect": "Tăng tác dụng phụ dopaminergic (kích động, loạn thần)",
                    "management": "Thận trọng. Theo dõi dấu hiệu kích động, loạn thần."
                }
            ],
            "minor": []
        },
        "contraindications": {
            "tuyệt_đối": [
                "Dùng MAO inhibitor (nguy cơ tăng huyết áp nặng)",
                "Động kinh hoặc tiền sử động kinh",
                "Rối loạn ăn uống (chán ăn, cuồng ăn)",
                "Dị ứng bupropion",
                "Sử dụng thuốc giảm ngưỡng co giật"
            ],
            "tương_đối": [
                "Suy gan nặng - thận trọng (chuyển hóa qua gan)",
                "Suy thận nặng - thận trọng",
                "Tiền sử chấn thương đầu - tăng nguy cơ co giật",
                "Mang thai (category C) - thận trọng, chỉ dùng nếu lợi ích > nguy cơ",
                "Liều >450mg/ngày - tăng nguy cơ co giật"
            ]
        },
        "pregnancy_lactation": {
            "fda_category": "C",
            "pregnancy_details": "Bupropion là category C. Chứng cứ về an toàn trong thai kỳ còn hạn chế. Chỉ dùng nếu lợi ích điều trị vượt trội nguy cơ.",
            "lactation": {
                "safety": "Compatible with monitoring",
                "details": "Bupropion bài tiết vào sữa mẹ ở nồng độ thấp. Có thể gây tác dụng phụ ở trẻ (kích động, mất ngủ).",
                "recommendation": "Có thể dùng khi cho con bú với theo dõi chặt chẽ trẻ. Theo dõi dấu hiệu kích động, mất ngủ ở trẻ."
            }
        },
        "hepatic_adjustment": {
            "mild": "Không cần điều chỉnh liều, nhưng theo dõi chặt chẽ chức năng gan",
            "moderate": "Thận trọng, có thể giảm liều nhẹ",
            "severe": "Thận trọng cực kỳ hoặc tránh dùng (chuyển hóa qua gan)",
            "notes": "Bupropion chuyển hóa qua gan (CYP2B6). Suy gan có thể làm giảm chuyển hóa, tăng nguy cơ co giật."
        },
        "overdose_management": {
            "symptoms": [
                "Co giật (phổ biến trong quá liều)",
                "Triệu chứng thần kinh: kích động, loạn thần, hôn mê",
                "Rối loạn tim mạch: nhịp nhanh, rối loạn nhịp",
                "Rối loạn hô hấp: suy hô hấp (hiếm)"
            ],
            "antidote": "Không có antidote đặc hiệu",
            "treatment": [
                "Đánh giá đường thở, hô hấp, tuần hoàn. Hỗ trợ hô hấp nếu cần",
                "Rửa dạ dày nếu trong vòng 1-2 giờ sau uống",
                "Than hoạt tính: 1g/kg (tối đa 50-100g) nếu trong vòng 1-2 giờ",
                "Điều trị co giật: Benzodiazepine (diazepam, lorazepam), nếu cần: phenobarbital, phenytoin",
                "Theo dõi liên tục: ý thức, hô hấp, tim mạch, ECG",
                "Hỗ trợ hô hấp: thở máy nếu suy hô hấp",
                "Điều trị rối loạn nhịp tim nếu có"
            ],
            "monitoring": "Theo dõi liên tục ý thức, hô hấp, tim mạch, ECG, dấu hiệu co giật trong ít nhất 24 giờ"
        },
        "reversal_agents": {
            "available": False,
            "agents": []
        },
        "administration_instructions": {
            "oral": {
                "with_food": "Có thể uống với hoặc không có thức ăn. Uống với thức ăn có thể giảm buồn nôn.",
                "timing": "Immediate release: 2-3 lần/ngày, cách nhau ít nhất 6 giờ, không quá 150mg/lần. SR: 2 lần/ngày, cách nhau ít nhất 8 giờ. XL: 1 lần/ngày buổi sáng. Uống buổi sáng để tránh mất ngủ. KHÔNG ngừng đột ngột - giảm liều dần dần."
            }
        },
        "references": {
            "primary_sources": [
                "FDA Drug Label - Wellbutrin (bupropion), Zyban (bupropion)",
                "UpToDate - Bupropion: Drug information",
                "Lexicomp - Bupropion"
            ],
            "last_updated": "2025-02-05",
            "evidence_level": "A"
        },
        "risk_flags": {
            "high_alert": True,
            "narrow_therapeutic_index": False,
            "icu_critical_care_only": False,
            "bleeding_risk": None,
            "organ_toxicity": {"neurological": "Seizures - Black Box Warning (dose-related, >450mg/day)", "cardiovascular": "Hypertension (rare)"},
            "qt_prolongation": False,
            "hepatotoxicity": False,
            "nephrotoxicity": False,
            "requires_monitoring": ["Seizure risk (Black Box Warning - contraindicated in epilepsy, eating disorders)", "Blood pressure (rare hypertension)", "Dose limit: max 450mg/day, max 150mg per dose (immediate release)"],
            "look_alike_sound_alike": ["Bupropion", "Buspirone"]
        },
        "guideline_tags": [
            "FDA Black Box Warning - Seizures (dose-related, contraindicated in epilepsy)",
            "FDA Black Box Warning - Contraindicated in Eating Disorders",
            "APA Guidelines - Depression",
            "APA Guidelines - Smoking Cessation"
        ],
        "last_updated": "2025-02-18"
    },
    
    "Mirtazapine": {
        "group": "Psychiatry - Tetracyclic Antidepressant",
        "vietnamese_name": "Mirtazapine, Remeron",
        "administration": ["PO"],
        "indications": [
            "Trầm cảm",
            "Rối loạn lo âu",
            "Mất ngủ (do tác dụng an thần)",
            "Chán ăn (do tăng cảm giác thèm ăn)"
        ],
        "contraindications": [
            "Dùng MAO inhibitor",
            "Dị ứng mirtazapine",
            "Suy gan nặng"
        ],
        "dosage": {
            "adult_initial": "15mg x 1 lần/ngày (uống trước khi ngủ)",
            "adult_maintenance": "15-45mg x 1 lần/ngày",
            "adult_max": "45mg/ngày",
            "notes": "Tác dụng an thần mạnh → uống trước khi ngủ. Tăng cân phổ biến."
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "Thận trọng",
            "under_30": "Thận trọng, có thể giảm liều"
        },
        "side_effects": [
            "Buồn ngủ (phổ biến, đặc biệt khi bắt đầu)",
            "Tăng cân (phổ biến - do tăng cảm giác thèm ăn)",
            "Khô miệng",
            "Tăng cholesterol, triglyceride",
            "Giảm bạch cầu (hiếm, nhưng nguy hiểm)",
            "Chóng mặt",
            "Tăng men gan (hiếm)"
        ],
        "interactions": [
            "MAO inhibitors: nguy cơ serotonin syndrome",
            "Benzodiazepine, rượu: tăng tác dụng an thần",
            "CYP2D6 inhibitors: tăng nồng độ mirtazapine"
        ],
        "pregnancy": "C",
        "mechanism_of_action": "Tetracyclic antidepressant, cơ chế đa dạng: 1) Đối vận thụ thể alpha-2 adrenergic (tăng giải phóng norepinephrine và serotonin). 2) Đối vận thụ thể 5-HT2 và 5-HT3 (giảm tác dụng phụ serotonin, tăng tác dụng qua 5-HT1). 3) Đối vận thụ thể histamine H1 (gây an thần, tăng cảm giác thèm ăn). Đặc điểm: tác dụng an thần mạnh (do đối vận H1), tăng cân phổ biến, ít tác dụng phụ tình dục hơn SSRIs.",
        "monitoring": [
            "Triệu chứng trầm cảm, lo âu",
            "Cân nặng (tăng cân phổ biến)",
            "Công thức máu (CBC) - hiếm giảm bạch cầu, nhưng nguy hiểm",
            "Cholesterol, triglyceride (có thể tăng)",
            "Chức năng gan (ALT, AST) - hiếm viêm gan",
            "Dấu hiệu nhiễm trùng (giảm bạch cầu)",
            "Buồn ngủ, mệt mỏi (phổ biến khi bắt đầu)"
        ],
        "precautions": [
            "KHÔNG được ngừng đột ngột (nguy cơ hội chứng cai) - giảm liều dần dần",
            "Tác dụng an thần mạnh → uống trước khi ngủ, thận trọng khi lái xe",
            "Tăng cân phổ biến - tư vấn bệnh nhân về chế độ ăn và tập luyện",
            "Nguy cơ giảm bạch cầu (hiếm, nhưng nguy hiểm) - theo dõi công thức máu",
            "Tăng cholesterol, triglyceride - theo dõi lipid máu",
            "Thận trọng ở bệnh nhân suy gan (giảm liều)",
            "Tránh dùng với MAO inhibitors (nguy cơ serotonin syndrome)",
            "Tránh rượu, benzodiazepine (tăng tác dụng an thần)",
            "Khởi đầu với liều thấp (15mg) để giảm tác dụng phụ"
        ],
        "pharmacokinetics": {
            "half_life": "20-40 giờ (dài)",
            "onset": "1-2 tuần",
            "duration": "Dài (do half-life dài, dùng 1 lần/ngày)",
            "protein_binding": "85%",
            "metabolism": "Gan (chuyển hóa qua CYP1A2, CYP2D6, CYP3A4)",
            "clearance": "Gan (chuyển hóa), thận (thải trừ một phần)"
        },
        "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm, tránh ánh sáng",
        "black_box_warnings": "Nguy cơ giảm bạch cầu (agranulocytosis) - rất hiếm nhưng có thể gây tử vong. Theo dõi công thức máu. Ngừng ngay nếu có dấu hiệu nhiễm trùng (sốt, đau họng, loét miệng).",
        "drug_interactions": {
            "major": [
                {
                    "drug": "MAO inhibitors (phenelzine, tranylcypromine, selegiline)",
                    "mechanism": "Tăng giải phóng serotonin, nguy cơ serotonin syndrome",
                    "effect": "Serotonin syndrome (kích động, tăng thân nhiệt, co giật, có thể tử vong)",
                    "management": "CHỐNG CHỈ ĐỊNH TUYỆT ĐỐI. Ngừng MAO inhibitor ít nhất 14 ngày trước khi bắt đầu mirtazapine."
                }
            ],
            "moderate": [
                {
                    "drug": "Benzodiazepine, rượu",
                    "mechanism": "Tác dụng hiệp đồng ức chế thần kinh trung ương",
                    "effect": "Tăng tác dụng an thần, tăng nguy cơ suy hô hấp",
                    "management": "Tránh hoặc thận trọng. Giảm liều benzodiazepine nếu cần."
                },
                {
                    "drug": "CYP2D6 inhibitors (fluoxetine, paroxetine, quinidine)",
                    "mechanism": "Ức chế chuyển hóa mirtazapine qua CYP2D6",
                    "effect": "Tăng nồng độ mirtazapine, tăng tác dụng phụ",
                    "management": "Thận trọng. Theo dõi dấu hiệu độc tính. Có thể cần giảm liều mirtazapine."
                }
            ],
            "minor": []
        },
        "contraindications": {
            "tuyệt_đối": [
                "Dùng MAO inhibitor (nguy cơ serotonin syndrome)",
                "Dị ứng mirtazapine",
                "Suy gan nặng (Child-Pugh C)"
            ],
            "tương_đối": [
                "Suy gan nhẹ đến trung bình (Child-Pugh A-B) - giảm liều, theo dõi chặt chẽ",
                "Suy thận nặng - thận trọng",
                "Tiền sử giảm bạch cầu - tăng nguy cơ",
                "Mang thai (category C) - thận trọng, chỉ dùng nếu lợi ích > nguy cơ"
            ]
        },
        "pregnancy_lactation": {
            "fda_category": "C",
            "pregnancy_details": "Mirtazapine là category C. Chứng cứ về an toàn trong thai kỳ còn hạn chế. Chỉ dùng nếu lợi ích điều trị vượt trội nguy cơ.",
            "lactation": {
                "safety": "Compatible with monitoring",
                "details": "Mirtazapine bài tiết vào sữa mẹ ở nồng độ thấp. Có thể gây tác dụng phụ ở trẻ (buồn ngủ, bú kém).",
                "recommendation": "Có thể dùng khi cho con bú với theo dõi chặt chẽ trẻ. Theo dõi dấu hiệu buồn ngủ, bú kém ở trẻ."
            }
        },
        "hepatic_adjustment": {
            "mild": "Không cần điều chỉnh liều, nhưng theo dõi chặt chẽ chức năng gan",
            "moderate": "Thận trọng, giảm liều 25-50%",
            "severe": "CHỐNG CHỈ ĐỊNH (chuyển hóa qua gan)",
            "notes": "Mirtazapine chuyển hóa qua gan (CYP1A2, CYP2D6, CYP3A4). Suy gan nặng là chống chỉ định."
        },
        "overdose_management": {
            "symptoms": [
                "Triệu chứng thần kinh: buồn ngủ sâu, hôn mê",
                "Rối loạn tim mạch: nhịp chậm, hạ huyết áp",
                "Rối loạn hô hấp: suy hô hấp (hiếm)"
            ],
            "antidote": "Không có antidote đặc hiệu",
            "treatment": [
                "Đánh giá đường thở, hô hấp, tuần hoàn. Hỗ trợ hô hấp nếu cần",
                "Rửa dạ dày nếu trong vòng 1-2 giờ sau uống",
                "Than hoạt tính: 1g/kg (tối đa 50-100g) nếu trong vòng 1-2 giờ",
                "Theo dõi liên tục: ý thức, hô hấp, tim mạch",
                "Hỗ trợ hô hấp: thở máy nếu suy hô hấp",
                "Điều trị hạ huyết áp: truyền dịch, vận mạch nếu cần"
            ],
            "monitoring": "Theo dõi liên tục ý thức, hô hấp, tim mạch"
        },
        "reversal_agents": {
            "available": False,
            "agents": []
        },
        "administration_instructions": {
            "oral": {
                "with_food": "Có thể uống với hoặc không có thức ăn. Uống trước khi ngủ để giảm tác dụng an thần ban ngày.",
                "timing": "Uống 1 lần/ngày, trước khi ngủ (do tác dụng an thần mạnh). Uống cùng thời điểm mỗi ngày. KHÔNG ngừng đột ngột - giảm liều dần dần."
            }
        },
        "references": {
            "primary_sources": [
                "FDA Drug Label - Remeron (mirtazapine)",
                "UpToDate - Mirtazapine: Drug information",
                "Lexicomp - Mirtazapine"
            ],
            "last_updated": "2025-02-05",
            "evidence_level": "A"
        },
        "risk_flags": {
            "high_alert": False,
            "narrow_therapeutic_index": False,
            "icu_critical_care_only": False,
            "bleeding_risk": None,
            "organ_toxicity": {"hematologic": "Agranulocytosis - Black Box Warning (rare but fatal)", "metabolic": "Weight gain (common), hyperlipidemia"},
            "qt_prolongation": False,
            "hepatotoxicity": "Rare",
            "nephrotoxicity": False,
            "requires_monitoring": ["CBC (agranulocytosis - Black Box Warning)", "Lipid panel (cholesterol, triglycerides)", "Liver function (rare hepatotoxicity)", "Weight", "Suicidal ideation (Black Box Warning)"],
            "look_alike_sound_alike": ["Mirtazapine", "Mirtazapine"]
        },
        "guideline_tags": [
            "FDA Black Box Warning - Agranulocytosis (rare but fatal)",
            "FDA Black Box Warning - Suicidal Behavior (Children/Adolescents)",
            "APA Guidelines - Depression",
            "NICE Guidelines - Depression"
        ],
        "last_updated": "2025-02-18"
    },
    
    "Phenelzine": {
        "group": "Psychiatry - MAO Inhibitor (MAOI)",
        "vietnamese_name": "Phenelzine, Nardil",
        "administration": ["PO"],
        "indications": [
            "Trầm cảm kháng trị",
            "Trầm cảm không điển hình (atypical depression)",
            "Panic disorder",
            "Social anxiety disorder"
        ],
        "contraindications": [
            "Dị ứng phenelzine",
            "Pheochromocytoma",
            "Suy gan nặng",
            "Suy tim nặng",
            "Dùng các thuốc tương tác (xem drug_interactions)"
        ],
        "dosage": {
            "adult_initial": "15mg x 3 lần/ngày, tăng dần",
            "adult_maintenance": "45-90mg/ngày chia 3 lần",
            "adult_max": "90mg/ngày",
            "notes": "MAOI, ức chế MAO-A và MAO-B. Tác dụng chậm (2-4 tuần). Cần chế độ ăn kiêng tyramine (tránh thực phẩm lên men, phô mai, rượu vang đỏ)."
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "Thận trọng",
            "under_30": "Thận trọng"
        },
        "side_effects": [
            "Hạ huyết áp tư thế (phổ biến)",
            "Mất ngủ",
            "Chóng mặt",
            "Khô miệng",
            "Tăng cân",
            "Phù",
            "Rối loạn chức năng tình dục",
            "Nguy cơ tăng huyết áp nặng (nếu ăn thực phẩm chứa tyramine)",
            "Nguy cơ serotonin syndrome (nếu dùng với SSRI/SNRI)"
        ],
        "interactions": [
            "SSRIs, SNRIs: CHỐNG CHỈ ĐỊNH (nguy cơ serotonin syndrome)",
            "TCAs: CHỐNG CHỈ ĐỊNH (nguy cơ tăng huyết áp)",
            "Tyramine (thực phẩm): tăng huyết áp nặng",
            "Sympathomimetics: tăng huyết áp nặng",
            "Meperidine: CHỐNG CHỈ ĐỊNH (nguy hiểm)"
        ],
        "pregnancy": "C",
        "mechanism_of_action": "Phenelzine là MAO inhibitor (MAOI) không chọn lọc, ức chế enzyme monoamine oxidase (MAO-A và MAO-B). MAO chuyển hóa các chất dẫn truyền thần kinh monoamine (serotonin, norepinephrine, dopamine, tyramine). Ức chế MAO → tăng nồng độ các chất dẫn truyền thần kinh → tác dụng chống trầm cảm. Đặc điểm: hiệu quả với trầm cảm kháng trị và trầm cảm không điển hình, nhưng có nhiều tương tác thuốc và thực phẩm (tyramine), nguy cơ tăng huyết áp nặng nếu ăn thực phẩm chứa tyramine.",
        "monitoring": [
            "Triệu chứng trầm cảm, lo âu",
            "Huyết áp (hạ huyết áp tư thế phổ biến)",
            "Dấu hiệu tăng huyết áp nặng (nếu ăn thực phẩm chứa tyramine): nhức đầu dữ dội, đau ngực, nhịp tim nhanh",
            "Dấu hiệu serotonin syndrome (nếu dùng với SSRI/SNRI): sốt, kích động, co giật",
            "Chức năng gan (hiếm viêm gan)",
            "Cân nặng (tăng cân phổ biến)"
        ],
        "precautions": [
            "CHẾ ĐỘ ĂN KIÊNG TYRAMINE - tránh thực phẩm lên men, phô mai, rượu vang đỏ, thịt xông khói, cá hun khói",
            "Nguy cơ tăng huyết áp nặng nếu ăn thực phẩm chứa tyramine - cấp cứu",
            "KHÔNG dùng với SSRIs, SNRIs, TCAs (chống chỉ định tuyệt đối)",
            "Hạ huyết áp tư thế - phổ biến, thận trọng khi đứng dậy",
            "Tác dụng chậm (2-4 tuần) - không mong đợi tác dụng tức thì",
            "Ngừng ít nhất 14 ngày trước khi bắt đầu SSRI/SNRI/TCA",
            "Thận trọng với sympathomimetics (tăng huyết áp nặng)"
        ],
        "pharmacokinetics": {
            "half_life": "11.6 giờ",
            "onset": "2-4 tuần (chậm)",
            "duration": "Dài (do ức chế MAO không hồi phục)",
            "protein_binding": "Không rõ",
            "clearance": "Gan (chuyển hóa qua acetylation), thận (thải trừ). Ức chế MAO không hồi phục (cần tổng hợp MAO mới)."
        },
        "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm, tránh ánh sáng",
        "black_box_warnings": "Nguy cơ tăng huyết áp nặng nếu ăn thực phẩm chứa tyramine. Nguy cơ serotonin syndrome nếu dùng với SSRI/SNRI/TCA. Chống chỉ định với nhiều thuốc.",
        "drug_interactions": {
            "major": [
                {
                    "drug": "SSRIs, SNRIs, TCAs",
                    "mechanism": "Cả hai đều tăng nồng độ serotonin",
                    "effect": "Hội chứng serotonin nghiêm trọng: sốt, kích động, co giật, rối loạn ý thức, có thể tử vong",
                    "management": "CHỐNG CHỈ ĐỊNH TUYỆT ĐỐI. Ngừng phenelzine ít nhất 14 ngày trước khi bắt đầu SSRI/SNRI/TCA."
                },
                {
                    "drug": "Tyramine (thực phẩm: phô mai, rượu vang đỏ, thịt xông khói, cá hun khói)",
                    "mechanism": "MAO chuyển hóa tyramine. Ức chế MAO → tyramine tích lũy → giải phóng norepinephrine → tăng huyết áp nặng",
                    "effect": "Tăng huyết áp nghiêm trọng: nhức đầu dữ dội, đau ngực, nhịp tim nhanh, có thể tử vong",
                    "management": "CHẾ ĐỘ ĂN KIÊNG TYRAMINE. Tránh thực phẩm lên men, phô mai, rượu vang đỏ, thịt xông khói, cá hun khói. Nếu có dấu hiệu tăng huyết áp: điều trị ngay (phentolamine, nifedipine)."
                },
                {
                    "drug": "Sympathomimetics (epinephrine, norepinephrine, pseudoephedrine)",
                    "mechanism": "Tăng nồng độ catecholamines",
                    "effect": "Tăng huyết áp nghiêm trọng",
                    "management": "CHỐNG CHỈ ĐỊNH. Tránh dùng."
                },
                {
                    "drug": "Meperidine",
                    "mechanism": "Tương tác nguy hiểm",
                    "effect": "Sốt cao, kích động, co giật, có thể tử vong",
                    "management": "CHỐNG CHỈ ĐỊNH TUYỆT ĐỐI."
                }
            ],
            "moderate": [
                {
                    "drug": "Antihistamines",
                    "mechanism": "Tăng tác dụng anticholinergic",
                    "effect": "Tăng khô miệng, táo bón, nhìn mờ",
                    "management": "Thận trọng."
                }
            ],
            "minor": []
        },
        "contraindications": {
            "tuyệt_đối": [
                "Dị ứng phenelzine",
                "Pheochromocytoma",
                "Dùng SSRI, SNRI, TCA (chống chỉ định tuyệt đối)",
                "Dùng meperidine (chống chỉ định tuyệt đối)",
                "Suy gan nặng",
                "Suy tim nặng"
            ],
            "tương_đối": [
                "Suy gan nhẹ đến trung bình - thận trọng",
                "Suy tim nhẹ đến trung bình - thận trọng",
                "Hạ huyết áp - có thể làm nặng",
                "Dùng với sympathomimetics - tránh"
            ]
        },
        "pregnancy_lactation": {
            "fda_category": "C",
            "pregnancy_details": "Category C - có nguy cơ cho thai nhi. Có thể dùng khi lợi ích > nguy cơ.",
            "lactation": {
                "safety": "Compatible with monitoring",
                "details": "Phenelzine bài tiết vào sữa mẹ ở nồng độ thấp.",
                "recommendation": "Có thể dùng khi cho con bú với theo dõi."
            }
        },
        "hepatic_adjustment": {
            "mild": "Thận trọng",
            "moderate": "Thận trọng, có thể giảm liều",
            "severe": "CHỐNG CHỈ ĐỊNH (chuyển hóa qua gan)",
            "notes": "Phenelzine chuyển hóa qua gan (acetylation). Suy gan làm giảm chuyển hóa, tăng nguy cơ tích lũy."
        },
        "overdose_management": {
            "symptoms": [
                "Kích động, lo âu",
                "Tăng huyết áp nghiêm trọng (nếu ăn tyramine)",
                "Hạ huyết áp (nếu quá liều)",
                "Sốt (nếu dùng với meperidine)",
                "Co giật",
                "Hôn mê"
            ],
            "antidote": "Không có antidote đặc hiệu. Điều trị tăng huyết áp: phentolamine, nifedipine.",
            "treatment": [
                "Nếu tăng huyết áp: Phentolamine 5mg IV, hoặc nifedipine 10mg ngậm",
                "Nếu hạ huyết áp: Truyền dịch, vận mạch nếu cần",
                "Điều trị co giật: Benzodiazepines",
                "Hỗ trợ hô hấp nếu cần",
                "Theo dõi huyết áp, ECG liên tục"
            ],
            "monitoring": "Huyết áp, ECG, ý thức, nhiệt độ"
        },
        "reversal_agents": {
            "available": False,
            "agents": []
        },
        "administration_instructions": {
            "oral": {
                "with_food": "Có thể uống với hoặc không có thức ăn",
                "timing": "Dùng 3 lần/ngày. Khởi đầu 15mg x 3 lần/ngày, tăng dần. QUAN TRỌNG: Chế độ ăn kiêng tyramine. KHÔNG ngừng đột ngột."
            }
        },
        "references": {
            "primary_sources": [
                "FDA Drug Label - Nardil (phenelzine)",
                "UpToDate - Phenelzine: Drug information"
            ],
            "last_updated": "2025-02-05",
            "evidence_level": "A"
        },
        "risk_flags": {
            "high_alert": True,
            "narrow_therapeutic_index": False,
            "icu_critical_care_only": False,
            "bleeding_risk": False,
            "organ_toxicity": {
                "cardiovascular": "Black Box Warning - Severe hypertension (tyramine reaction - can be fatal) - CRITICAL",
                "neurological": "Black Box Warning - Serotonin syndrome (if used with SSRIs/SNRIs/TCAs - can be fatal) - CRITICAL",
                "cardiovascular_other": "Orthostatic hypotension (common)",
                "hepatic": "Hepatotoxicity (rare)"
            },
            "qt_prolongation": False,
            "hepatotoxicity": True,
            "nephrotoxicity": False,
            "requires_monitoring": [
                "Black Box Warning - Tyramine-restricted diet (avoid fermented foods, cheese, red wine, cured meats) - CRITICAL to prevent severe hypertension",
                "Black Box Warning - Signs of tyramine reaction (severe headache, chest pain, tachycardia, severe hypertension) - CRITICAL, treat immediately with phentolamine/nifedipine",
                "Black Box Warning - CONTRAINDICATED with SSRIs, SNRIs, TCAs (serotonin syndrome risk - fatal) - CRITICAL, wait 14 days washout period",
                "Black Box Warning - CONTRAINDICATED with meperidine (fatal reaction) - CRITICAL",
                "Blood pressure (orthostatic hypotension - common, severe hypertension if tyramine reaction)",
                "Signs of serotonin syndrome (fever, agitation, seizures, altered mental status) - if used with serotonergic drugs",
                "Hepatic function (ALT, AST - hepatotoxicity rare)",
                "Weight (weight gain common)"
            ],
            "look_alike_sound_alike": ["Phenelzine", "Nardil", "Tranylcypromine"]
        },
        "guideline_tags": [
            "FDA Black Box Warning - Tyramine Reaction (Severe Hypertension)",
            "FDA Black Box Warning - Serotonin Syndrome (SSRI/SNRI/TCA Interaction)",
            "APA Guidelines - Treatment-Resistant Depression",
            "ISMP High Alert Medications",
            "WHO Essential Medicines List"
        ],
        "last_updated": "2025-02-18"
    },
    
    "Tranylcypromine": {
        "group": "Psychiatry - MAO Inhibitor (MAOI)",
        "vietnamese_name": "Tranylcypromine, Parnate",
        "administration": ["PO"],
        "indications": [
            "Trầm cảm kháng trị",
            "Trầm cảm không điển hình (atypical depression)",
            "Panic disorder"
        ],
        "contraindications": [
            "Dị ứng tranylcypromine",
            "Pheochromocytoma",
            "Suy gan nặng",
            "Suy tim nặng",
            "Dùng các thuốc tương tác (xem drug_interactions)"
        ],
        "dosage": {
            "adult_initial": "10mg x 2 lần/ngày, tăng dần",
            "adult_maintenance": "30-60mg/ngày chia 2-3 lần",
            "adult_max": "60mg/ngày",
            "notes": "MAOI, ức chế MAO-A và MAO-B. Tác dụng chậm (2-4 tuần). Cần chế độ ăn kiêng tyramine (tránh thực phẩm lên men, phô mai, rượu vang đỏ)."
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "Thận trọng",
            "under_30": "Thận trọng"
        },
        "side_effects": [
            "Hạ huyết áp tư thế (phổ biến)",
            "Mất ngủ",
            "Chóng mặt",
            "Khô miệng",
            "Tăng cân",
            "Phù",
            "Rối loạn chức năng tình dục",
            "Nguy cơ tăng huyết áp nặng (nếu ăn thực phẩm chứa tyramine)",
            "Nguy cơ serotonin syndrome (nếu dùng với SSRI/SNRI)"
        ],
        "interactions": [
            "SSRIs, SNRIs: CHỐNG CHỈ ĐỊNH (nguy cơ serotonin syndrome)",
            "TCAs: CHỐNG CHỈ ĐỊNH (nguy cơ tăng huyết áp)",
            "Tyramine (thực phẩm): tăng huyết áp nặng",
            "Sympathomimetics: tăng huyết áp nặng",
            "Meperidine: CHỐNG CHỈ ĐỊNH (nguy hiểm)"
        ],
        "pregnancy": "C",
        "mechanism_of_action": "Tranylcypromine là MAO inhibitor (MAOI) không chọn lọc, ức chế enzyme monoamine oxidase (MAO-A và MAO-B). MAO chuyển hóa các chất dẫn truyền thần kinh monoamine (serotonin, norepinephrine, dopamine, tyramine). Ức chế MAO → tăng nồng độ các chất dẫn truyền thần kinh → tác dụng chống trầm cảm. Đặc điểm: hiệu quả với trầm cảm kháng trị và trầm cảm không điển hình, nhưng có nhiều tương tác thuốc và thực phẩm (tyramine), nguy cơ tăng huyết áp nặng nếu ăn thực phẩm chứa tyramine. Tương tự phenelzine nhưng có cấu trúc amphetamine-like.",
        "monitoring": [
            "Triệu chứng trầm cảm, lo âu",
            "Huyết áp (hạ huyết áp tư thế phổ biến)",
            "Dấu hiệu tăng huyết áp nặng (nếu ăn thực phẩm chứa tyramine): nhức đầu dữ dội, đau ngực, nhịp tim nhanh",
            "Dấu hiệu serotonin syndrome (nếu dùng với SSRI/SNRI): sốt, kích động, co giật",
            "Chức năng gan (hiếm viêm gan)",
            "Cân nặng (tăng cân phổ biến)"
        ],
        "precautions": [
            "CHẾ ĐỘ ĂN KIÊNG TYRAMINE - tránh thực phẩm lên men, phô mai, rượu vang đỏ, thịt xông khói, cá hun khói",
            "Nguy cơ tăng huyết áp nặng nếu ăn thực phẩm chứa tyramine - cấp cứu",
            "KHÔNG dùng với SSRIs, SNRIs, TCAs (chống chỉ định tuyệt đối)",
            "Hạ huyết áp tư thế - phổ biến, thận trọng khi đứng dậy",
            "Tác dụng chậm (2-4 tuần) - không mong đợi tác dụng tức thì",
            "Ngừng ít nhất 14 ngày trước khi bắt đầu SSRI/SNRI/TCA",
            "Thận trọng với sympathomimetics (tăng huyết áp nặng)"
        ],
        "pharmacokinetics": {
            "half_life": "2.5 giờ",
            "onset": "2-4 tuần (chậm)",
            "duration": "Dài (do ức chế MAO không hồi phục)",
            "protein_binding": "Không rõ",
            "clearance": "Gan (chuyển hóa), thận (thải trừ). Ức chế MAO không hồi phục (cần tổng hợp MAO mới)."
        },
        "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm, tránh ánh sáng",
        "black_box_warnings": "Nguy cơ tăng huyết áp nặng nếu ăn thực phẩm chứa tyramine. Nguy cơ serotonin syndrome nếu dùng với SSRI/SNRI/TCA. Chống chỉ định với nhiều thuốc.",
        "drug_interactions": {
            "major": [
                {
                    "drug": "SSRIs, SNRIs, TCAs",
                    "mechanism": "Cả hai đều tăng nồng độ serotonin",
                    "effect": "Hội chứng serotonin nghiêm trọng: sốt, kích động, co giật, rối loạn ý thức, có thể tử vong",
                    "management": "CHỐNG CHỈ ĐỊNH TUYỆT ĐỐI. Ngừng tranylcypromine ít nhất 14 ngày trước khi bắt đầu SSRI/SNRI/TCA."
                },
                {
                    "drug": "Tyramine (thực phẩm: phô mai, rượu vang đỏ, thịt xông khói, cá hun khói)",
                    "mechanism": "MAO chuyển hóa tyramine. Ức chế MAO → tyramine tích lũy → giải phóng norepinephrine → tăng huyết áp nặng",
                    "effect": "Tăng huyết áp nghiêm trọng: nhức đầu dữ dội, đau ngực, nhịp tim nhanh, có thể tử vong",
                    "management": "CHẾ ĐỘ ĂN KIÊNG TYRAMINE. Tránh thực phẩm lên men, phô mai, rượu vang đỏ, thịt xông khói, cá hun khói. Nếu có dấu hiệu tăng huyết áp: điều trị ngay (phentolamine, nifedipine)."
                },
                {
                    "drug": "Sympathomimetics (epinephrine, norepinephrine, pseudoephedrine)",
                    "mechanism": "Tăng nồng độ catecholamines",
                    "effect": "Tăng huyết áp nghiêm trọng",
                    "management": "CHỐNG CHỈ ĐỊNH. Tránh dùng."
                },
                {
                    "drug": "Meperidine",
                    "mechanism": "Tương tác nguy hiểm",
                    "effect": "Sốt cao, kích động, co giật, có thể tử vong",
                    "management": "CHỐNG CHỈ ĐỊNH TUYỆT ĐỐI."
                }
            ],
            "moderate": [
                {
                    "drug": "Antihistamines",
                    "mechanism": "Tăng tác dụng anticholinergic",
                    "effect": "Tăng khô miệng, táo bón, nhìn mờ",
                    "management": "Thận trọng."
                }
            ],
            "minor": []
        },
        "contraindications": {
            "tuyệt_đối": [
                "Dị ứng tranylcypromine",
                "Pheochromocytoma",
                "Dùng SSRI, SNRI, TCA (chống chỉ định tuyệt đối)",
                "Dùng meperidine (chống chỉ định tuyệt đối)",
                "Suy gan nặng",
                "Suy tim nặng"
            ],
            "tương_đối": [
                "Suy gan nhẹ đến trung bình - thận trọng",
                "Suy tim nhẹ đến trung bình - thận trọng",
                "Hạ huyết áp - có thể làm nặng",
                "Dùng với sympathomimetics - tránh"
            ]
        },
        "pregnancy_lactation": {
            "fda_category": "C",
            "pregnancy_details": "Category C - có nguy cơ cho thai nhi. Có thể dùng khi lợi ích > nguy cơ.",
            "lactation": {
                "safety": "Compatible with monitoring",
                "details": "Tranylcypromine bài tiết vào sữa mẹ ở nồng độ thấp.",
                "recommendation": "Có thể dùng khi cho con bú với theo dõi."
            }
        },
        "hepatic_adjustment": {
            "mild": "Thận trọng",
            "moderate": "Thận trọng, có thể giảm liều",
            "severe": "CHỐNG CHỈ ĐỊNH (chuyển hóa qua gan)",
            "notes": "Tranylcypromine chuyển hóa qua gan. Suy gan làm giảm chuyển hóa, tăng nguy cơ tích lũy."
        },
        "overdose_management": {
            "symptoms": [
                "Kích động, lo âu",
                "Tăng huyết áp nghiêm trọng (nếu ăn tyramine)",
                "Hạ huyết áp (nếu quá liều)",
                "Sốt (nếu dùng với meperidine)",
                "Co giật",
                "Hôn mê"
            ],
            "antidote": "Không có antidote đặc hiệu. Điều trị tăng huyết áp: phentolamine, nifedipine.",
            "treatment": [
                "Nếu tăng huyết áp: Phentolamine 5mg IV, hoặc nifedipine 10mg ngậm",
                "Nếu hạ huyết áp: Truyền dịch, vận mạch nếu cần",
                "Điều trị co giật: Benzodiazepines",
                "Hỗ trợ hô hấp nếu cần",
                "Theo dõi huyết áp, ECG liên tục"
            ],
            "monitoring": "Huyết áp, ECG, ý thức, nhiệt độ"
        },
        "reversal_agents": {
            "available": False,
            "agents": []
        },
        "administration_instructions": {
            "oral": {
                "with_food": "Có thể uống với hoặc không có thức ăn",
                "timing": "Dùng 2-3 lần/ngày. Khởi đầu 10mg x 2 lần/ngày, tăng dần. QUAN TRỌNG: Chế độ ăn kiêng tyramine. KHÔNG ngừng đột ngột."
            }
        },
        "references": {
            "primary_sources": [
                "FDA Drug Label - Parnate (tranylcypromine)",
                "UpToDate - Tranylcypromine: Drug information"
            ],
            "last_updated": "2025-02-05",
            "evidence_level": "A"
        },
        "risk_flags": {
            "high_alert": True,
            "narrow_therapeutic_index": False,
            "icu_critical_care_only": False,
            "bleeding_risk": False,
            "organ_toxicity": {
                "cardiovascular": "Black Box Warning - Severe hypertension (tyramine reaction - can be fatal) - CRITICAL",
                "neurological": "Black Box Warning - Serotonin syndrome (if used with SSRIs/SNRIs/TCAs - can be fatal) - CRITICAL",
                "cardiovascular_other": "Orthostatic hypotension (common)",
                "hepatic": "Hepatotoxicity (rare)"
            },
            "qt_prolongation": False,
            "hepatotoxicity": True,
            "nephrotoxicity": False,
            "requires_monitoring": [
                "Black Box Warning - Tyramine-restricted diet (avoid fermented foods, cheese, red wine, cured meats) - CRITICAL to prevent severe hypertension",
                "Black Box Warning - Signs of tyramine reaction (severe headache, chest pain, tachycardia, severe hypertension) - CRITICAL, treat immediately with phentolamine/nifedipine",
                "Black Box Warning - CONTRAINDICATED with SSRIs, SNRIs, TCAs (serotonin syndrome risk - fatal) - CRITICAL, wait 14 days washout period",
                "Black Box Warning - CONTRAINDICATED with meperidine (fatal reaction) - CRITICAL",
                "Blood pressure (orthostatic hypotension - common, severe hypertension if tyramine reaction)",
                "Signs of serotonin syndrome (fever, agitation, seizures, altered mental status) - if used with serotonergic drugs",
                "Hepatic function (ALT, AST - hepatotoxicity rare)",
                "Weight (weight gain common)"
            ],
            "look_alike_sound_alike": ["Tranylcypromine", "Parnate", "Phenelzine"]
        },
        "guideline_tags": [
            "FDA Black Box Warning - Tyramine Reaction (Severe Hypertension)",
            "FDA Black Box Warning - Serotonin Syndrome (SSRI/SNRI/TCA Interaction)",
            "APA Guidelines - Treatment-Resistant Depression",
            "ISMP High Alert Medications",
            "WHO Essential Medicines List"
        ],
        "last_updated": "2025-02-18"
    },
    "Trazodone": {
        "group": "Psychiatry - Serotonin Antagonist/Reuptake Inhibitor (SARI)",
        "vietnamese_name": "Trazodone, Desyrel",
        "administration": ["PO"],
        "indications": [
            "Trầm cảm",
            "Mất ngủ (off-label, liều thấp)",
            "Rối loạn lo âu",
            "Rối loạn căng thẳng sau sang chấn (PTSD)"
        ],
        "contraindications": [
            "Dùng MAO inhibitor",
            "Dị ứng trazodone",
            "Suy gan nặng",
            "Priapism (cương dương kéo dài) trước đây"
        ],
        "dosage": {
            "adult_depression": "150-300mg/ngày chia 2-3 lần, tăng đến 400-600mg/ngày nếu cần",
            "adult_insomnia": "25-100mg trước khi ngủ (off-label)",
            "adult_max": "600mg/ngày",
            "notes": "Tác dụng an thần mạnh → uống trước khi ngủ. Nguy cơ priapism (cương dương kéo dài) - nguy hiểm."
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "Thận trọng",
            "under_30": "Thận trọng, có thể giảm liều"
        },
        "side_effects": [
            "Buồn ngủ (phổ biến, đặc biệt khi bắt đầu)",
            "Chóng mặt",
            "Nhức đầu",
            "Khô miệng",
            "Priapism (cương dương kéo dài) - nguy hiểm, cần cấp cứu",
            "Hạ huyết áp tư thế (orthostatic hypotension)",
            "Rối loạn nhịp tim (hiếm, nhưng quan trọng)",
            "Rối loạn tâm thần (hiếm)"
        ],
        "interactions": [
            "MAO inhibitors: nguy cơ serotonin syndrome",
            "CYP3A4 inhibitors: tăng nồng độ trazodone",
            "Thuốc ức chế dẫn truyền nhĩ thất: tăng nguy cơ rối loạn nhịp tim",
            "Ethanol: tăng tác dụng an thần"
        ],
        "pregnancy": "C",
        "mechanism_of_action": "Serotonin Antagonist/Reuptake Inhibitor (SARI). Cơ chế đa dạng: 1) Ức chế tái hấp thu serotonin, tăng nồng độ serotonin trong synap. 2) Đối vận thụ thể 5-HT2A và 5-HT2C (giảm tác dụng phụ serotonin, tăng tác dụng qua 5-HT1A). 3) Đối vận thụ thể alpha-1 adrenergic (gây hạ huyết áp tư thế, an thần). 4) Đối vận thụ thể histamine H1 (gây an thần). Đặc điểm: tác dụng an thần mạnh (do đối vận alpha-1 và H1), được dùng cho mất ngủ ở liều thấp. Nguy cơ priapism (cương dương kéo dài) - nguy hiểm, cần cấp cứu.",
        "monitoring": [
            "Triệu chứng trầm cảm, lo âu",
            "Priapism (cương dương kéo dài) - RẤT QUAN TRỌNG, cần cấp cứu nếu xảy ra",
            "Huyết áp tư thế (orthostatic hypotension) - đặc biệt khi đứng dậy",
            "ECG - hiếm rối loạn nhịp tim (QT kéo dài, rối loạn nhịp)",
            "Buồn ngủ, chóng mặt (phổ biến)",
            "Chức năng gan (ALT, AST) - hiếm viêm gan"
        ],
        "precautions": [
            "KHÔNG được ngừng đột ngột (nguy cơ hội chứng cai) - giảm liều dần dần",
            "Nguy cơ priapism (cương dương kéo dài) - nguy hiểm, cần cấp cứu ngay nếu xảy ra (có thể gây tổn thương dương vật vĩnh viễn)",
            "Cảnh báo bệnh nhân nam về nguy cơ priapism - cần báo ngay nếu có cương dương kéo dài >4 giờ",
            "Tác dụng an thần mạnh → uống trước khi ngủ, thận trọng khi lái xe",
            "Nguy cơ hạ huyết áp tư thế - đứng dậy chậm, đặc biệt khi bắt đầu",
            "Nguy cơ rối loạn nhịp tim (hiếm, nhưng quan trọng) - theo dõi ECG nếu có triệu chứng",
            "Tránh dùng với MAO inhibitors (nguy cơ serotonin syndrome)",
            "Tránh ethanol (rượu) - tăng tác dụng an thần",
            "Thận trọng ở bệnh nhân có bệnh tim - tăng nguy cơ rối loạn nhịp tim",
            "Khởi đầu với liều thấp để giảm tác dụng phụ"
        ],
        "pharmacokinetics": {
            "half_life": "5-9 giờ",
            "onset": "1-2 tuần",
            "duration": "Dài (do half-life và tác dụng trên receptor)",
            "protein_binding": "85-95%",
            "metabolism": "Gan (chuyển hóa chủ yếu qua CYP3A4 thành mCPP - có hoạt tính)",
            "clearance": "Gan (chuyển hóa), thận (thải trừ một phần)"
        },
        "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm, tránh ánh sáng",
        "black_box_warnings": "Nguy cơ priapism (cương dương kéo dài) - có thể gây tổn thương dương vật vĩnh viễn nếu không điều trị kịp thời. Cần cấp cứu ngay nếu có cương dương kéo dài >4 giờ. Nguy cơ rối loạn nhịp tim (QT kéo dài, rối loạn nhịp).",
        "drug_interactions": {
            "major": [
                {
                    "drug": "MAO inhibitors (phenelzine, tranylcypromine, selegiline)",
                    "mechanism": "Tăng giải phóng serotonin, nguy cơ serotonin syndrome",
                    "effect": "Serotonin syndrome (kích động, tăng thân nhiệt, co giật, có thể tử vong)",
                    "management": "CHỐNG CHỈ ĐỊNH TUYỆT ĐỐI. Ngừng MAO inhibitor ít nhất 14 ngày trước khi bắt đầu trazodone."
                },
                {
                    "drug": "CYP3A4 inhibitors (ketoconazole, itraconazole, clarithromycin, ritonavir)",
                    "mechanism": "Ức chế chuyển hóa trazodone qua CYP3A4",
                    "effect": "Tăng nồng độ trazodone đáng kể, tăng tác dụng phụ (buồn ngủ, hạ huyết áp, priapism, rối loạn nhịp tim)",
                    "management": "Thận trọng. Giảm liều trazodone 50-75%. Theo dõi dấu hiệu độc tính, đặc biệt priapism và rối loạn nhịp tim."
                }
            ],
            "moderate": [
                {
                    "drug": "Thuốc ức chế dẫn truyền nhĩ thất (verapamil, diltiazem, beta-blockers)",
                    "mechanism": "Tác dụng hiệp đồng ức chế dẫn truyền nhĩ thất",
                    "effect": "Tăng nguy cơ rối loạn nhịp tim, block nhĩ thất",
                    "management": "Thận trọng. Theo dõi ECG. Tránh dùng cùng nếu có thể."
                },
                {
                    "drug": "Ethanol",
                    "mechanism": "Tác dụng hiệp đồng ức chế thần kinh trung ương",
                    "effect": "Tăng tác dụng an thần, tăng nguy cơ suy hô hấp",
                    "management": "Tránh ethanol khi dùng trazodone."
                }
            ],
            "minor": []
        },
        "contraindications": {
            "tuyệt_đối": [
                "Dùng MAO inhibitor (nguy cơ serotonin syndrome)",
                "Dị ứng trazodone",
                "Priapism (cương dương kéo dài) trước đây",
                "Suy gan nặng (Child-Pugh C)"
            ],
            "tương_đối": [
                "Bệnh tim - tăng nguy cơ rối loạn nhịp tim",
                "Suy gan nhẹ đến trung bình (Child-Pugh A-B) - thận trọng, giảm liều",
                "Suy thận nặng - thận trọng",
                "Dùng với CYP3A4 inhibitors - tăng nồng độ trazodone đáng kể",
                "Mang thai (category C) - thận trọng, chỉ dùng nếu lợi ích > nguy cơ"
            ]
        },
        "pregnancy_lactation": {
            "fda_category": "C",
            "pregnancy_details": "Trazodone là category C. Chứng cứ về an toàn trong thai kỳ còn hạn chế. Chỉ dùng nếu lợi ích điều trị vượt trội nguy cơ.",
            "lactation": {
                "safety": "Compatible with monitoring",
                "details": "Trazodone bài tiết vào sữa mẹ ở nồng độ thấp. Có thể gây tác dụng phụ ở trẻ (buồn ngủ, bú kém).",
                "recommendation": "Có thể dùng khi cho con bú với theo dõi chặt chẽ trẻ. Theo dõi dấu hiệu buồn ngủ, bú kém ở trẻ."
            }
        },
        "hepatic_adjustment": {
            "mild": "Không cần điều chỉnh liều, nhưng theo dõi chặt chẽ chức năng gan",
            "moderate": "Thận trọng, giảm liều 25-50%",
            "severe": "CHỐNG CHỈ ĐỊNH (chuyển hóa chủ yếu qua gan)",
            "notes": "Trazodone chuyển hóa chủ yếu qua gan (CYP3A4). Suy gan nặng là chống chỉ định."
        },
        "overdose_management": {
            "symptoms": [
                "Triệu chứng thần kinh: buồn ngủ sâu, hôn mê",
                "Rối loạn tim mạch: hạ huyết áp nặng, rối loạn nhịp tim, QT kéo dài",
                "Rối loạn hô hấp: suy hô hấp (hiếm)",
                "Priapism (nếu quá liều ở nam giới)",
                "Rối loạn tiêu hóa: buồn nôn, nôn"
            ],
            "antidote": "Không có antidote đặc hiệu",
            "treatment": [
                "Đánh giá đường thở, hô hấp, tuần hoàn. Hỗ trợ hô hấp nếu cần",
                "Rửa dạ dày nếu trong vòng 1-2 giờ sau uống",
                "Than hoạt tính: 1g/kg (tối đa 50-100g) nếu trong vòng 1-2 giờ",
                "Theo dõi ECG liên tục (quan trọng - nguy cơ rối loạn nhịp tim)",
                "Điều trị hạ huyết áp: Truyền dịch, nâng chân, nếu cần: dopamine, norepinephrine",
                "Điều trị rối loạn nhịp tim nếu có",
                "Điều trị priapism nếu có: Cấp cứu ngay, có thể cần can thiệp phẫu thuật",
                "Hỗ trợ hô hấp: thở máy nếu suy hô hấp"
            ],
            "monitoring": "Theo dõi liên tục ECG, huyết áp, nhịp tim, ý thức, hô hấp, dấu hiệu priapism trong ít nhất 24 giờ"
        },
        "reversal_agents": {
            "available": False,
            "agents": []
        },
        "administration_instructions": {
            "oral": {
                "with_food": "Có thể uống với hoặc không có thức ăn. Uống với thức ăn có thể giảm buồn nôn.",
                "timing": "Uống trước khi ngủ (do tác dụng an thần mạnh). Chia 2-3 lần/ngày nếu dùng liều cao. QUAN TRỌNG: Cảnh báo bệnh nhân nam về nguy cơ priapism - cần báo ngay nếu có cương dương kéo dài >4 giờ. KHÔNG ngừng đột ngột - giảm liều dần dần."
            }
        },
        "references": {
            "primary_sources": [
                "FDA Drug Label - Desyrel (trazodone)",
                "UpToDate - Trazodone: Drug information",
                "Lexicomp - Trazodone"
            ],
            "last_updated": "2025-02-05",
            "evidence_level": "A"
        },
        "risk_flags": {
            "high_alert": True,
            "narrow_therapeutic_index": False,
            "icu_critical_care_only": False,
            "bleeding_risk": None,
            "organ_toxicity": {"genitourinary": "Priapism - Black Box Warning (can cause permanent damage)", "cardiovascular": "QT prolongation - Black Box Warning, arrhythmias", "cardiovascular_hypotension": "Orthostatic hypotension"},
            "qt_prolongation": True,
            "hepatotoxicity": "Rare",
            "nephrotoxicity": False,
            "requires_monitoring": ["ECG (QT prolongation - Black Box Warning)", "Priapism monitoring (Black Box Warning - emergency if >4 hours)", "Blood pressure (orthostatic hypotension)", "CYP3A4 interactions"],
            "look_alike_sound_alike": ["Trazodone", "Tramadol"]
        },
        "guideline_tags": [
            "FDA Black Box Warning - Priapism (can cause permanent damage)",
            "FDA Black Box Warning - QT Prolongation",
            "APA Guidelines - Depression",
            "NICE Guidelines - Depression"
        ],
        "last_updated": "2025-02-18"
    },
    
}

__all__ = ['OTHER_ANTIDEPRESSANTS_DRUGS']
