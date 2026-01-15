"""Gastrointestinal Fixed-Dose Combination Drugs
PPI + NSAID, PPI + Prokinetic, Antacid + Simethicone, Alginate combinations, etc."""

GASTROINTESTINAL_FIXED_DOSE_COMBINATIONS = {
    "Esomeprazole/Naproxen": {
        "group": "Gastrointestinal - PPI + NSAID (Fixed-Dose Combination)",
        "vietnamese_name": "Esomeprazole/Naproxen, Vimovo",
        "administration": ["PO"],
        "indications": [
            "Điều trị đau do viêm khớp dạng thấp, viêm xương khớp, viêm cột sống dính khớp",
            "Phòng ngừa loét dạ dày do NSAID ở bệnh nhân có nguy cơ cao",
            "Khi cần điều trị đau và phòng ngừa loét dạ dày đồng thời"
        ],
        "contraindications": [
            "Dị ứng esomeprazole, naproxen, hoặc NSAID khác",
            "Loét dạ dày tá tràng đang hoạt động",
            "Suy tim nặng (NYHA class IV)",
            "Suy thận nặng (CrCl <30 ml/phút)",
            "Suy gan nặng",
            "Tam cá nguyệt thứ ba của thai kỳ",
            "Trẻ em <18 tuổi"
        ],
        "dosage": {
            "adult_po": "Esomeprazole 20mg/Naproxen 375mg hoặc 500mg PO x 2 lần/ngày",
            "adult_typical": "Esomeprazole 20mg/Naproxen 500mg PO x 2 lần/ngày",
            "adult_max": "Esomeprazole 20mg/Naproxen 500mg PO x 2 lần/ngày",
            "notes": "Uống ít nhất 30 phút trước bữa ăn. Nuốt nguyên viên, không nhai hoặc nghiền. Dùng liều thấp nhất có hiệu quả và trong thời gian ngắn nhất."
        },
        "renal_adjustment": {
            "normal": "Không cần chỉnh liều",
            "30_60": "Thận trọng, có thể cần giảm liều naproxen",
            "under_30": "CHỐNG CHỈ ĐỊNH",
            "dialysis": "CHỐNG CHỈ ĐỊNH",
            "notes": "Naproxen thải trừ qua thận. Suy thận làm giảm thải trừ, tăng nguy cơ độc tính thận và tim mạch."
        },
        "side_effects": [
            "Đau đầu",
            "Khó tiêu, đau bụng",
            "Tiêu chảy",
            "Buồn nôn",
            "Chóng mặt",
            "Phù",
            "Tăng huyết áp",
            "Nguy cơ tim mạch (nhồi máu cơ tim, đột quỵ)",
            "Nguy cơ loét dạ dày tá tràng (mặc dù có PPI)",
            "Suy thận cấp",
            "Tăng men gan"
        ],
        "interactions": [
            "Warfarin: naproxen tăng nguy cơ chảy máu",
            "Aspirin: tăng nguy cơ loét dạ dày",
            "ACE inhibitors, ARBs: giảm hiệu quả, tăng nguy cơ suy thận",
            "Lithium: naproxen tăng nồng độ lithium",
            "Methotrexate: naproxen tăng độc tính methotrexate",
            "Corticosteroid: tăng nguy cơ loét dạ dày"
        ],
        "pregnancy": "D - Chống chỉ định trong tam cá nguyệt thứ ba",
        "mechanism_of_action": "Esomeprazole: ức chế bơm proton H+/K+ ATPase, giảm tiết acid dạ dày, phòng ngừa loét do NSAID. Naproxen: NSAID, ức chế COX-1 và COX-2, giảm đau và viêm. Kết hợp giúp điều trị đau và phòng ngừa loét dạ dày đồng thời.",
        "monitoring": [
            "Triệu chứng đau và viêm",
            "Dấu hiệu loét dạ dày tá tràng (đau bụng, nôn ra máu, phân đen)",
            "Huyết áp (naproxen có thể tăng huyết áp)",
            "Chức năng thận (creatinine, eGFR) - đặc biệt quan trọng",
            "Chức năng gan (ALT, AST)",
            "Công thức máu (CBC) - theo dõi thiếu máu do chảy máu",
            "Dấu hiệu tim mạch (đau ngực, khó thở)"
        ],
        "precautions": [
            "CHỐNG CHỈ ĐỊNH trong tam cá nguyệt thứ ba của thai kỳ",
            "Nguy cơ tim mạch (nhồi máu cơ tim, đột quỵ) - không dùng ở bệnh nhân có bệnh tim mạch",
            "Nguy cơ suy thận cấp - theo dõi creatinine chặt chẽ",
            "Nguy cơ loét dạ dày tá tràng vẫn còn (mặc dù có PPI)",
            "Uống ít nhất 30 phút trước bữa ăn",
            "Nuốt nguyên viên, không nhai hoặc nghiền",
            "Dùng liều thấp nhất có hiệu quả và trong thời gian ngắn nhất"
        ],
        "pharmacokinetics": {
            "half_life": "Esomeprazole: 1-1.5 giờ; Naproxen: 12-17 giờ",
            "onset": "Esomeprazole: 1-3 ngày; Naproxen: 30 phút - 1 giờ",
            "duration": "Esomeprazole: 24 giờ; Naproxen: 8-12 giờ",
            "protein_binding": "Esomeprazole: 97%; Naproxen: 99%",
            "metabolism": "Esomeprazole: gan (CYP2C19, CYP3A4); Naproxen: gan (glucuronidation)",
            "clearance": "Esomeprazole: gan; Naproxen: thận (95%)"
        },
        "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm, tránh ánh sáng",
        "black_box_warnings": "Nguy cơ tim mạch nghiêm trọng (nhồi máu cơ tim, đột quỵ), có thể tử vong. Nguy cơ tăng ở bệnh nhân có bệnh tim mạch hoặc các yếu tố nguy cơ tim mạch. Nguy cơ loét dạ dày tá tràng, chảy máu, thủng, có thể tử vong. Nguy cơ suy thận cấp. CHỐNG CHỈ ĐỊNH trong tam cá nguyệt thứ ba của thai kỳ.",
        "drug_interactions": {
            "major": [
                {
                    "drug": "Warfarin",
                    "mechanism": "Naproxen tăng nguy cơ chảy máu, có thể tăng INR",
                    "effect": "Tăng nguy cơ chảy máu nghiêm trọng",
                    "management": "Tránh dùng cùng hoặc thận trọng. Theo dõi INR chặt chẽ."
                },
                {
                    "drug": "Aspirin",
                    "mechanism": "Tăng nguy cơ loét dạ dày tá tràng",
                    "effect": "Tăng nguy cơ loét và chảy máu",
                    "management": "Tránh dùng cùng."
                },
                {
                    "drug": "ACE inhibitors, ARBs",
                    "mechanism": "Naproxen giảm hiệu quả ACE/ARB, tăng nguy cơ suy thận",
                    "effect": "Giảm kiểm soát huyết áp, tăng nguy cơ suy thận",
                    "management": "Thận trọng. Theo dõi creatinine và huyết áp chặt chẽ."
                }
            ],
            "moderate": [
                {
                    "drug": "Lithium",
                    "mechanism": "Naproxen giảm thải trừ lithium",
                    "effect": "Tăng nồng độ lithium, tăng độc tính",
                    "management": "Theo dõi nồng độ lithium, điều chỉnh liều lithium."
                },
                {
                    "drug": "Methotrexate",
                    "mechanism": "Naproxen giảm thải trừ methotrexate",
                    "effect": "Tăng độc tính methotrexate",
                    "management": "Thận trọng. Theo dõi độc tính methotrexate."
                }
            ],
            "minor": []
        },
        "contraindications_detail": {
            "tuyệt_đối": [
                "Dị ứng esomeprazole, naproxen, hoặc NSAID khác",
                "Loét dạ dày tá tràng đang hoạt động",
                "Suy tim nặng (NYHA class IV)",
                "Suy thận nặng (CrCl <30 ml/phút) - CHỐNG CHỈ ĐỊNH",
                "Suy gan nặng - CHỐNG CHỈ ĐỊNH",
                "Tam cá nguyệt thứ ba của thai kỳ - CHỐNG CHỈ ĐỊNH",
                "Trẻ em <18 tuổi"
            ],
            "tương_đối": [
                "Bệnh tim mạch - nguy cơ tim mạch tăng",
                "Suy thận trung bình (CrCl 30-60) - thận trọng",
                "Tiền sử loét dạ dày tá tràng - nguy cơ tái phát",
                "Người già - tăng nguy cơ tác dụng phụ"
            ]
        },
        "pregnancy_lactation": {
            "fda_category": "D",
            "pregnancy_details": "CHỐNG CHỈ ĐỊNH trong tam cá nguyệt thứ ba của thai kỳ. Naproxen có thể gây đóng ống động mạch sớm và các biến chứng khác.",
            "lactation": {
                "safety": "Caution",
                "details": "Naproxen bài tiết vào sữa mẹ. Thận trọng khi cho con bú.",
                "recommendation": "Thận trọng khi cho con bú. Cân nhắc ngừng cho con bú hoặc ngừng thuốc."
            }
        },
        "hepatic_adjustment": {
            "mild": "Thận trọng",
            "moderate": "Thận trọng, có thể cần giảm liều",
            "severe": "CHỐNG CHỈ ĐỊNH",
            "notes": "Cả esomeprazole và naproxen đều chuyển hóa ở gan. Suy gan làm giảm chuyển hóa, tăng nguy cơ độc tính."
        },
        "overdose_management": {
            "symptoms": [
                "Buồn nôn, nôn",
                "Đau bụng",
                "Chóng mặt, nhức đầu",
                "Hạ huyết áp",
                "Suy thận cấp",
                "Loạn nhịp tim"
            ],
            "antidote": "Không có antidote đặc hiệu",
            "treatment": [
                "Rửa dạ dày nếu uống trong vòng 1-2 giờ",
                "Than hoạt tính",
                "Hỗ trợ triệu chứng",
                "Điều trị hạ huyết áp: bù dịch, vasopressor nếu cần",
                "Lọc máu nếu suy thận cấp nặng"
            ],
            "monitoring": "Theo dõi dấu hiệu sinh tồn, creatinine, chức năng gan, ECG"
        },
        "reversal_agents": {
            "available": False,
            "agents": []
        },
        "administration_instructions": {
            "oral": {
                "with_food": "Uống ít nhất 30 phút trước bữa ăn",
                "timing": "Uống 2 lần/ngày (sáng và tối), ít nhất 30 phút trước bữa ăn. Nuốt nguyên viên, không nhai hoặc nghiền."
            }
        },
        "risk_flags": {
            "high_alert": True,
            "narrow_therapeutic_index": False,
            "bleeding_risk": True,
            "organ_toxicity": ["renal", "hepatic", "cardiovascular", "gastrointestinal"],
            "qt_prolongation": False,
            "hepatotoxicity": True,
            "nephrotoxicity": True,
            "requires_monitoring": ["Blood pressure", "Creatinine", "LFT", "CBC", "Cardiovascular symptoms"]
        },
        "guideline_tags": [
            "FDA Black Box Warning - Cardiovascular risk, GI bleeding risk",
            "ACG Guidelines - NSAID-induced GI injury",
            "FDA Drug Information"
        ],
        "references": {
            "primary_sources": [
                "FDA Drug Label - Esomeprazole/Naproxen (Vimovo)",
                "UpToDate - NSAID-induced gastrointestinal injury",
                "ACG Guidelines"
            ],
            "last_updated": "2025-01-15",
            "evidence_level": "High - FDA approved, multiple RCTs, black box warnings"
        }
    },
    
    "Omeprazole/Domperidone": {
        "group": "Gastrointestinal - PPI + Prokinetic (Fixed-Dose Combination)",
        "vietnamese_name": "Omeprazole/Domperidone, Omez-D",
        "administration": ["PO"],
        "indications": [
            "Trào ngược dạ dày-thực quản (GERD) với rối loạn nhu động",
            "Khó tiêu, đầy hơi, buồn nôn kèm tăng acid",
            "Liệt dạ dày (gastroparesis) với tăng acid"
        ],
        "contraindications": [
            "Dị ứng omeprazole hoặc domperidone",
            "Chảy máu dạ dày",
            "Tắc ruột cơ học",
            "Prolactinoma",
            "QT kéo dài",
            "Dùng với các thuốc QT kéo dài",
            "Suy gan nặng"
        ],
        "dosage": {
            "adult_po": "Omeprazole 20mg/Domperidone 10mg PO x 2-3 lần/ngày, trước bữa ăn",
            "adult_typical": "Omeprazole 20mg/Domperidone 10mg PO x 2 lần/ngày (sáng và tối), trước bữa ăn",
            "adult_max": "Omeprazole 40mg/Domperidone 30mg/ngày",
            "notes": "Uống 15-30 phút trước bữa ăn. Nuốt nguyên viên omeprazole (enteric-coated). Không vượt quá 80mg domperidone/ngày."
        },
        "renal_adjustment": {
            "normal": "Không cần chỉnh liều",
            "30_60": "Thận trọng, có thể giảm liều domperidone",
            "under_30": "Giảm liều domperidone 50%",
            "notes": "Omeprazole chủ yếu chuyển hóa qua gan. Domperidone thải trừ qua thận một phần, cần giảm liều ở suy thận."
        },
        "side_effects": [
            "Nhức đầu",
            "Buồn nôn",
            "Tiêu chảy",
            "Táo bón",
            "Rối loạn kinh nguyệt (do domperidone)",
            "Tăng prolactin (do domperidone)",
            "Chảy sữa (galactorrhea)",
            "QT kéo dài (domperidone, liều cao)",
            "Thiếu Vitamin B12 (omeprazole, dùng lâu dài)",
            "Thiếu Magie (omeprazole, dùng lâu dài)"
        ],
        "interactions": [
            "Clopidogrel: omeprazole giảm hiệu quả clopidogrel",
            "Ketoconazole, Itraconazole: omeprazole giảm hấp thu",
            "Thuốc QT kéo dài: domperidone tăng nguy cơ loạn nhịp",
            "CYP3A4 inhibitors: tăng nồng độ domperidone"
        ],
        "pregnancy": "C - Thận trọng trong thai kỳ",
        "mechanism_of_action": "Omeprazole: ức chế bơm proton H+/K+ ATPase, giảm tiết acid dạ dày. Domperidone: dopamine D2 receptor antagonist ở ngoại vi, tăng nhu động dạ dày và ruột, tăng trương lực cơ thắt dưới thực quản, giảm buồn nôn. Kết hợp giúp điều trị GERD với rối loạn nhu động và buồn nôn.",
        "monitoring": [
            "Triệu chứng GERD: giảm ợ nóng, đầy hơi, buồn nôn",
            "ECG (QT kéo dài - nếu dùng domperidone liều cao)",
            "Dấu hiệu tăng prolactin: rối loạn kinh nguyệt, chảy sữa",
            "Magie máu (nếu dùng omeprazole lâu dài)",
            "Vitamin B12 (nếu dùng omeprazole >3 năm)"
        ],
        "precautions": [
            "Uống 15-30 phút trước bữa ăn",
            "Nuốt nguyên viên omeprazole (enteric-coated), không nhai",
            "Không vượt quá 80mg domperidone/ngày (tăng nguy cơ QT kéo dài)",
            "Tránh dùng domperidone với các thuốc QT kéo dài",
            "Thận trọng ở suy thận - giảm liều domperidone",
            "Theo dõi dấu hiệu tăng prolactin"
        ],
        "pharmacokinetics": {
            "half_life": "Omeprazole: 0.5-1 giờ; Domperidone: 7-9 giờ",
            "onset": "Omeprazole: 1-3 ngày; Domperidone: 30 phút - 1 giờ",
            "duration": "Omeprazole: 24 giờ; Domperidone: 4-6 giờ",
            "protein_binding": "Omeprazole: 95%; Domperidone: 91-93%",
            "metabolism": "Omeprazole: gan (CYP2C19, CYP3A4); Domperidone: gan (CYP3A4)",
            "clearance": "Omeprazole: gan; Domperidone: gan và thận"
        },
        "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm, tránh ánh sáng",
        "black_box_warnings": "Domperidone: Nguy cơ QT kéo dài, có thể gây loạn nhịp tim nghiêm trọng. Không vượt quá 80mg/ngày. Omeprazole: Có thể tăng nguy cơ gãy xương khi dùng lâu dài. Nguy cơ nhiễm C. difficile tăng.",
        "drug_interactions": {
            "major": [
                {
                    "drug": "Clopidogrel",
                    "mechanism": "Omeprazole ức chế CYP2C19, giảm chuyển hóa clopidogrel thành dạng hoạt động",
                    "effect": "Giảm hiệu quả chống kết tập tiểu cầu của clopidogrel",
                    "management": "TRÁNH DÙNG CÙNG. Chuyển sang pantoprazole hoặc H2 blocker nếu cần PPI."
                },
                {
                    "drug": "Thuốc QT kéo dài (amiodarone, quinolone, macrolide)",
                    "mechanism": "Domperidone tăng nguy cơ QT kéo dài",
                    "effect": "Tăng nguy cơ loạn nhịp tim nghiêm trọng",
                    "management": "TRÁNH DÙNG CÙNG domperidone."
                }
            ],
            "moderate": [
                {
                    "drug": "Ketoconazole, Itraconazole",
                    "mechanism": "Omeprazole giảm hấp thu azole antifungals; CYP3A4 inhibitors tăng nồng độ domperidone",
                    "effect": "Giảm hiệu quả azole; tăng nguy cơ QT kéo dài do domperidone",
                    "management": "Cách thời gian ít nhất 2 giờ. Thận trọng với domperidone."
                }
            ],
            "minor": []
        },
        "contraindications_detail": {
            "tuyệt_đối": [
                "Dị ứng omeprazole hoặc domperidone",
                "Chảy máu dạ dày",
                "Tắc ruột cơ học",
                "Prolactinoma",
                "QT kéo dài",
                "Dùng với các thuốc QT kéo dài"
            ],
            "tương_đối": [
                "Suy thận trung bình - giảm liều domperidone",
                "Suy gan nặng - thận trọng",
                "Người già - thận trọng"
            ]
        },
        "pregnancy_lactation": {
            "fda_category": "C",
            "pregnancy_details": "Thận trọng trong thai kỳ. Chỉ dùng khi lợi ích > nguy cơ.",
            "lactation": {
                "safety": "Caution",
                "details": "Domperidone có thể tăng tiết sữa nhưng cũng bài tiết vào sữa mẹ. Omeprazole bài tiết vào sữa mẹ ở nồng độ thấp.",
                "recommendation": "Thận trọng khi cho con bú."
            }
        },
        "hepatic_adjustment": {
            "mild": "Không cần chỉnh liều",
            "moderate": "Thận trọng",
            "severe": "Thận trọng, có thể cần giảm liều",
            "notes": "Cả omeprazole và domperidone đều chuyển hóa ở gan. Suy gan làm giảm chuyển hóa."
        },
        "overdose_management": {
            "symptoms": [
                "QT kéo dài, loạn nhịp tim (domperidone)",
                "Nhức đầu, chóng mặt",
                "Buồn nôn, nôn",
                "Rối loạn kinh nguyệt, chảy sữa"
            ],
            "antidote": "Không có antidote đặc hiệu",
            "treatment": [
                "Ngừng thuốc",
                "Theo dõi ECG (QT interval)",
                "Điều trị torsades de pointes nếu có: magnesium sulfate 2g IV",
                "Hỗ trợ triệu chứng"
            ],
            "monitoring": "ECG, dấu hiệu sinh tồn, triệu chứng"
        },
        "reversal_agents": {
            "available": False,
            "agents": []
        },
        "administration_instructions": {
            "oral": {
                "with_food": "Uống 15-30 phút trước bữa ăn",
                "timing": "Uống 2-3 lần/ngày, 15-30 phút trước bữa ăn. Nuốt nguyên viên omeprazole (enteric-coated), không nhai."
            }
        },
        "risk_flags": {
            "high_alert": False,
            "narrow_therapeutic_index": False,
            "bleeding_risk": False,
            "organ_toxicity": [],
            "qt_prolongation": True,
            "hepatotoxicity": False,
            "nephrotoxicity": False,
            "requires_monitoring": ["ECG (if domperidone high dose)", "Prolactin"]
        },
        "guideline_tags": [
            "ACG 2017 GERD Guidelines",
            "FDA Drug Information"
        ],
        "references": {
            "primary_sources": [
                "UpToDate - GERD treatment",
                "ACG 2017 GERD Guidelines",
                "FDA Drug Information"
            ],
            "last_updated": "2025-01-15",
            "evidence_level": "Moderate - Common combination, clinical practice"
        }
    },
    
    "Aluminum hydroxide/Magnesium hydroxide/Simethicone": {
        "group": "Gastrointestinal - Antacid + Antiflatulent (Fixed-Dose Combination)",
        "vietnamese_name": "Aluminum hydroxide/Magnesium hydroxide/Simethicone, Maalox Plus, Mylanta",
        "administration": ["PO"],
        "indications": [
            "Đau rát thượng vị, ợ chua, khó tiêu do tăng acid dạ dày",
            "Đầy hơi, chướng bụng kèm tăng acid",
            "Viêm dạ dày, loét dạ dày-tá tràng (giảm triệu chứng)"
        ],
        "contraindications": [
            "Suy thận nặng (CrCl <30 ml/phút) - nguy cơ tích tụ nhôm và magiê",
            "Giảm phospho máu nặng",
            "Tắc ruột cơ học"
        ],
        "dosage": {
            "adult_po": "10-20ml hỗn dịch hoặc 2-4 viên nhai PO sau bữa ăn và khi có triệu chứng, tối đa 4 lần/ngày",
            "adult_typical": "10-15ml PO sau bữa ăn và trước khi ngủ",
            "notes": "Lắc kỹ hỗn dịch trước khi dùng. Không dùng kéo dài >2 tuần liên tục nếu không được bác sĩ đánh giá. Uống cách xa thuốc khác ít nhất 2 giờ."
        },
        "renal_adjustment": {
            "normal": "Không đổi nhưng tránh dùng liều cao kéo dài",
            "30_60": "Giảm số lần dùng, tránh dùng kéo dài",
            "under_30": "CHỐNG CHỈ ĐỊNH",
            "dialysis": "CHỐNG CHỈ ĐỊNH",
            "notes": "Nhôm và magiê tích tụ ở suy thận, có thể gây độc tính thần kinh và loạn nhịp tim."
        },
        "side_effects": [
            "Táo bón (nhôm)",
            "Tiêu chảy (magiê) - phối hợp giúp cân bằng",
            "Buồn nôn, đầy hơi",
            "Tăng magiê máu, tăng nhôm máu ở suy thận (nguy hiểm)",
            "Giảm phospho máu nếu dùng kéo dài"
        ],
        "interactions": [
            "Fluoroquinolones, tetracyclines: giảm hấp thu do tạo phức chelat",
            "Levothyroxine, digoxin, sắt: giảm hấp thu",
            "Bisphosphonates: giảm hấp thu mạnh"
        ],
        "pregnancy": "B - Thường an toàn nếu dùng ngắn hạn, liều thấp",
        "mechanism_of_action": "Aluminum hydroxide/Magnesium hydroxide: antacid, trung hòa acid dạ dày tại chỗ, làm tăng pH dạ dày. Simethicone: antiflatulent, giảm sức căng bề mặt của các bọt khí trong đường tiêu hóa, làm vỡ bọt khí và giảm đầy hơi. Kết hợp giúp điều trị cả tăng acid và đầy hơi.",
        "monitoring": [
            "Triệu chứng lâm sàng: giảm đau rát, ợ chua, đầy hơi",
            "Ở bệnh nhân suy thận: theo dõi creatinin, magiê, phospho nếu dùng > vài ngày"
        ],
        "precautions": [
            "CHỐNG CHỈ ĐỊNH ở suy thận nặng",
            "Không dùng thay thế PPI/H2 trong loét dạ dày nặng hoặc GERD có biến chứng",
            "Uống cách xa PPI/H2 và các thuốc uống khác ít nhất 2 giờ",
            "Không dùng kéo dài ở bệnh nhân suy thận hoặc người cao tuổi",
            "Lắc kỹ hỗn dịch trước khi dùng"
        ],
        "pharmacokinetics": {
            "half_life": "Không áp dụng (tác dụng tại chỗ, hầu như không hấp thu)",
            "onset": "Vài phút sau uống",
            "duration": "1-3 giờ (antacid), vài giờ (simethicone)",
            "protein_binding": "Không áp dụng",
            "clearance": "Thải qua phân; một phần nhỏ ion nhôm/magiê hấp thu được thải qua thận"
        },
        "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm; lắc kỹ hỗn dịch trước khi dùng",
        "black_box_warnings": "CHỐNG CHỈ ĐỊNH ở suy thận nặng (CrCl <30 ml/phút). Tăng magiê và nhôm máu có thể gây độc tính thần kinh và loạn nhịp tim, có thể tử vong.",
        "drug_interactions": {
            "major": [],
            "moderate": [
                {
                    "drug": "Fluoroquinolones, tetracyclines, bisphosphonates, levothyroxine, sắt",
                    "mechanism": "Tạo phức hoặc thay đổi pH → giảm hấp thu đường uống",
                    "effect": "Giảm hiệu quả điều trị",
                    "management": "Dùng thuốc kia ít nhất 2 giờ trước hoặc 4 giờ sau antacid."
                }
            ],
            "minor": []
        },
        "contraindications_detail": {
            "tuyệt_đối": [
                "Suy thận nặng (CrCl <30 ml/phút) - CHỐNG CHỈ ĐỊNH",
                "Tắc ruột cơ học",
                "Giảm phospho máu nặng"
            ],
            "tương_đối": [
                "Suy thận trung bình",
                "Người già dùng kéo dài"
            ]
        },
        "pregnancy_lactation": {
            "fda_category": "B",
            "pregnancy_details": "Thường an toàn nếu dùng ngắn hạn, liều thấp cho triệu chứng ợ chua trong thai kỳ.",
            "lactation": {
                "safety": "Compatible",
                "details": "Không hấp thu đáng kể; ít vào sữa mẹ.",
                "recommendation": "Có thể dùng, tránh lạm dụng kéo dài."
            }
        },
        "hepatic_adjustment": {
            "mild": "Không đổi",
            "moderate": "Không đổi",
            "severe": "Không đổi",
            "notes": "Không chuyển hóa qua gan; suy gan không ảnh hưởng nhiều."
        },
        "overdose_management": {
            "symptoms": [
                "Tiêu chảy hoặc táo bón nặng",
                "Tăng magiê máu (yếu cơ, tụt huyết áp, loạn nhịp) ở suy thận",
                "Tăng nhôm máu, bệnh não (nhầm lẫn, yếu cơ) ở suy thận"
            ],
            "antidote": "Calcium gluconate IV (đối kháng magie)",
            "treatment": [
                "Ngừng thuốc, bù dịch, điều chỉnh điện giải",
                "Calcium gluconate 1-3g IV chậm nếu tăng magie máu nặng",
                "Lọc máu nếu tăng magiê/nhôm máu nặng ở suy thận"
            ],
            "monitoring": "Điện giải, magiê, phospho, chức năng thận, triệu chứng thần kinh"
        },
        "reversal_agents": {
            "available": True,
            "agents": [
                {
                    "agent": "Calcium gluconate hoặc calcium chloride IV",
                    "dose": "1-3g IV chậm",
                    "mechanism": "Đối kháng tác dụng của magie",
                    "notes": "Điều trị tăng magie máu nặng"
                }
            ]
        },
        "administration_instructions": {
            "oral": {
                "with_food": "Dùng sau bữa ăn hoặc khi có triệu chứng; uống với nước",
                "timing": "Dùng sau bữa ăn 1-3 giờ và/hoặc trước ngủ nếu cần; cách xa thuốc khác ≥2 giờ. Lắc kỹ hỗn dịch trước khi dùng."
            }
        },
        "risk_flags": {
            "high_alert": True,
            "narrow_therapeutic_index": False,
            "bleeding_risk": False,
            "organ_toxicity": ["renal", "neurological"],
            "qt_prolongation": False,
            "hepatotoxicity": False,
            "nephrotoxicity": True,
            "requires_monitoring": ["Magnesium (if renal impairment)", "Aluminum (if renal impairment)"]
        },
        "guideline_tags": [
            "ACG 2017 GERD Guidelines",
            "FDA - Over-the-counter antacids"
        ],
        "references": {
            "primary_sources": [
                "UpToDate - Antacids: pharmacology and use",
                "Goodman & Gilman's - Antacids",
                "FDA Drug Information"
            ],
            "last_updated": "2025-01-15",
            "evidence_level": "High - Extensive clinical experience, OTC medication"
        }
    },
    
    "Alginate/Sodium bicarbonate/Calcium carbonate": {
        "group": "Gastrointestinal - Alginate + Antacid (Fixed-Dose Combination)",
        "vietnamese_name": "Alginate/Sodium bicarbonate/Calcium carbonate, Gaviscon, Gaviscon Double Action",
        "administration": ["PO"],
        "indications": [
            "Trào ngược dạ dày-thực quản (GERD)",
            "Ợ nóng, ợ chua",
            "Viêm thực quản do trào ngược"
        ],
        "contraindications": [
            "Dị ứng alginate hoặc các thành phần khác",
            "Suy thận nặng (nếu chứa natri cao)",
            "Tăng calci máu",
            "Suy tim nặng (nếu chứa natri cao)"
        ],
        "dosage": {
            "adult_po": "10-20ml hỗn dịch hoặc 2-4 viên nhai PO sau bữa ăn và trước khi ngủ",
            "adult_typical": "10-15ml PO sau bữa ăn và trước khi ngủ",
            "adult_max": "4 lần/ngày",
            "notes": "Nhai kỹ viên trước khi nuốt. Lắc kỹ hỗn dịch trước khi dùng. Tạo lớp bảo vệ trên dạ dày, ngăn trào ngược."
        },
        "renal_adjustment": {
            "normal": "Không cần chỉnh liều",
            "30_60": "Thận trọng nếu chứa natri cao",
            "under_30": "Thận trọng nếu chứa natri cao",
            "notes": "Một số chế phẩm chứa natri cao, cần thận trọng ở suy thận và suy tim."
        },
        "side_effects": [
            "Táo bón (calcium carbonate)",
            "Đầy hơi",
            "Buồn nôn",
            "Tăng calci máu (nếu dùng liều cao kéo dài)",
            "Giữ nước (nếu chứa natri cao)"
        ],
        "interactions": [
            "Các thuốc khác: có thể giảm hấp thu do tạo lớp bảo vệ",
            "Cách xa các thuốc khác 2 giờ"
        ],
        "pregnancy": "B - Thường an toàn trong thai kỳ",
        "mechanism_of_action": "Alginate: phản ứng với acid dạ dày tạo thành gel dày, nổi trên bề mặt dịch dạ dày, tạo lớp bảo vệ vật lý ngăn trào ngược acid vào thực quản. Sodium bicarbonate/Calcium carbonate: antacid, trung hòa acid dạ dày. Kết hợp tạo hàng rào vật lý và trung hòa acid đồng thời.",
        "monitoring": [
            "Triệu chứng GERD: giảm ợ nóng, ợ chua",
            "Dấu hiệu táo bón",
            "Calci máu (nếu dùng liều cao kéo dài)",
            "Huyết áp, phù (nếu chứa natri cao)"
        ],
        "precautions": [
            "Uống sau bữa ăn và trước khi ngủ",
            "Nhai kỹ viên trước khi nuốt",
            "Cách xa các thuốc khác 2 giờ (có thể giảm hấp thu)",
            "Thận trọng ở suy thận và suy tim nếu chứa natri cao",
            "Lắc kỹ hỗn dịch trước khi dùng"
        ],
        "pharmacokinetics": {
            "half_life": "Không áp dụng (tác dụng tại chỗ)",
            "onset": "Vài phút",
            "duration": "2-4 giờ",
            "protein_binding": "Không áp dụng",
            "clearance": "Thải qua phân (không hấp thu đáng kể)"
        },
        "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm. Lắc kỹ hỗn dịch trước khi dùng.",
        "black_box_warnings": None,
        "drug_interactions": {
            "major": [],
            "moderate": [
                {
                    "drug": "Các thuốc khác",
                    "mechanism": "Alginate và antacid tạo lớp bảo vệ, có thể giảm hấp thu thuốc",
                    "effect": "Giảm hấp thu thuốc, giảm hiệu quả",
                    "management": "Cách xa các thuốc khác ít nhất 2 giờ."
                }
            ],
            "minor": []
        },
        "contraindications_detail": {
            "tuyệt_đối": [
                "Dị ứng alginate hoặc các thành phần khác",
                "Tăng calci máu"
            ],
            "tương_đối": [
                "Suy thận nặng (nếu chứa natri cao) - thận trọng",
                "Suy tim nặng (nếu chứa natri cao) - thận trọng"
            ]
        },
        "pregnancy_lactation": {
            "fda_category": "B",
            "pregnancy_details": "Thường an toàn trong thai kỳ. Ít hấp thu toàn thân.",
            "lactation": {
                "safety": "Compatible",
                "details": "Alginate và antacid không hấp thu đáng kể, không vào sữa mẹ.",
                "recommendation": "Có thể dùng khi cho con bú."
            }
        },
        "hepatic_adjustment": {
            "mild": "Không cần chỉnh liều",
            "moderate": "Không cần chỉnh liều",
            "severe": "Không cần chỉnh liều",
            "notes": "Tác dụng tại chỗ ở dạ dày, không phụ thuộc chuyển hóa gan."
        },
        "overdose_management": {
            "symptoms": [
                "Táo bón",
                "Đầy hơi",
                "Tăng calci máu (nếu dùng liều cao kéo dài)"
            ],
            "antidote": "Không có antidote đặc hiệu",
            "treatment": [
                "Ngừng thuốc",
                "Hỗ trợ triệu chứng"
            ],
            "monitoring": "Theo dõi triệu chứng, calci máu nếu cần"
        },
        "reversal_agents": {
            "available": False,
            "agents": []
        },
        "administration_instructions": {
            "oral": {
                "with_food": "Uống sau bữa ăn và trước khi ngủ",
                "timing": "Uống sau bữa ăn và trước khi ngủ. Nhai kỹ viên trước khi nuốt. Lắc kỹ hỗn dịch trước khi dùng."
            }
        },
        "risk_flags": {
            "high_alert": False,
            "narrow_therapeutic_index": False,
            "bleeding_risk": False,
            "organ_toxicity": [],
            "qt_prolongation": False,
            "hepatotoxicity": False,
            "nephrotoxicity": False,
            "requires_monitoring": []
        },
        "guideline_tags": [
            "ACG 2017 GERD Guidelines",
            "FDA Drug Information"
        ],
        "references": {
            "primary_sources": [
                "UpToDate - Alginate: Drug information",
                "ACG 2017 GERD Guidelines",
                "FDA Drug Information"
            ],
            "last_updated": "2025-01-15",
            "evidence_level": "High - Guideline-recommended for GERD, OTC medication"
        }
    },
    
    "Loperamide/Simethicone": {
        "group": "Gastrointestinal - Antidiarrheal + Antiflatulent (Fixed-Dose Combination)",
        "vietnamese_name": "Loperamide/Simethicone, Imodium Advanced",
        "administration": ["PO"],
        "indications": [
            "Tiêu chảy cấp kèm đầy hơi, chướng bụng",
            "Tiêu chảy du lịch (traveler's diarrhea) kèm đầy hơi"
        ],
        "contraindications": [
            "Tiêu chảy do nhiễm khuẩn nặng",
            "Viêm đại tràng giả mạc",
            "Tắc ruột cơ học",
            "Trẻ em <2 tuổi",
            "Dị ứng loperamide hoặc simethicone"
        ],
        "dosage": {
            "adult_po": "Loperamide 2mg/Simethicone 125mg PO sau mỗi lần đi ngoài, tối đa 8 viên/ngày (16mg loperamide/1000mg simethicone)",
            "adult_initial": "2 viên PO ngay khi có tiêu chảy, sau đó 1 viên sau mỗi lần đi ngoài",
            "adult_max": "8 viên/ngày",
            "notes": "Không dùng quá 48 giờ nếu không cải thiện. Loperamide giảm tiêu chảy, simethicone giảm đầy hơi."
        },
        "renal_adjustment": {
            "normal": "Không cần chỉnh liều",
            "30_60": "Thận trọng với loperamide, có thể giảm liều",
            "under_30": "Giảm liều loperamide hoặc tránh dùng",
            "notes": "Loperamide thải trừ qua thận một phần. Simethicone không hấp thu."
        },
        "side_effects": [
            "Táo bón (loperamide)",
            "Buồn nôn",
            "Đau bụng",
            "Buồn ngủ",
            "Ức chế hô hấp (loperamide, liều cao)"
        ],
        "interactions": [
            "Opioids: loperamide tăng tác dụng",
            "CYP3A4 inhibitors: tăng nồng độ loperamide"
        ],
        "pregnancy": "C - Thận trọng trong thai kỳ",
        "mechanism_of_action": "Loperamide: opioid mu-receptor agonist ở ruột, ức chế nhu động ruột, tăng hấp thu nước, giảm tiêu chảy. Simethicone: antiflatulent, giảm sức căng bề mặt của các bọt khí, làm vỡ bọt khí và giảm đầy hơi. Kết hợp giúp điều trị cả tiêu chảy và đầy hơi.",
        "monitoring": [
            "Đáp ứng lâm sàng: giảm tần suất đi ngoài, giảm đầy hơi",
            "Dấu hiệu quá liều loperamide: ức chế hô hấp, giảm ý thức",
            "Dấu hiệu táo bón nặng",
            "Dấu hiệu nhiễm khuẩn (nếu giữ vi khuẩn trong ruột quá lâu)"
        ],
        "precautions": [
            "Chỉ dùng cho tiêu chảy không nhiễm khuẩn hoặc đã điều trị nhiễm khuẩn",
            "Không dùng quá 48 giờ nếu không cải thiện",
            "Không dùng cho tiêu chảy nhiễm khuẩn nặng",
            "Không dùng cho trẻ em <2 tuổi",
            "Không vượt quá 16mg loperamide/ngày"
        ],
        "pharmacokinetics": {
            "half_life": "Loperamide: 7-14 giờ; Simethicone: không áp dụng",
            "onset": "Loperamide: 1-2 giờ; Simethicone: vài phút",
            "duration": "Loperamide: 4-6 giờ; Simethicone: vài giờ",
            "protein_binding": "Loperamide: 97%; Simethicone: không áp dụng",
            "metabolism": "Loperamide: gan (CYP3A4, CYP2C8); Simethicone: không chuyển hóa",
            "clearance": "Loperamide: gan và thận; Simethicone: thải qua phân"
        },
        "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm, tránh ánh sáng",
        "black_box_warnings": "Loperamide: Liều cao có thể gây ức chế hô hấp nặng, có thể tử vong, đặc biệt ở trẻ em. Không dùng quá liều khuyến cáo (16mg/ngày). Không dùng cho trẻ em <2 tuổi.",
        "drug_interactions": {
            "major": [
                {
                    "drug": "Opioids (morphine, codeine, fentanyl)",
                    "mechanism": "Tác dụng hiệp đồng ức chế opioid mu-receptor",
                    "effect": "Tăng nguy cơ ức chế hô hấp, tăng tác dụng phụ opioid",
                    "management": "Tránh dùng cùng. Thận trọng nếu phải dùng cùng (giảm liều cả hai)."
                }
            ],
            "moderate": [
                {
                    "drug": "CYP3A4 inhibitors (ketoconazole, itraconazole, ritonavir, clarithromycin)",
                    "mechanism": "Ức chế chuyển hóa loperamide qua CYP3A4",
                    "effect": "Tăng nồng độ loperamide, tăng nguy cơ ức chế hô hấp",
                    "management": "Tránh dùng cùng hoặc giảm liều loperamide. Theo dõi dấu hiệu quá liều."
                }
            ],
            "minor": []
        },
        "contraindications_detail": {
            "tuyệt_đối": [
                "Tiêu chảy nhiễm khuẩn nặng (C. difficile, E. coli O157:H7)",
                "Viêm đại tràng giả mạc",
                "Tắc ruột cơ học",
                "Trẻ em <2 tuổi - CHỐNG CHỈ ĐỊNH",
                "Dị ứng loperamide hoặc simethicone"
            ],
            "tương_đối": [
                "Suy gan nặng - giảm liều loperamide",
                "Suy thận nặng - giảm liều loperamide",
                "Tiêu chảy nhiễm khuẩn nhẹ - thận trọng, đã điều trị kháng sinh"
            ]
        },
        "pregnancy_lactation": {
            "fda_category": "C",
            "pregnancy_details": "Loperamide là FDA category C. Thận trọng trong thai kỳ. Chỉ dùng khi lợi ích > nguy cơ.",
            "lactation": {
                "safety": "Compatible",
                "details": "Loperamide bài tiết vào sữa mẹ ở nồng độ thấp. Simethicone không hấp thu. An toàn khi cho con bú ở liều điều trị.",
                "recommendation": "Có thể dùng khi cho con bú."
            }
        },
        "hepatic_adjustment": {
            "mild": "Không cần chỉnh liều",
            "moderate": "Giảm liều loperamide 50%",
            "severe": "Giảm liều loperamide 50% hoặc tránh dùng",
            "notes": "Loperamide chuyển hóa ở gan. Suy gan làm giảm chuyển hóa, tăng nguy cơ tích lũy và ức chế hô hấp."
        },
        "overdose_management": {
            "symptoms": [
                "Ức chế hô hấp nặng (loperamide, triệu chứng chính)",
                "Giảm ý thức, hôn mê",
                "Co đồng tử (miosis)",
                "Táo bón nặng, tắc ruột"
            ],
            "antidote": "Naloxone (opioid antagonist) - có thể đảo ngược ức chế hô hấp",
            "treatment": [
                "Naloxone 0.4-2mg IV/IM/SC, lặp lại mỗi 2-3 phút nếu cần (tối đa 10mg)",
                "Hỗ trợ hô hấp: thông khí, oxy, nếu cần đặt nội khí quản",
                "Theo dõi dấu hiệu sinh tồn chặt chẽ",
                "Activated charcoal nếu uống trong vòng 1-2 giờ"
            ],
            "monitoring": "Theo dõi dấu hiệu sinh tồn (nhịp thở, SpO2, ý thức), dấu hiệu tắc ruột"
        },
        "reversal_agents": {
            "available": True,
            "agents": [
                {
                    "agent": "Naloxone",
                    "dose": "0.4-2mg IV/IM/SC, lặp lại mỗi 2-3 phút nếu cần (tối đa 10mg)",
                    "mechanism": "Opioid mu-receptor antagonist, đảo ngược ức chế hô hấp",
                    "notes": "Có thể đảo ngược ức chế hô hấp do quá liều loperamide"
                }
            ]
        },
        "administration_instructions": {
            "oral": {
                "with_food": "Có thể uống với hoặc không với thức ăn",
                "timing": "Liều đầu: 2 viên PO ngay khi có tiêu chảy. Sau đó: 1 viên sau mỗi lần đi ngoài (tối đa 8 viên/ngày). Không dùng quá 48 giờ nếu không cải thiện."
            }
        },
        "risk_flags": {
            "high_alert": True,
            "narrow_therapeutic_index": False,
            "bleeding_risk": False,
            "organ_toxicity": [],
            "qt_prolongation": False,
            "hepatotoxicity": False,
            "nephrotoxicity": False,
            "requires_monitoring": ["Respiratory status", "Bowel symptoms"]
        },
        "guideline_tags": [
            "WHO Guidelines - Diarrhea treatment",
            "FDA Drug Information",
            "FDA Black Box Warning"
        ],
        "references": {
            "primary_sources": [
                "FDA Drug Label - Loperamide/Simethicone",
                "UpToDate - Loperamide: Drug information",
                "WHO Guidelines - Diarrhea treatment"
            ],
            "last_updated": "2025-01-15",
            "evidence_level": "High - FDA approved, multiple RCTs, safety warnings"
        }
    },
    
    "Docusate/Senna": {
        "group": "Gastrointestinal - Stool Softener + Stimulant Laxative (Fixed-Dose Combination)",
        "vietnamese_name": "Docusate/Senna, Senokot-S, Pericolace",
        "administration": ["PO"],
        "indications": [
            "Táo bón cấp hoặc mạn tính",
            "Táo bón do opioid (kết hợp stool softener và stimulant)",
            "Chuẩn bị ruột trước phẫu thuật/nội soi"
        ],
        "contraindications": [
            "Tắc ruột cơ học",
            "Thủng ruột, viêm phúc mạc",
            "Viêm ruột cấp nặng",
            "Đau bụng cấp chưa rõ nguyên nhân",
            "Dị ứng docusate hoặc senna"
        ],
        "dosage": {
            "adult_po": "Docusate 50mg/Senna 8.6mg PO x 1-2 lần/ngày, thường vào buổi tối",
            "adult_opioid_constipation": "Docusate 50mg/Senna 8.6mg PO x 2 lần/ngày",
            "adult_max": "Docusate 200mg/Senna 34.4mg/ngày",
            "notes": "Uống buổi tối để đi ngoài buổi sáng hôm sau. Docusate làm mềm phân, senna kích thích nhu động. Kết hợp hiệu quả cho táo bón do opioid."
        },
        "renal_adjustment": {
            "normal": "Không cần chỉnh liều",
            "30_60": "Không cần chỉnh liều, nhưng tránh lạm dụng kéo dài",
            "under_30": "Thận trọng nếu dùng kéo dài (mất điện giải)",
            "notes": "Docusate ít hấp thu. Senna có thể gây mất điện giải nếu lạm dụng kéo dài."
        },
        "side_effects": [
            "Đau quặn bụng (senna)",
            "Tiêu chảy",
            "Buồn nôn",
            "Mất điện giải (giảm K+) nếu lạm dụng kéo dài",
            "Nước tiểu màu vàng-nâu (senna, vô hại)"
        ],
        "interactions": [
            "Digoxin: hạ K+ do senna làm tăng nhạy cảm với độc tính digoxin",
            "Thuốc lợi tiểu, corticosteroid: tăng nguy cơ hạ K+"
        ],
        "pregnancy": "C - Có thể dùng ngắn hạn khi cần thiết",
        "mechanism_of_action": "Docusate: stool softener, chất hoạt động bề mặt, làm giảm sức căng bề mặt của phân, cho phép nước và lipid thấm vào phân, làm mềm phân. Senna: stimulant laxative, chứa sennosides kích thích đám rối thần kinh ruột, tăng nhu động đại tràng. Kết hợp giúp làm mềm phân và kích thích nhu động đồng thời, hiệu quả cho táo bón do opioid.",
        "monitoring": [
            "Tần suất và tính chất phân",
            "Dấu hiệu mất nước, rối loạn điện giải nếu dùng kéo dài",
            "Dấu hiệu hạ K+ nếu dùng với digoxin hoặc thuốc lợi tiểu"
        ],
        "precautions": [
            "Chỉ dùng ngắn hạn (vài ngày); không dùng kéo dài hàng tuần-tháng",
            "Uống buổi tối để đi ngoài buổi sáng hôm sau",
            "Nếu táo bón kéo dài, cần tìm và xử lý nguyên nhân",
            "Thận trọng khi dùng với digoxin hoặc thuốc lợi tiểu (nguy cơ hạ K+)"
        ],
        "pharmacokinetics": {
            "half_life": "Docusate: không rõ; Senna: không rõ",
            "onset": "Docusate: 1-3 ngày; Senna: 6-12 giờ",
            "duration": "Một liều thường có tác dụng trong ngày",
            "protein_binding": "Không đáng kể",
            "clearance": "Thải qua phân và nước tiểu"
        },
        "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm",
        "black_box_warnings": "Lạm dụng kéo dài có thể gây lệ thuộc thuốc và rối loạn điện giải.",
        "drug_interactions": {
            "major": [],
            "moderate": [
                {
                    "drug": "Digoxin",
                    "mechanism": "Hạ K+ do senna làm tăng nhạy cảm với độc tính digoxin",
                    "effect": "Tăng nguy cơ loạn nhịp do digoxin",
                    "management": "Theo dõi K+ và ECG nếu dùng cùng."
                },
                {
                    "drug": "Thuốc lợi tiểu, corticosteroid",
                    "mechanism": "Cộng hưởng hạ K+",
                    "effect": "Tăng nguy cơ hạ K+ và biến chứng tim mạch",
                    "management": "Hạn chế dùng kéo dài; theo dõi điện giải."
                }
            ],
            "minor": []
        },
        "contraindications_detail": {
            "tuyệt_đối": [
                "Tắc ruột cơ học, thủng ruột, viêm phúc mạc",
                "Đau bụng cấp chưa rõ nguyên nhân"
            ],
            "tương_đối": [
                "Viêm ruột mạn tính nặng",
                "Suy thận (tránh lạm dụng kéo dài)"
            ]
        },
        "pregnancy_lactation": {
            "fda_category": "C",
            "pregnancy_details": "Có thể dùng ngắn hạn khi cần thiết; ưu tiên các biện pháp không dùng thuốc hoặc osmotic/bulk-forming trước.",
            "lactation": {
                "safety": "Compatible with caution",
                "details": "Một lượng nhỏ chất chuyển hóa có thể vào sữa; có báo cáo trẻ đi phân lỏng nhẹ.",
                "recommendation": "Có thể dùng ngắn hạn; theo dõi phân của trẻ."
            }
        },
        "hepatic_adjustment": {
            "mild": "Không cần chỉnh liều",
            "moderate": "Không cần chỉnh liều",
            "severe": "Không cần chỉnh liều",
            "notes": "Tác dụng chủ yếu tại đại tràng, không phụ thuộc chuyển hóa gan."
        },
        "overdose_management": {
            "symptoms": [
                "Tiêu chảy nhiều, mất nước, hạ K+",
                "Đau bụng quặn nhiều"
            ],
            "antidote": "Không có antidote đặc hiệu",
            "treatment": [
                "Ngừng thuốc",
                "Bù dịch và điện giải; điều chỉnh hạ K+",
                "Theo dõi ECG nếu có yếu tố nguy cơ"
            ],
            "monitoring": "Điện giải, chức năng thận, ECG nếu có yếu tố nguy cơ"
        },
        "reversal_agents": {
            "available": False,
            "agents": []
        },
        "administration_instructions": {
            "oral": {
                "with_food": "Có thể uống với hoặc không với thức ăn",
                "timing": "Uống buổi tối để đi ngoài buổi sáng hôm sau. Không dùng kéo dài."
            }
        },
        "risk_flags": {
            "high_alert": False,
            "narrow_therapeutic_index": False,
            "bleeding_risk": False,
            "organ_toxicity": [],
            "qt_prolongation": False,
            "hepatotoxicity": False,
            "nephrotoxicity": False,
            "requires_monitoring": ["Electrolytes (long-term use)"]
        },
        "guideline_tags": [
            "ACG 2013 Constipation Guidelines",
            "FDA - Laxative safety"
        ],
        "references": {
            "primary_sources": [
                "AGA guidelines - Management of chronic constipation and opioid-induced constipation",
                "UpToDate - Senna: Drug information",
                "ACG 2013 Constipation Guidelines"
            ],
            "last_updated": "2025-01-15",
            "evidence_level": "High - Guideline-recommended combination for opioid-induced constipation"
        }
    },
    
    "Pantoprazole/Domperidone": {
        "group": "Gastrointestinal - PPI + Prokinetic (Fixed-Dose Combination)",
        "vietnamese_name": "Pantoprazole/Domperidone",
        "administration": ["PO"],
        "indications": [
            "Trào ngược dạ dày-thực quản (GERD) với rối loạn nhu động",
            "Khó tiêu, đầy hơi, buồn nôn kèm tăng acid",
            "Liệt dạ dày (gastroparesis) với tăng acid"
        ],
        "contraindications": [
            "Dị ứng pantoprazole hoặc domperidone",
            "Chảy máu dạ dày",
            "Tắc ruột cơ học",
            "Prolactinoma",
            "QT kéo dài",
            "Dùng với các thuốc QT kéo dài"
        ],
        "dosage": {
            "adult_po": "Pantoprazole 40mg/Domperidone 10mg PO x 1-2 lần/ngày, trước bữa ăn",
            "adult_typical": "Pantoprazole 40mg/Domperidone 10mg PO x 1 lần/ngày (sáng), trước bữa ăn",
            "adult_max": "Pantoprazole 80mg/Domperidone 30mg/ngày",
            "notes": "Uống 15-30 phút trước bữa ăn. Nuốt nguyên viên pantoprazole (enteric-coated). Không vượt quá 80mg domperidone/ngày. Ưu điểm: pantoprazole ít tương tác CYP450 hơn omeprazole."
        },
        "renal_adjustment": {
            "normal": "Không cần chỉnh liều",
            "30_60": "Thận trọng, có thể giảm liều domperidone",
            "under_30": "Giảm liều domperidone 50%",
            "notes": "Pantoprazole chủ yếu chuyển hóa qua gan. Domperidone thải trừ qua thận một phần."
        },
        "side_effects": [
            "Nhức đầu",
            "Buồn nôn",
            "Tiêu chảy",
            "Rối loạn kinh nguyệt (do domperidone)",
            "Tăng prolactin (do domperidone)",
            "QT kéo dài (domperidone, liều cao)"
        ],
        "interactions": [
            "Clopidogrel: pantoprazole ít ảnh hưởng hơn omeprazole, nhưng vẫn thận trọng",
            "Ketoconazole, Itraconazole: pantoprazole giảm hấp thu",
            "Thuốc QT kéo dài: domperidone tăng nguy cơ loạn nhịp"
        ],
        "pregnancy": "C - Thận trọng trong thai kỳ",
        "mechanism_of_action": "Pantoprazole: ức chế bơm proton H+/K+ ATPase, giảm tiết acid dạ dày. Ưu điểm: ít tương tác CYP450 hơn omeprazole. Domperidone: dopamine D2 receptor antagonist ở ngoại vi, tăng nhu động dạ dày và ruột, giảm buồn nôn.",
        "monitoring": [
            "Triệu chứng GERD",
            "ECG (QT kéo dài - nếu dùng domperidone liều cao)",
            "Dấu hiệu tăng prolactin"
        ],
        "precautions": [
            "Uống 15-30 phút trước bữa ăn",
            "Nuốt nguyên viên pantoprazole (enteric-coated)",
            "Không vượt quá 80mg domperidone/ngày",
            "Ưu điểm: pantoprazole ít tương tác CYP450 hơn omeprazole, an toàn hơn với clopidogrel"
        ],
        "pharmacokinetics": {
            "half_life": "Pantoprazole: 1 giờ; Domperidone: 7-9 giờ",
            "onset": "Pantoprazole: 1-3 ngày; Domperidone: 30 phút - 1 giờ",
            "duration": "Pantoprazole: 24 giờ; Domperidone: 4-6 giờ",
            "protein_binding": "Pantoprazole: 98%; Domperidone: 91-93%",
            "metabolism": "Pantoprazole: gan (CYP2C19, CYP3A4 - ít ức chế hơn omeprazole); Domperidone: gan (CYP3A4)",
            "clearance": "Pantoprazole: gan; Domperidone: gan và thận"
        },
        "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm, tránh ánh sáng",
        "black_box_warnings": "Domperidone: Nguy cơ QT kéo dài. Không vượt quá 80mg/ngày.",
        "drug_interactions": {
            "major": [
                {
                    "drug": "Thuốc QT kéo dài (amiodarone, quinolone, macrolide)",
                    "mechanism": "Domperidone tăng nguy cơ QT kéo dài",
                    "effect": "Tăng nguy cơ loạn nhịp tim",
                    "management": "TRÁNH DÙNG CÙNG domperidone."
                }
            ],
            "moderate": [
                {
                    "drug": "Clopidogrel",
                    "mechanism": "Pantoprazole ít ảnh hưởng CYP2C19 hơn omeprazole",
                    "effect": "Ít ảnh hưởng đến clopidogrel hơn omeprazole",
                    "management": "Có thể dùng cùng, nhưng vẫn thận trọng."
                }
            ],
            "minor": []
        },
        "contraindications_detail": {
            "tuyệt_đối": [
                "Dị ứng pantoprazole hoặc domperidone",
                "Chảy máu dạ dày",
                "Tắc ruột cơ học",
                "Prolactinoma",
                "QT kéo dài"
            ],
            "tương_đối": [
                "Suy thận trung bình - giảm liều domperidone",
                "Suy gan nặng - thận trọng"
            ]
        },
        "pregnancy_lactation": {
            "fda_category": "C",
            "pregnancy_details": "Thận trọng trong thai kỳ.",
            "lactation": {
                "safety": "Caution",
                "details": "Domperidone có thể tăng tiết sữa nhưng cũng bài tiết vào sữa mẹ.",
                "recommendation": "Thận trọng khi cho con bú."
            }
        },
        "hepatic_adjustment": {
            "mild": "Không cần chỉnh liều",
            "moderate": "Thận trọng",
            "severe": "Thận trọng, có thể cần giảm liều",
            "notes": "Cả pantoprazole và domperidone đều chuyển hóa ở gan."
        },
        "overdose_management": {
            "symptoms": [
                "QT kéo dài, loạn nhịp tim (domperidone)",
                "Nhức đầu, chóng mặt"
            ],
            "antidote": "Không có antidote đặc hiệu",
            "treatment": [
                "Ngừng thuốc",
                "Theo dõi ECG",
                "Hỗ trợ triệu chứng"
            ],
            "monitoring": "ECG, dấu hiệu sinh tồn"
        },
        "reversal_agents": {
            "available": False,
            "agents": []
        },
        "administration_instructions": {
            "oral": {
                "with_food": "Uống 15-30 phút trước bữa ăn",
                "timing": "Uống 1-2 lần/ngày, 15-30 phút trước bữa ăn. Nuốt nguyên viên pantoprazole (enteric-coated)."
            }
        },
        "risk_flags": {
            "high_alert": False,
            "narrow_therapeutic_index": False,
            "bleeding_risk": False,
            "organ_toxicity": [],
            "qt_prolongation": True,
            "hepatotoxicity": False,
            "nephrotoxicity": False,
            "requires_monitoring": ["ECG (if domperidone high dose)"]
        },
        "guideline_tags": [
            "ACG 2017 GERD Guidelines",
            "FDA Drug Information"
        ],
        "references": {
            "primary_sources": [
                "UpToDate - GERD treatment",
                "ACG 2017 GERD Guidelines",
                "FDA Drug Information"
            ],
            "last_updated": "2025-01-15",
            "evidence_level": "Moderate - Common combination, clinical practice"
        }
    },
    
    "Omeprazole/Sodium bicarbonate": {
        "group": "Gastrointestinal - PPI + Antacid (Fixed-Dose Combination)",
        "vietnamese_name": "Omeprazole/Sodium bicarbonate, Zegerid",
        "administration": ["PO"],
        "indications": [
            "Loét dạ dày tá tràng",
            "GERD",
            "Diệt H. pylori (phối hợp kháng sinh)",
            "Khi cần tác dụng nhanh của PPI"
        ],
        "contraindications": [
            "Dị ứng omeprazole hoặc sodium bicarbonate",
            "Suy thận nặng (CrCl <30 ml/phút) - nguy cơ tăng natri máu",
            "Suy tim nặng (nguy cơ giữ nước do natri)",
            "Tăng natri máu",
            "Kiềm chuyển hóa"
        ],
        "dosage": {
            "adult_po": "Omeprazole 20mg/Sodium bicarbonate 1680mg PO x 1-2 lần/ngày, khi bụng đói",
            "adult_typical": "Omeprazole 20mg/Sodium bicarbonate 1680mg PO x 1 lần/ngày, khi bụng đói",
            "adult_h_pylori": "Omeprazole 20mg/Sodium bicarbonate 1680mg PO x 2 lần/ngày (kết hợp với amoxicillin + clarithromycin)",
            "notes": "Uống khi bụng đói, ít nhất 1 giờ trước bữa ăn. Sodium bicarbonate bảo vệ omeprazole khỏi acid dạ dày, cho phép hấp thu nhanh và tác dụng nhanh hơn PPI thông thường."
        },
        "renal_adjustment": {
            "normal": "Không cần chỉnh liều",
            "30_60": "Thận trọng, có thể cần giảm liều hoặc tránh dùng",
            "under_30": "CHỐNG CHỈ ĐỊNH",
            "dialysis": "CHỐNG CHỈ ĐỊNH",
            "notes": "Sodium bicarbonate chứa natri cao, có thể gây tăng natri máu và giữ nước ở suy thận và suy tim."
        },
        "side_effects": [
            "Nhức đầu",
            "Tiêu chảy",
            "Đau bụng",
            "Tăng natri máu (ở suy thận/suy tim)",
            "Giữ nước, phù (ở suy tim)",
            "Kiềm chuyển hóa (nếu dùng liều cao)",
            "Thiếu Vitamin B12 (omeprazole, dùng lâu dài)",
            "Thiếu Magie (omeprazole, dùng lâu dài)"
        ],
        "interactions": [
            "Clopidogrel: omeprazole giảm hiệu quả clopidogrel",
            "Ketoconazole, Itraconazole: omeprazole giảm hấp thu",
            "Warfarin: omeprazole có thể tăng INR"
        ],
        "pregnancy": "C - Thận trọng trong thai kỳ",
        "mechanism_of_action": "Omeprazole: ức chế bơm proton H+/K+ ATPase, giảm tiết acid dạ dày. Sodium bicarbonate: antacid, trung hòa acid dạ dày và tạo môi trường kiềm, bảo vệ omeprazole khỏi bị phá hủy bởi acid dạ dày. Cho phép omeprazole hấp thu nhanh và tác dụng nhanh hơn PPI thông thường (không cần enteric-coated).",
        "monitoring": [
            "Triệu chứng GERD, loét",
            "Natri máu (nếu suy thận/suy tim)",
            "Dấu hiệu giữ nước, phù",
            "Magie máu (nếu dùng omeprazole lâu dài)",
            "Vitamin B12 (nếu dùng omeprazole >3 năm)"
        ],
        "precautions": [
            "CHỐNG CHỈ ĐỊNH ở suy thận nặng và suy tim nặng",
            "Uống khi bụng đói, ít nhất 1 giờ trước bữa ăn",
            "Thận trọng ở suy thận trung bình và suy tim",
            "Theo dõi natri máu nếu có suy thận/suy tim",
            "Tránh dùng chung với Clopidogrel (chuyển sang Pantoprazole)"
        ],
        "pharmacokinetics": {
            "half_life": "Omeprazole: 0.5-1 giờ; Sodium bicarbonate: không áp dụng",
            "onset": "Omeprazole: tác dụng nhanh hơn PPI thông thường (do không cần enteric-coated)",
            "duration": "Omeprazole: 24 giờ",
            "protein_binding": "Omeprazole: 95%",
            "metabolism": "Omeprazole: gan (CYP2C19, CYP3A4)",
            "clearance": "Omeprazole: gan; Sodium bicarbonate: thận (thải natri)"
        },
        "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm, tránh ánh sáng",
        "black_box_warnings": "CHỐNG CHỈ ĐỊNH ở suy thận nặng (CrCl <30 ml/phút) và suy tim nặng. Tăng natri máu và giữ nước có thể gây suy tim cấp và các biến chứng nghiêm trọng.",
        "drug_interactions": {
            "major": [
                {
                    "drug": "Clopidogrel",
                    "mechanism": "Omeprazole ức chế CYP2C19, giảm chuyển hóa clopidogrel thành dạng hoạt động",
                    "effect": "Giảm hiệu quả chống kết tập tiểu cầu của clopidogrel",
                    "management": "TRÁNH DÙNG CÙNG. Chuyển sang pantoprazole hoặc H2 blocker."
                }
            ],
            "moderate": [
                {
                    "drug": "Ketoconazole, Itraconazole",
                    "mechanism": "Omeprazole giảm hấp thu azole antifungals",
                    "effect": "Giảm nồng độ azole, giảm hiệu quả",
                    "management": "Cách thời gian ít nhất 2 giờ."
                }
            ],
            "minor": []
        },
        "contraindications_detail": {
            "tuyệt_đối": [
                "Dị ứng omeprazole hoặc sodium bicarbonate",
                "Suy thận nặng (CrCl <30 ml/phút) - CHỐNG CHỈ ĐỊNH",
                "Suy tim nặng - CHỐNG CHỈ ĐỊNH",
                "Tăng natri máu",
                "Kiềm chuyển hóa"
            ],
            "tương_đối": [
                "Suy thận trung bình (CrCl 30-60) - thận trọng",
                "Suy tim trung bình - thận trọng"
            ]
        },
        "pregnancy_lactation": {
            "fda_category": "C",
            "pregnancy_details": "Thận trọng trong thai kỳ. Chỉ dùng khi lợi ích > nguy cơ.",
            "lactation": {
                "safety": "Compatible",
                "details": "Omeprazole bài tiết vào sữa mẹ ở nồng độ thấp. Sodium bicarbonate không hấp thu đáng kể.",
                "recommendation": "Có thể dùng khi cho con bú."
            }
        },
        "hepatic_adjustment": {
            "mild": "Không cần chỉnh liều",
            "moderate": "Thận trọng",
            "severe": "Thận trọng, có thể cần giảm liều",
            "notes": "Omeprazole chuyển hóa ở gan. Suy gan làm giảm chuyển hóa."
        },
        "overdose_management": {
            "symptoms": [
                "Tăng natri máu",
                "Kiềm chuyển hóa",
                "Giữ nước, phù",
                "Nhức đầu, chóng mặt"
            ],
            "antidote": "Không có antidote đặc hiệu",
            "treatment": [
                "Ngừng thuốc",
                "Điều chỉnh natri máu nếu tăng",
                "Điều chỉnh kiềm chuyển hóa nếu có",
                "Hỗ trợ triệu chứng"
            ],
            "monitoring": "Natri máu, pH máu, dấu hiệu giữ nước"
        },
        "reversal_agents": {
            "available": False,
            "agents": []
        },
        "administration_instructions": {
            "oral": {
                "with_food": "Uống khi bụng đói, ít nhất 1 giờ trước bữa ăn",
                "timing": "Uống 1-2 lần/ngày, khi bụng đói, ít nhất 1 giờ trước bữa ăn."
            }
        },
        "risk_flags": {
            "high_alert": True,
            "narrow_therapeutic_index": False,
            "bleeding_risk": False,
            "organ_toxicity": ["renal", "cardiovascular"],
            "qt_prolongation": False,
            "hepatotoxicity": False,
            "nephrotoxicity": True,
            "requires_monitoring": ["Sodium", "Fluid status", "Renal function"]
        },
        "guideline_tags": [
            "ACG 2017 GERD Guidelines",
            "FDA Drug Information",
            "FDA Black Box Warning"
        ],
        "references": {
            "primary_sources": [
                "FDA Drug Label - Omeprazole/Sodium bicarbonate (Zegerid)",
                "UpToDate - Omeprazole: Drug information",
                "ACG 2017 GERD Guidelines"
            ],
            "last_updated": "2025-01-15",
            "evidence_level": "High - FDA approved, multiple RCTs"
        }
    },
    
    "Pancreatin/Bile salts": {
        "group": "Gastrointestinal - Digestive Enzyme + Bile Salts (Fixed-Dose Combination)",
        "vietnamese_name": "Pancreatin/Bile salts, Festal, Digestal",
        "administration": ["PO"],
        "indications": [
            "Suy tụy ngoại tiết (pancreatic exocrine insufficiency)",
            "Xơ nang (cystic fibrosis)",
            "Viêm tụy mạn",
            "Thiếu hụt enzyme tiêu hóa và muối mật",
            "Khó tiêu do thiếu muối mật"
        ],
        "contraindications": [
            "Dị ứng pancreatin hoặc bile salts",
            "Dị ứng protein lợn",
            "Viêm tụy cấp",
            "Tắc ruột cơ học",
            "Tắc đường mật"
        ],
        "dosage": {
            "adult_po": "Pancreatin 25,000-50,000 units lipase/Bile salts 25-50mg PO với mỗi bữa ăn",
            "adult_typical": "Pancreatin 25,000 units lipase/Bile salts 25mg PO với mỗi bữa ăn",
            "adult_max": "Pancreatin 10,000 units lipase/kg/bữa ăn",
            "notes": "Uống cùng với thức ăn để tăng hiệu quả. Không nhai hoặc nghiền viên (enteric-coated). Bile salts giúp nhũ hóa chất béo, tăng hiệu quả tiêu hóa chất béo của pancreatin."
        },
        "renal_adjustment": {
            "normal": "Không cần chỉnh liều",
            "30_60": "Không cần chỉnh liều",
            "under_30": "Không cần chỉnh liều",
            "notes": "Pancreatin và bile salts không hấp thu đáng kể, tác dụng tại chỗ ở ruột."
        },
        "side_effects": [
            "Đau bụng",
            "Buồn nôn",
            "Tiêu chảy",
            "Táo bón",
            "Phát ban (dị ứng protein lợn)",
            "Tăng acid uric máu (liều cao)"
        ],
        "interactions": [
            "Acarbose, Miglitol: pancreatin giảm hiệu quả",
            "Iron: có thể giảm hấp thu sắt"
        ],
        "pregnancy": "C - Dữ liệu hạn chế, chỉ dùng khi lợi ích > nguy cơ",
        "mechanism_of_action": "Pancreatin: chứa lipase (tiêu hóa chất béo), amylase (tiêu hóa tinh bột), và protease (tiêu hóa protein). Bile salts: nhũ hóa chất béo, tạo micelles, tăng diện tích bề mặt cho lipase hoạt động, tăng hiệu quả tiêu hóa chất béo. Kết hợp giúp tiêu hóa chất béo hiệu quả hơn so với pancreatin đơn thuần.",
        "monitoring": [
            "Triệu chứng lâm sàng: giảm đau bụng, cải thiện tiêu hóa, tăng cân",
            "Phân: giảm phân mỡ (steatorrhea)",
            "Dấu hiệu dị ứng"
        ],
        "precautions": [
            "Uống cùng với thức ăn để tăng hiệu quả",
            "Không nhai hoặc nghiền viên (enteric-coated)",
            "Bắt đầu liều thấp và tăng dần theo đáp ứng",
            "Thận trọng ở bệnh nhân dị ứng protein lợn"
        ],
        "pharmacokinetics": {
            "half_life": "Không áp dụng (enzyme và bile salts, không hấp thu)",
            "onset": "Ngay lập tức khi vào ruột non",
            "duration": "Trong thời gian tiêu hóa bữa ăn",
            "protein_binding": "Không áp dụng",
            "clearance": "Thải qua phân (không hấp thu đáng kể)"
        },
        "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm, tránh ánh sáng",
        "black_box_warnings": "Nguy cơ fibrosing colonopathy ở trẻ em nếu dùng liều rất cao (>6,000 units lipase/kg/bữa ăn).",
        "drug_interactions": {
            "major": [],
            "moderate": [
                {
                    "drug": "Acarbose, Miglitol",
                    "mechanism": "Pancreatin chứa amylase, làm giảm hiệu quả acarbose/miglitol",
                    "effect": "Giảm hiệu quả điều trị đái tháo đường",
                    "management": "Thận trọng khi phối hợp."
                }
            ],
            "minor": []
        },
        "contraindications_detail": {
            "tuyệt_đối": [
                "Dị ứng pancreatin hoặc bile salts",
                "Dị ứng protein lợn",
                "Viêm tụy cấp",
                "Tắc ruột cơ học",
                "Tắc đường mật"
            ],
            "tương_đối": []
        },
        "pregnancy_lactation": {
            "fda_category": "C",
            "pregnancy_details": "Dữ liệu hạn chế. Chỉ dùng khi lợi ích > nguy cơ.",
            "lactation": {
                "safety": "Compatible",
                "details": "Pancreatin và bile salts không hấp thu đáng kể, không vào sữa mẹ.",
                "recommendation": "Có thể dùng khi cho con bú."
            }
        },
        "hepatic_adjustment": {
            "mild": "Không cần chỉnh liều",
            "moderate": "Không cần chỉnh liều",
            "severe": "Không cần chỉnh liều",
            "notes": "Không phụ thuộc chuyển hóa gan."
        },
        "overdose_management": {
            "symptoms": [
                "Đau bụng",
                "Tiêu chảy",
                "Tăng acid uric máu"
            ],
            "antidote": "Không có antidote đặc hiệu",
            "treatment": [
                "Ngừng thuốc",
                "Giảm liều",
                "Hỗ trợ triệu chứng"
            ],
            "monitoring": "Theo dõi triệu chứng"
        },
        "reversal_agents": {
            "available": False,
            "agents": []
        },
        "administration_instructions": {
            "oral": {
                "with_food": "Uống cùng với thức ăn để tăng hiệu quả",
                "timing": "Uống với mỗi bữa ăn và bữa ăn nhẹ. Không nhai hoặc nghiền viên (enteric-coated)."
            }
        },
        "risk_flags": {
            "high_alert": False,
            "narrow_therapeutic_index": False,
            "bleeding_risk": False,
            "organ_toxicity": [],
            "qt_prolongation": False,
            "hepatotoxicity": False,
            "nephrotoxicity": False,
            "requires_monitoring": []
        },
        "guideline_tags": [
            "FDA Drug Information",
            "Cystic Fibrosis Foundation Guidelines"
        ],
        "references": {
            "primary_sources": [
                "UpToDate - Pancreatic enzyme replacement therapy",
                "Cystic Fibrosis Foundation Guidelines",
                "FDA Drug Information"
            ],
            "last_updated": "2025-01-15",
            "evidence_level": "Moderate - Common combination, clinical practice"
        }
    }
}

__all__ = ["GASTROINTESTINAL_FIXED_DOSE_COMBINATIONS"]
