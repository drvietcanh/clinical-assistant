"""
Macrolides
"""

MACROLIDES = {
    "Azithromycin": {
        "group": "Macrolide",
        "vietnamese_name": "Azithromycin, Zithromax, Azitro, Azicine, Azyth, Azimycin, Azithrocin, Azomax",
        "administration": ["IV", "PO"],
        "indications": [
            "Viêm phổi cộng đồng",
            "Nhiễm khuẩn đường hô hấp trên",
            "Nhiễm Chlamydia, Mycoplasma",
            "Nhiễm khuẩn đường tiết niệu do Chlamydia"
        ],
        "contraindications": [
            "Dị ứng macrolide",
            "QT kéo dài",
            "Rối loạn nhịp tim"
        ],
        "dosage": {
            "adult_iv": "500mg IV x 1 lần/ngày",
            "adult_po_standard": "500mg PO ngày 1, sau đó 250mg/ngày x 4 ngày",
            "adult_po_single": "1g PO x 1 liều (Chlamydia)",
            "adult_po_extended": "500mg PO x 1 lần/ngày (nhiễm khuẩn kéo dài)",
            "pediatric_iv": "10mg/kg IV x 1 lần/ngày",
            "pediatric_po": "10mg/kg PO ngày 1 (max 500mg), sau đó 5mg/kg/ngày x 4 ngày",
            "notes": "Thời gian bán thải dài (68h), dùng 1 lần/ngày. Không cần điều chỉnh thận nhẹ"
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "Không đổi (thải qua gan)",
            "15_30": "Không đổi",
            "under_15": "Không đổi (thải qua gan)"
        },
        "side_effects": [
            "Buồn nôn, tiêu chảy",
            "QT kéo dài",
            "Rối loạn nhịp tim",
            "Viêm gan (hiếm)",
            "Nhạy cảm ánh sáng"
        ],
        "interactions": [
            "Warfarin: tăng nguy cơ chảy máu",
            "Digoxin: tăng nồng độ digoxin",
            "Cyclosporine: tăng nồng độ cyclosporine",
            "Antacids: giảm hấp thu PO (cách 2 giờ)"
        ],
        "aware_classification": "ACCESS",
        "pregnancy": "B"
    },

    "Erythromycin": {
        "group": "Macrolide",
        "vietnamese_name": "Erythromycin, Erythromycin, Erythrocin",
        "administration": ["IV", "PO"],
        "indications": [
            "Nhiễm khuẩn do Chlamydia, Mycoplasma, Legionella",
            "Nhiễm khuẩn đường hô hấp",
            "Viêm phổi cộng đồng",
            "Nhiễm khuẩn da và mô mềm",
            "Viêm nội tâm mạc do Streptococcus"
        ],
        "contraindications": [
            "Dị ứng erythromycin",
            "Rối loạn nhịp tim (QT kéo dài)",
            "Suy gan nặng"
        ],
        "dosage": {
            "adult_iv": "1-4g IV chia 4 lần/ngày",
            "adult_iv_standard": "500mg-1g IV mỗi 6 giờ",
            "adult_po": "250-500mg PO x 2-4 lần/ngày",
            "pediatric_iv": "20-50mg/kg/ngày chia 4 lần",
            "pediatric_po": "30-50mg/kg/ngày chia 3-4 lần",
            "notes": "Macrolide đầu tiên. Nguy cơ viêm tĩnh mạch cao (IV), QT kéo dài, tương tác nhiều"
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "Không đổi",
            "15_30": "Không đổi",
            "under_15": "Không đổi (thải qua gan)"
        },
        "side_effects": [
            "Viêm tĩnh mạch (IV - rất thường gặp)",
            "QT kéo dài, rối loạn nhịp tim",
            "Buồn nôn, nôn",
            "Tiêu chảy",
            "Rối loạn thính giác (liều cao)"
        ],
        "interactions": [
            "Warfarin: tăng nguy cơ chảy máu",
            "Cyclosporine: tăng nồng độ cyclosporine",
            "Digoxin: tăng nồng độ digoxin",
            "Theophylline: tăng nồng độ theophylline",
            "Statins: tăng nguy cơ tiêu cơ vân"
        ],
        "aware_classification": "ACCESS",
        "pregnancy": "B"
    },

    "Clarithromycin": {
        "group": "Macrolide",
        "vietnamese_name": "Clarithromycin, Klacid, Clamycin, Claridar, Clari, Klari, Clarit, Clarixin",
        "administration": ["PO", "IV"],
        "indications": [
            "Viêm phổi cộng đồng",
            "Viêm xoang cấp",
            "Nhiễm H. pylori (kết hợp)",
            "Nhiễm khuẩn da và mô mềm",
            "Nhiễm Chlamydia, Mycoplasma",
            "Viêm phổi do Legionella"
        ],
        "contraindications": [
            "Dị ứng macrolide",
            "Rối loạn nhịp tim nặng (QT kéo dài)",
            "Dùng đồng thời với terfenadine, astemizole, cisapride"
        ],
        "dosage": {
            "adult_po_standard": "250-500mg PO x 2 lần/ngày",
            "adult_po_severe": "500mg PO x 2 lần/ngày",
            "adult_po_hpylori": "500mg PO x 2 lần/ngày (kết hợp amoxicillin, PPI)",
            "adult_iv": "500mg IV x 2 lần/ngày",
            "pediatric_po": "15mg/kg/ngày chia 2 lần (max 1g/ngày)",
            "notes": "Tương tác nhiều thuốc. Uống với thức ăn hoặc không. Có dạng giải phóng kéo dài (XL)"
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "Giảm liều 25-50% (CrCl <30)",
            "15_30": "250mg PO x 2 lần/ngày hoặc 500mg x 1 lần/ngày",
            "under_15": "250mg PO x 1 lần/ngày"
        },
        "side_effects": [
            "Rối loạn tiêu hóa (tiêu chảy, buồn nôn, vị kim loại)",
            "Rối loạn nhịp tim (QT kéo dài)",
            "Nhức đầu",
            "Rối loạn chức năng gan",
            "Giảm bạch cầu (hiếm)"
        ],
        "interactions": [
            "Warfarin: tăng nguy cơ chảy máu (theo dõi INR)",
            "Statins: tăng nguy cơ tiêu cơ vân",
            "Digoxin: tăng nồng độ",
            "Cyclosporine, tacrolimus: tăng nồng độ",
            "Rifampin: giảm nồng độ clarithromycin"
        ],
        "monitoring": "ECG (QT interval) nếu có bệnh tim, LFT, công thức máu",
        "aware_classification": "WATCH",
        "pregnancy": "C"
    },

}

__all__ = ['MACROLIDES']
