"""
Fluoroquinolone Antibiotics
"""
FLUOROQUINOLONE_ANTIBIOTICS = {
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
    
    "Ciprofloxacin": {
        "group": "Antibiotic - Fluoroquinolone",
        "vietnamese_name": "Ciprofloxacin, Cipro",
        "administration": ["PO", "IV"],
        "indications": [
            "Nhiễm khuẩn đường tiết niệu (UTI)",
            "Viêm bể thận",
            "Nhiễm khuẩn đường tiêu hóa (tiêu chảy do vi khuẩn, thương hàn)",
            "Nhiễm khuẩn da và mô mềm do Gram âm",
            "Nhiễm khuẩn xương và khớp do Gram âm",
            "Viêm phổi bệnh viện do Gram âm (bao gồm Pseudomonas)",
            "Dự phòng và điều trị bệnh than (anthrax) dạng hít"
        ],
        "contraindications": [
            "Dị ứng fluoroquinolone",
            "Trẻ em <18 tuổi (trừ chỉ định đặc biệt)",
            "Có thai",
            "QT kéo dài hoặc rối loạn nhịp tim nặng"
        ],
        "contraindications_detail": {
            "tuyệt_đối": [
                "Dị ứng fluoroquinolone",
                "Trẻ em <18 tuổi (trừ chỉ định đặc biệt)",
                "Có thai",
                "QT kéo dài hoặc rối loạn nhịp tim nặng"
            ],
            "tương_đối": []
        },
        "reversal_agents": {
            "available": False,
            "agents": [],
            "notes": "Không có antidote đặc hiệu. Điều trị quá liều chủ yếu là điều trị hỗ trợ: ngừng ngay ciprofloxacin, rửa dạ dày hoặc than hoạt nếu uống trong vòng 1-2 giờ, theo dõi dấu hiệu sinh tồn, điều trị triệu chứng tiêu hóa, theo dõi ECG nếu có nguy cơ QT kéo dài, theo dõi đường huyết, theo dõi triệu chứng thần kinh, lọc máu có thể loại bỏ một phần nhưng không được khuyến nghị thường quy."
        },
        "dosage": {
            "adult_uti_uncomplicated": "250mg PO mỗi 12 giờ x 3 ngày",
            "adult_uti_complicated": "500mg PO mỗi 12 giờ x 7-14 ngày",
            "adult_pyelo": "500-750mg PO mỗi 12 giờ x 7-14 ngày",
            "adult_iv": "400mg IV mỗi 8-12 giờ",
            "adult_anthrax": "500mg PO mỗi 12 giờ x 60 ngày",
            "notes": "Uống với nhiều nước. Tránh antacid, sắt, kẽm 2 giờ trước/sau. Không phải lựa chọn đầu tay cho viêm phổi cộng đồng (kém hơn levo/moxi với Streptococcus pneumoniae)."
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "250-500mg mỗi 12 giờ",
            "under_30": "250-500mg mỗi 24 giờ",
            "hemodialysis": "250-500mg sau mỗi lần lọc"
        },
        "side_effects": [
            "Rối loạn tiêu hóa",
            "Nhức đầu, chóng mặt",
            "Rối loạn gân (viêm gân, đứt gân)",
            "QT kéo dài",
            "Rối loạn đường huyết",
            "Ảo giác, kích động (hiếm, chủ yếu ở người già)"
        ],
        "interactions": [
            "Antacid/Sắt/Kẽm: giảm hấp thu (cách 2 giờ)",
            "Warfarin: tăng nguy cơ chảy máu (tăng INR)",
            "Theophylline: tăng nồng độ theophylline",
            "NSAID: tăng nguy cơ co giật"
        ],
        "drug_interactions": {
            "major": [
                {
                    "drug": "Antacid/Sắt/Kẽm/Sucralfate",
                    "mechanism": "Cation đa hóa trị tạo phức, giảm hấp thu ciprofloxacin",
                    "effect": "Giảm nồng độ, giảm hiệu quả điều trị",
                    "management": "Cách ≥2 giờ (tốt nhất 4 giờ) trước/sau ciprofloxacin"
                },
                {
                    "drug": "Theophylline",
                    "mechanism": "Ức chế chuyển hóa theophylline",
                    "effect": "Tăng nồng độ theophylline → độc tính (run, loạn nhịp, co giật)",
                    "management": "Tránh nếu có thể; theo dõi nồng độ/triệu chứng, giảm liều theophylline"
                },
                {
                    "drug": "Thuốc kéo dài QT (amiodarone, sotalol, macrolide, antipsychotic)",
                    "mechanism": "Cộng dồn kéo dài QT",
                    "effect": "Tăng nguy cơ torsades de pointes",
                    "management": "Tránh phối hợp; nếu bắt buộc, theo dõi ECG chặt"
                }
            ],
            "moderate": [
                {
                    "drug": "Warfarin",
                    "mechanism": "Tác động vi khuẩn ruột, chuyển hóa/đạm gắn",
                    "effect": "INR tăng, nguy cơ chảy máu",
                    "management": "Theo dõi INR, điều chỉnh liều warfarin"
                },
                {
                    "drug": "NSAID",
                    "mechanism": "Cộng dồn nguy cơ kích thích CNS",
                    "effect": "Tăng nguy cơ co giật",
                    "management": "Tránh phối hợp nếu có thể; thận trọng bệnh nhân tiền sử co giật"
                }
            ],
            "minor": []
        },
        "pregnancy": "C",
        "pregnancy_lactation": {
            "fda_category": "C",
            "pregnancy_details": "Tránh dùng; fluoroquinolone có nguy cơ tổn thương sụn thai nhi.",
            "lactation": {
                "safety": "Caution",
                "details": "Bài tiết vào sữa mẹ ở mức thấp; cân nhắc tạm ngưng cho bú hoặc chọn thuốc khác.",
                "recommendation": "Dùng thận trọng, theo dõi trẻ (tiêu chảy, tưa miệng)."
            }
        },
        "mechanism_of_action": "Fluoroquinolone thế hệ 2, ức chế DNA gyrase (Gram âm) và topoisomerase IV (Gram dương), ngăn sao chép và sửa chữa DNA. Phổ: Gram âm mạnh (Enterobacteriaceae, Pseudomonas aeruginosa), một số Gram dương và vi khuẩn không điển hình; Gram dương yếu hơn levo/moxi.",
        "monitoring": [
            "Dấu hiệu nhiễm trùng và đáp ứng điều trị",
            "Đau gân, đặc biệt gân Achilles (ngừng ngay nếu có)",
            "ECG nếu có nguy cơ QT kéo dài hoặc dùng thuốc kéo dài QT",
            "Đường huyết (đặc biệt ở bệnh nhân đái tháo đường)",
            "Triệu chứng thần kinh (kích động, ảo giác) ở người cao tuổi"
        ],
        "precautions": [
            "Nguy cơ viêm gân/đứt gân (tăng ở >60 tuổi, dùng corticosteroid, ghép tạng)",
            "Nguy cơ QT kéo dài và rối loạn nhịp",
            "Không dùng thường quy cho viêm phổi cộng đồng (SPN kháng cao hơn)",
            "Tránh dùng cho trẻ em nếu có thể (nguy cơ tổn thương sụn)",
            "Tránh dùng đồng thời antacid, sắt, kẽm",
        ],
        "pharmacokinetics": {
            "half_life": "4 giờ",
            "onset": "1-2 giờ (PO)",
            "duration": "q12h",
            "protein_binding": "20-40%",
            "clearance": "Chủ yếu qua thận, cần chỉnh liều ở suy thận"
        },
        "storage": "Bảo quản ở nhiệt độ phòng, tránh ẩm và ánh sáng.",
        "hepatic_adjustment": {
            "mild": "Không cần chỉnh liều; chuyển hóa tối thiểu.",
            "moderate": "Không cần chỉnh liều; thận trọng vì dữ liệu hạn chế.",
            "severe": "Thận trọng; ưu tiên liều thấp và theo dõi nếu phải dùng.",
            "notes": "Chủ yếu thải trừ qua thận; ảnh hưởng gan không lớn nhưng thận trọng khi suy gan nặng."
        },
        "overdose_management": {
            "symptoms": [
                "Buồn nôn, nôn, chóng mặt",
                "Co giật, kích động",
                "QT kéo dài, loạn nhịp",
                "Rối loạn đường huyết"
            ],
            "antidote": "Không có antidote đặc hiệu.",
            "treatment": [
                "Ngừng ciprofloxacin; than hoạt/rửa dạ dày nếu sớm.",
                "Theo dõi ECG, dấu hiệu sinh tồn.",
                "Điều trị co giật: benzodiazepine.",
                "Bù dịch; theo dõi đường huyết, điện giải.",
                "Xem xét lọc máu: loại bỏ một phần thuốc nhưng không bắt buộc."
            ],
            "monitoring": "ECG (QT), đường huyết, thần kinh, điện giải trong 24-48h."
        },
        "administration_instructions": {
            "oral": {
                "with_food": "Có thể uống cùng hoặc không cùng thức ăn.",
                "timing": "Uống mỗi 12 giờ; cách antacid/sắt/kẽm/sucralfate ≥2 giờ."
            },
            "iv": {
                "reconstitution": "Dung dịch sẵn dùng hoặc pha NS/D5W.",
                "infusion_rate": "Truyền trong ≥60 phút (400mg/200ml ~3.3ml/phút).",
                "compatibility": ["NS", "D5W"],
                "notes": "Tránh truyền nhanh; theo dõi phản ứng tại chỗ và QT."
            }
        },
        "black_box_warnings": "Nguy cơ viêm gân/đứt gân, bệnh thần kinh ngoại biên, tác dụng phụ thần kinh trung ương, và làm nặng thêm nhược cơ.",
        "risk_flags": {
            "high_alert": True,
            "narrow_therapeutic_index": False,
            "icu_critical_care_only": False,
            "bleeding_risk": "Low",
            "organ_toxicity": {"musculoskeletal": "High (tendon rupture)", "cardiac": "Moderate (QT prolongation)", "neurological": "Moderate", "metabolic": "Moderate (glucose dysregulation)"}
        },
        "guideline_tags": [
            "IDSA Guidelines - Complicated Urinary Tract Infections",
            "IDSA Guidelines - Hospital-Acquired Pneumonia",
            "IDSA Guidelines - Skin and Soft Tissue Infections",
            "IDSA Guidelines - Traveler's Diarrhea",
            "CDC Guidelines - Anthrax Treatment",
            "WHO Essential Medicines List"
        ],
        "last_updated": "2026-01-07",
    },
    
    "Norfloxacin": {
        "group": "Antibiotic - Fluoroquinolone",
        "vietnamese_name": "Norfloxacin, Noroxin",
        "administration": ["PO"],
        "indications": [
            "Nhiễm khuẩn đường tiết niệu không biến chứng",
            "Dự phòng nhiễm khuẩn đường tiết niệu tái phát",
            "Dự phòng nhiễm khuẩn ở bệnh nhân xơ gan cổ trướng (SBP prophylaxis - ít dùng hơn hiện nay)"
        ],
        "contraindications": [
            "Dị ứng fluoroquinolone",
            "Trẻ em <18 tuổi",
            "Có thai",
            "QT kéo dài"
        ],
        "dosage": {
            "adult_uti": "400mg PO mỗi 12 giờ x 3-7 ngày",
            "adult_prophylaxis_uti": "200-400mg PO mỗi ngày",
            "adult_sbp_prophylaxis": "400mg PO mỗi ngày",
            "notes": "Sinh khả dụng kém hơn ciprofloxacin; chủ yếu dùng cho UTI không biến chứng và một số chỉ định dự phòng."
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "400mg mỗi 24 giờ",
            "under_30": "200-400mg mỗi 24-48 giờ"
        },
        "side_effects": [
            "Rối loạn tiêu hóa",
            "Nhức đầu",
            "Chóng mặt",
            "Rối loạn gân",
            "QT kéo dài"
        ],
        "interactions": [
            "Antacid/Sắt/Kẽm: giảm hấp thu (cách 2 giờ)",
            "Warfarin: tăng INR",
            "NSAID: tăng nguy cơ co giật"
        ],
        "pregnancy": "C",
        "mechanism_of_action": "Fluoroquinolone thế hệ 2, ức chế DNA gyrase/topoisomerase IV. Phổ chủ yếu Gram âm ở đường tiết niệu; ít dùng hiện nay do tác dụng phụ và có lựa chọn an toàn hơn.",
        "monitoring": [
            "Đau gân",
            "ECG nếu có yếu tố nguy cơ",
        ],
        "precautions": [
            "Không dùng kéo dài nếu có lựa chọn khác",
            "Nguy cơ tác dụng phụ lớp fluoroquinolone giống ciprofloxacin",
        ],
        "pharmacokinetics": {
            "half_life": "3-4 giờ",
            "clearance": "Chủ yếu qua thận"
        },
        "storage": "Bảo quản ở nhiệt độ phòng.",
        "black_box_warnings": "Như các fluoroquinolone khác: gân, thần kinh, tâm thần, nhược cơ.",
        "risk_flags": {
            "high_alert": False,
            "narrow_therapeutic_index": False,
            "icu_critical_care_only": False,
            "bleeding_risk": "Low",
            "organ_toxicity": {"musculoskeletal": "High (tendon rupture)", "neurological": "Moderate"}
        },
        "guideline_tags": [
            "IDSA Guidelines - Uncomplicated Urinary Tract Infections (Historical)",
            "WHO Essential Medicines List"
        ],
        "last_updated": "2025-02-18",
    },
    
    "Ofloxacin": {
        "group": "Antibiotic - Fluoroquinolone",
        "vietnamese_name": "Ofloxacin, Tarivid",
        "administration": ["PO", "IV", "Ophthalmic", "Otic"],
        "indications": [
            "Nhiễm khuẩn đường tiết niệu",
            "Viêm bể thận",
            "Nhiễm khuẩn da và mô mềm",
            "Viêm phế quản cấp",
            "Nhiễm khuẩn mắt/ tai (dạng nhỏ)",
        ],
        "contraindications": [
            "Dị ứng fluoroquinolone",
            "Trẻ em <18 tuổi",
            "Có thai",
            "QT kéo dài"
        ],
        "dosage": {
            "adult_po": "200-400mg PO mỗi 12 giờ",
            "adult_iv": "200-400mg IV mỗi 12 giờ",
            "adult_uti": "200mg PO mỗi 12 giờ x 3-7 ngày",
            "notes": "Tiền thân của levofloxacin (levo là đồng phân L). Ít dùng hơn hiện nay, thường được thay bằng levofloxacin."
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "200mg mỗi 12 giờ",
            "under_30": "200mg mỗi 24 giờ"
        },
        "side_effects": [
            "Rối loạn tiêu hóa",
            "Nhức đầu",
            "Rối loạn giấc ngủ",
            "Rối loạn gân",
            "QT kéo dài"
        ],
        "interactions": [
            "Antacid/Sắt/Kẽm: giảm hấp thu (cách 2 giờ)",
            "Warfarin: tăng INR",
            "Corticosteroid: tăng nguy cơ đứt gân"
        ],
        "pregnancy": "C",
        "mechanism_of_action": "Fluoroquinolone thế hệ 2, ức chế DNA gyrase/topoisomerase IV. Phổ tương tự ciprofloxacin nhưng Gram dương tốt hơn một chút, kém hơn levo/moxi.",
        "monitoring": [
            "Đau gân",
            "ECG nếu có nguy cơ QT kéo dài",
        ],
        "precautions": [
            "Tương tự các fluoroquinolone khác về gân, thần kinh, đường huyết",
            "Không ưu tiên khi có levofloxacin thay thế",
        ],
        "pharmacokinetics": {
            "half_life": "6-8 giờ",
            "clearance": "Chủ yếu qua thận"
        },
        "storage": "Bảo quản ở nhiệt độ phòng.",
        "black_box_warnings": "Như lớp fluoroquinolone khác.",
        "risk_flags": {
            "high_alert": False,
            "narrow_therapeutic_index": False,
            "icu_critical_care_only": False,
            "bleeding_risk": "Low",
            "organ_toxicity": {"musculoskeletal": "High (tendon rupture)", "neurological": "Moderate"}
        },
        "guideline_tags": [
            "IDSA Guidelines - Urinary Tract Infections",
            "CDC Guidelines - Sexually Transmitted Diseases (Historical)"
        ],
        "last_updated": "2025-02-18",
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
        "tuyệt_đối": [
            "Dị ứng levofloxacin hoặc các fluoroquinolone khác",
            "Có thai - chống chỉ định tuyệt đối, nguy cơ tổn thương sụn thai nhi",
            "Trẻ em < 18 tuổi (trừ trường hợp đặc biệt) - nguy cơ tổn thương sụn, viêm khớp",
            "QT kéo dài hoặc rối loạn nhịp tim nặng - tăng nguy cơ loạn nhịp tim nghiêm trọng"
        ],
        "tương_đối": [
            "Bệnh nhân > 60 tuổi - tăng nguy cơ đứt gân, viêm gân",
            "Dùng corticosteroid - tăng nguy cơ đứt gân",
            "Ghép cơ quan - tăng nguy cơ đứt gân",
            "Tiền sử co giật - tăng nguy cơ co giật",
            "Suy thận nặng (CrCl <30) - giảm liều đáng kể",
            "Dùng với warfarin - tăng nguy cơ chảy máu",
            "Hoạt động thể lực nặng - tăng nguy cơ đứt gân"
        ]
    },
    "contraindications_detail": {
        "tuyệt_đối": [
            "Dị ứng levofloxacin hoặc các fluoroquinolone khác",
            "Có thai - chống chỉ định tuyệt đối, nguy cơ tổn thương sụn thai nhi",
            "Trẻ em < 18 tuổi (trừ trường hợp đặc biệt) - nguy cơ tổn thương sụn, viêm khớp",
            "QT kéo dài hoặc rối loạn nhịp tim nặng - tăng nguy cơ loạn nhịp tim nghiêm trọng"
        ],
        "tương_đối": [
            "Bệnh nhân > 60 tuổi - tăng nguy cơ đứt gân, viêm gân",
            "Dùng corticosteroid - tăng nguy cơ đứt gân",
            "Ghép cơ quan - tăng nguy cơ đứt gân",
            "Tiền sử co giật - tăng nguy cơ co giật",
            "Suy thận nặng (CrCl <30) - giảm liều đáng kể",
            "Dùng với warfarin - tăng nguy cơ chảy máu",
            "Hoạt động thể lực nặng - tăng nguy cơ đứt gân"
        ]
    },
    "reversal_agents": {"available": False, "agents": [], "notes": "Không có antidote đặc hiệu. Điều trị chủ yếu là hỗ trợ và điều trị triệu chứng. Ngừng thuốc ngay nếu có triệu chứng đứt gân, QT kéo dài, hoặc co giật."},
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
    "pediatric_dosing": {
        "neonates": "CHỐNG CHỈ ĐỊNH ở trẻ <18 tuổi (trừ trường hợp đặc biệt như nhiễm trùng nặng không có lựa chọn khác). Nguy cơ tổn thương sụn, viêm khớp.",
        "infants": "CHỐNG CHỈ ĐỊNH ở trẻ <18 tuổi (trừ trường hợp đặc biệt như nhiễm trùng nặng không có lựa chọn khác). Nguy cơ tổn thương sụn, viêm khớp.",
        "children": "CHỐNG CHỈ ĐỊNH ở trẻ <18 tuổi (trừ trường hợp đặc biệt như nhiễm trùng nặng không có lựa chọn khác). Nếu bắt buộc: 10mg/kg/ngày IV (tối đa 500mg/ngày). Theo dõi chặt chẽ dấu hiệu đau gân, viêm gân. Nguy cơ tổn thương sụn, viêm khớp.",
        "adolescents": "CHỐNG CHỈ ĐỊNH ở trẻ <18 tuổi (trừ trường hợp đặc biệt như nhiễm trùng nặng không có lựa chọn khác). Nếu bắt buộc: liều người lớn (500-750mg x 1 lần/ngày). Theo dõi chặt chẽ dấu hiệu đau gân, viêm gân.",
        "notes": "CHỐNG CHỈ ĐỊNH ở trẻ <18 tuổi do nguy cơ tổn thương sụn, viêm khớp. Chỉ dùng trong trường hợp đặc biệt như nhiễm trùng nặng (ví dụ: viêm phổi do Pseudomonas nặng) không có lựa chọn khác. Nếu dùng, theo dõi chặt chẽ dấu hiệu đau gân, viêm gân, đứt gân. Ngừng ngay nếu có đau gân. Ưu điểm: dùng 1 lần/ngày, compliance tốt hơn ciprofloxacin."
    },
    "geriatric_dosing": {
        "considerations": "Người cao tuổi (>60 tuổi) có nguy cơ cao hơn đứt gân, viêm gân (đặc biệt gân Achilles). Suy thận phổ biến hơn, cần điều chỉnh liều. Tăng nguy cơ QT kéo dài, rối loạn nhịp tim.",
        "dose_adjustment": "Điều chỉnh liều theo chức năng thận: CrCl 30-60 → giảm liều 50% (250-375mg/ngày), CrCl <30 → 250-500mg x 1 lần/ngày. Khởi đầu với liều thấp hơn.",
        "monitoring": "Theo dõi chặt chẽ dấu hiệu đau gân, viêm gân, đứt gân (đặc biệt gân Achilles). Theo dõi ECG (QT interval). Theo dõi chức năng thận (creatinine, CrCl). Theo dõi dấu hiệu thần kinh (rối loạn giấc ngủ, nhức đầu). Ngừng ngay nếu có đau gân."
    },
    "brand_names": {
        "vietnam": ["Levofloxacin", "Tavanic", "Levofloxacin Stada", "Levo"],
        "common": ["Tavanic", "Levofloxacin", "Levaquin"]
    },
    "cost_estimate": {
        "unit": "VND",
        "range": "10,000 - 50,000 VND/viên (tùy hàm lượng và thương hiệu)",
        "note": "Giá thay đổi theo thương hiệu và nhà thuốc. Levofloxacin generic thường rẻ hơn (10,000-30,000 VND/viên 500mg). Tavanic (brand) thường đắt hơn (30,000-50,000 VND/viên 500mg). Dạng IV: 80,000-150,000 VND/lọ 500mg."
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
        "last_updated": "2025-02-18",
        "evidence_level": "A - Dựa trên FDA drug labels, IDSA guidelines, và dữ liệu lâm sàng từ nhiều nguồn"
    },
    "risk_flags": {
        "high_alert": True,
        "narrow_therapeutic_index": False,
        "icu_critical_care_only": False,
        "bleeding_risk": "Low",
        "organ_toxicity": {"musculoskeletal": "High (tendon rupture)", "cardiac": "Moderate (QT prolongation)", "neurological": "Moderate"}
    },
    "guideline_tags": [
        "IDSA Guidelines - Community-Acquired Pneumonia",
        "IDSA Guidelines - Complicated Urinary Tract Infections",
        "IDSA Guidelines - Skin and Soft Tissue Infections",
        "IDSA Guidelines - Acute Bacterial Sinusitis",
        "WHO Essential Medicines List"
    ],
    "last_updated": "2025-02-18",
    },
    
    "Moxifloxacin": {
        "group": "Antibiotic - Fluoroquinolone (4th Generation)",
        "vietnamese_name": "Moxifloxacin, Avelox",
        "administration": ["PO", "IV"],
        "indications": [
            "Viêm phổi cộng đồng",
            "Viêm phổi bệnh viện (một số trường hợp)",
            "Nhiễm khuẩn da và mô mềm",
            "Viêm xoang cấp",
            "Viêm phúc mạc (kết hợp)"
        ],
        "contraindications": [
            "Dị ứng fluoroquinolone",
            "Trẻ em <18 tuổi (trừ trường hợp đặc biệt)",
            "Có thai",
            "QT kéo dài",
            "Rối loạn nhịp tim nặng"
        ],
        "dosage": {
            "adult_po": "400mg x 1 lần/ngày",
            "adult_iv": "400mg IV x 1 lần/ngày",
            "adult_pneumonia": "400mg x 1 lần/ngày x 7-14 ngày",
            "notes": "Uống với hoặc không thức ăn. Không cần điều chỉnh thận (thải qua gan/mật)"
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "Không đổi (thải qua gan/mật)",
            "under_30": "Không đổi (thải qua gan/mật)"
        },
        "side_effects": [
            "Rối loạn tiêu hóa",
            "Nhức đầu",
            "Rối loạn giấc ngủ",
            "Rối loạn gân (viêm gân, đứt gân)",
            "QT kéo dài (nhiều hơn các fluoroquinolone khác)",
            "Hạ đường huyết (hiếm)",
            "Tăng men gan (hiếm)"
        ],
        "interactions": [
            "Antacid/Sắt: giảm hấp thu (cách 4 giờ)",
            "Warfarin: tăng nguy cơ chảy máu",
            "Corticosteroid: tăng nguy cơ đứt gân",
            "Thuốc kéo dài QT: tăng nguy cơ rối loạn nhịp tim"
        ],
        "pregnancy": "C",
        "mechanism_of_action": "Moxifloxacin là fluoroquinolone thế hệ 4, kháng sinh phổ rộng. Ức chế DNA gyrase (ở vi khuẩn Gram-âm) và topoisomerase IV (ở vi khuẩn Gram-dương), enzyme cần thiết cho sao chép và sửa chữa DNA. Dẫn đến tổn thương DNA và chết tế bào vi khuẩn. Phổ kháng khuẩn: Gram-âm mạnh (Enterobacteriaceae, H. influenzae, Neisseria), Gram-dương tốt hơn các fluoroquinolone khác (Streptococcus pneumoniae - kể cả penicillin-resistant và macrolide-resistant, Staphylococcus aureus - MSSA), và vi khuẩn không điển hình (Legionella, Mycoplasma, Chlamydia). Đặc điểm: dùng 1 lần/ngày, không cần điều chỉnh thận (thải qua gan/mật), hiệu quả tốt với viêm phổi, nhưng QT kéo dài nhiều hơn.",
        "monitoring": [
            "Dấu hiệu nhiễm trùng (sốt, WBC, triệu chứng lâm sàng)",
            "Cấy máu và cấy từ vị trí nhiễm trùng",
            "ECG - QT interval (quan trọng, moxifloxacin kéo dài QT nhiều hơn các fluoroquinolone khác)",
            "Tendon (gân) - đau, sưng, đứt gân (đặc biệt gân Achilles)",
            "Thần kinh trung ương (mất ngủ, lo âu, kích động, co giật)",
            "Tim mạch (QT kéo dài, rối loạn nhịp tim) - đặc biệt quan trọng với moxifloxacin",
            "Đường huyết (tăng hoặc hạ đường huyết)",
            "Chức năng gan (ALT, AST) - hiếm viêm gan nặng"
        ],
        "precautions": [
            "NGỪNG NGAY nếu có đau, sưng gân (nguy cơ đứt gân, đặc biệt gân Achilles)",
            "QT kéo dài NGHIÊM TRỌNG → không dùng với các thuốc kéo dài QT khác (amiodarone, sotalol, antipsychotics), bệnh nhân có tiền sử rối loạn nhịp, suy tim",
            "Theo dõi ECG trước và trong khi dùng (đặc biệt quan trọng với moxifloxacin)",
            "Co giật → không dùng ở bệnh nhân có tiền sử co giật, tránh dùng với NSAID",
            "Tăng độ nhạy cảm với ánh sáng → tránh ánh nắng trực tiếp, dùng kem chống nắng",
            "Tương tác với nhiều thuốc: giảm hấp thu với antacid, sucralfate, sắt, kẽm (cách 4 giờ)",
            "Hạ đường huyết → thận trọng với sulfonylurea",
            "Không dùng cho trẻ em < 18 tuổi (trừ trường hợp đặc biệt) - nguy cơ tổn thương sụn",
            "Không cần điều chỉnh thận (thải qua gan/mật) - ưu điểm",
            "Uống nhiều nước để tránh kết tinh trong nước tiểu",
            "Ưu điểm: dùng 1 lần/ngày, không cần điều chỉnh thận, hiệu quả tốt với viêm phổi"
        ],
        "pharmacokinetics": {
            "half_life": "12 giờ (dài nhất trong fluoroquinolone)",
            "onset": "1-2 giờ (PO), ngay lập tức (IV)",
            "duration": "q24h (1 lần/ngày)",
            "protein_binding": "30-50%",
            "metabolism": "Chủ yếu qua gan (CYP450)",
            "clearance": "Gan (chủ yếu, chuyển hóa qua CYP450), mật (một phần). Không thải qua thận → không cần điều chỉnh thận"
        },
        "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm, tránh ánh sáng. Dung dịch IV: bảo quản theo hướng dẫn nhà sản xuất",
        "black_box_warnings": "Nguy cơ đứt gân, viêm gân (đặc biệt gân Achilles) - có thể xảy ra bất cứ lúc nào, kể cả sau khi ngừng thuốc. Ngừng ngay nếu có đau, sưng gân. QT kéo dài NGHIÊM TRỌNG - có thể gây rối loạn nhịp tim nghiêm trọng, đe dọa tính mạng. Không dùng với các thuốc kéo dài QT khác. Theo dõi ECG trước và trong khi dùng.",
        "drug_interactions": {
            "major": [
                {
                    "drug": "Antacids (Aluminum, Magnesium), Sucralfate, Sắt, Kẽm",
                    "mechanism": "Cation (Al3+, Mg2+, Fe2+, Zn2+) tạo phức hợp không hòa tan với moxifloxacin, giảm hấp thu.",
                    "effect": "Giảm hấp thu moxifloxacin, giảm nồng độ trong máu, giảm hiệu quả điều trị",
                    "management": "Cách ít nhất 4 giờ trước hoặc sau khi uống moxifloxacin. Không uống cùng lúc."
                },
                {
                    "drug": "Warfarin",
                    "mechanism": "Moxifloxacin có thể ảnh hưởng đến chuyển hóa warfarin.",
                    "effect": "Tăng tác dụng chống đông, tăng INR, tăng nguy cơ chảy máu",
                    "management": "Theo dõi INR chặt chẽ khi bắt đầu, thay đổi liều, hoặc ngừng moxifloxacin. Điều chỉnh liều warfarin nếu cần."
                },
                {
                    "drug": "Thuốc kéo dài QT (Amiodarone, Sotalol, Antipsychotics, Macrolides)",
                    "mechanism": "Cả hai đều kéo dài QT, tác dụng cộng dồn.",
                    "effect": "Tăng nguy cơ rối loạn nhịp tim nghiêm trọng, đe dọa tính mạng (torsades de pointes)",
                    "management": "CHỐNG CHỈ ĐỊNH dùng cùng. Nếu bắt buộc, theo dõi ECG liên tục. Theo dõi QT interval."
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
                    "mechanism": "Moxifloxacin có thể gây hạ đường huyết.",
                    "effect": "Tăng nguy cơ hạ đường huyết",
                    "management": "Theo dõi đường huyết. Điều chỉnh liều sulfonylurea nếu cần."
                }
            ],
            "minor": []
        },
        "contraindications": {
            "tuyệt_đối": [
                "Dị ứng moxifloxacin hoặc các fluoroquinolone khác",
                "Có thai - chống chỉ định tuyệt đối, nguy cơ tổn thương sụn thai nhi",
                "Trẻ em < 18 tuổi (trừ trường hợp đặc biệt) - nguy cơ tổn thương sụn, viêm khớp",
                "QT kéo dài hoặc rối loạn nhịp tim nặng - tăng nguy cơ loạn nhịp tim nghiêm trọng",
                "Dùng với thuốc kéo dài QT - chống chỉ định tuyệt đối"
            ],
            "tương_đối": [
                "Bệnh nhân > 60 tuổi - tăng nguy cơ đứt gân, viêm gân, QT kéo dài",
                "Dùng corticosteroid - tăng nguy cơ đứt gân",
                "Ghép cơ quan - tăng nguy cơ đứt gân",
                "Tiền sử co giật - tăng nguy cơ co giật",
                "Suy tim - tăng nguy cơ QT kéo dài, rối loạn nhịp tim",
                "Suy gan nặng - có thể tích lũy (thải qua gan)",
                "Dùng với warfarin - tăng nguy cơ chảy máu",
                "Hoạt động thể lực nặng - tăng nguy cơ đứt gân"
            ]
        },
        "contraindications_detail": {
            "tuyệt_đối": [
                "Dị ứng moxifloxacin hoặc các fluoroquinolone khác",
                "Có thai - chống chỉ định tuyệt đối, nguy cơ tổn thương sụn thai nhi",
                "Trẻ em < 18 tuổi (trừ trường hợp đặc biệt) - nguy cơ tổn thương sụn, viêm khớp",
                "QT kéo dài hoặc rối loạn nhịp tim nặng - tăng nguy cơ loạn nhịp tim nghiêm trọng",
                "Dùng với thuốc kéo dài QT - chống chỉ định tuyệt đối"
            ],
            "tương_đối": [
                "Bệnh nhân > 60 tuổi - tăng nguy cơ đứt gân, viêm gân, QT kéo dài",
                "Dùng corticosteroid - tăng nguy cơ đứt gân",
                "Ghép cơ quan - tăng nguy cơ đứt gân",
                "Tiền sử co giật - tăng nguy cơ co giật",
                "Suy tim - tăng nguy cơ QT kéo dài, rối loạn nhịp tim",
                "Suy gan nặng - có thể tích lũy (thải qua gan)",
                "Dùng với warfarin - tăng nguy cơ chảy máu",
                "Hoạt động thể lực nặng - tăng nguy cơ đứt gân"
            ]
        },
        "reversal_agents": {"available": False, "agents": [], "notes": "Không có antidote đặc hiệu. Điều trị chủ yếu là hỗ trợ và điều trị triệu chứng. Ngừng thuốc ngay nếu có triệu chứng đứt gân, QT kéo dài, hoặc co giật."},
        "pregnancy_lactation": {
            "fda_category": "C",
            "pregnancy_details": "Moxifloxacin là thuốc phân loại C. Các nghiên cứu trên động vật cho thấy có thể gây tổn thương sụn ở khớp ở thai nhi. Có báo cáo về tổn thương sụn ở trẻ em khi dùng trong thai kỳ. CHỐNG CHỈ ĐỊNH trong thai kỳ trừ khi lợi ích vượt quá nguy cơ rõ ràng và không có lựa chọn khác. Nhiễm trùng nặng có thể gây nguy hiểm cho thai nhi, nhưng nên dùng kháng sinh khác nếu có thể.",
            "lactation": {
                "safety": "Compatible (với thận trọng)",
                "details": "Moxifloxacin bài tiết vào sữa mẹ ở nồng độ thấp. Nồng độ trong sữa mẹ thấp và không có báo cáo về tác dụng phụ đáng kể ở trẻ bú mẹ. Tuy nhiên, fluoroquinolone có thể gây tổn thương sụn ở trẻ sơ sinh.",
                "recommendation": "Có thể dùng khi cho con bú với thận trọng. Dùng liều thấp nhất hiệu quả. Theo dõi trẻ sơ sinh. Tránh dùng nếu có lựa chọn khác."
            }
        },
        "hepatic_adjustment": {
            "mild": "Không cần điều chỉnh liều. Moxifloxacin chuyển hóa qua gan nhưng không phụ thuộc nhiều vào chức năng gan.",
            "moderate": "Không cần điều chỉnh liều. Thận trọng nếu có suy gan nặng.",
            "severe": "Thận trọng, có thể tích lũy ở suy gan nặng. Có thể cần giảm liều hoặc tăng khoảng cách liều.",
            "notes": "Moxifloxacin chuyển hóa qua gan (CYP450), thải trừ qua mật. Suy gan nặng có thể giảm chuyển hóa và tích lũy. Theo dõi chức năng gan và tác dụng phụ."
        },
        "overdose_management": {
            "symptoms": [
                "Triệu chứng tiêu hóa: Buồn nôn, nôn, tiêu chảy, đau bụng",
                "Triệu chứng thần kinh: Co giật, kích động, lo âu, mất ngủ, trầm cảm, rối loạn tâm thần",
                "Triệu chứng gân: Đau gân, viêm gân, đứt gân (đặc biệt gân Achilles)",
                "Triệu chứng tim mạch: QT kéo dài NGHIÊM TRỌNG, rối loạn nhịp tim nghiêm trọng (torsades de pointes), có thể gây tử vong",
                "Triệu chứng chuyển hóa: Hạ hoặc tăng đường huyết",
                "Triệu chứng nghiêm trọng: Rối loạn nhịp tim nghiêm trọng, đứt gân"
            ],
            "antidote": "Không có antidote đặc hiệu. Điều trị hỗ trợ và điều trị triệu chứng.",
            "treatment": [
                "Ngừng ngay moxifloxacin",
                "Rửa dạ dày hoặc than hoạt nếu uống trong vòng 1-2 giờ (nếu không có chống chỉ định)",
                "Theo dõi dấu hiệu sinh tồn: Huyết áp, nhịp tim, nhịp thở, SpO2, ECG (QUAN TRỌNG)",
                "Điều trị rối loạn nhịp tim nếu có: Theo dõi ECG liên tục, điều trị torsades de pointes nếu cần (magnesium IV)",
                "Điều trị co giật nếu có: Benzodiazepine, theo dõi thần kinh chặt chẽ",
                "Điều trị đau gân nếu có: Ngừng ngay, nghỉ ngơi, chườm lạnh, thuốc giảm đau nếu cần",
                "Điều trị hạ đường huyết nếu có: Truyền glucose, theo dõi đường huyết",
                "Điều trị triệu chứng tiêu hóa: Chống nôn nếu cần, truyền dịch nếu mất nước"
            ],
            "monitoring": "Theo dõi dấu hiệu sinh tồn, ECG (QT interval) liên tục, dấu hiệu thần kinh, dấu hiệu gân, đường huyết trong ít nhất 24-48 giờ. Theo dõi lâu hơn nếu có biến chứng (loạn nhịp, co giật, đứt gân)."
        },
        "reversal_agents": {"available": False, "agents": [], "notes": "Không có antidote đặc hiệu. Điều trị chủ yếu là hỗ trợ và điều trị triệu chứng. Ngừng thuốc ngay nếu có triệu chứng đứt gân, QT kéo dài, hoặc co giật."},
        "administration_instructions": {
            "oral": {
                "with_food": "Có thể uống với hoặc không thức ăn. Uống với nước đầy đủ (ít nhất 1-2 ly nước) để tránh kết tinh trong nước tiểu.",
                "timing": "Uống 1 lần/ngày (q24h), cùng một thời điểm mỗi ngày. Cách ít nhất 4 giờ trước hoặc sau khi uống antacid, sucralfate, sắt, kẽm. Không uống cùng lúc với các cation này. Ưu điểm: dùng 1 lần/ngày, không cần điều chỉnh thận."
            },
            "iv": {
                "reconstitution": "Pha với NS hoặc D5W. Nồng độ pha: 1.6mg/ml (tối đa). Pha 400mg trong 250ml dịch = 1.6mg/ml.",
                "infusion_rate": "Truyền trong 60 phút (ít nhất 60 phút). Không truyền quá nhanh. Tốc độ: 250ml/60 phút = ~4.2ml/phút.",
                "compatibility": ["NS (0.9% NaCl)", "D5W (5% Dextrose)"],
                "incompatibility": ["Không trộn với các thuốc khác trong cùng một ống truyền. Kiểm tra tương thích trước khi pha. Tránh pha với cation (Al3+, Mg2+, Ca2+)."],
                "notes": "Theo dõi ECG (QT interval) trước và trong khi truyền. Theo dõi chức năng gan, dấu hiệu gân, thần kinh trong quá trình truyền. Có thể gây kích ứng tĩnh mạch - thay đổi vị trí tiêm nếu cần. Liều: 400mg x 1 lần/ngày (q24h)."
            }
        },
        "pediatric_dosing": {
            "neonates": "CHỐNG CHỈ ĐỊNH ở trẻ <18 tuổi (trừ trường hợp đặc biệt như nhiễm trùng nặng không có lựa chọn khác). Nguy cơ tổn thương sụn, viêm khớp.",
            "infants": "CHỐNG CHỈ ĐỊNH ở trẻ <18 tuổi (trừ trường hợp đặc biệt như nhiễm trùng nặng không có lựa chọn khác). Nguy cơ tổn thương sụn, viêm khớp.",
            "children": "CHỐNG CHỈ ĐỊNH ở trẻ <18 tuổi (trừ trường hợp đặc biệt như nhiễm trùng nặng không có lựa chọn khác). Nếu bắt buộc: 10mg/kg/ngày IV (tối đa 400mg/ngày). Theo dõi chặt chẽ ECG (QT interval), dấu hiệu đau gân, viêm gân. Nguy cơ tổn thương sụn, viêm khớp.",
            "adolescents": "CHỐNG CHỈ ĐỊNH ở trẻ <18 tuổi (trừ trường hợp đặc biệt như nhiễm trùng nặng không có lựa chọn khác). Nếu bắt buộc: liều người lớn (400mg x 1 lần/ngày). Theo dõi chặt chẽ ECG (QT interval), dấu hiệu đau gân, viêm gân.",
            "notes": "CHỐNG CHỈ ĐỊNH ở trẻ <18 tuổi do nguy cơ tổn thương sụn, viêm khớp. Chỉ dùng trong trường hợp đặc biệt như nhiễm trùng nặng (ví dụ: viêm phổi do Streptococcus pneumoniae kháng thuốc) không có lựa chọn khác. Nếu dùng, theo dõi chặt chẽ ECG (QT interval), dấu hiệu đau gân, viêm gân, đứt gân. Ngừng ngay nếu có đau gân hoặc QT kéo dài. Ưu điểm: dùng 1 lần/ngày, không cần điều chỉnh thận."
        },
        "geriatric_dosing": {
            "considerations": "Người cao tuổi (>60 tuổi) có nguy cơ cao hơn đứt gân, viêm gân (đặc biệt gân Achilles), QT kéo dài, rối loạn nhịp tim. Suy gan có thể phổ biến hơn, cần thận trọng.",
            "dose_adjustment": "Không cần điều chỉnh liều ở suy thận (thải qua gan/mật). Thận trọng ở suy gan nặng. Khởi đầu với liều thường dùng (400mg/ngày).",
            "monitoring": "Theo dõi chặt chẽ ECG (QT interval) trước và trong khi dùng. Theo dõi dấu hiệu đau gân, viêm gân, đứt gân (đặc biệt gân Achilles). Theo dõi chức năng gan (ALT, AST). Theo dõi dấu hiệu thần kinh (rối loạn giấc ngủ, nhức đầu). Ngừng ngay nếu có đau gân hoặc QT kéo dài."
        },
        "brand_names": {
            "vietnam": ["Moxifloxacin", "Avelox", "Moxifloxacin Stada"],
            "common": ["Avelox", "Moxifloxacin"]
        },
        "cost_estimate": {
            "unit": "VND",
            "range": "15,000 - 60,000 VND/viên (tùy hàm lượng và thương hiệu)",
            "note": "Giá thay đổi theo thương hiệu và nhà thuốc. Moxifloxacin generic thường rẻ hơn (15,000-40,000 VND/viên 400mg). Avelox (brand) thường đắt hơn (40,000-60,000 VND/viên 400mg). Dạng IV: 100,000-200,000 VND/lọ 400mg."
        },
        "references": {
            "primary_sources": [
                "FDA Drug Label - Moxifloxacin (Avelox)",
                "UpToDate - Moxifloxacin: Drug Information",
                "Medscape - Moxifloxacin Drug Reference",
                "Goodman & Gilman's The Pharmacological Basis of Therapeutics (14th ed)",
                "Lexicomp Online - Moxifloxacin Monograph",
                "Micromedex - Moxifloxacin Drug Information",
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
            "organ_toxicity": {"musculoskeletal": "High (tendon rupture)", "cardiac": "High (QT prolongation)", "neurological": "Moderate", "hepatic": "Moderate"}
        },
        "guideline_tags": [
            "IDSA Guidelines - Community-Acquired Pneumonia",
            "IDSA Guidelines - Complicated Skin and Soft Tissue Infections",
            "IDSA Guidelines - Complicated Intra-abdominal Infections",
            "WHO Essential Medicines List"
        ],
        "last_updated": "2025-02-18",
    },
}

__all__ = ['FLUOROQUINOLONE_ANTIBIOTICS']
