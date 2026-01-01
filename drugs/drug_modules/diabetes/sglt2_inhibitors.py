"""
SGLT2 Inhibitors (Thuốc ức chế SGLT2)
Nhóm thuốc mới nhất cho đái tháo đường type 2, có lợi ích tim mạch và thận đã được chứng minh.
"""

SGLT2_INHIBITORS_DRUGS = {
    "Empagliflozin": {
        "group": "Diabetes - SGLT2 Inhibitor",
        "vietnamese_name": "Empagliflozin, Jardiance",
        "brand_names": {
            "common": ["Jardiance"],
            "vietnam": ["Jardiance 10/25mg"]
        },
        "administration": ["PO"],
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
            "dm_t2": "Khởi đầu 10mg x 1 lần/sáng. Có thể tăng lên 25mg nếu cần.",
            "heart_failure": "10mg x 1 lần/ngày (không phụ thuộc đái tháo đường).",
            "notes": "Uống buổi sáng, có thể uống đói hoặc no. Tác dụng giảm đường huyết nhẹ (HbA1c ~0.5-0.8%) nhưng lợi ích tim mạch và thận rất lớn."
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
        "mechanism_of_action": "Ức chế SGLT2 (Sodium-Glucose Cotransporter 2) ở ống lượn gần thận, ngăn tái hấp thu glucose → Glucose thải qua nước tiểu (glucosuria) → Giảm đường huyết. Lợi ích tim mạch: Giảm tử vong tim mạch, nhập viện do suy tim (EMPA-REG OUTCOME trial). Lợi ích thận: Làm chậm tiến triển bệnh thận mạn.",
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
        "black_box_warnings": "Nguy cơ nhiễm toan ceton đái tháo đường (DKA), có thể xảy ra ngay cả khi đường huyết bình thường. Ngừng thuốc khi bệnh nhân ốm nặng, nhịn ăn, phẫu thuật."
    },

    "Dapagliflozin": {
        "group": "Diabetes - SGLT2 Inhibitor",
        "vietnamese_name": "Dapagliflozin, Forxiga",
        "brand_names": {
            "common": ["Forxiga", "Farxiga"],
            "vietnam": ["Forxiga 5/10mg"]
        },
        "administration": ["PO"],
        "indications": [
            "Đái tháo đường type 2",
            "Suy tim (HFrEF, HFmrEF, HFpEF) - Chỉ định mới",
            "Bệnh thận mạn (CKD) - Chỉ định mới"
        ],
        "dosage": {
            "dm_t2": "Khởi đầu 5mg x 1 lần/sáng. Có thể tăng lên 10mg nếu cần.",
            "heart_failure": "10mg x 1 lần/ngày.",
            "ckd": "10mg x 1 lần/ngày.",
            "notes": "Uống buổi sáng. Tương tự Empagliflozin về cơ chế và tác dụng phụ."
        },
        "side_effects": [
            "Nhiễm nấm âm đạo (Phụ nữ)",
            "Nhiễm trùng đường tiết niệu",
            "Đa niệu",
            "Hạ huyết áp",
            "DKA (Hiếm)"
        ],
        "mechanism_of_action": "Ức chế SGLT2 ở thận, tương tự Empagliflozin. Lợi ích tim mạch và thận đã được chứng minh (DAPA-HF, DAPA-CKD trials).",
        "monitoring": [
            "Đường huyết, eGFR, huyết áp",
            "Dấu hiệu nhiễm trùng, DKA"
        ]
    },

    "Canagliflozin": {
        "group": "Diabetes - SGLT2 Inhibitor",
        "vietnamese_name": "Canagliflozin, Invokana",
        "brand_names": {
            "common": ["Invokana"],
            "vietnam": ["Invokana 100/300mg"]
        },
        "administration": ["PO"],
        "indications": [
            "Đái tháo đường type 2",
            "Giảm nguy cơ biến cố tim mạch ở bệnh nhân đái tháo đường type 2 có bệnh tim mạch"
        ],
        "dosage": {
            "dm_t2": "Khởi đầu 100mg x 1 lần/sáng trước bữa ăn đầu tiên. Có thể tăng lên 300mg nếu eGFR ≥60.",
            "notes": "Uống trước bữa ăn đầu tiên trong ngày. Không tăng liều nếu eGFR <60."
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
        "mechanism_of_action": "Ức chế SGLT2, tương tự các SGLT2i khác. Lợi ích tim mạch và thận (CANVAS, CREDENCE trials). Lưu ý: Có cảnh báo về nguy cơ gãy xương và cắt cụt chi dưới (hiếm).",
        "monitoring": [
            "Đường huyết, eGFR, huyết áp",
            "Dấu hiệu nhiễm trùng, DKA",
            "Dấu hiệu đau chân, loét chân (nguy cơ cắt cụt)"
        ],
        "black_box_warnings": "Cảnh báo FDA về tăng nguy cơ cắt cụt chi dưới (hiếm, chủ yếu ở bệnh nhân có bệnh mạch máu ngoại vi). Ngừng thuốc nếu có loét chân, nhiễm trùng chân."
    }
}
