"""Diabetes Medications
Active module - contains all diabetes drug data"""

# DPP-4 Inhibitors

DPP_4_INHIBITORS_DRUGS = {
    "Alogliptin": {
        "group": "Diabetes - DPP-4 Inhibitor",
        "vietnamese_name": "Alogliptin, Nesina",
        "administration": ["PO"],
        "indications": [
            "Đái tháo đường type 2",
            "Kết hợp với metformin hoặc sulfonylurea"
        ],
        "contraindications": [
            "Đái tháo đường type 1",
            "Nhiễm toan ceton",
            "Dị ứng alogliptin"
        ],
        "dosage": {
            "adult_normal_renal": "25mg x 1 lần/ngày",
            "adult_moderate_renal": "12.5mg x 1 lần/ngày (CrCl 30-60)",
            "adult_severe_renal": "6.25mg x 1 lần/ngày (CrCl <30)",
            "dm_t2": "25mg x 1 lần/ngày (CrCl >60), 12.5mg x 1 lần/ngày (CrCl 30-60), 6.25mg x 1 lần/ngày (CrCl <30)",
            "adult_start": "25mg x 1 lần/ngày (CrCl >60)",
            "adult_usual": "25mg x 1 lần/ngày (CrCl >60)",
            "adult_max": "25mg/ngày",
            "elderly": "Không cần điều chỉnh liều đặc biệt, nhưng điều chỉnh theo CrCl.",
            "renal_adjustment_dosage": {
                "normal": "25mg x 1 lần/ngày (CrCl >60)",
                "30_60": "12.5mg x 1 lần/ngày (CrCl 30-60)",
                "under_30": "6.25mg x 1 lần/ngày (CrCl <30)",
                "dialysis": "6.25mg x 1 lần/ngày"
            },
            "administration_route": "PO",
            "frequency": "1 lần/ngày",
            "with_food": "Có thể uống bất kỳ lúc nào, không cần thức ăn",
            "notes": "Uống bất kỳ lúc nào. Cần điều chỉnh liều ở suy thận. Ít gây hạ đường huyết. Thải trừ chủ yếu qua thận."
        },
        "renal_adjustment": {
            "normal": "25mg/ngày",
            "30_60": "12.5mg/ngày (CrCl 30-60)",
            "under_30": "6.25mg/ngày (CrCl <30)"
        },
        "side_effects": [
            "Nhức đầu",
            "Nhiễm trùng đường hô hấp trên",
            "Viêm tụy cấp (hiếm nhưng nguy hiểm)",
            "Đau khớp nghiêm trọng (hiếm)",
            "Suy tim (tăng nhẹ nguy cơ)"
        ],
        "interactions": [
            "Insulin/Sulfonylurea: có thể tăng nguy cơ hạ đường huyết",
            "Digoxin: tăng nhẹ nồng độ digoxin"
        ],
        "pregnancy": "B",
        "mechanism_of_action": "Alogliptin là chất ức chế chọn lọc dipeptidyl peptidase-4 (DPP-4), enzyme chịu trách nhiệm phân hủy incretin hormones (GLP-1 và GIP). Bằng cách ức chế DPP-4, alogliptin làm tăng nồng độ GLP-1 và GIP, các hormone được tiết ra từ ruột non sau khi ăn. GLP-1 và GIP kích thích tiết insulin từ tế bào beta tuyến tụy phụ thuộc vào glucose (chỉ tiết khi đường huyết cao), đồng thời ức chế tiết glucagon từ tế bào alpha tuyến tụy. Điều này dẫn đến giảm đường huyết sau ăn và giảm sản xuất glucose từ gan. Cơ chế này phụ thuộc vào glucose nên ít gây hạ đường huyết so với sulfonylurea. Alogliptin được bài tiết chủ yếu qua thận, nên cần điều chỉnh liều ở suy thận.",
        "monitoring": [
            "Đường huyết (HbA1c, glucose máu) - đánh giá hiệu quả giảm đường huyết",
            "Chức năng thận (creatinine, CrCl) - cần điều chỉnh liều: CrCl 30-60 → 12.5mg/ngày, CrCl <30 → 6.25mg/ngày",
            "Triệu chứng viêm tụy cấp (đau bụng nặng, buồn nôn, nôn) - hiếm nhưng nguy hiểm",
            "Đau khớp nghiêm trọng - hiếm, cần ngừng thuốc nếu xảy ra",
            "Triệu chứng suy tim (khó thở, phù) - tăng nhẹ nguy cơ suy tim",
            "Dấu hiệu phản ứng dị ứng (phát ban, phù mạch) - hiếm",
            "Tác dụng phụ (nhức đầu, nhiễm trùng đường hô hấp trên)"
        ],
        "precautions": [
            "Không dùng cho đái tháo đường type 1 (không hiệu quả)",
            "Cần điều chỉnh liều ở suy thận: CrCl 30-60 → 12.5mg/ngày, CrCl <30 → 6.25mg/ngày",
            "Nguy cơ viêm tụy cấp - hiếm nhưng nguy hiểm, ngừng ngay nếu có đau bụng nặng",
            "Nguy cơ đau khớp nghiêm trọng - hiếm, ngừng thuốc nếu xảy ra",
            "Tăng nhẹ nguy cơ suy tim - thận trọng ở bệnh nhân có tiền sử suy tim",
            "Tăng nguy cơ hạ đường huyết khi dùng với insulin hoặc sulfonylurea",
            "Ít gây hạ đường huyết khi dùng đơn độc (do cơ chế phụ thuộc glucose)",
            "Có thể dùng bất kỳ lúc nào, không cần ăn",
            "An toàn trong thai kỳ (category B)",
            "Tương tác nhẹ với digoxin - có thể tăng nồng độ digoxin"
        ],
        "pharmacokinetics": {
            "half_life": "21 giờ",
            "onset": "1-2 giờ",
            "duration": "24 giờ",
            "protein_binding": "20%",
            "clearance": "Thận: bài tiết chủ yếu qua thận (60-70% nguyên dạng, không chuyển hóa). Gan: ít chuyển hóa. Cần điều chỉnh liều ở suy thận."
        },
        "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm, tránh ánh sáng",
        "black_box_warnings": None,
        "drug_interactions": {
            "major": [],
            "moderate": [
                {
                    "drug": "Digoxin",
                    "mechanism": "Alogliptin có thể tăng nhẹ nồng độ digoxin",
                    "effect": "Tăng nồng độ digoxin, tăng nguy cơ độc tính",
                    "management": "Theo dõi nồng độ digoxin và dấu hiệu độc tính."
                },
                {
                    "drug": "Insulin, Sulfonylureas",
                    "mechanism": "Tác dụng cộng dồn giảm đường huyết",
                    "effect": "Tăng nguy cơ hạ đường huyết",
                    "management": "Theo dõi đường huyết chặt chẽ. Có thể cần giảm liều insulin hoặc sulfonylurea."
                }
            ],
            "minor": []
        },
        "contraindications": {
            "tuyệt_đối": [
                "Đái tháo đường type 1",
                "Nhiễm toan ceton do đái tháo đường",
                "Dị ứng alogliptin hoặc DPP-4 inhibitor"
            ],
            "tương_đối": [
                "Suy thận - cần điều chỉnh liều (CrCl 30-60 → 12.5mg/ngày, CrCl <30 → 6.25mg/ngày)",
                "Suy gan - thận trọng",
                "Có thai - category B, an toàn"
            ]
        },
        "pregnancy_lactation": {
            "fda_category": "B",
            "pregnancy_details": "An toàn trong thai kỳ. Alogliptin là category B. Không có bằng chứng về dị tật thai nhi. Có thể dùng nếu lợi ích > nguy cơ.",
            "lactation": {
                "safety": "Compatible",
                "details": "Alogliptin bài tiết vào sữa mẹ ở nồng độ thấp. Ít có nguy cơ gây tác dụng phụ ở trẻ bú mẹ.",
                "recommendation": "Có thể dùng khi cho con bú với theo dõi chặt chẽ."
            }
        },
        "hepatic_adjustment": {
            "mild": "Không cần điều chỉnh liều. Alogliptin chuyển hóa ít qua gan.",
            "moderate": "Không cần điều chỉnh liều thường quy. Theo dõi đáp ứng điều trị.",
            "severe": "Thận trọng, có thể cần giảm liều. Theo dõi đáp ứng điều trị và độc tính.",
            "notes": "Alogliptin chuyển hóa ít qua gan, chủ yếu bài tiết qua thận. Suy gan thường không ảnh hưởng đáng kể đến nồng độ."
        },
        "overdose_management": {
            "symptoms": [
                "Hạ đường huyết (nếu dùng với insulin hoặc sulfonylurea)",
                "Nhức đầu",
                "Buồn nôn"
            ],
            "antidote": "Glucose (nếu hạ đường huyết)",
            "treatment": [
                "Ngừng alogliptin nếu cần",
                "Điều trị hạ đường huyết nếu có (glucose)",
                "Theo dõi tại bệnh viện nếu cần"
            ],
            "monitoring": "Đường huyết, dấu hiệu sinh tồn"
        },
        "reversal_agents": {
            "available": False,
            "agents": []
        },
        "administration_instructions": {
            "oral": {
                "with_food": "Có thể uống với hoặc không thức ăn. Uống bất kỳ lúc nào trong ngày.",
                "timing": "Uống 1 lần/ngày, bất kỳ lúc nào. Nên uống vào cùng một thời điểm mỗi ngày để dễ nhớ."
            }
        },
        "references": {
            "primary_sources": [
                "FDA Drug Label - Alogliptin (Nesina)",
                "UpToDate - Alogliptin: Drug Information",
                "EXAMINE Study - New England Journal of Medicine",
                "Goodman & Gilman's The Pharmacological Basis of Therapeutics"
            ],
            "last_updated": "2025-02-05",
            "evidence_level": "High - FDA approved, multiple RCTs (EXAMINE)"
        },
        "risk_flags": {
            "high_alert": False,
            "narrow_therapeutic_index": False,
            "bleeding_risk": False,
            "organ_toxicity": ["Pancreatitis (rare)", "Heart failure (slight increased risk)"],
            "qt_prolongation": False,
            "hepatotoxicity": False,
            "nephrotoxicity": False,
            "requires_monitoring": ["Blood glucose", "Renal function (CrCl for dose adjustment)", "Signs of pancreatitis", "Signs of heart failure"]
        },
        "guideline_tags": [
            "ADA Diabetes Guidelines",
            "AACE/ACE Diabetes Guidelines",
            "EXAMINE Study",
            "FDA Drug Safety Communication - DPP-4 Inhibitors and Heart Failure"
        ],
        "black_box_warnings": None,
},
    "Linagliptin": {
        "group": "Diabetes - DPP-4 Inhibitor",
        "vietnamese_name": "Linagliptin, Trajenta",
        "administration": ["PO"],
        "indications": [
            "Đái tháo đường type 2",
            "Kết hợp với metformin hoặc sulfonylurea"
        ],
        "contraindications": [
            "Đái tháo đường type 1",
            "Nhiễm toan ceton",
            "Dị ứng linagliptin"
        ],
        "dosage": {
            "adult_standard": "5mg x 1 lần/ngày",
            "adult_renal_impairment": "5mg x 1 lần/ngày (không cần điều chỉnh liều)",
            "dm_t2": "5mg x 1 lần/ngày (không cần điều chỉnh liều ở suy thận)",
            "adult_start": "5mg x 1 lần/ngày",
            "adult_usual": "5mg x 1 lần/ngày",
            "adult_max": "5mg/ngày",
            "elderly": "Không cần điều chỉnh liều đặc biệt.",
            "renal_adjustment_dosage": {
                "normal": "5mg x 1 lần/ngày",
                "30_60": "5mg x 1 lần/ngày (không cần điều chỉnh)",
                "under_30": "5mg x 1 lần/ngày (không cần điều chỉnh)",
                "dialysis": "5mg x 1 lần/ngày (không cần điều chỉnh)"
            },
            "administration_route": "PO",
            "frequency": "1 lần/ngày",
            "with_food": "Có thể uống bất kỳ lúc nào, không cần thức ăn",
            "notes": "Uống bất kỳ lúc nào. Không cần điều chỉnh liều ở suy thận (khác với các DPP-4 inhibitors khác). Ít gây hạ đường huyết. Thải trừ chủ yếu qua gan."
        },
        "renal_adjustment": {
            "normal": "5mg/ngày",
            "30_60": "5mg/ngày (không cần điều chỉnh)",
            "under_30": "5mg/ngày (không cần điều chỉnh)"
        },
        "side_effects": [
            "Nhức đầu",
            "Nhiễm trùng đường hô hấp trên",
            "Viêm tụy cấp (hiếm nhưng nguy hiểm)",
            "Đau khớp nghiêm trọng (hiếm)",
            "Suy tim (tăng nhẹ nguy cơ)"
        ],
        "interactions": [
            "Insulin/Sulfonylurea: có thể tăng nguy cơ hạ đường huyết",
            "Rifampin: giảm nồng độ linagliptin"
        ],
        "pregnancy": "B",
        "mechanism_of_action": "Linagliptin là chất ức chế chọn lọc dipeptidyl peptidase-4 (DPP-4), enzyme chịu trách nhiệm phân hủy incretin hormones (GLP-1 và GIP). Bằng cách ức chế DPP-4, linagliptin làm tăng nồng độ GLP-1 và GIP, các hormone được tiết ra từ ruột non sau khi ăn. GLP-1 và GIP kích thích tiết insulin từ tế bào beta tuyến tụy phụ thuộc vào glucose (chỉ tiết khi đường huyết cao), đồng thời ức chế tiết glucagon từ tế bào alpha tuyến tụy. Điều này dẫn đến giảm đường huyết sau ăn và giảm sản xuất glucose từ gan. Cơ chế này phụ thuộc vào glucose nên ít gây hạ đường huyết so với sulfonylurea. Linagliptin được chuyển hóa chủ yếu qua gan và bài tiết qua mật, nên không cần điều chỉnh liều ở suy thận (khác với sitagliptin, vildagliptin).",
        "monitoring": [
            "Đường huyết (HbA1c, glucose máu) - đánh giá hiệu quả giảm đường huyết",
            "Triệu chứng viêm tụy cấp (đau bụng nặng, buồn nôn, nôn) - hiếm nhưng nguy hiểm",
            "Đau khớp nghiêm trọng - hiếm, cần ngừng thuốc nếu xảy ra",
            "Triệu chứng suy tim (khó thở, phù) - tăng nhẹ nguy cơ suy tim",
            "Dấu hiệu phản ứng dị ứng (phát ban, phù mạch) - hiếm",
            "Tác dụng phụ (nhức đầu, nhiễm trùng đường hô hấp trên)"
        ],
        "precautions": [
            "Không dùng cho đái tháo đường type 1 (không hiệu quả)",
            "KHÔNG CẦN điều chỉnh liều ở suy thận (khác với các DPP-4 inhibitors khác) - ưu điểm",
            "Nguy cơ viêm tụy cấp - hiếm nhưng nguy hiểm, ngừng ngay nếu có đau bụng nặng",
            "Nguy cơ đau khớp nghiêm trọng - hiếm, ngừng thuốc nếu xảy ra",
            "Tăng nhẹ nguy cơ suy tim - thận trọng ở bệnh nhân có tiền sử suy tim",
            "Tăng nguy cơ hạ đường huyết khi dùng với insulin hoặc sulfonylurea",
            "Ít gây hạ đường huyết khi dùng đơn độc (do cơ chế phụ thuộc glucose)",
            "Có thể dùng bất kỳ lúc nào, không cần ăn",
            "An toàn trong thai kỳ (category B)",
            "Tương tác với rifampin - có thể giảm nồng độ linagliptin"
        ],
        "pharmacokinetics": {
            "half_life": "12 giờ",
            "onset": "1-2 giờ",
            "duration": "24 giờ",
            "protein_binding": "70-80%",
            "clearance": "Gan: chuyển hóa chủ yếu qua gan (CYP3A4), bài tiết qua mật. Thận: bài tiết một phần. Không cần điều chỉnh liều ở suy thận (khác với sitagliptin, vildagliptin)."
        },
        "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm, tránh ánh sáng",
        "black_box_warnings": None,
        "drug_interactions": {
            "major": [],
            "moderate": [
                {
                    "drug": "Rifampin",
                    "mechanism": "Cảm ứng CYP3A4, tăng chuyển hóa linagliptin",
                    "effect": "Giảm nồng độ linagliptin, giảm hiệu quả",
                    "management": "Có thể cần tăng liều linagliptin. Theo dõi đường huyết."
                },
                {
                    "drug": "Insulin, Sulfonylureas",
                    "mechanism": "Tác dụng cộng dồn giảm đường huyết",
                    "effect": "Tăng nguy cơ hạ đường huyết",
                    "management": "Theo dõi đường huyết chặt chẽ. Có thể cần giảm liều insulin hoặc sulfonylurea."
                }
            ],
            "minor": []
        },
        "contraindications": {
            "tuyệt_đối": [
                "Đái tháo đường type 1",
                "Nhiễm toan ceton do đái tháo đường",
                "Dị ứng linagliptin hoặc DPP-4 inhibitor"
            ],
            "tương_đối": [
                "Suy thận - không cần điều chỉnh liều (ưu điểm)",
                "Suy gan - thận trọng",
                "Có thai - category B, an toàn"
            ]
        },
        "pregnancy_lactation": {
            "fda_category": "B",
            "pregnancy_details": "An toàn trong thai kỳ. Linagliptin là category B. Không có bằng chứng về dị tật thai nhi. Có thể dùng nếu lợi ích > nguy cơ.",
            "lactation": {
                "safety": "Compatible",
                "details": "Linagliptin bài tiết vào sữa mẹ ở nồng độ thấp. Ít có nguy cơ gây tác dụng phụ ở trẻ bú mẹ.",
                "recommendation": "Có thể dùng khi cho con bú với theo dõi chặt chẽ."
            }
        },
        "hepatic_adjustment": {
            "mild": "Không cần điều chỉnh liều. Linagliptin chuyển hóa qua gan nhưng có thể dùng ở suy gan nhẹ.",
            "moderate": "Thận trọng, có thể cần giảm liều. Theo dõi đáp ứng điều trị.",
            "severe": "Thận trọng, có thể cần giảm liều. Theo dõi đáp ứng điều trị và độc tính.",
            "notes": "Linagliptin chuyển hóa chủ yếu qua gan (CYP3A4). Suy gan có thể làm giảm chuyển hóa, tăng nồng độ. Thận trọng ở suy gan nặng."
        },
        "overdose_management": {
            "symptoms": [
                "Hạ đường huyết (nếu dùng với insulin hoặc sulfonylurea)",
                "Nhức đầu",
                "Buồn nôn"
            ],
            "antidote": "Glucose (nếu hạ đường huyết)",
            "treatment": [
                "Ngừng linagliptin nếu cần",
                "Điều trị hạ đường huyết nếu có (glucose)",
                "Theo dõi tại bệnh viện nếu cần"
            ],
            "monitoring": "Đường huyết, dấu hiệu sinh tồn"
        },
        "reversal_agents": {
            "available": False,
            "agents": []
        },
        "administration_instructions": {
            "oral": {
                "with_food": "Có thể uống với hoặc không thức ăn. Uống bất kỳ lúc nào trong ngày.",
                "timing": "Uống 1 lần/ngày, bất kỳ lúc nào. Nên uống vào cùng một thời điểm mỗi ngày để dễ nhớ."
            }
        },
        "references": {
            "primary_sources": [
                "FDA Drug Label - Linagliptin (Trajenta)",
                "UpToDate - Linagliptin: Drug Information",
                "Goodman & Gilman's The Pharmacological Basis of Therapeutics"
            ],
            "last_updated": "2025-02-05",
            "evidence_level": "High - FDA approved, multiple RCTs"
        },
        "risk_flags": {
            "high_alert": False,
            "narrow_therapeutic_index": False,
            "bleeding_risk": False,
            "organ_toxicity": ["Pancreatitis (rare)", "Heart failure (slight increased risk)"],
            "qt_prolongation": False,
            "hepatotoxicity": False,
            "nephrotoxicity": False,
            "requires_monitoring": ["Blood glucose", "Signs of pancreatitis", "Signs of heart failure"]
        },
        "guideline_tags": [
            "ADA Diabetes Guidelines",
            "AACE/ACE Diabetes Guidelines",
            "FDA Drug Safety Communication - DPP-4 Inhibitors and Heart Failure"
        ]
    },
    
    "Saxagliptin": {
        "group": "Diabetes - DPP-4 Inhibitor",
        "vietnamese_name": "Saxagliptin, Onglyza",
        "administration": ["PO"],
        "indications": [
            "Đái tháo đường type 2",
            "Kết hợp với metformin hoặc sulfonylurea"
        ],
        "contraindications": [
            "Đái tháo đường type 1",
            "Nhiễm toan ceton",
            "Dị ứng saxagliptin"
        ],
        "dosage": {
            "adult_normal_renal": "5mg x 1 lần/ngày",
            "adult_moderate_renal": "2.5mg x 1 lần/ngày (CrCl ≤50)",
            "adult_severe_renal": "2.5mg x 1 lần/ngày (CrCl ≤50)",
            "dm_t2": "5mg x 1 lần/ngày (CrCl >50), 2.5mg x 1 lần/ngày (CrCl ≤50)",
            "adult_start": "5mg x 1 lần/ngày (CrCl >50)",
            "adult_usual": "5mg x 1 lần/ngày (CrCl >50), 2.5mg x 1 lần/ngày (CrCl ≤50)",
            "adult_max": "5mg/ngày",
            "elderly": "Không cần điều chỉnh liều đặc biệt, nhưng điều chỉnh theo CrCl.",
            "renal_adjustment_dosage": {
                "normal": "5mg x 1 lần/ngày (CrCl >50)",
                "30_60": "2.5mg x 1 lần/ngày (CrCl ≤50)",
                "under_30": "2.5mg x 1 lần/ngày (CrCl ≤50)",
                "dialysis": "2.5mg x 1 lần/ngày"
            },
            "administration_route": "PO",
            "frequency": "1 lần/ngày",
            "with_food": "Có thể uống bất kỳ lúc nào, không cần thức ăn",
            "notes": "Uống bất kỳ lúc nào. Cần điều chỉnh liều ở suy thận (CrCl ≤50). Ít gây hạ đường huyết. Thải trừ chủ yếu qua thận."
        },
        "renal_adjustment": {
            "normal": "5mg/ngày",
            "30_60": "2.5mg/ngày (CrCl ≤50)",
            "under_30": "2.5mg/ngày (CrCl ≤50)"
        },
        "side_effects": [
            "Nhức đầu",
            "Nhiễm trùng đường hô hấp trên",
            "Viêm tụy cấp (hiếm nhưng nguy hiểm)",
            "Đau khớp nghiêm trọng (hiếm)",
            "Suy tim (tăng nhẹ nguy cơ)",
            "Nhiễm trùng đường tiết niệu"
        ],
        "interactions": [
            "Insulin/Sulfonylurea: có thể tăng nguy cơ hạ đường huyết",
            "Digoxin: tăng nhẹ nồng độ digoxin",
            "Ketoconazole: tăng nồng độ saxagliptin"
        ],
        "pregnancy": "B",
        "mechanism_of_action": "Saxagliptin là chất ức chế chọn lọc dipeptidyl peptidase-4 (DPP-4), enzyme chịu trách nhiệm phân hủy incretin hormones (GLP-1 và GIP). Bằng cách ức chế DPP-4, saxagliptin làm tăng nồng độ GLP-1 và GIP, các hormone được tiết ra từ ruột non sau khi ăn. GLP-1 và GIP kích thích tiết insulin từ tế bào beta tuyến tụy phụ thuộc vào glucose (chỉ tiết khi đường huyết cao), đồng thời ức chế tiết glucagon từ tế bào alpha tuyến tụy. Điều này dẫn đến giảm đường huyết sau ăn và giảm sản xuất glucose từ gan. Cơ chế này phụ thuộc vào glucose nên ít gây hạ đường huyết so với sulfonylurea. Saxagliptin được chuyển hóa qua gan (CYP3A4) và bài tiết qua thận, nên cần điều chỉnh liều ở suy thận.",
        "monitoring": [
            "Đường huyết (HbA1c, glucose máu) - đánh giá hiệu quả giảm đường huyết",
            "Chức năng thận (creatinine, CrCl) - cần điều chỉnh liều: CrCl ≤50 → 2.5mg/ngày",
            "Triệu chứng viêm tụy cấp (đau bụng nặng, buồn nôn, nôn) - hiếm nhưng nguy hiểm",
            "Đau khớp nghiêm trọng - hiếm, cần ngừng thuốc nếu xảy ra",
            "Triệu chứng suy tim (khó thở, phù) - tăng nhẹ nguy cơ suy tim",
            "Dấu hiệu phản ứng dị ứng (phát ban, phù mạch) - hiếm",
            "Tác dụng phụ (nhức đầu, nhiễm trùng đường hô hấp trên, nhiễm trùng đường tiết niệu)"
        ],
        "precautions": [
            "Không dùng cho đái tháo đường type 1 (không hiệu quả)",
            "Cần điều chỉnh liều ở suy thận: CrCl ≤50 → 2.5mg/ngày",
            "Nguy cơ viêm tụy cấp - hiếm nhưng nguy hiểm, ngừng ngay nếu có đau bụng nặng",
            "Nguy cơ đau khớp nghiêm trọng - hiếm, ngừng thuốc nếu xảy ra",
            "Tăng nhẹ nguy cơ suy tim - thận trọng ở bệnh nhân có tiền sử suy tim",
            "Tăng nguy cơ hạ đường huyết khi dùng với insulin hoặc sulfonylurea",
            "Ít gây hạ đường huyết khi dùng đơn độc (do cơ chế phụ thuộc glucose)",
            "Có thể dùng bất kỳ lúc nào, không cần ăn",
            "An toàn trong thai kỳ (category B)",
            "Tương tác với ketoconazole - tăng nồng độ saxagliptin"
        ],
        "pharmacokinetics": {
            "half_life": "2.5 giờ (saxagliptin), 3.1 giờ (active metabolite)",
            "onset": "1-2 giờ",
            "duration": "24 giờ",
            "protein_binding": "Minimal",
            "clearance": "Gan: chuyển hóa qua CYP3A4 thành active metabolite. Thận: bài tiết một phần. Cần điều chỉnh liều ở suy thận."
        },
        "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm, tránh ánh sáng",
        "black_box_warnings": None,
        "drug_interactions": {
            "major": [],
            "moderate": [
                {
                    "drug": "Ketoconazole, Itraconazole",
                    "mechanism": "Ức chế CYP3A4, tăng nồng độ saxagliptin",
                    "effect": "Tăng nồng độ saxagliptin, tăng nguy cơ tác dụng phụ",
                    "management": "Thận trọng. Theo dõi dấu hiệu tác dụng phụ. Có thể cần giảm liều saxagliptin."
                },
                {
                    "drug": "Digoxin",
                    "mechanism": "Saxagliptin có thể tăng nhẹ nồng độ digoxin",
                    "effect": "Tăng nồng độ digoxin, tăng nguy cơ độc tính",
                    "management": "Theo dõi nồng độ digoxin và dấu hiệu độc tính."
                },
                {
                    "drug": "Insulin, Sulfonylureas",
                    "mechanism": "Tác dụng cộng dồn giảm đường huyết",
                    "effect": "Tăng nguy cơ hạ đường huyết",
                    "management": "Theo dõi đường huyết chặt chẽ. Có thể cần giảm liều insulin hoặc sulfonylurea."
                }
            ],
            "minor": []
        },
        "contraindications": {
            "tuyệt_đối": [
                "Đái tháo đường type 1",
                "Nhiễm toan ceton do đái tháo đường",
                "Dị ứng saxagliptin hoặc DPP-4 inhibitor"
            ],
            "tương_đối": [
                "Suy thận - cần điều chỉnh liều (CrCl ≤50 → 2.5mg/ngày)",
                "Suy gan - thận trọng",
                "Có thai - category B, an toàn"
            ]
        },
        "pregnancy_lactation": {
            "fda_category": "B",
            "pregnancy_details": "An toàn trong thai kỳ. Saxagliptin là category B. Không có bằng chứng về dị tật thai nhi. Có thể dùng nếu lợi ích > nguy cơ.",
            "lactation": {
                "safety": "Compatible",
                "details": "Saxagliptin bài tiết vào sữa mẹ ở nồng độ thấp. Ít có nguy cơ gây tác dụng phụ ở trẻ bú mẹ.",
                "recommendation": "Có thể dùng khi cho con bú với theo dõi chặt chẽ."
            }
        },
        "hepatic_adjustment": {
            "mild": "Không cần điều chỉnh liều. Saxagliptin chuyển hóa qua gan nhưng có thể dùng ở suy gan nhẹ.",
            "moderate": "Thận trọng, có thể cần giảm liều. Theo dõi đáp ứng điều trị.",
            "severe": "Thận trọng, có thể cần giảm liều. Theo dõi đáp ứng điều trị và độc tính.",
            "notes": "Saxagliptin chuyển hóa qua gan (CYP3A4). Suy gan có thể làm giảm chuyển hóa, tăng nồng độ. Thận trọng ở suy gan nặng."
        },
        "overdose_management": {
            "symptoms": [
                "Hạ đường huyết (nếu dùng với insulin hoặc sulfonylurea)",
                "Nhức đầu",
                "Buồn nôn"
            ],
            "antidote": "Glucose (nếu hạ đường huyết)",
            "treatment": [
                "Ngừng saxagliptin nếu cần",
                "Điều trị hạ đường huyết nếu có (glucose)",
                "Theo dõi tại bệnh viện nếu cần"
            ],
            "monitoring": "Đường huyết, dấu hiệu sinh tồn"
        },
        "reversal_agents": {
            "available": False,
            "agents": []
        },
        "administration_instructions": {
            "oral": {
                "with_food": "Có thể uống với hoặc không thức ăn. Uống bất kỳ lúc nào trong ngày.",
                "timing": "Uống 1 lần/ngày, bất kỳ lúc nào. Nên uống vào cùng một thời điểm mỗi ngày để dễ nhớ."
            }
        },
        "references": {
            "primary_sources": [
                "FDA Drug Label - Saxagliptin (Onglyza)",
                "UpToDate - Saxagliptin: Drug Information",
                "SAVOR-TIMI 53 Study - New England Journal of Medicine",
                "Goodman & Gilman's The Pharmacological Basis of Therapeutics"
            ],
            "last_updated": "2025-02-05",
            "evidence_level": "High - FDA approved, multiple RCTs (SAVOR-TIMI 53)"
        },
        "risk_flags": {
            "high_alert": False,
            "narrow_therapeutic_index": False,
            "bleeding_risk": False,
            "organ_toxicity": ["Pancreatitis (rare)", "Heart failure (slight increased risk)"],
            "qt_prolongation": False,
            "hepatotoxicity": False,
            "nephrotoxicity": False,
            "requires_monitoring": ["Blood glucose", "Renal function (CrCl for dose adjustment)", "Signs of pancreatitis", "Signs of heart failure"]
        },
        "guideline_tags": [
            "ADA Diabetes Guidelines",
            "AACE/ACE Diabetes Guidelines",
            "SAVOR-TIMI 53 Study",
            "FDA Drug Safety Communication - DPP-4 Inhibitors and Heart Failure"
        ]
    },
    
    "Sitagliptin": {'group': 'Diabetes - DPP-4 Inhibitor',
        'vietnamese_name':
        'Sitagliptin, Januvia', 'administration': ['PO'],
        'indications': [
        'Đái tháo đường type 2'],
        'contraindications': ['Đái tháo đường type 1',
        'Nhiễm toan ceton', 'Dị ứng sitagliptin', 'Suy thận nặng (CrCl <30)'],
        'dosage': {'adult_normal_renal': '100mg x 1 lần/ngày',
        'adult_moderate_renal': '50mg x 1 lần/ngày (CrCl 30-50)',
        'adult_severe_renal': '25mg x 1 lần/ngày (CrCl <30)', 'notes':
        'Uống bất kỳ lúc nào. Ít gây hạ đường huyết'},
        'renal_adjustment': {
        'normal': '100mg/ngày', '30_60': '50mg/ngày (CrCl 30-50)', 'under_30':
        '25mg/ngày (CrCl <30)'},
        'side_effects': ['Nhức đầu',
        'Nhiễm trùng đường hô hấp trên', 'Viêm tụy cấp (hiếm nhưng nguy hiểm)',
        'Đau khớp nghiêm trọng (hiếm)', 'Suy tim (tăng nhẹ nguy cơ)'],
        'interactions': [
        'Insulin/Sulfonylurea: có thể tăng nguy cơ hạ đường huyết',
        'Digoxin: tăng nhẹ nồng độ digoxin'],
        'pregnancy': 'B',
        'mechanism_of_action':
        'Sitagliptin là chất ức chế chọn lọc dipeptidyl peptidase-4 (DPP-4), enzyme chịu trách nhiệm phân hủy incretin hormones (GLP-1 và GIP). Bằng cách ức chế DPP-4, sitagliptin làm tăng nồng độ GLP-1 và GIP, các hormone được tiết ra từ ruột non sau khi ăn. GLP-1 và GIP kích thích tiết insulin từ tế bào beta tuyến tụy phụ thuộc vào glucose (chỉ tiết khi đường huyết cao), đồng thời ức chế tiết glucagon từ tế bào alpha tuyến tụy. Điều này dẫn đến giảm đường huyết sau ăn và giảm sản xuất glucose từ gan. Cơ chế này phụ thuộc vào glucose nên ít gây hạ đường huyết so với sulfonylurea. Sitagliptin cũng làm chậm làm rỗng dạ dày và có thể giảm cảm giác thèm ăn nhẹ.'
        , 'monitoring': [
        'Đường huyết (HbA1c, glucose máu) - đánh giá hiệu quả giảm đường huyết',
        'Chức năng thận (creatinine, CrCl) - cần điều chỉnh liều: CrCl 30-50 → 50mg/ngày, CrCl <30 → 25mg/ngày'
        'Triệu chứng viêm tụy cấp (đau bụng nặng, buồn nôn, nôn) - hiếm nhưng nguy hiểm'
        , 'Đau khớp nghiêm trọng - hiếm, cần ngừng thuốc nếu xảy ra',
        'Triệu chứng suy tim (khó thở, phù) - tăng nhẹ nguy cơ suy tim',
        'Dấu hiệu phản ứng dị ứng (phát ban, phù mạch) - hiếm',
        'Tác dụng phụ (nhức đầu, nhiễm trùng đường hô hấp trên)'],
        'precautions': ['Không dùng cho đái tháo đường type 1 (không hiệu quả)',
        'Cần điều chỉnh liều ở suy thận: CrCl 30-50 → 50mg/ngày, CrCl <30 → 25mg/ngày'
        'Nguy cơ viêm tụy cấp - hiếm nhưng nguy hiểm, ngừng ngay nếu có đau bụng nặng'
        , 'Nguy cơ đau khớp nghiêm trọng - hiếm, ngừng thuốc nếu xảy ra',
        'Tăng nhẹ nguy cơ suy tim - thận trọng ở bệnh nhân có tiền sử suy tim',
        'Tăng nguy cơ hạ đường huyết khi dùng với insulin hoặc sulfonylurea',
        'Ít gây hạ đường huyết khi dùng đơn độc (do cơ chế phụ thuộc glucose)',
        'Có thể dùng bất kỳ lúc nào, không cần ăn',
        'An toàn trong thai kỳ (category B)',
        'Tương tác nhẹ với digoxin - có thể tăng nồng độ digoxin'],
        'pharmacokinetics': {'half_life': '12.4 giờ', 'onset': '1-2 giờ',
        'duration': '24 giờ', 'protein_binding': '38%', 'clearance':
        'Thận: bài tiết chủ yếu qua thận (79% nguyên dạng, không chuyển hóa). Gan: ít chuyển hóa. Cần điều chỉnh liều ở suy thận.'
        },
        'storage':
        'Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm, tránh ánh sáng. Viên nén: bảo quản trong bao bì kín.'
        , 'black_box_warnings': None, 'drug_interactions': {'major': [],
        'moderate': [{'drug': 'Digoxin', 'mechanism':
        'Sitagliptin có thể tăng nhẹ nồng độ digoxin', 'effect':
        'Tăng nguy cơ độc tính digoxin', 'management':
        'Theo dõi nồng độ digoxin, ECG. Điều chỉnh liều digoxin nếu cần.'}, {
        'drug': 'Insulin, Sulfonylurea (glibenclamide, gliclazide)',
        'mechanism': 'Tác dụng hiệp đồng giảm đường huyết', 'effect':
        'Tăng nguy cơ hạ đường huyết', 'management':
        'Thận trọng. Theo dõi đường huyết. Có thể cần giảm liều insulin hoặc sulfonylurea.'
        }],
        'minor': [{'drug': 'CYP3A4 substrates', 'mechanism':
        'Sitagliptin ít chuyển hóa qua CYP, ít tương tác', 'effect':
        'Tương tác tối thiểu', 'management': 'Không cần điều chỉnh liều'}]},
        'contraindications': {'tuyệt_đối': ['Đái tháo đường type 1',
        'Nhiễm toan ceton do đái tháo đường', 'Dị ứng sitagliptin',
        'Viêm tụy cấp đang diễn ra'],
        'tương_đối': [
        'Suy thận nặng (CrCl <30) - cần giảm liều (25mg/ngày)',
        'Suy thận trung bình (CrCl 30-50) - cần giảm liều (50mg/ngày)',
        'Tiền sử viêm tụy cấp - tăng nguy cơ',
        'Tiền sử suy tim - tăng nhẹ nguy cơ suy tim',
        'Đau khớp nghiêm trọng - ngừng thuốc nếu xảy ra']},
        'pregnancy_lactation': {'fda_category': 'B', 'pregnancy_details':
        'Không có bằng chứng về nguy cơ gây dị tật thai nhi ở động vật. Có thể dùng trong thai kỳ nếu lợi ích > nguy cơ. Ít dữ liệu ở người, nhưng không có báo cáo về dị tật thai nhi. Theo dõi đường huyết chặt chẽ trong thai kỳ.'
        , 'lactation': {'safety': 'Caution', 'details':
        'Sitagliptin bài tiết vào sữa mẹ ở nồng độ thấp. Không có dữ liệu đầy đủ về an toàn ở trẻ bú mẹ.'
        , 'recommendation':
        'Thận trọng khi dùng khi cho con bú. Cân nhắc ngừng cho con bú hoặc ngừng thuốc nếu có thể. Nếu cần dùng, theo dõi trẻ chặt chẽ.'
        }},
        'hepatic_adjustment': {'mild': 'Không đổi', 'moderate': 'Không đổi',
        'severe': 'Không đổi (chủ yếu thải qua thận, không phụ thuộc gan)',
        'notes':
        'Sitagliptin chủ yếu bài tiết qua thận (79% nguyên dạng), không chuyển hóa đáng kể qua gan. Không cần điều chỉnh liều ở suy gan.'
        },
        'overdose_management': {'symptoms': [
        'Hạ đường huyết (nếu dùng với insulin hoặc sulfonylurea)',
        'Đau bụng, buồn nôn, nôn (dấu hiệu viêm tụy)', 'Nhức đầu', 'Đau khớp'],
        'antidote': 'Không có antidote đặc hiệu', 'treatment': [
        'Điều trị hạ đường huyết nếu có: Glucose 15-20g PO hoặc dextrose IV',
        'Rửa dạ dày nếu uống trong vòng 1-2 giờ', 'Than hoạt tính',
        'Theo dõi đường huyết, chức năng thận',
        'Nếu có dấu hiệu viêm tụy cấp: ngừng thuốc, điều trị hỗ trợ, theo dõi amylase/lipase'
        , 'Điều trị hỗ trợ'],
        'monitoring':
        'Đường huyết, chức năng thận, dấu hiệu viêm tụy (đau bụng, amylase/lipase), đau khớp'
        },
        'reversal_agents': {'available': False, 'agents': [],
        'notes':
        'Không có antidote đặc hiệu. Điều trị chủ yếu là hỗ trợ và điều trị triệu chứng. Ngừng thuốc ngay nếu có viêm tụy cấp. Điều trị viêm tụy hỗ trợ nếu có.'},
        'administration_instructions': {'oral': {'with_food':
        'Có thể dùng với hoặc không có thức ăn. Không ảnh hưởng đến hấp thu.',
        'timing':
        'Uống 1 lần/ngày, bất kỳ lúc nào trong ngày. Nên uống vào cùng một thời điểm mỗi ngày để dễ nhớ.'
        },
        'iv': {'reconstitution': 'Không có dạng IV', 'infusion_rate': 'N/A',
        'compatibility': [],
        'incompatibility': [],
        'notes': 'Chỉ có dạng uống'
        }},
        'pediatric_dosing': {'neonates':
        'Không khuyến cáo cho trẻ <18 tuổi (dữ liệu hạn chế). Đái tháo đường type 2 ở trẻ em thường hiếm, cần đánh giá cẩn thận.',
        'infants':
        'Không khuyến cáo cho trẻ <18 tuổi (dữ liệu hạn chế). Đái tháo đường type 2 ở trẻ em thường hiếm, cần đánh giá cẩn thận.',
        'children':
        'Không khuyến cáo cho trẻ <18 tuổi (dữ liệu hạn chế). Nếu cần: 25-100mg x 1 lần/ngày tùy chức năng thận. Điều chỉnh liều theo CrCl: CrCl 30-50 → 50mg/ngày, CrCl <30 → 25mg/ngày.',
        'adolescents':
        '≥18 tuổi: Liều người lớn. 100mg x 1 lần/ngày (CrCl ≥50), 50mg x 1 lần/ngày (CrCl 30-50), 25mg x 1 lần/ngày (CrCl <30).',
        'notes':
        'Dữ liệu hạn chế ở trẻ em. Đái tháo đường type 2 ở trẻ em thường hiếm. Cần điều chỉnh liều theo chức năng thận. Theo dõi đường huyết, dấu hiệu viêm tụy cấp.'},
        'geriatric_dosing': {'considerations':
        'Người cao tuổi có thể có suy thận phổ biến hơn, cần điều chỉnh liều theo CrCl. Tăng nhẹ nguy cơ suy tim. Ít gây hạ đường huyết hơn sulfonylurea.',
        'dose_adjustment':
        'Điều chỉnh liều theo chức năng thận: CrCl ≥50 → 100mg/ngày, CrCl 30-50 → 50mg/ngày, CrCl <30 → 25mg/ngày. Không cần điều chỉnh liều theo tuổi nếu chức năng thận bình thường.',
        'monitoring':
        'Theo dõi đường huyết (HbA1c, glucose máu). Theo dõi chức năng thận (creatinine, CrCl) định kỳ. Theo dõi dấu hiệu viêm tụy cấp (đau bụng nặng, buồn nôn, nôn). Theo dõi triệu chứng suy tim (khó thở, phù).'},
        'brand_names': {'vietnam': [
        'Sitagliptin', 'Januvia', 'Sitagliptin Stada', 'Sitaglu'],
        'common': [
        'Januvia', 'Sitagliptin']},
        'cost_estimate': {'unit': 'VND',
        'range': '20,000 - 60,000 VND/viên (tùy hàm lượng và thương hiệu)',
        'note':
        'Giá thay đổi theo thương hiệu và nhà thuốc. Sitagliptin generic thường rẻ hơn (20,000-40,000 VND/viên 100mg). Januvia (brand) thường đắt hơn (40,000-60,000 VND/viên 100mg).'},
        'references': {'primary_sources': [
        'FDA Drug Label - Januvia (sitagliptin)',
        'UpToDate - Sitagliptin: Drug information',
        'TECOS Study - New England Journal of Medicine',
        'American Diabetes Association guidelines'],
        'last_updated':
        '2024-12-19', 'evidence_level':
        'High - Multiple RCTs and systematic reviews (TECOS study)'},
        'risk_flags': {
            'high_alert': False,
            'narrow_therapeutic_index': False,
            'bleeding_risk': False,
            'organ_toxicity': ['Pancreatitis (rare)', 'Heart failure (slight increased risk)'],
        'qt_prolongation': False,
            'hepatotoxicity': False,
            'nephrotoxicity': False,
            'requires_monitoring': ['Blood glucose', 'Renal function (CrCl for dose adjustment)', 'Signs of pancreatitis']
        }, 'guideline_tags': [
            'ADA Diabetes Guidelines',
            'AACE/ACE Diabetes Guidelines',
            'TECOS Study',
            'FDA Drug Safety Communication - DPP-4 Inhibitors and Heart Failure'
        ]},
    "Vildagliptin": {'group': 'Diabetes - DPP-4 Inhibitor',
        'vietnamese_name':
        'Vildagliptin, Galvus', 'administration': ['PO'],
        'indications': [
        'Đái tháo đường type 2'],
        'contraindications': ['Đái tháo đường type 1',
        'Nhiễm toan ceton', 'Suy gan nặng'],
        'dosage': {'adult_standard':
        '50mg x 2 lần/ngày (sáng và tối)', 'adult_metformin_combination':
        '50mg x 2 lần/ngày', 'notes': 'Uống với bữa ăn. Ít gây hạ đường huyết'},
        'renal_adjustment': {'normal': '50mg x 2 lần/ngày', '30_60':
        '50mg x 2 lần/ngày', 'under_30': 'Thận trọng'},
        'side_effects': [
        'Nhức đầu', 'Chóng mặt', 'Nhiễm trùng đường hô hấp',
        'Viêm tụy cấp (hiếm)', 'Đau khớp (hiếm)'],
        'interactions': [
        'Insulin/Sulfonylurea: có thể tăng nguy cơ hạ đường huyết'],
        'pregnancy': 'C', 'mechanism_of_action':
        'Vildagliptin là DPP-4 (dipeptidyl peptidase-4) inhibitor, ức chế enzyme DPP-4 phân hủy incretin hormones (GLP-1 và GIP). Khi DPP-4 bị ức chế, nồng độ GLP-1 và GIP tăng, kích thích tế bào beta tụy tiết insulin (glucose-dependent) và ức chế tế bào alpha tụy tiết glucagon. Kết quả là tăng tiết insulin và giảm glucagon, giảm đường huyết sau ăn và đường huyết đói. Vildagliptin chỉ hoạt động khi đường huyết cao, nên ít gây hạ đường huyết hơn so với sulfonylurea'
        , 'monitoring': ['HbA1c mỗi 3 tháng', 'Đường huyết đói và sau ăn',
        'Chức năng gan (ALT, AST) trước và trong điều trị (nguy cơ viêm tụy cấp)',
        'Dấu hiệu viêm tụy cấp (đau bụng, nôn - hiếm nhưng nguy hiểm)',
        'Chức năng thận (creatinine, eGFR) định kỳ'],
        'precautions': [
        'Uống với bữa ăn (tăng hấp thu)',
        'Ít gây hạ đường huyết hơn sulfonylurea (glucose-dependent)',
        'Có thể dùng kết hợp với metformin, sulfonylurea, hoặc insulin',
        'Ngừng ngay nếu có dấu hiệu viêm tụy cấp (hiếm nhưng nguy hiểm)',
        'Có thể dùng trong thai kỳ (category C)',
        'Thận trọng nếu suy thận nặng (CrCl <30)',
        'Có thể tăng nguy cơ hạ đường huyết khi dùng với insulin/sulfonylurea'],
        'pharmacokinetics': {'half_life': '2-3 giờ (ngắn)', 'onset':
        '2-4 tuần (giảm HbA1c)', 'duration': '12-24 giờ', 'protein_binding':
        '9%', 'clearance': 'Thận (thải trừ chủ yếu), gan (chuyển hóa)'},
        'storage': 'Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm',
        'black_box_warnings':
        'Có thể gây viêm tụy cấp hiếm nhưng nguy hiểm. Ngừng ngay nếu có dấu hiệu viêm tụy cấp (đau bụng, nôn)'
        , 'drug_interactions': {'major': [],
        'moderate': [{'drug':
        'Insulin, Sulfonylurea (Glibenclamide, Gliclazide)', 'mechanism':
        'Vildagliptin tăng tiết insulin, tác dụng cộng dồn với insulin/sulfonylurea.'
        , 'effect': 'Tăng nguy cơ hạ đường huyết', 'management':
        'Thận trọng. Có thể cần giảm liều insulin/sulfonylurea. Theo dõi đường huyết chặt chẽ.'
        }],
        'minor': []},
        'contraindications': {'tuyệt_đối': [
        'Đái tháo đường type 1 - không hiệu quả (cần insulin)',
        'Nhiễm toan ceton - cần insulin, không dùng vildagliptin',
        'Suy gan nặng - chống chỉ định'],
        'tương_đối': [
        'Suy thận nặng (CrCl <30) - thận trọng, có thể cần giảm liều',
        'Có thai - category C, thận trọng',
        'Viêm tụy trước đây - tăng nguy cơ viêm tụy cấp']},
        'pregnancy_lactation': {'fda_category': 'C', 'pregnancy_details':
        'Vildagliptin là category C. Không có nghiên cứu đầy đủ ở phụ nữ có thai. Dùng được nếu lợi ích > nguy cơ. Thận trọng, đặc biệt trong tam cá nguyệt đầu.'
        , 'lactation': {'safety': 'Unknown', 'details':
        'Không biết vildagliptin có bài tiết vào sữa mẹ hay không. Thận trọng khi dùng khi cho con bú.'
        , 'recommendation':
        'Thận trọng khi dùng khi cho con bú. Cân nhắc ngừng cho con bú hoặc ngừng thuốc.'
        }},
        'hepatic_adjustment': {'mild':
        'Không cần điều chỉnh liều. Theo dõi chức năng gan.', 'moderate':
        'Thận trọng, có thể cần giảm liều. Theo dõi chức năng gan chặt chẽ.',
        'severe':
        'Chống chỉ định. Suy gan nặng làm giảm chuyển hóa, tăng nguy cơ độc tính.',
        'notes':
        'Vildagliptin chuyển hóa ở gan. Suy gan nặng làm giảm chuyển hóa, tăng nguy cơ độc tính, đặc biệt viêm tụy cấp.'
        },
        'overdose_management': {'symptoms': [
        'Hạ đường huyết (nếu dùng với insulin/sulfonylurea)',
        'Viêm tụy cấp (đau bụng, nôn, sốt)', 'Nhức đầu, chóng mặt'],
        'antidote':
        'Không có antidote đặc hiệu. Điều trị hỗ trợ.', 'treatment': [
        'Ngừng vildagliptin ngay lập tức',
        'Nếu hạ đường huyết: glucose đường uống hoặc IV, theo dõi đường huyết',
        'Nếu viêm tụy cấp: điều trị hỗ trợ, nhịn ăn, truyền dịch, giảm đau, theo dõi chức năng tụy'
        , 'Theo dõi đường huyết, chức năng gan, chức năng tụy'],
        'monitoring':
        'Đường huyết, dấu hiệu viêm tụy cấp, chức năng gan, dấu hiệu sinh tồn'},
        'reversal_agents': {'available': False, 'agents': [],
        'notes':
        'Không có antidote đặc hiệu. Điều trị chủ yếu là hỗ trợ và điều trị triệu chứng. Ngừng thuốc ngay nếu có viêm tụy cấp. Điều trị viêm tụy hỗ trợ nếu có.'},
        'administration_instructions': {'oral': {'with_food':
        'Uống với bữa ăn (tăng hấp thu). Có thể uống sáng và tối với bữa ăn.',
        'timing': 'Uống 2 lần/ngày (sáng và tối), cách đều, với bữa ăn.'},
        'iv':
        {'reconstitution': 'Không có dạng IV', 'infusion_rate': 'N/A',
        'compatibility': [],
        'incompatibility': [],
        'notes': 'Chỉ có dạng uống'
        }},
        'references': {'primary_sources': [
        'FDA Drug Label - Vildagliptin (Galvus)',
        'UpToDate - Vildagliptin: Drug Information',
        "Goodman & Gilman's The Pharmacological Basis of Therapeutics (14th ed)"
        ],
        'last_updated': '2025-02-04', 'evidence_level':
        'A - Dựa trên FDA drug labels và dữ liệu lâm sàng'},
        'risk_flags': {
            'high_alert': False,
            'narrow_therapeutic_index': False,
            'bleeding_risk': False,
            'organ_toxicity': ['Pancreatitis (rare)', 'Hepatotoxicity (contraindicated in severe hepatic impairment)'],
        'qt_prolongation': False,
            'hepatotoxicity': True,
            'nephrotoxicity': False,
            'requires_monitoring': ['Blood glucose', 'Hepatic function (ALT, AST)', 'Signs of pancreatitis']
        }, 'guideline_tags': [
            'ADA Diabetes Guidelines',
            'AACE/ACE Diabetes Guidelines',
            'FDA Drug Safety Communication - DPP-4 Inhibitors and Pancreatitis'
        ]},
    
}

__all__ = ['DPP_4_INHIBITORS_DRUGS']
