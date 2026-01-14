"""Infectious Disease & Antibiotic Drugs (Other) - Macrolides, Fluoroquinolones, Antimalarials, etc."""

# Cephalosporins

CEPHALOSPORINS_DRUGS = {
    "Cefaclor": {
        "group": "Antibiotic - Cephalosporin (2nd Generation, Oral)",
        "vietnamese_name": "Cefaclor, Ceclor, Cefador",
        "administration": ["PO"],
        "indications": [
            "Viêm phổi cộng đồng",
            "Viêm tai giữa",
            "Viêm xoang",
            "Viêm họng/amidan",
            "Nhiễm khuẩn da và mô mềm",
            "Nhiễm khuẩn đường tiết niệu"
        ],
        "contraindications": [
            "Dị ứng cephalosporin hoặc penicillin (thận trọng)",
            "Suy thận nặng (CrCl <10) - cần điều chỉnh liều"
        ],
        "dosage": {
            "adult_standard": "250-500mg PO x 3 lần/ngày",
            "adult_er": "500mg PO x 2 lần/ngày (dạng extended-release)",
            "pediatric_standard": "20-40mg/kg/ngày PO chia 3 lần (tối đa 1g/ngày)",
            "notes": "Uống với hoặc không thức ăn. Dạng extended-release: uống với thức ăn."
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "Giảm liều 25-50%",
            "under_30": "Giảm liều 50% hoặc tăng khoảng cách liều"
        },
        "side_effects": [
            "Tiêu chảy (phổ biến)",
            "Buồn nôn",
            "Đau bụng",
            "Phát ban",
            "Tăng transaminase (hiếm)",
            "Giảm bạch cầu (hiếm)"
        ],
        "interactions": [
            "Probenecid: tăng nồng độ cefaclor",
            "Warfarin: có thể tăng INR",
            "Antacid: giảm hấp thu (cách 2 giờ)"
        ],
        "pregnancy": "B - An toàn",
        "mechanism_of_action": "Cephalosporin thế hệ 2 dạng uống, ức chế tổng hợp thành tế bào vi khuẩn. Phổ kháng khuẩn: Gram-dương (Staphylococcus, Streptococcus), Gram-âm (E. coli, Klebsiella, H. influenzae, Moraxella catarrhalis), và một số kỵ khí (Bacteroides fragilis). Không hiệu quả với MRSA, Enterococcus, Pseudomonas. Đặc điểm: hấp thu tốt qua đường uống, phổ rộng hơn thế hệ 1.",
        "monitoring": [
            "Dấu hiệu nhiễm trùng (sốt, WBC, triệu chứng lâm sàng)",
            "Dấu hiệu nhiễm C. difficile (tiêu chảy)",
            "Chức năng thận (creatinine, eGFR) - cần điều chỉnh liều",
            "Chức năng gan (ALT, AST) - hiếm"
        ],
        "precautions": [
            "Điều chỉnh liều theo chức năng thận",
            "Không dùng ở bệnh nhân dị ứng penicillins hoặc cephalosporins",
            "Nguy cơ nhiễm C. difficile - theo dõi tiêu chảy",
            "Uống với thức ăn để tăng hấp thu (dạng extended-release)",
            "Tránh antacid trong 2 giờ"
        ],
        "pharmacokinetics": {
            "half_life": "0.5-1 giờ",
            "onset": "1-2 giờ sau khi uống",
            "duration": "6-8 giờ (liều q8h)",
            "protein_binding": "25%",
            "metabolism": "Không chuyển hóa đáng kể",
            "clearance": "Chủ yếu qua thận (60-80% bài tiết nguyên dạng), cần điều chỉnh thận"
        },
        "storage": "Bảo quản ở nhiệt độ phòng (20-25°C), tránh ẩm",
        "black_box_warnings": "Không có black box warning.",
        "references": {
            "primary_sources": [
                "FDA Drug Label - Cefaclor",
                "IDSA Guidelines - Community-Acquired Pneumonia",
                "UpToDate - Cefaclor: Drug Information"
            ],
            "last_updated": "2025-02-05",
            "evidence_level": "A"
        },
        "drug_interactions": {
                  "major": [
                      {
                          "drug": "Warfarin: có thể tăng INR",
                          "mechanism": "Tăng nguy cơ chảy máu"
                      }
                  ],
                  "moderate": [],
                  "minor": [
                      {
                          "drug": "Probenecid: tăng nồng độ cefaclor",
                          "mechanism": "Tương tác lâm sàng"
                      },
                      {
                          "drug": "Antacid: giảm hấp thu (cách 2 giờ)",
                          "mechanism": "Tương tác lâm sàng"
                      }
                  ]
              },
              "pregnancy_lactation": {
                  "fda_category": "B - An toàn",
                  "pregnancy_details": "Category B - An toàn - Cần tra cứu thêm thông tin chi tiết về sử dụng trong thai kỳ.",
                  "lactation": {
                      "safety": "Use with caution",
                      "details": "Cần tra cứu thêm thông tin chi tiết về bài tiết vào sữa mẹ.",
                      "recommendation": "Thận trọng khi cho con bú, tra cứu thêm thông tin."
                  }
              },
              "hepatic_adjustment": {
                  "mild": "Không đổi",
                  "moderate": "Thận trọng, có thể giảm liều",
                  "severe": "Thận trọng, giảm liều hoặc tránh dùng",
                  "notes": "Nhiều kháng sinh chuyển hóa qua gan, cần điều chỉnh liều ở suy gan nặng."
              },
              "overdose_management": {
                  "symptoms": [
                      "Cần tra cứu thêm thông tin về triệu chứng quá liều"
                  ],
                  "antidote": "Không có antidote đặc hiệu",
                  "treatment": [
                      "Ngừng ngay thuốc",
                      "Rửa dạ dày nếu uống trong vòng 1-2 giờ (nếu phù hợp)",
                      "Than hoạt tính",
                      "Điều trị hỗ trợ và điều trị triệu chứng",
                      "Theo dõi dấu hiệu sinh tồn"
                  ],
                  "monitoring": "Theo dõi dấu hiệu sinh tồn, triệu chứng lâm sàng"
              },
              "reversal_agents": {
                  "available": False,
                  "agents": []
              },
              "administration_instructions": {
                  "oral": {
                      "with_food": "Có thể uống với hoặc không có thức ăn (trừ khi có chỉ định khác)",
                      "timing": "Theo chỉ định của bác sĩ",
                      "notes": "Cần tra cứu thêm thông tin chi tiết về cách dùng."
                  }
              },
},
    
    "Cefadroxil": {
        "group": "Antibiotic - Cephalosporin (1st Generation, Oral)",
        "vietnamese_name": "Cefadroxil, Duricef, Cefadroxil 500mg",
        "administration": ["PO"],
        "indications": [
            "Nhiễm khuẩn đường hô hấp trên (viêm họng, viêm amidan)",
            "Nhiễm khuẩn đường tiết niệu",
            "Nhiễm khuẩn da và mô mềm",
            "Nhiễm khuẩn răng miệng"
        ],
        "contraindications": [
            "Dị ứng cephalosporin",
            "Dị ứng penicillin (phản ứng chéo 5-10%)"
        ],
        "dosage": {
            "adult_standard": "500mg-1g x 2 lần/ngày",
            "adult_uti": "1-2g x 1-2 lần/ngày",
            "pediatric": "30mg/kg/ngày chia 2 lần",
            "notes": "Cephalosporin uống thế hệ 1. Half-life dài hơn cefazolin, cho phép dùng 1-2 lần/ngày. Uống với hoặc không có thức ăn."
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "Giảm liều 50% hoặc tăng khoảng cách",
            "under_30": "Giảm liều 75% hoặc tăng khoảng cách",
            "hemodialysis": "Bổ sung liều sau mỗi lần lọc máu"
        },
        "side_effects": [
            "Tiêu chảy (phổ biến)",
            "Buồn nôn, nôn",
            "Phát ban",
            "Nhiễm trùng nấm Candida",
            "Tăng men gan (hiếm)",
            "Giảm bạch cầu (hiếm)"
        ],
        "interactions": [
            "Warfarin: có thể tăng INR",
            "Probenecid: tăng nồng độ cefadroxil",
            "Aminoglycosides: tăng độc thận (nếu dùng cùng)"
        ],
        "pregnancy": "B - An toàn trong thai kỳ",
        "mechanism_of_action": "Cefadroxil là cephalosporin uống thế hệ 1, ức chế tổng hợp thành tế bào vi khuẩn bằng cách gắn với penicillin-binding proteins (PBPs). Phổ kháng khuẩn: Gram-dương mạnh (Staphylococcus không kháng methicillin, Streptococcus), Gram-âm yếu (E. coli, Proteus mirabilis, Klebsiella). Không hiệu quả với Pseudomonas, Enterococcus, hoặc MRSA. Cefadroxil có half-life dài hơn cefazolin (1.5-2 giờ), cho phép dùng 1-2 lần/ngày. Hấp thu tốt qua đường uống, không bị ảnh hưởng bởi thức ăn.",
        "monitoring": [
            "Dấu hiệu nhiễm trùng (sốt, WBC)",
            "Cấy máu và cấy từ vị trí nhiễm trùng",
            "Dấu hiệu nhiễm C. difficile",
            "Chức năng thận (creatinine) - cần điều chỉnh liều ở suy thận",
            "Chức năng gan (ALT, AST) - hiếm viêm gan",
            "Công thức máu (CBC) - hiếm giảm bạch cầu"
        ],
        "precautions": [
            "Không dùng ở bệnh nhân dị ứng penicillins hoặc cephalosporins (phản ứng chéo ~5-10%)",
            "Nguy cơ nhiễm C. difficile - theo dõi tiêu chảy",
            "Phải điều chỉnh liều theo chức năng thận (eGFR) - quan trọng",
            "Uống với hoặc không có thức ăn (hấp thu tốt trong cả hai trường hợp)",
            "Dùng đúng liều và đủ thời gian để tránh kháng thuốc",
            "Theo dõi nhiễm nấm thứ phát khi dùng kéo dài"
        ],
        "pharmacokinetics": {
            "half_life": "1.5-2 giờ (dài hơn cefazolin)",
            "onset": "1-2 giờ (PO)",
            "duration": "q12h hoặc q24h",
            "protein_binding": "20%",
            "metabolism": "Một phần trong gan",
            "clearance": "Chủ yếu qua thận (90% bài tiết nguyên dạng qua nước tiểu), cần điều chỉnh thận ở suy thận nặng"
        },
        "storage": "Bảo quản ở nhiệt độ phòng (20-25°C), tránh ẩm, tránh ánh sáng. Viên nén: bảo quản trong bao bì kín.",
        "black_box_warnings": "Không có black box warning. Tuy nhiên, nguy cơ phản ứng dị ứng nặng (sốc phản vệ) ở bệnh nhân dị ứng penicillin hoặc cephalosporin.",
        "drug_interactions": {
            "major": [
                {
                    "drug": "Warfarin",
                    "mechanism": "Cefadroxil có thể ảnh hưởng đến hệ vi khuẩn đường ruột, làm giảm tổng hợp vitamin K, tăng tác dụng warfarin.",
                    "effect": "Tăng tác dụng chống đông, tăng INR, tăng nguy cơ chảy máu",
                    "management": "Theo dõi INR chặt chẽ khi bắt đầu, thay đổi liều, hoặc ngừng cefadroxil. Điều chỉnh liều warfarin nếu cần."
                }
            ],
            "moderate": [
                {
                    "drug": "Probenecid",
                    "mechanism": "Probenecid ức chế bài tiết cefadroxil ở ống thận, làm tăng nồng độ cefadroxil.",
                    "effect": "Tăng nồng độ cefadroxil, tăng thời gian bán thải",
                    "management": "Có thể dùng để tăng nồng độ cefadroxil nếu cần. Theo dõi tác dụng phụ."
                },
                {
                    "drug": "Aminoglycosides (Gentamicin, Amikacin, Tobramycin)",
                    "mechanism": "Cả hai đều có độc tính thận, tác dụng cộng dồn.",
                    "effect": "Tăng nguy cơ độc thận",
                    "management": "Theo dõi chức năng thận chặt chẽ. Tránh dùng cùng nếu có thể."
                }
            ],
            "minor": []
        },
        "contraindications": {
            "tuyệt_đối": [
                "Dị ứng cefadroxil hoặc các cephalosporin khác",
                "Dị ứng beta-lactam (penicillin, cephalosporin, carbapenem) - phản ứng chéo cao",
                "Sốc phản vệ với cephalosporin hoặc penicillin trước đây"
            ],
            "tương_đối": [
                "Dị ứng penicillin - phản ứng chéo 5-10%, thận trọng",
                "Suy thận nặng (CrCl <30) - cần điều chỉnh liều, tăng khoảng cách",
                "Tiền sử nhiễm C. difficile - tăng nguy cơ tái phát"
            ]
        },
        "contraindications_detail": {
            "tuyệt_đối": [
                "Dị ứng cefadroxil hoặc các cephalosporin khác",
                "Dị ứng beta-lactam (penicillin, cephalosporin, carbapenem) - phản ứng chéo cao",
                "Sốc phản vệ với cephalosporin hoặc penicillin trước đây"
            ],
            "tương_đối": [
                "Dị ứng penicillin - phản ứng chéo 5-10%, thận trọng",
                "Suy thận nặng (CrCl <30) - cần điều chỉnh liều, tăng khoảng cách",
                "Tiền sử nhiễm C. difficile - tăng nguy cơ tái phát"
            ]
        },
        "pregnancy_lactation": {
            "fda_category": "B",
            "pregnancy_details": "Cefadroxil phân loại B - an toàn trong thai kỳ. Cephalosporin là một trong những kháng sinh an toàn nhất trong thai kỳ.",
            "lactation": {
                "safety": "Compatible",
                "details": "Cefadroxil bài tiết vào sữa mẹ ở nồng độ thấp. An toàn cho trẻ bú mẹ.",
                "recommendation": "Có thể dùng khi cho con bú."
            }
        },
        "hepatic_adjustment": {
            "mild": "Không cần điều chỉnh liều",
            "moderate": "Không cần điều chỉnh liều",
            "severe": "Thận trọng, có thể cần giảm liều nhẹ",
            "notes": "Cefadroxil chuyển hóa một phần ở gan nhưng thải trừ chủ yếu qua thận. Suy gan ít ảnh hưởng."
        },
        "overdose_management": {
            "symptoms": [
                "Triệu chứng tiêu hóa: Buồn nôn, nôn, tiêu chảy",
                "Triệu chứng thần kinh: Kích động, co giật (hiếm)",
                "Triệu chứng thận: Tăng creatinine (hiếm)"
            ],
            "antidote": "Không có antidote đặc hiệu. Điều trị hỗ trợ.",
            "treatment": [
                "Ngừng ngay cefadroxil",
                "Rửa dạ dày hoặc than hoạt nếu uống trong vòng 1-2 giờ",
                "Theo dõi dấu hiệu sinh tồn",
                "Điều trị triệu chứng tiêu hóa",
                "Lọc máu có thể loại bỏ một phần cefadroxil nhưng không được khuyến nghị thường quy"
            ],
            "monitoring": "Theo dõi dấu hiệu sinh tồn, chức năng thận trong ít nhất 24 giờ."
        },
        "reversal_agents": {
            "available": False,
            "agents": [],
            "notes": "Không có antidote đặc hiệu. Điều trị quá liều chủ yếu là hỗ trợ. Lọc máu có thể loại bỏ một phần nhưng không được khuyến nghị thường quy."
        },
        "administration_instructions": {
            "oral": {
                "with_food": "Có thể uống với hoặc không có thức ăn. Hấp thu tốt trong cả hai trường hợp.",
                "timing": "Uống 1-2 lần/ngày (500mg-1g mỗi lần). Uống đều đặn, cách đều nhau trong ngày."
            },
            "iv": {
                "reconstitution": "N/A - Chỉ có dạng uống",
                "infusion_rate": "N/A",
                "compatibility": [],
                "incompatibility": [],
                "notes": "Cefadroxil chỉ có dạng uống. Nếu cần dạng IV, dùng cefazolin."
            }
        },
        "references": {
            "primary_sources": [
                "FDA Drug Label - Duricef (cefadroxil)",
                "UpToDate - Cefadroxil: Drug Information",
                "Goodman & Gilman's The Pharmacological Basis of Therapeutics"
            ],
            "last_updated": "2025-02-05",
            "evidence_level": "A - Dựa trên FDA drug labels và dữ liệu lâm sàng"
        }
    },
    
    "Cefazolin": {
        "group": "Antibiotic - Cephalosporin (1st Generation)",
        "vietnamese_name": "Cefazolin, Ancef, Kefzol",
        "administration": ["IV", "IM"],
        "indications": [
            "Dự phòng phẫu thuật (phẫu thuật sạch, sạch-nhiễm)",
            "Nhiễm khuẩn da và mô mềm",
            "Nhiễm khuẩn đường tiết niệu",
            "Nhiễm khuẩn đường hô hấp",
            "Viêm nội tâm mạc do S. aureus (kết hợp với gentamicin)"
        ],
        "contraindications": [
            "Dị ứng cephalosporin hoặc penicillin (thận trọng)",
            "Suy thận nặng (CrCl <10) - cần điều chỉnh liều"
        ],
        "dosage": {
            "adult_standard": "1-2g IV/IM mỗi 8 giờ",
            "adult_severe": "2g IV mỗi 6-8 giờ",
            "adult_prophylaxis": "1-2g IV 30-60 phút trước phẫu thuật",
            "adult_prophylaxis_repeat": "1-2g IV mỗi 2-4 giờ trong phẫu thuật dài",
            "notes": "Liều dự phòng: 1g (phẫu thuật nhỏ), 2g (phẫu thuật lớn, béo phì)"
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "1-2g IV mỗi 12 giờ",
            "under_30": "0.5-1g IV mỗi 12-24 giờ",
            "hemodialysis": "0.5-1g IV sau lọc máu"
        },
        "side_effects": [
            "Phát ban",
            "Tiêu chảy",
            "Buồn nôn",
            "Tăng transaminase (hiếm)",
            "Giảm bạch cầu (hiếm)",
            "Phản ứng tại chỗ tiêm"
        ],
        "interactions": [
            "Probenecid: tăng nồng độ cefazolin",
            "Warfarin: có thể tăng INR",
            "Aminoglycosides: không pha chung"
        ],
        "pregnancy": "B - An toàn",
        "mechanism_of_action": "Cephalosporin thế hệ 1, ức chế tổng hợp thành tế bào vi khuẩn bằng cách gắn với penicillin-binding proteins (PBPs). Phổ kháng khuẩn: Gram-dương mạnh (Staphylococcus aureus - kể cả MSSA, Staphylococcus epidermidis, Streptococcus), Gram-âm hạn chế (E. coli, Klebsiella, Proteus mirabilis). Không hiệu quả với MRSA, Enterococcus, Pseudomonas, hoặc kỵ khí. Đặc điểm: thời gian bán thải ngắn (1.5-2 giờ), cần dùng nhiều lần/ngày.",
        "monitoring": [
            "Dấu hiệu nhiễm trùng (sốt, WBC, triệu chứng lâm sàng)",
            "Cấy máu và cấy từ vị trí nhiễm trùng",
            "Chức năng thận (creatinine, eGFR) - cần điều chỉnh liều",
            "Dấu hiệu nhiễm C. difficile",
            "Phản ứng tại chỗ tiêm (đau, viêm tĩnh mạch)",
            "Chức năng gan (ALT, AST) - hiếm"
        ],
        "precautions": [
            "Điều chỉnh liều theo chức năng thận (eGFR) - quan trọng",
            "Không dùng ở bệnh nhân dị ứng penicillins hoặc cephalosporins (phản ứng chéo ~5-10%)",
            "Nguy cơ nhiễm C. difficile - theo dõi tiêu chảy",
            "Dự phòng phẫu thuật: tiêm 30-60 phút trước khi rạch da",
            "Pha trong NS hoặc D5W, tiêm IV hoặc IM",
            "Không pha trộn với aminoglycosides (bất hoạt)"
        ],
        "pharmacokinetics": {
            "half_life": "1.5-2 giờ",
            "onset": "Ngay lập tức sau khi tiêm IV",
            "duration": "6-8 giờ (liều q8h)",
            "protein_binding": "74-86%",
            "metabolism": "Không chuyển hóa đáng kể",
            "clearance": "Chủ yếu qua thận (80-100% bài tiết nguyên dạng), cần điều chỉnh thận"
        },
        "storage": "Bảo quản bột khô ở nhiệt độ phòng (20-25°C). Sau khi pha: bảo quản ở nhiệt độ phòng 24 giờ, hoặc trong tủ lạnh 10 ngày.",
        "black_box_warnings": "Không có black box warning. Tuy nhiên, cần điều chỉnh liều theo chức năng thận để tránh độc tính.",
        "references": {
            "primary_sources": [
                "FDA Drug Label - Cefazolin",
                "IDSA Guidelines - Surgical Prophylaxis",
                "UpToDate - Cefazolin: Drug Information",
                "Medscape - Cefazolin Drug Reference"
            ],
            "last_updated": "2025-02-05",
            "evidence_level": "A"
        },
        "drug_interactions": {
                  "major": [
                      {
                          "drug": "Warfarin: có thể tăng INR",
                          "mechanism": "Tăng nguy cơ chảy máu"
                      }
                  ],
                  "moderate": [],
                  "minor": [
                      {
                          "drug": "Probenecid: tăng nồng độ cefazolin",
                          "mechanism": "Tương tác lâm sàng"
                      },
                      {
                          "drug": "Aminoglycosides: không pha chung",
                          "mechanism": "Tương tác lâm sàng"
                      }
                  ]
              },
              "pregnancy_lactation": {
                  "fda_category": "B - An toàn",
                  "pregnancy_details": "Category B - An toàn - Cần tra cứu thêm thông tin chi tiết về sử dụng trong thai kỳ.",
                  "lactation": {
                      "safety": "Use with caution",
                      "details": "Cần tra cứu thêm thông tin chi tiết về bài tiết vào sữa mẹ.",
                      "recommendation": "Thận trọng khi cho con bú, tra cứu thêm thông tin."
                  }
              },
              "hepatic_adjustment": {
                  "mild": "Không đổi",
                  "moderate": "Thận trọng, có thể giảm liều",
                  "severe": "Thận trọng, giảm liều hoặc tránh dùng",
                  "notes": "Nhiều kháng sinh chuyển hóa qua gan, cần điều chỉnh liều ở suy gan nặng."
              },
              "overdose_management": {
                  "symptoms": [
                      "Cần tra cứu thêm thông tin về triệu chứng quá liều"
                  ],
                  "antidote": "Không có antidote đặc hiệu",
                  "treatment": [
                      "Ngừng ngay thuốc",
                      "Rửa dạ dày nếu uống trong vòng 1-2 giờ (nếu phù hợp)",
                      "Than hoạt tính",
                      "Điều trị hỗ trợ và điều trị triệu chứng",
                      "Theo dõi dấu hiệu sinh tồn"
                  ],
                  "monitoring": "Theo dõi dấu hiệu sinh tồn, triệu chứng lâm sàng"
              },
              "reversal_agents": {
                  "available": False,
                  "agents": []
              },
              "administration_instructions": {
                  "iv": {
                      "reconstitution": "Cần tra cứu",
                      "infusion_rate": "Cần tra cứu",
                      "compatibility": [
                          "Cần tra cứu"
                      ],
                      "incompatibility": [],
                      "notes": "Cần tra cứu thêm thông tin chi tiết."
                  }
              },
},
    
    "Cefdinir": {
        "group": "Antibiotic - Cephalosporin (3rd Generation, Oral)",
        "vietnamese_name": "Cefdinir, Omnicef, Cefdin",
        "administration": ["PO"],
        "indications": [
            "Viêm phổi cộng đồng",
            "Viêm tai giữa",
            "Viêm xoang",
            "Nhiễm khuẩn da và mô mềm",
            "Nhiễm khuẩn đường tiết niệu"
        ],
        "contraindications": [
            "Dị ứng cephalosporin hoặc penicillin (thận trọng)",
            "Suy thận nặng (CrCl <30) - cần điều chỉnh liều"
        ],
        "dosage": {
            "adult_standard": "300mg PO x 2 lần/ngày hoặc 600mg PO x 1 lần/ngày",
            "adult_uti": "300mg PO x 2 lần/ngày",
            "pediatric_standard": "7mg/kg PO x 2 lần/ngày (tối đa 300mg/lần)",
            "notes": "Uống với hoặc không thức ăn. Hấp thu tốt hơn với thức ăn."
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "300mg PO x 1 lần/ngày",
            "under_30": "300mg PO x 1 lần/ngày"
        },
        "side_effects": [
            "Tiêu chảy (phổ biến)",
            "Buồn nôn",
            "Đau bụng",
            "Phát ban",
            "Tăng transaminase (hiếm)",
            "Giảm bạch cầu (hiếm)"
        ],
        "interactions": [
            "Probenecid: tăng nồng độ cefdinir",
            "Warfarin: có thể tăng INR",
            "Antacid (chứa aluminum, magnesium): giảm hấp thu (cách 2 giờ)",
            "Sắt: giảm hấp thu (cách 2 giờ)"
        ],
        "pregnancy": "B - An toàn",
        "mechanism_of_action": "Cephalosporin thế hệ 3 dạng uống, ức chế tổng hợp thành tế bào vi khuẩn. Phổ kháng khuẩn: Gram-âm mạnh (E. coli, Klebsiella, Proteus, H. influenzae, Moraxella catarrhalis), Gram-dương tốt hơn cefixime (Streptococcus pneumoniae, Streptococcus pyogenes). Không hiệu quả với MRSA, Enterococcus, Pseudomonas, hoặc kỵ khí. Đặc điểm: hấp thu tốt qua đường uống, hiệu quả với cả Gram-dương và Gram-âm.",
        "monitoring": [
            "Dấu hiệu nhiễm trùng (sốt, WBC, triệu chứng lâm sàng)",
            "Dấu hiệu nhiễm C. difficile (tiêu chảy)",
            "Chức năng thận (creatinine, eGFR) - cần điều chỉnh liều",
            "Chức năng gan (ALT, AST) - hiếm"
        ],
        "precautions": [
            "Điều chỉnh liều theo chức năng thận",
            "Không dùng ở bệnh nhân dị ứng penicillins hoặc cephalosporins",
            "Nguy cơ nhiễm C. difficile - theo dõi tiêu chảy",
            "Uống với thức ăn để tăng hấp thu",
            "Tránh antacid và sắt trong 2 giờ"
        ],
        "pharmacokinetics": {
            "half_life": "1.5-2 giờ",
            "onset": "1-2 giờ sau khi uống",
            "duration": "8-12 giờ (liều q12h)",
            "protein_binding": "60-70%",
            "metabolism": "Không chuyển hóa đáng kể",
            "clearance": "Chủ yếu qua thận (60-70% bài tiết nguyên dạng), cần điều chỉnh thận"
        },
        "storage": "Bảo quản ở nhiệt độ phòng (20-25°C), tránh ẩm",
        "black_box_warnings": "Không có black box warning.",
        "references": {
            "primary_sources": [
                "FDA Drug Label - Cefdinir",
                "IDSA Guidelines - Community-Acquired Pneumonia",
                "UpToDate - Cefdinir: Drug Information"
            ],
            "last_updated": "2025-02-05",
            "evidence_level": "A"
        },
        "drug_interactions": {
                  "major": [
                      {
                          "drug": "Warfarin: có thể tăng INR",
                          "mechanism": "Tăng nguy cơ chảy máu"
                      }
                  ],
                  "moderate": [],
                  "minor": [
                      {
                          "drug": "Probenecid: tăng nồng độ cefdinir",
                          "mechanism": "Tương tác lâm sàng"
                      },
                      {
                          "drug": "Antacid (chứa aluminum, magnesium): giảm hấp thu (cách 2 giờ)",
                          "mechanism": "Tương tác lâm sàng"
                      },
                      {
                          "drug": "Sắt: giảm hấp thu (cách 2 giờ)",
                          "mechanism": "Tương tác lâm sàng"
                      }
                  ]
              },
              "pregnancy_lactation": {
                  "fda_category": "B - An toàn",
                  "pregnancy_details": "Category B - An toàn - Cần tra cứu thêm thông tin chi tiết về sử dụng trong thai kỳ.",
                  "lactation": {
                      "safety": "Use with caution",
                      "details": "Cần tra cứu thêm thông tin chi tiết về bài tiết vào sữa mẹ.",
                      "recommendation": "Thận trọng khi cho con bú, tra cứu thêm thông tin."
                  }
              },
              "hepatic_adjustment": {
                  "mild": "Không đổi",
                  "moderate": "Thận trọng, có thể giảm liều",
                  "severe": "Thận trọng, giảm liều hoặc tránh dùng",
                  "notes": "Nhiều kháng sinh chuyển hóa qua gan, cần điều chỉnh liều ở suy gan nặng."
              },
              "overdose_management": {
                  "symptoms": [
                      "Cần tra cứu thêm thông tin về triệu chứng quá liều"
                  ],
                  "antidote": "Không có antidote đặc hiệu",
                  "treatment": [
                      "Ngừng ngay thuốc",
                      "Rửa dạ dày nếu uống trong vòng 1-2 giờ (nếu phù hợp)",
                      "Than hoạt tính",
                      "Điều trị hỗ trợ và điều trị triệu chứng",
                      "Theo dõi dấu hiệu sinh tồn"
                  ],
                  "monitoring": "Theo dõi dấu hiệu sinh tồn, triệu chứng lâm sàng"
              },
              "reversal_agents": {
                  "available": False,
                  "agents": []
              },
              "administration_instructions": {
                  "oral": {
                      "with_food": "Có thể uống với hoặc không có thức ăn (trừ khi có chỉ định khác)",
                      "timing": "Theo chỉ định của bác sĩ",
                      "notes": "Cần tra cứu thêm thông tin chi tiết về cách dùng."
                  }
              },
},
    
    "Cefepime": {
        "group": "Antibiotic - Cephalosporin (4th Generation)",
        "vietnamese_name": "Cefepime, Maxipime",
        "administration": ["IV", "IM"],
        "indications": [
            "Nhiễm khuẩn bệnh viện nặng",
            "Nhiễm khuẩn huyết",
            "Viêm phổi bệnh viện",
            "Nhiễm khuẩn đường tiết niệu phức tạp",
            "Nhiễm khuẩn da và mô mềm",
            "Sốt giảm bạch cầu (febrile neutropenia)"
        ],
        "contraindications": [
            "Dị ứng cephalosporin hoặc penicillin (thận trọng)",
            "Suy thận nặng (CrCl <10) - cần điều chỉnh liều"
        ],
        "dosage": {
            "adult_standard": "1-2g IV mỗi 12 giờ",
            "adult_severe": "2g IV mỗi 8-12 giờ",
            "adult_febrile_neutropenia": "2g IV mỗi 8 giờ",
            "adult_pseudomonas": "2g IV mỗi 8 giờ",
            "notes": "Liều cao hơn cho nhiễm khuẩn nặng và Pseudomonas"
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "1-2g IV mỗi 12-24 giờ",
            "under_30": "1g IV mỗi 24 giờ",
            "hemodialysis": "1g IV sau lọc máu"
        },
        "side_effects": [
            "Phát ban",
            "Tiêu chảy",
            "Buồn nôn",
            "Tăng transaminase",
            "Giảm bạch cầu (hiếm)",
            "Co giật (hiếm, suy thận nặng)",
            "Rối loạn thần kinh (hiếm, suy thận)"
        ],
        "interactions": [
            "Probenecid: tăng nồng độ cefepime",
            "Warfarin: có thể tăng INR",
            "Aminoglycosides: không pha chung"
        ],
        "pregnancy": "B - An toàn",
        "mechanism_of_action": "Cephalosporin thế hệ 4, ức chế tổng hợp thành tế bào vi khuẩn. Phổ kháng khuẩn: Gram-dương tốt hơn thế hệ 3 (Staphylococcus, Streptococcus), Gram-âm mạnh (Enterobacteriaceae, Pseudomonas aeruginosa, Acinetobacter). Kháng được nhiều beta-lactamase. Không hiệu quả với MRSA, Enterococcus, hoặc kỵ khí. Đặc điểm: phổ rộng, hiệu quả với cả Gram-dương và Gram-âm, kể cả Pseudomonas.",
        "monitoring": [
            "Dấu hiệu nhiễm trùng (sốt, WBC, triệu chứng lâm sàng)",
            "Cấy máu và cấy từ vị trí nhiễm trùng",
            "Chức năng thận (creatinine, eGFR) - cần điều chỉnh liều",
            "Dấu hiệu nhiễm C. difficile",
            "Chức năng gan (ALT, AST)",
            "Rối loạn thần kinh (co giật, nhầm lẫn) - hiếm, suy thận",
            "Công thức máu (CBC) - đặc biệt trong sốt giảm bạch cầu"
        ],
        "precautions": [
            "Điều chỉnh liều theo chức năng thận - quan trọng",
            "Nguy cơ co giật và rối loạn thần kinh ở suy thận nặng - cần điều chỉnh liều",
            "Không dùng ở bệnh nhân dị ứng penicillins hoặc cephalosporins",
            "Nguy cơ nhiễm C. difficile",
            "Liều cao hơn cho nhiễm khuẩn nặng và Pseudomonas (2g q8h)",
            "Pha trong NS hoặc D5W",
            "Không pha trộn với aminoglycosides"
        ],
        "pharmacokinetics": {
            "half_life": "2 giờ",
            "onset": "Ngay lập tức sau khi tiêm IV",
            "duration": "8-12 giờ (liều q8-12h)",
            "protein_binding": "20%",
            "metabolism": "Không chuyển hóa đáng kể",
            "clearance": "Chủ yếu qua thận (85% bài tiết nguyên dạng), cần điều chỉnh thận"
        },
        "storage": "Bảo quản bột khô ở nhiệt độ phòng (20-25°C). Sau khi pha: bảo quản ở nhiệt độ phòng 24 giờ.",
        "black_box_warnings": "Nguy cơ co giật và rối loạn thần kinh ở suy thận nặng - cần điều chỉnh liều theo chức năng thận.",
        "references": {
            "primary_sources": [
                "FDA Drug Label - Cefepime",
                "IDSA Guidelines - Hospital-Acquired Pneumonia",
                "UpToDate - Cefepime: Drug Information"
            ],
            "last_updated": "2025-02-05",
            "evidence_level": "A"
        },
        "risk_flags": {
            "high_alert": True,
            "narrow_therapeutic_index": False,
            "icu_critical_care_only": False,
            "bleeding_risk": None,
            "organ_toxicity": {"neurological": "Black Box Warning - Seizures, encephalopathy (especially in renal impairment)", "hepatic": "Hepatotoxicity (rare)", "hematologic": "Neutropenia (rare)", "gastrointestinal": "C. difficile infection"},
            "qt_prolongation": False,
            "hepatotoxicity": "Rare",
            "nephrotoxicity": False,
            "requires_monitoring": ["Renal function (CrCl - dose adjustment required, Black Box Warning for neurotoxicity)", "Neurological signs (seizures, encephalopathy - Black Box Warning)", "C. difficile infection signs", "Hepatic function (ALT, AST)", "CBC (neutropenia risk)"],
            "look_alike_sound_alike": ["Cefepime", "Cefotaxime", "Ceftazidime"]
        },
        "guideline_tags": [
            "FDA Black Box Warning - Neurotoxicity (Seizures, Encephalopathy) in Renal Impairment",
            "IDSA Guidelines - Hospital-Acquired Pneumonia",
            "IDSA Guidelines - Febrile Neutropenia",
            "WHO Essential Medicines List"
        ],
        "last_updated": "2025-02-18",
        "drug_interactions": {
                  "major": [
                      {
                          "drug": "Warfarin: có thể tăng INR",
                          "mechanism": "Tăng nguy cơ chảy máu"
                      }
                  ],
                  "moderate": [],
                  "minor": [
                      {
                          "drug": "Probenecid: tăng nồng độ cefepime",
                          "mechanism": "Tương tác lâm sàng"
                      },
                      {
                          "drug": "Aminoglycosides: không pha chung",
                          "mechanism": "Tương tác lâm sàng"
                      }
                  ]
              },
              "pregnancy_lactation": {
                  "fda_category": "B - An toàn",
                  "pregnancy_details": "Category B - An toàn - Cần tra cứu thêm thông tin chi tiết về sử dụng trong thai kỳ.",
                  "lactation": {
                      "safety": "Use with caution",
                      "details": "Cần tra cứu thêm thông tin chi tiết về bài tiết vào sữa mẹ.",
                      "recommendation": "Thận trọng khi cho con bú, tra cứu thêm thông tin."
                  }
              },
              "hepatic_adjustment": {
                  "mild": "Không đổi",
                  "moderate": "Thận trọng, có thể giảm liều",
                  "severe": "Thận trọng, giảm liều hoặc tránh dùng",
                  "notes": "Nhiều kháng sinh chuyển hóa qua gan, cần điều chỉnh liều ở suy gan nặng."
              },
              "overdose_management": {
                  "symptoms": [
                      "Cần tra cứu thêm thông tin về triệu chứng quá liều"
                  ],
                  "antidote": "Không có antidote đặc hiệu",
                  "treatment": [
                      "Ngừng ngay thuốc",
                      "Rửa dạ dày nếu uống trong vòng 1-2 giờ (nếu phù hợp)",
                      "Than hoạt tính",
                      "Điều trị hỗ trợ và điều trị triệu chứng",
                      "Theo dõi dấu hiệu sinh tồn"
                  ],
                  "monitoring": "Theo dõi dấu hiệu sinh tồn, triệu chứng lâm sàng"
              },
              "reversal_agents": {
                  "available": False,
                  "agents": []
              },
              "administration_instructions": {
                  "iv": {
                      "reconstitution": "Cần tra cứu",
                      "infusion_rate": "Cần tra cứu",
                      "compatibility": [
                          "Cần tra cứu"
                      ],
                      "incompatibility": [],
                      "notes": "Cần tra cứu thêm thông tin chi tiết."
                  }
              },
},
    
    "Cefixime": {
        "group": "Antibiotic - Cephalosporin (3rd Generation, Oral)",
        "vietnamese_name": "Cefixime, Suprax, Cefix",
        "administration": ["PO"],
        "indications": [
            "Viêm phổi cộng đồng",
            "Viêm tai giữa",
            "Viêm xoang",
            "Nhiễm khuẩn đường tiết niệu",
            "Bệnh lậu (gonorrhea)",
            "Nhiễm khuẩn da và mô mềm"
        ],
        "contraindications": [
            "Dị ứng cephalosporin hoặc penicillin (thận trọng)",
            "Suy thận nặng (CrCl <10) - cần điều chỉnh liều"
        ],
        "dosage": {
            "adult_standard": "400mg PO x 1 lần/ngày hoặc 200mg PO x 2 lần/ngày",
            "adult_uti": "400mg PO x 1 lần/ngày",
            "adult_gonorrhea": "400mg PO x 1 lần (kết hợp với azithromycin hoặc doxycycline)",
            "pediatric_standard": "8mg/kg PO x 1 lần/ngày (tối đa 400mg)",
            "notes": "Uống với hoặc không thức ăn. Hấp thu tốt hơn với thức ăn."
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "Giảm liều 25-50%",
            "under_30": "Giảm liều 50% hoặc tăng khoảng cách liều"
        },
        "side_effects": [
            "Tiêu chảy (phổ biến)",
            "Buồn nôn",
            "Đau bụng",
            "Phát ban",
            "Tăng transaminase (hiếm)",
            "Giảm bạch cầu (hiếm)"
        ],
        "interactions": [
            "Probenecid: tăng nồng độ cefixime",
            "Warfarin: có thể tăng INR",
            "Antacid: giảm hấp thu (cách 2 giờ)"
        ],
        "pregnancy": "B - An toàn",
        "mechanism_of_action": "Cephalosporin thế hệ 3 dạng uống, ức chế tổng hợp thành tế bào vi khuẩn bằng cách gắn với penicillin-binding proteins (PBPs). Phổ kháng khuẩn: Gram-âm mạnh (E. coli, Klebsiella, Proteus, Neisseria gonorrhoeae, H. influenzae), Gram-dương hạn chế (Streptococcus). Không hiệu quả với MRSA, Enterococcus, Pseudomonas, hoặc kỵ khí. Đặc điểm: hấp thu tốt qua đường uống, thời gian bán thải dài (3-4 giờ), dùng 1-2 lần/ngày.",
        "monitoring": [
            "Dấu hiệu nhiễm trùng (sốt, WBC, triệu chứng lâm sàng)",
            "Dấu hiệu nhiễm C. difficile (tiêu chảy)",
            "Chức năng thận (creatinine, eGFR) - cần điều chỉnh liều",
            "Chức năng gan (ALT, AST) - hiếm"
        ],
        "precautions": [
            "Điều chỉnh liều theo chức năng thận",
            "Không dùng ở bệnh nhân dị ứng penicillins hoặc cephalosporins",
            "Nguy cơ nhiễm C. difficile - theo dõi tiêu chảy",
            "Uống với thức ăn để tăng hấp thu",
            "Tránh antacid trong 2 giờ"
        ],
        "pharmacokinetics": {
            "half_life": "3-4 giờ",
            "onset": "1-2 giờ sau khi uống",
            "duration": "12-24 giờ (liều q24h)",
            "protein_binding": "65%",
            "metabolism": "Không chuyển hóa đáng kể",
            "clearance": "Chủ yếu qua thận (50% bài tiết nguyên dạng), một phần qua mật"
        },
        "storage": "Bảo quản ở nhiệt độ phòng (20-25°C), tránh ẩm",
        "black_box_warnings": "Không có black box warning.",
        "references": {
            "primary_sources": [
                "FDA Drug Label - Cefixime",
                "IDSA Guidelines - Community-Acquired Pneumonia",
                "UpToDate - Cefixime: Drug Information"
            ],
            "last_updated": "2025-02-05",
            "evidence_level": "A"
        },
        "drug_interactions": {
                  "major": [
                      {
                          "drug": "Warfarin: có thể tăng INR",
                          "mechanism": "Tăng nguy cơ chảy máu"
                      }
                  ],
                  "moderate": [],
                  "minor": [
                      {
                          "drug": "Probenecid: tăng nồng độ cefixime",
                          "mechanism": "Tương tác lâm sàng"
                      },
                      {
                          "drug": "Antacid: giảm hấp thu (cách 2 giờ)",
                          "mechanism": "Tương tác lâm sàng"
                      }
                  ]
              },
              "pregnancy_lactation": {
                  "fda_category": "B - An toàn",
                  "pregnancy_details": "Category B - An toàn - Cần tra cứu thêm thông tin chi tiết về sử dụng trong thai kỳ.",
                  "lactation": {
                      "safety": "Use with caution",
                      "details": "Cần tra cứu thêm thông tin chi tiết về bài tiết vào sữa mẹ.",
                      "recommendation": "Thận trọng khi cho con bú, tra cứu thêm thông tin."
                  }
              },
              "hepatic_adjustment": {
                  "mild": "Không đổi",
                  "moderate": "Thận trọng, có thể giảm liều",
                  "severe": "Thận trọng, giảm liều hoặc tránh dùng",
                  "notes": "Nhiều kháng sinh chuyển hóa qua gan, cần điều chỉnh liều ở suy gan nặng."
              },
              "overdose_management": {
                  "symptoms": [
                      "Cần tra cứu thêm thông tin về triệu chứng quá liều"
                  ],
                  "antidote": "Không có antidote đặc hiệu",
                  "treatment": [
                      "Ngừng ngay thuốc",
                      "Rửa dạ dày nếu uống trong vòng 1-2 giờ (nếu phù hợp)",
                      "Than hoạt tính",
                      "Điều trị hỗ trợ và điều trị triệu chứng",
                      "Theo dõi dấu hiệu sinh tồn"
                  ],
                  "monitoring": "Theo dõi dấu hiệu sinh tồn, triệu chứng lâm sàng"
              },
              "reversal_agents": {
                  "available": False,
                  "agents": []
              },
              "administration_instructions": {
                  "oral": {
                      "with_food": "Có thể uống với hoặc không có thức ăn (trừ khi có chỉ định khác)",
                      "timing": "Theo chỉ định của bác sĩ",
                      "notes": "Cần tra cứu thêm thông tin chi tiết về cách dùng."
                  }
              },
},
    
    "Cefoperazone": {
        "group": "Antibiotic - Cephalosporin (3rd Generation)",
        "vietnamese_name": "Cefoperazone, Cefobid",
        "administration": ["IV", "IM"],
        "indications": [
            "Nhiễm khuẩn do Pseudomonas aeruginosa",
            "Nhiễm khuẩn bệnh viện",
            "Nhiễm khuẩn huyết",
            "Nhiễm khuẩn đường tiết niệu phức tạp",
            "Nhiễm khuẩn da và mô mềm"
        ],
        "contraindications": [
            "Dị ứng cephalosporin hoặc penicillin (thận trọng)",
            "Suy gan nặng",
            "Suy thận nặng (CrCl <10) - cần điều chỉnh liều"
        ],
        "dosage": {
            "adult_standard": "2-4g IV/IM mỗi 12 giờ",
            "adult_severe": "4g IV mỗi 8-12 giờ",
            "adult_pseudomonas": "4g IV mỗi 8 giờ",
            "notes": "Hiệu quả với Pseudomonas aeruginosa. Thải qua cả thận và mật, không cần điều chỉnh thận ở mức độ nhẹ. Có thể gây giảm prothrombin."
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "Không đổi (thải qua mật)",
            "under_30": "Giảm liều nếu CrCl <10 và suy gan"
        },
        "side_effects": [
            "Phát ban",
            "Tiêu chảy",
            "Buồn nôn",
            "Giảm prothrombin (hiếm, nhưng quan trọng)",
            "Chảy máu (hiếm, do giảm prothrombin)",
            "Tăng transaminase (hiếm)",
            "Giảm bạch cầu (hiếm)"
        ],
        "interactions": [
            "Warfarin: tăng INR (do giảm prothrombin)",
            "Ethanol: phản ứng disulfiram-like (buồn nôn, nôn, đỏ mặt)",
            "Probenecid: tăng nồng độ cefoperazone",
            "Aminoglycosides: không pha chung"
        ],
        "pregnancy": "B",
        "mechanism_of_action": "Cephalosporin thế hệ 3, ức chế tổng hợp thành tế bào vi khuẩn bằng cách gắn với penicillin-binding proteins (PBPs). Phổ kháng khuẩn: Gram-âm mạnh (Enterobacteriaceae, Pseudomonas aeruginosa - đặc biệt hiệu quả, Acinetobacter), Gram-dương hạn chế. Kháng được nhiều beta-lactamase. Không hiệu quả với MRSA, Enterococcus, hoặc kỵ khí. Đặc điểm: hiệu quả với Pseudomonas aeruginosa (tương tự ceftazidime), thải qua cả thận và mật (không cần điều chỉnh thận ở mức độ nhẹ), có thể gây giảm prothrombin và phản ứng disulfiram-like với ethanol.",
        "monitoring": [
            "Dấu hiệu nhiễm trùng (sốt, WBC, triệu chứng lâm sàng)",
            "Cấy máu và cấy từ vị trí nhiễm trùng",
            "PT/INR - quan trọng (có thể gây giảm prothrombin)",
            "Dấu hiệu chảy máu (do giảm prothrombin)",
            "Chức năng thận (creatinine, eGFR) - chỉ cần điều chỉnh ở suy thận nặng kèm suy gan",
            "Dấu hiệu nhiễm C. difficile",
            "Chức năng gan (ALT, AST)"
        ],
        "precautions": [
            "Theo dõi PT/INR - có thể gây giảm prothrombin, tăng nguy cơ chảy máu",
            "Tránh ethanol (rượu) - có thể gây phản ứng disulfiram-like (buồn nôn, nôn, đỏ mặt, nhịp tim nhanh)",
            "Thải qua cả thận và mật - không cần điều chỉnh thận ở mức độ nhẹ (trừ khi CrCl <10 và suy gan kèm theo)",
            "Không dùng ở bệnh nhân dị ứng penicillins hoặc cephalosporins",
            "Nguy cơ nhiễm C. difficile",
            "Liều cao hơn cho Pseudomonas (4g q8h)",
            "Pha trong NS hoặc D5W",
            "Không pha trộn với aminoglycosides"
        ],
        "pharmacokinetics": {
            "half_life": "2 giờ",
            "onset": "Ngay lập tức sau khi tiêm IV",
            "duration": "8-12 giờ (liều q8-12h)",
            "protein_binding": "82-93%",
            "metabolism": "Không chuyển hóa đáng kể",
            "clearance": "Thận (25-30%) và mật (70-75%), không cần điều chỉnh thận ở mức độ nhẹ"
        },
        "storage": "Bảo quản bột khô ở nhiệt độ phòng (20-25°C). Sau khi pha: bảo quản ở nhiệt độ phòng 24 giờ, hoặc trong tủ lạnh 10 ngày.",
        "black_box_warnings": "Có thể gây giảm prothrombin và chảy máu. Tránh ethanol (rượu) - phản ứng disulfiram-like.",
        "drug_interactions": {
            "major": [
                {
                    "drug": "Warfarin",
                    "mechanism": "Cefoperazone có thể ức chế tổng hợp vitamin K phụ thuộc vào hệ vi khuẩn đường ruột, làm giảm sản xuất các yếu tố đông máu phụ thuộc vitamin K. Ngoài ra, có thể gây giảm prothrombin trực tiếp.",
                    "effect": "Tăng INR, tăng nguy cơ chảy máu",
                    "management": "Theo dõi PT/INR thường xuyên (ít nhất 2-3 lần/tuần khi bắt đầu dùng cefoperazone). Có thể cần giảm liều warfarin hoặc bổ sung vitamin K. Đặc biệt thận trọng ở bệnh nhân suy gan, dùng kéo dài (>7 ngày)."
                },
                {
                    "drug": "Ethanol (Rượu)",
                    "mechanism": "Cefoperazone có cấu trúc tương tự disulfiram, ức chế aldehyde dehydrogenase, gây tích lũy acetaldehyde.",
                    "effect": "Phản ứng disulfiram-like: buồn nôn, nôn, đỏ mặt, nhịp tim nhanh, khó thở, hạ huyết áp",
                    "management": "TRÁNH TUYỆT ĐỐI ethanol (rượu) trong khi dùng cefoperazone và ít nhất 72 giờ sau liều cuối cùng. Tư vấn bệnh nhân về nguy cơ này."
                }
            ],
            "moderate": [
                {
                    "drug": "Probenecid",
                    "mechanism": "Probenecid ức chế bài tiết ống thận của cefoperazone, làm giảm thải trừ và tăng nồng độ cefoperazone.",
                    "effect": "Tăng nồng độ cefoperazone, tăng thời gian bán thải",
                    "management": "Có thể cần giảm liều cefoperazone. Theo dõi chức năng thận."
                }
            ],
            "minor": []
        },
        "contraindications": {
            "tuyệt_đối": [
                "Dị ứng cephalosporin hoặc beta-lactam (phản ứng type I - sốc phản vệ, phù mạch, phát ban nặng)"
            ],
            "tương_đối": [
                "Dị ứng penicillin (phản ứng chéo ~5-10%) - thận trọng",
                "Suy gan nặng - tăng nguy cơ giảm prothrombin",
                "Suy thận nặng (CrCl <10) kèm suy gan - cần giảm liều",
                "Rối loạn đông máu - tăng nguy cơ chảy máu khi dùng với warfarin",
                "Tiền sử nhiễm C. difficile - tăng nguy cơ tái phát"
            ]
        },
        "contraindications_detail": {
            "tuyệt_đối": [
                "Dị ứng cephalosporin hoặc beta-lactam (phản ứng type I - sốc phản vệ, phù mạch, phát ban nặng)"
            ],
            "tương_đối": [
                "Dị ứng penicillin (phản ứng chéo ~5-10%) - thận trọng",
                "Suy gan nặng - tăng nguy cơ giảm prothrombin",
                "Suy thận nặng (CrCl <10) kèm suy gan - cần giảm liều",
                "Rối loạn đông máu - tăng nguy cơ chảy máu khi dùng với warfarin",
                "Tiền sử nhiễm C. difficile - tăng nguy cơ tái phát"
            ]
        },
        "pregnancy_lactation": {
            "fda_category": "B",
            "pregnancy_details": "Cefoperazone phân loại B - an toàn trong thai kỳ. Cephalosporin là một trong những kháng sinh an toàn nhất trong thai kỳ.",
            "lactation": {
                "safety": "Compatible",
                "details": "Cefoperazone bài tiết vào sữa mẹ ở nồng độ thấp. An toàn cho trẻ bú mẹ.",
                "recommendation": "Có thể dùng khi cho con bú."
            }
        },
        "hepatic_adjustment": {
            "mild": "Không cần điều chỉnh liều, nhưng theo dõi PT/INR",
            "moderate": "Thận trọng, theo dõi PT/INR chặt chẽ",
            "severe": "CHỐNG CHỈ ĐỊNH hoặc thận trọng cực kỳ, theo dõi PT/INR chặt chẽ, có thể cần bổ sung vitamin K",
            "notes": "Cefoperazone thải qua mật (70-75%). Suy gan nặng có thể tăng nguy cơ giảm prothrombin. Theo dõi PT/INR chặt chẽ."
        },
        "overdose_management": {
            "symptoms": [
                "Triệu chứng chảy máu: Chảy máu kéo dài, tăng INR (do giảm prothrombin)",
                "Triệu chứng thần kinh: Co giật (hiếm, suy thận nặng)",
                "Triệu chứng tiêu hóa: Tiêu chảy nặng, buồn nôn, nôn",
                "Triệu chứng dị ứng: Phát ban, phù mạch, sốc phản vệ (nếu dị ứng)"
            ],
            "antidote": "Không có antidote đặc hiệu. Điều trị hỗ trợ và điều trị triệu chứng.",
            "treatment": [
                "Ngừng ngay cefoperazone",
                "Điều trị chảy máu nếu có:",
                "  - Bổ sung vitamin K (10mg IV hoặc IM)",
                "  - Truyền huyết tương tươi đông lạnh (FFP) nếu chảy máu nặng",
                "  - Điều chỉnh liều warfarin nếu đang dùng",
                "Điều trị co giật nếu có: Benzodiazepine (diazepam, lorazepam)",
                "Điều trị dị ứng nếu có: Epinephrine nếu sốc phản vệ, antihistamine, corticosteroid",
                "Theo dõi dấu hiệu sinh tồn: Huyết áp, nhịp tim, nhịp thở, SpO2",
                "Lọc máu: Hemodialysis có thể loại bỏ cefoperazone một phần (25-30% thải qua thận)"
            ],
            "monitoring": "Theo dõi PT/INR, dấu hiệu chảy máu, dấu hiệu thần kinh (co giật), dấu hiệu sinh tồn trong ít nhất 24-48 giờ"
        },
        "reversal_agents": {
            "available": False,
            "agents": [],
            "notes": "Không có antidote đặc hiệu. Điều trị quá liều chủ yếu là điều trị hỗ trợ: ngừng ngay cefoperazone, điều trị chảy máu nếu có (bổ sung vitamin K, FFP), điều trị co giật nếu có, điều trị dị ứng nếu có (epinephrine nếu sốc phản vệ), lọc máu có thể loại bỏ một phần (25-30% thải qua thận)."
        },
        "administration_instructions": {
            "oral": {
                "with_food": "N/A - Chỉ có dạng IV và IM",
                "timing": "N/A - Chỉ có dạng IV và IM"
            },
            "iv": {
                "reconstitution": "Pha với NS (0.9% NaCl) hoặc D5W (5% Dextrose). Nồng độ pha: 10-40mg/ml. Pha 1g trong 10ml = 100mg/ml. Pha 2g trong 50ml = 40mg/ml. Lắc kỹ để hòa tan hoàn toàn.",
                "infusion_rate": "Truyền IV trong 30 phút. Tốc độ: 50ml/30 phút = ~1.7ml/phút.",
                "compatibility": ["NS (0.9% NaCl)", "D5W (5% Dextrose)"],
                "incompatibility": [
                    "Aminoglycosides - bất hoạt, không pha chung",
                    "Vancomycin - có thể tạo kết tủa",
                    "Các thuốc có tính kiềm hoặc acid mạnh"
                ],
                "notes": "QUAN TRỌNG: 1) Theo dõi PT/INR (có thể gây giảm prothrombin), 2) Tránh ethanol (phản ứng disulfiram-like), 3) Thải qua cả thận và mật → không cần điều chỉnh thận ở mức độ nhẹ, 4) Đặc biệt hiệu quả với Pseudomonas aeruginosa."
            },
            "im": {
                "reconstitution": "Pha với lidocaine 1% (không có epinephrine) để giảm đau. Nồng độ pha: 200mg/ml (1g trong 5ml lidocaine 1%).",
                "injection_site": "Tiêm sâu vào cơ (gluteus maximus hoặc vastus lateralis).",
                "notes": "Pha với lidocaine 1% để giảm đau tại chỗ. Tiêm sâu vào cơ."
            }
        },
        "references": {
            "primary_sources": [
                "FDA Drug Label - Cefobid (cefoperazone)",
                "IDSA Guidelines - Hospital-Acquired Pneumonia",
                "UpToDate - Cefoperazone: Drug Information"
            ],
            "last_updated": "2025-02-05",
            "evidence_level": "A"
        }
    },
    
    "Cefotaxime": {
        "group": "Antibiotic - Cephalosporin (3rd Generation)",
        "vietnamese_name": "Cefotaxime, Claforan",
        "administration": ["IV", "IM"],
        "indications": [
            "Nhiễm khuẩn nặng",
            "Viêm màng não",
            "Nhiễm khuẩn bệnh viện",
            "Nhiễm khuẩn đường tiết niệu",
            "Viêm phổi",
            "Nhiễm khuẩn ổ bụng",
            "Nhiễm khuẩn da và mô mềm"
        ],
        "contraindications": [
            "Dị ứng cephalosporin hoặc penicillin (thận trọng)",
            "Suy thận nặng (CrCl <10) - cần điều chỉnh liều"
        ],
        "dosage": {
            "adult_standard": "1-2g IV/IM mỗi 6-8 giờ",
            "adult_severe": "2g IV mỗi 6-8 giờ",
            "adult_meningitis": "2g IV mỗi 4-6 giờ",
            "adult_severe_infection": "2g IV mỗi 4 giờ (tối đa 12g/ngày)",
            "pediatric_standard": "50-100mg/kg IV/IM mỗi 6-8 giờ (tối đa 12g/ngày)",
            "pediatric_meningitis": "50-75mg/kg IV mỗi 6 giờ (tối đa 12g/ngày)",
            "notes": "Thời gian bán thải ngắn (1-1.5 giờ), cần dùng nhiều lần/ngày. Khác với ceftriaxone (q24h)"
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "1-2g IV mỗi 8-12 giờ",
            "under_30": "1-2g IV mỗi 12-24 giờ",
            "hemodialysis": "1-2g IV sau lọc máu"
        },
        "side_effects": [
            "Tiêu chảy",
            "Phát ban",
            "Tăng transaminase",
            "Giảm bạch cầu (hiếm)",
            "Co giật (hiếm, ở suy thận nặng)",
            "Phản ứng tại chỗ tiêm"
        ],
        "interactions": [
            "Warfarin: tăng INR",
            "Probenecid: tăng nồng độ cefotaxime",
            "Aminoglycosides: không pha chung"
        ],
        "pregnancy": "B - An toàn",
        "mechanism_of_action": "Cephalosporin thế hệ 3, phổ rộng. Ức chế tổng hợp thành tế bào vi khuẩn bằng cách gắn với penicillin-binding proteins (PBPs). Phổ kháng khuẩn: Gram-dương (một số), Gram-âm mạnh (Enterobacteriaceae, Neisseria, H. influenzae), và một số kỵ khí. Kháng được nhiều beta-lactamase. Không hiệu quả với Pseudomonas aeruginosa, Enterococcus, hoặc MRSA. Đặc điểm: thời gian bán thải ngắn (1-1.5 giờ) → cần dùng nhiều lần/ngày (q6-8h), khác với ceftriaxone (q24h).",
        "monitoring": [
            "Dấu hiệu nhiễm trùng (sốt, WBC, CRP)",
            "Cấy máu và cấy từ vị trí nhiễm trùng",
            "Chức năng gan (ALT, AST, bilirubin)",
            "Chức năng thận (creatinine, eGFR) - cần điều chỉnh liều",
            "Dấu hiệu nhiễm C. difficile",
            "Co giật (hiếm, nhưng có thể ở suy thận nặng)",
            "Phản ứng tại chỗ tiêm (đau, viêm tĩnh mạch)",
            "PT/INR (nếu dùng với warfarin)"
        ],
        "precautions": [
            "Điều chỉnh liều theo chức năng thận (eGFR) - quan trọng",
            "Không dùng ở bệnh nhân dị ứng penicillins hoặc cephalosporins (phản ứng chéo ~5-10%)",
            "Nguy cơ nhiễm C. difficile - theo dõi tiêu chảy",
            "Thời gian bán thải ngắn → cần dùng nhiều lần/ngày (q6-8h), khác với ceftriaxone",
            "Pha trong NS, D5W, hoặc LR, tiêm IV hoặc IM",
            "Tiêm IM: pha với lidocaine 1% để giảm đau",
            "Không pha trộn với aminoglycosides (bất hoạt)",
            "Theo dõi INR nếu dùng với warfarin"
        ],
        "pharmacokinetics": {
            "half_life": "1-1.5 giờ (ngắn hơn ceftriaxone)",
            "onset": "Ngay lập tức sau khi tiêm IV",
            "duration": "6-8 giờ (liều q6-8h)",
            "protein_binding": "30-50%",
            "metabolism": "Chuyển hóa một phần ở gan thành desacetylcefotaxime (có hoạt tính)",
            "clearance": "Chủ yếu qua thận (60% bài tiết nguyên dạng, 40% dạng desacetyl), cần điều chỉnh thận"
        },
        "storage": "Bảo quản bột khô ở nhiệt độ phòng (20-25°C). Sau khi pha: bảo quản ở nhiệt độ phòng 24 giờ, hoặc trong tủ lạnh 10 ngày. Không đông lạnh.",
        "black_box_warnings": "Không có black box warning. Tuy nhiên, cần điều chỉnh liều theo chức năng thận để tránh độc tính.",
        "references": {
            "primary_sources": [
                "FDA Drug Label - Cefotaxime (Claforan)",
                "IDSA Guidelines - Community-Acquired Pneumonia, Meningitis",
                "UpToDate - Cefotaxime: Drug Information",
                "Medscape - Cefotaxime Drug Reference",
                "Goodman & Gilman's The Pharmacological Basis of Therapeutics (14th ed)",
                "Lexicomp Online - Cefotaxime Monograph"
            ],
            "last_updated": "2025-02-05",
            "evidence_level": "A - Dựa trên FDA drug labels, IDSA guidelines, và dữ liệu lâm sàng từ nhiều nguồn"
        },
        "risk_flags": {
            "high_alert": False,
            "narrow_therapeutic_index": False,
            "icu_critical_care_only": False,
            "bleeding_risk": None,
            "organ_toxicity": {"neurological": "Seizures (rare, in renal impairment)", "hepatic": "Hepatotoxicity (rare)", "hematologic": "Neutropenia (rare)", "gastrointestinal": "C. difficile infection"},
            "qt_prolongation": False,
            "hepatotoxicity": "Rare",
            "nephrotoxicity": False,
            "requires_monitoring": ["Renal function (CrCl - dose adjustment required)", "Neurological signs (seizures in renal impairment)", "C. difficile infection signs", "Hepatic function (ALT, AST)", "CBC (neutropenia risk)", "PT/INR (if used with warfarin)"],
            "look_alike_sound_alike": ["Cefotaxime", "Cefepime", "Ceftazidime"]
        },
        "guideline_tags": [
            "IDSA Guidelines - Community-Acquired Pneumonia",
            "IDSA Guidelines - Meningitis",
            "IDSA Guidelines - Hospital-Acquired Pneumonia",
            "WHO Essential Medicines List"
        ],
        "last_updated": "2025-02-18",
        "drug_interactions": {
                  "major": [
                      {
                          "drug": "Warfarin: tăng INR",
                          "mechanism": "Tăng nguy cơ chảy máu"
                      }
                  ],
                  "moderate": [],
                  "minor": [
                      {
                          "drug": "Probenecid: tăng nồng độ cefotaxime",
                          "mechanism": "Tương tác lâm sàng"
                      },
                      {
                          "drug": "Aminoglycosides: không pha chung",
                          "mechanism": "Tương tác lâm sàng"
                      }
                  ]
              },
              "pregnancy_lactation": {
                  "fda_category": "B - An toàn",
                  "pregnancy_details": "Category B - An toàn - Cần tra cứu thêm thông tin chi tiết về sử dụng trong thai kỳ.",
                  "lactation": {
                      "safety": "Use with caution",
                      "details": "Cần tra cứu thêm thông tin chi tiết về bài tiết vào sữa mẹ.",
                      "recommendation": "Thận trọng khi cho con bú, tra cứu thêm thông tin."
                  }
              },
              "hepatic_adjustment": {
                  "mild": "Không đổi",
                  "moderate": "Thận trọng, có thể giảm liều",
                  "severe": "Thận trọng, giảm liều hoặc tránh dùng",
                  "notes": "Nhiều kháng sinh chuyển hóa qua gan, cần điều chỉnh liều ở suy gan nặng."
              },
              "overdose_management": {
                  "symptoms": [
                      "Cần tra cứu thêm thông tin về triệu chứng quá liều"
                  ],
                  "antidote": "Không có antidote đặc hiệu",
                  "treatment": [
                      "Ngừng ngay thuốc",
                      "Rửa dạ dày nếu uống trong vòng 1-2 giờ (nếu phù hợp)",
                      "Than hoạt tính",
                      "Điều trị hỗ trợ và điều trị triệu chứng",
                      "Theo dõi dấu hiệu sinh tồn"
                  ],
                  "monitoring": "Theo dõi dấu hiệu sinh tồn, triệu chứng lâm sàng"
              },
              "reversal_agents": {
                  "available": False,
                  "agents": []
              },
              "administration_instructions": {
                  "iv": {
                      "reconstitution": "Cần tra cứu",
                      "infusion_rate": "Cần tra cứu",
                      "compatibility": [
                          "Cần tra cứu"
                      ],
                      "incompatibility": [],
                      "notes": "Cần tra cứu thêm thông tin chi tiết."
                  }
              },
},
    
    "Cefotetan": {
        "group": "Antibiotic - Cephalosporin (2nd Generation, Cephamycin)",
        "vietnamese_name": "Cefotetan, Cefotan",
        "administration": ["IV", "IM"],
        "indications": [
            "Dự phòng phẫu thuật (đặc biệt phẫu thuật bụng, phụ khoa)",
            "Nhiễm khuẩn ổ bụng",
            "Nhiễm khuẩn vùng chậu",
            "Nhiễm khuẩn da và mô mềm",
            "Nhiễm khuẩn đường tiết niệu phức tạp"
        ],
        "contraindications": [
            "Dị ứng cephalosporin hoặc penicillin (thận trọng)",
            "Suy thận nặng (CrCl <10) - cần điều chỉnh liều",
            "Rối loạn đông máu (có thể gây giảm prothrombin)"
        ],
        "dosage": {
            "adult_standard": "1-2g IV/IM mỗi 12 giờ",
            "adult_severe": "2g IV mỗi 12 giờ",
            "adult_prophylaxis": "1-2g IV 30-60 phút trước phẫu thuật",
            "adult_prophylaxis_repeat": "1-2g IV mỗi 6 giờ trong phẫu thuật dài",
            "notes": "Thời gian bán thải dài (3-4.5 giờ), dùng 2 lần/ngày. Đặc biệt hiệu quả với kỵ khí (Bacteroides fragilis)."
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "1-2g IV mỗi 24 giờ",
            "under_30": "1-2g IV mỗi 48 giờ",
            "hemodialysis": "1-2g IV sau lọc máu"
        },
        "side_effects": [
            "Phát ban",
            "Tiêu chảy",
            "Buồn nôn",
            "Giảm prothrombin (hiếm, nhưng quan trọng)",
            "Chảy máu (hiếm, do giảm prothrombin)",
            "Tăng transaminase (hiếm)",
            "Giảm bạch cầu (hiếm)"
        ],
        "interactions": [
            "Warfarin: tăng INR (do giảm prothrombin)",
            "Ethanol: phản ứng disulfiram-like (buồn nôn, nôn, đỏ mặt)",
            "Probenecid: tăng nồng độ cefotetan",
            "Aminoglycosides: không pha chung"
        ],
        "pregnancy": "B - An toàn",
        "mechanism_of_action": "Cephalosporin thế hệ 2 thuộc nhóm cephamycin, ức chế tổng hợp thành tế bào vi khuẩn bằng cách gắn với penicillin-binding proteins (PBPs). Phổ kháng khuẩn: Gram-dương (Staphylococcus, Streptococcus), Gram-âm (E. coli, Klebsiella, Proteus), và đặc biệt hiệu quả với kỵ khí (Bacteroides fragilis - do có cấu trúc cephamycin kháng beta-lactamase). Không hiệu quả với MRSA, Enterococcus, Pseudomonas. Đặc điểm: thời gian bán thải dài (3-4.5 giờ), dùng 2 lần/ngày. Có thể gây giảm prothrombin và phản ứng disulfiram-like với ethanol.",
        "monitoring": [
            "Dấu hiệu nhiễm trùng (sốt, WBC, triệu chứng lâm sàng)",
            "Cấy máu và cấy từ vị trí nhiễm trùng",
            "PT/INR - quan trọng (có thể gây giảm prothrombin)",
            "Dấu hiệu chảy máu (do giảm prothrombin)",
            "Chức năng thận (creatinine, eGFR) - cần điều chỉnh liều",
            "Dấu hiệu nhiễm C. difficile",
            "Chức năng gan (ALT, AST)"
        ],
        "precautions": [
            "Theo dõi PT/INR - có thể gây giảm prothrombin, tăng nguy cơ chảy máu",
            "Tránh ethanol (rượu) - có thể gây phản ứng disulfiram-like (buồn nôn, nôn, đỏ mặt, nhịp tim nhanh)",
            "Điều chỉnh liều theo chức năng thận",
            "Không dùng ở bệnh nhân dị ứng penicillins hoặc cephalosporins",
            "Nguy cơ nhiễm C. difficile",
            "Dự phòng phẫu thuật: tiêm 30-60 phút trước khi rạch da",
            "Pha trong NS hoặc D5W",
            "Không pha trộn với aminoglycosides"
        ],
        "pharmacokinetics": {
            "half_life": "3-4.5 giờ (dài hơn các cephalosporin thế hệ 2 khác)",
            "onset": "Ngay lập tức sau khi tiêm IV",
            "duration": "12 giờ (liều q12h)",
            "protein_binding": "78-88%",
            "metabolism": "Không chuyển hóa đáng kể",
            "clearance": "Chủ yếu qua thận (50-80% bài tiết nguyên dạng), cần điều chỉnh thận"
        },
        "storage": "Bảo quản bột khô ở nhiệt độ phòng (20-25°C). Sau khi pha: bảo quản ở nhiệt độ phòng 24 giờ, hoặc trong tủ lạnh 10 ngày.",
        "black_box_warnings": "Có thể gây giảm prothrombin và chảy máu. Tránh ethanol (rượu) - phản ứng disulfiram-like.",
        "drug_interactions": {
            "major": [
                {
                    "drug": "Warfarin",
                    "mechanism": "Cefotetan có thể ức chế tổng hợp vitamin K phụ thuộc vào hệ vi khuẩn đường ruột, làm giảm sản xuất các yếu tố đông máu phụ thuộc vitamin K. Ngoài ra, có thể gây giảm prothrombin trực tiếp.",
                    "effect": "Tăng INR, tăng nguy cơ chảy máu",
                    "management": "Theo dõi PT/INR thường xuyên (ít nhất 2-3 lần/tuần khi bắt đầu dùng cefotetan). Có thể cần giảm liều warfarin hoặc bổ sung vitamin K. Đặc biệt thận trọng ở bệnh nhân suy gan, dùng kéo dài (>7 ngày)."
                },
                {
                    "drug": "Ethanol (Rượu)",
                    "mechanism": "Cefotetan có cấu trúc tương tự disulfiram, ức chế aldehyde dehydrogenase, gây tích lũy acetaldehyde.",
                    "effect": "Phản ứng disulfiram-like: buồn nôn, nôn, đỏ mặt, nhịp tim nhanh, khó thở, hạ huyết áp",
                    "management": "TRÁNH TUYỆT ĐỐI ethanol (rượu) trong khi dùng cefotetan và ít nhất 72 giờ sau liều cuối cùng. Tư vấn bệnh nhân về nguy cơ này."
                }
            ],
            "moderate": [
                {
                    "drug": "Probenecid",
                    "mechanism": "Probenecid ức chế bài tiết ống thận của cefotetan, làm giảm thải trừ và tăng nồng độ cefotetan.",
                    "effect": "Tăng nồng độ cefotetan, tăng thời gian bán thải",
                    "management": "Có thể cần giảm liều cefotetan. Theo dõi chức năng thận."
                }
            ],
            "minor": []
        },
        "contraindications": {
            "tuyệt_đối": [
                "Dị ứng cephalosporin hoặc beta-lactam (phản ứng type I - sốc phản vệ, phù mạch, phát ban nặng)",
                "Rối loạn đông máu nặng (tăng nguy cơ chảy máu do giảm prothrombin)"
            ],
            "tương_đối": [
                "Dị ứng penicillin (phản ứng chéo ~5-10%) - thận trọng",
                "Suy thận nặng (CrCl <10) - cần điều chỉnh liều",
                "Suy gan nặng - tăng nguy cơ giảm prothrombin",
                "Tiền sử nhiễm C. difficile - tăng nguy cơ tái phát",
                "Đang dùng warfarin - tăng nguy cơ chảy máu"
            ]
        },
        "contraindications_detail": {
            "tuyệt_đối": [
                "Dị ứng cephalosporin hoặc beta-lactam (phản ứng type I - sốc phản vệ, phù mạch, phát ban nặng)",
                "Rối loạn đông máu nặng (tăng nguy cơ chảy máu do giảm prothrombin)"
            ],
            "tương_đối": [
                "Dị ứng penicillin (phản ứng chéo ~5-10%) - thận trọng",
                "Suy thận nặng (CrCl <10) - cần điều chỉnh liều",
                "Suy gan nặng - tăng nguy cơ giảm prothrombin",
                "Tiền sử nhiễm C. difficile - tăng nguy cơ tái phát",
                "Đang dùng warfarin - tăng nguy cơ chảy máu"
            ]
        },
        "pregnancy_lactation": {
            "fda_category": "B",
            "pregnancy_details": "Cefotetan phân loại B - an toàn trong thai kỳ. Cephalosporin là một trong những kháng sinh an toàn nhất trong thai kỳ.",
            "lactation": {
                "safety": "Compatible",
                "details": "Cefotetan bài tiết vào sữa mẹ ở nồng độ thấp. An toàn cho trẻ bú mẹ.",
                "recommendation": "Có thể dùng khi cho con bú."
            }
        },
        "hepatic_adjustment": {
            "mild": "Không cần điều chỉnh liều",
            "moderate": "Thận trọng, theo dõi PT/INR",
            "severe": "Thận trọng, theo dõi PT/INR chặt chẽ, có thể cần bổ sung vitamin K",
            "notes": "Suy gan có thể tăng nguy cơ giảm prothrombin. Theo dõi PT/INR chặt chẽ."
        },
        "overdose_management": {
            "symptoms": [
                "Triệu chứng thần kinh: Co giật (hiếm, suy thận nặng)",
                "Triệu chứng chảy máu: Chảy máu kéo dài, tăng INR (do giảm prothrombin)",
                "Triệu chứng tiêu hóa: Tiêu chảy nặng, buồn nôn, nôn",
                "Triệu chứng dị ứng: Phát ban, phù mạch, sốc phản vệ (nếu dị ứng)"
            ],
            "antidote": "Không có antidote đặc hiệu. Điều trị hỗ trợ và điều trị triệu chứng.",
            "treatment": [
                "Ngừng ngay cefotetan",
                "Điều trị chảy máu nếu có:",
                "  - Bổ sung vitamin K (10mg IV hoặc IM)",
                "  - Truyền huyết tương tươi đông lạnh (FFP) nếu chảy máu nặng",
                "  - Điều chỉnh liều warfarin nếu đang dùng",
                "Điều trị co giật nếu có: Benzodiazepine (diazepam, lorazepam)",
                "Điều trị dị ứng nếu có: Epinephrine nếu sốc phản vệ, antihistamine, corticosteroid",
                "Theo dõi dấu hiệu sinh tồn: Huyết áp, nhịp tim, nhịp thở, SpO2",
                "Lọc máu: Hemodialysis có thể loại bỏ cefotetan một phần"
            ],
            "monitoring": "Theo dõi PT/INR, dấu hiệu chảy máu, dấu hiệu thần kinh (co giật), dấu hiệu sinh tồn trong ít nhất 24-48 giờ."
        },
        "reversal_agents": {
            "available": False,
            "agents": [],
            "notes": "Không có antidote đặc hiệu. Điều trị quá liều chủ yếu là hỗ trợ. Nếu có chảy máu do giảm prothrombin: bổ sung vitamin K (10mg IV/IM) hoặc truyền huyết tương tươi đông lạnh (FFP). Lọc máu có thể loại bỏ một phần."
        },
        "administration_instructions": {
            "oral": {
                "with_food": "N/A - Chỉ có dạng IV và IM",
                "timing": "N/A - Chỉ có dạng IV và IM"
            },
            "iv": {
                "reconstitution": "Pha với NS (0.9% NaCl) hoặc D5W (5% Dextrose). Nồng độ pha: 10-40mg/ml. Pha 1g trong 10ml = 100mg/ml. Pha 2g trong 50ml = 40mg/ml. Lắc kỹ để hòa tan hoàn toàn.",
                "infusion_rate": "Truyền IV trong 30 phút. Tốc độ: 50ml/30 phút = ~1.7ml/phút.",
                "compatibility": ["NS (0.9% NaCl)", "D5W (5% Dextrose)"],
                "incompatibility": [
                    "Aminoglycosides - bất hoạt, không pha chung",
                    "Vancomycin - có thể tạo kết tủa",
                    "Các thuốc có tính kiềm hoặc acid mạnh"
                ],
                "notes": "QUAN TRỌNG: 1) Theo dõi PT/INR (có thể gây giảm prothrombin), 2) Tránh ethanol (phản ứng disulfiram-like), 3) Thời gian bán thải dài (3-4.5 giờ) → dùng 2 lần/ngày, 4) Đặc biệt hiệu quả với kỵ khí (Bacteroides fragilis)."
            },
            "im": {
                "reconstitution": "Pha với lidocaine 1% (không có epinephrine) để giảm đau. Nồng độ pha: 200mg/ml (1g trong 5ml lidocaine 1%).",
                "injection_site": "Tiêm sâu vào cơ (gluteus maximus hoặc vastus lateralis).",
                "notes": "Pha với lidocaine 1% để giảm đau tại chỗ. Tiêm sâu vào cơ."
            }
        },
        "references": {
            "primary_sources": [
                "FDA Drug Label - Cefotetan (Cefotan)",
                "IDSA Guidelines - Surgical Prophylaxis",
                "UpToDate - Cefotetan: Drug Information",
                "Medscape - Cefotetan Drug Reference"
            ],
            "last_updated": "2025-02-05",
            "evidence_level": "A"
        }
    },
    
    "Cefoxitin": {
        "group": "Antibiotic - Cephalosporin (2nd Generation, Cephamycin)",
        "vietnamese_name": "Cefoxitin, Mefoxin",
        "administration": ["IV", "IM"],
        "indications": [
            "Dự phòng phẫu thuật (đặc biệt phẫu thuật bụng, phụ khoa, đại tràng)",
            "Nhiễm khuẩn ổ bụng",
            "Nhiễm khuẩn vùng chậu",
            "Nhiễm khuẩn da và mô mềm",
            "Nhiễm khuẩn đường tiết niệu phức tạp",
            "Nhiễm khuẩn do kỵ khí"
        ],
        "contraindications": [
            "Dị ứng cephalosporin hoặc penicillin (thận trọng)",
            "Suy thận nặng (CrCl <10) - cần điều chỉnh liều"
        ],
        "dosage": {
            "adult_standard": "1-2g IV/IM mỗi 6-8 giờ",
            "adult_severe": "2g IV mỗi 4-6 giờ",
            "adult_prophylaxis": "1-2g IV 30-60 phút trước phẫu thuật",
            "adult_prophylaxis_repeat": "1-2g IV mỗi 2-4 giờ trong phẫu thuật dài",
            "notes": "Thời gian bán thải ngắn (0.7-1 giờ), cần dùng nhiều lần/ngày (q6-8h). Đặc biệt hiệu quả với kỵ khí (Bacteroides fragilis)."
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "1-2g IV mỗi 8-12 giờ",
            "under_30": "1-2g IV mỗi 12-24 giờ",
            "hemodialysis": "1-2g IV sau lọc máu"
        },
        "side_effects": [
            "Phát ban",
            "Tiêu chảy",
            "Buồn nôn",
            "Tăng transaminase (hiếm)",
            "Giảm bạch cầu (hiếm)",
            "Phản ứng tại chỗ tiêm"
        ],
        "interactions": [
            "Warfarin: có thể tăng INR",
            "Probenecid: tăng nồng độ cefoxitin",
            "Aminoglycosides: không pha chung"
        ],
        "pregnancy": "B - An toàn",
        "mechanism_of_action": "Cephalosporin thế hệ 2 thuộc nhóm cephamycin, ức chế tổng hợp thành tế bào vi khuẩn bằng cách gắn với penicillin-binding proteins (PBPs). Phổ kháng khuẩn: Gram-dương (Staphylococcus, Streptococcus), Gram-âm (E. coli, Klebsiella, Proteus), và đặc biệt hiệu quả với kỵ khí (Bacteroides fragilis - do có cấu trúc cephamycin kháng beta-lactamase). Không hiệu quả với MRSA, Enterococcus, Pseudomonas. Đặc điểm: thời gian bán thải ngắn (0.7-1 giờ), cần dùng nhiều lần/ngày (q6-8h). Được dùng rộng rãi trong dự phòng phẫu thuật bụng và phụ khoa.",
        "monitoring": [
            "Dấu hiệu nhiễm trùng (sốt, WBC, triệu chứng lâm sàng)",
            "Cấy máu và cấy từ vị trí nhiễm trùng",
            "Chức năng thận (creatinine, eGFR) - cần điều chỉnh liều",
            "Dấu hiệu nhiễm C. difficile",
            "Chức năng gan (ALT, AST)",
            "Phản ứng tại chỗ tiêm (đau, viêm tĩnh mạch)",
            "PT/INR (nếu dùng với warfarin)"
        ],
        "precautions": [
            "Điều chỉnh liều theo chức năng thận - quan trọng",
            "Không dùng ở bệnh nhân dị ứng penicillins hoặc cephalosporins",
            "Nguy cơ nhiễm C. difficile",
            "Thời gian bán thải ngắn → cần dùng nhiều lần/ngày (q6-8h)",
            "Dự phòng phẫu thuật: tiêm 30-60 phút trước khi rạch da",
            "Pha trong NS hoặc D5W",
            "Không pha trộn với aminoglycosides (bất hoạt)",
            "Theo dõi INR nếu dùng với warfarin"
        ],
        "pharmacokinetics": {
            "half_life": "0.7-1 giờ (ngắn)",
            "onset": "Ngay lập tức sau khi tiêm IV",
            "duration": "6-8 giờ (liều q6-8h)",
            "protein_binding": "65-79%",
            "metabolism": "Không chuyển hóa đáng kể",
            "clearance": "Chủ yếu qua thận (85% bài tiết nguyên dạng), cần điều chỉnh thận"
        },
        "storage": "Bảo quản bột khô ở nhiệt độ phòng (20-25°C). Sau khi pha: bảo quản ở nhiệt độ phòng 24 giờ, hoặc trong tủ lạnh 10 ngày.",
        "black_box_warnings": "Không có black box warning. Tuy nhiên, cần điều chỉnh liều theo chức năng thận.",
        "drug_interactions": {
            "major": [
                {
                    "drug": "Warfarin",
                    "mechanism": "Cefoxitin có thể ức chế tổng hợp vitamin K phụ thuộc vào hệ vi khuẩn đường ruột, làm giảm sản xuất các yếu tố đông máu phụ thuộc vitamin K.",
                    "effect": "Tăng INR, tăng nguy cơ chảy máu",
                    "management": "Theo dõi INR thường xuyên (ít nhất 2-3 lần/tuần khi bắt đầu dùng cefoxitin). Có thể cần giảm liều warfarin. Đặc biệt thận trọng ở bệnh nhân suy gan, dùng kéo dài (>7 ngày)."
                }
            ],
            "moderate": [
                {
                    "drug": "Probenecid",
                    "mechanism": "Probenecid ức chế bài tiết ống thận của cefoxitin, làm giảm thải trừ và tăng nồng độ cefoxitin.",
                    "effect": "Tăng nồng độ cefoxitin, tăng thời gian bán thải",
                    "management": "Có thể cần giảm liều cefoxitin. Theo dõi chức năng thận."
                },
                {
                    "drug": "Aminoglycosides (Gentamicin, Amikacin, Tobramycin)",
                    "mechanism": "Cefoxitin có thể bất hoạt aminoglycosides khi pha chung. Cả hai đều có thể gây độc thận, tác dụng cộng dồn.",
                    "effect": "Bất hoạt aminoglycosides khi pha chung, tăng nguy cơ độc thận",
                    "management": "Không pha chung. Truyền riêng biệt. Theo dõi chức năng thận chặt chẽ."
                }
            ],
            "minor": []
        },
        "contraindications": {
            "tuyệt_đối": [
                "Dị ứng cephalosporin hoặc beta-lactam (phản ứng type I - sốc phản vệ, phù mạch, phát ban nặng)"
            ],
            "tương_đối": [
                "Dị ứng penicillin (phản ứng chéo ~5-10%) - thận trọng",
                "Suy thận nặng (CrCl <10) - cần điều chỉnh liều",
                "Tiền sử nhiễm C. difficile - tăng nguy cơ tái phát",
                "Rối loạn đông máu - tăng nguy cơ chảy máu khi dùng với warfarin"
            ]
        },
        "contraindications_detail": {
            "tuyệt_đối": [
                "Dị ứng cephalosporin hoặc beta-lactam (phản ứng type I - sốc phản vệ, phù mạch, phát ban nặng)"
            ],
            "tương_đối": [
                "Dị ứng penicillin (phản ứng chéo ~5-10%) - thận trọng",
                "Suy thận nặng (CrCl <10) - cần điều chỉnh liều",
                "Tiền sử nhiễm C. difficile - tăng nguy cơ tái phát",
                "Rối loạn đông máu - tăng nguy cơ chảy máu khi dùng với warfarin"
            ]
        },
        "pregnancy_lactation": {
            "fda_category": "B",
            "pregnancy_details": "Cefoxitin phân loại B - an toàn trong thai kỳ. Cephalosporin là một trong những kháng sinh an toàn nhất trong thai kỳ.",
            "lactation": {
                "safety": "Compatible",
                "details": "Cefoxitin bài tiết vào sữa mẹ ở nồng độ thấp. An toàn cho trẻ bú mẹ.",
                "recommendation": "Có thể dùng khi cho con bú."
            }
        },
        "hepatic_adjustment": {
            "mild": "Không cần điều chỉnh liều",
            "moderate": "Không cần điều chỉnh liều",
            "severe": "Không cần điều chỉnh liều, nhưng thận trọng",
            "notes": "Cefoxitin không chuyển hóa qua gan, thải trừ chủ yếu qua thận. Suy gan ít ảnh hưởng."
        },
        "overdose_management": {
            "symptoms": [
                "Triệu chứng thần kinh: Co giật (hiếm, suy thận nặng)",
                "Triệu chứng tiêu hóa: Tiêu chảy nặng, buồn nôn, nôn",
                "Triệu chứng dị ứng: Phát ban, phù mạch, sốc phản vệ (nếu dị ứng)",
                "Triệu chứng thận: Suy thận cấp (hiếm với liều thông thường)"
            ],
            "antidote": "Không có antidote đặc hiệu. Điều trị hỗ trợ và điều trị triệu chứng.",
            "treatment": [
                "Ngừng ngay cefoxitin",
                "Điều trị co giật nếu có: Benzodiazepine (diazepam, lorazepam)",
                "Điều trị dị ứng nếu có: Epinephrine nếu sốc phản vệ, antihistamine, corticosteroid",
                "Điều trị suy thận cấp nếu có: Bù dịch đầy đủ, điều chỉnh điện giải, lọc máu nếu cần",
                "Theo dõi dấu hiệu sinh tồn: Huyết áp, nhịp tim, nhịp thở, SpO2",
                "Lọc máu: Hemodialysis có thể loại bỏ cefoxitin một phần (85% thải qua thận)"
            ],
            "monitoring": "Theo dõi dấu hiệu thần kinh (co giật), chức năng thận (creatinine, BUN, lượng nước tiểu), dấu hiệu sinh tồn trong ít nhất 24-48 giờ."
        },
        "reversal_agents": {
            "available": False,
            "agents": [],
            "notes": "Không có antidote đặc hiệu. Điều trị quá liều chủ yếu là hỗ trợ. Lọc máu có thể loại bỏ một phần nhưng không được khuyến nghị thường quy."
        },
        "administration_instructions": {
            "oral": {
                "with_food": "N/A - Chỉ có dạng IV và IM",
                "timing": "N/A - Chỉ có dạng IV và IM"
            },
            "iv": {
                "reconstitution": "Pha với NS (0.9% NaCl) hoặc D5W (5% Dextrose). Nồng độ pha: 10-40mg/ml. Pha 1g trong 10ml = 100mg/ml. Pha 2g trong 50ml = 40mg/ml. Lắc kỹ để hòa tan hoàn toàn.",
                "infusion_rate": "Truyền IV trong 30 phút. Tốc độ: 50ml/30 phút = ~1.7ml/phút.",
                "compatibility": ["NS (0.9% NaCl)", "D5W (5% Dextrose)"],
                "incompatibility": [
                    "Aminoglycosides - bất hoạt, không pha chung",
                    "Vancomycin - có thể tạo kết tủa",
                    "Các thuốc có tính kiềm hoặc acid mạnh"
                ],
                "notes": "QUAN TRỌNG: 1) Thời gian bán thải ngắn (0.7-1 giờ) → cần dùng nhiều lần/ngày (q6-8h), 2) Đặc biệt hiệu quả với kỵ khí (Bacteroides fragilis), 3) Không pha chung với aminoglycosides (bất hoạt), 4) Dự phòng phẫu thuật: tiêm 30-60 phút trước khi rạch da."
            },
            "im": {
                "reconstitution": "Pha với lidocaine 1% (không có epinephrine) để giảm đau. Nồng độ pha: 200mg/ml (1g trong 5ml lidocaine 1%).",
                "injection_site": "Tiêm sâu vào cơ (gluteus maximus hoặc vastus lateralis).",
                "notes": "Pha với lidocaine 1% để giảm đau tại chỗ. Tiêm sâu vào cơ."
            }
        },
        "references": {
            "primary_sources": [
                "FDA Drug Label - Cefoxitin (Mefoxin)",
                "IDSA Guidelines - Surgical Prophylaxis",
                "UpToDate - Cefoxitin: Drug Information",
                "Medscape - Cefoxitin Drug Reference"
            ],
            "last_updated": "2025-02-05",
            "evidence_level": "A"
        }
    },
    
    "Cefpirome": {
        "group": "Antibiotic - Cephalosporin (4th Generation)",
        "vietnamese_name": "Cefpirome, Cefrom",
        "administration": ["IV", "IM"],
        "indications": [
            "Nhiễm khuẩn bệnh viện nặng",
            "Nhiễm khuẩn huyết",
            "Viêm phổi bệnh viện",
            "Nhiễm khuẩn đường tiết niệu phức tạp",
            "Nhiễm khuẩn da và mô mềm",
            "Sốt giảm bạch cầu (febrile neutropenia)"
        ],
        "contraindications": [
            "Dị ứng cephalosporin hoặc penicillin (thận trọng)",
            "Suy thận nặng (CrCl <10) - cần điều chỉnh liều"
        ],
        "dosage": {
            "adult_standard": "1-2g IV/IM mỗi 12 giờ",
            "adult_severe": "2g IV mỗi 12 giờ",
            "adult_febrile_neutropenia": "2g IV mỗi 12 giờ",
            "adult_pseudomonas": "2g IV mỗi 8-12 giờ",
            "notes": "Cephalosporin thế hệ 4, phổ rộng. Hiệu quả với cả Gram-dương và Gram-âm, kể cả Pseudomonas. Ít dùng hơn cefepime."
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "1-2g IV mỗi 12-24 giờ",
            "under_30": "1g IV mỗi 24 giờ",
            "hemodialysis": "1g IV sau lọc máu"
        },
        "side_effects": [
            "Phát ban",
            "Tiêu chảy",
            "Buồn nôn",
            "Tăng transaminase (hiếm)",
            "Giảm bạch cầu (hiếm)",
            "Co giật (hiếm, suy thận nặng)",
            "Rối loạn thần kinh (hiếm, suy thận)"
        ],
        "interactions": [
            "Probenecid: tăng nồng độ cefpirome",
            "Warfarin: có thể tăng INR",
            "Aminoglycosides: không pha chung"
        ],
        "pregnancy": "B",
        "mechanism_of_action": "Cephalosporin thế hệ 4, ức chế tổng hợp thành tế bào vi khuẩn bằng cách gắn với penicillin-binding proteins (PBPs). Phổ kháng khuẩn: Gram-dương tốt hơn thế hệ 3 (Staphylococcus, Streptococcus), Gram-âm mạnh (Enterobacteriaceae, Pseudomonas aeruginosa, Acinetobacter). Kháng được nhiều beta-lactamase. Không hiệu quả với MRSA, Enterococcus, hoặc kỵ khí. Đặc điểm: phổ rộng, hiệu quả với cả Gram-dương và Gram-âm, kể cả Pseudomonas. Tương tự cefepime nhưng ít dùng hơn.",
        "monitoring": [
            "Dấu hiệu nhiễm trùng (sốt, WBC, triệu chứng lâm sàng)",
            "Cấy máu và cấy từ vị trí nhiễm trùng",
            "Chức năng thận (creatinine, eGFR) - cần điều chỉnh liều",
            "Dấu hiệu nhiễm C. difficile",
            "Chức năng gan (ALT, AST)",
            "Rối loạn thần kinh (co giật, nhầm lẫn) - hiếm, suy thận",
            "Công thức máu (CBC) - đặc biệt trong sốt giảm bạch cầu"
        ],
        "precautions": [
            "Điều chỉnh liều theo chức năng thận (eGFR) - quan trọng",
            "Nguy cơ co giật và rối loạn thần kinh ở suy thận nặng - cần điều chỉnh liều",
            "Không dùng ở bệnh nhân dị ứng penicillins hoặc cephalosporins",
            "Nguy cơ nhiễm C. difficile",
            "Liều cao hơn cho nhiễm khuẩn nặng và Pseudomonas (2g q8-12h)",
            "Pha trong NS hoặc D5W",
            "Không pha trộn với aminoglycosides"
        ],
        "pharmacokinetics": {
            "half_life": "2 giờ",
            "onset": "Ngay lập tức sau khi tiêm IV",
            "duration": "8-12 giờ (liều q8-12h)",
            "protein_binding": "10-15%",
            "metabolism": "Không chuyển hóa đáng kể",
            "clearance": "Chủ yếu qua thận (85% bài tiết nguyên dạng), cần điều chỉnh thận"
        },
        "storage": "Bảo quản bột khô ở nhiệt độ phòng (20-25°C). Sau khi pha: bảo quản ở nhiệt độ phòng 24 giờ, hoặc trong tủ lạnh 10 ngày.",
        "black_box_warnings": "Nguy cơ co giật và rối loạn thần kinh ở suy thận nặng - cần điều chỉnh liều theo chức năng thận.",
        "drug_interactions": {
            "major": [
                {
                    "drug": "Warfarin",
                    "mechanism": "Cefpirome có thể ức chế tổng hợp vitamin K phụ thuộc vào hệ vi khuẩn đường ruột, làm giảm sản xuất các yếu tố đông máu phụ thuộc vitamin K.",
                    "effect": "Tăng INR, tăng nguy cơ chảy máu",
                    "management": "Theo dõi INR thường xuyên (ít nhất 2-3 lần/tuần khi bắt đầu dùng cefpirome). Có thể cần giảm liều warfarin. Đặc biệt thận trọng ở bệnh nhân suy gan, dùng kéo dài (>7 ngày)."
                }
            ],
            "moderate": [
                {
                    "drug": "Probenecid",
                    "mechanism": "Probenecid ức chế bài tiết ống thận của cefpirome, làm giảm thải trừ và tăng nồng độ cefpirome.",
                    "effect": "Tăng nồng độ cefpirome, tăng thời gian bán thải",
                    "management": "Có thể cần giảm liều cefpirome. Theo dõi chức năng thận."
                },
                {
                    "drug": "Aminoglycosides (Gentamicin, Amikacin, Tobramycin)",
                    "mechanism": "Có thể tạo kết tủa khi pha chung. Cả hai đều có thể gây độc thận, tác dụng cộng dồn.",
                    "effect": "Kết tủa khi pha chung, tăng nguy cơ độc thận",
                    "management": "Không pha chung. Truyền riêng biệt. Theo dõi chức năng thận chặt chẽ."
                }
            ],
            "minor": []
        },
        "contraindications": {
            "tuyệt_đối": [
                "Dị ứng cephalosporin hoặc beta-lactam (phản ứng type I - sốc phản vệ, phù mạch, phát ban nặng)"
            ],
            "tương_đối": [
                "Dị ứng penicillin (phản ứng chéo ~5-10%) - thận trọng",
                "Suy thận nặng (CrCl <10) - cần điều chỉnh liều",
                "Tiền sử nhiễm C. difficile - tăng nguy cơ tái phát",
                "Rối loạn đông máu - tăng nguy cơ chảy máu khi dùng với warfarin"
            ]
        },
        "contraindications_detail": {
            "tuyệt_đối": [
                "Dị ứng cephalosporin hoặc beta-lactam (phản ứng type I - sốc phản vệ, phù mạch, phát ban nặng)"
            ],
            "tương_đối": [
                "Dị ứng penicillin (phản ứng chéo ~5-10%) - thận trọng",
                "Suy thận nặng (CrCl <10) - cần điều chỉnh liều",
                "Tiền sử nhiễm C. difficile - tăng nguy cơ tái phát",
                "Rối loạn đông máu - tăng nguy cơ chảy máu khi dùng với warfarin"
            ]
        },
        "pregnancy_lactation": {
            "fda_category": "B",
            "pregnancy_details": "Cefpirome phân loại B - an toàn trong thai kỳ. Cephalosporin là một trong những kháng sinh an toàn nhất trong thai kỳ.",
            "lactation": {
                "safety": "Compatible",
                "details": "Cefpirome bài tiết vào sữa mẹ ở nồng độ thấp. An toàn cho trẻ bú mẹ.",
                "recommendation": "Có thể dùng khi cho con bú."
            }
        },
        "hepatic_adjustment": {
            "mild": "Không cần điều chỉnh liều",
            "moderate": "Không cần điều chỉnh liều",
            "severe": "Không cần điều chỉnh liều, nhưng thận trọng",
            "notes": "Cefpirome không chuyển hóa qua gan, thải trừ chủ yếu qua thận. Suy gan ít ảnh hưởng."
        },
        "overdose_management": {
            "symptoms": [
                "Triệu chứng thần kinh: Co giật, rối loạn ý thức (hiếm, suy thận nặng)",
                "Triệu chứng tiêu hóa: Tiêu chảy nặng, buồn nôn, nôn",
                "Triệu chứng dị ứng: Phát ban, phù mạch, sốc phản vệ (nếu dị ứng)",
                "Triệu chứng thận: Suy thận cấp (hiếm với liều thông thường)"
            ],
            "antidote": "Không có antidote đặc hiệu. Điều trị hỗ trợ và điều trị triệu chứng.",
            "treatment": [
                "Ngừng ngay cefpirome",
                "Điều trị co giật nếu có: Benzodiazepine (diazepam, lorazepam)",
                "Điều trị dị ứng nếu có: Epinephrine nếu sốc phản vệ, antihistamine, corticosteroid",
                "Điều trị suy thận cấp nếu có: Bù dịch đầy đủ, điều chỉnh điện giải, lọc máu nếu cần",
                "Theo dõi dấu hiệu sinh tồn: Huyết áp, nhịp tim, nhịp thở, SpO2",
                "Lọc máu: Hemodialysis có thể loại bỏ cefpirome một phần (85% thải qua thận)"
            ],
            "monitoring": "Theo dõi dấu hiệu thần kinh (co giật), chức năng thận (creatinine, BUN, lượng nước tiểu), dấu hiệu sinh tồn trong ít nhất 24-48 giờ"
        },
        "reversal_agents": None,
        "administration_instructions": {
            "oral": {
                "with_food": "N/A - Chỉ có dạng IV và IM",
                "timing": "N/A - Chỉ có dạng IV và IM"
            },
            "iv": {
                "reconstitution": "Pha với NS (0.9% NaCl) hoặc D5W (5% Dextrose). Nồng độ pha: 10-40mg/ml. Pha 1g trong 10ml = 100mg/ml. Pha 2g trong 50ml = 40mg/ml. Lắc kỹ để hòa tan hoàn toàn.",
                "infusion_rate": "Truyền IV trong 30 phút. Tốc độ: 50ml/30 phút = ~1.7ml/phút.",
                "compatibility": ["NS (0.9% NaCl)", "D5W (5% Dextrose)"],
                "incompatibility": [
                    "Aminoglycosides - bất hoạt, không pha chung",
                    "Vancomycin - có thể tạo kết tủa",
                    "Các thuốc có tính kiềm hoặc acid mạnh"
                ],
                "notes": "QUAN TRỌNG: 1) Thời gian bán thải 2 giờ → dùng 2 lần/ngày (q12h), 2) Phổ rộng, hiệu quả với cả Gram-dương và Gram-âm, kể cả Pseudomonas, 3) Không pha chung với aminoglycosides, 4) Điều chỉnh liều theo chức năng thận."
            },
            "im": {
                "reconstitution": "Pha với lidocaine 1% (không có epinephrine) để giảm đau. Nồng độ pha: 200mg/ml (1g trong 5ml lidocaine 1%).",
                "injection_site": "Tiêm sâu vào cơ (gluteus maximus hoặc vastus lateralis).",
                "notes": "Pha với lidocaine 1% để giảm đau tại chỗ. Tiêm sâu vào cơ."
            }
        },
        "references": {
            "primary_sources": [
                "FDA Drug Label - Cefrom (cefpirome)",
                "IDSA Guidelines - Hospital-Acquired Pneumonia",
                "UpToDate - Cefpirome: Drug Information"
            ],
            "last_updated": "2025-02-05",
            "evidence_level": "A"
        }
    },
    "Ceftazidime": {
        "group": "Antibiotic - Cephalosporin (3rd Generation)",
        "vietnamese_name": "Ceftazidime, Fortaz, Tazicef",
        "administration": ["IV", "IM"],
        "indications": [
            "Nhiễm khuẩn do Pseudomonas aeruginosa",
            "Nhiễm khuẩn bệnh viện",
            "Nhiễm khuẩn huyết",
            "Viêm phổi bệnh viện",
            "Nhiễm khuẩn đường tiết niệu phức tạp",
            "Nhiễm khuẩn da và mô mềm"
        ],
        "contraindications": [
            "Dị ứng cephalosporin hoặc penicillin (thận trọng)",
            "Suy thận nặng (CrCl <10) - cần điều chỉnh liều"
        ],
        "dosage": {
            "adult_standard": "1-2g IV mỗi 8-12 giờ",
            "adult_severe": "2g IV mỗi 8 giờ",
            "adult_pseudomonas": "2g IV mỗi 8 giờ",
            "adult_cystic_fibrosis": "2g IV mỗi 8 giờ",
            "notes": "Liều cao hơn cho Pseudomonas và nhiễm khuẩn nặng"
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "1g IV mỗi 12 giờ",
            "under_30": "1g IV mỗi 24-48 giờ",
            "hemodialysis": "1g IV sau lọc máu"
        },
        "side_effects": [
            "Phát ban",
            "Tiêu chảy",
            "Buồn nôn",
            "Tăng transaminase",
            "Giảm bạch cầu (hiếm)",
            "Co giật (hiếm, suy thận nặng)"
        ],
        "interactions": [
            "Probenecid: tăng nồng độ ceftazidime",
            "Warfarin: có thể tăng INR",
            "Aminoglycosides: không pha chung"
        ],
        "pregnancy": "B - An toàn",
        "mechanism_of_action": "Cephalosporin thế hệ 3, ức chế tổng hợp thành tế bào vi khuẩn. Phổ kháng khuẩn: Gram-âm mạnh (Enterobacteriaceae, Pseudomonas aeruginosa - đặc biệt hiệu quả, Acinetobacter), Gram-dương hạn chế. Không hiệu quả với MRSA, Enterococcus, hoặc kỵ khí. Đặc điểm: hiệu quả với Pseudomonas aeruginosa (khác với các cephalosporin thế hệ 3 khác).",
        "monitoring": [
            "Dấu hiệu nhiễm trùng (sốt, WBC, triệu chứng lâm sàng)",
            "Cấy máu và cấy từ vị trí nhiễm trùng",
            "Chức năng thận (creatinine, eGFR) - cần điều chỉnh liều",
            "Dấu hiệu nhiễm C. difficile",
            "Chức năng gan (ALT, AST)",
            "Co giật (hiếm, suy thận nặng)"
        ],
        "precautions": [
            "Điều chỉnh liều theo chức năng thận - quan trọng",
            "Không dùng ở bệnh nhân dị ứng penicillins hoặc cephalosporins",
            "Nguy cơ nhiễm C. difficile",
            "Liều cao hơn cho Pseudomonas (2g q8h)",
            "Pha trong NS hoặc D5W",
            "Không pha trộn với aminoglycosides"
        ],
        "pharmacokinetics": {
            "half_life": "1.5-2 giờ",
            "onset": "Ngay lập tức sau khi tiêm IV",
            "duration": "6-8 giờ (liều q8h)",
            "protein_binding": "10-17%",
            "metabolism": "Không chuyển hóa đáng kể",
            "clearance": "Chủ yếu qua thận (80-90% bài tiết nguyên dạng), cần điều chỉnh thận"
        },
        "storage": "Bảo quản bột khô ở nhiệt độ phòng (20-25°C). Sau khi pha: bảo quản ở nhiệt độ phòng 24 giờ.",
        "black_box_warnings": "Không có black box warning. Tuy nhiên, cần điều chỉnh liều theo chức năng thận.",
        "references": {
            "primary_sources": [
                "FDA Drug Label - Ceftazidime",
                "IDSA Guidelines - Hospital-Acquired Pneumonia",
                "UpToDate - Ceftazidime: Drug Information"
            ],
            "last_updated": "2025-02-05",
            "evidence_level": "A"
        },
        "risk_flags": {
            "high_alert": False,
            "narrow_therapeutic_index": False,
            "icu_critical_care_only": False,
            "bleeding_risk": None,
            "organ_toxicity": {"neurological": "Seizures (rare, in renal impairment)", "hepatic": "Hepatotoxicity (rare)", "hematologic": "Neutropenia (rare)", "gastrointestinal": "C. difficile infection"},
            "qt_prolongation": False,
            "hepatotoxicity": "Rare",
            "nephrotoxicity": False,
            "requires_monitoring": ["Renal function (CrCl - dose adjustment required)", "Neurological signs (seizures in renal impairment)", "C. difficile infection signs", "Hepatic function (ALT, AST)", "CBC (neutropenia risk)"],
            "look_alike_sound_alike": ["Ceftazidime", "Cefepime", "Cefotaxime"]
        },
        "guideline_tags": [
            "IDSA Guidelines - Hospital-Acquired Pneumonia",
            "IDSA Guidelines - Pseudomonas Infections",
            "WHO Essential Medicines List"
        ],
        "last_updated": "2025-02-18",
        "drug_interactions": {
                  "major": [
                      {
                          "drug": "Warfarin: có thể tăng INR",
                          "mechanism": "Tăng nguy cơ chảy máu"
                      }
                  ],
                  "moderate": [],
                  "minor": [
                      {
                          "drug": "Probenecid: tăng nồng độ ceftazidime",
                          "mechanism": "Tương tác lâm sàng"
                      },
                      {
                          "drug": "Aminoglycosides: không pha chung",
                          "mechanism": "Tương tác lâm sàng"
                      }
                  ]
              },
              "pregnancy_lactation": {
                  "fda_category": "B - An toàn",
                  "pregnancy_details": "Category B - An toàn - Cần tra cứu thêm thông tin chi tiết về sử dụng trong thai kỳ.",
                  "lactation": {
                      "safety": "Use with caution",
                      "details": "Cần tra cứu thêm thông tin chi tiết về bài tiết vào sữa mẹ.",
                      "recommendation": "Thận trọng khi cho con bú, tra cứu thêm thông tin."
                  }
              },
              "hepatic_adjustment": {
                  "mild": "Không đổi",
                  "moderate": "Thận trọng, có thể giảm liều",
                  "severe": "Thận trọng, giảm liều hoặc tránh dùng",
                  "notes": "Nhiều kháng sinh chuyển hóa qua gan, cần điều chỉnh liều ở suy gan nặng."
              },
              "overdose_management": {
                  "symptoms": [
                      "Cần tra cứu thêm thông tin về triệu chứng quá liều"
                  ],
                  "antidote": "Không có antidote đặc hiệu",
                  "treatment": [
                      "Ngừng ngay thuốc",
                      "Rửa dạ dày nếu uống trong vòng 1-2 giờ (nếu phù hợp)",
                      "Than hoạt tính",
                      "Điều trị hỗ trợ và điều trị triệu chứng",
                      "Theo dõi dấu hiệu sinh tồn"
                  ],
                  "monitoring": "Theo dõi dấu hiệu sinh tồn, triệu chứng lâm sàng"
              },
              "reversal_agents": {
                  "available": False,
                  "agents": []
              },
              "administration_instructions": {
                  "iv": {
                      "reconstitution": "Cần tra cứu",
                      "infusion_rate": "Cần tra cứu",
                      "compatibility": [
                          "Cần tra cứu"
                      ],
                      "incompatibility": [],
                      "notes": "Cần tra cứu thêm thông tin chi tiết."
                  }
              },
},
    
    "Ceftriaxone": {'group': 'Antibiotic - Cephalosporin (3rd Generation)',
        'vietnamese_name':
        'Ceftriaxone, Rocephin', 'administration': ['IV', 'IM'],
        'indications':
        ['Nhiễm khuẩn nặng', 'Viêm màng não', 'Nhiễm khuẩn bệnh viện',
        'Nhiễm khuẩn đường tiết niệu', 'Viêm phổi'],
        'contraindications': [
        'Dị ứng cephalosporin hoặc penicillin (thận trọng)',
        'Trẻ sơ sinh <28 ngày với Ca IV'],
        'dosage': {'adult_standard':
        '1-2g IV/IM mỗi 24 giờ', 'adult_severe': '2-4g IV mỗi 24 giờ',
        'adult_meningitis': '2g IV mỗi 12 giờ', 'pediatric_standard':
        '50-75mg/kg IV/IM mỗi 24 giờ (tối đa 2g)', 'pediatric_meningitis':
        '80-100mg/kg IV mỗi 12-24 giờ (tối đa 4g/ngày)', 'notes':
        'Thời gian bán hủy dài, dùng 1 lần/ngày. Có thể gây kết tủa với Ca ở trẻ sơ sinh'
        },
        'renal_adjustment': {'normal': 'Không đổi', '30_60':
        'Không đổi (thải qua mật)', 'under_30':
        'Giảm liều nếu CrCl <10 và suy gan'},
        'side_effects': ['Tiêu chảy',
        'Phát ban', 'Tăng transaminase', 'Viêm túi mật (hiếm)',
        'Giảm bạch cầu (hiếm)', 'Sỏi mật (với liều cao dài ngày)'],
        'interactions': ['Warfarin: tăng INR',
        'Calcium IV: kết tủa (trẻ sơ sinh)',
        'Probenecid: tăng nồng độ ceftriaxone'],
        'mechanism_of_action':
        'Cephalosporin thế hệ 3, phổ rộng. Ức chế tổng hợp thành tế bào vi khuẩn bằng cách gắn với penicillin-binding proteins (PBPs). Phổ kháng khuẩn: Gram-dương (một số), Gram-âm mạnh (Enterobacteriaceae, Neisseria, H. influenzae), và một số kỵ khí. Kháng được nhiều beta-lactamase do có cấu trúc vòng beta-lactam bền vững. Không hiệu quả với Pseudomonas aeruginosa, Enterococcus, hoặc MRSA. Thời gian bán thải dài (6-9 giờ) → chỉ cần tiêm 1 lần/ngày.'
        , 'monitoring': ['Dấu hiệu nhiễm trùng (sốt, WBC, CRP)',
        'Cấy máu và cấy từ vị trí nhiễm trùng',
        'Chức năng gan (ALT, AST, bilirubin) - có thể tăng, hiếm sỏi mật',
        'Sỏi mật (ceftriaxone-calcium complex) - đặc biệt ở trẻ em, dùng liều cao',
        'Chức năng thận (creatinine) - không cần điều chỉnh thận nhưng theo dõi',
        'Dấu hiệu nhiễm C. difficile',
        'Co giật (hiếm, nhưng có thể ở suy thận nặng)',
        'Phản ứng tại chỗ tiêm (đau, viêm tĩnh mạch)'],
        'precautions': [
        'KHÔNG dùng ở trẻ sơ sinh < 28 ngày tuổi nếu đang dùng calci IV (nguy cơ kết tủa ceftriaxone-calcium trong phổi, thận) - có thể tử vong'
        'Nguy cơ sỏi mật (ceftriaxone-calcium complex) - đặc biệt ở trẻ em, dùng liều cao, dùng kéo dài'
        'Không dùng ở bệnh nhân dị ứng penicillins hoặc cephalosporins (phản ứng chéo ~5-10%)'
        , 'Nguy cơ nhiễm C. difficile - theo dõi tiêu chảy',
        'Có thể gây tăng bilirubin (nhất thời, do đẩy bilirubin khỏi albumin)',
        'Pha trong NS, D5W, hoặc LR, tiêm IV hoặc IM',
        'Tiêm IM: pha với lidocaine 1% để giảm đau',
        'Không pha trộn với các thuốc khác (tương kỵ với nhiều thuốc, đặc biệt vancomycin, calcium)'
        'Thời gian bán thải dài → chỉ cần 1 lần/ngày (trừ viêm màng não: q12h)'
        ],
        'pharmacokinetics': {'half_life':
        '6-9 giờ (rất dài cho cephalosporin)', 'onset':
        'Ngay lập tức sau khi tiêm IV', 'duration':
        '24 giờ (liều 1-2g q24h), 12 giờ (viêm màng não: 2g q12h)',
        'protein_binding': '85-95% (rất cao)', 'metabolism':
        'Không chuyển hóa, bài tiết nguyên dạng', 'clearance':
        '40% qua thận, 60% qua mật (độc nhất trong cephalosporin) → không cần điều chỉnh thận'
        },storage':
        'Bảo quản bột khô ở nhiệt độ phòng (20-25°C). Sau khi pha: bảo quản ở nhiệt độ phòng 24 giờ, hoặc trong tủ lạnh 10 ngày. Không đông lạnh.'
        , 'black_box_warnings':
        'KHÔNG dùng ở trẻ sơ sinh < 28 ngày tuổi nếu đang dùng calci IV - có thể gây kết tủa ceftriaxone-calcium trong phổi, thận, có thể tử vong. Tránh dùng calci IV trong 48 giờ sau liều ceftriaxone cuối cùng ở trẻ sơ sinh.'
        , 'drug_interactions': {'major': [{'drug':
        'Calcium IV (đặc biệt ở trẻ sơ sinh < 28 ngày)', 'mechanism':
        'Ceftriaxone tạo phức hợp không hòa tan với calci, gây kết tủa ceftriaxone-calcium trong phổi, thận, có thể tử vong.'
        , 'effect':
        'Kết tủa ceftriaxone-calcium trong phổi, thận, có thể tử vong (đặc biệt ở trẻ sơ sinh)'
        , 'management':
        'CHỐNG CHỈ ĐỊNH TUYỆT ĐỐI: Không dùng ceftriaxone ở trẻ sơ sinh < 28 ngày nếu đang dùng calci IV. Tránh dùng calci IV trong 48 giờ sau liều ceftriaxone cuối cùng ở trẻ sơ sinh. Ở người lớn, tránh pha chung trong cùng một ống truyền, truyền riêng biệt.'
        }, {'drug': 'Warfarin', 'mechanism':
        'Ceftriaxone có thể ức chế tổng hợp vitamin K phụ thuộc vào hệ vi khuẩn đường ruột, làm giảm sản xuất các yếu tố đông máu phụ thuộc vitamin K. Ngoài ra, có thể đẩy warfarin khỏi albumin (protein binding cao).'
        , 'effect': 'Tăng INR, tăng nguy cơ chảy máu', 'management':
        'Theo dõi INR thường xuyên (ít nhất 2-3 lần/tuần khi bắt đầu dùng ceftriaxone). Có thể cần giảm liều warfarin. Đặc biệt thận trọng ở bệnh nhân suy gan, dùng kéo dài (>7 ngày).'
        }],
        'moderate': [{'drug': 'Probenecid', 'mechanism':
        'Probenecid ức chế bài tiết ống thận của ceftriaxone, làm giảm thải trừ và tăng nồng độ ceftriaxone.'
        , 'effect': 'Tăng nồng độ ceftriaxone, tăng thời gian bán thải',
        'management':
        'Có thể cần giảm liều ceftriaxone. Theo dõi chức năng thận. Thường không cần điều chỉnh liều thường quy do ceftriaxone thải trừ chủ yếu qua mật.'
        }, {'drug': 'Vancomycin', 'mechanism':
        'Có thể tạo kết tủa khi pha chung. Cả hai đều có thể gây độc thận, tác dụng cộng dồn.'
        , 'effect': 'Kết tủa khi pha chung, tăng nguy cơ độc thận',
        'management':
        'Không pha chung. Truyền riêng biệt. Theo dõi chức năng thận chặt chẽ. Theo dõi nồng độ vancomycin nếu có thể.'
        }, {'drug': 'Aminoglycosides (Gentamicin, Tobramycin, Amikacin)',
        'mechanism':
        'Có thể tạo kết tủa khi pha chung. Cả hai đều có thể gây độc thận, tác dụng cộng dồn.'
        , 'effect': 'Kết tủa khi pha chung, tăng nguy cơ độc thận',
        'management':
        'Không pha chung. Truyền riêng biệt. Theo dõi chức năng thận chặt chẽ.'
        }],
        'minor': [{'drug': 'Thuốc tránh thai đường uống', 'mechanism':
        'Kháng sinh phổ rộng có thể làm giảm hệ vi khuẩn đường ruột, làm giảm tái hấp thu estrogen từ đường ruột.'
        , 'effect':
        'Giảm hiệu quả thuốc tránh thai (hiếm, nhưng có thể xảy ra)',
        'management':
        'Khuyến cáo sử dụng biện pháp tránh thai bổ sung (bao cao su) trong khi dùng kháng sinh và 7 ngày sau khi ngừng.'
        }]},
        'contraindications': {'tuyệt_đối': [
        'Dị ứng cephalosporin hoặc beta-lactam (phản ứng type I - sốc phản vệ, phù mạch, phát ban nặng)'
        'Trẻ sơ sinh < 28 ngày tuổi đang dùng calci IV - CHỐNG CHỈ ĐỊNH TUYỆT ĐỐI (nguy cơ kết tủa tử vong)'
        ],
        'tương_đối': [
        'Dị ứng penicillin (phản ứng chéo ~5-10%) - thận trọng, có thể dùng nếu phản ứng nhẹ'
        , 'Suy gan nặng kèm suy thận (CrCl <10) - cần giảm liều',
        'Tiền sử nhiễm C. difficile - tăng nguy cơ tái phát',
        'Rối loạn đông máu - tăng nguy cơ chảy máu khi dùng với warfarin',
        'Sỏi mật - tăng nguy cơ sỏi mật (ceftriaxone-calcium complex), đặc biệt ở trẻ em, dùng liều cao'
        ]},contraindications_detail': {'tuyệt_đối': [
        'Dị ứng cephalosporin hoặc beta-lactam (phản ứng type I - sốc phản vệ, phù mạch, phát ban nặng)'
        'Trẻ sơ sinh < 28 ngày tuổi đang dùng calci IV - CHỐNG CHỈ ĐỊNH TUYỆT ĐỐI (nguy cơ kết tủa tử vong)'
        ],
        'tương_đối': [
        'Dị ứng penicillin (phản ứng chéo ~5-10%) - thận trọng, có thể dùng nếu phản ứng nhẹ'
        , 'Suy gan nặng kèm suy thận (CrCl <10) - cần giảm liều',
        'Tiền sử nhiễm C. difficile - tăng nguy cơ tái phát',
        'Rối loạn đông máu - tăng nguy cơ chảy máu khi dùng với warfarin',
        'Sỏi mật - tăng nguy cơ sỏi mật (ceftriaxone-calcium complex), đặc biệt ở trẻ em, dùng liều cao'
        ]},pregnancy_lactation': {'fda_category': 'B', 'pregnancy_details':
        'Ceftriaxone là thuốc phân loại B. Các nghiên cứu trên động vật không cho thấy nguy cơ dị tật bẩm sinh, nhưng không có nghiên cứu đầy đủ trên phụ nữ có thai. Cephalosporins nói chung được coi là an toàn trong thai kỳ và được sử dụng rộng rãi. Ceftriaxone có thể được dùng khi lợi ích vượt quá nguy cơ, đặc biệt trong nhiễm khuẩn nặng như viêm màng não. Tuy nhiên, cần thận trọng với nguy cơ sỏi mật và tương tác với calci. Nên tránh dùng kéo dài nếu có thể.'
        , 'lactation': {'safety': 'Compatible', 'details':
        'Ceftriaxone bài tiết vào sữa mẹ ở nồng độ thấp. Nồng độ trong sữa mẹ thấp và không có báo cáo về tác dụng phụ đáng kể ở trẻ bú mẹ. Cephalosporins nói chung được coi là an toàn khi cho con bú.'
        , 'recommendation':
        'Có thể dùng khi cho con bú. Theo dõi trẻ sơ sinh về dấu hiệu tiêu chảy, phát ban, hoặc các tác dụng phụ khác. Dùng liều thấp nhất hiệu quả.'
        }},hepatic_adjustment': {'mild':
        'Không cần điều chỉnh liều. Ceftriaxone thải trừ 40% qua thận, 60% qua mật, không chuyển hóa qua gan.'
        , 'moderate':
        'Không cần điều chỉnh liều. Tuy nhiên, cần thận trọng với nguy cơ tăng bilirubin (nhất thời, do đẩy bilirubin khỏi albumin).'
        , 'severe':
        'Không cần điều chỉnh liều. Tuy nhiên, nếu kèm theo suy thận nặng (CrCl <10), có thể cần giảm liều. Theo dõi bilirubin và chức năng gan.'
        , 'notes':
        'Ceftriaxone không chuyển hóa qua gan, thải trừ 40% qua thận và 60% qua mật (độc nhất trong cephalosporin). Không cần điều chỉnh liều ở bệnh nhân suy gan. Tuy nhiên, suy gan nặng có thể kèm theo suy thận, nên cần điều chỉnh liều theo chức năng thận nếu CrCl <10. Ngoài ra, ceftriaxone có protein binding cao (85-95%), có thể đẩy bilirubin khỏi albumin, gây tăng bilirubin nhất thời.'
        },overdose_management': {'symptoms': [
        'Triệu chứng thần kinh: Co giật, rối loạn ý thức (hiếm, thường chỉ với liều rất cao hoặc suy thận nặng)'
        , 'Triệu chứng gan: Tăng bilirubin, tăng transaminase (nhất thời)',
        'Triệu chứng sỏi mật: Đau bụng, buồn nôn, nôn (do kết tủa ceftriaxone-calcium)'
        , 'Triệu chứng thận: Suy thận cấp (hiếm với liều thông thường)',
        'Triệu chứng tiêu hóa: Tiêu chảy nặng, buồn nôn, nôn',
        'Triệu chứng dị ứng: Phát ban, phù mạch, sốc phản vệ (nếu dị ứng)',
        'Triệu chứng chảy máu: Chảy máu kéo dài, tăng INR (khi dùng với warfarin)'
        ],antidote':
        'Không có antidote đặc hiệu. Điều trị hỗ trợ và điều trị triệu chứng.',
        'treatment': ['Ngừng ngay ceftriaxone',
        'Điều trị co giật nếu có: Benzodiazepine (diazepam, lorazepam), phenobarbital'
        , 'Điều trị sỏi mật nếu có:', '  - Giảm đau: NSAID hoặc opioid',
        '  - Bù dịch đầy đủ', '  - Theo dõi siêu âm bụng',
        '  - Có thể cần can thiệp nếu tắc nghẽn', 'Điều trị chảy máu nếu có:',
        '  - Bổ sung vitamin K nếu giảm prothrombin',
        '  - Truyền huyết tương tươi đông lạnh (FFP) nếu chảy máu nặng',
        '  - Điều chỉnh liều warfarin nếu đang dùng',
        'Điều trị suy thận cấp nếu có:', '  - Bù dịch đầy đủ',
        '  - Điều chỉnh điện giải',
        '  - Lọc máu nếu cần (hemodialysis có thể loại bỏ ceftriaxone một phần)',
        'Điều trị dị ứng nếu có:', '  - Epinephrine nếu sốc phản vệ',
        '  - Antihistamine, corticosteroid', '  - Hỗ trợ hô hấp nếu cần',
        'Theo dõi dấu hiệu sinh tồn: Huyết áp, nhịp tim, nhịp thở, SpO2',
        'Lọc máu: Hemodialysis có thể loại bỏ ceftriaxone một phần (40% thải qua thận), nhưng không hiệu quả bằng các cephalosporin khác do thải trừ chủ yếu qua mật.'
        ],
        'monitoring':
        'Theo dõi dấu hiệu thần kinh (co giật, ý thức), chức năng gan (bilirubin, ALT, AST), dấu hiệu sỏi mật (đau bụng), chức năng thận (creatinine, BUN, lượng nước tiểu), PT/INR (nếu dùng với warfarin), dấu hiệu chảy máu, dấu hiệu sinh tồn trong ít nhất 24-48 giờ. Theo dõi lâu hơn nếu có suy thận cấp hoặc sỏi mật.'
        },reversal_agents': {'available': False, 'agents': [],notes':
        'Không có antidote đặc hiệu. Điều trị quá liều chủ yếu là điều trị hỗ trợ: ngừng ngay ceftriaxone, điều trị co giật nếu có, điều trị sỏi mật nếu có, điều trị chảy máu nếu có (bổ sung vitamin K, FFP), điều trị suy thận cấp nếu có, điều trị dị ứng nếu có (epinephrine nếu sốc phản vệ), lọc máu có thể loại bỏ một phần nhưng không hiệu quả bằng các cephalosporin khác do thải trừ chủ yếu qua mật.'},administration_instructions': {'oral': {
        'with_food': 'Không áp dụng - chỉ có dạng IV và IM', 'timing':
        'Không áp dụng - chỉ có dạng IV và IM'},iv': {'reconstitution':
        "Pha với NS (0.9% NaCl), D5W (5% Dextrose), hoặc Ringer's Lactate. Nồng độ pha: 10-40mg/ml. Pha 1g trong 10ml = 100mg/ml (quá đậm, không dùng). Pha 1g trong 50ml = 20mg/ml. Pha 2g trong 50ml = 40mg/ml. Lắc kỹ để hòa tan hoàn toàn. KHÔNG pha với calci IV."
        , 'infusion_rate':
        'Truyền IV trong 30 phút. Tốc độ: 50ml/30 phút = ~1.7ml/phút. Có thể truyền nhanh hơn (bolus) nếu cần, nhưng thường truyền trong 30 phút để giảm đau tại chỗ.'
        , 'compatibility': ['NS (0.9% NaCl)', 'D5W (5% Dextrose)',
        "Ringer's Lactate"],incompatibility': [
        'Calcium IV - KHÔNG pha chung, nguy cơ kết tủa tử vong (đặc biệt ở trẻ sơ sinh)'
        , 'Vancomycin - tạo kết tủa, không pha chung',
        'Aminoglycosides - có thể tạo kết tủa, truyền riêng biệt',
        'Amphotericin B - không tương thích',
        'Các thuốc có tính kiềm hoặc acid mạnh'],notes':
        'QUAN TRỌNG: 1) KHÔNG pha chung với calci IV (nguy cơ kết tủa tử vong ở trẻ sơ sinh), 2) Không pha chung với vancomycin hoặc aminoglycosides, 3) Thời gian bán thải dài (6-9 giờ) → chỉ cần 1 lần/ngày (trừ viêm màng não: q12h), 4) Tiêm IM: pha với lidocaine 1% để giảm đau, 5) Theo dõi sỏi mật ở trẻ em, dùng liều cao, dùng kéo dài.'
        },im': {'reconstitution':
        'Pha với lidocaine 1% (không có epinephrine) để giảm đau. Nồng độ pha: 250mg/ml (1g trong 3.5ml lidocaine 1%). Pha 1g trong 3.5ml lidocaine 1% = 250mg/ml. Lắc kỹ để hòa tan hoàn toàn.'
        , 'injection_site':
        'Tiêm sâu vào cơ (gluteus maximus hoặc vastus lateralis). Tránh tiêm vào mạch máu.'
        , 'notes':
        'Pha với lidocaine 1% để giảm đau tại chỗ. Tiêm sâu vào cơ. Có thể gây đau tại chỗ, nhưng thường nhẹ khi pha với lidocaine.'
        }},pediatric_dosing': {'neonates':
        '<28 ngày: 50mg/kg IV/IM mỗi 24 giờ. CHỐNG CHỈ ĐỊNH pha chung với calci IV (nguy cơ kết tủa tử vong).',
        'infants':
        '1-3 tháng: 50-75mg/kg IV/IM mỗi 24 giờ. Viêm màng não: 80-100mg/kg IV mỗi 12-24 giờ (tối đa 4g/ngày). CHỐNG CHỈ ĐỊNH pha chung với calci IV.',
        'children':
        '3 tháng - 12 tuổi: 50-75mg/kg IV/IM mỗi 24 giờ (tối đa 2g). Viêm màng não: 80-100mg/kg IV mỗi 12-24 giờ (tối đa 4g/ngày). Theo dõi sỏi mật với liều cao, dùng kéo dài.',
        'adolescents':
        '≥12 tuổi: Liều người lớn. 1-2g IV/IM mỗi 24 giờ. Viêm màng não: 2g IV mỗi 12 giờ. Nhiễm trùng nặng: 2-4g IV mỗi 24 giờ.',
        'notes':
        'CHỐNG CHỈ ĐỊNH pha chung với calci IV ở trẻ sơ sinh <28 ngày (nguy cơ kết tủa tử vong). Thời gian bán thải dài → chỉ cần 1 lần/ngày (trừ viêm màng não: q12h). Theo dõi sỏi mật ở trẻ em, dùng liều cao, dùng kéo dài.'},geriatric_dosing': {'considerations':
        'Người cao tuổi có thể có suy thận, suy gan phổ biến hơn. Tuy nhiên, ceftriaxone thải qua mật nên không cần điều chỉnh liều ở suy thận (trừ khi CrCl <10 và suy gan kèm theo).',
        'dose_adjustment':
        'Không cần điều chỉnh liều ở suy thận (thải qua mật). Chỉ giảm liều nếu CrCl <10 và suy gan kèm theo. Thận trọng ở suy gan nặng.',
        'monitoring':
        'Theo dõi chức năng gan (ALT, AST) nếu có bệnh gan. Theo dõi chức năng thận (creatinine, CrCl) nếu có suy thận nặng kèm suy gan. Theo dõi dấu hiệu nhiễm trùng (sốt, WBC). Theo dõi sỏi mật nếu dùng liều cao, dùng kéo dài.'},brand_names': {'vietnam': [
        'Ceftriaxone', 'Rocephin', 'Ceftriaxone Stada', 'Ceftriax'],common': [
        'Rocephin', 'Ceftriaxone'],range': '50,000 - 200,000 VND/lọ (tùy hàm lượng và thương hiệu)',
        'note':
        'Giá thay đổi theo thương hiệu và nhà thuốc. Ceftriaxone generic thường rẻ hơn (50,000-100,000 VND/lọ 1g). Rocephin (brand) thường đắt hơn (100,000-200,000 VND/lọ 1g).'},references': {'primary_sources': [
        'FDA Drug Label - Ceftriaxone (Rocephin)',
        'UpToDate - Ceftriaxone: Drug Information',
        'Medscape - Ceftriaxone Drug Reference',
        "Goodman & Gilman's The Pharmacological Basis of Therapeutics (14th ed)",
        'Lexicomp Online - Ceftriaxone Monograph',
        'Micromedex - Ceftriaxone Drug Information',
        'IDSA Guidelines - Community-Acquired Pneumonia, Meningitis'],last_updated': '2025-02-03', 'evidence_level':
        'A - Dựa trên FDA drug labels, IDSA guidelines, và dữ liệu lâm sàng từ nhiều nguồn'
        }},
    
    "Cefuroxime": {
        "group": "Antibiotic - Cephalosporin (2nd Generation)",
        "vietnamese_name": "Cefuroxime, Zinacef, Ceftin",
        "administration": ["IV", "IM", "PO"],
        "indications": [
            "Viêm phổi cộng đồng",
            "Nhiễm khuẩn đường tiết niệu",
            "Nhiễm khuẩn da và mô mềm",
            "Viêm xoang",
            "Viêm tai giữa",
            "Dự phòng phẫu thuật"
        ],
        "contraindications": [
            "Dị ứng cephalosporin hoặc penicillin (thận trọng)",
            "Suy thận nặng (CrCl <10) - cần điều chỉnh liều"
        ],
        "dosage": {
            "adult_iv_standard": "750mg-1.5g IV mỗi 8 giờ",
            "adult_iv_severe": "1.5g IV mỗi 6-8 giờ",
            "adult_po": "250-500mg PO x 2 lần/ngày",
            "adult_prophylaxis": "1.5g IV 30-60 phút trước phẫu thuật",
            "notes": "Uống với thức ăn để tăng hấp thu"
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "750mg-1.5g IV mỗi 12 giờ",
            "under_30": "750mg IV mỗi 12-24 giờ",
            "hemodialysis": "750mg IV sau lọc máu"
        },
        "side_effects": [
            "Tiêu chảy",
            "Phát ban",
            "Buồn nôn",
            "Tăng transaminase",
            "Giảm bạch cầu (hiếm)"
        ],
        "interactions": [
            "Probenecid: tăng nồng độ cefuroxime",
            "Warfarin: có thể tăng INR",
            "Antacid: giảm hấp thu (PO)"
        ],
        "pregnancy": "B - An toàn",
        "mechanism_of_action": "Cephalosporin thế hệ 2, ức chế tổng hợp thành tế bào vi khuẩn. Phổ kháng khuẩn: Gram-dương (Staphylococcus, Streptococcus), Gram-âm tốt hơn thế hệ 1 (E. coli, Klebsiella, H. influenzae, Neisseria), và một số kỵ khí (Bacteroides fragilis). Không hiệu quả với MRSA, Enterococcus, Pseudomonas.",
        "monitoring": [
            "Dấu hiệu nhiễm trùng (sốt, WBC, triệu chứng lâm sàng)",
            "Cấy máu và cấy từ vị trí nhiễm trùng",
            "Chức năng thận (creatinine, eGFR)",
            "Dấu hiệu nhiễm C. difficile",
            "Chức năng gan (ALT, AST)"
        ],
        "precautions": [
            "Điều chỉnh liều theo chức năng thận",
            "Không dùng ở bệnh nhân dị ứng penicillins hoặc cephalosporins",
            "Nguy cơ nhiễm C. difficile",
            "Uống với thức ăn để tăng hấp thu (PO)",
            "Tránh antacid trong 2 giờ (PO)"
        ],
        "pharmacokinetics": {
            "half_life": "1-2 giờ",
            "onset": "Ngay lập tức sau khi tiêm IV",
            "duration": "6-8 giờ (liều q8h)",
            "protein_binding": "33-50%",
            "metabolism": "Không chuyển hóa đáng kể",
            "clearance": "Chủ yếu qua thận (90-100% bài tiết nguyên dạng), cần điều chỉnh thận"
        },
        "storage": "Bảo quản bột khô ở nhiệt độ phòng (20-25°C). Sau khi pha: bảo quản ở nhiệt độ phòng 24 giờ.",
        "black_box_warnings": "Không có black box warning.",
        "references": {
            "primary_sources": [
                "FDA Drug Label - Cefuroxime",
                "IDSA Guidelines - Community-Acquired Pneumonia",
                "UpToDate - Cefuroxime: Drug Information"
            ],
            "last_updated": "2025-02-05",
            "evidence_level": "A"
        },
        "risk_flags": {
            "high_alert": False,
            "narrow_therapeutic_index": False,
            "icu_critical_care_only": False,
            "bleeding_risk": None,
            "organ_toxicity": {"hepatic": "Hepatotoxicity (rare)", "hematologic": "Neutropenia (rare)", "gastrointestinal": "C. difficile infection"},
            "qt_prolongation": False,
            "hepatotoxicity": "Rare",
            "nephrotoxicity": False,
            "requires_monitoring": ["Renal function (CrCl - dose adjustment required)", "C. difficile infection signs", "Hepatic function (ALT, AST)", "CBC (neutropenia risk)"],
            "look_alike_sound_alike": ["Cefuroxime", "Cefuroxime axetil"]
        },
        "guideline_tags": [
            "IDSA Guidelines - Community-Acquired Pneumonia",
            "IDSA Guidelines - Surgical Prophylaxis",
            "WHO Essential Medicines List"
        ],
        "last_updated": "2025-02-18",
        "drug_interactions": {
                  "major": [
                      {
                          "drug": "Warfarin: có thể tăng INR",
                          "mechanism": "Tăng nguy cơ chảy máu"
                      }
                  ],
                  "moderate": [],
                  "minor": [
                      {
                          "drug": "Probenecid: tăng nồng độ cefuroxime",
                          "mechanism": "Tương tác lâm sàng"
                      },
                      {
                          "drug": "Antacid: giảm hấp thu (PO)",
                          "mechanism": "Tương tác lâm sàng"
                      }
                  ]
              },
              "pregnancy_lactation": {
                  "fda_category": "B - An toàn",
                  "pregnancy_details": "Category B - An toàn - Cần tra cứu thêm thông tin chi tiết về sử dụng trong thai kỳ.",
                  "lactation": {
                      "safety": "Use with caution",
                      "details": "Cần tra cứu thêm thông tin chi tiết về bài tiết vào sữa mẹ.",
                      "recommendation": "Thận trọng khi cho con bú, tra cứu thêm thông tin."
                  }
              },
              "hepatic_adjustment": {
                  "mild": "Không đổi",
                  "moderate": "Thận trọng, có thể giảm liều",
                  "severe": "Thận trọng, giảm liều hoặc tránh dùng",
                  "notes": "Nhiều kháng sinh chuyển hóa qua gan, cần điều chỉnh liều ở suy gan nặng."
              },
              "overdose_management": {
                  "symptoms": [
                      "Cần tra cứu thêm thông tin về triệu chứng quá liều"
                  ],
                  "antidote": "Không có antidote đặc hiệu",
                  "treatment": [
                      "Ngừng ngay thuốc",
                      "Rửa dạ dày nếu uống trong vòng 1-2 giờ (nếu phù hợp)",
                      "Than hoạt tính",
                      "Điều trị hỗ trợ và điều trị triệu chứng",
                      "Theo dõi dấu hiệu sinh tồn"
                  ],
                  "monitoring": "Theo dõi dấu hiệu sinh tồn, triệu chứng lâm sàng"
              },
              "reversal_agents": {
                  "available": False,
                  "agents": []
              },
              "administration_instructions": {
                  "oral": {
                      "with_food": "Có thể uống với hoặc không có thức ăn (trừ khi có chỉ định khác)",
                      "timing": "Theo chỉ định của bác sĩ",
                      "notes": "Cần tra cứu thêm thông tin chi tiết về cách dùng."
                  },
                  "iv": {
                      "reconstitution": "Cần tra cứu",
                      "infusion_rate": "Cần tra cứu",
                      "compatibility": [
                          "Cần tra cứu"
                      ],
                      "incompatibility": [],
                      "notes": "Cần tra cứu thêm thông tin chi tiết."
                  }
              },
},
    
}

__all__ = ['CEPHALOSPORINS_DRUGS']
