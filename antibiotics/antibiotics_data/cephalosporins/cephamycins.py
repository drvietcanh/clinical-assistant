"""
Cephalosporins - Cephamycins
"""

CEPHAMYCINS = {
    "Cefotetan": {
        "group": "Beta-lactam - Cephamycin",
        "vietnamese_name": "Cefotetan, Cefotan",
        "administration": ["IV", "IM"],
        "indications": [
            "Nhiễm khuẩn ổ bụng (phẫu thuật)",
            "Nhiễm khuẩn phụ khoa",
            "Nhiễm khuẩn đường tiết niệu phức tạp",
            "Phẫu thuật đại tràng (prophylaxis)",
            "Nhiễm khuẩn do vi khuẩn kỵ khí + gram âm"
        ],
        "contraindications": [
            "Dị ứng cephalosporin/penicillin",
            "Sốc phản vệ beta-lactam",
            "Phụ nữ có thai (chống chỉ định)"
        ],
        "dosage": {
            "adult_iv": "1-2g IV mỗi 12 giờ (2-4g/ngày)",
            "adult_im": "1-2g IM mỗi 12 giờ",
            "prophylaxis_iv": "1-2g IV trước phẫu thuật",
            "adult_iv_severe": "2g IV mỗi 12 giờ (4g/ngày)",
            "notes": "Phổ rộng bao gồm kỵ khí. Có disulfiram-like effect. Chống chỉ định thai kỳ"
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "1-2g mỗi 24 giờ",
            "15_30": "1-2g mỗi 24 giờ",
            "under_15": "0.5-1g mỗi 24 giờ hoặc lọc máu"
        },
        "side_effects": [
            "Phản ứng disulfiram (rượu)",
            "Rối loạn đông máu (hypoprothrombinemia)",
            "Tiêu chảy",
            "Phản ứng dị ứng",
            "Viêm tĩnh mạch"
        ],
        "interactions": [
            "Rượu: phản ứng disulfiram (đỏ mặt, nôn, tim đập nhanh)",
            "Warfarin: tăng nguy cơ chảy máu",
            "Vitamin K: cần bổ sung trong điều trị dài ngày"
        ],
        "monitoring": "PT/INR, dấu hiệu chảy máu",
        "aware_classification": "WATCH",
        "pregnancy": "X - Chống chỉ định trong thai kỳ (gây quái thai trong thí nghiệm)",
        "notes": "Chống chỉ định thai kỳ. Phản ứng disulfiram với rượu. Phổ kỵ khí tốt"
    },

    "Cefoxitin": {
        "group": "Beta-lactam - Cephamycin",
        "vietnamese_name": "Cefoxitin, Mefoxin",
        "administration": ["IV", "IM"],
        "indications": [
            "Nhiễm khuẩn ổ bụng",
            "Nhiễm khuẩn phụ khoa",
            "Viêm nội mạc tử cung",
            "Nhiễm khuẩn đường tiết niệu phức tạp",
            "Nhiễm khuẩn da và mô mềm có kỵ khí",
            "Phẫu thuật đại tràng (prophylaxis)"
        ],
        "contraindications": [
            "Dị ứng cephalosporin/penicillin",
            "Sốc phản vệ beta-lactam"
        ],
        "dosage": {
            "adult_iv": "1-2g IV mỗi 6-8 giờ (3-8g/ngày)",
            "adult_im": "1-2g IM mỗi 6-8 giờ",
            "prophylaxis_iv": "1-2g IV trước phẫu thuật",
            "adult_iv_severe": "2g IV mỗi 6 giờ (8g/ngày)",
            "pediatric_iv": "80-160mg/kg/ngày chia 4-6 lần (tối đa 12g/ngày)",
            "notes": "Phổ rộng bao gồm kỵ khí. Tương tự cefotetan nhưng an toàn hơn trong thai kỳ"
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "1-2g mỗi 8-12 giờ",
            "15_30": "1-2g mỗi 12 giờ",
            "under_15": "0.5-1g mỗi 12-24 giờ hoặc lọc máu"
        },
        "side_effects": [
            "Tiêu chảy",
            "Phản ứng dị ứng",
            "Viêm tĩnh mạch",
            "Rối loạn chức năng gan nhẹ"
        ],
        "interactions": [
            "Probenecid: tăng nồng độ cefoxitin",
            "Warfarin: tăng nguy cơ chảy máu (ít hơn cefotetan)"
        ],
        "monitoring": "LFT, công thức máu",
        "aware_classification": "WATCH",
        "pregnancy": "B"
    },
}

