"""
Fluoroquinolones
"""

FLUOROQUINOLONES = {
    "Ciprofloxacin": {
        "group": "Fluoroquinolone",
        "vietnamese_name": "Ciprofloxacin, Cipro, Ciprobay, Ciproflox, Ciproxin, Ciprox, Cifran, Flox",
        "administration": ["IV", "PO"],
        "indications": [
            "Nhiễm khuẩn đường tiết niệu",
            "Nhiễm khuẩn đường tiêu hóa",
            "Nhiễm khuẩn do Pseudomonas",
            "Viêm phổi bệnh viện",
            "Nhiễm khuẩn da và mô mềm"
        ],
        "contraindications": [
            "Dị ứng quinolone",
            "Trẻ em <18 tuổi (trừ trường hợp đặc biệt)",
            "Có thai, cho con bú"
        ],
        "dosage": {
            "adult_iv_standard": "400mg IV mỗi 12 giờ",
            "adult_iv_severe": "400mg IV mỗi 8 giờ",
            "adult_po_standard": "500-750mg PO x 2 lần/ngày",
            "adult_po_uti": "250-500mg PO x 2 lần/ngày",
            "pediatric_iv": "10-15mg/kg IV mỗi 12 giờ (chỉ khi thực sự cần)",
            "notes": "Tránh dùng quinolone nếu có lựa chọn khác (nguy cơ tác dụng phụ)"
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "Giảm liều 50%",
            "15_30": "200-400mg mỗi 12 giờ",
            "under_15": "200mg mỗi 12 giờ hoặc tránh"
        },
        "side_effects": [
            "Rối loạn thần kinh trung ương (lú lẫn, co giật, mất ngủ)",
            "Đứt gân (Achilles)",
            "Rối loạn nhịp tim (QT kéo dài)",
            "Tăng đường huyết/hạ đường huyết",
            "Phát ban, nhạy cảm ánh sáng"
        ],
        "interactions": [
            "Antacids, Sucralfate: giảm hấp thu (cách 2-4 giờ)",
            "Warfarin: tăng nguy cơ chảy máu",
            "Theophylline: tăng nồng độ theophylline",
            "Probenecid: tăng nồng độ ciprofloxacin"
        ],
        "aware_classification": "WATCH",
        "pregnancy": "C"
    },

    "Levofloxacin": {
        "group": "Fluoroquinolone",
        "vietnamese_name": "Levofloxacin, Levaquin, Tavanic, Levotab, Levoxin, Levo, Levox, Loxof",
        "administration": ["IV", "PO"],
        "indications": [
            "Viêm phổi cộng đồng",
            "Viêm phổi bệnh viện",
            "Nhiễm khuẩn đường tiết niệu phức tạp",
            "Viêm xoang",
            "Nhiễm khuẩn da và mô mềm"
        ],
        "contraindications": [
            "Dị ứng quinolone",
            "Trẻ em <18 tuổi",
            "QT kéo dài",
            "Có thai, cho con bú"
        ],
        "dosage": {
            "adult_iv_standard": "500-750mg IV x 1 lần/ngày",
            "adult_po_standard": "500-750mg PO x 1 lần/ngày",
            "adult_severe": "750mg IV/PO x 1 lần/ngày",
            "adult_uti": "250-500mg PO x 1 lần/ngày",
            "notes": "Dùng 1 lần/ngày, tiện lợi hơn ciprofloxacin"
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "250-500mg mỗi 24 giờ",
            "15_30": "250mg mỗi 24 giờ",
            "under_15": "250mg mỗi 48 giờ hoặc tránh"
        },
        "side_effects": [
            "Giống ciprofloxacin",
            "Đứt gân",
            "Rối loạn thần kinh",
            "QT kéo dài"
        ],
        "interactions": [
            "Giống ciprofloxacin",
            "Antacids: giảm hấp thu",
            "Warfarin: tăng nguy cơ chảy máu"
        ],
        "aware_classification": "WATCH",
        "pregnancy": "C"
    },

    "Moxifloxacin": {
        "group": "Fluoroquinolone",
        "vietnamese_name": "Moxifloxacin, Avelox, Moxifloxacin",
        "administration": ["PO", "IV"],
        "indications": [
            "Viêm phổi cộng đồng",
            "Viêm phổi bệnh viện",
            "Nhiễm khuẩn da và mô mềm",
            "Viêm xoang",
            "Nhiễm khuẩn ổ bụng phức tạp"
        ],
        "contraindications": [
            "Dị ứng quinolone",
            "QT kéo dài, rối loạn nhịp tim",
            "Trẻ em < 18 tuổi (ảnh hưởng sụn)",
            "Có thai, cho con bú"
        ],
        "dosage": {
            "adult_iv": "400mg IV x 1 lần/ngày",
            "adult_po": "400mg PO x 1 lần/ngày",
            "notes": "Quinolone thế hệ 4. Phổ rộng, bao gồm vi khuẩn kỵ khí. QT kéo dài nguy hiểm"
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "Không đổi (thải qua gan)",
            "15_30": "Không đổi (thải qua gan)",
            "under_15": "Không đổi (thải qua gan)"
        },
        "side_effects": [
            "QT kéo dài, rối loạn nhịp tim (torsades de pointes)",
            "Tendinitis, đứt gân",
            "Rối loạn thần kinh trung ương",
            "Phản ứng quá mẫn",
            "Tăng nguy cơ viêm đại tràng giả mạc"
        ],
        "interactions": [
            "QT-prolonging drugs: tăng nguy cơ rối loạn nhịp",
            "Warfarin: tăng nguy cơ chảy máu",
            "Antacids, multivitamins: giảm hấp thu"
        ],
        "monitoring": "ECG trước và trong điều trị, QT interval",
        "aware_classification": "WATCH",
        "pregnancy": "C"
    },

}

__all__ = ['FLUOROQUINOLONES']
