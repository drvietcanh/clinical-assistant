"""
Cephalosporins - Generation 2
"""

GENERATION_2 = {
    "Cefuroxime": {
        "group": "Beta-lactam - Cephalosporin thế hệ 2",
        "vietnamese_name": "Cefuroxime, Zinacef, Cefurox",
        "administration": ["IV", "IM"],
        "indications": [
            "Viêm phổi cộng đồng",
            "Nhiễm khuẩn đường tiết niệu",
            "Nhiễm khuẩn da và mô mềm",
            "Viêm xương tủy"
        ],
        "contraindications": [
            "Dị ứng cephalosporin",
            "Dị ứng penicillin nặng (phản ứng chéo)"
        ],
        "dosage": {
            "adult_iv": "750mg-1.5g IV mỗi 8 giờ",
            "adult_im": "750mg IM mỗi 8 giờ",
            "adult_severe": "1.5g IV mỗi 8 giờ",
            "pediatric_iv": "75-150mg/kg/ngày chia 3 lần (max 6g/ngày)",
            "notes": "Phổ rộng hơn cefazolin, kháng beta-lactamase tốt hơn"
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "Giảm liều 25-50%",
            "15_30": "750mg mỗi 12 giờ",
            "under_15": "750mg mỗi 24 giờ"
        },
        "side_effects": [
            "Tiêu chảy",
            "Phát ban",
            "Viêm tĩnh mạch"
        ],
        "interactions": [
            "Warfarin: tăng nguy cơ chảy máu",
            "Probenecid: tăng nồng độ"
        ],
        "aware_classification": "ACCESS",
        "pregnancy": "B"
    },

    "Cefaclor": {
        "group": "Beta-lactam - Cephalosporin thế hệ 2 (Oral)",
        "vietnamese_name": "Cefaclor, Ceclor, Cefaclor, Cefador, Cefalor, Ceclor, Cefac, Cefaclorin",
        "administration": ["PO"],
        "indications": [
            "Viêm phổi cộng đồng nhẹ",
            "Viêm tai giữa",
            "Viêm xoang cấp",
            "Viêm họng/amidan",
            "Nhiễm khuẩn da và mô mềm",
            "Nhiễm khuẩn đường tiết niệu"
        ],
        "contraindications": [
            "Dị ứng cephalosporin/penicillin"
        ],
        "dosage": {
            "adult_standard": "250-500mg PO x 3 lần/ngày",
            "adult_severe": "500mg PO x 3 lần/ngày",
            "pediatric_standard": "20-40mg/kg/ngày chia 3 lần (max 1g/ngày)",
            "pediatric_otitis": "40mg/kg/ngày chia 3 lần",
            "notes": "Cephalosporin thế hệ 2, phổ trung bình. Dùng với thức ăn để giảm khó chịu dạ dày"
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "Giảm liều 25-50%",
            "15_30": "Giảm liều 50%",
            "under_15": "250mg mỗi 12-24 giờ"
        },
        "side_effects": [
            "Tiêu chảy (2-3%)",
            "Buồn nôn, nôn",
            "Phát ban",
            "Nhức đầu",
            "Rối loạn chức năng gan (hiếm)"
        ],
        "interactions": [
            "Probenecid: tăng nồng độ",
            "Warfarin: tăng nguy cơ chảy máu"
        ],
        "monitoring": "LFT nếu có triệu chứng",
        "aware_classification": "ACCESS",
        "pregnancy": "B"
    },
}

