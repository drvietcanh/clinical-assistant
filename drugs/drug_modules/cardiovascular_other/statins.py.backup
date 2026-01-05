"""
Cardiovascular Statin Drugs
Rosuvastatin
"""

STATINS_DRUGS = {
    "High-intensity statin (đột quỵ/TIA)": {
        "group": "Cardiovascular - Statin (high-intensity, secondary prevention stroke/TIA)",
        "vietnamese_name": "Atorvastatin 40-80mg hoặc Rosuvastatin 20-40mg",
        "administration": ["PO"],
        "indications": [
            "Dự phòng thứ phát sau đột quỵ thiếu máu não/TIA do xơ vữa",
            "Hẹp động mạch cảnh/động mạch não do xơ vữa (điều trị nội khoa hoặc sau can thiệp)",
            "Sau hội chứng vành cấp/nhồi máu cơ tim kèm nguy cơ đột quỵ",
        ],
        "contraindications": [
            "Bệnh gan hoạt động hoặc men gan tăng kéo dài",
            "Có thai hoặc cho con bú",
            "Tiêu cơ vân đang hoạt động",
            "Dị ứng với statin",
        ],
        "dosage": {
            "atorvastatin_high": "40-80mg x 1 lần/ngày",
            "rosuvastatin_high": "20-40mg x 1 lần/ngày",
            "timing": "Uống buổi tối hoặc bất kỳ thời điểm cố định trong ngày",
            "notes": "Bắt đầu/tiếp tục trong 24-48 giờ đầu sau AIS/TIA khi nuốt được và đã loại trừ xuất huyết sau tiêu sợi huyết/EVT. Mục tiêu LDL-C <70 mg/dL hoặc giảm ≥50%.",
        },
        "renal_adjustment": {
            "normal": "Không cần chỉnh (ưu tiên atorvastatin nếu chức năng thận giảm)",
            "30_60": "Rosuvastatin khởi đầu 10-20mg; atorvastatin không cần chỉnh",
            "under_30": "Tránh rosuvastatin >10-20mg; ưu tiên atorvastatin và theo dõi CK/men gan",
        },
        "side_effects": [
            "Đau cơ/ yếu cơ; hiếm tiêu cơ vân",
            "Tăng men gan thoáng qua",
            "Tăng đường huyết nhẹ",
            "Rối loạn tiêu hóa, nhức đầu",
        ],
        "interactions": [
            "Ức chế CYP3A4 mạnh (clarithromycin, itraconazole, protease inhibitor) tăng nồng độ atorvastatin",
            "Cyclosporine/gemfibrozil: tăng nguy cơ tiêu cơ vân (cả atorvastatin, rosuvastatin)",
            "Niacin liều cao, fibrate: tăng nguy cơ độc cơ",
            "Warfarin: có thể tăng INR",
        ],
        "pregnancy": "X - Chống chỉ định",
        "mechanism_of_action": (
            "Ức chế HMG-CoA reductase → giảm tổng hợp cholesterol gan, tăng LDL receptor, giảm LDL-C. "
            "Hiệu ứng chống viêm/ổn định mảng xơ vữa giúp giảm tái phát đột quỵ và biến cố tim mạch."
        ),
        "monitoring": [
            "Lipid profile sau 4-12 tuần, sau đó mỗi 3-12 tháng (mục tiêu LDL-C <70 mg/dL)",
            "AST/ALT trước điều trị, sau 12 tuần hoặc khi có triệu chứng",
            "CK khi đau cơ hoặc nguy cơ cao",
            "Đường huyết/HbA1c ở bệnh nhân đái tháo đường/nguy cơ cao",
        ],
        "precautions": [
            "Nếu dùng tiêu sợi huyết, thường khởi statin sau 24 giờ và sau CT loại trừ xuất huyết.",
            "Ngừng statin nếu CK >10x ULN hoặc men gan >3x ULN kèm triệu chứng.",
            "Tránh phối hợp ức chế CYP3A4 mạnh với atorvastatin; giảm liều rosuvastatin khi dùng cyclosporine/gemfibrozil.",
            "Tư vấn tránh thai hiệu quả cho phụ nữ trong độ tuổi sinh đẻ.",
        ],
        "pharmacokinetics": {
            "half_life": "Atorvastatin ~14 giờ; Rosuvastatin ~19 giờ",
            "onset": "Giảm LDL sau 1-2 tuần, tối đa 4-6 tuần",
            "duration": "24 giờ với dùng hàng ngày",
            "protein_binding": ">95%",
            "clearance": "Atorvastatin: gan (CYP3A4); Rosuvastatin: gan (CYP2C9/2C19 nhẹ), thận 10%",
        },
        "storage": "Bảo quản nhiệt độ phòng 20-25°C, tránh ẩm và ánh sáng.",
        "black_box_warnings": "Nguy cơ tiêu cơ vân và viêm gan; ngừng ngay nếu đau cơ nặng, nước tiểu sẫm, hoặc men gan tăng nhiều.",
        "drug_interactions": {
            "major": [
                {
                    "drug": "Cyclosporine, Tacrolimus",
                    "mechanism": "Ức chế OATP1B1/P-gp, tăng nồng độ statin",
                    "effect": "Tăng nguy cơ tiêu cơ vân nặng",
                    "management": "Tránh nếu có thể; nếu bắt buộc dùng liều rất thấp và theo dõi CK.",
                },
                {
                    "drug": "Gemfibrozil",
                    "mechanism": "Hiệp đồng độc cơ",
                    "effect": "Tăng nguy cơ tiêu cơ vân",
                    "management": "Tránh phối hợp; nếu cần hạ triglyceride, cân nhắc fenofibrate và giảm liều statin.",
                },
            ],
            "moderate": [
                {
                    "drug": "Clarithromycin, Erythromycin, Azole (ketoconazole, itraconazole)",
                    "mechanism": "Ức chế CYP3A4 (atorvastatin)",
                    "effect": "Tăng nguy cơ độc cơ",
                    "management": "Giảm liều hoặc tạm ngừng atorvastatin; chọn rosuvastatin liều thấp nếu cần.",
                },
                {
                    "drug": "Niacin liều cao, Fenofibrate",
                    "mechanism": "Hiệp đồng độc cơ",
                    "effect": "Tăng nguy cơ tiêu cơ vân",
                    "management": "Theo dõi CK và triệu chứng cơ; cân nhắc giảm liều.",
                },
                {
                    "drug": "Warfarin",
                    "mechanism": "Tăng nhẹ tác dụng chống đông",
                    "effect": "Tăng INR",
                    "management": "Theo dõi INR khi khởi statin hoặc thay đổi liều.",
                },
            ],
            "minor": [
                {
                    "drug": "Rifampin, Phenytoin",
                    "mechanism": "Cảm ứng CYP3A4/UGT (atorvastatin)",
                    "effect": "Giảm hiệu quả hạ LDL",
                    "management": "Theo dõi LDL và điều chỉnh liều nếu cần.",
                }
            ],
        },
        "contraindications_detail": {
            "tuyệt_đối": [
                "Bệnh gan hoạt động, ALT/AST tăng kéo dài",
                "Có thai hoặc cho con bú",
                "Tiêu cơ vân đang hoạt động",
            ],
            "tương_đối": [
                "Tiền sử không dung nạp statin",
                "Suy thận (ưu tiên atorvastatin; nếu dùng rosuvastatin cần liều thấp)",
                "Dùng kèm thuốc ức chế CYP3A4 hoặc OATP1B1",
                "Người cao tuổi hoặc BMI thấp (tăng nguy cơ đau cơ)",
            ],
        },
        "pregnancy_lactation": {
            "fda_category": "X",
            "pregnancy_details": "Chống chỉ định; statin có thể gây dị tật thai và ảnh hưởng tổng hợp cholesterol của thai.",
            "lactation": {
                "safety": "Incompatible",
                "details": "Bài tiết vào sữa mẹ; nguy cơ ảnh hưởng phát triển lipid của trẻ.",
                "recommendation": "Ngừng statin hoặc ngừng cho bú.",
            },
        },
        "hepatic_adjustment": {
            "mild": "Thận trọng, theo dõi men gan",
            "moderate": "Giảm liều hoặc tránh nếu men gan tăng kéo dài",
            "severe": "Tránh dùng (nguy cơ tích lũy và độc gan)",
        },
        "overdose_management": {
            "symptoms": ["Đau cơ nặng, CK tăng, tiêu cơ vân, tăng men gan"],
            "antidote": "Không có antidote đặc hiệu",
            "treatment": [
                "Ngừng statin",
                "Truyền dịch tích cực nếu nghi tiêu cơ vân; kiềm hóa nước tiểu nếu cần",
                "Theo dõi CK, men gan, creatinine",
                "Lọc máu nếu suy thận cấp do tiêu cơ vân",
            ],
            "monitoring": "CK, creatinine, AST/ALT, điện giải, lượng nước tiểu",
        },
        "reversal_agents": None,
        "administration_instructions": {
            "oral": {
                "with_food": "Có thể uống với hoặc không thức ăn",
                "timing": "Uống 1 lần/ngày; tuân thủ thời điểm cố định để tăng tuân thủ",
            }
        },
        "references": {
            "primary_sources": [
                "AHA/ASA 2021–2023 Secondary Stroke Prevention Guidelines (statin cường độ cao)",
                "ACC/AHA Cholesterol Guidelines 2018/2022 updates",
                "SPARCL trial (atorvastatin 80mg giảm tái phát đột quỵ)",
            ],
            "last_updated": "2025-03-02",
            "evidence_level": "A (giảm tái phát đột quỵ/tim mạch)",
        },
             "reversal_agents": {
             "available": False,
             "agents": []
         },
},
}

__all__ = ['STATINS_DRUGS']

