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

    "Linezolid (lao MDR/XDR)": {
        "group": "Infectious Disease - Oxazolidinone (Second-line antitubercular, MDR/XDR-TB)",
        "vietnamese_name": "Linezolid",
        "administration": ["PO", "IV"],
        "indications": [
            "Điều trị lao kháng đa thuốc (MDR-TB) hoặc lao kháng rộng (XDR-TB) theo phác đồ WHO mới (group A drug).",
            "Một số nhiễm trùng Gram dương nặng (MRSA, VRE) – ngoài phạm vi lao.",
        ],
        "contraindications": [
            "Dị ứng với linezolid hoặc oxazolidinone khác.",
            "Đang dùng hoặc trong vòng 14 ngày sau khi dùng IMAO khác.",
            "Không kiểm soát được tình trạng suy tủy nặng.",
        ],
        "dosage": {
            "adult_mdr_tb": "600mg uống hoặc IV mỗi 24 giờ (nhiều phác đồ hiện giảm còn 600mg cách ngày hoặc 300mg/ngày sau giai đoạn đầu để giảm độc tính).",
            "adult_severe_infection": "600mg IV/PO mỗi 12 giờ (chỉ định ngoài lao).",
            "notes": "Trong MDR/XDR-TB ưu tiên liều thấp hơn hoặc giảm tần suất sau vài tháng để giảm độc tính thần kinh/huyết học; luôn theo phác đồ chuyên khoa.",
        },
        "renal_adjustment": {
            "normal": "Không cần chỉnh liều; tuy nhiên các chất chuyển hóa có thể tích lũy khi suy thận.",
            "30_60": "Thận trọng; theo dõi tác dụng phụ huyết học và thần kinh.",
            "under_30": "Không cần chỉnh liều chính, nhưng nên theo dõi chặt CBC và triệu chứng ngoại biên/thị giác.",
        },
        "side_effects": [
            "Ức chế tủy xương: thiếu máu, giảm bạch cầu, giảm tiểu cầu (phụ thuộc liều và thời gian).",
            "Bệnh lý thần kinh ngoại biên và thị giác (dùng kéo dài nhiều tháng).",
            "Nhiễm acid lactic, toan chuyển hóa (hiếm nhưng nặng).",
            "Buồn nôn, tiêu chảy, đau đầu.",
            "Hội chứng serotonin khi phối hợp SSRI, SNRI, TCA, triptan.",
        ],
        "interactions": [
            "SSRI, SNRI, TCA, MAOI, triptan: tăng nguy cơ hội chứng serotonin.",
            "Thuốc gây ức chế tủy xương khác (chemotherapy, zidovudine): tăng nguy cơ suy tủy.",
        ],
        "pregnancy": "C – dữ liệu hạn chế; chỉ dùng trong MDR/XDR-TB khi lợi ích vượt trội nguy cơ.",
        "mechanism_of_action": (
            "Linezolid là kháng sinh oxazolidinone, ức chế bước khởi đầu tổng hợp protein bằng cách gắn vào vị trí 23S của tiểu đơn vị 50S "
            "ribosome, ngăn hình thành phức hợp 70S. Đối với Mycobacterium tuberculosis, linezolid có tác dụng kìm khuẩn hoặc diệt khuẩn "
            "chậm, được xếp nhóm A trong phác đồ MDR/XDR-TB mới."
        ),
        "monitoring": [
            "Công thức máu (Hb, bạch cầu, tiểu cầu) hàng tuần trong giai đoạn đầu, sau đó ít nhất hàng tháng khi điều trị kéo dài.",
            "Triệu chứng thần kinh ngoại biên (tê bì, đau bỏng rát chi) và thị giác (mờ mắt, giảm thị lực màu).",
            "Lactate, toan chuyển hóa nếu có triệu chứng mệt nhiều, thở nhanh, đau bụng không giải thích được.",
        ],
        "precautions": [
            "Giới hạn thời gian dùng ở liều cao; giảm liều hoặc giãn cách sau vài tháng trong MDR-TB để giảm độc tính.",
            "Tránh phối hợp với thuốc serotoninergic mạnh nếu có thể; nếu bắt buộc, theo dõi sát hội chứng serotonin.",
            "Ngừng thuốc nếu có bệnh lý thần kinh thị giác tiến triển.",
        ],
        "pharmacokinetics": {
            "half_life": "khoảng 5–7 giờ.",
            "onset": "Nồng độ đỉnh sau 1–2 giờ (PO).",
            "duration": "Dùng 1–2 lần/ngày tùy chỉ định.",
            "protein_binding": "Khoảng 30%.",
            "clearance": "Gan (oxy hóa không qua CYP) và thận; chuyển hóa thành chất không hoạt tính.",
        },
        "storage": "Bảo quản nơi khô mát, tránh ánh sáng, 20–25°C.",
        "black_box_warnings": (
            "Nguy cơ ức chế tủy xương, bệnh lý thần kinh ngoại biên/thị giác và nhiễm acid lactic khi điều trị kéo dài; "
            "cần theo dõi sát CBC và thần kinh."
        ),
        "drug_interactions": {
            "major": [
                {
                    "drug": "SSRI, SNRI, TCA, MAOI, triptan",
                    "mechanism": "Tác dụng giống IMAO nhẹ của linezolid cộng hưởng với thuốc serotoninergic.",
                    "effect": "Nguy cơ hội chứng serotonin (sốt, run, cứng cơ, thay đổi ý thức).",
                    "management": "Tránh phối hợp nếu có thể; nếu bắt buộc, theo dõi sát và giáo dục bệnh nhân về triệu chứng.",
                }
            ],
            "moderate": [
                {
                    "drug": "Thuốc ức chế tủy xương (chemotherapy, zidovudine)",
                    "mechanism": "Hiệp đồng gây suy tủy.",
                    "effect": "Tăng nguy cơ thiếu máu, giảm bạch cầu, giảm tiểu cầu.",
                    "management": "Theo dõi CBC thường xuyên; cân nhắc giảm liều hoặc thay thuốc.",
                }
            ],
            "minor": [],
        },
        "contraindications_detail": {
            "tuyệt_đối": [
                "Dị ứng với linezolid.",
                "Đang dùng IMAO khác hoặc trong vòng 14 ngày sau ngừng IMAO.",
            ],
            "tương_đối": [
                "Tiền sử suy tủy, thiếu máu nặng.",
                "Bệnh thần kinh ngoại biên hoặc bệnh lý mắt nền.",
            ],
        },
        "pregnancy_lactation": {
            "fda_category": "C",
            "pregnancy_details": "Dữ liệu người hạn chế; chỉ dùng trong MDR/XDR-TB khi không có lựa chọn an toàn hơn.",
            "lactation": {
                "safety": "Caution",
                "details": "Chưa rõ mức bài tiết; cân nhắc ngừng cho bú khi điều trị kéo dài.",
                "recommendation": "Ưu tiên tránh nếu có lựa chọn khác; nếu dùng cần theo dõi trẻ.",
            },
        },
        "hepatic_adjustment": {
            "mild": "Không cần chỉnh.",
            "moderate": "Thận trọng; theo dõi độc tính.",
            "severe": "Dữ liệu hạn chế; chỉ dùng khi thật cần.",
            "notes": "Chuyển hóa không đáng kể qua CYP; suy gan trung bình có thể ít ảnh hưởng, nhưng dữ liệu dài hạn hạn chế.",
        },
        "overdose_management": {
            "symptoms": [
                "Tăng ức chế tủy (giảm tiểu cầu, thiếu máu).",
                "Hội chứng serotonin nếu phối hợp thuốc khác.",
                "Nôn, tiêu chảy, đau đầu.",
            ],
            "antidote": "Không có antidote đặc hiệu.",
            "treatment": [
                "Ngừng thuốc, điều trị hỗ trợ.",
                "Điều trị hội chứng serotonin nếu có (benzodiazepine, hỗ trợ hô hấp, cyproheptadine).",
            ],
            "monitoring": "CBC, dấu hiệu thần kinh, dấu hiệu sống.",
        },
        "reversal_agents": None,
        "administration_instructions": {
            "oral": {
                "with_food": "Có thể uống cùng hoặc không cùng thức ăn; thức ăn không ảnh hưởng đáng kể.",
                "timing": "Uống 1 hoặc 2 lần/ngày tùy phác đồ; cố định giờ.",
            },
            "iv": {
                "reconstitution": "Dùng dung dịch sẵn pha hoặc pha loãng theo hướng dẫn nhà sản xuất.",
                "infusion_rate": "Truyền trong 30–120 phút.",
                "compatibility": ["NS", "D5W"],
                "incompatibility": [],
            },
        },
        "references": {
            "primary_sources": [
                "WHO Consolidated Guidelines on Drug-Resistant Tuberculosis Treatment (Linezolid as Group A drug).",
                "NEJM and Lancet trials on linezolid-containing MDR-TB regimens.",
            ],
            "last_updated": "2025-03-02",
            "evidence_level": "High – guideline and RCT-based trong MDR/XDR-TB.",
        },
    },

    "Clofazimine": {
        "group": "Infectious Disease - Riminophenazine dye (Second-line antitubercular, MDR-TB; leprosy drug)",
        "vietnamese_name": "Clofazimine",
        "administration": ["PO"],
        "indications": [
            "Điều trị lao kháng đa thuốc (MDR-TB) trong các phác đồ nền mới (group B/C).",
            "Điều trị phong (Hansen) đa khuẩn (thuốc chuẩn trong phác đồ WHO).",
        ],
        "contraindications": [
            "Dị ứng với clofazimine hoặc các dẫn xuất tương tự.",
            "Bệnh nhân có tiền sử rối loạn nhịp thất nặng hoặc QTc kéo dài không kiểm soát.",
        ],
        "dosage": {
            "adult_mdr_tb": "100mg uống 1 lần/ngày (một số phác đồ dùng 50–100mg/ngày tùy cân nặng).",
            "adult_leprosy": "50mg/ngày kết hợp liều cao 300mg mỗi tháng (theo phác đồ WHO).",
            "notes": "Trong lao MDR, dùng kết hợp với nhiều thuốc khác trong thời gian 6–20 tháng theo phác đồ quốc gia/WHO.",
        },
        "renal_adjustment": {
            "normal": "Không cần chỉnh.",
            "30_60": "Không cần chỉnh; theo dõi tác dụng phụ tiêu hóa và da.",
            "under_30": "Không cần chỉnh liều, nhưng dữ liệu hạn chế; theo dõi sát.",
        },
        "side_effects": [
            "Tăng sắc tố da (da, niêm mạc, kết mạc màu nâu–đỏ, tím) và đổi màu phân; có thể kéo dài sau ngừng thuốc.",
            "Rối loạn tiêu hóa: đau bụng, buồn nôn, nôn, tiêu chảy.",
            "Khô da, ngứa, bong vảy.",
            "QTc kéo dài, xoắn đỉnh (hiếm, thường khi phối hợp nhiều thuốc kéo dài QT).",
        ],
        "interactions": [
            "Thuốc kéo dài QT khác (bedaquiline, moxifloxacin, delamanid): tăng nguy cơ loạn nhịp.",
        ],
        "pregnancy": "C – dữ liệu hạn chế; dùng khi lợi ích vượt nguy cơ, thường trong MDR-TB nặng.",
        "risk_flags": {
            "high_alert": True,
            "narrow_therapeutic_index": False,
            "organ_toxicity": {"cardiac": True, "dermatologic": True},
            "icu_critical_care_only": False,
            "look_alike_sound_alike": []
        },
        "guideline_tags": [
            "WHO Consolidated Guidelines on Drug-Resistant TB Treatment 2022",
            "Group B/C - MDR/XDR-TB Regimens"
        ],
        "mechanism_of_action": (
            "Clofazimine là thuốc nhuộm riminophenazine, tích lũy trong đại thực bào và tổ chức, có hoạt tính "
            "kháng Mycobacterium leprae và M. tuberculosis. Cơ chế chưa hoàn toàn rõ, có thể liên quan đến sinh các "
            "gốc oxy và can thiệp vận chuyển ion, làm tổn thương vách tế bào và DNA vi khuẩn."
        ),
        "monitoring": [
            "Điện tâm đồ (QTc) trước và định kỳ khi phối hợp với thuốc kéo dài QT khác.",
            "Triệu chứng tiêu hóa và giảm cân.",
            "Thay đổi sắc tố da và ảnh hưởng tâm lý (tự ti, trầm cảm).",
        ],
        "precautions": [
            "Tư vấn trước về thay đổi màu da/niêm mạc để giảm lo lắng và cải thiện tuân thủ.",
            "Thận trọng khi phối hợp với bedaquiline, delamanid, fluoroquinolone do cộng hưởng kéo dài QT.",
            "Tránh dùng ở bệnh nhân có QTc >500 ms hoặc rối loạn nhịp thất không ổn định.",
        ],
        "pharmacokinetics": {
            "half_life": "Rất dài (~70 ngày) do tích lũy mô.",
            "onset": "Tác dụng tích lũy dần sau vài tuần.",
            "duration": "Hiệu ứng kéo dài nhiều tháng sau ngừng thuốc.",
            "protein_binding": "Rất cao, phân bố nhiều ở mô mỡ và mô liên kết.",
            "clearance": "Chủ yếu qua mật và phân; rất ít qua thận.",
        },
        "storage": "Bảo quản nơi khô mát, tránh ánh sáng, 15–30°C.",
        "black_box_warnings": (
            "Có thể gây tăng sắc tố da dai dẳng và kéo dài QT; cần theo dõi ECG khi phối hợp các thuốc kéo dài QT khác."
        ),
        "drug_interactions": {
            "major": [
                {
                    "drug": "Bedaquiline, Delamanid, Fluoroquinolones",
                    "mechanism": "Cộng hưởng kéo dài QT.",
                    "effect": "Tăng nguy cơ xoắn đỉnh, rung thất.",
                    "management": "Theo dõi ECG định kỳ, điều chỉnh phác đồ nếu QTc >500 ms.",
                }
            ],
            "moderate": [],
            "minor": [],
        },
        "contraindications_detail": {
            "tuyệt_đối": [
                "QTc kéo dài nặng, loạn nhịp thất không kiểm soát.",
            ],
            "tương_đối": [
                "Tiền sử trầm cảm nặng (do thay đổi sắc tố gây ảnh hưởng tâm lý).",
                "Bệnh gan mạn tính (do chuyển hóa mật).",
            ],
        },
        "pregnancy_lactation": {
            "fda_category": "C",
            "pregnancy_details": "Dữ liệu hạn chế; chỉ dùng khi cần trong MDR-TB, tránh trong thai kỳ nhẹ/ổn định.",
            "lactation": {
                "safety": "Caution",
                "details": "Có thể bài tiết vào sữa; nguy cơ đổi màu da trẻ.",
                "recommendation": "Cân nhắc lợi ích–nguy cơ; theo dõi da trẻ nếu dùng.",
            },
        },
        "hepatic_adjustment": {
            "mild": "Thận trọng; theo dõi men gan.",
            "moderate": "Giảm liều hoặc kéo dài khoảng cách liều nếu có dấu hiệu độc gan.",
            "severe": "Tránh dùng nếu có thể.",
            "notes": "Thải trừ chủ yếu qua mật; suy gan có thể tăng tích lũy.",
        },
        "overdose_management": {
            "symptoms": [
                "Buồn nôn, nôn, đau bụng.",
                "Rối loạn nhịp tim, QT kéo dài.",
                "Tăng sắc tố da rõ.",
            ],
            "antidote": "Không có antidote đặc hiệu.",
            "treatment": [
                "Điều trị hỗ trợ, theo dõi ECG.",
                "Sửa rối loạn điện giải (K+, Mg2+).",
            ],
            "monitoring": "ECG, men gan, triệu chứng lâm sàng.",
        },
        "reversal_agents": None,
        "administration_instructions": {
            "oral": {
                "with_food": "Nên uống cùng bữa ăn để giảm kích ứng tiêu hóa và tăng hấp thu.",
                "timing": "Uống 1 lần/ngày, cố định giờ.",
            },
        },
        "references": {
            "primary_sources": [
                "WHO Consolidated Guidelines on Drug-Resistant Tuberculosis Treatment (Clofazimine as Group B/C).",
                "Clinical trials of clofazimine-containing MDR-TB regimens.",
            ],
            "last_updated": "2025-03-02",
            "evidence_level": "Moderate–High trong MDR-TB; High trong phong.",
        },
    },

    "Bedaquiline": {
        "group": "Infectious Disease - Diarylquinoline (Group A second-line antitubercular for MDR/XDR-TB)",
        "vietnamese_name": "Bedaquiline",
        "administration": ["PO"],
        "indications": [
            "Điều trị lao kháng đa thuốc (MDR-TB) hoặc XDR-TB trong phác đồ ngắn/ngắn mở rộng theo WHO (Group A).",
        ],
        "contraindications": [
            "Dị ứng với bedaquiline.",
            "QTc >500 ms hoặc tiền sử loạn nhịp thất nặng.",
            "Bệnh gan nặng tiến triển (Child-Pugh C) không kiểm soát.",
        ],
        "dosage": {
            "adult_mdr_tb": "Tuần 1–2: 400mg/ngày; tuần 3–24: 200mg uống 3 lần/tuần (cách ngày), tổng tối đa 24 tuần.",
            "notes": "Luôn dùng cùng bữa ăn (tăng hấp thu); không vượt quá thời gian 6 tháng trừ khi có chỉ định đặc biệt.",
        },
        "renal_adjustment": {
            "normal": "Không cần chỉnh.",
            "30_60": "Không cần chỉnh; theo dõi tác dụng phụ.",
            "under_30": "Dữ liệu hạn chế; thận trọng và theo dõi sát.",
        },
        "side_effects": [
            "QTc kéo dài, nguy cơ xoắn đỉnh.",
            "Tăng men gan, viêm gan do thuốc.",
            "Đau đầu, buồn nôn, đau khớp.",
        ],
        "interactions": [
            "Thuốc kéo dài QT khác (clofazimine, moxifloxacin, delamanid): tăng nguy cơ loạn nhịp.",
            "CYP3A4 inducers (rifampin, efavirenz): giảm nồng độ bedaquiline, giảm hiệu quả.",
            "CYP3A4 inhibitors mạnh (ketoconazole, protease inhibitor): tăng nồng độ, tăng độc tính.",
        ],
        "pregnancy": "Không khuyến cáo rộng rãi; cân nhắc chỉ dùng khi không có lựa chọn an toàn hơn trong MDR/XDR-TB nặng.",
        "risk_flags": {
            "high_alert": True,
            "narrow_therapeutic_index": False,
            "organ_toxicity": {"cardiac": True, "hepatic": True},
            "icu_critical_care_only": False,
            "look_alike_sound_alike": []
        },
        "guideline_tags": [
            "WHO Consolidated Guidelines on Drug-Resistant TB Treatment 2022",
            "Group A - MDR/XDR-TB Regimens"
        ],
        "mechanism_of_action": (
            "Bedaquiline ức chế ATP synthase (subunit c) đặc hiệu của Mycobacterium tuberculosis, "
            "làm mất khả năng tạo ATP và gây chết vi khuẩn, bao gồm cả vi khuẩn đang nhân lên chậm hoặc ngủ. "
            "Được xếp Group A trong phác đồ MDR/XDR-TB hiện đại."
        ),
        "monitoring": [
            "ECG (QTc) trước điều trị và định kỳ (ví dụ mỗi tháng) hoặc khi thêm thuốc kéo dài QT khác.",
            "Men gan (ALT, AST, bilirubin) trước và định kỳ.",
            "Triệu chứng loạn nhịp (hồi hộp, ngất, chóng mặt).",
        ],
        "precautions": [
            "Tránh phối hợp với rifampin hoặc cảm ứng CYP3A4 mạnh (giảm hiệu quả rõ).",
            "Hạn chế phối hợp nhiều thuốc kéo dài QT; nếu cần, theo dõi ECG sát và chỉnh phác đồ khi QTc >500 ms.",
            "Ngừng thuốc nếu xuất hiện loạn nhịp thất nguy hiểm hoặc tăng QTc rõ rệt không hồi phục sau chỉnh điện giải.",
        ],
        "pharmacokinetics": {
            "half_life": "~5.5 tháng (rất dài do phân bố mô mạnh).",
            "onset": "Tích lũy dần; hiệu quả thấy sau vài tuần.",
            "duration": "Tác dụng kéo dài nhiều tháng do half-life dài.",
            "protein_binding": ">99%.",
            "clearance": "Gan (CYP3A4); thải trừ chủ yếu qua mật và phân.",
        },
        "storage": "Bảo quản nơi khô mát, tránh ánh sáng, 15–30°C.",
        "black_box_warnings": (
            "Nguy cơ tử vong tăng trong một số nghiên cứu ban đầu (không giải thích rõ) và QTc kéo dài đáng kể; "
            "chỉ dùng khi lợi ích vượt trội và theo dõi ECG chặt chẽ."
        ),
        "drug_interactions": {
            "major": [
                {
                    "drug": "Rifampin, Rifapentine, Efavirenz",
                    "mechanism": "Cảm ứng CYP3A4 mạnh, giảm nồng độ bedaquiline.",
                    "effect": "Giảm hiệu quả điều trị MDR-TB.",
                    "management": "Tránh phối hợp; nếu bắt buộc, tham khảo phác đồ chuyên khoa và theo dõi sát.",
                },
                {
                    "drug": "Ketoconazole, Protease inhibitors",
                    "mechanism": "Ức chế CYP3A4 mạnh.",
                    "effect": "Tăng nồng độ bedaquiline và nguy cơ QT kéo dài/độc gan.",
                    "management": "Tránh phối hợp hoặc theo dõi sát ECG và men gan.",
                },
            ],
            "moderate": [
                {
                    "drug": "Clofazimine, Delamanid, Fluoroquinolones",
                    "mechanism": "Cộng hưởng kéo dài QT.",
                    "effect": "Tăng nguy cơ loạn nhịp thất.",
                    "management": "Theo dõi ECG định kỳ, giảm bớt thuốc kéo dài QT khác nếu có thể.",
                }
            ],
            "minor": [],
        },
        "contraindications_detail": {
            "tuyệt_đối": [
                "QTc >500 ms.",
                "Loạn nhịp thất nặng chưa kiểm soát.",
            ],
            "tương_đối": [
                "Bệnh gan mạn tiến triển.",
                "Dùng đồng thời nhiều thuốc kéo dài QT.",
            ],
        },
        "pregnancy_lactation": {
            "fda_category": "C (theo tương đương)",
            "pregnancy_details": "Dữ liệu người rất ít; chỉ dùng trong MDR/XDR-TB đe dọa tính mạng và không có lựa chọn khác.",
            "lactation": {
                "safety": "Caution",
                "details": "Chưa rõ mức bài tiết; nên thận trọng.",
                "recommendation": "Cân nhắc ngừng cho bú nếu dùng kéo dài.",
            },
        },
        "hepatic_adjustment": {
            "mild": "Có thể dùng với theo dõi men gan.",
            "moderate": "Thận trọng; tăng tần suất theo dõi men gan.",
            "severe": "Tránh dùng nếu có lựa chọn khác.",
            "notes": "Chuyển hóa mạnh qua gan; suy gan làm tăng nguy cơ độc tính.",
        },
        "overdose_management": {
            "symptoms": [
                "QT kéo dài, loạn nhịp thất.",
                "Tăng men gan, vàng da.",
            ],
            "antidote": "Không có antidote đặc hiệu.",
            "treatment": [
                "Điều trị hỗ trợ, theo dõi tại ICU nếu loạn nhịp.",
                "Sửa rối loạn điện giải (K+, Mg2+, Ca2+).",
                "Theo dõi ECG liên tục.",
            ],
            "monitoring": "ECG, men gan, dấu hiệu sinh tồn.",
        },
        "reversal_agents": None,
        "administration_instructions": {
            "oral": {
                "with_food": "BẮT BUỘC dùng cùng thức ăn giàu mỡ để tăng hấp thu (gấp ~2 lần).",
                "timing": "Theo đúng lịch tải/duy trì (tuần 1–2 hằng ngày, sau đó 3 lần/tuần).",
            },
        },
        "references": {
            "primary_sources": [
                "WHO Consolidated Guidelines on Drug-Resistant Tuberculosis Treatment (Bedaquiline as Group A).",
                "NEJM trials on bedaquiline-containing MDR-TB regimens.",
            ],
            "last_updated": "2025-03-02",
            "evidence_level": "High trong MDR/XDR-TB (guideline- and trial-based).",
        },
    },

    "Delamanid": {
        "group": "Infectious Disease - Nitroimidazole (Group C second-line antitubercular for MDR/XDR-TB)",
        "vietnamese_name": "Delamanid",
        "administration": ["PO"],
        "indications": [
            "Điều trị lao kháng đa thuốc (MDR-TB) và XDR-TB phối hợp với phác đồ nền phù hợp.",
        ],
        "contraindications": [
            "Dị ứng với delamanid.",
            "QTc >500 ms hoặc loạn nhịp thất nặng.",
            "Albumin máu rất thấp (<2.8 g/dL) do tăng nguy cơ QT kéo dài.",
        ],
        "dosage": {
            "adult_mdr_tb": "100mg uống 2 lần/ngày trong 24 tuần, cùng phác đồ nền MDR/XDR-TB.",
            "notes": "Dùng cùng thức ăn để tăng hấp thu; kéo dài hơn 24 tuần chỉ khi có chỉ định chuyên khoa.",
        },
        "renal_adjustment": {
            "normal": "Không cần chỉnh.",
            "30_60": "Không cần chỉnh; dữ liệu hạn chế.",
            "under_30": "Chưa có dữ liệu rõ; thận trọng và theo dõi sát nếu bắt buộc dùng.",
        },
        "side_effects": [
            "QTc kéo dài, loạn nhịp thất (nguy cơ tăng nếu albumin thấp).",
            "Buồn nôn, nôn, đau đầu.",
            "Giảm cân, kém ăn.",
        ],
        "interactions": [
            "Thuốc kéo dài QT (bedaquiline, clofazimine, fluoroquinolones): cộng hưởng kéo dài QT.",
            "Inducer CYP3A4 mạnh (rifampin): có thể giảm nồng độ delamanid.",
        ],
        "pregnancy": "Dữ liệu hạn chế; không khuyến cáo thường quy, chỉ dùng khi lợi ích vượt trội nguy cơ.",
        "risk_flags": {
            "high_alert": True,
            "narrow_therapeutic_index": False,
            "organ_toxicity": {"cardiac": True},
            "icu_critical_care_only": False,
            "look_alike_sound_alike": []
        },
        "guideline_tags": [
            "WHO Consolidated Guidelines on Drug-Resistant TB Treatment 2022",
            "Group C - MDR/XDR-TB Regimens"
        ],
        "mechanism_of_action": (
            "Delamanid là dẫn xuất nitro-dihydro-imidazooxazole; sau khi được nitroreductase của vi khuẩn hoạt hóa, "
            "thuốc ức chế tổng hợp acid mycolic (methoxy- và keto-mycolic acid), thành phần vách tế bào Mycobacterium tuberculosis, "
            "dẫn tới rối loạn vách và chết vi khuẩn."
        ),
        "monitoring": [
            "ECG (QTc) trước điều trị, sau 2 tuần, rồi định kỳ.",
            "Albumin huyết thanh; thận trọng nếu <2.8 g/dL.",
            "Triệu chứng tim mạch (hồi hộp, ngất).",
        ],
        "precautions": [
            "Hạn chế phối hợp với nhiều thuốc kéo dài QT; nếu cần, tăng tần suất theo dõi ECG.",
            "Điều chỉnh dinh dưỡng và điều trị albumin thấp nếu có thể.",
            "Không dùng đơn trị; luôn phối hợp nhiều thuốc hoạt lực cao trong MDR/XDR-TB.",
        ],
        "pharmacokinetics": {
            "half_life": "~30–38 giờ.",
            "onset": "Hấp thu tăng rõ với thức ăn giàu mỡ.",
            "duration": "Dùng 2 lần/ngày.",
            "protein_binding": ">99% (phụ thuộc albumin).",
            "clearance": "Chuyển hóa nhiều qua albumin và CYP; thải trừ chủ yếu qua phân.",
        },
        "storage": "Bảo quản nơi khô mát, tránh ánh sáng, 15–30°C.",
        "black_box_warnings": (
            "Nguy cơ QTc kéo dài đáng kể, đặc biệt khi albumin thấp hoặc phối hợp thuốc kéo dài QT khác; "
            "cần theo dõi ECG và albumin sát."
        ),
        "drug_interactions": {
            "major": [
                {
                    "drug": "Bedaquiline, Clofazimine, Fluoroquinolones",
                    "mechanism": "Cộng hưởng kéo dài QT.",
                    "effect": "Tăng nguy cơ xoắn đỉnh.",
                    "management": "Theo dõi ECG sát, cân nhắc giảm số thuốc kéo dài QT trong phác đồ.",
                }
            ],
            "moderate": [
                {
                    "drug": "Rifampin và các cảm ứng CYP mạnh",
                    "mechanism": "Tăng chuyển hóa delamanid.",
                    "effect": "Giảm nồng độ và hiệu quả.",
                    "management": "Tránh phối hợp; sử dụng phác đồ khác nếu cần rifampin.",
                }
            ],
            "minor": [],
        },
        "contraindications_detail": {
            "tuyệt_đối": [
                "QTc >500 ms.",
                "Albumin rất thấp không cải thiện được.",
            ],
            "tương_đối": [
                "Tiền sử bệnh tim mạch cấu trúc, loạn nhịp thất.",
                "Dùng đồng thời nhiều thuốc kéo dài QT.",
            ],
        },
        "pregnancy_lactation": {
            "fda_category": "C (áp dụng theo mức độ dữ liệu hạn chế).",
            "pregnancy_details": "Chỉ dùng khi MDR/XDR-TB nặng, sau khi cân nhắc lợi ích–nguy cơ.",
            "lactation": {
                "safety": "Caution",
                "details": "Chưa rõ bài tiết sữa; thận trọng khi cho con bú.",
                "recommendation": "Cân nhắc tạm ngừng cho bú trong giai đoạn dùng delamanid.",
            },
        },
        "hepatic_adjustment": {
            "mild": "Có thể dùng; theo dõi men gan.",
            "moderate": "Thận trọng, tăng tần suất theo dõi.",
            "severe": "Tránh dùng nếu có lựa chọn khác.",
            "notes": "Chuyển hóa qua gan; suy gan nặng có thể tăng nồng độ.",
        },
        "overdose_management": {
            "symptoms": [
                "QT kéo dài, loạn nhịp.",
                "Buồn nôn, nôn, chóng mặt.",
            ],
            "antidote": "Không có antidote đặc hiệu.",
            "treatment": [
                "Điều trị hỗ trợ, theo dõi ECG liên tục.",
                "Sửa điện giải, dùng magnesi IV nếu có xoắn đỉnh.",
            ],
            "monitoring": "ECG, men gan, dấu hiệu sinh tồn.",
        },
        "reversal_agents": None,
        "administration_instructions": {
            "oral": {
                "with_food": "Dùng cùng thức ăn để tăng hấp thu.",
                "timing": "100mg x 2 lần/ngày, cách nhau 12 giờ.",
            },
        },
        "references": {
            "primary_sources": [
                "WHO Consolidated Guidelines on Drug-Resistant Tuberculosis Treatment (Delamanid as Group C).",
                "Phase II & III delamanid MDR-TB trials.",
            ],
            "last_updated": "2025-03-02",
            "evidence_level": "Moderate–High trong MDR/XDR-TB (trial- and guideline-based).",
        },
    },

    "Cycloserine / Terizidone": {
        "group": "Infectious Disease - Second-line antitubercular (D-alanine analog, MDR-TB)",
        "vietnamese_name": "Cycloserine, Terizidone",
        "administration": ["PO"],
        "indications": [
            "Điều trị MDR/XDR-TB khi không đủ số thuốc nhóm A/B; thường nhóm C.",
        ],
        "contraindications": [
            "Động kinh không kiểm soát.",
            "Rối loạn tâm thần nặng (trầm cảm, loạn thần) không kiểm soát.",
            "Suy thận nặng không chỉnh được liều.",
        ],
        "dosage": {
            "adult_mdr_tb": "Usual 10–15mg/kg/ngày chia 2 lần (tối đa 750–1000mg/ngày), điều chỉnh theo dung nạp và chức năng thận.",
            "notes": "Bổ sung pyridoxine (vitamin B6) để giảm độc tính thần kinh; chia liều để giảm dao động nồng độ.",
        },
        "renal_adjustment": {
            "normal": "Dùng liều chuẩn chia 2 lần/ngày.",
            "30_60": "Giảm liều hoặc kéo dài khoảng cách liều (ví dụ 250mg mỗi 12–24 giờ).",
            "under_30": "Giảm đáng kể liều, có thể 250mg mỗi 24–48 giờ; tham khảo phác đồ chuyên khoa.",
        },
        "side_effects": [
            "Độc tính thần kinh trung ương: kích thích, mất ngủ, loạn thần, trầm cảm, ý tưởng tự sát.",
            "Co giật (đặc biệt khi không chỉnh liều ở suy thận hoặc không dùng B6).",
            "Nhức đầu, run tay.",
            "Buồn nôn, nôn.",
        ],
        "interactions": [
            "Rượu, thuốc hướng thần (SSRI, TCA, antipsychotic): có thể làm nặng triệu chứng tâm thần.",
            "Thuốc làm giảm ngưỡng co giật (tramadol, fluoroquinolone): tăng nguy cơ co giật.",
        ],
        "pregnancy": "Dữ liệu hạn chế; chỉ dùng khi MDR/XDR-TB nặng và không có lựa chọn khác.",
        "risk_flags": {
            "high_alert": True,
            "narrow_therapeutic_index": False,
            "organ_toxicity": {"neurologic": True, "psychiatric": True},
            "icu_critical_care_only": False,
            "look_alike_sound_alike": []
        },
        "guideline_tags": [
            "WHO Consolidated Guidelines on Drug-Resistant TB Treatment 2022",
            "Group C - MDR/XDR-TB Regimens"
        ],
        "mechanism_of_action": (
            "Cycloserine là chất tương tự D-alanine, ức chế enzyme alanine racemase và D-alanine:D-alanine ligase, "
            "ngăn tổng hợp peptidoglycan của vách tế bào Mycobacterium tuberculosis, dẫn đến rối loạn vách và chết vi khuẩn."
        ),
        "monitoring": [
            "Đánh giá tâm thần kinh cơ bản (trầm cảm, lo âu, tiền sử co giật) trước khi bắt đầu.",
            "Theo dõi triệu chứng tâm thần (mất ngủ nặng, loạn thần, ý tưởng tự sát) mỗi lần tái khám.",
            "Chức năng thận định kỳ để điều chỉnh liều.",
        ],
        "precautions": [
            "Luôn bổ sung pyridoxine để giảm độc thần kinh.",
            "Ngừng thuốc nếu xuất hiện loạn thần nặng hoặc ý tưởng tự sát; điều trị chuyên khoa tâm thần.",
            "Tránh rượu và các chất kích thích thần kinh.",
        ],
        "pharmacokinetics": {
            "half_life": "~10 giờ (kéo dài khi suy thận).",
            "onset": "Hấp thu tốt qua đường uống.",
            "duration": "Dùng 1–2 lần/ngày.",
            "protein_binding": "Thấp.",
            "clearance": "Thải trừ chủ yếu qua thận ở dạng không chuyển hóa.",
        },
        "storage": "Bảo quản nơi khô mát, tránh ánh sáng, 15–30°C.",
        "black_box_warnings": (
            "Nguy cơ cao gây rối loạn tâm thần và co giật, đặc biệt khi dùng liều cao hoặc suy thận; "
            "cần sàng lọc và theo dõi tâm thần chặt chẽ."
        ),
        "drug_interactions": {
            "major": [
                {
                    "drug": "Rượu, thuốc kích thích thần kinh",
                    "mechanism": "Tăng kích thích CNS.",
                    "effect": "Tăng nguy cơ loạn thần, co giật.",
                    "management": "Tránh hoàn toàn rượu; thận trọng với thuốc hướng thần.",
                }
            ],
            "moderate": [
                {
                    "drug": "Thuốc làm giảm ngưỡng co giật (tramadol, fluoroquinolone)",
                    "mechanism": "Cộng hưởng kích thích CNS.",
                    "effect": "Tăng nguy cơ co giật.",
                    "management": "Hạn chế phối hợp; nếu bắt buộc, theo dõi sát và cân nhắc giảm liều.",
                }
            ],
            "minor": [],
        },
        "contraindications_detail": {
            "tuyệt_đối": [
                "Động kinh không kiểm soát.",
                "Rối loạn tâm thần nặng hiện tại.",
            ],
            "tương_đối": [
                "Tiền sử trầm cảm, ý tưởng tự sát.",
                "Suy thận trung bình–nặng.",
            ],
        },
        "pregnancy_lactation": {
            "fda_category": "C/D (dữ liệu hạn chế, nghiêng về thận trọng cao).",
            "pregnancy_details": "Chỉ dùng khi MDR/XDR-TB đe dọa tính mạng và cuối cùng không có thuốc khác.",
            "lactation": {
                "safety": "Caution",
                "details": "Chưa rõ mức bài tiết; cân nhắc thận trọng.",
                "recommendation": "Thảo luận nguy cơ–lợi ích; có thể ưu tiên ngừng cho bú.",
            },
        },
        "hepatic_adjustment": {
            "mild": "Không cần chỉnh; chủ yếu theo dõi thận.",
            "moderate": "Không cần chỉnh liều riêng, nhưng cân nhắc toàn bộ phác đồ.",
            "severe": "Ảnh hưởng hạn chế; điều chỉnh theo thận là chính.",
            "notes": "Thải trừ qua thận; suy gan ít ảnh hưởng.",
        },
        "overdose_management": {
            "symptoms": [
                "Kích thích, loạn thần nặng.",
                "Co giật.",
            ],
            "antidote": "Không có antidote đặc hiệu.",
            "treatment": [
                "Điều trị co giật bằng benzodiazepine.",
                "An thần và điều trị hỗ trợ tâm thần.",
                "Lọc máu có thể giúp loại bỏ thuốc (do thải qua thận).",
            ],
            "monitoring": "Trạng thái tâm thần, dấu hiệu sinh tồn, chức năng thận.",
        },
        "reversal_agents": None,
        "administration_instructions": {
            "oral": {
                "with_food": "Có thể uống cùng hoặc không cùng thức ăn.",
                "timing": "Chia 1–2 lần/ngày; tránh dùng tối muộn nếu gây mất ngủ.",
            },
        },
        "references": {
            "primary_sources": [
                "WHO Consolidated Guidelines on Drug-Resistant Tuberculosis Treatment (Cycloserine/Terizidone as Group C).",
            ],
            "last_updated": "2025-03-02",
            "evidence_level": "Moderate – sử dụng rộng rãi nhưng độc tính thần kinh cao.",
        },
    },

    "PAS (para-aminosalicylic acid)": {
        "group": "Infectious Disease - Second-line antitubercular (folate antagonist, MDR-TB)",
        "vietnamese_name": "Acid para-aminosalicylic (PAS)",
        "administration": ["PO"],
        "indications": [
            "Điều trị MDR/XDR-TB khi không đủ lựa chọn khác (thường Group C/D).",
        ],
        "contraindications": [
            "Dị ứng với PAS hoặc salicylate nặng.",
            "Suy gan nặng tiến triển.",
        ],
        "dosage": {
            "adult_mdr_tb": "8–12g/ngày chia 2–3 lần, thường dùng dạng hạt phóng thích chậm theo khuyến cáo nhà sản xuất.",
            "notes": "Luôn dùng phối hợp với nhiều thuốc khác; điều chỉnh liều giảm nếu dung nạp kém.",
        },
        "renal_adjustment": {
            "normal": "Không cần chỉnh.",
            "30_60": "Thận trọng; theo dõi chức năng thận và dung nạp.",
            "under_30": "Dữ liệu hạn chế; có thể cần giảm liều hoặc tăng khoảng cách; tham khảo chuyên khoa.",
        },
        "side_effects": [
            "Rối loạn tiêu hóa nặng: buồn nôn, nôn, tiêu chảy, đau bụng.",
            "Viêm gan do thuốc.",
            "Dị ứng: phát ban, sốt, hiếm gặp hội chứng giống lupus.",
        ],
        "interactions": [
            "Thuốc gây độc gan khác: tăng nguy cơ viêm gan.",
        ],
        "pregnancy": "Dữ liệu hạn chế; không dùng thường quy, chỉ khi cần trong MDR/XDR-TB nặng.",
        "risk_flags": {
            "high_alert": True,
            "narrow_therapeutic_index": False,
            "organ_toxicity": {"hepatic": True, "gastrointestinal": True},
            "icu_critical_care_only": False,
            "look_alike_sound_alike": []
        },
        "guideline_tags": [
            "WHO Consolidated Guidelines on Drug-Resistant TB Treatment 2022",
            "Group C/D - MDR/XDR-TB Regimens"
        ],
        "mechanism_of_action": (
            "PAS là chất tương tự PABA, ức chế tổng hợp acid folic ở Mycobacterium tuberculosis; "
            "đồng thời làm giảm hấp thu/hoạt tính một số thuốc chống lao khác nếu dùng sai cách, nên cần tuân thủ hướng dẫn phối hợp."
        ),
        "monitoring": [
            "Men gan định kỳ.",
            "Triệu chứng tiêu hóa và cân nặng.",
            "Dấu hiệu dị ứng (ban, sốt).",
        ],
        "precautions": [
            "Cho bệnh nhân dùng thuốc cùng thức ăn để giảm kích ứng dạ dày.",
            "Giảm liều hoặc chuyển dạng bào chế phóng thích chậm nếu tiêu hóa kém.",
            "Ngừng thuốc nếu có viêm gan lâm sàng rõ hoặc phản ứng dị ứng nặng.",
        ],
        "pharmacokinetics": {
            "half_life": "~1 giờ (ngắn).",
            "onset": "Hấp thu tương đối nhanh, nhưng dung nạp phụ thuộc dạng bào chế.",
            "duration": "Cần chia liều 2–3 lần/ngày.",
            "protein_binding": "Trung bình.",
            "clearance": "Chủ yếu qua thận (liên hợp acetyl, glucuronid).",
        },
        "storage": "Bảo quản nơi khô mát, tránh ẩm và ánh sáng; dạng hạt cần bảo quản theo hướng dẫn đặc biệt.",
        "black_box_warnings": (
            "Nguy cơ viêm gan và rối loạn tiêu hóa nặng có thể dẫn tới bỏ điều trị; cần theo dõi và can thiệp sớm."
        ),
        "drug_interactions": {
            "major": [],
            "moderate": [
                {
                    "drug": "Thuốc độc gan (INH, RIF, PZA, alcohol)",
                    "mechanism": "Tăng gánh nặng gan.",
                    "effect": "Tăng nguy cơ viêm gan.",
                    "management": "Theo dõi men gan sát; tư vấn tránh rượu.",
                }
            ],
            "minor": [],
        },
        "contraindications_detail": {
            "tuyệt_đối": [
                "Dị ứng nặng với PAS.",
                "Viêm gan cấp tiến triển.",
            ],
            "tương_đối": [
                "Bệnh gan mạn.",
                "Tiền sử rối loạn tiêu hóa nặng.",
            ],
        },
        "pregnancy_lactation": {
            "fda_category": "C (thận trọng).",
            "pregnancy_details": "Chỉ dùng khi cần thiết trong MDR/XDR-TB và không có thuốc khác an toàn hơn.",
            "lactation": {
                "safety": "Caution",
                "details": "Có thể bài tiết vào sữa; dữ liệu hạn chế.",
                "recommendation": "Cân nhắc lợi ích–nguy cơ, theo dõi trẻ tiêu chảy hoặc vàng da.",
            },
        },
        "hepatic_adjustment": {
            "mild": "Theo dõi men gan; cân nhắc giảm liều nếu tăng men gan.",
            "moderate": "Thận trọng; chỉ dùng khi thật cần, với theo dõi sát.",
            "severe": "Tránh dùng nếu có thể.",
            "notes": "PAS có độc tính gan; suy gan làm tăng nguy cơ.",
        },
        "overdose_management": {
            "symptoms": [
                "Nôn, tiêu chảy nặng, đau bụng.",
                "Tăng men gan, vàng da.",
            ],
            "antidote": "Không có antidote đặc hiệu.",
            "treatment": [
                "Điều trị hỗ trợ, bù dịch, điều chỉnh điện giải.",
                "Theo dõi và điều trị suy gan nếu có.",
            ],
            "monitoring": "Men gan, chức năng thận, điện giải, tình trạng lâm sàng.",
        },
        "reversal_agents": None,
        "administration_instructions": {
            "oral": {
                "with_food": "Nên uống cùng thức ăn để giảm kích ứng dạ dày.",
                "timing": "Chia 2–3 lần/ngày theo chỉ định.",
            },
        },
        "references": {
            "primary_sources": [
                "WHO Consolidated Guidelines on Drug-Resistant Tuberculosis Treatment (PAS as Group C/D).",
            ],
            "last_updated": "2025-03-02",
            "evidence_level": "Moderate (ít dùng hơn do dung nạp kém).",
        }
    }
}

__all__ = ["ANTITUBERCULAR_DRUGS"]


