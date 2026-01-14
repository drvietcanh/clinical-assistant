"""Gastrointestinal Drugs - Antacids
Aluminum hydroxide, Magnesium hydroxide, Calcium carbonate"""

ANTACIDS_DRUGS = {
    "Aluminum hydroxide/Magnesium hydroxide": {
        "group": "Gastrointestinal - Antacid (Aluminum/Magnesium hydroxide combination)",
        "vietnamese_name": "Nhôm hydroxide/Magiê hydroxide, Maalox, Mylanta",
        "administration": ["PO"],
        "indications": [
            "Đau rát thượng vị, ợ chua, khó tiêu do tăng acid dạ dày",
            "Viêm dạ dày, loét dạ dày-tá tràng (giảm triệu chứng, không thay thế PPI/H2)",
            "Trào ngược dạ dày-thực quản (giảm triệu chứng nhanh)",
        ],
        "contraindications": [
            "Suy thận nặng (nguy cơ tích tụ nhôm và magiê)",
            "Giảm phospho máu nặng (nhôm gắn phosphat)",
            "Tắc ruột hoặc liệt ruột",
        ],
        "dosage": {
            "adult_dyspepsia": "5–10ml hỗn dịch hoặc 1–2 viên nhai sau bữa ăn và khi có triệu chứng, tối đa 4 lần/ngày",
            "notes": "Không dùng kéo dài >2 tuần liên tục nếu không được bác sĩ đánh giá nguyên nhân. Uống cách xa thuốc khác ít nhất 2 giờ.",
        },
        "renal_adjustment": {
            "normal": "Không đổi nhưng tránh dùng liều cao kéo dài",
            "30_60": "Giảm số lần dùng, tránh dùng kéo dài",
            "under_30": "Tránh dùng (nguy cơ tích tụ nhôm/magiê và bệnh não, loạn nhịp)",
        },
        "side_effects": [
            "Táo bón (nhôm)",
            "Tiêu chảy (magiê) – phối hợp giúp cân bằng",
            "Buồn nôn, đầy hơi",
            "Tăng magiê máu, tăng nhôm máu ở suy thận (nguy hiểm)",
            "Giảm phospho máu nếu dùng kéo dài",
        ],
        "interactions": [
            "Fluoroquinolones, tetracyclines: giảm hấp thu do tạo phức chelat",
            "Levothyroxine, digoxin, sắt: giảm hấp thu",
            "Bisphosphonates: giảm hấp thu mạnh",
        ],
        "pregnancy": "B – thường an toàn nếu dùng ngắn hạn, liều thấp",
        "mechanism_of_action": (
            "Antacid không hấp thu, trung hòa acid dạ dày tại chỗ bằng phản ứng với HCl tạo muối và nước, "
            "làm tăng pH dạ dày, giảm hoạt tính pepsin và giảm kích ứng niêm mạc. "
            "Nhôm hydroxide gây táo bón và gắn phosphat; magiê hydroxide gây tiêu chảy và tăng nhu động, "
            "nên phối hợp giúp cân bằng tác dụng phụ trên ruột."
        ),
        "monitoring": [
            "Triệu chứng lâm sàng: giảm đau rát, ợ chua",
            "Ở bệnh nhân suy thận: theo dõi creatinin, magiê, phospho nếu dùng > vài ngày",
        ],
        "precautions": [
            "Không dùng thay thế PPI/H2 trong loét dạ dày nặng hoặc GERD có biến chứng",
            "Uống cách xa PPI/H2 và các thuốc uống khác ít nhất 2 giờ",
            "Không dùng kéo dài ở bệnh nhân suy thận hoặc người cao tuổi",
        ],
        "pharmacokinetics": {
            "half_life": "Không áp dụng (tác dụng tại chỗ, hầu như không hấp thu)",
            "onset": "Vài phút sau uống",
            "duration": "1–3 giờ tùy lượng acid và thức ăn",
            "protein_binding": "Không áp dụng",
            "clearance": "Thải qua phân; một phần nhỏ ion nhôm/magiê hấp thu được thải qua thận",
        },
        "storage": "Bảo quản ở nhiệt độ phòng (15–30°C), tránh ẩm; lắc kỹ hỗn dịch trước khi dùng.",
        "black_box_warnings": None,
        "drug_interactions": {
            "major": [],
            "moderate": [
                {
                    "drug": "Fluoroquinolones, tetracyclines, bisphosphonates, levothyroxine, sắt",
                    "mechanism": "Tạo phức hoặc thay đổi pH → giảm hấp thu đường uống",
                    "effect": "Giảm hiệu quả điều trị",
                    "management": "Dùng thuốc kia ít nhất 2 giờ trước hoặc 4 giờ sau antacid.",
                }
            ],
            "minor": [],
        },
        "contraindications_detail": {
            "tuyệt_đối": [
                "Suy thận nặng (CrCl <30 ml/phút) hoặc đang lọc máu nếu không được bác sĩ chuyên khoa chỉ định",
                "Tắc ruột hoặc liệt ruột",
            ],
            "tương_đối": [
                "Suy thận trung bình",
                "Giảm phospho máu",
                "Người già dùng kéo dài",
            ],
        },
        "pregnancy_lactation": {
            "fda_category": "B",
            "pregnancy_details": "Thường an toàn nếu dùng ngắn hạn, liều thấp cho triệu chứng ợ chua trong thai kỳ.",
            "lactation": {
                "safety": "Compatible",
                "details": "Không hấp thu đáng kể; ít vào sữa mẹ.",
                "recommendation": "Có thể dùng, tránh lạm dụng kéo dài.",
            },
        },
        "hepatic_adjustment": {
            "mild": "Không đổi",
            "moderate": "Không đổi",
            "severe": "Không đổi",
            "notes": "Không chuyển hóa qua gan; suy gan không ảnh hưởng nhiều.",
        },
        "overdose_management": {
            "symptoms": [
                "Tiêu chảy hoặc táo bón nặng",
                "Tăng magiê máu (yếu cơ, tụt huyết áp, loạn nhịp) ở suy thận",
                "Tăng nhôm máu, bệnh não (nhầm lẫn, yếu cơ) ở suy thận",
            ],
            "antidote": "Không có antidote đặc hiệu; điều trị hỗ trợ.",
            "treatment": [
                "Ngừng thuốc, bù dịch, điều chỉnh điện giải",
                "Lọc máu nếu tăng magiê/nhôm máu nặng ở suy thận",
            ],
            "monitoring": "Điện giải, magiê, phospho, chức năng thận, triệu chứng thần kinh.",
        },
        "reversal_agents": {"available": False, "agents": [], "notes": "Không có antidote đặc hiệu. Điều trị chủ yếu là hỗ trợ và điều trị triệu chứng. Ngừng thuốc ngay. Điều chỉnh điện giải nếu có tăng magiê máu hoặc hạ phospho máu."},
        "administration_instructions": {
            "oral": {
                "with_food": "Có thể dùng sau bữa ăn hoặc khi có triệu chứng; uống với nước.",
                "timing": "Dùng sau bữa ăn 1–3 giờ và/hoặc trước ngủ nếu cần; cách xa thuốc khác ≥2 giờ.",
            }
        },
        "references": {
            "primary_sources": [
                "UpToDate – Antacids: pharmacology and use",
                "Goodman & Gilman's – Antacids",
            ],
            "last_updated": "2025-02-18",
            "evidence_level": "High – lâu năm, thực hành lâm sàng rộng rãi",
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
                "ACG 2017 GERD Guidelines",
                "FDA - Over-the-counter antacids",
            ]
},

    "Calcium carbonate": {
        "group": "Gastrointestinal - Antacid (Calcium carbonate)",
        "vietnamese_name": "Calci carbonat, Tums, Rennie",
        "administration": ["PO"],
        "indications": [
            "Đau rát thượng vị, ợ chua, khó tiêu do tăng acid",
            "Bổ sung calci (khi dùng liều thấp, có chỉ định)",
        ],
        "contraindications": [
            "Tăng calci máu",
            "Sỏi thận calci, tăng calci niệu",
            "Suy thận nặng (nguy cơ tăng calci và hội chứng milk-alkali)",
        ],
        "dosage": {
            "adult_dyspepsia": "500–1000mg (1–2 viên nhai 500mg) khi có triệu chứng; có thể lặp lại sau 2 giờ, tối đa 7g/ngày nguyên tố CaCO3 cho tự điều trị ngắn hạn",
            "notes": "Nhai kỹ trước khi nuốt. Không dùng như thuốc bổ calci liều cao nếu không có chỉ định rõ ràng.",
        },
        "renal_adjustment": {
            "normal": "Không đổi, nhưng tránh lạm dụng kéo dài",
            "30_60": "Giảm liều và tránh dùng kéo dài",
            "under_30": "Tránh dùng nếu không có chỉ định chuyên khoa (nguy cơ tăng calci, milk-alkali)",
        },
        "side_effects": [
            "Táo bón",
            "Đầy hơi",
            "Tăng calci máu, hội chứng milk-alkali (kiềm chuyển hóa, suy thận, tăng calci)",
            "Sỏi thận calci (nếu dùng kéo dài liều cao)",
        ],
        "interactions": [
            "Fluoroquinolones, tetracyclines, levothyroxine, sắt, bisphosphonates: giảm hấp thu",
            "Thiazide: tăng nguy cơ tăng calci máu",
        ],,
"pregnancy": "B – thường an toàn nếu dùng ngắn hạn cho ợ chua",
        "mechanism_of_action": (
            "Calcium carbonate phản ứng với acid HCl trong dạ dày tạo thành CaCl2, CO2 và nước, "
            "làm tăng pH dạ dày, giảm hoạt tính pepsin và giảm kích ứng niêm mạc. "
            "Một phần calci được hấp thu có thể góp phần tăng calci máu nếu dùng liều cao kéo dài."
        ),
        "monitoring": [
            "Triệu chứng lâm sàng: giảm ợ chua",
            "Ở người dùng kéo dài: calci máu, creatinin nếu có yếu tố nguy cơ",
        ],
        "precautions": [
            "Tránh dùng liều cao kéo dài → nguy cơ hội chứng milk-alkali",
            "Tránh phối hợp với nhiều chế phẩm calci khác nếu không theo dõi calci máu",
            "Uống cách xa thuốc dễ tạo phức với calci (levothyroxine, fluoroquinolones, tetracyclines, sắt, bisphosphonates) ít nhất 2 giờ",
        ],
        "pharmacokinetics": {
            "half_life": "Không áp dụng (tác dụng tại chỗ, calci hấp thu có t1/2 sinh lý)",
            "onset": "Vài phút",
            "duration": "1–3 giờ",
            "protein_binding": "Không áp dụng",
            "clearance": "Calci thừa thải qua thận; phần không hấp thu thải qua phân",
        },
        "storage": "Bảo quản ở nhiệt độ phòng, tránh ẩm.",
        "black_box_warnings": None,
        "drug_interactions": {
            "major": [],
            "moderate": [
                {
                    "drug": "Thiazide diuretics",
                    "mechanism": "Giảm thải calci ở thận",
                    "effect": "Tăng nguy cơ tăng calci máu khi dùng cùng calci carbonate liều cao",
                    "management": "Theo dõi calci máu nếu phải phối hợp, hạn chế liều calci.",
                }
            ],
            "minor": [],
        },
        "contraindications_detail": {
            "tuyệt_đối": [
                "Tăng calci máu",
                "Sỏi thận calci hoạt động",
                "Suy thận nặng không được giám sát bởi chuyên khoa",
            ],
            "tương_đối": [
                "Tiền sử sỏi thận calci",
                "Dùng đồng thời nhiều nguồn calci",
            ],
        },
        "pregnancy_lactation": {
            "fda_category": "B",
            "pregnancy_details": "Dùng ngắn hạn, liều thấp cho ợ chua trong thai kỳ thường an toàn; tránh liều cao kéo dài.",
            "lactation": {
                "safety": "Compatible",
                "details": "Calci là thành phần sinh lý; nguy cơ thấp nếu liều vừa phải.",
                "recommendation": "Có thể dùng, tránh lạm dụng.",
            },
        },
        "hepatic_adjustment": {
            "mild": "Không đổi",
            "moderate": "Không đổi",
            "severe": "Không đổi",
            "notes": "Không phụ thuộc chuyển hóa gan.",
        },
        "overdose_management": {
            "symptoms": [
                "Buồn nôn, nôn",
                "Lú lẫn, yếu cơ do tăng calci máu",
                "Đa niệu, khát nước (milk-alkali)",
            ],
            "antidote": "Không có antidote đặc hiệu.",
            "treatment": [
                "Ngừng tất cả nguồn calci và vitamin D",
                "Truyền NaCl 0,9% để tăng thải calci",
                "Furosemide sau khi bù dịch (tăng thải calci) nếu cần",
            ],
            "monitoring": "Calci máu, creatinin, cân nặng, nước tiểu.",
        },
        "reversal_agents": {"available": False, "agents": [], "notes": "Không có antidote đặc hiệu. Điều trị chủ yếu là hỗ trợ và điều trị triệu chứng. Ngừng thuốc ngay. Điều chỉnh calci máu nếu tăng calci máu nặng."},
        "administration_instructions": {
            "oral": {
                "with_food": "Thường dùng khi có triệu chứng hoặc sau bữa ăn.",
                "timing": "Nhai kỹ, uống với nước; cách xa thuốc khác ≥2 giờ.",
            }
        },
        "references": {
            "primary_sources": [
                "UpToDate – Pharmacology of calcium carbonate",
                "Goodman & Gilman's – Antacid agents",
            ],
            "last_updated": "2025-02-18",
            "evidence_level": "High – extensive clinical experience",
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
                "ACG 2017 GERD Guidelines",
                "FDA - Over-the-counter antacids",
            ]
},
}

__all__ = ["ANTACIDS_DRUGS"]


