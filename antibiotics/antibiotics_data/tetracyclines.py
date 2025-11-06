"""
Tetracyclines and Glycylcyclines
"""

TETRACYCLINES = {
    "Tigecycline": {
        "group": "Glycylcycline",
        "vietnamese_name": "Tigecycline, Tygacil, Tigecycline",
        "administration": ["IV"],
        "indications": [
            "Nhiễm khuẩn đa kháng (MDR)",
            "Nhiễm khuẩn do Acinetobacter baumannii",
            "Nhiễm khuẩn ổ bụng phức tạp",
            "Nhiễm khuẩn da và mô mềm phức tạp",
            "Viêm phổi bệnh viện do MDR"
        ],
        "contraindications": [
            "Dị ứng tigecycline",
            "Trẻ em <8 tuổi (ảnh hưởng răng)",
            "Tam cá nguyệt 2-3 thai kỳ (ảnh hưởng răng thai nhi)"
        ],
        "dosage": {
            "adult_loading": "100mg IV x 1 liều đầu",
            "adult_maintenance": "50mg IV mỗi 12 giờ",
            "adult_severe": "100mg IV mỗi 12 giờ (off-label, cân nhắc)",
            "pediatric": "2mg/kg IV loading, sau đó 1mg/kg mỗi 12 giờ (max 50mg/liều)",
            "notes": "Phổ rộng chống MDR. CẢNH BÁO: Tăng tỷ lệ tử vong trong nghiên cứu (FDA black box)"
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "Không đổi (thải qua gan)",
            "15_30": "Không đổi",
            "under_15": "Không đổi"
        },
        "side_effects": [
            "Buồn nôn, nôn (20-30%)",
            "Tiêu chảy",
            "Tăng nguy cơ tử vong (đặc biệt nhiễm khuẩn huyết, viêm phổi)",
            "Tăng bilirubin, transaminase",
            "Phát ban"
        ],
        "interactions": [
            "Warfarin: tăng nguy cơ chảy máu",
            "Oral contraceptives: giảm hiệu quả"
        ],
        "aware_classification": "RESERVE",
        "pregnancy": "D - Gây đổi màu răng"
    },

    "Doxycycline": {
        "group": "Tetracycline",
        "vietnamese_name": "Doxycycline, Vibramycin, Doxycycline",
        "administration": ["IV", "PO"],
        "indications": [
            "Nhiễm khuẩn do Rickettsia, Mycoplasma, Chlamydia",
            "Sốt rét (kết hợp)",
            "Nhiễm khuẩn da và mô mềm",
            "Nhiễm khuẩn đường hô hấp",
            "Nhiễm khuẩn đường tiết niệu do Chlamydia"
        ],
        "contraindications": [
            "Dị ứng tetracycline",
            "Trẻ em <8 tuổi (ảnh hưởng răng)",
            "Tam cá nguyệt 2-3 thai kỳ (ảnh hưởng răng thai nhi)"
        ],
        "dosage": {
            "adult_iv": "100mg IV mỗi 12 giờ hoặc 200mg IV x 1 lần/ngày",
            "adult_po": "100mg PO x 2 lần/ngày",
            "adult_po_loading": "200mg PO x 1 liều đầu, sau đó 100mg x 2 lần/ngày",
            "pediatric_iv": "4.4mg/kg ngày 1, sau đó 2.2mg/kg mỗi 12 giờ (max 100mg/liều)",
            "notes": "Tránh dùng với sữa, antacids (giảm hấp thu). Tăng nhạy cảm ánh sáng"
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "Không đổi (thải qua gan)",
            "15_30": "Không đổi",
            "under_15": "Không đổi"
        },
        "side_effects": [
            "Buồn nôn, nôn",
            "Nhạy cảm ánh sáng (bắt buộc dùng kem chống nắng)",
            "Rối loạn thực quản (nuốt với nước nhiều)",
            "Phát ban",
            "Đổi màu răng (trẻ em, thai nhi)"
        ],
        "interactions": [
            "Antacids, Sắt, Canxi: giảm hấp thu (cách 2 giờ)",
            "Warfarin: tăng nguy cơ chảy máu",
            "Isotretinoin: tăng áp lực nội sọ",
            "Oral contraceptives: giảm hiệu quả"
        ],
        "aware_classification": "ACCESS",
        "pregnancy": "D - Đổi màu răng thai nhi"
    },

    "Minocycline": {
        "group": "Tetracycline",
        "vietnamese_name": "Minocycline, Minocycline, Minocin",
        "administration": ["PO", "IV"],
        "indications": [
            "Nhiễm khuẩn do Chlamydia, Mycoplasma",
            "Viêm phổi không điển hình",
            "Mụn trứng cá (liều thấp)",
            "Nhiễm khuẩn da và mô mềm",
            "Bệnh lây truyền qua đường tình dục"
        ],
        "contraindications": [
            "Trẻ em < 8 tuổi (ảnh hưởng răng và xương)",
            "Có thai (ảnh hưởng xương thai nhi)",
            "Suy gan nặng"
        ],
        "dosage": {
            "adult_po": "100mg PO x 2 lần/ngày",
            "adult_iv": "200mg IV x 1 lần/ngày hoặc 100mg IV x 2 lần/ngày",
            "adult_acne": "50-100mg PO x 1-2 lần/ngày",
            "pediatric_po": "4mg/kg/ngày chia 2 lần (≥8 tuổi)",
            "notes": "Tetracycline, tốt hơn Doxycycline về CNS penetration"
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "Không đổi (thải qua gan)",
            "15_30": "Không đổi (thải qua gan)",
            "under_15": "Không đổi (thải qua gan)"
        },
        "side_effects": [
            "Rối loạn tiền đình (chóng mặt, mất thăng bằng)",
            "Tăng áp lực nội sọ (pseudotumor cerebri)",
            "Phản ứng quá mẫn (DRESS, SJS)",
            "Ảnh hưởng răng và xương (trẻ em, thai nhi)"
        ],
        "interactions": [
            "Warfarin: tăng nguy cơ chảy máu",
            "Oral contraceptives: giảm hiệu quả",
            "Antacids, Ca2+, Fe2+: giảm hấp thu"
        ],
        "aware_classification": "ACCESS",
        "pregnancy": "D"
    },

}

__all__ = ['TETRACYCLINES']
