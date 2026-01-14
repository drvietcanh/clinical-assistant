"""
Obstetrics and Gynecology Medications
Contraceptive medications
"""
from typing import Dict, Any

CONTRACEPTIVES_DRUGS: Dict[str, Dict[str, Any]] = {
    "Ethinyl estradiol + Levonorgestrel":     {
        "group": "Obstetrics/Gynecology - Combined Oral Contraceptive",
        "vietnamese_name": "Ethinyl Estradiol + Levonorgestrel, Loestrin, Nordette",
        "administration": [
            "PO"
    ],
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
    ],
        },
        "dosage": {
            "adult_contraception_21_day": "1 viên PO x 1 lần/ngày trong 21 ngày, nghỉ 7 ngày, lặp lại",
            "adult_contraception_28_day": "1 viên hoạt động PO x 1 lần/ngày trong 21 ngày, sau đó 1 viên giả dược trong 7 ngày, lặp lại",
            "adult_contraception_extended": "1 viên PO x 1 lần/ngày liên tục (một số chế phẩm)",
            "notes": """Ethinyl estradiol + Levonorgestrel là thuốc tránh thai kết hợp (combined oral contraceptive - COC). Nhiều chế phẩm với tỷ lệ khác nhau. Uống đều đặn mỗi ngày vào cùng một thời điểm. Hiệu quả tránh thai >99% nếu dùng đúng cách.""",
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "Không cần điều chỉnh đáng kể",
            "under_30": "Không cần điều chỉnh đáng kể",
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
    ],
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
    ],
        },
"pregnancy": "X - CHỐNG CHỈ ĐỊNH nếu đã mang thai",
        "mechanism_of_action": """Ethinyl estradiol + Levonorgestrel là thuốc tránh thai kết hợp (combined oral contraceptive - COC). Cơ chế: (1) Ức chế rụng trứng (ovulation) - cơ chế chính, (2) Làm dày chất nhầy cổ tử cung (cervical mucus) - ngăn tinh trùng vào tử cung, (3) Làm mỏng niêm mạc tử cung (endometrium) - giảm khả năng làm tổ của trứng đã thụ tinh. Hiệu quả tránh thai >99% nếu dùng đúng cách. ĐẶC ĐIỂM: (1) Hiệu quả tránh thai >99% nếu dùng đúng cách, (2) Nhiều chế phẩm với tỷ lệ khác nhau, (3) Nguy cơ huyết khối tĩnh mạch (DVT, PE) - tăng nguy cơ, đặc biệt ở hút thuốc lá, (4) Nguy cơ đột quỵ, nhồi máu cơ tim - tăng nguy cơ, (5) Cần uống đều đặn mỗi ngày vào cùng một thời điểm.""",
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
    ],
        },
        "pharmacokinetics": {
            "half_life": "Ethinyl estradiol: 24 giờ; Levonorgestrel: 24-30 giờ",
            "onset": "Ngay lập tức (ức chế rụng trứng)",
            "duration": "Dài (cần dùng liên tục)",
            "protein_binding": "Ethinyl estradiol: 98%; Levonorgestrel: 50%",
            "metabolism": "Gan (CYP3A4, CYP2C9)",
            "clearance": "Gan, thận (bài tiết qua nước tiểu và phân)",
        },
        "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm, tránh ánh sáng.",
        "black_box_warnings": """Nguy cơ huyết khối tĩnh mạch (DVT, PE), đột quỵ, nhồi máu cơ tim. CHỐNG CHỈ ĐỊNH ở hút thuốc lá ≥35 tuổi. CHỐNG CHỈ ĐỊNH ở huyết khối tĩnh mạch, bệnh tim mạch nặng, ung thư vú.""",
        "drug_interactions": {
            "major": [
    {
                    "drug": "Thuốc cảm ứng CYP3A4 (Rifampin, Carbamazepine, Phenytoin, St. John's Wort)",
                    "mechanism": "Cảm ứng CYP3A4, tăng chuyển hóa ethinyl estradiol và levonorgestrel",
                    "effect": "Giảm nồng độ, giảm hiệu quả tránh thai",
                    "management": "TRÁNH DÙNG CHUNG. Nếu bắt buộc, cần dùng biện pháp tránh thai bổ sung (bao cao su).",
                }
                ],
            "moderate": [
    {
                    "drug": "Một số kháng sinh (Ampicillin, Tetracycline)",
                    "mechanism": "Có thể ảnh hưởng hệ vi khuẩn đường ruột, giảm hấp thu",
                    "effect": "Có thể giảm hiệu quả tránh thai (dữ liệu không rõ ràng)",
                    "management": "Thận trọng. Có thể cần dùng biện pháp tránh thai bổ sung.",
                }
                ],
            "minor": [],
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
    ],
        },
        "pregnancy_lactation": {
            "fda_category": "X",
            "pregnancy_details": """Ethinyl estradiol + Levonorgestrel là thuốc phân loại X. CHỐNG CHỈ ĐỊNH nếu đã mang thai. Nếu mang thai khi đang dùng, ngừng ngay và tư vấn bác sĩ.""",
            "lactation": {
                "safety": "Compatible with Caution",
                "details": """Ethinyl estradiol và levonorgestrel bài tiết vào sữa mẹ ở nồng độ thấp. Có thể ảnh hưởng đến sản xuất sữa và trẻ bú mẹ. Không khuyến cáo dùng trong 6 tuần đầu sau sinh.""",
                "recommendation": "Có thể dùng khi cho con bú sau 6 tuần, nhưng thận trọng. Theo dõi sản xuất sữa và trẻ bú mẹ.",
            },
        },
        "hepatic_adjustment": {
            "mild": "Không cần điều chỉnh liều",
            "moderate": "Thận trọng. Chuyển hóa qua gan có thể giảm, tăng nồng độ và nguy cơ tác dụng phụ.",
            "severe": "CHỐNG CHỈ ĐỊNH. Chuyển hóa qua gan giảm đáng kể, tăng nguy cơ bệnh gan và tác dụng phụ nặng.",
            "notes": """Ethinyl estradiol và levonorgestrel chuyển hóa qua gan. Suy gan có thể làm giảm chuyển hóa, tăng nồng độ và nguy cơ bệnh gan, tác dụng phụ nặng.""",
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
            "monitoring": "Theo dõi dấu hiệu sinh tồn, lượng máu mất cho đến khi hồi phục.",
        },
        "reversal_agents": {
            "available": False,
            "agents": [],
        },
        "administration_instructions": {
            "oral": {
                "with_food": "Uống với hoặc không thức ăn. Có thể uống không thức ăn.",
                "timing": "1 viên PO x 1 lần/ngày vào cùng một thời điểm mỗi ngày. Uống đều đặn.",
                "schedule": "21 ngày uống, 7 ngày nghỉ (hoặc 28 ngày với viên giả dược).",
                "missed_dose": """Nếu quên uống <24 giờ: uống ngay khi nhớ, tiếp tục bình thường. Nếu quên uống >48 giờ: cần dùng biện pháp tránh thai bổ sung.""",
                "notes": """QUAN TRỌNG: 1) Uống đều đặn mỗi ngày vào cùng một thời điểm, 2) Nếu quên uống >48 giờ, cần dùng biện pháp tránh thai bổ sung, 3) KHÔNG bảo vệ khỏi STI, 4) Nguy cơ huyết khối tĩnh mạch, đột quỵ, nhồi máu cơ tim.""",
            },
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
            "evidence_level": "A - Dựa trên FDA drug labels, ACOG/WHO guidelines, và dữ liệu lâm sàng từ nhiều nguồn",
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

    "Levonorgestrel":     {
        "group": "Obstetrics/Gynecology - Emergency Contraception",
        "vietnamese_name": "Levonorgestrel, Plan B, Next Choice",
        "administration": [
            "PO"
    ],
        "indications": [
            "Tránh thai khẩn cấp (emergency contraception)",
            "Dự phòng mang thai sau quan hệ tình dục không được bảo vệ",
            "Dự phòng mang thai sau thất bại biện pháp tránh thai (ví dụ: bao cao su bị rách)"
    ],
        "contraindications": {
            "tuyệt_đối": [
                "Dị ứng levonorgestrel",
                "Đã mang thai - CHỐNG CHỈ ĐỊNH (nhưng không gây sẩy thai)"
    ],
            "tương_đối": [
                "Xuất huyết âm đạo bất thường chưa rõ nguyên nhân - thận trọng",
                "Dùng với thuốc cảm ứng CYP3A4 - có thể giảm hiệu quả"
    ],
        },
        "dosage": {
            "adult_emergency_contraception": "1.5mg PO x 1 liều duy nhất (càng sớm càng tốt, tối đa 72 giờ sau quan hệ)",
            "adult_emergency_contraception_2_dose": "0.75mg PO x 2 liều cách nhau 12 giờ (nếu dùng dạng 2 liều)",
            "notes": """Levonorgestrel là thuốc tránh thai khẩn cấp (emergency contraception). Hiệu quả cao nhất nếu dùng trong 24 giờ đầu (95%), giảm dần theo thời gian (85% trong 48-72 giờ). KHÔNG gây sẩy thai nếu đã mang thai. Cơ chế: ức chế rụng trứng, làm dày chất nhầy cổ tử cung, làm mỏng niêm mạc tử cung.""",
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "Không cần điều chỉnh đáng kể",
            "under_30": "Không cần điều chỉnh đáng kể",
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
        "mechanism_of_action": """Levonorgestrel là progestin tổng hợp. Cơ chế tránh thai khẩn cấp: (1) Ức chế rụng trứng (ovulation) - cơ chế chính nếu dùng trước rụng trứng, (2) Làm dày chất nhầy cổ tử cung (cervical mucus) - ngăn tinh trùng vào tử cung, (3) Làm mỏng niêm mạc tử cung (endometrium) - giảm khả năng làm tổ của trứng đã thụ tinh. KHÔNG gây sẩy thai nếu đã mang thai (không ảnh hưởng đến thai đã làm tổ). ĐẶC ĐIỂM: (1) Hiệu quả cao nhất nếu dùng trong 24 giờ đầu (95%), (2) Hiệu quả giảm dần theo thời gian (85% trong 48-72 giờ), (3) KHÔNG gây sẩy thai nếu đã mang thai, (4) Buồn nôn, nôn phổ biến, (5) Có thể chậm kinh đến 1 tuần.""",
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
            "clearance": "Gan, thận (bài tiết qua nước tiểu và phân)",
        },
        "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm, tránh ánh sáng.",
        "black_box_warnings": "Cần xem xét black box warnings",
        "drug_interactions": {
            "major": [
    {
                    "drug": "Thuốc cảm ứng CYP3A4 (Rifampin, Carbamazepine, Phenytoin, St. John's Wort)",
                    "mechanism": "Cảm ứng CYP3A4, tăng chuyển hóa levonorgestrel",
                    "effect": "Giảm nồng độ levonorgestrel, giảm hiệu quả tránh thai khẩn cấp",
                    "management": "Thận trọng. Có thể cần tăng liều hoặc dùng biện pháp tránh thai khác.",
                }
                ],
            "moderate": [
    {
                    "drug": "Thuốc ức chế CYP3A4 (Ketoconazole, Ritonavir, Clarithromycin)",
                    "mechanism": "Ức chế CYP3A4, giảm chuyển hóa levonorgestrel",
                    "effect": "Tăng nồng độ levonorgestrel, tăng nguy cơ tác dụng phụ",
                    "management": "Thận trọng. Theo dõi tác dụng phụ.",
                }
                ],
            "minor": [],
        },
        "pregnancy_lactation": {
            "fda_category": "X",
            "pregnancy_details": """Levonorgestrel là thuốc phân loại X. CHỐNG CHỈ ĐỊNH nếu đã mang thai. Tuy nhiên, levonorgestrel KHÔNG gây sẩy thai nếu đã mang thai (không ảnh hưởng đến thai đã làm tổ). Levonorgestrel chỉ hiệu quả nếu dùng trước khi thai làm tổ.""",
            "lactation": {
                "safety": "Compatible",
                "details": """Levonorgestrel bài tiết vào sữa mẹ ở nồng độ thấp. Không có báo cáo về tác dụng phụ đáng kể ở trẻ bú mẹ khi dùng liều tránh thai khẩn cấp.""",
                "recommendation": "Có thể dùng khi cho con bú. Nồng độ trong sữa mẹ thấp và không gây tác dụng phụ ở trẻ bú mẹ.",
            },
        },
        "hepatic_adjustment": {
            "mild": "Không cần điều chỉnh liều",
            "moderate": "Thận trọng. Chuyển hóa qua gan có thể giảm, tăng nồng độ levonorgestrel.",
            "severe": "Thận trọng. Chuyển hóa qua gan giảm đáng kể, tăng nồng độ levonorgestrel và nguy cơ tác dụng phụ.",
            "notes": """Levonorgestrel chuyển hóa qua gan (CYP3A4). Suy gan có thể làm giảm chuyển hóa, tăng nồng độ và nguy cơ tác dụng phụ.""",
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
            "monitoring": "Theo dõi dấu hiệu sinh tồn, lượng máu mất cho đến khi hồi phục.",
        },
        "reversal_agents": {
            "available": False,
            "agents": [],
        },
        "administration_instructions": {
            "oral": {
                "with_food": "Uống với hoặc không thức ăn. Có thể uống không thức ăn.",
                "timing": "1.5mg PO x 1 liều duy nhất (càng sớm càng tốt, tối đa 72 giờ sau quan hệ).",
                "notes": """QUAN TRỌNG: 1) Dùng càng sớm càng tốt (tối đa 72 giờ), 2) Nếu nôn trong vòng 2 giờ sau uống, cần uống lại, 3) KHÔNG bảo vệ khỏi STI, 4) KHÔNG dùng như biện pháp tránh thai thường xuyên, 5) Có thể chậm kinh đến 1 tuần.""",
            },
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
            "evidence_level": "A - Dựa trên FDA drug labels, ACOG/WHO guidelines, và dữ liệu lâm sàng từ nhiều nguồn",
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

    "Medroxyprogesterone":     {
        "group": "Obstetrics/Gynecology - Progestin Contraception (Injectable)",
        "vietnamese_name": "Medroxyprogesterone, Depo-Provera",
        "administration": [
            "IM"
    ],
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
    ],
        },
        "dosage": {
            "adult_contraception_im": "150mg IM mỗi 12 tuần (3 tháng)",
            "adult_contraception_im_timing": "Tiêm trong vòng 5 ngày đầu của chu kỳ kinh nguyệt",
            "adult_contraception_im_postpartum": "Tiêm trong vòng 5 ngày sau sinh (nếu không cho con bú)",
            "notes": """Medroxyprogesterone là thuốc tránh thai tiêm (injectable contraception). Hiệu quả tránh thai >99%. Tiêm mỗi 12 tuần (3 tháng). Có thể gây mất kinh (amenorrhea) - không nguy hiểm. Có thể gây giảm mật độ xương (bone density) - hồi phục sau khi ngừng.""",
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "Không cần điều chỉnh đáng kể",
            "under_30": "Không cần điều chỉnh đáng kể",
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
    ],
        },
        "interactions": {
            "giảm_hiệu_quả": [
                "Thuốc cảm ứng CYP3A4 (rifampin, carbamazepine, phenytoin, St. John's Wort)"
    ],
            "tăng_nguy_cơ": [
                "Thuốc ức chế CYP3A4 (ketoconazole, ritonavir): tăng nồng độ medroxyprogesterone"
    ],
        },
"pregnancy": "X - CHỐNG CHỈ ĐỊNH nếu đã mang thai",
        "mechanism_of_action": """Medroxyprogesterone là progestin tổng hợp. Cơ chế tránh thai: (1) Ức chế rụng trứng (ovulation) - cơ chế chính, (2) Làm dày chất nhầy cổ tử cung (cervical mucus) - ngăn tinh trùng vào tử cung, (3) Làm mỏng niêm mạc tử cung (endometrium) - giảm khả năng làm tổ của trứng đã thụ tinh. Hiệu quả tránh thai >99%. Tác dụng kéo dài 12 tuần (3 tháng). ĐẶC ĐIỂM: (1) Hiệu quả tránh thai >99%, (2) Tiêm mỗi 12 tuần (3 tháng), (3) Có thể gây mất kinh (amenorrhea) - không nguy hiểm, (4) Có thể gây giảm mật độ xương - hồi phục sau khi ngừng, (5) Tăng cân phổ biến, (6) Có thể gây trầm cảm.""",
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
    ],
        },
        "pharmacokinetics": {
            "half_life": "50 ngày (dài)",
            "onset": "Ngay lập tức (ức chế rụng trứng)",
            "duration": "12 tuần (3 tháng)",
            "protein_binding": "90%",
            "metabolism": "Gan (CYP3A4)",
            "clearance": "Gan, thận (bài tiết qua nước tiểu và phân)",
        },
        "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh đông lạnh, tránh ánh sáng. Lắc kỹ trước khi tiêm.",
        "black_box_warnings": """Giảm mật độ xương (bone density loss). Có thể hồi phục sau khi ngừng. Thận trọng nếu dùng >2 năm, đặc biệt ở phụ nữ trẻ.""",
        "drug_interactions": {
            "major": [
    {
                    "drug": "Thuốc cảm ứng CYP3A4 (Rifampin, Carbamazepine, Phenytoin, St. John's Wort)",
                    "mechanism": "Cảm ứng CYP3A4, tăng chuyển hóa medroxyprogesterone",
                    "effect": "Giảm nồng độ, giảm hiệu quả tránh thai",
                    "management": "TRÁNH DÙNG CHUNG. Nếu bắt buộc, cần dùng biện pháp tránh thai bổ sung (bao cao su).",
                }
                ],
            "moderate": [],
            "minor": [],
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
    ],
        },
        "pregnancy_lactation": {
            "fda_category": "X",
            "pregnancy_details": """Medroxyprogesterone là thuốc phân loại X. CHỐNG CHỈ ĐỊNH nếu đã mang thai. Nếu mang thai khi đang dùng, ngừng ngay và tư vấn bác sĩ.""",
            "lactation": {
                "safety": "Compatible",
                "details": """Medroxyprogesterone bài tiết vào sữa mẹ ở nồng độ thấp. Không có báo cáo về tác dụng phụ đáng kể ở trẻ bú mẹ. Có thể dùng khi cho con bú sau 6 tuần.""",
                "recommendation": """Có thể dùng khi cho con bú sau 6 tuần. Nồng độ trong sữa mẹ thấp và không gây tác dụng phụ ở trẻ bú mẹ.""",
            },
        },
        "hepatic_adjustment": {
            "mild": "Không cần điều chỉnh liều",
            "moderate": "Thận trọng. Chuyển hóa qua gan có thể giảm, tăng nồng độ và nguy cơ tác dụng phụ.",
            "severe": "CHỐNG CHỈ ĐỊNH. Chuyển hóa qua gan giảm đáng kể, tăng nguy cơ bệnh gan và tác dụng phụ nặng.",
            "notes": """Medroxyprogesterone chuyển hóa qua gan. Suy gan có thể làm giảm chuyển hóa, tăng nồng độ và nguy cơ bệnh gan, tác dụng phụ nặng.""",
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
            "monitoring": "Theo dõi dấu hiệu sinh tồn, lượng máu mất, tình trạng tinh thần cho đến khi hồi phục.",
        },
        "reversal_agents": {
            "available": False,
            "agents": [],
        },
        "administration_instructions": {
            "im": {
                "reconstitution": "Lắc kỹ trước khi tiêm.",
                "injection_site": "Tiêm sâu vào cơ lớn (mông, đùi).",
                "timing": """150mg IM mỗi 12 tuần (3 tháng). Tiêm trong vòng 5 ngày đầu của chu kỳ kinh nguyệt hoặc trong vòng 5 ngày sau sinh (nếu không cho con bú).""",
                "notes": """QUAN TRỌNG: 1) Tiêm đúng lịch mỗi 12 tuần, 2) Mất kinh không nguy hiểm, nhưng cần test thai nếu nghi ngờ, 3) Giảm mật độ xương có thể hồi phục sau khi ngừng, 4) Tăng cân phổ biến, 5) Có thể gây trầm cảm.""",
            },
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
            "evidence_level": "A - Dựa trên FDA drug labels, ACOG/WHO guidelines, và dữ liệu lâm sàng từ nhiều nguồn",
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

    "Dienogest": {
        "group": "Obstetrics/Gynecology - Progestin (Endometriosis)",
        "vietnamese_name": "Dienogest, Visanne",
        "brand_names": {
            "common": ["Visanne"],
            "vietnam": ["Dienogest 2mg"]
        },
        "administration": ["PO"],
        "indications": [
            "Điều trị lạc nội mạc tử cung (endometriosis)",
            "Giảm đau do lạc nội mạc tử cung"
        ],
        "contraindications": {
            "tuyệt_đối": [
                "Dị ứng dienogest",
                "Huyết khối tĩnh mạch sâu (DVT) hoặc thuyên tắc phổi (PE) hiện tại hoặc tiền sử",
                "Bệnh tim mạch nặng (bệnh mạch vành, đột quỵ, nhồi máu cơ tim)",
                "Bệnh gan nặng (viêm gan cấp, suy gan)",
                "Ung thư phụ thuộc hormon sinh dục (ung thư vú, ung thư nội mạc tử cung)",
                "Xuất huyết âm đạo bất thường chưa rõ nguyên nhân",
                "Đã mang thai (suspected or confirmed)"
            ],
            "tương_đối": [
                "Tiền sử trầm cảm - thận trọng (có thể làm nặng)",
                "Đái tháo đường - thận trọng",
                "Loãng xương - thận trọng (có thể giảm mật độ xương)"
            ]
        },
        "dosage": {
            "adult_endometriosis": "2mg PO x 1 lần/ngày, liên tục không nghỉ",
            "notes": "Dienogest là thuốc điều trị lạc nội mạc tử cung. Uống liên tục không nghỉ. Bắt đầu vào bất kỳ ngày nào của chu kỳ kinh nguyệt. Điều trị kéo dài. Có thể gây chảy máu âm đạo bất thường hoặc vô kinh."
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
                "Tăng cân",
                "Thay đổi tâm trạng, trầm cảm",
                "Giảm ham muốn tình dục",
                "Mụn trứng cá",
                "Rụng tóc",
                "Chảy máu âm đạo bất thường (spotting, vô kinh)"
            ],
            "nghiêm_trọng": [
                "Huyết khối tĩnh mạch sâu (DVT) - hiếm",
                "Thuyên tắc phổi (PE) - hiếm",
                "Giảm mật độ xương (bone density loss) - khi dùng kéo dài"
            ]
        },
        "interactions": {
            "giảm_hiệu_quả": [
                "Thuốc cảm ứng CYP3A4 (rifampin, carbamazepine, phenytoin, St. John's Wort)"
            ],
            "tăng_nguy_cơ": [
                "Thuốc ức chế CYP3A4 (ketoconazole, ritonavir): tăng nồng độ dienogest"
            ]
        },
        "pregnancy": "X - CHỐNG CHỈ ĐỊNH nếu đã mang thai",
        "mechanism_of_action": "Dienogest là một progestin tổng hợp có tác dụng progestogenic mạnh. Cơ chế chính trong điều trị lạc nội mạc tử cung là ức chế sự phát triển của nội mạc tử cung bằng cách giảm sản xuất estrogen và gây teo các mô lạc nội mạc tử cung. Nó cũng có tác dụng chống androgen nhẹ. ĐẶC ĐIỂM: (1) Hiệu quả cao trong giảm đau do lạc nội mạc tử cung, (2) Có thể gây chảy máu âm đạo bất thường hoặc vô kinh, (3) Có thể gây giảm mật độ xương khi dùng kéo dài.",
        "monitoring": [
            "Dấu hiệu trầm cảm (thay đổi tâm trạng, mất ngủ, mệt mỏi)",
            "Chảy máu âm đạo bất thường",
            "Mật độ xương (nếu dùng kéo dài)"
        ],
        "precautions": {
            "quan_trọng": [
                "CHỐNG CHỈ ĐỊNH ở huyết khối tĩnh mạch, bệnh tim mạch nặng, ung thư phụ thuộc hormon",
                "CHỐNG CHỈ ĐỊNH ở đã mang thai hoặc đang cho con bú",
                "Có thể gây giảm mật độ xương khi dùng kéo dài - cần bổ sung calci/vitamin D",
                "Có thể gây trầm cảm - cần theo dõi sát"
            ],
            "khác": [
                "Chảy máu âm đạo bất thường hoặc vô kinh - phổ biến, thường không nguy hiểm",
                "Thận trọng ở bệnh nhân dùng thuốc cảm ứng/ức chế CYP3A4"
            ]
        },
        "pharmacokinetics": {
            "half_life": "9-10 giờ",
            "onset": "Vài tuần để đạt hiệu quả lâm sàng",
            "duration": "Dài (cần dùng liên tục)",
            "protein_binding": "90%",
            "metabolism": "Gan (CYP3A4)",
            "clearance": "Thận (bài tiết qua nước tiểu và phân)"
        },
        "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm, tránh ánh sáng.",
        "black_box_warnings": "CHỐNG CHỈ ĐỊNH ở huyết khối tĩnh mạch, bệnh tim mạch nặng, ung thư phụ thuộc hormon. CHỐNG CHỈ ĐỊNH ở đã mang thai hoặc đang cho con bú. Có thể gây giảm mật độ xương khi dùng kéo dài.",
        "drug_interactions": {
            "major": [
                {
                    "drug": "Thuốc cảm ứng CYP3A4 (Rifampin, Carbamazepine, Phenytoin, St. John's Wort)",
                    "mechanism": "Cảm ứng CYP3A4, tăng chuyển hóa dienogest",
                    "effect": "Giảm nồng độ dienogest, giảm hiệu quả điều trị lạc nội mạc tử cung",
                    "management": "TRÁNH DÙNG CHUNG. Nếu bắt buộc, cần cân nhắc thuốc khác hoặc tăng liều dienogest."
                }
            ],
            "moderate": [
                {
                    "drug": "Thuốc ức chế CYP3A4 (Ketoconazole, Ritonavir, Clarithromycin)",
                    "mechanism": "Ức chế CYP3A4, giảm chuyển hóa dienogest",
                    "effect": "Tăng nồng độ dienogest, tăng nguy cơ tác dụng phụ",
                    "management": "Thận trọng. Theo dõi tác dụng phụ. Có thể cần giảm liều dienogest."
                }
            ],
            "minor": []
        },
        "contraindications_detail": {
            "tuyệt_đối": [
                "Dị ứng dienogest",
                "Huyết khối tĩnh mạch sâu (DVT) hoặc thuyên tắc phổi (PE) hiện tại hoặc tiền sử - CHỐNG CHỈ ĐỊNH",
                "Bệnh tim mạch nặng (bệnh mạch vành, đột quỵ, nhồi máu cơ tim) - CHỐNG CHỈ ĐỊNH",
                "Bệnh gan nặng (viêm gan cấp, suy gan) - CHỐNG CHỈ ĐỊNH",
                "Ung thư phụ thuộc hormon sinh dục (ung thư vú, ung thư nội mạc tử cung) - CHỐNG CHỈ ĐỊNH",
                "Xuất huyết âm đạo bất thường chưa rõ nguyên nhân - CHỐNG CHỈ ĐỊNH",
                "Đã mang thai - CHỐNG CHỈ ĐỊNH"
            ],
            "tương_đối": [
                "Tiền sử trầm cảm - thận trọng (có thể làm nặng)",
                "Đái tháo đường - thận trọng",
                "Loãng xương - thận trọng (có thể giảm mật độ xương)"
            ]
        },
        "pregnancy_lactation": {
            "fda_category": "X",
            "pregnancy_details": "Dienogest là thuốc phân loại X. CHỐNG CHỈ ĐỊNH nếu đã mang thai. Nếu mang thai khi đang dùng, ngừng ngay và tư vấn bác sĩ.",
            "lactation": {
                "safety": "Incompatible",
                "details": "Dienogest bài tiết vào sữa mẹ. Có thể ảnh hưởng đến trẻ bú mẹ. Không dùng khi đang cho con bú.",
                "recommendation": "Không dùng khi đang cho con bú."
            }
        },
        "hepatic_adjustment": {
            "mild": "Thận trọng. Chuyển hóa qua gan có thể giảm, tăng nồng độ và nguy cơ tác dụng phụ.",
            "moderate": "CHỐNG CHỈ ĐỊNH. Chuyển hóa qua gan giảm đáng kể, tăng nguy cơ bệnh gan và tác dụng phụ nặng.",
            "severe": "CHỐNG CHỈ ĐỊNH. Chuyển hóa qua gan giảm đáng kể, tăng nguy cơ bệnh gan và tác dụng phụ nặng."
        },
        "overdose_management": {
            "symptoms": [
                "Buồn nôn, nôn",
                "Chảy máu âm đạo bất thường",
                "Đau đầu"
            ],
            "antidote": "Không có antidote đặc hiệu. Điều trị hỗ trợ.",
            "treatment": [
                "Ngừng thuốc",
                "Điều trị triệu chứng"
            ],
            "monitoring": "Theo dõi dấu hiệu sinh tồn, tình trạng chảy máu."
        },
        "reversal_agents": {
            "available": False,
            "agents": []
        },
        "administration_instructions": {
            "oral": {
                "with_food": "Uống với hoặc không thức ăn.",
                "timing": "1 viên PO x 1 lần/ngày vào cùng một thời điểm mỗi ngày.",
                "notes": "Uống liên tục không nghỉ. Nếu quên uống, uống ngay khi nhớ và tiếp tục liều tiếp theo như bình thường."
            }
        },
        "references": {
            "primary_sources": [
                "FDA Drug Label - Dienogest (Visanne)",
                "European Medicines Agency - Dienogest",
                "UpToDate - Dienogest: Drug Information",
                "Medscape - Dienogest Drug Reference"
            ],
            "last_updated": "2025-02-18",
            "evidence_level": "A - Dựa trên FDA/EMA drug labels, và dữ liệu lâm sàng từ nhiều nguồn"
        },
        "risk_flags": {
            "high_alert": False,
            "narrow_therapeutic_index": False,
            "bleeding_risk": False,
            "organ_toxicity": [],
            "qt_prolongation": False,
            "hepatotoxicity": False,
            "nephrotoxicity": False,
            "requires_monitoring": []
        },
        "guideline_tags": [
            "FDA Drug Information",
            "UpToDate Drug Information"
        ],
        "last_updated": "2025-02-18"
    },

    "Desogestrel": {
        "group": "Obstetrics/Gynecology - Progestin-Only Contraceptive",
        "vietnamese_name": "Desogestrel, Cerazette",
        "administration": ["PO"],
        "indications": [
            "Tránh thai (contraception) - progestin đơn thuần",
            "Phụ nữ không dung nạp estrogen",
            "Phụ nữ cho con bú (sau 6 tuần)",
            "Phụ nữ có chống chỉ định với estrogen"
        ],
        "contraindications": {
            "tuyệt_đối": [
                "Dị ứng desogestrel",
                "Ung thư vú hiện tại hoặc tiền sử",
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
            "adult_contraception": "0.075mg (75mcg) PO x 1 lần/ngày, liên tục không nghỉ",
            "notes": "Desogestrel là thuốc tránh thai progestin đơn thuần (progestin-only pill - POP). Uống liên tục không nghỉ. Hiệu quả tránh thai >99% nếu dùng đúng cách. Có thể gây rối loạn kinh nguyệt (không đều, mất kinh)."
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "Không cần điều chỉnh đáng kể",
            "under_30": "Không cần điều chỉnh đáng kể"
        },
        "side_effects": {
            "phổ_biến": [
                "Rối loạn kinh nguyệt (irregular bleeding, spotting) - phổ biến",
                "Mất kinh (amenorrhea) - có thể xảy ra",
                "Đau đầu",
                "Buồn nôn",
                "Tăng cân",
                "Đau vú",
                "Thay đổi tâm trạng, trầm cảm",
                "Giảm ham muốn tình dục",
                "Mụn trứng cá"
            ],
            "nghiêm_trọng": [
                "Ung thư vú - tăng nguy cơ nhẹ",
                "Huyết khối tĩnh mạch sâu (DVT) - hiếm hơn so với COC",
                "Thuyên tắc phổi (PE) - hiếm hơn so với COC",
                "Bệnh gan (viêm gan, u máu gan) - hiếm"
            ]
        },
        "interactions": {
            "giảm_hiệu_quả": [
                "Thuốc cảm ứng CYP3A4 (rifampin, carbamazepine, phenytoin, St. John's Wort)",
                "Một số kháng sinh (ampicillin, tetracycline) - dữ liệu không rõ ràng"
            ],
            "tăng_nguy_cơ": [
                "Thuốc ức chế CYP3A4 (ketoconazole, ritonavir): tăng nồng độ desogestrel"
            ]
        },
        "pregnancy": "X - CHỐNG CHỈ ĐỊNH nếu đã mang thai",
        "mechanism_of_action": "Desogestrel là progestin tổng hợp. Cơ chế tránh thai: (1) Ức chế rụng trứng (ovulation) - cơ chế chính, (2) Làm dày chất nhầy cổ tử cung (cervical mucus) - ngăn tinh trùng vào tử cung, (3) Làm mỏng niêm mạc tử cung (endometrium) - giảm khả năng làm tổ của trứng đã thụ tinh. Hiệu quả tránh thai >99% nếu dùng đúng cách. ĐẶC ĐIỂM: (1) Progestin đơn thuần - không có estrogen, (2) Uống liên tục không nghỉ, (3) Có thể gây rối loạn kinh nguyệt (không đều, mất kinh), (4) An toàn hơn COC ở một số trường hợp (cho con bú, không dung nạp estrogen), (5) Nguy cơ huyết khối thấp hơn COC.",
        "monitoring": [
            "Dấu hiệu mang thai (nếu chậm kinh >3 tháng, cần test thai)",
            "Chảy máu âm đạo bất thường",
            "Dấu hiệu trầm cảm (thay đổi tâm trạng, mất ngủ, mệt mỏi)",
            "Dấu hiệu ung thư vú (khối u vú, thay đổi da vú)",
            "Dấu hiệu huyết khối tĩnh mạch (đau chân, sưng chân, đau ngực, khó thở)"
        ],
        "precautions": {
            "quan_trọng": [
                "CHỐNG CHỈ ĐỊNH ở ung thư vú, huyết khối tĩnh mạch, bệnh gan nặng",
                "Uống đều đặn mỗi ngày vào cùng một thời điểm - QUAN TRỌNG",
                "Nếu quên uống >12 giờ - cần dùng biện pháp tránh thai bổ sung trong 7 ngày",
                "Rối loạn kinh nguyệt - phổ biến, không nguy hiểm",
                "Mất kinh - có thể xảy ra, không nguy hiểm, nhưng cần test thai nếu nghi ngờ",
                "KHÔNG bảo vệ khỏi STI - cần dùng bao cao su"
            ],
            "khác": [
                "Thận trọng ở bệnh nhân dùng thuốc cảm ứng CYP3A4 (có thể giảm hiệu quả)",
                "Thận trọng ở bệnh nhân có tiền sử trầm cảm"
            ]
        },
        "pharmacokinetics": {
            "half_life": "30-38 giờ",
            "onset": "Ngay lập tức (ức chế rụng trứng)",
            "duration": "Dài (cần dùng liên tục)",
            "protein_binding": "98%",
            "metabolism": "Gan (CYP3A4)",
            "clearance": "Gan, thận (bài tiết qua nước tiểu và phân)"
        },
        "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm, tránh ánh sáng.",
        "black_box_warnings": "Nguy cơ huyết khối tĩnh mạch (DVT, PE) - thấp hơn COC nhưng vẫn có. CHỐNG CHỈ ĐỊNH ở huyết khối tĩnh mạch, bệnh gan nặng, ung thư vú.",
        "drug_interactions": {
            "major": [
                {
                    "drug": "Thuốc cảm ứng CYP3A4 (Rifampin, Carbamazepine, Phenytoin, St. John's Wort)",
                    "mechanism": "Cảm ứng CYP3A4, tăng chuyển hóa desogestrel",
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
                "Dị ứng desogestrel",
                "Ung thư vú hiện tại hoặc tiền sử - CHỐNG CHỈ ĐỊNH",
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
            "pregnancy_details": "Desogestrel là thuốc phân loại X. CHỐNG CHỈ ĐỊNH nếu đã mang thai. Nếu mang thai khi đang dùng, ngừng ngay và tư vấn bác sĩ.",
            "lactation": {
                "safety": "Compatible",
                "details": "Desogestrel bài tiết vào sữa mẹ ở nồng độ thấp. Không có báo cáo về tác dụng phụ đáng kể ở trẻ bú mẹ. Có thể dùng khi cho con bú sau 6 tuần.",
                "recommendation": "Có thể dùng khi cho con bú sau 6 tuần. Nồng độ trong sữa mẹ thấp và không gây tác dụng phụ ở trẻ bú mẹ."
            }
        },
        "hepatic_adjustment": {
            "mild": "Không cần điều chỉnh liều",
            "moderate": "Thận trọng. Chuyển hóa qua gan có thể giảm, tăng nồng độ và nguy cơ tác dụng phụ.",
            "severe": "CHỐNG CHỈ ĐỊNH. Chuyển hóa qua gan giảm đáng kể, tăng nguy cơ bệnh gan và tác dụng phụ nặng.",
            "notes": "Desogestrel chuyển hóa qua gan (CYP3A4). Suy gan có thể làm giảm chuyển hóa, tăng nồng độ và nguy cơ bệnh gan, tác dụng phụ nặng."
        },
        "overdose_management": {
            "symptoms": [
                "Chảy máu âm đạo bất thường",
                "Chóng mặt, mệt mỏi",
                "Thay đổi tâm trạng nặng"
            ],
            "antidote": "Không có antidote đặc hiệu. Điều trị hỗ trợ.",
            "treatment": [
                "Ngừng ngay thuốc",
                "Nếu chảy máu âm đạo nặng: theo dõi lượng máu mất, điều trị hỗ trợ nếu cần",
                "Theo dõi: Dấu hiệu sinh tồn, lượng máu mất, tình trạng tinh thần"
            ],
            "monitoring": "Theo dõi dấu hiệu sinh tồn, lượng máu mất, tình trạng tinh thần cho đến khi hồi phục."
        },
        "reversal_agents": {
            "available": False,
            "agents": []
        },
        "administration_instructions": {
            "oral": {
                "with_food": "Uống với hoặc không thức ăn. Có thể uống không thức ăn.",
                "timing": "0.075mg PO x 1 lần/ngày vào cùng một thời điểm mỗi ngày. Uống liên tục không nghỉ.",
                "missed_dose": "Nếu quên uống <12 giờ: uống ngay khi nhớ, tiếp tục bình thường. Nếu quên uống >12 giờ: uống ngay khi nhớ, dùng biện pháp tránh thai bổ sung trong 7 ngày.",
                "notes": "QUAN TRỌNG: 1) Uống đều đặn mỗi ngày vào cùng một thời điểm, 2) Nếu quên uống >12 giờ, cần dùng biện pháp tránh thai bổ sung trong 7 ngày, 3) KHÔNG bảo vệ khỏi STI, 4) Rối loạn kinh nguyệt phổ biến."
            }
        },
        "references": {
            "primary_sources": [
                "FDA Drug Label - Desogestrel (Cerazette)",
                "ACOG Practice Bulletin - Progestin-Only Contraception",
                "WHO Medical Eligibility Criteria for Contraceptive Use",
                "UpToDate - Desogestrel: Drug Information"
            ],
            "last_updated": "2025-02-18",
            "evidence_level": "A - Dựa trên FDA drug labels, ACOG/WHO guidelines, và dữ liệu lâm sàng"
        },
        "risk_flags": {
            "high_alert": False,
            "narrow_therapeutic_index": False,
            "bleeding_risk": False,
            "organ_toxicity": [],
            "qt_prolongation": False,
            "hepatotoxicity": False,
            "nephrotoxicity": False,
            "requires_monitoring": []
        },
        "guideline_tags": [
            "FDA Drug Information",
            "ACOG Practice Bulletin - Progestin-Only Contraception",
            "WHO Medical Eligibility Criteria"
        ],
        "last_updated": "2025-02-18"
    },

    "Ulipristal Acetate": {
        "group": "Obstetrics/Gynecology - Emergency Contraception",
        "vietnamese_name": "Ulipristal Acetate, EllaOne",
        "administration": ["PO"],
        "indications": [
            "Tránh thai khẩn cấp (emergency contraception)",
            "Dự phòng mang thai sau quan hệ tình dục không được bảo vệ (trong vòng 120 giờ)"
        ],
        "contraindications": {
            "tuyệt_đối": [
                "Dị ứng ulipristal acetate",
                "Đã mang thai - CHỐNG CHỈ ĐỊNH (nhưng không gây sẩy thai)",
                "Suy gan nặng"
            ],
            "tương_đối": [
                "Xuất huyết âm đạo bất thường chưa rõ nguyên nhân - thận trọng",
                "Dùng với thuốc cảm ứng CYP3A4 - có thể giảm hiệu quả"
            ]
        },
        "dosage": {
            "adult_emergency_contraception": "30mg PO x 1 liều duy nhất (càng sớm càng tốt, tối đa 120 giờ sau quan hệ)",
            "notes": "Ulipristal acetate là thuốc tránh thai khẩn cấp (emergency contraception). Hiệu quả cao hơn levonorgestrel, đặc biệt trong 72-120 giờ. Hiệu quả: 95% trong 24 giờ đầu, 85% trong 120 giờ. KHÔNG gây sẩy thai nếu đã mang thai."
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "Không cần điều chỉnh đáng kể",
            "under_30": "Không cần điều chỉnh đáng kể"
        },
        "side_effects": [
            "Buồn nôn - phổ biến",
            "Đau đầu",
            "Chóng mặt",
            "Mệt mỏi",
            "Đau bụng",
            "Chảy máu âm đạo bất thường (spotting)",
            "Chậm kinh (delay menses) - có thể chậm đến 1 tuần",
            "Đau vú"
        ],
        "interactions": {
            "giảm_hiệu_quả": [
                "Thuốc cảm ứng CYP3A4 (rifampin, carbamazepine, phenytoin, St. John's Wort)",
                "Thuốc chống co giật (phenytoin, carbamazepine)"
            ],
            "tăng_nguy_cơ": [
                "Thuốc ức chế CYP3A4 (ketoconazole, ritonavir): có thể tăng nồng độ ulipristal"
            ]
        },
        "pregnancy": "X - CHỐNG CHỈ ĐỊNH nếu đã mang thai (nhưng không gây sẩy thai)",
        "mechanism_of_action": "Ulipristal acetate là selective progesterone receptor modulator (SPRM). Cơ chế tránh thai khẩn cấp: (1) Ức chế hoặc trì hoãn rụng trứng (ovulation) - cơ chế chính, (2) Làm thay đổi niêm mạc tử cung (endometrium) - giảm khả năng làm tổ của trứng đã thụ tinh. KHÔNG gây sẩy thai nếu đã mang thai (không ảnh hưởng đến thai đã làm tổ). ĐẶC ĐIỂM: (1) Hiệu quả cao hơn levonorgestrel, đặc biệt trong 72-120 giờ, (2) Hiệu quả: 95% trong 24 giờ đầu, 85% trong 120 giờ, (3) KHÔNG gây sẩy thai nếu đã mang thai, (4) Buồn nôn, đau đầu phổ biến, (5) Có thể chậm kinh đến 1 tuần.",
        "monitoring": [
            "Dấu hiệu mang thai (nếu chậm kinh >1 tuần, cần test thai)",
            "Chảy máu âm đạo bất thường"
        ],
        "precautions": {
            "quan_trọng": [
                "Hiệu quả giảm dần theo thời gian - dùng càng sớm càng tốt (tối đa 120 giờ)",
                "KHÔNG bảo vệ khỏi STI (sexually transmitted infections) - cần dùng bao cao su",
                "KHÔNG dùng như biện pháp tránh thai thường xuyên - chỉ dùng khẩn cấp",
                "Có thể chậm kinh đến 1 tuần - không lo lắng",
                "Nếu chậm kinh >1 tuần - cần test thai",
                "Thận trọng ở bệnh nhân dùng thuốc cảm ứng CYP3A4 (có thể giảm hiệu quả)"
            ]
        },
        "pharmacokinetics": {
            "half_life": "32 giờ",
            "onset": "Ngay lập tức (ức chế rụng trứng)",
            "duration": "Tác dụng ngắn (chỉ 1 liều)",
            "protein_binding": "98%",
            "metabolism": "Gan (CYP3A4)",
            "clearance": "Gan, thận (bài tiết qua nước tiểu và phân)"
        },
        "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm, tránh ánh sáng.",
        "black_box_warnings": "CHỐNG CHỈ ĐỊNH nếu đã mang thai (phân loại X). Tuy nhiên, ulipristal acetate KHÔNG gây sẩy thai nếu đã mang thai (không ảnh hưởng đến thai đã làm tổ). Chỉ hiệu quả nếu dùng trước khi thai làm tổ. Hiệu quả giảm dần theo thời gian - dùng càng sớm càng tốt (tối đa 120 giờ).",
        "drug_interactions": {
            "major": [
                {
                    "drug": "Thuốc cảm ứng CYP3A4 (Rifampin, Carbamazepine, Phenytoin, St. John's Wort)",
                    "mechanism": "Cảm ứng CYP3A4, tăng chuyển hóa ulipristal acetate",
                    "effect": "Giảm nồng độ ulipristal acetate, giảm hiệu quả tránh thai khẩn cấp",
                    "management": "Thận trọng. Có thể cần tăng liều hoặc dùng biện pháp tránh thai khác."
                }
            ],
            "moderate": [
                {
                    "drug": "Thuốc ức chế CYP3A4 (Ketoconazole, Ritonavir, Clarithromycin)",
                    "mechanism": "Ức chế CYP3A4, giảm chuyển hóa ulipristal acetate",
                    "effect": "Tăng nồng độ ulipristal acetate, tăng nguy cơ tác dụng phụ",
                    "management": "Thận trọng. Theo dõi tác dụng phụ."
                }
            ],
            "minor": []
        },
        "pregnancy_lactation": {
            "fda_category": "X",
            "pregnancy_details": "Ulipristal acetate là thuốc phân loại X. CHỐNG CHỈ ĐỊNH nếu đã mang thai. Tuy nhiên, ulipristal acetate KHÔNG gây sẩy thai nếu đã mang thai (không ảnh hưởng đến thai đã làm tổ). Ulipristal acetate chỉ hiệu quả nếu dùng trước khi thai làm tổ.",
            "lactation": {
                "safety": "Compatible with Caution",
                "details": "Ulipristal acetate bài tiết vào sữa mẹ ở nồng độ thấp. Không có báo cáo về tác dụng phụ đáng kể ở trẻ bú mẹ khi dùng liều tránh thai khẩn cấp.",
                "recommendation": "Có thể dùng khi cho con bú. Nồng độ trong sữa mẹ thấp và không gây tác dụng phụ ở trẻ bú mẹ."
            }
        },
        "hepatic_adjustment": {
            "mild": "Không cần điều chỉnh liều",
            "moderate": "Thận trọng. Chuyển hóa qua gan có thể giảm, tăng nồng độ ulipristal acetate.",
            "severe": "CHỐNG CHỈ ĐỊNH. Chuyển hóa qua gan giảm đáng kể, tăng nguy cơ tác dụng phụ nặng.",
            "notes": "Ulipristal acetate chuyển hóa qua gan (CYP3A4). Suy gan có thể làm giảm chuyển hóa, tăng nồng độ và nguy cơ tác dụng phụ."
        },
        "overdose_management": {
            "symptoms": [
                "Chảy máu âm đạo bất thường",
                "Chóng mặt, mệt mỏi"
            ],
            "antidote": "Không có antidote đặc hiệu. Điều trị hỗ trợ.",
            "treatment": [
                "Nếu chảy máu âm đạo nặng: theo dõi lượng máu mất, điều trị hỗ trợ nếu cần",
                "Theo dõi: Dấu hiệu sinh tồn, lượng máu mất"
            ],
            "monitoring": "Theo dõi dấu hiệu sinh tồn, lượng máu mất cho đến khi hồi phục."
        },
        "reversal_agents": {
            "available": False,
            "agents": []
        },
        "administration_instructions": {
            "oral": {
                "with_food": "Uống với hoặc không thức ăn. Có thể uống không thức ăn.",
                "timing": "30mg PO x 1 liều duy nhất (càng sớm càng tốt, tối đa 120 giờ sau quan hệ).",
                "notes": "QUAN TRỌNG: 1) Dùng càng sớm càng tốt (tối đa 120 giờ), 2) KHÔNG bảo vệ khỏi STI, 3) KHÔNG dùng như biện pháp tránh thai thường xuyên, 4) Có thể chậm kinh đến 1 tuần."
            }
        },
        "references": {
            "primary_sources": [
                "FDA Drug Label - Ulipristal Acetate (EllaOne)",
                "ACOG Practice Bulletin - Emergency Contraception",
                "WHO Recommendations - Emergency Contraception",
                "UpToDate - Ulipristal Acetate: Drug Information"
            ],
            "last_updated": "2025-02-18",
            "evidence_level": "A - Dựa trên FDA drug labels, ACOG/WHO guidelines, và dữ liệu lâm sàng"
        },
        "risk_flags": {
            "high_alert": False,
            "narrow_therapeutic_index": False,
            "bleeding_risk": False,
            "organ_toxicity": [],
            "qt_prolongation": False,
            "hepatotoxicity": False,
            "nephrotoxicity": False,
            "requires_monitoring": []
        },
        "guideline_tags": [
            "FDA Drug Information",
            "ACOG Practice Bulletin - Emergency Contraception",
            "WHO Recommendations"
        ],
        "last_updated": "2025-02-18"
    }

}

__all__ = ['CONTRACEPTIVES_DRUGS']
