"""
Glycopeptides - Vancomycin, Teicoplanin
"""

GLYCOPEPTIDES = {
    "Vancomycin": {
        "group": "Glycopeptide",
        "vietnamese_name": "Vancomycin, Vancocin, Vancomax, Vancoled, Vancoplus, Vanco, Vancocid",
        "administration": ["IV", "PO"],
        "indications": [
            "Nhiễm khuẩn do MRSA",
            "Viêm màng não do S. pneumoniae kháng penicillin",
            "Nhiễm khuẩn do Enterococcus kháng ampicillin",
            "Viêm đại tràng giả mạc (PO)",
            "Dự phòng phẫu thuật"
        ],
        "contraindications": [
            "Dị ứng vancomycin",
            "Suy thận nặng (phải điều chỉnh liều)"
        ],
        "dosage": {
            "adult_iv_standard": "15-20mg/kg IV mỗi 8-12 giờ (dựa trên CrCl)",
            "adult_iv_load": "25-30mg/kg IV x 1 liều đầu (loading dose) - IDSA 2024",
            "adult_iv_obese": "Dựa trên ABW, thường 20-25mg/kg (max 2g liều thường)",
            "adult_iv_extended": "15-20mg/kg IV mỗi 12 giờ (extended infusion 3-4h) - tối ưu PK/PD",
            "adult_iv_severe": "20mg/kg IV mỗi 8 giờ (sepsis, endocarditis)",
            "adult_po_cdiff": "125-500mg PO x 4 lần/ngày",
            "pediatric_iv": "40-60mg/kg/ngày chia 4 lần hoặc 15mg/kg mỗi 6 giờ",
            "pediatric_load": "20-25mg/kg IV x 1 liều đầu",
            "notes": "IDSA 2024: Loading dose 25-30mg/kg cho nhiễm khuẩn nặng. Phải truyền tĩnh mạch chậm (≥60 phút) để tránh Red Man Syndrome. Trough target: 10-20 mg/L (15-20 cho nhiễm khuẩn nặng, viêm màng não)"
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "Giảm liều hoặc tăng khoảng cách 12-24h",
            "15_30": "Giảm liều 50% hoặc mỗi 24-48h",
            "under_15": "Liều thấp mỗi 48-72h hoặc lọc máu",
            "hemodialysis": "15-20mg/kg sau mỗi lần lọc máu"
        },
        "side_effects": [
            "Red Man Syndrome (phản ứng histamine - truyền quá nhanh)",
            "Độc thận (15-30%) - đặc biệt với aminoglycoside",
            "Độc tai",
            "Thrombophlebitis",
            "Giảm bạch cầu (hiếm)"
        ],
        "interactions": [
            "Aminoglycosides: tăng độc thận",
            "Piperacillin-tazobactam: giảm nồng độ vancomycin (tăng khoảng cách)",
            "Furosemide: tăng độc tai",
            "Anesthetic agents: tăng nguy cơ hạ huyết áp"
        ],
        "monitoring": "Bắt buộc: Trough level (mục tiêu 10-20 mg/L, 15-20 cho nhiễm khuẩn nặng) - IDSA 2024. Đo sau liều thứ 4. Creatinine hàng ngày, thính giác (nếu dùng dài ngày)",
        "aware_classification": "WATCH",
        "pregnancy": "C",
        "guidelines": "IDSA 2024: Loading dose 25-30mg/kg. Extended infusion 3-4h tối ưu PK/PD. Trough 15-20 mg/L cho nhiễm khuẩn nặng, viêm màng não"
    },

    "Teicoplanin": {
        "group": "Glycopeptide",
        "vietnamese_name": "Teicoplanin, Targocid, Teicoplanin",
        "administration": ["IV", "IM"],
        "indications": [
            "Nhiễm khuẩn do MRSA (da, mô mềm)",
            "Viêm nội tâm mạc do MRSA",
            "Nhiễm khuẩn do Enterococcus",
            "Nhiễm khuẩn xương khớp do MRSA",
            "Nhiễm khuẩn bệnh viện do MRSA"
        ],
        "contraindications": [
            "Dị ứng teicoplanin",
            "Suy thận nặng (phải điều chỉnh liều)"
        ],
        "dosage": {
            "adult_iv_load": "6mg/kg IV x 2-3 lần (loading, mỗi 12 giờ)",
            "adult_iv_maintenance": "6mg/kg IV x 1 lần/ngày",
            "adult_iv_severe": "12mg/kg IV x 1 lần/ngày",
            "adult_im": "6mg/kg IM x 1 lần/ngày",
            "pediatric_iv": "10mg/kg IV x 2 lần đầu, sau đó 6mg/kg x 1 lần/ngày",
            "notes": "Glycopeptide, liên kết protein 90%. Ít độc thận hơn Vancomycin. Có thể tiêm IM"
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "Giảm liều 50% hoặc mỗi 48h",
            "15_30": "Giảm liều 75% hoặc mỗi 72h",
            "under_15": "Liều thấp mỗi 72-96h hoặc lọc máu"
        },
        "side_effects": [
            "Độc thận (ít hơn Vancomycin)",
            "Độc tai (ít hơn Vancomycin)",
            "Thrombocytopenia (hiếm)",
            "Phản ứng tại chỗ tiêm (IM)"
        ],
        "interactions": [
            "Aminoglycosides: tăng độc thận",
            "Furosemide: tăng độc tai"
        ],
        "monitoring": "Monitor nồng độ trough (15-30 mg/L), creatinine",
        "aware_classification": "RESERVE",
        "pregnancy": "C"
    },

    "Telavancin": {
        "group": "Glycopeptide",
        "vietnamese_name": "Telavancin, Vibativ",
        "administration": ["IV"],
        "indications": [
            "Nhiễm khuẩn da và mô mềm phức tạp do vi khuẩn gram dương",
            "MRSA (Methicillin-Resistant S. aureus)",
            "Viêm phổi bệnh viện do MRSA",
            "VRE (Vancomycin-Resistant Enterococcus) - một số chủng",
            "Nhiễm khuẩn do S. aureus kháng vancomycin"
        ],
        "contraindications": [
            "Dị ứng telavancin/glycopeptide",
            "Phụ nữ có thai (nguy cơ dị tật)",
            "Suy thận nặng (CrCl < 30 ml/min)",
            "Lactation (nguy cơ cho trẻ sơ sinh)"
        ],
        "dosage": {
            "adult_iv": "10mg/kg IV mỗi 24 giờ (liều đầu tiên: 10mg/kg, liều duy trì: 7.5mg/kg nếu CrCl 30-50)",
            "adult_iv_severe": "10mg/kg IV mỗi 24 giờ",
            "notes": "Dùng trong 7-14 ngày. Pha trong D5W. Truyền trong 60 phút"
        },
        "renal_adjustment": {
            "normal": "10mg/kg mỗi 24 giờ",
            "30_60": "7.5mg/kg mỗi 24 giờ (giảm liều)",
            "15_30": "10mg/kg mỗi 48 giờ",
            "under_15": "Chống chỉ định (nguy cơ độc tính thận cao)"
        },
        "side_effects": [
            "Độc tính thận (tăng creatinine, suy thận cấp)",
            "Foam trong nước tiểu (do chất tẩy, không nguy hiểm)",
            "Rối loạn vị giác (vị kim loại)",
            "Buồn nôn, nôn",
            "Đau đầu",
            "Phản ứng tại chỗ tiêm (viêm tĩnh mạch)"
        ],
        "interactions": [
            "Thuốc độc thận: tăng nguy cơ suy thận (aminoglycoside, NSAID)",
            "Thuốc kéo dài QT: tăng nguy cơ rối loạn nhịp (cần theo dõi ECG)",
            "Warfarin: tăng nguy cơ chảy máu"
        ],
        "monitoring": "Creatinine hàng ngày, GFR, ECG (QT interval), công thức máu",
        "aware_classification": "RESERVE",
        "pregnancy": "C - Chống chỉ định trong thai kỳ (gây dị tật trong thí nghiệm động vật)",
        "notes": "Dùng khi vancomycin/daptomycin thất bại hoặc không dung nạp. Độc tính thận cao, cần theo dõi chặt chẽ. Chống chỉ định thai kỳ"
    },

}

__all__ = ['GLYCOPEPTIDES']
