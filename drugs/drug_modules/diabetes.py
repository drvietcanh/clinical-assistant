"""
Diabetes Medications
Active module - contains all diabetes drug data
"""

DIABETES_DRUGS = {
"Metformin": {
        "group": "Diabetes - Biguanide",
        "vietnamese_name": "Metformin, Glucophage",
        "administration": ["PO"],
        "indications": [
            "Đái tháo đường type 2",
            "Hội chứng buồng trứng đa nang (PCOS)",
            "Dự phòng đái tháo đường"
        ],
        "contraindications": [
            "Suy thận (CrCl <30 hoặc eGFR <30)",
            "Toan chuyển hóa",
            "Nhiễm toan lactic",
            "Suy gan nặng",
            "Suy tim nặng",
            "Dùng thuốc cản quang (tạm ngừng)"
        ],
        "dosage": {
            "adult_start": "500mg x 2 lần/ngày với bữa ăn",
            "adult_usual": "500-1000mg x 2-3 lần/ngày",
            "adult_max": "1000mg x 2 lần/ngày (2000mg/ngày)",
            "extended_release": "500-2000mg x 1 lần/ngày với bữa ăn tối",
            "notes": "Khởi đầu với liều thấp, tăng dần. Tạm ngừng khi dùng thuốc cản quang"
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "Thận trọng, giảm liều",
            "under_30": "Chống chỉ định"
        },
        "side_effects": [
            "Buồn nôn, nôn",
            "Tiêu chảy",
            "Đau bụng",
            "Nhiễm toan lactic (hiếm nhưng nguy hiểm)",
            "Hạ đường huyết (ít khi)",
            "Thiếu vitamin B12 (dùng lâu dài)"
        ],
        "interactions": [
            "Thuốc cản quang: tăng nguy cơ nhiễm toan lactic - ngừng 48h trước và sau",
            "Rượu: tăng nguy cơ nhiễm toan lactic",
            "Furosemide: có thể tăng nồng độ metformin"
        ],
        "pregnancy": "B",
        "mechanism_of_action": "Ức chế sản xuất glucose ở gan, tăng nhạy cảm với insulin ở mô ngoại vi, giảm hấp thu glucose ở ruột",
        "monitoring": [
            "HbA1c mỗi 3 tháng",
            "Đường huyết đói và sau ăn",
            "Creatinine, eGFR mỗi 3-6 tháng",
            "Vitamin B12 mỗi 1-2 năm",
            "Lactate nếu nghi ngờ nhiễm toan lactic (đau cơ, khó thở, đau bụng)"
        ],
        "precautions": [
            "Ngừng 48h trước và sau khi dùng thuốc cản quang",
            "Theo dõi nhiễm toan lactic ở bệnh nhân suy tim, suy gan, suy thận",
            "Bổ sung vitamin B12 nếu dùng lâu dài",
            "Tránh rượu (tăng nguy cơ nhiễm toan lactic)"
        ],
        "pharmacokinetics": {
            "half_life": "6.2 giờ",
            "onset": "1-2 giờ",
            "duration": "10-12 giờ",
            "protein_binding": "Minimal",
            "clearance": "Thận (chủ yếu)"
        },
        "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm",
        "black_box_warnings": "Nhiễm toan lactic - có thể tử vong. Nguy cơ cao ở suy thận, suy tim, suy gan, nhiễm trùng nặng",
        "drug_interactions": {
            "major": [
                {
                    "drug": "Thuốc cản quang (iodinated contrast media)",
                    "mechanism": "Tăng nguy cơ nhiễm toan lactic do suy thận cấp",
                    "effect": "Nguy cơ nhiễm toan lactic, suy thận cấp, tử vong",
                    "management": "NGỪNG METFORMIN 48 GIỜ TRƯỚC và 48 GIỜ SAU khi dùng thuốc cản quang. Đánh giá chức năng thận trước khi dùng lại."
                },
                {
                    "drug": "Rượu (ethanol)",
                    "mechanism": "Tăng sản xuất lactate, giảm chuyển hóa lactate",
                    "effect": "Tăng nguy cơ nhiễm toan lactic",
                    "management": "TRÁNH RƯỢU hoàn toàn khi dùng metformin. Cảnh báo bệnh nhân về nguy cơ."
                }
            ],
            "moderate": [
                {
                    "drug": "Furosemide",
                    "mechanism": "Có thể tăng nồng độ metformin, tăng nguy cơ nhiễm toan lactic",
                    "effect": "Tăng nguy cơ nhiễm toan lactic",
                    "management": "Thận trọng. Theo dõi chức năng thận, lactate. Có thể cần giảm liều metformin."
                },
                {
                    "drug": "Cimetidine",
                    "mechanism": "Giảm thải trừ metformin qua thận",
                    "effect": "Tăng nồng độ metformin, tăng nguy cơ độc tính",
                    "management": "Thận trọng. Theo dõi lactate. Có thể cần giảm liều metformin."
                }
            ],
            "minor": [
                {
                    "drug": "Warfarin",
                    "mechanism": "Metformin có thể tăng nhẹ tác dụng chống đông",
                    "effect": "Tăng nhẹ INR",
                    "management": "Theo dõi INR. Điều chỉnh liều warfarin nếu cần."
                }
            ]
        },
        "contraindications": {
            "absolute": [
                "Suy thận nặng (CrCl <30 hoặc eGFR <30)",
                "Nhiễm toan lactic",
                "Suy gan nặng",
                "Suy tim nặng (NYHA class III-IV)",
                "Dùng thuốc cản quang (tạm ngừng 48h trước và sau)",
                "Nhiễm trùng nặng (tăng nguy cơ nhiễm toan lactic)",
                "Dị ứng metformin"
            ],
            "relative": [
                "Suy thận trung bình (CrCl 30-60) - giảm liều, theo dõi sát",
                "Suy gan nhẹ đến trung bình - thận trọng",
                "Suy tim nhẹ đến trung bình - thận trọng",
                "Người cao tuổi - tăng nguy cơ nhiễm toan lactic",
                "Uống rượu - tăng nguy cơ nhiễm toan lactic",
                "Phẫu thuật lớn - tạm ngừng trước và sau phẫu thuật"
            ]
        },
        "pregnancy_lactation": {
            "fda_category": "B",
            "pregnancy_details": "Không có bằng chứng về nguy cơ gây dị tật thai nhi ở động vật. Có thể dùng trong thai kỳ nếu lợi ích > nguy cơ. Được sử dụng rộng rãi trong thai kỳ, đặc biệt ở bệnh nhân đái tháo đường thai kỳ và PCOS. Theo dõi đường huyết chặt chẽ trong thai kỳ. Có thể dùng với insulin.",
            "lactation": {
                "safety": "Compatible",
                "details": "Metformin bài tiết vào sữa mẹ ở nồng độ thấp. Nồng độ trong máu trẻ bú mẹ thường rất thấp. Không có báo cáo về tác dụng phụ nghiêm trọng ở trẻ bú mẹ.",
                "recommendation": "Có thể dùng khi cho con bú. An toàn và được khuyến nghị trong thời kỳ cho con bú. Theo dõi trẻ nếu có dấu hiệu bất thường."
            }
        },
        "hepatic_adjustment": {
            "mild": "Thận trọng",
            "moderate": "Thận trọng, có thể cần giảm liều",
            "severe": "CHỐNG CHỈ ĐỊNH",
            "notes": "Metformin chuyển hóa một phần ở gan. Suy gan làm giảm chuyển hóa lactate, tăng nguy cơ nhiễm toan lactic. Không dùng ở suy gan nặng. Thận trọng ở suy gan nhẹ đến trung bình."
        },
        "overdose_management": {
            "symptoms": [
                "Buồn nôn, nôn, tiêu chảy",
                "Đau bụng",
                "Nhiễm toan lactic (pH <7.35, lactate >5 mmol/L) - nguy hiểm",
                "Hạ đường huyết (hiếm)",
                "Suy thận cấp",
                "Hôn mê, tử vong (nếu nhiễm toan lactic nặng)"
            ],
            "antidote": "Không có antidote đặc hiệu. Điều trị hỗ trợ và lọc máu",
            "treatment": [
                "Rửa dạ dày nếu uống trong vòng 1-2 giờ",
                "Than hoạt tính (hiệu quả hạn chế)",
                "Điều trị nhiễm toan lactic: Bicarbonate IV, lọc máu (hemodialysis) để loại bỏ metformin",
                "Hỗ trợ hô hấp và tuần hoàn",
                "Theo dõi lactate, pH máu, điện giải, chức năng thận",
                "Lọc máu nếu lactate >5 mmol/L hoặc nhiễm toan lactic nặng",
                "Điều trị hạ đường huyết nếu có: Glucose IV",
                "Theo dõi ít nhất 24-48 giờ"
            ],
            "monitoring": "Lactate máu, pH máu, điện giải, chức năng thận, glucose máu, dấu hiệu sống, ý thức"
        },
        "reversal_agents": {
            "available": False,
            "agents": []
        },
        "administration_instructions": {
            "oral": {
                "with_food": "Uống với bữa ăn để giảm buồn nôn, tiêu chảy. Có thể giảm tác dụng phụ đường tiêu hóa.",
                "timing": "Uống 2-3 lần/ngày với bữa ăn. Dạng extended-release: 1 lần/ngày với bữa ăn tối. Khởi đầu với liều thấp (500mg x 2 lần/ngày), tăng dần để giảm tác dụng phụ."
            },
            "iv": {
                "reconstitution": "Không có dạng IV",
                "infusion_rate": "N/A",
                "compatibility": [],
                "incompatibility": [],
                "notes": "Chỉ có dạng uống"
            }
        },
        "references": {
            "primary_sources": [
                "FDA Drug Label - Glucophage (metformin)",
                "UpToDate - Metformin: Drug information",
                "UK Prospective Diabetes Study (UKPDS)",
                "American Diabetes Association guidelines",
                "Goodman & Gilman's The Pharmacological Basis of Therapeutics"
            ],
            "last_updated": "2024-12-19",
            "evidence_level": "High - Multiple large RCTs (UKPDS) and extensive clinical experience"
        }
    },
    "Glibenclamide": {
        "group": "Diabetes - Sulfonylurea",
        "vietnamese_name": "Glibenclamide, Daonil",
        "administration": ["PO"],
        "indications": [
            "Đái tháo đường type 2"
        ],
        "contraindications": [
            "Đái tháo đường type 1",
            "Nhiễm toan ceton do đái tháo đường",
            "Suy thận nặng",
            "Suy gan nặng",
            "Có thai"
        ],
        "dosage": {
            "adult_start": "2.5-5mg x 1 lần/ngày trước bữa sáng",
            "adult_usual": "5-15mg/ngày chia 1-2 lần",
            "adult_max": "20mg/ngày",
            "notes": "Nguy cơ hạ đường huyết cao, đặc biệt ở người già, suy thận"
        },
        "side_effects": [
            "Hạ đường huyết (thường gặp, có thể nặng)",
            "Tăng cân",
            "Ban da",
            "Rối loạn tiêu hóa"
        ],
        "interactions": [
            "Warfarin: có thể tăng tác dụng chống đông",
            "Rượu: tăng nguy cơ hạ đường huyết",
            "Beta-blocker: che dấu triệu chứng hạ đường huyết"
        ],
        "pregnancy": "C - Tránh dùng trong thai kỳ",
        "mechanism_of_action": "Glibenclamide (glyburide) là thuốc sulfonylurea thế hệ thứ hai, kích thích tế bào beta tuyến tụy tiết insulin. Glibenclamide gắn vào SUR1 (sulfonylurea receptor 1) trên kênh KATP (ATP-sensitive K+ channel) ở màng tế bào beta, làm đóng kênh KATP. Điều này ngăn chặn dòng kali ra ngoài, làm khử cực màng tế bào (depolarization), mở kênh canxi phụ thuộc điện thế, tăng dòng canxi vào tế bào, và kích thích giải phóng insulin từ các hạt tiết. Glibenclamide chỉ hoạt động khi còn chức năng tế bào beta (cần có insulin nội sinh). Glibenclamide có tác dụng mạnh và thời gian bán thải dài, dẫn đến nguy cơ hạ đường huyết cao hơn các sulfonylurea khác, đặc biệt ở người cao tuổi và suy thận. Glibenclamide cũng có thể làm giảm đề kháng insulin ngoại vi và giảm sản xuất glucose ở gan.",
        "monitoring": [
            "Đường huyết: HbA1c (mỗi 3 tháng), đường huyết đói, đường huyết sau ăn - đánh giá hiệu quả",
            "Dấu hiệu hạ đường huyết: run, vã mồ hôi, nhịp tim nhanh, đói, lú lẫn, co giật, hôn mê - QUAN TRỌNG",
            "Đường huyết khi nghi ngờ hạ đường huyết - đo ngay",
            "Cân nặng - sulfonylureas có thể gây tăng cân",
            "Chức năng thận (creatinine, eGFR) - suy thận tăng nguy cơ hạ đường huyết (tăng thời gian bán thải)",
            "Chức năng gan (ALT, AST) - nếu có bệnh gan (tăng nguy cơ hạ đường huyết)",
            "Tương tác với warfarin (tăng INR), rượu (tăng nguy cơ hạ đường huyết), beta-blocker (che dấu triệu chứng hạ đường huyết)"
        ],
        "precautions": [
            "Hạ đường huyết là tác dụng phụ phổ biến nhất và nghiêm trọng - bệnh nhân cần biết dấu hiệu và cách xử trí (uống nước đường, nước ngọt, hoặc glucose)",
            "Nguy cơ hạ đường huyết cao hơn các sulfonylurea khác do thời gian bán thải dài",
            "Nguy cơ tăng ở: người cao tuổi, suy thận, suy gan, bỏ bữa, uống rượu, tập luyện quá mức",
            "KHÔNG dùng ở đái tháo đường type 1 hoặc nhiễm toan ceton (không có insulin nội sinh)",
            "Thận trọng ở bệnh nhân suy thận - tăng nguy cơ hạ đường huyết (có thể cần giảm liều hoặc tránh dùng)",
            "Thận trọng ở bệnh nhân suy gan - tăng nguy cơ hạ đường huyết",
            "Uống với thức ăn hoặc trước bữa ăn để tránh hạ đường huyết",
            "Tránh bỏ bữa - tăng nguy cơ hạ đường huyết",
            "Tránh rượu - tăng nguy cơ hạ đường huyết (có thể gây hạ đường huyết kéo dài)",
            "Beta-blocker có thể che dấu triệu chứng hạ đường huyết (nhịp tim nhanh, run) - chỉ còn vã mồ hôi, lú lẫn",
            "Có thể tăng cân - cần tư vấn chế độ ăn và tập luyện",
            "Không dùng trong thai kỳ (có thể gây hạ đường huyết ở trẻ sơ sinh)",
            "Bắt đầu với liều thấp (2.5-5mg/ngày) và tăng dần"
        ],
        "pharmacokinetics": {
            "half_life": "10 giờ (bình thường), tăng ở suy thận",
            "onset": "2-4 giờ",
            "duration": "16-24 giờ (dùng 1-2 lần/ngày)",
            "protein_binding": "99% (gắn chặt với albumin)",
            "clearance": "Gan: chuyển hóa qua CYP2C9 và CYP3A4 thành metabolites không hoạt động. Thận: bài tiết một phần nguyên dạng và metabolites. Thời gian bán thải tăng ở suy thận (tăng nguy cơ hạ đường huyết)."
        },
        "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm, tránh ánh sáng. Viên nén: bảo quản trong bao bì kín.",
        "black_box_warnings": "Nguy cơ hạ đường huyết nghiêm trọng, có thể gây tử vong. Nguy cơ tăng ở người cao tuổi, suy thận, suy gan, bỏ bữa, uống rượu. Bệnh nhân cần biết dấu hiệu và cách xử trí hạ đường huyết. Không dùng ở đái tháo đường type 1 hoặc nhiễm toan ceton.",
        "drug_interactions": {
            "major": [
                {
                    "drug": "Rượu (ethanol)",
                    "mechanism": "Ức chế sản xuất glucose ở gan, tăng nguy cơ hạ đường huyết",
                    "effect": "Hạ đường huyết nghiêm trọng, có thể kéo dài",
                    "management": "TRÁNH RƯỢU hoàn toàn khi dùng glibenclamide. Cảnh báo bệnh nhân về nguy cơ."
                },
                {
                    "drug": "Beta-blockers (propranolol, metoprolol)",
                    "mechanism": "Che dấu triệu chứng hạ đường huyết (nhịp tim nhanh, run)",
                    "effect": "Khó nhận biết hạ đường huyết, tăng nguy cơ hạ đường huyết nặng",
                    "management": "Thận trọng. Theo dõi đường huyết chặt chẽ. Bệnh nhân cần biết các triệu chứng hạ đường huyết không bị che dấu (vã mồ hôi, lú lẫn)."
                }
            ],
            "moderate": [
                {
                    "drug": "Warfarin",
                    "mechanism": "Glibenclamide có thể tăng tác dụng chống đông",
                    "effect": "Tăng INR, tăng nguy cơ chảy máu",
                    "management": "Theo dõi INR thường xuyên. Điều chỉnh liều warfarin nếu cần."
                },
                {
                    "drug": "CYP2C9 inhibitors (fluconazole, amiodarone)",
                    "mechanism": "Ức chế chuyển hóa glibenclamide, tăng nồng độ",
                    "effect": "Tăng nguy cơ hạ đường huyết",
                    "management": "Thận trọng. Theo dõi đường huyết. Có thể cần giảm liều glibenclamide."
                },
                {
                    "drug": "Salicylates (aspirin liều cao)",
                    "mechanism": "Tăng tác dụng giảm đường huyết",
                    "effect": "Tăng nguy cơ hạ đường huyết",
                    "management": "Thận trọng. Theo dõi đường huyết."
                }
            ],
            "minor": [
                {
                    "drug": "Chloramphenicol",
                    "mechanism": "Tăng nồng độ glibenclamide",
                    "effect": "Tăng nguy cơ hạ đường huyết",
                    "management": "Thận trọng. Theo dõi đường huyết."
                }
            ]
        },
        "contraindications": {
            "absolute": [
                "Đái tháo đường type 1",
                "Nhiễm toan ceton do đái tháo đường",
                "Dị ứng glibenclamide hoặc sulfonylurea",
                "Suy thận nặng (CrCl <30) - tăng nguy cơ hạ đường huyết nghiêm trọng"
            ],
            "relative": [
                "Suy gan nặng - tăng nguy cơ hạ đường huyết",
                "Người cao tuổi - tăng nguy cơ hạ đường huyết",
                "Suy thận trung bình (CrCl 30-60) - giảm liều, theo dõi sát",
                "Có thai - có thể gây hạ đường huyết ở trẻ sơ sinh",
                "Bỏ bữa thường xuyên - tăng nguy cơ hạ đường huyết",
                "Uống rượu - tăng nguy cơ hạ đường huyết nghiêm trọng",
                "Dùng beta-blocker - che dấu triệu chứng hạ đường huyết"
            ]
        },
        "pregnancy_lactation": {
            "fda_category": "C",
            "pregnancy_details": "Có thể dùng trong thai kỳ nếu lợi ích > nguy cơ, nhưng THƯỜNG TRÁNH DÙNG. Sulfonylureas có thể gây hạ đường huyết ở trẻ sơ sinh. Insulin là lựa chọn ưu tiên trong thai kỳ. Nếu dùng, theo dõi đường huyết chặt chẽ và ngừng trước khi sinh để tránh hạ đường huyết ở trẻ sơ sinh.",
            "lactation": {
                "safety": "Compatible",
                "details": "Glibenclamide bài tiết vào sữa mẹ ở nồng độ thấp. Ít có nguy cơ gây hạ đường huyết ở trẻ bú mẹ do nồng độ thấp.",
                "recommendation": "Có thể dùng khi cho con bú với theo dõi chặt chẽ. Theo dõi dấu hiệu hạ đường huyết ở trẻ (quấy khóc, bú kém, vã mồ hôi)."
            }
        },
        "hepatic_adjustment": {
            "mild": "Thận trọng, giảm liều nhẹ",
            "moderate": "Giảm liều 25-50%. Theo dõi chức năng gan và đường huyết",
            "severe": "CHỐNG CHỈ ĐỊNH",
            "notes": "Glibenclamide chuyển hóa ở gan qua CYP2C9 và CYP3A4. Suy gan làm giảm chuyển hóa, tăng nồng độ, tăng nguy cơ hạ đường huyết nghiêm trọng. Không dùng ở suy gan nặng."
        },
        "overdose_management": {
            "symptoms": [
                "Hạ đường huyết: run, vã mồ hôi, nhịp tim nhanh, đói, lú lẫn, co giật, hôn mê",
                "Hạ đường huyết có thể kéo dài (do thời gian bán thải dài)",
                "Hạ đường huyết nghiêm trọng có thể gây tử vong hoặc tổn thương não vĩnh viễn"
            ],
            "antidote": "Glucose (đường uống hoặc IV)",
            "treatment": [
                "Nếu tỉnh táo: Glucose 15-20g PO (nước đường, nước ngọt, kẹo)",
                "Nếu hôn mê hoặc không thể uống: Dextrose 50% 50ml IV hoặc glucagon 1mg SC/IM",
                "Theo dõi đường huyết mỗi 15-30 phút trong ít nhất 4-6 giờ (do thời gian bán thải dài)",
                "Duy trì glucose IV nếu cần (dextrose 5% hoặc 10% truyền liên tục)",
                "Theo dõi ít nhất 24 giờ (do thời gian bán thải dài, có thể tái phát hạ đường huyết)",
                "Rửa dạ dày nếu uống trong vòng 1-2 giờ (nhưng ưu tiên điều trị hạ đường huyết)",
                "Than hoạt tính (hiệu quả hạn chế do hấp thu nhanh)",
                "Hỗ trợ hô hấp và tuần hoàn nếu cần",
                "Theo dõi ý thức, dấu hiệu sống"
            ],
            "monitoring": "Đường huyết (mỗi 15-30 phút trong ít nhất 4-6 giờ), ý thức, dấu hiệu sống, điện giải, chức năng thận"
        },
        "reversal_agents": {
            "available": True,
            "agents": [
                {
                    "agent": "Glucose",
                    "route": "PO hoặc IV",
                    "dose": "15-20g PO hoặc dextrose 50% 50ml IV",
                    "notes": "Điều trị hạ đường huyết ngay lập tức"
                },
                {
                    "agent": "Glucagon",
                    "route": "SC hoặc IM",
                    "dose": "1mg SC/IM",
                    "notes": "Nếu không thể truyền IV, dùng glucagon để tăng đường huyết"
                }
            ]
        },
        "administration_instructions": {
            "oral": {
                "with_food": "Uống với thức ăn hoặc trước bữa ăn (15-30 phút trước bữa ăn) để tránh hạ đường huyết. Không bỏ bữa sau khi uống.",
                "timing": "Uống 1-2 lần/ngày, thường trước bữa sáng và/hoặc bữa tối. Khởi đầu với liều thấp (2.5-5mg/ngày) và tăng dần. Uống đúng giờ mỗi ngày."
            },
            "iv": {
                "reconstitution": "Không có dạng IV",
                "infusion_rate": "N/A",
                "compatibility": [],
                "incompatibility": [],
                "notes": "Chỉ có dạng uống"
            }
        },
        "references": {
            "primary_sources": [
                "FDA Drug Label - Glyburide (glibenclamide)",
                "UpToDate - Glyburide: Drug information",
                "UK Prospective Diabetes Study (UKPDS)",
                "American Diabetes Association guidelines",
                "Goodman & Gilman's The Pharmacological Basis of Therapeutics"
            ],
            "last_updated": "2024-12-19",
            "evidence_level": "High - Multiple large RCTs (UKPDS) and extensive clinical experience"
        }
    },
    "Gliclazide": {
        "group": "Diabetes - Sulfonylurea",
        "vietnamese_name": "Gliclazide, Diamicron",
        "administration": ["PO"],
        "indications": [
            "Đái tháo đường type 2"
        ],
        "contraindications": [
            "Đái tháo đường type 1",
            "Nhiễm toan ceton",
            "Suy thận nặng"
        ],
        "dosage": {
            "adult_standard": "80-320mg/ngày chia 1-2 lần",
            "adult_modified_release": "30-120mg x 1 lần/ngày",
            "notes": "Ít nguy cơ hạ đường huyết hơn glibenclamide"
        },
        "side_effects": [
            "Hạ đường huyết",
            "Tăng cân",
            "Ban da"
        ],
                  "interactions": [
              "Tương tự sulfonylurea khác"
          ],
          "pregnancy": "C",
          "mechanism_of_action": "Sulfonylurea thế hệ 2. Kích thích tế bào beta tuyến tụy tiết insulin bằng cách đóng kênh KATP (ATP-sensitive K+ channel), làm khử cực màng tế bào, mở kênh Ca2+, và giải phóng insulin. Chỉ hoạt động khi còn chức năng tế bào beta. Gliclazide ưu điểm: thời gian bán hủy ngắn hơn, ít nguy cơ hạ đường huyết hơn glibenclamide.",
          "monitoring": [
              "Đường huyết: HbA1c (mỗi 3 tháng), đường huyết đói, đường huyết sau ăn",
              "Dấu hiệu hạ đường huyết: run, vã mồ hôi, nhịp tim nhanh, lú lẫn, co giật",
              "Cân nặng - sulfonylureas có thể gây tăng cân",
              "Chức năng thận: creatinine, eGFR (suy thận tăng nguy cơ hạ đường huyết)",
              "Chức năng gan: ALT, AST (nếu có bệnh gan)"
          ],
          "precautions": [
              "Uống với thức ăn hoặc trước bữa ăn để tránh hạ đường huyết",
              "KHÔNG dùng ở đái tháo đường type 1 hoặc nhiễm toan ceton",
              "Thận trọng ở bệnh nhân suy thận - tăng nguy cơ hạ đường huyết (có thể cần giảm liều hoặc tránh dùng)",
              "Thận trọng ở bệnh nhân suy gan - tăng nguy cơ hạ đường huyết",
              "Hạ đường huyết là tác dụng phụ phổ biến nhất - bệnh nhân cần biết dấu hiệu và cách xử trí",
              "Tránh bỏ bữa - tăng nguy cơ hạ đường huyết",
              "Tránh rượu - tăng nguy cơ hạ đường huyết",
              "Có thể tăng cân - cần tư vấn chế độ ăn và tập luyện",
              "Gliclazide ưu điểm: thời gian bán hủy ngắn hơn, ít hạ đường huyết hơn glibenclamide"
          ],
          "pharmacokinetics": {
              "half_life": "10-12 giờ (ngắn hơn glibenclamide)",
              "onset": "30-60 phút (PO)",
              "duration": "12-24 giờ",
              "protein_binding": "85-95%",
              "clearance": "Gan (CYP2C9), thận (metabolites)"
          },
          "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm, tránh ánh sáng",
          "black_box_warnings": "Hạ đường huyết có thể gây nguy hiểm tính mạng, đặc biệt ở bệnh nhân suy thận, suy gan, người già. Bệnh nhân cần biết dấu hiệu và cách xử trí hạ đường huyết",
          "drug_interactions": {
              "major": [
                  {
                      "drug": "Rượu (ethanol)",
                      "mechanism": "Ức chế sản xuất glucose ở gan, tăng nguy cơ hạ đường huyết",
                      "effect": "Hạ đường huyết nghiêm trọng",
                      "management": "TRÁNH RƯỢU hoàn toàn khi dùng gliclazide. Cảnh báo bệnh nhân về nguy cơ."
                  },
                  {
                      "drug": "Beta-blockers (propranolol, metoprolol)",
                      "mechanism": "Che dấu triệu chứng hạ đường huyết (nhịp tim nhanh, run)",
                      "effect": "Khó nhận biết hạ đường huyết",
                      "management": "Thận trọng. Theo dõi đường huyết chặt chẽ."
                  }
              ],
              "moderate": [
                  {
                      "drug": "CYP2C9 inhibitors (fluconazole, amiodarone)",
                      "mechanism": "Ức chế chuyển hóa gliclazide, tăng nồng độ",
                      "effect": "Tăng nguy cơ hạ đường huyết",
                      "management": "Thận trọng. Theo dõi đường huyết. Có thể cần giảm liều gliclazide."
                  },
                  {
                      "drug": "Salicylates (aspirin liều cao)",
                      "mechanism": "Tăng tác dụng giảm đường huyết",
                      "effect": "Tăng nguy cơ hạ đường huyết",
                      "management": "Thận trọng. Theo dõi đường huyết."
                  }
              ],
              "minor": [
                  {
                      "drug": "Chloramphenicol",
                      "mechanism": "Tăng nồng độ gliclazide",
                      "effect": "Tăng nguy cơ hạ đường huyết",
                      "management": "Thận trọng. Theo dõi đường huyết."
                  }
              ]
          },
          "contraindications": {
              "absolute": [
                  "Đái tháo đường type 1",
                  "Nhiễm toan ceton do đái tháo đường",
                  "Dị ứng gliclazide hoặc sulfonylurea",
                  "Suy thận nặng (CrCl <30) - tăng nguy cơ hạ đường huyết"
              ],
              "relative": [
                  "Suy gan nặng - tăng nguy cơ hạ đường huyết",
                  "Người cao tuổi - tăng nguy cơ hạ đường huyết",
                  "Suy thận trung bình (CrCl 30-60) - giảm liều, theo dõi sát",
                  "Có thai - có thể gây hạ đường huyết ở trẻ sơ sinh",
                  "Bỏ bữa thường xuyên - tăng nguy cơ hạ đường huyết",
                  "Uống rượu - tăng nguy cơ hạ đường huyết"
              ]
          },
          "pregnancy_lactation": {
              "fda_category": "C",
              "pregnancy_details": "Có thể dùng trong thai kỳ nếu lợi ích > nguy cơ, nhưng THƯỜNG TRÁNH DÙNG. Sulfonylureas có thể gây hạ đường huyết ở trẻ sơ sinh. Insulin là lựa chọn ưu tiên trong thai kỳ. Nếu dùng, theo dõi đường huyết chặt chẽ và ngừng trước khi sinh.",
              "lactation": {
                  "safety": "Compatible",
                  "details": "Gliclazide bài tiết vào sữa mẹ ở nồng độ thấp. Ít có nguy cơ gây hạ đường huyết ở trẻ bú mẹ do nồng độ thấp.",
                  "recommendation": "Có thể dùng khi cho con bú với theo dõi chặt chẽ. Theo dõi dấu hiệu hạ đường huyết ở trẻ."
              }
          },
          "hepatic_adjustment": {
              "mild": "Thận trọng, giảm liều nhẹ",
              "moderate": "Giảm liều 25-50%. Theo dõi chức năng gan và đường huyết",
              "severe": "CHỐNG CHỈ ĐỊNH",
              "notes": "Gliclazide chuyển hóa ở gan qua CYP2C9. Suy gan làm giảm chuyển hóa, tăng nồng độ, tăng nguy cơ hạ đường huyết. Không dùng ở suy gan nặng."
          },
          "overdose_management": {
              "symptoms": [
                  "Hạ đường huyết: run, vã mồ hôi, nhịp tim nhanh, đói, lú lẫn, co giật, hôn mê",
                  "Hạ đường huyết ít kéo dài hơn glibenclamide (do thời gian bán thải ngắn hơn)"
              ],
              "antidote": "Glucose (đường uống hoặc IV)",
              "treatment": [
                  "Nếu tỉnh táo: Glucose 15-20g PO (nước đường, nước ngọt, kẹo)",
                  "Nếu hôn mê hoặc không thể uống: Dextrose 50% 50ml IV hoặc glucagon 1mg SC/IM",
                  "Theo dõi đường huyết mỗi 15-30 phút trong ít nhất 4 giờ",
                  "Duy trì glucose IV nếu cần (dextrose 5% hoặc 10% truyền liên tục)",
                  "Theo dõi ít nhất 12-24 giờ (thời gian ngắn hơn glibenclamide)",
                  "Rửa dạ dày nếu uống trong vòng 1-2 giờ (nhưng ưu tiên điều trị hạ đường huyết)",
                  "Than hoạt tính (hiệu quả hạn chế)",
                  "Hỗ trợ hô hấp và tuần hoàn nếu cần"
              ],
              "monitoring": "Đường huyết (mỗi 15-30 phút trong ít nhất 4 giờ), ý thức, dấu hiệu sống, điện giải"
          },
          "reversal_agents": {
              "available": True,
              "agents": [
                  {
                      "agent": "Glucose",
                      "route": "PO hoặc IV",
                      "dose": "15-20g PO hoặc dextrose 50% 50ml IV",
                      "notes": "Điều trị hạ đường huyết ngay lập tức"
                  },
                  {
                      "agent": "Glucagon",
                      "route": "SC hoặc IM",
                      "dose": "1mg SC/IM",
                      "notes": "Nếu không thể truyền IV, dùng glucagon để tăng đường huyết"
                  }
              ]
          },
          "administration_instructions": {
              "oral": {
                  "with_food": "Uống với thức ăn hoặc trước bữa ăn (15-30 phút trước bữa ăn) để tránh hạ đường huyết. Không bỏ bữa sau khi uống.",
                  "timing": "Uống 1-2 lần/ngày, thường trước bữa sáng và/hoặc bữa tối. Dạng modified-release: 1 lần/ngày với bữa sáng. Khởi đầu với liều thấp và tăng dần."
              },
              "iv": {
                  "reconstitution": "Không có dạng IV",
                  "infusion_rate": "N/A",
                  "compatibility": [],
                  "incompatibility": [],
                  "notes": "Chỉ có dạng uống"
              }
          },
          "references": {
              "primary_sources": [
                  "FDA Drug Label - Diamicron (gliclazide)",
                  "UpToDate - Gliclazide: Drug information",
                  "UK Prospective Diabetes Study (UKPDS)",
                  "American Diabetes Association guidelines",
                  "Goodman & Gilman's The Pharmacological Basis of Therapeutics"
              ],
              "last_updated": "2024-12-19",
              "evidence_level": "High - Multiple large RCTs (UKPDS) and extensive clinical experience"
          }
      },
      "Insulin": {
        "group": "Diabetes - Insulin",
        "vietnamese_name": "Insulin",
        "administration": ["SC", "IV"],
        "indications": [
            "Đái tháo đường type 1",
            "Đái tháo đường type 2 (khi không kiểm soát bằng thuốc uống)",
            "Nhiễm toan ceton do đái tháo đường",
            "Tăng đường huyết tăng áp lực thẩm thấu",
            "Tăng đường huyết trong bệnh viện"
        ],
        "contraindications": [
            "Hạ đường huyết",
            "Dị ứng insulin"
        ],
        "dosage": {
            "type1_basal": "0.2-0.4 đơn vị/kg/ngày (NPH hoặc insulin dài)",
            "type1_bolus": "0.5-1 đơn vị/kg/ngày chia trước bữa ăn",
            "dka_iv": "0.1 đơn vị/kg/giờ IV truyền liên tục",
            "hospital_hyperglycemia": "0.05-0.1 đơn vị/kg/giờ",
            "notes": "Nhiều loại: rapid-acting, short-acting, intermediate, long-acting. Điều chỉnh theo đường huyết"
        },
        "side_effects": [
            "Hạ đường huyết (nguy hiểm)",
            "Tăng cân",
            "Phản ứng tại chỗ tiêm",
            "Kháng insulin (hiếm)"
        ],
        "interactions": [
            "Beta-blocker: che dấu triệu chứng hạ đường huyết",
            "Corticosteroid: tăng đường huyết",
            "Rượu: tăng nguy cơ hạ đường huyết"
        ],
        "pregnancy": "B - An toàn, điều chỉnh liều theo thai kỳ",
        "mechanism_of_action": "Insulin là hormone tự nhiên được tiết ra từ tế bào beta tuyến tụy. Gắn với thụ thể insulin, kích hoạt các tín hiệu nội bào, tăng vận chuyển glucose vào tế bào, kích thích tổng hợp glycogen, protein, lipid, và ức chế sản xuất glucose ở gan. Giảm đường huyết bằng cách tăng sử dụng glucose và giảm sản xuất glucose",
        "monitoring": [
            "Đường huyết (glucose) thường xuyên: Trước bữa ăn, 2 giờ sau bữa ăn, trước khi ngủ",
            "HbA1c mỗi 3 tháng (mục tiêu <7% hoặc theo cá thể hóa)",
            "Dấu hiệu hạ đường huyết: Run rẩy, đổ mồ hôi, nhịp tim nhanh, đói, nhầm lẫn, co giật, hôn mê",
            "Dấu hiệu tăng đường huyết: Khát nhiều, tiểu nhiều, mệt mỏi, mờ mắt",
            "Cân nặng (insulin có thể gây tăng cân)",
            "Chức năng thận (giảm clearance insulin ở suy thận)",
            "Kiểm tra vị trí tiêm (tránh lipodystrophy)"
        ],
        "precautions": [
            "LUÔN có glucagon và glucose sẵn để điều trị hạ đường huyết",
            "Điều chỉnh liều theo đường huyết, bữa ăn, hoạt động thể chất",
            "Xoay vị trí tiêm (bụng, đùi, cánh tay, mông)",
            "Bảo quản đúng cách: Insulin đang dùng có thể để ở nhiệt độ phòng, chưa mở phải để tủ lạnh",
            "Không được làm đông lạnh insulin",
            "Giảm liều ở suy thận (giảm clearance)",
            "Tăng liều trong bệnh nặng, stress, nhiễm trùng",
            "Dạy bệnh nhân nhận biết và xử trí hạ đường huyết",
            "Trong thai kỳ: tăng nhu cầu insulin, điều chỉnh thường xuyên"
        ],
        "pharmacokinetics": {
            "half_life": "Rapid-acting (lispro, aspart): 1 giờ; Short-acting (regular): 2-4 giờ; Intermediate (NPH): 8-12 giờ; Long-acting (glargine, detemir): 12-24 giờ; Ultra-long (degludec): 42 giờ",
            "onset": "Rapid: 15 phút; Short: 30-60 phút; Intermediate: 1-3 giờ; Long: 1-2 giờ",
            "duration": "Rapid: 3-5 giờ; Short: 6-8 giờ; Intermediate: 12-16 giờ; Long: 18-24 giờ; Ultra-long: >42 giờ",
            "protein_binding": "Không (peptide hormone)",
            "clearance": "Gan (50-60%), thận (30-40%), một phần bị phân hủy bởi insulinase"
        },
        "storage": "Chưa mở: Tủ lạnh (2-8°C), không đông lạnh. Đang dùng: Nhiệt độ phòng (<30°C), tránh ánh sáng, tránh nhiệt độ cao. Dùng trong vòng 28-30 ngày sau khi mở",
        "black_box_warnings": "Hạ đường huyết có thể đe dọa tính mạng. Cần theo dõi đường huyết thường xuyên và có sẵn glucose/glucagon để điều trị hạ đường huyết. Không được dùng chung ống tiêm insulin",
        "drug_interactions": {
            "major": [
                {
                    "drug": "Beta-blockers (atenolol, metoprolol, propranolol)",
                    "mechanism": "Beta-blockers che dấu triệu chứng hạ đường huyết (nhịp tim nhanh, run, đổ mồ hôi) và ức chế glycogenolysis",
                    "effect": "Tăng nguy cơ hạ đường huyết nặng, khó nhận biết triệu chứng, khó điều trị",
                    "management": "Theo dõi đường huyết thường xuyên. Bệnh nhân nên biết các triệu chứng hạ đường huyết khác (lú lẫn, đổ mồ hôi). Cân nhắc dùng beta-1 selective (atenolol, metoprolol) thay vì non-selective (propranolol)."
                },
                {
                    "drug": "Rượu (ethanol)",
                    "mechanism": "Rượu ức chế gluconeogenesis ở gan, tăng nguy cơ hạ đường huyết, đặc biệt khi đói",
                    "effect": "Tăng nguy cơ hạ đường huyết nặng, có thể hôn mê, đặc biệt khi uống rượu mà không ăn",
                    "management": "Tránh uống rượu khi đói. Nếu uống rượu, nên ăn kèm. Theo dõi đường huyết sau khi uống rượu. Giáo dục bệnh nhân về nguy cơ."
                },
                {
                    "drug": "Corticosteroids (prednisone, dexamethasone, hydrocortisone)",
                    "mechanism": "Corticosteroids tăng sản xuất glucose ở gan, tăng insulin resistance, tăng đường huyết",
                    "effect": "Giảm hiệu quả insulin, tăng nhu cầu insulin, tăng đường huyết",
                    "management": "Tăng liều insulin khi dùng corticosteroid. Theo dõi đường huyết thường xuyên. Giảm liều insulin khi ngừng corticosteroid."
                }
            ],
            "moderate": [
                {
                    "drug": "Thiazide diuretics (hydrochlorothiazide, chlorthalidone)",
                    "mechanism": "Thiazide có thể gây hạ kali máu, tăng đường huyết nhẹ",
                    "effect": "Tăng nhẹ đường huyết, có thể cần tăng liều insulin",
                    "management": "Theo dõi đường huyết. Có thể cần tăng liều insulin nhẹ."
                },
                {
                    "drug": "Sulfonylureas (glibenclamide, gliclazide)",
                    "mechanism": "Cả hai đều kích thích tiết insulin, tác dụng hiệp đồng",
                    "effect": "Tăng nguy cơ hạ đường huyết",
                    "management": "Thường không dùng cùng. Nếu cần, giảm liều cả hai. Theo dõi đường huyết chặt chẽ."
                },
                {
                    "drug": "ACE inhibitors, ARB (enalapril, losartan)",
                    "mechanism": "ACE inhibitors có thể tăng nhạy cảm với insulin, tăng nguy cơ hạ đường huyết",
                    "effect": "Tăng nguy cơ hạ đường huyết nhẹ",
                    "management": "Theo dõi đường huyết. Có thể cần giảm liều insulin nhẹ."
                },
                {
                    "drug": "MAO inhibitors",
                    "mechanism": "MAO inhibitors có thể tăng tác dụng insulin",
                    "effect": "Tăng nguy cơ hạ đường huyết",
                    "management": "Theo dõi đường huyết. Có thể cần giảm liều insulin."
                },
                {
                    "drug": "Pentamidine (antiparasitic)",
                    "mechanism": "Pentamidine có thể gây hạ đường huyết (phá hủy tế bào beta) hoặc tăng đường huyết",
                    "effect": "Hạ đường huyết hoặc tăng đường huyết",
                    "management": "Theo dõi đường huyết chặt chẽ. Điều chỉnh liều insulin theo đường huyết."
                }
            ],
            "minor": [
                {
                    "drug": "Aspirin liều thấp",
                    "mechanism": "Aspirin có thể tăng nhẹ tác dụng insulin",
                    "effect": "Tăng nhẹ nguy cơ hạ đường huyết",
                    "management": "Thường không cần điều chỉnh. Theo dõi đường huyết."
                },
                {
                    "drug": "Thyroid hormones (levothyroxine)",
                    "mechanism": "Thyroid hormones tăng chuyển hóa, có thể tăng nhu cầu insulin",
                    "effect": "Tăng nhẹ nhu cầu insulin",
                    "management": "Theo dõi đường huyết. Có thể cần tăng liều insulin nhẹ khi bắt đầu levothyroxine."
                }
            ]
        },
        "contraindications": {
            "absolute": [
                "Hạ đường huyết (hypoglycemia) - không được dùng khi đường huyết thấp",
                "Dị ứng insulin hoặc bất kỳ thành phần nào trong chế phẩm insulin",
                "Hôn mê do hạ đường huyết - không được dùng insulin cho đến khi hồi phục"
            ],
            "relative": [
                "Suy thận - giảm clearance insulin, giảm liều insulin",
                "Suy gan - giảm gluconeogenesis, tăng nguy cơ hạ đường huyết, giảm liều insulin",
                "Suy tim - thận trọng, có thể cần điều chỉnh liều",
                "Người cao tuổi - tăng nguy cơ hạ đường huyết, cần liều thấp hơn",
                "Bệnh nhân không có khả năng tự quản lý - cần người chăm sóc",
                "Bệnh nhân không có khả năng nhận biết hạ đường huyết - tăng nguy cơ",
                "Thai kỳ - điều chỉnh liều thường xuyên (tăng nhu cầu trong tam cá nguyệt 2-3)"
            ]
        },
        "pregnancy_lactation": {
            "fda_category": "B",
            "pregnancy_details": "Insulin là thuốc được ưu tiên trong thai kỳ cho đái tháo đường. Insulin không qua nhau thai, an toàn cho thai nhi. Nhu cầu insulin tăng trong thai kỳ, đặc biệt ở tam cá nguyệt 2-3 (tăng 50-100%). Cần điều chỉnh liều thường xuyên. Hạ đường huyết mẹ có thể ảnh hưởng đến thai nhi. Tăng đường huyết mẹ có thể gây dị tật thai nhi, thai to, hạ đường huyết ở trẻ sơ sinh. Mục tiêu đường huyết: <95 mg/dL (trước ăn), <140 mg/dL (1 giờ sau ăn), <120 mg/dL (2 giờ sau ăn).",
            "lactation": {
                "safety": "Compatible",
                "details": "Insulin không bài tiết vào sữa mẹ ở nồng độ đáng kể. Insulin là protein, bị tiêu hóa trong đường tiêu hóa của trẻ, không hấp thu. Insulin là thuốc được ưu tiên cho phụ nữ đái tháo đường cho con bú. Nhu cầu insulin có thể giảm nhẹ khi cho con bú (do tiêu thụ glucose).",
                "recommendation": "Có thể dùng khi cho con bú. Insulin là thuốc được ưu tiên cho phụ nữ đái tháo đường cho con bú. Theo dõi đường huyết và điều chỉnh liều nếu cần."
            }
        },
        "hepatic_adjustment": {
            "mild": "Thận trọng. Giảm liều insulin 10-20% do giảm gluconeogenesis, tăng nguy cơ hạ đường huyết.",
            "moderate": "Thận trọng. Giảm liều insulin 20-30%. Theo dõi đường huyết thường xuyên. Tăng nguy cơ hạ đường huyết.",
            "severe": "Thận trọng. Giảm liều insulin 30-50%. Theo dõi đường huyết rất thường xuyên. Tăng nguy cơ hạ đường huyết nặng. Cân nhắc dùng insulin tác dụng ngắn và điều chỉnh theo đường huyết.",
            "notes": "Insulin chuyển hóa chủ yếu ở gan (50-60%). Suy gan làm giảm gluconeogenesis và glycogenolysis, tăng nguy cơ hạ đường huyết. Cần giảm liều insulin và theo dõi đường huyết thường xuyên."
        },
        "overdose_management": {
            "symptoms": [
                "Hạ đường huyết (hypoglycemia) - triệu chứng chính và nguy hiểm nhất",
                "Triệu chứng nhẹ đến trung bình: Run rẩy, đổ mồ hôi, nhịp tim nhanh, đói, lo lắng, nhức đầu, nhầm lẫn nhẹ",
                "Triệu chứng nặng: Co giật, hôn mê, mất ý thức, rối loạn hành vi, yếu cơ, nhìn đôi",
                "Hạ đường huyết nặng có thể gây tổn thương não vĩnh viễn, tử vong",
                "Tăng kali máu (hiếm, với insulin IV liều cao)",
                "Hạ kali máu (do điều trị hạ đường huyết với glucose)"
            ],
            "antidote": "Glucagon (đối kháng insulin, kích thích glycogenolysis), Glucose (điều trị trực tiếp hạ đường huyết)",
            "treatment": [
                "Đo đường huyết ngay (nếu có thể, nhưng không trì hoãn điều trị nếu nghi ngờ hạ đường huyết)",
                "Nếu bệnh nhân tỉnh và có thể nuốt:",
                "  - Glucose 15-20g đường miệng (4 viên glucose, 1/2 lon nước ngọt, 1/2 cốc nước trái cây, 1 thìa mật ong)",
                "  - Lặp lại sau 15 phút nếu đường huyết vẫn <70 mg/dL",
                "  - Ăn bữa ăn hoặc snack sau khi đường huyết ổn định",
                "Nếu bệnh nhân không tỉnh hoặc không thể nuốt:",
                "  - Glucagon 1mg SC/IM (có thể lặp lại sau 15 phút nếu cần)",
                "  - HOẶC Dextrose 50% 50ml IV (có thể lặp lại)",
                "  - HOẶC Dextrose 10% truyền IV liên tục nếu cần",
                "  - Theo dõi đường huyết mỗi 15-30 phút cho đến khi ổn định",
                "Ngừng insulin tạm thời (nếu đang truyền liên tục)",
                "Theo dõi đường huyết thường xuyên (mỗi 15-30 phút) cho đến khi ổn định",
                "Theo dõi dấu hiệu sinh tồn: Huyết áp, nhịp tim, ý thức",
                "Theo dõi kali máu (có thể hạ kali sau khi điều trị hạ đường huyết)",
                "Hỗ trợ hô hấp nếu cần",
                "Theo dõi ít nhất 24 giờ (tùy loại insulin - rapid-acting 3-5 giờ, long-acting 18-24 giờ)"
            ],
            "monitoring": "Đường huyết (mỗi 15-30 phút cho đến khi ổn định), dấu hiệu sinh tồn (huyết áp, nhịp tim, ý thức), kali máu (có thể hạ kali), dấu hiệu hạ đường huyết tái phát, dấu hiệu tổn thương não (nếu hạ đường huyết nặng kéo dài)"
        },
        "reversal_agents": {
            "available": True,
            "agents": [
                {
                    "name": "Glucagon",
                    "mechanism": "Kích thích glycogenolysis ở gan, tăng đường huyết, đối kháng tác dụng insulin",
                    "dose": "1mg SC/IM, có thể lặp lại sau 15 phút nếu cần",
                    "indication": "Hạ đường huyết nặng, đặc biệt khi bệnh nhân không tỉnh hoặc không thể nuốt"
                },
                {
                    "name": "Glucose (Dextrose)",
                    "mechanism": "Cung cấp glucose trực tiếp, tăng đường huyết",
                    "dose": "Dextrose 50% 50ml IV, hoặc Dextrose 10% truyền IV liên tục",
                    "indication": "Hạ đường huyết nặng, đặc biệt khi bệnh nhân không tỉnh"
                },
                {
                    "name": "Glucose đường miệng",
                    "mechanism": "Cung cấp glucose trực tiếp qua đường tiêu hóa",
                    "dose": "15-20g glucose (4 viên glucose, 1/2 lon nước ngọt, 1/2 cốc nước trái cây)",
                    "indication": "Hạ đường huyết nhẹ đến trung bình, bệnh nhân tỉnh và có thể nuốt"
                }
            ]
        },
        "administration_instructions": {
            "oral": {
                "with_food": "Không áp dụng - insulin không uống được",
                "timing": "Không áp dụng"
            },
            "iv": {
                "reconstitution": "Insulin regular (short-acting) có thể dùng IV. Pha trong normal saline hoặc dextrose. Nồng độ thường: 0.05-0.1 đơn vị/kg/giờ trong DKA hoặc tăng đường huyết trong bệnh viện.",
                "infusion_rate": "Truyền liên tục với tốc độ điều chỉnh theo đường huyết. Thường bắt đầu với 0.05-0.1 đơn vị/kg/giờ. Điều chỉnh theo protocol insulin sliding scale hoặc theo đường huyết.",
                "compatibility": [
                    "Normal saline (0.9% NaCl)",
                    "Dextrose 5% (D5W)",
                    "Dextrose 10% (D10W)",
                    "Ringer's lactate"
                ],
                "incompatibility": [
                    "Không trộn với các thuốc khác trong cùng ống truyền",
                    "Một số thuốc có thể làm giảm hiệu quả insulin (cần kiểm tra cụ thể)"
                ],
                "notes": "Insulin IV chỉ dùng trong bệnh viện, DKA, hoặc tăng đường huyết nặng. Phải có protocol rõ ràng và theo dõi đường huyết thường xuyên (mỗi 1-2 giờ)."
            },
            "sc": {
                "with_food": "Rapid-acting insulin: Tiêm 15 phút TRƯỚC bữa ăn. Short-acting insulin: Tiêm 30-60 phút TRƯỚC bữa ăn. Long-acting insulin: Tiêm 1 lần/ngày, không phụ thuộc bữa ăn.",
                "timing": "Rapid-acting (lispro, aspart): 15 phút trước bữa ăn. Short-acting (regular): 30-60 phút trước bữa ăn. Intermediate (NPH): 1-3 giờ trước bữa ăn. Long-acting (glargine, detemir): 1 lần/ngày, cùng một giờ mỗi ngày. Xoay vị trí tiêm (bụng, đùi, cánh tay, mông)."
            }
        },
        "references": {
            "primary_sources": [
                "FDA Drug Label - Various insulin products",
                "UpToDate - Insulin therapy in type 1 and type 2 diabetes",
                "American Diabetes Association (ADA) Standards of Medical Care in Diabetes",
                "American Association of Clinical Endocrinologists (AACE) Guidelines",
                "DCCT Study - New England Journal of Medicine (1993) - Intensive insulin therapy in type 1 diabetes",
                "UKPDS Study - Lancet (1998) - Intensive glucose control in type 2 diabetes",
                "Goodman & Gilman's Pharmacological Basis of Therapeutics - Insulin and oral hypoglycemic agents"
            ],
            "last_updated": "2024-12-19",
            "evidence_level": "High - Multiple large RCTs (DCCT, UKPDS) showing benefit of intensive glucose control"
        }
    },
    "Empagliflozin": {
        "group": "Diabetes - SGLT2 Inhibitor",
        "vietnamese_name": "Empagliflozin, Jardiance",
        "administration": ["PO"],
        "indications": [
            "Đái tháo đường type 2",
            "Suy tim với phân suất tống máu giảm (HFrEF)",
            "Bệnh thận mạn tính (CKD) ở bệnh nhân đái tháo đường",
            "Giảm nguy cơ tim mạch"
        ],
        "contraindications": [
            "Đái tháo đường type 1",
            "Nhiễm toan ceton do đái tháo đường",
            "Suy thận nặng (eGFR <20)",
            "Đang lọc máu",
            "Nhiễm trùng đường tiết niệu tái phát"
        ],
        "dosage": {
            "adult_type2_dm": "10-25mg x 1 lần/ngày",
            "adult_heart_failure": "10mg x 1 lần/ngày",
            "adult_ckd": "10mg x 1 lần/ngày (eGFR ≥20)",
            "notes": "Uống bất kỳ lúc nào, không cần ăn. Giảm đường huyết nhẹ"
        },
        "renal_adjustment": {
            "normal": "10-25mg/ngày",
            "30_60": "10mg/ngày (eGFR ≥30)",
            "under_30": "Không dùng nếu eGFR <20"
        },
        "side_effects": [
            "Nhiễm trùng đường tiết niệu",
            "Nhiễm trùng đường sinh dục (nấm âm đạo, viêm quy đầu)",
            "Mất nước, hạ huyết áp",
            "Nhiễm toan ceton (hiếm)",
            "Gãy xương tăng nhẹ",
            "Hoại thư Fournier (hiếm nhưng nguy hiểm)"
        ],
        "interactions": [
            "Insulin/Sulfonylurea: tăng nguy cơ hạ đường huyết",
            "Diuretics: tăng nguy cơ mất nước",
            "Digoxin: tăng nhẹ nồng độ digoxin"
        ],
        "pregnancy": "C",
        "mechanism_of_action": "Empagliflozin là chất ức chế chọn lọc sodium-glucose cotransporter 2 (SGLT2) ở ống lượn gần của thận. SGLT2 chịu trách nhiệm tái hấp thu 90% glucose từ nước tiểu. Bằng cách ức chế SGLT2, empagliflozin ngăn chặn tái hấp thu glucose, làm tăng bài tiết glucose qua nước tiểu (glucosuria), từ đó giảm đường huyết. Cơ chế này không phụ thuộc vào insulin, giúp giảm đường huyết mà không tăng nguy cơ hạ đường huyết (trừ khi dùng với insulin hoặc sulfonylurea). Ngoài ra, empagliflozin có lợi ích tim mạch và thận: giảm thể tích tuần hoàn, giảm huyết áp, giảm albumin niệu, và cải thiện kết cục tim mạch ở bệnh nhân suy tim và bệnh thận mạn. Các nghiên cứu EMPA-REG OUTCOME, EMPEROR-Reduced, và EMPEROR-Preserved đã chứng minh lợi ích tim mạch và thận.",
        "monitoring": [
            "Đường huyết (HbA1c, glucose máu) - đánh giá hiệu quả giảm đường huyết",
            "Chức năng thận (eGFR, creatinine) - không dùng nếu eGFR <20",
            "Nhiễm trùng đường tiết niệu (UTI) - triệu chứng, cấy nước tiểu nếu cần",
            "Nhiễm trùng đường sinh dục (nấm âm đạo, viêm quy đầu) - đặc biệt ở phụ nữ",
            "Dấu hiệu mất nước, hạ huyết áp (đặc biệt ở người cao tuổi, dùng diuretics)",
            "Nhiễm toan ceton (DKA) - glucose máu, ketone, pH máu nếu có triệu chứng",
            "Hoại thư Fournier (nhiễm trùng vùng sinh dục nặng) - hiếm nhưng nguy hiểm",
            "Gãy xương (đặc biệt ở người cao tuổi)"
        ],
        "precautions": [
            "Không dùng cho đái tháo đường type 1 (tăng nguy cơ nhiễm toan ceton)",
            "Không dùng nếu eGFR <20 (empagliflozin) hoặc <25 (dapagliflozin) - không hiệu quả",
            "Tăng nguy cơ nhiễm trùng đường tiết niệu và đường sinh dục - vệ sinh tốt, uống nhiều nước",
            "Nguy cơ nhiễm toan ceton (DKA) - đặc biệt ở bệnh nhân type 1, phẫu thuật, bệnh cấp tính, nhịn ăn",
            "Nguy cơ mất nước, hạ huyết áp - đặc biệt ở người cao tuổi, dùng diuretics, suy tim",
            "Tăng nguy cơ hạ đường huyết khi dùng với insulin hoặc sulfonylurea - có thể cần giảm liều",
            "Hoại thư Fournier - hiếm nhưng nguy hiểm, cần chú ý vệ sinh vùng sinh dục",
            "Uống nhiều nước để giảm nguy cơ nhiễm trùng",
            "Có thể dùng bất kỳ lúc nào, không cần ăn",
            "Lợi ích tim mạch và thận độc lập với tác dụng giảm đường huyết"
        ],
        "pharmacokinetics": {
            "half_life": "12.4 giờ",
            "onset": "1 giờ",
            "duration": "24 giờ",
            "protein_binding": "86.2%",
            "clearance": "Gan: chuyển hóa qua glucuronidation (phần lớn). Thận: bài tiết một phần nguyên dạng và metabolites. Không cần điều chỉnh liều ở suy gan, nhưng không dùng nếu eGFR <20."
        },
        "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm, tránh ánh sáng. Viên nén: bảo quản trong bao bì kín.",
        "black_box_warnings": None,
        "drug_interactions": {
            "major": [
                {
                    "drug": "Insulin, Sulfonylurea (glibenclamide, gliclazide)",
                    "mechanism": "Tác dụng hiệp đồng giảm đường huyết",
                    "effect": "Tăng nguy cơ hạ đường huyết",
                    "management": "Giảm liều insulin hoặc sulfonylurea khi bắt đầu empagliflozin. Theo dõi đường huyết chặt chẽ."
                },
                {
                    "drug": "Loop diuretics (furosemide, torsemide)",
                    "mechanism": "Tăng bài tiết natri và nước",
                    "effect": "Tăng nguy cơ mất nước, hạ huyết áp, suy thận cấp",
                    "management": "Thận trọng. Theo dõi huyết áp, cân nặng, chức năng thận. Có thể cần giảm liều diuretic."
                }
            ],
            "moderate": [
                {
                    "drug": "Digoxin",
                    "mechanism": "Empagliflozin có thể tăng nhẹ nồng độ digoxin",
                    "effect": "Tăng nguy cơ độc tính digoxin",
                    "management": "Theo dõi nồng độ digoxin, ECG. Điều chỉnh liều digoxin nếu cần."
                },
                {
                    "drug": "Thiazide diuretics (hydrochlorothiazide)",
                    "mechanism": "Tăng bài tiết natri và nước",
                    "effect": "Tăng nguy cơ mất nước, hạ huyết áp",
                    "management": "Thận trọng. Theo dõi huyết áp, cân nặng."
                }
            ],
            "minor": [
                {
                    "drug": "UDP-glucuronosyltransferase (UGT) inducers",
                    "mechanism": "Có thể giảm nồng độ empagliflozin",
                    "effect": "Giảm hiệu quả empagliflozin",
                    "management": "Thận trọng. Theo dõi đường huyết."
                }
            ]
        },
        "contraindications": {
            "absolute": [
                "Đái tháo đường type 1",
                "Nhiễm toan ceton do đái tháo đường",
                "Suy thận nặng (eGFR <20)",
                "Đang lọc máu",
                "Dị ứng empagliflozin"
            ],
            "relative": [
                "Nhiễm trùng đường tiết niệu tái phát - tăng nguy cơ nhiễm trùng",
                "Suy tim nặng - tăng nguy cơ mất nước",
                "Người cao tuổi - tăng nguy cơ mất nước, hạ huyết áp",
                "Dùng diuretics - tăng nguy cơ mất nước",
                "Nhiễm trùng đường sinh dục tái phát - tăng nguy cơ nhiễm trùng"
            ]
        },
        "pregnancy_lactation": {
            "fda_category": "C",
            "pregnancy_details": "Không có nghiên cứu đầy đủ ở người. Có thể dùng trong thai kỳ nếu lợi ích > nguy cơ. Không nên dùng trong 3 tháng đầu trừ khi thực sự cần thiết. Có thể gây hạ đường huyết ở thai nhi. Theo dõi đường huyết chặt chẽ trong thai kỳ.",
            "lactation": {
                "safety": "Caution",
                "details": "Empagliflozin bài tiết vào sữa mẹ ở nồng độ thấp. Không có dữ liệu đầy đủ về an toàn ở trẻ bú mẹ.",
                "recommendation": "Thận trọng khi dùng khi cho con bú. Cân nhắc ngừng cho con bú hoặc ngừng thuốc nếu có thể. Nếu cần dùng, theo dõi trẻ chặt chẽ."
            }
        },
        "hepatic_adjustment": {
            "mild": "Không đổi",
            "moderate": "Không đổi",
            "severe": "Không đổi (không chuyển hóa đáng kể qua gan)",
            "notes": "Empagliflozin chủ yếu chuyển hóa qua glucuronidation ở gan, nhưng không cần điều chỉnh liều ở suy gan nhẹ đến trung bình. Chưa có nghiên cứu đầy đủ ở suy gan nặng."
        },
        "overdose_management": {
            "symptoms": [
                "Hạ đường huyết",
                "Mất nước",
                "Hạ huyết áp",
                "Nhiễm toan ceton (hiếm)"
            ],
            "antidote": "Không có antidote đặc hiệu",
            "treatment": [
                "Điều trị hạ đường huyết: Glucose 15-20g PO hoặc dextrose IV",
                "Bù dịch nếu mất nước, hạ huyết áp",
                "Theo dõi đường huyết, điện giải",
                "Rửa dạ dày nếu uống trong vòng 1-2 giờ",
                "Than hoạt tính không hiệu quả (do không hấp thu qua đường tiêu hóa tốt)",
                "Theo dõi chức năng thận",
                "Nếu có nhiễm toan ceton: điều trị theo protocol DKA"
            ],
            "monitoring": "Đường huyết, huyết áp, cân nặng, chức năng thận, điện giải, dấu hiệu nhiễm toan ceton"
        },
        "reversal_agents": {
            "available": False,
            "agents": []
        },
        "administration_instructions": {
            "oral": {
                "with_food": "Có thể dùng với hoặc không có thức ăn. Không ảnh hưởng đến hấp thu.",
                "timing": "Uống 1 lần/ngày, bất kỳ lúc nào trong ngày. Nên uống vào cùng một thời điểm mỗi ngày để dễ nhớ."
            },
            "iv": {
                "reconstitution": "Không có dạng IV",
                "infusion_rate": "N/A",
                "compatibility": [],
                "incompatibility": [],
                "notes": "Chỉ có dạng uống"
            }
        },
        "references": {
            "primary_sources": [
                "FDA Drug Label - Jardiance (empagliflozin)",
                "EMPA-REG OUTCOME Study - New England Journal of Medicine",
                "EMPEROR-Reduced Study - New England Journal of Medicine",
                "EMPEROR-Preserved Study - New England Journal of Medicine",
                "UpToDate - Empagliflozin: Drug information"
            ],
            "last_updated": "2024-12-19",
            "evidence_level": "High - Multiple large RCTs (EMPA-REG OUTCOME, EMPEROR-Reduced, EMPEROR-Preserved)"
        }
    },
    "Dapagliflozin": {
        "group": "Diabetes - SGLT2 Inhibitor",
        "vietnamese_name": "Dapagliflozin, Forxiga",
        "administration": ["PO"],
        "indications": [
            "Đái tháo đường type 2",
            "Suy tim với phân suất tống máu giảm (HFrEF)",
            "Bệnh thận mạn tính (CKD) ở bệnh nhân đái tháo đường"
        ],
        "contraindications": [
            "Đái tháo đường type 1",
            "Nhiễm toan ceton",
            "Suy thận nặng (eGFR <25)",
            "Đang lọc máu",
            "Nhiễm trùng đường tiết niệu tái phát"
        ],
        "dosage": {
            "adult_type2_dm": "5-10mg x 1 lần/ngày",
            "adult_heart_failure": "10mg x 1 lần/ngày",
            "adult_ckd": "10mg x 1 lần/ngày (eGFR ≥25)",
            "notes": "Uống bất kỳ lúc nào"
        },
        "renal_adjustment": {
            "normal": "5-10mg/ngày",
            "30_60": "10mg/ngày (eGFR ≥25)",
            "under_30": "Không dùng nếu eGFR <25"
        },
        "side_effects": [
            "Nhiễm trùng đường tiết niệu",
            "Nhiễm trùng đường sinh dục",
            "Mất nước",
            "Nhiễm toan ceton (hiếm)"
        ],
        "interactions": [
            "Insulin/Sulfonylurea: tăng nguy cơ hạ đường huyết",
            "Diuretics: mất nước"
        ],
        "pregnancy": "C",
        "mechanism_of_action": "Dapagliflozin là chất ức chế chọn lọc sodium-glucose cotransporter 2 (SGLT2) ở ống lượn gần của thận. SGLT2 chịu trách nhiệm tái hấp thu 90% glucose từ nước tiểu. Bằng cách ức chế SGLT2, dapagliflozin ngăn chặn tái hấp thu glucose, làm tăng bài tiết glucose qua nước tiểu (glucosuria), từ đó giảm đường huyết. Cơ chế này không phụ thuộc vào insulin, giúp giảm đường huyết mà không tăng nguy cơ hạ đường huyết (trừ khi dùng với insulin hoặc sulfonylurea). Dapagliflozin có lợi ích tim mạch và thận: giảm thể tích tuần hoàn, giảm huyết áp, giảm albumin niệu, và cải thiện kết cục tim mạch ở bệnh nhân suy tim và bệnh thận mạn. Các nghiên cứu DECLARE-TIMI 58 và DAPA-HF đã chứng minh lợi ích tim mạch và thận.",
        "monitoring": [
            "Đường huyết (HbA1c, glucose máu) - đánh giá hiệu quả giảm đường huyết",
            "Chức năng thận (eGFR, creatinine) - không dùng nếu eGFR <25",
            "Nhiễm trùng đường tiết niệu (UTI) - triệu chứng, cấy nước tiểu nếu cần",
            "Nhiễm trùng đường sinh dục (nấm âm đạo, viêm quy đầu) - đặc biệt ở phụ nữ",
            "Dấu hiệu mất nước, hạ huyết áp (đặc biệt ở người cao tuổi, dùng diuretics)",
            "Nhiễm toan ceton (DKA) - glucose máu, ketone, pH máu nếu có triệu chứng",
            "Hoại thư Fournier (nhiễm trùng vùng sinh dục nặng) - hiếm nhưng nguy hiểm"
        ],
        "precautions": [
            "Không dùng cho đái tháo đường type 1 (tăng nguy cơ nhiễm toan ceton)",
            "Không dùng nếu eGFR <25 - không hiệu quả",
            "Tăng nguy cơ nhiễm trùng đường tiết niệu và đường sinh dục - vệ sinh tốt, uống nhiều nước",
            "Nguy cơ nhiễm toan ceton (DKA) - đặc biệt ở bệnh nhân type 1, phẫu thuật, bệnh cấp tính, nhịn ăn",
            "Nguy cơ mất nước, hạ huyết áp - đặc biệt ở người cao tuổi, dùng diuretics, suy tim",
            "Tăng nguy cơ hạ đường huyết khi dùng với insulin hoặc sulfonylurea - có thể cần giảm liều",
            "Hoại thư Fournier - hiếm nhưng nguy hiểm, cần chú ý vệ sinh vùng sinh dục",
            "Uống nhiều nước để giảm nguy cơ nhiễm trùng",
            "Có thể dùng bất kỳ lúc nào, không cần ăn",
            "Lợi ích tim mạch và thận độc lập với tác dụng giảm đường huyết"
        ],
        "pharmacokinetics": {
            "half_life": "12.9 giờ",
            "onset": "1 giờ",
            "duration": "24 giờ",
            "protein_binding": "91%",
            "clearance": "Gan: chuyển hóa qua glucuronidation (phần lớn). Thận: bài tiết một phần nguyên dạng và metabolites. Không cần điều chỉnh liều ở suy gan, nhưng không dùng nếu eGFR <25."
        },
        "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm, tránh ánh sáng. Viên nén: bảo quản trong bao bì kín.",
        "black_box_warnings": None,
        "drug_interactions": {
            "major": [
                {
                    "drug": "Insulin, Sulfonylurea (glibenclamide, gliclazide)",
                    "mechanism": "Tác dụng hiệp đồng giảm đường huyết",
                    "effect": "Tăng nguy cơ hạ đường huyết",
                    "management": "Giảm liều insulin hoặc sulfonylurea khi bắt đầu dapagliflozin. Theo dõi đường huyết chặt chẽ."
                },
                {
                    "drug": "Loop diuretics (furosemide, torsemide)",
                    "mechanism": "Tăng bài tiết natri và nước",
                    "effect": "Tăng nguy cơ mất nước, hạ huyết áp, suy thận cấp",
                    "management": "Thận trọng. Theo dõi huyết áp, cân nặng, chức năng thận. Có thể cần giảm liều diuretic."
                }
            ],
            "moderate": [
                {
                    "drug": "Digoxin",
                    "mechanism": "Dapagliflozin có thể tăng nhẹ nồng độ digoxin",
                    "effect": "Tăng nguy cơ độc tính digoxin",
                    "management": "Theo dõi nồng độ digoxin, ECG. Điều chỉnh liều digoxin nếu cần."
                },
                {
                    "drug": "Thiazide diuretics (hydrochlorothiazide)",
                    "mechanism": "Tăng bài tiết natri và nước",
                    "effect": "Tăng nguy cơ mất nước, hạ huyết áp",
                    "management": "Thận trọng. Theo dõi huyết áp, cân nặng."
                }
            ],
            "minor": [
                {
                    "drug": "UDP-glucuronosyltransferase (UGT) inducers",
                    "mechanism": "Có thể giảm nồng độ dapagliflozin",
                    "effect": "Giảm hiệu quả dapagliflozin",
                    "management": "Thận trọng. Theo dõi đường huyết."
                }
            ]
        },
        "contraindications": {
            "absolute": [
                "Đái tháo đường type 1",
                "Nhiễm toan ceton do đái tháo đường",
                "Suy thận nặng (eGFR <25)",
                "Đang lọc máu",
                "Dị ứng dapagliflozin"
            ],
            "relative": [
                "Nhiễm trùng đường tiết niệu tái phát - tăng nguy cơ nhiễm trùng",
                "Suy tim nặng - tăng nguy cơ mất nước",
                "Người cao tuổi - tăng nguy cơ mất nước, hạ huyết áp",
                "Dùng diuretics - tăng nguy cơ mất nước",
                "Nhiễm trùng đường sinh dục tái phát - tăng nguy cơ nhiễm trùng"
            ]
        },
        "pregnancy_lactation": {
            "fda_category": "C",
            "pregnancy_details": "Không có nghiên cứu đầy đủ ở người. Có thể dùng trong thai kỳ nếu lợi ích > nguy cơ. Không nên dùng trong 3 tháng đầu trừ khi thực sự cần thiết. Có thể gây hạ đường huyết ở thai nhi. Theo dõi đường huyết chặt chẽ trong thai kỳ.",
            "lactation": {
                "safety": "Caution",
                "details": "Dapagliflozin bài tiết vào sữa mẹ ở nồng độ thấp. Không có dữ liệu đầy đủ về an toàn ở trẻ bú mẹ.",
                "recommendation": "Thận trọng khi dùng khi cho con bú. Cân nhắc ngừng cho con bú hoặc ngừng thuốc nếu có thể. Nếu cần dùng, theo dõi trẻ chặt chẽ."
            }
        },
        "hepatic_adjustment": {
            "mild": "Không đổi",
            "moderate": "Không đổi",
            "severe": "Không đổi (không chuyển hóa đáng kể qua gan)",
            "notes": "Dapagliflozin chủ yếu chuyển hóa qua glucuronidation ở gan, nhưng không cần điều chỉnh liều ở suy gan nhẹ đến trung bình. Chưa có nghiên cứu đầy đủ ở suy gan nặng."
        },
        "overdose_management": {
            "symptoms": [
                "Hạ đường huyết",
                "Mất nước",
                "Hạ huyết áp",
                "Nhiễm toan ceton (hiếm)"
            ],
            "antidote": "Không có antidote đặc hiệu",
            "treatment": [
                "Điều trị hạ đường huyết: Glucose 15-20g PO hoặc dextrose IV",
                "Bù dịch nếu mất nước, hạ huyết áp",
                "Theo dõi đường huyết, điện giải",
                "Rửa dạ dày nếu uống trong vòng 1-2 giờ",
                "Than hoạt tính không hiệu quả (do không hấp thu qua đường tiêu hóa tốt)",
                "Theo dõi chức năng thận",
                "Nếu có nhiễm toan ceton: điều trị theo protocol DKA"
            ],
            "monitoring": "Đường huyết, huyết áp, cân nặng, chức năng thận, điện giải, dấu hiệu nhiễm toan ceton"
        },
        "reversal_agents": {
            "available": False,
            "agents": []
        },
        "administration_instructions": {
            "oral": {
                "with_food": "Có thể dùng với hoặc không có thức ăn. Không ảnh hưởng đến hấp thu.",
                "timing": "Uống 1 lần/ngày, bất kỳ lúc nào trong ngày. Nên uống vào cùng một thời điểm mỗi ngày để dễ nhớ."
            },
            "iv": {
                "reconstitution": "Không có dạng IV",
                "infusion_rate": "N/A",
                "compatibility": [],
                "incompatibility": [],
                "notes": "Chỉ có dạng uống"
            }
        },
        "references": {
            "primary_sources": [
                "FDA Drug Label - Forxiga (dapagliflozin)",
                "DECLARE-TIMI 58 Study - New England Journal of Medicine",
                "DAPA-HF Study - New England Journal of Medicine",
                "UpToDate - Dapagliflozin: Drug information"
            ],
            "last_updated": "2024-12-19",
            "evidence_level": "High - Multiple large RCTs (DECLARE-TIMI 58, DAPA-HF)"
        }
    },
    "Sitagliptin": {
        "group": "Diabetes - DPP-4 Inhibitor",
        "vietnamese_name": "Sitagliptin, Januvia",
        "administration": ["PO"],
        "indications": [
            "Đái tháo đường type 2"
        ],
        "contraindications": [
            "Đái tháo đường type 1",
            "Nhiễm toan ceton",
            "Dị ứng sitagliptin",
            "Suy thận nặng (CrCl <30)"
        ],
        "dosage": {
            "adult_normal_renal": "100mg x 1 lần/ngày",
            "adult_moderate_renal": "50mg x 1 lần/ngày (CrCl 30-50)",
            "adult_severe_renal": "25mg x 1 lần/ngày (CrCl <30)",
            "notes": "Uống bất kỳ lúc nào. Ít gây hạ đường huyết"
        },
        "renal_adjustment": {
            "normal": "100mg/ngày",
            "30_60": "50mg/ngày (CrCl 30-50)",
            "under_30": "25mg/ngày (CrCl <30)"
        },
        "side_effects": [
            "Nhức đầu",
            "Nhiễm trùng đường hô hấp trên",
            "Viêm tụy cấp (hiếm nhưng nguy hiểm)",
            "Đau khớp nghiêm trọng (hiếm)",
            "Suy tim (tăng nhẹ nguy cơ)"
        ],
        "interactions": [
            "Insulin/Sulfonylurea: có thể tăng nguy cơ hạ đường huyết",
            "Digoxin: tăng nhẹ nồng độ digoxin"
        ],
        "pregnancy": "B",
        "mechanism_of_action": "Sitagliptin là chất ức chế chọn lọc dipeptidyl peptidase-4 (DPP-4), enzyme chịu trách nhiệm phân hủy incretin hormones (GLP-1 và GIP). Bằng cách ức chế DPP-4, sitagliptin làm tăng nồng độ GLP-1 và GIP, các hormone được tiết ra từ ruột non sau khi ăn. GLP-1 và GIP kích thích tiết insulin từ tế bào beta tuyến tụy phụ thuộc vào glucose (chỉ tiết khi đường huyết cao), đồng thời ức chế tiết glucagon từ tế bào alpha tuyến tụy. Điều này dẫn đến giảm đường huyết sau ăn và giảm sản xuất glucose từ gan. Cơ chế này phụ thuộc vào glucose nên ít gây hạ đường huyết so với sulfonylurea. Sitagliptin cũng làm chậm làm rỗng dạ dày và có thể giảm cảm giác thèm ăn nhẹ.",
        "monitoring": [
            "Đường huyết (HbA1c, glucose máu) - đánh giá hiệu quả giảm đường huyết",
            "Chức năng thận (creatinine, CrCl) - cần điều chỉnh liều: CrCl 30-50 → 50mg/ngày, CrCl <30 → 25mg/ngày",
            "Triệu chứng viêm tụy cấp (đau bụng nặng, buồn nôn, nôn) - hiếm nhưng nguy hiểm",
            "Đau khớp nghiêm trọng - hiếm, cần ngừng thuốc nếu xảy ra",
            "Triệu chứng suy tim (khó thở, phù) - tăng nhẹ nguy cơ suy tim",
            "Dấu hiệu phản ứng dị ứng (phát ban, phù mạch) - hiếm",
            "Tác dụng phụ (nhức đầu, nhiễm trùng đường hô hấp trên)"
        ],
        "precautions": [
            "Không dùng cho đái tháo đường type 1 (không hiệu quả)",
            "Cần điều chỉnh liều ở suy thận: CrCl 30-50 → 50mg/ngày, CrCl <30 → 25mg/ngày",
            "Nguy cơ viêm tụy cấp - hiếm nhưng nguy hiểm, ngừng ngay nếu có đau bụng nặng",
            "Nguy cơ đau khớp nghiêm trọng - hiếm, ngừng thuốc nếu xảy ra",
            "Tăng nhẹ nguy cơ suy tim - thận trọng ở bệnh nhân có tiền sử suy tim",
            "Tăng nguy cơ hạ đường huyết khi dùng với insulin hoặc sulfonylurea",
            "Ít gây hạ đường huyết khi dùng đơn độc (do cơ chế phụ thuộc glucose)",
            "Có thể dùng bất kỳ lúc nào, không cần ăn",
            "An toàn trong thai kỳ (category B)",
            "Tương tác nhẹ với digoxin - có thể tăng nồng độ digoxin"
        ],
        "pharmacokinetics": {
            "half_life": "12.4 giờ",
            "onset": "1-2 giờ",
            "duration": "24 giờ",
            "protein_binding": "38%",
            "clearance": "Thận: bài tiết chủ yếu qua thận (79% nguyên dạng, không chuyển hóa). Gan: ít chuyển hóa. Cần điều chỉnh liều ở suy thận."
        },
        "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm, tránh ánh sáng. Viên nén: bảo quản trong bao bì kín.",
        "black_box_warnings": None,
        "drug_interactions": {
            "major": [],
            "moderate": [
                {
                    "drug": "Digoxin",
                    "mechanism": "Sitagliptin có thể tăng nhẹ nồng độ digoxin",
                    "effect": "Tăng nguy cơ độc tính digoxin",
                    "management": "Theo dõi nồng độ digoxin, ECG. Điều chỉnh liều digoxin nếu cần."
                },
                {
                    "drug": "Insulin, Sulfonylurea (glibenclamide, gliclazide)",
                    "mechanism": "Tác dụng hiệp đồng giảm đường huyết",
                    "effect": "Tăng nguy cơ hạ đường huyết",
                    "management": "Thận trọng. Theo dõi đường huyết. Có thể cần giảm liều insulin hoặc sulfonylurea."
                }
            ],
            "minor": [
                {
                    "drug": "CYP3A4 substrates",
                    "mechanism": "Sitagliptin ít chuyển hóa qua CYP, ít tương tác",
                    "effect": "Tương tác tối thiểu",
                    "management": "Không cần điều chỉnh liều"
                }
            ]
        },
        "contraindications": {
            "absolute": [
                "Đái tháo đường type 1",
                "Nhiễm toan ceton do đái tháo đường",
                "Dị ứng sitagliptin",
                "Viêm tụy cấp đang diễn ra"
            ],
            "relative": [
                "Suy thận nặng (CrCl <30) - cần giảm liều (25mg/ngày)",
                "Suy thận trung bình (CrCl 30-50) - cần giảm liều (50mg/ngày)",
                "Tiền sử viêm tụy cấp - tăng nguy cơ",
                "Tiền sử suy tim - tăng nhẹ nguy cơ suy tim",
                "Đau khớp nghiêm trọng - ngừng thuốc nếu xảy ra"
            ]
        },
        "pregnancy_lactation": {
            "fda_category": "B",
            "pregnancy_details": "Không có bằng chứng về nguy cơ gây dị tật thai nhi ở động vật. Có thể dùng trong thai kỳ nếu lợi ích > nguy cơ. Ít dữ liệu ở người, nhưng không có báo cáo về dị tật thai nhi. Theo dõi đường huyết chặt chẽ trong thai kỳ.",
            "lactation": {
                "safety": "Caution",
                "details": "Sitagliptin bài tiết vào sữa mẹ ở nồng độ thấp. Không có dữ liệu đầy đủ về an toàn ở trẻ bú mẹ.",
                "recommendation": "Thận trọng khi dùng khi cho con bú. Cân nhắc ngừng cho con bú hoặc ngừng thuốc nếu có thể. Nếu cần dùng, theo dõi trẻ chặt chẽ."
            }
        },
        "hepatic_adjustment": {
            "mild": "Không đổi",
            "moderate": "Không đổi",
            "severe": "Không đổi (chủ yếu thải qua thận, không phụ thuộc gan)",
            "notes": "Sitagliptin chủ yếu bài tiết qua thận (79% nguyên dạng), không chuyển hóa đáng kể qua gan. Không cần điều chỉnh liều ở suy gan."
        },
        "overdose_management": {
            "symptoms": [
                "Hạ đường huyết (nếu dùng với insulin hoặc sulfonylurea)",
                "Đau bụng, buồn nôn, nôn (dấu hiệu viêm tụy)",
                "Nhức đầu",
                "Đau khớp"
            ],
            "antidote": "Không có antidote đặc hiệu",
            "treatment": [
                "Điều trị hạ đường huyết nếu có: Glucose 15-20g PO hoặc dextrose IV",
                "Rửa dạ dày nếu uống trong vòng 1-2 giờ",
                "Than hoạt tính",
                "Theo dõi đường huyết, chức năng thận",
                "Nếu có dấu hiệu viêm tụy cấp: ngừng thuốc, điều trị hỗ trợ, theo dõi amylase/lipase",
                "Điều trị hỗ trợ"
            ],
            "monitoring": "Đường huyết, chức năng thận, dấu hiệu viêm tụy (đau bụng, amylase/lipase), đau khớp"
        },
        "reversal_agents": {
            "available": False,
            "agents": []
        },
        "administration_instructions": {
            "oral": {
                "with_food": "Có thể dùng với hoặc không có thức ăn. Không ảnh hưởng đến hấp thu.",
                "timing": "Uống 1 lần/ngày, bất kỳ lúc nào trong ngày. Nên uống vào cùng một thời điểm mỗi ngày để dễ nhớ."
            },
            "iv": {
                "reconstitution": "Không có dạng IV",
                "infusion_rate": "N/A",
                "compatibility": [],
                "incompatibility": [],
                "notes": "Chỉ có dạng uống"
            }
        },
        "references": {
            "primary_sources": [
                "FDA Drug Label - Januvia (sitagliptin)",
                "UpToDate - Sitagliptin: Drug information",
                "TECOS Study - New England Journal of Medicine",
                "American Diabetes Association guidelines"
            ],
            "last_updated": "2024-12-19",
            "evidence_level": "High - Multiple RCTs and systematic reviews (TECOS study)"
        }
    },
    "Vildagliptin": {
        "group": "Diabetes - DPP-4 Inhibitor",
        "vietnamese_name": "Vildagliptin, Galvus",
        "administration": ["PO"],
        "indications": [
            "Đái tháo đường type 2"
        ],
        "contraindications": [
            "Đái tháo đường type 1",
            "Nhiễm toan ceton",
            "Suy gan nặng"
        ],
        "dosage": {
            "adult_standard": "50mg x 2 lần/ngày (sáng và tối)",
            "adult_metformin_combination": "50mg x 2 lần/ngày",
            "notes": "Uống với bữa ăn. Ít gây hạ đường huyết"
        },
        "renal_adjustment": {
            "normal": "50mg x 2 lần/ngày",
            "30_60": "50mg x 2 lần/ngày",
            "under_30": "Thận trọng"
        },
        "side_effects": [
            "Nhức đầu",
            "Chóng mặt",
            "Nhiễm trùng đường hô hấp",
            "Viêm tụy cấp (hiếm)",
            "Đau khớp (hiếm)"
        ],
        "interactions": [
            "Insulin/Sulfonylurea: có thể tăng nguy cơ hạ đường huyết"
        ],
        "pregnancy": "C",
        "mechanism_of_action": "Vildagliptin là DPP-4 (dipeptidyl peptidase-4) inhibitor, ức chế enzyme DPP-4 phân hủy incretin hormones (GLP-1 và GIP). Khi DPP-4 bị ức chế, nồng độ GLP-1 và GIP tăng, kích thích tế bào beta tụy tiết insulin (glucose-dependent) và ức chế tế bào alpha tụy tiết glucagon. Kết quả là tăng tiết insulin và giảm glucagon, giảm đường huyết sau ăn và đường huyết đói. Vildagliptin chỉ hoạt động khi đường huyết cao, nên ít gây hạ đường huyết hơn so với sulfonylurea",
        "monitoring": [
            "HbA1c mỗi 3 tháng",
            "Đường huyết đói và sau ăn",
            "Chức năng gan (ALT, AST) trước và trong điều trị (nguy cơ viêm tụy cấp)",
            "Dấu hiệu viêm tụy cấp (đau bụng, nôn - hiếm nhưng nguy hiểm)",
            "Chức năng thận (creatinine, eGFR) định kỳ"
        ],
        "precautions": [
            "Uống với bữa ăn (tăng hấp thu)",
            "Ít gây hạ đường huyết hơn sulfonylurea (glucose-dependent)",
            "Có thể dùng kết hợp với metformin, sulfonylurea, hoặc insulin",
            "Ngừng ngay nếu có dấu hiệu viêm tụy cấp (hiếm nhưng nguy hiểm)",
            "Có thể dùng trong thai kỳ (category C)",
            "Thận trọng nếu suy thận nặng (CrCl <30)",
            "Có thể tăng nguy cơ hạ đường huyết khi dùng với insulin/sulfonylurea"
        ],
        "pharmacokinetics": {
            "half_life": "2-3 giờ (ngắn)",
            "onset": "2-4 tuần (giảm HbA1c)",
            "duration": "12-24 giờ",
            "protein_binding": "9%",
            "clearance": "Thận (thải trừ chủ yếu), gan (chuyển hóa)"
        },
        "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm",
        "black_box_warnings": "Có thể gây viêm tụy cấp hiếm nhưng nguy hiểm. Ngừng ngay nếu có dấu hiệu viêm tụy cấp (đau bụng, nôn)"
    },
    "Pioglitazone": {
        "group": "Diabetes - Thiazolidinedione (TZD)",
        "vietnamese_name": "Pioglitazone, Actos",
        "administration": ["PO"],
        "indications": [
            "Đái tháo đường type 2"
        ],
        "contraindications": [
            "Đái tháo đường type 1",
            "Suy tim (NYHA class III-IV)",
            "Bệnh gan nặng",
            "Ung thư bàng quang",
            "Gãy xương (phụ nữ có nguy cơ)"
        ],
        "dosage": {
            "adult_start": "15-30mg x 1 lần/ngày",
            "adult_usual": "15-45mg x 1 lần/ngày",
            "adult_max": "45mg/ngày",
            "notes": "Uống bất kỳ lúc nào. Tác dụng chậm (2-4 tuần). Gây giữ nước"
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "Không đổi",
            "under_30": "Thận trọng"
        },
        "side_effects": [
            "Giữ nước, phù (tăng nguy cơ suy tim)",
            "Tăng cân",
            "Gãy xương (phụ nữ có nguy cơ tăng)",
            "Thiếu máu",
            "Tăng LDL cholesterol",
            "Ung thư bàng quang (tăng nhẹ nguy cơ)"
        ],
        "interactions": [
            "Insulin: tăng nguy cơ suy tim, phù",
            "Digoxin: có thể tăng nồng độ digoxin"
        ],
        "pregnancy": "C",
        "mechanism_of_action": "Pioglitazone là thiazolidinedione (TZD), hoạt động như agonist của PPAR-gamma (peroxisome proliferator-activated receptor gamma). Khi gắn vào PPAR-gamma trong nhân tế bào, pioglitazone kích hoạt phiên mã các gen liên quan đến chuyển hóa glucose và lipid, tăng nhạy cảm với insulin ở mô ngoại vi (cơ, mỡ, gan). Thuốc giảm đề kháng insulin, tăng sử dụng glucose ở mô ngoại vi, giảm sản xuất glucose ở gan, và giảm giải phóng acid béo tự do từ mô mỡ. Tác dụng chậm (2-4 tuần), và có thể gây giữ nước, tăng cân",
        "monitoring": [
            "HbA1c mỗi 3 tháng",
            "Đường huyết đói",
            "Chức năng gan (ALT, AST) trước và trong 12 tháng đầu (nguy cơ độc gan)",
            "Dấu hiệu suy tim (khó thở, phù, tăng cân) - đặc biệt khi dùng với insulin",
            "Dấu hiệu gãy xương (đặc biệt ở phụ nữ)",
            "Công thức máu (thiếu máu)",
            "Lipid (LDL cholesterol có thể tăng)",
            "Ung thư bàng quang (tăng nhẹ nguy cơ - cần theo dõi)"
        ],
        "precautions": [
            "Không dùng nếu suy tim (NYHA class III-IV)",
            "Ngừng ngay nếu có dấu hiệu suy tim",
            "Tránh dùng với insulin nếu có thể (tăng nguy cơ suy tim, phù)",
            "Tác dụng chậm (2-4 tuần) - cần kiên nhẫn",
            "Có thể gây giữ nước và phù (tăng nguy cơ suy tim)",
            "Có thể gây tăng cân",
            "Tăng nguy cơ gãy xương ở phụ nữ (cần theo dõi)",
            "Tăng nhẹ nguy cơ ung thư bàng quang (cần theo dõi)",
            "Ngừng nếu ALT >3x ULN (nguy cơ độc gan)",
            "Có thể dùng trong thai kỳ (category C)"
        ],
        "pharmacokinetics": {
            "half_life": "16-24 giờ (dài)",
            "onset": "2-4 tuần (giảm HbA1c)",
            "duration": "24 giờ",
            "protein_binding": ">99%",
            "clearance": "Gan (chuyển hóa qua CYP2C8, CYP3A4), thận (thải trừ)"
        },
        "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm",
        "black_box_warnings": "Có thể gây suy tim hoặc làm trầm trọng suy tim hiện có. Không dùng nếu suy tim (NYHA class III-IV). Ngừng ngay nếu có dấu hiệu suy tim. Có thể gây độc gan - ngừng nếu ALT >3x ULN"
    },
}

__all__ = ['DIABETES_DRUGS']
