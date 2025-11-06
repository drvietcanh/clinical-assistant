"""
Gastrointestinal Drugs
Generated from drug_database_data.py
"""

GASTROINTESTINAL_DRUGS = {
"Omeprazole": {
        "group": "Gastrointestinal - Proton Pump Inhibitor (PPI)",
        "vietnamese_name": "Omeprazole, Losec",
        "administration": ["PO", "IV"],
        "indications": [
            "Loét dạ dày tá tràng",
            "Trào ngược dạ dày thực quản (GERD)",
            "Hội chứng Zollinger-Ellison",
            "Phòng ngừa loét do stress",
            "Eradication H. pylori (kết hợp với kháng sinh)"
        ],
        "contraindications": [
            "Dị ứng",
            "Dùng cùng atazanavir"
        ],
        "dosage": {
            "adult_po": "20-40mg x 1-2 lần/ngày",
            "adult_iv": "40mg x 1-2 lần/ngày",
            "h_pylori": "20mg x 2 lần/ngày (với amoxicillin + clarithromycin)",
            "notes": "Uống 30 phút trước bữa ăn, không nhai/cắn viên"
        },
        "side_effects": [
            "Nhức đầu",
            "Tiêu chảy",
            "Đau bụng",
            "Tăng nguy cơ nhiễm C. difficile",
            "Gãy xương (dùng lâu dài, liều cao)",
            "Thiếu vitamin B12 (dùng lâu dài)",
            "Thiếu magnesium (dùng lâu dài)"
        ],
        "interactions": [
            "Clopidogrel: giảm hiệu quả clopidogrel",
            "Warfarin: có thể tăng tác dụng",
            "Phenytoin: tăng nồng độ phenytoin",
            "Methotrexate: tăng nồng độ methotrexate"
        ],
        "pregnancy": "C",
        "mechanism_of_action": "Ức chế không hồi phục H+/K+-ATPase (proton pump) ở tế bào thành dạ dày, giảm tiết acid dạ dày",
        "monitoring": [
            "Triệu chứng cải thiện (đau dạ dày, ợ chua)",
            "Vitamin B12 mỗi 1-2 năm nếu dùng lâu dài",
            "Magnesium nếu có triệu chứng (chuột rút, yếu cơ) hoặc dùng lâu dài",
            "Mật độ xương nếu dùng lâu dài, liều cao (phụ nữ >50 tuổi)",
            "Theo dõi nhiễm C. difficile nếu có tiêu chảy"
        ],
        "precautions": [
            "Uống 30 phút trước bữa ăn (để tối đa hóa hiệu quả)",
            "Không nhai/cắn viên bao tan trong ruột",
            "Dùng liều thấp nhất có hiệu quả, thời gian ngắn nhất",
            "Cân nhắc giảm liều hoặc ngừng sau 4-8 tuần nếu có thể",
            "Bổ sung vitamin B12 nếu dùng lâu dài",
            "Bổ sung magnesium nếu thiếu"
        ],
        "pharmacokinetics": {
            "half_life": "0.5-1 giờ (ngắn), nhưng tác dụng kéo dài do ức chế không hồi phục",
            "onset": "1-3 giờ",
            "duration": "24 giờ (một liều)",
            "protein_binding": "95%",
            "clearance": "Gan (CYP2C19, CYP3A4)"
                },
        "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm",
        "black_box_warnings": "Có thể tăng nguy cơ gãy xương hông, cổ tay, cột sống khi dùng lâu dài (≥1 năm) và liều cao. Giảm hiệu quả clopidogrel khi dùng đồng thời. Nguy cơ nhiễm C. difficile tăng. Giảm hấp thu vitamin B12 và magnesium khi dùng lâu dài",
        "drug_interactions": {
            "major": [
                {
                    "drug": "Clopidogrel",
                    "mechanism": "Omeprazole ức chế CYP2C19, enzyme cần thiết để chuyển hóa clopidogrel thành dạng hoạt động",
                    "effect": "Giảm hiệu quả chống kết tập tiểu cầu của clopidogrel, tăng nguy cơ biến cố tim mạch",
                    "management": "Tránh dùng cùng. Chuyển sang pantoprazole (ít ảnh hưởng hơn) hoặc PPI khác không ức chế CYP2C19. Nếu phải dùng, cân nhắc dùng cách thời gian (omeprazole trước clopidogrel 12 giờ)."
                },
                {
                    "drug": "Atazanavir (HIV protease inhibitor)",
                    "mechanism": "PPI làm tăng pH dạ dày, giảm hấp thu atazanavir (cần môi trường acid)",
                    "effect": "Giảm nồng độ atazanavir, giảm hiệu quả điều trị HIV, tăng nguy cơ kháng thuốc",
                    "management": "CHỐNG CHỈ ĐỊNH dùng cùng. Không dùng omeprazole với atazanavir. Dùng H2 blocker hoặc PPI khác cách thời gian (12 giờ)."
                }
            ],
            "moderate": [
                {
                    "drug": "Warfarin",
                    "mechanism": "Omeprazole ức chế CYP2C9 nhẹ, có thể tăng nồng độ warfarin",
                    "effect": "Tăng INR, tăng nguy cơ chảy máu",
                    "management": "Theo dõi INR thường xuyên. Điều chỉnh liều warfarin nếu cần."
                },
                {
                    "drug": "Phenytoin",
                    "mechanism": "Omeprazole ức chế CYP2C19, giảm chuyển hóa phenytoin",
                    "effect": "Tăng nồng độ phenytoin, tăng nguy cơ độc tính (chóng mặt, nystagmus, ataxia)",
                    "management": "Theo dõi nồng độ phenytoin. Giảm liều phenytoin nếu cần."
                },
                {
                    "drug": "Methotrexate (liều cao)",
                    "mechanism": "PPI giảm thải trừ methotrexate qua thận (cạnh tranh với organic anion transporters)",
                    "effect": "Tăng nồng độ methotrexate, tăng nguy cơ độc tính (myelosuppression, mucositis, nephrotoxicity)",
                    "management": "Thận trọng. Tạm ngừng PPI khi dùng methotrexate liều cao. Theo dõi chức năng thận, công thức máu."
                },
                {
                    "drug": "Ketoconazole, Itraconazole, Posaconazole",
                    "mechanism": "PPI tăng pH dạ dày, giảm hấp thu azole antifungals (cần môi trường acid)",
                    "effect": "Giảm nồng độ azole, giảm hiệu quả điều trị",
                    "management": "Cách thời gian ít nhất 2 giờ. Hoặc dùng dạng lỏng posaconazole (ít ảnh hưởng pH hơn)."
                },
                {
                    "drug": "Iron salts (ferrous sulfate, ferrous fumarate)",
                    "mechanism": "PPI giảm acid dạ dày, giảm chuyển Fe3+ thành Fe2+ (dạng hấp thu được)",
                    "effect": "Giảm hấp thu sắt, có thể gây thiếu máu thiếu sắt",
                    "management": "Cách thời gian ít nhất 2 giờ. Hoặc dùng sắt dạng chelate (iron bisglycinate) ít phụ thuộc acid."
                },
                {
                    "drug": "Vitamin B12 (cobalamin)",
                    "mechanism": "PPI giảm acid dạ dày, giảm tách B12 khỏi protein thức ăn",
                    "effect": "Giảm hấp thu B12, có thể gây thiếu máu thiếu B12 sau 2-3 năm dùng PPI",
                    "management": "Bổ sung B12 định kỳ nếu dùng PPI lâu dài (>2 năm). Theo dõi B12 máu mỗi 1-2 năm."
                }
            ],
            "minor": [
                {
                    "drug": "Diazepam",
                    "mechanism": "Ức chế CYP2C19 nhẹ",
                    "effect": "Tăng nồng độ diazepam nhẹ",
                    "management": "Thận trọng, không cần điều chỉnh liều thường quy"
                },
                {
                    "drug": "Citalopram, Escitalopram",
                    "mechanism": "Ức chế CYP2C19",
                    "effect": "Tăng nồng độ SSRI nhẹ",
                    "management": "Thận trọng, theo dõi tác dụng phụ SSRI"
                }
            ]
        },
        "contraindications": {
            "absolute": [
                "Dị ứng omeprazole hoặc PPI khác",
                "Dùng cùng atazanavir (HIV protease inhibitor) - CHỐNG CHỈ ĐỊNH tuyệt đối do giảm hấp thu atazanavir"
            ],
            "relative": [
                "Suy gan nặng (Child-Pugh C) - giảm liều tối đa 20mg/ngày",
                "Suy thận nặng (CrCl <30) - không cần chỉnh liều nhưng thận trọng",
                "Loãng xương - tăng nguy cơ gãy xương khi dùng lâu dài",
                "Nhiễm C. difficile - tăng nguy cơ",
                "Thiếu vitamin B12 - bổ sung nếu dùng lâu dài",
                "Thiếu magnesium - bổ sung nếu dùng lâu dài"
            ]
        },
        "pregnancy_lactation": {
            "fda_category": "C",
            "pregnancy_details": "Omeprazole là FDA category C. Nghiên cứu trên động vật cho thấy có thể gây độc tính cho thai nhi, nhưng không có nghiên cứu đầy đủ trên người. Một số nghiên cứu quan sát lớn không cho thấy tăng nguy cơ dị tật bẩm sinh. Có thể dùng trong thai kỳ nếu lợi ích > nguy cơ, đặc biệt trong GERD nặng hoặc loét dạ dày. Dùng liều thấp nhất có hiệu quả.",
            "lactation": {
                "safety": "Compatible",
                "details": "Omeprazole bài tiết vào sữa mẹ ở nồng độ thấp. Nồng độ trong sữa mẹ rất thấp (<0.01% liều mẹ). Không có báo cáo tác dụng phụ ở trẻ bú mẹ. An toàn khi cho con bú.",
                "recommendation": "Có thể dùng khi cho con bú. Dùng liều thường dùng (20-40mg/ngày). Theo dõi trẻ nếu có lo ngại."
            }
        },
        "hepatic_adjustment": {
            "mild": "Không cần chỉnh liều",
            "moderate": "Không cần chỉnh liều, nhưng thận trọng",
            "severe": "Giảm liều tối đa 20mg/ngày (Child-Pugh C). Omeprazole chuyển hóa ở gan qua CYP2C19 và CYP3A4. Suy gan nặng làm giảm clearance, tăng nồng độ thuốc.",
            "notes": "Omeprazole chuyển hóa ở gan. Suy gan nặng làm giảm chuyển hóa, tăng nồng độ. Tuy nhiên, PPI thường được dung nạp tốt ngay cả ở suy gan. Giảm liều ở suy gan nặng (Child-Pugh C)."
        },
        "overdose_management": {
            "symptoms": [
                "PPI ít gây quá liều nghiêm trọng do an toàn tốt",
                "Triệu chứng nhẹ: nhức đầu, buồn nôn, tiêu chảy, chóng mặt",
                "Liều rất cao có thể gây: buồn ngủ, lú lẫn"
            ],
            "antidote": "Không có antidote đặc hiệu",
            "treatment": [
                "Hỗ trợ triệu chứng nếu có",
                "Theo dõi dấu hiệu sinh tồn",
                "Nếu uống trong vòng 1-2 giờ: có thể cân nhắc activated charcoal (hiệu quả thấp)",
                "Hầu hết trường hợp tự khỏi, không cần điều trị đặc hiệu"
            ],
            "monitoring": "Theo dõi dấu hiệu sinh tồn, triệu chứng thần kinh nhẹ"
        },
        "reversal_agents": None,
        "administration_instructions": {
            "oral": {
                "with_food": "Uống 30 phút TRƯỚC bữa ăn (quan trọng - để PPI hoạt động khi proton pump được kích hoạt bởi thức ăn)",
                "timing": "Uống vào buổi sáng trước bữa sáng (hoặc 30 phút trước bữa tối nếu dùng 2 lần/ngày). KHÔNG được nhai hoặc nghiền viên bao tan trong ruột (enteric-coated) - phải nuốt nguyên viên. Nếu khó nuốt, có thể mở viên và rắc vào thức ăn mềm (táo, sữa chua) nhưng phải nuốt ngay, không nhai."
            },
            "iv": {
                "reconstitution": "Omeprazole IV: 40mg pha với 100ml NaCl 0.9% hoặc dextrose 5%",
                "infusion_rate": "Truyền trong 20-30 phút",
                "compatibility": ["NaCl 0.9%", "Dextrose 5%"],
                "incompatibility": ["Không pha với các thuốc khác trong cùng đường truyền"],
                "notes": "Chỉ dùng IV khi không uống được. Chuyển sang PO sớm nhất có thể. Bảo quản dung dịch đã pha ở nhiệt độ phòng, dùng trong 12 giờ."
            }
        },
        "references": {
            "primary_sources": [
                "FDA Drug Label - Omeprazole",
                "UpToDate - Proton pump inhibitors: Overview of use and adverse effects",
                "Micromedex - Omeprazole",
                "Goodman & Gilman's The Pharmacological Basis of Therapeutics",
                "Lancet - Proton pump inhibitors and risk of fractures (2006)",
                "JAMA - Clopidogrel-omeprazole interaction (2010)"
            ],
            "last_updated": "2024-12-19",
            "evidence_level": "High - FDA approved, multiple RCTs, systematic reviews"
        }
    },
    "Pantoprazole": {
        "group": "Gastrointestinal - Proton Pump Inhibitor",
        "vietnamese_name": "Pantoprazole, Pantoloc",
        "administration": ["PO", "IV"],
        "indications": [
            "Loét dạ dày tá tràng",
            "GERD",
            "Phòng ngừa loét do stress"
        ],
        "contraindications": [
            "Dị ứng"
        ],
        "dosage": {
            "adult_po": "40mg x 1-2 lần/ngày",
            "adult_iv": "40mg x 1-2 lần/ngày",
            "notes": "Ít tương tác hơn omeprazole với clopidogrel"
        },
        "side_effects": [
            "Nhức đầu",
            "Tiêu chảy",
            "Tương tự omeprazole"
        ],
                  "interactions": [
              "Ít tương tác hơn omeprazole"
          ],
          "pregnancy": "B",
          "mechanism_of_action": "Proton pump inhibitor (PPI). Ức chế H+/K+-ATPase (proton pump) ở tế bào thành dạ dày, giảm tiết acid dạ dày mạnh và kéo dài. Khác với H2 blockers, PPI ức chế bước cuối cùng của quá trình tiết acid, nên hiệu quả hơn. Pantoprazole ít tương tác với CYP450 hơn omeprazole.",
          "monitoring": [
              "Đáp ứng lâm sàng: giảm triệu chứng đau, ợ nóng",
              "Mg2+ máu (nếu dùng kéo dài >3 tháng) - PPI có thể gây hạ magie máu",
              "Vitamin B12 (nếu dùng kéo dài >2 năm) - PPI giảm hấp thu B12",
              "Dấu hiệu nhiễm trùng: PPI tăng nguy cơ viêm phổi, C. difficile colitis",
              "Loãng xương: PPI dùng kéo dài có thể tăng nguy cơ gãy xương (cần monitor nếu >1 năm)"
          ],
          "precautions": [
              "Uống 30-60 phút TRƯỚC bữa ăn (để PPI hoạt động khi proton pump được kích hoạt)",
              "KHÔNG được nhai hoặc nghiền viên bao tan trong ruột (enteric-coated)",
              "Pantoprazole ưu điểm: ít tương tác với CYP450 hơn omeprazole, ít ảnh hưởng đến clopidogrel hơn",
              "Dùng ngắn hạn khi có thể - tránh dùng kéo dài không cần thiết",
              "Thận trọng ở bệnh nhân loãng xương (PPI dùng kéo dài có thể tăng nguy cơ gãy xương)",
              "Thận trọng ở bệnh nhân suy thận (không cần chỉnh liều nhưng monitor)",
              "Tăng nguy cơ viêm phổi, C. difficile colitis (đặc biệt ở người già, suy giảm miễn dịch)"
          ],
          "pharmacokinetics": {
              "half_life": "1 giờ (ngắn), nhưng tác dụng kéo dài 24h do ức chế không thuận nghịch proton pump",
              "onset": "1-3 ngày (tác dụng đầy đủ)",
              "duration": "24 giờ (mặc dù half-life ngắn)",
              "protein_binding": "98%",
              "clearance": "Gan (CYP2C19, CYP3A4) - ít tương tác hơn omeprazole"
          },
          "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm, tránh ánh sáng",
          "black_box_warnings": "Có thể tăng nguy cơ gãy xương hông, cổ tay, cột sống khi dùng lâu dài (≥1 năm) và liều cao. Nguy cơ nhiễm C. difficile tăng. Giảm hấp thu vitamin B12 và magnesium khi dùng lâu dài",
          "drug_interactions": {
            "major": [
                {
                    "drug": "Atazanavir (HIV protease inhibitor)",
                    "mechanism": "PPI làm tăng pH dạ dày, giảm hấp thu atazanavir (cần môi trường acid)",
                    "effect": "Giảm nồng độ atazanavir, giảm hiệu quả điều trị HIV",
                    "management": "CHỐNG CHỈ ĐỊNH dùng cùng. Không dùng pantoprazole với atazanavir. Dùng H2 blocker hoặc cách thời gian 12 giờ."
                }
            ],
            "moderate": [
                {
                    "drug": "Warfarin",
                    "mechanism": "Pantoprazole ít ức chế CYP450 hơn omeprazole, nhưng vẫn có thể tương tác nhẹ",
                    "effect": "Có thể tăng INR nhẹ",
                    "management": "Theo dõi INR thường xuyên. Pantoprazole ít ảnh hưởng hơn omeprazole."
                },
                {
                    "drug": "Ketoconazole, Itraconazole, Posaconazole",
                    "mechanism": "PPI tăng pH dạ dày, giảm hấp thu azole antifungals (cần môi trường acid)",
                    "effect": "Giảm nồng độ azole, giảm hiệu quả điều trị",
                    "management": "Cách thời gian ít nhất 2 giờ. Hoặc dùng dạng lỏng posaconazole."
                },
                {
                    "drug": "Iron salts (ferrous sulfate, ferrous fumarate)",
                    "mechanism": "PPI giảm acid dạ dày, giảm chuyển Fe3+ thành Fe2+",
                    "effect": "Giảm hấp thu sắt",
                    "management": "Cách thời gian ít nhất 2 giờ. Hoặc dùng sắt dạng chelate."
                },
                {
                    "drug": "Vitamin B12 (cobalamin)",
                    "mechanism": "PPI giảm acid dạ dày, giảm tách B12 khỏi protein thức ăn",
                    "effect": "Giảm hấp thu B12 sau 2-3 năm dùng PPI",
                    "management": "Bổ sung B12 định kỳ nếu dùng lâu dài (>2 năm)."
                }
            ],
            "minor": [
                {
                    "drug": "Clopidogrel",
                    "mechanism": "Pantoprazole ít ức chế CYP2C19 hơn omeprazole",
                    "effect": "Ít ảnh hưởng đến clopidogrel hơn omeprazole, nhưng vẫn thận trọng",
                    "management": "Pantoprazole là lựa chọn tốt hơn omeprazole khi cần dùng với clopidogrel. Vẫn nên tránh dùng cùng nếu có thể."
                }
            ]
        },
        "contraindications": {
            "absolute": [
                "Dị ứng pantoprazole hoặc PPI khác",
                "Dùng cùng atazanavir (HIV protease inhibitor) - CHỐNG CHỈ ĐỊNH tuyệt đối"
            ],
            "relative": [
                "Suy gan nặng (Child-Pugh C) - thận trọng, có thể giảm liều",
                "Suy thận nặng (CrCl <30) - không cần chỉnh liều nhưng thận trọng",
                "Loãng xương - tăng nguy cơ gãy xương khi dùng lâu dài",
                "Nhiễm C. difficile - tăng nguy cơ",
                "Thiếu vitamin B12 - bổ sung nếu dùng lâu dài",
                "Thiếu magnesium - bổ sung nếu dùng lâu dài"
            ]
        },
        "pregnancy_lactation": {
            "fda_category": "B",
            "pregnancy_details": "Pantoprazole là FDA category B. Nghiên cứu trên động vật không cho thấy nguy cơ cho thai nhi, nhưng không có nghiên cứu đầy đủ trên người. Một số nghiên cứu quan sát không cho thấy tăng nguy cơ dị tật bẩm sinh. Có thể dùng trong thai kỳ nếu lợi ích > nguy cơ. An toàn hơn omeprazole (category C) trong thai kỳ.",
            "lactation": {
                "safety": "Compatible",
                "details": "Pantoprazole bài tiết vào sữa mẹ ở nồng độ rất thấp. Không có báo cáo tác dụng phụ ở trẻ bú mẹ. An toàn khi cho con bú.",
                "recommendation": "Có thể dùng khi cho con bú. Dùng liều thường dùng (40mg/ngày)."
            }
        },
        "hepatic_adjustment": {
            "mild": "Không cần chỉnh liều",
            "moderate": "Không cần chỉnh liều, nhưng thận trọng",
            "severe": "Thận trọng ở suy gan nặng (Child-Pugh C). Có thể giảm liều. Pantoprazole chuyển hóa ở gan qua CYP2C19 và CYP3A4, nhưng ít phụ thuộc vào CYP2C19 hơn omeprazole.",
            "notes": "Pantoprazole ít tương tác với CYP450 hơn omeprazole, nên ít ảnh hưởng hơn ở suy gan. Tuy nhiên, vẫn thận trọng ở suy gan nặng."
        },
        "overdose_management": {
            "symptoms": [
                "PPI ít gây quá liều nghiêm trọng",
                "Triệu chứng nhẹ: nhức đầu, buồn nôn, tiêu chảy, chóng mặt"
            ],
            "antidote": "Không có antidote đặc hiệu",
            "treatment": [
                "Hỗ trợ triệu chứng",
                "Theo dõi dấu hiệu sinh tồn",
                "Hầu hết trường hợp tự khỏi"
            ],
            "monitoring": "Theo dõi dấu hiệu sinh tồn, triệu chứng nhẹ"
        },
        "reversal_agents": None,
        "administration_instructions": {
            "oral": {
                "with_food": "Uống 30-60 phút TRƯỚC bữa ăn (quan trọng - để PPI hoạt động khi proton pump được kích hoạt)",
                "timing": "Uống vào buổi sáng trước bữa sáng (hoặc trước bữa tối nếu dùng 2 lần/ngày). KHÔNG được nhai hoặc nghiền viên bao tan trong ruột - phải nuốt nguyên viên."
            },
            "iv": {
                "reconstitution": "Pantoprazole IV: 40mg pha với 100ml NaCl 0.9% hoặc dextrose 5%",
                "infusion_rate": "Truyền trong 15 phút (IV bolus) hoặc 30 phút (infusion)",
                "compatibility": ["NaCl 0.9%", "Dextrose 5%"],
                "incompatibility": ["Không pha với các thuốc khác trong cùng đường truyền"],
                "notes": "Chỉ dùng IV khi không uống được. Chuyển sang PO sớm nhất có thể."
            }
        },
        "references": {
            "primary_sources": [
                "FDA Drug Label - Pantoprazole",
                "UpToDate - Proton pump inhibitors: Overview of use and adverse effects",
                "Micromedex - Pantoprazole",
                "Goodman & Gilman's The Pharmacological Basis of Therapeutics",
                "JAMA - Pantoprazole vs omeprazole and clopidogrel interaction (2010)"
            ],
            "last_updated": "2024-12-19",
            "evidence_level": "High - FDA approved, multiple RCTs"
        }
      },
      "Ranitidine": {
        "group": "Gastrointestinal - H2 Receptor Antagonist",
        "vietnamese_name": "Ranitidine, Zantac",
        "administration": ["PO", "IV"],
        "indications": [
            "Loét dạ dày tá tràng",
            "GERD",
            "Phòng ngừa loét do stress"
        ],
        "contraindications": [
            "Dị ứng"
        ],
        "dosage": {
            "adult_po": "150mg x 2 lần/ngày hoặc 300mg x 1 lần/ngày",
            "adult_iv": "50mg x 3 lần/ngày hoặc 150mg truyền liên tục/24h",
            "notes": "Yếu hơn PPI, nhưng rẻ hơn. Một số sản phẩm đã bị thu hồi do NDMA"
        },
        "side_effects": [
            "Nhức đầu",
            "Rối loạn tiêu hóa",
            "Tăng men gan (hiếm)"
        ],
        "interactions": [
            "Warfarin: có thể tăng tác dụng (ít hơn cimetidine)"
        ],
        "pregnancy": "B",
        "mechanism_of_action": "H2 (histamine-2) receptor antagonist. Ức chế histamine tại H2 receptors ở tế bào thành dạ dày, giảm tiết acid dạ dày (giảm acid kích thích và một phần acid cơ bản). Yếu hơn PPI (proton pump inhibitor) nhưng rẻ hơn. Tác dụng ngắn hơn PPI (cần dùng 2 lần/ngày). Ức chế nhẹ một số enzyme CYP450 (ít hơn cimetidine).",
        "monitoring": [
            "Đáp ứng lâm sàng (giảm đau, triệu chứng GERD)",
            "Chức năng gan (transaminase) - có thể tăng men gan (hiếm)",
            "Dấu hiệu nhiễm C. difficile (tiêu chảy nặng, đau bụng) - tăng nguy cơ nhẹ",
            "INR nếu dùng với warfarin (tăng nguy cơ chảy máu nhẹ)"
        ],
        "precautions": [
            "Uống với thức ăn hoặc trước bữa ăn (tăng hiệu quả)",
            "Yếu hơn PPI - cân nhắc dùng PPI nếu không đáp ứng",
            "Thận trọng ở suy thận (giảm liều)",
            "Thận trọng ở suy gan (giảm liều)",
            "Cân nhắc ngừng sau 4-8 tuần nếu không cần thiết (giảm nguy cơ tác dụng phụ)",
            "Một số sản phẩm đã bị thu hồi do NDMA (chất gây ung thư) - kiểm tra nguồn gốc sản phẩm",
            "Không dùng với các thuốc cần acid để hấp thu (ketoconazole, itraconazole, iron salts) - cách 2 giờ"
        ],
        "pharmacokinetics": {
            "half_life": "2-3 giờ",
            "onset": "1-3 giờ",
            "duration": "8-12 giờ",
            "protein_binding": "15%",
            "metabolism": "Gan (chuyển hóa qua CYP450, một phần), thận (thải trừ)",
            "clearance": "Gan (chuyển hóa), thận (30-50% thải nguyên dạng)"
        },
        "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm, tránh ánh sáng. Kiểm tra nguồn gốc sản phẩm (một số sản phẩm đã bị thu hồi do NDMA).",
        "black_box_warnings": "Một số sản phẩm ranitidine đã bị thu hồi do chứa NDMA (N-nitrosodimethylamine) - chất gây ung thư. NDMA có thể tích lũy trong sản phẩm theo thời gian, đặc biệt ở nhiệt độ cao. Kiểm tra nguồn gốc sản phẩm và cân nhắc dùng thuốc khác (PPI, famotidine) nếu có thể.",
        "drug_interactions": {
            "major": [],
            "moderate": [
                {
                    "drug": "Warfarin",
                    "mechanism": "Ranitidine ức chế CYP450 nhẹ (ít hơn cimetidine)",
                    "effect": "Có thể tăng INR nhẹ, tăng nguy cơ chảy máu",
                    "management": "Theo dõi INR thường xuyên. Ranitidine ít ảnh hưởng hơn cimetidine."
                },
                {
                    "drug": "Ketoconazole, Itraconazole",
                    "mechanism": "H2 blocker giảm acid dạ dày, giảm hấp thu azole antifungals",
                    "effect": "Giảm nồng độ azole, giảm hiệu quả điều trị",
                    "management": "Cách thời gian ít nhất 2 giờ."
                },
                {
                    "drug": "Iron salts",
                    "mechanism": "H2 blocker giảm acid dạ dày, giảm hấp thu sắt",
                    "effect": "Giảm hấp thu sắt",
                    "management": "Cách thời gian ít nhất 2 giờ."
                }
            ],
            "minor": [
                {
                    "drug": "Phenytoin, Theophylline",
                    "mechanism": "Ức chế CYP450 nhẹ",
                    "effect": "Có thể tăng nồng độ nhẹ",
                    "management": "Thận trọng, theo dõi nồng độ nếu cần"
                }
            ]
        },
        "contraindications": {
            "absolute": [
                "Dị ứng ranitidine hoặc H2 blocker khác",
                "Một số sản phẩm ranitidine đã bị thu hồi do NDMA - tránh dùng các sản phẩm bị thu hồi"
            ],
            "relative": [
                "Suy thận nặng (CrCl <30) - giảm liều 50%",
                "Suy gan nặng (Child-Pugh C) - giảm liều 50%",
                "Người già - thận trọng, giảm liều nếu cần",
                "Nhiễm C. difficile - tăng nguy cơ nhẹ"
            ]
        },
        "pregnancy_lactation": {
            "fda_category": "B",
            "pregnancy_details": "Ranitidine là FDA category B. Nghiên cứu trên động vật không cho thấy nguy cơ cho thai nhi. Một số nghiên cứu trên người không cho thấy tăng nguy cơ dị tật bẩm sinh. Có thể dùng trong thai kỳ nếu lợi ích > nguy cơ. Tuy nhiên, một số nghiên cứu gần đây gợi ý có thể có nguy cơ nhẹ, nên cân nhắc dùng PPI (pantoprazole, esomeprazole) nếu có thể.",
            "lactation": {
                "safety": "Compatible",
                "details": "Ranitidine bài tiết vào sữa mẹ ở nồng độ thấp. An toàn khi cho con bú.",
                "recommendation": "Có thể dùng khi cho con bú. Dùng liều thường dùng."
            }
        },
        "hepatic_adjustment": {
            "mild": "Không cần chỉnh liều",
            "moderate": "Giảm liều 50%",
            "severe": "Giảm liều 50% (Child-Pugh C). Ranitidine chuyển hóa ở gan một phần, thải trừ qua thận. Suy gan nặng làm giảm chuyển hóa.",
            "notes": "Giảm liều ở suy gan trung bình và nặng. Thận trọng theo dõi."
        },
        "overdose_management": {
            "symptoms": [
                "H2 blocker ít gây quá liều nghiêm trọng",
                "Triệu chứng nhẹ: nhức đầu, buồn nôn, chóng mặt",
                "Liều rất cao có thể gây: lú lẫn, co giật (hiếm)"
            ],
            "antidote": "Không có antidote đặc hiệu",
            "treatment": [
                "Hỗ trợ triệu chứng",
                "Theo dõi dấu hiệu sinh tồn",
                "Nếu uống trong vòng 1-2 giờ: có thể cân nhắc activated charcoal",
                "Hầu hết trường hợp tự khỏi"
            ],
            "monitoring": "Theo dõi dấu hiệu sinh tồn, triệu chứng thần kinh"
        },
        "reversal_agents": None,
        "administration_instructions": {
            "oral": {
                "with_food": "Uống với thức ăn hoặc trước bữa ăn (tăng hiệu quả)",
                "timing": "Uống 2 lần/ngày (sáng và tối) hoặc 1 lần/ngày vào buổi tối. Có thể uống với hoặc không với thức ăn."
            },
            "iv": {
                "reconstitution": "Ranitidine IV: 50mg pha với 20-50ml NaCl 0.9% hoặc dextrose 5%",
                "infusion_rate": "Truyền trong 15-20 phút (bolus) hoặc 50mg truyền liên tục trong 24 giờ",
                "compatibility": ["NaCl 0.9%", "Dextrose 5%"],
                "incompatibility": ["Không pha với các thuốc khác trong cùng đường truyền"],
                "notes": "Chỉ dùng IV khi không uống được. Chuyển sang PO sớm nhất có thể."
            }
        },
        "references": {
            "primary_sources": [
                "FDA Drug Label - Ranitidine (Note: Many products recalled due to NDMA)",
                "UpToDate - H2-receptor antagonists: Pharmacology and clinical use",
                "Micromedex - Ranitidine",
                "Goodman & Gilman's The Pharmacological Basis of Therapeutics"
            ],
            "last_updated": "2024-12-19",
            "evidence_level": "High - FDA approved, multiple RCTs (Note: Many products recalled due to NDMA contamination)"
        }
    },
    "Metoclopramide": {
        "group": "Gastrointestinal - Prokinetic, Antiemetic",
        "vietnamese_name": "Metoclopramide, Primperan",
        "administration": ["PO", "IV", "IM"],
        "indications": [
            "Buồn nôn, nôn",
            "Liệt dạ dày",
            "Trào ngược dạ dày thực quản",
            "Đau nửa đầu (kết hợp)"
        ],
        "contraindications": [
            "Tắc ruột",
            "Xuất huyết tiêu hóa",
            "Rối loạn vận động (Parkinson, dystonia)",
            "Epilepsy"
        ],
        "dosage": {
            "adult_po": "10mg x 3-4 lần/ngày",
            "adult_iv_im": "10mg IV/IM mỗi 6-8 giờ",
            "adult_max": "60mg/ngày",
            "notes": "Không dùng quá 12 tuần (rối loạn vận động muộn)"
        },
        "side_effects": [
            "Rối loạn vận động (dystonia, parkinsonism)",
            "Buồn ngủ",
            "Hội chứng serotonin (với SSRI)",
            "Rối loạn vận động muộn (dùng lâu dài)"
        ],
        "interactions": [
            "SSRI/SNRI: tăng nguy cơ hội chứng serotonin",
            "Antipsychotics: tăng nguy cơ rối loạn vận động"
        ],
        "pregnancy": "B",
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "Giảm liều 25-50%",
            "under_30": "Giảm liều 50-75%"
        },
        "mechanism_of_action": "Dopamine D2 receptor antagonist và 5-HT3 receptor antagonist. Ức chế dopamine ở chemoreceptor trigger zone (CTZ), giảm buồn nôn, nôn. Tăng co bóp dạ dày, tăng trương lực cơ thắt môn vị, tăng nhu động ruột (prokinetic effect). Cũng ức chế 5-HT3 receptor (giống ondansetron).",
        "monitoring": [
            "Dấu hiệu rối loạn vận động: dystonia, parkinsonism, akathisia (xuất hiện sớm, có thể điều trị)",
            "Rối loạn vận động muộn (tardive dyskinesia) - nếu dùng >12 tuần (có thể không hồi phục)",
            "Dấu hiệu hội chứng serotonin: kích động, tăng thân nhiệt, tăng phản xạ (nếu dùng với SSRI/SNRI)",
            "Đáp ứng lâm sàng: giảm buồn nôn, nôn; tăng nhu động dạ dày"
        ],
        "precautions": [
            "KHÔNG dùng quá 12 tuần - tăng nguy cơ rối loạn vận động muộn (tardive dyskinesia) có thể không hồi phục",
            "Thận trọng ở trẻ em và thanh niên - tăng nguy cơ rối loạn vận động (dystonia, parkinsonism)",
            "Tránh dùng ở bệnh nhân Parkinson, dystonia - làm nặng triệu chứng",
            "Thận trọng khi dùng với SSRI/SNRI - tăng nguy cơ hội chứng serotonin",
            "Thận trọng khi dùng với antipsychotics - tăng nguy cơ rối loạn vận động",
            "Tránh dùng với anticholinergics - đối kháng tác dụng prokinetic",
            "CHỐNG CHỈ ĐỊNH trong tắc ruột, xuất huyết tiêu hóa",
            "Có thể gây buồn ngủ - tránh lái xe, vận hành máy móc"
        ],
        "pharmacokinetics": {
            "half_life": "5-6 giờ",
            "onset": "1-3 phút (IV), 30-60 phút (PO)",
            "duration": "1-2 giờ",
            "protein_binding": "30%",
            "clearance": "Gan (CYP2D6), thận (30% thải nguyên dạng)"
        },
        "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm, tránh ánh sáng",
        "black_box_warnings": "Rối loạn vận động muộn (tardive dyskinesia) có thể phát triển và trở thành không hồi phục. Nguy cơ tăng với thời gian điều trị và tổng liều. Ngừng ngay nếu có dấu hiệu rối loạn vận động. KHÔNG dùng quá 12 tuần",
        "drug_interactions": {
            "major": [
                {
                    "drug": "SSRI/SNRI (fluoxetine, sertraline, venlafaxine, etc.)",
                    "mechanism": "Metoclopramide ức chế 5-HT3 receptor và có thể tăng serotonin, tác dụng hiệp đồng với SSRI/SNRI",
                    "effect": "Tăng nguy cơ hội chứng serotonin (kích động, tăng thân nhiệt, tăng phản xạ, co giật)",
                    "management": "Tránh dùng cùng hoặc thận trọng. Theo dõi dấu hiệu hội chứng serotonin. Ngừng ngay nếu có triệu chứng."
                }
            ],
            "moderate": [
                {
                    "drug": "Antipsychotics (haloperidol, chlorpromazine, risperidone, etc.)",
                    "mechanism": "Tác dụng hiệp đồng ức chế dopamine D2 receptor",
                    "effect": "Tăng nguy cơ rối loạn vận động (extrapyramidal symptoms, tardive dyskinesia)",
                    "management": "Thận trọng. Tránh dùng cùng nếu có thể. Theo dõi dấu hiệu rối loạn vận động."
                },
                {
                    "drug": "Anticholinergics (atropine, scopolamine, benztropine)",
                    "mechanism": "Đối kháng tác dụng prokinetic của metoclopramide",
                    "effect": "Giảm hiệu quả prokinetic, có thể gây tắc ruột",
                    "management": "Tránh dùng cùng. Đối kháng tác dụng."
                },
                {
                    "drug": "CNS depressants (alcohol, opioids, benzodiazepines)",
                    "mechanism": "Tác dụng hiệp đồng ức chế thần kinh trung ương",
                    "effect": "Tăng buồn ngủ, lú lẫn",
                    "management": "Thận trọng. Tránh lái xe, vận hành máy móc."
                }
            ],
            "minor": [
                {
                    "drug": "Paracetamol",
                    "mechanism": "Tăng nhu động dạ dày",
                    "effect": "Tăng hấp thu paracetamol nhẹ",
                    "management": "Không cần điều chỉnh liều"
                }
            ]
        },
        "contraindications": {
            "absolute": [
                "Dị ứng metoclopramide",
                "Tắc ruột cơ học",
                "Xuất huyết tiêu hóa",
                "Thủng dạ dày-ruột",
                "Pheochromocytoma (tăng nguy cơ tăng huyết áp)",
                "Rối loạn vận động (Parkinson, dystonia, tardive dyskinesia)"
            ],
            "relative": [
                "Suy thận (CrCl <30) - giảm liều 50-75%",
                "Suy gan nặng - thận trọng, có thể giảm liều",
                "Trẻ em và thanh niên - tăng nguy cơ dystonia, parkinsonism",
                "Epilepsy - có thể làm nặng co giật",
                "Đang dùng SSRI/SNRI - tăng nguy cơ hội chứng serotonin",
                "Đang dùng antipsychotics - tăng nguy cơ rối loạn vận động"
            ]
        },
        "pregnancy_lactation": {
            "fda_category": "B",
            "pregnancy_details": "Metoclopramide là FDA category B. Nghiên cứu trên động vật không cho thấy nguy cơ cho thai nhi. Một số nghiên cứu trên người không cho thấy tăng nguy cơ dị tật bẩm sinh. Có thể dùng trong thai kỳ nếu lợi ích > nguy cơ. Thường dùng để điều trị buồn nôn, nôn trong thai kỳ (hyperemesis gravidarum).",
            "lactation": {
                "safety": "Compatible",
                "details": "Metoclopramide bài tiết vào sữa mẹ ở nồng độ thấp. Có thể dùng để tăng tiết sữa mẹ (off-label). An toàn khi cho con bú.",
                "recommendation": "Có thể dùng khi cho con bú. Dùng liều thường dùng."
            }
        },
        "hepatic_adjustment": {
            "mild": "Không cần chỉnh liều",
            "moderate": "Thận trọng, có thể giảm liều",
            "severe": "Thận trọng, giảm liều. Metoclopramide chuyển hóa ở gan qua CYP2D6. Suy gan nặng làm giảm chuyển hóa.",
            "notes": "Metoclopramide chuyển hóa ở gan. Suy gan nặng làm tăng nồng độ. Thận trọng, giảm liều ở suy gan nặng."
        },
        "overdose_management": {
            "symptoms": [
                "Rối loạn vận động nặng: dystonia, parkinsonism, akathisia",
                "Buồn ngủ, lú lẫn",
                "Hội chứng serotonin (nếu dùng với SSRI/SNRI): kích động, tăng thân nhiệt, co giật",
                "Rối loạn nhịp tim (hiếm)"
            ],
            "antidote": "Không có antidote đặc hiệu. Dùng diphenhydramine hoặc benztropine để điều trị dystonia.",
            "treatment": [
                "Điều trị rối loạn vận động: diphenhydramine 25-50mg IV/IM hoặc benztropine 1-2mg IV/IM",
                "Hỗ trợ triệu chứng",
                "Theo dõi dấu hiệu sinh tồn",
                "Điều trị hội chứng serotonin nếu có: cyproheptadine, cooling, benzodiazepines"
            ],
            "monitoring": "Theo dõi dấu hiệu sinh tồn, dấu hiệu rối loạn vận động, dấu hiệu hội chứng serotonin"
        },
        "reversal_agents": None,
        "administration_instructions": {
            "oral": {
                "with_food": "Uống 30 phút trước bữa ăn (để tăng hiệu quả prokinetic)",
                "timing": "Uống 30 phút trước bữa ăn và trước khi đi ngủ. Có thể uống với hoặc không với thức ăn."
            },
            "iv": {
                "reconstitution": "Metoclopramide IV: 10mg pha với 10-20ml NaCl 0.9% hoặc dextrose 5%",
                "infusion_rate": "Truyền trong 15-30 phút (bolus) hoặc tiêm tĩnh mạch chậm",
                "compatibility": ["NaCl 0.9%", "Dextrose 5%"],
                "incompatibility": ["Không pha với các thuốc khác trong cùng đường truyền"],
                "notes": "IV nhanh hơn PO. Chỉ dùng IV khi không uống được. Chuyển sang PO sớm nhất có thể."
            }
        },
        "references": {
            "primary_sources": [
                "FDA Drug Label - Metoclopramide",
                "UpToDate - Metoclopramide: Drug information",
                "Micromedex - Metoclopramide",
                "Goodman & Gilman's The Pharmacological Basis of Therapeutics",
                "FDA Black Box Warning - Tardive dyskinesia risk"
            ],
            "last_updated": "2024-12-19",
            "evidence_level": "High - FDA approved, multiple RCTs, black box warning"
        }
      },
      "Loperamide": {
        "group": "Gastrointestinal - Antidiarrheal",
        "vietnamese_name": "Loperamide, Imodium",
        "administration": ["PO"],
        "indications": [
            "Tiêu chảy cấp",
            "Tiêu chảy mạn tính"
        ],
        "contraindications": [
            "Tiêu chảy do nhiễm khuẩn (nặng)",
            "Viêm đại tràng giả mạc",
            "Tắc ruột",
            "Trẻ em <2 tuổi"
        ],
        "dosage": {
            "adult_loading": "4mg x 1 lần",
            "adult_maintenance": "2mg sau mỗi lần đi ngoài (tối đa 16mg/ngày)",
            "notes": "Không dùng quá 48 giờ nếu không cải thiện"
        },
        "side_effects": [
            "Táo bón",
            "Buồn nôn",
            "Đau bụng",
            "Buồn ngủ"
        ],
        "interactions": [
            "Opioids: tăng tác dụng (ít dùng chung)"
        ],
        "pregnancy": "C",
        "mechanism_of_action": "Opioid mu-receptor agonist ở ruột (peripheral opioid). Ức chế acetylcholine và prostaglandin ở cơ trơn ruột, giảm nhu động ruột, tăng trương lực cơ thắt hậu môn, tăng hấp thu nước từ phân. Tác dụng chống tiêu chảy. Không qua hàng rào máu-não đáng kể ở liều điều trị → ít tác dụng phụ thần kinh và ít nguy cơ nghiện hơn opioid hệ thống. Tuy nhiên, liều cao có thể qua hàng rào máu-não và gây tác dụng opioid hệ thống.",
        "monitoring": [
            "Đáp ứng lâm sàng (giảm tần suất đi ngoài, cải thiện tính chất phân)",
            "Dấu hiệu quá liều: ức chế hô hấp, giảm ý thức, co đồng tử (miosis)",
            "Dấu hiệu táo bón nặng (có thể gây tắc ruột giả)",
            "Dấu hiệu nhiễm khuẩn (nếu giữ vi khuẩn trong ruột quá lâu)",
            "Dấu hiệu viêm đại tràng giả mạc (tiêu chảy nặng, đau bụng, sốt) - nguy cơ nếu dùng với kháng sinh"
        ],
        "precautions": [
            "Chỉ dùng cho tiêu chảy không nhiễm khuẩn hoặc đã điều trị nhiễm khuẩn",
            "Không dùng quá 48 giờ nếu không cải thiện (cần đánh giá lại nguyên nhân)",
            "Không dùng cho tiêu chảy nhiễm khuẩn nặng (có thể giữ vi khuẩn trong ruột)",
            "Không dùng cho viêm đại tràng giả mạc (có thể làm nặng thêm)",
            "Không dùng cho trẻ em <2 tuổi (nguy cơ ức chế hô hấp)",
            "Không vượt quá 16mg/ngày (tăng nguy cơ tác dụng phụ hệ thống)",
            "Ngừng ngay nếu có dấu hiệu quá liều (ức chế hô hấp, giảm ý thức)",
            "Thận trọng ở bệnh nhân suy gan (giảm chuyển hóa)",
            "Thận trọng ở bệnh nhân suy thận (tích lũy)",
            "Nếu dùng với kháng sinh → tăng nguy cơ viêm đại tràng giả mạc"
        ],
        "pharmacokinetics": {
            "half_life": "7-14 giờ",
            "onset": "1-2 giờ",
            "duration": "4-6 giờ",
            "protein_binding": "97%",
            "metabolism": "Gan (chuyển hóa qua CYP3A4, CYP2C8)",
            "clearance": "Gan (chuyển hóa), thận (thải trừ)"
        },
        "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm, tránh ánh sáng. Để xa tầm tay trẻ em (nguy cơ quá liều).",
        "black_box_warnings": "Liều cao có thể gây ức chế hô hấp nặng, có thể tử vong, đặc biệt ở trẻ em. Không dùng quá liều khuyến cáo (16mg/ngày). Không dùng cho trẻ em <2 tuổi. Không dùng cho tiêu chảy nhiễm khuẩn nặng - có thể giữ vi khuẩn trong ruột và làm nặng bệnh. Ngừng ngay nếu có dấu hiệu quá liều.",
        "drug_interactions": {
            "major": [
                {
                    "drug": "Opioids (morphine, codeine, fentanyl, etc.)",
                    "mechanism": "Tác dụng hiệp đồng ức chế opioid mu-receptor",
                    "effect": "Tăng nguy cơ ức chế hô hấp, tăng nguy cơ tác dụng phụ opioid hệ thống",
                    "management": "Tránh dùng cùng. Thận trọng nếu phải dùng cùng (giảm liều cả hai)."
                }
            ],
            "moderate": [
                {
                    "drug": "CYP3A4 inhibitors (ketoconazole, itraconazole, ritonavir, clarithromycin)",
                    "mechanism": "Ức chế chuyển hóa loperamide qua CYP3A4",
                    "effect": "Tăng nồng độ loperamide, tăng nguy cơ tác dụng phụ hệ thống (ức chế hô hấp)",
                    "management": "Tránh dùng cùng hoặc giảm liều loperamide. Theo dõi dấu hiệu quá liều."
                },
                {
                    "drug": "CYP2C8 inhibitors (gemfibrozil)",
                    "mechanism": "Ức chế chuyển hóa loperamide",
                    "effect": "Tăng nồng độ loperamide",
                    "management": "Thận trọng, giảm liều loperamide"
                }
            ],
            "minor": []
        },
        "contraindications": {
            "absolute": [
                "Dị ứng loperamide",
                "Tiêu chảy nhiễm khuẩn nặng (C. difficile, E. coli O157:H7) - có thể giữ vi khuẩn trong ruột",
                "Viêm đại tràng giả mạc - có thể làm nặng thêm",
                "Tắc ruột cơ học",
                "Trẻ em <2 tuổi - nguy cơ ức chế hô hấp",
                "Liều cao với CYP3A4 inhibitors - CHỐNG CHỈ ĐỊNH"
            ],
            "relative": [
                "Suy gan nặng - giảm liều, tăng nguy cơ tích lũy",
                "Suy thận nặng - giảm liều, tăng nguy cơ tích lũy",
                "Tiêu chảy nhiễm khuẩn nhẹ - thận trọng, đã điều trị kháng sinh",
                "Trẻ em 2-6 tuổi - thận trọng, giảm liều",
                "Đang dùng opioids - tăng nguy cơ tác dụng phụ"
            ]
        },
        "pregnancy_lactation": {
            "fda_category": "C",
            "pregnancy_details": "Loperamide là FDA category C. Nghiên cứu trên động vật cho thấy có thể gây độc tính cho thai nhi ở liều cao. Không có nghiên cứu đầy đủ trên người. Có thể dùng trong thai kỳ nếu lợi ích > nguy cơ, nhưng nên tránh trong tam cá nguyệt đầu nếu có thể. Dùng liều thấp nhất có hiệu quả.",
            "lactation": {
                "safety": "Compatible",
                "details": "Loperamide bài tiết vào sữa mẹ ở nồng độ thấp. An toàn khi cho con bú ở liều điều trị.",
                "recommendation": "Có thể dùng khi cho con bú. Dùng liều thường dùng."
            }
        },
        "hepatic_adjustment": {
            "mild": "Không cần chỉnh liều",
            "moderate": "Giảm liều 50%",
            "severe": "Giảm liều 50% hoặc tránh dùng. Loperamide chuyển hóa ở gan qua CYP3A4 và CYP2C8. Suy gan nặng làm giảm chuyển hóa, tăng nguy cơ tích lũy và tác dụng phụ hệ thống.",
            "notes": "Loperamide chuyển hóa ở gan. Suy gan nặng làm tăng nồng độ, tăng nguy cơ ức chế hô hấp. Giảm liều hoặc tránh dùng ở suy gan nặng."
        },
        "overdose_management": {
            "symptoms": [
                "Ức chế hô hấp nặng (triệu chứng chính, có thể tử vong)",
                "Giảm ý thức, hôn mê",
                "Co đồng tử (miosis)",
                "Táo bón nặng, tắc ruột",
                "Buồn nôn, nôn",
                "Buồn ngủ, lú lẫn"
            ],
            "antidote": "Naloxone (opioid antagonist) - có thể đảo ngược ức chế hô hấp",
            "treatment": [
                "Naloxone 0.4-2mg IV/IM/SC, lặp lại mỗi 2-3 phút nếu cần (tối đa 10mg)",
                "Hỗ trợ hô hấp: thông khí, oxy, nếu cần đặt nội khí quản",
                "Theo dõi dấu hiệu sinh tồn chặt chẽ",
                "Activated charcoal nếu uống trong vòng 1-2 giờ",
                "Điều trị tắc ruột nếu có"
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
                "timing": "Liều đầu: 4mg. Sau đó: 2mg sau mỗi lần đi ngoài (tối đa 16mg/ngày). Không dùng quá 48 giờ nếu không cải thiện."
            },
            "iv": {
                "reconstitution": "Loperamide chỉ có dạng uống (PO)",
                "infusion_rate": "N/A",
                "compatibility": [],
                "incompatibility": [],
                "notes": "Loperamide chỉ có dạng uống, không có dạng IV"
            }
        },
        "references": {
            "primary_sources": [
                "FDA Drug Label - Loperamide",
                "UpToDate - Loperamide: Drug information",
                "Micromedex - Loperamide",
                "Goodman & Gilman's The Pharmacological Basis of Therapeutics",
                "FDA Safety Communication - Loperamide abuse and overdose (2016)"
            ],
            "last_updated": "2024-12-19",
            "evidence_level": "High - FDA approved, multiple RCTs, safety warnings"
        }
    },
    "Domperidone": {
        "group": "Gastrointestinal - Prokinetic, Antiemetic",
        "vietnamese_name": "Domperidone, Motilium",
        "administration": ["PO"],
        "indications": [
            "Buồn nôn, nôn",
            "Liệt dạ dày (gastroparesis)",
            "Ợ nóng",
            "Trào ngược dạ dày thực quản"
        ],
        "contraindications": [
            "Dị ứng domperidone",
            "Chảy máu dạ dày",
            "Tắc ruột cơ học",
            "Prolactinoma",
            "Dùng với các thuốc QT kéo dài"
        ],
        "dosage": {
            "adult_nausea": "10-20mg x 3-4 lần/ngày, uống trước bữa ăn",
            "adult_gastroparesis": "10mg x 3-4 lần/ngày trước bữa ăn",
            "adult_max": "80mg/ngày",
            "notes": "Không qua hàng rào máu-não nên ít tác dụng phụ thần kinh hơn metoclopramide"
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "Thận trọng, giảm liều",
            "under_30": "Thận trọng, giảm liều 50%"
        },
        "side_effects": [
            "Rối loạn kinh nguyệt",
            "Tăng prolactin",
            "Đau vú",
            "Chảy sữa (galactorrhea)",
            "QT kéo dài (liều cao)",
            "Nhức đầu"
        ],
        "interactions": [
            "QT kéo dài: tránh dùng với thuốc QT kéo dài (amiodarone, quinolone)",
            "Ketoconazole: tăng nồng độ domperidone",
            "Erythromycin: tăng nồng độ domperidone"
        ],
        "pregnancy": "C",
        "mechanism_of_action": "Dopamine D2 receptor antagonist ở ngoại vi (ruột và chemoreceptor trigger zone). Ức chế dopamine → tăng nhu động dạ dày và ruột, tăng trương lực cơ thắt dưới thực quản, tăng tốc độ làm rỗng dạ dày. Có tác dụng chống nôn do ức chế dopamine ở chemoreceptor trigger zone. KHÔNG qua hàng rào máu-não (do bị P-glycoprotein đẩy ra) → ít tác dụng phụ thần kinh hơn metoclopramide (không gây mê sảng, parkinsonism). Tăng prolactin do ức chế dopamine ở tuyến yên (dopamine ức chế tiết prolactin).",
        "monitoring": [
            "Đáp ứng lâm sàng (giảm buồn nôn, nôn, cải thiện làm rỗng dạ dày)",
            "ECG nếu dùng liều cao hoặc kéo dài (nguy cơ QT kéo dài)",
            "Dấu hiệu tăng prolactin: rối loạn kinh nguyệt, chảy sữa, đau vú",
            "Dấu hiệu QT kéo dài: loạn nhịp tim, chóng mặt, ngất",
            "Dấu hiệu tác dụng phụ thần kinh (hiếm nhưng có thể xảy ra nếu tích lũy)"
        ],
        "precautions": [
            "Uống trước bữa ăn 15-30 phút (tăng hiệu quả)",
            "Không vượt quá 80mg/ngày (tăng nguy cơ QT kéo dài)",
            "Tránh dùng với các thuốc kéo dài QT (amiodarone, quinolone, macrolide) - tăng nguy cơ loạn nhịp",
            "Thận trọng ở suy thận (giảm liều)",
            "Thận trọng ở suy gan (giảm liều)",
            "Theo dõi dấu hiệu tăng prolactin (rối loạn kinh nguyệt, chảy sữa)",
            "Ngừng nếu có dấu hiệu QT kéo dài hoặc loạn nhịp",
            "Ít tác dụng phụ thần kinh hơn metoclopramide (không qua hàng rào máu-não)",
            "Không dùng trong prolactinoma (tăng prolactin có thể làm tăng kích thước u)"
        ],
        "pharmacokinetics": {
            "half_life": "7-9 giờ",
            "onset": "30-60 phút",
            "duration": "4-8 giờ",
            "protein_binding": "91-93%",
            "metabolism": "Gan (chuyển hóa qua CYP3A4), CYP1A2",
            "clearance": "Gan (chuyển hóa), thận (thải trừ)"
        },
        "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm, tránh ánh sáng",
        "black_box_warnings": "Nguy cơ QT kéo dài và loạn nhịp tim nghiêm trọng (torsades de pointes), có thể tử vong. Nguy cơ tăng ở liều cao (>80mg/ngày), suy thận, suy gan, hoặc dùng với các thuốc kéo dài QT. Không vượt quá 80mg/ngày. Tránh dùng với các thuốc kéo dài QT.",
        "drug_interactions": {
            "major": [
                {
                    "drug": "Thuốc kéo dài QT (amiodarone, quinolone, macrolide, haloperidol, etc.)",
                    "mechanism": "Tác dụng hiệp đồng kéo dài QT interval",
                    "effect": "Tăng nguy cơ QT kéo dài, torsades de pointes, loạn nhịp tim, có thể tử vong",
                    "management": "CHỐNG CHỈ ĐỊNH dùng cùng. Tránh dùng domperidone với các thuốc kéo dài QT."
                }
            ],
            "moderate": [
                {
                    "drug": "CYP3A4 inhibitors (ketoconazole, itraconazole, ritonavir, clarithromycin, erythromycin)",
                    "mechanism": "Ức chế chuyển hóa domperidone qua CYP3A4",
                    "effect": "Tăng nồng độ domperidone, tăng nguy cơ QT kéo dài",
                    "management": "Tránh dùng cùng hoặc giảm liều domperidone. Theo dõi ECG."
                },
                {
                    "drug": "Anticholinergics",
                    "mechanism": "Đối kháng tác dụng prokinetic",
                    "effect": "Giảm hiệu quả prokinetic",
                    "management": "Tránh dùng cùng nếu có thể"
                }
            ],
            "minor": []
        },
        "contraindications": {
            "absolute": [
                "Dị ứng domperidone",
                "Chảy máu dạ dày",
                "Tắc ruột cơ học",
                "Prolactinoma",
                "Dùng với các thuốc kéo dài QT - CHỐNG CHỈ ĐỊNH tuyệt đối",
                "QT kéo dài (QTc >450ms ở nam, >470ms ở nữ) - CHỐNG CHỈ ĐỊNH"
            ],
            "relative": [
                "Suy thận nặng (CrCl <30) - giảm liều 50%",
                "Suy gan nặng - giảm liều, tăng nguy cơ QT kéo dài",
                "Hạ kali, hạ magie - tăng nguy cơ QT kéo dài",
                "Người già - thận trọng, giảm liều",
                "Rối loạn nhịp tim - thận trọng"
            ]
        },
        "pregnancy_lactation": {
            "fda_category": "C",
            "pregnancy_details": "Domperidone là FDA category C. Nghiên cứu trên động vật cho thấy có thể gây độc tính cho thai nhi. Không có nghiên cứu đầy đủ trên người. Có thể dùng trong thai kỳ nếu lợi ích > nguy cơ, nhưng nên tránh trong tam cá nguyệt đầu nếu có thể.",
            "lactation": {
                "safety": "Compatible",
                "details": "Domperidone bài tiết vào sữa mẹ ở nồng độ thấp. Có thể dùng để tăng tiết sữa mẹ (off-label). An toàn khi cho con bú.",
                "recommendation": "Có thể dùng khi cho con bú. Dùng liều thường dùng (10-20mg x 3-4 lần/ngày)."
            }
        },
        "hepatic_adjustment": {
            "mild": "Không cần chỉnh liều",
            "moderate": "Thận trọng, có thể giảm liều",
            "severe": "Giảm liều hoặc tránh dùng. Domperidone chuyển hóa ở gan qua CYP3A4. Suy gan nặng làm giảm chuyển hóa, tăng nồng độ, tăng nguy cơ QT kéo dài.",
            "notes": "Domperidone chuyển hóa ở gan. Suy gan nặng làm tăng nồng độ, tăng nguy cơ QT kéo dài. Giảm liều hoặc tránh dùng ở suy gan nặng."
        },
        "overdose_management": {
            "symptoms": [
                "QT kéo dài, torsades de pointes, loạn nhịp tim (triệu chứng chính, có thể tử vong)",
                "Tăng prolactin: rối loạn kinh nguyệt, chảy sữa",
                "Buồn nôn, nôn",
                "Nhức đầu"
            ],
            "antidote": "Không có antidote đặc hiệu",
            "treatment": [
                "Theo dõi ECG liên tục (QT interval)",
                "Điều trị torsades de pointes nếu có: magnesium sulfate 2g IV, pacing nếu cần",
                "Bổ sung kali, magie nếu thiếu",
                "Hỗ trợ triệu chứng",
                "Theo dõi dấu hiệu sinh tồn chặt chẽ"
            ],
            "monitoring": "Theo dõi ECG liên tục (QT interval), dấu hiệu sinh tồn, điện giải"
        },
        "reversal_agents": None,
        "administration_instructions": {
            "oral": {
                "with_food": "Uống 15-30 phút TRƯỚC bữa ăn (tăng hiệu quả)",
                "timing": "Uống 15-30 phút trước bữa ăn và trước khi đi ngủ. Không vượt quá 80mg/ngày."
            },
            "iv": {
                "reconstitution": "Domperidone chỉ có dạng uống (PO)",
                "infusion_rate": "N/A",
                "compatibility": [],
                "incompatibility": [],
                "notes": "Domperidone chỉ có dạng uống, không có dạng IV"
            }
        },
        "references": {
            "primary_sources": [
                "FDA Drug Label - Domperidone (Note: Not FDA approved in US, available in other countries)",
                "UpToDate - Domperidone: Drug information",
                "Micromedex - Domperidone",
                "European Medicines Agency - Domperidone safety review",
                "Goodman & Gilman's The Pharmacological Basis of Therapeutics"
            ],
            "last_updated": "2024-12-19",
            "evidence_level": "High - Multiple RCTs, safety warnings (QT prolongation)"
        }
    },
    "Ondansetron": {
        "group": "Gastrointestinal - Antiemetic (5-HT3 Antagonist)",
        "vietnamese_name": "Ondansetron, Zofran",
        "administration": ["PO", "IV", "IM"],
        "indications": [
            "Buồn nôn, nôn sau hóa trị",
            "Buồn nôn, nôn sau phẫu thuật",
            "Buồn nôn, nôn do xạ trị",
            "Buồn nôn, nôn do nhiều nguyên nhân"
        ],
        "contraindications": [
            "Dị ứng ondansetron",
            "QT kéo dài",
            "Dùng với apomorphine"
        ],
        "dosage": {
            "adult_po": "8mg x 2-3 lần/ngày",
            "adult_iv_im": "4-8mg x 2-3 lần/ngày",
            "adult_chemotherapy": "8mg IV trước hóa trị, sau đó 8mg PO x 2 lần/ngày x 3 ngày",
            "adult_surgery": "4mg IV trước khi gây mê",
            "notes": "Rất hiệu quả cho buồn nôn do hóa trị và phẫu thuật"
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "Không đổi",
            "under_30": "Không đổi"
        },
        "side_effects": [
            "QT kéo dài",
            "Nhức đầu",
            "Chóng mặt",
            "Táo bón",
            "Mệt mỏi"
        ],
        "interactions": [
            "Apomorphine: chống chỉ định",
            "Thuốc QT kéo dài: tăng nguy cơ loạn nhịp",
            "CYP2D6 inhibitors: tăng nồng độ ondansetron"
        ],
        "pregnancy": "B",
        "mechanism_of_action": "5-HT3 (serotonin) receptor antagonist. Ức chế chọn lọc receptor 5-HT3 ở ngoại vi (dây thần kinh phế vị) và trung ương (chemoreceptor trigger zone trong area postrema). Ngăn cản tác dụng của serotonin, dẫn đến giảm nôn và buồn nôn. Được dùng trong dự phòng và điều trị nôn do hóa trị, xạ trị, và sau phẫu thuật. Hiệu quả hơn metoclopramide và không gây tác dụng phụ ngoại tháp như metoclopramide.",
        "monitoring": [
            "Tần suất nôn và buồn nôn",
            "ECG (QT kéo dài - nguy cơ rối loạn nhịp tim, đặc biệt ở liều cao)",
            "Điện giải (kali, magie) - hạ kali, hạ magie tăng nguy cơ QT kéo dài",
            "Dấu hiệu tắc ruột (ondansetron có thể che dấu triệu chứng)",
            "Chức năng gan (ALT, AST) - hiếm tăng men gan"
        ],
        "precautions": [
            "QT kéo dài → không dùng ở bệnh nhân có QT kéo dài, rối loạn nhịp tim, hoặc dùng các thuốc kéo dài QT khác",
            "Nguy cơ tăng ở liều cao (> 16mg đơn liều), hạ kali, hạ magie, suy gan",
            "Có thể che dấu triệu chứng tắc ruột - thận trọng ở bệnh nhân có nguy cơ",
            "Giảm liều ở suy gan nặng (giảm chuyển hóa)",
            "Liều thường: 4-8mg (PO/IV), có thể lặp lại mỗi 8 giờ",
            "Liều tối đa: 32mg/ngày (để giảm nguy cơ QT kéo dài)",
            "Có thể dùng trước hóa trị/xạ trị để dự phòng",
            "An toàn trong thai kỳ (category B)"
        ],
        "pharmacokinetics": {
            "half_life": "3-6 giờ (bình thường), kéo dài ở suy gan",
            "onset": "30 phút (PO), ngay lập tức (IV)",
            "duration": "4-8 giờ",
            "protein_binding": "70-76%",
            "metabolism": "Gan (CYP1A2, CYP2D6, CYP3A4) - chuyển hóa mạnh",
            "clearance": "Chủ yếu qua gan, cần điều chỉnh ở suy gan"
        },
        "storage": "Bảo quản ở nhiệt độ phòng (20-25°C), tránh ẩm. Dung dịch tiêm: bảo quản ở nhiệt độ phòng, tránh ánh sáng.",
        "black_box_warnings": "Nguy cơ QT kéo dài, có thể gây rối loạn nhịp tim nghiêm trọng (torsades de pointes), có thể tử vong. Nguy cơ tăng ở liều cao, hạ kali, hạ magie, suy gan, hoặc dùng với các thuốc kéo dài QT khác. Không dùng vượt quá liều khuyến cáo.",
        "drug_interactions": {
            "major": [
                {
                    "drug": "Apomorphine",
                    "mechanism": "Ondansetron ức chế 5-HT3 receptor, đối kháng với apomorphine",
                    "effect": "Giảm hiệu quả apomorphine, có thể gây hạ huyết áp nặng",
                    "management": "CHỐNG CHỈ ĐỊNH dùng cùng. Không dùng ondansetron với apomorphine."
                }
            ],
            "moderate": [
                {
                    "drug": "Thuốc kéo dài QT (amiodarone, quinolone, macrolide, haloperidol, etc.)",
                    "mechanism": "Tác dụng hiệp đồng kéo dài QT interval",
                    "effect": "Tăng nguy cơ QT kéo dài, torsades de pointes, loạn nhịp tim",
                    "management": "Tránh dùng cùng hoặc thận trọng. Theo dõi ECG. Giảm liều ondansetron."
                },
                {
                    "drug": "CYP2D6 inhibitors (fluoxetine, paroxetine, quinidine)",
                    "mechanism": "Ức chế chuyển hóa ondansetron qua CYP2D6",
                    "effect": "Tăng nồng độ ondansetron, tăng nguy cơ QT kéo dài",
                    "management": "Thận trọng, giảm liều ondansetron nếu cần"
                }
            ],
            "minor": []
        },
        "contraindications": {
            "absolute": [
                "Dị ứng ondansetron",
                "Dùng với apomorphine - CHỐNG CHỈ ĐỊNH tuyệt đối",
                "QT kéo dài (QTc >450ms ở nam, >470ms ở nữ) - CHỐNG CHỈ ĐỊNH"
            ],
            "relative": [
                "Suy gan nặng - giảm liều 50% (tối đa 8mg/ngày)",
                "Hạ kali, hạ magie - tăng nguy cơ QT kéo dài, bổ sung trước khi dùng",
                "Đang dùng thuốc kéo dài QT - thận trọng, giảm liều",
                "Người già - thận trọng, giảm liều",
                "Rối loạn nhịp tim - thận trọng"
            ]
        },
        "pregnancy_lactation": {
            "fda_category": "B",
            "pregnancy_details": "Ondansetron là FDA category B. Nghiên cứu trên động vật không cho thấy nguy cơ cho thai nhi. Một số nghiên cứu trên người không cho thấy tăng nguy cơ dị tật bẩm sinh. Có thể dùng trong thai kỳ nếu lợi ích > nguy cơ. Thường dùng để điều trị buồn nôn, nôn trong thai kỳ (hyperemesis gravidarum).",
            "lactation": {
                "safety": "Compatible",
                "details": "Ondansetron bài tiết vào sữa mẹ ở nồng độ thấp. An toàn khi cho con bú.",
                "recommendation": "Có thể dùng khi cho con bú. Dùng liều thường dùng."
            }
        },
        "hepatic_adjustment": {
            "mild": "Không cần chỉnh liều",
            "moderate": "Giảm liều 50% (tối đa 8mg/ngày)",
            "severe": "Giảm liều 50% (tối đa 8mg/ngày). Ondansetron chuyển hóa ở gan qua CYP1A2, CYP2D6, CYP3A4. Suy gan nặng làm giảm chuyển hóa, tăng nồng độ, tăng nguy cơ QT kéo dài.",
            "notes": "Ondansetron chuyển hóa ở gan. Suy gan nặng làm tăng nồng độ, tăng nguy cơ QT kéo dài. Giảm liều ở suy gan trung bình và nặng."
        },
        "overdose_management": {
            "symptoms": [
                "QT kéo dài, torsades de pointes, loạn nhịp tim (triệu chứng chính, có thể tử vong)",
                "Nhức đầu, chóng mặt",
                "Buồn nôn, nôn",
                "Mệt mỏi"
            ],
            "antidote": "Không có antidote đặc hiệu",
            "treatment": [
                "Theo dõi ECG liên tục (QT interval)",
                "Điều trị torsades de pointes nếu có: magnesium sulfate 2g IV, pacing nếu cần",
                "Bổ sung kali, magie nếu thiếu",
                "Hỗ trợ triệu chứng",
                "Theo dõi dấu hiệu sinh tồn chặt chẽ"
            ],
            "monitoring": "Theo dõi ECG liên tục (QT interval), dấu hiệu sinh tồn, điện giải"
        },
        "reversal_agents": None,
        "administration_instructions": {
            "oral": {
                "with_food": "Có thể uống với hoặc không với thức ăn",
                "timing": "Uống 30 phút trước hóa trị/xạ trị/phẫu thuật (dự phòng) hoặc ngay khi có buồn nôn. Có thể lặp lại mỗi 8 giờ. Tối đa 32mg/ngày."
            },
            "iv": {
                "reconstitution": "Ondansetron IV: 4-8mg pha với 50ml NaCl 0.9% hoặc dextrose 5%",
                "infusion_rate": "Truyền trong 15 phút",
                "compatibility": ["NaCl 0.9%", "Dextrose 5%"],
                "incompatibility": ["Không pha với các thuốc khác trong cùng đường truyền"],
                "notes": "Có thể tiêm IV trực tiếp chậm (2-5 phút) hoặc truyền. Chỉ dùng IV khi không uống được. Chuyển sang PO sớm nhất có thể."
            }
        },
        "references": {
            "primary_sources": [
                "FDA Drug Label - Ondansetron",
                "UpToDate - Ondansetron: Drug information",
                "Micromedex - Ondansetron",
                "Goodman & Gilman's The Pharmacological Basis of Therapeutics",
                "FDA Safety Communication - Ondansetron QT prolongation (2012)"
            ],
            "last_updated": "2024-12-19",
            "evidence_level": "High - FDA approved, multiple RCTs, safety warnings (QT prolongation)"
        }
    },
    "Lansoprazole": {
        "group": "Gastrointestinal - Proton Pump Inhibitor (PPI)",
        "vietnamese_name": "Lansoprazole, Prevacid",
        "administration": ["PO"],
        "indications": [
            "Loét dạ dày tá tràng",
            "Trào ngược dạ dày thực quản (GERD)",
            "Hội chứng Zollinger-Ellison",
            "Tiệt trừ H. pylori (kết hợp)"
        ],
        "contraindications": [
            "Dị ứng lansoprazole/PPI"
        ],
        "dosage": {
            "adult_ulcer": "15-30mg x 1 lần/ngày",
            "adult_gerd": "15-30mg x 1 lần/ngày",
            "adult_h_pylori": "30mg x 2 lần/ngày (với amoxicillin + clarithromycin)",
            "notes": "Uống trước bữa ăn 30 phút. Viên tan trong miệng không cần nước"
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "Không đổi",
            "under_30": "Không đổi"
        },
        "side_effects": [
            "Đau đầu",
            "Tiêu chảy",
            "Đau bụng",
            "Tăng nguy cơ nhiễm trùng (Clostridium difficile)",
            "Loãng xương (dùng lâu dài)",
            "Thiếu vitamin B12 (dùng lâu dài)",
            "Thiếu magie (hiếm)"
        ],
        "interactions": [
            "Warfarin: tăng nhẹ nguy cơ chảy máu",
            "Digoxin: tăng nhẹ nồng độ digoxin",
            "Ketoconazole/Itraconazole: giảm hấp thu (giảm acid dạ dày)",
            "Methotrexate: tăng nồng độ methotrexate"
        ],
        "pregnancy": "B",
        "mechanism_of_action": "Ức chế không hồi phục enzyme H+/K+-ATPase (proton pump) ở tế bào thành dạ dày, ức chế bước cuối cùng trong quá trình tiết acid dạ dày. Ức chế cả acid kích thích và acid cơ bản. Cần chuyển hóa ở gan thành dạng hoạt động (sulfenamide). Tác dụng mạnh hơn H2 blocker. Thời gian bán thải ngắn nhưng tác dụng kéo dài do ức chế không hồi phục enzyme.",
        "monitoring": [
            "Đáp ứng lâm sàng (giảm đau, triệu chứng GERD)",
            "Magie máu nếu dùng lâu dài (>1 năm) - có thể giảm magie",
            "Vitamin B12 nếu dùng lâu dài (>2 năm) - có thể thiếu B12",
            "Mật độ xương (DEXA scan) nếu dùng lâu dài và có nguy cơ loãng xương",
            "Dấu hiệu nhiễm C. difficile (tiêu chảy nặng, đau bụng) - tăng nguy cơ",
            "Chức năng thận (nếu dùng lâu dài với nguy cơ suy thận)"
        ],
        "precautions": [
            "Uống trước bữa ăn 30 phút (tăng hiệu quả)",
            "Viên tan trong miệng: đặt trên lưỡi, để tan tự nhiên, không cần nước",
            "Không nghiền hoặc nhai viên (bao tan trong ruột)",
            "Dùng liều thấp nhất hiệu quả, thời gian ngắn nhất có thể",
            "Cân nhắc ngừng sau 4-8 tuần nếu không cần thiết (giảm nguy cơ tác dụng phụ)",
            "Cân nhắc dùng liều cách ngày hoặc ngắt quãng nếu dùng lâu dài",
            "Thận trọng ở bệnh nhân suy gan nặng (giảm liều)",
            "Không dùng với các thuốc cần acid để hấp thu (ketoconazole, itraconazole, iron salts)"
        ],
        "pharmacokinetics": {
            "half_life": "1-2 giờ (ngắn, nhưng tác dụng kéo dài do ức chế không hồi phục)",
            "onset": "1-3 giờ",
            "duration": "24 giờ (một lần/ngày)",
            "protein_binding": "97%",
            "clearance": "Gan (chuyển hóa qua CYP2C19, CYP3A4), thận (thải trừ)"
        },
        "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm, tránh ánh sáng. Viên tan trong miệng: bảo quản trong bao bì gốc, tránh ẩm.",
        "black_box_warnings": "Dùng lâu dài (>1 năm) có thể tăng nguy cơ loãng xương, gãy xương hông, cổ tay, cột sống. Dùng lâu dài có thể tăng nguy cơ thiếu vitamin B12. Tăng nguy cơ nhiễm C. difficile.",
        "drug_interactions": {
            "major": [
                {
                    "drug": "Atazanavir (HIV protease inhibitor)",
                    "mechanism": "PPI làm tăng pH dạ dày, giảm hấp thu atazanavir",
                    "effect": "Giảm nồng độ atazanavir, giảm hiệu quả điều trị HIV",
                    "management": "CHỐNG CHỈ ĐỊNH dùng cùng. Không dùng lansoprazole với atazanavir."
                }
            ],
            "moderate": [
                {
                    "drug": "Warfarin",
                    "mechanism": "Lansoprazole ức chế CYP2C9 nhẹ",
                    "effect": "Tăng INR nhẹ, tăng nguy cơ chảy máu",
                    "management": "Theo dõi INR thường xuyên. Điều chỉnh liều warfarin nếu cần."
                },
                {
                    "drug": "Digoxin",
                    "mechanism": "Lansoprazole có thể tăng nồng độ digoxin nhẹ",
                    "effect": "Tăng nồng độ digoxin nhẹ",
                    "management": "Theo dõi nồng độ digoxin. Thận trọng."
                },
                {
                    "drug": "Methotrexate (liều cao)",
                    "mechanism": "PPI giảm thải trừ methotrexate qua thận",
                    "effect": "Tăng nồng độ methotrexate, tăng nguy cơ độc tính",
                    "management": "Thận trọng. Tạm ngừng PPI khi dùng methotrexate liều cao."
                },
                {
                    "drug": "Ketoconazole, Itraconazole, Posaconazole",
                    "mechanism": "PPI tăng pH dạ dày, giảm hấp thu azole antifungals",
                    "effect": "Giảm nồng độ azole, giảm hiệu quả điều trị",
                    "management": "Cách thời gian ít nhất 2 giờ."
                },
                {
                    "drug": "Iron salts, Vitamin B12",
                    "mechanism": "PPI giảm acid dạ dày, giảm hấp thu",
                    "effect": "Giảm hấp thu sắt và B12",
                    "management": "Cách thời gian ít nhất 2 giờ. Bổ sung B12 nếu dùng lâu dài."
                }
            ],
            "minor": []
        },
        "contraindications": {
            "absolute": [
                "Dị ứng lansoprazole hoặc PPI khác",
                "Dùng cùng atazanavir (HIV protease inhibitor)"
            ],
            "relative": [
                "Suy gan nặng (Child-Pugh C) - giảm liều tối đa 15mg/ngày",
                "Suy thận nặng (CrCl <30) - không cần chỉnh liều nhưng thận trọng",
                "Loãng xương - tăng nguy cơ gãy xương khi dùng lâu dài",
                "Nhiễm C. difficile - tăng nguy cơ",
                "Thiếu vitamin B12 - bổ sung nếu dùng lâu dài",
                "Thiếu magnesium - bổ sung nếu dùng lâu dài"
            ]
        },
        "pregnancy_lactation": {
            "fda_category": "B",
            "pregnancy_details": "Lansoprazole là FDA category B. Nghiên cứu trên động vật không cho thấy nguy cơ cho thai nhi. Một số nghiên cứu quan sát không cho thấy tăng nguy cơ dị tật bẩm sinh. Có thể dùng trong thai kỳ nếu lợi ích > nguy cơ.",
            "lactation": {
                "safety": "Compatible",
                "details": "Lansoprazole bài tiết vào sữa mẹ ở nồng độ rất thấp. An toàn khi cho con bú.",
                "recommendation": "Có thể dùng khi cho con bú. Dùng liều thường dùng."
            }
        },
        "hepatic_adjustment": {
            "mild": "Không cần chỉnh liều",
            "moderate": "Không cần chỉnh liều, nhưng thận trọng",
            "severe": "Giảm liều tối đa 15mg/ngày (Child-Pugh C). Lansoprazole chuyển hóa ở gan qua CYP2C19 và CYP3A4.",
            "notes": "Suy gan nặng làm giảm chuyển hóa, tăng nồng độ. Giảm liều ở suy gan nặng."
        },
        "overdose_management": {
            "symptoms": [
                "PPI ít gây quá liều nghiêm trọng",
                "Triệu chứng nhẹ: nhức đầu, buồn nôn, tiêu chảy"
            ],
            "antidote": "Không có antidote đặc hiệu",
            "treatment": [
                "Hỗ trợ triệu chứng",
                "Theo dõi dấu hiệu sinh tồn",
                "Hầu hết trường hợp tự khỏi"
            ],
            "monitoring": "Theo dõi dấu hiệu sinh tồn"
        },
        "reversal_agents": None,
        "administration_instructions": {
            "oral": {
                "with_food": "Uống 30 phút TRƯỚC bữa ăn (quan trọng)",
                "timing": "Uống vào buổi sáng trước bữa sáng. Viên tan trong miệng: đặt trên lưỡi, để tan tự nhiên, không cần nước. KHÔNG nghiền hoặc nhai viên bao tan trong ruột."
            },
            "iv": {
                "reconstitution": "Không có dạng IV cho lansoprazole",
                "infusion_rate": "N/A",
                "compatibility": [],
                "incompatibility": [],
                "notes": "Lansoprazole chỉ có dạng uống (PO)"
            }
        },
        "references": {
            "primary_sources": [
                "FDA Drug Label - Lansoprazole",
                "UpToDate - Proton pump inhibitors: Overview of use and adverse effects",
                "Micromedex - Lansoprazole",
                "Goodman & Gilman's The Pharmacological Basis of Therapeutics"
            ],
            "last_updated": "2024-12-19",
            "evidence_level": "High - FDA approved, multiple RCTs"
        }
    },
    "Esomeprazole": {
        "group": "Gastrointestinal - Proton Pump Inhibitor (PPI)",
        "vietnamese_name": "Esomeprazole, Nexium",
        "administration": ["PO", "IV"],
        "indications": [
            "Loét dạ dày tá tràng",
            "Trào ngược dạ dày thực quản (GERD)",
            "Hội chứng Zollinger-Ellison",
            "Tiệt trừ H. pylori (kết hợp)",
            "Loét do NSAID (dự phòng)"
        ],
        "contraindications": [
            "Dị ứng esomeprazole/PPI"
        ],
        "dosage": {
            "adult_po": "20-40mg x 1 lần/ngày",
            "adult_iv": "20-40mg x 1 lần/ngày",
            "adult_h_pylori": "20mg x 2 lần/ngày (với amoxicillin + clarithromycin)",
            "adult_gerd_healing": "40mg x 1 lần/ngày x 4-8 tuần",
            "notes": "Enantiomer của omeprazole (S-omeprazole). Uống trước bữa ăn"
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "Không đổi",
            "under_30": "Không đổi"
        },
        "side_effects": [
            "Đau đầu",
            "Tiêu chảy",
            "Đau bụng",
            "Tăng nguy cơ nhiễm trùng (C. difficile)",
            "Loãng xương (dùng lâu dài)",
            "Thiếu vitamin B12 (dùng lâu dài)",
            "Thiếu magie (hiếm)"
        ],
        "interactions": [
            "Warfarin: tăng nhẹ nguy cơ chảy máu",
            "Ketoconazole/Itraconazole: giảm hấp thu",
            "Clopidogrel: có thể giảm hiệu quả (controversial)",
            "Methotrexate: tăng nồng độ methotrexate"
        ],
        "pregnancy": "B",
        "mechanism_of_action": "Enantiomer S của omeprazole. Ức chế không hồi phục enzyme H+/K+-ATPase (proton pump) ở tế bào thành dạ dày, ức chế bước cuối cùng trong quá trình tiết acid dạ dày. Chuyển hóa qua CYP2C19 ít hơn omeprazole (racemic) → hiệu quả tốt hơn và ổn định hơn. Ức chế cả acid kích thích và acid cơ bản. Tác dụng mạnh hơn và ổn định hơn omeprazole do ít chuyển hóa qua CYP2C19.",
        "monitoring": [
            "Đáp ứng lâm sàng (giảm đau, triệu chứng GERD)",
            "Magie máu nếu dùng lâu dài (>1 năm) - có thể giảm magie",
            "Vitamin B12 nếu dùng lâu dài (>2 năm) - có thể thiếu B12",
            "Mật độ xương (DEXA scan) nếu dùng lâu dài và có nguy cơ loãng xương",
            "Dấu hiệu nhiễm C. difficile (tiêu chảy nặng, đau bụng) - tăng nguy cơ",
            "INR nếu dùng với warfarin (tăng nguy cơ chảy máu)",
            "Chức năng thận (nếu dùng lâu dài với nguy cơ suy thận)"
        ],
        "precautions": [
            "Uống trước bữa ăn 30 phút (tăng hiệu quả)",
            "Không nghiền hoặc nhai viên (bao tan trong ruột)",
            "Dùng liều thấp nhất hiệu quả, thời gian ngắn nhất có thể",
            "Cân nhắc ngừng sau 4-8 tuần nếu không cần thiết (giảm nguy cơ tác dụng phụ)",
            "Cân nhắc dùng liều cách ngày hoặc ngắt quãng nếu dùng lâu dài",
            "Thận trọng ở bệnh nhân suy gan nặng (giảm liều)",
            "Không dùng với các thuốc cần acid để hấp thu (ketoconazole, itraconazole, iron salts)",
            "Cân nhắc tương tác với clopidogrel (có thể giảm hiệu quả - controversial, cân nhắc dùng PPI khác)"
        ],
        "pharmacokinetics": {
            "half_life": "1-1.5 giờ (ngắn, nhưng tác dụng kéo dài do ức chế không hồi phục)",
            "onset": "1-3 giờ",
            "duration": "24 giờ (một lần/ngày)",
            "protein_binding": "97%",
            "clearance": "Gan (chuyển hóa qua CYP2C19 ít hơn omeprazole, CYP3A4), thận (thải trừ)"
        },
        "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm, tránh ánh sáng. Viên bao tan trong ruột: không nghiền hoặc nhai.",
        "black_box_warnings": "Dùng lâu dài (>1 năm) có thể tăng nguy cơ loãng xương, gãy xương hông, cổ tay, cột sống. Dùng lâu dài có thể tăng nguy cơ thiếu vitamin B12. Tăng nguy cơ nhiễm C. difficile.",
        "drug_interactions": {
            "major": [
                {
                    "drug": "Atazanavir (HIV protease inhibitor)",
                    "mechanism": "PPI làm tăng pH dạ dày, giảm hấp thu atazanavir",
                    "effect": "Giảm nồng độ atazanavir, giảm hiệu quả điều trị HIV",
                    "management": "CHỐNG CHỈ ĐỊNH dùng cùng. Không dùng esomeprazole với atazanavir."
                },
                {
                    "drug": "Clopidogrel",
                    "mechanism": "Esomeprazole ức chế CYP2C19, enzyme cần thiết để chuyển hóa clopidogrel",
                    "effect": "Giảm hiệu quả chống kết tập tiểu cầu của clopidogrel (controversial, nhưng nên thận trọng)",
                    "management": "Thận trọng. Cân nhắc dùng pantoprazole (ít ảnh hưởng hơn) hoặc cách thời gian."
                }
            ],
            "moderate": [
                {
                    "drug": "Warfarin",
                    "mechanism": "Esomeprazole ức chế CYP2C9 nhẹ",
                    "effect": "Tăng INR nhẹ, tăng nguy cơ chảy máu",
                    "management": "Theo dõi INR thường xuyên. Điều chỉnh liều warfarin nếu cần."
                },
                {
                    "drug": "Methotrexate (liều cao)",
                    "mechanism": "PPI giảm thải trừ methotrexate qua thận",
                    "effect": "Tăng nồng độ methotrexate, tăng nguy cơ độc tính",
                    "management": "Thận trọng. Tạm ngừng PPI khi dùng methotrexate liều cao."
                },
                {
                    "drug": "Ketoconazole, Itraconazole, Posaconazole",
                    "mechanism": "PPI tăng pH dạ dày, giảm hấp thu azole antifungals",
                    "effect": "Giảm nồng độ azole, giảm hiệu quả điều trị",
                    "management": "Cách thời gian ít nhất 2 giờ."
                },
                {
                    "drug": "Iron salts, Vitamin B12",
                    "mechanism": "PPI giảm acid dạ dày, giảm hấp thu",
                    "effect": "Giảm hấp thu sắt và B12",
                    "management": "Cách thời gian ít nhất 2 giờ. Bổ sung B12 nếu dùng lâu dài."
                }
            ],
            "minor": []
        },
        "contraindications": {
            "absolute": [
                "Dị ứng esomeprazole hoặc PPI khác",
                "Dùng cùng atazanavir (HIV protease inhibitor)"
            ],
            "relative": [
                "Suy gan nặng (Child-Pugh C) - giảm liều tối đa 20mg/ngày",
                "Suy thận nặng (CrCl <30) - không cần chỉnh liều nhưng thận trọng",
                "Loãng xương - tăng nguy cơ gãy xương khi dùng lâu dài",
                "Nhiễm C. difficile - tăng nguy cơ",
                "Thiếu vitamin B12 - bổ sung nếu dùng lâu dài",
                "Thiếu magnesium - bổ sung nếu dùng lâu dài"
            ]
        },
        "pregnancy_lactation": {
            "fda_category": "B",
            "pregnancy_details": "Esomeprazole là FDA category B. Nghiên cứu trên động vật không cho thấy nguy cơ cho thai nhi. Một số nghiên cứu quan sát không cho thấy tăng nguy cơ dị tật bẩm sinh. Có thể dùng trong thai kỳ nếu lợi ích > nguy cơ. An toàn hơn omeprazole (category C) trong thai kỳ.",
            "lactation": {
                "safety": "Compatible",
                "details": "Esomeprazole bài tiết vào sữa mẹ ở nồng độ rất thấp. An toàn khi cho con bú.",
                "recommendation": "Có thể dùng khi cho con bú. Dùng liều thường dùng."
            }
        },
        "hepatic_adjustment": {
            "mild": "Không cần chỉnh liều",
            "moderate": "Không cần chỉnh liều, nhưng thận trọng",
            "severe": "Giảm liều tối đa 20mg/ngày (Child-Pugh C). Esomeprazole chuyển hóa ở gan qua CYP2C19 (ít hơn omeprazole) và CYP3A4.",
            "notes": "Esomeprazole ít phụ thuộc CYP2C19 hơn omeprazole, nên ít ảnh hưởng hơn ở suy gan. Tuy nhiên, vẫn giảm liều ở suy gan nặng."
        },
        "overdose_management": {
            "symptoms": [
                "PPI ít gây quá liều nghiêm trọng",
                "Triệu chứng nhẹ: nhức đầu, buồn nôn, tiêu chảy"
            ],
            "antidote": "Không có antidote đặc hiệu",
            "treatment": [
                "Hỗ trợ triệu chứng",
                "Theo dõi dấu hiệu sinh tồn",
                "Hầu hết trường hợp tự khỏi"
            ],
            "monitoring": "Theo dõi dấu hiệu sinh tồn"
        },
        "reversal_agents": None,
        "administration_instructions": {
            "oral": {
                "with_food": "Uống 30 phút TRƯỚC bữa ăn (quan trọng)",
                "timing": "Uống vào buổi sáng trước bữa sáng (hoặc trước bữa tối nếu dùng 2 lần/ngày). KHÔNG nghiền hoặc nhai viên bao tan trong ruột - phải nuốt nguyên viên."
            },
            "iv": {
                "reconstitution": "Esomeprazole IV: 20-40mg pha với 100ml NaCl 0.9% hoặc dextrose 5%",
                "infusion_rate": "Truyền trong 10-30 phút",
                "compatibility": ["NaCl 0.9%", "Dextrose 5%"],
                "incompatibility": ["Không pha với các thuốc khác trong cùng đường truyền"],
                "notes": "Chỉ dùng IV khi không uống được. Chuyển sang PO sớm nhất có thể."
            }
        },
        "references": {
            "primary_sources": [
                "FDA Drug Label - Esomeprazole",
                "UpToDate - Proton pump inhibitors: Overview of use and adverse effects",
                "Micromedex - Esomeprazole",
                "Goodman & Gilman's The Pharmacological Basis of Therapeutics"
            ],
            "last_updated": "2024-12-19",
            "evidence_level": "High - FDA approved, multiple RCTs"
        }
    },
    "Sucralfate": {
        "group": "Gastrointestinal - Mucosal Protectant",
        "vietnamese_name": "Sucralfate, Carafate",
        "administration": ["PO"],
        "indications": [
            "Loét dạ dày tá tràng",
            "Viêm dạ dày",
            "Trào ngược dạ dày thực quản",
            "Loét do stress"
        ],
        "contraindications": [
            "Dị ứng sucralfate",
            "Suy thận nặng (tăng nguy cơ tích tụ nhôm)"
        ],
        "dosage": {
            "adult_ulcer": "1g x 4 lần/ngày (trước bữa ăn và trước khi ngủ) hoặc 2g x 2 lần/ngày",
            "adult_maintenance": "1g x 2 lần/ngày",
            "notes": "Uống khi bụng đói (1 giờ trước bữa ăn). Không dùng với PPI, H2 blocker, antacid (cách 2 giờ)"
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "Thận trọng",
            "under_30": "Tránh dùng (tích tụ nhôm)"
        },
        "side_effects": [
            "Táo bón",
            "Khô miệng",
            "Buồn nôn",
            "Đầy hơi",
            "Tích tụ nhôm (suy thận)"
        ],
        "interactions": [
            "PPI/H2 blocker/Antacid: giảm hiệu quả - cách 2 giờ",
            "Warfarin: có thể tăng tác dụng chống đông",
            "Phenytoin: giảm hấp thu phenytoin",
            "Digoxin: giảm hấp thu digoxin",
            "Quinolone: giảm hấp thu quinolone",
            "Thyroxine: giảm hấp thu thyroxine"
        ],
        "pregnancy": "B",
        "mechanism_of_action": "Phức hợp sucrose-aluminum. Tạo lớp phủ bảo vệ trên vết loét dạ dày tá tràng. Phản ứng với acid dạ dày tạo thành gel dính, bám chặt vào vết loét, tạo hàng rào bảo vệ khỏi acid, pepsin, và muối mật. Kích thích tổng hợp prostaglandin, tăng tiết chất nhầy, tăng tái tạo niêm mạc. Cũng có thể hấp phụ pepsin và muối mật. Không giảm tiết acid như PPI/H2 blocker mà bảo vệ niêm mạc trực tiếp.",
        "monitoring": [
            "Đáp ứng lâm sàng (giảm đau, lành vết loét)",
            "Dấu hiệu tích tụ nhôm: rối loạn thần kinh, xương yếu (nếu dùng lâu dài ở suy thận)",
            "Chức năng thận (creatinine, BUN) - đặc biệt nếu dùng lâu dài",
            "INR nếu dùng với warfarin (có thể tăng tác dụng chống đông)",
            "Dấu hiệu táo bón nặng (tác dụng phụ thường gặp)"
        ],
        "precautions": [
            "Uống khi bụng đói (1 giờ trước bữa ăn) - cần acid dạ dày để tạo gel",
            "Không dùng với PPI, H2 blocker, antacid - cách 2 giờ (chúng làm giảm acid → giảm hiệu quả sucralfate)",
            "Không dùng với các thuốc khác - cách 2 giờ (sucralfate có thể giảm hấp thu)",
            "Thận trọng ở suy thận (CrCl 30-60) - giảm liều",
            "Tránh dùng ở suy thận nặng (CrCl <30) - tích tụ nhôm có thể gây độc",
            "Có thể gây táo bón - dùng thuốc nhuận tràng nếu cần",
            "Không nghiền hoặc nhai viên (giảm hiệu quả)",
            "Dùng đủ 4-8 tuần để lành vết loét hoàn toàn"
        ],
        "pharmacokinetics": {
            "half_life": "Không áp dụng (tác dụng tại chỗ, không hấp thu)",
            "onset": "1-2 giờ",
            "duration": "6 giờ (lớp phủ bảo vệ)",
            "protein_binding": "Không áp dụng (không hấp thu)",
            "clearance": "Không hấp thu đáng kể, thải qua phân. Nhôm có thể tích tụ ở suy thận."
        },
        "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm",
        "black_box_warnings": "Tích tụ nhôm ở suy thận nặng có thể gây độc tính thần kinh và xương. Tránh dùng ở suy thận nặng (CrCl <30).",
        "drug_interactions": {
            "major": [],
            "moderate": [
                {
                    "drug": "PPI, H2 blocker, Antacid",
                    "mechanism": "Giảm acid dạ dày, làm giảm khả năng tạo gel của sucralfate",
                    "effect": "Giảm hiệu quả của sucralfate",
                    "management": "Cách thời gian ít nhất 2 giờ. Uống sucralfate trước PPI/H2 blocker/antacid."
                },
                {
                    "drug": "Warfarin",
                    "mechanism": "Sucralfate có thể tăng hấp thu warfarin hoặc tương tác khác",
                    "effect": "Có thể tăng tác dụng chống đông, tăng INR",
                    "management": "Theo dõi INR thường xuyên. Cách thời gian 2 giờ."
                },
                {
                    "drug": "Phenytoin, Digoxin, Quinolone, Thyroxine",
                    "mechanism": "Sucralfate giảm hấp thu các thuốc này (hấp phụ hoặc chelate)",
                    "effect": "Giảm nồng độ thuốc, giảm hiệu quả điều trị",
                    "management": "Cách thời gian ít nhất 2 giờ. Uống các thuốc khác trước sucralfate."
                },
                {
                    "drug": "Iron salts, Vitamin D, Calcium",
                    "mechanism": "Sucralfate có thể giảm hấp thu",
                    "effect": "Giảm hấp thu iron, vitamin D, calcium",
                    "management": "Cách thời gian ít nhất 2 giờ"
                }
            ],
            "minor": []
        },
        "contraindications": {
            "absolute": [
                "Dị ứng sucralfate",
                "Suy thận nặng (CrCl <30) - CHỐNG CHỈ ĐỊNH do tích tụ nhôm"
            ],
            "relative": [
                "Suy thận trung bình (CrCl 30-60) - thận trọng, giảm liều, theo dõi chức năng thận",
                "Táo bón nặng - có thể làm nặng thêm",
                "Đang dùng nhiều thuốc - tăng nguy cơ tương tác hấp thu"
            ]
        },
        "pregnancy_lactation": {
            "fda_category": "B",
            "pregnancy_details": "Sucralfate là FDA category B. Nghiên cứu trên động vật không cho thấy nguy cơ cho thai nhi. Không hấp thu đáng kể, nên an toàn hơn trong thai kỳ. Có thể dùng trong thai kỳ nếu lợi ích > nguy cơ.",
            "lactation": {
                "safety": "Compatible",
                "details": "Sucralfate không hấp thu đáng kể, không bài tiết vào sữa mẹ. An toàn khi cho con bú.",
                "recommendation": "Có thể dùng khi cho con bú. Dùng liều thường dùng."
            }
        },
        "hepatic_adjustment": {
            "mild": "Không cần chỉnh liều",
            "moderate": "Không cần chỉnh liều",
            "severe": "Không cần chỉnh liều. Sucralfate không hấp thu đáng kể, không chuyển hóa ở gan.",
            "notes": "Sucralfate không hấp thu đáng kể, không cần điều chỉnh liều ở suy gan."
        },
        "overdose_management": {
            "symptoms": [
                "Sucralfate ít gây quá liều nghiêm trọng do không hấp thu",
                "Triệu chứng nhẹ: táo bón nặng, buồn nôn",
                "Ở suy thận nặng: tích tụ nhôm có thể gây độc tính thần kinh, xương yếu"
            ],
            "antidote": "Không có antidote đặc hiệu",
            "treatment": [
                "Hỗ trợ triệu chứng (điều trị táo bón nếu cần)",
                "Theo dõi dấu hiệu tích tụ nhôm ở suy thận nặng",
                "Hầu hết trường hợp tự khỏi"
            ],
            "monitoring": "Theo dõi dấu hiệu tích tụ nhôm ở suy thận nặng (rối loạn thần kinh, xương yếu)"
        },
        "reversal_agents": None,
        "administration_instructions": {
            "oral": {
                "with_food": "Uống KHI BỤNG ĐÓI (1 giờ trước bữa ăn) - quan trọng, cần acid dạ dày để tạo gel",
                "timing": "Uống 1 giờ trước bữa ăn và trước khi đi ngủ. Không uống với PPI, H2 blocker, antacid, hoặc các thuốc khác - cách ít nhất 2 giờ. KHÔNG nghiền hoặc nhai viên - nuốt nguyên viên với nước."
            },
            "iv": {
                "reconstitution": "Sucralfate chỉ có dạng uống (PO)",
                "infusion_rate": "N/A",
                "compatibility": [],
                "incompatibility": [],
                "notes": "Sucralfate chỉ có dạng uống, không có dạng IV"
            }
        },
        "references": {
            "primary_sources": [
                "FDA Drug Label - Sucralfate",
                "UpToDate - Sucralfate: Drug information",
                "Micromedex - Sucralfate",
                "Goodman & Gilman's The Pharmacological Basis of Therapeutics"
            ],
            "last_updated": "2024-12-19",
            "evidence_level": "High - FDA approved, multiple RCTs"
        }
    },
}

__all__ = ['GASTROINTESTINAL_DRUGS']
