"""Diabetes Medications
Active module - contains all diabetes drug data"""

# Meglitinides (Glinides)

MEGLITINIDES_DRUGS = {
    "Nateglinide": {
        "group": "Diabetes - Meglitinide (Glinide)",
        "vietnamese_name": "Nateglinide, Starlix",
        "administration": ["PO"],
        "indications": [
            "Đái tháo đường type 2",
            "Kết hợp với metformin"
        ],
        "contraindications": [
            "Đái tháo đường type 1",
            "Nhiễm toan ceton do đái tháo đường",
            "Suy gan nặng",
            "Có thai"
        ],
        "dosage": {
            "adult_start": "60-120mg trước mỗi bữa ăn chính",
            "adult_usual": "60-120mg trước mỗi bữa ăn chính",
            "adult_max": "360mg/ngày (120mg x 3 bữa)",
            "notes": "Uống 1-30 phút trước mỗi bữa ăn. Bỏ liều nếu bỏ bữa. Tác dụng nhanh nhất trong các meglitinides."
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "Không đổi",
            "under_30": "Không đổi"
        },
        "side_effects": [
            "Hạ đường huyết (phổ biến, nhưng ít nghiêm trọng hơn sulfonylureas)",
            "Tăng cân (nhẹ)",
            "Rối loạn tiêu hóa",
            "Ban da (hiếm)"
        ],
        "interactions": [
            "Rifampin: giảm nồng độ nateglinide",
            "Rượu: tăng nguy cơ hạ đường huyết"
        ],
        "pregnancy": "C - Tránh dùng trong thai kỳ",
        "mechanism_of_action": "Nateglinide là meglitinide (glinide), kích thích tế bào beta tuyến tụy tiết insulin. Nateglinide gắn vào SUR1 trên kênh KATP ở màng tế bào beta, làm đóng kênh KATP, khử cực màng tế bào, mở kênh canxi, và kích thích giải phóng insulin. Nateglinide có tác dụng nhanh nhất trong các meglitinides (1-30 phút) và thời gian bán thải ngắn (1.5 giờ), nên chỉ kích thích tiết insulin trong bữa ăn và giảm nguy cơ hạ đường huyết giữa các bữa ăn. Nateglinide được chuyển hóa chủ yếu qua CYP2C9 và CYP3A4, nhưng ít tương tác hơn repaglinide.",
        "monitoring": [
            "Đường huyết: HbA1c (mỗi 3 tháng), đường huyết đói, đường huyết sau ăn",
            "Dấu hiệu hạ đường huyết: run, vã mồ hôi, nhịp tim nhanh, đói, lú lẫn",
            "Đường huyết khi nghi ngờ hạ đường huyết",
            "Cân nặng - có thể gây tăng cân nhẹ",
            "Chức năng gan (ALT, AST) - suy gan tăng nguy cơ hạ đường huyết"
        ],
        "precautions": [
            "Hạ đường huyết là tác dụng phụ phổ biến nhất - bệnh nhân cần biết dấu hiệu và cách xử trí",
            "Uống 1-30 phút TRƯỚC mỗi bữa ăn chính - không uống nếu bỏ bữa",
            "Bỏ liều nếu bỏ bữa - giảm nguy cơ hạ đường huyết",
            "Nguy cơ hạ đường huyết thấp hơn sulfonylureas (thời gian bán thải ngắn)",
            "Nguy cơ tăng ở: suy gan, bỏ bữa, uống rượu",
            "CHỐNG CHỈ ĐỊNH ở suy gan nặng",
            "Tránh rượu - tăng nguy cơ hạ đường huyết",
            "Có thể tăng cân nhẹ - cần tư vấn chế độ ăn và tập luyện",
            "Không dùng trong thai kỳ",
            "Bắt đầu với liều thấp (60mg/bữa) và tăng dần"
        ],
        "pharmacokinetics": {
            "half_life": "1.5 giờ (rất ngắn)",
            "onset": "1-30 phút (nhanh nhất trong meglitinides)",
            "duration": "2-4 giờ",
            "protein_binding": ">98%",
            "clearance": "Gan: chuyển hóa qua CYP2C9 và CYP3A4 thành metabolites không hoạt động. Thận: bài tiết một phần. Thời gian bán thải rất ngắn → chỉ kích thích tiết insulin trong bữa ăn, giảm nguy cơ hạ đường huyết giữa các bữa ăn."
        },
        "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm, tránh ánh sáng",
        "black_box_warnings": "Nguy cơ hạ đường huyết nghiêm trọng, có thể gây tử vong. Nguy cơ tăng ở suy gan, bỏ bữa, uống rượu. Bệnh nhân cần biết dấu hiệu và cách xử trí hạ đường huyết. Không dùng ở đái tháo đường type 1 hoặc nhiễm toan ceton. CHỐNG CHỈ ĐỊNH ở suy gan nặng.",
        "drug_interactions": {
            "major": [
                {
                    "drug": "Rượu (ethanol)",
                    "mechanism": "Ức chế sản xuất glucose ở gan, tăng nguy cơ hạ đường huyết",
                    "effect": "Hạ đường huyết nghiêm trọng",
                    "management": "TRÁNH RƯỢU hoàn toàn khi dùng nateglinide."
                }
            ],
            "moderate": [
                {
                    "drug": "Rifampin",
                    "mechanism": "Cảm ứng CYP2C9 và CYP3A4, tăng chuyển hóa nateglinide",
                    "effect": "Giảm nồng độ nateglinide, giảm hiệu quả",
                    "management": "Có thể cần tăng liều nateglinide. Theo dõi đường huyết."
                }
            ],
            "minor": []
        },
        "contraindications": {
            "tuyệt_đối": [
                "Đái tháo đường type 1",
                "Nhiễm toan ceton do đái tháo đường",
                "Dị ứng nateglinide",
                "Suy gan nặng - CHỐNG CHỈ ĐỊNH"
            ],
            "tương_đối": [
                "Suy gan nhẹ-trung bình - thận trọng, có thể cần giảm liều",
                "Người cao tuổi - thận trọng",
                "Có thai - có thể gây hạ đường huyết ở trẻ sơ sinh",
                "Bỏ bữa thường xuyên - tăng nguy cơ hạ đường huyết",
                "Uống rượu - tăng nguy cơ hạ đường huyết nghiêm trọng"
            ]
        },
        "pregnancy_lactation": {
            "fda_category": "C",
            "pregnancy_details": "Có thể dùng trong thai kỳ nếu lợi ích > nguy cơ, nhưng THƯỜNG TRÁNH DÙNG. Meglitinides có thể gây hạ đường huyết ở trẻ sơ sinh. Insulin là lựa chọn ưu tiên trong thai kỳ.",
            "lactation": {
                "safety": "Compatible",
                "details": "Nateglinide bài tiết vào sữa mẹ ở nồng độ thấp. Ít có nguy cơ gây hạ đường huyết ở trẻ bú mẹ.",
                "recommendation": "Có thể dùng khi cho con bú với theo dõi chặt chẽ."
            }
        },
        "hepatic_adjustment": {
            "mild": "Thận trọng, có thể cần giảm liều",
            "moderate": "Thận trọng, giảm liều",
            "severe": "CHỐNG CHỈ ĐỊNH",
            "notes": "Nateglinide chuyển hóa ở gan qua CYP2C9 và CYP3A4. Suy gan làm giảm chuyển hóa, tăng nồng độ, tăng nguy cơ hạ đường huyết. CHỐNG CHỈ ĐỊNH ở suy gan nặng."
        },
        "overdose_management": {
            "symptoms": [
                "Hạ đường huyết nghiêm trọng: run, vã mồ hôi, nhịp tim nhanh, đói, lú lẫn, co giật, hôn mê",
                "Có thể gây tử vong nếu không điều trị"
            ],
            "antidote": "Glucose (đường uống hoặc IV)",
            "treatment": [
                "Nếu tỉnh táo: uống nước đường, nước ngọt, hoặc glucose 15-20g",
                "Nếu không tỉnh táo: glucose 50% 50ml IV hoặc glucagon 1mg IM/SC",
                "Theo dõi đường huyết liên tục",
                "Có thể cần truyền glucose liên tục nếu hạ đường huyết kéo dài",
                "Theo dõi tại bệnh viện ít nhất 24 giờ"
            ],
            "monitoring": "Đường huyết liên tục, dấu hiệu sinh tồn, dấu hiệu hạ đường huyết"
        },
        "reversal_agents": {
            "available": True,
            "agents": [
                {
                    "name": "Glucose",
                    "route": "PO hoặc IV",
                    "dose": "15-20g PO (nếu tỉnh táo) hoặc 50% 50ml IV (nếu không tỉnh táo)",
                    "notes": "Điều trị hạ đường huyết do nateglinide"
                },
                {
                    "name": "Glucagon",
                    "route": "IM hoặc SC",
                    "dose": "1mg IM/SC",
                    "notes": "Nếu không có đường tĩnh mạch"
                }
            ]
        },
        "administration_instructions": {
            "oral": {
                "with_food": "Uống 1-30 phút TRƯỚC mỗi bữa ăn chính (không uống với thức ăn)",
                "timing": "Uống 1-30 phút trước mỗi bữa ăn chính. Bỏ liều nếu bỏ bữa. Tối đa 120mg/bữa, tối đa 360mg/ngày (3 bữa)."
            }
        },
        "references": {
            "primary_sources": [
                "FDA Drug Label - Nateglinide (Starlix)",
                "UpToDate - Nateglinide: Drug Information",
                "American Diabetes Association guidelines",
                "Goodman & Gilman's The Pharmacological Basis of Therapeutics"
            ],
            "last_updated": "2025-02-05",
            "evidence_level": "High - FDA approved, multiple RCTs"
        }
    },
    "Repaglinide": {
        "group": "Diabetes - Meglitinide (Glinide)",
        "vietnamese_name": "Repaglinide, Prandin",
        "administration": ["PO"],
        "indications": [
            "Đái tháo đường type 2",
            "Kết hợp với metformin"
        ],
        "contraindications": [
            "Đái tháo đường type 1",
            "Nhiễm toan ceton do đái tháo đường",
            "Suy gan nặng",
            "Có thai"
        ],
        "dosage": {
            "adult_start": "0.5mg trước mỗi bữa ăn chính (tối đa 4mg/bữa)",
            "adult_usual": "0.5-4mg trước mỗi bữa ăn chính",
            "adult_max": "16mg/ngày (4mg x 4 bữa)",
            "notes": "Uống 15-30 phút trước mỗi bữa ăn. Bỏ liều nếu bỏ bữa. Tác dụng nhanh, thời gian bán thải ngắn."
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "Không đổi",
            "under_30": "Khởi đầu 0.5mg/bữa, tăng dần"
        },
        "side_effects": [
            "Hạ đường huyết (phổ biến, nhưng ít nghiêm trọng hơn sulfonylureas)",
            "Tăng cân (nhẹ)",
            "Rối loạn tiêu hóa",
            "Ban da (hiếm)"
        ],
        "interactions": [
            "Gemfibrozil: tăng nồng độ repaglinide đáng kể (tránh dùng chung)",
            "Clarithromycin: tăng nồng độ repaglinide",
            "Rifampin: giảm nồng độ repaglinide",
            "Rượu: tăng nguy cơ hạ đường huyết"
        ],
        "pregnancy": "C - Tránh dùng trong thai kỳ",
        "mechanism_of_action": "Repaglinide là meglitinide (glinide), kích thích tế bào beta tuyến tụy tiết insulin. Repaglinide gắn vào SUR1 trên kênh KATP ở màng tế bào beta, làm đóng kênh KATP, khử cực màng tế bào, mở kênh canxi, và kích thích giải phóng insulin. Khác với sulfonylureas, repaglinide có tác dụng nhanh (15-30 phút) và thời gian bán thải ngắn (1 giờ), nên chỉ kích thích tiết insulin trong bữa ăn và giảm nguy cơ hạ đường huyết giữa các bữa ăn. Repaglinide được chuyển hóa chủ yếu qua CYP3A4 và CYP2C8, nên có tương tác với các thuốc ức chế hoặc cảm ứng các enzyme này.",
        "monitoring": [
            "Đường huyết: HbA1c (mỗi 3 tháng), đường huyết đói, đường huyết sau ăn",
            "Dấu hiệu hạ đường huyết: run, vã mồ hôi, nhịp tim nhanh, đói, lú lẫn",
            "Đường huyết khi nghi ngờ hạ đường huyết",
            "Cân nặng - có thể gây tăng cân nhẹ",
            "Chức năng gan (ALT, AST) - suy gan tăng nguy cơ hạ đường huyết"
        ],
        "precautions": [
            "Hạ đường huyết là tác dụng phụ phổ biến nhất - bệnh nhân cần biết dấu hiệu và cách xử trí",
            "Uống 15-30 phút TRƯỚC mỗi bữa ăn chính - không uống nếu bỏ bữa",
            "Bỏ liều nếu bỏ bữa - giảm nguy cơ hạ đường huyết",
            "Nguy cơ hạ đường huyết thấp hơn sulfonylureas (thời gian bán thải ngắn)",
            "Nguy cơ tăng ở: suy gan, bỏ bữa, uống rượu",
            "CHỐNG CHỈ ĐỊNH ở suy gan nặng",
            "Tránh rượu - tăng nguy cơ hạ đường huyết",
            "CHỐNG CHỈ ĐỊNH với gemfibrozil (tăng nồng độ repaglinide đáng kể)",
            "Có thể tăng cân nhẹ - cần tư vấn chế độ ăn và tập luyện",
            "Không dùng trong thai kỳ",
            "Bắt đầu với liều thấp (0.5mg/bữa) và tăng dần"
        ],
        "pharmacokinetics": {
            "half_life": "1 giờ (rất ngắn)",
            "onset": "15-30 phút",
            "duration": "2-4 giờ",
            "protein_binding": ">98%",
            "clearance": "Gan: chuyển hóa qua CYP3A4 và CYP2C8 thành metabolites không hoạt động. Thận: bài tiết một phần. Thời gian bán thải rất ngắn → chỉ kích thích tiết insulin trong bữa ăn, giảm nguy cơ hạ đường huyết giữa các bữa ăn."
        },
        "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm, tránh ánh sáng",
        "black_box_warnings": "Nguy cơ hạ đường huyết nghiêm trọng, có thể gây tử vong. Nguy cơ tăng ở suy gan, bỏ bữa, uống rượu. Bệnh nhân cần biết dấu hiệu và cách xử trí hạ đường huyết. Không dùng ở đái tháo đường type 1 hoặc nhiễm toan ceton. CHỐNG CHỈ ĐỊNH ở suy gan nặng. CHỐNG CHỈ ĐỊNH với gemfibrozil.",
        "drug_interactions": {
            "major": [
                {
                    "drug": "Gemfibrozil",
                    "mechanism": "Gemfibrozil ức chế CYP2C8 mạnh, tăng nồng độ repaglinide đáng kể",
                    "effect": "Tăng nồng độ repaglinide 8-10 lần, tăng nguy cơ hạ đường huyết nghiêm trọng",
                    "management": "CHỐNG CHỈ ĐỊNH dùng cùng. Tránh dùng repaglinide với gemfibrozil."
                },
                {
                    "drug": "Clarithromycin, Erythromycin",
                    "mechanism": "Macrolide ức chế CYP3A4, tăng nồng độ repaglinide",
                    "effect": "Tăng nguy cơ hạ đường huyết",
                    "management": "Thận trọng. Theo dõi đường huyết chặt chẽ. Có thể cần giảm liều repaglinide."
                },
                {
                    "drug": "Rượu (ethanol)",
                    "mechanism": "Ức chế sản xuất glucose ở gan, tăng nguy cơ hạ đường huyết",
                    "effect": "Hạ đường huyết nghiêm trọng",
                    "management": "TRÁNH RƯỢU hoàn toàn khi dùng repaglinide."
                }
            ],
            "moderate": [
                {
                    "drug": "Rifampin",
                    "mechanism": "Cảm ứng CYP3A4 và CYP2C8, tăng chuyển hóa repaglinide",
                    "effect": "Giảm nồng độ repaglinide, giảm hiệu quả",
                    "management": "Có thể cần tăng liều repaglinide. Theo dõi đường huyết."
                },
                {
                    "drug": "Ketoconazole, Itraconazole",
                    "mechanism": "Ức chế CYP3A4, tăng nồng độ repaglinide",
                    "effect": "Tăng nguy cơ hạ đường huyết",
                    "management": "Thận trọng. Theo dõi đường huyết. Có thể cần giảm liều repaglinide."
                }
            ],
            "minor": []
        },
        "contraindications": {
            "tuyệt_đối": [
                "Đái tháo đường type 1",
                "Nhiễm toan ceton do đái tháo đường",
                "Dị ứng repaglinide",
                "Suy gan nặng - CHỐNG CHỈ ĐỊNH",
                "Dùng với gemfibrozil - CHỐNG CHỈ ĐỊNH"
            ],
            "tương_đối": [
                "Suy gan nhẹ-trung bình - thận trọng, có thể cần giảm liều",
                "Người cao tuổi - thận trọng",
                "Có thai - có thể gây hạ đường huyết ở trẻ sơ sinh",
                "Bỏ bữa thường xuyên - tăng nguy cơ hạ đường huyết",
                "Uống rượu - tăng nguy cơ hạ đường huyết nghiêm trọng"
            ]
        },
        "pregnancy_lactation": {
            "fda_category": "C",
            "pregnancy_details": "Có thể dùng trong thai kỳ nếu lợi ích > nguy cơ, nhưng THƯỜNG TRÁNH DÙNG. Meglitinides có thể gây hạ đường huyết ở trẻ sơ sinh. Insulin là lựa chọn ưu tiên trong thai kỳ.",
            "lactation": {
                "safety": "Compatible",
                "details": "Repaglinide bài tiết vào sữa mẹ ở nồng độ thấp. Ít có nguy cơ gây hạ đường huyết ở trẻ bú mẹ.",
                "recommendation": "Có thể dùng khi cho con bú với theo dõi chặt chẽ."
            }
        },
        "hepatic_adjustment": {
            "mild": "Thận trọng, có thể cần giảm liều",
            "moderate": "Thận trọng, giảm liều",
            "severe": "CHỐNG CHỈ ĐỊNH",
            "notes": "Repaglinide chuyển hóa ở gan qua CYP3A4 và CYP2C8. Suy gan làm giảm chuyển hóa, tăng nồng độ, tăng nguy cơ hạ đường huyết. CHỐNG CHỈ ĐỊNH ở suy gan nặng."
        },
        "overdose_management": {
            "symptoms": [
                "Hạ đường huyết nghiêm trọng: run, vã mồ hôi, nhịp tim nhanh, đói, lú lẫn, co giật, hôn mê",
                "Có thể gây tử vong nếu không điều trị"
            ],
            "antidote": "Glucose (đường uống hoặc IV)",
            "treatment": [
                "Nếu tỉnh táo: uống nước đường, nước ngọt, hoặc glucose 15-20g",
                "Nếu không tỉnh táo: glucose 50% 50ml IV hoặc glucagon 1mg IM/SC",
                "Theo dõi đường huyết liên tục",
                "Có thể cần truyền glucose liên tục nếu hạ đường huyết kéo dài",
                "Theo dõi tại bệnh viện ít nhất 24 giờ"
            ],
            "monitoring": "Đường huyết liên tục, dấu hiệu sinh tồn, dấu hiệu hạ đường huyết"
        },
        "reversal_agents": {
            "available": True,
            "agents": [
                {
                    "name": "Glucose",
                    "route": "PO hoặc IV",
                    "dose": "15-20g PO (nếu tỉnh táo) hoặc 50% 50ml IV (nếu không tỉnh táo)",
                    "notes": "Điều trị hạ đường huyết do repaglinide"
                },
                {
                    "name": "Glucagon",
                    "route": "IM hoặc SC",
                    "dose": "1mg IM/SC",
                    "notes": "Nếu không có đường tĩnh mạch"
                }
            ]
        },
        "administration_instructions": {
            "oral": {
                "with_food": "Uống 15-30 phút TRƯỚC mỗi bữa ăn chính (không uống với thức ăn)",
                "timing": "Uống 15-30 phút trước mỗi bữa ăn chính. Bỏ liều nếu bỏ bữa. Tối đa 4mg/bữa, tối đa 16mg/ngày (4 bữa)."
            }
        },
        "references": {
            "primary_sources": [
                "FDA Drug Label - Repaglinide (Prandin)",
                "UpToDate - Repaglinide: Drug Information",
                "American Diabetes Association guidelines",
                "Goodman & Gilman's The Pharmacological Basis of Therapeutics"
            ],
            "last_updated": "2025-02-05",
            "evidence_level": "High - FDA approved, multiple RCTs"
        }
    },
    
}

__all__ = ['MEGLITINIDES_DRUGS']


