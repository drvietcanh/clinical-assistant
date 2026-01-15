"""Cough Suppressants, Expectorants, and Mucolytics
Active module - contains cough suppressants, expectorants, and mucolytics"""

COUGH_EXPECTORANTS_MUCOLYTICS_DRUGS = {
    "Dextromethorphan": {
        "group": "Respiratory - Cough Suppressant (Antitussive)",
        "vietnamese_name": "Dextromethorphan, Robitussin DM, Tussin DM",
        "administration": ["PO"],
        "indications": [
            "Ho khan không có đờm",
            "Ho do kích ứng đường hô hấp trên",
            "Ho do cảm lạnh, cúm",
        ],
        "contraindications": {
            "tuyệt_đối": [
                "Dị ứng với dextromethorphan hoặc bất kỳ thành phần nào",
                "Đang dùng MAO inhibitors (trong vòng 14 ngày)",
                "Ho có đờm (không dùng vì ức chế ho sẽ giữ đờm lại)",
            ],
            "tương_đối": [
                "Hen phế quản - thận trọng",
                "Suy gan nặng - thận trọng",
                "Suy thận nặng - thận trọng",
                "Đang dùng SSRI, SNRI - thận trọng (tăng nguy cơ serotonin syndrome)",
            ],
        },
        "dosage": {
            "adult_po": "10-20mg x 3-4 lần/ngày (mỗi 4-6 giờ), tối đa 120mg/ngày",
            "pediatric_po_6_12_years": "5-10mg x 3-4 lần/ngày, tối đa 60mg/ngày",
            "pediatric_po_2_6_years": "2.5-5mg x 3-4 lần/ngày, tối đa 30mg/ngày",
            "pediatric_po_under_2_years": "Không khuyến cáo cho trẻ <2 tuổi",
            "notes": "Dùng khi cần. Không dùng quá 7 ngày. Không dùng cho ho có đờm.",
        },
        "renal_adjustment": {"normal": "Không đổi", "30_60": "Thận trọng", "under_30": "Thận trọng, có thể giảm liều", "dialysis": "Thận trọng", "notes": "Dextromethorphan chuyển hóa ở gan và thải trừ qua thận. Suy thận có thể tích lũy."},
        "side_effects": [
            "Buồn ngủ, chóng mặt",
            "Buồn nôn, nôn",
            "Táo bón",
            "Kích động, ảo giác (liều cao)",
            "Serotonin syndrome (khi dùng với SSRI/SNRI/MAOI)",
        ],
        "interactions": [
            "MAO inhibitors: CHỐNG CHỈ ĐỊNH (tăng nguy cơ serotonin syndrome nghiêm trọng)",
            "SSRI, SNRI: tăng nguy cơ serotonin syndrome",
            "Alcohol: tăng tác dụng ức chế thần kinh trung ương",
            "Các thuốc ức chế thần kinh trung ương khác: tăng tác dụng",
        ],
        "pregnancy": "C - Thận trọng trong thai kỳ",
        "risk_flags": {
            "high_alert": False,
            "narrow_therapeutic_index": False,
            "organ_toxicity": {},
            "icu_critical_care_only": False,
            "look_alike_sound_alike": ["Dextromethorphan", "Dextroamphetamine", "Dexamethasone"]
        },
        "guideline_tags": [
            "ACCP Guidelines - Cough Management",
            "GOLD Guidelines (Global Initiative for Chronic Obstructive Lung Disease)"
        ],
        "mechanism_of_action": "Dextromethorphan là thuốc giảm ho tác động lên trung tâm ho ở hành não. Ức chế trung tâm ho bằng cách tác động lên sigma-1 receptors và NMDA receptors. Không có tác dụng giảm đau hoặc gây nghiện như codeine. Tác dụng giảm ho tương đương codeine nhưng ít tác dụng phụ hơn. KHÔNG dùng cho ho có đờm vì sẽ giữ đờm lại trong phổi.",
        "monitoring": [
            "Triệu chứng ho (giảm ho khan)",
            "Dấu hiệu serotonin syndrome nếu dùng với SSRI/SNRI: nhịp tim nhanh, tăng huyết áp, sốt, kích động, co giật",
            "Dấu hiệu quá liều: kích động, ảo giác, loạn nhịp tim",
            "Chức năng gan, thận nếu dùng kéo dài",
        ],
        "precautions": [
            "CHỐNG CHỈ ĐỊNH với MAO inhibitors (trong vòng 14 ngày) - nguy cơ serotonin syndrome nghiêm trọng",
            "KHÔNG dùng cho ho có đờm - sẽ giữ đờm lại trong phổi, tăng nguy cơ nhiễm trùng",
            "Thận trọng với SSRI, SNRI - tăng nguy cơ serotonin syndrome",
            "Tránh dùng với alcohol - tăng tác dụng ức chế thần kinh trung ương",
            "Không dùng quá 7 ngày - nếu ho kéo dài, cần đánh giá lại nguyên nhân",
            "Thận trọng khi lái xe hoặc vận hành máy móc (buồn ngủ)",
        ],
        "pharmacokinetics": {
            "half_life": "2-4 giờ",
            "onset": "15-30 phút",
            "duration": "3-6 giờ",
            "bioavailability": "Không rõ",
            "protein_binding": "Không đáng kể",
            "metabolism": "Gan: chuyển hóa qua CYP2D6 thành dextrorphan (active metabolite), CYP3A4 thành 3-methoxymorphinan (inactive)",
            "clearance": "Thận: thải trừ chủ yếu qua thận (metabolites)",
            "absorption": "Hấp thu nhanh sau khi uống",
        },
        "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ánh sáng trực tiếp, tránh ẩm. Để xa tầm tay trẻ em.",
        "black_box_warnings": "CHỐNG CHỈ ĐỊNH với MAO inhibitors (trong vòng 14 ngày) - tăng nguy cơ serotonin syndrome nghiêm trọng, có thể tử vong. KHÔNG dùng cho ho có đờm.",
        "drug_interactions": {
            "major": [
                {
                    "drug": "MAO inhibitors (phenelzine, tranylcypromine, selegiline, rasagiline)",
                    "mechanism": "Ức chế chuyển hóa dextromethorphan, tăng nồng độ, tăng nguy cơ serotonin syndrome",
                    "effect": "Tăng nguy cơ serotonin syndrome nghiêm trọng: nhịp tim nhanh, tăng huyết áp, sốt, kích động, co giật, có thể tử vong",
                    "management": "CHỐNG CHỈ ĐỊNH TUYỆT ĐỐI. Không dùng dextromethorphan trong vòng 14 ngày sau khi ngừng MAO inhibitor."
                }
            ],
            "moderate": [
                {
                    "drug": "SSRI (fluoxetine, sertraline, paroxetine, citalopram, escitalopram)",
                    "mechanism": "Ức chế CYP2D6, tăng nồng độ dextromethorphan, tăng nguy cơ serotonin syndrome",
                    "effect": "Tăng nguy cơ serotonin syndrome: nhịp tim nhanh, tăng huyết áp, sốt, kích động",
                    "management": "Thận trọng. Theo dõi dấu hiệu serotonin syndrome. Có thể cần giảm liều dextromethorphan hoặc tránh dùng."
                },
                {
                    "drug": "SNRI (venlafaxine, duloxetine)",
                    "mechanism": "Ức chế CYP2D6, tăng nồng độ dextromethorphan, tăng nguy cơ serotonin syndrome",
                    "effect": "Tăng nguy cơ serotonin syndrome",
                    "management": "Thận trọng. Theo dõi dấu hiệu serotonin syndrome."
                },
                {
                    "drug": "Alcohol",
                    "mechanism": "Tác dụng cộng dồn ức chế thần kinh trung ương",
                    "effect": "Tăng buồn ngủ, chóng mặt, giảm khả năng vận hành máy móc",
                    "management": "Tránh dùng với alcohol."
                }
            ],
            "minor": []
        },
        "contraindications_detail": {
            "tuyệt_đối": [
                "Dị ứng với dextromethorphan",
                "Đang dùng MAO inhibitors (trong vòng 14 ngày) - CHỐNG CHỈ ĐỊNH TUYỆT ĐỐI",
                "Ho có đờm - KHÔNG dùng vì sẽ giữ đờm lại"
            ],
            "tương_đối": [
                "Hen phế quản - thận trọng",
                "Suy gan nặng - thận trọng",
                "Suy thận nặng - thận trọng",
                "Đang dùng SSRI, SNRI - thận trọng (tăng nguy cơ serotonin syndrome)"
            ]
        },
        "pregnancy_lactation": {
            "fda_category": "C",
            "pregnancy_details": "Category C - có nguy cơ cho thai nhi. Dextromethorphan có thể ảnh hưởng đến thai nhi. Có thể được dùng khi lợi ích vượt quá nguy cơ, đặc biệt trong tam cá nguyệt thứ hai và thứ ba.",
            "lactation": {
                "safety": "Compatible with monitoring",
                "details": "Dextromethorphan bài tiết vào sữa mẹ ở nồng độ thấp. Nồng độ trong sữa mẹ rất thấp, không đáng kể.",
                "recommendation": "Có thể dùng khi cho con bú với liều thường dùng."
            }
        },
        "hepatic_adjustment": {
            "mild": "Không đổi",
            "moderate": "Thận trọng",
            "severe": "Thận trọng, có thể giảm liều",
            "notes": "Dextromethorphan chuyển hóa qua gan (CYP2D6, CYP3A4). Suy gan có thể làm giảm chuyển hóa và tích lũy."
        },
        "overdose_management": {
            "symptoms": [
                "Kích động, ảo giác",
                "Buồn ngủ nặng, hôn mê",
                "Loạn nhịp tim",
                "Co giật",
                "Serotonin syndrome (nếu dùng với SSRI/SNRI/MAOI)",
            ],
            "antidote": "Không có antidote đặc hiệu. Naloxone KHÔNG có tác dụng với dextromethorphan.",
            "treatment": [
                "Ngừng ngay dextromethorphan",
                "Than hoạt tính nếu uống trong vòng 1-2 giờ",
                "Hỗ trợ hô hấp nếu cần",
                "Điều trị triệu chứng: benzodiazepine cho co giật, hỗ trợ hô hấp cho ức chế hô hấp",
                "Nếu có serotonin syndrome: điều trị với cyproheptadine hoặc benzodiazepine",
            ],
            "monitoring": "Nhịp tim, huyết áp, SpO2, dấu hiệu serotonin syndrome, dấu hiệu thần kinh"
        },
        "reversal_agents": {
            "available": False,
            "agents": [],
            "notes": "Không có antidote đặc hiệu. Naloxone KHÔNG có tác dụng với dextromethorphan. Điều trị chủ yếu là hỗ trợ và điều trị triệu chứng."
        },
        "administration_instructions": {
            "oral": {
                "with_food": "Có thể uống với hoặc không có thức ăn",
                "timing": "Mỗi 4-6 giờ khi cần, không quá 4 lần/ngày",
                "missed_dose": "Dùng ngay khi nhớ ra nếu cần, không dùng gấp đôi liều",
                "notes": "Không dùng quá 7 ngày. Không dùng cho ho có đờm."
            }
        },
        "references": {
            "primary_sources": [
                "FDA Drug Label - Dextromethorphan",
                "UpToDate - Dextromethorphan: Drug information",
                "ACCP Guidelines - Cough Management",
            ],
            "last_updated": "2025-02-19",
            "evidence_level": "B - FDA approved, widely used in clinical practice"
        }
    },
    "Guaifenesin": {
        "group": "Respiratory - Expectorant",
        "vietnamese_name": "Guaifenesin, Mucinex, Robitussin",
        "administration": ["PO"],
        "indications": [
            "Ho có đờm",
            "Viêm phế quản cấp và mạn tính",
            "Làm loãng đờm để dễ khạc ra",
        ],
        "contraindications": {
            "tuyệt_đối": [
                "Dị ứng với guaifenesin hoặc bất kỳ thành phần nào",
            ],
            "tương_đối": [
                "Suy thận nặng - thận trọng",
                "Suy gan nặng - thận trọng",
            ],
        },
        "dosage": {
            "adult_po": "200-400mg x 3-4 lần/ngày (mỗi 4 giờ), tối đa 2.4g/ngày",
            "pediatric_po_12_plus": "200-400mg x 3-4 lần/ngày, tối đa 1.2g/ngày",
            "pediatric_po_6_12_years": "100-200mg x 3-4 lần/ngày, tối đa 1.2g/ngày",
            "pediatric_po_2_6_years": "50-100mg x 3-4 lần/ngày",
            "pediatric_po_under_2_years": "Không khuyến cáo cho trẻ <2 tuổi",
            "notes": "Uống nhiều nước để tăng hiệu quả. Dùng khi cần.",
        },
        "renal_adjustment": {"normal": "Không đổi", "30_60": "Thận trọng", "under_30": "Thận trọng", "dialysis": "Thận trọng", "notes": "Guaifenesin thải trừ qua thận. Suy thận có thể tích lũy."},
        "side_effects": [
            "Buồn nôn, nôn",
            "Đau bụng",
            "Chóng mặt",
            "Đau đầu",
            "Phát ban (hiếm)",
        ],
        "interactions": [
            "Không có tương tác thuốc quan trọng",
        ],
        "pregnancy": "C - Thận trọng trong thai kỳ",
        "risk_flags": {
            "high_alert": False,
            "narrow_therapeutic_index": False,
            "organ_toxicity": {},
            "icu_critical_care_only": False,
            "look_alike_sound_alike": []
        },
        "guideline_tags": [
            "ACCP Guidelines - Cough Management",
            "GOLD Guidelines (Global Initiative for Chronic Obstructive Lung Disease)"
        ],
        "mechanism_of_action": "Guaifenesin là thuốc long đờm (expectorant). Kích thích tiết dịch phế quản, làm tăng lượng dịch trong đường hô hấp, làm loãng đờm và giúp đờm dễ khạc ra ngoài. Tăng hoạt động của lông chuyển phế quản, giúp tống đờm ra ngoài. Uống nhiều nước sẽ tăng hiệu quả của guaifenesin.",
        "monitoring": [
            "Triệu chứng ho có đờm (đờm loãng hơn, dễ khạc ra)",
            "Dấu hiệu quá liều: buồn nôn, nôn nặng",
        ],
        "precautions": [
            "Uống nhiều nước để tăng hiệu quả - QUAN TRỌNG",
            "Không dùng cho ho khan (không có đờm)",
            "Thận trọng ở suy thận nặng",
        ],
        "pharmacokinetics": {
            "half_life": "1 giờ",
            "onset": "30 phút - 1 giờ",
            "duration": "4 giờ",
            "bioavailability": "Không rõ",
            "protein_binding": "Không đáng kể",
            "metabolism": "Gan: chuyển hóa một phần",
            "clearance": "Thận: thải trừ chủ yếu qua thận (dạng nguyên dạng và metabolites)",
            "absorption": "Hấp thu nhanh sau khi uống",
        },
        "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ánh sáng trực tiếp, tránh ẩm. Để xa tầm tay trẻ em.",
        "black_box_warnings": None,
        "drug_interactions": {
            "major": [],
            "moderate": [],
            "minor": []
        },
        "contraindications_detail": {
            "tuyệt_đối": [
                "Dị ứng với guaifenesin"
            ],
            "tương_đối": [
                "Suy thận nặng - thận trọng",
                "Suy gan nặng - thận trọng"
            ]
        },
        "pregnancy_lactation": {
            "fda_category": "C",
            "pregnancy_details": "Category C - có nguy cơ cho thai nhi. Guaifenesin có thể ảnh hưởng đến thai nhi. Có thể được dùng khi lợi ích vượt quá nguy cơ.",
            "lactation": {
                "safety": "Compatible",
                "details": "Guaifenesin bài tiết vào sữa mẹ ở nồng độ thấp. Nồng độ trong sữa mẹ rất thấp, không đáng kể.",
                "recommendation": "Có thể dùng khi cho con bú."
            }
        },
        "hepatic_adjustment": {
            "mild": "Không đổi",
            "moderate": "Thận trọng",
            "severe": "Thận trọng",
            "notes": "Guaifenesin chuyển hóa một phần ở gan. Suy gan có thể ảnh hưởng nhưng thường không cần điều chỉnh liều."
        },
        "overdose_management": {
            "symptoms": [
                "Buồn nôn, nôn nặng",
                "Đau bụng",
                "Chóng mặt",
            ],
            "antidote": "Không có antidote đặc hiệu.",
            "treatment": [
                "Ngừng ngay guaifenesin",
                "Than hoạt tính nếu uống trong vòng 1-2 giờ",
                "Điều trị triệu chứng",
            ],
            "monitoring": "Triệu chứng tiêu hóa, dấu hiệu mất nước nếu nôn nhiều"
        },
        "reversal_agents": {
            "available": False,
            "agents": [],
            "notes": "Không có antidote đặc hiệu. Điều trị chủ yếu là hỗ trợ và điều trị triệu chứng."
        },
        "administration_instructions": {
            "oral": {
                "with_food": "Có thể uống với hoặc không có thức ăn",
                "timing": "Mỗi 4 giờ khi cần, không quá 4 lần/ngày",
                "missed_dose": "Dùng ngay khi nhớ ra nếu cần",
                "notes": "QUAN TRỌNG: Uống nhiều nước để tăng hiệu quả. Không dùng cho ho khan."
            }
        },
        "references": {
            "primary_sources": [
                "FDA Drug Label - Guaifenesin",
                "UpToDate - Guaifenesin: Drug information",
                "ACCP Guidelines - Cough Management",
            ],
            "last_updated": "2025-02-19",
            "evidence_level": "B - FDA approved, widely used in clinical practice"
        }
    },
    "Acetylcysteine (mucolytic)": {
        "group": "Respiratory - Mucolytic",
        "vietnamese_name": "Acetylcysteine, Mucomyst, Fluimucil",
        "administration": ["Inhalation", "Nebulizer", "PO"],
        "indications": [
            "Ho có đờm đặc, khó khạc",
            "Viêm phế quản cấp và mạn tính",
            "COPD có đờm đặc",
            "Làm tan đờm đặc",
        ],
        "contraindications": {
            "tuyệt_đối": [
                "Dị ứng với acetylcysteine hoặc bất kỳ thành phần nào",
            ],
            "tương_đối": [
                "Hen phế quản - thận trọng (có thể gây co thắt phế quản)",
                "Loét dạ dày tá tràng - thận trọng (dạng uống)",
            ],
        },
        "dosage": {
            "adult_inhalation": "3-5ml dung dịch 20% hoặc 6-10ml dung dịch 10% x 3-4 lần/ngày qua máy khí dung",
            "adult_po": "200mg x 2-3 lần/ngày",
            "pediatric_inhalation": "1-2ml dung dịch 20% hoặc 2-4ml dung dịch 10% x 3-4 lần/ngày",
            "pediatric_po": "100mg x 2-3 lần/ngày (trẻ >2 tuổi)",
            "notes": "Dạng hít: có thể gây co thắt phế quản ở bệnh nhân hen. Có thể dùng kèm với bronchodilator. Dạng uống: uống sau bữa ăn để giảm kích ứng dạ dày.",
        },
        "renal_adjustment": {"normal": "Không đổi", "30_60": "Không đổi", "under_30": "Không đổi", "dialysis": "Không đổi", "notes": "Acetylcysteine chuyển hóa ở gan và thải trừ qua thận. Tuy nhiên, dạng hít tác dụng tại chỗ, không cần điều chỉnh liều ở suy thận."},
        "side_effects": [
            "Co thắt phế quản (dạng hít, đặc biệt ở bệnh nhân hen)",
            "Buồn nôn, nôn (dạng uống)",
            "Đau bụng (dạng uống)",
            "Kích ứng đường hô hấp (dạng hít)",
            "Mùi khó chịu (dạng hít)",
        ],
        "interactions": [
            "Không có tương tác thuốc quan trọng",
            "Có thể dùng kèm với bronchodilator để giảm co thắt phế quản",
        ],
        "pregnancy": "B - Có thể dùng trong thai kỳ",
        "risk_flags": {
            "high_alert": False,
            "narrow_therapeutic_index": False,
            "organ_toxicity": {},
            "icu_critical_care_only": False,
            "look_alike_sound_alike": ["Acetylcysteine", "N-acetylcysteine"]
        },
        "guideline_tags": [
            "ACCP Guidelines - Cough Management",
            "GOLD Guidelines (Global Initiative for Chronic Obstructive Lung Disease)"
        ],
        "mechanism_of_action": "Acetylcysteine là thuốc làm tan đờm (mucolytic). Phá vỡ liên kết disulfide (-S-S-) trong glycoprotein của đờm, làm giảm độ nhớt và độ đặc của đờm, giúp đờm dễ khạc ra ngoài. Cũng có tác dụng chống oxy hóa. Dạng hít: tác dụng trực tiếp tại đường hô hấp. Dạng uống: hấp thu và chuyển hóa thành cysteine, có tác dụng tại chỗ sau khi bài tiết vào đường hô hấp.",
        "monitoring": [
            "Triệu chứng ho có đờm (đờm loãng hơn, dễ khạc ra)",
            "Dấu hiệu co thắt phế quản (dạng hít): khó thở, thở khò khè",
            "Triệu chứng tiêu hóa (dạng uống): buồn nôn, đau bụng",
        ],
        "precautions": [
            "Dạng hít: có thể gây co thắt phế quản ở bệnh nhân hen - cần dùng kèm với bronchodilator hoặc thận trọng",
            "Dạng uống: uống sau bữa ăn để giảm kích ứng dạ dày",
            "Mùi khó chịu của dạng hít có thể gây khó chịu cho bệnh nhân",
            "Không dùng cho ho khan (không có đờm)",
        ],
        "pharmacokinetics": {
            "half_life": "5.6 giờ (dạng uống)",
            "onset": "15-30 phút (dạng hít), 1-2 giờ (dạng uống)",
            "duration": "4-6 giờ",
            "bioavailability": "10% (dạng uống)",
            "protein_binding": "83%",
            "metabolism": "Gan: chuyển hóa thành cysteine và các chất chuyển hóa khác",
            "clearance": "Thận: thải trừ chủ yếu qua thận (metabolites)",
            "absorption": "Dạng hít: tác dụng tại chỗ. Dạng uống: hấp thu một phần.",
        },
        "storage": "Dạng hít: bảo quản ở nhiệt độ phòng (15-30°C), tránh ánh sáng trực tiếp. Dạng uống: bảo quản ở nhiệt độ phòng. Để xa tầm tay trẻ em.",
        "black_box_warnings": None,
        "drug_interactions": {
            "major": [],
            "moderate": [],
            "minor": []
        },
        "contraindications_detail": {
            "tuyệt_đối": [
                "Dị ứng với acetylcysteine"
            ],
            "tương_đối": [
                "Hen phế quản - thận trọng (dạng hít có thể gây co thắt phế quản)",
                "Loét dạ dày tá tràng - thận trọng (dạng uống)"
            ]
        },
        "pregnancy_lactation": {
            "fda_category": "B",
            "pregnancy_details": "Category B - không có nguy cơ cho thai nhi. Acetylcysteine có vẻ an toàn trong thai kỳ. Có thể được dùng khi lợi ích vượt quá nguy cơ.",
            "lactation": {
                "safety": "Compatible",
                "details": "Acetylcysteine bài tiết vào sữa mẹ ở nồng độ thấp. Nồng độ trong sữa mẹ rất thấp, không đáng kể.",
                "recommendation": "Có thể dùng khi cho con bú."
            }
        },
        "hepatic_adjustment": {
            "mild": "Không đổi",
            "moderate": "Không đổi",
            "severe": "Không đổi",
            "notes": "Acetylcysteine chuyển hóa ở gan nhưng không tích lũy ở suy gan. Không cần điều chỉnh liều."
        },
        "overdose_management": {
            "symptoms": [
                "Buồn nôn, nôn nặng (dạng uống)",
                "Co thắt phế quản nặng (dạng hít)",
                "Đau bụng",
            ],
            "antidote": "Không có antidote đặc hiệu.",
            "treatment": [
                "Ngừng ngay acetylcysteine",
                "Nếu co thắt phế quản: dùng bronchodilator (salbutamol)",
                "Điều trị triệu chứng",
            ],
            "monitoring": "Triệu chứng hô hấp, triệu chứng tiêu hóa"
        },
        "reversal_agents": {
            "available": False,
            "agents": [],
            "notes": "Không có antidote đặc hiệu. Nếu có co thắt phế quản, dùng bronchodilator (salbutamol)."
        },
        "administration_instructions": {
            "inhalation": {
                "technique": "Dùng qua máy khí dung. Hít sâu và chậm. Có thể gây co thắt phế quản ở bệnh nhân hen - cần dùng kèm với bronchodilator hoặc thận trọng.",
                "timing": "3-4 lần/ngày khi cần",
                "notes": "QUAN TRỌNG: Có thể gây co thắt phế quản ở bệnh nhân hen. Có thể dùng kèm với bronchodilator."
            },
            "oral": {
                "with_food": "Uống sau bữa ăn để giảm kích ứng dạ dày",
                "timing": "2-3 lần/ngày",
                "notes": "Uống sau bữa ăn để giảm kích ứng dạ dày."
            }
        },
        "references": {
            "primary_sources": [
                "FDA Drug Label - Mucomyst (Acetylcysteine)",
                "UpToDate - Acetylcysteine: Drug information",
                "ACCP Guidelines - Cough Management",
            ],
            "last_updated": "2025-02-19",
            "evidence_level": "B - FDA approved, widely used in clinical practice"
        }
    },
    "Ambroxol": {
        "group": "Respiratory - Mucolytic",
        "vietnamese_name": "Ambroxol, Mucosolvan, Ambrohexal",
        "administration": ["PO", "Inhalation", "Nebulizer"],
        "indications": [
            "Ho có đờm đặc, khó khạc",
            "Viêm phế quản cấp và mạn tính",
            "COPD có đờm đặc",
            "Làm tan đờm đặc",
        ],
        "contraindications": {
            "tuyệt_đối": [
                "Dị ứng với ambroxol hoặc bất kỳ thành phần nào",
            ],
            "tương_đối": [
                "Loét dạ dày tá tràng - thận trọng (dạng uống)",
                "Suy thận nặng - thận trọng",
            ],
        },
        "dosage": {
            "adult_po": "30mg x 3 lần/ngày hoặc 75mg x 2 lần/ngày (extended release)",
            "adult_inhalation": "15mg x 2-3 lần/ngày qua máy khí dung",
            "pediatric_po_12_plus": "30mg x 2-3 lần/ngày",
            "pediatric_po_5_12_years": "15mg x 3 lần/ngày",
            "pediatric_po_2_5_years": "7.5mg x 2-3 lần/ngày",
            "pediatric_po_under_2_years": "Không khuyến cáo cho trẻ <2 tuổi",
            "notes": "Dạng uống: uống sau bữa ăn để giảm kích ứng dạ dày.",
        },
        "renal_adjustment": {"normal": "Không đổi", "30_60": "Thận trọng", "under_30": "Thận trọng, có thể giảm liều", "dialysis": "Thận trọng", "notes": "Ambroxol thải trừ qua thận. Suy thận có thể tích lũy."},
        "side_effects": [
            "Buồn nôn, nôn",
            "Đau bụng",
            "Tiêu chảy",
            "Đau đầu",
            "Phát ban (hiếm)",
        ],
        "interactions": [
            "Không có tương tác thuốc quan trọng",
        ],
        "pregnancy": "C - Thận trọng trong thai kỳ",
        "risk_flags": {
            "high_alert": False,
            "narrow_therapeutic_index": False,
            "organ_toxicity": {},
            "icu_critical_care_only": False,
            "look_alike_sound_alike": []
        },
        "guideline_tags": [
            "ACCP Guidelines - Cough Management",
            "GOLD Guidelines (Global Initiative for Chronic Obstructive Lung Disease)"
        ],
        "mechanism_of_action": "Ambroxol là thuốc làm tan đờm (mucolytic), là metabolite của bromhexine. Kích thích sản xuất surfactant ở phổi, làm tăng hoạt động của lông chuyển phế quản, và làm giảm độ nhớt của đờm. Tăng tiết dịch phế quản loãng, giúp đờm dễ khạc ra ngoài. Cũng có tác dụng chống viêm nhẹ.",
        "monitoring": [
            "Triệu chứng ho có đờm (đờm loãng hơn, dễ khạc ra)",
            "Triệu chứng tiêu hóa: buồn nôn, đau bụng",
        ],
        "precautions": [
            "Dạng uống: uống sau bữa ăn để giảm kích ứng dạ dày",
            "Thận trọng ở suy thận nặng",
            "Không dùng cho ho khan (không có đờm)",
        ],
        "pharmacokinetics": {
            "half_life": "7-12 giờ",
            "onset": "30 phút - 1 giờ",
            "duration": "6-12 giờ",
            "bioavailability": "70-80% (dạng uống)",
            "protein_binding": "90%",
            "metabolism": "Gan: chuyển hóa một phần",
            "clearance": "Thận: thải trừ chủ yếu qua thận (dạng nguyên dạng và metabolites)",
            "absorption": "Hấp thu tốt sau khi uống",
        },
        "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ánh sáng trực tiếp, tránh ẩm. Để xa tầm tay trẻ em.",
        "black_box_warnings": None,
        "drug_interactions": {
            "major": [],
            "moderate": [],
            "minor": []
        },
        "contraindications_detail": {
            "tuyệt_đối": [
                "Dị ứng với ambroxol"
            ],
            "tương_đối": [
                "Loét dạ dày tá tràng - thận trọng (dạng uống)",
                "Suy thận nặng - thận trọng"
            ]
        },
        "pregnancy_lactation": {
            "fda_category": "C",
            "pregnancy_details": "Category C - có nguy cơ cho thai nhi. Ambroxol có thể ảnh hưởng đến thai nhi. Có thể được dùng khi lợi ích vượt quá nguy cơ.",
            "lactation": {
                "safety": "Compatible",
                "details": "Ambroxol bài tiết vào sữa mẹ ở nồng độ thấp. Nồng độ trong sữa mẹ rất thấp, không đáng kể.",
                "recommendation": "Có thể dùng khi cho con bú."
            }
        },
        "hepatic_adjustment": {
            "mild": "Không đổi",
            "moderate": "Thận trọng",
            "severe": "Thận trọng",
            "notes": "Ambroxol chuyển hóa một phần ở gan. Suy gan có thể ảnh hưởng nhưng thường không cần điều chỉnh liều."
        },
        "overdose_management": {
            "symptoms": [
                "Buồn nôn, nôn nặng",
                "Đau bụng",
                "Tiêu chảy",
            ],
            "antidote": "Không có antidote đặc hiệu.",
            "treatment": [
                "Ngừng ngay ambroxol",
                "Than hoạt tính nếu uống trong vòng 1-2 giờ",
                "Điều trị triệu chứng",
            ],
            "monitoring": "Triệu chứng tiêu hóa, dấu hiệu mất nước nếu nôn/tiêu chảy nhiều"
        },
        "reversal_agents": {
            "available": False,
            "agents": [],
            "notes": "Không có antidote đặc hiệu. Điều trị chủ yếu là hỗ trợ và điều trị triệu chứng."
        },
        "administration_instructions": {
            "oral": {
                "with_food": "Uống sau bữa ăn để giảm kích ứng dạ dày",
                "timing": "3 lần/ngày hoặc 2 lần/ngày (extended release)",
                "missed_dose": "Dùng ngay khi nhớ ra nếu cần",
                "notes": "Uống sau bữa ăn để giảm kích ứng dạ dày."
            },
            "inhalation": {
                "technique": "Dùng qua máy khí dung. Hít sâu và chậm.",
                "timing": "2-3 lần/ngày",
                "notes": "Dùng qua máy khí dung."
            }
        },
        "references": {
            "primary_sources": [
                "FDA Drug Label - Mucosolvan (Ambroxol)",
                "UpToDate - Ambroxol: Drug information",
                "ACCP Guidelines - Cough Management",
            ],
            "last_updated": "2025-02-19",
            "evidence_level": "B - FDA approved, widely used in clinical practice"
        }
    },
    "Bromhexine": {
        "group": "Respiratory - Mucolytic",
        "vietnamese_name": "Bromhexine, Bisolvon, Mucol",
        "administration": ["PO"],
        "indications": [
            "Ho có đờm đặc, khó khạc",
            "Viêm phế quản cấp và mạn tính",
            "COPD có đờm đặc",
            "Làm tan đờm đặc",
        ],
        "contraindications": {
            "tuyệt_đối": [
                "Dị ứng với bromhexine hoặc bất kỳ thành phần nào",
            ],
            "tương_đối": [
                "Loét dạ dày tá tràng - thận trọng",
                "Suy thận nặng - thận trọng",
            ],
        },
        "dosage": {
            "adult_po": "8mg x 3 lần/ngày hoặc 16mg x 2 lần/ngày",
            "pediatric_po_12_plus": "8mg x 2-3 lần/ngày",
            "pediatric_po_5_12_years": "4mg x 3 lần/ngày",
            "pediatric_po_under_5_years": "Không khuyến cáo cho trẻ <5 tuổi",
            "notes": "Uống sau bữa ăn để giảm kích ứng dạ dày.",
        },
        "renal_adjustment": {"normal": "Không đổi", "30_60": "Thận trọng", "under_30": "Thận trọng, có thể giảm liều", "dialysis": "Thận trọng", "notes": "Bromhexine thải trừ qua thận. Suy thận có thể tích lũy."},
        "side_effects": [
            "Buồn nôn, nôn",
            "Đau bụng",
            "Tiêu chảy",
            "Đau đầu",
            "Chóng mặt",
        ],
        "interactions": [
            "Không có tương tác thuốc quan trọng",
        ],
        "pregnancy": "C - Thận trọng trong thai kỳ",
        "risk_flags": {
            "high_alert": False,
            "narrow_therapeutic_index": False,
            "organ_toxicity": {},
            "icu_critical_care_only": False,
            "look_alike_sound_alike": []
        },
        "guideline_tags": [
            "ACCP Guidelines - Cough Management",
            "GOLD Guidelines (Global Initiative for Chronic Obstructive Lung Disease)"
        ],
        "mechanism_of_action": "Bromhexine là thuốc làm tan đờm (mucolytic). Kích thích sản xuất surfactant ở phổi, làm tăng hoạt động của lông chuyển phế quản, và làm giảm độ nhớt của đờm. Tăng tiết dịch phế quản loãng, giúp đờm dễ khạc ra ngoài. Ambroxol là metabolite hoạt động của bromhexine và có tác dụng tương tự.",
        "monitoring": [
            "Triệu chứng ho có đờm (đờm loãng hơn, dễ khạc ra)",
            "Triệu chứng tiêu hóa: buồn nôn, đau bụng",
        ],
        "precautions": [
            "Uống sau bữa ăn để giảm kích ứng dạ dày",
            "Thận trọng ở suy thận nặng",
            "Không dùng cho ho khan (không có đờm)",
        ],
        "pharmacokinetics": {
            "half_life": "12 giờ",
            "onset": "1-2 giờ",
            "duration": "6-8 giờ",
            "bioavailability": "70-80%",
            "protein_binding": "Không rõ",
            "metabolism": "Gan: chuyển hóa thành ambroxol (active metabolite) và các chất chuyển hóa khác",
            "clearance": "Thận: thải trừ chủ yếu qua thận (metabolites)",
            "absorption": "Hấp thu tốt sau khi uống",
        },
        "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ánh sáng trực tiếp, tránh ẩm. Để xa tầm tay trẻ em.",
        "black_box_warnings": None,
        "drug_interactions": {
            "major": [],
            "moderate": [],
            "minor": []
        },
        "contraindications_detail": {
            "tuyệt_đối": [
                "Dị ứng với bromhexine"
            ],
            "tương_đối": [
                "Loét dạ dày tá tràng - thận trọng",
                "Suy thận nặng - thận trọng"
            ]
        },
        "pregnancy_lactation": {
            "fda_category": "C",
            "pregnancy_details": "Category C - có nguy cơ cho thai nhi. Bromhexine có thể ảnh hưởng đến thai nhi. Có thể được dùng khi lợi ích vượt quá nguy cơ.",
            "lactation": {
                "safety": "Compatible",
                "details": "Bromhexine bài tiết vào sữa mẹ ở nồng độ thấp. Nồng độ trong sữa mẹ rất thấp, không đáng kể.",
                "recommendation": "Có thể dùng khi cho con bú."
            }
        },
        "hepatic_adjustment": {
            "mild": "Không đổi",
            "moderate": "Thận trọng",
            "severe": "Thận trọng",
            "notes": "Bromhexine chuyển hóa ở gan thành ambroxol. Suy gan có thể ảnh hưởng nhưng thường không cần điều chỉnh liều."
        },
        "overdose_management": {
            "symptoms": [
                "Buồn nôn, nôn nặng",
                "Đau bụng",
                "Tiêu chảy",
            ],
            "antidote": "Không có antidote đặc hiệu.",
            "treatment": [
                "Ngừng ngay bromhexine",
                "Than hoạt tính nếu uống trong vòng 1-2 giờ",
                "Điều trị triệu chứng",
            ],
            "monitoring": "Triệu chứng tiêu hóa, dấu hiệu mất nước nếu nôn/tiêu chảy nhiều"
        },
        "reversal_agents": {
            "available": False,
            "agents": [],
            "notes": "Không có antidote đặc hiệu. Điều trị chủ yếu là hỗ trợ và điều trị triệu chứng."
        },
        "administration_instructions": {
            "oral": {
                "with_food": "Uống sau bữa ăn để giảm kích ứng dạ dày",
                "timing": "3 lần/ngày hoặc 2 lần/ngày",
                "missed_dose": "Dùng ngay khi nhớ ra nếu cần",
                "notes": "Uống sau bữa ăn để giảm kích ứng dạ dày."
            }
        },
        "references": {
            "primary_sources": [
                "FDA Drug Label - Bisolvon (Bromhexine)",
                "UpToDate - Bromhexine: Drug information",
                "ACCP Guidelines - Cough Management",
            ],
            "last_updated": "2025-02-19",
            "evidence_level": "B - FDA approved, widely used in clinical practice"
        }
    },
    "Guaifenesin/Dextromethorphan": {
        "group": "Respiratory - Fixed-dose Combination (Expectorant/Antitussive)",
        "vietnamese_name": "Guaifenesin/Dextromethorphan, Robitussin DM, Mucinex DM",
        "administration": ["PO"],
        "indications": [
            "Ho có đờm (guaifenesin làm loãng đờm, dextromethorphan giảm ho)",
            "Viêm phế quản cấp và mạn tính",
            "Ho do cảm lạnh, cúm",
        ],
        "contraindications": {
            "tuyệt_đối": [
                "Dị ứng với guaifenesin, dextromethorphan hoặc bất kỳ thành phần nào",
                "Đang dùng MAO inhibitors (trong vòng 14 ngày)",
            ],
            "tương_đối": [
                "Hen phế quản - thận trọng",
                "Suy gan nặng - thận trọng",
                "Suy thận nặng - thận trọng",
                "Đang dùng SSRI, SNRI - thận trọng (tăng nguy cơ serotonin syndrome)",
            ],
        },
        "dosage": {
            "adult_po": "Guaifenesin 200-400mg/Dextromethorphan 10-20mg x 3-4 lần/ngày (mỗi 4-6 giờ)",
            "pediatric_po_12_plus": "Guaifenesin 200mg/Dextromethorphan 10mg x 3-4 lần/ngày",
            "pediatric_po_6_12_years": "Guaifenesin 100mg/Dextromethorphan 5mg x 3-4 lần/ngày",
            "pediatric_po_under_6_years": "Không khuyến cáo cho trẻ <6 tuổi",
            "notes": "Uống nhiều nước để tăng hiệu quả của guaifenesin. Dùng khi cần.",
        },
        "renal_adjustment": {"normal": "Không đổi", "30_60": "Thận trọng", "under_30": "Thận trọng", "dialysis": "Thận trọng", "notes": "Cả hai thành phần thải trừ qua thận. Suy thận có thể tích lũy."},
        "side_effects": [
            "Buồn ngủ, chóng mặt (dextromethorphan)",
            "Buồn nôn, nôn",
            "Đau bụng",
            "Kích động, ảo giác (dextromethorphan, liều cao)",
        ],
        "interactions": [
            "MAO inhibitors: CHỐNG CHỈ ĐỊNH (tăng nguy cơ serotonin syndrome nghiêm trọng)",
            "SSRI, SNRI: tăng nguy cơ serotonin syndrome",
            "Alcohol: tăng tác dụng ức chế thần kinh trung ương",
        ],
        "pregnancy": "C - Thận trọng trong thai kỳ",
        "risk_flags": {
            "high_alert": False,
            "narrow_therapeutic_index": False,
            "organ_toxicity": {},
            "icu_critical_care_only": False,
            "look_alike_sound_alike": []
        },
        "guideline_tags": [
            "ACCP Guidelines - Cough Management",
            "GOLD Guidelines (Global Initiative for Chronic Obstructive Lung Disease)"
        ],
        "mechanism_of_action": "Kết hợp guaifenesin (expectorant) làm loãng đờm và dextromethorphan (antitussive) giảm ho. Guaifenesin kích thích tiết dịch phế quản, làm loãng đờm. Dextromethorphan ức chế trung tâm ho. Phù hợp cho ho có đờm khi cần vừa làm loãng đờm vừa giảm ho.",
        "monitoring": [
            "Triệu chứng ho có đờm (đờm loãng hơn, dễ khạc ra, giảm ho)",
            "Dấu hiệu serotonin syndrome nếu dùng với SSRI/SNRI",
            "Dấu hiệu quá liều: kích động, ảo giác",
        ],
        "precautions": [
            "CHỐNG CHỈ ĐỊNH với MAO inhibitors (trong vòng 14 ngày)",
            "Uống nhiều nước để tăng hiệu quả của guaifenesin - QUAN TRỌNG",
            "Thận trọng với SSRI, SNRI - tăng nguy cơ serotonin syndrome",
            "Tránh dùng với alcohol",
            "Thận trọng khi lái xe hoặc vận hành máy móc (buồn ngủ)",
        ],
        "pharmacokinetics": {
            "half_life": "Guaifenesin: 1 giờ; Dextromethorphan: 2-4 giờ",
            "onset": "Guaifenesin: 30 phút - 1 giờ; Dextromethorphan: 15-30 phút",
            "duration": "Guaifenesin: 4 giờ; Dextromethorphan: 3-6 giờ",
            "protein_binding": "Guaifenesin: không đáng kể; Dextromethorphan: không đáng kể",
            "clearance": "Cả hai thải trừ qua thận",
        },
        "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ánh sáng trực tiếp, tránh ẩm. Để xa tầm tay trẻ em.",
        "black_box_warnings": "CHỐNG CHỈ ĐỊNH với MAO inhibitors (trong vòng 14 ngày) - tăng nguy cơ serotonin syndrome nghiêm trọng.",
        "drug_interactions": {
            "major": [
                {
                    "drug": "MAO inhibitors",
                    "mechanism": "Tăng nguy cơ serotonin syndrome",
                    "effect": "Tăng nguy cơ serotonin syndrome nghiêm trọng",
                    "management": "CHỐNG CHỈ ĐỊNH TUYỆT ĐỐI."
                }
            ],
            "moderate": [
                {
                    "drug": "SSRI, SNRI",
                    "mechanism": "Tăng nguy cơ serotonin syndrome",
                    "effect": "Tăng nguy cơ serotonin syndrome",
                    "management": "Thận trọng. Theo dõi dấu hiệu serotonin syndrome."
                }
            ],
            "minor": []
        },
        "contraindications_detail": {
            "tuyệt_đối": [
                "Dị ứng với guaifenesin, dextromethorphan",
                "Đang dùng MAO inhibitors (trong vòng 14 ngày) - CHỐNG CHỈ ĐỊNH TUYỆT ĐỐI"
            ],
            "tương_đối": [
                "Hen phế quản - thận trọng",
                "Suy gan nặng - thận trọng",
                "Suy thận nặng - thận trọng",
                "Đang dùng SSRI, SNRI - thận trọng"
            ]
        },
        "pregnancy_lactation": {
            "fda_category": "C",
            "pregnancy_details": "Category C - có nguy cơ cho thai nhi. Có thể được dùng khi lợi ích vượt quá nguy cơ.",
            "lactation": {
                "safety": "Compatible with monitoring",
                "details": "Cả hai thành phần bài tiết vào sữa mẹ ở nồng độ thấp.",
                "recommendation": "Có thể dùng khi cho con bú với liều thường dùng."
            }
        },
        "hepatic_adjustment": {
            "mild": "Không đổi",
            "moderate": "Thận trọng",
            "severe": "Thận trọng",
            "notes": "Cả hai thành phần chuyển hóa ở gan. Suy gan có thể tích lũy."
        },
        "overdose_management": {
            "symptoms": [
                "Kích động, ảo giác (dextromethorphan)",
                "Buồn nôn, nôn nặng",
                "Buồn ngủ nặng",
            ],
            "antidote": "Không có antidote đặc hiệu.",
            "treatment": [
                "Ngừng ngay thuốc",
                "Than hoạt tính nếu uống trong vòng 1-2 giờ",
                "Điều trị triệu chứng",
            ],
            "monitoring": "Triệu chứng thần kinh, triệu chứng tiêu hóa"
        },
        "reversal_agents": {
            "available": False,
            "agents": [],
            "notes": "Không có antidote đặc hiệu. Điều trị chủ yếu là hỗ trợ và điều trị triệu chứng."
        },
        "administration_instructions": {
            "oral": {
                "with_food": "Có thể uống với hoặc không có thức ăn",
                "timing": "Mỗi 4-6 giờ khi cần, không quá 4 lần/ngày",
                "missed_dose": "Dùng ngay khi nhớ ra nếu cần",
                "notes": "QUAN TRỌNG: Uống nhiều nước để tăng hiệu quả của guaifenesin."
            }
        },
        "references": {
            "primary_sources": [
                "FDA Drug Label - Robitussin DM (Guaifenesin/Dextromethorphan)",
                "UpToDate - Guaifenesin/Dextromethorphan: Drug information",
                "ACCP Guidelines - Cough Management",
            ],
            "last_updated": "2025-02-19",
            "evidence_level": "B - FDA approved, widely used in clinical practice"
        }
    }
}

__all__ = ["COUGH_EXPECTORANTS_MUCOLYTICS_DRUGS"]
