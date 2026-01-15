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
            "icu_critical_care_only": False,
            "bleeding_risk": "High (with warfarin)",
            "organ_toxicity": {"hepatic": "Hepatotoxicity (especially with high doses or prolonged use)", "cardiovascular": "QT prolongation (high doses ≥400mg/day)", "dermatologic": "SJS/TEN (rare)", "teratogenic": "Teratogenicity (Category D in 1st trimester)"},
            "qt_prolongation": True,
            "hepatotoxicity": True,
            "nephrotoxicity": False,
            "requires_monitoring": ["Hepatic function (ALT, AST - especially with high doses or prolonged use)", "Renal function (creatinine, BUN - dose adjustment required)", "ECG (QT prolongation risk with high doses ≥400mg/day)", "PT/INR (if used with warfarin - critical interaction)", "Blood glucose (if used with sulfonylureas)", "Phenytoin levels (if used with phenytoin)", "Cyclosporine/Tacrolimus levels (if used with immunosuppressants)"],
            "look_alike_sound_alike": ["Fluconazole", "Flucytosine"]
        },
        "guideline_tags": [
            "FDA Black Box Warning - Teratogenicity (Category D in 1st trimester)",
            "IDSA Guidelines - Antifungal Therapy",
            "IDSA Guidelines - Candidiasis",
            "IDSA Guidelines - Cryptococcosis",
            "WHO Essential Medicines List"
        ],
        "last_updated": "2025-02-18",
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
            "icu_critical_care_only": False,
            "bleeding_risk": "High (with warfarin)",
            "organ_toxicity": {"cardiovascular": "Black Box Warning - Congestive heart failure (contraindicated in CHF)", "hepatic": "Black Box Warning - Hepatotoxicity (may be severe)", "cardiovascular_other": "QT prolongation (with quinidine)", "teratogenic": "Teratogenicity (Category D)", "musculoskeletal": "Rhabdomyolysis (with simvastatin/lovastatin)"},
            "qt_prolongation": True,
            "hepatotoxicity": True,
            "nephrotoxicity": False,
            "requires_monitoring": ["Black Box Warning - Heart failure signs (edema, dyspnea, weight gain - contraindicated in CHF)", "Hepatic function (ALT, AST, bilirubin - Black Box Warning for hepatotoxicity)", "ECG (QT prolongation risk with quinidine)", "PT/INR (if used with warfarin - critical interaction)", "Digoxin levels (if used with digoxin)", "Phenytoin levels (if used with phenytoin)", "CK (rhabdomyolysis risk with simvastatin/lovastatin)", "CYP3A4 interactions (many critical drug interactions)"],
            "look_alike_sound_alike": ["Itraconazole", "Fluconazole"]
        },
        "guideline_tags": [
            "FDA Black Box Warning - Congestive Heart Failure (contraindicated in CHF)",
            "FDA Black Box Warning - Hepatotoxicity (may be severe)",
            "FDA Black Box Warning - Teratogenicity (Category D)",
            "IDSA Guidelines - Antifungal Therapy",
            "IDSA Guidelines - Aspergillosis",
            "IDSA Guidelines - Blastomycosis",
            "IDSA Guidelines - Histoplasmosis",
            "WHO Essential Medicines List"
        ],
        "last_updated": "2025-02-18",
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
            "icu_critical_care_only": False,
            "bleeding_risk": "High (with warfarin)",
            "organ_toxicity": {"hepatic": "Black Box Warning - Hepatotoxicity (may be severe, may be fatal)", "cardiovascular": "Black Box Warning - QT prolongation", "neurological": "Visual disturbances (common, usually transient)", "ophthalmic": "Photosensitivity (severe skin reactions)", "renal": "Nephrotoxicity (IV vehicle - cyclodextrin accumulation)", "teratogenic": "Teratogenicity (Category D)"},
            "qt_prolongation": True,
            "hepatotoxicity": True,
            "nephrotoxicity": True,
            "requires_monitoring": ["TDM required (trough levels - Black Box Warning, narrow therapeutic index, CYP2C19 polymorphism)", "Hepatic function (ALT, AST, bilirubin - Black Box Warning for hepatotoxicity)", "ECG (Black Box Warning - QT prolongation)", "Visual function (visual disturbances - common, usually transient)", "Photosensitivity (severe skin reactions - avoid sunlight)", "Renal function (for IV - cyclodextrin accumulation, avoid IV if CrCl <50)", "Cyclosporine/Tacrolimus levels (if used with immunosuppressants)", "PT/INR (if used with warfarin - critical interaction)"],
            "look_alike_sound_alike": ["Voriconazole", "Fluconazole"]
        },
        "guideline_tags": [
            "FDA Black Box Warning - Hepatotoxicity (may be severe, may be fatal)",
            "FDA Black Box Warning - QT Prolongation",
            "FDA Black Box Warning - Teratogenicity (Category D)",
            "IDSA Guidelines - Invasive Aspergillosis",
            "IDSA Guidelines - Candidiasis",
            "ESCMID-ECMM-ERS Guidelines - Aspergillus",
            "WHO Essential Medicines List"
        ],
        "last_updated": "2025-02-18",
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
    
    "Vivjoa": {
                "group": "FDA Approved 2022",
                "vietnamese_name": "Oteseconazole, Vivjoa",
                "administration": [
                        "PO",
                ],
                "indications": [
                        "Giảm tỷ lệ tái phát viêm âm đạo do nấm Candida tái phát (RVVC) ở phụ nữ có tiền sử RVVC và không còn khả năng sinh sản",
                        "Điều trị dự phòng RVVC sau khi đã điều trị đợt cấp bằng thuốc kháng nấm azole",
                ],
                "contraindications": [
                        "Dị ứng oteseconazole hoặc bất kỳ thành phần nào",
                        "Phụ nữ có khả năng sinh sản (phải xác nhận không có khả năng sinh sản trước khi dùng)",
                        "Có thai hoặc đang cho con bú",
                ],
                "dosage": {
                        "adult_standard": "150mg PO x 2 lần/ngày (sáng và tối) x 14 ngày, sau đó 150mg PO x 1 lần/tuần x 11 tuần (tổng cộng 12 tuần điều trị)",
                        "adult_loading": "150mg PO x 2 lần/ngày x 14 ngày (liều nạp)",
                        "adult_maintenance": "150mg PO x 1 lần/tuần x 11 tuần (liều duy trì)",
                        "notes": "Uống với thức ăn để tăng hấp thu. Chỉ dùng cho phụ nữ không còn khả năng sinh sản (postmenopausal, đã cắt tử cung/buồng trứng, hoặc xác nhận không có khả năng sinh sản). FDA phê duyệt 2022.",
                },
                "renal_adjustment": {
                        "normal": "Không cần chỉnh liều",
                        "30_60": "Không cần chỉnh liều (CrCl ≥30)",
                        "under_30": "Thận trọng, dữ liệu hạn chế ở bệnh nhân suy thận nặng (CrCl <30)",
                        "hemodialysis": "Dữ liệu hạn chế, thận trọng",
                },
                "side_effects": [
                        "Nhức đầu (thường gặp)",
                        "Buồn nôn (thường gặp)",
                        "Tiêu chảy (thường gặp)",
                        "Đau bụng",
                        "Đầy hơi",
                        "Chóng mặt",
                        "Mệt mỏi",
                        "Tăng men gan (hiếm)",
                        "Phát ban (hiếm)",
                        "Rối loạn vị giác",
                ],
                "interactions": [
                        "CYP3A4 substrates: Oteseconazole là chất ức chế CYP3A4 mạnh, có thể tăng nồng độ các thuốc chuyển hóa qua CYP3A4 (statins, warfarin, cyclosporine, tacrolimus, v.v.)",
                        "CYP3A4 inducers (rifampin, carbamazepine, phenytoin): Có thể giảm nồng độ oteseconazole, giảm hiệu quả",
                        "Thuốc tránh thai nội tiết: Có thể tăng nồng độ, tăng nguy cơ tác dụng phụ",
                        "Warfarin: Tăng tác dụng chống đông, tăng INR",
                        "Statin (atorvastatin, simvastatin): Tăng nguy cơ tiêu cơ vân",
                ],
                "pregnancy": "X - Chống chỉ định trong thai kỳ",
                "mechanism_of_action": "Oteseconazole là thuốc kháng nấm azole thế hệ mới, ức chế enzyme lanosterol 14α-demethylase (CYP51) của nấm Candida. Enzyme này chuyển lanosterol thành ergosterol - thành phần quan trọng của màng tế bào nấm. Ức chế tổng hợp ergosterol → màng tế bào nấm không ổn định, rò rỉ, chết tế bào. Oteseconazole có ái lực cao với CYP51 của Candida, có thời gian bán thải rất dài (khoảng 138 ngày), cho phép dùng liều duy trì hàng tuần. Đặc điểm quan trọng: Oteseconazole có ái lực thấp với CYP51 của người, ít ảnh hưởng đến tổng hợp steroid ở người so với các azole khác. Tuy nhiên, oteseconazole là chất ức chế CYP3A4 mạnh, có nhiều tương tác thuốc. FDA phê duyệt 2022 để giảm tỷ lệ tái phát RVVC ở phụ nữ không còn khả năng sinh sản.",
                "monitoring": [
                        "Xác nhận bệnh nhân không còn khả năng sinh sản trước khi bắt đầu điều trị",
                        "Theo dõi đáp ứng điều trị (giảm tần suất tái phát RVVC)",
                        "Theo dõi tác dụng phụ (nhức đầu, buồn nôn, tiêu chảy)",
                        "Chức năng gan (ALT, AST) nếu có triệu chứng hoặc dùng kéo dài",
                        "INR nếu dùng với warfarin",
                        "Creatine kinase (CK) nếu dùng với statin",
                        "Theo dõi tương tác thuốc với các thuốc chuyển hóa qua CYP3A4",
                ],
                "precautions": [
                        "CHỈ dùng cho phụ nữ không còn khả năng sinh sản (postmenopausal, đã cắt tử cung/buồng trứng, hoặc xác nhận không có khả năng sinh sản). CHỐNG CHỈ ĐỊNH ở phụ nữ có khả năng sinh sản do thời gian bán thải rất dài (138 ngày), có thể gây hại cho thai nhi nếu có thai sau khi ngừng thuốc.",
                        "Uống với thức ăn để tăng hấp thu và giảm tác dụng phụ đường tiêu hóa",
                        "Thận trọng với tương tác thuốc: Oteseconazole là chất ức chế CYP3A4 mạnh, có thể tăng nồng độ nhiều thuốc (statins, warfarin, cyclosporine, tacrolimus, v.v.)",
                        "Theo dõi INR chặt chẽ nếu dùng với warfarin (tăng nguy cơ chảy máu)",
                        "Theo dõi CK nếu dùng với statin (tăng nguy cơ tiêu cơ vân)",
                        "Tránh dùng với các chất cảm ứng CYP3A4 mạnh (rifampin, carbamazepine, phenytoin) vì có thể giảm hiệu quả",
                        "Thận trọng ở bệnh nhân suy gan, suy thận nặng (dữ liệu hạn chế)",
                        "Theo dõi chức năng gan nếu có triệu chứng hoặc dùng kéo dài",
                        "Dùng đủ thời gian (12 tuần) để đạt hiệu quả tối đa",
                ],
                "pharmacokinetics": {
                        "half_life": "Khoảng 138 ngày (rất dài, cho phép dùng liều duy trì hàng tuần)",
                        "onset": "Vài ngày đến vài tuần (tác dụng dự phòng tái phát)",
                        "duration": "Rất dài do half-life rất dài (138 ngày), có thể duy trì nồng độ hiệu quả trong nhiều tháng sau khi ngừng thuốc",
                        "protein_binding": ">99% (gắn kết cao với protein huyết tương)",
                        "metabolism": "Chuyển hóa chủ yếu qua gan bởi CYP3A4 và CYP2C9, tạo ra các chất chuyển hóa không hoạt động",
                        "clearance": "Chủ yếu qua gan (chuyển hóa), một phần nhỏ qua thận. Thời gian bán thải rất dài do gắn kết cao với protein và chuyển hóa chậm.",
                },
                "storage": "Bảo quản ở nhiệt độ phòng (20-25°C), tránh ẩm và ánh sáng trực tiếp. Bảo quản trong hộp gốc, đậy kín.",
                "black_box_warnings": "CHỐNG CHỈ ĐỊNH ở phụ nữ có khả năng sinh sản. Oteseconazole có thời gian bán thải rất dài (138 ngày), có thể gây hại cho thai nhi nếu có thai sau khi ngừng thuốc. Chỉ dùng cho phụ nữ không còn khả năng sinh sản (postmenopausal, đã cắt tử cung/buồng trứng, hoặc xác nhận không có khả năng sinh sản).",
                "drug_interactions": {
                        "major": [
                                {
                                        "drug": "Warfarin",
                                        "mechanism": "Oteseconazole ức chế CYP3A4 và CYP2C9, làm giảm chuyển hóa warfarin, tăng nồng độ warfarin.",
                                        "effect": "Tăng tác dụng chống đông, tăng INR, tăng nguy cơ chảy máu nghiêm trọng",
                                        "management": "Theo dõi INR chặt chẽ khi bắt đầu, thay đổi liều, hoặc ngừng oteseconazole. Giảm liều warfarin 25-50% khi bắt đầu oteseconazole. Điều chỉnh liều warfarin theo INR."
                                },
                                {
                                        "drug": "Statin (atorvastatin, simvastatin, lovastatin)",
                                        "mechanism": "Oteseconazole ức chế CYP3A4, làm giảm chuyển hóa statin, tăng nồng độ statin.",
                                        "effect": "Tăng nguy cơ tiêu cơ vân (rhabdomyolysis), đau cơ, suy thận cấp",
                                        "management": "Tránh dùng với simvastatin, lovastatin. Giảm liều atorvastatin 50% hoặc dùng statin không chuyển hóa qua CYP3A4 (pravastatin, rosuvastatin). Theo dõi CK và triệu chứng đau cơ."
                                },
                                {
                                        "drug": "Cyclosporine, Tacrolimus",
                                        "mechanism": "Oteseconazole ức chế CYP3A4, làm giảm chuyển hóa cyclosporine và tacrolimus.",
                                        "effect": "Tăng nồng độ cyclosporine/tacrolimus, tăng độc tính (độc thận, tăng huyết áp, độc thần kinh)",
                                        "management": "Giảm liều cyclosporine/tacrolimus 25-50% khi bắt đầu oteseconazole. Theo dõi nồng độ cyclosporine/tacrolimus, chức năng thận. Điều chỉnh liều theo nồng độ."
                                },
                        ],
                        "moderate": [
                                {
                                        "drug": "Rifampin, Carbamazepine, Phenytoin (CYP3A4 inducers)",
                                        "mechanism": "Các thuốc cảm ứng CYP3A4 làm tăng chuyển hóa oteseconazole, giảm nồng độ oteseconazole.",
                                        "effect": "Giảm nồng độ oteseconazole, giảm hiệu quả điều trị RVVC",
                                        "management": "Tránh dùng đồng thời nếu có thể. Nếu phải dùng, theo dõi đáp ứng điều trị và cân nhắc tăng liều oteseconazole (dữ liệu hạn chế)."
                                },
                                {
                                        "drug": "Thuốc tránh thai nội tiết",
                                        "mechanism": "Oteseconazole ức chế CYP3A4, có thể tăng nồng độ estrogen và progestin.",
                                        "effect": "Tăng nguy cơ tác dụng phụ của thuốc tránh thai (buồn nôn, đau đầu, huyết khối)",
                                        "management": "Theo dõi tác dụng phụ. Lưu ý: Oteseconazole chỉ dùng cho phụ nữ không còn khả năng sinh sản, nên ít khi dùng với thuốc tránh thai."
                                },
                        ],
                        "minor": [],
                },
                "contraindications_detail": {
                        "tuyệt_đối": [
                                "Dị ứng oteseconazole hoặc bất kỳ thành phần nào",
                                "Phụ nữ có khả năng sinh sản (phải xác nhận không có khả năng sinh sản trước khi dùng)",
                                "Có thai hoặc đang cho con bú",
                        ],
                        "tương_đối": [
                                "Suy gan nặng (dữ liệu hạn chế, thận trọng)",
                                "Suy thận nặng (CrCl <30, dữ liệu hạn chế, thận trọng)",
                                "Dùng đồng thời với các chất cảm ứng CYP3A4 mạnh (rifampin, carbamazepine, phenytoin) - có thể giảm hiệu quả",
                        ],
                },
                "pregnancy_lactation": {
                        "fda_category": "X",
                        "pregnancy_details": "CHỐNG CHỈ ĐỊNH trong thai kỳ. Oteseconazole có thời gian bán thải rất dài (138 ngày), có thể gây hại cho thai nhi nếu có thai sau khi ngừng thuốc. Chỉ dùng cho phụ nữ không còn khả năng sinh sản. Nếu có thai trong khi dùng hoặc sau khi ngừng thuốc, cần thông báo ngay cho bác sĩ.",
                        "lactation": {
                                "safety": "Chống chỉ định",
                                "details": "Chưa biết oteseconazole có bài tiết vào sữa mẹ hay không, nhưng do thời gian bán thải rất dài (138 ngày) và có thể gây hại cho trẻ sơ sinh, nên chống chỉ định khi cho con bú.",
                                "recommendation": "Không dùng khi đang cho con bú. Nếu cần điều trị, nên ngừng cho con bú hoặc chọn phương pháp điều trị khác.",
                        },
                },
                "hepatic_adjustment": {
                        "mild": "Không cần chỉnh liều",
                        "moderate": "Thận trọng, theo dõi chặt chẽ (dữ liệu hạn chế)",
                        "severe": "Thận trọng, dữ liệu hạn chế, cân nhắc giảm liều hoặc tránh dùng",
                        "notes": "Oteseconazole chuyển hóa chủ yếu qua gan bởi CYP3A4 và CYP2C9. Ở bệnh nhân suy gan, có thể tăng nồng độ và tăng nguy cơ tác dụng phụ. Dữ liệu hạn chế ở bệnh nhân suy gan nặng.",
                },
                "overdose_management": {
                        "symptoms": [
                                "Buồn nôn, nôn",
                                "Tiêu chảy",
                                "Nhức đầu",
                                "Chóng mặt",
                                "Mệt mỏi",
                                "Tăng men gan (nếu quá liều lớn)",
                        ],
                        "antidote": "Không có antidote đặc hiệu",
                        "treatment": [
                                "Điều trị hỗ trợ",
                                "Theo dõi dấu hiệu sinh tồn",
                                "Theo dõi chức năng gan nếu có triệu chứng",
                                "Rửa dạ dày nếu uống quá liều trong vòng 1-2 giờ",
                                "Than hoạt tính có thể hữu ích nếu uống quá liều gần đây",
                        ],
                        "monitoring": "Theo dõi dấu hiệu sinh tồn, chức năng gan, triệu chứng lâm sàng. Do thời gian bán thải rất dài (138 ngày), cần theo dõi kéo dài.",
                },
                "reversal_agents": {
                        "available": False,
                        "agents": [],
                },
                "administration_instructions": {
                        "oral": {
                                "with_food": "Uống với thức ăn để tăng hấp thu và giảm tác dụng phụ đường tiêu hóa",
                                "timing": "Liều nạp: 150mg x 2 lần/ngày (sáng và tối) x 14 ngày. Liều duy trì: 150mg x 1 lần/tuần x 11 tuần. Uống cùng thời điểm mỗi ngày/tuần để duy trì nồng độ ổn định.",
                        },
                },
                "references": {
                        "primary_sources": [
                                "FDA Drug Label - Oteseconazole (Vivjoa)",
                                "FDA Approval Date: April 26, 2022",
                                "FDA-approved use: To reduce the incidence of recurrent vulvovaginal candidiasis (RVVC) in females with a history of RVVC who are not of reproductive potential",
                        ],
                        "last_updated": "2026-01-15",
                        "evidence_level": "A - FDA-approved 2022",
                },
                "risk_flags": {
                        "high_alert": False,
                        "narrow_therapeutic_index": False,
                        "bleeding_risk": False,
                        "organ_toxicity": [
                                "Hepatotoxicity (hiếm, nhưng có thể xảy ra)",
                        ],
                        "qt_prolongation": False,
                        "hepatotoxicity": True,
                        "nephrotoxicity": False,
                        "requires_monitoring": [
                                "Clinical response",
                                "Adverse effects",
                                "Liver function (if symptoms or prolonged use)",
                                "Drug interactions (CYP3A4 substrates)",
                        ],
                },
                "guideline_tags": [
                        "FDA Drug Information - Oteseconazole (Vivjoa)",
                        "Recurrent Vulvovaginal Candidiasis",
                        "Antifungal - Azole",
                ],
                "last_updated": "2026-01-15",
        },
    "Bimzelx": {
                "group": "FDA Approved 2023",
                "vietnamese_name": "Bimekizumab, Bimzelx",
                "administration": [
                        "SC",
                ],
                "indications": [
                        "Điều trị vảy nến mảng bám từ trung bình đến nặng ở người lớn là ứng viên cho liệu pháp toàn thân hoặc quang trị liệu",
                        "Điều trị viêm khớp vảy nến (psoriatic arthritis) ở người lớn",
                ],
                "contraindications": [
                        "Dị ứng bimekizumab hoặc bất kỳ thành phần nào",
                        "Nhiễm trùng hoạt động nghiêm trọng",
                ],
                "dosage": {
                        "adult_standard": "320mg SC (tiêm 2 lần, mỗi lần 160mg ở 2 vị trí khác nhau) x 1 lần/4 tuần sau liều nạp",
                        "adult_loading": "320mg SC (tiêm 2 lần, mỗi lần 160mg) tại tuần 0, 4, 8, 12, 16",
                        "adult_maintenance": "320mg SC x 1 lần/4 tuần (bắt đầu từ tuần 20)",
                        "adult_alternative": "320mg SC x 1 lần/8 tuần có thể được xem xét ở một số bệnh nhân sau khi đạt đáp ứng",
                        "notes": "Tiêm dưới da (SC) ở vùng đùi, bụng, hoặc cánh tay. Làm ấm đến nhiệt độ phòng trước khi tiêm. FDA phê duyệt 2023.",
                },
                "renal_adjustment": {
                        "normal": "Không cần chỉnh liều",
                        "30_60": "Không cần chỉnh liều",
                        "under_30": "Không cần chỉnh liều (monoclonal antibody, không thải qua thận)",
                        "hemodialysis": "Không cần chỉnh liều",
                },
                "side_effects": [
                        "Nhiễm trùng đường hô hấp trên (thường gặp)",
                        "Nhiễm trùng nấm Candida (oral candidiasis, vulvovaginal candidiasis) - thường gặp do ức chế IL-17",
                        "Phản ứng tại chỗ tiêm (đau, đỏ, sưng, ngứa)",
                        "Nhức đầu",
                        "Mệt mỏi",
                        "Buồn nôn",
                        "Tiêu chảy",
                        "Tăng men gan (ALT, AST) - hiếm",
                        "Giảm bạch cầu trung tính (neutropenia) - hiếm",
                        "Nhiễm trùng nghiêm trọng (viêm phổi, nhiễm trùng da, nhiễm trùng huyết) - hiếm nhưng có thể xảy ra",
                        "Phản ứng dị ứng (phát ban, nổi mề đay, phù mạch) - hiếm",
                ],
                "interactions": [
                        "Vắc-xin sống: Bimekizumab ức chế miễn dịch, có thể làm giảm hiệu quả vắc-xin sống và tăng nguy cơ nhiễm trùng từ vắc-xin sống. Tránh dùng vắc-xin sống trong khi điều trị và ít nhất 16 tuần sau khi ngừng bimekizumab.",
                        "Thuốc ức chế miễn dịch khác: Có thể tăng nguy cơ nhiễm trùng. Thận trọng khi dùng đồng thời.",
                        "Cyclosporine, Methotrexate: Có thể dùng đồng thời nhưng cần theo dõi chặt chẽ tác dụng phụ và nhiễm trùng.",
                ],
                "pregnancy": "Không phân loại (chưa có dữ liệu đầy đủ)",
                "mechanism_of_action": "Bimekizumab là kháng thể đơn dòng (monoclonal antibody) IgG1 humanized, ức chế đồng thời cả interleukin-17A (IL-17A) và interleukin-17F (IL-17F). IL-17A và IL-17F là các cytokine tiền viêm quan trọng trong bệnh sinh của vảy nến và viêm khớp vảy nến. Bằng cách ức chế cả hai cytokine này, bimekizumab làm giảm quá trình viêm, giảm tăng sinh tế bào sừng, và cải thiện các tổn thương da và khớp. Đặc điểm quan trọng: Bimekizumab là thuốc duy nhất ức chế đồng thời cả IL-17A và IL-17F, trong khi các thuốc khác (secukinumab, ixekizumab) chỉ ức chế IL-17A. FDA phê duyệt 2023 để điều trị vảy nến mảng bám từ trung bình đến nặng và viêm khớp vảy nến.",
                "monitoring": [
                        "Theo dõi đáp ứng điều trị (PASI score, BSA, PGA)",
                        "Theo dõi dấu hiệu nhiễm trùng (sốt, ho, khó thở, đau họng, tiểu buốt, tiểu gắt)",
                        "Nhiễm trùng nấm Candida (oral candidiasis, vulvovaginal candidiasis) - theo dõi triệu chứng và điều trị nếu cần",
                        "Công thức máu (CBC) - theo dõi bạch cầu trung tính",
                        "Chức năng gan (ALT, AST) - nếu có triệu chứng",
                        "Phản ứng tại chỗ tiêm",
                        "Phản ứng dị ứng (phát ban, nổi mề đay, phù mạch)",
                        "Dấu hiệu viêm ruột (IBD) - bimekizumab có thể làm trầm trọng hoặc gây viêm ruột mới",
                ],
                "precautions": [
                        "Nhiễm trùng: Bimekizumab ức chế miễn dịch, có thể tăng nguy cơ nhiễm trùng. Không bắt đầu điều trị ở bệnh nhân có nhiễm trùng hoạt động nghiêm trọng. Nếu phát triển nhiễm trùng nghiêm trọng trong khi điều trị, tạm ngừng bimekizumab cho đến khi nhiễm trùng được kiểm soát.",
                        "Nhiễm trùng nấm Candida: Bimekizumab ức chế IL-17, làm tăng nguy cơ nhiễm trùng nấm Candida (oral, vulvovaginal). Theo dõi triệu chứng và điều trị nếu cần.",
                        "Vắc-xin sống: Tránh dùng vắc-xin sống trong khi điều trị và ít nhất 16 tuần sau khi ngừng bimekizumab.",
                        "Viêm ruột (IBD): Bimekizumab có thể làm trầm trọng hoặc gây viêm ruột mới (Crohn's disease, ulcerative colitis). Theo dõi triệu chứng (đau bụng, tiêu chảy, chảy máu trực tràng).",
                        "Phản ứng tại chỗ tiêm: Có thể xảy ra đau, đỏ, sưng, ngứa tại chỗ tiêm. Thường nhẹ và tự khỏi.",
                        "Phản ứng dị ứng: Hiếm nhưng có thể xảy ra phản ứng dị ứng nghiêm trọng. Ngừng điều trị nếu có phản ứng dị ứng.",
                        "Thận trọng ở bệnh nhân suy giảm miễn dịch, có tiền sử nhiễm trùng tái phát, hoặc có bệnh lý viêm ruột.",
                ],
                "pharmacokinetics": {
                        "half_life": "Khoảng 3-4 tuần (dài, cho phép dùng liều mỗi 4-8 tuần)",
                        "onset": "2-4 tuần (bắt đầu thấy cải thiện)",
                        "duration": "Dài do half-life dài, duy trì hiệu quả trong 4-8 tuần giữa các liều",
                        "protein_binding": "Không áp dụng (monoclonal antibody)",
                        "metabolism": "Chuyển hóa qua hệ thống proteolytic (giống các protein nội sinh), không qua CYP450. Chuyển hóa chủ yếu ở gan và các mô khác.",
                        "clearance": "Chủ yếu qua hệ thống proteolytic và thải trừ qua thận (dạng đã chuyển hóa). Không thải trừ qua thận dạng nguyên dạng như các thuốc phân tử nhỏ.",
                },
                "storage": "Bảo quản trong tủ lạnh ở 2-8°C, tránh đông lạnh. Bảo quản trong hộp gốc để tránh ánh sáng. Có thể bảo quản ở nhiệt độ phòng (≤25°C) tối đa 30 ngày, nhưng không được quay lại tủ lạnh sau khi đã lấy ra. Làm ấm đến nhiệt độ phòng trước khi tiêm.",
                "black_box_warnings": "Tăng nguy cơ nhiễm trùng nghiêm trọng. Bimekizumab ức chế miễn dịch, có thể tăng nguy cơ nhiễm trùng nghiêm trọng, bao gồm nhiễm trùng huyết, viêm phổi, và nhiễm trùng da. Không bắt đầu điều trị ở bệnh nhân có nhiễm trùng hoạt động nghiêm trọng. Nếu phát triển nhiễm trùng nghiêm trọng trong khi điều trị, tạm ngừng bimekizumab cho đến khi nhiễm trùng được kiểm soát.",
                "drug_interactions": {
                        "major": [
                                {
                                        "drug": "Vắc-xin sống (MMR, varicella, zoster, BCG, v.v.)",
                                        "mechanism": "Bimekizumab ức chế miễn dịch, có thể làm giảm hiệu quả vắc-xin sống và tăng nguy cơ nhiễm trùng từ vắc-xin sống.",
                                        "effect": "Giảm hiệu quả vắc-xin, tăng nguy cơ nhiễm trùng từ vắc-xin sống",
                                        "management": "Tránh dùng vắc-xin sống trong khi điều trị và ít nhất 16 tuần sau khi ngừng bimekizumab. Có thể tiêm vắc-xin bất hoạt (inactivated vaccines) nhưng hiệu quả có thể giảm."
                                },
                        ],
                        "moderate": [
                                {
                                        "drug": "Thuốc ức chế miễn dịch khác (cyclosporine, methotrexate, azathioprine, v.v.)",
                                        "mechanism": "Có thể tăng nguy cơ nhiễm trùng do ức chế miễn dịch cộng hưởng.",
                                        "effect": "Tăng nguy cơ nhiễm trùng nghiêm trọng",
                                        "management": "Thận trọng khi dùng đồng thời. Theo dõi chặt chẽ dấu hiệu nhiễm trùng. Có thể dùng methotrexate đồng thời nhưng cần theo dõi chặt chẽ."
                                },
                        ],
                        "minor": [],
                },
                "contraindications_detail": {
                        "tuyệt_đối": [
                                "Dị ứng bimekizumab hoặc bất kỳ thành phần nào",
                                "Nhiễm trùng hoạt động nghiêm trọng (viêm phổi, nhiễm trùng huyết, v.v.)",
                        ],
                        "tương_đối": [
                                "Nhiễm trùng mạn tính hoặc tái phát",
                                "Suy giảm miễn dịch",
                                "Bệnh lý viêm ruột (Crohn's disease, ulcerative colitis) - có thể làm trầm trọng",
                                "Tiền sử ung thư (dữ liệu hạn chế)",
                        ],
                },
                "pregnancy_lactation": {
                        "fda_category": "Không phân loại",
                        "pregnancy_details": "Chưa có dữ liệu đầy đủ về việc sử dụng bimekizumab trong thai kỳ. Bimekizumab là IgG1, có thể qua nhau thai trong 3 tháng cuối thai kỳ. Dữ liệu từ các nghiên cứu trên động vật không cho thấy tác hại rõ ràng, nhưng dữ liệu trên người còn hạn chế. Cân nhắc lợi ích/nguy cơ. Nếu có thai trong khi điều trị, cần thông báo ngay cho bác sĩ.",
                        "lactation": {
                                "safety": "Chưa biết",
                                "details": "Chưa biết bimekizumab có bài tiết vào sữa mẹ hay không. Bimekizumab là IgG1, có thể bài tiết vào sữa mẹ với lượng nhỏ. Tuy nhiên, do phân tử lớn, khả năng hấp thu qua đường tiêu hóa của trẻ sơ sinh là thấp.",
                                "recommendation": "Thận trọng khi cho con bú. Cân nhắc lợi ích/nguy cơ. Nếu cần điều trị, có thể tiếp tục cho con bú nhưng theo dõi trẻ sơ sinh chặt chẽ.",
                        },
                },
                "hepatic_adjustment": {
                        "mild": "Không cần chỉnh liều",
                        "moderate": "Không cần chỉnh liều (monoclonal antibody, không chuyển hóa qua CYP450)",
                        "severe": "Không cần chỉnh liều, nhưng thận trọng ở bệnh nhân suy gan nặng (dữ liệu hạn chế)",
                        "notes": "Bimekizumab là monoclonal antibody, chuyển hóa qua hệ thống proteolytic, không qua CYP450. Không cần điều chỉnh liều theo chức năng gan. Tuy nhiên, ở bệnh nhân suy gan nặng, có thể ảnh hưởng đến chuyển hóa protein nói chung.",
                },
                "overdose_management": {
                        "symptoms": [
                                "Tăng nguy cơ nhiễm trùng",
                                "Phản ứng tại chỗ tiêm (nếu tiêm quá nhiều)",
                                "Phản ứng dị ứng (nếu quá mẫn)",
                        ],
                        "antidote": "Không có antidote đặc hiệu",
                        "treatment": [
                                "Điều trị hỗ trợ",
                                "Theo dõi dấu hiệu sinh tồn",
                                "Theo dõi dấu hiệu nhiễm trùng chặt chẽ",
                                "Điều trị nhiễm trùng nếu phát triển",
                                "Xử trí phản ứng dị ứng nếu có",
                        ],
                        "monitoring": "Theo dõi dấu hiệu sinh tồn, dấu hiệu nhiễm trùng, phản ứng dị ứng. Do half-life dài (3-4 tuần), cần theo dõi kéo dài.",
                },
                "reversal_agents": {
                        "available": False,
                        "agents": [],
                },
                "administration_instructions": {
                        "subcutaneous": {
                                "injection_sites": "Vùng đùi, bụng, hoặc cánh trước cánh tay. Tránh vùng da bị tổn thương, sẹo, hoặc vảy nến.",
                                "preparation": "Làm ấm đến nhiệt độ phòng (15-30 phút) trước khi tiêm. Không làm nóng bằng lò vi sóng hoặc nước nóng. Không lắc.",
                                "technique": "Tiêm dưới da (90 độ góc). Mỗi liều 320mg được tiêm thành 2 lần, mỗi lần 160mg ở 2 vị trí khác nhau.",
                                "timing": "Liều nạp: Tuần 0, 4, 8, 12, 16. Liều duy trì: Mỗi 4 tuần (bắt đầu từ tuần 20). Có thể giảm xuống mỗi 8 tuần ở một số bệnh nhân sau khi đạt đáp ứng.",
                        },
                },
                "references": {
                        "primary_sources": [
                                "FDA Drug Label - Bimekizumab (Bimzelx)",
                                "FDA Approval Date: October 15, 2023",
                                "FDA-approved use: To treat moderate to severe plaque psoriasis in adults who are candidates for systemic therapy or phototherapy",
                        ],
                        "last_updated": "2026-01-15",
                        "evidence_level": "A - FDA-approved 2023",
                },
                "risk_flags": {
                        "high_alert": False,
                        "narrow_therapeutic_index": False,
                        "bleeding_risk": False,
                        "organ_toxicity": [
                                "Hepatotoxicity (hiếm, tăng men gan)",
                        ],
                        "qt_prolongation": False,
                        "hepatotoxicity": True,
                        "nephrotoxicity": False,
                        "requires_monitoring": [
                                "Clinical response",
                                "Adverse effects",
                                "Infections (serious infections, candidiasis)",
                                "Liver function (if symptoms)",
                                "CBC (neutrophil count)",
                                "Injection site reactions",
                        ],
                },
                "guideline_tags": [
                        "FDA Drug Information - Bimekizumab (Bimzelx)",
                        "Plaque Psoriasis",
                        "Psoriatic Arthritis",
                        "Monoclonal Antibody - IL-17 Inhibitor",
                ],
                "last_updated": "2026-01-15",
        },
    "Rezzayo": {
                "group": "FDA Approved 2023",
                "vietnamese_name": "Rezafungin, Rezzayo",
                "administration": [
                        "IV",
                ],
                "indications": [
                        "Điều trị candidemia (nhiễm nấm Candida trong máu)",
                        "Điều trị nhiễm nấm Candida xâm lấn (invasive candidiasis)",
                        "Điều trị nhiễm nấm Candida xâm lấn ở bệnh nhân suy giảm miễn dịch",
                ],
                "contraindications": [
                        "Dị ứng rezafungin hoặc bất kỳ thành phần nào",
                        "Dị ứng với các echinocandin khác (caspofungin, micafungin, anidulafungin)",
                ],
                "dosage": {
                        "adult_standard": "400mg IV x 1 lần/ngày (liều nạp), sau đó 200mg IV x 1 lần/ngày (liều duy trì)",
                        "adult_loading": "400mg IV x 1 lần (liều đầu tiên)",
                        "adult_maintenance": "200mg IV x 1 lần/ngày (bắt đầu từ ngày thứ 2)",
                        "adult_duration": "Điều trị tối thiểu 14 ngày sau khi cấy máu âm tính và triệu chứng lâm sàng cải thiện",
                        "notes": "Truyền IV trong 60 phút. Không cần điều chỉnh liều theo chức năng thận hoặc gan. FDA phê duyệt 2023.",
                },
                "renal_adjustment": {
                        "normal": "Không cần chỉnh liều",
                        "30_60": "Không cần chỉnh liều",
                        "under_30": "Không cần chỉnh liều (echinocandin, không thải qua thận)",
                        "hemodialysis": "Không cần chỉnh liều, không bị loại bỏ đáng kể qua lọc máu",
                },
                "side_effects": [
                        "Phản ứng truyền (infusion reactions) - sốt, ớn lạnh, đỏ bừng, hạ huyết áp (thường gặp)",
                        "Tăng men gan (ALT, AST) - thường gặp",
                        "Giảm kali máu (hypokalemia) - thường gặp",
                        "Buồn nôn, nôn - thường gặp",
                        "Tiêu chảy - thường gặp",
                        "Nhức đầu - thường gặp",
                        "Phát ban - hiếm",
                        "Giảm bạch cầu trung tính (neutropenia) - hiếm",
                        "Phản ứng dị ứng (phản vệ) - hiếm nhưng có thể xảy ra",
                ],
                "interactions": [
                        "Ít tương tác thuốc: Rezafungin không ức chế hoặc cảm ứng CYP450, nên ít tương tác với các thuốc chuyển hóa qua CYP450",
                        "Cyclosporine: Có thể tăng nhẹ nồng độ cyclosporine, theo dõi nồng độ",
                        "Tacrolimus: Có thể tăng nhẹ nồng độ tacrolimus, theo dõi nồng độ",
                        "Warfarin: Không có tương tác đáng kể",
                ],
                "pregnancy": "C",
                "mechanism_of_action": "Rezafungin là echinocandin (lipopeptide) kháng nấm, ức chế enzyme β-(1,3)-D-glucan synthase của nấm Candida. Enzyme này tổng hợp β-(1,3)-D-glucan - thành phần quan trọng của thành tế bào nấm. Ức chế tổng hợp β-(1,3)-D-glucan → thành tế bào nấm yếu, không ổn định, rò rỉ → chết tế bào nấm. Phổ kháng nấm: Hiệu quả với Candida (bao gồm cả C. auris kháng azole), Aspergillus (fungistatic). Đặc điểm quan trọng: Rezafungin có thời gian bán thải dài hơn các echinocandin khác (caspofungin, micafungin, anidulafungin), cho phép dùng liều hàng ngày đơn giản. Không ức chế hoặc cảm ứng CYP450, nên ít tương tác thuốc hơn các azole. FDA phê duyệt 2023 để điều trị candidemia và nhiễm nấm Candida xâm lấn.",
                "monitoring": [
                        "Theo dõi đáp ứng điều trị (cấy máu, triệu chứng lâm sàng)",
                        "Theo dõi phản ứng truyền (infusion reactions) - sốt, ớn lạnh, đỏ bừng, hạ huyết áp trong và sau khi truyền",
                        "Chức năng gan (ALT, AST) - trước và trong điều trị",
                        "Điện giải (kali) - theo dõi kali máu",
                        "Công thức máu (CBC) - theo dõi bạch cầu trung tính",
                        "Dấu hiệu nhiễm trùng (sốt, WBC, CRP)",
                        "Cấy máu và cấy từ vị trí nhiễm trùng để đánh giá đáp ứng",
                ],
                "precautions": [
                        "Phản ứng truyền: Có thể xảy ra phản ứng truyền (infusion reactions) - sốt, ớn lạnh, đỏ bừng, hạ huyết áp trong và sau khi truyền. Thường nhẹ và tự khỏi, nhưng cần theo dõi. Nếu phản ứng nghiêm trọng, có thể giảm tốc độ truyền hoặc tạm ngừng.",
                        "Truyền IV trong 60 phút. Không truyền nhanh hơn để tránh phản ứng truyền.",
                        "Không cần điều chỉnh liều theo chức năng thận hoặc gan (echinocandin, không chuyển hóa qua CYP450, không thải qua thận).",
                        "Theo dõi chức năng gan (tăng men gan có thể xảy ra, thường nhẹ và tự khỏi).",
                        "Theo dõi kali máu (có thể gây hạ kali máu).",
                        "Ít tương tác thuốc: Rezafungin không ức chế hoặc cảm ứng CYP450, nên ít tương tác với các thuốc chuyển hóa qua CYP450. Tuy nhiên, vẫn cần theo dõi khi dùng với cyclosporine hoặc tacrolimus.",
                        "Điều trị tối thiểu 14 ngày sau khi cấy máu âm tính và triệu chứng lâm sàng cải thiện.",
                        "Thận trọng ở bệnh nhân suy gan nặng (dữ liệu hạn chế, nhưng không cần điều chỉnh liều).",
                ],
                "pharmacokinetics": {
                        "half_life": "Khoảng 130-150 giờ (rất dài, dài hơn các echinocandin khác như caspofungin ~10-15 giờ, micafungin ~14-17 giờ, anidulafungin ~40-50 giờ)",
                        "onset": "Tác dụng kháng nấm bắt đầu trong 24-48 giờ",
                        "duration": "Dài do half-life rất dài, duy trì nồng độ hiệu quả trong nhiều ngày",
                        "protein_binding": ">98% (gắn kết cao với protein huyết tương, chủ yếu albumin)",
                        "metabolism": "Chuyển hóa chậm qua peptide hydrolysis và glutathione conjugation, không qua CYP450",
                        "clearance": "Chủ yếu qua gan (chuyển hóa), một phần nhỏ qua thận (dạng đã chuyển hóa). Không thải trừ qua thận dạng nguyên dạng. Thời gian bán thải rất dài do gắn kết cao với protein và chuyển hóa chậm.",
                },
                "storage": "Bảo quản trong tủ lạnh ở 2-8°C, tránh đông lạnh. Bảo quản trong hộp gốc để tránh ánh sáng. Dung dịch đã pha: ổn định ở nhiệt độ phòng (20-25°C) trong 24 giờ, hoặc trong tủ lạnh (2-8°C) trong 7 ngày. Không đông lạnh dung dịch đã pha.",
                "black_box_warnings": "Không có cảnh báo hộp đen đặc biệt. Tuy nhiên, cần thận trọng với phản ứng truyền (infusion reactions) và phản ứng dị ứng (phản vệ).",
                "drug_interactions": {
                        "major": [],
                        "moderate": [
                                {
                                        "drug": "Cyclosporine, Tacrolimus",
                                        "mechanism": "Rezafungin có thể tăng nhẹ nồng độ cyclosporine và tacrolimus, mặc dù cơ chế chưa rõ ràng (không qua CYP450).",
                                        "effect": "Tăng nhẹ nồng độ cyclosporine/tacrolimus, có thể tăng độc tính",
                                        "management": "Theo dõi nồng độ cyclosporine/tacrolimus khi bắt đầu rezafungin. Điều chỉnh liều nếu cần."
                                },
                        ],
                        "minor": [],
                },
                "contraindications_detail": {
                        "tuyệt_đối": [
                                "Dị ứng rezafungin hoặc bất kỳ thành phần nào",
                                "Dị ứng với các echinocandin khác (caspofungin, micafungin, anidulafungin) - có thể có phản ứng chéo",
                        ],
                        "tương_đối": [
                                "Suy gan nặng (dữ liệu hạn chế, nhưng không cần điều chỉnh liều)",
                                "Phản ứng truyền nghiêm trọng với echinocandin trước đó",
                        ],
                },
                "pregnancy_lactation": {
                        "fda_category": "C",
                        "pregnancy_details": "Chưa có dữ liệu đầy đủ về việc sử dụng rezafungin trong thai kỳ. Dữ liệu từ các nghiên cứu trên động vật không cho thấy tác hại rõ ràng, nhưng dữ liệu trên người còn hạn chế. Cân nhắc lợi ích/nguy cơ. Nếu có thai trong khi điều trị, cần thông báo ngay cho bác sĩ.",
                        "lactation": {
                                "safety": "Chưa biết",
                                "details": "Chưa biết rezafungin có bài tiết vào sữa mẹ hay không. Rezafungin là peptide, có thể bài tiết vào sữa mẹ với lượng nhỏ. Tuy nhiên, do phân tử lớn, khả năng hấp thu qua đường tiêu hóa của trẻ sơ sinh là thấp.",
                                "recommendation": "Thận trọng khi cho con bú. Cân nhắc lợi ích/nguy cơ. Nếu cần điều trị, có thể tiếp tục cho con bú nhưng theo dõi trẻ sơ sinh chặt chẽ.",
                        },
                },
                "hepatic_adjustment": {
                        "mild": "Không cần chỉnh liều",
                        "moderate": "Không cần chỉnh liều (dữ liệu hạn chế)",
                        "severe": "Không cần chỉnh liều, nhưng thận trọng (dữ liệu hạn chế)",
                        "notes": "Rezafungin chuyển hóa chủ yếu qua gan, nhưng không qua CYP450. Không cần điều chỉnh liều theo chức năng gan. Tuy nhiên, ở bệnh nhân suy gan nặng, có thể ảnh hưởng đến chuyển hóa protein nói chung. Dữ liệu hạn chế ở bệnh nhân suy gan nặng.",
                },
                "overdose_management": {
                        "symptoms": [
                                "Phản ứng truyền nghiêm trọng (sốt, ớn lạnh, đỏ bừng, hạ huyết áp)",
                                "Tăng men gan",
                                "Hạ kali máu",
                                "Phản ứng dị ứng (phản vệ)",
                        ],
                        "antidote": "Không có antidote đặc hiệu",
                        "treatment": [
                                "Ngừng truyền ngay lập tức",
                                "Điều trị hỗ trợ",
                                "Theo dõi dấu hiệu sinh tồn",
                                "Xử trí phản ứng dị ứng nếu có (epinephrine, antihistamine, corticosteroid)",
                                "Điều chỉnh điện giải (kali) nếu cần",
                                "Theo dõi chức năng gan",
                        ],
                        "monitoring": "Theo dõi dấu hiệu sinh tồn, phản ứng dị ứng, chức năng gan, điện giải. Do half-life rất dài (130-150 giờ), cần theo dõi kéo dài.",
                },
                "reversal_agents": {
                        "available": False,
                        "agents": [],
                },
                "administration_instructions": {
                        "intravenous": {
                                "preparation": "Pha trong NS hoặc D5W. Pha 400mg trong 250ml (liều nạp) hoặc 200mg trong 250ml (liều duy trì).",
                                "infusion_rate": "Truyền IV trong 60 phút. Không truyền nhanh hơn để tránh phản ứng truyền.",
                                "compatibility": "Không trộn với các thuốc khác. Truyền riêng biệt.",
                                "timing": "Liều nạp: 400mg IV x 1 lần (ngày đầu tiên). Liều duy trì: 200mg IV x 1 lần/ngày (bắt đầu từ ngày thứ 2). Điều trị tối thiểu 14 ngày sau khi cấy máu âm tính và triệu chứng lâm sàng cải thiện.",
                        },
                },
                "references": {
                        "primary_sources": [
                                "FDA Drug Label - Rezafungin (Rezzayo)",
                                "FDA Approval Date: March 22, 2023",
                                "FDA-approved use: To treat candidemia and invasive candidiasis",
                        ],
                        "last_updated": "2026-01-15",
                        "evidence_level": "A - FDA-approved 2023",
                },
                "risk_flags": {
                        "high_alert": False,
                        "narrow_therapeutic_index": False,
                        "bleeding_risk": False,
                        "organ_toxicity": [
                                "Hepatotoxicity (tăng men gan, thường nhẹ)",
                        ],
                        "qt_prolongation": False,
                        "hepatotoxicity": True,
                        "nephrotoxicity": False,
                        "requires_monitoring": [
                                "Clinical response",
                                "Adverse effects",
                                "Infusion reactions",
                                "Liver function",
                                "Electrolytes (potassium)",
                                "CBC (neutrophil count)",
                        ],
                },
                "guideline_tags": [
                        "FDA Drug Information - Rezafungin (Rezzayo)",
                        "Candidemia",
                        "Invasive Candidiasis",
                        "Echinocandin Antifungal",
                ],
                "last_updated": "2026-01-15",
        },
}

__all__ = ['AZOLES_DRUGS']
