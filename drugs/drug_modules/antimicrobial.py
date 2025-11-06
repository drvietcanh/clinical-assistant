"""
Antimicrobial Medications (Antibiotics, Antivirals, Antifungals)
Generated from drug_database_data.py
"""

ANTIMICROBIAL_DRUGS = {
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
            "absolute": [
                "Dị ứng acyclovir hoặc valacyclovir",
                "Suy thận nặng (CrCl <10 ml/min) khi dùng IV - chống chỉ định tuyệt đối với IV",
                "Rối loạn thần kinh nặng không kiểm soát (khi dùng IV)"
            ],
            "relative": [
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
        }
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
            "absolute": [
                "Dị ứng valacyclovir, acyclovir hoặc các thành phần",
                "Suy thận nặng (CrCl <10 ml/min) - chống chỉ định với liều cao (1g x 3 lần/ngày)",
                "Bệnh nhân suy giảm miễn dịch nặng với suy thận (tăng nguy cơ hội chứng tan máu-ure huyết)"
            ],
            "relative": [
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
        }
    },
    "Oseltamivir": {
        "group": "Infectious Disease - Antiviral (Neuraminidase Inhibitor)",
        "vietnamese_name": "Oseltamivir, Tamiflu",
        "administration": ["PO"],
        "indications": [
            "Cúm A và B (treatment)",
            "Phòng ngừa cúm",
            "Cúm ở người suy giảm miễn dịch"
        ],
        "contraindications": [
            "Dị ứng",
            "Suy thận nặng (thận trọng)"
        ],
        "dosage": {
            "adult_treatment": "75mg x 2 lần/ngày x 5 ngày",
            "adult_prophylaxis": "75mg x 1 lần/ngày x 10 ngày (sau tiếp xúc) hoặc x 6 tuần (mùa cúm)",
            "adult_max": "150mg x 2 lần/ngày (suy giảm miễn dịch)",
            "notes": "Bắt đầu trong 48 giờ đầu triệu chứng. Hiệu quả nhất trong 24 giờ đầu"
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "75mg x 1 lần/ngày (treatment), 75mg cách ngày (prophylaxis)",
            "under_30": "75mg x 1 lần/ngày (treatment), 75mg cách 2 ngày (prophylaxis)"
        },
        "side_effects": [
            "Buồn nôn, nôn",
            "Đau đầu",
            "Tiêu chảy",
            "Rối loạn tâm thần (hiếm, ở trẻ em)",
            "Co giật (hiếm)"
        ],
        "interactions": [
            "Probenecid: tăng nồng độ oseltamivir",
            "Ít tương tác khác"
        ],
        "pregnancy": "C",
        "mechanism_of_action": "Oseltamivir là thuốc kháng virus cúm, thuộc nhóm chất ức chế neuraminidase. Oseltamivir phosphate là tiền thuốc (prodrug), được chuyển hóa trong gan thành oseltamivir carboxylate (chất hoạt động). Oseltamivir carboxylate ức chế enzyme neuraminidase của virus cúm A và B, enzyme này có vai trò quan trọng trong việc giải phóng các hạt virus mới từ tế bào chủ và lan truyền virus trong đường hô hấp. Bằng cách ức chế neuraminidase, oseltamivir ngăn chặn sự giải phóng virus, làm giảm lan truyền virus và giảm thời gian bệnh. Oseltamivir hiệu quả với cả cúm A và cúm B, nhưng hiệu quả nhất khi bắt đầu điều trị trong vòng 48 giờ đầu (tốt nhất là 24 giờ đầu) sau khi xuất hiện triệu chứng.",
        "monitoring": [
            "Triệu chứng cúm (sốt, ho, đau họng, đau cơ) - đánh giá đáp ứng điều trị",
            "Dấu hiệu biến chứng (viêm phổi, suy hô hấp, nhiễm trùng thứ phát)",
            "Tác dụng phụ (buồn nôn, nôn, đau đầu, tiêu chảy) - thường nhẹ",
            "Rối loạn tâm thần ở trẻ em (kích động, lú lẫn, hành vi bất thường) - hiếm nhưng cần theo dõi",
            "Co giật - hiếm, đặc biệt ở trẻ em",
            "Chức năng thận (creatinine) - điều chỉnh liều ở suy thận",
            "Tương tác với probenecid (tăng nồng độ oseltamivir)"
        ],
        "precautions": [
            "Bắt đầu điều trị càng sớm càng tốt - hiệu quả nhất trong vòng 48 giờ đầu (tốt nhất là 24 giờ đầu) sau khi xuất hiện triệu chứng",
            "Điều chỉnh liều ở suy thận: CrCl 30-60: 75mg x 1 lần/ngày (treatment), 75mg cách ngày (prophylaxis); CrCl <30: 75mg x 1 lần/ngày (treatment), 75mg cách 2 ngày (prophylaxis)",
            "Uống với thức ăn để giảm buồn nôn, nôn",
            "Rối loạn tâm thần ở trẻ em - hiếm nhưng có thể nghiêm trọng, cần theo dõi chặt chẽ",
            "Thận trọng ở bệnh nhân suy thận nặng - cần điều chỉnh liều",
            "Probenecid tăng nồng độ oseltamivir - có thể cần điều chỉnh liều",
            "Hiệu quả phòng ngừa: dùng 75mg x 1 lần/ngày x 10 ngày sau tiếp xúc hoặc x 6 tuần trong mùa cúm",
            "Liều cao hơn (150mg x 2 lần/ngày) có thể cần ở bệnh nhân suy giảm miễn dịch",
            "Không thay thế vaccine cúm - vaccine vẫn là biện pháp phòng ngừa chính",
            "Kháng thuốc có thể xảy ra - theo dõi đáp ứng điều trị"
        ],
        "pharmacokinetics": {
            "half_life": "1-3 giờ (oseltamivir), 6-10 giờ (oseltamivir carboxylate - chất hoạt động)",
            "onset": "24-48 giờ (giảm triệu chứng)",
            "duration": "5 ngày (treatment), 10 ngày - 6 tuần (prophylaxis)",
            "protein_binding": "3% (oseltamivir carboxylate)",
            "clearance": "Gan: chuyển hóa oseltamivir thành oseltamivir carboxylate (chất hoạt động) qua esterase. Thận: bài tiết chủ yếu qua thận (oseltamivir carboxylate bài tiết nguyên dạng). Cần điều chỉnh liều ở suy thận."
        },
        "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm, tránh ánh sáng. Viên nén: bảo quản trong bao bì kín. Dạng suspension: bảo quản ở nhiệt độ phòng, lắc kỹ trước khi dùng, dùng trong vòng 10 ngày sau khi pha hoặc 17 ngày nếu bảo quản trong tủ lạnh.",
        "black_box_warnings": None
    },
    "Ganciclovir": {
        "group": "Infectious Disease - Antiviral",
        "vietnamese_name": "Ganciclovir, Cytovene",
        "administration": ["IV", "PO"],
        "indications": [
            "Nhiễm CMV ở người suy giảm miễn dịch",
            "Phòng ngừa CMV sau ghép tạng",
            "Viêm võng mạc do CMV",
            "CMV bẩm sinh"
        ],
        "contraindications": [
            "Dị ứng",
            "Suy thận nặng",
            "Có thai",
            "Giảm bạch cầu <500",
            "Giảm tiểu cầu <25,000"
        ],
        "dosage": {
            "adult_iv_induction": "5mg/kg IV mỗi 12 giờ x 14-21 ngày",
            "adult_iv_maintenance": "5mg/kg IV x 1 lần/ngày hoặc 6mg/kg x 5 lần/tuần",
            "adult_po": "1g x 3 lần/ngày (sau IV induction)",
            "notes": "Theo dõi bạch cầu, tiểu cầu, chức năng thận. Rất độc với tủy xương"
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "50_80": "Giảm liều 50%",
            "25_50": "Giảm liều 75%",
            "under_25": "Giảm liều 90%"
        },
        "side_effects": [
            "Giảm bạch cầu (phổ biến, nặng)",
            "Giảm tiểu cầu",
            "Giảm hồng cầu",
            "Độc thận",
            "Độc thần kinh",
            "Sốt",
            "Ban da",
            "Rất độc - chỉ dùng khi cần thiết"
        ],
        "interactions": [
            "Probenecid: tăng nồng độ ganciclovir",
            "Zidovudine: tăng độc tính tủy xương",
            "Mycophenolate: tăng nồng độ ganciclovir"
        ],
        "pregnancy": "C - D (với CMV)",
        "mechanism_of_action": "Ganciclovir là thuốc kháng virus, là nucleotide analog của guanosine, tương tự acyclovir nhưng có hiệu quả mạnh hơn với cytomegalovirus (CMV). Sau khi vào tế bào nhiễm CMV, ganciclovir được phosphoryl hóa bởi virus UL97 kinase thành ganciclovir monophosphate, sau đó được phosphoryl hóa tiếp bởi enzyme tế bào thành ganciclovir triphosphate (GCV-TP). GCV-TP ức chế cạnh tranh DNA polymerase của CMV, gây chấm dứt chuỗi DNA và ngăn chặn sự nhân lên của virus. Ganciclovir có hiệu quả với CMV (acyclovir không hiệu quả) và HSV, VZV. Tuy nhiên, ganciclovir cũng được phosphoryl hóa ở tế bào người (ở mức độ thấp hơn), dẫn đến độc tính cao hơn acyclovir, đặc biệt độc với tủy xương (giảm bạch cầu, tiểu cầu, hồng cầu nghiêm trọng). Ganciclovir chỉ dùng khi thực sự cần thiết (CMV nặng ở người suy giảm miễn dịch).",
        "monitoring": [
            "Công thức máu (CBC) - QUAN TRỌNG: giảm bạch cầu, tiểu cầu, hồng cầu là tác dụng phụ phổ biến và nghiêm trọng (2-3 lần/tuần khi dùng IV)",
            "Bạch cầu - giảm bạch cầu nặng phổ biến, ngừng nếu <500/mm³",
            "Tiểu cầu - giảm tiểu cầu phổ biến, ngừng nếu <25,000/mm³",
            "Hồng cầu - thiếu máu có thể xảy ra",
            "Chức năng thận (creatinine, BUN) - độc thận có thể xảy ra, điều chỉnh liều ở suy thận",
            "Dấu hiệu độc thần kinh (lú lẫn, co giật, ảo giác, rối loạn tâm thần) - hiếm nhưng có thể nghiêm trọng",
            "Dấu hiệu nhiễm trùng (sốt, nhiễm trùng) - do giảm bạch cầu",
            "Dấu hiệu chảy máu (chảy máu, bầm tím) - do giảm tiểu cầu",
            "Tương tác với probenecid (tăng nồng độ), zidovudine (tăng độc tính tủy xương), mycophenolate (tăng nồng độ ganciclovir)"
        ],
        "precautions": [
            "RẤT ĐỘC - chỉ dùng khi thực sự cần thiết (CMV nặng ở người suy giảm miễn dịch)",
            "CHỐNG CHỈ ĐỊNH nếu bạch cầu <500/mm³ hoặc tiểu cầu <25,000/mm³",
            "Giảm bạch cầu, tiểu cầu, hồng cầu - tác dụng phụ phổ biến và nghiêm trọng, cần theo dõi chặt chẽ CBC (2-3 lần/tuần khi dùng IV)",
            "Ngừng ngay nếu bạch cầu <500/mm³ hoặc tiểu cầu <25,000/mm³",
            "Có thể cần dùng G-CSF (filgrastim) để tăng bạch cầu, hoặc truyền tiểu cầu",
            "Điều chỉnh liều ở suy thận QUAN TRỌNG: CrCl 50-80: giảm liều 50%; CrCl 25-50: giảm liều 75%; CrCl <25: giảm liều 90%",
            "CHỐNG CHỈ ĐỊNH trong thai kỳ - gây dị tật thai nhi, ung thư ở động vật (category D với CMV)",
            "Độc thần kinh - hiếm nhưng có thể nghiêm trọng (lú lẫn, co giật, ảo giác), cần theo dõi",
            "Độc thận - theo dõi chức năng thận, điều chỉnh liều",
            "Tránh dùng với zidovudine (tăng độc tính tủy xương)",
            "Thận trọng với probenecid (tăng nồng độ ganciclovir), mycophenolate (tăng nồng độ ganciclovir)",
            "Truyền IV chậm (trong 1 giờ) để giảm độc tính",
            "Duy trì đủ dịch để giảm độc thận",
            "Dùng đủ liều và đủ thời gian (induction 14-21 ngày, sau đó maintenance)"
        ],
        "pharmacokinetics": {
            "half_life": "2.5-3.5 giờ (IV), 3-4 giờ (PO)",
            "onset": "Nhanh sau khi vào tế bào",
            "duration": "Ngắn (cần dùng nhiều lần/ngày)",
            "protein_binding": "1-2% (không gắn protein)",
            "clearance": "Thận: bài tiết chủ yếu qua thận (90% nguyên dạng, không chuyển hóa). Hấp thu PO kém (6-9% bioavailability). Cần điều chỉnh liều ở suy thận (tỷ lệ với CrCl)."
        },
        "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm, tránh ánh sáng. Dung dịch IV: bảo quản ở 2-8°C, pha xong dùng trong 24 giờ. Viên nén: bảo quản trong bao bì kín.",
        "black_box_warnings": "RẤT ĐỘC với tủy xương - giảm bạch cầu, tiểu cầu, hồng cầu nghiêm trọng phổ biến. CHỐNG CHỈ ĐỊNH nếu bạch cầu <500/mm³ hoặc tiểu cầu <25,000/mm³. Theo dõi CBC 2-3 lần/tuần khi dùng IV. CHỐNG CHỈ ĐỊNH trong thai kỳ - gây dị tật thai nhi, ung thư ở động vật (category D với CMV). Chỉ dùng khi thực sự cần thiết. Nguy cơ độc thần kinh (lú lẫn, co giật, ảo giác)."
    },
    "Ribavirin": {
        "group": "Infectious Disease - Antiviral",
        "vietnamese_name": "Ribavirin, Rebetol",
        "administration": ["PO", "IV", "Inhalation"],
        "indications": [
            "Viêm gan C (kết hợp với interferon)",
            "Viêm gan C (kết hợp với sofosbuvir)",
            "Sốt Lassa (IV)",
            "RSV ở trẻ sơ sinh (inhalation)"
        ],
        "contraindications": [
            "Có thai (nam và nữ)",
            "Suy thận nặng",
            "Bệnh tim nặng",
            "Thiếu máu nặng",
            "Dị ứng"
        ],
        "dosage": {
            "adult_hcv": "800-1200mg/ngày chia 2 lần (tùy genotype và trọng lượng)",
            "adult_hcv_sofosbuvir": "1000mg/ngày (nếu >75kg) hoặc 800mg/ngày (<75kg)",
            "adult_iv": "30-35mg/kg x 1 lần (loading), sau đó 15-20mg/kg mỗi 6 giờ",
            "notes": "Rất độc. Nam và nữ phải dùng biện pháp tránh thai 6 tháng sau khi ngừng"
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "Giảm liều 50%",
            "under_30": "Không dùng"
        },
        "side_effects": [
            "Thiếu máu (phổ biến, có thể nặng)",
            "Giảm bạch cầu",
            "Dị tật thai nhi (nam và nữ - chống chỉ định tuyệt đối nếu có thai)",
            "Rối loạn tâm thần",
            "Rối loạn hô hấp (inhalation)",
            "Rất độc"
        ],
        "interactions": [
            "Zidovudine: tăng độc tính",
            "Didanosine: tăng độc tính",
            "Azathioprine: tăng độc tính"
        ],
        "pregnancy": "X - Chống chỉ định tuyệt đối",
        "mechanism_of_action": "Ribavirin là nucleoside analog (guanosine), ức chế tổng hợp RNA và DNA của virus. Thuốc được phosphoryl hóa trong tế bào thành ribavirin triphosphate, ức chế RNA polymerase của virus, gây đột biến và ngăn chặn sao chép virus. Ribavirin cũng ức chế inosine monophosphate dehydrogenase (IMPDH), làm giảm GTP nội bào, ảnh hưởng đến tổng hợp RNA virus. Thuốc có tác dụng phổ rộng trên nhiều virus RNA, đặc biệt hiệu quả trong điều trị viêm gan C khi kết hợp với interferon hoặc sofosbuvir. Ribavirin rất độc, gây thiếu máu, dị tật thai nhi, và các tác dụng phụ nghiêm trọng khác.",
        "monitoring": [
            "Công thức máu (CBC) - theo dõi thiếu máu, giảm bạch cầu, giảm tiểu cầu - mỗi 2-4 tuần",
            "Hemoglobin (Hb) - mục tiêu: giữ >10g/dL, nếu <8.5g/dL cần giảm liều hoặc ngừng",
            "Chức năng thận (creatinine, BUN) - trước khi bắt đầu và định kỳ",
            "Chức năng gan (ALT, AST, bilirubin) - theo dõi đáp ứng điều trị HCV",
            "Tâm thần (trầm cảm, rối loạn tâm thần) - đặc biệt khi dùng với interferon",
            "Dấu hiệu quá liều (thiếu máu nặng, mệt mỏi)",
            "Xét nghiệm thai (nam và nữ) - trước khi bắt đầu và định kỳ"
        ],
        "precautions": [
            "Rất độc - chỉ dùng khi thật sự cần thiết",
            "Chống chỉ định tuyệt đối trong thai kỳ (nam và nữ) - gây dị tật thai nhi nghiêm trọng",
            "Nam và nữ phải dùng biện pháp tránh thai hiệu quả trong và 6 tháng sau khi ngừng",
            "Kiểm tra thai trước khi bắt đầu điều trị (nam và nữ)",
            "Không dùng nếu CrCl <50 (suy thận nặng)",
            "Giảm liều 50% nếu CrCl 30-50",
            "Thận trọng ở bệnh nhân bệnh tim (nguy cơ thiếu máu)",
            "Theo dõi sát hemoglobin - nếu <8.5g/dL: giảm liều hoặc ngừng",
            "Có thể cần truyền máu nếu thiếu máu nặng",
            "Thận trọng ở bệnh nhân có tiền sử rối loạn tâm thần (đặc biệt khi dùng với interferon)"
        ],
        "pharmacokinetics": {
            "half_life": "298 giờ (12.4 ngày) - rất dài, tích tụ trong tế bào",
            "onset": "2-4 giờ",
            "duration": "Rất dài do half-life dài",
            "protein_binding": "Không đáng kể",
            "clearance": "Thận (chủ yếu), một phần qua gan"
        },
        "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm, tránh ánh sáng",
        "black_box_warnings": "Chống chỉ định tuyệt đối trong thai kỳ (nam và nữ) - gây dị tật thai nhi và tử vong thai nhi. Có thể gây thiếu máu nặng, đe dọa tính mạng. Có thể gây rối loạn tâm thần nghiêm trọng"
    },
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
            "absolute": [
                "Dị ứng fluconazole hoặc các azole antifungals khác",
                "Có thai (3 tháng đầu) - chống chỉ định tuyệt đối, có thể gây dị tật thai nhi",
                "Dùng terfenadine hoặc astemizole với liều fluconazole ≥400mg/ngày - tăng nguy cơ QT kéo dài, loạn nhịp tim nghiêm trọng"
            ],
            "relative": [
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
        "black_box_warnings": "CHỐNG CHỈ ĐỊNH ở bệnh nhân suy tim sung huyết hoặc có tiền sử suy tim. Itraconazole có thể gây suy tim, đặc biệt ở liều cao. CHỐNG CHỈ ĐỊNH trong thai kỳ - gây dị tật thai nhi (category D). Nhiều tương tác thuốc nghiêm trọng do ức chế CYP3A4 - tăng nguy cơ tiêu cơ vân với simvastatin/lovastatin, tăng an thần với midazolam/triazolam, tăng nguy cơ loạn nhịp với quinidine."
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
        "black_box_warnings": "CHỐNG CHỈ ĐỊNH trong thai kỳ - gây dị tật thai nhi (category D). Nguy cơ suy gan nghiêm trọng, có thể gây tử vong. Theo dõi chức năng gan trước và trong khi điều trị. Ngừng ngay nếu có suy gan. Nguy cơ QT kéo dài và rối loạn nhịp tim. Theo dõi ECG nếu có nguy cơ. Nguy cơ rối loạn thị giác (thường thoáng qua). CHỐNG CHỈ ĐỊNH với rifampin, rifabutin, carbamazepine, phenobarbital, ergotamine."
    },
    "Nystatin": {
        "group": "Infectious Disease - Antifungal (Polyene)",
        "vietnamese_name": "Nystatin, Mycostatin",
        "administration": ["PO (suspension, tablet)", "Topical"],
        "indications": [
            "Nhiễm nấm Candida miệng (oral candidiasis/thrush)",
            "Nhiễm nấm Candida thực quản",
            "Nhiễm nấm Candida da (topical)",
            "Nhiễm nấm Candida âm đạo (topical)"
        ],
        "contraindications": [
            "Dị ứng nystatin"
        ],
        "dosage": {
            "adult_oral_suspension": "400,000-600,000 đơn vị x 4 lần/ngày",
            "adult_oral_tablet": "500,000-1,000,000 đơn vị x 4 lần/ngày",
            "adult_topical": "Bôi 2-3 lần/ngày",
            "notes": "Không hấp thu qua đường tiêu hóa. Chỉ tác dụng tại chỗ. Súc miệng và nuốt (suspension)"
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "Không đổi",
            "under_30": "Không đổi"
        },
        "side_effects": [
            "Buồn nôn, nôn (hiếm, PO)",
            "Tiêu chảy (hiếm, PO)",
            "Kích ứng da (hiếm, topical)",
            "Dị ứng (hiếm)"
        ],
        "interactions": [
            "Rất ít tương tác (không hấp thu hệ thống)"
        ],
        "pregnancy": "C - An toàn (không hấp thu)",
        "mechanism_of_action": "Nystatin là polyene antifungal, gắn với ergosterol trong màng tế bào nấm, tạo lỗ thủng trong màng, làm rò rỉ các ion và chất dinh dưỡng, dẫn đến chết tế bào nấm. Thuốc có ái lực cao với ergosterol (có trong nấm) nhưng không gắn với cholesterol (có trong tế bào người), nên an toàn cho tế bào người. Nystatin không hấp thu qua đường tiêu hóa hoặc qua da, nên chỉ tác dụng tại chỗ. Thuốc hiệu quả trên Candida species, đặc biệt Candida albicans, thường dùng cho nhiễm nấm miệng, thực quản, và da.",
        "monitoring": [
            "Đáp ứng điều trị (giảm triệu chứng, giảm mảng trắng trong miệng)",
            "Dấu hiệu dị ứng (ban da, kích ứng)",
            "Triệu chứng tiêu hóa (buồn nôn, tiêu chảy) - hiếm",
            "Tái nhiễm (nếu điều trị không đủ hoặc yếu tố nguy cơ vẫn còn)"
        ],
        "precautions": [
            "Suspension: súc miệng kỹ, giữ trong miệng vài phút, sau đó nuốt (cho nhiễm nấm thực quản)",
            "Tablet: ngậm trong miệng cho tan (cho nhiễm nấm miệng)",
            "Topical: bôi đều, rửa sạch tay sau khi bôi",
            "Tiếp tục điều trị 48 giờ sau khi hết triệu chứng",
            "Với nhiễm nấm miệng: điều trị 7-14 ngày",
            "Với nhiễm nấm thực quản: điều trị 14-21 ngày",
            "An toàn trong thai kỳ và cho con bú (không hấp thu)",
            "Rất ít tác dụng phụ do không hấp thu hệ thống",
            "Thận trọng ở bệnh nhân có vết thương mở rộng (topical)"
        ],
        "pharmacokinetics": {
            "half_life": "Không áp dụng (không hấp thu)",
            "onset": "Tác dụng tại chỗ ngay lập tức",
            "duration": "Tác dụng tại chỗ trong vài giờ",
            "protein_binding": "Không áp dụng (không vào máu)",
            "clearance": "Không hấp thu, thải trừ qua phân (PO) hoặc rửa trôi (topical)"
        },
        "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh đông lạnh, lắc kỹ trước khi dùng (suspension)",
        "black_box_warnings": None
    },

"Piperacillin-tazobactam": {
    "group": "Antibiotic - Penicillin/Beta-lactamase Inhibitor",
    "vietnamese_name": "Piperacillin-tazobactam, Tazocin, Zosyn",
    "administration": ["IV"],
    "indications": [
        "Nhiễm khuẩn nặng (bệnh viện)",
        "Nhiễm khuẩn ổ bụng",
        "Nhiễm khuẩn da và mô mềm",
        "Viêm phổi bệnh viện",
        "Nhiễm khuẩn đường tiết niệu phức tạp",
        "Nhiễm khuẩn huyết"
    ],
    "contraindications": [
        "Dị ứng penicillin",
        "Dị ứng beta-lactam"
    ],
    "dosage": {
        "adult_standard": "4.5g IV mỗi 8 giờ",
        "adult_severe": "4.5g IV mỗi 6 giờ",
        "adult_nosocomial_pneumonia": "4.5g IV mỗi 6 giờ",
        "notes": "Liều tối đa: 18g/ngày. Pha trong 50-150ml NS hoặc D5W, truyền trong 30 phút"
    },
    "renal_adjustment": {
        "normal": "Không đổi",
        "30_60": "4.5g IV mỗi 8 giờ",
        "under_30": "2.25g IV mỗi 8 giờ",
        "hemodialysis": "2.25g IV mỗi 8 giờ (sau lọc máu)"
    },
    "side_effects": [
        "Tiêu chảy",
        "Buồn nôn, nôn",
        "Phát ban",
        "Tăng men gan",
        "Giảm tiểu cầu (hiếm)",
        "Giảm bạch cầu (hiếm)"
    ],
    "interactions": [
        "Warfarin: có thể tăng INR",
        "Aminoglycosides: không pha chung, truyền riêng"
    ],
    "pregnancy": "B",
        "mechanism_of_action": "Piperacillin: penicillin phổ rộng, ức chế tổng hợp thành tế bào vi khuẩn bằng cách gắn với penicillin-binding proteins (PBPs). Tazobactam: beta-lactamase inhibitor, bảo vệ piperacillin khỏi bị phân hủy bởi beta-lactamase (TEM, SHV, OXA). Kết hợp này mở rộng phổ kháng khuẩn, đặc biệt hiệu quả với Pseudomonas aeruginosa, Enterobacteriaceae (bao gồm một số ESBL), và kỵ khí. Tazobactam không có hoạt tính kháng khuẩn riêng, chỉ có tác dụng bảo vệ.",
        "monitoring": [
            "Chức năng thận (creatinine, eGFR) - điều chỉnh liều theo thận",
            "Điện giải (natri - mỗi 4.5g chứa 2.79 mEq natri, kali - có thể tăng)",
            "Dấu hiệu nhiễm trùng (sốt, WBC, CRP)",
            "Cấy máu và cấy từ vị trí nhiễm trùng",
            "Dấu hiệu nhiễm C. difficile",
            "Chức năng gan (ALT, AST) - hiếm viêm gan",
            "Thời gian prothrombin/PT (hiếm giảm prothrombin)",
            "Số lượng tiểu cầu (hiếm giảm tiểu cầu)",
            "Đường huyết (có thể tăng hoặc giảm)"
        ],
        "precautions": [
            "Phải điều chỉnh liều theo chức năng thận (eGFR) - đặc biệt quan trọng",
            "Hàm lượng natri cao (2.79 mEq/4.5g) - thận trọng ở suy tim, tăng huyết áp, phù",
            "Không dùng ở bệnh nhân dị ứng penicillins (phản ứng chéo cao)",
            "Nguy cơ nhiễm C. difficile - theo dõi tiêu chảy",
            "Có thể gây giảm prothrombin → tăng nguy cơ chảy máu, đặc biệt ở suy thận, suy gan, dùng kéo dài",
            "Theo dõi nhiễm nấm thứ phát khi dùng kéo dài",
            "Pha trong NS hoặc D5W, truyền IV trong 30 phút (liều chuẩn) hoặc 3-4 giờ (liều cao/extended infusion)",
            "Extended infusion (3-4 giờ) được khuyến cáo cho Pseudomonas aeruginosa để tối ưu hóa pharmacokinetics/pharmacodynamics (PK/PD)",
            "Không pha trộn với vancomycin (tạo kết tủa)"
        ],
        "pharmacokinetics": {
            "half_life": "0.7-1.2 giờ (piperacillin), 0.7-1 giờ (tazobactam)",
            "onset": "Ngay lập tức sau khi truyền IV",
            "duration": "Liều 4.5g q6h hoặc q8h, extended infusion q8h",
            "protein_binding": "30% (piperacillin), 20-30% (tazobactam)",
            "metabolism": "Piperacillin: thủy phân một phần, tazobactam: thủy phân",
            "clearance": "Chủ yếu qua thận (68% piperacillin, 80% tazobactam bài tiết nguyên dạng), cần điều chỉnh thận"
        },
        "storage": "Bảo quản bột khô ở nhiệt độ phòng (20-25°C). Sau khi pha: bảo quản ở nhiệt độ phòng 24 giờ, hoặc trong tủ lạnh 7 ngày. Không đông lạnh.",
        "black_box_warnings": "Không có black box warning. Tuy nhiên, hàm lượng natri cao có thể gây vấn đề ở bệnh nhân suy tim hoặc cần hạn chế natri. Giảm prothrombin có thể gây chảy máu nặng.",
        "drug_interactions": {
            "major": [
                {
                    "drug": "Warfarin",
                    "mechanism": "Piperacillin-tazobactam có thể ức chế tổng hợp vitamin K phụ thuộc vào hệ vi khuẩn đường ruột, làm giảm sản xuất các yếu tố đông máu phụ thuộc vitamin K. Ngoài ra, có thể ức chế chuyển hóa warfarin.",
                    "effect": "Tăng INR, tăng nguy cơ chảy máu, đặc biệt ở bệnh nhân suy thận, suy gan, dùng kéo dài",
                    "management": "Theo dõi INR thường xuyên (ít nhất 2-3 lần/tuần khi bắt đầu dùng piperacillin-tazobactam). Có thể cần giảm liều warfarin. Đặc biệt thận trọng ở bệnh nhân suy thận, suy gan, dùng kéo dài (>7 ngày)."
                },
                {
                    "drug": "Methotrexate",
                    "mechanism": "Piperacillin có thể ức chế bài tiết ống thận của methotrexate, làm giảm thải trừ và tăng nồng độ methotrexate.",
                    "effect": "Tăng nồng độ methotrexate, tăng nguy cơ độc tính (giảm bạch cầu, độc thận, viêm niêm mạc)",
                    "management": "TRÁNH DÙNG đồng thời nếu có thể. Nếu bắt buộc, theo dõi chặt chẽ nồng độ methotrexate, công thức máu, chức năng thận. Có thể cần giảm liều methotrexate hoặc tăng khoảng cách giữa các liều."
                }
            ],
            "moderate": [
                {
                    "drug": "Aminoglycosides (Gentamicin, Tobramycin, Amikacin)",
                    "mechanism": "Cả hai đều có độc tính thận, tác dụng cộng dồn. Ngoài ra, aminoglycosides có thể bị bất hoạt về mặt hóa học bởi beta-lactams khi pha chung.",
                    "effect": "Tăng nguy cơ độc thận, giảm hiệu quả kháng khuẩn của aminoglycosides nếu pha chung",
                    "management": "Không pha chung trong cùng một ống truyền. Truyền riêng biệt. Theo dõi chức năng thận chặt chẽ (creatinine, BUN). Có thể cần giảm liều hoặc tăng khoảng cách giữa các liều."
                },
                {
                    "drug": "Vancomycin",
                    "mechanism": "Cả hai đều có độc tính thận, tác dụng cộng dồn. Ngoài ra, có thể tạo kết tủa khi pha chung.",
                    "effect": "Tăng nguy cơ độc thận, kết tủa khi pha chung",
                    "management": "Không pha chung. Truyền riêng biệt. Theo dõi chức năng thận chặt chẽ. Theo dõi nồng độ vancomycin nếu có thể."
                },
                {
                    "drug": "Probenecid",
                    "mechanism": "Probenecid ức chế bài tiết ống thận của piperacillin, làm giảm thải trừ và tăng nồng độ piperacillin.",
                    "effect": "Tăng nồng độ piperacillin, tăng thời gian bán thải",
                    "management": "Có thể cần giảm liều piperacillin-tazobactam. Theo dõi chức năng thận. Thường không cần điều chỉnh liều thường quy."
                }
            ],
            "minor": [
                {
                    "drug": "Thuốc tránh thai đường uống",
                    "mechanism": "Kháng sinh phổ rộng có thể làm giảm hệ vi khuẩn đường ruột, làm giảm tái hấp thu estrogen từ đường ruột.",
                    "effect": "Giảm hiệu quả thuốc tránh thai (hiếm, nhưng có thể xảy ra)",
                    "management": "Khuyến cáo sử dụng biện pháp tránh thai bổ sung (bao cao su) trong khi dùng kháng sinh và 7 ngày sau khi ngừng."
                }
            ]
        },
        "contraindications": {
            "absolute": [
                "Dị ứng penicillin hoặc beta-lactam (phản ứng type I - sốc phản vệ, phù mạch, phát ban nặng)",
                "Dị ứng tazobactam",
                "Tiền sử phản ứng dị ứng nặng với beta-lactam (penicillin, cephalosporin, carbapenem)"
            ],
            "relative": [
                "Suy thận nặng (CrCl <20) - cần giảm liều đáng kể, theo dõi chặt chẽ",
                "Suy tim, phù, tăng huyết áp - hàm lượng natri cao (2.79 mEq/4.5g) có thể làm nặng thêm tình trạng",
                "Suy gan nặng - tăng nguy cơ giảm prothrombin và chảy máu",
                "Rối loạn đông máu - tăng nguy cơ chảy máu do giảm prothrombin",
                "Bệnh nhân đang dùng warfarin - tăng nguy cơ chảy máu",
                "Tiền sử nhiễm C. difficile - tăng nguy cơ tái phát"
            ]
        },
        "pregnancy_lactation": {
            "fda_category": "B",
            "pregnancy_details": "Piperacillin-tazobactam là thuốc phân loại B. Các nghiên cứu trên động vật không cho thấy nguy cơ dị tật bẩm sinh, nhưng không có nghiên cứu đầy đủ trên phụ nữ có thai. Penicillins nói chung được coi là an toàn trong thai kỳ và được sử dụng rộng rãi. Piperacillin-tazobactam có thể được dùng khi lợi ích vượt quá nguy cơ, đặc biệt trong nhiễm khuẩn nặng. Tuy nhiên, cần thận trọng với hàm lượng natri cao và nguy cơ giảm prothrombin. Nên tránh dùng kéo dài nếu có thể.",
            "lactation": {
                "safety": "Compatible",
                "details": "Piperacillin và tazobactam bài tiết vào sữa mẹ ở nồng độ thấp. Nồng độ trong sữa mẹ thấp và không có báo cáo về tác dụng phụ đáng kể ở trẻ bú mẹ. Penicillins nói chung được coi là an toàn khi cho con bú.",
                "recommendation": "Có thể dùng khi cho con bú. Theo dõi trẻ sơ sinh về dấu hiệu tiêu chảy, phát ban, hoặc các tác dụng phụ khác. Dùng liều thấp nhất hiệu quả."
            }
        },
        "hepatic_adjustment": {
            "mild": "Không cần điều chỉnh liều. Piperacillin và tazobactam không chuyển hóa đáng kể qua gan, thải trừ chủ yếu qua thận.",
            "moderate": "Không cần điều chỉnh liều. Tuy nhiên, cần thận trọng với nguy cơ giảm prothrombin và chảy máu. Theo dõi PT/INR.",
            "severe": "Không cần điều chỉnh liều. Tuy nhiên, tăng nguy cơ giảm prothrombin và chảy máu. Theo dõi PT/INR chặt chẽ. Có thể cần bổ sung vitamin K hoặc điều chỉnh liều thuốc chống đông nếu đang dùng.",
            "notes": "Piperacillin và tazobactam không chuyển hóa đáng kể qua gan, thải trừ chủ yếu qua thận (68% piperacillin, 80% tazobactam bài tiết nguyên dạng). Không cần điều chỉnh liều ở bệnh nhân suy gan. Tuy nhiên, suy gan có thể kèm theo suy thận, nên cần điều chỉnh liều theo chức năng thận. Ngoài ra, suy gan làm tăng nguy cơ giảm prothrombin và chảy máu, cần theo dõi PT/INR."
        },
        "overdose_management": {
            "symptoms": [
                "Triệu chứng thần kinh: Co giật, rối loạn ý thức (hiếm, thường chỉ với liều rất cao)",
                "Triệu chứng điện giải: Tăng natri máu (do hàm lượng natri cao), rối loạn điện giải",
                "Triệu chứng chảy máu: Chảy máu kéo dài, tăng INR (do giảm prothrombin)",
                "Triệu chứng thận: Suy thận cấp, tăng creatinine (hiếm với liều thông thường)",
                "Triệu chứng tiêu hóa: Tiêu chảy nặng, buồn nôn, nôn",
                "Triệu chứng dị ứng: Phát ban, phù mạch, sốc phản vệ (nếu dị ứng)"
            ],
            "antidote": "Không có antidote đặc hiệu. Điều trị hỗ trợ và điều trị triệu chứng.",
            "treatment": [
                "Ngừng ngay piperacillin-tazobactam",
                "Điều trị co giật nếu có: Benzodiazepine (diazepam, lorazepam), phenobarbital",
                "Điều chỉnh điện giải: Điều chỉnh natri máu nếu tăng natri, bù dịch phù hợp",
                "Điều trị chảy máu:",
                "  - Bổ sung vitamin K nếu giảm prothrombin",
                "  - Truyền huyết tương tươi đông lạnh (FFP) nếu chảy máu nặng",
                "  - Điều chỉnh liều thuốc chống đông nếu đang dùng",
                "Điều trị suy thận cấp nếu có:",
                "  - Bù dịch đầy đủ",
                "  - Điều chỉnh điện giải",
                "  - Lọc máu nếu cần (hemodialysis có thể loại bỏ piperacillin và tazobactam)",
                "Điều trị dị ứng nếu có:",
                "  - Epinephrine nếu sốc phản vệ",
                "  - Antihistamine, corticosteroid",
                "  - Hỗ trợ hô hấp nếu cần",
                "Theo dõi dấu hiệu sinh tồn: Huyết áp, nhịp tim, nhịp thở, SpO2",
                "Lọc máu: Hemodialysis có thể loại bỏ piperacillin và tazobactam nếu suy thận nặng"
            ],
            "monitoring": "Theo dõi dấu hiệu thần kinh (co giật, ý thức), điện giải (natri, kali), PT/INR, chức năng thận (creatinine, BUN, lượng nước tiểu), dấu hiệu chảy máu, dấu hiệu sinh tồn trong ít nhất 24-48 giờ. Theo dõi lâu hơn nếu có suy thận cấp hoặc rối loạn đông máu."
        },
        "reversal_agents": None,
        "administration_instructions": {
            "oral": {
                "with_food": "Không áp dụng - chỉ có dạng IV",
                "timing": "Không áp dụng - chỉ có dạng IV"
            },
            "iv": {
                "reconstitution": "Pha với NS (0.9% NaCl) hoặc D5W (5% Dextrose). Thể tích pha: 50-150ml cho liều 4.5g. Nồng độ pha: 90mg/ml (4.5g/50ml) đến 30mg/ml (4.5g/150ml). Pha 4.5g trong 50ml = 90mg/ml. Pha 4.5g trong 100ml = 45mg/ml. Pha 4.5g trong 150ml = 30mg/ml. Lắc kỹ để hòa tan hoàn toàn.",
                "infusion_rate": "Liều chuẩn (4.5g q6h hoặc q8h): Truyền trong 30 phút. Extended infusion (4.5g q8h trong 3-4 giờ): Được khuyến cáo cho Pseudomonas aeruginosa để tối ưu hóa PK/PD. Tốc độ: 50ml/30 phút = ~1.7ml/phút (liều chuẩn), 50ml/3-4 giờ = ~0.25-0.33ml/phút (extended infusion).",
                "compatibility": ["NS (0.9% NaCl)", "D5W (5% Dextrose)", "Ringer's Lactate"],
                "incompatibility": [
                    "Vancomycin - tạo kết tủa, không pha chung",
                    "Aminoglycosides - có thể bị bất hoạt khi pha chung, truyền riêng biệt",
                    "Amphotericin B - không tương thích",
                    "Các thuốc có tính kiềm hoặc acid mạnh"
                ],
                "notes": "QUAN TRỌNG: 1) Không pha chung với vancomycin (tạo kết tủa), 2) Không pha chung với aminoglycosides (truyền riêng biệt), 3) Điều chỉnh liều theo CrCl, 4) Hàm lượng natri cao (2.79 mEq/4.5g) - thận trọng ở suy tim, 5) Extended infusion (3-4 giờ) được khuyến cáo cho Pseudomonas aeruginosa, 6) Theo dõi PT/INR ở bệnh nhân suy thận, suy gan, dùng kéo dài."
            }
        },
        "references": {
            "primary_sources": [
                "FDA Drug Label - Piperacillin-Tazobactam (Zosyn)",
                "UpToDate - Piperacillin-Tazobactam: Drug Information",
                "Medscape - Piperacillin-Tazobactam Drug Reference",
                "Goodman & Gilman's The Pharmacological Basis of Therapeutics (14th ed)",
                "Lexicomp Online - Piperacillin-Tazobactam Monograph",
                "Micromedex - Piperacillin-Tazobactam Drug Information",
                "IDSA Guidelines - Hospital-Acquired Pneumonia, Intra-abdominal Infections"
            ],
            "last_updated": "2025-02-03",
            "evidence_level": "A - Dựa trên FDA drug labels, IDSA guidelines, và dữ liệu lâm sàng từ nhiều nguồn"
        }

},

"Meropenem": {
    "group": "Antibiotic - Carbapenem",
    "vietnamese_name": "Meropenem, Meronem",
    "administration": ["IV"],
    "indications": [
        "Nhiễm khuẩn nặng đa kháng",
        "Nhiễm khuẩn bệnh viện",
        "Viêm màng não",
        "Nhiễm khuẩn ổ bụng",
        "Nhiễm khuẩn huyết"
    ],
    "contraindications": [
        "Dị ứng carbapenem",
        "Dị ứng beta-lactam nặng"
    ],
    "dosage": {
        "adult_standard": "1g IV mỗi 8 giờ",
        "adult_severe": "1g IV mỗi 6 giờ hoặc 2g IV mỗi 8 giờ",
        "adult_meningitis": "2g IV mỗi 8 giờ",
        "notes": "Truyền trong 15-30 phút. Phổ rộng, dự phòng kháng penicillinase"
    },
    "renal_adjustment": {
        "normal": "Không đổi",
        "30_60": "1g IV mỗi 12 giờ",
        "under_30": "500mg-1g IV mỗi 12 giờ",
        "hemodialysis": "500mg-1g IV mỗi 12 giờ (sau lọc máu)"
    },
    "side_effects": [
        "Tiêu chảy",
        "Phát ban",
        "Co giật (liều cao, suy thận)",
        "Tăng men gan",
        "Viêm tĩnh mạch tại chỗ tiêm"
    ],
    "interactions": [
        "Valproate: giảm nồng độ valproate (có thể gây co giật)",
        "Probenecid: tăng nồng độ meropenem"
    ],
    "pregnancy": "B",
        "mechanism_of_action": "Carbapenem kháng sinh beta-lactam. Ức chế tổng hợp thành tế bào vi khuẩn bằng cách gắn với penicillin-binding proteins (PBPs), đặc biệt PBP-2, dẫn đến ly giải tế bào vi khuẩn. Phổ kháng khuẩn rộng, bao phủ cả vi khuẩn Gram-dương, Gram-âm, và kỵ khí. Kháng được nhiều beta-lactamase do có cấu trúc vòng beta-lactam bền vững. Đặc biệt hiệu quả với Enterobacteriaceae (bao gồm ESBL-producing), Pseudomonas aeruginosa, và kỵ khí.",
        "monitoring": [
            "Chức năng thận (creatinine, eGFR) - điều chỉnh liều theo thận",
            "Dấu hiệu nhiễm trùng (sốt, WBC, CRP, procalcitonin)",
            "Cấy máu và cấy từ vị trí nhiễm trùng để đánh giá đáp ứng",
            "Dấu hiệu nhiễm trùng thứ phát (nấm, C. difficile)",
            "Co giật (nguy cơ tăng ở suy thận, bệnh thần kinh trung ương)",
            "Chức năng gan (ALT, AST) - hiếm nhưng có thể tăng",
            "Số lượng tiểu cầu (hiếm giảm tiểu cầu)"
        ],
        "precautions": [
            "Phải điều chỉnh liều theo chức năng thận (eGFR) - giảm liều và tăng khoảng cách liều",
            "Nguy cơ co giật tăng ở: suy thận nặng (CrCl < 25), bệnh thần kinh trung ương, tiền sử co giật",
            "Không dùng ở bệnh nhân dị ứng penicillins hoặc cephalosporins (phản ứng chéo ~1%)",
            "Nguy cơ nhiễm C. difficile - theo dõi tiêu chảy, phân lỏng",
            "Có thể gây kháng thuốc nếu dùng không đúng chỉ định - chỉ dùng khi thực sự cần",
            "Theo dõi nhiễm nấm thứ phát (đặc biệt Candida) khi dùng kéo dài",
            "Pha trong dung dịch NS hoặc D5W, truyền IV trong 15-30 phút",
            "Không pha trộn với các thuốc khác (có thể tương kỵ)"
        ],
        "pharmacokinetics": {
            "half_life": "1 giờ (bình thường), 1.5-2.5 giờ (suy thận)",
            "onset": "Ngay lập tức sau khi truyền IV",
            "duration": "Liều 1g q8h đạt nồng độ hiệu quả",
            "protein_binding": "2% (rất thấp)",
            "metabolism": "Thủy phân trong gan (40%), không qua CYP450",
            "clearance": "Chủ yếu qua thận (70% bài tiết nguyên dạng), cần điều chỉnh thận"
        },
        "storage": "Bảo quản bột khô ở nhiệt độ phòng (20-25°C). Sau khi pha: bảo quản ở nhiệt độ phòng 2-4 giờ, hoặc trong tủ lạnh 24 giờ. Không đông lạnh.",
        "black_box_warnings": "Không có black box warning. Tuy nhiên, nguy cơ co giật tăng ở suy thận nặng và bệnh nhân có tiền sử co giật. Kháng thuốc có thể phát triển nếu dùng không đúng chỉ định.",
        "drug_interactions": {
            "major": [
                {
                    "drug": "Valproate (Valproic acid)",
                    "mechanism": "Meropenem ức chế hấp thu và tăng thải trừ valproate, làm giảm nồng độ valproate trong máu đáng kể (có thể giảm 50-70%).",
                    "effect": "Giảm nồng độ valproate, mất kiểm soát co giật, nguy cơ co giật nặng",
                    "management": "TRÁNH dùng cùng nếu có thể. Nếu bắt buộc: tăng liều valproate, theo dõi nồng độ valproate trong máu thường xuyên, cân nhắc dùng thuốc chống co giật khác. Theo dõi chặt chẽ dấu hiệu co giật."
                },
                {
                    "drug": "Probenecid",
                    "mechanism": "Probenecid ức chế bài tiết meropenem qua thận, làm tăng nồng độ và thời gian bán thải của meropenem.",
                    "effect": "Tăng nồng độ meropenem, tăng nguy cơ tác dụng phụ (co giật, độc tính thần kinh)",
                    "management": "GIẢM LIỀU meropenem hoặc tăng khoảng cách liều. Theo dõi chặt chẽ dấu hiệu độc tính. Không khuyến cáo dùng cùng."
                }
            ],
            "moderate": [
                {
                    "drug": "Warfarin",
                    "mechanism": "Meropenem có thể ảnh hưởng đến hệ vi khuẩn đường ruột, làm giảm sản xuất vitamin K, tăng tác dụng của warfarin.",
                    "effect": "Tăng tác dụng warfarin, tăng nguy cơ chảy máu",
                    "management": "Theo dõi INR thường xuyên. Có thể cần giảm liều warfarin. Theo dõi dấu hiệu chảy máu."
                }
            ],
            "minor": [
                {
                    "drug": "Các kháng sinh beta-lactam khác",
                    "mechanism": "Có thể có tương tác phụ thuộc thời gian (time-dependent killing), nhưng thường không dùng cùng.",
                    "effect": "Không rõ, thường không dùng cùng",
                    "management": "Không khuyến cáo dùng cùng. Chọn một kháng sinh phù hợp."
                }
            ]
        },
        "contraindications": {
            "absolute": [
                "Dị ứng meropenem hoặc carbapenem",
                "Dị ứng penicillins hoặc cephalosporins nặng (phản ứng chéo ~1%, nhưng có thể nguy hiểm)"
            ],
            "relative": [
                "Suy thận nặng (CrCl < 25ml/min) - tăng nguy cơ co giật, cần giảm liều mạnh",
                "Bệnh thần kinh trung ương - tăng nguy cơ co giật",
                "Tiền sử co giật - tăng nguy cơ co giật",
                "Suy gan nặng - thận trọng, mặc dù chủ yếu thải qua thận",
                "Người cao tuổi - tăng nguy cơ co giật, suy thận",
                "Dùng với valproate - giảm nồng độ valproate, mất kiểm soát co giật",
                "Dùng với probenecid - tăng nồng độ meropenem"
            ]
        },
        "pregnancy_lactation": {
            "fda_category": "B",
            "pregnancy_details": "Meropenem là thuốc phân loại B. Có một số nghiên cứu trên động vật không cho thấy nguy cơ cho thai nhi. Không có nghiên cứu đầy đủ trên phụ nữ có thai. Meropenem có thể qua nhau thai, nhưng nồng độ trong máu thai nhi thấp. Được sử dụng trong nhiễm trùng nặng ở phụ nữ có thai và được coi là an toàn khi lợi ích vượt quá nguy cơ. Nhiễm trùng nặng có thể nguy hiểm cho cả mẹ và thai nhi.",
            "lactation": {
                "safety": "Compatible",
                "details": "Meropenem bài tiết vào sữa mẹ ở nồng độ thấp. Không có báo cáo về tác dụng phụ ở trẻ bú mẹ. Nồng độ trong sữa mẹ thấp và không đáng kể.",
                "recommendation": "Có thể dùng khi cho con bú. Meropenem bài tiết vào sữa mẹ ở nồng độ thấp và không gây tác dụng phụ ở trẻ bú mẹ."
            }
        },
        "hepatic_adjustment": {
            "mild": "Không cần điều chỉnh liều. Meropenem chủ yếu thải qua thận, không phụ thuộc vào chức năng gan.",
            "moderate": "Không cần điều chỉnh liều.",
            "severe": "Thận trọng, nhưng không cần điều chỉnh liều thường quy. Meropenem chủ yếu thải qua thận. Theo dõi chức năng gan nếu có triệu chứng.",
            "notes": "Meropenem chủ yếu thải qua thận (70% bài tiết nguyên dạng), chỉ 40% chuyển hóa ở gan. Không cần điều chỉnh liều ở suy gan. Tuy nhiên, thận trọng ở suy gan nặng."
        },
        "overdose_management": {
            "symptoms": [
                "Co giật (nguy hiểm, đặc biệt ở suy thận nặng)",
                "Độc tính thần kinh trung ương (lú lẫn, kích động)",
                "Tăng men gan (ALT, AST)",
                "Giảm tiểu cầu (hiếm)",
                "Tiêu chảy nặng",
                "Nhiễm C. difficile (tiêu chảy, đau bụng, sốt)"
            ],
            "antidote": "Không có antidote đặc hiệu cho quá liều meropenem. Điều trị hỗ trợ và điều trị triệu chứng.",
            "treatment": [
                "Ngừng ngay meropenem nếu đang truyền",
                "Theo dõi dấu hiệu sinh tồn: Huyết áp, nhịp tim, nhịp thở, SpO2",
                "Nếu co giật:",
                "  - Benzodiazepine (diazepam 5-10mg IV, lorazepam 2-4mg IV) - điều trị chính",
                "  - Nếu không đáp ứng: Phenytoin, phenobarbital",
                "  - Hỗ trợ hô hấp: Thở oxy, nếu cần hỗ trợ thông khí cơ học",
                "Nếu độc tính thần kinh trung ương:",
                "  - Hỗ trợ tâm lý, an ủi bệnh nhân",
                "  - Theo dõi chặt chẽ, thường tự hồi phục sau khi ngừng thuốc",
                "Nếu nhiễm C. difficile:",
                "  - Ngừng meropenem và các kháng sinh khác nếu có thể",
                "  - Metronidazole 500mg PO x 3 lần/ngày x 10-14 ngày",
                "  - Hoặc Vancomycin 125mg PO x 4 lần/ngày x 10-14 ngày (nếu nặng)",
                "  - Theo dõi dấu hiệu viêm đại tràng giả mạc",
                "Nếu tăng men gan:",
                "  - Ngừng meropenem nếu tăng nặng",
                "  - Theo dõi chức năng gan",
                "  - Thường tự hồi phục sau khi ngừng thuốc",
                "Hỗ trợ hô hấp: Thở oxy, nếu cần hỗ trợ thông khí cơ học",
                "Theo dõi dấu hiệu sinh tồn: Huyết áp, nhịp tim, nhịp thở, SpO2 trong ít nhất 24-48 giờ",
                "Có thể cần lọc máu nếu suy thận nặng (meropenem có thể được loại bỏ qua lọc máu)"
            ],
            "monitoring": "Theo dõi dấu hiệu sinh tồn (huyết áp, nhịp tim, nhịp thở, SpO2) liên tục trong ít nhất 24-48 giờ sau khi ngừng meropenem. Theo dõi lâu hơn nếu có biến chứng (co giật, độc tính thần kinh, nhiễm C. difficile)."
        },
        "reversal_agents": {
            "available": False,
            "agents": [],
            "notes": "Không có reversal agent đặc hiệu cho meropenem. Điều trị hỗ trợ và điều trị triệu chứng (benzodiazepine cho co giật)."
        },
        "administration_instructions": {
            "oral": None,
            "iv": {
                "reconstitution": "Pha bột khô trong NS hoặc D5W: 500mg pha trong 10ml = 50mg/ml, 1g pha trong 20ml = 50mg/ml. Sau đó pha loãng trong 50-250ml NS hoặc D5W để truyền.",
                "infusion_rate": "Truyền IV trong 15-30 phút. Không truyền nhanh hơn (có thể gây co giật). Liều: 1g IV mỗi 8 giờ (bình thường), 500mg-1g IV mỗi 12 giờ (suy thận).",
                "compatibility": ["NS (0.9% NaCl)", "D5W (5% Dextrose)"],
                "incompatibility": ["Không trộn với các thuốc khác. Dùng đường truyền riêng hoặc flush trước/sau khi truyền thuốc khác."],
                "notes": "QUAN TRỌNG: 1) PHẢI điều chỉnh liều theo chức năng thận (eGFR), 2) Truyền trong 15-30 phút (không nhanh hơn), 3) Nguy cơ co giật tăng ở suy thận nặng và bệnh nhân có tiền sử co giật, 4) TRÁNH dùng với valproate (giảm nồng độ valproate), 5) Theo dõi nhiễm C. difficile, 6) Không pha trộn với các thuốc khác."
            }
        },
        "references": {
            "primary_sources": [
                "FDA Drug Label - Meropenem",
                "IDSA Guidelines - Antimicrobial Therapy",
                "UpToDate - Meropenem: Drug Information",
                "Medscape - Meropenem Drug Reference",
                "Goodman & Gilman's The Pharmacological Basis of Therapeutics (14th ed)",
                "Lexicomp Online - Meropenem Monograph",
                "Micromedex - Meropenem Drug Information"
            ],
            "last_updated": "2025-02-03",
            "evidence_level": "A - Dựa trên FDA drug labels, IDSA guidelines, và dữ liệu lâm sàng từ nhiều nguồn"
        }

},

"Clindamycin": {
    "group": "Antibiotic - Lincosamide",
    "vietnamese_name": "Clindamycin, Dalacin",
    "administration": ["PO", "IV", "IM"],
    "indications": [
        "Nhiễm khuẩn kỵ khí",
        "Nhiễm khuẩn da và mô mềm",
        "Viêm phổi do vi khuẩn",
        "Nhiễm khuẩn răng miệng",
        "Sốt do chuột cắn"
    ],
    "contraindications": [
        "Dị ứng clindamycin",
        "Viêm đại tràng giả mạc trước đây"
    ],
    "dosage": {
        "adult_po": "150-450mg x 3-4 lần/ngày",
        "adult_iv": "600-900mg IV mỗi 8 giờ",
        "adult_severe": "900mg IV mỗi 8 giờ",
        "notes": "Có thể gây viêm đại tràng giả mạc (C. difficile). Dùng với thức ăn"
    },
    "renal_adjustment": {
        "normal": "Không đổi",
        "30_60": "Không đổi",
        "under_30": "Không đổi (không thải qua thận)"
    },
    "side_effects": [
        "Tiêu chảy (phổ biến)",
        "Viêm đại tràng giả mạc (C. difficile - nghiêm trọng)",
        "Buồn nôn, nôn",
        "Phát ban",
        "Rối loạn vị giác"
    ],
    "interactions": [
        "Erythromycin: đối kháng",
        "Neuromuscular blockers: tăng tác dụng"
    ],
    "pregnancy": "B",
        "mechanism_of_action": "Lincosamide kháng sinh. Ức chế tổng hợp protein vi khuẩn bằng cách gắn với tiểu phần 50S của ribosome, ngăn cản quá trình dịch mã. Phổ kháng khuẩn: Gram-dương mạnh (Staphylococcus, Streptococcus, bao gồm một số MRSA), kỵ khí (Bacteroides, Clostridium), và một số vi khuẩn không điển hình. Không hiệu quả với Enterobacteriaceae (Gram-âm). Đặc biệt hiệu quả với kỵ khí và được dùng trong nhiễm trùng răng miệng, xương, và mô mềm.",
        "monitoring": [
            "Dấu hiệu nhiễm trùng (sốt, WBC)",
            "Cấy máu và cấy từ vị trí nhiễm trùng",
            "Dấu hiệu nhiễm C. difficile (tiêu chảy, đau bụng) - nguy cơ CAO",
            "Chức năng gan (ALT, AST) - hiếm viêm gan",
            "Số lượng bạch cầu (hiếm giảm bạch cầu, giảm bạch cầu trung tính)",
            "Phản ứng tại chỗ tiêm (viêm tĩnh mạch, đau)",
            "Phát ban (hiếm hội chứng Stevens-Johnson)"
        ],
        "precautions": [
            "Nguy cơ nhiễm C. difficile CAO - đây là một trong những kháng sinh có nguy cơ cao nhất",
            "NGỪNG NGAY nếu có tiêu chảy, đau bụng - có thể là C. difficile",
            "Không dùng cho điều trị dự phòng (trừ một số trường hợp đặc biệt) để giảm nguy cơ C. difficile",
            "Theo dõi sát dấu hiệu nhiễm C. difficile trong và sau khi dùng",
            "Có thể gây giảm bạch cầu trung tính (hiếm nhưng nguy hiểm)",
            "Tương kỵ với nhiều thuốc - không pha trộn",
            "Pha trong NS hoặc D5W, truyền IV trong ít nhất 10-60 phút (tùy liều)",
            "Không dùng cho nhiễm trùng do vi khuẩn Gram-âm (không hiệu quả)",
            "Uống với nước đầy đủ để giảm kích ứng thực quản"
        ],
        "pharmacokinetics": {
            "half_life": "2-3 giờ",
            "onset": "30-60 phút (PO), ngay lập tức (IV)",
            "duration": "q6h hoặc q8h (PO/IV)",
            "protein_binding": "90-95% (rất cao)",
            "metabolism": "Gan (CYP3A4) - một phần",
            "clearance": "Gan và thận, không cần điều chỉnh thận nhưng thận trọng ở suy gan"
        },
        "storage": "Bảo quản ở nhiệt độ phòng (20-25°C). Viên nang: tránh ẩm. Dung dịch pha tiêm: sau khi pha, bảo quản ở nhiệt độ phòng 24 giờ.",
        "black_box_warnings": "Không có black box warning. Tuy nhiên, nguy cơ nhiễm C. difficile rất cao, có thể gây viêm đại tràng giả mạc nặng, có thể tử vong. Ngừng ngay nếu có tiêu chảy.",
        "drug_interactions": {
            "major": [
                {
                    "drug": "Erythromycin",
                    "mechanism": "Cả hai đều gắn với tiểu phần 50S của ribosome, đối kháng cạnh tranh, làm giảm hiệu quả kháng khuẩn của cả hai thuốc.",
                    "effect": "Giảm hiệu quả kháng khuẩn của cả hai thuốc",
                    "management": "TRÁNH DÙNG đồng thời. Chọn một trong hai thuốc. Nếu đã dùng erythromycin, chờ ít nhất 2-3 giờ trước khi dùng clindamycin."
                },
                {
                    "drug": "Neuromuscular blocking agents (Succinylcholine, Vecuronium, Rocuronium)",
                    "mechanism": "Clindamycin có thể tăng cường tác dụng của thuốc giãn cơ, gây tê liệt kéo dài và suy hô hấp.",
                    "effect": "Tăng tác dụng giãn cơ, tăng thời gian tê liệt, tăng nguy cơ suy hô hấp",
                    "management": "Thận trọng khi dùng đồng thời. Theo dõi chức năng hô hấp chặt chẽ. Có thể cần giảm liều thuốc giãn cơ. Đảm bảo có thiết bị hỗ trợ hô hấp sẵn sàng."
                }
            ],
            "moderate": [
                {
                    "drug": "Warfarin",
                    "mechanism": "Clindamycin có thể ức chế tổng hợp vitamin K phụ thuộc vào hệ vi khuẩn đường ruột, làm giảm sản xuất các yếu tố đông máu phụ thuộc vitamin K.",
                    "effect": "Tăng INR, tăng nguy cơ chảy máu",
                    "management": "Theo dõi INR thường xuyên (ít nhất 2-3 lần/tuần khi bắt đầu dùng clindamycin). Có thể cần giảm liều warfarin. Đặc biệt thận trọng ở bệnh nhân dùng kéo dài (>7 ngày)."
                },
                {
                    "drug": "Kaolin-pectin (thuốc chống tiêu chảy)",
                    "mechanism": "Kaolin-pectin có thể hấp phụ clindamycin, làm giảm hấp thu và giảm nồng độ clindamycin trong máu.",
                    "effect": "Giảm hấp thu clindamycin, giảm hiệu quả kháng khuẩn",
                    "management": "Cách ít nhất 2 giờ giữa clindamycin và kaolin-pectin. Không dùng kaolin-pectin nếu đang điều trị C. difficile (có thể làm nặng bệnh)."
                }
            ],
            "minor": [
                {
                    "drug": "Thuốc tránh thai đường uống",
                    "mechanism": "Kháng sinh phổ rộng có thể làm giảm hệ vi khuẩn đường ruột, làm giảm tái hấp thu estrogen từ đường ruột.",
                    "effect": "Giảm hiệu quả thuốc tránh thai (hiếm, nhưng có thể xảy ra)",
                    "management": "Khuyến cáo sử dụng biện pháp tránh thai bổ sung (bao cao su) trong khi dùng kháng sinh và 7 ngày sau khi ngừng."
                }
            ]
        },
        "contraindications": {
            "absolute": [
                "Dị ứng clindamycin hoặc lincomycin",
                "Viêm đại tràng giả mạc trước đây do C. difficile (tiền sử)"
            ],
            "relative": [
                "Tiền sử nhiễm C. difficile - tăng nguy cơ tái phát",
                "Suy gan nặng - giảm chuyển hóa, tăng nguy cơ tác dụng phụ",
                "Bệnh nhân đang dùng thuốc giãn cơ - tăng nguy cơ tê liệt kéo dài",
                "Bệnh nhân đang dùng warfarin - tăng nguy cơ chảy máu",
                "Nhiễm trùng do vi khuẩn Gram-âm - không hiệu quả"
            ]
        },
        "pregnancy_lactation": {
            "fda_category": "B",
            "pregnancy_details": "Clindamycin là thuốc phân loại B. Các nghiên cứu trên động vật không cho thấy nguy cơ dị tật bẩm sinh, nhưng không có nghiên cứu đầy đủ trên phụ nữ có thai. Clindamycin được sử dụng rộng rãi trong thai kỳ và có vẻ an toàn. Có thể được dùng khi lợi ích vượt quá nguy cơ, đặc biệt trong nhiễm khuẩn kỵ khí. Tuy nhiên, cần thận trọng với nguy cơ nhiễm C. difficile, có thể nghiêm trọng trong thai kỳ.",
            "lactation": {
                "safety": "Compatible",
                "details": "Clindamycin bài tiết vào sữa mẹ ở nồng độ thấp. Nồng độ trong sữa mẹ thấp và không có báo cáo về tác dụng phụ đáng kể ở trẻ bú mẹ. Tuy nhiên, có thể gây tiêu chảy hoặc phát ban ở trẻ sơ sinh.",
                "recommendation": "Có thể dùng khi cho con bú. Theo dõi trẻ sơ sinh về dấu hiệu tiêu chảy, phát ban, hoặc các tác dụng phụ khác. Dùng liều thấp nhất hiệu quả."
            }
        },
        "hepatic_adjustment": {
            "mild": "Không cần điều chỉnh liều. Clindamycin chuyển hóa một phần qua gan (CYP3A4), nhưng không tích lũy đáng kể.",
            "moderate": "Thận trọng, có thể cần giảm liều. Theo dõi chức năng gan và dấu hiệu tác dụng phụ.",
            "severe": "Giảm liều 25-50% hoặc tăng khoảng cách giữa các liều. Theo dõi chức năng gan chặt chẽ. Có thể cần giảm tần suất dùng (q12h thay vì q8h).",
            "notes": "Clindamycin chuyển hóa một phần qua gan (CYP3A4), nhưng thải trừ chủ yếu qua gan và thận. Không tích lũy đáng kể ở suy gan nhẹ, nhưng có thể tích lũy ở suy gan nặng. Cần điều chỉnh liều ở suy gan nặng."
        },
        "overdose_management": {
            "symptoms": [
                "Triệu chứng tiêu hóa: Tiêu chảy nặng, đau bụng, buồn nôn, nôn (có thể là C. difficile)",
                "Triệu chứng thần kinh: Co giật, rối loạn ý thức (hiếm, thường chỉ với liều rất cao)",
                "Triệu chứng hô hấp: Suy hô hấp (nếu dùng với thuốc giãn cơ)",
                "Triệu chứng chảy máu: Chảy máu kéo dài, tăng INR (khi dùng với warfarin)",
                "Triệu chứng gan: Tăng men gan, viêm gan (hiếm)",
                "Triệu chứng dị ứng: Phát ban, phù mạch, sốc phản vệ (nếu dị ứng)"
            ],
            "antidote": "Không có antidote đặc hiệu. Điều trị hỗ trợ và điều trị triệu chứng.",
            "treatment": [
                "Ngừng ngay clindamycin",
                "Điều trị C. difficile nếu có:",
                "  - Ngừng ngay clindamycin",
                "  - Điều trị bằng vancomycin PO hoặc metronidazole PO",
                "  - Bù dịch đầy đủ",
                "  - Theo dõi dấu hiệu viêm đại tràng nặng (sốt, đau bụng, tiêu chảy máu)",
                "Điều trị co giật nếu có: Benzodiazepine (diazepam, lorazepam), phenobarbital",
                "Điều trị suy hô hấp nếu có:",
                "  - Hỗ trợ hô hấp (thở máy nếu cần)",
                "  - Điều trị tê liệt do thuốc giãn cơ nếu có",
                "Điều trị chảy máu nếu có:",
                "  - Bổ sung vitamin K nếu giảm prothrombin",
                "  - Truyền huyết tương tươi đông lạnh (FFP) nếu chảy máu nặng",
                "  - Điều chỉnh liều warfarin nếu đang dùng",
                "Điều trị dị ứng nếu có:",
                "  - Epinephrine nếu sốc phản vệ",
                "  - Antihistamine, corticosteroid",
                "  - Hỗ trợ hô hấp nếu cần",
                "Theo dõi dấu hiệu sinh tồn: Huyết áp, nhịp tim, nhịp thở, SpO2",
                "Lọc máu: Hemodialysis không hiệu quả do protein binding cao (90-95%)"
            ],
            "monitoring": "Theo dõi dấu hiệu C. difficile (tiêu chảy, đau bụng, sốt), dấu hiệu thần kinh (co giật, ý thức), chức năng hô hấp (nếu dùng với thuốc giãn cơ), PT/INR (nếu dùng với warfarin), chức năng gan (ALT, AST), dấu hiệu chảy máu, dấu hiệu sinh tồn trong ít nhất 24-48 giờ. Theo dõi lâu hơn nếu có C. difficile hoặc suy hô hấp."
        },
        "reversal_agents": None,
        "administration_instructions": {
            "oral": {
                "with_food": "Có thể uống với hoặc không thức ăn. Uống với thức ăn có thể giảm kích ứng dạ dày nhưng không ảnh hưởng đáng kể đến hấp thu.",
                "timing": "Uống 3-4 lần/ngày (150-450mg mỗi lần). Cách đều trong ngày. Uống với nhiều nước (ít nhất 200ml) để giảm kích ứng thực quản."
            },
            "iv": {
                "reconstitution": "Pha với NS (0.9% NaCl) hoặc D5W (5% Dextrose). Nồng độ pha: 6-12mg/ml. Pha 600mg trong 50ml = 12mg/ml. Pha 900mg trong 50ml = 18mg/ml (quá đậm, không dùng). Pha 900mg trong 100ml = 9mg/ml. Lắc kỹ để hòa tan hoàn toàn.",
                "infusion_rate": "Truyền IV trong ít nhất 10-60 phút (tùy liều). Liều 600mg: truyền trong 10-30 phút. Liều 900mg: truyền trong 30-60 phút. Tốc độ: 50ml/30 phút = ~1.7ml/phút. KHÔNG truyền nhanh (bolus) - tăng nguy cơ viêm tĩnh mạch.",
                "compatibility": ["NS (0.9% NaCl)", "D5W (5% Dextrose)", "Ringer's Lactate"],
                "incompatibility": [
                    "Aminophylline - tạo kết tủa, không pha chung",
                    "Phenytoin - tạo kết tủa, không pha chung",
                    "Barbiturates - tạo kết tủa, không pha chung",
                    "Các thuốc có tính kiềm hoặc acid mạnh"
                ],
                "notes": "QUAN TRỌNG: 1) Không pha chung với aminophylline, phenytoin, barbiturates (tạo kết tủa), 2) Truyền chậm (ít nhất 10-60 phút) để giảm viêm tĩnh mạch, 3) Theo dõi sát dấu hiệu C. difficile, 4) Không dùng cho nhiễm trùng do vi khuẩn Gram-âm."
            },
            "im": {
                "reconstitution": "Pha với NS (0.9% NaCl) hoặc D5W (5% Dextrose). Nồng độ pha: 150mg/ml (tối đa). Pha 600mg trong 4ml = 150mg/ml. Lắc kỹ để hòa tan hoàn toàn.",
                "injection_site": "Tiêm sâu vào cơ (gluteus maximus hoặc vastus lateralis). Tránh tiêm vào mạch máu.",
                "notes": "Tiêm sâu vào cơ. Có thể gây đau tại chỗ. Liều IM: 600mg mỗi 12 giờ."
            }
        },
        "references": {
            "primary_sources": [
                "FDA Drug Label - Clindamycin (Cleocin)",
                "UpToDate - Clindamycin: Drug Information",
                "Medscape - Clindamycin Drug Reference",
                "Goodman & Gilman's The Pharmacological Basis of Therapeutics (14th ed)",
                "Lexicomp Online - Clindamycin Monograph",
                "Micromedex - Clindamycin Drug Information",
                "IDSA Guidelines - Skin and Soft Tissue Infections, Anaerobic Infections"
            ],
            "last_updated": "2025-02-03",
            "evidence_level": "A - Dựa trên FDA drug labels, IDSA guidelines, và dữ liệu lâm sàng từ nhiều nguồn"
        }

},

"Trimethoprim-sulfamethoxazole": {
    "group": "Antibiotic - Sulfonamide",
    "vietnamese_name": "Trimethoprim-sulfamethoxazole, Bactrim, Septra, Cotrimoxazole",
    "administration": ["PO", "IV"],
    "indications": [
        "Nhiễm khuẩn đường tiết niệu",
        "Viêm phổi do Pneumocystis jirovecii (PJP)",
        "Nhiễm khuẩn do Toxoplasma",
        "Nhiễm khuẩn do MRSA",
        "Nhiễm khuẩn đường hô hấp"
    ],
    "contraindications": [
        "Dị ứng sulfonamide",
        "Suy thận nặng (CrCl <15)",
        "Suy gan nặng",
        "Thiếu máu do thiếu folate",
        "Có thai (gần sinh)"
    ],
    "dosage": {
        "adult_uti": "160/800mg (DS) x 2 lần/ngày",
        "adult_pjp": "160/800mg (DS) x 3-4 lần/ngày",
        "adult_pjp_iv": "15-20mg/kg (TMP) IV mỗi 6-8 giờ",
        "notes": "Tỷ lệ TMP:SMX = 1:5. Dùng với nhiều nước"
    },
    "renal_adjustment": {
        "normal": "Không đổi",
        "30_60": "Giảm liều 50%",
        "under_30": "Tránh dùng nếu CrCl <15"
    },
    "side_effects": [
        "Phát ban (thường gặp)",
        "Tăng kali máu",
        "Giảm bạch cầu",
        "Thiếu máu",
        "Tăng creatinine (giả, không phản ánh suy thận)",
        "Độc tính da (SJS/TEN - hiếm nhưng nguy hiểm)"
    ],
    "interactions": [
        "Warfarin: tăng tác dụng",
        "Phenytoin: tăng nồng độ phenytoin",
        "ACE inhibitor: tăng kali máu",
        "Methotrexate: tăng độc tính"
    ],
    "pregnancy": "C - D gần sinh",
    "mechanism_of_action": "Trimethoprim-sulfamethoxazole (TMP-SMX, cotrimoxazole) là kháng sinh kết hợp với tác dụng hiệp đồng (synergistic). Sulfamethoxazole (SMX) là sulfonamide ức chế tổng hợp acid folic ở vi khuẩn bằng cách ức chế enzyme dihydropteroate synthase, ngăn chặn tổng hợp dihydrofolic acid. Trimethoprim (TMP) ức chế enzyme dihydrofolate reductase, ngăn chặn chuyển đổi dihydrofolic acid thành tetrahydrofolic acid, một cofactor cần thiết cho tổng hợp DNA, RNA, và protein. Cả hai chất cùng ức chế con đường tổng hợp acid folic ở hai bước khác nhau, tạo ra tác dụng hiệp đồng mạnh. Tỷ lệ TMP:SMX = 1:5 (160mg TMP : 800mg SMX). Phổ kháng khuẩn: Gram-dương (một số Staphylococcus, Streptococcus), Gram-âm (Enterobacteriaceae, H. influenzae), và một số vi khuẩn không điển hình (Pneumocystis jirovecii, Toxoplasma gondii, Nocardia).",
    "monitoring": [
        "Dấu hiệu nhiễm trùng (sốt, WBC, triệu chứng lâm sàng) để đánh giá đáp ứng điều trị",
        "Cấy máu và cấy từ vị trí nhiễm trùng (nếu có) để xác định vi khuẩn và độ nhạy cảm",
        "Điện giải (natri, kali) - tăng kali máu (đặc biệt ở người cao tuổi, suy thận, dùng ACE inhibitor/ARB)",
        "Công thức máu (CBC) - giảm bạch cầu, thiếu máu, giảm tiểu cầu (do thiếu folate)",
        "Creatinine - tăng creatinine giả (do ức chế bài tiết creatinine ở ống thận, không phản ánh suy thận thực sự)",
        "Chức năng gan (ALT, AST) - hiếm viêm gan nặng",
        "Dấu hiệu phản ứng dị ứng (phát ban, sốt) - có thể tiến triển thành SJS/TEN",
        "Dấu hiệu SJS/TEN (Stevens-Johnson syndrome, toxic epidermal necrolysis) - phát ban, mụn nước, bong da",
        "Tương tác với warfarin (tăng INR), phenytoin (tăng nồng độ), methotrexate (tăng độc tính)"
    ],
    "precautions": [
        "Phản ứng dị ứng - nguy cơ cao với sulfonamide, đặc biệt SJS/TEN (hiếm nhưng nguy hiểm, có thể tử vong)",
        "NGỪNG NGAY nếu có phát ban, sốt, mụn nước, bong da - có thể là SJS/TEN",
        "Tăng kali máu - đặc biệt ở người cao tuổi, suy thận, dùng ACE inhibitor/ARB, trimethoprim",
        "Không dùng nếu CrCl <15 (tăng nguy cơ tác dụng phụ, không hiệu quả)",
        "Tăng creatinine giả - không phản ánh suy thận thực sự, do ức chế bài tiết creatinine",
        "Thiếu máu, giảm bạch cầu - do ức chế tổng hợp folate, đặc biệt ở bệnh nhân thiếu folate",
        "Không dùng gần sinh (trong 3 tháng cuối thai kỳ) - nguy cơ kernicterus ở trẻ sơ sinh",
        "Uống nhiều nước để tránh kết tinh trong nước tiểu (sulfamethoxazole)",
        "Tương tác với nhiều thuốc: warfarin (tăng INR), phenytoin (tăng nồng độ), methotrexate (tăng độc tính), ACE inhibitor/ARB (tăng kali)",
        "Thận trọng ở bệnh nhân suy gan (chuyển hóa qua gan)",
        "Dùng với thức ăn để giảm kích ứng dạ dày"
    ],
    "pharmacokinetics": {
        "half_life": "8-10 giờ (TMP), 10-12 giờ (SMX)",
        "onset": "2-4 giờ",
        "duration": "q12h (PO), q6-8h (IV cho PJP)",
        "protein_binding": "44% (TMP), 70% (SMX)",
        "clearance": "Gan: chuyển hóa một phần. Thận: bài tiết chủ yếu qua thận (TMP và SMX). Cần điều chỉnh liều ở suy thận (CrCl <30: giảm 50%, CrCl <15: tránh dùng)."
    },
    "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm, tránh ánh sáng. Viên nén: bảo quản trong bao bì kín. Dạng suspension: bảo quản ở nhiệt độ phòng, lắc kỹ trước khi dùng. IV: bảo quản trong tủ lạnh, để nhiệt độ phòng trước khi pha, dùng trong vòng 6 giờ sau khi pha.",
    "black_box_warnings": "Nguy cơ phản ứng dị ứng nghiêm trọng, bao gồm SJS/TEN, có thể gây tử vong. Nguy cơ tăng ở bệnh nhân có tiền sử dị ứng sulfonamide. Ngừng ngay nếu có phát ban, sốt, mụn nước, bong da.",
    "drug_interactions": {
        "major": [
            {
                "drug": "Warfarin",
                "mechanism": "Trimethoprim-sulfamethoxazole ức chế CYP2C9, làm giảm chuyển hóa warfarin. Sulfamethoxazole cũng có thể ức chế tổng hợp vitamin K.",
                "effect": "Tăng tác dụng chống đông, tăng INR, tăng nguy cơ chảy máu nghiêm trọng",
                "management": "Theo dõi INR chặt chẽ khi bắt đầu, thay đổi liều, hoặc ngừng trimethoprim-sulfamethoxazole. Giảm liều warfarin 25-50% khi bắt đầu trimethoprim-sulfamethoxazole. Điều chỉnh liều warfarin theo INR."
            },
            {
                "drug": "Phenytoin",
                "mechanism": "Trimethoprim-sulfamethoxazole ức chế CYP2C9, làm giảm chuyển hóa phenytoin.",
                "effect": "Tăng nồng độ phenytoin, tăng độc tính (chóng mặt, rung giật, ataxia, co giật)",
                "management": "Theo dõi nồng độ phenytoin. Giảm liều phenytoin khi bắt đầu trimethoprim-sulfamethoxazole. Theo dõi dấu hiệu độc tính phenytoin."
            },
            {
                "drug": "Methotrexate",
                "mechanism": "Trimethoprim-sulfamethoxazole ức chế tổng hợp folate, làm tăng độc tính methotrexate. Cũng ức chế bài tiết methotrexate ở ống thận.",
                "effect": "Tăng nồng độ methotrexate, tăng độc tính nghiêm trọng (giảm bạch cầu, thiếu máu, độc gan, độc thận, tử vong)",
                "management": "TRÁNH DÙNG đồng thời nếu có thể. Nếu bắt buộc, giảm liều methotrexate đáng kể, bổ sung folinic acid (leucovorin), theo dõi chặt chẽ công thức máu, chức năng gan, thận. Ngừng methotrexate nếu có dấu hiệu độc tính."
            }
        ],
        "moderate": [
            {
                "drug": "ACE inhibitor, ARB",
                "mechanism": "Trimethoprim ức chế bài tiết kali ở ống thận, làm tăng kali máu. ACE inhibitor/ARB cũng tăng kali máu.",
                "effect": "Tăng kali máu, tăng nguy cơ rối loạn nhịp tim, đặc biệt ở người cao tuổi, suy thận",
                "management": "Theo dõi kali máu chặt chẽ, đặc biệt ở người cao tuổi, suy thận. Giảm liều hoặc ngừng ACE inhibitor/ARB nếu kali tăng. Điều chỉnh liều trimethoprim-sulfamethoxazole nếu cần."
            },
            {
                "drug": "Digoxin",
                "mechanism": "Trimethoprim-sulfamethoxazole có thể ảnh hưởng đến hệ vi khuẩn đường ruột, làm tăng hấp thu digoxin.",
                "effect": "Tăng nồng độ digoxin, tăng độc tính (buồn nôn, nôn, rối loạn nhịp tim, block AV)",
                "management": "Theo dõi nồng độ digoxin và dấu hiệu độc tính. Giảm liều digoxin nếu cần. Theo dõi ECG."
            },
            {
                "drug": "Sulfonylurea (Glibenclamide, Gliclazide)",
                "mechanism": "Trimethoprim-sulfamethoxazole ức chế CYP2C9, làm giảm chuyển hóa sulfonylurea.",
                "effect": "Tăng nồng độ sulfonylurea, tăng nguy cơ hạ đường huyết",
                "management": "Theo dõi đường huyết chặt chẽ. Giảm liều sulfonylurea khi bắt đầu trimethoprim-sulfamethoxazole. Điều chỉnh liều theo đường huyết."
            }
        ],
        "minor": [
            {
                "drug": "Cyclosporine",
                "mechanism": "Trimethoprim-sulfamethoxazole có thể ảnh hưởng đến chuyển hóa cyclosporine.",
                "effect": "Tăng nhẹ nồng độ cyclosporine",
                "management": "Theo dõi nồng độ cyclosporine. Không cần điều chỉnh liều thường quy."
            }
        ]
    },
    "contraindications": {
        "absolute": [
            "Dị ứng trimethoprim, sulfamethoxazole, hoặc các sulfonamide khác - phản ứng chéo cao",
            "Suy thận nặng (CrCl <15) - tăng nguy cơ tác dụng phụ, không hiệu quả",
            "Suy gan nặng - tăng nguy cơ độc tính",
            "Thiếu máu do thiếu folate - tăng nguy cơ thiếu máu nặng, giảm bạch cầu",
            "Có thai (gần sinh, 3 tháng cuối) - nguy cơ kernicterus ở trẻ sơ sinh",
            "Tiền sử SJS/TEN do sulfonamide - nguy cơ tái phát cao, có thể tử vong"
        ],
        "relative": [
            "Dị ứng sulfonamide nhẹ - thận trọng, có thể dùng nếu cần thiết nhưng theo dõi chặt chẽ",
            "Suy thận (CrCl 15-30) - cần giảm liều 50%, theo dõi chặt chẽ",
            "Suy gan - thận trọng, có thể giảm chuyển hóa",
            "Thiếu folate - bổ sung folate trước và trong khi dùng",
            "Người cao tuổi - tăng nguy cơ tăng kali máu, tác dụng phụ",
            "Dùng với ACE inhibitor/ARB - tăng nguy cơ tăng kali máu",
            "Dùng với warfarin - tăng nguy cơ chảy máu",
            "Dùng với phenytoin - tăng độc tính phenytoin",
            "Dùng với methotrexate - tăng độc tính methotrexate nghiêm trọng",
            "Có thai (tam cá nguyệt 1-2) - thận trọng, chỉ dùng khi thực sự cần thiết"
        ]
    },
    "pregnancy_lactation": {
        "fda_category": "C (tam cá nguyệt 1-2), D (tam cá nguyệt 3)",
        "pregnancy_details": "Tam cá nguyệt 1-2: Thuốc phân loại C - thận trọng. Các nghiên cứu trên động vật cho thấy một số nguy cơ. Các nghiên cứu trên người không cho thấy nguy cơ tăng dị tật bẩm sinh rõ ràng, nhưng dữ liệu còn hạn chế. Có thể dùng khi lợi ích vượt quá nguy cơ, đặc biệt trong điều trị PJP hoặc nhiễm trùng nặng. Tam cá nguyệt 3 (gần sinh): Thuốc phân loại D - CHỐNG CHỈ ĐỊNH. Sulfamethoxazole có thể gây kernicterus ở trẻ sơ sinh (vàng da nặng, tổn thương não). Không dùng trong 3 tháng cuối thai kỳ. Nếu cần điều trị, dùng thuốc khác hoặc trì hoãn đến sau sinh.",
        "lactation": {
            "safety": "Compatible with Caution",
            "details": "Trimethoprim và sulfamethoxazole bài tiết vào sữa mẹ ở nồng độ thấp. Nồng độ trong sữa mẹ thấp và không có báo cáo về tác dụng phụ đáng kể ở trẻ bú mẹ. Tuy nhiên, sulfonamide có thể gây vàng da ở trẻ sơ sinh thiếu tháng hoặc có bệnh gan. Thận trọng ở trẻ sơ sinh < 1 tháng tuổi hoặc thiếu tháng.",
            "recommendation": "Có thể dùng khi cho con bú, nhưng thận trọng ở trẻ sơ sinh < 1 tháng tuổi hoặc thiếu tháng. Dùng liều thấp nhất hiệu quả. Theo dõi trẻ sơ sinh nếu dùng liều cao hoặc kéo dài (vàng da, tiêu chảy, phát ban)."
        }
    },
    "hepatic_adjustment": {
        "mild": "Không cần điều chỉnh liều. Trimethoprim và sulfamethoxazole chuyển hóa một phần qua gan nhưng không đáng kể.",
        "moderate": "Thận trọng, có thể cần giảm liều nhẹ. Chuyển hóa có thể giảm ở suy gan trung bình, tăng nồng độ và nguy cơ tác dụng phụ.",
        "severe": "CHỐNG CHỈ ĐỊNH hoặc thận trọng tối đa. Chuyển hóa có thể giảm đáng kể ở suy gan nặng, tăng nồng độ và nguy cơ độc tính gan nghiêm trọng. Không dùng nếu suy gan nặng.",
        "notes": "Trimethoprim và sulfamethoxazole chuyển hóa một phần qua gan nhưng thải trừ chủ yếu qua thận. Suy gan có thể giảm chuyển hóa, tăng nồng độ và nguy cơ độc tính gan. Tuy nhiên, suy gan nặng là chống chỉ định do nguy cơ độc tính gan nghiêm trọng. Theo dõi chặt chẽ chức năng gan ở suy gan trung bình."
    },
    "overdose_management": {
        "symptoms": [
            "Triệu chứng tiêu hóa: Buồn nôn, nôn, tiêu chảy, đau bụng",
            "Triệu chứng thần kinh: Đau đầu, chóng mặt, lú lẫn, co giật (hiếm)",
            "Triệu chứng huyết học: Thiếu máu, giảm bạch cầu, giảm tiểu cầu (do thiếu folate)",
            "Triệu chứng thận: Tăng creatinine (giả), suy thận cấp (hiếm)",
            "Triệu chứng điện giải: Tăng kali máu (đặc biệt với trimethoprim)",
            "Triệu chứng da: Phát ban, mày đay, SJS/TEN (hiếm nhưng nghiêm trọng, có thể tử vong)",
            "Triệu chứng gan: Tăng men gan, viêm gan (hiếm nhưng nghiêm trọng)",
            "Triệu chứng nghiêm trọng: SJS/TEN, suy thận cấp, viêm gan nặng, thiếu máu nặng"
        ],
        "antidote": "Không có antidote đặc hiệu. Điều trị hỗ trợ và điều trị triệu chứng. Bổ sung folinic acid (leucovorin) nếu có thiếu máu do thiếu folate.",
        "treatment": [
            "Ngừng ngay trimethoprim-sulfamethoxazole",
            "Rửa dạ dày hoặc than hoạt nếu uống trong vòng 1-2 giờ (nếu không có chống chỉ định)",
            "Theo dõi dấu hiệu sinh tồn: Huyết áp, nhịp tim, nhịp thở, SpO2",
            "Điều trị triệu chứng tiêu hóa:",
            "  - Chống nôn nếu cần",
            "  - Truyền dịch nếu mất nước",
            "  - Theo dõi điện giải",
            "Điều trị tăng kali máu nếu có:",
            "  - Theo dõi kali máu",
            "  - Điều trị tăng kali máu: Calcium gluconate, insulin + glucose, sodium bicarbonate, kayexalate",
            "  - Lọc máu nếu cần",
            "Điều trị thiếu máu/giảm bạch cầu nếu có:",
            "  - Bổ sung folinic acid (leucovorin) 5-15mg/ngày",
            "  - Theo dõi công thức máu",
            "  - Truyền máu nếu cần",
            "Điều trị tăng creatinine (giả) nếu có:",
            "  - Theo dõi creatinine, BUN, lượng nước tiểu",
            "  - Điều trị suy thận cấp nếu có",
            "Điều trị SJS/TEN nếu có:",
            "  - CHUYỂN NGAY khoa da liễu/bỏng",
            "  - Điều trị hỗ trợ (truyền dịch, dinh dưỡng, chăm sóc vết thương)",
            "  - Kháng sinh nếu có nhiễm trùng",
            "  - Corticosteroid (còn tranh cãi)",
            "Điều trị tăng men gan/viêm gan nếu có:",
            "  - Theo dõi ALT, AST, bilirubin",
            "  - Điều trị hỗ trợ gan",
            "  - Nếu viêm gan nặng: điều trị suy gan",
            "Theo dõi dấu hiệu sinh tồn: Huyết áp, nhịp tim, nhịp thở, SpO2"
        ],
        "monitoring": "Theo dõi dấu hiệu sinh tồn, công thức máu (CBC), điện giải (natri, kali), chức năng thận (creatinine, BUN, lượng nước tiểu), chức năng gan (ALT, AST, bilirubin), dấu hiệu da (SJS/TEN) trong ít nhất 24-48 giờ. Theo dõi lâu hơn nếu có biến chứng (SJS/TEN, suy thận, viêm gan, thiếu máu)."
    },
    "reversal_agents": None,
    "administration_instructions": {
        "oral": {
            "with_food": "Uống với thức ăn để giảm kích ứng dạ dày. Có thể uống không thức ăn nếu cần nhưng không khuyến nghị.",
            "timing": "Uống 2 lần/ngày (q12h) cho UTI, 3-4 lần/ngày (q6-8h) cho PJP. Uống đều đặn, cách đều nhau trong ngày. Không bỏ liều. Uống nhiều nước để tránh kết tinh trong nước tiểu."
        },
        "iv": {
            "reconstitution": "Pha theo hướng dẫn nhà sản xuất. Thường pha với D5W hoặc NaCl 0.9%. Lắc kỹ để hòa tan hoàn toàn. Dùng trong vòng 6 giờ sau khi pha.",
            "infusion_rate": "Truyền IV trong 60-90 phút (không truyền nhanh hơn). Có thể truyền trong 30-60 phút nếu cần nhưng không khuyến nghị.",
            "compatibility": [
                "D5W (Dextrose 5%)",
                "NaCl 0.9%",
                "Nước cất vô trùng"
            ],
            "incompatibility": [
                "Không trộn với các thuốc khác trong cùng một bơm tiêm hoặc chai truyền",
                "Lactated Ringer's (LR) - không tương thích",
                "Các dung dịch có cation (Al3+, Mg2+, Ca2+) - có thể tạo phức hợp"
            ],
            "notes": "Truyền IV trong 60-90 phút. Không truyền nhanh hơn. Theo dõi phản ứng tại chỗ tiêm (viêm tĩnh mạch). Dùng trong vòng 6 giờ sau khi pha. Không bảo quản lâu sau khi pha."
        }
    },
    "references": {
        "primary_sources": [
            "FDA Label: Bactrim, Septra (trimethoprim-sulfamethoxazole)",
            "UpToDate: Trimethoprim-sulfamethoxazole drug information",
            "Lexicomp: Trimethoprim-sulfamethoxazole monograph",
            "Goodman & Gilman's The Pharmacological Basis of Therapeutics",
            "Sanford Guide to Antimicrobial Therapy"
        ],
        "last_updated": "2025-02-03",
        "evidence_level": "Level 1 - FDA approved, multiple clinical trials, extensive clinical experience"
    }
},

"Levofloxacin": {
    "group": "Antibiotic - Fluoroquinolone",
    "vietnamese_name": "Levofloxacin, Tavanic",
    "administration": ["PO", "IV"],
    "indications": [
        "Viêm phổi cộng đồng",
        "Nhiễm khuẩn đường tiết niệu phức tạp",
        "Nhiễm khuẩn da và mô mềm",
        "Viêm xoang",
        "Viêm tuyến tiền liệt do vi khuẩn"
    ],
    "contraindications": [
        "Dị ứng fluoroquinolone",
        "Trẻ em <18 tuổi (trừ trường hợp đặc biệt)",
        "Có thai"
    ],
    "dosage": {
        "adult_po": "500-750mg x 1 lần/ngày",
        "adult_iv": "500-750mg IV x 1 lần/ngày",
        "adult_pneumonia": "500-750mg x 1 lần/ngày x 7-14 ngày",
        "notes": "Uống với nhiều nước. Tránh antacid, sắt trong 2 giờ"
    },
    "renal_adjustment": {
        "normal": "Không đổi",
        "30_60": "Giảm liều 50%",
        "under_30": "250-500mg x 1 lần/ngày"
    },
    "side_effects": [
        "Rối loạn tiêu hóa",
        "Nhức đầu",
        "Rối loạn giấc ngủ",
        "Rối loạn gân (viêm gân, đứt gân)",
        "QT kéo dài",
        "Hạ đường huyết (hiếm)"
    ],
    "interactions": [
        "Antacid/Sắt: giảm hấp thu",
        "Warfarin: tăng nguy cơ chảy máu",
        "Corticosteroid: tăng nguy cơ đứt gân"
    ],
    "pregnancy": "C",
    "mechanism_of_action": "Levofloxacin là fluoroquinolone kháng sinh phổ rộng, là enantiomer L của ofloxacin. Ức chế DNA gyrase (ở vi khuẩn Gram-âm) và topoisomerase IV (ở vi khuẩn Gram-dương), enzyme cần thiết cho sao chép và sửa chữa DNA. Dẫn đến tổn thương DNA và chết tế bào vi khuẩn. Phổ kháng khuẩn: Gram-âm mạnh (Enterobacteriaceae, H. influenzae, Neisseria), một số Gram-dương (Streptococcus pneumoniae - kể cả penicillin-resistant), và vi khuẩn không điển hình (Legionella, Mycoplasma, Chlamydia). Ưu điểm: dùng 1 lần/ngày (half-life dài hơn ciprofloxacin), tác dụng tốt với viêm phổi",
    "monitoring": [
        "Dấu hiệu nhiễm trùng (sốt, WBC, triệu chứng lâm sàng)",
        "Cấy máu và cấy từ vị trí nhiễm trùng",
        "Tendon (gân) - đau, sưng, đứt gân (đặc biệt gân Achilles) - có thể xảy ra bất cứ lúc nào",
        "Thần kinh trung ương (mất ngủ, lo âu, kích động, co giật)",
        "Tim mạch (QT kéo dài, rối loạn nhịp tim) - ECG nếu có yếu tố nguy cơ",
        "Đường huyết (tăng hoặc hạ đường huyết - đặc biệt với sulfonylurea)",
        "Chức năng thận (creatinine) - điều chỉnh liều ở suy thận",
        "Chức năng gan (ALT, AST) - hiếm viêm gan nặng"
    ],
    "precautions": [
        "NGỪNG NGAY nếu có đau, sưng gân (nguy cơ đứt gân, đặc biệt gân Achilles)",
        "Nguy cơ đứt gân tăng ở: > 60 tuổi, dùng corticosteroid, ghép tạng, hoạt động thể lực",
        "QT kéo dài → không dùng với các thuốc kéo dài QT khác, bệnh nhân có tiền sử rối loạn nhịp",
        "Co giật → không dùng ở bệnh nhân có tiền sử co giật, tránh dùng với NSAID",
        "Tăng độ nhạy cảm với ánh sáng → tránh ánh nắng trực tiếp, dùng kem chống nắng",
        "Tương tác với nhiều thuốc: giảm hấp thu với antacid, sucralfate, sắt, kẽm (cách 2 giờ)",
        "Hạ đường huyết → thận trọng với sulfonylurea",
        "Không dùng cho trẻ em < 18 tuổi (trừ trường hợp đặc biệt) - nguy cơ tổn thương sụn",
        "Điều chỉnh liều khi suy thận (giảm liều khi CrCl <50)",
        "Uống nhiều nước để tránh kết tinh trong nước tiểu",
        "Ưu điểm: dùng 1 lần/ngày (compliance tốt hơn ciprofloxacin)"
    ],
    "pharmacokinetics": {
        "half_life": "6-8 giờ (dài hơn ciprofloxacin)",
        "onset": "1-2 giờ (PO), ngay lập tức (IV)",
        "duration": "q24h (1 lần/ngày)",
        "protein_binding": "24-38%",
        "clearance": "Thận (chủ yếu, 80-90% thải nguyên dạng qua nước tiểu), gan (chuyển hóa ít)"
    },
    "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm, tránh ánh sáng. Dung dịch IV: bảo quản theo hướng dẫn nhà sản xuất",
    "black_box_warnings": "Nguy cơ đứt gân, viêm gân (đặc biệt gân Achilles) - có thể xảy ra bất cứ lúc nào, kể cả sau khi ngừng thuốc. Ngừng ngay nếu có đau, sưng gân. Nguy cơ tăng ở > 60 tuổi, dùng corticosteroid, ghép tạng. QT kéo dài có thể gây rối loạn nhịp tim nghiêm trọng",
    "drug_interactions": {
        "major": [
            {
                "drug": "Antacids (Aluminum, Magnesium), Sucralfate, Sắt, Kẽm",
                "mechanism": "Cation (Al3+, Mg2+, Fe2+, Zn2+) tạo phức hợp không hòa tan với levofloxacin, giảm hấp thu.",
                "effect": "Giảm hấp thu levofloxacin, giảm nồng độ trong máu, giảm hiệu quả điều trị",
                "management": "Cách ít nhất 2 giờ (tốt nhất 4 giờ) trước hoặc sau khi uống levofloxacin. Không uống cùng lúc."
            },
            {
                "drug": "Warfarin",
                "mechanism": "Levofloxacin có thể ảnh hưởng đến chuyển hóa warfarin.",
                "effect": "Tăng tác dụng chống đông, tăng INR, tăng nguy cơ chảy máu",
                "management": "Theo dõi INR chặt chẽ khi bắt đầu, thay đổi liều, hoặc ngừng levofloxacin. Điều chỉnh liều warfarin nếu cần."
            }
        ],
        "moderate": [
            {
                "drug": "Corticosteroid",
                "mechanism": "Cả hai đều tăng nguy cơ đứt gân, tác dụng cộng dồn.",
                "effect": "Tăng nguy cơ viêm gân, đứt gân",
                "management": "TRÁNH DÙNG đồng thời nếu có thể. Nếu bắt buộc, theo dõi chặt chẽ dấu hiệu đau, sưng gân. Ngừng ngay nếu có đau gân."
            },
            {
                "drug": "NSAID",
                "mechanism": "Cả hai đều có thể gây co giật, tác dụng cộng dồn.",
                "effect": "Tăng nguy cơ co giật",
                "management": "Tránh dùng đồng thời nếu có thể. Thận trọng ở bệnh nhân có tiền sử co giật."
            },
            {
                "drug": "Sulfonylurea",
                "mechanism": "Levofloxacin có thể gây hạ đường huyết.",
                "effect": "Tăng nguy cơ hạ đường huyết",
                "management": "Theo dõi đường huyết. Điều chỉnh liều sulfonylurea nếu cần."
            }
        ],
        "minor": []
    },
    "contraindications": {
        "absolute": [
            "Dị ứng levofloxacin hoặc các fluoroquinolone khác",
            "Có thai - chống chỉ định tuyệt đối, nguy cơ tổn thương sụn thai nhi",
            "Trẻ em < 18 tuổi (trừ trường hợp đặc biệt) - nguy cơ tổn thương sụn, viêm khớp",
            "QT kéo dài hoặc rối loạn nhịp tim nặng - tăng nguy cơ loạn nhịp tim nghiêm trọng"
        ],
        "relative": [
            "Bệnh nhân > 60 tuổi - tăng nguy cơ đứt gân, viêm gân",
            "Dùng corticosteroid - tăng nguy cơ đứt gân",
            "Ghép cơ quan - tăng nguy cơ đứt gân",
            "Tiền sử co giật - tăng nguy cơ co giật",
            "Suy thận nặng (CrCl <30) - giảm liều đáng kể",
            "Dùng với warfarin - tăng nguy cơ chảy máu",
            "Hoạt động thể lực nặng - tăng nguy cơ đứt gân"
        ]
    },
    "pregnancy_lactation": {
        "fda_category": "C",
        "pregnancy_details": "Levofloxacin là thuốc phân loại C. Các nghiên cứu trên động vật cho thấy có thể gây tổn thương sụn ở khớp ở thai nhi. Có báo cáo về tổn thương sụn ở trẻ em khi dùng trong thai kỳ. CHỐNG CHỈ ĐỊNH trong thai kỳ trừ khi lợi ích vượt quá nguy cơ rõ ràng và không có lựa chọn khác. Nhiễm trùng nặng có thể gây nguy hiểm cho thai nhi, nhưng nên dùng kháng sinh khác nếu có thể.",
        "lactation": {
            "safety": "Compatible (với thận trọng)",
            "details": "Levofloxacin bài tiết vào sữa mẹ ở nồng độ thấp. Nồng độ trong sữa mẹ thấp và không có báo cáo về tác dụng phụ đáng kể ở trẻ bú mẹ. Tuy nhiên, fluoroquinolone có thể gây tổn thương sụn ở trẻ sơ sinh.",
            "recommendation": "Có thể dùng khi cho con bú với thận trọng. Dùng liều thấp nhất hiệu quả. Theo dõi trẻ sơ sinh. Tránh dùng nếu có lựa chọn khác."
        }
    },
    "hepatic_adjustment": {
        "mild": "Không cần điều chỉnh liều. Levofloxacin chuyển hóa ít qua gan, thải trừ chủ yếu qua thận.",
        "moderate": "Không cần điều chỉnh liều. Thận trọng nếu có suy thận kèm theo.",
        "severe": "Thận trọng, có thể cần giảm liều nhẹ. Chuyển hóa có thể giảm ở suy gan nặng, nhưng thải trừ chủ yếu qua thận nên ít ảnh hưởng.",
        "notes": "Levofloxacin chuyển hóa ít qua gan, thải trừ chủ yếu qua thận (80-90% nguyên dạng). Suy gan có thể giảm chuyển hóa nhẹ nhưng không đáng kể. Tuy nhiên, suy gan có thể kèm theo suy thận, nên cần điều chỉnh liều theo chức năng thận."
    },
    "overdose_management": {
        "symptoms": [
            "Triệu chứng tiêu hóa: Buồn nôn, nôn, tiêu chảy, đau bụng",
            "Triệu chứng thần kinh: Co giật, kích động, lo âu, mất ngủ, trầm cảm, rối loạn tâm thần",
            "Triệu chứng gân: Đau gân, viêm gân, đứt gân (đặc biệt gân Achilles)",
            "Triệu chứng tim mạch: QT kéo dài, rối loạn nhịp tim, có thể gây tử vong",
            "Triệu chứng chuyển hóa: Hạ hoặc tăng đường huyết",
            "Triệu chứng nghiêm trọng: Rối loạn nhịp tim nghiêm trọng, đứt gân"
        ],
        "antidote": "Không có antidote đặc hiệu. Điều trị hỗ trợ và điều trị triệu chứng.",
        "treatment": [
            "Ngừng ngay levofloxacin",
            "Rửa dạ dày hoặc than hoạt nếu uống trong vòng 1-2 giờ (nếu không có chống chỉ định)",
            "Theo dõi dấu hiệu sinh tồn: Huyết áp, nhịp tim, nhịp thở, SpO2, ECG",
            "Điều trị co giật nếu có: Benzodiazepine, theo dõi thần kinh chặt chẽ",
            "Điều trị rối loạn nhịp tim nếu có: Theo dõi ECG liên tục, điều trị loạn nhịp nếu cần",
            "Điều trị đau gân nếu có: Ngừng ngay, nghỉ ngơi, chườm lạnh, thuốc giảm đau nếu cần",
            "Điều trị hạ đường huyết nếu có: Truyền glucose, theo dõi đường huyết",
            "Điều trị triệu chứng tiêu hóa: Chống nôn nếu cần, truyền dịch nếu mất nước"
        ],
        "monitoring": "Theo dõi dấu hiệu sinh tồn, ECG, dấu hiệu thần kinh, dấu hiệu gân, đường huyết trong ít nhất 24-48 giờ. Theo dõi lâu hơn nếu có biến chứng."
    },
    "reversal_agents": None,
    "administration_instructions": {
        "oral": {
            "with_food": "Có thể uống với hoặc không thức ăn. Uống với nước đầy đủ (ít nhất 1-2 ly nước) để tránh kết tinh trong nước tiểu.",
            "timing": "Uống 1 lần/ngày (q24h), cùng một thời điểm mỗi ngày. Cách ít nhất 2 giờ (tốt nhất 4 giờ) trước hoặc sau khi uống antacid, sucralfate, sắt, kẽm. Không uống cùng lúc với các cation này. Ưu điểm: dùng 1 lần/ngày, compliance tốt hơn ciprofloxacin."
        },
        "iv": {
            "reconstitution": "Pha với NS hoặc D5W. Nồng độ pha: 5mg/ml (tối đa). Pha 500mg trong 100ml dịch = 5mg/ml. Pha 750mg trong 150ml dịch = 5mg/ml.",
            "infusion_rate": "Truyền trong 60 phút (ít nhất 60 phút). Không truyền quá nhanh. Tốc độ: 100ml/60 phút = ~1.7ml/phút. 150ml/60 phút = ~2.5ml/phút.",
            "compatibility": ["NS (0.9% NaCl)", "D5W (5% Dextrose)"],
            "incompatibility": ["Không trộn với các thuốc khác trong cùng một ống truyền. Kiểm tra tương thích trước khi pha. Tránh pha với cation (Al3+, Mg2+, Ca2+)."],
            "notes": "Theo dõi chức năng thận, dấu hiệu gân, thần kinh trong quá trình truyền. Có thể gây kích ứng tĩnh mạch - thay đổi vị trí tiêm nếu cần. Liều: 500-750mg x 1 lần/ngày (q24h)."
        }
    },
    "references": {
        "primary_sources": [
            "FDA Drug Label - Levofloxacin (Tavanic)",
            "UpToDate - Levofloxacin: Drug Information",
            "Medscape - Levofloxacin Drug Reference",
            "Goodman & Gilman's The Pharmacological Basis of Therapeutics (14th ed)",
            "Lexicomp Online - Levofloxacin Monograph",
            "Micromedex - Levofloxacin Drug Information",
            "IDSA Guidelines - Antimicrobial Therapy"
        ],
        "last_updated": "2024-12-19",
        "evidence_level": "A - Dựa trên FDA drug labels, IDSA guidelines, và dữ liệu lâm sàng từ nhiều nguồn"
    }
}
}

__all__ = ['ANTIMICROBIAL_DRUGS']
