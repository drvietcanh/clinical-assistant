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
            "last_updated": "2025-02-05",
            "evidence_level": "A - Dựa trên FDA drug labels, IDSA guidelines, và dữ liệu lâm sàng từ nhiều nguồn"
        }
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
            "last_updated": "2025-02-05",
            "evidence_level": "A"
        }
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
            "last_updated": "2025-02-05",
            "evidence_level": "A - Dựa trên FDA drug labels, IDSA guidelines, và dữ liệu lâm sàng từ nhiều nguồn"
        }
    }
}

__all__ = ['AMINOGLYCOSIDE_ANTIBIOTICS']

