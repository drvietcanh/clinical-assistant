"""Gastrointestinal Drugs - Antiflatulents / Anti-gas
Simethicone"""

ANTIFLATULENTS_DRUGS = {
    "Simethicone": {
        "group": "Gastrointestinal - Antiflatulent (Chống đầy hơi, chống sủi bọt)",
        "vietnamese_name": "Simethicone, Dimethicone, thuốc chống đầy hơi",
        "administration": ["PO"],
        "indications": [
            "Đầy hơi, chướng bụng, khó chịu do tích tụ khí trong dạ dày–ruột",
            "Hỗ trợ chuẩn bị siêu âm, nội soi (giảm bọt khí trong đường tiêu hóa)",
            "Đầy hơi, đau bụng do khí ở trẻ em (dạng giọt uống, tùy sản phẩm)",
        ],
        "contraindications": [
            "Dị ứng với simethicone hoặc tá dược",
            "Tắc ruột cơ học (cần loại trừ khi có triệu chứng bụng cấp)",
        ],
        "dosage": {
            "adult_dyspepsia": "40–125mg PO sau bữa ăn và trước khi đi ngủ, tối đa ~500mg/ngày (tùy chế phẩm)",
            "pediatric": "20–40mg sau bữa ăn và trước ngủ (tùy tuổi và sản phẩm, tham khảo hướng dẫn cụ thể)",
            "notes": "Có nhiều dạng bào chế (viên nhai, giọt uống, hỗn dịch). Dùng ngắn hạn khi có triệu chứng.",
        },
        "renal_adjustment": {
            "normal": "Không cần chỉnh liều",
            "30_60": "Không cần chỉnh liều",
            "under_30": "Không cần chỉnh liều (không hấp thu đáng kể)",
        },
        "side_effects": [
            "Rất hiếm, thường dung nạp tốt",
            "Buồn nôn nhẹ hoặc táo bón (hiếm)",
            "Phản ứng dị ứng da rất hiếm",
        ],
        "interactions": [
            "Ít hoặc không có tương tác thuốc có ý nghĩa; về lý thuyết có thể ảnh hưởng nhẹ hấp thu thuốc tan trong bọt khí, nhưng không đáng kể lâm sàng.",
        ],
        "pregnancy": "C nhưng thường được xem là an toàn do không hấp thu đáng kể",
        "mechanism_of_action": (
            "Simethicone là polymer silicone trơ, có tác dụng giảm sức căng bề mặt của các bọt khí trong đường tiêu hóa, "
            "làm vỡ bọt khí lớn thành các bóng khí nhỏ hơn dễ di chuyển và được tống ra ngoài qua ợ hơi hoặc trung tiện. "
            "Không hấp thu toàn thân và không tham gia phản ứng hóa học trong cơ thể."
        ),
        "monitoring": [
            "Triệu chứng đầy hơi, chướng bụng, đau bụng giảm dần",
            "Nếu đau bụng nặng, sốt, nôn, không trung tiện/đi ngoài được: cần đánh giá nguyên nhân khác (tắc ruột, viêm ruột...)",
        ],
        "precautions": [
            "Chỉ dùng điều trị triệu chứng. Nếu triệu chứng kéo dài hoặc nặng dần, cần đánh giá nguyên nhân thực thể (loét, tắc ruột, IBS...).",
            "Không thay thế cho đánh giá nội soi/sinh thiết khi có dấu hiệu báo động (sụt cân, thiếu máu, nôn ói kéo dài, phân đen...).",
        ],
        "pharmacokinetics": {
            "half_life": "Không áp dụng (không hấp thu)",
            "onset": "Vài phút đến <1 giờ sau uống",
            "duration": "Vài giờ tùy liều và chế độ ăn",
            "protein_binding": "Không áp dụng",
            "clearance": "Thải nguyên dạng qua phân",
        },
        "storage": "Bảo quản nơi khô mát, tránh nhiệt độ cao; lắc đều hỗn dịch trước dùng.",
        "black_box_warnings": None,
        "drug_interactions": {
            "major": [],
            "moderate": [],
            "minor": [],
        },
        "contraindications_detail": {
            "tuyệt_đối": [
                "Dị ứng với simethicone hoặc bất kỳ tá dược nào trong chế phẩm",
            ],
            "tương_đối": [
                "Bụng cấp chưa rõ nguyên nhân (đau dữ dội, sốt, nôn liên tục, bí trung đại tiện)",
            ],
        },
        "pregnancy_lactation": {
            "fda_category": "C",
            "pregnancy_details": "Không hấp thu đáng kể; đa số tài liệu coi là an toàn khi dùng ngắn hạn cho triệu chứng đầy hơi.",
            "lactation": {
                "safety": "Compatible",
                "details": "Không hấp thu → không vào sữa hoặc ở mức rất thấp.",
                "recommendation": "Có thể dùng khi cho con bú.",
            },
        },
        "hepatic_adjustment": {
            "mild": "Không cần chỉnh liều",
            "moderate": "Không cần chỉnh liều",
            "severe": "Không cần chỉnh liều",
            "notes": "Không chuyển hóa qua gan.",
        },
        "overdose_management": {
            "symptoms": [
                "Không có hội chứng quá liều đặc hiệu được ghi nhận; nói chung rất an toàn",
            ],
            "antidote": "Không có; điều trị hỗ trợ nếu cần.",
            "treatment": [
                "Ngừng thuốc, theo dõi triệu chứng",
            ],
            "monitoring": "Triệu chứng tiêu hóa và lâm sàng chung.",
        },
        "reversal_agents": {"available": False, "agents": [], "notes": "Không có antidote đặc hiệu. Điều trị chủ yếu là hỗ trợ và điều trị triệu chứng. Ngừng thuốc ngay nếu có phản ứng dị ứng nghiêm trọng."},
        "administration_instructions": {
            "oral": {
                "with_food": "Thường dùng sau bữa ăn và trước khi đi ngủ.",
                "timing": "2–4 lần/ngày tùy nhu cầu; có thể nhai kỹ viên nhai hoặc lắc đều giọt/hỗn dịch trước khi dùng.",
            }
        },
        "references": {
            "primary_sources": [
                "UpToDate – Simethicone: Drug information",
                "Goodman & Gilman – Antiflatulent agents",
            ],
            "last_updated": "2025-02-23",
            "evidence_level": "High – thuốc không kê đơn, kinh nghiệm lâm sàng rộng rãi",
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
                "FDA Drug Information",
                "UpToDate Drug Information",
            ]
},
}

__all__ = ["ANTIFLATULENTS_DRUGS"]


