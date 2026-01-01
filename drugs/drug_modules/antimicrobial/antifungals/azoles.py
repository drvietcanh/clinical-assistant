"""
Azole Antifungals - Antifungal Medications
"""

AZOLES_DRUGS = {
    "Fluconazole": {
        "group": "Infectious Disease - Antifungal (Azole)",
        "vietnamese_name": "Fluconazole, Diflucan",
        "administration": ["PO", "IV"],
        "indications": [
            "Nhiễm nấm Candida (oral, esophageal, vaginal, systemic)",
            "Nhiễm nấm Cryptococcus",
            "Nhiễm nấm Coccidioidomycosis",
            "Dự phòng nhiễm nấm ở bệnh nhân suy giảm miễn dịch"
        ],
        "contraindications": [
            "Dị ứng fluconazole/azole",
            "Có thai (3 tháng đầu)",
            "Dùng terfenadine/astemizole với liều fluconazole ≥400mg/ngày"
        ],
        "dosage": {
            "adult_candidiasis_oral": "150mg x 1 lần (đơn liều) hoặc 50-100mg x 1 lần/ngày x 7-14 ngày",
            "adult_candidiasis_esophageal": "100-200mg x 1 lần/ngày x 14-21 ngày",
            "adult_candidiasis_vaginal": "150mg x 1 lần (đơn liều)",
            "adult_cryptococcal_meningitis": "400mg ngày đầu, sau đó 200-400mg x 1 lần/ngày",
            "adult_prophylaxis": "50-400mg x 1 lần/ngày",
            "notes": "Thải qua thận, cần điều chỉnh liều khi suy thận"
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "Giảm liều 50%",
            "under_30": "Giảm liều 50-75%"
        },
        "side_effects": [
            "Nhức đầu",
            "Buồn nôn, nôn",
            "Tiêu chảy",
            "Ban da",
            "Tăng men gan",
            "Rụng tóc",
            "QT kéo dài (liều cao)"
        ],
        "interactions": [
            "Warfarin: tăng tác dụng chống đông",
            "Phenytoin: tăng nồng độ phenytoin",
            "Cyclosporine: tăng nồng độ cyclosporine",
            "Sulfonylurea: tăng nguy cơ hạ đường huyết",
            "Rifampin: giảm nồng độ fluconazole"
        ],
        "pregnancy": "C - D trong 3 tháng đầu",
        "mechanism_of_action": "Fluconazole ức chế enzyme lanosterol 14α-demethylase (CYP51) của nấm, enzyme chuyển lanosterol thành ergosterol. Ergosterol là thành phần quan trọng của màng tế bào nấm. Ức chế tổng hợp ergosterol → màng tế bào nấm không ổn định, rò rỉ, chết tế bào. Chọn lọc cao với nấm (ít ảnh hưởng đến tế bào người). Cũng ức chế một số enzyme CYP ở người (CYP2C9, CYP2C19, CYP3A4) nên có nhiều tương tác thuốc",
        "monitoring": [
            "Chức năng gan (ALT, AST) khi dùng liều cao hoặc kéo dài",
            "Chức năng thận (creatinine, BUN) - điều chỉnh liều khi suy thận",
            "Dấu hiệu độc gan: vàng da, mệt mỏi, đau bụng",
            "ECG nếu dùng liều cao ≥400mg/ngày (QT kéo dài)",
            "Đường huyết nếu dùng với sulfonylurea",
            "INR nếu dùng với warfarin",
            "Đáp ứng điều trị và triệu chứng lâm sàng"
        ],
        "precautions": [
            "Điều chỉnh liều theo chức năng thận (giảm liều khi CrCl <50)",
            "Theo dõi sát chức năng gan khi dùng liều cao hoặc kéo dài",
            "Thận trọng với QT kéo dài khi dùng liều cao ≥400mg/ngày",
            "Theo dõi INR khi dùng với warfarin (tăng nguy cơ chảy máu)",
            "Theo dõi đường huyết khi dùng với sulfonylurea (tăng nguy cơ hạ đường huyết)",
            "Tránh dùng trong 3 tháng đầu thai kỳ (có thể gây dị tật)",
            "Dùng đủ thời gian để tránh tái phát (7-21 ngày tùy chỉ định)",
            "Thận trọng ở bệnh nhân suy gan, suy thận"
        ],
        "pharmacokinetics": {
            "half_life": "30 giờ (dài, cho phép dùng 1 lần/ngày)",
            "onset": "Vài giờ đến vài ngày",
            "duration": "Dài (do half-life dài)",
            "protein_binding": "11-12% (thấp, dễ khuếch tán vào mô)",
            "clearance": "Thận (chủ yếu, 80% thải nguyên dạng qua nước tiểu), gan (chuyển hóa ít)"
        },
        "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm. Dung dịch IV: bảo quản theo hướng dẫn nhà sản xuất",
        "black_box_warnings": "Chống chỉ định trong 3 tháng đầu thai kỳ - có thể gây dị tật thai nhi. QT kéo dài có thể xảy ra ở liều cao",
        "drug_interactions": {
            "major": [
                {
                    "drug": "Warfarin",
                    "mechanism": "Fluconazole ức chế CYP2C9, làm giảm chuyển hóa warfarin, tăng nồng độ warfarin.",
                    "effect": "Tăng tác dụng chống đông, tăng INR, tăng nguy cơ chảy máu nghiêm trọng",
                    "management": "Theo dõi INR chặt chẽ khi bắt đầu, thay đổi liều, hoặc ngừng fluconazole. Giảm liều warfarin 25-50% khi bắt đầu fluconazole. Điều chỉnh liều warfarin theo INR."
                },
                {
                    "drug": "Phenytoin",
                    "mechanism": "Fluconazole ức chế CYP2C9 và CYP2C19, làm giảm chuyển hóa phenytoin. Phenytoin cảm ứng CYP450, có thể giảm nồng độ fluconazole.",
                    "effect": "Tăng nồng độ phenytoin, tăng độc tính phenytoin (chóng mặt, rung giật, ataxia). Giảm nồng độ fluconazole.",
                    "management": "Theo dõi nồng độ phenytoin. Giảm liều phenytoin khi bắt đầu fluconazole. Tăng liều fluconazole nếu cần. Theo dõi dấu hiệu độc tính phenytoin."
                },
                {
                    "drug": "Cyclosporine, Tacrolimus",
                    "mechanism": "Fluconazole ức chế CYP3A4, làm giảm chuyển hóa cyclosporine và tacrolimus.",
                    "effect": "Tăng nồng độ cyclosporine/tacrolimus, tăng độc tính (độc thận, tăng huyết áp, độc thần kinh)",
                    "management": "Giảm liều cyclosporine/tacrolimus 25-50% khi bắt đầu fluconazole. Theo dõi nồng độ cyclosporine/tacrolimus, chức năng thận. Điều chỉnh liều theo nồng độ."
                },
                {
                    "drug": "Rifampin",
                    "mechanism": "Rifampin cảm ứng CYP450, làm tăng chuyển hóa fluconazole.",
                    "effect": "Giảm nồng độ fluconazole, giảm hiệu quả điều trị",
                    "management": "Tăng liều fluconazole 50-100% khi dùng với rifampin. Theo dõi đáp ứng điều trị."
                }
            ],
            "moderate": [
                {
                    "drug": "Sulfonylurea (Glibenclamide, Gliclazide)",
                    "mechanism": "Fluconazole ức chế CYP2C9, làm giảm chuyển hóa sulfonylurea.",
                    "effect": "Tăng nồng độ sulfonylurea, tăng nguy cơ hạ đường huyết",
                    "management": "Theo dõi đường huyết chặt chẽ. Giảm liều sulfonylurea khi bắt đầu fluconazole. Điều chỉnh liều theo đường huyết."
                },
                {
                    "drug": "Statins (Atorvastatin, Simvastatin)",
                    "mechanism": "Fluconazole ức chế CYP3A4, làm giảm chuyển hóa statins (đặc biệt simvastatin, atorvastatin).",
                    "effect": "Tăng nồng độ statin, tăng nguy cơ độc cơ (myopathy, rhabdomyolysis)",
                    "management": "Giảm liều statin hoặc tạm ngừng khi dùng fluconazole. Theo dõi CK, dấu hiệu đau cơ. Dùng pravastatin hoặc rosuvastatin (ít chuyển hóa qua CYP3A4) nếu có thể."
                },
                {
                    "drug": "Benzodiazepine (Midazolam, Triazolam)",
                    "mechanism": "Fluconazole ức chế CYP3A4, làm giảm chuyển hóa benzodiazepine.",
                    "effect": "Tăng nồng độ benzodiazepine, tăng tác dụng an thần, kéo dài thời gian tác dụng",
                    "management": "Giảm liều benzodiazepine. Theo dõi dấu hiệu an thần quá mức."
                }
            ],
            "minor": [
                {
                    "drug": "Theophylline",
                    "mechanism": "Fluconazole có thể ảnh hưởng nhẹ đến chuyển hóa theophylline.",
                    "effect": "Tăng nhẹ nồng độ theophylline",
                    "management": "Theo dõi nồng độ theophylline. Không cần điều chỉnh liều thường quy."
                }
            ]
        },
        "contraindications": {
            "tuyệt_đối": [
                "Dị ứng fluconazole hoặc các azole antifungals khác",
                "Có thai (3 tháng đầu) - chống chỉ định tuyệt đối, có thể gây dị tật thai nhi",
                "Dùng terfenadine hoặc astemizole với liều fluconazole ≥400mg/ngày - tăng nguy cơ QT kéo dài, loạn nhịp tim nghiêm trọng"
            ],
            "tương_đối": [
                "Có thai (tam cá nguyệt 2-3) - thận trọng, chỉ dùng khi thực sự cần thiết",
                "Suy thận nặng (CrCl <30) - giảm liều đáng kể, theo dõi chặt chẽ",
                "Suy gan - thận trọng, có thể giảm chuyển hóa",
                "QT kéo dài hoặc loạn nhịp tim - tăng nguy cơ QT kéo dài với liều cao",
                "Dùng với warfarin - tăng nguy cơ chảy máu, cần theo dõi INR",
                "Dùng với cyclosporine/tacrolimus - tăng độc tính, cần giảm liều",
                "Dùng với statins - tăng nguy cơ độc cơ",
                "Dùng với phenytoin - tăng độc tính phenytoin"
            ]
        },
        "contraindications_detail": {
            "tuyệt_đối": [
                "Dị ứng fluconazole hoặc các azole antifungals khác",
                "Có thai (3 tháng đầu) - chống chỉ định tuyệt đối, có thể gây dị tật thai nhi",
                "Dùng terfenadine hoặc astemizole với liều fluconazole ≥400mg/ngày - tăng nguy cơ QT kéo dài, loạn nhịp tim nghiêm trọng"
            ],
            "tương_đối": [
                "Có thai (tam cá nguyệt 2-3) - thận trọng, chỉ dùng khi thực sự cần thiết",
                "Suy thận nặng (CrCl <30) - giảm liều đáng kể, theo dõi chặt chẽ",
                "Suy gan - thận trọng, có thể giảm chuyển hóa",
                "QT kéo dài hoặc loạn nhịp tim - tăng nguy cơ QT kéo dài với liều cao",
                "Dùng với warfarin - tăng nguy cơ chảy máu, cần theo dõi INR",
                "Dùng với cyclosporine/tacrolimus - tăng độc tính, cần giảm liều",
                "Dùng với statins - tăng nguy cơ độc cơ",
                "Dùng với phenytoin - tăng độc tính phenytoin"
            ]
        },
        "reversal_agents": {
            "available": False,
            "agents": [],
            "notes": "Không có antidote đặc hiệu. Điều trị quá liều chủ yếu là hỗ trợ."
        },
        "pregnancy_lactation": {
            "fda_category": "C (tam cá nguyệt 2-3), D (tam cá nguyệt đầu)",
            "pregnancy_details": "Tam cá nguyệt đầu: Thuốc phân loại D - CHỐNG CHỈ ĐỊNH. Các nghiên cứu trên động vật cho thấy fluconazole liều cao có thể gây dị tật thai nhi (dị tật xương, sứt môi/vòm miệng). Có báo cáo về dị tật bẩm sinh ở người khi dùng liều cao trong tam cá nguyệt đầu. Tam cá nguyệt 2-3: Thuốc phân loại C. Có thể dùng khi lợi ích vượt quá nguy cơ, nhưng nên tránh nếu không cần thiết. Nhiễm nấm có thể gây nguy hiểm cho thai nhi. Dùng liều thấp nhất hiệu quả.",
            "lactation": {
                "safety": "Compatible",
                "details": "Fluconazole bài tiết vào sữa mẹ ở nồng độ thấp (tương đương nồng độ trong máu mẹ). Nồng độ trong sữa mẹ thấp và không có báo cáo về tác dụng phụ đáng kể ở trẻ bú mẹ. Hấp thu qua đường tiêu hóa của trẻ sơ sinh thấp.",
                "recommendation": "Có thể dùng khi cho con bú. Dùng liều thấp nhất hiệu quả. Theo dõi trẻ sơ sinh nếu dùng liều cao hoặc kéo dài."
            }
        },
        "hepatic_adjustment": {
            "mild": "Không cần điều chỉnh liều. Fluconazole chuyển hóa ít qua gan, thải trừ chủ yếu qua thận.",
            "moderate": "Thận trọng, có thể cần giảm liều nhẹ. Chuyển hóa có thể giảm ở suy gan trung bình.",
            "severe": "Thận trọng, có thể cần giảm liều. Chuyển hóa có thể giảm đáng kể ở suy gan nặng, nhưng thải trừ chủ yếu qua thận nên ít ảnh hưởng.",
            "notes": "Fluconazole chuyển hóa ít qua gan (chủ yếu qua CYP2C9, CYP2C19), thải trừ chủ yếu qua thận (80% nguyên dạng). Suy gan có thể giảm chuyển hóa nhẹ nhưng không đáng kể. Tuy nhiên, suy gan có thể kèm theo suy thận, nên cần điều chỉnh liều theo chức năng thận."
        },
        "overdose_management": {
            "symptoms": [
                "Triệu chứng tiêu hóa: Buồn nôn, nôn, tiêu chảy, đau bụng",
                "Triệu chứng thần kinh: Đau đầu, chóng mặt, lú lẫn, co giật (hiếm)",
                "Triệu chứng gan: Tăng men gan, vàng da, suy gan (hiếm nhưng nghiêm trọng)",
                "Triệu chứng tim mạch: QT kéo dài, loạn nhịp tim (với liều cao ≥400mg/ngày)",
                "Triệu chứng da: Phát ban, hội chứng Stevens-Johnson (hiếm nhưng nghiêm trọng)",
                "Triệu chứng nghiêm trọng: Suy gan, rối loạn nhịp tim, hội chứng Stevens-Johnson"
            ],
            "antidote": "Không có antidote đặc hiệu. Điều trị hỗ trợ và điều trị triệu chứng.",
            "treatment": [
                "Ngừng ngay fluconazole",
                "Rửa dạ dày hoặc than hoạt nếu uống trong vòng 1-2 giờ (nếu không có chống chỉ định)",
                "Theo dõi dấu hiệu sinh tồn: Huyết áp, nhịp tim, nhịp thở, SpO2, ECG",
                "Điều trị triệu chứng tiêu hóa:",
                "  - Chống nôn nếu cần",
                "  - Truyền dịch nếu mất nước",
                "  - Theo dõi điện giải",
                "Điều trị tăng men gan/suy gan nếu có:",
                "  - Theo dõi ALT, AST, bilirubin",
                "  - Điều trị hỗ trợ gan",
                "  - Nếu suy gan nặng: điều trị suy gan",
                "Điều trị QT kéo dài/loạn nhịp nếu có:",
                "  - Theo dõi ECG liên tục",
                "  - Điều trị loạn nhịp nếu cần",
                "Điều trị hội chứng Stevens-Johnson nếu có:",
                "  - Chuyển khoa da liễu/bỏng",
                "  - Điều trị hỗ trợ",
                "  - Kháng sinh nếu có nhiễm trùng",
                "Theo dõi dấu hiệu sinh tồn: Huyết áp, nhịp tim, nhịp thở, SpO2"
            ],
            "monitoring": "Theo dõi dấu hiệu sinh tồn, ECG, chức năng gan (ALT, AST, bilirubin), dấu hiệu da trong ít nhất 24-48 giờ. Theo dõi lâu hơn nếu có biến chứng (suy gan, loạn nhịp, hội chứng Stevens-Johnson)."
        },
        "reversal_agents": None,
        "administration_instructions": {
            "oral": {
                "with_food": "Có thể uống với hoặc không thức ăn. Hấp thu không phụ thuộc vào thức ăn. Có thể uống với nước đầy đủ.",
                "timing": "Uống 1 lần/ngày (do half-life dài 30 giờ). Có thể uống bất kỳ thời điểm nào trong ngày. Cách đều 24 giờ. Với liều cao (≥400mg), có thể chia 2 lần/ngày."
            },
            "iv": {
                "reconstitution": "Pha với NS hoặc D5W. Nồng độ pha: 2mg/ml (tối đa). Pha 200mg trong 100ml dịch = 2mg/ml. Pha 400mg trong 200ml dịch = 2mg/ml.",
                "infusion_rate": "Truyền trong 1-2 giờ. Không truyền quá nhanh. Tốc độ: 100ml/giờ = ~1.7ml/phút. 200ml/2 giờ = ~1.7ml/phút.",
                "compatibility": ["NS (0.9% NaCl)", "D5W (5% Dextrose)"],
                "incompatibility": ["Không trộn với các thuốc khác trong cùng một ống truyền. Kiểm tra tương thích trước khi pha."],
                "notes": "Theo dõi chức năng gan, thận trong quá trình truyền. Có thể gây kích ứng tĩnh mạch - thay đổi vị trí tiêm nếu cần."
            }
        },
        "references": {
            "primary_sources": [
                "FDA Drug Label - Fluconazole (Diflucan)",
                "UpToDate - Fluconazole: Drug Information",
                "Medscape - Fluconazole Drug Reference",
                "Goodman & Gilman's The Pharmacological Basis of Therapeutics (14th ed)",
                "Lexicomp Online - Fluconazole Monograph",
                "Micromedex - Fluconazole Drug Information",
                "IDSA Guidelines - Antifungal Therapy"
            ],
            "last_updated": "2024-12-19",
            "evidence_level": "A - Dựa trên FDA drug labels, IDSA guidelines, và dữ liệu lâm sàng từ nhiều nguồn"
        },
        "risk_flags": {
            "high_alert": False,
            "narrow_therapeutic_index": False,
            "bleeding_risk": False,
            "organ_toxicity": ["Hepatotoxicity", "QT prolongation (high doses ≥400mg/day)"],
            "qt_prolongation": True,
            "hepatotoxicity": True,
            "nephrotoxicity": False,
            "requires_monitoring": ["Hepatic function (ALT, AST) - especially with high doses or prolonged use", "Renal function (creatinine, BUN) - for dose adjustment", "ECG if high doses ≥400mg/day", "INR if co-administered with warfarin - CRITICAL", "Blood glucose if co-administered with sulfonylureas", "Phenytoin levels if co-administered"]
        },
        "guideline_tags": [
            "IDSA Guidelines - Antifungal Therapy",
            "FDA Black Box Warning - Fluconazole and Pregnancy (Category D in 1st trimester)",
            "FDA Drug Information - Fluconazole",
            "UpToDate - Fluconazole Drug Information"
        ],
        "reversal_agents": {
            "available": False,
            "agents": [],
        },
    },

    "Isavuconazole": {
        "group": "Infectious Disease - Antifungal (Azole - Triazole, prodrug)",
        "vietnamese_name": "Isavuconazole (Isavuconazonium sulfate), Cresemba",
        "administration": ["PO", "IV"],
        "indications": [
            "Nhiễm nấm Aspergillosis xâm lấn",
            "Nhiễm nấm Mucorales (mucormycosis) khi không dung nạp/không đáp ứng Amphotericin B",
            "Nhiễm nấm Candida xâm lấn (off-label/backup)",
            "Thay thế khi chống chỉ định hoặc thất bại với voriconazole/posaconazole"
        ],
        "contraindications": [
            "Dị ứng isavuconazole/isavuconazonium",
            "Hội chứng QT ngắn bẩm sinh",
            "Dùng với chất cảm ứng mạnh CYP3A4 (rifampin, carbamazepine, phenobarbital, phenytoin, St. John's wort)",
            "Dùng với chất ức chế mạnh CYP3A4 (ketoconazole, high-dose ritonavir, clarithromycin) do tăng nồng độ"
        ],
        "dosage": {
            "adult_loading": "372mg (tương đương 200mg isavuconazole) IV/PO mỗi 8 giờ x 6 liều (48 giờ)",
            "adult_maintenance": "372mg IV/PO mỗi 24 giờ, bắt đầu 12-24 giờ sau liều loading cuối",
            "notes": "Không cần chỉnh liều giữa PO và IV. Không chứa cyclodextrin nên an toàn hơn ở suy thận so với voriconazole/posaconazole."
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "Không đổi",
            "under_30": "Không đổi (không chứa cyclodextrin)",
            "hemodialysis": "Không bị loại đáng kể qua lọc máu, không cần bổ sung"
        },
        "side_effects": [
            "Tăng men gan",
            "Buồn nôn, nôn, tiêu chảy",
            "Nhức đầu",
            "Hạ kali máu",
            "Phản ứng truyền (IV)",
            "QT NGẮN (đặc trưng của isavuconazole)"
        ],
        "interactions": [
            "CYP3A4 inducers mạnh (rifampin, carbamazepine, phenobarbital, phenytoin, St. John's wort): giảm nồng độ, tránh",
            "CYP3A4 inhibitors mạnh (ketoconazole, ritonavir liều cao, clarithromycin): tăng nồng độ, tránh/giảm liều",
            "Tacrolimus/Cyclosporine/Sirolimus: tăng nồng độ, cần giảm liều và theo dõi",
            "Warfarin: có thể tăng nhẹ INR, theo dõi",
            "Thuốc/nhóm gây QT ngắn: thận trọng"
        ],
        "pregnancy": "C",
        "risk_flags": {
            "high_alert": True,
            "narrow_therapeutic_index": False,
            "organ_toxicity": {"hepatic": True, "cardiac": True},
            "icu_critical_care_only": False,
            "look_alike_sound_alike": []
        },
        "guideline_tags": [
            "IDSA Invasive Aspergillosis Guidelines 2024",
            "IDSA Candidiasis Guidelines 2024",
            "ECMM-ERCMID-ERS Invasive Fungal Disease Guidelines",
            "WHO Guidelines for Invasive Fungal Infections"
        ],
        "mechanism_of_action": "Isavuconazole (hoạt chất từ tiền chất isavuconazonium sulfate) là triazole ức chế lanosterol 14α-demethylase (CYP51) của nấm, ngăn tổng hợp ergosterol → màng tế bào nấm mất ổn định. Phổ rộng: Aspergillus, Mucorales, Candida, Fusarium.",
        "monitoring": [
            "Chức năng gan (ALT, AST, bilirubin) trước và trong điều trị",
            "Điện giải (đặc biệt kali) do nguy cơ QT ngắn",
            "ECG nền và khi có triệu chứng tim mạch",
            "Theo dõi tương tác khi phối hợp thuốc ức chế/cảm ứng CYP3A4",
            "Đánh giá đáp ứng lâm sàng và xét nghiệm với nhiễm nấm xâm lấn"
        ],
        "precautions": [
            "Có thể gây QT NGẮN (khác với azole khác gây QT dài) - tránh ở bệnh nhân có hội chứng QT ngắn",
            "Chất nền và ức chế CYP3A4 mức trung bình → nhiều tương tác",
            "Không cần chỉnh liều ở suy thận, không chứa cyclodextrin",
            "Suy gan trung bình-nặng: theo dõi sát men gan, cân nhắc giảm liều nếu tăng men",
            "Thẩm tách máu không loại bỏ đáng kể thuốc",
            "Theo dõi phản ứng truyền khi dùng IV"
        ],
        "pharmacokinetics": {
            "half_life": "≈130 giờ (rất dài) → dùng 1 lần/ngày sau liều tải",
            "onset": "Cần liều tải để đạt nồng độ điều trị nhanh; trạng thái ổn định sau ~7 ngày",
            "duration": "Duy trì 24 giờ/liều sau pha tải",
            "protein_binding": "≈99%",
            "clearance": "Chuyển hóa gan (CYP3A4/5; glucuronidation thứ cấp), thải trừ qua phân và nước tiểu dưới dạng chuyển hóa"
        },
        "storage": "Bảo quản viên và lọ bột ở 20-25°C, tránh ẩm. Dung dịch sau pha IV dùng trong 6 giờ ở nhiệt độ phòng hoặc 24 giờ nếu bảo quản lạnh (2-8°C).",
        "black_box_warnings": None,
        "drug_interactions": {
            "major": [
                {
                    "drug": "Rifampin, Carbamazepine, Phenobarbital, Phenytoin, St. John's wort",
                    "mechanism": "Cảm ứng mạnh CYP3A4 → giảm mạnh nồng độ isavuconazole",
                    "effect": "Giảm hiệu quả điều trị, nguy cơ thất bại",
                    "management": "TRÁNH dùng chung; chọn thuốc kháng nấm khác."
                },
                {
                    "drug": "Ketoconazole, Ritonavir liều cao, Clarithromycin",
                    "mechanism": "Ức chế mạnh CYP3A4 → tăng nồng độ isavuconazole",
                    "effect": "Nguy cơ tăng độc tính (tăng men gan, rối loạn điện giải, QT ngắn)",
                    "management": "Tránh phối hợp hoặc giảm liều và theo dõi chặt chẽ."
                }
            ],
            "moderate": [
                {
                    "drug": "Tacrolimus, Cyclosporine, Sirolimus",
                    "mechanism": "Isavuconazole ức chế CYP3A4 mức trung bình → tăng nồng độ thuốc ức chế miễn dịch",
                    "effect": "Tăng độc tính thận, tăng huyết áp, rối loạn điện giải",
                    "management": "Giảm liều và theo dõi nồng độ thuốc ức chế miễn dịch."
                },
                {
                    "drug": "Warfarin",
                    "mechanism": "Ảnh hưởng chuyển hóa qua CYP, có thể tăng INR",
                    "effect": "Tăng nguy cơ chảy máu",
                    "management": "Theo dõi INR khi bắt đầu/ngừng hoặc thay đổi liều."
                }
            ],
            "minor": []
        },
        "contraindications": {
            "tuyệt_đối": [
                "Dị ứng isavuconazole/isavuconazonium",
                "Hội chứng QT ngắn bẩm sinh",
                "Dùng cùng chất ức chế hoặc cảm ứng mạnh CYP3A4 (ketoconazole, rifampin, carbamazepine, phenobarbital, phenytoin, St. John's wort)"
            ],
            "tương_đối": [
                "Suy gan trung bình-nặng (theo dõi men gan chặt chẽ)",
                "Rối loạn điện giải (hạ kali, hạ magie) - có thể làm nặng QT ngắn",
                "Bệnh tim nền hoặc tiền sử loạn nhịp"
            ]
        },
        "pregnancy_lactation": {
            "fda_category": "C",
            "pregnancy_details": "Dữ liệu trên người hạn chế; động vật cho thấy độc tính phôi. Chỉ dùng khi lợi ích vượt trội.",
            "lactation": {
                "safety": "Caution",
                "details": "Chưa rõ bài tiết vào sữa mẹ. Cân nhắc ngừng cho bú hoặc chọn thuốc khác.",
                "recommendation": "Tránh hoặc theo dõi trẻ nếu phải dùng."
            }
        },
        "hepatic_adjustment": {
            "mild": "Không cần điều chỉnh",
            "moderate": "Thận trọng, theo dõi men gan; cân nhắc giảm liều nếu men gan tăng kéo dài",
            "severe": "Dữ liệu hạn chế; thận trọng tối đa hoặc cân nhắc thuốc khác",
            "notes": "Chuyển hóa qua gan (CYP3A4/5). Tăng AUC ở Child-Pugh B/C; cần giám sát lâm sàng."
        },
        "overdose_management": {
            "symptoms": [
                "Buồn nôn, nôn, chóng mặt",
                "Tăng men gan",
                "Rối loạn điện giải, QT ngắn"
            ],
            "antidote": "Không có antidote đặc hiệu",
            "treatment": [
                "Ngừng thuốc, điều trị hỗ trợ",
                "Theo dõi ECG và điện giải (K, Mg)",
                "Bù điện giải nếu cần",
                "Thẩm tách máu không hiệu quả do gắn protein cao"
            ],
            "monitoring": "Theo dõi men gan, ECG, điện giải, dấu hiệu lâm sàng trong 24-48 giờ."
        },
        "reversal_agents": None,
        "administration_instructions": {
            "oral": {
                "with_food": "Có thể uống cùng hoặc không cùng thức ăn",
                "timing": "Liều tải: mỗi 8 giờ x 6 liều; sau đó 1 lần/ngày vào cùng thời điểm"
            },
            "iv": {
                "reconstitution": "Pha lọ 200mg base (372mg muối) với dung môi kèm theo, sau đó pha loãng trong 250ml NS hoặc D5W",
                "infusion_rate": "Truyền trong ≥1 giờ",
                "compatibility": ["NS", "D5W"],
                "incompatibility": [],
                "notes": "Không chứa cyclodextrin; theo dõi phản ứng truyền."
            }
        },
        "references": {
            "primary_sources": [
                "FDA Drug Label - Cresemba (Isavuconazonium sulfate)",
                "IDSA Guidelines - Treatment of Aspergillosis and Mucormycosis",
                "UpToDate - Isavuconazole: Drug Information"
            ],
            "last_updated": "2025-02-05",
            "evidence_level": "High (FDA-approved, IDSA guideline-endorsed)"
        }
    },
    "Itraconazole": {
        "group": "Infectious Disease - Antifungal (Azole)",
        "vietnamese_name": "Itraconazole, Sporanox",
        "administration": ["PO", "IV"],
        "indications": [
            "Nhiễm nấm Aspergillosis",
            "Nhiễm nấm Blastomycosis",
            "Nhiễm nấm Histoplasmosis",
            "Nhiễm nấm Candidiasis (oral, esophageal)",
            "Onychomycosis (nấm móng)"
        ],
        "contraindications": [
            "Dị ứng itraconazole/azole",
            "Có thai",
            "Suy tim sung huyết",
            "Dùng với thuốc chuyển hóa CYP3A4 (xem interactions)"
        ],
        "dosage": {
            "adult_systemic": "200mg x 1-2 lần/ngày (PO)",
            "adult_aspergillosis": "200mg x 3 lần/ngày x 3 ngày, sau đó 200mg x 1-2 lần/ngày",
            "adult_onychomycosis": "200mg x 2 lần/ngày x 1 tuần mỗi tháng (x 3-4 tháng)",
            "adult_vaginal_candidiasis": "200mg x 2 lần/ngày x 1 ngày",
            "notes": "Uống với thức ăn để tăng hấp thu. Capsule cần acid dạ dày"
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "Thận trọng (IV không dùng nếu CrCl <30)",
            "under_30": "Tránh dùng IV"
        },
        "side_effects": [
            "Nhức đầu",
            "Buồn nôn, nôn",
            "Tiêu chảy",
            "Tăng men gan (hiếm suy gan)",
            "Phù, suy tim",
            "Rụng tóc",
            "Ban da"
        ],
        "interactions": [
            "CYP3A4 substrates: tăng đáng kể nồng độ (simvastatin, lovastatin, midazolam, triazolam, quinidine)",
            "Rifampin: giảm nồng độ itraconazole",
            "Warfarin: tăng tác dụng chống đông",
            "Digoxin: tăng nồng độ digoxin",
            "Phenytoin: tăng nồng độ phenytoin"
        ],
        "pregnancy": "C - D (chống chỉ định)",
        "mechanism_of_action": "Itraconazole là thuốc chống nấm phổ rộng thuộc nhóm triazole, ức chế enzyme lanosterol 14-alpha-demethylase (CYP51) của nấm. Enzyme này có vai trò quan trọng trong tổng hợp ergosterol, một thành phần chính của màng tế bào nấm. Bằng cách ức chế tổng hợp ergosterol, itraconazole làm thay đổi tính thấm màng tế bào nấm, dẫn đến ức chế sự phát triển và gây chết tế bào nấm. Itraconazole có phổ kháng nấm rộng: nấm men (Candida, Cryptococcus), nấm sợi (Aspergillus, Blastomyces, Histoplasma, Coccidioides), và dermatophytes (Trichophyton, Microsporum). Itraconazole cũng ức chế CYP3A4 ở gan, dẫn đến nhiều tương tác thuốc quan trọng. Hấp thu phụ thuộc vào pH dạ dày (cần acid dạ dày), tăng khi uống với thức ăn.",
        "monitoring": [
            "Đáp ứng điều trị (giảm triệu chứng nhiễm nấm, cải thiện lâm sàng)",
            "Chức năng gan (ALT, AST, bilirubin) - tăng men gan phổ biến, suy gan hiếm nhưng có thể nghiêm trọng",
            "Dấu hiệu suy tim (phù, khó thở, tăng cân) - itraconazole có thể gây suy tim, đặc biệt ở liều cao",
            "Tương tác với CYP3A4 substrates (simvastatin, lovastatin - nguy cơ tiêu cơ vân; midazolam, triazolam - tăng an thần; quinidine - tăng nguy cơ loạn nhịp)",
            "Warfarin (tăng INR), digoxin (tăng nồng độ, nguy cơ độc tính), phenytoin (tăng nồng độ)",
            "Rifampin (giảm nồng độ itraconazole, có thể giảm hiệu quả)",
            "Dấu hiệu phản ứng dị ứng (phát ban, sốt)"
        ],
        "precautions": [
            "CHỐNG CHỈ ĐỊNH ở bệnh nhân suy tim sung huyết - itraconazole có thể gây suy tim, đặc biệt ở liều cao",
            "CHỐNG CHỈ ĐỊNH trong thai kỳ - gây dị tật thai nhi (category D)",
            "Uống với thức ăn hoặc thức uống có acid (cola) để tăng hấp thu (cần acid dạ dày)",
            "Tránh dùng với PPI, H2 blocker, antacid (giảm acid dạ dày → giảm hấp thu)",
            "Nhiều tương tác thuốc do ức chế CYP3A4 - tăng nồng độ simvastatin, lovastatin (nguy cơ tiêu cơ vân), midazolam, triazolam (tăng an thần), quinidine (tăng nguy cơ loạn nhịp), warfarin (tăng INR), digoxin (tăng nồng độ), phenytoin (tăng nồng độ)",
            "Tránh dùng với rifampin (giảm nồng độ itraconazole, có thể giảm hiệu quả)",
            "Tăng men gan - phổ biến, theo dõi chức năng gan, ngừng nếu có suy gan",
            "Suy tim - ngừng ngay nếu có dấu hiệu suy tim (phù, khó thở)",
            "Không dùng IV nếu CrCl <30 (chứa cyclodextrin, tích lũy ở suy thận)",
            "Dùng đủ liều và đủ thời gian để tránh tái phát",
            "Thận trọng ở bệnh nhân có bệnh gan (chuyển hóa qua gan)"
        ],
        "pharmacokinetics": {
            "half_life": "21 giờ (itraconazole), 12 giờ (hydroxy-itraconazole - metabolite hoạt động)",
            "onset": "Vài ngày đến vài tuần (tác dụng chống nấm)",
            "duration": "24 giờ (dùng 1-2 lần/ngày)",
            "protein_binding": "99.8% (gắn chặt với albumin)",
            "clearance": "Gan: chuyển hóa qua CYP3A4 thành hydroxy-itraconazole (metabolite hoạt động, mạnh hơn itraconazole). Thận: bài tiết một phần metabolites. Hấp thu phụ thuộc vào pH dạ dày (cần acid dạ dày), tăng khi uống với thức ăn. IV chứa cyclodextrin, tích lũy ở suy thận."
        },
        "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm, tránh ánh sáng. Viên nén/capsule: bảo quản trong bao bì kín. Dạng solution: bảo quản ở nhiệt độ phòng, không làm lạnh. IV: bảo quản trong tủ lạnh (2-8°C), để nhiệt độ phòng trước khi pha.",
        "black_box_warnings": "CHỐNG CHỈ ĐỊNH ở bệnh nhân suy tim sung huyết hoặc có tiền sử suy tim. Itraconazole có thể gây suy tim, đặc biệt ở liều cao. CHỐNG CHỈ ĐỊNH trong thai kỳ - gây dị tật thai nhi (category D). Nhiều tương tác thuốc nghiêm trọng do ức chế CYP3A4 - tăng nguy cơ tiêu cơ vân với simvastatin/lovastatin, tăng an thần với midazolam/triazolam, tăng nguy cơ loạn nhịp với quinidine.",
        "drug_interactions": {
            "major": [
                {
                    "drug": "Simvastatin, Lovastatin",
                    "mechanism": "Itraconazole ức chế CYP3A4, làm giảm chuyển hóa simvastatin và lovastatin, tăng nồng độ statin trong máu.",
                    "effect": "Tăng nguy cơ tiêu cơ vân (rhabdomyolysis) nghiêm trọng, suy thận cấp, đe dọa tính mạng",
                    "management": "TRÁNH DÙNG đồng thời. Nếu bắt buộc, ngừng statin hoặc dùng statin không chuyển hóa qua CYP3A4 (pravastatin, rosuvastatin). Theo dõi CK, creatinine, dấu hiệu tiêu cơ vân (đau cơ, nước tiểu sẫm màu)."
                },
                {
                    "drug": "Midazolam, Triazolam",
                    "mechanism": "Itraconazole ức chế CYP3A4, làm giảm chuyển hóa midazolam và triazolam, tăng nồng độ benzodiazepine trong máu.",
                    "effect": "Tăng an thần nghiêm trọng, suy hô hấp, nguy cơ tử vong",
                    "management": "TRÁNH DÙNG đồng thời. Nếu bắt buộc, giảm liều benzodiazepine đáng kể, theo dõi hô hấp chặt chẽ."
                },
                {
                    "drug": "Quinidine",
                    "mechanism": "Itraconazole ức chế CYP3A4, làm giảm chuyển hóa quinidine, tăng nồng độ quinidine trong máu.",
                    "effect": "Tăng nguy cơ loạn nhịp tim nghiêm trọng (torsades de pointes), QT kéo dài, đe dọa tính mạng",
                    "management": "TRÁNH DÙNG đồng thời. Nếu bắt buộc, theo dõi ECG chặt chẽ, giảm liều quinidine."
                },
                {
                    "drug": "Rifampin, Rifabutin",
                    "mechanism": "Rifampin cảm ứng CYP3A4 mạnh, làm tăng chuyển hóa itraconazole, giảm nồng độ itraconazole trong máu.",
                    "effect": "Giảm nồng độ itraconazole, giảm hiệu quả điều trị, nguy cơ thất bại điều trị",
                    "management": "TRÁNH DÙNG đồng thời. Nếu bắt buộc, tăng liều itraconazole (có thể cần tăng gấp đôi), theo dõi nồng độ itraconazole trong máu."
                }
            ],
            "moderate": [
                {
                    "drug": "Warfarin",
                    "mechanism": "Itraconazole ức chế CYP3A4 và CYP2C9, làm giảm chuyển hóa warfarin, tăng nồng độ warfarin trong máu.",
                    "effect": "Tăng tác dụng chống đông, tăng INR, tăng nguy cơ chảy máu",
                    "management": "Theo dõi INR chặt chẽ khi bắt đầu, thay đổi liều, hoặc ngừng itraconazole. Giảm liều warfarin 25-50% khi bắt đầu itraconazole."
                },
                {
                    "drug": "Digoxin",
                    "mechanism": "Itraconazole ức chế P-glycoprotein, làm giảm thải trừ digoxin, tăng nồng độ digoxin trong máu.",
                    "effect": "Tăng nồng độ digoxin, tăng độc tính digoxin (buồn nôn, rối loạn nhịp tim)",
                    "management": "Theo dõi nồng độ digoxin và dấu hiệu độc tính. Giảm liều digoxin 25-50% khi bắt đầu itraconazole."
                },
                {
                    "drug": "Phenytoin",
                    "mechanism": "Phenytoin cảm ứng CYP3A4, làm giảm nồng độ itraconazole. Itraconazole ức chế CYP2C9, tăng nồng độ phenytoin.",
                    "effect": "Giảm nồng độ itraconazole, tăng nồng độ phenytoin",
                    "management": "Theo dõi nồng độ cả hai thuốc. Tăng liều itraconazole, giảm liều phenytoin nếu cần."
                }
            ],
            "minor": []
        },
        "contraindications": {
            "tuyệt_đối": [
                "Dị ứng itraconazole hoặc azole",
                "Có thai - chống chỉ định tuyệt đối, gây dị tật thai nhi (category D)",
                "Suy tim sung huyết hoặc có tiền sử suy tim - itraconazole có thể gây suy tim, đặc biệt ở liều cao"
            ],
            "tương_đối": [
                "Suy thận (CrCl <30) khi dùng IV - không dùng IV (chứa cyclodextrin, tích lũy ở suy thận), có thể dùng PO",
                "Suy gan - thận trọng, theo dõi chức năng gan, ngừng nếu có suy gan",
                "Dùng với PPI, H2 blocker, antacid - giảm hấp thu (cần acid dạ dày), có thể cần tăng liều hoặc dùng solution",
                "Bệnh nhân cao tuổi - tăng nguy cơ độc tính, suy tim"
            ]
        },
        "contraindications_detail": {
            "tuyệt_đối": [
                "Dị ứng itraconazole hoặc azole",
                "Có thai - chống chỉ định tuyệt đối, gây dị tật thai nhi (category D)",
                "Suy tim sung huyết hoặc có tiền sử suy tim - itraconazole có thể gây suy tim, đặc biệt ở liều cao"
            ],
            "tương_đối": [
                "Suy thận (CrCl <30) khi dùng IV - không dùng IV (chứa cyclodextrin, tích lũy ở suy thận), có thể dùng PO",
                "Suy gan - thận trọng, theo dõi chức năng gan, ngừng nếu có suy gan",
                "Dùng với PPI, H2 blocker, antacid - giảm hấp thu (cần acid dạ dày), có thể cần tăng liều hoặc dùng solution",
                "Bệnh nhân cao tuổi - tăng nguy cơ độc tính, suy tim"
            ]
        },
        "reversal_agents": {
            "available": False,
            "agents": [],
            "notes": "Không có antidote đặc hiệu. Điều trị quá liều chủ yếu là hỗ trợ."
        },
        "pregnancy_lactation": {
            "fda_category": "D",
            "pregnancy_details": "Chống chỉ định trong thai kỳ. Itraconazole gây dị tật thai nhi, đặc biệt trong 3 tháng đầu. Có thể gây sẩy thai, dị tật tim, dị tật xương. Không dùng trong thai kỳ trừ khi lợi ích vượt trội rõ ràng so với nguy cơ.",
            "lactation": {
                "safety": "Incompatible",
                "details": "Itraconazole bài tiết vào sữa mẹ. Thuốc có thể gây độc tính cho trẻ sơ sinh.",
                "recommendation": "Không cho con bú khi dùng itraconazole. Ngừng cho con bú hoặc ngừng thuốc."
            }
        },
        "hepatic_adjustment": {
            "mild": "Không đổi",
            "moderate": "Thận trọng, theo dõi chức năng gan, có thể cần giảm liều",
            "severe": "Tránh dùng hoặc giảm liều mạnh, theo dõi chặt chẽ",
            "notes": "Itraconazole chuyển hóa chủ yếu qua gan (CYP3A4). Suy gan làm giảm chuyển hóa, tăng nồng độ và độc tính. Theo dõi chức năng gan, ngừng nếu có suy gan."
        },
        "overdose_management": {
            "symptoms": [
                "Buồn nôn, nôn",
                "Tiêu chảy",
                "Tăng men gan, suy gan",
                "Phù, suy tim",
                "Rối loạn nhịp tim (khi dùng với quinidine)",
                "Tiêu cơ vân (khi dùng với statin)"
            ],
            "antidote": "Không có antidote đặc hiệu",
            "treatment": [
                "Ngừng ngay itraconazole",
                "Rửa dạ dày nếu mới uống <1 giờ",
                "Supportive care",
                "Theo dõi chức năng gan, chức năng tim",
                "Điều trị suy tim nếu có (furosemide, ACE inhibitor)",
                "Điều trị suy gan nếu có (supportive care)",
                "Theo dõi ECG nếu có rối loạn nhịp tim"
            ],
            "monitoring": "Chức năng gan, chức năng tim, ECG, dấu hiệu lâm sàng"
        },
        "reversal_agents": None,
        "administration_instructions": {
            "oral": {
                "with_food": "Uống với thức ăn hoặc thức uống có acid (cola) để tăng hấp thu",
                "timing": "Uống với thức ăn. Capsule cần acid dạ dày, tránh dùng với PPI, H2 blocker, antacid."
            },
            "iv": {
                "reconstitution": "Pha với NS hoặc D5W theo hướng dẫn nhà sản xuất",
                "infusion_rate": "Truyền trong 60 phút",
                "compatibility": ["NS", "D5W"],
                "incompatibility": [],
                "notes": "Không dùng IV nếu CrCl <30 (chứa cyclodextrin, tích lũy ở suy thận). Truyền trong 60 phút."
            }
        },
        "references": {
            "primary_sources": [
                "FDA Drug Label - Itraconazole (Sporanox)",
                "UpToDate - Itraconazole Drug Information",
                "Goodman & Gilman's Pharmacological Basis of Therapeutics, 14th ed"
            ],
            "last_updated": "2025-01-15",
            "evidence_level": "High (FDA-approved, extensive clinical data)"
        },
        "risk_flags": {
            "high_alert": True,
            "narrow_therapeutic_index": False,
            "bleeding_risk": False,
            "organ_toxicity": ["Heart failure (contraindicated in CHF) - CRITICAL", "Hepatotoxicity", "QT prolongation"],
            "qt_prolongation": True,
            "hepatotoxicity": True,
            "nephrotoxicity": False,
            "requires_monitoring": ["Signs of heart failure (edema, dyspnea, weight gain) - CRITICAL", "Hepatic function (ALT, AST, bilirubin) - common elevation", "ECG if co-administered with QT-prolonging drugs", "INR if co-administered with warfarin", "Digoxin levels if co-administered", "Phenytoin levels if co-administered", "Clinical response"]
        },
        "guideline_tags": [
            "IDSA Guidelines - Antifungal Therapy",
            "FDA Black Box Warning - Itraconazole and Heart Failure",
            "FDA Black Box Warning - Itraconazole and Pregnancy (Category D)",
            "FDA Black Box Warning - Itraconazole and Drug Interactions (CYP3A4)"
        ],
        "reversal_agents": {
            "available": False,
            "agents": [],
        },
    },

    "Posaconazole": {
        "group": "Infectious Disease - Antifungal (Azole - Triazole)",
        "vietnamese_name": "Posaconazole, Noxafil",
        "administration": ["PO", "IV"],
        "indications": [
            "Dự phòng nhiễm nấm xâm lấn (invasive fungal infections) ở bệnh nhân suy giảm miễn dịch nặng",
            "Điều trị nhiễm nấm xâm lấn (Aspergillus, Candida, Mucor)",
            "Nhiễm nấm kháng với các azole khác",
            "Nhiễm nấm Mucor (mucormycosis) - hiệu quả hơn các azole khác"
        ],
        "contraindications": [
            "Dị ứng posaconazole",
            "Dùng với sirolimus (tăng nồng độ sirolimus)",
            "Dùng với ergot alkaloids (tăng nguy cơ co thắt mạch)",
            "Dùng với pimozide, quinidine (tăng nguy cơ QT kéo dài)"
        ],
        "contraindications_detail": {
            "tuyệt_đối": [
                "Dị ứng posaconazole",
                "Dùng với sirolimus - CHỐNG CHỈ ĐỊNH (tăng nồng độ sirolimus nghiêm trọng)",
                "Dùng với ergot alkaloids - CHỐNG CHỈ ĐỊNH (tăng nguy cơ co thắt mạch)",
                "Dùng với pimozide, quinidine - CHỐNG CHỈ ĐỊNH (tăng nguy cơ QT kéo dài)"
            ],
            "tương_đối": [
                "Suy thận nặng (CrCl <30) khi dùng IV - thận trọng (chứa cyclodextrin, tích lũy)",
                "Suy gan - thận trọng, theo dõi chức năng gan",
                "QT kéo dài hoặc rối loạn nhịp tim - tăng nguy cơ QT kéo dài",
                "Dùng với cyclosporine/tacrolimus - tăng nồng độ, cần giảm liều 50%"
            ]
        },
        "reversal_agents": {
            "available": False,
            "agents": [],
            "notes": "Không có antidote đặc hiệu. Điều trị quá liều chủ yếu là hỗ trợ."
        },
        "dosage": {
            "adult_prophylaxis": "300mg x 2 lần/ngày (ngày đầu), sau đó 300mg x 1 lần/ngày",
            "adult_treatment": "300mg x 2 lần/ngày (ngày đầu), sau đó 300mg x 1 lần/ngày",
            "adult_iv": "300mg IV x 2 lần/ngày (ngày đầu), sau đó 300mg IV x 1 lần/ngày",
            "adult_delayed_release": "300mg x 1 lần/ngày (dạng delayed-release tablet)",
            "notes": "Uống với thức ăn hoặc bữa ăn giàu chất béo để tăng hấp thu. Dạng IV: truyền trong 90 phút."
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "Không đổi",
            "under_30": "Thận trọng (dạng IV chứa cyclodextrin, tích lũy ở suy thận)"
        },
        "side_effects": [
            "Rối loạn tiêu hóa (buồn nôn, nôn, tiêu chảy)",
            "Tăng men gan (ALT, AST)",
            "QT kéo dài (hiếm)",
            "Nhức đầu",
            "Phát ban",
            "Giảm tiểu cầu (hiếm)"
        ],
        "interactions": [
            "Sirolimus: tăng nồng độ sirolimus - CHỐNG CHỈ ĐỊNH",
            "Ergot alkaloids: tăng nguy cơ co thắt mạch - CHỐNG CHỈ ĐỊNH",
            "Pimozide, Quinidine: tăng nguy cơ QT kéo dài - CHỐNG CHỈ ĐỊNH",
            "Cyclosporine, Tacrolimus: tăng nồng độ - giảm liều 50%",
            "Phenytoin, Rifampin: giảm nồng độ posaconazole",
            "Midazolam, Triazolam: tăng nồng độ - giảm liều"
        ],
        "pregnancy": "C",
        "risk_flags": {
            "high_alert": True,
            "narrow_therapeutic_index": False,
            "organ_toxicity": {"hepatic": True, "cardiac": True},
            "icu_critical_care_only": False,
            "look_alike_sound_alike": []
        },
        "guideline_tags": [
            "IDSA Invasive Aspergillosis Guidelines 2024",
            "IDSA Candidiasis Guidelines 2024",
            "ECMM-ERCMID-ERS Invasive Fungal Disease Guidelines",
            "WHO Guidelines for Invasive Fungal Infections"
        ],
        "mechanism_of_action": "Posaconazole là triazole antifungal, ức chế enzyme lanosterol 14-alpha-demethylase (CYP51), ngăn chặn chuyển đổi lanosterol thành ergosterol (thành phần chính của màng tế bào nấm). Thiếu ergosterol → màng tế bào nấm không ổn định → chết tế bào nấm. Phổ kháng nấm rộng: Aspergillus, Candida, Mucor, Fusarium, Scedosporium. Đặc biệt hiệu quả trên Mucor (mucormycosis) - hiệu quả hơn các azole khác. Ức chế CYP3A4 mạnh → nhiều tương tác thuốc.",
        "monitoring": [
            "Chức năng gan (ALT, AST) - trước và trong điều trị",
            "ECG (QT interval) - trước và trong điều trị (nếu có nguy cơ)",
            "Nồng độ posaconazole trong máu (trough level) - mục tiêu >0.7-1.0 mcg/ml (prophylaxis), >1.0-1.25 mcg/ml (treatment)",
            "Dấu hiệu nhiễm trùng (sốt, WBC, CRP)",
            "Cấy máu và cấy từ vị trí nhiễm trùng",
            "Nồng độ cyclosporine/tacrolimus nếu đang dùng (posaconazole tăng nồng độ)"
        ],
        "precautions": [
            "Uống với thức ăn hoặc bữa ăn giàu chất béo để tăng hấp thu (tăng nồng độ trong máu)",
            "Theo dõi nồng độ posaconazole trong máu (trough level) - quan trọng để đảm bảo hiệu quả",
            "Mục tiêu nồng độ: >0.7-1.0 mcg/ml (prophylaxis), >1.0-1.25 mcg/ml (treatment)",
            "Nhiều tương tác thuốc (ức chế CYP3A4 mạnh) - kiểm tra tất cả thuốc đang dùng",
            "CHỐNG CHỈ ĐỊNH với sirolimus, ergot alkaloids, pimozide, quinidine",
            "Giảm liều cyclosporine/tacrolimus 50% khi bắt đầu posaconazole",
            "Theo dõi chức năng gan (tăng men gan có thể xảy ra)",
            "Theo dõi ECG nếu có nguy cơ QT kéo dài",
            "Dạng IV: thận trọng ở suy thận (chứa cyclodextrin, tích lũy)",
            "Đặc biệt hiệu quả trên Mucor (mucormycosis) - lựa chọn tốt hơn các azole khác"
        ],
        "pharmacokinetics": {
            "half_life": "20-35 giờ (dài)",
            "onset": "Tác dụng kháng nấm bắt đầu trong 24-48 giờ",
            "duration": "Dùng 1 lần/ngày sau loading dose",
            "protein_binding": ">98%",
            "metabolism": "Chuyển hóa qua gan (glucuronidation, không phải CYP) - ít tương tác hơn voriconazole",
            "clearance": "Chủ yếu qua phân (77%), một phần qua thận (14%)"
        },
        "storage": "Bảo quản ở nhiệt độ phòng (20-25°C), tránh ẩm, tránh ánh sáng. Dạng suspension: lắc kỹ trước khi dùng.",
        "black_box_warnings": "CHỐNG CHỈ ĐỊNH với sirolimus, ergot alkaloids, pimozide, quinidine. Có thể gây QT kéo dài. Có thể gây tăng men gan.",
        "drug_interactions": {
            "major": [
                {
                    "drug": "Sirolimus",
                    "mechanism": "Posaconazole ức chế CYP3A4, tăng nồng độ sirolimus",
                    "effect": "Tăng nồng độ sirolimus đáng kể, tăng nguy cơ độc tính",
                    "management": "CHỐNG CHỈ ĐỊNH dùng cùng. Nếu cần: ngừng sirolimus hoặc dùng thuốc kháng nấm khác."
                },
                {
                    "drug": "Ergot alkaloids (Ergotamine, Dihydroergotamine)",
                    "mechanism": "Posaconazole ức chế CYP3A4, tăng nồng độ ergot alkaloids",
                    "effect": "Tăng nguy cơ co thắt mạch, hoại tử chi",
                    "management": "CHỐNG CHỈ ĐỊNH dùng cùng."
                },
                {
                    "drug": "Pimozide, Quinidine",
                    "mechanism": "Posaconazole ức chế CYP3A4, tăng nồng độ pimozide/quinidine",
                    "effect": "Tăng nguy cơ QT kéo dài, rối loạn nhịp tim",
                    "management": "CHỐNG CHỈ ĐỊNH dùng cùng."
                }
            ],
            "moderate": [
                {
                    "drug": "Cyclosporine, Tacrolimus",
                    "mechanism": "Posaconazole ức chế CYP3A4, tăng nồng độ cyclosporine/tacrolimus",
                    "effect": "Tăng nồng độ cyclosporine/tacrolimus, tăng nguy cơ độc tính thận",
                    "management": "Giảm liều cyclosporine/tacrolimus 50% khi bắt đầu posaconazole. Theo dõi nồng độ cyclosporine/tacrolimus thường xuyên."
                },
                {
                    "drug": "Phenytoin, Rifampin",
                    "mechanism": "Cảm ứng enzyme, tăng chuyển hóa posaconazole",
                    "effect": "Giảm nồng độ posaconazole, giảm hiệu quả",
                    "management": "Tránh dùng cùng nếu có thể. Nếu cần: tăng liều posaconazole hoặc dùng thuốc kháng nấm khác. Theo dõi nồng độ posaconazole."
                }
            ],
            "minor": [
                {
                    "drug": "Midazolam, Triazolam",
                    "mechanism": "Posaconazole ức chế CYP3A4, tăng nồng độ benzodiazepine",
                    "effect": "Tăng tác dụng an thần",
                    "management": "Giảm liều midazolam/triazolam. Thận trọng."
                }
            ]
        },
        "contraindications": {
            "tuyệt_đối": [
                "Dị ứng posaconazole",
                "Dùng với sirolimus - CHỐNG CHỈ ĐỊNH TUYỆT ĐỐI",
                "Dùng với ergot alkaloids - CHỐNG CHỈ ĐỊNH TUYỆT ĐỐI",
                "Dùng với pimozide, quinidine - CHỐNG CHỈ ĐỊNH TUYỆT ĐỐI"
            ],
            "tương_đối": [
                "Suy thận nặng (CrCl <30) - thận trọng với dạng IV (chứa cyclodextrin)",
                "Suy gan nặng - thận trọng, theo dõi men gan",
                "QT kéo dài - thận trọng, theo dõi ECG",
                "Dùng với cyclosporine/tacrolimus - giảm liều 50%",
                "Dùng với phenytoin/rifampin - giảm hiệu quả"
            ]
        },
        "pregnancy_lactation": {
            "fda_category": "C",
            "pregnancy_details": "Posaconazole phân loại C - thận trọng trong thai kỳ. Các nghiên cứu trên động vật cho thấy một số nguy cơ. Không có nghiên cứu đầy đủ trên phụ nữ có thai. Cân nhắc lợi ích/nguy cơ. Nếu cần dùng: theo dõi sát thai nhi.",
            "lactation": {
                "safety": "Compatible",
                "details": "Posaconazole bài tiết vào sữa mẹ ở nồng độ thấp. Nồng độ trong máu trẻ bú mẹ thường rất thấp. Không có báo cáo về tác dụng phụ nghiêm trọng ở trẻ bú mẹ.",
                "recommendation": "Có thể dùng khi cho con bú. Theo dõi trẻ nếu có dấu hiệu bất thường."
            }
        },
        "hepatic_adjustment": {
            "mild": "Không đổi",
            "moderate": "Thận trọng, theo dõi men gan",
            "severe": "Thận trọng, có thể cần giảm liều. Theo dõi men gan chặt chẽ.",
            "notes": "Posaconazole chuyển hóa qua gan (glucuronidation). Suy gan có thể ảnh hưởng đến chuyển hóa. Theo dõi men gan thường xuyên."
        },
        "overdose_management": {
            "symptoms": [
                "Rối loạn tiêu hóa nặng (buồn nôn, nôn, tiêu chảy)",
                "Tăng men gan",
                "QT kéo dài (rối loạn nhịp tim)",
                "Chóng mặt, nhức đầu"
            ],
            "antidote": "Không có antidote đặc hiệu. Điều trị hỗ trợ.",
            "treatment": [
                "Ngừng posaconazole",
                "Rửa dạ dày nếu mới uống <1 giờ",
                "Than hoạt tính",
                "Supportive care",
                "Theo dõi chức năng gan, ECG",
                "Điều trị rối loạn nhịp tim nếu có"
            ],
            "monitoring": "Chức năng gan, ECG, nồng độ posaconazole trong máu, dấu hiệu lâm sàng"
        },
        "reversal_agents": None,
        "administration_instructions": {
            "oral": {
                "with_food": "NÊN uống với thức ăn hoặc bữa ăn giàu chất béo để tăng hấp thu (tăng nồng độ trong máu đáng kể)",
                "timing": "Loading dose: 300mg x 2 lần/ngày (ngày đầu). Maintenance: 300mg x 1 lần/ngày. Dạng delayed-release tablet: 300mg x 1 lần/ngày (không cần thức ăn)."
            },
            "iv": {
                "reconstitution": "Pha với NS hoặc D5W theo hướng dẫn nhà sản xuất",
                "infusion_rate": "Truyền trong 90 phút",
                "compatibility": ["NS", "D5W"],
                "incompatibility": [],
                "notes": "Loading dose: 300mg IV x 2 lần/ngày (ngày đầu). Maintenance: 300mg IV x 1 lần/ngày. Truyền trong 90 phút. Thận trọng ở suy thận (chứa cyclodextrin)."
            }
        },
        "references": {
            "primary_sources": [
                "FDA Drug Label - Posaconazole (Noxafil)",
                "UpToDate - Posaconazole Drug Information",
                "IDSA Guidelines - Antifungal Therapy",
                "Goodman & Gilman's Pharmacological Basis of Therapeutics, 14th ed"
            ],
            "last_updated": "2025-02-05",
            "evidence_level": "High (FDA-approved, extensive clinical data, IDSA guidelines)"
        },
        "reversal_agents": {
            "available": False,
            "agents": [],
        },
    },

    "Voriconazole": {
        "group": "Infectious Disease - Antifungal (Azole, 2nd generation)",
        "vietnamese_name": "Voriconazole, Vfend",
        "administration": ["PO", "IV"],
        "indications": [
            "Nhiễm nấm Aspergillosis invasive",
            "Nhiễm nấm Candida (invasive, kháng fluconazole)",
            "Nhiễm nấm Fusarium",
            "Nhiễm nấm Scedosporium",
            "Nhiễm nấm Seedosporium"
        ],
        "contraindications": [
            "Dị ứng voriconazole",
            "Có thai",
            "Dùng rifampin, rifabutin, carbamazepine, phenobarbital, ergotamine"
        ],
        "dosage": {
            "adult_po_loading": "400mg x 2 lần/ngày x 2 ngày đầu",
            "adult_po_maintenance": "200mg x 2 lần/ngày",
            "adult_iv_loading": "6mg/kg x 2 lần/ngày x 2 ngày đầu",
            "adult_iv_maintenance": "4mg/kg x 2 lần/ngày",
            "notes": "Theo dõi nồng độ trong máu. Nguy cơ cao với rối loạn chuyển hóa CYP2C19"
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "IV: thay đổi chất pha (không dùng cyclodextrin)",
            "under_30": "IV: thay đổi chất pha. PO: không đổi"
        },
        "side_effects": [
            "Rối loạn thị giác (nhìn mờ, nhạy cảm ánh sáng - thường thoáng qua)",
            "Ban da (phản ứng quang hóa)",
            "Tăng men gan, suy gan",
            "Hallucination",
            "QT kéo dài",
            "Nhức đầu",
            "Buồn nôn"
        ],
        "interactions": [
            "Rifampin/Rifabutin: giảm nồng độ voriconazole - tránh dùng",
            "Carbamazepine/Phenobarbital: giảm nồng độ voriconazole - tránh dùng",
            "Warfarin: tăng tác dụng chống đông",
            "Cyclosporine/Tacrolimus: tăng nồng độ",
            "Phenytoin: giảm nồng độ voriconazole",
            "Omeprazole: tăng nồng độ omeprazole"
        ],
        "pregnancy": "D - Chống chỉ định",
        "mechanism_of_action": "Voriconazole là thuốc chống nấm phổ rộng thuộc nhóm triazole thế hệ thứ hai, ức chế enzyme lanosterol 14-alpha-demethylase (CYP51) của nấm. Enzyme này có vai trò quan trọng trong tổng hợp ergosterol, một thành phần chính của màng tế bào nấm. Bằng cách ức chế tổng hợp ergosterol, voriconazole làm thay đổi tính thấm màng tế bào nấm, dẫn đến ức chế sự phát triển và gây chết tế bào nấm. Voriconazole có phổ kháng nấm rộng hơn fluconazole: nấm men (Candida, bao gồm cả kháng fluconazole), nấm sợi (Aspergillus, Fusarium, Scedosporium), và một số nấm kháng thuốc khác. Voriconazole được coi là thuốc điều trị đầu tay cho nhiễm nấm Aspergillus invasive. Voriconazole ức chế CYP2C19, CYP2C9, và CYP3A4 ở gan, dẫn đến nhiều tương tác thuốc. Chuyển hóa phụ thuộc vào CYP2C19 (polymorphism), cần theo dõi nồng độ trong máu.",
        "monitoring": [
            "Đáp ứng điều trị (giảm triệu chứng nhiễm nấm, cải thiện lâm sàng)",
            "Nồng độ voriconazole trong máu (therapeutic drug monitoring - TDM) - QUAN TRỌNG, đặc biệt ở bệnh nhân suy gan, suy thận, hoặc có rối loạn chuyển hóa CYP2C19",
            "Chức năng gan (ALT, AST, bilirubin) - tăng men gan phổ biến, suy gan có thể nghiêm trọng",
            "Rối loạn thị giác (nhìn mờ, nhạy cảm ánh sáng, nhìn thấy ánh sáng bất thường) - thường thoáng qua, xuất hiện 30 phút sau liều, kéo dài 30 phút",
            "Dấu hiệu phản ứng quang hóa (ban da, phồng rộp) - tránh ánh nắng trực tiếp",
            "ECG - QT kéo dài (nguy cơ loạn nhịp)",
            "Hallucination - hiếm nhưng có thể xảy ra",
            "Tương tác với rifampin, rifabutin, carbamazepine, phenobarbital (giảm nồng độ voriconazole), warfarin (tăng INR), cyclosporine, tacrolimus (tăng nồng độ), phenytoin (giảm nồng độ voriconazole)"
        ],
        "precautions": [
            "CHỐNG CHỈ ĐỊNH trong thai kỳ - gây dị tật thai nhi (category D)",
            "CHỐNG CHỈ ĐỊNH với rifampin, rifabutin, carbamazepine, phenobarbital, ergotamine (giảm nồng độ voriconazole hoặc tăng nguy cơ độc tính)",
            "Theo dõi nồng độ trong máu (TDM) - QUAN TRỌNG, đặc biệt ở bệnh nhân suy gan, suy thận, hoặc có rối loạn chuyển hóa CYP2C19 (poor metabolizer có nồng độ cao, extensive metabolizer có nồng độ thấp)",
            "Liều khởi đầu (loading dose) QUAN TRỌNG - PO: 400mg x 2 lần/ngày x 2 ngày đầu, IV: 6mg/kg x 2 lần/ngày x 2 ngày đầu",
            "Rối loạn thị giác - thường thoáng qua, xuất hiện 30 phút sau liều, kéo dài 30 phút, thường tự khỏi, không cần ngừng thuốc",
            "Tránh ánh nắng trực tiếp - nguy cơ phản ứng quang hóa (ban da, phồng rộp), dùng kem chống nắng, mặc quần áo che",
            "Tăng men gan, suy gan - theo dõi chức năng gan, ngừng nếu có suy gan",
            "QT kéo dài - không dùng với các thuốc kéo dài QT khác, bệnh nhân có tiền sử rối loạn nhịp",
            "Hallucination - hiếm nhưng có thể xảy ra, cần theo dõi",
            "Nhiều tương tác thuốc do ức chế CYP - tăng nồng độ warfarin (tăng INR), cyclosporine, tacrolimus (tăng nồng độ, nguy cơ độc tính), omeprazole (tăng nồng độ)",
            "Phenytoin giảm nồng độ voriconazole - có thể cần tăng liều voriconazole",
            "IV chứa cyclodextrin - không dùng ở suy thận nặng (CrCl <50), tích lũy cyclodextrin",
            "Uống với hoặc không thức ăn (không ảnh hưởng hấp thu như itraconazole)"
        ],
        "pharmacokinetics": {
            "half_life": "6 giờ (bình thường), tăng ở poor CYP2C19 metabolizers",
            "onset": "Vài ngày đến vài tuần (tác dụng chống nấm)",
            "duration": "12 giờ (dùng 2 lần/ngày)",
            "protein_binding": "58%",
            "clearance": "Gan: chuyển hóa qua CYP2C19 (chính), CYP2C9, và CYP3A4. Chuyển hóa phụ thuộc vào polymorphism CYP2C19 (poor metabolizer có nồng độ cao, extensive metabolizer có nồng độ thấp). Thận: bài tiết một phần metabolites. IV chứa cyclodextrin, tích lũy ở suy thận."
        },
        "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm, tránh ánh sáng. Viên nén: bảo quản trong bao bì kín. IV: bảo quản trong tủ lạnh (2-8°C), để nhiệt độ phòng trước khi pha, dùng trong vòng 24 giờ sau khi pha.",
        "black_box_warnings": "CHỐNG CHỈ ĐỊNH trong thai kỳ - gây dị tật thai nhi (category D). Nguy cơ suy gan nghiêm trọng, có thể gây tử vong. Theo dõi chức năng gan trước và trong khi điều trị. Ngừng ngay nếu có suy gan. Nguy cơ QT kéo dài và rối loạn nhịp tim. Theo dõi ECG nếu có nguy cơ. Nguy cơ rối loạn thị giác (thường thoáng qua). CHỐNG CHỈ ĐỊNH với rifampin, rifabutin, carbamazepine, phenobarbital, ergotamine.",
        "risk_flags": {
            "high_alert": True,
            "narrow_therapeutic_index": True,
            "bleeding_risk": False,
            "organ_toxicity": ["Hepatotoxicity - CRITICAL", "QT prolongation", "Visual disturbances", "Renal toxicity (IV vehicle accumulation)"],
            "qt_prolongation": True,
            "hepatotoxicity": True,
            "nephrotoxicity": True,
            "requires_monitoring": ["Therapeutic Drug Monitoring (TDM) - CRITICAL", "Hepatic function (ALT, AST, bilirubin)", "Visual function (acuity, visual field)", "ECG", "Renal function (for IV vehicle)", "Cyclosporine/Tacrolimus levels if co-administered", "INR if co-administered with warfarin"]
        },
        "guideline_tags": [
            "IDSA Invasive Aspergillosis Guidelines 2024",
            "IDSA Candidiasis Guidelines 2024",
            "FDA Black Box Warning - Voriconazole and Pregnancy (Category D)",
            "FDA Black Box Warning - Voriconazole and Hepatotoxicity",
            "FDA Black Box Warning - Voriconazole and QT Prolongation",
            "ESCMID-ECMM-ERS Guidelines for Aspergillus"
        ],
        "drug_interactions": {
            "major": [
                {
                    "drug": "Rifampin, Rifabutin",
                    "mechanism": "Rifampin và rifabutin cảm ứng CYP450 mạnh, làm tăng chuyển hóa voriconazole, giảm nồng độ voriconazole trong máu.",
                    "effect": "Giảm nồng độ voriconazole đáng kể, giảm hiệu quả điều trị, nguy cơ thất bại điều trị",
                    "management": "CHỐNG CHỈ ĐỊNH - không dùng đồng thời. Nếu bắt buộc, tăng liều voriconazole (có thể cần tăng gấp đôi), theo dõi nồng độ voriconazole trong máu."
                },
                {
                    "drug": "Carbamazepine, Phenobarbital",
                    "mechanism": "Carbamazepine và phenobarbital cảm ứng CYP450 mạnh, làm tăng chuyển hóa voriconazole, giảm nồng độ voriconazole trong máu.",
                    "effect": "Giảm nồng độ voriconazole đáng kể, giảm hiệu quả điều trị",
                    "management": "CHỐNG CHỈ ĐỊNH - không dùng đồng thời. Nếu bắt buộc, tăng liều voriconazole, theo dõi nồng độ voriconazole trong máu."
                },
                {
                    "drug": "Ergotamine",
                    "mechanism": "Voriconazole ức chế CYP3A4, làm giảm chuyển hóa ergotamine, tăng nồng độ ergotamine trong máu.",
                    "effect": "Tăng nguy cơ co thắt mạch máu nghiêm trọng, hoại tử chi, đe dọa tính mạng",
                    "management": "CHỐNG CHỈ ĐỊNH - không dùng đồng thời."
                }
            ],
            "moderate": [
                {
                    "drug": "Warfarin",
                    "mechanism": "Voriconazole ức chế CYP2C9, làm giảm chuyển hóa warfarin, tăng nồng độ warfarin trong máu.",
                    "effect": "Tăng tác dụng chống đông, tăng INR, tăng nguy cơ chảy máu",
                    "management": "Theo dõi INR chặt chẽ khi bắt đầu, thay đổi liều, hoặc ngừng voriconazole. Giảm liều warfarin 25-50% khi bắt đầu voriconazole."
                },
                {
                    "drug": "Cyclosporine, Tacrolimus",
                    "mechanism": "Voriconazole ức chế CYP3A4, làm giảm chuyển hóa cyclosporine và tacrolimus, tăng nồng độ trong máu.",
                    "effect": "Tăng nồng độ cyclosporine/tacrolimus, tăng độc tính (độc thận, tăng huyết áp, rối loạn điện giải)",
                    "management": "Theo dõi nồng độ cyclosporine/tacrolimus chặt chẽ. Giảm liều cyclosporine/tacrolimus 50-75% khi bắt đầu voriconazole."
                },
                {
                    "drug": "Phenytoin",
                    "mechanism": "Phenytoin cảm ứng CYP450, làm giảm nồng độ voriconazole. Voriconazole ức chế CYP2C9, tăng nồng độ phenytoin.",
                    "effect": "Giảm nồng độ voriconazole, tăng nồng độ phenytoin",
                    "management": "Theo dõi nồng độ cả hai thuốc. Tăng liều voriconazole (có thể cần tăng gấp đôi), giảm liều phenytoin nếu cần."
                }
            ],
            "minor": [
                {
                    "drug": "Omeprazole",
                    "mechanism": "Voriconazole ức chế CYP2C19, làm giảm chuyển hóa omeprazole, tăng nồng độ omeprazole trong máu.",
                    "effect": "Tăng nhẹ nồng độ omeprazole",
                    "management": "Theo dõi dấu hiệu độc tính omeprazole. Có thể cần giảm liều omeprazole."
                }
            ]
        },
        "contraindications": {
            "tuyệt_đối": [
                "Dị ứng voriconazole",
                "Có thai - chống chỉ định tuyệt đối, gây dị tật thai nhi (category D)",
                "Dùng với rifampin, rifabutin, carbamazepine, phenobarbital, ergotamine - chống chỉ định"
            ],
            "tương_đối": [
                "Suy thận nặng (CrCl <50) khi dùng IV - không dùng IV (chứa cyclodextrin, tích lũy), có thể dùng PO",
                "Suy gan - thận trọng, theo dõi chức năng gan, ngừng nếu có suy gan",
                "Rối loạn chuyển hóa CYP2C19 (poor metabolizer) - tăng nồng độ, tăng độc tính, cần giảm liều",
                "Rối loạn chuyển hóa CYP2C19 (extensive metabolizer) - giảm nồng độ, có thể cần tăng liều",
                "Bệnh nhân có tiền sử rối loạn nhịp tim - nguy cơ QT kéo dài"
            ]
        },
        "contraindications_detail": {
            "tuyệt_đối": [
                "Dị ứng voriconazole",
                "Có thai - chống chỉ định tuyệt đối, gây dị tật thai nhi (category D)",
                "Dùng với rifampin, rifabutin, carbamazepine, phenobarbital, ergotamine - chống chỉ định"
            ],
            "tương_đối": [
                "Suy thận nặng (CrCl <50) khi dùng IV - không dùng IV (chứa cyclodextrin, tích lũy), có thể dùng PO",
                "Suy gan - thận trọng, theo dõi chức năng gan, ngừng nếu có suy gan",
                "Rối loạn chuyển hóa CYP2C19 (poor metabolizer) - tăng nồng độ, tăng độc tính, cần giảm liều",
                "Rối loạn chuyển hóa CYP2C19 (extensive metabolizer) - giảm nồng độ, có thể cần tăng liều",
                "Bệnh nhân có tiền sử rối loạn nhịp tim - nguy cơ QT kéo dài"
            ]
        },
        "reversal_agents": {
            "available": False,
            "agents": [],
            "notes": "Không có antidote đặc hiệu. Điều trị quá liều chủ yếu là hỗ trợ."
        },
        "pregnancy_lactation": {
            "fda_category": "D",
            "pregnancy_details": "Chống chỉ định trong thai kỳ. Voriconazole gây dị tật thai nhi, đặc biệt trong 3 tháng đầu. Có thể gây sẩy thai, dị tật xương, dị tật tim. Không dùng trong thai kỳ trừ khi lợi ích vượt trội rõ ràng so với nguy cơ.",
            "lactation": {
                "safety": "Incompatible",
                "details": "Voriconazole bài tiết vào sữa mẹ. Thuốc có thể gây độc tính cho trẻ sơ sinh.",
                "recommendation": "Không cho con bú khi dùng voriconazole. Ngừng cho con bú hoặc ngừng thuốc."
            }
        },
        "hepatic_adjustment": {
            "mild": "Không đổi",
            "moderate": "Thận trọng, theo dõi chức năng gan, có thể cần giảm liều",
            "severe": "Tránh dùng hoặc giảm liều mạnh, theo dõi chặt chẽ",
            "notes": "Voriconazole chuyển hóa chủ yếu qua gan (CYP2C19, CYP2C9, CYP3A4). Suy gan làm giảm chuyển hóa, tăng nồng độ và độc tính. Theo dõi chức năng gan và nồng độ voriconazole trong máu, ngừng nếu có suy gan."
        },
        "overdose_management": {
            "symptoms": [
                "Rối loạn thị giác (nhìn mờ, nhạy cảm ánh sáng)",
                "Tăng men gan, suy gan",
                "Ban da (phản ứng quang hóa)",
                "Hallucination",
                "QT kéo dài, rối loạn nhịp tim",
                "Buồn nôn, nôn"
            ],
            "antidote": "Không có antidote đặc hiệu",
            "treatment": [
                "Ngừng ngay voriconazole",
                "Rửa dạ dày nếu mới uống <1 giờ",
                "Supportive care",
                "Theo dõi chức năng gan, ECG",
                "Điều trị suy gan nếu có (supportive care)",
                "Theo dõi và điều trị rối loạn nhịp tim nếu có",
                "Tránh ánh nắng trực tiếp (phản ứng quang hóa)"
            ],
            "monitoring": "Chức năng gan, ECG, nồng độ voriconazole trong máu, dấu hiệu lâm sàng"
        },
        "reversal_agents": None,
        "administration_instructions": {
            "oral": {
                "with_food": "Uống với hoặc không thức ăn (không ảnh hưởng hấp thu)",
                "timing": "Chia 2 lần/ngày. Loading dose: 400mg x 2 lần/ngày x 2 ngày đầu, sau đó 200mg x 2 lần/ngày."
            },
            "iv": {
                "reconstitution": "Pha với NS hoặc D5W theo hướng dẫn nhà sản xuất",
                "infusion_rate": "Truyền trong 1-2 giờ",
                "compatibility": ["NS", "D5W"],
                "incompatibility": [],
                "notes": "Không dùng IV nếu CrCl <50 (chứa cyclodextrin, tích lũy ở suy thận). Loading dose: 6mg/kg x 2 lần/ngày x 2 ngày đầu, sau đó 4mg/kg x 2 lần/ngày. Truyền trong 1-2 giờ."
            }
        },
        "references": {
            "primary_sources": [
                "FDA Drug Label - Voriconazole (Vfend)",
                "UpToDate - Voriconazole Drug Information",
                "Goodman & Gilman's Pharmacological Basis of Therapeutics, 14th ed"
            ],
            "last_updated": "2025-01-15",
            "evidence_level": "High (FDA-approved, extensive clinical data)"
        },
        "reversal_agents": {
            "available": False,
            "agents": [],
        },
    },
    
}

__all__ = ['AZOLES_DRUGS']
