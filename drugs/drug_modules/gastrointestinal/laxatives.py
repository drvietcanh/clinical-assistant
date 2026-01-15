"""Gastrointestinal Drugs - Laxatives
Lactulose, Polyethylene glycol (PEG 3350)"""

LAXATIVES_DRUGS = {
    "Bisacodyl": {
        "group": "Gastrointestinal - Stimulant Laxative (Diphenylmethane)",
        "vietnamese_name": "Bisacodyl, Dulcolax",
        "administration": ["PO", "PR"],
        "indications": [
            "Táo bón cấp, táo bón do ít vận động",
            "Chuẩn bị ruột trước phẫu thuật, nội soi (kết hợp các thuốc khác)",
        ],
        "contraindications": [
            "Tắc ruột, thủng ruột, viêm phúc mạc",
            "Đau bụng cấp chưa rõ nguyên nhân (nghi ngờ bụng ngoại khoa)",
            "Viêm ruột cấp (viêm đại tràng nặng, bệnh Crohn đợt cấp nặng)",
        ],
        "dosage": {
            "adult_po": "5–10mg PO vào buổi tối; có thể tăng tối đa 15–20mg theo chỉ định",
            "adult_pr": "10mg đặt trực tràng (suppository) buổi sáng; tác dụng nhanh 15–60 phút",
            "notes": "Uống nguyên viên, không nghiền/nhai; không uống cùng sữa, antacid hoặc PPI ngay trước/sau.",
        },
        "renal_adjustment": {
            "normal": "Không cần chỉnh liều",
            "30_60": "Không cần chỉnh liều; tránh lạm dụng kéo dài",
            "under_30": "Thận trọng nếu dùng kéo dài (mất điện giải)",
        },
        "side_effects": [
            "Đau quặn bụng, tiêu chảy",
            "Buồn nôn",
            "Kích ứng trực tràng (dạng suppository)",
            "Mất điện giải (giảm K+, Na+) nếu lạm dụng",
        ],
        "interactions": [
            "Sữa, antacid, PPI: hòa tan sớm viên bao tan trong ruột → kích ứng dạ dày",
            "Thuốc lợi tiểu, corticosteroid: tăng nguy cơ hạ K+ khi tiêu chảy nhiều",
        ],
        "pregnancy": "C – dùng ngắn hạn khi cần thiết; ưu tiên thuốc an toàn hơn nếu có",
        "mechanism_of_action": (
            "Bisacodyl là thuốc nhuận tràng kích thích, sau khi được thủy phân ở đại tràng sẽ kích thích đám rối thần kinh "
            "cơ trơn ruột (plexus myentericus), tăng nhu động đại tràng và tiết nước vào lòng ruột, giúp tống phân."
        ),
        "monitoring": [
            "Tần suất và tính chất phân",
            "Dấu hiệu mất nước, rối loạn điện giải nếu dùng lặp lại",
        ],
        "precautions": [
            "Chỉ dùng ngắn hạn (vài ngày); không dùng kéo dài hàng tuần–tháng vì nguy cơ lệ thuộc thuốc và rối loạn điện giải.",
            "Nếu táo bón kéo dài, cần tìm và xử lý nguyên nhân (chế độ ăn, thuốc, bệnh nền).",
        ],
        "pharmacokinetics": {
            "half_life": "Không rõ (tác dụng chủ yếu tại chỗ ở đại tràng)",
            "onset": "PO: 6–12 giờ; PR: 15–60 phút",
            "duration": "Một liều thường có tác dụng trong ngày",
            "protein_binding": "Không đáng kể",
            "clearance": "Bài tiết qua phân và nước tiểu dưới dạng chuyển hóa.",
        },
        "storage": "Bảo quản nơi khô mát, tránh ẩm; suppository cần bảo quản tránh nóng chảy.",
        "black_box_warnings": "Không có cảnh báo hộp đen đặc biệt. Tuy nhiên, lạm dụng kéo dài có thể gây lệ thuộc thuốc và rối loạn điện giải.",
        "drug_interactions": {
            "major": [],
            "moderate": [
                {
                    "drug": "Thuốc lợi tiểu, corticosteroid",
                    "mechanism": "Cả hai đều có thể gây hạ K+; cộng hưởng với tiêu chảy do bisacodyl",
                    "effect": "Tăng nguy cơ hạ K+, loạn nhịp tim",
                    "management": "Theo dõi điện giải nếu dùng nhiều lần hoặc kéo dài.",
                }
            ],
            "minor": [],
        },
        "drug_interactions_detail": {
            "major": [],
            "moderate": [
                {
                    "drug": "Thuốc lợi tiểu, corticosteroid",
                    "mechanism": "Cả hai đều có thể gây hạ K+; cộng hưởng với tiêu chảy do bisacodyl",
                    "effect": "Tăng nguy cơ hạ K+, loạn nhịp tim",
                    "management": "Theo dõi điện giải nếu dùng nhiều lần hoặc kéo dài.",
                }
            ],
            "minor": [],
        },
        "contraindications_detail": {
            "tuyệt_đối": [
                "Tắc ruột, thủng ruột, viêm phúc mạc",
                "Đau bụng cấp chưa rõ nguyên nhân",
            ],
            "tương_đối": [
                "Viêm ruột cấp nặng",
                "Suy thận (tránh lạm dụng kéo dài)",
            ],
        },
        "pregnancy_lactation": {
            "fda_category": "C",
            "pregnancy_details": "Có thể dùng ngắn hạn nếu các biện pháp khác thất bại; ưu tiên bulk-forming/osmotic trước.",
            "lactation": {
                "safety": "Compatible with caution",
                "details": "Hấp thu toàn thân ít; chưa ghi nhận tác dụng phụ rõ ràng ở trẻ bú mẹ.",
                "recommendation": "Có thể dùng ngắn hạn, theo dõi phân của trẻ.",
            },
        },
        "hepatic_adjustment": {
            "mild": "Không cần chỉnh liều",
            "moderate": "Không cần chỉnh liều",
            "severe": "Không cần chỉnh liều",
            "notes": "Tác dụng chủ yếu tại chỗ ở đại tràng.",
        },
        "overdose_management": {
            "symptoms": [
                "Tiêu chảy nhiều, đau bụng, mất nước, hạ K+",
            ],
            "antidote": "Không có antidote đặc hiệu.",
            "treatment": [
                "Ngừng thuốc, bù dịch và điện giải",
                "Điều chỉnh hạ K+ nếu có",
            ],
            "monitoring": "Điện giải, chức năng thận, dấu hiệu mất nước.",
        },
        "reversal_agents": {"available": False, "agents": [], "notes": "Không có antidote đặc hiệu. Điều trị chủ yếu là hỗ trợ và điều trị triệu chứng. Ngừng thuốc ngay. Bù nước và điện giải nếu mất nước."},
        "administration_instructions": {
            "oral": {
                "with_food": "Uống nguyên viên với nước, không nghiền/nhai.",
                "timing": "Uống buổi tối (tác dụng sau 6–12 giờ). Không uống ngay sau khi dùng sữa/antacid.",
            },
            "pr": {
                "notes": "Đặt trực tràng, giữ thuốc càng lâu càng tốt (15–30 phút) cho đến khi muốn đi ngoài.",
            },
        },
        "references": {
            "primary_sources": [
                "AGA guidelines – Management of chronic constipation",
                "UpToDate – Bisacodyl: Drug information",
            ],
            "last_updated": "2025-02-23",
            "evidence_level": "High – guideline-recommended stimulant laxative",
        },
    },

    "Lactulose": {
        "group": "Gastrointestinal - Osmotic Laxative (Disaccharide)",
        "vietnamese_name": "Lactulose, Duphalac",
        "administration": ["PO"],
        "indications": [
            "Táo bón mạn tính",
            "Điều trị và dự phòng bệnh não gan (hepatic encephalopathy)",
        ],
        "contraindications": [
            "Tắc ruột cơ học",
            "Galactosemia",
            "Không dung nạp lactose nặng (thận trọng)",
        ],
        "dosage": {
            "adult_constipation": "15–30ml PO mỗi ngày, có thể điều chỉnh 10–45ml/ngày để đạt 2–3 lần đi phân mềm/ngày",
            "adult_encephalopathy": "25ml PO mỗi 1–2 giờ cho đến khi đạt 2–3 lần đi phân mềm/ngày, sau đó chỉnh liều duy trì",
            "notes": "Có thể pha với nước hoặc nước trái cây để dễ uống. Tác dụng thường sau 24–48 giờ.",
        },
        "renal_adjustment": {
            "normal": "Không cần chỉnh liều",
            "30_60": "Không cần chỉnh liều",
            "under_30": "Không cần chỉnh liều (ít hấp thu hệ thống)",
        },
        "side_effects": [
            "Chướng bụng, đầy hơi (rất thường gặp khi khởi đầu hoặc tăng liều nhanh)",
            "Đau bụng quặn",
            "Tiêu chảy (nếu liều quá cao)",
            "Mất nước, rối loạn điện giải nếu tiêu chảy kéo dài",
        ],
        "interactions": [
            "Thuốc gây tiêu chảy khác: tăng nguy cơ mất nước, rối loạn điện giải",
            "Thuốc kháng acid mạnh hoặc kháng sinh phổ rộng đường ruột có thể giảm hiệu quả trong bệnh não gan",
        ],
        "pregnancy": "B – thường được coi là an toàn trong thai kỳ cho táo bón",
        "mechanism_of_action": (
            "Lactulose là disaccharide tổng hợp không bị tiêu hóa/ hấp thu ở ruột non. "
            "Vào đại tràng, lactulose được vi khuẩn lên men thành acid hữu cơ (lactic, acetic), "
            "tăng áp lực thẩm thấu trong lòng ruột, kéo nước vào lòng đại tràng, làm mềm phân và tăng nhu động. "
            "Trong bệnh não gan, acid hóa lòng đại tràng giúp chuyển NH3 (không ion hóa) sang NH4+ (ion hóa, khó hấp thu), "
            "tăng thải amonia qua phân và giảm nồng độ amonia máu."
        ),
        "monitoring": [
            "Tần suất và tính chất phân (mục tiêu 2–3 lần phân mềm/ngày trong bệnh não gan)",
            "Dấu hiệu mất nước, rối loạn điện giải nếu tiêu chảy kéo dài",
            "Amonia máu và ý thức (bệnh não gan)",
        ],
        "precautions": [
            "Bắt đầu liều thấp và tăng dần để giảm đầy hơi, chướng bụng",
            "Cân nhắc giảm liều khi đã đạt mục tiêu phân mềm; tránh tiêu chảy nặng",
            "Thận trọng ở bệnh nhân đái tháo đường (có chứa lượng nhỏ lactose, galactose, fructose)",
        ],
        "pharmacokinetics": {
            "half_life": "Không áp dụng (không hấp thu đáng kể)",
            "onset": "24–48 giờ cho tác dụng nhuận tràng; vài giờ cho tác dụng trong bệnh não gan (liều tấn công cao)",
            "duration": "Phụ thuộc tần suất dùng và đáp ứng",
            "protein_binding": "Không áp dụng",
            "clearance": "Lên men bởi vi khuẩn đại tràng, phần nhỏ không hấp thu thải qua phân",
        },
        "storage": "Bảo quản ở nhiệt độ phòng, tránh nóng; siro có thể đặc hơn nếu lạnh.",
        "black_box_warnings": None,
        "drug_interactions_detail": {
            "major": [],
            "moderate": [
                {
                    "drug": "Thuốc lợi tiểu, thuốc gây tiêu chảy khác",
                    "mechanism": "Cộng hưởng gây mất nước và rối loạn điện giải",
                    "effect": "Tăng nguy cơ hạ K+, hạ Na+, suy thận trước thận",
                    "management": "Theo dõi điện giải nếu dùng kéo dài hoặc phối hợp nhiều thuốc.",
                }
            ],
            "minor": [],
        },
        "contraindications_detail": {
            "tuyệt_đối": ["Tắc ruột cơ học đã xác định", "Galactosemia"],
            "tương_đối": [
                "Bụng cấp chưa rõ nguyên nhân",
                "Không dung nạp lactose nặng",
            ],
        },
        "pregnancy_lactation": {
            "fda_category": "B",
            "pregnancy_details": "Được xem là an toàn cho táo bón trong thai kỳ; ít hấp thu toàn thân.",
            "lactation": {
                "safety": "Compatible",
                "details": "Ít hấp thu nên rất ít vào sữa mẹ.",
                "recommendation": "Có thể dùng khi cho con bú.",
            },
        },
        "hepatic_adjustment": {
            "mild": "Không đổi",
            "moderate": "Không đổi",
            "severe": "Không đổi (thường dùng chính trong suy gan/bệnh não gan)",
            "notes": "Lactulose là thuốc lựa chọn hàng đầu trong bệnh não gan.",
        },
        "overdose_management": {
            "symptoms": [
                "Tiêu chảy nhiều lần/ngày",
                "Mất nước, chuột rút, choáng váng",
            ],
            "antidote": "Không có; điều trị hỗ trợ.",
            "treatment": [
                "Giảm hoặc ngừng lactulose tạm thời",
                "Bù dịch, điện giải đường uống hoặc truyền tĩnh mạch nếu cần",
            ],
            "monitoring": "Điện giải, chức năng thận, dấu hiệu mất nước.",
        },
        "reversal_agents": {"available": False, "agents": [], "notes": "Không có antidote đặc hiệu. Điều trị chủ yếu là hỗ trợ và điều trị triệu chứng. Ngừng thuốc ngay. Bù nước và điện giải nếu mất nước."},
        "administration_instructions": {
            "oral": {
                "with_food": "Có thể uống cùng hoặc không cùng thức ăn; có thể pha loãng với nước hoặc nước trái cây.",
                "timing": "Dùng 1–2 lần/ngày, điều chỉnh theo đáp ứng; bệnh não gan có thể chia nhiều lần.",
            }
        },
        "references": {
            "primary_sources": [
                "UpToDate – Lactulose: Drug information",
                "AASLD guidelines – Hepatic encephalopathy",
            ],
            "last_updated": "2025-02-18",
            "evidence_level": "High – guideline-supported in hepatic encephalopathy",
        },
             "drug_interactions": {
             "major": [],
             "moderate": [],
             "minor": [
                 {
                     "drug": "Thuốc gây tiêu chảy khác: tăng nguy cơ mất nước, rối loạn điện giải",
                     "mechanism": "Tương tác lâm sàng"
                 },
                 {
                     "drug": "Thuốc kháng acid mạnh hoặc kháng sinh phổ rộng đường ruột có thể giảm hiệu quả trong bệnh não gan",
                     "mechanism": "Tương tác lâm sàng"
                 }
             ]
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
            "risk_flags": {
                "high_alert": False,
                "narrow_therapeutic_index": False,
                "bleeding_risk": False,
                "organ_toxicity": [],
                "qt_prolongation": False,
                "hepatotoxicity": False,
                "nephrotoxicity": False,
                "requires_monitoring": ["Electrolytes (long-term use)"],
            },
            "guideline_tags": [
                "ACG 2013 Constipation Guidelines",
                "FDA - Laxative safety",
            ]
},

    "Polyethylene glycol 3350": {
        "group": "Gastrointestinal - Osmotic Laxative (PEG 3350)",
        "vietnamese_name": "Polyethylene glycol 3350, PEG, Forlax, Miralax",
        "administration": ["PO"],
        "indications": [
            "Táo bón mạn tính",
            "Chuẩn bị đại tràng (liều cao + điện giải – tùy chế phẩm, ngoài phạm vi bản ghi này)",
        ],
        "contraindications": [
            "Tắc ruột cơ học",
            "Thủng ruột, viêm phúc mạc",
            "Bệnh viêm ruột nặng trong đợt cấp (thận trọng)",
        ],
        "dosage": {
            "adult_constipation": "17g bột (1 gói hoặc 1 muỗng đong) hòa trong 120–240ml nước, uống 1 lần/ngày; có thể tăng tối đa 34g/ngày theo đáp ứng",
            "notes": "Tác dụng thường sau 24–72 giờ. Không dùng liều chuẩn bị đại tràng nếu chưa có chỉ định rõ và phác đồ riêng.",
        },
        "renal_adjustment": {
            "normal": "Không cần chỉnh liều",
            "30_60": "Không cần chỉnh liều (ít hấp thu)",
            "under_30": "Thận trọng nếu dùng liều rất cao (chuẩn bị đại tràng có kèm điện giải)",
        },
        "side_effects": [
            "Đầy hơi, chướng bụng",
            "Đau quặn bụng nhẹ",
            "Tiêu chảy nếu liều cao",
        ],
        "interactions": [
            "Ít tương tác đáng kể; nếu tiêu chảy nhiều có thể giảm hấp thu thuốc uống khác",
        ],
        "pregnancy": "C (đa số dữ liệu cho thấy an toàn tương đối; dùng khi cần thiết)",
        "mechanism_of_action": (
            "PEG 3350 là polymer trơ, không hấp thu, giữ nước theo cơ chế thẩm thấu trong lòng ruột, "
            "tăng lượng nước trong phân, làm mềm phân và tăng nhu động đại tràng. "
            "Không gây mất điện giải đáng kể ở liều điều trị táo bón thông thường."
        ),
        "monitoring": [
            "Tần suất và tính chất phân",
            "Dấu hiệu mất nước nếu lạm dụng hoặc dùng liều cao",
        ],
        "precautions": [
            "Không dùng kéo dài liều cao mà không đánh giá nguyên nhân táo bón",
            "Thận trọng ở bệnh nhân có nguy cơ tắc ruột (đau bụng cấp, nôn, chướng bụng nhiều)",
        ],
        "pharmacokinetics": {
            "half_life": "Không áp dụng (không hấp thu đáng kể)",
            "onset": "24–72 giờ",
            "duration": "Phụ thuộc tần suất dùng",
            "protein_binding": "Không áp dụng",
            "clearance": "Thải nguyên dạng qua phân",
        },
        "storage": "Bảo quản bột khô ở nhiệt độ phòng, tránh ẩm; dung dịch sau pha dùng trong 24 giờ.",
        "black_box_warnings": None,
        "drug_interactions_detail": {
            "major": [],
            "moderate": [],
            "minor": [],
        },
        "contraindications_detail": {
            "tuyệt_đối": [
                "Tắc ruột cơ học, thủng ruột, viêm phúc mạc",
            ],
            "tương_đối": [
                "Bụng cấp chưa rõ nguyên nhân",
                "Bệnh viêm ruột nặng trong đợt cấp",
            ],
        },
        "pregnancy_lactation": {
            "fda_category": "C",
            "pregnancy_details": "Ít hấp thu; thường được xem là lựa chọn an toàn tương đối nếu cần nhuận tràng thẩm thấu.",
            "lactation": {
                "safety": "Compatible",
                "details": "Không hấp thu đáng kể nên rất ít vào sữa mẹ.",
                "recommendation": "Có thể dùng khi cho con bú.",
            },
        },
        "hepatic_adjustment": {
            "mild": "Không đổi",
            "moderate": "Không đổi",
            "severe": "Không đổi",
            "notes": "Không chuyển hóa qua gan.",
        },
        "overdose_management": {
            "symptoms": [
                "Tiêu chảy nhiều, mất nước",
                "Chuột rút bụng",
            ],
            "antidote": "Không có; điều trị hỗ trợ.",
            "treatment": [
                "Ngừng PEG, bù dịch và điện giải",
            ],
            "monitoring": "Điện giải, chức năng thận nếu tiêu chảy kéo dài.",
        },
        "reversal_agents": {"available": False, "agents": [], "notes": "Không có antidote đặc hiệu. Điều trị chủ yếu là hỗ trợ và điều trị triệu chứng. Ngừng thuốc ngay. Bù nước và điện giải nếu mất nước."},
        "administration_instructions": {
            "oral": {
                "with_food": "Hòa tan bột trong nước, có thể uống cùng hoặc không cùng thức ăn.",
                "timing": "Thường dùng 1 lần/ngày; có thể điều chỉnh thời điểm phù hợp thói quen đi ngoài.",
            }
        },
        "references": {
            "primary_sources": [
                "UpToDate – Polyethylene glycol: Drug information",
                "AGA guidelines – Management of chronic constipation",
            ],
            "last_updated": "2025-02-18",
            "evidence_level": "High – guideline-recommended osmotic laxative",
        },
              "drug_interactions": {
              "major": [],
              "moderate": [],
              "minor": [
                  {
                      "drug": "Ít tương tác đáng kể; nếu tiêu chảy nhiều có thể giảm hấp thu thuốc uống khác",
                      "mechanism": "Tương tác lâm sàng"
                  }
              ]
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
            "risk_flags": {
                "high_alert": False,
                "narrow_therapeutic_index": False,
                "bleeding_risk": False,
                "organ_toxicity": [],
                "qt_prolongation": False,
                "hepatotoxicity": False,
                "nephrotoxicity": False,
                "requires_monitoring": ["Electrolytes (long-term use)"],
            },
            "guideline_tags": [
                "ACG 2013 Constipation Guidelines",
                "FDA - Laxative safety",
            ]
},

    "Senna (sennosides)": {
        "group": "Gastrointestinal - Stimulant Laxative (Anthraquinone)",
        "vietnamese_name": "Senna, Sennosides, thuốc nhuận tràng thảo dược (lá muồng trâu, diếp cá senna)",
        "administration": ["PO"],
        "indications": [
            "Táo bón cấp hoặc ngắn hạn",
            "Táo bón do thuốc opioid (kết hợp stool softener)",
        ],
        "contraindications": [
            "Tắc ruột, thủng ruột, viêm phúc mạc",
            "Viêm ruột cấp (viêm loét đại tràng đợt cấp nặng, Crohn nặng)",
            "Đau bụng cấp chưa rõ nguyên nhân",
        ],
        "dosage": {
            "adult_constipation": "8.6–17.2mg sennosides PO vào buổi tối; có thể tăng đến 34.4mg/ngày tùy đáp ứng (tùy chế phẩm)",
            "notes": "Thường bắt đầu liều thấp, có thể phối hợp với docusate (stool softener) trong táo bón do opioid.",
        },
        "renal_adjustment": {
            "normal": "Không cần chỉnh liều",
            "30_60": "Không cần chỉnh liều; tránh lạm dụng kéo dài",
            "under_30": "Thận trọng nếu sử dụng kéo dài do nguy cơ mất điện giải",
        },
        "side_effects": [
            "Đau quặn bụng, tiêu chảy",
            "Nước tiểu màu vàng–nâu (vô hại)",
            "Mất điện giải (giảm K+) nếu lạm dụng kéo dài",
            "Hiếm: viêm đại tràng nếu dùng quá liều kéo dài",
        ],
        "interactions": [
            "Thuốc lợi tiểu, corticosteroid, digoxin: tăng nguy cơ mất K+ và độc tính digoxin",
        ],
        "pregnancy": "C – có thể dùng ngắn hạn; ưu tiên thuốc an toàn hơn nếu có",
        "mechanism_of_action": (
            "Senna chứa sennosides (glycosid anthraquinone), được vi khuẩn đại tràng chuyển thành dạng hoạt tính "
            "kích thích đám rối thần kinh ruột, tăng nhu động đại tràng và tiết dịch, giúp tống phân. "
            "Tác dụng sau 6–12 giờ khi uống buổi tối."
        ),
        "monitoring": [
            "Số lần đi ngoài, tính chất phân",
            "Dấu hiệu mất nước và hạ K+ nếu dùng kéo dài",
        ],
        "precautions": [
            "Chỉ dùng ngắn hạn; không dùng như biện pháp điều trị táo bón mạn mà không đánh giá nguyên nhân.",
            "Tránh lạm dụng như 'thuốc giảm cân' hoặc 'thanh lọc' vì gây rối loạn điện giải và tổn thương đại tràng.",
        ],
        "pharmacokinetics": {
            "half_life": "Không rõ; tác dụng chủ yếu tại đại tràng",
            "onset": "6–12 giờ (uống buổi tối → đi ngoài sáng hôm sau)",
            "duration": "Tác dụng trong 1 ngày",
            "protein_binding": "Không đáng kể",
            "clearance": "Chuyển hóa bởi vi khuẩn ruột, thải qua phân và một phần nước tiểu.",
        },
        "storage": "Bảo quản nơi khô mát, tránh ẩm; tránh để trẻ em tự dùng vì dạng 'thảo dược' dễ bị lạm dụng.",
        "black_box_warnings": "Không có cảnh báo hộp đen đặc biệt. Tuy nhiên, lạm dụng kéo dài có thể gây lệ thuộc thuốc, rối loạn điện giải và tổn thương đại tràng.",
        "drug_interactions": {
            "major": [],
            "moderate": [
                {
                    "drug": "Digoxin",
                    "mechanism": "Hạ K+ do senna làm tăng nhạy cảm với độc tính digoxin",
                    "effect": "Tăng nguy cơ loạn nhịp do digoxin",
                    "management": "Theo dõi K+ và ECG nếu dùng cùng.",
                },
                {
                    "drug": "Thuốc lợi tiểu, corticosteroid",
                    "mechanism": "Cộng hưởng hạ K+",
                    "effect": "Tăng nguy cơ hạ K+ và biến chứng tim mạch",
                    "management": "Hạn chế dùng kéo dài; theo dõi điện giải.",
                },
            ],
            "minor": [],
        },
        "drug_interactions_detail": {
            "major": [],
            "moderate": [
                {
                    "drug": "Digoxin",
                    "mechanism": "Hạ K+ do senna làm tăng nhạy cảm với độc tính digoxin",
                    "effect": "Tăng nguy cơ loạn nhịp do digoxin",
                    "management": "Theo dõi K+ và ECG nếu dùng cùng.",
                },
                {
                    "drug": "Thuốc lợi tiểu, corticosteroid",
                    "mechanism": "Cộng hưởng hạ K+",
                    "effect": "Tăng nguy cơ hạ K+ và biến chứng tim mạch",
                    "management": "Hạn chế dùng kéo dài; theo dõi điện giải.",
                },
            ],
            "minor": [],
        },
        "contraindications_detail": {
            "tuyệt_đối": [
                "Tắc ruột, thủng ruột, viêm phúc mạc",
                "Đau bụng cấp chưa rõ nguyên nhân",
            ],
            "tương_đối": [
                "Viêm ruột mạn tính nặng",
                "Suy thận (tránh lạm dụng kéo dài)",
            ],
        },
        "pregnancy_lactation": {
            "fda_category": "C",
            "pregnancy_details": "Có thể dùng ngắn hạn khi cần thiết; ưu tiên các biện pháp không dùng thuốc hoặc osmotic/bulk-forming trước.",
            "lactation": {
                "safety": "Compatible with caution",
                "details": "Một lượng nhỏ chất chuyển hóa có thể vào sữa; có báo cáo trẻ đi phân lỏng nhẹ.",
                "recommendation": "Có thể dùng ngắn hạn; theo dõi phân của trẻ.",
            },
        },
        "hepatic_adjustment": {
            "mild": "Không cần chỉnh liều",
            "moderate": "Không cần chỉnh liều",
            "severe": "Không cần chỉnh liều",
            "notes": "Tác dụng chủ yếu tại đại tràng.",
        },
        "overdose_management": {
            "symptoms": [
                "Tiêu chảy nhiều, mất nước, hạ K+",
                "Đau bụng quặn nhiều",
            ],
            "antidote": "Không có antidote đặc hiệu.",
            "treatment": [
                "Ngừng senna",
                "Bù dịch và điện giải; điều chỉnh hạ K+",
            ],
            "monitoring": "Điện giải, chức năng thận, ECG nếu có yếu tố nguy cơ.",
        },
        "reversal_agents": {"available": False, "agents": [], "notes": "Không có antidote đặc hiệu. Điều trị chủ yếu là hỗ trợ và điều trị triệu chứng. Ngừng thuốc ngay. Bù nước và điện giải nếu mất nước. Theo dõi ECG nếu có yếu tố nguy cơ."},
        "administration_instructions": {
            "oral": {
                "with_food": "Có thể uống với hoặc không với thức ăn.",
                "timing": "Thường uống buổi tối để đi ngoài buổi sáng hôm sau.",
            }
        },
        "references": {
            "primary_sources": [
                "AGA guidelines – Management of chronic constipation and opioid-induced constipation",
                "UpToDate – Senna: Drug information",
            ],
            "last_updated": "2025-02-23",
            "evidence_level": "High – thuốc phổ biến, được khuyến nghị trong táo bón cấp và do opioid",
        },
            "risk_flags": {
                "high_alert": False,
                "narrow_therapeutic_index": False,
                "bleeding_risk": False,
                "organ_toxicity": [],
                "qt_prolongation": False,
                "hepatotoxicity": False,
                "nephrotoxicity": False,
                "requires_monitoring": ["Electrolytes (long-term use)"],
            },
            "guideline_tags": [
                "ACG 2013 Constipation Guidelines",
                "FDA - Laxative safety",
            ]
    },
    
    "Docusate": {
        "group": "Gastrointestinal - Stool Softener (Surfactant Laxative)",
        "vietnamese_name": "Docusate sodium, Docusate calcium, Colace, Docusol",
        "brand_names": {
            "common": ["Colace", "Docusol", "Surfak"],
            "vietnam": ["Docusate 100mg", "Colace", "Docusol"]
        },
        "administration": ["PO"],
        "indications": [
            "Táo bón (làm mềm phân)",
            "Táo bón do opioid (kết hợp với stimulant laxative)",
            "Phòng ngừa táo bón sau phẫu thuật",
            "Bệnh nhân cần tránh gắng sức khi đi ngoài (bệnh tim, trĩ, nứt hậu môn)"
        ],
        "contraindications": [
            "Tắc ruột cơ học",
            "Đau bụng cấp chưa rõ nguyên nhân",
            "Dị ứng docusate"
        ],
        "dosage": {
            "adult_po": "50-200mg PO x 1-3 lần/ngày",
            "adult_typical": "100mg PO x 2 lần/ngày",
            "pediatric_2_12_years": "50-150mg PO x 1-2 lần/ngày",
            "pediatric_over_12_years": "50-200mg PO x 1-3 lần/ngày",
            "geriatric_dosing": "Không cần chỉnh liều",
            "notes": "Tác dụng sau 1-3 ngày. An toàn cho dùng lâu dài. Thường kết hợp với stimulant laxative (senna, bisacodyl) trong táo bón do opioid."
        },
        "renal_adjustment": {
            "normal": "Không cần chỉnh liều",
            "30_60": "Không cần chỉnh liều",
            "under_30": "Không cần chỉnh liều",
            "notes": "Docusate ít hấp thu toàn thân, tác dụng chủ yếu tại chỗ ở ruột."
        },
        "side_effects": [
            "Đau bụng nhẹ",
            "Buồn nôn",
            "Tiêu chảy (nếu dùng liều cao)",
            "Phát ban (hiếm)"
        ],
        "interactions": [
            "Có thể tăng hấp thu các thuốc tan trong dầu (vitamin D, A, E, K)",
            "Mineral oil: không dùng cùng (tăng hấp thu mineral oil)"
        ],
        "pregnancy": "C - Thường được coi là an toàn trong thai kỳ",
        "mechanism_of_action": "Stool softener (surfactant laxative). Docusate là chất hoạt động bề mặt (surfactant), làm giảm sức căng bề mặt của phân, cho phép nước và lipid thấm vào phân, làm mềm phân và dễ đi ngoài hơn. Không kích thích nhu động ruột, chỉ làm mềm phân. An toàn cho dùng lâu dài.",
        "monitoring": [
            "Tần suất và tính chất phân",
            "Dấu hiệu tiêu chảy nếu dùng liều cao"
        ],
        "precautions": [
            "Tác dụng chậm (1-3 ngày) - không mong đợi tác dụng ngay",
            "An toàn cho dùng lâu dài",
            "Thường kết hợp với stimulant laxative (senna, bisacodyl) trong táo bón do opioid",
            "Không dùng cùng mineral oil"
        ],
        "pharmacokinetics": {
            "half_life": "Không rõ (ít hấp thu)",
            "onset": "1-3 ngày",
            "duration": "Phụ thuộc tần suất dùng",
            "protein_binding": "Không áp dụng",
            "clearance": "Thải qua phân (không hấp thu đáng kể)"
        },
        "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm",
        "black_box_warnings": None,
        "drug_interactions": {
            "major": [],
            "moderate": [
                {
                    "drug": "Mineral oil",
                    "mechanism": "Docusate tăng hấp thu mineral oil",
                    "effect": "Tăng nguy cơ độc tính mineral oil (viêm phổi lipid)",
                    "management": "Không dùng cùng mineral oil."
                }
            ],
            "minor": []
        },
        "contraindications_detail": {
            "tuyệt_đối": [
                "Tắc ruột cơ học",
                "Đau bụng cấp chưa rõ nguyên nhân"
            ],
            "tương_đối": [
                "Tiêu chảy - có thể làm nặng"
            ]
        },
        "pregnancy_lactation": {
            "fda_category": "C",
            "pregnancy_details": "Thường được coi là an toàn trong thai kỳ. Ít hấp thu toàn thân.",
            "lactation": {
                "safety": "Compatible",
                "details": "Ít hấp thu nên rất ít vào sữa mẹ.",
                "recommendation": "Có thể dùng khi cho con bú."
            }
        },
        "hepatic_adjustment": {
            "mild": "Không cần chỉnh liều",
            "moderate": "Không cần chỉnh liều",
            "severe": "Không cần chỉnh liều",
            "notes": "Tác dụng chủ yếu tại chỗ ở ruột, không phụ thuộc chuyển hóa gan."
        },
        "overdose_management": {
            "symptoms": [
                "Tiêu chảy",
                "Đau bụng"
            ],
            "antidote": "Không có antidote đặc hiệu",
            "treatment": [
                "Ngừng thuốc",
                "Bù dịch nếu tiêu chảy nhiều"
            ],
            "monitoring": "Theo dõi triệu chứng"
        },
        "reversal_agents": {
            "available": False,
            "agents": []
        },
        "administration_instructions": {
            "oral": {
                "with_food": "Có thể uống với hoặc không với thức ăn",
                "timing": "Uống 1-3 lần/ngày. Tác dụng sau 1-3 ngày."
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
            "ACG 2013 Constipation Guidelines",
            "FDA - Laxative safety"
        ],
        "references": {
            "primary_sources": [
                "UpToDate - Docusate: Drug information",
                "ACG 2013 Constipation Guidelines",
                "FDA Drug Information"
            ],
            "last_updated": "2025-01-15",
            "evidence_level": "High - Guideline-recommended stool softener"
        },
        "cost_estimate": {
            "generic": "Thấp",
            "brand": "Thấp-trung bình",
            "notes": "OTC medication, giá rẻ"
        }
    },
    
    "Magnesium hydroxide": {
        "group": "Gastrointestinal - Osmotic Laxative (Antacid/Laxative)",
        "vietnamese_name": "Magnesium hydroxide, Milk of Magnesia, Maalox",
        "brand_names": {
            "common": ["Milk of Magnesia", "Maalox", "Phillips"],
            "vietnam": ["Magnesium hydroxide", "Milk of Magnesia"]
        },
        "administration": ["PO"],
        "indications": [
            "Táo bón cấp",
            "Đau rát thượng vị, ợ chua (tác dụng antacid)",
            "Chuẩn bị ruột trước phẫu thuật/nội soi (liều cao)"
        ],
        "contraindications": [
            "Suy thận nặng (CrCl <30 ml/phút) - nguy cơ tăng magie máu",
            "Tắc ruột cơ học",
            "Viêm ruột cấp nặng",
            "Bệnh tim nặng (nguy cơ rối loạn điện giải)"
        ],
        "dosage": {
            "adult_constipation": "30-60ml hỗn dịch (2.4-4.8g) PO vào buổi tối hoặc chia 2 lần/ngày",
            "adult_antacid": "5-15ml hỗn dịch PO sau bữa ăn và khi có triệu chứng",
            "adult_bowel_prep": "240ml hỗn dịch PO (theo phác đồ chuẩn bị ruột)",
            "pediatric_2_5_years": "5-15ml PO x 1-2 lần/ngày",
            "pediatric_6_11_years": "15-30ml PO x 1-2 lần/ngày",
            "pediatric_over_12_years": "30-60ml PO x 1-2 lần/ngày",
            "geriatric_dosing": "Thận trọng ở người già, đặc biệt nếu có suy thận",
            "notes": "Tác dụng sau 30 phút - 6 giờ. Không dùng kéo dài ở suy thận. Có thể dùng như antacid hoặc laxative tùy liều."
        },
        "renal_adjustment": {
            "normal": "Không cần chỉnh liều, nhưng tránh dùng liều cao kéo dài",
            "30_60": "Giảm liều, tránh dùng kéo dài",
            "under_30": "CHỐNG CHỈ ĐỊNH - nguy cơ tăng magie máu nặng",
            "dialysis": "CHỐNG CHỈ ĐỊNH",
            "notes": "Magnesium hydroxide thải trừ qua thận. Suy thận làm giảm thải trừ, tăng nguy cơ tăng magie máu nặng (yếu cơ, loạn nhịp tim, suy hô hấp)."
        },
        "side_effects": [
            "Tiêu chảy (phổ biến)",
            "Đau quặn bụng",
            "Tăng magie máu (ở suy thận - nguy hiểm)",
            "Giảm phospho máu (nếu dùng kéo dài)",
            "Buồn nôn"
        ],
        "interactions": [
            "Thuốc khác: giảm hấp thu do tạo phức hoặc tăng nhu động ruột",
            "Digoxin: giảm hấp thu digoxin",
            "Quinolone, tetracycline: giảm hấp thu - cách 2 giờ",
            "Bisphosphonates: giảm hấp thu - cách 2 giờ"
        ],
        "pregnancy": "B - Thường an toàn nếu dùng ngắn hạn",
        "mechanism_of_action": "Osmotic laxative và antacid. Magnesium hydroxide phản ứng với acid dạ dày tạo magnesium chloride và nước (tác dụng antacid). Trong ruột, tạo magnesium chloride không hấp thu, tăng áp lực thẩm thấu trong lòng ruột, kéo nước vào lòng ruột, làm mềm phân và tăng nhu động. Tác dụng nhanh (30 phút - 6 giờ).",
        "monitoring": [
            "Tần suất và tính chất phân",
            "Magie máu (nếu dùng kéo dài hoặc suy thận) - nguy cơ tăng magie máu",
            "Dấu hiệu tăng magie máu: yếu cơ, buồn ngủ, loạn nhịp tim, suy hô hấp",
            "Chức năng thận (creatinine, eGFR) - đặc biệt quan trọng"
        ],
        "precautions": [
            "CHỐNG CHỈ ĐỊNH ở suy thận nặng - nguy cơ tăng magie máu nặng",
            "Không dùng kéo dài ở suy thận trung bình",
            "Uống cách xa các thuốc khác ít nhất 2 giờ (giảm hấp thu)",
            "Tác dụng nhanh - không dùng trước khi ngủ",
            "Có thể dùng như antacid (liều thấp) hoặc laxative (liều cao)"
        ],
        "pharmacokinetics": {
            "half_life": "Không áp dụng (tác dụng tại chỗ)",
            "onset": "30 phút - 6 giờ",
            "duration": "Vài giờ",
            "protein_binding": "Không áp dụng",
            "clearance": "Thận (thải trừ magie), một phần qua phân"
        },
        "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh đông lạnh. Lắc kỹ hỗn dịch trước khi dùng.",
        "black_box_warnings": "CHỐNG CHỈ ĐỊNH ở suy thận nặng (CrCl <30 ml/phút). Tăng magie máu có thể gây yếu cơ, loạn nhịp tim, suy hô hấp, có thể tử vong.",
        "drug_interactions": {
            "major": [],
            "moderate": [
                {
                    "drug": "Digoxin, Quinolone, Tetracycline, Bisphosphonates",
                    "mechanism": "Magnesium hydroxide giảm hấp thu các thuốc này",
                    "effect": "Giảm nồng độ thuốc, giảm hiệu quả điều trị",
                    "management": "Uống cách xa ít nhất 2 giờ."
                }
            ],
            "minor": []
        },
        "contraindications_detail": {
            "tuyệt_đối": [
                "Suy thận nặng (CrCl <30 ml/phút) - CHỐNG CHỈ ĐỊNH",
                "Tắc ruột cơ học",
                "Viêm ruột cấp nặng"
            ],
            "tương_đối": [
                "Suy thận trung bình (CrCl 30-60) - giảm liều, tránh dùng kéo dài",
                "Bệnh tim nặng - nguy cơ rối loạn điện giải"
            ]
        },
        "pregnancy_lactation": {
            "fda_category": "B",
            "pregnancy_details": "Thường an toàn nếu dùng ngắn hạn cho táo bón hoặc ợ chua trong thai kỳ.",
            "lactation": {
                "safety": "Compatible",
                "details": "Magnesium là thành phần sinh lý. Nguy cơ thấp nếu liều vừa phải.",
                "recommendation": "Có thể dùng khi cho con bú, tránh lạm dụng."
            }
        },
        "hepatic_adjustment": {
            "mild": "Không cần chỉnh liều",
            "moderate": "Không cần chỉnh liều",
            "severe": "Không cần chỉnh liều",
            "notes": "Tác dụng chủ yếu tại chỗ ở ruột, không phụ thuộc chuyển hóa gan."
        },
        "overdose_management": {
            "symptoms": [
                "Tiêu chảy nhiều",
                "Tăng magie máu: yếu cơ, buồn ngủ, loạn nhịp tim, suy hô hấp (ở suy thận)"
            ],
            "antidote": "Calcium gluconate hoặc calcium chloride IV (đối kháng magie)",
            "treatment": [
                "Ngừng thuốc",
                "Bù dịch nếu tiêu chảy nhiều",
                "Điều trị tăng magie máu: calcium gluconate 1-3g IV chậm",
                "Lọc máu nếu tăng magie máu nặng ở suy thận"
            ],
            "monitoring": "Magie máu, ECG, dấu hiệu sinh tồn, chức năng thận"
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
                "with_food": "Có thể uống với hoặc không với thức ăn",
                "timing": "Laxative: uống buổi tối hoặc chia 2 lần/ngày. Antacid: sau bữa ăn và khi có triệu chứng. Lắc kỹ hỗn dịch trước khi dùng."
            }
        },
        "risk_flags": {
            "high_alert": True,
            "narrow_therapeutic_index": False,
            "bleeding_risk": False,
            "organ_toxicity": ["renal"],
            "qt_prolongation": False,
            "hepatotoxicity": False,
            "nephrotoxicity": False,
            "requires_monitoring": ["Magnesium (if renal impairment)"]
        },
        "guideline_tags": [
            "ACG 2013 Constipation Guidelines",
            "FDA - Laxative safety"
        ],
        "references": {
            "primary_sources": [
                "UpToDate - Magnesium hydroxide: Drug information",
                "ACG 2013 Constipation Guidelines",
                "FDA Drug Information"
            ],
            "last_updated": "2025-01-15",
            "evidence_level": "High - Guideline-recommended osmotic laxative"
        },
        "cost_estimate": {
            "generic": "Thấp",
            "brand": "Thấp",
            "notes": "OTC medication, giá rất rẻ"
        }
    }
}

__all__ = ["LAXATIVES_DRUGS"]



