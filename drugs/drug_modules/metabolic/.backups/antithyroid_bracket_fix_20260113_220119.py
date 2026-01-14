"""
Antithyroid Medications - Metabolic and Endocrine Medications
"""

ANTITHYROID_DRUGS = {
    "Methimazole": {
        "group": "Endocrinology - Antithyroid (Thionamide)",
        "vietnamese_name": "Methimazole, Tapazole",
        "administration": ["PO"],
        "indications": [
            "Cường giáp (hyperthyroidism)",
            "Bệnh Graves",
            "Bướu cổ độc (toxic goiter)",
            "Chuẩn bị trước phẫu thuật tuyến giáp",
            "Điều trị cường giáp trước phóng xạ iod"
        ],
        "contraindications": [
            "Dị ứng methimazole",
            "Có thai (3 tháng đầu - dùng PTU)",
            "Đang cho con bú (ưu tiên PTU)",
            "Giảm bạch cầu nặng"
        ],
        "dosage": {
            "adult_mild": "15-30mg/ngày chia 1-3 lần",
            "adult_moderate": "30-45mg/ngày chia 2-3 lần",
            "adult_severe": "40-60mg/ngày chia 2-3 lần",
            "adult_maintenance": "5-15mg/ngày chia 1-2 lần",
            "notes": "Khởi đầu với liều cao, giảm dần khi đạt bình giáp. Điều trị 12-18 tháng"
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "Không đổi",
            "under_30": "Không đổi"
        },
        "side_effects": [
            "Giảm bạch cầu, giảm tiểu cầu (nguy hiểm - theo dõi công thức máu)",
            "Phát ban",
            "Ngứa",
            "Đau khớp",
            "Rối loạn vị giác",
            "Độc gan (hiếm nhưng nguy hiểm)",
            "Agranulocytosis (mất bạch cầu - hiếm nhưng nguy hiểm)"
        ],
        "interactions": [
            "Warfarin: có thể cần giảm liều warfarin (khi đạt bình giáp)",
            "Digoxin: có thể cần giảm liều digoxin"
        ],
        "pregnancy": "D - Tránh trong 3 tháng đầu (dùng PTU). Thận trọng sau đó",
        "mechanism_of_action": "Ức chế enzyme thyroid peroxidase (TPO), ngăn cản quá trình iod hóa tyrosine và ghép nối các iodotyrosine để tạo thành T3 và T4. Methimazole ức chế cả quá trình tổng hợp và giải phóng hormone tuyến giáp, dẫn đến giảm nồng độ T3 và T4 trong máu, giảm triệu chứng cường giáp",
        "monitoring": [
            "Công thức máu toàn phần (CBC) mỗi tuần trong 3 tháng đầu, sau đó mỗi tháng (theo dõi agranulocytosis)",
            "Chức năng gan (ALT, AST, bilirubin) mỗi 1-2 tháng",
            "TSH, FT3, FT4 mỗi 4-6 tuần khi điều chỉnh liều, sau đó mỗi 3-6 tháng",
            "Dấu hiệu nhiễm trùng (sốt, viêm họng - có thể là dấu hiệu agranulocytosis)",
            "Dấu hiệu độc gan (vàng da, mệt mỏi, đau bụng)"
        ],
        "precautions": [
            "Khởi đầu với liều cao (30-60mg/ngày), giảm dần khi đạt bình giáp",
            "Ngừng ngay nếu có sốt, viêm họng (dấu hiệu agranulocytosis - cấp cứu)",
            "Ngừng ngay nếu có dấu hiệu độc gan (vàng da, tăng ALT/AST)",
            "Tránh dùng trong 3 tháng đầu thai kỳ (dùng PTU thay thế)",
            "Có thể dùng trong cho con bú nhưng ưu tiên PTU",
            "Theo dõi sát công thức máu, đặc biệt trong 3 tháng đầu",
            "Có thể gây dị tật thai nhi nếu dùng trong thai kỳ (teratogenic)"
        ],
        "pharmacokinetics": {
            "half_life": "4-6 giờ (ngắn)",
            "onset": "1-2 tuần (giảm T3/T4)",
            "duration": "12-24 giờ (tác dụng kéo dài do tích lũy trong tuyến giáp)",
            "protein_binding": "Minimal",
            "clearance": "Gan (chuyển hóa), thận (thải trừ)"
        },
        "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm, tránh ánh sáng",
        "black_box_warnings": "Có thể gây agranulocytosis (mất bạch cầu) - nguy hiểm tính mạng. Bệnh nhân cần được hướng dẫn ngừng thuốc và đến bệnh viện ngay nếu có sốt, viêm họng. Có thể gây dị tật thai nhi nếu dùng trong thai kỳ",
        "drug_interactions": {
            "major": [
                {
                    "drug": "Warfarin",
                    "mechanism": "Khi đạt bình giáp, nhu cầu warfarin giảm, tăng nguy cơ chảy máu.",
                    "effect": "Tăng tác dụng chống đông, tăng INR, tăng nguy cơ chảy máu",
                    "management": "Theo dõi INR chặt chẽ khi điều chỉnh liều methimazole. Giảm liều warfarin khi đạt bình giáp."
                }
            ],
            "moderate": [
                {
                    "drug": "Digoxin",
                    "mechanism": "Khi đạt bình giáp, nhu cầu digoxin giảm.",
                    "effect": "Tăng nồng độ digoxin, tăng nguy cơ độc tính",
                    "management": "Theo dõi nồng độ digoxin và điều chỉnh liều khi đạt bình giáp."
                }
            ],
            "minor": []
        },
        "contraindications": {
            "tuyệt_đối": [
                "Dị ứng methimazole",
                "Có thai (3 tháng đầu - dùng PTU thay thế)",
                "Giảm bạch cầu nặng"
            ],
            "tương_đối": [
                "Đang cho con bú (ưu tiên PTU)",
                "Suy gan (thận trọng, theo dõi chức năng gan)"
            ]
        },
        "pregnancy_lactation": {
            "fda_category": "D",
            "pregnancy_details": "Methimazole có thể gây dị tật thai nhi (aplasia cutis, choanal atresia, esophageal atresia) nếu dùng trong tam cá nguyệt đầu. Tránh dùng trong 3 tháng đầu thai kỳ, dùng PTU thay thế. Sau tam cá nguyệt đầu, có thể dùng methimazole nhưng thận trọng. Dùng liều thấp nhất hiệu quả.",
            "lactation": {
                "safety": "Compatible with caution",
                "details": "Methimazole bài tiết vào sữa mẹ ở nồng độ thấp. Có thể dùng nhưng ưu tiên PTU. Theo dõi chức năng tuyến giáp của trẻ.",
                "recommendation": "Có thể dùng khi cho con bú nhưng ưu tiên PTU. Dùng liều thấp nhất hiệu quả. Theo dõi chức năng tuyến giáp của trẻ."
            }
        },
        "hepatic_adjustment": {
            "mild": "Không cần điều chỉnh liều. Theo dõi chức năng gan.",
            "moderate": "Thận trọng, theo dõi chức năng gan chặt chẽ. Có thể cần giảm liều.",
            "severe": "Thận trọng, theo dõi chức năng gan chặt chẽ. Có thể cần giảm liều hoặc dùng PTU thay thế.",
            "notes": "Methimazole chuyển hóa qua gan. Suy gan có thể làm tăng nồng độ và độc tính. Theo dõi ALT, AST định kỳ."
        },
        "overdose_management": {
            "symptoms": [
                "Giảm bạch cầu, agranulocytosis (sốt, viêm họng, nhiễm trùng)",
                "Độc gan (vàng da, tăng ALT/AST)",
                "Phát ban nặng",
                "Rối loạn vị giác"
            ],
            "antidote": "Không có antidote đặc hiệu. Điều trị hỗ trợ.",
            "treatment": [
                "Ngừng methimazole ngay lập tức",
                "Nếu agranulocytosis: điều trị nhiễm trùng, có thể cần G-CSF",
                "Nếu độc gan: điều trị hỗ trợ gan, có thể cần N-acetylcysteine",
                "Theo dõi công thức máu và chức năng gan",
                "Có thể cần dùng PTU thay thế nếu vẫn cần điều trị cường giáp"
            ],
            "monitoring": "Công thức máu, chức năng gan, dấu hiệu nhiễm trùng"
        },
        "reversal_agents": {
            "available": False,
            "agents": []
        },
        "administration_instructions": {
            "oral": {
                "with_food": "Có thể uống với hoặc không thức ăn. Uống với thức ăn có thể giảm kích ứng dạ dày.",
                "timing": "Uống 1-3 lần/ngày tùy liều. Có thể uống cùng thời điểm mỗi ngày."
            },
            "iv": {
                "reconstitution": "Không có dạng IV",
                "infusion_rate": "N/A",
                "compatibility": [],
                "incompatibility": [],
                "notes": "Chỉ có dạng uống"
            }
        },
        "references": {
            "primary_sources": [
                "FDA Drug Label - Methimazole (Tapazole)",
                "American Thyroid Association Guidelines - Hyperthyroidism",
                "UpToDate - Hyperthyroidism treatment",
                "Goodman & Gilman's The Pharmacological Basis of Therapeutics (14th ed)"
            ],
            "last_updated": "2024-12-19",
            "evidence_level": "A - Dựa trên FDA drug labels, ATA guidelines, và dữ liệu lâm sàng"
        },
        "risk_flags": {
            "high_alert": True,
            "narrow_therapeutic_index": False,
            "bleeding_risk": False,
            "organ_toxicity": ["hepatic", "hematologic"],
            "qt_prolongation": False,
            "hepatotoxicity": True,
            "nephrotoxicity": False,
            "requires_monitoring": ["CBC", "LFT", "Thyroid Function Tests"]
        },
        "guideline_tags": [
            "FDA Drug Label - Methimazole (Tapazole)",
            "American Thyroid Association Guidelines - Hyperthyroidism",
            "ISMP High Alert Medications - Antithyroid Drugs"
        ]
    },
    "Propylthiouracil": {
        "group": "Endocrinology - Antithyroid (Thionamide)",
        "vietnamese_name": "Propylthiouracil, PTU",
        "administration": ["PO"],
        "indications": [
            "Cường giáp (hyperthyroidism)",
            "Bệnh Graves",
            "Bướu cổ độc",
            "Có thai (3 tháng đầu - ưu tiên hơn methimazole)",
            "Cường giáp cấp (thyroid storm)"
        ],
        "contraindications": [
            "Dị ứng propylthiouracil",
            "Giảm bạch cầu nặng",
            "Đang cho con bú (có thể dùng)"
        ],
        "dosage": {
            "adult_mild": "100-150mg x 3 lần/ngày",
            "adult_moderate": "150-200mg x 3 lần/ngày",
            "adult_severe": "200-300mg x 3-4 lần/ngày",
            "adult_storm": "200-300mg x 4 lần/ngày",
            "adult_maintenance": "50-150mg/ngày chia 1-3 lần",
            "notes": "Ưu tiên hơn methimazole trong 3 tháng đầu thai kỳ. Nhiều tác dụng phụ gan hơn"
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "Không đổi",
            "under_30": "Thận trọng"
        },
        "side_effects": [
            "Độc gan (cao hơn methimazole, có thể suy gan cấp)",
            "Giảm bạch cầu, agranulocytosis",
            "Phát ban",
            "Ngứa",
            "Đau khớp",
            "Vasculitis (hiếm)",
            "Lupus-like syndrome (hiếm)"
        ],
        "interactions": [
            "Warfarin: có thể cần giảm liều warfarin",
            "Digoxin: có thể cần giảm liều digoxin"
        ],',
"pregnancy": "D - An toàn hơn methimazole trong 3 tháng đầu, nhưng vẫn thận trọng",
        "mechanism_of_action": "Ức chế enzyme thyroid peroxidase (TPO), ngăn cản quá trình iod hóa tyrosine và ghép nối các iodotyrosine để tạo thành T3 và T4. Propylthiouracil còn ức chế chuyển đổi T4 thành T3 ở mô ngoại vi (ức chế 5'-deiodinase), giảm nhanh T3 hơn so với methimazole. Dẫn đến giảm nồng độ T3 và T4, giảm triệu chứng cường giáp",
        "monitoring": [
            "Công thức máu toàn phần (CBC) mỗi tuần trong 3 tháng đầu, sau đó mỗi tháng (theo dõi agranulocytosis)",
            "Chức năng gan (ALT, AST, bilirubin) mỗi 1-2 tháng (nguy cơ độc gan cao hơn methimazole)",
            "TSH, FT3, FT4 mỗi 4-6 tuần khi điều chỉnh liều, sau đó mỗi 3-6 tháng",
            "Dấu hiệu nhiễm trùng (sốt, viêm họng - có thể là dấu hiệu agranulocytosis)",
            "Dấu hiệu độc gan (vàng da, mệt mỏi, đau bụng, suy gan cấp)",
            "Dấu hiệu vasculitis (phát ban, đau khớp, tổn thương da)"
        ],
        "precautions": [
            "Khởi đầu với liều cao (600-900mg/ngày chia 3-4 lần), giảm dần khi đạt bình giáp",
            "Ngừng ngay nếu có sốt, viêm họng (dấu hiệu agranulocytosis - cấp cứu)",
            "Ngừng ngay nếu có dấu hiệu độc gan (vàng da, tăng ALT/AST, suy gan cấp)",
            "Ưu tiên hơn methimazole trong 3 tháng đầu thai kỳ (ít nguy cơ dị tật hơn)",
            "Có thể dùng trong cho con bú (an toàn hơn methimazole)",
            "Theo dõi sát chức năng gan (nguy cơ độc gan cao hơn methimazole)",
            "Cần dùng nhiều lần/ngày (3-4 lần) do thời gian bán thải ngắn",
            "Có thể gây vasculitis và lupus-like syndrome (hiếm)"
        ],
        "pharmacokinetics": {
            "half_life": "1-2 giờ (rất ngắn)",
            "onset": "1-2 tuần (giảm T3/T4)",
            "duration": "6-8 giờ (ngắn hơn methimazole)",
            "protein_binding": "Minimal",
            "clearance": "Gan (chuyển hóa chủ yếu), thận (thải trừ)"
        },
        "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm, tránh ánh sáng",
        "black_box_warnings": "Có thể gây suy gan cấp nặng và tử vong. Theo dõi sát chức năng gan và ngừng ngay nếu có dấu hiệu độc gan. Có thể gây agranulocytosis (mất bạch cầu) - nguy hiểm tính mạng",
        "drug_interactions": {
            "major": [
                {
                    "drug": "Warfarin",
                    "mechanism": "Khi đạt bình giáp, nhu cầu warfarin giảm.",
                    "effect": "Tăng tác dụng chống đông, tăng INR",
                    "management": "Theo dõi INR chặt chẽ, giảm liều warfarin khi đạt bình giáp."
                }
            ],
            "moderate": [
                {
                    "drug": "Digoxin",
                    "mechanism": "Khi đạt bình giáp, nhu cầu digoxin giảm.",
                    "effect": "Tăng nồng độ digoxin",
                    "management": "Theo dõi nồng độ digoxin và điều chỉnh liều."
                }
            ],
            "minor": []
        },
        "contraindications": {
            "tuyệt_đối": [
                "Dị ứng propylthiouracil",
                "Giảm bạch cầu nặng",
                "Suy gan nặng"
            ],
            "tương_đối": [
                "Suy thận (thận trọng, giảm liều)",
                "Đang cho con bú (có thể dùng)"
            ]
        },
        "pregnancy_lactation": {
            "fda_category": "D",
            "pregnancy_details": "PTU ưu tiên hơn methimazole trong 3 tháng đầu thai kỳ (ít nguy cơ dị tật hơn). Sau tam cá nguyệt đầu, có thể dùng methimazole. Dùng liều thấp nhất hiệu quả.",
            "lactation": {
                "safety": "Compatible",
                "details": "PTU bài tiết vào sữa mẹ ở nồng độ thấp. An toàn hơn methimazole khi cho con bú.",
                "recommendation": "Có thể dùng khi cho con bú. Dùng liều thấp nhất hiệu quả."
            }
        },
        "hepatic_adjustment": {
            "mild": "Thận trọng, theo dõi chức năng gan.",
            "moderate": "Thận trọng, theo dõi chức năng gan chặt chẽ. Có thể cần giảm liều.",
            "severe": "Chống chỉ định hoặc thận trọng tối đa. Nguy cơ suy gan cấp cao.",
            "notes": "PTU có nguy cơ độc gan cao hơn methimazole. Theo dõi ALT, AST định kỳ. Ngừng ngay nếu có dấu hiệu độc gan."
        },
        "overdose_management": {
            "symptoms": [
                "Suy gan cấp (vàng da, tăng ALT/AST, suy gan)",
                "Agranulocytosis (sốt, viêm họng, nhiễm trùng)",
                "Phát ban nặng",
                "Vasculitis"
            ],
            "antidote": "Không có antidote đặc hiệu. Điều trị hỗ trợ.",
            "treatment": [
                "Ngừng PTU ngay lập tức",
                "Nếu suy gan cấp: điều trị hỗ trợ gan, có thể cần N-acetylcysteine, xem xét ghép gan nếu nặng",
                "Nếu agranulocytosis: điều trị nhiễm trùng, có thể cần G-CSF",
                "Theo dõi chức năng gan và công thức máu"
            ],
            "monitoring": "Chức năng gan, công thức máu, dấu hiệu nhiễm trùng"
        },
        "reversal_agents": {
            "available": False,
            "agents": []
        },
        "administration_instructions": {
            "oral": {
                "with_food": "Có thể uống với hoặc không thức ăn.",
                "timing": "Uống 3-4 lần/ngày do thời gian bán thải ngắn. Uống cùng thời điểm mỗi ngày."
            },
            "iv": {
                "reconstitution": "Không có dạng IV",
                "infusion_rate": "N/A",
                "compatibility": [],
                "incompatibility": [],
                "notes": "Chỉ có dạng uống"
            }
        },
        "references": {
            "primary_sources": [
                "FDA Drug Label - Propylthiouracil (PTU)",
                "American Thyroid Association Guidelines - Hyperthyroidism",
                "UpToDate - Hyperthyroidism treatment",
                "Goodman & Gilman's The Pharmacological Basis of Therapeutics (14th ed)"
            ],
            "last_updated": "2024-12-19",
            "evidence_level": "A - Dựa trên FDA drug labels, ATA guidelines, và dữ liệu lâm sàng"
        },
        "risk_flags": {
            "high_alert": True,
            "narrow_therapeutic_index": False,
            "bleeding_risk": False,
            "organ_toxicity": ["hepatic", "hematologic"],
            "qt_prolongation": False,
            "hepatotoxicity": True,
            "nephrotoxicity": False,
            "requires_monitoring": ["CBC", "LFT", "Thyroid Function Tests"]
        },
        "guideline_tags": [
            "FDA Drug Label - Propylthiouracil (PTU)",
            "American Thyroid Association Guidelines - Hyperthyroidism",
            "ISMP High Alert Medications - Antithyroid Drugs"
        ]
    },
}

__all__ = ['ANTITHYROID_DRUGS']
