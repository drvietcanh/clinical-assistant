"""
Muscle Relaxants
Skeletal muscle relaxants for spasticity and muscle spasms
"""

MUSCLE_RELAXANTS_DRUGS = {
    "Baclofen": {
        "group": "Neurology - Muscle Relaxant (GABA-B Agonist)",
        "vietnamese_name": "Baclofen, Lioresal",
        "administration": ["PO", "Intrathecal"],
        "indications": [
            "Co cứng cơ (spasticity) - đa xơ cứng, chấn thương tủy sống",
            "Co cứng cơ do bại não",
            "Đau cơ xương (off-label)",
            "Hiccups kháng trị (off-label)"
        ],
        "contraindications": [
            "Dị ứng",
            "Suy thận nặng (CrCl <30)"
        ],
        "dosage": {
            "adult_spasticity_po": "5mg x 3 lần/ngày, tăng dần mỗi 3-7 ngày đến 15-20mg x 3-4 lần/ngày (tối đa 80mg/ngày)",
            "adult_intrathecal": "Bắt đầu với test dose, sau đó truyền liên tục qua pump (50-200mcg/ngày)",
            "adult_max": "80mg/ngày PO",
            "notes": "GABA-B receptor agonist. Tăng liều chậm để giảm tác dụng phụ. Không ngừng đột ngột (có thể gây co giật, ảo giác)."
        },
        "side_effects": [
            "Buồn ngủ (phổ biến)",
            "Chóng mặt",
            "Yếu cơ (phổ biến)",
            "Mệt mỏi",
            "Buồn nôn",
            "Hạ huyết áp",
            "Lú lẫn (đặc biệt ở người cao tuổi)",
            "Suy hô hấp (hiếm, đặc biệt khi dùng intrathecal)",
            "Co giật khi ngừng đột ngột"
        ],
        "interactions": [
            "Alcohol: tăng tác dụng ức chế hệ thần kinh trung ương, suy hô hấp",
            "Opioids: tăng tác dụng ức chế hệ thần kinh trung ương, suy hô hấp",
            "Benzodiazepines: tăng tác dụng ức chế hệ thần kinh trung ương",
            "Antihypertensives: tăng nguy cơ hạ huyết áp",
            "MAO inhibitors: tăng nguy cơ tác dụng phụ"
        ],
        "pregnancy": "C",
        "mechanism_of_action": "Baclofen là GABA-B receptor agonist, kích thích thụ thể GABA-B ở tủy sống và não. GABA-B receptors là thụ thể G-protein coupled, khi được kích thích sẽ ức chế phóng thích chất dẫn truyền thần kinh kích thích (glutamate) và tăng phóng thích chất dẫn truyền thần kinh ức chế (GABA). Ở tủy sống, baclofen ức chế phản xạ kéo dãn (stretch reflex), giảm co cứng cơ (spasticity). Tác dụng: điều trị co cứng cơ (spasticity) trong đa xơ cứng, chấn thương tủy sống, và bại não. Có dạng uống (PO) và dạng intrathecal (tiêm vào khoang dưới nhện, qua pump). Tác dụng phụ: buồn ngủ, chóng mặt, yếu cơ (phổ biến), suy hô hấp (hiếm, đặc biệt khi dùng intrathecal), co giật khi ngừng đột ngột.",
        "monitoring": [
            "Đáp ứng điều trị: giảm co cứng cơ, cải thiện chức năng vận động",
            "Dấu hiệu suy hô hấp: thở chậm, thở nông, giảm SpO2 (đặc biệt khi dùng intrathecal)",
            "Dấu hiệu quá liều: buồn ngủ nặng, lú lẫn, hôn mê, suy hô hấp",
            "Yếu cơ - phổ biến, có thể ảnh hưởng đến khả năng đi lại",
            "Hạ huyết áp - đặc biệt khi bắt đầu hoặc tăng liều",
            "Dấu hiệu cai khi ngừng đột ngột: co giật, ảo giác, lo âu, mất ngủ",
            "Tương tác với alcohol, opioids, benzodiazepines, antihypertensives"
        ],
        "precautions": [
            "Suy hô hấp - hiếm nhưng nguy hiểm, đặc biệt khi dùng intrathecal, theo dõi hô hấp chặt chẽ",
            "Yếu cơ - phổ biến, có thể ảnh hưởng đến khả năng đi lại, cân nhắc giảm liều",
            "Hạ huyết áp - đặc biệt khi bắt đầu hoặc tăng liều, đứng dậy chậm, uống đủ nước",
            "Lú lẫn - đặc biệt ở người cao tuổi, giảm liều",
            "Tăng liều chậm để giảm tác dụng phụ (đặc biệt buồn ngủ, yếu cơ)",
            "Tránh rượu - tăng tác dụng ức chế hệ thần kinh trung ương, suy hô hấp",
            "Tránh opioids - tăng nguy cơ suy hô hấp (nguy hiểm)",
            "Thận trọng khi dùng với benzodiazepines - tăng tác dụng ức chế hệ thần kinh trung ương",
            "Thận trọng khi dùng với antihypertensives - tăng nguy cơ hạ huyết áp",
            "Dạng intrathecal - dùng cho co cứng cơ nặng không đáp ứng với PO, cần pump và theo dõi chặt chẽ",
            "KHÔNG ngừng đột ngột (có thể gây co giật, ảo giác, lo âu, mất ngủ) - giảm liều dần (tapering)"
        ],
        "pharmacokinetics": {
            "half_life": "2-4 giờ",
            "onset": "1-2 giờ (PO)",
            "duration": "4-8 giờ (PO)",
            "protein_binding": "30%",
            "clearance": "Thận: bài tiết chủ yếu nguyên dạng (70-80%). Gan: chuyển hóa một phần. Cần điều chỉnh liều ở suy thận."
        },
        "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm, tránh ánh sáng. Viên nén: bảo quản trong bao bì kín.",
        "black_box_warnings": "Nguy cơ suy hô hấp, đặc biệt khi dùng với opioids hoặc alcohol. Nguy cơ co giật khi ngừng đột ngột - phải giảm liều dần (tapering).",
        "drug_interactions": {
            "major": [
                {
                    "drug": "Alcohol",
                    "mechanism": "Tăng tác dụng ức chế hệ thần kinh trung ương",
                    "effect": "Tăng buồn ngủ, chóng mặt, suy hô hấp (nguy hiểm)",
                    "management": "Tránh hoặc giảm rượu. Cảnh báo bệnh nhân về nguy cơ suy hô hấp."
                },
                {
                    "drug": "Opioids (Morphine, Fentanyl, Oxycodone)",
                    "mechanism": "Tăng tác dụng ức chế hệ thần kinh trung ương",
                    "effect": "Tăng nguy cơ suy hô hấp (nguy hiểm, có thể tử vong)",
                    "management": "Tránh dùng cùng nếu có thể. Nếu bắt buộc, giảm liều cả hai thuốc, theo dõi hô hấp chặt chẽ."
                }
            ],
            "moderate": [
                {
                    "drug": "Benzodiazepines (Diazepam, Lorazepam)",
                    "mechanism": "Tăng tác dụng ức chế hệ thần kinh trung ương",
                    "effect": "Tăng buồn ngủ, chóng mặt, suy hô hấp",
                    "management": "Thận trọng. Có thể cần giảm liều một trong hai thuốc. Theo dõi hô hấp."
                },
                {
                    "drug": "Antihypertensives",
                    "mechanism": "Cả hai đều có thể gây hạ huyết áp",
                    "effect": "Tăng nguy cơ hạ huyết áp tư thế, ngất",
                    "management": "Thận trọng. Có thể cần giảm liều một trong hai thuốc. Theo dõi huyết áp."
                }
            ]
        },
        "contraindications": {
            "tuyệt_đối": [
                "Dị ứng baclofen hoặc các thành phần khác",
                "Suy thận nặng (CrCl <30) - giảm thải trừ, tăng nguy cơ tích lũy"
            ],
            "tương_đối": [
                "Bệnh thận (CrCl 30-60) - giảm thải trừ, giảm liều 25-50%",
                "Bệnh gan nặng - giảm chuyển hóa, tăng nguy cơ tích lũy",
                "Suy hô hấp - tăng nguy cơ suy hô hấp",
                "Người cao tuổi - tăng nguy cơ tác dụng phụ, lú lẫn, giảm liều 50%",
                "Mang thai (nguy cơ dị tật bẩm sinh) - chỉ dùng nếu lợi ích > nguy cơ",
                "Dùng với alcohol hoặc opioids - tăng nguy cơ suy hô hấp",
                "Dùng với benzodiazepines - tăng tác dụng ức chế hệ thần kinh trung ương"
            ]
        },
        "pregnancy_lactation": {
            "fda_category": "C",
            "pregnancy_details": "Chứng cứ về an toàn trong thai kỳ còn hạn chế. Một số nghiên cứu gợi ý tăng nhẹ nguy cơ dị tật bẩm sinh, nhưng chứng cứ không rõ ràng. Trẻ sơ sinh có thể có withdrawal syndrome (khó chịu, run, khó thở, co giật) nếu mẹ dùng baclofen trong thai kỳ, đặc biệt gần cuối thai kỳ. Chỉ dùng nếu lợi ích điều trị vượt trội nguy cơ. Nếu dùng trong thai kỳ, cần tư vấn di truyền và theo dõi chặt chẽ. Theo dõi trẻ sơ sinh về dấu hiệu withdrawal.",
            "lactation": {
                "safety": "Compatible with monitoring",
                "details": "Baclofen bài tiết vào sữa mẹ ở nồng độ thấp. Nồng độ trong máu trẻ sơ sinh rất thấp. Tác dụng phụ ở trẻ rất hiếm nhưng có thể có buồn ngủ nhẹ.",
                "recommendation": "Có thể cho con bú nhưng cần theo dõi trẻ về dấu hiệu tác dụng phụ (buồn ngủ, bú kém)."
            }
        },
        "hepatic_adjustment": {
            "mild": "Không cần điều chỉnh liều",
            "moderate": "Giảm liều 25-50%, theo dõi tác dụng phụ",
            "severe": "Giảm liều 50%, theo dõi tác dụng phụ chặt chẽ. Hoặc tránh dùng nếu có thể.",
            "notes": "Baclofen chuyển hóa một phần ở gan. Suy gan làm giảm chuyển hóa, tăng nguy cơ tích lũy và tác dụng phụ."
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "Giảm liều 25-50%, theo dõi tác dụng phụ",
            "under_30": "Giảm liều 50%, theo dõi tác dụng phụ chặt chẽ. Hoặc tránh dùng nếu có thể.",
            "notes": "Baclofen bài tiết chủ yếu qua thận (70-80% nguyên dạng). Suy thận làm giảm thải trừ, tăng nguy cơ tích lũy và tác dụng phụ."
        },
        "overdose_management": {
            "symptoms": [
                "Triệu chứng thần kinh: buồn ngủ nặng, lú lẫn, hôn mê",
                "Rối loạn hô hấp: suy hô hấp (nguy hiểm, có thể tử vong)",
                "Rối loạn tim mạch: hạ huyết áp, nhịp chậm",
                "Rối loạn tiêu hóa: buồn nôn, nôn"
            ],
            "antidote": "Không có antidote đặc hiệu. Điều trị hỗ trợ",
            "treatment": [
                "Đánh giá đường thở, hô hấp, tuần hoàn. Hỗ trợ hô hấp nếu cần (quan trọng, có thể cần thở máy)",
                "Rửa dạ dày nếu trong vòng 1-2 giờ sau uống (nếu bệnh nhân tỉnh táo)",
                "Than hoạt tính: 1g/kg (tối đa 50-100g) nếu trong vòng 1-2 giờ",
                "Theo dõi liên tục: ý thức, hô hấp (quan trọng), tim mạch, huyết áp",
                "Hỗ trợ hô hấp: thở máy nếu suy hô hấp",
                "Xử trí hạ huyết áp: IV fluids, vasopressors nếu cần",
                "Theo dõi ít nhất 24 giờ"
            ],
            "monitoring": "Theo dõi ý thức, hô hấp (quan trọng), tim mạch, huyết áp"
        },
        "reversal_agents": {
            "available": False,
            "agents": []
        },
        "administration_instructions": {
            "oral": {
                "with_food": "Có thể dùng với hoặc không có thức ăn. Dùng với thức ăn có thể giảm buồn nôn.",
                "timing": "Chia 3-4 lần/ngày. Uống cùng thời điểm mỗi ngày. Tăng liều chậm (mỗi 3-7 ngày) để giảm tác dụng phụ. KHÔNG ngừng đột ngột (có thể gây co giật, ảo giác, lo âu, mất ngủ) - giảm liều dần (tapering)."
            },
            "intrathecal": {
                "reconstitution": "Dạng intrathecal: pha loãng trong sterile solution.",
                "infusion_rate": "Truyền liên tục qua pump. Bắt đầu với test dose, sau đó điều chỉnh liều.",
                "compatibility": [],
                "incompatibility": [],
                "notes": "Dạng intrathecal: dùng cho co cứng cơ nặng không đáp ứng với PO, cần pump và theo dõi chặt chẽ. Nguy cơ suy hô hấp cao hơn PO."
            }
        },
        "references": {
            "primary_sources": [
                "Lexicomp - Baclofen",
                "UpToDate - Baclofen: Drug information",
                "FDA - Lioresal (baclofen) prescribing information",
                "Goodman & Gilman's The Pharmacological Basis of Therapeutics, 13th ed."
            ],
            "last_updated": "2024-12-19",
            "evidence_level": "A - Evidence from well-designed randomized controlled trials and systematic reviews"
        }
    },
    "Tizanidine": {
        "group": "Neurology - Muscle Relaxant (Alpha-2 Adrenergic Agonist)",
        "vietnamese_name": "Tizanidine, Zanaflex",
        "administration": ["PO"],
        "indications": [
            "Co cứng cơ (spasticity) - đa xơ cứng, chấn thương tủy sống",
            "Co cứng cơ do bại não",
            "Đau cơ xương (off-label)"
        ],
        "contraindications": [
            "Dị ứng",
            "Dùng với ciprofloxacin hoặc fluvoxamine (tăng nguy cơ tác dụng phụ nặng)"
        ],
        "dosage": {
            "adult_spasticity": "2-4mg x 3 lần/ngày, tăng dần đến 8mg x 3 lần/ngày (tối đa 36mg/ngày)",
            "adult_max": "36mg/ngày",
            "notes": "Alpha-2 adrenergic agonist. Tác dụng ngắn (3-6 giờ). Tăng liều chậm để giảm tác dụng phụ. CHỐNG CHỈ ĐỊNH với ciprofloxacin hoặc fluvoxamine."
        },
        "side_effects": [
            "Buồn ngủ (phổ biến)",
            "Chóng mặt",
            "Khô miệng (phổ biến)",
            "Yếu cơ",
            "Mệt mỏi",
            "Hạ huyết áp (phổ biến)",
            "Nhịp chậm",
            "Lú lẫn (đặc biệt ở người cao tuổi)",
            "Tăng ALT/AST (hiếm)"
        ],
        "interactions": [
            "Ciprofloxacin: CHỐNG CHỈ ĐỊNH - tăng nồng độ tizanidine, tăng nguy cơ tác dụng phụ nặng",
            "Fluvoxamine: CHỐNG CHỈ ĐỊNH - tăng nồng độ tizanidine, tăng nguy cơ tác dụng phụ nặng",
            "CYP1A2 inhibitors: tăng nồng độ tizanidine",
            "CYP1A2 inducers: giảm nồng độ tizanidine",
            "Alcohol: tăng tác dụng ức chế hệ thần kinh trung ương",
            "Antihypertensives: tăng nguy cơ hạ huyết áp",
            "Oral contraceptives: tăng nồng độ tizanidine"
        ],
        "pregnancy": "C",
        "mechanism_of_action": "Tizanidine là alpha-2 adrenergic agonist, kích thích thụ thể alpha-2 adrenergic ở tủy sống và não. Alpha-2 receptors là thụ thể G-protein coupled, khi được kích thích sẽ ức chế phóng thích chất dẫn truyền thần kinh kích thích (norepinephrine) và tăng phóng thích chất dẫn truyền thần kinh ức chế (GABA). Ở tủy sống, tizanidine ức chế phản xạ kéo dãn (stretch reflex), giảm co cứng cơ (spasticity). Tác dụng: điều trị co cứng cơ (spasticity) trong đa xơ cứng, chấn thương tủy sống, và bại não. Có dạng uống (PO). Tác dụng ngắn (3-6 giờ), cần dùng nhiều lần/ngày. Tác dụng phụ: buồn ngủ, chóng mặt, khô miệng (phổ biến), hạ huyết áp (phổ biến), nhịp chậm, tăng ALT/AST (hiếm).",
        "monitoring": [
            "Đáp ứng điều trị: giảm co cứng cơ, cải thiện chức năng vận động",
            "Huyết áp - hạ huyết áp phổ biến, đặc biệt khi bắt đầu hoặc tăng liều",
            "Nhịp tim - nhịp chậm, đặc biệt khi bắt đầu hoặc tăng liều",
            "Dấu hiệu quá liều: buồn ngủ nặng, lú lẫn, hạ huyết áp nặng, nhịp chậm",
            "ALT/AST - tăng ALT/AST hiếm, theo dõi định kỳ",
            "Tương tác với ciprofloxacin, fluvoxamine (CHỐNG CHỈ ĐỊNH), CYP1A2 inhibitors/inducers, oral contraceptives"
        ],
        "precautions": [
            "CHỐNG CHỈ ĐỊNH với ciprofloxacin hoặc fluvoxamine - tăng nồng độ tizanidine, tăng nguy cơ tác dụng phụ nặng (hạ huyết áp nặng, nhịp chậm, suy hô hấp)",
            "Hạ huyết áp - phổ biến, đặc biệt khi bắt đầu hoặc tăng liều, đứng dậy chậm, uống đủ nước",
            "Nhịp chậm - đặc biệt khi bắt đầu hoặc tăng liều, theo dõi nhịp tim",
            "Lú lẫn - đặc biệt ở người cao tuổi, giảm liều",
            "Tăng liều chậm để giảm tác dụng phụ (đặc biệt hạ huyết áp, buồn ngủ)",
            "Tránh rượu - tăng tác dụng ức chế hệ thần kinh trung ương",
            "Thận trọng khi dùng với CYP1A2 inhibitors (fluvoxamine, ciprofloxacin) - CHỐNG CHỈ ĐỊNH với fluvoxamine và ciprofloxacin",
            "Thận trọng khi dùng với CYP1A2 inducers (carbamazepine, smoking) - giảm nồng độ tizanidine, có thể cần tăng liều",
            "Thận trọng khi dùng với oral contraceptives - tăng nồng độ tizanidine, giảm liều tizanidine 50%",
            "Thận trọng khi dùng với antihypertensives - tăng nguy cơ hạ huyết áp",
            "Hút thuốc - giảm nồng độ tizanidine, có thể cần tăng liều ở người hút thuốc"
        ],
        "pharmacokinetics": {
            "half_life": "2-4 giờ",
            "onset": "1-2 giờ (PO)",
            "duration": "3-6 giờ (PO)",
            "protein_binding": "30%",
            "clearance": "Gan: chuyển hóa qua CYP1A2 (chính). Thận: bài tiết một phần nguyên dạng và metabolites. Cần điều chỉnh liều khi dùng với CYP1A2 inhibitors/inducers và oral contraceptives."
        },
        "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm, tránh ánh sáng. Viên nén: bảo quản trong bao bì kín.",
        "black_box_warnings": "CHỐNG CHỈ ĐỊNH với ciprofloxacin hoặc fluvoxamine - tăng nồng độ tizanidine, tăng nguy cơ tác dụng phụ nặng (hạ huyết áp nặng, nhịp chậm, suy hô hấp).",
        "drug_interactions": {
            "major": [
                {
                    "drug": "Ciprofloxacin",
                    "mechanism": "Ức chế chuyển hóa tizanidine qua CYP1A2, tăng nồng độ tizanidine",
                    "effect": "Tăng nồng độ tizanidine 10-33 lần, tăng nguy cơ tác dụng phụ nặng (hạ huyết áp nặng, nhịp chậm, suy hô hấp)",
                    "management": "CHỐNG CHỈ ĐỊNH - không được dùng cùng. Nếu đang dùng tizanidine, ngừng tizanidine ít nhất 2 tuần trước khi dùng ciprofloxacin."
                },
                {
                    "drug": "Fluvoxamine",
                    "mechanism": "Ức chế chuyển hóa tizanidine qua CYP1A2, tăng nồng độ tizanidine",
                    "effect": "Tăng nồng độ tizanidine 10-33 lần, tăng nguy cơ tác dụng phụ nặng (hạ huyết áp nặng, nhịp chậm, suy hô hấp)",
                    "management": "CHỐNG CHỈ ĐỊNH - không được dùng cùng. Nếu đang dùng tizanidine, ngừng tizanidine ít nhất 2 tuần trước khi dùng fluvoxamine."
                },
                {
                    "drug": "Other CYP1A2 inhibitors (Cimetidine, Acyclovir)",
                    "mechanism": "Ức chế chuyển hóa tizanidine qua CYP1A2, tăng nồng độ tizanidine",
                    "effect": "Tăng nồng độ tizanidine, tăng tác dụng phụ (hạ huyết áp, nhịp chậm)",
                    "management": "Tránh dùng cùng nếu có thể. Nếu bắt buộc, giảm liều tizanidine 50-75%. Theo dõi tác dụng phụ chặt chẽ."
                }
            ],
            "moderate": [
                {
                    "drug": "CYP1A2 inducers (Carbamazepine, Smoking)",
                    "mechanism": "Cảm ứng chuyển hóa tizanidine qua CYP1A2, giảm nồng độ tizanidine",
                    "effect": "Giảm nồng độ tizanidine, giảm hiệu quả",
                    "management": "Tăng liều tizanidine 50-100% khi dùng với carbamazepine hoặc ở người hút thuốc. Theo dõi đáp ứng điều trị."
                },
                {
                    "drug": "Oral contraceptives",
                    "mechanism": "Ức chế chuyển hóa tizanidine qua CYP1A2, tăng nồng độ tizanidine",
                    "effect": "Tăng nồng độ tizanidine, tăng tác dụng phụ",
                    "management": "Giảm liều tizanidine 50% khi dùng với oral contraceptives. Theo dõi tác dụng phụ."
                },
                {
                    "drug": "Antihypertensives",
                    "mechanism": "Cả hai đều có thể gây hạ huyết áp",
                    "effect": "Tăng nguy cơ hạ huyết áp tư thế, ngất",
                    "management": "Thận trọng. Có thể cần giảm liều một trong hai thuốc. Theo dõi huyết áp."
                }
            ]
        },
        "contraindications": {
            "tuyệt_đối": [
                "Dị ứng tizanidine hoặc các thành phần khác",
                "Dùng với ciprofloxacin - CHỐNG CHỈ ĐỊNH",
                "Dùng với fluvoxamine - CHỐNG CHỈ ĐỊNH"
            ],
            "tương_đối": [
                "Bệnh gan nặng - giảm chuyển hóa, tăng nguy cơ tích lũy",
                "Bệnh thận nặng - giảm thải trừ, tăng nguy cơ tích lũy",
                "Bệnh tim mạch (suy tim, loạn nhịp) - tăng nguy cơ hạ huyết áp, nhịp chậm",
                "Người cao tuổi - tăng nguy cơ tác dụng phụ, lú lẫn, hạ huyết áp, giảm liều 50%",
                "Mang thai (nguy cơ dị tật bẩm sinh) - chỉ dùng nếu lợi ích > nguy cơ",
                "Dùng với CYP1A2 inhibitors (trừ ciprofloxacin, fluvoxamine) - giảm liều tizanidine",
                "Dùng với CYP1A2 inducers hoặc hút thuốc - tăng liều tizanidine",
                "Dùng với oral contraceptives - giảm liều tizanidine 50%",
                "Dùng với antihypertensives - tăng nguy cơ hạ huyết áp"
            ]
        },
        "pregnancy_lactation": {
            "fda_category": "C",
            "pregnancy_details": "Chứng cứ về an toàn trong thai kỳ còn hạn chế. Một số nghiên cứu gợi ý tăng nhẹ nguy cơ dị tật bẩm sinh, nhưng chứng cứ không rõ ràng. Chỉ dùng nếu lợi ích điều trị vượt trội nguy cơ. Nếu dùng trong thai kỳ, cần tư vấn di truyền và theo dõi chặt chẽ.",
            "lactation": {
                "safety": "Compatible with monitoring",
                "details": "Tizanidine bài tiết vào sữa mẹ ở nồng độ thấp. Nồng độ trong máu trẻ sơ sinh rất thấp. Tác dụng phụ ở trẻ rất hiếm nhưng có thể có buồn ngủ nhẹ.",
                "recommendation": "Có thể cho con bú nhưng cần theo dõi trẻ về dấu hiệu tác dụng phụ (buồn ngủ, bú kém)."
            }
        },
        "hepatic_adjustment": {
            "mild": "Không cần điều chỉnh liều",
            "moderate": "Giảm liều 25-50%, theo dõi tác dụng phụ",
            "severe": "Giảm liều 50%, theo dõi tác dụng phụ chặt chẽ. Hoặc tránh dùng nếu có thể.",
            "notes": "Tizanidine chuyển hóa ở gan qua CYP1A2. Suy gan làm giảm chuyển hóa, tăng nguy cơ tích lũy và tác dụng phụ."
        },
        "overdose_management": {
            "symptoms": [
                "Triệu chứng thần kinh: buồn ngủ nặng, lú lẫn, hôn mê",
                "Rối loạn tim mạch: hạ huyết áp nặng, nhịp chậm",
                "Rối loạn hô hấp: suy hô hấp (hiếm)",
                "Rối loạn tiêu hóa: buồn nôn, nôn"
            ],
            "antidote": "Không có antidote đặc hiệu. Điều trị hỗ trợ",
            "treatment": [
                "Đánh giá đường thở, hô hấp, tuần hoàn. Hỗ trợ hô hấp nếu cần",
                "Rửa dạ dày nếu trong vòng 1-2 giờ sau uống (nếu bệnh nhân tỉnh táo)",
                "Than hoạt tính: 1g/kg (tối đa 50-100g) nếu trong vòng 1-2 giờ",
                "Theo dõi liên tục: ý thức, hô hấp, tim mạch, huyết áp (quan trọng)",
                "Xử trí hạ huyết áp: IV fluids, vasopressors nếu cần",
                "Xử trí nhịp chậm: Atropine nếu cần",
                "Hỗ trợ hô hấp: thở máy nếu suy hô hấp",
                "Theo dõi ít nhất 24 giờ"
            ],
            "monitoring": "Theo dõi ý thức, hô hấp, tim mạch, huyết áp (quan trọng), nhịp tim"
        },
        "reversal_agents": {
            "available": False,
            "agents": []
        },
        "administration_instructions": {
            "oral": {
                "with_food": "Có thể dùng với hoặc không có thức ăn. Dùng với thức ăn có thể giảm buồn nôn.",
                "timing": "Chia 3 lần/ngày. Uống cùng thời điểm mỗi ngày. Tăng liều chậm để giảm tác dụng phụ (đặc biệt hạ huyết áp, buồn ngủ)."
            },
            "im": {
                "reconstitution": "Không có dạng IM",
                "infusion_rate": "N/A",
                "compatibility": [],
                "incompatibility": [],
                "notes": "Chỉ có dạng uống"
            },
            "iv": {
                "reconstitution": "Không có dạng IV",
                "infusion_rate": "N/A",
                "compatibility": [],
                "incompatibility": [],
                "notes": "Chỉ có dạng uống"
            }
        },
        "references": {
            "primary_sources": [
                "Lexicomp - Tizanidine",
                "UpToDate - Tizanidine: Drug information",
                "FDA - Zanaflex (tizanidine) prescribing information",
                "Goodman & Gilman's The Pharmacological Basis of Therapeutics, 13th ed."
            ],
            "last_updated": "2024-12-19",
            "evidence_level": "A - Evidence from well-designed randomized controlled trials and systematic reviews"
        }
    }
}

__all__ = ['MUSCLE_RELAXANTS_DRUGS']





















