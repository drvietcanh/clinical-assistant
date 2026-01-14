"""
Standard Vaccines (Vắc xin tiêm chủng & dịch vụ)
"""

STANDARD_VACCINES = {
    "VAT (Tetanus Vaccine)":     {
        "group": "Vaccines - Tetanus (Uốn ván)",
        "vietnamese_name": "Vắc xin Uốn ván hấp phụ (VAT)",
        "brand_names": {
            "common": [
                "VAT",
                "Tetavax"
    ],
            "vietnam": [
                "VAT (IVAC)",
                "Tetavax (Pháp)"
    ],
        },
        "administration": [
            "IM (Cơ Delta)"
    ],
        "indications": [
            "Dự phòng uốn ván cho người bị thương có nguy cơ",
            "Tiêm chủng mở rộng cho phụ nữ mang thai và người lớn"
    ],
        "contraindications": {
            "absolute": [
                "Dị ứng nặng với liều tiêm trước",
                "Đang sốt cao hoặc bệnh cấp tính (hoãn tiêm)"
    ],
        },
        "dosage": {
            "wound_management": "0.5 ml IM. (Kết hợp SAT/HTIG nếu vết thương bẩn và chưa tiêm đủ liều).",
            "pregnancy": "C - Nguy cơ không thể loại trừ. Khuyến nghị trong thai kỳ""notes": "Lắc kỹ trước khi tiêm.",
        },
        "side_effects": [
            "Sưng đau tại chỗ tiêm (thường gặp)",
            "Sốt nhẹ",
            "Sốc phản vệ (hiếm)"
    ],
        "storage": "2-8 độ C. Không được đông băng.",
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
                "Dị ứng nặng với liều tiêm VAT trước đó.",
            ],
            "tương_đối": [
                "Đang sốt cao hoặc bệnh cấp tính (nên hoãn tiêm đến khi ổn định).",
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
            "30_60": "Không cần chỉnh liều; tiêm theo lịch khuyến cáo.",
            "under_30": "Không cần chỉnh liều; tiêm theo lịch khuyến cáo.",
            "dialysis": "Không cần chỉnh liều; tiêm theo lịch khuyến cáo.",
            "notes": "Vắc xin không thải trừ qua thận như thuốc; suy thận không làm thay đổi liều.",
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
            "notes": "Không có antidote đặc hiệu; xử trí phản ứng nặng bằng hỗ trợ, adrenalin, và điều trị cấp cứu.",
        },
        "administration_instructions": {
            "im": {
                "site": "Tiêm bắp cơ Delta (người lớn) hoặc mặt trước ngoài đùi (trẻ em).",
                "notes": "Lắc kỹ trước khi tiêm; luôn chuẩn bị sẵn bộ cấp cứu phản vệ.",
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
    "Verorab (Rabies Vaccine)":     {
        "group": "Vaccines - Rabies (Dại)",
        "vietnamese_name": "Vắc xin phòng Dại (Verorab, Abhayrab)",
        "brand_names": {
            "common": [
                "Verorab",
                "Abhayrab",
                "Indirab"
    ],
            "vietnam": [
                "Verorab (Pháp)",
                "Abhayrab (Ấn Độ)"
    ],
        },
        "administration": [
            "IM (Cơ Delta) - KHÔNG tiêm mông",
            "Tiêm trong da (ID)"
    ],
        "indications": [
            "Dự phòng sau phơi nhiễm (PEP) - Khi bị chó/mèo cắn/cào",
            "Dự phòng trước phơi nhiễm (PrEP) - Người nguy cơ cao (thú y)"
    ],
        "contraindications": {
            "pep_post_exposure": "KHÔNG CÓ CHỐNG CHỈ ĐỊNH TUYỆT ĐỐI VỚI ĐIỀU TRỊ DỰ PHÒNG SAU PHƠI NHIỄM (vì bệnh Dại tử vong 100%).",
            "prep_pre_exposure": "Dị ứng nặng, sốt cao (hoãn)",
        },
        "dosage": {
            "pep_im_essen": "Lịch 5 mũi (Ngày 0, 3, 7, 14, 28). 0.5 ml/lần.",
            "pep_id_thai_red_cross": "Lịch 2-2-2-0-2 (Ngày 0, 3, 7, 28). Tiêm 2 điểm 0.1 ml mỗi lần.",
            "notes": "Nếu vết thương độ III (chảy máu, niêm mạc): CẦN PHỐI HỢP HUYẾT THANH KHÁNG DẠI (SAR).",
        },
        "side_effects": [
            "Đau tại chỗ, sốt, mệt mỏi.",
            "Phản ứng phụ hiếm gặp: Hội chứng Guillain-Barre (rất hiếm)."
    ],
        "storage": "2-8 độ C. Hoàn nguyên xong dùng ngay.",
        "interactions": [],
        "pregnancy": "C - Nguy cơ không thể loại trừ. Khuyến nghị khi có chỉ định""mechanism_of_action": "",
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
                "Không có chống chỉ định tuyệt đối trong điều trị dự phòng sau phơi nhiễm (PEP) vì bệnh Dại tử vong 100%.",
            ],
            "tương_đối": [
                "Dị ứng nặng với liều tiêm trước hoặc thành phần vắc xin (cân nhắc thay loại, tiêm tại cơ sở có khả năng cấp cứu).",
                "Đang sốt cao hoặc bệnh cấp tính (có thể hoãn tiêm trong chương trình dự phòng trước phơi nhiễm - PrEP).",
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
            "30_60": "Không cần chỉnh liều; ưu tiên hoàn tất lịch tiêm PEP.",
            "under_30": "Không cần chỉnh liều; ưu tiên hoàn tất lịch tiêm PEP.",
            "dialysis": "Không cần chỉnh liều; tiêm theo phác đồ chuẩn.",
            "notes": "Vắc xin dại không cần chỉnh theo mức lọc cầu thận; lợi ích vượt trội so với nguy cơ.",
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
            "notes": "Không có antidote đặc hiệu; xử trí phản ứng nặng bằng hỗ trợ, adrenalin, và điều trị cấp cứu.",
        },
        "administration_instructions": {
            "im": {
                "site": "Tiêm bắp cơ Delta; KHÔNG tiêm mông.",
                "notes": "Tuân thủ phác đồ Essen hoặc phác đồ IM khuyến cáo.",
            },
            "id": {
                "site": "Tiêm trong da theo phác đồ Thai Red Cross.",
                "notes": "Chia liều đúng số điểm tiêm; dùng kim tiêm trong da.",
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
    "Influenza Vaccine":     {
        "group": "Vaccines - Influenza (Cúm)",
        "vietnamese_name": "Vắc xin Cúm (Vaxigrip, Influvac)",
        "brand_names": {
            "common": [
                "Vaxigrip Tetra",
                "Influvac Tetra",
                "GC Flu"
    ],
            "vietnam": [
                "Vaxigrip Tetra (Pháp)",
                "Influvac Tetra (Hà Lan)",
                "Ivacflu-S (Việt Nam)"
    ],
        },
        "administration": [
            "IM (Cơ Delta) hoặc SC sâu"
    ],
        "indications": [
            "Phòng ngừa cúm mùa (người lớn và trẻ em >6 tháng)"
    ],
        "contraindications": [
            "Dị ứng nặng với trứng gà (Ovalbumin) - thận trọng hoặc chống chỉ định tùy loại",
            "Hội chứng Guillain-Barre sau tiêm cúm trước đó (trong vòng 6 tuần)",
            "Đang sốt cao"
    ],
        "dosage": {
            "adult_child": "0.5 ml IM. Tiêm nhắc lại hàng năm.",
            "child_6m_9y_first_time": "2 mũi cách nhau 4 tuần (nếu lần đầu tiêm cúm).",
        },
        "side_effects": [
            "Đau tại chỗ, sốt nhẹ, đau cơ."
    ],
        "storage": "2-8 độ C.",
        "interactions": [],
        "pregnancy": "B - Không có bằng chứng về nguy cơ ở người. Khuyến nghị trong thai kỳ""mechanism_of_action": "",
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
                "Dị ứng nặng với thành phần vắc xin (trứng gà/ovalbumin hoặc các tá dược).",
                "Hội chứng Guillain–Barré trong vòng 6 tuần sau tiêm vắc xin cúm trước đó.",
                "Đang sốt cao hoặc bệnh cấp tính nặng (hoãn tiêm).",
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
            "30_60": "Không cần chỉnh liều; tiêm theo lịch hàng năm.",
            "under_30": "Không cần chỉnh liều; ưu tiên tiêm cho bệnh nhân nguy cơ cao.",
            "dialysis": "Không cần chỉnh liều; khuyến cáo tiêm ngừa cúm hàng năm.",
            "notes": "Vắc xin cúm không thải trừ qua thận như thuốc; suy thận không làm thay đổi liều.",
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
            "notes": "Không có antidote đặc hiệu; xử trí phản ứng nặng bằng hỗ trợ, adrenalin, và điều trị cấp cứu.",
        },
        "administration_instructions": {
            "im": {
                "site": "Tiêm bắp cơ Delta hoặc SC sâu theo hướng dẫn nhà sản xuất.",
                "notes": "Không tiêm trong da; tiêm nhắc lại hàng năm trước mùa cúm.",
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
    "Hepatitis B Vaccine":     {
        "group": "Vaccines - Hepatitis B (Viêm gan B)",
        "vietnamese_name": "Vắc xin Viêm gan B (Engerix B, Euvax B)",
        "brand_names": {
            "common": [
                "Engerix B",
                "Euvax B",
                "Heberbiovac HB"
    ],
            "vietnam": [
                "Gene-HBvax (Việt Nam)",
                "Engerix B (Bỉ)",
                "Euvax B (Hàn Quốc)"
    ],
        },
        "administration": [
            "IM (Cơ Delta - người lớn; Đùi - trẻ em)"
    ],
        "indications": [
            "Phòng ngừa viêm gan B (Sơ sinh, người lớn chưa có miễn dịch)"
    ],
        "dosage": {
            "adult": "Lịch 0-1-6 tháng (3 mũi). 1 ml (20mcg).",
            "newborn": "Tiêm trong 24h đầu sau sinh. Nếu mẹ HBsAg(+), tiêm cùng kháng huyết thanh (HBIg).",
        },
        "side_effects": [
            "Đau tại chỗ, sốt nhẹ."
    ],
        "storage": "2-8 độ C. Không để đông băng.",
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
                "Dị ứng nặng với thành phần vắc xin hoặc liều tiêm trước.",
                "Đang sốt cao hoặc bệnh cấp tính nặng (có thể hoãn tiêm).",
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
            "30_60": "Không cần chỉnh liều; tiêm theo lịch khuyến cáo.",
            "under_30": "Không cần chỉnh liều; ưu tiên tiêm ở nhóm nguy cơ cao.",
            "dialysis": "Không cần chỉnh liều; khuyến cáo tiêm cho bệnh nhân lọc máu.",
            "notes": "Vắc xin viêm gan B không yêu cầu chỉnh liều theo mức lọc cầu thận.",
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
            "notes": "Không có antidote đặc hiệu; xử trí phản ứng nặng bằng hỗ trợ, adrenalin, và điều trị cấp cứu.",
        },
        "administration_instructions": {
            "im": {
                "site": "Tiêm bắp cơ Delta (người lớn) hoặc mặt trước ngoài đùi (trẻ sơ sinh/trẻ nhỏ).",
                "notes": "Không tiêm mông; tuân thủ lịch tiêm 0–1–6 tháng hoặc theo chương trình tiêm chủng mở rộng.",
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
