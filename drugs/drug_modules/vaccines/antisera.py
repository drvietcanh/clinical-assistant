"""
Antisera & Antivenoms (Huyết thanh kháng độc & Kháng nọc rắn)
"""

ANTISERA_DRUGS = {
    "SAT (Tetanus Antitoxin)":     {
        "group": "Antisera - Tetanus (Huyết thanh kháng uốn ván)",
        "vietnamese_name": "Huyết thanh kháng độc tố uốn ván (SAT)",
        "brand_names": {
            "common": [
                "SAT"
    ],
            "vietnam": [
                "SAT (IVAC)"
    ],
        },
        "administration": [
            "IM (tiêm bắp), SC (dưới da)"
    ],
        "indications": [
            "Dự phòng uốn ván khi bị vết thương (thụ động)",
            "Điều trị bệnh uốn ván (liều cao)"
    ],
        "contraindications": [
            "Dị ứng với huyết thanh nguồn gốc ngựa (thử test trước khi tiêm là BẮT BUỘC)"
    ],
        "dosage": {
            "prophylaxis": "1500 IU (1 ống) tiêm bắp sau khi test âm tính.",
            "treatment": "Liều cao (10.000 - 20.000 IU hoặc hơn) theo phác đồ điều trị.",
            "test_dose": "Pha loãng 1/10, tiêm 0.1ml trong da. Đọc kết quả sau 15 phút. Nếu (+) -> Giải mẫn cảm Besredka.",
        },
        "side_effects": [
            "Sốc phản vệ (nguy cơ cao do nguồn gốc ngựa)",
            "Bệnh huyết thanh (Serum sickness) - sốt, đau khớp, hạch to sau 7-10 ngày"
    ],
        "storage": "2-8 độ C.",
        "interactions": [],
        "pregnancy": "",
        "mechanism_of_action": "",
        "monitoring": [],
        "precautions": [],
        "pharmacokinetics": {
        },
        "black_box_warnings": None,
        "drug_interactions": {
            "major": [],
            "moderate": [],
            "minor": [],
        },
        "contraindications_detail": {
            "tuyệt_đối": [
                "Dị ứng nặng với huyết thanh nguồn gốc ngựa (sau khi đã test và/hoặc giải mẫn cảm thất bại).",
            ],
            "tương_đối": [
                "Tiền sử bệnh huyết thanh nặng với SAT hoặc các huyết thanh nguồn gốc ngựa khác.",
            ],
        },
        "pregnancy_lactation": {
            "fda_category": "",
            "pregnancy_details": "",
            "lactation": {
                "safety": "",
                "details": "",
                "recommendation": "",
            },
        },
        "hepatic_adjustment": {
            "mild": "",
            "moderate": "",
            "severe": "",
            "notes": "",
        },
        "renal_adjustment": {
            "normal": "Không cần chỉnh liều.",
            "30_60": "Không cần chỉnh liều; theo dõi sát phản vệ và bệnh huyết thanh.",
            "under_30": "Không cần chỉnh liều; ưu tiên điều trị uốn ván, theo dõi sát.",
            "dialysis": "Không cần chỉnh liều; dùng theo phác đồ, theo dõi sát.",
            "notes": "Huyết thanh kháng độc được dùng theo IU cố định; không chỉnh theo chức năng thận.",
        },
        "overdose_management": {
            "symptoms": [],
            "antidote": "",
            "treatment": [],
            "monitoring": "",
        },
        "reversal_agents": {
            "available": False,
            "agents": [],
            "notes": "Không có antidote đặc hiệu; xử trí biến chứng bằng adrenalin, dịch truyền, corticosteroid, và hỗ trợ hô hấp.",
        },
        "administration_instructions": {
            "im_sc": {
                "site": "Tiêm bắp (IM) hoặc dưới da (SC) theo phác đồ.",
                "notes": "BẮT BUỘC test trong da trước khi tiêm; chuẩn bị sẵn bộ cấp cứu phản vệ.",
            },
        },
        "references": {
            "primary_sources": [],
            "last_updated": "",
            "evidence_level": "",
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
    "SAR (Rabies Antiserum)":     {
        "group": "Antisera - Rabies (Huyết thanh kháng dại)",
        "vietnamese_name": "Huyết thanh kháng dại (SAR)",
        "brand_names": {
            "common": [
                "Favirab",
                "SAR"
    ],
            "vietnam": [
                "SAR (IVAC) - gốc ngựa",
                "Favirab (Pháp) - gốc ngựa",
                "HBIg (người) - hiếm"
    ],
        },
        "administration": [
            "Tiêm thấm nhiễm quanh vết thương (càng nhiều càng tốt) + IM phần còn lại"
    ],
        "indications": [
            "Dự phòng bệnh dại sau phơi nhiễm độ III (vết thương chảy máu, niêm mạc, đầu mặt cổ)"
    ],
        "dosage": {
            "equine_sar": "40 IU/kg (SAR, Favirab). Thử test trước tiêm.",
            "human_hbig": "20 IU/kg (Ít gây dị ứng, không cần test, nhưng đắt/hiếm).",
            "notes": "Tiêm càng sớm càng tốt (ngày 0). Thấm nhiễm tối đa vào vết thương.",
        },
        "side_effects": [
            "Sốc phản vệ (gốc ngựa). Bệnh huyết thanh."
    ],
        "storage": "2-8 độ C.",
        "contraindications": [],
        "interactions": [],
        "pregnancy": "",
        "mechanism_of_action": "",
        "monitoring": [],
        "precautions": [],
        "pharmacokinetics": {
        },
        "black_box_warnings": None,
        "drug_interactions": {
            "major": [],
            "moderate": [],
            "minor": [],
        },
        "contraindications_detail": {
            "tuyệt_đối": [],
            "tương_đối": [
                "Tiền sử phản vệ nặng với huyết thanh kháng dại nguồn gốc ngựa (SAR/Favirab).",
            ],
        },
        "pregnancy_lactation": {
            "fda_category": "",
            "pregnancy_details": "",
            "lactation": {
                "safety": "",
                "details": "",
                "recommendation": "",
            },
        },
        "hepatic_adjustment": {
            "mild": "",
            "moderate": "",
            "severe": "",
            "notes": "",
        },
        "renal_adjustment": {
            "normal": "Không cần chỉnh liều.",
            "30_60": "Không cần chỉnh liều; tiêm đủ liều theo cân nặng (IU/kg).",
            "under_30": "Không cần chỉnh liều; ưu tiên điều trị dại, theo dõi sát phản vệ và chức năng thận.",
            "dialysis": "Không cần chỉnh liều; dùng theo phác đồ chuẩn.",
            "notes": "Huyết thanh kháng dại dùng liều theo IU/kg, không chỉnh theo mức lọc cầu thận.",
        },
        "overdose_management": {
            "symptoms": [],
            "antidote": "",
            "treatment": [],
            "monitoring": "",
        },
        "reversal_agents": {
            "available": False,
            "agents": [],
            "notes": "Không có antidote đặc hiệu; xử trí biến chứng bằng adrenalin, dịch truyền, corticosteroid, và hỗ trợ hô hấp.",
        },
        "administration_instructions": {
            "local_im": {
                "with_food": "",
                "timing": "Tiêm thấm nhiễm tối đa quanh vết thương; phần còn lại tiêm bắp xa vị trí vắc xin.",
            },
        },
        "references": {
            "primary_sources": [],
            "last_updated": "",
            "evidence_level": "",
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
    "Snake Antivenom (Luc Tre)":     {
        "group": "Antivenom - Snake (Kháng nọc rắn)",
        "vietnamese_name": "Huyết thanh kháng nọc rắn Lục Tre",
        "brand_names": {
            "vietnam": [
                "SAV Lục Tre (IVAC)"
    ],
        },
        "administration": [
            "IV chậm hoặc truyền tĩnh mạch (pha loãng)"
    ],
        "indications": [
            "Rắn Lục Tre cắn có rối loạn đông máu nặng hoặc triệu chứng toàn thân"
    ],
        "dosage": {
            "initial": "10-20 lọ (tùy tình trạng, theo phác đồ BV Chợ Rẫy/Bạch Mai).",
            "notes": "Cần thử test trước (bắt buộc). Theo dõi sát phản vệ.",
        },
        "side_effects": [
            "Sốc phản vệ (tỷ lệ cao)."
    ],
        "storage": "2-8 độ C.",
        "contraindications": [],
        "interactions": [],
        "pregnancy": "",
        "mechanism_of_action": "",
        "monitoring": [],
        "precautions": [],
        "pharmacokinetics": {
        },
        "black_box_warnings": None,
        "drug_interactions": {
            "major": [],
            "moderate": [],
            "minor": [],
        },
        "contraindications_detail": {
            "tuyệt_đối": [],
            "tương_đối": [
                "Tiền sử phản vệ nặng với huyết thanh kháng nọc rắn Lục Tre hoặc thành phần chế phẩm.",
            ],
        },
        "pregnancy_lactation": {
            "fda_category": "",
            "pregnancy_details": "",
            "lactation": {
                "safety": "",
                "details": "",
                "recommendation": "",
            },
        },
        "hepatic_adjustment": {
            "mild": "",
            "moderate": "",
            "severe": "",
            "notes": "",
        },
        "renal_adjustment": {
            "normal": "Không cần chỉnh liều.",
            "30_60": "Không cần chỉnh liều; ưu tiên điều trị rối loạn đông máu do nọc rắn.",
            "under_30": "Không cần chỉnh liều; theo dõi sát chức năng thận và đông máu.",
            "dialysis": "Không cần chỉnh liều; xử trí theo phác đồ hồi sức nhiễm độc.",
            "notes": "Liều huyết thanh kháng nọc rắn dựa trên mức độ nhiễm độc, không dựa trên chức năng thận.",
        },
        "overdose_management": {
            "symptoms": [],
            "antidote": "",
            "treatment": [],
            "monitoring": "",
        },
        "reversal_agents": {
            "available": False,
            "agents": [],
            "notes": "Không có antidote đặc hiệu; xử trí biến chứng bằng adrenalin, dịch truyền, corticosteroid, và hỗ trợ hô hấp.",
        },
        "administration_instructions": {
            "iv": {
                "reconstitution": "Pha loãng theo hướng dẫn nhà sản xuất; truyền chậm, theo dõi sát dấu hiệu sinh tồn.",
                "infusion_rate": "Truyền tĩnh mạch chậm; ngừng ngay nếu có dấu hiệu phản vệ.",
            },
        },
        "references": {
            "primary_sources": [],
            "last_updated": "",
            "evidence_level": "",
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
    "Snake Antivenom (Ho Dat)":     {
        "group": "Antivenom - Snake (Kháng nọc rắn)",
        "vietnamese_name": "Huyết thanh kháng nọc rắn Hổ Đất",
        "brand_names": {
            "vietnam": [
                "SAV Hổ Đất (IVAC)"
    ],
        },
        "administration": [
            "IV chậm/Truyền TM"
    ],
        "indications": [
            "Rắn Hổ Đất cắn có liệt cơ/suy hô hấp"
    ],
        "dosage": {
            "initial": "Liều cao, đánh giá đáp ứng lâm sàng (cải thiện liệt, mở mắt).",
            "notes": "Thử test trước. Chuẩn bị sẵn Adrenalin.",
        },
        "storage": "2-8 độ C.",
        "side_effects": [],
        "contraindications": [],
        "interactions": [],
        "pregnancy": "",
        "mechanism_of_action": "",
        "monitoring": [],
        "precautions": [],
        "pharmacokinetics": {
        },
        "black_box_warnings": None,
        "drug_interactions": {
            "major": [],
            "moderate": [],
            "minor": [],
        },
        "contraindications_detail": {
            "tuyệt_đối": [],
            "tương_đối": [
                "Tiền sử phản vệ nặng với huyết thanh kháng nọc rắn Hổ Đất hoặc thành phần chế phẩm.",
            ],
        },
        "pregnancy_lactation": {
            "fda_category": "",
            "pregnancy_details": "",
            "lactation": {
                "safety": "",
                "details": "",
                "recommendation": "",
            },
        },
        "hepatic_adjustment": {
            "mild": "",
            "moderate": "",
            "severe": "",
            "notes": "",
        },
        "renal_adjustment": {
            "normal": "Không cần chỉnh liều.",
            "30_60": "Không cần chỉnh liều; ưu tiên điều trị suy hô hấp/liệt do nọc rắn.",
            "under_30": "Không cần chỉnh liều; theo dõi sát chức năng thận.",
            "dialysis": "Không cần chỉnh liều; xử trí theo phác đồ hồi sức nhiễm độc.",
            "notes": "Liều huyết thanh kháng nọc rắn dựa trên mức độ nhiễm độc, không dựa trên chức năng thận.",
        },
        "overdose_management": {
            "symptoms": [],
            "antidote": "",
            "treatment": [],
            "monitoring": "",
        },
        "reversal_agents": {
            "available": False,
            "agents": [],
            "notes": "Không có antidote đặc hiệu; xử trí biến chứng bằng adrenalin, dịch truyền, corticosteroid, và hỗ trợ hô hấp.",
        },
        "administration_instructions": {
            "iv": {
                "reconstitution": "Pha loãng theo hướng dẫn nhà sản xuất; truyền chậm, theo dõi sát dấu hiệu sinh tồn.",
                "infusion_rate": "Truyền tĩnh mạch chậm; ngừng ngay nếu có dấu hiệu phản vệ.",
            },
        },
        "references": {
            "primary_sources": [],
            "last_updated": "",
            "evidence_level": "",
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
}
