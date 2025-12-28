"""ENT / Upper Respiratory Combination Medications
Đường uống và xịt mũi: kháng histamin + thuốc thông mũi, corticoid mũi phối hợp.
Nhóm này dùng nhiều trong tai mũi họng và hô hấp trên (viêm mũi dị ứng, viêm xoang…)."""

ENT_ORAL_NASAL_COMBINATIONS_DRUGS = {
    "Loratadine/Pseudoephedrine": {
        "group": "ENT - Combination (Oral Antihistamine + Decongestant)",
        "vietnamese_name": "Loratadine/Pseudoephedrine, Clarityne-D",
        "administration": ["PO"],
        "indications": [
            "Viêm mũi dị ứng có nghẹt mũi (allergic rhinitis with nasal congestion)",
            "Cảm lạnh, viêm mũi xoang kèm nghẹt mũi",
        ],
        "contraindications": [
            "Dị ứng với loratadine, pseudoephedrine hoặc thành phần khác",
            "Tăng huyết áp nặng, bệnh mạch vành, nhồi máu cơ tim gần đây",
            "Cường giáp, glaucom góc đóng",
            "Đang dùng IMAO hoặc trong vòng 14 ngày ngừng IMAO",
        ],
        "dosage": {
            "adult": "1 viên (loratadine 5mg + pseudoephedrine 120mg) mỗi 12 giờ",
            "adult_max": "2 viên/ngày",
            "notes": "Không dùng quá 10 ngày liên tục. Uống trước 18h để tránh mất ngủ.",
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "Cân nhắc kéo dài khoảng cách liều pseudoephedrine",
            "under_30": "Tránh dùng hoặc chọn thuốc khác an toàn hơn",
        },
        "side_effects": [
            "Tim đập nhanh, tăng huyết áp (do pseudoephedrine)",
            "Mất ngủ, kích thích, lo âu",
            "Khô miệng, nhức đầu",
        ],
        "interactions": [
            "IMAO: nguy cơ tăng huyết áp ác tính (CHỐNG CHỈ ĐỊNH)",
            "Thuốc cường giao cảm khác: tăng nguy cơ tim mạch",
            "Thuốc hạ huyết áp: giảm hiệu quả",
        ],
        "pregnancy": "C",
        "mechanism_of_action": "Loratadine kháng H1 ngoại vi, giảm hắt hơi, chảy mũi, ngứa. Pseudoephedrine là chất cường giao cảm, co mạch niêm mạc mũi, giảm sung huyết và nghẹt mũi.",
        "monitoring": [
            "Huyết áp, nhịp tim (đặc biệt ở người có bệnh tim mạch)",
            "Triệu chứng mất ngủ, kích thích",
        ],
        "precautions": [
            "Không dùng kéo dài; chỉ dùng ngắn ngày cho giai đoạn cấp.",
            "Thận trọng ở người tăng huyết áp, bệnh mạch vành, người cao tuổi.",
        ],
        "pharmacokinetics": {
            "half_life": "Loratadine: 8-14 giờ; Pseudoephedrine: 9-16 giờ",
            "onset": "Loratadine: 1-3 giờ; Pseudoephedrine: 30-60 phút",
            "duration": "Loratadine: 24 giờ; Pseudoephedrine: 4-6 giờ",
            "protein_binding": "Loratadine: 97-99%; Pseudoephedrine: Thấp",
            "clearance": "Loratadine: Gan (chuyển hóa CYP3A4, CYP2D6); Pseudoephedrine: Thận (thải trừ nguyên dạng 70-90%)"
        },
        "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm, tránh ánh sáng",
        "black_box_warnings": None,
        "drug_interactions": {
            "major": [
                {
                    "drug": "MAOIs (phenelzine, tranylcypromine)",
                    "mechanism": "Pseudoephedrine: tăng giải phóng catecholamine",
                    "effect": "Nguy cơ tăng huyết áp ác tính, tăng thân nhiệt",
                    "management": "CHỐNG CHỈ ĐỊNH. Tránh dùng trong vòng 14 ngày sau khi ngừng MAOIs."
                }
            ],
            "moderate": [
                {
                    "drug": "Thuốc cường giao cảm khác (ephedrine, phenylephrine)",
                    "mechanism": "Tác dụng cộng dồn",
                    "effect": "Tăng nguy cơ tim mạch (tăng huyết áp, nhịp tim nhanh)",
                    "management": "Thận trọng. Theo dõi huyết áp, nhịp tim."
                },
                {
                    "drug": "Thuốc hạ huyết áp",
                    "mechanism": "Pseudoephedrine: đối kháng tác dụng",
                    "effect": "Giảm hiệu quả thuốc hạ huyết áp",
                    "management": "Thận trọng. Theo dõi huyết áp."
                }
            ],
            "minor": []
        },
        "contraindications": {
            "tuyệt_đối": [
                "Dị ứng với loratadine, pseudoephedrine hoặc thành phần khác",
                "Đang dùng MAOIs hoặc trong vòng 14 ngày ngừng MAOIs",
                "Tăng huyết áp nặng, bệnh mạch vành nặng, nhồi máu cơ tim gần đây",
                "Cường giáp nặng, glaucom góc đóng"
            ],
            "tương_đối": [
                "Tăng huyết áp nhẹ đến trung bình - thận trọng",
                "Bệnh mạch vành nhẹ - thận trọng",
                "Người cao tuổi - thận trọng",
                "Suy thận - giảm liều pseudoephedrine"
            ]
        },
        "pregnancy_lactation": {
            "fda_category": "C",
            "pregnancy_details": "Category C - có nguy cơ cho thai nhi. Pseudoephedrine: có thể gây co mạch tử cung, giảm lưu lượng máu thai nhi. Loratadine: dữ liệu hạn chế.",
            "lactation": {
                "safety": "Compatible with monitoring",
                "details": "Loratadine và pseudoephedrine bài tiết vào sữa mẹ ở nồng độ thấp.",
                "recommendation": "Có thể dùng khi cho con bú với theo dõi. Thận trọng với pseudoephedrine (có thể gây kích thích ở trẻ)."
            }
        },
        "hepatic_adjustment": {
            "mild": "Không đổi",
            "moderate": "Thận trọng (loratadine chuyển hóa qua gan)",
            "severe": "Thận trọng, có thể giảm liều",
            "notes": "Loratadine chuyển hóa qua gan (CYP3A4, CYP2D6). Suy gan có thể làm giảm chuyển hóa và tăng nồng độ loratadine."
        },
        "overdose_management": {
            "symptoms": [
                "Pseudoephedrine: tăng huyết áp, nhịp tim nhanh, lo âu, mất ngủ, co giật (hiếm)",
                "Loratadine: buồn ngủ, nhức đầu, tim đập nhanh (hiếm)"
            ],
            "antidote": "Không có antidote đặc hiệu",
            "treatment": [
                "Ngừng ngay thuốc",
                "Rửa dạ dày nếu uống trong vòng 1-2 giờ",
                "Than hoạt tính",
                "Điều trị triệu chứng: benzodiazepines nếu co giật, thuốc hạ huyết áp nếu tăng huyết áp nặng",
                "Theo dõi huyết áp, nhịp tim, dấu hiệu sinh tồn"
            ],
            "monitoring": "Huyết áp, nhịp tim, ECG, dấu hiệu sinh tồn"
        },
        "reversal_agents": {
            "available": False,
            "agents": []
        },
        "administration_instructions": {
            "oral": {
                "with_food": "Có thể uống với hoặc không có thức ăn",
                "timing": "Uống mỗi 12 giờ (2 lần/ngày). Uống trước 18h để tránh mất ngủ do pseudoephedrine.",
                "notes": "Không dùng quá 10 ngày liên tục. Uống đủ nước."
            }
        },
        "references": {
            "primary_sources": [
                "FDA Drug Label - Clarityne-D (loratadine/pseudoephedrine)",
                "UpToDate - Combination antihistamine and decongestant products"
            ],
            "last_updated": "2025-02-05",
            "evidence_level": "A"
        },
             "black_box_warnings": None,
         "black_box_warnings": None,
         "black_box_warnings": None,
         "black_box_warnings": None,
         "black_box_warnings": None,
         "black_box_warnings": None,
         "black_box_warnings": None,
         "black_box_warnings": None,
         "black_box_warnings": None,
         "black_box_warnings": None,
         "black_box_warnings": None,
         "black_box_warnings": None,
         "black_box_warnings": None,
         "black_box_warnings": None,
         "black_box_warnings": None,
         "black_box_warnings": None,
         "black_box_warnings": "Không có",
},
    "Cetirizine/Pseudoephedrine": {
        "group": "ENT - Combination (Oral Antihistamine + Decongestant)",
        "vietnamese_name": "Cetirizine/Pseudoephedrine, Zyrtec-D",
        "administration": ["PO"],
        "indications": [
            "Viêm mũi dị ứng kèm nghẹt mũi",
        ],
        "contraindications": [
            "Dị ứng với cetirizine, pseudoephedrine hoặc thành phần khác",
            "Tăng huyết áp nặng, bệnh mạch vành",
            "Cường giáp, glaucom góc đóng",
            "Đang dùng IMAO hoặc trong vòng 14 ngày ngừng IMAO",
        ],
        "dosage": {
            "adult": "1 viên (cetirizine 5mg + pseudoephedrine 120mg) mỗi 12 giờ",
            "adult_max": "2 viên/ngày",
            "notes": "Có thể gây buồn ngủ (cetirizine) và mất ngủ (pseudoephedrine); đánh giá trên từng bệnh nhân.",
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "Giảm tần suất dùng (mỗi 24 giờ)",
            "under_30": "Tránh dùng",
        },
        "side_effects": [
            "Buồn ngủ hoặc mất ngủ",
            "Tim đập nhanh, tăng huyết áp",
            "Khô miệng, nhức đầu",
        ],
        "interactions": [
            "IMAO: CHỐNG CHỈ ĐỊNH",
            "Alcohol, thuốc ức chế TKTW: tăng buồn ngủ (cetirizine)",
        ],
        "pregnancy": "C",
        "mechanism_of_action": "Cetirizine kháng H1, pseudoephedrine co mạch niêm mạc mũi, kết hợp giúp giảm cả triệu chứng dị ứng và nghẹt mũi.",
        "monitoring": [
            "Huyết áp, nhịp tim",
            "Mức độ buồn ngủ/kích thích",
        ],
        "precautions": [
            "Không dùng cho bệnh nhân tim mạch nặng, tăng huyết áp khó kiểm soát.",
            "Không dùng kéo dài >10 ngày.",
        ],
        "pharmacokinetics": {
            "half_life": "Cetirizine: 8-11 giờ; Pseudoephedrine: 9-16 giờ",
            "onset": "Cetirizine: 1 giờ; Pseudoephedrine: 30-60 phút",
            "duration": "Cetirizine: 24 giờ; Pseudoephedrine: 4-6 giờ",
            "protein_binding": "Cetirizine: 93%; Pseudoephedrine: Thấp",
            "clearance": "Cetirizine: Thận (70% thải trừ nguyên dạng); Pseudoephedrine: Thận (thải trừ nguyên dạng 70-90%)"
        },
        "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm, tránh ánh sáng",
        "black_box_warnings": None,
        "drug_interactions": {
            "major": [
                {
                    "drug": "MAOIs (phenelzine, tranylcypromine)",
                    "mechanism": "Pseudoephedrine: tăng giải phóng catecholamine",
                    "effect": "Nguy cơ tăng huyết áp ác tính, tăng thân nhiệt",
                    "management": "CHỐNG CHỈ ĐỊNH. Tránh dùng trong vòng 14 ngày sau khi ngừng MAOIs."
                }
            ],
            "moderate": [
                {
                    "drug": "Alcohol, thuốc ức chế TKTW (benzodiazepines, opioids)",
                    "mechanism": "Cetirizine: tác dụng cộng dồn",
                    "effect": "Tăng buồn ngủ, giảm sự tỉnh táo",
                    "management": "Thận trọng. Tránh lái xe, vận hành máy móc."
                },
                {
                    "drug": "Thuốc cường giao cảm khác",
                    "mechanism": "Tác dụng cộng dồn",
                    "effect": "Tăng nguy cơ tim mạch",
                    "management": "Thận trọng. Theo dõi huyết áp, nhịp tim."
                }
            ],
            "minor": []
        },
        "contraindications": {
            "tuyệt_đối": [
                "Dị ứng với cetirizine, pseudoephedrine hoặc thành phần khác",
                "Đang dùng MAOIs hoặc trong vòng 14 ngày ngừng MAOIs",
                "Tăng huyết áp nặng, bệnh mạch vành nặng",
                "Cường giáp nặng, glaucom góc đóng"
            ],
            "tương_đối": [
                "Tăng huyết áp nhẹ đến trung bình - thận trọng",
                "Bệnh mạch vành nhẹ - thận trọng",
                "Suy thận - giảm tần suất dùng"
            ]
        },
        "pregnancy_lactation": {
            "fda_category": "C",
            "pregnancy_details": "Category C - có nguy cơ cho thai nhi. Pseudoephedrine: có thể gây co mạch tử cung. Cetirizine: dữ liệu hạn chế, nhưng an toàn hơn các thuốc kháng H1 thế hệ 1.",
            "lactation": {
                "safety": "Compatible with monitoring",
                "details": "Cetirizine và pseudoephedrine bài tiết vào sữa mẹ ở nồng độ thấp.",
                "recommendation": "Có thể dùng khi cho con bú với theo dõi."
            }
        },
        "hepatic_adjustment": {
            "mild": "Không đổi",
            "moderate": "Không đổi",
            "severe": "Thận trọng",
            "notes": "Cetirizine chủ yếu thải trừ qua thận. Pseudoephedrine thải trừ qua thận. Suy gan không ảnh hưởng đáng kể."
        },
        "overdose_management": {
            "symptoms": [
                "Pseudoephedrine: tăng huyết áp, nhịp tim nhanh, lo âu, mất ngủ, co giật (hiếm)",
                "Cetirizine: buồn ngủ, nhức đầu (hiếm, thường nhẹ)"
            ],
            "antidote": "Không có antidote đặc hiệu",
            "treatment": [
                "Ngừng ngay thuốc",
                "Rửa dạ dày nếu uống trong vòng 1-2 giờ",
                "Than hoạt tính",
                "Điều trị triệu chứng: benzodiazepines nếu co giật, thuốc hạ huyết áp nếu tăng huyết áp nặng",
                "Theo dõi huyết áp, nhịp tim"
            ],
            "monitoring": "Huyết áp, nhịp tim, ECG, dấu hiệu sinh tồn"
        },
        "reversal_agents": {
            "available": False,
            "agents": []
        },
        "administration_instructions": {
            "oral": {
                "with_food": "Có thể uống với hoặc không có thức ăn",
                "timing": "Uống mỗi 12 giờ (2 lần/ngày). Uống trước 18h để tránh mất ngủ.",
                "notes": "Không dùng kéo dài >10 ngày."
            }
        },
        "references": {
            "primary_sources": [
                "FDA Drug Label - Zyrtec-D (cetirizine/pseudoephedrine)",
                "UpToDate - Combination antihistamine and decongestant products"
            ],
            "last_updated": "2025-02-05",
            "evidence_level": "A"
        },
             "black_box_warnings": None,
         "black_box_warnings": None,
         "black_box_warnings": None,
         "black_box_warnings": None,
         "black_box_warnings": None,
         "black_box_warnings": None,
         "black_box_warnings": None,
         "black_box_warnings": None,
         "black_box_warnings": None,
         "black_box_warnings": None,
         "black_box_warnings": None,
         "black_box_warnings": None,
         "black_box_warnings": None,
         "black_box_warnings": None,
         "black_box_warnings": None,
         "black_box_warnings": None,
         "black_box_warnings": None,
         "black_box_warnings": "Không có",
},
    "Fexofenadine/Pseudoephedrine": {
        "group": "ENT - Combination (Oral Antihistamine + Decongestant)",
        "vietnamese_name": "Fexofenadine/Pseudoephedrine, Allegra-D",
        "administration": ["PO"],
        "indications": [
            "Viêm mũi dị ứng theo mùa kèm nghẹt mũi",
        ],
        "contraindications": [
            "Dị ứng với fexofenadine, pseudoephedrine",
            "Tăng huyết áp nặng, bệnh mạch vành",
            "Cường giáp, glaucom góc đóng",
            "Đang dùng IMAO hoặc trong vòng 14 ngày ngừng IMAO",
        ],
        "dosage": {
            "adult": "60/120mg mỗi 12 giờ hoặc 180/240mg mỗi 24 giờ (tùy chế phẩm)",
            "notes": "Fexofenadine ít gây buồn ngủ; pseudoephedrine có thể gây mất ngủ.",
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "Giảm tần suất dùng",
            "under_30": "Thận trọng hoặc tránh dùng",
        },
        "side_effects": [
            "Mất ngủ, kích thích",
            "Tim đập nhanh, tăng huyết áp",
            "Đau đầu, khô miệng",
        ],
        "interactions": [
            "Fruit juices: giảm hấp thu fexofenadine (uống cách xa 2 giờ)",
            "IMAO: CHỐNG CHỈ ĐỊNH (pseudoephedrine)",
        ],
        "pregnancy": "C",
        "mechanism_of_action": "Fexofenadine kháng H1 không gây buồn ngủ; pseudoephedrine co mạch niêm mạc mũi, giảm nghẹt mũi.",
        "monitoring": [
            "Huyết áp, nhịp tim",
            "Triệu chứng kích thích TKTW (mất ngủ, lo âu)",
        ],
        "precautions": [
            "Không dùng với nước hoa quả (giảm hấp thu fexofenadine).",
            "Không dùng kéo dài, chỉ dùng ngắn ngày.",
        ],
        "pharmacokinetics": {
            "half_life": "Fexofenadine: 14.4 giờ; Pseudoephedrine: 9-16 giờ",
            "onset": "Fexofenadine: 1 giờ; Pseudoephedrine: 30-60 phút",
            "duration": "Fexofenadine: 24 giờ; Pseudoephedrine: 4-6 giờ",
            "protein_binding": "Fexofenadine: 60-70%; Pseudoephedrine: Thấp",
            "clearance": "Fexofenadine: Thận (80% thải trừ nguyên dạng, 11% qua phân); Pseudoephedrine: Thận (thải trừ nguyên dạng 70-90%)"
        },
        "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm, tránh ánh sáng",
        "black_box_warnings": None,
        "drug_interactions": {
            "major": [
                {
                    "drug": "MAOIs (phenelzine, tranylcypromine)",
                    "mechanism": "Pseudoephedrine: tăng giải phóng catecholamine",
                    "effect": "Nguy cơ tăng huyết áp ác tính, tăng thân nhiệt",
                    "management": "CHỐNG CHỈ ĐỊNH. Tránh dùng trong vòng 14 ngày sau khi ngừng MAOIs."
                }
            ],
            "moderate": [
                {
                    "drug": "Fruit juices (apple, orange, grapefruit)",
                    "mechanism": "Giảm hấp thu fexofenadine qua transporter",
                    "effect": "Giảm nồng độ fexofenadine đáng kể (giảm 36-40%)",
                    "management": "Uống cách xa nước hoa quả ít nhất 2 giờ."
                },
                {
                    "drug": "Ketoconazole, erythromycin",
                    "mechanism": "Ức chế P-glycoprotein",
                    "effect": "Tăng nồng độ fexofenadine (ít quan trọng về mặt lâm sàng)",
                    "management": "Thận trọng. Theo dõi tác dụng phụ."
                }
            ],
            "minor": []
        },
        "contraindications": {
            "tuyệt_đối": [
                "Dị ứng với fexofenadine, pseudoephedrine hoặc thành phần khác",
                "Đang dùng MAOIs hoặc trong vòng 14 ngày ngừng MAOIs",
                "Tăng huyết áp nặng, bệnh mạch vành nặng",
                "Cường giáp nặng, glaucom góc đóng"
            ],
            "tương_đối": [
                "Tăng huyết áp nhẹ đến trung bình - thận trọng",
                "Bệnh mạch vành nhẹ - thận trọng",
                "Suy thận - giảm tần suất dùng"
            ]
        },
        "pregnancy_lactation": {
            "fda_category": "C",
            "pregnancy_details": "Category C - có nguy cơ cho thai nhi. Pseudoephedrine: có thể gây co mạch tử cung. Fexofenadine: dữ liệu hạn chế, nhưng được coi là an toàn hơn các thuốc kháng H1 thế hệ 1.",
            "lactation": {
                "safety": "Compatible with monitoring",
                "details": "Fexofenadine và pseudoephedrine bài tiết vào sữa mẹ ở nồng độ thấp.",
                "recommendation": "Có thể dùng khi cho con bú với theo dõi."
            }
        },
        "hepatic_adjustment": {
            "mild": "Không đổi",
            "moderate": "Không đổi",
            "severe": "Không đổi",
            "notes": "Fexofenadine chủ yếu thải trừ qua thận (không chuyển hóa qua gan). Pseudoephedrine thải trừ qua thận. Suy gan không ảnh hưởng đáng kể."
        },
        "overdose_management": {
            "symptoms": [
                "Pseudoephedrine: tăng huyết áp, nhịp tim nhanh, lo âu, mất ngủ, co giật (hiếm)",
                "Fexofenadine: nhức đầu, buồn nôn (hiếm, thường nhẹ)"
            ],
            "antidote": "Không có antidote đặc hiệu",
            "treatment": [
                "Ngừng ngay thuốc",
                "Rửa dạ dày nếu uống trong vòng 1-2 giờ",
                "Than hoạt tính",
                "Điều trị triệu chứng: benzodiazepines nếu co giật, thuốc hạ huyết áp nếu tăng huyết áp nặng",
                "Theo dõi huyết áp, nhịp tim"
            ],
            "monitoring": "Huyết áp, nhịp tim, ECG, dấu hiệu sinh tồn"
        },
        "reversal_agents": {
            "available": False,
            "agents": []
        },
        "administration_instructions": {
            "oral": {
                "with_food": "Có thể uống với hoặc không có thức ăn. Uống với nước lọc (KHÔNG với nước hoa quả).",
                "timing": "Uống mỗi 12 giờ hoặc mỗi 24 giờ tùy chế phẩm. Uống trước 18h để tránh mất ngủ.",
                "notes": "QUAN TRỌNG: Uống cách xa nước hoa quả (apple, orange, grapefruit) ít nhất 2 giờ để tránh giảm hấp thu fexofenadine. Không dùng kéo dài."
            }
        },
        "references": {
            "primary_sources": [
                "FDA Drug Label - Allegra-D (fexofenadine/pseudoephedrine)",
                "UpToDate - Combination antihistamine and decongestant products"
            ],
            "last_updated": "2025-02-05",
            "evidence_level": "A"
        },
             "black_box_warnings": None,
         "black_box_warnings": None,
         "black_box_warnings": None,
         "black_box_warnings": None,
         "black_box_warnings": None,
         "black_box_warnings": None,
         "black_box_warnings": None,
         "black_box_warnings": None,
         "black_box_warnings": None,
         "black_box_warnings": None,
         "black_box_warnings": None,
         "black_box_warnings": None,
         "black_box_warnings": None,
         "black_box_warnings": None,
         "black_box_warnings": None,
         "black_box_warnings": None,
         "black_box_warnings": None,
         "black_box_warnings": "Không có",
},
    "Azelastine/Fluticasone nasal spray": {
        "group": "ENT - Combination (Intranasal Antihistamine + Corticosteroid)",
        "vietnamese_name": "Azelastine/Fluticasone xịt mũi, Dymista",
        "administration": ["Nasal"],
        "indications": [
            "Viêm mũi dị ứng trung bình–nặng (perennial/seasonal)",
            "Bệnh nhân không đáp ứng đủ với corticoid mũi đơn độc",
        ],
        "contraindications": [
            "Dị ứng với azelastine, fluticasone hoặc thành phần khác",
            "Nhiễm trùng mũi chưa điều trị (nấm, lao…) – thận trọng",
        ],
        "dosage": {
            "adult": "1 nhát xịt mỗi bên mũi x 2 lần/ngày",
            "notes": "Lắc kỹ trước khi dùng. Hướng đầu xịt hơi ra ngoài vách ngăn để tránh chảy máu mũi.",
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "Không đổi",
            "under_30": "Không đổi",
        },
        "side_effects": [
            "Cảm giác đắng ở miệng (azelastine)",
            "Kích ứng mũi, khô mũi",
            "Chảy máu mũi nhẹ",
            "Nấm họng/mũi (hiếm, do corticoid)",
        ],
        "interactions": [
            "Ritonavir, ketoconazole, itraconazole: tăng nồng độ fluticasone (thận trọng)",
            "Rượu hoặc thuốc an thần: có thể tăng buồn ngủ nhẹ (azelastine)",
        ],
        "pregnancy": "C",
        "mechanism_of_action": "Azelastine là kháng H1 tại chỗ, giảm ngứa, hắt hơi, chảy mũi; fluticasone là corticoid mũi kháng viêm mạnh, giảm phù nề niêm mạc mũi. Phối hợp cho hiệu quả nhanh và mạnh hơn đơn trị.",
        "monitoring": [
            "Triệu chứng viêm mũi (ngứa, hắt hơi, chảy mũi, nghẹt mũi)",
            "Chảy máu mũi, kích ứng mũi",
            "Dấu hiệu nhiễm trùng nấm tại chỗ",
        ],
        "precautions": [
            "Hướng vòi xịt lệch ra ngoài vách ngăn để tránh loét vách ngăn.",
            "Súc miệng/nước sau xịt để giảm vị đắng và nguy cơ nấm.",
            "Không dùng kéo dài liều cao nếu không cần thiết; đánh giá định kỳ.",
        ],
        "pharmacokinetics": {
            "half_life": "Azelastine: 22 giờ; Fluticasone: 7.8 giờ",
            "onset": "Azelastine: 15 phút (nhanh); Fluticasone: vài giờ đến vài ngày",
            "duration": "Azelastine: 12 giờ; Fluticasone: 12 giờ",
            "protein_binding": "Azelastine: 78-88%; Fluticasone: 91%",
            "clearance": "Azelastine: Gan (chuyển hóa CYP3A4 thành desmethylazelastine), thận (thải trừ). Fluticasone: Gan (chuyển hóa CYP3A4), thận (thải trừ). Hấp thu toàn thân từ dạng xịt mũi: tối thiểu."
        },
        "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm, tránh ánh sáng. Lắc kỹ trước khi dùng.",
        "black_box_warnings": None,
        "drug_interactions": {
            "major": [],
            "moderate": [
                {
                    "drug": "Ritonavir, ketoconazole, itraconazole, clarithromycin",
                    "mechanism": "Ức chế CYP3A4, tăng chuyển hóa fluticasone",
                    "effect": "Tăng nồng độ fluticasone toàn thân, tăng nguy cơ ức chế HPA, hội chứng Cushing",
                    "management": "Thận trọng. Theo dõi dấu hiệu ức chế HPA. Có thể cần giảm liều fluticasone."
                },
                {
                    "drug": "Rượu hoặc thuốc an thần",
                    "mechanism": "Azelastine: tác dụng cộng dồn",
                    "effect": "Tăng buồn ngủ nhẹ (ít hơn các thuốc kháng H1 thế hệ 1)",
                    "management": "Thận trọng. Tránh lái xe, vận hành máy móc nếu buồn ngủ."
                }
            ],
            "minor": []
        },
        "contraindications": {
            "tuyệt_đối": [
                "Dị ứng với azelastine, fluticasone hoặc thành phần khác"
            ],
            "tương_đối": [
                "Nhiễm trùng mũi chưa điều trị (nấm, lao) - thận trọng, điều trị nhiễm trùng trước",
                "Dùng với ritonavir, ketoconazole - thận trọng (tăng nguy cơ ức chế HPA)"
            ]
        },
        "pregnancy_lactation": {
            "fda_category": "C",
            "pregnancy_details": "Category C - có nguy cơ cho thai nhi. Fluticasone: có nguy cơ ức chế HPA ở thai nhi nếu dùng liều cao, kéo dài. Azelastine: dữ liệu hạn chế. Hấp thu toàn thân từ dạng xịt mũi: tối thiểu, giảm nguy cơ.",
            "lactation": {
                "safety": "Compatible with monitoring",
                "details": "Azelastine và fluticasone bài tiết vào sữa mẹ ở nồng độ thấp. Hấp thu toàn thân từ dạng xịt mũi: tối thiểu.",
                "recommendation": "Có thể dùng khi cho con bú với theo dõi."
            }
        },
        "hepatic_adjustment": {
            "mild": "Không đổi",
            "moderate": "Không đổi",
            "severe": "Thận trọng",
            "notes": "Azelastine và fluticasone chuyển hóa qua gan (CYP3A4). Suy gan nặng có thể làm giảm chuyển hóa. Tuy nhiên, hấp thu toàn thân từ dạng xịt mũi: tối thiểu, nên ít ảnh hưởng."
        },
        "overdose_management": {
            "symptoms": [
                "Azelastine: buồn ngủ nhẹ, nhức đầu (hiếm, thường nhẹ do hấp thu toàn thân tối thiểu)",
                "Fluticasone: kích ứng mũi, chảy máu mũi (tại chỗ), hiếm khi có dấu hiệu ức chế HPA nếu hấp thu nhiều"
            ],
            "antidote": "Không có antidote đặc hiệu",
            "treatment": [
                "Ngừng ngay thuốc",
                "Rửa sạch mũi bằng nước muối sinh lý",
                "Điều trị triệu chứng",
                "Nếu có dấu hiệu ức chế HPA (hiếm): theo dõi, có thể cần bổ sung corticosteroid"
            ],
            "monitoring": "Triệu chứng tại chỗ, dấu hiệu ức chế HPA (nếu hấp thu nhiều)"
        },
        "reversal_agents": {
            "available": False,
            "agents": []
        },
        "administration_instructions": {
            "nasal": {
                "preparation": "Lắc kỹ chai trước khi dùng.",
                "technique": "Xì mũi nhẹ trước. Nghiêng đầu về phía trước. Đưa vòi xịt vào một bên mũi, hướng vòi xịt LỆCH RA NGOÀI (về phía má, không hướng vào vách ngăn) để tránh loét vách ngăn và chảy máu mũi.",
                "dosing": "1 nhát xịt mỗi bên mũi x 2 lần/ngày (sáng và tối).",
                "after_use": "Súc miệng/nước sau xịt để giảm vị đắng (do azelastine chảy xuống họng) và nguy cơ nấm họng/mũi (do fluticasone).",
                "notes": "Không dùng kéo dài liều cao nếu không cần thiết. Đánh giá định kỳ."
            }
        },
        "references": {
            "primary_sources": [
                "FDA Drug Label - Dymista (azelastine/fluticasone nasal spray)",
                "UpToDate - Intranasal antihistamines and combination products for allergic rhinitis"
            ],
            "last_updated": "2025-02-05",
            "evidence_level": "A"
        },
             "black_box_warnings": None,
         "black_box_warnings": None,
         "black_box_warnings": None,
         "black_box_warnings": None,
         "black_box_warnings": None,
         "black_box_warnings": None,
         "black_box_warnings": None,
         "black_box_warnings": None,
         "black_box_warnings": None,
         "black_box_warnings": None,
         "black_box_warnings": None,
         "black_box_warnings": None,
         "black_box_warnings": None,
         "black_box_warnings": None,
         "black_box_warnings": None,
         "black_box_warnings": None,
         "black_box_warnings": None,
         "black_box_warnings": "Không có",
},
}

__all__ = ["ENT_ORAL_NASAL_COMBINATIONS_DRUGS"]


