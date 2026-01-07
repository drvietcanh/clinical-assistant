"""Gastrointestinal Drugs
Active module - contains all gastrointestinal drug data"""

# Proton Pump Inhibitor (PPI)s

PROTON_PUMP_INHIBITOR_PPIS_DRUGS = {
    "Dexlansoprazole": {
        "group": "Gastrointestinal - Proton Pump Inhibitor (PPI) - Dual delayed release",
        "vietnamese_name": "Dexlansoprazole, Dexilant/Kapidex",
        "administration": ["PO"],
        "indications": [
            "GERD/ERD (trào ngược có viêm thực quản)",
            "Duy trì lành viêm thực quản và giảm ợ nóng",
            "Điều trị ợ nóng (heartburn) thường xuyên"
        ],
        "contraindications": ["Dị ứng dexlansoprazole/PPI", "Dùng cùng rilpivirine (giảm hấp thu)"],
        "dosage": {
            "adult_gerd": "30mg PO mỗi ngày",
            "adult_erd_healing": "60mg PO mỗi ngày x 8 tuần",
            "adult_erd_maintenance": "30mg PO mỗi ngày",
            "notes": "Có thể uống bất kỳ lúc nào trong ngày, không cần theo bữa ăn (công nghệ giải phóng kép). Nuốt nguyên viên; có thể rắc hạt trên táo nghiền và nuốt ngay."
        },
        "renal_adjustment": {"normal": "Không cần chỉnh liều", "30_60": "Không cần chỉnh", "under_30": "Không cần chỉnh"},
        "side_effects": ["Nhức đầu", "Tiêu chảy", "Đau bụng", "Buồn nôn", "Tăng nguy cơ nhiễm C. difficile", "Thiếu B12/Mg khi dùng lâu dài", "Gãy xương khi dùng dài hạn liều cao"],
        "interactions": ["Rilpivirine: chống chỉ định (giảm hấp thu)", "Clopidogrel: lý thuyết giảm hoạt hóa (ít hơn omeprazole)", "Ketoconazole/itraconazole: giảm hấp thu"],
        "pregnancy": "B",
        "mechanism_of_action": "PPI ức chế không hồi phục H+/K+-ATPase tại tế bào thành dạ dày. Công nghệ dual delayed release giải phóng 2 pha → kéo dài nồng độ ức chế acid suốt 24h, ít phụ thuộc thời điểm ăn.",
        "monitoring": ["Triệu chứng GERD/ợ nóng", "Magnesium, vitamin B12 nếu dùng >1 năm", "DEXA nếu nguy cơ loãng xương", "Dấu hiệu nhiễm C. difficile nếu tiêu chảy kéo dài"],
        "precautions": [
            "Dùng liều thấp nhất có hiệu quả, thời gian ngắn nhất",
            "Cân nhắc ngừng sau 4-8 tuần nếu kiểm soát tốt",
            "Nguy cơ gãy xương, thiếu Mg/B12 nếu dùng lâu",
            "Tránh dùng với rilpivirine; thận trọng với clopidogrel"
        ],
        "pharmacokinetics": {
            "half_life": "1-2 giờ (tác dụng kéo dài nhờ ức chế không hồi phục + phóng thích kép)",
            "onset": "1-2 giờ",
            "duration": "24 giờ",
            "protein_binding": "~96%",
            "clearance": "Gan (CYP2C19, CYP3A4); thận thải trừ chất chuyển hóa"
        },
        "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm, tránh ánh sáng",
        "black_box_warnings": "Dùng dài hạn có thể tăng nguy cơ gãy xương, thiếu Mg/B12; nguy cơ C. difficile.",
        "drug_interactions": {
            "major": [
                {"drug": "Rilpivirine", "mechanism": "Tăng pH dạ dày làm giảm hấp thu rilpivirine", "effect": "Giảm nồng độ rilpivirine, thất bại điều trị", "management": "CHỐNG CHỈ ĐỊNH phối hợp"}
            ],
            "moderate": [
                {"drug": "Clopidogrel", "mechanism": "Ức chế CYP2C19 (nhẹ hơn omeprazole)", "effect": "Có thể giảm hoạt hóa clopidogrel", "management": "Thận trọng; cân nhắc pantoprazole nếu cần tránh tương tác"},
                {"drug": "Ketoconazole/Itraconazole", "mechanism": "Tăng pH dạ dày giảm hấp thu", "effect": "Giảm hiệu quả azole", "management": "Cách thời gian hoặc dùng dạng lỏng/acid hoá"}
            ],
            "minor": []
        },
        "contraindications_detail": {
            "tuyệt_đối": ["Dị ứng dexlansoprazole/PPI", "Dùng cùng rilpivirine"],
            "tương_đối": ["Suy gan trung bình-nặng (giảm liều tối đa 30mg/ngày)", "Loãng xương/nguy cơ gãy xương", "Thiếu Mg/B12", "Tiền sử C. difficile"]
        },
        "pregnancy_lactation": {
            "fda_category": "B",
            "pregnancy_details": "Dữ liệu quan sát không cho thấy tăng dị tật; dùng nếu lợi ích vượt nguy cơ.",
            "lactation": {"safety": "Caution", "details": "Bài tiết ít vào sữa; thận trọng khi cho bú", "recommendation": "Theo dõi trẻ hoặc cân nhắc PPI khác an toàn hơn nếu cần"}
        },
        "hepatic_adjustment": {
            "mild": "Không cần chỉnh",
            "moderate": "Giảm liều tối đa 30mg/ngày",
            "severe": "Tránh hoặc dùng liều thấp nhất, thiếu dữ liệu",
            "notes": "Chuyển hóa qua CYP2C19/3A4; suy gan làm tăng AUC"
        },
        "overdose_management": {
            "symptoms": ["Buồn ngủ, nhức đầu, tiêu chảy"],
            "antidote": "Không có antidote đặc hiệu",
            "treatment": ["Hỗ trợ triệu chứng", "Theo dõi dấu hiệu sinh tồn"],
            "monitoring": "Sinh tồn, điện giải nếu triệu chứng kéo dài"
        },
        "reversal_agents": None,
        "administration_instructions": {
            "oral": {
                "with_food": "Có thể uống cùng hoặc không cùng thức ăn (công nghệ phóng thích kép)",
                "timing": "Uống 1 lần/ngày, không cần 30 phút trước ăn; nuốt nguyên viên hoặc rắc hạt lên táo nghiền và nuốt ngay"
            }
        },
        "references": {
            "primary_sources": [
                "FDA Label - Dexilant (dexlansoprazole)",
                "UpToDate - Proton pump inhibitors: Dexlansoprazole",
                "ACG GERD Guidelines 2022"
            ],
            "last_updated": "2025-02-18",
            "evidence_level": "High - FDA-approved"
        },
        "risk_flags": {
            "high_alert": False,
            "narrow_therapeutic_index": False,
            "bleeding_risk": False,
            "organ_toxicity": [],
            "qt_prolongation": False,
            "hepatotoxicity": False,
            "nephrotoxicity": False,
            "requires_monitoring": ["Magnesium (long-term use)", "Vitamin B12 (long-term use)", "Bone density"]
        },
        "guideline_tags": [
            "ACG 2017 GERD Guidelines",
            "FDA - Long-term PPI use monitoring",
            "UpToDate - Proton Pump Inhibitors"
        ]
    },

    # Esomeprazole, Lansoprazole, Omeprazole đã được chuyển sang proton_pump_inhibitors.py

    "Ilaprazole": {
        "group": "Gastrointestinal - Proton Pump Inhibitor (PPI)",
        "vietnamese_name": "Ilaprazole, Noltec",
        "administration": ["PO"],
        "indications": [
            "Loét dạ dày tá tràng",
            "GERD/viêm thực quản do trào ngược",
            "Hội chứng Zollinger-Ellison"
        ],
        "contraindications": ["Dị ứng ilaprazole/PPI"],
        "dosage": {
            "adult_ulcer": "10mg PO mỗi ngày",
            "adult_gerd": "10-20mg PO mỗi ngày",
            "zollinger_ellison": "20-40mg PO chia 1-2 lần/ngày, chỉnh theo đáp ứng",
            "notes": "Uống trước bữa ăn 30 phút. Nuốt nguyên viên."
        },
        "renal_adjustment": {"normal": "Không cần chỉnh liều", "30_60": "Không cần chỉnh", "under_30": "Không cần chỉnh"},
        "side_effects": ["Nhức đầu", "Buồn nôn", "Tiêu chảy", "Đau bụng", "Tăng men gan nhẹ", "Hiếm: giảm Mg/B12 khi dùng dài hạn"],
        "interactions": ["Warfarin: theo dõi INR", "Clopidogrel: ít ức chế CYP2C19 hơn omeprazole nhưng vẫn thận trọng", "Ketoconazole/itraconazole: giảm hấp thu"],
        "pregnancy": "C",
        "mechanism_of_action": "Ức chế không hồi phục H+/K+-ATPase tế bào thành dạ dày. Ilaprazole chuyển hóa chủ yếu qua CYP3A, ít phụ thuộc CYP2C19 → ít biến thiên giữa các kiểu gen, hiệu lực ổn định hơn ở người chuyển hóa kém.",
        "monitoring": ["Triệu chứng lâm sàng", "Men gan nếu dùng kéo dài", "Mg/B12 nếu dùng >1 năm", "DEXA nếu nguy cơ loãng xương"],
        "precautions": [
            "Uống trước ăn 30 phút",
            "Dùng liều thấp nhất hiệu quả, thời gian ngắn nhất",
            "Thận trọng ở suy gan nặng (giảm liều)",
            "Nguy cơ loãng xương, thiếu Mg/B12, C. difficile khi dùng dài hạn"
        ],
        "pharmacokinetics": {
            "half_life": "7-9 giờ (dài hơn omeprazole)",
            "onset": "1-3 giờ",
            "duration": "≥24 giờ (một lần/ngày)",
            "protein_binding": "~96%",
            "clearance": "Gan (CYP3A chủ yếu, ít phụ thuộc CYP2C19); thận thải trừ chất chuyển hóa"
        },
        "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm, tránh ánh sáng",
        "black_box_warnings": "Dùng dài hạn có thể tăng nguy cơ gãy xương, thiếu Mg/B12; nguy cơ C. difficile.",
        "drug_interactions": {
            "major": [],
            "moderate": [
                {"drug": "Clopidogrel", "mechanism": "Ức chế CYP2C19 nhẹ, chủ yếu CYP3A", "effect": "Tương tác ít hơn omeprazole nhưng vẫn thận trọng", "management": "Theo dõi, cân nhắc pantoprazole nếu cần tránh tương tác"},
                {"drug": "Warfarin", "mechanism": "Có thể tăng INR nhẹ", "effect": "Tăng nguy cơ chảy máu", "management": "Theo dõi INR khi bắt đầu/ngưng"}
            ],
            "minor": [
                {"drug": "Ketoconazole/Itraconazole", "mechanism": "Tăng pH dạ dày", "effect": "Giảm hấp thu azole", "management": "Cách thời gian, cân nhắc dạng lỏng/acid hóa"}
            ]
        },
        "contraindications_detail": {
            "tuyệt_đối": ["Dị ứng ilaprazole hoặc PPI khác"],
            "tương_đối": ["Suy gan trung bình-nặng", "Loãng xương/nguy cơ gãy xương", "Thiếu Mg/B12", "Tiền sử C. difficile"]
        },
        "pregnancy_lactation": {
            "fda_category": "C",
            "pregnancy_details": "Dữ liệu người còn hạn chế; dùng nếu lợi ích vượt nguy cơ.",
            "lactation": {"safety": "Caution", "details": "Chưa rõ bài tiết vào sữa; thận trọng", "recommendation": "Cân nhắc ngừng cho bú hoặc chọn PPI khác có dữ liệu hơn (lansoprazole/omeprazole)"}
        },
        "hepatic_adjustment": {
            "mild": "Không cần chỉnh",
            "moderate": "Giảm liều (ví dụ 5-10mg/ngày) và theo dõi men gan",
            "severe": "Tránh hoặc dùng liều thấp nhất, thiếu dữ liệu",
            "notes": "Suy gan làm tăng AUC; ilaprazole chuyển hóa qua CYP3A"
        },
        "overdose_management": {
            "symptoms": ["Buồn nôn, nhức đầu, chóng mặt"],
            "antidote": "Không có antidote đặc hiệu",
            "treatment": ["Hỗ trợ triệu chứng", "Theo dõi sinh tồn"],
            "monitoring": "Sinh tồn, điện giải nếu cần"
        },
        "reversal_agents": None,
        "administration_instructions": {
            "oral": {
                "with_food": "Uống trước ăn 30 phút",
                "timing": "Uống 1 lần/ngày, buổi sáng; nuốt nguyên viên"
            }
        },
        "references": {
            "primary_sources": [
                "Noltec (ilaprazole) product label",
                "UpToDate - Proton pump inhibitors: Ilaprazole",
                "Comparative studies CYP2C19 vs omeprazole/esomeprazole"
            ],
            "last_updated": "2025-02-18",
            "evidence_level": "Moderate – approved in several countries"
        },
        "risk_flags": {
            "high_alert": False,
            "narrow_therapeutic_index": False,
            "bleeding_risk": False,
            "organ_toxicity": [],
            "qt_prolongation": False,
            "hepatotoxicity": False,
            "nephrotoxicity": False,
            "requires_monitoring": ["Magnesium (long-term use)", "Vitamin B12 (long-term use)", "LFT", "Bone density"]
        },
        "guideline_tags": [
            "ACG 2017 GERD Guidelines",
            "FDA - Long-term PPI use monitoring",
            "UpToDate - Proton Pump Inhibitors"
        ]
    }
    # Lansoprazole và Omeprazole đã được chuyển sang proton_pump_inhibitors.py
}

__all__ = ['PROTON_PUMP_INHIBITOR_PPIS_DRUGS']
