"""
SNRI (Serotonin-Norepinephrine Reuptake Inhibitor) Drugs
"""

SNRI_DRUGS = {
    "Venlafaxine": {
        "group": "Psychiatry - SNRI (Serotonin-Norepinephrine Reuptake Inhibitor)",
        "vietnamese_name": "Venlafaxine, Effexor",
        "administration": ["PO"],
        "indications": [
            "Trầm cảm",
            "Rối loạn lo âu tổng quát (GAD)",
            "Rối loạn hoảng sợ",
            "Rối loạn lo âu xã hội"
        ],
        "contraindications": [
            "Dùng MAO inhibitor",
            "Tăng huyết áp không kiểm soát",
            "Dị ứng"
        ],
        "dosage": {
            "adult_standard": "37.5-75mg x 2 lần/ngày (immediate) hoặc 75-150mg x 1 lần/ngày (extended release)",
            "adult_max": "225mg/ngày (immediate) hoặc 225mg/ngày (extended release)",
            "notes": "Extended release: uống 1 lần/ngày, thuận tiện hơn"
        },
        "side_effects": [
            "Buồn nôn",
            "Tăng huyết áp (liều cao)",
            "Mất ngủ",
            "Chóng mặt",
            "Giảm ham muốn tình dục",
            "Tăng nhịp tim",
            "Khó chịu khi ngừng (withdrawal)"
        ],
        "interactions": [
            "MAO inhibitor: chống chỉ định",
            "Warfarin: có thể tăng tác dụng",
            "Tramadol: tăng nguy cơ co giật và hội chứng serotonin"
        ],
        "pregnancy": "C",
        "mechanism_of_action": "Venlafaxine là thuốc chống trầm cảm thuộc nhóm SNRI (serotonin-norepinephrine reuptake inhibitor), ức chế tái hấp thu serotonin và norepinephrine ở synap thần kinh. Ở liều thấp (<75mg/ngày), venlafaxine chủ yếu ức chế tái hấp thu serotonin (giống SSRI). Ở liều trung bình (75-225mg/ngày), venlafaxine ức chế cả serotonin và norepinephrine. Ở liều cao (>225mg/ngày), venlafaxine cũng có thể ức chế tái hấp thu dopamine nhẹ. Bằng cách ức chế tái hấp thu, venlafaxine làm tăng nồng độ serotonin và norepinephrine trong synap, dẫn đến tăng hoạt động của các chất dẫn truyền thần kinh này và cải thiện triệu chứng trầm cảm và lo âu. Venlafaxine có tác dụng mạnh hơn SSRI trong một số trường hợp, đặc biệt trầm cảm nặng và kháng trị. Tác dụng phụ chính: tăng huyết áp ở liều cao do ức chế norepinephrine. Venlafaxine có dạng extended release (ER) cho phép dùng 1 lần/ngày.",
        "monitoring": [
            "Đáp ứng điều trị (giảm triệu chứng trầm cảm, lo âu) - đánh giá sau 2-4 tuần",
            "Huyết áp - tăng huyết áp ở liều cao (>150mg/ngày), đặc biệt ở bệnh nhân có tăng huyết áp",
            "Nhịp tim - tăng nhịp tim có thể xảy ra",
            "Dấu hiệu hội chứng serotonin (sốt, kích động, run, nhịp tim nhanh, co giật) - đặc biệt khi dùng với tramadol, MAO inhibitor",
            "Dấu hiệu withdrawal (khó chịu, buồn nôn, chóng mặt, lo âu, mất ngủ) - khi ngừng đột ngột",
            "Tác dụng phụ (buồn nôn, mất ngủ, chóng mặt, giảm ham muốn tình dục)",
            "Tương tác với MAO inhibitor (chống chỉ định), warfarin (tăng INR), tramadol (tăng nguy cơ co giật và hội chứng serotonin)"
        ],
        "precautions": [
            "CHỐNG CHỈ ĐỊNH với MAO inhibitor - phải ngừng MAO inhibitor ít nhất 14 ngày trước khi bắt đầu venlafaxine (nguy cơ hội chứng serotonin nghiêm trọng)",
            "Không ngừng đột ngột - giảm liều dần dần trong ít nhất 2 tuần (nguy cơ withdrawal syndrome: khó chịu, buồn nôn, chóng mặt, lo âu, mất ngủ)",
            "Tăng huyết áp - nguy cơ tăng ở liều cao (>150mg/ngày), đặc biệt ở bệnh nhân có tăng huyết áp, cần theo dõi huyết áp",
            "Tăng nhịp tim - có thể xảy ra, thận trọng ở bệnh nhân có bệnh tim",
            "Nguy cơ hội chứng serotonin - đặc biệt khi dùng với tramadol, triptans, MAO inhibitor, SSRI",
            "Tăng nguy cơ tự sát - đặc biệt ở trẻ em, thanh thiếu niên, và người trẻ tuổi (<25 tuổi) trong vài tuần đầu",
            "Buồn nôn - tác dụng phụ phổ biến nhất, thường tự khỏi sau vài tuần, có thể giảm bằng cách uống với thức ăn",
            "Mất ngủ - có thể xảy ra, cân nhắc dùng vào buổi sáng",
            "Giảm ham muốn tình dục - tác dụng phụ phổ biến, có thể kéo dài",
            "Dạng extended release (ER) - uống 1 lần/ngày, thuận tiện hơn, ít tác dụng phụ hơn",
            "Dùng với thức ăn để giảm buồn nôn",
            "Thận trọng ở bệnh nhân có bệnh gan, suy thận (có thể cần giảm liều)"
        ],
        "pharmacokinetics": {
            "half_life": "5 giờ (venlafaxine), 11 giờ (desvenlafaxine - metabolite hoạt động)",
            "onset": "2-4 tuần (tác dụng chống trầm cảm)",
            "duration": "12-24 giờ (dùng 1-2 lần/ngày)",
            "protein_binding": "27-30%",
            "clearance": "Gan: chuyển hóa qua CYP2D6 thành desvenlafaxine (metabolite hoạt động, mạnh hơn venlafaxine). Thận: bài tiết một phần nguyên dạng và metabolites. Cần điều chỉnh liều ở suy thận và suy gan nặng."
        },
        "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm, tránh ánh sáng. Viên nén: bảo quản trong bao bì kín. Dạng extended release: bảo quản tương tự, không nghiền hoặc nhai (phải uống nguyên viên).",
        "black_box_warnings": "Nguy cơ tự sát và hành vi tự sát ở trẻ em, thanh thiếu niên, và người trẻ tuổi (<25 tuổi) với các thuốc chống trầm cảm. Nguy cơ tăng trong vài tháng đầu điều trị và khi tăng liều. Theo dõi chặt chẽ dấu hiệu tự sát, thay đổi hành vi, lo âu, kích động, mất ngủ, hoặc các triệu chứng mới hoặc nặng hơn. Nguy cơ hội chứng serotonin khi dùng với MAO inhibitor, tramadol, triptans.",
        "drug_interactions": {
            "major": [
                {
                    "drug": "MAO inhibitors (phenelzine, tranylcypromine, selegiline)",
                    "mechanism": "Ức chế chuyển hóa serotonin, tăng nồng độ serotonin",
                    "effect": "Nguy cơ hội chứng serotonin nghiêm trọng, có thể tử vong (sốt, kích động, run, nhịp tim nhanh, co giật, hôn mê)",
                    "management": "CHỐNG CHỈ ĐỊNH. Phải ngừng MAO inhibitor ít nhất 14 ngày trước khi bắt đầu venlafaxine. Phải ngừng venlafaxine ít nhất 7 ngày trước khi bắt đầu MAO inhibitor."
                },
                {
                    "drug": "Tramadol",
                    "mechanism": "Cả hai đều tăng serotonin, tăng nguy cơ hội chứng serotonin",
                    "effect": "Nguy cơ hội chứng serotonin và co giật",
                    "management": "Tránh dùng chung nếu có thể. Nếu phải dùng, theo dõi chặt chẽ dấu hiệu hội chứng serotonin. Giảm liều tramadol."
                },
                {
                    "drug": "Warfarin",
                    "mechanism": "Venlafaxine có thể ức chế CYP2C9 nhẹ, tăng nồng độ warfarin",
                    "effect": "Tăng INR, tăng nguy cơ chảy máu",
                    "management": "Theo dõi INR thường xuyên. Có thể cần giảm liều warfarin."
                }
            ],
            "moderate": [
                {
                    "drug": "Triptans (sumatriptan, rizatriptan)",
                    "mechanism": "Cả hai đều tăng serotonin",
                    "effect": "Tăng nguy cơ hội chứng serotonin",
                    "management": "Thận trọng, theo dõi dấu hiệu hội chứng serotonin. Có thể cần giảm liều triptan hoặc tăng khoảng cách giữa các liều."
                },
                {
                    "drug": "Lithium",
                    "mechanism": "Tăng serotonin",
                    "effect": "Tăng nguy cơ hội chứng serotonin",
                    "management": "Theo dõi dấu hiệu hội chứng serotonin. Có thể cần giảm liều lithium."
                },
                {
                    "drug": "Cimetidine",
                    "mechanism": "Ức chế CYP2D6, giảm chuyển hóa venlafaxine",
                    "effect": "Tăng nồng độ venlafaxine",
                    "management": "Giảm liều venlafaxine 25-50%. Theo dõi tác dụng phụ."
                }
            ],
            "minor": [
                {
                    "drug": "Metoclopramide",
                    "mechanism": "Cả hai đều tăng serotonin nhẹ",
                    "effect": "Tăng nhẹ nguy cơ hội chứng serotonin",
                    "management": "Theo dõi dấu hiệu hội chứng serotonin. Thường không cần điều chỉnh liều."
                }
            ]
        },
        "contraindications": {
            "tuyệt_đối": [
                "Dùng MAO inhibitor (trong vòng 14 ngày)",
                "Dị ứng venlafaxine hoặc các thành phần khác"
            ],
            "tương_đối": [
                "Tăng huyết áp không kiểm soát - nguy cơ tăng huyết áp ở liều cao",
                "Bệnh tim mạch (loạn nhịp, suy tim) - tăng nhịp tim, tăng huyết áp",
                "Suy gan nặng - giảm chuyển hóa, tăng nguy cơ tích lũy",
                "Suy thận nặng (CrCl <30) - giảm thải trừ, tăng nguy cơ tích lũy",
                "Mang thai (nguy cơ dị tật bẩm sinh, withdrawal ở trẻ sơ sinh) - chỉ dùng nếu lợi ích > nguy cơ",
                "Tiền sử co giật - tăng nguy cơ co giật",
                "Glaucoma góc hẹp - tăng nguy cơ tăng nhãn áp",
                "Bệnh nhân lớn tuổi - tăng nguy cơ tác dụng phụ"
            ]
        },
        "pregnancy_lactation": {
            "fda_category": "C",
            "pregnancy_details": "Chứng cứ về an toàn trong thai kỳ còn hạn chế. Một số nghiên cứu gợi ý tăng nhẹ nguy cơ dị tật bẩm sinh (tim, sứt môi/hà ếch), nhưng chứng cứ không rõ ràng. Trẻ sơ sinh có thể có withdrawal syndrome (khó chịu, run, khó thở, co giật) nếu mẹ dùng venlafaxine trong thai kỳ, đặc biệt gần cuối thai kỳ. Chỉ dùng nếu lợi ích điều trị vượt trội nguy cơ. Nếu dùng trong thai kỳ, cần tư vấn di truyền và theo dõi chặt chẽ. Theo dõi trẻ sơ sinh về dấu hiệu withdrawal.",
            "lactation": {
                "safety": "Compatible with monitoring",
                "details": "Venlafaxine và desvenlafaxine bài tiết vào sữa mẹ ở nồng độ thấp đến trung bình. Nồng độ trong máu trẻ sơ sinh rất thấp (<5% nồng độ trong máu mẹ). Tác dụng phụ ở trẻ rất hiếm nhưng có thể có buồn ngủ nhẹ, kích động nhẹ.",
                "recommendation": "Có thể cho con bú nhưng cần theo dõi trẻ về dấu hiệu tác dụng phụ (buồn ngủ, kích động, bú kém)."
            }
        },
        "hepatic_adjustment": {
            "mild": "Không cần điều chỉnh liều",
            "moderate": "Giảm liều 25-50%, theo dõi tác dụng phụ",
            "severe": "Giảm liều 50%, theo dõi tác dụng phụ chặt chẽ. Hoặc tránh dùng nếu có thể.",
            "notes": "Venlafaxine chuyển hóa ở gan qua CYP2D6 thành desvenlafaxine. Suy gan làm giảm chuyển hóa, tăng nguy cơ tích lũy venlafaxine và tác dụng phụ."
        },
        "overdose_management": {
            "symptoms": [
                "Triệu chứng thần kinh: buồn ngủ, chóng mặt, lú lẫn, co giật, hôn mê",
                "Hội chứng serotonin: sốt, kích động, run, nhịp tim nhanh, tăng huyết áp, co giật",
                "Rối loạn tim mạch: nhịp nhanh, tăng huyết áp, rối loạn nhịp, QT kéo dài",
                "Rối loạn hô hấp: suy hô hấp",
                "Rối loạn tiêu hóa: buồn nôn, nôn",
                "Triệu chứng khác: giãn đồng tử, sốt"
            ],
            "antidote": "Không có antidote đặc hiệu. Cyproheptadine có thể được dùng để điều trị hội chứng serotonin (không được FDA chấp thuận).",
            "treatment": [
                "Đánh giá đường thở, hô hấp, tuần hoàn. Hỗ trợ hô hấp nếu cần",
                "Rửa dạ dày nếu trong vòng 1-2 giờ sau uống (nếu bệnh nhân tỉnh táo)",
                "Than hoạt tính: 1g/kg (tối đa 50-100g) nếu trong vòng 1-2 giờ",
                "Theo dõi liên tục: ý thức, hô hấp, tim mạch, điện tâm đồ (QT kéo dài)",
                "Xử trí hội chứng serotonin: cyproheptadine (antagonist serotonin), hạ nhiệt, benzodiazepine cho kích động, co giật",
                "Xử trí co giật: benzodiazepine (diazepam, lorazepam)",
                "Xử trí tăng huyết áp: labetalol, esmolol (beta-blocker)",
                "Hỗ trợ hô hấp: thở máy nếu suy hô hấp",
                "Theo dõi điện tâm đồ: QT kéo dài, rối loạn nhịp"
            ],
            "monitoring": "Theo dõi ý thức, hô hấp, tim mạch, điện tâm đồ (QT, nhịp tim), dấu hiệu hội chứng serotonin, nhiệt độ cơ thể"
        },
        "reversal_agents": None,
        "administration_instructions": {
            "oral": {
                "with_food": "Uống với thức ăn để giảm buồn nôn (tác dụng phụ phổ biến nhất)",
                "timing": "Dạng immediate release: chia 2-3 lần/ngày. Dạng extended release (ER): uống 1 lần/ngày vào buổi sáng hoặc tối. Uống cùng thời điểm mỗi ngày. KHÔNG nghiền hoặc nhai viên ER (phải uống nguyên viên). Không ngừng đột ngột - giảm liều dần dần trong ít nhất 2 tuần."
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
                "Lexicomp - Venlafaxine",
                "UpToDate - Venlafaxine: Drug information",
                "FDA - Effexor (venlafaxine) prescribing information",
                "Goodman & Gilman's The Pharmacological Basis of Therapeutics, 13th ed."
            ],
            "last_updated": "2024-12-19",
            "evidence_level": "A - Evidence from well-designed randomized controlled trials and systematic reviews"
        }
    },

    "Duloxetine": {
        "group": "Psychiatry - SNRI (Serotonin-Norepinephrine Reuptake Inhibitor)",
        "vietnamese_name": "Duloxetine, Cymbalta",
        "administration": ["PO"],
        "indications": [
            "Trầm cảm",
            "Rối loạn lo âu tổng quát (GAD)",
            "Đau thần kinh do tiểu đường",
            "Đau cơ xơ hóa",
            "Đau thần kinh mạn tính"
        ],
        "contraindications": [
            "Dùng MAO inhibitor",
            "Suy gan nặng",
            "Dị ứng"
        ],
        "dosage": {
            "adult_depression": "20-30mg x 2 lần/ngày hoặc 60mg x 1 lần/ngày, tăng đến 60-120mg/ngày",
            "adult_neuropathic": "60mg x 1 lần/ngày, có thể tăng đến 60mg x 2 lần/ngày",
            "adult_max": "120mg/ngày",
            "notes": "Uống với thức ăn. Không nghiền hoặc nhai viên (phải uống nguyên viên)"
        },
        "side_effects": [
            "Buồn nôn (phổ biến)",
            "Khô miệng",
            "Mất ngủ",
            "Chóng mặt",
            "Táo bón",
            "Giảm ham muốn tình dục",
            "Tăng nhịp tim",
            "Tăng huyết áp (liều cao)",
            "Tăng men gan (hiếm)"
        ],
        "interactions": [
            "MAO inhibitor: chống chỉ định",
            "Warfarin: có thể tăng tác dụng",
            "Tramadol: tăng nguy cơ co giật và hội chứng serotonin",
            "CYP1A2 inhibitors: tăng nồng độ duloxetine",
            "CYP2D6 inhibitors: tăng nồng độ duloxetine"
        ],
        "pregnancy": "C",
        "mechanism_of_action": "Duloxetine là thuốc chống trầm cảm thuộc nhóm SNRI (serotonin-norepinephrine reuptake inhibitor), ức chế tái hấp thu serotonin và norepinephrine ở synap thần kinh. Ở liều điều trị, duloxetine ức chế cả serotonin và norepinephrine với tỷ lệ tương đương. Bằng cách ức chế tái hấp thu, duloxetine làm tăng nồng độ serotonin và norepinephrine trong synap, dẫn đến tăng hoạt động của các chất dẫn truyền thần kinh này và cải thiện triệu chứng trầm cảm và lo âu. Duloxetine cũng có tác dụng giảm đau thần kinh (đau thần kinh do tiểu đường, đau cơ xơ hóa) thông qua ức chế tái hấp thu serotonin và norepinephrine ở tủy sống, giảm truyền tín hiệu đau. Tác dụng: chống trầm cảm, chống lo âu, và giảm đau thần kinh. Ưu điểm: dùng 1 lần/ngày, có tác dụng giảm đau. Tác dụng phụ: buồn nôn (phổ biến), tăng men gan (hiếm nhưng nguy hiểm).",
        "monitoring": [
            "Đáp ứng điều trị (giảm triệu chứng trầm cảm, lo âu, đau thần kinh) - đánh giá sau 2-4 tuần",
            "Tác dụng phụ tiêu hóa: buồn nôn (phổ biến nhất) - thường tự khỏi sau vài tuần",
            "Chức năng gan (ALT, AST) - tăng men gan hiếm nhưng nguy hiểm, CHỐNG CHỈ ĐỊNH trong suy gan nặng",
            "Huyết áp - tăng huyết áp ở liều cao",
            "Nhịp tim - tăng nhịp tim có thể xảy ra",
            "Dấu hiệu hội chứng serotonin (sốt, kích động, run, nhịp tim nhanh, co giật) - đặc biệt khi dùng với tramadol, MAO inhibitor",
            "Dấu hiệu withdrawal (khó chịu, buồn nôn, chóng mặt, lo âu, mất ngủ) - khi ngừng đột ngột",
            "Tương tác với MAO inhibitor (chống chỉ định), warfarin (tăng INR), tramadol (tăng nguy cơ co giật và hội chứng serotonin)"
        ],
        "precautions": [
            "CHỐNG CHỈ ĐỊNH với MAO inhibitor - phải ngừng MAO inhibitor ít nhất 14 ngày trước khi bắt đầu duloxetine",
            "CHỐNG CHỈ ĐỊNH trong suy gan nặng - tăng men gan hiếm nhưng nguy hiểm",
            "Không ngừng đột ngột - giảm liều dần dần trong ít nhất 2 tuần (nguy cơ withdrawal syndrome)",
            "Buồn nôn - tác dụng phụ phổ biến nhất, thường tự khỏi sau vài tuần, uống với thức ăn để giảm",
            "Tăng men gan - hiếm nhưng nguy hiểm, CHỐNG CHỈ ĐỊNH trong suy gan nặng, theo dõi ALT/AST",
            "Tăng huyết áp - nguy cơ tăng ở liều cao, đặc biệt ở bệnh nhân có tăng huyết áp, cần theo dõi huyết áp",
            "Tăng nhịp tim - có thể xảy ra, thận trọng ở bệnh nhân có bệnh tim",
            "Nguy cơ hội chứng serotonin - đặc biệt khi dùng với tramadol, triptans, MAO inhibitor, SSRI",
            "Tăng nguy cơ tự sát - đặc biệt ở trẻ em, thanh thiếu niên, và người trẻ tuổi (<25 tuổi) trong vài tuần đầu",
            "Uống với thức ăn để giảm buồn nôn",
            "KHÔNG nghiền hoặc nhai viên (phải uống nguyên viên) - có thể gây tác dụng phụ nghiêm trọng",
            "Thận trọng ở bệnh nhân có bệnh gan, suy thận (có thể cần giảm liều)"
        ],
        "pharmacokinetics": {
            "half_life": "12 giờ (trung bình)",
            "onset": "2-4 tuần (tác dụng chống trầm cảm), 1-2 tuần (tác dụng giảm đau)",
            "duration": "12-24 giờ (dùng 1-2 lần/ngày)",
            "protein_binding": ">90%",
            "clearance": "Gan: chuyển hóa qua CYP1A2, CYP2D6. Thận: bài tiết một phần nguyên dạng và metabolites. Cần điều chỉnh liều ở suy gan và suy thận nặng."
        },
        "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm, tránh ánh sáng. Viên nén: bảo quản trong bao bì kín. KHÔNG nghiền hoặc nhai viên (phải uống nguyên viên).",
        "black_box_warnings": "Nguy cơ tự sát và hành vi tự sát ở trẻ em, thanh thiếu niên, và người trẻ tuổi (<25 tuổi) với các thuốc chống trầm cảm. Nguy cơ tăng trong vài tháng đầu điều trị và khi tăng liều. Theo dõi chặt chẽ dấu hiệu tự sát, thay đổi hành vi, lo âu, kích động, mất ngủ, hoặc các triệu chứng mới hoặc nặng hơn. Nguy cơ hội chứng serotonin khi dùng với MAO inhibitor, tramadol, triptans. CHỐNG CHỈ ĐỊNH trong suy gan nặng - tăng men gan hiếm nhưng nguy hiểm.",
        "drug_interactions": {
            "major": [
                {
                    "drug": "MAO Inhibitors (Phenelzine, Tranylcypromine, Selegiline)",
                    "mechanism": "Ức chế chuyển hóa serotonin, tăng nồng độ serotonin",
                    "effect": "Nguy cơ hội chứng serotonin nghiêm trọng, có thể tử vong (sốt, kích động, run, nhịp tim nhanh, co giật, hôn mê)",
                    "management": "CHỐNG CHỈ ĐỊNH. Phải ngừng MAO inhibitor ít nhất 14 ngày trước khi bắt đầu duloxetine. Phải ngừng duloxetine ít nhất 7 ngày trước khi bắt đầu MAO inhibitor."
                },
                {
                    "drug": "Tramadol",
                    "mechanism": "Cả hai đều tăng serotonin, tăng nguy cơ hội chứng serotonin",
                    "effect": "Nguy cơ hội chứng serotonin và co giật",
                    "management": "Tránh dùng chung nếu có thể. Nếu phải dùng, theo dõi chặt chẽ dấu hiệu hội chứng serotonin. Giảm liều tramadol."
                },
                {
                    "drug": "CYP1A2 inhibitors (Fluvoxamine, Ciprofloxacin)",
                    "mechanism": "Ức chế chuyển hóa duloxetine, tăng nồng độ duloxetine",
                    "effect": "Tăng nồng độ duloxetine, tăng tác dụng phụ",
                    "management": "Giảm liều duloxetine 50%. Theo dõi tác dụng phụ."
                }
            ],
            "moderate": [
                {
                    "drug": "Warfarin",
                    "mechanism": "Duloxetine có thể tăng nồng độ warfarin",
                    "effect": "Tăng INR, tăng nguy cơ chảy máu",
                    "management": "Theo dõi INR thường xuyên. Có thể cần giảm liều warfarin."
                },
                {
                    "drug": "Triptans (Sumatriptan, Rizatriptan)",
                    "mechanism": "Cả hai đều tăng serotonin",
                    "effect": "Tăng nguy cơ hội chứng serotonin",
                    "management": "Thận trọng, theo dõi dấu hiệu hội chứng serotonin. Có thể cần giảm liều triptan hoặc tăng khoảng cách giữa các liều."
                },
                {
                    "drug": "CYP2D6 inhibitors (Paroxetine, Fluoxetine)",
                    "mechanism": "Ức chế chuyển hóa duloxetine",
                    "effect": "Tăng nồng độ duloxetine",
                    "management": "Thận trọng. Có thể cần giảm liều duloxetine."
                }
            ],
            "minor": [
                {
                    "drug": "Aspirin, NSAIDs",
                    "mechanism": "Cả hai đều có thể tăng nguy cơ chảy máu",
                    "effect": "Tăng nguy cơ chảy máu",
                    "management": "Thận trọng. Theo dõi dấu hiệu chảy máu."
                }
            ]
        },
        "contraindications": {
            "tuyệt_đối": [
                "Dùng MAO inhibitor (trong vòng 14 ngày)",
                "Suy gan nặng (CHỐNG CHỈ ĐỊNH do tăng men gan hiếm nhưng nguy hiểm)",
                "Dị ứng duloxetine hoặc các thành phần khác"
            ],
            "tương_đối": [
                "Suy gan nhẹ đến trung bình - giảm liều, theo dõi ALT/AST",
                "Suy thận nặng (CrCl <30) - giảm thải trừ, tăng nguy cơ tích lũy",
                "Tăng huyết áp không kiểm soát - nguy cơ tăng huyết áp ở liều cao",
                "Bệnh tim mạch (loạn nhịp, suy tim) - tăng nhịp tim, tăng huyết áp",
                "Mang thai (nguy cơ dị tật bẩm sinh, withdrawal ở trẻ sơ sinh) - chỉ dùng nếu lợi ích > nguy cơ",
                "Tiền sử co giật - tăng nguy cơ co giật",
                "Bệnh nhân lớn tuổi - tăng nguy cơ tác dụng phụ"
            ]
        },
        "pregnancy_lactation": {
            "fda_category": "C",
            "pregnancy_details": "Chứng cứ về an toàn trong thai kỳ còn hạn chế. Một số nghiên cứu gợi ý tăng nhẹ nguy cơ dị tật bẩm sinh (tim, sứt môi/hà ếch), nhưng chứng cứ không rõ ràng. Trẻ sơ sinh có thể có withdrawal syndrome (khó chịu, run, khó thở, co giật) nếu mẹ dùng duloxetine trong thai kỳ, đặc biệt gần cuối thai kỳ. Chỉ dùng nếu lợi ích điều trị vượt trội nguy cơ. Nếu dùng trong thai kỳ, cần tư vấn di truyền và theo dõi chặt chẽ. Theo dõi trẻ sơ sinh về dấu hiệu withdrawal.",
            "lactation": {
                "safety": "Compatible with monitoring",
                "details": "Duloxetine bài tiết vào sữa mẹ ở nồng độ thấp đến trung bình. Nồng độ trong máu trẻ sơ sinh rất thấp (<5% nồng độ trong máu mẹ). Tác dụng phụ ở trẻ rất hiếm nhưng có thể có buồn ngủ nhẹ, kích động nhẹ.",
                "recommendation": "Có thể cho con bú nhưng cần theo dõi trẻ về dấu hiệu tác dụng phụ (buồn ngủ, kích động, bú kém)."
            }
        },
        "hepatic_adjustment": {
            "mild": "Không cần điều chỉnh liều",
            "moderate": "Giảm liều 25-50%, theo dõi ALT/AST chặt chẽ",
            "severe": "CHỐNG CHỈ ĐỊNH - không dùng trong suy gan nặng (tăng men gan hiếm nhưng nguy hiểm)",
            "notes": "Duloxetine chuyển hóa ở gan qua CYP1A2, CYP2D6. Suy gan làm giảm chuyển hóa, tăng nguy cơ tích lũy và tăng men gan. CHỐNG CHỈ ĐỊNH trong suy gan nặng."
        },
        "overdose_management": {
            "symptoms": [
                "Triệu chứng thần kinh: buồn ngủ, chóng mặt, lú lẫn, co giật, hôn mê",
                "Hội chứng serotonin: sốt, kích động, run, nhịp tim nhanh, tăng huyết áp, co giật",
                "Rối loạn tim mạch: nhịp nhanh, tăng huyết áp, rối loạn nhịp, QT kéo dài",
                "Rối loạn hô hấp: suy hô hấp",
                "Rối loạn tiêu hóa: buồn nôn, nôn",
                "Triệu chứng khác: giãn đồng tử, sốt"
            ],
            "antidote": "Không có antidote đặc hiệu. Cyproheptadine có thể được dùng để điều trị hội chứng serotonin (không được FDA chấp thuận).",
            "treatment": [
                "Đánh giá đường thở, hô hấp, tuần hoàn. Hỗ trợ hô hấp nếu cần",
                "Rửa dạ dày nếu trong vòng 1-2 giờ sau uống (nếu bệnh nhân tỉnh táo)",
                "Than hoạt tính: 1g/kg (tối đa 50-100g) nếu trong vòng 1-2 giờ",
                "Theo dõi liên tục: ý thức, hô hấp, tim mạch, điện tâm đồ (QT kéo dài)",
                "Xử trí hội chứng serotonin: cyproheptadine (antagonist serotonin), hạ nhiệt, benzodiazepine cho kích động, co giật",
                "Xử trí co giật: benzodiazepine (diazepam, lorazepam)",
                "Xử trí tăng huyết áp: labetalol, esmolol (beta-blocker)",
                "Hỗ trợ hô hấp: thở máy nếu suy hô hấp",
                "Theo dõi điện tâm đồ: QT kéo dài, rối loạn nhịp"
            ],
            "monitoring": "Theo dõi ý thức, hô hấp, tim mạch, điện tâm đồ (QT, nhịp tim), dấu hiệu hội chứng serotonin, nhiệt độ cơ thể"
        },
        "reversal_agents": None,
        "administration_instructions": {
            "oral": {
                "with_food": "Uống với thức ăn để giảm buồn nôn (tác dụng phụ phổ biến nhất)",
                "timing": "Dùng 1-2 lần/ngày (thường 1 lần/ngày với liều 60mg). Uống cùng thời điểm mỗi ngày. KHÔNG nghiền hoặc nhai viên (phải uống nguyên viên). Không ngừng đột ngột - giảm liều dần dần trong ít nhất 2 tuần."
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
                "Lexicomp - Duloxetine",
                "UpToDate - Duloxetine: Drug information",
                "FDA - Cymbalta (duloxetine) prescribing information",
                "Goodman & Gilman's The Pharmacological Basis of Therapeutics, 13th ed."
            ],
            "last_updated": "2024-12-19",
            "evidence_level": "A - Evidence from well-designed randomized controlled trials and systematic reviews"
        }
    }
}

__all__ = ['SNRI_DRUGS']
