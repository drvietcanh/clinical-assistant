"""
Thyroid Medications (Thuốc tuyến giáp)
Bao gồm: Hormone tuyến giáp, thuốc kháng giáp.
"""

THYROID_DRUGS = {
    "Levothyroxine": {
        "group": "Endocrinology - Thyroid Hormone",
        "vietnamese_name": "Levothyroxine, L-Thyroxine, T4",
        "brand_names": {
            "common": ["Synthroid", "Levoxyl", "Euthyrox"],
            "vietnam": ["Euthyrox 50/100mcg", "L-Thyroxine"]
        },
        "administration": ["PO"],
        "indications": [
            "Suy giáp (Hypothyroidism)",
            "Bướu giáp (Goiter)",
            "Ung thư tuyến giáp (sau phẫu thuật)"
        ],
        "contraindications": [
            "Cường giáp chưa điều trị",
            "Nhồi máu cơ tim cấp",
            "Suy thượng thận chưa điều trị"
        ],
        "dosage": {
            "hypothyroidism": "Khởi đầu 25-50mcg/ngày (12.5-25mcg ở người cao tuổi/bệnh tim). Tăng dần 12.5-25mcg mỗi 4-6 tuần. Liều duy trì: 100-200mcg/ngày.",
            "notes": "Uống lúc đói (30-60 phút trước ăn sáng). Điều chỉnh liều theo TSH (target TSH 0.5-2.5 mIU/L)."
        },
        "side_effects": [
            "Liều quá cao (Cường giáp iatrogen): Tim đập nhanh, run tay, giảm cân, mất ngủ, lo âu",
            "Loãng xương (nếu TSH bị ức chế quá mức)",
            "Rối loạn nhịp tim (ở người cao tuổi)"
        ],
        "interactions": [
            "Sắt, Calci, PPI, Sucralfate: Giảm hấp thu levothyroxine (uống cách xa ≥4h).",
            "Estrogen, Tamoxifen: Tăng nhu cầu levothyroxine.",
            "Warfarin: Tăng INR (cần theo dõi).",
            "Amiodarone: Ảnh hưởng chuyển hóa T4→T3."
        ],
        "mechanism_of_action": "Hormone tuyến giáp tổng hợp (T4). Chuyển hóa thành T3 (triiodothyronine) - hormone hoạt động. Điều hòa chuyển hóa, tăng trưởng, phát triển.",
        "monitoring": [
            "TSH (Thyroid Stimulating Hormone) - Mỗi 4-6 tuần khi điều chỉnh liều, sau đó mỗi 6-12 tháng",
            "Free T4 (nếu cần)",
            "Nhịp tim, huyết áp",
            "Cân nặng",
            "Triệu chứng cường giáp (nếu liều quá cao)"
        ],
        "precautions": [
            "Uống lúc đói (30-60 phút trước ăn sáng) để hấp thu tốt nhất",
            "Uống cách xa sắt, calci, PPI ≥4h",
            "Điều chỉnh liều từ từ (mỗi 4-6 tuần) theo TSH",
            "Thận trọng ở người cao tuổi, bệnh tim (khởi đầu liều thấp)",
            "Không ngừng đột ngột",
            "Thai kỳ: Tăng nhu cầu levothyroxine ~30-50%"
        ],
        "references": {
            "primary_sources": [
                "FDA Drug Label - Levothyroxine (Synthroid, Levoxyl)",
                "UpToDate - Levothyroxine: Drug information",
                "ATA Guidelines - Hypothyroidism",
                "AACE Guidelines - Thyroid Disorders"
            ],
            "last_updated": "2025-02-05",
            "evidence_level": "High - FDA approved, extensive clinical experience"
        },
        "risk_flags": {
            "high_alert": False,
            "narrow_therapeutic_index": True,
            "icu_critical_care_only": False,
            "bleeding_risk": None,
            "organ_toxicity": {"cardiovascular": "Tachycardia, arrhythmias (if over-replacement)", "metabolic": "Osteoporosis (if TSH suppressed)", "endocrine": "Iatrogenic hyperthyroidism (if over-replacement)"},
            "qt_prolongation": False,
            "hepatotoxicity": False,
            "nephrotoxicity": False,
            "requires_monitoring": ["TSH (TDM required - target 0.5-2.5 mIU/L, Black Box Warning - not for weight loss)", "Free T4 (if needed)", "Heart rate, blood pressure (tachycardia, arrhythmias if over-replacement)", "Bone density (osteoporosis risk if TSH suppressed)", "Drug interactions (iron, calcium, PPI - separate by ≥4h)"],
            "look_alike_sound_alike": ["Levothyroxine", "Liothyronine"]
        },
        "guideline_tags": [
            "FDA Black Box Warning - Not for Weight Loss",
            "ATA Guidelines - Hypothyroidism",
            "AACE Guidelines - Thyroid Disorders",
            "WHO Essential Medicines List"
        ],
        "last_updated": "2025-02-18"
    },

    "Methimazole": {
        "group": "Endocrinology - Antithyroid Drug",
        "vietnamese_name": "Methimazole, Thiamazole",
        "brand_names": {
            "common": ["Tapazole"],
            "vietnam": ["Methimazole 5/10mg", "Thyrozol"]
        },
        "administration": ["PO"],
        "indications": [
            "Cường giáp (Hyperthyroidism - Graves' disease)",
            "Bão giáp (Thyroid storm) - Phối hợp điều trị",
            "Chuẩn bị trước phẫu thuật tuyến giáp"
        ],
        "contraindications": [
            "Dị ứng methimazole",
            "Thai kỳ tam cá nguyệt 1 (ưu tiên PTU)"
        ],
        "dosage": {
            "hyperthyroidism": "Khởi đầu 15-30mg/ngày (chia 1-3 lần). Giảm dần khi đạt euthyroid. Duy trì: 5-10mg/ngày.",
            "notes": "Hiệu quả hơn PTU (dùng 1 lần/ngày). Ưu tiên cho hầu hết bệnh nhân cường giáp."
        },
        "side_effects": [
            "Phát ban da (phổ biến, nhẹ)",
            "Suy tủy (Agranulocytosis) - Hiếm nhưng nguy hiểm (0.2-0.5%)",
            "Độc gan (Hepatotoxicity) - Hiếm hơn PTU",
            "Viêm khớp",
            "Giảm vị giác"
        ],
        "interactions": [
            "Warfarin: Giảm INR (do cường giáp được điều trị).",
            "Beta-blockers: Dùng kèm để kiểm soát triệu chứng cường giáp."
        ],
        "mechanism_of_action": "Ức chế enzyme thyroid peroxidase (TPO), ngăn cản tổng hợp hormone tuyến giáp (T3, T4). Không phá hủy hormone đã tổng hợp sẵn → Tác dụng chậm (4-6 tuần).",
        "monitoring": [
            "Công thức máu (CBC) - Trước điều trị và khi có triệu chứng nhiễm trùng (phát hiện agranulocytosis)",
            "Free T4, T3, TSH - Mỗi 4-6 tuần khi điều chỉnh liều",
            "Men gan (ALT, AST) - Định kỳ",
            "Dấu hiệu nhiễm trùng (sốt, đau họng - nghi ngờ agranulocytosis)"
        ],
        "precautions": [
            "Nguy cơ suy tủy (Agranulocytosis) - NGỪNG THUỐC NGAY nếu sốt, đau họng, nhiễm trùng",
            "Kiểm tra CBC nếu có triệu chứng nhiễm trùng",
            "Thai kỳ tam cá nguyệt 1: Ưu tiên PTU (methimazole có nguy cơ quái thai)",
            "Tác dụng chậm (4-6 tuần) - Cần kiên nhẫn",
            "Dùng kèm beta-blocker (Propranolol) để kiểm soát triệu chứng cường giáp"
        ],
        "black_box_warnings": "Nguy cơ suy tủy (Agranulocytosis) nghiêm trọng, có thể tử vong. Ngừng thuốc ngay nếu có sốt, đau họng, nhiễm trùng.",
        "references": {
            "primary_sources": [
                "FDA Drug Label - Methimazole (Tapazole)",
                "UpToDate - Methimazole: Drug information",
                "ATA Guidelines - Hyperthyroidism",
                "AACE Guidelines - Thyroid Disorders"
            ],
            "last_updated": "2025-02-05",
            "evidence_level": "High - FDA approved, extensive clinical experience"
        },
        "risk_flags": {
            "high_alert": True,
            "narrow_therapeutic_index": False,
            "icu_critical_care_only": False,
            "bleeding_risk": None,
            "organ_toxicity": {"hematologic": "Black Box Warning - Agranulocytosis (may be fatal)", "hepatic": "Black Box Warning - Hepatotoxicity", "dermatologic": "Rash (common), SJS/TEN (rare)", "teratogenic": "Teratogenicity (first trimester - prefer PTU)"},
            "qt_prolongation": False,
            "hepatotoxicity": True,
            "nephrotoxicity": False,
            "requires_monitoring": ["CBC (Black Box Warning - agranulocytosis, stop immediately if fever/sore throat/infection)", "Hepatic function (ALT, AST - Black Box Warning for hepatotoxicity)", "Free T4, T3, TSH (thyroid function)", "Infection signs (fever, sore throat - agranulocytosis risk)"],
            "look_alike_sound_alike": ["Methimazole", "Metronidazole"]
        },
        "guideline_tags": [
            "FDA Black Box Warning - Agranulocytosis (may be fatal)",
            "FDA Black Box Warning - Hepatotoxicity",
            "ATA Guidelines - Hyperthyroidism",
            "AACE Guidelines - Thyroid Disorders",
            "WHO Essential Medicines List"
        ],
        "last_updated": "2025-02-18"
    },

    "Propylthiouracil": {
        "group": "Endocrinology - Antithyroid Drug",
        "vietnamese_name": "Propylthiouracil, PTU",
        "brand_names": {
            "common": ["PTU"],
            "vietnam": ["Propylthiouracil 50mg"]
        },
        "administration": ["PO"],
        "indications": [
            "Cường giáp ở thai kỳ tam cá nguyệt 1 (ưu tiên hơn Methimazole)",
            "Bão giáp (Thyroid storm)",
            "Cường giáp (khi không dung nạp Methimazole)"
        ],
        "dosage": {
            "hyperthyroidism": "Khởi đầu 300-600mg/ngày chia 3 lần. Giảm dần. Duy trì: 50-150mg/ngày.",
            "thyroid_storm": "200-400mg mỗi 4-6h (liều cao).",
            "notes": "Phải uống 3 lần/ngày (ít tiện lợi hơn Methimazole). Ưu tiên cho thai kỳ tam cá nguyệt 1."
        },
        "side_effects": [
            "Độc gan (Hepatotoxicity) - Nguy hiểm hơn Methimazole, có thể suy gan cấp",
            "Suy tủy (Agranulocytosis)",
            "Phát ban da",
            "Viêm khớp",
            "Viêm mạch (ANCA-associated vasculitis)"
        ],
        "mechanism_of_action": "Tương tự Methimazole (ức chế TPO). Thêm tác dụng: Ức chế chuyển hóa T4→T3 ở ngoại vi → Tác dụng nhanh hơn Methimazole một chút.",
        "monitoring": [
            "Men gan (ALT, AST) - Trước điều trị và định kỳ (nguy cơ độc gan cao)",
            "CBC - Phát hiện agranulocytosis",
            "Free T4, T3, TSH"
        ],
        "precautions": [
            "Nguy cơ độc gan cao - Theo dõi men gan chặt chẽ",
            "Nguy cơ suy tủy - Tương tự Methimazole",
            "Thai kỳ: Ưu tiên cho tam cá nguyệt 1, chuyển sang Methimazole ở tam cá nguyệt 2-3",
            "Ít được dùng hơn Methimazole (trừ thai kỳ và bão giáp)"
        ],
        "black_box_warnings": "Nguy cơ suy gan cấp nghiêm trọng, có thể tử vong. Nguy cơ suy tủy (Agranulocytosis).",
        "references": {
            "primary_sources": [
                "FDA Drug Label - Propylthiouracil (PTU)",
                "UpToDate - Propylthiouracil: Drug information",
                "ATA Guidelines - Hyperthyroidism",
                "AACE Guidelines - Thyroid Disorders"
            ],
            "last_updated": "2025-02-05",
            "evidence_level": "High - FDA approved, extensive clinical experience"
        },
        "risk_flags": {
            "high_alert": True,
            "narrow_therapeutic_index": False,
            "icu_critical_care_only": False,
            "bleeding_risk": None,
            "organ_toxicity": {"hepatic": "Black Box Warning - Severe hepatotoxicity, liver failure (may be fatal)", "hematologic": "Black Box Warning - Agranulocytosis (may be fatal)", "dermatologic": "Rash (common), SJS/TEN (rare)", "vascular": "ANCA-associated vasculitis (rare)"},
            "qt_prolongation": False,
            "hepatotoxicity": True,
            "nephrotoxicity": False,
            "requires_monitoring": ["Hepatic function (ALT, AST - Black Box Warning for severe hepatotoxicity/liver failure)", "CBC (Black Box Warning - agranulocytosis, stop immediately if fever/sore throat/infection)", "Free T4, T3, TSH (thyroid function)", "Infection signs (fever, sore throat - agranulocytosis risk)", "Vasculitis signs (ANCA-associated vasculitis risk)"],
            "look_alike_sound_alike": ["Propylthiouracil", "Propylthiouracil"]
        },
        "guideline_tags": [
            "FDA Black Box Warning - Severe Hepatotoxicity, Liver Failure (may be fatal)",
            "FDA Black Box Warning - Agranulocytosis (may be fatal)",
            "ATA Guidelines - Hyperthyroidism",
            "AACE Guidelines - Thyroid Disorders",
            "WHO Essential Medicines List"
        ],
        "last_updated": "2025-02-18"
    }
}
