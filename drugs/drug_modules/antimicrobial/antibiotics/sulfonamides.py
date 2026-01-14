"""
Sulfonamide Antibiotics
"""
SULFONAMIDE_ANTIBIOTICS = {
    "Trimethoprim-sulfamethoxazole": {
    "group": "Antibiotic - Sulfonamide",
    "vietnamese_name": "Trimethoprim-sulfamethoxazole, Bactrim, Septra, Cotrimoxazole",
    "administration": ["PO", "IV"],
    "indications": [
        "Nhiễm khuẩn đường tiết niệu",
        "Viêm phổi do Pneumocystis jirovecii (PJP)",
        "Nhiễm khuẩn do Toxoplasma",
        "Nhiễm khuẩn do MRSA",
        "Nhiễm khuẩn đường hô hấp"
    ],
    "contraindications": [
        "Dị ứng sulfonamide",
        "Suy thận nặng (CrCl <15)",
        "Suy gan nặng",
        "Thiếu máu do thiếu folate",
        "Có thai (gần sinh)"
    ],
    "dosage": {
        "adult_uti": "160/800mg (DS) x 2 lần/ngày",
        "adult_pjp": "160/800mg (DS) x 3-4 lần/ngày",
        "adult_pjp_iv": "15-20mg/kg (TMP) IV mỗi 6-8 giờ",
        "notes": "Tỷ lệ TMP:SMX = 1:5. Dùng với nhiều nước"
    },
    "renal_adjustment": {
        "normal": "Không đổi",
        "30_60": "Giảm liều 50%",
        "under_30": "Tránh dùng nếu CrCl <15"
    },
    "side_effects": [
        "Phát ban (thường gặp)",
        "Tăng kali máu",
        "Giảm bạch cầu",
        "Thiếu máu",
        "Tăng creatinine (giả, không phản ánh suy thận)",
        "Độc tính da (SJS/TEN - hiếm nhưng nguy hiểm)"
    ],
    "interactions": [
        "Warfarin: tăng tác dụng",
        "Phenytoin: tăng nồng độ phenytoin",
        "ACE inhibitor: tăng kali máu",
        "Methotrexate: tăng độc tính"
    ],
        "pregnancy": "C - D gần sinh",
    "mechanism_of_action": "Trimethoprim-sulfamethoxazole (TMP-SMX, cotrimoxazole) là kháng sinh kết hợp với tác dụng hiệp đồng (synergistic). Sulfamethoxazole (SMX) là sulfonamide ức chế tổng hợp acid folic ở vi khuẩn bằng cách ức chế enzyme dihydropteroate synthase, ngăn chặn tổng hợp dihydrofolic acid. Trimethoprim (TMP) ức chế enzyme dihydrofolate reductase, ngăn chặn chuyển đổi dihydrofolic acid thành tetrahydrofolic acid, một cofactor cần thiết cho tổng hợp DNA, RNA, và protein. Cả hai chất cùng ức chế con đường tổng hợp acid folic ở hai bước khác nhau, tạo ra tác dụng hiệp đồng mạnh. Tỷ lệ TMP:SMX = 1:5 (160mg TMP : 800mg SMX). Phổ kháng khuẩn: Gram-dương (một số Staphylococcus, Streptococcus), Gram-âm (Enterobacteriaceae, H. influenzae), và một số vi khuẩn không điển hình (Pneumocystis jirovecii, Toxoplasma gondii, Nocardia).",
    "monitoring": [
        "Dấu hiệu nhiễm trùng (sốt, WBC, triệu chứng lâm sàng) để đánh giá đáp ứng điều trị",
        "Cấy máu và cấy từ vị trí nhiễm trùng (nếu có) để xác định vi khuẩn và độ nhạy cảm",
        "Điện giải (natri, kali) - tăng kali máu (đặc biệt ở người cao tuổi, suy thận, dùng ACE inhibitor/ARB)",
        "Công thức máu (CBC) - giảm bạch cầu, thiếu máu, giảm tiểu cầu (do thiếu folate)",
        "Creatinine - tăng creatinine giả (do ức chế bài tiết creatinine ở ống thận, không phản ánh suy thận thực sự)",
        "Chức năng gan (ALT, AST) - hiếm viêm gan nặng",
        "Dấu hiệu phản ứng dị ứng (phát ban, sốt) - có thể tiến triển thành SJS/TEN",
        "Dấu hiệu SJS/TEN (Stevens-Johnson syndrome, toxic epidermal necrolysis) - phát ban, mụn nước, bong da",
        "Tương tác với warfarin (tăng INR), phenytoin (tăng nồng độ), methotrexate (tăng độc tính)"
    ],
    "precautions": [
        "Phản ứng dị ứng - nguy cơ cao với sulfonamide, đặc biệt SJS/TEN (hiếm nhưng nguy hiểm, có thể tử vong)",
        "NGỪNG NGAY nếu có phát ban, sốt, mụn nước, bong da - có thể là SJS/TEN",
        "Tăng kali máu - đặc biệt ở người cao tuổi, suy thận, dùng ACE inhibitor/ARB, trimethoprim",
        "Không dùng nếu CrCl <15 (tăng nguy cơ tác dụng phụ, không hiệu quả)",
        "Tăng creatinine giả - không phản ánh suy thận thực sự, do ức chế bài tiết creatinine",
        "Thiếu máu, giảm bạch cầu - do ức chế tổng hợp folate, đặc biệt ở bệnh nhân thiếu folate",
        "Không dùng gần sinh (trong 3 tháng cuối thai kỳ) - nguy cơ kernicterus ở trẻ sơ sinh",
        "Uống nhiều nước để tránh kết tinh trong nước tiểu (sulfamethoxazole)",
        "Tương tác với nhiều thuốc: warfarin (tăng INR), phenytoin (tăng nồng độ), methotrexate (tăng độc tính), ACE inhibitor/ARB (tăng kali)",
        "Thận trọng ở bệnh nhân suy gan (chuyển hóa qua gan)",
        "Dùng với thức ăn để giảm kích ứng dạ dày"
    ],
    "pharmacokinetics": {
        "half_life": "8-10 giờ (TMP), 10-12 giờ (SMX)",
        "onset": "2-4 giờ",
        "duration": "q12h (PO), q6-8h (IV cho PJP)",
        "protein_binding": "44% (TMP), 70% (SMX)",
        "clearance": "Gan: chuyển hóa một phần. Thận: bài tiết chủ yếu qua thận (TMP và SMX). Cần điều chỉnh liều ở suy thận (CrCl <30: giảm 50%, CrCl <15: tránh dùng)."
    },
    "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm, tránh ánh sáng. Viên nén: bảo quản trong bao bì kín. Dạng suspension: bảo quản ở nhiệt độ phòng, lắc kỹ trước khi dùng. IV: bảo quản trong tủ lạnh, để nhiệt độ phòng trước khi pha, dùng trong vòng 6 giờ sau khi pha.",
    "black_box_warnings": "Nguy cơ phản ứng dị ứng nghiêm trọng, bao gồm SJS/TEN, có thể gây tử vong. Nguy cơ tăng ở bệnh nhân có tiền sử dị ứng sulfonamide. Ngừng ngay nếu có phát ban, sốt, mụn nước, bong da.",
    "drug_interactions": {
        "major": [
            {
                "drug": "Warfarin",
                "mechanism": "Trimethoprim-sulfamethoxazole ức chế CYP2C9, làm giảm chuyển hóa warfarin. Sulfamethoxazole cũng có thể ức chế tổng hợp vitamin K.",
                "effect": "Tăng tác dụng chống đông, tăng INR, tăng nguy cơ chảy máu nghiêm trọng",
                "management": "Theo dõi INR chặt chẽ khi bắt đầu, thay đổi liều, hoặc ngừng trimethoprim-sulfamethoxazole. Giảm liều warfarin 25-50% khi bắt đầu trimethoprim-sulfamethoxazole. Điều chỉnh liều warfarin theo INR."
            },
            {
                "drug": "Phenytoin",
                "mechanism": "Trimethoprim-sulfamethoxazole ức chế CYP2C9, làm giảm chuyển hóa phenytoin.",
                "effect": "Tăng nồng độ phenytoin, tăng độc tính (chóng mặt, rung giật, ataxia, co giật)",
                "management": "Theo dõi nồng độ phenytoin. Giảm liều phenytoin khi bắt đầu trimethoprim-sulfamethoxazole. Theo dõi dấu hiệu độc tính phenytoin."
            },
            {
                "drug": "Methotrexate",
                "mechanism": "Trimethoprim-sulfamethoxazole ức chế tổng hợp folate, làm tăng độc tính methotrexate. Cũng ức chế bài tiết methotrexate ở ống thận.",
                "effect": "Tăng nồng độ methotrexate, tăng độc tính nghiêm trọng (giảm bạch cầu, thiếu máu, độc gan, độc thận, tử vong)",
                "management": "TRÁNH DÙNG đồng thời nếu có thể. Nếu bắt buộc, giảm liều methotrexate đáng kể, bổ sung folinic acid (leucovorin), theo dõi chặt chẽ công thức máu, chức năng gan, thận. Ngừng methotrexate nếu có dấu hiệu độc tính."
            }
        ],
        "moderate": [
            {
                "drug": "ACE inhibitor, ARB",
                "mechanism": "Trimethoprim ức chế bài tiết kali ở ống thận, làm tăng kali máu. ACE inhibitor/ARB cũng tăng kali máu.",
                "effect": "Tăng kali máu, tăng nguy cơ rối loạn nhịp tim, đặc biệt ở người cao tuổi, suy thận",
                "management": "Theo dõi kali máu chặt chẽ, đặc biệt ở người cao tuổi, suy thận. Giảm liều hoặc ngừng ACE inhibitor/ARB nếu kali tăng. Điều chỉnh liều trimethoprim-sulfamethoxazole nếu cần."
            },
            {
                "drug": "Digoxin",
                "mechanism": "Trimethoprim-sulfamethoxazole có thể ảnh hưởng đến hệ vi khuẩn đường ruột, làm tăng hấp thu digoxin.",
                "effect": "Tăng nồng độ digoxin, tăng độc tính (buồn nôn, nôn, rối loạn nhịp tim, block AV)",
                "management": "Theo dõi nồng độ digoxin và dấu hiệu độc tính. Giảm liều digoxin nếu cần. Theo dõi ECG."
            },
            {
                "drug": "Sulfonylurea (Glibenclamide, Gliclazide)",
                "mechanism": "Trimethoprim-sulfamethoxazole ức chế CYP2C9, làm giảm chuyển hóa sulfonylurea.",
                "effect": "Tăng nồng độ sulfonylurea, tăng nguy cơ hạ đường huyết",
                "management": "Theo dõi đường huyết chặt chẽ. Giảm liều sulfonylurea khi bắt đầu trimethoprim-sulfamethoxazole. Điều chỉnh liều theo đường huyết."
            }
        ],
        "minor": [
            {
                "drug": "Cyclosporine",
                "mechanism": "Trimethoprim-sulfamethoxazole có thể ảnh hưởng đến chuyển hóa cyclosporine.",
                "effect": "Tăng nhẹ nồng độ cyclosporine",
                "management": "Theo dõi nồng độ cyclosporine. Không cần điều chỉnh liều thường quy."
            }
        ]
    },
    "contraindications": {
        "tuyệt_đối": [
            "Dị ứng trimethoprim, sulfamethoxazole, hoặc các sulfonamide khác - phản ứng chéo cao",
            "Suy thận nặng (CrCl <15) - tăng nguy cơ tác dụng phụ, không hiệu quả",
            "Suy gan nặng - tăng nguy cơ độc tính",
            "Thiếu máu do thiếu folate - tăng nguy cơ thiếu máu nặng, giảm bạch cầu",
            "Có thai (gần sinh, 3 tháng cuối) - nguy cơ kernicterus ở trẻ sơ sinh",
            "Tiền sử SJS/TEN do sulfonamide - nguy cơ tái phát cao, có thể tử vong"
        ],
        "tương_đối": [
            "Dị ứng sulfonamide nhẹ - thận trọng, có thể dùng nếu cần thiết nhưng theo dõi chặt chẽ",
            "Suy thận (CrCl 15-30) - cần giảm liều 50%, theo dõi chặt chẽ",
            "Suy gan - thận trọng, có thể giảm chuyển hóa",
            "Thiếu folate - bổ sung folate trước và trong khi dùng",
            "Người cao tuổi - tăng nguy cơ tăng kali máu, tác dụng phụ",
            "Dùng với ACE inhibitor/ARB - tăng nguy cơ tăng kali máu",
            "Dùng với warfarin - tăng nguy cơ chảy máu",
            "Dùng với phenytoin - tăng độc tính phenytoin",
            "Dùng với methotrexate - tăng độc tính methotrexate nghiêm trọng",
            "Có thai (tam cá nguyệt 1-2) - thận trọng, chỉ dùng khi thực sự cần thiết"
        ]
    },
    "contraindications_detail": {
        "tuyệt_đối": [
            "Dị ứng trimethoprim, sulfamethoxazole, hoặc các sulfonamide khác - phản ứng chéo cao",
            "Suy thận nặng (CrCl <15) - tăng nguy cơ tác dụng phụ, không hiệu quả",
            "Suy gan nặng - tăng nguy cơ độc tính",
            "Thiếu máu do thiếu folate - tăng nguy cơ thiếu máu nặng, giảm bạch cầu",
            "Có thai (gần sinh, 3 tháng cuối) - nguy cơ kernicterus ở trẻ sơ sinh",
            "Tiền sử SJS/TEN do sulfonamide - nguy cơ tái phát cao, có thể tử vong"
        ],
        "tương_đối": [
            "Dị ứng sulfonamide nhẹ - thận trọng, có thể dùng nếu cần thiết nhưng theo dõi chặt chẽ",
            "Suy thận (CrCl 15-30) - cần giảm liều 50%, theo dõi chặt chẽ",
            "Suy gan - thận trọng, có thể giảm chuyển hóa",
            "Thiếu folate - bổ sung folate trước và trong khi dùng",
            "Người cao tuổi - tăng nguy cơ tăng kali máu, tác dụng phụ",
            "Dùng với ACE inhibitor/ARB - tăng nguy cơ tăng kali máu",
            "Dùng với warfarin - tăng nguy cơ chảy máu",
            "Dùng với phenytoin - tăng độc tính phenytoin",
            "Dùng với methotrexate - tăng độc tính methotrexate nghiêm trọng",
            "Có thai (tam cá nguyệt 1-2) - thận trọng, chỉ dùng khi thực sự cần thiết"
        ]
    },
    "pregnancy_lactation": {
        "fda_category": "C (tam cá nguyệt 1-2), D (tam cá nguyệt 3)",
        "pregnancy_details": "Tam cá nguyệt 1-2: Thuốc phân loại C - thận trọng. Các nghiên cứu trên động vật cho thấy một số nguy cơ. Các nghiên cứu trên người không cho thấy nguy cơ tăng dị tật bẩm sinh rõ ràng, nhưng dữ liệu còn hạn chế. Có thể dùng khi lợi ích vượt quá nguy cơ, đặc biệt trong điều trị PJP hoặc nhiễm trùng nặng. Tam cá nguyệt 3 (gần sinh): Thuốc phân loại D - CHỐNG CHỈ ĐỊNH. Sulfamethoxazole có thể gây kernicterus ở trẻ sơ sinh (vàng da nặng, tổn thương não). Không dùng trong 3 tháng cuối thai kỳ. Nếu cần điều trị, dùng thuốc khác hoặc trì hoãn đến sau sinh.",
        "lactation": {
            "safety": "Compatible with Caution",
            "details": "Trimethoprim và sulfamethoxazole bài tiết vào sữa mẹ ở nồng độ thấp. Nồng độ trong sữa mẹ thấp và không có báo cáo về tác dụng phụ đáng kể ở trẻ bú mẹ. Tuy nhiên, sulfonamide có thể gây vàng da ở trẻ sơ sinh thiếu tháng hoặc có bệnh gan. Thận trọng ở trẻ sơ sinh < 1 tháng tuổi hoặc thiếu tháng.",
            "recommendation": "Có thể dùng khi cho con bú, nhưng thận trọng ở trẻ sơ sinh < 1 tháng tuổi hoặc thiếu tháng. Dùng liều thấp nhất hiệu quả. Theo dõi trẻ sơ sinh nếu dùng liều cao hoặc kéo dài (vàng da, tiêu chảy, phát ban)."
        }
    },
    "hepatic_adjustment": {
        "mild": "Không cần điều chỉnh liều. Trimethoprim và sulfamethoxazole chuyển hóa một phần qua gan nhưng không đáng kể.",
        "moderate": "Thận trọng, có thể cần giảm liều nhẹ. Chuyển hóa có thể giảm ở suy gan trung bình, tăng nồng độ và nguy cơ tác dụng phụ.",
        "severe": "CHỐNG CHỈ ĐỊNH hoặc thận trọng tối đa. Chuyển hóa có thể giảm đáng kể ở suy gan nặng, tăng nồng độ và nguy cơ độc tính gan nghiêm trọng. Không dùng nếu suy gan nặng.",
        "notes": "Trimethoprim và sulfamethoxazole chuyển hóa một phần qua gan nhưng thải trừ chủ yếu qua thận. Suy gan có thể giảm chuyển hóa, tăng nồng độ và nguy cơ độc tính gan. Tuy nhiên, suy gan nặng là chống chỉ định do nguy cơ độc tính gan nghiêm trọng. Theo dõi chặt chẽ chức năng gan ở suy gan trung bình."
    },
    "overdose_management": {
        "symptoms": [
            "Triệu chứng tiêu hóa: Buồn nôn, nôn, tiêu chảy, đau bụng",
            "Triệu chứng thần kinh: Đau đầu, chóng mặt, lú lẫn, co giật (hiếm)",
            "Triệu chứng huyết học: Thiếu máu, giảm bạch cầu, giảm tiểu cầu (do thiếu folate)",
            "Triệu chứng thận: Tăng creatinine (giả), suy thận cấp (hiếm)",
            "Triệu chứng điện giải: Tăng kali máu (đặc biệt với trimethoprim)",
            "Triệu chứng da: Phát ban, mày đay, SJS/TEN (hiếm nhưng nghiêm trọng, có thể tử vong)",
            "Triệu chứng gan: Tăng men gan, viêm gan (hiếm nhưng nghiêm trọng)",
            "Triệu chứng nghiêm trọng: SJS/TEN, suy thận cấp, viêm gan nặng, thiếu máu nặng"
        ],
        "antidote": "Không có antidote đặc hiệu. Điều trị hỗ trợ và điều trị triệu chứng. Bổ sung folinic acid (leucovorin) nếu có thiếu máu do thiếu folate.",
        "treatment": [
            "Ngừng ngay trimethoprim-sulfamethoxazole",
            "Rửa dạ dày hoặc than hoạt nếu uống trong vòng 1-2 giờ (nếu không có chống chỉ định)",
            "Theo dõi dấu hiệu sinh tồn: Huyết áp, nhịp tim, nhịp thở, SpO2",
            "Điều trị triệu chứng tiêu hóa:",
            "  - Chống nôn nếu cần",
            "  - Truyền dịch nếu mất nước",
            "  - Theo dõi điện giải",
            "Điều trị tăng kali máu nếu có:",
            "  - Theo dõi kali máu",
            "  - Điều trị tăng kali máu: Calcium gluconate, insulin + glucose, sodium bicarbonate, kayexalate",
            "  - Lọc máu nếu cần",
            "Điều trị thiếu máu/giảm bạch cầu nếu có:",
            "  - Bổ sung folinic acid (leucovorin) 5-15mg/ngày",
            "  - Theo dõi công thức máu",
            "  - Truyền máu nếu cần",
            "Điều trị tăng creatinine (giả) nếu có:",
            "  - Theo dõi creatinine, BUN, lượng nước tiểu",
            "  - Điều trị suy thận cấp nếu có",
            "Điều trị SJS/TEN nếu có:",
            "  - CHUYỂN NGAY khoa da liễu/bỏng",
            "  - Điều trị hỗ trợ (truyền dịch, dinh dưỡng, chăm sóc vết thương)",
            "  - Kháng sinh nếu có nhiễm trùng",
            "  - Corticosteroid (còn tranh cãi)",
            "Điều trị tăng men gan/viêm gan nếu có:",
            "  - Theo dõi ALT, AST, bilirubin",
            "  - Điều trị hỗ trợ gan",
            "  - Nếu viêm gan nặng: điều trị suy gan",
            "Theo dõi dấu hiệu sinh tồn: Huyết áp, nhịp tim, nhịp thở, SpO2"
        ],
        "monitoring": "Theo dõi dấu hiệu sinh tồn, công thức máu (CBC), điện giải (natri, kali), chức năng thận (creatinine, BUN, lượng nước tiểu), chức năng gan (ALT, AST, bilirubin), dấu hiệu da (SJS/TEN) trong ít nhất 24-48 giờ. Theo dõi lâu hơn nếu có biến chứng (SJS/TEN, suy thận, viêm gan, thiếu máu)."
    },
    "reversal_agents": {"available": False, "agents": [], "notes": "Không có antidote đặc hiệu. Điều trị chủ yếu là hỗ trợ và điều trị triệu chứng. Ngừng thuốc ngay nếu có SJS/TEN hoặc phản ứng dị ứng nghiêm trọng. Hydration đầy đủ để tăng thải trừ."},
    "administration_instructions": {
        "oral": {
            "with_food": "Uống với thức ăn để giảm kích ứng dạ dày. Có thể uống không thức ăn nếu cần nhưng không khuyến nghị.",
            "timing": "Uống 2 lần/ngày (q12h) cho UTI, 3-4 lần/ngày (q6-8h) cho PJP. Uống đều đặn, cách đều nhau trong ngày. Không bỏ liều. Uống nhiều nước để tránh kết tinh trong nước tiểu."
        },
        "iv": {
            "reconstitution": "Pha theo hướng dẫn nhà sản xuất. Thường pha với D5W hoặc NaCl 0.9%. Lắc kỹ để hòa tan hoàn toàn. Dùng trong vòng 6 giờ sau khi pha.",
            "infusion_rate": "Truyền IV trong 60-90 phút (không truyền nhanh hơn). Có thể truyền trong 30-60 phút nếu cần nhưng không khuyến nghị.",
            "compatibility": [
                "D5W (Dextrose 5%)",
                "NaCl 0.9%",
                "Nước cất vô trùng"
            ],
            "incompatibility": [
                "Không trộn với các thuốc khác trong cùng một bơm tiêm hoặc chai truyền",
                "Lactated Ringer's (LR) - không tương thích",
                "Các dung dịch có cation (Al3+, Mg2+, Ca2+) - có thể tạo phức hợp"
            ],
            "notes": "Truyền IV trong 60-90 phút. Không truyền nhanh hơn. Theo dõi phản ứng tại chỗ tiêm (viêm tĩnh mạch). Dùng trong vòng 6 giờ sau khi pha. Không bảo quản lâu sau khi pha."
        }
    },
    "references": {
        "primary_sources": [
            "FDA Label: Bactrim, Septra (trimethoprim-sulfamethoxazole)",
            "UpToDate: Trimethoprim-sulfamethoxazole drug information",
            "Lexicomp: Trimethoprim-sulfamethoxazole monograph",
            "Goodman & Gilman's The Pharmacological Basis of Therapeutics",
            "Sanford Guide to Antimicrobial Therapy"
        ],
        "last_updated": "2025-02-18",
        "evidence_level": "Level 1 - FDA approved, multiple clinical trials, extensive clinical experience"
    },
    "risk_flags": {
        "high_alert": True,
        "narrow_therapeutic_index": False,
        "icu_critical_care_only": False,
        "bleeding_risk": "Low",
        "organ_toxicity": {"dermatologic": "High (SJS/TEN)", "renal": "Moderate", "hematologic": "Moderate", "metabolic": "Moderate (hyperkalemia)"}
    },
    "guideline_tags": [
        "IDSA Guidelines - Complicated Urinary Tract Infections",
        "IDSA Guidelines - Pneumocystis jirovecii Pneumonia",
        "IDSA Guidelines - Toxoplasma gondii Infection",
        "IDSA Guidelines - Methicillin-Resistant Staphylococcus aureus Infections",
        "CDC Guidelines - Opportunistic Infections in HIV",
        "WHO Essential Medicines List"
    ],
    "last_updated": "2025-02-18",
    },
}

__all__ = ['SULFONAMIDE_ANTIBIOTICS']
