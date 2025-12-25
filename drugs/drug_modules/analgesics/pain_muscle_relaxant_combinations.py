"""
Pain Reliever + Muscle Relaxant Combination Drugs
Fixed-dose combinations for musculoskeletal pain with muscle spasm
"""

PAIN_MUSCLE_RELAXANT_COMBINATIONS_DRUGS = {
    "Paracetamol/Carisoprodol": {
        "group": "Analgesic - Combination (Paracetamol + Muscle Relaxant)",
        "vietnamese_name": "Paracetamol/Carisoprodol, Soma Compound",
        "administration": ["PO"],
        "indications": [
            "Đau cơ xương khớp kèm co thắt cơ (musculoskeletal pain with muscle spasm)",
            "Đau lưng cấp tính",
            "Đau cơ sau chấn thương"
        ],
        "contraindications": [
            "Dị ứng paracetamol hoặc carisoprodol",
            "Suy gan nặng",
            "Porphyria",
            "Dị ứng với meprobamate"
        ],
        "dosage": {
            "adult_standard": "Paracetamol 325mg/Carisoprodol 250mg x 3-4 lần/ngày",
            "adult_max": "Paracetamol 4g/ngày, Carisoprodol 1400mg/ngày",
            "notes": "CHỈ dùng ngắn hạn (2-3 tuần). Carisoprodol chuyển hóa thành meprobamate (controlled substance, nguy cơ nghiện)."
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "Thận trọng",
            "under_30": "Thận trọng"
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
        "mechanism_of_action": "Kết hợp paracetamol (giảm đau, hạ sốt) và carisoprodol (giãn cơ xương khớp). Paracetamol ức chế COX-3 ở CNS, giảm đau và hạ sốt. Carisoprodol là thuốc giãn cơ xương khớp, chuyển hóa thành meprobamate (controlled substance, có nguy cơ nghiện). Tác dụng hiệp đồng: giảm đau cơ xương khớp kèm co thắt cơ. CHỈ dùng ngắn hạn (2-3 tuần).",
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
            "clearance": "Gan: chuyển hóa paracetamol và carisoprodol. Thận: thải trừ."
        },
        "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm. Controlled substance - cần bảo quản an toàn.",
        "black_box_warnings": "NGUY CƠ NGHIỆN, LẠM DỤNG, VÀ LỆ THUỘC - carisoprodol chuyển hóa thành meprobamate (controlled substance). Nguy cơ độc gan nghiêm trọng với paracetamol nếu quá liều (>4g/ngày). Chỉ dùng ngắn hạn (2-3 tuần).",
        "drug_interactions": {
            "major": [
                {
                    "drug": "Alcohol",
                    "mechanism": "Tăng tác dụng ức chế CNS, tăng nguy cơ độc gan (paracetamol)",
                    "effect": "Tăng buồn ngủ, tăng nguy cơ độc gan nặng",
                    "management": "TRÁNH RƯỢU hoàn toàn khi dùng thuốc này."
                },
                {
                    "drug": "Warfarin",
                    "mechanism": "Paracetamol có thể tăng tác dụng warfarin",
                    "effect": "Tăng INR, tăng nguy cơ chảy máu",
                    "management": "Thận trọng. Theo dõi INR thường xuyên."
                }
            ],
            "moderate": [
                {
                    "drug": "CNS depressants (Benzodiazepines, Opioids)",
                    "mechanism": "Tăng tác dụng ức chế CNS",
                    "effect": "Tăng buồn ngủ, nguy cơ ức chế hô hấp",
                    "management": "Thận trọng. Giảm liều nếu cần."
                },
                {
                    "drug": "CYP2C19 inhibitors (Omeprazole, Fluoxetine)",
                    "mechanism": "Ức chế chuyển hóa carisoprodol",
                    "effect": "Tăng nồng độ carisoprodol",
                    "management": "Thận trọng. Có thể cần giảm liều."
                }
            ]
        },
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
            ]
        },
        "pregnancy_lactation": {
            "fda_category": "C",
            "pregnancy_details": "Category C. Có thể dùng nếu lợi ích > nguy cơ.",
            "lactation": {
                "safety": "Caution",
                "details": "Paracetamol và carisoprodol đều bài tiết vào sữa mẹ. Có thể gây tác dụng phụ ở trẻ.",
                "recommendation": "Thận trọng khi cho con bú."
            }
        },
        "hepatic_adjustment": {
            "mild": "Thận trọng",
            "moderate": "Thận trọng, giảm liều",
            "severe": "CHỐNG CHỈ ĐỊNH",
            "notes": "Paracetamol chuyển hóa ở gan, nguy cơ độc gan. Suy gan nặng là chống chỉ định."
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
            "monitoring": "Theo dõi ý thức, hô hấp, tim mạch. Nếu paracetamol quá liều: theo dõi chức năng gan (ALT, AST, bilirubin), INR."
        },
        "reversal_agents": {
            "available": True,
            "agents": [
                {
                    "agent": "N-acetylcysteine (NAC)",
                    "mechanism": "Chống độc cho paracetamol quá liều",
                    "indication": "Quá liều paracetamol (>150mg/kg hoặc >10g)",
                    "dose": "Theo phác đồ điều trị quá liều paracetamol",
                    "caution": "Chỉ hiệu quả nếu dùng trong vòng 8-10 giờ sau khi uống paracetamol"
                }
            ]
        },
        "administration_instructions": {
            "oral": {
                "with_food": "Có thể uống với thức ăn hoặc không. Uống với thức ăn có thể giảm kích ứng dạ dày.",
                "timing": "Paracetamol 325mg/Carisoprodol 250mg x 3-4 lần/ngày. CHỈ dùng ngắn hạn (2-3 tuần). KHÔNG vượt quá 4g paracetamol/ngày."
            }
        },
        "references": {
            "primary_sources": [
                "FDA Drug Label - Soma Compound (Paracetamol/Carisoprodol)",
                "UpToDate - Muscle relaxants: Drug information"
            ],
            "last_updated": "2025-02-18",
            "evidence_level": "High - FDA-approved, controlled substance"
        }
    },

    "Paracetamol/Orphenadrine": {
        "group": "Analgesic - Combination (Paracetamol + Muscle Relaxant)",
        "vietnamese_name": "Paracetamol/Orphenadrine, Norgesic, Norflex Compound",
        "administration": ["PO"],
        "indications": [
            "Đau cơ xương khớp kèm co thắt cơ (musculoskeletal pain with muscle spasm)",
            "Đau lưng cấp tính",
            "Đau cơ sau chấn thương"
        ],
        "contraindications": [
            "Dị ứng paracetamol hoặc orphenadrine",
            "Suy gan nặng",
            "Glaucoma góc đóng",
            "Phì đại tuyến tiền liệt",
            "Tắc ruột cơ học",
            "Bệnh tim mạch nặng"
        ],
        "dosage": {
            "adult_standard": "Paracetamol 450mg/Orphenadrine 35mg x 3 lần/ngày",
            "adult_max": "Paracetamol 4g/ngày",
            "notes": "CHỈ dùng ngắn hạn. Orphenadrine có tác dụng kháng cholinergic (khô miệng, nhìn mờ, bí tiểu)."
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "Thận trọng",
            "under_30": "Thận trọng"
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
        "mechanism_of_action": "Kết hợp paracetamol (giảm đau, hạ sốt) và orphenadrine (giãn cơ xương khớp, anticholinergic). Paracetamol ức chế COX-3 ở CNS, giảm đau và hạ sốt. Orphenadrine là thuốc giãn cơ xương khớp có tác dụng anticholinergic (kháng muscarinic), gây giãn cơ trơn và giảm co thắt cơ. Tác dụng hiệp đồng: giảm đau cơ xương khớp kèm co thắt cơ. CHỈ dùng ngắn hạn. Tác dụng phụ anticholinergic: khô miệng, nhìn mờ, bí tiểu.",
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
            "clearance": "Gan: chuyển hóa. Thận: thải trừ."
        },
        "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm",
        "black_box_warnings": "Nguy cơ độc gan nghiêm trọng với paracetamol nếu quá liều (>4g/ngày). CHỐNG CHỈ ĐỊNH ở glaucoma góc đóng, phì đại tuyến tiền liệt, tắc ruột cơ học. Chỉ dùng ngắn hạn.",
        "drug_interactions": {
            "major": [
                {
                    "drug": "Alcohol",
                    "mechanism": "Tăng tác dụng ức chế CNS, tăng nguy cơ độc gan",
                    "effect": "Tăng buồn ngủ, tăng nguy cơ độc gan nặng",
                    "management": "TRÁNH RƯỢU hoàn toàn khi dùng thuốc này."
                },
                {
                    "drug": "Thuốc kháng cholinergic khác (Atropine, Scopolamine, Antihistamines)",
                    "mechanism": "Tác dụng cộng dồn anticholinergic",
                    "effect": "Tăng tác dụng phụ anticholinergic (khô miệng nặng, bí tiểu, nhìn mờ)",
                    "management": "Tránh dùng chung nếu có thể."
                }
            ],
            "moderate": [
                {
                    "drug": "MAO inhibitors",
                    "mechanism": "Tăng nguy cơ tác dụng phụ",
                    "effect": "Tăng nguy cơ tác dụng phụ nghiêm trọng",
                    "management": "Tránh dùng chung."
                }
            ]
        },
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
            ]
        },
        "pregnancy_lactation": {
            "fda_category": "C",
            "pregnancy_details": "Category C. Có thể dùng nếu lợi ích > nguy cơ.",
            "lactation": {
                "safety": "Caution",
                "details": "Paracetamol và orphenadrine đều bài tiết vào sữa mẹ. Có thể gây tác dụng phụ ở trẻ.",
                "recommendation": "Thận trọng khi cho con bú."
            }
        },
        "hepatic_adjustment": {
            "mild": "Thận trọng",
            "moderate": "Thận trọng, giảm liều",
            "severe": "CHỐNG CHỈ ĐỊNH",
            "notes": "Paracetamol chuyển hóa ở gan, nguy cơ độc gan. Suy gan nặng là chống chỉ định."
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
            "monitoring": "Theo dõi ý thức, hô hấp, tim mạch, nhịp tim. Nếu paracetamol quá liều: theo dõi chức năng gan."
        },
        "reversal_agents": {
            "available": True,
            "agents": [
                {
                    "agent": "N-acetylcysteine (NAC)",
                    "mechanism": "Chống độc cho paracetamol quá liều",
                    "indication": "Quá liều paracetamol (>150mg/kg)",
                    "dose": "Theo phác đồ điều trị quá liều paracetamol",
                    "caution": "Chỉ hiệu quả nếu dùng trong vòng 8-10 giờ sau khi uống paracetamol"
                },
                {
                    "agent": "Physostigmine",
                    "mechanism": "Chất ức chế cholinesterase, đảo ngược tác dụng anticholinergic",
                    "indication": "Orphenadrine quá liều nặng (ảo giác, rối loạn ý thức)",
                    "dose": "0.5-2mg IV, có thể lặp lại",
                    "caution": "Chỉ dùng khi quá liều nặng, cần theo dõi chặt chẽ"
                }
            ]
        },
        "administration_instructions": {
            "oral": {
                "with_food": "Có thể uống với thức ăn hoặc không",
                "timing": "Paracetamol 450mg/Orphenadrine 35mg x 3 lần/ngày. CHỈ dùng ngắn hạn. KHÔNG vượt quá 4g paracetamol/ngày."
            }
        },
        "references": {
            "primary_sources": [
                "FDA Drug Label - Norgesic (Paracetamol/Orphenadrine)",
                "UpToDate - Muscle relaxants: Drug information"
            ],
            "last_updated": "2025-02-18",
            "evidence_level": "High - FDA-approved"
        }
    },

    "Paracetamol/Chlorzoxazone": {
        "group": "Analgesic - Combination (Paracetamol + Muscle Relaxant)",
        "vietnamese_name": "Paracetamol/Chlorzoxazone, Chlorzoxazone Compound",
        "administration": ["PO"],
        "indications": [
            "Đau cơ xương khớp kèm co thắt cơ (musculoskeletal pain with muscle spasm)",
            "Đau lưng cấp tính",
            "Đau cơ sau chấn thương"
        ],
        "contraindications": [
            "Dị ứng paracetamol hoặc chlorzoxazone",
            "Suy gan nặng"
        ],
        "dosage": {
            "adult_standard": "Paracetamol 325mg/Chlorzoxazone 250mg x 3-4 lần/ngày",
            "adult_max": "Paracetamol 4g/ngày, Chlorzoxazone 1500mg/ngày",
            "notes": "CHỈ dùng ngắn hạn. Chlorzoxazone có thể gây nước tiểu màu cam/đỏ (vô hại)."
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "Thận trọng",
            "under_30": "Thận trọng"
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
        "mechanism_of_action": "Kết hợp paracetamol (giảm đau, hạ sốt) và chlorzoxazone (giãn cơ xương khớp). Paracetamol ức chế COX-3 ở CNS, giảm đau và hạ sốt. Chlorzoxazone là thuốc giãn cơ xương khớp, tác động lên tủy sống để giảm phản xạ cơ xương. Tác dụng hiệp đồng: giảm đau cơ xương khớp kèm co thắt cơ. CHỈ dùng ngắn hạn. Có thể gây nước tiểu màu cam/đỏ (vô hại).",
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
            "clearance": "Gan: chuyển hóa. Thận: thải trừ."
        },
        "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm",
        "black_box_warnings": "Nguy cơ độc gan nghiêm trọng với paracetamol nếu quá liều (>4g/ngày). Chlorzoxazone có thể gây độc gan (hiếm nhưng nghiêm trọng). Chỉ dùng ngắn hạn. Theo dõi chức năng gan.",
        "drug_interactions": {
            "major": [
                {
                    "drug": "Alcohol",
                    "mechanism": "Tăng tác dụng ức chế CNS, tăng nguy cơ độc gan",
                    "effect": "Tăng buồn ngủ, tăng nguy cơ độc gan nặng",
                    "management": "TRÁNH RƯỢU hoàn toàn khi dùng thuốc này."
                }
            ],
            "moderate": [
                {
                    "drug": "Warfarin",
                    "mechanism": "Paracetamol có thể tăng tác dụng warfarin",
                    "effect": "Tăng INR, tăng nguy cơ chảy máu",
                    "management": "Thận trọng. Theo dõi INR thường xuyên."
                }
            ]
        },
        "contraindications": {
            "tuyệt_đối": [
                "Dị ứng paracetamol hoặc chlorzoxazone",
                "Suy gan nặng"
            ],
            "tương_đối": [
                "Suy gan trung bình - thận trọng, tránh dùng nếu có thể",
                "Bệnh gan - tăng nguy cơ độc gan"
            ]
        },
        "pregnancy_lactation": {
            "fda_category": "C",
            "pregnancy_details": "Category C. Có thể dùng nếu lợi ích > nguy cơ.",
            "lactation": {
                "safety": "Caution",
                "details": "Paracetamol và chlorzoxazone đều bài tiết vào sữa mẹ. Có thể gây tác dụng phụ ở trẻ.",
                "recommendation": "Thận trọng khi cho con bú."
            }
        },
        "hepatic_adjustment": {
            "mild": "Thận trọng, theo dõi chức năng gan",
            "moderate": "Thận trọng, tránh dùng nếu có thể",
            "severe": "CHỐNG CHỈ ĐỊNH",
            "notes": "CẢ HAI thuốc đều có nguy cơ độc gan. Suy gan nặng là chống chỉ định. Theo dõi chức năng gan định kỳ."
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
            "monitoring": "Theo dõi ý thức, hô hấp, tim mạch. Theo dõi chức năng gan (ALT, AST, bilirubin, INR) - QUAN TRỌNG."
        },
        "reversal_agents": {
            "available": True,
            "agents": [
                {
                    "agent": "N-acetylcysteine (NAC)",
                    "mechanism": "Chống độc cho paracetamol quá liều",
                    "indication": "Quá liều paracetamol (>150mg/kg)",
                    "dose": "Theo phác đồ điều trị quá liều paracetamol",
                    "caution": "Chỉ hiệu quả nếu dùng trong vòng 8-10 giờ sau khi uống paracetamol"
                }
            ]
        },
        "administration_instructions": {
            "oral": {
                "with_food": "Có thể uống với thức ăn hoặc không",
                "timing": "Paracetamol 325mg/Chlorzoxazone 250mg x 3-4 lần/ngày. CHỈ dùng ngắn hạn. KHÔNG vượt quá 4g paracetamol/ngày."
            }
        },
        "references": {
            "primary_sources": [
                "FDA Drug Label - Chlorzoxazone Compound",
                "UpToDate - Muscle relaxants: Drug information"
            ],
            "last_updated": "2025-02-18",
            "evidence_level": "High - FDA-approved"
        }
    },

    "Paracetamol/Methocarbamol": {
        "group": "Analgesic - Combination (Paracetamol + Muscle Relaxant)",
        "vietnamese_name": "Paracetamol/Methocarbamol, Robaxacet",
        "administration": ["PO"],
        "indications": [
            "Đau cơ xương khớp kèm co thắt cơ (musculoskeletal pain with muscle spasm)",
            "Đau lưng cấp tính",
            "Đau cơ sau chấn thương"
        ],
        "contraindications": [
            "Dị ứng paracetamol hoặc methocarbamol",
            "Suy gan nặng"
        ],
        "dosage": {
            "adult_standard": "Paracetamol 325mg/Methocarbamol 400mg x 4 lần/ngày",
            "adult_max": "Paracetamol 4g/ngày, Methocarbamol 2400mg/ngày",
            "notes": "CHỈ dùng ngắn hạn. Methocarbamol có thể gây nước tiểu màu xanh/đen (vô hại)."
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "Thận trọng",
            "under_30": "Thận trọng"
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
        "mechanism_of_action": "Kết hợp paracetamol (giảm đau, hạ sốt) và methocarbamol (giãn cơ xương khớp). Paracetamol ức chế COX-3 ở CNS, giảm đau và hạ sốt. Methocarbamol là thuốc giãn cơ xương khớp, tác động lên CNS để giảm phản xạ cơ xương. Tác dụng hiệp đồng: giảm đau cơ xương khớp kèm co thắt cơ. CHỈ dùng ngắn hạn. Có thể gây nước tiểu màu xanh/đen (vô hại).",
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
            "clearance": "Gan: chuyển hóa. Thận: thải trừ."
        },
        "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm",
        "black_box_warnings": "Nguy cơ độc gan nghiêm trọng với paracetamol nếu quá liều (>4g/ngày). Chỉ dùng ngắn hạn.",
        "drug_interactions": {
            "major": [
                {
                    "drug": "Alcohol",
                    "mechanism": "Tăng tác dụng ức chế CNS, tăng nguy cơ độc gan",
                    "effect": "Tăng buồn ngủ, tăng nguy cơ độc gan nặng",
                    "management": "TRÁNH RƯỢU hoàn toàn khi dùng thuốc này."
                }
            ],
            "moderate": [
                {
                    "drug": "Warfarin",
                    "mechanism": "Paracetamol có thể tăng tác dụng warfarin",
                    "effect": "Tăng INR, tăng nguy cơ chảy máu",
                    "management": "Thận trọng. Theo dõi INR thường xuyên."
                }
            ]
        },
        "contraindications": {
            "tuyệt_đối": [
                "Dị ứng paracetamol hoặc methocarbamol",
                "Suy gan nặng"
            ],
            "tương_đối": [
                "Suy gan trung bình - thận trọng"
            ]
        },
        "pregnancy_lactation": {
            "fda_category": "C",
            "pregnancy_details": "Category C. Có thể dùng nếu lợi ích > nguy cơ.",
            "lactation": {
                "safety": "Caution",
                "details": "Paracetamol và methocarbamol đều bài tiết vào sữa mẹ. Có thể gây tác dụng phụ ở trẻ.",
                "recommendation": "Thận trọng khi cho con bú."
            }
        },
        "hepatic_adjustment": {
            "mild": "Thận trọng",
            "moderate": "Thận trọng, giảm liều",
            "severe": "CHỐNG CHỈ ĐỊNH",
            "notes": "Paracetamol chuyển hóa ở gan, nguy cơ độc gan. Suy gan nặng là chống chỉ định."
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
            "monitoring": "Theo dõi ý thức, hô hấp, tim mạch. Nếu paracetamol quá liều: theo dõi chức năng gan."
        },
        "reversal_agents": {
            "available": True,
            "agents": [
                {
                    "agent": "N-acetylcysteine (NAC)",
                    "mechanism": "Chống độc cho paracetamol quá liều",
                    "indication": "Quá liều paracetamol (>150mg/kg)",
                    "dose": "Theo phác đồ điều trị quá liều paracetamol",
                    "caution": "Chỉ hiệu quả nếu dùng trong vòng 8-10 giờ sau khi uống paracetamol"
                }
            ]
        },
        "administration_instructions": {
            "oral": {
                "with_food": "Có thể uống với thức ăn hoặc không",
                "timing": "Paracetamol 325mg/Methocarbamol 400mg x 4 lần/ngày. CHỈ dùng ngắn hạn. KHÔNG vượt quá 4g paracetamol/ngày."
            }
        },
        "references": {
            "primary_sources": [
                "FDA Drug Label - Robaxacet (Paracetamol/Methocarbamol)",
                "UpToDate - Muscle relaxants: Drug information"
            ],
            "last_updated": "2025-02-18",
            "evidence_level": "High - FDA-approved"
        }
    },

    "Aspirin/Carisoprodol": {
        "group": "Analgesic - Combination (NSAID + Muscle Relaxant)",
        "vietnamese_name": "Aspirin/Carisoprodol, Soma Compound",
        "administration": ["PO"],
        "indications": [
            "Đau cơ xương khớp kèm co thắt cơ và viêm (musculoskeletal pain with muscle spasm and inflammation)",
            "Đau lưng cấp tính",
            "Đau cơ sau chấn thương"
        ],
        "contraindications": [
            "Dị ứng aspirin hoặc carisoprodol",
            "Loét dạ dày tá tràng đang hoạt động",
            "Suy thận nặng",
            "Suy gan nặng",
            "Porphyria",
            "Dị ứng với meprobamate",
            "Dùng warfarin hoặc thuốc chống đông khác"
        ],
        "dosage": {
            "adult_standard": "Aspirin 325mg/Carisoprodol 200mg x 3-4 lần/ngày",
            "adult_max": "Aspirin 4g/ngày, Carisoprodol 1400mg/ngày",
            "notes": "CHỈ dùng ngắn hạn (2-3 tuần). Aspirin có tác dụng chống kết tập tiểu cầu. Carisoprodol chuyển hóa thành meprobamate (controlled substance, nguy cơ nghiện)."
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "Thận trọng, giảm liều",
            "under_30": "Tránh dùng"
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
        "mechanism_of_action": "Kết hợp aspirin (NSAID, giảm đau, chống viêm, chống kết tập tiểu cầu) và carisoprodol (giãn cơ xương khớp). Aspirin ức chế COX-1 và COX-2, giảm đau, chống viêm, và chống kết tập tiểu cầu (ức chế không hồi phục COX-1 tiểu cầu). Carisoprodol là thuốc giãn cơ xương khớp, chuyển hóa thành meprobamate (controlled substance, có nguy cơ nghiện). Tác dụng hiệp đồng: giảm đau cơ xương khớp kèm viêm và co thắt cơ. CHỈ dùng ngắn hạn (2-3 tuần).",
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
            "clearance": "Gan: chuyển hóa. Thận: thải trừ."
        },
        "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm. Controlled substance - cần bảo quản an toàn.",
        "black_box_warnings": "NGUY CƠ NGHIỆN, LẠM DỤNG, VÀ LỆ THUỘC - carisoprodol chuyển hóa thành meprobamate (controlled substance). Nguy cơ chảy máu dạ dày nặng với aspirin. CHỐNG CHỈ ĐỊNH với warfarin hoặc thuốc chống đông khác. Chỉ dùng ngắn hạn (2-3 tuần).",
        "drug_interactions": {
            "major": [
                {
                    "drug": "Warfarin, các thuốc chống đông khác",
                    "mechanism": "Aspirin ức chế COX-1 tiểu cầu, tăng nguy cơ chảy máu",
                    "effect": "Tăng nguy cơ chảy máu nặng, tăng INR",
                    "management": "CHỐNG CHỈ ĐỊNH. Tránh dùng cùng. Nếu phải dùng, theo dõi INR thường xuyên."
                },
                {
                    "drug": "Alcohol",
                    "mechanism": "Tăng tác dụng ức chế CNS, tăng nguy cơ chảy máu dạ dày",
                    "effect": "Tăng buồn ngủ, tăng nguy cơ chảy máu dạ dày nặng",
                    "management": "TRÁNH RƯỢU hoàn toàn khi dùng thuốc này."
                }
            ],
            "moderate": [
                {
                    "drug": "CNS depressants (Benzodiazepines, Opioids)",
                    "mechanism": "Tăng tác dụng ức chế CNS",
                    "effect": "Tăng buồn ngủ, nguy cơ ức chế hô hấp",
                    "management": "Thận trọng. Giảm liều nếu cần."
                }
            ]
        },
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
            ]
        },
        "pregnancy_lactation": {
            "fda_category": "C - D trong 3 tháng cuối",
            "pregnancy_details": "Category C trong 3 tháng đầu-2. Category D trong 3 tháng cuối - CHỐNG CHỈ ĐỊNH. Aspirin trong 3 tháng cuối có thể gây đóng ống động mạch sớm, thiểu ối. Có thể dùng trong 3 tháng đầu-2 nếu lợi ích > nguy cơ.",
            "lactation": {
                "safety": "Caution",
                "details": "Aspirin và carisoprodol đều bài tiết vào sữa mẹ. Có thể gây tác dụng phụ ở trẻ.",
                "recommendation": "Thận trọng khi cho con bú. Không khuyến cáo dùng aspirin khi cho con bú, đặc biệt liều cao."
            }
        },
        "hepatic_adjustment": {
            "mild": "Không đổi",
            "moderate": "Thận trọng",
            "severe": "CHỐNG CHỈ ĐỊNH",
            "notes": "Cả hai thuốc đều chuyển hóa ở gan. Suy gan nặng là chống chỉ định."
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
            "monitoring": "Theo dõi ý thức, hô hấp, tim mạch. Nếu aspirin quá liều: theo dõi nồng độ salicylat máu, khí máu, điện giải."
        },
        "reversal_agents": {
            "available": False,
            "agents": []
        },
        "administration_instructions": {
            "oral": {
                "with_food": "Uống với thức ăn hoặc sữa để giảm kích ứng dạ dày (aspirin)",
                "timing": "Aspirin 325mg/Carisoprodol 200mg x 3-4 lần/ngày. CHỈ dùng ngắn hạn (2-3 tuần). Uống với thức ăn để giảm kích ứng dạ dày."
            }
        },
        "references": {
            "primary_sources": [
                "FDA Drug Label - Soma Compound (Aspirin/Carisoprodol)",
                "UpToDate - Muscle relaxants: Drug information",
                "UpToDate - Aspirin: Drug information"
            ],
            "last_updated": "2025-02-18",
            "evidence_level": "High - FDA-approved, controlled substance"
        }
    }
}

__all__ = ['PAIN_MUSCLE_RELAXANT_COMBINATIONS_DRUGS']

