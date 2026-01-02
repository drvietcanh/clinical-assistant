"""
Dermatology Drugs - Topical Antibiotics
"""
from typing import Dict, Any


TOPICAL_ANTIBIOTICS_DRUGS: Dict[str, Dict[str, Any]] = {
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

}

__all__ = ['TOPICAL_ANTIBIOTICS_DRUGS']
