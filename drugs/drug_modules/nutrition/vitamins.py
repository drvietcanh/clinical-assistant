"""
Vitamins & Minerals (Dinh dưỡng & Khoáng chất)
"""

VITAMINS_DRUGS = {
    "Thiamine (Vitamin B1)": {
        "group": "Nutrition - Vitamin B",
        "vietnamese_name": "Vitamin B1, Thiamine",
        "brand_names": {
            "common": ["Vitamin B1"],
            "vietnam": ["Vitamin B1 250mg", "Vinpharlife B1"]
        },
        "administration": ["PO", "IV", "IM"],
        "indications": [
            "Bệnh Beriberi (tê phù)",
            "Hội chứng Wernicke-Korsakoff (người nghiện rượu)",
            "Dự phòng thiếu hụt B1 ở người nghiện rượu (trước khi truyền đường)"
        ],
        "dosage": {
            "wernicke_treatment": "500 mg IV mỗi 8 giờ x 2-3 ngày. (Pha loãng truyền chậm).",
            "prophylaxis_alcohol_withdrawal": "100 mg PO/IV/IM hàng ngày.",
            "notes": "Rất quan trọng: Phải tiêm B1 TRƯỚC khi truyền Glucose cho người nghiện rượu để tránh làm nặng thêm bệnh não Wernicke."
        },
        "side_effects": ["Phản ứng dị ứng (hiếm, chủ yếu tiêm nhanh)", "Đau tại chỗ tiêm"],
        "storage": "Tránh ánh sáng."
    },

    "Pyridoxine (Vitamin B6)": {
        "group": "Nutrition - Vitamin B",
        "vietnamese_name": "Vitamin B6, Pyridoxine",
        "brand_names": {
             "vietnam": ["Vitamin B6"]
        },
        "administration": ["PO", "IV", "IM"],
        "indications": [
            "Dự phòng bệnh thần kinh ngoại biên do Isoniazid (INH)",
            "Ngộ độc Isoniazid (liều cao)",
            "Nôn nghén (thai kỳ)"
        ],
        "dosage": {
            "inh_prophylaxis": "10-25 mg/ngày (tối đa 50mg).",
            "inh_poisoning": "Liều ngang bằng lượng INH đã uống (gram-for-gram). Nếu không rõ, dùng 5g IV.",
            "pregnancy_nausea": "10-25 mg mỗi 8 giờ."
        },
        "side_effects": ["Bệnh thần kinh ngoại biên (nếu dùng liều >200mg/ngày kéo dài) - Paradoxical effect"],
        "pregnancy": "A"
    },

    "Cyanocobalamin (Vitamin B12)": {
        "group": "Nutrition - Vitamin B",
        "vietnamese_name": "Vitamin B12",
        "brand_names": {
            "vietnam": ["Vitamin B12 1000mcg"]
        },
        "administration": ["IM", "SC", "PO", "Intranasal"],
        "indications": [
            "Thiếu máu hồng cầu to (Pernicious anemia)",
            "Thiếu hụt B12 (người ăn chay trường, cắt dạ dày)",
            "Ngộ độc Cyanide (dạng Hydroxocobalamin)"
        ],
        "dosage": {
            "deficiency_treatment": "1000 mcg IM mỗi ngày x 1 tuần, sau đó 1 tuần/lần x 4 tuần, sau đó 1 tháng/lần.",
            "notes": "Oral absorption kém ở người thiếu yếu tố nội tại (Pernicious anemia) -> Bắt buộc tiêm."
        }
    },

    "Vitamin C (Ascorbic Acid)": {
        "group": "Nutrition - Vitamin",
        "vietnamese_name": "Vitamin C, Ascorbic Acid",
        "brand_names": {
            "common": ["Laroscorbine"],
            "vietnam": ["Vitamin C 500mg/1g", "Ceplin"]
        },
        "administration": ["PO", "IV", "IM"],
        "indications": [
            "Bệnh Scorbut (Scurvy)",
            "Hỗ trợ mau lành vết thương",
            "Methemoglobinemia (thay thế Methylene Blue nếu chống chỉ định dung nạp kém hơn)"
        ],
        "contraindications": [
            "Sỏi thận oxalate (liều cao)",
            "Thiếu G6PD (liều cao IV gây tan máu)"
        ],
        "dosage": {
            "scurvy": "100-250 mg x 1-2 lần/ngày.",
            "notes": "Liều cao acid hóa nước tiểu -> tăng nguy cơ sỏi oxalate."
        }
    },

    "Vitamin D3 (Cholecalciferol)": {
        "group": "Nutrition - Vitamin",
        "vietnamese_name": "Vitamin D3",
        "brand_names": {
            "vietnam": ["Aquadetrim", "D3 B.O.N"]
        },
        "administration": ["PO", "IM"],
        "indications": [
            "Loãng xương (Osteoporosis) - phối hợp Calci",
            "Còi xương (Rickets)",
            "Thiếu Vitamin D"
        ],
        "dosage": {
            "osteoporosis": "800-1000 IU/ngày (kèm Calci 1000-1200mg).",
            "deficiency_treatment": "50,000 IU mỗi tuần x 8 tuần (liều tải), sau đó duy trì.",
            "notes": "Cần chức năng thận để chuyển hóa thành dạng hoạt động (Calcitriol). Nếu suy thận nặng -> dùng Calcitriol."
        },
        "monitoring": ["Nồng độ 25(OH)D máu", "Calci máu"]
    }
}
