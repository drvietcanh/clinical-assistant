"""Oncology Medications - Targeted Therapy (Tyrosine Kinase Inhibitors)
Active module - contains targeted therapy TKIs for cancer treatment"""

# Targeted Therapy - Tyrosine Kinase Inhibitors

TARGETED_THERAPY_TKIS_DRUGS = {
    "Erlotinib": {
        "group": "Oncology - EGFR Tyrosine Kinase Inhibitor",
        "vietnamese_name": "Erlotinib, Tarceva",
        "administration": ["PO"],
        "indications": [
            "Ung thư phổi không tế bào nhỏ (NSCLC) - EGFR mutation positive",
            "Ung thư phổi không tế bào nhỏ (NSCLC) - maintenance therapy sau hóa trị",
            "Ung thư tụy (metastatic) - kết hợp với gemcitabine"
        ],
        "contraindications": [
            "Dị ứng erlotinib hoặc bất kỳ thành phần nào"
        ],
        "dosage": {
            "adult_nsclc_egfr_mutation": "150mg PO x 1 lần/ngày",
            "adult_nsclc_maintenance": "150mg PO x 1 lần/ngày",
            "adult_pancreatic": "100mg PO x 1 lần/ngày (với gemcitabine)",
            "notes": "Uống 1 giờ trước hoặc 2 giờ sau bữa ăn (uống khi đói). Erlotinib là EGFR TKI, hiệu quả với NSCLC có EGFR mutation."
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "Không cần điều chỉnh đáng kể",
            "under_30": "Thận trọng, không cần điều chỉnh liều"
        },
        "side_effects": [
            "Phát ban (rash) - RẤT PHỔ BIẾN (75-90%), đặc trưng (acneiform rash)",
            "Tiêu chảy - phổ biến",
            "Mệt mỏi - phổ biến",
            "Ngứa - phổ biến",
            "Khô da - phổ biến",
            "Viêm móng (paronychia) - phổ biến",
            "Buồn nôn, nôn - phổ biến",
            "Chán ăn - phổ biến",
            "Viêm phổi kẽ (interstitial lung disease - ILD) - hiếm nhưng NGUY HIỂM, có thể tử vong",
            "Tăng men gan (ALT, AST) - phổ biến",
            "Xuất huyết (chảy máu) - hiếm"
        ],
        "interactions": [
            "CYP3A4 inhibitors (ketoconazole, itraconazole, ritonavir): tăng nồng độ erlotinib",
            "CYP3A4 inducers (rifampin, carbamazepine): giảm nồng độ erlotinib",
            "CYP1A2 inhibitors (ciprofloxacin): tăng nồng độ erlotinib",
            "Warfarin: tăng nguy cơ chảy máu",
            "Smoking: giảm nồng độ erlotinib (cảm ứng CYP1A2)"
        ],
        "pregnancy": "D",
        "mechanism_of_action": "Erlotinib là tyrosine kinase inhibitor (TKI), ức chế đặc hiệu EGFR (Epidermal Growth Factor Receptor) tyrosine kinase. EGFR là thụ thể trên bề mặt tế bào, khi được kích hoạt bởi EGF hoặc các ligands khác, kích hoạt tín hiệu tăng sinh tế bào (RAS-RAF-MEK-ERK pathway và PI3K-AKT pathway). Trong ung thư phổi, một số bệnh nhân có EGFR mutations (đặc biệt exon 19 deletion và L858R) làm cho EGFR hoạt động liên tục, dẫn đến tăng sinh tế bào ung thư. Erlotinib gắn với vị trí ATP-binding của EGFR, ức chế hoạt tính kinase, ngăn chặn tín hiệu tăng sinh và gây chết tế bào ung thư. ĐẶC ĐIỂM: (1) EGFR TKI, hiệu quả với NSCLC có EGFR mutation, (2) Phát ban (rash) - RẤT PHỔ BIẾN (75-90%), đặc trưng (acneiform rash), có thể là dấu hiệu đáp ứng điều trị, (3) Viêm phổi kẽ (ILD) - hiếm nhưng NGUY HIỂM, có thể tử vong, (4) Uống khi đói (1 giờ trước hoặc 2 giờ sau bữa ăn), (5) Tương tác với CYP3A4 và CYP1A2, (6) Smoking giảm nồng độ erlotinib.",
        "monitoring": [
            "Phát ban (rash) - RẤT PHỔ BIẾN (75-90%), đặc trưng (acneiform rash), có thể là dấu hiệu đáp ứng điều trị",
            "Viêm phổi kẽ (ILD) - hiếm nhưng NGUY HIỂM, có thể tử vong - theo dõi khó thở, ho, sốt",
            "Chức năng gan (ALT, AST, bilirubin) trước và trong điều trị (mỗi tháng trong 3 tháng đầu)",
            "Dấu hiệu tiêu chảy - phổ biến",
            "Dấu hiệu xuất huyết (chảy máu) - hiếm",
            "Đáp ứng điều trị: CT scan mỗi 2-3 tháng",
            "INR nếu dùng với warfarin"
        ],
        "precautions": [
            "PHÁT BAN (RASH) - RẤT PHỔ BIẾN (75-90%), đặc trưng (acneiform rash), có thể là dấu hiệu đáp ứng điều trị, điều trị với corticosteroid tại chỗ hoặc kháng sinh nếu nhiễm trùng",
            "VIÊM PHỔI KẼ (ILD) - hiếm nhưng NGUY HIỂM, có thể tử vong - NGỪNG NGAY nếu có khó thở, ho, sốt, chụp X-quang ngực",
            "Uống khi đói (1 giờ trước hoặc 2 giờ sau bữa ăn) - QUAN TRỌNG (thức ăn tăng hấp thu, tăng độc tính)",
            "Tương tác với CYP3A4 inhibitors/inducers - điều chỉnh liều nếu cần",
            "Tương tác với CYP1A2 inhibitors - điều chỉnh liều nếu cần",
            "Smoking giảm nồng độ erlotinib - khuyến cáo bỏ thuốc lá",
            "Tương tác với warfarin (tăng nguy cơ chảy máu - theo dõi INR)",
            "Theo dõi chức năng gan chặt chẽ (tăng men gan phổ biến)"
        ],
        "pharmacokinetics": {
            "half_life": "36 giờ",
            "onset": "1-2 tuần (tác dụng lâm sàng)",
            "duration": "Dài (dùng hàng ngày)",
            "protein_binding": "93%",
            "metabolism": "Gan (CYP3A4, CYP1A2)",
            "clearance": "Gan (chủ yếu), thận (một phần)"
        },
        "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm, tránh ánh sáng.",
        "black_box_warnings": "VIÊM PHỔI KẼ (Interstitial Lung Disease - ILD) - hiếm nhưng NGUY HIỂM, có thể tử vong. Ngừng ngay erlotinib nếu có khó thở, ho, sốt. Chụp X-quang ngực ngay. Có thể gây xuất huyết (chảy máu) - hiếm.",
        "drug_interactions": {
            "major": [
                {
                    "drug": "CYP3A4 Inhibitors mạnh (Ketoconazole, Itraconazole, Ritonavir)",
                    "mechanism": "Ức chế CYP3A4, tăng nồng độ erlotinib",
                    "effect": "Tăng nồng độ erlotinib, tăng nguy cơ tác dụng phụ",
                    "management": "Thận trọng. Có thể cần giảm liều erlotinib 50%. Theo dõi tác dụng phụ."
                },
                {
                    "drug": "CYP3A4 Inducers mạnh (Rifampin, Carbamazepine, Phenytoin)",
                    "mechanism": "Cảm ứng CYP3A4, giảm nồng độ erlotinib",
                    "effect": "Giảm nồng độ erlotinib, giảm hiệu quả điều trị",
                    "management": "Thận trọng. Có thể cần tăng liều erlotinib. Theo dõi đáp ứng điều trị."
                },
                {
                    "drug": "Warfarin",
                    "mechanism": "Erlotinib ức chế chuyển hóa warfarin",
                    "effect": "Tăng tác dụng chống đông, tăng INR, tăng nguy cơ chảy máu",
                    "management": "Thận trọng. Theo dõi INR chặt chẽ. Có thể cần giảm liều warfarin."
                }
            ],
            "moderate": [
                {
                    "drug": "CYP1A2 Inhibitors (Ciprofloxacin, Fluvoxamine)",
                    "mechanism": "Ức chế CYP1A2, tăng nồng độ erlotinib",
                    "effect": "Tăng nồng độ erlotinib, tăng nguy cơ tác dụng phụ",
                    "management": "Thận trọng. Có thể cần giảm liều erlotinib."
                },
                {
                    "drug": "Smoking",
                    "mechanism": "Smoking cảm ứng CYP1A2, giảm nồng độ erlotinib",
                    "effect": "Giảm nồng độ erlotinib, giảm hiệu quả điều trị",
                    "management": "Khuyến cáo bỏ thuốc lá. Có thể cần tăng liều erlotinib ở người hút thuốc."
                }
            ],
            "minor": []
        },
        "contraindications": {
            "tuyệt_đối": [
                "Dị ứng erlotinib hoặc bất kỳ thành phần nào"
            ],
            "tương_đối": [
                "Viêm phổi kẽ đang hoạt động - tăng nguy cơ ILD",
                "Suy gan nặng - thận trọng, có thể cần giảm liều",
                "Suy thận nặng - thận trọng",
                "Bệnh phổi - tăng nguy cơ ILD"
            ]
        },
        "pregnancy_lactation": {
            "fda_category": "D",
            "pregnancy_details": "Erlotinib phân loại D - có thể gây hại cho thai nhi. Không dùng trong thai kỳ trừ khi lợi ích vượt trội nguy cơ. Có thể gây dị tật thai nhi. Tránh thai hiệu quả trong và sau điều trị.",
            "lactation": {
                "safety": "Incompatible",
                "details": "Erlotinib bài tiết vào sữa mẹ. Không dùng khi cho con bú.",
                "recommendation": "Không dùng khi cho con bú. Ngừng cho con bú hoặc ngừng thuốc."
            }
        },
        "hepatic_adjustment": {
            "mild": "Không đổi",
            "moderate": "Thận trọng, có thể cần giảm liều",
            "severe": "Thận trọng, giảm liều 25-50%",
            "notes": "Erlotinib chuyển hóa qua gan (CYP3A4, CYP1A2). Suy gan có thể làm giảm chuyển hóa, tăng nồng độ và độc tính. Theo dõi chức năng gan và độc tính chặt chẽ."
        },
        "overdose_management": {
            "symptoms": [
                "Phát ban nặng",
                "Tiêu chảy nặng",
                "Viêm phổi kẽ nặng (khó thở, ho, sốt)",
                "Tăng men gan nặng",
                "Xuất huyết (chảy máu)"
            ],
            "antidote": "Không có antidote đặc hiệu. Điều trị hỗ trợ.",
            "treatment": [
                "Ngừng ngay erlotinib",
                "Rửa dạ dày nếu mới uống <1 giờ",
                "Than hoạt tính",
                "Nếu viêm phổi kẽ: ngừng ngay, chụp X-quang ngực, corticosteroid, hỗ trợ hô hấp nếu cần",
                "Điều trị phát ban: corticosteroid tại chỗ, kháng sinh nếu nhiễm trùng",
                "Điều trị tiêu chảy: loperamide, bù dịch",
                "Supportive care: bù dịch, điều trị nhiễm trùng"
            ],
            "monitoring": "Chức năng gan, chức năng thận, X-quang ngực, dấu hiệu nhiễm trùng, dấu hiệu chảy máu, dấu hiệu viêm phổi kẽ"
        },
        "reversal_agents": {
            "available": False,
            "agents": []
        },
        "administration_instructions": {
            "oral": {
                "with_food": "Uống 1 giờ trước hoặc 2 giờ sau bữa ăn (uống khi đói). QUAN TRỌNG: thức ăn tăng hấp thu erlotinib, tăng độc tính.",
                "timing": "NSCLC: 150mg PO x 1 lần/ngày. Pancreatic: 100mg PO x 1 lần/ngày (với gemcitabine). Uống đều đặn cùng một thời điểm mỗi ngày.",
                "notes": "QUAN TRỌNG: 1) Uống khi đói (1 giờ trước hoặc 2 giờ sau bữa ăn), 2) PHÁT BAN - RẤT PHỔ BIẾN (75-90%), có thể là dấu hiệu đáp ứng điều trị, 3) VIÊM PHỔI KẼ - hiếm nhưng NGUY HIỂM, ngừng ngay nếu có, 4) Tương tác với CYP3A4 và CYP1A2, 5) Smoking giảm nồng độ erlotinib."
            }
        },
        "references": {
            "primary_sources": [
                "FDA Drug Label - Erlotinib (Tarceva)",
                "UpToDate - Erlotinib: Drug Information",
                "NCCN Guidelines - Non-Small Cell Lung Cancer",
                "Goodman & Gilman's The Pharmacological Basis of Therapeutics"
            ],
            "last_updated": "2025-02-18",
            "evidence_level": "High - FDA-approved, extensive clinical data, effective for EGFR mutation positive NSCLC"
        }
    },

    "Gefitinib": {
        "group": "Oncology - EGFR Tyrosine Kinase Inhibitor",
        "vietnamese_name": "Gefitinib, Iressa",
        "administration": ["PO"],
        "indications": [
            "Ung thư phổi không tế bào nhỏ (NSCLC) - EGFR mutation positive",
            "Ung thư phổi không tế bào nhỏ (NSCLC) - first-line treatment cho EGFR mutation positive"
        ],
        "contraindications": [
            "Dị ứng gefitinib hoặc bất kỳ thành phần nào"
        ],
        "dosage": {
            "adult_standard": "250mg PO x 1 lần/ngày",
            "notes": "Uống với hoặc không thức ăn. Gefitinib là EGFR TKI, tương tự erlotinib, hiệu quả với NSCLC có EGFR mutation."
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "Không cần điều chỉnh đáng kể",
            "under_30": "Thận trọng, không cần điều chỉnh liều"
        },
        "side_effects": [
            "Phát ban (rash) - RẤT PHỔ BIẾN (75-90%), đặc trưng (acneiform rash)",
            "Tiêu chảy - phổ biến",
            "Mệt mỏi - phổ biến",
            "Ngứa - phổ biến",
            "Khô da - phổ biến",
            "Viêm móng (paronychia) - phổ biến",
            "Buồn nôn, nôn - phổ biến",
            "Chán ăn - phổ biến",
            "Viêm phổi kẽ (interstitial lung disease - ILD) - hiếm nhưng NGUY HIỂM, có thể tử vong",
            "Tăng men gan (ALT, AST) - phổ biến",
            "Xuất huyết (chảy máu) - hiếm"
        ],
        "interactions": [
            "CYP3A4 inhibitors (ketoconazole, itraconazole, ritonavir): tăng nồng độ gefitinib",
            "CYP3A4 inducers (rifampin, carbamazepine): giảm nồng độ gefitinib",
            "Warfarin: tăng nguy cơ chảy máu",
            "Proton pump inhibitors (PPIs): giảm hấp thu gefitinib (tăng pH dạ dày)"
        ],
        "pregnancy": "D",
        "mechanism_of_action": "Gefitinib là tyrosine kinase inhibitor (TKI), ức chế đặc hiệu EGFR (Epidermal Growth Factor Receptor) tyrosine kinase, tương tự erlotinib. Gefitinib gắn với vị trí ATP-binding của EGFR, ức chế hoạt tính kinase, ngăn chặn tín hiệu tăng sinh và gây chết tế bào ung thư. Hiệu quả với NSCLC có EGFR mutations (đặc biệt exon 19 deletion và L858R). ĐẶC ĐIỂM: (1) EGFR TKI, hiệu quả với NSCLC có EGFR mutation, (2) Phát ban (rash) - RẤT PHỔ BIẾN (75-90%), đặc trưng (acneiform rash), có thể là dấu hiệu đáp ứng điều trị, (3) Viêm phổi kẽ (ILD) - hiếm nhưng NGUY HIỂM, có thể tử vong, (4) Có thể uống với hoặc không thức ăn (khác với erlotinib phải uống khi đói), (5) Tương tác với CYP3A4, (6) Tương tác với PPIs (giảm hấp thu do tăng pH dạ dày).",
        "monitoring": [
            "Phát ban (rash) - RẤT PHỔ BIẾN (75-90%), đặc trưng (acneiform rash), có thể là dấu hiệu đáp ứng điều trị",
            "Viêm phổi kẽ (ILD) - hiếm nhưng NGUY HIỂM, có thể tử vong - theo dõi khó thở, ho, sốt",
            "Chức năng gan (ALT, AST, bilirubin) trước và trong điều trị (mỗi tháng trong 3 tháng đầu)",
            "Dấu hiệu tiêu chảy - phổ biến",
            "Dấu hiệu xuất huyết (chảy máu) - hiếm",
            "Đáp ứng điều trị: CT scan mỗi 2-3 tháng",
            "INR nếu dùng với warfarin"
        ],
        "precautions": [
            "PHÁT BAN (RASH) - RẤT PHỔ BIẾN (75-90%), đặc trưng (acneiform rash), có thể là dấu hiệu đáp ứng điều trị, điều trị với corticosteroid tại chỗ hoặc kháng sinh nếu nhiễm trùng",
            "VIÊM PHỔI KẼ (ILD) - hiếm nhưng NGUY HIỂM, có thể tử vong - NGỪNG NGAY nếu có khó thở, ho, sốt, chụp X-quang ngực",
            "Có thể uống với hoặc không thức ăn (khác với erlotinib phải uống khi đói)",
            "Tương tác với CYP3A4 inhibitors/inducers - điều chỉnh liều nếu cần",
            "Tương tác với PPIs (giảm hấp thu do tăng pH dạ dày) - tránh dùng đồng thời hoặc dùng H2 blocker thay thế",
            "Tương tác với warfarin (tăng nguy cơ chảy máu - theo dõi INR)",
            "Theo dõi chức năng gan chặt chẽ (tăng men gan phổ biến)"
        ],
        "pharmacokinetics": {
            "half_life": "48 giờ",
            "onset": "1-2 tuần (tác dụng lâm sàng)",
            "duration": "Dài (dùng hàng ngày)",
            "protein_binding": "90%",
            "metabolism": "Gan (CYP3A4)",
            "clearance": "Gan (chủ yếu), thận (một phần)"
        },
        "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm, tránh ánh sáng.",
        "black_box_warnings": "VIÊM PHỔI KẼ (Interstitial Lung Disease - ILD) - hiếm nhưng NGUY HIỂM, có thể tử vong. Ngừng ngay gefitinib nếu có khó thở, ho, sốt. Chụp X-quang ngực ngay. Có thể gây xuất huyết (chảy máu) - hiếm.",
        "drug_interactions": {
            "major": [
                {
                    "drug": "CYP3A4 Inhibitors mạnh (Ketoconazole, Itraconazole, Ritonavir)",
                    "mechanism": "Ức chế CYP3A4, tăng nồng độ gefitinib",
                    "effect": "Tăng nồng độ gefitinib, tăng nguy cơ tác dụng phụ",
                    "management": "Thận trọng. Có thể cần giảm liều gefitinib 50%. Theo dõi tác dụng phụ."
                },
                {
                    "drug": "CYP3A4 Inducers mạnh (Rifampin, Carbamazepine, Phenytoin)",
                    "mechanism": "Cảm ứng CYP3A4, giảm nồng độ gefitinib",
                    "effect": "Giảm nồng độ gefitinib, giảm hiệu quả điều trị",
                    "management": "Thận trọng. Có thể cần tăng liều gefitinib. Theo dõi đáp ứng điều trị."
                },
                {
                    "drug": "Warfarin",
                    "mechanism": "Gefitinib ức chế chuyển hóa warfarin",
                    "effect": "Tăng tác dụng chống đông, tăng INR, tăng nguy cơ chảy máu",
                    "management": "Thận trọng. Theo dõi INR chặt chẽ. Có thể cần giảm liều warfarin."
                }
            ],
            "moderate": [
                {
                    "drug": "Proton Pump Inhibitors (PPIs - Omeprazole, Lansoprazole, Esomeprazole)",
                    "mechanism": "PPIs tăng pH dạ dày, giảm hấp thu gefitinib (gefitinib hòa tan tốt hơn ở pH thấp)",
                    "effect": "Giảm hấp thu gefitinib, giảm nồng độ, giảm hiệu quả điều trị",
                    "management": "Tránh dùng đồng thời. Dùng H2 blocker thay thế (cách xa gefitinib ít nhất 2 giờ) hoặc dùng antacid (cách xa gefitinib ít nhất 2 giờ)."
                }
            ],
            "minor": []
        },
        "contraindications": {
            "tuyệt_đối": [
                "Dị ứng gefitinib hoặc bất kỳ thành phần nào"
            ],
            "tương_đối": [
                "Viêm phổi kẽ đang hoạt động - tăng nguy cơ ILD",
                "Suy gan nặng - thận trọng, có thể cần giảm liều",
                "Suy thận nặng - thận trọng",
                "Bệnh phổi - tăng nguy cơ ILD"
            ]
        },
        "pregnancy_lactation": {
            "fda_category": "D",
            "pregnancy_details": "Gefitinib phân loại D - có thể gây hại cho thai nhi. Không dùng trong thai kỳ trừ khi lợi ích vượt trội nguy cơ. Có thể gây dị tật thai nhi. Tránh thai hiệu quả trong và sau điều trị.",
            "lactation": {
                "safety": "Incompatible",
                "details": "Gefitinib bài tiết vào sữa mẹ. Không dùng khi cho con bú.",
                "recommendation": "Không dùng khi cho con bú. Ngừng cho con bú hoặc ngừng thuốc."
            }
        },
        "hepatic_adjustment": {
            "mild": "Không đổi",
            "moderate": "Thận trọng, có thể cần giảm liều",
            "severe": "Thận trọng, giảm liều 25-50%",
            "notes": "Gefitinib chuyển hóa qua gan (CYP3A4). Suy gan có thể làm giảm chuyển hóa, tăng nồng độ và độc tính. Theo dõi chức năng gan và độc tính chặt chẽ."
        },
        "overdose_management": {
            "symptoms": [
                "Phát ban nặng",
                "Tiêu chảy nặng",
                "Viêm phổi kẽ nặng (khó thở, ho, sốt)",
                "Tăng men gan nặng",
                "Xuất huyết (chảy máu)"
            ],
            "antidote": "Không có antidote đặc hiệu. Điều trị hỗ trợ.",
            "treatment": [
                "Ngừng ngay gefitinib",
                "Rửa dạ dày nếu mới uống <1 giờ",
                "Than hoạt tính",
                "Nếu viêm phổi kẽ: ngừng ngay, chụp X-quang ngực, corticosteroid, hỗ trợ hô hấp nếu cần",
                "Điều trị phát ban: corticosteroid tại chỗ, kháng sinh nếu nhiễm trùng",
                "Điều trị tiêu chảy: loperamide, bù dịch",
                "Supportive care: bù dịch, điều trị nhiễm trùng"
            ],
            "monitoring": "Chức năng gan, chức năng thận, X-quang ngực, dấu hiệu nhiễm trùng, dấu hiệu chảy máu, dấu hiệu viêm phổi kẽ"
        },
        "reversal_agents": {
            "available": False,
            "agents": []
        },
        "administration_instructions": {
            "oral": {
                "with_food": "Có thể uống với hoặc không thức ăn. Không ảnh hưởng đáng kể đến hấp thu (khác với erlotinib phải uống khi đói).",
                "timing": "250mg PO x 1 lần/ngày. Uống đều đặn cùng một thời điểm mỗi ngày.",
                "notes": "QUAN TRỌNG: 1) Có thể uống với hoặc không thức ăn, 2) PHÁT BAN - RẤT PHỔ BIẾN (75-90%), có thể là dấu hiệu đáp ứng điều trị, 3) VIÊM PHỔI KẼ - hiếm nhưng NGUY HIỂM, ngừng ngay nếu có, 4) Tương tác với CYP3A4, 5) Tránh dùng với PPIs (dùng H2 blocker thay thế)."
            }
        },
        "references": {
            "primary_sources": [
                "FDA Drug Label - Gefitinib (Iressa)",
                "UpToDate - Gefitinib: Drug Information",
                "NCCN Guidelines - Non-Small Cell Lung Cancer",
                "Goodman & Gilman's The Pharmacological Basis of Therapeutics"
            ],
            "last_updated": "2025-02-18",
            "evidence_level": "High - FDA-approved, extensive clinical data, effective for EGFR mutation positive NSCLC"
        }
    },
    "Imatinib": {
        "group": "Oncology - BCR-ABL Tyrosine Kinase Inhibitor",
        "vietnamese_name": "Imatinib, Gleevec, Glivec",
        "administration": ["PO"],
        "indications": [
            "Bệnh bạch cầu dòng tủy mạn (CML - Chronic Myeloid Leukemia) - tất cả các giai đoạn",
            "Bệnh bạch cầu lympho cấp (ALL) - Ph+ (Philadelphia chromosome positive)",
            "U mô đệm đường tiêu hóa (GIST - Gastrointestinal Stromal Tumor)",
            "U xơ da (DFSP - Dermatofibrosarcoma Protuberans)",
            "Hội chứng tăng bạch cầu ái toan (HES - Hypereosinophilic Syndrome)",
            "U tế bào mast hệ thống (SM - Systemic Mastocytosis)"
        ],
        "contraindications": [
            "Dị ứng imatinib hoặc bất kỳ thành phần nào"
        ],
        "dosage": {
            "adult_cml_chronic": "400mg PO x 1 lần/ngày",
            "adult_cml_accelerated": "600mg PO x 1 lần/ngày",
            "adult_cml_blast_crisis": "600mg PO x 1 lần/ngày",
            "adult_all_ph_positive": "600mg PO x 1 lần/ngày",
            "adult_gist": "400mg PO x 1 lần/ngày",
            "notes": "Uống với thức ăn và một cốc nước lớn để giảm kích ứng dạ dày. Có thể tăng liều nếu không đáp ứng. Imatinib là thuốc đầu tiên trong nhóm TKI, đã cách mạng hóa điều trị CML."
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "Giảm liều 25-50%",
            "under_30": "Giảm liều 50%"
        },
        "side_effects": [
            "Giữ nước, phù (fluid retention, edema) - phổ biến",
            "Buồn nôn, nôn - phổ biến",
            "Tiêu chảy - phổ biến",
            "Đau cơ, đau khớp - phổ biến",
            "Phát ban - phổ biến",
            "Mệt mỏi - phổ biến",
            "Giảm bạch cầu, tiểu cầu (myelosuppression) - phổ biến",
            "Tăng men gan (ALT, AST) - phổ biến",
            "Độc tim (suy tim, rối loạn nhịp) - hiếm nhưng nghiêm trọng",
            "Xuất huyết (chảy máu) - hiếm"
        ],
        "interactions": [
            "CYP3A4 inhibitors (ketoconazole, itraconazole, ritonavir): tăng nồng độ imatinib",
            "CYP3A4 inducers (rifampin, carbamazepine): giảm nồng độ imatinib",
            "Warfarin: tăng nguy cơ chảy máu - dùng thuốc chống đông khác",
            "Simvastatin, atorvastatin: tăng nguy cơ tiêu cơ vân"
        ],
        "pregnancy": "D",
        "mechanism_of_action": "Imatinib là tyrosine kinase inhibitor (TKI), ức chế đặc hiệu BCR-ABL tyrosine kinase (fusion protein trong CML do translocation t(9;22) tạo ra Philadelphia chromosome). BCR-ABL là protein bất thường có hoạt tính tyrosine kinase liên tục, kích thích tăng sinh và ức chế apoptosis của tế bào bạch cầu, dẫn đến CML. Imatinib gắn với vị trí ATP-binding của BCR-ABL, ức chế hoạt tính kinase, ngăn chặn tín hiệu tăng sinh và khôi phục apoptosis. Imatinib cũng ức chế các tyrosine kinase khác: c-KIT (trong GIST), PDGFR (platelet-derived growth factor receptor). ĐẶC ĐIỂM: (1) Thuốc đầu tiên trong nhóm TKI, đã cách mạng hóa điều trị CML (từ 30% sống 5 năm → 90% sống 5 năm), (2) Uống hàng ngày, tiện lợi, (3) Tác dụng phụ thường nhẹ đến trung bình, (4) Có thể phát triển kháng thuốc (mutations) → cần TKI thế hệ 2 (dasatinib, nilotinib), (5) Hiệu quả cao với CML chronic phase (90% đạt complete cytogenetic response).",
        "monitoring": [
            "Công thức máu toàn phần (CBC) mỗi 2 tuần trong 3 tháng đầu, sau đó mỗi tháng - theo dõi myelosuppression",
            "Chức năng gan (ALT, AST, bilirubin) mỗi tháng trong 3 tháng đầu, sau đó mỗi 3 tháng",
            "Chức năng thận (creatinine, eGFR) trước và trong điều trị",
            "Đáp ứng điều trị CML:",
            "  - Complete hematologic response (CHR): CBC bình thường",
            "  - Complete cytogenetic response (CCyR): không còn Philadelphia chromosome",
            "  - Major molecular response (MMR): BCR-ABL <0.1%",
            "Dấu hiệu giữ nước, phù (fluid retention) - phổ biến",
            "Dấu hiệu độc tim (suy tim, rối loạn nhịp) - hiếm nhưng nghiêm trọng",
            "Dấu hiệu xuất huyết (chảy máu) - hiếm"
        ],
        "precautions": [
            "GIỮ NƯỚC, PHÙ - phổ biến, có thể nặng, điều trị với furosemide nếu cần",
            "Tăng men gan - phổ biến, theo dõi ALT/AST, giảm liều hoặc ngừng nếu nặng",
            "Myelosuppression - phổ biến, theo dõi CBC, giảm liều hoặc trì hoãn nếu nặng",
            "Độc tim - hiếm nhưng nghiêm trọng, ngừng ngay nếu có suy tim",
            "Tương tác với CYP3A4 inhibitors/inducers - điều chỉnh liều nếu cần",
            "Tương tác với warfarin - dùng thuốc chống đông khác",
            "Uống với thức ăn và một cốc nước lớn để giảm kích ứng dạ dày",
            "Có thể phát triển kháng thuốc (mutations) → cần TKI thế hệ 2",
            "Theo dõi đáp ứng điều trị (CHR, CCyR, MMR)"
        ],
        "pharmacokinetics": {
            "half_life": "18 giờ",
            "onset": "1-2 tuần (tác dụng lâm sàng)",
            "duration": "Dài (dùng hàng ngày)",
            "protein_binding": "95%",
            "metabolism": "Gan (CYP3A4, CYP2D6, CYP2C9, CYP2C19)",
            "clearance": "Gan (chủ yếu), thận (một phần)"
        },
        "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm, tránh ánh sáng.",
        "black_box_warnings": "Có thể gây độc tim (suy tim, rối loạn nhịp) - hiếm nhưng nghiêm trọng. Ngừng ngay nếu có suy tim. Có thể gây xuất huyết (chảy máu) - hiếm. Theo dõi chức năng tim và dấu hiệu xuất huyết.",
        "drug_interactions": {
            "major": [
                {
                    "drug": "CYP3A4 Inhibitors mạnh (Ketoconazole, Itraconazole, Ritonavir)",
                    "mechanism": "Ức chế CYP3A4, tăng nồng độ imatinib",
                    "effect": "Tăng nồng độ imatinib, tăng nguy cơ tác dụng phụ",
                    "management": "Thận trọng. Có thể cần giảm liều imatinib 50%. Theo dõi tác dụng phụ."
                },
                {
                    "drug": "CYP3A4 Inducers mạnh (Rifampin, Carbamazepine, Phenytoin)",
                    "mechanism": "Cảm ứng CYP3A4, giảm nồng độ imatinib",
                    "effect": "Giảm nồng độ imatinib, giảm hiệu quả điều trị",
                    "management": "Thận trọng. Có thể cần tăng liều imatinib. Theo dõi đáp ứng điều trị."
                },
                {
                    "drug": "Warfarin",
                    "mechanism": "Imatinib ức chế chuyển hóa warfarin",
                    "effect": "Tăng tác dụng chống đông, tăng INR, tăng nguy cơ chảy máu",
                    "management": "TRÁNH DÙNG warfarin. Dùng thuốc chống đông khác (LMWH, DOAC). Nếu bắt buộc, theo dõi INR chặt chẽ."
                }
            ],
            "moderate": [
                {
                    "drug": "Simvastatin, Atorvastatin",
                    "mechanism": "Imatinib ức chế CYP3A4, tăng nồng độ statin",
                    "effect": "Tăng nồng độ statin, tăng nguy cơ tiêu cơ vân",
                    "management": "Thận trọng. Có thể cần giảm liều statin hoặc dùng statin khác (pravastatin, rosuvastatin)."
                }
            ],
            "minor": []
        },
        "contraindications": {
            "tuyệt_đối": [
                "Dị ứng imatinib hoặc bất kỳ thành phần nào"
            ],
            "tương_đối": [
                "Suy thận nặng (CrCl <30) - giảm liều 50%",
                "Suy gan nặng - thận trọng, có thể cần giảm liều",
                "Bệnh tim - tăng nguy cơ độc tim",
                "Giảm bạch cầu/tiểu cầu nặng - trì hoãn điều trị"
            ]
        },
        "pregnancy_lactation": {
            "fda_category": "D",
            "pregnancy_details": "Imatinib phân loại D - có thể gây hại cho thai nhi. Không dùng trong thai kỳ trừ khi lợi ích vượt trội nguy cơ. Có thể gây dị tật thai nhi. Tránh thai hiệu quả trong và sau điều trị.",
            "lactation": {
                "safety": "Incompatible",
                "details": "Imatinib bài tiết vào sữa mẹ. Không dùng khi cho con bú.",
                "recommendation": "Không dùng khi cho con bú. Ngừng cho con bú hoặc ngừng thuốc."
            }
        },
        "hepatic_adjustment": {
            "mild": "Không đổi",
            "moderate": "Thận trọng, có thể cần giảm liều",
            "severe": "Thận trọng, giảm liều 25-50%",
            "notes": "Imatinib chuyển hóa qua gan (CYP3A4, CYP2D6, CYP2C9, CYP2C19). Suy gan có thể làm giảm chuyển hóa, tăng nồng độ và độc tính. Theo dõi chức năng gan và độc tính chặt chẽ."
        },
        "overdose_management": {
            "symptoms": [
                "Giữ nước, phù nặng",
                "Buồn nôn, nôn nặng",
                "Tiêu chảy nặng",
                "Giảm bạch cầu, tiểu cầu nặng",
                "Tăng men gan nặng",
                "Độc tim (suy tim, rối loạn nhịp)",
                "Xuất huyết (chảy máu)"
            ],
            "antidote": "Không có antidote đặc hiệu. Điều trị hỗ trợ.",
            "treatment": [
                "Ngừng ngay imatinib",
                "Rửa dạ dày nếu mới uống <1 giờ",
                "Than hoạt tính",
                "Điều trị giữ nước: furosemide, hạn chế muối",
                "Điều trị độc tim: hỗ trợ tim mạch nếu cần",
                "Supportive care: bù dịch, điều trị nhiễm trùng, truyền máu nếu cần",
                "Theo dõi CBC, chức năng gan, chức năng thận, ECG"
            ],
            "monitoring": "CBC, chức năng gan, chức năng thận, ECG, dấu hiệu nhiễm trùng, dấu hiệu chảy máu, dấu hiệu độc tim"
        },
        "reversal_agents": {
            "available": False,
            "agents": []
        },
        "administration_instructions": {
            "oral": {
                "with_food": "Uống với thức ăn và một cốc nước lớn để giảm kích ứng dạ dày.",
                "timing": "CML chronic: 400mg PO x 1 lần/ngày. CML accelerated/blast crisis: 600mg PO x 1 lần/ngày. GIST: 400mg PO x 1 lần/ngày. Uống đều đặn cùng một thời điểm mỗi ngày.",
                "notes": "QUAN TRỌNG: 1) Uống với thức ăn và một cốc nước lớn, 2) Giữ nước, phù - phổ biến, 3) Theo dõi CBC và chức năng gan chặt chẽ, 4) Có thể phát triển kháng thuốc → cần TKI thế hệ 2, 5) Tương tác với CYP3A4 inhibitors/inducers."
            }
        },
        "references": {
            "primary_sources": [
                "FDA Drug Label - Imatinib (Gleevec)",
                "UpToDate - Imatinib: Drug Information",
                "NCCN Guidelines - Chronic Myeloid Leukemia",
                "Goodman & Gilman's The Pharmacological Basis of Therapeutics"
            ],
            "last_updated": "2025-02-18",
            "evidence_level": "High - FDA-approved, revolutionized CML treatment, extensive clinical data"
        }
    },

    "Sotorasib": {
        "group": "Oncology - KRAS G12C Inhibitor",
        "vietnamese_name": "Sotorasib, Lumakras",
        "administration": ["PO"],
        "indications": [
            "Ung thư phổi không tế bào nhỏ (NSCLC) - KRAS G12C mutation, đã điều trị trước đó"
        ],
        "contraindications": [
            "Dị ứng sotorasib hoặc bất kỳ thành phần nào"
        ],
        "dosage": {
            "adult_standard": "960mg PO x 1 lần/ngày",
            "notes": "Uống với hoặc không thức ăn. Điều trị cho đến khi bệnh tiến triển hoặc độc tính không chấp nhận được. FDA phê duyệt 5/28/2021."
        },
        "renal_adjustment": {
            "normal": "Không cần chỉnh liều",
            "30_60": "Không cần chỉnh liều",
            "under_30": "Thận trọng, dữ liệu hạn chế"
        },
        "side_effects": [
            "Tiêu chảy - phổ biến",
            "Buồn nôn - phổ biến",
            "Tăng men gan (ALT, AST) - phổ biến, có thể nghiêm trọng",
            "Mệt mỏi - phổ biến",
            "Đau cơ, đau khớp - phổ biến",
            "Ho - phổ biến",
            "Viêm phổi kẽ (interstitial lung disease - ILD) - hiếm nhưng NGUY HIỂM",
            "Tăng amylase, lipase - phổ biến"
        ],
        "interactions": [
            "CYP3A4 inducers (rifampin, carbamazepine): giảm nồng độ sotorasib - TRÁNH hoặc tăng liều",
            "CYP3A4 inhibitors (ketoconazole): tăng nồng độ sotorasib - thận trọng"
        ],
        "pregnancy": "D",
        "mechanism_of_action": "Sotorasib là KRAS G12C inhibitor, ức chế KRAS G12C protein. KRAS là oncogene quan trọng, đột biến KRAS G12C xảy ra ở ~13% NSCLC. Sotorasib gắn với KRAS G12C ở trạng thái GDP-bound → giữ KRAS ở trạng thái inactive → ức chế signaling → giảm tăng sinh tế bào ung thư. Sotorasib được FDA phê duyệt 5/28/2021 để điều trị NSCLC có KRAS G12C mutation, đã điều trị trước đó.",
        "monitoring": [
            "Chức năng gan (ALT, AST) - QUAN TRỌNG: theo dõi trước điều trị và mỗi 3 tuần",
            "Amylase, lipase - theo dõi định kỳ",
            "Dấu hiệu viêm phổi kẽ (ILD) - ho, khó thở - QUAN TRỌNG",
            "Đáp ứng điều trị (CT scan) - đánh giá mỗi 6-8 tuần",
            "KRAS G12C mutation status - cần xác nhận trước điều trị"
        ],
        "precautions": [
            "VIÊM PHỔI KẼ (ILD) - hiếm nhưng NGUY HIỂM. Ngừng ngay nếu có dấu hiệu ILD.",
            "Tăng men gan - phổ biến, có thể nghiêm trọng. Theo dõi chức năng gan trước điều trị và mỗi 3 tuần.",
            "CHỐNG CHỈ ĐỊNH trong thai kỳ (category D)",
            "Cần test KRAS G12C mutation trước điều trị"
        ],
        "pharmacokinetics": {
            "half_life": "~5 giờ",
            "onset": "Vài tuần",
            "duration": "Ngắn (cần dùng hàng ngày)",
            "protein_binding": "~89%",
            "metabolism": "Chuyển hóa qua CYP3A4",
            "clearance": "Thải trừ qua thận và gan"
        },
        "storage": "Bảo quản ở nhiệt độ phòng (20-25°C), tránh ẩm, tránh ánh sáng",
        "black_box_warnings": "VIÊM PHỔI KẼ (ILD) - có thể gây viêm phổi kẽ nghiêm trọng. Ngừng ngay nếu có dấu hiệu ILD. TĂNG MEN GAN - có thể gây tăng men gan nghiêm trọng. CHỐNG CHỈ ĐỊNH trong thai kỳ (category D).",
        "drug_interactions": {
            "major": [
                {
                    "drug": "CYP3A4 inducers mạnh (rifampin, carbamazepine)",
                    "mechanism": "Cảm ứng CYP3A4 → tăng chuyển hóa sotorasib",
                    "effect": "Giảm nồng độ sotorasib, giảm hiệu quả",
                    "management": "TRÁNH hoặc tăng liều sotorasib."
                }
            ],
            "moderate": [],
            "minor": []
        },
        "contraindications_detail": {
            "tuyệt_đối": [
                "Dị ứng sotorasib hoặc bất kỳ thành phần nào",
                "Có thai (category D) - CHỐNG CHỈ ĐỊNH"
            ],
            "tương_đối": []
        },
        "pregnancy_lactation": {
            "fda_category": "D",
            "pregnancy_details": "CHỐNG CHỈ ĐỊNH trong thai kỳ. Sotorasib là FDA category D - có nguy cơ cho thai nhi.",
            "lactation": {
                "safety": "Unknown",
                "details": "Chưa biết có bài tiết vào sữa mẹ hay không.",
                "recommendation": "Không dùng khi cho con bú."
            }
        },
        "hepatic_adjustment": {
            "mild": "Không đổi",
            "moderate": "Thận trọng",
            "severe": "Thận trọng, dữ liệu hạn chế",
            "notes": "Sotorasib chuyển hóa qua CYP3A4 ở gan."
        },
        "overdose_management": {
            "symptoms": ["Tăng men gan nặng", "Tiêu chảy nặng"],
            "antidote": "Không có antidote đặc hiệu",
            "treatment": ["Ngừng sotorasib", "Theo dõi chức năng gan", "Điều trị hỗ trợ"],
            "monitoring": "Dấu hiệu sinh tồn, chức năng gan, dấu hiệu ILD"
        },
        "reversal_agents": {
            "available": False,
            "agents": []
        },
        "administration_instructions": {
            "oral": {
                "with_food": "Uống với hoặc không thức ăn",
                "timing": "Uống 1 lần/ngày, 960mg mỗi lần."
            }
        },
        "references": {
            "primary_sources": [
                "FDA Drug Label - Sotorasib (Lumakras)",
                "FDA Approval Date: 5/28/2021",
                "FDA-approved use: To treat types of non-small cell lung cancer",
                "UpToDate - Sotorasib: Drug information"
            ],
            "last_updated": "2025-02-18",
            "evidence_level": "A - FDA-approved 5/28/2021"
        },
        "risk_flags": {
            "high_alert": True,
            "narrow_therapeutic_index": False,
            "bleeding_risk": False,
            "organ_toxicity": ["Hepatic (elevated transaminases)", "Pulmonary (interstitial lung disease - ILD)"],
            "qt_prolongation": False,
            "hepatotoxicity": True,
            "nephrotoxicity": False,
            "requires_monitoring": ["Hepatic function (ALT, AST) - CRITICAL", "Signs of ILD - CRITICAL", "KRAS G12C mutation status"]
        },
        "guideline_tags": [
            "NCCN Guidelines - Non-Small Cell Lung Cancer",
            "FDA Black Box Warning - Sotorasib and ILD",
            "FDA Drug Information - Sotorasib (Lumakras)"
        ],
        "last_updated": "2025-02-18"
    },

    "Scemblix": {
        "group": "FDA Approved 10/29/2021",
        "vietnamese_name": "Asciminib, Scemblix",
        "administration": ["PO"],
        "indications": [
            "Bạch cầu mạn dòng tủy (CML) có nhiễm sắc thể Philadelphia (Ph+) đã điều trị trước đó với ít nhất 2 TKIs",
            "CML Ph+ kháng trị hoặc không dung nạp với các TKI khác"
        ],
        "contraindications": {
            "tuyệt_đối": [
                "Dị ứng asciminib hoặc bất kỳ thành phần nào"
            ],
            "tương_đối": [
                "Suy gan nặng - thận trọng",
                "Suy thận nặng - thận trọng",
                "QT kéo dài - thận trọng"
            ]
        },
        "dosage": {
            "adult_standard": "80mg PO x 1 lần/ngày hoặc 40mg PO x 2 lần/ngày",
            "notes": "Uống với hoặc không có thức ăn. Asciminib là STAMP inhibitor (Allosteric TKI), khác với các TKI khác. FDA phê duyệt 10/29/2021 cho CML Ph+ đã điều trị trước đó với ít nhất 2 TKIs."
        },
        "renal_adjustment": {
            "normal": "Không cần chỉnh liều",
            "30_60": "Thận trọng, không cần chỉnh liều",
            "under_30": "Thận trọng, dữ liệu hạn chế"
        },
        "side_effects": [
            "Giảm bạch cầu (neutropenia) - phổ biến",
            "Giảm tiểu cầu (thrombocytopenia) - phổ biến",
            "Giảm hồng cầu (anemia) - phổ biến",
            "Tăng men gan (ALT, AST) - phổ biến",
            "Tăng lipase - phổ biến",
            "Tăng amylase - phổ biến",
            "Đau đầu - phổ biến",
            "Mệt mỏi - phổ biến",
            "Buồn nôn - phổ biến",
            "Tiêu chảy - phổ biến",
            "Đau cơ (myalgia) - phổ biến",
            "Đau khớp (arthralgia) - phổ biến",
            "QT kéo dài - không phổ biến nhưng quan trọng",
            "Viêm tụy - không phổ biến"
        ],
        "interactions": [
            "CYP3A4 inhibitors (ketoconazole, itraconazole, ritonavir): tăng nồng độ asciminib",
            "CYP3A4 inducers (rifampin, carbamazepine): giảm nồng độ asciminib",
            "Thuốc kéo dài QT: tăng nguy cơ QT kéo dài"
        ],
        "pregnancy": "D",
        "mechanism_of_action": "Asciminib là STAMP inhibitor (Specifically Targeting the ABL Myristoyl Pocket), một loại allosteric TKI khác với các TKI ATP-competitive truyền thống (như imatinib, nilotinib, dasatinib). Asciminib gắn với myristoyl pocket của BCR-ABL, một vị trí allosteric, dẫn đến: (1) Ức chế hoạt tính kinase của BCR-ABL, (2) Ức chế tăng sinh tế bào CML, (3) Gây chết tế bào CML. ĐẶC ĐIỂM: (1) Allosteric TKI, khác với các TKI ATP-competitive, (2) Hiệu quả với CML Ph+ kháng trị với các TKI khác, (3) Tác dụng phụ tương tự các TKI khác (giảm tế bào máu, tăng men gan), (4) Có thể gây QT kéo dài, (5) FDA phê duyệt 10/29/2021 cho CML Ph+ đã điều trị trước đó với ít nhất 2 TKIs.",
        "monitoring": [
            "Công thức máu: CBC với phân loại (giảm tế bào máu phổ biến) - QUAN TRỌNG",
            "Chức năng gan: ALT, AST, bilirubin (tăng men gan phổ biến)",
            "Lipase, amylase (tăng phổ biến, viêm tụy không phổ biến)",
            "ECG: QT interval (QT kéo dài không phổ biến nhưng quan trọng)",
            "Đáp ứng điều trị: BCR-ABL transcript levels, cytogenetic response",
            "Dấu hiệu viêm tụy: đau bụng, tăng lipase/amylase"
        ],
        "precautions": [
            "GIẢM TẾ BÀO MÁU - phổ biến. Theo dõi CBC thường xuyên. Có thể cần giảm liều hoặc ngừng tạm thời nếu giảm tế bào máu nặng.",
            "TĂNG MEN GAN - phổ biến. Theo dõi chức năng gan định kỳ.",
            "QT KÉO DÀI - không phổ biến nhưng quan trọng. Theo dõi ECG trước và trong điều trị.",
            "Tăng lipase/amylase - phổ biến. Viêm tụy không phổ biến nhưng cần theo dõi.",
            "Tương tác với CYP3A4 inhibitors/inducers - điều chỉnh liều nếu cần",
            "Thận trọng với thuốc kéo dài QT (tăng nguy cơ QT kéo dài)",
            "Uống với hoặc không có thức ăn"
        ],
        "pharmacokinetics": {
            "half_life": "Khoảng 15-20 giờ",
            "onset": "Vài tuần đến vài tháng (tác dụng lâm sàng)",
            "duration": "Dài (dùng hàng ngày)",
            "protein_binding": ">99%",
            "metabolism": "Gan (CYP3A4 chủ yếu)",
            "clearance": "Gan (chủ yếu), thận (một phần)"
        },
        "storage": "Bảo quản ở nhiệt độ phòng (20-25°C), tránh ẩm. Bảo quản trong hộp kín gốc. Để xa tầm tay trẻ em.",
        "black_box_warnings": "Không có black box warning. Tuy nhiên, cần cảnh báo về: (1) Giảm tế bào máu có thể nặng, (2) QT kéo dài có thể xảy ra, (3) Tăng men gan phổ biến.",
        "drug_interactions": {
            "major": [
                {
                    "drug": "CYP3A4 Inhibitors mạnh (Ketoconazole, Itraconazole, Ritonavir)",
                    "mechanism": "Ức chế CYP3A4, tăng nồng độ asciminib",
                    "effect": "Tăng nồng độ asciminib, tăng nguy cơ tác dụng phụ",
                    "management": "Thận trọng. Có thể cần giảm liều asciminib 50%. Theo dõi tác dụng phụ."
                },
                {
                    "drug": "CYP3A4 Inducers mạnh (Rifampin, Carbamazepine, Phenytoin)",
                    "mechanism": "Cảm ứng CYP3A4, giảm nồng độ asciminib",
                    "effect": "Giảm nồng độ asciminib, giảm hiệu quả điều trị",
                    "management": "Thận trọng. Có thể cần tăng liều asciminib. Theo dõi đáp ứng điều trị."
                }
            ],
            "moderate": [
                {
                    "drug": "Thuốc kéo dài QT (quinidine, procainamide, sotalol)",
                    "mechanism": "Tác dụng cộng dồn",
                    "effect": "Tăng nguy cơ QT kéo dài, rối loạn nhịp tim",
                    "management": "Thận trọng. Theo dõi ECG chặt chẽ. Tránh dùng cùng nếu có thể."
                }
            ],
            "minor": []
        },
        "contraindications_detail": {
            "tuyệt_đối": [
                "Dị ứng asciminib hoặc bất kỳ thành phần nào"
            ],
            "tương_đối": [
                "Suy gan nặng - thận trọng, có thể tăng nồng độ",
                "Suy thận nặng - thận trọng, dữ liệu hạn chế",
                "QT kéo dài - thận trọng, tăng nguy cơ",
                "Giảm tế bào máu nặng - có thể cần trì hoãn điều trị"
            ]
        },
        "pregnancy_lactation": {
            "fda_category": "D",
            "pregnancy_details": "Category D - có bằng chứng về nguy cơ cho thai nhi. Asciminib có thể gây hại cho thai nhi. Không dùng trong thai kỳ trừ khi lợi ích vượt trội nguy cơ. Tránh thai hiệu quả trong và sau điều trị.",
            "lactation": {
                "safety": "Incompatible",
                "details": "Asciminib có thể bài tiết vào sữa mẹ. Không dùng khi cho con bú.",
                "recommendation": "Không dùng khi cho con bú. Ngừng cho con bú hoặc ngừng thuốc."
            }
        },
        "hepatic_adjustment": {
            "mild": "Không đổi",
            "moderate": "Thận trọng, không cần chỉnh liều",
            "severe": "Thận trọng, có thể cần giảm liều",
            "notes": "Asciminib chuyển hóa qua gan (CYP3A4). Suy gan có thể làm giảm chuyển hóa, tăng nồng độ và độc tính. Theo dõi chức năng gan và độc tính chặt chẽ."
        },
        "overdose_management": {
            "symptoms": [
                "Giảm tế bào máu nặng (neutropenia, thrombocytopenia, anemia)",
                "Tăng men gan nặng",
                "QT kéo dài nặng",
                "Viêm tụy",
                "Buồn nôn, nôn nặng"
            ],
            "antidote": "Không có antidote đặc hiệu",
            "treatment": [
                "Ngừng ngay asciminib",
                "Điều trị hỗ trợ: truyền máu, G-CSF nếu giảm bạch cầu nặng",
                "Theo dõi CBC thường xuyên",
                "Theo dõi ECG (QT interval)",
                "Theo dõi chức năng gan",
                "Điều trị viêm tụy nếu có",
                "Hỗ trợ và điều trị triệu chứng"
            ],
            "monitoring": "Theo dõi CBC, ECG (QT interval), chức năng gan, lipase/amylase, dấu hiệu sinh tồn cho đến khi hồi phục."
        },
        "reversal_agents": {
            "available": False,
            "agents": []
        },
        "administration_instructions": {
            "oral": {
                "with_food": "Có thể uống với hoặc không có thức ăn",
                "timing": "80mg x 1 lần/ngày hoặc 40mg x 2 lần/ngày. Uống đều đặn hàng ngày.",
                "notes": "QUAN TRỌNG: (1) Uống đều đặn hàng ngày, (2) Theo dõi CBC thường xuyên, (3) Theo dõi ECG trước và trong điều trị, (4) Theo dõi chức năng gan định kỳ, (5) Tương tác với CYP3A4 inhibitors/inducers."
            }
        },
        "references": {
            "primary_sources": [
                "FDA Drug Label - Asciminib (Scemblix)",
                "FDA Approval Date: 10/29/2021",
                "FDA-approved use: To treat Philadelphia chromosome-positive chronic myeloid leukemia with disease that meets certain criteria",
                "UpToDate - Asciminib: Drug information",
                "Lexicomp - Asciminib monograph"
            ],
            "last_updated": "2025-02-18",
            "evidence_level": "A - FDA-approved 10/29/2021, dựa trên dữ liệu lâm sàng từ các thử nghiệm lâm sàng"
        },
        "risk_flags": {
            "high_alert": True,
            "narrow_therapeutic_index": False,
            "bleeding_risk": False,
            "organ_toxicity": ["Hepatotoxicity (elevated liver enzymes) - common", "Pancreatitis - uncommon"],
            "qt_prolongation": True,
            "hepatotoxicity": True,
            "nephrotoxicity": False,
            "requires_monitoring": ["CBC with differential - CRITICAL", "Liver function (ALT, AST, bilirubin)", "Lipase, amylase", "ECG (QT interval) - CRITICAL", "Clinical response (BCR-ABL levels)", "Signs of pancreatitis"]
        },
        "guideline_tags": [
            "FDA Drug Information - Asciminib (Scemblix)",
            "NCCN Guidelines - CML Treatment",
            "UpToDate - CML Treatment"
        ],
        "last_updated": "2025-02-18"
    },

    "Exkivity": {
        "group": "FDA Approved 9/15/2021",
        "vietnamese_name": "Mobocertinib, Exkivity",
        "administration": ["PO"],
        "indications": [
            "Ung thư phổi không tế bào nhỏ (NSCLC) tiến triển tại chỗ hoặc di căn có đột biến EGFR exon 20 insertion",
            "NSCLC với EGFR exon 20 insertion mutations đã điều trị trước đó"
        ],
        "contraindications": {
            "tuyệt_đối": [
                "Dị ứng mobocertinib hoặc bất kỳ thành phần nào"
            ],
            "tương_đối": [
                "Bệnh phổi mô kẽ (ILD) - thận trọng",
                "Suy gan nặng - thận trọng",
                "Suy thận nặng - thận trọng",
                "QT kéo dài - thận trọng"
            ]
        },
        "dosage": {
            "adult_standard": "160mg PO x 1 lần/ngày",
            "notes": "Uống với thức ăn. Mobocertinib là EGFR TKI cho NSCLC với EGFR exon 20 insertion mutations. FDA phê duyệt 9/15/2021."
        },
        "renal_adjustment": {
            "normal": "Không cần chỉnh liều",
            "30_60": "Thận trọng, không cần chỉnh liều",
            "under_30": "Thận trọng, dữ liệu hạn chế"
        },
        "side_effects": [
            "Tiêu chảy - rất phổ biến",
            "Phát ban (rash) - phổ biến",
            "Buồn nôn - phổ biến",
            "Nôn - phổ biến",
            "Mệt mỏi - phổ biến",
            "Đau đầu - phổ biến",
            "Giảm cảm giác thèm ăn - phổ biến",
            "Tăng men gan (ALT, AST) - phổ biến",
            "Bệnh phổi mô kẽ (ILD) - hiếm nhưng NGUY HIỂM, có thể tử vong",
            "QT kéo dài - không phổ biến",
            "Viêm móng (paronychia) - phổ biến",
            "Khô da - phổ biến"
        ],
        "interactions": [
            "CYP3A4 inhibitors (ketoconazole, itraconazole, ritonavir): tăng nồng độ mobocertinib",
            "CYP3A4 inducers (rifampin, carbamazepine): giảm nồng độ mobocertinib",
            "Thuốc kéo dài QT: tăng nguy cơ QT kéo dài",
            "PPI/H2 blockers: có thể giảm hấp thu"
        ],
        "pregnancy": "D",
        "mechanism_of_action": "Mobocertinib là tyrosine kinase inhibitor (TKI), ức chế đặc hiệu EGFR (Epidermal Growth Factor Receptor) tyrosine kinase, đặc biệt hiệu quả với EGFR exon 20 insertion mutations. EGFR exon 20 insertion mutations là một loại đột biến EGFR khác với các đột biến thường gặp (exon 19 deletion, L858R), và thường kháng với các EGFR TKI thế hệ 1-2. Mobocertinib gắn với vị trí ATP-binding của EGFR, ức chế hoạt tính kinase, ngăn chặn tín hiệu tăng sinh và gây chết tế bào ung thư. ĐẶC ĐIỂM: (1) EGFR TKI cho NSCLC với EGFR exon 20 insertion mutations, (2) Phát ban (rash) - phổ biến, có thể là dấu hiệu đáp ứng điều trị, (3) Bệnh phổi mô kẽ (ILD) - hiếm nhưng NGUY HIỂM, có thể tử vong, (4) Uống với thức ăn, (5) Tương tác với CYP3A4, (6) FDA phê duyệt 9/15/2021.",
        "monitoring": [
            "Phát ban (rash) - phổ biến, có thể là dấu hiệu đáp ứng điều trị",
            "Bệnh phổi mô kẽ (ILD) - hiếm nhưng NGUY HIỂM, có thể tử vong - theo dõi khó thở, ho, sốt - QUAN TRỌNG",
            "Chức năng gan (ALT, AST, bilirubin) trước và trong điều trị",
            "ECG: QT interval (QT kéo dài không phổ biến)",
            "Dấu hiệu tiêu chảy - rất phổ biến",
            "Đáp ứng điều trị: CT scan mỗi 2-3 tháng"
        ],
        "precautions": [
            "BỆNH PHỔI MÔ KẼ (ILD) - hiếm nhưng NGUY HIỂM, có thể tử vong - NGỪNG NGAY nếu có khó thở, ho, sốt, chụp X-quang ngực",
            "PHÁT BAN (RASH) - phổ biến, có thể là dấu hiệu đáp ứng điều trị, điều trị với corticosteroid tại chỗ hoặc kháng sinh nếu nhiễm trùng",
            "TIÊU CHẢY - rất phổ biến. Điều trị với loperamide nếu cần.",
            "Uống với thức ăn",
            "Tương tác với CYP3A4 inhibitors/inducers - điều chỉnh liều nếu cần",
            "Thận trọng với thuốc kéo dài QT (tăng nguy cơ QT kéo dài)",
            "Theo dõi chức năng gan chặt chẽ (tăng men gan phổ biến)"
        ],
        "pharmacokinetics": {
            "half_life": "Khoảng 15-20 giờ",
            "onset": "Vài tuần (tác dụng lâm sàng)",
            "duration": "Dài (dùng hàng ngày)",
            "protein_binding": ">90%",
            "metabolism": "Gan (CYP3A4 chủ yếu)",
            "clearance": "Gan (chủ yếu), thận (một phần)"
        },
        "storage": "Bảo quản ở nhiệt độ phòng (20-25°C), tránh ẩm. Bảo quản trong hộp kín gốc. Để xa tầm tay trẻ em.",
        "black_box_warnings": "BỆNH PHỔI MÔ KẼ (Interstitial Lung Disease - ILD) - hiếm nhưng NGUY HIỂM, có thể tử vong. Ngừng ngay mobocertinib nếu có khó thở, ho, sốt. Chụp X-quang ngực ngay.",
        "drug_interactions": {
            "major": [
                {
                    "drug": "CYP3A4 Inhibitors mạnh (Ketoconazole, Itraconazole, Ritonavir)",
                    "mechanism": "Ức chế CYP3A4, tăng nồng độ mobocertinib",
                    "effect": "Tăng nồng độ mobocertinib, tăng nguy cơ tác dụng phụ",
                    "management": "Thận trọng. Có thể cần giảm liều mobocertinib 50%. Theo dõi tác dụng phụ."
                },
                {
                    "drug": "CYP3A4 Inducers mạnh (Rifampin, Carbamazepine, Phenytoin)",
                    "mechanism": "Cảm ứng CYP3A4, giảm nồng độ mobocertinib",
                    "effect": "Giảm nồng độ mobocertinib, giảm hiệu quả điều trị",
                    "management": "Thận trọng. Có thể cần tăng liều mobocertinib. Theo dõi đáp ứng điều trị."
                }
            ],
            "moderate": [
                {
                    "drug": "Thuốc kéo dài QT (quinidine, procainamide, sotalol)",
                    "mechanism": "Tác dụng cộng dồn",
                    "effect": "Tăng nguy cơ QT kéo dài, rối loạn nhịp tim",
                    "management": "Thận trọng. Theo dõi ECG chặt chẽ. Tránh dùng cùng nếu có thể."
                }
            ],
            "minor": []
        },
        "contraindications_detail": {
            "tuyệt_đối": [
                "Dị ứng mobocertinib hoặc bất kỳ thành phần nào"
            ],
            "tương_đối": [
                "Bệnh phổi mô kẽ đang hoạt động - tăng nguy cơ ILD",
                "Suy gan nặng - thận trọng, có thể cần giảm liều",
                "Suy thận nặng - thận trọng",
                "QT kéo dài - thận trọng, tăng nguy cơ"
            ]
        },
        "pregnancy_lactation": {
            "fda_category": "D",
            "pregnancy_details": "Category D - có bằng chứng về nguy cơ cho thai nhi. Mobocertinib có thể gây hại cho thai nhi. Không dùng trong thai kỳ trừ khi lợi ích vượt trội nguy cơ. Tránh thai hiệu quả trong và sau điều trị.",
            "lactation": {
                "safety": "Incompatible",
                "details": "Mobocertinib có thể bài tiết vào sữa mẹ. Không dùng khi cho con bú.",
                "recommendation": "Không dùng khi cho con bú. Ngừng cho con bú hoặc ngừng thuốc."
            }
        },
        "hepatic_adjustment": {
            "mild": "Không đổi",
            "moderate": "Thận trọng, có thể cần giảm liều",
            "severe": "Thận trọng, giảm liều 25-50%",
            "notes": "Mobocertinib chuyển hóa qua gan (CYP3A4). Suy gan có thể làm giảm chuyển hóa, tăng nồng độ và độc tính. Theo dõi chức năng gan và độc tính chặt chẽ."
        },
        "overdose_management": {
            "symptoms": [
                "Phát ban nặng",
                "Tiêu chảy nặng",
                "Bệnh phổi mô kẽ nặng (khó thở, ho, sốt)",
                "Tăng men gan nặng",
                "QT kéo dài nặng"
            ],
            "antidote": "Không có antidote đặc hiệu",
            "treatment": [
                "Ngừng ngay mobocertinib",
                "Nếu ILD: ngừng ngay, chụp X-quang ngực, điều trị hỗ trợ hô hấp, corticosteroid nếu cần",
                "Điều trị tiêu chảy: loperamide, bù nước và điện giải",
                "Theo dõi ECG (QT interval)",
                "Theo dõi chức năng gan",
                "Hỗ trợ và điều trị triệu chứng"
            ],
            "monitoring": "Theo dõi dấu hiệu sinh tồn, hô hấp (ILD), ECG (QT interval), chức năng gan cho đến khi hồi phục."
        },
        "reversal_agents": {
            "available": False,
            "agents": []
        },
        "administration_instructions": {
            "oral": {
                "with_food": "Uống với thức ăn để tăng hấp thu và giảm tác dụng phụ",
                "timing": "160mg x 1 lần/ngày với bữa ăn. Uống đều đặn hàng ngày.",
                "notes": "QUAN TRỌNG: (1) Uống với thức ăn, (2) Uống đều đặn hàng ngày, (3) NGỪNG NGAY nếu có dấu hiệu ILD (khó thở, ho, sốt), (4) Theo dõi phát ban và điều trị nếu cần, (5) Tương tác với CYP3A4 inhibitors/inducers."
            }
        },
        "references": {
            "primary_sources": [
                "FDA Drug Label - Mobocertinib (Exkivity)",
                "FDA Approval Date: 9/15/2021",
                "FDA-approved use: To treat locally advanced or metastatic non-small cell lung cancer with epidermal growth factor receptor exon 20 insertion mutations",
                "UpToDate - Mobocertinib: Drug information",
                "Lexicomp - Mobocertinib monograph"
            ],
            "last_updated": "2025-02-18",
            "evidence_level": "A - FDA-approved 9/15/2021, dựa trên dữ liệu lâm sàng từ các thử nghiệm lâm sàng"
        },
        "risk_flags": {
            "high_alert": True,
            "narrow_therapeutic_index": False,
            "bleeding_risk": False,
            "organ_toxicity": ["Interstitial lung disease (ILD) - rare but FATAL - CRITICAL", "Hepatotoxicity (elevated liver enzymes) - common"],
            "qt_prolongation": True,
            "hepatotoxicity": True,
            "nephrotoxicity": False,
            "requires_monitoring": ["Rash (may indicate treatment response)", "Interstitial lung disease (ILD) - signs: dyspnea, cough, fever - CRITICAL", "Liver function (ALT, AST, bilirubin)", "ECG (QT interval)", "Diarrhea - very common", "Clinical response (CT scan every 2-3 months)"]
        },
        "guideline_tags": [
            "FDA Drug Information - Mobocertinib (Exkivity)",
            "NCCN Guidelines - NSCLC Treatment",
            "UpToDate - NSCLC Treatment"
        ],
        "last_updated": "2025-02-18"
    },

    "Truseltiq": {
        "group": "FDA Approved 5/28/2021",
        "vietnamese_name": "Infigratinib, Truseltiq",
        "administration": ["PO"],
        "indications": [
            "Ung thư đường mật (cholangiocarcinoma) tiến triển hoặc di căn có đột biến FGFR2 fusion hoặc rearrangement",
            "Cholangiocarcinoma với FGFR2 alterations đã điều trị trước đó"
        ],
        "contraindications": {
            "tuyệt_đối": [
                "Dị ứng infigratinib hoặc bất kỳ thành phần nào"
            ],
            "tương_đối": [
                "Bệnh võng mạc - thận trọng (có thể gây rối loạn võng mạc)",
                "Suy gan nặng - thận trọng",
                "Suy thận nặng - thận trọng",
                "Tăng phosphate máu - thận trọng"
            ]
        },
        "dosage": {
            "adult_standard": "125mg PO x 1 lần/ngày trong 21 ngày, sau đó nghỉ 7 ngày (chu kỳ 28 ngày)",
            "notes": "Uống với hoặc không có thức ăn. Infigratinib là FGFR inhibitor cho cholangiocarcinoma với FGFR2 alterations. FDA phê duyệt 5/28/2021."
        },
        "renal_adjustment": {
            "normal": "Không cần chỉnh liều",
            "30_60": "Thận trọng, không cần chỉnh liều",
            "under_30": "Thận trọng, dữ liệu hạn chế"
        },
        "side_effects": [
            "Tăng phosphate máu - rất phổ biến (do ức chế FGFR)",
            "Rối loạn võng mạc - phổ biến (retinal pigment epithelial detachment - RPED)",
            "Tăng men gan (ALT, AST) - phổ biến",
            "Mệt mỏi - phổ biến",
            "Buồn nôn - phổ biến",
            "Tiêu chảy - phổ biến",
            "Đau bụng - phổ biến",
            "Giảm cảm giác thèm ăn - phổ biến",
            "Khô miệng - phổ biến",
            "Đau cơ (myalgia) - phổ biến",
            "Đau khớp (arthralgia) - phổ biến",
            "Rụng tóc - phổ biến",
            "Tăng creatinine - phổ biến",
            "Giảm bạch cầu (neutropenia) - không phổ biến",
            "Giảm tiểu cầu (thrombocytopenia) - không phổ biến"
        ],
        "interactions": [
            "CYP3A4 inhibitors (ketoconazole, itraconazole, ritonavir): tăng nồng độ infigratinib",
            "CYP3A4 inducers (rifampin, carbamazepine): giảm nồng độ infigratinib",
            "Thuốc ức chế phosphate: có thể tương tác với tăng phosphate máu"
        ],
        "pregnancy": "D",
        "mechanism_of_action": "Infigratinib là tyrosine kinase inhibitor (TKI), ức chế đặc hiệu FGFR (Fibroblast Growth Factor Receptor) 1, 2, và 3. FGFR là thụ thể tyrosine kinase quan trọng trong tăng sinh tế bào, biệt hóa, và hình thành mạch máu. Trong cholangiocarcinoma, một số bệnh nhân có FGFR2 fusions hoặc rearrangements làm cho FGFR hoạt động liên tục, dẫn đến tăng sinh tế bào ung thư. Infigratinib gắn với vị trí ATP-binding của FGFR, ức chế hoạt tính kinase, ngăn chặn tín hiệu tăng sinh và gây chết tế bào ung thư. ĐẶC ĐIỂM: (1) FGFR inhibitor, hiệu quả với cholangiocarcinoma có FGFR2 alterations, (2) Tăng phosphate máu - rất phổ biến (do ức chế FGFR), (3) Rối loạn võng mạc (RPED) - phổ biến, cần khám mắt định kỳ, (4) Uống với hoặc không có thức ăn, (5) Tương tác với CYP3A4, (6) FDA phê duyệt 5/28/2021.",
        "monitoring": [
            "Phosphate máu - rất phổ biến, theo dõi định kỳ - QUAN TRỌNG",
            "Khám mắt: thị lực, khám đáy mắt (rối loạn võng mạc - RPED) - QUAN TRỌNG",
            "Chức năng gan: ALT, AST, bilirubin (tăng men gan phổ biến)",
            "Creatinine (tăng creatinine phổ biến)",
            "CBC: giảm bạch cầu, giảm tiểu cầu (không phổ biến)",
            "Đáp ứng điều trị: CT scan mỗi 2-3 tháng"
        ],
        "precautions": [
            "TĂNG PHOSPHATE MÁU - rất phổ biến (do ức chế FGFR). Theo dõi phosphate máu định kỳ. Có thể cần điều trị với phosphate binders nếu tăng nặng.",
            "RỐI LOẠN VÕNG MẠC (RPED) - phổ biến. Khám mắt trước và trong điều trị định kỳ. Ngừng tạm thời nếu có rối loạn võng mạc nặng.",
            "Tăng men gan - phổ biến. Theo dõi chức năng gan định kỳ.",
            "Tăng creatinine - phổ biến. Theo dõi chức năng thận.",
            "Uống với hoặc không có thức ăn",
            "Tương tác với CYP3A4 inhibitors/inducers - điều chỉnh liều nếu cần",
            "Chu kỳ 28 ngày: dùng 21 ngày, nghỉ 7 ngày"
        ],
        "pharmacokinetics": {
            "half_life": "Khoảng 33-38 giờ",
            "onset": "Vài tuần đến vài tháng (tác dụng lâm sàng)",
            "duration": "Dài (dùng 21 ngày trong chu kỳ 28 ngày)",
            "protein_binding": ">99%",
            "metabolism": "Gan (CYP3A4 chủ yếu)",
            "clearance": "Gan (chủ yếu), thận (một phần)"
        },
        "storage": "Bảo quản ở nhiệt độ phòng (20-25°C), tránh ẩm. Bảo quản trong hộp kín gốc. Để xa tầm tay trẻ em.",
        "black_box_warnings": "Không có black box warning. Tuy nhiên, cần cảnh báo về: (1) Tăng phosphate máu rất phổ biến, (2) Rối loạn võng mạc (RPED) phổ biến, cần khám mắt định kỳ.",
        "drug_interactions": {
            "major": [
                {
                    "drug": "CYP3A4 Inhibitors mạnh (Ketoconazole, Itraconazole, Ritonavir)",
                    "mechanism": "Ức chế CYP3A4, tăng nồng độ infigratinib",
                    "effect": "Tăng nồng độ infigratinib, tăng nguy cơ tác dụng phụ",
                    "management": "Thận trọng. Có thể cần giảm liều infigratinib 50%. Theo dõi tác dụng phụ."
                },
                {
                    "drug": "CYP3A4 Inducers mạnh (Rifampin, Carbamazepine, Phenytoin)",
                    "mechanism": "Cảm ứng CYP3A4, giảm nồng độ infigratinib",
                    "effect": "Giảm nồng độ infigratinib, giảm hiệu quả điều trị",
                    "management": "Thận trọng. Có thể cần tăng liều infigratinib. Theo dõi đáp ứng điều trị."
                }
            ],
            "moderate": [
                {
                    "drug": "Phosphate binders (sevelamer, lanthanum)",
                    "mechanism": "Cả hai đều ảnh hưởng đến phosphate",
                    "effect": "Có thể tương tác với tăng phosphate máu do infigratinib",
                    "management": "Thận trọng. Theo dõi phosphate máu chặt chẽ."
                }
            ],
            "minor": []
        },
        "contraindications_detail": {
            "tuyệt_đối": [
                "Dị ứng infigratinib hoặc bất kỳ thành phần nào"
            ],
            "tương_đối": [
                "Bệnh võng mạc đang hoạt động - thận trọng, tăng nguy cơ rối loạn võng mạc",
                "Suy gan nặng - thận trọng, có thể tăng nồng độ",
                "Suy thận nặng - thận trọng, dữ liệu hạn chế",
                "Tăng phosphate máu nặng - có thể cần điều trị trước"
            ]
        },
        "pregnancy_lactation": {
            "fda_category": "D",
            "pregnancy_details": "Category D - có bằng chứng về nguy cơ cho thai nhi. Infigratinib có thể gây hại cho thai nhi. Không dùng trong thai kỳ trừ khi lợi ích vượt trội nguy cơ. Tránh thai hiệu quả trong và sau điều trị.",
            "lactation": {
                "safety": "Incompatible",
                "details": "Infigratinib có thể bài tiết vào sữa mẹ. Không dùng khi cho con bú.",
                "recommendation": "Không dùng khi cho con bú. Ngừng cho con bú hoặc ngừng thuốc."
            }
        },
        "hepatic_adjustment": {
            "mild": "Không đổi",
            "moderate": "Thận trọng, không cần chỉnh liều",
            "severe": "Thận trọng, có thể cần giảm liều",
            "notes": "Infigratinib chuyển hóa qua gan (CYP3A4). Suy gan có thể làm giảm chuyển hóa, tăng nồng độ và độc tính. Theo dõi chức năng gan và độc tính chặt chẽ."
        },
        "overdose_management": {
            "symptoms": [
                "Tăng phosphate máu nặng",
                "Rối loạn võng mạc nặng",
                "Tăng men gan nặng",
                "Tăng creatinine nặng",
                "Giảm tế bào máu nặng"
            ],
            "antidote": "Không có antidote đặc hiệu",
            "treatment": [
                "Ngừng ngay infigratinib",
                "Nếu tăng phosphate máu nặng: điều trị với phosphate binders, hạn chế phosphate trong chế độ ăn",
                "Nếu rối loạn võng mạc: khám mắt ngay, ngừng tạm thời",
                "Theo dõi chức năng gan, thận",
                "Hỗ trợ và điều trị triệu chứng"
            ],
            "monitoring": "Theo dõi phosphate máu, khám mắt, chức năng gan/thận, CBC, dấu hiệu sinh tồn cho đến khi hồi phục."
        },
        "reversal_agents": {
            "available": False,
            "agents": []
        },
        "administration_instructions": {
            "oral": {
                "with_food": "Có thể uống với hoặc không có thức ăn",
                "timing": "125mg x 1 lần/ngày trong 21 ngày, sau đó nghỉ 7 ngày (chu kỳ 28 ngày). Uống đều đặn.",
                "notes": "QUAN TRỌNG: (1) Chu kỳ 28 ngày: dùng 21 ngày, nghỉ 7 ngày, (2) Theo dõi phosphate máu định kỳ, (3) Khám mắt trước và trong điều trị định kỳ, (4) Tương tác với CYP3A4 inhibitors/inducers."
            }
        },
        "references": {
            "primary_sources": [
                "FDA Drug Label - Infigratinib (Truseltiq)",
                "FDA Approval Date: 5/28/2021",
                "FDA-approved use: To treat cholangiocarcinoma whose disease meets certain criteria",
                "UpToDate - Infigratinib: Drug information",
                "Lexicomp - Infigratinib monograph"
            ],
            "last_updated": "2025-02-18",
            "evidence_level": "A - FDA-approved 5/28/2021, dựa trên dữ liệu lâm sàng từ các thử nghiệm lâm sàng"
        },
        "risk_flags": {
            "high_alert": True,
            "narrow_therapeutic_index": False,
            "bleeding_risk": False,
            "organ_toxicity": ["Retinal disorders (RPED) - common - CRITICAL", "Hepatotoxicity (elevated liver enzymes) - common", "Hyperphosphatemia - very common"],
            "qt_prolongation": False,
            "hepatotoxicity": True,
            "nephrotoxicity": False,
            "requires_monitoring": ["Serum phosphate - CRITICAL", "Eye examination (vision, fundoscopy) - CRITICAL", "Liver function (ALT, AST, bilirubin)", "Creatinine", "CBC (neutropenia, thrombocytopenia)", "Clinical response (CT scan every 2-3 months)"]
        },
        "guideline_tags": [
            "FDA Drug Information - Infigratinib (Truseltiq)",
            "NCCN Guidelines - Cholangiocarcinoma Treatment",
            "UpToDate - Cholangiocarcinoma Treatment"
        ],
        "last_updated": "2025-02-18"
    },

    "Tepmetko": {
        "group": "FDA Approved 2/3/2021",
        "vietnamese_name": "Tepotinib, Tepmetko",
        "administration": ["PO"],
        "indications": [
            "Ung thư phổi không tế bào nhỏ (NSCLC) tiến triển hoặc di căn có đột biến MET exon 14 skipping",
            "NSCLC với MET exon 14 skipping mutations đã điều trị trước đó"
        ],
        "contraindications": {
            "tuyệt_đối": [
                "Dị ứng tepotinib hoặc bất kỳ thành phần nào"
            ],
            "tương_đối": [
                "Bệnh phổi mô kẽ (ILD) - thận trọng",
                "Suy gan nặng - thận trọng",
                "Suy thận nặng - thận trọng"
            ]
        },
        "dosage": {
            "adult_standard": "450mg PO x 1 lần/ngày",
            "notes": "Uống với thức ăn. Tepotinib là MET inhibitor cho NSCLC với MET exon 14 skipping mutations. FDA phê duyệt 2/3/2021."
        },
        "renal_adjustment": {
            "normal": "Không cần chỉnh liều",
            "30_60": "Thận trọng, không cần chỉnh liều",
            "under_30": "Thận trọng, dữ liệu hạn chế"
        },
        "side_effects": [
            "Phù (edema) - phổ biến (phù ngoại biên, phù mặt)",
            "Mệt mỏi - phổ biến",
            "Buồn nôn - phổ biến",
            "Tiêu chảy - phổ biến",
            "Tăng men gan (ALT, AST) - phổ biến",
            "Đau cơ (myalgia) - phổ biến",
            "Đau khớp (arthralgia) - phổ biến",
            "Bệnh phổi mô kẽ (ILD) - hiếm nhưng NGUY HIỂM, có thể tử vong",
            "Giảm bạch cầu (neutropenia) - không phổ biến",
            "Giảm tiểu cầu (thrombocytopenia) - không phổ biến"
        ],
        "interactions": [
            "CYP3A4 inhibitors (ketoconazole, itraconazole, ritonavir): tăng nồng độ tepotinib",
            "CYP3A4 inducers (rifampin, carbamazepine): giảm nồng độ tepotinib",
            "P-gp inhibitors: có thể tăng nồng độ tepotinib"
        ],
        "pregnancy": "D",
        "mechanism_of_action": "Tepotinib là tyrosine kinase inhibitor (TKI), ức chế đặc hiệu MET (Mesenchymal-Epithelial Transition factor) tyrosine kinase. MET là thụ thể tyrosine kinase quan trọng trong tăng sinh tế bào, di chuyển tế bào, và hình thành mạch máu. Trong NSCLC, một số bệnh nhân có MET exon 14 skipping mutations làm cho MET hoạt động liên tục, dẫn đến tăng sinh tế bào ung thư. Tepotinib gắn với vị trí ATP-binding của MET, ức chế hoạt tính kinase, ngăn chặn tín hiệu tăng sinh và gây chết tế bào ung thư. ĐẶC ĐIỂM: (1) MET inhibitor, hiệu quả với NSCLC có MET exon 14 skipping mutations, (2) Phù (edema) - phổ biến, đặc trưng, (3) Bệnh phổi mô kẽ (ILD) - hiếm nhưng NGUY HIỂM, có thể tử vong, (4) Uống với thức ăn, (5) Tương tác với CYP3A4 và P-gp, (6) FDA phê duyệt 2/3/2021.",
        "monitoring": [
            "Phù (edema) - phổ biến, đặc trưng - theo dõi phù ngoại biên, phù mặt",
            "Bệnh phổi mô kẽ (ILD) - hiếm nhưng NGUY HIỂM, có thể tử vong - theo dõi khó thở, ho, sốt - QUAN TRỌNG",
            "Chức năng gan: ALT, AST, bilirubin (tăng men gan phổ biến)",
            "CBC: giảm bạch cầu, giảm tiểu cầu (không phổ biến)",
            "Đáp ứng điều trị: CT scan mỗi 2-3 tháng"
        ],
        "precautions": [
            "BỆNH PHỔI MÔ KẼ (ILD) - hiếm nhưng NGUY HIỂM, có thể tử vong - NGỪNG NGAY nếu có khó thở, ho, sốt, chụp X-quang ngực",
            "PHÙ (EDEMA) - phổ biến, đặc trưng. Có thể cần điều trị với furosemide nếu phù nặng.",
            "Tăng men gan - phổ biến. Theo dõi chức năng gan định kỳ.",
            "Uống với thức ăn",
            "Tương tác với CYP3A4 inhibitors/inducers - điều chỉnh liều nếu cần",
            "Tương tác với P-gp inhibitors - thận trọng",
            "Theo dõi CBC định kỳ"
        ],
        "pharmacokinetics": {
            "half_life": "Khoảng 32-35 giờ",
            "onset": "Vài tuần đến vài tháng (tác dụng lâm sàng)",
            "duration": "Dài (dùng hàng ngày)",
            "protein_binding": ">99%",
            "metabolism": "Gan (CYP3A4 chủ yếu)",
            "clearance": "Gan (chủ yếu), thận (một phần), P-gp"
        },
        "storage": "Bảo quản ở nhiệt độ phòng (20-25°C), tránh ẩm. Bảo quản trong hộp kín gốc. Để xa tầm tay trẻ em.",
        "black_box_warnings": "BỆNH PHỔI MÔ KẼ (Interstitial Lung Disease - ILD) - hiếm nhưng NGUY HIỂM, có thể tử vong. Ngừng ngay tepotinib nếu có khó thở, ho, sốt. Chụp X-quang ngực ngay.",
        "drug_interactions": {
            "major": [
                {
                    "drug": "CYP3A4 Inhibitors mạnh (Ketoconazole, Itraconazole, Ritonavir)",
                    "mechanism": "Ức chế CYP3A4, tăng nồng độ tepotinib",
                    "effect": "Tăng nồng độ tepotinib, tăng nguy cơ tác dụng phụ",
                    "management": "Thận trọng. Có thể cần giảm liều tepotinib 50%. Theo dõi tác dụng phụ."
                },
                {
                    "drug": "CYP3A4 Inducers mạnh (Rifampin, Carbamazepine, Phenytoin)",
                    "mechanism": "Cảm ứng CYP3A4, giảm nồng độ tepotinib",
                    "effect": "Giảm nồng độ tepotinib, giảm hiệu quả điều trị",
                    "management": "Thận trọng. Có thể cần tăng liều tepotinib. Theo dõi đáp ứng điều trị."
                }
            ],
            "moderate": [
                {
                    "drug": "P-gp Inhibitors (Verapamil, Amiodarone, Quinidine)",
                    "mechanism": "Ức chế P-gp, tăng nồng độ tepotinib",
                    "effect": "Tăng nồng độ tepotinib, tăng nguy cơ tác dụng phụ",
                    "management": "Thận trọng. Có thể cần giảm liều tepotinib."
                }
            ],
            "minor": []
        },
        "contraindications_detail": {
            "tuyệt_đối": [
                "Dị ứng tepotinib hoặc bất kỳ thành phần nào"
            ],
            "tương_đối": [
                "Bệnh phổi mô kẽ đang hoạt động - tăng nguy cơ ILD",
                "Suy gan nặng - thận trọng, có thể cần giảm liều",
                "Suy thận nặng - thận trọng, dữ liệu hạn chế"
            ]
        },
        "pregnancy_lactation": {
            "fda_category": "D",
            "pregnancy_details": "Category D - có bằng chứng về nguy cơ cho thai nhi. Tepotinib có thể gây hại cho thai nhi. Không dùng trong thai kỳ trừ khi lợi ích vượt trội nguy cơ. Tránh thai hiệu quả trong và sau điều trị.",
            "lactation": {
                "safety": "Incompatible",
                "details": "Tepotinib có thể bài tiết vào sữa mẹ. Không dùng khi cho con bú.",
                "recommendation": "Không dùng khi cho con bú. Ngừng cho con bú hoặc ngừng thuốc."
            }
        },
        "hepatic_adjustment": {
            "mild": "Không đổi",
            "moderate": "Thận trọng, không cần chỉnh liều",
            "severe": "Thận trọng, có thể cần giảm liều",
            "notes": "Tepotinib chuyển hóa qua gan (CYP3A4). Suy gan có thể làm giảm chuyển hóa, tăng nồng độ và độc tính. Theo dõi chức năng gan và độc tính chặt chẽ."
        },
        "overdose_management": {
            "symptoms": [
                "Phù nặng",
                "Bệnh phổi mô kẽ nặng (khó thở, ho, sốt)",
                "Tăng men gan nặng",
                "Giảm tế bào máu nặng"
            ],
            "antidote": "Không có antidote đặc hiệu",
            "treatment": [
                "Ngừng ngay tepotinib",
                "Nếu ILD: ngừng ngay, chụp X-quang ngực, điều trị hỗ trợ hô hấp, corticosteroid nếu cần",
                "Nếu phù nặng: furosemide, hạn chế muối",
                "Theo dõi chức năng gan",
                "Theo dõi CBC",
                "Hỗ trợ và điều trị triệu chứng"
            ],
            "monitoring": "Theo dõi dấu hiệu sinh tồn, hô hấp (ILD), phù, chức năng gan, CBC cho đến khi hồi phục."
        },
        "reversal_agents": {
            "available": False,
            "agents": []
        },
        "administration_instructions": {
            "oral": {
                "with_food": "Uống với thức ăn để tăng hấp thu",
                "timing": "450mg x 1 lần/ngày với bữa ăn. Uống đều đặn hàng ngày.",
                "notes": "QUAN TRỌNG: (1) Uống với thức ăn, (2) Uống đều đặn hàng ngày, (3) NGỪNG NGAY nếu có dấu hiệu ILD (khó thở, ho, sốt), (4) Theo dõi phù và điều trị nếu cần, (5) Tương tác với CYP3A4 và P-gp inhibitors/inducers."
            }
        },
        "references": {
            "primary_sources": [
                "FDA Drug Label - Tepotinib (Tepmetko)",
                "FDA Approval Date: 2/3/2021",
                "FDA-approved use: To treat non-small cell lung cancer",
                "UpToDate - Tepotinib: Drug information",
                "Lexicomp - Tepotinib monograph"
            ],
            "last_updated": "2025-02-18",
            "evidence_level": "A - FDA-approved 2/3/2021, dựa trên dữ liệu lâm sàng từ các thử nghiệm lâm sàng"
        },
        "risk_flags": {
            "high_alert": True,
            "narrow_therapeutic_index": False,
            "bleeding_risk": False,
            "organ_toxicity": ["Interstitial lung disease (ILD) - rare but FATAL - CRITICAL", "Hepatotoxicity (elevated liver enzymes) - common"],
            "qt_prolongation": False,
            "hepatotoxicity": True,
            "nephrotoxicity": False,
            "requires_monitoring": ["Edema (peripheral, facial) - common", "Interstitial lung disease (ILD) - signs: dyspnea, cough, fever - CRITICAL", "Liver function (ALT, AST, bilirubin)", "CBC (neutropenia, thrombocytopenia)", "Clinical response (CT scan every 2-3 months)"]
        },
        "guideline_tags": [
            "FDA Drug Information - Tepotinib (Tepmetko)",
            "NCCN Guidelines - NSCLC Treatment",
            "UpToDate - NSCLC Treatment"
        ],
        "last_updated": "2025-02-18"
    },

    "Lytgobi": {
                "group": "FDA Approved 2022",
                "vietnamese_name": "Futibatinib, Lytgobi",
                "administration": [
                        "PO",
                ],
                "indications": [
                        "To treat intrahepatic cholangiocarcinoma harboring fibroblast growth factor receptor 2 (FGFR2) gene fusions or other rearrangements",
                ],
                "contraindications": [
                        "Dị ứng futibatinib hoặc bất kỳ thành phần nào",
                ],
                "dosage": {
                        "adult_standard": "Theo chỉ định của bác sĩ",
                        "notes": "FDA phê duyệt 2022. To treat intrahepatic cholangiocarcinoma harboring fibroblast growth factor receptor 2 (FGFR2) gene fusions or other rearrangements",
                },
                "renal_adjustment": {
                        "normal": "Không cần chỉnh liều",
                        "30_60": "Thận trọng",
                        "under_30": "Thận trọng, dữ liệu hạn chế",
                },
                "side_effects": [
                        "Cần bổ sung thông tin từ tài liệu FDA",
                ],
                "interactions": [
                        "Cần bổ sung thông tin từ tài liệu FDA",
                ],
                "pregnancy": "C",
                "mechanism_of_action": "Futibatinib được FDA phê duyệt 2022 để to treat intrahepatic cholangiocarcinoma harboring fibroblast growth factor receptor 2 (fgfr2) gene fusions or other rearrangements. Cần bổ sung thông tin chi tiết về cơ chế tác dụng.",
                "monitoring": [
                        "Theo dõi đáp ứng điều trị",
                        "Theo dõi tác dụng phụ",
                ],
                "precautions": [
                        "Dị ứng futibatinib",
                        "Cần bổ sung thông tin từ tài liệu FDA",
                ],
                "pharmacokinetics": {
                        "half_life": "Cần bổ sung",
                        "onset": "Cần bổ sung",
                        "duration": "Cần bổ sung",
                        "protein_binding": "Cần bổ sung",
                        "metabolism": "Cần bổ sung",
                        "clearance": "Cần bổ sung",
                },
                "storage": "Bảo quản theo hướng dẫn của nhà sản xuất",
                "black_box_warnings": "Cần kiểm tra tài liệu FDA",
                "drug_interactions": {
                        "major": [],
                        "moderate": [],
                        "minor": [],
                },
                "contraindications_detail": {
                        "tuyệt_đối": [
                                "Dị ứng futibatinib hoặc bất kỳ thành phần nào",
                        ],
                        "tương_đối": [],
                },
                "pregnancy_lactation": {
                        "fda_category": "C",
                        "pregnancy_details": "Cần bổ sung thông tin từ tài liệu FDA",
                        "lactation": {
                                "safety": "Unknown",
                                "details": "Chưa biết có bài tiết vào sữa mẹ hay không",
                                "recommendation": "Thận trọng khi cho con bú",
                        },
                },
                "hepatic_adjustment": {
                        "mild": "Không đổi",
                        "moderate": "Thận trọng",
                        "severe": "Thận trọng, dữ liệu hạn chế",
                        "notes": "Cần bổ sung thông tin từ tài liệu FDA",
                },
                "overdose_management": {
                        "symptoms": [
                                "Cần bổ sung",
                        ],
                        "antidote": "Không có antidote đặc hiệu",
                        "treatment": [
                                "Điều trị hỗ trợ",
                        ],
                        "monitoring": "Theo dõi dấu hiệu sinh tồn",
                },
                "reversal_agents": {
                        "available": False,
                        "agents": [],
                },
                "administration_instructions": {
                        "oral": {
                                "with_food": "Cần bổ sung",
                                "timing": "Cần bổ sung",
                        },
                },
                "references": {
                        "primary_sources": [
                                "FDA Drug Label - Futibatinib (Lytgobi)",
                                "FDA Approval Date: 2022",
                                "FDA-approved use: To treat intrahepatic cholangiocarcinoma harboring fibroblast growth factor receptor 2 (FGFR2) gene fusions or other rearrangements",
                        ],
                        "last_updated": "2026-01-15",
                        "evidence_level": "A - FDA-approved 2022",
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
                        "FDA Drug Information - Futibatinib (Lytgobi)",
                ],
                "last_updated": "2026-01-15",
        },
    "Augtyro": {
                "group": "FDA Approved 2023",
                "vietnamese_name": "Repotrectinib, Augtyro",
                "administration": [
                        "IV",
                        "SC",
                ],
                "indications": [
                        "To treat ROS1-positive non-small cell lung cancer",
                ],
                "contraindications": [
                        "Dị ứng repotrectinib hoặc bất kỳ thành phần nào",
                ],
                "dosage": {
                        "adult_standard": "Theo chỉ định của bác sĩ",
                        "notes": "FDA phê duyệt 2023. To treat ROS1-positive non-small cell lung cancer",
                },
                "renal_adjustment": {
                        "normal": "Không cần chỉnh liều",
                        "30_60": "Thận trọng",
                        "under_30": "Thận trọng, dữ liệu hạn chế",
                },
                "side_effects": [
                        "Cần bổ sung thông tin từ tài liệu FDA",
                ],
                "interactions": [
                        "Cần bổ sung thông tin từ tài liệu FDA",
                ],
                "pregnancy": "C",
                "mechanism_of_action": "Repotrectinib được FDA phê duyệt 2023 để to treat ros1-positive non-small cell lung cancer. Cần bổ sung thông tin chi tiết về cơ chế tác dụng.",
                "monitoring": [
                        "Theo dõi đáp ứng điều trị",
                        "Theo dõi tác dụng phụ",
                ],
                "precautions": [
                        "Dị ứng repotrectinib",
                        "Cần bổ sung thông tin từ tài liệu FDA",
                ],
                "pharmacokinetics": {
                        "half_life": "Cần bổ sung",
                        "onset": "Cần bổ sung",
                        "duration": "Cần bổ sung",
                        "protein_binding": "Cần bổ sung",
                        "metabolism": "Cần bổ sung",
                        "clearance": "Cần bổ sung",
                },
                "storage": "Bảo quản theo hướng dẫn của nhà sản xuất",
                "black_box_warnings": "Cần kiểm tra tài liệu FDA",
                "drug_interactions": {
                        "major": [],
                        "moderate": [],
                        "minor": [],
                },
                "contraindications_detail": {
                        "tuyệt_đối": [
                                "Dị ứng repotrectinib hoặc bất kỳ thành phần nào",
                        ],
                        "tương_đối": [],
                },
                "pregnancy_lactation": {
                        "fda_category": "C",
                        "pregnancy_details": "Cần bổ sung thông tin từ tài liệu FDA",
                        "lactation": {
                                "safety": "Unknown",
                                "details": "Chưa biết có bài tiết vào sữa mẹ hay không",
                                "recommendation": "Thận trọng khi cho con bú",
                        },
                },
                "hepatic_adjustment": {
                        "mild": "Không đổi",
                        "moderate": "Thận trọng",
                        "severe": "Thận trọng, dữ liệu hạn chế",
                        "notes": "Cần bổ sung thông tin từ tài liệu FDA",
                },
                "overdose_management": {
                        "symptoms": [
                                "Cần bổ sung",
                        ],
                        "antidote": "Không có antidote đặc hiệu",
                        "treatment": [
                                "Điều trị hỗ trợ",
                        ],
                        "monitoring": "Theo dõi dấu hiệu sinh tồn",
                },
                "reversal_agents": {
                        "available": False,
                        "agents": [],
                },
                "administration_instructions": {
                        "oral": {
                                "with_food": "Cần bổ sung",
                                "timing": "Cần bổ sung",
                        },
                },
                "references": {
                        "primary_sources": [
                                "FDA Drug Label - Repotrectinib (Augtyro)",
                                "FDA Approval Date: 2023",
                                "FDA-approved use: To treat ROS1-positive non-small cell lung cancer",
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
                        "FDA Drug Information - Repotrectinib (Augtyro)",
                ],
                "last_updated": "2026-01-15",
        },
    "Fruzaqla": {
                "group": "FDA Approved 2023",
                "vietnamese_name": "Fruquintinib, Fruzaqla",
                "administration": [
                        "PO",
                ],
                "indications": [
                        "To treat refractory, metastatic colorectal cancer",
                ],
                "contraindications": [
                        "Dị ứng fruquintinib hoặc bất kỳ thành phần nào",
                ],
                "dosage": {
                        "adult_standard": "Theo chỉ định của bác sĩ",
                        "notes": "FDA phê duyệt 2023. To treat refractory, metastatic colorectal cancer",
                },
                "renal_adjustment": {
                        "normal": "Không cần chỉnh liều",
                        "30_60": "Thận trọng",
                        "under_30": "Thận trọng, dữ liệu hạn chế",
                },
                "side_effects": [
                        "Cần bổ sung thông tin từ tài liệu FDA",
                ],
                "interactions": [
                        "Cần bổ sung thông tin từ tài liệu FDA",
                ],
                "pregnancy": "C",
                "mechanism_of_action": "Fruquintinib được FDA phê duyệt 2023 để to treat refractory, metastatic colorectal cancer. Cần bổ sung thông tin chi tiết về cơ chế tác dụng.",
                "monitoring": [
                        "Theo dõi đáp ứng điều trị",
                        "Theo dõi tác dụng phụ",
                ],
                "precautions": [
                        "Dị ứng fruquintinib",
                        "Cần bổ sung thông tin từ tài liệu FDA",
                ],
                "pharmacokinetics": {
                        "half_life": "Cần bổ sung",
                        "onset": "Cần bổ sung",
                        "duration": "Cần bổ sung",
                        "protein_binding": "Cần bổ sung",
                        "metabolism": "Cần bổ sung",
                        "clearance": "Cần bổ sung",
                },
                "storage": "Bảo quản theo hướng dẫn của nhà sản xuất",
                "black_box_warnings": "Cần kiểm tra tài liệu FDA",
                "drug_interactions": {
                        "major": [],
                        "moderate": [],
                        "minor": [],
                },
                "contraindications_detail": {
                        "tuyệt_đối": [
                                "Dị ứng fruquintinib hoặc bất kỳ thành phần nào",
                        ],
                        "tương_đối": [],
                },
                "pregnancy_lactation": {
                        "fda_category": "C",
                        "pregnancy_details": "Cần bổ sung thông tin từ tài liệu FDA",
                        "lactation": {
                                "safety": "Unknown",
                                "details": "Chưa biết có bài tiết vào sữa mẹ hay không",
                                "recommendation": "Thận trọng khi cho con bú",
                        },
                },
                "hepatic_adjustment": {
                        "mild": "Không đổi",
                        "moderate": "Thận trọng",
                        "severe": "Thận trọng, dữ liệu hạn chế",
                        "notes": "Cần bổ sung thông tin từ tài liệu FDA",
                },
                "overdose_management": {
                        "symptoms": [
                                "Cần bổ sung",
                        ],
                        "antidote": "Không có antidote đặc hiệu",
                        "treatment": [
                                "Điều trị hỗ trợ",
                        ],
                        "monitoring": "Theo dõi dấu hiệu sinh tồn",
                },
                "reversal_agents": {
                        "available": False,
                        "agents": [],
                },
                "administration_instructions": {
                        "oral": {
                                "with_food": "Cần bổ sung",
                                "timing": "Cần bổ sung",
                        },
                },
                "references": {
                        "primary_sources": [
                                "FDA Drug Label - Fruquintinib (Fruzaqla)",
                                "FDA Approval Date: 2023",
                                "FDA-approved use: To treat refractory, metastatic colorectal cancer",
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
                        "FDA Drug Information - Fruquintinib (Fruzaqla)",
                ],
                "last_updated": "2026-01-15",
        },
    "Jaypirca": {
                "group": "FDA Approved 2023",
                "vietnamese_name": "Pirtobrutinib, Jaypirca",
                "administration": [
                        "PO",
                ],
                "indications": [
                        "To treat relapsed or refractory mantle cell lymphoma in adults who have had at least two lines of systemic therapy, including a BTK inhibitor",
                ],
                "contraindications": [
                        "Dị ứng pirtobrutinib hoặc bất kỳ thành phần nào",
                ],
                "dosage": {
                        "adult_standard": "Theo chỉ định của bác sĩ",
                        "notes": "FDA phê duyệt 2023. To treat relapsed or refractory mantle cell lymphoma in adults who have had at least two lines of systemic therapy, including a BTK inhibitor",
                },
                "renal_adjustment": {
                        "normal": "Không cần chỉnh liều",
                        "30_60": "Thận trọng",
                        "under_30": "Thận trọng, dữ liệu hạn chế",
                },
                "side_effects": [
                        "Cần bổ sung thông tin từ tài liệu FDA",
                ],
                "interactions": [
                        "Cần bổ sung thông tin từ tài liệu FDA",
                ],
                "pregnancy": "C",
                "mechanism_of_action": "Pirtobrutinib được FDA phê duyệt 2023 để to treat relapsed or refractory mantle cell lymphoma in adults who have had at least two lines of systemic therapy, including a btk inhibitor. Cần bổ sung thông tin chi tiết về cơ chế tác dụng.",
                "monitoring": [
                        "Theo dõi đáp ứng điều trị",
                        "Theo dõi tác dụng phụ",
                ],
                "precautions": [
                        "Dị ứng pirtobrutinib",
                        "Cần bổ sung thông tin từ tài liệu FDA",
                ],
                "pharmacokinetics": {
                        "half_life": "Cần bổ sung",
                        "onset": "Cần bổ sung",
                        "duration": "Cần bổ sung",
                        "protein_binding": "Cần bổ sung",
                        "metabolism": "Cần bổ sung",
                        "clearance": "Cần bổ sung",
                },
                "storage": "Bảo quản theo hướng dẫn của nhà sản xuất",
                "black_box_warnings": "Cần kiểm tra tài liệu FDA",
                "drug_interactions": {
                        "major": [],
                        "moderate": [],
                        "minor": [],
                },
                "contraindications_detail": {
                        "tuyệt_đối": [
                                "Dị ứng pirtobrutinib hoặc bất kỳ thành phần nào",
                        ],
                        "tương_đối": [],
                },
                "pregnancy_lactation": {
                        "fda_category": "C",
                        "pregnancy_details": "Cần bổ sung thông tin từ tài liệu FDA",
                        "lactation": {
                                "safety": "Unknown",
                                "details": "Chưa biết có bài tiết vào sữa mẹ hay không",
                                "recommendation": "Thận trọng khi cho con bú",
                        },
                },
                "hepatic_adjustment": {
                        "mild": "Không đổi",
                        "moderate": "Thận trọng",
                        "severe": "Thận trọng, dữ liệu hạn chế",
                        "notes": "Cần bổ sung thông tin từ tài liệu FDA",
                },
                "overdose_management": {
                        "symptoms": [
                                "Cần bổ sung",
                        ],
                        "antidote": "Không có antidote đặc hiệu",
                        "treatment": [
                                "Điều trị hỗ trợ",
                        ],
                        "monitoring": "Theo dõi dấu hiệu sinh tồn",
                },
                "reversal_agents": {
                        "available": False,
                        "agents": [],
                },
                "administration_instructions": {
                        "oral": {
                                "with_food": "Cần bổ sung",
                                "timing": "Cần bổ sung",
                        },
                },
                "references": {
                        "primary_sources": [
                                "FDA Drug Label - Pirtobrutinib (Jaypirca)",
                                "FDA Approval Date: 2023",
                                "FDA-approved use: To treat relapsed or refractory mantle cell lymphoma in adults who have had at least two lines of systemic therapy, including a BTK inhibitor",
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
                        "FDA Drug Information - Pirtobrutinib (Jaypirca)",
                ],
                "last_updated": "2026-01-15",
        },
    "Vanflyta": {
                "group": "FDA Approved 2023",
                "vietnamese_name": "Quizartinib, Vanflyta",
                "administration": [
                        "PO",
                ],
                "indications": [
                        "To use as part of a treatment regimen for newly diagnosed acute myeloid leukemia that meets certain criteria",
                ],
                "contraindications": [
                        "Dị ứng quizartinib hoặc bất kỳ thành phần nào",
                ],
                "dosage": {
                        "adult_standard": "Theo chỉ định của bác sĩ",
                        "notes": "FDA phê duyệt 2023. To use as part of a treatment regimen for newly diagnosed acute myeloid leukemia that meets certain criteria",
                },
                "renal_adjustment": {
                        "normal": "Không cần chỉnh liều",
                        "30_60": "Thận trọng",
                        "under_30": "Thận trọng, dữ liệu hạn chế",
                },
                "side_effects": [
                        "Cần bổ sung thông tin từ tài liệu FDA",
                ],
                "interactions": [
                        "Cần bổ sung thông tin từ tài liệu FDA",
                ],
                "pregnancy": "C",
                "mechanism_of_action": "Quizartinib được FDA phê duyệt 2023 để to use as part of a treatment regimen for newly diagnosed acute myeloid leukemia that meets certain criteria. Cần bổ sung thông tin chi tiết về cơ chế tác dụng.",
                "monitoring": [
                        "Theo dõi đáp ứng điều trị",
                        "Theo dõi tác dụng phụ",
                ],
                "precautions": [
                        "Dị ứng quizartinib",
                        "Cần bổ sung thông tin từ tài liệu FDA",
                ],
                "pharmacokinetics": {
                        "half_life": "Cần bổ sung",
                        "onset": "Cần bổ sung",
                        "duration": "Cần bổ sung",
                        "protein_binding": "Cần bổ sung",
                        "metabolism": "Cần bổ sung",
                        "clearance": "Cần bổ sung",
                },
                "storage": "Bảo quản theo hướng dẫn của nhà sản xuất",
                "black_box_warnings": "Cần kiểm tra tài liệu FDA",
                "drug_interactions": {
                        "major": [],
                        "moderate": [],
                        "minor": [],
                },
                "contraindications_detail": {
                        "tuyệt_đối": [
                                "Dị ứng quizartinib hoặc bất kỳ thành phần nào",
                        ],
                        "tương_đối": [],
                },
                "pregnancy_lactation": {
                        "fda_category": "C",
                        "pregnancy_details": "Cần bổ sung thông tin từ tài liệu FDA",
                        "lactation": {
                                "safety": "Unknown",
                                "details": "Chưa biết có bài tiết vào sữa mẹ hay không",
                                "recommendation": "Thận trọng khi cho con bú",
                        },
                },
                "hepatic_adjustment": {
                        "mild": "Không đổi",
                        "moderate": "Thận trọng",
                        "severe": "Thận trọng, dữ liệu hạn chế",
                        "notes": "Cần bổ sung thông tin từ tài liệu FDA",
                },
                "overdose_management": {
                        "symptoms": [
                                "Cần bổ sung",
                        ],
                        "antidote": "Không có antidote đặc hiệu",
                        "treatment": [
                                "Điều trị hỗ trợ",
                        ],
                        "monitoring": "Theo dõi dấu hiệu sinh tồn",
                },
                "reversal_agents": {
                        "available": False,
                        "agents": [],
                },
                "administration_instructions": {
                        "oral": {
                                "with_food": "Cần bổ sung",
                                "timing": "Cần bổ sung",
                        },
                },
                "references": {
                        "primary_sources": [
                                "FDA Drug Label - Quizartinib (Vanflyta)",
                                "FDA Approval Date: 2023",
                                "FDA-approved use: To use as part of a treatment regimen for newly diagnosed acute myeloid leukemia that meets certain criteria",
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
                        "FDA Drug Information - Quizartinib (Vanflyta)",
                ],
                "last_updated": "2026-01-15",
        },
    "Ensacove": {
                "group": "FDA Approved 2024",
                "vietnamese_name": "Ensartinib, Ensacove",
                "administration": [
                        "PO",
                ],
                "indications": [
                        "To treat non-small cell lung cancer",
                ],
                "contraindications": [
                        "Dị ứng ensartinib hoặc bất kỳ thành phần nào",
                ],
                "dosage": {
                        "adult_standard": "Theo chỉ định của bác sĩ",
                        "notes": "FDA phê duyệt 2024. To treat non-small cell lung cancer",
                },
                "renal_adjustment": {
                        "normal": "Không cần chỉnh liều",
                        "30_60": "Thận trọng",
                        "under_30": "Thận trọng, dữ liệu hạn chế",
                },
                "side_effects": [
                        "Cần bổ sung thông tin từ tài liệu FDA",
                ],
                "interactions": [
                        "Cần bổ sung thông tin từ tài liệu FDA",
                ],
                "pregnancy": "C",
                "mechanism_of_action": "Ensartinib được FDA phê duyệt 2024 để to treat non-small cell lung cancer. Cần bổ sung thông tin chi tiết về cơ chế tác dụng.",
                "monitoring": [
                        "Theo dõi đáp ứng điều trị",
                        "Theo dõi tác dụng phụ",
                ],
                "precautions": [
                        "Dị ứng ensartinib",
                        "Cần bổ sung thông tin từ tài liệu FDA",
                ],
                "pharmacokinetics": {
                        "half_life": "Cần bổ sung",
                        "onset": "Cần bổ sung",
                        "duration": "Cần bổ sung",
                        "protein_binding": "Cần bổ sung",
                        "metabolism": "Cần bổ sung",
                        "clearance": "Cần bổ sung",
                },
                "storage": "Bảo quản theo hướng dẫn của nhà sản xuất",
                "black_box_warnings": "Cần kiểm tra tài liệu FDA",
                "drug_interactions": {
                        "major": [],
                        "moderate": [],
                        "minor": [],
                },
                "contraindications_detail": {
                        "tuyệt_đối": [
                                "Dị ứng ensartinib hoặc bất kỳ thành phần nào",
                        ],
                        "tương_đối": [],
                },
                "pregnancy_lactation": {
                        "fda_category": "C",
                        "pregnancy_details": "Cần bổ sung thông tin từ tài liệu FDA",
                        "lactation": {
                                "safety": "Unknown",
                                "details": "Chưa biết có bài tiết vào sữa mẹ hay không",
                                "recommendation": "Thận trọng khi cho con bú",
                        },
                },
                "hepatic_adjustment": {
                        "mild": "Không đổi",
                        "moderate": "Thận trọng",
                        "severe": "Thận trọng, dữ liệu hạn chế",
                        "notes": "Cần bổ sung thông tin từ tài liệu FDA",
                },
                "overdose_management": {
                        "symptoms": [
                                "Cần bổ sung",
                        ],
                        "antidote": "Không có antidote đặc hiệu",
                        "treatment": [
                                "Điều trị hỗ trợ",
                        ],
                        "monitoring": "Theo dõi dấu hiệu sinh tồn",
                },
                "reversal_agents": {
                        "available": False,
                        "agents": [],
                },
                "administration_instructions": {
                        "oral": {
                                "with_food": "Cần bổ sung",
                                "timing": "Cần bổ sung",
                        },
                },
                "references": {
                        "primary_sources": [
                                "FDA Drug Label - Ensartinib (Ensacove)",
                                "FDA Approval Date: 2024",
                                "FDA-approved use: To treat non-small cell lung cancer",
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
                        "FDA Drug Information - Ensartinib (Ensacove)",
                ],
                "last_updated": "2026-01-15",
        },
    "Lazcluze": {
                "group": "FDA Approved 2024",
                "vietnamese_name": "Lazertinib, Lazcluze",
                "administration": [
                        "PO",
                ],
                "indications": [
                        "To treat non-small cell lung cancer",
                ],
                "contraindications": [
                        "Dị ứng lazertinib hoặc bất kỳ thành phần nào",
                ],
                "dosage": {
                        "adult_standard": "Theo chỉ định của bác sĩ",
                        "notes": "FDA phê duyệt 2024. To treat non-small cell lung cancer",
                },
                "renal_adjustment": {
                        "normal": "Không cần chỉnh liều",
                        "30_60": "Thận trọng",
                        "under_30": "Thận trọng, dữ liệu hạn chế",
                },
                "side_effects": [
                        "Cần bổ sung thông tin từ tài liệu FDA",
                ],
                "interactions": [
                        "Cần bổ sung thông tin từ tài liệu FDA",
                ],
                "pregnancy": "C",
                "mechanism_of_action": "Lazertinib được FDA phê duyệt 2024 để to treat non-small cell lung cancer. Cần bổ sung thông tin chi tiết về cơ chế tác dụng.",
                "monitoring": [
                        "Theo dõi đáp ứng điều trị",
                        "Theo dõi tác dụng phụ",
                ],
                "precautions": [
                        "Dị ứng lazertinib",
                        "Cần bổ sung thông tin từ tài liệu FDA",
                ],
                "pharmacokinetics": {
                        "half_life": "Cần bổ sung",
                        "onset": "Cần bổ sung",
                        "duration": "Cần bổ sung",
                        "protein_binding": "Cần bổ sung",
                        "metabolism": "Cần bổ sung",
                        "clearance": "Cần bổ sung",
                },
                "storage": "Bảo quản theo hướng dẫn của nhà sản xuất",
                "black_box_warnings": "Cần kiểm tra tài liệu FDA",
                "drug_interactions": {
                        "major": [],
                        "moderate": [],
                        "minor": [],
                },
                "contraindications_detail": {
                        "tuyệt_đối": [
                                "Dị ứng lazertinib hoặc bất kỳ thành phần nào",
                        ],
                        "tương_đối": [],
                },
                "pregnancy_lactation": {
                        "fda_category": "C",
                        "pregnancy_details": "Cần bổ sung thông tin từ tài liệu FDA",
                        "lactation": {
                                "safety": "Unknown",
                                "details": "Chưa biết có bài tiết vào sữa mẹ hay không",
                                "recommendation": "Thận trọng khi cho con bú",
                        },
                },
                "hepatic_adjustment": {
                        "mild": "Không đổi",
                        "moderate": "Thận trọng",
                        "severe": "Thận trọng, dữ liệu hạn chế",
                        "notes": "Cần bổ sung thông tin từ tài liệu FDA",
                },
                "overdose_management": {
                        "symptoms": [
                                "Cần bổ sung",
                        ],
                        "antidote": "Không có antidote đặc hiệu",
                        "treatment": [
                                "Điều trị hỗ trợ",
                        ],
                        "monitoring": "Theo dõi dấu hiệu sinh tồn",
                },
                "reversal_agents": {
                        "available": False,
                        "agents": [],
                },
                "administration_instructions": {
                        "oral": {
                                "with_food": "Cần bổ sung",
                                "timing": "Cần bổ sung",
                        },
                },
                "references": {
                        "primary_sources": [
                                "FDA Drug Label - Lazertinib (Lazcluze)",
                                "FDA Approval Date: 2024",
                                "FDA-approved use: To treat non-small cell lung cancer",
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
                        "FDA Drug Information - Lazertinib (Lazcluze)",
                ],
                "last_updated": "2026-01-15",
        },
    "AvmapkiFakzynjaCoPack": {
                "group": "FDA Approved 2025",
                "vietnamese_name": "Avutometinib, Avmapki Fakzynja Co-Pack",
                "administration": [
                        "PO",
                ],
                "indications": [
                        "To treat KRAS-mutated recurrent low-grade serous ovarian cancer (LGSOC) after prior systemic therapy",
                ],
                "contraindications": [
                        "Dị ứng avutometinib hoặc bất kỳ thành phần nào",
                ],
                "dosage": {
                        "adult_standard": "Theo chỉ định của bác sĩ",
                        "notes": "FDA phê duyệt 2025. To treat KRAS-mutated recurrent low-grade serous ovarian cancer (LGSOC) after prior systemic therapy",
                },
                "renal_adjustment": {
                        "normal": "Không cần chỉnh liều",
                        "30_60": "Thận trọng",
                        "under_30": "Thận trọng, dữ liệu hạn chế",
                },
                "side_effects": [
                        "Cần bổ sung thông tin từ tài liệu FDA",
                ],
                "interactions": [
                        "Cần bổ sung thông tin từ tài liệu FDA",
                ],
                "pregnancy": "C",
                "mechanism_of_action": "Avutometinib được FDA phê duyệt 2025 để to treat kras-mutated recurrent low-grade serous ovarian cancer (lgsoc) after prior systemic therapy. Cần bổ sung thông tin chi tiết về cơ chế tác dụng.",
                "monitoring": [
                        "Theo dõi đáp ứng điều trị",
                        "Theo dõi tác dụng phụ",
                ],
                "precautions": [
                        "Dị ứng avutometinib",
                        "Cần bổ sung thông tin từ tài liệu FDA",
                ],
                "pharmacokinetics": {
                        "half_life": "Cần bổ sung",
                        "onset": "Cần bổ sung",
                        "duration": "Cần bổ sung",
                        "protein_binding": "Cần bổ sung",
                        "metabolism": "Cần bổ sung",
                        "clearance": "Cần bổ sung",
                },
                "storage": "Bảo quản theo hướng dẫn của nhà sản xuất",
                "black_box_warnings": "Cần kiểm tra tài liệu FDA",
                "drug_interactions": {
                        "major": [],
                        "moderate": [],
                        "minor": [],
                },
                "contraindications_detail": {
                        "tuyệt_đối": [
                                "Dị ứng avutometinib hoặc bất kỳ thành phần nào",
                        ],
                        "tương_đối": [],
                },
                "pregnancy_lactation": {
                        "fda_category": "C",
                        "pregnancy_details": "Cần bổ sung thông tin từ tài liệu FDA",
                        "lactation": {
                                "safety": "Unknown",
                                "details": "Chưa biết có bài tiết vào sữa mẹ hay không",
                                "recommendation": "Thận trọng khi cho con bú",
                        },
                },
                "hepatic_adjustment": {
                        "mild": "Không đổi",
                        "moderate": "Thận trọng",
                        "severe": "Thận trọng, dữ liệu hạn chế",
                        "notes": "Cần bổ sung thông tin từ tài liệu FDA",
                },
                "overdose_management": {
                        "symptoms": [
                                "Cần bổ sung",
                        ],
                        "antidote": "Không có antidote đặc hiệu",
                        "treatment": [
                                "Điều trị hỗ trợ",
                        ],
                        "monitoring": "Theo dõi dấu hiệu sinh tồn",
                },
                "reversal_agents": {
                        "available": False,
                        "agents": [],
                },
                "administration_instructions": {
                        "oral": {
                                "with_food": "Cần bổ sung",
                                "timing": "Cần bổ sung",
                        },
                },
                "references": {
                        "primary_sources": [
                                "FDA Drug Label - Avutometinib (Avmapki Fakzynja Co-Pack)",
                                "FDA Approval Date: 2025",
                                "FDA-approved use: To treat KRAS-mutated recurrent low-grade serous ovarian cancer (LGSOC) after prior systemic therapy",
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
                        "FDA Drug Information - Avutometinib (Avmapki Fakzynja Co-Pack)",
                ],
                "last_updated": "2026-01-15",
        },
    "Hernexeos": {
                "group": "FDA Approved 2025",
                "vietnamese_name": "Zongertinib, Hernexeos",
                "administration": [
                        "IV",
                        "SC",
                ],
                "indications": [
                        "To treat adults with unresectable or metastatic non-squamous non-small cell lung cancer whose tumors have HER2 tyrosine kinase domain activating mutations, as detected by an FDA-approved test, and who have received prior systemic therapy",
                ],
                "contraindications": [
                        "Dị ứng zongertinib hoặc bất kỳ thành phần nào",
                ],
                "dosage": {
                        "adult_standard": "Theo chỉ định của bác sĩ",
                        "notes": "FDA phê duyệt 2025. To treat adults with unresectable or metastatic non-squamous non-small cell lung cancer whose tumors have HER2 tyrosine kinase domain activating mutations, as detected by an FDA-approved test, and who have received prior systemic therapy",
                },
                "renal_adjustment": {
                        "normal": "Không cần chỉnh liều",
                        "30_60": "Thận trọng",
                        "under_30": "Thận trọng, dữ liệu hạn chế",
                },
                "side_effects": [
                        "Cần bổ sung thông tin từ tài liệu FDA",
                ],
                "interactions": [
                        "Cần bổ sung thông tin từ tài liệu FDA",
                ],
                "pregnancy": "C",
                "mechanism_of_action": "Zongertinib được FDA phê duyệt 2025 để to treat adults with unresectable or metastatic non-squamous non-small cell lung cancer whose tumors have her2 tyrosine kinase domain activating mutations, as detected by an fda-approved test, and who have received prior systemic therapy. Cần bổ sung thông tin chi tiết về cơ chế tác dụng.",
                "monitoring": [
                        "Theo dõi đáp ứng điều trị",
                        "Theo dõi tác dụng phụ",
                ],
                "precautions": [
                        "Dị ứng zongertinib",
                        "Cần bổ sung thông tin từ tài liệu FDA",
                ],
                "pharmacokinetics": {
                        "half_life": "Cần bổ sung",
                        "onset": "Cần bổ sung",
                        "duration": "Cần bổ sung",
                        "protein_binding": "Cần bổ sung",
                        "metabolism": "Cần bổ sung",
                        "clearance": "Cần bổ sung",
                },
                "storage": "Bảo quản theo hướng dẫn của nhà sản xuất",
                "black_box_warnings": "Cần kiểm tra tài liệu FDA",
                "drug_interactions": {
                        "major": [],
                        "moderate": [],
                        "minor": [],
                },
                "contraindications_detail": {
                        "tuyệt_đối": [
                                "Dị ứng zongertinib hoặc bất kỳ thành phần nào",
                        ],
                        "tương_đối": [],
                },
                "pregnancy_lactation": {
                        "fda_category": "C",
                        "pregnancy_details": "Cần bổ sung thông tin từ tài liệu FDA",
                        "lactation": {
                                "safety": "Unknown",
                                "details": "Chưa biết có bài tiết vào sữa mẹ hay không",
                                "recommendation": "Thận trọng khi cho con bú",
                        },
                },
                "hepatic_adjustment": {
                        "mild": "Không đổi",
                        "moderate": "Thận trọng",
                        "severe": "Thận trọng, dữ liệu hạn chế",
                        "notes": "Cần bổ sung thông tin từ tài liệu FDA",
                },
                "overdose_management": {
                        "symptoms": [
                                "Cần bổ sung",
                        ],
                        "antidote": "Không có antidote đặc hiệu",
                        "treatment": [
                                "Điều trị hỗ trợ",
                        ],
                        "monitoring": "Theo dõi dấu hiệu sinh tồn",
                },
                "reversal_agents": {
                        "available": False,
                        "agents": [],
                },
                "administration_instructions": {
                        "oral": {
                                "with_food": "Cần bổ sung",
                                "timing": "Cần bổ sung",
                        },
                },
                "references": {
                        "primary_sources": [
                                "FDA Drug Label - Zongertinib (Hernexeos)",
                                "FDA Approval Date: 2025",
                                "FDA-approved use: To treat adults with unresectable or metastatic non-squamous non-small cell lung cancer whose tumors have HER2 tyrosine kinase domain activating mutations, as detected by an FDA-approved test, and who have received prior systemic therapy",
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
                        "FDA Drug Information - Zongertinib (Hernexeos)",
                ],
                "last_updated": "2026-01-15",
        },
    "Hyrnuo": {
                "group": "FDA Approved 2025",
                "vietnamese_name": "Sevabertinib, Hyrnuo",
                "administration": [
                        "IV",
                        "SC",
                ],
                "indications": [
                        "To treat locally advanced or metastatic non-squamous non-small cell lung cancer with tumors that have activating HER2 tyrosine kinase domain activating mutations in patients who received a systemic therapy",
                ],
                "contraindications": [
                        "Dị ứng sevabertinib hoặc bất kỳ thành phần nào",
                ],
                "dosage": {
                        "adult_standard": "Theo chỉ định của bác sĩ",
                        "notes": "FDA phê duyệt 2025. To treat locally advanced or metastatic non-squamous non-small cell lung cancer with tumors that have activating HER2 tyrosine kinase domain activating mutations in patients who received a systemic therapy",
                },
                "renal_adjustment": {
                        "normal": "Không cần chỉnh liều",
                        "30_60": "Thận trọng",
                        "under_30": "Thận trọng, dữ liệu hạn chế",
                },
                "side_effects": [
                        "Cần bổ sung thông tin từ tài liệu FDA",
                ],
                "interactions": [
                        "Cần bổ sung thông tin từ tài liệu FDA",
                ],
                "pregnancy": "C",
                "mechanism_of_action": "Sevabertinib được FDA phê duyệt 2025 để to treat locally advanced or metastatic non-squamous non-small cell lung cancer with tumors that have activating her2 tyrosine kinase domain activating mutations in patients who received a systemic therapy. Cần bổ sung thông tin chi tiết về cơ chế tác dụng.",
                "monitoring": [
                        "Theo dõi đáp ứng điều trị",
                        "Theo dõi tác dụng phụ",
                ],
                "precautions": [
                        "Dị ứng sevabertinib",
                        "Cần bổ sung thông tin từ tài liệu FDA",
                ],
                "pharmacokinetics": {
                        "half_life": "Cần bổ sung",
                        "onset": "Cần bổ sung",
                        "duration": "Cần bổ sung",
                        "protein_binding": "Cần bổ sung",
                        "metabolism": "Cần bổ sung",
                        "clearance": "Cần bổ sung",
                },
                "storage": "Bảo quản theo hướng dẫn của nhà sản xuất",
                "black_box_warnings": "Cần kiểm tra tài liệu FDA",
                "drug_interactions": {
                        "major": [],
                        "moderate": [],
                        "minor": [],
                },
                "contraindications_detail": {
                        "tuyệt_đối": [
                                "Dị ứng sevabertinib hoặc bất kỳ thành phần nào",
                        ],
                        "tương_đối": [],
                },
                "pregnancy_lactation": {
                        "fda_category": "C",
                        "pregnancy_details": "Cần bổ sung thông tin từ tài liệu FDA",
                        "lactation": {
                                "safety": "Unknown",
                                "details": "Chưa biết có bài tiết vào sữa mẹ hay không",
                                "recommendation": "Thận trọng khi cho con bú",
                        },
                },
                "hepatic_adjustment": {
                        "mild": "Không đổi",
                        "moderate": "Thận trọng",
                        "severe": "Thận trọng, dữ liệu hạn chế",
                        "notes": "Cần bổ sung thông tin từ tài liệu FDA",
                },
                "overdose_management": {
                        "symptoms": [
                                "Cần bổ sung",
                        ],
                        "antidote": "Không có antidote đặc hiệu",
                        "treatment": [
                                "Điều trị hỗ trợ",
                        ],
                        "monitoring": "Theo dõi dấu hiệu sinh tồn",
                },
                "reversal_agents": {
                        "available": False,
                        "agents": [],
                },
                "administration_instructions": {
                        "oral": {
                                "with_food": "Cần bổ sung",
                                "timing": "Cần bổ sung",
                        },
                },
                "references": {
                        "primary_sources": [
                                "FDA Drug Label - Sevabertinib (Hyrnuo)",
                                "FDA Approval Date: 2025",
                                "FDA-approved use: To treat locally advanced or metastatic non-squamous non-small cell lung cancer with tumors that have activating HER2 tyrosine kinase domain activating mutations in patients who received a systemic therapy",
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
                        "FDA Drug Information - Sevabertinib (Hyrnuo)",
                ],
                "last_updated": "2026-01-15",
        },
    "Ibtrozi": {
                "group": "FDA Approved 2025",
                "vietnamese_name": "Taletrectinib, Ibtrozi",
                "administration": [
                        "IV",
                        "SC",
                ],
                "indications": [
                        "To treat locally advanced or metastatic ROS1-positive non-small cell lung cancer",
                ],
                "contraindications": [
                        "Dị ứng taletrectinib hoặc bất kỳ thành phần nào",
                ],
                "dosage": {
                        "adult_standard": "Theo chỉ định của bác sĩ",
                        "notes": "FDA phê duyệt 2025. To treat locally advanced or metastatic ROS1-positive non-small cell lung cancer",
                },
                "renal_adjustment": {
                        "normal": "Không cần chỉnh liều",
                        "30_60": "Thận trọng",
                        "under_30": "Thận trọng, dữ liệu hạn chế",
                },
                "side_effects": [
                        "Cần bổ sung thông tin từ tài liệu FDA",
                ],
                "interactions": [
                        "Cần bổ sung thông tin từ tài liệu FDA",
                ],
                "pregnancy": "C",
                "mechanism_of_action": "Taletrectinib được FDA phê duyệt 2025 để to treat locally advanced or metastatic ros1-positive non-small cell lung cancer. Cần bổ sung thông tin chi tiết về cơ chế tác dụng.",
                "monitoring": [
                        "Theo dõi đáp ứng điều trị",
                        "Theo dõi tác dụng phụ",
                ],
                "precautions": [
                        "Dị ứng taletrectinib",
                        "Cần bổ sung thông tin từ tài liệu FDA",
                ],
                "pharmacokinetics": {
                        "half_life": "Cần bổ sung",
                        "onset": "Cần bổ sung",
                        "duration": "Cần bổ sung",
                        "protein_binding": "Cần bổ sung",
                        "metabolism": "Cần bổ sung",
                        "clearance": "Cần bổ sung",
                },
                "storage": "Bảo quản theo hướng dẫn của nhà sản xuất",
                "black_box_warnings": "Cần kiểm tra tài liệu FDA",
                "drug_interactions": {
                        "major": [],
                        "moderate": [],
                        "minor": [],
                },
                "contraindications_detail": {
                        "tuyệt_đối": [
                                "Dị ứng taletrectinib hoặc bất kỳ thành phần nào",
                        ],
                        "tương_đối": [],
                },
                "pregnancy_lactation": {
                        "fda_category": "C",
                        "pregnancy_details": "Cần bổ sung thông tin từ tài liệu FDA",
                        "lactation": {
                                "safety": "Unknown",
                                "details": "Chưa biết có bài tiết vào sữa mẹ hay không",
                                "recommendation": "Thận trọng khi cho con bú",
                        },
                },
                "hepatic_adjustment": {
                        "mild": "Không đổi",
                        "moderate": "Thận trọng",
                        "severe": "Thận trọng, dữ liệu hạn chế",
                        "notes": "Cần bổ sung thông tin từ tài liệu FDA",
                },
                "overdose_management": {
                        "symptoms": [
                                "Cần bổ sung",
                        ],
                        "antidote": "Không có antidote đặc hiệu",
                        "treatment": [
                                "Điều trị hỗ trợ",
                        ],
                        "monitoring": "Theo dõi dấu hiệu sinh tồn",
                },
                "reversal_agents": {
                        "available": False,
                        "agents": [],
                },
                "administration_instructions": {
                        "oral": {
                                "with_food": "Cần bổ sung",
                                "timing": "Cần bổ sung",
                        },
                },
                "references": {
                        "primary_sources": [
                                "FDA Drug Label - Taletrectinib (Ibtrozi)",
                                "FDA Approval Date: 2025",
                                "FDA-approved use: To treat locally advanced or metastatic ROS1-positive non-small cell lung cancer",
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
                        "FDA Drug Information - Taletrectinib (Ibtrozi)",
                ],
                "last_updated": "2026-01-15",
        },
    "Romvimza": {
                "group": "FDA Approved 2025",
                "vietnamese_name": "Vimseltinib, Romvimza",
                "administration": [
                        "PO",
                ],
                "indications": [
                        "To treat symptomatic tenosynovial giant cell tumor for which surgical resection will potentially cause worsening functional limitation or severe morbidity",
                ],
                "contraindications": [
                        "Dị ứng vimseltinib hoặc bất kỳ thành phần nào",
                ],
                "dosage": {
                        "adult_standard": "Theo chỉ định của bác sĩ",
                        "notes": "FDA phê duyệt 2025. To treat symptomatic tenosynovial giant cell tumor for which surgical resection will potentially cause worsening functional limitation or severe morbidity",
                },
                "renal_adjustment": {
                        "normal": "Không cần chỉnh liều",
                        "30_60": "Thận trọng",
                        "under_30": "Thận trọng, dữ liệu hạn chế",
                },
                "side_effects": [
                        "Cần bổ sung thông tin từ tài liệu FDA",
                ],
                "interactions": [
                        "Cần bổ sung thông tin từ tài liệu FDA",
                ],
                "pregnancy": "C",
                "mechanism_of_action": "Vimseltinib được FDA phê duyệt 2025 để to treat symptomatic tenosynovial giant cell tumor for which surgical resection will potentially cause worsening functional limitation or severe morbidity. Cần bổ sung thông tin chi tiết về cơ chế tác dụng.",
                "monitoring": [
                        "Theo dõi đáp ứng điều trị",
                        "Theo dõi tác dụng phụ",
                ],
                "precautions": [
                        "Dị ứng vimseltinib",
                        "Cần bổ sung thông tin từ tài liệu FDA",
                ],
                "pharmacokinetics": {
                        "half_life": "Cần bổ sung",
                        "onset": "Cần bổ sung",
                        "duration": "Cần bổ sung",
                        "protein_binding": "Cần bổ sung",
                        "metabolism": "Cần bổ sung",
                        "clearance": "Cần bổ sung",
                },
                "storage": "Bảo quản theo hướng dẫn của nhà sản xuất",
                "black_box_warnings": "Cần kiểm tra tài liệu FDA",
                "drug_interactions": {
                        "major": [],
                        "moderate": [],
                        "minor": [],
                },
                "contraindications_detail": {
                        "tuyệt_đối": [
                                "Dị ứng vimseltinib hoặc bất kỳ thành phần nào",
                        ],
                        "tương_đối": [],
                },
                "pregnancy_lactation": {
                        "fda_category": "C",
                        "pregnancy_details": "Cần bổ sung thông tin từ tài liệu FDA",
                        "lactation": {
                                "safety": "Unknown",
                                "details": "Chưa biết có bài tiết vào sữa mẹ hay không",
                                "recommendation": "Thận trọng khi cho con bú",
                        },
                },
                "hepatic_adjustment": {
                        "mild": "Không đổi",
                        "moderate": "Thận trọng",
                        "severe": "Thận trọng, dữ liệu hạn chế",
                        "notes": "Cần bổ sung thông tin từ tài liệu FDA",
                },
                "overdose_management": {
                        "symptoms": [
                                "Cần bổ sung",
                        ],
                        "antidote": "Không có antidote đặc hiệu",
                        "treatment": [
                                "Điều trị hỗ trợ",
                        ],
                        "monitoring": "Theo dõi dấu hiệu sinh tồn",
                },
                "reversal_agents": {
                        "available": False,
                        "agents": [],
                },
                "administration_instructions": {
                        "oral": {
                                "with_food": "Cần bổ sung",
                                "timing": "Cần bổ sung",
                        },
                },
                "references": {
                        "primary_sources": [
                                "FDA Drug Label - Vimseltinib (Romvimza)",
                                "FDA Approval Date: 2025",
                                "FDA-approved use: To treat symptomatic tenosynovial giant cell tumor for which surgical resection will potentially cause worsening functional limitation or severe morbidity",
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
                        "FDA Drug Information - Vimseltinib (Romvimza)",
                ],
                "last_updated": "2026-01-15",
        },
    "Zegfrovy": {
                "group": "FDA Approved 2025",
                "vietnamese_name": "Sunvozertinib, Zegfrovy",
                "administration": [
                        "PO",
                ],
                "indications": [
                        "To treat locally advanced or metastatic non-small cell lung cancer with epidermal growth factor receptor exon 20 insertion mutations, as detected by an FDA-approved test, with disease progression on or after platinum-based chemotherapy",
                ],
                "contraindications": [
                        "Dị ứng sunvozertinib hoặc bất kỳ thành phần nào",
                ],
                "dosage": {
                        "adult_standard": "Theo chỉ định của bác sĩ",
                        "notes": "FDA phê duyệt 2025. To treat locally advanced or metastatic non-small cell lung cancer with epidermal growth factor receptor exon 20 insertion mutations, as detected by an FDA-approved test, with disease progression on or after platinum-based chemotherapy",
                },
                "renal_adjustment": {
                        "normal": "Không cần chỉnh liều",
                        "30_60": "Thận trọng",
                        "under_30": "Thận trọng, dữ liệu hạn chế",
                },
                "side_effects": [
                        "Cần bổ sung thông tin từ tài liệu FDA",
                ],
                "interactions": [
                        "Cần bổ sung thông tin từ tài liệu FDA",
                ],
                "pregnancy": "C",
                "mechanism_of_action": "Sunvozertinib được FDA phê duyệt 2025 để to treat locally advanced or metastatic non-small cell lung cancer with epidermal growth factor receptor exon 20 insertion mutations, as detected by an fda-approved test, with disease progression on or after platinum-based chemotherapy. Cần bổ sung thông tin chi tiết về cơ chế tác dụng.",
                "monitoring": [
                        "Theo dõi đáp ứng điều trị",
                        "Theo dõi tác dụng phụ",
                ],
                "precautions": [
                        "Dị ứng sunvozertinib",
                        "Cần bổ sung thông tin từ tài liệu FDA",
                ],
                "pharmacokinetics": {
                        "half_life": "Cần bổ sung",
                        "onset": "Cần bổ sung",
                        "duration": "Cần bổ sung",
                        "protein_binding": "Cần bổ sung",
                        "metabolism": "Cần bổ sung",
                        "clearance": "Cần bổ sung",
                },
                "storage": "Bảo quản theo hướng dẫn của nhà sản xuất",
                "black_box_warnings": "Cần kiểm tra tài liệu FDA",
                "drug_interactions": {
                        "major": [],
                        "moderate": [],
                        "minor": [],
                },
                "contraindications_detail": {
                        "tuyệt_đối": [
                                "Dị ứng sunvozertinib hoặc bất kỳ thành phần nào",
                        ],
                        "tương_đối": [],
                },
                "pregnancy_lactation": {
                        "fda_category": "C",
                        "pregnancy_details": "Cần bổ sung thông tin từ tài liệu FDA",
                        "lactation": {
                                "safety": "Unknown",
                                "details": "Chưa biết có bài tiết vào sữa mẹ hay không",
                                "recommendation": "Thận trọng khi cho con bú",
                        },
                },
                "hepatic_adjustment": {
                        "mild": "Không đổi",
                        "moderate": "Thận trọng",
                        "severe": "Thận trọng, dữ liệu hạn chế",
                        "notes": "Cần bổ sung thông tin từ tài liệu FDA",
                },
                "overdose_management": {
                        "symptoms": [
                                "Cần bổ sung",
                        ],
                        "antidote": "Không có antidote đặc hiệu",
                        "treatment": [
                                "Điều trị hỗ trợ",
                        ],
                        "monitoring": "Theo dõi dấu hiệu sinh tồn",
                },
                "reversal_agents": {
                        "available": False,
                        "agents": [],
                },
                "administration_instructions": {
                        "oral": {
                                "with_food": "Cần bổ sung",
                                "timing": "Cần bổ sung",
                        },
                },
                "references": {
                        "primary_sources": [
                                "FDA Drug Label - Sunvozertinib (Zegfrovy)",
                                "FDA Approval Date: 2025",
                                "FDA-approved use: To treat locally advanced or metastatic non-small cell lung cancer with epidermal growth factor receptor exon 20 insertion mutations, as detected by an FDA-approved test, with disease progression on or after platinum-based chemotherapy",
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
                        "FDA Drug Information - Sunvozertinib (Zegfrovy)",
                ],
                "last_updated": "2026-01-15",
        },
}

__all__ = ['TARGETED_THERAPY_TKIS_DRUGS']

