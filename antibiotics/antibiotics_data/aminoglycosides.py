"""
Aminoglycosides
"""

AMINOGLYCOSIDES = {
    "Gentamicin": {
        "group": "Aminoglycoside",
        "vietnamese_name": "Gentamicin, Garamycin, Genticyn, Gentas, Gentamycin, Gentin, Genoptic, Genta",
        "administration": ["IV", "IM"],
        "indications": [
            "Nhiễm khuẩn huyết nghi ngờ Gram âm",
            "Nhiễm khuẩn do Pseudomonas",
            "Viêm nội tâm mạc",
            "Dự phòng phẫu thuật (kết hợp)"
        ],
        "contraindications": [
            "Dị ứng aminoglycoside",
            "Suy thận nặng (dùng với thận trọng)",
            "Rối loạn thần kinh tai"
        ],
        "dosage": {
            "adult_iv_once_daily": "5-7mg/kg IV x 1 lần/ngày (dựa trên cân nặng thực tế)",
            "adult_iv_tid": "1-2mg/kg IV mỗi 8 giờ (liều cũ, ít dùng)",
            "adult_im": "1-2mg/kg IM mỗi 8 giờ",
            "adult_obese_abw": "5-7mg/kg IV x 1 lần/ngày (dựa trên ABW)",
            "pediatric": "7.5mg/kg IV x 1 lần/ngày hoặc 2.5mg/kg mỗi 8 giờ",
            "notes": "Ưu tiên dùng 1 lần/ngày (ODD) - hiệu quả cao hơn, độc tính thấp hơn. Phải monitor nồng độ!"
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "Giảm liều 25-50% hoặc tăng khoảng cách",
            "15_30": "Giảm liều 50-75%",
            "under_15": "Giảm liều mạnh hoặc tránh nếu có thể",
            "hemodialysis": "1-2mg/kg sau mỗi lần lọc máu"
        },
        "side_effects": [
            "Độc thận (10-25%) - tăng creatinine, AKI",
            "Độc tai (2-25%) - điếc, ù tai, mất thăng bằng",
            "Tê liệt thần kinh cơ (hiếm)",
            "Tăng creatinin máu"
        ],
        "interactions": [
            "Vancomycin: tăng độc thận (cẩn trọng khi dùng chung)",
            "Furosemide: tăng độc tai",
            "Ciclosporin: tăng độc thận",
            "Beta-lactams: không pha cùng (mất hoạt tính)"
        ],
        "monitoring": "Bắt buộc: Peak và Trough levels, Creatinine hàng ngày, thính giác",
        "aware_classification": "ACCESS",
        "pregnancy": "D - Độc thai nhi"
    },

    "Amikacin": {
        "group": "Aminoglycoside",
        "vietnamese_name": "Amikacin, Amikin, Amikacine, Biklin, Likacin, Amikabiotic, Amikacyn, Amik",
        "administration": ["IV", "IM"],
        "indications": [
            "Nhiễm khuẩn đa kháng (MDR)",
            "Nhiễm khuẩn do vi khuẩn kháng gentamicin/tobramycin",
            "Nhiễm khuẩn huyết nghi ngờ Gram âm kháng",
            "Viêm phổi bệnh viện nặng"
        ],
        "contraindications": [
            "Dị ứng aminoglycoside",
            "Suy thận nặng",
            "Rối loạn thần kinh tai"
        ],
        "dosage": {
            "adult_iv_once_daily": "15-20mg/kg IV x 1 lần/ngày",
            "adult_iv_tid": "7.5mg/kg IV mỗi 8 giờ",
            "adult_im": "7.5mg/kg IM mỗi 8 giờ",
            "adult_obese_abw": "15-20mg/kg IV x 1 lần/ngày (dựa trên ABW)",
            "pediatric": "15-20mg/kg IV x 1 lần/ngày",
            "notes": "Liều cao hơn gentamicin (15-20mg/kg vs 5-7mg/kg). Ưu tiên ODD. Monitor nồng độ!"
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "Giảm liều 25-50%",
            "15_30": "Giảm liều 50-75%",
            "under_15": "Tránh hoặc giảm liều mạnh",
            "hemodialysis": "7.5mg/kg sau mỗi lần lọc máu"
        },
        "side_effects": [
            "Độc thận (tương tự gentamicin)",
            "Độc tai",
            "Giống gentamicin nhưng có thể ít hơn ở liều tương đương"
        ],
        "interactions": [
            "Giống gentamicin",
            "Vancomycin: tăng độc thận",
            "Beta-lactams: không pha cùng"
        ],
        "monitoring": "Bắt buộc: Peak/Trough, Creatinine, thính giác",
        "aware_classification": "WATCH",
        "pregnancy": "D"
    },

    "Tobramycin": {
        "group": "Aminoglycoside",
        "vietnamese_name": "Tobramycin, Nebcin, Tobramycin",
        "administration": ["IV", "IM", "Inhalation"],
        "indications": [
            "Nhiễm khuẩn do Pseudomonas aeruginosa",
            "Nhiễm khuẩn đường tiết niệu",
            "Nhiễm khuẩn da và mô mềm",
            "Viêm phổi do P. aeruginosa",
            "Nhiễm khuẩn huyết do Gram âm"
        ],
        "contraindications": [
            "Dị ứng aminoglycoside",
            "Nhược cơ nặng",
            "Suy thận nặng (thận trọng, monitor)"
        ],
        "dosage": {
            "adult_iv_standard": "5-7mg/kg IV mỗi 24 giờ (extended-interval)",
            "adult_iv_traditional": "1-1.7mg/kg IV mỗi 8 giờ",
            "adult_inhalation": "300mg x 2 lần/ngày (cho P. aeruginosa trong CF)",
            "pediatric_iv": "5-7mg/kg IV mỗi 24 giờ",
            "notes": "Tốt hơn Gentamicin chống P. aeruginosa. Extended-interval dosing khuyến cáo"
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "Rút ngắn interval hoặc giảm liều",
            "15_30": "Rút ngắn interval hoặc giảm liều 50%",
            "under_15": "Dùng liều thấp với interval dài hoặc tránh"
        },
        "side_effects": [
            "Độc tai (irreversible)",
            "Độc thận (reversible)",
            "Chóng mặt, mất thăng bằng",
            "Tê bì (neuromuscular blockade - liều cao)"
        ],
        "interactions": [
            "Vancomycin: tăng độc thận",
            "Furosemide: tăng độc tai",
            "Neuromuscular blocking agents: tăng tê liệt"
        ],
        "monitoring": "Bắt buộc: Peak/Trough, Creatinine, thính giác",
        "aware_classification": "WATCH",
        "pregnancy": "D"
    },

}

__all__ = ['AMINOGLYCOSIDES']
