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
        ],,
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

}

__all__ = ['TARGETED_THERAPY_TKIS_DRUGS']

