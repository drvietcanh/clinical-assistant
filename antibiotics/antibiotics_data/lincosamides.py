"""
Lincosamides - Clindamycin
"""

LINCOSAMIDES = {
    "Clindamycin": {
        "group": "Lincosamide",
        "vietnamese_name": "Clindamycin, Cleocin, Clindamycin",
        "administration": ["IV", "IM", "PO"],
        "indications": [
            "Nhiễm khuẩn do vi khuẩn kỵ khí",
            "Nhiễm khuẩn da và mô mềm",
            "Viêm phổi do vi khuẩn kỵ khí",
            "Viêm nội tâm mạc do vi khuẩn kỵ khí",
            "Nhiễm khuẩn răng miệng",
            "Viêm mô tế bào"
        ],
        "contraindications": [
            "Dị ứng clindamycin",
            "Viêm đại tràng giả mạc trước đây"
        ],
        "dosage": {
            "adult_iv": "600-900mg IV mỗi 8 giờ",
            "adult_iv_severe": "900mg IV mỗi 8 giờ hoặc 600mg IV mỗi 6 giờ",
            "adult_im": "600mg IM mỗi 12 giờ",
            "adult_po": "150-450mg PO x 3-4 lần/ngày",
            "pediatric_iv": "20-40mg/kg/ngày chia 3-4 lần (max 4.5g/ngày)",
            "pediatric_po": "10-25mg/kg/ngày chia 3-4 lần",
            "notes": "Tốt chống vi khuẩn kỵ khí, đặc biệt Bacteroides. Nguy cơ viêm đại tràng giả mạc (C. difficile)"
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "Không đổi",
            "15_30": "Không đổi",
            "under_15": "Không đổi (thải qua gan)"
        },
        "side_effects": [
            "Viêm đại tràng giả mạc (C. difficile) - nguy hiểm",
            "Tiêu chảy",
            "Phát ban",
            "Viêm tĩnh mạch (IV)",
            "Đau tại chỗ tiêm (IM)"
        ],
        "interactions": [
            "Neuromuscular blocking agents: tăng tê liệt",
            "Erythromycin: đối kháng (không dùng chung)"
        ],
        "aware_classification": "ACCESS",
        "pregnancy": "B"
    },

}

__all__ = ['LINCOSAMIDES']
