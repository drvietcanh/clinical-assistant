"""
Neurology / Psychiatry Combination Drugs
Thuốc phối hợp tuần hoàn não, nootropic, và tâm thần kinh.
Ví dụ: Piracetam + Vinpocetine, Citicoline + Piracetam, Ginkgo + Vinpocetine, Olanzapine/Fluoxetine.
"""

NEUROLOGICAL_COMBINATIONS_DRUGS = {
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
         "black_box_warnings": None,
         "black_box_warnings": None,
         "black_box_warnings": None,
         "black_box_warnings": None,
         "black_box_warnings": None,
         "black_box_warnings": None,
         "black_box_warnings": None,
         "black_box_warnings": None,
         "black_box_warnings": None,
         "black_box_warnings": None,
         "black_box_warnings": None,
         "black_box_warnings": None,
         "black_box_warnings": None,
         "black_box_warnings": None,
         "black_box_warnings": None,
         "black_box_warnings": None,
         "black_box_warnings": "Không có",
},
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
             "black_box_warnings": None,
         "black_box_warnings": None,
         "black_box_warnings": None,
         "black_box_warnings": None,
         "black_box_warnings": None,
         "black_box_warnings": None,
         "black_box_warnings": None,
         "black_box_warnings": None,
         "black_box_warnings": None,
         "black_box_warnings": None,
         "black_box_warnings": None,
         "black_box_warnings": None,
         "black_box_warnings": None,
         "black_box_warnings": None,
         "black_box_warnings": None,
         "black_box_warnings": None,
         "black_box_warnings": None,
         "black_box_warnings": "Không có",
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
}

__all__ = ["NEUROLOGICAL_COMBINATIONS_DRUGS"]


