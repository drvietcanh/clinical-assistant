"""
SGLT2 Inhibitors (Thuốc ức chế SGLT2)
Nhóm thuốc mới nhất cho đái tháo đường type 2, có lợi ích tim mạch và thận đã được chứng minh.
"""

SGLT2_INHIBITORS_DRUGS = {
    "Empagliflozin":     {
        "group": "Diabetes - SGLT2 Inhibitor",
        "vietnamese_name": "Empagliflozin, Jardiance",
        "brand_names": {
            "common": [
                "Jardiance"
    ],
            "vietnam": [
                "Jardiance 10/25mg"
    ],
        },
        "administration": [
            "PO"
    ],
        "indications": [
            "Đái tháo đường type 2",
            "Suy tim (HFrEF và HFpEF) - Chỉ định mới, không cần có đái tháo đường",
            "Bệnh thận mạn (CKD) - Chỉ định mới"
    ],
        "contraindications": [
            "Đái tháo đường type 1",
            "Nhiễm toan ceton đái tháo đường (DKA)",
            "Suy thận nặng (eGFR <20)",
            "Lọc máu"
    ],
        "dosage": {
            "adult_start": "10mg PO x 1 lần/ngày vào buổi sáng",
            "adult_usual": "10-25mg PO x 1 lần/ngày vào buổi sáng. Thường 10mg/ngày, có thể tăng lên 25mg nếu cần.",
            "adult_max": "25mg/ngày",
            "dm_t2": "Khởi đầu 10mg PO x 1 lần/ngày vào buổi sáng. Có thể tăng lên 25mg sau ít nhất 2-4 tuần nếu cần và dung nạp tốt. Tối đa 25mg/ngày.",
            "heart_failure": "10mg PO x 1 lần/ngày (không phụ thuộc đái tháo đường). Dựa trên EMPEROR-Reduced và EMPEROR-Preserved trials. Giảm tử vong tim mạch và nhập viện do suy tim ở cả HFrEF và HFpEF.",
            "ckd": "10mg PO x 1 lần/ngày (eGFR ≥20, không phụ thuộc đái tháo đường). Dựa trên EMPA-KIDNEY trial. Làm chậm tiến triển bệnh thận mạn và giảm biến cố tim mạch. CHỐNG CHỈ ĐỊNH nếu eGFR <20.",
            "elderly": "Khởi đầu 10mg PO x 1 lần/ngày vào buổi sáng, tăng dần chậm. Người cao tuổi nhạy cảm hơn với tác dụng phụ (mất nước, hạ huyết áp). Theo dõi huyết áp và thể tích dịch chặt chẽ.",
            "pregnancy": "Không khuyến nghị trong thai kỳ. Insulin là lựa chọn ưu tiên trong thai kỳ.",
            "renal_adjustment_dosage": {
                "normal": "10-25mg PO x 1 lần/ngày (eGFR ≥60)",
                "45_60": "10mg PO x 1 lần/ngày (eGFR 45-60). Có thể tăng lên 25mg nếu cần và dung nạp tốt.",
                "30_45": "10mg PO x 1 lần/ngày (eGFR 30-45). Không tăng liều lên 25mg. Theo dõi chức năng thận thường xuyên.",
                "20_30": "10mg PO x 1 lần/ngày (eGFR 20-30). CHỐNG CHỈ ĐỊNH nếu eGFR <20. Theo dõi chức năng thận rất chặt chẽ.",
                "under_20": "CHỐNG CHỈ ĐỊNH (eGFR <20)",
                "dialysis": "CHỐNG CHỈ ĐỊNH"
            },
            "hepatic_adjustment_dosage": {
                "mild": "10-25mg PO x 1 lần/ngày. Không cần điều chỉnh liều đặc biệt.",
                "moderate": "10-25mg PO x 1 lần/ngày. Không cần điều chỉnh liều đặc biệt. Theo dõi chức năng gan.",
                "severe": "Thận trọng, có thể cần giảm liều. Khởi đầu 10mg/ngày, tăng dần chậm. Theo dõi chức năng gan chặt chẽ."
            },
            "administration_route": "PO (uống)",
            "frequency": "1 lần/ngày",
            "with_food": "Có thể uống với hoặc không thức ăn. Uống bất kỳ lúc nào trong ngày, nhưng nên uống vào buổi sáng để tránh đi tiểu đêm.",
            "timing": "Uống 1 lần/ngày vào buổi sáng. Uống cùng giờ mỗi ngày để dễ nhớ. Có thể uống đói hoặc no. Uống với nhiều nước để giảm nguy cơ nhiễm trùng đường tiết niệu.",
            "titration": "Tăng liều từ từ: Tuần 1-4: 10mg/ngày. Tuần 5+: 25mg/ngày (nếu cần và dung nạp tốt). Đánh giá hiệu quả sau mỗi 2-4 tuần. Không tăng liều nếu eGFR <45.",
            "notes": "Uống buổi sáng, có thể uống đói hoặc no. Tác dụng giảm đường huyết nhẹ (HbA1c ~0.5-0.8%) nhưng lợi ích tim mạch và thận rất lớn. CHỐNG CHỈ ĐỊNH nếu eGFR <20. Chỉ định mở rộng: Suy tim (HFrEF và HFpEF) và bệnh thận mạn (CKD) không phụ thuộc đái tháo đường. Ngừng thuốc khi bệnh nhân ốm nặng, nhịn ăn, phẫu thuật để tránh DKA."
        },
        "side_effects": [
            "Nhiễm nấm âm đạo (Phụ nữ - rất phổ biến ~10%)",
            "Nhiễm trùng đường tiết niệu",
            "Đa niệu (Tiểu nhiều)",
            "Hạ huyết áp tư thế (đặc biệt khi dùng với lợi tiểu)",
            "Nhiễm toan ceton đái tháo đường (DKA) - Hiếm nhưng nguy hiểm, có thể xảy ra ngay cả khi đường huyết bình thường (euglycemic DKA)"
    ],
        "interactions": [
            "Lợi tiểu: Tăng nguy cơ mất nước, hạ huyết áp.",
            "Insulin, Sulfonylurea: Tăng nguy cơ hạ đường huyết (cần giảm liều insulin/SU)."
    ],
        "mechanism_of_action": """Ức chế SGLT2 (Sodium-Glucose Cotransporter 2) ở ống lượn gần thận, ngăn tái hấp thu glucose → Glucose thải qua nước tiểu (glucosuria) → Giảm đường huyết. Lợi ích tim mạch: Giảm tử vong tim mạch, nhập viện do suy tim (EMPA-REG OUTCOME trial). Lợi ích thận: Làm chậm tiến triển bệnh thận mạn.""",
        "monitoring": [
            "Đường huyết (HbA1c, glucose máu)",
            "Chức năng thận (eGFR, creatinine) - Trước khi bắt đầu và định kỳ",
            "Huyết áp (nguy cơ hạ huyết áp)",
            "Dấu hiệu nhiễm trùng tiết niệu, nhiễm nấm âm đạo",
            "Dấu hiệu DKA (đau bụng, buồn nôn, khó thở) - Đặc biệt khi bệnh nhân ốm, nhịn ăn, phẫu thuật"
    ],
        "precautions": [
            "Nguy cơ DKA (Diabetic Ketoacidosis) - Ngừng thuốc khi bệnh nhân ốm nặng, nhịn ăn, phẫu thuật",
            "Nguy cơ nhiễm nấm âm đạo cao ở phụ nữ - Giáo dục vệ sinh",
            "Nguy cơ hạ huyết áp - Thận trọng ở người cao tuổi, dùng lợi tiểu",
            "Không dùng cho đái tháo đường type 1 (tăng nguy cơ DKA)",
            "Giảm liều insulin/sulfonylurea khi bắt đầu dùng để tránh hạ đường huyết",
            "Lợi ích tim mạch và thận lớn hơn tác dụng giảm đường huyết"
    ],
        "black_box_warnings": None,
        "contraindications_detail": {
            "tuyệt_đối": [
                "Đái tháo đường type 1",
                "Nhiễm toan ceton do đái tháo đường",
                "Suy thận nặng (eGFR <20)",
                "Đang lọc máu",
                "Dị ứng empagliflozin"
    ],
            "tương_đối": [
                "Nhiễm trùng đường tiết niệu tái phát - tăng nguy cơ nhiễm trùng",
                "Suy tim nặng - tăng nguy cơ mất nước",
                "Người cao tuổi - tăng nguy cơ mất nước, hạ huyết áp",
                "Dùng diuretics - tăng nguy cơ mất nước",
                "Nhiễm trùng đường sinh dục tái phát - tăng nguy cơ nhiễm trùng"
    ],
        },
        "pregnancy": "C - Nguy cơ không thể loại trừ. Không khuyến nghị trong thai kỳ",
        "pharmacokinetics": {
            "half_life": "12.4 giờ",
            "onset": "1 giờ",
            "duration": "24 giờ",
            "protein_binding": "86%",
            "metabolism": "Gan (UGT1A9, UGT2B7, UGT1A3)",
            "clearance": "Thận (41.2% nguyên dạng), gan (chuyển hóa)"
        },
        "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm, tránh ánh sáng. Viên nén: bảo quản trong bao bì kín.",
        "drug_interactions": {
            "major": [
                {
                    "drug": "Diuretics (Furosemide, Hydrochlorothiazide, etc.)",
                    "mechanism": "Cả hai đều tăng thải nước và natri",
                    "effect": "Tăng nguy cơ mất nước, hạ huyết áp, suy thận cấp",
                    "management": "Theo dõi huyết áp và thể tích dịch. Có thể cần giảm liều diuretic hoặc tạm ngừng SGLT2i."
                }
            ],
            "moderate": [
                {
                    "drug": "Insulin, Sulfonylureas",
                    "mechanism": "SGLT2i tăng thải glucose qua nước tiểu, có thể tăng nguy cơ hạ đường huyết",
                    "effect": "Tăng nguy cơ hạ đường huyết",
                    "management": "Giảm liều insulin hoặc sulfonylurea khi bắt đầu SGLT2i. Theo dõi đường huyết chặt chẽ."
                },
                {
                    "drug": "ACE inhibitors, ARBs",
                    "mechanism": "Cả hai đều có thể ảnh hưởng đến chức năng thận",
                    "effect": "Tăng nguy cơ suy thận cấp (hiếm)",
                    "management": "Theo dõi eGFR và creatinine khi bắt đầu hoặc thay đổi liều."
                }
            ],
            "minor": [
                {
                    "drug": "Digoxin",
                    "mechanism": "SGLT2i có thể ảnh hưởng nhẹ đến nồng độ digoxin",
                    "effect": "Tăng nhẹ nồng độ digoxin",
                    "management": "Theo dõi nồng độ digoxin nếu dùng cùng."
                }
            ]
        },
        "pregnancy_lactation": {
            "fda_category": "C",
            "pregnancy_details": "Có thể gây hại cho thai nhi. Nghiên cứu trên động vật cho thấy có thể gây hại cho thai nhi. Không có nghiên cứu đầy đủ trên người. Không khuyến nghị dùng trong thai kỳ. Insulin là lựa chọn ưu tiên trong thai kỳ.",
            "lactation": {
                "safety": "Caution",
                "details": "Empagliflozin bài tiết vào sữa mẹ ở nồng độ thấp. Không có dữ liệu đầy đủ về an toàn cho trẻ bú mẹ.",
                "recommendation": "Thận trọng khi dùng khi cho con bú. Cân nhắc lợi ích/nguy cơ. Theo dõi trẻ bú mẹ nếu có dấu hiệu bất thường."
            }
        },
        "hepatic_adjustment": {
            "mild": "Không cần điều chỉnh liều",
            "moderate": "Không cần điều chỉnh liều",
            "severe": "Thận trọng, có thể cần giảm liều",
            "notes": "Empagliflozin chuyển hóa qua gan (UGT1A9, UGT2B7, UGT1A3). Suy gan nhẹ đến trung bình không cần điều chỉnh liều. Suy gan nặng có thể làm giảm chuyển hóa, tăng nồng độ thuốc."
        },
        "renal_adjustment": {
            "normal": "Không cần chỉnh liều",
            "30_60": "Có thể dùng nhưng cần điều chỉnh liều. Không dùng nếu eGFR <30.",
            "under_30": "CHỐNG CHỈ ĐỊNH nếu eGFR <20.",
            "dialysis": "CHỐNG CHỈ ĐỊNH. Không dùng khi đang lọc máu.",
            "notes": "Empagliflozin chống chỉ định ở suy thận nặng (eGFR <20). Cần kiểm tra eGFR trước khi bắt đầu và định kỳ. Ngừng thuốc nếu eGFR giảm xuống dưới 20."
        },
        "overdose_management": {
            "symptoms": [
                "Hạ đường huyết (nếu dùng với insulin hoặc sulfonylurea)",
                "Mất nước",
                "Hạ huyết áp",
                "Nhiễm toan ceton đái tháo đường (DKA) - đặc biệt euglycemic DKA",
                "Nhiễm trùng đường tiết niệu",
                "Nhiễm nấm âm đạo"
            ],
            "antidote": "Không có antidote đặc hiệu. Điều trị hỗ trợ: bù dịch, điều chỉnh đường huyết, điều trị DKA nếu có.",
            "treatment": [
                "Ngừng empagliflozin ngay lập tức",
                "Điều trị hạ đường huyết nếu có: Glucose PO hoặc IV (dextrose 50% 50ml IV)",
                "Bù dịch nếu mất nước: Normal saline IV",
                "Điều trị DKA nếu có: Insulin IV, bù dịch, bicarbonate nếu cần",
                "Điều trị nhiễm trùng đường tiết niệu hoặc nhiễm nấm nếu có",
                "Theo dõi đường huyết, điện giải, chức năng thận",
                "Theo dõi ít nhất 24-48 giờ"
            ],
            "monitoring": "Đường huyết, điện giải (Na, K, Cl, HCO3), chức năng thận (creatinine, eGFR), huyết áp, dấu hiệu DKA (ketone máu/nước tiểu), dấu hiệu nhiễm trùng"
        },
        "reversal_agents": {
            "available": False,
            "agents": [],
            "notes": "Không có antidote đặc hiệu. Điều trị quá liều chủ yếu là hỗ trợ: ngừng thuốc, bù dịch nếu mất nước, điều chỉnh đường huyết nếu hạ đường huyết, điều trị DKA nếu có."
        },
        "administration_instructions": {
            "oral": {
                "with_food": "Có thể uống với hoặc không thức ăn. Uống bất kỳ lúc nào trong ngày.",
                "timing": "Uống 1 lần/ngày vào buổi sáng. Uống cùng giờ mỗi ngày để dễ nhớ. Có thể uống đói hoặc no.",
                "notes": "Uống buổi sáng để tránh đi tiểu đêm. Uống với nhiều nước để giảm nguy cơ nhiễm trùng đường tiết niệu. Nếu quên liều, uống ngay khi nhớ ra, nhưng nếu gần đến liều tiếp theo thì bỏ qua liều đã quên và tiếp tục lịch trình bình thường."
            },
            "iv": {
                "reconstitution": "Không có dạng IV",
                "infusion_rate": "N/A",
                "compatibility": [],
                "incompatibility": [],
                "notes": "Chỉ có dạng uống (PO)"
            }
        },
        "references": {
            "primary_sources": [
                "FDA Drug Label - Jardiance (empagliflozin)",
                "UpToDate - Empagliflozin: Drug information",
                "EMPA-REG OUTCOME Study - New England Journal of Medicine (2015) - Empagliflozin trong đái tháo đường type 2 và bệnh tim mạch",
                "EMPEROR-Reduced Study - New England Journal of Medicine (2020) - Empagliflozin trong suy tim",
                "EMPA-KIDNEY Study - New England Journal of Medicine (2023) - Empagliflozin trong bệnh thận mạn",
                "American Diabetes Association guidelines - SGLT2 inhibitors"
            ],
            "last_updated": "2025-02-18",
            "evidence_level": "High - Multiple large RCTs (EMPA-REG OUTCOME, EMPEROR-Reduced, EMPA-KIDNEY) showing cardiovascular and renal benefits"
        },
            "risk_flags": {
                "high_alert": False,
                "narrow_therapeutic_index": False,
                "bleeding_risk": False,
                "organ_toxicity": ["genitourinary"],
                "qt_prolongation": False,
                "hepatotoxicity": False,
                "nephrotoxicity": False,
                "requires_monitoring": ["eGFR", "Genital/urinary infections"],
            },
            "guideline_tags": [
                "ADA 2024 Standards of Care - Diabetes",
                "AACE/ACE 2023 Type 2 Diabetes Guidelines",
                "FDA Black Box Warning - Fournier's Gangrene (rare)",
            ]
    },
    "Dapagliflozin":     {
        "group": "Diabetes - SGLT2 Inhibitor",
        "vietnamese_name": "Dapagliflozin, Forxiga",
        "brand_names": {
            "common": [
                "Forxiga",
                "Farxiga"
    ],
            "vietnam": [
                "Forxiga 5/10mg"
    ],
        },
        "administration": [
            "PO"
    ],
        "indications": [
            "Đái tháo đường type 2",
            "Suy tim (HFrEF, HFmrEF, HFpEF) - Chỉ định mới",
            "Bệnh thận mạn (CKD) - Chỉ định mới"
    ],
        "dosage": {
            "adult_start": "5mg PO x 1 lần/ngày vào buổi sáng",
            "adult_usual": "5-10mg PO x 1 lần/ngày vào buổi sáng. Thường 5mg/ngày, có thể tăng lên 10mg nếu cần.",
            "adult_max": "10mg/ngày",
            "dm_t2": "Khởi đầu 5mg PO x 1 lần/ngày vào buổi sáng. Có thể tăng lên 10mg sau ít nhất 2-4 tuần nếu cần và dung nạp tốt. Tối đa 10mg/ngày.",
            "heart_failure": "10mg PO x 1 lần/ngày (không phụ thuộc đái tháo đường). Dựa trên DAPA-HF (HFrEF), DELIVER (HFpEF) trials. Giảm tử vong tim mạch và nhập viện do suy tim ở cả HFrEF, HFmrEF, và HFpEF.",
            "ckd": "10mg PO x 1 lần/ngày (eGFR ≥25, không phụ thuộc đái tháo đường). Dựa trên DAPA-CKD trial. Làm chậm tiến triển bệnh thận mạn và giảm biến cố tim mạch. CHỐNG CHỈ ĐỊNH nếu eGFR <25.",
            "elderly": "Khởi đầu 5mg PO x 1 lần/ngày vào buổi sáng, tăng dần chậm. Người cao tuổi nhạy cảm hơn với tác dụng phụ (mất nước, hạ huyết áp).",
            "pregnancy": "Không khuyến nghị trong thai kỳ. Insulin là lựa chọn ưu tiên trong thai kỳ.",
            "renal_adjustment_dosage": {
                "normal": "5-10mg PO x 1 lần/ngày (eGFR ≥60)",
                "45_60": "5mg PO x 1 lần/ngày (eGFR 45-60). Có thể tăng lên 10mg nếu cần và dung nạp tốt.",
                "25_45": "5mg PO x 1 lần/ngày (eGFR 25-45). Không tăng liều lên 10mg. Theo dõi chức năng thận thường xuyên.",
                "under_25": "CHỐNG CHỈ ĐỊNH (eGFR <25)",
                "dialysis": "CHỐNG CHỈ ĐỊNH"
            },
            "hepatic_adjustment_dosage": {
                "mild": "5-10mg PO x 1 lần/ngày. Không cần điều chỉnh liều đặc biệt.",
                "moderate": "5-10mg PO x 1 lần/ngày. Không cần điều chỉnh liều đặc biệt. Theo dõi chức năng gan.",
                "severe": "Thận trọng, có thể cần giảm liều. Khởi đầu 5mg/ngày, tăng dần chậm. Theo dõi chức năng gan chặt chẽ."
            },
            "administration_route": "PO (uống)",
            "frequency": "1 lần/ngày",
            "with_food": "Có thể uống với hoặc không thức ăn. Uống bất kỳ lúc nào trong ngày, nhưng nên uống vào buổi sáng để tránh đi tiểu đêm.",
            "timing": "Uống 1 lần/ngày vào buổi sáng. Uống cùng giờ mỗi ngày để dễ nhớ. Có thể uống đói hoặc no. Uống với nhiều nước để giảm nguy cơ nhiễm trùng đường tiết niệu.",
            "titration": "Tăng liều từ từ: Tuần 1-4: 5mg/ngày. Tuần 5+: 10mg/ngày (nếu cần và dung nạp tốt). Đánh giá hiệu quả sau mỗi 2-4 tuần. Không tăng liều nếu eGFR <45.",
            "notes": "Uống buổi sáng. Tương tự Empagliflozin về cơ chế và tác dụng phụ. Chỉ định mở rộng: Suy tim (HFrEF, HFmrEF, HFpEF) và bệnh thận mạn (CKD) không phụ thuộc đái tháo đường. CHỐNG CHỈ ĐỊNH nếu eGFR <25. Ngừng thuốc khi bệnh nhân ốm nặng, nhịn ăn, phẫu thuật để tránh DKA."
        },
        "side_effects": [
            "Nhiễm nấm âm đạo (Phụ nữ)",
            "Nhiễm trùng đường tiết niệu",
            "Đa niệu",
            "Hạ huyết áp",
            "DKA (Hiếm)"
    ],
        "mechanism_of_action": """Ức chế SGLT2 ở thận, tương tự Empagliflozin. Lợi ích tim mạch và thận đã được chứng minh (DAPA-HF, DAPA-CKD trials).""",
        "monitoring": [
            "Đường huyết, eGFR, huyết áp",
            "Dấu hiệu nhiễm trùng, DKA"
    ],
        "black_box_warnings": None,
        "contraindications_detail": {
            "tuyệt_đối": [
                "Đái tháo đường type 1",
                "Nhiễm toan ceton do đái tháo đường",
                "Suy thận nặng (eGFR <25)",
                "Đang lọc máu",
                "Dị ứng dapagliflozin"
    ],
            "tương_đối": [
                "Nhiễm trùng đường tiết niệu tái phát - tăng nguy cơ nhiễm trùng",
                "Suy tim nặng - tăng nguy cơ mất nước",
                "Người cao tuổi - tăng nguy cơ mất nước, hạ huyết áp",
                "Dùng diuretics - tăng nguy cơ mất nước",
                "Nhiễm trùng đường sinh dục tái phát - tăng nguy cơ nhiễm trùng"
    ],
        },
        "contraindications": [],
        "interactions": [],
        "pregnancy": "C - Nguy cơ không thể loại trừ. Không khuyến nghị trong thai kỳ",
        "precautions": [
            "Nguy cơ DKA (Diabetic Ketoacidosis) - Ngừng thuốc khi bệnh nhân ốm nặng, nhịn ăn, phẫu thuật",
            "Nguy cơ nhiễm nấm âm đạo cao ở phụ nữ - Giáo dục vệ sinh",
            "Nguy cơ hạ huyết áp - Thận trọng ở người cao tuổi, dùng lợi tiểu",
            "Không dùng cho đái tháo đường type 1 (tăng nguy cơ DKA)",
            "Giảm liều insulin/sulfonylurea khi bắt đầu dùng để tránh hạ đường huyết",
            "Lợi ích tim mạch và thận lớn hơn tác dụng giảm đường huyết"
        ],
        "pharmacokinetics": {
            "half_life": "12.9 giờ",
            "onset": "1 giờ",
            "duration": "24 giờ",
            "protein_binding": "91%",
            "metabolism": "Gan (UGT1A9 chủ yếu)",
            "clearance": "Thận (75% nguyên dạng), gan (chuyển hóa)"
        },
        "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm, tránh ánh sáng. Viên nén: bảo quản trong bao bì kín.",
        "drug_interactions": {
            "major": [
                {
                    "drug": "Diuretics (Furosemide, Hydrochlorothiazide, etc.)",
                    "mechanism": "Cả hai đều tăng thải nước và natri",
                    "effect": "Tăng nguy cơ mất nước, hạ huyết áp, suy thận cấp",
                    "management": "Theo dõi huyết áp và thể tích dịch. Có thể cần giảm liều diuretic hoặc tạm ngừng SGLT2i."
                }
            ],
            "moderate": [
                {
                    "drug": "Insulin, Sulfonylureas",
                    "mechanism": "SGLT2i tăng thải glucose qua nước tiểu, có thể tăng nguy cơ hạ đường huyết",
                    "effect": "Tăng nguy cơ hạ đường huyết",
                    "management": "Giảm liều insulin hoặc sulfonylurea khi bắt đầu SGLT2i. Theo dõi đường huyết chặt chẽ."
                },
                {
                    "drug": "ACE inhibitors, ARBs",
                    "mechanism": "Cả hai đều có thể ảnh hưởng đến chức năng thận",
                    "effect": "Tăng nguy cơ suy thận cấp (hiếm)",
                    "management": "Theo dõi eGFR và creatinine khi bắt đầu hoặc thay đổi liều."
                }
            ],
            "minor": [
                {
                    "drug": "Digoxin",
                    "mechanism": "SGLT2i có thể ảnh hưởng nhẹ đến nồng độ digoxin",
                    "effect": "Tăng nhẹ nồng độ digoxin",
                    "management": "Theo dõi nồng độ digoxin nếu dùng cùng."
                }
            ]
        },
        "pregnancy_lactation": {
            "fda_category": "C",
            "pregnancy_details": "Có thể gây hại cho thai nhi. Nghiên cứu trên động vật cho thấy có thể gây hại cho thai nhi. Không có nghiên cứu đầy đủ trên người. Không khuyến nghị dùng trong thai kỳ. Insulin là lựa chọn ưu tiên trong thai kỳ.",
            "lactation": {
                "safety": "Caution",
                "details": "Dapagliflozin bài tiết vào sữa mẹ ở nồng độ thấp. Không có dữ liệu đầy đủ về an toàn cho trẻ bú mẹ.",
                "recommendation": "Thận trọng khi dùng khi cho con bú. Cân nhắc lợi ích/nguy cơ. Theo dõi trẻ bú mẹ nếu có dấu hiệu bất thường."
            }
        },
        "hepatic_adjustment": {
            "mild": "Không cần điều chỉnh liều",
            "moderate": "Không cần điều chỉnh liều",
            "severe": "Thận trọng, có thể cần giảm liều",
            "notes": "Dapagliflozin chuyển hóa qua gan (UGT1A9). Suy gan nhẹ đến trung bình không cần điều chỉnh liều. Suy gan nặng có thể làm giảm chuyển hóa, tăng nồng độ thuốc."
        },
        "renal_adjustment": {
            "normal": "Không cần chỉnh liều",
            "30_60": "Có thể dùng nhưng cần điều chỉnh liều. Không dùng nếu eGFR <30.",
            "under_30": "CHỐNG CHỈ ĐỊNH nếu eGFR <25.",
            "dialysis": "CHỐNG CHỈ ĐỊNH. Không dùng khi đang lọc máu.",
            "notes": "Dapagliflozin chống chỉ định ở suy thận nặng (eGFR <25). Cần kiểm tra eGFR trước khi bắt đầu và định kỳ. Ngừng thuốc nếu eGFR giảm xuống dưới 25."
        },
        "overdose_management": {
            "symptoms": [
                "Hạ đường huyết (nếu dùng với insulin hoặc sulfonylurea)",
                "Mất nước",
                "Hạ huyết áp",
                "Nhiễm toan ceton đái tháo đường (DKA) - đặc biệt euglycemic DKA",
                "Nhiễm trùng đường tiết niệu",
                "Nhiễm nấm âm đạo"
            ],
            "antidote": "Không có antidote đặc hiệu. Điều trị hỗ trợ: bù dịch, điều chỉnh đường huyết, điều trị DKA nếu có.",
            "treatment": [
                "Ngừng dapagliflozin ngay lập tức",
                "Điều trị hạ đường huyết nếu có: Glucose PO hoặc IV (dextrose 50% 50ml IV)",
                "Bù dịch nếu mất nước: Normal saline IV",
                "Điều trị DKA nếu có: Insulin IV, bù dịch, bicarbonate nếu cần",
                "Điều trị nhiễm trùng đường tiết niệu hoặc nhiễm nấm nếu có",
                "Theo dõi đường huyết, điện giải, chức năng thận",
                "Theo dõi ít nhất 24-48 giờ"
            ],
            "monitoring": "Đường huyết, điện giải (Na, K, Cl, HCO3), chức năng thận (creatinine, eGFR), huyết áp, dấu hiệu DKA (ketone máu/nước tiểu), dấu hiệu nhiễm trùng"
        },
        "reversal_agents": {
            "available": False,
            "agents": [],
            "notes": "Không có antidote đặc hiệu. Điều trị quá liều chủ yếu là hỗ trợ: ngừng thuốc, bù dịch nếu mất nước, điều chỉnh đường huyết nếu hạ đường huyết, điều trị DKA nếu có."
        },
        "administration_instructions": {
            "oral": {
                "with_food": "Có thể uống với hoặc không thức ăn. Uống bất kỳ lúc nào trong ngày.",
                "timing": "Uống 1 lần/ngày vào buổi sáng. Uống cùng giờ mỗi ngày để dễ nhớ. Có thể uống đói hoặc no.",
                "notes": "Uống buổi sáng để tránh đi tiểu đêm. Uống với nhiều nước để giảm nguy cơ nhiễm trùng đường tiết niệu. Nếu quên liều, uống ngay khi nhớ ra, nhưng nếu gần đến liều tiếp theo thì bỏ qua liều đã quên và tiếp tục lịch trình bình thường."
            },
            "iv": {
                "reconstitution": "Không có dạng IV",
                "infusion_rate": "N/A",
                "compatibility": [],
                "incompatibility": [],
                "notes": "Chỉ có dạng uống (PO)"
            }
        },
        "references": {
            "primary_sources": [
                "FDA Drug Label - Farxiga (dapagliflozin)",
                "UpToDate - Dapagliflozin: Drug information",
                "DAPA-HF Study - New England Journal of Medicine (2019) - Dapagliflozin trong suy tim",
                "DAPA-CKD Study - New England Journal of Medicine (2020) - Dapagliflozin trong bệnh thận mạn",
                "DECLARE-TIMI 58 Study - New England Journal of Medicine (2019) - Dapagliflozin trong đái tháo đường type 2 và bệnh tim mạch",
                "American Diabetes Association guidelines - SGLT2 inhibitors"
            ],
            "last_updated": "2025-02-18",
            "evidence_level": "High - Multiple large RCTs (DAPA-HF, DAPA-CKD, DECLARE-TIMI 58) showing cardiovascular and renal benefits"
        },
            "risk_flags": {
                "high_alert": False,
                "narrow_therapeutic_index": False,
                "bleeding_risk": False,
                "organ_toxicity": ["genitourinary"],
                "qt_prolongation": False,
                "hepatotoxicity": False,
                "nephrotoxicity": False,
                "requires_monitoring": ["eGFR", "Genital/urinary infections"],
            },
            "guideline_tags": [
                "ADA 2024 Standards of Care - Diabetes",
                "AACE/ACE 2023 Type 2 Diabetes Guidelines",
                "FDA Black Box Warning - Fournier's Gangrene (rare)",
            ]
    },
    "Canagliflozin":     {
        "group": "Diabetes - SGLT2 Inhibitor",
        "vietnamese_name": "Canagliflozin, Invokana",
        "brand_names": {
            "common": [
                "Invokana"
    ],
            "vietnam": [
                "Invokana 100/300mg"
    ],
        },
        "administration": [
            "PO"
    ],
        "indications": [
            "Đái tháo đường type 2",
            "Giảm nguy cơ biến cố tim mạch ở bệnh nhân đái tháo đường type 2 có bệnh tim mạch"
    ],
        "dosage": {
            "adult_start": "100mg PO x 1 lần/ngày trước bữa ăn đầu tiên",
            "adult_usual": "100-300mg PO x 1 lần/ngày trước bữa ăn đầu tiên. Thường 100mg/ngày, có thể tăng lên 300mg nếu eGFR ≥60 và cần.",
            "adult_max": "300mg/ngày (chỉ khi eGFR ≥60)",
            "dm_t2": "Khởi đầu 100mg PO x 1 lần/ngày trước bữa ăn đầu tiên. Có thể tăng lên 300mg sau ít nhất 2-4 tuần nếu eGFR ≥60 và cần. Tối đa 300mg/ngày (chỉ khi eGFR ≥60). Không tăng liều nếu eGFR <60.",
            "cardiovascular_benefit": "100mg PO x 1 lần/ngày (CANVAS trial) - giảm biến cố tim mạch lớn ở bệnh nhân đái tháo đường type 2 có bệnh tim mạch hoặc yếu tố nguy cơ tim mạch.",
            "ckd_benefit": "100mg PO x 1 lần/ngày (CREDENCE trial) - làm chậm tiến triển bệnh thận mạn ở bệnh nhân đái tháo đường type 2 có bệnh thận mạn.",
            "elderly": "Khởi đầu 100mg PO x 1 lần/ngày trước bữa ăn đầu tiên, tăng dần chậm. Người cao tuổi nhạy cảm hơn với tác dụng phụ (mất nước, hạ huyết áp). Không tăng liều lên 300mg nếu eGFR <60.",
            "pregnancy": "Không khuyến nghị trong thai kỳ. Insulin là lựa chọn ưu tiên trong thai kỳ.",
            "renal_adjustment_dosage": {
                "normal": "100-300mg PO x 1 lần/ngày (eGFR ≥60). Có thể tăng lên 300mg nếu cần.",
                "45_60": "100mg PO x 1 lần/ngày (eGFR 45-60). KHÔNG tăng liều lên 300mg. Theo dõi chức năng thận thường xuyên.",
                "30_45": "100mg PO x 1 lần/ngày (eGFR 30-45). KHÔNG tăng liều lên 300mg. Theo dõi chức năng thận thường xuyên.",
                "under_30": "CHỐNG CHỈ ĐỊNH (eGFR <30)",
                "dialysis": "CHỐNG CHỈ ĐỊNH"
            },
            "hepatic_adjustment_dosage": {
                "mild": "100-300mg PO x 1 lần/ngày (nếu eGFR ≥60). Không cần điều chỉnh liều đặc biệt.",
                "moderate": "100mg PO x 1 lần/ngày. Không cần điều chỉnh liều đặc biệt. Theo dõi chức năng gan.",
                "severe": "Thận trọng, có thể cần giảm liều. Khởi đầu 100mg/ngày, không tăng liều. Theo dõi chức năng gan chặt chẽ."
            },
            "administration_route": "PO (uống)",
            "frequency": "1 lần/ngày",
            "with_food": "Uống trước bữa ăn đầu tiên trong ngày. Uống với nhiều nước để giảm nguy cơ nhiễm trùng đường tiết niệu.",
            "timing": "Uống 1 lần/ngày trước bữa ăn đầu tiên trong ngày (thường buổi sáng). Uống cùng giờ mỗi ngày để dễ nhớ. Uống với nhiều nước.",
            "titration": "Tăng liều từ từ: Tuần 1-4: 100mg/ngày. Tuần 5+: 300mg/ngày (chỉ nếu eGFR ≥60 và cần). Đánh giá hiệu quả sau mỗi 2-4 tuần. KHÔNG tăng liều nếu eGFR <60.",
            "notes": "Uống trước bữa ăn đầu tiên trong ngày. Không tăng liều nếu eGFR <60. Lưu ý: Có cảnh báo FDA về nguy cơ gãy xương và cắt cụt chi dưới (hiếm, chủ yếu ở bệnh nhân có bệnh mạch máu ngoại vi). Ngừng thuốc nếu có loét chân, nhiễm trùng chân, đau chân. CHỐNG CHỈ ĐỊNH nếu eGFR <30. Ngừng thuốc khi bệnh nhân ốm nặng, nhịn ăn, phẫu thuật để tránh DKA."
        },
        "side_effects": [
            "Nhiễm nấm âm đạo",
            "Nhiễm trùng tiết niệu",
            "Đa niệu",
            "Hạ huyết áp",
            "Tăng nguy cơ gãy xương (Cảnh báo FDA)",
            "Tăng nguy cơ cắt cụt chi dưới (Cảnh báo FDA - Hiếm)",
            "DKA"
    ],
        "mechanism_of_action": """Ức chế SGLT2, tương tự các SGLT2i khác. Lợi ích tim mạch và thận (CANVAS, CREDENCE trials). Lưu ý: Có cảnh báo về nguy cơ gãy xương và cắt cụt chi dưới (hiếm).""",
        "monitoring": [
            "Đường huyết, eGFR, huyết áp",
            "Dấu hiệu nhiễm trùng, DKA",
            "Dấu hiệu đau chân, loét chân (nguy cơ cắt cụt)"
    ],
        "black_box_warnings": """Cảnh báo FDA về tăng nguy cơ cắt cụt chi dưới (hiếm, chủ yếu ở bệnh nhân có bệnh mạch máu ngoại vi). Ngừng thuốc nếu có loét chân, nhiễm trùng chân.""",
        "contraindications_detail": {
            "tuyệt_đối": [
                "Dị ứng với canagliflozin hoặc SGLT2 inhibitor",
                "Suy thận nặng (eGFR <30 mL/min)",
                "Nhiễm toan ceton do đái tháo đường"
    ],
            "tương_đối": [
                "Suy thận vừa (eGFR 30-60, cần điều chỉnh liều)",
                "Suy tim nặng",
                "Nhiễm trùng đường tiết niệu tái phát",
                "Nhiễm nấm sinh dục"
    ],
        },
        "contraindications": [],
        "interactions": [],
        "pregnancy": "C - Nguy cơ không thể loại trừ. Không khuyến nghị trong thai kỳ",
        "precautions": [],
        "pharmacokinetics": {
        },
        "storage": "",
        "drug_interactions": {
            "major": [
                {
                    "drug": "Diuretics (Furosemide, Hydrochlorothiazide, etc.)",
                    "mechanism": "Cả hai đều tăng thải nước và natri",
                    "effect": "Tăng nguy cơ mất nước, hạ huyết áp, suy thận cấp",
                    "management": "Theo dõi huyết áp và thể tích dịch. Có thể cần giảm liều diuretic hoặc tạm ngừng SGLT2i."
                }
            ],
            "moderate": [
                {
                    "drug": "Insulin, Sulfonylureas",
                    "mechanism": "SGLT2i tăng thải glucose qua nước tiểu, có thể tăng nguy cơ hạ đường huyết",
                    "effect": "Tăng nguy cơ hạ đường huyết",
                    "management": "Giảm liều insulin hoặc sulfonylurea khi bắt đầu SGLT2i. Theo dõi đường huyết chặt chẽ."
                },
                {
                    "drug": "ACE inhibitors, ARBs",
                    "mechanism": "Cả hai đều có thể ảnh hưởng đến chức năng thận",
                    "effect": "Tăng nguy cơ suy thận cấp (hiếm)",
                    "management": "Theo dõi eGFR và creatinine khi bắt đầu hoặc thay đổi liều."
                }
            ],
            "minor": [
                {
                    "drug": "Digoxin",
                    "mechanism": "SGLT2i có thể ảnh hưởng nhẹ đến nồng độ digoxin",
                    "effect": "Tăng nhẹ nồng độ digoxin",
                    "management": "Theo dõi nồng độ digoxin nếu dùng cùng."
                }
            ]
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
            "normal": "Không cần chỉnh liều",
            "30_60": "Có thể dùng nhưng cần điều chỉnh liều. Không tăng liều lên 300mg nếu eGFR <60.",
            "under_30": "CHỐNG CHỈ ĐỊNH nếu eGFR <30.",
            "dialysis": "CHỐNG CHỈ ĐỊNH. Không dùng khi đang lọc máu.",
            "notes": "Canagliflozin chống chỉ định ở suy thận nặng (eGFR <30). Không tăng liều lên 300mg nếu eGFR <60. Cần kiểm tra eGFR trước khi bắt đầu và định kỳ. Ngừng thuốc nếu eGFR giảm xuống dưới 30."
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
            "notes": "Không có antidote đặc hiệu. Điều trị quá liều chủ yếu là hỗ trợ: ngừng thuốc, bù dịch nếu mất nước, điều chỉnh đường huyết nếu hạ đường huyết, điều trị DKA nếu có."
        },
        "administration_instructions": {
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
                "organ_toxicity": ["genitourinary"],
                "qt_prolongation": False,
                "hepatotoxicity": False,
                "nephrotoxicity": False,
                "requires_monitoring": ["eGFR", "Genital/urinary infections"],
            },
            "guideline_tags": [
                "ADA 2024 Standards of Care - Diabetes",
                "AACE/ACE 2023 Type 2 Diabetes Guidelines",
                "FDA Black Box Warning - Fournier's Gangrene (rare)",
            ]
    },
}
