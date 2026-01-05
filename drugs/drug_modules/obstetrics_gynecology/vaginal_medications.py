"""
Obstetrics and Gynecology Medications
Vaginal medications (antifungals, antibacterials)
"""
from typing import Dict, Any

VAGINAL_MEDICATIONS_DRUGS: Dict[str, Dict[str, Any]] = {
    "Clotrimazole (vaginal)":     {
        "group": "Obstetrics/Gynecology - Antifungal (Vulvovaginal Candidiasis)",
        "vietnamese_name": "Clotrimazole đặt âm đạo (Canesten, Mycelex-G)",
        "administration": [
            "Vaginal"
    ],
        "indications": [
            "Nhiễm nấm Candida âm đạo – vulvovaginal candidiasis (VVC) thể nhẹ đến trung bình"
    ],
        "contraindications": [
            "Dị ứng với clotrimazole hoặc bất kỳ thành phần nào của thuốc"
    ],
        "dosage": {
            "adult_vvc_1_day": "Viên đặt 500mg âm đạo, 1 lần duy nhất buổi tối",
            "adult_vvc_3_day": "Viên đặt 200mg âm đạo, 1 viên mỗi tối x 3 ngày",
            "adult_vvc_7_day": "Viên đặt 100mg âm đạo, 1 viên mỗi tối x 7 ngày",
            "notes": "Đặt sâu vào âm đạo trước khi ngủ. Có thể dùng thêm kem bôi ngoài âm hộ nếu ngứa nhiều.",
        },
        "renal_adjustment": {
            "normal": "Không cần chỉnh liều (tác dụng tại chỗ)",
            "30_60": "Không cần chỉnh liều",
            "under_30": "Không cần chỉnh liều",
        },
        "side_effects": [
            "Kích ứng tại chỗ: nóng rát, ngứa, châm chích nhẹ",
            "Tiết dịch tăng tạm thời",
            "Phản ứng dị ứng rất hiếm"
    ],
        "interactions": [
            "Ít tương tác toàn thân do hấp thu rất ít; có thể làm giảm độ bền bao cao su/diaphragm latex trong thời gian dùng."
    ],
        "pregnancy": """B – có thể dùng trong thai kỳ (ưu tiên phác đồ 7 ngày, đặt bằng tay thay vì dụng cụ nếu 3 tháng cuối).""",
        "mechanism_of_action": """Clotrimazole là azole chống nấm, ức chế tổng hợp ergosterol màng tế bào nấm, làm thay đổi tính thấm màng, gây chết tế bào nấm Candida tại chỗ.""",
        "monitoring": [
            "Giảm triệu chứng ngứa, khí hư vón cục sau 3–7 ngày",
            "Nếu triệu chứng tái phát thường xuyên (≥4 lần/năm) → cần đánh giá VVC tái phát, tiểu đường, suy giảm miễn dịch"
    ],
        "precautions": [
            "Tránh quan hệ trong thời gian điều trị hoặc dùng bao cao su; lưu ý thuốc có thể làm giảm độ bền latex.",
            "Nếu triệu chứng không cải thiện sau 7 ngày hoặc tái phát nhiều lần, cần khám phụ khoa để loại trừ chẩn đoán khác."
    ],
        "pharmacokinetics": {
            "half_life": "Không áp dụng (tác dụng tại chỗ, hấp thu rất ít)",
            "onset": "Vài giờ – vài ngày",
            "duration": "Tác dụng kéo dài trong ngày sau đặt",
            "protein_binding": "Không đáng kể toàn thân",
            "clearance": "Chủ yếu tại chỗ, phần rất nhỏ hấp thu chuyển hóa ở gan.",
        },
        "storage": "Bảo quản nơi khô mát, tránh nhiệt độ cao.",
        "black_box_warnings": "Cần xem xét black box warnings",
        "drug_interactions": {
            "major": [],
            "moderate": [],
            "minor": [],
        },
        "contraindications_detail": {
            "tuyệt_đối": [
                "Dị ứng với clotrimazole hoặc tá dược"
    ],
            "tương_đối": [
                "Âm đạo trợt loét nhiều (cần khám trước khi tự điều trị)"
    ],
        },
        "pregnancy_lactation": {
            "fda_category": "B",
            "pregnancy_details": "Phác đồ đặt 7 ngày được ưa chuộng trong thai kỳ; tránh dụng cụ đặt cứng ở 3 tháng cuối.",
            "lactation": {
                "safety": "Compatible",
                "details": "Hấp thu toàn thân rất ít; an toàn khi cho con bú.",
                "recommendation": "Có thể dùng khi cho con bú.",
            },
        },
        "hepatic_adjustment": {
            "mild": "Không cần chỉnh liều",
            "moderate": "Không cần chỉnh liều",
            "severe": "Không cần chỉnh liều",
            "notes": "Hấp thu toàn thân tối thiểu.",
        },
        "overdose_management": {
            "symptoms": [
                "Kích ứng tại chỗ tăng (rát, đỏ, ngứa nhiều)"
    ],
            "antidote": "Không có; điều trị hỗ trợ.",
            "treatment": [
                "Ngừng thuốc, rửa sạch bằng nước",
                "Điều trị triệu chứng nếu cần (kem dưỡng, kháng histamine đường uống nếu ngứa nhiều)"
    ],
            "monitoring": "Theo dõi cải thiện kích ứng tại chỗ.",
        },
        "reversal_agents": {
            "available": False,
            "agents": [],
            "notes": """Không có antidote đặc hiệu. Điều trị chủ yếu là hỗ trợ và điều trị triệu chứng. Rửa sạch vùng âm đạo nếu cần.""",
        },
        "administration_instructions": {
            "vaginal": {
                "with_food": "Không liên quan bữa ăn.",
                "timing": "Đặt buổi tối trước khi ngủ; nằm ngửa và đưa viên/ống đặt sâu vào âm đạo.",
            },
        },
        "references": {
            "primary_sources": [
                "CDC STI Treatment Guidelines – Vulvovaginal candidiasis",
                "UpToDate – Clotrimazole vaginal: Drug information"
    ],
            "last_updated": "2025-02-23",
            "evidence_level": "High – guideline-based local therapy",
        },
            "risk_flags": {
                "high_alert": False,
                "narrow_therapeutic_index": False,
                "bleeding_risk": False,
                "organ_toxicity": [],
                "qt_prolongation": False,
                "hepatotoxicity": False,
                "nephrotoxicity": False,
                "requires_monitoring": [],
            },
            "guideline_tags": [
                "FDA Drug Information",
                "UpToDate Drug Information",
            ]
    },

    "Metronidazole (vaginal gel)":     {
        "group": "Obstetrics/Gynecology - Nitroimidazole (Bacterial Vaginosis)",
        "vietnamese_name": "Metronidazole gel âm đạo 0,75%",
        "administration": [
            "Vaginal"
    ],
        "indications": [
            "Bacterial vaginosis (BV) – viêm âm đạo do vi khuẩn"
    ],
        "contraindications": [
            "Dị ứng với metronidazole hoặc nitroimidazole",
            "Ba tháng đầu thai kỳ (thận trọng, ưu tiên đường uống theo phác đồ nếu cần)"
    ],
        "dosage": {
            "adult_bv": "Gel 0,75%: 5g bơm âm đạo 1 lần/ngày vào buổi tối x 5 ngày",
            "notes": "Không nên dùng chung với bao cao su/diaphragm latex trong khi điều trị (có thể ảnh hưởng vật liệu).",
        },
        "renal_adjustment": {
            "normal": "Không cần chỉnh liều (hấp thu toàn thân thấp)",
            "30_60": "Không cần chỉnh liều",
            "under_30": "Không cần chỉnh liều",
        },
        "side_effects": [
            "Kích ứng âm đạo nhẹ, nóng rát, ngứa",
            "Tiết dịch tăng tạm thời",
            "Vị kim loại, buồn nôn rất hiếm (do hấp thu nhỏ)"
    ],
        "interactions": [
            "Rượu: lý thuyết có phản ứng giống disulfiram nhưng với dạng gel nguy cơ rất thấp."
    ],
        "pregnancy": "B – thường tránh 3 tháng đầu; dùng được từ tam cá nguyệt 2–3 theo hướng dẫn.",
        "mechanism_of_action": """Metronidazole là nitroimidazole, được khử trong tế bào vi khuẩn kỵ khí, tạo gốc tự do gây phá hủy DNA vi khuẩn. Dạng gel âm đạo tập trung tác dụng tại chỗ trên Gardnerella và vi khuẩn kỵ khí gây BV, giảm hấp thu toàn thân.""",
        "monitoring": [
            "Giảm khí hư hôi, giảm ngứa/sưng sau 3–5 ngày",
            "Nếu không cải thiện hoặc tái phát nhiều lần, cần xét nghiệm và loại trừ STI khác."
    ],
        "precautions": [
            "Tránh quan hệ đường âm đạo trong thời gian điều trị hoặc dùng bao cao su; lưu ý tương tác với latex.",
            "Nếu bệnh nhân có viêm âm đạo nặng/huyết trắng lẫn máu, cần khám phụ khoa trước khi dùng."
    ],
        "pharmacokinetics": {
            "half_life": "Tác dụng tại chỗ; phần nhỏ hấp thu có t1/2 khoảng 8 giờ",
            "onset": "Vài ngày",
            "duration": "Tác dụng trong ngày sau bơm",
            "protein_binding": "~20% (phần hấp thu)",
            "clearance": "Gan (chuyển hóa) và thận (thải trừ) cho phần hấp thu nhỏ.",
        },
        "storage": "Bảo quản ở nhiệt độ phòng, tránh nóng; giữ ống thuốc kín nắp.",
        "black_box_warnings": None,
        "drug_interactions": {
            "major": [],
            "moderate": [],
            "minor": [],
        },
        "contraindications_detail": {
            "tuyệt_đối": [
                "Dị ứng metronidazole/nitroimidazole"
    ],
            "tương_đối": [
                "Ba tháng đầu thai kỳ"
    ],
        },
        "pregnancy_lactation": {
            "fda_category": "B",
            "pregnancy_details": "Dạng gel âm đạo với hấp thu thấp; tránh 3 tháng đầu nếu có lựa chọn khác.",
            "lactation": {
                "safety": "Compatible",
                "details": "Hấp thu ít, lượng vào sữa thấp; nguy cơ thấp cho trẻ bú mẹ.",
                "recommendation": "Có thể dùng khi cho con bú; nếu lo lắng có thể cho bú trước khi dùng thuốc.",
            },
        },
        "hepatic_adjustment": {
            "mild": "Không cần chỉnh liều",
            "moderate": "Không cần chỉnh liều",
            "severe": "Thận trọng; hấp thu toàn thân thấp nhưng vẫn nên theo dõi nếu dùng kéo dài.",
            "notes": "Phần hấp thu nhỏ chuyển hóa ở gan.",
        },
        "overdose_management": {
            "symptoms": [
                "Kích ứng âm đạo tăng"
    ],
            "antidote": "Không có; điều trị hỗ trợ.",
            "treatment": [
                "Ngừng thuốc; rửa sạch nếu kích ứng nhiều."
    ],
            "monitoring": "Theo dõi giảm kích ứng; nếu không cải thiện, khám phụ khoa.",
        },
        "reversal_agents": {
            "available": False,
            "agents": [],
            "notes": """Không có antidote đặc hiệu. Điều trị chủ yếu là hỗ trợ và điều trị triệu chứng. Rửa sạch vùng âm đạo nếu cần.""",
        },
        "administration_instructions": {
            "vaginal": {
                "with_food": "Không liên quan bữa ăn.",
                "timing": "Bơm 5g gel vào âm đạo buổi tối trước ngủ trong 5 ngày; sử dụng applicator đúng cách.",
            },
        },
        "references": {
            "primary_sources": [
                "CDC STI Treatment Guidelines – Bacterial vaginosis",
                "UpToDate – Metronidazole vaginal: Drug information"
    ],
            "last_updated": "2025-02-23",
            "evidence_level": "High – guideline-recommended local therapy",
        },
            "risk_flags": {
                "high_alert": False,
                "narrow_therapeutic_index": False,
                "bleeding_risk": False,
                "organ_toxicity": [],
                "qt_prolongation": False,
                "hepatotoxicity": False,
                "nephrotoxicity": False,
                "requires_monitoring": [],
            },
            "guideline_tags": [
                "FDA Drug Information",
                "UpToDate Drug Information",
            ]
    },

    "Miconazole (vaginal)":     {
        "group": "Obstetrics/Gynecology - Antifungal (Vulvovaginal Candidiasis)",
        "vietnamese_name": "Miconazole đặt âm đạo",
        "administration": [
            "Vaginal"
    ],
        "indications": [
            "Nhiễm nấm Candida âm đạo – VVC thể nhẹ đến trung bình"
    ],
        "contraindications": [
            "Dị ứng với miconazole hoặc azole khác"
    ],
        "dosage": {
            "adult_vvc_3_day": "Viên đặt 200mg âm đạo, 1 viên mỗi tối x 3 ngày",
            "adult_vvc_7_day": "Viên đặt 100mg âm đạo, 1 viên mỗi tối x 7 ngày",
            "notes": "Có thể kèm kem bôi ngoài âm hộ nếu ngứa/nóng rát vùng ngoài.",
        },
        "renal_adjustment": {
            "normal": "Không cần chỉnh liều",
            "30_60": "Không cần chỉnh liều",
            "under_30": "Không cần chỉnh liều",
        },
        "side_effects": [
            "Kích ứng tại chỗ: nóng rát, ngứa, châm chích",
            "Tiết dịch tăng tạm thời"
    ],
        "interactions": [
            "Có thể làm giảm độ bền bao cao su/diaphragm latex trong khi dùng."
    ],
        "pregnancy": "C – thường tránh liều cao ngắn ngày; có thể dùng dạng 7 ngày nếu cần, theo bác sĩ.",
        "mechanism_of_action": ("Miconazole là azole chống nấm, ức chế tổng hợp ergosterol màng tế bào nấm, gây thay đổi tính thấm màng và chết tế bào nấm. Tác dụng chủ yếu tại chỗ ở âm đạo."),
        "monitoring": [
            "Giảm ngứa, khí hư sau 3–7 ngày"
    ],
        "precautions": [
            "Nếu triệu chứng không cải thiện hoặc tái phát nhiều lần, cần khám phụ khoa và xét nghiệm."
    ],
        "pharmacokinetics": {
            "half_life": "Không áp dụng (tại chỗ)",
            "onset": "Vài giờ – vài ngày",
            "duration": "Trong ngày sau đặt",
            "protein_binding": "Không đáng kể toàn thân",
            "clearance": "Chủ yếu tại chỗ; phần nhỏ hấp thu được chuyển hóa ở gan.",
        },
        "storage": "Bảo quản nơi khô mát, tránh ánh sáng.",
        "black_box_warnings": "Cần xem xét black box warnings",
        "drug_interactions": {
            "major": [],
            "moderate": [],
            "minor": [],
        },
        "contraindications_detail": {
            "tuyệt_đối": [
                "Dị ứng với miconazole hoặc azole"
    ],
            "tương_đối": [
                "Âm đạo trợt loét, đau nhiều – cần khám trước khi dùng"
    ],
        },
        "pregnancy_lactation": {
            "fda_category": "C",
            "pregnancy_details": "Chỉ dùng khi lợi ích vượt nguy cơ; ưu tiên clotrimazole/nhóm B nếu khả dụng.",
            "lactation": {
                "safety": "Compatible",
                "details": "Hấp thu toàn thân rất thấp; ít nguy cơ cho trẻ bú mẹ.",
                "recommendation": "Có thể dùng khi cho con bú.",
            },
        },
        "hepatic_adjustment": {
            "mild": "Không cần chỉnh liều",
            "moderate": "Không cần chỉnh liều",
            "severe": "Không cần chỉnh liều",
            "notes": "Tác dụng chủ yếu tại chỗ.",
        },
        "overdose_management": {
            "symptoms": [
                "Kích ứng tại chỗ tăng"
    ],
            "antidote": "Không có; điều trị hỗ trợ.",
            "treatment": [
                "Ngừng thuốc, rửa sạch vùng âm đạo – âm hộ bằng nước sạch"
    ],
            "monitoring": "Theo dõi triệu chứng kích ứng.",
        },
        "reversal_agents": {
            "available": False,
            "agents": [],
            "notes": """Không có antidote đặc hiệu. Điều trị chủ yếu là hỗ trợ và điều trị triệu chứng. Rửa sạch vùng âm đạo nếu cần.""",
        },
        "administration_instructions": {
            "vaginal": {
                "with_food": "Không liên quan bữa ăn.",
                "timing": "Đặt buổi tối trước ngủ; tránh đứng dậy ngay sau khi đặt.",
            },
        },
        "references": {
            "primary_sources": [
                "CDC STI Treatment Guidelines – Vulvovaginal candidiasis",
                "UpToDate – Miconazole vaginal: Drug information"
    ],
            "last_updated": "2025-02-23",
            "evidence_level": "High – widely used local antifungal",
        },
            "risk_flags": {
                "high_alert": False,
                "narrow_therapeutic_index": False,
                "bleeding_risk": False,
                "organ_toxicity": [],
                "qt_prolongation": False,
                "hepatotoxicity": False,
                "nephrotoxicity": False,
                "requires_monitoring": [],
            },
            "guideline_tags": [
                "FDA Drug Information",
                "UpToDate Drug Information",
            ]
    },

}

__all__ = ['VAGINAL_MEDICATIONS_DRUGS']
