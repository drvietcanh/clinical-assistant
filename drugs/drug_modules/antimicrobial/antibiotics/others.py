"""
Other Antibiotics
Fosfomycin, Nitrofurantoin, Fidaxomicin
"""

OTHER_ANTIBIOTICS = {
    "Eravacycline": {
        "group": "Antibiotic - Tetracycline (Next Generation)",
        "vietnamese_name": "Eravacycline, Xerava",
        "administration": ["IV"],
        "indications": [
            "Nhiễm khuẩn ổ bụng phức tạp (cIAI) do vi khuẩn Gram-âm, Gram-dương, và kỵ khí",
            "Nhiễm khuẩn ổ bụng do vi khuẩn đa kháng",
            "Nhiễm khuẩn do CRE (Carbapenem-resistant Enterobacteriaceae)",
            "Nhiễm khuẩn do MDR Gram-âm (khi các kháng sinh khác không hiệu quả)"
        ],
        "contraindications": [
            "Dị ứng eravacycline hoặc tetracycline",
            "Trẻ em <18 tuổi - chưa được nghiên cứu",
            "Phụ nữ có thai - CHỐNG CHỈ ĐỊNH (category D)",
            "Phụ nữ đang cho con bú - thận trọng"
        ],
        "contraindications_detail": {
            "tuyệt_đối": [
                "Dị ứng eravacycline hoặc tetracycline",
                "Phụ nữ có thai - CHỐNG CHỈ ĐỊNH (category D)"
            ],
            "tương_đối": [
                "Trẻ em <18 tuổi - chưa được nghiên cứu",
                "Phụ nữ đang cho con bú - thận trọng"
            ]
        },
        "reversal_agents": {"available": False, "agents": [], "notes": "Không có antidote đặc hiệu. Điều trị chủ yếu là hỗ trợ và điều trị triệu chứng. Ngừng thuốc ngay. Hydration đầy đủ để tăng thải trừ."},
        "dosage": {
            "adult_standard": "1mg/kg IV mỗi 12 giờ trong 4-14 ngày",
            "adult_ciai": "1mg/kg IV mỗi 12 giờ trong 4-14 ngày",
            "notes": "Eravacycline là tetracycline thế hệ mới, kháng được nhiều cơ chế kháng tetracycline. Dùng 2 lần/ngày. Truyền IV trong 60 phút. Điều chỉnh liều theo chức năng gan."
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "Không đổi",
            "under_30": "Không đổi (thải trừ qua gan và thận)"
        },
        "side_effects": [
            "Buồn nôn, nôn - phổ biến",
            "Tiêu chảy",
            "Phản ứng tại chỗ tiêm (đau, viêm tĩnh mạch)",
            "Tăng transaminase (hiếm)",
            "Nhạy cảm với ánh sáng (photosensitivity) - hiếm",
            "Răng vàng (ở trẻ em, nếu dùng) - hiếm",
            "Ức chế xương (ở trẻ em, nếu dùng) - hiếm"
        ],
        "interactions": [
            "Warfarin: có thể tăng INR",
            "Thuốc tránh thai đường uống: có thể giảm hiệu quả",
            "Antacid, sắt, canxi: giảm hấp thu (nếu có dạng uống)",
            "Penicillin: giảm hiệu quả penicillin (bacteriostatic vs bactericidal)"
        ],
        "pregnancy": "D - CHỐNG CHỈ ĐỊNH",
        "mechanism_of_action": "Eravacycline là tetracycline thế hệ mới (fluorocycline), kháng được nhiều cơ chế kháng tetracycline (efflux pumps, ribosomal protection). Gắn với ribosome 30S của vi khuẩn, ngăn chặn sự gắn aminoacyl-tRNA với ribosome, dẫn đến ức chế tổng hợp protein (bacteriostatic). Phổ kháng khuẩn: Gram-dương (Staphylococcus - kể cả MRSA, Streptococcus, Enterococcus - kể cả VRE), Gram-âm (Enterobacteriaceae - kể cả CRE, E. coli, Klebsiella, Enterobacter, Acinetobacter), và kỵ khí (Bacteroides fragilis, Clostridium). Không hiệu quả với Pseudomonas aeruginosa. ĐẶC ĐIỂM: (1) Kháng được nhiều cơ chế kháng tetracycline (ưu điểm so với tetracycline cũ), (2) Hiệu quả với CRE và MDR Gram-âm, (3) Phổ rộng (Gram-dương, Gram-âm, kỵ khí), (4) Dùng 2 lần/ngày, (5) CHỐNG CHỈ ĐỊNH ở phụ nữ có thai (category D), (6) Buồn nôn, nôn phổ biến.",
        "monitoring": [
            "Dấu hiệu nhiễm trùng (sốt, WBC, triệu chứng lâm sàng)",
            "Cấy máu và cấy từ vị trí nhiễm trùng",
            "Dấu hiệu buồn nôn, nôn - phổ biến",
            "Chức năng gan (ALT, AST) - hiếm",
            "Dấu hiệu nhạy cảm với ánh sáng (đỏ da, phát ban)",
            "PT/INR (nếu dùng với warfarin)"
        ],
        "precautions": [
            "CHỐNG CHỈ ĐỊNH ở phụ nữ có thai (category D) - gây răng vàng và ức chế xương ở thai nhi",
            "Buồn nôn, nôn phổ biến - có thể cần điều trị hỗ trợ",
            "Truyền IV trong 60 phút để giảm phản ứng tại chỗ",
            "Điều chỉnh liều theo chức năng gan (suy gan nặng)",
            "Tránh ánh nắng mặt trời (nhạy cảm ánh sáng)",
            "Theo dõi INR nếu dùng với warfarin",
            "Không dùng với antacid, sắt, canxi cùng lúc (nếu có dạng uống)",
            "Trẻ em <18 tuổi - chưa được nghiên cứu"
        ],
        "pharmacokinetics": {
            "half_life": "20 giờ",
            "onset": "Ngay lập tức sau khi tiêm IV",
            "duration": "12 giờ (dùng 2 lần/ngày)",
            "protein_binding": "79-90%",
            "metabolism": "Chuyển hóa một phần ở gan (CYP3A4)",
            "clearance": "Thải trừ qua gan (50%) và thận (50%)"
        },
        "storage": "Bảo quản bột khô ở nhiệt độ phòng (20-25°C). Sau khi pha: bảo quản ở nhiệt độ phòng 6 giờ, hoặc trong tủ lạnh 24 giờ. Không đông lạnh.",
        "black_box_warnings": "CHỐNG CHỈ ĐỊNH ở phụ nữ có thai (category D). Eravacycline gây răng vàng và ức chế xương ở thai nhi. Không dùng trong thai kỳ.",
        "drug_interactions": {
            "major": [
                {
                    "drug": "Warfarin",
                    "mechanism": "Eravacycline có thể ức chế tổng hợp vitamin K phụ thuộc vào hệ vi khuẩn đường ruột, làm giảm sản xuất các yếu tố đông máu phụ thuộc vitamin K.",
                    "effect": "Tăng INR, tăng nguy cơ chảy máu",
                    "management": "Theo dõi INR thường xuyên (ít nhất 2-3 lần/tuần khi bắt đầu dùng eravacycline). Có thể cần giảm liều warfarin."
                }
            ],
            "moderate": [
                {
                    "drug": "Thuốc tránh thai đường uống",
                    "mechanism": "Tetracycline có thể làm giảm hệ vi khuẩn đường ruột, làm giảm tái hấp thu estrogen từ đường ruột.",
                    "effect": "Giảm hiệu quả thuốc tránh thai (hiếm, nhưng có thể xảy ra)",
                    "management": "Khuyến cáo sử dụng biện pháp tránh thai bổ sung (bao cao su) trong khi dùng eravacycline và 7 ngày sau khi ngừng."
                }
            ],
            "minor": []
        },
        "contraindications": {
            "tuyệt_đối": [
                "Dị ứng eravacycline hoặc tetracycline",
                "Phụ nữ có thai - CHỐNG CHỈ ĐỊNH (category D, gây răng vàng và ức chế xương ở thai nhi)"
            ],
            "tương_đối": [
                "Trẻ em <18 tuổi - chưa được nghiên cứu",
                "Phụ nữ đang cho con bú - thận trọng",
                "Suy gan nặng - điều chỉnh liều",
                "Nhạy cảm với ánh sáng - tránh ánh nắng mặt trời"
            ]
        },
        "pregnancy_lactation": {
            "fda_category": "D",
            "pregnancy_details": "Eravacycline là thuốc phân loại D. CHỐNG CHỈ ĐỊNH trong thai kỳ. Tetracycline gây răng vàng và ức chế xương ở thai nhi. Không dùng trong thai kỳ.",
            "lactation": {
                "safety": "Compatible with Caution",
                "details": "Eravacycline bài tiết vào sữa mẹ. Tetracycline có thể gây răng vàng và ức chế xương ở trẻ bú mẹ. Thận trọng khi cho con bú.",
                "recommendation": "Tránh dùng khi cho con bú. Nếu bắt buộc, theo dõi trẻ về dấu hiệu răng vàng và ức chế xương."
            }
        },
        "hepatic_adjustment": {
            "mild": "Không cần điều chỉnh liều",
            "moderate": "Giảm liều 25-50%",
            "severe": "Giảm liều 50% hoặc tăng khoảng cách liều",
            "notes": "Eravacycline chuyển hóa một phần ở gan (CYP3A4) và thải trừ qua gan (50%). Suy gan nặng có thể làm tích lũy eravacycline, tăng nguy cơ tác dụng phụ. Cần điều chỉnh liều ở suy gan nặng."
        },
        "overdose_management": {
            "symptoms": [
                "Buồn nôn, nôn nặng",
                "Tiêu chảy nặng",
                "Tăng transaminase",
                "Nhạy cảm với ánh sáng nặng"
            ],
            "antidote": "Không có antidote đặc hiệu. Điều trị hỗ trợ.",
            "treatment": [
                "Ngừng ngay eravacycline",
                "Điều trị buồn nôn, nôn: Antiemetic (ondansetron, metoclopramide)",
                "Điều trị tiêu chảy: Bù dịch, điện giải",
                "Theo dõi: Dấu hiệu sinh tồn, chức năng gan"
            ],
            "monitoring": "Theo dõi dấu hiệu sinh tồn, chức năng gan (ALT, AST) trong ít nhất 24-48 giờ."
        },
        "reversal_agents": {"available": False, "agents": [], "notes": "Không có antidote đặc hiệu. Điều trị chủ yếu là hỗ trợ và điều trị triệu chứng. Ngừng thuốc ngay nếu có độc tính gan nặng."},
        "administration_instructions": {
            "oral": None,
            "iv": {
                "reconstitution": "Pha với NS (0.9% NaCl) hoặc D5W (5% Dextrose). Nồng độ pha: 0.3-0.5mg/ml. Pha 1mg/kg trong 100ml = 0.01mg/ml (quá loãng). Pha 1mg/kg trong 250ml = 0.004mg/ml. Truyền trong 60 phút.",
                "infusion_rate": "Truyền IV trong 60 phút. Tốc độ: 100ml/60 phút = ~1.7ml/phút.",
                "compatibility": ["NS (0.9% NaCl)", "D5W (5% Dextrose)"],
                "incompatibility": [
                    "Antacid, sắt, canxi - giảm hấp thu (nếu có dạng uống)",
                    "Penicillin - giảm hiệu quả penicillin"
                ],
                "notes": "QUAN TRỌNG: 1) Dùng 2 lần/ngày (1mg/kg mỗi 12 giờ), 2) CHỐNG CHỈ ĐỊNH ở phụ nữ có thai, 3) Buồn nôn, nôn phổ biến, 4) Truyền IV trong 60 phút, 5) Điều chỉnh liều theo chức năng gan, 6) Tránh ánh nắng mặt trời."
            }
        },
        "references": {
            "primary_sources": [
                "FDA Drug Label - Eravacycline (Xerava)",
                "UpToDate - Eravacycline: Drug Information",
                "Medscape - Eravacycline Drug Reference",
                "IDSA Guidelines - Complicated Intra-abdominal Infections",
                "IDSA Guidelines - Antimicrobial Resistance"
            ],
            "last_updated": "2025-02-18",
            "evidence_level": "A - Dựa trên FDA drug labels, IDSA guidelines, và dữ liệu lâm sàng từ nhiều nguồn"
        },
        "risk_flags": {
            "high_alert": False,
            "narrow_therapeutic_index": False,
            "icu_critical_care_only": False,
            "bleeding_risk": "Low",
            "organ_toxicity": {"hepatic": "Low", "gastrointestinal": "Moderate"}
        },
        "guideline_tags": [
            "IDSA Guidelines - Complicated Intra-abdominal Infections",
            "IDSA Guidelines - Antimicrobial Resistance",
            "IDSA Guidelines - Multidrug-Resistant Gram-Negative Infections"
        ]
    },
    
    "Fidaxomicin": {
        "group": "Antibiotic - Macrocyclic",
        "vietnamese_name": "Fidaxomicin, Dificid",
        "administration": ["PO"],
        "indications": [
            "Nhiễm Clostridioides difficile (C. diff) - đợt đầu tiên",
            "Nhiễm C. diff tái phát",
            "Nhiễm C. diff nặng",
            "Dự phòng tái phát C. diff (ở bệnh nhân có nguy cơ cao)"
        ],
        "contraindications": [
            "Dị ứng fidaxomicin",
            "Trẻ em <18 tuổi - chưa có dữ liệu an toàn"
        ],
        "dosage": {
            "adult_cdiff_first": "200mg PO x 2 lần/ngày x 10 ngày",
            "adult_cdiff_recurrent": "200mg PO x 2 lần/ngày x 10 ngày",
            "adult_cdiff_severe": "200mg PO x 2 lần/ngày x 10 ngày",
            "notes": "Uống với hoặc không thức ăn. Liều cố định 200mg x 2 lần/ngày. Tỷ lệ tái phát thấp hơn vancomycin (ưu điểm chính). Không hấp thu vào máu (chỉ tác dụng tại ruột)."
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "Không đổi (không hấp thu vào máu)",
            "under_30": "Không đổi (không hấp thu vào máu)"
        },
        "side_effects": [
            "Buồn nôn (phổ biến)",
            "Nôn",
            "Đau bụng",
            "Tiêu chảy",
            "Phát ban (hiếm)",
            "Giảm bạch cầu (hiếm)",
            "Tăng men gan (hiếm)"
        ],
        "interactions": [
            "Cyclosporine: tăng nồng độ fidaxomicin (hiếm, vì fidaxomicin không hấp thu)",
            "Không có tương tác đáng kể (không hấp thu vào máu)"
        ],
        "pregnancy": "B - An toàn trong thai kỳ",
        "mechanism_of_action": "Fidaxomicin là kháng sinh macrocyclic, ức chế RNA polymerase của vi khuẩn, ngăn chặn tổng hợp RNA và protein. Phổ kháng khuẩn: Clostridioides difficile (C. diff) mạnh, một số vi khuẩn Gram-dương khác (Staphylococcus, Enterococcus), không có hoạt tính với vi khuẩn Gram-âm hoặc kỵ khí khác. ĐẶC ĐIỂM QUAN TRỌNG: (1) KHÔNG hấp thu vào máu (chỉ tác dụng tại ruột) - an toàn, ít tác dụng phụ toàn thân, (2) Tỷ lệ tái phát thấp hơn vancomycin (15-25% so với 25-35% của vancomycin) - ưu điểm chính, (3) Ít ảnh hưởng đến hệ vi khuẩn đường ruột bình thường (microbiome-sparing), (4) Hiệu quả với cả đợt đầu tiên và tái phát, (5) Đắt tiền hơn vancomycin. Được khuyến cáo là lựa chọn ưu tiên trong IDSA/SHEA 2021 guidelines cho C. diff.",
        "monitoring": [
            "Dấu hiệu nhiễm C. diff (tiêu chảy, đau bụng, sốt) để đánh giá đáp ứng điều trị",
            "Xét nghiệm C. diff (NAAT, GDH, Toxin) - theo dõi đáp ứng",
            "Công thức máu (CBC) - hiếm giảm bạch cầu",
            "Chức năng gan (ALT, AST) - hiếm tăng men gan",
            "Dấu hiệu tái phát (tiêu chảy tái phát sau khi ngừng thuốc)",
            "Dấu hiệu dị ứng (phát ban) - hiếm"
        ],
        "precautions": [
            "Chỉ dùng cho nhiễm C. diff - KHÔNG dùng cho nhiễm khuẩn khác",
            "Uống với hoặc không thức ăn (không ảnh hưởng hấp thu vì không hấp thu)",
            "Liều cố định 200mg x 2 lần/ngày - không cần điều chỉnh liều",
            "Không cần điều chỉnh liều theo chức năng thận (không hấp thu vào máu)",
            "Không cần điều chỉnh liều theo chức năng gan (không hấp thu vào máu)",
            "Tỷ lệ tái phát thấp hơn vancomycin - ưu điểm chính",
            "Ít ảnh hưởng đến hệ vi khuẩn đường ruột bình thường (microbiome-sparing)",
            "Đắt tiền hơn vancomycin - cân nhắc chi phí",
            "Theo dõi dấu hiệu tái phát sau khi ngừng thuốc"
        ],
        "pharmacokinetics": {
            "half_life": "Không áp dụng (không hấp thu vào máu)",
            "onset": "2-4 ngày (cải thiện triệu chứng)",
            "duration": "10 ngày (liều chuẩn)",
            "protein_binding": "Không áp dụng (không hấp thu vào máu)",
            "clearance": "Không hấp thu vào máu, thải trừ qua phân (dạng nguyên dạng)"
        },
        "storage": "Bảo quản ở nhiệt độ phòng (20-25°C), tránh ẩm, tránh ánh sáng. Viên nén: bảo quản trong bao bì kín.",
        "black_box_warnings": None,
        "drug_interactions": {
            "major": [],
            "moderate": [
                {
                    "drug": "Cyclosporine",
                    "mechanism": "Cyclosporine ức chế P-gp, có thể tăng nồng độ fidaxomicin (hiếm, vì fidaxomicin không hấp thu)",
                    "effect": "Tăng nhẹ nồng độ fidaxomicin (không đáng kể vì không hấp thu)",
                    "management": "Không cần điều chỉnh liều. Fidaxomicin không hấp thu vào máu, tương tác không đáng kể."
                }
            ],
            "minor": []
        },
        "contraindications": {
            "tuyệt_đối": [
                "Dị ứng fidaxomicin"
            ],
            "tương_đối": [
                "Trẻ em <18 tuổi - chưa có dữ liệu an toàn",
                "Có thai - thận trọng (phân loại B, nhưng dữ liệu còn hạn chế)"
            ]
        },
        "contraindications_detail": {
            "tuyệt_đối": [
                "Dị ứng fidaxomicin"
            ],
            "tương_đối": [
                "Trẻ em <18 tuổi - chưa có dữ liệu an toàn",
                "Có thai - thận trọng (phân loại B, nhưng dữ liệu còn hạn chế)"
            ]
        },
        "pregnancy_lactation": {
            "fda_category": "B",
            "pregnancy_details": "Fidaxomicin là thuốc phân loại B. Không có bằng chứng về nguy cơ dị tật thai nhi trong các nghiên cứu trên động vật. Các nghiên cứu trên người không cho thấy nguy cơ tăng dị tật bẩm sinh rõ ràng, nhưng dữ liệu còn hạn chế. Fidaxomicin không hấp thu vào máu (chỉ tác dụng tại ruột), nên ít có khả năng ảnh hưởng đến thai nhi. Có thể dùng khi lợi ích vượt quá nguy cơ, đặc biệt trong điều trị C. diff nặng. C. diff trong thai kỳ có thể gây nguy hiểm cho cả mẹ và thai nhi nếu không điều trị.",
            "lactation": {
                "safety": "Compatible",
                "details": "Fidaxomicin không hấp thu vào máu, nên không bài tiết vào sữa mẹ. Không có báo cáo về tác dụng phụ ở trẻ bú mẹ.",
                "recommendation": "Có thể dùng khi cho con bú. Fidaxomicin không hấp thu vào máu và không bài tiết vào sữa mẹ."
            }
        },
        "hepatic_adjustment": {
            "mild": "Không cần điều chỉnh liều (không hấp thu vào máu)",
            "moderate": "Không cần điều chỉnh liều (không hấp thu vào máu)",
            "severe": "Không cần điều chỉnh liều (không hấp thu vào máu)",
            "notes": "Fidaxomicin không hấp thu vào máu, chỉ tác dụng tại ruột. Không cần điều chỉnh liều ở bệnh nhân suy gan."
        },
        "overdose_management": {
            "symptoms": [
                "Buồn nôn, nôn nặng",
                "Tiêu chảy",
                "Đau bụng"
            ],
            "antidote": "Không có antidote đặc hiệu. Điều trị hỗ trợ.",
            "treatment": [
                "Ngừng fidaxomicin",
                "Điều trị triệu chứng tiêu hóa:",
                "  - Chống nôn nếu cần",
                "  - Truyền dịch nếu mất nước",
                "  - Theo dõi điện giải",
                "Theo dõi: Triệu chứng, điện giải"
            ],
            "monitoring": "Theo dõi triệu chứng, điện giải trong 24-48 giờ."
        },
        "reversal_agents": {
            "available": False,
            "agents": [],
            "notes": "Không có reversal agent đặc hiệu. Điều trị hỗ trợ. Fidaxomicin không hấp thu vào máu, nên ít nguy cơ độc tính toàn thân."
        },
        "administration_instructions": {
            "oral": {
                "with_food": "Uống với hoặc không thức ăn (không ảnh hưởng hấp thu vì không hấp thu vào máu).",
                "timing": "200mg PO x 2 lần/ngày x 10 ngày. Uống đều đặn, cách đều nhau trong ngày (q12h). Không bỏ liều.",
                "notes": "QUAN TRỌNG: 1) Chỉ dùng cho nhiễm C. diff, 2) Liều cố định 200mg x 2 lần/ngày, 3) Không cần điều chỉnh liều theo chức năng thận/gan (không hấp thu vào máu), 4) Tỷ lệ tái phát thấp hơn vancomycin (ưu điểm chính), 5) Ít ảnh hưởng đến hệ vi khuẩn đường ruột bình thường, 6) Đắt tiền hơn vancomycin."
            }
        },
        "references": {
            "primary_sources": [
                "FDA Drug Label - Fidaxomicin (Dificid)",
                "IDSA/SHEA Guidelines 2021 - Clostridioides difficile Infection",
                "UpToDate - Fidaxomicin: Drug Information",
                "Medscape - Fidaxomicin Drug Reference"
            ],
            "last_updated": "2025-02-18",
            "evidence_level": "A - Dựa trên FDA drug labels, IDSA/SHEA guidelines 2021, và dữ liệu lâm sàng từ nhiều nguồn"
        },
        "risk_flags": {
            "high_alert": False,
            "narrow_therapeutic_index": False,
            "icu_critical_care_only": False,
            "bleeding_risk": "Low",
            "organ_toxicity": {"gastrointestinal": "Low"}
        },
        "guideline_tags": [
            "IDSA/SHEA Guidelines - Clostridioides difficile Infection",
            "IDSA Guidelines - Clostridium difficile Infection",
            "WHO Essential Medicines List"
        ],
        "last_updated": "2025-02-18"
    },
    
    "Fosfomycin": {
        "group": "Antibiotic - Phosphonic Acid",
        "vietnamese_name": "Fosfomycin, Monuril",
        "administration": ["PO", "IV"],
        "indications": [
            "Nhiễm khuẩn đường tiết niệu không biến chứng (PO) - liều đơn",
            "Nhiễm khuẩn đường tiết niệu phức tạp (IV)",
            "Viêm bể thận cấp",
            "Nhiễm khuẩn do MDR Gram âm (kết hợp với kháng sinh khác)",
            "Nhiễm khuẩn đường tiết niệu tái phát"
        ],
        "contraindications": [
            "Dị ứng fosfomycin",
            "Suy thận nặng (CrCl <10) - IV",
            "Trẻ em <12 tuổi - PO (dạng hạt)"
        ],
        "dosage": {
            "adult_po_uti": "3g PO x 1 liều duy nhất (nhiễm khuẩn tiết niệu không biến chứng)",
            "adult_iv_standard": "12-16g IV chia 3-4 lần/ngày",
            "adult_iv_severe": "12g IV mỗi 8 giờ hoặc 16g IV mỗi 8 giờ",
            "adult_iv_max": "24g IV/ngày (tối đa)",
            "pediatric_po": "Không dùng <12 tuổi (dạng hạt)",
            "pediatric_iv": "200-300mg/kg/ngày IV chia 3-4 lần (tối đa 12g/ngày)",
            "notes": "PO: liều đơn 3g cho UTI không biến chứng (ưu điểm - compliance cao). IV: dùng cho nhiễm khuẩn nặng, thường kết hợp với kháng sinh khác. Uống khi đói (2-3 giờ trước hoặc sau ăn) để tăng hấp thu."
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "Giảm liều 25-50% (IV)",
            "15_30": "Giảm liều 50% (IV)",
            "under_15": "Tránh dùng IV (CrCl <10). PO: có thể dùng nhưng thận trọng."
        },
        "side_effects": [
            "Tiêu chảy (phổ biến với PO)",
            "Buồn nôn, nôn",
            "Phát ban",
            "Viêm tĩnh mạch (IV)",
            "Tăng transaminase (hiếm)",
            "Đau đầu",
            "Chóng mặt"
        ],
        "interactions": [
            "Metoclopramide: giảm nồng độ fosfomycin PO (giảm hấp thu)",
            "Cần cách 2 giờ trước uống metoclopramide"
        ],
        "pregnancy": "B - An toàn trong thai kỳ",
        "mechanism_of_action": "Fosfomycin là kháng sinh phosphonic acid, ức chế tổng hợp thành tế bào vi khuẩn bằng cách ức chế enzyme MurA (UDP-N-acetylglucosamine enolpyruvyl transferase), ngăn chặn bước đầu tiên trong tổng hợp peptidoglycan. Phổ kháng khuẩn: Gram-dương (một số Staphylococcus, Enterococcus), Gram-âm (E. coli, K. pneumoniae, Enterobacter, Proteus, Pseudomonas - một số chủng), và một số vi khuẩn khác. Đặc điểm: (1) Liều đơn cho UTI không biến chứng (3g PO x 1 lần) - ưu điểm compliance cao, (2) Hiệu quả với một số vi khuẩn kháng đa thuốc (MDR), (3) Ít tương tác thuốc, (4) An toàn trong thai kỳ. Hấp thu tốt khi uống khi đói (2-3 giờ trước hoặc sau ăn).",
        "monitoring": [
            "Dấu hiệu nhiễm trùng (sốt, triệu chứng UTI) để đánh giá đáp ứng điều trị",
            "Cấy nước tiểu (nếu có) để xác định vi khuẩn và độ nhạy cảm",
            "Chức năng thận (creatinine, eGFR) - đặc biệt với IV",
            "Chức năng gan (ALT, AST) - hiếm tăng men gan",
            "Dấu hiệu dị ứng (phát ban) - hiếm"
        ],
        "precautions": [
            "PO: uống khi đói (2-3 giờ trước hoặc sau ăn) để tăng hấp thu",
            "PO: pha hạt trong nước (150-200ml), uống ngay sau khi pha",
            "PO: liều đơn 3g cho UTI không biến chứng - ưu điểm compliance cao",
            "IV: điều chỉnh liều theo chức năng thận (CrCl <30: giảm liều)",
            "Tránh dùng IV nếu CrCl <10",
            "Tránh dùng metoclopramide cùng lúc (giảm hấp thu PO)",
            "Cách metoclopramide 2 giờ nếu cần dùng",
            "Thận trọng ở suy thận (IV)",
            "Có thể dùng trong thai kỳ (phân loại B)"
        ],
        "pharmacokinetics": {
            "half_life": "5.7 giờ (PO), 2-4 giờ (IV)",
            "onset": "2-4 giờ (PO)",
            "duration": "Liều đơn (PO), q8h (IV)",
            "protein_binding": "Không đáng kể",
            "clearance": "Thận (chủ yếu bài tiết qua thận dạng nguyên dạng), cần điều chỉnh thận với IV"
        },
        "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm, tránh ánh sáng. Dạng hạt: bảo quản trong bao bì kín. IV: bảo quản trong tủ lạnh, dùng trong vòng 24 giờ sau khi pha.",
        "black_box_warnings": None,
        "drug_interactions": {
            "major": [
                {
                    "drug": "Metoclopramide",
                    "mechanism": "Metoclopramide tăng nhu động ruột, giảm thời gian lưu lại trong ruột, giảm hấp thu fosfomycin PO",
                    "effect": "Giảm nồng độ fosfomycin, giảm hiệu quả điều trị",
                    "management": "Cách metoclopramide 2 giờ trước khi uống fosfomycin. Hoặc dùng IV nếu cần dùng metoclopramide."
                }
            ],
            "moderate": [],
            "minor": []
        },
        "contraindications": {
            "tuyệt_đối": [
                "Dị ứng fosfomycin"
            ],
            "tương_đối": [
                "Suy thận nặng (CrCl <10) - tránh dùng IV",
                "Trẻ em <12 tuổi - PO (dạng hạt không dùng được)",
                "Suy thận (CrCl 10-30) - giảm liều IV"
            ]
        },
        "contraindications_detail": {
            "tuyệt_đối": [
                "Dị ứng fosfomycin"
            ],
            "tương_đối": [
                "Suy thận nặng (CrCl <10) - tránh dùng IV",
                "Trẻ em <12 tuổi - PO (dạng hạt không dùng được)",
                "Suy thận (CrCl 10-30) - giảm liều IV"
            ]
        },
        "pregnancy_lactation": {
            "fda_category": "B",
            "pregnancy_details": "Fosfomycin là thuốc phân loại B. Không có bằng chứng về nguy cơ dị tật thai nhi trong các nghiên cứu trên động vật. Các nghiên cứu trên người không cho thấy nguy cơ tăng dị tật bẩm sinh. Được sử dụng trong thai kỳ để điều trị UTI và có vẻ an toàn. UTI trong thai kỳ có thể gây nguy hiểm cho cả mẹ và thai nhi nếu không điều trị.",
            "lactation": {
                "safety": "Compatible",
                "details": "Fosfomycin bài tiết vào sữa mẹ ở nồng độ thấp. Không có báo cáo về tác dụng phụ ở trẻ bú mẹ.",
                "recommendation": "Có thể dùng khi cho con bú. Fosfomycin bài tiết vào sữa mẹ ở nồng độ thấp và không gây hại cho trẻ."
            }
        },
        "hepatic_adjustment": {
            "mild": "Không cần điều chỉnh liều",
            "moderate": "Không cần điều chỉnh liều",
            "severe": "Thận trọng (hiếm tăng men gan)",
            "notes": "Fosfomycin không chuyển hóa đáng kể, thải trừ chủ yếu qua thận. Không cần điều chỉnh liều ở bệnh nhân suy gan, nhưng thận trọng ở suy gan nặng (hiếm tăng men gan)."
        },
        "overdose_management": {
            "symptoms": [
                "Tiêu chảy nặng",
                "Buồn nôn, nôn",
                "Đau bụng",
                "Tăng men gan (hiếm)"
            ],
            "antidote": "Không có antidote đặc hiệu. Điều trị hỗ trợ.",
            "treatment": [
                "Ngừng fosfomycin",
                "Điều trị triệu chứng tiêu hóa:",
                "  - Chống nôn nếu cần",
                "  - Truyền dịch nếu mất nước",
                "  - Theo dõi điện giải",
                "Theo dõi chức năng gan nếu có tăng men gan",
                "Theo dõi: Triệu chứng, chức năng gan"
            ],
            "monitoring": "Theo dõi triệu chứng, chức năng gan trong 24-48 giờ."
        },
        "reversal_agents": {
            "available": False,
            "agents": [],
            "notes": "Không có reversal agent đặc hiệu. Điều trị hỗ trợ."
        },
        "administration_instructions": {
            "oral": {
                "with_food": "Uống khi đói (2-3 giờ trước hoặc sau ăn) để tăng hấp thu. Không uống với thức ăn.",
                "timing": "Liều đơn 3g PO x 1 lần cho UTI không biến chứng. Pha hạt trong 150-200ml nước, uống ngay sau khi pha.",
                "reconstitution": "Pha hạt trong 150-200ml nước (lạnh hoặc ấm), khuấy đều, uống ngay sau khi pha."
            },
            "iv": {
                "reconstitution": "Pha theo hướng dẫn nhà sản xuất. Thường pha với D5W hoặc NS.",
                "infusion_rate": "Standard: 12-16g IV chia 3-4 lần/ngày, truyền trong 30-60 phút. Severe: 12g IV mỗi 8 giờ hoặc 16g IV mỗi 8 giờ.",
                "compatibility": ["D5W (5% Dextrose)", "NS (0.9% NaCl)"],
                "incompatibility": [
                    "Không trộn với các thuốc khác. Dùng đường truyền riêng."
                ],
                "notes": "QUAN TRỌNG: 1) Điều chỉnh liều theo chức năng thận (CrCl <30: giảm liều), 2) Tránh dùng IV nếu CrCl <10, 3) Truyền trong 30-60 phút, 4) Theo dõi chức năng thận."
            }
        },
        "references": {
            "primary_sources": [
                "FDA Drug Label - Fosfomycin (Monuril)",
                "IDSA Guidelines - Antimicrobial Therapy, UTI",
                "UpToDate - Fosfomycin: Drug Information",
                "Medscape - Fosfomycin Drug Reference"
            ],
            "last_updated": "2025-02-18",
            "evidence_level": "A - Dựa trên FDA drug labels, IDSA guidelines, và dữ liệu lâm sàng từ nhiều nguồn"
        },
        "risk_flags": {
            "high_alert": False,
            "narrow_therapeutic_index": False,
            "icu_critical_care_only": False,
            "bleeding_risk": "Low",
            "organ_toxicity": {"hepatic": "Low", "renal": "Low"}
        },
        "guideline_tags": [
            "IDSA Guidelines - Complicated Urinary Tract Infections",
            "IDSA Guidelines - Uncomplicated Urinary Tract Infections",
            "IDSA Guidelines - Multidrug-Resistant Gram-Negative Infections",
            "WHO Essential Medicines List"
        ],
        "last_updated": "2025-02-18"
    },
    
    "Lefamulin": {
        "group": "Antibiotic - Pleuromutilin",
        "vietnamese_name": "Lefamulin, Xenleta",
        "administration": ["IV", "PO"],
        "indications": [
            "Viêm phổi cộng đồng (CABP) do vi khuẩn",
            "Viêm phổi do MRSA",
            "Viêm phổi do MDR Gram-âm (khi các kháng sinh khác không hiệu quả)"
        ],
        "contraindications": [
            "Dị ứng lefamulin",
            "Rối loạn nhịp tim (QT prolongation) - thận trọng",
            "Dùng với thuốc kéo dài QT - thận trọng",
            "Trẻ em <18 tuổi - chưa được nghiên cứu"
        ],
        "dosage": {
            "adult_iv": "150mg IV mỗi 12 giờ trong 5-7 ngày",
            "adult_po": "600mg PO mỗi 12 giờ trong 5-7 ngày",
            "notes": "Lefamulin là pleuromutilin, có cả dạng IV và PO. Dùng 2 lần/ngày trong 5-7 ngày. Uống khi đói (1 giờ trước hoặc 2 giờ sau ăn). Có thể kéo dài QT interval."
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "Không đổi",
            "under_30": "Không đổi (thải trừ qua gan và thận)"
        },
        "side_effects": [
            "Tiêu chảy - phổ biến",
            "Buồn nôn, nôn",
            "Phản ứng tại chỗ tiêm (IV) - đau, viêm tĩnh mạch",
            "Kéo dài QT interval - phổ biến",
            "Rối loạn nhịp tim (arrhythmia) - hiếm",
            "Tăng transaminase (hiếm)",
            "Đau đầu"
        ],
        "interactions": [
            "Thuốc kéo dài QT (quinidine, procainamide, amiodarone, sotalol): tăng nguy cơ kéo dài QT",
            "CYP3A4 inhibitors (ketoconazole, clarithromycin): tăng nồng độ lefamulin",
            "CYP3A4 inducers (rifampin, carbamazepine): giảm nồng độ lefamulin",
            "P-glycoprotein inhibitors: tăng nồng độ lefamulin"
        ],
        "pregnancy": "C - Thận trọng",
        "mechanism_of_action": "Lefamulin là pleuromutilin (kháng sinh mới), gắn với ribosome 50S của vi khuẩn tại vị trí peptidyl transferase center, ngăn chặn sự tổng hợp protein, dẫn đến tiêu diệt vi khuẩn (bactericidal). Phổ kháng khuẩn: Gram-dương (Staphylococcus - kể cả MRSA, Streptococcus, Enterococcus - kể cả VRE), Gram-âm (Haemophilus influenzae, Moraxella catarrhalis), và một số kỵ khí (Mycoplasma pneumoniae, Chlamydia pneumoniae, Legionella pneumophila). Không hiệu quả với Enterobacteriaceae, Pseudomonas, hoặc Acinetobacter. ĐẶC ĐIỂM: (1) Pleuromutilin (kháng sinh mới, cơ chế độc đáo), (2) Hiệu quả với MRSA và viêm phổi cộng đồng, (3) Có cả dạng IV và PO (ưu điểm), (4) Dùng 2 lần/ngày trong 5-7 ngày, (5) Có thể kéo dài QT interval - cần theo dõi ECG, (6) Tiêu chảy phổ biến.",
        "monitoring": [
            "Dấu hiệu nhiễm trùng (sốt, WBC, triệu chứng lâm sàng)",
            "Cấy máu và cấy từ vị trí nhiễm trùng",
            "ECG - QUAN TRỌNG: theo dõi QT interval (có thể kéo dài)",
            "Dấu hiệu rối loạn nhịp tim (palpitations, chóng mặt, ngất)",
            "Dấu hiệu tiêu chảy - phổ biến",
            "Chức năng gan (ALT, AST) - hiếm"
        ],
        "precautions": [
            "Có thể kéo dài QT interval - theo dõi ECG trước và sau điều trị",
            "Thận trọng ở bệnh nhân có rối loạn nhịp tim hoặc dùng thuốc kéo dài QT",
            "Tiêu chảy phổ biến - có thể cần điều trị hỗ trợ",
            "Uống khi đói (1 giờ trước hoặc 2 giờ sau ăn) để tăng hấp thu (PO)",
            "Tránh dùng với CYP3A4 inhibitors mạnh (ketoconazole, clarithromycin) - tăng nồng độ",
            "Tránh dùng với CYP3A4 inducers mạnh (rifampin, carbamazepine) - giảm nồng độ",
            "Trẻ em <18 tuổi - chưa được nghiên cứu"
        ],
        "pharmacokinetics": {
            "half_life": "8 giờ",
            "onset": "Ngay lập tức sau khi tiêm IV, 1-2 giờ sau khi uống (PO)",
            "duration": "12 giờ (dùng 2 lần/ngày)",
            "protein_binding": "94-97%",
            "metabolism": "Chuyển hóa một phần ở gan (CYP3A4)",
            "clearance": "Thải trừ qua gan (50%) và thận (50%)"
        },
        "storage": "Bảo quản bột khô (IV) và viên nén (PO) ở nhiệt độ phòng (20-25°C). Sau khi pha (IV): bảo quản ở nhiệt độ phòng 6 giờ, hoặc trong tủ lạnh 24 giờ. Không đông lạnh.",
        "black_box_warnings": "Có thể kéo dài QT interval và gây rối loạn nhịp tim. Theo dõi ECG trước và sau điều trị. Thận trọng ở bệnh nhân có rối loạn nhịp tim hoặc dùng thuốc kéo dài QT.",
        "drug_interactions": {
            "major": [
                {
                    "drug": "Thuốc kéo dài QT (Quinidine, Procainamide, Amiodarone, Sotalol)",
                    "mechanism": "Cả hai đều kéo dài QT interval, tác dụng cộng dồn",
                    "effect": "Tăng nguy cơ kéo dài QT nặng, rối loạn nhịp tim (torsades de pointes)",
                    "management": "TRÁNH DÙNG CÙNG. Nếu bắt buộc, theo dõi ECG chặt chẽ trước và sau điều trị. Theo dõi QT interval."
                },
                {
                    "drug": "CYP3A4 Inhibitors mạnh (Ketoconazole, Clarithromycin, Itraconazole)",
                    "mechanism": "Ức chế CYP3A4, tăng nồng độ lefamulin",
                    "effect": "Tăng nồng độ lefamulin, tăng nguy cơ tác dụng phụ (kéo dài QT)",
                    "management": "TRÁNH DÙNG CÙNG. Nếu bắt buộc, giảm liều lefamulin và theo dõi ECG chặt chẽ."
                }
            ],
            "moderate": [
                {
                    "drug": "CYP3A4 Inducers mạnh (Rifampin, Carbamazepine, Phenytoin)",
                    "mechanism": "Cảm ứng CYP3A4, giảm nồng độ lefamulin",
                    "effect": "Giảm nồng độ lefamulin, giảm hiệu quả",
                    "management": "Thận trọng. Có thể cần tăng liều lefamulin. Theo dõi đáp ứng điều trị."
                }
            ],
            "minor": []
        },
        "contraindications": {
            "tuyệt_đối": [
                "Dị ứng lefamulin"
            ],
            "tương_đối": [
                "Rối loạn nhịp tim (QT prolongation) - thận trọng, theo dõi ECG",
                "Dùng với thuốc kéo dài QT - thận trọng, theo dõi ECG",
                "Trẻ em <18 tuổi - chưa được nghiên cứu",
                "Có thai (category C) - thận trọng"
            ]
        },
        "pregnancy_lactation": {
            "fda_category": "C",
            "pregnancy_details": "Lefamulin là thuốc phân loại C. Không có nghiên cứu đầy đủ trên phụ nữ có thai. Có thể dùng khi lợi ích vượt quá nguy cơ, đặc biệt khi không có lựa chọn khác.",
            "lactation": {
                "safety": "Compatible with Caution",
                "details": "Lefamulin bài tiết vào sữa mẹ. Thận trọng khi cho con bú.",
                "recommendation": "Có thể dùng khi cho con bú, nhưng thận trọng. Theo dõi trẻ về dấu hiệu tiêu chảy."
            }
        },
        "hepatic_adjustment": {
            "mild": "Không cần điều chỉnh liều",
            "moderate": "Giảm liều 25-50%",
            "severe": "Giảm liều 50% hoặc tăng khoảng cách liều",
            "notes": "Lefamulin chuyển hóa một phần ở gan (CYP3A4) và thải trừ qua gan (50%). Suy gan nặng có thể làm tích lũy lefamulin, tăng nguy cơ tác dụng phụ (kéo dài QT). Cần điều chỉnh liều ở suy gan nặng."
        },
        "overdose_management": {
            "symptoms": [
                "Kéo dài QT interval nặng",
                "Rối loạn nhịp tim (torsades de pointes) - NGUY HIỂM",
                "Tiêu chảy nặng",
                "Buồn nôn, nôn nặng"
            ],
            "antidote": "Magnesium sulfate cho torsades de pointes. Điều trị hỗ trợ.",
            "treatment": [
                "Ngừng ngay lefamulin",
                "Nếu torsades de pointes:",
                "  - Magnesium sulfate 1-2g IV",
                "  - Điều chỉnh điện giải (K+, Mg2+)",
                "  - Máy tạo nhịp tạm thời nếu cần",
                "Nếu tiêu chảy nặng:",
                "  - Bù dịch, điện giải",
                "  - Điều trị hỗ trợ",
                "Theo dõi: ECG, dấu hiệu sinh tồn, điện giải"
            ],
            "monitoring": "Theo dõi ECG (QT interval), dấu hiệu sinh tồn, điện giải (K+, Mg2+) trong ít nhất 24-48 giờ. Theo dõi lâu hơn nếu có rối loạn nhịp tim."
        },
        "reversal_agents": {
            "available": True,
            "agents": [
                {
                    "agent": "Magnesium Sulfate",
                    "mechanism": "Điều trị torsades de pointes do kéo dài QT",
                    "indication": "Torsades de pointes do lefamulin",
                    "dose": "1-2g IV, lặp lại nếu cần"
                }
            ],
            "notes": "Magnesium sulfate điều trị torsades de pointes do kéo dài QT interval."
        },
        "administration_instructions": {
            "oral": {
                "with_food": "Uống khi đói (1 giờ trước hoặc 2 giờ sau ăn) để tăng hấp thu",
                "timing": "600mg PO mỗi 12 giờ trong 5-7 ngày. Uống đều đặn, cách đều nhau trong ngày."
            },
            "iv": {
                "reconstitution": "Pha với NS (0.9% NaCl) hoặc D5W (5% Dextrose). Nồng độ pha: 1.5mg/ml. Pha 150mg trong 100ml = 1.5mg/ml. Truyền trong 60 phút.",
                "infusion_rate": "Truyền IV trong 60 phút. Tốc độ: 100ml/60 phút = ~1.7ml/phút.",
                "compatibility": ["NS (0.9% NaCl)", "D5W (5% Dextrose)"],
                "incompatibility": [
                    "Thuốc kéo dài QT - tăng nguy cơ kéo dài QT",
                    "CYP3A4 inhibitors mạnh - tăng nồng độ"
                ],
                "notes": "QUAN TRỌNG: 1) Dùng 2 lần/ngày (150mg IV hoặc 600mg PO mỗi 12 giờ), 2) Có thể kéo dài QT interval - theo dõi ECG, 3) Tiêu chảy phổ biến, 4) Uống khi đói (PO), 5) Tránh dùng với thuốc kéo dài QT, 6) Tránh dùng với CYP3A4 inhibitors mạnh."
            }
        },
        "references": {
            "primary_sources": [
                "FDA Drug Label - Lefamulin (Xenleta)",
                "UpToDate - Lefamulin: Drug Information",
                "Medscape - Lefamulin Drug Reference",
                "IDSA Guidelines - Community-Acquired Pneumonia"
            ],
            "last_updated": "2025-02-18",
            "evidence_level": "A - Dựa trên FDA drug labels, IDSA guidelines, và dữ liệu lâm sàng từ nhiều nguồn"
        },
        "risk_flags": {
            "high_alert": True,
            "narrow_therapeutic_index": False,
            "icu_critical_care_only": False,
            "bleeding_risk": "Low",
            "organ_toxicity": {"cardiac": "High (QT prolongation)", "gastrointestinal": "Moderate"}
        },
        "guideline_tags": [
            "IDSA Guidelines - Community-Acquired Pneumonia",
            "IDSA Guidelines - Methicillin-Resistant Staphylococcus aureus Infections"
        ]
    },
    "Nitrofurantoin": {
        "group": "Antibiotic - Nitrofuran",
        "vietnamese_name": "Nitrofurantoin, Macrobid, Macrodantin",
        "administration": ["PO"],
        "indications": [
            "Nhiễm khuẩn đường tiết niệu không biến chứng (cystitis)",
            "Dự phòng nhiễm khuẩn đường tiết niệu tái phát",
            "Nhiễm khuẩn đường tiết niệu do E. coli, Enterococcus"
        ],
        "contraindications": [
            "Dị ứng nitrofurantoin",
            "Suy thận nặng (CrCl <30) - CHỐNG CHỈ ĐỊNH (không hiệu quả, tăng độc tính)",
            "Suy thận (CrCl 30-60) - thận trọng",
            "Trẻ em <1 tháng tuổi - CHỐNG CHỈ ĐỊNH",
            "Thiếu G6PD (glucose-6-phosphate dehydrogenase) - CHỐNG CHỈ ĐỊNH (nguy cơ tan máu)",
            "Có thai (gần sinh, 38-42 tuần) - CHỐNG CHỈ ĐỊNH (nguy cơ tan máu ở trẻ sơ sinh)"
        ],
        "dosage": {
            "adult_uti_standard": "100mg PO x 2 lần/ngày x 5-7 ngày",
            "adult_uti_macrobid": "100mg PO x 2 lần/ngày (dạng viên nang phóng thích kéo dài)",
            "adult_uti_macrodantin": "50-100mg PO x 4 lần/ngày x 5-7 ngày",
            "adult_prophylaxis": "50-100mg PO x 1 lần/ngày (buổi tối)",
            "pediatric_uti": "5-7 mg/kg/ngày PO chia 4 lần (tối đa 400mg/ngày)",
            "notes": "Uống với thức ăn hoặc sữa để giảm kích ứng dạ dày. Dạng macrobid (phóng thích kéo dài): 100mg x 2 lần/ngày. Dạng macrodantin (phóng thích nhanh): 50-100mg x 4 lần/ngày. KHÔNG dùng nếu CrCl <30 (không hiệu quả, tăng độc tính)."
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "Thận trọng (có thể không hiệu quả, tăng độc tính)",
            "under_30": "CHỐNG CHỈ ĐỊNH (không hiệu quả, tăng độc tính)"
        },
        "side_effects": [
            "Buồn nôn, nôn (phổ biến)",
            "Tiêu chảy",
            "Đau đầu",
            "Phát ban",
            "Tan máu (hemolytic anemia) - đặc biệt ở thiếu G6PD",
            "Viêm phổi cấp (acute pneumonitis) - hiếm nhưng nguy hiểm",
            "Viêm phổi mạn tính (chronic pneumonitis) - hiếm, có thể không hồi phục",
            "Độc thần kinh ngoại biên (peripheral neuropathy) - hiếm, có thể không hồi phục",
            "Độc gan (hepatotoxicity) - hiếm"
        ],
        "interactions": [
            "Antacids (magnesium trisilicate): giảm hấp thu nitrofurantoin",
            "Probenecid: tăng nồng độ nitrofurantoin (giảm bài tiết ở ống thận)",
            "Sulfinpyrazone: tăng nồng độ nitrofurantoin"
        ],
        "pregnancy": "B - Tránh gần sinh (38-42 tuần)",
        "mechanism_of_action": "Nitrofurantoin là kháng sinh nitrofuran, ức chế nhiều enzyme trong quá trình tổng hợp DNA, RNA, và protein của vi khuẩn. Nitrofurantoin được chuyển đổi thành các chất trung gian phản ứng trong vi khuẩn, gây tổn thương DNA và ức chế tổng hợp protein. Phổ kháng khuẩn: Gram-dương (một số Staphylococcus, Enterococcus), Gram-âm (E. coli, Enterobacter, Klebsiella, Proteus), không hiệu quả với Pseudomonas, Serratia. Đặc điểm: (1) Chỉ hiệu quả trong đường tiết niệu (nồng độ cao trong nước tiểu, nồng độ thấp trong máu), (2) KHÔNG dùng cho nhiễm khuẩn ngoài đường tiết niệu (viêm phổi, nhiễm khuẩn huyết), (3) KHÔNG hiệu quả nếu CrCl <30 (không đạt nồng độ trong nước tiểu), (4) Nguy cơ tan máu ở thiếu G6PD, (5) Nguy cơ viêm phổi (cấp và mạn tính), (6) Nguy cơ độc thần kinh ngoại biên.",
        "monitoring": [
            "Dấu hiệu nhiễm trùng (triệu chứng UTI) để đánh giá đáp ứng điều trị",
            "Cấy nước tiểu (nếu có) để xác định vi khuẩn và độ nhạy cảm",
            "Chức năng thận (creatinine, eGFR) - QUAN TRỌNG: không dùng nếu CrCl <30",
            "Công thức máu (CBC) - theo dõi tan máu, đặc biệt ở thiếu G6PD",
            "Dấu hiệu viêm phổi: ho, khó thở, sốt, đau ngực (ngừng ngay nếu có)",
            "Dấu hiệu độc thần kinh ngoại biên: tê bì, yếu cơ, đau (ngừng ngay nếu có)",
            "Chức năng gan (ALT, AST) - hiếm độc gan",
            "Dấu hiệu dị ứng (phát ban) - hiếm"
        ],
        "precautions": [
            "CHỐNG CHỈ ĐỊNH nếu CrCl <30 - không hiệu quả, tăng độc tính",
            "CHỐNG CHỈ ĐỊNH nếu thiếu G6PD - nguy cơ tan máu nặng",
            "CHỐNG CHỈ ĐỊNH gần sinh (38-42 tuần) - nguy cơ tan máu ở trẻ sơ sinh",
            "CHỐNG CHỈ ĐỊNH trẻ em <1 tháng tuổi",
            "CHỈ dùng cho nhiễm khuẩn đường tiết niệu - KHÔNG dùng cho nhiễm khuẩn ngoài đường tiết niệu",
            "NGỪNG NGAY nếu có dấu hiệu viêm phổi (ho, khó thở, sốt, đau ngực) - có thể nguy hiểm tính mạng",
            "NGỪNG NGAY nếu có dấu hiệu độc thần kinh ngoại biên (tê bì, yếu cơ, đau) - có thể không hồi phục",
            "Uống với thức ăn hoặc sữa để giảm kích ứng dạ dày",
            "Tránh dùng với antacids (giảm hấp thu)",
            "Thận trọng ở người cao tuổi (tăng nguy cơ tác dụng phụ)",
            "Theo dõi công thức máu nếu dùng kéo dài (prophylaxis)"
        ],
        "pharmacokinetics": {
            "half_life": "20-60 phút (rất ngắn)",
            "onset": "2-4 giờ",
            "duration": "q6-12h (tùy dạng)",
            "protein_binding": "60%",
            "clearance": "Thận (chủ yếu bài tiết qua thận dạng nguyên dạng), nồng độ cao trong nước tiểu, nồng độ thấp trong máu"
        },
        "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm, tránh ánh sáng. Viên nén/viên nang: bảo quản trong bao bì kín.",
        "black_box_warnings": "CHỐNG CHỈ ĐỊNH nếu CrCl <30 (không hiệu quả, tăng độc tính). CHỐNG CHỈ ĐỊNH nếu thiếu G6PD (nguy cơ tan máu nặng). CHỐNG CHỈ ĐỊNH gần sinh (38-42 tuần) - nguy cơ tan máu ở trẻ sơ sinh. Nguy cơ viêm phổi cấp và mạn tính (có thể nguy hiểm tính mạng, có thể không hồi phục). Nguy cơ độc thần kinh ngoại biên (có thể không hồi phục).",
        "drug_interactions": {
            "major": [
                {
                    "drug": "Probenecid, Sulfinpyrazone",
                    "mechanism": "Probenecid và sulfinpyrazone ức chế bài tiết nitrofurantoin ở ống thận, tăng nồng độ nitrofurantoin trong máu",
                    "effect": "Tăng nồng độ nitrofurantoin, tăng độc tính (viêm phổi, độc thần kinh)",
                    "management": "TRÁNH dùng đồng thời. Nếu bắt buộc, giảm liều nitrofurantoin, theo dõi sát dấu hiệu độc tính."
                }
            ],
            "moderate": [
                {
                    "drug": "Antacids (magnesium trisilicate, aluminum hydroxide)",
                    "mechanism": "Làm giảm hấp thu nitrofurantoin",
                    "effect": "Giảm hiệu quả điều trị",
                    "management": "Uống cách nhau ít nhất 2 giờ."
                }
            ],
            "minor": []
        },
        "risk_flags": {
            "high_alert": True,
            "narrow_therapeutic_index": False,
            "icu_critical_care_only": False,
            "bleeding_risk": "Low",
            "organ_toxicity": {"pulmonary": "High (acute/chronic pneumonitis)", "neurological": "High (peripheral neuropathy)", "hematologic": "High (hemolytic anemia in G6PD)"}
        },
        "guideline_tags": [
            "IDSA Guidelines - Uncomplicated Urinary Tract Infections",
            "WHO Essential Medicines List"
        ],
        "last_updated": "2025-02-18",
        "contraindications": {
            "tuyệt_đối": [
                "Dị ứng nitrofurantoin",
                "Suy thận nặng (CrCl <30) - CHỐNG CHỈ ĐỊNH (không hiệu quả, tăng độc tính)",
                "Thiếu G6PD (glucose-6-phosphate dehydrogenase) - CHỐNG CHỈ ĐỊNH (nguy cơ tan máu nặng)",
                "Trẻ em <1 tháng tuổi - CHỐNG CHỈ ĐỊNH",
                "Có thai (gần sinh, 38-42 tuần) - CHỐNG CHỈ ĐỊNH (nguy cơ tan máu ở trẻ sơ sinh)"
            ],
            "tương_đối": [
                "Suy thận (CrCl 30-60) - thận trọng (có thể không hiệu quả, tăng độc tính)",
                "Có thai (tam cá nguyệt 1-2) - thận trọng, chỉ dùng khi thực sự cần thiết",
                "Người cao tuổi - tăng nguy cơ tác dụng phụ",
                "Có tiền sử bệnh phổi - tăng nguy cơ viêm phổi",
                "Có tiền sử bệnh thần kinh - tăng nguy cơ độc thần kinh"
            ]
        },
        "pregnancy_lactation": {
            "fda_category": "B (tam cá nguyệt 1-2), D (gần sinh)",
            "pregnancy_details": "Tam cá nguyệt 1-2: Thuốc phân loại B - thận trọng. Các nghiên cứu trên động vật không cho thấy nguy cơ dị tật bẩm sinh. Các nghiên cứu trên người không cho thấy nguy cơ tăng dị tật bẩm sinh rõ ràng. Có thể dùng khi lợi ích vượt quá nguy cơ, đặc biệt trong điều trị UTI. Gần sinh (38-42 tuần): Thuốc phân loại D - CHỐNG CHỈ ĐỊNH. Nitrofurantoin có thể gây tan máu ở trẻ sơ sinh thiếu G6PD, dẫn đến vàng da nặng và kernicterus. Không dùng trong 38-42 tuần thai kỳ.",
            "lactation": {
                "safety": "Compatible with Caution",
                "details": "Nitrofurantoin bài tiết vào sữa mẹ ở nồng độ thấp. Nồng độ trong sữa mẹ thấp và không có báo cáo về tác dụng phụ đáng kể ở trẻ bú mẹ. Tuy nhiên, nitrofurantoin có thể gây tan máu ở trẻ sơ sinh thiếu G6PD. Thận trọng ở trẻ sơ sinh < 1 tháng tuổi hoặc thiếu G6PD.",
                "recommendation": "Có thể dùng khi cho con bú, nhưng thận trọng ở trẻ sơ sinh < 1 tháng tuổi hoặc thiếu G6PD. Dùng liều thấp nhất hiệu quả. Theo dõi trẻ sơ sinh nếu dùng liều cao hoặc kéo dài (vàng da, tan máu)."
            }
        },
        "hepatic_adjustment": {
            "mild": "Không cần điều chỉnh liều",
            "moderate": "Thận trọng (hiếm độc gan)",
            "severe": "CHỐNG CHỈ ĐỊNH hoặc thận trọng tối đa (nguy cơ độc gan nặng)",
            "notes": "Nitrofurantoin có thể gây độc gan (hiếm nhưng nghiêm trọng). Suy gan nặng là chống chỉ định do nguy cơ độc gan nặng. Theo dõi chặt chẽ chức năng gan ở suy gan trung bình."
        },
        "overdose_management": {
            "symptoms": [
                "Buồn nôn, nôn nặng",
                "Tiêu chảy",
                "Tan máu (hemolytic anemia) - đặc biệt ở thiếu G6PD",
                "Viêm phổi cấp (ho, khó thở, sốt, đau ngực) - nguy hiểm tính mạng",
                "Độc thần kinh ngoại biên (tê bì, yếu cơ, đau) - có thể không hồi phục",
                "Độc gan (tăng men gan, viêm gan) - hiếm nhưng nghiêm trọng"
            ],
            "antidote": "Không có antidote đặc hiệu. Điều trị hỗ trợ và điều trị triệu chứng.",
            "treatment": [
                "Ngừng ngay nitrofurantoin",
                "Rửa dạ dày hoặc than hoạt nếu uống trong vòng 1-2 giờ (nếu không có chống chỉ định)",
                "Theo dõi dấu hiệu sinh tồn: Huyết áp, nhịp tim, nhịp thở, SpO2",
                "Điều trị triệu chứng tiêu hóa:",
                "  - Chống nôn nếu cần",
                "  - Truyền dịch nếu mất nước",
                "Nếu tan máu:",
                "  - Theo dõi công thức máu (CBC), bilirubin",
                "  - Truyền máu nếu cần",
                "  - Điều trị vàng da nếu có",
                "Nếu viêm phổi cấp:",
                "  - NGỪNG NGAY nitrofurantoin",
                "  - Hỗ trợ hô hấp: Thở oxy, nếu cần hỗ trợ thông khí cơ học",
                "  - Corticosteroid (còn tranh cãi)",
                "  - Điều trị hỗ trợ",
                "Nếu độc thần kinh ngoại biên:",
                "  - NGỪNG NGAY nitrofurantoin",
                "  - Điều trị hỗ trợ (vật lý trị liệu)",
                "  - Có thể không hồi phục",
                "Nếu độc gan:",
                "  - Theo dõi ALT, AST, bilirubin",
                "  - Điều trị hỗ trợ gan",
                "  - Nếu viêm gan nặng: điều trị suy gan",
                "Theo dõi: Dấu hiệu sinh tồn, công thức máu, chức năng gan, thần kinh, hô hấp"
            ],
            "monitoring": "Theo dõi dấu hiệu sinh tồn, công thức máu (CBC), chức năng gan (ALT, AST, bilirubin), dấu hiệu hô hấp (viêm phổi), dấu hiệu thần kinh (độc thần kinh ngoại biên) trong ít nhất 24-48 giờ. Theo dõi lâu hơn nếu có biến chứng (viêm phổi, độc thần kinh, độc gan, tan máu)."
        },
        "reversal_agents": {
            "available": False,
            "agents": [],
            "notes": "Không có reversal agent đặc hiệu. Điều trị hỗ trợ. Ngừng ngay nitrofurantoin nếu có dấu hiệu độc tính."
        },
        "administration_instructions": {
            "oral": {
                "with_food": "Uống với thức ăn hoặc sữa để giảm kích ứng dạ dày. Có thể uống không thức ăn nếu cần nhưng không khuyến nghị.",
                "timing": "Standard: 100mg PO x 2 lần/ngày x 5-7 ngày (dạng macrobid). Hoặc 50-100mg PO x 4 lần/ngày x 5-7 ngày (dạng macrodantin). Prophylaxis: 50-100mg PO x 1 lần/ngày (buổi tối). Uống đều đặn, cách đều nhau trong ngày. Không bỏ liều.",
                "notes": "QUAN TRỌNG: 1) CHỐNG CHỈ ĐỊNH nếu CrCl <30, 2) CHỐNG CHỈ ĐỊNH nếu thiếu G6PD, 3) CHỐNG CHỈ ĐỊNH gần sinh (38-42 tuần), 4) CHỈ dùng cho nhiễm khuẩn đường tiết niệu, 5) NGỪNG NGAY nếu có dấu hiệu viêm phổi hoặc độc thần kinh, 6) Uống với thức ăn hoặc sữa, 7) Tránh dùng với antacids (cách 2 giờ)."
            }
        },
        "references": {
            "primary_sources": [
                "FDA Drug Label - Nitrofurantoin (Macrobid, Macrodantin)",
                "IDSA Guidelines - Antimicrobial Therapy, UTI",
                "UpToDate - Nitrofurantoin: Drug Information",
                "Medscape - Nitrofurantoin Drug Reference"
            ],
            "last_updated": "2025-02-18",
            "evidence_level": "A - Dựa trên FDA drug labels, IDSA guidelines, và dữ liệu lâm sàng từ nhiều nguồn"
        },
        "risk_flags": {
            "high_alert": True,
            "narrow_therapeutic_index": False,
            "icu_critical_care_only": False,
            "bleeding_risk": "Low",
            "organ_toxicity": {"pulmonary": "High (acute pneumonitis)", "neurological": "High (peripheral neuropathy)", "hepatic": "Moderate", "hematologic": "Moderate (hemolytic anemia in G6PD deficiency)"}
        },
        "guideline_tags": [
            "IDSA Guidelines - Uncomplicated Urinary Tract Infections",
            "IDSA Guidelines - Urinary Tract Infection Prophylaxis",
            "WHO Essential Medicines List"
        ],
        "last_updated": "2025-02-18",
    },
    
    "Omadacycline": {
        "group": "Antibiotic - Tetracycline (Next Generation)",
        "vietnamese_name": "Omadacycline, Nuzyra",
        "administration": ["IV", "PO"],
        "indications": [
            "Viêm phổi cộng đồng (CABP) do vi khuẩn",
            "Nhiễm khuẩn da và mô mềm (ABSSSI) do vi khuẩn",
            "Nhiễm khuẩn do MRSA",
            "Nhiễm khuẩn do MDR Gram-âm (khi các kháng sinh khác không hiệu quả)"
        ],
        "contraindications": [
            "Dị ứng omadacycline hoặc tetracycline",
            "Trẻ em <18 tuổi - chưa được nghiên cứu",
            "Phụ nữ có thai - CHỐNG CHỈ ĐỊNH (category D)",
            "Phụ nữ đang cho con bú - thận trọng"
        ],
        "dosage": {
            "adult_iv_loading": "200mg IV x 1 liều (liều nạp), sau đó 100mg IV mỗi 12 giờ",
            "adult_iv_maintenance": "100mg IV mỗi 12 giờ",
            "adult_po_loading": "300mg PO x 2 lần/ngày (ngày đầu), sau đó 300mg PO x 1 lần/ngày",
            "adult_po_maintenance": "300mg PO x 1 lần/ngày",
            "notes": "Omadacycline là tetracycline thế hệ mới, có cả dạng IV và PO. Dạng IV: liều nạp 200mg, sau đó 100mg mỗi 12 giờ. Dạng PO: liều nạp 300mg x 2 lần/ngày (ngày đầu), sau đó 300mg x 1 lần/ngày. Uống khi đói (4 giờ trước hoặc 2 giờ sau ăn)."
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "Không đổi",
            "under_30": "Không đổi (thải trừ qua gan và thận)"
        },
        "side_effects": [
            "Buồn nôn, nôn - phổ biến",
            "Tiêu chảy",
            "Phản ứng tại chỗ tiêm (IV) - đau, viêm tĩnh mạch",
            "Tăng transaminase (hiếm)",
            "Nhạy cảm với ánh sáng (photosensitivity) - hiếm",
            "Răng vàng (ở trẻ em, nếu dùng) - hiếm",
            "Ức chế xương (ở trẻ em, nếu dùng) - hiếm"
        ],
        "interactions": [
            "Warfarin: có thể tăng INR",
            "Thuốc tránh thai đường uống: có thể giảm hiệu quả",
            "Antacid, sắt, canxi, magie, nhôm: giảm hấp thu (PO) - cách 4 giờ",
            "Penicillin: giảm hiệu quả penicillin (bacteriostatic vs bactericidal)"
        ],
        "pregnancy": "D - CHỐNG CHỈ ĐỊNH",
        "mechanism_of_action": "Omadacycline là tetracycline thế hệ mới (aminomethylcycline), kháng được nhiều cơ chế kháng tetracycline (efflux pumps, ribosomal protection). Gắn với ribosome 30S của vi khuẩn, ngăn chặn sự gắn aminoacyl-tRNA với ribosome, dẫn đến ức chế tổng hợp protein (bacteriostatic). Phổ kháng khuẩn: Gram-dương (Staphylococcus - kể cả MRSA, Streptococcus, Enterococcus - kể cả VRE), Gram-âm (Enterobacteriaceae, E. coli, Klebsiella, Enterobacter, Acinetobacter), và một số kỵ khí (Bacteroides fragilis). Không hiệu quả với Pseudomonas aeruginosa. ĐẶC ĐIỂM: (1) Kháng được nhiều cơ chế kháng tetracycline (ưu điểm so với tetracycline cũ), (2) Hiệu quả với MRSA và MDR Gram-âm, (3) Có cả dạng IV và PO (ưu điểm), (4) Dạng PO: liều nạp ngày đầu, sau đó 1 lần/ngày, (5) CHỐNG CHỈ ĐỊNH ở phụ nữ có thai (category D), (6) Buồn nôn, nôn phổ biến.",
        "monitoring": [
            "Dấu hiệu nhiễm trùng (sốt, WBC, triệu chứng lâm sàng)",
            "Cấy máu và cấy từ vị trí nhiễm trùng",
            "Dấu hiệu buồn nôn, nôn - phổ biến",
            "Chức năng gan (ALT, AST) - hiếm",
            "Dấu hiệu nhạy cảm với ánh sáng (đỏ da, phát ban)",
            "PT/INR (nếu dùng với warfarin)"
        ],
        "precautions": [
            "CHỐNG CHỈ ĐỊNH ở phụ nữ có thai (category D) - gây răng vàng và ức chế xương ở thai nhi",
            "Buồn nôn, nôn phổ biến - có thể cần điều trị hỗ trợ",
            "Uống khi đói (4 giờ trước hoặc 2 giờ sau ăn) để tăng hấp thu (PO)",
            "Tránh antacid, sắt, canxi, magie, nhôm trong 4 giờ (PO)",
            "Tránh ánh nắng mặt trời (nhạy cảm ánh sáng)",
            "Theo dõi INR nếu dùng với warfarin",
            "Trẻ em <18 tuổi - chưa được nghiên cứu"
        ],
        "pharmacokinetics": {
            "half_life": "16 giờ",
            "onset": "Ngay lập tức sau khi tiêm IV, 1-2 giờ sau khi uống (PO)",
            "duration": "12-24 giờ (dùng 1-2 lần/ngày)",
            "protein_binding": "20-30%",
            "metabolism": "Chuyển hóa một phần ở gan (CYP3A4)",
            "clearance": "Thải trừ qua gan (50%) và thận (50%)"
        },
        "storage": "Bảo quản bột khô (IV) và viên nén (PO) ở nhiệt độ phòng (20-25°C). Sau khi pha (IV): bảo quản ở nhiệt độ phòng 6 giờ, hoặc trong tủ lạnh 24 giờ. Không đông lạnh.",
        "black_box_warnings": "CHỐNG CHỈ ĐỊNH ở phụ nữ có thai (category D). Omadacycline gây răng vàng và ức chế xương ở thai nhi. Không dùng trong thai kỳ.",
        "drug_interactions": {
            "major": [
                {
                    "drug": "Warfarin",
                    "mechanism": "Omadacycline có thể ức chế tổng hợp vitamin K phụ thuộc vào hệ vi khuẩn đường ruột, làm giảm sản xuất các yếu tố đông máu phụ thuộc vitamin K.",
                    "effect": "Tăng INR, tăng nguy cơ chảy máu",
                    "management": "Theo dõi INR thường xuyên (ít nhất 2-3 lần/tuần khi bắt đầu dùng omadacycline). Có thể cần giảm liều warfarin."
                }
            ],
            "moderate": [
                {
                    "drug": "Antacid, Sắt, Canxi, Magie, Nhôm (PO)",
                    "mechanism": "Các cation (canxi, magie, nhôm, sắt) tạo phức hợp không hòa tan với omadacycline, giảm hấp thu.",
                    "effect": "Giảm hấp thu omadacycline, giảm hiệu quả",
                    "management": "Tránh dùng cùng lúc. Cách ít nhất 4 giờ trước hoặc sau khi uống omadacycline."
                },
                {
                    "drug": "Thuốc tránh thai đường uống",
                    "mechanism": "Tetracycline có thể làm giảm hệ vi khuẩn đường ruột, làm giảm tái hấp thu estrogen từ đường ruột.",
                    "effect": "Giảm hiệu quả thuốc tránh thai (hiếm, nhưng có thể xảy ra)",
                    "management": "Khuyến cáo sử dụng biện pháp tránh thai bổ sung (bao cao su) trong khi dùng omadacycline và 7 ngày sau khi ngừng."
                }
            ],
            "minor": []
        },
        "contraindications": {
            "tuyệt_đối": [
                "Dị ứng omadacycline hoặc tetracycline",
                "Phụ nữ có thai - CHỐNG CHỈ ĐỊNH (category D, gây răng vàng và ức chế xương ở thai nhi)"
            ],
            "tương_đối": [
                "Trẻ em <18 tuổi - chưa được nghiên cứu",
                "Phụ nữ đang cho con bú - thận trọng",
                "Suy gan nặng - điều chỉnh liều",
                "Nhạy cảm với ánh sáng - tránh ánh nắng mặt trời"
            ]
        },
        "pregnancy_lactation": {
            "fda_category": "D",
            "pregnancy_details": "Omadacycline là thuốc phân loại D. CHỐNG CHỈ ĐỊNH trong thai kỳ. Tetracycline gây răng vàng và ức chế xương ở thai nhi. Không dùng trong thai kỳ.",
            "lactation": {
                "safety": "Compatible with Caution",
                "details": "Omadacycline bài tiết vào sữa mẹ. Tetracycline có thể gây răng vàng và ức chế xương ở trẻ bú mẹ. Thận trọng khi cho con bú.",
                "recommendation": "Tránh dùng khi cho con bú. Nếu bắt buộc, theo dõi trẻ về dấu hiệu răng vàng và ức chế xương."
            }
        },
        "hepatic_adjustment": {
            "mild": "Không cần điều chỉnh liều",
            "moderate": "Giảm liều 25-50%",
            "severe": "Giảm liều 50% hoặc tăng khoảng cách liều",
            "notes": "Omadacycline chuyển hóa một phần ở gan (CYP3A4) và thải trừ qua gan (50%). Suy gan nặng có thể làm tích lũy omadacycline, tăng nguy cơ tác dụng phụ. Cần điều chỉnh liều ở suy gan nặng."
        },
        "overdose_management": {
            "symptoms": [
                "Buồn nôn, nôn nặng",
                "Tiêu chảy nặng",
                "Tăng transaminase",
                "Nhạy cảm với ánh sáng nặng"
            ],
            "antidote": "Không có antidote đặc hiệu. Điều trị hỗ trợ.",
            "treatment": [
                "Ngừng ngay omadacycline",
                "Điều trị buồn nôn, nôn: Antiemetic (ondansetron, metoclopramide)",
                "Điều trị tiêu chảy: Bù dịch, điện giải",
                "Theo dõi: Dấu hiệu sinh tồn, chức năng gan"
            ],
            "monitoring": "Theo dõi dấu hiệu sinh tồn, chức năng gan (ALT, AST) trong ít nhất 24-48 giờ."
        },
        "reversal_agents": {"available": False, "agents": [], "notes": "Không có antidote đặc hiệu. Điều trị chủ yếu là hỗ trợ và điều trị triệu chứng. Ngừng thuốc ngay nếu có độc tính gan nặng."},
        "administration_instructions": {
            "oral": {
                "with_food": "Uống khi đói (4 giờ trước hoặc 2 giờ sau ăn) để tăng hấp thu",
                "timing": "Dạng PO: Liều nạp 300mg x 2 lần/ngày (ngày đầu), sau đó 300mg x 1 lần/ngày. Uống đều đặn, cách đều nhau trong ngày."
            },
            "iv": {
                "reconstitution": "Pha với NS (0.9% NaCl) hoặc D5W (5% Dextrose). Nồng độ pha: 1-2mg/ml. Pha 100mg trong 100ml = 1mg/ml. Pha 200mg trong 250ml = 0.8mg/ml. Truyền trong 60 phút.",
                "infusion_rate": "Truyền IV trong 60 phút. Tốc độ: 100ml/60 phút = ~1.7ml/phút.",
                "compatibility": ["NS (0.9% NaCl)", "D5W (5% Dextrose)"],
                "incompatibility": [
                    "Antacid, sắt, canxi, magie, nhôm - giảm hấp thu (nếu có dạng uống)",
                    "Penicillin - giảm hiệu quả penicillin"
                ],
                "notes": "QUAN TRỌNG: 1) Dạng IV: liều nạp 200mg, sau đó 100mg mỗi 12 giờ, 2) Dạng PO: liều nạp 300mg x 2 lần/ngày (ngày đầu), sau đó 300mg x 1 lần/ngày, 3) CHỐNG CHỈ ĐỊNH ở phụ nữ có thai, 4) Buồn nôn, nôn phổ biến, 5) Uống khi đói (PO), 6) Tránh antacid, sắt, canxi trong 4 giờ (PO), 7) Tránh ánh nắng mặt trời."
            }
        },
        "references": {
            "primary_sources": [
                "FDA Drug Label - Omadacycline (Nuzyra)",
                "UpToDate - Omadacycline: Drug Information",
                "Medscape - Omadacycline Drug Reference",
                "IDSA Guidelines - Community-Acquired Pneumonia",
                "IDSA Guidelines - Skin and Soft Tissue Infections"
            ],
            "last_updated": "2025-02-18",
            "evidence_level": "A - Dựa trên FDA drug labels, IDSA guidelines, và dữ liệu lâm sàng từ nhiều nguồn"
        },
        "risk_flags": {
            "high_alert": False,
            "narrow_therapeutic_index": False,
            "icu_critical_care_only": False,
            "bleeding_risk": "Low",
            "organ_toxicity": {"hepatic": "Low", "gastrointestinal": "Moderate"}
        },
        "guideline_tags": [
            "IDSA Guidelines - Community-Acquired Pneumonia",
            "IDSA Guidelines - Skin and Soft Tissue Infections",
            "IDSA Guidelines - Methicillin-Resistant Staphylococcus aureus Infections"
        ]
    },
    
    "Defencath": {
                "group": "FDA Approved 2023",
                "vietnamese_name": "Taurolidine/heparin, Defencath",
                "administration": [
                        "IV",
                ],
                "indications": [
                        "To reduce the incidence of catheter-related bloodstream infections in adults with kidney failure receiving chronic hemodialysis through a central venous catheter",
                ],
                "contraindications": [
                        "Dị ứng taurolidine, heparin, hoặc bất kỳ thành phần nào",
                        "Giảm tiểu cầu do heparin (HIT)",
                ],
                "dosage": {
                        "adult_standard": "4.5% taurolidine/5000 U/mL heparin lock solution, instil vào catheter sau mỗi lần lọc máu",
                        "adult_loading": "Instil vào catheter sau mỗi lần lọc máu",
                        "notes": "FDA phê duyệt 2023. To reduce the incidence of catheter-related bloodstream infections in adults with kidney failure receiving chronic hemodialysis through a central venous catheter. Dùng như lock solution (dung dịch khóa catheter) để ngăn ngừa nhiễm trùng. Instil vào catheter sau mỗi lần lọc máu và để trong catheter giữa các lần lọc.",
                },
                "renal_adjustment": {
                        "normal": "Không cần chỉnh liều",
                        "30_60": "Không cần chỉnh liều (dùng cho bệnh nhân lọc máu)",
                        "under_30": "Không cần chỉnh liều (dùng cho bệnh nhân lọc máu)",
                },
                "side_effects": [
                        "Chảy máu - có thể xảy ra (do heparin)",
                        "Giảm tiểu cầu do heparin (HIT) - hiếm nhưng nghiêm trọng",
                        "Phản ứng tại chỗ - có thể xảy ra",
                        "Phản ứng dị ứng - hiếm nhưng có thể nghiêm trọng",
                        "Tăng men gan - hiếm",
                ],
                "interactions": [
                        "Thuốc chống đông: heparin trong Defencath có thể tăng nguy cơ chảy máu khi dùng với thuốc chống đông khác",
                        "Thuốc ảnh hưởng đến tiểu cầu: có thể tăng nguy cơ chảy máu",
                        "Thuốc chống kết tập tiểu cầu: có thể tăng nguy cơ chảy máu",
                ],
                "pregnancy": "C",
                "mechanism_of_action": "Defencath là sự kết hợp của taurolidine (4.5%) và heparin (5000 U/mL) được FDA phê duyệt 2023 để giảm tỷ lệ nhiễm trùng máu liên quan đến catheter ở bệnh nhân suy thận mạn tính đang lọc máu qua catheter tĩnh mạch trung tâm. Cơ chế: (1) Taurolidine: là một chất kháng khuẩn phổ rộng, hoạt động bằng cách tạo ra các chất trung gian có hoạt tính kháng khuẩn mạnh (methylol derivatives) khi tiếp xúc với vi khuẩn. Các chất này phá hủy thành tế bào vi khuẩn và ức chế sự phát triển của vi khuẩn, đặc biệt hiệu quả chống lại các vi khuẩn Gram-dương và Gram-âm, bao gồm cả các chủng kháng thuốc. Taurolidine cũng có tác dụng chống nấm và chống biofilm, giúp ngăn ngừa sự hình thành biofilm trên catheter. (2) Heparin: là một chất chống đông, hoạt động bằng cách tăng cường hoạt động của antithrombin III, ức chế các yếu tố đông máu và ngăn ngừa sự hình thành cục máu đông trong catheter. Sự kết hợp này giúp vừa ngăn ngừa nhiễm trùng (taurolidine) vừa ngăn ngừa tắc nghẽn catheter do cục máu đông (heparin). Defencath được dùng như lock solution, instil vào catheter sau mỗi lần lọc máu và để trong catheter giữa các lần lọc để duy trì tác dụng kháng khuẩn và chống đông.",
                "monitoring": [
                        "Tỷ lệ nhiễm trùng máu liên quan đến catheter - mục tiêu giảm tỷ lệ nhiễm trùng",
                        "Dấu hiệu chảy máu - do heparin, đặc biệt khi dùng với thuốc chống đông khác",
                        "Số lượng tiểu cầu - theo dõi dấu hiệu HIT (giảm tiểu cầu do heparin)",
                        "Dấu hiệu HIT - hiếm nhưng nghiêm trọng, cần ngừng heparin ngay",
                        "Chức năng gan - định kỳ",
                        "Phản ứng tại chỗ - khi instil vào catheter",
                ],
                "precautions": [
                        "Dị ứng taurolidine, heparin, hoặc bất kỳ thành phần nào",
                        "NGUY CƠ CHẢY MÁU - heparin trong Defencath có thể tăng nguy cơ chảy máu, đặc biệt khi dùng với thuốc chống đông khác",
                        "GIẢM TIỂU CẦU DO HEPARIN (HIT) - hiếm nhưng nghiêm trọng, cần ngừng heparin ngay nếu có dấu hiệu",
                        "Thận trọng ở bệnh nhân có nguy cơ chảy máu cao",
                        "Thận trọng khi dùng với thuốc chống đông hoặc thuốc chống kết tập tiểu cầu",
                        "Chỉ dùng như lock solution trong catheter, không truyền vào máu",
                        "Theo dõi chặt chẽ dấu hiệu chảy máu và HIT",
                ],
                "pharmacokinetics": {
                        "half_life": "Taurolidine: ngắn (phân hủy nhanh tại chỗ); Heparin: khoảng 1-2 giờ",
                        "onset": "Nhanh (tác dụng tại chỗ ngay sau khi instil)",
                        "duration": "Kéo dài (duy trì trong catheter giữa các lần lọc máu)",
                        "protein_binding": "Taurolidine: thấp; Heparin: gắn với antithrombin III",
                        "metabolism": "Taurolidine: phân hủy tại chỗ thành các chất trung gian; Heparin: chuyển hóa một phần trong gan",
                        "clearance": "Taurolidine: thải trừ qua thận; Heparin: thải trừ qua hệ thống reticuloendothelial và thận"
                },
                "storage": "Bảo quản ở nhiệt độ phòng (20-25°C), tránh đông lạnh. Bảo vệ khỏi ánh sáng. Không lắc. Sử dụng ngay sau khi mở.",
                "black_box_warnings": "Không có black box warning. Tuy nhiên, cần cảnh báo về nguy cơ chảy máu do heparin và HIT.",
                "drug_interactions": {
                        "major": [],
                        "moderate": [
                                {
                                        "drug": "Thuốc chống đông (warfarin, apixaban, rivaroxaban, etc.)",
                                        "mechanism": "Heparin trong Defencath tăng tác dụng chống đông",
                                        "effect": "Tăng nguy cơ chảy máu",
                                        "management": "Theo dõi chặt chẽ dấu hiệu chảy máu, có thể cần điều chỉnh liều thuốc chống đông"
                                }
                        ],
                        "minor": [],
                },
                "contraindications_detail": {
                        "tuyệt_đối": [
                                "Dị ứng taurolidine, heparin, hoặc bất kỳ thành phần nào",
                                "Giảm tiểu cầu do heparin (HIT)",
                        ],
                        "tương_đối": [
                                "Nguy cơ chảy máu cao - thận trọng",
                                "Đang dùng thuốc chống đông - thận trọng, theo dõi chặt chẽ",
                        ],
                },
                "pregnancy_lactation": {
                        "fda_category": "C",
                        "pregnancy_details": "Category C - có nguy cơ cho thai nhi. Taurolidine và heparin chưa có dữ liệu đầy đủ về an toàn trong thai kỳ. Heparin không qua nhau thai nhưng có thể gây chảy máu. Chỉ dùng khi lợi ích vượt trội nguy cơ.",
                        "lactation": {
                                "safety": "Unknown",
                                "details": "Chưa biết có bài tiết vào sữa mẹ hay không. Heparin không bài tiết vào sữa mẹ do phân tử lớn.",
                                "recommendation": "Thận trọng khi cho con bú. Cân nhắc ngừng cho con bú hoặc ngừng thuốc tùy theo tình huống lâm sàng.",
                        },
                },
                "hepatic_adjustment": {
                        "mild": "Không đổi",
                        "moderate": "Không đổi",
                        "severe": "Thận trọng, dữ liệu hạn chế",
                        "notes": "Chưa có nghiên cứu cụ thể về điều chỉnh liều ở bệnh nhân suy gan. Thận trọng ở bệnh nhân suy gan nặng.",
                },
                "overdose_management": {
                        "symptoms": [
                                "Tăng nguy cơ chảy máu (do heparin)",
                                "Phản ứng dị ứng",
                        ],
                        "antidote": "Protamine sulfate có thể đảo ngược tác dụng của heparin",
                        "treatment": [
                                "Ngừng thuốc ngay lập tức",
                                "Xử trí chảy máu nếu có",
                                "Protamine sulfate nếu chảy máu nặng do heparin",
                                "Điều trị hỗ trợ theo triệu chứng",
                        ],
                        "monitoring": "Theo dõi dấu hiệu sinh tồn, dấu hiệu chảy máu, số lượng tiểu cầu",
                },
                "reversal_agents": {
                        "available": True,
                        "agents": ["Protamine sulfate (cho heparin)"],
                },
                "administration_instructions": {
                        "iv": {
                                "method": "Instil vào catheter như lock solution",
                                "timing": "Sau mỗi lần lọc máu",
                                "volume": "Đủ để lấp đầy catheter",
                                "notes": "Instil vào catheter sau mỗi lần lọc máu và để trong catheter giữa các lần lọc. Rút bỏ trước khi lọc máu tiếp theo. Chỉ dùng như lock solution, không truyền vào máu. Không trộn với các thuốc khác.",
                        },
                },
                "references": {
                        "primary_sources": [
                                "FDA Drug Label - Taurolidine (Defencath)",
                                "FDA Approval Date: 2023",
                                "FDA-approved use: To reduce the incidence of catheter-related bloodstream infections in adults with kidney failure receiving chronic hemodialysis through a central venous catheter",
                        ],
                        "last_updated": "2026-01-15",
                        "evidence_level": "A - FDA-approved 2023",
                },
                "risk_flags": {
                        "high_alert": False,
                        "narrow_therapeutic_index": False,
                        "bleeding_risk": False,
                        "organ_toxicity": [],
                        "qt_prolongation": False,
                        "hepatotoxicity": False,
                        "nephrotoxicity": False,
                        "requires_monitoring": [
                                "Clinical response",
                                "Adverse effects",
                        ],
                },
                "guideline_tags": [
                        "FDA Drug Information - Taurolidine (Defencath)",
                ],
                "last_updated": "2026-01-15",
        },
    "Xolremdi": {
                "group": "FDA Approved 2024",
                "vietnamese_name": "Mavorixafor, Xolremdi",
                "administration": [
                        "PO",
                ],
                "indications": [
                        "To treat WHIM syndrome (warts, hypogammaglobulinemia, infections and myelokathexis)",
                ],
                "contraindications": [
                        "Dị ứng mavorixafor hoặc bất kỳ thành phần nào",
                ],
                "dosage": {
                        "adult_standard": "400mg PO x 2 lần/ngày",
                        "adult_loading": "Bắt đầu với 400mg PO x 2 lần/ngày",
                        "notes": "FDA phê duyệt 2024. To treat WHIM syndrome (warts, hypogammaglobulinemia, infections and myelokathexis). Uống với thức ăn. Mavorixafor là chất đối kháng CXCR4, giúp cải thiện chức năng miễn dịch ở bệnh nhân WHIM syndrome.",
                },
                "renal_adjustment": {
                        "normal": "400mg PO x 2 lần/ngày",
                        "30_60": "400mg PO x 2 lần/ngày (không cần chỉnh liều)",
                        "under_30": "Thận trọng, dữ liệu hạn chế, có thể cần giảm liều",
                },
                "side_effects": [
                        "Tiêu chảy - phổ biến",
                        "Buồn nôn - phổ biến",
                        "Đau bụng - phổ biến",
                        "Đau đầu - phổ biến",
                        "Mệt mỏi - phổ biến",
                        "Nôn - có thể xảy ra",
                        "Chóng mặt - có thể xảy ra",
                        "Phát ban - có thể xảy ra",
                        "Tăng men gan (ALT, AST) - có thể xảy ra",
                ],
                "interactions": [
                        "Thuốc ức chế CYP3A4: có thể tăng nồng độ mavorixafor (theo dõi)",
                        "Thuốc cảm ứng CYP3A4: có thể giảm nồng độ mavorixafor (theo dõi)",
                        "Thuốc ảnh hưởng đến hệ miễn dịch: có thể tương tác",
                ],
                "pregnancy": "C",
                "mechanism_of_action": "Mavorixafor là một chất đối kháng thụ thể CXCR4 được FDA phê duyệt 2024 để điều trị WHIM syndrome (warts, hypogammaglobulinemia, infections and myelokathexis). Cơ chế: WHIM syndrome là một rối loạn miễn dịch di truyền hiếm gặp do đột biến gen CXCR4, dẫn đến tăng hoạt động của thụ thể CXCR4. CXCR4 là một chemokine receptor quan trọng trong hệ miễn dịch, có vai trò trong sự di chuyển và trưởng thành của tế bào bạch cầu, đặc biệt là bạch cầu trung tính (neutrophils) và tế bào B. Trong WHIM syndrome, đột biến CXCR4 dẫn đến sự giữ lại bất thường của bạch cầu trung tính trong tủy xương (myelokathexis), giảm số lượng bạch cầu trung tính trong máu ngoại vi, và tăng nguy cơ nhiễm trùng. Mavorixafor hoạt động bằng cách đối kháng với thụ thể CXCR4, ức chế hoạt động quá mức của nó, do đó giúp giải phóng bạch cầu trung tính từ tủy xương vào máu ngoại vi. Điều này làm tăng số lượng bạch cầu trung tính trong máu, cải thiện chức năng miễn dịch, giảm tần suất nhiễm trùng, và cải thiện các triệu chứng khác của WHIM syndrome như mụn cóc (warts) và hypogammaglobulinemia. Mavorixafor được dùng đường uống và cần uống với thức ăn để tăng hấp thu.",
                "monitoring": [
                        "Số lượng bạch cầu trung tính - mục tiêu tăng số lượng bạch cầu trung tính trong máu",
                        "Tần suất nhiễm trùng - mục tiêu giảm tần suất nhiễm trùng",
                        "Chức năng gan (ALT, AST) - định kỳ",
                        "Đáp ứng điều trị: cải thiện triệu chứng WHIM syndrome",
                        "Chức năng thận - định kỳ",
                        "Công thức máu đầy đủ - định kỳ",
                ],
                "precautions": [
                        "Dị ứng mavorixafor hoặc bất kỳ thành phần nào",
                        "Tăng men gan - có thể xảy ra, theo dõi chức năng gan định kỳ",
                        "Suy gan - thận trọng, theo dõi chức năng gan",
                        "Suy thận nặng - thận trọng, có thể cần giảm liều",
                        "Uống với thức ăn để tăng hấp thu",
                        "Thận trọng khi dùng với thuốc ức chế hoặc cảm ứng CYP3A4",
                ],
                "pharmacokinetics": {
                        "half_life": "Khoảng 8-12 giờ",
                        "onset": "Vài tuần đến vài tháng (tác dụng lâm sàng trên WHIM syndrome)",
                        "duration": "12 giờ (uống mỗi 12 giờ)",
                        "protein_binding": "Khoảng 95-98%",
                        "metabolism": "Chuyển hóa chủ yếu trong gan qua CYP3A4",
                        "clearance": "Thải trừ chủ yếu qua gan (khoảng 70%) và một phần qua thận"
                },
                "storage": "Bảo quản ở nhiệt độ phòng (20-25°C), tránh ẩm, tránh ánh sáng. Bảo quản trong bao bì gốc. Để xa tầm tay trẻ em.",
                "black_box_warnings": "Không có black box warning.",
                "drug_interactions": {
                        "major": [],
                        "moderate": [
                                {
                                        "drug": "Thuốc ức chế CYP3A4 (ketoconazole, itraconazole, clarithromycin, etc.)",
                                        "mechanism": "Ức chế CYP3A4, giảm chuyển hóa mavorixafor",
                                        "effect": "Tăng nồng độ mavorixafor",
                                        "management": "Theo dõi tác dụng phụ, có thể cần giảm liều mavorixafor"
                                },
                                {
                                        "drug": "Thuốc cảm ứng CYP3A4 (rifampin, carbamazepine, phenytoin, etc.)",
                                        "mechanism": "Cảm ứng CYP3A4, tăng chuyển hóa mavorixafor",
                                        "effect": "Giảm nồng độ và hiệu quả của mavorixafor",
                                        "management": "Theo dõi đáp ứng điều trị, có thể cần tăng liều mavorixafor"
                                }
                        ],
                        "minor": [],
                },
                "contraindications_detail": {
                        "tuyệt_đối": [
                                "Dị ứng mavorixafor hoặc bất kỳ thành phần nào",
                        ],
                        "tương_đối": [
                                "Suy gan nặng - thận trọng",
                                "Suy thận nặng - thận trọng, có thể cần giảm liều",
                        ],
                },
                "pregnancy_lactation": {
                        "fda_category": "C",
                        "pregnancy_details": "Category C - có nguy cơ cho thai nhi. Mavorixafor chưa có dữ liệu đầy đủ về an toàn trong thai kỳ. Chỉ dùng khi lợi ích vượt trội nguy cơ.",
                        "lactation": {
                                "safety": "Unknown",
                                "details": "Chưa biết có bài tiết vào sữa mẹ hay không. Có thể ảnh hưởng đến hệ miễn dịch của trẻ sơ sinh.",
                                "recommendation": "Thận trọng khi cho con bú. Cân nhắc ngừng cho con bú hoặc ngừng thuốc tùy theo tình huống lâm sàng.",
                        },
                },
                "hepatic_adjustment": {
                        "mild": "Không đổi",
                        "moderate": "Thận trọng, theo dõi chức năng gan",
                        "severe": "Thận trọng, dữ liệu hạn chế, có thể cần giảm liều",
                        "notes": "Mavorixafor chuyển hóa chủ yếu trong gan. Thận trọng ở bệnh nhân suy gan nặng, theo dõi chức năng gan và có thể cần giảm liều.",
                },
                "overdose_management": {
                        "symptoms": [
                                "Tăng tác dụng phụ (tiêu chảy, buồn nôn, đau đầu)",
                                "Tăng men gan",
                        ],
                        "antidote": "Không có antidote đặc hiệu",
                        "treatment": [
                                "Ngừng thuốc ngay lập tức",
                                "Điều trị hỗ trợ theo triệu chứng",
                                "Theo dõi chức năng gan",
                        ],
                        "monitoring": "Theo dõi dấu hiệu sinh tồn, chức năng gan, tác dụng phụ",
                },
                "reversal_agents": {
                        "available": False,
                        "agents": [],
                },
                "administration_instructions": {
                        "oral": {
                                "with_food": "Uống với thức ăn để tăng hấp thu",
                                "timing": "Uống mỗi 12 giờ (2 lần/ngày), cách đều nhau",
                                "notes": "Uống đủ nước trong khi điều trị. Không bẻ hoặc nghiền viên. Uống với thức ăn để tăng hấp thu và giảm tác dụng phụ đường tiêu hóa.",
                        },
                },
                "references": {
                        "primary_sources": [
                                "FDA Drug Label - Mavorixafor (Xolremdi)",
                                "FDA Approval Date: 2024",
                                "FDA-approved use: To treat WHIM syndrome (warts, hypogammaglobulinemia, infections and myelokathexis)",
                        ],
                        "last_updated": "2026-01-15",
                        "evidence_level": "A - FDA-approved 2024",
                },
                "risk_flags": {
                        "high_alert": False,
                        "narrow_therapeutic_index": False,
                        "bleeding_risk": False,
                        "organ_toxicity": [],
                        "qt_prolongation": False,
                        "hepatotoxicity": False,
                        "nephrotoxicity": False,
                        "requires_monitoring": [
                                "Clinical response",
                                "Adverse effects",
                        ],
                },
                "guideline_tags": [
                        "FDA Drug Information - Mavorixafor (Xolremdi)",
                ],
                "last_updated": "2026-01-15",
        },
    "Nuzolvence": {
                "group": "FDA Approved 2025",
                "vietnamese_name": "Zoliflodacin, Nuzolvence",
                "administration": [
                        "PO",
                ],
                "indications": [
                        "To treat uncomplicated urogenital gonorrhea due to Neisseria gonorrhoeae",
                ],
                "contraindications": [
                        "Dị ứng zoliflodacin hoặc bất kỳ thành phần nào",
                ],
                "dosage": {
                        "adult_standard": "3g PO liều duy nhất",
                        "adult_loading": "3g PO liều duy nhất",
                        "notes": "FDA phê duyệt 2025. To treat uncomplicated urogenital gonorrhea due to Neisseria gonorrhoeae. Uống với thức ăn hoặc không cần thức ăn. Đây là kháng sinh mới thuộc nhóm spiropyrimidinetrione, ức chế DNA gyrase.",
                },
                "renal_adjustment": {
                        "normal": "3g PO liều duy nhất",
                        "30_60": "3g PO liều duy nhất (không cần chỉnh liều)",
                        "under_30": "Thận trọng, dữ liệu hạn chế",
                },
                "side_effects": [
                        "Tiêu chảy - phổ biến",
                        "Buồn nôn - phổ biến",
                        "Đau bụng - phổ biến",
                        "Đau đầu - phổ biến",
                        "Nôn - có thể xảy ra",
                        "Chóng mặt - có thể xảy ra",
                        "Phát ban - có thể xảy ra",
                        "Viêm đại tràng do C. difficile - có thể xảy ra, nghiêm trọng",
                        "Phản ứng dị ứng - hiếm nhưng có thể nghiêm trọng (phản vệ)",
                ],
                "interactions": [
                        "Thuốc chống acid (antacid): có thể giảm hấp thu zoliflodacin (uống cách nhau ít nhất 2 giờ)",
                        "Thuốc chứa cation (sắt, canxi, magie, kẽm): có thể giảm hấp thu zoliflodacin (uống cách nhau ít nhất 2 giờ)",
                        "Thuốc ức chế tủy xương: có thể tăng nguy cơ giảm bạch cầu",
                ],
                "pregnancy": "C",
                "mechanism_of_action": "Zoliflodacin là một kháng sinh mới thuộc nhóm spiropyrimidinetrione được FDA phê duyệt 2025 để điều trị uncomplicated urogenital gonorrhea do Neisseria gonorrhoeae. Cơ chế: Zoliflodacin hoạt động bằng cách ức chế DNA gyrase, một enzyme quan trọng trong quá trình sao chép DNA của vi khuẩn. DNA gyrase (một loại topoisomerase type II) có chức năng tháo xoắn DNA trong quá trình sao chép và phiên mã, giúp giải phóng stress xoắn và cho phép DNA polymerase tiếp tục quá trình sao chép. Zoliflodacin gắn với DNA gyrase và ức chế hoạt động của nó, dẫn đến sự tích tụ các vết nứt DNA và phá hủy DNA của vi khuẩn, cuối cùng gây chết vi khuẩn. Zoliflodacin có cơ chế tác dụng tương tự fluoroquinolones nhưng có cấu trúc hóa học khác (spiropyrimidinetrione), giúp hoạt động hiệu quả chống lại các chủng Neisseria gonorrhoeae kháng fluoroquinolone và các kháng sinh khác. Zoliflodacin có phổ kháng khuẩn hẹp, chủ yếu hoạt động chống lại Neisseria gonorrhoeae, và được dùng như liều duy nhất (single-dose therapy) để điều trị lậu không biến chứng. Thuốc được dùng đường uống và tập trung cao trong đường tiết niệu và sinh dục, lý tưởng cho điều trị lậu.",
                "monitoring": [
                        "Đáp ứng điều trị: giảm triệu chứng, xét nghiệm âm tính sau điều trị",
                        "Dấu hiệu tiêu chảy - đặc biệt quan trọng do nguy cơ viêm đại tràng do C. difficile",
                        "Dấu hiệu phản ứng dị ứng - hiếm nhưng có thể nghiêm trọng",
                        "Chức năng thận - trước điều trị",
                        "Chức năng gan - định kỳ",
                        "Công thức máu đầy đủ - định kỳ",
                ],
                "precautions": [
                        "Dị ứng zoliflodacin hoặc bất kỳ thành phần nào",
                        "VIÊM ĐẠI TRÀNG DO C. DIFFICILE - có thể xảy ra, nghiêm trọng, có thể xuất hiện sau khi ngừng thuốc",
                        "Suy thận nặng - thận trọng, dữ liệu hạn chế",
                        "Suy gan - thận trọng, theo dõi chức năng gan",
                        "Tiêu chảy - ngừng thuốc nếu nghi ngờ viêm đại tràng do C. difficile",
                        "Tránh dùng cùng với thuốc chống acid hoặc thuốc chứa cation (uống cách nhau ít nhất 2 giờ)",
                        "Có thể uống với thức ăn hoặc không cần thức ăn",
                        "Chỉ điều trị lậu không biến chứng, không dùng cho lậu có biến chứng",
                ],
                "pharmacokinetics": {
                        "half_life": "Khoảng 8-12 giờ",
                        "onset": "Nhanh (bắt đầu tác dụng kháng khuẩn sau khi hấp thu)",
                        "duration": "Kéo dài (liều duy nhất)",
                        "protein_binding": "Khoảng 30-40%",
                        "metabolism": "Chuyển hóa một phần trong gan qua CYP450 enzymes",
                        "clearance": "Thải trừ chủ yếu qua thận (khoảng 60-70% không đổi trong nước tiểu) và một phần qua gan"
                },
                "storage": "Bảo quản ở nhiệt độ phòng (20-25°C), tránh ẩm, tránh ánh sáng. Bảo quản trong bao bì gốc. Để xa tầm tay trẻ em.",
                "black_box_warnings": "Không có black box warning. Tuy nhiên, cần cảnh báo về nguy cơ viêm đại tràng do C. difficile.",
                "drug_interactions": {
                        "major": [],
                        "moderate": [
                                {
                                        "drug": "Thuốc chống acid, thuốc chứa cation (sắt, canxi, magie, kẽm)",
                                        "mechanism": "Giảm hấp thu zoliflodacin do tạo phức hợp",
                                        "effect": "Giảm nồng độ và hiệu quả của zoliflodacin",
                                        "management": "Uống cách nhau ít nhất 2 giờ"
                                }
                        ],
                        "minor": [],
                },
                "contraindications_detail": {
                        "tuyệt_đối": [
                                "Dị ứng zoliflodacin hoặc bất kỳ thành phần nào",
                        ],
                        "tương_đối": [
                                "Suy thận nặng - thận trọng, dữ liệu hạn chế",
                                "Suy gan nặng - thận trọng",
                        ],
                },
                "pregnancy_lactation": {
                        "fda_category": "C",
                        "pregnancy_details": "Category C - có nguy cơ cho thai nhi. Zoliflodacin chưa có dữ liệu đầy đủ về an toàn trong thai kỳ. Chỉ dùng khi lợi ích vượt trội nguy cơ.",
                        "lactation": {
                                "safety": "Unknown",
                                "details": "Chưa biết có bài tiết vào sữa mẹ hay không. Có thể ảnh hưởng đến hệ vi khuẩn đường ruột của trẻ sơ sinh.",
                                "recommendation": "Thận trọng khi cho con bú. Cân nhắc ngừng cho con bú hoặc ngừng thuốc tùy theo tình huống lâm sàng.",
                        },
                },
                "hepatic_adjustment": {
                        "mild": "Không đổi",
                        "moderate": "Thận trọng, theo dõi chức năng gan",
                        "severe": "Thận trọng, dữ liệu hạn chế",
                        "notes": "Chưa có nghiên cứu cụ thể về điều chỉnh liều ở bệnh nhân suy gan. Thận trọng ở bệnh nhân suy gan nặng, theo dõi chức năng gan.",
                },
                "overdose_management": {
                        "symptoms": [
                                "Tăng tác dụng phụ (tiêu chảy, buồn nôn, nôn)",
                                "Tăng nguy cơ viêm đại tràng do C. difficile",
                        ],
                        "antidote": "Không có antidote đặc hiệu",
                        "treatment": [
                                "Ngừng thuốc ngay lập tức",
                                "Điều trị hỗ trợ theo triệu chứng",
                                "Xử trí viêm đại tràng do C. difficile nếu có",
                        ],
                        "monitoring": "Theo dõi dấu hiệu sinh tồn, dấu hiệu tiêu chảy, phản ứng dị ứng",
                },
                "reversal_agents": {
                        "available": False,
                        "agents": [],
                },
                "administration_instructions": {
                        "oral": {
                                "with_food": "Có thể uống với thức ăn hoặc không cần thức ăn",
                                "timing": "Liều duy nhất (single dose)",
                                "notes": "Uống đủ nước trong khi điều trị. Tránh dùng cùng với thuốc chống acid hoặc thuốc chứa cation (sắt, canxi, magie, kẽm) - uống cách nhau ít nhất 2 giờ. Không bẻ hoặc nghiền viên.",
                        },
                },
                "references": {
                        "primary_sources": [
                                "FDA Drug Label - Zoliflodacin (Nuzolvence)",
                                "FDA Approval Date: 2025",
                                "FDA-approved use: To treat uncomplicated urogenital gonorrhea due to Neisseria gonorrhoeae",
                        ],
                        "last_updated": "2026-01-15",
                        "evidence_level": "A - FDA-approved 2025",
                },
                "risk_flags": {
                        "high_alert": False,
                        "narrow_therapeutic_index": False,
                        "bleeding_risk": False,
                        "organ_toxicity": [],
                        "qt_prolongation": False,
                        "hepatotoxicity": False,
                        "nephrotoxicity": False,
                        "requires_monitoring": [
                                "Clinical response",
                                "Adverse effects",
                        ],
                },
                "guideline_tags": [
                        "FDA Drug Information - Zoliflodacin (Nuzolvence)",
                ],
                "last_updated": "2026-01-15",
        },
}

__all__ = ['OTHER_ANTIBIOTICS']

