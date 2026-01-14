"""
Dermatology Drugs - Topical Antifungals
"""
from typing import Dict, Any


TOPICAL_ANTIFUNGALS_DRUGS: Dict[str, Dict[str, Any]] = {
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
            },
            "risk_flags": {
                "high_alert": False,
                "narrow_therapeutic_index": False,
                "bleeding_risk": False,
                "organ_toxicity": [],
                "qt_prolongation": False,
                "hepatotoxicity": False,
                "nephrotoxicity": False,
                "requires_monitoring": ["Clinical response (reduction in fungal infection)", "Signs of skin irritation", "Signs of recurrence"]
            },
            "guideline_tags": [
                "AAD Guidelines - Fungal Skin Infections",
                "FDA Drug Information - Clotrimazole Topical",
                "UpToDate - Fungal Skin Infections"
            ]
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
            },
            "risk_flags": {
                "high_alert": False,
                "narrow_therapeutic_index": False,
                "bleeding_risk": False,
                "organ_toxicity": [],
                "qt_prolongation": False,
                "hepatotoxicity": False,
                "nephrotoxicity": False,
                "requires_monitoring": ["Clinical response (reduction in fungal infection)", "Signs of skin irritation", "Signs of recurrence"]
            },
            "guideline_tags": [
                "AAD Guidelines - Fungal Skin Infections",
                "FDA Drug Information - Econazole Topical",
                "UpToDate - Fungal Skin Infections"
            ]
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
            },
            "risk_flags": {
                "high_alert": False,
                "narrow_therapeutic_index": False,
                "bleeding_risk": False,
                "organ_toxicity": [],
                "qt_prolongation": False,
                "hepatotoxicity": False,
                "nephrotoxicity": False,
                "requires_monitoring": ["Clinical response (reduction in fungal infection, dandruff)", "Signs of skin irritation", "Signs of recurrence"]
            },
            "guideline_tags": [
                "AAD Guidelines - Fungal Skin Infections",
                "AAD Guidelines - Seborrheic Dermatitis",
                "FDA Drug Information - Ketoconazole Topical",
                "UpToDate - Fungal Skin Infections"
            ]
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
            },
            "risk_flags": {
                "high_alert": False,
                "narrow_therapeutic_index": False,
                "bleeding_risk": False,
                "organ_toxicity": [],
                "qt_prolongation": False,
                "hepatotoxicity": False,
                "nephrotoxicity": False,
                "requires_monitoring": ["Clinical response (reduction in fungal infection)", "Signs of skin irritation", "Signs of recurrence", "INR if using warfarin (rare with topical form)"]
            },
            "guideline_tags": [
                "AAD Guidelines - Fungal Skin Infections",
                "FDA Drug Information - Miconazole Topical",
                "UpToDate - Fungal Skin Infections"
            ]
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
            },
            "risk_flags": {
                "high_alert": False,
                "narrow_therapeutic_index": False,
                "bleeding_risk": False,
                "organ_toxicity": [],
                "qt_prolongation": False,
                "hepatotoxicity": False,
                "nephrotoxicity": False,
                "requires_monitoring": ["Clinical response (reduction in redness, itching, scaling)", "Signs of skin irritation (increased redness, itching, burning)", "Signs of skin infection (pus, increased redness/swelling)"]
            },
            "guideline_tags": [
                "AAD Guidelines - Fungal Skin Infections",
                "FDA Drug Information - Terbinafine Topical",
                "UpToDate - Fungal Skin Infections"
            ]
        },

}

__all__ = ['TOPICAL_ANTIFUNGALS_DRUGS']
