"""Gastrointestinal Drugs - Other GI Medications
Prucalopride (prokinetic), Alginate (GERD)"""

OTHER_GI_DRUGS = {
    "Prucalopride": {
        "group": "Gastrointestinal - Prokinetic (5-HT4 Agonist)",
        "vietnamese_name": "Prucalopride, Motegrity",
        "brand_names": {
            "common": ["Motegrity"],
            "vietnam": ["Prucalopride 1mg/2mg", "Motegrity"]
        },
        "administration": ["PO"],
        "indications": [
            "Táo bón mạn tính vô căn",
            "Táo bón do opioid (kết hợp với các thuốc khác)",
            "Liệt dạ dày (gastroparesis) - off-label"
        ],
        "contraindications": [
            "Tắc ruột cơ học",
            "Thủng ruột",
            "Viêm ruột cấp nặng",
            "Suy thận nặng (CrCl <30 ml/phút)",
            "Dị ứng prucalopride"
        ],
        "dosage": {
            "adult_po": "2mg PO x 1 lần/ngày",
            "adult_elderly": "1mg PO x 1 lần/ngày (người ≥65 tuổi)",
            "adult_renal_impairment": "1mg PO x 1 lần/ngày (CrCl 30-60 ml/phút)",
            "pediatric_dosing": "Không khuyến cáo cho trẻ em",
            "geriatric_dosing": "Giảm liều còn 1mg/ngày ở người ≥65 tuổi",
            "notes": "Uống với hoặc không với thức ăn. Tác dụng sau 1-3 ngày. Hiệu quả tốt cho táo bón mạn tính."
        },
        "renal_adjustment": {
            "normal": "Không cần chỉnh liều",
            "30_60": "Giảm liều còn 1mg/ngày",
            "under_30": "CHỐNG CHỈ ĐỊNH",
            "dialysis": "CHỐNG CHỈ ĐỊNH",
            "notes": "Prucalopride thải trừ qua thận. Suy thận làm giảm thải trừ, tăng nồng độ thuốc."
        },
        "side_effects": [
            "Nhức đầu",
            "Buồn nôn",
            "Đau bụng",
            "Tiêu chảy",
            "Chóng mặt",
            "Mệt mỏi"
        ],
        "interactions": [
            "Ít tương tác thuốc đáng kể",
            "CYP3A4 inhibitors: có thể tăng nồng độ prucalopride"
        ],
        "pregnancy": "C - Dữ liệu hạn chế, chỉ dùng khi lợi ích > nguy cơ",
        "mechanism_of_action": "5-HT4 receptor agonist. Kích thích thụ thể 5-HT4 ở ruột, tăng giải phóng acetylcholine và các chất dẫn truyền thần kinh khác, tăng nhu động ruột và làm rỗng đại tràng. Giúp điều trị táo bón mạn tính bằng cách tăng nhu động ruột.",
        "monitoring": [
            "Triệu chứng táo bón: tần suất đi ngoài, tính chất phân",
            "Dấu hiệu tiêu chảy",
            "Chức năng thận (creatinine, eGFR)"
        ],
        "precautions": [
            "Uống với hoặc không với thức ăn",
            "Giảm liều ở suy thận trung bình và người già",
            "CHỐNG CHỈ ĐỊNH ở suy thận nặng",
            "Thận trọng ở bệnh nhân có tiền sử bệnh tim mạch"
        ],
        "pharmacokinetics": {
            "half_life": "24-30 giờ",
            "onset": "1-3 ngày",
            "duration": "Cần dùng liên tục",
            "protein_binding": "98%",
            "metabolism": "Gan (CYP3A4)",
            "clearance": "Thận (thải trừ)"
        },
        "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm, tránh ánh sáng",
        "black_box_warnings": None,
        "drug_interactions": {
            "major": [],
            "moderate": [
                {
                    "drug": "CYP3A4 inhibitors (ketoconazole, itraconazole, clarithromycin)",
                    "mechanism": "Ức chế chuyển hóa prucalopride qua CYP3A4",
                    "effect": "Tăng nồng độ prucalopride, tăng tác dụng phụ",
                    "management": "Thận trọng, có thể giảm liều prucalopride."
                }
            ],
            "minor": []
        },
        "contraindications_detail": {
            "tuyệt_đối": [
                "Tắc ruột cơ học",
                "Thủng ruột",
                "Viêm ruột cấp nặng",
                "Suy thận nặng (CrCl <30 ml/phút) - CHỐNG CHỈ ĐỊNH",
                "Dị ứng prucalopride"
            ],
            "tương_đối": [
                "Suy thận trung bình (CrCl 30-60) - giảm liều",
                "Người già (≥65 tuổi) - giảm liều",
                "Bệnh tim mạch - thận trọng"
            ]
        },
        "pregnancy_lactation": {
            "fda_category": "C",
            "pregnancy_details": "Dữ liệu hạn chế. Chỉ dùng khi lợi ích > nguy cơ.",
            "lactation": {
                "safety": "Unknown",
                "details": "Chưa rõ bài tiết vào sữa mẹ. Thận trọng khi cho con bú.",
                "recommendation": "Thận trọng khi cho con bú."
            }
        },
        "hepatic_adjustment": {
            "mild": "Không cần chỉnh liều",
            "moderate": "Thận trọng",
            "severe": "Thận trọng, có thể giảm liều",
            "notes": "Prucalopride chuyển hóa ở gan qua CYP3A4. Suy gan có thể làm giảm chuyển hóa."
        },
        "overdose_management": {
            "symptoms": [
                "Tiêu chảy",
                "Đau bụng",
                "Nhức đầu",
                "Chóng mặt"
            ],
            "antidote": "Không có antidote đặc hiệu",
            "treatment": [
                "Ngừng thuốc",
                "Hỗ trợ triệu chứng",
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
                "timing": "Uống 1 lần/ngày. Giảm liều ở suy thận trung bình và người già."
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
            "FDA Drug Information"
        ],
        "references": {
            "primary_sources": [
                "FDA Drug Label - Prucalopride (Motegrity)",
                "UpToDate - Prucalopride: Drug information",
                "ACG 2013 Constipation Guidelines"
            ],
            "last_updated": "2025-01-15",
            "evidence_level": "High - FDA approved, multiple RCTs"
        },
        "cost_estimate": {
            "generic": "Cao",
            "brand": "Rất cao",
            "notes": "Thuốc mới, giá cao"
        }
    },
    
    "Alginate": {
        "group": "Gastrointestinal - GERD Treatment (Alginate Barrier)",
        "vietnamese_name": "Alginate, Gaviscon, Gavison Double Action",
        "brand_names": {
            "common": ["Gaviscon", "Gaviscon Double Action"],
            "vietnam": ["Alginate", "Gaviscon"]
        },
        "administration": ["PO"],
        "indications": [
            "Trào ngược dạ dày-thực quản (GERD)",
            "Ợ nóng, ợ chua",
            "Viêm thực quản do trào ngược"
        ],
        "contraindications": [
            "Dị ứng alginate hoặc các thành phần khác",
            "Suy thận nặng (nếu chứa natri cao)"
        ],
        "dosage": {
            "adult_po": "10-20ml hỗn dịch hoặc 2-4 viên nhai PO sau bữa ăn và trước khi ngủ",
            "adult_max": "4 lần/ngày",
            "pediatric_dosing": "Trẻ em: 5-10ml hỗn dịch hoặc 1-2 viên nhai PO sau bữa ăn và trước khi ngủ",
            "geriatric_dosing": "Không cần chỉnh liều, nhưng thận trọng ở người già",
            "notes": "Uống sau bữa ăn và trước khi ngủ. Nhai kỹ viên trước khi nuốt. Tạo lớp bảo vệ trên dạ dày, ngăn trào ngược."
        },
        "renal_adjustment": {
            "normal": "Không cần chỉnh liều",
            "30_60": "Thận trọng nếu chứa natri cao",
            "under_30": "Thận trọng nếu chứa natri cao",
            "notes": "Một số chế phẩm chứa natri cao, cần thận trọng ở suy thận."
        },
        "side_effects": [
            "Táo bón (nếu chứa nhôm)",
            "Tiêu chảy (nếu chứa magie)",
            "Đầy hơi",
            "Buồn nôn"
        ],
        "interactions": [
            "Các thuốc khác: có thể giảm hấp thu do tạo lớp bảo vệ",
            "Cách xa các thuốc khác 2 giờ"
        ],
        "pregnancy": "B - Thường an toàn trong thai kỳ",
        "mechanism_of_action": "Alginate barrier. Alginate (từ rong biển) phản ứng với acid dạ dày tạo thành gel dày, nổi trên bề mặt dịch dạ dày. Gel này tạo thành lớp bảo vệ vật lý, ngăn trào ngược acid vào thực quản. Khác với antacid (trung hòa acid), alginate tạo hàng rào vật lý chống trào ngược.",
        "monitoring": [
            "Triệu chứng GERD: giảm ợ nóng, ợ chua",
            "Dấu hiệu táo bón hoặc tiêu chảy"
        ],
        "precautions": [
            "Uống sau bữa ăn và trước khi ngủ",
            "Nhai kỹ viên trước khi nuốt",
            "Cách xa các thuốc khác 2 giờ (có thể giảm hấp thu)",
            "Thận trọng ở suy thận nếu chứa natri cao"
        ],
        "pharmacokinetics": {
            "half_life": "Không áp dụng (tác dụng tại chỗ)",
            "onset": "Vài phút",
            "duration": "2-4 giờ",
            "protein_binding": "Không áp dụng",
            "clearance": "Thải qua phân (không hấp thu đáng kể)"
        },
        "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm. Lắc kỹ hỗn dịch trước khi dùng.",
        "black_box_warnings": None,
        "drug_interactions": {
            "major": [],
            "moderate": [
                {
                    "drug": "Các thuốc khác",
                    "mechanism": "Alginate tạo lớp bảo vệ, có thể giảm hấp thu thuốc",
                    "effect": "Giảm hấp thu thuốc, giảm hiệu quả",
                    "management": "Cách xa các thuốc khác ít nhất 2 giờ."
                }
            ],
            "minor": []
        },
        "contraindications_detail": {
            "tuyệt_đối": [
                "Dị ứng alginate hoặc các thành phần khác"
            ],
            "tương_đối": [
                "Suy thận nặng (nếu chứa natri cao) - thận trọng"
            ]
        },
        "pregnancy_lactation": {
            "fda_category": "B",
            "pregnancy_details": "Thường an toàn trong thai kỳ. Ít hấp thu toàn thân.",
            "lactation": {
                "safety": "Compatible",
                "details": "Alginate không hấp thu đáng kể, không vào sữa mẹ.",
                "recommendation": "Có thể dùng khi cho con bú."
            }
        },
        "hepatic_adjustment": {
            "mild": "Không cần chỉnh liều",
            "moderate": "Không cần chỉnh liều",
            "severe": "Không cần chỉnh liều",
            "notes": "Tác dụng tại chỗ ở dạ dày, không phụ thuộc chuyển hóa gan."
        },
        "overdose_management": {
            "symptoms": [
                "Táo bón hoặc tiêu chảy",
                "Đầy hơi"
            ],
            "antidote": "Không có antidote đặc hiệu",
            "treatment": [
                "Ngừng thuốc",
                "Hỗ trợ triệu chứng"
            ],
            "monitoring": "Theo dõi triệu chứng"
        },
        "reversal_agents": {
            "available": False,
            "agents": []
        },
        "administration_instructions": {
            "oral": {
                "with_food": "Uống sau bữa ăn và trước khi ngủ",
                "timing": "Uống sau bữa ăn và trước khi ngủ. Nhai kỹ viên trước khi nuốt. Lắc kỹ hỗn dịch trước khi dùng."
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
            "ACG 2017 GERD Guidelines",
            "FDA Drug Information"
        ],
        "references": {
            "primary_sources": [
                "UpToDate - Alginate: Drug information",
                "ACG 2017 GERD Guidelines",
                "FDA Drug Information"
            ],
            "last_updated": "2025-01-15",
            "evidence_level": "High - Guideline-recommended for GERD"
        },
        "cost_estimate": {
            "generic": "Thấp",
            "brand": "Thấp-trung bình",
            "notes": "OTC medication, giá rẻ"
        }
    }
}

__all__ = ["OTHER_GI_DRUGS"]
