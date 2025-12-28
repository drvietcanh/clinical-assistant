"""
Obstetrics and Gynecology Medications
Includes contraception and hormone therapy drugs
Note: Uterotonics are in emergency/uterotonics.py
"""

OBSTETRICS_GYNECOLOGY_DRUGS = {
    "Levonorgestrel": {
        "group": "Obstetrics/Gynecology - Emergency Contraception",
        "vietnamese_name": "Levonorgestrel, Plan B, Next Choice",
        "administration": ["PO"],
        "indications": [
            "Tránh thai khẩn cấp (emergency contraception)",
            "Dự phòng mang thai sau quan hệ tình dục không được bảo vệ",
            "Dự phòng mang thai sau thất bại biện pháp tránh thai (ví dụ: bao cao su bị rách)"
        ],
        "contraindications": [
            "Dị ứng levonorgestrel",
            "Đã mang thai (không hiệu quả, không gây sẩy thai)",
            "Xuất huyết âm đạo bất thường chưa rõ nguyên nhân"
        ],
        "dosage": {
            "adult_emergency_contraception": "1.5mg PO x 1 liều duy nhất (càng sớm càng tốt, tối đa 72 giờ sau quan hệ)",
            "adult_emergency_contraception_2_dose": "0.75mg PO x 2 liều cách nhau 12 giờ (nếu dùng dạng 2 liều)",
            "notes": "Levonorgestrel là thuốc tránh thai khẩn cấp (emergency contraception). Hiệu quả cao nhất nếu dùng trong 24 giờ đầu (95%), giảm dần theo thời gian (85% trong 48-72 giờ). KHÔNG gây sẩy thai nếu đã mang thai. Cơ chế: ức chế rụng trứng, làm dày chất nhầy cổ tử cung, làm mỏng niêm mạc tử cung."
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "Không cần điều chỉnh đáng kể",
            "under_30": "Không cần điều chỉnh đáng kể"
        },
        "side_effects": [
            "Buồn nôn - phổ biến",
            "Nôn - phổ biến (nếu nôn trong vòng 2 giờ sau uống, cần uống lại)",
            "Đau đầu",
            "Chóng mặt",
            "Mệt mỏi",
            "Đau bụng",
            "Chảy máu âm đạo bất thường (spotting)",
            "Chậm kinh (delay menses) - có thể chậm đến 1 tuần",
            "Đau vú"
        ],
        "interactions": [
            "Thuốc ức chế CYP3A4 (ketoconazole, ritonavir): có thể tăng nồng độ levonorgestrel",
            "Thuốc cảm ứng CYP3A4 (rifampin, carbamazepine): có thể giảm hiệu quả",
            "Thuốc chống co giật (phenytoin, carbamazepine): có thể giảm hiệu quả"
        ],
        "pregnancy": "X - CHỐNG CHỈ ĐỊNH nếu đã mang thai (nhưng không gây sẩy thai)",
        "mechanism_of_action": "Levonorgestrel là progestin tổng hợp. Cơ chế tránh thai khẩn cấp: (1) Ức chế rụng trứng (ovulation) - cơ chế chính nếu dùng trước rụng trứng, (2) Làm dày chất nhầy cổ tử cung (cervical mucus) - ngăn tinh trùng vào tử cung, (3) Làm mỏng niêm mạc tử cung (endometrium) - giảm khả năng làm tổ của trứng đã thụ tinh. KHÔNG gây sẩy thai nếu đã mang thai (không ảnh hưởng đến thai đã làm tổ). ĐẶC ĐIỂM: (1) Hiệu quả cao nhất nếu dùng trong 24 giờ đầu (95%), (2) Hiệu quả giảm dần theo thời gian (85% trong 48-72 giờ), (3) KHÔNG gây sẩy thai nếu đã mang thai, (4) Buồn nôn, nôn phổ biến, (5) Có thể chậm kinh đến 1 tuần.",
        "monitoring": [
            "Dấu hiệu mang thai (nếu chậm kinh >1 tuần, cần test thai)",
            "Dấu hiệu nôn (nếu nôn trong vòng 2 giờ sau uống, cần uống lại)",
            "Chảy máu âm đạo bất thường"
        ],
        "precautions": [
            "Hiệu quả giảm dần theo thời gian - dùng càng sớm càng tốt (tối đa 72 giờ)",
            "Nếu nôn trong vòng 2 giờ sau uống - cần uống lại liều",
            "KHÔNG bảo vệ khỏi STI (sexually transmitted infections) - cần dùng bao cao su",
            "KHÔNG dùng như biện pháp tránh thai thường xuyên - chỉ dùng khẩn cấp",
            "Có thể chậm kinh đến 1 tuần - không lo lắng",
            "Nếu chậm kinh >1 tuần - cần test thai",
            "Thận trọng ở bệnh nhân dùng thuốc cảm ứng CYP3A4 (có thể giảm hiệu quả)"
        ],
        "pharmacokinetics": {
            "half_life": "24-30 giờ",
            "onset": "Ngay lập tức (ức chế rụng trứng)",
            "duration": "Tác dụng ngắn (chỉ 1 liều)",
            "protein_binding": "50%",
            "metabolism": "Gan (CYP3A4)",
            "clearance": "Gan, thận (bài tiết qua nước tiểu và phân)"
        },
        "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm, tránh ánh sáng.",
        "black_box_warnings": None,
        "drug_interactions": {
            "major": [
                {
                    "drug": "Thuốc cảm ứng CYP3A4 (Rifampin, Carbamazepine, Phenytoin, St. John's Wort)",
                    "mechanism": "Cảm ứng CYP3A4, tăng chuyển hóa levonorgestrel",
                    "effect": "Giảm nồng độ levonorgestrel, giảm hiệu quả tránh thai khẩn cấp",
                    "management": "Thận trọng. Có thể cần tăng liều hoặc dùng biện pháp tránh thai khác."
                }
            ],
            "moderate": [
                {
                    "drug": "Thuốc ức chế CYP3A4 (Ketoconazole, Ritonavir, Clarithromycin)",
                    "mechanism": "Ức chế CYP3A4, giảm chuyển hóa levonorgestrel",
                    "effect": "Tăng nồng độ levonorgestrel, tăng nguy cơ tác dụng phụ",
                    "management": "Thận trọng. Theo dõi tác dụng phụ."
                }
            ],
            "minor": []
        },
        "contraindications": {
            "tuyệt_đối": [
                "Dị ứng levonorgestrel",
                "Đã mang thai - CHỐNG CHỈ ĐỊNH (nhưng không gây sẩy thai)"
            ],
            "tương_đối": [
                "Xuất huyết âm đạo bất thường chưa rõ nguyên nhân - thận trọng",
                "Dùng với thuốc cảm ứng CYP3A4 - có thể giảm hiệu quả"
            ]
        },
        "pregnancy_lactation": {
            "fda_category": "X",
            "pregnancy_details": "Levonorgestrel là thuốc phân loại X. CHỐNG CHỈ ĐỊNH nếu đã mang thai. Tuy nhiên, levonorgestrel KHÔNG gây sẩy thai nếu đã mang thai (không ảnh hưởng đến thai đã làm tổ). Levonorgestrel chỉ hiệu quả nếu dùng trước khi thai làm tổ.",
            "lactation": {
                "safety": "Compatible",
                "details": "Levonorgestrel bài tiết vào sữa mẹ ở nồng độ thấp. Không có báo cáo về tác dụng phụ đáng kể ở trẻ bú mẹ khi dùng liều tránh thai khẩn cấp.",
                "recommendation": "Có thể dùng khi cho con bú. Nồng độ trong sữa mẹ thấp và không gây tác dụng phụ ở trẻ bú mẹ."
            }
        },
        "hepatic_adjustment": {
            "mild": "Không cần điều chỉnh liều",
            "moderate": "Thận trọng. Chuyển hóa qua gan có thể giảm, tăng nồng độ levonorgestrel.",
            "severe": "Thận trọng. Chuyển hóa qua gan giảm đáng kể, tăng nồng độ levonorgestrel và nguy cơ tác dụng phụ.",
            "notes": "Levonorgestrel chuyển hóa qua gan (CYP3A4). Suy gan có thể làm giảm chuyển hóa, tăng nồng độ và nguy cơ tác dụng phụ."
        },
        "overdose_management": {
            "symptoms": [
                "Buồn nôn, nôn nặng",
                "Chảy máu âm đạo bất thường",
                "Chóng mặt, mệt mỏi"
            ],
            "antidote": "Không có antidote đặc hiệu. Điều trị hỗ trợ.",
            "treatment": [
                "Nếu nôn nặng:",
                "  - Điều trị buồn nôn, nôn",
                "  - Theo dõi tình trạng mất nước",
                "Nếu chảy máu âm đạo nặng:",
                "  - Theo dõi lượng máu mất",
                "  - Điều trị hỗ trợ nếu cần",
                "Theo dõi: Dấu hiệu sinh tồn, lượng máu mất"
            ],
            "monitoring": "Theo dõi dấu hiệu sinh tồn, lượng máu mất cho đến khi hồi phục."
        },
        "reversal_agents": None,
        "administration_instructions": {
            "oral": {
                "with_food": "Uống với hoặc không thức ăn. Có thể uống không thức ăn.",
                "timing": "1.5mg PO x 1 liều duy nhất (càng sớm càng tốt, tối đa 72 giờ sau quan hệ).",
                "notes": "QUAN TRỌNG: 1) Dùng càng sớm càng tốt (tối đa 72 giờ), 2) Nếu nôn trong vòng 2 giờ sau uống, cần uống lại, 3) KHÔNG bảo vệ khỏi STI, 4) KHÔNG dùng như biện pháp tránh thai thường xuyên, 5) Có thể chậm kinh đến 1 tuần."
            }
        },
        "references": {
            "primary_sources": [
                "FDA Drug Label - Levonorgestrel (Plan B, Next Choice)",
                "ACOG Practice Bulletin - Emergency Contraception",
                "WHO Recommendations - Emergency Contraception",
                "UpToDate - Levonorgestrel: Drug Information",
                "Medscape - Levonorgestrel Drug Reference"
            ],
            "last_updated": "2025-02-18",
            "evidence_level": "A - Dựa trên FDA drug labels, ACOG/WHO guidelines, và dữ liệu lâm sàng từ nhiều nguồn"
        }
        "black_box_warnings": "Cần xem xét black box warnings",
        "reversal_agents": {
            "available": false,
            "agents": [],
        },
    },
    
    "Ethinyl estradiol + Levonorgestrel": {
        "group": "Obstetrics/Gynecology - Combined Oral Contraceptive",
        "vietnamese_name": "Ethinyl Estradiol + Levonorgestrel, Loestrin, Nordette",
        "administration": ["PO"],
        "indications": [
            "Tránh thai (contraception)",
            "Điều hòa kinh nguyệt (menstrual regulation)",
            "Giảm đau bụng kinh (dysmenorrhea)",
            "Giảm mụn trứng cá (acne) - một số chế phẩm",
            "Giảm nguy cơ ung thư buồng trứng và ung thư nội mạc tử cung"
        ],
        "contraindications": {
            "tuyệt_đối": [
                "Dị ứng ethinyl estradiol hoặc levonorgestrel",
                "Huyết khối tĩnh mạch sâu (DVT) hoặc thuyên tắc phổi (PE) hiện tại hoặc tiền sử",
                "Bệnh tim mạch nặng (bệnh mạch vành, đột quỵ, nhồi máu cơ tim)",
                "Tăng huyết áp không kiểm soát (>160/100 mmHg)",
                "Ung thư vú hiện tại hoặc tiền sử",
                "Ung thư nội mạc tử cung hiện tại hoặc tiền sử",
                "Ung thư gan hiện tại hoặc tiền sử",
                "Bệnh gan nặng (viêm gan cấp, suy gan)",
                "Migraine với aura",
                "Hút thuốc lá ≥35 tuổi",
                "Đã mang thai (suspected or confirmed)"
            ],
            "tương_đối": [
                "Hút thuốc lá <35 tuổi - tăng nguy cơ",
                "Tăng huyết áp kiểm soát tốt - thận trọng",
                "Đái tháo đường với biến chứng mạch máu - thận trọng",
                "Bệnh gan nhẹ - thận trọng",
                "Migraine không có aura - thận trọng",
                "Béo phì (BMI >30) - tăng nguy cơ",
                "Tiền sử gia đình huyết khối tĩnh mạch - thận trọng"
            ]
        },
        "dosage": {
            "adult_contraception_21_day": "1 viên PO x 1 lần/ngày trong 21 ngày, nghỉ 7 ngày, lặp lại",
            "adult_contraception_28_day": "1 viên hoạt động PO x 1 lần/ngày trong 21 ngày, sau đó 1 viên giả dược trong 7 ngày, lặp lại",
            "adult_contraception_extended": "1 viên PO x 1 lần/ngày liên tục (một số chế phẩm)",
            "notes": "Ethinyl estradiol + Levonorgestrel là thuốc tránh thai kết hợp (combined oral contraceptive - COC). Nhiều chế phẩm với tỷ lệ khác nhau. Uống đều đặn mỗi ngày vào cùng một thời điểm. Hiệu quả tránh thai >99% nếu dùng đúng cách."
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "Không cần điều chỉnh đáng kể",
            "under_30": "Không cần điều chỉnh đáng kể"
        },
        "side_effects": {
            "phổ_biến": [
                "Buồn nôn - phổ biến trong vài tháng đầu",
                "Đau đầu",
                "Chóng mặt",
                "Chảy máu âm đạo bất thường (breakthrough bleeding) - phổ biến trong vài tháng đầu",
                "Đau vú",
                "Tăng cân nhẹ",
                "Thay đổi tâm trạng",
                "Giảm ham muốn tình dục"
            ],
            "nghiêm_trọng": [
                "Huyết khối tĩnh mạch sâu (DVT) - NGUY HIỂM",
                "Thuyên tắc phổi (PE) - NGUY HIỂM",
                "Đột quỵ (stroke) - NGUY HIỂM",
                "Nhồi máu cơ tim (MI) - NGUY HIỂM",
                "Ung thư vú - tăng nguy cơ nhẹ",
                "Ung thư cổ tử cung - tăng nguy cơ nhẹ",
                "Tăng huyết áp",
                "Bệnh gan (viêm gan, u máu gan)"
            ]
        },
        "interactions": {
            "giảm_hiệu_quả": [
                "Thuốc cảm ứng CYP3A4 (rifampin, carbamazepine, phenytoin, St. John's Wort)",
                "Một số kháng sinh (ampicillin, tetracycline) - dữ liệu không rõ ràng",
                "Một số thuốc chống HIV (efavirenz, nevirapine)"
            ],
            "tăng_nguy_cơ": [
                "Thuốc ức chế CYP3A4 (ketoconazole, ritonavir): tăng nồng độ estrogen",
                "Thuốc gây QT kéo dài: tăng nguy cơ rối loạn nhịp tim"
            ]
        },
        "pregnancy": "X - CHỐNG CHỈ ĐỊNH nếu đã mang thai",
        "mechanism_of_action": "Ethinyl estradiol + Levonorgestrel là thuốc tránh thai kết hợp (combined oral contraceptive - COC). Cơ chế: (1) Ức chế rụng trứng (ovulation) - cơ chế chính, (2) Làm dày chất nhầy cổ tử cung (cervical mucus) - ngăn tinh trùng vào tử cung, (3) Làm mỏng niêm mạc tử cung (endometrium) - giảm khả năng làm tổ của trứng đã thụ tinh. Hiệu quả tránh thai >99% nếu dùng đúng cách. ĐẶC ĐIỂM: (1) Hiệu quả tránh thai >99% nếu dùng đúng cách, (2) Nhiều chế phẩm với tỷ lệ khác nhau, (3) Nguy cơ huyết khối tĩnh mạch (DVT, PE) - tăng nguy cơ, đặc biệt ở hút thuốc lá, (4) Nguy cơ đột quỵ, nhồi máu cơ tim - tăng nguy cơ, (5) Cần uống đều đặn mỗi ngày vào cùng một thời điểm.",
        "monitoring": [
            "Huyết áp - định kỳ",
            "Dấu hiệu huyết khối tĩnh mạch (đau chân, sưng chân, đau ngực, khó thở) - NGUY HIỂM",
            "Dấu hiệu đột quỵ (yếu liệt, nói khó, nhìn mờ) - NGUY HIỂM",
            "Dấu hiệu nhồi máu cơ tim (đau ngực, khó thở) - NGUY HIỂM",
            "Chảy máu âm đạo bất thường",
            "Dấu hiệu ung thư vú (khối u vú, thay đổi da vú)"
        ],
        "precautions": {
            "quan_trọng": [
                "CHỐNG CHỈ ĐỊNH ở huyết khối tĩnh mạch, bệnh tim mạch nặng, ung thư vú",
                "CHỐNG CHỈ ĐỊNH ở hút thuốc lá ≥35 tuổi",
                "Nguy cơ huyết khối tĩnh mạch (DVT, PE) - tăng nguy cơ, đặc biệt ở hút thuốc lá",
                "Nguy cơ đột quỵ, nhồi máu cơ tim - tăng nguy cơ",
                "Uống đều đặn mỗi ngày vào cùng một thời điểm - QUAN TRỌNG",
                "Nếu quên uống >48 giờ - cần dùng biện pháp tránh thai bổ sung",
                "KHÔNG bảo vệ khỏi STI - cần dùng bao cao su"
            ],
            "khác": [
                "Buồn nôn, chảy máu âm đạo bất thường - phổ biến trong vài tháng đầu, thường giảm",
                "Thận trọng ở bệnh nhân dùng thuốc cảm ứng CYP3A4 (có thể giảm hiệu quả)",
                "Thận trọng ở bệnh nhân béo phì (BMI >30) - tăng nguy cơ huyết khối"
            ]
        },
        "pharmacokinetics": {
            "half_life": "Ethinyl estradiol: 24 giờ; Levonorgestrel: 24-30 giờ",
            "onset": "Ngay lập tức (ức chế rụng trứng)",
            "duration": "Dài (cần dùng liên tục)",
            "protein_binding": "Ethinyl estradiol: 98%; Levonorgestrel: 50%",
            "metabolism": "Gan (CYP3A4, CYP2C9)",
            "clearance": "Gan, thận (bài tiết qua nước tiểu và phân)"
        },
        "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm, tránh ánh sáng.",
        "black_box_warnings": "Nguy cơ huyết khối tĩnh mạch (DVT, PE), đột quỵ, nhồi máu cơ tim. CHỐNG CHỈ ĐỊNH ở hút thuốc lá ≥35 tuổi. CHỐNG CHỈ ĐỊNH ở huyết khối tĩnh mạch, bệnh tim mạch nặng, ung thư vú.",
        "drug_interactions": {
            "major": [
                {
                    "drug": "Thuốc cảm ứng CYP3A4 (Rifampin, Carbamazepine, Phenytoin, St. John's Wort)",
                    "mechanism": "Cảm ứng CYP3A4, tăng chuyển hóa ethinyl estradiol và levonorgestrel",
                    "effect": "Giảm nồng độ, giảm hiệu quả tránh thai",
                    "management": "TRÁNH DÙNG CHUNG. Nếu bắt buộc, cần dùng biện pháp tránh thai bổ sung (bao cao su)."
                }
            ],
            "moderate": [
                {
                    "drug": "Một số kháng sinh (Ampicillin, Tetracycline)",
                    "mechanism": "Có thể ảnh hưởng hệ vi khuẩn đường ruột, giảm hấp thu",
                    "effect": "Có thể giảm hiệu quả tránh thai (dữ liệu không rõ ràng)",
                    "management": "Thận trọng. Có thể cần dùng biện pháp tránh thai bổ sung."
                }
            ],
            "minor": []
        },
        "contraindications_detail": {
            "tuyệt_đối": [
                "Dị ứng ethinyl estradiol hoặc levonorgestrel",
                "Huyết khối tĩnh mạch sâu (DVT) hoặc thuyên tắc phổi (PE) hiện tại hoặc tiền sử - CHỐNG CHỈ ĐỊNH",
                "Bệnh tim mạch nặng (bệnh mạch vành, đột quỵ, nhồi máu cơ tim) - CHỐNG CHỈ ĐỊNH",
                "Tăng huyết áp không kiểm soát (>160/100 mmHg) - CHỐNG CHỈ ĐỊNH",
                "Ung thư vú hiện tại hoặc tiền sử - CHỐNG CHỈ ĐỊNH",
                "Ung thư nội mạc tử cung hiện tại hoặc tiền sử - CHỐNG CHỈ ĐỊNH",
                "Ung thư gan hiện tại hoặc tiền sử - CHỐNG CHỈ ĐỊNH",
                "Bệnh gan nặng (viêm gan cấp, suy gan) - CHỐNG CHỈ ĐỊNH",
                "Migraine với aura - CHỐNG CHỈ ĐỊNH",
                "Hút thuốc lá ≥35 tuổi - CHỐNG CHỈ ĐỊNH",
                "Đã mang thai - CHỐNG CHỈ ĐỊNH"
            ],
            "tương_đối": [
                "Hút thuốc lá <35 tuổi - tăng nguy cơ huyết khối",
                "Tăng huyết áp kiểm soát tốt - thận trọng",
                "Đái tháo đường với biến chứng mạch máu - thận trọng",
                "Bệnh gan nhẹ - thận trọng",
                "Migraine không có aura - thận trọng",
                "Béo phì (BMI >30) - tăng nguy cơ huyết khối",
                "Tiền sử gia đình huyết khối tĩnh mạch - thận trọng"
            ]
        },
        "pregnancy_lactation": {
            "fda_category": "X",
            "pregnancy_details": "Ethinyl estradiol + Levonorgestrel là thuốc phân loại X. CHỐNG CHỈ ĐỊNH nếu đã mang thai. Nếu mang thai khi đang dùng, ngừng ngay và tư vấn bác sĩ.",
            "lactation": {
                "safety": "Compatible with Caution",
                "details": "Ethinyl estradiol và levonorgestrel bài tiết vào sữa mẹ ở nồng độ thấp. Có thể ảnh hưởng đến sản xuất sữa và trẻ bú mẹ. Không khuyến cáo dùng trong 6 tuần đầu sau sinh.",
                "recommendation": "Có thể dùng khi cho con bú sau 6 tuần, nhưng thận trọng. Theo dõi sản xuất sữa và trẻ bú mẹ."
            }
        },
        "hepatic_adjustment": {
            "mild": "Không cần điều chỉnh liều",
            "moderate": "Thận trọng. Chuyển hóa qua gan có thể giảm, tăng nồng độ và nguy cơ tác dụng phụ.",
            "severe": "CHỐNG CHỈ ĐỊNH. Chuyển hóa qua gan giảm đáng kể, tăng nguy cơ bệnh gan và tác dụng phụ nặng.",
            "notes": "Ethinyl estradiol và levonorgestrel chuyển hóa qua gan. Suy gan có thể làm giảm chuyển hóa, tăng nồng độ và nguy cơ bệnh gan, tác dụng phụ nặng."
        },
        "overdose_management": {
            "symptoms": [
                "Buồn nôn, nôn nặng",
                "Chảy máu âm đạo nặng",
                "Chóng mặt, mệt mỏi"
            ],
            "antidote": "Không có antidote đặc hiệu. Điều trị hỗ trợ.",
            "treatment": [
                "Ngừng ngay thuốc",
                "Nếu chảy máu âm đạo nặng:",
                "  - Theo dõi lượng máu mất",
                "  - Điều trị hỗ trợ nếu cần",
                "Theo dõi: Dấu hiệu sinh tồn, lượng máu mất"
            ],
            "monitoring": "Theo dõi dấu hiệu sinh tồn, lượng máu mất cho đến khi hồi phục."
        },
        "reversal_agents": None,
        "administration_instructions": {
            "oral": {
                "with_food": "Uống với hoặc không thức ăn. Có thể uống không thức ăn.",
                "timing": "1 viên PO x 1 lần/ngày vào cùng một thời điểm mỗi ngày. Uống đều đặn.",
                "schedule": "21 ngày uống, 7 ngày nghỉ (hoặc 28 ngày với viên giả dược).",
                "missed_dose": "Nếu quên uống <24 giờ: uống ngay khi nhớ, tiếp tục bình thường. Nếu quên uống >48 giờ: cần dùng biện pháp tránh thai bổ sung.",
                "notes": "QUAN TRỌNG: 1) Uống đều đặn mỗi ngày vào cùng một thời điểm, 2) Nếu quên uống >48 giờ, cần dùng biện pháp tránh thai bổ sung, 3) KHÔNG bảo vệ khỏi STI, 4) Nguy cơ huyết khối tĩnh mạch, đột quỵ, nhồi máu cơ tim."
            }
        },
        "references": {
            "primary_sources": [
                "FDA Drug Label - Combined Oral Contraceptives",
                "ACOG Practice Bulletin - Combined Hormonal Contraception",
                "WHO Medical Eligibility Criteria for Contraceptive Use",
                "UpToDate - Combined Oral Contraceptives: Drug Information",
                "Medscape - Combined Oral Contraceptives Drug Reference"
            ],
            "last_updated": "2025-02-18",
            "evidence_level": "A - Dựa trên FDA drug labels, ACOG/WHO guidelines, và dữ liệu lâm sàng từ nhiều nguồn"
        }
        "reversal_agents": {
            "available": false,
            "agents": [],
        },
    },
    
    "Medroxyprogesterone": {
        "group": "Obstetrics/Gynecology - Progestin Contraception (Injectable)",
        "vietnamese_name": "Medroxyprogesterone, Depo-Provera",
        "administration": ["IM"],
        "indications": [
            "Tránh thai (contraception) - dài hạn",
            "Điều hòa kinh nguyệt (menstrual regulation)",
            "Giảm đau bụng kinh (dysmenorrhea)",
            "Điều trị lạc nội mạc tử cung (endometriosis)",
            "Điều trị ung thư nội mạc tử cung hoặc ung thư thận"
        ],
        "contraindications": {
            "tuyệt_đối": [
                "Dị ứng medroxyprogesterone",
                "Ung thư vú hiện tại hoặc tiền sử",
                "Ung thư nội mạc tử cung hiện tại (trừ điều trị ung thư)",
                "Ung thư gan hiện tại hoặc tiền sử",
                "Bệnh gan nặng (viêm gan cấp, suy gan)",
                "Huyết khối tĩnh mạch sâu (DVT) hoặc thuyên tắc phổi (PE) hiện tại hoặc tiền sử",
                "Xuất huyết âm đạo bất thường chưa rõ nguyên nhân",
                "Đã mang thai (suspected or confirmed)"
            ],
            "tương_đối": [
                "Bệnh gan nhẹ - thận trọng",
                "Tiền sử gia đình ung thư vú - thận trọng",
                "Bệnh tim mạch - thận trọng",
                "Đái tháo đường - thận trọng",
                "Trầm cảm - thận trọng (có thể làm nặng)"
            ]
        },
        "dosage": {
            "adult_contraception_im": "150mg IM mỗi 12 tuần (3 tháng)",
            "adult_contraception_im_timing": "Tiêm trong vòng 5 ngày đầu của chu kỳ kinh nguyệt",
            "adult_contraception_im_postpartum": "Tiêm trong vòng 5 ngày sau sinh (nếu không cho con bú)",
            "notes": "Medroxyprogesterone là thuốc tránh thai tiêm (injectable contraception). Hiệu quả tránh thai >99%. Tiêm mỗi 12 tuần (3 tháng). Có thể gây mất kinh (amenorrhea) - không nguy hiểm. Có thể gây giảm mật độ xương (bone density) - hồi phục sau khi ngừng."
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "Không cần điều chỉnh đáng kể",
            "under_30": "Không cần điều chỉnh đáng kể"
        },
        "side_effects": {
            "phổ_biến": [
                "Mất kinh (amenorrhea) - phổ biến sau vài tháng",
                "Chảy máu âm đạo bất thường (irregular bleeding) - phổ biến trong vài tháng đầu",
                "Tăng cân - phổ biến",
                "Đau đầu",
                "Thay đổi tâm trạng, trầm cảm",
                "Giảm ham muốn tình dục",
                "Đau vú",
                "Mệt mỏi"
            ],
            "nghiêm_trọng": [
                "Giảm mật độ xương (bone density loss) - có thể hồi phục sau khi ngừng",
                "Ung thư vú - tăng nguy cơ nhẹ",
                "Huyết khối tĩnh mạch sâu (DVT) - hiếm",
                "Thuyên tắc phổi (PE) - hiếm",
                "Bệnh gan (viêm gan, u máu gan) - hiếm"
            ]
        },
        "interactions": {
            "giảm_hiệu_quả": [
                "Thuốc cảm ứng CYP3A4 (rifampin, carbamazepine, phenytoin, St. John's Wort)"
            ],
            "tăng_nguy_cơ": [
                "Thuốc ức chế CYP3A4 (ketoconazole, ritonavir): tăng nồng độ medroxyprogesterone"
            ]
        },
        "pregnancy": "X - CHỐNG CHỈ ĐỊNH nếu đã mang thai",
        "mechanism_of_action": "Medroxyprogesterone là progestin tổng hợp. Cơ chế tránh thai: (1) Ức chế rụng trứng (ovulation) - cơ chế chính, (2) Làm dày chất nhầy cổ tử cung (cervical mucus) - ngăn tinh trùng vào tử cung, (3) Làm mỏng niêm mạc tử cung (endometrium) - giảm khả năng làm tổ của trứng đã thụ tinh. Hiệu quả tránh thai >99%. Tác dụng kéo dài 12 tuần (3 tháng). ĐẶC ĐIỂM: (1) Hiệu quả tránh thai >99%, (2) Tiêm mỗi 12 tuần (3 tháng), (3) Có thể gây mất kinh (amenorrhea) - không nguy hiểm, (4) Có thể gây giảm mật độ xương - hồi phục sau khi ngừng, (5) Tăng cân phổ biến, (6) Có thể gây trầm cảm.",
        "monitoring": [
            "Dấu hiệu mang thai (nếu chậm kinh >3 tháng, cần test thai)",
            "Chảy máu âm đạo bất thường",
            "Dấu hiệu trầm cảm (thay đổi tâm trạng, mất ngủ, mệt mỏi)",
            "Dấu hiệu ung thư vú (khối u vú, thay đổi da vú)",
            "Mật độ xương (nếu dùng >2 năm, đặc biệt ở phụ nữ trẻ)"
        ],
        "precautions": {
            "quan_trọng": [
                "CHỐNG CHỈ ĐỊNH ở ung thư vú, huyết khối tĩnh mạch, bệnh gan nặng",
                "Tiêm đúng lịch mỗi 12 tuần - QUAN TRỌNG",
                "Mất kinh (amenorrhea) - không nguy hiểm, nhưng cần test thai nếu nghi ngờ",
                "Giảm mật độ xương - có thể hồi phục sau khi ngừng, thận trọng nếu dùng >2 năm",
                "Tăng cân - phổ biến, cần tư vấn chế độ ăn và tập thể dục",
                "Có thể gây trầm cảm - cần theo dõi sát",
                "KHÔNG bảo vệ khỏi STI - cần dùng bao cao su"
            ],
            "khác": [
                "Chảy máu âm đạo bất thường - phổ biến trong vài tháng đầu, thường giảm",
                "Thận trọng ở bệnh nhân dùng thuốc cảm ứng CYP3A4 (có thể giảm hiệu quả)",
                "Thận trọng ở bệnh nhân có tiền sử trầm cảm"
            ]
        },
        "pharmacokinetics": {
            "half_life": "50 ngày (dài)",
            "onset": "Ngay lập tức (ức chế rụng trứng)",
            "duration": "12 tuần (3 tháng)",
            "protein_binding": "90%",
            "metabolism": "Gan (CYP3A4)",
            "clearance": "Gan, thận (bài tiết qua nước tiểu và phân)"
        },
        "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh đông lạnh, tránh ánh sáng. Lắc kỹ trước khi tiêm.",
        "black_box_warnings": "Giảm mật độ xương (bone density loss). Có thể hồi phục sau khi ngừng. Thận trọng nếu dùng >2 năm, đặc biệt ở phụ nữ trẻ.",
        "drug_interactions": {
            "major": [
                {
                    "drug": "Thuốc cảm ứng CYP3A4 (Rifampin, Carbamazepine, Phenytoin, St. John's Wort)",
                    "mechanism": "Cảm ứng CYP3A4, tăng chuyển hóa medroxyprogesterone",
                    "effect": "Giảm nồng độ, giảm hiệu quả tránh thai",
                    "management": "TRÁNH DÙNG CHUNG. Nếu bắt buộc, cần dùng biện pháp tránh thai bổ sung (bao cao su)."
                }
            ],
            "moderate": [],
            "minor": []
        },
        "contraindications_detail": {
            "tuyệt_đối": [
                "Dị ứng medroxyprogesterone",
                "Ung thư vú hiện tại hoặc tiền sử - CHỐNG CHỈ ĐỊNH",
                "Ung thư nội mạc tử cung hiện tại (trừ điều trị ung thư) - CHỐNG CHỈ ĐỊNH",
                "Ung thư gan hiện tại hoặc tiền sử - CHỐNG CHỈ ĐỊNH",
                "Bệnh gan nặng (viêm gan cấp, suy gan) - CHỐNG CHỈ ĐỊNH",
                "Huyết khối tĩnh mạch sâu (DVT) hoặc thuyên tắc phổi (PE) hiện tại hoặc tiền sử - CHỐNG CHỈ ĐỊNH",
                "Xuất huyết âm đạo bất thường chưa rõ nguyên nhân - CHỐNG CHỈ ĐỊNH",
                "Đã mang thai - CHỐNG CHỈ ĐỊNH"
            ],
            "tương_đối": [
                "Bệnh gan nhẹ - thận trọng",
                "Tiền sử gia đình ung thư vú - thận trọng",
                "Bệnh tim mạch - thận trọng",
                "Đái tháo đường - thận trọng",
                "Trầm cảm - thận trọng (có thể làm nặng)"
            ]
        },
        "pregnancy_lactation": {
            "fda_category": "X",
            "pregnancy_details": "Medroxyprogesterone là thuốc phân loại X. CHỐNG CHỈ ĐỊNH nếu đã mang thai. Nếu mang thai khi đang dùng, ngừng ngay và tư vấn bác sĩ.",
            "lactation": {
                "safety": "Compatible",
                "details": "Medroxyprogesterone bài tiết vào sữa mẹ ở nồng độ thấp. Không có báo cáo về tác dụng phụ đáng kể ở trẻ bú mẹ. Có thể dùng khi cho con bú sau 6 tuần.",
                "recommendation": "Có thể dùng khi cho con bú sau 6 tuần. Nồng độ trong sữa mẹ thấp và không gây tác dụng phụ ở trẻ bú mẹ."
            }
        },
        "hepatic_adjustment": {
            "mild": "Không cần điều chỉnh liều",
            "moderate": "Thận trọng. Chuyển hóa qua gan có thể giảm, tăng nồng độ và nguy cơ tác dụng phụ.",
            "severe": "CHỐNG CHỈ ĐỊNH. Chuyển hóa qua gan giảm đáng kể, tăng nguy cơ bệnh gan và tác dụng phụ nặng.",
            "notes": "Medroxyprogesterone chuyển hóa qua gan. Suy gan có thể làm giảm chuyển hóa, tăng nồng độ và nguy cơ bệnh gan, tác dụng phụ nặng."
        },
        "overdose_management": {
            "symptoms": [
                "Chảy máu âm đạo nặng",
                "Chóng mặt, mệt mỏi",
                "Thay đổi tâm trạng nặng"
            ],
            "antidote": "Không có antidote đặc hiệu. Điều trị hỗ trợ.",
            "treatment": [
                "Nếu chảy máu âm đạo nặng:",
                "  - Theo dõi lượng máu mất",
                "  - Điều trị hỗ trợ nếu cần",
                "Theo dõi: Dấu hiệu sinh tồn, lượng máu mất, tình trạng tinh thần"
            ],
            "monitoring": "Theo dõi dấu hiệu sinh tồn, lượng máu mất, tình trạng tinh thần cho đến khi hồi phục."
        },
        "reversal_agents": None,
        "administration_instructions": {
            "im": {
                "reconstitution": "Lắc kỹ trước khi tiêm.",
                "injection_site": "Tiêm sâu vào cơ lớn (mông, đùi).",
                "timing": "150mg IM mỗi 12 tuần (3 tháng). Tiêm trong vòng 5 ngày đầu của chu kỳ kinh nguyệt hoặc trong vòng 5 ngày sau sinh (nếu không cho con bú).",
                "notes": "QUAN TRỌNG: 1) Tiêm đúng lịch mỗi 12 tuần, 2) Mất kinh không nguy hiểm, nhưng cần test thai nếu nghi ngờ, 3) Giảm mật độ xương có thể hồi phục sau khi ngừng, 4) Tăng cân phổ biến, 5) Có thể gây trầm cảm."
            }
        },
        "references": {
            "primary_sources": [
                "FDA Drug Label - Medroxyprogesterone (Depo-Provera)",
                "ACOG Practice Bulletin - Injectable Contraception",
                "WHO Medical Eligibility Criteria for Contraceptive Use",
                "UpToDate - Medroxyprogesterone: Drug Information",
                "Medscape - Medroxyprogesterone Drug Reference"
            ],
            "last_updated": "2025-02-18",
            "evidence_level": "A - Dựa trên FDA drug labels, ACOG/WHO guidelines, và dữ liệu lâm sàng từ nhiều nguồn"
        }
        "reversal_agents": {
            "available": false,
            "agents": [],
        },
    },
    
    "Estradiol": {
        "group": "Obstetrics/Gynecology - Estrogen Replacement Therapy",
        "vietnamese_name": "Estradiol, Estrace, Climara",
        "administration": ["PO", "Transdermal", "Vaginal"],
        "indications": [
            "Điều trị triệu chứng mãn kinh (hot flashes, night sweats, vaginal dryness)",
            "Phòng ngừa loãng xương (osteoporosis) ở phụ nữ mãn kinh",
            "Điều trị suy buồng trứng (ovarian failure)",
            "Điều trị thiếu hụt estrogen (hypoestrogenism)",
            "Điều trị khô âm đạo (vaginal atrophy)"
        ],
        "contraindications": {
            "tuyệt_đối": [
                "Dị ứng estradiol",
                "Ung thư vú hiện tại hoặc tiền sử",
                "Ung thư nội mạc tử cung hiện tại hoặc tiền sử",
                "Ung thư gan hiện tại hoặc tiền sử",
                "Huyết khối tĩnh mạch sâu (DVT) hoặc thuyên tắc phổi (PE) hiện tại hoặc tiền sử",
                "Bệnh tim mạch nặng (bệnh mạch vành, đột quỵ, nhồi máu cơ tim)",
                "Tăng huyết áp không kiểm soát",
                "Bệnh gan nặng (viêm gan cấp, suy gan)",
                "Xuất huyết âm đạo bất thường chưa rõ nguyên nhân",
                "Đã mang thai (suspected or confirmed)"
            ],
            "tương_đối": [
                "Bệnh gan nhẹ - thận trọng",
                "Tăng huyết áp kiểm soát tốt - thận trọng",
                "Đái tháo đường - thận trọng",
                "Migraine - thận trọng",
                "Bệnh túi mật - thận trọng",
                "Tiền sử gia đình ung thư vú - thận trọng"
            ]
        },
        "dosage": {
            "adult_menopause_po": "1-2mg PO x 1 lần/ngày",
            "adult_menopause_transdermal": "0.025-0.1mg/ngày qua patch, thay mỗi 3-7 ngày tùy chế phẩm",
            "adult_vaginal_atrophy": "0.5-2g cream hoặc 10-25mcg tablet đặt âm đạo x 1 lần/ngày trong 2 tuần, sau đó 2-3 lần/tuần",
            "notes": "Estradiol là estrogen replacement therapy. Nhiều chế phẩm và đường dùng. Dùng liều thấp nhất hiệu quả. Nếu còn tử cung, cần dùng kết hợp với progestin để giảm nguy cơ ung thư nội mạc tử cung."
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "Không cần điều chỉnh đáng kể",
            "under_30": "Không cần điều chỉnh đáng kể"
        },
        "side_effects": {
            "phổ_biến": [
                "Đau đầu",
                "Buồn nôn",
                "Đau vú",
                "Chảy máu âm đạo bất thường (breakthrough bleeding)",
                "Chuột rút bụng",
                "Đầy hơi",
                "Tăng cân nhẹ",
                "Giữ nước"
            ],
            "nghiêm_trọng": [
                "Ung thư vú - tăng nguy cơ",
                "Ung thư nội mạc tử cung - tăng nguy cơ (nếu dùng đơn độc không có progestin)",
                "Huyết khối tĩnh mạch sâu (DVT) - tăng nguy cơ",
                "Thuyên tắc phổi (PE) - tăng nguy cơ",
                "Đột quỵ (stroke) - tăng nguy cơ",
                "Nhồi máu cơ tim (MI) - tăng nguy cơ",
                "Bệnh túi mật (gallbladder disease) - tăng nguy cơ",
                "Bệnh gan (viêm gan, u máu gan) - hiếm"
            ]
        },
        "interactions": {
            "giảm_hiệu_quả": [
                "Thuốc cảm ứng CYP3A4 (rifampin, carbamazepine, phenytoin, St. John's Wort)"
            ],
            "tăng_nguy_cơ": [
                "Thuốc ức chế CYP3A4 (ketoconazole, ritonavir): tăng nồng độ estradiol"
            ]
        },
        "pregnancy": "X - CHỐNG CHỈ ĐỊNH nếu đã mang thai",
        "mechanism_of_action": "Estradiol là estrogen tự nhiên. Bổ sung estrogen cho phụ nữ mãn kinh hoặc thiếu hụt estrogen. Tác dụng: (1) Giảm triệu chứng mãn kinh (hot flashes, night sweats), (2) Cải thiện khô âm đạo, (3) Phòng ngừa loãng xương, (4) Cải thiện tình trạng da và tóc. ĐẶC ĐIỂM: (1) Nhiều chế phẩm và đường dùng (PO, transdermal, vaginal), (2) Dùng liều thấp nhất hiệu quả, (3) Nếu còn tử cung, cần dùng kết hợp với progestin, (4) Nguy cơ ung thư vú, huyết khối tĩnh mạch, đột quỵ - tăng nguy cơ, (5) Nguy cơ ung thư nội mạc tử cung nếu dùng đơn độc không có progestin.",
        "monitoring": [
            "Triệu chứng mãn kinh (hot flashes, night sweats, vaginal dryness)",
            "Huyết áp - định kỳ",
            "Dấu hiệu huyết khối tĩnh mạch (đau chân, sưng chân, đau ngực, khó thở) - NGUY HIỂM",
            "Dấu hiệu đột quỵ (yếu liệt, nói khó, nhìn mờ) - NGUY HIỂM",
            "Dấu hiệu nhồi máu cơ tim (đau ngực, khó thở) - NGUY HIỂM",
            "Chảy máu âm đạo bất thường",
            "Dấu hiệu ung thư vú (khối u vú, thay đổi da vú)",
            "Mật độ xương (nếu dùng để phòng ngừa loãng xương)"
        ],
        "precautions": {
            "quan_trọng": [
                "CHỐNG CHỈ ĐỊNH ở ung thư vú, huyết khối tĩnh mạch, bệnh tim mạch nặng",
                "Dùng liều thấp nhất hiệu quả - QUAN TRỌNG",
                "Nếu còn tử cung, cần dùng kết hợp với progestin để giảm nguy cơ ung thư nội mạc tử cung",
                "Nguy cơ ung thư vú - tăng nguy cơ, cần khám vú định kỳ",
                "Nguy cơ huyết khối tĩnh mạch (DVT, PE) - tăng nguy cơ",
                "Nguy cơ đột quỵ, nhồi máu cơ tim - tăng nguy cơ",
                "Nguy cơ ung thư nội mạc tử cung nếu dùng đơn độc không có progestin - tăng nguy cơ",
                "Nguy cơ bệnh túi mật - tăng nguy cơ"
            ],
            "khác": [
                "Chảy máu âm đạo bất thường - phổ biến trong vài tháng đầu, thường giảm",
                "Thận trọng ở bệnh nhân dùng thuốc cảm ứng CYP3A4 (có thể giảm hiệu quả)",
                "Thận trọng ở bệnh nhân có tiền sử bệnh túi mật"
            ]
        },
        "pharmacokinetics": {
            "half_life": "PO: 13-20 giờ; Transdermal: phụ thuộc patch",
            "onset": "Vài tuần",
            "duration": "Dài (cần dùng liên tục)",
            "protein_binding": "37%",
            "metabolism": "Gan (CYP3A4, CYP1A2)",
            "clearance": "Gan, thận (bài tiết qua nước tiểu và phân)"
        },
        "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm, tránh ánh sáng. Patch: bảo quản trong túi kín.",
        "black_box_warnings": "Nguy cơ ung thư vú, huyết khối tĩnh mạch (DVT, PE), đột quỵ, nhồi máu cơ tim. CHỐNG CHỈ ĐỊNH ở ung thư vú, huyết khối tĩnh mạch, bệnh tim mạch nặng. Dùng liều thấp nhất hiệu quả trong thời gian ngắn nhất cần thiết.",
        "drug_interactions": {
            "major": [
                {
                    "drug": "Thuốc cảm ứng CYP3A4 (Rifampin, Carbamazepine, Phenytoin, St. John's Wort)",
                    "mechanism": "Cảm ứng CYP3A4, tăng chuyển hóa estradiol",
                    "effect": "Giảm nồng độ estradiol, giảm hiệu quả",
                    "management": "Thận trọng. Có thể cần tăng liều estradiol."
                }
            ],
            "moderate": [
                {
                    "drug": "Thuốc ức chế CYP3A4 (Ketoconazole, Ritonavir, Clarithromycin)",
                    "mechanism": "Ức chế CYP3A4, giảm chuyển hóa estradiol",
                    "effect": "Tăng nồng độ estradiol, tăng nguy cơ tác dụng phụ",
                    "management": "Thận trọng. Theo dõi tác dụng phụ."
                }
            ],
            "minor": []
        },
        "contraindications_detail": {
            "tuyệt_đối": [
                "Dị ứng estradiol",
                "Ung thư vú hiện tại hoặc tiền sử - CHỐNG CHỈ ĐỊNH",
                "Ung thư nội mạc tử cung hiện tại hoặc tiền sử - CHỐNG CHỈ ĐỊNH",
                "Ung thư gan hiện tại hoặc tiền sử - CHỐNG CHỈ ĐỊNH",
                "Huyết khối tĩnh mạch sâu (DVT) hoặc thuyên tắc phổi (PE) hiện tại hoặc tiền sử - CHỐNG CHỈ ĐỊNH",
                "Bệnh tim mạch nặng (bệnh mạch vành, đột quỵ, nhồi máu cơ tim) - CHỐNG CHỈ ĐỊNH",
                "Tăng huyết áp không kiểm soát - CHỐNG CHỈ ĐỊNH",
                "Bệnh gan nặng (viêm gan cấp, suy gan) - CHỐNG CHỈ ĐỊNH",
                "Xuất huyết âm đạo bất thường chưa rõ nguyên nhân - CHỐNG CHỈ ĐỊNH",
                "Đã mang thai - CHỐNG CHỈ ĐỊNH"
            ],
            "tương_đối": [
                "Bệnh gan nhẹ - thận trọng",
                "Tăng huyết áp kiểm soát tốt - thận trọng",
                "Đái tháo đường - thận trọng",
                "Migraine - thận trọng",
                "Bệnh túi mật - thận trọng",
                "Tiền sử gia đình ung thư vú - thận trọng"
            ]
        },
        "pregnancy_lactation": {
            "fda_category": "X",
            "pregnancy_details": "Estradiol là thuốc phân loại X. CHỐNG CHỈ ĐỊNH nếu đã mang thai. Nếu mang thai khi đang dùng, ngừng ngay và tư vấn bác sĩ.",
            "lactation": {
                "safety": "Compatible with Caution",
                "details": "Estradiol bài tiết vào sữa mẹ ở nồng độ thấp. Có thể ảnh hưởng đến sản xuất sữa và trẻ bú mẹ. Không khuyến cáo dùng khi cho con bú.",
                "recommendation": "Không khuyến cáo dùng khi cho con bú. Cân nhắc ngừng cho con bú hoặc ngừng thuốc."
            }
        },
        "hepatic_adjustment": {
            "mild": "Không cần điều chỉnh liều",
            "moderate": "Thận trọng. Chuyển hóa qua gan có thể giảm, tăng nồng độ và nguy cơ tác dụng phụ.",
            "severe": "CHỐNG CHỈ ĐỊNH. Chuyển hóa qua gan giảm đáng kể, tăng nguy cơ bệnh gan và tác dụng phụ nặng.",
            "notes": "Estradiol chuyển hóa qua gan. Suy gan có thể làm giảm chuyển hóa, tăng nồng độ và nguy cơ bệnh gan, tác dụng phụ nặng."
        },
        "overdose_management": {
            "symptoms": [
                "Buồn nôn, nôn nặng",
                "Chảy máu âm đạo nặng",
                "Chóng mặt, mệt mỏi"
            ],
            "antidote": "Không có antidote đặc hiệu. Điều trị hỗ trợ.",
            "treatment": [
                "Ngừng ngay estradiol",
                "Nếu chảy máu âm đạo nặng:",
                "  - Theo dõi lượng máu mất",
                "  - Điều trị hỗ trợ nếu cần",
                "Theo dõi: Dấu hiệu sinh tồn, lượng máu mất"
            ],
            "monitoring": "Theo dõi dấu hiệu sinh tồn, lượng máu mất cho đến khi hồi phục."
        },
        "reversal_agents": None,
        "administration_instructions": {
            "oral": {
                "with_food": "Uống với hoặc không thức ăn. Có thể uống không thức ăn.",
                "timing": "1-2mg PO x 1 lần/ngày. Uống đều đặn.",
                "notes": "QUAN TRỌNG: 1) Dùng liều thấp nhất hiệu quả, 2) Nếu còn tử cung, cần dùng kết hợp với progestin, 3) Nguy cơ ung thư vú, huyết khối tĩnh mạch, đột quỵ."
            },
            "transdermal": {
                "preparation": "Patch estradiol.",
                "application": "Dán patch lên vùng da sạch, khô (bụng, mông, đùi). Thay patch mỗi 3-7 ngày tùy chế phẩm.",
                "dosing": "0.025-0.1mg/ngày tùy chế phẩm.",
                "notes": "QUAN TRỌNG: 1) Dùng liều thấp nhất hiệu quả, 2) Nếu còn tử cung, cần dùng kết hợp với progestin, 3) Thay patch đúng lịch."
            },
            "vaginal": {
                "preparation": "Cream hoặc tablet estradiol.",
                "application": "Đặt cream hoặc tablet vào âm đạo. 0.5-2g cream hoặc 10-25mcg tablet x 1 lần/ngày trong 2 tuần, sau đó 2-3 lần/tuần.",
                "notes": "QUAN TRỌNG: 1) Dùng cho khô âm đạo, 2) Hấp thu toàn thân tối thiểu, 3) Ít nguy cơ tác dụng phụ toàn thân hơn PO/transdermal."
            }
        },
        "references": {
            "primary_sources": [
                "FDA Drug Label - Estradiol (Estrace, Climara)",
                "ACOG Practice Bulletin - Hormone Therapy",
                "NAMS (North American Menopause Society) Guidelines",
                "UpToDate - Estradiol: Drug Information",
                "Medscape - Estradiol Drug Reference"
            ],
            "last_updated": "2025-02-18",
            "evidence_level": "A - Dựa trên FDA drug labels, ACOG/NAMS guidelines, và dữ liệu lâm sàng từ nhiều nguồn"
        }
        "reversal_agents": {
            "available": false,
            "agents": [],
        },
    },
    
    "Progesterone": {
        "group": "Obstetrics/Gynecology - Progestin Replacement Therapy",
        "vietnamese_name": "Progesterone, Prometrium, Crinone",
        "administration": ["PO", "Vaginal", "IM"],
        "indications": [
            "Điều trị thiếu hụt progesterone (hypoprogesteronism)",
            "Hỗ trợ giai đoạn hoàng thể (luteal phase support) trong thụ tinh trong ống nghiệm (IVF)",
            "Dự phòng sẩy thai tái phát do thiếu hụt progesterone",
            "Điều hòa kinh nguyệt (menstrual regulation)",
            "Điều trị rong kinh (menorrhagia)",
            "Kết hợp với estrogen trong hormone replacement therapy (HRT) để giảm nguy cơ ung thư nội mạc tử cung"
        ],
        "contraindications": {
            "tuyệt_đối": [
                "Dị ứng progesterone",
                "Ung thư vú hiện tại hoặc tiền sử",
                "Ung thư nội mạc tử cung hiện tại (trừ điều trị ung thư)",
                "Ung thư gan hiện tại hoặc tiền sử",
                "Bệnh gan nặng (viêm gan cấp, suy gan)",
                "Huyết khối tĩnh mạch sâu (DVT) hoặc thuyên tắc phổi (PE) hiện tại hoặc tiền sử",
                "Xuất huyết âm đạo bất thường chưa rõ nguyên nhân"
            ],
            "tương_đối": [
                "Bệnh gan nhẹ - thận trọng",
                "Tiền sử gia đình ung thư vú - thận trọng",
                "Bệnh tim mạch - thận trọng",
                "Đái tháo đường - thận trọng",
                "Trầm cảm - thận trọng (có thể làm nặng)"
            ]
        },
        "dosage": {
            "adult_luteal_support_po": "200-300mg PO x 2-3 lần/ngày trong 12-14 ngày",
            "adult_luteal_support_vaginal": "90-200mg gel hoặc 100-200mg suppository đặt âm đạo x 2-3 lần/ngày trong 12-14 ngày",
            "adult_ivf_support": "Theo phác đồ IVF, thường 200mg gel đặt âm đạo x 2-3 lần/ngày hoặc 200-300mg PO x 2-3 lần/ngày",
            "adult_hrt": "200mg PO x 1 lần/ngày trong 12-14 ngày mỗi tháng (kết hợp với estrogen)",
            "notes": "Progesterone là progestin tự nhiên. Nhiều chế phẩm và đường dùng. Dùng liều thấp nhất hiệu quả. Đường âm đạo thường được ưa chuộng cho hỗ trợ giai đoạn hoàng thể (ít tác dụng phụ toàn thân hơn)."
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "Không cần điều chỉnh đáng kể",
            "under_30": "Không cần điều chỉnh đáng kể"
        },
        "side_effects": {
            "phổ_biến": [
                "Buồn ngủ, mệt mỏi - phổ biến (đặc biệt với PO)",
                "Chóng mặt",
                "Đau đầu",
                "Buồn nôn",
                "Đau vú",
                "Chảy máu âm đạo bất thường (breakthrough bleeding)",
                "Thay đổi tâm trạng",
                "Tăng cân nhẹ"
            ],
            "nghiêm_trọng": [
                "Ung thư vú - tăng nguy cơ nhẹ",
                "Huyết khối tĩnh mạch sâu (DVT) - hiếm",
                "Thuyên tắc phổi (PE) - hiếm",
                "Bệnh gan (viêm gan, u máu gan) - hiếm"
            ]
        },
        "interactions": {
            "giảm_hiệu_quả": [
                "Thuốc cảm ứng CYP3A4 (rifampin, carbamazepine, phenytoin, St. John's Wort)"
            ],
            "tăng_nguy_cơ": [
                "Thuốc ức chế CYP3A4 (ketoconazole, ritonavir): tăng nồng độ progesterone"
            ]
        },
        "pregnancy": "B - An toàn trong thai kỳ (dùng cho hỗ trợ giai đoạn hoàng thể)",
        "mechanism_of_action": "Progesterone là progestin tự nhiên. Tác dụng: (1) Chuẩn bị niêm mạc tử cung (endometrium) cho thai làm tổ, (2) Duy trì thai kỳ sớm (hỗ trợ giai đoạn hoàng thể), (3) Ức chế co bóp tử cung, (4) Giảm nguy cơ ung thư nội mạc tử cung khi dùng kết hợp với estrogen trong HRT. ĐẶC ĐIỂM: (1) Nhiều chế phẩm và đường dùng (PO, vaginal, IM), (2) Đường âm đạo thường được ưa chuộng cho hỗ trợ giai đoạn hoàng thể (ít tác dụng phụ toàn thân), (3) Buồn ngủ, mệt mỏi phổ biến với PO, (4) An toàn trong thai kỳ (category B), (5) Dùng kết hợp với estrogen trong HRT để giảm nguy cơ ung thư nội mạc tử cung.",
        "monitoring": [
            "Triệu chứng (buồn ngủ, mệt mỏi, chóng mặt)",
            "Chảy máu âm đạo bất thường",
            "Dấu hiệu ung thư vú (khối u vú, thay đổi da vú)",
            "Dấu hiệu huyết khối tĩnh mạch (đau chân, sưng chân, đau ngực, khó thở) - hiếm",
            "Tình trạng thai (nếu dùng cho hỗ trợ giai đoạn hoàng thể)"
        ],
        "precautions": {
            "quan_trọng": [
                "CHỐNG CHỈ ĐỊNH ở ung thư vú, huyết khối tĩnh mạch, bệnh gan nặng",
                "Dùng liều thấp nhất hiệu quả",
                "Buồn ngủ, mệt mỏi phổ biến với PO - tránh lái xe hoặc vận hành máy móc",
                "Đường âm đạo thường được ưa chuộng cho hỗ trợ giai đoạn hoàng thể (ít tác dụng phụ toàn thân)",
                "Có thể gây trầm cảm - cần theo dõi sát",
                "Nguy cơ ung thư vú - tăng nguy cơ nhẹ"
            ],
            "khác": [
                "Chảy máu âm đạo bất thường - phổ biến, thường giảm",
                "Thận trọng ở bệnh nhân dùng thuốc cảm ứng CYP3A4 (có thể giảm hiệu quả)",
                "Thận trọng ở bệnh nhân có tiền sử trầm cảm"
            ]
        },
        "pharmacokinetics": {
            "half_life": "PO: 16-18 giờ; Vaginal: phụ thuộc chế phẩm",
            "onset": "Vài giờ đến vài ngày",
            "duration": "Dài (cần dùng liên tục)",
            "protein_binding": "96-99%",
            "metabolism": "Gan (CYP3A4, CYP2C19)",
            "clearance": "Gan, thận (bài tiết qua nước tiểu và phân)"
        },
        "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm, tránh ánh sáng. Một số chế phẩm cần bảo quản trong tủ lạnh.",
        "black_box_warnings": None,
        "drug_interactions": {
            "major": [
                {
                    "drug": "Thuốc cảm ứng CYP3A4 (Rifampin, Carbamazepine, Phenytoin, St. John's Wort)",
                    "mechanism": "Cảm ứng CYP3A4, tăng chuyển hóa progesterone",
                    "effect": "Giảm nồng độ progesterone, giảm hiệu quả",
                    "management": "Thận trọng. Có thể cần tăng liều progesterone."
                }
            ],
            "moderate": [
                {
                    "drug": "Thuốc ức chế CYP3A4 (Ketoconazole, Ritonavir, Clarithromycin)",
                    "mechanism": "Ức chế CYP3A4, giảm chuyển hóa progesterone",
                    "effect": "Tăng nồng độ progesterone, tăng nguy cơ tác dụng phụ",
                    "management": "Thận trọng. Theo dõi tác dụng phụ."
                }
            ],
            "minor": []
        },
        "contraindications_detail": {
            "tuyệt_đối": [
                "Dị ứng progesterone",
                "Ung thư vú hiện tại hoặc tiền sử - CHỐNG CHỈ ĐỊNH",
                "Ung thư nội mạc tử cung hiện tại (trừ điều trị ung thư) - CHỐNG CHỈ ĐỊNH",
                "Ung thư gan hiện tại hoặc tiền sử - CHỐNG CHỈ ĐỊNH",
                "Bệnh gan nặng (viêm gan cấp, suy gan) - CHỐNG CHỈ ĐỊNH",
                "Huyết khối tĩnh mạch sâu (DVT) hoặc thuyên tắc phổi (PE) hiện tại hoặc tiền sử - CHỐNG CHỈ ĐỊNH",
                "Xuất huyết âm đạo bất thường chưa rõ nguyên nhân - CHỐNG CHỈ ĐỊNH"
            ],
            "tương_đối": [
                "Bệnh gan nhẹ - thận trọng",
                "Tiền sử gia đình ung thư vú - thận trọng",
                "Bệnh tim mạch - thận trọng",
                "Đái tháo đường - thận trọng",
                "Trầm cảm - thận trọng (có thể làm nặng)"
            ]
        },
        "pregnancy_lactation": {
            "fda_category": "B",
            "pregnancy_details": "Progesterone là thuốc phân loại B. An toàn trong thai kỳ. Được dùng rộng rãi cho hỗ trợ giai đoạn hoàng thể trong thụ tinh trong ống nghiệm (IVF) và dự phòng sẩy thai tái phát.",
            "lactation": {
                "safety": "Compatible",
                "details": "Progesterone bài tiết vào sữa mẹ ở nồng độ thấp. Không có báo cáo về tác dụng phụ đáng kể ở trẻ bú mẹ.",
                "recommendation": "Có thể dùng khi cho con bú. Nồng độ trong sữa mẹ thấp và không gây tác dụng phụ ở trẻ bú mẹ."
            }
        },
        "hepatic_adjustment": {
            "mild": "Không cần điều chỉnh liều",
            "moderate": "Thận trọng. Chuyển hóa qua gan có thể giảm, tăng nồng độ và nguy cơ tác dụng phụ.",
            "severe": "CHỐNG CHỈ ĐỊNH. Chuyển hóa qua gan giảm đáng kể, tăng nguy cơ bệnh gan và tác dụng phụ nặng.",
            "notes": "Progesterone chuyển hóa qua gan. Suy gan có thể làm giảm chuyển hóa, tăng nồng độ và nguy cơ bệnh gan, tác dụng phụ nặng."
        },
        "overdose_management": {
            "symptoms": [
                "Buồn ngủ nặng",
                "Chóng mặt nặng",
                "Chảy máu âm đạo nặng"
            ],
            "antidote": "Không có antidote đặc hiệu. Điều trị hỗ trợ.",
            "treatment": [
                "Ngừng ngay progesterone",
                "Nếu buồn ngủ nặng:",
                "  - Theo dõi sát",
                "  - Tránh lái xe hoặc vận hành máy móc",
                "Nếu chảy máu âm đạo nặng:",
                "  - Theo dõi lượng máu mất",
                "  - Điều trị hỗ trợ nếu cần",
                "Theo dõi: Dấu hiệu sinh tồn, lượng máu mất, tình trạng tinh thần"
            ],
            "monitoring": "Theo dõi dấu hiệu sinh tồn, lượng máu mất, tình trạng tinh thần cho đến khi hồi phục."
        },
        "reversal_agents": None,
        "administration_instructions": {
            "oral": {
                "with_food": "Uống với thức ăn để giảm buồn nôn và tăng hấp thu.",
                "timing": "200-300mg PO x 2-3 lần/ngày. Uống đều đặn.",
                "notes": "QUAN TRỌNG: 1) Uống với thức ăn, 2) Buồn ngủ, mệt mỏi phổ biến - tránh lái xe, 3) Dùng liều thấp nhất hiệu quả."
            },
            "vaginal": {
                "preparation": "Gel hoặc suppository progesterone.",
                "application": "Đặt gel hoặc suppository vào âm đạo. 90-200mg gel hoặc 100-200mg suppository x 2-3 lần/ngày.",
                "notes": "QUAN TRỌNG: 1) Đường âm đạo thường được ưa chuộng cho hỗ trợ giai đoạn hoàng thể (ít tác dụng phụ toàn thân), 2) Đặt đều đặn."
            },
            "im": {
                "reconstitution": "Dùng dung dịch sẵn có.",
                "injection_site": "Tiêm sâu vào cơ lớn (mông, đùi).",
                "timing": "Theo phác đồ, thường 50-100mg IM mỗi ngày hoặc cách ngày.",
                "notes": "QUAN TRỌNG: 1) Tiêm đúng lịch, 2) Thường dùng cho hỗ trợ giai đoạn hoàng thể."
            }
        },
        "references": {
            "primary_sources": [
                "FDA Drug Label - Progesterone (Prometrium, Crinone)",
                "ACOG Practice Bulletin - Progesterone Supplementation",
                "ASRM (American Society for Reproductive Medicine) Guidelines",
                "UpToDate - Progesterone: Drug Information",
                "Medscape - Progesterone Drug Reference"
            ],
            "last_updated": "2025-02-18",
            "evidence_level": "A - Dựa trên FDA drug labels, ACOG/ASRM guidelines, và dữ liệu lâm sàng từ nhiều nguồn"
        }
        "black_box_warnings": "Cần xem xét black box warnings",
        "reversal_agents": {
            "available": false,
            "agents": [],
        },
    },

    "Clotrimazole (vaginal)": {
        "group": "Obstetrics/Gynecology - Antifungal (Vulvovaginal Candidiasis)",
        "vietnamese_name": "Clotrimazole đặt âm đạo (Canesten, Mycelex-G)",
        "administration": ["Vaginal"],
        "indications": [
            "Nhiễm nấm Candida âm đạo – vulvovaginal candidiasis (VVC) thể nhẹ đến trung bình",
        ],
        "contraindications": [
            "Dị ứng với clotrimazole hoặc bất kỳ thành phần nào của thuốc",
        ],
        "dosage": {
            "adult_vvc_1_day": "Viên đặt 500mg âm đạo, 1 lần duy nhất buổi tối",
            "adult_vvc_3_day": "Viên đặt 200mg âm đạo, 1 viên mỗi tối x 3 ngày",
            "adult_vvc_7_day": "Viên đặt 100mg âm đạo, 1 viên mỗi tối x 7 ngày",
            "notes": "Đặt sâu vào âm đạo trước khi ngủ. Có thể dùng thêm kem bôi ngoài âm hộ nếu ngứa nhiều.",
        },
        "renal_adjustment": {
            "normal": "Không cần chỉnh liều (tác dụng tại chỗ)",
            "30_60": "Không cần chỉnh liều",
            "under_30": "Không cần chỉnh liều",
        },
        "side_effects": [
            "Kích ứng tại chỗ: nóng rát, ngứa, châm chích nhẹ",
            "Tiết dịch tăng tạm thời",
            "Phản ứng dị ứng rất hiếm",
        ],
        "interactions": [
            "Ít tương tác toàn thân do hấp thu rất ít; có thể làm giảm độ bền bao cao su/diaphragm latex trong thời gian dùng.",
        ],
        "pregnancy": "B – có thể dùng trong thai kỳ (ưu tiên phác đồ 7 ngày, đặt bằng tay thay vì dụng cụ nếu 3 tháng cuối).",
        "mechanism_of_action": (
            "Clotrimazole là azole chống nấm, ức chế tổng hợp ergosterol màng tế bào nấm, làm thay đổi tính thấm "
            "màng, gây chết tế bào nấm Candida tại chỗ."
        ),
        "monitoring": [
            "Giảm triệu chứng ngứa, khí hư vón cục sau 3–7 ngày",
            "Nếu triệu chứng tái phát thường xuyên (≥4 lần/năm) → cần đánh giá VVC tái phát, tiểu đường, suy giảm miễn dịch",
        ],
        "precautions": [
            "Tránh quan hệ trong thời gian điều trị hoặc dùng bao cao su; lưu ý thuốc có thể làm giảm độ bền latex.",
            "Nếu triệu chứng không cải thiện sau 7 ngày hoặc tái phát nhiều lần, cần khám phụ khoa để loại trừ chẩn đoán khác.",
        ],
        "pharmacokinetics": {
            "half_life": "Không áp dụng (tác dụng tại chỗ, hấp thu rất ít)",
            "onset": "Vài giờ – vài ngày",
            "duration": "Tác dụng kéo dài trong ngày sau đặt",
            "protein_binding": "Không đáng kể toàn thân",
            "clearance": "Chủ yếu tại chỗ, phần rất nhỏ hấp thu chuyển hóa ở gan.",
        },
        "storage": "Bảo quản nơi khô mát, tránh nhiệt độ cao.",
        "black_box_warnings": None,
        "drug_interactions": {
            "major": [],
            "moderate": [],
            "minor": [],
        },
        "contraindications_detail": {
            "tuyệt_đối": [
                "Dị ứng với clotrimazole hoặc tá dược",
            ],
            "tương_đối": [
                "Âm đạo trợt loét nhiều (cần khám trước khi tự điều trị)",
            ],
        },
        "pregnancy_lactation": {
            "fda_category": "B",
            "pregnancy_details": "Phác đồ đặt 7 ngày được ưa chuộng trong thai kỳ; tránh dụng cụ đặt cứng ở 3 tháng cuối.",
            "lactation": {
                "safety": "Compatible",
                "details": "Hấp thu toàn thân rất ít; an toàn khi cho con bú.",
                "recommendation": "Có thể dùng khi cho con bú.",
            },
        },
        "hepatic_adjustment": {
            "mild": "Không cần chỉnh liều",
            "moderate": "Không cần chỉnh liều",
            "severe": "Không cần chỉnh liều",
            "notes": "Hấp thu toàn thân tối thiểu.",
        },
        "overdose_management": {
            "symptoms": [
                "Kích ứng tại chỗ tăng (rát, đỏ, ngứa nhiều)",
            ],
            "antidote": "Không có; điều trị hỗ trợ.",
            "treatment": [
                "Ngừng thuốc, rửa sạch bằng nước",
                "Điều trị triệu chứng nếu cần (kem dưỡng, kháng histamine đường uống nếu ngứa nhiều)",
            ],
            "monitoring": "Theo dõi cải thiện kích ứng tại chỗ.",
        },
        "reversal_agents": {"available": False, "agents": [], "notes": "Không có antidote đặc hiệu. Điều trị chủ yếu là hỗ trợ và điều trị triệu chứng. Rửa sạch vùng âm đạo nếu cần."},
        "administration_instructions": {
            "vaginal": {
                "with_food": "Không liên quan bữa ăn.",
                "timing": "Đặt buổi tối trước khi ngủ; nằm ngửa và đưa viên/ống đặt sâu vào âm đạo.",
            }
        },
        "references": {
            "primary_sources": [
                "CDC STI Treatment Guidelines – Vulvovaginal candidiasis",
                "UpToDate – Clotrimazole vaginal: Drug information",
            ],
            "last_updated": "2025-02-23",
            "evidence_level": "High – guideline-based local therapy",
        },
        "black_box_warnings": "Cần xem xét black box warnings",
    },

    "Miconazole (vaginal)": {
        "group": "Obstetrics/Gynecology - Antifungal (Vulvovaginal Candidiasis)",
        "vietnamese_name": "Miconazole đặt âm đạo",
        "administration": ["Vaginal"],
        "indications": [
            "Nhiễm nấm Candida âm đạo – VVC thể nhẹ đến trung bình",
        ],
        "contraindications": [
            "Dị ứng với miconazole hoặc azole khác",
        ],
        "dosage": {
            "adult_vvc_3_day": "Viên đặt 200mg âm đạo, 1 viên mỗi tối x 3 ngày",
            "adult_vvc_7_day": "Viên đặt 100mg âm đạo, 1 viên mỗi tối x 7 ngày",
            "notes": "Có thể kèm kem bôi ngoài âm hộ nếu ngứa/nóng rát vùng ngoài.",
        },
        "renal_adjustment": {
            "normal": "Không cần chỉnh liều",
            "30_60": "Không cần chỉnh liều",
            "under_30": "Không cần chỉnh liều",
        },
        "side_effects": [
            "Kích ứng tại chỗ: nóng rát, ngứa, châm chích",
            "Tiết dịch tăng tạm thời",
        ],
        "interactions": [
            "Có thể làm giảm độ bền bao cao su/diaphragm latex trong khi dùng.",
        ],
        "pregnancy": "C – thường tránh liều cao ngắn ngày; có thể dùng dạng 7 ngày nếu cần, theo bác sĩ.",
        "mechanism_of_action": (
            "Miconazole là azole chống nấm, ức chế tổng hợp ergosterol màng tế bào nấm, gây thay đổi tính thấm "
            "màng và chết tế bào nấm. Tác dụng chủ yếu tại chỗ ở âm đạo.",
        ),
        "monitoring": [
            "Giảm ngứa, khí hư sau 3–7 ngày",
        ],
        "precautions": [
            "Nếu triệu chứng không cải thiện hoặc tái phát nhiều lần, cần khám phụ khoa và xét nghiệm.",
        ],
        "pharmacokinetics": {
            "half_life": "Không áp dụng (tại chỗ)",
            "onset": "Vài giờ – vài ngày",
            "duration": "Trong ngày sau đặt",
            "protein_binding": "Không đáng kể toàn thân",
            "clearance": "Chủ yếu tại chỗ; phần nhỏ hấp thu được chuyển hóa ở gan.",
        },
        "storage": "Bảo quản nơi khô mát, tránh ánh sáng.",
        "black_box_warnings": None,
        "drug_interactions": {
            "major": [],
            "moderate": [],
            "minor": [],
        },
        "contraindications_detail": {
            "tuyệt_đối": [
                "Dị ứng với miconazole hoặc azole",
            ],
            "tương_đối": [
                "Âm đạo trợt loét, đau nhiều – cần khám trước khi dùng",
            ],
        },
        "pregnancy_lactation": {
            "fda_category": "C",
            "pregnancy_details": "Chỉ dùng khi lợi ích vượt nguy cơ; ưu tiên clotrimazole/nhóm B nếu khả dụng.",
            "lactation": {
                "safety": "Compatible",
                "details": "Hấp thu toàn thân rất thấp; ít nguy cơ cho trẻ bú mẹ.",
                "recommendation": "Có thể dùng khi cho con bú.",
            },
        },
        "hepatic_adjustment": {
            "mild": "Không cần chỉnh liều",
            "moderate": "Không cần chỉnh liều",
            "severe": "Không cần chỉnh liều",
            "notes": "Tác dụng chủ yếu tại chỗ.",
        },
        "overdose_management": {
            "symptoms": [
                "Kích ứng tại chỗ tăng",
            ],
            "antidote": "Không có; điều trị hỗ trợ.",
            "treatment": [
                "Ngừng thuốc, rửa sạch vùng âm đạo – âm hộ bằng nước sạch",
            ],
            "monitoring": "Theo dõi triệu chứng kích ứng.",
        },
        "reversal_agents": {"available": False, "agents": [], "notes": "Không có antidote đặc hiệu. Điều trị chủ yếu là hỗ trợ và điều trị triệu chứng. Rửa sạch vùng âm đạo nếu cần."},
        "administration_instructions": {
            "vaginal": {
                "with_food": "Không liên quan bữa ăn.",
                "timing": "Đặt buổi tối trước ngủ; tránh đứng dậy ngay sau khi đặt.",
            }
        },
        "references": {
            "primary_sources": [
                "CDC STI Treatment Guidelines – Vulvovaginal candidiasis",
                "UpToDate – Miconazole vaginal: Drug information",
            ],
            "last_updated": "2025-02-23",
            "evidence_level": "High – widely used local antifungal",
        },
        "black_box_warnings": "Cần xem xét black box warnings",
    },

    "Metronidazole (vaginal gel)": {
        "group": "Obstetrics/Gynecology - Nitroimidazole (Bacterial Vaginosis)",
        "vietnamese_name": "Metronidazole gel âm đạo 0,75%",
        "administration": ["Vaginal"],
        "indications": [
            "Bacterial vaginosis (BV) – viêm âm đạo do vi khuẩn",
        ],
        "contraindications": [
            "Dị ứng với metronidazole hoặc nitroimidazole",
            "Ba tháng đầu thai kỳ (thận trọng, ưu tiên đường uống theo phác đồ nếu cần)",
        ],
        "dosage": {
            "adult_bv": "Gel 0,75%: 5g bơm âm đạo 1 lần/ngày vào buổi tối x 5 ngày",
            "notes": "Không nên dùng chung với bao cao su/diaphragm latex trong khi điều trị (có thể ảnh hưởng vật liệu).",
        },
        "renal_adjustment": {
            "normal": "Không cần chỉnh liều (hấp thu toàn thân thấp)",
            "30_60": "Không cần chỉnh liều",
            "under_30": "Không cần chỉnh liều",
        },
        "side_effects": [
            "Kích ứng âm đạo nhẹ, nóng rát, ngứa",
            "Tiết dịch tăng tạm thời",
            "Vị kim loại, buồn nôn rất hiếm (do hấp thu nhỏ)",
        ],
        "interactions": [
            "Rượu: lý thuyết có phản ứng giống disulfiram nhưng với dạng gel nguy cơ rất thấp.",
        ],
        "pregnancy": "B – thường tránh 3 tháng đầu; dùng được từ tam cá nguyệt 2–3 theo hướng dẫn.",
        "mechanism_of_action": (
            "Metronidazole là nitroimidazole, được khử trong tế bào vi khuẩn kỵ khí, tạo gốc tự do gây phá hủy DNA vi khuẩn. "
            "Dạng gel âm đạo tập trung tác dụng tại chỗ trên Gardnerella và vi khuẩn kỵ khí gây BV, giảm hấp thu toàn thân."
        ),
        "monitoring": [
            "Giảm khí hư hôi, giảm ngứa/sưng sau 3–5 ngày",
            "Nếu không cải thiện hoặc tái phát nhiều lần, cần xét nghiệm và loại trừ STI khác.",
        ],
        "precautions": [
            "Tránh quan hệ đường âm đạo trong thời gian điều trị hoặc dùng bao cao su; lưu ý tương tác với latex.",
            "Nếu bệnh nhân có viêm âm đạo nặng/huyết trắng lẫn máu, cần khám phụ khoa trước khi dùng.",
        ],
        "pharmacokinetics": {
            "half_life": "Tác dụng tại chỗ; phần nhỏ hấp thu có t1/2 khoảng 8 giờ",
            "onset": "Vài ngày",
            "duration": "Tác dụng trong ngày sau bơm",
            "protein_binding": "~20% (phần hấp thu)",
            "clearance": "Gan (chuyển hóa) và thận (thải trừ) cho phần hấp thu nhỏ.",
        },
        "storage": "Bảo quản ở nhiệt độ phòng, tránh nóng; giữ ống thuốc kín nắp.",
        "black_box_warnings": None,
        "drug_interactions": {
            "major": [],
            "moderate": [],
            "minor": [],
        },
        "contraindications_detail": {
            "tuyệt_đối": [
                "Dị ứng metronidazole/nitroimidazole",
            ],
            "tương_đối": [
                "Ba tháng đầu thai kỳ",
            ],
        },
        "pregnancy_lactation": {
            "fda_category": "B",
            "pregnancy_details": "Dạng gel âm đạo với hấp thu thấp; tránh 3 tháng đầu nếu có lựa chọn khác.",
            "lactation": {
                "safety": "Compatible",
                "details": "Hấp thu ít, lượng vào sữa thấp; nguy cơ thấp cho trẻ bú mẹ.",
                "recommendation": "Có thể dùng khi cho con bú; nếu lo lắng có thể cho bú trước khi dùng thuốc.",
            },
        },
        "hepatic_adjustment": {
            "mild": "Không cần chỉnh liều",
            "moderate": "Không cần chỉnh liều",
            "severe": "Thận trọng; hấp thu toàn thân thấp nhưng vẫn nên theo dõi nếu dùng kéo dài.",
            "notes": "Phần hấp thu nhỏ chuyển hóa ở gan.",
        },
        "overdose_management": {
            "symptoms": [
                "Kích ứng âm đạo tăng",
            ],
            "antidote": "Không có; điều trị hỗ trợ.",
            "treatment": [
                "Ngừng thuốc; rửa sạch nếu kích ứng nhiều.",
            ],
            "monitoring": "Theo dõi giảm kích ứng; nếu không cải thiện, khám phụ khoa.",
        },
        "reversal_agents": {"available": False, "agents": [], "notes": "Không có antidote đặc hiệu. Điều trị chủ yếu là hỗ trợ và điều trị triệu chứng. Rửa sạch vùng âm đạo nếu cần."},
        "administration_instructions": {
            "vaginal": {
                "with_food": "Không liên quan bữa ăn.",
                "timing": "Bơm 5g gel vào âm đạo buổi tối trước ngủ trong 5 ngày; sử dụng applicator đúng cách.",
            }
        },
        "references": {
            "primary_sources": [
                "CDC STI Treatment Guidelines – Bacterial vaginosis",
                "UpToDate – Metronidazole vaginal: Drug information",
            ],
            "last_updated": "2025-02-23",
            "evidence_level": "High – guideline-recommended local therapy",
        },
    },
}

__all__ = ['OBSTETRICS_GYNECOLOGY_DRUGS']

