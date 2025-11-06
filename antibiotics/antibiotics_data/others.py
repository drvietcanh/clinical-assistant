"""
Other Antibiotics - Metronidazole, Linezolid, Colistin, etc.
"""

OTHER_ANTIBIOTICS = {
    "Metronidazole": {
        "group": "Nitroimidazole",
        "vietnamese_name": "Metronidazole, Flagyl, Metronidazol, Metrogyl, Trichopol, Metronid, Metro, Flagyl, Klion",
        "administration": ["IV", "PO"],
        "indications": [
            "Nhiễm khuẩn do vi khuẩn kỵ khí",
            "Viêm phúc mạc",
            "Nhiễm khuẩn ổ bụng",
            "Viêm đại tràng giả mạc (C. difficile)",
            "Nhiễm Trichomonas, Giardia, Amebiasis"
        ],
        "contraindications": [
            "Dị ứng metronidazole",
            "Tam cá nguyệt đầu thai kỳ (tránh nếu có thể)"
        ],
        "dosage": {
            "adult_iv": "500mg IV mỗi 8 giờ hoặc 1g IV mỗi 12 giờ",
            "adult_po": "500mg PO x 3 lần/ngày hoặc 1g PO x 2 lần/ngày",
            "adult_cdiff": "500mg PO x 3 lần/ngày x 10-14 ngày",
            "pediatric_iv": "30mg/kg/ngày chia 3 lần",
            "pediatric_po": "30-50mg/kg/ngày chia 3 lần",
            "notes": "Hoạt động tốt chống kỵ khí, đặc biệt B. fragilis"
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "Không đổi",
            "15_30": "Giảm liều 50%",
            "under_15": "Giảm liều 50% hoặc tránh"
        },
        "side_effects": [
            "Vị kim loại, buồn nôn",
            "Nhức đầu",
            "Phản ứng giống disulfiram (nếu uống rượu)",
            "Rối loạn thần kinh ngoại biên (dài ngày)",
            "Nước tiểu sẫm màu (bình thường)"
        ],
        "interactions": [
            "Rượu: phản ứng giống disulfiram (buồn nôn, nôn, đỏ mặt)",
            "Warfarin: tăng nguy cơ chảy máu",
            "Lithium: tăng độc tính lithium",
            "Phenytoin: tăng nồng độ phenytoin"
        ],
        "aware_classification": "ACCESS",
        "pregnancy": "B"
    },

    "Linezolid": {
        "group": "Oxazolidinone",
        "vietnamese_name": "Linezolid, Zyvox, Linezolid",
        "administration": ["IV", "PO"],
        "indications": [
            "Nhiễm khuẩn do MRSA (da, mô mềm, phổi)",
            "Nhiễm khuẩn do VRE",
            "Viêm phổi bệnh viện do MRSA",
            "Nhiễm khuẩn da và mô mềm do MRSA"
        ],
        "contraindications": [
            "Dị ứng linezolid",
            "Dùng MAOIs (cách 2 tuần)",
            "Hội chứng serotonin (khi dùng SSRI/SNRI)"
        ],
        "dosage": {
            "adult_iv": "600mg IV mỗi 12 giờ",
            "adult_po": "600mg PO x 2 lần/ngày",
            "adult_severe": "600mg IV mỗi 12 giờ (không tăng liều)",
            "pediatric_iv": "10mg/kg IV mỗi 8-12 giờ (max 600mg/liều)",
            "pediatric_po": "10mg/kg PO x 2 lần/ngày (max 600mg/liều)",
            "notes": "Thuốc mới, đắt tiền. Chống MRSA/VRE. CẢNH BÁO: Nguy cơ ức chế tủy xương (giảm tiểu cầu) - không dùng >28 ngày"
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "Không đổi",
            "15_30": "Không đổi",
            "under_15": "Không đổi (thải qua gan)"
        },
        "side_effects": [
            "Giảm tiểu cầu (15-30% nếu dùng >14 ngày)",
            "Giảm bạch cầu (hiếm)",
            "Viêm dây thần kinh ngoại vi (dùng kéo dài)",
            "Tăng lactate máu (hiếm nhưng nặng)",
            "Buồn nôn, nôn"
        ],
        "interactions": [
            "SSRI/SNRI: hội chứng serotonin",
            "MAOIs: nguy hiểm",
            "Warfarin: tăng nguy cơ chảy máu",
            "Tyramine-rich foods: tăng huyết áp"
        ],
        "monitoring": "Bắt buộc: Huyết đồ 2 lần/tuần, lactate máu nếu có triệu chứng, ngừng nếu giảm tiểu cầu",
        "aware_classification": "RESERVE",
        "pregnancy": "C"
    },

    "Colistin": {
        "group": "Polypeptide",
        "vietnamese_name": "Colistin, Colistin, Colistimethate",
        "administration": ["IV", "IM", "Inhalation"],
        "indications": [
            "Nhiễm khuẩn do MDR/XDR Gram âm (Pseudomonas, Acinetobacter)",
            "Viêm phổi bệnh viện do MDR",
            "Nhiễm khuẩn huyết do MDR",
            "Khi không còn lựa chọn khác"
        ],
        "contraindications": [
            "Dị ứng colistin",
            "Bệnh nhược cơ (myasthenia gravis)",
            "Suy thận nặng (phải điều chỉnh liều chặt chẽ)"
        ],
        "dosage": {
            "adult_iv_load": "6-9 triệu đơn vị (MU) IV loading, sau đó",
            "adult_iv_maintenance": "4.5-6 MU IV mỗi 12 giờ (theo CrCl)",
            "adult_iv_cmg": "2.5-5mg/kg (theo colistin base) IV mỗi 12 giờ",
            "adult_inhalation": "75-150mg (1-2 MU) x 2-3 lần/ngày",
            "pediatric_iv": "5mg/kg/ngày (theo colistin base) chia 2-3 lần",
            "notes": "Thuốc độc, chỉ dùng cuối cùng khi không còn lựa chọn. Phải tính liều theo CBA (colistin base activity) hoặc MU. Monitor độc thận/độc thần kinh chặt chẽ"
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "Giảm liều 25-50%",
            "15_30": "Giảm liều 50-75%",
            "under_15": "Giảm liều mạnh hoặc tránh"
        },
        "side_effects": [
            "Độc thận (30-50%) - nguy hiểm",
            "Độc thần kinh (paresthesia, rối loạn cảm giác, yếu cơ)",
            "Co giật (hiếm)",
            "Suy hô hấp (neuromuscular blockade)",
            "Viêm tĩnh mạch"
        ],
        "interactions": [
            "Aminoglycosides: tăng độc thận",
            "Neuromuscular blocking agents: tăng tê liệt",
            "Diuretics: tăng độc thận"
        ],
        "monitoring": "Bắt buộc: Creatinine hàng ngày, xét nghiệm thần kinh, cân nhắc TDM",
        "aware_classification": "RESERVE",
        "pregnancy": "C"
    },

    "Daptomycin": {
        "group": "Lipopeptide",
        "vietnamese_name": "Daptomycin, Cubicin, Daptomycin",
        "administration": ["IV"],
        "indications": [
            "Nhiễm khuẩn da và mô mềm do MRSA",
            "Nhiễm khuẩn huyết do MRSA",
            "Viêm nội tâm mạc do MRSA/VRE",
            "Nhiễm khuẩn do VRE (Enterococcus kháng vancomycin)"
        ],
        "contraindications": [
            "Dị ứng daptomycin",
            "Viêm cơ trước đây do daptomycin"
        ],
        "dosage": {
            "adult_skin": "4mg/kg IV x 1 lần/ngày (nhiễm khuẩn da)",
            "adult_bacteremia": "6mg/kg IV x 1 lần/ngày (nhiễm khuẩn huyết)",
            "adult_endocarditis": "6-10mg/kg IV x 1 lần/ngày",
            "adult_obese": "Dựa trên ABW, không dùng cân nặng thực tế",
            "pediatric": "Không khuyến cáo <18 tuổi",
            "notes": "Phải truyền tĩnh mạch chậm (≥30 phút). Monitor CPK hàng tuần!"
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "Giảm liều 25-50% hoặc mỗi 48 giờ",
            "15_30": "Mỗi 48 giờ",
            "under_15": "Mỗi 48 giờ hoặc lọc máu"
        },
        "side_effects": [
            "Viêm cơ (CPK tăng) - nguy hiểm, phải ngừng",
            "Phát ban",
            "Viêm tĩnh mạch",
            "Tiêu chảy"
        ],
        "interactions": [
            "Statins: tăng nguy cơ viêm cơ (ngừng statin khi dùng)",
            "Cyclosporine: tăng nồng độ daptomycin"
        ],
        "monitoring": "Bắt buộc: CPK hàng tuần, ngừng nếu CPK >5x ULN hoặc có triệu chứng viêm cơ",
        "aware_classification": "RESERVE",
        "pregnancy": "B"
    },

    "Fosfomycin": {
        "group": "Phosphonic Acid",
        "vietnamese_name": "Fosfomycin, Fosfomycin, Monuril",
        "administration": ["IV", "PO"],
        "indications": [
            "Nhiễm khuẩn đường tiết niệu không biến chứng (PO)",
            "Nhiễm khuẩn đường tiết niệu phức tạp (IV)",
            "Nhiễm khuẩn do MDR Gram âm (kết hợp)",
            "Viêm bể thận cấp"
        ],
        "contraindications": [
            "Dị ứng fosfomycin",
            "Suy thận nặng (CrCl < 10) - IV"
        ],
        "dosage": {
            "adult_po_uti": "3g PO x 1 liều (nhiễm khuẩn tiết niệu đơn giản)",
            "adult_iv": "12-24g IV chia 3-4 lần/ngày (nhiễm khuẩn nặng)",
            "adult_iv_severe": "12g IV mỗi 8 giờ hoặc 16g IV mỗi 8 giờ",
            "pediatric_po": "Không dùng <12 tuổi",
            "pediatric_iv": "200-300mg/kg/ngày chia 3-4 lần",
            "notes": "PO: liều đơn cho UTI. IV: dùng cho nhiễm khuẩn nặng, thường kết hợp"
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "Giảm liều 25-50%",
            "15_30": "Giảm liều 50%",
            "under_15": "Giảm liều mạnh hoặc tránh (IV)"
        },
        "side_effects": [
            "Tiêu chảy",
            "Buồn nôn, nôn",
            "Phát ban",
            "Viêm tĩnh mạch (IV)",
            "Tăng transaminase"
        ],
        "interactions": [
            "Metoclopramide: giảm nồng độ fosfomycin PO",
            "Cần cách 2 giờ trước uống"
        ],
        "aware_classification": "WATCH",
        "pregnancy": "B"
    },

    "Aztreonam": {
        "group": "Beta-lactam - Monobactam",
        "vietnamese_name": "Aztreonam, Azactam, Aztreonam",
        "administration": ["IV", "IM"],
        "indications": [
            "Nhiễm khuẩn do Pseudomonas",
            "Nhiễm khuẩn do Gram âm",
            "Dị ứng penicillin nặng (an toàn, không phản ứng chéo)",
            "Viêm phổi bệnh viện",
            "Nhiễm khuẩn ổ bụng"
        ],
        "contraindications": [
            "Dị ứng aztreonam",
            "Không hoạt động chống Gram dương và kỵ khí"
        ],
        "dosage": {
            "adult_iv": "1-2g IV mỗi 6-8 giờ",
            "adult_im": "1g IM mỗi 8 giờ",
            "adult_severe": "2g IV mỗi 6-8 giờ",
            "pediatric": "90-120mg/kg/ngày chia 3-4 lần (max 8g/ngày)",
            "notes": "An toàn cho người dị ứng penicillin (không phản ứng chéo). Chỉ hoạt động chống Gram âm"
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "Giảm liều 25-50%",
            "15_30": "Giảm liều 50%",
            "under_15": "Giảm liều mạnh hoặc lọc máu"
        },
        "side_effects": [
            "Phát ban",
            "Tiêu chảy",
            "Viêm tĩnh mạch",
            "Đau tại chỗ tiêm (IM)"
        ],
        "interactions": [
            "Warfarin: tăng nguy cơ chảy máu",
            "Probenecid: tăng nồng độ"
        ],
        "aware_classification": "WATCH",
        "pregnancy": "B"
    },

    "Trimethoprim-Sulfamethoxazole": {
        "group": "Sulfonamide",
        "vietnamese_name": "Trimethoprim-Sulfamethoxazole, Bactrim, Cotrimoxazol",
        "administration": ["IV", "PO"],
        "indications": [
            "Nhiễm khuẩn đường tiết niệu",
            "Nhiễm khuẩn đường hô hấp (Pneumocystis jirovecii)",
            "Nhiễm khuẩn do MRSA",
            "Nhiễm khuẩn da và mô mềm",
            "Nhiễm Toxoplasma (kết hợp)"
        ],
        "contraindications": [
            "Dị ứng sulfonamide",
            "Thiếu G6PD (tan máu)",
            "Suy thận nặng (CrCl < 15)",
            "Suy gan nặng",
            "Tam cá nguyệt cuối thai kỳ (kernicterus)"
        ],
        "dosage": {
            "adult_iv": "8-10mg/kg (theo TMP) IV mỗi 6-12 giờ",
            "adult_po_standard": "160/800mg (1 viên DS) PO x 2 lần/ngày",
            "adult_po_pcp": "15-20mg/kg (theo TMP) PO mỗi 6-8 giờ",
            "adult_mrsa": "160/800mg PO x 2-4 lần/ngày",
            "pediatric_iv": "8-10mg/kg (theo TMP) IV mỗi 6-12 giờ",
            "pediatric_po": "8-10mg/kg (theo TMP) PO x 2 lần/ngày",
            "notes": "Tỷ lệ 1:5 (TMP:Sulfa). IV: truyền chậm ≥60 phút"
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "Giảm liều 50%",
            "15_30": "Tránh hoặc giảm liều mạnh",
            "under_15": "Chống chỉ định"
        },
        "side_effects": [
            "Phát ban, Stevens-Johnson (nguy hiểm)",
            "Giảm bạch cầu, giảm tiểu cầu",
            "Tan máu (thiếu G6PD)",
            "Tăng K+ máu (đặc biệt suy thận)",
            "Tăng creatinine (tăng creatinine không phải suy thận thật)"
        ],
        "interactions": [
            "Warfarin: tăng nguy cơ chảy máu mạnh",
            "Methotrexate: tăng độc tính",
            "ACE inhibitors: tăng K+ máu",
            "Phenytoin: tăng nồng độ phenytoin"
        ],
        "aware_classification": "ACCESS",
        "pregnancy": "D - Kernicterus ở tam cá nguyệt cuối"
    },

    "Chloramphenicol": {
        "group": "Phenicol",
        "vietnamese_name": "Chloramphenicol, Chloramphenicol, Cloran",
        "administration": ["IV", "PO"],
        "indications": [
            "Viêm màng não do H. influenzae (khi ampicillin kháng)",
            "Nhiễm khuẩn do Salmonella typhi (sốt thương hàn)",
            "Nhiễm khuẩn do vi khuẩn kỵ khí",
            "Nhiễm khuẩn mắt (tại chỗ)"
        ],
        "contraindications": [
            "Dị ứng chloramphenicol",
            "Suy gan nặng",
            "Suy thận nặng"
        ],
        "dosage": {
            "adult_iv": "50-100mg/kg/ngày chia 4 lần (max 4g/ngày)",
            "adult_po": "50mg/kg/ngày chia 4 lần",
            "adult_meningitis": "100mg/kg/ngày chia 4 lần",
            "pediatric": "50-75mg/kg/ngày chia 4 lần",
            "pediatric_meningitis": "75-100mg/kg/ngày chia 4 lần",
            "notes": "Thuốc độc, chỉ dùng khi thực sự cần. Monitor huyết đồ chặt chẽ"
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "Giảm liều 25-50%",
            "15_30": "Giảm liều 50%",
            "under_15": "Tránh"
        },
        "side_effects": [
            "Suy tủy xương (hiếm nhưng nặng - aplastic anemia)",
            "Gray baby syndrome (trẻ sơ sinh - ngừng tim mạch)",
            "Giảm bạch cầu, giảm tiểu cầu",
            "Tăng transaminase"
        ],
        "interactions": [
            "Warfarin: tăng nguy cơ chảy máu",
            "Phenytoin: tăng nồng độ phenytoin",
            "Paracetamol: tăng độc tính"
        ],
        "monitoring": "Bắt buộc: Huyết đồ 2 lần/tuần, ngừng nếu giảm bạch cầu/tiểu cầu",
        "aware_classification": "ACCESS",
        "pregnancy": "C"
    },

    "Quinupristin-Dalfopristin": {
        "group": "Streptogramin",
        "vietnamese_name": "Quinupristin-Dalfopristin, Synercid, Quinupristin-Dalfopristin",
        "administration": ["IV"],
        "indications": [
            "Nhiễm khuẩn do VRE (Enterococcus faecium)",
            "Nhiễm khuẩn da và mô mềm do MRSA",
            "Nhiễm khuẩn do MRSA khi vancomycin thất bại"
        ],
        "contraindications": [
            "Dị ứng streptogramin",
            "Suy gan nặng"
        ],
        "dosage": {
            "adult_standard": "7.5mg/kg IV mỗi 8-12 giờ",
            "adult_severe": "7.5mg/kg IV mỗi 8 giờ",
            "pediatric": "7.5mg/kg IV mỗi 8-12 giờ",
            "notes": "Thuốc mới, đắt tiền. Chỉ hoạt động chống Enterococcus faecium (VRE), không hoạt động chống E. faecalis. Phải truyền qua central line"
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "Không đổi",
            "15_30": "Không đổi",
            "under_15": "Không đổi (thải qua gan)"
        },
        "side_effects": [
            "Viêm tĩnh mạch (thường gặp - phải dùng central line)",
            "Đau khớp, đau cơ (arthralgia, myalgia)",
            "Phát ban",
            "Tăng bilirubin, transaminase",
            "Buồn nôn, nôn"
        ],
        "interactions": [
            "Cyclosporine: tăng nồng độ cyclosporine",
            "CYP3A4 substrates: tăng nồng độ"
        ],
        "aware_classification": "RESERVE",
        "pregnancy": "B"
    },

    "Polymyxin B": {
        "group": "Polymyxin",
        "vietnamese_name": "Polymyxin B, Polymyxin B",
        "administration": ["IV", "IM", "Topical"],
        "indications": [
            "Nhiễm khuẩn do MDR/XDR Gram âm (cuối cùng)",
            "P. aeruginosa, Acinetobacter MDR",
            "Klebsiella MDR (KPC)",
            "Khi không còn lựa chọn khác"
        ],
        "contraindications": [
            "Dị ứng polymyxin",
            "Nhược cơ (myasthenia gravis)",
            "Suy thận nặng (thận trọng)"
        ],
        "dosage": {
            "adult_iv": "15,000-25,000 đơn vị/kg/ngày chia 2 lần",
            "adult_iv_standard": "2.5mg/kg/ngày (theo colistin base) chia 2 lần",
            "adult_topical": "Dùng ngoài da, không dùng toàn thân",
            "notes": "Rất độc. Chỉ dùng khi không còn lựa chọn. Đơn vị: 1mg ≈ 10,000 đơn vị"
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "Giảm liều 25-50%",
            "15_30": "Giảm liều 50-75%",
            "under_15": "Giảm liều mạnh hoặc tránh"
        },
        "side_effects": [
            "Độc thận (30-50%)",
            "Độc thần kinh (paresthesia, rối loạn cảm giác)",
            "Co giật",
            "Suy hô hấp (neuromuscular blockade)"
        ],
        "interactions": [
            "Aminoglycosides: tăng độc thận",
            "Neuromuscular blocking agents: tăng tê liệt",
            "Diuretics: tăng độc thận"
        ],
        "monitoring": "Bắt buộc: Creatinine hàng ngày, xét nghiệm thần kinh",
        "aware_classification": "RESERVE",
        "pregnancy": "C"
    },

    "Rifampin": {
        "group": "Rifamycin - Anti-tuberculosis/Anti-staphylococcal",
        "vietnamese_name": "Rifampin, Rifampicin, Rimactan",
        "administration": ["IV", "PO"],
        "indications": [
            "Lao (TB) - phác đồ chuẩn (kết hợp)",
            "Nhiễm khuẩn do MSSA/MRSA - liệu pháp kết hợp",
            "Nhiễm khuẩn do S. epidermidis (prosthetic devices)",
            "Prophylaxis viêm màng não do H. influenzae, N. meningitidis",
            "Brucellosis (kết hợp doxycycline)"
        ],
        "contraindications": [
            "Dị ứng rifampin/rifamycin",
            "Viêm gan cấp",
            "Suy gan nặng",
            "Dùng đơn độc (dễ kháng thuốc)"
        ],
        "dosage": {
            "adult_iv": "600mg IV mỗi 12-24 giờ",
            "adult_po": "600mg PO mỗi 24 giờ (nên uống lúc đói)",
            "pediatric_iv": "10-20mg/kg/ngày (tối đa 600mg) chia 1-2 lần",
            "pediatric_po": "10-20mg/kg/ngày (tối đa 600mg) 1 lần/ngày",
            "tb_po": "600mg PO mỗi 24 giờ (phối hợp với isoniazid, pyrazinamide, ethambutol)",
            "mrsa_po": "600mg PO mỗi 12 giờ (phối hợp vancomycin/daptomycin)",
            "notes": "Nước tiểu, mồ hôi, nước bọt, nước mắt màu đỏ cam. Uống lúc đói để hấp thu tốt nhất"
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "Không đổi",
            "15_30": "Giảm liều 25-50% nếu suy gan kèm theo",
            "under_15": "Giảm liều 25-50% nếu suy gan kèm theo"
        },
        "side_effects": [
            "Đỏ da, nước tiểu màu đỏ cam (bình thường)",
            "Viêm gan (tăng transaminase)",
            "Giảm tiểu cầu",
            "Giảm bạch cầu",
            "Phản ứng quá mẫn (sốt, phát ban)",
            "Phản ứng giống cúm",
            "Tiêu chảy, buồn nôn"
        ],
        "interactions": [
            "Warfarin: giảm tác dụng (tăng CYP450)",
            "Oral contraceptives: giảm hiệu quả",
            "HIV protease inhibitors: giảm nồng độ",
            "Nhiều thuốc khác: rifampin là chất cảm ứng mạnh CYP450"
        ],
        "monitoring": "LFT (AST/ALT, bilirubin), công thức máu, nước tiểu màu đỏ cam là bình thường",
        "aware_classification": "WATCH",
        "pregnancy": "C - An toàn cho TB (phối hợp với isoniazid, pyrazinamide)",
        "notes": "Chất cảm ứng mạnh CYP450 - tương tác với nhiều thuốc. Màu đỏ cam nước tiểu là bình thường"
    },

    "Tedizolid": {
        "group": "Oxazolidinone",
        "vietnamese_name": "Tedizolid, Sivextro",
        "administration": ["IV", "PO"],
        "indications": [
            "Nhiễm khuẩn da và mô mềm do vi khuẩn gram dương",
            "MRSA (Methicillin-Resistant S. aureus)",
            "VRE (Vancomycin-Resistant Enterococcus)",
            "Nhiễm khuẩn do Streptococcus",
            "Thay thế Linezolid (tác dụng tương tự, ít tác dụng phụ hơn)"
        ],
        "contraindications": [
            "Dị ứng tedizolid/linezolid",
            "Dùng MAO inhibitors trong vòng 14 ngày",
            "Serotonin syndrome risk với SSRI"
        ],
        "dosage": {
            "adult_iv": "200mg IV mỗi 24 giờ (liều cố định)",
            "adult_po": "200mg PO mỗi 24 giờ (liều cố định)",
            "pediatric_iv": "6mg/kg/ngày IV (tối đa 200mg) mỗi 24 giờ",
            "pediatric_po": "6mg/kg/ngày PO (tối đa 200mg) mỗi 24 giờ",
            "notes": "Liều cố định, không cần điều chỉnh theo cân nặng/thận. IV và PO tương đương sinh học"
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "Không đổi (liều cố định)",
            "15_30": "Không đổi (liều cố định)",
            "under_15": "Không đổi (liều cố định, có thể dùng)"
        },
        "side_effects": [
            "Ức chế tủy xương (giảm bạch cầu, tiểu cầu) - ít hơn Linezolid",
            "Viêm dây thần kinh thị giác",
            "Ức chế MAO (tương tác với tyramine)",
            "Tiêu chảy, buồn nôn",
            "Đau đầu"
        ],
        "interactions": [
            "MAO inhibitors: chống chỉ định (serotonin syndrome)",
            "SSRI/SNRI: tăng nguy cơ serotonin syndrome",
            "Tyramine (thức ăn lên men): tăng huyết áp",
            "Warfarin: tăng nguy cơ chảy máu"
        ],
        "monitoring": "Công thức máu (WBC, platelet), thị lực, dấu hiệu serotonin syndrome",
        "aware_classification": "RESERVE",
        "pregnancy": "C - Dữ liệu hạn chế, cân nhắc lợi ích/nguy cơ",
        "notes": "Thay thế Linezolid với ưu điểm: liều cố định, ít tác dụng phụ tủy xương hơn, dùng 1 lần/ngày"
    },

}

__all__ = ['OTHER_ANTIBIOTICS']
