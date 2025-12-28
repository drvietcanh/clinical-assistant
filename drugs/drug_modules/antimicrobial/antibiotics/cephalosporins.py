"""
Cephalosporin Antibiotics
1st-5th Generation Cephalosporins
"""

CEPHALOSPORIN_ANTIBIOTICS = {
    "Cefazolin": {
        "group": "Antibiotic - Cephalosporin (1st Generation)",
        "vietnamese_name": "Cefazolin, Ancef, Kefzol",
        "administration": ["IV", "IM"],
        "indications": [
            "Dự phòng phẫu thuật",
            "Nhiễm khuẩn da và mô mềm",
            "Nhiễm khuẩn đường tiết niệu",
            "Viêm phổi cộng đồng",
            "Nhiễm khuẩn do Staphylococcus (MSSA)",
            "Nhiễm khuẩn do Streptococcus"
        ],
        "contraindications": [
            "Dị ứng cephalosporin",
            "Dị ứng penicillin nặng (phản ứng chéo 5-10%)"
        ],
        "dosage": {
            "adult_standard": "1-2g IV/IM mỗi 8 giờ",
            "adult_severe": "2g IV mỗi 6-8 giờ",
            "adult_prophylaxis": "1-2g IV x 1 liều trước phẫu thuật (30-60 phút trước)",
            "adult_prophylaxis_repeat": "1-2g IV mỗi 2-4 giờ trong phẫu thuật kéo dài",
            "notes": "Dự phòng phẫu thuật: liều đơn 1-2g trước phẫu thuật. Phẫu thuật kéo dài (>3-4 giờ): lặp lại mỗi 2-4 giờ."
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "1g IV mỗi 12 giờ",
            "under_30": "0.5-1g IV mỗi 12-24 giờ",
            "hemodialysis": "0.5-1g IV sau mỗi lần lọc máu"
        },
        "side_effects": [
            "Phát ban dị ứng",
            "Tiêu chảy",
            "Buồn nôn, nôn",
            "Viêm tĩnh mạch tại chỗ tiêm",
            "Tăng men gan (hiếm)",
            "Giảm bạch cầu (hiếm)"
        ],
        "interactions": [
            "Probenecid: tăng nồng độ cefazolin",
            "Warfarin: có thể tăng INR",
            "Aminoglycosides: không pha chung (bất hoạt)"
        ],
        "pregnancy": "B",
        "mechanism_of_action": "Cefazolin là cephalosporin thế hệ 1, kháng sinh beta-lactam. Ức chế tổng hợp thành tế bào vi khuẩn bằng cách gắn với penicillin-binding proteins (PBPs), ngăn chặn quá trình cross-linking của peptidoglycan. Phổ kháng khuẩn: Gram-dương mạnh (Staphylococcus aureus - MSSA, Staphylococcus epidermidis, Streptococcus pneumoniae, Streptococcus pyogenes), Gram-âm yếu (E. coli, Klebsiella, Proteus mirabilis - một số chủng), không hiệu quả với Enterococcus, Pseudomonas, kỵ khí. Đặc điểm: thời gian bán thải dài (1.5-2 giờ), dùng 3 lần/ngày, là lựa chọn hàng đầu cho dự phòng phẫu thuật.",
        "monitoring": [
            "Dấu hiệu dị ứng (phát ban, sốc phản vệ)",
            "Dấu hiệu nhiễm trùng (sốt, WBC)",
            "Cấy máu và cấy từ vị trí nhiễm trùng",
            "Chức năng thận (creatinine, eGFR) - điều chỉnh liều",
            "Chức năng gan (ALT, AST) - hiếm",
            "Công thức máu (CBC) - hiếm giảm bạch cầu"
        ],
        "precautions": [
            "Phản ứng chéo với penicillin (5-10%) - thận trọng ở bệnh nhân dị ứng penicillin",
            "Điều chỉnh liều theo chức năng thận (CrCl)",
            "Không pha chung với aminoglycosides (truyền riêng biệt)",
            "Dự phòng phẫu thuật: liều đơn 1-2g trước phẫu thuật (30-60 phút trước)",
            "Pha trong NS hoặc D5W, truyền IV trong 30 phút",
            "Theo dõi nhiễm C. difficile"
        ],
        "pharmacokinetics": {
            "half_life": "1.5-2 giờ",
            "onset": "Ngay lập tức sau khi truyền IV",
            "duration": "Liều q8h",
            "protein_binding": "80-85%",
            "clearance": "Chủ yếu qua thận (80-90% bài tiết nguyên dạng), cần điều chỉnh thận"
        },
        "storage": "Bảo quản bột khô ở nhiệt độ phòng (20-25°C). Sau khi pha: bảo quản ở nhiệt độ phòng 24 giờ, hoặc trong tủ lạnh 10 ngày.",
        "black_box_warnings": None,
        "drug_interactions": {
            "major": [],
            "moderate": [
                {
                    "drug": "Probenecid",
                    "mechanism": "Probenecid ức chế bài tiết cefazolin ở thận, tăng nồng độ cefazolin",
                    "effect": "Tăng nồng độ cefazolin, tăng thời gian bán thải",
                    "management": "Có thể dùng cùng để tăng nồng độ cefazolin. Theo dõi dấu hiệu độc tính."
                },
                {
                    "drug": "Warfarin",
                    "mechanism": "Cefazolin có thể ức chế tổng hợp vitamin K phụ thuộc vào hệ vi khuẩn đường ruột",
                    "effect": "Tăng INR, tăng nguy cơ chảy máu",
                    "management": "Theo dõi INR thường xuyên. Có thể cần giảm liều warfarin."
                }
            ],
            "minor": []
        },
        "contraindications": {
            "tuyệt_đối": [
                "Dị ứng cefazolin hoặc cephalosporin",
                "Dị ứng penicillin nặng (sốc phản vệ) - phản ứng chéo 5-10%"
            ],
            "tương_đối": [
                "Dị ứng penicillin nhẹ - thận trọng, có thể dùng nếu cần",
                "Suy thận nặng - giảm liều",
                "Tiền sử nhiễm C. difficile - tăng nguy cơ tái phát"
            ]
        },
        "pregnancy_lactation": {
            "fda_category": "B",
            "pregnancy_details": "Cefazolin là thuốc phân loại B. Các nghiên cứu trên động vật không cho thấy nguy cơ dị tật bẩm sinh. Các nghiên cứu trên người không cho thấy nguy cơ tăng dị tật bẩm sinh. Cephalosporin được sử dụng rộng rãi trong thai kỳ và có vẻ an toàn.",
            "lactation": {
                "safety": "Compatible",
                "details": "Cefazolin bài tiết vào sữa mẹ ở nồng độ thấp. Không có báo cáo về tác dụng phụ ở trẻ bú mẹ.",
                "recommendation": "Có thể dùng khi cho con bú."
            }
        },
        "hepatic_adjustment": {
            "mild": "Không cần điều chỉnh liều",
            "moderate": "Không cần điều chỉnh liều",
            "severe": "Không cần điều chỉnh liều (thải trừ chủ yếu qua thận)"
        },
        "overdose_management": {
            "symptoms": [
                "Co giật (hiếm, ở liều rất cao)",
                "Phản ứng dị ứng nặng",
                "Tăng men gan"
            ],
            "antidote": "Không có antidote đặc hiệu. Điều trị hỗ trợ.",
            "treatment": [
                "Ngừng cefazolin",
                "Điều trị co giật nếu có: Benzodiazepine",
                "Điều trị dị ứng nếu có: Epinephrine, antihistamine, corticosteroid",
                "Theo dõi chức năng thận, gan"
            ],
            "monitoring": "Theo dõi dấu hiệu sinh tồn, chức năng thận, gan trong 24-48 giờ."
        },
        "reversal_agents": None,
        "administration_instructions": {
            "oral": None,
            "iv": {
                "reconstitution": "Pha với NS hoặc D5W. Nồng độ pha: 100mg/ml (tối đa). Pha 1g trong 10ml = 100mg/ml, sau đó pha loãng trong 50-100ml NS hoặc D5W.",
                "infusion_rate": "Truyền IV trong 30 phút. Tốc độ: 50ml/30 phút = ~1.7ml/phút.",
                "compatibility": ["NS (0.9% NaCl)", "D5W (5% Dextrose)"],
                "incompatibility": [
                    "Aminoglycosides - bất hoạt, không pha chung",
                    "Amphotericin B - không tương thích"
                ],
                "notes": "QUAN TRỌNG: 1) Dự phòng phẫu thuật: liều đơn 1-2g trước phẫu thuật (30-60 phút), 2) Điều chỉnh liều theo chức năng thận, 3) Không pha chung với aminoglycosides, 4) Phản ứng chéo với penicillin (5-10%)."
            },
            "im": {
                "reconstitution": "Pha với NS hoặc lidocaine 1%. Nồng độ pha: 225mg/ml (tối đa).",
                "injection_site": "Cơ lớn (mông, đùi)",
                "notes": "IM: 1-2g mỗi 8 giờ. Tiêm sâu vào cơ. Có thể đau tại chỗ tiêm."
            }
        },
        "references": {
            "primary_sources": [
                "FDA Drug Label - Cefazolin",
                "IDSA Guidelines - Surgical Site Infection Prevention",
                "UpToDate - Cefazolin: Drug Information",
                "Medscape - Cefazolin Drug Reference"
            ],
            "last_updated": "2025-02-18",
            "evidence_level": "A - Dựa trên FDA drug labels, IDSA guidelines, và dữ liệu lâm sàng"
        },
        "risk_flags": {
            "high_alert": False,
            "narrow_therapeutic_index": False,
            "icu_critical_care_only": False,
            "bleeding_risk": "Low",
            "organ_toxicity": {"hepatic": "Low", "renal": "Low"}
        },
        "guideline_tags": [
            "IDSA Guidelines - Surgical Site Infection Prevention",
            "IDSA Guidelines - Skin and Soft Tissue Infections",
            "IDSA Guidelines - Community-Acquired Pneumonia",
            "WHO Essential Medicines List"
        ],
        "last_updated": "2025-02-18",
    },

    "Cephalexin": {
        "group": "Antibiotic - Cephalosporin (1st Generation)",
        "vietnamese_name": "Cephalexin, Keflex",
        "administration": ["PO"],
        "indications": [
            "Nhiễm khuẩn da và mô mềm",
            "Nhiễm khuẩn đường tiết niệu",
            "Viêm phổi cộng đồng",
            "Nhiễm khuẩn do Staphylococcus (MSSA)",
            "Nhiễm khuẩn do Streptococcus",
            "Nhiễm khuẩn xương và khớp (nhẹ)"
        ],
        "contraindications": [
            "Dị ứng cephalosporin",
            "Dị ứng penicillin nặng (phản ứng chéo 5-10%)"
        ],
        "dosage": {
            "adult_standard": "250-500mg PO x 4 lần/ngày",
            "adult_severe": "500mg-1g PO x 4 lần/ngày",
            "adult_uti": "250-500mg PO x 4 lần/ngày",
            "adult_skin": "250-500mg PO x 4 lần/ngày",
            "pediatric": "25-50mg/kg/ngày PO chia 4 lần (tối đa 4g/ngày)",
            "notes": "Uống với hoặc không thức ăn. Có thể uống với thức ăn để giảm kích ứng dạ dày."
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "250-500mg PO x 2-3 lần/ngày",
            "under_30": "250mg PO x 2 lần/ngày",
            "hemodialysis": "250-500mg PO sau mỗi lần lọc máu"
        },
        "side_effects": [
            "Tiêu chảy (phổ biến)",
            "Buồn nôn, nôn",
            "Phát ban dị ứng",
            "Đau đầu",
            "Chóng mặt",
            "Nhiễm C. difficile (hiếm)"
        ],
        "interactions": [
            "Probenecid: tăng nồng độ cephalexin",
            "Warfarin: có thể tăng INR",
            "Metformin: có thể tăng nồng độ metformin"
        ],
        "pregnancy": "B",
        "mechanism_of_action": "Cephalexin là cephalosporin thế hệ 1 đường uống, kháng sinh beta-lactam. Ức chế tổng hợp thành tế bào vi khuẩn bằng cách gắn với penicillin-binding proteins (PBPs). Phổ kháng khuẩn: Gram-dương mạnh (Staphylococcus aureus - MSSA, Streptococcus pneumoniae, Streptococcus pyogenes), Gram-âm yếu (E. coli, Klebsiella, Proteus mirabilis - một số chủng), không hiệu quả với Enterococcus, Pseudomonas, kỵ khí. Đặc điểm: cephalosporin đường uống phổ biến nhất, dùng 4 lần/ngày, hấp thu tốt qua đường tiêu hóa.",
        "monitoring": [
            "Dấu hiệu dị ứng (phát ban)",
            "Dấu hiệu nhiễm trùng (sốt, triệu chứng lâm sàng)",
            "Cấy máu và cấy từ vị trí nhiễm trùng (nếu có)",
            "Chức năng thận (creatinine, eGFR) - điều chỉnh liều",
            "Dấu hiệu nhiễm C. difficile (tiêu chảy)"
        ],
        "precautions": [
            "Phản ứng chéo với penicillin (5-10%)",
            "Điều chỉnh liều theo chức năng thận",
            "Uống với thức ăn để giảm kích ứng dạ dày",
            "Theo dõi nhiễm C. difficile",
            "Uống nhiều nước"
        ],
        "pharmacokinetics": {
            "half_life": "0.5-1 giờ",
            "onset": "1-2 giờ sau khi uống",
            "duration": "q6h (dùng 4 lần/ngày)",
            "protein_binding": "10-15%",
            "clearance": "Chủ yếu qua thận (80-90% bài tiết nguyên dạng), cần điều chỉnh thận"
        },
        "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm. Viên nang/viên nén: bảo quản trong bao bì kín.",
        "black_box_warnings": None,
        "drug_interactions": {
            "major": [],
            "moderate": [
                {
                    "drug": "Probenecid",
                    "mechanism": "Probenecid ức chế bài tiết cephalexin ở thận",
                    "effect": "Tăng nồng độ cephalexin",
                    "management": "Có thể dùng cùng. Theo dõi dấu hiệu độc tính."
                },
                {
                    "drug": "Warfarin",
                    "mechanism": "Cephalexin có thể ảnh hưởng đến hệ vi khuẩn đường ruột",
                    "effect": "Tăng INR",
                    "management": "Theo dõi INR thường xuyên."
                }
            ],
            "minor": []
        },
        "contraindications": {
            "tuyệt_đối": [
                "Dị ứng cephalexin hoặc cephalosporin",
                "Dị ứng penicillin nặng (sốc phản vệ)"
            ],
            "tương_đối": [
                "Dị ứng penicillin nhẹ - thận trọng",
                "Suy thận nặng - giảm liều",
                "Tiền sử nhiễm C. difficile"
            ]
        },
        "pregnancy_lactation": {
            "fda_category": "B",
            "pregnancy_details": "Cephalexin là thuốc phân loại B. An toàn trong thai kỳ.",
            "lactation": {
                "safety": "Compatible",
                "details": "Cephalexin bài tiết vào sữa mẹ ở nồng độ thấp. An toàn khi cho con bú.",
                "recommendation": "Có thể dùng khi cho con bú."
            }
        },
        "hepatic_adjustment": {
            "mild": "Không cần điều chỉnh liều",
            "moderate": "Không cần điều chỉnh liều",
            "severe": "Không cần điều chỉnh liều (thải trừ chủ yếu qua thận)"
        },
        "overdose_management": {
            "symptoms": [
                "Buồn nôn, nôn",
                "Tiêu chảy",
                "Phát ban"
            ],
            "antidote": "Không có antidote đặc hiệu. Điều trị hỗ trợ.",
            "treatment": [
                "Ngừng cephalexin",
                "Rửa dạ dày nếu uống trong vòng 1-2 giờ",
                "Điều trị triệu chứng",
                "Theo dõi chức năng thận"
            ],
            "monitoring": "Theo dõi triệu chứng, chức năng thận trong 24 giờ."
        },
        "reversal_agents": None,
        "administration_instructions": {
            "oral": {
                "with_food": "Có thể uống với hoặc không thức ăn. Uống với thức ăn có thể giảm kích ứng dạ dày.",
                "timing": "Uống 4 lần/ngày (q6h), thường 250-500mg mỗi lần. Uống đều đặn, cách đều nhau trong ngày."
            }
        },
        "references": {
            "primary_sources": [
                "FDA Drug Label - Cephalexin (Keflex)",
                "UpToDate - Cephalexin: Drug Information",
                "Medscape - Cephalexin Drug Reference"
            ],
            "last_updated": "2025-02-18",
            "evidence_level": "A"
        }
    },

    "Ceftriaxone": {
        "group": "Antibiotic - Cephalosporin (3rd Generation)",
        "vietnamese_name": "Ceftriaxone, Rocephin",
        "administration": ["IV", "IM"],
        "indications": [
            "Viêm màng não do vi khuẩn",
            "Viêm phổi cộng đồng",
            "Viêm phổi bệnh viện",
            "Nhiễm khuẩn huyết",
            "Nhiễm khuẩn đường tiết niệu phức tạp",
            "Nhiễm khuẩn da và mô mềm",
            "Bệnh lậu",
            "Bệnh Lyme",
            "Nhiễm khuẩn ổ bụng"
        ],
        "contraindications": [
            "Dị ứng ceftriaxone",
            "Dị ứng cephalosporin",
            "Dị ứng penicillin nặng (phản ứng chéo 5-10%)",
            "Trẻ sơ sinh <28 ngày tuổi có tăng bilirubin - CHỐNG CHỈ ĐỊNH (nguy cơ kernicterus)"
        ],
        "dosage": {
            "adult_standard": "1-2g IV/IM x 1 lần/ngày",
            "adult_severe": "2g IV x 1-2 lần/ngày",
            "adult_meningitis": "2g IV mỗi 12 giờ",
            "adult_gonorrhea": "250mg IM x 1 liều duy nhất",
            "adult_lyme": "2g IV x 1 lần/ngày x 14-28 ngày",
            "pediatric_meningitis": "50-100mg/kg IV mỗi 12 giờ (tối đa 4g/ngày)",
            "pediatric_standard": "50-75mg/kg IV/IM x 1 lần/ngày (tối đa 2g/ngày)",
            "notes": "Ưu điểm: dùng 1 lần/ngày (half-life dài 6-9 giờ). Không cần điều chỉnh liều ở suy thận (thải qua gan và thận). CHỐNG CHỈ ĐỊNH ở trẻ sơ sinh <28 ngày có tăng bilirubin (nguy cơ kernicterus)."
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "Không đổi (thải qua gan và thận)",
            "under_30": "Không đổi (thải qua gan và thận)",
            "hemodialysis": "Không đổi (không bị loại bỏ qua lọc máu)"
        },
        "side_effects": [
            "Tiêu chảy",
            "Phát ban dị ứng",
            "Buồn nôn, nôn",
            "Viêm tĩnh mạch tại chỗ tiêm",
            "Đau tại chỗ tiêm (IM)",
            "Tăng men gan (hiếm)",
            "Sỏi mật (hiếm, khi dùng kéo dài)",
            "Giảm bạch cầu (hiếm)",
            "Kernicterus ở trẻ sơ sinh (nếu tăng bilirubin)"
        ],
        "interactions": [
            "Warfarin: có thể tăng INR",
            "Calcium: không pha chung với ceftriaxone (tạo kết tủa) - đặc biệt ở trẻ sơ sinh",
            "Aminoglycosides: không pha chung (bất hoạt)"
        ],
        "pregnancy": "B",
        "mechanism_of_action": "Ceftriaxone là cephalosporin thế hệ 3, kháng sinh beta-lactam. Ức chế tổng hợp thành tế bào vi khuẩn bằng cách gắn với penicillin-binding proteins (PBPs). Phổ kháng khuẩn: Gram-dương (Staphylococcus aureus - MSSA, Streptococcus pneumoniae, Streptococcus pyogenes), Gram-âm mạnh (Enterobacteriaceae - E. coli, Klebsiella, Enterobacter, Proteus, Serratia, Neisseria meningitidis, Neisseria gonorrhoeae, Haemophilus influenzae), một số kỵ khí (Bacteroides fragilis). Không hiệu quả với Enterococcus, Pseudomonas aeruginosa, Acinetobacter. Đặc điểm: half-life dài (6-9 giờ) cho phép dùng 1 lần/ngày, không cần điều chỉnh liều ở suy thận (thải qua gan và thận), hiệu quả với viêm màng não, là lựa chọn hàng đầu cho nhiều nhiễm khuẩn nặng.",
        "monitoring": [
            "Dấu hiệu dị ứng (phát ban, sốc phản vệ)",
            "Dấu hiệu nhiễm trùng (sốt, WBC, triệu chứng lâm sàng)",
            "Cấy máu và cấy từ vị trí nhiễm trùng",
            "Chức năng gan (ALT, AST) - hiếm",
            "Bilirubin ở trẻ sơ sinh - CHỐNG CHỈ ĐỊNH nếu tăng bilirubin",
            "Công thức máu (CBC) - hiếm giảm bạch cầu",
            "Siêu âm bụng nếu dùng kéo dài (sỏi mật)"
        ],
        "precautions": [
            "CHỐNG CHỈ ĐỊNH ở trẻ sơ sinh <28 ngày có tăng bilirubin - nguy cơ kernicterus",
            "KHÔNG pha chung với calcium (tạo kết tủa) - đặc biệt ở trẻ sơ sinh, có thể gây tử vong",
            "Phản ứng chéo với penicillin (5-10%)",
            "Không cần điều chỉnh liều ở suy thận (ưu điểm)",
            "Sỏi mật khi dùng kéo dài - theo dõi nếu dùng >14 ngày",
            "Không pha chung với aminoglycosides",
            "Pha trong NS hoặc D5W, truyền IV trong 30 phút",
            "Theo dõi nhiễm C. difficile"
        ],
        "pharmacokinetics": {
            "half_life": "6-9 giờ (dài, cho phép dùng 1 lần/ngày)",
            "onset": "Ngay lập tức sau khi truyền IV",
            "duration": "24 giờ (dùng 1 lần/ngày)",
            "protein_binding": "85-95% (cao)",
            "clearance": "Gan (40-50%) và thận (50-60%), không cần điều chỉnh thận"
        },
        "storage": "Bảo quản bột khô ở nhiệt độ phòng (20-25°C). Sau khi pha: bảo quản ở nhiệt độ phòng 6 giờ, hoặc trong tủ lạnh 24 giờ.",
        "black_box_warnings": "CHỐNG CHỈ ĐỊNH ở trẻ sơ sinh <28 ngày có tăng bilirubin - nguy cơ kernicterus. KHÔNG pha chung với calcium (tạo kết tủa) - có thể gây tử vong, đặc biệt ở trẻ sơ sinh.",
        "drug_interactions": {
            "major": [
                {
                    "drug": "Calcium (IV)",
                    "mechanism": "Ceftriaxone tạo kết tủa không hòa tan với calcium, có thể gây tắc mạch, tử vong",
                    "effect": "Kết tủa trong mạch máu, tắc mạch, có thể tử vong",
                    "management": "CHỐNG CHỈ ĐỊNH pha chung. Không dùng cùng đường truyền. Cách ít nhất 48 giờ giữa ceftriaxone và calcium IV ở trẻ sơ sinh."
                }
            ],
            "moderate": [
                {
                    "drug": "Warfarin",
                    "mechanism": "Ceftriaxone có thể ảnh hưởng đến hệ vi khuẩn đường ruột",
                    "effect": "Tăng INR",
                    "management": "Theo dõi INR thường xuyên."
                }
            ],
            "minor": []
        },
        "contraindications": {
            "tuyệt_đối": [
                "Dị ứng ceftriaxone hoặc cephalosporin",
                "Dị ứng penicillin nặng (sốc phản vệ)",
                "Trẻ sơ sinh <28 ngày tuổi có tăng bilirubin - CHỐNG CHỈ ĐỊNH (nguy cơ kernicterus)"
            ],
            "tương_đối": [
                "Dị ứng penicillin nhẹ - thận trọng",
                "Tiền sử nhiễm C. difficile",
                "Dùng kéo dài (>14 ngày) - nguy cơ sỏi mật"
            ]
        },
        "contraindications_detail": {
            "tuyệt_đối": [
                "Dị ứng ceftriaxone hoặc cephalosporin",
                "Dị ứng penicillin nặng (sốc phản vệ)",
                "Trẻ sơ sinh <28 ngày tuổi có tăng bilirubin - CHỐNG CHỈ ĐỊNH (nguy cơ kernicterus)"
            ],
            "tương_đối": [
                "Dị ứng penicillin nhẹ - thận trọng",
                "Tiền sử nhiễm C. difficile",
                "Dùng kéo dài (>14 ngày) - nguy cơ sỏi mật"
            ]
        },
        "reversal_agents": {"available": False, "agents": []},
        "pregnancy_lactation": {
            "fda_category": "B",
            "pregnancy_details": "Ceftriaxone là thuốc phân loại B. An toàn trong thai kỳ. Được sử dụng rộng rãi trong thai kỳ.",
            "lactation": {
                "safety": "Compatible",
                "details": "Ceftriaxone bài tiết vào sữa mẹ ở nồng độ thấp. An toàn khi cho con bú.",
                "recommendation": "Có thể dùng khi cho con bú."
            }
        },
        "hepatic_adjustment": {
            "mild": "Không cần điều chỉnh liều",
            "moderate": "Không cần điều chỉnh liều",
            "severe": "Thận trọng (thải trừ một phần qua gan)"
        },
        "overdose_management": {
            "symptoms": [
                "Co giật (hiếm)",
                "Phản ứng dị ứng nặng",
                "Tăng men gan"
            ],
            "antidote": "Không có antidote đặc hiệu. Điều trị hỗ trợ.",
            "treatment": [
                "Ngừng ceftriaxone",
                "Điều trị co giật nếu có: Benzodiazepine",
                "Điều trị dị ứng nếu có: Epinephrine, antihistamine, corticosteroid",
                "Theo dõi chức năng gan, thận"
            ],
            "monitoring": "Theo dõi dấu hiệu sinh tồn, chức năng gan, thận trong 24-48 giờ."
        },
        "reversal_agents": None,
        "administration_instructions": {
            "oral": None,
            "iv": {
                "reconstitution": "Pha với NS hoặc D5W. Nồng độ pha: 100mg/ml (tối đa). Pha 1g trong 10ml = 100mg/ml, sau đó pha loãng trong 50-100ml NS hoặc D5W.",
                "infusion_rate": "Truyền IV trong 30 phút. Tốc độ: 50ml/30 phút = ~1.7ml/phút.",
                "compatibility": ["NS (0.9% NaCl)", "D5W (5% Dextrose)"],
                "incompatibility": [
                    "Calcium (IV) - CHỐNG CHỈ ĐỊNH pha chung, tạo kết tủa, có thể tử vong",
                    "Aminoglycosides - bất hoạt, không pha chung",
                    "Amphotericin B - không tương thích"
                ],
                "notes": "QUAN TRỌNG: 1) CHỐNG CHỈ ĐỊNH pha chung với calcium IV (tạo kết tủa, có thể tử vong), 2) Dùng 1 lần/ngày (half-life dài), 3) Không cần điều chỉnh liều ở suy thận, 4) CHỐNG CHỈ ĐỊNH ở trẻ sơ sinh <28 ngày có tăng bilirubin."
            },
            "im": {
                "reconstitution": "Pha với NS hoặc lidocaine 1%. Nồng độ pha: 250mg/ml (tối đa).",
                "injection_site": "Cơ lớn (mông, đùi)",
                "notes": "IM: 1-2g x 1 lần/ngày. Tiêm sâu vào cơ. Có thể đau tại chỗ tiêm. Gonorrhea: 250mg IM x 1 liều duy nhất."
            }
        },
        "references": {
            "primary_sources": [
                "FDA Drug Label - Ceftriaxone (Rocephin)",
                "IDSA Guidelines - Meningitis, Community-Acquired Pneumonia",
                "UpToDate - Ceftriaxone: Drug Information",
                "Medscape - Ceftriaxone Drug Reference"
            ],
            "last_updated": "2025-02-18",
            "evidence_level": "A"
        },
        "risk_flags": {
            "high_alert": True,
            "narrow_therapeutic_index": False,
            "icu_critical_care_only": False,
            "bleeding_risk": "Low",
            "organ_toxicity": {"hepatic": "Low", "renal": "Low", "neurological": "High (kernicterus ở trẻ sơ sinh)"}
        },
        "guideline_tags": [
            "IDSA Guidelines - Bacterial Meningitis",
            "IDSA Guidelines - Community-Acquired Pneumonia",
            "IDSA Guidelines - Hospital-Acquired Pneumonia",
            "IDSA Guidelines - Skin and Soft Tissue Infections",
            "CDC Guidelines - Sexually Transmitted Diseases (Gonorrhea)",
            "WHO Essential Medicines List"
        ],
        "last_updated": "2025-02-18",
    },

    "Cefepime": {
        "group": "Antibiotic - Cephalosporin (4th Generation)",
        "vietnamese_name": "Cefepime, Maxipime",
        "administration": ["IV", "IM"],
        "indications": [
            "Viêm phổi bệnh viện",
            "Nhiễm khuẩn huyết",
            "Nhiễm khuẩn đường tiết niệu phức tạp",
            "Nhiễm khuẩn da và mô mềm phức tạp",
            "Nhiễm khuẩn ổ bụng phức tạp",
            "Nhiễm khuẩn do Pseudomonas aeruginosa",
            "Nhiễm khuẩn do Enterobacteriaceae (kể cả một số ESBL)"
        ],
        "contraindications": [
            "Dị ứng cefepime",
            "Dị ứng cephalosporin",
            "Dị ứng penicillin nặng (phản ứng chéo 5-10%)"
        ],
        "dosage": {
            "adult_standard": "1-2g IV mỗi 12 giờ",
            "adult_severe": "2g IV mỗi 8 giờ",
            "adult_pseudomonas": "2g IV mỗi 8 giờ",
            "adult_febrile_neutropenia": "2g IV mỗi 8 giờ",
            "adult_im": "500mg-1g IM mỗi 12 giờ",
            "pediatric": "50mg/kg IV mỗi 8-12 giờ (tối đa 2g mỗi liều)",
            "notes": "Cefepime là cephalosporin thế hệ 4, phổ rộng hơn thế hệ 3, hiệu quả với Pseudomonas aeruginosa. Dùng 2-3 lần/ngày. Điều chỉnh liều theo chức năng thận."
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "1-2g IV mỗi 12 giờ",
            "under_30": "1g IV mỗi 12 giờ",
            "hemodialysis": "1g IV sau mỗi lần lọc máu"
        },
        "side_effects": [
            "Tiêu chảy",
            "Phát ban dị ứng",
            "Buồn nôn, nôn",
            "Viêm tĩnh mạch tại chỗ tiêm",
            "Tăng men gan (hiếm)",
            "Co giật (hiếm, ở suy thận nặng)",
            "Rối loạn thần kinh (lú lẫn, kích động) - hiếm, ở suy thận nặng",
            "Giảm bạch cầu (hiếm)"
        ],
        "interactions": [
            "Aminoglycosides: tác dụng hiệp đồng với Pseudomonas, nhưng không pha chung",
            "Warfarin: có thể tăng INR",
            "Probenecid: tăng nồng độ cefepime"
        ],
        "pregnancy": "B",
        "mechanism_of_action": "Cefepime là cephalosporin thế hệ 4, kháng sinh beta-lactam. Ức chế tổng hợp thành tế bào vi khuẩn bằng cách gắn với penicillin-binding proteins (PBPs). Phổ kháng khuẩn: Gram-dương (Staphylococcus aureus - MSSA, Streptococcus pneumoniae), Gram-âm mạnh (Enterobacteriaceae - kể cả một số ESBL, Pseudomonas aeruginosa, Acinetobacter - một số chủng), một số kỵ khí. Không hiệu quả với MRSA, Enterococcus, kỵ khí mạnh. Đặc điểm: phổ rộng hơn thế hệ 3, hiệu quả với Pseudomonas aeruginosa, kháng được một số beta-lactamase, dùng 2-3 lần/ngày, có thể gây co giật và rối loạn thần kinh ở suy thận nặng.",
        "monitoring": [
            "Dấu hiệu dị ứng (phát ban, sốc phản vệ)",
            "Dấu hiệu nhiễm trùng (sốt, WBC, triệu chứng lâm sàng)",
            "Cấy máu và cấy từ vị trí nhiễm trùng",
            "Chức năng thận (creatinine, eGFR) - điều chỉnh liều, đặc biệt quan trọng",
            "Dấu hiệu co giật, rối loạn thần kinh (lú lẫn, kích động) - đặc biệt ở suy thận nặng",
            "Chức năng gan (ALT, AST) - hiếm",
            "Công thức máu (CBC) - hiếm giảm bạch cầu"
        ],
        "precautions": [
            "Nguy cơ co giật và rối loạn thần kinh ở suy thận nặng - điều chỉnh liều quan trọng",
            "Phản ứng chéo với penicillin (5-10%)",
            "Điều chỉnh liều theo chức năng thận (CrCl) - QUAN TRỌNG",
            "Hiệu quả với Pseudomonas aeruginosa - ưu điểm so với thế hệ 3",
            "Không pha chung với aminoglycosides",
            "Pha trong NS hoặc D5W, truyền IV trong 30 phút",
            "Theo dõi nhiễm C. difficile"
        ],
        "pharmacokinetics": {
            "half_life": "2 giờ",
            "onset": "Ngay lập tức sau khi truyền IV",
            "duration": "Liều q8-12h",
            "protein_binding": "20%",
            "clearance": "Chủ yếu qua thận (85% bài tiết nguyên dạng), cần điều chỉnh thận"
        },
        "storage": "Bảo quản bột khô ở nhiệt độ phòng (20-25°C). Sau khi pha: bảo quản ở nhiệt độ phòng 24 giờ, hoặc trong tủ lạnh 7 ngày.",
        "black_box_warnings": "Nguy cơ co giật và rối loạn thần kinh ở suy thận nặng. Phải điều chỉnh liều theo chức năng thận.",
        "drug_interactions": {
            "major": [],
            "moderate": [
                {
                    "drug": "Aminoglycosides",
                    "mechanism": "Tác dụng hiệp đồng với Pseudomonas, nhưng aminoglycosides có thể bị bất hoạt khi pha chung",
                    "effect": "Tăng hiệu quả nếu truyền riêng biệt",
                    "management": "Có thể dùng cùng nhưng truyền riêng biệt, không pha chung."
                },
                {
                    "drug": "Warfarin",
                    "mechanism": "Cefepime có thể ảnh hưởng đến hệ vi khuẩn đường ruột",
                    "effect": "Tăng INR",
                    "management": "Theo dõi INR thường xuyên."
                }
            ],
            "minor": []
        },
        "contraindications": {
            "tuyệt_đối": [
                "Dị ứng cefepime hoặc cephalosporin",
                "Dị ứng penicillin nặng (sốc phản vệ)"
            ],
            "tương_đối": [
                "Dị ứng penicillin nhẹ - thận trọng",
                "Suy thận nặng - giảm liều, tăng nguy cơ co giật",
                "Tiền sử co giật - tăng nguy cơ",
                "Tiền sử nhiễm C. difficile"
            ]
        },
        "pregnancy_lactation": {
            "fda_category": "B",
            "pregnancy_details": "Cefepime là thuốc phân loại B. An toàn trong thai kỳ.",
            "lactation": {
                "safety": "Compatible",
                "details": "Cefepime bài tiết vào sữa mẹ ở nồng độ thấp. An toàn khi cho con bú.",
                "recommendation": "Có thể dùng khi cho con bú."
            }
        },
        "hepatic_adjustment": {
            "mild": "Không cần điều chỉnh liều",
            "moderate": "Không cần điều chỉnh liều",
            "severe": "Không cần điều chỉnh liều (thải trừ chủ yếu qua thận)"
        },
        "overdose_management": {
            "symptoms": [
                "Co giật (đặc biệt ở suy thận nặng)",
                "Rối loạn thần kinh (lú lẫn, kích động)",
                "Phản ứng dị ứng nặng"
            ],
            "antidote": "Không có antidote đặc hiệu. Điều trị hỗ trợ.",
            "treatment": [
                "Ngừng cefepime",
                "Điều trị co giật nếu có: Benzodiazepine",
                "Điều trị dị ứng nếu có: Epinephrine, antihistamine, corticosteroid",
                "Lọc máu nếu suy thận nặng",
                "Theo dõi chức năng thận, thần kinh"
            ],
            "monitoring": "Theo dõi dấu hiệu sinh tồn, chức năng thận, thần kinh trong 24-48 giờ."
        },
        "reversal_agents": None,
        "administration_instructions": {
            "oral": None,
            "iv": {
                "reconstitution": "Pha với NS hoặc D5W. Nồng độ pha: 100mg/ml (tối đa). Pha 1g trong 10ml = 100mg/ml, sau đó pha loãng trong 50-100ml NS hoặc D5W.",
                "infusion_rate": "Truyền IV trong 30 phút. Tốc độ: 50ml/30 phút = ~1.7ml/phút.",
                "compatibility": ["NS (0.9% NaCl)", "D5W (5% Dextrose)"],
                "incompatibility": [
                    "Aminoglycosides - bất hoạt, không pha chung",
                    "Amphotericin B - không tương thích"
                ],
                "notes": "QUAN TRỌNG: 1) Điều chỉnh liều theo chức năng thận (nguy cơ co giật ở suy thận nặng), 2) Hiệu quả với Pseudomonas aeruginosa, 3) Dùng 2-3 lần/ngày, 4) Không pha chung với aminoglycosides."
            },
            "im": {
                "reconstitution": "Pha với NS hoặc lidocaine 1%. Nồng độ pha: 280mg/ml (tối đa).",
                "injection_site": "Cơ lớn (mông, đùi)",
                "notes": "IM: 500mg-1g mỗi 12 giờ. Tiêm sâu vào cơ. Có thể đau tại chỗ tiêm."
            }
        },
        "references": {
            "primary_sources": [
                "FDA Drug Label - Cefepime (Maxipime)",
                "IDSA Guidelines - Hospital-Acquired Pneumonia",
                "UpToDate - Cefepime: Drug Information",
                "Medscape - Cefepime Drug Reference"
            ],
            "last_updated": "2025-02-18",
            "evidence_level": "A"
        },
        "risk_flags": {
            "high_alert": True,
            "narrow_therapeutic_index": False,
            "icu_critical_care_only": False,
            "bleeding_risk": "Low",
            "organ_toxicity": {"hepatic": "Low", "renal": "Low", "neurological": "High (co giật ở suy thận nặng)"}
        },
        "guideline_tags": [
            "IDSA Guidelines - Hospital-Acquired Pneumonia",
            "IDSA Guidelines - Ventilator-Associated Pneumonia",
            "IDSA Guidelines - Complicated Urinary Tract Infections",
            "IDSA Guidelines - Febrile Neutropenia",
            "WHO Essential Medicines List"
        ],
        "last_updated": "2025-02-18",
    }
}

__all__ = ['CEPHALOSPORIN_ANTIBIOTICS']

