"""
Pain Reliever + Muscle Relaxant Combination Drugs
Fixed-dose combinations for musculoskeletal pain with muscle spasm
"""

PAIN_MUSCLE_RELAXANT_COMBINATIONS_DRUGS = {
    "Aspirin/Carisoprodol":     {
        "group": "Analgesic - Combination (NSAID + Muscle Relaxant)",
        "vietnamese_name": "Aspirin/Carisoprodol, Soma Compound",
        "administration": [
            "PO"
    ],
        "indications": [
            "Đau cơ xương khớp kèm co thắt cơ và viêm (musculoskeletal pain with muscle spasm and inflammation)",
            "Đau lưng cấp tính",
            "Đau cơ sau chấn thương"
    ],
        "contraindications": {
            "tuyệt_đối": [
                "Dị ứng aspirin hoặc carisoprodol",
                "Loét dạ dày tá tràng đang hoạt động",
                "Suy thận nặng",
                "Suy gan nặng",
                "Porphyria",
                "Dị ứng với meprobamate",
                "Dùng warfarin hoặc thuốc chống đông khác"
    ],
            "tương_đối": [
                "Suy thận trung bình - thận trọng, giảm liều",
                "Suy gan trung bình - thận trọng",
                "Tiền sử nghiện/lạm dụng chất - tăng nguy cơ nghiện"
    ],
        },
        "dosage": {
            "adult_standard": "Aspirin 325mg/Carisoprodol 200mg x 3-4 lần/ngày",
            "adult_max": "Aspirin 4g/ngày, Carisoprodol 1400mg/ngày",
            "notes": """CHỈ dùng ngắn hạn (2-3 tuần). Aspirin có tác dụng chống kết tập tiểu cầu. Carisoprodol chuyển hóa thành meprobamate (controlled substance, nguy cơ nghiện).""",
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "Thận trọng, giảm liều",
            "under_30": "Tránh dùng",
        },
        "side_effects": [
            "Chảy máu dạ dày (do aspirin)",
            "Loét dạ dày",
            "Buồn ngủ (do carisoprodol)",
            "Chóng mặt",
            "Nguy cơ nghiện/lệ thuộc (do meprobamate)",
            "Ù tai (liều cao aspirin)",
            "Hội chứng cai khi ngừng carisoprodol"
    ],
        "interactions": [
            "Warfarin: tăng nguy cơ chảy máu nặng",
            "Alcohol: tăng tác dụng an thần, tăng nguy cơ chảy máu dạ dày",
            "CNS depressants: tăng tác dụng ức chế",
            "CYP2C19 inhibitors: tăng nồng độ carisoprodol"
    ],
        "pregnancy": "C - D trong 3 tháng cuối",
        "mechanism_of_action": """Kết hợp aspirin (NSAID, giảm đau, chống viêm, chống kết tập tiểu cầu) và carisoprodol (giãn cơ xương khớp). Aspirin ức chế COX-1 và COX-2, giảm đau, chống viêm, và chống kết tập tiểu cầu (ức chế không hồi phục COX-1 tiểu cầu). Carisoprodol là thuốc giãn cơ xương khớp, chuyển hóa thành meprobamate (controlled substance, có nguy cơ nghiện). Tác dụng hiệp đồng: giảm đau cơ xương khớp kèm viêm và co thắt cơ. CHỈ dùng ngắn hạn (2-3 tuần).""",
        "monitoring": [
            "Đáp ứng điều trị: giảm đau, giảm viêm, giảm co thắt cơ",
            "Dấu hiệu chảy máu dạ dày (phân đen, nôn ra máu, đau bụng)",
            "Dấu hiệu nghiện/lệ thuộc (do meprobamate)",
            "Dấu hiệu quá liều aspirin (ù tai, chóng mặt)"
    ],
        "precautions": [
            "CHỈ dùng ngắn hạn (2-3 tuần)",
            "NGUY CƠ CHẢY MÁU DẠ DÀY - do aspirin, uống với thức ăn hoặc sữa",
            "CHỐNG CHỈ ĐỊNH với warfarin hoặc thuốc chống đông khác - tăng nguy cơ chảy máu nặng",
            "NGUY CƠ NGHIỆN/LỆ THUỘC - do meprobamate (controlled substance)",
            "Tránh rượu - tăng tác dụng an thần, tăng nguy cơ chảy máu dạ dày",
            "Thận trọng ở suy thận, suy gan",
            "Thận trọng ở bệnh nhân có tiền sử nghiện/lạm dụng chất"
    ],
        "pharmacokinetics": {
            "half_life": "2-3 giờ (aspirin), 2 giờ (carisoprodol), 10 giờ (meprobamate)",
            "onset": "30 phút",
            "duration": "4-6 giờ",
            "protein_binding": "80-90% (aspirin), không đáng kể (carisoprodol)",
            "clearance": "Gan: chuyển hóa. Thận: thải trừ.",
        },
        "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm. Controlled substance - cần bảo quản an toàn.",
        "black_box_warnings": """NGUY CƠ NGHIỆN, LẠM DỤNG, VÀ LỆ THUỘC - carisoprodol chuyển hóa thành meprobamate (controlled substance). Nguy cơ chảy máu dạ dày nặng với aspirin. CHỐNG CHỈ ĐỊNH với warfarin hoặc thuốc chống đông khác. Chỉ dùng ngắn hạn (2-3 tuần).""",
        "drug_interactions": {
            "major": [
    {
                    "drug": "Warfarin, các thuốc chống đông khác",
                    "mechanism": "Aspirin ức chế COX-1 tiểu cầu, tăng nguy cơ chảy máu",
                    "effect": "Tăng nguy cơ chảy máu nặng, tăng INR",
                    "management": "CHỐNG CHỈ ĐỊNH. Tránh dùng cùng. Nếu phải dùng, theo dõi INR thường xuyên.",
                },
    {
                    "drug": "Alcohol",
                    "mechanism": "Tăng tác dụng ức chế CNS, tăng nguy cơ chảy máu dạ dày",
                    "effect": "Tăng buồn ngủ, tăng nguy cơ chảy máu dạ dày nặng",
                    "management": "TRÁNH RƯỢU hoàn toàn khi dùng thuốc này.",
                }
                ],
            "moderate": [
    {
                    "drug": "CNS depressants (Benzodiazepines, Opioids)",
                    "mechanism": "Tăng tác dụng ức chế CNS",
                    "effect": "Tăng buồn ngủ, nguy cơ ức chế hô hấp",
                    "management": "Thận trọng. Giảm liều nếu cần.",
                }
                ],
            "minor": [],
        },
        "pregnancy_lactation": {
            "fda_category": "C - D trong 3 tháng cuối",
            "pregnancy_details": """Category C trong 3 tháng đầu-2. Category D trong 3 tháng cuối - CHỐNG CHỈ ĐỊNH. Aspirin trong 3 tháng cuối có thể gây đóng ống động mạch sớm, thiểu ối. Có thể dùng trong 3 tháng đầu-2 nếu lợi ích > nguy cơ.""",
            "lactation": {
                "safety": "Caution",
                "details": "Aspirin và carisoprodol đều bài tiết vào sữa mẹ. Có thể gây tác dụng phụ ở trẻ.",
                "recommendation": "Thận trọng khi cho con bú. Không khuyến cáo dùng aspirin khi cho con bú, đặc biệt liều cao.",
            },
        },
        "hepatic_adjustment": {
            "mild": "Không đổi",
            "moderate": "Thận trọng",
            "severe": "CHỐNG CHỈ ĐỊNH",
            "notes": "Cả hai thuốc đều chuyển hóa ở gan. Suy gan nặng là chống chỉ định.",
        },
        "overdose_management": {
            "symptoms": [
                "Aspirin quá liều: ù tai, chóng mặt, buồn nôn, nôn, tăng thông khí, kiềm hô hấp, toan chuyển hóa",
                "Carisoprodol quá liều: buồn ngủ nặng, ức chế hô hấp, hôn mê"
    ],
            "antidote": "Không có antidote đặc hiệu. Điều trị hỗ trợ.",
            "treatment": [
                "Đánh giá đường thở, hô hấp, tuần hoàn",
                "Rửa dạ dày nếu trong vòng 1-2 giờ",
                "Than hoạt tính",
                "Nếu aspirin quá liều: kiềm hóa nước tiểu (sodium bicarbonate), điều chỉnh điện giải",
                "Hỗ trợ hô hấp nếu cần",
                "Theo dõi nồng độ salicylat máu (nếu aspirin quá liều)"
    ],
            "monitoring": """Theo dõi ý thức, hô hấp, tim mạch. Nếu aspirin quá liều: theo dõi nồng độ salicylat máu, khí máu, điện giải.""",
        },
        "reversal_agents": {
            "available": False,
            "agents": [],
        },
        "administration_instructions": {
            "oral": {
                "with_food": "Uống với thức ăn hoặc sữa để giảm kích ứng dạ dày (aspirin)",
                "timing": """Aspirin 325mg/Carisoprodol 200mg x 3-4 lần/ngày. CHỈ dùng ngắn hạn (2-3 tuần). Uống với thức ăn để giảm kích ứng dạ dày.""",
            },
        },
        "references": {
            "primary_sources": [
                "FDA Drug Label - Soma Compound (Aspirin/Carisoprodol)",
                "UpToDate - Muscle relaxants: Drug information",
                "UpToDate - Aspirin: Drug information"
    ],
            "last_updated": "2025-02-18",
            "evidence_level": "High - FDA-approved, controlled substance",
        },
            "risk_flags": {
                "high_alert": False,
                "narrow_therapeutic_index": False,
                "bleeding_risk": False,
                "organ_toxicity": [],
                "qt_prolongation": False,
                "hepatotoxicity": False,
                "nephrotoxicity": False,
                "requires_monitoring": [],
            },
            "guideline_tags": [
                "FDA Drug Information",
                "UpToDate Drug Information",
            ]
    },
    "Paracetamol/Carisoprodol":     {
        "group": "Analgesic - Combination (Paracetamol + Muscle Relaxant)",
        "vietnamese_name": "Paracetamol/Carisoprodol, Soma Compound",
        "administration": [
            "PO"
    ],
        "indications": [
            "Đau cơ xương khớp kèm co thắt cơ (musculoskeletal pain with muscle spasm)",
            "Đau lưng cấp tính",
            "Đau cơ sau chấn thương"
    ],
        "contraindications": {
            "tuyệt_đối": [
                "Dị ứng paracetamol hoặc carisoprodol",
                "Suy gan nặng",
                "Porphyria",
                "Dị ứng với meprobamate"
    ],
            "tương_đối": [
                "Suy gan trung bình - thận trọng",
                "Tiền sử nghiện/lạm dụng chất - tăng nguy cơ nghiện"
    ],
        },
        "dosage": {
            "adult_standard": "Paracetamol 325mg/Carisoprodol 250mg x 3-4 lần/ngày",
            "adult_max": "Paracetamol 4g/ngày, Carisoprodol 1400mg/ngày",
            "notes": """CHỈ dùng ngắn hạn (2-3 tuần). Carisoprodol chuyển hóa thành meprobamate (controlled substance, nguy cơ nghiện).""",
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "Thận trọng",
            "under_30": "Thận trọng",
        },
        "side_effects": [
            "Buồn ngủ (do carisoprodol)",
            "Chóng mặt",
            "Đau đầu",
            "Nguy cơ nghiện/lệ thuộc (do meprobamate từ carisoprodol)",
            "Độc gan (do paracetamol - nếu quá liều)",
            "Hội chứng cai khi ngừng carisoprodol"
    ],
        "interactions": [
            "Alcohol: tăng tác dụng an thần, tăng nguy cơ độc gan (paracetamol)",
            "Warfarin: tăng nguy cơ chảy máu (paracetamol)",
            "CNS depressants: tăng tác dụng ức chế",
            "CYP2C19 inhibitors: tăng nồng độ carisoprodol"
    ],
        "pregnancy": "C",
        "mechanism_of_action": """Kết hợp paracetamol (giảm đau, hạ sốt) và carisoprodol (giãn cơ xương khớp). Paracetamol ức chế COX-3 ở CNS, giảm đau và hạ sốt. Carisoprodol là thuốc giãn cơ xương khớp, chuyển hóa thành meprobamate (controlled substance, có nguy cơ nghiện). Tác dụng hiệp đồng: giảm đau cơ xương khớp kèm co thắt cơ. CHỈ dùng ngắn hạn (2-3 tuần).""",
        "monitoring": [
            "Đáp ứng điều trị: giảm đau, giảm co thắt cơ",
            "Dấu hiệu nghiện/lệ thuộc (do meprobamate)",
            "Chức năng gan (nếu dùng >4g paracetamol/ngày)",
            "Dấu hiệu quá liều paracetamol (buồn nôn, đau bụng, vàng da)"
    ],
        "precautions": [
            "CHỈ dùng ngắn hạn (2-3 tuần)",
            "NGUY CƠ NGHIỆN/LỆ THUỘC - do meprobamate (controlled substance)",
            "Không vượt quá 4g paracetamol/ngày - nguy cơ độc gan",
            "Tránh rượu - tăng tác dụng an thần, tăng nguy cơ độc gan",
            "Thận trọng ở suy gan - chống chỉ định paracetamol ở suy gan nặng",
            "Thận trọng ở bệnh nhân có tiền sử nghiện/lạm dụng chất"
    ],
        "pharmacokinetics": {
            "half_life": "1-3 giờ (paracetamol), 2 giờ (carisoprodol), 10 giờ (meprobamate)",
            "onset": "30 phút",
            "duration": "4-6 giờ",
            "protein_binding": "10-25% (paracetamol), không đáng kể (carisoprodol)",
            "clearance": "Gan: chuyển hóa paracetamol và carisoprodol. Thận: thải trừ.",
        },
        "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm. Controlled substance - cần bảo quản an toàn.",
        "black_box_warnings": """NGUY CƠ NGHIỆN, LẠM DỤNG, VÀ LỆ THUỘC - carisoprodol chuyển hóa thành meprobamate (controlled substance). Nguy cơ độc gan nghiêm trọng với paracetamol nếu quá liều (>4g/ngày). Chỉ dùng ngắn hạn (2-3 tuần).""",
        "drug_interactions": {
            "major": [
    {
                    "drug": "Alcohol",
                    "mechanism": "Tăng tác dụng ức chế CNS, tăng nguy cơ độc gan (paracetamol)",
                    "effect": "Tăng buồn ngủ, tăng nguy cơ độc gan nặng",
                    "management": "TRÁNH RƯỢU hoàn toàn khi dùng thuốc này.",
                },
    {
                    "drug": "Warfarin",
                    "mechanism": "Paracetamol có thể tăng tác dụng warfarin",
                    "effect": "Tăng INR, tăng nguy cơ chảy máu",
                    "management": "Thận trọng. Theo dõi INR thường xuyên.",
                }
                ],
            "moderate": [
    {
                    "drug": "CNS depressants (Benzodiazepines, Opioids)",
                    "mechanism": "Tăng tác dụng ức chế CNS",
                    "effect": "Tăng buồn ngủ, nguy cơ ức chế hô hấp",
                    "management": "Thận trọng. Giảm liều nếu cần.",
                },
    {
                    "drug": "CYP2C19 inhibitors (Omeprazole, Fluoxetine)",
                    "mechanism": "Ức chế chuyển hóa carisoprodol",
                    "effect": "Tăng nồng độ carisoprodol",
                    "management": "Thận trọng. Có thể cần giảm liều.",
                }
                ],
            "minor": [],
        },
        "pregnancy_lactation": {
            "fda_category": "C",
            "pregnancy_details": "Category C. Có thể dùng nếu lợi ích > nguy cơ.",
            "lactation": {
                "safety": "Caution",
                "details": "Paracetamol và carisoprodol đều bài tiết vào sữa mẹ. Có thể gây tác dụng phụ ở trẻ.",
                "recommendation": "Thận trọng khi cho con bú.",
            },
        },
        "hepatic_adjustment": {
            "mild": "Thận trọng",
            "moderate": "Thận trọng, giảm liều",
            "severe": "CHỐNG CHỈ ĐỊNH",
            "notes": "Paracetamol chuyển hóa ở gan, nguy cơ độc gan. Suy gan nặng là chống chỉ định.",
        },
        "overdose_management": {
            "symptoms": [
                "Paracetamol quá liều: buồn nôn, nôn, đau bụng, vàng da (sau 24-48 giờ), suy gan",
                "Carisoprodol quá liều: buồn ngủ nặng, ức chế hô hấp, hôn mê"
    ],
            "antidote": "N-acetylcysteine (NAC) cho paracetamol quá liều. Không có antidote cho carisoprodol.",
            "treatment": [
                "Nếu quá liều paracetamol (>150mg/kg hoặc >10g): N-acetylcysteine (NAC) ngay lập tức",
                "Đánh giá đường thở, hô hấp, tuần hoàn",
                "Rửa dạ dày nếu trong vòng 1-2 giờ",
                "Than hoạt tính",
                "Hỗ trợ hô hấp nếu cần",
                "Theo dõi chức năng gan (paracetamol quá liều)"
    ],
            "monitoring": """Theo dõi ý thức, hô hấp, tim mạch. Nếu paracetamol quá liều: theo dõi chức năng gan (ALT, AST, bilirubin), INR.""",
        },
        "reversal_agents": {
            "available": True,
            "agents": [
    {
                    "agent": "N-acetylcysteine (NAC)",
                    "mechanism": "Chống độc cho paracetamol quá liều",
                    "indication": "Quá liều paracetamol (>150mg/kg hoặc >10g)",
                    "dose": "Theo phác đồ điều trị quá liều paracetamol",
                    "caution": "Chỉ hiệu quả nếu dùng trong vòng 8-10 giờ sau khi uống paracetamol",
                }
                ],
        },
        "administration_instructions": {
            "oral": {
                "with_food": "Có thể uống với thức ăn hoặc không. Uống với thức ăn có thể giảm kích ứng dạ dày.",
                "timing": """Paracetamol 325mg/Carisoprodol 250mg x 3-4 lần/ngày. CHỈ dùng ngắn hạn (2-3 tuần). KHÔNG vượt quá 4g paracetamol/ngày.""",
            },
        },
        "references": {
            "primary_sources": [
                "FDA Drug Label - Soma Compound (Paracetamol/Carisoprodol)",
                "UpToDate - Muscle relaxants: Drug information"
    ],
            "last_updated": "2025-02-18",
            "evidence_level": "High - FDA-approved, controlled substance",
        },
            "risk_flags": {
                "high_alert": False,
                "narrow_therapeutic_index": False,
                "bleeding_risk": False,
                "organ_toxicity": [],
                "qt_prolongation": False,
                "hepatotoxicity": False,
                "nephrotoxicity": False,
                "requires_monitoring": [],
            },
            "guideline_tags": [
                "FDA Drug Information",
                "UpToDate Drug Information",
            ]
    },
    "Paracetamol/Chlorzoxazone":     {
        "group": "Analgesic - Combination (Paracetamol + Muscle Relaxant)",
        "vietnamese_name": "Paracetamol/Chlorzoxazone, Chlorzoxazone Compound",
        "administration": [
            "PO"
    ],
        "indications": [
            "Đau cơ xương khớp kèm co thắt cơ (musculoskeletal pain with muscle spasm)",
            "Đau lưng cấp tính",
            "Đau cơ sau chấn thương"
    ],
        "contraindications": {
            "tuyệt_đối": [
                "Dị ứng paracetamol hoặc chlorzoxazone",
                "Suy gan nặng"
    ],
            "tương_đối": [
                "Suy gan trung bình - thận trọng, tránh dùng nếu có thể",
                "Bệnh gan - tăng nguy cơ độc gan"
    ],
        },
        "dosage": {
            "adult_standard": "Paracetamol 325mg/Chlorzoxazone 250mg x 3-4 lần/ngày",
            "adult_max": "Paracetamol 4g/ngày, Chlorzoxazone 1500mg/ngày",
            "notes": "CHỈ dùng ngắn hạn. Chlorzoxazone có thể gây nước tiểu màu cam/đỏ (vô hại).",
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "Thận trọng",
            "under_30": "Thận trọng",
        },
        "side_effects": [
            "Buồn ngủ",
            "Chóng mặt",
            "Mệt mỏi",
            "Nước tiểu màu cam/đỏ (vô hại - do chlorzoxazone)",
            "Độc gan (do paracetamol - nếu quá liều)",
            "Độc gan (do chlorzoxazone - hiếm nhưng nghiêm trọng)"
    ],
        "interactions": [
            "Alcohol: tăng tác dụng an thần, tăng nguy cơ độc gan",
            "Warfarin: tăng nguy cơ chảy máu",
            "CNS depressants: tăng tác dụng ức chế"
    ],
        "pregnancy": "C",
        "mechanism_of_action": """Kết hợp paracetamol (giảm đau, hạ sốt) và chlorzoxazone (giãn cơ xương khớp). Paracetamol ức chế COX-3 ở CNS, giảm đau và hạ sốt. Chlorzoxazone là thuốc giãn cơ xương khớp, tác động lên tủy sống để giảm phản xạ cơ xương. Tác dụng hiệp đồng: giảm đau cơ xương khớp kèm co thắt cơ. CHỈ dùng ngắn hạn. Có thể gây nước tiểu màu cam/đỏ (vô hại).""",
        "monitoring": [
            "Đáp ứng điều trị: giảm đau, giảm co thắt cơ",
            "Chức năng gan - QUAN TRỌNG (cả paracetamol và chlorzoxazone đều có nguy cơ độc gan)",
            "Dấu hiệu quá liều paracetamol",
            "Màu nước tiểu (cam/đỏ - vô hại, không cần điều trị)"
    ],
        "precautions": [
            "CHỈ dùng ngắn hạn",
            "NGUY CƠ ĐỘC GAN - cả paracetamol và chlorzoxazone đều có nguy cơ độc gan",
            "Nước tiểu màu cam/đỏ - vô hại, không cần điều trị, giải thích cho bệnh nhân",
            "Không vượt quá 4g paracetamol/ngày - nguy cơ độc gan",
            "Tránh rượu - tăng tác dụng an thần, tăng nguy cơ độc gan",
            "Theo dõi chức năng gan định kỳ nếu dùng >1 tuần"
    ],
        "pharmacokinetics": {
            "half_life": "1-3 giờ (paracetamol), 1-2 giờ (chlorzoxazone)",
            "onset": "30 phút",
            "duration": "4-6 giờ",
            "protein_binding": "10-25% (paracetamol), không đáng kể (chlorzoxazone)",
            "clearance": "Gan: chuyển hóa. Thận: thải trừ.",
        },
        "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm",
        "black_box_warnings": """Nguy cơ độc gan nghiêm trọng với paracetamol nếu quá liều (>4g/ngày). Chlorzoxazone có thể gây độc gan (hiếm nhưng nghiêm trọng). Chỉ dùng ngắn hạn. Theo dõi chức năng gan.""",
        "drug_interactions": {
            "major": [
    {
                    "drug": "Alcohol",
                    "mechanism": "Tăng tác dụng ức chế CNS, tăng nguy cơ độc gan",
                    "effect": "Tăng buồn ngủ, tăng nguy cơ độc gan nặng",
                    "management": "TRÁNH RƯỢU hoàn toàn khi dùng thuốc này.",
                }
                ],
            "moderate": [
    {
                    "drug": "Warfarin",
                    "mechanism": "Paracetamol có thể tăng tác dụng warfarin",
                    "effect": "Tăng INR, tăng nguy cơ chảy máu",
                    "management": "Thận trọng. Theo dõi INR thường xuyên.",
                }
                ],
            "minor": [],
        },
        "pregnancy_lactation": {
            "fda_category": "C",
            "pregnancy_details": "Category C. Có thể dùng nếu lợi ích > nguy cơ.",
            "lactation": {
                "safety": "Caution",
                "details": "Paracetamol và chlorzoxazone đều bài tiết vào sữa mẹ. Có thể gây tác dụng phụ ở trẻ.",
                "recommendation": "Thận trọng khi cho con bú.",
            },
        },
        "hepatic_adjustment": {
            "mild": "Thận trọng, theo dõi chức năng gan",
            "moderate": "Thận trọng, tránh dùng nếu có thể",
            "severe": "CHỐNG CHỈ ĐỊNH",
            "notes": "CẢ HAI thuốc đều có nguy cơ độc gan. Suy gan nặng là chống chỉ định. Theo dõi chức năng gan định kỳ.",
        },
        "overdose_management": {
            "symptoms": [
                "Paracetamol quá liều: buồn nôn, nôn, đau bụng, vàng da, suy gan",
                "Chlorzoxazone quá liều: buồn ngủ nặng, ức chế hô hấp"
    ],
            "antidote": "N-acetylcysteine (NAC) cho paracetamol quá liều. Không có antidote cho chlorzoxazone.",
            "treatment": [
                "Nếu quá liều paracetamol (>150mg/kg): N-acetylcysteine (NAC) ngay lập tức",
                "Đánh giá đường thở, hô hấp, tuần hoàn",
                "Rửa dạ dày nếu trong vòng 1-2 giờ",
                "Than hoạt tính",
                "Hỗ trợ hô hấp nếu cần",
                "Theo dõi chức năng gan (quan trọng - cả hai thuốc đều có nguy cơ độc gan)"
    ],
            "monitoring": "Theo dõi ý thức, hô hấp, tim mạch. Theo dõi chức năng gan (ALT, AST, bilirubin, INR) - QUAN TRỌNG.",
        },
        "reversal_agents": {
            "available": True,
            "agents": [
    {
                    "agent": "N-acetylcysteine (NAC)",
                    "mechanism": "Chống độc cho paracetamol quá liều",
                    "indication": "Quá liều paracetamol (>150mg/kg)",
                    "dose": "Theo phác đồ điều trị quá liều paracetamol",
                    "caution": "Chỉ hiệu quả nếu dùng trong vòng 8-10 giờ sau khi uống paracetamol",
                }
                ],
        },
        "administration_instructions": {
            "oral": {
                "with_food": "Có thể uống với thức ăn hoặc không",
                "timing": """Paracetamol 325mg/Chlorzoxazone 250mg x 3-4 lần/ngày. CHỈ dùng ngắn hạn. KHÔNG vượt quá 4g paracetamol/ngày.""",
            },
        },
        "references": {
            "primary_sources": [
                "FDA Drug Label - Chlorzoxazone Compound",
                "UpToDate - Muscle relaxants: Drug information"
    ],
            "last_updated": "2025-02-18",
            "evidence_level": "High - FDA-approved",
        },
            "risk_flags": {
                "high_alert": False,
                "narrow_therapeutic_index": False,
                "bleeding_risk": False,
                "organ_toxicity": [],
                "qt_prolongation": False,
                "hepatotoxicity": False,
                "nephrotoxicity": False,
                "requires_monitoring": [],
            },
            "guideline_tags": [
                "FDA Drug Information",
                "UpToDate Drug Information",
            ]
    },
    "Paracetamol/Methocarbamol":     {
        "group": "Analgesic - Combination (Paracetamol + Muscle Relaxant)",
        "vietnamese_name": "Paracetamol/Methocarbamol, Robaxacet",
        "administration": [
            "PO"
    ],
        "indications": [
            "Đau cơ xương khớp kèm co thắt cơ (musculoskeletal pain with muscle spasm)",
            "Đau lưng cấp tính",
            "Đau cơ sau chấn thương"
    ],
        "contraindications": {
            "tuyệt_đối": [
                "Dị ứng paracetamol hoặc methocarbamol",
                "Suy gan nặng"
    ],
            "tương_đối": [
                "Suy gan trung bình - thận trọng"
    ],
        },
        "dosage": {
            "adult_standard": "Paracetamol 325mg/Methocarbamol 400mg x 4 lần/ngày",
            "adult_max": "Paracetamol 4g/ngày, Methocarbamol 2400mg/ngày",
            "notes": "CHỈ dùng ngắn hạn. Methocarbamol có thể gây nước tiểu màu xanh/đen (vô hại).",
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "Thận trọng",
            "under_30": "Thận trọng",
        },
        "side_effects": [
            "Buồn ngủ",
            "Chóng mặt",
            "Mệt mỏi",
            "Nhìn mờ",
            "Nước tiểu màu xanh/đen (vô hại - do methocarbamol)",
            "Độc gan (do paracetamol - nếu quá liều)"
    ],
        "interactions": [
            "Alcohol: tăng tác dụng an thần, tăng nguy cơ độc gan",
            "Warfarin: tăng nguy cơ chảy máu",
            "CNS depressants: tăng tác dụng ức chế"
    ],
        "pregnancy": "C",
        "mechanism_of_action": """Kết hợp paracetamol (giảm đau, hạ sốt) và methocarbamol (giãn cơ xương khớp). Paracetamol ức chế COX-3 ở CNS, giảm đau và hạ sốt. Methocarbamol là thuốc giãn cơ xương khớp, tác động lên CNS để giảm phản xạ cơ xương. Tác dụng hiệp đồng: giảm đau cơ xương khớp kèm co thắt cơ. CHỈ dùng ngắn hạn. Có thể gây nước tiểu màu xanh/đen (vô hại).""",
        "monitoring": [
            "Đáp ứng điều trị: giảm đau, giảm co thắt cơ",
            "Chức năng gan (nếu dùng >4g paracetamol/ngày)",
            "Dấu hiệu quá liều paracetamol",
            "Màu nước tiểu (xanh/đen - vô hại, không cần điều trị)"
    ],
        "precautions": [
            "CHỈ dùng ngắn hạn",
            "Nước tiểu màu xanh/đen - vô hại, không cần điều trị, giải thích cho bệnh nhân",
            "Không vượt quá 4g paracetamol/ngày - nguy cơ độc gan",
            "Tránh rượu - tăng tác dụng an thần, tăng nguy cơ độc gan",
            "Thận trọng ở suy gan - chống chỉ định paracetamol ở suy gan nặng"
    ],
        "pharmacokinetics": {
            "half_life": "1-3 giờ (paracetamol), 1-2 giờ (methocarbamol)",
            "onset": "30 phút",
            "duration": "4-6 giờ",
            "protein_binding": "10-25% (paracetamol), 46-50% (methocarbamol)",
            "clearance": "Gan: chuyển hóa. Thận: thải trừ.",
        },
        "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm",
        "black_box_warnings": "Nguy cơ độc gan nghiêm trọng với paracetamol nếu quá liều (>4g/ngày). Chỉ dùng ngắn hạn.",
        "drug_interactions": {
            "major": [
    {
                    "drug": "Alcohol",
                    "mechanism": "Tăng tác dụng ức chế CNS, tăng nguy cơ độc gan",
                    "effect": "Tăng buồn ngủ, tăng nguy cơ độc gan nặng",
                    "management": "TRÁNH RƯỢU hoàn toàn khi dùng thuốc này.",
                }
                ],
            "moderate": [
    {
                    "drug": "Warfarin",
                    "mechanism": "Paracetamol có thể tăng tác dụng warfarin",
                    "effect": "Tăng INR, tăng nguy cơ chảy máu",
                    "management": "Thận trọng. Theo dõi INR thường xuyên.",
                }
                ],
            "minor": [],
        },
        "pregnancy_lactation": {
            "fda_category": "C",
            "pregnancy_details": "Category C. Có thể dùng nếu lợi ích > nguy cơ.",
            "lactation": {
                "safety": "Caution",
                "details": "Paracetamol và methocarbamol đều bài tiết vào sữa mẹ. Có thể gây tác dụng phụ ở trẻ.",
                "recommendation": "Thận trọng khi cho con bú.",
            },
        },
        "hepatic_adjustment": {
            "mild": "Thận trọng",
            "moderate": "Thận trọng, giảm liều",
            "severe": "CHỐNG CHỈ ĐỊNH",
            "notes": "Paracetamol chuyển hóa ở gan, nguy cơ độc gan. Suy gan nặng là chống chỉ định.",
        },
        "overdose_management": {
            "symptoms": [
                "Paracetamol quá liều: buồn nôn, nôn, đau bụng, vàng da, suy gan",
                "Methocarbamol quá liều: buồn ngủ nặng, ức chế hô hấp"
    ],
            "antidote": "N-acetylcysteine (NAC) cho paracetamol quá liều. Không có antidote cho methocarbamol.",
            "treatment": [
                "Nếu quá liều paracetamol (>150mg/kg): N-acetylcysteine (NAC) ngay lập tức",
                "Đánh giá đường thở, hô hấp, tuần hoàn",
                "Rửa dạ dày nếu trong vòng 1-2 giờ",
                "Than hoạt tính",
                "Hỗ trợ hô hấp nếu cần",
                "Theo dõi chức năng gan (paracetamol quá liều)"
    ],
            "monitoring": "Theo dõi ý thức, hô hấp, tim mạch. Nếu paracetamol quá liều: theo dõi chức năng gan.",
        },
        "reversal_agents": {
            "available": True,
            "agents": [
    {
                    "agent": "N-acetylcysteine (NAC)",
                    "mechanism": "Chống độc cho paracetamol quá liều",
                    "indication": "Quá liều paracetamol (>150mg/kg)",
                    "dose": "Theo phác đồ điều trị quá liều paracetamol",
                    "caution": "Chỉ hiệu quả nếu dùng trong vòng 8-10 giờ sau khi uống paracetamol",
                }
                ],
        },
        "administration_instructions": {
            "oral": {
                "with_food": "Có thể uống với thức ăn hoặc không",
                "timing": """Paracetamol 325mg/Methocarbamol 400mg x 4 lần/ngày. CHỈ dùng ngắn hạn. KHÔNG vượt quá 4g paracetamol/ngày.""",
            },
        },
        "references": {
            "primary_sources": [
                "FDA Drug Label - Robaxacet (Paracetamol/Methocarbamol)",
                "UpToDate - Muscle relaxants: Drug information"
    ],
            "last_updated": "2025-02-18",
            "evidence_level": "High - FDA-approved",
        },
            "risk_flags": {
                "high_alert": False,
                "narrow_therapeutic_index": False,
                "bleeding_risk": False,
                "organ_toxicity": [],
                "qt_prolongation": False,
                "hepatotoxicity": False,
                "nephrotoxicity": False,
                "requires_monitoring": [],
            },
            "guideline_tags": [
                "FDA Drug Information",
                "UpToDate Drug Information",
            ]
    },
    "Paracetamol/Orphenadrine":     {
        "group": "Analgesic - Combination (Paracetamol + Muscle Relaxant)",
        "vietnamese_name": "Paracetamol/Orphenadrine, Norgesic, Norflex Compound",
        "administration": [
            "PO"
    ],
        "indications": [
            "Đau cơ xương khớp kèm co thắt cơ (musculoskeletal pain with muscle spasm)",
            "Đau lưng cấp tính",
            "Đau cơ sau chấn thương"
    ],
        "contraindications": {
            "tuyệt_đối": [
                "Dị ứng paracetamol hoặc orphenadrine",
                "Suy gan nặng",
                "Glaucoma góc đóng",
                "Phì đại tuyến tiền liệt",
                "Tắc ruột cơ học",
                "Bệnh tim mạch nặng"
    ],
            "tương_đối": [
                "Suy gan trung bình - thận trọng",
                "Người cao tuổi - tăng nhạy cảm với anticholinergic"
    ],
        },
        "dosage": {
            "adult_standard": "Paracetamol 450mg/Orphenadrine 35mg x 3 lần/ngày",
            "adult_max": "Paracetamol 4g/ngày",
            "notes": "CHỈ dùng ngắn hạn. Orphenadrine có tác dụng kháng cholinergic (khô miệng, nhìn mờ, bí tiểu).",
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "Thận trọng",
            "under_30": "Thận trọng",
        },
        "side_effects": [
            "Khô miệng (do orphenadrine - anticholinergic)",
            "Nhìn mờ",
            "Bí tiểu (đặc biệt ở nam giới có phì đại tuyến tiền liệt)",
            "Buồn ngủ",
            "Chóng mặt",
            "Độc gan (do paracetamol - nếu quá liều)",
            "Tăng nhịp tim (do orphenadrine)"
    ],
        "interactions": [
            "Alcohol: tăng tác dụng an thần, tăng nguy cơ độc gan",
            "Warfarin: tăng nguy cơ chảy máu",
            "Thuốc kháng cholinergic khác: tăng tác dụng phụ anticholinergic",
            "MAO inhibitors: tăng nguy cơ tác dụng phụ"
    ],
        "pregnancy": "C",
        "mechanism_of_action": """Kết hợp paracetamol (giảm đau, hạ sốt) và orphenadrine (giãn cơ xương khớp, anticholinergic). Paracetamol ức chế COX-3 ở CNS, giảm đau và hạ sốt. Orphenadrine là thuốc giãn cơ xương khớp có tác dụng anticholinergic (kháng muscarinic), gây giãn cơ trơn và giảm co thắt cơ. Tác dụng hiệp đồng: giảm đau cơ xương khớp kèm co thắt cơ. CHỈ dùng ngắn hạn. Tác dụng phụ anticholinergic: khô miệng, nhìn mờ, bí tiểu.""",
        "monitoring": [
            "Đáp ứng điều trị: giảm đau, giảm co thắt cơ",
            "Dấu hiệu tác dụng phụ anticholinergic (khô miệng, nhìn mờ, bí tiểu)",
            "Chức năng gan (nếu dùng >4g paracetamol/ngày)",
            "Dấu hiệu quá liều paracetamol",
            "Nhịp tim (tăng nhịp tim do orphenadrine)"
    ],
        "precautions": [
            "CHỈ dùng ngắn hạn",
            "Tác dụng phụ anticholinergic - khô miệng, nhìn mờ, bí tiểu (đặc biệt ở nam giới có phì đại tuyến tiền liệt)",
            "CHỐNG CHỈ ĐỊNH ở glaucoma góc đóng, phì đại tuyến tiền liệt, tắc ruột cơ học",
            "Không vượt quá 4g paracetamol/ngày - nguy cơ độc gan",
            "Tránh rượu - tăng tác dụng an thần, tăng nguy cơ độc gan",
            "Thận trọng ở bệnh nhân cao tuổi - tăng nhạy cảm với tác dụng anticholinergic"
    ],
        "pharmacokinetics": {
            "half_life": "1-3 giờ (paracetamol), 14 giờ (orphenadrine)",
            "onset": "30 phút",
            "duration": "4-6 giờ",
            "protein_binding": "10-25% (paracetamol), không đáng kể (orphenadrine)",
            "clearance": "Gan: chuyển hóa. Thận: thải trừ.",
        },
        "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm",
        "black_box_warnings": """Nguy cơ độc gan nghiêm trọng với paracetamol nếu quá liều (>4g/ngày). CHỐNG CHỈ ĐỊNH ở glaucoma góc đóng, phì đại tuyến tiền liệt, tắc ruột cơ học. Chỉ dùng ngắn hạn.""",
        "drug_interactions": {
            "major": [
    {
                    "drug": "Alcohol",
                    "mechanism": "Tăng tác dụng ức chế CNS, tăng nguy cơ độc gan",
                    "effect": "Tăng buồn ngủ, tăng nguy cơ độc gan nặng",
                    "management": "TRÁNH RƯỢU hoàn toàn khi dùng thuốc này.",
                },
    {
                    "drug": "Thuốc kháng cholinergic khác (Atropine, Scopolamine, Antihistamines)",
                    "mechanism": "Tác dụng cộng dồn anticholinergic",
                    "effect": "Tăng tác dụng phụ anticholinergic (khô miệng nặng, bí tiểu, nhìn mờ)",
                    "management": "Tránh dùng chung nếu có thể.",
                }
                ],
            "moderate": [
    {
                    "drug": "MAO inhibitors",
                    "mechanism": "Tăng nguy cơ tác dụng phụ",
                    "effect": "Tăng nguy cơ tác dụng phụ nghiêm trọng",
                    "management": "Tránh dùng chung.",
                }
                ],
            "minor": [],
        },
        "pregnancy_lactation": {
            "fda_category": "C",
            "pregnancy_details": "Category C. Có thể dùng nếu lợi ích > nguy cơ.",
            "lactation": {
                "safety": "Caution",
                "details": "Paracetamol và orphenadrine đều bài tiết vào sữa mẹ. Có thể gây tác dụng phụ ở trẻ.",
                "recommendation": "Thận trọng khi cho con bú.",
            },
        },
        "hepatic_adjustment": {
            "mild": "Thận trọng",
            "moderate": "Thận trọng, giảm liều",
            "severe": "CHỐNG CHỈ ĐỊNH",
            "notes": "Paracetamol chuyển hóa ở gan, nguy cơ độc gan. Suy gan nặng là chống chỉ định.",
        },
        "overdose_management": {
            "symptoms": [
                "Paracetamol quá liều: buồn nôn, nôn, đau bụng, vàng da, suy gan",
                "Orphenadrine quá liều: khô miệng nặng, nhìn mờ, bí tiểu, tăng nhịp tim, ảo giác"
    ],
            "antidote": "N-acetylcysteine (NAC) cho paracetamol quá liều. Physostigmine cho orphenadrine quá liều nặng.",
            "treatment": [
                "Nếu quá liều paracetamol (>150mg/kg): N-acetylcysteine (NAC) ngay lập tức",
                "Đánh giá đường thở, hô hấp, tuần hoàn",
                "Rửa dạ dày nếu trong vòng 1-2 giờ",
                "Than hoạt tính",
                "Nếu orphenadrine quá liều nặng (ảo giác, rối loạn ý thức): Physostigmine có thể được xem xét",
                "Theo dõi chức năng gan (paracetamol quá liều)"
    ],
            "monitoring": "Theo dõi ý thức, hô hấp, tim mạch, nhịp tim. Nếu paracetamol quá liều: theo dõi chức năng gan.",
        },
        "reversal_agents": {
            "available": True,
            "agents": [
    {
                    "agent": "N-acetylcysteine (NAC)",
                    "mechanism": "Chống độc cho paracetamol quá liều",
                    "indication": "Quá liều paracetamol (>150mg/kg)",
                    "dose": "Theo phác đồ điều trị quá liều paracetamol",
                    "caution": "Chỉ hiệu quả nếu dùng trong vòng 8-10 giờ sau khi uống paracetamol",
                },
    {
                    "agent": "Physostigmine",
                    "mechanism": "Chất ức chế cholinesterase, đảo ngược tác dụng anticholinergic",
                    "indication": "Orphenadrine quá liều nặng (ảo giác, rối loạn ý thức)",
                    "dose": "0.5-2mg IV, có thể lặp lại",
                    "caution": "Chỉ dùng khi quá liều nặng, cần theo dõi chặt chẽ",
                }
                ],
        },
        "administration_instructions": {
            "oral": {
                "with_food": "Có thể uống với thức ăn hoặc không",
                "timing": """Paracetamol 450mg/Orphenadrine 35mg x 3 lần/ngày. CHỈ dùng ngắn hạn. KHÔNG vượt quá 4g paracetamol/ngày.""",
            },
        },
        "references": {
            "primary_sources": [
                "FDA Drug Label - Norgesic (Paracetamol/Orphenadrine)",
                "UpToDate - Muscle relaxants: Drug information"
    ],
            "last_updated": "2025-02-18",
            "evidence_level": "High - FDA-approved",
        },
            "risk_flags": {
                "high_alert": False,
                "narrow_therapeutic_index": False,
                "bleeding_risk": False,
                "organ_toxicity": [],
                "qt_prolongation": False,
                "hepatotoxicity": False,
                "nephrotoxicity": False,
                "requires_monitoring": [],
            },
            "guideline_tags": [
                "FDA Drug Information",
                "UpToDate Drug Information",
            ]
    },
    "Paracetamol/Ibuprofen":     {
        "group": "Analgesic - Combination (Paracetamol + NSAID)",
        "vietnamese_name": "Paracetamol/Ibuprofen, Combiflam, Advil Dual Action",
        "administration": [
            "PO"
    ],
        "indications": [
            "Đau nhẹ đến trung bình",
            "Sốt",
            "Đau đầu",
            "Đau răng",
            "Đau cơ xương",
            "Đau bụng kinh"
    ],
        "contraindications": {
            "tuyệt_đối": [
                "Dị ứng paracetamol hoặc ibuprofen",
                "Suy gan nặng",
                "Loét dạ dày tá tràng đang hoạt động",
                "Tam cá nguyệt 3 thai kỳ (3 tháng cuối)",
                "Suy thận nặng"
    ],
            "tương_đối": [
                "Suy gan trung bình - thận trọng",
                "Suy thận trung bình - thận trọng",
                "Hen phế quản do aspirin/NSAID - thận trọng"
    ],
        },
        "dosage": {
            "adult_standard": "Paracetamol 500mg/Ibuprofen 200mg x 3-4 lần/ngày",
            "adult_max": "Paracetamol 4g/ngày, Ibuprofen 2400mg/ngày",
            "notes": """Kết hợp paracetamol (giảm đau, hạ sốt) và ibuprofen (NSAID, giảm đau, chống viêm, hạ sốt). Tác dụng hiệp đồng, hiệu quả tốt hơn từng thuốc đơn lẻ. Không vượt quá 4g paracetamol/ngày.""",
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "Thận trọng, giảm liều",
            "under_30": "Tránh dùng",
        },
        "side_effects": [
            "Chảy máu dạ dày (do ibuprofen)",
            "Độc gan (do paracetamol - nếu quá liều)",
            "Suy thận (do ibuprofen)",
            "Tăng huyết áp (do ibuprofen)",
            "Buồn nôn, nôn",
            "Đau đầu",
            "Chóng mặt"
    ],
        "interactions": [
            "Warfarin: tăng nguy cơ chảy máu (cả hai thuốc)",
            "Alcohol: tăng nguy cơ độc gan (paracetamol), tăng nguy cơ chảy máu dạ dày (ibuprofen)",
            "ACE inhibitor: giảm hiệu quả, tăng nguy cơ suy thận (ibuprofen)",
            "Methotrexate: tăng độc tính methotrexate (ibuprofen)"
    ],
        "pregnancy": "C - D trong 3 tháng cuối",
        "mechanism_of_action": """Kết hợp paracetamol (giảm đau, hạ sốt) và ibuprofen (NSAID, giảm đau, chống viêm, hạ sốt). Paracetamol ức chế COX-3 ở CNS, giảm đau và hạ sốt. Ibuprofen ức chế COX-1 và COX-2, giảm đau, chống viêm, và hạ sốt. Tác dụng hiệp đồng: hiệu quả giảm đau và hạ sốt tốt hơn từng thuốc đơn lẻ. Ibuprofen cung cấp thêm tác dụng chống viêm mà paracetamol không có.""",
        "monitoring": [
            "Đáp ứng điều trị: giảm đau, hạ sốt",
            "Dấu hiệu chảy máu dạ dày (do ibuprofen)",
            "Chức năng gan (nếu dùng >4g paracetamol/ngày)",
            "Creatinine, BUN (do ibuprofen)",
            "Dấu hiệu quá liều paracetamol"
    ],
        "precautions": [
            "KHÔNG vượt quá 4g paracetamol/ngày - nguy cơ độc gan",
            "Nguy cơ chảy máu dạ dày do ibuprofen - uống với thức ăn",
            "Tránh rượu - tăng nguy cơ độc gan và chảy máu dạ dày",
            "Không dùng trong 3 tháng cuối thai kỳ",
            "Thận trọng ở suy gan, suy thận",
            "Theo dõi chức năng gan và thận nếu dùng kéo dài"
    ],
        "pharmacokinetics": {
            "half_life": "1-3 giờ (paracetamol), 2 giờ (ibuprofen)",
            "onset": "30 phút",
            "duration": "4-6 giờ",
            "protein_binding": "10-25% (paracetamol), 99% (ibuprofen)",
            "clearance": "Gan: chuyển hóa. Thận: thải trừ.",
        },
        "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm",
        "black_box_warnings": """Nguy cơ độc gan nghiêm trọng với paracetamol nếu quá liều (>4g/ngày). Nguy cơ chảy máu dạ dày với ibuprofen. Không dùng trong 3 tháng cuối thai kỳ. NSAID có thể gây tăng nguy cơ nhồi máu cơ tim và đột quỵ.""",
        "drug_interactions": {
            "major": [
    {
                    "drug": "Warfarin, các thuốc chống đông khác",
                    "mechanism": "Cả hai thuốc đều tăng nguy cơ chảy máu",
                    "effect": "Tăng nguy cơ chảy máu nặng, tăng INR",
                    "management": "Tránh dùng đồng thời hoặc theo dõi INR chặt chẽ.",
                },
    {
                    "drug": "Alcohol",
                    "mechanism": "Tăng nguy cơ độc gan (paracetamol), tăng nguy cơ chảy máu dạ dày (ibuprofen)",
                    "effect": "Tăng nguy cơ độc gan nặng, tăng nguy cơ chảy máu dạ dày",
                    "management": "TRÁNH RƯỢU hoàn toàn khi dùng thuốc này.",
                }
                ],
            "moderate": [
    {
                    "drug": "ACE inhibitor, ARB",
                    "mechanism": "Ibuprofen giảm tổng hợp prostaglandin → giảm lưu lượng máu thận",
                    "effect": "Giảm hiệu quả, tăng nguy cơ suy thận",
                    "management": "Thận trọng. Theo dõi creatinine, BUN.",
                }
                ],
            "minor": [],
        },
        "pregnancy_lactation": {
            "fda_category": "C - D trong tam cá nguyệt 3",
            "pregnancy_details": "Tam cá nguyệt 3: CHỐNG CHỈ ĐỊNH (do ibuprofen).",
            "lactation": {
                "safety": "Caution",
                "details": "Cả hai thuốc đều bài tiết vào sữa mẹ. Có thể gây tác dụng phụ ở trẻ.",
                "recommendation": "Thận trọng khi cho con bú.",
            },
        },
        "hepatic_adjustment": {
            "mild": "Thận trọng",
            "moderate": "Thận trọng, giảm liều",
            "severe": "CHỐNG CHỈ ĐỊNH",
            "notes": "Paracetamol chuyển hóa ở gan, nguy cơ độc gan. Suy gan nặng là chống chỉ định.",
        },
        "overdose_management": {
            "symptoms": [
                "Paracetamol quá liều: buồn nôn, nôn, đau bụng, vàng da, suy gan",
                "Ibuprofen quá liều: buồn nôn, nôn, đau bụng, chảy máu dạ dày, suy thận cấp"
    ],
            "antidote": "N-acetylcysteine (NAC) cho paracetamol quá liều. Không có antidote cho ibuprofen.",
            "treatment": [
                "Nếu quá liều paracetamol (>150mg/kg): N-acetylcysteine (NAC) ngay lập tức",
                "Đánh giá đường thở, hô hấp, tuần hoàn",
                "Rửa dạ dày nếu trong vòng 1-2 giờ",
                "Than hoạt tính",
                "Điều trị hỗ trợ",
                "Theo dõi chức năng gan và thận"
    ],
            "monitoring": "Theo dõi ý thức, hô hấp, tim mạch. Nếu paracetamol quá liều: theo dõi chức năng gan (ALT, AST, bilirubin, INR). Nếu ibuprofen quá liều: theo dõi chức năng thận, dấu hiệu chảy máu.",
        },
        "reversal_agents": {
            "available": True,
            "agents": [
    {
                    "agent": "N-acetylcysteine (NAC)",
                    "mechanism": "Chống độc cho paracetamol quá liều",
                    "indication": "Quá liều paracetamol (>150mg/kg hoặc >10g)",
                    "dose": "Theo phác đồ điều trị quá liều paracetamol",
                    "caution": "Chỉ hiệu quả nếu dùng trong vòng 8-10 giờ sau khi uống paracetamol",
                }
                ],
        },
        "administration_instructions": {
            "oral": {
                "with_food": "Uống với thức ăn để giảm kích ứng dạ dày (ibuprofen)",
                "timing": """Paracetamol 500mg/Ibuprofen 200mg x 3-4 lần/ngày. KHÔNG vượt quá 4g paracetamol/ngày và 2400mg ibuprofen/ngày.""",
            },
        },
        "references": {
            "primary_sources": [
                "FDA Drug Label - Paracetamol/Ibuprofen combinations",
                "UpToDate - Combination analgesics: Drug information"
    ],
            "last_updated": "2025-02-18",
            "evidence_level": "High - FDA-approved, extensive clinical data",
        },
            "risk_flags": {
                "high_alert": False,
                "narrow_therapeutic_index": False,
                "bleeding_risk": True,
                "organ_toxicity": ["GI", "renal", "hepatic"],
                "qt_prolongation": False,
                "hepatotoxicity": True,
                "nephrotoxicity": True,
                "requires_monitoring": ["LFT", "RFT", "GI symptoms"],
            },
            "guideline_tags": [
                "FDA Drug Information",
                "UpToDate Drug Information",
            ]
    },
    "Paracetamol/Codeine":     {
        "group": "Analgesic - Combination (Paracetamol + Opioid)",
        "vietnamese_name": "Paracetamol/Codeine, Co-codamol, Tylenol #3",
        "administration": [
            "PO"
    ],
        "indications": [
            "Đau nhẹ đến trung bình",
            "Đau sau phẫu thuật",
            "Đau không đáp ứng với paracetamol đơn thuần"
    ],
        "contraindications": {
            "tuyệt_đối": [
                "Dị ứng paracetamol hoặc codeine",
                "Suy gan nặng",
                "Suy hô hấp nặng",
                "Tắc ruột cơ học",
                "Trẻ em <12 tuổi",
                "Trẻ em 12-18 tuổi sau phẫu thuật cắt amidan/VA (nguy cơ ức chế hô hấp)"
    ],
            "tương_đối": [
                "Suy gan trung bình - thận trọng",
                "Suy thận - thận trọng",
                "Tiền sử nghiện/lạm dụng chất - tăng nguy cơ nghiện"
    ],
        },
        "dosage": {
            "adult_standard": "Paracetamol 500mg/Codeine 15-30mg x 3-4 lần/ngày",
            "adult_max": "Paracetamol 4g/ngày, Codeine 240mg/ngày",
            "notes": """Kết hợp paracetamol (giảm đau, hạ sốt) và codeine (opioid yếu, giảm đau). Codeine là prodrug, chuyển hóa thành morphine qua CYP2D6. Tác dụng hiệp đồng. Controlled substance - nguy cơ nghiện. KHÔNG vượt quá 4g paracetamol/ngày.""",
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "Thận trọng",
            "under_30": "Thận trọng, giảm liều codeine",
        },
        "side_effects": [
            "Buồn ngủ (do codeine)",
            "Táo bón (do codeine)",
            "Buồn nôn, nôn",
            "Chóng mặt",
            "Ức chế hô hấp (do codeine - hiếm nhưng nghiêm trọng)",
            "Độc gan (do paracetamol - nếu quá liều)",
            "Nguy cơ nghiện/lệ thuộc (do codeine)"
    ],
        "interactions": [
            "Alcohol: tăng tác dụng ức chế CNS, tăng nguy cơ độc gan",
            "Warfarin: tăng nguy cơ chảy máu",
            "CNS depressants: tăng tác dụng ức chế",
            "CYP2D6 inhibitors: giảm chuyển hóa codeine thành morphine"
    ],
        "pregnancy": "C - D trong 3 tháng cuối",
        "mechanism_of_action": """Kết hợp paracetamol (giảm đau, hạ sốt) và codeine (opioid yếu, giảm đau). Paracetamol ức chế COX-3 ở CNS, giảm đau và hạ sốt. Codeine là prodrug, chuyển hóa thành morphine qua CYP2D6. Morphine tác động lên thụ thể mu-opioid ở CNS, giảm đau. Tác dụng hiệp đồng: hiệu quả giảm đau tốt hơn từng thuốc đơn lẻ. Controlled substance - nguy cơ nghiện/lệ thuộc.""",
        "monitoring": [
            "Đáp ứng điều trị: giảm đau",
            "Dấu hiệu ức chế hô hấp (đặc biệt ở trẻ em và người cao tuổi)",
            "Chức năng gan (nếu dùng >4g paracetamol/ngày)",
            "Dấu hiệu nghiện/lệ thuộc",
            "Dấu hiệu quá liều paracetamol"
    ],
        "precautions": [
            "CONTROLLED SUBSTANCE - nguy cơ nghiện/lệ thuộc",
            "KHÔNG vượt quá 4g paracetamol/ngày - nguy cơ độc gan",
            "CHỐNG CHỈ ĐỊNH ở trẻ <12 tuổi và trẻ 12-18 tuổi sau phẫu thuật cắt amidan/VA",
            "Nguy cơ ức chế hô hấp - đặc biệt ở trẻ em và người cao tuổi",
            "Tránh rượu - tăng tác dụng ức chế CNS, tăng nguy cơ độc gan",
            "Thận trọng ở suy gan, suy thận",
            "Táo bón phổ biến - có thể cần thuốc nhuận tràng"
    ],
        "pharmacokinetics": {
            "half_life": "1-3 giờ (paracetamol), 3 giờ (codeine), 2-3 giờ (morphine)",
            "onset": "30 phút",
            "duration": "4-6 giờ",
            "protein_binding": "10-25% (paracetamol), 7-25% (codeine)",
            "clearance": "Gan: chuyển hóa (codeine → morphine qua CYP2D6). Thận: thải trừ.",
        },
        "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm. Controlled substance - cần bảo quản an toàn.",
        "black_box_warnings": """CONTROLLED SUBSTANCE - nguy cơ nghiện, lạm dụng, và lệ thuộc. Nguy cơ ức chế hô hấp, đặc biệt ở trẻ em. CHỐNG CHỈ ĐỊNH ở trẻ <12 tuổi và trẻ 12-18 tuổi sau phẫu thuật cắt amidan/VA. Nguy cơ độc gan nghiêm trọng với paracetamol nếu quá liều (>4g/ngày).""",
        "drug_interactions": {
            "major": [
    {
                    "drug": "Alcohol",
                    "mechanism": "Tăng tác dụng ức chế CNS, tăng nguy cơ độc gan",
                    "effect": "Tăng buồn ngủ, tăng nguy cơ ức chế hô hấp, tăng nguy cơ độc gan nặng",
                    "management": "TRÁNH RƯỢU hoàn toàn khi dùng thuốc này.",
                },
    {
                    "drug": "CNS depressants (Benzodiazepines, Opioids khác)",
                    "mechanism": "Tăng tác dụng ức chế CNS",
                    "effect": "Tăng buồn ngủ, nguy cơ ức chế hô hấp nặng",
                    "management": "Tránh dùng chung hoặc giảm liều.",
                }
                ],
            "moderate": [
    {
                    "drug": "CYP2D6 inhibitors (Fluoxetine, Paroxetine, Quinidine)",
                    "mechanism": "Ức chế chuyển hóa codeine thành morphine",
                    "effect": "Giảm hiệu quả giảm đau",
                    "management": "Có thể cần tăng liều hoặc dùng opioid khác.",
                }
                ],
            "minor": [],
        },
        "pregnancy_lactation": {
            "fda_category": "C - D trong tam cá nguyệt 3",
            "pregnancy_details": "Tam cá nguyệt 3: Category D - CHỐNG CHỈ ĐỊNH (do codeine).",
            "lactation": {
                "safety": "Contraindicated",
                "details": "Codeine bài tiết vào sữa mẹ, có thể gây ức chế hô hấp ở trẻ sơ sinh.",
                "recommendation": "KHÔNG dùng khi cho con bú.",
            },
        },
        "hepatic_adjustment": {
            "mild": "Thận trọng",
            "moderate": "Thận trọng, giảm liều",
            "severe": "CHỐNG CHỈ ĐỊNH",
            "notes": "Paracetamol chuyển hóa ở gan, nguy cơ độc gan. Codeine chuyển hóa ở gan. Suy gan nặng là chống chỉ định.",
        },
        "overdose_management": {
            "symptoms": [
                "Paracetamol quá liều: buồn nôn, nôn, đau bụng, vàng da, suy gan",
                "Codeine quá liều: buồn ngủ nặng, ức chế hô hấp, hôn mê, co đồng tử"
    ],
            "antidote": "N-acetylcysteine (NAC) cho paracetamol quá liều. Naloxone cho codeine quá liều.",
            "treatment": [
                "Nếu quá liều paracetamol (>150mg/kg): N-acetylcysteine (NAC) ngay lập tức",
                "Nếu quá liều codeine (ức chế hô hấp): Naloxone 0.4-2mg IV/IM, có thể lặp lại",
                "Đánh giá đường thở, hô hấp, tuần hoàn - QUAN TRỌNG",
                "Hỗ trợ hô hấp nếu cần",
                "Rửa dạ dày nếu trong vòng 1-2 giờ",
                "Than hoạt tính",
                "Theo dõi chức năng gan (paracetamol quá liều)"
    ],
            "monitoring": "Theo dõi ý thức, hô hấp (QUAN TRỌNG), tim mạch. Nếu paracetamol quá liều: theo dõi chức năng gan (ALT, AST, bilirubin, INR).",
        },
        "reversal_agents": {
            "available": True,
            "agents": [
    {
                    "agent": "N-acetylcysteine (NAC)",
                    "mechanism": "Chống độc cho paracetamol quá liều",
                    "indication": "Quá liều paracetamol (>150mg/kg hoặc >10g)",
                    "dose": "Theo phác đồ điều trị quá liều paracetamol",
                    "caution": "Chỉ hiệu quả nếu dùng trong vòng 8-10 giờ sau khi uống paracetamol",
                },
    {
                    "agent": "Naloxone",
                    "mechanism": "Đối kháng thụ thể mu-opioid, đảo ngược tác dụng codeine/morphine",
                    "indication": "Codeine quá liều (ức chế hô hấp)",
                    "dose": "0.4-2mg IV/IM, có thể lặp lại mỗi 2-3 phút",
                    "caution": "Tác dụng ngắn (30-90 phút), có thể cần lặp lại",
                }
                ],
        },
        "administration_instructions": {
            "oral": {
                "with_food": "Có thể uống với thức ăn hoặc không",
                "timing": """Paracetamol 500mg/Codeine 15-30mg x 3-4 lần/ngày. KHÔNG vượt quá 4g paracetamol/ngày và 240mg codeine/ngày. Controlled substance - cần kê đơn.""",
            },
        },
        "references": {
            "primary_sources": [
                "FDA Drug Label - Co-codamol (Paracetamol/Codeine)",
                "UpToDate - Combination analgesics: Drug information"
    ],
            "last_updated": "2025-02-18",
            "evidence_level": "High - FDA-approved, controlled substance",
        },
            "risk_flags": {
                "high_alert": True,
                "narrow_therapeutic_index": False,
                "bleeding_risk": False,
                "organ_toxicity": ["hepatic", "CNS"],
                "qt_prolongation": False,
                "hepatotoxicity": True,
                "nephrotoxicity": False,
                "requires_monitoring": ["LFT", "Respiratory status", "CNS status"],
            },
            "guideline_tags": [
                "FDA Drug Information",
                "UpToDate Drug Information",
                "Controlled Substance - Risk of Addiction",
            ]
    },
    "Paracetamol/Tramadol":     {
        "group": "Analgesic - Combination (Paracetamol + Opioid)",
        "vietnamese_name": "Paracetamol/Tramadol, Tramacet, Ultracet",
        "administration": [
            "PO"
    ],
        "indications": [
            "Đau trung bình đến nặng",
            "Đau sau phẫu thuật",
            "Đau cấp tính",
            "Đau không đáp ứng với paracetamol đơn thuần"
    ],
        "contraindications": {
            "tuyệt_đối": [
                "Dị ứng paracetamol hoặc tramadol",
                "Suy gan nặng",
                "Suy hô hấp nặng",
                "Tắc ruột cơ học",
                "Động kinh không kiểm soát",
                "Dùng MAO inhibitors trong vòng 14 ngày",
                "Trẻ em <12 tuổi"
    ],
            "tương_đối": [
                "Suy gan trung bình - thận trọng",
                "Suy thận - thận trọng, giảm liều",
                "Tiền sử nghiện/lạm dụng chất - tăng nguy cơ nghiện",
                "Tiền sử co giật - tăng nguy cơ co giật"
    ],
        },
        "dosage": {
            "adult_standard": "Paracetamol 325mg/Tramadol 37.5mg x 4 lần/ngày",
            "adult_max": "Paracetamol 4g/ngày, Tramadol 400mg/ngày",
            "notes": """Kết hợp paracetamol (giảm đau, hạ sốt) và tramadol (opioid yếu, giảm đau). Tramadol có cơ chế kép: tác động lên thụ thể mu-opioid và ức chế tái hấp thu serotonin/norepinephrine. Tác dụng hiệp đồng. Controlled substance - nguy cơ nghiện. KHÔNG vượt quá 4g paracetamol/ngày. Nguy cơ co giật với tramadol.""",
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "Thận trọng, giảm liều tramadol",
            "under_30": "Thận trọng, giảm liều tramadol (tối đa 200mg/ngày)",
        },
        "side_effects": [
            "Buồn ngủ (do tramadol)",
            "Táo bón (do tramadol)",
            "Buồn nôn, nôn",
            "Chóng mặt",
            "Co giật (do tramadol - nguy cơ tăng với liều cao)",
            "Ức chế hô hấp (do tramadol - hiếm nhưng nghiêm trọng)",
            "Độc gan (do paracetamol - nếu quá liều)",
            "Nguy cơ nghiện/lệ thuộc (do tramadol)",
            "Hội chứng serotonin (nếu dùng với SSRI/SNRI)"
    ],
        "interactions": [
            "Alcohol: tăng tác dụng ức chế CNS, tăng nguy cơ độc gan",
            "Warfarin: tăng nguy cơ chảy máu",
            "CNS depressants: tăng tác dụng ức chế",
            "MAO inhibitors: CHỐNG CHỈ ĐỊNH - nguy cơ hội chứng serotonin nặng",
            "SSRI/SNRI: tăng nguy cơ hội chứng serotonin, tăng nguy cơ co giật",
            "Carbamazepine: giảm hiệu quả tramadol"
    ],
        "pregnancy": "C - D trong 3 tháng cuối",
        "mechanism_of_action": """Kết hợp paracetamol (giảm đau, hạ sốt) và tramadol (opioid yếu, giảm đau). Paracetamol ức chế COX-3 ở CNS, giảm đau và hạ sốt. Tramadol có cơ chế kép: (1) tác động lên thụ thể mu-opioid (yếu hơn morphine), (2) ức chế tái hấp thu serotonin và norepinephrine. Tác dụng hiệp đồng: hiệu quả giảm đau tốt hơn từng thuốc đơn lẻ. Controlled substance - nguy cơ nghiện/lệ thuộc. Nguy cơ co giật với tramadol, đặc biệt khi dùng liều cao hoặc với SSRI/SNRI.""",
        "monitoring": [
            "Đáp ứng điều trị: giảm đau",
            "Dấu hiệu ức chế hô hấp (đặc biệt ở người cao tuổi)",
            "Dấu hiệu co giật (nguy cơ tăng với liều cao, SSRI/SNRI)",
            "Dấu hiệu hội chứng serotonin (nếu dùng với SSRI/SNRI)",
            "Chức năng gan (nếu dùng >4g paracetamol/ngày)",
            "Dấu hiệu nghiện/lệ thuộc",
            "Dấu hiệu quá liều paracetamol"
    ],
        "precautions": [
            "CONTROLLED SUBSTANCE - nguy cơ nghiện/lệ thuộc",
            "KHÔNG vượt quá 4g paracetamol/ngày - nguy cơ độc gan",
            "NGUY CƠ CO GIẬT - tăng với liều cao, SSRI/SNRI, tiền sử co giật",
            "CHỐNG CHỈ ĐỊNH với MAO inhibitors - nguy cơ hội chứng serotonin nặng",
            "CHỐNG CHỈ ĐỊNH ở trẻ <12 tuổi",
            "Nguy cơ ức chế hô hấp - đặc biệt ở người cao tuổi",
            "Tránh rượu - tăng tác dụng ức chế CNS, tăng nguy cơ độc gan",
            "Thận trọng với SSRI/SNRI - tăng nguy cơ hội chứng serotonin và co giật",
            "Thận trọng ở suy gan, suy thận",
            "Táo bón phổ biến - có thể cần thuốc nhuận tràng"
    ],
        "pharmacokinetics": {
            "half_life": "1-3 giờ (paracetamol), 6 giờ (tramadol)",
            "onset": "30 phút",
            "duration": "4-6 giờ",
            "protein_binding": "10-25% (paracetamol), 20% (tramadol)",
            "clearance": "Gan: chuyển hóa (tramadol qua CYP2D6 và CYP3A4). Thận: thải trừ.",
        },
        "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm. Controlled substance - cần bảo quản an toàn.",
        "black_box_warnings": """CONTROLLED SUBSTANCE - nguy cơ nghiện, lạm dụng, và lệ thuộc. Nguy cơ ức chế hô hấp, đặc biệt ở người cao tuổi. Nguy cơ co giật, đặc biệt với liều cao hoặc SSRI/SNRI. CHỐNG CHỈ ĐỊNH với MAO inhibitors. CHỐNG CHỈ ĐỊNH ở trẻ <12 tuổi. Nguy cơ độc gan nghiêm trọng với paracetamol nếu quá liều (>4g/ngày).""",
        "drug_interactions": {
            "major": [
    {
                    "drug": "MAO inhibitors",
                    "mechanism": "Tăng nguy cơ hội chứng serotonin nặng",
                    "effect": "Nguy cơ hội chứng serotonin nặng, có thể tử vong",
                    "management": "CHỐNG CHỈ ĐỊNH. Không dùng trong vòng 14 ngày sau khi ngừng MAO inhibitors.",
                },
    {
                    "drug": "Alcohol",
                    "mechanism": "Tăng tác dụng ức chế CNS, tăng nguy cơ độc gan",
                    "effect": "Tăng buồn ngủ, tăng nguy cơ ức chế hô hấp, tăng nguy cơ độc gan nặng",
                    "management": "TRÁNH RƯỢU hoàn toàn khi dùng thuốc này.",
                },
    {
                    "drug": "SSRI/SNRI (Fluoxetine, Sertraline, Venlafaxine)",
                    "mechanism": "Tăng nguy cơ hội chứng serotonin và co giật",
                    "effect": "Tăng nguy cơ hội chứng serotonin, tăng nguy cơ co giật",
                    "management": "Thận trọng. Theo dõi dấu hiệu hội chứng serotonin và co giật.",
                }
                ],
            "moderate": [
    {
                    "drug": "CNS depressants (Benzodiazepines, Opioids khác)",
                    "mechanism": "Tăng tác dụng ức chế CNS",
                    "effect": "Tăng buồn ngủ, nguy cơ ức chế hô hấp nặng",
                    "management": "Tránh dùng chung hoặc giảm liều.",
                }
                ],
            "minor": [],
        },
        "pregnancy_lactation": {
            "fda_category": "C - D trong tam cá nguyệt 3",
            "pregnancy_details": "Tam cá nguyệt 3: Category D - CHỐNG CHỈ ĐỊNH (do tramadol).",
            "lactation": {
                "safety": "Contraindicated",
                "details": "Tramadol bài tiết vào sữa mẹ, có thể gây ức chế hô hấp ở trẻ sơ sinh.",
                "recommendation": "KHÔNG dùng khi cho con bú.",
            },
        },
        "hepatic_adjustment": {
            "mild": "Thận trọng",
            "moderate": "Thận trọng, giảm liều",
            "severe": "CHỐNG CHỈ ĐỊNH",
            "notes": "Paracetamol chuyển hóa ở gan, nguy cơ độc gan. Tramadol chuyển hóa ở gan. Suy gan nặng là chống chỉ định.",
        },
        "overdose_management": {
            "symptoms": [
                "Paracetamol quá liều: buồn nôn, nôn, đau bụng, vàng da, suy gan",
                "Tramadol quá liều: buồn ngủ nặng, ức chế hô hấp, hôn mê, co giật, hội chứng serotonin"
    ],
            "antidote": "N-acetylcysteine (NAC) cho paracetamol quá liều. Naloxone cho tramadol quá liều (ức chế hô hấp).",
            "treatment": [
                "Nếu quá liều paracetamol (>150mg/kg): N-acetylcysteine (NAC) ngay lập tức",
                "Nếu quá liều tramadol (ức chế hô hấp): Naloxone 0.4-2mg IV/IM, có thể lặp lại",
                "Nếu co giật: benzodiazepine (diazepam, lorazepam)",
                "Nếu hội chứng serotonin: cyproheptadine, hỗ trợ hô hấp",
                "Đánh giá đường thở, hô hấp, tuần hoàn - QUAN TRỌNG",
                "Hỗ trợ hô hấp nếu cần",
                "Rửa dạ dày nếu trong vòng 1-2 giờ",
                "Than hoạt tính",
                "Theo dõi chức năng gan (paracetamol quá liều)"
    ],
            "monitoring": "Theo dõi ý thức, hô hấp (QUAN TRỌNG), tim mạch, dấu hiệu co giật, dấu hiệu hội chứng serotonin. Nếu paracetamol quá liều: theo dõi chức năng gan (ALT, AST, bilirubin, INR).",
        },
        "reversal_agents": {
            "available": True,
            "agents": [
    {
                    "agent": "N-acetylcysteine (NAC)",
                    "mechanism": "Chống độc cho paracetamol quá liều",
                    "indication": "Quá liều paracetamol (>150mg/kg hoặc >10g)",
                    "dose": "Theo phác đồ điều trị quá liều paracetamol",
                    "caution": "Chỉ hiệu quả nếu dùng trong vòng 8-10 giờ sau khi uống paracetamol",
                },
    {
                    "agent": "Naloxone",
                    "mechanism": "Đối kháng thụ thể mu-opioid, đảo ngược tác dụng tramadol",
                    "indication": "Tramadol quá liều (ức chế hô hấp)",
                    "dose": "0.4-2mg IV/IM, có thể lặp lại mỗi 2-3 phút",
                    "caution": "Tác dụng ngắn (30-90 phút), có thể cần lặp lại. Có thể không hiệu quả hoàn toàn do cơ chế kép của tramadol.",
                }
                ],
        },
        "administration_instructions": {
            "oral": {
                "with_food": "Có thể uống với thức ăn hoặc không",
                "timing": """Paracetamol 325mg/Tramadol 37.5mg x 4 lần/ngày. KHÔNG vượt quá 4g paracetamol/ngày và 400mg tramadol/ngày. Controlled substance - cần kê đơn.""",
            },
        },
        "references": {
            "primary_sources": [
                "FDA Drug Label - Tramacet (Paracetamol/Tramadol)",
                "UpToDate - Combination analgesics: Drug information"
    ],
            "last_updated": "2025-02-18",
            "evidence_level": "High - FDA-approved, controlled substance",
        },
            "risk_flags": {
                "high_alert": True,
                "narrow_therapeutic_index": False,
                "bleeding_risk": False,
                "organ_toxicity": ["hepatic", "CNS"],
                "qt_prolongation": False,
                "hepatotoxicity": True,
                "nephrotoxicity": False,
                "requires_monitoring": ["LFT", "Respiratory status", "CNS status", "Seizure risk"],
            },
            "guideline_tags": [
                "FDA Drug Information",
                "UpToDate Drug Information",
                "Controlled Substance - Risk of Addiction",
                "Serotonin Syndrome Risk",
            ]
    },
    "Aspirin/Codeine":     {
        "group": "Analgesic - Combination (NSAID + Opioid)",
        "vietnamese_name": "Aspirin/Codeine, Co-codaprin",
        "administration": [
            "PO"
    ],
        "indications": [
            "Đau nhẹ đến trung bình",
            "Đau cơ xương",
            "Đau đầu",
            "Đau răng",
            "Đau không đáp ứng với aspirin đơn thuần"
    ],
        "contraindications": {
            "tuyệt_đối": [
                "Dị ứng aspirin hoặc codeine",
                "Loét dạ dày tá tràng đang hoạt động",
                "Suy hô hấp nặng",
                "Tắc ruột cơ học",
                "Trẻ em <12 tuổi (hội chứng Reye với aspirin)",
                "Trẻ em 12-18 tuổi sau phẫu thuật cắt amidan/VA",
                "Dùng warfarin hoặc thuốc chống đông khác"
    ],
            "tương_đối": [
                "Suy thận trung bình - thận trọng",
                "Suy gan trung bình - thận trọng",
                "Tiền sử nghiện/lạm dụng chất - tăng nguy cơ nghiện"
    ],
        },
        "dosage": {
            "adult_standard": "Aspirin 325mg/Codeine 15-30mg x 3-4 lần/ngày",
            "adult_max": "Aspirin 4g/ngày, Codeine 240mg/ngày",
            "notes": """Kết hợp aspirin (NSAID, giảm đau, chống viêm, chống kết tập tiểu cầu) và codeine (opioid yếu, giảm đau). Aspirin có tác dụng chống kết tập tiểu cầu kéo dài. Codeine là prodrug, chuyển hóa thành morphine qua CYP2D6. Tác dụng hiệp đồng. Controlled substance - nguy cơ nghiện. CHỐNG CHỈ ĐỊNH với warfarin.""",
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "Thận trọng, giảm liều",
            "under_30": "Thận trọng, giảm liều codeine",
        },
        "side_effects": [
            "Chảy máu dạ dày (do aspirin)",
            "Buồn ngủ (do codeine)",
            "Táo bón (do codeine)",
            "Buồn nôn, nôn",
            "Chóng mặt",
            "Ức chế hô hấp (do codeine - hiếm nhưng nghiêm trọng)",
            "Nguy cơ nghiện/lệ thuộc (do codeine)",
            "Tinnitus (ù tai) ở liều cao aspirin"
    ],
        "interactions": [
            "Warfarin: CHỐNG CHỈ ĐỊNH - tăng nguy cơ chảy máu nặng",
            "Alcohol: tăng tác dụng ức chế CNS, tăng nguy cơ chảy máu dạ dày",
            "CNS depressants: tăng tác dụng ức chế",
            "ACE inhibitor: giảm hiệu quả, tăng nguy cơ suy thận (aspirin)",
            "CYP2D6 inhibitors: giảm chuyển hóa codeine thành morphine"
    ],
        "pregnancy": "C - D trong 3 tháng cuối",
        "mechanism_of_action": """Kết hợp aspirin (NSAID, giảm đau, chống viêm, chống kết tập tiểu cầu) và codeine (opioid yếu, giảm đau). Aspirin ức chế không hồi phục COX-1 và COX-2, giảm đau, chống viêm, và chống kết tập tiểu cầu (tác dụng kéo dài 7-10 ngày). Codeine là prodrug, chuyển hóa thành morphine qua CYP2D6. Morphine tác động lên thụ thể mu-opioid ở CNS, giảm đau. Tác dụng hiệp đồng: hiệu quả giảm đau tốt hơn từng thuốc đơn lẻ. Controlled substance - nguy cơ nghiện/lệ thuộc.""",
        "monitoring": [
            "Đáp ứng điều trị: giảm đau",
            "Dấu hiệu chảy máu dạ dày (phân đen, nôn ra máu, đau bụng) - do aspirin",
            "Dấu hiệu ức chế hô hấp (đặc biệt ở trẻ em và người cao tuổi) - do codeine",
            "Dấu hiệu nghiện/lệ thuộc",
            "Tinnitus (ù tai) ở liều cao aspirin"
    ],
        "precautions": [
            "CONTROLLED SUBSTANCE - nguy cơ nghiện/lệ thuộc",
            "CHỐNG CHỈ ĐỊNH với warfarin hoặc thuốc chống đông khác - tăng nguy cơ chảy máu nặng",
            "CHỐNG CHỈ ĐỊNH ở trẻ <12 tuổi (hội chứng Reye với aspirin)",
            "CHỐNG CHỈ ĐỊNH ở trẻ 12-18 tuổi sau phẫu thuật cắt amidan/VA",
            "Nguy cơ chảy máu dạ dày cao - do aspirin, uống với thức ăn",
            "Nguy cơ ức chế hô hấp - đặc biệt ở trẻ em và người cao tuổi",
            "Tránh rượu - tăng tác dụng ức chế CNS, tăng nguy cơ chảy máu dạ dày",
            "Thận trọng ở suy gan, suy thận",
            "Táo bón phổ biến - có thể cần thuốc nhuận tràng"
    ],
        "pharmacokinetics": {
            "half_life": "2-3 giờ (aspirin), 3 giờ (codeine), 2-3 giờ (morphine)",
            "onset": "30 phút",
            "duration": "4-6 giờ",
            "protein_binding": "50-80% (aspirin), 7-25% (codeine)",
            "clearance": "Gan: chuyển hóa (aspirin → salicylic acid, codeine → morphine qua CYP2D6). Thận: thải trừ.",
        },
        "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm. Controlled substance - cần bảo quản an toàn.",
        "black_box_warnings": """CONTROLLED SUBSTANCE - nguy cơ nghiện, lạm dụng, và lệ thuộc. CHỐNG CHỈ ĐỊNH với warfarin hoặc thuốc chống đông khác - tăng nguy cơ chảy máu nặng. CHỐNG CHỈ ĐỊNH ở trẻ <12 tuổi (hội chứng Reye với aspirin). Nguy cơ ức chế hô hấp, đặc biệt ở trẻ em. Nguy cơ chảy máu dạ dày nặng với aspirin. Không dùng trong 3 tháng cuối thai kỳ.""",
        "drug_interactions": {
            "major": [
    {
                    "drug": "Warfarin, các thuốc chống đông khác",
                    "mechanism": "Aspirin ức chế COX-1 tiểu cầu, tăng nguy cơ chảy máu",
                    "effect": "Tăng nguy cơ chảy máu nặng, tăng INR",
                    "management": "CHỐNG CHỈ ĐỊNH. Tránh dùng cùng.",
                },
    {
                    "drug": "Alcohol",
                    "mechanism": "Tăng tác dụng ức chế CNS, tăng nguy cơ chảy máu dạ dày",
                    "effect": "Tăng buồn ngủ, tăng nguy cơ ức chế hô hấp, tăng nguy cơ chảy máu dạ dày nặng",
                    "management": "TRÁNH RƯỢU hoàn toàn khi dùng thuốc này.",
                }
                ],
            "moderate": [
    {
                    "drug": "CNS depressants (Benzodiazepines, Opioids khác)",
                    "mechanism": "Tăng tác dụng ức chế CNS",
                    "effect": "Tăng buồn ngủ, nguy cơ ức chế hô hấp nặng",
                    "management": "Tránh dùng chung hoặc giảm liều.",
                }
                ],
            "minor": [],
        },
        "pregnancy_lactation": {
            "fda_category": "C - D trong tam cá nguyệt 3",
            "pregnancy_details": "Tam cá nguyệt 3: Category D - CHỐNG CHỈ ĐỊNH (do cả aspirin và codeine).",
            "lactation": {
                "safety": "Contraindicated",
                "details": "Cả aspirin và codeine đều bài tiết vào sữa mẹ. Có thể gây tác dụng phụ nghiêm trọng ở trẻ sơ sinh.",
                "recommendation": "KHÔNG dùng khi cho con bú.",
            },
        },
        "hepatic_adjustment": {
            "mild": "Thận trọng",
            "moderate": "Thận trọng, giảm liều",
            "severe": "CHỐNG CHỈ ĐỊNH",
            "notes": "Cả hai thuốc đều chuyển hóa ở gan. Suy gan nặng là chống chỉ định.",
        },
        "overdose_management": {
            "symptoms": [
                "Aspirin quá liều: ù tai, chóng mặt, buồn nôn, nôn, tăng thông khí, kiềm hô hấp, toan chuyển hóa",
                "Codeine quá liều: buồn ngủ nặng, ức chế hô hấp, hôn mê, co đồng tử"
    ],
            "antidote": "Naloxone cho codeine quá liều. Không có antidote đặc hiệu cho aspirin.",
            "treatment": [
                "Nếu quá liều codeine (ức chế hô hấp): Naloxone 0.4-2mg IV/IM, có thể lặp lại",
                "Nếu aspirin quá liều: kiềm hóa nước tiểu (sodium bicarbonate), điều chỉnh điện giải",
                "Đánh giá đường thở, hô hấp, tuần hoàn - QUAN TRỌNG",
                "Hỗ trợ hô hấp nếu cần",
                "Rửa dạ dày nếu trong vòng 1-2 giờ",
                "Than hoạt tính",
                "Theo dõi nồng độ salicylat máu (nếu aspirin quá liều)"
    ],
            "monitoring": "Theo dõi ý thức, hô hấp (QUAN TRỌNG), tim mạch. Nếu aspirin quá liều: theo dõi nồng độ salicylat máu, khí máu, điện giải.",
        },
        "reversal_agents": {
            "available": True,
            "agents": [
    {
                    "agent": "Naloxone",
                    "mechanism": "Đối kháng thụ thể mu-opioid, đảo ngược tác dụng codeine/morphine",
                    "indication": "Codeine quá liều (ức chế hô hấp)",
                    "dose": "0.4-2mg IV/IM, có thể lặp lại mỗi 2-3 phút",
                    "caution": "Tác dụng ngắn (30-90 phút), có thể cần lặp lại",
                }
                ],
        },
        "administration_instructions": {
            "oral": {
                "with_food": "Uống với thức ăn hoặc sữa để giảm kích ứng dạ dày (aspirin)",
                "timing": """Aspirin 325mg/Codeine 15-30mg x 3-4 lần/ngày. KHÔNG vượt quá 4g aspirin/ngày và 240mg codeine/ngày. Controlled substance - cần kê đơn.""",
            },
        },
        "references": {
            "primary_sources": [
                "FDA Drug Label - Co-codaprin (Aspirin/Codeine)",
                "UpToDate - Combination analgesics: Drug information"
    ],
            "last_updated": "2025-02-18",
            "evidence_level": "High - FDA-approved, controlled substance",
        },
            "risk_flags": {
                "high_alert": True,
                "narrow_therapeutic_index": False,
                "bleeding_risk": True,
                "organ_toxicity": ["GI", "CNS"],
                "qt_prolongation": False,
                "hepatotoxicity": False,
                "nephrotoxicity": False,
                "requires_monitoring": ["GI symptoms", "Respiratory status", "CNS status"],
            },
            "guideline_tags": [
                "FDA Drug Information",
                "UpToDate Drug Information",
                "Controlled Substance - Risk of Addiction",
            ]
    },
    "Ibuprofen/Codeine":     {
        "group": "Analgesic - Combination (NSAID + Opioid)",
        "vietnamese_name": "Ibuprofen/Codeine, Nurofen Plus",
        "administration": [
            "PO"
    ],
        "indications": [
            "Đau nhẹ đến trung bình",
            "Đau cơ xương",
            "Đau đầu",
            "Đau răng",
            "Đau không đáp ứng với ibuprofen đơn thuần"
    ],
        "contraindications": {
            "tuyệt_đối": [
                "Dị ứng ibuprofen hoặc codeine",
                "Loét dạ dày tá tràng đang hoạt động",
                "Suy hô hấp nặng",
                "Tắc ruột cơ học",
                "Tam cá nguyệt 3 thai kỳ (3 tháng cuối)",
                "Trẻ em <12 tuổi",
                "Trẻ em 12-18 tuổi sau phẫu thuật cắt amidan/VA"
    ],
            "tương_đối": [
                "Suy thận trung bình - thận trọng",
                "Suy gan trung bình - thận trọng",
                "Tiền sử nghiện/lạm dụng chất - tăng nguy cơ nghiện"
    ],
        },
        "dosage": {
            "adult_standard": "Ibuprofen 200mg/Codeine 12.5-15mg x 3-4 lần/ngày",
            "adult_max": "Ibuprofen 2400mg/ngày, Codeine 240mg/ngày",
            "notes": """Kết hợp ibuprofen (NSAID, giảm đau, chống viêm, hạ sốt) và codeine (opioid yếu, giảm đau). Codeine là prodrug, chuyển hóa thành morphine qua CYP2D6. Tác dụng hiệp đồng. Controlled substance - nguy cơ nghiện.""",
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "Thận trọng, giảm liều",
            "under_30": "Thận trọng, giảm liều codeine",
        },
        "side_effects": [
            "Chảy máu dạ dày (do ibuprofen)",
            "Buồn ngủ (do codeine)",
            "Táo bón (do codeine)",
            "Buồn nôn, nôn",
            "Chóng mặt",
            "Suy thận (do ibuprofen)",
            "Tăng huyết áp (do ibuprofen)",
            "Ức chế hô hấp (do codeine - hiếm nhưng nghiêm trọng)",
            "Nguy cơ nghiện/lệ thuộc (do codeine)"
    ],
        "interactions": [
            "Warfarin: tăng nguy cơ chảy máu nặng",
            "Alcohol: tăng tác dụng ức chế CNS, tăng nguy cơ chảy máu dạ dày",
            "CNS depressants: tăng tác dụng ức chế",
            "ACE inhibitor: giảm hiệu quả, tăng nguy cơ suy thận (ibuprofen)",
            "CYP2D6 inhibitors: giảm chuyển hóa codeine thành morphine"
    ],
        "pregnancy": "C - D trong 3 tháng cuối",
        "mechanism_of_action": """Kết hợp ibuprofen (NSAID, giảm đau, chống viêm, hạ sốt) và codeine (opioid yếu, giảm đau). Ibuprofen ức chế COX-1 và COX-2, giảm đau, chống viêm, và hạ sốt. Codeine là prodrug, chuyển hóa thành morphine qua CYP2D6. Morphine tác động lên thụ thể mu-opioid ở CNS, giảm đau. Tác dụng hiệp đồng: hiệu quả giảm đau và chống viêm tốt hơn từng thuốc đơn lẻ. Controlled substance - nguy cơ nghiện/lệ thuộc.""",
        "monitoring": [
            "Đáp ứng điều trị: giảm đau",
            "Dấu hiệu chảy máu dạ dày - do ibuprofen",
            "Dấu hiệu ức chế hô hấp (đặc biệt ở trẻ em và người cao tuổi) - do codeine",
            "Creatinine, BUN - do ibuprofen",
            "Dấu hiệu nghiện/lệ thuộc"
    ],
        "precautions": [
            "CONTROLLED SUBSTANCE - nguy cơ nghiện/lệ thuộc",
            "CHỐNG CHỈ ĐỊNH ở trẻ <12 tuổi và trẻ 12-18 tuổi sau phẫu thuật cắt amidan/VA",
            "Nguy cơ chảy máu dạ dày - do ibuprofen, uống với thức ăn",
            "Nguy cơ ức chế hô hấp - đặc biệt ở trẻ em và người cao tuổi",
            "Tránh rượu - tăng tác dụng ức chế CNS, tăng nguy cơ chảy máu dạ dày",
            "Không dùng trong 3 tháng cuối thai kỳ",
            "Thận trọng ở suy gan, suy thận",
            "Táo bón phổ biến - có thể cần thuốc nhuận tràng"
    ],
        "pharmacokinetics": {
            "half_life": "2 giờ (ibuprofen), 3 giờ (codeine), 2-3 giờ (morphine)",
            "onset": "30 phút",
            "duration": "4-6 giờ",
            "protein_binding": "99% (ibuprofen), 7-25% (codeine)",
            "clearance": "Gan: chuyển hóa (ibuprofen qua CYP2C9, codeine → morphine qua CYP2D6). Thận: thải trừ.",
        },
        "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm. Controlled substance - cần bảo quản an toàn.",
        "black_box_warnings": """CONTROLLED SUBSTANCE - nguy cơ nghiện, lạm dụng, và lệ thuộc. Nguy cơ ức chế hô hấp, đặc biệt ở trẻ em. CHỐNG CHỈ ĐỊNH ở trẻ <12 tuổi và trẻ 12-18 tuổi sau phẫu thuật cắt amidan/VA. Nguy cơ chảy máu dạ dày với ibuprofen. Không dùng trong 3 tháng cuối thai kỳ. NSAID có thể gây tăng nguy cơ nhồi máu cơ tim và đột quỵ.""",
        "drug_interactions": {
            "major": [
    {
                    "drug": "Warfarin, các thuốc chống đông khác",
                    "mechanism": "Ibuprofen ức chế COX, chống kết tập tiểu cầu, tăng nguy cơ chảy máu",
                    "effect": "Tăng nguy cơ chảy máu nặng, tăng INR",
                    "management": "Tránh dùng đồng thời hoặc theo dõi INR chặt chẽ.",
                },
    {
                    "drug": "Alcohol",
                    "mechanism": "Tăng tác dụng ức chế CNS, tăng nguy cơ chảy máu dạ dày",
                    "effect": "Tăng buồn ngủ, tăng nguy cơ ức chế hô hấp, tăng nguy cơ chảy máu dạ dày nặng",
                    "management": "TRÁNH RƯỢU hoàn toàn khi dùng thuốc này.",
                }
                ],
            "moderate": [
    {
                    "drug": "CNS depressants (Benzodiazepines, Opioids khác)",
                    "mechanism": "Tăng tác dụng ức chế CNS",
                    "effect": "Tăng buồn ngủ, nguy cơ ức chế hô hấp nặng",
                    "management": "Tránh dùng chung hoặc giảm liều.",
                }
                ],
            "minor": [],
        },
        "pregnancy_lactation": {
            "fda_category": "C - D trong tam cá nguyệt 3",
            "pregnancy_details": "Tam cá nguyệt 3: Category D - CHỐNG CHỈ ĐỊNH (do cả ibuprofen và codeine).",
            "lactation": {
                "safety": "Contraindicated",
                "details": "Cả ibuprofen và codeine đều bài tiết vào sữa mẹ. Có thể gây tác dụng phụ nghiêm trọng ở trẻ sơ sinh.",
                "recommendation": "KHÔNG dùng khi cho con bú.",
            },
        },
        "hepatic_adjustment": {
            "mild": "Thận trọng",
            "moderate": "Thận trọng, giảm liều",
            "severe": "CHỐNG CHỈ ĐỊNH",
            "notes": "Cả hai thuốc đều chuyển hóa ở gan. Suy gan nặng là chống chỉ định.",
        },
        "overdose_management": {
            "symptoms": [
                "Ibuprofen quá liều: buồn nôn, nôn, đau bụng, chảy máu dạ dày, suy thận cấp",
                "Codeine quá liều: buồn ngủ nặng, ức chế hô hấp, hôn mê, co đồng tử"
    ],
            "antidote": "Naloxone cho codeine quá liều. Không có antidote đặc hiệu cho ibuprofen.",
            "treatment": [
                "Nếu quá liều codeine (ức chế hô hấp): Naloxone 0.4-2mg IV/IM, có thể lặp lại",
                "Đánh giá đường thở, hô hấp, tuần hoàn - QUAN TRỌNG",
                "Hỗ trợ hô hấp nếu cần",
                "Rửa dạ dày nếu trong vòng 1-2 giờ",
                "Than hoạt tính",
                "Theo dõi chức năng thận (ibuprofen quá liều)"
    ],
            "monitoring": "Theo dõi ý thức, hô hấp (QUAN TRỌNG), tim mạch. Nếu ibuprofen quá liều: theo dõi chức năng thận, dấu hiệu chảy máu.",
        },
        "reversal_agents": {
            "available": True,
            "agents": [
    {
                    "agent": "Naloxone",
                    "mechanism": "Đối kháng thụ thể mu-opioid, đảo ngược tác dụng codeine/morphine",
                    "indication": "Codeine quá liều (ức chế hô hấp)",
                    "dose": "0.4-2mg IV/IM, có thể lặp lại mỗi 2-3 phút",
                    "caution": "Tác dụng ngắn (30-90 phút), có thể cần lặp lại",
                }
                ],
        },
        "administration_instructions": {
            "oral": {
                "with_food": "Uống với thức ăn để giảm kích ứng dạ dày (ibuprofen)",
                "timing": """Ibuprofen 200mg/Codeine 12.5-15mg x 3-4 lần/ngày. KHÔNG vượt quá 2400mg ibuprofen/ngày và 240mg codeine/ngày. Controlled substance - cần kê đơn.""",
            },
        },
        "references": {
            "primary_sources": [
                "FDA Drug Label - Nurofen Plus (Ibuprofen/Codeine)",
                "UpToDate - Combination analgesics: Drug information"
    ],
            "last_updated": "2025-02-18",
            "evidence_level": "High - FDA-approved, controlled substance",
        },
            "risk_flags": {
                "high_alert": True,
                "narrow_therapeutic_index": False,
                "bleeding_risk": True,
                "organ_toxicity": ["GI", "renal", "CNS"],
                "qt_prolongation": False,
                "hepatotoxicity": False,
                "nephrotoxicity": True,
                "requires_monitoring": ["GI symptoms", "RFT", "Respiratory status", "CNS status"],
            },
            "guideline_tags": [
                "FDA Drug Information",
                "UpToDate Drug Information",
                "Controlled Substance - Risk of Addiction",
            ]
    },
    "Diclofenac/Thiocolchicoside":     {
        "group": "Analgesic - Combination (NSAID + Muscle Relaxant)",
        "vietnamese_name": "Diclofenac/Thiocolchicoside, Decontractyl",
        "administration": [
            "PO"
    ],
        "indications": [
            "Đau cơ xương khớp kèm co thắt cơ và viêm",
            "Đau lưng cấp tính",
            "Đau cơ sau chấn thương",
            "Viêm khớp kèm co thắt cơ"
    ],
        "contraindications": {
            "tuyệt_đối": [
                "Dị ứng diclofenac hoặc thiocolchicoside",
                "Loét dạ dày tá tràng đang hoạt động",
                "Tam cá nguyệt 3 thai kỳ (3 tháng cuối)",
                "Suy thận nặng",
                "Suy gan nặng"
    ],
            "tương_đối": [
                "Suy thận trung bình - thận trọng",
                "Suy gan trung bình - thận trọng"
    ],
        },
        "dosage": {
            "adult_standard": "Diclofenac 50mg/Thiocolchicoside 4-8mg x 2-3 lần/ngày",
            "adult_max": "Diclofenac 150mg/ngày, Thiocolchicoside 24mg/ngày",
            "notes": """Kết hợp diclofenac (NSAID, giảm đau, chống viêm) và thiocolchicoside (giãn cơ xương khớp). Tác dụng hiệp đồng: giảm đau cơ xương khớp kèm viêm và co thắt cơ. CHỈ dùng ngắn hạn (2-3 tuần).""",
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "Thận trọng, giảm liều",
            "under_30": "Tránh dùng",
        },
        "side_effects": [
            "Chảy máu dạ dày (do diclofenac)",
            "Buồn ngủ (do thiocolchicoside)",
            "Chóng mặt",
            "Mệt mỏi",
            "Suy thận (do diclofenac)",
            "Tăng huyết áp (do diclofenac)",
            "Tăng men gan (do diclofenac)"
    ],
        "interactions": [
            "Warfarin: tăng nguy cơ chảy máu nặng",
            "Alcohol: tăng tác dụng an thần, tăng nguy cơ chảy máu dạ dày",
            "CNS depressants: tăng tác dụng ức chế",
            "ACE inhibitor: giảm hiệu quả, tăng nguy cơ suy thận (diclofenac)"
    ],
        "pregnancy": "C - D trong 3 tháng cuối",
        "mechanism_of_action": """Kết hợp diclofenac (NSAID, giảm đau, chống viêm) và thiocolchicoside (giãn cơ xương khớp). Diclofenac ức chế COX-1 và COX-2, giảm đau và chống viêm. Thiocolchicoside là thuốc giãn cơ xương khớp, tác động lên tủy sống để giảm phản xạ cơ xương. Tác dụng hiệp đồng: giảm đau cơ xương khớp kèm viêm và co thắt cơ. CHỈ dùng ngắn hạn (2-3 tuần).""",
        "monitoring": [
            "Đáp ứng điều trị: giảm đau, giảm viêm, giảm co thắt cơ",
            "Dấu hiệu chảy máu dạ dày (phân đen, nôn ra máu, đau bụng) - do diclofenac",
            "Creatinine, BUN - do diclofenac",
            "Chức năng gan (ALT, AST) - do diclofenac"
    ],
        "precautions": [
            "CHỈ dùng ngắn hạn (2-3 tuần)",
            "NGUY CƠ CHẢY MÁU DẠ DÀY - do diclofenac, uống với thức ăn",
            "Tránh rượu - tăng tác dụng an thần, tăng nguy cơ chảy máu dạ dày",
            "Không dùng trong 3 tháng cuối thai kỳ",
            "Thận trọng ở suy gan, suy thận",
            "Theo dõi chức năng gan và thận"
    ],
        "pharmacokinetics": {
            "half_life": "1-2 giờ (diclofenac), 1-2 giờ (thiocolchicoside)",
            "onset": "30 phút",
            "duration": "6-8 giờ",
            "protein_binding": "99% (diclofenac), không đáng kể (thiocolchicoside)",
            "clearance": "Gan: chuyển hóa. Thận: thải trừ.",
        },
        "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm",
        "black_box_warnings": """Không dùng trong 3 tháng cuối thai kỳ - có thể gây đóng ống động mạch sớm. Nguy cơ chảy máu dạ dày nặng với diclofenac. NSAID có thể gây tăng nguy cơ nhồi máu cơ tim và đột quỵ. Chỉ dùng ngắn hạn (2-3 tuần).""",
        "drug_interactions": {
            "major": [
    {
                    "drug": "Warfarin, các thuốc chống đông khác",
                    "mechanism": "Diclofenac ức chế COX, chống kết tập tiểu cầu, tăng nguy cơ chảy máu",
                    "effect": "Tăng nguy cơ chảy máu nặng, tăng INR",
                    "management": "Tránh dùng đồng thời hoặc theo dõi INR chặt chẽ.",
                }
                ],
            "moderate": [
    {
                    "drug": "ACE inhibitor, ARB",
                    "mechanism": "Diclofenac giảm tổng hợp prostaglandin → giảm lưu lượng máu thận",
                    "effect": "Giảm hiệu quả, tăng nguy cơ suy thận",
                    "management": "Thận trọng. Theo dõi creatinine, BUN.",
                }
                ],
            "minor": [],
        },
        "pregnancy_lactation": {
            "fda_category": "C - D trong tam cá nguyệt 3",
            "pregnancy_details": "Tam cá nguyệt 3: CHỐNG CHỈ ĐỊNH (do diclofenac).",
            "lactation": {
                "safety": "Caution",
                "details": "Cả hai thuốc đều bài tiết vào sữa mẹ. Có thể gây tác dụng phụ ở trẻ.",
                "recommendation": "Thận trọng khi cho con bú.",
            },
        },
        "hepatic_adjustment": {
            "mild": "Thận trọng",
            "moderate": "Tránh dùng",
            "severe": "CHỐNG CHỈ ĐỊNH",
            "notes": "Diclofenac chuyển hóa ở gan, nguy cơ tăng men gan. Suy gan nặng là chống chỉ định.",
        },
        "overdose_management": {
            "symptoms": [
                "Diclofenac quá liều: buồn nôn, nôn, đau bụng, chảy máu dạ dày, suy thận cấp",
                "Thiocolchicoside quá liều: buồn ngủ nặng, ức chế hô hấp"
    ],
            "antidote": "Không có antidote đặc hiệu",
            "treatment": [
                "Đánh giá đường thở, hô hấp, tuần hoàn",
                "Rửa dạ dày nếu trong vòng 1-2 giờ",
                "Than hoạt tính",
                "Điều trị hỗ trợ",
                "Theo dõi chức năng thận và gan"
    ],
            "monitoring": "Theo dõi ý thức, hô hấp, tim mạch. Theo dõi chức năng thận, gan, dấu hiệu chảy máu.",
        },
        "reversal_agents": {
            "available": False,
            "agents": [],
        },
        "administration_instructions": {
            "oral": {
                "with_food": "Uống với thức ăn để giảm kích ứng dạ dày (diclofenac)",
                "timing": """Diclofenac 50mg/Thiocolchicoside 4-8mg x 2-3 lần/ngày. CHỈ dùng ngắn hạn (2-3 tuần).""",
            },
        },
        "references": {
            "primary_sources": [
                "FDA Drug Label - Decontractyl (Diclofenac/Thiocolchicoside)",
                "UpToDate - Combination analgesics: Drug information"
    ],
            "last_updated": "2025-02-18",
            "evidence_level": "High - FDA-approved",
        },
            "risk_flags": {
                "high_alert": False,
                "narrow_therapeutic_index": False,
                "bleeding_risk": True,
                "organ_toxicity": ["GI", "renal", "hepatic"],
                "qt_prolongation": False,
                "hepatotoxicity": True,
                "nephrotoxicity": True,
                "requires_monitoring": ["LFT", "RFT", "GI symptoms"],
            },
            "guideline_tags": [
                "FDA Drug Information",
                "UpToDate Drug Information",
            ]
    },
    "Paracetamol/Diphenhydramine":     {
        "group": "Analgesic - Combination (Paracetamol + Antihistamine)",
        "vietnamese_name": "Paracetamol/Diphenhydramine, Tylenol PM",
        "administration": [
            "PO"
    ],
        "indications": [
            "Đau nhẹ đến trung bình kèm mất ngủ",
            "Đau đầu kèm mất ngủ",
            "Đau cơ xương kèm mất ngủ",
            "Sốt kèm mất ngủ"
    ],
        "contraindications": {
            "tuyệt_đối": [
                "Dị ứng paracetamol hoặc diphenhydramine",
                "Suy gan nặng",
                "Glaucoma góc đóng",
                "Phì đại tuyến tiền liệt",
                "Tắc ruột cơ học"
    ],
            "tương_đối": [
                "Suy gan trung bình - thận trọng",
                "Người cao tuổi - tăng nhạy cảm với anticholinergic",
                "Bệnh tim mạch - thận trọng"
    ],
        },
        "dosage": {
            "adult_standard": "Paracetamol 500mg/Diphenhydramine 25-50mg x 1-2 lần/ngày (trước khi ngủ)",
            "adult_max": "Paracetamol 4g/ngày, Diphenhydramine 300mg/ngày",
            "notes": """Kết hợp paracetamol (giảm đau, hạ sốt) và diphenhydramine (antihistamine H1, an thần). Diphenhydramine có tác dụng an thần, giúp ngủ. Tác dụng hiệp đồng: giảm đau và giúp ngủ. KHÔNG vượt quá 4g paracetamol/ngày. Thường dùng trước khi ngủ.""",
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "Thận trọng",
            "under_30": "Thận trọng",
        },
        "side_effects": [
            "Buồn ngủ (do diphenhydramine)",
            "Chóng mặt",
            "Khô miệng (do diphenhydramine - anticholinergic)",
            "Nhìn mờ",
            "Bí tiểu (đặc biệt ở nam giới có phì đại tuyến tiền liệt)",
            "Độc gan (do paracetamol - nếu quá liều)",
            "Tăng nhịp tim (do diphenhydramine)"
    ],
        "interactions": [
            "Alcohol: tăng tác dụng an thần, tăng nguy cơ độc gan",
            "Warfarin: tăng nguy cơ chảy máu",
            "CNS depressants: tăng tác dụng ức chế",
            "Thuốc kháng cholinergic khác: tăng tác dụng phụ anticholinergic",
            "MAO inhibitors: tăng nguy cơ tác dụng phụ"
    ],
        "pregnancy": "C",
        "mechanism_of_action": """Kết hợp paracetamol (giảm đau, hạ sốt) và diphenhydramine (antihistamine H1, an thần). Paracetamol ức chế COX-3 ở CNS, giảm đau và hạ sốt. Diphenhydramine là antihistamine H1 thế hệ 1, có tác dụng anticholinergic mạnh, gây an thần và buồn ngủ. Tác dụng hiệp đồng: giảm đau và giúp ngủ. Thường dùng trước khi ngủ.""",
        "monitoring": [
            "Đáp ứng điều trị: giảm đau, cải thiện giấc ngủ",
            "Dấu hiệu tác dụng phụ anticholinergic (khô miệng, nhìn mờ, bí tiểu)",
            "Chức năng gan (nếu dùng >4g paracetamol/ngày)",
            "Dấu hiệu quá liều paracetamol"
    ],
        "precautions": [
            "Tác dụng an thần mạnh - không lái xe hoặc vận hành máy móc sau khi uống",
            "Tác dụng phụ anticholinergic - khô miệng, nhìn mờ, bí tiểu (đặc biệt ở nam giới có phì đại tuyến tiền liệt)",
            "CHỐNG CHỈ ĐỊNH ở glaucoma góc đóng, phì đại tuyến tiền liệt, tắc ruột cơ học",
            "KHÔNG vượt quá 4g paracetamol/ngày - nguy cơ độc gan",
            "Tránh rượu - tăng tác dụng an thần, tăng nguy cơ độc gan",
            "Thận trọng ở bệnh nhân cao tuổi - tăng nhạy cảm với tác dụng anticholinergic",
            "Thường dùng trước khi ngủ"
    ],
        "pharmacokinetics": {
            "half_life": "1-3 giờ (paracetamol), 2-8 giờ (diphenhydramine)",
            "onset": "30 phút",
            "duration": "4-6 giờ",
            "protein_binding": "10-25% (paracetamol), 98-99% (diphenhydramine)",
            "clearance": "Gan: chuyển hóa. Thận: thải trừ.",
        },
        "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm",
        "black_box_warnings": """Nguy cơ độc gan nghiêm trọng với paracetamol nếu quá liều (>4g/ngày). CHỐNG CHỈ ĐỊNH ở glaucoma góc đóng, phì đại tuyến tiền liệt, tắc ruột cơ học. Tác dụng an thần mạnh - không lái xe sau khi uống.""",
        "drug_interactions": {
            "major": [
    {
                    "drug": "Alcohol",
                    "mechanism": "Tăng tác dụng ức chế CNS, tăng nguy cơ độc gan",
                    "effect": "Tăng buồn ngủ, tăng nguy cơ độc gan nặng",
                    "management": "TRÁNH RƯỢU hoàn toàn khi dùng thuốc này.",
                },
    {
                    "drug": "Thuốc kháng cholinergic khác (Atropine, Scopolamine, Orphenadrine)",
                    "mechanism": "Tác dụng cộng dồn anticholinergic",
                    "effect": "Tăng tác dụng phụ anticholinergic (khô miệng nặng, bí tiểu, nhìn mờ)",
                    "management": "Tránh dùng chung nếu có thể.",
                }
                ],
            "moderate": [
    {
                    "drug": "CNS depressants (Benzodiazepines, Opioids)",
                    "mechanism": "Tăng tác dụng ức chế CNS",
                    "effect": "Tăng buồn ngủ, nguy cơ ức chế hô hấp",
                    "management": "Thận trọng. Giảm liều nếu cần.",
                }
                ],
            "minor": [],
        },
        "pregnancy_lactation": {
            "fda_category": "C",
            "pregnancy_details": "Category C. Có thể dùng nếu lợi ích > nguy cơ.",
            "lactation": {
                "safety": "Caution",
                "details": "Cả hai thuốc đều bài tiết vào sữa mẹ. Có thể gây tác dụng phụ ở trẻ (buồn ngủ, kích thích).",
                "recommendation": "Thận trọng khi cho con bú.",
            },
        },
        "hepatic_adjustment": {
            "mild": "Thận trọng",
            "moderate": "Thận trọng, giảm liều",
            "severe": "CHỐNG CHỈ ĐỊNH",
            "notes": "Paracetamol chuyển hóa ở gan, nguy cơ độc gan. Suy gan nặng là chống chỉ định.",
        },
        "overdose_management": {
            "symptoms": [
                "Paracetamol quá liều: buồn nôn, nôn, đau bụng, vàng da, suy gan",
                "Diphenhydramine quá liều: buồn ngủ nặng, nhìn mờ, khô miệng nặng, bí tiểu, ảo giác, co giật"
    ],
            "antidote": "N-acetylcysteine (NAC) cho paracetamol quá liều. Physostigmine cho diphenhydramine quá liều nặng.",
            "treatment": [
                "Nếu quá liều paracetamol (>150mg/kg): N-acetylcysteine (NAC) ngay lập tức",
                "Đánh giá đường thở, hô hấp, tuần hoàn",
                "Rửa dạ dày nếu trong vòng 1-2 giờ",
                "Than hoạt tính",
                "Nếu diphenhydramine quá liều nặng (ảo giác, co giật, rối loạn ý thức): Physostigmine có thể được xem xét",
                "Theo dõi chức năng gan (paracetamol quá liều)"
    ],
            "monitoring": "Theo dõi ý thức, hô hấp, tim mạch, nhịp tim. Nếu paracetamol quá liều: theo dõi chức năng gan (ALT, AST, bilirubin, INR).",
        },
        "reversal_agents": {
            "available": True,
            "agents": [
    {
                    "agent": "N-acetylcysteine (NAC)",
                    "mechanism": "Chống độc cho paracetamol quá liều",
                    "indication": "Quá liều paracetamol (>150mg/kg hoặc >10g)",
                    "dose": "Theo phác đồ điều trị quá liều paracetamol",
                    "caution": "Chỉ hiệu quả nếu dùng trong vòng 8-10 giờ sau khi uống paracetamol",
                },
    {
                    "agent": "Physostigmine",
                    "mechanism": "Chất ức chế cholinesterase, đảo ngược tác dụng anticholinergic",
                    "indication": "Diphenhydramine quá liều nặng (ảo giác, co giật, rối loạn ý thức)",
                    "dose": "0.5-2mg IV, có thể lặp lại",
                    "caution": "Chỉ dùng khi quá liều nặng, cần theo dõi chặt chẽ",
                }
                ],
        },
        "administration_instructions": {
            "oral": {
                "with_food": "Có thể uống với thức ăn hoặc không",
                "timing": """Paracetamol 500mg/Diphenhydramine 25-50mg x 1-2 lần/ngày (thường trước khi ngủ). KHÔNG vượt quá 4g paracetamol/ngày và 300mg diphenhydramine/ngày. KHÔNG lái xe sau khi uống.""",
            },
        },
        "references": {
            "primary_sources": [
                "FDA Drug Label - Tylenol PM (Paracetamol/Diphenhydramine)",
                "UpToDate - Combination analgesics: Drug information"
    ],
            "last_updated": "2025-02-18",
            "evidence_level": "High - FDA-approved",
        },
            "risk_flags": {
                "high_alert": False,
                "narrow_therapeutic_index": False,
                "bleeding_risk": False,
                "organ_toxicity": ["hepatic", "CNS"],
                "qt_prolongation": False,
                "hepatotoxicity": True,
                "nephrotoxicity": False,
                "requires_monitoring": ["LFT", "CNS status"],
            },
            "guideline_tags": [
                "FDA Drug Information",
                "UpToDate Drug Information",
            ]
    },
    "Paracetamol/Codeine/Caffeine":     {
        "group": "Analgesic - Combination (Paracetamol + Opioid + Stimulant)",
        "vietnamese_name": "Paracetamol/Codeine/Caffeine, Panadeine Forte, Solpadeine",
        "administration": [
            "PO"
    ],
        "indications": [
            "Đau nhẹ đến trung bình",
            "Đau đầu",
            "Đau răng",
            "Đau cơ xương",
            "Đau không đáp ứng với paracetamol đơn thuần"
    ],
        "contraindications": {
            "tuyệt_đối": [
                "Dị ứng paracetamol, codeine hoặc caffeine",
                "Suy gan nặng",
                "Suy hô hấp nặng",
                "Tắc ruột cơ học",
                "Rối loạn lo âu nặng",
                "Rối loạn giấc ngủ nặng",
                "Trẻ em <12 tuổi",
                "Trẻ em 12-18 tuổi sau phẫu thuật cắt amidan/VA"
    ],
            "tương_đối": [
                "Suy gan trung bình - thận trọng",
                "Suy thận - thận trọng",
                "Tiền sử nghiện/lạm dụng chất - tăng nguy cơ nghiện",
                "Bệnh tim mạch - thận trọng (do caffeine)",
                "Loét dạ dày - thận trọng (do caffeine)"
    ],
        },
        "dosage": {
            "adult_standard": "Paracetamol 500mg/Codeine 15-30mg/Caffeine 30-50mg x 3-4 lần/ngày",
            "adult_max": "Paracetamol 4g/ngày, Codeine 240mg/ngày, Caffeine 400mg/ngày",
            "notes": """Kết hợp paracetamol (giảm đau, hạ sốt), codeine (opioid yếu, giảm đau) và caffeine (kích thích, tăng cường tác dụng giảm đau). Caffeine có thể tăng cường tác dụng giảm đau của paracetamol và codeine, đồng thời giúp giảm mệt mỏi và buồn ngủ do codeine. Codeine là prodrug, chuyển hóa thành morphine qua CYP2D6. Tác dụng hiệp đồng. Controlled substance - nguy cơ nghiện. KHÔNG vượt quá 4g paracetamol/ngày. Tránh dùng gần giờ ngủ do caffeine.""",
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "Thận trọng",
            "under_30": "Thận trọng, giảm liều codeine",
        },
        "side_effects": [
            "Buồn ngủ (do codeine) - ít hơn do caffeine đối kháng",
            "Mất ngủ (do caffeine)",
            "Bồn chồn, lo âu (do caffeine)",
            "Tăng nhịp tim (do caffeine)",
            "Táo bón (do codeine)",
            "Buồn nôn, nôn",
            "Chóng mặt",
            "Ức chế hô hấp (do codeine - hiếm nhưng nghiêm trọng)",
            "Độc gan (do paracetamol - nếu quá liều)",
            "Nguy cơ nghiện/lệ thuộc (do codeine)"
    ],
        "interactions": [
            "Alcohol: tăng tác dụng ức chế CNS, tăng nguy cơ độc gan",
            "Warfarin: tăng nguy cơ chảy máu",
            "CNS depressants: tăng tác dụng ức chế (codeine)",
            "CNS stimulants: tăng tác dụng kích thích (caffeine)",
            "CYP2D6 inhibitors: giảm chuyển hóa codeine thành morphine",
            "MAO inhibitors: tăng nguy cơ tác dụng phụ với caffeine"
    ],
        "pregnancy": "C - D trong 3 tháng cuối",
        "mechanism_of_action": """Kết hợp paracetamol (giảm đau, hạ sốt), codeine (opioid yếu, giảm đau) và caffeine (kích thích, tăng cường tác dụng giảm đau). Paracetamol ức chế COX-3 ở CNS, giảm đau và hạ sốt. Codeine là prodrug, chuyển hóa thành morphine qua CYP2D6. Morphine tác động lên thụ thể mu-opioid ở CNS, giảm đau. Caffeine là chất kích thích CNS, có thể tăng cường tác dụng giảm đau của paracetamol và codeine thông qua nhiều cơ chế (tăng hấp thu, tăng tác dụng tại thụ thể adenosine, đối kháng tác dụng buồn ngủ của codeine). Tác dụng hiệp đồng: hiệu quả giảm đau tốt hơn và giảm buồn ngủ so với Paracetamol/Codeine đơn thuần. Controlled substance - nguy cơ nghiện/lệ thuộc.""",
        "monitoring": [
            "Đáp ứng điều trị: giảm đau",
            "Dấu hiệu ức chế hô hấp (đặc biệt ở trẻ em và người cao tuổi) - do codeine",
            "Dấu hiệu kích thích quá mức (bồn chồn, lo âu, mất ngủ) - do caffeine",
            "Nhịp tim (tăng nhịp tim do caffeine)",
            "Chức năng gan (nếu dùng >4g paracetamol/ngày)",
            "Dấu hiệu nghiện/lệ thuộc",
            "Dấu hiệu quá liều paracetamol"
    ],
        "precautions": [
            "CONTROLLED SUBSTANCE - nguy cơ nghiện/lệ thuộc",
            "KHÔNG vượt quá 4g paracetamol/ngày - nguy cơ độc gan",
            "CHỐNG CHỈ ĐỊNH ở trẻ <12 tuổi và trẻ 12-18 tuổi sau phẫu thuật cắt amidan/VA",
            "Nguy cơ ức chế hô hấp - đặc biệt ở trẻ em và người cao tuổi",
            "Nguy cơ mất ngủ, bồn chồn - do caffeine, tránh dùng gần giờ ngủ",
            "Thận trọng ở bệnh nhân có bệnh tim mạch, loét dạ dày - do caffeine",
            "Tránh rượu - tăng tác dụng ức chế CNS, tăng nguy cơ độc gan",
            "Thận trọng ở suy gan, suy thận",
            "Táo bón phổ biến - có thể cần thuốc nhuận tràng"
    ],
        "pharmacokinetics": {
            "half_life": "1-3 giờ (paracetamol), 3 giờ (codeine), 2-3 giờ (morphine), 3-5 giờ (caffeine)",
            "onset": "30 phút",
            "duration": "4-6 giờ",
            "protein_binding": "10-25% (paracetamol), 7-25% (codeine), 36% (caffeine)",
            "clearance": "Gan: chuyển hóa (codeine → morphine qua CYP2D6, caffeine qua CYP1A2). Thận: thải trừ.",
        },
        "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm. Controlled substance - cần bảo quản an toàn.",
        "black_box_warnings": """CONTROLLED SUBSTANCE - nguy cơ nghiện, lạm dụng, và lệ thuộc. Nguy cơ ức chế hô hấp, đặc biệt ở trẻ em. CHỐNG CHỈ ĐỊNH ở trẻ <12 tuổi và trẻ 12-18 tuổi sau phẫu thuật cắt amidan/VA. Nguy cơ độc gan nghiêm trọng với paracetamol nếu quá liều (>4g/ngày). Caffeine có thể gây mất ngủ, bồn chồn, tăng nhịp tim.""",
        "drug_interactions": {
            "major": [
    {
                    "drug": "Alcohol",
                    "mechanism": "Tăng tác dụng ức chế CNS, tăng nguy cơ độc gan",
                    "effect": "Tăng buồn ngủ, tăng nguy cơ ức chế hô hấp, tăng nguy cơ độc gan nặng",
                    "management": "TRÁNH RƯỢU hoàn toàn khi dùng thuốc này.",
                },
    {
                    "drug": "CNS stimulants (Amphetamines, Methylphenidate)",
                    "mechanism": "Tăng tác dụng kích thích CNS",
                    "effect": "Tăng bồn chồn, lo âu, mất ngủ, tăng nhịp tim",
                    "management": "Tránh dùng chung hoặc giảm liều caffeine.",
                }
                ],
            "moderate": [
    {
                    "drug": "CNS depressants (Benzodiazepines, Opioids khác)",
                    "mechanism": "Tăng tác dụng ức chế CNS (codeine)",
                    "effect": "Tăng buồn ngủ, nguy cơ ức chế hô hấp nặng",
                    "management": "Thận trọng. Giảm liều nếu cần.",
                },
    {
                    "drug": "MAO inhibitors",
                    "mechanism": "Tăng nguy cơ tác dụng phụ với caffeine",
                    "effect": "Tăng nguy cơ tác dụng phụ nghiêm trọng",
                    "management": "Tránh dùng chung.",
                }
                ],
            "minor": [],
        },
        "pregnancy_lactation": {
            "fda_category": "C - D trong tam cá nguyệt 3",
            "pregnancy_details": "Tam cá nguyệt 3: Category D - CHỐNG CHỈ ĐỊNH (do codeine). Caffeine: Category C - thận trọng, giới hạn <200mg/ngày.",
            "lactation": {
                "safety": "Contraindicated",
                "details": "Codeine bài tiết vào sữa mẹ, có thể gây ức chế hô hấp ở trẻ sơ sinh. Caffeine bài tiết vào sữa mẹ.",
                "recommendation": "KHÔNG dùng khi cho con bú.",
            },
        },
        "hepatic_adjustment": {
            "mild": "Thận trọng",
            "moderate": "Thận trọng, giảm liều",
            "severe": "CHỐNG CHỈ ĐỊNH",
            "notes": "Paracetamol và codeine chuyển hóa ở gan. Caffeine chuyển hóa ở gan qua CYP1A2. Suy gan nặng là chống chỉ định.",
        },
        "overdose_management": {
            "symptoms": [
                "Paracetamol quá liều: buồn nôn, nôn, đau bụng, vàng da, suy gan",
                "Codeine quá liều: buồn ngủ nặng, ức chế hô hấp, hôn mê, co đồng tử",
                "Caffeine quá liều: bồn chồn, lo âu, mất ngủ, tăng nhịp tim, run, co giật"
    ],
            "antidote": "N-acetylcysteine (NAC) cho paracetamol quá liều. Naloxone cho codeine quá liều.",
            "treatment": [
                "Nếu quá liều paracetamol (>150mg/kg): N-acetylcysteine (NAC) ngay lập tức",
                "Nếu quá liều codeine (ức chế hô hấp): Naloxone 0.4-2mg IV/IM, có thể lặp lại",
                "Nếu caffeine quá liều: điều trị hỗ trợ, benzodiazepine cho co giật nếu có",
                "Đánh giá đường thở, hô hấp, tuần hoàn - QUAN TRỌNG",
                "Hỗ trợ hô hấp nếu cần",
                "Rửa dạ dày nếu trong vòng 1-2 giờ",
                "Than hoạt tính",
                "Theo dõi chức năng gan (paracetamol quá liều), nhịp tim (caffeine quá liều)"
    ],
            "monitoring": "Theo dõi ý thức, hô hấp (QUAN TRỌNG), tim mạch, nhịp tim. Nếu paracetamol quá liều: theo dõi chức năng gan (ALT, AST, bilirubin, INR).",
        },
        "reversal_agents": {
            "available": True,
            "agents": [
    {
                    "agent": "N-acetylcysteine (NAC)",
                    "mechanism": "Chống độc cho paracetamol quá liều",
                    "indication": "Quá liều paracetamol (>150mg/kg hoặc >10g)",
                    "dose": "Theo phác đồ điều trị quá liều paracetamol",
                    "caution": "Chỉ hiệu quả nếu dùng trong vòng 8-10 giờ sau khi uống paracetamol",
                },
    {
                    "agent": "Naloxone",
                    "mechanism": "Đối kháng thụ thể mu-opioid, đảo ngược tác dụng codeine/morphine",
                    "indication": "Codeine quá liều (ức chế hô hấp)",
                    "dose": "0.4-2mg IV/IM, có thể lặp lại mỗi 2-3 phút",
                    "caution": "Tác dụng ngắn (30-90 phút), có thể cần lặp lại",
                }
                ],
        },
        "administration_instructions": {
            "oral": {
                "with_food": "Có thể uống với thức ăn hoặc không",
                "timing": """Paracetamol 500mg/Codeine 15-30mg/Caffeine 30-50mg x 3-4 lần/ngày. KHÔNG vượt quá 4g paracetamol/ngày và 240mg codeine/ngày. TRÁNH dùng gần giờ ngủ do caffeine. Controlled substance - cần kê đơn.""",
            },
        },
        "references": {
            "primary_sources": [
                "FDA Drug Label - Panadeine Forte (Paracetamol/Codeine/Caffeine)",
                "UpToDate - Combination analgesics: Drug information"
    ],
            "last_updated": "2025-02-18",
            "evidence_level": "High - FDA-approved, controlled substance",
        },
            "risk_flags": {
                "high_alert": True,
                "narrow_therapeutic_index": False,
                "bleeding_risk": False,
                "organ_toxicity": ["hepatic", "CNS", "cardiac"],
                "qt_prolongation": False,
                "hepatotoxicity": True,
                "nephrotoxicity": False,
                "requires_monitoring": ["LFT", "Respiratory status", "CNS status", "Heart rate"],
            },
            "guideline_tags": [
                "FDA Drug Information",
                "UpToDate Drug Information",
                "Controlled Substance - Risk of Addiction",
            ]
    },
    "Paracetamol/Codeine/Promethazine":     {
        "group": "Analgesic - Combination (Paracetamol + Opioid + Antihistamine)",
        "vietnamese_name": "Paracetamol/Codeine/Promethazine, Phenergan with Codeine",
        "administration": [
            "PO"
    ],
        "indications": [
            "Đau nhẹ đến trung bình kèm buồn nôn",
            "Đau kèm mất ngủ",
            "Đau sau phẫu thuật",
            "Đau không đáp ứng với paracetamol đơn thuần"
    ],
        "contraindications": {
            "tuyệt_đối": [
                "Dị ứng paracetamol, codeine hoặc promethazine",
                "Suy gan nặng",
                "Suy hô hấp nặng",
                "Tắc ruột cơ học",
                "Glaucoma góc đóng",
                "Phì đại tuyến tiền liệt",
                "Trẻ em <12 tuổi",
                "Trẻ em 12-18 tuổi sau phẫu thuật cắt amidan/VA",
                "Dùng MAO inhibitors trong vòng 14 ngày"
    ],
            "tương_đối": [
                "Suy gan trung bình - thận trọng",
                "Suy thận - thận trọng",
                "Tiền sử nghiện/lạm dụng chất - tăng nguy cơ nghiện",
                "Người cao tuổi - tăng nhạy cảm với anticholinergic"
    ],
        },
        "dosage": {
            "adult_standard": "Paracetamol 500mg/Codeine 15-30mg/Promethazine 6.25-12.5mg x 3-4 lần/ngày",
            "adult_max": "Paracetamol 4g/ngày, Codeine 240mg/ngày, Promethazine 100mg/ngày",
            "notes": """Kết hợp paracetamol (giảm đau, hạ sốt), codeine (opioid yếu, giảm đau) và promethazine (antihistamine H1, chống nôn, an thần). Promethazine có tác dụng chống nôn và an thần mạnh, giúp giảm buồn nôn và giúp ngủ. Codeine là prodrug, chuyển hóa thành morphine qua CYP2D6. Tác dụng hiệp đồng. Controlled substance - nguy cơ nghiện. KHÔNG vượt quá 4g paracetamol/ngày.""",
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "Thận trọng",
            "under_30": "Thận trọng, giảm liều codeine và promethazine",
        },
        "side_effects": [
            "Buồn ngủ nặng (do cả codeine và promethazine)",
            "Chóng mặt",
            "Khô miệng (do promethazine - anticholinergic)",
            "Nhìn mờ",
            "Bí tiểu (đặc biệt ở nam giới có phì đại tuyến tiền liệt)",
            "Táo bón (do codeine)",
            "Ức chế hô hấp (do codeine - hiếm nhưng nghiêm trọng, tăng với promethazine)",
            "Độc gan (do paracetamol - nếu quá liều)",
            "Nguy cơ nghiện/lệ thuộc (do codeine)"
    ],
        "interactions": [
            "Alcohol: tăng tác dụng ức chế CNS, tăng nguy cơ độc gan, tăng nguy cơ ức chế hô hấp",
            "Warfarin: tăng nguy cơ chảy máu",
            "CNS depressants: tăng tác dụng ức chế (cả codeine và promethazine)",
            "Thuốc kháng cholinergic khác: tăng tác dụng phụ anticholinergic",
            "MAO inhibitors: CHỐNG CHỈ ĐỊNH - nguy cơ tác dụng phụ nghiêm trọng",
            "CYP2D6 inhibitors: giảm chuyển hóa codeine thành morphine"
    ],
        "pregnancy": "C - D trong 3 tháng cuối",
        "mechanism_of_action": """Kết hợp paracetamol (giảm đau, hạ sốt), codeine (opioid yếu, giảm đau) và promethazine (antihistamine H1, chống nôn, an thần). Paracetamol ức chế COX-3 ở CNS, giảm đau và hạ sốt. Codeine là prodrug, chuyển hóa thành morphine qua CYP2D6. Morphine tác động lên thụ thể mu-opioid ở CNS, giảm đau. Promethazine là antihistamine H1 thế hệ 1, có tác dụng anticholinergic mạnh, chống nôn (tác động lên trung tâm nôn), và an thần. Tác dụng hiệp đồng: giảm đau, giảm buồn nôn, và giúp ngủ. Controlled substance - nguy cơ nghiện/lệ thuộc. Nguy cơ ức chế hô hấp tăng do cả codeine và promethazine.""",
        "monitoring": [
            "Đáp ứng điều trị: giảm đau, giảm buồn nôn, cải thiện giấc ngủ",
            "Dấu hiệu ức chế hô hấp (QUAN TRỌNG - đặc biệt ở trẻ em và người cao tuổi) - do cả codeine và promethazine",
            "Dấu hiệu tác dụng phụ anticholinergic (khô miệng, nhìn mờ, bí tiểu)",
            "Chức năng gan (nếu dùng >4g paracetamol/ngày)",
            "Dấu hiệu nghiện/lệ thuộc",
            "Dấu hiệu quá liều paracetamol"
    ],
        "precautions": [
            "CONTROLLED SUBSTANCE - nguy cơ nghiện/lệ thuộc",
            "KHÔNG vượt quá 4g paracetamol/ngày - nguy cơ độc gan",
            "CHỐNG CHỈ ĐỊNH ở trẻ <12 tuổi và trẻ 12-18 tuổi sau phẫu thuật cắt amidan/VA",
            "NGUY CƠ ỨC CHẾ HÔ HẤP CAO - do cả codeine và promethazine, đặc biệt ở trẻ em và người cao tuổi",
            "Tác dụng an thần mạnh - không lái xe hoặc vận hành máy móc sau khi uống",
            "Tác dụng phụ anticholinergic - khô miệng, nhìn mờ, bí tiểu (đặc biệt ở nam giới có phì đại tuyến tiền liệt)",
            "CHỐNG CHỈ ĐỊNH ở glaucoma góc đóng, phì đại tuyến tiền liệt, tắc ruột cơ học",
            "CHỐNG CHỈ ĐỊNH với MAO inhibitors",
            "Tránh rượu - tăng nguy cơ ức chế hô hấp nặng, tăng nguy cơ độc gan",
            "Thận trọng ở suy gan, suy thận",
            "Táo bón phổ biến - có thể cần thuốc nhuận tràng"
    ],
        "pharmacokinetics": {
            "half_life": "1-3 giờ (paracetamol), 3 giờ (codeine), 2-3 giờ (morphine), 9-16 giờ (promethazine)",
            "onset": "30 phút",
            "duration": "4-6 giờ",
            "protein_binding": "10-25% (paracetamol), 7-25% (codeine), 93% (promethazine)",
            "clearance": "Gan: chuyển hóa (codeine → morphine qua CYP2D6, promethazine qua CYP2D6). Thận: thải trừ.",
        },
        "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm. Controlled substance - cần bảo quản an toàn.",
        "black_box_warnings": """CONTROLLED SUBSTANCE - nguy cơ nghiện, lạm dụng, và lệ thuộc. NGUY CƠ ỨC CHẾ HÔ HẤP CAO - do cả codeine và promethazine, đặc biệt ở trẻ em. CHỐNG CHỈ ĐỊNH ở trẻ <12 tuổi và trẻ 12-18 tuổi sau phẫu thuật cắt amidan/VA. CHỐNG CHỈ ĐỊNH với MAO inhibitors. Nguy cơ độc gan nghiêm trọng với paracetamol nếu quá liều (>4g/ngày). CHỐNG CHỈ ĐỊNH ở glaucoma góc đóng, phì đại tuyến tiền liệt, tắc ruột cơ học.""",
        "drug_interactions": {
            "major": [
    {
                    "drug": "MAO inhibitors",
                    "mechanism": "Tăng nguy cơ tác dụng phụ nghiêm trọng với cả codeine và promethazine",
                    "effect": "Nguy cơ tác dụng phụ nghiêm trọng, có thể tử vong",
                    "management": "CHỐNG CHỈ ĐỊNH. Không dùng trong vòng 14 ngày sau khi ngừng MAO inhibitors.",
                },
    {
                    "drug": "Alcohol",
                    "mechanism": "Tăng tác dụng ức chế CNS, tăng nguy cơ độc gan, tăng nguy cơ ức chế hô hấp",
                    "effect": "Tăng buồn ngủ, tăng nguy cơ ức chế hô hấp nặng, tăng nguy cơ độc gan nặng",
                    "management": "TRÁNH RƯỢU hoàn toàn khi dùng thuốc này.",
                },
    {
                    "drug": "CNS depressants (Benzodiazepines, Opioids khác)",
                    "mechanism": "Tăng tác dụng ức chế CNS (cả codeine và promethazine)",
                    "effect": "Tăng buồn ngủ, nguy cơ ức chế hô hấp nặng",
                    "management": "Tránh dùng chung hoặc giảm liều đáng kể.",
                }
                ],
            "moderate": [
    {
                    "drug": "Thuốc kháng cholinergic khác (Atropine, Scopolamine, Orphenadrine)",
                    "mechanism": "Tác dụng cộng dồn anticholinergic",
                    "effect": "Tăng tác dụng phụ anticholinergic (khô miệng nặng, bí tiểu, nhìn mờ)",
                    "management": "Tránh dùng chung nếu có thể.",
                }
                ],
            "minor": [],
        },
        "pregnancy_lactation": {
            "fda_category": "C - D trong tam cá nguyệt 3",
            "pregnancy_details": "Tam cá nguyệt 3: Category D - CHỐNG CHỈ ĐỊNH (do codeine).",
            "lactation": {
                "safety": "Contraindicated",
                "details": "Cả codeine và promethazine đều bài tiết vào sữa mẹ, có thể gây ức chế hô hấp và buồn ngủ ở trẻ sơ sinh.",
                "recommendation": "KHÔNG dùng khi cho con bú.",
            },
        },
        "hepatic_adjustment": {
            "mild": "Thận trọng",
            "moderate": "Thận trọng, giảm liều",
            "severe": "CHỐNG CHỈ ĐỊNH",
            "notes": "Paracetamol và codeine chuyển hóa ở gan. Promethazine chuyển hóa ở gan qua CYP2D6. Suy gan nặng là chống chỉ định.",
        },
        "overdose_management": {
            "symptoms": [
                "Paracetamol quá liều: buồn nôn, nôn, đau bụng, vàng da, suy gan",
                "Codeine quá liều: buồn ngủ nặng, ức chế hô hấp, hôn mê, co đồng tử",
                "Promethazine quá liều: buồn ngủ nặng, khô miệng nặng, nhìn mờ, bí tiểu, ảo giác, co giật"
    ],
            "antidote": "N-acetylcysteine (NAC) cho paracetamol quá liều. Naloxone cho codeine quá liều. Physostigmine cho promethazine quá liều nặng.",
            "treatment": [
                "Nếu quá liều paracetamol (>150mg/kg): N-acetylcysteine (NAC) ngay lập tức",
                "Nếu quá liều codeine (ức chế hô hấp): Naloxone 0.4-2mg IV/IM, có thể lặp lại",
                "Nếu promethazine quá liều nặng (ảo giác, co giật, rối loạn ý thức): Physostigmine có thể được xem xét",
                "Đánh giá đường thở, hô hấp, tuần hoàn - CRITICAL (nguy cơ ức chế hô hấp cao)",
                "Hỗ trợ hô hấp nếu cần - QUAN TRỌNG",
                "Rửa dạ dày nếu trong vòng 1-2 giờ",
                "Than hoạt tính",
                "Theo dõi chức năng gan (paracetamol quá liều)"
    ],
            "monitoring": "Theo dõi ý thức, hô hấp (CRITICAL - nguy cơ cao), tim mạch. Nếu paracetamol quá liều: theo dõi chức năng gan (ALT, AST, bilirubin, INR).",
        },
        "reversal_agents": {
            "available": True,
            "agents": [
    {
                    "agent": "N-acetylcysteine (NAC)",
                    "mechanism": "Chống độc cho paracetamol quá liều",
                    "indication": "Quá liều paracetamol (>150mg/kg hoặc >10g)",
                    "dose": "Theo phác đồ điều trị quá liều paracetamol",
                    "caution": "Chỉ hiệu quả nếu dùng trong vòng 8-10 giờ sau khi uống paracetamol",
                },
    {
                    "agent": "Naloxone",
                    "mechanism": "Đối kháng thụ thể mu-opioid, đảo ngược tác dụng codeine/morphine",
                    "indication": "Codeine quá liều (ức chế hô hấp)",
                    "dose": "0.4-2mg IV/IM, có thể lặp lại mỗi 2-3 phút",
                    "caution": "Tác dụng ngắn (30-90 phút), có thể cần lặp lại",
                },
    {
                    "agent": "Physostigmine",
                    "mechanism": "Chất ức chế cholinesterase, đảo ngược tác dụng anticholinergic",
                    "indication": "Promethazine quá liều nặng (ảo giác, co giật, rối loạn ý thức)",
                    "dose": "0.5-2mg IV, có thể lặp lại",
                    "caution": "Chỉ dùng khi quá liều nặng, cần theo dõi chặt chẽ",
                }
                ],
        },
        "administration_instructions": {
            "oral": {
                "with_food": "Có thể uống với thức ăn hoặc không",
                "timing": """Paracetamol 500mg/Codeine 15-30mg/Promethazine 6.25-12.5mg x 3-4 lần/ngày. KHÔNG vượt quá 4g paracetamol/ngày và 240mg codeine/ngày. KHÔNG lái xe sau khi uống. Controlled substance - cần kê đơn.""",
            },
        },
        "references": {
            "primary_sources": [
                "FDA Drug Label - Phenergan with Codeine (Paracetamol/Codeine/Promethazine)",
                "UpToDate - Combination analgesics: Drug information"
    ],
            "last_updated": "2025-02-18",
            "evidence_level": "High - FDA-approved, controlled substance",
        },
            "risk_flags": {
                "high_alert": True,
                "narrow_therapeutic_index": False,
                "bleeding_risk": False,
                "organ_toxicity": ["hepatic", "CNS"],
                "qt_prolongation": False,
                "hepatotoxicity": True,
                "nephrotoxicity": False,
                "requires_monitoring": ["LFT", "Respiratory status", "CNS status"],
            },
            "guideline_tags": [
                "FDA Drug Information",
                "UpToDate Drug Information",
                "Controlled Substance - Risk of Addiction",
            ]
    },
    "Paracetamol/Ibuprofen/Caffeine":     {
        "group": "Analgesic - Combination (Paracetamol + NSAID + Stimulant)",
        "vietnamese_name": "Paracetamol/Ibuprofen/Caffeine, Advil Dual Action with Caffeine",
        "administration": [
            "PO"
    ],
        "indications": [
            "Đau nhẹ đến trung bình",
            "Đau đầu",
            "Đau răng",
            "Đau cơ xương",
            "Sốt",
            "Đau không đáp ứng với paracetamol hoặc ibuprofen đơn thuần"
    ],
        "contraindications": {
            "tuyệt_đối": [
                "Dị ứng paracetamol, ibuprofen hoặc caffeine",
                "Loét dạ dày tá tràng đang hoạt động",
                "Suy gan nặng",
                "Tam cá nguyệt 3 thai kỳ (3 tháng cuối)",
                "Suy thận nặng",
                "Rối loạn lo âu nặng",
                "Rối loạn giấc ngủ nặng"
    ],
            "tương_đối": [
                "Suy gan trung bình - thận trọng",
                "Suy thận trung bình - thận trọng",
                "Bệnh tim mạch - thận trọng (do caffeine)",
                "Loét dạ dày - thận trọng (do cả ibuprofen và caffeine)",
                "Hen phế quản do aspirin/NSAID - thận trọng"
    ],
        },
        "dosage": {
            "adult_standard": "Paracetamol 500mg/Ibuprofen 200mg/Caffeine 30-50mg x 3-4 lần/ngày",
            "adult_max": "Paracetamol 4g/ngày, Ibuprofen 2400mg/ngày, Caffeine 400mg/ngày",
            "notes": """Kết hợp paracetamol (giảm đau, hạ sốt), ibuprofen (NSAID, giảm đau, chống viêm, hạ sốt) và caffeine (kích thích, tăng cường tác dụng giảm đau). Caffeine có thể tăng cường tác dụng giảm đau của cả paracetamol và ibuprofen, đồng thời giúp giảm mệt mỏi. Tác dụng hiệp đồng: hiệu quả giảm đau và chống viêm tốt hơn từng thuốc đơn lẻ. KHÔNG vượt quá 4g paracetamol/ngày và 2400mg ibuprofen/ngày. Tránh dùng gần giờ ngủ do caffeine.""",
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "Thận trọng, giảm liều",
            "under_30": "Tránh dùng",
        },
        "side_effects": [
            "Chảy máu dạ dày (do ibuprofen)",
            "Mất ngủ (do caffeine)",
            "Bồn chồn, lo âu (do caffeine)",
            "Tăng nhịp tim (do caffeine)",
            "Suy thận (do ibuprofen)",
            "Tăng huyết áp (do ibuprofen và caffeine)",
            "Độc gan (do paracetamol - nếu quá liều)",
            "Buồn nôn, nôn",
            "Đau đầu",
            "Chóng mặt"
    ],
        "interactions": [
            "Warfarin: tăng nguy cơ chảy máu nặng (cả paracetamol và ibuprofen)",
            "Alcohol: tăng nguy cơ độc gan (paracetamol), tăng nguy cơ chảy máu dạ dày (ibuprofen)",
            "ACE inhibitor: giảm hiệu quả, tăng nguy cơ suy thận (ibuprofen)",
            "CNS stimulants: tăng tác dụng kích thích (caffeine)",
            "MAO inhibitors: tăng nguy cơ tác dụng phụ với caffeine"
    ],
        "pregnancy": "C - D trong 3 tháng cuối",
        "mechanism_of_action": """Kết hợp paracetamol (giảm đau, hạ sốt), ibuprofen (NSAID, giảm đau, chống viêm, hạ sốt) và caffeine (kích thích, tăng cường tác dụng giảm đau). Paracetamol ức chế COX-3 ở CNS, giảm đau và hạ sốt. Ibuprofen ức chế COX-1 và COX-2, giảm đau, chống viêm, và hạ sốt. Caffeine là chất kích thích CNS, có thể tăng cường tác dụng giảm đau của cả paracetamol và ibuprofen thông qua nhiều cơ chế (tăng hấp thu, tăng tác dụng tại thụ thể adenosine, giảm mệt mỏi). Tác dụng hiệp đồng: hiệu quả giảm đau và chống viêm tốt hơn từng thuốc đơn lẻ, đồng thời giảm mệt mỏi.""",
        "monitoring": [
            "Đáp ứng điều trị: giảm đau, hạ sốt",
            "Dấu hiệu chảy máu dạ dày - do ibuprofen",
            "Dấu hiệu kích thích quá mức (bồn chồn, lo âu, mất ngủ) - do caffeine",
            "Nhịp tim (tăng nhịp tim do caffeine)",
            "Chức năng gan (nếu dùng >4g paracetamol/ngày)",
            "Creatinine, BUN - do ibuprofen",
            "Dấu hiệu quá liều paracetamol"
    ],
        "precautions": [
            "KHÔNG vượt quá 4g paracetamol/ngày và 2400mg ibuprofen/ngày",
            "Nguy cơ chảy máu dạ dày - do ibuprofen, uống với thức ăn",
            "Nguy cơ mất ngủ, bồn chồn - do caffeine, tránh dùng gần giờ ngủ",
            "Thận trọng ở bệnh nhân có bệnh tim mạch, loét dạ dày - do caffeine và ibuprofen",
            "Tránh rượu - tăng nguy cơ độc gan và chảy máu dạ dày",
            "Không dùng trong 3 tháng cuối thai kỳ",
            "Thận trọng ở suy gan, suy thận",
            "Theo dõi chức năng gan và thận nếu dùng kéo dài"
    ],
        "pharmacokinetics": {
            "half_life": "1-3 giờ (paracetamol), 2 giờ (ibuprofen), 3-5 giờ (caffeine)",
            "onset": "30 phút",
            "duration": "4-6 giờ",
            "protein_binding": "10-25% (paracetamol), 99% (ibuprofen), 36% (caffeine)",
            "clearance": "Gan: chuyển hóa (ibuprofen qua CYP2C9, caffeine qua CYP1A2). Thận: thải trừ.",
        },
        "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm",
        "black_box_warnings": """Nguy cơ độc gan nghiêm trọng với paracetamol nếu quá liều (>4g/ngày). Nguy cơ chảy máu dạ dày với ibuprofen. Không dùng trong 3 tháng cuối thai kỳ. NSAID có thể gây tăng nguy cơ nhồi máu cơ tim và đột quỵ. Caffeine có thể gây mất ngủ, bồn chồn, tăng nhịp tim.""",
        "drug_interactions": {
            "major": [
    {
                    "drug": "Warfarin, các thuốc chống đông khác",
                    "mechanism": "Cả paracetamol và ibuprofen đều tăng nguy cơ chảy máu",
                    "effect": "Tăng nguy cơ chảy máu nặng, tăng INR",
                    "management": "Tránh dùng đồng thời hoặc theo dõi INR chặt chẽ.",
                },
    {
                    "drug": "Alcohol",
                    "mechanism": "Tăng nguy cơ độc gan (paracetamol), tăng nguy cơ chảy máu dạ dày (ibuprofen)",
                    "effect": "Tăng nguy cơ độc gan nặng, tăng nguy cơ chảy máu dạ dày",
                    "management": "TRÁNH RƯỢU hoàn toàn khi dùng thuốc này.",
                }
                ],
            "moderate": [
    {
                    "drug": "ACE inhibitor, ARB",
                    "mechanism": "Ibuprofen giảm tổng hợp prostaglandin → giảm lưu lượng máu thận",
                    "effect": "Giảm hiệu quả, tăng nguy cơ suy thận",
                    "management": "Thận trọng. Theo dõi creatinine, BUN.",
                },
    {
                    "drug": "CNS stimulants (Amphetamines, Methylphenidate)",
                    "mechanism": "Tăng tác dụng kích thích CNS",
                    "effect": "Tăng bồn chồn, lo âu, mất ngủ, tăng nhịp tim",
                    "management": "Tránh dùng chung hoặc giảm liều caffeine.",
                }
                ],
            "minor": [],
        },
        "pregnancy_lactation": {
            "fda_category": "C - D trong tam cá nguyệt 3",
            "pregnancy_details": "Tam cá nguyệt 3: CHỐNG CHỈ ĐỊNH (do ibuprofen). Caffeine: Category C - thận trọng, giới hạn <200mg/ngày.",
            "lactation": {
                "safety": "Caution",
                "details": "Cả ba thuốc đều bài tiết vào sữa mẹ. Có thể gây tác dụng phụ ở trẻ.",
                "recommendation": "Thận trọng khi cho con bú. Giới hạn caffeine <200mg/ngày.",
            },
        },
        "hepatic_adjustment": {
            "mild": "Thận trọng",
            "moderate": "Thận trọng, giảm liều",
            "severe": "CHỐNG CHỈ ĐỊNH",
            "notes": "Paracetamol và ibuprofen chuyển hóa ở gan. Caffeine chuyển hóa ở gan qua CYP1A2. Suy gan nặng là chống chỉ định.",
        },
        "overdose_management": {
            "symptoms": [
                "Paracetamol quá liều: buồn nôn, nôn, đau bụng, vàng da, suy gan",
                "Ibuprofen quá liều: buồn nôn, nôn, đau bụng, chảy máu dạ dày, suy thận cấp",
                "Caffeine quá liều: bồn chồn, lo âu, mất ngủ, tăng nhịp tim, run, co giật"
    ],
            "antidote": "N-acetylcysteine (NAC) cho paracetamol quá liều. Không có antidote đặc hiệu cho ibuprofen và caffeine.",
            "treatment": [
                "Nếu quá liều paracetamol (>150mg/kg): N-acetylcysteine (NAC) ngay lập tức",
                "Nếu caffeine quá liều: điều trị hỗ trợ, benzodiazepine cho co giật nếu có",
                "Đánh giá đường thở, hô hấp, tuần hoàn",
                "Rửa dạ dày nếu trong vòng 1-2 giờ",
                "Than hoạt tính",
                "Điều trị hỗ trợ",
                "Theo dõi chức năng gan và thận"
    ],
            "monitoring": "Theo dõi ý thức, hô hấp, tim mạch, nhịp tim. Nếu paracetamol quá liều: theo dõi chức năng gan (ALT, AST, bilirubin, INR). Nếu ibuprofen quá liều: theo dõi chức năng thận, dấu hiệu chảy máu.",
        },
        "reversal_agents": {
            "available": True,
            "agents": [
    {
                    "agent": "N-acetylcysteine (NAC)",
                    "mechanism": "Chống độc cho paracetamol quá liều",
                    "indication": "Quá liều paracetamol (>150mg/kg hoặc >10g)",
                    "dose": "Theo phác đồ điều trị quá liều paracetamol",
                    "caution": "Chỉ hiệu quả nếu dùng trong vòng 8-10 giờ sau khi uống paracetamol",
                }
                ],
        },
        "administration_instructions": {
            "oral": {
                "with_food": "Uống với thức ăn để giảm kích ứng dạ dày (ibuprofen)",
                "timing": """Paracetamol 500mg/Ibuprofen 200mg/Caffeine 30-50mg x 3-4 lần/ngày. KHÔNG vượt quá 4g paracetamol/ngày và 2400mg ibuprofen/ngày. TRÁNH dùng gần giờ ngủ do caffeine.""",
            },
        },
        "references": {
            "primary_sources": [
                "FDA Drug Label - Advil Dual Action with Caffeine (Paracetamol/Ibuprofen/Caffeine)",
                "UpToDate - Combination analgesics: Drug information"
    ],
            "last_updated": "2025-02-18",
            "evidence_level": "High - FDA-approved",
        },
            "risk_flags": {
                "high_alert": False,
                "narrow_therapeutic_index": False,
                "bleeding_risk": True,
                "organ_toxicity": ["GI", "renal", "hepatic", "cardiac"],
                "qt_prolongation": False,
                "hepatotoxicity": True,
                "nephrotoxicity": True,
                "requires_monitoring": ["LFT", "RFT", "GI symptoms", "Heart rate"],
            },
            "guideline_tags": [
                "FDA Drug Information",
                "UpToDate Drug Information",
            ]
    },
    "Aspirin/Codeine/Caffeine":     {
        "group": "Analgesic - Combination (NSAID + Opioid + Stimulant)",
        "vietnamese_name": "Aspirin/Codeine/Caffeine, Co-codaprin Forte",
        "administration": [
            "PO"
    ],
        "indications": [
            "Đau nhẹ đến trung bình",
            "Đau đầu",
            "Đau răng",
            "Đau cơ xương",
            "Đau không đáp ứng với aspirin đơn thuần"
    ],
        "contraindications": {
            "tuyệt_đối": [
                "Dị ứng aspirin, codeine hoặc caffeine",
                "Loét dạ dày tá tràng đang hoạt động",
                "Suy hô hấp nặng",
                "Tắc ruột cơ học",
                "Rối loạn lo âu nặng",
                "Rối loạn giấc ngủ nặng",
                "Trẻ em <12 tuổi (hội chứng Reye với aspirin)",
                "Trẻ em 12-18 tuổi sau phẫu thuật cắt amidan/VA",
                "Dùng warfarin hoặc thuốc chống đông khác"
    ],
            "tương_đối": [
                "Suy thận trung bình - thận trọng",
                "Suy gan trung bình - thận trọng",
                "Tiền sử nghiện/lạm dụng chất - tăng nguy cơ nghiện",
                "Bệnh tim mạch - thận trọng (do caffeine)"
    ],
        },
        "dosage": {
            "adult_standard": "Aspirin 325mg/Codeine 15-30mg/Caffeine 30-50mg x 3-4 lần/ngày",
            "adult_max": "Aspirin 4g/ngày, Codeine 240mg/ngày, Caffeine 400mg/ngày",
            "notes": """Kết hợp aspirin (NSAID, giảm đau, chống viêm, chống kết tập tiểu cầu), codeine (opioid yếu, giảm đau) và caffeine (kích thích, tăng cường tác dụng giảm đau). Aspirin có tác dụng chống kết tập tiểu cầu kéo dài. Caffeine có thể tăng cường tác dụng giảm đau và giảm buồn ngủ do codeine. Codeine là prodrug, chuyển hóa thành morphine qua CYP2D6. Tác dụng hiệp đồng. Controlled substance - nguy cơ nghiện. CHỐNG CHỈ ĐỊNH với warfarin. Tránh dùng gần giờ ngủ do caffeine.""",
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "Thận trọng, giảm liều",
            "under_30": "Thận trọng, giảm liều codeine",
        },
        "side_effects": [
            "Chảy máu dạ dày (do aspirin)",
            "Buồn ngủ (do codeine) - ít hơn do caffeine đối kháng",
            "Mất ngủ (do caffeine)",
            "Bồn chồn, lo âu (do caffeine)",
            "Tăng nhịp tim (do caffeine)",
            "Táo bón (do codeine)",
            "Tinnitus (ù tai) ở liều cao aspirin",
            "Ức chế hô hấp (do codeine - hiếm nhưng nghiêm trọng)",
            "Nguy cơ nghiện/lệ thuộc (do codeine)"
    ],
        "interactions": [
            "Warfarin: CHỐNG CHỈ ĐỊNH - tăng nguy cơ chảy máu nặng",
            "Alcohol: tăng tác dụng ức chế CNS, tăng nguy cơ chảy máu dạ dày",
            "CNS depressants: tăng tác dụng ức chế (codeine)",
            "CNS stimulants: tăng tác dụng kích thích (caffeine)",
            "ACE inhibitor: giảm hiệu quả, tăng nguy cơ suy thận (aspirin)",
            "CYP2D6 inhibitors: giảm chuyển hóa codeine thành morphine",
            "MAO inhibitors: tăng nguy cơ tác dụng phụ với caffeine"
    ],
        "pregnancy": "C - D trong 3 tháng cuối",
        "mechanism_of_action": """Kết hợp aspirin (NSAID, giảm đau, chống viêm, chống kết tập tiểu cầu), codeine (opioid yếu, giảm đau) và caffeine (kích thích, tăng cường tác dụng giảm đau). Aspirin ức chế không hồi phục COX-1 và COX-2, giảm đau, chống viêm, và chống kết tập tiểu cầu (tác dụng kéo dài 7-10 ngày). Codeine là prodrug, chuyển hóa thành morphine qua CYP2D6. Morphine tác động lên thụ thể mu-opioid ở CNS, giảm đau. Caffeine là chất kích thích CNS, có thể tăng cường tác dụng giảm đau của aspirin và codeine, đồng thời đối kháng tác dụng buồn ngủ của codeine. Tác dụng hiệp đồng: hiệu quả giảm đau tốt hơn và giảm buồn ngủ so với Aspirin/Codeine đơn thuần. Controlled substance - nguy cơ nghiện/lệ thuộc.""",
        "monitoring": [
            "Đáp ứng điều trị: giảm đau",
            "Dấu hiệu chảy máu dạ dày (phân đen, nôn ra máu, đau bụng) - do aspirin",
            "Dấu hiệu ức chế hô hấp (đặc biệt ở trẻ em và người cao tuổi) - do codeine",
            "Dấu hiệu kích thích quá mức (bồn chồn, lo âu, mất ngủ) - do caffeine",
            "Nhịp tim (tăng nhịp tim do caffeine)",
            "Dấu hiệu nghiện/lệ thuộc",
            "Tinnitus (ù tai) ở liều cao aspirin"
    ],
        "precautions": [
            "CONTROLLED SUBSTANCE - nguy cơ nghiện/lệ thuộc",
            "CHỐNG CHỈ ĐỊNH với warfarin hoặc thuốc chống đông khác - tăng nguy cơ chảy máu nặng",
            "CHỐNG CHỈ ĐỊNH ở trẻ <12 tuổi (hội chứng Reye với aspirin)",
            "CHỐNG CHỈ ĐỊNH ở trẻ 12-18 tuổi sau phẫu thuật cắt amidan/VA",
            "Nguy cơ chảy máu dạ dày cao - do aspirin, uống với thức ăn",
            "Nguy cơ ức chế hô hấp - đặc biệt ở trẻ em và người cao tuổi",
            "Nguy cơ mất ngủ, bồn chồn - do caffeine, tránh dùng gần giờ ngủ",
            "Thận trọng ở bệnh nhân có bệnh tim mạch - do caffeine",
            "Tránh rượu - tăng tác dụng ức chế CNS, tăng nguy cơ chảy máu dạ dày",
            "Thận trọng ở suy gan, suy thận",
            "Táo bón phổ biến - có thể cần thuốc nhuận tràng"
    ],
        "pharmacokinetics": {
            "half_life": "2-3 giờ (aspirin), 3 giờ (codeine), 2-3 giờ (morphine), 3-5 giờ (caffeine)",
            "onset": "30 phút",
            "duration": "4-6 giờ",
            "protein_binding": "50-80% (aspirin), 7-25% (codeine), 36% (caffeine)",
            "clearance": "Gan: chuyển hóa (aspirin → salicylic acid, codeine → morphine qua CYP2D6, caffeine qua CYP1A2). Thận: thải trừ.",
        },
        "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm. Controlled substance - cần bảo quản an toàn.",
        "black_box_warnings": """CONTROLLED SUBSTANCE - nguy cơ nghiện, lạm dụng, và lệ thuộc. CHỐNG CHỈ ĐỊNH với warfarin hoặc thuốc chống đông khác - tăng nguy cơ chảy máu nặng. CHỐNG CHỈ ĐỊNH ở trẻ <12 tuổi (hội chứng Reye với aspirin). Nguy cơ ức chế hô hấp, đặc biệt ở trẻ em. Nguy cơ chảy máu dạ dày nặng với aspirin. Caffeine có thể gây mất ngủ, bồn chồn, tăng nhịp tim. Không dùng trong 3 tháng cuối thai kỳ.""",
        "drug_interactions": {
            "major": [
    {
                    "drug": "Warfarin, các thuốc chống đông khác",
                    "mechanism": "Aspirin ức chế COX-1 tiểu cầu, tăng nguy cơ chảy máu",
                    "effect": "Tăng nguy cơ chảy máu nặng, tăng INR",
                    "management": "CHỐNG CHỈ ĐỊNH. Tránh dùng cùng.",
                },
    {
                    "drug": "Alcohol",
                    "mechanism": "Tăng tác dụng ức chế CNS, tăng nguy cơ chảy máu dạ dày",
                    "effect": "Tăng buồn ngủ, tăng nguy cơ ức chế hô hấp, tăng nguy cơ chảy máu dạ dày nặng",
                    "management": "TRÁNH RƯỢU hoàn toàn khi dùng thuốc này.",
                }
                ],
            "moderate": [
    {
                    "drug": "CNS depressants (Benzodiazepines, Opioids khác)",
                    "mechanism": "Tăng tác dụng ức chế CNS",
                    "effect": "Tăng buồn ngủ, nguy cơ ức chế hô hấp nặng",
                    "management": "Tránh dùng chung hoặc giảm liều.",
                },
    {
                    "drug": "CNS stimulants (Amphetamines, Methylphenidate)",
                    "mechanism": "Tăng tác dụng kích thích CNS",
                    "effect": "Tăng bồn chồn, lo âu, mất ngủ, tăng nhịp tim",
                    "management": "Tránh dùng chung hoặc giảm liều caffeine.",
                }
                ],
            "minor": [],
        },
        "pregnancy_lactation": {
            "fda_category": "C - D trong tam cá nguyệt 3",
            "pregnancy_details": "Tam cá nguyệt 3: Category D - CHỐNG CHỈ ĐỊNH (do cả aspirin và codeine). Caffeine: Category C - thận trọng, giới hạn <200mg/ngày.",
            "lactation": {
                "safety": "Contraindicated",
                "details": "Cả ba thuốc đều bài tiết vào sữa mẹ. Có thể gây tác dụng phụ nghiêm trọng ở trẻ sơ sinh.",
                "recommendation": "KHÔNG dùng khi cho con bú.",
            },
        },
        "hepatic_adjustment": {
            "mild": "Thận trọng",
            "moderate": "Thận trọng, giảm liều",
            "severe": "CHỐNG CHỈ ĐỊNH",
            "notes": "Cả ba thuốc đều chuyển hóa ở gan. Suy gan nặng là chống chỉ định.",
        },
        "overdose_management": {
            "symptoms": [
                "Aspirin quá liều: ù tai, chóng mặt, buồn nôn, nôn, tăng thông khí, kiềm hô hấp, toan chuyển hóa",
                "Codeine quá liều: buồn ngủ nặng, ức chế hô hấp, hôn mê, co đồng tử",
                "Caffeine quá liều: bồn chồn, lo âu, mất ngủ, tăng nhịp tim, run, co giật"
    ],
            "antidote": "Naloxone cho codeine quá liều. Không có antidote đặc hiệu cho aspirin và caffeine.",
            "treatment": [
                "Nếu quá liều codeine (ức chế hô hấp): Naloxone 0.4-2mg IV/IM, có thể lặp lại",
                "Nếu aspirin quá liều: kiềm hóa nước tiểu (sodium bicarbonate), điều chỉnh điện giải",
                "Nếu caffeine quá liều: điều trị hỗ trợ, benzodiazepine cho co giật nếu có",
                "Đánh giá đường thở, hô hấp, tuần hoàn - QUAN TRỌNG",
                "Hỗ trợ hô hấp nếu cần",
                "Rửa dạ dày nếu trong vòng 1-2 giờ",
                "Than hoạt tính",
                "Theo dõi nồng độ salicylat máu (nếu aspirin quá liều)"
    ],
            "monitoring": "Theo dõi ý thức, hô hấp (QUAN TRỌNG), tim mạch, nhịp tim. Nếu aspirin quá liều: theo dõi nồng độ salicylat máu, khí máu, điện giải.",
        },
        "reversal_agents": {
            "available": True,
            "agents": [
    {
                    "agent": "Naloxone",
                    "mechanism": "Đối kháng thụ thể mu-opioid, đảo ngược tác dụng codeine/morphine",
                    "indication": "Codeine quá liều (ức chế hô hấp)",
                    "dose": "0.4-2mg IV/IM, có thể lặp lại mỗi 2-3 phút",
                    "caution": "Tác dụng ngắn (30-90 phút), có thể cần lặp lại",
                }
                ],
        },
        "administration_instructions": {
            "oral": {
                "with_food": "Uống với thức ăn hoặc sữa để giảm kích ứng dạ dày (aspirin)",
                "timing": """Aspirin 325mg/Codeine 15-30mg/Caffeine 30-50mg x 3-4 lần/ngày. KHÔNG vượt quá 4g aspirin/ngày và 240mg codeine/ngày. TRÁNH dùng gần giờ ngủ do caffeine. Controlled substance - cần kê đơn.""",
            },
        },
        "references": {
            "primary_sources": [
                "FDA Drug Label - Co-codaprin Forte (Aspirin/Codeine/Caffeine)",
                "UpToDate - Combination analgesics: Drug information"
    ],
            "last_updated": "2025-02-18",
            "evidence_level": "High - FDA-approved, controlled substance",
        },
            "risk_flags": {
                "high_alert": True,
                "narrow_therapeutic_index": False,
                "bleeding_risk": True,
                "organ_toxicity": ["GI", "CNS", "cardiac"],
                "qt_prolongation": False,
                "hepatotoxicity": False,
                "nephrotoxicity": False,
                "requires_monitoring": ["GI symptoms", "Respiratory status", "CNS status", "Heart rate"],
            },
            "guideline_tags": [
                "FDA Drug Information",
                "UpToDate Drug Information",
                "Controlled Substance - Risk of Addiction",
            ]
    },
}

__all__ = ['PAIN_MUSCLE_RELAXANT_COMBINATIONS_DRUGS']

