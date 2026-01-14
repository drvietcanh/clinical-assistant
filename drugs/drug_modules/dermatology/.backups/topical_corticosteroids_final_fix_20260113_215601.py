"""
Dermatology Drugs - Topical Corticosteroids
"""
from typing import Dict, Any


TOPICAL_CORTICOSTEROIDS_DRUGS: Dict[str, Dict[str, Any]] = {
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
            },
            "risk_flags": {
                "high_alert": False,
                "narrow_therapeutic_index": False,
                "bleeding_risk": False,
                "organ_toxicity": ["Skin atrophy (common with prolonged use)", "HPA axis suppression (if used on large areas/long-term)"],
                "qt_prolongation": False,
                "hepatotoxicity": False,
                "nephrotoxicity": False,
                "requires_monitoring": ["Clinical response", "Signs of skin atrophy", "Signs of skin infection", "HPA axis function if used on large areas/long-term"]
            },
            "guideline_tags": [
                "AAD Guidelines - Atopic Dermatitis",
                "AAD Guidelines - Contact Dermatitis",
                "FDA Drug Information - Betamethasone Topical"
            ]
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
            },
            "risk_flags": {
                "high_alert": True,
                "narrow_therapeutic_index": False,
                "bleeding_risk": False,
                "organ_toxicity": ["Skin atrophy (common with prolonged use) - CRITICAL", "HPA axis suppression (if used on large areas/long-term) - CRITICAL"],
                "qt_prolongation": False,
                "hepatotoxicity": False,
                "nephrotoxicity": False,
                "requires_monitoring": ["Clinical response (reduction in redness, swelling, itching)", "Signs of skin atrophy (thin, wrinkled skin, telangiectasia) - CRITICAL", "Signs of skin infection (pus, increased redness/swelling)", "Signs of HPA axis suppression (fatigue, hypotension, hypoglycemia) if used on large areas/long-term - CRITICAL", "Treatment area (avoid >20% body surface area)"]
            },
            "guideline_tags": [
                "AAD Guidelines - Atopic Dermatitis",
                "AAD Guidelines - Psoriasis",
                "FDA Drug Information - Clobetasol Topical",
                "ISMP High Alert Medications - Ultra-high Potency Topical Corticosteroids"
            ]
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
            "risk_flags": {
                "high_alert": False,
                "narrow_therapeutic_index": False,
                "bleeding_risk": False,
                "organ_toxicity": ["Skin atrophy (from betamethasone with prolonged use)", "Antibiotic resistance (if used long-term)"],
                "qt_prolongation": False,
                "hepatotoxicity": False,
                "nephrotoxicity": False,
                "requires_monitoring": ["Clinical response (improvement in redness, discharge, pustules)", "Signs of skin irritation or skin atrophy (if used >1-2 weeks)", "Signs of bacterial resistance (no improvement or worsening)"]
            },
            "guideline_tags": [
                "AAD Guidelines - Infected Eczema",
                "AAD Guidelines - Topical Combination Therapy",
                "FDA Drug Information - Topical Combinations"
            ],
            "hepatic_adjustment": {
                      "mild": "Không đổi",
                      "moderate": "Thận trọng, có thể giảm liều",
                      "severe": "Thận trọng, giảm liều hoặc tránh dùng",
                      "notes": "Nhiều kháng sinh chuyển hóa qua gan, cần điều chỉnh liều ở suy gan nặng."
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
            "risk_flags": {
                "high_alert": False,
                "narrow_therapeutic_index": False,
                "bleeding_risk": False,
                "organ_toxicity": [
                    "Skin atrophy (rare, only with prolonged use)",
                    "Systemic absorption (rare, only with large surface area, prolonged use)"
                ],
                "qt_prolongation": False,
                "hepatotoxicity": False,
                "nephrotoxicity": False,
                "requires_monitoring": [
                    "Clinical response (reduction in redness, swelling, itching)",
                    "Signs of skin irritation",
                    "Signs of skin infection",
                    "Signs of skin atrophy (if used long-term)"
                ]
            },
            "guideline_tags": [
                "AAD Guidelines - Atopic Dermatitis",
                "AAD Guidelines - Contact Dermatitis",
                "FDA Drug Information - Hydrocortisone Topical"
            ],
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
            "risk_flags": {
                "high_alert": False,
                "narrow_therapeutic_index": False,
                "bleeding_risk": False,
                "organ_toxicity": ["Skin atrophy (rare, from hydrocortisone with prolonged use)"],
                "qt_prolongation": False,
                "hepatotoxicity": False,
                "nephrotoxicity": False,
                "requires_monitoring": ["Clinical response (improvement in redness, itching, scaling)", "Signs of skin irritation or worsening"]
            },
            "guideline_tags": [
                "AAD Guidelines - Topical Antifungal Treatment",
                "AAD Guidelines - Topical Combination Therapy",
                "FDA Drug Information - Topical Combinations"
            ],
            "hepatic_adjustment": {
                      "mild": "Không đổi",
                      "moderate": "Thận trọng",
                      "severe": "Thận trọng, có thể giảm liều",
                      "notes": "Cần tra cứu thêm thông tin chi tiết về điều chỉnh liều ở suy gan."
                  },
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
            },
            "risk_flags": {
                "high_alert": False,
                "narrow_therapeutic_index": False,
                "bleeding_risk": False,
                "organ_toxicity": ["Skin atrophy (common with prolonged use)", "HPA axis suppression (if used on large areas/long-term)"],
                "qt_prolongation": False,
                "hepatotoxicity": False,
                "nephrotoxicity": False,
                "requires_monitoring": ["Clinical response", "Signs of skin atrophy", "Signs of skin infection"]
            },
            "guideline_tags": [
                "AAD Guidelines - Atopic Dermatitis",
                "AAD Guidelines - Contact Dermatitis",
                "FDA Drug Information - Mometasone Topical"
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
            },
            "risk_flags": {
                "high_alert": False,
                "narrow_therapeutic_index": False,
                "bleeding_risk": False,
                "organ_toxicity": ["Skin atrophy (common with prolonged use)", "HPA axis suppression (if used on large areas/long-term)"],
                "qt_prolongation": False,
                "hepatotoxicity": False,
                "nephrotoxicity": False,
                "requires_monitoring": ["Clinical response (reduction in redness, swelling, itching)", "Signs of skin atrophy (thin, wrinkled skin, telangiectasia)", "Signs of skin infection (pus, increased redness/swelling)", "Signs of HPA axis suppression (fatigue, hypotension, hypoglycemia) if used on large areas/long-term", "Treatment area (avoid >20% body surface area)"]
            },
            "guideline_tags": [
                "AAD Guidelines - Atopic Dermatitis",
                "AAD Guidelines - Psoriasis",
                "FDA Drug Information - Triamcinolone Topical"
            ]
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
            },
            "risk_flags": {
                "high_alert": False,
                "narrow_therapeutic_index": False,
                "bleeding_risk": False,
                "organ_toxicity": ["Skin atrophy (common with prolonged use)", "HPA axis suppression (if used on large areas/long-term)"],
                "qt_prolongation": False,
                "hepatotoxicity": False,
                "nephrotoxicity": False,
                "requires_monitoring": ["Clinical response", "Signs of skin atrophy", "Signs of skin infection"]
            },
            "guideline_tags": [
                "AAD Guidelines - Atopic Dermatitis",
                "AAD Guidelines - Contact Dermatitis",
                "FDA Drug Information - Triamcinolone Topical"
            ]
        },

}

__all__ = ['TOPICAL_CORTICOSTEROIDS_DRUGS']
