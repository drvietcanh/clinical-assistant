"""
Emergency Obstetric Uterotonics
Includes Oxytocin for postpartum hemorrhage prevention and treatment
"""

UTEROTONICS_DRUGS = {
    "Carboprost":     {
        "group": "Emergency - Obstetric uterotonic (Prostaglandin F2-alpha)",
        "vietnamese_name": "Carboprost, Hemabate",
        "administration": [
            "IM",
            "Intrauterine"
    ],
        "indications": [
            "Điều trị băng huyết sau sinh (PPH) kháng trị với oxytocin và methylergonovine",
            "Băng huyết sau sinh do đờ tử cung nặng",
            "Sẩy thai không hoàn toàn với chảy máu nặng"
    ],
        "contraindications": {
            "tuyệt_đối": [
                "Dị ứng carboprost hoặc prostaglandin",
                "Bệnh phổi nặng (hen phế quản, COPD) - CHỐNG CHỈ ĐỊNH (nguy cơ co thắt phế quản nặng)",
                "Bệnh tim nặng - CHỐNG CHỈ ĐỊNH",
                "Tăng huyết áp nặng - CHỐNG CHỈ ĐỊNH"
    ],
            "tương_đối": [
                "Bệnh gan nặng - thận trọng (chuyển hóa qua gan)",
                "Bệnh nhân cao tuổi - tăng nhạy cảm với tác dụng phụ",
                "Dùng với thuốc tăng huyết áp - tăng nguy cơ tăng huyết áp"
    ],
        },
        "dosage": {
            "adult_pph_im": "250mcg (0.25mg) IM, lặp lại mỗi 15-90 phút nếu cần (tối đa 8 liều, tổng 2mg)",
            "adult_pph_intrauterine": "250mcg (0.25mg) tiêm trực tiếp vào cơ tử cung (khi mổ lấy thai)",
            "notes": """Thuốc mạnh nhất trong nhóm uterotonic. Dùng khi oxytocin và methylergonovine không đủ. Theo dõi huyết áp, nhịp tim, hô hấp sát. Nguy cơ co thắt phế quản.""",
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "Thận trọng",
            "under_30": "Thận trọng",
        },
        "side_effects": [
            "Co thắt phế quản (nguy hiểm, đặc biệt ở bệnh nhân hen)",
            "Tăng huyết áp",
            "Nhịp tim nhanh",
            "Buồn nôn, nôn (phổ biến)",
            "Tiêu chảy",
            "Đau đầu",
            "Sốt, ớn lạnh",
            "Đau bụng"
    ],
        "interactions": [
            "Thuốc giãn phế quản: có thể cần dùng để điều trị co thắt phế quản",
            "Thuốc tăng huyết áp: tăng nguy cơ tăng huyết áp"
    ],
        "pregnancy": "C - Chỉ dùng sau sinh",
        "mechanism_of_action": """Carboprost là prostaglandin F2-alpha (PGF2α) tổng hợp. Gắn với thụ thể prostaglandin F trên cơ tử cung, gây co tử cung mạnh và kéo dài. Carboprost là thuốc uterotonic mạnh nhất, được dùng khi oxytocin và methylergonovine không đủ để kiểm soát PPH. Cũng có tác dụng co mạch và co thắt phế quản (nguy cơ cao ở bệnh nhân hen). ĐẶC ĐIỂM: (1) Thuốc mạnh nhất trong nhóm uterotonic, (2) Nguy cơ co thắt phế quản (CHỐNG CHỈ ĐỊNH ở bệnh nhân hen/COPD), (3) Thường dùng IM hoặc tiêm trực tiếp vào cơ tử cung, (4) Theo dõi huyết áp, nhịp tim, hô hấp sát.""",
        "monitoring": [
            "Huyết áp, nhịp tim, nhịp thở liên tục (QUAN TRỌNG)",
            "Dấu hiệu co thắt phế quản (khó thở, thở khò khè, SpO2 giảm) - NGUY HIỂM",
            "Mức độ co tử cung và chảy máu",
            "Dấu hiệu sốt, ớn lạnh",
            "Dấu hiệu buồn nôn, nôn, tiêu chảy"
    ],
        "precautions": [
            "CHỐNG CHỈ ĐỊNH ở bệnh nhân hen phế quản hoặc COPD (nguy cơ co thắt phế quản nặng)",
            "CHỐNG CHỈ ĐỊNH ở bệnh nhân bệnh phổi nặng",
            "Theo dõi huyết áp, nhịp tim, hô hấp sát",
            "Chuẩn bị thuốc giãn phế quản (salbutamol, epinephrine) nếu có nguy cơ co thắt phế quản",
            "Dùng liều thấp nhất hiệu quả",
            "Thận trọng ở bệnh nhân bệnh tim, tăng huyết áp"
    ],
        "pharmacokinetics": {
            "half_life": "8 phút",
            "onset": "3-15 phút (IM)",
            "duration": "2-3 giờ",
            "protein_binding": "Không đáng kể",
            "metabolism": "Gan (chuyển hóa nhanh)",
            "clearance": "Gan, thận",
        },
        "storage": "Bảo quản trong tủ lạnh (2-8°C), tránh đông lạnh, tránh ánh sáng.",
        "black_box_warnings": """Nguy cơ co thắt phế quản nặng, có thể gây tử vong, đặc biệt ở bệnh nhân hen phế quản hoặc COPD. CHỐNG CHỈ ĐỊNH ở bệnh nhân bệnh phổi nặng. Phải theo dõi hô hấp sát và chuẩn bị thuốc giãn phế quản.""",
        "drug_interactions": {
            "major": [
    {
                    "drug": "Thuốc giãn phế quản (Salbutamol, Epinephrine)",
                    "mechanism": "Đối kháng tác dụng co thắt phế quản của carboprost",
                    "effect": "Có thể cần dùng để điều trị co thắt phế quản do carboprost",
                    "management": "Chuẩn bị sẵn thuốc giãn phế quản. Dùng ngay nếu có dấu hiệu co thắt phế quản.",
                }
                ],
            "moderate": [],
            "minor": [],
        },
        "pregnancy_lactation": {
            "fda_category": "C",
            "pregnancy_details": """Carboprost là thuốc phân loại C. CHỈ được dùng sau khi sinh (postpartum) để điều trị PPH. Không dùng trong thai kỳ (có thể gây sẩy thai, sinh non).""",
            "lactation": {
                "safety": "Compatible",
                "details": """Carboprost bài tiết vào sữa mẹ ở nồng độ rất thấp. Thời gian bán thải ngắn (8 phút). Không có báo cáo về tác dụng phụ ở trẻ bú mẹ.""",
                "recommendation": """Có thể dùng khi cho con bú. Carboprost bài tiết vào sữa mẹ ở nồng độ thấp và không gây tác dụng phụ ở trẻ bú mẹ.""",
            },
        },
        "hepatic_adjustment": {
            "mild": "Không cần điều chỉnh liều",
            "moderate": "Thận trọng. Chuyển hóa qua gan có thể giảm, nhưng thời gian bán thải ngắn (8 phút).",
            "severe": "Thận trọng. Chuyển hóa qua gan giảm, nhưng thời gian bán thải ngắn. Theo dõi sát.",
            "notes": """Carboprost chuyển hóa qua gan nhanh (thời gian bán thải 8 phút). Suy gan có thể ảnh hưởng chuyển hóa, nhưng do thời gian bán thải ngắn, ảnh hưởng thường không đáng kể.""",
        },
        "overdose_management": {
            "symptoms": [
                "Co thắt phế quản nặng (khó thở, thở khò khè, SpO2 giảm) - NGUY HIỂM",
                "Tăng huyết áp nặng",
                "Nhịp tim nhanh",
                "Buồn nôn, nôn nặng",
                "Tiêu chảy nặng",
                "Sốt cao"
    ],
            "antidote": "Không có antidote đặc hiệu. Điều trị hỗ trợ. Thuốc giãn phế quản cho co thắt phế quản.",
            "treatment": [
                "Ngừng ngay carboprost",
                "Nếu co thắt phế quản:",
                "  - Salbutamol 2.5-5mg qua nebulizer hoặc 100mcg qua MDI",
                "  - Epinephrine 0.3-0.5mg IM nếu nặng",
                "  - Thở oxy, hỗ trợ thông khí cơ học nếu cần",
                "Nếu tăng huyết áp nặng:",
                "  - Thuốc hạ huyết áp (labetalol, hydralazine) nếu cần",
                "Theo dõi: Huyết áp, nhịp tim, nhịp thở, SpO2 liên tục",
                "Hỗ trợ hô hấp: Thở oxy, nếu cần hỗ trợ thông khí cơ học"
    ],
            "monitoring": """Theo dõi huyết áp, nhịp tim, nhịp thở, SpO2 liên tục cho đến khi hồi phục. Theo dõi lâu hơn nếu có biến chứng (co thắt phế quản).""",
        },
        "reversal_agents": {
            "available": True,
            "agents": [
    {
                    "agent": "Salbutamol",
                    "mechanism": "Beta-2 agonist, giãn phế quản",
                    "indication": "Co thắt phế quản do carboprost",
                    "dose": "2.5-5mg qua nebulizer hoặc 100mcg qua MDI",
                },
    {
                    "agent": "Epinephrine",
                    "mechanism": "Alpha và beta agonist, giãn phế quản",
                    "indication": "Co thắt phế quản nặng do carboprost",
                    "dose": "0.3-0.5mg IM",
                }
                ],
            "notes": "Salbutamol và epinephrine điều trị co thắt phế quản do carboprost.",
        },
        "administration_instructions": {
            "im": {
                "reconstitution": "Dùng dung dịch sẵn có, không cần pha loãng.",
                "injection_site": "Tiêm sâu vào cơ lớn (mông, đùi).",
                "notes": """250mcg (0.25mg) IM, lặp lại mỗi 15-90 phút nếu cần (tối đa 8 liều, tổng 2mg). Theo dõi huyết áp, nhịp tim, hô hấp sát.""",
            },
            "intrauterine": {
                "reconstitution": "Dùng dung dịch sẵn có, không cần pha loãng.",
                "injection_site": "Tiêm trực tiếp vào cơ tử cung (khi mổ lấy thai).",
                "notes": "250mcg (0.25mg) tiêm trực tiếp vào cơ tử cung. Chỉ dùng khi mổ lấy thai và có chảy máu.",
            },
        },
        "references": {
            "primary_sources": [
                "FDA Drug Label - Carboprost (Hemabate)",
                "WHO Recommendations for the Prevention and Treatment of Postpartum Haemorrhage",
                "ACOG Practice Bulletin - Postpartum Hemorrhage",
                "UpToDate - Carboprost: Drug Information",
                "Medscape - Carboprost Drug Reference"
    ],
            "last_updated": "2025-02-18",
            "evidence_level": "A - Dựa trên FDA drug labels, WHO/ACOG guidelines, và dữ liệu lâm sàng từ nhiều nguồn",
        },
    },
    "Dinoprostone": {
        "group": "Emergency - Obstetric (Prostaglandin E2, Cervical ripening)",
        "vietnamese_name": "Dinoprostone, Prepidil, Cervidil",
        "administration": ["Vaginal", "Intracervical"],
        "indications": [
            "Làm mềm cổ tử cung (cervical ripening) trước khi khởi phát chuyển dạ",
            "Khởi phát chuyển dạ (induction of labor) ở phụ nữ có thai đủ tháng",
            "Sẩy thai muộn (second trimester abortion)"
        ],
        "contraindications": [
            "Dị ứng dinoprostone hoặc prostaglandin",
            "Bất tương xứng đầu chậu, ngôi bất thường",
            "Sẹo mổ cũ tử cung có nguy cơ vỡ (mổ lấy thai dọc thân, nhiều lần)",
            "Suy thai, nhau tiền đạo trung tâm, nhau bong non",
            "Bệnh phổi nặng (hen phế quản, COPD)",
            "Bệnh tim nặng",
            "Nhiễm trùng đường sinh dục nặng"
        ],
        "dosage": {
            "cervical_ripening_gel": "0.5mg dinoprostone gel đặt trong cổ tử cung, lặp lại sau 6 giờ nếu cần (tối đa 1.5mg trong 24 giờ)",
            "cervical_ripening_insert": "10mg dinoprostone insert đặt trong cổ tử cung, để 12 giờ hoặc cho đến khi bắt đầu chuyển dạ",
            "induction_of_labor": "Theo phác đồ của bệnh viện, thường bắt đầu với gel 0.5mg",
            "notes": "Chỉ dùng trong bệnh viện với monitoring sát. Theo dõi co tử cung, tim thai, huyết áp. Nguy cơ tăng co tử cung quá mức (hyperstimulation)."
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "Không cần điều chỉnh đáng kể",
            "under_30": "Không cần điều chỉnh đáng kể"
        },
        "side_effects": [
            "Tăng co tử cung quá mức (hyperstimulation) - nguy hiểm",
            "Đau bụng, đau lưng",
            "Buồn nôn, nôn",
            "Tiêu chảy",
            "Sốt, ớn lạnh",
            "Nhịp tim nhanh",
            "Co thắt phế quản (ở bệnh nhân hen)",
            "Dấu hiệu suy thai (nếu tăng co quá mức)"
        ],
        "interactions": [
            "Oxytocin: tăng nguy cơ tăng co tử cung quá mức",
            "Thuốc giãn phế quản: có thể cần dùng để điều trị co thắt phế quản"
        ],
        "pregnancy": "C - Dùng trong thai kỳ có kiểm soát",
        "mechanism_of_action": "Dinoprostone là prostaglandin E2 (PGE2). Gắn với thụ thể prostaglandin E trên cổ tử cung và cơ tử cung, gây: (1) Làm mềm cổ tử cung (cervical ripening) - tăng collagenase, giảm collagen, tăng độ đàn hồi, (2) Kích thích co tử cung nhịp nhàng. Được dùng để làm mềm cổ tử cung trước khi khởi phát chuyển dạ hoặc để khởi phát chuyển dạ. ĐẶC ĐIỂM: (1) Chủ yếu dùng cho cervical ripening, (2) Nguy cơ tăng co tử cung quá mức (hyperstimulation), (3) CHỐNG CHỈ ĐỊNH ở bệnh nhân hen/COPD (nguy cơ co thắt phế quản), (4) Chỉ dùng trong bệnh viện với monitoring sát.",
        "monitoring": [
            "Mức độ co tử cung (tần số, biên độ, thời gian co) - QUAN TRỌNG",
            "Tim thai liên tục (fetal monitoring) - QUAN TRỌNG",
            "Huyết áp, nhịp tim mẹ",
            "Dấu hiệu tăng co tử cung quá mức (hyperstimulation) - NGUY HIỂM",
            "Dấu hiệu suy thai (bất thường tim thai)",
            "Dấu hiệu co thắt phế quản (ở bệnh nhân hen)",
            "Dấu hiệu sốt, ớn lạnh"
        ],
        "precautions": [
            "CHỈ dùng trong bệnh viện với monitoring sát (co tử cung, tim thai)",
            "CHỐNG CHỈ ĐỊNH ở bệnh nhân hen phế quản hoặc COPD (nguy cơ co thắt phế quản)",
            "Theo dõi sát co tử cung để tránh tăng co quá mức (hyperstimulation)",
            "NGỪNG NGAY nếu có tăng co quá mức hoặc suy thai",
            "Thận trọng ở tiền sử mổ lấy thai, sẹo tử cung",
            "Chuẩn bị thuốc giảm co (tocolytic) nếu cần",
            "Chuẩn bị thuốc giãn phế quản nếu có nguy cơ co thắt phế quản"
        ],
        "pharmacokinetics": {
            "half_life": "2.5-5 phút (ngắn)",
            "onset": "10-30 phút (gel), 30-60 phút (insert)",
            "duration": "2-3 giờ (gel), 12 giờ (insert)",
            "protein_binding": "Không đáng kể",
            "metabolism": "Chuyển hóa nhanh ở mô (15-keto-PGE2)",
            "clearance": "Chuyển hóa ở mô, thận"
        },
        "storage": "Bảo quản trong tủ lạnh (2-8°C), tránh đông lạnh, tránh ánh sáng. Gel: dùng trong 24 giờ sau khi mở. Insert: dùng ngay sau khi mở.",
        "black_box_warnings": "Nguy cơ tăng co tử cung quá mức (hyperstimulation), suy thai, vỡ tử cung nếu dùng sai chỉ định hoặc liều. CHỈ sử dụng bởi bác sĩ có kinh nghiệm sản khoa trong môi trường bệnh viện có phương tiện hồi sức và monitoring tim thai. CHỐNG CHỈ ĐỊNH ở bệnh nhân hen phế quản hoặc COPD.",
        "drug_interactions": {
            "major": [
                {
                    "drug": "Oxytocin",
                    "mechanism": "Tác dụng cộng dồn tăng co tử cung",
                    "effect": "Tăng nguy cơ tăng co tử cung quá mức (hyperstimulation), suy thai, vỡ tử cung",
                    "management": "Dùng tuần tự, không dùng đồng thời. Chờ ít nhất 6-12 giờ sau khi lấy dinoprostone insert trước khi dùng oxytocin. Theo dõi co tử cung và tim thai sát."
                }
            ],
            "moderate": [
                {
                    "drug": "Thuốc giãn phế quản (Salbutamol, Epinephrine)",
                    "mechanism": "Đối kháng tác dụng co thắt phế quản của dinoprostone",
                    "effect": "Có thể cần dùng để điều trị co thắt phế quản do dinoprostone",
                    "management": "Chuẩn bị sẵn thuốc giãn phế quản. Dùng ngay nếu có dấu hiệu co thắt phế quản."
                }
            ],
            "minor": []
        },
        "contraindications": {
            "tuyệt_đối": [
                "Dị ứng dinoprostone hoặc prostaglandin",
                "Bất tương xứng đầu chậu chưa xử trí",
                "Ngôi ngang, ngôi bất thường chưa cho phép sinh đường âm đạo",
                "Nhau tiền đạo trung tâm, nhau bong non nặng chưa xử trí",
                "Bệnh phổi nặng (hen phế quản, COPD) - CHỐNG CHỈ ĐỊNH (nguy cơ co thắt phế quản)",
                "Bệnh tim nặng - CHỐNG CHỈ ĐỊNH",
                "Nhiễm trùng đường sinh dục nặng - CHỐNG CHỈ ĐỊNH"
            ],
            "tương_đối": [
                "Sẹo mổ lấy thai dọc thân tử cung hoặc nhiều lần",
                "Đa thai, đa ối",
                "Tiền sản giật nặng/tăng huyết áp chưa kiểm soát",
                "Suy thai - thận trọng"
            ]
        },
        "pregnancy_lactation": {
            "fda_category": "C",
            "pregnancy_details": "Dinoprostone là thuốc phân loại C. Được dùng trong thai kỳ để làm mềm cổ tử cung và khởi phát chuyển dạ, nhưng phải theo dõi sát tại bệnh viện. Nguy cơ tăng co tử cung quá mức, suy thai nếu dùng sai chỉ định hoặc liều.",
            "lactation": {
                "safety": "Compatible",
                "details": "Dinoprostone bài tiết vào sữa mẹ ở nồng độ rất thấp. Thời gian bán thải ngắn (2.5-5 phút). Không có báo cáo về tác dụng phụ ở trẻ bú mẹ.",
                "recommendation": "Có thể dùng khi cho con bú. Dinoprostone bài tiết vào sữa mẹ ở nồng độ thấp và không gây tác dụng phụ ở trẻ bú mẹ."
            }
        },
        "hepatic_adjustment": {
            "mild": "Không cần điều chỉnh liều",
            "moderate": "Không cần điều chỉnh liều",
            "severe": "Không cần điều chỉnh liều (chuyển hóa ở mô, không phụ thuộc gan)",
            "notes": "Dinoprostone chuyển hóa nhanh ở mô (thời gian bán thải 2.5-5 phút). Không cần điều chỉnh liều ở bệnh nhân suy gan."
        },
        "overdose_management": {
            "symptoms": [
                "Tăng co tử cung quá mức (hyperstimulation) - NGUY HIỂM",
                "Dấu hiệu suy thai (bất thường tim thai)",
                "Vỡ tử cung (hiếm nhưng nguy hiểm)",
                "Co thắt phế quản (ở bệnh nhân hen)",
                "Sốt cao",
                "Buồn nôn, nôn nặng"
            ],
            "antidote": "Không có antidote đặc hiệu. Điều trị hỗ trợ. Thuốc giảm co (tocolytic) cho tăng co quá mức.",
            "treatment": [
                "Lấy ngay dinoprostone insert nếu đang dùng",
                "Nếu tăng co tử cung quá mức:",
                "  - Thuốc giảm co (tocolytic): Salbutamol 2.5-5mg IV hoặc Nitroglycerin IV",
                "  - Theo dõi tim thai sát",
                "Nếu suy thai:",
                "  - Cho sản phụ nằm nghiêng trái",
                "  - Thở oxy cho mẹ",
                "  - Xử trí sản khoa (mổ lấy thai cấp cứu nếu cần)",
                "Nếu co thắt phế quản:",
                "  - Salbutamol 2.5-5mg qua nebulizer",
                "  - Thở oxy, hỗ trợ thông khí nếu cần",
                "Theo dõi: Co tử cung, tim thai, huyết áp, nhịp tim, nhịp thở liên tục"
            ],
            "monitoring": "Theo dõi co tử cung, tim thai, huyết áp, nhịp tim, nhịp thở liên tục cho đến khi hồi phục. Theo dõi lâu hơn nếu có biến chứng (tăng co quá mức, suy thai)."
        },
        "reversal_agents": {
            "available": True,
            "agents": [
                {
                    "agent": "Salbutamol",
                    "mechanism": "Beta-2 agonist, giảm co tử cung (tocolytic)",
                    "indication": "Tăng co tử cung quá mức do dinoprostone",
                    "dose": "2.5-5mg IV hoặc 100mcg qua MDI"
                },
                {
                    "agent": "Nitroglycerin",
                    "mechanism": "Giãn cơ trơn, giảm co tử cung (tocolytic)",
                    "indication": "Tăng co tử cung quá mức do dinoprostone",
                    "dose": "50-100mcg IV bolus, sau đó 10-20mcg/phút IV infusion"
                }
            ],
            "notes": "Salbutamol và nitroglycerin điều trị tăng co tử cung quá mức. Lấy dinoprostone insert ngay nếu đang dùng."
        },
        "administration_instructions": {
            "vaginal": {
                "reconstitution": "Gel: 0.5mg dinoprostone gel trong ống tiêm. Insert: 10mg dinoprostone trong màng polymer.",
                "application": "Gel: Đặt trong cổ tử cung bằng ống tiêm chuyên dụng. Insert: Đặt trong cổ tử cung, để 12 giờ hoặc cho đến khi bắt đầu chuyển dạ.",
                "notes": "QUAN TRỌNG: 1) CHỈ dùng trong bệnh viện với monitoring sát, 2) Theo dõi co tử cung và tim thai liên tục, 3) NGỪNG NGAY nếu có tăng co quá mức hoặc suy thai, 4) Lấy insert ngay nếu có tăng co quá mức."
            },
            "intracervical": {
                "reconstitution": "Gel: 0.5mg dinoprostone gel trong ống tiêm.",
                "application": "Đặt trong cổ tử cung bằng ống tiêm chuyên dụng. Lặp lại sau 6 giờ nếu cần (tối đa 1.5mg trong 24 giờ).",
                "notes": "QUAN TRỌNG: 1) CHỈ dùng trong bệnh viện với monitoring sát, 2) Theo dõi co tử cung và tim thai liên tục, 3) NGỪNG NGAY nếu có tăng co quá mức hoặc suy thai."
            }
        },
        "references": {
            "primary_sources": [
                "FDA Drug Label - Dinoprostone (Prepidil, Cervidil)",
                "ACOG Practice Bulletin - Induction of Labor",
                "WHO Recommendations for Induction of Labor",
                "UpToDate - Dinoprostone: Drug Information",
                "Medscape - Dinoprostone Drug Reference"
            ],
            "last_updated": "2025-02-18",
            "evidence_level": "A - Dựa trên FDA drug labels, ACOG/WHO guidelines, và dữ liệu lâm sàng từ nhiều nguồn"
        }
    },
    "Methylergonovine":     {
        "group": "Emergency - Obstetric uterotonic (Ergot alkaloid)",
        "vietnamese_name": "Methylergonovine, Methergine",
        "administration": [
            "PO",
            "IM",
            "IV"
    ],
        "indications": [
            "Điều trị băng huyết sau sinh (PPH) do đờ tử cung",
            "Dự phòng băng huyết sau sinh (ít dùng hơn oxytocin)",
            "Kiểm soát chảy máu sau sẩy thai hoặc nạo thai"
    ],
        "contraindications": {
            "tuyệt_đối": [
                "Dị ứng ergot alkaloid",
                "Tăng huyết áp nặng (hypertensive emergency) - CHỐNG CHỈ ĐỊNH",
                "Bệnh mạch vành - CHỐNG CHỈ ĐỊNH",
                "Bệnh mạch máu ngoại vi - CHỐNG CHỈ ĐỊNH",
                "Thai kỳ - CHỐNG CHỈ ĐỊNH (chỉ dùng sau sinh)",
                "Nhiễm trùng huyết (sepsis) - CHỐNG CHỈ ĐỊNH"
    ],
            "tương_đối": [
                "Bệnh gan nặng - thận trọng (chuyển hóa qua gan)",
                "Bệnh nhân cao tuổi - tăng nhạy cảm với tác dụng phụ",
                "Hen phế quản - thận trọng (nguy cơ co thắt phế quản)",
                "Dùng với macrolides hoặc protease inhibitors - tăng nồng độ methylergonovine"
    ],
        },
        "dosage": {
            "adult_pph_im": "0.2mg IM mỗi 2-4 giờ (tối đa 5 liều)",
            "adult_pph_po": "0.2mg PO mỗi 6-8 giờ trong 2-7 ngày",
            "adult_pph_iv": "0.2mg IV chậm trong ít nhất 60 giây (CHỈ khi cấp cứu, nguy cơ cao)",
            "notes": """KHÔNG dùng IV bolus nhanh (nguy cơ tăng huyết áp nặng, co mạch, nhồi máu cơ tim). Thường dùng IM hoặc PO. Theo dõi huyết áp sát.""",
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "Thận trọng, theo dõi huyết áp",
            "under_30": "Thận trọng, theo dõi huyết áp sát",
        },
        "side_effects": [
            "Tăng huyết áp (phổ biến, có thể nặng)",
            "Buồn nôn, nôn (phổ biến)",
            "Đau đầu",
            "Chóng mặt",
            "Co mạch ngoại vi (lạnh đầu chi, tím tái)",
            "Nhồi máu cơ tim (hiếm nhưng nguy hiểm)",
            "Co thắt phế quản (ở bệnh nhân hen)"
    ],
        "interactions": [
            "Thuốc tăng huyết áp: tăng nguy cơ tăng huyết áp nặng",
            "Macrolides (erythromycin, clarithromycin): tăng nồng độ methylergonovine",
            "Protease inhibitors: tăng nồng độ methylergonovine"
    ],
        "pregnancy": "X - Chống chỉ định trong thai kỳ (chỉ dùng sau sinh)",
        "mechanism_of_action": """Methylergonovine là ergot alkaloid. Gắn với thụ thể alpha-adrenergic và serotonin trên cơ tử cung, gây co tử cung mạnh và kéo dài. Cũng có tác dụng co mạch (alpha-adrenergic), dẫn đến tăng huyết áp. Khác với oxytocin (co tử cung nhịp nhàng), methylergonovine gây co tử cung liên tục và mạnh hơn. Được dùng để điều trị PPH khi oxytocin không đủ. ĐẶC ĐIỂM: (1) Tác dụng mạnh hơn oxytocin, (2) Nguy cơ tăng huyết áp nặng (đặc biệt khi dùng IV), (3) CHỐNG CHỈ ĐỊNH trong thai kỳ, (4) Thường dùng IM hoặc PO, tránh IV bolus nhanh.""",
        "monitoring": [
            "Huyết áp liên tục (QUAN TRỌNG) - theo dõi tăng huyết áp",
            "Mức độ co tử cung và chảy máu",
            "Dấu hiệu co mạch ngoại vi (lạnh đầu chi, tím tái)",
            "Dấu hiệu nhồi máu cơ tim (đau ngực, khó thở)",
            "Dấu hiệu co thắt phế quản (ở bệnh nhân hen)"
    ],
        "precautions": [
            "CHỐNG CHỈ ĐỊNH trong thai kỳ (chỉ dùng sau sinh)",
            "CHỐNG CHỈ ĐỊNH nếu tăng huyết áp nặng hoặc bệnh mạch máu",
            "KHÔNG dùng IV bolus nhanh (nguy cơ tăng huyết áp nặng, nhồi máu cơ tim)",
            "Theo dõi huyết áp sát (đặc biệt khi dùng IV)",
            "Thận trọng ở bệnh nhân bệnh mạch vành, bệnh mạch máu ngoại vi",
            "Thận trọng ở bệnh nhân hen phế quản (nguy cơ co thắt phế quản)",
            "Dùng liều thấp nhất hiệu quả"
    ],
        "pharmacokinetics": {
            "half_life": "0.5-2 giờ",
            "onset": "2-5 phút (IM), ngay lập tức (IV)",
            "duration": "3-4 giờ",
            "protein_binding": "Không đáng kể",
            "metabolism": "Gan (CYP3A4)",
            "clearance": "Gan, thận",
        },
        "storage": "Bảo quản ở nhiệt độ phòng (20-25°C), tránh ánh sáng, tránh ẩm.",
        "black_box_warnings": """Nguy cơ tăng huyết áp nặng, co mạch, nhồi máu cơ tim, đặc biệt khi dùng IV bolus nhanh. CHỐNG CHỈ ĐỊNH trong thai kỳ. CHỐNG CHỈ ĐỊNH nếu tăng huyết áp nặng hoặc bệnh mạch máu. Chỉ dùng sau sinh.""",
        "drug_interactions": {
            "major": [
    {
                    "drug": "Macrolides (Erythromycin, Clarithromycin, Telithromycin)",
                    "mechanism": "Ức chế CYP3A4, tăng nồng độ methylergonovine",
                    "effect": "Tăng nồng độ methylergonovine, tăng nguy cơ tăng huyết áp nặng, co mạch, nhồi máu cơ tim",
                    "management": "TRÁNH DÙNG CHUNG. Nếu bắt buộc, giảm liều methylergonovine và theo dõi huyết áp sát.",
                },
    {
                    "drug": "Protease Inhibitors (Ritonavir, Saquinavir, Indinavir)",
                    "mechanism": "Ức chế CYP3A4, tăng nồng độ methylergonovine",
                    "effect": "Tăng nồng độ methylergonovine, tăng nguy cơ tăng huyết áp nặng",
                    "management": "TRÁNH DÙNG CHUNG. Nếu bắt buộc, giảm liều methylergonovine và theo dõi huyết áp sát.",
                },
    {
                    "drug": "Thuốc tăng huyết áp khác (Norepinephrine, Phenylephrine)",
                    "mechanism": "Tác dụng tăng huyết áp cộng dồn",
                    "effect": "Tăng nguy cơ tăng huyết áp nặng, nhồi máu cơ tim, đột quỵ",
                    "management": "TRÁNH DÙNG CHUNG. Nếu bắt buộc, theo dõi huyết áp sát.",
                }
                ],
            "moderate": [],
            "minor": [],
        },
        "pregnancy_lactation": {
            "fda_category": "X",
            "pregnancy_details": """Methylergonovine là thuốc phân loại X - CHỐNG CHỈ ĐỊNH trong thai kỳ. Methylergonovine gây co tử cung mạnh, có thể gây sẩy thai, sinh non, hoặc vỡ tử cung. CHỈ được dùng sau khi sinh (postpartum).""",
            "lactation": {
                "safety": "Compatible with Caution",
                "details": """Methylergonovine bài tiết vào sữa mẹ ở nồng độ thấp. Có thể gây buồn nôn, nôn, tiêu chảy ở trẻ bú mẹ. Thời gian bán thải ngắn (0.5-2 giờ).""",
                "recommendation": """Có thể dùng khi cho con bú, nhưng thận trọng. Theo dõi trẻ bú mẹ về dấu hiệu buồn nôn, nôn, tiêu chảy.""",
            },
        },
        "hepatic_adjustment": {
            "mild": "Không cần điều chỉnh liều",
            "moderate": "Thận trọng. Chuyển hóa qua gan có thể giảm, tăng nồng độ methylergonovine. Theo dõi huyết áp sát.",
            "severe": """Thận trọng. Chuyển hóa qua gan giảm đáng kể, tăng nồng độ methylergonovine và nguy cơ tác dụng phụ. Giảm liều, theo dõi huyết áp sát.""",
            "notes": """Methylergonovine chuyển hóa qua gan (CYP3A4). Suy gan có thể làm giảm chuyển hóa, tăng nồng độ và nguy cơ tác dụng phụ. Cần thận trọng và giảm liều ở suy gan trung bình đến nặng.""",
        },
        "overdose_management": {
            "symptoms": [
                "Tăng huyết áp nặng (có thể >200/120 mmHg)",
                "Co mạch ngoại vi nặng (lạnh đầu chi, tím tái, hoại tử)",
                "Nhồi máu cơ tim",
                "Đột quỵ",
                "Co thắt phế quản (ở bệnh nhân hen)",
                "Buồn nôn, nôn nặng",
                "Co tử cung quá mức"
    ],
            "antidote": """Không có antidote đặc hiệu. Có thể dùng thuốc giãn mạch (phentolamine, nitroglycerin) để đối kháng tác dụng alpha.""",
            "treatment": [
                "Ngừng ngay methylergonovine",
                "Theo dõi ECG và huyết áp liên tục",
                "Nếu tăng huyết áp nặng:",
                "  - Phentolamine 5-10mg IV (đối kháng alpha, giảm huyết áp)",
                "  - Hoặc Nitroglycerin IV (giãn mạch, giảm huyết áp)",
                "Nếu nhồi máu cơ tim: Điều trị theo protocol nhồi máu cơ tim",
                "Nếu đột quỵ: Điều trị theo protocol đột quỵ",
                "Nếu co thắt phế quản: Salbutamol, epinephrine",
                "Hỗ trợ hô hấp: Thở oxy, nếu cần hỗ trợ thông khí cơ học",
                "Theo dõi dấu hiệu sinh tồn: Huyết áp, nhịp tim, ECG trong ít nhất 2-4 giờ"
    ],
            "monitoring": """Theo dõi ECG, huyết áp, nhịp tim liên tục trong ít nhất 2-4 giờ sau khi ngừng. Theo dõi lâu hơn nếu có biến chứng (nhồi máu cơ tim, đột quỵ).""",
        },
        "reversal_agents": {
            "available": True,
            "agents": [
    {
                    "agent": "Phentolamine",
                    "mechanism": "Alpha-blocker, đối kháng tác dụng alpha của methylergonovine (co mạch, tăng huyết áp)",
                    "indication": "Tăng huyết áp nặng do quá liều methylergonovine",
                    "dose": "5-10mg IV",
                },
    {
                    "agent": "Nitroglycerin",
                    "mechanism": "Giãn mạch, giảm huyết áp",
                    "indication": "Tăng huyết áp nặng do quá liều methylergonovine",
                    "dose": "5-10mcg/phút IV, tăng dần đến khi đạt huyết áp mục tiêu",
                }
                ],
        },
        "administration_instructions": {
            "oral": {
                "with_food": "Uống với hoặc không thức ăn. Có thể uống không thức ăn nếu cần.",
                "timing": "0.2mg PO mỗi 6-8 giờ trong 2-7 ngày. Uống đều đặn.",
                "notes": """QUAN TRỌNG: 1) CHỈ dùng sau sinh, 2) Theo dõi huyết áp sát, 3) Thường dùng IM hoặc PO, tránh IV bolus nhanh.""",
            },
            "im": {
                "reconstitution": "Dùng dung dịch sẵn có, không cần pha loãng.",
                "injection_site": "Tiêm sâu vào cơ lớn (mông, đùi).",
                "notes": "0.2mg IM mỗi 2-4 giờ (tối đa 5 liều). Hấp thu nhanh hơn PO.",
            },
            "iv": {
                "reconstitution": "Dùng dung dịch sẵn có, không cần pha loãng.",
                "infusion_rate": "0.2mg IV chậm trong ít nhất 60 giây (CHỈ khi cấp cứu, nguy cơ cao). KHÔNG dùng IV bolus nhanh.",
                "compatibility": [
                    "NS (0.9% NaCl)",
                    "D5W (5% Dextrose)"
    ],
                "incompatibility": [
                    "Không trộn với các thuốc khác. Dùng đường truyền riêng."
    ],
                "notes": """QUAN TRỌNG: 1) CHỈ dùng IV khi cấp cứu, 2) Tiêm chậm trong ít nhất 60 giây, 3) KHÔNG dùng IV bolus nhanh (nguy cơ tăng huyết áp nặng), 4) Theo dõi huyết áp sát.""",
            },
        },
        "references": {
            "primary_sources": [
                "FDA Drug Label - Methylergonovine (Methergine)",
                "WHO Recommendations for the Prevention and Treatment of Postpartum Haemorrhage",
                "ACOG Practice Bulletin - Postpartum Hemorrhage",
                "UpToDate - Methylergonovine: Drug Information",
                "Medscape - Methylergonovine Drug Reference"
    ],
            "last_updated": "2025-02-18",
            "evidence_level": "A - Dựa trên FDA drug labels, WHO/ACOG guidelines, và dữ liệu lâm sàng từ nhiều nguồn",
        },
    },
    "Oxytocin": {
        "group": "Emergency - Obstetric uterotonic (PPH prevention/treatment)",
        "vietnamese_name": "Oxytocin (Ocytocin)",
        "administration": ["IV", "IM"],
        "indications": [
            "Dự phòng băng huyết sau sinh (PPH) ngay sau sổ thai.",
            "Điều trị băng huyết sau sinh do đờ tử cung.",
            "Kích thích hoặc tăng co chuyển dạ (trong môi trường sản khoa có theo dõi sát).",
        ],
        "contraindications": [
            "Bất tương xứng đầu chậu, ngôi bất thường chưa xử trí.",
            "Sẹo mổ cũ tử cung có nguy cơ vỡ (mổ lấy thai dọc thân, nhiều lần).",
            "Suy thai, nhau tiền đạo trung tâm, nhau bong non chưa xử trí.",
            "Dị ứng với oxytocin.",
        ],
        "dosage": {
            "pph_prophylaxis_im": "10 đơn vị (IU) tiêm bắp ngay sau sổ thai.",
            "pph_prophylaxis_iv": "5–10 IU tiêm tĩnh mạch chậm (trong ít nhất 1 phút).",
            "pph_treatment_infusion": (
                "20–40 IU pha trong 1.000mL NaCl 0,9% hoặc Ringer lactate, "
                "truyền 60–120 giọt/phút (≈ 3–6 IU/giờ), chỉnh theo co tử cung và huyết động."
            ),
            "labor_induction_augmentation": (
                "Pha 5 IU trong 500mL dung dịch đẳng trương (10 mU/mL). "
                "Bắt đầu 1–2 mU/phút, tăng 1–2 mU/phút mỗi 30 phút đến khi đạt co tử cung hiệu quả "
                "(tối đa thường 20 mU/phút, theo phác đồ đơn vị)."
            ),
            "notes": "KHÔNG tiêm tĩnh mạch bolus nhanh liều cao (nguy cơ tụt huyết áp, nhịp nhanh).",
        },
        "renal_adjustment": {
            "normal": "Không cần chỉnh liều riêng.",
            "30_60": "Không cần chỉnh liều; chú ý phù, quá tải dịch do kèm truyền dịch.",
            "under_30": "Thận trọng nguy cơ quá tải dịch/hạ natri máu nếu truyền kéo dài.",
        },
        "side_effects": [
            "Buồn nôn, nôn, đỏ bừng.",
            "Hạ huyết áp thoáng qua (nhất là khi tiêm IV nhanh), nhịp tim nhanh phản xạ.",
            "Tăng co tử cung quá mức → đau, vỡ tử cung (hiếm nhưng nguy hiểm).",
            "Nước nhiều, hạ natri máu, co giật (khi truyền kéo dài liều rất cao với dung dịch nhược trương).",
        ],
        "interactions": [
            "Thuốc gây mê, thuốc giãn cơ trơn tử cung (magnesium sulfate liều cao): có thể giảm đáp ứng co tử cung.",
            "Thuốc co mạch/thuốc gây mê hít: phối hợp có thể ảnh hưởng huyết động.",
        ],
        "pregnancy": "Dùng trong thai kỳ chỉ trong bệnh viện với chỉ định rõ ràng (khởi phát/tăng co chuyển dạ).",
        "mechanism_of_action": (
            "Oxytocin là peptide hormone gắn vào thụ thể oxytocin trên cơ tử cung, "
            "hoạt hóa đường tín hiệu phospholipase C–IP3–Ca2+, làm tăng Ca2+ nội bào và gây co cơ tử cung nhịp nhàng. "
            "Ở vú, kích thích tiết sữa bằng cách co cơ biểu mô quanh nang tuyến sữa."
        ),
        "monitoring": [
            "Mức độ co tử cung (tần số, biên độ, thời gian co) và đau bụng.",
            "Mạch, huyết áp, tình trạng mất máu mẹ (PPH).",
            "Tình trạng thai (monitoring tim thai) khi dùng trong chuyển dạ.",
            "Lượng dịch vào/ra nếu truyền kéo dài, dấu hiệu quá tải dịch/hạ natri máu.",
        ],
        "precautions": [
            "Chỉ dùng tại cơ sở y tế có khả năng phẫu thuật cấp cứu và hồi sức mẹ/trẻ.",
            "Tránh truyền nhanh hoặc bolus liều cao IV (nguy cơ hạ huyết áp, loạn nhịp).",
            "Theo dõi sát co tử cung để tránh tăng co/hyperstimulation (nguy cơ vỡ tử cung, suy thai).",
            "Thận trọng ở tiền sử mổ lấy thai, sẹo tử cung, đa thai, đa ối.",
        ],
        "pharmacokinetics": {
            "half_life": "3–5 phút (ngắn).",
            "onset": "Ngay sau khi tiêm IV; 3–5 phút sau IM.",
            "duration": "Khoảng 30–60 phút sau IM; tác dụng IV phụ thuộc tốc độ truyền.",
            "protein_binding": "Thấp; bị phân hủy nhanh bởi oxytocinase.",
            "clearance": "Bị giáng hóa ở gan, thận và bởi oxytocinase nhau thai.",
        },
        "storage": (
            "Bảo quản 2–8°C (tủ lạnh), tránh ánh sáng. "
            "Một số chế phẩm ổn định ở nhiệt độ phòng trong thời gian ngắn theo hướng dẫn nhà sản xuất."
        ),
        "black_box_warnings": (
            "Nguy cơ tăng co tử cung quá mức, vỡ tử cung, rối loạn huyết động nếu dùng sai chỉ định hoặc liều. "
            "Chỉ sử dụng bởi bác sĩ có kinh nghiệm sản khoa trong môi trường bệnh viện có phương tiện hồi sức."
        ),
        "drug_interactions": {
            "major": [
                {
                    "drug": "Prostaglandin uterotonic mạnh (ví dụ carboprost)",
                    "mechanism": "Tác dụng cộng dồn tăng co tử cung.",
                    "effect": "Nguy cơ tăng co, vỡ tử cung.",
                    "management": "Dùng tuần tự, theo dõi rất sát co tử cung và huyết động.",
                }
            ],
            "moderate": [
                {
                    "drug": "Magnesium sulfate liều cao",
                    "mechanism": "Giảm co cơ tử cung, đối kháng một phần tác dụng oxytocin.",
                    "effect": "Có thể cần liều oxytocin cao hơn để đạt co hiệu quả.",
                    "management": "Điều chỉnh liều dựa trên co tử cung; không vượt liều khuyến cáo.",
                }
            ],
            "minor": [],
        },
        "contraindications_detail": {
            "tuyệt_đối": [
                "Bất tương xứng đầu chậu chưa xử trí.",
                "Ngôi ngang, ngôi bất thường chưa cho phép sinh đường âm đạo.",
                "Nhau tiền đạo trung tâm, nhau bong non nặng chưa xử trí.",
            ],
            "tương_đối": [
                "Sẹo mổ lấy thai dọc thân tử cung hoặc nhiều lần.",
                "Đa thai, đa ối.",
                "Tiền sản giật nặng/tăng huyết áp chưa kiểm soát.",
            ],
        },
        "pregnancy_lactation": {
            "fda_category": "Không phân loại – dùng có kiểm soát trong thai kỳ và sau sinh.",
            "pregnancy_details": (
                "Được dùng rộng rãi để khởi phát/tăng co chuyển dạ và dự phòng/điều trị băng huyết sau sinh, "
                "nhưng phải theo dõi sát tại bệnh viện."
            ),
            "lactation": {
                "safety": "Compatible",
                "details": "Oxytocin nội sinh là hormone tiết sữa; liều dùng sản khoa không gây hại cho trẻ bú.",
                "recommendation": "Có thể cho bú bình thường sau dùng oxytocin.",
            },
        },
        "hepatic_adjustment": {
            "mild": "Không cần chỉnh liều.",
            "moderate": "Không cần chỉnh liều; theo dõi huyết động.",
            "severe": "Dữ liệu hạn chế; dùng liều thấp nhất hiệu quả, theo dõi sát.",
            "notes": "Giáng hóa nhanh bởi oxytocinase; suy gan ít ảnh hưởng đáng kể đến thời gian bán thải.",
        },
        "overdose_management": {
            "symptoms": [
                "Tăng co tử cung kéo dài, đau dữ dội.",
                "Dấu hiệu suy thai (nếu đang chuyển dạ): bất thường tim thai.",
                "Hạ huyết áp, nhịp nhanh, quá tải dịch, hạ natri máu (truyền kéo dài liều cao).",
            ],
            "antidote": "Không có antidote đặc hiệu.",
            "treatment": [
                "Ngừng ngay oxytocin, cho sản phụ nằm nghiêng trái.",
                "Hỗ trợ hô hấp, huyết động; điều chỉnh dịch và điện giải.",
                "Nếu co tử cung quá mức, có thể dùng thuốc giảm co (tocolytic) theo phác đồ (ví dụ salbutamol, nitroglycerin).",
                "Xử trí sản khoa nếu nghi vỡ tử cung hoặc suy thai.",
            ],
            "monitoring": (
                "Theo dõi liên tục co tử cung, huyết áp, mạch, tình trạng thai (nếu còn thai), "
                "và điện giải/natri nếu truyền kéo dài với lượng dịch lớn."
            ),
        },
        "reversal_agents": None,
        "administration_instructions": {
            "iv": {
                "reconstitution": (
                    "Pha 5–10 IU oxytocin trong 500–1000mL NaCl 0,9% hoặc Ringer lactate. "
                    "KHÔNG pha với dung dịch nhược trương quá mức để tránh hạ natri máu."
                ),
                "infusion_rate": (
                    "PPH: truyền nhanh hơn ban đầu (ví dụ 120 giọt/phút) rồi giảm khi tử cung co tốt; "
                    "khởi phát chuyển dạ: bắt đầu 1–2 mU/phút, tăng dần mỗi 30 phút đến khi đạt co hiệu quả."
                ),
                "compatibility": ["NaCl 0,9%", "Ringer lactate"],
                "incompatibility": [
                    "Không pha chung với thuốc khác trong cùng dây truyền nếu chưa có dữ liệu tương hợp.",
                ],
                "notes": "Luôn dùng bơm tiêm điện hoặc dây truyền giọt đếm để kiểm soát tốc độ.",
            },
            "im": {
                "reconstitution": "Dùng dung dịch oxytocin sẵn có, không cần pha loãng.",
                "notes": "Tiêm bắp sâu 10 IU ngay sau sổ thai để dự phòng PPH khi không có đường truyền.",
            },
        },
        "references": {
            "primary_sources": [
                "WHO Recommendations for the Prevention and Treatment of Postpartum Haemorrhage",
                "FIGO/ICM guidelines on active management of third stage of labour",
                "Textbook of Obstetrics and Gynecology",
            ],
            "last_updated": "2025-02-18",
            "evidence_level": "High – guideline-based",
        },
             "reversal_agents": {
             "available": False,
             "agents": []
         },
},
    
}

__all__ = ["UTEROTONICS_DRUGS"]

