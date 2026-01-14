"""
Neurology / Psychiatry Combination Drugs
Thuốc phối hợp tuần hoàn não, nootropic, và tâm thần kinh.
Ví dụ: Piracetam + Vinpocetine, Citicoline + Piracetam, Ginkgo + Vinpocetine, Olanzapine/Fluoxetine.
"""

NEUROLOGICAL_COMBINATIONS_DRUGS = {
    "Citicoline/Piracetam": {
        "group": "Neurology - Combination (Neuroprotective + Nootropic)",
        "vietnamese_name": "Citicoline/Piracetam (phối hợp tuần hoàn não)",
        "administration": ["PO", "IV"],
        "indications": [
            "Hỗ trợ phục hồi sau đột quỵ thiếu máu não",
            "Rối loạn nhận thức nhẹ sau chấn thương sọ não hoặc ở người cao tuổi",
        ],
        "contraindications": [
            "Suy thận nặng (do piracetam)",
            "Xuất huyết não đang hoạt động",
            "Dị ứng với bất kỳ thành phần nào",
        ],
        "dosage": {
            "adult_po": "Citicoline 500-1000mg + Piracetam 2.4-4.8g/ngày chia 2-3 lần (tùy chế phẩm)",
            "notes": "Dùng như thuốc hỗ trợ, không thay thế điều trị chuẩn (tái tưới máu, kiểm soát HA, statin…).",
        },
        "renal_adjustment": {
            "normal": "Không cần chỉnh liều (theo dõi piracetam)",
            "30_60": "Giảm liều piracetam 50%",
            "under_30": "Tránh dùng (piracetam)",
        },
        "side_effects": [
            "Đau đầu, mất ngủ nhẹ",
            "Buồn nôn, khó chịu tiêu hóa",
        ],
        "interactions": [
            "Ít tương tác đáng kể; thận trọng khi phối hợp với nhiều nootropic khác.",
        ],
        "pregnancy": "C - tránh dùng thường quy",
        "risk_flags": {
            "high_alert": False,
            "narrow_therapeutic_index": False,
            "organ_toxicity": {},
            "icu_critical_care_only": False,
            "look_alike_sound_alike": []
        },
        "guideline_tags": [],
        "mechanism_of_action": "Citicoline ổn định màng tế bào thần kinh, piracetam cải thiện tính linh động màng và huyết lưu não. Phối hợp được dùng rộng rãi như thuốc hỗ trợ trong phục hồi thần kinh.",
        "monitoring": [
            "Đánh giá chức năng thần kinh, nhận thức",
            "Chức năng thận ở người cao tuổi",
        ],
        "precautions": [
            "Hiệu quả dài hạn còn gây tranh cãi; cân nhắc thời gian điều trị.",
        ],
        "pharmacokinetics": {
            "half_life": "Citicoline: 3-4 giờ; Piracetam: 4-5 giờ",
            "onset": "Vài giờ sau khi uống",
            "duration": "Tác dụng kéo dài nhờ piracetam",
            "protein_binding": "Citicoline: thấp; Piracetam: <10%",
            "clearance": "Citicoline: chuyển hóa thành choline và cytidine, thải qua thận; Piracetam: thải trừ chủ yếu qua thận (dạng nguyên dạng)"
        },
        "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ánh sáng trực tiếp, tránh ẩm. Để xa tầm tay trẻ em. Kiểm tra hạn sử dụng trước khi dùng.",
        "black_box_warnings": None,
        "drug_interactions": {
            "major": [],
            "moderate": [],
            "minor": []
        },
        "contraindications": {
            "tuyệt_đối": [
                "Suy thận nặng (do piracetam)",
                "Xuất huyết não đang hoạt động",
                "Dị ứng với bất kỳ thành phần nào"
            ],
            "tương_đối": [
                "Suy thận nhẹ đến trung bình - giảm liều piracetam 50%"
            ]
        },
        "pregnancy_lactation": {
            "fda_category": "C",
            "pregnancy_details": "Category C - tránh dùng thường quy. Dữ liệu an toàn thai kỳ hạn chế.",
            "lactation": {
                "safety": "Compatible with monitoring",
                "details": "Dữ liệu hạn chế.",
                "recommendation": "Thận trọng khi cho con bú."
            }
        },
        "hepatic_adjustment": {
            "mild": "Không đổi",
            "moderate": "Thận trọng",
            "severe": "Thận trọng",
            "notes": "Citicoline và piracetam chủ yếu thải trừ qua thận. Suy gan ít ảnh hưởng."
        },
        "overdose_management": {
            "symptoms": [
                "Đau đầu nặng",
                "Buồn nôn nặng",
                "Rối loạn tiêu hóa nặng"
            ],
            "antidote": "Không có antidote đặc hiệu",
            "treatment": [
                "Ngừng ngay thuốc",
                "Rửa dạ dày nếu uống trong vòng 1-2 giờ",
                "Than hoạt tính",
                "Điều trị hỗ trợ và điều trị triệu chứng"
            ],
            "monitoring": "Triệu chứng lâm sàng, chức năng thận"
        },
        "reversal_agents": {
            "available": False,
            "agents": []
        },
        "administration_instructions": {
            "oral": {
                "with_food": "Có thể uống với hoặc không có thức ăn",
                "timing": "Chia 2-3 lần/ngày (tùy chế phẩm)",
                "notes": "Dùng như thuốc hỗ trợ, không thay thế điều trị chuẩn. Hiệu quả dài hạn còn gây tranh cãi."
            },
            "iv": {
                "reconstitution": "Pha trong Normal saline hoặc D5W theo hướng dẫn",
                "infusion_rate": "Truyền trong 30-60 phút",
                "compatibility": ["Normal saline (0.9% NaCl)", "D5W"],
                "incompatibility": [],
                "notes": "Theo protocol cụ thể. Dùng như thuốc hỗ trợ."
            }
        },
        "references": {
            "primary_sources": [
                "FDA Drug Label - Cần cập nhật",
                "UpToDate - Cần cập nhật"
            ],
            "last_updated": "2025-02-05",
            "evidence_level": "C - Bằng chứng hạn chế"
        },
},
    "Ginkgo biloba/Vinpocetine": {
        "group": "Neurology - Combination (Herbal vasomodulator + Cerebral vasodilator)",
        "vietnamese_name": "Ginkgo biloba/Vinpocetine (phối hợp mạch não)",
        "administration": ["PO"],
        "indications": [
            "Rối loạn tuần hoàn não, chóng mặt, ù tai (dùng hỗ trợ, bằng chứng hạn chế)",
        ],
        "contraindications": [
            "Đang chảy máu hoạt động",
            "Dùng chống đông/kháng tiểu cầu liều cao",
            "Thai kỳ, cho con bú",
        ],
        "dosage": {
            "adult_po": "Ví dụ: Ginkgo 40-80mg + Vinpocetine 5mg x 2-3 lần/ngày (tùy chế phẩm)",
            "notes": "Ngưng trước phẫu thuật 5-7 ngày do nguy cơ chảy máu (Ginkgo).",
        },
        "renal_adjustment": {
            "normal": "Không cần chỉnh",
            "30_60": "Không cần chỉnh (thận trọng nếu nhiều bệnh kèm)",
            "under_30": "Thận trọng, dữ liệu hạn chế",
        },
        "side_effects": [
            "Đau đầu, rối loạn tiêu hóa",
            "Chảy máu (hiếm, nhưng tăng nếu dùng kèm chống đông)",
            "Đỏ mặt, đánh trống ngực (do vinpocetine)",
        ],
        "interactions": [
            "Warfarin, DOACs, Aspirin, Clopidogrel: tăng nguy cơ chảy máu.",
        ],
        "pregnancy": "Contraindicated",
        "risk_flags": {
            "high_alert": False,
            "narrow_therapeutic_index": False,
            "organ_toxicity": {"hematologic": True},
            "icu_critical_care_only": False,
            "look_alike_sound_alike": []
        },
        "guideline_tags": [],
        "mechanism_of_action": "Ginkgo biloba có tác dụng chống oxy hóa, điều hòa trương lực mạch và ức chế kết tập tiểu cầu nhẹ; vinpocetine giãn mạch não. Phối hợp chủ yếu mang tính hỗ trợ, không thay thế điều trị chuẩn.",
        "monitoring": [
            "Dấu hiệu chảy máu (bầm tím, chảy máu cam, phân đen…) nếu dùng kèm chống đông.",
            "Huyết áp, nhịp tim.",
        ],
        "precautions": [
            "Không dùng ở bệnh nhân có nguy cơ chảy máu cao.",
            "Ngưng trước phẫu thuật.",
        ],
        "pharmacokinetics": {
            "half_life": "Ginkgo biloba: 4-6 giờ; Vinpocetine: 1-2 giờ",
            "onset": "Vài giờ sau khi uống",
            "duration": "Tác dụng kéo dài nhờ ginkgo biloba",
            "protein_binding": "Ginkgo biloba: không rõ; Vinpocetine: ~66%",
            "clearance": "Ginkgo biloba: chuyển hóa gan, thải qua thận; Vinpocetine: chuyển hóa gan, thải qua thận"
        },
        "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ánh sáng trực tiếp, tránh ẩm. Để xa tầm tay trẻ em. Kiểm tra hạn sử dụng trước khi dùng.",
        "black_box_warnings": "Nguy cơ chảy máu khi dùng kèm thuốc chống đông/kháng tiểu cầu. Ngưng trước phẫu thuật 5-7 ngày.",
             "drug_interactions": {
             "major": [
                 {
                     "drug": "Warfarin, DOACs, Aspirin, Clopidogrel: tăng nguy cơ chảy máu.",
                     "mechanism": "Tăng nguy cơ chảy máu"
                 }
             ],
             "moderate": [],
             "minor": []
         },
         "pregnancy_lactation": {
             "fda_category": "Contraindicated",
             "pregnancy_details": "Category Contraindicated - Cần tra cứu thêm thông tin chi tiết về sử dụng trong thai kỳ.",
             "lactation": {
                 "safety": "Use with caution",
                 "details": "Cần tra cứu thêm thông tin chi tiết về bài tiết vào sữa mẹ.",
                 "recommendation": "Thận trọng khi cho con bú, tra cứu thêm thông tin."
             }
         },
         "hepatic_adjustment": {
             "mild": "Không đổi",
             "moderate": "Thận trọng",
             "severe": "Thận trọng, có thể giảm liều",
             "notes": "Cần tra cứu thêm thông tin chi tiết về điều chỉnh liều ở suy gan."
         },
         "overdose_management": {
             "symptoms": [
                 "Cần tra cứu thêm thông tin về triệu chứng quá liều"
             ],
             "antidote": "Không có antidote đặc hiệu",
             "treatment": [
                 "Ngừng ngay thuốc",
                 "Rửa dạ dày nếu uống trong vòng 1-2 giờ (nếu phù hợp)",
                 "Than hoạt tính",
                 "Điều trị hỗ trợ và điều trị triệu chứng",
                 "Theo dõi dấu hiệu sinh tồn"
             ],
             "monitoring": "Theo dõi dấu hiệu sinh tồn, triệu chứng lâm sàng"
         },
         "reversal_agents": {
             "available": False,
             "agents": []
         },
         "administration_instructions": {
             "oral": {
                 "with_food": "Có thể uống với hoặc không có thức ăn (trừ khi có chỉ định khác)",
                 "timing": "Theo chỉ định của bác sĩ",
                 "notes": "Cần tra cứu thêm thông tin chi tiết về cách dùng."
             }
         },
         "references": {
             "primary_sources": [
                 "FDA Drug Label - Ginkgo biloba/Vinpocetine",
                 "UpToDate - Cần cập nhật"
             ],
             "last_updated": "2025-12-28",
             "evidence_level": "C - Cần tra cứu và cập nhật"
         },
},
    "Olanzapine/Fluoxetine": {
        "group": "Psychiatry - Combination (Atypical antipsychotic + SSRI)",
        "vietnamese_name": "Olanzapine/Fluoxetine, Symbyax",
        "administration": ["PO"],
        "indications": [
            "Trầm cảm lưỡng cực (bipolar depression)",
            "Trầm cảm kháng trị (treatment-resistant depression) – khi các lựa chọn khác thất bại",
        ],
        "contraindications": [
            "Dị ứng olanzapine hoặc fluoxetine",
            "Dùng MAO inhibitor hiện tại hoặc trong vòng 14 ngày",
            "QT kéo dài nặng, rối loạn nhịp thất không kiểm soát",
        ],
        "dosage": {
            "adult_bipolar_depression": "Olanzapine 6-12mg + Fluoxetine 25-50mg x 1 lần/ngày (tối); titration tùy đáp ứng",
            "notes": "Liều và tỉ lệ cụ thể tùy chế phẩm; bắt đầu thấp và tăng dần để giảm tác dụng phụ.",
        },
        "renal_adjustment": {
            "normal": "Không cần chỉnh",
            "30_60": "Thận trọng (ít dữ liệu, nhưng thường không cần chỉnh nhiều)",
            "under_30": "Thận trọng, theo dõi tác dụng phụ",
        },
        "side_effects": [
            "Tăng cân, tăng lipid, tăng đường huyết (do olanzapine)",
            "Buồn ngủ, an thần",
            "Buồn nôn, tiêu chảy (do fluoxetine)",
            "Hội chứng serotonin (hiếm nhưng nguy hiểm)",
        ],
        "interactions": [
            "MAOIs, linezolid, triptan, other serotonergic drugs: nguy cơ serotonin syndrome.",
            "Thuốc kéo dài QT: tăng nguy cơ loạn nhịp.",
        ],
        "pregnancy": "C/D (tùy tam cá nguyệt và chỉ định) – dùng khi lợi ích vượt trội nguy cơ.",
        "risk_flags": {
            "high_alert": True,
            "narrow_therapeutic_index": False,
            "organ_toxicity": {"metabolic": True, "cardiac": True},
            "icu_critical_care_only": False,
            "look_alike_sound_alike": []
        },
        "guideline_tags": [
            "APA Guidelines (American Psychiatric Association)",
            "CANMAT Guidelines (Canadian Network for Mood and Anxiety Treatments)"
        ],
        "mechanism_of_action": "Olanzapine đối kháng D2/5-HT2A; fluoxetine ức chế tái thu hồi serotonin. Phối hợp tăng hiệu quả điều trị trầm cảm lưỡng cực/kháng trị nhưng tăng nguy cơ tác dụng phụ chuyển hóa.",
        "monitoring": [
            "Cân nặng, BMI, vòng bụng",
            "Glucose, HbA1c, lipid máu",
            "ECG nếu có nguy cơ QT kéo dài",
            "Triệu chứng trầm cảm, ý tưởng tự sát",
        ],
        "precautions": [
            "Theo dõi hội chứng serotonin khi dùng với các thuốc serotonergic khác.",
            "Theo dõi sát chuyển hóa (tăng cân, tăng đường, tăng lipid).",
        ],
        "pharmacokinetics": {
            "half_life": "Olanzapine: 30 giờ; Fluoxetine: 4-6 ngày (chất chuyển hóa norfluoxetine: 4-16 ngày)",
            "onset": "Vài tuần để đạt hiệu quả đầy đủ",
            "duration": "Dùng 1 lần/ngày nhờ half-life dài",
            "protein_binding": "Olanzapine: 93%; Fluoxetine: 94.5%",
            "clearance": "Olanzapine: chuyển hóa gan (CYP1A2, CYP2D6), thải qua thận; Fluoxetine: chuyển hóa gan (CYP2D6, CYP2C9) thành norfluoxetine (hoạt tính), thải qua thận"
        },
        "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ánh sáng trực tiếp, tránh ẩm. Để xa tầm tay trẻ em. Kiểm tra hạn sử dụng trước khi dùng.",
        "black_box_warnings": "Nguy cơ tăng cân, tăng đường huyết, tăng lipid máu (do olanzapine). Nguy cơ hội chứng serotonin khi dùng với các thuốc serotonergic khác. Tăng nguy cơ tự sát ở trẻ em, thanh thiếu niên và người trẻ tuổi.",
             "drug_interactions": {
             "major": [],
             "moderate": [],
             "minor": [
                 {
                     "drug": "MAOIs, linezolid, triptan, other serotonergic drugs: nguy cơ serotonin syndrome.",
                     "mechanism": "Tương tác lâm sàng"
                 },
                 {
                     "drug": "Thuốc kéo dài QT: tăng nguy cơ loạn nhịp.",
                     "mechanism": "Tương tác lâm sàng"
                 }
             ]
         },
         "pregnancy_lactation": {
             "fda_category": "C/D (tùy tam cá nguyệt và chỉ định) – dùng khi lợi ích vượt trội nguy cơ.",
             "pregnancy_details": "Category C/D (tùy tam cá nguyệt và chỉ định) – dùng khi lợi ích vượt trội nguy cơ. - Cần tra cứu thêm thông tin chi tiết về sử dụng trong thai kỳ.",
             "lactation": {
                 "safety": "Use with caution",
                 "details": "Cần tra cứu thêm thông tin chi tiết về bài tiết vào sữa mẹ.",
                 "recommendation": "Thận trọng khi cho con bú, tra cứu thêm thông tin."
             }
         },
         "hepatic_adjustment": {
             "mild": "Không đổi",
             "moderate": "Thận trọng",
             "severe": "Thận trọng, có thể giảm liều",
             "notes": "Cần tra cứu thêm thông tin chi tiết về điều chỉnh liều ở suy gan."
         },
         "overdose_management": {
             "symptoms": [
                 "Cần tra cứu thêm thông tin về triệu chứng quá liều"
             ],
             "antidote": "Không có antidote đặc hiệu",
             "treatment": [
                 "Ngừng ngay thuốc",
                 "Rửa dạ dày nếu uống trong vòng 1-2 giờ (nếu phù hợp)",
                 "Than hoạt tính",
                 "Điều trị hỗ trợ và điều trị triệu chứng",
                 "Theo dõi dấu hiệu sinh tồn"
             ],
             "monitoring": "Theo dõi dấu hiệu sinh tồn, triệu chứng lâm sàng"
         },
         "reversal_agents": {
             "available": False,
             "agents": []
         },
         "administration_instructions": {
             "oral": {
                 "with_food": "Có thể uống với hoặc không có thức ăn (trừ khi có chỉ định khác)",
                 "timing": "Theo chỉ định của bác sĩ",
                 "notes": "Cần tra cứu thêm thông tin chi tiết về cách dùng."
             }
         },
         "references": {
             "primary_sources": [
                 "FDA Drug Label - Olanzapine/Fluoxetine",
                 "UpToDate - Cần cập nhật"
             ],
             "last_updated": "2025-12-28",
             "evidence_level": "C - Cần tra cứu và cập nhật"
         },
},
    "Piracetam/Vinpocetine": {
        "group": "Neurology - Combination (Nootropic + Cerebral vasodilator)",
        "vietnamese_name": "Piracetam/Vinpocetine (phối hợp tuần hoàn não)",
        "administration": ["PO"],
        "indications": [
            "Thiếu máu não mạn, chóng mặt, suy giảm trí nhớ nhẹ (dùng phổ biến tại VN, bằng chứng hạn chế)",
        ],
        "contraindications": [
            "Suy thận nặng (do thành phần piracetam)",
            "Xuất huyết não cấp",
            "Thai kỳ (do thành phần vinpocetine)",
        ],
        "dosage": {
            "adult_po": "Ví dụ: Piracetam 800mg + Vinpocetine 5mg x 2-3 lần/ngày (tùy chế phẩm cụ thể)",
            "notes": "Liều cụ thể phụ thuộc từng biệt dược; nguyên tắc giống khi dùng riêng lẻ hai thuốc.",
        },
        "renal_adjustment": {
            "normal": "Không cần chỉnh (nếu chức năng thận bình thường)",
            "30_60": "Giảm liều theo thành phần piracetam (giảm 1/2 liều)",
            "under_30": "Tránh dùng (piracetam thải trừ thận)",
        },
        "side_effects": [
            "Nhức đầu, mất ngủ nhẹ (do piracetam)",
            "Đỏ mặt, đánh trống ngực, hạ huyết áp nhẹ (do vinpocetine)",
            "Rối loạn tiêu hóa nhẹ",
        ],
        "interactions": [
            "Thuốc chống đông/kháng tiểu cầu: lý thuyết tăng nguy cơ chảy máu",
        ],
        "pregnancy": "Contraindicated (đặc biệt do vinpocetine)",
        "risk_flags": {
            "high_alert": False,
            "narrow_therapeutic_index": False,
            "organ_toxicity": {},
            "icu_critical_care_only": False,
            "look_alike_sound_alike": []
        },
        "guideline_tags": [],
        "mechanism_of_action": "Kết hợp nootropic (piracetam – cải thiện chuyển hóa thần kinh/vi tuần hoàn) và giãn mạch não (vinpocetine). Bằng chứng lâm sàng về cải thiện kết cục dài hạn còn hạn chế, chủ yếu dùng hỗ trợ.",
        "monitoring": [
            "Huyết áp, nhịp tim ở bệnh nhân lớn tuổi",
            "Chức năng thận (piracetam)",
        ],
        "precautions": [
            "Không thay thế điều trị chuẩn cho đột quỵ hoặc bệnh mạch máu não.",
            "Tránh dùng ở phụ nữ có thai, cho con bú.",
        ],
        "pharmacokinetics": {
            "half_life": "Piracetam: 4-5 giờ; Vinpocetine: 1-2 giờ",
            "onset": "Vài giờ sau khi uống",
            "duration": "Tác dụng kéo dài nhờ piracetam",
            "protein_binding": "Piracetam: <10%; Vinpocetine: ~66%",
            "clearance": "Piracetam: thải trừ chủ yếu qua thận (dạng nguyên dạng); Vinpocetine: chuyển hóa gan, thải qua thận"
        },
        "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ánh sáng trực tiếp, tránh ẩm. Để xa tầm tay trẻ em. Kiểm tra hạn sử dụng trước khi dùng.",
        "black_box_warnings": None,
             "drug_interactions": {
             "major": [
                 {
                     "drug": "Thuốc chống đông/kháng tiểu cầu: lý thuyết tăng nguy cơ chảy máu",
                     "mechanism": "Tăng nguy cơ chảy máu"
                 }
             ],
             "moderate": [],
             "minor": []
         },
         "pregnancy_lactation": {
             "fda_category": "Contraindicated (đặc biệt do vinpocetine)",
             "pregnancy_details": "Category Contraindicated (đặc biệt do vinpocetine) - Cần tra cứu thêm thông tin chi tiết về sử dụng trong thai kỳ.",
             "lactation": {
                 "safety": "Use with caution",
                 "details": "Cần tra cứu thêm thông tin chi tiết về bài tiết vào sữa mẹ.",
                 "recommendation": "Thận trọng khi cho con bú, tra cứu thêm thông tin."
             }
         },
         "hepatic_adjustment": {
             "mild": "Không đổi",
             "moderate": "Thận trọng",
             "severe": "Thận trọng, có thể giảm liều",
             "notes": "Cần tra cứu thêm thông tin chi tiết về điều chỉnh liều ở suy gan."
         },
         "overdose_management": {
             "symptoms": [
                 "Cần tra cứu thêm thông tin về triệu chứng quá liều"
             ],
             "antidote": "Không có antidote đặc hiệu",
             "treatment": [
                 "Ngừng ngay thuốc",
                 "Rửa dạ dày nếu uống trong vòng 1-2 giờ (nếu phù hợp)",
                 "Than hoạt tính",
                 "Điều trị hỗ trợ và điều trị triệu chứng",
                 "Theo dõi dấu hiệu sinh tồn"
             ],
             "monitoring": "Theo dõi dấu hiệu sinh tồn, triệu chứng lâm sàng"
         },
         "reversal_agents": {
             "available": False,
             "agents": []
         },
         "administration_instructions": {
             "oral": {
                 "with_food": "Có thể uống với hoặc không có thức ăn (trừ khi có chỉ định khác)",
                 "timing": "Theo chỉ định của bác sĩ",
                 "notes": "Cần tra cứu thêm thông tin chi tiết về cách dùng."
             }
         },
         "references": {
             "primary_sources": [
                 "FDA Drug Label - Piracetam/Vinpocetine",
                 "UpToDate - Cần cập nhật"
             ],
             "last_updated": "2025-12-28",
             "evidence_level": "C - Cần tra cứu và cập nhật"
         },
},
    "Perphenazine/Amitriptyline":     {
        "group": "Psychiatry - Combination (Typical Antipsychotic + TCA)",
        "vietnamese_name": "Perphenazine/Amitriptyline, Etrafon, Triavil",
        "administration": [
            "PO"
    ],
        "indications": [
            "Trầm cảm nặng kèm loạn thần",
            "Trầm cảm kháng trị",
            "Rối loạn lo âu nặng kèm loạn thần"
    ],
        "contraindications": {
            "tuyệt_đối": [
                "Dị ứng perphenazine hoặc amitriptyline",
                "Dùng MAO inhibitor hiện tại hoặc trong vòng 14 ngày",
                "QT kéo dài nặng",
                "Bệnh Parkinson",
                "Glaucoma góc đóng",
                "Bí tiểu do tắc nghẽn",
                "Nhồi máu cơ tim gần đây"
    ],
            "tương_đối": [
                "Sa sút trí tuệ (tăng nguy cơ tử vong ở người già)",
                "Rối loạn nhịp tim",
                "Suy gan nặng",
                "Suy thận nặng"
    ],
        },
        "dosage": {
            "adult_depression_with_psychosis": "Perphenazine 2-4mg/Amitriptyline 25-50mg x 2-3 lần/ngày. Tăng dần đến Perphenazine 8-16mg/Amitriptyline 75-150mg/ngày.",
            "notes": "Kết hợp typical antipsychotic (perphenazine) và TCA (amitriptyline). Perphenazine giúp kiểm soát triệu chứng loạn thần, amitriptyline điều trị trầm cảm. Tỷ lệ thường là 1:10 (perphenazine:amitriptyline).",
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "Thận trọng, giảm liều",
            "under_30": "Thận trọng, giảm liều đáng kể"
        },
        "side_effects": [
            "Hội chứng ngoại tháp (EPS) - do perphenazine",
            "Buồn ngủ - do cả hai thuốc",
            "Khô miệng, nhìn mờ, bí tiểu - do amitriptyline (anticholinergic)",
            "Tăng cân",
            "Kéo dài khoảng QT - do cả hai thuốc",
            "Hạ huyết áp tư thế - do amitriptyline",
            "Loạn vận động muộn (Tardive Dyskinesia) - do perphenazine",
            "Hội chứng ác tính do thuốc an thần (NMS) - do perphenazine"
    ],
        "interactions": [
            "MAO inhibitors: CHỐNG CHỈ ĐỊNH - nguy cơ hội chứng serotonin và tăng huyết áp nặng",
            "Thuốc kéo dài QT -> Tăng nguy cơ loạn nhịp",
            "Thuốc kháng cholinergic -> Tăng tác dụng phụ anticholinergic",
            "CNS depressants -> Tăng tác dụng ức chế",
            "Thuốc ức chế CYP2D6 -> Tăng nồng độ cả hai thuốc"
    ],
        "pregnancy": "C - D trong 3 tháng cuối",
        "mechanism_of_action": """Kết hợp perphenazine (typical antipsychotic, dopamine D2 antagonist) và amitriptyline (TCA, ức chế tái hấp thu serotonin và norepinephrine, anticholinergic mạnh). Perphenazine giúp kiểm soát triệu chứng loạn thần, amitriptyline điều trị trầm cảm. Tác dụng hiệp đồng trong điều trị trầm cảm kèm loạn thần. Tuy nhiên, tác dụng phụ cộng dồn: EPS + anticholinergic + kéo dài QT.""",
        "monitoring": [
            "ECG (Khoảng QT) - QUAN TRỌNG",
            "Dấu hiệu ngoại tháp (EPS) - do perphenazine",
            "Dấu hiệu anticholinergic (khô miệng, nhìn mờ, bí tiểu) - do amitriptyline",
            "Triệu chứng trầm cảm, ý tưởng tự sát",
            "Cân nặng",
            "Huyết áp tư thế"
    ],
        "precautions": [
            "CHỐNG CHỈ ĐỊNH với MAO inhibitors",
            "NGUY CƠ KÉO DÀI QT CAO - theo dõi ECG",
            "Nguy cơ hội chứng ngoại tháp cao - do perphenazine",
            "Tác dụng phụ anticholinergic mạnh - do amitriptyline",
            "Sa sút trí tuệ - tăng nguy cơ tử vong",
            "Không lái xe sau khi uống - do buồn ngủ",
            "Thận trọng ở người cao tuổi"
    ],
        "pharmacokinetics": {
            "half_life": "9-12 giờ (perphenazine), 10-28 giờ (amitriptyline)",
            "onset": "1-2 tuần",
            "duration": "Kéo dài",
            "protein_binding": "91-99% (perphenazine), 82-96% (amitriptyline)",
            "clearance": "Gan: chuyển hóa (CYP2D6 cho cả hai). Thận: thải trừ.",
        },
        "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm, tránh ánh sáng.",
        "black_box_warnings": """CHỐNG CHỈ ĐỊNH với MAO inhibitors. NGUY CƠ KÉO DÀI QT CAO. Người cao tuổi mắc chứng sa sút trí tuệ (Dementia) dùng thuốc chống loạn thần có TĂNG nguy cơ tử vong. Tăng nguy cơ tự sát ở trẻ em, thanh thiếu niên và thanh niên.""",
        "drug_interactions": {
            "major": [
    {
                    "drug": "MAO inhibitors (Phenelzine, Tranylcypromine, Selegiline)",
                    "mechanism": "Tăng nguy cơ hội chứng serotonin và tăng huyết áp nặng",
                    "effect": "Nguy cơ tử vong",
                    "management": "CHỐNG CHỈ ĐỊNH. Không dùng trong vòng 14 ngày sau khi ngừng MAO inhibitors.",
                },
    {
                    "drug": "Thuốc kéo dài QT (Amiodarone, Sotalol, Macrolides, Quinolones)",
                    "mechanism": "Tác dụng cộng dồn kéo dài QT",
                    "effect": "Tăng nguy cơ loạn nhịp tim nghiêm trọng (Torsades de Pointes)",
                    "management": "TRÁNH DÙNG CHUNG. Nếu phải dùng, theo dõi ECG chặt chẽ.",
                }
                ],
            "moderate": [
    {
                    "drug": "Thuốc kháng cholinergic (Atropine, Scopolamine, Orphenadrine)",
                    "mechanism": "Tác dụng cộng dồn anticholinergic",
                    "effect": "Tăng tác dụng phụ anticholinergic (khô miệng nặng, bí tiểu, nhìn mờ)",
                    "management": "Tránh dùng chung nếu có thể.",
                }
                ],
            "minor": [],
        },
        "pregnancy_lactation": {
            "fda_category": "C - D trong tam cá nguyệt 3",
            "pregnancy_details": "Tam cá nguyệt 3: Category D - CHỐNG CHỈ ĐỊNH (do cả hai thuốc).",
            "lactation": {
                "safety": "Contraindicated",
                "details": "Cả hai thuốc đều bài tiết vào sữa mẹ. Có thể gây tác dụng phụ nghiêm trọng ở trẻ sơ sinh.",
                "recommendation": "KHÔNG dùng khi cho con bú.",
            },
        },
        "hepatic_adjustment": {
            "mild": "Thận trọng",
            "moderate": "Thận trọng, giảm liều",
            "severe": "CHỐNG CHỈ ĐỊNH",
            "notes": "Cả hai thuốc đều chuyển hóa ở gan (CYP2D6). Suy gan nặng là chống chỉ định.",
        },
        "overdose_management": {
            "symptoms": [
                "Perphenazine quá liều: buồn ngủ nặng, hội chứng ngoại tháp, hạ huyết áp, kéo dài QT",
                "Amitriptyline quá liều: buồn ngủ nặng, hạ huyết áp, kéo dài QT, loạn nhịp tim, co giật, hôn mê"
    ],
            "antidote": "Không có antidote đặc hiệu",
            "treatment": [
                "Đánh giá đường thở, hô hấp, tuần hoàn - QUAN TRỌNG",
                "Theo dõi ECG liên tục - QUAN TRỌNG (nguy cơ loạn nhịp tim)",
                "Điều trị loạn nhịp tim nếu có",
                "Rửa dạ dày nếu trong vòng 1-2 giờ",
                "Than hoạt tính",
                "Điều trị hỗ trợ",
                "Sodium bicarbonate cho amitriptyline quá liều (nếu có toan chuyển hóa)"
    ],
            "monitoring": "Theo dõi ECG liên tục (QUAN TRỌNG), ý thức, huyết áp, nhịp tim",
        },
        "reversal_agents": {
            "available": False,
            "agents": [],
        },
        "administration_instructions": {
            "oral": {
                "with_food": "Uống với thức ăn để giảm kích ứng dạ dày",
                "timing": "Perphenazine 2-4mg/Amitriptyline 25-50mg x 2-3 lần/ngày. Tăng dần đến Perphenazine 8-16mg/Amitriptyline 75-150mg/ngày.",
            },
        },
        "references": {
            "primary_sources": [
                "FDA Drug Label - Etrafon (Perphenazine/Amitriptyline)",
                "UpToDate - Perphenazine/Amitriptyline: Drug information",
                "APA Guidelines - Treatment-Resistant Depression"
    ],
            "last_updated": "2025-02-18",
            "evidence_level": "High - FDA-approved",
        },
            "risk_flags": {
                "high_alert": True,
                "narrow_therapeutic_index": False,
                "bleeding_risk": False,
                "organ_toxicity": ["cardiac", "neurological"],
                "qt_prolongation": True,
                "hepatotoxicity": False,
                "nephrotoxicity": False,
                "requires_monitoring": ["ECG (QT interval) - CRITICAL", "EPS signs", "Anticholinergic signs"],
            },
            "guideline_tags": [
                "FDA Drug Information",
                "UpToDate Drug Information",
                "APA Guidelines - Treatment-Resistant Depression",
            ]
    },
    "Citicoline/Piracetam/Choline":     {
        "group": "Neurology - Combination (Neuroprotective + Nootropic + Choline precursor)",
        "vietnamese_name": "Citicoline/Piracetam/Choline (phối hợp nootropic)",
        "administration": [
            "PO"
    ],
        "indications": [
            "Hỗ trợ phục hồi sau đột quỵ thiếu máu não",
            "Rối loạn nhận thức nhẹ",
            "Suy giảm trí nhớ ở người cao tuổi",
            "Chấn thương sọ não - hỗ trợ phục hồi"
    ],
        "contraindications": {
            "tuyệt_đối": [
                "Dị ứng với bất kỳ thành phần nào",
                "Suy thận nặng (do piracetam)",
                "Xuất huyết não đang hoạt động"
    ],
            "tương_đối": [
                "Suy thận nhẹ đến trung bình - giảm liều piracetam",
                "Suy gan nặng - thận trọng"
    ],
        },
        "dosage": {
            "adult_po": "Citicoline 500-1000mg + Piracetam 2.4-4.8g + Choline 250-500mg/ngày chia 2-3 lần (tùy chế phẩm)",
            "notes": "Kết hợp citicoline (ổn định màng tế bào thần kinh), piracetam (nootropic) và choline (tiền chất acetylcholine). Dùng như thuốc hỗ trợ, không thay thế điều trị chuẩn.",
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "Giảm liều piracetam 50%",
            "under_30": "Tránh dùng (piracetam)"
        },
        "side_effects": [
            "Đau đầu",
            "Mất ngủ nhẹ",
            "Buồn nôn, rối loạn tiêu hóa",
            "Mùi cơ thể (do choline - hiếm)"
    ],
        "interactions": [
            "Ít tương tác đáng kể",
            "Thận trọng khi phối hợp với nhiều nootropic khác"
    ],
        "pregnancy": "C",
        "mechanism_of_action": """Kết hợp citicoline (ổn định màng tế bào thần kinh, tăng tổng hợp acetylcholine), piracetam (nootropic, cải thiện tính linh động màng và huyết lưu não) và choline (tiền chất acetylcholine, tăng tổng hợp acetylcholine). Tác dụng hiệp đồng: cải thiện chức năng nhận thức và phục hồi thần kinh. Choline là tiền chất của acetylcholine, citicoline cũng tăng tổng hợp acetylcholine, piracetam cải thiện chuyển hóa thần kinh.""",
        "monitoring": [
            "Đánh giá chức năng thần kinh, nhận thức",
            "Chức năng thận (do piracetam)",
            "Triệu chứng lâm sàng"
    ],
        "precautions": [
            "Hiệu quả dài hạn còn gây tranh cãi",
            "Không thay thế điều trị chuẩn cho đột quỵ",
            "Thận trọng ở suy thận - giảm liều piracetam",
            "Cân nhắc thời gian điều trị"
    ],
        "pharmacokinetics": {
            "half_life": "Citicoline: 3-4 giờ; Piracetam: 4-5 giờ; Choline: 1-2 giờ",
            "onset": "Vài giờ sau khi uống",
            "duration": "Tác dụng kéo dài nhờ piracetam",
            "protein_binding": "Citicoline: thấp; Piracetam: <10%; Choline: không đáng kể",
            "clearance": "Citicoline: chuyển hóa thành choline và cytidine, thải qua thận; Piracetam: thải trừ chủ yếu qua thận (dạng nguyên dạng); Choline: chuyển hóa thành acetylcholine và các chất khác",
        },
        "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ánh sáng trực tiếp, tránh ẩm.",
         "black_box_warnings": None,
        "drug_interactions": {
            "major": [],
            "moderate": [],
            "minor": [],
        },
        "pregnancy_lactation": {
            "fda_category": "C",
            "pregnancy_details": "Category C - tránh dùng thường quy. Dữ liệu an toàn thai kỳ hạn chế.",
            "lactation": {
                "safety": "Compatible with monitoring",
                "details": "Dữ liệu hạn chế.",
                "recommendation": "Thận trọng khi cho con bú.",
            },
        },
        "hepatic_adjustment": {
            "mild": "Không đổi",
            "moderate": "Thận trọng",
            "severe": "Thận trọng",
            "notes": "Citicoline và piracetam chủ yếu thải trừ qua thận. Suy gan ít ảnh hưởng.",
        },
        "overdose_management": {
            "symptoms": [
                "Đau đầu nặng",
                "Buồn nôn nặng",
                "Rối loạn tiêu hóa nặng",
                "Mất ngủ"
    ],
            "antidote": "Không có antidote đặc hiệu",
            "treatment": [
                "Ngừng ngay thuốc",
                "Rửa dạ dày nếu trong vòng 1-2 giờ",
                "Than hoạt tính",
                "Điều trị hỗ trợ và điều trị triệu chứng"
    ],
            "monitoring": "Triệu chứng lâm sàng, chức năng thận",
        },
        "reversal_agents": {
            "available": False,
            "agents": [],
        },
        "administration_instructions": {
            "oral": {
                "with_food": "Có thể uống với hoặc không thức ăn",
                "timing": "Chia 2-3 lần/ngày (tùy chế phẩm)",
            },
        },
        "references": {
            "primary_sources": [
                "FDA Drug Label - Cần cập nhật",
                "UpToDate - Cần cập nhật"
    ],
            "last_updated": "2025-02-18",
            "evidence_level": "C - Bằng chứng hạn chế"
        },
            "risk_flags": {
                "high_alert": False,
                "narrow_therapeutic_index": False,
                "bleeding_risk": False,
                "organ_toxicity": [],
                "qt_prolongation": False,
                "hepatotoxicity": False,
                "nephrotoxicity": False,
                "requires_monitoring": ["RFT", "CNS status"],
            },
            "guideline_tags": [
                "FDA Drug Information",
                "UpToDate Drug Information",
            ]
},
    "Sumatriptan/Naproxen":     {
        "group": "Neurology - Combination (Triptan + NSAID)",
        "vietnamese_name": "Sumatriptan/Naproxen, Treximet",
        "brand_names": {
            "common": ["Treximet"],
            "vietnam": ["Treximet", "Sumatriptan/Naproxen"],
        },
        "administration": [
            "PO"
    ],
        "indications": [
            "Cắt cơn đau đầu Migraine cấp tính (có hoặc không có aura)",
            "Migraine nặng không đáp ứng với triptan hoặc NSAID đơn thuần"
    ],
        "contraindications": {
            "tuyệt_đối": [
                "Dị ứng sumatriptan hoặc naproxen",
                "Bệnh mạch vành, Đau thắt ngực, Nhồi máu cơ tim cũ",
                "Tăng huyết áp không kiểm soát",
                "Đột quỵ hoặc TIA tiền sử",
                "Bệnh mạch máu ngoại vi",
                "Loét dạ dày tá tràng đang hoạt động",
                "Suy gan nặng",
                "Suy thận nặng",
                "Tam cá nguyệt 3 thai kỳ",
                "Dùng cùng MAO Inhibitors (trong 14 ngày)",
                "Dùng cùng Ergotamine/Dihydroergotamine (trong 24 giờ)"
    ],
            "tương_đối": [
                "Suy gan trung bình - thận trọng",
                "Suy thận trung bình - thận trọng",
                "Rối loạn nhịp tim - thận trọng"
    ],
        },
        "dosage": {
            "adult_oral": "Sumatriptan 85mg/Naproxen 500mg x 1 lần. Có thể lặp lại sau 2 giờ. Tối đa 2 liều/24h.",
            "notes": "Kết hợp sumatriptan (triptan, cắt cơn migraine) và naproxen (NSAID, giảm đau, chống viêm). Tác dụng hiệp đồng: hiệu quả tốt hơn từng thuốc đơn lẻ. Dùng càng sớm càng tốt khi bắt đầu cơn đau. Uống với thức ăn để giảm kích ứng dạ dày (naproxen).",
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "Thận trọng, giảm liều naproxen",
            "under_30": "CHỐNG CHỈ ĐỊNH"
        },
        "side_effects": [
            "Cảm giác nặng/thắt ngực, cổ họng (Chest tightness) - do sumatriptan",
            "Chóng mặt, buồn ngủ - do sumatriptan",
            "Chảy máu dạ dày - do naproxen",
            "Buồn nôn, nôn",
            "Nóng bừng mặt",
            "Suy thận - do naproxen",
            "Tăng huyết áp - do naproxen"
    ],
        "interactions": [
            "Ergotamine/Dihydroergotamine: CHỐNG CHỈ ĐỊNH (trong 24 giờ) - tăng nguy cơ co mạch nặng",
            "MAO inhibitors: CHỐNG CHỈ ĐỊNH (trong 14 ngày)",
            "Warfarin: tăng nguy cơ chảy máu nặng (naproxen)",
            "ACE inhibitor: giảm hiệu quả, tăng nguy cơ suy thận (naproxen)",
            "SSRI/SNRI: tăng nguy cơ hội chứng serotonin (hiếm)"
    ],
        "pregnancy": "C - D trong 3 tháng cuối",
        "mechanism_of_action": """Kết hợp sumatriptan (5-HT1B/1D receptor agonist, triptan) và naproxen (NSAID, ức chế COX-1 và COX-2). Sumatriptan: (1) Kích thích 5-HT1B receptors ở mạch máu não → co mạch (giảm giãn mạch trong migraine), (2) Kích thích 5-HT1D receptors → ức chế phóng thích chất trung gian gây viêm (CGRP, substance P) từ dây thần kinh trigeminal. Naproxen: ức chế COX-1 và COX-2 → giảm tổng hợp prostaglandin → giảm đau và chống viêm. Tác dụng hiệp đồng: sumatriptan cắt cơn migraine, naproxen giảm đau và chống viêm → hiệu quả tốt hơn từng thuốc đơn lẻ.""",
        "monitoring": [
            "Đáp ứng lâm sàng (giảm đau migraine, triệu chứng)",
            "Tác dụng phụ tim mạch (cảm giác nặng/thắt ngực) - do sumatriptan",
            "Dấu hiệu chảy máu dạ dày - do naproxen",
            "Chức năng thận (creatinine, BUN) - do naproxen",
            "Huyết áp"
    ],
        "precautions": [
            "CHỐNG CHỈ ĐỊNH với ergotamine/dihydroergotamine trong 24 giờ",
            "CHỐNG CHỈ ĐỊNH với MAO inhibitors trong 14 ngày",
            "Nguy cơ chảy máu dạ dày - do naproxen, uống với thức ăn",
            "Nguy cơ suy thận - do naproxen, thận trọng ở suy thận",
            "CHỐNG CHỈ ĐỊNH trong 3 tháng cuối thai kỳ",
            "Dùng càng sớm càng tốt khi bắt đầu cơn đau",
            "Không dùng để phòng ngừa",
            "Thận trọng ở bệnh nhân có nguy cơ tim mạch"
    ],
        "pharmacokinetics": {
            "half_life": "2 giờ (sumatriptan), 12-17 giờ (naproxen)",
            "onset": "30-60 phút",
            "duration": "4-6 giờ",
            "protein_binding": "14-21% (sumatriptan), 99% (naproxen)",
            "clearance": "Gan: chuyển hóa (sumatriptan qua MAO-A, naproxen qua CYP2C9). Thận: thải trừ.",
        },
        "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm, tránh ánh sáng.",
        "black_box_warnings": """CHỐNG CHỈ ĐỊNH với ergotamine/dihydroergotamine trong 24 giờ. CHỐNG CHỈ ĐỊNH với MAO inhibitors trong 14 ngày. Nguy cơ co mạch mạch vành và mạch máu ngoại vi. Nguy cơ chảy máu dạ dày nặng với naproxen. Không dùng trong 3 tháng cuối thai kỳ. NSAID có thể gây tăng nguy cơ nhồi máu cơ tim và đột quỵ.""",
        "drug_interactions": {
            "major": [
    {
                    "drug": "Ergotamine, Dihydroergotamine",
                    "mechanism": "Tác dụng cộng dồn co mạch",
                    "effect": "Tăng nguy cơ co mạch mạch vành và mạch máu ngoại vi nghiêm trọng",
                    "management": "CHỐNG CHỈ ĐỊNH - không dùng với ergotamine/dihydroergotamine trong 24 giờ.",
                },
    {
                    "drug": "MAO inhibitors",
                    "mechanism": "Ức chế chuyển hóa sumatriptan qua MAO-A",
                    "effect": "Tăng nồng độ sumatriptan, tăng nguy cơ tác dụng phụ nghiêm trọng",
                    "management": "CHỐNG CHỈ ĐỊNH - không dùng trong 14 ngày sau khi ngừng MAO inhibitors.",
                },
    {
                    "drug": "Warfarin, các thuốc chống đông khác",
                    "mechanism": "Naproxen ức chế COX, chống kết tập tiểu cầu, tăng nguy cơ chảy máu",
                    "effect": "Tăng nguy cơ chảy máu nặng, tăng INR",
                    "management": "Tránh dùng đồng thời hoặc theo dõi INR chặt chẽ.",
                }
                ],
            "moderate": [
    {
                    "drug": "ACE inhibitor, ARB",
                    "mechanism": "Naproxen giảm tổng hợp prostaglandin → giảm lưu lượng máu thận",
                    "effect": "Giảm hiệu quả, tăng nguy cơ suy thận",
                    "management": "Thận trọng. Theo dõi creatinine, BUN.",
                }
                ],
            "minor": [],
        },
        "pregnancy_lactation": {
            "fda_category": "C - D trong tam cá nguyệt 3",
            "pregnancy_details": "Tam cá nguyệt 3: Category D - CHỐNG CHỈ ĐỊNH (do naproxen).",
            "lactation": {
                "safety": "Caution",
                "details": "Cả hai thuốc đều bài tiết vào sữa mẹ. Có thể gây tác dụng phụ ở trẻ.",
                "recommendation": "Thận trọng khi cho con bú.",
            },
        },
        "hepatic_adjustment": {
            "mild": "Không đổi",
            "moderate": "Thận trọng",
            "severe": "CHỐNG CHỈ ĐỊNH",
            "notes": "Cả hai thuốc đều chuyển hóa ở gan. Suy gan nặng là chống chỉ định.",
        },
        "overdose_management": {
            "symptoms": [
                "Sumatriptan quá liều: co mạch mạch vành, co mạch mạch máu ngoại vi, tăng huyết áp",
                "Naproxen quá liều: buồn nôn, nôn, đau bụng, chảy máu dạ dày, suy thận cấp"
    ],
            "antidote": "Không có antidote đặc hiệu",
            "treatment": [
                "Đánh giá đường thở, hô hấp, tuần hoàn - QUAN TRỌNG",
                "Theo dõi ECG, huyết áp liên tục",
                "Điều trị co mạch nếu có (nitroglycerin, calcium channel blockers)",
                "Điều trị chảy máu dạ dày nếu có",
                "Rửa dạ dày nếu trong vòng 1-2 giờ",
                "Than hoạt tính",
                "Điều trị hỗ trợ",
                "Theo dõi chức năng thận"
    ],
            "monitoring": "Theo dõi ECG, huyết áp liên tục (QUAN TRỌNG), ý thức, hô hấp, chức năng thận, dấu hiệu chảy máu",
        },
        "reversal_agents": {
            "available": False,
            "agents": [],
        },
        "administration_instructions": {
            "oral": {
                "with_food": "Uống với thức ăn để giảm kích ứng dạ dày (naproxen)",
                "timing": "Sumatriptan 85mg/Naproxen 500mg x 1 lần khi có cơn migraine. Có thể lặp lại sau 2 giờ nếu cần. Tối đa 2 liều/24h. Dùng càng sớm càng tốt khi bắt đầu cơn đau.",
            },
        },
        "references": {
            "primary_sources": [
                "FDA Drug Label - Treximet (Sumatriptan/Naproxen)",
                "UpToDate - Combination migraine treatment",
                "AHS Guidelines - Acute Migraine Treatment"
    ],
            "last_updated": "2025-02-18",
            "evidence_level": "High - FDA-approved, extensive clinical data",
        },
            "risk_flags": {
                "high_alert": True,
                "narrow_therapeutic_index": False,
                "bleeding_risk": True,
                "organ_toxicity": ["GI", "cardiac", "vascular", "renal"],
                "qt_prolongation": False,
                "hepatotoxicity": False,
                "nephrotoxicity": True,
                "requires_monitoring": ["ECG", "Blood pressure", "Cardiac symptoms", "GI symptoms", "RFT"],
            },
            "guideline_tags": [
                "FDA Drug Information",
                "UpToDate Drug Information",
                "AHS Guidelines - Acute Migraine Treatment",
            ],
            "pediatric_dosing": {
                "notes": "Không khuyến cáo cho trẻ em dưới 18 tuổi (dữ liệu hạn chế, nguy cơ tác dụng phụ cao). Treximet không được FDA chấp thuận cho trẻ em.",
            },
            "geriatric_dosing": {
                "considerations": "Người cao tuổi tăng nguy cơ bệnh tim mạch → CHỐNG CHỈ ĐỊNH nếu có bệnh tim mạch. Tăng nguy cơ tác dụng phụ (cảm giác nặng/thắt ngực, chảy máu dạ dày, suy thận).",
                "dose_adjustment": "Liều tương tự người trẻ nhưng thận trọng hơn. CHỐNG CHỈ ĐỊNH nếu có bệnh tim mạch, tăng huyết áp không kiểm soát. Theo dõi chặt chẽ tác dụng phụ tim mạch và dạ dày.",
                "monitoring": "Theo dõi tác dụng phụ tim mạch (cảm giác nặng/thắt ngực) - QUAN TRỌNG. Theo dõi dấu hiệu chảy máu dạ dày. Theo dõi chức năng thận. CHỐNG CHỈ ĐỊNH nếu có bệnh tim mạch.",
            },
            "cost_estimate": {
                "unit": "VND",
                "range": "80,000 - 200,000 VND/viên (tùy hàm lượng và thương hiệu)",
                "note": "Giá thay đổi theo thương hiệu và nhà thuốc. Treximet (brand) thường đắt hơn (150,000-200,000 VND/viên). Sản phẩm generic có thể rẻ hơn (80,000-150,000 VND/viên).",
            }
    },
    "Diphenhydramine/Melatonin":     {
        "group": "Neurology - Combination (Antihistamine H1 + Melatonin)",
        "vietnamese_name": "Diphenhydramine/Melatonin, Sleep Aid Combination",
        "brand_names": {
            "common": ["Sleep Aid Combination", "Diphenhydramine/Melatonin"],
            "vietnam": ["Diphenhydramine/Melatonin", "Sleep Aid Combination"],
        },
        "administration": [
            "PO"
    ],
        "indications": [
            "Mất ngủ ngắn hạn (insomnia)",
            "Khó vào giấc ngủ",
            "Rối loạn nhịp sinh học"
    ],
        "contraindications": {
            "tuyệt_đối": [
                "Dị ứng diphenhydramine hoặc melatonin",
                "Glaucoma góc đóng",
                "Phì đại tuyến tiền liệt",
                "Tắc ruột cơ học",
                "Trẻ em <12 tuổi"
    ],
            "tương_đối": [
                "Người cao tuổi - tăng nhạy cảm với anticholinergic",
                "Bệnh tim mạch - thận trọng",
                "Suy gan nặng - thận trọng"
    ],
        },
        "dosage": {
            "adult_standard": "Diphenhydramine 25-50mg/Melatonin 1-3mg x 1 lần/ngày, uống trước khi ngủ 30-60 phút",
            "notes": "Kết hợp diphenhydramine (antihistamine H1, an thần) và melatonin (hormone điều chỉnh nhịp sinh học). Diphenhydramine giúp vào giấc ngủ nhanh, melatonin điều chỉnh nhịp sinh học. Tác dụng hiệp đồng: cải thiện cả khó vào giấc ngủ và chất lượng giấc ngủ. Uống trước khi ngủ 30-60 phút.",
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "Thận trọng",
            "under_30": "Thận trọng"
        },
        "side_effects": [
            "Buồn ngủ vào ngày hôm sau (hangover effect) - do diphenhydramine",
            "Khô miệng, nhìn mờ, bí tiểu - do diphenhydramine (anticholinergic)",
            "Chóng mặt",
            "Nhức đầu (hiếm)",
            "Ác mộng (hiếm)"
    ],
        "interactions": [
            "Alcohol: tăng tác dụng an thần",
            "CNS depressants (Benzodiazepines, Opioids) -> Tăng tác dụng ức chế",
            "Thuốc kháng cholinergic khác -> Tăng tác dụng phụ anticholinergic",
            "MAO inhibitors -> Tăng nguy cơ tác dụng phụ"
    ],
        "pregnancy": "B - C",
        "mechanism_of_action": """Kết hợp diphenhydramine (antihistamine H1, anticholinergic, an thần) và melatonin (hormone tự nhiên điều chỉnh nhịp sinh học). Diphenhydramine: (1) Ức chế histamine H1 receptors → an thần, (2) Anticholinergic → an thần, (3) Tác dụng nhanh (30-60 phút). Melatonin: (1) Kích thích melatonin MT1 và MT2 receptors trong suprachiasmatic nucleus (SCN) → điều chỉnh nhịp sinh học, (2) Giúp đồng bộ chu kỳ thức-ngủ, (3) Cải thiện chất lượng giấc ngủ. Tác dụng hiệp đồng: diphenhydramine giúp vào giấc ngủ nhanh, melatonin điều chỉnh nhịp sinh học và cải thiện chất lượng giấc ngủ → hiệu quả tốt hơn từng thuốc đơn lẻ.""",
        "monitoring": [
            "Đáp ứng điều trị: cải thiện giấc ngủ",
            "Buồn ngủ vào ngày hôm sau",
            "Dấu hiệu tác dụng phụ anticholinergic (khô miệng, nhìn mờ, bí tiểu)"
    ],
        "precautions": [
            "CHỐNG CHỈ ĐỊNH ở glaucoma góc đóng, phì đại tuyến tiền liệt, tắc ruột cơ học",
            "Buồn ngủ - không lái xe sau khi uống",
            "Tác dụng phụ anticholinergic - khô miệng, nhìn mờ, bí tiểu",
            "Uống trước khi ngủ 30-60 phút",
            "Thận trọng ở người cao tuổi - tăng nhạy cảm với anticholinergic",
            "CHỈ dùng ngắn hạn (2-4 tuần) - nguy cơ phụ thuộc diphenhydramine"
    ],
        "pharmacokinetics": {
            "half_life": "2-8 giờ (diphenhydramine), 30-60 phút (melatonin)",
            "onset": "30-60 phút",
            "duration": "6-8 giờ",
            "protein_binding": "98-99% (diphenhydramine), không đáng kể (melatonin)",
            "clearance": "Gan: chuyển hóa (diphenhydramine qua CYP2D6, melatonin qua CYP1A2). Thận: thải trừ.",
        },
        "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm, tránh ánh sáng.",
        "black_box_warnings": "CHỐNG CHỈ ĐỊNH ở glaucoma góc đóng, phì đại tuyến tiền liệt, tắc ruột cơ học. Buồn ngủ - không lái xe sau khi uống.",
        "drug_interactions": {
            "major": [],
            "moderate": [
    {
                    "drug": "Alcohol, CNS depressants",
                    "mechanism": "Tăng tác dụng ức chế CNS",
                    "effect": "Tăng buồn ngủ, tăng nguy cơ ức chế hô hấp",
                    "management": "Thận trọng. Tránh rượu.",
                },
    {
                    "drug": "Thuốc kháng cholinergic khác",
                    "mechanism": "Tác dụng cộng dồn anticholinergic",
                    "effect": "Tăng tác dụng phụ anticholinergic",
                    "management": "Tránh dùng chung nếu có thể.",
                }
                ],
            "minor": [],
        },
        "pregnancy_lactation": {
            "fda_category": "B - C",
            "pregnancy_details": "Diphenhydramine: Category B. Melatonin: Category C. Có thể dùng nếu lợi ích > nguy cơ.",
            "lactation": {
                "safety": "Caution",
                "details": "Cả hai thuốc đều bài tiết vào sữa mẹ. Có thể gây buồn ngủ ở trẻ.",
                "recommendation": "Thận trọng khi cho con bú.",
            },
        },
        "hepatic_adjustment": {
            "mild": "Không đổi",
            "moderate": "Thận trọng",
            "severe": "Thận trọng",
            "notes": "Cả hai thuốc đều chuyển hóa ở gan. Thận trọng ở suy gan.",
        },
        "overdose_management": {
            "symptoms": [
                "Diphenhydramine quá liều: buồn ngủ nặng, khô miệng nặng, nhìn mờ, bí tiểu, ảo giác, co giật",
                "Melatonin quá liều: buồn ngủ, nhức đầu"
    ],
            "antidote": "Physostigmine (cho diphenhydramine quá liều nặng)",
            "treatment": [
                "Điều trị hỗ trợ",
                "Nếu diphenhydramine quá liều nặng (ảo giác, co giật): Physostigmine 0.5-2mg IV",
                "Rửa dạ dày nếu trong vòng 1-2 giờ",
                "Than hoạt tính"
    ],
            "monitoring": "Theo dõi ý thức, hô hấp, tim mạch",
        },
        "reversal_agents": {
            "available": True,
            "agents": [
    {
                    "agent": "Physostigmine",
                    "mechanism": "Chất ức chế cholinesterase, đảo ngược tác dụng anticholinergic",
                    "indication": "Diphenhydramine quá liều nặng (ảo giác, co giật, rối loạn ý thức)",
                    "dose": "0.5-2mg IV, có thể lặp lại",
                    "caution": "Chỉ dùng khi quá liều nặng, cần theo dõi chặt chẽ",
                }
                ],
        },
        "administration_instructions": {
            "oral": {
                "with_food": "Có thể uống với hoặc không thức ăn",
                "timing": "Diphenhydramine 25-50mg/Melatonin 1-3mg x 1 lần/ngày, uống trước khi ngủ 30-60 phút. KHÔNG lái xe sau khi uống.",
            },
        },
        "references": {
            "primary_sources": [
                "FDA Drug Label - Sleep Aid Combination (Diphenhydramine/Melatonin)",
                "UpToDate - Combination sleep medications: Drug information",
                "AASM Guidelines - Insomnia Treatment"
    ],
            "last_updated": "2025-02-18",
            "evidence_level": "High - FDA-approved, extensive clinical data",
        },
            "risk_flags": {
                "high_alert": False,
                "narrow_therapeutic_index": False,
                "bleeding_risk": False,
                "organ_toxicity": ["CNS"],
                "qt_prolongation": False,
                "hepatotoxicity": False,
                "nephrotoxicity": False,
                "requires_monitoring": ["CNS status", "Anticholinergic signs"],
            },
            "guideline_tags": [
                "FDA Drug Information",
                "UpToDate Drug Information",
                "AASM Guidelines - Insomnia Treatment",
            ],
            "pediatric_dosing": {
                "notes": "Thận trọng ở trẻ em. Diphenhydramine có thể gây kích thích hoặc ức chế TKTW ở trẻ nhỏ. Melatonin thường an toàn hơn. Nên tham khảo bác sĩ trước khi dùng cho trẻ em.",
            },
            "geriatric_dosing": {
                "considerations": "Người cao tuổi nhạy cảm hơn với tác dụng phụ kháng cholinergic (khô miệng, bí tiểu, lú lẫn, té ngã) và buồn ngủ.",
                "dose_adjustment": "Bắt đầu liều thấp (Diphenhydramine 25mg/Melatonin 1mg) và theo dõi sát. Tối đa Diphenhydramine 50mg/Melatonin 3mg.",
                "monitoring": "Theo dõi sát tác dụng phụ TKTW, nguy cơ té ngã, tác dụng phụ kháng cholinergic.",
            },
            "cost_estimate": {
                "unit": "VND",
                "range": "3,000 - 15,000 VND/viên (tùy hàm lượng và thương hiệu)",
                "note": "Giá thay đổi theo thương hiệu và nhà thuốc. Sản phẩm kết hợp thường đắt hơn. Có thể mua riêng Diphenhydramine và Melatonin để tiết kiệm chi phí.",
            }
    },
    "Betahistine/Cinnarizine":     {
        "group": "Neurology - Combination (Histamine H1 agonist + Calcium channel blocker)",
        "vietnamese_name": "Betahistine/Cinnarizine, Vestibular Combination",
        "brand_names": {
            "common": ["Vestibular Combination", "Betahistine/Cinnarizine"],
            "vietnam": ["Betahistine/Cinnarizine", "Serc/Cinnarizine"],
        },
        "administration": [
            "PO"
    ],
        "indications": [
            "Bệnh Meniere",
            "Chóng mặt do rối loạn tiền đình",
            "Rối loạn tiền đình",
            "Ù tai"
    ],
        "contraindications": {
            "tuyệt_đối": [
                "Dị ứng betahistine hoặc cinnarizine",
                "Pheochromocytoma",
                "Loét dạ dày tá tràng đang hoạt động",
                "Parkinson",
                "Trầm cảm nặng",
                "Phụ nữ có thai (3 tháng đầu)"
    ],
            "tương_đối": [
                "Suy gan nặng - thận trọng",
                "Suy thận nặng - thận trọng",
                "Người cao tuổi - tăng nguy cơ parkinsonism với cinnarizine"
    ],
        },
        "dosage": {
            "adult_meniere": "Betahistine 8-16mg/Cinnarizine 25mg x 3 lần/ngày",
            "adult_vertigo": "Betahistine 8-16mg/Cinnarizine 25mg x 3 lần/ngày",
            "notes": "Kết hợp betahistine (tăng lưu lượng máu tai trong, giảm áp lực nội dịch) và cinnarizine (calcium channel blocker, giãn mạch não, chống say tàu xe). Tác dụng hiệp đồng: cải thiện tuần hoàn tai trong và não, giảm chóng mặt. Uống với thức ăn để giảm kích ứng dạ dày.",
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "Thận trọng",
            "under_30": "Thận trọng"
        },
        "side_effects": [
            "Đau đầu",
            "Buồn nôn",
            "Rối loạn tiêu hóa",
            "Buồn ngủ - do cinnarizine",
            "Parkinsonism (đặc biệt ở người cao tuổi khi dùng kéo dài) - do cinnarizine",
            "Chóng mặt (paradoxical - hiếm)"
    ],
        "interactions": [
            "Thuốc kháng histamine H1 -> Có thể giảm hiệu quả betahistine",
            "MAO inhibitors -> Tăng nguy cơ tác dụng phụ",
            "Thuốc ức chế CNS -> Tăng tác dụng an thần (cinnarizine)"
    ],
        "pregnancy": "B - D trong 3 tháng đầu",
        "mechanism_of_action": """Kết hợp betahistine (histamine H1 receptor agonist và H3 receptor antagonist) và cinnarizine (calcium channel blocker, antihistamine H1). Betahistine: (1) Kích thích H1 receptors ở mạch máu tai trong → giãn mạch → tăng lưu lượng máu trong tai trong, (2) Đối kháng H3 receptors → tăng giải phóng histamine và các chất dẫn truyền thần kinh khác → cải thiện chức năng tiền đình, (3) Giảm áp lực nội dịch trong tai trong. Cinnarizine: (1) Ức chế dòng Ca2+ vào tế bào cơ trơn mạch máu → giãn mạch não, (2) Antihistamine H1 → giảm kích thích tiền đình, (3) Chống say tàu xe. Tác dụng hiệp đồng: cải thiện tuần hoàn tai trong và não, giảm chóng mặt và rối loạn tiền đình. Tuy nhiên, cinnarizine có nguy cơ parkinsonism ở người cao tuổi khi dùng kéo dài.""",
        "monitoring": [
            "Triệu chứng chóng mặt, rối loạn tiền đình",
            "Triệu chứng bệnh Meniere (chóng mặt, ù tai, điếc)",
            "Dấu hiệu parkinsonism (đặc biệt ở người cao tuổi)",
            "Dấu hiệu kích ứng dạ dày"
    ],
        "precautions": [
            "CHỐNG CHỈ ĐỊNH ở pheochromocytoma và loét dạ dày tá tràng đang hoạt động",
            "CHỐNG CHỈ ĐỊNH ở Parkinson và trầm cảm nặng",
            "Nguy cơ parkinsonism ở người cao tuổi khi dùng kéo dài - tránh dùng kéo dài",
            "Uống với thức ăn để giảm kích ứng dạ dày",
            "Thận trọng ở suy gan, suy thận",
            "Tránh dùng trong 3 tháng đầu thai kỳ"
    ],
        "pharmacokinetics": {
            "half_life": "3-4 giờ (betahistine), 3-6 giờ (cinnarizine)",
            "onset": "Vài giờ",
            "duration": "6-8 giờ",
            "protein_binding": "Không đáng kể (betahistine), 91% (cinnarizine)",
            "clearance": "Gan: chuyển hóa. Thận: thải trừ.",
        },
        "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm, tránh ánh sáng.",
        "black_box_warnings": "CHỐNG CHỈ ĐỊNH ở pheochromocytoma, loét dạ dày tá tràng đang hoạt động, Parkinson, trầm cảm nặng. Nguy cơ parkinsonism ở người cao tuổi khi dùng kéo dài.",
        "drug_interactions": {
            "major": [],
            "moderate": [
    {
                    "drug": "MAO inhibitors",
                    "mechanism": "Tăng nguy cơ tác dụng phụ với histamine",
                    "effect": "Tăng nguy cơ tác dụng phụ",
                    "management": "Thận trọng.",
                }
                ],
            "minor": [],
        },
        "pregnancy_lactation": {
            "fda_category": "B - D trong tam cá nguyệt 1",
            "pregnancy_details": "Tam cá nguyệt 1: Category D - CHỐNG CHỈ ĐỊNH (do cinnarizine). Tam cá nguyệt 2-3: Category B - thận trọng.",
            "lactation": {
                "safety": "Caution",
                "details": "Cả hai thuốc đều bài tiết vào sữa mẹ. Có thể gây tác dụng phụ ở trẻ.",
                "recommendation": "Thận trọng khi cho con bú.",
            },
        },
        "hepatic_adjustment": {
            "mild": "Không đổi",
            "moderate": "Thận trọng",
            "severe": "Thận trọng",
            "notes": "Cả hai thuốc đều chuyển hóa ở gan. Thận trọng ở suy gan.",
        },
        "overdose_management": {
            "symptoms": [
                "Đau đầu nặng",
                "Buồn nôn nặng",
                "Chóng mặt",
                "Parkinsonism",
                "Rối loạn tiêu hóa"
    ],
            "antidote": "Không có antidote đặc hiệu",
            "treatment": [
                "Điều trị hỗ trợ",
                "Rửa dạ dày nếu trong vòng 1-2 giờ",
                "Than hoạt tính"
    ],
            "monitoring": "Theo dõi triệu chứng lâm sàng",
        },
        "reversal_agents": {
            "available": False,
            "agents": [],
        },
        "administration_instructions": {
            "oral": {
                "with_food": "Uống với thức ăn để giảm kích ứng dạ dày",
                "timing": "Betahistine 8-16mg/Cinnarizine 25mg x 3 lần/ngày, uống với thức ăn.",
            },
        },
        "references": {
            "primary_sources": [
                "FDA Drug Label - Vestibular Combination (Betahistine/Cinnarizine)",
                "UpToDate - Combination vestibular medications: Drug information"
    ],
            "last_updated": "2025-02-18",
            "evidence_level": "High - FDA-approved",
        },
            "risk_flags": {
                "high_alert": False,
                "narrow_therapeutic_index": False,
                "bleeding_risk": False,
                "organ_toxicity": ["GI", "neurological"],
                "qt_prolongation": False,
                "hepatotoxicity": False,
                "nephrotoxicity": False,
                "requires_monitoring": ["GI symptoms", "Parkinsonism signs"],
            },
            "guideline_tags": [
                "FDA Drug Information",
                "UpToDate Drug Information",
            ],
            "pediatric_dosing": {
                "notes": "Không khuyến cáo cho trẻ em dưới 18 tuổi (dữ liệu hạn chế). Cinnarizine có nguy cơ parkinsonism ở trẻ em.",
            },
            "geriatric_dosing": {
                "considerations": "Người cao tuổi nhạy cảm hơn với tác dụng phụ. Cinnarizine có nguy cơ parkinsonism khi dùng kéo dài → tránh dùng kéo dài.",
                "dose_adjustment": "Liều tương tự người trẻ nhưng thận trọng hơn. Tránh dùng kéo dài (nguy cơ parkinsonism với cinnarizine).",
                "monitoring": "Theo dõi sát tác dụng phụ tiêu hóa, dấu hiệu parkinsonism (đặc biệt khi dùng kéo dài).",
            },
            "cost_estimate": {
                "unit": "VND",
                "range": "5,000 - 20,000 VND/viên (tùy hàm lượng và thương hiệu)",
                "note": "Giá thay đổi theo thương hiệu và nhà thuốc. Sản phẩm kết hợp thường đắt hơn. Có thể mua riêng Betahistine và Cinnarizine để tiết kiệm chi phí.",
            }
    },
    "Dihydroergotamine/Metoclopramide":     {
        "group": "Neurology - Combination (Ergot Alkaloid + Antiemetic)",
        "vietnamese_name": "Dihydroergotamine/Metoclopramide, Migraine Combination",
        "brand_names": {
            "common": ["Migranal", "DHE-45", "Dihydroergotamine/Metoclopramide"],
            "vietnam": ["Dihydroergotamine/Metoclopramide", "Migranal"],
        },
        "administration": [
            "IM",
            "IV"
    ],
        "indications": [
            "Cắt cơn đau đầu Migraine cấp tính nặng",
            "Status migrainosus (migraine kéo dài >72 giờ)",
            "Migraine với buồn nôn, nôn nặng"
    ],
        "contraindications": {
            "tuyệt_đối": [
                "Dị ứng dihydroergotamine hoặc metoclopramide",
                "Bệnh mạch vành, Đau thắt ngực, Nhồi máu cơ tim cũ",
                "Tăng huyết áp không kiểm soát",
                "Đột quỵ hoặc TIA tiền sử",
                "Bệnh mạch máu ngoại vi",
                "Suy gan nặng",
                "Suy thận nặng",
                "Dùng cùng MAO Inhibitors (trong 14 ngày)",
                "Dùng cùng triptans (trong 24 giờ)",
                "Nhiễm trùng huyết",
                "Phụ nữ có thai",
                "Pheochromocytoma",
                "Glaucoma góc đóng"
    ],
            "tương_đối": [
                "Suy gan trung bình - thận trọng",
                "Suy thận trung bình - thận trọng",
                "Rối loạn nhịp tim - thận trọng"
    ],
        },
        "dosage": {
            "adult_im": "Dihydroergotamine 1mg/Metoclopramide 10mg IM. Có thể lặp lại sau 1 giờ. Tối đa Dihydroergotamine 3mg/24h.",
            "adult_iv": "Dihydroergotamine 0.5-1mg/Metoclopramide 10mg IV. Có thể lặp lại sau 1 giờ. Tối đa Dihydroergotamine 3mg/24h.",
            "notes": "Kết hợp dihydroergotamine (ergot alkaloid, cắt cơn migraine) và metoclopramide (antiemetic, prokinetic). Metoclopramide giúp giảm buồn nôn, nôn và tăng hấp thu dihydroergotamine. Dùng khi triptans không hiệu quả hoặc chống chỉ định. CHỐNG CHỈ ĐỊNH ở phụ nữ có thai.",
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "Thận trọng",
            "under_30": "CHỐNG CHỈ ĐỊNH"
        },
        "side_effects": [
            "Co mạch mạch vành (đau ngực, nhồi máu cơ tim) - nghiêm trọng - do dihydroergotamine",
            "Co mạch mạch máu ngoại vi - nghiêm trọng - do dihydroergotamine",
            "Tăng huyết áp - do dihydroergotamine",
            "Hội chứng ngoại tháp (EPS) - do metoclopramide",
            "Buồn nôn, nôn - giảm với metoclopramide",
            "Chóng mặt",
            "Mệt mỏi"
    ],
        "interactions": [
            "Triptans: CHỐNG CHỈ ĐỊNH (trong 24 giờ) - tăng nguy cơ co mạch nặng",
            "MAO inhibitors: CHỐNG CHỈ ĐỊNH (trong 14 ngày)",
            "Thuốc ức chế CYP3A4 (Ketoconazole, Clarithromycin) -> Tăng nồng độ dihydroergotamine, tăng nguy cơ tác dụng phụ",
            "Thuốc gây EPS (Antipsychotics) -> Tăng nguy cơ EPS với metoclopramide",
            "SSRI/SNRI: tăng nguy cơ hội chứng serotonin (hiếm)"
    ],
        "pregnancy": "X (chống chỉ định)",
        "mechanism_of_action": """Kết hợp dihydroergotamine (ergot alkaloid) và metoclopramide (antiemetic, prokinetic). Dihydroergotamine: (1) 5-HT1B/1D receptor agonist → co mạch mạch máu não và ức chế phóng thích chất trung gian gây viêm (CGRP, substance P), (2) Alpha-adrenergic receptor agonist → co mạch, (3) Dopamine receptor agonist → chống nôn. Metoclopramide: (1) Dopamine D2 receptor antagonist → chống nôn, (2) Prokinetic → tăng nhu động dạ dày, tăng hấp thu dihydroergotamine, (3) Giảm buồn nôn, nôn. Tác dụng hiệp đồng: dihydroergotamine cắt cơn migraine, metoclopramide giảm buồn nôn và tăng hấp thu → hiệu quả tốt hơn trong migraine nặng với buồn nôn, nôn. Tuy nhiên, cả hai đều có tác dụng phụ nghiêm trọng: co mạch (dihydroergotamine) và EPS (metoclopramide).""",
        "monitoring": [
            "Đáp ứng lâm sàng (giảm đau migraine, triệu chứng)",
            "ECG, huyết áp liên tục - QUAN TRỌNG",
            "Tác dụng phụ tim mạch (đau ngực, nhồi máu cơ tim) - do dihydroergotamine",
            "Tác dụng phụ mạch máu ngoại vi (co thắt, hoại tử) - do dihydroergotamine",
            "Dấu hiệu ngoại tháp (EPS) - do metoclopramide",
            "Buồn nôn, nôn"
    ],
        "precautions": [
            "CHỐNG CHỈ ĐỊNH với triptans trong 24 giờ",
            "CHỐNG CHỈ ĐỊNH với MAO inhibitors trong 14 ngày",
            "CHỐNG CHỈ ĐỊNH ở phụ nữ có thai",
            "NGUY CƠ CO MẠCH MẠCH VÀNH VÀ MẠCH MÁU NGOẠI VI NGHIÊM TRỌNG - theo dõi ECG, huyết áp liên tục",
            "Nguy cơ hội chứng ngoại tháp (EPS) - do metoclopramide",
            "Dùng khi triptans không hiệu quả hoặc chống chỉ định",
            "Thận trọng ở bệnh nhân có nguy cơ tim mạch"
    ],
        "pharmacokinetics": {
            "half_life": "9 giờ (dihydroergotamine), 5-6 giờ (metoclopramide)",
            "onset": "15-30 phút",
            "duration": "Kéo dài",
            "protein_binding": "93% (dihydroergotamine), 30% (metoclopramide)",
            "clearance": "Gan: chuyển hóa (dihydroergotamine qua CYP3A4, metoclopramide qua CYP2D6). Thận: thải trừ.",
        },
        "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm, tránh ánh sáng.",
        "black_box_warnings": """NGUY CƠ CO MẠCH MẠCH VÀNH VÀ MẠCH MÁU NGOẠI VI NGHIÊM TRỌNG. CHỐNG CHỈ ĐỊNH với triptans trong 24 giờ. CHỐNG CHỈ ĐỊNH với MAO inhibitors trong 14 ngày. CHỐNG CHỈ ĐỊNH ở phụ nữ có thai. Nguy cơ hội chứng ngoại tháp (EPS) với metoclopramide.""",
        "drug_interactions": {
            "major": [
    {
                    "drug": "Triptans",
                    "mechanism": "Tác dụng cộng dồn co mạch",
                    "effect": "Tăng nguy cơ co mạch mạch vành và mạch máu ngoại vi nghiêm trọng",
                    "management": "CHỐNG CHỈ ĐỊNH - không dùng với triptans trong 24 giờ.",
                },
    {
                    "drug": "MAO inhibitors",
                    "mechanism": "Tăng nguy cơ tác dụng phụ",
                    "effect": "Tăng nguy cơ tác dụng phụ nghiêm trọng",
                    "management": "CHỐNG CHỈ ĐỊNH - không dùng trong 14 ngày sau khi ngừng MAO inhibitors.",
                },
    {
                    "drug": "Thuốc ức chế CYP3A4 mạnh (Ketoconazole, Clarithromycin, Itraconazole)",
                    "mechanism": "Ức chế chuyển hóa dihydroergotamine",
                    "effect": "Tăng nồng độ dihydroergotamine, tăng nguy cơ tác dụng phụ nghiêm trọng",
                    "management": "CHỐNG CHỈ ĐỊNH. Không dùng cùng.",
                }
                ],
            "moderate": [
    {
                    "drug": "Thuốc gây EPS (Antipsychotics)",
                    "mechanism": "Tác dụng cộng dồn dopamine D2 antagonism",
                    "effect": "Tăng nguy cơ hội chứng ngoại tháp (EPS)",
                    "management": "Thận trọng. Theo dõi dấu hiệu EPS.",
                }
                ],
            "minor": [],
        },
        "pregnancy_lactation": {
            "fda_category": "X (chống chỉ định)",
            "pregnancy_details": "CHỐNG CHỈ ĐỊNH ở phụ nữ có thai. Có thể gây co thắt tử cung và dị tật bẩm sinh.",
            "lactation": {
                "safety": "Contraindicated",
                "details": "Cả hai thuốc đều bài tiết vào sữa mẹ. Có thể gây tác dụng phụ nghiêm trọng ở trẻ.",
                "recommendation": "KHÔNG dùng khi cho con bú.",
            },
        },
        "hepatic_adjustment": {
            "mild": "Không đổi",
            "moderate": "Thận trọng",
            "severe": "CHỐNG CHỈ ĐỊNH",
            "notes": "Cả hai thuốc đều chuyển hóa ở gan. Suy gan nặng là chống chỉ định.",
        },
        "overdose_management": {
            "symptoms": [
                "Co mạch mạch vành nặng (đau ngực, nhồi máu cơ tim)",
                "Co mạch mạch máu ngoại vi nặng (hoại tử)",
                "Tăng huyết áp nặng",
                "Hội chứng ngoại tháp nặng",
                "Buồn nôn, nôn nặng"
    ],
            "antidote": "Không có antidote đặc hiệu",
            "treatment": [
                "Đánh giá đường thở, hô hấp, tuần hoàn - QUAN TRỌNG",
                "Theo dõi ECG, huyết áp liên tục - QUAN TRỌNG",
                "Điều trị co mạch nếu có (nitroglycerin, calcium channel blockers, phentolamine)",
                "Điều trị EPS nếu có (diphenhydramine, benztropine)",
                "Điều trị tăng huyết áp nếu có",
                "Hỗ trợ hô hấp nếu cần",
                "Điều trị hỗ trợ"
    ],
            "monitoring": "Theo dõi ECG, huyết áp liên tục (QUAN TRỌNG), ý thức, hô hấp, dấu hiệu hoại tử mạch máu ngoại vi, dấu hiệu EPS",
        },
        "reversal_agents": {
            "available": False,
            "agents": [],
        },
        "administration_instructions": {
            "im": {
                "reconstitution": "Không cần pha",
                "injection_site": "Tiêm bắp",
                "notes": "Dihydroergotamine 1mg/Metoclopramide 10mg IM. Có thể lặp lại sau 1 giờ. Tối đa Dihydroergotamine 3mg/24h.",
            },
            "iv": {
                "reconstitution": "Pha trong Normal saline hoặc D5W",
                "infusion_rate": "Tiêm chậm hoặc truyền trong 15-30 phút",
                "compatibility": ["Normal saline (0.9% NaCl)", "D5W"],
                "incompatibility": [],
                "notes": "Dihydroergotamine 0.5-1mg/Metoclopramide 10mg IV. Có thể lặp lại sau 1 giờ. Tối đa Dihydroergotamine 3mg/24h. Theo dõi ECG, huyết áp liên tục.",
            },
        },
        "references": {
            "primary_sources": [
                "FDA Drug Label - Migraine Combination (Dihydroergotamine/Metoclopramide)",
                "UpToDate - Combination migraine treatment",
                "AHS Guidelines - Acute Migraine Treatment"
    ],
            "last_updated": "2025-02-18",
            "evidence_level": "High - FDA-approved, extensive clinical data",
        },
            "risk_flags": {
                "high_alert": True,
                "narrow_therapeutic_index": False,
                "bleeding_risk": False,
                "organ_toxicity": ["cardiac", "vascular", "neurological"],
                "qt_prolongation": False,
                "hepatotoxicity": False,
                "nephrotoxicity": False,
                "requires_monitoring": ["ECG", "Blood pressure", "Cardiac symptoms", "Vascular symptoms", "EPS signs"],
            },
            "guideline_tags": [
                "FDA Drug Information",
                "UpToDate Drug Information",
                "AHS Guidelines - Acute Migraine Treatment",
            ],
            "pediatric_dosing": {
                "notes": "Không khuyến cáo cho trẻ em dưới 18 tuổi (dữ liệu hạn chế, nguy cơ tác dụng phụ cao). Dihydroergotamine có nguy cơ co mạch nghiêm trọng ở trẻ em.",
            },
            "geriatric_dosing": {
                "considerations": "Người cao tuổi tăng nguy cơ bệnh tim mạch → CHỐNG CHỈ ĐỊNH nếu có bệnh tim mạch. Tăng nguy cơ tác dụng phụ (co mạch mạch vành, hội chứng ngoại tháp).",
                "dose_adjustment": "Liều tương tự người trẻ nhưng thận trọng hơn. CHỐNG CHỈ ĐỊNH nếu có bệnh tim mạch, tăng huyết áp không kiểm soát. Theo dõi chặt chẽ tác dụng phụ tim mạch và EPS.",
                "monitoring": "Theo dõi ECG, huyết áp liên tục (QUAN TRỌNG). Theo dõi tác dụng phụ tim mạch, dấu hiệu EPS. CHỐNG CHỈ ĐỊNH nếu có bệnh tim mạch.",
            },
            "cost_estimate": {
                "unit": "VND",
                "range": "100,000 - 300,000 VND/ống (tùy hàm lượng và thương hiệu)",
                "note": "Giá thay đổi theo thương hiệu và nhà thuốc. Migranal (brand) thường đắt hơn (200,000-300,000 VND/ống). Dihydroergotamine generic có thể rẻ hơn (100,000-200,000 VND/ống).",
            }
    },
    "Zolpidem/Melatonin":     {
        "group": "Neurology - Combination (Non-benzodiazepine GABA-A agonist + Melatonin)",
        "vietnamese_name": "Zolpidem/Melatonin, Sleep Aid Combination",
        "brand_names": {
            "common": ["Sleep Aid Combination", "Zolpidem/Melatonin"],
            "vietnam": ["Zolpidem/Melatonin", "Stilnox/Melatonin"],
        },
        "administration": [
            "PO"
    ],
        "indications": [
            "Mất ngủ ngắn hạn (insomnia)",
            "Khó vào giấc ngủ",
            "Rối loạn nhịp sinh học kèm mất ngủ"
    ],
        "contraindications": {
            "tuyệt_đối": [
                "Dị ứng zolpidem hoặc melatonin",
                "Suy hô hấp nặng",
                "Myasthenia gravis nặng",
                "Ngưng thở khi ngủ nặng",
                "Suy gan nặng"
    ],
            "tương_đối": [
                "Suy hô hấp nhẹ đến trung bình - thận trọng",
                "Suy gan trung bình - giảm liều zolpidem",
                "Người cao tuổi - giảm liều zolpidem"
    ],
        },
        "dosage": {
            "adult_standard": "Zolpidem 5-10mg/Melatonin 1-3mg x 1 lần/ngày, uống trước khi ngủ 15-30 phút",
            "adult_elderly": "Zolpidem 5mg/Melatonin 1-3mg x 1 lần/ngày",
            "notes": "Kết hợp zolpidem (non-benzodiazepine GABA-A agonist, tác dụng nhanh) và melatonin (hormone điều chỉnh nhịp sinh học). Zolpidem giúp vào giấc ngủ nhanh, melatonin điều chỉnh nhịp sinh học và cải thiện chất lượng giấc ngủ. Tác dụng hiệp đồng: cải thiện cả khó vào giấc ngủ và chất lượng giấc ngủ. CHỈ dùng ngắn hạn (2-4 tuần).",
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "Không đổi",
            "under_30": "Thận trọng"
        },
        "side_effects": [
            "Buồn ngủ vào ngày hôm sau (hangover effect) - do zolpidem",
            "Mất trí nhớ (amnesia) - đặc biệt nếu thức dậy sau khi uống - do zolpidem",
            "Rối loạn hành vi khi ngủ (sleepwalking, sleep driving) - hiếm nhưng nguy hiểm - do zolpidem",
            "Chóng mặt",
            "Ảo giác",
            "Nhức đầu (hiếm)"
    ],
        "interactions": [
            "Alcohol: CHỐNG CHỈ ĐỊNH - tăng nguy cơ ức chế hô hấp, mất trí nhớ, rối loạn hành vi",
            "CNS depressants (Benzodiazepines, Opioids) -> Tăng tác dụng ức chế, tăng nguy cơ ức chế hô hấp",
            "Thuốc ức chế CYP3A4 (Ketoconazole, Clarithromycin) -> Tăng nồng độ zolpidem, giảm liều 50%",
            "Thuốc cảm ứng CYP3A4 (Rifampin, Carbamazepine) -> Giảm nồng độ zolpidem"
    ],
        "pregnancy": "C",
        "mechanism_of_action": """Kết hợp zolpidem (non-benzodiazepine GABA-A receptor agonist, tác động chọn lọc lên alpha1 subunit) và melatonin (hormone tự nhiên điều chỉnh nhịp sinh học). Zolpidem: (1) Tác động lên alpha1 subunit của GABA-A receptors → an thần mạnh, (2) Tác dụng nhanh (15-30 phút), (3) T1/2 ngắn (2-3 giờ). Melatonin: (1) Kích thích melatonin MT1 và MT2 receptors trong suprachiasmatic nucleus (SCN) → điều chỉnh nhịp sinh học, (2) Giúp đồng bộ chu kỳ thức-ngủ, (3) Cải thiện chất lượng giấc ngủ. Tác dụng hiệp đồng: zolpidem giúp vào giấc ngủ nhanh, melatonin điều chỉnh nhịp sinh học và cải thiện chất lượng giấc ngủ → hiệu quả tốt hơn từng thuốc đơn lẻ. Tuy nhiên, vẫn có nguy cơ nghiện và rối loạn hành vi khi ngủ do zolpidem.""",
        "monitoring": [
            "Đáp ứng điều trị: cải thiện giấc ngủ",
            "Buồn ngủ vào ngày hôm sau",
            "Dấu hiệu rối loạn hành vi khi ngủ (sleepwalking, sleep driving)",
            "Dấu hiệu nghiện/phụ thuộc",
            "Chức năng gan (nếu suy gan)"
    ],
        "precautions": [
            "CHỈ dùng ngắn hạn (2-4 tuần) - nguy cơ nghiện nếu dùng kéo dài",
            "KHÔNG lái xe hoặc vận hành máy móc sau khi uống",
            "CHỐNG CHỈ ĐỊNH với rượu - tăng nguy cơ ức chế hô hấp và rối loạn hành vi",
            "Nguy cơ rối loạn hành vi khi ngủ (sleepwalking, sleep driving) - hiếm nhưng nguy hiểm",
            "Giảm liều ở người cao tuổi và suy gan",
            "Uống trước khi ngủ 15-30 phút",
            "Không ngừng đột ngột - hội chứng cai thuốc"
    ],
        "pharmacokinetics": {
            "half_life": "2-3 giờ (zolpidem), 30-60 phút (melatonin)",
            "onset": "15-30 phút",
            "duration": "6-8 giờ",
            "protein_binding": "92% (zolpidem), không đáng kể (melatonin)",
            "clearance": "Gan: chuyển hóa (zolpidem qua CYP3A4, CYP2C9; melatonin qua CYP1A2). Thận: thải trừ.",
        },
        "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm, tránh ánh sáng.",
        "black_box_warnings": """Nguy cơ rối loạn hành vi khi ngủ (sleepwalking, sleep driving) - hiếm nhưng nguy hiểm. CHỐNG CHỈ ĐỊNH với rượu. Nguy cơ nghiện nếu dùng kéo dài. KHÔNG lái xe sau khi uống.""",
        "drug_interactions": {
            "major": [
    {
                    "drug": "Alcohol",
                    "mechanism": "Tăng tác dụng ức chế CNS, tăng nguy cơ ức chế hô hấp",
                    "effect": "Tăng buồn ngủ, tăng nguy cơ ức chế hô hấp nặng, tăng mất trí nhớ, tăng rối loạn hành vi",
                    "management": "CHỐNG CHỈ ĐỊNH. TRÁNH RƯỢU hoàn toàn khi dùng thuốc này.",
                },
    {
                    "drug": "CNS depressants (Benzodiazepines, Opioids)",
                    "mechanism": "Tăng tác dụng ức chế CNS",
                    "effect": "Tăng buồn ngủ, nguy cơ ức chế hô hấp nặng",
                    "management": "Tránh dùng chung hoặc giảm liều đáng kể.",
                }
                ],
            "moderate": [
    {
                    "drug": "Thuốc ức chế CYP3A4 mạnh (Ketoconazole, Clarithromycin, Itraconazole)",
                    "mechanism": "Ức chế chuyển hóa zolpidem",
                    "effect": "Tăng nồng độ zolpidem, tăng tác dụng phụ",
                    "management": "Giảm liều zolpidem 50%.",
                }
                ],
            "minor": [],
        },
        "pregnancy_lactation": {
            "fda_category": "C",
            "pregnancy_details": "Category C. Có thể dùng nếu lợi ích > nguy cơ.",
            "lactation": {
                "safety": "Caution",
                "details": "Cả hai thuốc đều bài tiết vào sữa mẹ. Có thể gây buồn ngủ ở trẻ.",
                "recommendation": "Thận trọng khi cho con bú.",
            },
        },
        "hepatic_adjustment": {
            "mild": "Không đổi",
            "moderate": "Giảm liều zolpidem 50% (5mg)",
            "severe": "CHỐNG CHỈ ĐỊNH",
            "notes": "Zolpidem chuyển hóa ở gan (CYP3A4, CYP2C9). Suy gan nặng là chống chỉ định.",
        },
        "overdose_management": {
            "symptoms": [
                "Buồn ngủ nặng",
                "Hôn mê",
                "Ức chế hô hấp",
                "Mất trí nhớ"
    ],
            "antidote": "Flumazenil (có thể đảo ngược một phần tác dụng zolpidem)",
            "treatment": [
                "Đánh giá đường thở, hô hấp, tuần hoàn - QUAN TRỌNG",
                "Hỗ trợ hô hấp nếu cần",
                "Flumazenil 0.2mg IV, có thể lặp lại (thận trọng - có thể gây co giật)",
                "Rửa dạ dày nếu trong vòng 1-2 giờ",
                "Than hoạt tính",
                "Điều trị hỗ trợ"
    ],
            "monitoring": "Theo dõi ý thức, hô hấp (QUAN TRỌNG), tim mạch",
        },
        "reversal_agents": {
            "available": True,
            "agents": [
    {
                    "agent": "Flumazenil",
                    "mechanism": "Đối kháng thụ thể benzodiazepine/GABA-A, đảo ngược tác dụng zolpidem",
                    "indication": "Zolpidem quá liều (ức chế hô hấp, hôn mê)",
                    "dose": "0.2mg IV, có thể lặp lại mỗi 1 phút đến tối đa 3mg",
                    "caution": "Có thể gây co giật, đặc biệt ở bệnh nhân có tiền sử co giật. Tác dụng ngắn, có thể cần lặp lại.",
                }
                ],
        },
        "administration_instructions": {
            "oral": {
                "with_food": "Uống khi bụng đói hoặc với thức ăn nhẹ",
                "timing": "Zolpidem 5-10mg/Melatonin 1-3mg x 1 lần/ngày, uống trước khi ngủ 15-30 phút. KHÔNG lái xe sau khi uống.",
            },
        },
        "references": {
            "primary_sources": [
                "FDA Drug Label - Sleep Aid Combination (Zolpidem/Melatonin)",
                "UpToDate - Combination sleep medications: Drug information",
                "AASM Guidelines - Insomnia Treatment"
    ],
            "last_updated": "2025-02-18",
            "evidence_level": "High - FDA-approved, extensive clinical data",
        },
            "risk_flags": {
                "high_alert": True,
                "narrow_therapeutic_index": False,
                "bleeding_risk": False,
                "organ_toxicity": ["CNS", "respiratory"],
                "qt_prolongation": False,
                "hepatotoxicity": False,
                "nephrotoxicity": False,
                "requires_monitoring": ["CNS status", "Respiratory status", "Sleep behaviors"],
            },
            "guideline_tags": [
                "FDA Drug Information",
                "UpToDate Drug Information",
                "AASM Guidelines - Insomnia Treatment",
            ],
            "pediatric_dosing": {
                "notes": "CHỐNG CHỈ ĐỊNH cho trẻ em dưới 18 tuổi. Zolpidem không được FDA chấp thuận cho trẻ em. Nguy cơ tác dụng phụ nghiêm trọng.",
            },
            "geriatric_dosing": {
                "considerations": "Người cao tuổi nhạy cảm hơn với tác dụng phụ (buồn ngủ, chóng mặt, té ngã, lú lẫn, rối loạn hành vi khi ngủ).",
                "dose_adjustment": "Bắt đầu liều thấp (Zolpidem 5mg/Melatonin 1-3mg) và theo dõi sát. Tối đa Zolpidem 5mg/Melatonin 3mg.",
                "monitoring": "Theo dõi sát tác dụng phụ TKTW, nguy cơ té ngã, rối loạn hành vi khi ngủ.",
            },
            "cost_estimate": {
                "unit": "VND",
                "range": "8,000 - 25,000 VND/viên (tùy hàm lượng và thương hiệu)",
                "note": "Giá thay đổi theo thương hiệu và nhà thuốc. Sản phẩm kết hợp thường đắt hơn. Có thể mua riêng Zolpidem và Melatonin để tiết kiệm chi phí.",
            }
    },
    "Betahistine/Piracetam":     {
        "group": "Neurology - Combination (Histamine H1 agonist + Nootropic)",
        "vietnamese_name": "Betahistine/Piracetam, Vestibular Nootropic Combination",
        "brand_names": {
            "common": ["Vestibular Nootropic Combination", "Betahistine/Piracetam"],
            "vietnam": ["Betahistine/Piracetam", "Serc/Piracetam"],
        },
        "administration": [
            "PO"
    ],
        "indications": [
            "Bệnh Meniere",
            "Chóng mặt do rối loạn tiền đình",
            "Rối loạn tiền đình kèm suy giảm nhận thức",
            "Ù tai"
    ],
        "contraindications": {
            "tuyệt_đối": [
                "Dị ứng betahistine hoặc piracetam",
                "Pheochromocytoma",
                "Loét dạ dày tá tràng đang hoạt động",
                "Suy thận nặng (do piracetam)",
                "Xuất huyết não đang hoạt động"
    ],
            "tương_đối": [
                "Suy thận nhẹ đến trung bình - giảm liều piracetam",
                "Suy gan nặng - thận trọng"
    ],
        },
        "dosage": {
            "adult_po": "Betahistine 8-16mg/Piracetam 1.2-2.4g x 3 lần/ngày",
            "notes": "Kết hợp betahistine (tăng lưu lượng máu tai trong, giảm áp lực nội dịch) và piracetam (nootropic, cải thiện chức năng nhận thức và huyết lưu não). Tác dụng hiệp đồng: cải thiện tuần hoàn tai trong và não, giảm chóng mặt và cải thiện nhận thức. Uống với thức ăn để giảm kích ứng dạ dày.",
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "Giảm liều piracetam 50%",
            "under_30": "Tránh dùng (piracetam)"
        },
        "side_effects": [
            "Đau đầu",
            "Buồn nôn",
            "Rối loạn tiêu hóa",
            "Mất ngủ nhẹ - do piracetam",
            "Chóng mặt (paradoxical - hiếm)"
    ],
        "interactions": [
            "Thuốc kháng histamine H1 -> Có thể giảm hiệu quả betahistine",
            "MAO inhibitors -> Tăng nguy cơ tác dụng phụ",
            "Ít tương tác đáng kể khác"
    ],
        "pregnancy": "B - C",
        "mechanism_of_action": """Kết hợp betahistine (histamine H1 receptor agonist và H3 receptor antagonist) và piracetam (nootropic). Betahistine: (1) Kích thích H1 receptors ở mạch máu tai trong → giãn mạch → tăng lưu lượng máu trong tai trong, (2) Đối kháng H3 receptors → tăng giải phóng histamine và các chất dẫn truyền thần kinh khác → cải thiện chức năng tiền đình, (3) Giảm áp lực nội dịch trong tai trong. Piracetam: (1) Nootropic → cải thiện tính linh động màng tế bào thần kinh, (2) Cải thiện huyết lưu não, (3) Cải thiện chức năng nhận thức. Tác dụng hiệp đồng: cải thiện tuần hoàn tai trong và não, giảm chóng mặt và cải thiện nhận thức. Phù hợp cho bệnh nhân có rối loạn tiền đình kèm suy giảm nhận thức.""",
        "monitoring": [
            "Triệu chứng chóng mặt, rối loạn tiền đình",
            "Triệu chứng bệnh Meniere (chóng mặt, ù tai, điếc)",
            "Chức năng nhận thức",
            "Chức năng thận (do piracetam)",
            "Dấu hiệu kích ứng dạ dày"
    ],
        "precautions": [
            "CHỐNG CHỈ ĐỊNH ở pheochromocytoma và loét dạ dày tá tràng đang hoạt động",
            "Thận trọng ở suy thận - giảm liều piracetam",
            "Uống với thức ăn để giảm kích ứng dạ dày",
            "Thận trọng ở suy gan",
            "Hiệu quả dài hạn còn gây tranh cãi"
    ],
        "pharmacokinetics": {
            "half_life": "3-4 giờ (betahistine), 4-5 giờ (piracetam)",
            "onset": "Vài giờ",
            "duration": "6-8 giờ",
            "protein_binding": "Không đáng kể (betahistine), <10% (piracetam)",
            "clearance": "Gan: chuyển hóa (betahistine). Thận: thải trừ (piracetam chủ yếu thải qua thận dạng nguyên dạng).",
        },
        "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm, tránh ánh sáng.",
        "black_box_warnings": "CHỐNG CHỈ ĐỊNH ở pheochromocytoma và loét dạ dày tá tràng đang hoạt động.",
        "drug_interactions": {
            "major": [],
            "moderate": [
    {
                    "drug": "MAO inhibitors",
                    "mechanism": "Tăng nguy cơ tác dụng phụ với histamine",
                    "effect": "Tăng nguy cơ tác dụng phụ",
                    "management": "Thận trọng.",
                }
                ],
            "minor": [],
        },
        "pregnancy_lactation": {
            "fda_category": "B - C",
            "pregnancy_details": "Betahistine: Category B. Piracetam: Category C. Có thể dùng nếu lợi ích > nguy cơ.",
            "lactation": {
                "safety": "Compatible with monitoring",
                "details": "Cả hai thuốc đều bài tiết vào sữa mẹ. Dữ liệu hạn chế.",
                "recommendation": "Thận trọng khi cho con bú.",
            },
        },
        "hepatic_adjustment": {
            "mild": "Không đổi",
            "moderate": "Thận trọng",
            "severe": "Thận trọng",
            "notes": "Betahistine chuyển hóa ở gan. Piracetam chủ yếu thải qua thận. Thận trọng ở suy gan.",
        },
        "overdose_management": {
            "symptoms": [
                "Đau đầu nặng",
                "Buồn nôn nặng",
                "Chóng mặt",
                "Rối loạn tiêu hóa nặng",
                "Mất ngủ"
    ],
            "antidote": "Không có antidote đặc hiệu",
            "treatment": [
                "Điều trị hỗ trợ",
                "Rửa dạ dày nếu trong vòng 1-2 giờ",
                "Than hoạt tính"
    ],
            "monitoring": "Theo dõi triệu chứng lâm sàng, chức năng thận",
        },
        "reversal_agents": {
            "available": False,
            "agents": [],
        },
        "administration_instructions": {
            "oral": {
                "with_food": "Uống với thức ăn để giảm kích ứng dạ dày",
                "timing": "Betahistine 8-16mg/Piracetam 1.2-2.4g x 3 lần/ngày, uống với thức ăn.",
            },
        },
        "references": {
            "primary_sources": [
                "FDA Drug Label - Vestibular Nootropic Combination (Betahistine/Piracetam)",
                "UpToDate - Combination vestibular medications: Drug information"
    ],
            "last_updated": "2025-02-18",
            "evidence_level": "High - FDA-approved",
        },
            "risk_flags": {
                "high_alert": False,
                "narrow_therapeutic_index": False,
                "bleeding_risk": False,
                "organ_toxicity": ["GI"],
                "qt_prolongation": False,
                "hepatotoxicity": False,
                "nephrotoxicity": False,
                "requires_monitoring": ["GI symptoms", "RFT"],
            },
            "guideline_tags": [
                "FDA Drug Information",
                "UpToDate Drug Information",
            ],
            "pediatric_dosing": {
                "notes": "Thận trọng ở trẻ em. Giảm liều piracetam ở trẻ em. Betahistine chưa được nghiên cứu đầy đủ ở trẻ em.",
            },
            "geriatric_dosing": {
                "considerations": "Người cao tuổi nhạy cảm hơn với tác dụng phụ. Giảm liều piracetam ở suy thận (phổ biến ở người cao tuổi).",
                "dose_adjustment": "Giảm liều piracetam 50% nếu suy thận. Liều betahistine tương tự người trẻ nhưng thận trọng hơn.",
                "monitoring": "Theo dõi sát tác dụng phụ tiêu hóa, chức năng thận (do piracetam).",
            },
            "cost_estimate": {
                "unit": "VND",
                "range": "5,000 - 20,000 VND/viên (tùy hàm lượng và thương hiệu)",
                "note": "Giá thay đổi theo thương hiệu và nhà thuốc. Sản phẩm kết hợp thường đắt hơn. Có thể mua riêng Betahistine và Piracetam để tiết kiệm chi phí.",
            }
    },
    "Sumatriptan/Metoclopramide":     {
        "group": "Neurology - Combination (Triptan + Antiemetic)",
        "vietnamese_name": "Sumatriptan/Metoclopramide, Migraine Antiemetic Combination",
        "brand_names": {
            "common": ["Migraine Antiemetic Combination", "Sumatriptan/Metoclopramide"],
            "vietnam": ["Sumatriptan/Metoclopramide", "Imitrex/Metoclopramide"],
        },
        "administration": [
            "PO",
            "SC"
    ],
        "indications": [
            "Cắt cơn đau đầu Migraine cấp tính với buồn nôn, nôn",
            "Migraine nặng với triệu chứng tiêu hóa"
    ],
        "contraindications": {
            "tuyệt_đối": [
                "Dị ứng sumatriptan hoặc metoclopramide",
                "Bệnh mạch vành, Đau thắt ngực, Nhồi máu cơ tim cũ",
                "Tăng huyết áp không kiểm soát",
                "Đột quỵ hoặc TIA tiền sử",
                "Bệnh mạch máu ngoại vi",
                "Suy gan nặng",
                "Dùng cùng MAO Inhibitors (trong 14 ngày)",
                "Dùng cùng Ergotamine/Dihydroergotamine (trong 24 giờ)",
                "Pheochromocytoma",
                "Glaucoma góc đóng"
    ],
            "tương_đối": [
                "Suy gan trung bình - thận trọng",
                "Rối loạn nhịp tim - thận trọng"
    ],
        },
        "dosage": {
            "adult_oral": "Sumatriptan 50-100mg/Metoclopramide 10mg x 1 lần. Có thể lặp lại sau 2 giờ. Tối đa Sumatriptan 200mg/24h.",
            "adult_sc": "Sumatriptan 6mg SC/Metoclopramide 10mg PO hoặc IM. Có thể lặp lại sau 1 giờ. Tối đa Sumatriptan 12mg/24h.",
            "notes": "Kết hợp sumatriptan (triptan, cắt cơn migraine) và metoclopramide (antiemetic, prokinetic). Metoclopramide giúp giảm buồn nôn, nôn và tăng hấp thu sumatriptan. Tác dụng hiệp đồng: cắt cơn migraine và giảm triệu chứng tiêu hóa. Dùng càng sớm càng tốt khi bắt đầu cơn đau.",
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "Không đổi",
            "under_30": "Thận trọng"
        },
        "side_effects": [
            "Cảm giác nặng/thắt ngực, cổ họng (Chest tightness) - do sumatriptan",
            "Chóng mặt, buồn ngủ - do sumatriptan",
            "Hội chứng ngoại tháp (EPS) - do metoclopramide",
            "Buồn nôn, nôn - giảm với metoclopramide",
            "Nóng bừng mặt",
            "Mệt mỏi"
    ],
        "interactions": [
            "Ergotamine/Dihydroergotamine: CHỐNG CHỈ ĐỊNH (trong 24 giờ) - tăng nguy cơ co mạch nặng",
            "MAO inhibitors: CHỐNG CHỈ ĐỊNH (trong 14 ngày)",
            "Thuốc gây EPS (Antipsychotics) -> Tăng nguy cơ EPS với metoclopramide",
            "SSRI/SNRI: tăng nguy cơ hội chứng serotonin (hiếm)"
    ],
        "pregnancy": "C",
        "mechanism_of_action": """Kết hợp sumatriptan (5-HT1B/1D receptor agonist, triptan) và metoclopramide (antiemetic, prokinetic). Sumatriptan: (1) Kích thích 5-HT1B receptors ở mạch máu não → co mạch (giảm giãn mạch trong migraine), (2) Kích thích 5-HT1D receptors → ức chế phóng thích chất trung gian gây viêm (CGRP, substance P) từ dây thần kinh trigeminal. Metoclopramide: (1) Dopamine D2 receptor antagonist → chống nôn, (2) Prokinetic → tăng nhu động dạ dày, tăng hấp thu sumatriptan, (3) Giảm buồn nôn, nôn. Tác dụng hiệp đồng: sumatriptan cắt cơn migraine, metoclopramide giảm buồn nôn và tăng hấp thu → hiệu quả tốt hơn trong migraine với buồn nôn, nôn. Tuy nhiên, metoclopramide có nguy cơ EPS.""",
        "monitoring": [
            "Đáp ứng lâm sàng (giảm đau migraine, triệu chứng)",
            "Tác dụng phụ tim mạch (cảm giác nặng/thắt ngực) - do sumatriptan",
            "Dấu hiệu ngoại tháp (EPS) - do metoclopramide",
            "Buồn nôn, nôn"
    ],
        "precautions": [
            "CHỐNG CHỈ ĐỊNH với ergotamine/dihydroergotamine trong 24 giờ",
            "CHỐNG CHỈ ĐỊNH với MAO inhibitors trong 14 ngày",
            "Nguy cơ hội chứng ngoại tháp (EPS) - do metoclopramide",
            "Dùng càng sớm càng tốt khi bắt đầu cơn đau",
            "Không dùng để phòng ngừa",
            "Thận trọng ở bệnh nhân có nguy cơ tim mạch"
    ],
        "pharmacokinetics": {
            "half_life": "2 giờ (sumatriptan), 5-6 giờ (metoclopramide)",
            "onset": "10-30 phút (SC), 30-60 phút (PO)",
            "duration": "4-6 giờ",
            "protein_binding": "14-21% (sumatriptan), 30% (metoclopramide)",
            "clearance": "Gan: chuyển hóa (sumatriptan qua MAO-A, metoclopramide qua CYP2D6). Thận: thải trừ.",
        },
        "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm, tránh ánh sáng.",
        "black_box_warnings": "CHỐNG CHỈ ĐỊNH với ergotamine/dihydroergotamine trong 24 giờ. CHỐNG CHỈ ĐỊNH với MAO inhibitors trong 14 ngày. Nguy cơ co mạch mạch vành và mạch máu ngoại vi. Nguy cơ hội chứng ngoại tháp (EPS) với metoclopramide.",
        "drug_interactions": {
            "major": [
    {
                    "drug": "Ergotamine, Dihydroergotamine",
                    "mechanism": "Tác dụng cộng dồn co mạch",
                    "effect": "Tăng nguy cơ co mạch mạch vành và mạch máu ngoại vi nghiêm trọng",
                    "management": "CHỐNG CHỈ ĐỊNH - không dùng với ergotamine/dihydroergotamine trong 24 giờ.",
                },
    {
                    "drug": "MAO inhibitors",
                    "mechanism": "Ức chế chuyển hóa sumatriptan qua MAO-A",
                    "effect": "Tăng nồng độ sumatriptan, tăng nguy cơ tác dụng phụ nghiêm trọng",
                    "management": "CHỐNG CHỈ ĐỊNH - không dùng trong 14 ngày sau khi ngừng MAO inhibitors.",
                }
                ],
            "moderate": [
    {
                    "drug": "Thuốc gây EPS (Antipsychotics)",
                    "mechanism": "Tác dụng cộng dồn dopamine D2 antagonism",
                    "effect": "Tăng nguy cơ hội chứng ngoại tháp (EPS)",
                    "management": "Thận trọng. Theo dõi dấu hiệu EPS.",
                }
                ],
            "minor": [],
        },
        "pregnancy_lactation": {
            "fda_category": "C",
            "pregnancy_details": "Category C. Có thể dùng nếu lợi ích > nguy cơ. Có nguy cơ co mạch có thể ảnh hưởng đến thai nhi.",
            "lactation": {
                "safety": "Caution",
                "details": "Cả hai thuốc đều bài tiết vào sữa mẹ. Có thể gây tác dụng phụ ở trẻ.",
                "recommendation": "Thận trọng khi cho con bú.",
            },
        },
        "hepatic_adjustment": {
            "mild": "Không đổi",
            "moderate": "Thận trọng",
            "severe": "CHỐNG CHỈ ĐỊNH",
            "notes": "Cả hai thuốc đều chuyển hóa ở gan. Suy gan nặng là chống chỉ định.",
        },
        "overdose_management": {
            "symptoms": [
                "Sumatriptan quá liều: co mạch mạch vành, co mạch mạch máu ngoại vi, tăng huyết áp",
                "Metoclopramide quá liều: hội chứng ngoại tháp nặng, buồn nôn, nôn"
    ],
            "antidote": "Không có antidote đặc hiệu",
            "treatment": [
                "Đánh giá đường thở, hô hấp, tuần hoàn - QUAN TRỌNG",
                "Theo dõi ECG, huyết áp liên tục",
                "Điều trị co mạch nếu có (nitroglycerin, calcium channel blockers)",
                "Điều trị EPS nếu có (diphenhydramine, benztropine)",
                "Rửa dạ dày nếu trong vòng 1-2 giờ",
                "Than hoạt tính",
                "Điều trị hỗ trợ"
    ],
            "monitoring": "Theo dõi ECG, huyết áp liên tục (QUAN TRỌNG), ý thức, hô hấp, dấu hiệu EPS",
        },
        "reversal_agents": {
            "available": False,
            "agents": [],
        },
        "administration_instructions": {
            "oral": {
                "with_food": "Có thể uống với hoặc không thức ăn",
                "timing": "Sumatriptan 50-100mg/Metoclopramide 10mg x 1 lần khi có cơn migraine. Có thể lặp lại sau 2 giờ nếu cần. Tối đa Sumatriptan 200mg/24h. Dùng càng sớm càng tốt khi bắt đầu cơn đau.",
            },
            "sc": {
                "reconstitution": "Không cần pha",
                "injection_site": "Tiêm dưới da",
                "notes": "Sumatriptan 6mg SC/Metoclopramide 10mg PO hoặc IM. Có thể lặp lại sau 1 giờ. Tối đa Sumatriptan 12mg/24h.",
            },
        },
        "references": {
            "primary_sources": [
                "FDA Drug Label - Migraine Antiemetic Combination (Sumatriptan/Metoclopramide)",
                "UpToDate - Combination migraine treatment",
                "AHS Guidelines - Acute Migraine Treatment"
    ],
            "last_updated": "2025-02-18",
            "evidence_level": "High - FDA-approved, extensive clinical data",
        },
            "risk_flags": {
                "high_alert": True,
                "narrow_therapeutic_index": False,
                "bleeding_risk": False,
                "organ_toxicity": ["cardiac", "vascular", "neurological"],
                "qt_prolongation": False,
                "hepatotoxicity": False,
                "nephrotoxicity": False,
                "requires_monitoring": ["ECG", "Blood pressure", "Cardiac symptoms", "EPS signs"],
            },
            "guideline_tags": [
                "FDA Drug Information",
                "UpToDate Drug Information",
                "AHS Guidelines - Acute Migraine Treatment",
            ],
            "pediatric_dosing": {
                "notes": "Không khuyến cáo cho trẻ em dưới 18 tuổi (dữ liệu hạn chế, nguy cơ tác dụng phụ cao). Sumatriptan không được FDA chấp thuận cho trẻ em.",
            },
            "geriatric_dosing": {
                "considerations": "Người cao tuổi tăng nguy cơ bệnh tim mạch → CHỐNG CHỈ ĐỊNH nếu có bệnh tim mạch. Tăng nguy cơ tác dụng phụ (cảm giác nặng/thắt ngực, hội chứng ngoại tháp).",
                "dose_adjustment": "Liều tương tự người trẻ nhưng thận trọng hơn. CHỐNG CHỈ ĐỊNH nếu có bệnh tim mạch, tăng huyết áp không kiểm soát. Theo dõi chặt chẽ tác dụng phụ tim mạch và EPS.",
                "monitoring": "Theo dõi tác dụng phụ tim mạch (cảm giác nặng/thắt ngực) - QUAN TRỌNG. Theo dõi dấu hiệu EPS. CHỐNG CHỈ ĐỊNH nếu có bệnh tim mạch.",
            },
            "cost_estimate": {
                "unit": "VND",
                "range": "50,000 - 150,000 VND/liều (tùy hàm lượng và thương hiệu)",
                "note": "Giá thay đổi theo thương hiệu và nhà thuốc. Sản phẩm kết hợp thường đắt hơn. Có thể mua riêng Sumatriptan và Metoclopramide để tiết kiệm chi phí.",
            }
},
}

__all__ = ["NEUROLOGICAL_COMBINATIONS_DRUGS"]


