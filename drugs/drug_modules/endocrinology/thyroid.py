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
    }
}
