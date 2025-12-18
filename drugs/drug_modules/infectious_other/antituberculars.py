"""
Antitubercular Drugs - First-line agents for tuberculosis
"""

ANTITUBERCULAR_DRUGS = {
    "Isoniazid": {
        "group": "Infectious Disease - Antitubercular (First-line)",
        "vietnamese_name": "Isoniazid, INH",
        "administration": ["PO", "IV"],
        "indications": [
            "Điều trị lao phổi và lao ngoài phổi (phác đồ phối hợp)",
            "Điều trị lao tiềm ẩn (latent TB infection - LTBI)",
        ],
        "contraindications": [
            "Dị ứng với isoniazid",
            "Viêm gan cấp do thuốc hoặc bệnh gan tiến triển nặng",
            "Tiền sử viêm gan nặng do isoniazid",
        ],
        "dosage": {
            "adult_tb_treatment": "5mg/kg/ngày (tối đa 300mg/ngày) uống 1 lần; trong phác đồ đa thuốc",
            "adult_latent_tb": "300mg/ngày uống 1 lần trong 6–9 tháng",
            "pediatric_tb_treatment": "10–15mg/kg/ngày (tối đa 300mg/ngày) uống 1 lần",
            "notes": "Uống xa bữa ăn để tăng hấp thu; thường phối hợp pyridoxine (vitamin B6) 10–25mg/ngày để giảm nguy cơ viêm dây thần kinh ngoại biên.",
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "Không cần điều chỉnh đáng kể; theo dõi độc tính thần kinh và gan",
            "under_30": "Không cần điều chỉnh liều; có thể tăng khoảng cách liều nếu tích luỹ",
        },
        "side_effects": [
            "Tăng men gan, viêm gan do thuốc",
            "Viêm dây thần kinh ngoại biên (tê bì, dị cảm chi)",
            "Phát ban, sốt",
            "Lupus ban đỏ do thuốc (hiếm)",
        ],
        "interactions": [
            "Rifampin: tăng nguy cơ độc gan khi phối hợp",
            "Carbamazepine, phenytoin: tăng nồng độ các thuốc này (ức chế chuyển hóa)",
            "Alcohol: tăng nguy cơ độc gan",
        ],
        "pregnancy": "C – dùng được khi lợi ích vượt trội nguy cơ; thường vẫn dùng trong phác đồ lao thai kỳ.",
        # === 6 ENHANCED FIELDS CƠ BẢN ===
        "mechanism_of_action": (
            "Isoniazid là thuốc diệt khuẩn đặc hiệu với Mycobacterium tuberculosis, ức chế tổng hợp acid mycolic – "
            "thành phần quan trọng của vách tế bào trực khuẩn lao. Thuốc là tiền chất, được hoạt hóa bởi catalase-peroxidase "
            "của vi khuẩn (KatG), sau đó phức hợp hoạt hóa gắn vào enzyme InhA và KasA, làm gián đoạn tổng hợp acid mycolic, "
            "làm mất tính toàn vẹn vách tế bào và dẫn đến chết vi khuẩn, đặc biệt với vi khuẩn đang nhân lên nhanh."
        ),
        "monitoring": [
            "Men gan (ALT, AST) trước điều trị và định kỳ, đặc biệt 3 tháng đầu",
            "Triệu chứng viêm gan: mệt mỏi, chán ăn, vàng da, nước tiểu sẫm màu",
            "Triệu chứng viêm dây thần kinh ngoại biên: tê bì, dị cảm ở bàn tay/bàn chân",
            "Tuân thủ phác đồ và dấu hiệu cải thiện lâm sàng lao",
        ],
        "precautions": [
            "Không uống rượu trong quá trình điều trị (tăng nguy cơ viêm gan do thuốc).",
            "Ngừng thuốc và đánh giá lại nếu ALT/AST tăng >3 lần kèm triệu chứng hoặc >5 lần dù không triệu chứng.",
            "Bổ sung pyridoxine (vitamin B6) 10–25mg/ngày cho mọi bệnh nhân nguy cơ cao (đái tháo đường, suy dinh dưỡng, nghiện rượu, thai kỳ, HIV) để giảm nguy cơ viêm dây thần kinh ngoại biên.",
            "Thận trọng ở người cao tuổi và bệnh gan mạn; cần theo dõi men gan sát hơn.",
        ],
        "pharmacokinetics": {
            "half_life": "1–4 giờ (phụ thuộc kiểu acetyl hóa: nhanh/chậm)",
            "onset": "Nồng độ đỉnh trong 1–2 giờ sau uống",
            "duration": "Dùng 1 lần/ngày đủ hiệu quả nhờ AUC cao",
            "protein_binding": "Khoảng 10%",
            "clearance": "Gan (acetyl hóa qua NAT2), thận (thải trừ dạng chuyển hóa qua nước tiểu)",
        },
        "storage": "Bảo quản ở nhiệt độ phòng (15–30°C), tránh ẩm, tránh ánh sáng; để xa tầm tay trẻ em.",
        "black_box_warnings": (
            "Nguy cơ viêm gan nặng, đôi khi gây tử vong. Nguy cơ cao hơn ở người >35 tuổi, sử dụng rượu, bệnh gan mạn, "
            "thai kỳ hoặc sau sinh. Cần theo dõi men gan định kỳ và ngừng thuốc ngay khi có dấu hiệu viêm gan do thuốc."
        ),
        # === 8 ENHANCED FIELDS TÙY CHỌN (ĐIỀN Ở MỨC CƠ BẢN, CÓ THỂ TINH CHỈNH SAU) ===
        "drug_interactions": {
            "major": [
                {
                    "drug": "Rifampin",
                    "mechanism": "Cả hai đều chuyển hóa qua gan, phối hợp trong phác đồ HRZE làm tăng gánh nặng chuyển hóa gan.",
                    "effect": "Tăng nguy cơ viêm gan do thuốc.",
                    "management": "Theo dõi men gan sát hơn; tư vấn bệnh nhân về triệu chứng viêm gan và ngừng thuốc khi xuất hiện.",
                }
            ],
            "moderate": [
                {
                    "drug": "Phenytoin, Carbamazepine",
                    "mechanism": "Isoniazid ức chế chuyển hóa qua CYP, làm tăng nồng độ các thuốc chống động kinh.",
                    "effect": "Tăng nguy cơ độc tính thần kinh (song thị, rung giật nhãn cầu, mất điều hòa).",
                    "management": "Theo dõi nồng độ thuốc (nếu có thể) và dấu hiệu độc tính; giảm liều thuốc chống động kinh khi cần.",
                }
            ],
            "minor": [],
        },
        "contraindications_detail": {
            "tuyệt_đối": [
                "Tiền sử viêm gan nặng do isoniazid.",
                "Viêm gan cấp tiến triển.",
            ],
            "tương_đối": [
                "Bệnh gan mạn tính hoặc xơ gan.",
                "Nghiện rượu nặng.",
            ],
        },
        "pregnancy_lactation": {
            "fda_category": "C",
            "pregnancy_details": (
                "Isoniazid thường được sử dụng trong phác đồ điều trị lao khi mang thai khi lợi ích vượt trội nguy cơ. "
                "Cần bổ sung pyridoxine và theo dõi men gan sát hơn."
            ),
            "lactation": {
                "safety": "Compatible",
                "details": "Isoniazid bài tiết vào sữa mẹ với nồng độ thấp; nhìn chung an toàn với trẻ bú mẹ.",
                "recommendation": "Có thể dùng khi cho con bú, kết hợp bổ sung pyridoxine cho mẹ (và cân nhắc cho trẻ nếu cần).",
            },
        },
        "hepatic_adjustment": {
            "mild": "Có thể dùng nhưng cần theo dõi men gan định kỳ.",
            "moderate": "Thận trọng, cân nhắc liều thấp hơn hoặc theo dõi men gan thường xuyên hơn.",
            "severe": "Tránh dùng nếu có lựa chọn khác; nếu bắt buộc dùng, theo dõi rất sát và ngừng khi men gan tăng đáng kể.",
            "notes": "Chuyển hóa chủ yếu qua gan; suy gan làm tăng nguy cơ độc tính.",
        },
        "overdose_management": {
            "symptoms": [
                "Buồn nôn, nôn, chóng mặt.",
                "Co giật, hôn mê (quá liều nặng).",
                "Toan chuyển hóa, tăng đường huyết.",
            ],
            "antidote": "Pyridoxine (vitamin B6) đường tĩnh mạch liều cao trong quá liều nặng.",
            "treatment": [
                "Đảm bảo đường thở, hô hấp, tuần hoàn.",
                "Pyridoxine IV liều tương đương lượng isoniazid đã uống (gram–gram) nếu biết liều; nếu không, dùng 5g IV chậm.",
                "Điều trị co giật bằng benzodiazepine và hỗ trợ hồi sức.",
            ],
            "monitoring": "Theo dõi ý thức, dấu hiệu sinh tồn, khí máu, đường huyết và men gan.",
        },
        "reversal_agents": {
            "available": True,
            "agents": [
                {
                    "name": "Pyridoxine (Vitamin B6)",
                    "indication": "Quá liều isoniazid, co giật do thiếu vitamin B6 liên quan điều trị isoniazid.",
                    "dose": "Quá liều: liều IV tương đương lượng isoniazid đã uống; dự phòng: 10–25mg/ngày uống.",
                    "mechanism": "Phục hồi dự trữ pyridoxine cạn kiệt do isoniazid, đảo ngược độc tính thần kinh.",
                    "notes": "Nên cho dự phòng ở nhóm nguy cơ cao khi điều trị kéo dài.",
                }
            ],
        },
        "administration_instructions": {
            "oral": {
                "with_food": "Uống xa bữa ăn (trước ăn 1 giờ hoặc sau ăn 2 giờ) để tăng hấp thu; có thể uống với một ít nước.",
                "timing": "Uống 1 lần/ngày vào cùng một thời điểm (thường buổi sáng).",
            },
            "iv": {
                "reconstitution": "Pha theo hướng dẫn nhà sản xuất nếu dùng dạng IV.",
                "infusion_rate": "Truyền chậm trong 30–60 phút.",
                "compatibility": [],
                "incompatibility": [],
                "notes": "Đường IV chỉ dùng khi không thể uống; chuyển sang đường uống sớm nhất có thể.",
            },
        },
        "references": {
            "primary_sources": [
                "WHO Consolidated Guidelines on Tuberculosis Treatment",
                "CDC Guidelines for the Treatment of Latent Tuberculosis Infection",
                "Goodman & Gilman's Pharmacological Basis of Therapeutics",
            ],
            "last_updated": "2025-02-18",
            "evidence_level": "High – guideline-based with extensive clinical experience",
        },
    },

    "Rifampin": {
        "group": "Infectious Disease - Antitubercular (First-line, Rifamycin)",
        "vietnamese_name": "Rifampin, Rifampicin, Rimactan",
        "administration": ["PO", "IV"],
        "indications": [
            "Điều trị lao phổi và lao ngoài phổi (phác đồ phối hợp HRZE)",
            "Điều trị lao tiềm ẩn (phối hợp isoniazid hoặc đơn trị theo một số phác đồ)",
            "Dự phòng viêm màng não do Neisseria meningitidis hoặc Haemophilus influenzae type b",
        ],
        "contraindications": [
            "Dị ứng với rifampin hoặc các rifamycin khác (rifabutin, rifapentine)",
            "Bệnh gan tiến triển nặng",
            "Đang dùng nhiều thuốc có khoảng điều trị hẹp chuyển hóa qua CYP3A4 không thể thay thế",
        ],
        "dosage": {
            "adult_tb_treatment": "10mg/kg/ngày (thường 600mg/ngày) uống 1 lần",
            "adult_meningococcal_prophylaxis": "600mg x 2 lần/ngày x 2 ngày",
            "pediatric_tb_treatment": "10–20mg/kg/ngày (tối đa 600mg/ngày) uống 1 lần",
            "notes": "Uống xa bữa ăn để tăng hấp thu; thường phối hợp với isoniazid, pyrazinamide và ethambutol trong giai đoạn tấn công.",
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "Không cần điều chỉnh liều; theo dõi chức năng thận/gan định kỳ",
            "under_30": "Thường không cần điều chỉnh nhưng thận trọng; cân nhắc tăng khoảng cách liều ở trường hợp nặng",
        },
        "side_effects": [
            "Tăng men gan, viêm gan do thuốc",
            "Nước tiểu, nước mắt, mồ hôi, nước bọt đổi màu đỏ cam (vô hại)",
            "Rối loạn tiêu hoá (buồn nôn, đau bụng)",
            "Hội chứng giống cúm khi dùng gián đoạn liều cao",
            "Giảm tiểu cầu, thiếu máu tán huyết (hiếm, liên quan liều gián đoạn)",
        ],
        "interactions": [
            "Thuốc tránh thai đường uống: giảm hiệu lực (cảm ứng CYP3A4)",
            "Warfarin: giảm nồng độ, giảm INR",
            "Thuốc ARV (PI, NNRTI), azole, nhiều thuốc tim mạch và thần kinh: thay đổi nồng độ đáng kể",
        ],
        "pregnancy": "C – thường vẫn dùng trong phác đồ lao thai kỳ khi lợi ích vượt trội nguy cơ.",
        "mechanism_of_action": (
            "Rifampin là kháng sinh rifamycin, ức chế RNA polymerase phụ thuộc DNA của vi khuẩn "
            "bằng cách gắn vào tiểu đơn vị β, ngăn tổng hợp RNA. Thuốc có tác dụng diệt khuẩn mạnh đối với "
            "Mycobacterium tuberculosis và nhiều vi khuẩn Gram dương/Gram âm khác. Đồng thời là chất cảm ứng "
            "mạnh CYP450 (CYP3A4, 2C9, 2C19) và P‑glycoprotein, gây nhiều tương tác thuốc."
        ),
        "monitoring": [
            "Men gan (ALT, AST, bilirubin) trước và trong điều trị lao (đặc biệt khi phối hợp nhiều thuốc độc gan).",
            "Triệu chứng viêm gan: mệt mỏi, vàng da, nước tiểu sẫm màu, ngứa.",
            "Công thức máu nếu dùng liều gián đoạn hoặc có triệu chứng xuất huyết.",
            "Đánh giá tuân thủ và đáp ứng điều trị lao (triệu chứng, X-quang, đờm).",
        ],
        "precautions": [
            "Tư vấn bệnh nhân về đổi màu đỏ cam của nước tiểu, nước mắt, mồ hôi – hiện tượng lành tính.",
            "Không dùng đơn trị trong điều trị lao (nguy cơ kháng thuốc nhanh).",
            "Kiểm tra kỹ tương tác thuốc do cảm ứng CYP mạnh (ARV, thuốc tránh thai, thuốc chống động kinh, warfarin, azole...).",
            "Ngừng thuốc và đánh giá lại nếu men gan tăng đáng kể hoặc có triệu chứng viêm gan rõ.",
        ],
        "pharmacokinetics": {
            "half_life": "2–5 giờ (kéo dài ở liều cao hoặc suy gan)",
            "onset": "Nồng độ đỉnh 2–4 giờ sau uống",
            "duration": "Dùng 1 lần/ngày đủ hiệu quả nhờ hiệu ứng hậu kháng khuẩn",
            "protein_binding": "Khoảng 80%",
            "clearance": "Gan (khử acetyl, loại trừ qua mật và phân), một phần nhỏ qua thận",
        },
        "storage": "Bảo quản ở nhiệt độ phòng (15–30°C), tránh ẩm, tránh ánh sáng; đậy kín nắp chai.",
        "black_box_warnings": (
            "Có thể gây tổn thương gan nặng, đặc biệt khi phối hợp với các thuốc chống lao khác hoặc alcohol. "
            "Cần theo dõi men gan định kỳ và xử trí kịp thời khi có dấu hiệu viêm gan do thuốc."
        ),
        "drug_interactions": {
            "major": [
                {
                    "drug": "Thuốc tránh thai đường uống chứa estrogen/progestin",
                    "mechanism": "Cảm ứng CYP3A4 và P‑gp làm tăng chuyển hóa hormon.",
                    "effect": "Giảm hiệu quả tránh thai, tăng nguy cơ có thai ngoài ý muốn.",
                    "management": "Khuyến cáo dùng biện pháp tránh thai không hormon (bao cao su, dụng cụ tử cung) trong khi điều trị.",
                },
                {
                    "drug": "Thuốc ARV (protease inhibitors, NNRTIs)",
                    "mechanism": "Cảm ứng CYP mạnh làm giảm nồng độ ARV.",
                    "effect": "Giảm hiệu quả điều trị HIV, nguy cơ kháng thuốc.",
                    "management": "Cần phối hợp lựa chọn phác đồ ARV đặc biệt (tham khảo guideline HIV/TB) hoặc dùng rifabutin thay thế.",
                },
            ],
            "moderate": [
                {
                    "drug": "Warfarin",
                    "mechanism": "Cảm ứng CYP2C9 và 3A4 làm tăng chuyển hóa warfarin.",
                    "effect": "Giảm INR, giảm hiệu quả chống đông.",
                    "management": "Theo dõi INR sát và tăng liều warfarin khi bắt đầu rifampin; giảm liều khi ngừng.",
                }
            ],
            "minor": [],
        },
        "contraindications_detail": {
            "tuyệt_đối": [
                "Dị ứng với rifampin hoặc các rifamycin khác.",
                "Bệnh gan nặng tiến triển với tăng men gan rõ rệt.",
            ],
            "tương_đối": [
                "Xơ gan còn bù – cần theo dõi rất sát men gan.",
                "Dùng đồng thời nhiều thuốc có khoảng điều trị hẹp chuyển hóa qua CYP (chống động kinh, thuốc tim mạch, ARV...).",
            ],
        },
        "pregnancy_lactation": {
            "fda_category": "C",
            "pregnancy_details": (
                "Rifampin thường được sử dụng trong phác đồ điều trị lao ở thai kỳ khi cần thiết; có thể tăng nguy cơ xuất huyết sau sinh "
                "do giảm vitamin K, nên cân nhắc bổ sung vitamin K cho mẹ và trẻ sơ sinh."
            ),
            "lactation": {
                "safety": "Compatible",
                "details": "Bài tiết vào sữa ở nồng độ thấp; nhìn chung an toàn cho trẻ bú mẹ.",
                "recommendation": "Có thể dùng khi cho con bú, theo dõi vàng da hoặc triệu chứng gan ở trẻ nếu điều trị kéo dài.",
            },
        },
        "hepatic_adjustment": {
            "mild": "Có thể dùng nhưng cần theo dõi men gan mỗi 1–3 tháng.",
            "moderate": "Thận trọng; cân nhắc giảm liều hoặc kéo dài khoảng cách liều, theo dõi sát.",
            "severe": "Tránh dùng nếu có lựa chọn khác; nếu bắt buộc, theo dõi rất sát và ngừng khi có dấu hiệu suy gan tiến triển.",
            "notes": "Chuyển hóa chủ yếu tại gan; độc tính gan tăng khi phối hợp nhiều thuốc độc gan.",
        },
        "overdose_management": {
            "symptoms": [
                "Buồn nôn, nôn, đau bụng.",
                "Tăng men gan, vàng da.",
                "Lú lẫn, ngủ gà trong trường hợp nặng.",
                "Nước tiểu, nước mắt, da màu đỏ cam đậm.",
            ],
            "antidote": "Không có antidote đặc hiệu.",
            "treatment": [
                "Điều trị hỗ trợ: truyền dịch, bảo vệ đường thở.",
                "Theo dõi men gan, đông máu; điều trị suy gan nếu có.",
                "Hấp phụ than hoạt nếu bệnh nhân đến sớm sau uống quá liều.",
            ],
            "monitoring": "Theo dõi men gan, bilirubin, INR, tình trạng lâm sàng trong vài ngày.",
        },
        "reversal_agents": None,
        "administration_instructions": {
            "oral": {
                "with_food": "Uống xa bữa ăn (trước ăn 1 giờ hoặc sau ăn 2 giờ) để tối ưu hấp thu.",
                "timing": "Uống 1 lần/ngày, tốt nhất buổi sáng.",
            },
            "iv": {
                "reconstitution": "Pha bột thuốc với dung môi phù hợp rồi pha loãng trong dung dịch truyền (NS hoặc D5W).",
                "infusion_rate": "Truyền chậm trong 30–60 phút.",
                "compatibility": [],
                "incompatibility": [],
                "notes": "Dùng đường IV khi không uống được; chuyển sang đường uống sớm nhất có thể.",
            },
        },
        "references": {
            "primary_sources": [
                "WHO Consolidated Guidelines on Tuberculosis Treatment",
                "CDC Guidelines for the Treatment of Tuberculosis",
                "Goodman & Gilman's Pharmacological Basis of Therapeutics",
            ],
            "last_updated": "2025-02-18",
            "evidence_level": "High – guideline-based with extensive clinical experience",
        },
    },

    "Pyrazinamide": {
        "group": "Infectious Disease - Antitubercular (First-line)",
        "vietnamese_name": "Pyrazinamide, PZA",
        "administration": ["PO"],
        "indications": [
            "Điều trị lao phổi và lao ngoài phổi trong giai đoạn tấn công (phác đồ HRZE)",
        ],
        "contraindications": [
            "Bệnh gan cấp tiến triển hoặc viêm gan hoạt động",
            "Gout tiến triển, tăng acid uric triệu chứng nặng",
            "Dị ứng với pyrazinamide",
        ],
        "dosage": {
            "adult_tb_treatment": "20–25mg/kg/ngày uống 1 lần (tối đa khoảng 2g/ngày) phối hợp HRZE trong 2 tháng đầu",
            "pediatric_tb_treatment": "30–40mg/kg/ngày uống 1 lần (tối đa 2g/ngày)",
            "notes": "Điều chỉnh liều theo cân nặng; thường không dùng kéo dài quá giai đoạn tấn công do độc gan tăng dần.",
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "Có thể dùng liều chuẩn, theo dõi chức năng thận/gan và acid uric",
            "under_30": "Giảm tần suất dùng (ví dụ 3 lần/tuần) hoặc giảm liều; tham khảo phác đồ chuyên khoa.",
        },
        "side_effects": [
            "Tăng men gan, viêm gan do thuốc",
            "Tăng acid uric, làm nặng thêm gout",
            "Buồn nôn, nôn, chán ăn",
            "Đau khớp, đau cơ",
        ],
        "interactions": [
            "Thuốc gây độc gan khác (Rifampin, Isoniazid, rượu): tăng nguy cơ viêm gan",
            "Thuốc điều trị gout (allopurinol, colchicine, NSAID): cần điều chỉnh và theo dõi triệu chứng gout",
        ],
        "pregnancy": "C – có thể dùng trong phác đồ lao thai kỳ khi lợi ích vượt trội nguy cơ; dữ liệu còn hạn chế hơn so với isoniazid/rifampin.",
        "mechanism_of_action": (
            "Pyrazinamide là tiền chất, được chuyển hóa trong trực khuẩn lao thành pyrazinoic acid. "
            "Dạng hoạt tính này làm giảm pH nội bào và can thiệp vào chức năng màng và chuyển hóa năng lượng của Mycobacterium tuberculosis, "
            "đặc biệt hiệu quả trên vi khuẩn lao đang tồn tại trong môi trường toan (ổ viêm, đại thực bào). Thuốc giúp rút ngắn thời gian điều trị tổng thể."
        ),
        "monitoring": [
            "Men gan (ALT, AST) trước điều trị và định kỳ trong giai đoạn dùng PZA.",
            "Acid uric máu, đặc biệt ở bệnh nhân có tiền sử gout.",
            "Triệu chứng viêm gan: mệt mỏi, vàng da, chán ăn.",
            "Đau khớp, đau cơ, biểu hiện gout cấp.",
        ],
        "precautions": [
            "Thận trọng ở bệnh nhân bệnh gan mạn hoặc tiền sử viêm gan do thuốc.",
            "Theo dõi acid uric và triệu chứng gout; cân nhắc điều trị dự phòng ở bệnh nhân gout.",
            "Ngừng thuốc nếu men gan tăng đáng kể hoặc có viêm gan lâm sàng rõ.",
        ],
        "pharmacokinetics": {
            "half_life": "8–11 giờ (kéo dài khi suy thận)",
            "onset": "Đạt nồng độ đỉnh trong 2 giờ sau uống",
            "duration": "Dùng 1 lần/ngày đủ duy trì hiệu quả",
            "protein_binding": "Khoảng 10–20%",
            "clearance": "Chuyển hóa chủ yếu qua gan, thải trừ qua thận (dạng chuyển hóa).",
        },
        "storage": "Bảo quản nơi khô mát, tránh ánh sáng, nhiệt độ 15–30°C.",
        "black_box_warnings": (
            "Có thể gây viêm gan nặng; nguy cơ tăng khi phối hợp với các thuốc chống lao khác. "
            "Theo dõi men gan định kỳ và ngừng thuốc khi có bằng chứng tổn thương gan đáng kể."
        ),
        "drug_interactions": {
            "major": [
                {
                    "drug": "Thuốc độc gan khác (Rifampin, Isoniazid, alcohol)",
                    "mechanism": "Tăng gánh nặng chuyển hóa gan.",
                    "effect": "Tăng nguy cơ viêm gan do thuốc.",
                    "management": "Theo dõi men gan sát; tư vấn tránh rượu.",
                }
            ],
            "moderate": [
                {
                    "drug": "Thuốc điều trị gout",
                    "mechanism": "Tăng acid uric có thể làm tăng nhu cầu điều trị gout.",
                    "effect": "Khó kiểm soát cơn gout.",
                    "management": "Theo dõi triệu chứng và điều chỉnh liều thuốc gout khi cần.",
                }
            ],
            "minor": [],
        },
        "contraindications_detail": {
            "tuyệt_đối": [
                "Viêm gan cấp hoạt động.",
                "Tiền sử viêm gan nặng do pyrazinamide.",
            ],
            "tương_đối": [
                "Bệnh gan mạn tính.",
                "Gout hoặc tăng acid uric mạn tính.",
            ],
        },
        "pregnancy_lactation": {
            "fda_category": "C",
            "pregnancy_details": (
                "Có thể được sử dụng trong một số phác đồ điều trị lao khi cần thiết; dữ liệu an toàn còn hạn chế, nên cân nhắc lợi ích–nguy cơ."
            ),
            "lactation": {
                "safety": "Caution",
                "details": "Bài tiết vào sữa với lượng nhỏ; nhìn chung ít dữ liệu.",
                "recommendation": "Có thể dùng kèm theo dõi trẻ; cân nhắc lợi ích điều trị cho mẹ.",
            },
        },
        "hepatic_adjustment": {
            "mild": "Có thể dùng nhưng theo dõi men gan sát.",
            "moderate": "Cân nhắc tránh nếu có lựa chọn khác; nếu dùng, cần giám sát chặt chẽ.",
            "severe": "Thường tránh dùng.",
            "notes": "Pyrazinamide có độc tính gan đáng kể; cần đặc biệt thận trọng trong suy gan.",
        },
        "overdose_management": {
            "symptoms": [
                "Buồn nôn, nôn, đau bụng.",
                "Tăng men gan, vàng da.",
                "Tăng acid uric, đau khớp.",
            ],
            "antidote": "Không có antidote đặc hiệu.",
            "treatment": [
                "Điều trị hỗ trợ, bù dịch, theo dõi chức năng gan.",
                "Điều trị gout cấp nếu có (NSAID, colchicine phù hợp).",
            ],
            "monitoring": "Theo dõi men gan, acid uric, triệu chứng lâm sàng.",
        },
        "reversal_agents": None,
        "administration_instructions": {
            "oral": {
                "with_food": "Uống xa bữa ăn nếu dung nạp được để tối ưu hấp thu; có thể uống cùng thức ăn nếu kích ứng dạ dày.",
                "timing": "Uống 1 lần/ngày cùng các thuốc chống lao khác trong phác đồ.",
            },
        },
        "references": {
            "primary_sources": [
                "WHO Consolidated Guidelines on Tuberculosis Treatment",
                "CDC Guidelines for the Treatment of Tuberculosis",
            ],
            "last_updated": "2025-02-18",
            "evidence_level": "High – guideline-based",
        },
    },

    "Ethambutol": {
        "group": "Infectious Disease - Antitubercular (First-line)",
        "vietnamese_name": "Ethambutol, EMB",
        "administration": ["PO"],
        "indications": [
            "Điều trị lao phổi và lao ngoài phổi trong phác đồ phối hợp HRZE.",
            "Điều trị một số nhiễm Mycobacterium không điển hình (kết hợp thuốc khác).",
        ],
        "contraindications": [
            "Viêm thần kinh thị giác (optic neuritis) đang hoạt động.",
            "Không đánh giá được thị lực, phân biệt màu (trẻ quá nhỏ không hợp tác).",
            "Dị ứng với ethambutol.",
        ],
        "dosage": {
            "adult_tb_treatment": "15–20mg/kg/ngày uống 1 lần (giai đoạn tấn công), có thể 3 lần/tuần trong phác đồ rút gọn.",
            "pediatric_tb_treatment": "15–25mg/kg/ngày uống 1 lần.",
            "notes": "Điều chỉnh liều theo chức năng thận; cần tính liều theo cân nặng thực.",
        },
        "renal_adjustment": {
            "normal": "Không đổi.",
            "30_60": "Giảm liều hoặc kéo dài khoảng cách liều (ví dụ 15mg/kg mỗi 24–36 giờ).",
            "under_30": "Giảm liều đáng kể hoặc dùng giãn cách (3 lần/tuần); tham khảo phác đồ chuyên khoa.",
        },
        "side_effects": [
            "Rối loạn thị giác: giảm thị lực, khó phân biệt màu đỏ–xanh (optic neuritis).",
            "Phát ban, sốt.",
            "Đau khớp, rối loạn tiêu hóa nhẹ.",
        ],
        "interactions": [
            "Ít tương tác qua CYP; chủ yếu cần lưu ý với các thuốc ảnh hưởng thị lực khác.",
        ],
        "pregnancy": "B – thường được xem là tương đối an toàn trong thai kỳ khi cần thiết.",
        "mechanism_of_action": (
            "Ethambutol ức chế enzyme arabinosyl transferase của Mycobacterium, "
            "ngăn tổng hợp arabinogalactan – một thành phần quan trọng của vách tế bào vi khuẩn. "
            "Điều này làm suy yếu vách tế bào và tăng tính thấm với các thuốc chống lao khác, giúp tăng hiệu lực phối hợp."
        ),
        "monitoring": [
            "Khám mắt cơ bản (thị lực, phân biệt màu đỏ–xanh) trước khi bắt đầu điều trị dài ngày.",
            "Hỏi bệnh nhân về thay đổi thị lực (mờ mắt, nhìn mờ màu, nhìn tối) mỗi tháng.",
            "Chức năng thận (creatinin, eGFR) để điều chỉnh liều.",
        ],
        "precautions": [
            "Ngừng thuốc ngay nếu nghi ngờ viêm thần kinh thị giác; tham vấn chuyên khoa mắt.",
            "Thận trọng ở bệnh nhân suy thận (cần điều chỉnh liều).",
            "Theo dõi thị lực đặc biệt cẩn thận nếu dùng kéo dài >2–3 tháng.",
        ],
        "pharmacokinetics": {
            "half_life": "3–4 giờ (kéo dài khi suy thận).",
            "onset": "Hấp thu tốt qua đường uống, nồng độ đỉnh trong 2–4 giờ.",
            "duration": "Dùng 1 lần/ngày đủ hiệu quả; có thể dùng liều giãn cách theo phác đồ.",
            "protein_binding": "Khoảng 20–30%.",
            "clearance": "Chủ yếu thải trừ qua thận dưới dạng không chuyển hóa.",
        },
        "storage": "Bảo quản nơi khô mát, tránh ánh sáng, 15–30°C.",
        "black_box_warnings": (
            "Nguy cơ viêm thần kinh thị giác có thể không hồi phục nếu không phát hiện sớm; cần theo dõi thị lực định kỳ."
        ),
        "drug_interactions": {
            "major": [],
            "moderate": [],
            "minor": [],
        },
        "contraindications_detail": {
            "tuyệt_đối": [
                "Viêm thần kinh thị giác đang hoạt động.",
            ],
            "tương_đối": [
                "Suy thận trung bình–nặng.",
                "Bệnh mắt nền sẵn có (glaucoma, bệnh võng mạc) – cần theo dõi kỹ.",
            ],
        },
        "pregnancy_lactation": {
            "fda_category": "B",
            "pregnancy_details": (
                "Dữ liệu cho thấy không tăng rõ dị tật bẩm sinh; được xem là có thể dùng trong thai kỳ khi cần phối hợp điều trị lao."
            ),
            "lactation": {
                "safety": "Compatible",
                "details": "Bài tiết vào sữa với nồng độ thấp; ít nguy cơ cho trẻ.",
                "recommendation": "Có thể dùng khi cho con bú; theo dõi thị lực trẻ sơ sinh nếu dùng kéo dài.",
            },
        },
        "hepatic_adjustment": {
            "mild": "Thường không cần điều chỉnh; theo dõi men gan nếu phối hợp nhiều thuốc độc gan.",
            "moderate": "Thận trọng do phối hợp với các thuốc độc gan khác trong phác đồ.",
            "severe": "Cân nhắc lợi ích–nguy cơ; ưu tiên điều chỉnh các thuốc độc gan khác hơn là ethambutol.",
            "notes": "Chủ yếu thải qua thận; suy gan ảnh hưởng ít hơn suy thận.",
        },
        "overdose_management": {
            "symptoms": [
                "Rối loạn thị giác cấp: mờ mắt, mất thị lực tạm thời.",
                "Buồn nôn, nôn, chóng mặt.",
            ],
            "antidote": "Không có antidote đặc hiệu.",
            "treatment": [
                "Ngừng thuốc ngay.",
                "Điều trị hỗ trợ; tham vấn chuyên khoa mắt.",
            ],
            "monitoring": "Theo dõi thị lực, thị trường, màu sắc; chức năng thận.",
        },
        "reversal_agents": None,
        "administration_instructions": {
            "oral": {
                "with_food": "Có thể uống cùng hoặc xa bữa ăn; uống với nước.",
                "timing": "Uống 1 lần/ngày cùng các thuốc chống lao khác.",
            },
        },
        "references": {
            "primary_sources": [
                "WHO Consolidated Guidelines on Tuberculosis Treatment",
                "CDC Guidelines for the Treatment of Tuberculosis",
            ],
            "last_updated": "2025-02-18",
            "evidence_level": "High – guideline-based",
        },
    },

    "Streptomycin": {
        "group": "Infectious Disease - Antitubercular (Injectable aminoglycoside, second-line in many regimens)",
        "vietnamese_name": "Streptomycin",
        "administration": ["IM", "IV"],
        "indications": [
            "Điều trị lao trong một số phác đồ đặc biệt (lao kháng thuốc, thất bại điều trị, không dung nạp thuốc khác).",
            "Nhiễm vi khuẩn Gram âm và Gram dương nhạy cảm trong các chỉ định hạn chế (ít dùng do độc tai/thận).",
        ],
        "contraindications": [
            "Quá mẫn với streptomycin hoặc các aminoglycoside khác.",
            "Suy thận nặng không kiểm soát được.",
            "Rối loạn dẫn truyền thần kinh–cơ (như nhược cơ).",
        ],
        "dosage": {
            "adult_tb_treatment": "15mg/kg/ngày (tối đa khoảng 1g/ngày) tiêm bắp, thường dùng 5–7 ngày/tuần tùy phác đồ.",
            "pediatric_tb_treatment": "15–20mg/kg/ngày (tối đa 1g/ngày) tiêm bắp.",
            "notes": "Điều chỉnh liều theo chức năng thận và tuổi; tránh dùng kéo dài do nguy cơ độc tai/thận không hồi phục.",
        },
        "renal_adjustment": {
            "normal": "Có thể dùng liều chuẩn 1 lần/ngày.",
            "30_60": "Giảm tần suất hoặc liều; ví dụ 15mg/kg mỗi 24–48 giờ, theo dõi nồng độ thuốc nếu có.",
            "under_30": "Giảm liều rõ rệt hoặc kéo dài khoảng cách (2–3 lần/tuần); cần tham khảo phác đồ chuyên khoa và theo dõi sát chức năng thận/ống tai.",
        },
        "side_effects": [
            "Độc tai (tổn thương ốc tai, tiền đình): chóng mặt, ù tai, giảm thính lực, mất thăng bằng.",
            "Độc thận (tổn thương ống thận): tăng creatinin, giảm eGFR.",
            "Phản ứng tại chỗ tiêm: đau, sưng.",
            "Phản vệ (hiếm).",
        ],
        "interactions": [
            "Thuốc độc tai khác (furosemid IV liều cao, cisplatin): tăng nguy cơ mất thính lực.",
            "Thuốc độc thận khác (vancomycin, amphotericin B, NSAID): tăng nguy cơ suy thận.",
            "Thuốc gây ức chế dẫn truyền thần kinh–cơ: tăng nguy cơ yếu cơ, suy hô hấp.",
        ],
        "pregnancy": "D – có nguy cơ gây độc tai cho thai nhi; thường tránh dùng trong thai kỳ trừ khi không còn lựa chọn khác.",
        "mechanism_of_action": (
            "Streptomycin là kháng sinh aminoglycoside, gắn không hồi phục vào tiểu đơn vị 30S ribosome của vi khuẩn, "
            "làm sai lệch quá trình đọc mã mRNA và ức chế tổng hợp protein, dẫn đến tác dụng diệt khuẩn. "
            "Thuốc có hoạt tính với Mycobacterium tuberculosis và nhiều vi khuẩn Gram âm hiếu khí."
        ),
        "monitoring": [
            "Creatinin huyết thanh, eGFR trước và định kỳ trong điều trị.",
            "Thính lực (đánh giá thính lực đồ nếu có thể) và hỏi bệnh về ù tai, giảm nghe, chóng mặt.",
            "Dấu hiệu rối loạn thăng bằng, choáng váng, đi loạng choạng.",
        ],
        "precautions": [
            "Tránh dùng phối hợp kéo dài với các thuốc độc tai/thận khác nếu có thể.",
            "Giới hạn thời gian điều trị; dùng liều 1 lần/ngày có thể giảm độc tính so với chia nhiều lần.",
            "Điều chỉnh liều ở bệnh nhân cao tuổi, suy thận, suy dinh dưỡng.",
        ],
        "pharmacokinetics": {
            "half_life": "2–4 giờ (kéo dài đáng kể khi suy thận).",
            "onset": "Nồng độ đỉnh huyết tương đạt nhanh sau tiêm bắp (1–2 giờ).",
            "duration": "Hiệu quả phụ thuộc nồng độ đỉnh (Cmax/MIC) và hiệu ứng hậu kháng sinh.",
            "protein_binding": "Khoảng 30%.",
            "clearance": "Thải trừ chủ yếu qua thận ở dạng không chuyển hóa.",
        },
        "storage": "Bảo quản bột thuốc ở nơi khô mát; dung dịch đã pha dùng trong thời gian khuyến cáo của nhà sản xuất.",
        "black_box_warnings": (
            "Nguy cơ độc tai (có thể không hồi phục) và độc thận, đặc biệt khi dùng kéo dài, liều cao hoặc bệnh nhân suy thận. "
            "Cần theo dõi chức năng thận và thính lực định kỳ."
        ),
        "drug_interactions": {
            "major": [
                {
                    "drug": "Furosemid liều cao đường IV, các thuốc lợi tiểu quai khác",
                    "mechanism": "Tăng độc tính trên ốc tai.",
                    "effect": "Tăng nguy cơ giảm thính lực không hồi phục.",
                    "management": "Hạn chế phối hợp; nếu bắt buộc, theo dõi thính lực sát.",
                },
                {
                    "drug": "Vancomycin, amphotericin B, các thuốc độc thận khác",
                    "mechanism": "Tăng tổn thương ống thận.",
                    "effect": "Tăng nguy cơ suy thận cấp.",
                    "management": "Theo dõi creatinin thường xuyên; cân nhắc giảm liều hoặc thay thế thuốc.",
                },
            ],
            "moderate": [
                {
                    "drug": "Thuốc giãn cơ, thuốc gây mê",
                    "mechanism": "Tăng ức chế dẫn truyền thần kinh–cơ.",
                    "effect": "Tăng nguy cơ yếu cơ, suy hô hấp trong và sau phẫu thuật.",
                    "management": "Thông báo cho bác sĩ gây mê; theo dõi sát hô hấp.",
                }
            ],
            "minor": [],
        },
        "contraindications_detail": {
            "tuyệt_đối": [
                "Quá mẫn nặng với aminoglycoside.",
                "Nhược cơ nặng.",
            ],
            "tương_đối": [
                "Suy thận trung bình–nặng.",
                "Tiền sử giảm thính lực hoặc bệnh tai trong.",
                "Người cao tuổi, suy dinh dưỡng.",
            ],
        },
        "pregnancy_lactation": {
            "fda_category": "D",
            "pregnancy_details": (
                "Có báo cáo gây điếc bẩm sinh cho thai nhi khi mẹ dùng streptomycin; chỉ dùng khi đe dọa tính mạng và không còn lựa chọn an toàn hơn."
            ),
            "lactation": {
                "safety": "Caution",
                "details": "Bài tiết một lượng nhỏ vào sữa; hấp thu đường tiêu hóa của trẻ kém nhưng dữ liệu còn hạn chế.",
                "recommendation": "Có thể tiếp tục cho bú nếu thật cần thiết cho mẹ, nhưng ưu tiên thuốc khác nếu có thể.",
            },
        },
        "hepatic_adjustment": {
            "mild": "Không cần điều chỉnh đáng kể; chủ yếu điều chỉnh theo chức năng thận.",
            "moderate": "Không cần chỉnh liều riêng, nhưng cân nhắc toàn bộ phác đồ.",
            "severe": "Tác động hạn chế; vẫn ưu tiên chỉnh theo chức năng thận.",
            "notes": "Thải trừ chủ yếu qua thận; suy gan ít ảnh hưởng đến dược động học.",
        },
        "overdose_management": {
            "symptoms": [
                "Yếu cơ, liệt cơ hô hấp.",
                "Giảm thính lực cấp, ù tai, chóng mặt.",
                "Suy thận cấp.",
            ],
            "antidote": "Không có antidote đặc hiệu; có thể dùng hỗ trợ hô hấp và lọc máu.",
            "treatment": [
                "Ngừng thuốc ngay lập tức.",
                "Hỗ trợ hô hấp, có thể cần thở máy nếu suy hô hấp.",
                "Lọc máu (hemodialysis) để loại bỏ thuốc trong suy thận.",
            ],
            "monitoring": "Theo dõi chặt chẽ chức năng thận, thính lực và tình trạng hô hấp.",
        },
        "reversal_agents": None,
        "administration_instructions": {
            "im": {
                "site": "Tiêm bắp sâu vùng mông hoặc đùi.",
                "notes": "Thay đổi vị trí tiêm để giảm đau và tổn thương mô.",
            },
            "iv": {
                "reconstitution": "Pha bột thuốc với dung môi thích hợp rồi pha loãng trong dung dịch truyền.",
                "infusion_rate": "Truyền chậm trong 30–60 phút.",
                "notes": "Theo dõi phản ứng tại chỗ và toàn thân trong lúc truyền.",
            },
        },
        "references": {
            "primary_sources": [
                "WHO Guidelines for the Programmatic Management of Drug-resistant Tuberculosis",
                "CDC Guidelines for the Treatment of Tuberculosis",
            ],
            "last_updated": "2025-02-18",
            "evidence_level": "High – guideline-based, nhưng hiện ít dùng do độc tính.",
        },
    },

    "Rifabutin": {
        "group": "Infectious Disease - Antitubercular (Rifamycin, dùng trong HIV/TB và các phác đồ đặc biệt)",
        "vietnamese_name": "Rifabutin",
        "administration": ["PO"],
        "indications": [
            "Điều trị lao ở bệnh nhân HIV đang dùng phác đồ ARV có tương tác mạnh với rifampin.",
            "Dự phòng và điều trị nhiễm Mycobacterium avium complex (MAC) ở bệnh nhân suy giảm miễn dịch nặng.",
        ],
        "contraindications": [
            "Dị ứng với rifabutin hoặc các rifamycin khác.",
            "Bệnh gan nặng tiến triển.",
        ],
        "dosage": {
            "adult_tb_hiv": "300mg/ngày uống 1 lần; điều chỉnh xuống 150mg/ngày khi dùng kèm một số PI/NNRTI (theo guideline HIV/TB).",
            "mac_prophylaxis": "300mg/ngày uống 1 lần cho bệnh nhân HIV với CD4 <50 tế bào/mm³.",
            "notes": "Liều chính xác phụ thuộc phác đồ ARV đi kèm; cần tham khảo guideline HIV/TB cập nhật.",
        },
        "renal_adjustment": {
            "normal": "Không cần điều chỉnh.",
            "30_60": "Thường không cần điều chỉnh; theo dõi thêm độc tính.",
            "under_30": "Thận trọng, có thể phải giảm liều hoặc kéo dài khoảng cách; tham khảo tài liệu chuyên sâu.",
        },
        "side_effects": [
            "Đổi màu nước tiểu, nước mắt, mồ hôi sang vàng–cam.",
            "Viêm màng bồ đào (uveitis), đặc biệt khi dùng liều cao hoặc phối hợp với clarithromycin, fluconazole.",
            "Giảm bạch cầu, giảm tiểu cầu.",
            "Tăng men gan.",
        ],
        "interactions": [
            "Thuốc ARV (PI, NNRTI): tương tác phức tạp (vừa là cơ chất, vừa cảm ứng/ức chế CYP).",
            "Clarithromycin, azole (fluconazole): tăng nồng độ rifabutin, tăng nguy cơ uveitis và độc tính.",
        ],
        "pregnancy": "B–C (dữ liệu hạn chế); chỉ dùng khi lợi ích vượt trội nguy cơ.",
        "mechanism_of_action": (
            "Rifabutin là rifamycin, ức chế RNA polymerase phụ thuộc DNA của vi khuẩn bằng cách gắn vào tiểu đơn vị β, "
            "ngăn tổng hợp RNA và có tác dụng diệt khuẩn đối với Mycobacterium tuberculosis và một số Mycobacterium không điển hình "
            "(như MAC). So với rifampin, rifabutin là cảm ứng CYP3A4 yếu hơn, do đó thích hợp hơn cho bệnh nhân HIV dùng ARV."
        ),
        "monitoring": [
            "Men gan (ALT, AST, bilirubin) định kỳ.",
            "Công thức máu (bạch cầu, tiểu cầu).",
            "Triệu chứng mắt: mờ mắt, đau mắt, nhạy sáng (nghi uveitis).",
            "Theo dõi tương tác với phác đồ ARV (tải lượng virus, CD4).",
        ],
        "precautions": [
            "Thận trọng khi phối hợp với clarithromycin hoặc azole (tăng nguy cơ uveitis).",
            "Điều chỉnh liều theo guideline HIV/TB khi phối hợp với PI/NNRTI.",
            "Tư vấn bệnh nhân về đổi màu dịch cơ thể tương tự rifampin.",
        ],
        "pharmacokinetics": {
            "half_life": "30–40 giờ (dài hơn rifampin).",
            "onset": "Nồng độ đỉnh sau 2–4 giờ uống.",
            "duration": "Cho phép dùng 1 lần/ngày hoặc 3 lần/tuần tùy phác đồ.",
            "protein_binding": "Khoảng 70%.",
            "clearance": "Chủ yếu qua gan; bài tiết qua mật và phân, một phần nhỏ qua thận.",
        },
        "storage": "Bảo quản nơi khô mát, tránh ánh sáng, 15–30°C.",
        "black_box_warnings": (
            "Có thể gây viêm màng bồ đào, giảm bạch cầu, giảm tiểu cầu và độc gan; cần theo dõi sát, đặc biệt khi phối hợp clarithromycin hoặc azole."
        ),
        "drug_interactions": {
            "major": [
                {
                    "drug": "Protease inhibitors (PI), NNRTI",
                    "mechanism": "Ảnh hưởng lẫn nhau qua CYP3A4 (rifabutin là cơ chất và cảm ứng nhẹ).",
                    "effect": "Thay đổi nồng độ cả ARV và rifabutin.",
                    "management": "Điều chỉnh liều rifabutin (thường giảm còn 150mg/ngày hoặc 3 lần/tuần) theo guideline HIV/TB.",
                },
                {
                    "drug": "Clarithromycin, fluconazole",
                    "mechanism": "Ức chế chuyển hóa rifabutin.",
                    "effect": "Tăng nguy cơ uveitis, độc tính toàn thân.",
                    "management": "Theo dõi sát triệu chứng mắt và độc tính; cân nhắc giảm liều rifabutin.",
                },
            ],
            "moderate": [],
            "minor": [],
        },
        "contraindications_detail": {
            "tuyệt_đối": [
                "Dị ứng với rifabutin hoặc rifamycin khác.",
            ],
            "tương_đối": [
                "Bệnh gan mạn tính.",
                "Tiền sử viêm màng bồ đào.",
            ],
        },
        "pregnancy_lactation": {
            "fda_category": "B/C (tùy tài liệu)",
            "pregnancy_details": (
                "Dữ liệu trên người còn hạn chế; chỉ nên dùng khi thực sự cần thiết và không có lựa chọn an toàn hơn."
            ),
            "lactation": {
                "safety": "Caution",
                "details": "Không có nhiều dữ liệu; có thể bài tiết vào sữa.",
                "recommendation": "Cân nhắc lợi ích–nguy cơ cho mẹ và trẻ, ưu tiên thuốc có dữ liệu an toàn hơn nếu có.",
            },
        },
        "hepatic_adjustment": {
            "mild": "Có thể dùng nhưng cần theo dõi men gan.",
            "moderate": "Thận trọng; cân nhắc giảm liều hoặc tăng khoảng cách liều.",
            "severe": "Tránh nếu có lựa chọn khác.",
            "notes": "Chuyển hóa chủ yếu qua gan, nên suy gan làm tăng nguy cơ độc tính.",
        },
        "overdose_management": {
            "symptoms": [
                "Buồn nôn, nôn, đau bụng.",
                "Vàng da, mệt mỏi.",
                "Triệu chứng mắt (mờ, đau, đỏ).",
            ],
            "antidote": "Không có antidote đặc hiệu.",
            "treatment": [
                "Điều trị hỗ trợ, bù dịch.",
                "Theo dõi chức năng gan, công thức máu.",
                "Tham vấn chuyên khoa mắt nếu có triệu chứng uveitis.",
            ],
            "monitoring": "Men gan, công thức máu, triệu chứng mắt.",
        },
        "reversal_agents": None,
        "administration_instructions": {
            "oral": {
                "with_food": "Có thể uống cùng hoặc xa bữa ăn; thức ăn không ảnh hưởng đáng kể.",
                "timing": "Uống 1 lần/ngày, nên cố định thời điểm.",
            },
        },
        "references": {
            "primary_sources": [
                "WHO Consolidated Guidelines on Tuberculosis and HIV",
                "DHHS Guidelines for the Use of Antiretroviral Agents in Adults and Adolescents with HIV",
            ],
            "last_updated": "2025-02-18",
            "evidence_level": "High – guideline-based, nhưng phụ thuộc phác đồ ARV.",
        },
    },

    "Rifapentine": {
        "group": "Infectious Disease - Antitubercular (Long-acting rifamycin)",
        "vietnamese_name": "Rifapentine",
        "administration": ["PO"],
        "indications": [
            "Điều trị lao hoạt động (phối hợp trong một số phác đồ rút ngắn, theo nghiên cứu và guideline).",
            "Điều trị lao tiềm ẩn (LTBI) trong phác đồ isoniazid + rifapentine 1 lần/tuần (3HP, 1HP tùy guideline).",
        ],
        "contraindications": [
            "Dị ứng với rifapentine hoặc rifamycin khác.",
            "Bệnh gan nặng tiến triển.",
        ],
        "dosage": {
            "ltbi_3hp": "Isoniazid + rifapentine uống 1 lần/tuần trong 3 tháng (theo cân nặng và guideline).",
            "active_tb": "Liều theo cân nặng, thường 10–20mg/kg dùng 1–2 lần/tuần tùy phác đồ.",
            "notes": "Liều và lịch dùng rất phụ thuộc phác đồ cụ thể (3HP, 1HP, phác đồ rút ngắn); cần tham khảo guideline chi tiết.",
        },
        "renal_adjustment": {
            "normal": "Không cần điều chỉnh.",
            "30_60": "Thường không cần điều chỉnh; theo dõi độc tính.",
            "under_30": "Thận trọng; dữ liệu hạn chế, tham khảo tài liệu chuyên sâu.",
        },
        "side_effects": [
            "Tăng men gan, viêm gan do thuốc.",
            "Đổi màu dịch cơ thể (đỏ–cam) tương tự rifampin.",
            "Các triệu chứng giống cúm, đau đầu.",
            "Ban da, ngứa.",
        ],
        "interactions": [
            "Thuốc tránh thai uống, warfarin, nhiều thuốc chuyển hóa qua CYP3A4/2C8/2C9: giảm hiệu lực.",
            "ARV: tương tác phức tạp, cần tham khảo guideline HIV/TB khi phối hợp.",
        ],
        "pregnancy": "Không khuyến cáo rộng rãi trong thai kỳ do dữ liệu hạn chế; tham khảo guideline.",
        "mechanism_of_action": (
            "Rifapentine là rifamycin tác dụng kéo dài, ức chế RNA polymerase phụ thuộc DNA của vi khuẩn bằng cách gắn vào tiểu đơn vị β, "
            "ngăn tổng hợp RNA. Thời gian bán thải dài cho phép dùng ít lần hơn (1–2 lần/tuần) trong một số phác đồ lao hoạt động và lao tiềm ẩn."
        ),
        "monitoring": [
            "Men gan định kỳ trong quá trình điều trị.",
            "Triệu chứng viêm gan và phản ứng quá mẫn.",
            "Tương tác với các thuốc có khoảng điều trị hẹp (warfarin, thuốc chống loạn nhịp, thuốc chống động kinh...).",
        ],
        "precautions": [
            "Không dùng đơn trị trong lao hoạt động.",
            "Đánh giá tương tác thuốc kỹ, đặc biệt ở bệnh nhân đa bệnh lý.",
            "Thận trọng ở phụ nữ mang thai và cho con bú do dữ liệu hạn chế.",
        ],
        "pharmacokinetics": {
            "half_life": "13–25 giờ (dài hơn rifampin).",
            "onset": "Nồng độ đỉnh sau 5–6 giờ uống.",
            "duration": "Cho phép dùng liều hàng tuần trong một số phác đồ LTBI.",
            "protein_binding": "Rất cao (~98%).",
            "clearance": "Chủ yếu chuyển hóa và bài tiết qua mật, một phần qua thận.",
        },
        "storage": "Bảo quản nơi khô mát, tránh ánh sáng, 15–30°C.",
        "black_box_warnings": (
            "Nguy cơ tổn thương gan, đặc biệt khi phối hợp với các thuốc độc gan khác; cần theo dõi chức năng gan định kỳ."
        ),
        "drug_interactions": {
            "major": [
                {
                    "drug": "Thuốc tránh thai nội tiết, warfarin, thuốc chống loạn nhịp, thuốc chống động kinh",
                    "mechanism": "Cảm ứng CYP mạnh, tăng chuyển hóa thuốc.",
                    "effect": "Giảm nồng độ và hiệu quả điều trị.",
                    "management": "Cân nhắc thay thế thuốc hoặc tăng liều và theo dõi chỉ số hiệu quả (INR, ECG, kiểm soát cơn động kinh...).",
                }
            ],
            "moderate": [],
            "minor": [],
        },
        "contraindications_detail": {
            "tuyệt_đối": [
                "Dị ứng với rifapentine hoặc rifamycin khác.",
            ],
            "tương_đối": [
                "Bệnh gan mạn, uống rượu nhiều.",
                "Dùng nhiều thuốc có khoảng điều trị hẹp chuyển hóa qua CYP.",
            ],
        },
        "pregnancy_lactation": {
            "fda_category": "Chưa rõ/không phân loại rõ ràng",
            "pregnancy_details": (
                "Dữ liệu trên thai kỳ hạn chế; nên tránh dùng trừ khi lợi ích vượt trội nguy cơ và không có lựa chọn khác."
            ),
            "lactation": {
                "safety": "Caution",
                "details": "Chưa rõ mức độ bài tiết vào sữa mẹ.",
                "recommendation": "Cân nhắc lợi ích–nguy cơ; nếu dùng, theo dõi trẻ về triệu chứng gan và vàng da.",
            },
        },
        "hepatic_adjustment": {
            "mild": "Có thể dùng với theo dõi men gan.",
            "moderate": "Thận trọng; cân nhắc giảm liều hoặc kéo dài khoảng cách liều.",
            "severe": "Tránh dùng nếu có lựa chọn khác.",
            "notes": "Chuyển hóa chủ yếu qua gan; suy gan làm tăng nguy cơ độc tính.",
        },
        "overdose_management": {
            "symptoms": [
                "Buồn nôn, nôn, đau bụng.",
                "Mệt mỏi, vàng da.",
            ],
            "antidote": "Không có antidote đặc hiệu.",
            "treatment": [
                "Điều trị hỗ trợ, bù dịch.",
                "Theo dõi chặt chức năng gan.",
            ],
            "monitoring": "Men gan, bilirubin, triệu chứng lâm sàng.",
        },
        "reversal_agents": None,
        "administration_instructions": {
            "oral": {
                "with_food": "Thường dùng cùng thức ăn để cải thiện dung nạp đường tiêu hóa.",
                "timing": "Tùy phác đồ (1 lần/tuần hoặc 1–2 lần/tuần); nên uống cố định ngày trong tuần.",
            },
        },
        "references": {
            "primary_sources": [
                "CDC/ATS/IDSA Guidelines for the Treatment of Latent Tuberculosis Infection",
                "WHO documents on short-course rifapentine-based regimens",
            ],
            "last_updated": "2025-02-18",
            "evidence_level": "High – guideline and trial-based, nhưng áp dụng chọn lọc.",
        },
    },
}

__all__ = ["ANTITUBERCULAR_DRUGS"]


