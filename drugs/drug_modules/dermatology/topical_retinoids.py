"""
Dermatology Drugs - Topical Retinoids
"""
from typing import Dict, Any


TOPICAL_RETINOIDS_DRUGS: Dict[str, Dict[str, Any]] = {
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
            },
            "risk_flags": {
                "high_alert": False,
                "narrow_therapeutic_index": False,
                "bleeding_risk": False,
                "organ_toxicity": [],
                "qt_prolongation": False,
                "hepatotoxicity": False,
                "nephrotoxicity": False,
                "requires_monitoring": ["Clinical response (reduction in acne)", "Signs of skin irritation (redness, burning, dryness, peeling)", "Signs of photosensitivity", "Signs of excessive irritation (stop if too severe)"]
            },
            "guideline_tags": [
                "AAD Guidelines - Acne Treatment",
                "FDA Drug Information - Adapalene",
                "UpToDate - Acne Treatment"
            ]
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
            },
            "risk_flags": {
                "high_alert": True,
                "narrow_therapeutic_index": False,
                "bleeding_risk": False,
                "organ_toxicity": ["Teratogenicity (category X) - CRITICAL"],
                "qt_prolongation": False,
                "hepatotoxicity": False,
                "nephrotoxicity": False,
                "requires_monitoring": ["Clinical response (reduction in acne, psoriasis)", "Signs of skin irritation (redness, burning, dryness, peeling)", "Signs of photosensitivity", "Pregnancy status (contraindicated in pregnancy) - CRITICAL"]
            },
            "guideline_tags": [
                "FDA Black Box Warning - Tazarotene and Pregnancy (Category X)",
                "AAD Guidelines - Acne Treatment",
                "AAD Guidelines - Psoriasis Treatment",
                "FDA Drug Information - Tazarotene"
            ]
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
            },
            "risk_flags": {
                "high_alert": True,
                "narrow_therapeutic_index": False,
                "bleeding_risk": False,
                "organ_toxicity": ["Teratogenicity (category X) - CRITICAL"],
                "qt_prolongation": False,
                "hepatotoxicity": False,
                "nephrotoxicity": False,
                "requires_monitoring": ["Clinical response (reduction in acne) - improvement after 4-8 weeks", "Signs of skin irritation (redness, burning, dryness, peeling) - common in first few weeks", "Signs of photosensitivity (redness, burning when exposed to sunlight)", "Signs of allergic reaction (rash, itching)", "Pregnancy status (contraindicated in pregnancy) - CRITICAL"]
            },
            "guideline_tags": [
                "FDA Black Box Warning - Tretinoin and Pregnancy (Category X)",
                "AAD Guidelines - Acne Treatment",
                "FDA Drug Information - Tretinoin Topical",
                "ISMP High Alert Medications - Teratogenic Medications"
            ]
        },

}

__all__ = ['TOPICAL_RETINOIDS_DRUGS']
