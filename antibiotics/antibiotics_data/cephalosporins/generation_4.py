"""
Cephalosporins - Generation 4
"""

GENERATION_4 = {
    "Cefepime": {
        "group": "Beta-lactam - Cephalosporin thế hệ 4",
        "vietnamese_name": "Cefepime, Maxipime, Cefepim, Maxipim, Cefomax, Cepime, Cefepimax, Cepim",
        "administration": ["IV", "IM"],
        "indications": [
            "Nhiễm khuẩn bệnh viện",
            "Viêm phổi bệnh viện",
            "Nhiễm khuẩn huyết",
            "Nhiễm khuẩn do Pseudomonas (khi ceftazidime không có)",
            "Sốt giảm bạch cầu hạt"
        ],
        "contraindications": [
            "Dị ứng cephalosporin",
            "Suy thận nặng (nguy cơ rối loạn thần kinh)"
        ],
        "dosage": {
            "adult_standard": "1-2g IV mỗi 12 giờ",
            "adult_severe": "2g IV mỗi 8 giờ",
            "adult_neutropenia": "2g IV mỗi 8 giờ",
            "pediatric": "100-150mg/kg/ngày chia 2-3 lần (max 6g/ngày)",
            "notes": "Phổ rộng hơn ceftriaxone, hoạt động tốt chống Pseudomonas"
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "1-2g mỗi 12 giờ",
            "15_30": "1-2g mỗi 24 giờ",
            "under_15": "1g mỗi 24 giờ hoặc lọc máu"
        },
        "side_effects": [
            "Rối loạn thần kinh (lú lẫn, co giật) - đặc biệt suy thận",
            "Phát ban",
            "Tiêu chảy",
            "Viêm tĩnh mạch"
        ],
        "interactions": [
            "Aminoglycosides: không pha cùng",
            "Warfarin: tăng nguy cơ chảy máu"
        ],
        "aware_classification": "WATCH",
        "pregnancy": "B"
    },
}

