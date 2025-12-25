"""
Aminoglycoside Antibiotics
Gentamicin, Amikacin, Tobramycin
"""

AMINOGLYCOSIDE_ANTIBIOTICS = {
    "Gentamicin": {
        "group": "Antibiotic - Aminoglycoside",
        "vietnamese_name": "Gentamicin, Garamycin",
        "administration": ["IV", "IM"],
        "indications": [
            "Nhiễm khuẩn Gram-âm nặng",
            "Nhiễm khuẩn huyết",
            "Viêm phổi bệnh viện",
            "Nhiễm khuẩn đường tiết niệu phức tạp",
            "Nhiễm khuẩn da và mô mềm",
            "Viêm nội tâm mạc (kết hợp với beta-lactam)"
        ],
        "contraindications": [
            "Dị ứng aminoglycoside",
            "Suy thận nặng (CrCl <10)",
            "Myasthenia gravis"
        ],
        "dosage": {
            "adult_standard": "3-5 mg/kg/ngày IV/IM, chia 1-3 lần",
            "adult_severe": "5-7 mg/kg/ngày IV/IM",
            "adult_once_daily": "5-7 mg/kg IV x 1 lần/ngày (phổ biến)",
            "adult_pneumonia": "5-7 mg/kg IV x 1 lần/ngày",
            "notes": "Cần TDM (therapeutic drug monitoring). Peak: 5-10 mg/L, Trough: <1 mg/L"
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "Giảm liều 30-50% hoặc tăng khoảng cách",
            "under_30": "Giảm liều 50-75% hoặc tăng khoảng cách đáng kể",
            "hemodialysis": "Liều sau lọc máu, cần TDM"
        },
        "side_effects": [
            "Độc thận (nephrotoxicity) - tăng creatinine",
            "Độc thần kinh thính giác (ototoxicity) - điếc không hồi phục",
            "Độc tiền đình (vestibular toxicity) - chóng mặt, mất thăng bằng",
            "Block thần kinh-cơ (neuromuscular blockade) - hiếm nhưng nguy hiểm",
            "Phát ban, sốt"
        ],
        "interactions": [
            "Vancomycin: tăng độc thận",
            "Furosemide: tăng độc thận và độc thính giác",
            "Cisplatin: tăng độc thận",
            "Beta-lactams: không pha chung (bất hoạt)"
        ],
        "pregnancy": "D - Độc thai nhi",
        "mechanism_of_action": "Gentamicin là aminoglycoside kháng sinh, ức chế tổng hợp protein vi khuẩn bằng cách gắn với tiểu đơn vị 30S của ribosome vi khuẩn. Dẫn đến đọc sai mã di truyền và tổng hợp protein bất thường, gây chết tế bào vi khuẩn. Phổ kháng khuẩn: Gram-âm mạnh (Enterobacteriaceae, Pseudomonas aeruginosa, Acinetobacter), một số Gram-dương (Staphylococcus aureus - kết hợp với beta-lactam). Hoạt tính kỵ khí kém. Đặc điểm: phụ thuộc nồng độ (concentration-dependent killing), có hiệu ứng hậu kháng sinh (post-antibiotic effect), cần TDM để tối ưu hiệu quả và giảm độc tính.",
        "monitoring": [
            "TDM (Therapeutic Drug Monitoring) - BẮT BUỘC: Peak (30-60 phút sau liều) và Trough (ngay trước liều tiếp theo)",
            "Mục tiêu: Peak 5-10 mg/L, Trough <1 mg/L (nhiễm khuẩn thông thường); Peak 8-10 mg/L, Trough <1 mg/L (nhiễm khuẩn nặng)",
            "Chức năng thận (creatinine, eGFR) - hàng ngày, đặc biệt quan trọng vì độc thận",
            "Dấu hiệu nhiễm trùng (sốt, WBC, triệu chứng lâm sàng)",
            "Cấy máu và cấy từ vị trí nhiễm trùng",
            "Thính giác (audiometry) - nếu dùng kéo dài (>7 ngày) hoặc liều cao",
            "Tiền đình (dấu hiệu chóng mặt, mất thăng bằng)",
            "Điện giải (natri, kali, magie) - có thể gây hạ kali, hạ magie"
        ],
        "precautions": [
            "TDM BẮT BUỘC - không dùng nếu không có khả năng theo dõi nồng độ",
            "Độc thận và độc thính giác - không hồi phục, đặc biệt nguy hiểm ở suy thận, người cao tuổi, dùng kéo dài, liều cao",
            "Điều chỉnh liều theo chức năng thận (eGFR) - quan trọng",
            "Tránh dùng với thuốc độc thận khác (vancomycin, furosemide, cisplatin)",
            "Tránh dùng với thuốc độc thính giác khác (furosemide, cisplatin)",
            "Không pha trộn với beta-lactams (bất hoạt) - truyền riêng, cách xa",
            "Liều một lần/ngày (extended interval dosing) được ưa chuộng hơn liều nhiều lần/ngày (tăng hiệu quả, giảm độc tính)",
            "Thận trọng ở người cao tuổi, suy thận, mất nước",
            "Theo dõi thính giác nếu dùng >7 ngày hoặc liều cao"
        ],
        "pharmacokinetics": {
            "half_life": "2-3 giờ (bình thường), 24-60 giờ (suy thận nặng)",
            "onset": "Ngay lập tức sau khi tiêm IV/IM",
            "duration": "Liều một lần/ngày (extended interval) hoặc q8-12h (traditional)",
            "protein_binding": "<10%",
            "metabolism": "Không chuyển hóa",
            "clearance": "Chủ yếu qua thận (90-100% bài tiết nguyên dạng), cần điều chỉnh thận",
            "volume_of_distribution": "0.2-0.3 L/kg"
        },
        "storage": "Bảo quản ở nhiệt độ phòng (20-25°C). Sau khi pha: bảo quản ở nhiệt độ phòng 24 giờ, hoặc trong tủ lạnh 7 ngày. Không đông lạnh.",
        "black_box_warnings": "Độc thận và độc thính giác - có thể không hồi phục. Đặc biệt nguy hiểm ở suy thận, người cao tuổi, dùng kéo dài, liều cao. Cần TDM để tối ưu hiệu quả và giảm độc tính.",
        "drug_interactions": {
            "major": [
                {
                    "drug": "Vancomycin",
                    "mechanism": "Cả hai đều độc thận, tác dụng cộng dồn",
                    "effect": "Tăng nguy cơ độc thận nặng, có thể không hồi phục",
                    "management": "Tránh dùng đồng thời nếu có thể. Nếu bắt buộc, theo dõi chức năng thận sát, TDM cho cả hai, giảm liều nếu cần."
                },
                {
                    "drug": "Furosemide",
                    "mechanism": "Furosemide tăng nồng độ gentamicin trong ốc tai và thận, tăng độc tính",
                    "effect": "Tăng nguy cơ độc thận và độc thính giác",
                    "management": "Tránh dùng đồng thời nếu có thể. Nếu bắt buộc, theo dõi chức năng thận và thính giác sát."
                },
                {
                    "drug": "Cisplatin",
                    "mechanism": "Cả hai đều độc thận và độc thính giác, tác dụng cộng dồn",
                    "effect": "Tăng nguy cơ độc thận và độc thính giác nặng",
                    "management": "Tránh dùng đồng thời nếu có thể. Nếu bắt buộc, theo dõi chức năng thận và thính giác sát."
                }
            ],
            "moderate": [
                {
                    "drug": "Beta-lactams (Penicillins, Cephalosporins)",
                    "mechanism": "Beta-lactams có thể bất hoạt gentamicin về mặt hóa học khi pha chung",
                    "effect": "Giảm hiệu quả kháng khuẩn của gentamicin",
                    "management": "Không pha trộn. Truyền riêng, cách xa ít nhất 1 giờ."
                }
            ]
        },
        "references": {
            "primary_sources": [
                "FDA Drug Label - Gentamicin",
                "IDSA Guidelines - Antimicrobial Therapy",
                "UpToDate - Gentamicin: Drug Information",
                "Medscape - Gentamicin Drug Reference",
                "Goodman & Gilman's The Pharmacological Basis of Therapeutics (14th ed)",
                "Lexicomp Online - Gentamicin Monograph",
                "Micromedex - Gentamicin Drug Information"
            ],
            "last_updated": "2025-02-18",
            "evidence_level": "A - Dựa trên FDA drug labels, IDSA guidelines, và dữ liệu lâm sàng từ nhiều nguồn"
        },
        "risk_flags": {
            "high_alert": True,
            "narrow_therapeutic_index": True,
            "icu_critical_care_only": False,
            "bleeding_risk": "Low",
            "organ_toxicity": {"renal": "High", "neurological": "High (ototoxicity, vestibular toxicity)"}
        },
        "guideline_tags": [
            "IDSA Guidelines - Hospital-Acquired Pneumonia",
            "IDSA Guidelines - Complicated Urinary Tract Infections",
            "IDSA Guidelines - Infective Endocarditis",
            "IDSA Guidelines - Skin and Soft Tissue Infections",
            "WHO Essential Medicines List"
        ],
        "last_updated": "2025-02-18",
    },
    
    "Amikacin": {
        "group": "Antibiotic - Aminoglycoside",
        "vietnamese_name": "Amikacin, Amikin",
        "administration": ["IV", "IM"],
        "indications": [
            "Nhiễm khuẩn Gram-âm nặng (kháng gentamicin/tobramycin)",
            "Nhiễm khuẩn huyết",
            "Viêm phổi bệnh viện",
            "Nhiễm khuẩn đường tiết niệu phức tạp",
            "Nhiễm khuẩn da và mô mềm",
            "Nhiễm khuẩn do vi khuẩn kháng đa thuốc (MDR)"
        ],
        "contraindications": [
            "Dị ứng aminoglycoside",
            "Suy thận nặng (CrCl <10)",
            "Myasthenia gravis"
        ],
        "dosage": {
            "adult_standard": "15 mg/kg/ngày IV/IM, chia 1-3 lần",
            "adult_severe": "15-20 mg/kg/ngày IV/IM",
            "adult_once_daily": "15-20 mg/kg IV x 1 lần/ngày (phổ biến)",
            "adult_pneumonia": "15-20 mg/kg IV x 1 lần/ngày",
            "notes": "Cần TDM. Peak: 20-30 mg/L, Trough: <5 mg/L"
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "Giảm liều 30-50% hoặc tăng khoảng cách",
            "under_30": "Giảm liều 50-75% hoặc tăng khoảng cách đáng kể",
            "hemodialysis": "Liều sau lọc máu, cần TDM"
        },
        "side_effects": [
            "Độc thận (nephrotoxicity)",
            "Độc thần kinh thính giác (ototoxicity)",
            "Độc tiền đình (vestibular toxicity)",
            "Block thần kinh-cơ (neuromuscular blockade)",
            "Phát ban, sốt"
        ],
        "interactions": [
            "Vancomycin: tăng độc thận",
            "Furosemide: tăng độc thận và độc thính giác",
            "Cisplatin: tăng độc thận",
            "Beta-lactams: không pha chung"
        ],
        "pregnancy": "D - Độc thai nhi",
        "mechanism_of_action": "Amikacin là aminoglycoside kháng sinh, ức chế tổng hợp protein vi khuẩn bằng cách gắn với tiểu đơn vị 30S của ribosome vi khuẩn. Tương tự gentamicin nhưng ít bị kháng hơn do có cấu trúc hóa học khác. Phổ kháng khuẩn: Gram-âm mạnh (Enterobacteriaceae, Pseudomonas aeruginosa, Acinetobacter - kể cả một số chủng kháng gentamicin/tobramycin), một số Gram-dương. Hoạt tính kỵ khí kém. Đặc điểm: phụ thuộc nồng độ, có hiệu ứng hậu kháng sinh, cần TDM.",
        "monitoring": [
            "TDM (Therapeutic Drug Monitoring) - BẮT BUỘC: Peak (30-60 phút sau liều) và Trough (ngay trước liều tiếp theo)",
            "Mục tiêu: Peak 20-30 mg/L, Trough <5 mg/L",
            "Chức năng thận (creatinine, eGFR) - hàng ngày",
            "Dấu hiệu nhiễm trùng (sốt, WBC, triệu chứng lâm sàng)",
            "Cấy máu và cấy từ vị trí nhiễm trùng",
            "Thính giác (audiometry) - nếu dùng kéo dài",
            "Tiền đình (dấu hiệu chóng mặt, mất thăng bằng)",
            "Điện giải (natri, kali, magie)"
        ],
        "precautions": [
            "TDM BẮT BUỘC",
            "Độc thận và độc thính giác - không hồi phục",
            "Điều chỉnh liều theo chức năng thận",
            "Tránh dùng với thuốc độc thận/độc thính giác khác",
            "Không pha trộn với beta-lactams",
            "Liều một lần/ngày được ưa chuộng",
            "Thận trọng ở người cao tuổi, suy thận, mất nước"
        ],
        "pharmacokinetics": {
            "half_life": "2-3 giờ (bình thường), 24-60 giờ (suy thận nặng)",
            "onset": "Ngay lập tức sau khi tiêm IV/IM",
            "duration": "Liều một lần/ngày hoặc q8-12h",
            "protein_binding": "<10%",
            "metabolism": "Không chuyển hóa",
            "clearance": "Chủ yếu qua thận (90-100% bài tiết nguyên dạng), cần điều chỉnh thận"
        },
        "storage": "Bảo quản ở nhiệt độ phòng (20-25°C). Sau khi pha: bảo quản ở nhiệt độ phòng 24 giờ, hoặc trong tủ lạnh 7 ngày.",
        "black_box_warnings": "Độc thận và độc thính giác - có thể không hồi phục. Cần TDM để tối ưu hiệu quả và giảm độc tính.",
        "references": {
            "primary_sources": [
                "FDA Drug Label - Amikacin",
                "IDSA Guidelines - Antimicrobial Therapy",
                "UpToDate - Amikacin: Drug Information",
                "Medscape - Amikacin Drug Reference"
            ],
            "last_updated": "2025-02-18",
            "evidence_level": "A"
        },
        "risk_flags": {
            "high_alert": True,
            "narrow_therapeutic_index": True,
            "icu_critical_care_only": False,
            "bleeding_risk": "Low",
            "organ_toxicity": {"renal": "High", "neurological": "High (ototoxicity, vestibular toxicity)"}
        },
        "guideline_tags": [
            "IDSA Guidelines - Hospital-Acquired Pneumonia",
            "IDSA Guidelines - Complicated Urinary Tract Infections",
            "IDSA Guidelines - Multidrug-Resistant Gram-Negative Infections",
            "WHO Essential Medicines List"
        ],
        "last_updated": "2025-02-18",
    },
    
    "Tobramycin": {
        "group": "Antibiotic - Aminoglycoside",
        "vietnamese_name": "Tobramycin, Nebcin",
        "administration": ["IV", "IM", "Inhaled"],
        "indications": [
            "Nhiễm khuẩn Gram-âm nặng",
            "Nhiễm khuẩn huyết",
            "Viêm phổi bệnh viện",
            "Nhiễm khuẩn đường tiết niệu phức tạp",
            "Nhiễm khuẩn da và mô mềm",
            "Pseudomonas aeruginosa (đặc biệt hiệu quả)",
            "Viêm phổi mãn tính ở bệnh nhân xơ nang (CF) - dạng hít"
        ],
        "contraindications": [
            "Dị ứng aminoglycoside",
            "Suy thận nặng (CrCl <10)",
            "Myasthenia gravis"
        ],
        "dosage": {
            "adult_standard": "3-5 mg/kg/ngày IV/IM, chia 1-3 lần",
            "adult_severe": "5-7 mg/kg/ngày IV/IM",
            "adult_once_daily": "5-7 mg/kg IV x 1 lần/ngày (phổ biến)",
            "adult_pseudomonas": "5-7 mg/kg IV x 1 lần/ngày",
            "adult_inhaled_cf": "300mg x 2 lần/ngày (dạng hít)",
            "notes": "Cần TDM. Peak: 5-10 mg/L, Trough: <1 mg/L. Đặc biệt hiệu quả với Pseudomonas aeruginosa"
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "Giảm liều 30-50% hoặc tăng khoảng cách",
            "under_30": "Giảm liều 50-75% hoặc tăng khoảng cách đáng kể",
            "hemodialysis": "Liều sau lọc máu, cần TDM"
        },
        "side_effects": [
            "Độc thận (nephrotoxicity) - tăng creatinine",
            "Độc thần kinh thính giác (ototoxicity) - điếc không hồi phục",
            "Độc tiền đình (vestibular toxicity) - chóng mặt, mất thăng bằng",
            "Block thần kinh-cơ (neuromuscular blockade) - hiếm nhưng nguy hiểm",
            "Phát ban, sốt",
            "Ho, khó thở (dạng hít)"
        ],
        "interactions": [
            "Vancomycin: tăng độc thận",
            "Furosemide: tăng độc thận và độc thính giác",
            "Cisplatin: tăng độc thận",
            "Beta-lactams: không pha chung (bất hoạt)"
        ],
        "pregnancy": "D - Độc thai nhi",
        "mechanism_of_action": "Tobramycin là aminoglycoside kháng sinh, ức chế tổng hợp protein vi khuẩn bằng cách gắn với tiểu đơn vị 30S của ribosome vi khuẩn. Tương tự gentamicin nhưng đặc biệt hiệu quả với Pseudomonas aeruginosa (thường hiệu quả hơn gentamicin). Phổ kháng khuẩn: Gram-âm mạnh (Enterobacteriaceae, Pseudomonas aeruginosa - đặc biệt hiệu quả, Acinetobacter), một số Gram-dương. Hoạt tính kỵ khí kém. Đặc điểm: phụ thuộc nồng độ, có hiệu ứng hậu kháng sinh, cần TDM. Dạng hít được dùng cho bệnh nhân xơ nang (CF) để điều trị nhiễm Pseudomonas mãn tính.",
        "monitoring": [
            "TDM (Therapeutic Drug Monitoring) - BẮT BUỘC: Peak (30-60 phút sau liều) và Trough (ngay trước liều tiếp theo)",
            "Mục tiêu: Peak 5-10 mg/L, Trough <1 mg/L (nhiễm khuẩn thông thường); Peak 8-10 mg/L, Trough <1 mg/L (nhiễm khuẩn nặng, Pseudomonas)",
            "Chức năng thận (creatinine, eGFR) - hàng ngày, đặc biệt quan trọng vì độc thận",
            "Dấu hiệu nhiễm trùng (sốt, WBC, triệu chứng lâm sàng)",
            "Cấy máu và cấy từ vị trí nhiễm trùng",
            "Thính giác (audiometry) - nếu dùng kéo dài (>7 ngày) hoặc liều cao",
            "Tiền đình (dấu hiệu chóng mặt, mất thăng bằng)",
            "Điện giải (natri, kali, magie) - có thể gây hạ kali, hạ magie",
            "Chức năng phổi (nếu dùng dạng hít)"
        ],
        "precautions": [
            "TDM BẮT BUỘC - không dùng nếu không có khả năng theo dõi nồng độ",
            "Độc thận và độc thính giác - không hồi phục, đặc biệt nguy hiểm ở suy thận, người cao tuổi, dùng kéo dài, liều cao",
            "Điều chỉnh liều theo chức năng thận (eGFR) - quan trọng",
            "Tránh dùng với thuốc độc thận khác (vancomycin, furosemide, cisplatin)",
            "Tránh dùng với thuốc độc thính giác khác (furosemide, cisplatin)",
            "Không pha trộn với beta-lactams (bất hoạt) - truyền riêng, cách xa",
            "Liều một lần/ngày (extended interval dosing) được ưa chuộng hơn liều nhiều lần/ngày (tăng hiệu quả, giảm độc tính)",
            "Thận trọng ở người cao tuổi, suy thận, mất nước",
            "Theo dõi thính giác nếu dùng >7 ngày hoặc liều cao",
            "Dạng hít: dùng cho bệnh nhân xơ nang (CF) để điều trị nhiễm Pseudomonas mãn tính, ít độc tính toàn thân hơn"
        ],
        "pharmacokinetics": {
            "half_life": "2-3 giờ (bình thường), 24-60 giờ (suy thận nặng)",
            "onset": "Ngay lập tức sau khi tiêm IV/IM",
            "duration": "Liều một lần/ngày (extended interval) hoặc q8-12h (traditional)",
            "protein_binding": "<10%",
            "metabolism": "Không chuyển hóa",
            "clearance": "Chủ yếu qua thận (90-100% bài tiết nguyên dạng), cần điều chỉnh thận",
            "volume_of_distribution": "0.2-0.3 L/kg"
        },
        "storage": "Bảo quản ở nhiệt độ phòng (20-25°C). Sau khi pha: bảo quản ở nhiệt độ phòng 24 giờ, hoặc trong tủ lạnh 7 ngày. Không đông lạnh.",
        "black_box_warnings": "Độc thận và độc thính giác - có thể không hồi phục. Đặc biệt nguy hiểm ở suy thận, người cao tuổi, dùng kéo dài, liều cao. Cần TDM để tối ưu hiệu quả và giảm độc tính.",
        "drug_interactions": {
            "major": [
                {
                    "drug": "Vancomycin",
                    "mechanism": "Cả hai đều độc thận, tác dụng cộng dồn",
                    "effect": "Tăng nguy cơ độc thận nặng, có thể không hồi phục",
                    "management": "Tránh dùng đồng thời nếu có thể. Nếu bắt buộc, theo dõi chức năng thận sát, TDM cho cả hai, giảm liều nếu cần."
                },
                {
                    "drug": "Furosemide",
                    "mechanism": "Furosemide tăng nồng độ tobramycin trong ốc tai và thận, tăng độc tính",
                    "effect": "Tăng nguy cơ độc thận và độc thính giác",
                    "management": "Tránh dùng đồng thời nếu có thể. Nếu bắt buộc, theo dõi chức năng thận và thính giác sát."
                },
                {
                    "drug": "Cisplatin",
                    "mechanism": "Cả hai đều độc thận và độc thính giác, tác dụng cộng dồn",
                    "effect": "Tăng nguy cơ độc thận và độc thính giác nặng",
                    "management": "Tránh dùng đồng thời nếu có thể. Nếu bắt buộc, theo dõi chức năng thận và thính giác sát."
                }
            ],
            "moderate": [
                {
                    "drug": "Beta-lactams (Penicillins, Cephalosporins)",
                    "mechanism": "Beta-lactams có thể bất hoạt tobramycin về mặt hóa học khi pha chung",
                    "effect": "Giảm hiệu quả kháng khuẩn của tobramycin",
                    "management": "Không pha trộn. Truyền riêng, cách xa ít nhất 1 giờ."
                }
            ]
        },
        "references": {
            "primary_sources": [
                "FDA Drug Label - Tobramycin",
                "IDSA Guidelines - Antimicrobial Therapy",
                "UpToDate - Tobramycin: Drug Information",
                "Medscape - Tobramycin Drug Reference",
                "Goodman & Gilman's The Pharmacological Basis of Therapeutics (14th ed)",
                "Lexicomp Online - Tobramycin Monograph",
                "Micromedex - Tobramycin Drug Information"
            ],
            "last_updated": "2025-02-18",
            "evidence_level": "A - Dựa trên FDA drug labels, IDSA guidelines, và dữ liệu lâm sàng từ nhiều nguồn"
        },
        "risk_flags": {
            "high_alert": True,
            "narrow_therapeutic_index": True,
            "icu_critical_care_only": False,
            "bleeding_risk": "Low",
            "organ_toxicity": {"renal": "High", "neurological": "High (ototoxicity, vestibular toxicity)"}
        },
        "guideline_tags": [
            "IDSA Guidelines - Hospital-Acquired Pneumonia",
            "IDSA Guidelines - Complicated Urinary Tract Infections",
            "IDSA Guidelines - Pseudomonas aeruginosa Infections",
            "Cystic Fibrosis Foundation Guidelines - Pseudomonas Infections",
            "WHO Essential Medicines List"
        ],
        "last_updated": "2025-02-18",
    },
    
    "Plazomicin": {
        "group": "Antibiotic - Aminoglycoside (Next Generation)",
        "vietnamese_name": "Plazomicin, Zemdri",
        "administration": ["IV"],
        "indications": [
            "Nhiễm khuẩn đường tiết niệu phức tạp (cUTI) do vi khuẩn Gram-âm đa kháng",
            "Nhiễm khuẩn huyết do vi khuẩn Gram-âm đa kháng",
            "Nhiễm khuẩn do CRE (Carbapenem-resistant Enterobacteriaceae)",
            "Nhiễm khuẩn do MDR Gram-âm (khi các kháng sinh khác không hiệu quả)"
        ],
        "contraindications": [
            "Dị ứng plazomicin hoặc aminoglycoside",
            "Suy thận nặng (CrCl <15) - CHỐNG CHỈ ĐỊNH",
            "Myasthenia gravis - CHỐNG CHỈ ĐỊNH",
            "Trẻ em <18 tuổi - chưa được nghiên cứu"
        ],
        "dosage": {
            "adult_standard": "15mg/kg IV x 1 lần/ngày (dựa trên trọng lượng cơ thể thực tế)",
            "adult_cuti": "15mg/kg IV x 1 lần/ngày trong 4-7 ngày",
            "adult_bloodstream": "15mg/kg IV x 1 lần/ngày trong 7-14 ngày",
            "notes": "Plazomicin là aminoglycoside thế hệ mới, kháng được nhiều enzyme kháng aminoglycoside (AME). Dùng 1 lần/ngày. Cần TDM (therapeutic drug monitoring) - Peak: 50-100 mg/L, Trough: <3 mg/L. Điều chỉnh liều theo CrCl."
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "15mg/kg IV mỗi 24 giờ (theo dõi CrCl)",
            "15_30": "15mg/kg IV mỗi 48 giờ",
            "under_15": "CHỐNG CHỈ ĐỊNH",
            "hemodialysis": "CHỐNG CHỈ ĐỊNH hoặc dùng rất thận trọng với liều sau lọc máu"
        },
        "side_effects": [
            "Độc thận (nephrotoxicity) - tăng creatinine, giảm eGFR - phổ biến",
            "Độc thần kinh thính giác (ototoxicity) - điếc không hồi phục - phổ biến",
            "Độc tiền đình (vestibular toxicity) - chóng mặt, mất thăng bằng - phổ biến",
            "Tiêu chảy",
            "Buồn nôn, nôn",
            "Đau đầu",
            "Tăng transaminase (hiếm)",
            "Block thần kinh-cơ (neuromuscular blockade) - hiếm nhưng nguy hiểm"
        ],
        "interactions": [
            "Vancomycin: tăng độc thận - tránh dùng cùng",
            "Furosemide: tăng độc thận và độc thính giác - tránh dùng cùng",
            "Cisplatin: tăng độc thận - tránh dùng cùng",
            "Beta-lactams: không pha chung (bất hoạt)",
            "Thuốc độc thận khác: tăng nguy cơ độc thận"
        ],
        "pregnancy": "D - Độc thai nhi",
        "mechanism_of_action": "Plazomicin là aminoglycoside thế hệ mới (next-generation aminoglycoside), được thiết kế để kháng các enzyme kháng aminoglycoside (AME - aminoglycoside-modifying enzymes) như AAC(2'), AAC(6'), ANT(2''), APH(2''). Gắn với ribosome 30S của vi khuẩn, ngăn chặn sự tổng hợp protein, dẫn đến tiêu diệt vi khuẩn (bactericidal). Phổ kháng khuẩn: Gram-âm mạnh (Enterobacteriaceae - kể cả CRE, E. coli, Klebsiella, Enterobacter, Serratia, Proteus, Citrobacter), một số Gram-dương (Staphylococcus - kể cả MRSA). Không hiệu quả với Pseudomonas aeruginosa, Acinetobacter, hoặc kỵ khí. ĐẶC ĐIỂM: (1) Kháng được nhiều AME (ưu điểm so với aminoglycoside cũ), (2) Hiệu quả với CRE và MDR Gram-âm, (3) Dùng 1 lần/ngày, (4) Cần TDM (Peak: 50-100 mg/L, Trough: <3 mg/L), (5) Nguy cơ độc thận và độc thính giác cao (tương tự aminoglycoside khác), (6) CHỐNG CHỈ ĐỊNH ở suy thận nặng (CrCl <15).",
        "monitoring": [
            "TDM (therapeutic drug monitoring) - QUAN TRỌNG: Peak: 50-100 mg/L, Trough: <3 mg/L",
            "Chức năng thận (creatinine, eGFR, BUN) - QUAN TRỌNG: theo dõi hàng ngày",
            "Độc thận: tăng creatinine, giảm eGFR, giảm lượng nước tiểu",
            "Độc thần kinh thính giác: giảm thính lực, ù tai - theo dõi thính lực trước và sau điều trị",
            "Độc tiền đình: chóng mặt, mất thăng bằng, nôn",
            "Dấu hiệu nhiễm trùng (sốt, WBC, triệu chứng lâm sàng)",
            "Cấy máu và cấy từ vị trí nhiễm trùng",
            "Chức năng gan (ALT, AST) - hiếm"
        ],
        "precautions": [
            "CHỐNG CHỈ ĐỊNH ở suy thận nặng (CrCl <15)",
            "CHỐNG CHỈ ĐỊNH ở myasthenia gravis",
            "Cần TDM (therapeutic drug monitoring) - Peak: 50-100 mg/L, Trough: <3 mg/L",
            "Theo dõi chức năng thận hàng ngày - nguy cơ độc thận cao",
            "Theo dõi thính lực trước và sau điều trị - nguy cơ độc thính giác cao",
            "Tránh dùng với vancomycin, furosemide, cisplatin - tăng độc thận",
            "Không pha chung với beta-lactams (bất hoạt)",
            "Điều chỉnh liều theo CrCl - quan trọng",
            "Dùng 1 lần/ngày (dựa trên trọng lượng cơ thể thực tế)",
            "Nguy cơ block thần kinh-cơ - thận trọng ở bệnh nhân có nguy cơ"
        ],
        "pharmacokinetics": {
            "half_life": "3.5-4.5 giờ (bình thường), tăng ở suy thận",
            "onset": "Ngay lập tức sau khi tiêm IV",
            "duration": "24 giờ (dùng 1 lần/ngày)",
            "protein_binding": "<20%",
            "metabolism": "Không chuyển hóa đáng kể",
            "clearance": "Chủ yếu qua thận (90-95% bài tiết nguyên dạng), cần điều chỉnh thận"
        },
        "storage": "Bảo quản bột khô ở nhiệt độ phòng (20-25°C). Sau khi pha: bảo quản ở nhiệt độ phòng 24 giờ, hoặc trong tủ lạnh 48 giờ. Không đông lạnh.",
        "black_box_warnings": "NGUY CƠ ĐỘC THẬN VÀ ĐỘC THÍNH GIÁC. CHỐNG CHỈ ĐỊNH ở suy thận nặng (CrCl <15) và myasthenia gravis. Cần TDM và theo dõi chức năng thận hàng ngày. Theo dõi thính lực trước và sau điều trị.",
        "drug_interactions": {
            "major": [
                {
                    "drug": "Vancomycin",
                    "mechanism": "Cả hai đều có độc tính thận, tác dụng cộng dồn",
                    "effect": "Tăng nguy cơ độc thận nặng",
                    "management": "TRÁNH DÙNG CÙNG. Nếu bắt buộc, theo dõi chức năng thận chặt chẽ hàng ngày, giảm liều cả hai nếu cần."
                },
                {
                    "drug": "Furosemide",
                    "mechanism": "Furosemide tăng độc thận và độc thính giác của aminoglycoside",
                    "effect": "Tăng nguy cơ độc thận và độc thính giác nặng",
                    "management": "TRÁNH DÙNG CÙNG. Nếu bắt buộc, theo dõi chức năng thận và thính lực chặt chẽ."
                },
                {
                    "drug": "Cisplatin",
                    "mechanism": "Cả hai đều có độc tính thận, tác dụng cộng dồn",
                    "effect": "Tăng nguy cơ độc thận nặng",
                    "management": "TRÁNH DÙNG CÙNG. Nếu bắt buộc, theo dõi chức năng thận chặt chẽ hàng ngày."
                }
            ],
            "moderate": [
                {
                    "drug": "Beta-lactams (Penicillin, Cephalosporin, Carbapenem)",
                    "mechanism": "Beta-lactams có thể bất hoạt aminoglycoside khi pha chung",
                    "effect": "Giảm hiệu quả plazomicin",
                    "management": "Không pha chung. Truyền riêng biệt, cách nhau ít nhất 1 giờ."
                }
            ],
            "minor": []
        },
        "contraindications": {
            "tuyệt_đối": [
                "Dị ứng plazomicin hoặc aminoglycoside",
                "Suy thận nặng (CrCl <15) - CHỐNG CHỈ ĐỊNH",
                "Myasthenia gravis - CHỐNG CHỈ ĐỊNH (nguy cơ block thần kinh-cơ nặng)"
            ],
            "tương_đối": [
                "Suy thận (CrCl 15-30) - điều chỉnh liều, theo dõi chặt chẽ",
                "Suy thận (CrCl 30-60) - theo dõi chặt chẽ",
                "Tiền sử độc thận - tăng nguy cơ",
                "Tiền sử độc thính giác - tăng nguy cơ",
                "Trẻ em <18 tuổi - chưa được nghiên cứu",
                "Có thai (category D) - độc thai nhi"
            ]
        },
        "pregnancy_lactation": {
            "fda_category": "D",
            "pregnancy_details": "Plazomicin là thuốc phân loại D. Aminoglycoside gây độc thính giác và độc thận ở thai nhi. CHỐNG CHỈ ĐỊNH trong thai kỳ trừ khi lợi ích vượt quá nguy cơ rõ ràng.",
            "lactation": {
                "safety": "Compatible with Caution",
                "details": "Plazomicin bài tiết vào sữa mẹ. Aminoglycoside có thể gây độc thính giác ở trẻ bú mẹ. Thận trọng khi cho con bú.",
                "recommendation": "Tránh dùng khi cho con bú. Nếu bắt buộc, theo dõi trẻ về dấu hiệu độc thính giác."
            }
        },
        "hepatic_adjustment": {
            "mild": "Không cần điều chỉnh liều",
            "moderate": "Không cần điều chỉnh liều",
            "severe": "Không cần điều chỉnh liều (thải trừ qua thận)",
            "notes": "Plazomicin không chuyển hóa qua gan, thải trừ chủ yếu qua thận. Không cần điều chỉnh liều ở bệnh nhân suy gan."
        },
        "overdose_management": {
            "symptoms": [
                "Độc thận nặng: Suy thận cấp, tăng creatinine, giảm eGFR, giảm lượng nước tiểu",
                "Độc thính giác nặng: Điếc không hồi phục, ù tai",
                "Độc tiền đình nặng: Chóng mặt nặng, mất thăng bằng, nôn",
                "Block thần kinh-cơ: Yếu cơ, suy hô hấp - NGUY HIỂM"
            ],
            "antidote": "Calcium gluconate hoặc neostigmine cho block thần kinh-cơ. Hemodialysis có thể loại bỏ plazomicin một phần.",
            "treatment": [
                "Ngừng ngay plazomicin",
                "Nếu block thần kinh-cơ:",
                "  - Calcium gluconate 1-3g IV (đối kháng block thần kinh-cơ)",
                "  - Neostigmine 0.5-2mg IV (nếu cần)",
                "  - Hỗ trợ hô hấp (thở máy) nếu cần",
                "Nếu độc thận:",
                "  - Bù dịch đầy đủ",
                "  - Điều chỉnh điện giải",
                "  - Lọc máu nếu cần (hemodialysis có thể loại bỏ plazomicin một phần)",
                "Theo dõi: Dấu hiệu sinh tồn, chức năng thận, thính lực, dấu hiệu block thần kinh-cơ"
            ],
            "monitoring": "Theo dõi dấu hiệu sinh tồn, chức năng thận (creatinine, eGFR, lượng nước tiểu), thính lực, dấu hiệu block thần kinh-cơ (yếu cơ, suy hô hấp) trong ít nhất 48-72 giờ. Theo dõi lâu hơn nếu có độc thận hoặc block thần kinh-cơ."
        },
        "reversal_agents": {
            "available": True,
            "agents": [
                {
                    "agent": "Calcium Gluconate",
                    "mechanism": "Đối kháng block thần kinh-cơ do aminoglycoside",
                    "indication": "Block thần kinh-cơ do plazomicin",
                    "dose": "1-3g IV, lặp lại nếu cần"
                },
                {
                    "agent": "Neostigmine",
                    "mechanism": "Cholinesterase inhibitor, tăng acetylcholine, đối kháng block thần kinh-cơ",
                    "indication": "Block thần kinh-cơ do plazomicin (nếu calcium không hiệu quả)",
                    "dose": "0.5-2mg IV, lặp lại nếu cần"
                }
            ],
            "notes": "Calcium gluconate và neostigmine đối kháng block thần kinh-cơ do aminoglycoside. Hemodialysis có thể loại bỏ plazomicin một phần."
        },
        "administration_instructions": {
            "oral": None,
            "iv": {
                "reconstitution": "Pha với NS (0.9% NaCl) hoặc D5W (5% Dextrose). Nồng độ pha: 5-10mg/ml. Pha 500mg trong 50ml = 10mg/ml. Pha 750mg trong 75ml = 10mg/ml. Lắc kỹ để hòa tan hoàn toàn.",
                "infusion_rate": "Truyền IV trong 30 phút. Tốc độ: 50ml/30 phút = ~1.7ml/phút.",
                "compatibility": ["NS (0.9% NaCl)", "D5W (5% Dextrose)"],
                "incompatibility": [
                    "Beta-lactams - bất hoạt, không pha chung",
                    "Vancomycin - tăng độc thận, tránh dùng cùng",
                    "Các thuốc độc thận khác"
                ],
                "notes": "QUAN TRỌNG: 1) Dùng 1 lần/ngày (15mg/kg dựa trên trọng lượng cơ thể thực tế), 2) Cần TDM (Peak: 50-100 mg/L, Trough: <3 mg/L), 3) CHỐNG CHỈ ĐỊNH ở suy thận nặng (CrCl <15), 4) Theo dõi chức năng thận hàng ngày, 5) Theo dõi thính lực trước và sau điều trị, 6) Không pha chung với beta-lactams, 7) Tránh dùng với vancomycin, furosemide, cisplatin."
            }
        },
        "references": {
            "primary_sources": [
                "FDA Drug Label - Plazomicin (Zemdri)",
                "UpToDate - Plazomicin: Drug Information",
                "Medscape - Plazomicin Drug Reference",
                "IDSA Guidelines - Complicated Urinary Tract Infections",
                "IDSA Guidelines - Antimicrobial Resistance"
            ],
            "last_updated": "2025-02-18",
            "evidence_level": "A - Dựa trên FDA drug labels, IDSA guidelines, và dữ liệu lâm sàng từ nhiều nguồn"
        }
    }
}

__all__ = ['AMINOGLYCOSIDE_ANTIBIOTICS']

