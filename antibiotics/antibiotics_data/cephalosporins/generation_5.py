"""
Cephalosporins - Generation 5
"""

GENERATION_5 = {
    "Ceftaroline": {
        "group": "Beta-lactam - Cephalosporin thế hệ 5",
        "vietnamese_name": "Ceftaroline, Teflaro, Ceftaroline",
        "administration": ["IV"],
        "indications": [
            "Nhiễm khuẩn da và mô mềm do MRSA",
            "Viêm phổi cộng đồng do MRSA",
            "Nhiễm khuẩn do MRSA (khi vancomycin không phù hợp)"
        ],
        "contraindications": [
            "Dị ứng cephalosporin",
            "Dị ứng penicillin nặng"
        ],
        "dosage": {
            "adult_standard": "600mg IV mỗi 12 giờ",
            "adult_impaired": "400mg IV mỗi 12 giờ (CrCl 30-50)",
            "adult_severe_renal": "400mg IV mỗi 24 giờ (CrCl <30)",
            "pediatric": "Không khuyến cáo <18 tuổi",
            "notes": "Cephalosporin duy nhất hoạt động chống MRSA. Đắt tiền, chỉ dùng khi cần"
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "400mg mỗi 12 giờ",
            "15_30": "400mg mỗi 24 giờ",
            "under_15": "300mg mỗi 24 giờ hoặc lọc máu"
        },
        "side_effects": [
            "Tiêu chảy",
            "Phát ban",
            "Viêm tĩnh mạch",
            "Tăng transaminase"
        ],
        "interactions": [
            "Warfarin: tăng nguy cơ chảy máu"
        ],
        "aware_classification": "RESERVE",
        "pregnancy": "B"
    },

    "Ceftobiprole": {
        "group": "Beta-lactam - Cephalosporin (5th Generation)",
        "vietnamese_name": "Ceftobiprole, Zevtera, Mabelio",
        "administration": ["IV"],
        "indications": [
            "Viêm phổi bệnh viện (HAP)",
            "Viêm phổi thở máy (VAP)",
            "Nhiễm khuẩn da và mô mềm phức tạp",
            "MRSA (Methicillin-Resistant S. aureus)",
            "Nhiễm khuẩn do P. aeruginosa",
            "Nhiễm khuẩn do vi khuẩn gram dương và gram âm"
        ],
        "contraindications": [
            "Dị ứng cephalosporin/penicillin",
            "Sốc phản vệ beta-lactam"
        ],
        "dosage": {
            "adult_iv": "500mg IV mỗi 8 giờ (truyền trong 2 giờ)",
            "adult_iv_severe": "500mg IV mỗi 8 giờ",
            "notes": "Phổ rộng bao gồm MRSA và P. aeruginosa. Phải truyền trong 2 giờ (không bolus)"
        },
        "renal_adjustment": {
            "normal": "500mg mỗi 8 giờ",
            "30_60": "500mg mỗi 12 giờ",
            "15_30": "250mg mỗi 12 giờ",
            "under_15": "250mg mỗi 24 giờ hoặc lọc máu (liều sau lọc máu)"
        },
        "side_effects": [
            "Tiêu chảy",
            "Buồn nôn, nôn",
            "Phản ứng dị ứng",
            "Rối loạn vị giác",
            "Viêm tĩnh mạch"
        ],
        "interactions": [
            "Probenecid: tăng nồng độ ceftobiprole",
            "Warfarin: tăng nguy cơ chảy máu (theo dõi PT/INR)"
        ],
        "monitoring": "LFT, công thức máu, dấu hiệu nhiễm trùng",
        "aware_classification": "RESERVE",
        "pregnancy": "B - Dữ liệu hạn chế nhưng không thấy nguy cơ rõ ràng",
        "notes": "Cephalosporin thế hệ 5, phổ rộng bao gồm MRSA và P. aeruginosa. Phải truyền trong 2 giờ (không bolus)"
    },
}

