"""
Thyroid Medications (Thuốc tuyến giáp)
Bao gồm: Hormone tuyến giáp, thuốc kháng giáp.
"""

THYROID_DRUGS = {
    "Levothyroxine": {
        "group": "Endocrinology - Thyroid Hormone",

        "pregnancy": "A - Không có nguy cơ trong các nghiên cứu có đối chứng. An toàn trong thai kỳ",
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
        "contraindications_detail": {
            "tuyệt_đối": [
                "Cường giáp chưa điều trị",
                "Nhồi máu cơ tim cấp",
                "Suy thượng thận chưa điều trị"
            ],
            "tương_đối": [
                "Bệnh tim mạch (bệnh mạch vành, loạn nhịp)",
                "Người cao tuổi - cần tăng liều rất chậm",
                "Bệnh nhân có nguy cơ loãng xương (tránh ức chế TSH quá mức)"
            ]
        },
        "renal_adjustment": {
            "normal": "Không cần chỉnh liều; chuẩn độ theo TSH.",
            "30_60": "Không cần chỉnh liều; tăng/giảm liều chậm, theo dõi nhịp tim và TSH.",
            "under_30": "Không cần chỉnh liều; thận trọng bệnh tim/suy thận, chuẩn độ rất chậm."
        },
        "hepatic_adjustment": {
            "mild": "Không cần chỉnh liều.",
            "moderate": "Không cần chỉnh liều; theo dõi TSH sát.",
            "severe": "Không cần chỉnh liều; chuẩn độ chậm và theo dõi lâm sàng.",
            "notes": "Liều điều chỉnh chủ yếu dựa trên TSH hơn là chức năng gan/thận."
        },
        "drug_interactions": {
            "major": [
                {
                    "drug": "Sắt, Calci, antacid, sucralfate, PPI",
                    "mechanism": "Giảm hấp thu levothyroxine (tạo phức hoặc thay đổi pH).",
                    "effect": "Giảm nồng độ/TSH tăng.",
                    "management": "Uống levothyroxine cách xa ≥4 giờ."
                },
                {
                    "drug": "Warfarin",
                    "mechanism": "Tăng nhạy cảm với warfarin khi đạt trạng thái eutyroid.",
                    "effect": "INR có thể tăng.",
                    "management": "Theo dõi INR; giảm liều warfarin nếu cần."
                }
            ],
            "moderate": [
                {
                    "drug": "Amiodarone",
                    "mechanism": "Ức chế chuyển T4→T3, chứa iod.",
                    "effect": "Có thể cần điều chỉnh liều levothyroxine.",
                    "management": "Theo dõi TSH/FT4 sát."
                }
            ],
            "minor": []
        },
        "overdose_management": {
            "symptoms": [
                "Cường giáp iatrogenic: tim nhanh, loạn nhịp, run, sốt",
                "Bão giáp (hiếm): sốt cao, mê sảng, suy tim"
            ],
            "antidote": "Không có antidote đặc hiệu.",
            "treatment": [
                "Ngừng levothyroxine; than hoạt nếu mới uống.",
                "Chẹn beta (propranolol) để kiểm soát nhịp tim/lo âu.",
                "Điều trị hỗ trợ (dịch, hạ sốt).",
                "Trường hợp nặng: PTU + iod + steroid theo phác đồ bão giáp."
            ],
            "monitoring": "Mạch, huyết áp, ECG, TSH/FT4 nếu cần."
        },
        "reversal_agents": None,
        "administration_instructions": {
            "oral": {
                "with_food": "Uống lúc đói, 30-60 phút trước ăn sáng.",
                "timing": "Uống buổi sáng với nước lọc; tách sắt/calci/antacid/PPI ≥4 giờ.",
                "notes": "Nếu uống ban đêm, cần nhịn ăn ≥3-4 giờ trước."
            }
        },
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

        "pregnancy": "D - Có bằng chứng về nguy cơ. Thận trọng trong thai kỳ",
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
        "contraindications_detail": {
            "tuyệt_đối": [
                "Dị ứng với methimazole",
                "Thai kỳ tam cá nguyệt 1 (ưu tiên PTU)",
                "Tiền sử viêm gan nặng do methimazole",
                "Bạch cầu trung tính <1500/mm3"
            ],
            "tương_đối": [
                "Bệnh gan mạn/men gan tăng sẵn",
                "Suy tủy, giảm bạch cầu hạt",
                "Người cao tuổi hoặc có bệnh tim nặng (titrate chậm)"
            ]
        },
        "renal_adjustment": {
            "normal": "Không cần chỉnh liều.",
            "30_60": "Không cần chỉnh liều; theo dõi độc tính.",
            "under_30": "Không cần chỉnh liều; theo dõi sát CBC/men gan."
        },
        "hepatic_adjustment": {
            "mild": "Thận trọng; theo dõi men gan.",
            "moderate": "Tránh hoặc dùng liều thấp, theo dõi sát.",
            "severe": "Tránh nếu có thể (nguy cơ độc gan).",
            "notes": "Ngừng thuốc nếu men gan tăng đáng kể hoặc vàng da."
        },
        "drug_interactions": {
            "major": [
                {
                    "drug": "Warfarin",
                    "mechanism": "Điều chỉnh cường giáp làm giảm độ nhạy với warfarin.",
                    "effect": "INR giảm khi trạng thái cường giáp được kiểm soát.",
                    "management": "Theo dõi INR và điều chỉnh liều warfarin."
                }
            ],
            "moderate": [
                {
                    "drug": "Clozapine hoặc thuốc gây giảm bạch cầu",
                    "mechanism": "Cộng gộp nguy cơ giảm bạch cầu hạt.",
                    "effect": "Tăng nguy cơ agranulocytosis.",
                    "management": "Tránh phối hợp nếu có thể; theo dõi CBC sát."
                }
            ],
            "minor": []
        },
        "overdose_management": {
            "symptoms": [
                "Giảm bạch cầu hạt, sốt, đau họng",
                "Vàng da, tăng men gan",
                "Buồn nôn, đau bụng"
            ],
            "antidote": "Không có antidote đặc hiệu.",
            "treatment": [
                "Ngừng methimazole ngay.",
                "Hỗ trợ: truyền dịch, kiểm soát triệu chứng.",
                "CBC/men gan khẩn; G-CSF nếu agranulocytosis nặng.",
                "Kháng sinh nếu nhiễm trùng."
            ],
            "monitoring": "CBC, men gan, dấu hiệu nhiễm trùng."
        },
        "reversal_agents": None,
        "administration_instructions": {
            "oral": {
                "with_food": "Có thể uống cùng hoặc không cùng thức ăn.",
                "timing": "Thường 1 lần/ngày; chia 2-3 lần nếu liều cao.",
                "notes": "Uống cùng giờ mỗi ngày; không tự ý ngừng."
            }
        },
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

        "pregnancy": "D - Có bằng chứng về nguy cơ. Thận trọng trong thai kỳ",
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
        "contraindications_detail": {
            "tuyệt_đối": [
                "Dị ứng với PTU",
                "Tiền sử suy gan nặng do PTU",
                "Bạch cầu trung tính <1500/mm3"
            ],
            "tương_đối": [
                "Bệnh gan mạn/men gan tăng",
                "Suy tủy, giảm bạch cầu hạt",
                "Người cao tuổi/bệnh tim (titrate chậm)"
            ]
        },
        "renal_adjustment": {
            "normal": "Không cần chỉnh liều.",
            "30_60": "Không cần chỉnh liều; theo dõi độc tính.",
            "under_30": "Không cần chỉnh liều; theo dõi sát CBC/men gan."
        },
        "hepatic_adjustment": {
            "mild": "Thận trọng; theo dõi men gan.",
            "moderate": "Tránh nếu có lựa chọn khác; theo dõi sát.",
            "severe": "Chống chỉ định do nguy cơ suy gan.",
            "notes": "Ngừng thuốc ngay nếu men gan tăng đáng kể hoặc vàng da."
        },
        "drug_interactions": {
            "major": [
                {
                    "drug": "Warfarin",
                    "mechanism": "Điều chỉnh cường giáp làm thay đổi nhạy cảm với warfarin.",
                    "effect": "INR giảm khi kiểm soát cường giáp.",
                    "management": "Theo dõi INR; điều chỉnh liều warfarin."
                }
            ],
            "moderate": [
                {
                    "drug": "Clozapine/thuốc gây giảm bạch cầu",
                    "mechanism": "Cộng gộp nguy cơ giảm bạch cầu hạt.",
                    "effect": "Tăng nguy cơ agranulocytosis.",
                    "management": "Tránh phối hợp; nếu dùng, theo dõi CBC sát."
                }
            ],
            "minor": []
        },
        "overdose_management": {
            "symptoms": [
                "Độc gan (vàng da, tăng men gan)",
                "Giảm bạch cầu hạt, sốt, đau họng",
                "Buồn nôn, đau bụng"
            ],
            "antidote": "Không có antidote đặc hiệu.",
            "treatment": [
                "Ngừng PTU ngay.",
                "Hỗ trợ: truyền dịch, kiểm soát triệu chứng.",
                "CBC/men gan khẩn; G-CSF nếu agranulocytosis nặng.",
                "Cân nhắc ghép gan trong suy gan tối cấp."
            ],
            "monitoring": "CBC, men gan, dấu hiệu nhiễm trùng, dấu hiệu suy gan."
        },
        "reversal_agents": None,
        "administration_instructions": {
            "oral": {
                "with_food": "Có thể uống cùng hoặc không cùng thức ăn.",
                "timing": "Chia 3 lần/ngày do T1/2 ngắn; ưu tiên giờ cố định.",
                "notes": "Không tự ý ngừng; báo ngay nếu sốt/đau họng."
            }
        },
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
    },

    "Liothyronine": {
        "group": "Endocrinology - Thyroid Hormone",
        "pregnancy": "A - Không có nguy cơ trong các nghiên cứu có đối chứng. An toàn trong thai kỳ",
        "vietnamese_name": "Liothyronine, L-Triiodothyronine, T3, Cytomel",
        "brand_names": {
            "common": ["Cytomel", "Triostat"],
            "vietnam": ["Liothyronine 5/25mcg"]
        },
        "administration": ["PO", "IV"],
        "indications": [
            "Suy giáp nặng cần tác dụng nhanh",
            "Myxedema coma (IV)",
            "Suy giáp kháng với levothyroxine",
            "Ức chế TSH sau điều trị ung thư tuyến giáp (kết hợp với T4)"
        ],
        "contraindications": [
            "Cường giáp chưa điều trị",
            "Nhồi máu cơ tim cấp",
            "Suy thượng thận chưa điều trị",
            "Dị ứng liothyronine"
        ],
        "dosage": {
            "hypothyroidism": "Khởi đầu 5-25mcg/ngày chia 2-3 lần. Tăng dần 5-12.5mcg mỗi 1-2 tuần. Liều duy trì: 25-75mcg/ngày.",
            "myxedema_coma": "10-20mcg IV nạp, sau đó 2.5-10mcg IV mỗi 8h x 2-3 ngày đầu. Có thể kết hợp với levothyroxine IV.",
            "notes": "T3 có tác dụng nhanh hơn T4 (onset 6-12h vs 3-5 ngày) nhưng thời gian bán thải ngắn (1 ngày vs 7 ngày). Thường dùng kết hợp với levothyroxine hoặc khi cần tác dụng nhanh."
        },
        "side_effects": [
            "Liều quá cao: Tim đập nhanh, run tay, lo âu, mất ngủ, đổ mồ hôi",
            "Rối loạn nhịp tim (nhịp nhanh xoang, rung nhĩ)",
            "Đau thắt ngực (ở bệnh nhân bệnh mạch vành)",
            "Loãng xương (nếu TSH bị ức chế quá mức)"
        ],
        "interactions": [
            "Sắt, Calci, PPI, Sucralfate: Giảm hấp thu (uống cách xa ≥4h).",
            "Warfarin: Tăng INR (cần theo dõi).",
            "Amiodarone: Ảnh hưởng chuyển hóa T3."
        ],
        "mechanism_of_action": "Hormone tuyến giáp tổng hợp (T3, triiodothyronine) - dạng hoạt động trực tiếp. Không cần chuyển hóa như T4. Gắn với thyroid hormone receptor trong nhân tế bào, điều hòa biểu hiện gen, tăng chuyển hóa cơ bản. Tác dụng nhanh hơn levothyroxine (T4) nhưng thời gian bán thải ngắn hơn.",
        "monitoring": [
            "TSH, Free T3 - Mỗi 2-4 tuần khi điều chỉnh liều (T3 thay đổi nhanh hơn T4)",
            "Free T4 (nếu dùng kết hợp với levothyroxine)",
            "Nhịp tim, huyết áp (theo dõi sát do tác dụng nhanh)",
            "ECG (rối loạn nhịp tim)",
            "Triệu chứng cường giáp (nếu liều quá cao)"
        ],
        "precautions": [
            "Tác dụng nhanh và mạnh - thận trọng ở bệnh nhân bệnh tim mạch",
            "Khởi đầu liều thấp (5mcg/ngày) ở người cao tuổi/bệnh tim",
            "Phải chia liều 2-3 lần/ngày do thời gian bán thải ngắn",
            "Thường dùng kết hợp với levothyroxine (T4) để mô phỏng sinh lý tự nhiên",
            "Không dùng đơn độc lâu dài (ưu tiên levothyroxine)",
            "Myxedema coma: Dùng IV, có thể kết hợp với levothyroxine IV"
        ],
        "contraindications_detail": {
            "tuyệt_đối": [
                "Cường giáp chưa điều trị",
                "Nhồi máu cơ tim cấp",
                "Suy thượng thận chưa điều trị",
                "Dị ứng liothyronine"
            ],
            "tương_đối": [
                "Bệnh tim mạch (bệnh mạch vành, loạn nhịp) - thận trọng tối đa",
                "Người cao tuổi - khởi đầu liều rất thấp",
                "Bệnh nhân có nguy cơ loãng xương"
            ]
        },
        "renal_adjustment": {
            "normal": "Không cần chỉnh liều; chuẩn độ theo TSH/FT3.",
            "30_60": "Không cần chỉnh liều; tăng/giảm liều chậm, theo dõi nhịp tim và TSH.",
            "under_30": "Không cần chỉnh liều; thận trọng bệnh tim/suy thận, chuẩn độ rất chậm."
        },
        "hepatic_adjustment": {
            "mild": "Không cần chỉnh liều.",
            "moderate": "Không cần chỉnh liều; theo dõi TSH/FT3 sát.",
            "severe": "Không cần chỉnh liều; chuẩn độ chậm và theo dõi lâm sàng.",
            "notes": "Liều điều chỉnh chủ yếu dựa trên TSH/FT3 hơn là chức năng gan/thận."
        },
        "drug_interactions": {
            "major": [
                {
                    "drug": "Sắt, Calci, antacid, sucralfate, PPI",
                    "mechanism": "Giảm hấp thu liothyronine (tạo phức hoặc thay đổi pH).",
                    "effect": "Giảm nồng độ/TSH tăng.",
                    "management": "Uống liothyronine cách xa ≥4 giờ."
                },
                {
                    "drug": "Warfarin",
                    "mechanism": "Tăng nhạy cảm với warfarin khi đạt trạng thái eutyroid.",
                    "effect": "INR có thể tăng.",
                    "management": "Theo dõi INR; giảm liều warfarin nếu cần."
                }
            ],
            "moderate": [
                {
                    "drug": "Amiodarone",
                    "mechanism": "Ức chế chuyển T4→T3, chứa iod.",
                    "effect": "Có thể cần điều chỉnh liều liothyronine.",
                    "management": "Theo dõi TSH/FT3 sát."
                }
            ],
            "minor": []
        },
        "overdose_management": {
            "symptoms": [
                "Cường giáp iatrogenic: tim nhanh, loạn nhịp, run, sốt (nhanh hơn T4)",
                "Bão giáp (hiếm): sốt cao, mê sảng, suy tim"
            ],
            "antidote": "Không có antidote đặc hiệu.",
            "treatment": [
                "Ngừng liothyronine ngay; than hoạt nếu mới uống.",
                "Chẹn beta (propranolol) để kiểm soát nhịp tim/lo âu.",
                "Điều trị hỗ trợ (dịch, hạ sốt).",
                "Trường hợp nặng: PTU + iod + steroid theo phác đồ bão giáp."
            ],
            "monitoring": "Mạch, huyết áp, ECG, TSH/FT3 nếu cần."
        },
        "reversal_agents": None,
        "administration_instructions": {
            "oral": {
                "with_food": "Uống lúc đói, 30-60 phút trước ăn (tương tự levothyroxine).",
                "timing": "Chia 2-3 lần/ngày do thời gian bán thải ngắn. Uống buổi sáng và trưa/tối với nước lọc; tách sắt/calci/antacid/PPI ≥4 giờ.",
                "notes": "Không dùng ban đêm (có thể gây mất ngủ do tác dụng kích thích)."
            },
            "iv": {
                "reconstitution": "Pha với nước cất hoặc dung dịch muối đẳng trương.",
                "infusion_rate": "Truyền chậm trong 2-5 phút. Không truyền nhanh.",
                "compatibility": ["D5W", "Normal saline"],
                "incompatibility": ["Không trộn với các thuốc khác"],
                "notes": "Chỉ dùng IV trong myxedema coma. Chuyển sang PO ngay khi có thể."
            }
        },
        "pregnancy_lactation": {
            "fda_category": "A",
            "pregnancy_details": "Liothyronine là hormone tuyến giáp tự nhiên, an toàn trong thai kỳ. Tuy nhiên, levothyroxine (T4) được ưu tiên hơn trong thai kỳ vì T4 có thể chuyển hóa thành T3 ở thai nhi. Nếu dùng liothyronine, cần theo dõi TSH/FT3 sát.",
            "lactation": {
                "safety": "Compatible",
                "details": "Liothyronine bài tiết vào sữa mẹ ở nồng độ rất thấp, không ảnh hưởng đến chức năng tuyến giáp của trẻ bú mẹ.",
                "recommendation": "Có thể dùng khi cho con bú. Không cần điều chỉnh liều."
            }
        },
        "pharmacokinetics": {
            "half_life": "1 ngày (ngắn hơn T4)",
            "onset": "6-12 giờ (nhanh hơn T4)",
            "duration": "Ngắn (1-2 ngày)",
            "protein_binding": "99.7% (gắn với TBG, transthyretin, albumin)",
            "metabolism": "Chủ yếu ở gan và các mô ngoại vi (deiodination)",
            "clearance": "Gan và thận"
        },
        "storage": "Bảo quản ở nhiệt độ phòng (20-25°C), tránh ẩm, tránh ánh sáng.",
        "black_box_warnings": "Không được dùng để giảm cân ở bệnh nhân bình giáp. Quá liều có thể gây cường giáp, rối loạn nhịp tim nhanh hơn T4. Ở bệnh nhân bệnh mạch vành, phải bắt đầu với liều rất thấp và tăng chậm.",
        "references": {
            "primary_sources": [
                "FDA Drug Label - Liothyronine (Cytomel, Triostat)",
                "UpToDate - Liothyronine: Drug information",
                "ATA Guidelines - Hypothyroidism",
                "AACE Guidelines - Thyroid Disorders"
            ],
            "last_updated": "2025-02-18",
            "evidence_level": "High - FDA approved, extensive clinical experience"
        },
        "risk_flags": {
            "high_alert": False,
            "narrow_therapeutic_index": True,
            "icu_critical_care_only": False,
            "bleeding_risk": None,
            "organ_toxicity": {"cardiovascular": "Tachycardia, arrhythmias (if over-replacement, faster than T4)", "metabolic": "Osteoporosis (if TSH suppressed)", "endocrine": "Iatrogenic hyperthyroidism (if over-replacement)"},
            "qt_prolongation": False,
            "hepatotoxicity": False,
            "nephrotoxicity": False,
            "requires_monitoring": ["TSH, Free T3 (TDM required - target TSH 0.5-2.5 mIU/L, faster changes than T4)", "Free T4 (if combined with levothyroxine)", "Heart rate, blood pressure, ECG (tachycardia, arrhythmias if over-replacement)", "Bone density (osteoporosis risk if TSH suppressed)"],
            "look_alike_sound_alike": ["Liothyronine", "Levothyroxine"]
        },
        "guideline_tags": [
            "FDA Black Box Warning - Not for Weight Loss",
            "ATA Guidelines - Hypothyroidism",
            "AACE Guidelines - Thyroid Disorders"
        ],
        "last_updated": "2025-02-18"
    },

    "Radioactive Iodine (I-131)": {
        "group": "Endocrinology - Thyroid Treatment",
        "pregnancy": "X - Chống chỉ định tuyệt đối trong thai kỳ",
        "vietnamese_name": "I-ốt phóng xạ, Radioactive Iodine, I-131, RAI",
        "brand_names": {
            "common": ["I-131", "Radioiodine"],
            "vietnam": ["I-131"]
        },
        "administration": ["PO"],
        "indications": [
            "Cường giáp (Hyperthyroidism - Graves' disease, toxic nodular goiter)",
            "Điều trị dứt điểm cường giáp",
            "Ung thư tuyến giáp (sau phẫu thuật)",
            "Bướu giáp độc đơn nhân hoặc đa nhân"
        ],
        "contraindications": [
            "Có thai (chống chỉ định tuyệt đối)",
            "Đang cho con bú",
            "Kế hoạch có thai trong vòng 6-12 tháng",
            "Dị ứng iod",
            "Cường giáp nặng không kiểm soát được (cần điều trị trước bằng thuốc kháng giáp)"
        ],
        "dosage": {
            "hyperthyroidism_graves": "5-15 mCi (millicurie) tùy kích thước tuyến giáp và độ hấp thu. Liều tính dựa trên: kích thước tuyến giáp (gram), % hấp thu I-131 tại 24h, T1/2 hiệu quả.",
            "hyperthyroidism_toxic_nodule": "10-30 mCi tùy kích thước nhân.",
            "thyroid_cancer_ablation": "30-150 mCi sau phẫu thuật cắt tuyến giáp.",
            "notes": "Liều được tính bởi bác sĩ y học hạt nhân. Uống 1 lần duy nhất. Hiệu quả sau 6-12 tuần. Có thể cần liều lặp lại nếu không đáp ứng."
        },
        "side_effects": [
            "Suy giáp (phổ biến, 50-80% sau 1 năm) - cần điều trị suốt đời bằng levothyroxine",
            "Viêm tuyến giáp tạm thời (2-3 tuần sau điều trị): đau cổ, sưng, sốt nhẹ",
            "Cường giáp tạm thời tăng (1-2 tuần sau điều trị) - do giải phóng hormone từ tuyến giáp bị phá hủy",
            "Bão giáp (hiếm, nếu cường giáp nặng chưa kiểm soát trước điều trị)",
            "Khô miệng, thay đổi vị giác (tạm thời)",
            "Rụng tóc (hiếm, tạm thời)"
        ],
        "interactions": [
            "Thuốc kháng giáp (Methimazole, PTU): Ngừng 3-7 ngày trước I-131 để tăng hấp thu.",
            "Iod (thuốc, thực phẩm giàu iod): Giảm hấp thu I-131 - tránh 1-2 tuần trước điều trị.",
            "Levothyroxine: Ngừng 4-6 tuần trước I-131 (nếu đang dùng).",
            "Chất cản quang có iod: Tránh 4-6 tuần trước điều trị."
        ],
        "mechanism_of_action": "I-131 là đồng vị phóng xạ của iod. Tuyến giáp hấp thu iod (bao gồm I-131) để tổng hợp hormone. I-131 phát ra tia beta (electron) phá hủy tế bào tuyến giáp từ bên trong. Tác dụng chậm (6-12 tuần) do tế bào chết dần. Giảm sản xuất hormone tuyến giáp, điều trị cường giáp hoặc phá hủy mô ung thư còn sót lại.",
        "monitoring": [
            "Chức năng tuyến giáp (TSH, Free T4, Free T3) - Mỗi 4-6 tuần sau điều trị cho đến khi ổn định, sau đó mỗi 6-12 tháng",
            "Triệu chứng suy giáp: mệt mỏi, tăng cân, nhịp tim chậm, táo bón, lạnh",
            "Triệu chứng cường giáp tạm thời tăng: tim nhanh, run, lo âu (1-2 tuần sau điều trị)",
            "Viêm tuyến giáp: đau cổ, sưng, sốt (2-3 tuần sau điều trị)",
            "Xét nghiệm thai kỳ (nếu phụ nữ trong độ tuổi sinh đẻ) - trước điều trị và sau 6-12 tháng"
        ],
        "precautions": [
            "CHỐNG CHỈ ĐỊNH TUYỆT ĐỐI trong thai kỳ - gây dị tật thai nhi, suy giáp bẩm sinh",
            "Tránh có thai 6-12 tháng sau điều trị (nam và nữ)",
            "Ngừng cho con bú trước điều trị và không cho con bú lại",
            "Cách ly tạm thời sau uống I-131: tránh tiếp xúc gần với trẻ em, phụ nữ có thai 3-7 ngày",
            "Uống nhiều nước, đi tiểu thường xuyên để thải I-131 nhanh",
            "Ngừng thuốc kháng giáp 3-7 ngày trước I-131 (để tăng hấp thu)",
            "Tránh iod (thuốc, thực phẩm) 1-2 tuần trước điều trị",
            "Theo dõi sát sau điều trị - có thể cần điều trị triệu chứng cường giáp tạm thời"
        ],
        "contraindications_detail": {
            "tuyệt_đối": [
                "Có thai (chống chỉ định tuyệt đối - gây dị tật thai nhi, suy giáp bẩm sinh)",
                "Đang cho con bú",
                "Kế hoạch có thai trong vòng 6-12 tháng (nam và nữ)",
                "Dị ứng iod",
                "Cường giáp nặng không kiểm soát được (cần điều trị trước bằng thuốc kháng giáp)"
            ],
            "tương_đối": [
                "Trẻ em <5 tuổi (thận trọng, ưu tiên phẫu thuật)",
                "Bệnh mắt do Basedow nặng (có thể làm nặng thêm)",
                "Bướu giáp rất lớn gây chèn ép (ưu tiên phẫu thuật)"
            ]
        },
        "renal_adjustment": {
            "normal": "Không cần chỉnh liều.",
            "30_60": "Không cần chỉnh liều.",
            "under_30": "Thận trọng; I-131 thải qua thận, có thể tích lũy ở suy thận nặng."
        },
        "hepatic_adjustment": {
            "mild": "Không cần chỉnh liều.",
            "moderate": "Không cần chỉnh liều.",
            "severe": "Không cần chỉnh liều."
        },
        "drug_interactions": {
            "major": [
                {
                    "drug": "Thuốc kháng giáp (Methimazole, PTU)",
                    "mechanism": "Giảm hấp thu I-131 vào tuyến giáp.",
                    "effect": "Giảm hiệu quả điều trị I-131.",
                    "management": "Ngừng thuốc kháng giáp 3-7 ngày trước I-131. Có thể dùng lại sau I-131 để kiểm soát triệu chứng tạm thời."
                },
                {
                    "drug": "Iod (thuốc, thực phẩm giàu iod, chất cản quang)",
                    "mechanism": "Iod không phóng xạ cạnh tranh với I-131, giảm hấp thu I-131.",
                    "effect": "Giảm hiệu quả điều trị I-131 đáng kể.",
                    "management": "Tránh iod 1-2 tuần trước điều trị (thuốc, thực phẩm giàu iod như rong biển, chất cản quang có iod)."
                }
            ],
            "moderate": [
                {
                    "drug": "Levothyroxine",
                    "mechanism": "Ức chế TSH, giảm hấp thu I-131.",
                    "effect": "Giảm hiệu quả điều trị I-131.",
                    "management": "Ngừng levothyroxine 4-6 tuần trước I-131 (nếu đang dùng)."
                }
            ],
            "minor": []
        },
        "overdose_management": {
            "symptoms": [
                "Suy giáp nặng (sớm hoặc muộn)",
                "Viêm tuyến giáp nặng: đau cổ, sưng, sốt",
                "Bão giáp (nếu cường giáp nặng chưa kiểm soát trước điều trị)"
            ],
            "antidote": "Không có antidote đặc hiệu. I-131 đã hấp thu vào tuyến giáp không thể loại bỏ.",
            "treatment": [
                "Điều trị hỗ trợ: truyền dịch, hạ sốt, giảm đau nếu viêm tuyến giáp.",
                "Điều trị bão giáp nếu xảy ra: PTU, iod, steroid, chẹn beta.",
                "Điều trị suy giáp: levothyroxine ngay khi có dấu hiệu suy giáp.",
                "Theo dõi chức năng tuyến giáp sát."
            ],
            "monitoring": "Chức năng tuyến giáp (TSH, FT4, FT3), triệu chứng lâm sàng, dấu hiệu viêm tuyến giáp."
        },
        "reversal_agents": None,
        "administration_instructions": {
            "oral": {
                "with_food": "Uống lúc đói, với nước đầy đủ.",
                "timing": "Uống 1 lần duy nhất tại khoa y học hạt nhân. Uống nhiều nước sau đó để thải I-131 nhanh.",
                "notes": "Cách ly tạm thời sau uống: tránh tiếp xúc gần với trẻ em, phụ nữ có thai 3-7 ngày. Uống nhiều nước, đi tiểu thường xuyên."
            }
        },
        "pregnancy_lactation": {
            "fda_category": "X",
            "pregnancy_details": "CHỐNG CHỈ ĐỊNH TUYỆT ĐỐI trong thai kỳ. I-131 qua nhau thai, tích lũy trong tuyến giáp thai nhi, gây suy giáp bẩm sinh, dị tật, và tăng nguy cơ ung thư tuyến giáp ở trẻ. Phải xác nhận không có thai trước điều trị (xét nghiệm thai kỳ). Tránh có thai 6-12 tháng sau điều trị (nam và nữ).",
            "lactation": {
                "safety": "Contraindicated",
                "details": "I-131 bài tiết vào sữa mẹ ở nồng độ cao, gây nguy hiểm cho trẻ bú mẹ. Phải ngừng cho con bú trước điều trị và không cho con bú lại sau điều trị.",
                "recommendation": "CHỐNG CHỈ ĐỊNH khi cho con bú. Phải ngừng cho con bú trước điều trị."
            }
        },
        "pharmacokinetics": {
            "half_life": "8 ngày (I-131), nhưng tích lũy trong tuyến giáp với T1/2 hiệu quả 5-7 ngày",
            "onset": "6-12 tuần (tác dụng phá hủy tế bào)",
            "duration": "Vĩnh viễn (phá hủy tế bào tuyến giáp)",
            "protein_binding": "Không áp dụng (phóng xạ)",
            "metabolism": "Tích lũy trong tuyến giáp, phát ra tia beta phá hủy tế bào",
            "clearance": "Thải qua nước tiểu, phân (I-131 không hấp thu)"
        },
        "storage": "Bảo quản và sử dụng tại khoa y học hạt nhân. Không lưu trữ tại nhà.",
        "black_box_warnings": "CHỐNG CHỈ ĐỊNH TUYỆT ĐỐI trong thai kỳ và khi cho con bú. Gây dị tật thai nhi, suy giáp bẩm sinh, và tăng nguy cơ ung thư tuyến giáp ở trẻ. Phải xác nhận không có thai trước điều trị. Tránh có thai 6-12 tháng sau điều trị.",
        "references": {
            "primary_sources": [
                "FDA Drug Label - Radioactive Iodine (I-131)",
                "UpToDate - Radioactive iodine therapy for hyperthyroidism",
                "ATA Guidelines - Hyperthyroidism",
                "AACE Guidelines - Thyroid Disorders",
                "SNMMI Guidelines - Radioiodine Therapy"
            ],
            "last_updated": "2025-02-18",
            "evidence_level": "High - FDA approved, extensive clinical experience"
        },
        "risk_flags": {
            "high_alert": True,
            "narrow_therapeutic_index": False,
            "icu_critical_care_only": False,
            "bleeding_risk": None,
            "organ_toxicity": {"endocrine": "Black Box Warning - Permanent hypothyroidism (50-80% after 1 year)", "teratogenic": "Black Box Warning - Teratogenicity, congenital hypothyroidism (X category)", "radiation": "Radiation exposure - requires isolation"},
            "qt_prolongation": False,
            "hepatotoxicity": False,
            "nephrotoxicity": False,
            "requires_monitoring": ["Pregnancy test (Black Box Warning - X category, absolute contraindication in pregnancy)", "Thyroid function (TSH, Free T4, Free T3 - every 4-6 weeks until stable)", "Symptoms of hypothyroidism (permanent in 50-80%)", "Symptoms of temporary hyperthyroidism exacerbation (1-2 weeks post-treatment)", "Thyroiditis symptoms (2-3 weeks post-treatment)"],
            "look_alike_sound_alike": ["I-131", "I-123 (diagnostic)"]
        },
        "guideline_tags": [
            "FDA Black Box Warning - X Category - Absolute Contraindication in Pregnancy",
            "ATA Guidelines - Hyperthyroidism",
            "AACE Guidelines - Thyroid Disorders",
            "SNMMI Guidelines - Radioiodine Therapy"
        ],
        "last_updated": "2025-02-18"
    },

    "Potassium Iodide": {
        "group": "Endocrinology - Thyroid Treatment",
        "pregnancy": "D - Có bằng chứng về nguy cơ. Thận trọng trong thai kỳ",
        "vietnamese_name": "Kali iodid, Potassium Iodide, SSKI, Lugol's Solution",
        "brand_names": {
            "common": ["SSKI (Saturated Solution of Potassium Iodide)", "Lugol's Solution", "Pima"],
            "vietnam": ["Dung dịch SSKI", "Lugol"]
        },
        "administration": ["PO"],
        "indications": [
            "Bão giáp (Thyroid storm) - ức chế giải phóng hormone",
            "Chuẩn bị trước phẫu thuật cắt tuyến giáp (giảm lưu lượng máu tuyến giáp)",
            "Bảo vệ tuyến giáp trong phơi nhiễm phóng xạ (nuclear emergency)",
            "Viêm tuyến giáp bán cấp (giảm đau, viêm)"
        ],
        "contraindications": [
            "Dị ứng iod",
            "Bệnh da do iod (iododerma)",
            "Viêm mạch do iod",
            "Cường giáp do nhân độc (có thể làm nặng thêm)"
        ],
        "dosage": {
            "thyroid_storm": "SSKI: 5 giọt (250mg) mỗi 6-8h PO. Hoặc Lugol's solution: 5-10 giọt mỗi 6-8h PO. Dùng 1 giờ sau khi đã dùng thuốc kháng giáp.",
            "pre_surgery": "SSKI: 3-5 giọt 3 lần/ngày x 7-10 ngày trước phẫu thuật.",
            "radiation_protection": "130mg/ngày (người lớn), 65mg/ngày (trẻ 3-18 tuổi), 32mg/ngày (trẻ 1 tháng-3 tuổi) x 10-14 ngày sau phơi nhiễm.",
            "notes": "Dùng ngắn hạn (1-2 tuần). Không dùng lâu dài. Phải dùng SAU thuốc kháng giáp (ít nhất 1 giờ) trong bão giáp."
        },
        "side_effects": [
            "Phản ứng dị ứng iod: phát ban, mày đay, phù mạch",
            "Iododerma (bệnh da do iod): mụn mủ, loét da",
            "Viêm tuyến nước bọt: sưng, đau",
            "Rối loạn vị giác: vị kim loại",
            "Buồn nôn, nôn, đau bụng",
            "Cường giáp do iod (Jod-Basedow phenomenon) - ở bệnh nhân nhân độc"
        ],
        "interactions": [
            "Thuốc kháng giáp: Phải dùng SAU thuốc kháng giáp (ít nhất 1 giờ) để tránh cung cấp iod cho tổng hợp hormone.",
            "Lithium: Tăng nguy cơ suy giáp.",
            "Amiodarone: Đã chứa iod, có thể cộng gộp tác dụng."
        ],
        "mechanism_of_action": "Iod vô cơ (iodide) ức chế giải phóng hormone tuyến giáp (Wolff-Chaikoff effect) khi dùng liều cao. Giảm lưu lượng máu đến tuyến giáp, làm tuyến giáp cứng lại (dễ phẫu thuật). Trong bão giáp: ức chế giải phóng hormone đã tổng hợp sẵn, giảm nhanh nồng độ hormone trong máu. Trong phơi nhiễm phóng xạ: bão hòa tuyến giáp với iod không phóng xạ, ngăn hấp thu iod phóng xạ.",
        "monitoring": [
            "Triệu chứng bão giáp: sốt, nhịp tim, huyết áp, ý thức",
            "Dấu hiệu dị ứng iod: phát ban, phù mạch",
            "Chức năng tuyến giáp (nếu dùng lâu)",
            "Dấu hiệu cường giáp do iod (Jod-Basedow)"
        ],
        "precautions": [
            "CHỈ dùng ngắn hạn (1-2 tuần) - không dùng lâu dài",
            "Trong bão giáp: Phải dùng SAU thuốc kháng giáp (ít nhất 1 giờ) - nếu dùng trước sẽ cung cấp iod cho tổng hợp hormone mới",
            "Dị ứng iod: Ngừng ngay nếu có phản ứng dị ứng",
            "Tránh ở bệnh nhân nhân độc (có thể gây cường giáp do iod)",
            "Pha loãng với nước hoặc nước trái cây để giảm kích ứng dạ dày",
            "Dùng ống nhỏ giọt chính xác để tránh quá liều"
        ],
        "contraindications_detail": {
            "tuyệt_đối": [
                "Dị ứng iod",
                "Bệnh da do iod (iododerma)",
                "Viêm mạch do iod"
            ],
            "tương_đối": [
                "Nhân độc tuyến giáp (có thể gây cường giáp do iod)",
                "Bệnh thận (thận trọng với kali)",
                "Bệnh tim (thận trọng với kali)"
            ]
        },
        "renal_adjustment": {
            "normal": "Không cần chỉnh liều.",
            "30_60": "Thận trọng; kali có thể tích lũy.",
            "under_30": "Thận trọng; theo dõi kali máu."
        },
        "hepatic_adjustment": {
            "mild": "Không cần chỉnh liều.",
            "moderate": "Không cần chỉnh liều.",
            "severe": "Không cần chỉnh liều."
        },
        "drug_interactions": {
            "major": [
                {
                    "drug": "Thuốc kháng giáp (Methimazole, PTU)",
                    "mechanism": "Nếu dùng iod TRƯỚC thuốc kháng giáp, iod sẽ cung cấp nguyên liệu để tổng hợp hormone mới.",
                    "effect": "Giảm hiệu quả thuốc kháng giáp, có thể làm nặng cường giáp.",
                    "management": "PHẢI dùng thuốc kháng giáp TRƯỚC, iod SAU (ít nhất 1 giờ)."
                }
            ],
            "moderate": [
                {
                    "drug": "Lithium",
                    "mechanism": "Cộng gộp tác dụng ức chế giải phóng hormone.",
                    "effect": "Tăng nguy cơ suy giáp.",
                    "management": "Theo dõi chức năng tuyến giáp."
                },
                {
                    "drug": "Amiodarone",
                    "mechanism": "Amiodarone đã chứa iod, có thể cộng gộp.",
                    "effect": "Tăng nguy cơ rối loạn chức năng tuyến giáp.",
                    "management": "Thận trọng khi phối hợp."
                }
            ],
            "minor": []
        },
        "overdose_management": {
            "symptoms": [
                "Phản ứng dị ứng nặng: phù mạch, sốc phản vệ",
                "Iododerma nặng: loét da, nhiễm trùng",
                "Cường giáp do iod (Jod-Basedow)",
                "Tăng kali máu (nếu dùng liều rất cao)"
            ],
            "antidote": "Không có antidote đặc hiệu.",
            "treatment": [
                "Ngừng kali iodid ngay.",
                "Điều trị phản ứng dị ứng: epinephrine, steroid, kháng histamine nếu cần.",
                "Điều trị cường giáp do iod: thuốc kháng giáp, chẹn beta.",
                "Điều trị tăng kali máu nếu có.",
                "Điều trị hỗ trợ."
            ],
            "monitoring": "Dấu hiệu dị ứng, chức năng tuyến giáp, kali máu, triệu chứng lâm sàng."
        },
        "reversal_agents": None,
        "administration_instructions": {
            "oral": {
                "with_food": "Pha loãng với nước hoặc nước trái cây để giảm kích ứng dạ dày. Có thể uống với thức ăn.",
                "timing": "Trong bão giáp: 5 giọt mỗi 6-8h, dùng SAU thuốc kháng giáp ít nhất 1 giờ. Dùng ống nhỏ giọt chính xác.",
                "notes": "CHỈ dùng ngắn hạn (1-2 tuần). Không dùng lâu dài. Pha loãng để giảm vị khó chịu và kích ứng dạ dày."
            }
        },
        "pregnancy_lactation": {
            "fda_category": "D",
            "pregnancy_details": "Có thể dùng trong thai kỳ khi cần thiết (bão giáp, chuẩn bị phẫu thuật) nhưng thận trọng. Iod qua nhau thai, có thể ảnh hưởng đến chức năng tuyến giáp thai nhi. Dùng liều thấp nhất hiệu quả, ngắn hạn.",
            "lactation": {
                "safety": "Compatible with caution",
                "details": "Iod bài tiết vào sữa mẹ. Có thể dùng ngắn hạn khi cần thiết nhưng thận trọng. Theo dõi chức năng tuyến giáp của trẻ.",
                "recommendation": "Có thể dùng khi cho con bú nhưng thận trọng, dùng ngắn hạn, liều thấp nhất hiệu quả."
            }
        },
        "pharmacokinetics": {
            "half_life": "Không áp dụng (chất vô cơ)",
            "onset": "1-2 giờ (ức chế giải phóng hormone)",
            "duration": "Ngắn (6-8 giờ)",
            "protein_binding": "Không",
            "metabolism": "Hấp thu nhanh, tích lũy trong tuyến giáp",
            "clearance": "Thải qua nước tiểu, một phần tích lũy trong tuyến giáp"
        },
        "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ánh sáng. Để xa tầm tay trẻ em.",
        "black_box_warnings": "Chỉ dùng ngắn hạn (1-2 tuần). Không dùng lâu dài. Có thể gây phản ứng dị ứng nặng, iododerma. Trong bão giáp, phải dùng SAU thuốc kháng giáp (ít nhất 1 giờ).",
        "references": {
            "primary_sources": [
                "FDA Drug Label - Potassium Iodide (SSKI, Pima)",
                "UpToDate - Thyroid storm treatment",
                "ATA Guidelines - Hyperthyroidism",
                "AACE Guidelines - Thyroid Disorders"
            ],
            "last_updated": "2025-02-18",
            "evidence_level": "High - FDA approved, extensive clinical experience"
        },
        "risk_flags": {
            "high_alert": True,
            "narrow_therapeutic_index": False,
            "icu_critical_care_only": False,
            "bleeding_risk": None,
            "organ_toxicity": {"dermatologic": "Iododerma (skin lesions)", "endocrine": "Iod-induced hyperthyroidism (Jod-Basedow)", "allergic": "Severe allergic reactions (angioedema, anaphylaxis)"},
            "qt_prolongation": False,
            "hepatotoxicity": False,
            "nephrotoxicity": False,
            "requires_monitoring": ["Allergic reactions (angioedema, anaphylaxis risk)", "Thyroid function (if used long-term)", "Potassium levels (if high doses)", "Symptoms of iod-induced hyperthyroidism (Jod-Basedow)"],
            "look_alike_sound_alike": ["Potassium Iodide", "Potassium Chloride"]
        },
        "guideline_tags": [
            "ATA Guidelines - Hyperthyroidism, Thyroid Storm",
            "AACE Guidelines - Thyroid Disorders",
            "WHO Essential Medicines List"
        ],
        "last_updated": "2025-02-18"
    },

    "Carbimazole": {
        "group": "Endocrinology - Antithyroid Drug",
        "pregnancy": "D - Có bằng chứng về nguy cơ. Thận trọng trong thai kỳ",
        "vietnamese_name": "Carbimazole, Neo-Mercazole",
        "brand_names": {
            "common": ["Neo-Mercazole"],
            "vietnam": ["Carbimazole 5/10mg"]
        },
        "administration": ["PO"],
        "indications": [
            "Cường giáp (Hyperthyroidism - Graves' disease)",
            "Bướu giáp độc (Toxic goiter)",
            "Chuẩn bị trước phẫu thuật tuyến giáp"
        ],
        "contraindications": [
            "Dị ứng carbimazole hoặc methimazole",
            "Suy gan nặng",
            "Giảm bạch cầu hạt nặng",
            "Thai kỳ tam cá nguyệt 1 (ưu tiên PTU)"
        ],
        "dosage": {
            "hyperthyroidism": "Khởi đầu 15-40mg/ngày chia 2-3 lần. Giảm dần khi đạt euthyroid. Duy trì: 5-15mg/ngày.",
            "notes": "Carbimazole được chuyển hóa thành methimazole trong cơ thể. Tác dụng tương tự methimazole. Được dùng ở một số nước (Anh, Úc)."
        },
        "side_effects": [
            "Phát ban da (phổ biến, nhẹ)",
            "Suy tủy (Agranulocytosis) - Hiếm nhưng nguy hiểm (0.2-0.5%)",
            "Độc gan (Hepatotoxicity) - Hiếm",
            "Viêm khớp",
            "Giảm vị giác",
            "Rối loạn tiêu hóa"
        ],
        "interactions": [
            "Warfarin: Giảm INR (do cường giáp được điều trị).",
            "Beta-blockers: Dùng kèm để kiểm soát triệu chứng cường giáp."
        ],
        "mechanism_of_action": "Carbimazole là tiền chất (prodrug) của methimazole. Sau khi uống, carbimazole được chuyển hóa thành methimazole trong cơ thể. Methimazole ức chế enzyme thyroid peroxidase (TPO), ngăn cản tổng hợp hormone tuyến giáp (T3, T4). Tác dụng tương tự methimazole.",
        "monitoring": [
            "Công thức máu (CBC) - Trước điều trị và khi có triệu chứng nhiễm trùng (phát hiện agranulocytosis)",
            "Free T4, T3, TSH - Mỗi 4-6 tuần khi điều chỉnh liều",
            "Men gan (ALT, AST) - Định kỳ",
            "Dấu hiệu nhiễm trùng (sốt, đau họng - nghi ngờ agranulocytosis)"
        ],
        "precautions": [
            "Nguy cơ suy tủy (Agranulocytosis) - NGỪNG THUỐC NGAY nếu sốt, đau họng, nhiễm trùng",
            "Kiểm tra CBC nếu có triệu chứng nhiễm trùng",
            "Thai kỳ tam cá nguyệt 1: Ưu tiên PTU (carbimazole/methimazole có nguy cơ quái thai)",
            "Tác dụng chậm (4-6 tuần) - Cần kiên nhẫn",
            "Dùng kèm beta-blocker (Propranolol) để kiểm soát triệu chứng cường giáp"
        ],
        "contraindications_detail": {
            "tuyệt_đối": [
                "Dị ứng với carbimazole hoặc methimazole",
                "Thai kỳ tam cá nguyệt 1 (ưu tiên PTU)",
                "Tiền sử viêm gan nặng do carbimazole/methimazole",
                "Bạch cầu trung tính <1500/mm3",
                "Suy gan nặng"
            ],
            "tương_đối": [
                "Bệnh gan mạn/men gan tăng sẵn",
                "Suy tủy, giảm bạch cầu hạt",
                "Người cao tuổi hoặc có bệnh tim nặng (titrate chậm)"
            ]
        },
        "renal_adjustment": {
            "normal": "Không cần chỉnh liều.",
            "30_60": "Không cần chỉnh liều; theo dõi độc tính.",
            "under_30": "Không cần chỉnh liều; theo dõi sát CBC/men gan."
        },
        "hepatic_adjustment": {
            "mild": "Thận trọng; theo dõi men gan.",
            "moderate": "Tránh hoặc dùng liều thấp, theo dõi sát.",
            "severe": "Chống chỉ định do nguy cơ độc gan.",
            "notes": "Ngừng thuốc nếu men gan tăng đáng kể hoặc vàng da."
        },
        "drug_interactions": {
            "major": [
                {
                    "drug": "Warfarin",
                    "mechanism": "Điều chỉnh cường giáp làm giảm độ nhạy với warfarin.",
                    "effect": "INR giảm khi trạng thái cường giáp được kiểm soát.",
                    "management": "Theo dõi INR và điều chỉnh liều warfarin."
                }
            ],
            "moderate": [
                {
                    "drug": "Clozapine hoặc thuốc gây giảm bạch cầu",
                    "mechanism": "Cộng gộp nguy cơ giảm bạch cầu hạt.",
                    "effect": "Tăng nguy cơ agranulocytosis.",
                    "management": "Tránh phối hợp nếu có thể; theo dõi CBC sát."
                }
            ],
            "minor": []
        },
        "overdose_management": {
            "symptoms": [
                "Giảm bạch cầu hạt, sốt, đau họng",
                "Vàng da, tăng men gan",
                "Buồn nôn, đau bụng"
            ],
            "antidote": "Không có antidote đặc hiệu.",
            "treatment": [
                "Ngừng carbimazole ngay.",
                "Hỗ trợ: truyền dịch, kiểm soát triệu chứng.",
                "CBC/men gan khẩn; G-CSF nếu agranulocytosis nặng.",
                "Kháng sinh nếu nhiễm trùng."
            ],
            "monitoring": "CBC, men gan, dấu hiệu nhiễm trùng."
        },
        "reversal_agents": None,
        "administration_instructions": {
            "oral": {
                "with_food": "Có thể uống cùng hoặc không cùng thức ăn.",
                "timing": "Chia 2-3 lần/ngày; uống cùng giờ mỗi ngày.",
                "notes": "Uống cùng giờ mỗi ngày; không tự ý ngừng."
            }
        },
        "black_box_warnings": "Nguy cơ suy tủy (Agranulocytosis) nghiêm trọng, có thể tử vong. Ngừng thuốc ngay nếu có sốt, đau họng, nhiễm trùng.",
        "references": {
            "primary_sources": [
                "FDA Drug Label - Carbimazole (Neo-Mercazole)",
                "UpToDate - Carbimazole: Drug information",
                "ATA Guidelines - Hyperthyroidism",
                "AACE Guidelines - Thyroid Disorders"
            ],
            "last_updated": "2025-02-18",
            "evidence_level": "High - FDA approved, extensive clinical experience"
        },
        "risk_flags": {
            "high_alert": True,
            "narrow_therapeutic_index": False,
            "icu_critical_care_only": False,
            "bleeding_risk": None,
            "organ_toxicity": {"hematologic": "Black Box Warning - Agranulocytosis (may be fatal)", "hepatic": "Hepatotoxicity", "dermatologic": "Rash (common), SJS/TEN (rare)", "teratogenic": "Teratogenicity (first trimester - prefer PTU)"},
            "qt_prolongation": False,
            "hepatotoxicity": True,
            "nephrotoxicity": False,
            "requires_monitoring": ["CBC (Black Box Warning - agranulocytosis, stop immediately if fever/sore throat/infection)", "Hepatic function (ALT, AST)", "Free T4, T3, TSH (thyroid function)", "Infection signs (fever, sore throat - agranulocytosis risk)"],
            "look_alike_sound_alike": ["Carbimazole", "Methimazole"]
        },
        "guideline_tags": [
            "FDA Black Box Warning - Agranulocytosis (may be fatal)",
            "ATA Guidelines - Hyperthyroidism",
            "AACE Guidelines - Thyroid Disorders",
            "WHO Essential Medicines List"
        ],
        "last_updated": "2025-02-18"
    }
}
