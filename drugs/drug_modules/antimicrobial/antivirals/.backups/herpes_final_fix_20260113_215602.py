"""
Herpes Antivirals
Acyclovir and Valacyclovir for HSV and VZV infections
"""

HERPES_ANTIVIRALS = {
    "Acyclovir": {
        "group": "Infectious Disease - Antiviral",
        "vietnamese_name": "Acyclovir, Zovirax",
        "administration": ["PO", "IV", "Topical"],
        "indications": [
            "Herpes simplex (HSV)",
            "Herpes zoster (shingles)",
            "Viêm não do HSV",
            "Nhiễm HSV ở người suy giảm miễn dịch"
        ],
        "contraindications": [
            "Dị ứng",
            "Suy thận nặng (IV)"
        ],
        "dosage": {
            "adult_herpes_simplex": "200mg x 5 lần/ngày x 7-10 ngày",
            "adult_shingles": "800mg x 5 lần/ngày x 7-10 ngày",
            "adult_iv": "5-10mg/kg IV mỗi 8 giờ",
            "adult_encephalitis": "10mg/kg IV mỗi 8 giờ x 14-21 ngày",
            "notes": "Uống nhiều nước. Truyền IV chậm (1 giờ) để tránh độc thận"
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "Giảm liều 50%",
            "under_30": "Giảm liều 75%"
        },
        "side_effects": [
            "Buồn nôn",
            "Đau đầu",
            "Độc thận (IV, liều cao)",
            "Rối loạn thần kinh (IV)",
            "Viêm tĩnh mạch (IV)",
            "Ban da"
        ],
        "interactions": [
            "Probenecid: tăng nồng độ acyclovir",
            "Nephrotoxic drugs: tăng nguy cơ độc thận"
        ],
        "pregnancy": "B",
        "mechanism_of_action": "Acyclovir là một nucleotide analog của guanosine. Sau khi vào tế bào nhiễm virus, acyclovir được phosphoryl hóa bởi virus thymidine kinase (TK) thành acyclovir monophosphate, sau đó được phosphoryl hóa tiếp bởi enzyme tế bào thành acyclovir triphosphate (ACV-TP). ACV-TP ức chế cạnh tranh DNA polymerase của virus, gây chấm dứt chuỗi DNA và ngăn chặn sự nhân lên của virus. Chọn lọc cao với virus (chỉ được phosphoryl hóa bởi virus TK, không phải tế bào người), nên ít độc với tế bào người",
        "monitoring": [
            "Creatinine, BUN khi dùng IV (đặc biệt liều cao, kéo dài)",
            "Chức năng thận trước và trong khi dùng IV",
            "Dấu hiệu độc thận: tăng creatinine, giảm lượng nước tiểu, phù",
            "Dấu hiệu rối loạn thần kinh: lú lẫn, co giật, ảo giác (IV, hiếm)",
            "Dấu hiệu viêm tĩnh mạch tại chỗ tiêm (IV)",
            "Đáp ứng điều trị và triệu chứng lâm sàng"
        ],
        "precautions": [
            "PHẢI truyền IV chậm (trong 1 giờ) để tránh độc thận",
            "Duy trì đủ dịch trong khi dùng IV (tối thiểu 1-2L/ngày)",
            "Điều chỉnh liều theo chức năng thận (giảm liều khi CrCl <50)",
            "Theo dõi sát creatinine khi dùng IV, đặc biệt liều cao (10mg/kg)",
            "Tránh dùng cùng các thuốc độc thận khác nếu có thể",
            "Uống nhiều nước khi dùng PO để giảm nguy cơ kết tinh ở thận",
            "Dùng đúng liều và đủ thời gian (7-21 ngày tùy chỉ định)",
            "Thận trọng ở bệnh nhân suy thận, cao tuổi (tăng nguy cơ độc thận)"
        ],
        "pharmacokinetics": {
            "half_life": "2.5-3.3 giờ (PO), 2.5 giờ (IV)",
            "onset": "Nhanh sau khi vào tế bào",
            "duration": "Ngắn (cần dùng nhiều lần/ngày)",
            "protein_binding": "9-33%",
            "clearance": "Thận (chủ yếu qua lọc cầu thận và bài tiết ống thận), không chuyển hóa đáng kể"
        },
        "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm. Dung dịch IV: bảo quản ở 2-8°C, pha xong dùng trong 24 giờ",
        "black_box_warnings": None,
        "drug_interactions": {
            "major": [
                {
                    "drug": "Probenecid",
                    "mechanism": "Probenecid ức chế bài tiết ống thận của acyclovir, làm giảm thải trừ và tăng nồng độ acyclovir trong máu.",
                    "effect": "Tăng nồng độ acyclovir, tăng thời gian bán thải, tăng nguy cơ độc tính (độc thận, rối loạn thần kinh)",
                    "management": "Giảm liều acyclovir 25-50% khi dùng với probenecid. Theo dõi chức năng thận và dấu hiệu độc tính chặt chẽ."
                },
                {
                    "drug": "Thuốc độc thận (Aminoglycosides, Vancomycin, Amphotericin B, Cisplatin)",
                    "mechanism": "Cả hai đều có độc tính thận, tác dụng cộng dồn làm tăng nguy cơ suy thận cấp.",
                    "effect": "Tăng nguy cơ suy thận cấp, độc thận nghiêm trọng, tăng creatinine",
                    "management": "TRÁNH DÙNG đồng thời nếu có thể. Nếu bắt buộc, theo dõi creatinine, BUN, lượng nước tiểu chặt chẽ. Duy trì đủ dịch. Có thể cần giảm liều cả hai thuốc."
                }
            ],
            "moderate": [
                {
                    "drug": "Cimetidine",
                    "mechanism": "Cimetidine có thể ức chế bài tiết ống thận của acyclovir (nhẹ).",
                    "effect": "Tăng nhẹ nồng độ acyclovir",
                    "management": "Theo dõi chức năng thận. Không cần điều chỉnh liều thường quy."
                },
                {
                    "drug": "Zidovudine (AZT)",
                    "mechanism": "Cả hai đều có thể gây độc thận và giảm bạch cầu, tác dụng cộng dồn.",
                    "effect": "Tăng nguy cơ độc thận, giảm bạch cầu",
                    "management": "Theo dõi chức năng thận và công thức máu. Thận trọng khi dùng đồng thời."
                }
            ],
            "minor": [
                {
                    "drug": "Mycophenolate",
                    "mechanism": "Cả hai đều có thể gây độc thận, tác dụng cộng dồn nhẹ.",
                    "effect": "Tăng nguy cơ độc thận (nhẹ)",
                    "management": "Theo dõi chức năng thận. Không cần điều chỉnh liều thường quy."
                }
            ]
        },
        "contraindications": {
            "tuyệt_đối": [
                "Dị ứng acyclovir hoặc valacyclovir",
                "Suy thận nặng (CrCl <10 ml/min) khi dùng IV - chống chỉ định tuyệt đối với IV",
                "Rối loạn thần kinh nặng không kiểm soát (khi dùng IV)"
            ],
            "tương_đối": [
                "Suy thận nhẹ đến trung bình (CrCl 10-50) - giảm liều đáng kể, theo dõi chặt chẽ",
                "Suy thận nặng (CrCl <10) khi dùng PO - giảm liều 75%, theo dõi chặt chẽ",
                "Mất nước - tăng nguy cơ độc thận, cần bù dịch đầy đủ",
                "Dùng với thuốc độc thận - tăng nguy cơ suy thận cấp",
                "Người cao tuổi - tăng nguy cơ độc thận, có thể cần giảm liều",
                "Bệnh thần kinh - tăng nguy cơ rối loạn thần kinh khi dùng IV"
            ]
        },
        "pregnancy_lactation": {
            "fda_category": "B",
            "pregnancy_details": "Acyclovir là thuốc phân loại B. Các nghiên cứu trên động vật không cho thấy nguy cơ dị tật bẩm sinh, nhưng không có nghiên cứu đầy đủ trên phụ nữ có thai. Acyclovir được sử dụng rộng rãi trong thai kỳ để điều trị nhiễm HSV và có vẻ an toàn. Nhiễm HSV có thể gây nguy hiểm cho thai nhi (nhiễm HSV ở trẻ sơ sinh, viêm não). Acyclovir có thể được dùng khi lợi ích vượt quá nguy cơ. Dạng uống được ưu tiên hơn dạng IV để giảm nguy cơ độc tính. Tránh dùng liều cao IV trong thai kỳ nếu có thể.",
            "lactation": {
                "safety": "Compatible",
                "details": "Acyclovir bài tiết vào sữa mẹ ở nồng độ thấp (tương đương nồng độ trong máu mẹ). Nồng độ trong sữa mẹ thấp và không có báo cáo về tác dụng phụ đáng kể ở trẻ bú mẹ. Hấp thu qua đường tiêu hóa của trẻ sơ sinh thấp.",
                "recommendation": "Có thể dùng khi cho con bú. Dạng uống được ưu tiên. Dùng liều thấp nhất hiệu quả. Theo dõi trẻ sơ sinh nếu dùng liều cao hoặc kéo dài."
            }
        },
        "hepatic_adjustment": {
            "mild": "Không cần điều chỉnh liều. Acyclovir không chuyển hóa qua gan, thải trừ chủ yếu qua thận.",
            "moderate": "Không cần điều chỉnh liều.",
            "severe": "Không cần điều chỉnh liều. Acyclovir không chuyển hóa qua gan.",
            "notes": "Acyclovir không chuyển hóa qua gan, thải trừ chủ yếu qua thận (lọc cầu thận và bài tiết ống thận). Không cần điều chỉnh liều ở bệnh nhân suy gan. Tuy nhiên, suy gan có thể kèm theo suy thận, nên cần điều chỉnh liều theo chức năng thận."
        },
        "overdose_management": {
            "symptoms": [
                "Triệu chứng độc thận: Tăng creatinine, BUN, giảm lượng nước tiểu, phù, suy thận cấp",
                "Triệu chứng thần kinh: Lú lẫn, co giật, ảo giác, rối loạn ý thức, hôn mê (với IV liều cao)",
                "Triệu chứng tiêu hóa: Buồn nôn, nôn, đau bụng",
                "Triệu chứng tại chỗ: Viêm tĩnh mạch, đau tại chỗ tiêm (IV)",
                "Triệu chứng nghiêm trọng: Suy thận cấp, rối loạn thần kinh nặng, hôn mê"
            ],
            "antidote": "Không có antidote đặc hiệu. Điều trị hỗ trợ và điều trị triệu chứng.",
            "treatment": [
                "Ngừng ngay acyclovir",
                "Bù dịch đầy đủ: Truyền dịch để tăng thải trừ qua thận và giảm nguy cơ kết tinh ở thận",
                "Theo dõi chức năng thận: Creatinine, BUN, lượng nước tiểu",
                "Điều trị suy thận cấp nếu có:",
                "  - Bù dịch đầy đủ",
                "  - Điều chỉnh điện giải",
                "  - Lọc máu nếu cần (hemodialysis có thể loại bỏ acyclovir)",
                "Điều trị rối loạn thần kinh nếu có:",
                "  - Hỗ trợ hô hấp nếu cần",
                "  - Điều trị co giật: Benzodiazepine",
                "  - Theo dõi thần kinh chặt chẽ",
                "Điều trị viêm tĩnh mạch: Chườm ấm, thay đổi vị trí tiêm",
                "Theo dõi dấu hiệu sinh tồn: Huyết áp, nhịp tim, nhịp thở, SpO2",
                "Lọc máu: Hemodialysis có thể loại bỏ acyclovir nếu suy thận nặng"
            ],
            "monitoring": "Theo dõi chức năng thận (creatinine, BUN, lượng nước tiểu), dấu hiệu thần kinh, dấu hiệu sinh tồn trong ít nhất 24-48 giờ. Theo dõi lâu hơn nếu có suy thận cấp hoặc rối loạn thần kinh."
        },
        "reversal_agents": None,
        "administration_instructions": {
            "oral": {
                "with_food": "Có thể uống với hoặc không thức ăn. Uống với nước đầy đủ (ít nhất 1-2 ly nước) để giảm nguy cơ kết tinh ở thận.",
                "timing": "Uống 3-5 lần/ngày tùy chỉ định (herpes simplex: 5 lần/ngày, shingles: 5 lần/ngày). Cách đều trong ngày. Có thể uống với hoặc sau bữa ăn để giảm buồn nôn."
            },
            "iv": {
                "reconstitution": "Pha với NS hoặc D5W. Nồng độ pha: 7mg/ml (tối đa). Pha 500mg trong 100ml dịch = 5mg/ml. Pha 1g trong 250ml dịch = 4mg/ml. Pha 10mg/kg trong 100ml dịch cho liều tiêu chuẩn.",
                "infusion_rate": "TRUYỀN CHẬM trong 1 giờ (ít nhất 1 giờ). KHÔNG được truyền nhanh - sẽ tăng nguy cơ độc thận. Tốc độ: 100ml/giờ = ~1.7ml/phút. Ví dụ: 500mg/100ml = 100ml/giờ. 1g/250ml = 250ml/giờ (4.2ml/phút).",
                "compatibility": ["NS (0.9% NaCl)", "D5W (5% Dextrose)", "Ringer's Lactate"],
                "incompatibility": ["Không trộn với các thuốc khác trong cùng một ống truyền. Kiểm tra tương thích trước khi pha. Tránh pha với thuốc có tính kiềm hoặc độc thận."],
                "notes": "QUAN TRỌNG: 1) Truyền CHẬM trong 1 giờ, 2) Duy trì đủ dịch (tối thiểu 1-2L/ngày), 3) Theo dõi creatinine, BUN, 4) Điều chỉnh liều theo CrCl. Nếu truyền nhanh → tăng nguy cơ độc thận. Liều: 5-10mg/kg mỗi 8 giờ."
            },
            "topical": {
                "application": "Rửa sạch và lau khô vùng da bị tổn thương. Bôi một lớp mỏng lên vùng tổn thương 5-6 lần/ngày trong 7-10 ngày. Dùng găng tay hoặc dụng cụ khi bôi để tránh lây lan virus. Rửa tay sau khi bôi."
            }
        },
        "references": {
            "primary_sources": [
                "FDA Drug Label - Acyclovir (Zovirax)",
                "UpToDate - Acyclovir: Drug Information",
                "Medscape - Acyclovir Drug Reference",
                "Goodman & Gilman's The Pharmacological Basis of Therapeutics (14th ed)",
                "Lexicomp Online - Acyclovir Monograph",
                "Micromedex - Acyclovir Drug Information",
                "IDSA Guidelines - Herpes Simplex Virus Infections"
            ],
            "last_updated": "2024-12-19",
            "evidence_level": "A - Dựa trên FDA drug labels, IDSA guidelines, và dữ liệu lâm sàng từ nhiều nguồn"
        },
        "risk_flags": {
            "high_alert": False,
            "narrow_therapeutic_index": False,
            "icu_critical_care_only": False,
            "bleeding_risk": None,
            "organ_toxicity": {"renal": "Nephrotoxicity (IV, especially with high doses - dose-dependent, may be irreversible)", "neurological": "Neurotoxicity (IV, rare - confusion, seizures, hallucinations)", "dermatologic": "Phlebitis (IV administration)"},
            "qt_prolongation": False,
            "hepatotoxicity": False,
            "nephrotoxicity": True,
            "requires_monitoring": ["Renal function (creatinine, BUN, CrCl - dose adjustment required, especially IV)", "Neurological status (confusion, seizures, hallucinations - IV, rare)", "Fluid balance (maintain adequate hydration - critical for IV)", "Infusion rate (must infuse slowly over 1 hour - critical)", "Phlebitis signs (IV administration)"],
            "look_alike_sound_alike": ["Acyclovir", "Valacyclovir"]
        },
        "guideline_tags": [
            "IDSA Guidelines - Herpes Simplex Virus Infections",
            "IDSA Guidelines - Varicella-Zoster Virus Infections",
            "FDA Drug Safety Communication - Acyclovir and Renal Toxicity",
            "UpToDate - Acyclovir Drug Information",
            "WHO Essential Medicines List"
        ],
        "last_updated": "2025-02-18"
    },

    "Valacyclovir": {
        "group": "Infectious Disease - Antiviral",
        "vietnamese_name": "Valacyclovir, Valtrex",
        "administration": ["PO"],
        "indications": [
            "Herpes simplex (HSV)",
            "Herpes zoster (shingles)",
            "Phòng ngừa tái phát HSV",
            "Phòng ngừa CMV sau ghép tạng"
        ],
        "contraindications": [
            "Dị ứng",
            "Suy thận nặng"
        ],
        "dosage": {
            "adult_herpes_simplex": "500mg x 2 lần/ngày x 7-10 ngày",
            "adult_shingles": "1g x 3 lần/ngày x 7 ngày",
            "adult_prophylaxis": "500mg-1g x 1 lần/ngày",
            "adult_max": "3g/ngày",
            "notes": "Prodrug của acyclovir, hấp thu tốt hơn, uống ít lần hơn"
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "Giảm liều 50%",
            "under_30": "Giảm liều 75%"
        },
        "side_effects": [
            "Buồn nôn",
            "Đau đầu",
            "Độc thận (liều cao)",
            "Ít tác dụng phụ hơn acyclovir"
        ],
        "interactions": [
            "Probenecid: tăng nồng độ",
            "Cimetidine: tăng nồng độ"
        ],
        "pregnancy": "B",
        "mechanism_of_action": "Valacyclovir là prodrug của acyclovir, được chuyển hóa nhanh trong gan và ruột thành acyclovir bởi enzyme valacyclovir hydrolase. Sau khi chuyển thành acyclovir, cơ chế tác dụng giống acyclovir: được phosphoryl hóa bởi virus thymidine kinase thành acyclovir triphosphate, ức chế DNA polymerase của virus. Ưu điểm: hấp thu tốt hơn acyclovir (sinh khả dụng 54% vs 10-20%), nồng độ acyclovir trong máu cao hơn 3-5 lần, nên có thể dùng ít lần hơn (2-3 lần/ngày thay vì 5 lần/ngày)",
        "monitoring": [
            "Creatinine, BUN khi dùng liều cao hoặc kéo dài",
            "Chức năng thận (điều chỉnh liều khi suy thận)",
            "Dấu hiệu độc thận: tăng creatinine, giảm lượng nước tiểu",
            "Đáp ứng điều trị và triệu chứng lâm sàng"
        ],
        "precautions": [
            "Điều chỉnh liều theo chức năng thận (giảm liều khi CrCl <50)",
            "Uống nhiều nước để giảm nguy cơ kết tinh ở thận",
            "Thận trọng ở bệnh nhân suy thận, cao tuổi",
            "Dùng đúng liều và đủ thời gian",
            "Ưu điểm: dùng ít lần hơn acyclovir (2-3 lần/ngày), compliance tốt hơn"
        ],
        "pharmacokinetics": {
            "half_life": "2.5-3.3 giờ (sau chuyển thành acyclovir)",
            "onset": "Nhanh sau khi chuyển thành acyclovir",
            "duration": "Tương tự acyclovir nhưng dùng ít lần hơn",
            "protein_binding": "Tương tự acyclovir (9-33%)",
            "clearance": "Chuyển thành acyclovir, sau đó thải qua thận (tương tự acyclovir)"
        },
        "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm",
        "black_box_warnings": None,
        "drug_interactions": {
            "major": [
                {
                    "drug": "Probenecid",
                    "mechanism": "Probenecid ức chế bài tiết ống thận của acyclovir (sau khi valacyclovir chuyển thành acyclovir), làm giảm thải trừ và tăng nồng độ acyclovir trong máu.",
                    "effect": "Tăng nồng độ acyclovir, tăng thời gian bán thải, tăng nguy cơ độc tính (độc thận)",
                    "management": "Giảm liều valacyclovir 25-50% khi dùng với probenecid. Theo dõi chức năng thận và dấu hiệu độc tính chặt chẽ."
                },
                {
                    "drug": "Thuốc độc thận (Aminoglycosides, Vancomycin, Amphotericin B, Cisplatin)",
                    "mechanism": "Cả hai đều có độc tính thận, tác dụng cộng dồn làm tăng nguy cơ suy thận cấp.",
                    "effect": "Tăng nguy cơ suy thận cấp, độc thận nghiêm trọng, tăng creatinine",
                    "management": "TRÁNH DÙNG đồng thời nếu có thể. Nếu bắt buộc, theo dõi creatinine, BUN, lượng nước tiểu chặt chẽ. Duy trì đủ dịch. Có thể cần giảm liều cả hai thuốc."
                }
            ],
            "moderate": [
                {
                    "drug": "Cimetidine",
                    "mechanism": "Cimetidine có thể ức chế bài tiết ống thận của acyclovir (nhẹ).",
                    "effect": "Tăng nhẹ nồng độ acyclovir",
                    "management": "Theo dõi chức năng thận. Không cần điều chỉnh liều thường quy."
                },
                {
                    "drug": "Zidovudine (AZT)",
                    "mechanism": "Cả hai đều có thể gây độc thận và giảm bạch cầu, tác dụng cộng dồn.",
                    "effect": "Tăng nguy cơ độc thận, giảm bạch cầu",
                    "management": "Theo dõi chức năng thận và công thức máu. Thận trọng khi dùng đồng thời."
                }
            ],
            "minor": [
                {
                    "drug": "Mycophenolate",
                    "mechanism": "Cả hai đều có thể gây độc thận, tác dụng cộng dồn nhẹ.",
                    "effect": "Tăng nguy cơ độc thận (nhẹ)",
                    "management": "Theo dõi chức năng thận. Không cần điều chỉnh liều thường quy."
                }
            ]
        },
        "contraindications": {
            "tuyệt_đối": [
                "Dị ứng valacyclovir, acyclovir hoặc các thành phần",
                "Suy thận nặng (CrCl <10 ml/min) - chống chỉ định với liều cao (1g x 3 lần/ngày)",
                "Bệnh nhân suy giảm miễn dịch nặng với suy thận (tăng nguy cơ hội chứng tan máu-ure huyết)"
            ],
            "tương_đối": [
                "Suy thận nhẹ đến trung bình (CrCl 10-50) - giảm liều đáng kể, theo dõi chặt chẽ",
                "Suy thận nặng (CrCl <10) với liều thấp - giảm liều 75%, theo dõi chặt chẽ",
                "Mất nước - tăng nguy cơ độc thận, cần bù dịch đầy đủ",
                "Dùng với thuốc độc thận - tăng nguy cơ suy thận cấp",
                "Người cao tuổi - tăng nguy cơ độc thận, có thể cần giảm liều",
                "Bệnh nhân suy giảm miễn dịch (HIV, ghép tạng) - tăng nguy cơ hội chứng tan máu-ure huyết với liều cao"
            ]
        },
        "pregnancy_lactation": {
            "fda_category": "B",
            "pregnancy_details": "Valacyclovir là thuốc phân loại B (tương tự acyclovir). Valacyclovir là prodrug của acyclovir, chuyển thành acyclovir trong cơ thể. Các nghiên cứu trên động vật không cho thấy nguy cơ dị tật bẩm sinh, nhưng không có nghiên cứu đầy đủ trên phụ nữ có thai. Valacyclovir được sử dụng trong thai kỳ để điều trị nhiễm HSV và có vẻ an toàn. Nhiễm HSV có thể gây nguy hiểm cho thai nhi (nhiễm HSV ở trẻ sơ sinh, viêm não). Valacyclovir có thể được dùng khi lợi ích vượt quá nguy cơ. Ưu điểm: dùng ít lần hơn acyclovir, compliance tốt hơn.",
            "lactation": {
                "safety": "Compatible",
                "details": "Valacyclovir chuyển thành acyclovir trong cơ thể. Acyclovir bài tiết vào sữa mẹ ở nồng độ thấp (tương đương nồng độ trong máu mẹ). Nồng độ trong sữa mẹ thấp và không có báo cáo về tác dụng phụ đáng kể ở trẻ bú mẹ. Hấp thu qua đường tiêu hóa của trẻ sơ sinh thấp.",
                "recommendation": "Có thể dùng khi cho con bú. Dùng liều thấp nhất hiệu quả. Theo dõi trẻ sơ sinh nếu dùng liều cao hoặc kéo dài."
            }
        },
        "hepatic_adjustment": {
            "mild": "Không cần điều chỉnh liều. Valacyclovir chuyển hóa thành acyclovir (chủ yếu qua gan), nhưng acyclovir thải trừ qua thận.",
            "moderate": "Không cần điều chỉnh liều. Chuyển hóa có thể giảm nhẹ nhưng không đáng kể.",
            "severe": "Thận trọng, có thể cần giảm liều nhẹ. Chuyển hóa có thể giảm ở suy gan nặng.",
            "notes": "Valacyclovir chuyển hóa thành acyclovir bởi valacyclovir hydrolase (chủ yếu ở gan và ruột). Suy gan có thể làm giảm chuyển hóa valacyclovir, nhưng acyclovir thải trừ qua thận nên ít ảnh hưởng. Tuy nhiên, suy gan có thể kèm theo suy thận, nên cần điều chỉnh liều theo chức năng thận."
        },
        "overdose_management": {
            "symptoms": [
                "Triệu chứng độc thận: Tăng creatinine, BUN, giảm lượng nước tiểu, phù, suy thận cấp",
                "Triệu chứng thần kinh: Lú lẫn, co giật, ảo giác, rối loạn ý thức (hiếm, với liều rất cao)",
                "Triệu chứng tiêu hóa: Buồn nôn, nôn, đau bụng, tiêu chảy",
                "Hội chứng tan máu-ure huyết (TTP/HUS) - hiếm nhưng nghiêm trọng, đặc biệt ở bệnh nhân suy giảm miễn dịch với liều cao",
                "Triệu chứng nghiêm trọng: Suy thận cấp, TTP/HUS, rối loạn thần kinh nặng"
            ],
            "antidote": "Không có antidote đặc hiệu. Điều trị hỗ trợ và điều trị triệu chứng.",
            "treatment": [
                "Ngừng ngay valacyclovir",
                "Bù dịch đầy đủ: Truyền dịch để tăng thải trừ qua thận và giảm nguy cơ kết tinh ở thận",
                "Theo dõi chức năng thận: Creatinine, BUN, lượng nước tiểu",
                "Điều trị suy thận cấp nếu có:",
                "  - Bù dịch đầy đủ",
                "  - Điều chỉnh điện giải",
                "  - Lọc máu nếu cần (hemodialysis có thể loại bỏ acyclovir)",
                "Điều trị rối loạn thần kinh nếu có:",
                "  - Hỗ trợ hô hấp nếu cần",
                "  - Điều trị co giật: Benzodiazepine",
                "  - Theo dõi thần kinh chặt chẽ",
                "Điều trị TTP/HUS nếu có:",
                "  - Plasmapheresis",
                "  - Truyền máu nếu cần",
                "  - Điều trị hỗ trợ",
                "Theo dõi dấu hiệu sinh tồn: Huyết áp, nhịp tim, nhịp thở, SpO2",
                "Lọc máu: Hemodialysis có thể loại bỏ acyclovir nếu suy thận nặng"
            ],
            "monitoring": "Theo dõi chức năng thận (creatinine, BUN, lượng nước tiểu), công thức máu (nếu nghi ngờ TTP/HUS), dấu hiệu thần kinh, dấu hiệu sinh tồn trong ít nhất 24-48 giờ. Theo dõi lâu hơn nếu có suy thận cấp, TTP/HUS hoặc rối loạn thần kinh."
        },
        "reversal_agents": None,
        "administration_instructions": {
            "oral": {
                "with_food": "Có thể uống với hoặc không thức ăn. Uống với nước đầy đủ (ít nhất 1-2 ly nước) để giảm nguy cơ kết tinh ở thận. Uống với thức ăn có thể giảm buồn nôn.",
                "timing": "Uống 1-3 lần/ngày tùy chỉ định (herpes simplex: 2 lần/ngày, shingles: 3 lần/ngày, prophylaxis: 1 lần/ngày). Cách đều trong ngày. Có thể uống với hoặc sau bữa ăn để giảm buồn nôn. Ưu điểm: dùng ít lần hơn acyclovir (2-3 lần/ngày thay vì 5 lần/ngày), compliance tốt hơn."
            },
            "iv": None
        },
        "references": {
            "primary_sources": [
                "FDA Drug Label - Valacyclovir (Valtrex)",
                "UpToDate - Valacyclovir: Drug Information",
                "Medscape - Valacyclovir Drug Reference",
                "Goodman & Gilman's The Pharmacological Basis of Therapeutics (14th ed)",
                "Lexicomp Online - Valacyclovir Monograph",
                "Micromedex - Valacyclovir Drug Information",
                "IDSA Guidelines - Herpes Simplex Virus Infections"
            ],
            "last_updated": "2024-12-19",
            "evidence_level": "A - Dựa trên FDA drug labels, IDSA guidelines, và dữ liệu lâm sàng từ nhiều nguồn"
        },
        "risk_flags": {
            "high_alert": False,
            "narrow_therapeutic_index": False,
            "icu_critical_care_only": False,
            "bleeding_risk": None,
            "organ_toxicity": {"renal": "Nephrotoxicity (high doses, dehydration - dose-dependent)", "neurological": "Neurotoxicity (confusion, hallucinations - especially in renal impairment)", "hematologic": "Thrombotic thrombocytopenic purpura/hemolytic uremic syndrome (TTP/HUS - in immunocompromised patients)"},
            "qt_prolongation": False,
            "hepatotoxicity": False,
            "nephrotoxicity": True,
            "requires_monitoring": ["Renal function (CrCl, creatinine, BUN - dose adjustment required, critical)", "Neurological status (confusion, hallucinations - especially in elderly/renal impairment)", "TTP/HUS signs (pallor, bruising, oliguria - in immunocompromised patients)", "Fluid balance (maintain adequate hydration)"],
            "look_alike_sound_alike": ["Valacyclovir", "Acyclovir"]
        },
        "guideline_tags": [
            "IDSA Guidelines - Herpes Simplex Virus Infections",
            "IDSA Guidelines - Herpes Zoster",
            "WHO Essential Medicines List"
        ],
        "last_updated": "2025-02-18"
    },
}

__all__ = ['HERPES_ANTIVIRALS']
