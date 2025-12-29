"""
Dermatology - Topical Medications
"""

DERMATOLOGY_DRUGS = {
    "Clobetasol": {
        "group": "Dermatology - Topical Corticosteroid (Ultra-high Potency)",
        "vietnamese_name": "Clobetasol, Clobex, Temovate",
        "administration": ["Topical", "Scalp"],
        "indications": [
            "Viêm da dị ứng (atopic dermatitis) nặng",
            "Vảy nến (psoriasis) nặng",
            "Lichen planus",
            "Lichen sclerosus",
            "Viêm da tiếp xúc (contact dermatitis) nặng",
            "Eczema nặng"
        ],
        "contraindications": [
            "Dị ứng clobetasol hoặc corticosteroid",
            "Nhiễm trùng da (bacterial, fungal, viral) - không dùng trừ khi có kháng sinh/kháng nấm",
            "Loét da",
            "Trẻ em <12 tuổi (thận trọng)",
            "Phụ nữ có thai (thận trọng, tránh dùng diện rộng)"
        ],
        "dosage": {
            "adult_topical": "Bôi mỏng 1-2 lần/ngày lên vùng da bị ảnh hưởng",
            "adult_scalp": "Bôi lên da đầu 1-2 lần/ngày",
            "adult_max_duration": "Tối đa 2 tuần liên tục (tránh dùng kéo dài)",
            "notes": "Clobetasol là corticosteroid mạnh nhất (ultra-high potency). Chỉ dùng cho tổn thương nặng, diện tích nhỏ. Tránh dùng trên mặt, nách, bẹn (da mỏng, hấp thu cao). Không dùng >2 tuần liên tục."
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "Không đổi",
            "under_30": "Không đổi"
        },
        "side_effects": [
            "Teo da (skin atrophy) - phổ biến nếu dùng kéo dài",
            "Giãn mạch (telangiectasia)",
            "Rạn da (striae)",
            "Mụn trứng cá (acne)",
            "Viêm nang lông (folliculitis)",
            "Nhiễm trùng da thứ phát (bacterial, fungal)",
            "Ức chế trục HPA (nếu dùng diện rộng, kéo dài)",
            "Hấp thu toàn thân (nếu dùng diện rộng, kéo dài)"
        ],
        "interactions": [
            "Không có tương tác đáng kể với thuốc khác (topical)"
        ],
        "pregnancy": "C - Thận trọng, tránh dùng diện rộng",
        "mechanism_of_action": "Clobetasol là corticosteroid tổng hợp, ultra-high potency (nhóm I - mạnh nhất). Gắn với thụ thể glucocorticoid trong tế bào, điều hòa biểu hiện gen, dẫn đến: (1) Ức chế viêm (giảm cytokine, chemokine, adhesion molecules), (2) Ức chế miễn dịch (giảm T-cell activation, cytokine production), (3) Co mạch (giảm đỏ, sưng), (4) Ức chế tăng sinh tế bào (giảm vảy nến). Clobetasol có độ mạnh cao nhất trong các corticosteroid tại chỗ, hiệu quả nhanh và mạnh, nhưng nguy cơ tác dụng phụ cao (teo da, ức chế HPA). ĐẶC ĐIỂM: (1) Ultra-high potency (nhóm I), (2) Chỉ dùng cho tổn thương nặng, diện tích nhỏ, (3) Không dùng >2 tuần liên tục, (4) Tránh dùng trên mặt, nách, bẹn, (5) Nguy cơ hấp thu toàn thân nếu dùng diện rộng, kéo dài.",
        "monitoring": [
            "Đáp ứng lâm sàng (giảm đỏ, sưng, ngứa)",
            "Dấu hiệu teo da (da mỏng, nhăn, giãn mạch)",
            "Dấu hiệu nhiễm trùng da (mủ, đỏ, sưng tăng)",
            "Dấu hiệu ức chế HPA (nếu dùng diện rộng, kéo dài): mệt mỏi, hạ huyết áp, hạ đường huyết",
            "Diện tích da điều trị (tránh >20% diện tích cơ thể)"
        ],
        "precautions": [
            "Clobetasol là corticosteroid mạnh nhất - chỉ dùng cho tổn thương nặng, diện tích nhỏ",
            "KHÔNG dùng >2 tuần liên tục (nguy cơ teo da, ức chế HPA)",
            "Tránh dùng trên mặt, nách, bẹn (da mỏng, hấp thu cao)",
            "Tránh dùng trên vùng da bị loét, nhiễm trùng",
            "Nếu cần dùng kéo dài: giảm tần suất (q2-3 ngày) hoặc chuyển sang corticosteroid yếu hơn",
            "Nguy cơ hấp thu toàn thân nếu dùng diện rộng (>20% diện tích cơ thể) hoặc kéo dài",
            "Trẻ em: thận trọng, giảm liều, tránh dùng kéo dài",
            "Phụ nữ có thai: thận trọng, tránh dùng diện rộng",
            "Bảo vệ khỏi ánh nắng mặt trời (nhạy cảm ánh sáng)"
        ],
        "pharmacokinetics": {
            "half_life": "Không áp dụng (topical)",
            "onset": "Vài ngày đến 1 tuần",
            "duration": "Phụ thuộc tần suất dùng",
            "protein_binding": "Không áp dụng (topical)",
            "metabolism": "Chuyển hóa tại da và gan (nếu hấp thu toàn thân)",
            "clearance": "Thải trừ qua nước tiểu (nếu hấp thu toàn thân)"
        },
        "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm, tránh ánh sáng. Đóng nắp kín sau khi dùng.",
        "black_box_warnings": None,
        "drug_interactions": {
            "major": [],
            "moderate": [],
            "minor": []
        },
        "contraindications": {
            "tuyệt_đối": [
                "Dị ứng clobetasol hoặc corticosteroid",
                "Nhiễm trùng da (bacterial, fungal, viral) - không dùng trừ khi có kháng sinh/kháng nấm",
                "Loét da"
            ],
            "tương_đối": [
                "Trẻ em <12 tuổi - thận trọng, giảm liều, tránh dùng kéo dài",
                "Phụ nữ có thai - thận trọng, tránh dùng diện rộng",
                "Da mỏng (mặt, nách, bẹn) - tránh dùng (hấp thu cao)",
                "Dùng diện rộng (>20% diện tích cơ thể) - nguy cơ hấp thu toàn thân",
                "Dùng kéo dài (>2 tuần) - nguy cơ teo da, ức chế HPA"
            ]
        },
        "pregnancy_lactation": {
            "fda_category": "C",
            "pregnancy_details": "Clobetasol là thuốc phân loại C. Corticosteroid tại chỗ có thể hấp thu toàn thân, đặc biệt khi dùng diện rộng hoặc kéo dài. Corticosteroid có thể qua nhau thai và có thể gây ức chế thượng thận ở thai nhi. Tránh dùng diện rộng hoặc kéo dài trong thai kỳ. Chỉ dùng khi lợi ích vượt quá nguy cơ, đặc biệt trong tam cá nguyệt thứ nhất.",
            "lactation": {
                "safety": "Compatible with Caution",
                "details": "Clobetasol có thể hấp thu toàn thân và bài tiết vào sữa mẹ ở nồng độ thấp. Tuy nhiên, nồng độ trong sữa mẹ thấp và không có báo cáo về tác dụng phụ đáng kể ở trẻ bú mẹ khi dùng tại chỗ với diện tích nhỏ.",
                "recommendation": "Có thể dùng khi cho con bú, nhưng thận trọng. Tránh dùng diện rộng hoặc kéo dài. Tránh bôi lên vú hoặc núm vú."
            }
        },
        "hepatic_adjustment": {
            "mild": "Không cần điều chỉnh liều",
            "moderate": "Không cần điều chỉnh liều",
            "severe": "Không cần điều chỉnh liều (topical, hấp thu tối thiểu)",
            "notes": "Clobetasol dùng tại chỗ, hấp thu toàn thân tối thiểu. Không cần điều chỉnh liều ở bệnh nhân suy gan."
        },
        "overdose_management": {
            "symptoms": [
                "Teo da nặng",
                "Ức chế trục HPA (mệt mỏi, hạ huyết áp, hạ đường huyết)",
                "Hấp thu toàn thân (nếu dùng diện rộng, kéo dài)"
            ],
            "antidote": "Không có antidote đặc hiệu. Ngừng thuốc, điều trị hỗ trợ.",
            "treatment": [
                "Ngừng ngay clobetasol",
                "Nếu ức chế HPA:",
                "  - Hydrocortisone thay thế nếu cần",
                "  - Theo dõi huyết áp, đường huyết",
                "Nếu teo da:",
                "  - Ngừng thuốc, chờ hồi phục (có thể mất vài tháng)",
                "  - Dưỡng ẩm da",
                "Theo dõi: Dấu hiệu sinh tồn, chức năng thượng thận"
            ],
            "monitoring": "Theo dõi dấu hiệu sinh tồn, chức năng thượng thận (nếu có ức chế HPA) cho đến khi hồi phục."
        },
        "reversal_agents": None,
        "administration_instructions": {
            "oral": None,
            "topical": {
                "preparation": "Dạng cream, ointment, lotion, gel, foam, shampoo. Chọn dạng phù hợp với vị trí và loại tổn thương.",
                "application": "Bôi mỏng 1-2 lần/ngày lên vùng da bị ảnh hưởng. Massage nhẹ cho đến khi thấm. Rửa tay sau khi bôi.",
                "area": "Chỉ bôi lên vùng da bị ảnh thương. Tránh bôi lên vùng da lành, mặt, nách, bẹn.",
                "duration": "Tối đa 2 tuần liên tục. Nếu cần dùng kéo dài: giảm tần suất (q2-3 ngày) hoặc chuyển sang corticosteroid yếu hơn.",
                "notes": "QUAN TRỌNG: 1) Chỉ dùng cho tổn thương nặng, diện tích nhỏ, 2) KHÔNG dùng >2 tuần liên tục, 3) Tránh dùng trên mặt, nách, bẹn, 4) Tránh bôi lên vùng da bị loét, nhiễm trùng, 5) Bảo vệ khỏi ánh nắng mặt trời."
            },
            "scalp": {
                "preparation": "Dạng lotion, foam, shampoo.",
                "application": "Bôi lên da đầu 1-2 lần/ngày. Massage nhẹ cho đến khi thấm.",
                "notes": "Dùng cho vảy nến da đầu, viêm da tiết bã. Tránh dùng >2 tuần liên tục."
            }
        },
        "references": {
            "primary_sources": [
                "FDA Drug Label - Clobetasol (Temovate, Clobex)",
                "UpToDate - Topical Corticosteroids: Drug Information",
                "Medscape - Clobetasol Drug Reference",
                "Goodman & Gilman's The Pharmacological Basis of Therapeutics (14th ed)"
            ],
            "last_updated": "2025-02-18",
            "evidence_level": "A - Dựa trên FDA drug labels, clinical guidelines, và dữ liệu lâm sàng từ nhiều nguồn"
        }
    },
    
    "Pimecrolimus": {
        "group": "Dermatology - Topical Calcineurin Inhibitor",
        "vietnamese_name": "Pimecrolimus, Elidel",
        "administration": ["Topical"],
        "indications": [
            "Viêm da dị ứng (atopic dermatitis) nhẹ đến trung bình",
            "Viêm da dị ứng ở trẻ em (≥2 tuổi)",
            "Viêm da dị ứng ở vùng da nhạy cảm (mặt, cổ)",
            "Thay thế corticosteroid tại chỗ (tránh teo da)"
        ],
        "contraindications": [
            "Dị ứng pimecrolimus hoặc tacrolimus",
            "Nhiễm trùng da (bacterial, fungal, viral) - không dùng trừ khi có kháng sinh/kháng nấm",
            "Trẻ em <2 tuổi - CHỐNG CHỈ ĐỊNH",
            "Ức chế miễn dịch (HIV, transplant) - thận trọng",
            "Ung thư da - thận trọng"
        ],
        "dosage": {
            "adult_topical": "Bôi mỏng 2 lần/ngày lên vùng da bị ảnh hưởng",
            "pediatric_≥2_years": "Bôi mỏng 2 lần/ngày lên vùng da bị ảnh hưởng",
            "notes": "Bôi ngay khi có dấu hiệu viêm da dị ứng. Có thể dùng kéo dài (không giới hạn thời gian như corticosteroid). Tránh ánh nắng mặt trời."
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "Không đổi",
            "under_30": "Không đổi"
        },
        "side_effects": [
            "Kích ứng da tại chỗ (đỏ, rát, ngứa) - phổ biến trong vài ngày đầu",
            "Nóng rát tại chỗ",
            "Nhiễm trùng da (herpes simplex, varicella zoster) - tăng nguy cơ",
            "Ung thư da (lymphoma, skin cancer) - nguy cơ tăng nhẹ (FDA warning)",
            "Hấp thu toàn thân (hiếm, nếu dùng diện rộng)"
        ],
        "interactions": [
            "Corticosteroid tại chỗ: có thể dùng kết hợp (nhưng thường không cần)",
            "Thuốc ức chế miễn dịch: tăng nguy cơ nhiễm trùng"
        ],
        "pregnancy": "C - Thận trọng",
        "mechanism_of_action": "Pimecrolimus là calcineurin inhibitor tại chỗ. Ức chế calcineurin (enzyme cần thiết cho T-cell activation), dẫn đến: (1) Ức chế sản xuất cytokine (IL-2, IL-4, IL-5, TNF-α), (2) Ức chế T-cell activation và proliferation, (3) Giảm viêm và ngứa. Khác với corticosteroid tại chỗ, pimecrolimus không gây teo da và có thể dùng kéo dài. ĐẶC ĐIỂM: (1) Không gây teo da (ưu điểm so với corticosteroid), (2) Có thể dùng kéo dài, (3) An toàn cho vùng da nhạy cảm (mặt, cổ), (4) FDA warning về nguy cơ ung thư da (lymphoma, skin cancer) - nguy cơ tăng nhẹ, (5) Chỉ dùng cho viêm da dị ứng nhẹ đến trung bình (không dùng cho nặng).",
        "monitoring": [
            "Đáp ứng lâm sàng (giảm đỏ, sưng, ngứa)",
            "Dấu hiệu kích ứng da (đỏ, rát, ngứa tăng)",
            "Dấu hiệu nhiễm trùng da (mủ, đỏ, sưng tăng, herpes)",
            "Dấu hiệu ung thư da (nốt mới, thay đổi nốt cũ)",
            "Diện tích da điều trị (tránh >20% diện tích cơ thể)"
        ],
        "precautions": [
            "FDA warning về nguy cơ ung thư da (lymphoma, skin cancer) - nguy cơ tăng nhẹ",
            "CHỐNG CHỈ ĐỊNH ở trẻ em <2 tuổi",
            "Chỉ dùng cho viêm da dị ứng nhẹ đến trung bình (không dùng cho nặng)",
            "Tránh dùng trên vùng da bị loét, nhiễm trùng",
            "Tránh ánh nắng mặt trời (nhạy cảm ánh sáng, tăng nguy cơ ung thư da)",
            "Nguy cơ nhiễm trùng da (herpes simplex, varicella zoster) - tăng nguy cơ",
            "Thận trọng ở bệnh nhân ức chế miễn dịch (HIV, transplant)",
            "Nguy cơ hấp thu toàn thân nếu dùng diện rộng (>20% diện tích cơ thể)",
            "Không dùng với corticosteroid tại chỗ mạnh (thường không cần)"
        ],
        "pharmacokinetics": {
            "half_life": "Không áp dụng (topical)",
            "onset": "Vài ngày đến 1 tuần",
            "duration": "Phụ thuộc tần suất dùng, có thể dùng kéo dài",
            "protein_binding": "Không áp dụng (topical)",
            "metabolism": "Chuyển hóa tại da và gan (nếu hấp thu toàn thân)",
            "clearance": "Thải trừ qua nước tiểu (nếu hấp thu toàn thân)"
        },
        "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm, tránh ánh sáng. Đóng nắp kín sau khi dùng.",
        "black_box_warnings": "FDA warning: Nguy cơ ung thư da (lymphoma, skin cancer) - nguy cơ tăng nhẹ. Chỉ dùng cho viêm da dị ứng nhẹ đến trung bình không đáp ứng với điều trị khác. Tránh ánh nắng mặt trời. CHỐNG CHỈ ĐỊNH ở trẻ em <2 tuổi.",
        "drug_interactions": {
            "major": [],
            "moderate": [
                {
                    "drug": "Corticosteroid tại chỗ mạnh",
                    "mechanism": "Có thể tăng nguy cơ ức chế miễn dịch và nhiễm trùng",
                    "effect": "Tăng nguy cơ nhiễm trùng da",
                    "management": "Thường không cần dùng kết hợp. Nếu cần, theo dõi dấu hiệu nhiễm trùng sát."
                }
            ],
            "minor": []
        },
        "contraindications": {
            "tuyệt_đối": [
                "Dị ứng pimecrolimus hoặc tacrolimus",
                "Nhiễm trùng da (bacterial, fungal, viral) - không dùng trừ khi có kháng sinh/kháng nấm",
                "Trẻ em <2 tuổi - CHỐNG CHỈ ĐỊNH"
            ],
            "tương_đối": [
                "Ức chế miễn dịch (HIV, transplant) - thận trọng, tăng nguy cơ nhiễm trùng",
                "Ung thư da - thận trọng, tăng nguy cơ",
                "Dùng diện rộng (>20% diện tích cơ thể) - nguy cơ hấp thu toàn thân",
                "Phụ nữ có thai - thận trọng"
            ]
        },
        "contraindications_detail": {
            "tuyệt_đối": [
                "Dị ứng pimecrolimus hoặc tacrolimus",
                "Nhiễm trùng da (bacterial, fungal, viral) - không dùng trừ khi có kháng sinh/kháng nấm",
                "Trẻ em <2 tuổi - CHỐNG CHỈ ĐỊNH"
            ],
            "tương_đối": [
                "Ức chế miễn dịch (HIV, transplant) - thận trọng, tăng nguy cơ nhiễm trùng",
                "Ung thư da - thận trọng, tăng nguy cơ",
                "Dùng diện rộng (>20% diện tích cơ thể) - nguy cơ hấp thu toàn thân",
                "Phụ nữ có thai - thận trọng"
            ]
        },
        "pregnancy_lactation": {
            "fda_category": "C",
            "pregnancy_details": "Pimecrolimus là thuốc phân loại C. Không có nghiên cứu đầy đủ trên phụ nữ có thai. Pimecrolimus có thể hấp thu toàn thân và qua nhau thai. Có thể dùng khi lợi ích vượt quá nguy cơ, đặc biệt khi không có lựa chọn khác.",
            "lactation": {
                "safety": "Compatible with Caution",
                "details": "Pimecrolimus có thể hấp thu toàn thân và bài tiết vào sữa mẹ ở nồng độ thấp. Tuy nhiên, nồng độ trong sữa mẹ thấp và không có báo cáo về tác dụng phụ đáng kể ở trẻ bú mẹ khi dùng tại chỗ với diện tích nhỏ.",
                "recommendation": "Có thể dùng khi cho con bú, nhưng thận trọng. Tránh dùng diện rộng hoặc kéo dài. Tránh bôi lên vú hoặc núm vú."
            }
        },
        "hepatic_adjustment": {
            "mild": "Không cần điều chỉnh liều",
            "moderate": "Không cần điều chỉnh liều",
            "severe": "Không cần điều chỉnh liều (topical, hấp thu tối thiểu)",
            "notes": "Pimecrolimus dùng tại chỗ, hấp thu toàn thân tối thiểu. Không cần điều chỉnh liều ở bệnh nhân suy gan."
        },
        "overdose_management": {
            "symptoms": [
                "Kích ứng da nặng",
                "Hấp thu toàn thân (nếu dùng diện rộng, kéo dài): ức chế miễn dịch, nhiễm trùng"
            ],
            "antidote": "Không có antidote đặc hiệu. Ngừng thuốc, điều trị hỗ trợ.",
            "treatment": [
                "Ngừng ngay pimecrolimus",
                "Nếu kích ứng da nặng:",
                "  - Dưỡng ẩm da",
                "  - Corticosteroid tại chỗ yếu nếu cần",
                "Nếu hấp thu toàn thân:",
                "  - Theo dõi dấu hiệu nhiễm trùng",
                "  - Điều trị nhiễm trùng nếu có",
                "Theo dõi: Dấu hiệu sinh tồn, dấu hiệu nhiễm trùng"
            ],
            "monitoring": "Theo dõi dấu hiệu sinh tồn, dấu hiệu nhiễm trùng (nếu có hấp thu toàn thân) cho đến khi hồi phục."
        },
        "reversal_agents": {
            "available": False,
            "agents": [],
            "notes": "Không có antidote đặc hiệu. Điều trị quá liều chủ yếu là ngừng thuốc và điều trị hỗ trợ. Nếu có hấp thu toàn thân: theo dõi dấu hiệu nhiễm trùng và điều trị nếu cần."
        },
        "administration_instructions": {
            "oral": None,
            "topical": {
                "preparation": "Dạng cream 1%.",
                "application": "Bôi mỏng 2 lần/ngày lên vùng da bị ảnh hưởng. Massage nhẹ cho đến khi thấm. Rửa tay sau khi bôi.",
                "area": "Chỉ bôi lên vùng da bị ảnh thương. Có thể dùng trên vùng da nhạy cảm (mặt, cổ).",
                "duration": "Có thể dùng kéo dài (không giới hạn thời gian như corticosteroid). Bôi ngay khi có dấu hiệu viêm da dị ứng.",
                "notes": "QUAN TRỌNG: 1) Chỉ dùng cho viêm da dị ứng nhẹ đến trung bình, 2) CHỐNG CHỈ ĐỊNH ở trẻ em <2 tuổi, 3) Tránh ánh nắng mặt trời, 4) Tránh bôi lên vùng da bị loét, nhiễm trùng, 5) FDA warning về nguy cơ ung thư da."
            }
        },
        "references": {
            "primary_sources": [
                "FDA Drug Label - Pimecrolimus (Elidel)",
                "UpToDate - Topical Calcineurin Inhibitors: Drug Information",
                "Medscape - Pimecrolimus Drug Reference",
                "Goodman & Gilman's The Pharmacological Basis of Therapeutics (14th ed)"
            ],
            "last_updated": "2025-02-18",
            "evidence_level": "A - Dựa trên FDA drug labels, clinical guidelines, và dữ liệu lâm sàng từ nhiều nguồn"
        }
    },
    
    "Hydrocortisone topical": {
        "group": "Dermatology - Topical Corticosteroid (Low Potency)",
        "vietnamese_name": "Hydrocortisone, Cortaid, Cortizone",
        "administration": ["Topical"],
        "indications": [
            "Viêm da dị ứng (atopic dermatitis) nhẹ",
            "Viêm da tiếp xúc (contact dermatitis) nhẹ",
            "Eczema nhẹ",
            "Phát ban nhẹ",
            "Ngứa nhẹ",
            "Vùng da nhạy cảm (mặt, nách, bẹn, vùng sinh dục)"
        ],
        "contraindications": [
            "Dị ứng hydrocortisone hoặc corticosteroid",
            "Nhiễm trùng da (bacterial, fungal, viral) - không dùng trừ khi có kháng sinh/kháng nấm",
            "Loét da"
        ],
        "dosage": {
            "adult_topical": "Bôi mỏng 2-4 lần/ngày lên vùng da bị ảnh hưởng",
            "pediatric": "Bôi mỏng 2-4 lần/ngày lên vùng da bị ảnh hưởng",
            "notes": "Hydrocortisone là corticosteroid yếu nhất (low potency, nhóm VII). An toàn cho vùng da nhạy cảm (mặt, nách, bẹn). Có thể dùng kéo dài hơn các corticosteroid mạnh hơn."
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "Không đổi",
            "under_30": "Không đổi"
        },
        "side_effects": [
            "Kích ứng da tại chỗ (hiếm)",
            "Teo da (skin atrophy) - hiếm, chỉ nếu dùng kéo dài",
            "Nhiễm trùng da thứ phát (bacterial, fungal) - hiếm",
            "Hấp thu toàn thân (rất hiếm, chỉ nếu dùng diện rộng, kéo dài)"
        ],
        "interactions": [
            "Không có tương tác đáng kể với thuốc khác (topical)"
        ],
        "pregnancy": "C - An toàn cho vùng da nhạy cảm",
        "mechanism_of_action": "Hydrocortisone là corticosteroid tự nhiên (cortisol), low potency (nhóm VII - yếu nhất). Gắn với thụ thể glucocorticoid trong tế bào, điều hòa biểu hiện gen, dẫn đến: (1) Ức chế viêm (giảm cytokine, chemokine, adhesion molecules), (2) Ức chế miễn dịch (giảm T-cell activation, cytokine production), (3) Co mạch (giảm đỏ, sưng), (4) Ức chế tăng sinh tế bào. Hydrocortisone có độ mạnh thấp nhất trong các corticosteroid tại chỗ, an toàn cho vùng da nhạy cảm (mặt, nách, bẹn, vùng sinh dục), và có thể dùng kéo dài hơn các corticosteroid mạnh hơn. ĐẶC ĐIỂM: (1) Low potency (nhóm VII - yếu nhất), (2) An toàn cho vùng da nhạy cảm, (3) Có thể dùng kéo dài, (4) Nguy cơ tác dụng phụ thấp (teo da, ức chế HPA rất hiếm), (5) Phù hợp cho trẻ em và phụ nữ có thai.",
        "monitoring": [
            "Đáp ứng lâm sàng (giảm đỏ, sưng, ngứa)",
            "Dấu hiệu kích ứng da (đỏ, rát, ngứa tăng)",
            "Dấu hiệu nhiễm trùng da (mủ, đỏ, sưng tăng)",
            "Dấu hiệu teo da (nếu dùng kéo dài) - hiếm"
        ],
        "precautions": [
            "Hydrocortisone là corticosteroid yếu nhất - chỉ dùng cho tổn thương nhẹ",
            "An toàn cho vùng da nhạy cảm (mặt, nách, bẹn, vùng sinh dục)",
            "Có thể dùng kéo dài hơn các corticosteroid mạnh hơn",
            "Tránh dùng trên vùng da bị loét, nhiễm trùng",
            "Nguy cơ tác dụng phụ thấp (teo da, ức chế HPA rất hiếm)",
            "Bảo vệ khỏi ánh nắng mặt trời (nhạy cảm ánh sáng nhẹ)"
        ],
        "pharmacokinetics": {
            "half_life": "Không áp dụng (topical)",
            "onset": "Vài ngày",
            "duration": "Phụ thuộc tần suất dùng, có thể dùng kéo dài",
            "protein_binding": "Không áp dụng (topical)",
            "metabolism": "Chuyển hóa tại da và gan (nếu hấp thu toàn thân)",
            "clearance": "Thải trừ qua nước tiểu (nếu hấp thu toàn thân)"
        },
        "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm, tránh ánh sáng. Đóng nắp kín sau khi dùng.",
        "black_box_warnings": None,
        "drug_interactions": {
            "major": [],
            "moderate": [],
            "minor": []
        },
        "risk_flags": {
            "high_alert": False,
            "narrow_therapeutic_index": False,
            "bleeding_risk": False,
            "organ_toxicity": ["Skin atrophy (rare, only with prolonged use)", "Systemic absorption (rare, only with large surface area, prolonged use)"],
            "qt_prolongation": False,
            "hepatotoxicity": False,
            "nephrotoxicity": False,
            "requires_monitoring": ["Clinical response (reduction in redness, swelling, itching)", "Signs of skin irritation", "Signs of skin infection", "Signs of skin atrophy (if used long-term)"]
        },
        "guideline_tags": [
            "AAD Guidelines - Atopic Dermatitis",
            "AAD Guidelines - Contact Dermatitis",
            "FDA Drug Information - Hydrocortisone Topical"
        ],
        "contraindications": {
            "tuyệt_đối": [
                "Dị ứng hydrocortisone hoặc corticosteroid",
                "Nhiễm trùng da (bacterial, fungal, viral) - không dùng trừ khi có kháng sinh/kháng nấm",
                "Loét da"
            ],
            "tương_đối": [
                "Dùng kéo dài trên diện rộng - nguy cơ hấp thu toàn thân (rất hiếm)"
            ]
        },
        "pregnancy_lactation": {
            "fda_category": "C",
            "pregnancy_details": "Hydrocortisone là thuốc phân loại C. Corticosteroid tại chỗ có thể hấp thu toàn thân, đặc biệt khi dùng diện rộng hoặc kéo dài. Tuy nhiên, hydrocortisone là corticosteroid yếu nhất và an toàn hơn các corticosteroid mạnh hơn. Có thể dùng khi lợi ích vượt quá nguy cơ, đặc biệt cho vùng da nhạy cảm.",
            "lactation": {
                "safety": "Compatible",
                "details": "Hydrocortisone có thể hấp thu toàn thân và bài tiết vào sữa mẹ ở nồng độ rất thấp. Nồng độ trong sữa mẹ thấp và không có báo cáo về tác dụng phụ đáng kể ở trẻ bú mẹ khi dùng tại chỗ với diện tích nhỏ.",
                "recommendation": "Có thể dùng khi cho con bú. Hydrocortisone bài tiết vào sữa mẹ ở nồng độ thấp và không gây tác dụng phụ ở trẻ bú mẹ."
            }
        },
        "hepatic_adjustment": {
            "mild": "Không cần điều chỉnh liều",
            "moderate": "Không cần điều chỉnh liều",
            "severe": "Không cần điều chỉnh liều (topical, hấp thu tối thiểu)",
            "notes": "Hydrocortisone dùng tại chỗ, hấp thu toàn thân tối thiểu. Không cần điều chỉnh liều ở bệnh nhân suy gan."
        },
        "overdose_management": {
            "symptoms": [
                "Kích ứng da nhẹ",
                "Hấp thu toàn thân (rất hiếm, nếu dùng diện rộng, kéo dài): ức chế HPA"
            ],
            "antidote": "Không có antidote đặc hiệu. Ngừng thuốc, điều trị hỗ trợ.",
            "treatment": [
                "Ngừng ngay hydrocortisone",
                "Nếu kích ứng da:",
                "  - Dưỡng ẩm da",
                "Nếu ức chế HPA (rất hiếm):",
                "  - Hydrocortisone thay thế nếu cần",
                "  - Theo dõi huyết áp, đường huyết",
                "Theo dõi: Dấu hiệu sinh tồn, chức năng thượng thận (nếu có ức chế HPA)"
            ],
            "monitoring": "Theo dõi dấu hiệu sinh tồn, chức năng thượng thận (nếu có ức chế HPA) cho đến khi hồi phục."
        },
        "reversal_agents": None,
        "administration_instructions": {
            "oral": None,
            "topical": {
                "preparation": "Dạng cream, ointment, lotion 0.5%, 1%, 2.5%. Chọn dạng phù hợp với vị trí và loại tổn thương.",
                "application": "Bôi mỏng 2-4 lần/ngày lên vùng da bị ảnh hưởng. Massage nhẹ cho đến khi thấm. Rửa tay sau khi bôi.",
                "area": "Chỉ bôi lên vùng da bị ảnh thương. An toàn cho vùng da nhạy cảm (mặt, nách, bẹn, vùng sinh dục).",
                "duration": "Có thể dùng kéo dài hơn các corticosteroid mạnh hơn. Điều chỉnh tần suất theo đáp ứng.",
                "notes": "QUAN TRỌNG: 1) Corticosteroid yếu nhất, an toàn cho vùng da nhạy cảm, 2) Có thể dùng kéo dài, 3) Tránh bôi lên vùng da bị loét, nhiễm trùng, 4) Bảo vệ khỏi ánh nắng mặt trời."
            }
        },
        "references": {
            "primary_sources": [
                "FDA Drug Label - Hydrocortisone (Cortaid, Cortizone)",
                "UpToDate - Topical Corticosteroids: Drug Information",
                "Medscape - Hydrocortisone Drug Reference",
                "Goodman & Gilman's The Pharmacological Basis of Therapeutics (14th ed)"
            ],
            "last_updated": "2025-02-18",
            "evidence_level": "A - Dựa trên FDA drug labels, clinical guidelines, và dữ liệu lâm sàng từ nhiều nguồn"
        }
    },
    
    "Betamethasone/Clotrimazole topical": {
        "group": "Dermatology - Topical Combination (Corticosteroid + Antifungal)",
        "vietnamese_name": "Betamethasone/Clotrimazole, Canesten Plus, Lotrisone",
        "administration": ["Topical"],
        "indications": [
            "Nấm da kèm viêm, ngứa nhiều (tinea corporis, tinea cruris, tinea pedis)",
            "Viêm da do nấm kèm phản ứng viêm mạnh"
        ],
        "contraindications": [
            "Dị ứng betamethasone, clotrimazole hoặc thành phần khác",
            "Nhiễm virus tại chỗ (mụn rộp, zona, thủy đậu)",
            "Nhiễm lao/nấm sâu da chưa điều trị toàn thân",
            "Trẻ em nhỏ (thận trọng, tránh dùng kéo dài/diện rộng)"
        ],
        "dosage": {
            "adult_topical": "Bôi mỏng 2 lần/ngày lên vùng da bị tổn thương",
            "duration": "2–4 tuần tùy vị trí; không dùng kéo dài như corticoid đơn thuần",
            "notes": "Không băng kín. Nếu cần dùng lâu dài nên chuyển sang kháng nấm đơn thuần sau khi hết viêm."
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "Không đổi",
            "under_30": "Không đổi"
        },
        "side_effects": [
            "Kích ứng, rát, đỏ da tại chỗ",
            "Teo da, rạn da nếu dùng kéo dài (do betamethasone)",
            "Nhiễm nấm hoặc vi khuẩn thứ phát nếu lạm dụng corticoid"
        ],
        "interactions": [
            "Corticosteroid tại chỗ khác: tăng nguy cơ teo da"
        ],
        "pregnancy": "C",
        "mechanism_of_action": "Betamethasone là corticosteroid mạnh, kháng viêm, giảm ngứa; clotrimazole là kháng nấm azole, ức chế tổng hợp ergosterol. Phối hợp giúp vừa điều trị nấm vừa giảm nhanh triệu chứng viêm, nhưng nguy cơ che lấp nhiễm nấm nếu lạm dụng.",
        "monitoring": [
            "Đáp ứng triệu chứng (giảm ngứa, đỏ, bong vảy)",
            "Dấu hiệu teo da nếu dùng >2–4 tuần",
            "Tái phát nấm sau ngừng thuốc (cần chuyển sang kháng nấm đơn thuần)"
        ],
        "precautions": [
            "Không dùng kéo dài hoặc trên diện rộng",
            "Tránh dùng trên mặt, vùng sinh dục lâu dài",
            "Nếu cần điều trị duy trì nấm, dùng kháng nấm đơn thuần sau giai đoạn cấp"
        ],
        "pharmacokinetics": {
            "half_life": "Không áp dụng (topical)",
            "onset": "Vài ngày",
            "duration": "Phụ thuộc tần suất và thời gian dùng",
            "protein_binding": "Không áp dụng (topical)",
            "metabolism": "Chuyển hóa tại da và gan (nếu hấp thu toàn thân)",
            "clearance": "Thải trừ qua nước tiểu (nếu hấp thu toàn thân)"
        },
        "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm, tránh ánh sáng. Đóng nắp kín sau khi dùng.",
        "black_box_warnings": None,
        "drug_interactions": {
            "major": [],
            "moderate": [],
            "minor": []
        },
        "contraindications": {
            "tuyệt_đối": [
                "Dị ứng betamethasone, clotrimazole hoặc thành phần khác",
                "Nhiễm virus da (herpes, varicella, vaccinia)",
                "Lao da chưa điều trị"
            ],
            "tương_đối": [
                "Trẻ em, phụ nữ có thai – tránh dùng kéo dài",
                "Dùng trên diện rộng hoặc dưới băng kín"
            ]
        },
        "pregnancy_lactation": {
            "fda_category": "C",
            "pregnancy_details": "Dùng được ngắn ngày trên diện tích nhỏ khi lợi ích vượt trội nguy cơ. Tránh dùng kéo dài hoặc trên diện rộng trong thai kỳ.",
            "lactation": {
                "safety": "Compatible with Caution",
                "details": "Hấp thu toàn thân rất thấp nếu dùng diện tích nhỏ. Tránh bôi lên vùng vú trước khi cho bú.",
                "recommendation": "Có thể dùng trên diện tích nhỏ, thời gian ngắn; không bôi lên vú."
            }
        },
        "overdose_management": {
            "symptoms": [
                "Teo da, rạn da",
                "Nặng hơn nhiễm nấm do che lấp triệu chứng",
                "Ức chế HPA nếu dùng diện rộng, kéo dài (hiếm)"
            ],
            "antidote": "Không có antidote đặc hiệu. Ngừng thuốc, điều trị hỗ trợ.",
            "treatment": [
                "Ngừng ngay thuốc",
                "Chuyển sang kháng nấm đơn thuần nếu còn nhiễm nấm",
                "Theo dõi dấu hiệu ức chế HPA nếu đã dùng diện rộng, kéo dài"
            ],
            "monitoring": "Theo dõi lâm sàng da và (nếu cần) chức năng trục HPA."
        },
        "reversal_agents": None,
        "administration_instructions": {
            "oral": None,
            "topical": {
                "preparation": "Cream/ointment phối hợp betamethasone + clotrimazole.",
                "application": "Rửa sạch, lau khô vùng da, bôi mỏng 2 lần/ngày, không băng kín trừ khi có chỉ định.",
                "area": "Chỉ bôi lên vùng da nhiễm nấm viêm; tránh vùng mặt, sinh dục.",
                "duration": "2–4 tuần; sau đó đánh giá lại.",
                "notes": "Dùng cho giai đoạn cấp. Không lạm dụng corticoid phối hợp lâu dài."
            }
        },
        "references": {
            "primary_sources": [
                "FDA/EMA product information – betamethasone/clotrimazole",
                "UpToDate – Topical treatment of dermatophyte infections",
                "Dermatology texts on combination steroid/antifungal creams"
            ],
            "last_updated": "2025-02-23",
            "evidence_level": "B - Hướng dẫn lâm sàng và kinh nghiệm thực hành"
        },
        "risk_flags": {
            "high_alert": False,
            "narrow_therapeutic_index": False,
            "bleeding_risk": False,
            "organ_toxicity": ["Skin atrophy (from betamethasone with prolonged use)", "HPA axis suppression (if used on large areas/long-term)"],
            "qt_prolongation": False,
            "hepatotoxicity": False,
            "nephrotoxicity": False,
            "requires_monitoring": ["Clinical response (improvement in itching, redness, scaling)", "Signs of skin atrophy (if used >2-4 weeks)", "Signs of fungal recurrence after stopping", "HPA axis function if used on large areas/long-term"]
        },
        "guideline_tags": [
            "AAD Guidelines - Topical Antifungal Treatment",
            "AAD Guidelines - Topical Combination Therapy",
            "FDA Drug Information - Topical Combinations",
            "UpToDate - Dermatophyte Infections Treatment"
        ],
                  "hepatic_adjustment": {
                  "mild": "Không đổi",
                  "moderate": "Thận trọng",
                  "severe": "Thận trọng, có thể giảm liều",
                  "notes": "Cần tra cứu thêm thông tin chi tiết về điều chỉnh liều ở suy gan."
              },
},
    
    "Fusidic acid/Betamethasone topical": {
        "group": "Dermatology - Topical Combination (Antibiotic + Corticosteroid)",
        "vietnamese_name": "Fusidic acid/Betamethasone, Fucidin H/F",
        "administration": ["Topical"],
        "indications": [
            "Viêm da dị ứng bội nhiễm vi khuẩn (eczema bội nhiễm)",
            "Viêm da tiếp xúc bội nhiễm",
            "Chốc lở quanh tổn thương viêm da"
        ],
        "contraindications": [
            "Dị ứng fusidic acid, betamethasone",
            "Nhiễm virus da (herpes, varicella, vaccinia)",
            "Lao da, nấm da chưa điều trị hệ thống"
        ],
        "dosage": {
            "adult_topical": "Bôi mỏng 2–3 lần/ngày lên vùng da bội nhiễm",
            "duration": "Tối đa 1–2 tuần; không dùng như duy trì dài hạn",
            "notes": "Khi đã kiểm soát bội nhiễm nên chuyển sang điều trị nền (dưỡng ẩm, corticoid đơn, v.v.)."
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "Không đổi",
            "under_30": "Không đổi"
        },
        "side_effects": [
            "Kích ứng da, nóng rát nhẹ",
            "Teo da, rạn da (do corticoid nếu lạm dụng)",
            "Kháng kháng sinh tại chỗ nếu dùng kéo dài"
        ],
        "interactions": [
            "Kháng sinh tại chỗ khác: tăng nguy cơ kháng thuốc"
        ],
        "pregnancy": "C",
        "mechanism_of_action": "Fusidic acid là kháng sinh ức chế tổng hợp protein Gram dương (đặc biệt Staphylococcus aureus); betamethasone kháng viêm mạnh. Phối hợp dùng ngắn ngày cho tổn thương viêm da bội nhiễm.",
        "monitoring": [
            "Cải thiện đỏ, tiết dịch, mụn mủ",
            "Dấu hiệu kích ứng, teo da nếu dùng kéo dài",
            "Không cải thiện hoặc nặng hơn → đánh giá lại vi khuẩn kháng thuốc"
        ],
        "precautions": [
            "Không dùng kéo dài để tránh kháng kháng sinh và teo da.",
            "Không băng kín trừ khi có chỉ định.",
            "Tránh dùng quanh mắt, mặt lâu dài."
        ],
        "pharmacokinetics": {
            "half_life": "Không áp dụng (topical)",
            "onset": "Vài ngày",
            "duration": "Phụ thuộc tần suất và thời gian dùng",
            "protein_binding": "Không áp dụng (topical)",
            "metabolism": "Chủ yếu tại chỗ; hấp thu toàn thân tối thiểu nếu da lành",
            "clearance": "Không đáng kể qua đường toàn thân ở liều dùng thông thường"
        },
        "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm, tránh ánh sáng.",
        "black_box_warnings": None,
        "drug_interactions": {
            "major": [],
            "moderate": [],
            "minor": []
        },
        "contraindications": {
            "tuyệt_đối": [
                "Dị ứng thành phần thuốc",
                "Nhiễm lao/nấm da chưa điều trị toàn thân",
                "Nhiễm virus tại chỗ (herpes simplex, varicella, vaccinia)"
            ],
            "tương_đối": [
                "Trẻ em, phụ nữ có thai – dùng ngắn ngày trên diện tích nhỏ",
                "Dùng trên diện rộng hoặc dưới băng kín"
            ]
        },
        "pregnancy_lactation": {
            "fda_category": "C",
            "pregnancy_details": "Có thể dùng ngắn ngày trên diện tích nhỏ khi lợi ích vượt nguy cơ. Tránh lạm dụng corticoid tại chỗ trong thai kỳ.",
            "lactation": {
                "safety": "Compatible with Caution",
                "details": "Hấp thu toàn thân rất thấp nếu dùng diện tích nhỏ. Tránh bôi lên vú trước khi cho bú.",
                "recommendation": "Có thể dùng ngắn ngày, diện tích nhỏ; không bôi lên vú."
            }
        },
        "overdose_management": {
            "symptoms": [
                "Teo da, rạn da",
                "Tổn thương không lành, có thể do vi khuẩn kháng thuốc"
            ],
            "antidote": "Không có antidote đặc hiệu. Ngừng thuốc, điều trị hỗ trợ.",
            "treatment": [
                "Ngừng thuốc",
                "Đánh giá lại nhiễm khuẩn, cấy mủ nếu cần",
                "Điều trị theo kháng sinh toàn thân nếu cần thiết"
            ],
            "monitoring": "Theo dõi lâm sàng tổn thương da và dấu hiệu nhiễm trùng."
        },
        "reversal_agents": None,
        "administration_instructions": {
            "oral": None,
            "topical": {
                "preparation": "Cream/ointment phối hợp fusidic acid + betamethasone.",
                "application": "Rửa sạch, lau khô, bôi mỏng 2–3 lần/ngày lên vùng bội nhiễm.",
                "area": "Chỉ bôi lên vùng da viêm bội nhiễm; tránh diện rộng.",
                "duration": "Tối đa 1–2 tuần.",
                "notes": "Dùng cho giai đoạn cấp bội nhiễm, sau đó chuyển điều trị nền khác."
            }
        },
        "references": {
            "primary_sources": [
                "Product information – fusidic acid/betamethasone",
                "Dermatology guidelines on infected eczema",
                "UpToDate – Management of secondarily infected eczema"
            ],
            "last_updated": "2025-02-23",
            "evidence_level": "B - Hướng dẫn lâm sàng và dữ liệu thực hành"
        },
        "hepatic_adjustment": {
                  "mild": "Không đổi",
                  "moderate": "Thận trọng, có thể giảm liều",
                  "severe": "Thận trọng, giảm liều hoặc tránh dùng",
                  "notes": "Nhiều kháng sinh chuyển hóa qua gan, cần điều chỉnh liều ở suy gan nặng."
              },
},
    
    "Miconazole/Hydrocortisone topical": {
        "group": "Dermatology - Topical Combination (Antifungal + Low-potency Corticosteroid)",
        "vietnamese_name": "Miconazole/Hydrocortisone",
        "administration": ["Topical"],
        "indications": [
            "Viêm da do nấm (Candida, dermatophyte) kèm ngứa/viêm nhẹ đến trung bình",
            "Hăm da, hăm tã bội nhiễm nấm (chọn lọc, ngắn ngày)"
        ],
        "contraindications": [
            "Dị ứng miconazole, hydrocortisone hoặc azole khác",
            "Nhiễm virus da (herpes, varicella, vaccinia)",
            "Lao da, nấm sâu da chưa điều trị",
        ],
        "dosage": {
            "adult_topical": "Bôi mỏng 2 lần/ngày lên vùng da tổn thương sau khi rửa sạch và lau khô",
            "pediatric": "Bôi mỏng 1–2 lần/ngày (trẻ lớn, theo chỉ định bác sĩ)",
            "duration": "Thường 1–2 tuần; sau đó nếu còn nấm nên chuyển sang miconazole đơn thuần",
            "notes": "Không dùng kéo dài như hydrocortisone đơn thuần để tránh che lấp nhiễm nấm."
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "Không đổi",
            "under_30": "Không đổi"
        },
        "side_effects": [
            "Kích ứng, nóng rát tại chỗ",
            "Hiếm: teo da nếu lạm dụng hydrocortisone kéo dài",
        ],
        "interactions": [
            "Warfarin (với miconazole bôi diện rộng/ở vùng rộng): lý thuyết tăng INR – rất hiếm nhưng nên thận trọng."
        ],
        "pregnancy": "C",
        "mechanism_of_action": "Miconazole là kháng nấm azole ức chế tổng hợp ergosterol; hydrocortisone là corticoid yếu, giúp giảm viêm/ngứa. Phối hợp phù hợp cho tổn thương nấm nhẹ kèm viêm, dùng ngắn hạn.",
        "monitoring": [
            "Đáp ứng lâm sàng (giảm đỏ, ngứa, bong vảy)",
            "Tồn tại hoặc lan rộng tổn thương → nghi ngờ kháng nấm hoặc lạm dụng corticoid",
        ],
        "precautions": [
            "Chỉ dùng ngắn hạn; sau đó ưu tiên kháng nấm đơn thuần.",
            "Tránh dùng diện rộng, đặc biệt ở trẻ nhỏ.",
        ],
        "pharmacokinetics": {
            "half_life": "Không áp dụng (topical)",
            "onset": "Vài ngày",
            "duration": "Phụ thuộc tần suất và thời gian dùng",
            "protein_binding": "Không áp dụng (topical)",
            "metabolism": "Chủ yếu tại chỗ, hấp thu toàn thân rất thấp",
            "clearance": "Không đáng kể qua đường toàn thân ở liều thông thường"
        },
        "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm, tránh ánh sáng.",
        "black_box_warnings": None,
        "drug_interactions": {
            "major": [],
            "moderate": [],
            "minor": []
        },
        "contraindications_detail": {
            "tuyệt_đối": [
                "Dị ứng miconazole, hydrocortisone hoặc azole khác",
                "Nhiễm virus da hoạt động"
            ],
            "tương_đối": [
                "Trẻ sơ sinh, hăm tã nặng – cần theo dõi sát, tránh băng kín lâu"
            ]
        },
        "pregnancy_lactation": {
            "fda_category": "C",
            "pregnancy_details": "Có thể dùng ngắn ngày trên diện tích nhỏ nếu cần thiết; tránh diện rộng/kéo dài.",
            "lactation": {
                "safety": "Compatible with Caution",
                "details": "Hấp thu toàn thân rất thấp; tránh bôi lên vú trước khi cho bú.",
                "recommendation": "Có thể dùng diện tích nhỏ, ngắn ngày; không bôi lên vú."
            }
        },
        "overdose_management": {
            "symptoms": [
                "Kích ứng da, đỏ nhiều hơn",
            ],
            "antidote": "Không có antidote đặc hiệu.",
            "treatment": [
                "Ngừng thuốc, điều trị triệu chứng (dưỡng ẩm, kháng histamin đường uống nếu ngứa nhiều)."
            ],
            "monitoring": "Theo dõi cải thiện tổn thương và hết kích ứng."
        },
        "reversal_agents": None,
        "administration_instructions": {
            "oral": None,
            "topical": {
                "preparation": "Cream hoặc ointment phối hợp miconazole + hydrocortisone.",
                "application": "Rửa sạch, lau khô vùng da, bôi mỏng 1 lớp mỏng, tránh băng kín lâu.",
                "area": "Vùng da nhiễm nấm có viêm/ ngứa; tránh vùng mặt kéo dài.",
                "duration": "1–2 tuần, sau đó xem xét chuyển kháng nấm đơn thuần.",
                "notes": "Không dùng như corticoid bôi thường quy lâu dài."
            }
        },
        "references": {
            "primary_sources": [
                "Product information – miconazole/hydrocortisone",
            ],
            "last_updated": "2025-02-23",
            "evidence_level": "B - Dựa trên dữ liệu thực hành và tờ hướng dẫn thuốc"
        },
        "hepatic_adjustment": {
                  "mild": "Không đổi",
                  "moderate": "Thận trọng",
                  "severe": "Thận trọng, có thể giảm liều",
                  "notes": "Cần tra cứu thêm thông tin chi tiết về điều chỉnh liều ở suy gan."
              },
},
    
    "Gentamicin/Betamethasone/Clotrimazole topical": {
        "group": "Dermatology - Topical Combination (Antibiotic + Corticosteroid + Antifungal)",
        "vietnamese_name": "Gentamicin/Betamethasone/Clotrimazole",
        "administration": ["Topical"],
        "indications": [
            "Viêm da hoặc nấm da kèm bội nhiễm vi khuẩn (Staphylococcus, Streptococcus) và viêm/ ngứa",
            "Chốc lở quanh tổn thương nấm/viêm",
        ],
        "contraindications": [
            "Dị ứng gentamicin, betamethasone, clotrimazole hoặc aminoglycoside/azole khác",
            "Nhiễm virus da (herpes, varicella, vaccinia)",
            "Lao da, nấm sâu chưa điều trị",
            "Vết thương sâu, bỏng rộng (tránh aminoglycoside trên diện rộng)",
        ],
        "dosage": {
            "adult_topical": "Bôi mỏng 2–3 lần/ngày lên vùng tổn thương sau khi rửa sạch và lau khô",
            "duration": "Thường 1–2 tuần; không dùng kéo dài như duy trì",
            "notes": "Dùng cho giai đoạn cấp có bội nhiễm; sau đó chuyển sang liệu pháp chuyên biệt (kháng nấm đơn, dưỡng ẩm, corticoid đơn nhẹ hơn) nếu cần.",
        },
        "renal_adjustment": {
            "normal": "Không đổi (hấp thu toàn thân rất thấp nếu da lành)",
            "30_60": "Thận trọng nếu cần dùng trên diện rộng/băng kín",
            "under_30": "Tránh dùng trên diện rộng/bỏng (nguy cơ hấp thu gentamicin)",
        },
        "side_effects": [
            "Kích ứng, rát, khô da tại chỗ",
            "Teo da, rạn da nếu lạm dụng (do betamethasone)",
            "Viêm da tiếp xúc, đặc biệt do aminoglycoside (gentamicin)",
        ],
        "interactions": [
            "Corticosteroid tại chỗ khác: tăng nguy cơ teo da",
            "Kháng sinh tại chỗ khác: tăng nguy cơ kháng thuốc hoặc kích ứng",
        ],
        "pregnancy": "C",
        "mechanism_of_action": "Gentamicin (aminoglycoside) kháng khuẩn Gram âm/Gram dương; clotrimazole kháng nấm azole; betamethasone kháng viêm mạnh. Phối hợp nhằm xử trí tổn thương viêm/nấm có bội nhiễm vi khuẩn và ngứa nhiều, dùng ngắn hạn.",
        "monitoring": [
            "Cải thiện đỏ, ngứa, tiết dịch hoặc mụn mủ",
            "Dấu hiệu kích ứng hoặc viêm da tiếp xúc (dừng thuốc nếu xuất hiện)",
            "Dấu hiệu teo da khi dùng >2 tuần",
        ],
        "precautions": [
            "Không dùng kéo dài hoặc trên diện rộng; tránh băng kín trừ khi có chỉ định.",
            "Sau giai đoạn cấp, chuyển sang điều trị chuyên biệt (kháng nấm đơn, dưỡng ẩm) nếu cần.",
            "Tránh dùng quanh mắt, vùng mặt lâu dài.",
        ],
        "pharmacokinetics": {
            "half_life": "Không áp dụng (topical); hấp thu toàn thân rất thấp nếu da lành",
            "onset": "Vài ngày",
            "duration": "Phụ thuộc tần suất và thời gian dùng",
            "protein_binding": "Không áp dụng (topical)",
            "metabolism": "Chủ yếu tại chỗ; hấp thu toàn thân tối thiểu",
            "clearance": "Nếu hấp thu: gentamicin thải qua thận; betamethasone chuyển hóa gan; clotrimazole chuyển hóa gan",
        },
        "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm và ánh sáng. Đóng nắp kín sau khi dùng.",
        "black_box_warnings": None,
        "drug_interactions": {
            "major": [],
            "moderate": [],
            "minor": []
        },
        "contraindications_detail": {
            "tuyệt_đối": [
                "Dị ứng thành phần thuốc",
                "Nhiễm virus da hoạt động",
                "Bỏng rộng, vết thương sâu (tránh aminoglycoside hấp thu)",
            ],
            "tương_đối": [
                "Trẻ nhỏ, phụ nữ có thai: chỉ dùng ngắn ngày trên diện tích nhỏ",
                "Dùng trên mặt hoặc băng kín – tăng hấp thu corticoid/aminoglycoside",
            ],
        },
        "pregnancy_lactation": {
            "fda_category": "C",
            "pregnancy_details": "Có thể dùng ngắn ngày trên diện tích nhỏ khi lợi ích vượt trội nguy cơ; tránh dùng diện rộng/băng kín trong thai kỳ.",
            "lactation": {
                "safety": "Compatible with Caution",
                "details": "Hấp thu toàn thân thấp; tránh bôi lên vú trước khi cho bú.",
                "recommendation": "Có thể dùng ngắn ngày, diện tích nhỏ; không bôi lên vú."
            }
        },
        "overdose_management": {
            "symptoms": [
                "Kích ứng, viêm da tiếp xúc",
                "Teo da (nếu lạm dụng corticoid)"
            ],
            "antidote": "Không có antidote đặc hiệu.",
            "treatment": [
                "Ngừng thuốc",
                "Điều trị triệu chứng (dưỡng ẩm, kháng histamin uống nếu ngứa)",
                "Nếu nghi viêm da tiếp xúc: có thể cần corticoid nhẹ tại chỗ ngắn ngày sau khi ngừng (theo chỉ định bác sĩ)"
            ],
            "monitoring": "Theo dõi cải thiện sau ngừng thuốc; nếu không cải thiện cần khám lại.",
        },
        "reversal_agents": None,
        "administration_instructions": {
            "oral": None,
            "topical": {
                "preparation": "Cream/ointment phối hợp gentamicin + betamethasone + clotrimazole.",
                "application": "Rửa sạch, lau khô, bôi mỏng 2–3 lần/ngày; không băng kín trừ khi bác sĩ chỉ định.",
                "area": "Vùng viêm/nấm có bội nhiễm vi khuẩn; tránh bôi trên diện rộng.",
                "duration": "1–2 tuần; đánh giá lại nếu chưa cải thiện.",
                "notes": "Dùng cho giai đoạn cấp; không lạm dụng kéo dài để tránh teo da/kháng thuốc."
            }
        },
        "references": {
            "primary_sources": [
                "Product information – gentamicin/betamethasone/clotrimazole",
                "Thực hành lâm sàng trong điều trị tổn thương nấm/viêm bội nhiễm"
            ],
            "last_updated": "2025-02-23",
            "evidence_level": "B - Dữ liệu thực hành và tờ hướng dẫn thuốc"
        },
        "risk_flags": {
            "high_alert": False,
            "narrow_therapeutic_index": False,
            "bleeding_risk": False,
            "organ_toxicity": ["Skin atrophy (from betamethasone with prolonged use)", "Contact dermatitis (especially from gentamicin)", "Systemic absorption of gentamicin (if used on large areas/burns)"],
            "qt_prolongation": False,
            "hepatotoxicity": False,
            "nephrotoxicity": False,
            "requires_monitoring": ["Clinical response (improvement in redness, itching, discharge)", "Signs of skin irritation or contact dermatitis", "Signs of skin atrophy (if used >2 weeks)", "Systemic effects if used on large areas/burns"]
        },
        "guideline_tags": [
            "AAD Guidelines - Topical Combination Therapy",
            "FDA Drug Information - Topical Combinations",
            "Clinical Practice Guidelines - Dermatitis Treatment"
        ],
                  "hepatic_adjustment": {
                  "mild": "Không đổi",
                  "moderate": "Thận trọng, có thể giảm liều",
                  "severe": "Thận trọng, giảm liều hoặc tránh dùng",
                  "notes": "Nhiều kháng sinh chuyển hóa qua gan, cần điều chỉnh liều ở suy gan nặng."
              },
},
    
    "Tacrolimus topical": {
        "group": "Dermatology - Topical Calcineurin Inhibitor",
        "vietnamese_name": "Tacrolimus, Protopic",
        "administration": ["Topical"],
        "indications": [
            "Viêm da dị ứng (atopic dermatitis) trung bình đến nặng",
            "Viêm da dị ứng ở trẻ em (≥2 tuổi)",
            "Viêm da dị ứng ở vùng da nhạy cảm (mặt, cổ)",
            "Thay thế corticosteroid tại chỗ (tránh teo da)",
            "Viêm da dị ứng kháng trị với corticosteroid"
        ],
        "contraindications": [
            "Dị ứng tacrolimus",
            "Nhiễm trùng da (bacterial, fungal, viral) - không dùng trừ khi có kháng sinh/kháng nấm",
            "Trẻ em <2 tuổi - CHỐNG CHỈ ĐỊNH",
            "Ức chế miễn dịch (HIV, transplant) - thận trọng",
            "Ung thư da - thận trọng"
        ],
        "dosage": {
            "adult_topical_0.03%": "Bôi mỏng 2 lần/ngày lên vùng da bị ảnh hưởng (0.03% ointment)",
            "adult_topical_0.1%": "Bôi mỏng 2 lần/ngày lên vùng da bị ảnh hưởng (0.1% ointment)",
            "pediatric_≥2_years_0.03%": "Bôi mỏng 2 lần/ngày lên vùng da bị ảnh hưởng (0.03% ointment)",
            "notes": "Bôi ngay khi có dấu hiệu viêm da dị ứng. Có thể dùng kéo dài (không giới hạn thời gian như corticosteroid). Tránh ánh nắng mặt trời. 0.1% cho người lớn, 0.03% cho trẻ em ≥2 tuổi."
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "Không đổi",
            "under_30": "Không đổi"
        },
        "side_effects": [
            "Kích ứng da tại chỗ (đỏ, rát, ngứa, nóng rát) - phổ biến trong vài ngày đầu",
            "Nhiễm trùng da (herpes simplex, varicella zoster) - tăng nguy cơ",
            "Ung thư da (lymphoma, skin cancer) - nguy cơ tăng nhẹ (FDA warning)",
            "Hấp thu toàn thân (hiếm, nếu dùng diện rộng)",
            "Nhức đầu (hiếm)"
        ],
        "interactions": [
            "Corticosteroid tại chỗ: có thể dùng kết hợp (nhưng thường không cần)",
            "Thuốc ức chế miễn dịch: tăng nguy cơ nhiễm trùng",
            "CYP3A4 inhibitors (ketoconazole, erythromycin): tăng nồng độ tacrolimus (nếu hấp thu toàn thân)"
        ],
        "pregnancy": "C - Thận trọng",
        "mechanism_of_action": "Tacrolimus là calcineurin inhibitor tại chỗ. Ức chế calcineurin (enzyme cần thiết cho T-cell activation), dẫn đến: (1) Ức chế sản xuất cytokine (IL-2, IL-4, IL-5, TNF-α), (2) Ức chế T-cell activation và proliferation, (3) Giảm viêm và ngứa. Khác với corticosteroid tại chỗ, tacrolimus không gây teo da và có thể dùng kéo dài. Tacrolimus mạnh hơn pimecrolimus, phù hợp cho viêm da dị ứng trung bình đến nặng. ĐẶC ĐIỂM: (1) Không gây teo da (ưu điểm so với corticosteroid), (2) Có thể dùng kéo dài, (3) An toàn cho vùng da nhạy cảm (mặt, cổ), (4) Mạnh hơn pimecrolimus, (5) FDA warning về nguy cơ ung thư da (lymphoma, skin cancer) - nguy cơ tăng nhẹ, (6) Chỉ dùng cho viêm da dị ứng trung bình đến nặng (không dùng cho nhẹ).",
        "monitoring": [
            "Đáp ứng lâm sàng (giảm đỏ, sưng, ngứa)",
            "Dấu hiệu kích ứng da (đỏ, rát, ngứa, nóng rát tăng)",
            "Dấu hiệu nhiễm trùng da (mủ, đỏ, sưng tăng, herpes)",
            "Dấu hiệu ung thư da (nốt mới, thay đổi nốt cũ)",
            "Diện tích da điều trị (tránh >20% diện tích cơ thể)"
        ],
        "precautions": [
            "FDA warning về nguy cơ ung thư da (lymphoma, skin cancer) - nguy cơ tăng nhẹ",
            "CHỐNG CHỈ ĐỊNH ở trẻ em <2 tuổi",
            "Chỉ dùng cho viêm da dị ứng trung bình đến nặng (không dùng cho nhẹ)",
            "Tránh dùng trên vùng da bị loét, nhiễm trùng",
            "Tránh ánh nắng mặt trời (nhạy cảm ánh sáng, tăng nguy cơ ung thư da)",
            "Nguy cơ nhiễm trùng da (herpes simplex, varicella zoster) - tăng nguy cơ",
            "Thận trọng ở bệnh nhân ức chế miễn dịch (HIV, transplant)",
            "Nguy cơ hấp thu toàn thân nếu dùng diện rộng (>20% diện tích cơ thể)",
            "Kích ứng da tại chỗ phổ biến trong vài ngày đầu (thường giảm sau vài ngày)"
        ],
        "pharmacokinetics": {
            "half_life": "Không áp dụng (topical)",
            "onset": "Vài ngày đến 1 tuần",
            "duration": "Phụ thuộc tần suất dùng, có thể dùng kéo dài",
            "protein_binding": "Không áp dụng (topical)",
            "metabolism": "Chuyển hóa tại da và gan (nếu hấp thu toàn thân, CYP3A4)",
            "clearance": "Thải trừ qua nước tiểu (nếu hấp thu toàn thân)"
        },
        "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm, tránh ánh sáng. Đóng nắp kín sau khi dùng.",
        "black_box_warnings": "FDA warning: Nguy cơ ung thư da (lymphoma, skin cancer) - nguy cơ tăng nhẹ. Chỉ dùng cho viêm da dị ứng trung bình đến nặng không đáp ứng với điều trị khác. Tránh ánh nắng mặt trời. CHỐNG CHỈ ĐỊNH ở trẻ em <2 tuổi.",
        "drug_interactions": {
            "major": [],
            "moderate": [
                {
                    "drug": "CYP3A4 Inhibitors (Ketoconazole, Erythromycin, Clarithromycin)",
                    "mechanism": "Ức chế CYP3A4, tăng nồng độ tacrolimus (nếu hấp thu toàn thân)",
                    "effect": "Tăng nồng độ tacrolimus, tăng nguy cơ tác dụng phụ",
                    "management": "Thận trọng. Theo dõi dấu hiệu tác dụng phụ nếu hấp thu toàn thân."
                },
                {
                    "drug": "Corticosteroid tại chỗ mạnh",
                    "mechanism": "Có thể tăng nguy cơ ức chế miễn dịch và nhiễm trùng",
                    "effect": "Tăng nguy cơ nhiễm trùng da",
                    "management": "Thường không cần dùng kết hợp. Nếu cần, theo dõi dấu hiệu nhiễm trùng sát."
                }
            ],
            "minor": []
        },
        "contraindications": {
            "tuyệt_đối": [
                "Dị ứng tacrolimus",
                "Nhiễm trùng da (bacterial, fungal, viral) - không dùng trừ khi có kháng sinh/kháng nấm",
                "Trẻ em <2 tuổi - CHỐNG CHỈ ĐỊNH"
            ],
            "tương_đối": [
                "Ức chế miễn dịch (HIV, transplant) - thận trọng, tăng nguy cơ nhiễm trùng",
                "Ung thư da - thận trọng, tăng nguy cơ",
                "Dùng diện rộng (>20% diện tích cơ thể) - nguy cơ hấp thu toàn thân",
                "Phụ nữ có thai - thận trọng"
            ]
        },
        "contraindications_detail": {
            "tuyệt_đối": [
                "Dị ứng tacrolimus",
                "Nhiễm trùng da (bacterial, fungal, viral) - không dùng trừ khi có kháng sinh/kháng nấm",
                "Trẻ em <2 tuổi - CHỐNG CHỈ ĐỊNH"
            ],
            "tương_đối": [
                "Ức chế miễn dịch (HIV, transplant) - thận trọng, tăng nguy cơ nhiễm trùng",
                "Ung thư da - thận trọng, tăng nguy cơ",
                "Dùng diện rộng (>20% diện tích cơ thể) - nguy cơ hấp thu toàn thân",
                "Phụ nữ có thai - thận trọng"
            ]
        },
        "pregnancy_lactation": {
            "fda_category": "C",
            "pregnancy_details": "Tacrolimus là thuốc phân loại C. Không có nghiên cứu đầy đủ trên phụ nữ có thai. Tacrolimus có thể hấp thu toàn thân và qua nhau thai. Có thể dùng khi lợi ích vượt quá nguy cơ, đặc biệt khi không có lựa chọn khác.",
            "lactation": {
                "safety": "Compatible with Caution",
                "details": "Tacrolimus có thể hấp thu toàn thân và bài tiết vào sữa mẹ ở nồng độ thấp. Tuy nhiên, nồng độ trong sữa mẹ thấp và không có báo cáo về tác dụng phụ đáng kể ở trẻ bú mẹ khi dùng tại chỗ với diện tích nhỏ.",
                "recommendation": "Có thể dùng khi cho con bú, nhưng thận trọng. Tránh dùng diện rộng hoặc kéo dài. Tránh bôi lên vú hoặc núm vú."
            }
        },
        "hepatic_adjustment": {
            "mild": "Không cần điều chỉnh liều",
            "moderate": "Không cần điều chỉnh liều",
            "severe": "Không cần điều chỉnh liều (topical, hấp thu tối thiểu)",
            "notes": "Tacrolimus dùng tại chỗ, hấp thu toàn thân tối thiểu. Không cần điều chỉnh liều ở bệnh nhân suy gan."
        },
        "overdose_management": {
            "symptoms": [
                "Kích ứng da nặng",
                "Hấp thu toàn thân (nếu dùng diện rộng, kéo dài): ức chế miễn dịch, nhiễm trùng"
            ],
            "antidote": "Không có antidote đặc hiệu. Ngừng thuốc, điều trị hỗ trợ.",
            "treatment": [
                "Ngừng ngay tacrolimus",
                "Nếu kích ứng da nặng:",
                "  - Dưỡng ẩm da",
                "  - Corticosteroid tại chỗ yếu nếu cần",
                "Nếu hấp thu toàn thân:",
                "  - Theo dõi dấu hiệu nhiễm trùng",
                "  - Điều trị nhiễm trùng nếu có",
                "Theo dõi: Dấu hiệu sinh tồn, dấu hiệu nhiễm trùng"
            ],
            "monitoring": "Theo dõi dấu hiệu sinh tồn, dấu hiệu nhiễm trùng (nếu có hấp thu toàn thân) cho đến khi hồi phục."
        },
        "reversal_agents": {
            "available": False,
            "agents": [],
            "notes": "Không có antidote đặc hiệu. Điều trị quá liều chủ yếu là ngừng thuốc và điều trị hỗ trợ. Nếu có hấp thu toàn thân: theo dõi dấu hiệu nhiễm trùng và điều trị nếu cần."
        },
        "administration_instructions": {
            "oral": None,
            "topical": {
                "preparation": "Dạng ointment 0.03% hoặc 0.1%. 0.1% cho người lớn, 0.03% cho trẻ em ≥2 tuổi.",
                "application": "Bôi mỏng 2 lần/ngày lên vùng da bị ảnh hưởng. Massage nhẹ cho đến khi thấm. Rửa tay sau khi bôi.",
                "area": "Chỉ bôi lên vùng da bị ảnh thương. Có thể dùng trên vùng da nhạy cảm (mặt, cổ).",
                "duration": "Có thể dùng kéo dài (không giới hạn thời gian như corticosteroid). Bôi ngay khi có dấu hiệu viêm da dị ứng.",
                "notes": "QUAN TRỌNG: 1) Chỉ dùng cho viêm da dị ứng trung bình đến nặng, 2) CHỐNG CHỈ ĐỊNH ở trẻ em <2 tuổi, 3) Tránh ánh nắng mặt trời, 4) Tránh bôi lên vùng da bị loét, nhiễm trùng, 5) FDA warning về nguy cơ ung thư da, 6) Kích ứng da tại chỗ phổ biến trong vài ngày đầu."
            }
        },
        "risk_flags": {
            "high_alert": True,
            "narrow_therapeutic_index": False,
            "bleeding_risk": False,
            "organ_toxicity": ["Skin cancer (lymphoma, skin cancer) - slight increased risk (FDA warning) - CRITICAL", "Skin infections (herpes simplex, varicella zoster) - increased risk"],
            "qt_prolongation": False,
            "hepatotoxicity": False,
            "nephrotoxicity": False,
            "requires_monitoring": ["Clinical response (reduction in redness, swelling, itching)", "Signs of skin irritation (increased redness, burning, itching, stinging)", "Signs of skin infection (pus, increased redness/swelling, herpes) - CRITICAL", "Signs of skin cancer (new lesions, changes in existing lesions) - CRITICAL", "Treatment area (avoid >20% body surface area)"]
        },
        "guideline_tags": [
            "AAD Guidelines - Atopic Dermatitis",
            "FDA Black Box Warning - Tacrolimus Topical and Skin Cancer",
            "FDA Black Box Warning - Tacrolimus Topical and Age Restriction (<2 years)",
            "FDA Drug Information - Tacrolimus Topical"
        ],
        "references": {
            "primary_sources": [
                "FDA Drug Label - Tacrolimus (Protopic)",
                "UpToDate - Topical Calcineurin Inhibitors: Drug Information",
                "Medscape - Tacrolimus Drug Reference",
                "Goodman & Gilman's The Pharmacological Basis of Therapeutics (14th ed)"
            ],
            "last_updated": "2025-02-18",
            "evidence_level": "A - Dựa trên FDA drug labels, clinical guidelines, và dữ liệu lâm sàng từ nhiều nguồn"
        }
    },
    
    "Mupirocin topical": {
        "group": "Dermatology - Topical Antibiotic",
        "vietnamese_name": "Mupirocin, Bactroban",
        "administration": ["Topical"],
        "indications": [
            "Nhiễm trùng da do vi khuẩn (bacterial skin infections)",
            "Impetigo (Staphylococcus aureus, Streptococcus pyogenes)",
            "Viêm nang lông (folliculitis)",
            "Chốc lở (ecthyma)",
            "Vết thương nhiễm trùng",
            "Dự phòng nhiễm trùng sau phẫu thuật da"
        ],
        "contraindications": [
            "Dị ứng mupirocin hoặc polyethylene glycol",
            "Nhiễm trùng do virus hoặc nấm (không hiệu quả)"
        ],
        "dosage": {
            "adult_topical": "Bôi mỏng 3 lần/ngày lên vùng da bị ảnh hưởng, trong 5-10 ngày",
            "pediatric": "Bôi mỏng 3 lần/ngày lên vùng da bị ảnh hưởng, trong 5-10 ngày",
            "notes": "Mupirocin là kháng sinh tại chỗ, hiệu quả với Staphylococcus aureus (kể cả MRSA) và Streptococcus pyogenes. Dùng 3 lần/ngày trong 5-10 ngày. Che phủ vùng da bị ảnh hưởng bằng băng gạc nếu cần."
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "Không đổi",
            "under_30": "Không đổi"
        },
        "side_effects": [
            "Kích ứng da tại chỗ (đỏ, rát, ngứa) - phổ biến",
            "Khô da",
            "Phản ứng dị ứng (phát ban, ngứa) - hiếm",
            "Kháng thuốc (nếu dùng kéo dài hoặc không đúng cách)"
        ],
        "interactions": [
            "Không có tương tác đáng kể với thuốc khác (topical)"
        ],
        "pregnancy": "B - An toàn",
        "mechanism_of_action": "Mupirocin là kháng sinh tại chỗ, ức chế enzyme isoleucyl-tRNA synthetase của vi khuẩn, ngăn chặn sự tổng hợp protein, dẫn đến tiêu diệt vi khuẩn (bactericidal). Mupirocin hiệu quả với Staphylococcus aureus (kể cả MRSA - methicillin-resistant S. aureus) và Streptococcus pyogenes. ĐẶC ĐIỂM: (1) Hiệu quả với S. aureus (kể cả MRSA) và S. pyogenes, (2) Bactericidal (tiêu diệt vi khuẩn), (3) Dùng 3 lần/ngày trong 5-10 ngày, (4) Nguy cơ kháng thuốc nếu dùng kéo dài hoặc không đúng cách, (5) An toàn, ít tác dụng phụ.",
        "monitoring": [
            "Đáp ứng lâm sàng (giảm đỏ, sưng, mủ) - cải thiện sau 2-3 ngày",
            "Dấu hiệu kích ứng da (đỏ, rát, ngứa tăng)",
            "Dấu hiệu nhiễm trùng (mủ, đỏ, sưng tăng) - nếu không cải thiện",
            "Dấu hiệu kháng thuốc (nhiễm trùng không cải thiện sau 5-7 ngày)"
        ],
        "precautions": [
            "CHỈ DÙNG CHO NHIỄM TRÙNG DO VI KHUẨN - không hiệu quả với virus hoặc nấm",
            "Dùng đủ liều và đủ thời gian (5-10 ngày) để tránh kháng thuốc",
            "Không dùng kéo dài (>10 ngày) - nguy cơ kháng thuốc",
            "Kích ứng da - phổ biến, thường giảm sau vài ngày",
            "Tránh bôi lên vùng da bị loét rộng hoặc vết thương sâu",
            "Rửa tay sau khi bôi",
            "Che phủ vùng da bị ảnh hưởng bằng băng gạc nếu cần"
        ],
        "pharmacokinetics": {
            "half_life": "Không áp dụng (topical)",
            "onset": "Ngay lập tức",
            "duration": "4-6 giờ (dùng 3 lần/ngày)",
            "protein_binding": "Không áp dụng (topical)",
            "metabolism": "Chuyển hóa tại da thành monic acid (không hoạt động)",
            "clearance": "Thải trừ tại chỗ, không hấp thu toàn thân"
        },
        "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm, tránh ánh sáng. Đóng nắp kín sau khi dùng. Dùng trong 4 tuần sau khi mở.",
        "black_box_warnings": None,
        "drug_interactions": {
            "major": [],
            "moderate": [],
            "minor": []
        },
        "contraindications": {
            "tuyệt_đối": [
                "Dị ứng mupirocin hoặc polyethylene glycol",
                "Nhiễm trùng do virus hoặc nấm - không hiệu quả"
            ],
            "tương_đối": [
                "Dùng kéo dài (>10 ngày) - nguy cơ kháng thuốc",
                "Vết thương sâu hoặc loét rộng - thận trọng"
            ]
        },
        "pregnancy_lactation": {
            "fda_category": "B",
            "pregnancy_details": "Mupirocin là thuốc phân loại B. Không hấp thu toàn thân khi dùng tại chỗ. An toàn trong thai kỳ.",
            "lactation": {
                "safety": "Compatible",
                "details": "Mupirocin không hấp thu toàn thân khi dùng tại chỗ, không bài tiết vào sữa mẹ. An toàn khi cho con bú.",
                "recommendation": "Có thể dùng khi cho con bú. An toàn, không có tác dụng phụ."
            }
        },
        "hepatic_adjustment": {
            "mild": "Không cần điều chỉnh liều",
            "moderate": "Không cần điều chỉnh liều",
            "severe": "Không cần điều chỉnh liều (topical, không hấp thu toàn thân)",
            "notes": "Mupirocin không hấp thu toàn thân khi dùng tại chỗ. Không cần điều chỉnh liều ở bệnh nhân suy gan."
        },
        "overdose_management": {
            "symptoms": [
                "Kích ứng da nặng",
                "Đỏ da, rát da"
            ],
            "antidote": "Không có antidote đặc hiệu. Rửa da, điều trị hỗ trợ.",
            "treatment": [
                "Rửa da ngay với nước sạch và xà phòng",
                "Nếu kích ứng da nặng:",
                "  - Ngừng mupirocin",
                "  - Dưỡng ẩm da",
                "  - Corticosteroid tại chỗ yếu nếu cần",
                "Theo dõi: Dấu hiệu kích ứng da"
            ],
            "monitoring": "Theo dõi dấu hiệu kích ứng da cho đến khi hồi phục."
        },
        "reversal_agents": None,
        "administration_instructions": {
            "oral": None,
            "topical": {
                "preparation": "Dạng ointment 2%.",
                "application": "Bôi mỏng 3 lần/ngày lên vùng da bị ảnh hưởng. Massage nhẹ cho đến khi thấm. Rửa tay sau khi bôi.",
                "area": "Chỉ bôi lên vùng da bị nhiễm trùng. Che phủ bằng băng gạc nếu cần.",
                "duration": "5-10 ngày. Không dùng kéo dài (>10 ngày) để tránh kháng thuốc.",
                "notes": "QUAN TRỌNG: 1) CHỈ DÙNG CHO NHIỄM TRÙNG DO VI KHUẨN, 2) Dùng đủ liều và đủ thời gian (5-10 ngày), 3) Không dùng kéo dài (>10 ngày), 4) Rửa tay sau khi bôi, 5) Che phủ bằng băng gạc nếu cần."
            }
        },
        "references": {
            "primary_sources": [
                "FDA Drug Label - Mupirocin (Bactroban)",
                "UpToDate - Mupirocin: Drug Information",
                "Medscape - Mupirocin Drug Reference",
                "IDSA Guidelines - Skin and Soft Tissue Infections"
            ],
            "last_updated": "2025-02-18",
            "evidence_level": "A - Dựa trên FDA drug labels, clinical guidelines, và dữ liệu lâm sàng từ nhiều nguồn"
        }
    },
    
    "Tretinoin topical": {
        "group": "Dermatology - Topical Retinoid (Acne)",
        "vietnamese_name": "Tretinoin, Retin-A, Renova",
        "administration": ["Topical"],
        "indications": [
            "Mụn trứng cá (acne vulgaris)",
            "Mụn đầu đen (comedonal acne)",
            "Mụn viêm (inflammatory acne)",
            "Làm mịn nếp nhăn (fine wrinkles) - Renova",
            "Tăng sắc tố da (hyperpigmentation)",
            "Sừng hóa nang lông (keratosis pilaris)"
        ],
        "contraindications": [
            "Dị ứng tretinoin hoặc retinoid",
            "Eczema nặng",
            "Viêm da nặng",
            "Phụ nữ có thai - CHỐNG CHỈ ĐỊNH",
            "Phụ nữ đang cho con bú - thận trọng"
        ],
        "dosage": {
            "adult_acne_0.025%": "Bôi mỏng 1 lần/ngày (buổi tối) lên vùng da bị ảnh hưởng (0.025% cream/gel)",
            "adult_acne_0.05%": "Bôi mỏng 1 lần/ngày (buổi tối) lên vùng da bị ảnh hưởng (0.05% cream/gel)",
            "adult_acne_0.1%": "Bôi mỏng 1 lần/ngày (buổi tối) lên vùng da bị ảnh hưởng (0.1% cream/gel)",
            "adult_wrinkles_0.02%": "Bôi mỏng 1 lần/ngày (buổi tối) lên mặt (0.02% cream - Renova)",
            "notes": "Tretinoin là retinoid tại chỗ, điều trị mụn trứng cá. Bắt đầu với nồng độ thấp (0.025%), tăng dần nếu cần. Dùng buổi tối, tránh ánh nắng mặt trời. Có thể gây kích ứng da trong vài tuần đầu."
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "Không đổi",
            "under_30": "Không đổi"
        },
        "side_effects": [
            "Kích ứng da (đỏ, rát, khô, bong tróc) - phổ biến trong vài tuần đầu",
            "Nhạy cảm với ánh sáng (photosensitivity) - phổ biến",
            "Khô da",
            "Bong tróc da",
            "Ngứa",
            "Phản ứng dị ứng (phát ban, ngứa) - hiếm",
            "Tăng sắc tố da tạm thời (hiếm)"
        ],
        "interactions": [
            "Các sản phẩm làm khô da (benzoyl peroxide, salicylic acid): tăng kích ứng da",
            "Các sản phẩm chứa cồn: tăng kích ứng da",
            "Các sản phẩm chứa sulfur, resorcinol: tăng kích ứng da"
        ],
        "pregnancy": "X - CHỐNG CHỈ ĐỊNH",
        "mechanism_of_action": "Tretinoin là retinoid (vitamin A derivative) tại chỗ. Gắn với thụ thể retinoic acid (RAR) trong tế bào, điều hòa biểu hiện gen, dẫn đến: (1) Tăng tẩy tế bào chết (desquamation), giảm bít tắc nang lông, (2) Giảm sản xuất bã nhờn (sebum), (3) Giảm viêm, (4) Tăng tổng hợp collagen (làm mịn nếp nhăn). Dẫn đến: giảm mụn trứng cá, làm mịn nếp nhăn. ĐẶC ĐIỂM: (1) Retinoid tại chỗ, điều trị mụn trứng cá, (2) Bắt đầu với nồng độ thấp (0.025%), tăng dần nếu cần, (3) Dùng buổi tối, tránh ánh nắng mặt trời, (4) Kích ứng da phổ biến trong vài tuần đầu, (5) CHỐNG CHỈ ĐỊNH ở phụ nữ có thai (category X), (6) Nhạy cảm với ánh sáng - phổ biến.",
        "monitoring": [
            "Đáp ứng lâm sàng (giảm mụn) - cải thiện sau 4-8 tuần",
            "Dấu hiệu kích ứng da (đỏ, rát, khô, bong tróc) - phổ biến trong vài tuần đầu",
            "Dấu hiệu nhạy cảm với ánh sáng (đỏ, rát khi tiếp xúc ánh nắng)",
            "Dấu hiệu phản ứng dị ứng (phát ban, ngứa)"
        ],
        "precautions": [
            "CHỐNG CHỈ ĐỊNH ở phụ nữ có thai (category X) - gây dị tật bẩm sinh",
            "Bắt đầu với nồng độ thấp (0.025%), tăng dần nếu cần",
            "Kích ứng da phổ biến trong vài tuần đầu - thường giảm sau vài tuần",
            "Dùng buổi tối, tránh ánh nắng mặt trời (nhạy cảm ánh sáng)",
            "Bôi kem chống nắng (SPF ≥30) vào ban ngày",
            "Tránh dùng với các sản phẩm làm khô da (benzoyl peroxide, salicylic acid) cùng lúc",
            "Tránh dùng với các sản phẩm chứa cồn",
            "Không dùng trên vùng da bị eczema hoặc viêm da nặng",
            "Tránh bôi lên vùng da quanh mắt, miệng"
        ],
        "pharmacokinetics": {
            "half_life": "Không áp dụng (topical)",
            "onset": "4-8 tuần",
            "duration": "Phụ thuộc tần suất dùng",
            "protein_binding": "Không áp dụng (topical)",
            "metabolism": "Chuyển hóa tại da và gan (nếu hấp thu toàn thân)",
            "clearance": "Thải trừ qua nước tiểu (nếu hấp thu toàn thân)"
        },
        "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm, tránh ánh sáng. Đóng nắp kín sau khi dùng. Không để đông lạnh.",
        "black_box_warnings": "CHỐNG CHỈ ĐỊNH ở phụ nữ có thai (category X). Tretinoin gây dị tật bẩm sinh ở động vật. Phụ nữ trong độ tuổi sinh đẻ phải sử dụng biện pháp tránh thai hiệu quả.",
        "drug_interactions": {
            "major": [],
            "moderate": [
                {
                    "drug": "Benzoyl Peroxide, Salicylic Acid",
                    "mechanism": "Cả hai đều làm khô da, tác dụng cộng dồn",
                    "effect": "Tăng kích ứng da",
                    "management": "Tránh dùng cùng lúc. Dùng cách nhau ít nhất 1 giờ, hoặc dùng vào thời điểm khác trong ngày."
                },
                {
                    "drug": "Các sản phẩm chứa cồn",
                    "mechanism": "Cồn làm khô da, tác dụng cộng dồn",
                    "effect": "Tăng kích ứng da",
                    "management": "Tránh dùng cùng lúc."
                }
            ],
            "minor": []
        },
        "contraindications": {
            "tuyệt_đối": [
                "Dị ứng tretinoin hoặc retinoid",
                "Phụ nữ có thai - CHỐNG CHỈ ĐỊNH (category X, gây dị tật bẩm sinh)",
                "Eczema nặng - CHỐNG CHỈ ĐỊNH",
                "Viêm da nặng - CHỐNG CHỈ ĐỊNH"
            ],
            "tương_đối": [
                "Phụ nữ đang cho con bú - thận trọng",
                "Da nhạy cảm - bắt đầu với nồng độ thấp",
                "Đang dùng các sản phẩm làm khô da - tăng kích ứng"
            ]
        },
        "contraindications_detail": {
            "tuyệt_đối": [
                "Dị ứng tretinoin hoặc retinoid",
                "Phụ nữ có thai - CHỐNG CHỈ ĐỊNH (category X, gây dị tật bẩm sinh)",
                "Eczema nặng - CHỐNG CHỈ ĐỊNH",
                "Viêm da nặng - CHỐNG CHỈ ĐỊNH"
            ],
            "tương_đối": [
                "Phụ nữ đang cho con bú - thận trọng",
                "Da nhạy cảm - bắt đầu với nồng độ thấp",
                "Đang dùng các sản phẩm làm khô da - tăng kích ứng"
            ]
        },
        "pregnancy_lactation": {
            "fda_category": "X",
            "pregnancy_details": "Tretinoin là thuốc phân loại X. CHỐNG CHỈ ĐỊNH ở phụ nữ có thai. Tretinoin gây dị tật bẩm sinh ở động vật. Phụ nữ trong độ tuổi sinh đẻ phải sử dụng biện pháp tránh thai hiệu quả khi dùng tretinoin.",
            "lactation": {
                "safety": "Compatible with Caution",
                "details": "Tretinoin có thể hấp thu toàn thân và bài tiết vào sữa mẹ ở nồng độ thấp. Tuy nhiên, nồng độ trong sữa mẹ thấp và không có báo cáo về tác dụng phụ đáng kể ở trẻ bú mẹ khi dùng tại chỗ.",
                "recommendation": "Có thể dùng khi cho con bú, nhưng thận trọng. Tránh bôi lên vú hoặc núm vú."
            }
        },
        "hepatic_adjustment": {
            "mild": "Không cần điều chỉnh liều",
            "moderate": "Không cần điều chỉnh liều",
            "severe": "Không cần điều chỉnh liều (topical, hấp thu tối thiểu)",
            "notes": "Tretinoin dùng tại chỗ, hấp thu toàn thân tối thiểu. Không cần điều chỉnh liều ở bệnh nhân suy gan."
        },
        "overdose_management": {
            "symptoms": [
                "Kích ứng da nặng (đỏ, rát, khô, bong tróc)",
                "Nhạy cảm với ánh sáng nặng"
            ],
            "antidote": "Không có antidote đặc hiệu. Ngừng thuốc, điều trị hỗ trợ.",
            "treatment": [
                "Ngừng ngay tretinoin",
                "Dưỡng ẩm da",
                "Tránh ánh nắng mặt trời",
                "Bôi kem chống nắng (SPF ≥30)",
                "Corticosteroid tại chỗ yếu nếu kích ứng nặng",
                "Theo dõi: Dấu hiệu kích ứng da, dấu hiệu nhạy cảm với ánh sáng"
            ],
            "monitoring": "Theo dõi dấu hiệu kích ứng da, dấu hiệu nhạy cảm với ánh sáng cho đến khi hồi phục."
        },
        "reversal_agents": {
            "available": False,
            "agents": [],
            "notes": "Không có antidote đặc hiệu. Điều trị quá liều chủ yếu là ngừng thuốc và điều trị hỗ trợ. Dưỡng ẩm da, tránh ánh nắng mặt trời, bôi kem chống nắng (SPF ≥30)."
        },
        "administration_instructions": {
            "oral": None,
            "topical": {
                "preparation": "Dạng cream hoặc gel 0.025%, 0.05%, 0.1%. Renova 0.02% cho nếp nhăn.",
                "application": "Bôi mỏng 1 lần/ngày (buổi tối) lên vùng da bị ảnh hưởng. Massage nhẹ cho đến khi thấm. Rửa tay sau khi bôi.",
                "area": "Chỉ bôi lên vùng da bị mụn. Tránh bôi lên vùng da quanh mắt, miệng.",
                "timing": "Buổi tối, tránh ánh nắng mặt trời. Bôi kem chống nắng (SPF ≥30) vào ban ngày.",
                "duration": "Điều trị thường 8-12 tuần. Có thể dùng kéo dài để duy trì.",
                "notes": "QUAN TRỌNG: 1) CHỐNG CHỈ ĐỊNH ở phụ nữ có thai, 2) Bắt đầu với nồng độ thấp (0.025%), 3) Dùng buổi tối, tránh ánh nắng mặt trời, 4) Kích ứng da phổ biến trong vài tuần đầu, 5) Bôi kem chống nắng (SPF ≥30) vào ban ngày, 6) Tránh dùng với các sản phẩm làm khô da cùng lúc."
            }
        },
        "references": {
            "primary_sources": [
                "FDA Drug Label - Tretinoin (Retin-A, Renova)",
                "UpToDate - Tretinoin: Drug Information",
                "Medscape - Tretinoin Drug Reference",
                "AAD Guidelines - Acne Treatment"
            ],
            "last_updated": "2025-02-18",
            "evidence_level": "A - Dựa trên FDA drug labels, clinical guidelines, và dữ liệu lâm sàng từ nhiều nguồn"
        }
    },
    
    "Benzoyl peroxide topical": {
        "group": "Dermatology - Topical Antiseptic (Acne)",
        "vietnamese_name": "Benzoyl Peroxide, Clearasil, Oxy",
        "administration": ["Topical"],
        "indications": [
            "Mụn trứng cá (acne vulgaris)",
            "Mụn đầu đen (comedonal acne)",
            "Mụn viêm (inflammatory acne)",
            "Nhiễm trùng da nhẹ"
        ],
        "contraindications": [
            "Dị ứng benzoyl peroxide",
            "Eczema nặng",
            "Viêm da nặng"
        ],
        "dosage": {
            "adult_acne_2.5%": "Bôi mỏng 1-2 lần/ngày lên vùng da bị ảnh hưởng (2.5% gel/cream)",
            "adult_acne_5%": "Bôi mỏng 1-2 lần/ngày lên vùng da bị ảnh hưởng (5% gel/cream)",
            "adult_acne_10%": "Bôi mỏng 1 lần/ngày lên vùng da bị ảnh hưởng (10% gel/cream)",
            "notes": "Benzoyl peroxide là thuốc kháng khuẩn và tẩy tế bào chết, điều trị mụn trứng cá. Bắt đầu với nồng độ thấp (2.5-5%), tăng dần nếu cần. Có thể gây khô da và làm bạc màu vải, tóc."
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "Không đổi",
            "under_30": "Không đổi"
        },
        "side_effects": [
            "Khô da - phổ biến",
            "Kích ứng da (đỏ, rát, ngứa) - phổ biến",
            "Bong tróc da",
            "Làm bạc màu vải, tóc - phổ biến",
            "Phản ứng dị ứng (phát ban, ngứa) - hiếm",
            "Nhạy cảm với ánh sáng (nhẹ) - hiếm"
        ],
        "interactions": [
            "Tretinoin: tăng kích ứng da nếu dùng cùng lúc",
            "Các sản phẩm làm khô da: tăng kích ứng da"
        ],
        "pregnancy": "C - Thận trọng",
        "mechanism_of_action": "Benzoyl peroxide là thuốc kháng khuẩn và tẩy tế bào chết. Tác dụng: (1) Kháng khuẩn - tiêu diệt Propionibacterium acnes (vi khuẩn gây mụn), (2) Tẩy tế bào chết - làm bong lớp sừng, giảm bít tắc nang lông, (3) Giảm viêm. Dẫn đến: giảm mụn trứng cá. ĐẶC ĐIỂM: (1) Kháng khuẩn và tẩy tế bào chết, (2) Bắt đầu với nồng độ thấp (2.5-5%), tăng dần nếu cần, (3) Khô da và kích ứng da phổ biến, (4) Làm bạc màu vải, tóc - phổ biến, (5) Có thể dùng kết hợp với tretinoin (dùng cách nhau ít nhất 1 giờ).",
        "monitoring": [
            "Đáp ứng lâm sàng (giảm mụn) - cải thiện sau 4-8 tuần",
            "Dấu hiệu kích ứng da (đỏ, rát, khô, bong tróc)",
            "Dấu hiệu phản ứng dị ứng (phát ban, ngứa)"
        ],
        "precautions": [
            "Bắt đầu với nồng độ thấp (2.5-5%), tăng dần nếu cần",
            "Khô da và kích ứng da phổ biến - dưỡng ẩm da nếu cần",
            "Làm bạc màu vải, tóc - tránh tiếp xúc với vải, tóc",
            "Tránh dùng với tretinoin cùng lúc (dùng cách nhau ít nhất 1 giờ)",
            "Tránh dùng trên vùng da bị eczema hoặc viêm da nặng",
            "Tránh bôi lên vùng da quanh mắt, miệng",
            "Bôi kem chống nắng (SPF ≥30) vào ban ngày nếu nhạy cảm với ánh sáng"
        ],
        "pharmacokinetics": {
            "half_life": "Không áp dụng (topical)",
            "onset": "4-8 tuần",
            "duration": "Phụ thuộc tần suất dùng",
            "protein_binding": "Không áp dụng (topical)",
            "metabolism": "Chuyển hóa tại da thành benzoic acid",
            "clearance": "Thải trừ tại chỗ, không hấp thu toàn thân"
        },
        "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm, tránh ánh sáng. Đóng nắp kín sau khi dùng.",
        "black_box_warnings": None,
        "drug_interactions": {
            "major": [],
            "moderate": [
                {
                    "drug": "Tretinoin",
                    "mechanism": "Cả hai đều làm khô da, tác dụng cộng dồn",
                    "effect": "Tăng kích ứng da",
                    "management": "Tránh dùng cùng lúc. Dùng cách nhau ít nhất 1 giờ, hoặc dùng vào thời điểm khác trong ngày."
                }
            ],
            "minor": []
        },
        "contraindications": {
            "tuyệt_đối": [
                "Dị ứng benzoyl peroxide",
                "Eczema nặng - CHỐNG CHỈ ĐỊNH",
                "Viêm da nặng - CHỐNG CHỈ ĐỊNH"
            ],
            "tương_đối": [
                "Da nhạy cảm - bắt đầu với nồng độ thấp",
                "Đang dùng tretinoin - tăng kích ứng"
            ]
        },
        "pregnancy_lactation": {
            "fda_category": "C",
            "pregnancy_details": "Benzoyl peroxide là thuốc phân loại C. Không có nghiên cứu đầy đủ trên phụ nữ có thai. Benzoyl peroxide không hấp thu toàn thân khi dùng tại chỗ. Có thể dùng khi lợi ích vượt quá nguy cơ.",
            "lactation": {
                "safety": "Compatible",
                "details": "Benzoyl peroxide không hấp thu toàn thân khi dùng tại chỗ, không bài tiết vào sữa mẹ. An toàn khi cho con bú.",
                "recommendation": "Có thể dùng khi cho con bú. An toàn, không có tác dụng phụ."
            }
        },
        "hepatic_adjustment": {
            "mild": "Không cần điều chỉnh liều",
            "moderate": "Không cần điều chỉnh liều",
            "severe": "Không cần điều chỉnh liều (topical, không hấp thu toàn thân)",
            "notes": "Benzoyl peroxide không hấp thu toàn thân khi dùng tại chỗ. Không cần điều chỉnh liều ở bệnh nhân suy gan."
        },
        "overdose_management": {
            "symptoms": [
                "Kích ứng da nặng (đỏ, rát, khô, bong tróc)",
                "Khô da nặng"
            ],
            "antidote": "Không có antidote đặc hiệu. Ngừng thuốc, điều trị hỗ trợ.",
            "treatment": [
                "Ngừng ngay benzoyl peroxide",
                "Dưỡng ẩm da",
                "Corticosteroid tại chỗ yếu nếu kích ứng nặng",
                "Theo dõi: Dấu hiệu kích ứng da"
            ],
            "monitoring": "Theo dõi dấu hiệu kích ứng da cho đến khi hồi phục."
        },
        "reversal_agents": None,
        "administration_instructions": {
            "oral": None,
            "topical": {
                "preparation": "Dạng gel, cream, lotion, wash 2.5%, 5%, 10%.",
                "application": "Bôi mỏng 1-2 lần/ngày lên vùng da bị ảnh hưởng. Massage nhẹ cho đến khi thấm. Rửa tay sau khi bôi.",
                "area": "Chỉ bôi lên vùng da bị mụn. Tránh bôi lên vùng da quanh mắt, miệng.",
                "timing": "1-2 lần/ngày. Có thể dùng vào buổi sáng hoặc buổi tối.",
                "duration": "Điều trị thường 8-12 tuần. Có thể dùng kéo dài để duy trì.",
                "notes": "QUAN TRỌNG: 1) Bắt đầu với nồng độ thấp (2.5-5%), 2) Khô da và kích ứng da phổ biến, 3) Làm bạc màu vải, tóc, 4) Tránh dùng với tretinoin cùng lúc, 5) Dưỡng ẩm da nếu cần."
            }
        },
        "references": {
            "primary_sources": [
                "FDA Drug Label - Benzoyl Peroxide",
                "UpToDate - Benzoyl Peroxide: Drug Information",
                "Medscape - Benzoyl Peroxide Drug Reference",
                "AAD Guidelines - Acne Treatment"
            ],
            "last_updated": "2025-02-18",
            "evidence_level": "A - Dựa trên FDA drug labels, clinical guidelines, và dữ liệu lâm sàng từ nhiều nguồn"
        },
        "risk_flags": {
            "high_alert": False,
            "narrow_therapeutic_index": False,
            "bleeding_risk": False,
            "organ_toxicity": [],
            "qt_prolongation": False,
            "hepatotoxicity": False,
            "nephrotoxicity": False,
            "requires_monitoring": ["Clinical response (reduction in acne)", "Signs of skin irritation (redness, dryness, peeling)", "Signs of allergic reaction"]
        },
        "guideline_tags": [
            "AAD Guidelines - Acne Treatment",
            "FDA Drug Information - Benzoyl Peroxide",
            "UpToDate - Acne Treatment"
        ]
    },
    
    "Triamcinolone topical": {
        "group": "Dermatology - Topical Corticosteroid (Medium Potency)",
        "vietnamese_name": "Triamcinolone, Kenalog, Aristocort",
        "administration": ["Topical"],
        "indications": [
            "Viêm da dị ứng (atopic dermatitis) trung bình",
            "Vảy nến (psoriasis) trung bình",
            "Viêm da tiếp xúc (contact dermatitis) trung bình",
            "Eczema trung bình",
            "Lichen planus",
            "Phát ban dị ứng"
        ],
        "contraindications": [
            "Dị ứng triamcinolone hoặc corticosteroid",
            "Nhiễm trùng da (bacterial, fungal, viral) - không dùng trừ khi có kháng sinh/kháng nấm",
            "Loét da"
        ],
        "dosage": {
            "adult_topical_0.025%": "Bôi mỏng 2-4 lần/ngày lên vùng da bị ảnh hưởng (0.025% cream/ointment)",
            "adult_topical_0.1%": "Bôi mỏng 2-4 lần/ngày lên vùng da bị ảnh hưởng (0.1% cream/ointment)",
            "adult_topical_0.5%": "Bôi mỏng 2 lần/ngày lên vùng da bị ảnh hưởng (0.5% cream/ointment)",
            "adult_max_duration": "Tối đa 2-4 tuần liên tục (tránh dùng kéo dài)",
            "notes": "Triamcinolone là corticosteroid trung bình (medium potency, nhóm III-V). Phù hợp cho tổn thương trung bình. Tránh dùng trên mặt, nách, bẹn (da mỏng, hấp thu cao). Không dùng >2-4 tuần liên tục."
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "Không đổi",
            "under_30": "Không đổi"
        },
        "side_effects": [
            "Teo da (skin atrophy) - phổ biến nếu dùng kéo dài",
            "Giãn mạch (telangiectasia)",
            "Rạn da (striae)",
            "Mụn trứng cá (acne)",
            "Viêm nang lông (folliculitis)",
            "Nhiễm trùng da thứ phát (bacterial, fungal)",
            "Ức chế trục HPA (nếu dùng diện rộng, kéo dài)",
            "Hấp thu toàn thân (nếu dùng diện rộng, kéo dài)"
        ],
        "interactions": [
            "Không có tương tác đáng kể với thuốc khác (topical)"
        ],
        "pregnancy": "C - Thận trọng",
        "mechanism_of_action": "Triamcinolone là corticosteroid tổng hợp, medium potency (nhóm III-V). Gắn với thụ thể glucocorticoid trong tế bào, điều hòa biểu hiện gen, dẫn đến: (1) Ức chế viêm (giảm cytokine, chemokine, adhesion molecules), (2) Ức chế miễn dịch (giảm T-cell activation, cytokine production), (3) Co mạch (giảm đỏ, sưng), (4) Ức chế tăng sinh tế bào (giảm vảy nến). Triamcinolone có độ mạnh trung bình, phù hợp cho tổn thương trung bình. ĐẶC ĐIỂM: (1) Medium potency (nhóm III-V), (2) Phù hợp cho tổn thương trung bình, (3) Không dùng >2-4 tuần liên tục, (4) Tránh dùng trên mặt, nách, bẹn, (5) Nguy cơ teo da và ức chế HPA nếu dùng kéo dài.",
        "monitoring": [
            "Đáp ứng lâm sàng (giảm đỏ, sưng, ngứa)",
            "Dấu hiệu teo da (da mỏng, nhăn, giãn mạch)",
            "Dấu hiệu nhiễm trùng da (mủ, đỏ, sưng tăng)",
            "Dấu hiệu ức chế HPA (nếu dùng diện rộng, kéo dài): mệt mỏi, hạ huyết áp, hạ đường huyết",
            "Diện tích da điều trị (tránh >20% diện tích cơ thể)"
        ],
        "precautions": [
            "Triamcinolone là corticosteroid trung bình - phù hợp cho tổn thương trung bình",
            "KHÔNG dùng >2-4 tuần liên tục (nguy cơ teo da, ức chế HPA)",
            "Tránh dùng trên mặt, nách, bẹn (da mỏng, hấp thu cao)",
            "Tránh dùng trên vùng da bị loét, nhiễm trùng",
            "Nếu cần dùng kéo dài: giảm tần suất (q2-3 ngày) hoặc chuyển sang corticosteroid yếu hơn",
            "Nguy cơ hấp thu toàn thân nếu dùng diện rộng (>20% diện tích cơ thể) hoặc kéo dài",
            "Trẻ em: thận trọng, giảm liều, tránh dùng kéo dài",
            "Phụ nữ có thai: thận trọng, tránh dùng diện rộng",
            "Bảo vệ khỏi ánh nắng mặt trời (nhạy cảm ánh sáng)"
        ],
        "pharmacokinetics": {
            "half_life": "Không áp dụng (topical)",
            "onset": "Vài ngày đến 1 tuần",
            "duration": "Phụ thuộc tần suất dùng",
            "protein_binding": "Không áp dụng (topical)",
            "metabolism": "Chuyển hóa tại da và gan (nếu hấp thu toàn thân)",
            "clearance": "Thải trừ qua nước tiểu (nếu hấp thu toàn thân)"
        },
        "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm, tránh ánh sáng. Đóng nắp kín sau khi dùng.",
        "black_box_warnings": None,
        "drug_interactions": {
            "major": [],
            "moderate": [],
            "minor": []
        },
        "contraindications": {
            "tuyệt_đối": [
                "Dị ứng triamcinolone hoặc corticosteroid",
                "Nhiễm trùng da (bacterial, fungal, viral) - không dùng trừ khi có kháng sinh/kháng nấm",
                "Loét da"
            ],
            "tương_đối": [
                "Trẻ em - thận trọng, giảm liều, tránh dùng kéo dài",
                "Phụ nữ có thai - thận trọng, tránh dùng diện rộng",
                "Da mỏng (mặt, nách, bẹn) - tránh dùng (hấp thu cao)",
                "Dùng diện rộng (>20% diện tích cơ thể) - nguy cơ hấp thu toàn thân",
                "Dùng kéo dài (>2-4 tuần) - nguy cơ teo da, ức chế HPA"
            ]
        },
        "pregnancy_lactation": {
            "fda_category": "C",
            "pregnancy_details": "Triamcinolone là thuốc phân loại C. Corticosteroid tại chỗ có thể hấp thu toàn thân, đặc biệt khi dùng diện rộng hoặc kéo dài. Corticosteroid có thể qua nhau thai và có thể gây ức chế thượng thận ở thai nhi. Tránh dùng diện rộng hoặc kéo dài trong thai kỳ. Chỉ dùng khi lợi ích vượt quá nguy cơ.",
            "lactation": {
                "safety": "Compatible with Caution",
                "details": "Triamcinolone có thể hấp thu toàn thân và bài tiết vào sữa mẹ ở nồng độ thấp. Tuy nhiên, nồng độ trong sữa mẹ thấp và không có báo cáo về tác dụng phụ đáng kể ở trẻ bú mẹ khi dùng tại chỗ với diện tích nhỏ.",
                "recommendation": "Có thể dùng khi cho con bú, nhưng thận trọng. Tránh dùng diện rộng hoặc kéo dài. Tránh bôi lên vú hoặc núm vú."
            }
        },
        "hepatic_adjustment": {
            "mild": "Không cần điều chỉnh liều",
            "moderate": "Không cần điều chỉnh liều",
            "severe": "Không cần điều chỉnh liều (topical, hấp thu tối thiểu)",
            "notes": "Triamcinolone dùng tại chỗ, hấp thu toàn thân tối thiểu. Không cần điều chỉnh liều ở bệnh nhân suy gan."
        },
        "overdose_management": {
            "symptoms": [
                "Teo da nặng",
                "Ức chế trục HPA (mệt mỏi, hạ huyết áp, hạ đường huyết)",
                "Hấp thu toàn thân (nếu dùng diện rộng, kéo dài)"
            ],
            "antidote": "Không có antidote đặc hiệu. Ngừng thuốc, điều trị hỗ trợ.",
            "treatment": [
                "Ngừng ngay triamcinolone",
                "Nếu ức chế HPA:",
                "  - Hydrocortisone thay thế nếu cần",
                "  - Theo dõi huyết áp, đường huyết",
                "Nếu teo da:",
                "  - Ngừng thuốc, chờ hồi phục (có thể mất vài tháng)",
                "  - Dưỡng ẩm da",
                "Theo dõi: Dấu hiệu sinh tồn, chức năng thượng thận"
            ],
            "monitoring": "Theo dõi dấu hiệu sinh tồn, chức năng thượng thận (nếu có ức chế HPA) cho đến khi hồi phục."
        },
        "reversal_agents": None,
        "administration_instructions": {
            "oral": None,
            "topical": {
                "preparation": "Dạng cream, ointment, lotion 0.025%, 0.1%, 0.5%. Chọn dạng phù hợp với vị trí và loại tổn thương.",
                "application": "Bôi mỏng 2-4 lần/ngày lên vùng da bị ảnh hưởng. Massage nhẹ cho đến khi thấm. Rửa tay sau khi bôi.",
                "area": "Chỉ bôi lên vùng da bị ảnh thương. Tránh bôi lên vùng da lành, mặt, nách, bẹn.",
                "duration": "Tối đa 2-4 tuần liên tục. Nếu cần dùng kéo dài: giảm tần suất (q2-3 ngày) hoặc chuyển sang corticosteroid yếu hơn.",
                "notes": "QUAN TRỌNG: 1) Corticosteroid trung bình, phù hợp cho tổn thương trung bình, 2) KHÔNG dùng >2-4 tuần liên tục, 3) Tránh dùng trên mặt, nách, bẹn, 4) Tránh bôi lên vùng da bị loét, nhiễm trùng, 5) Bảo vệ khỏi ánh nắng mặt trời."
            }
        },
        "references": {
            "primary_sources": [
                "FDA Drug Label - Triamcinolone (Kenalog, Aristocort)",
                "UpToDate - Topical Corticosteroids: Drug Information",
                "Medscape - Triamcinolone Drug Reference",
                "Goodman & Gilman's The Pharmacological Basis of Therapeutics (14th ed)"
            ],
            "last_updated": "2025-02-18",
            "evidence_level": "A - Dựa trên FDA drug labels, clinical guidelines, và dữ liệu lâm sàng từ nhiều nguồn"
        }
    },
    
    "Azelaic acid topical": {
        "group": "Dermatology - Topical Antiacne/Anti-inflammatory",
        "vietnamese_name": "Azelaic Acid, Finacea, Azelex",
        "administration": ["Topical"],
        "indications": [
            "Mụn trứng cá (acne vulgaris) - viêm nhẹ đến trung bình",
            "Rosacea (papulopustular rosacea)",
            "Tăng sắc tố da (hyperpigmentation)",
            "Melasma"
        ],
        "contraindications": [
            "Dị ứng azelaic acid"
        ],
        "dosage": {
            "adult_acne_20%": "Bôi mỏng 2 lần/ngày lên vùng da bị ảnh hưởng (20% cream)",
            "adult_rosacea_15%": "Bôi mỏng 2 lần/ngày lên mặt (15% gel)",
            "notes": "Azelaic acid là thuốc kháng khuẩn và chống viêm, điều trị mụn trứng cá và rosacea. Dùng 2 lần/ngày. Có thể gây kích ứng da nhẹ trong vài tuần đầu."
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "Không đổi",
            "under_30": "Không đổi"
        },
        "side_effects": [
            "Kích ứng da (đỏ, rát, ngứa, khô) - phổ biến trong vài tuần đầu",
            "Bong tróc da",
            "Phản ứng dị ứng (phát ban, ngứa) - hiếm",
            "Nhạy cảm với ánh sáng (nhẹ) - hiếm"
        ],
        "interactions": [
            "Các sản phẩm làm khô da: tăng kích ứng da"
        ],
        "pregnancy": "B - An toàn",
        "mechanism_of_action": "Azelaic acid là dicarboxylic acid, có tác dụng: (1) Kháng khuẩn - ức chế Propionibacterium acnes và Staphylococcus epidermidis, (2) Chống viêm - ức chế sản xuất reactive oxygen species, (3) Tẩy tế bào chết - làm bong lớp sừng, giảm bít tắc nang lông, (4) Giảm tăng sắc tố - ức chế tyrosinase. Dẫn đến: giảm mụn trứng cá, giảm rosacea, giảm tăng sắc tố da. ĐẶC ĐIỂM: (1) Kháng khuẩn và chống viêm, (2) Dùng 2 lần/ngày, (3) Kích ứng da phổ biến trong vài tuần đầu, (4) An toàn trong thai kỳ (category B), (5) Phù hợp cho mụn trứng cá và rosacea.",
        "monitoring": [
            "Đáp ứng lâm sàng (giảm mụn, giảm rosacea) - cải thiện sau 4-8 tuần",
            "Dấu hiệu kích ứng da (đỏ, rát, ngứa, khô, bong tróc)",
            "Dấu hiệu phản ứng dị ứng (phát ban, ngứa)"
        ],
        "precautions": [
            "Kích ứng da phổ biến trong vài tuần đầu - thường giảm sau vài tuần",
            "Tránh dùng với các sản phẩm làm khô da cùng lúc",
            "Tránh bôi lên vùng da quanh mắt",
            "Bôi kem chống nắng (SPF ≥30) vào ban ngày nếu nhạy cảm với ánh sáng",
            "Dưỡng ẩm da nếu khô da"
        ],
        "pharmacokinetics": {
            "half_life": "Không áp dụng (topical)",
            "onset": "4-8 tuần",
            "duration": "Phụ thuộc tần suất dùng",
            "protein_binding": "Không áp dụng (topical)",
            "metabolism": "Chuyển hóa tại da",
            "clearance": "Thải trừ tại chỗ, hấp thu toàn thân tối thiểu"
        },
        "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm, tránh ánh sáng. Đóng nắp kín sau khi dùng.",
        "black_box_warnings": None,
        "drug_interactions": {
            "major": [],
            "moderate": [],
            "minor": []
        },
        "contraindications": {
            "tuyệt_đối": [
                "Dị ứng azelaic acid"
            ],
            "tương_đối": [
                "Da nhạy cảm - bắt đầu với tần suất thấp hơn (1 lần/ngày)"
            ]
        },
        "pregnancy_lactation": {
            "fda_category": "B",
            "pregnancy_details": "Azelaic acid là thuốc phân loại B. Không hấp thu toàn thân khi dùng tại chỗ. An toàn trong thai kỳ.",
            "lactation": {
                "safety": "Compatible",
                "details": "Azelaic acid không hấp thu toàn thân khi dùng tại chỗ, không bài tiết vào sữa mẹ. An toàn khi cho con bú.",
                "recommendation": "Có thể dùng khi cho con bú. An toàn, không có tác dụng phụ."
            }
        },
        "hepatic_adjustment": {
            "mild": "Không cần điều chỉnh liều",
            "moderate": "Không cần điều chỉnh liều",
            "severe": "Không cần điều chỉnh liều (topical, hấp thu tối thiểu)",
            "notes": "Azelaic acid không hấp thu toàn thân khi dùng tại chỗ. Không cần điều chỉnh liều ở bệnh nhân suy gan."
        },
        "overdose_management": {
            "symptoms": [
                "Kích ứng da nặng (đỏ, rát, khô, bong tróc)"
            ],
            "antidote": "Không có antidote đặc hiệu. Ngừng thuốc, điều trị hỗ trợ.",
            "treatment": [
                "Ngừng ngay azelaic acid",
                "Dưỡng ẩm da",
                "Corticosteroid tại chỗ yếu nếu kích ứng nặng",
                "Theo dõi: Dấu hiệu kích ứng da"
            ],
            "monitoring": "Theo dõi dấu hiệu kích ứng da cho đến khi hồi phục."
        },
        "reversal_agents": None,
        "administration_instructions": {
            "oral": None,
            "topical": {
                "preparation": "Dạng cream 20% (acne) hoặc gel 15% (rosacea).",
                "application": "Bôi mỏng 2 lần/ngày lên vùng da bị ảnh hưởng. Massage nhẹ cho đến khi thấm. Rửa tay sau khi bôi.",
                "area": "Chỉ bôi lên vùng da bị mụn hoặc rosacea. Tránh bôi lên vùng da quanh mắt.",
                "timing": "2 lần/ngày (sáng, tối).",
                "duration": "Điều trị thường 8-12 tuần. Có thể dùng kéo dài để duy trì.",
                "notes": "QUAN TRỌNG: 1) Dùng 2 lần/ngày, 2) Kích ứng da phổ biến trong vài tuần đầu, 3) Dưỡng ẩm da nếu khô da, 4) Bôi kem chống nắng (SPF ≥30) vào ban ngày nếu nhạy cảm với ánh sáng."
            }
        },
        "references": {
            "primary_sources": [
                "FDA Drug Label - Azelaic Acid (Finacea, Azelex)",
                "UpToDate - Azelaic Acid: Drug Information",
                "Medscape - Azelaic Acid Drug Reference",
                "AAD Guidelines - Acne Treatment, Rosacea Treatment"
            ],
            "last_updated": "2025-02-18",
            "evidence_level": "A - Dựa trên FDA drug labels, clinical guidelines, và dữ liệu lâm sàng từ nhiều nguồn"
        },
        "risk_flags": {
            "high_alert": False,
            "narrow_therapeutic_index": False,
            "bleeding_risk": False,
            "organ_toxicity": [],
            "qt_prolongation": False,
            "hepatotoxicity": False,
            "nephrotoxicity": False,
            "requires_monitoring": ["Clinical response (reduction in acne, rosacea)", "Signs of skin irritation (redness, dryness, peeling) - common in first few weeks", "Signs of allergic reaction"]
        },
        "guideline_tags": [
            "AAD Guidelines - Acne Treatment",
            "AAD Guidelines - Rosacea Treatment",
            "FDA Drug Information - Azelaic Acid",
            "UpToDate - Acne Treatment"
        ]
    },
    
    "Metronidazole topical": {
        "group": "Dermatology - Topical Antibiotic (Rosacea)",
        "vietnamese_name": "Metronidazole, Metrogel, Metrocream",
        "administration": ["Topical"],
        "indications": [
            "Rosacea (papulopustular rosacea)",
            "Rosacea đỏ mặt (erythematous rosacea)",
            "Viêm da quanh miệng (perioral dermatitis)"
        ],
        "contraindications": [
            "Dị ứng metronidazole hoặc nitroimidazole"
        ],
        "dosage": {
            "adult_rosacea_0.75%": "Bôi mỏng 2 lần/ngày lên mặt (0.75% gel/cream)",
            "adult_rosacea_1%": "Bôi mỏng 1 lần/ngày lên mặt (1% gel)",
            "notes": "Metronidazole là kháng sinh tại chỗ, điều trị rosacea. Dùng 1-2 lần/ngày tùy theo nồng độ. Điều trị thường 8-12 tuần. Có thể dùng kéo dài để duy trì."
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "Không đổi",
            "under_30": "Không đổi"
        },
        "side_effects": [
            "Kích ứng da tại chỗ (đỏ, rát, ngứa, khô) - phổ biến",
            "Bong tróc da",
            "Phản ứng dị ứng (phát ban, ngứa) - hiếm",
            "Nhạy cảm với ánh sáng (nhẹ) - hiếm"
        ],
        "interactions": [
            "Không có tương tác đáng kể với thuốc khác (topical)",
            "Metronidazole đường uống: không dùng cùng lúc (tăng nguy cơ tác dụng phụ)"
        ],
        "pregnancy": "B - An toàn",
        "mechanism_of_action": "Metronidazole là kháng sinh nitroimidazole tại chỗ. Tác dụng: (1) Kháng khuẩn - ức chế DNA synthesis của vi khuẩn (Propionibacterium acnes, Demodex mites), (2) Chống viêm - ức chế sản xuất reactive oxygen species, giảm viêm. Dẫn đến: giảm rosacea. ĐẶC ĐIỂM: (1) Kháng khuẩn và chống viêm, (2) Dùng 1-2 lần/ngày tùy theo nồng độ, (3) Điều trị thường 8-12 tuần, (4) Có thể dùng kéo dài để duy trì, (5) An toàn trong thai kỳ (category B), (6) Kích ứng da phổ biến.",
        "monitoring": [
            "Đáp ứng lâm sàng (giảm đỏ, giảm mụn rosacea) - cải thiện sau 4-8 tuần",
            "Dấu hiệu kích ứng da (đỏ, rát, ngứa, khô, bong tróc)",
            "Dấu hiệu phản ứng dị ứng (phát ban, ngứa)"
        ],
        "precautions": [
            "Kích ứng da phổ biến - thường giảm sau vài tuần",
            "Tránh bôi lên vùng da quanh mắt",
            "Bôi kem chống nắng (SPF ≥30) vào ban ngày nếu nhạy cảm với ánh sáng",
            "Dưỡng ẩm da nếu khô da",
            "Không dùng với metronidazole đường uống cùng lúc",
            "Tránh uống rượu (nếu dùng metronidazole đường uống)"
        ],
        "pharmacokinetics": {
            "half_life": "Không áp dụng (topical)",
            "onset": "4-8 tuần",
            "duration": "Phụ thuộc tần suất dùng",
            "protein_binding": "Không áp dụng (topical)",
            "metabolism": "Chuyển hóa tại da",
            "clearance": "Thải trừ tại chỗ, hấp thu toàn thân tối thiểu"
        },
        "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm, tránh ánh sáng. Đóng nắp kín sau khi dùng.",
        "black_box_warnings": None,
        "drug_interactions": {
            "major": [],
            "moderate": [
                {
                    "drug": "Metronidazole đường uống",
                    "mechanism": "Cả hai đều là metronidazole, tác dụng cộng dồn",
                    "effect": "Tăng nguy cơ tác dụng phụ toàn thân",
                    "management": "Không dùng cùng lúc. Chọn một trong hai."
                }
            ],
            "minor": []
        },
        "contraindications": {
            "tuyệt_đối": [
                "Dị ứng metronidazole hoặc nitroimidazole"
            ],
            "tương_đối": [
                "Da nhạy cảm - bắt đầu với tần suất thấp hơn (1 lần/ngày)",
                "Đang dùng metronidazole đường uống - không dùng cùng lúc"
            ]
        },
        "pregnancy_lactation": {
            "fda_category": "B",
            "pregnancy_details": "Metronidazole là thuốc phân loại B. Không hấp thu toàn thân khi dùng tại chỗ. An toàn trong thai kỳ.",
            "lactation": {
                "safety": "Compatible",
                "details": "Metronidazole không hấp thu toàn thân khi dùng tại chỗ, không bài tiết vào sữa mẹ. An toàn khi cho con bú.",
                "recommendation": "Có thể dùng khi cho con bú. An toàn, không có tác dụng phụ."
            }
        },
        "hepatic_adjustment": {
            "mild": "Không cần điều chỉnh liều",
            "moderate": "Không cần điều chỉnh liều",
            "severe": "Không cần điều chỉnh liều (topical, hấp thu tối thiểu)",
            "notes": "Metronidazole không hấp thu toàn thân khi dùng tại chỗ. Không cần điều chỉnh liều ở bệnh nhân suy gan."
        },
        "overdose_management": {
            "symptoms": [
                "Kích ứng da nặng (đỏ, rát, khô, bong tróc)"
            ],
            "antidote": "Không có antidote đặc hiệu. Ngừng thuốc, điều trị hỗ trợ.",
            "treatment": [
                "Ngừng ngay metronidazole",
                "Dưỡng ẩm da",
                "Corticosteroid tại chỗ yếu nếu kích ứng nặng",
                "Theo dõi: Dấu hiệu kích ứng da"
            ],
            "monitoring": "Theo dõi dấu hiệu kích ứng da cho đến khi hồi phục."
        },
        "reversal_agents": None,
        "administration_instructions": {
            "oral": None,
            "topical": {
                "preparation": "Dạng gel hoặc cream 0.75% hoặc gel 1%.",
                "application": "Bôi mỏng 1-2 lần/ngày tùy theo nồng độ lên mặt. Massage nhẹ cho đến khi thấm. Rửa tay sau khi bôi.",
                "area": "Chỉ bôi lên vùng da bị rosacea. Tránh bôi lên vùng da quanh mắt.",
                "timing": "1-2 lần/ngày tùy theo nồng độ (0.75%: 2 lần/ngày, 1%: 1 lần/ngày).",
                "duration": "Điều trị thường 8-12 tuần. Có thể dùng kéo dài để duy trì.",
                "notes": "QUAN TRỌNG: 1) Dùng 1-2 lần/ngày tùy theo nồng độ, 2) Kích ứng da phổ biến, 3) Dưỡng ẩm da nếu khô da, 4) Bôi kem chống nắng (SPF ≥30) vào ban ngày nếu nhạy cảm với ánh sáng, 5) Không dùng với metronidazole đường uống cùng lúc."
            }
        },
        "references": {
            "primary_sources": [
                "FDA Drug Label - Metronidazole (Metrogel, Metrocream)",
                "UpToDate - Metronidazole: Drug Information",
                "Medscape - Metronidazole Drug Reference",
                "AAD Guidelines - Rosacea Treatment"
            ],
            "last_updated": "2025-02-18",
            "evidence_level": "A - Dựa trên FDA drug labels, clinical guidelines, và dữ liệu lâm sàng từ nhiều nguồn"
        }
    },
    
    "Terbinafine topical": {
        "group": "Dermatology - Topical Antifungal",
        "vietnamese_name": "Terbinafine, Lamisil",
        "administration": ["Topical"],
        "indications": [
            "Nấm da (tinea corporis, tinea cruris, tinea pedis)",
            "Nấm móng (onychomycosis) - dạng uống hiệu quả hơn",
            "Nhiễm nấm da do dermatophytes"
        ],
        "contraindications": [
            "Dị ứng terbinafine",
            "Nhiễm trùng da do vi khuẩn (không dùng trừ khi có kháng sinh)"
        ],
        "dosage": {
            "adult_topical_cream": "Bôi mỏng 1-2 lần/ngày lên vùng da bị ảnh hưởng và vùng da xung quanh 2cm",
            "adult_topical_spray": "Xịt 1-2 lần/ngày lên vùng da bị ảnh hưởng",
            "adult_duration": "1-4 tuần tùy theo loại nấm (tinea pedis: 4 tuần)",
            "notes": "Terbinafine là allylamine antifungal, hiệu quả cao với dermatophytes. Dùng 1-2 lần/ngày trong 1-4 tuần. Rửa tay sau khi bôi."
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "Không đổi",
            "under_30": "Không đổi"
        },
        "side_effects": [
            "Kích ứng da nhẹ (đỏ, ngứa, bỏng rát) - phổ biến",
            "Khô da",
            "Phát ban",
            "Dị ứng da (hiếm)"
        ],
        "interactions": [
            "Không có tương tác đáng kể với thuốc khác (topical)"
        ],
        "pregnancy": "B - An toàn khi dùng tại chỗ",
        "mechanism_of_action": "Terbinafine là allylamine antifungal, ức chế enzyme squalene epoxidase trong quá trình tổng hợp ergosterol (thành phần màng tế bào nấm). Ức chế squalene epoxidase → tích tụ squalene (độc cho nấm) và giảm ergosterol → màng tế bào nấm bị tổn thương → chết tế bào nấm. Terbinafine có ái lực cao với enzyme của nấm, ít ảnh hưởng đến enzyme của người. Hiệu quả cao với dermatophytes (Trichophyton, Microsporum, Epidermophyton). ĐẶC ĐIỂM: (1) Allylamine antifungal, (2) Hiệu quả cao với dermatophytes, (3) Dùng 1-2 lần/ngày trong 1-4 tuần, (4) Ít tác dụng phụ, (5) An toàn khi dùng tại chỗ.",
        "monitoring": [
            "Đáp ứng lâm sàng (giảm đỏ, ngứa, vảy da)",
            "Dấu hiệu kích ứng da (đỏ, ngứa, bỏng rát tăng)",
            "Dấu hiệu nhiễm trùng da (mủ, đỏ, sưng tăng)"
        ],
        "precautions": [
            "Bôi mỏng lên vùng da bị ảnh hưởng và vùng da xung quanh 2cm",
            "Rửa tay sau khi bôi (tránh lây lan)",
            "Dùng đều đặn 1-2 lần/ngày trong 1-4 tuần",
            "Không dùng trên vùng da bị loét, nhiễm trùng",
            "Nếu không đáp ứng sau 2-4 tuần → cần đánh giá lại chẩn đoán",
            "Trẻ em: thận trọng, giảm liều nếu cần"
        ],
        "pharmacokinetics": {
            "half_life": "Không áp dụng (topical)",
            "onset": "Vài ngày",
            "duration": "Phụ thuộc tần suất dùng",
            "protein_binding": "Không áp dụng (topical)",
            "metabolism": "Chuyển hóa tại da (nếu hấp thu toàn thân: gan)",
            "clearance": "Thải trừ qua nước tiểu (nếu hấp thu toàn thân)"
        },
        "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm, tránh ánh sáng. Đóng nắp kín sau khi dùng.",
        "black_box_warnings": None,
        "drug_interactions": {
            "major": [],
            "moderate": [],
            "minor": []
        },
        "contraindications": {
            "tuyệt_đối": [
                "Dị ứng terbinafine",
                "Nhiễm trùng da do vi khuẩn (không dùng trừ khi có kháng sinh)"
            ],
            "tương_đối": [
                "Trẻ em - thận trọng, giảm liều nếu cần",
                "Vùng da bị loét - tránh dùng"
            ]
        },
        "pregnancy_lactation": {
            "fda_category": "B",
            "pregnancy_details": "Terbinafine là thuốc phân loại B. Terbinafine tại chỗ hấp thu toàn thân tối thiểu. An toàn khi dùng tại chỗ trong thai kỳ.",
            "lactation": {
                "safety": "Compatible",
                "details": "Terbinafine tại chỗ hấp thu toàn thân tối thiểu, không bài tiết vào sữa mẹ. An toàn khi cho con bú.",
                "recommendation": "Có thể dùng khi cho con bú."
            }
        },
        "hepatic_adjustment": {
            "mild": "Không cần điều chỉnh liều",
            "moderate": "Không cần điều chỉnh liều",
            "severe": "Không cần điều chỉnh liều",
            "notes": "Terbinafine tại chỗ hấp thu toàn thân tối thiểu. Không cần điều chỉnh liều ở bệnh nhân suy gan."
        },
        "overdose_management": {
            "symptoms": [
                "Kích ứng da nặng (đỏ, ngứa, bỏng rát)",
                "Phát ban",
                "Dị ứng da"
            ],
            "antidote": "Không có antidote đặc hiệu",
            "treatment": [
                "Ngừng terbinafine ngay lập tức",
                "Rửa sạch vùng da đã bôi",
                "Điều trị triệu chứng (kem dưỡng ẩm, corticosteroid tại chỗ nếu cần)"
            ],
            "monitoring": "Theo dõi dấu hiệu kích ứng da và dị ứng."
        },
        "reversal_agents": {
            "available": False,
            "agents": []
        },
        "administration_instructions": {
            "oral": None,
            "iv": None,
            "topical": {
                "preparation": "Dạng cream 1% hoặc spray 1%.",
                "application": "Bôi mỏng 1-2 lần/ngày lên vùng da bị ảnh hưởng và vùng da xung quanh 2cm. Massage nhẹ cho đến khi thấm. Rửa tay sau khi bôi.",
                "area": "Bôi lên vùng da bị nấm và vùng da xung quanh 2cm. Tránh bôi lên vùng da bị loét, nhiễm trùng.",
                "timing": "1-2 lần/ngày (thường 2 lần/ngày cho tinea pedis, 1 lần/ngày cho tinea corporis/cruris).",
                "duration": "1-4 tuần tùy theo loại nấm (tinea pedis: 4 tuần, tinea corporis/cruris: 1-2 tuần).",
                "notes": "QUAN TRỌNG: 1) Dùng 1-2 lần/ngày, 2) Bôi lên vùng da bị ảnh hưởng và vùng da xung quanh 2cm, 3) Rửa tay sau khi bôi, 4) Dùng đều đặn trong 1-4 tuần, 5) Nếu không đáp ứng sau 2-4 tuần → cần đánh giá lại chẩn đoán."
            }
        },
        "references": {
            "primary_sources": [
                "FDA Drug Label - Terbinafine (Lamisil)",
                "UpToDate - Terbinafine: Drug Information",
                "Medscape - Terbinafine Drug Reference",
                "AAD Guidelines - Fungal Skin Infections"
            ],
            "last_updated": "2025-02-05",
            "evidence_level": "A - Dựa trên FDA drug labels, clinical guidelines, và dữ liệu lâm sàng"
        }
    },
    
    "Permethrin topical": {
        "group": "Dermatology - Topical Antiparasitic",
        "vietnamese_name": "Permethrin, Elimite, Nix",
        "administration": ["Topical"],
        "indications": [
            "Ghẻ (scabies)",
            "Chấy (head lice, pubic lice)",
            "Nhiễm ký sinh trùng da (Sarcoptes scabiei, Pediculus humanus)"
        ],
        "contraindications": [
            "Dị ứng permethrin hoặc pyrethroid",
            "Trẻ sơ sinh <2 tháng tuổi (thận trọng)"
        ],
        "dosage": {
            "adult_scabies": "Bôi từ cổ xuống toàn bộ cơ thể (kể cả lòng bàn tay, bàn chân), để 8-14 giờ, sau đó tắm rửa sạch. Lặp lại sau 1 tuần nếu cần.",
            "adult_lice": "Bôi lên tóc và da đầu (nếu chấy đầu) hoặc vùng lông mu (nếu chấy mu), để 10 phút, sau đó gội đầu. Lặp lại sau 7-10 ngày nếu cần.",
            "pediatric_scabies_2mo_2yr": "Bôi từ cổ xuống toàn bộ cơ thể, để 6-8 giờ, sau đó tắm rửa sạch. Lặp lại sau 1 tuần nếu cần.",
            "pediatric_scabies_2yr_plus": "Bôi từ cổ xuống toàn bộ cơ thể, để 8-14 giờ, sau đó tắm rửa sạch. Lặp lại sau 1 tuần nếu cần.",
            "notes": "Permethrin là pyrethroid, ức chế kênh Na+ của ký sinh trùng. Dùng 1 lần, lặp lại sau 1 tuần (ghẻ) hoặc 7-10 ngày (chấy) nếu cần. Điều trị tất cả người tiếp xúc cùng lúc."
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "Không đổi",
            "under_30": "Không đổi"
        },
        "side_effects": [
            "Kích ứng da nhẹ (đỏ, ngứa, bỏng rát) - phổ biến",
            "Ngứa tiếp tục sau điều trị (do phản ứng dị ứng với xác ký sinh trùng) - phổ biến",
            "Phát ban",
            "Dị ứng da (hiếm)",
            "Tê, ngứa ran (hiếm, nếu hấp thu toàn thân)"
        ],
        "interactions": [
            "Không có tương tác đáng kể với thuốc khác (topical)"
        ],
        "pregnancy": "B - An toàn khi dùng tại chỗ",
        "mechanism_of_action": "Permethrin là pyrethroid (synthetic pyrethrin), ức chế kênh Na+ của ký sinh trùng, gây tăng kích thích thần kinh, co giật, và chết. Permethrin có ái lực cao với kênh Na+ của ký sinh trùng (Sarcoptes scabiei, Pediculus humanus), ít ảnh hưởng đến kênh Na+ của người. Permethrin cũng có tác dụng độc với ty thể của ký sinh trùng. ĐẶC ĐIỂM: (1) Pyrethroid antiparasitic, (2) Hiệu quả cao với ghẻ và chấy, (3) Dùng 1 lần, lặp lại sau 1 tuần nếu cần, (4) An toàn khi dùng tại chỗ, (5) Điều trị tất cả người tiếp xúc cùng lúc.",
        "monitoring": [
            "Đáp ứng lâm sàng (giảm ngứa, giảm tổn thương da)",
            "Dấu hiệu kích ứng da (đỏ, ngứa, bỏng rát tăng)",
            "Dấu hiệu nhiễm trùng da thứ phát (mủ, đỏ, sưng tăng)",
            "Ngứa tiếp tục (có thể do phản ứng dị ứng với xác ký sinh trùng, không phải do thuốc)"
        ],
        "precautions": [
            "Điều trị tất cả người tiếp xúc cùng lúc (tránh tái nhiễm)",
            "Bôi từ cổ xuống toàn bộ cơ thể (kể cả lòng bàn tay, bàn chân) cho ghẻ",
            "Để 8-14 giờ (người lớn) hoặc 6-8 giờ (trẻ 2 tháng-2 tuổi) cho ghẻ",
            "Tắm rửa sạch sau khi để đủ thời gian",
            "Giặt quần áo, ga gối, khăn tắm ở nhiệt độ cao (60°C) hoặc cách ly 3-7 ngày",
            "Lặp lại sau 1 tuần (ghẻ) hoặc 7-10 ngày (chấy) nếu cần",
            "Ngứa có thể tiếp tục 2-4 tuần sau điều trị (do phản ứng dị ứng với xác ký sinh trùng, không phải do thuốc)",
            "Trẻ sơ sinh <2 tháng tuổi: thận trọng, giảm thời gian để (6 giờ)"
        ],
        "pharmacokinetics": {
            "half_life": "Không áp dụng (topical)",
            "onset": "Ngay lập tức sau khi bôi",
            "duration": "8-14 giờ (thời gian để trên da)",
            "protein_binding": "Không áp dụng (topical)",
            "metabolism": "Chuyển hóa tại da (nếu hấp thu toàn thân: gan, esterase)",
            "clearance": "Thải trừ qua nước tiểu (nếu hấp thu toàn thân)"
        },
        "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm, tránh ánh sáng. Đóng nắp kín sau khi dùng.",
        "black_box_warnings": None,
        "drug_interactions": {
            "major": [],
            "moderate": [],
            "minor": []
        },
        "contraindications": {
            "tuyệt_đối": [
                "Dị ứng permethrin hoặc pyrethroid"
            ],
            "tương_đối": [
                "Trẻ sơ sinh <2 tháng tuổi - thận trọng, giảm thời gian để (6 giờ)",
                "Phụ nữ có thai - thận trọng, chỉ dùng khi cần thiết"
            ]
        },
        "pregnancy_lactation": {
            "fda_category": "B",
            "pregnancy_details": "Permethrin là thuốc phân loại B. Permethrin tại chỗ hấp thu toàn thân tối thiểu. An toàn khi dùng tại chỗ trong thai kỳ.",
            "lactation": {
                "safety": "Compatible",
                "details": "Permethrin tại chỗ hấp thu toàn thân tối thiểu, không bài tiết vào sữa mẹ. An toàn khi cho con bú.",
                "recommendation": "Có thể dùng khi cho con bú."
            }
        },
        "hepatic_adjustment": {
            "mild": "Không cần điều chỉnh liều",
            "moderate": "Không cần điều chỉnh liều",
            "severe": "Không cần điều chỉnh liều",
            "notes": "Permethrin tại chỗ hấp thu toàn thân tối thiểu. Không cần điều chỉnh liều ở bệnh nhân suy gan."
        },
        "overdose_management": {
            "symptoms": [
                "Kích ứng da nặng (đỏ, ngứa, bỏng rát)",
                "Phát ban",
                "Dị ứng da",
                "Tê, ngứa ran (nếu hấp thu toàn thân)",
                "Co giật (nếu hấp thu toàn thân rất nhiều)"
            ],
            "antidote": "Không có antidote đặc hiệu",
            "treatment": [
                "Ngừng permethrin ngay lập tức",
                "Rửa sạch vùng da đã bôi",
                "Điều trị triệu chứng (kem dưỡng ẩm, corticosteroid tại chỗ nếu cần)",
                "Nếu hấp thu toàn thân: hỗ trợ hô hấp, điều trị co giật"
            ],
            "monitoring": "Theo dõi dấu hiệu kích ứng da, dị ứng, và triệu chứng thần kinh nếu hấp thu toàn thân."
        },
        "reversal_agents": {
            "available": False,
            "agents": []
        },
        "administration_instructions": {
            "oral": None,
            "iv": None,
            "topical": {
                "preparation": "Dạng cream 5% (ghẻ) hoặc lotion 1% (chấy).",
                "application": "GHẺ: Bôi từ cổ xuống toàn bộ cơ thể (kể cả lòng bàn tay, bàn chân), để 8-14 giờ (người lớn) hoặc 6-8 giờ (trẻ 2 tháng-2 tuổi), sau đó tắm rửa sạch. CHẤY: Bôi lên tóc và da đầu (nếu chấy đầu) hoặc vùng lông mu (nếu chấy mu), để 10 phút, sau đó gội đầu.",
                "area": "GHẺ: Toàn bộ cơ thể từ cổ xuống (kể cả lòng bàn tay, bàn chân). CHẤY: Tóc và da đầu (chấy đầu) hoặc vùng lông mu (chấy mu).",
                "timing": "GHẺ: 1 lần, lặp lại sau 1 tuần nếu cần. CHẤY: 1 lần, lặp lại sau 7-10 ngày nếu cần.",
                "duration": "GHẺ: Để 8-14 giờ (người lớn) hoặc 6-8 giờ (trẻ 2 tháng-2 tuổi). CHẤY: Để 10 phút.",
                "notes": "QUAN TRỌNG: 1) Điều trị tất cả người tiếp xúc cùng lúc, 2) Giặt quần áo, ga gối, khăn tắm ở nhiệt độ cao (60°C) hoặc cách ly 3-7 ngày, 3) Ngứa có thể tiếp tục 2-4 tuần sau điều trị (do phản ứng dị ứng với xác ký sinh trùng), 4) Lặp lại sau 1 tuần (ghẻ) hoặc 7-10 ngày (chấy) nếu cần."
            }
        },
        "references": {
            "primary_sources": [
                "FDA Drug Label - Permethrin (Elimite, Nix)",
                "UpToDate - Permethrin: Drug Information",
                "Medscape - Permethrin Drug Reference",
                "CDC Guidelines - Scabies and Lice Treatment"
            ],
            "last_updated": "2025-02-05",
            "evidence_level": "A - Dựa trên FDA drug labels, CDC guidelines, và dữ liệu lâm sàng"
        }
    },
    
    "Clindamycin topical": {
        "group": "Dermatology - Topical Antibiotic",
        "vietnamese_name": "Clindamycin topical, Cleocin T",
        "administration": ["Topical"],
        "indications": [
            "Mụn trứng cá (acne vulgaris)",
            "Nhiễm khuẩn da",
            "Viêm nang lông do vi khuẩn"
        ],
        "contraindications": [
            "Dị ứng clindamycin hoặc lincomycin",
            "Viêm đại tràng (tiền sử viêm đại tràng do kháng sinh)",
            "Nhiễm khuẩn nặng (cần kháng sinh toàn thân)"
        ],
        "dosage": {
            "adult_topical": "Bôi mỏng 2 lần/ngày lên vùng da bị ảnh hưởng",
            "pediatric": "Bôi mỏng 2 lần/ngày (từ 12 tuổi trở lên)",
            "notes": "Dùng cho mụn trứng cá. Bôi lên vùng da sạch, khô. Tránh mắt, miệng, niêm mạc."
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "Không đổi",
            "under_30": "Không đổi"
        },
        "side_effects": [
            "Kích ứng da tại chỗ (đỏ, rát, khô) - phổ biến",
            "Bong tróc da",
            "Ngứa",
            "Viêm đại tràng (hiếm, nếu hấp thu toàn thân)",
            "Nhiễm C. difficile (hiếm, nếu hấp thu toàn thân)"
        ],
        "interactions": [
            "Erythromycin tại chỗ: đối kháng, tránh dùng cùng",
            "Benzoyl peroxide: có thể dùng kết hợp (tăng hiệu quả)"
        ],
        "pregnancy": "B",
        "mechanism_of_action": "Clindamycin là lincosamide antibiotic, ức chế tổng hợp protein vi khuẩn bằng cách gắn với 50S ribosomal subunit. Tác dụng với Propionibacterium acnes (vi khuẩn gây mụn trứng cá) và các vi khuẩn Gram-dương khác. Dạng tại chỗ hấp thu toàn thân tối thiểu, giảm nguy cơ tác dụng phụ toàn thân. Được dùng cho mụn trứng cá, đặc biệt mụn viêm.",
        "monitoring": [
            "Đáp ứng điều trị (giảm mụn trứng cá)",
            "Kích ứng da tại chỗ (đỏ, rát, khô)",
            "Dấu hiệu viêm đại tràng (tiêu chảy, đau bụng) - hiếm",
            "Dấu hiệu nhiễm C. difficile - hiếm"
        ],
        "precautions": [
            "Kích ứng da tại chỗ - phổ biến, thường tự khỏi sau vài ngày",
            "Tránh mắt, miệng, niêm mạc",
            "Bôi lên vùng da sạch, khô",
            "Có thể dùng kết hợp với benzoyl peroxide (tăng hiệu quả)",
            "Tránh dùng với erythromycin tại chỗ (đối kháng)",
            "Nguy cơ viêm đại tràng nếu hấp thu toàn thân (hiếm)"
        ],
        "pharmacokinetics": {
            "half_life": "Không áp dụng (topical)",
            "onset": "Vài ngày đến vài tuần",
            "duration": "12 giờ (dùng 2 lần/ngày)",
            "protein_binding": "Không áp dụng (topical)",
            "clearance": "Hấp thu toàn thân tối thiểu. Nếu hấp thu: gan (chuyển hóa), thận (thải trừ)."
        },
        "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm, tránh ánh sáng",
        "black_box_warnings": "Nguy cơ viêm đại tràng do C. difficile nếu hấp thu toàn thân (hiếm với dạng tại chỗ).",
        "drug_interactions": {
            "major": [
                {
                    "drug": "Erythromycin tại chỗ",
                    "mechanism": "Đối kháng tác dụng",
                    "effect": "Giảm hiệu quả cả hai",
                    "management": "Tránh dùng cùng."
                }
            ],
            "moderate": [],
            "minor": []
        },
        "contraindications": {
            "tuyệt_đối": [
                "Dị ứng clindamycin hoặc lincomycin",
                "Viêm đại tràng (tiền sử viêm đại tràng do kháng sinh)"
            ],
            "tương_đối": [
                "Nhiễm khuẩn nặng - cần kháng sinh toàn thân",
                "Trẻ em <12 tuổi - thận trọng"
            ]
        },
        "pregnancy_lactation": {
            "fda_category": "B",
            "pregnancy_details": "Category B - an toàn hơn category C. Hấp thu toàn thân tối thiểu từ dạng tại chỗ.",
            "lactation": {
                "safety": "Compatible",
                "details": "Hấp thu toàn thân tối thiểu từ dạng tại chỗ. Bài tiết vào sữa mẹ ở nồng độ rất thấp.",
                "recommendation": "Có thể dùng an toàn khi cho con bú."
            }
        },
        "hepatic_adjustment": {
            "mild": "Không đổi",
            "moderate": "Không đổi",
            "severe": "Không đổi",
            "notes": "Hấp thu toàn thân tối thiểu từ dạng tại chỗ. Không cần điều chỉnh liều ở suy gan."
        },
        "overdose_management": {
            "symptoms": [
                "Kích ứng da nặng",
                "Viêm đại tràng (nếu hấp thu toàn thân)",
                "Tiêu chảy (nếu hấp thu toàn thân)"
            ],
            "antidote": "Không có antidote đặc hiệu",
            "treatment": [
                "Ngừng ngay clindamycin tại chỗ",
                "Rửa sạch vùng da",
                "Hỗ trợ và điều trị triệu chứng",
                "Nếu có dấu hiệu viêm đại tràng: điều trị theo protocol"
            ],
            "monitoring": "Theo dõi kích ứng da, dấu hiệu viêm đại tràng"
        },
        "reversal_agents": {
            "available": False,
            "agents": []
        },
        "administration_instructions": {
            "topical": {
                "technique": "Bôi mỏng 2 lần/ngày lên vùng da sạch, khô. Tránh mắt, miệng, niêm mạc.",
                "timing": "Dùng 2 lần/ngày, đều đặn. Có thể dùng kết hợp với benzoyl peroxide.",
                "notes": "Dùng cho mụn trứng cá. Bôi lên vùng da sạch, khô trước khi đi ngủ và buổi sáng."
            }
        },
        "references": {
            "primary_sources": [
                "FDA Drug Label - Cleocin T (clindamycin topical)",
                "UpToDate - Topical antibiotics for acne"
            ],
            "last_updated": "2025-02-05",
            "evidence_level": "A"
        }
    },
    
    "Fusidic Acid": {
        "group": "Dermatology - Topical Antibiotic",
        "vietnamese_name": "Fusidic acid, Fucidin",
        "administration": ["Topical"],
        "indications": [
            "Nhiễm khuẩn da do Staphylococcus (bao gồm MRSA)",
            "Viêm nang lông do vi khuẩn",
            "Chốc lở (impetigo)",
            "Nhiễm khuẩn vết thương"
        ],
        "contraindications": [
            "Dị ứng fusidic acid",
            "Nhiễm khuẩn nặng (cần kháng sinh toàn thân)"
        ],
        "dosage": {
            "adult_topical": "Bôi mỏng 3 lần/ngày lên vùng da bị ảnh hưởng",
            "pediatric": "Bôi mỏng 3 lần/ngày (từ 1 tuổi trở lên)",
            "notes": "Hiệu quả với Staphylococcus, bao gồm MRSA. Bôi lên vùng da sạch, khô."
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "Không đổi",
            "under_30": "Không đổi"
        },
        "side_effects": [
            "Kích ứng da tại chỗ (đỏ, rát) - hiếm",
            "Ngứa",
            "Kháng thuốc (nếu dùng kéo dài)"
        ],
        "interactions": [
            "Ít tương tác thuốc"
        ],
        "pregnancy": "B",
        "mechanism_of_action": "Fusidic acid là antibiotic, ức chế tổng hợp protein vi khuẩn bằng cách gắn với elongation factor G (EF-G) trên ribosome. Tác dụng chủ yếu với Staphylococcus (bao gồm MRSA) và một số vi khuẩn Gram-dương khác. Đặc điểm: hiệu quả với MRSA, ít kháng thuốc, hấp thu toàn thân tối thiểu từ dạng tại chỗ.",
        "monitoring": [
            "Đáp ứng điều trị (giảm nhiễm khuẩn)",
            "Kích ứng da tại chỗ",
            "Dấu hiệu kháng thuốc (nếu dùng kéo dài)"
        ],
        "precautions": [
            "Kích ứng da tại chỗ - hiếm",
            "Nguy cơ kháng thuốc nếu dùng kéo dài - dùng đủ thời gian, không dùng quá lâu",
            "Bôi lên vùng da sạch, khô",
            "Hiệu quả với MRSA - ưu điểm"
        ],
        "pharmacokinetics": {
            "half_life": "Không áp dụng (topical)",
            "onset": "Vài ngày",
            "duration": "8 giờ (dùng 3 lần/ngày)",
            "protein_binding": "Không áp dụng (topical)",
            "clearance": "Hấp thu toàn thân tối thiểu từ dạng tại chỗ."
        },
        "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm, tránh ánh sáng",
        "black_box_warnings": None,
        "drug_interactions": {
            "major": [],
            "moderate": [],
            "minor": []
        },
        "contraindications": {
            "tuyệt_đối": [
                "Dị ứng fusidic acid"
            ],
            "tương_đối": [
                "Nhiễm khuẩn nặng - cần kháng sinh toàn thân",
                "Trẻ em <1 tuổi - thận trọng"
            ]
        },
        "pregnancy_lactation": {
            "fda_category": "B",
            "pregnancy_details": "Category B - an toàn hơn category C. Hấp thu toàn thân tối thiểu từ dạng tại chỗ.",
            "lactation": {
                "safety": "Compatible",
                "details": "Hấp thu toàn thân tối thiểu từ dạng tại chỗ.",
                "recommendation": "Có thể dùng an toàn khi cho con bú."
            }
        },
        "hepatic_adjustment": {
            "mild": "Không đổi",
            "moderate": "Không đổi",
            "severe": "Không đổi",
            "notes": "Hấp thu toàn thân tối thiểu từ dạng tại chỗ. Không cần điều chỉnh liều ở suy gan."
        },
        "overdose_management": {
            "symptoms": [
                "Kích ứng da nặng"
            ],
            "antidote": "Không có antidote đặc hiệu",
            "treatment": [
                "Ngừng ngay fusidic acid",
                "Rửa sạch vùng da",
                "Hỗ trợ và điều trị triệu chứng"
            ],
            "monitoring": "Theo dõi kích ứng da"
        },
        "reversal_agents": {
            "available": False,
            "agents": []
        },
        "administration_instructions": {
            "topical": {
                "technique": "Bôi mỏng 3 lần/ngày lên vùng da sạch, khô.",
                "timing": "Dùng 3 lần/ngày, đều đặn. Dùng đủ thời gian, không dùng quá lâu.",
                "notes": "Hiệu quả với Staphylococcus, bao gồm MRSA."
            }
        },
        "references": {
            "primary_sources": [
                "FDA Drug Label - Fucidin (fusidic acid)",
                "UpToDate - Topical antibiotics for skin infections"
            ],
            "last_updated": "2025-02-05",
            "evidence_level": "A"
        }
    },
    
    "Metronidazole topical": {
        "group": "Dermatology - Topical Antibiotic/Antiparasitic",
        "vietnamese_name": "Metronidazole topical, Metrogel, Metrocream",
        "administration": ["Topical"],
        "indications": [
            "Rosacea (đỏ mặt, mụn mủ)",
            "Viêm da quanh miệng (perioral dermatitis)",
            "Nhiễm khuẩn da do kỵ khí"
        ],
        "contraindications": [
            "Dị ứng metronidazole",
            "Nhiễm khuẩn nặng (cần kháng sinh toàn thân)"
        ],
        "dosage": {
            "adult_topical": "Bôi mỏng 1-2 lần/ngày lên vùng da bị ảnh hưởng",
            "notes": "Dùng cho rosacea. Bôi lên vùng da sạch, khô. Tránh mắt, miệng."
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "Không đổi",
            "under_30": "Không đổi"
        },
        "side_effects": [
            "Kích ứng da tại chỗ (đỏ, rát, khô) - phổ biến",
            "Bong tróc da",
            "Ngứa",
            "Khô da"
        ],
        "interactions": [
            "Rượu: có thể gây phản ứng disulfiram-like (hiếm với dạng tại chỗ)",
            "Warfarin: có thể tăng INR (hiếm với dạng tại chỗ)"
        ],
        "pregnancy": "B",
        "mechanism_of_action": "Metronidazole là nitroimidazole antibiotic/antiparasitic. Ức chế DNA synthesis của vi khuẩn kỵ khí và ký sinh trùng. Tác dụng với Demodex mites (có thể liên quan đến rosacea) và vi khuẩn kỵ khí. Dạng tại chỗ hấp thu toàn thân tối thiểu, giảm nguy cơ tác dụng phụ toàn thân. Được dùng chủ yếu cho rosacea (đỏ mặt, mụn mủ).",
        "monitoring": [
            "Đáp ứng điều trị (giảm rosacea)",
            "Kích ứng da tại chỗ (đỏ, rát, khô)",
            "Dấu hiệu nhiễm khuẩn (nếu có)"
        ],
        "precautions": [
            "Kích ứng da tại chỗ - phổ biến, thường tự khỏi sau vài ngày",
            "Tránh mắt, miệng",
            "Bôi lên vùng da sạch, khô",
            "Tránh rượu (có thể gây phản ứng disulfiram-like, hiếm với dạng tại chỗ)",
            "Dùng đều đặn hàng ngày"
        ],
        "pharmacokinetics": {
            "half_life": "Không áp dụng (topical)",
            "onset": "Vài ngày đến vài tuần",
            "duration": "12-24 giờ (dùng 1-2 lần/ngày)",
            "protein_binding": "Không áp dụng (topical)",
            "clearance": "Hấp thu toàn thân tối thiểu từ dạng tại chỗ."
        },
        "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm, tránh ánh sáng",
        "black_box_warnings": None,
        "drug_interactions": {
            "major": [],
            "moderate": [
                {
                    "drug": "Rượu",
                    "mechanism": "Có thể gây phản ứng disulfiram-like",
                    "effect": "Buồn nôn, nôn, đỏ mặt (hiếm với dạng tại chỗ)",
                    "management": "Tránh rượu (hiếm với dạng tại chỗ)."
                }
            ],
            "minor": []
        },
        "contraindications": {
            "tuyệt_đối": [
                "Dị ứng metronidazole"
            ],
            "tương_đối": [
                "Nhiễm khuẩn nặng - cần kháng sinh toàn thân"
            ]
        },
        "pregnancy_lactation": {
            "fda_category": "B",
            "pregnancy_details": "Category B - an toàn hơn category C. Hấp thu toàn thân tối thiểu từ dạng tại chỗ.",
            "lactation": {
                "safety": "Compatible",
                "details": "Hấp thu toàn thân tối thiểu từ dạng tại chỗ.",
                "recommendation": "Có thể dùng an toàn khi cho con bú."
            }
        },
        "hepatic_adjustment": {
            "mild": "Không đổi",
            "moderate": "Không đổi",
            "severe": "Không đổi",
            "notes": "Hấp thu toàn thân tối thiểu từ dạng tại chỗ. Không cần điều chỉnh liều ở suy gan."
        },
        "overdose_management": {
            "symptoms": [
                "Kích ứng da nặng"
            ],
            "antidote": "Không có antidote đặc hiệu",
            "treatment": [
                "Ngừng ngay metronidazole tại chỗ",
                "Rửa sạch vùng da",
                "Hỗ trợ và điều trị triệu chứng"
            ],
            "monitoring": "Theo dõi kích ứng da"
        },
        "reversal_agents": {
            "available": False,
            "agents": []
        },
        "administration_instructions": {
            "topical": {
                "technique": "Bôi mỏng 1-2 lần/ngày lên vùng da sạch, khô. Tránh mắt, miệng.",
                "timing": "Dùng 1-2 lần/ngày, đều đặn hàng ngày.",
                "notes": "Dùng cho rosacea. Bôi lên vùng da sạch, khô trước khi đi ngủ và/hoặc buổi sáng."
            }
        },
        "references": {
            "primary_sources": [
                "FDA Drug Label - Metrogel, Metrocream (metronidazole topical)",
                "UpToDate - Topical metronidazole for rosacea"
            ],
            "last_updated": "2025-02-05",
            "evidence_level": "A"
        }
    },
    
    "Clotrimazole topical": {
        "group": "Dermatology - Topical Antifungal",
        "vietnamese_name": "Clotrimazole topical, Lotrimin, Canesten",
        "administration": ["Topical"],
        "indications": [
            "Nấm da (tinea corporis, tinea cruris, tinea pedis)",
            "Nấm móng (onychomycosis) - dạng bôi",
            "Nấm âm đạo (vulvovaginal candidiasis) - dạng kem/viên đặt",
            "Nấm miệng (oral thrush) - dạng viên ngậm"
        ],
        "contraindications": [
            "Dị ứng clotrimazole"
        ],
        "dosage": {
            "adult_topical": "Bôi mỏng 2 lần/ngày lên vùng da bị ảnh hưởng, dùng 2-4 tuần",
            "adult_vaginal": "1% cream hoặc 100mg viên đặt âm đạo x 1 lần/ngày, dùng 3-7 ngày",
            "adult_oral": "10mg viên ngậm x 5 lần/ngày, dùng 14 ngày",
            "notes": "Dùng cho nấm da, nấm móng, nấm âm đạo, nấm miệng. Dùng đủ thời gian để tránh tái phát."
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "Không đổi",
            "under_30": "Không đổi"
        },
        "side_effects": [
            "Kích ứng da tại chỗ (đỏ, rát, ngứa) - hiếm",
            "Bong tróc da",
            "Kích ứng âm đạo (khi dùng dạng đặt)"
        ],
        "interactions": [
            "Ít tương tác thuốc"
        ],
        "pregnancy": "B",
        "mechanism_of_action": "Clotrimazole là imidazole antifungal, ức chế tổng hợp ergosterol (thành phần chính của màng tế bào nấm) bằng cách ức chế enzyme lanosterol 14-alpha-demethylase (CYP51). Thiếu ergosterol làm màng tế bào nấm bị rò rỉ, dẫn đến chết tế bào. Tác dụng với Candida, dermatophytes (Trichophyton, Microsporum, Epidermophyton), và một số nấm khác. Dạng tại chỗ hấp thu toàn thân tối thiểu.",
        "monitoring": [
            "Đáp ứng điều trị (giảm nấm)",
            "Kích ứng da tại chỗ",
            "Dấu hiệu tái phát"
        ],
        "precautions": [
            "Kích ứng da tại chỗ - hiếm",
            "Dùng đủ thời gian (2-4 tuần cho nấm da) để tránh tái phát",
            "Bôi lên vùng da sạch, khô",
            "Tránh mắt, miệng (trừ khi dùng dạng viên ngậm cho nấm miệng)"
        ],
        "pharmacokinetics": {
            "half_life": "Không áp dụng (topical)",
            "onset": "Vài ngày",
            "duration": "12 giờ (dùng 2 lần/ngày)",
            "protein_binding": "Không áp dụng (topical)",
            "clearance": "Hấp thu toàn thân tối thiểu từ dạng tại chỗ."
        },
        "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm, tránh ánh sáng",
        "black_box_warnings": None,
        "drug_interactions": {
            "major": [],
            "moderate": [],
            "minor": []
        },
        "contraindications": {
            "tuyệt_đối": [
                "Dị ứng clotrimazole"
            ],
            "tương_đối": []
        },
        "pregnancy_lactation": {
            "fda_category": "B",
            "pregnancy_details": "Category B - an toàn hơn category C. Hấp thu toàn thân tối thiểu từ dạng tại chỗ.",
            "lactation": {
                "safety": "Compatible",
                "details": "Hấp thu toàn thân tối thiểu từ dạng tại chỗ.",
                "recommendation": "Có thể dùng an toàn khi cho con bú."
            }
        },
        "hepatic_adjustment": {
            "mild": "Không đổi",
            "moderate": "Không đổi",
            "severe": "Không đổi",
            "notes": "Hấp thu toàn thân tối thiểu từ dạng tại chỗ. Không cần điều chỉnh liều ở suy gan."
        },
        "overdose_management": {
            "symptoms": [
                "Kích ứng da nặng"
            ],
            "antidote": "Không có antidote đặc hiệu",
            "treatment": [
                "Ngừng ngay clotrimazole",
                "Rửa sạch vùng da",
                "Hỗ trợ và điều trị triệu chứng"
            ],
            "monitoring": "Theo dõi kích ứng da"
        },
        "reversal_agents": {
            "available": False,
            "agents": []
        },
        "administration_instructions": {
            "topical": {
                "technique": "Bôi mỏng 2 lần/ngày lên vùng da sạch, khô. Tránh mắt, miệng.",
                "timing": "Dùng 2 lần/ngày, đều đặn. Dùng đủ thời gian (2-4 tuần cho nấm da).",
                "notes": "Dùng cho nấm da, nấm móng, nấm âm đạo, nấm miệng."
            }
        },
        "references": {
            "primary_sources": [
                "FDA Drug Label - Lotrimin, Canesten (clotrimazole)",
                "UpToDate - Topical antifungals for skin infections"
            ],
            "last_updated": "2025-02-05",
            "evidence_level": "A"
        }
    },
    
    "Miconazole topical": {
        "group": "Dermatology - Topical Antifungal",
        "vietnamese_name": "Miconazole topical, Monistat, Micatin",
        "administration": ["Topical"],
        "indications": [
            "Nấm da (tinea corporis, tinea cruris, tinea pedis)",
            "Nấm âm đạo (vulvovaginal candidiasis)",
            "Nhiễm nấm da do Candida"
        ],
        "contraindications": [
            "Dị ứng miconazole"
        ],
        "dosage": {
            "adult_topical": "Bôi mỏng 2 lần/ngày lên vùng da bị ảnh hưởng, dùng 2-4 tuần",
            "adult_vaginal": "2% cream hoặc 100-200mg viên đặt âm đạo x 1 lần/ngày, dùng 3-7 ngày",
            "notes": "Dùng cho nấm da, nấm âm đạo. Dùng đủ thời gian để tránh tái phát."
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "Không đổi",
            "under_30": "Không đổi"
        },
        "side_effects": [
            "Kích ứng da tại chỗ (đỏ, rát, ngứa) - hiếm",
            "Bong tróc da",
            "Kích ứng âm đạo (khi dùng dạng đặt)"
        ],
        "interactions": [
            "Warfarin: có thể tăng INR (hiếm với dạng tại chỗ)"
        ],
        "pregnancy": "C",
        "mechanism_of_action": "Miconazole là imidazole antifungal, ức chế tổng hợp ergosterol (thành phần chính của màng tế bào nấm) bằng cách ức chế enzyme lanosterol 14-alpha-demethylase (CYP51). Thiếu ergosterol làm màng tế bào nấm bị rò rỉ, dẫn đến chết tế bào. Tác dụng với Candida, dermatophytes, và một số nấm khác. Dạng tại chỗ hấp thu toàn thân tối thiểu.",
        "monitoring": [
            "Đáp ứng điều trị (giảm nấm)",
            "Kích ứng da tại chỗ",
            "Dấu hiệu tái phát"
        ],
        "precautions": [
            "Kích ứng da tại chỗ - hiếm",
            "Dùng đủ thời gian (2-4 tuần cho nấm da) để tránh tái phát",
            "Bôi lên vùng da sạch, khô",
            "Thận trọng với warfarin (có thể tăng INR, hiếm với dạng tại chỗ)"
        ],
        "pharmacokinetics": {
            "half_life": "Không áp dụng (topical)",
            "onset": "Vài ngày",
            "duration": "12 giờ (dùng 2 lần/ngày)",
            "protein_binding": "Không áp dụng (topical)",
            "clearance": "Hấp thu toàn thân tối thiểu từ dạng tại chỗ."
        },
        "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm, tránh ánh sáng",
        "black_box_warnings": None,
        "drug_interactions": {
            "major": [],
            "moderate": [
                {
                    "drug": "Warfarin",
                    "mechanism": "Có thể ức chế chuyển hóa warfarin",
                    "effect": "Tăng INR, tăng nguy cơ chảy máu (hiếm với dạng tại chỗ)",
                    "management": "Theo dõi INR nếu dùng cùng (hiếm với dạng tại chỗ)."
                }
            ],
            "minor": []
        },
        "contraindications": {
            "tuyệt_đối": [
                "Dị ứng miconazole"
            ],
            "tương_đối": []
        },
        "pregnancy_lactation": {
            "fda_category": "C",
            "pregnancy_details": "Category C - có nguy cơ cho thai nhi. Hấp thu toàn thân tối thiểu từ dạng tại chỗ. Có thể dùng khi lợi ích > nguy cơ.",
            "lactation": {
                "safety": "Compatible",
                "details": "Hấp thu toàn thân tối thiểu từ dạng tại chỗ.",
                "recommendation": "Có thể dùng an toàn khi cho con bú."
            }
        },
        "hepatic_adjustment": {
            "mild": "Không đổi",
            "moderate": "Không đổi",
            "severe": "Không đổi",
            "notes": "Hấp thu toàn thân tối thiểu từ dạng tại chỗ. Không cần điều chỉnh liều ở suy gan."
        },
        "overdose_management": {
            "symptoms": [
                "Kích ứng da nặng"
            ],
            "antidote": "Không có antidote đặc hiệu",
            "treatment": [
                "Ngừng ngay miconazole",
                "Rửa sạch vùng da",
                "Hỗ trợ và điều trị triệu chứng"
            ],
            "monitoring": "Theo dõi kích ứng da"
        },
        "reversal_agents": {
            "available": False,
            "agents": []
        },
        "administration_instructions": {
            "topical": {
                "technique": "Bôi mỏng 2 lần/ngày lên vùng da sạch, khô.",
                "timing": "Dùng 2 lần/ngày, đều đặn. Dùng đủ thời gian (2-4 tuần cho nấm da).",
                "notes": "Dùng cho nấm da, nấm âm đạo."
            }
        },
        "references": {
            "primary_sources": [
                "FDA Drug Label - Monistat, Micatin (miconazole)",
                "UpToDate - Topical antifungals for skin infections"
            ],
            "last_updated": "2025-02-05",
            "evidence_level": "A"
        }
    },
    
    "Ketoconazole topical": {
        "group": "Dermatology - Topical Antifungal",
        "vietnamese_name": "Ketoconazole topical, Nizoral",
        "administration": ["Topical", "Shampoo"],
        "indications": [
            "Nấm da (tinea corporis, tinea cruris, tinea pedis)",
            "Nấm da đầu (tinea capitis)",
            "Gàu, viêm da tiết bã (seborrheic dermatitis) - dạng dầu gội",
            "Nhiễm nấm da do Candida"
        ],
        "contraindications": [
            "Dị ứng ketoconazole"
        ],
        "dosage": {
            "adult_topical": "Bôi mỏng 1-2 lần/ngày lên vùng da bị ảnh hưởng, dùng 2-4 tuần",
            "adult_shampoo": "Dầu gội 2% x 2 lần/tuần, để 5 phút rồi rửa sạch",
            "notes": "Dùng cho nấm da, gàu, viêm da tiết bã. Dùng đủ thời gian để tránh tái phát."
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "Không đổi",
            "under_30": "Không đổi"
        },
        "side_effects": [
            "Kích ứng da tại chỗ (đỏ, rát, ngứa) - hiếm",
            "Bong tróc da",
            "Khô da (khi dùng dầu gội)"
        ],
        "interactions": [
            "Ít tương tác thuốc (dạng tại chỗ)"
        ],
        "pregnancy": "C",
        "mechanism_of_action": "Ketoconazole là imidazole antifungal, ức chế tổng hợp ergosterol (thành phần chính của màng tế bào nấm) bằng cách ức chế enzyme lanosterol 14-alpha-demethylase (CYP51). Thiếu ergosterol làm màng tế bào nấm bị rò rỉ, dẫn đến chết tế bào. Tác dụng với Candida, dermatophytes, Malassezia (gây gàu, viêm da tiết bã), và một số nấm khác. Dạng tại chỗ hấp thu toàn thân tối thiểu. Có dạng kem và dầu gội.",
        "monitoring": [
            "Đáp ứng điều trị (giảm nấm, gàu)",
            "Kích ứng da tại chỗ",
            "Dấu hiệu tái phát"
        ],
        "precautions": [
            "Kích ứng da tại chỗ - hiếm",
            "Dùng đủ thời gian (2-4 tuần cho nấm da) để tránh tái phát",
            "Bôi lên vùng da sạch, khô",
            "Dầu gội: để 5 phút rồi rửa sạch",
            "Tránh mắt, miệng"
        ],
        "pharmacokinetics": {
            "half_life": "Không áp dụng (topical)",
            "onset": "Vài ngày",
            "duration": "12-24 giờ (dùng 1-2 lần/ngày)",
            "protein_binding": "Không áp dụng (topical)",
            "clearance": "Hấp thu toàn thân tối thiểu từ dạng tại chỗ."
        },
        "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm, tránh ánh sáng",
        "black_box_warnings": None,
        "drug_interactions": {
            "major": [],
            "moderate": [],
            "minor": []
        },
        "contraindications": {
            "tuyệt_đối": [
                "Dị ứng ketoconazole"
            ],
            "tương_đối": []
        },
        "pregnancy_lactation": {
            "fda_category": "C",
            "pregnancy_details": "Category C - có nguy cơ cho thai nhi. Hấp thu toàn thân tối thiểu từ dạng tại chỗ. Có thể dùng khi lợi ích > nguy cơ.",
            "lactation": {
                "safety": "Compatible",
                "details": "Hấp thu toàn thân tối thiểu từ dạng tại chỗ.",
                "recommendation": "Có thể dùng an toàn khi cho con bú."
            }
        },
        "hepatic_adjustment": {
            "mild": "Không đổi",
            "moderate": "Không đổi",
            "severe": "Không đổi",
            "notes": "Hấp thu toàn thân tối thiểu từ dạng tại chỗ. Không cần điều chỉnh liều ở suy gan."
        },
        "overdose_management": {
            "symptoms": [
                "Kích ứng da nặng"
            ],
            "antidote": "Không có antidote đặc hiệu",
            "treatment": [
                "Ngừng ngay ketoconazole",
                "Rửa sạch vùng da",
                "Hỗ trợ và điều trị triệu chứng"
            ],
            "monitoring": "Theo dõi kích ứng da"
        },
        "reversal_agents": {
            "available": False,
            "agents": []
        },
        "administration_instructions": {
            "topical": {
                "technique": "Bôi mỏng 1-2 lần/ngày lên vùng da sạch, khô. Tránh mắt, miệng.",
                "timing": "Dùng 1-2 lần/ngày, đều đặn. Dùng đủ thời gian (2-4 tuần cho nấm da).",
                "notes": "Dùng cho nấm da, gàu, viêm da tiết bã. Dầu gội: để 5 phút rồi rửa sạch."
            }
        },
        "references": {
            "primary_sources": [
                "FDA Drug Label - Nizoral (ketoconazole topical)",
                "UpToDate - Topical antifungals for skin infections"
            ],
            "last_updated": "2025-02-05",
            "evidence_level": "A"
        }
    },
    
    "Adapalene": {
        "group": "Dermatology - Topical Retinoid",
        "vietnamese_name": "Adapalene, Differin",
        "administration": ["Topical"],
        "indications": [
            "Mụn trứng cá (acne vulgaris)",
            "Mụn trứng cá viêm",
            "Mụn đầu đen, mụn đầu trắng"
        ],
        "contraindications": [
            "Dị ứng adapalene",
            "Mang thai (category C)"
        ],
        "dosage": {
            "adult_topical": "Bôi mỏng 1 lần/ngày buổi tối lên vùng da bị ảnh hưởng",
            "pediatric": "Bôi mỏng 1 lần/ngày buổi tối (từ 12 tuổi trở lên)",
            "notes": "Retinoid tại chỗ, bôi buổi tối. Tránh ánh nắng mặt trời. Kích ứng da phổ biến khi bắt đầu."
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "Không đổi",
            "under_30": "Không đổi"
        },
        "side_effects": [
            "Kích ứng da tại chỗ (đỏ, rát, khô, bong tróc) - phổ biến khi bắt đầu",
            "Khô da",
            "Nhạy cảm với ánh nắng (tăng nguy cơ cháy nắng)",
            "Ngứa",
            "Đỏ da"
        ],
        "interactions": [
            "Các retinoid khác (tretinoin, isotretinoin): tăng kích ứng da",
            "Benzoyl peroxide: có thể dùng kết hợp (tăng hiệu quả)",
            "Ánh nắng mặt trời: tăng nhạy cảm"
        ],
        "pregnancy": "C",
        "mechanism_of_action": "Adapalene là retinoid tại chỗ thế hệ 3, gắn với retinoic acid receptors (RAR-beta, RAR-gamma). Kích thích tế bào sừng biệt hóa, giảm sự dính kết của tế bào sừng, giảm hình thành microcomedone (tiền thân của mụn). Cũng có tác dụng chống viêm. Đặc điểm: ít kích ứng da hơn tretinoin, ổn định hơn với ánh nắng, có thể dùng kết hợp với benzoyl peroxide. Tác dụng phát huy sau vài tuần.",
        "monitoring": [
            "Đáp ứng điều trị (giảm mụn trứng cá)",
            "Kích ứng da tại chỗ (đỏ, rát, khô, bong tróc)",
            "Nhạy cảm với ánh nắng",
            "Dấu hiệu quá kích ứng (ngừng nếu quá nặng)"
        ],
        "precautions": [
            "Kích ứng da tại chỗ - phổ biến khi bắt đầu, thường tự khỏi sau vài tuần",
            "Nhạy cảm với ánh nắng - TRÁNH ánh nắng mặt trời, dùng kem chống nắng",
            "Bôi buổi tối để tránh ánh nắng",
            "Bắt đầu với tần suất thấp (cách ngày) nếu kích ứng nhiều",
            "Có thể dùng kết hợp với benzoyl peroxide (tăng hiệu quả)",
            "Tránh dùng với các retinoid khác (tăng kích ứng)",
            "Không dùng khi mang thai (category C)"
        ],
        "pharmacokinetics": {
            "half_life": "Không áp dụng (topical)",
            "onset": "Vài tuần",
            "duration": "24 giờ (dùng 1 lần/ngày)",
            "protein_binding": "Không áp dụng (topical)",
            "clearance": "Hấp thu toàn thân tối thiểu từ dạng tại chỗ."
        },
        "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm, tránh ánh sáng",
        "black_box_warnings": "Không dùng khi mang thai (category C). Tránh ánh nắng mặt trời.",
        "drug_interactions": {
            "major": [],
            "moderate": [
                {
                    "drug": "Các retinoid khác (tretinoin, isotretinoin)",
                    "mechanism": "Tác dụng cộng dồn",
                    "effect": "Tăng kích ứng da",
                    "management": "Tránh dùng cùng."
                },
                {
                    "drug": "Ánh nắng mặt trời",
                    "mechanism": "Tăng nhạy cảm với ánh nắng",
                    "effect": "Tăng nguy cơ cháy nắng",
                    "management": "TRÁNH ánh nắng mặt trời, dùng kem chống nắng."
                }
            ],
            "minor": []
        },
        "contraindications": {
            "tuyệt_đối": [
                "Dị ứng adapalene",
                "Mang thai (category C)"
            ],
            "tương_đối": [
                "Da nhạy cảm - thận trọng, bắt đầu với tần suất thấp",
                "Đang dùng các retinoid khác - tránh dùng cùng"
            ]
        },
        "pregnancy_lactation": {
            "fda_category": "C",
            "pregnancy_details": "Category C - có nguy cơ cho thai nhi. Không nên dùng khi mang thai.",
            "lactation": {
                "safety": "Compatible",
                "details": "Hấp thu toàn thân tối thiểu từ dạng tại chỗ.",
                "recommendation": "Có thể dùng khi cho con bú."
            }
        },
        "hepatic_adjustment": {
            "mild": "Không đổi",
            "moderate": "Không đổi",
            "severe": "Không đổi",
            "notes": "Hấp thu toàn thân tối thiểu từ dạng tại chỗ. Không cần điều chỉnh liều ở suy gan."
        },
        "overdose_management": {
            "symptoms": [
                "Kích ứng da nặng (đỏ, rát, bong tróc)",
                "Cháy nắng nặng"
            ],
            "antidote": "Không có antidote đặc hiệu",
            "treatment": [
                "Ngừng ngay adapalene",
                "Rửa sạch vùng da",
                "Điều trị kích ứng da: dưỡng ẩm, tránh ánh nắng",
                "Hỗ trợ và điều trị triệu chứng"
            ],
            "monitoring": "Theo dõi kích ứng da, cháy nắng"
        },
        "reversal_agents": {
            "available": False,
            "agents": []
        },
        "administration_instructions": {
            "topical": {
                "technique": "Bôi mỏng 1 lần/ngày buổi tối lên vùng da sạch, khô. Tránh mắt, miệng.",
                "timing": "Dùng 1 lần/ngày buổi tối. Bắt đầu với tần suất thấp (cách ngày) nếu kích ứng nhiều. TRÁNH ánh nắng mặt trời, dùng kem chống nắng.",
                "notes": "Dùng cho mụn trứng cá. Bôi buổi tối để tránh ánh nắng. Có thể dùng kết hợp với benzoyl peroxide."
            }
        },
        "references": {
            "primary_sources": [
                "FDA Drug Label - Differin (adapalene)",
                "UpToDate - Topical retinoids for acne"
            ],
            "last_updated": "2025-02-05",
            "evidence_level": "A"
        }
    },
    
    "Calcipotriol": {
        "group": "Dermatology - Topical Vitamin D Analog",
        "vietnamese_name": "Calcipotriol, Calcipotriene, Dovonex",
        "administration": ["Topical"],
        "indications": [
            "Vảy nến (psoriasis) - mảng bám",
            "Vảy nến thể mảng",
            "Vảy nến da đầu"
        ],
        "contraindications": [
            "Dị ứng calcipotriol",
            "Tăng calci máu",
            "Rối loạn chuyển hóa calci",
            "Trẻ em <12 tuổi"
        ],
        "dosage": {
            "adult_topical": "Bôi mỏng 2 lần/ngày lên vùng da bị ảnh hưởng, tối đa 100g/tuần",
            "adult_scalp": "Dung dịch bôi da đầu 2 lần/ngày",
            "notes": "Vitamin D analog tại chỗ. Tối đa 100g/tuần để tránh tăng calci máu. Dùng đủ thời gian (4-8 tuần)."
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "Thận trọng (tăng nguy cơ tăng calci máu)",
            "under_30": "Thận trọng (tăng nguy cơ tăng calci máu)"
        },
        "side_effects": [
            "Kích ứng da tại chỗ (đỏ, rát, ngứa) - phổ biến",
            "Bong tróc da",
            "Tăng calci máu (nếu dùng quá liều hoặc diện rộng)",
            "Khô da"
        ],
        "interactions": [
            "Thiazide diuretics: tăng nguy cơ tăng calci máu",
            "Calcium supplements: tăng nguy cơ tăng calci máu"
        ],
        "pregnancy": "C",
        "mechanism_of_action": "Calcipotriol là vitamin D3 analog tại chỗ. Gắn với vitamin D receptor (VDR), điều chỉnh sự biệt hóa và tăng sinh tế bào sừng. Ức chế tăng sinh tế bào sừng (giảm tốc độ tăng trưởng), tăng biệt hóa tế bào sừng (cải thiện chất lượng), và giảm viêm. Được dùng cho vảy nến (psoriasis) - mảng bám. Đặc điểm: tác dụng chậm (4-8 tuần), tối đa 100g/tuần để tránh tăng calci máu, có thể dùng kết hợp với corticosteroid tại chỗ.",
        "monitoring": [
            "Đáp ứng điều trị (giảm vảy nến)",
            "Kích ứng da tại chỗ",
            "Calci máu (nếu dùng diện rộng hoặc lâu dài) - quan trọng",
            "Dấu hiệu tăng calci máu: mệt mỏi, buồn nôn, táo bón"
        ],
        "precautions": [
            "TĂNG CALCI MÁU - tối đa 100g/tuần để tránh tăng calci máu",
            "Theo dõi calci máu nếu dùng diện rộng hoặc lâu dài",
            "Kích ứng da tại chỗ - phổ biến, thường tự khỏi sau vài ngày",
            "Dùng đủ thời gian (4-8 tuần) để đạt hiệu quả",
            "Có thể dùng kết hợp với corticosteroid tại chỗ (tăng hiệu quả)",
            "Thận trọng với thiazide diuretics, calcium supplements (tăng nguy cơ tăng calci máu)",
            "Tránh mắt, miệng"
        ],
        "pharmacokinetics": {
            "half_life": "Không áp dụng (topical)",
            "onset": "4-8 tuần (chậm)",
            "duration": "12 giờ (dùng 2 lần/ngày)",
            "protein_binding": "Không áp dụng (topical)",
            "clearance": "Hấp thu toàn thân tối thiểu từ dạng tại chỗ. Nếu hấp thu: chuyển hóa nhanh thành chất không hoạt động."
        },
        "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm, tránh ánh sáng",
        "black_box_warnings": "Tăng calci máu nếu dùng quá liều hoặc diện rộng. Tối đa 100g/tuần.",
        "drug_interactions": {
            "major": [],
            "moderate": [
                {
                    "drug": "Thiazide diuretics (hydrochlorothiazide, chlorthalidone)",
                    "mechanism": "Tăng tái hấp thu calci ở thận",
                    "effect": "Tăng nguy cơ tăng calci máu",
                    "management": "Thận trọng. Theo dõi calci máu."
                },
                {
                    "drug": "Calcium supplements",
                    "mechanism": "Tăng calci máu",
                    "effect": "Tăng nguy cơ tăng calci máu",
                    "management": "Thận trọng. Theo dõi calci máu."
                }
            ],
            "minor": []
        },
        "contraindications": {
            "tuyệt_đối": [
                "Dị ứng calcipotriol",
                "Tăng calci máu",
                "Rối loạn chuyển hóa calci",
                "Trẻ em <12 tuổi"
            ],
            "tương_đối": [
                "Suy thận - tăng nguy cơ tăng calci máu",
                "Dùng với thiazide diuretics - tăng nguy cơ tăng calci máu"
            ]
        },
        "pregnancy_lactation": {
            "fda_category": "C",
            "pregnancy_details": "Category C - có nguy cơ cho thai nhi. Hấp thu toàn thân tối thiểu từ dạng tại chỗ. Có thể dùng khi lợi ích > nguy cơ.",
            "lactation": {
                "safety": "Compatible",
                "details": "Hấp thu toàn thân tối thiểu từ dạng tại chỗ.",
                "recommendation": "Có thể dùng khi cho con bú."
            }
        },
        "hepatic_adjustment": {
            "mild": "Không đổi",
            "moderate": "Không đổi",
            "severe": "Không đổi",
            "notes": "Hấp thu toàn thân tối thiểu từ dạng tại chỗ. Không cần điều chỉnh liều ở suy gan."
        },
        "overdose_management": {
            "symptoms": [
                "Kích ứng da nặng",
                "Tăng calci máu: mệt mỏi, buồn nôn, táo bón, nhịp tim chậm"
            ],
            "antidote": "Không có antidote đặc hiệu",
            "treatment": [
                "Ngừng ngay calcipotriol",
                "Rửa sạch vùng da",
                "Nếu tăng calci máu: điều trị theo protocol (truyền dịch, furosemide, calcitonin nếu cần)",
                "Theo dõi calci máu",
                "Hỗ trợ và điều trị triệu chứng"
            ],
            "monitoring": "Theo dõi calci máu, kích ứng da"
        },
        "reversal_agents": {
            "available": False,
            "agents": []
        },
        "administration_instructions": {
            "topical": {
                "technique": "Bôi mỏng 2 lần/ngày lên vùng da sạch, khô. Tránh mắt, miệng.",
                "timing": "Dùng 2 lần/ngày, đều đặn. Tối đa 100g/tuần. Dùng đủ thời gian (4-8 tuần).",
                "notes": "Dùng cho vảy nến. Tối đa 100g/tuần để tránh tăng calci máu. Có thể dùng kết hợp với corticosteroid tại chỗ."
            }
        },
        "references": {
            "primary_sources": [
                "FDA Drug Label - Dovonex (calcipotriol)",
                "UpToDate - Topical vitamin D analogs for psoriasis"
            ],
            "last_updated": "2025-02-05",
            "evidence_level": "A"
        }
    },
    
    "Diclofenac gel": {
        "group": "Dermatology - Topical NSAID",
        "vietnamese_name": "Diclofenac gel, Voltaren gel, Pennsaid",
        "administration": ["Topical"],
        "indications": [
            "Đau khớp (osteoarthritis) - tại chỗ",
            "Đau cơ xương - tại chỗ",
            "Viêm gân (tendinitis) - tại chỗ",
            "Đau do chấn thương - tại chỗ"
        ],
        "contraindications": [
            "Dị ứng diclofenac hoặc NSAIDs",
            "Dị ứng aspirin (nếu có hội chứng dị ứng aspirin)",
            "Loét dạ dày tá tràng nặng",
            "Suy thận nặng",
            "Suy gan nặng"
        ],
        "dosage": {
            "adult_topical": "Bôi mỏng 4 lần/ngày lên vùng da bị ảnh hưởng, tối đa 32g/ngày",
            "notes": "NSAID tại chỗ. Bôi lên vùng da sạch, khô. Tránh mắt, miệng, niêm mạc. Hấp thu toàn thân tối thiểu."
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "Thận trọng",
            "under_30": "Thận trọng"
        },
        "side_effects": [
            "Kích ứng da tại chỗ (đỏ, rát, ngứa) - phổ biến",
            "Bong tróc da",
            "Khô da",
            "Phát ban",
            "Tác dụng phụ toàn thân (hiếm, nếu hấp thu nhiều): đau dạ dày, tăng huyết áp"
        ],
        "interactions": [
            "NSAIDs đường uống: tăng nguy cơ tác dụng phụ",
            "Aspirin: tăng nguy cơ chảy máu",
            "Warfarin: có thể tăng INR (hiếm với dạng tại chỗ)"
        ],
        "pregnancy": "C - D trong 3 tháng cuối",
        "mechanism_of_action": "Diclofenac là NSAID (nonsteroidal anti-inflammatory drug), ức chế enzyme cyclooxygenase (COX-1 và COX-2), giảm tổng hợp prostaglandin. Prostaglandin là chất trung gian gây viêm, đau, và sốt. Ức chế COX → giảm prostaglandin → giảm viêm, giảm đau. Dạng gel tại chỗ hấp thu toàn thân tối thiểu, giảm nguy cơ tác dụng phụ toàn thân (đau dạ dày, tổn thương thận) so với NSAID đường uống. Được dùng cho đau khớp, đau cơ xương tại chỗ.",
        "monitoring": [
            "Đáp ứng điều trị (giảm đau, viêm)",
            "Kích ứng da tại chỗ",
            "Dấu hiệu tác dụng phụ toàn thân (hiếm): đau dạ dày, tăng huyết áp"
        ],
        "precautions": [
            "Kích ứng da tại chỗ - phổ biến, thường tự khỏi sau vài ngày",
            "Tránh mắt, miệng, niêm mạc",
            "Bôi lên vùng da sạch, khô",
            "Tối đa 32g/ngày",
            "Thận trọng với NSAIDs đường uống (tăng nguy cơ tác dụng phụ)",
            "Thận trọng với aspirin, warfarin (tăng nguy cơ chảy máu, hiếm với dạng tại chỗ)",
            "Không dùng trong 3 tháng cuối thai kỳ (category D)"
        ],
        "pharmacokinetics": {
            "half_life": "Không áp dụng (topical, hấp thu toàn thân tối thiểu)",
            "onset": "Vài giờ",
            "duration": "6 giờ (dùng 4 lần/ngày)",
            "protein_binding": "Không áp dụng (topical)",
            "clearance": "Hấp thu toàn thân tối thiểu từ dạng gel. Nếu hấp thu: gan (chuyển hóa), thận (thải trừ)."
        },
        "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm, tránh ánh sáng",
        "black_box_warnings": "Không dùng trong 3 tháng cuối thai kỳ (category D). Nguy cơ đau dạ dày, tổn thương thận nếu hấp thu toàn thân (hiếm với dạng tại chỗ).",
        "drug_interactions": {
            "major": [],
            "moderate": [
                {
                    "drug": "NSAIDs đường uống (ibuprofen, naproxen)",
                    "mechanism": "Tác dụng cộng dồn",
                    "effect": "Tăng nguy cơ tác dụng phụ (đau dạ dày, tổn thương thận)",
                    "management": "Thận trọng. Tránh dùng cùng nếu có thể."
                },
                {
                    "drug": "Aspirin, Warfarin",
                    "mechanism": "Tăng nguy cơ chảy máu",
                    "effect": "Tăng nguy cơ chảy máu (hiếm với dạng tại chỗ)",
                    "management": "Thận trọng. Theo dõi INR nếu dùng với warfarin (hiếm với dạng tại chỗ)."
                }
            ],
            "minor": []
        },
        "contraindications": {
            "tuyệt_đối": [
                "Dị ứng diclofenac hoặc NSAIDs",
                "Dị ứng aspirin (nếu có hội chứng dị ứng aspirin)",
                "Loét dạ dày tá tràng nặng",
                "Suy thận nặng",
                "Suy gan nặng",
                "3 tháng cuối thai kỳ (category D)"
            ],
            "tương_đối": [
                "Suy thận nhẹ đến trung bình - thận trọng",
                "Suy gan nhẹ đến trung bình - thận trọng",
                "Dùng với NSAIDs đường uống - tăng nguy cơ tác dụng phụ"
            ]
        },
        "pregnancy_lactation": {
            "fda_category": "C - D trong 3 tháng cuối",
            "pregnancy_details": "Category C trong 1-2 tháng đầu, Category D trong 3 tháng cuối. Không dùng trong 3 tháng cuối thai kỳ (nguy cơ đóng ống động mạch thai nhi). Hấp thu toàn thân tối thiểu từ dạng gel.",
            "lactation": {
                "safety": "Compatible with monitoring",
                "details": "Hấp thu toàn thân tối thiểu từ dạng gel. Bài tiết vào sữa mẹ ở nồng độ rất thấp.",
                "recommendation": "Có thể dùng khi cho con bú với theo dõi."
            }
        },
        "hepatic_adjustment": {
            "mild": "Không đổi",
            "moderate": "Thận trọng",
            "severe": "CHỐNG CHỈ ĐỊNH (nguy cơ tổn thương gan)",
            "notes": "Hấp thu toàn thân tối thiểu từ dạng gel. Nếu hấp thu: chuyển hóa qua gan. Suy gan làm giảm chuyển hóa và tăng nguy cơ tổn thương gan."
        },
        "overdose_management": {
            "symptoms": [
                "Kích ứng da nặng",
                "Tác dụng phụ toàn thân (nếu hấp thu nhiều): đau dạ dày, tổn thương thận"
            ],
            "antidote": "Không có antidote đặc hiệu",
            "treatment": [
                "Ngừng ngay diclofenac gel",
                "Rửa sạch vùng da",
                "Nếu có tác dụng phụ toàn thân: điều trị theo protocol NSAID overdose",
                "Hỗ trợ và điều trị triệu chứng"
            ],
            "monitoring": "Theo dõi kích ứng da, dấu hiệu tác dụng phụ toàn thân"
        },
        "reversal_agents": {
            "available": False,
            "agents": []
        },
        "administration_instructions": {
            "topical": {
                "technique": "Bôi mỏng 4 lần/ngày lên vùng da sạch, khô. Tránh mắt, miệng, niêm mạc.",
                "timing": "Dùng 4 lần/ngày, đều đặn. Tối đa 32g/ngày.",
                "notes": "Dùng cho đau khớp, đau cơ xương tại chỗ. Bôi lên vùng da sạch, khô. Hấp thu toàn thân tối thiểu."
            }
        },
        "references": {
            "primary_sources": [
                "FDA Drug Label - Voltaren gel, Pennsaid (diclofenac gel)",
                "UpToDate - Topical NSAIDs for pain"
            ],
            "last_updated": "2025-02-05",
            "evidence_level": "A"
        }
    },
    
    "Hydrocortisone topical": {
        "group": "Dermatology - Topical Corticosteroid (Low Potency)",
        "vietnamese_name": "Hydrocortisone topical, Cortaid, Cortizone",
        "administration": ["Topical"],
        "indications": [
            "Viêm da dị ứng (atopic dermatitis) nhẹ",
            "Viêm da tiếp xúc (contact dermatitis) nhẹ",
            "Eczema nhẹ",
            "Phát ban nhẹ",
            "Vùng da nhạy cảm (mặt, nách, bẹn)"
        ],
        "contraindications": [
            "Dị ứng hydrocortisone hoặc corticosteroid",
            "Nhiễm trùng da (bacterial, fungal, viral) - không dùng trừ khi có kháng sinh/kháng nấm"
        ],
        "dosage": {
            "adult_topical": "Bôi mỏng 2-4 lần/ngày lên vùng da bị ảnh hưởng",
            "pediatric": "Bôi mỏng 2-4 lần/ngày (từ 2 tuổi trở lên)",
            "notes": "Corticosteroid yếu nhất (low potency). An toàn cho vùng da nhạy cảm. Có thể dùng kéo dài hơn các corticosteroid mạnh."
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "Không đổi",
            "under_30": "Không đổi"
        },
        "side_effects": [
            "Kích ứng da tại chỗ (hiếm)",
            "Teo da (hiếm, nếu dùng kéo dài)",
            "Nhiễm trùng da thứ phát (hiếm)"
        ],
        "interactions": [
            "Không có tương tác đáng kể"
        ],
        "pregnancy": "C",
        "mechanism_of_action": "Hydrocortisone là corticosteroid tự nhiên, low potency (nhóm VII - yếu nhất). Gắn với thụ thể glucocorticoid, ức chế viêm, ức chế miễn dịch, co mạch. Đặc điểm: yếu nhất, an toàn cho vùng da nhạy cảm (mặt, nách, bẹn), có thể dùng kéo dài hơn các corticosteroid mạnh, ít nguy cơ teo da.",
        "monitoring": [
            "Đáp ứng lâm sàng",
            "Kích ứng da tại chỗ (hiếm)",
            "Dấu hiệu teo da (nếu dùng kéo dài)"
        ],
        "precautions": [
            "Corticosteroid yếu nhất - chỉ dùng cho tổn thương nhẹ",
            "An toàn cho vùng da nhạy cảm (mặt, nách, bẹn)",
            "Có thể dùng kéo dài hơn các corticosteroid mạnh",
            "Ít nguy cơ teo da",
            "Tránh dùng trên vùng da bị loét, nhiễm trùng"
        ],
        "pharmacokinetics": {
            "half_life": "Không áp dụng (topical)",
            "onset": "Vài ngày",
            "duration": "6-12 giờ (dùng 2-4 lần/ngày)",
            "protein_binding": "Không áp dụng (topical)",
            "clearance": "Hấp thu toàn thân tối thiểu từ dạng tại chỗ."
        },
        "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm, tránh ánh sáng",
        "black_box_warnings": None,
        "drug_interactions": {
            "major": [],
            "moderate": [],
            "minor": []
        },
        "contraindications": {
            "tuyệt_đối": [
                "Dị ứng hydrocortisone hoặc corticosteroid",
                "Nhiễm trùng da (bacterial, fungal, viral) - không dùng trừ khi có kháng sinh/kháng nấm"
            ],
            "tương_đối": []
        },
        "pregnancy_lactation": {
            "fda_category": "C",
            "pregnancy_details": "Category C - có nguy cơ cho thai nhi. Hấp thu toàn thân tối thiểu từ dạng tại chỗ.",
            "lactation": {
                "safety": "Compatible",
                "details": "Hấp thu toàn thân tối thiểu từ dạng tại chỗ.",
                "recommendation": "Có thể dùng khi cho con bú."
            }
        },
        "hepatic_adjustment": {
            "mild": "Không đổi",
            "moderate": "Không đổi",
            "severe": "Không đổi",
            "notes": "Hấp thu toàn thân tối thiểu từ dạng tại chỗ. Không cần điều chỉnh liều ở suy gan."
        },
        "overdose_management": {
            "symptoms": [
                "Kích ứng da (hiếm)"
            ],
            "antidote": "Không có antidote đặc hiệu",
            "treatment": [
                "Ngừng ngay hydrocortisone",
                "Rửa sạch vùng da",
                "Hỗ trợ và điều trị triệu chứng"
            ],
            "monitoring": "Theo dõi kích ứng da"
        },
        "reversal_agents": {
            "available": False,
            "agents": []
        },
        "administration_instructions": {
            "topical": {
                "technique": "Bôi mỏng 2-4 lần/ngày lên vùng da sạch, khô.",
                "timing": "Dùng 2-4 lần/ngày, đều đặn. Có thể dùng kéo dài hơn các corticosteroid mạnh.",
                "notes": "Corticosteroid yếu nhất. An toàn cho vùng da nhạy cảm (mặt, nách, bẹn)."
            }
        },
        "references": {
            "primary_sources": [
                "FDA Drug Label - Cortaid, Cortizone (hydrocortisone topical)",
                "UpToDate - Topical corticosteroids for skin disorders"
            ],
            "last_updated": "2025-02-05",
            "evidence_level": "A"
        }
    },
    
    "Triamcinolone topical": {
        "group": "Dermatology - Topical Corticosteroid (Medium-High Potency)",
        "vietnamese_name": "Triamcinolone topical, Kenalog, Aristocort",
        "administration": ["Topical"],
        "indications": [
            "Viêm da dị ứng (atopic dermatitis)",
            "Vảy nến (psoriasis)",
            "Viêm da tiếp xúc (contact dermatitis)",
            "Eczema",
            "Lichen planus"
        ],
        "contraindications": [
            "Dị ứng triamcinolone hoặc corticosteroid",
            "Nhiễm trùng da (bacterial, fungal, viral) - không dùng trừ khi có kháng sinh/kháng nấm"
        ],
        "dosage": {
            "adult_topical": "Bôi mỏng 2-4 lần/ngày lên vùng da bị ảnh hưởng",
            "notes": "Medium-high potency (nhóm III-IV). Không dùng >2 tuần liên tục. Tránh dùng trên mặt, nách, bẹn."
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "Không đổi",
            "under_30": "Không đổi"
        },
        "side_effects": [
            "Teo da (skin atrophy) - phổ biến nếu dùng kéo dài",
            "Giãn mạch (telangiectasia)",
            "Rạn da (striae)",
            "Kích ứng da tại chỗ",
            "Nhiễm trùng da thứ phát"
        ],
        "interactions": [
            "Không có tương tác đáng kể"
        ],
        "pregnancy": "C",
        "mechanism_of_action": "Triamcinolone là corticosteroid tổng hợp, medium-high potency (nhóm III-IV). Gắn với thụ thể glucocorticoid, ức chế viêm, ức chế miễn dịch, co mạch. Đặc điểm: medium-high potency, hiệu quả với nhiều bệnh da, nhưng có nguy cơ teo da nếu dùng kéo dài.",
        "monitoring": [
            "Đáp ứng lâm sàng",
            "Dấu hiệu teo da",
            "Dấu hiệu nhiễm trùng da"
        ],
        "precautions": [
            "Medium-high potency - không dùng >2 tuần liên tục",
            "Tránh dùng trên mặt, nách, bẹn",
            "Nguy cơ teo da nếu dùng kéo dài",
            "Tránh dùng trên vùng da bị loét, nhiễm trùng"
        ],
        "pharmacokinetics": {
            "half_life": "Không áp dụng (topical)",
            "onset": "Vài ngày",
            "duration": "6-12 giờ (dùng 2-4 lần/ngày)",
            "protein_binding": "Không áp dụng (topical)",
            "clearance": "Hấp thu toàn thân tối thiểu từ dạng tại chỗ."
        },
        "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm, tránh ánh sáng",
        "black_box_warnings": None,
        "drug_interactions": {
            "major": [],
            "moderate": [],
            "minor": []
        },
        "contraindications": {
            "tuyệt_đối": [
                "Dị ứng triamcinolone hoặc corticosteroid",
                "Nhiễm trùng da (bacterial, fungal, viral) - không dùng trừ khi có kháng sinh/kháng nấm"
            ],
            "tương_đối": []
        },
        "pregnancy_lactation": {
            "fda_category": "C",
            "pregnancy_details": "Category C - có nguy cơ cho thai nhi. Hấp thu toàn thân tối thiểu từ dạng tại chỗ.",
            "lactation": {
                "safety": "Compatible",
                "details": "Hấp thu toàn thân tối thiểu từ dạng tại chỗ.",
                "recommendation": "Có thể dùng khi cho con bú."
            }
        },
        "hepatic_adjustment": {
            "mild": "Không đổi",
            "moderate": "Không đổi",
            "severe": "Không đổi",
            "notes": "Hấp thu toàn thân tối thiểu từ dạng tại chỗ. Không cần điều chỉnh liều ở suy gan."
        },
        "overdose_management": {
            "symptoms": [
                "Teo da nặng",
                "Kích ứng da nặng"
            ],
            "antidote": "Không có antidote đặc hiệu",
            "treatment": [
                "Ngừng ngay triamcinolone",
                "Rửa sạch vùng da",
                "Hỗ trợ và điều trị triệu chứng"
            ],
            "monitoring": "Theo dõi kích ứng da, teo da"
        },
        "reversal_agents": {
            "available": False,
            "agents": []
        },
        "administration_instructions": {
            "topical": {
                "technique": "Bôi mỏng 2-4 lần/ngày lên vùng da sạch, khô.",
                "timing": "Dùng 2-4 lần/ngày, đều đặn. Không dùng >2 tuần liên tục.",
                "notes": "Medium-high potency. Tránh dùng trên mặt, nách, bẹn."
            }
        },
        "references": {
            "primary_sources": [
                "FDA Drug Label - Kenalog, Aristocort (triamcinolone topical)",
                "UpToDate - Topical corticosteroids for skin disorders"
            ],
            "last_updated": "2025-02-05",
            "evidence_level": "A"
        }
    },
    
    "Betamethasone topical": {
        "group": "Dermatology - Topical Corticosteroid (High Potency)",
        "vietnamese_name": "Betamethasone topical, Diprolene, Celestone",
        "administration": ["Topical"],
        "indications": [
            "Viêm da dị ứng (atopic dermatitis) nặng",
            "Vảy nến (psoriasis) nặng",
            "Viêm da tiếp xúc (contact dermatitis) nặng",
            "Eczema nặng"
        ],
        "contraindications": [
            "Dị ứng betamethasone hoặc corticosteroid",
            "Nhiễm trùng da (bacterial, fungal, viral) - không dùng trừ khi có kháng sinh/kháng nấm"
        ],
        "dosage": {
            "adult_topical": "Bôi mỏng 1-2 lần/ngày lên vùng da bị ảnh hưởng",
            "notes": "High potency (nhóm II). Không dùng >2 tuần liên tục. Tránh dùng trên mặt, nách, bẹn."
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "Không đổi",
            "under_30": "Không đổi"
        },
        "side_effects": [
            "Teo da (skin atrophy) - phổ biến nếu dùng kéo dài",
            "Giãn mạch (telangiectasia)",
            "Rạn da (striae)",
            "Kích ứng da tại chỗ",
            "Nhiễm trùng da thứ phát"
        ],
        "interactions": [
            "Không có tương tác đáng kể"
        ],
        "pregnancy": "C",
        "mechanism_of_action": "Betamethasone là corticosteroid tổng hợp, high potency (nhóm II). Gắn với thụ thể glucocorticoid, ức chế viêm, ức chế miễn dịch, co mạch. Đặc điểm: high potency, hiệu quả với tổn thương nặng, nhưng có nguy cơ teo da cao nếu dùng kéo dài.",
        "monitoring": [
            "Đáp ứng lâm sàng",
            "Dấu hiệu teo da",
            "Dấu hiệu nhiễm trùng da"
        ],
        "precautions": [
            "High potency - không dùng >2 tuần liên tục",
            "Tránh dùng trên mặt, nách, bẹn",
            "Nguy cơ teo da cao nếu dùng kéo dài",
            "Tránh dùng trên vùng da bị loét, nhiễm trùng"
        ],
        "pharmacokinetics": {
            "half_life": "Không áp dụng (topical)",
            "onset": "Vài ngày",
            "duration": "12-24 giờ (dùng 1-2 lần/ngày)",
            "protein_binding": "Không áp dụng (topical)",
            "clearance": "Hấp thu toàn thân tối thiểu từ dạng tại chỗ."
        },
        "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm, tránh ánh sáng",
        "black_box_warnings": None,
        "drug_interactions": {
            "major": [],
            "moderate": [],
            "minor": []
        },
        "contraindications": {
            "tuyệt_đối": [
                "Dị ứng betamethasone hoặc corticosteroid",
                "Nhiễm trùng da (bacterial, fungal, viral) - không dùng trừ khi có kháng sinh/kháng nấm"
            ],
            "tương_đối": []
        },
        "pregnancy_lactation": {
            "fda_category": "C",
            "pregnancy_details": "Category C - có nguy cơ cho thai nhi. Hấp thu toàn thân tối thiểu từ dạng tại chỗ.",
            "lactation": {
                "safety": "Compatible",
                "details": "Hấp thu toàn thân tối thiểu từ dạng tại chỗ.",
                "recommendation": "Có thể dùng khi cho con bú."
            }
        },
        "hepatic_adjustment": {
            "mild": "Không đổi",
            "moderate": "Không đổi",
            "severe": "Không đổi",
            "notes": "Hấp thu toàn thân tối thiểu từ dạng tại chỗ. Không cần điều chỉnh liều ở suy gan."
        },
        "overdose_management": {
            "symptoms": [
                "Teo da nặng",
                "Kích ứng da nặng"
            ],
            "antidote": "Không có antidote đặc hiệu",
            "treatment": [
                "Ngừng ngay betamethasone",
                "Rửa sạch vùng da",
                "Hỗ trợ và điều trị triệu chứng"
            ],
            "monitoring": "Theo dõi kích ứng da, teo da"
        },
        "reversal_agents": {
            "available": False,
            "agents": []
        },
        "administration_instructions": {
            "topical": {
                "technique": "Bôi mỏng 1-2 lần/ngày lên vùng da sạch, khô.",
                "timing": "Dùng 1-2 lần/ngày, đều đặn. Không dùng >2 tuần liên tục.",
                "notes": "High potency. Tránh dùng trên mặt, nách, bẹn."
            }
        },
        "references": {
            "primary_sources": [
                "FDA Drug Label - Diprolene, Celestone (betamethasone topical)",
                "UpToDate - Topical corticosteroids for skin disorders"
            ],
            "last_updated": "2025-02-05",
            "evidence_level": "A"
        }
    },
    
    "Mometasone topical": {
        "group": "Dermatology - Topical Corticosteroid (High Potency)",
        "vietnamese_name": "Mometasone topical, Elocon",
        "administration": ["Topical"],
        "indications": [
            "Viêm da dị ứng (atopic dermatitis)",
            "Vảy nến (psoriasis)",
            "Viêm da tiếp xúc (contact dermatitis)",
            "Eczema"
        ],
        "contraindications": [
            "Dị ứng mometasone hoặc corticosteroid",
            "Nhiễm trùng da (bacterial, fungal, viral) - không dùng trừ khi có kháng sinh/kháng nấm"
        ],
        "dosage": {
            "adult_topical": "Bôi mỏng 1 lần/ngày lên vùng da bị ảnh hưởng",
            "notes": "High potency (nhóm II). Dùng 1 lần/ngày. Không dùng >2 tuần liên tục. Tránh dùng trên mặt, nách, bẹn."
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "Không đổi",
            "under_30": "Không đổi"
        },
        "side_effects": [
            "Teo da (skin atrophy) - phổ biến nếu dùng kéo dài",
            "Giãn mạch (telangiectasia)",
            "Rạn da (striae)",
            "Kích ứng da tại chỗ",
            "Nhiễm trùng da thứ phát"
        ],
        "interactions": [
            "Không có tương tác đáng kể"
        ],
        "pregnancy": "C",
        "mechanism_of_action": "Mometasone là corticosteroid tổng hợp, high potency (nhóm II). Gắn với thụ thể glucocorticoid, ức chế viêm, ức chế miễn dịch, co mạch. Đặc điểm: high potency, dùng 1 lần/ngày (ưu điểm), hiệu quả với nhiều bệnh da, nhưng có nguy cơ teo da nếu dùng kéo dài.",
        "monitoring": [
            "Đáp ứng lâm sàng",
            "Dấu hiệu teo da",
            "Dấu hiệu nhiễm trùng da"
        ],
        "precautions": [
            "High potency - không dùng >2 tuần liên tục",
            "Dùng 1 lần/ngày - ưu điểm",
            "Tránh dùng trên mặt, nách, bẹn",
            "Nguy cơ teo da nếu dùng kéo dài",
            "Tránh dùng trên vùng da bị loét, nhiễm trùng"
        ],
        "pharmacokinetics": {
            "half_life": "Không áp dụng (topical)",
            "onset": "Vài ngày",
            "duration": "24 giờ (dùng 1 lần/ngày)",
            "protein_binding": "Không áp dụng (topical)",
            "clearance": "Hấp thu toàn thân tối thiểu từ dạng tại chỗ."
        },
        "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm, tránh ánh sáng",
        "black_box_warnings": None,
        "drug_interactions": {
            "major": [],
            "moderate": [],
            "minor": []
        },
        "contraindications": {
            "tuyệt_đối": [
                "Dị ứng mometasone hoặc corticosteroid",
                "Nhiễm trùng da (bacterial, fungal, viral) - không dùng trừ khi có kháng sinh/kháng nấm"
            ],
            "tương_đối": []
        },
        "pregnancy_lactation": {
            "fda_category": "C",
            "pregnancy_details": "Category C - có nguy cơ cho thai nhi. Hấp thu toàn thân tối thiểu từ dạng tại chỗ.",
            "lactation": {
                "safety": "Compatible",
                "details": "Hấp thu toàn thân tối thiểu từ dạng tại chỗ.",
                "recommendation": "Có thể dùng khi cho con bú."
            }
        },
        "hepatic_adjustment": {
            "mild": "Không đổi",
            "moderate": "Không đổi",
            "severe": "Không đổi",
            "notes": "Hấp thu toàn thân tối thiểu từ dạng tại chỗ. Không cần điều chỉnh liều ở suy gan."
        },
        "overdose_management": {
            "symptoms": [
                "Teo da nặng",
                "Kích ứng da nặng"
            ],
            "antidote": "Không có antidote đặc hiệu",
            "treatment": [
                "Ngừng ngay mometasone",
                "Rửa sạch vùng da",
                "Hỗ trợ và điều trị triệu chứng"
            ],
            "monitoring": "Theo dõi kích ứng da, teo da"
        },
        "reversal_agents": {
            "available": False,
            "agents": []
        },
        "administration_instructions": {
            "topical": {
                "technique": "Bôi mỏng 1 lần/ngày lên vùng da sạch, khô.",
                "timing": "Dùng 1 lần/ngày, đều đặn. Không dùng >2 tuần liên tục.",
                "notes": "High potency. Dùng 1 lần/ngày - ưu điểm. Tránh dùng trên mặt, nách, bẹn."
            }
        },
        "references": {
            "primary_sources": [
                "FDA Drug Label - Elocon (mometasone topical)",
                "UpToDate - Topical corticosteroids for skin disorders"
            ],
            "last_updated": "2025-02-05",
            "evidence_level": "A"
        }
    },
    
    "Erythromycin topical": {
        "group": "Dermatology - Topical Antibiotic",
        "vietnamese_name": "Erythromycin topical, Erygel, Akne-Mycin",
        "administration": ["Topical"],
        "indications": [
            "Mụn trứng cá (acne vulgaris)",
            "Nhiễm khuẩn da do vi khuẩn",
            "Viêm nang lông do vi khuẩn"
        ],
        "contraindications": [
            "Dị ứng erythromycin hoặc macrolides",
            "Nhiễm khuẩn nặng (cần kháng sinh toàn thân)"
        ],
        "dosage": {
            "adult_topical": "Bôi mỏng 2 lần/ngày lên vùng da bị ảnh hưởng",
            "pediatric": "Bôi mỏng 2 lần/ngày (từ 12 tuổi trở lên)",
            "notes": "Macrolide antibiotic tại chỗ. Dùng cho mụn trứng cá. Bôi lên vùng da sạch, khô. Tránh mắt, miệng."
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "Không đổi",
            "under_30": "Không đổi"
        },
        "side_effects": [
            "Kích ứng da tại chỗ (đỏ, rát, khô) - phổ biến",
            "Bong tróc da",
            "Ngứa",
            "Kháng thuốc (nếu dùng kéo dài)"
        ],
        "interactions": [
            "Clindamycin tại chỗ: đối kháng, tránh dùng cùng",
            "Benzoyl peroxide: có thể dùng kết hợp (tăng hiệu quả)"
        ],
        "pregnancy": "B",
        "mechanism_of_action": "Erythromycin là macrolide antibiotic, ức chế tổng hợp protein vi khuẩn bằng cách gắn với 50S ribosomal subunit. Tác dụng với Propionibacterium acnes (vi khuẩn gây mụn trứng cá) và các vi khuẩn Gram-dương khác. Dạng tại chỗ hấp thu toàn thân tối thiểu, giảm nguy cơ tác dụng phụ toàn thân. Được dùng cho mụn trứng cá, đặc biệt mụn viêm.",
        "monitoring": [
            "Đáp ứng điều trị (giảm mụn trứng cá)",
            "Kích ứng da tại chỗ (đỏ, rát, khô)",
            "Dấu hiệu kháng thuốc (nếu dùng kéo dài)"
        ],
        "precautions": [
            "Kích ứng da tại chỗ - phổ biến, thường tự khỏi sau vài ngày",
            "Tránh mắt, miệng",
            "Bôi lên vùng da sạch, khô",
            "Có thể dùng kết hợp với benzoyl peroxide (tăng hiệu quả)",
            "Tránh dùng với clindamycin tại chỗ (đối kháng)",
            "Nguy cơ kháng thuốc nếu dùng kéo dài"
        ],
        "pharmacokinetics": {
            "half_life": "Không áp dụng (topical)",
            "onset": "Vài ngày đến vài tuần",
            "duration": "12 giờ (dùng 2 lần/ngày)",
            "protein_binding": "Không áp dụng (topical)",
            "clearance": "Hấp thu toàn thân tối thiểu từ dạng tại chỗ."
        },
        "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm, tránh ánh sáng",
        "black_box_warnings": None,
        "drug_interactions": {
            "major": [
                {
                    "drug": "Clindamycin tại chỗ",
                    "mechanism": "Đối kháng tác dụng",
                    "effect": "Giảm hiệu quả cả hai",
                    "management": "Tránh dùng cùng."
                }
            ],
            "moderate": [],
            "minor": []
        },
        "contraindications": {
            "tuyệt_đối": [
                "Dị ứng erythromycin hoặc macrolides"
            ],
            "tương_đối": [
                "Nhiễm khuẩn nặng - cần kháng sinh toàn thân",
                "Trẻ em <12 tuổi - thận trọng"
            ]
        },
        "pregnancy_lactation": {
            "fda_category": "B",
            "pregnancy_details": "Category B - an toàn hơn category C. Hấp thu toàn thân tối thiểu từ dạng tại chỗ.",
            "lactation": {
                "safety": "Compatible",
                "details": "Hấp thu toàn thân tối thiểu từ dạng tại chỗ.",
                "recommendation": "Có thể dùng an toàn khi cho con bú."
            }
        },
        "hepatic_adjustment": {
            "mild": "Không đổi",
            "moderate": "Không đổi",
            "severe": "Không đổi",
            "notes": "Hấp thu toàn thân tối thiểu từ dạng tại chỗ. Không cần điều chỉnh liều ở suy gan."
        },
        "overdose_management": {
            "symptoms": [
                "Kích ứng da nặng"
            ],
            "antidote": "Không có antidote đặc hiệu",
            "treatment": [
                "Ngừng ngay erythromycin tại chỗ",
                "Rửa sạch vùng da",
                "Hỗ trợ và điều trị triệu chứng"
            ],
            "monitoring": "Theo dõi kích ứng da"
        },
        "reversal_agents": {
            "available": False,
            "agents": []
        },
        "administration_instructions": {
            "topical": {
                "technique": "Bôi mỏng 2 lần/ngày lên vùng da sạch, khô. Tránh mắt, miệng.",
                "timing": "Dùng 2 lần/ngày, đều đặn. Có thể dùng kết hợp với benzoyl peroxide.",
                "notes": "Dùng cho mụn trứng cá. Bôi lên vùng da sạch, khô trước khi đi ngủ và buổi sáng."
            }
        },
        "references": {
            "primary_sources": [
                "FDA Drug Label - Erygel, Akne-Mycin (erythromycin topical)",
                "UpToDate - Topical antibiotics for acne"
            ],
            "last_updated": "2025-02-05",
            "evidence_level": "A"
        }
    },
    
    "Econazole topical": {
        "group": "Dermatology - Topical Antifungal",
        "vietnamese_name": "Econazole topical, Spectazole",
        "administration": ["Topical"],
        "indications": [
            "Nấm da (tinea corporis, tinea cruris, tinea pedis)",
            "Nhiễm nấm da do Candida",
            "Nấm móng (onychomycosis) - dạng bôi"
        ],
        "contraindications": [
            "Dị ứng econazole"
        ],
        "dosage": {
            "adult_topical": "Bôi mỏng 1-2 lần/ngày lên vùng da bị ảnh hưởng, dùng 2-4 tuần",
            "notes": "Imidazole antifungal tại chỗ. Dùng cho nấm da, nấm móng. Dùng đủ thời gian để tránh tái phát."
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "Không đổi",
            "under_30": "Không đổi"
        },
        "side_effects": [
            "Kích ứng da tại chỗ (đỏ, rát, ngứa) - hiếm",
            "Bong tróc da"
        ],
        "interactions": [
            "Ít tương tác thuốc"
        ],
        "pregnancy": "C",
        "mechanism_of_action": "Econazole là imidazole antifungal, ức chế tổng hợp ergosterol (thành phần chính của màng tế bào nấm) bằng cách ức chế enzyme lanosterol 14-alpha-demethylase (CYP51). Thiếu ergosterol làm màng tế bào nấm bị rò rỉ, dẫn đến chết tế bào. Tác dụng với Candida, dermatophytes, và một số nấm khác. Dạng tại chỗ hấp thu toàn thân tối thiểu.",
        "monitoring": [
            "Đáp ứng điều trị (giảm nấm)",
            "Kích ứng da tại chỗ",
            "Dấu hiệu tái phát"
        ],
        "precautions": [
            "Kích ứng da tại chỗ - hiếm",
            "Dùng đủ thời gian (2-4 tuần cho nấm da) để tránh tái phát",
            "Bôi lên vùng da sạch, khô",
            "Tránh mắt, miệng"
        ],
        "pharmacokinetics": {
            "half_life": "Không áp dụng (topical)",
            "onset": "Vài ngày",
            "duration": "12-24 giờ (dùng 1-2 lần/ngày)",
            "protein_binding": "Không áp dụng (topical)",
            "clearance": "Hấp thu toàn thân tối thiểu từ dạng tại chỗ."
        },
        "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm, tránh ánh sáng",
        "black_box_warnings": None,
        "drug_interactions": {
            "major": [],
            "moderate": [],
            "minor": []
        },
        "contraindications": {
            "tuyệt_đối": [
                "Dị ứng econazole"
            ],
            "tương_đối": []
        },
        "pregnancy_lactation": {
            "fda_category": "C",
            "pregnancy_details": "Category C - có nguy cơ cho thai nhi. Hấp thu toàn thân tối thiểu từ dạng tại chỗ. Có thể dùng khi lợi ích > nguy cơ.",
            "lactation": {
                "safety": "Compatible",
                "details": "Hấp thu toàn thân tối thiểu từ dạng tại chỗ.",
                "recommendation": "Có thể dùng an toàn khi cho con bú."
            }
        },
        "hepatic_adjustment": {
            "mild": "Không đổi",
            "moderate": "Không đổi",
            "severe": "Không đổi",
            "notes": "Hấp thu toàn thân tối thiểu từ dạng tại chỗ. Không cần điều chỉnh liều ở suy gan."
        },
        "overdose_management": {
            "symptoms": [
                "Kích ứng da nặng"
            ],
            "antidote": "Không có antidote đặc hiệu",
            "treatment": [
                "Ngừng ngay econazole",
                "Rửa sạch vùng da",
                "Hỗ trợ và điều trị triệu chứng"
            ],
            "monitoring": "Theo dõi kích ứng da"
        },
        "reversal_agents": {
            "available": False,
            "agents": []
        },
        "administration_instructions": {
            "topical": {
                "technique": "Bôi mỏng 1-2 lần/ngày lên vùng da sạch, khô. Tránh mắt, miệng.",
                "timing": "Dùng 1-2 lần/ngày, đều đặn. Dùng đủ thời gian (2-4 tuần cho nấm da).",
                "notes": "Dùng cho nấm da, nấm móng."
            }
        },
        "references": {
            "primary_sources": [
                "FDA Drug Label - Spectazole (econazole)",
                "UpToDate - Topical antifungals for skin infections"
            ],
            "last_updated": "2025-02-05",
            "evidence_level": "A"
        }
    },
    
    "Tazarotene": {
        "group": "Dermatology - Topical Retinoid",
        "vietnamese_name": "Tazarotene, Tazorac, Avage",
        "administration": ["Topical"],
        "indications": [
            "Mụn trứng cá (acne vulgaris)",
            "Vảy nến (psoriasis)",
            "Làm mờ nếp nhăn (off-label)"
        ],
        "contraindications": [
            "Dị ứng tazarotene",
            "Mang thai (category X)",
            "Đang cho con bú"
        ],
        "dosage": {
            "adult_acne": "Bôi mỏng 1 lần/ngày buổi tối lên vùng da bị ảnh hưởng",
            "adult_psoriasis": "Bôi mỏng 1 lần/ngày buổi tối lên vùng da bị ảnh hưởng",
            "notes": "Retinoid tại chỗ thế hệ 3, bôi buổi tối. Tránh ánh nắng mặt trời. Kích ứng da phổ biến khi bắt đầu. CHỐNG CHỈ ĐỊNH khi mang thai (category X)."
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "Không đổi",
            "under_30": "Không đổi"
        },
        "side_effects": [
            "Kích ứng da tại chỗ (đỏ, rát, khô, bong tróc) - phổ biến khi bắt đầu",
            "Khô da",
            "Nhạy cảm với ánh nắng (tăng nguy cơ cháy nắng)",
            "Ngứa",
            "Đỏ da"
        ],
        "interactions": [
            "Các retinoid khác (tretinoin, adapalene, isotretinoin): tăng kích ứng da",
            "Benzoyl peroxide: có thể dùng kết hợp (tăng hiệu quả)",
            "Ánh nắng mặt trời: tăng nhạy cảm"
        ],
        "pregnancy": "X - CHỐNG CHỈ ĐỊNH",
        "mechanism_of_action": "Tazarotene là retinoid tại chỗ thế hệ 3, là prodrug của tazarotenic acid. Gắn với retinoic acid receptors (RAR-beta, RAR-gamma). Kích thích tế bào sừng biệt hóa, giảm sự dính kết của tế bào sừng, giảm hình thành microcomedone (tiền thân của mụn). Cũng có tác dụng chống viêm và ức chế tăng sinh tế bào (cho vảy nến). Đặc điểm: mạnh hơn tretinoin và adapalene, kích ứng da nhiều hơn, CHỐNG CHỈ ĐỊNH khi mang thai (category X).",
        "monitoring": [
            "Đáp ứng điều trị (giảm mụn trứng cá, vảy nến)",
            "Kích ứng da tại chỗ (đỏ, rát, khô, bong tróc)",
            "Nhạy cảm với ánh nắng",
            "Dấu hiệu quá kích ứng (ngừng nếu quá nặng)"
        ],
        "precautions": [
            "CHỐNG CHỈ ĐỊNH KHI MANG THAI (category X) - nguy cơ dị tật thai nhi",
            "Kích ứng da tại chỗ - phổ biến khi bắt đầu, thường tự khỏi sau vài tuần",
            "Nhạy cảm với ánh nắng - TRÁNH ánh nắng mặt trời, dùng kem chống nắng",
            "Bôi buổi tối để tránh ánh nắng",
            "Bắt đầu với tần suất thấp (cách ngày) nếu kích ứng nhiều",
            "Có thể dùng kết hợp với benzoyl peroxide (tăng hiệu quả)",
            "Tránh dùng với các retinoid khác (tăng kích ứng)",
            "Không dùng khi đang cho con bú"
        ],
        "pharmacokinetics": {
            "half_life": "Không áp dụng (topical)",
            "onset": "Vài tuần",
            "duration": "24 giờ (dùng 1 lần/ngày)",
            "protein_binding": "Không áp dụng (topical)",
            "clearance": "Hấp thu toàn thân tối thiểu từ dạng tại chỗ. Chuyển hóa thành tazarotenic acid."
        },
        "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm, tránh ánh sáng",
        "black_box_warnings": "CHỐNG CHỈ ĐỊNH KHI MANG THAI (category X) - nguy cơ dị tật thai nhi. Tránh ánh nắng mặt trời.",
        "drug_interactions": {
            "major": [],
            "moderate": [
                {
                    "drug": "Các retinoid khác (tretinoin, adapalene, isotretinoin)",
                    "mechanism": "Tác dụng cộng dồn",
                    "effect": "Tăng kích ứng da",
                    "management": "Tránh dùng cùng."
                },
                {
                    "drug": "Ánh nắng mặt trời",
                    "mechanism": "Tăng nhạy cảm với ánh nắng",
                    "effect": "Tăng nguy cơ cháy nắng",
                    "management": "TRÁNH ánh nắng mặt trời, dùng kem chống nắng."
                }
            ],
            "minor": []
        },
        "contraindications": {
            "tuyệt_đối": [
                "Dị ứng tazarotene",
                "Mang thai (category X)",
                "Đang cho con bú"
            ],
            "tương_đối": [
                "Da nhạy cảm - thận trọng, bắt đầu với tần suất thấp",
                "Đang dùng các retinoid khác - tránh dùng cùng"
            ]
        },
        "pregnancy_lactation": {
            "fda_category": "X",
            "pregnancy_details": "Category X - CHỐNG CHỈ ĐỊNH trong thai kỳ. Có nguy cơ dị tật thai nhi nghiêm trọng.",
            "lactation": {
                "safety": "Contraindicated",
                "details": "Không nên dùng khi đang cho con bú.",
                "recommendation": "Tránh dùng khi cho con bú."
            }
        },
        "hepatic_adjustment": {
            "mild": "Không đổi",
            "moderate": "Không đổi",
            "severe": "Không đổi",
            "notes": "Hấp thu toàn thân tối thiểu từ dạng tại chỗ. Không cần điều chỉnh liều ở suy gan."
        },
        "overdose_management": {
            "symptoms": [
                "Kích ứng da nặng (đỏ, rát, bong tróc)",
                "Cháy nắng nặng"
            ],
            "antidote": "Không có antidote đặc hiệu",
            "treatment": [
                "Ngừng ngay tazarotene",
                "Rửa sạch vùng da",
                "Điều trị kích ứng da: dưỡng ẩm, tránh ánh nắng",
                "Hỗ trợ và điều trị triệu chứng"
            ],
            "monitoring": "Theo dõi kích ứng da, cháy nắng"
        },
        "reversal_agents": {
            "available": False,
            "agents": []
        },
        "administration_instructions": {
            "topical": {
                "technique": "Bôi mỏng 1 lần/ngày buổi tối lên vùng da sạch, khô. Tránh mắt, miệng.",
                "timing": "Dùng 1 lần/ngày buổi tối. Bắt đầu với tần suất thấp (cách ngày) nếu kích ứng nhiều. TRÁNH ánh nắng mặt trời, dùng kem chống nắng.",
                "notes": "Dùng cho mụn trứng cá, vảy nến. Bôi buổi tối để tránh ánh nắng. CHỐNG CHỈ ĐỊNH khi mang thai (category X)."
            }
        },
        "references": {
            "primary_sources": [
                "FDA Drug Label - Tazorac, Avage (tazarotene)",
                "UpToDate - Topical retinoids for acne and psoriasis"
            ],
            "last_updated": "2025-02-05",
            "evidence_level": "A"
        }
    },
    
    "Calcitriol topical": {
        "group": "Dermatology - Topical Vitamin D Analog",
        "vietnamese_name": "Calcitriol topical, Vectical",
        "administration": ["Topical"],
        "indications": [
            "Vảy nến (psoriasis) - mảng bám",
            "Vảy nến thể mảng"
        ],
        "contraindications": [
            "Dị ứng calcitriol",
            "Tăng calci máu",
            "Rối loạn chuyển hóa calci"
        ],
        "dosage": {
            "adult_topical": "Bôi mỏng 2 lần/ngày lên vùng da bị ảnh hưởng",
            "notes": "Vitamin D3 analog tại chỗ. Tương tự calcipotriol nhưng là calcitriol (dạng hoạt động). Dùng đủ thời gian (4-8 tuần)."
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "Thận trọng (tăng nguy cơ tăng calci máu)",
            "under_30": "Thận trọng (tăng nguy cơ tăng calci máu)"
        },
        "side_effects": [
            "Kích ứng da tại chỗ (đỏ, rát, ngứa) - phổ biến",
            "Bong tróc da",
            "Tăng calci máu (nếu dùng quá liều hoặc diện rộng)",
            "Khô da"
        ],
        "interactions": [
            "Thiazide diuretics: tăng nguy cơ tăng calci máu",
            "Calcium supplements: tăng nguy cơ tăng calci máu"
        ],
        "pregnancy": "C",
        "mechanism_of_action": "Calcitriol là vitamin D3 dạng hoạt động tại chỗ. Gắn với vitamin D receptor (VDR), điều chỉnh sự biệt hóa và tăng sinh tế bào sừng. Ức chế tăng sinh tế bào sừng (giảm tốc độ tăng trưởng), tăng biệt hóa tế bào sừng (cải thiện chất lượng), và giảm viêm. Được dùng cho vảy nến (psoriasis) - mảng bám. Đặc điểm: tác dụng chậm (4-8 tuần), nguy cơ tăng calci máu nếu dùng diện rộng, tương tự calcipotriol nhưng là calcitriol (dạng hoạt động).",
        "monitoring": [
            "Đáp ứng điều trị (giảm vảy nến)",
            "Kích ứng da tại chỗ",
            "Calci máu (nếu dùng diện rộng hoặc lâu dài) - quan trọng",
            "Dấu hiệu tăng calci máu: mệt mỏi, buồn nôn, táo bón"
        ],
        "precautions": [
            "TĂNG CALCI MÁU - theo dõi calci máu nếu dùng diện rộng hoặc lâu dài",
            "Kích ứng da tại chỗ - phổ biến, thường tự khỏi sau vài ngày",
            "Dùng đủ thời gian (4-8 tuần) để đạt hiệu quả",
            "Có thể dùng kết hợp với corticosteroid tại chỗ (tăng hiệu quả)",
            "Thận trọng với thiazide diuretics, calcium supplements (tăng nguy cơ tăng calci máu)",
            "Tránh mắt, miệng"
        ],
        "pharmacokinetics": {
            "half_life": "Không áp dụng (topical)",
            "onset": "4-8 tuần (chậm)",
            "duration": "12 giờ (dùng 2 lần/ngày)",
            "protein_binding": "Không áp dụng (topical)",
            "clearance": "Hấp thu toàn thân tối thiểu từ dạng tại chỗ."
        },
        "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm, tránh ánh sáng",
        "black_box_warnings": "Tăng calci máu nếu dùng quá liều hoặc diện rộng.",
        "drug_interactions": {
            "major": [],
            "moderate": [
                {
                    "drug": "Thiazide diuretics (hydrochlorothiazide, chlorthalidone)",
                    "mechanism": "Tăng tái hấp thu calci ở thận",
                    "effect": "Tăng nguy cơ tăng calci máu",
                    "management": "Thận trọng. Theo dõi calci máu."
                },
                {
                    "drug": "Calcium supplements",
                    "mechanism": "Tăng calci máu",
                    "effect": "Tăng nguy cơ tăng calci máu",
                    "management": "Thận trọng. Theo dõi calci máu."
                }
            ],
            "minor": []
        },
        "contraindications": {
            "tuyệt_đối": [
                "Dị ứng calcitriol",
                "Tăng calci máu",
                "Rối loạn chuyển hóa calci"
            ],
            "tương_đối": [
                "Suy thận - tăng nguy cơ tăng calci máu",
                "Dùng với thiazide diuretics - tăng nguy cơ tăng calci máu"
            ]
        },
        "pregnancy_lactation": {
            "fda_category": "C",
            "pregnancy_details": "Category C - có nguy cơ cho thai nhi. Hấp thu toàn thân tối thiểu từ dạng tại chỗ.",
            "lactation": {
                "safety": "Compatible",
                "details": "Hấp thu toàn thân tối thiểu từ dạng tại chỗ.",
                "recommendation": "Có thể dùng khi cho con bú."
            }
        },
        "hepatic_adjustment": {
            "mild": "Không đổi",
            "moderate": "Không đổi",
            "severe": "Không đổi",
            "notes": "Hấp thu toàn thân tối thiểu từ dạng tại chỗ. Không cần điều chỉnh liều ở suy gan."
        },
        "overdose_management": {
            "symptoms": [
                "Kích ứng da nặng",
                "Tăng calci máu: mệt mỏi, buồn nôn, táo bón, nhịp tim chậm"
            ],
            "antidote": "Không có antidote đặc hiệu",
            "treatment": [
                "Ngừng ngay calcitriol",
                "Rửa sạch vùng da",
                "Nếu tăng calci máu: điều trị theo protocol (truyền dịch, furosemide, calcitonin nếu cần)",
                "Theo dõi calci máu",
                "Hỗ trợ và điều trị triệu chứng"
            ],
            "monitoring": "Theo dõi calci máu, kích ứng da"
        },
        "reversal_agents": {
            "available": False,
            "agents": []
        },
        "administration_instructions": {
            "topical": {
                "technique": "Bôi mỏng 2 lần/ngày lên vùng da sạch, khô. Tránh mắt, miệng.",
                "timing": "Dùng 2 lần/ngày, đều đặn. Dùng đủ thời gian (4-8 tuần).",
                "notes": "Dùng cho vảy nến. Có thể dùng kết hợp với corticosteroid tại chỗ."
            }
        },
        "references": {
            "primary_sources": [
                "FDA Drug Label - Vectical (calcitriol topical)",
                "UpToDate - Topical vitamin D analogs for psoriasis"
            ],
            "last_updated": "2025-02-05",
            "evidence_level": "A"
        }
    },
    
    "Azelaic Acid": {
        "group": "Dermatology - Topical Antiacne/Anti-inflammatory",
        "vietnamese_name": "Azelaic acid, Finacea, Azelex",
        "administration": ["Topical"],
        "indications": [
            "Mụn trứng cá (acne vulgaris)",
            "Rosacea (đỏ mặt, mụn mủ)",
            "Melasma (tăng sắc tố da)"
        ],
        "contraindications": [
            "Dị ứng azelaic acid"
        ],
        "dosage": {
            "adult_topical": "Bôi mỏng 2 lần/ngày lên vùng da bị ảnh hưởng",
            "notes": "Antiacne, anti-inflammatory, và làm sáng da. Dùng cho mụn trứng cá, rosacea, melasma. Kích ứng da nhẹ hơn retinoid."
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "Không đổi",
            "under_30": "Không đổi"
        },
        "side_effects": [
            "Kích ứng da tại chỗ (đỏ, rát, khô) - phổ biến khi bắt đầu",
            "Bong tróc da",
            "Ngứa",
            "Khô da"
        ],
        "interactions": [
            "Ít tương tác thuốc"
        ],
        "pregnancy": "B",
        "mechanism_of_action": "Azelaic acid có nhiều tác dụng: (1) Ức chế Propionibacterium acnes (vi khuẩn gây mụn trứng cá), (2) Ức chế tyrosinase (enzyme tạo melanin) → làm sáng da, giảm melasma, (3) Chống viêm, (4) Ức chế tăng sinh tế bào sừng. Được dùng cho mụn trứng cá, rosacea, và melasma. Đặc điểm: kích ứng da nhẹ hơn retinoid, an toàn cho da nhạy cảm, có thể dùng khi mang thai (category B).",
        "monitoring": [
            "Đáp ứng điều trị (giảm mụn trứng cá, rosacea, melasma)",
            "Kích ứng da tại chỗ (đỏ, rát, khô)",
            "Dấu hiệu quá kích ứng (ngừng nếu quá nặng)"
        ],
        "precautions": [
            "Kích ứng da tại chỗ - phổ biến khi bắt đầu, thường tự khỏi sau vài tuần",
            "Kích ứng nhẹ hơn retinoid - ưu điểm",
            "An toàn cho da nhạy cảm",
            "Có thể dùng khi mang thai (category B)",
            "Bôi lên vùng da sạch, khô",
            "Tránh mắt, miệng"
        ],
        "pharmacokinetics": {
            "half_life": "Không áp dụng (topical)",
            "onset": "Vài tuần",
            "duration": "12 giờ (dùng 2 lần/ngày)",
            "protein_binding": "Không áp dụng (topical)",
            "clearance": "Hấp thu toàn thân tối thiểu từ dạng tại chỗ."
        },
        "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm, tránh ánh sáng",
        "black_box_warnings": None,
        "drug_interactions": {
            "major": [],
            "moderate": [],
            "minor": []
        },
        "contraindications": {
            "tuyệt_đối": [
                "Dị ứng azelaic acid"
            ],
            "tương_đối": []
        },
        "pregnancy_lactation": {
            "fda_category": "B",
            "pregnancy_details": "Category B - an toàn hơn category C. Hấp thu toàn thân tối thiểu từ dạng tại chỗ.",
            "lactation": {
                "safety": "Compatible",
                "details": "Hấp thu toàn thân tối thiểu từ dạng tại chỗ.",
                "recommendation": "Có thể dùng an toàn khi cho con bú."
            }
        },
        "hepatic_adjustment": {
            "mild": "Không đổi",
            "moderate": "Không đổi",
            "severe": "Không đổi",
            "notes": "Hấp thu toàn thân tối thiểu từ dạng tại chỗ. Không cần điều chỉnh liều ở suy gan."
        },
        "overdose_management": {
            "symptoms": [
                "Kích ứng da nặng"
            ],
            "antidote": "Không có antidote đặc hiệu",
            "treatment": [
                "Ngừng ngay azelaic acid",
                "Rửa sạch vùng da",
                "Hỗ trợ và điều trị triệu chứng"
            ],
            "monitoring": "Theo dõi kích ứng da"
        },
        "reversal_agents": {
            "available": False,
            "agents": []
        },
        "administration_instructions": {
            "topical": {
                "technique": "Bôi mỏng 2 lần/ngày lên vùng da sạch, khô. Tránh mắt, miệng.",
                "timing": "Dùng 2 lần/ngày, đều đặn. Có thể dùng kết hợp với các thuốc khác.",
                "notes": "Dùng cho mụn trứng cá, rosacea, melasma. Kích ứng nhẹ hơn retinoid."
            }
        },
        "references": {
            "primary_sources": [
                "FDA Drug Label - Finacea, Azelex (azelaic acid)",
                "UpToDate - Topical azelaic acid for acne and rosacea"
            ],
            "last_updated": "2025-02-05",
            "evidence_level": "A"
        }
    },
    
    "Salicylic Acid": {
        "group": "Dermatology - Topical Keratolytic",
        "vietnamese_name": "Salicylic acid, Salicylic acid topical",
        "administration": ["Topical"],
        "indications": [
            "Mụn cóc (warts)",
            "Mụn trứng cá (acne vulgaris)",
            "Vảy nến (psoriasis)",
            "Gàu, viêm da tiết bã (seborrheic dermatitis)",
            "Da chết, tẩy tế bào chết"
        ],
        "contraindications": [
            "Dị ứng salicylic acid hoặc aspirin",
            "Suy thận nặng",
            "Trẻ em <2 tuổi (nguy cơ hấp thu toàn thân)"
        ],
        "dosage": {
            "adult_topical": "Bôi mỏng 1-3 lần/ngày lên vùng da bị ảnh hưởng",
            "adult_warts": "Bôi mỏng 1-2 lần/ngày, dùng 12 tuần",
            "notes": "Keratolytic, làm bong tróc lớp sừng. Nồng độ khác nhau cho các chỉ định khác nhau (2-17%)."
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "Thận trọng",
            "under_30": "Thận trọng (tăng nguy cơ hấp thu toàn thân)"
        },
        "side_effects": [
            "Kích ứng da tại chỗ (đỏ, rát, khô) - phổ biến",
            "Bong tróc da",
            "Ngộ độc salicylate (nếu dùng diện rộng, nồng độ cao) - hiếm nhưng nguy hiểm",
            "Khô da"
        ],
        "interactions": [
            "Warfarin: có thể tăng INR (nếu hấp thu toàn thân)",
            "Aspirin: tăng nguy cơ ngộ độc salicylate"
        ],
        "pregnancy": "C",
        "mechanism_of_action": "Salicylic acid là keratolytic (làm bong tróc lớp sừng). Hòa tan chất kết dính giữa các tế bào sừng, làm bong tróc lớp sừng, giảm độ dày của lớp sừng. Được dùng cho mụn cóc (làm bong tróc), mụn trứng cá (làm thông thoáng lỗ chân lông), vảy nến (làm bong tróc vảy), gàu (làm bong tróc vảy). Đặc điểm: keratolytic, nồng độ khác nhau cho các chỉ định khác nhau (2-17%), nguy cơ ngộ độc salicylate nếu dùng diện rộng hoặc nồng độ cao.",
        "monitoring": [
            "Đáp ứng điều trị (giảm mụn cóc, mụn trứng cá, vảy nến)",
            "Kích ứng da tại chỗ",
            "Dấu hiệu ngộ độc salicylate (nếu dùng diện rộng): ù tai, buồn nôn, thở nhanh, rối loạn ý thức"
        ],
        "precautions": [
            "Kích ứng da tại chỗ - phổ biến",
            "Ngộ độc salicylate - hiếm nhưng nguy hiểm, đặc biệt nếu dùng diện rộng hoặc nồng độ cao",
            "Thận trọng ở trẻ em <2 tuổi (tăng nguy cơ hấp thu toàn thân)",
            "Thận trọng ở suy thận (tăng nguy cơ hấp thu toàn thân)",
            "Tránh dùng với aspirin (tăng nguy cơ ngộ độc salicylate)",
            "Bôi lên vùng da sạch, khô",
            "Tránh mắt, miệng, niêm mạc"
        ],
        "pharmacokinetics": {
            "half_life": "Không áp dụng (topical, hấp thu toàn thân tối thiểu)",
            "onset": "Vài ngày",
            "duration": "6-12 giờ (dùng 1-3 lần/ngày)",
            "protein_binding": "Không áp dụng (topical)",
            "clearance": "Hấp thu toàn thân tối thiểu từ dạng tại chỗ. Nếu hấp thu: gan (chuyển hóa), thận (thải trừ)."
        },
        "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm, tránh ánh sáng",
        "black_box_warnings": "Ngộ độc salicylate nếu dùng diện rộng hoặc nồng độ cao - hiếm nhưng nguy hiểm.",
        "drug_interactions": {
            "major": [],
            "moderate": [
                {
                    "drug": "Aspirin",
                    "mechanism": "Cả hai đều là salicylate",
                    "effect": "Tăng nguy cơ ngộ độc salicylate",
                    "management": "Thận trọng. Tránh dùng cùng nếu có thể."
                },
                {
                    "drug": "Warfarin",
                    "mechanism": "Salicylic acid có thể tăng INR (nếu hấp thu toàn thân)",
                    "effect": "Tăng INR, tăng nguy cơ chảy máu (hiếm với dạng tại chỗ)",
                    "management": "Thận trọng. Theo dõi INR nếu dùng cùng (hiếm với dạng tại chỗ)."
                }
            ],
            "minor": []
        },
        "contraindications": {
            "tuyệt_đối": [
                "Dị ứng salicylic acid hoặc aspirin",
                "Suy thận nặng",
                "Trẻ em <2 tuổi (nguy cơ hấp thu toàn thân)"
            ],
            "tương_đối": [
                "Suy thận nhẹ đến trung bình - tăng nguy cơ hấp thu toàn thân",
                "Dùng với aspirin - tăng nguy cơ ngộ độc salicylate"
            ]
        },
        "pregnancy_lactation": {
            "fda_category": "C",
            "pregnancy_details": "Category C - có nguy cơ cho thai nhi. Hấp thu toàn thân tối thiểu từ dạng tại chỗ.",
            "lactation": {
                "safety": "Compatible",
                "details": "Hấp thu toàn thân tối thiểu từ dạng tại chỗ.",
                "recommendation": "Có thể dùng khi cho con bú."
            }
        },
        "hepatic_adjustment": {
            "mild": "Không đổi",
            "moderate": "Không đổi",
            "severe": "Không đổi",
            "notes": "Hấp thu toàn thân tối thiểu từ dạng tại chỗ. Không cần điều chỉnh liều ở suy gan."
        },
        "overdose_management": {
            "symptoms": [
                "Kích ứng da nặng",
                "Ngộ độc salicylate: ù tai, buồn nôn, thở nhanh, rối loạn ý thức, sốt"
            ],
            "antidote": "Không có antidote đặc hiệu. Điều trị ngộ độc salicylate.",
            "treatment": [
                "Ngừng ngay salicylic acid",
                "Rửa sạch vùng da",
                "Nếu ngộ độc salicylate: truyền dịch, điều chỉnh điện giải, có thể cần lọc máu",
                "Theo dõi dấu hiệu sinh tồn",
                "Hỗ trợ và điều trị triệu chứng"
            ],
            "monitoring": "Theo dõi kích ứng da, dấu hiệu ngộ độc salicylate"
        },
        "reversal_agents": {
            "available": False,
            "agents": []
        },
        "administration_instructions": {
            "topical": {
                "technique": "Bôi mỏng 1-3 lần/ngày lên vùng da sạch, khô. Tránh mắt, miệng, niêm mạc.",
                "timing": "Dùng 1-3 lần/ngày, đều đặn. Nồng độ khác nhau cho các chỉ định khác nhau.",
                "notes": "Dùng cho mụn cóc, mụn trứng cá, vảy nến, gàu. Thận trọng nếu dùng diện rộng hoặc nồng độ cao."
            }
        },
        "references": {
            "primary_sources": [
                "FDA Drug Label - Salicylic acid topical",
                "UpToDate - Topical salicylic acid for warts and acne"
            ],
            "last_updated": "2025-02-05",
            "evidence_level": "A"
        }
    },
    
    "Ketoprofen gel": {
        "group": "Dermatology - Topical NSAID",
        "vietnamese_name": "Ketoprofen gel, Fastum gel",
        "administration": ["Topical"],
        "indications": [
            "Đau khớp (osteoarthritis) - tại chỗ",
            "Đau cơ xương - tại chỗ",
            "Viêm gân (tendinitis) - tại chỗ",
            "Đau do chấn thương - tại chỗ"
        ],
        "contraindications": [
            "Dị ứng ketoprofen hoặc NSAIDs",
            "Dị ứng aspirin (nếu có hội chứng dị ứng aspirin)",
            "Loét dạ dày tá tràng nặng",
            "Suy thận nặng",
            "Suy gan nặng"
        ],
        "dosage": {
            "adult_topical": "Bôi mỏng 2-3 lần/ngày lên vùng da bị ảnh hưởng",
            "notes": "NSAID tại chỗ. Bôi lên vùng da sạch, khô. Tránh mắt, miệng, niêm mạc. Hấp thu toàn thân tối thiểu."
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "Thận trọng",
            "under_30": "Thận trọng"
        },
        "side_effects": [
            "Kích ứng da tại chỗ (đỏ, rát, ngứa) - phổ biến",
            "Bong tróc da",
            "Khô da",
            "Phát ban",
            "Tác dụng phụ toàn thân (hiếm, nếu hấp thu nhiều): đau dạ dày, tăng huyết áp"
        ],
        "interactions": [
            "NSAIDs đường uống: tăng nguy cơ tác dụng phụ",
            "Aspirin: tăng nguy cơ chảy máu",
            "Warfarin: có thể tăng INR (hiếm với dạng tại chỗ)"
        ],
        "pregnancy": "C - D trong 3 tháng cuối",
        "mechanism_of_action": "Ketoprofen là NSAID (nonsteroidal anti-inflammatory drug), ức chế enzyme cyclooxygenase (COX-1 và COX-2), giảm tổng hợp prostaglandin. Prostaglandin là chất trung gian gây viêm, đau, và sốt. Ức chế COX → giảm prostaglandin → giảm viêm, giảm đau. Dạng gel tại chỗ hấp thu toàn thân tối thiểu, giảm nguy cơ tác dụng phụ toàn thân (đau dạ dày, tổn thương thận) so với NSAID đường uống. Được dùng cho đau khớp, đau cơ xương tại chỗ.",
        "monitoring": [
            "Đáp ứng điều trị (giảm đau, viêm)",
            "Kích ứng da tại chỗ",
            "Dấu hiệu tác dụng phụ toàn thân (hiếm): đau dạ dày, tăng huyết áp"
        ],
        "precautions": [
            "Kích ứng da tại chỗ - phổ biến, thường tự khỏi sau vài ngày",
            "Tránh mắt, miệng, niêm mạc",
            "Bôi lên vùng da sạch, khô",
            "Thận trọng với NSAIDs đường uống (tăng nguy cơ tác dụng phụ)",
            "Thận trọng với aspirin, warfarin (tăng nguy cơ chảy máu, hiếm với dạng tại chỗ)",
            "Không dùng trong 3 tháng cuối thai kỳ (category D)"
        ],
        "pharmacokinetics": {
            "half_life": "Không áp dụng (topical, hấp thu toàn thân tối thiểu)",
            "onset": "Vài giờ",
            "duration": "6-8 giờ (dùng 2-3 lần/ngày)",
            "protein_binding": "Không áp dụng (topical)",
            "clearance": "Hấp thu toàn thân tối thiểu từ dạng gel. Nếu hấp thu: gan (chuyển hóa), thận (thải trừ)."
        },
        "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm, tránh ánh sáng",
        "black_box_warnings": "Không dùng trong 3 tháng cuối thai kỳ (category D). Nguy cơ đau dạ dày, tổn thương thận nếu hấp thu toàn thân (hiếm với dạng tại chỗ).",
        "drug_interactions": {
            "major": [],
            "moderate": [
                {
                    "drug": "NSAIDs đường uống (ibuprofen, naproxen)",
                    "mechanism": "Tác dụng cộng dồn",
                    "effect": "Tăng nguy cơ tác dụng phụ (đau dạ dày, tổn thương thận)",
                    "management": "Thận trọng. Tránh dùng cùng nếu có thể."
                },
                {
                    "drug": "Aspirin, Warfarin",
                    "mechanism": "Tăng nguy cơ chảy máu",
                    "effect": "Tăng nguy cơ chảy máu (hiếm với dạng tại chỗ)",
                    "management": "Thận trọng. Theo dõi INR nếu dùng với warfarin (hiếm với dạng tại chỗ)."
                }
            ],
            "minor": []
        },
        "contraindications": {
            "tuyệt_đối": [
                "Dị ứng ketoprofen hoặc NSAIDs",
                "Dị ứng aspirin (nếu có hội chứng dị ứng aspirin)",
                "Loét dạ dày tá tràng nặng",
                "Suy thận nặng",
                "Suy gan nặng",
                "3 tháng cuối thai kỳ (category D)"
            ],
            "tương_đối": [
                "Suy thận nhẹ đến trung bình - thận trọng",
                "Suy gan nhẹ đến trung bình - thận trọng",
                "Dùng với NSAIDs đường uống - tăng nguy cơ tác dụng phụ"
            ]
        },
        "pregnancy_lactation": {
            "fda_category": "C - D trong 3 tháng cuối",
            "pregnancy_details": "Category C trong 1-2 tháng đầu, Category D trong 3 tháng cuối. Không dùng trong 3 tháng cuối thai kỳ (nguy cơ đóng ống động mạch thai nhi). Hấp thu toàn thân tối thiểu từ dạng gel.",
            "lactation": {
                "safety": "Compatible with monitoring",
                "details": "Hấp thu toàn thân tối thiểu từ dạng gel. Bài tiết vào sữa mẹ ở nồng độ rất thấp.",
                "recommendation": "Có thể dùng khi cho con bú với theo dõi."
            }
        },
        "hepatic_adjustment": {
            "mild": "Không đổi",
            "moderate": "Thận trọng",
            "severe": "CHỐNG CHỈ ĐỊNH (nguy cơ tổn thương gan)",
            "notes": "Hấp thu toàn thân tối thiểu từ dạng gel. Nếu hấp thu: chuyển hóa qua gan. Suy gan làm giảm chuyển hóa và tăng nguy cơ tổn thương gan."
        },
        "overdose_management": {
            "symptoms": [
                "Kích ứng da nặng",
                "Tác dụng phụ toàn thân (nếu hấp thu nhiều): đau dạ dày, tổn thương thận"
            ],
            "antidote": "Không có antidote đặc hiệu",
            "treatment": [
                "Ngừng ngay ketoprofen gel",
                "Rửa sạch vùng da",
                "Nếu có tác dụng phụ toàn thân: điều trị theo protocol NSAID overdose",
                "Hỗ trợ và điều trị triệu chứng"
            ],
            "monitoring": "Theo dõi kích ứng da, dấu hiệu tác dụng phụ toàn thân"
        },
        "reversal_agents": {
            "available": False,
            "agents": []
        },
        "administration_instructions": {
            "topical": {
                "technique": "Bôi mỏng 2-3 lần/ngày lên vùng da sạch, khô. Tránh mắt, miệng, niêm mạc.",
                "timing": "Dùng 2-3 lần/ngày, đều đặn.",
                "notes": "Dùng cho đau khớp, đau cơ xương tại chỗ. Bôi lên vùng da sạch, khô. Hấp thu toàn thân tối thiểu."
            }
        },
        "references": {
            "primary_sources": [
                "FDA Drug Label - Fastum gel (ketoprofen gel)",
                "UpToDate - Topical NSAIDs for pain"
            ],
            "last_updated": "2025-02-05",
            "evidence_level": "A"
        }
    },
    
    "Ivermectin cream": {
        "group": "Dermatology - Topical Antiparasitic",
        "vietnamese_name": "Ivermectin cream, Soolantra",
        "administration": ["Topical"],
        "indications": [
            "Rosacea (đỏ mặt, mụn mủ)",
            "Demodex mites (có thể liên quan đến rosacea)"
        ],
        "contraindications": [
            "Dị ứng ivermectin"
        ],
        "dosage": {
            "adult_topical": "Bôi mỏng 1 lần/ngày buổi tối lên vùng da bị ảnh hưởng",
            "notes": "Antiparasitic tại chỗ. Dùng cho rosacea. Bôi lên vùng da sạch, khô. Tránh mắt, miệng."
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "Không đổi",
            "under_30": "Không đổi"
        },
        "side_effects": [
            "Kích ứng da tại chỗ (đỏ, rát, khô) - phổ biến khi bắt đầu",
            "Bong tróc da",
            "Ngứa",
            "Khô da"
        ],
        "interactions": [
            "Ít tương tác thuốc (dạng tại chỗ)"
        ],
        "pregnancy": "C",
        "mechanism_of_action": "Ivermectin là antiparasitic, ức chế kênh chloride phụ thuộc glutamate (glutamate-gated chloride channels) trong tế bào thần kinh và cơ của ký sinh trùng. Gây tăng tính thấm màng tế bào, dẫn đến tê liệt và chết ký sinh trùng. Tác dụng với Demodex mites (có thể liên quan đến rosacea) và các ký sinh trùng khác. Dạng cream tại chỗ hấp thu toàn thân tối thiểu, giảm nguy cơ tác dụng phụ toàn thân. Được dùng chủ yếu cho rosacea (đỏ mặt, mụn mủ).",
        "monitoring": [
            "Đáp ứng điều trị (giảm rosacea)",
            "Kích ứng da tại chỗ (đỏ, rát, khô)",
            "Dấu hiệu quá kích ứng (ngừng nếu quá nặng)"
        ],
        "precautions": [
            "Kích ứng da tại chỗ - phổ biến khi bắt đầu, thường tự khỏi sau vài tuần",
            "Tránh mắt, miệng",
            "Bôi lên vùng da sạch, khô",
            "Dùng đều đặn hàng ngày",
            "Có thể dùng kết hợp với các thuốc khác cho rosacea"
        ],
        "pharmacokinetics": {
            "half_life": "Không áp dụng (topical)",
            "onset": "Vài tuần",
            "duration": "24 giờ (dùng 1 lần/ngày)",
            "protein_binding": "Không áp dụng (topical)",
            "clearance": "Hấp thu toàn thân tối thiểu từ dạng cream."
        },
        "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm, tránh ánh sáng",
        "black_box_warnings": None,
        "drug_interactions": {
            "major": [],
            "moderate": [],
            "minor": []
        },
        "contraindications": {
            "tuyệt_đối": [
                "Dị ứng ivermectin"
            ],
            "tương_đối": []
        },
        "pregnancy_lactation": {
            "fda_category": "C",
            "pregnancy_details": "Category C - có nguy cơ cho thai nhi. Hấp thu toàn thân tối thiểu từ dạng cream. Có thể dùng khi lợi ích > nguy cơ.",
            "lactation": {
                "safety": "Compatible",
                "details": "Hấp thu toàn thân tối thiểu từ dạng cream.",
                "recommendation": "Có thể dùng an toàn khi cho con bú."
            }
        },
        "hepatic_adjustment": {
            "mild": "Không đổi",
            "moderate": "Không đổi",
            "severe": "Không đổi",
            "notes": "Hấp thu toàn thân tối thiểu từ dạng cream. Không cần điều chỉnh liều ở suy gan."
        },
        "overdose_management": {
            "symptoms": [
                "Kích ứng da nặng"
            ],
            "antidote": "Không có antidote đặc hiệu",
            "treatment": [
                "Ngừng ngay ivermectin cream",
                "Rửa sạch vùng da",
                "Hỗ trợ và điều trị triệu chứng"
            ],
            "monitoring": "Theo dõi kích ứng da"
        },
        "reversal_agents": {
            "available": False,
            "agents": []
        },
        "administration_instructions": {
            "topical": {
                "technique": "Bôi mỏng 1 lần/ngày buổi tối lên vùng da sạch, khô. Tránh mắt, miệng.",
                "timing": "Dùng 1 lần/ngày buổi tối, đều đặn hàng ngày.",
                "notes": "Dùng cho rosacea. Bôi lên vùng da sạch, khô trước khi đi ngủ."
            }
        },
        "references": {
            "primary_sources": [
                "FDA Drug Label - Soolantra (ivermectin cream)",
                "UpToDate - Topical ivermectin for rosacea"
            ],
            "last_updated": "2025-02-05",
            "evidence_level": "A"
        }
    }
}

__all__ = ['DERMATOLOGY_DRUGS']

