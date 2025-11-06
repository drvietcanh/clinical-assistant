"""
Supportive Care Medications (Vitamins, Corticosteroids, Antihistamines)
Active module - contains all supportive care drug data
"""

SUPPORTIVE_DRUGS = {
"Loratadine": {
        "group": "Allergy - Antihistamine (H1 Antagonist, 2nd generation)",
        "vietnamese_name": "Loratadine, Clarityne",
        "administration": ["PO"],
        "indications": [
            "Dị ứng (allergic rhinitis)",
            "Mề đay (urticaria)",
            "Dị ứng thức ăn",
            "Dị ứng da"
        ],
        "contraindications": [
            "Dị ứng"
        ],
        "dosage": {
            "adult_standard": "10mg x 1 lần/ngày",
            "adult_max": "10mg x 2 lần/ngày",
            "pediatric": "5mg x 1 lần/ngày (2-12 tuổi)",
            "notes": "Non-sedating, ít tác dụng phụ"
        },
        "side_effects": [
            "Buồn ngủ (ít hơn 1st generation)",
            "Khô miệng (hiếm)",
            "Nhức đầu (hiếm)",
            "Ít tác dụng phụ hơn antihistamine 1st generation"
        ],
        "interactions": [
            "Ít tương tác",
            "Erythromycin/Ketoconazole: tăng nồng độ (nhưng thường không cần điều chỉnh)"
        ],
        "pregnancy": "B",
        "mechanism_of_action": "Loratadine là antihistamine thế hệ thứ hai, đối kháng chọn lọc và có ái lực cao với thụ thể H1 ở ngoại biên. Khác với antihistamine thế hệ thứ nhất (diphenhydramine, chlorpheniramine), loratadine ít qua hàng rào máu-não nên ít gây buồn ngủ và tác dụng phụ anticholinergic. Loratadine ức chế phóng thích histamine từ mast cells và basophils, ngăn chặn tác dụng của histamine trên các thụ thể H1 ở mạch máu, cơ trơn phế quản, và các mô khác. Điều này làm giảm các triệu chứng dị ứng như ngứa, chảy nước mũi, hắt hơi, và mề đay. Loratadine cũng có tác dụng kháng viêm nhẹ do ức chế phóng thích các chất trung gian gây viêm.",
        "monitoring": [
            "Đáp ứng điều trị (giảm triệu chứng dị ứng)",
            "Tác dụng phụ (buồn ngủ, khô miệng) - hiếm với loratadine",
            "Chức năng gan nếu dùng lâu dài hoặc có triệu chứng (hiếm)",
            "Tương tác với erythromycin, ketoconazole (có thể tăng nồng độ nhưng thường không cần điều chỉnh)"
        ],
        "precautions": [
            "Non-sedating nhưng một số người vẫn có thể buồn ngủ nhẹ",
            "Có thể dùng với thức ăn hoặc không (hấp thu tốt)",
            "Thận trọng với bệnh nhân suy gan (metabolite qua CYP3A4 và CYP2D6)",
            "Có thể dùng cho trẻ em từ 2 tuổi trở lên",
            "An toàn trong thai kỳ (category B)",
            "Ít tương tác thuốc, an toàn cho hầu hết bệnh nhân",
            "Tác dụng kéo dài 24 giờ nên chỉ cần dùng 1 lần/ngày"
        ],
        "pharmacokinetics": {
            "half_life": "8-28 giờ (desloratadine - metabolite hoạt động có half-life dài hơn)",
            "onset": "1-3 giờ",
            "duration": "24 giờ",
            "protein_binding": "97-99%",
            "clearance": "Gan: chuyển hóa qua CYP3A4 và CYP2D6 thành desloratadine (metabolite hoạt động, mạnh hơn loratadine). Thận: bài tiết một phần nguyên dạng và metabolites."
        },
        "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm, tránh ánh sáng. Viên nén: bảo quản trong bao bì kín. Dạng syrup: bảo quản ở nhiệt độ phòng, đậy kín sau khi dùng.",
        "black_box_warnings": None,
        "drug_interactions": {
            "major": [],
            "moderate": [
                {
                    "drug": "Erythromycin, Ketoconazole, Itraconazole",
                    "mechanism": "Ức chế CYP3A4, giảm chuyển hóa loratadine",
                    "effect": "Tăng nồng độ loratadine và desloratadine",
                    "management": "Thận trọng. Thường không cần điều chỉnh liều nhưng có thể tăng buồn ngủ nhẹ."
                }
            ],
            "minor": []
        },
        "contraindications": {
            "tuyệt_đối": [
                "Dị ứng loratadine hoặc desloratadine"
            ],
            "tương_đối": [
                "Suy gan nặng - thận trọng (giảm chuyển hóa)",
                "Trẻ em <2 tuổi - an toàn từ 2 tuổi trở lên"
            ]
        },
        "pregnancy_lactation": {
            "fda_category": "B",
            "pregnancy_details": "An toàn trong thai kỳ. Không có bằng chứng về dị tật bẩm sinh. Có thể dùng ở tất cả các tam cá nguyệt. Loratadine là một trong những antihistamine được lựa chọn trong thai kỳ.",
            "lactation": {
                "safety": "Compatible",
                "details": "Loratadine bài tiết vào sữa mẹ ở nồng độ thấp. An toàn cho trẻ bú mẹ. Ít báo cáo về tác dụng phụ ở trẻ.",
                "recommendation": "Có thể dùng khi cho con bú. Theo dõi dấu hiệu buồn ngủ ở trẻ (hiếm)."
            }
        },
        "hepatic_adjustment": {
            "mild": "Không đổi",
            "moderate": "Thận trọng, có thể giảm liều nhẹ",
            "severe": "Thận trọng, giảm liều hoặc tránh dùng",
            "notes": "Loratadine chuyển hóa ở gan qua CYP3A4 và CYP2D6 thành desloratadine (metabolite hoạt động). Suy gan có thể làm giảm chuyển hóa, tăng nguy cơ tích lũy."
        },
        "overdose_management": {
            "symptoms": [
                "Buồn ngủ (tăng so với liều điều trị)",
                "Nhức đầu",
                "Khô miệng",
                "Lú lẫn (hiếm)",
                "Tim đập nhanh (hiếm)"
            ],
            "antidote": "Không có antidote đặc hiệu. Điều trị hỗ trợ",
            "treatment": [
                "Rửa dạ dày nếu uống trong vòng 1-2 giờ",
                "Than hoạt tính nếu uống trong vòng 1-2 giờ",
                "Theo dõi ý thức, huyết áp, nhịp tim",
                "Điều trị hỗ trợ: truyền dịch nếu cần",
                "Theo dõi ít nhất 4-6 giờ"
            ],
            "monitoring": "Ý thức, huyết áp, nhịp tim"
        },
        "reversal_agents": {
            "available": False,
            "agents": []
        },
        "administration_instructions": {
            "oral": {
                "with_food": "Có thể dùng với hoặc không có thức ăn. Hấp thu tốt trong cả hai trường hợp",
                "timing": "Dùng 1 lần/ngày (tác dụng kéo dài 24 giờ). Có thể dùng buổi sáng hoặc tối."
            },
            "iv": {
                "reconstitution": "Không có dạng IV",
                "infusion_rate": "N/A",
                "compatibility": [],
                "incompatibility": [],
                "notes": "Chỉ có dạng uống"
            }
        },
        "references": {
            "primary_sources": [
                "FDA Drug Label - Clarityne (loratadine)",
                "UpToDate - Loratadine: Drug information",
                "Allergy & Clinical Immunology guidelines"
            ],
            "last_updated": "2024-12-19",
            "evidence_level": "High - Multiple RCTs and systematic reviews"
        }
    },
    "Cetirizine": {
        "group": "Allergy - Antihistamine (H1 Antagonist, 2nd generation)",
        "vietnamese_name": "Cetirizine, Zyrtec",
        "administration": ["PO"],
        "indications": [
            "Dị ứng (allergic rhinitis)",
            "Mề đay (urticaria)",
            "Dị ứng mắt",
            "Dị ứng da"
        ],
        "contraindications": [
            "Dị ứng",
            "Suy thận nặng"
        ],
        "dosage": {
            "adult_standard": "10mg x 1 lần/ngày",
            "adult_max": "10mg x 2 lần/ngày",
            "pediatric": "5mg x 1 lần/ngày (2-6 tuổi), 10mg/ngày (6-12 tuổi)",
            "notes": "Non-sedating, an toàn cho trẻ em"
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "5mg x 1 lần/ngày",
            "under_30": "5mg cách ngày"
        },
        "side_effects": [
            "Buồn ngủ (ít, 10-15% người)",
            "Khô miệng",
            "Nhức đầu",
            "Mệt mỏi"
        ],
        "interactions": [
            "Ít tương tác",
            "Alcohol: có thể tăng buồn ngủ"
        ],
        "pregnancy": "B",
        "mechanism_of_action": "Cetirizine là metabolite của hydroxyzine, là antihistamine thế hệ thứ hai, đối kháng chọn lọc và có ái lực cao với thụ thể H1 ở ngoại biên. Cetirizine ít qua hàng rào máu-não (do là zwitterion ở pH sinh lý) nên ít gây buồn ngủ hơn so với antihistamine thế hệ thứ nhất, nhưng vẫn có thể gây buồn ngủ ở một số người (10-15%). Cetirizine ức chế phóng thích histamine từ mast cells và basophils, ngăn chặn tác dụng của histamine trên các thụ thể H1. Ngoài ra, cetirizine có tác dụng kháng viêm nhẹ do ức chế phóng thích các chất trung gian gây viêm và ức chế chemotaxis của eosinophils. Tác dụng tốt cho cả allergic rhinitis và urticaria.",
        "monitoring": [
            "Đáp ứng điều trị (giảm triệu chứng dị ứng)",
            "Buồn ngủ (10-15% người dùng, mặc dù là thế hệ thứ hai)",
            "Chức năng thận (creatinine) - cần điều chỉnh liều ở suy thận",
            "Tác dụng phụ (khô miệng, nhức đầu, mệt mỏi)",
            "Tương tác với alcohol (có thể tăng buồn ngủ)"
        ],
        "precautions": [
            "Có thể gây buồn ngủ ở một số người (10-15%) - thận trọng khi lái xe hoặc vận hành máy móc",
            "Cần điều chỉnh liều ở suy thận: CrCl 30-60 → 5mg/ngày, CrCl <30 → 5mg cách ngày",
            "Có thể dùng với thức ăn hoặc không",
            "An toàn cho trẻ em từ 2 tuổi trở lên",
            "An toàn trong thai kỳ (category B)",
            "Tránh dùng với alcohol (tăng buồn ngủ)",
            "Ít tương tác thuốc, an toàn cho hầu hết bệnh nhân",
            "Tác dụng kéo dài 24 giờ nên chỉ cần dùng 1 lần/ngày"
        ],
        "pharmacokinetics": {
            "half_life": "8-10 giờ",
            "onset": "1 giờ",
            "duration": "24 giờ",
            "protein_binding": "93%",
            "clearance": "Thận: bài tiết chủ yếu qua thận (60-70% nguyên dạng, không chuyển hóa). Gan: ít chuyển hóa. Cần điều chỉnh liều ở suy thận."
        },
        "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm, tránh ánh sáng. Viên nén: bảo quản trong bao bì kín. Dạng syrup: bảo quản ở nhiệt độ phòng, đậy kín sau khi dùng.",
        "black_box_warnings": None,
        "drug_interactions": {
            "major": [],
            "moderate": [
                {
                    "drug": "Alcohol",
                    "mechanism": "Tăng tác dụng ức chế hệ thần kinh trung ương",
                    "effect": "Tăng buồn ngủ, suy hô hấp",
                    "management": "Tránh dùng với rượu. Cảnh báo bệnh nhân về nguy cơ."
                }
            ],
            "minor": [
                {
                    "drug": "Theophylline",
                    "mechanism": "Có thể tăng nhẹ nồng độ theophylline",
                    "effect": "Tăng nhẹ tác dụng theophylline",
                    "management": "Thận trọng. Theo dõi nồng độ theophylline nếu cần."
                }
            ]
        },
        "contraindications": {
            "tuyệt_đối": [
                "Dị ứng cetirizine hoặc hydroxyzine",
                "Suy thận nặng (CrCl <30) - chống chỉ định hoặc dùng liều rất thấp"
            ],
            "tương_đối": [
                "Suy thận nhẹ đến trung bình (CrCl 30-60) - giảm liều 50%",
                "Người cao tuổi - có thể tăng nguy cơ buồn ngủ",
                "Bệnh nhân có nguy cơ bí tiểu - tăng nguy cơ"
            ]
        },
        "pregnancy_lactation": {
            "fda_category": "B",
            "pregnancy_details": "An toàn trong thai kỳ. Không có bằng chứng về dị tật bẩm sinh. Có thể dùng ở tất cả các tam cá nguyệt. Cetirizine là một trong những antihistamine được lựa chọn trong thai kỳ.",
            "lactation": {
                "safety": "Compatible",
                "details": "Cetirizine bài tiết vào sữa mẹ ở nồng độ thấp. Nồng độ trong máu trẻ bú mẹ thường <1% nồng độ mẹ. An toàn cho trẻ bú mẹ. Ít báo cáo về tác dụng phụ ở trẻ.",
                "recommendation": "Có thể dùng khi cho con bú. Theo dõi dấu hiệu buồn ngủ ở trẻ (hiếm)."
            }
        },
        "hepatic_adjustment": {
            "mild": "Không đổi",
            "moderate": "Không đổi",
            "severe": "Không đổi",
            "notes": "Cetirizine chủ yếu thải trừ qua thận (không chuyển hóa ở gan), không cần điều chỉnh liều ở suy gan. Tuy nhiên, suy gan nặng có thể ảnh hưởng đến protein binding."
        },
        "overdose_management": {
            "symptoms": [
                "Buồn ngủ (tăng so với liều điều trị)",
                "Nhức đầu",
                "Khô miệng",
                "Lú lẫn (hiếm)",
                "Tim đập nhanh (hiếm)"
            ],
            "antidote": "Không có antidote đặc hiệu. Điều trị hỗ trợ",
            "treatment": [
                "Rửa dạ dày nếu uống trong vòng 1-2 giờ",
                "Than hoạt tính nếu uống trong vòng 1-2 giờ",
                "Theo dõi ý thức, huyết áp, nhịp tim",
                "Điều trị hỗ trợ: truyền dịch nếu cần",
                "Theo dõi ít nhất 4-6 giờ"
            ],
            "monitoring": "Ý thức, huyết áp, nhịp tim"
        },
        "reversal_agents": {
            "available": False,
            "agents": []
        },
        "administration_instructions": {
            "oral": {
                "with_food": "Có thể dùng với hoặc không có thức ăn. Dùng với thức ăn có thể giảm buồn nôn",
                "timing": "Dùng 1 lần/ngày (tác dụng kéo dài 24 giờ). Có thể dùng buổi sáng hoặc tối. CẦN ĐIỀU CHỈNH LIỀU Ở SUY THẬN: CrCl 30-60 → 5mg/ngày, CrCl <30 → 5mg cách ngày."
            },
            "iv": {
                "reconstitution": "Không có dạng IV",
                "infusion_rate": "N/A",
                "compatibility": [],
                "incompatibility": [],
                "notes": "Chỉ có dạng uống"
            }
        },
        "references": {
            "primary_sources": [
                "FDA Drug Label - Zyrtec (cetirizine)",
                "UpToDate - Cetirizine: Drug information",
                "Allergy & Clinical Immunology guidelines"
            ],
            "last_updated": "2024-12-19",
            "evidence_level": "High - Multiple RCTs and systematic reviews"
        }
    },
    "Fexofenadine": {
        "group": "Allergy - Antihistamine (H1 Antagonist, 2nd generation)",
        "vietnamese_name": "Fexofenadine, Allegra",
        "administration": ["PO"],
        "indications": [
            "Dị ứng (allergic rhinitis)",
            "Mề đay (urticaria)",
            "Dị ứng da"
        ],
        "contraindications": [
            "Dị ứng"
        ],
        "dosage": {
            "adult_standard": "180mg x 1 lần/ngày hoặc 60mg x 2 lần/ngày",
            "adult_max": "180mg x 2 lần/ngày",
            "pediatric": "30mg x 2 lần/ngày (6-11 tuổi)",
            "notes": "Non-sedating, ít buồn ngủ nhất"
        },
        "side_effects": [
            "Rất ít tác dụng phụ",
            "Buồn ngủ rất hiếm",
            "Nhức đầu (hiếm)",
            "Mệt mỏi (hiếm)"
        ],
        "interactions": [
            "Fruit juices (apple, orange, grapefruit): giảm hấp thu (cách xa 1-2 giờ)",
            "Antacids: giảm hấp thu (cách xa 2 giờ)"
        ],
        "pregnancy": "C",
        "mechanism_of_action": "Fexofenadine là metabolite hoạt động của terfenadine, là antihistamine thế hệ thứ hai, đối kháng chọn lọc và có ái lực cao với thụ thể H1 ở ngoại biên. Fexofenadine gần như không qua hàng rào máu-não (do là carboxylate anion ở pH sinh lý) nên không gây buồn ngủ và không có tác dụng anticholinergic. Fexofenadine ức chế phóng thích histamine từ mast cells và basophils, ngăn chặn tác dụng của histamine trên các thụ thể H1. Fexofenadine được coi là non-sedating nhất trong các antihistamine thế hệ thứ hai, phù hợp cho bệnh nhân cần tỉnh táo hoàn toàn. Tác dụng tốt cho cả allergic rhinitis và urticaria.",
        "monitoring": [
            "Đáp ứng điều trị (giảm triệu chứng dị ứng)",
            "Tác dụng phụ (rất hiếm: nhức đầu, mệt mỏi)",
            "Tương tác với fruit juices và antacids (giảm hấp thu)",
            "Chức năng thận nếu dùng lâu dài (mặc dù không cần điều chỉnh liều)"
        ],
        "precautions": [
            "Non-sedating nhất - không gây buồn ngủ, an toàn khi lái xe",
            "Không dùng với fruit juices (táo, cam, bưởi) - giảm hấp thu đáng kể, cách xa 1-2 giờ",
            "Không dùng với antacids - giảm hấp thu, cách xa 2 giờ",
            "Uống với nước lọc, không dùng với thức ăn có acid (có thể giảm hấp thu)",
            "Có thể dùng cho trẻ em từ 6 tuổi trở lên",
            "Thận trọng trong thai kỳ (category C) - cân nhắc lợi ích/nguy cơ",
            "Ít tương tác thuốc, an toàn cho hầu hết bệnh nhân",
            "Không cần điều chỉnh liều ở suy thận hoặc suy gan",
            "Tác dụng kéo dài 24 giờ nên chỉ cần dùng 1-2 lần/ngày tùy liều"
        ],
        "pharmacokinetics": {
            "half_life": "14.4 giờ",
            "onset": "1-2 giờ",
            "duration": "24 giờ",
            "protein_binding": "60-70%",
            "clearance": "Thận: bài tiết chủ yếu qua thận (80% nguyên dạng, 11% metabolites). Gan: ít chuyển hóa. Không cần điều chỉnh liều ở suy thận hoặc suy gan (mặc dù có thể tích lũy nhẹ ở suy thận nặng)."
        },
        "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm, tránh ánh sáng. Viên nén: bảo quản trong bao bì kín. Dạng viên nén tan nhanh: bảo quản trong bao bì kín, tránh ẩm.",
        "black_box_warnings": None,
        "drug_interactions": {
            "major": [],
            "moderate": [
                {
                    "drug": "Fruit juices (apple, orange, grapefruit)",
                    "mechanism": "Giảm hấp thu fexofenadine qua transporter",
                    "effect": "Giảm nồng độ fexofenadine, giảm hiệu quả",
                    "management": "KHÔNG dùng với fruit juices. Cách xa ít nhất 1-2 giờ. Uống với nước lọc."
                },
                {
                    "drug": "Antacids (aluminum, magnesium)",
                    "mechanism": "Giảm hấp thu fexofenadine",
                    "effect": "Giảm nồng độ fexofenadine, giảm hiệu quả",
                    "management": "Cách xa ít nhất 2 giờ. Uống với nước lọc."
                }
            ],
            "minor": []
        },
        "contraindications": {
            "tuyệt_đối": [
                "Dị ứng fexofenadine hoặc terfenadine"
            ],
            "tương_đối": [
                "Trẻ em <6 tuổi - an toàn từ 6 tuổi trở lên",
                "Suy thận nặng - có thể tích lũy nhẹ nhưng không cần điều chỉnh liều"
            ]
        },
        "pregnancy_lactation": {
            "fda_category": "C",
            "pregnancy_details": "Dùng được trong thai kỳ nếu lợi ích > nguy cơ. Không có bằng chứng rõ ràng về dị tật bẩm sinh, nhưng ít dữ liệu hơn so với loratadine và cetirizine. Cân nhắc dùng loratadine hoặc cetirizine (category B) nếu có thể.",
            "lactation": {
                "safety": "Compatible",
                "details": "Fexofenadine bài tiết vào sữa mẹ ở nồng độ thấp. An toàn cho trẻ bú mẹ. Ít báo cáo về tác dụng phụ ở trẻ.",
                "recommendation": "Có thể dùng khi cho con bú. Theo dõi dấu hiệu bất thường ở trẻ (hiếm)."
            }
        },
        "hepatic_adjustment": {
            "mild": "Không đổi",
            "moderate": "Không đổi",
            "severe": "Không đổi",
            "notes": "Fexofenadine chủ yếu thải trừ qua thận (ít chuyển hóa ở gan), không cần điều chỉnh liều ở suy gan."
        },
        "overdose_management": {
            "symptoms": [
                "Nhức đầu (tăng so với liều điều trị)",
                "Mệt mỏi",
                "Buồn ngủ (hiếm)",
                "Lú lẫn (rất hiếm)"
            ],
            "antidote": "Không có antidote đặc hiệu. Điều trị hỗ trợ",
            "treatment": [
                "Rửa dạ dày nếu uống trong vòng 1-2 giờ",
                "Than hoạt tính nếu uống trong vòng 1-2 giờ",
                "Theo dõi ý thức, huyết áp, nhịp tim",
                "Điều trị hỗ trợ: truyền dịch nếu cần",
                "Theo dõi ít nhất 4-6 giờ"
            ],
            "monitoring": "Ý thức, huyết áp, nhịp tim"
        },
        "reversal_agents": {
            "available": False,
            "agents": []
        },
        "administration_instructions": {
            "oral": {
                "with_food": "Có thể dùng với hoặc không có thức ăn. Uống với nước lọc. KHÔNG dùng với fruit juices (táo, cam, bưởi) - giảm hấp thu đáng kể",
                "timing": "Dùng 1-2 lần/ngày tùy liều (180mg x 1 lần/ngày hoặc 60mg x 2 lần/ngày). Cách xa fruit juices 1-2 giờ. Cách xa antacids 2 giờ."
            },
            "iv": {
                "reconstitution": "Không có dạng IV",
                "infusion_rate": "N/A",
                "compatibility": [],
                "incompatibility": [],
                "notes": "Chỉ có dạng uống"
            }
        },
        "references": {
            "primary_sources": [
                "FDA Drug Label - Allegra (fexofenadine)",
                "UpToDate - Fexofenadine: Drug information",
                "Allergy & Clinical Immunology guidelines"
            ],
            "last_updated": "2024-12-19",
            "evidence_level": "High - Multiple RCTs and systematic reviews"
        }
    },
    "Desloratadine": {
        "group": "Allergy - Antihistamine (H1 Antagonist, 2nd generation)",
        "vietnamese_name": "Desloratadine, Aerius",
        "administration": ["PO"],
        "indications": [
            "Dị ứng (allergic rhinitis)",
            "Mề đay (urticaria)",
            "Dị ứng da"
        ],
        "contraindications": [
            "Dị ứng"
        ],
        "dosage": {
            "adult_standard": "5mg x 1 lần/ngày",
            "adult_max": "5mg x 2 lần/ngày",
            "pediatric": "2.5mg x 1 lần/ngày (6-11 tuổi)",
            "notes": "Là metabolite của loratadine, mạnh hơn và tác dụng dài hơn"
        },
        "side_effects": [
            "Buồn ngủ (rất hiếm)",
            "Khô miệng",
            "Nhức đầu",
            "Ít tác dụng phụ"
        ],
        "interactions": [
            "Ít tương tác"
        ],
        "pregnancy": "C",
        "mechanism_of_action": "Desloratadine là antihistamine thế hệ 2, là metabolite hoạt động của loratadine. Thuốc ức chế chọn lọc receptor H1 ngoại vi, ngăn cản histamine gắn vào receptor và gây các phản ứng dị ứng (ngứa, hắt hơi, chảy nước mũi, nổi mề đay). Desloratadine không qua hàng rào máu-não (BBB) nên ít gây buồn ngủ hơn so với antihistamine thế hệ 1. Thuốc cũng có tác dụng ức chế giải phóng các chất trung gian gây viêm từ tế bào mast và basophil",
        "monitoring": [
            "Dấu hiệu phản ứng dị ứng (nếu có)",
            "Dấu hiệu buồn ngủ (rất hiếm nhưng cần theo dõi khi lái xe)",
            "Chức năng gan nếu dùng lâu dài"
        ],
        "precautions": [
            "Ít tác dụng phụ, ít gây buồn ngủ hơn antihistamine thế hệ 1",
            "Có thể dùng trong thai kỳ (category C)",
            "Dùng được ở trẻ em từ 6 tháng tuổi",
            "Ít tương tác với các thuốc khác",
            "Có thể dùng với thức ăn hoặc không"
        ],
        "pharmacokinetics": {
            "half_life": "27 giờ (dài)",
            "onset": "1-2 giờ",
            "duration": "24 giờ",
            "protein_binding": "82-87%",
            "clearance": "Gan (chuyển hóa), thận (thải trừ)"
        },
        "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm",
        "black_box_warnings": None,
        "drug_interactions": {
            "major": [],
            "moderate": [],
            "minor": [
                {
                    "drug": "CYP3A4 inhibitors (ketoconazole, itraconazole, erythromycin)",
                    "mechanism": "Có thể ức chế chuyển hóa desloratadine nhẹ.",
                    "effect": "Tăng nhẹ nồng độ desloratadine",
                    "management": "Thận trọng. Thường không cần điều chỉnh liều."
                }
            ]
        },
        "contraindications": {
            "tuyệt_đối": [
                "Dị ứng desloratadine hoặc loratadine"
            ],
            "tương_đối": [
                "Suy gan nặng - thận trọng, có thể cần giảm liều",
                "Có thai - category C, thận trọng",
                "Trẻ em <6 tháng tuổi - không khuyến cáo"
            ]
        },
        "pregnancy_lactation": {
            "fda_category": "C",
            "pregnancy_details": "Desloratadine là category C. Không có nghiên cứu đầy đủ ở phụ nữ có thai. Dùng được nếu lợi ích > nguy cơ. Thận trọng, đặc biệt trong tam cá nguyệt đầu.",
            "lactation": {
                "safety": "Compatible",
                "details": "Desloratadine bài tiết vào sữa mẹ ở nồng độ thấp. An toàn cho trẻ bú mẹ.",
                "recommendation": "Có thể dùng khi cho con bú. An toàn cho trẻ bú mẹ."
            }
        },
        "hepatic_adjustment": {
            "mild": "Không cần điều chỉnh liều. Theo dõi chức năng gan.",
            "moderate": "Thận trọng, có thể cần giảm liều. Theo dõi chức năng gan.",
            "severe": "Thận trọng, giảm liều. Suy gan nặng làm giảm chuyển hóa, có thể tăng nồng độ.",
            "notes": "Desloratadine chuyển hóa ở gan. Suy gan có thể làm giảm chuyển hóa, tăng nồng độ và tác dụng phụ."
        },
        "overdose_management": {
            "symptoms": [
                "Buồn ngủ nặng",
                "Nhức đầu",
                "Khô miệng",
                "Chóng mặt"
            ],
            "antidote": "Không có antidote đặc hiệu. Điều trị hỗ trợ.",
            "treatment": [
                "Ngừng desloratadine ngay lập tức",
                "Theo dõi dấu hiệu sinh tồn",
                "Hỗ trợ hô hấp nếu cần",
                "Theo dõi trong 24-48 giờ (half-life dài)"
            ],
            "monitoring": "Dấu hiệu sinh tồn, mức độ ý thức, dấu hiệu buồn ngủ"
        },
        "reversal_agents": {
            "available": False,
            "agents": []
        },
        "administration_instructions": {
            "oral": {
                "with_food": "Có thể uống với hoặc không thức ăn. Không ảnh hưởng hấp thu.",
                "timing": "Uống 1 lần/ngày, bất kỳ lúc nào, cùng thời điểm mỗi ngày."
            },
            "iv": {
                "reconstitution": "Không có dạng IV",
                "infusion_rate": "N/A",
                "compatibility": [],
                "incompatibility": [],
                "notes": "Chỉ có dạng uống"
            }
        },
        "references": {
            "primary_sources": [
                "FDA Drug Label - Desloratadine (Clarinex)",
                "UpToDate - Desloratadine: Drug Information",
                "Goodman & Gilman's The Pharmacological Basis of Therapeutics (14th ed)"
            ],
            "last_updated": "2025-02-04",
            "evidence_level": "A - Dựa trên FDA drug labels và dữ liệu lâm sàng"
        }
    },
    "Levocetirizine": {
        "group": "Allergy - Antihistamine (H1 Antagonist, 2nd generation)",
        "vietnamese_name": "Levocetirizine, Xyzal",
        "administration": ["PO"],
        "indications": [
            "Dị ứng (allergic rhinitis)",
            "Mề đay (urticaria)",
            "Dị ứng da"
        ],
        "contraindications": [
            "Dị ứng",
            "Suy thận nặng"
        ],
        "dosage": {
            "adult_standard": "5mg x 1 lần/ngày buổi tối",
            "adult_max": "5mg x 2 lần/ngày",
            "pediatric": "2.5mg x 1 lần/ngày (6-12 tuổi)",
            "notes": "Là R-enantiomer của cetirizine, mạnh hơn cetirizine"
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "5mg cách ngày",
            "under_30": "5mg mỗi 3 ngày"
        },
        "side_effects": [
            "Buồn ngủ (ít hơn cetirizine)",
            "Nhức đầu",
            "Mệt mỏi",
            "Khô miệng"
        ],
        "interactions": [
            "Ít tương tác",
            "Alcohol: có thể tăng buồn ngủ"
        ],
        "pregnancy": "B",
        "mechanism_of_action": "Levocetirizine là R-enantiomer của cetirizine, là antihistamine thế hệ 2. Thuốc ức chế chọn lọc receptor H1 ngoại vi, ngăn cản histamine gắn vào receptor và gây các phản ứng dị ứng. Levocetirizine mạnh hơn và tác dụng dài hơn so với cetirizine (racemic mixture). Thuốc không qua hàng rào máu-não (BBB) nên ít gây buồn ngủ hơn so với antihistamine thế hệ 1. Thuốc cũng có tác dụng ức chế giải phóng các chất trung gian gây viêm từ tế bào mast",
        "monitoring": [
            "Dấu hiệu phản ứng dị ứng (nếu có)",
            "Dấu hiệu buồn ngủ (ít hơn cetirizine nhưng cần theo dõi khi lái xe)",
            "Chức năng thận nếu suy thận (cần điều chỉnh liều)",
            "Chức năng gan nếu dùng lâu dài"
        ],
        "precautions": [
            "Giảm liều nếu suy thận (CrCl 30-60: 5mg cách ngày, <30: 5mg mỗi 3 ngày)",
            "Ít gây buồn ngủ hơn cetirizine",
            "Có thể dùng trong thai kỳ (category B)",
            "Dùng được ở trẻ em từ 6 tuổi",
            "Tránh rượu (có thể tăng buồn ngủ)",
            "Có thể dùng với thức ăn hoặc không"
        ],
        "pharmacokinetics": {
            "half_life": "8 giờ",
            "onset": "1 giờ",
            "duration": "24 giờ",
            "protein_binding": "91%",
            "clearance": "Thận (thải trừ chủ yếu - 85%), gan (chuyển hóa - 15%)"
        },
        "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm",
        "black_box_warnings": None,
        "drug_interactions": {
            "major": [],
            "moderate": [
                {
                    "drug": "Alcohol",
                    "mechanism": "Cả hai đều ức chế hệ thần kinh trung ương, tác dụng cộng dồn.",
                    "effect": "Tăng buồn ngủ, giảm khả năng lái xe",
                    "management": "Tránh rượu khi dùng levocetirizine."
                }
            ],
            "minor": []
        },
        "contraindications": {
            "tuyệt_đối": [
                "Dị ứng levocetirizine hoặc cetirizine",
                "Suy thận nặng (CrCl <10) - chống chỉ định"
            ],
            "tương_đối": [
                "Suy thận (CrCl 30-60) - giảm liều (5mg cách ngày)",
                "Suy thận (CrCl 10-30) - giảm liều (5mg mỗi 3 ngày)",
                "Có thai - category B, thận trọng",
                "Trẻ em <6 tuổi - không khuyến cáo"
            ]
        },
        "pregnancy_lactation": {
            "fda_category": "B",
            "pregnancy_details": "Levocetirizine là category B - an toàn hơn category C. Không có bằng chứng về dị tật thai nhi. Có thể dùng trong thai kỳ nếu lợi ích > nguy cơ.",
            "lactation": {
                "safety": "Compatible",
                "details": "Levocetirizine bài tiết vào sữa mẹ ở nồng độ thấp. An toàn cho trẻ bú mẹ.",
                "recommendation": "Có thể dùng khi cho con bú. An toàn cho trẻ bú mẹ."
            }
        },
        "hepatic_adjustment": {
            "mild": "Không cần điều chỉnh liều. Levocetirizine chủ yếu thải qua thận.",
            "moderate": "Không cần điều chỉnh liều. Levocetirizine chủ yếu thải qua thận.",
            "severe": "Không cần điều chỉnh liều. Levocetirizine chủ yếu thải qua thận.",
            "notes": "Levocetirizine chủ yếu thải qua thận (85%), chỉ 15% chuyển hóa ở gan. Suy gan không ảnh hưởng đáng kể đến nồng độ."
        },
        "overdose_management": {
            "symptoms": [
                "Buồn ngủ nặng",
                "Nhức đầu",
                "Mệt mỏi",
                "Khô miệng",
                "Chóng mặt"
            ],
            "antidote": "Không có antidote đặc hiệu. Điều trị hỗ trợ.",
            "treatment": [
                "Ngừng levocetirizine ngay lập tức",
                "Theo dõi dấu hiệu sinh tồn",
                "Hỗ trợ hô hấp nếu cần",
                "Theo dõi trong 24-48 giờ"
            ],
            "monitoring": "Dấu hiệu sinh tồn, mức độ ý thức, dấu hiệu buồn ngủ"
        },
        "reversal_agents": {
            "available": False,
            "agents": []
        },
        "administration_instructions": {
            "oral": {
                "with_food": "Có thể uống với hoặc không thức ăn. Không ảnh hưởng hấp thu.",
                "timing": "Uống 1 lần/ngày buổi tối (để giảm buồn ngủ ban ngày) hoặc bất kỳ lúc nào, cùng thời điểm mỗi ngày. Giảm liều nếu suy thận (CrCl 30-60: 5mg cách ngày, CrCl 10-30: 5mg mỗi 3 ngày)."
            },
            "iv": {
                "reconstitution": "Không có dạng IV",
                "infusion_rate": "N/A",
                "compatibility": [],
                "incompatibility": [],
                "notes": "Chỉ có dạng uống"
            }
        },
        "references": {
            "primary_sources": [
                "FDA Drug Label - Levocetirizine (Xyzal)",
                "UpToDate - Levocetirizine: Drug Information",
                "Goodman & Gilman's The Pharmacological Basis of Therapeutics (14th ed)"
            ],
            "last_updated": "2025-02-04",
            "evidence_level": "A - Dựa trên FDA drug labels và dữ liệu lâm sàng"
        }
    },
"Vitamin D": {
        "group": "Vitamins/Supplements - Vitamin D",
        "vietnamese_name": "Vitamin D, Cholecalciferol (D3), Ergocalciferol (D2)",
        "administration": ["PO"],
        "indications": [
            "Thiếu vitamin D",
            "Còi xương",
            "Loãng xương (kết hợp với calcium)",
            "Dự phòng thiếu vitamin D",
            "Suy giảm chức năng thận (cần dạng hoạt hóa)"
        ],
        "contraindications": [
            "Tăng calci máu",
            "Tăng calci niệu",
            "Sỏi thận calci",
            "Quá liều vitamin D"
        ],
        "dosage": {
            "adult_deficiency": "1,000-2,000 IU x 1 lần/ngày hoặc 50,000 IU x 1 lần/tuần x 8 tuần",
            "adult_maintenance": "600-800 IU x 1 lần/ngày",
            "adult_deficiency_severe": "50,000 IU x 1 lần/tuần x 8 tuần, sau đó 1,500-2,000 IU/ngày",
            "adult_osteoporosis": "800-1,200 IU/ngày (kết hợp với calcium)",
            "notes": "D3 (cholecalciferol) hiệu quả hơn D2. Theo dõi nồng độ 25(OH)D trong máu"
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "Có thể cần dạng hoạt hóa (calcitriol)",
            "under_30": "Dùng calcitriol (dạng hoạt hóa) thay vì vitamin D thường"
        },
        "side_effects": [
            "Tăng calci máu (quá liều)",
            "Tăng calci niệu",
            "Sỏi thận",
            "Buồn nôn, nôn (liều cao)",
            "Táo bón"
        ],
        "interactions": [
            "Calcium: tăng hấp thu calcium",
            "Thiazide diuretics: tăng nguy cơ tăng calci máu",
            "Corticosteroid: giảm hấp thu vitamin D",
            "Cholestyramine: giảm hấp thu vitamin D"
        ],
        "pregnancy": "A - An toàn, cần thiết cho thai kỳ",
        "mechanism_of_action": "Vitamin D là hormone steroid quan trọng cho chuyển hóa calcium và phosphate. Có 2 dạng chính: D2 (ergocalciferol, từ thực vật) và D3 (cholecalciferol, từ ánh sáng mặt trời và động vật). Vitamin D được chuyển hóa thành 25(OH)D ở gan (calcidiol), sau đó thành 1,25(OH)2D (calcitriol) ở thận - đây là dạng hoạt động. Calcitriol gắn với vitamin D receptor (VDR) trong tế bào, kích hoạt biểu hiện gen, dẫn đến: tăng hấp thu calcium và phosphate ở ruột, tăng tái hấp thu calcium ở thận, và tăng giải phóng calcium từ xương (với PTH). Vitamin D cũng có vai trò trong hệ miễn dịch, tăng trưởng tế bào, và điều hòa hormone. Thiếu vitamin D gây còi xương (trẻ em), nhuyễn xương (người lớn), và loãng xương. Vitamin D được tổng hợp ở da nhờ ánh sáng UVB từ mặt trời, hoặc được hấp thu từ thức ăn/bổ sung.",
        "monitoring": [
            "Nồng độ 25(OH)D trong máu (mục tiêu: 30-50 ng/mL hoặc 75-125 nmol/L) - xét nghiệm chính để đánh giá tình trạng vitamin D",
            "Nồng độ calcium trong máu (tăng calci máu có thể xảy ra với quá liều vitamin D)",
            "Nồng độ phosphate trong máu",
            "Nồng độ PTH (parathyroid hormone) - tăng khi thiếu vitamin D",
            "24h calcium niệu (tăng calci niệu có thể xảy ra với quá liều)",
            "Creatinine và eGFR - theo dõi chức năng thận",
            "Dấu hiệu lâm sàng tăng calci máu: buồn nôn, nôn, táo bón, yếu cơ, rối loạn tâm thần, sỏi thận (nếu quá liều)",
            "DEXA scan (mật độ xương) nếu dùng để điều trị loãng xương",
            "Theo dõi đáp ứng điều trị: giảm triệu chứng còi xương/nhuyễn xương, cải thiện mật độ xương"
        ],
        "precautions": [
            "D3 (cholecalciferol) hiệu quả hơn D2 (ergocalciferol) - nên chọn D3 nếu có thể",
            "Kết hợp với calcium để tăng hiệu quả (đặc biệt trong điều trị loãng xương)",
            "Theo dõi nồng độ 25(OH)D định kỳ để điều chỉnh liều (tránh thiếu hoặc quá liều)",
            "Thận trọng ở bệnh nhân suy thận - có thể cần dùng calcitriol (dạng hoạt hóa) thay vì vitamin D thường",
            "Thận trọng ở bệnh nhân có tiền sử sỏi thận calci (tăng calci niệu)",
            "Thận trọng ở bệnh nhân tăng calci máu hoặc tăng calci niệu",
            "Thận trọng với thiazide diuretics (tăng nguy cơ tăng calci máu)",
            "Tránh quá liều - có thể gây tăng calci máu nghiêm trọng, sỏi thận, suy thận",
            "Uống nhiều nước để giảm nguy cơ sỏi thận",
            "Corticosteroid và cholestyramine có thể giảm hấp thu vitamin D",
            "Dùng với thức ăn có chất béo để tăng hấp thu (vitamin D tan trong dầu)"
        ],
        "pharmacokinetics": {
            "half_life": "25(OH)D: 2-3 tuần (dài). 1,25(OH)2D: 4-6 giờ (ngắn)",
            "onset": "Bắt đầu tác dụng sau vài ngày đến vài tuần",
            "duration": "Liên tục khi dùng đều đặn, tác dụng kéo dài do tích lũy",
            "protein_binding": "25(OH)D: gắn với vitamin D-binding protein (DBP). 1,25(OH)2D: gắn với DBP và albumin",
            "clearance": "Gan: chuyển hóa 25(OH)D thành các metabolites không hoạt động. Thận: chuyển hóa 25(OH)D thành 1,25(OH)2D (dưới tác dụng của PTH), và bài tiết các metabolites. Tích lũy trong mô mỡ (dự trữ dài hạn)."
        },
        "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ánh sáng trực tiếp, tránh ẩm. Để nơi khô ráo, tránh xa tầm tay trẻ em. Một số dạng có thể bảo quản trong tủ lạnh (xem hướng dẫn trên nhãn).",
        "black_box_warnings": None,
        "drug_interactions": {
            "major": [
                {
                    "drug": "Thiazide diuretics (Hydrochlorothiazide, Chlorthalidone)",
                    "mechanism": "Thiazide diuretics giảm bài tiết calcium qua thận, kết hợp với vitamin D tăng hấp thu calcium, dẫn đến tăng calci máu.",
                    "effect": "Tăng nguy cơ tăng calci máu nghiêm trọng, sỏi thận, suy thận",
                    "management": "Theo dõi nồng độ calcium trong máu chặt chẽ. Có thể cần giảm liều vitamin D hoặc thiazide. Theo dõi dấu hiệu tăng calci máu."
                }
            ],
            "moderate": [
                {
                    "drug": "Corticosteroid (Prednisone, Dexamethasone)",
                    "mechanism": "Corticosteroid giảm hấp thu calcium ở ruột và tăng bài tiết calcium qua thận, đối kháng với tác dụng của vitamin D.",
                    "effect": "Giảm hiệu quả vitamin D, giảm hấp thu calcium",
                    "management": "Có thể cần tăng liều vitamin D khi dùng corticosteroid. Theo dõi nồng độ calcium và 25(OH)D."
                },
                {
                    "drug": "Cholestyramine, Colestipol, Colesevelam",
                    "mechanism": "Các resin gắn acid mật gắn với vitamin D trong ruột, giảm hấp thu.",
                    "effect": "Giảm hấp thu vitamin D, giảm hiệu quả",
                    "management": "Cách ít nhất 4 giờ giữa vitamin D và resin. Uống vitamin D trước, resin sau."
                }
            ],
            "minor": [
                {
                    "drug": "Calcium supplements",
                    "mechanism": "Vitamin D tăng hấp thu calcium từ ruột.",
                    "effect": "Tăng hấp thu calcium (tác dụng mong muốn khi dùng kết hợp)",
                    "management": "Kết hợp vitamin D và calcium là phổ biến và an toàn. Theo dõi nồng độ calcium để tránh tăng calci máu."
                }
            ]
        },
        "contraindications": {
            "tuyệt_đối": [
                "Tăng calci máu (hypercalcemia) - vitamin D làm nặng thêm",
                "Tăng calci niệu (hypercalciuria) nặng - tăng nguy cơ sỏi thận",
                "Sỏi thận calci đang hoạt động - tăng nguy cơ tái phát",
                "Quá liều vitamin D đang điều trị"
            ],
            "tương_đối": [
                "Suy thận nặng - có thể cần dùng calcitriol (dạng hoạt hóa) thay vì vitamin D thường",
                "Sỏi thận calci (tiền sử) - thận trọng, theo dõi calci niệu",
                "Bệnh sarcoidosis - tăng nhạy cảm với vitamin D, tăng nguy cơ tăng calci máu",
                "Bệnh cường cận giáp (hyperparathyroidism) - có thể làm nặng tăng calci máu",
                "Dùng thiazide diuretics - tăng nguy cơ tăng calci máu"
            ]
        },
        "pregnancy_lactation": {
            "fda_category": "A",
            "pregnancy_details": "Vitamin D an toàn và cần thiết trong thai kỳ. Thiếu vitamin D trong thai kỳ có thể gây còi xương ở trẻ sơ sinh, chậm phát triển xương, và các biến chứng khác. Nhu cầu vitamin D tăng trong thai kỳ. Khuyến cáo: 600-800 IU/ngày trong thai kỳ. Một số phụ nữ có thể cần liều cao hơn nếu thiếu vitamin D. Theo dõi nồng độ 25(OH)D trong thai kỳ.",
            "lactation": {
                "safety": "Compatible",
                "details": "Vitamin D bài tiết vào sữa mẹ ở nồng độ thấp. Vitamin D trong sữa mẹ phụ thuộc vào nồng độ vitamin D của mẹ. Bổ sung vitamin D cho mẹ giúp tăng nồng độ trong sữa mẹ.",
                "recommendation": "Có thể dùng khi cho con bú. Khuyến cáo: 600-800 IU/ngày khi cho con bú. Có thể cần liều cao hơn nếu thiếu vitamin D. Theo dõi nồng độ 25(OH)D của mẹ."
            }
        },
        "hepatic_adjustment": {
            "mild": "Không cần điều chỉnh liều. Vitamin D được chuyển hóa ở gan thành 25(OH)D (calcidiol), nhưng suy gan nhẹ không ảnh hưởng đáng kể.",
            "moderate": "Không cần điều chỉnh liều thường quy. Theo dõi nồng độ 25(OH)D. Chuyển hóa có thể giảm nhẹ ở suy gan trung bình.",
            "severe": "Thận trọng, theo dõi nồng độ 25(OH)D. Chuyển hóa có thể giảm ở suy gan nặng, nhưng thường không cần điều chỉnh liều.",
            "notes": "Vitamin D được chuyển hóa ở gan thành 25(OH)D (calcidiol). Suy gan có thể làm giảm chuyển hóa, nhưng thường không ảnh hưởng đáng kể đến nồng độ 25(OH)D. Theo dõi nồng độ 25(OH)D để đảm bảo đủ vitamin D."
        },
        "overdose_management": {
            "symptoms": [
                "Tăng calci máu (hypercalcemia): buồn nôn, nôn, táo bón, yếu cơ, rối loạn tâm thần, hôn mê",
                "Tăng calci niệu (hypercalciuria): sỏi thận, đau thắt lưng, tiểu máu",
                "Suy thận: do tăng calci máu và sỏi thận",
                "Loạn nhịp tim: do tăng calci máu",
                "Tổn thương thận vĩnh viễn (nếu không điều trị)",
                "Tử vong (trong trường hợp quá liều nghiêm trọng)"
            ],
            "antidote": "Không có antidote đặc hiệu. Điều trị hỗ trợ và giảm calci máu.",
            "treatment": [
                "Ngừng vitamin D ngay lập tức",
                "Ngừng bổ sung calcium nếu đang dùng",
                "Điều trị tăng calci máu:",
                "  - Truyền dịch muối đẳng trương (0.9% NaCl) để tăng bài tiết calcium qua thận",
                "  - Furosemide (lợi tiểu) để tăng bài tiết calcium (sau khi đã bù dịch)",
                "  - Calcitonin (giảm giải phóng calcium từ xương) nếu tăng calci máu nặng",
                "  - Bisphosphonates (pamidronate, zoledronate) nếu tăng calci máu nặng, kháng với điều trị khác",
                "  - Glucocorticoid (prednisone) để giảm hấp thu calcium ở ruột (trong một số trường hợp)",
                "  - Hemodialysis nếu tăng calci máu rất nặng và suy thận",
                "Theo dõi nồng độ calcium trong máu thường xuyên (mỗi 6-12 giờ)",
                "Theo dõi chức năng thận (creatinine, eGFR)",
                "Theo dõi ECG (loạn nhịp tim do tăng calci máu)",
                "Điều trị sỏi thận nếu có",
                "Theo dõi ít nhất 1-2 tuần sau khi ngừng vitamin D (do tích lũy)"
            ],
            "monitoring": "Nồng độ calcium trong máu (ionized và total), phosphate, creatinine, eGFR, ECG, dấu hiệu lâm sàng tăng calci máu. Theo dõi ít nhất 1-2 tuần sau khi ngừng vitamin D."
        },
        "reversal_agents": {
            "available": False,
            "agents": []
        },
        "administration_instructions": {
            "oral": {
                "with_food": "Nên uống với thức ăn có chất béo để tăng hấp thu (vitamin D tan trong dầu). Có thể uống với sữa, dầu ăn, hoặc bữa ăn có chất béo.",
                "timing": "Uống 1 lần/ngày hoặc theo chỉ định. Có thể uống bất kỳ lúc nào trong ngày, nhưng nên uống cùng thời điểm mỗi ngày để dễ nhớ. Với liều cao (50,000 IU/tuần), uống 1 lần/tuần vào cùng ngày mỗi tuần."
            },
            "iv": {
                "reconstitution": "Vitamin D chủ yếu dùng đường uống. Nếu cần dùng IV, có thể dùng calcitriol (dạng hoạt hóa) IV trong một số trường hợp đặc biệt.",
                "infusion_rate": "N/A - chủ yếu dùng đường uống",
                "compatibility": ["N/A"],
                "incompatibility": ["N/A"],
                "notes": "Vitamin D chủ yếu dùng đường uống. Nếu cần dùng IV, cân nhắc dùng calcitriol (dạng hoạt hóa) thay thế."
            }
        },
        "references": {
            "primary_sources": [
                "FDA Drug Label - Vitamin D (Cholecalciferol, Ergocalciferol)",
                "Endocrine Society Clinical Practice Guidelines - Evaluation, Treatment, and Prevention of Vitamin D Deficiency",
                "Institute of Medicine (IOM) - Dietary Reference Intakes for Calcium and Vitamin D",
                "UpToDate - Vitamin D deficiency in adults",
                "Goodman & Gilman's The Pharmacological Basis of Therapeutics (14th ed)"
            ],
            "last_updated": "2025-02-04",
            "evidence_level": "A - Dựa trên FDA drug labels, Endocrine Society guidelines, và dữ liệu lâm sàng từ nhiều nguồn"
        }
    },
    "Vitamin B12": {
        "group": "Vitamins/Supplements - Vitamin B12",
        "vietnamese_name": "Vitamin B12, Cyanocobalamin, Methylcobalamin",
        "administration": ["PO", "IM", "SC"],
        "indications": [
            "Thiếu vitamin B12",
            "Thiếu máu hồng cầu to",
            "Bệnh thần kinh do thiếu B12",
            "Dự phòng thiếu B12",
            "Sau phẫu thuật cắt dạ dày"
        ],
        "contraindications": [
            "Dị ứng vitamin B12/cobalt",
            "Leber's disease (thoái hóa thần kinh thị giác di truyền)"
        ],
        "dosage": {
            "adult_po": "1,000-2,000mcg x 1 lần/ngày",
            "adult_im_loading": "1,000mcg IM mỗi ngày x 1 tuần, sau đó mỗi tuần x 4 tuần",
            "adult_im_maintenance": "1,000mcg IM mỗi tháng",
            "adult_deficiency_severe": "1,000mcg IM mỗi ngày x 1-2 tuần, sau đó mỗi tuần x 4 tuần",
            "notes": "IM cho thiếu máu nặng. PO cho thiếu nhẹ hoặc dự phòng"
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "Không đổi",
            "under_30": "Không đổi"
        },
        "side_effects": [
            "Phản ứng tại chỗ tiêm (IM)",
            "Ban da (hiếm)",
            "Phản ứng dị ứng (hiếm)",
            "Tăng đông máu (liều rất cao)"
        ],
        "interactions": [
            "Acid folic: che dấu thiếu B12",
            "Chloramphenicol: giảm đáp ứng với B12",
            "Metformin: giảm nồng độ B12 (dùng lâu dài)",
            "PPI/H2 blocker: giảm hấp thu B12"
        ],
        "pregnancy": "A - An toàn, cần thiết",
        "mechanism_of_action": "Vitamin B12 (cobalamin) là coenzyme cần thiết cho tổng hợp DNA, methyl transfer, và chuyển hóa homocysteine thành methionine. Vitamin B12 kết hợp với folic acid để tổng hợp DNA, đặc biệt quan trọng cho sự phát triển tế bào hồng cầu. Thiếu B12 gây thiếu máu hồng cầu to (megaloblastic anemia) và tổn thương thần kinh (neuropathy, dementia, myelopathy). Vitamin B12 được hấp thu qua đường tiêu hóa nhờ intrinsic factor (từ dạ dày), sau đó dự trữ trong gan. Thiếu B12 thường do thiếu intrinsic factor (pernicious anemia, cắt dạ dày), thiếu hấp thu (bệnh Crohn, cắt ruột), hoặc thiếu trong chế độ ăn (ăn chay). Vitamin B12 có 2 dạng: cyanocobalamin (tổng hợp) và methylcobalamin (tự nhiên).",
        "monitoring": [
            "Hemoglobin, MCV (mean corpuscular volume) - theo dõi đáp ứng điều trị thiếu máu",
            "Nồng độ B12 trong máu (mục tiêu: >300 pg/mL)",
            "Methylmalonic acid (MMA) - tăng khi thiếu B12",
            "Homocysteine - tăng khi thiếu B12",
            "Dấu hiệu tổn thương thần kinh (tê bì, yếu chân tay, mất trí nhớ)",
            "Đáp ứng điều trị (giảm triệu chứng thiếu máu và thần kinh)"
        ],
        "precautions": [
            "IM cho thiếu máu nặng hoặc thiếu hấp thu (nhanh hơn, hiệu quả hơn PO)",
            "PO cho thiếu nhẹ hoặc dự phòng (cần liều cao hơn)",
            "Thiếu B12 có thể che dấu bởi folic acid - luôn kiểm tra B12 khi thiếu máu",
            "Thiếu B12 không điều trị có thể gây tổn thương thần kinh vĩnh viễn",
            "An toàn trong thai kỳ và cho con bú",
            "Thận trọng ở bệnh nhân Leber's disease (thoái hóa thần kinh thị giác)",
            "Theo dõi đáp ứng điều trị (tăng hemoglobin, giảm triệu chứng thần kinh)",
            "Dùng kèm folic acid khi thiếu máu (nhưng không thay thế B12)"
        ],
        "pharmacokinetics": {
            "half_life": "6 ngày (dự trữ trong gan)",
            "onset": "Vài ngày đến vài tuần (tác dụng tích tụ)",
            "duration": "Dự trữ trong gan kéo dài 3-5 năm",
            "protein_binding": "Gắn với transcobalamin",
            "clearance": "Dự trữ trong gan, thải trừ qua mật và nước tiểu"
        },
        "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ánh sáng, tránh nhiệt độ cao",
        "black_box_warnings": None,
        "drug_interactions": {
            "major": [],
            "moderate": [
                {
                    "drug": "Metformin",
                    "mechanism": "Metformin dùng lâu dài có thể giảm hấp thu vitamin B12 ở ruột, dẫn đến thiếu B12.",
                    "effect": "Giảm nồng độ B12, tăng nguy cơ thiếu B12",
                    "management": "Theo dõi nồng độ B12 định kỳ ở bệnh nhân dùng metformin lâu dài (>2 năm). Bổ sung B12 nếu thiếu."
                },
                {
                    "drug": "PPI (Omeprazole, Pantoprazole), H2 blockers (Ranitidine, Famotidine)",
                    "mechanism": "Giảm acid dạ dày, giảm tách B12 khỏi protein trong thức ăn, giảm hấp thu.",
                    "effect": "Giảm hấp thu B12, tăng nguy cơ thiếu B12",
                    "management": "Theo dõi nồng độ B12 định kỳ ở bệnh nhân dùng PPI/H2 blocker lâu dài (>2 năm). Bổ sung B12 nếu thiếu."
                }
            ],
            "minor": [
                {
                    "drug": "Folic acid",
                    "mechanism": "Folic acid có thể che dấu thiếu B12 (cải thiện thiếu máu nhưng không cải thiện tổn thương thần kinh).",
                    "effect": "Che dấu thiếu B12, dẫn đến tổn thương thần kinh không được điều trị",
                    "management": "Luôn kiểm tra B12 khi thiếu máu. Không dùng folic acid đơn độc mà không kiểm tra B12."
                },
                {
                    "drug": "Chloramphenicol",
                    "mechanism": "Chloramphenicol có thể giảm đáp ứng với B12 trong điều trị thiếu máu.",
                    "effect": "Giảm đáp ứng với B12",
                    "management": "Thận trọng. Theo dõi đáp ứng điều trị thiếu máu."
                }
            ]
        },
        "contraindications": {
            "tuyệt_đối": [
                "Dị ứng vitamin B12 hoặc cobalt",
                "Leber's disease (thoái hóa thần kinh thị giác di truyền) - B12 có thể làm nặng bệnh"
            ],
            "tương_đối": [
                "Thiếu B12 do thiếu intrinsic factor (pernicious anemia) - cần dùng IM, không dùng PO",
                "Thiếu hấp thu ở ruột - cần dùng IM, không dùng PO"
            ]
        },
        "pregnancy_lactation": {
            "fda_category": "A",
            "pregnancy_details": "Vitamin B12 an toàn và cần thiết trong thai kỳ. Thiếu B12 trong thai kỳ có thể gây thiếu máu ở mẹ, chậm phát triển thần kinh ở thai nhi, và các biến chứng khác. Nhu cầu B12 tăng trong thai kỳ. Khuyến cáo: 2.6 mcg/ngày trong thai kỳ. Phụ nữ thiếu B12 cần bổ sung đủ trước và trong thai kỳ.",
            "lactation": {
                "safety": "Compatible",
                "details": "Vitamin B12 bài tiết vào sữa mẹ. Nồng độ B12 trong sữa mẹ phụ thuộc vào nồng độ B12 của mẹ. Thiếu B12 ở mẹ có thể dẫn đến thiếu B12 ở trẻ bú mẹ.",
                "recommendation": "Có thể dùng khi cho con bú. Khuyến cáo: 2.8 mcg/ngày khi cho con bú. Phụ nữ thiếu B12 cần bổ sung đủ để đảm bảo đủ B12 cho trẻ."
            }
        },
        "hepatic_adjustment": {
            "mild": "Không cần điều chỉnh liều. B12 được dự trữ trong gan, nhưng suy gan nhẹ không ảnh hưởng đáng kể.",
            "moderate": "Không cần điều chỉnh liều. B12 được dự trữ trong gan, nhưng suy gan trung bình không ảnh hưởng đáng kể.",
            "severe": "Không cần điều chỉnh liều. B12 được dự trữ trong gan, nhưng suy gan nặng không ảnh hưởng đáng kể đến nồng độ B12.",
            "notes": "Vitamin B12 được dự trữ trong gan. Suy gan không ảnh hưởng đáng kể đến nồng độ B12 trong máu. Tuy nhiên, suy gan có thể ảnh hưởng đến dự trữ B12."
        },
        "overdose_management": {
            "symptoms": [
                "Rất hiếm khi có triệu chứng quá liều (B12 là vitamin tan trong nước, thải trừ qua nước tiểu)",
                "Phản ứng dị ứng (hiếm): phát ban, ngứa, sốc phản vệ",
                "Tăng đông máu (với liều rất cao, hiếm)",
                "Phản ứng tại chỗ tiêm (IM): đau, sưng, đỏ"
            ],
            "antidote": "Không có antidote đặc hiệu. Điều trị hỗ trợ.",
            "treatment": [
                "Ngừng B12 nếu có phản ứng dị ứng",
                "Điều trị phản ứng dị ứng:",
                "  - Antihistamine nếu phản ứng nhẹ",
                "  - Epinephrine nếu sốc phản vệ",
                "  - Corticosteroid nếu phản ứng nặng",
                "Theo dõi dấu hiệu sinh tồn",
                "Điều trị phản ứng tại chỗ tiêm: chườm lạnh, giảm đau"
            ],
            "monitoring": "Dấu hiệu phản ứng dị ứng, dấu hiệu sinh tồn, phản ứng tại chỗ tiêm"
        },
        "reversal_agents": {
            "available": False,
            "agents": []
        },
        "administration_instructions": {
            "oral": {
                "with_food": "Có thể uống với hoặc không thức ăn. Hấp thu tốt trong cả hai trường hợp.",
                "timing": "Uống 1 lần/ngày, bất kỳ lúc nào trong ngày. Uống cùng thời điểm mỗi ngày để dễ nhớ."
            },
            "im": {
                "reconstitution": "Vitamin B12 IM thường có sẵn dạng tiêm sẵn. Không cần pha.",
                "injection_site": "Tiêm bắp (deltoid hoặc gluteal). Xoay vị trí tiêm.",
                "injection_rate": "Tiêm chậm, đều",
                "notes": "IM cho thiếu máu nặng hoặc thiếu hấp thu. Tiêm bắp, xoay vị trí tiêm. Theo dõi phản ứng tại chỗ."
            },
            "sc": {
                "reconstitution": "Vitamin B12 SC thường có sẵn dạng tiêm sẵn. Không cần pha.",
                "injection_site": "Tiêm dưới da (bụng, đùi). Xoay vị trí tiêm.",
                "injection_rate": "Tiêm chậm, đều",
                "notes": "SC có thể dùng thay cho IM. Tiêm dưới da, xoay vị trí tiêm."
            },
            "iv": {
                "reconstitution": "Không khuyến cáo dùng IV thường quy",
                "infusion_rate": "N/A",
                "compatibility": ["N/A"],
                "incompatibility": ["N/A"],
                "notes": "Vitamin B12 chủ yếu dùng PO, IM, hoặc SC. IV chỉ dùng trong trường hợp đặc biệt."
            }
        },
        "references": {
            "primary_sources": [
                "FDA Drug Label - Vitamin B12 (Cyanocobalamin, Methylcobalamin)",
                "UpToDate - Vitamin B12 deficiency",
                "American Society of Hematology Guidelines - Vitamin B12 Deficiency",
                "Goodman & Gilman's The Pharmacological Basis of Therapeutics (14th ed)"
            ],
            "last_updated": "2025-02-04",
            "evidence_level": "A - Dựa trên FDA drug labels, ASH guidelines, và dữ liệu lâm sàng"
        }
    },
    "Folic acid": {
        "group": "Vitamins/Supplements - Folate",
        "vietnamese_name": "Folic acid, Folate, Vitamin B9",
        "administration": ["PO"],
        "indications": [
            "Thiếu acid folic",
            "Thiếu máu hồng cầu to do thiếu folate",
            "Dự phòng dị tật ống thần kinh (có thai)",
            "Dự phòng thiếu máu",
            "Điều trị methotrexate độc tính"
        ],
        "contraindications": [
            "Dị ứng acid folic",
            "Ung thư (trừ khi điều trị thiếu máu do hóa trị)"
        ],
        "dosage": {
            "adult_deficiency": "1-5mg x 1 lần/ngày",
            "adult_pregnancy": "400-800mcg x 1 lần/ngày (bắt đầu trước khi có thai)",
            "adult_maintenance": "400mcg x 1 lần/ngày",
            "adult_methotrexate": "1-5mg x 1 lần/ngày (sau khi dùng methotrexate)",
            "notes": "Uống trước khi có thai ít nhất 1 tháng để dự phòng dị tật ống thần kinh"
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "Không đổi",
            "under_30": "Không đổi"
        },
        "side_effects": [
            "Rất ít tác dụng phụ",
            "Ban da (hiếm)",
            "Phản ứng dị ứng (hiếm)"
        ],
        "interactions": [
            "Methotrexate: giảm hiệu quả methotrexate (trừ khi dùng để điều trị độc tính)",
            "Phenytoin: giảm nồng độ phenytoin",
            "Chloramphenicol: giảm đáp ứng với acid folic",
            "Sulfasalazine: giảm hấp thu acid folic"
        ],
        "pregnancy": "A - An toàn, cần thiết (dự phòng dị tật ống thần kinh)",
        "mechanism_of_action": "Folic acid (folate, vitamin B9) là coenzyme cần thiết cho tổng hợp DNA và RNA, đặc biệt quan trọng trong quá trình phân chia tế bào. Folic acid được chuyển đổi thành tetrahydrofolate (THF), tham gia vào các phản ứng methyl transfer, tổng hợp purine và pyrimidine (các nucleotide của DNA/RNA). Folic acid cần thiết cho sự phát triển bình thường của ống thần kinh trong thai kỳ (tuần 3-4), giúp ngăn ngừa dị tật ống thần kinh (spina bifida, anencephaly). Thiếu folic acid gây thiếu máu hồng cầu to do giảm tổng hợp DNA, dẫn đến tế bào hồng cầu chưa trưởng thành. Folic acid cũng được dùng để giảm độc tính của methotrexate (methotrexate ức chế dihydrofolate reductase, folic acid bổ sung folate).",
        "monitoring": [
            "Hemoglobin, MCV (mean corpuscular volume) - theo dõi đáp ứng điều trị thiếu máu",
            "Nồng độ folate trong máu (nếu cần)",
            "Nồng độ vitamin B12 (thiếu B12 có thể che dấu bởi folic acid)",
            "Đáp ứng điều trị (giảm triệu chứng thiếu máu)",
            "Dấu hiệu dị ứng (hiếm)"
        ],
        "precautions": [
            "Dùng kèm vitamin B12 khi thiếu máu (folic acid có thể che dấu thiếu B12, dẫn đến tổn thương thần kinh)",
            "Với thiếu máu: luôn kiểm tra B12 trước khi dùng folic acid",
            "Dự phòng dị tật ống thần kinh: bắt đầu trước khi có thai 1 tháng, tiếp tục trong 3 tháng đầu",
            "Với methotrexate: dùng 24 giờ sau methotrexate (không dùng cùng lúc)",
            "Liều cao (>1mg/ngày) có thể che dấu thiếu B12",
            "An toàn trong thai kỳ và cho con bú",
            "Hiếm khi có tác dụng phụ",
            "Thận trọng ở bệnh nhân ung thư (folic acid có thể kích thích tế bào ung thư)"
        ],
        "pharmacokinetics": {
            "half_life": "Không áp dụng (vitamin)",
            "onset": "Vài ngày đến vài tuần (tác dụng tích tụ)",
            "duration": "Phụ thuộc vào dự trữ trong cơ thể",
            "protein_binding": "Không đáng kể",
            "clearance": "Thận (thải trừ qua nước tiểu), một phần dự trữ trong gan"
        },
        "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm, tránh ánh sáng",
        "black_box_warnings": None,
        "drug_interactions": {
            "major": [
                {
                    "drug": "Methotrexate",
                    "mechanism": "Folic acid đối kháng với tác dụng của methotrexate (methotrexate ức chế dihydrofolate reductase, folic acid bổ sung folate).",
                    "effect": "Giảm hiệu quả methotrexate trong điều trị ung thư/viêm khớp",
                    "management": "KHÔNG dùng folic acid cùng lúc với methotrexate trong điều trị ung thư/viêm khớp. Chỉ dùng folic acid để điều trị độc tính methotrexate, và phải dùng 24 giờ sau methotrexate."
                }
            ],
            "moderate": [
                {
                    "drug": "Phenytoin",
                    "mechanism": "Folic acid có thể giảm nồng độ phenytoin trong máu.",
                    "effect": "Giảm nồng độ phenytoin, giảm hiệu quả chống động kinh, tăng nguy cơ co giật",
                    "management": "Theo dõi nồng độ phenytoin khi bắt đầu hoặc ngừng folic acid. Có thể cần tăng liều phenytoin."
                },
                {
                    "drug": "Sulfasalazine",
                    "mechanism": "Sulfasalazine giảm hấp thu folic acid ở ruột.",
                    "effect": "Giảm hấp thu folic acid, tăng nguy cơ thiếu folate",
                    "management": "Bổ sung folic acid khi dùng sulfasalazine lâu dài. Theo dõi nồng độ folate."
                }
            ],
            "minor": [
                {
                    "drug": "Chloramphenicol",
                    "mechanism": "Chloramphenicol có thể giảm đáp ứng với folic acid trong điều trị thiếu máu.",
                    "effect": "Giảm đáp ứng với folic acid",
                    "management": "Thận trọng. Theo dõi đáp ứng điều trị thiếu máu."
                },
                {
                    "drug": "Vitamin B12",
                    "mechanism": "Folic acid có thể che dấu thiếu B12 (cải thiện thiếu máu nhưng không cải thiện tổn thương thần kinh).",
                    "effect": "Che dấu thiếu B12, dẫn đến tổn thương thần kinh không được điều trị",
                    "management": "Luôn kiểm tra B12 khi thiếu máu. Không dùng folic acid đơn độc mà không kiểm tra B12."
                }
            ]
        },
        "contraindications": {
            "tuyệt_đối": [
                "Dị ứng folic acid",
                "Ung thư đang điều trị bằng methotrexate (trừ khi dùng để điều trị độc tính methotrexate)"
            ],
            "tương_đối": [
                "Ung thư (không điều trị) - folic acid có thể kích thích tế bào ung thư",
                "Thiếu B12 chưa được điều trị - folic acid có thể che dấu thiếu B12"
            ]
        },
        "pregnancy_lactation": {
            "fda_category": "A",
            "pregnancy_details": "Folic acid an toàn và cần thiết trong thai kỳ, đặc biệt quan trọng để dự phòng dị tật ống thần kinh (spina bifida, anencephaly). Dị tật ống thần kinh xảy ra trong tuần 3-4 của thai kỳ, trước khi nhiều phụ nữ biết mình có thai. Do đó, phụ nữ trong độ tuổi sinh đẻ nên bổ sung folic acid trước khi có thai. Khuyến cáo: 400-800 mcg/ngày trước và trong 3 tháng đầu thai kỳ. Phụ nữ có tiền sử dị tật ống thần kinh hoặc dùng một số thuốc (valproate, carbamazepine) cần liều cao hơn (4-5 mg/ngày).",
            "lactation": {
                "safety": "Compatible",
                "details": "Folic acid bài tiết vào sữa mẹ. Nồng độ folic acid trong sữa mẹ phụ thuộc vào nồng độ folic acid của mẹ. Bổ sung folic acid cho mẹ giúp tăng nồng độ trong sữa mẹ.",
                "recommendation": "Có thể dùng khi cho con bú. Khuyến cáo: 500 mcg/ngày khi cho con bú. Phụ nữ thiếu folate cần bổ sung đủ để đảm bảo đủ folate cho trẻ."
            }
        },
        "hepatic_adjustment": {
            "mild": "Không cần điều chỉnh liều. Folic acid chủ yếu thải trừ qua thận, không chuyển hóa ở gan.",
            "moderate": "Không cần điều chỉnh liều. Folic acid chủ yếu thải trừ qua thận, không chuyển hóa ở gan.",
            "severe": "Không cần điều chỉnh liều. Folic acid chủ yếu thải trừ qua thận, không chuyển hóa ở gan.",
            "notes": "Folic acid chủ yếu thải trừ qua thận, một phần dự trữ trong gan. Suy gan không ảnh hưởng đáng kể đến nồng độ folic acid."
        },
        "overdose_management": {
            "symptoms": [
                "Rất hiếm khi có triệu chứng quá liều (folic acid là vitamin tan trong nước, thải trừ qua nước tiểu)",
                "Phản ứng dị ứng (hiếm): phát ban, ngứa",
                "Che dấu thiếu B12 (với liều cao >1mg/ngày) - cải thiện thiếu máu nhưng không cải thiện tổn thương thần kinh"
            ],
            "antidote": "Không có antidote đặc hiệu. Điều trị hỗ trợ.",
            "treatment": [
                "Ngừng folic acid nếu có phản ứng dị ứng",
                "Điều trị phản ứng dị ứng: antihistamine nếu cần",
                "Kiểm tra B12 nếu nghi ngờ che dấu thiếu B12",
                "Theo dõi dấu hiệu sinh tồn"
            ],
            "monitoring": "Dấu hiệu phản ứng dị ứng, nồng độ B12 nếu nghi ngờ che dấu thiếu B12"
        },
        "reversal_agents": {
            "available": False,
            "agents": []
        },
        "administration_instructions": {
            "oral": {
                "with_food": "Có thể uống với hoặc không thức ăn. Hấp thu tốt trong cả hai trường hợp.",
                "timing": "Uống 1 lần/ngày, bất kỳ lúc nào trong ngày. Uống cùng thời điểm mỗi ngày để dễ nhớ. Với methotrexate: dùng 24 giờ sau methotrexate (không dùng cùng lúc)."
            },
            "iv": {
                "reconstitution": "Folic acid chủ yếu dùng đường uống. IV chỉ dùng trong trường hợp đặc biệt.",
                "infusion_rate": "N/A - chủ yếu dùng đường uống",
                "compatibility": ["N/A"],
                "incompatibility": ["N/A"],
                "notes": "Folic acid chủ yếu dùng đường uống. IV chỉ dùng trong trường hợp đặc biệt."
            }
        },
        "references": {
            "primary_sources": [
                "FDA Drug Label - Folic Acid (Folate)",
                "CDC Guidelines - Folic Acid for Prevention of Neural Tube Defects",
                "American College of Obstetricians and Gynecologists (ACOG) - Folic Acid Supplementation",
                "UpToDate - Folic acid deficiency",
                "Goodman & Gilman's The Pharmacological Basis of Therapeutics (14th ed)"
            ],
            "last_updated": "2025-02-04",
            "evidence_level": "A - Dựa trên FDA drug labels, CDC/ACOG guidelines, và dữ liệu lâm sàng"
        }
    },
    "Iron": {
        "group": "Vitamins/Supplements - Iron",
        "vietnamese_name": "Iron, Ferrous sulfate, Ferrous fumarate, Ferrous gluconate",
        "administration": ["PO", "IV", "IM"],
        "indications": [
            "Thiếu máu thiếu sắt",
            "Dự phòng thiếu sắt",
            "Có thai (dự phòng)",
            "Chảy máu mạn tính",
            "Sau phẫu thuật"
        ],
        "contraindications": [
            "Thừa sắt (hemochromatosis)",
            "Thiếu máu không do thiếu sắt",
            "Viêm loét dạ dày tá tràng nặng",
            "Viêm ruột"
        ],
        "dosage": {
            "adult_po_ferrous_sulfate": "325mg (65mg sắt nguyên tố) x 1-3 lần/ngày",
            "adult_po_ferrous_fumarate": "200mg (66mg sắt nguyên tố) x 2-3 lần/ngày",
            "adult_po_ferrous_gluconate": "300mg (35mg sắt nguyên tố) x 3 lần/ngày",
            "adult_pregnancy": "30-60mg sắt nguyên tố/ngày",
            "adult_iv": "100-200mg IV mỗi ngày hoặc theo phác đồ",
            "notes": "Uống khi bụng đói (1 giờ trước bữa ăn) để tăng hấp thu. Uống với vitamin C"
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "Không đổi",
            "under_30": "Thận trọng (tăng nguy cơ tích tụ sắt)"
        },
        "side_effects": [
            "Táo bón",
            "Phân đen (không nguy hiểm)",
            "Buồn nôn, nôn",
            "Đau bụng",
            "Tiêu chảy",
            "Kích ứng dạ dày",
            "Phản ứng dị ứng (IV)",
            "Quá tải sắt (dùng lâu dài, liều cao)"
        ],
        "interactions": [
            "Antacid/PPI/H2 blocker: giảm hấp thu sắt",
            "Tetracycline/Quinolone: giảm hấp thu cả hai",
            "Thyroxine: giảm hấp thu thyroxine",
            "Chloramphenicol: giảm đáp ứng với sắt",
            "Vitamin C: tăng hấp thu sắt"
        ],
        "pregnancy": "A - An toàn, cần thiết",
        "mechanism_of_action": "Sắt (iron) là nguyên tố vi lượng cần thiết cho tổng hợp hemoglobin, myoglobin, và các enzyme chứa sắt. Sắt được hấp thu ở tá tràng và phần trên ruột non, chuyển hóa thành ferritin (dự trữ) và transferrin (vận chuyển). Sắt tham gia vào chuỗi hô hấp tế bào, tổng hợp DNA, và nhiều phản ứng enzyme. Thiếu sắt gây thiếu máu thiếu sắt (iron deficiency anemia), đặc trưng bởi hồng cầu nhỏ, nhược sắc (microcytic, hypochromic). Sắt có nhiều dạng: ferrous sulfate (65mg sắt nguyên tố/325mg), ferrous fumarate (66mg sắt nguyên tố/200mg), ferrous gluconate (35mg sắt nguyên tố/300mg). Hấp thu sắt tăng khi bụng đói và khi dùng với vitamin C.",
        "monitoring": [
            "Hemoglobin (Hb) - mục tiêu: tăng 1-2g/dL mỗi tháng",
            "Ferritin - dự trữ sắt (mục tiêu: >50 ng/mL)",
            "TIBC (total iron binding capacity), transferrin saturation",
            "MCV (mean corpuscular volume) - tăng khi điều trị thành công",
            "Đáp ứng điều trị (giảm mệt mỏi, tăng năng lượng)",
            "Dấu hiệu quá tải sắt (nếu dùng lâu dài, liều cao)"
        ],
        "precautions": [
            "Uống khi bụng đói (1 giờ trước bữa ăn) để tăng hấp thu (có thể gây kích ứng dạ dày)",
            "Nếu kích ứng dạ dày: uống với thức ăn (giảm hấp thu 50%)",
            "Uống với vitamin C (tăng hấp thu sắt)",
            "Tránh uống với antacid, PPI, H2 blocker (giảm hấp thu)",
            "Cách xa tetracycline, quinolone ít nhất 2 giờ (giảm hấp thu cả hai)",
            "Phân đen là bình thường (không phải chảy máu)",
            "Táo bón là tác dụng phụ phổ biến (uống nhiều nước, ăn nhiều chất xơ)",
            "Thận trọng ở bệnh nhân hemochromatosis (thừa sắt)",
            "IV cho thiếu máu nặng hoặc không dung nạp PO (có thể gây phản ứng dị ứng nặng)",
            "Tiếp tục điều trị 3-6 tháng sau khi hemoglobin bình thường (để bổ sung dự trữ)"
        ],
        "pharmacokinetics": {
            "half_life": "Không áp dụng (khoáng chất)",
            "onset": "Vài ngày đến vài tuần (tác dụng tích tụ)",
            "duration": "Phụ thuộc vào dự trữ trong cơ thể",
            "protein_binding": "Gắn với transferrin (vận chuyển) và ferritin (dự trữ)",
            "clearance": "Dự trữ trong gan, lách, tủy xương; thải trừ qua phân, mồ hôi, nước tiểu (ít)"
        },
        "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm, tránh ánh sáng",
        "black_box_warnings": "Quá tải sắt có thể gây tổn thương gan, tim, và các cơ quan khác. Tránh dùng ở bệnh nhân hemochromatosis",
        "drug_interactions": {
            "major": [
                {
                    "drug": "Tetracycline, Doxycycline, Minocycline",
                    "mechanism": "Sắt gắn với tetracycline trong ruột, tạo phức hợp không hấp thu được, giảm hấp thu cả hai.",
                    "effect": "Giảm hấp thu cả sắt và tetracycline, giảm hiệu quả điều trị",
                    "management": "Cách ít nhất 2-3 giờ giữa sắt và tetracycline. Uống sắt trước, tetracycline sau."
                },
                {
                    "drug": "Quinolone (Ciprofloxacin, Levofloxacin, Moxifloxacin)",
                    "mechanism": "Sắt gắn với quinolone trong ruột, tạo phức hợp không hấp thu được, giảm hấp thu cả hai.",
                    "effect": "Giảm hấp thu cả sắt và quinolone, giảm hiệu quả điều trị",
                    "management": "Cách ít nhất 2-3 giờ giữa sắt và quinolone. Uống sắt trước, quinolone sau."
                }
            ],
            "moderate": [
                {
                    "drug": "Levothyroxine",
                    "mechanism": "Sắt gắn với levothyroxine trong ruột, giảm hấp thu levothyroxine.",
                    "effect": "Giảm hấp thu levothyroxine, giảm hiệu quả điều trị suy giáp",
                    "management": "Cách ít nhất 4 giờ giữa sắt và levothyroxine. Uống levothyroxine sáng đói, sắt sau bữa ăn."
                },
                {
                    "drug": "Antacid, PPI (Omeprazole, Pantoprazole), H2 blockers (Ranitidine)",
                    "mechanism": "Giảm acid dạ dày, giảm hấp thu sắt (sắt cần acid để hấp thu tốt).",
                    "effect": "Giảm hấp thu sắt, giảm hiệu quả điều trị thiếu máu",
                    "management": "Cách ít nhất 2 giờ giữa sắt và antacid/PPI/H2 blocker. Uống sắt khi bụng đói (nếu dung nạp), antacid sau bữa ăn."
                }
            ],
            "minor": [
                {
                    "drug": "Vitamin C (Ascorbic acid)",
                    "mechanism": "Vitamin C tăng hấp thu sắt bằng cách khử Fe3+ thành Fe2+ (dạng hấp thu tốt hơn).",
                    "effect": "Tăng hấp thu sắt (tác dụng mong muốn)",
                    "management": "Kết hợp sắt và vitamin C là phổ biến và có lợi. Uống cùng lúc hoặc gần nhau."
                },
                {
                    "drug": "Chloramphenicol",
                    "mechanism": "Chloramphenicol có thể giảm đáp ứng với sắt trong điều trị thiếu máu.",
                    "effect": "Giảm đáp ứng với sắt",
                    "management": "Thận trọng. Theo dõi đáp ứng điều trị thiếu máu."
                }
            ]
        },
        "contraindications": {
            "tuyệt_đối": [
                "Hemochromatosis (thừa sắt di truyền) - sắt làm nặng thêm",
                "Thiếu máu không do thiếu sắt - không hiệu quả và có thể gây quá tải sắt",
                "Dị ứng sắt"
            ],
            "tương_đối": [
                "Viêm loét dạ dày tá tràng nặng - sắt có thể gây kích ứng",
                "Viêm ruột (Crohn, viêm loét đại tràng) - sắt có thể gây kích ứng",
                "Suy thận nặng - tăng nguy cơ tích tụ sắt",
                "Đang truyền máu thường xuyên - tăng nguy cơ quá tải sắt"
            ]
        },
        "pregnancy_lactation": {
            "fda_category": "A",
            "pregnancy_details": "Sắt an toàn và cần thiết trong thai kỳ. Thiếu sắt trong thai kỳ có thể gây thiếu máu ở mẹ, sinh non, nhẹ cân, và các biến chứng khác. Nhu cầu sắt tăng trong thai kỳ. Khuyến cáo: 30-60 mg sắt nguyên tố/ngày trong thai kỳ. Phụ nữ thiếu máu thiếu sắt cần liều cao hơn. Theo dõi hemoglobin và ferritin trong thai kỳ.",
            "lactation": {
                "safety": "Compatible",
                "details": "Sắt bài tiết vào sữa mẹ ở nồng độ thấp. Nồng độ sắt trong sữa mẹ tương đối ổn định và không phụ thuộc nhiều vào nồng độ sắt của mẹ. Tuy nhiên, thiếu sắt ở mẹ có thể ảnh hưởng đến sức khỏe mẹ.",
                "recommendation": "Có thể dùng khi cho con bú. Khuyến cáo: 15-30 mg sắt nguyên tố/ngày khi cho con bú. Phụ nữ thiếu máu thiếu sắt cần liều cao hơn."
            }
        },
        "hepatic_adjustment": {
            "mild": "Không cần điều chỉnh liều. Sắt được dự trữ trong gan, nhưng suy gan nhẹ không ảnh hưởng đáng kể.",
            "moderate": "Thận trọng, theo dõi ferritin. Sắt được dự trữ trong gan, suy gan trung bình có thể ảnh hưởng đến dự trữ.",
            "severe": "Thận trọng, theo dõi ferritin chặt chẽ. Suy gan nặng có thể ảnh hưởng đến dự trữ sắt và tăng nguy cơ quá tải sắt.",
            "notes": "Sắt được dự trữ trong gan dưới dạng ferritin. Suy gan có thể ảnh hưởng đến dự trữ sắt. Theo dõi ferritin để tránh quá tải sắt."
        },
        "overdose_management": {
            "symptoms": [
                "Quá liều cấp tính (thường ở trẻ em):",
                "  - Buồn nôn, nôn (có thể có máu)",
                "  - Đau bụng, tiêu chảy (có thể có máu)",
                "  - Mệt mỏi, yếu cơ",
                "  - Sốc, hạ huyết áp",
                "  - Tổn thương gan (tăng ALT/AST, vàng da)",
                "  - Tổn thương thận (suy thận cấp)",
                "  - Rối loạn đông máu",
                "  - Hôn mê, tử vong (với liều rất cao)",
                "Quá tải sắt mạn tính (hemosiderosis, hemochromatosis):",
                "  - Tổn thương gan (xơ gan, suy gan)",
                "  - Tổn thương tim (suy tim, loạn nhịp)",
                "  - Tổn thương tụy (đái tháo đường)",
                "  - Tổn thương khớp (viêm khớp)",
                "  - Tăng sắc tố da (da xám, đồng)"
            ],
            "antidote": "Deferoxamine (Desferal) - chelate sắt, tăng bài tiết qua nước tiểu. Deferasirox (Exjade) - chelate sắt đường uống.",
            "treatment": [
                "Quá liều cấp tính:",
                "  - Rửa dạ dày nếu uống trong vòng 1-2 giờ",
                "  - Than hoạt tính KHÔNG hiệu quả với sắt (không dùng)",
                "  - Deferoxamine IV: 15 mg/kg/giờ (tối đa 6g/24h) nếu nồng độ sắt >350 mcg/dL hoặc có triệu chứng nặng",
                "  - Deferoxamine IM: 1g mỗi 4-6 giờ (nếu không thể IV)",
                "  - Theo dõi nồng độ sắt trong máu, ferritin",
                "  - Điều trị hỗ trợ: truyền dịch, điều chỉnh điện giải, hỗ trợ gan/thận",
                "  - Theo dõi dấu hiệu sinh tồn, chức năng gan/thận",
                "Quá tải sắt mạn tính:",
                "  - Ngừng bổ sung sắt",
                "  - Deferoxamine hoặc deferasirox để giảm dự trữ sắt",
                "  - Phlebotomy (lấy máu) nếu hemochromatosis",
                "  - Điều trị tổn thương cơ quan (gan, tim, tụy)"
            ],
            "monitoring": "Nồng độ sắt trong máu, ferritin, TIBC, transferrin saturation, chức năng gan (ALT/AST, bilirubin), chức năng thận (creatinine, eGFR), dấu hiệu sinh tồn, ECG (nếu quá tải sắt nặng)."
        },
        "reversal_agents": {
            "available": True,
            "agents": [
                {
                    "name": "Deferoxamine (Desferal)",
                    "mechanism": "Chelate sắt, tạo phức hợp sắt-deferoxamine, tăng bài tiết qua nước tiểu.",
                    "indication": "Quá liều sắt cấp tính hoặc quá tải sắt mạn tính",
                    "dose": "IV: 15 mg/kg/giờ (tối đa 6g/24h). IM: 1g mỗi 4-6 giờ.",
                    "notes": "Deferoxamine là antidote chính cho quá liều sắt. Bắt đầu sớm nếu có triệu chứng nặng hoặc nồng độ sắt cao."
                },
                {
                    "name": "Deferasirox (Exjade)",
                    "mechanism": "Chelate sắt đường uống, tăng bài tiết qua phân.",
                    "indication": "Quá tải sắt mạn tính",
                    "dose": "Theo chỉ định, thường 20-30 mg/kg/ngày",
                    "notes": "Dùng cho quá tải sắt mạn tính, không dùng cho quá liều cấp tính."
                }
            ]
        },
        "administration_instructions": {
            "oral": {
                "with_food": "Nên uống khi bụng đói (1 giờ trước bữa ăn) để tăng hấp thu. Nếu kích ứng dạ dày, có thể uống với thức ăn (giảm hấp thu 50%). Uống với vitamin C (nước cam, viên vitamin C) để tăng hấp thu.",
                "timing": "Uống 1-3 lần/ngày tùy liều. Uống khi bụng đói (1 giờ trước bữa ăn) để tăng hấp thu. Cách xa các thuốc khác ít nhất 2-4 giờ: tetracycline, quinolone (2-3 giờ), levothyroxine (4 giờ), antacid/PPI/H2 blocker (2 giờ)."
            },
            "iv": {
                "reconstitution": "Pha với nước muối đẳng trương (0.9% NaCl). Không pha với các dung dịch khác.",
                "infusion_rate": "Truyền chậm trong ít nhất 1 giờ. Không truyền nhanh (tăng nguy cơ phản ứng dị ứng).",
                "compatibility": ["Normal saline (0.9% NaCl)"],
                "incompatibility": ["Không trộn với các thuốc khác"],
                "notes": "IV cho thiếu máu nặng hoặc không dung nạp PO. Có thể gây phản ứng dị ứng nặng (sốc phản vệ). Theo dõi chặt chẽ trong 30 phút đầu. Test dose trước khi truyền đầy đủ."
            },
            "im": {
                "reconstitution": "Sắt IM thường có sẵn dạng tiêm sẵn. Không cần pha.",
                "injection_site": "Tiêm bắp sâu (gluteal). Xoay vị trí tiêm.",
                "injection_rate": "Tiêm chậm, đều",
                "notes": "IM ít dùng hơn IV. Tiêm bắp sâu, xoay vị trí tiêm. Có thể gây đau và đổi màu da tại chỗ tiêm."
            }
        },
        "references": {
            "primary_sources": [
                "FDA Drug Label - Iron (Ferrous sulfate, Ferrous fumarate, Ferrous gluconate)",
                "American Society of Hematology Guidelines - Iron Deficiency Anemia",
                "WHO Guidelines - Iron Supplementation in Pregnancy",
                "UpToDate - Iron deficiency anemia treatment",
                "Goodman & Gilman's The Pharmacological Basis of Therapeutics (14th ed)"
            ],
            "last_updated": "2025-02-04",
            "evidence_level": "A - Dựa trên FDA drug labels, ASH/WHO guidelines, và dữ liệu lâm sàng"
        }
    },
    "Calcium": {
        "group": "Vitamins/Supplements - Calcium",
        "vietnamese_name": "Calcium, Calcium carbonate, Calcium citrate",
        "administration": ["PO"],
        "indications": [
            "Thiếu calci",
            "Loãng xương (kết hợp với vitamin D)",
            "Hạ calci máu",
            "Dự phòng loãng xương",
            "Có thai, cho con bú"
        ],
        "contraindications": [
            "Tăng calci máu",
            "Tăng calci niệu",
            "Sỏi thận calci",
            "Suy thận nặng",
            "Suy tim (calcium carbonate)"
        ],
        "dosage": {
            "adult_daily_requirement": "1,000-1,200mg nguyên tố calci/ngày",
            "adult_calcium_carbonate": "500-1,000mg x 2-3 lần/ngày (40% nguyên tố calci)",
            "adult_calcium_citrate": "500-1,000mg x 2-3 lần/ngày (21% nguyên tố calci)",
            "adult_hypocalcemia": "1-2g nguyên tố calci/ngày chia 2-3 lần",
            "adult_osteoporosis": "1,000-1,200mg nguyên tố calci/ngày (với vitamin D)",
            "notes": "Calcium citrate hấp thu tốt hơn, không cần acid dạ dày. Uống với thức ăn"
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "Thận trọng, giảm liều",
            "under_30": "Tránh dùng hoặc giảm liều (tăng nguy cơ tăng calci máu)"
        },
        "side_effects": [
            "Táo bón",
            "Đầy hơi",
            "Buồn nôn",
            "Tăng calci máu (quá liều)",
            "Sỏi thận (quá liều)",
            "Giảm hấp thu sắt, kẽm"
        ],
        "interactions": [
            "Sắt: giảm hấp thu sắt - cách 2 giờ",
            "Tetracycline/Quinolone: giảm hấp thu kháng sinh - cách 2 giờ",
            "Thyroxine: giảm hấp thu thyroxine - cách 4 giờ",
            "Digoxin: tăng nguy cơ loạn nhịp",
            "Thiazide diuretics: tăng nguy cơ tăng calci máu",
            "Vitamin D: tăng hấp thu calci"
        ],
        "pregnancy": "A - An toàn, cần thiết",
        "mechanism_of_action": "Calcium là khoáng chất thiết yếu cho nhiều chức năng sinh học. Trong xương: calcium là thành phần chính của hydroxyapatite, tạo cấu trúc và độ bền của xương. Trong máu: calcium ion (Ca2+) tham gia vào quá trình đông máu (cần thiết cho cascade đông máu), co cơ (bao gồm cơ tim và cơ trơn), dẫn truyền thần kinh, và giải phóng hormone. Calcium được hấp thu ở ruột non (chủ yếu ở tá tràng) nhờ vitamin D (calcitriol) và parathyroid hormone (PTH). Hấp thu phụ thuộc vào dạng muối: calcium citrate hấp thu tốt hơn calcium carbonate vì không cần acid dạ dày. Nồng độ calcium trong máu được điều hòa chặt chẽ bởi PTH, calcitonin, và vitamin D thông qua hấp thu ở ruột, tái hấp thu ở thận, và giải phóng từ xương.",
        "monitoring": [
            "Nồng độ calcium trong máu (ionized calcium hoặc total calcium với albumin) - theo dõi tăng calci máu",
            "Nồng độ phosphate trong máu (tăng calci máu có thể kèm hạ phosphate)",
            "Creatinine và eGFR - theo dõi chức năng thận (quan trọng vì tăng calci máu có thể gây suy thận)",
            "Nồng độ PTH (parathyroid hormone) nếu có triệu chứng tăng calci máu",
            "25(OH)D và 1,25(OH)2D nếu nghi ngờ liên quan đến vitamin D",
            "Dấu hiệu lâm sàng tăng calci máu: buồn nôn, nôn, táo bón, yếu cơ, rối loạn tâm thần, sỏi thận",
            "DEXA scan (mật độ xương) nếu dùng để điều trị loãng xương",
            "Sỏi thận (siêu âm) nếu có triệu chứng hoặc dùng liều cao"
        ],
        "precautions": [
            "Uống với thức ăn để tăng hấp thu và giảm tác dụng phụ",
            "Chia liều (không uống quá 500-600mg nguyên tố calci mỗi lần) để tăng hấp thu",
            "Calcium citrate hấp thu tốt hơn calcium carbonate, đặc biệt ở người già hoặc dùng PPI (không cần acid dạ dày)",
            "Cách xa các thuốc khác ít nhất 2 giờ: sắt, tetracycline, quinolone, thyroxine (giảm hấp thu)",
            "Thận trọng ở bệnh nhân suy thận (tăng nguy cơ tăng calci máu, sỏi thận)",
            "Thận trọng ở bệnh nhân có tiền sử sỏi thận calci (tăng calci niệu)",
            "Thận trọng ở bệnh nhân suy tim (calcium carbonate có thể gây đầy hơi, táo bón)",
            "Kết hợp với vitamin D để tăng hấp thu và hiệu quả (đặc biệt trong điều trị loãng xương)",
            "Uống nhiều nước để giảm nguy cơ sỏi thận",
            "Theo dõi triệu chứng tăng calci máu: buồn nôn, nôn, táo bón, yếu cơ"
        ],
        "pharmacokinetics": {
            "half_life": "Không áp dụng (calcium là khoáng chất, không có half-life như thuốc)",
            "onset": "Bắt đầu tác dụng sau vài giờ đến vài ngày",
            "duration": "Liên tục khi dùng đều đặn",
            "protein_binding": "Khoảng 40-50% calcium trong máu gắn với albumin, phần còn lại là ionized (Ca2+) - dạng hoạt động",
            "clearance": "Thận: bài tiết qua nước tiểu (tái hấp thu ở ống thận dưới tác dụng của PTH). Xương: lưu trữ dài hạn. Ruột: bài tiết qua phân (phần không hấp thu)."
        },
        "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm, tránh ánh sáng trực tiếp. Để nơi khô ráo, tránh xa tầm tay trẻ em.",
        "black_box_warnings": None,
        "drug_interactions": {
            "major": [
                {
                    "drug": "Levothyroxine",
                    "mechanism": "Calcium gắn với levothyroxine trong ruột, tạo phức hợp không hấp thu được, giảm hấp thu levothyroxine.",
                    "effect": "Giảm hấp thu levothyroxine 30-50%, giảm hiệu quả điều trị suy giáp",
                    "management": "Cách ít nhất 4 giờ giữa calcium và levothyroxine. Uống levothyroxine sáng đói, calcium sau bữa ăn."
                },
                {
                    "drug": "Tetracycline, Doxycycline, Minocycline",
                    "mechanism": "Calcium gắn với tetracycline trong ruột, tạo phức hợp không hấp thu được, giảm hấp thu cả hai.",
                    "effect": "Giảm hấp thu cả calcium và tetracycline, giảm hiệu quả điều trị",
                    "management": "Cách ít nhất 2 giờ giữa calcium và tetracycline. Uống calcium trước, tetracycline sau."
                },
                {
                    "drug": "Quinolone (Ciprofloxacin, Levofloxacin, Moxifloxacin)",
                    "mechanism": "Calcium gắn với quinolone trong ruột, tạo phức hợp không hấp thu được, giảm hấp thu cả hai.",
                    "effect": "Giảm hấp thu cả calcium và quinolone, giảm hiệu quả điều trị",
                    "management": "Cách ít nhất 2 giờ giữa calcium và quinolone. Uống calcium trước, quinolone sau."
                }
            ],
            "moderate": [
                {
                    "drug": "Digoxin",
                    "mechanism": "Calcium có thể tăng tác dụng của digoxin trên tim, tăng nguy cơ loạn nhịp.",
                    "effect": "Tăng nguy cơ loạn nhịp tim do digoxin",
                    "management": "Thận trọng. Theo dõi nồng độ digoxin và ECG. Tránh tăng calci máu."
                },
                {
                    "drug": "Thiazide diuretics (Hydrochlorothiazide, Chlorthalidone)",
                    "mechanism": "Thiazide diuretics giảm bài tiết calcium qua thận, kết hợp với bổ sung calcium, dẫn đến tăng calci máu.",
                    "effect": "Tăng nguy cơ tăng calci máu, sỏi thận",
                    "management": "Theo dõi nồng độ calcium trong máu chặt chẽ. Có thể cần giảm liều calcium hoặc thiazide."
                },
                {
                    "drug": "Sắt (Iron)",
                    "mechanism": "Calcium gắn với sắt trong ruột, giảm hấp thu sắt.",
                    "effect": "Giảm hấp thu sắt, giảm hiệu quả điều trị thiếu máu",
                    "management": "Cách ít nhất 2 giờ giữa calcium và sắt. Uống sắt khi bụng đói, calcium sau bữa ăn."
                }
            ],
            "minor": [
                {
                    "drug": "Vitamin D",
                    "mechanism": "Vitamin D tăng hấp thu calcium từ ruột.",
                    "effect": "Tăng hấp thu calcium (tác dụng mong muốn khi dùng kết hợp)",
                    "management": "Kết hợp calcium và vitamin D là phổ biến và an toàn. Theo dõi nồng độ calcium để tránh tăng calci máu."
                }
            ]
        },
        "contraindications": {
            "tuyệt_đối": [
                "Tăng calci máu (hypercalcemia) - calcium làm nặng thêm",
                "Tăng calci niệu (hypercalciuria) nặng - tăng nguy cơ sỏi thận",
                "Sỏi thận calci đang hoạt động - tăng nguy cơ tái phát",
                "Suy thận nặng với tăng calci máu"
            ],
            "tương_đối": [
                "Suy thận nặng - tăng nguy cơ tăng calci máu, sỏi thận",
                "Sỏi thận calci (tiền sử) - thận trọng, theo dõi calci niệu",
                "Bệnh sarcoidosis - tăng nhạy cảm với calcium, tăng nguy cơ tăng calci máu",
                "Bệnh cường cận giáp (hyperparathyroidism) - có thể làm nặng tăng calci máu",
                "Dùng thiazide diuretics - tăng nguy cơ tăng calci máu",
                "Suy tim - calcium carbonate có thể gây đầy hơi, táo bón"
            ]
        },
        "pregnancy_lactation": {
            "fda_category": "A",
            "pregnancy_details": "Calcium an toàn và cần thiết trong thai kỳ. Thiếu calcium trong thai kỳ có thể gây loãng xương ở mẹ, chậm phát triển xương ở thai nhi, và các biến chứng khác. Nhu cầu calcium tăng trong thai kỳ. Khuyến cáo: 1,000-1,300 mg nguyên tố calci/ngày trong thai kỳ. Phụ nữ thiếu calcium cần bổ sung đủ. Kết hợp với vitamin D để tăng hấp thu.",
            "lactation": {
                "safety": "Compatible",
                "details": "Calcium bài tiết vào sữa mẹ. Nồng độ calcium trong sữa mẹ tương đối ổn định và không phụ thuộc nhiều vào nồng độ calcium của mẹ (do điều hòa từ xương). Tuy nhiên, thiếu calcium ở mẹ có thể ảnh hưởng đến sức khỏe mẹ (loãng xương).",
                "recommendation": "Có thể dùng khi cho con bú. Khuyến cáo: 1,000-1,300 mg nguyên tố calci/ngày khi cho con bú. Phụ nữ thiếu calcium cần bổ sung đủ để đảm bảo sức khỏe mẹ."
            }
        },
        "hepatic_adjustment": {
            "mild": "Không cần điều chỉnh liều. Calcium không chuyển hóa ở gan.",
            "moderate": "Không cần điều chỉnh liều. Calcium không chuyển hóa ở gan.",
            "severe": "Không cần điều chỉnh liều. Calcium không chuyển hóa ở gan. Tuy nhiên, suy gan nặng có thể ảnh hưởng đến albumin (protein binding của calcium).",
            "notes": "Calcium không chuyển hóa ở gan. Suy gan không ảnh hưởng đáng kể đến nồng độ calcium. Tuy nhiên, suy gan nặng có thể ảnh hưởng đến albumin, ảnh hưởng đến protein binding của calcium (nhưng không ảnh hưởng đến ionized calcium - dạng hoạt động)."
        },
        "overdose_management": {
            "symptoms": [
                "Tăng calci máu (hypercalcemia): buồn nôn, nôn, táo bón, yếu cơ, rối loạn tâm thần, hôn mê",
                "Tăng calci niệu (hypercalciuria): sỏi thận, đau thắt lưng, tiểu máu",
                "Suy thận: do tăng calci máu và sỏi thận",
                "Loạn nhịp tim: do tăng calci máu (đặc biệt với digoxin)",
                "Tổn thương thận vĩnh viễn (nếu không điều trị)",
                "Tử vong (trong trường hợp quá liều nghiêm trọng)"
            ],
            "antidote": "Không có antidote đặc hiệu. Điều trị hỗ trợ và giảm calci máu.",
            "treatment": [
                "Ngừng calcium ngay lập tức",
                "Ngừng bổ sung vitamin D nếu đang dùng",
                "Điều trị tăng calci máu:",
                "  - Truyền dịch muối đẳng trương (0.9% NaCl) để tăng bài tiết calcium qua thận",
                "  - Furosemide (lợi tiểu) để tăng bài tiết calcium (sau khi đã bù dịch)",
                "  - Calcitonin (giảm giải phóng calcium từ xương) nếu tăng calci máu nặng",
                "  - Bisphosphonates (pamidronate, zoledronate) nếu tăng calci máu nặng, kháng với điều trị khác",
                "  - Glucocorticoid (prednisone) để giảm hấp thu calcium ở ruột (trong một số trường hợp)",
                "  - Hemodialysis nếu tăng calci máu rất nặng và suy thận",
                "Theo dõi nồng độ calcium trong máu thường xuyên (mỗi 6-12 giờ)",
                "Theo dõi chức năng thận (creatinine, eGFR)",
                "Theo dõi ECG (loạn nhịp tim do tăng calci máu, đặc biệt với digoxin)",
                "Điều trị sỏi thận nếu có"
            ],
            "monitoring": "Nồng độ calcium trong máu (ionized và total), phosphate, creatinine, eGFR, ECG, dấu hiệu lâm sàng tăng calci máu."
        },
        "reversal_agents": {
            "available": False,
            "agents": []
        },
        "administration_instructions": {
            "oral": {
                "with_food": "Nên uống với thức ăn để tăng hấp thu và giảm tác dụng phụ (táo bón, đầy hơi).",
                "timing": "Uống 2-3 lần/ngày, chia liều (không uống quá 500-600mg nguyên tố calci mỗi lần) để tăng hấp thu. Cách xa các thuốc khác ít nhất 2-4 giờ: sắt (2 giờ), tetracycline, quinolone (2 giờ), levothyroxine (4 giờ)."
            },
            "iv": {
                "reconstitution": "Calcium chủ yếu dùng đường uống. IV chỉ dùng trong trường hợp hạ calci máu cấp tính.",
                "infusion_rate": "Truyền chậm (không quá 0.5-1 mEq/phút). Không truyền nhanh (tăng nguy cơ loạn nhịp tim).",
                "compatibility": ["Normal saline (0.9% NaCl), D5W"],
                "incompatibility": ["Không trộn với bicarbonate, phosphate (tạo kết tủa)"],
                "notes": "Calcium IV chỉ dùng trong trường hợp hạ calci máu cấp tính. Truyền chậm, theo dõi ECG. Không trộn với bicarbonate hoặc phosphate."
            }
        },
        "references": {
            "primary_sources": [
                "FDA Drug Label - Calcium (Calcium carbonate, Calcium citrate)",
                "Institute of Medicine (IOM) - Dietary Reference Intakes for Calcium and Vitamin D",
                "National Osteoporosis Foundation Guidelines - Calcium and Vitamin D",
                "UpToDate - Calcium supplementation",
                "Goodman & Gilman's The Pharmacological Basis of Therapeutics (14th ed)"
            ],
            "last_updated": "2025-02-04",
            "evidence_level": "A - Dựa trên FDA drug labels, IOM/NOF guidelines, và dữ liệu lâm sàng"
        }
    },
}

__all__ = ['SUPPORTIVE_DRUGS']
