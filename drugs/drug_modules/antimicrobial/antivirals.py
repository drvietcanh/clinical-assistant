"""
Antivirals - Antiviral Medications
"""

ANTIVIRALS = {
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
        "black_box_warnings": None,
        "drug_interactions": {
            "major": [],
            "moderate": [
                {
                    "drug": "Probenecid",
                    "mechanism": "Probenecid ức chế bài tiết oseltamivir carboxylate qua thận, tăng nồng độ oseltamivir.",
                    "effect": "Tăng nồng độ oseltamivir carboxylate, tăng tác dụng và tác dụng phụ",
                    "management": "Thận trọng. Có thể cần giảm liều oseltamivir khi dùng với probenecid. Theo dõi tác dụng phụ."
                }
            ],
            "minor": []
        },
        "contraindications": {
            "tuyệt_đối": [
                "Dị ứng oseltamivir hoặc các thành phần khác"
            ],
            "tương_đối": [
                "Suy thận nặng (CrCl <30) - cần điều chỉnh liều nghiêm ngặt",
                "Có thai - category C, thận trọng",
                "Trẻ em <1 tuổi - không khuyến cáo"
            ]
        },
        "pregnancy_lactation": {
            "fda_category": "C",
            "pregnancy_details": "Oseltamivir là category C. Không có nghiên cứu đầy đủ ở phụ nữ có thai. Dùng được nếu lợi ích > nguy cơ. Cúm trong thai kỳ có thể gây biến chứng nghiêm trọng (viêm phổi, suy hô hấp, tử vong). Oseltamivir được khuyến cáo để điều trị cúm trong thai kỳ nếu có chỉ định.",
            "lactation": {
                "safety": "Compatible",
                "details": "Oseltamivir và oseltamivir carboxylate bài tiết vào sữa mẹ ở nồng độ thấp. Nồng độ trong sữa mẹ thấp và không có báo cáo về tác dụng phụ đáng kể ở trẻ bú mẹ.",
                "recommendation": "Có thể dùng khi cho con bú. Theo dõi trẻ sơ sinh nếu có dấu hiệu bất thường (hiếm)."
            }
        },
        "hepatic_adjustment": {
            "mild": "Không cần điều chỉnh liều. Oseltamivir chuyển hóa ở gan thành oseltamivir carboxylate, nhưng suy gan nhẹ không ảnh hưởng đáng kể.",
            "moderate": "Không cần điều chỉnh liều thường quy. Theo dõi tác dụng phụ. Chuyển hóa có thể giảm nhẹ ở suy gan trung bình.",
            "severe": "Thận trọng, theo dõi tác dụng phụ. Chuyển hóa có thể giảm ở suy gan nặng, nhưng thường không cần điều chỉnh liều.",
            "notes": "Oseltamivir chuyển hóa ở gan thành oseltamivir carboxylate (chất hoạt động) qua esterase. Suy gan có thể làm giảm chuyển hóa, nhưng thường không ảnh hưởng đáng kể đến nồng độ oseltamivir carboxylate."
        },
        "overdose_management": {
            "symptoms": [
                "Buồn nôn, nôn (tăng so với liều điều trị)",
                "Đau đầu",
                "Tiêu chảy",
                "Rối loạn tâm thần (hiếm)",
                "Co giật (hiếm)"
            ],
            "antidote": "Không có antidote đặc hiệu. Điều trị hỗ trợ.",
            "treatment": [
                "Ngừng oseltamivir nếu có thể",
                "Rửa dạ dày nếu uống trong vòng 1-2 giờ",
                "Than hoạt tính nếu uống trong vòng 1-2 giờ",
                "Theo dõi dấu hiệu sinh tồn",
                "Điều trị hỗ trợ: truyền dịch nếu cần, điều trị triệu chứng",
                "Theo dõi ít nhất 4-6 giờ"
            ],
            "monitoring": "Dấu hiệu sinh tồn, dấu hiệu rối loạn tâm thần, co giật"
        },
        "reversal_agents": {
            "available": False,
            "agents": []
        },
        "administration_instructions": {
            "oral": {
                "with_food": "Nên uống với thức ăn để giảm buồn nôn, nôn. Có thể uống với hoặc không thức ăn, nhưng uống với thức ăn giúp giảm tác dụng phụ.",
                "timing": "Uống 2 lần/ngày (treatment) hoặc 1 lần/ngày (prophylaxis). Uống cùng thời điểm mỗi ngày để dễ nhớ. Điều chỉnh liều ở suy thận: CrCl 30-60: 75mg x 1 lần/ngày (treatment), 75mg cách ngày (prophylaxis); CrCl <30: 75mg x 1 lần/ngày (treatment), 75mg cách 2 ngày (prophylaxis)."
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
                "FDA Drug Label - Oseltamivir (Tamiflu)",
                "CDC Guidelines - Influenza Antiviral Medications",
                "WHO Guidelines - Antiviral Treatment for Influenza",
                "UpToDate - Oseltamivir: Drug Information",
                "Goodman & Gilman's The Pharmacological Basis of Therapeutics (14th ed)"
            ],
            "last_updated": "2025-02-04",
            "evidence_level": "A - Dựa trên FDA drug labels, CDC/WHO guidelines, và dữ liệu lâm sàng"
        }
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
        "black_box_warnings": "RẤT ĐỘC với tủy xương - giảm bạch cầu, tiểu cầu, hồng cầu nghiêm trọng phổ biến. CHỐNG CHỈ ĐỊNH nếu bạch cầu <500/mm³ hoặc tiểu cầu <25,000/mm³. Theo dõi CBC 2-3 lần/tuần khi dùng IV. CHỐNG CHỈ ĐỊNH trong thai kỳ - gây dị tật thai nhi, ung thư ở động vật (category D với CMV). Chỉ dùng khi thực sự cần thiết. Nguy cơ độc thần kinh (lú lẫn, co giật, ảo giác).",
        "drug_interactions": {
            "major": [
                {
                    "drug": "Zidovudine (AZT)",
                    "mechanism": "Cả hai đều độc với tủy xương, tác dụng cộng dồn.",
                    "effect": "Tăng độc tính tủy xương nghiêm trọng, tăng nguy cơ giảm bạch cầu, tiểu cầu, hồng cầu",
                    "management": "TRÁNH dùng đồng thời nếu có thể. Nếu phải dùng, theo dõi CBC chặt chẽ (2-3 lần/tuần). Có thể cần giảm liều hoặc ngừng một trong hai thuốc."
                }
            ],
            "moderate": [
                {
                    "drug": "Probenecid",
                    "mechanism": "Probenecid ức chế bài tiết ganciclovir qua thận, tăng nồng độ ganciclovir.",
                    "effect": "Tăng nồng độ ganciclovir, tăng độc tính",
                    "management": "Thận trọng. Có thể cần giảm liều ganciclovir. Theo dõi CBC và chức năng thận chặt chẽ."
                },
                {
                    "drug": "Mycophenolate mofetil",
                    "mechanism": "Mycophenolate ức chế bài tiết ganciclovir qua thận, tăng nồng độ ganciclovir.",
                    "effect": "Tăng nồng độ ganciclovir, tăng độc tính",
                    "management": "Thận trọng. Có thể cần giảm liều ganciclovir. Theo dõi CBC và chức năng thận chặt chẽ."
                },
                {
                    "drug": "Imipenem-cilastatin",
                    "mechanism": "Có thể tăng nguy cơ co giật khi dùng với ganciclovir.",
                    "effect": "Tăng nguy cơ co giật",
                    "management": "Thận trọng. Tránh dùng đồng thời nếu có thể. Theo dõi dấu hiệu co giật."
                }
            ],
            "minor": [
                {
                    "drug": "Didanosine",
                    "mechanism": "Có thể tăng độc tính tủy xương.",
                    "effect": "Tăng độc tính tủy xương",
                    "management": "Thận trọng. Theo dõi CBC chặt chẽ."
                }
            ]
        },
        "contraindications": {
            "tuyệt_đối": [
                "Dị ứng ganciclovir",
                "Bạch cầu <500/mm³ - chống chỉ định tuyệt đối",
                "Tiểu cầu <25,000/mm³ - chống chỉ định tuyệt đối",
                "Có thai - chống chỉ định tuyệt đối (category D với CMV, gây dị tật thai nhi, ung thư ở động vật)"
            ],
            "tương_đối": [
                "Suy thận nặng (CrCl <25) - cần điều chỉnh liều nghiêm ngặt (giảm 90%)",
                "Suy thận (CrCl 25-50) - cần điều chỉnh liều (giảm 75%)",
                "Suy thận (CrCl 50-80) - cần điều chỉnh liều (giảm 50%)",
                "Giảm bạch cầu, tiểu cầu, hồng cầu - thận trọng, theo dõi chặt chẽ",
                "Độc thần kinh (tiền sử) - thận trọng",
                "Độc thận (tiền sử) - thận trọng, theo dõi chức năng thận"
            ]
        },
        "pregnancy_lactation": {
            "fda_category": "C - D (với CMV)",
            "pregnancy_details": "Ganciclovir là category C (thường) hoặc D (với CMV). CHỐNG CHỈ ĐỊNH trong thai kỳ. Ganciclovir gây dị tật thai nhi, ung thư, và các tác dụng phụ nghiêm trọng khác ở động vật. Không có dữ liệu an toàn ở phụ nữ có thai. Phụ nữ trong độ tuổi sinh đẻ phải dùng biện pháp tránh thai hiệu quả trong và sau khi dùng ganciclovir (ít nhất 30 ngày sau khi ngừng).",
            "lactation": {
                "safety": "Contraindicated",
                "details": "Ganciclovir bài tiết vào sữa mẹ. Không có dữ liệu an toàn ở trẻ bú mẹ. Ganciclovir có thể gây độc tính nghiêm trọng ở trẻ sơ sinh.",
                "recommendation": "KHÔNG dùng khi cho con bú. Ngừng cho con bú hoặc ngừng ganciclovir. Nếu phải dùng ganciclovir, không cho con bú."
            }
        },
        "hepatic_adjustment": {
            "mild": "Không cần điều chỉnh liều. Ganciclovir chủ yếu thải trừ qua thận, không chuyển hóa ở gan.",
            "moderate": "Không cần điều chỉnh liều. Ganciclovir chủ yếu thải trừ qua thận, không chuyển hóa ở gan.",
            "severe": "Không cần điều chỉnh liều. Ganciclovir chủ yếu thải trừ qua thận, không chuyển hóa ở gan. Tuy nhiên, suy gan nặng có thể ảnh hưởng đến protein binding (nhưng ganciclovir không gắn protein đáng kể).",
            "notes": "Ganciclovir chủ yếu thải trừ qua thận (90% nguyên dạng, không chuyển hóa ở gan). Suy gan không ảnh hưởng đáng kể đến nồng độ ganciclovir. Tuy nhiên, suy gan có thể ảnh hưởng đến chức năng thận, gián tiếp ảnh hưởng đến thải trừ ganciclovir."
        },
        "overdose_management": {
            "symptoms": [
                "Giảm bạch cầu, tiểu cầu, hồng cầu nghiêm trọng (tăng so với liều điều trị)",
                "Độc thận (suy thận cấp)",
                "Độc thần kinh (lú lẫn, co giật, ảo giác, rối loạn tâm thần)",
                "Nhiễm trùng nặng (do giảm bạch cầu)",
                "Chảy máu nặng (do giảm tiểu cầu)",
                "Thiếu máu nặng (do giảm hồng cầu)",
                "Tử vong (trong trường hợp quá liều nghiêm trọng)"
            ],
            "antidote": "Không có antidote đặc hiệu. Điều trị hỗ trợ và điều trị triệu chứng.",
            "treatment": [
                "Ngừng ganciclovir ngay lập tức",
                "Theo dõi CBC chặt chẽ (mỗi ngày hoặc 2 lần/ngày)",
                "Điều trị giảm bạch cầu:",
                "  - G-CSF (filgrastim) để tăng bạch cầu",
                "  - Kháng sinh phổ rộng nếu có nhiễm trùng",
                "  - Cách ly nếu bạch cầu rất thấp",
                "Điều trị giảm tiểu cầu:",
                "  - Truyền tiểu cầu nếu <10,000/mm³ hoặc có chảy máu",
                "  - Tránh thuốc chống đông, NSAID",
                "Điều trị thiếu máu:",
                "  - Truyền hồng cầu nếu cần",
                "  - Erythropoietin nếu cần",
                "Điều trị độc thận:",
                "  - Truyền dịch, điều chỉnh điện giải",
                "  - Hemodialysis nếu suy thận nặng (ganciclovir có thể được lọc qua thận nhân tạo)",
                "Điều trị độc thần kinh:",
                "  - An thần nếu co giật, kích động",
                "  - Anticonvulsant nếu co giật",
                "  - Theo dõi thần kinh chặt chẽ",
                "Theo dõi dấu hiệu sinh tồn: Huyết áp, nhịp tim, nhịp thở, SpO2",
                "Theo dõi chức năng thận: Creatinine, BUN, eGFR",
                "Theo dõi ít nhất 1-2 tuần sau khi ngừng ganciclovir"
            ],
            "monitoring": "CBC (bạch cầu, tiểu cầu, hồng cầu) mỗi ngày hoặc 2 lần/ngày, chức năng thận (creatinine, BUN, eGFR), dấu hiệu nhiễm trùng, dấu hiệu chảy máu, dấu hiệu độc thần kinh, dấu hiệu sinh tồn. Theo dõi ít nhất 1-2 tuần sau khi ngừng ganciclovir."
        },
        "reversal_agents": {
            "available": False,
            "agents": []
        },
        "administration_instructions": {
            "oral": {
                "with_food": "Có thể uống với hoặc không thức ăn. Hấp thu kém (6-9% bioavailability), nhưng thức ăn không ảnh hưởng đáng kể.",
                "timing": "Uống 3 lần/ngày (1g mỗi lần) sau khi hoàn thành IV induction. Uống cùng thời điểm mỗi ngày để duy trì nồng độ ổn định."
            },
            "iv": {
                "reconstitution": "Pha với nước muối đẳng trương (0.9% NaCl) hoặc D5W. Nồng độ pha: 10 mg/ml (tối đa). Pha 500mg trong 50ml = 10 mg/ml. Lắc kỹ để hòa tan hoàn toàn.",
                "infusion_rate": "Truyền chậm trong ít nhất 1 giờ. Không truyền nhanh (tăng nguy cơ độc tính).",
                "compatibility": ["Normal saline (0.9% NaCl)", "D5W (5% Dextrose)"],
                "incompatibility": ["Không trộn với các thuốc khác"],
                "notes": "Truyền IV chậm trong ít nhất 1 giờ. Duy trì đủ dịch để giảm độc thận. Theo dõi CBC 2-3 lần/tuần khi dùng IV. Điều chỉnh liều ở suy thận: CrCl 50-80: giảm liều 50%; CrCl 25-50: giảm liều 75%; CrCl <25: giảm liều 90%."
            }
        },
        "references": {
            "primary_sources": [
                "FDA Drug Label - Ganciclovir (Cytovene)",
                "IDSA Guidelines - Cytomegalovirus Infection",
                "UpToDate - Ganciclovir: Drug Information",
                "Goodman & Gilman's The Pharmacological Basis of Therapeutics (14th ed)"
            ],
            "last_updated": "2025-02-04",
            "evidence_level": "A - Dựa trên FDA drug labels, IDSA guidelines, và dữ liệu lâm sàng"
        }
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
        "black_box_warnings": "Chống chỉ định tuyệt đối trong thai kỳ (nam và nữ) - gây dị tật thai nhi và tử vong thai nhi. Có thể gây thiếu máu nặng, đe dọa tính mạng. Có thể gây rối loạn tâm thần nghiêm trọng",
        "drug_interactions": {
            "major": [
                {
                    "drug": "Zidovudine (AZT)",
                    "mechanism": "Cả hai đều gây thiếu máu và giảm bạch cầu, tác dụng cộng dồn làm tăng nguy cơ độc tính huyết học nghiêm trọng.",
                    "effect": "Tăng nguy cơ thiếu máu nặng, giảm bạch cầu, giảm tiểu cầu, đe dọa tính mạng",
                    "management": "TRÁNH DÙNG đồng thời nếu có thể. Nếu bắt buộc, theo dõi CBC chặt chẽ mỗi 1-2 tuần. Có thể cần giảm liều hoặc ngừng một trong hai thuốc nếu có thiếu máu nặng."
                },
                {
                    "drug": "Didanosine",
                    "mechanism": "Cả hai đều gây độc tính ty thể và thiếu máu, tác dụng cộng dồn.",
                    "effect": "Tăng nguy cơ thiếu máu, độc tính ty thể, viêm tụy, nhiễm toan lactic",
                    "management": "TRÁNH DÙNG đồng thời. Nếu bắt buộc, theo dõi CBC, chức năng tụy, và lactate chặt chẽ."
                },
                {
                    "drug": "Azathioprine",
                    "mechanism": "Cả hai đều ức chế tổng hợp purine và gây độc tính tủy xương, tác dụng cộng dồn.",
                    "effect": "Tăng nguy cơ thiếu máu, giảm bạch cầu, giảm tiểu cầu nghiêm trọng",
                    "management": "TRÁNH DÙNG đồng thời. Nếu bắt buộc, theo dõi CBC chặt chẽ, giảm liều hoặc ngừng nếu có độc tính huyết học."
                }
            ],
            "moderate": [],
            "minor": []
        },
        "contraindications": {
            "tuyệt_đối": [
                "Có thai (nam và nữ) - chống chỉ định tuyệt đối, gây dị tật thai nhi và tử vong thai nhi",
                "Suy thận nặng (CrCl <50 ml/min) - không dùng",
                "Bệnh tim nặng (suy tim, bệnh mạch vành không ổn định) - nguy cơ thiếu máu làm nặng bệnh tim",
                "Thiếu máu nặng (Hb <8.5g/dL) - không bắt đầu điều trị",
                "Dị ứng ribavirin"
            ],
            "tương_đối": [
                "Suy thận trung bình (CrCl 30-50) - giảm liều 50%, theo dõi chặt chẽ",
                "Bệnh tim nhẹ đến trung bình - thận trọng, theo dõi sát hemoglobin",
                "Thiếu máu nhẹ đến trung bình (Hb 8.5-10g/dL) - có thể cần giảm liều hoặc truyền máu",
                "Tiền sử rối loạn tâm thần - tăng nguy cơ rối loạn tâm thần, đặc biệt khi dùng với interferon",
                "Bệnh nhân cao tuổi - tăng nguy cơ độc tính"
            ]
        },
        "pregnancy_lactation": {
            "fda_category": "X",
            "pregnancy_details": "Chống chỉ định tuyệt đối trong thai kỳ (nam và nữ). Ribavirin gây dị tật thai nhi nghiêm trọng, tử vong thai nhi, và sẩy thai. Nam và nữ phải dùng biện pháp tránh thai hiệu quả trong và 6 tháng sau khi ngừng thuốc. Kiểm tra thai trước khi bắt đầu điều trị (nam và nữ).",
            "lactation": {
                "safety": "Incompatible",
                "details": "Ribavirin bài tiết vào sữa mẹ. Thuốc rất độc, có thể gây độc tính nghiêm trọng cho trẻ sơ sinh.",
                "recommendation": "Không cho con bú khi dùng ribavirin. Ngừng cho con bú hoặc ngừng thuốc."
            }
        },
        "hepatic_adjustment": {
            "mild": "Không đổi",
            "moderate": "Thận trọng, theo dõi chức năng gan",
            "severe": "Thận trọng, có thể cần giảm liều",
            "notes": "Ribavirin chuyển hóa một phần qua gan. Thải trừ chủ yếu qua thận. Suy gan có thể làm tăng nồng độ và độc tính."
        },
        "overdose_management": {
            "symptoms": [
                "Thiếu máu nặng (Hb <8.5g/dL)",
                "Giảm bạch cầu, giảm tiểu cầu",
                "Mệt mỏi, khó thở",
                "Rối loạn tâm thần",
                "Suy thận cấp"
            ],
            "antidote": "Không có antidote đặc hiệu",
            "treatment": [
                "Ngừng ngay ribavirin",
                "Theo dõi CBC, chức năng thận, chức năng gan",
                "Truyền máu nếu thiếu máu nặng (Hb <8.5g/dL)",
                "Supportive care",
                "Lọc máu có thể giúp loại bỏ ribavirin (half-life dài, tích tụ trong tế bào)",
                "Theo dõi tâm thần nếu có rối loạn tâm thần"
            ],
            "monitoring": "CBC mỗi ngày, chức năng thận, chức năng gan, dấu hiệu lâm sàng"
        },
        "reversal_agents": None,
        "administration_instructions": {
            "oral": {
                "with_food": "Uống với thức ăn để giảm kích ứng dạ dày",
                "timing": "Chia 2 lần/ngày, uống với thức ăn"
            },
            "iv": {
                "reconstitution": "Pha với NS hoặc D5W theo hướng dẫn nhà sản xuất",
                "infusion_rate": "Truyền trong 30-60 phút",
                "compatibility": ["NS", "D5W"],
                "incompatibility": [],
                "notes": "Loading dose: 30-35mg/kg x 1 lần, sau đó 15-20mg/kg mỗi 6 giờ. Theo dõi chức năng thận."
            }
        },
        "references": {
            "primary_sources": [
                "FDA Drug Label - Ribavirin (Rebetol)",
                "UpToDate - Ribavirin Drug Information",
                "Goodman & Gilman's Pharmacological Basis of Therapeutics, 14th ed"
            ],
            "last_updated": "2025-01-15",
            "evidence_level": "High (FDA-approved, extensive clinical data)"
        }
    },

}

__all__ = ['ANTIVIRALS']
