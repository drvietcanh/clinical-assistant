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
    },
    "Rosuvastatin": {
        "group": "Cardiovascular - Statin (HMG-CoA Reductase Inhibitor)",
        "vietnamese_name": "Rosuvastatin, Crestor",
        "administration": ["PO"],
        "indications": [
            "Tăng cholesterol máu",
            "Phòng ngừa biến cố tim mạch",
            "Hội chứng chuyển hóa"
        ],
        "contraindications": [
            "Dị ứng rosuvastatin",
            "Bệnh gan hoạt động",
            "Có thai",
            "Đang cho con bú"
        ],
        "dosage": {
            "adult_start": "5-10mg x 1 lần/ngày (tối)",
            "adult_usual": "10-20mg x 1 lần/ngày",
            "adult_max": "40mg x 1 lần/ngày",
            "notes": "Uống với hoặc không thức ăn. Mạnh hơn atorvastatin ở liều tương đương"
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "Không đổi",
            "under_30": "Bắt đầu với 5mg/ngày"
        },
        "side_effects": [
            "Đau cơ, yếu cơ",
            "Tăng transaminase",
            "Tiêu cơ vân (hiếm nhưng nguy hiểm)",
            "Đau đầu",
            "Táo bón",
            "Đái tháo đường (nguy cơ tăng nhẹ)"
        ],
        "interactions": [
            "Cyclosporine: tăng nguy cơ độc tính",
            "Gemfibrozil: tăng nguy cơ độc cơ",
            "Warfarin: tăng INR",
            "Rifampin: giảm nồng độ rosuvastatin"
        ],
        "pregnancy": "X - Chống chỉ định",
        "mechanism_of_action": "Statin (HMG-CoA reductase inhibitor). Ức chế không chọn lọc enzyme HMG-CoA reductase trong gan, enzyme chính trong tổng hợp cholesterol. Giảm tổng hợp cholesterol nội sinh → tăng số lượng LDL receptors trên bề mặt tế bào gan → tăng thanh thải LDL từ máu. Giảm LDL cholesterol, giảm triglyceride, tăng nhẹ HDL cholesterol. Có tác dụng chống viêm và ổn định mảng xơ vữa (pleiotropic effects). Được dùng trong tăng cholesterol máu, dự phòng biến cố tim mạch (nhồi máu cơ tim, đột quỵ).",
        "monitoring": [
            "Lipid profile (LDL, HDL, triglyceride, total cholesterol) - kiểm tra 4-12 tuần sau khi bắt đầu, sau đó định kỳ",
            "Chức năng gan (ALT, AST) - tăng men gan (thường nhất thời), hiếm viêm gan",
            "CK (creatine kinase) - tăng CK, dấu hiệu tiêu cơ vân (myopathy, rhabdomyolysis)",
            "Dấu hiệu tiêu cơ vân (đau cơ, yếu cơ, nước tiểu sẫm màu) - nguy hiểm",
            "Đường huyết (có thể tăng nhẹ đường huyết)",
            "HbA1c (tăng nguy cơ đái tháo đường type 2)"
        ],
        "precautions": [
            "Nguy cơ tiêu cơ vân (myopathy, rhabdomyolysis) - nguy hiểm, có thể gây suy thận cấp",
            "Nguy cơ tăng ở: liều cao, suy thận, suy gan, người cao tuổi, dùng với fibrate, niacin, cyclosporine, diltiazem, verapamil",
            "NGỪNG NGAY nếu có đau cơ, yếu cơ, CK tăng > 10 lần ULN, hoặc dấu hiệu tiêu cơ vân",
            "Nguy cơ tăng men gan - kiểm tra ALT/AST trước khi bắt đầu, sau 12 tuần, và định kỳ",
            "Tăng nguy cơ đái tháo đường type 2 (nhẹ)",
            "Không dùng trong thai kỳ (gây dị tật thai nhi) - dùng biện pháp tránh thai",
            "Không dùng ở suy gan hoạt động",
            "Tương tác với nhiều thuốc: cyclosporine, gemfibrozil, diltiazem, verapamil → tăng nguy cơ tiêu cơ vân",
            "Liều khởi đầu thường: 10-20mg/ngày, liều tối đa: 40mg/ngày",
            "Uống với hoặc không có thức ăn"
        ],
        "pharmacokinetics": {
            "half_life": "19 giờ (dài)",
            "onset": "1-2 tuần (giảm LDL)",
            "duration": "Dài (nhiều ngày)",
            "protein_binding": "88%",
            "metabolism": "Gan (CYP2C9, CYP2C19) - chuyển hóa yếu, ít tương tác hơn các statin khác",
            "clearance": "Chủ yếu qua gan (90%), một phần qua thận (10%)"
        },
        "storage": "Bảo quản ở nhiệt độ phòng (20-25°C), tránh ẩm, tránh ánh sáng. Viên nén: tránh ẩm.",
        "black_box_warnings": "Nguy cơ tiêu cơ vân (rhabdomyolysis), có thể gây suy thận cấp và tử vong. Nguy cơ tăng ở liều cao, suy thận, và dùng với một số thuốc. Ngừng ngay nếu có đau cơ, yếu cơ, hoặc dấu hiệu tiêu cơ vân. Không dùng trong thai kỳ.",
        "drug_interactions": {
            "major": [
                {
                    "drug": "Cyclosporine, Tacrolimus",
                    "mechanism": "Cyclosporine ức chế OATP1B1 transporter và P-glycoprotein, tăng nồng độ rosuvastatin đáng kể",
                    "effect": "Tăng nguy cơ tiêu cơ vân nghiêm trọng, có thể gây suy thận cấp, tử vong",
                    "management": "CHỐNG CHỈ ĐỊNH dùng cùng. Nếu cần: giảm liều rosuvastatin tối đa 5mg/ngày, theo dõi CK và men gan thường xuyên. Cân nhắc dùng pravastatin (ít tương tác hơn)."
                },
                {
                    "drug": "Gemfibrozil, Fenofibrate (fibrates)",
                    "mechanism": "Fibrates và rosuvastatin đều có thể gây độc cơ, tác dụng hiệp đồng",
                    "effect": "Tăng nguy cơ tiêu cơ vân nghiêm trọng",
                    "management": "Thận trọng. Tránh dùng cùng nếu có thể. Nếu cần: dùng liều thấp cả hai, theo dõi CK và dấu hiệu đau cơ thường xuyên. KHÔNG dùng gemfibrozil với rosuvastatin (tăng nguy cơ cao). Có thể cân nhắc fenofibrate (ít tương tác hơn gemfibrozil)."
                }
            ],
            "moderate": [
                {
                    "drug": "Warfarin",
                    "mechanism": "Rosuvastatin có thể tăng tác dụng chống đông của warfarin",
                    "effect": "Tăng INR, tăng nguy cơ chảy máu",
                    "management": "Theo dõi INR thường xuyên khi bắt đầu hoặc thay đổi liều rosuvastatin. Có thể cần giảm liều warfarin."
                },
                {
                    "drug": "Diltiazem, Verapamil",
                    "mechanism": "Có thể tăng nhẹ nồng độ rosuvastatin qua OATP1B1",
                    "effect": "Tăng nguy cơ tiêu cơ vân",
                    "management": "Thận trọng. Giảm liều rosuvastatin 50% hoặc tối đa 10mg/ngày. Theo dõi CK và dấu hiệu đau cơ."
                },
                {
                    "drug": "Niacin (liều cao)",
                    "mechanism": "Cả hai đều có thể gây độc cơ, tác dụng hiệp đồng",
                    "effect": "Tăng nguy cơ tiêu cơ vân",
                    "management": "Thận trọng. Theo dõi CK và dấu hiệu đau cơ thường xuyên. Có thể cần giảm liều một trong hai thuốc."
                },
                {
                    "drug": "Colchicine",
                    "mechanism": "Có thể tăng tác dụng phụ độc cơ",
                    "effect": "Tăng nguy cơ độc cơ, đặc biệt ở bệnh nhân suy thận",
                    "management": "Thận trọng, đặc biệt ở bệnh nhân suy thận. Theo dõi CK và dấu hiệu đau cơ. Có thể cần giảm liều một trong hai thuốc."
                }
            ],
            "minor": [
                {
                    "drug": "Rifampin",
                    "mechanism": "Cảm ứng OATP1B1, giảm hấp thu rosuvastatin",
                    "effect": "Giảm hiệu quả rosuvastatin",
                    "management": "Có thể cần tăng liều rosuvastatin. Theo dõi lipid profile."
                },
                {
                    "drug": "Oral contraceptives",
                    "mechanism": "Rosuvastatin có thể tăng nhẹ nồng độ estrogen",
                    "effect": "Tăng nhẹ tác dụng phụ của thuốc tránh thai",
                    "management": "Thường không cần điều chỉnh. Theo dõi tác dụng phụ."
                }
            ]
        },
        "contraindications": {
            "tuyệt_đối": [
                "Bệnh gan hoạt động (active liver disease) - tăng men gan kéo dài, viêm gan",
                "Có thai (pregnancy) - FDA category X, gây dị tật thai nhi",
                "Cho con bú (lactation) - bài tiết vào sữa mẹ",
                "Tiêu cơ vân đang hoạt động (active myopathy/rhabdomyolysis)",
                "Dị ứng với rosuvastatin hoặc bất kỳ thành phần nào",
                "Dùng cùng cyclosporine (tăng nguy cơ tiêu cơ vân nghiêm trọng)"
            ],
            "tương_đối": [
                "Suy thận nặng (CrCl <30) - bắt đầu với liều thấp (5mg/ngày)",
                "Suy gan - thận trọng, theo dõi men gan thường xuyên",
                "Uống rượu nhiều - tăng nguy cơ viêm gan",
                "Người cao tuổi - tăng nguy cơ đau cơ, tiêu cơ vân",
                "Đái tháo đường - statins có thể tăng đường huyết nhẹ",
                "Bệnh tuyến giáp - tăng nguy cơ đau cơ",
                "Dùng với fibrate, niacin liều cao - tăng nguy cơ tiêu cơ vân",
                "Bệnh nhân Châu Á - tăng nồng độ rosuvastatin, có thể cần liều thấp hơn"
            ]
        },
        "pregnancy_lactation": {
            "fda_category": "X",
            "pregnancy_details": "CHỐNG CHỈ ĐỊNH trong thai kỳ. Rosuvastatin gây dị tật thai nhi, đặc biệt trong tam cá nguyệt đầu tiên. Statins ức chế tổng hợp cholesterol, cần thiết cho sự phát triển của thai nhi. Có thể gây dị tật bẩm sinh, chậm phát triển. Phụ nữ trong độ tuổi sinh đẻ phải dùng biện pháp tránh thai hiệu quả. Phải ngừng rosuvastatin ít nhất 1-2 tháng trước khi có thai. Nếu có thai khi đang dùng, ngừng ngay lập tức.",
            "lactation": {
                "safety": "Incompatible",
                "details": "Rosuvastatin bài tiết vào sữa mẹ. Có thể gây tác dụng phụ trên trẻ bú mẹ. Chưa có dữ liệu đầy đủ về an toàn. Statins có thể ảnh hưởng đến sự phát triển của trẻ.",
                "recommendation": "CHỐNG CHỈ ĐỊNH khi cho con bú. Ngừng rosuvastatin hoặc ngừng cho con bú. Cân nhắc thuốc thay thế nếu cần."
            }
        },
        "hepatic_adjustment": {
            "mild": "Không đổi liều. Theo dõi men gan thường xuyên.",
            "moderate": "Thận trọng. Giảm liều hoặc dùng liều thấp hơn. Theo dõi men gan mỗi 3-6 tháng. Ngừng nếu ALT >3 lần ULN.",
            "severe": "CHỐNG CHỈ ĐỊNH. Không dùng ở bệnh nhân suy gan nặng hoặc bệnh gan hoạt động.",
            "notes": "Rosuvastatin chuyển hóa qua gan (CYP2C9, CYP2C19) - chuyển hóa yếu hơn atorvastatin/simvastatin, ít tương tác hơn. Tuy nhiên, suy gan vẫn có thể làm tăng nồng độ và tăng nguy cơ độc tính. Kiểm tra men gan trước điều trị. Ngừng nếu ALT >3 lần ULN hoặc có dấu hiệu viêm gan."
        },
        "overdose_management": {
            "symptoms": [
                "Tiêu cơ vân (rhabdomyolysis) - triệu chứng chính và nguy hiểm nhất",
                "Đau cơ dữ dội, yếu cơ",
                "Nước tiểu sẫm màu (myoglobinuria)",
                "Suy thận cấp (do myoglobin)",
                "Tăng men gan (ALT, AST)",
                "Tăng CK (creatine kinase)",
                "Mệt mỏi, buồn nôn",
                "Rối loạn tiêu hóa"
            ],
            "antidote": "Không có antidote đặc hiệu. Điều trị hỗ trợ: ngừng rosuvastatin, truyền dịch tích cực để phòng suy thận, lọc máu nếu cần",
            "treatment": [
                "Ngừng rosuvastatin ngay lập tức",
                "Đo CK, men gan, chức năng thận ngay",
                "Nếu có tiêu cơ vân:",
                "  - Truyền dịch tích cực (normal saline 1-2L/giờ) để duy trì lượng nước tiểu >100-200ml/giờ",
                "  - Kiềm hóa nước tiểu (sodium bicarbonate) để giảm độc tính myoglobin trên thận",
                "  - Theo dõi chức năng thận (creatinine, BUN, lượng nước tiểu)",
                "  - Hemodialysis nếu suy thận cấp, tăng kali máu, hoặc quá tải dịch",
                "  - Theo dõi điện giải (natri, kali, canxi, phosphate)",
                "Điều trị hỗ trợ:",
                "  - Điều chỉnh rối loạn điện giải",
                "  - Hỗ trợ hô hấp và tuần hoàn nếu cần",
                "  - Giảm đau (opioids) nếu đau cơ nặng",
                "Theo dõi CK, men gan, chức năng thận hàng ngày cho đến khi ổn định",
                "Theo dõi ít nhất 48-72 giờ do half-life 19 giờ (dài)"
            ],
            "monitoring": "CK, ALT, AST, creatinine, BUN, kali, canxi, phosphate, lượng nước tiểu, ECG (nếu có rối loạn điện giải), dấu hiệu suy thận"
        },
        "reversal_agents": {
            "available": False,
            "agents": []
        },
        "administration_instructions": {
            "oral": {
                "with_food": "Có thể uống với hoặc không có thức ăn. Không ảnh hưởng đáng kể đến hấp thu.",
                "timing": "Uống 1 lần/ngày, có thể uống vào buổi sáng hoặc buổi tối. Uống cùng một giờ mỗi ngày để nhớ. Không cần thiết phải uống buổi tối như simvastatin (rosuvastatin có half-life dài 19 giờ)."
            },
            "iv": {
                "reconstitution": "Không có dạng IV",
                "infusion_rate": "Không áp dụng",
                "compatibility": [],
                "incompatibility": [],
                "notes": "Rosuvastatin chỉ có dạng uống (PO)."
            }
        },
        "references": {
            "primary_sources": [
                "FDA Drug Label - Crestor (rosuvastatin)",
                "UpToDate - Rosuvastatin: Drug information",
                "ACC/AHA Guidelines - Cholesterol Management (2018)",
                "NLA Guidelines - Statin Safety (2014)",
                "JUPITER Study - New England Journal of Medicine (2008) - Rosuvastatin trong dự phòng biến cố tim mạch",
                "Goodman & Gilman's Pharmacological Basis of Therapeutics - Lipid-lowering drugs"
            ],
            "last_updated": "2024-12-19",
            "evidence_level": "High - Multiple large RCTs (JUPITER, CORONA) showing cardiovascular benefit"
        }
    }
}

__all__ = ['STATINS_DRUGS']

