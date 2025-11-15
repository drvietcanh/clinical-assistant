"""
Cephalosporins - Beta-lactamase Inhibitor Combinations
"""

BETA_LACTAMASE_INHIBITORS = {
    "Ceftazidime-Avibactam": {
        "group": "Beta-lactam - Cephalosporin + Beta-lactamase inhibitor",
        "vietnamese_name": "Ceftazidime-Avibactam, Avycaz, Zavicefta, Avibactam, Zavi, Ceftaz-Avi",
        "administration": ["IV"],
        "indications": [
            "Nhiễm khuẩn do vi khuẩn đa kháng (MDR/XDR)",
            "Nhiễm khuẩn do ESBL-producing Gram âm",
            "Nhiễm khuẩn do KPC-producing bacteria",
            "Viêm phổi bệnh viện do MDR",
            "Nhiễm khuẩn ổ bụng phức tạp do MDR"
        ],
        "contraindications": [
            "Dị ứng cephalosporin",
            "Dị ứng penicillin nặng"
        ],
        "dosage": {
            "adult_standard": "2.5g (2g ceftazidime + 0.5g avibactam) IV mỗi 8 giờ",
            "adult_severe": "2.5g IV mỗi 8 giờ (không tăng liều)",
            "adult_renal": "Giảm liều theo CrCl: 1.25g mỗi 12 giờ nếu CrCl 31-50, 1.25g mỗi 24 giờ nếu CrCl 16-30",
            "pediatric": "62.5mg/kg (theo ceftazidime) IV mỗi 8 giờ",
            "notes": "Thuốc mới, đắt tiền. Chỉ dùng khi không còn lựa chọn khác (MDR/XDR)"
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "1.25g mỗi 12 giờ",
            "15_30": "1.25g mỗi 24 giờ",
            "under_15": "1.25g mỗi 48 giờ hoặc lọc máu"
        },
        "side_effects": [
            "Tiêu chảy",
            "Phát ban",
            "Viêm tĩnh mạch",
            "Tăng transaminase"
        ],
        "interactions": [
            "Giống ceftazidime",
            "Probenecid: không nên dùng chung"
        ],
        "aware_classification": "RESERVE",
        "pregnancy": "B"
    },

    "Ceftolozane-Tazobactam": {
        "group": "Beta-lactam - Cephalosporin + Beta-lactamase inhibitor",
        "vietnamese_name": "Ceftolozane-Tazobactam, Zerbaxa, Ceftolozane-Tazobactam",
        "administration": ["IV"],
        "indications": [
            "Nhiễm khuẩn bệnh viện do P. aeruginosa MDR",
            "Viêm phổi bệnh viện",
            "Nhiễm khuẩn ổ bụng phức tạp",
            "Nhiễm khuẩn đường tiết niệu phức tạp"
        ],
        "contraindications": [
            "Dị ứng cephalosporin",
            "Dị ứng penicillin nặng (phản ứng chéo)"
        ],
        "dosage": {
            "adult_standard": "1.5g (1g ceftolozane + 0.5g tazobactam) IV mỗi 8 giờ",
            "adult_renal_30_50": "750mg IV mỗi 8 giờ",
            "adult_renal_15_30": "375mg IV mỗi 8 giờ",
            "adult_renal_under_15": "Loading 750mg, sau đó 375mg mỗi 8 giờ",
            "pediatric": "30mg/kg (theo ceftolozane) IV mỗi 8 giờ",
            "notes": "Thuốc mới, rất tốt chống P. aeruginosa. Đắt tiền. Cần điều chỉnh liều theo CrCl"
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "Giảm liều 50%",
            "15_30": "Giảm liều 75%",
            "under_15": "Giảm liều mạnh hoặc lọc máu"
        },
        "side_effects": [
            "Tiêu chảy",
            "Buồn nôn, nôn",
            "Phát ban",
            "Tăng transaminase"
        ],
        "interactions": [
            "Probenecid: tăng nồng độ"
        ],
        "aware_classification": "RESERVE",
        "pregnancy": "B"
    },

    "Cefoperazone-Sulbactam": {
        "group": "Beta-lactam - Cephalosporin + Beta-lactamase inhibitor",
        "vietnamese_name": "Cefoperazone-Sulbactam, Sulperazone, Cefazone-S, Sulzone, Cefpera-S, Sulcef, Cefoperazone-Sul",
        "administration": ["IV", "IM"],
        "indications": [
            "Nhiễm khuẩn bệnh viện (HAP, VAP)",
            "Nhiễm khuẩn ổ bụng",
            "Nhiễm khuẩn đường tiết niệu phức tạp",
            "Nhiễm khuẩn do vi khuẩn kháng beta-lactamase",
            "Nhiễm khuẩn do P. aeruginosa"
        ],
        "contraindications": [
            "Dị ứng cephalosporin/penicillin",
            "Sốc phản vệ beta-lactam"
        ],
        "dosage": {
            "adult_iv": "2g-1g (Cefoperazone-Sulbactam) IV mỗi 8-12 giờ",
            "adult_im": "1g-0.5g IM mỗi 12 giờ",
            "pediatric_iv": "40-80mg/kg/ngày (tính theo Cefoperazone) chia 2-3 lần",
            "severe_iv": "3g-1.5g IV mỗi 8 giờ",
            "notes": "Tỷ lệ 2:1 (Cefoperazone:Sulbactam), phổ rộng hơn Cefoperazone đơn"
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "Giảm liều 25-50%",
            "15_30": "Giảm liều 50%",
            "under_15": "1g-0.5g mỗi 12 giờ"
        },
        "side_effects": [
            "Rối loạn đông máu (giống Cefoperazone)",
            "Tiêu chảy",
            "Phản ứng dị ứng",
            "Viêm tĩnh mạch"
        ],
        "interactions": [
            "Rượu: phản ứng disulfiram",
            "Warfarin: tăng nguy cơ chảy máu",
            "Vitamin K: bổ sung nếu điều trị dài ngày"
        ],
        "monitoring": "PT/INR, đông máu",
        "aware_classification": "WATCH",
        "pregnancy": "B"
    },
}

