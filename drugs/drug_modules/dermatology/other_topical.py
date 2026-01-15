"""
Dermatology Drugs - Other Topical
"""
from typing import Dict, Any


OTHER_TOPICAL_DRUGS: Dict[str, Dict[str, Any]] = {
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
            },
            "risk_flags": {
                "high_alert": False,
                "narrow_therapeutic_index": False,
                "bleeding_risk": False,
                "organ_toxicity": ["Hypercalcemia (if used in excess or on large areas) - CRITICAL"],
                "qt_prolongation": False,
                "hepatotoxicity": False,
                "nephrotoxicity": False,
                "requires_monitoring": ["Clinical response (reduction in psoriasis)", "Signs of skin irritation", "Serum calcium (if used on large areas or long-term) - CRITICAL", "Signs of hypercalcemia: fatigue, nausea, constipation"]
            },
            "guideline_tags": [
                "AAD Guidelines - Psoriasis Treatment",
                "FDA Drug Information - Calcipotriol Topical",
                "UpToDate - Psoriasis Treatment"
            ]
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
            },
            "risk_flags": {
                "high_alert": False,
                "narrow_therapeutic_index": False,
                "bleeding_risk": False,
                "organ_toxicity": ["Hypercalcemia (if used in excess or on large areas) - CRITICAL"],
                "qt_prolongation": False,
                "hepatotoxicity": False,
                "nephrotoxicity": False,
                "requires_monitoring": ["Clinical response (reduction in psoriasis)", "Signs of skin irritation", "Serum calcium (if used on large areas or long-term) - CRITICAL", "Signs of hypercalcemia: fatigue, nausea, constipation"]
            },
            "guideline_tags": [
                "AAD Guidelines - Psoriasis Treatment",
                "FDA Drug Information - Calcitriol Topical",
                "UpToDate - Psoriasis Treatment"
            ]
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
            },
            "risk_flags": {
                "high_alert": False,
                "narrow_therapeutic_index": False,
                "bleeding_risk": False,
                "organ_toxicity": ["GI toxicity (rare, if systemic absorption occurs)", "Renal toxicity (rare, if systemic absorption occurs)"],
                "qt_prolongation": False,
                "hepatotoxicity": False,
                "nephrotoxicity": False,
                "requires_monitoring": ["Clinical response (reduction in pain, inflammation)", "Signs of skin irritation", "Signs of systemic side effects (rare): GI pain, hypertension"]
            },
            "guideline_tags": [
                "AAD Guidelines - Topical NSAIDs",
                "FDA Drug Information - Diclofenac Gel",
                "UpToDate - Topical NSAIDs for Pain"
            ]
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
            },
            "risk_flags": {
                "high_alert": False,
                "narrow_therapeutic_index": False,
                "bleeding_risk": False,
                "organ_toxicity": [],
                "qt_prolongation": False,
                "hepatotoxicity": False,
                "nephrotoxicity": False,
                "requires_monitoring": ["Clinical response (reduction in rosacea)", "Signs of skin irritation (redness, burning, dryness)", "Signs of excessive irritation (stop if too severe)"]
            },
            "guideline_tags": [
                "AAD Guidelines - Rosacea Treatment",
                "FDA Drug Information - Ivermectin Cream",
                "UpToDate - Rosacea Treatment"
            ]
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
            },
            "risk_flags": {
                "high_alert": False,
                "narrow_therapeutic_index": False,
                "bleeding_risk": False,
                "organ_toxicity": ["GI toxicity (rare, if systemic absorption occurs)", "Renal toxicity (rare, if systemic absorption occurs)"],
                "qt_prolongation": False,
                "hepatotoxicity": False,
                "nephrotoxicity": False,
                "requires_monitoring": ["Clinical response (reduction in pain, inflammation)", "Signs of skin irritation", "Signs of systemic side effects (rare): GI pain, hypertension"]
            },
            "guideline_tags": [
                "AAD Guidelines - Topical NSAIDs",
                "FDA Drug Information - Ketoprofen Gel",
                "UpToDate - Topical NSAIDs for Pain"
            ]
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
            },
            "risk_flags": {
                "high_alert": False,
                "narrow_therapeutic_index": False,
                "bleeding_risk": False,
                "organ_toxicity": [],
                "qt_prolongation": False,
                "hepatotoxicity": False,
                "nephrotoxicity": False,
                "requires_monitoring": ["Clinical response (reduction in itching, reduction in skin lesions)", "Signs of skin irritation (increased redness, itching, burning)", "Signs of secondary skin infection (pus, increased redness/swelling)", "Continued itching (may be due to allergic reaction to dead parasites, not medication)"]
            },
            "guideline_tags": [
                "CDC Guidelines - Scabies and Lice Treatment",
                "AAD Guidelines - Scabies Treatment",
                "FDA Drug Information - Permethrin Topical",
                "UpToDate - Scabies and Lice Treatment"
            ]
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
                "FDA Black Box Warning - Pimecrolimus Topical and Skin Cancer",
                "FDA Black Box Warning - Pimecrolimus Topical and Age Restriction (<2 years)",
                "FDA Drug Information - Pimecrolimus Topical"
            ]
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
            },
            "risk_flags": {
                "high_alert": False,
                "narrow_therapeutic_index": False,
                "bleeding_risk": False,
                "organ_toxicity": ["Salicylate toxicity (if used on large areas or high concentrations) - rare but dangerous"],
                "qt_prolongation": False,
                "hepatotoxicity": False,
                "nephrotoxicity": False,
                "requires_monitoring": ["Clinical response (reduction in warts, acne, psoriasis)", "Signs of skin irritation", "Signs of salicylate toxicity (if used on large areas): tinnitus, nausea, rapid breathing, altered consciousness"]
            },
            "guideline_tags": [
                "AAD Guidelines - Warts Treatment",
                "AAD Guidelines - Acne Treatment",
                "FDA Drug Information - Salicylic Acid Topical",
                "UpToDate - Warts and Acne Treatment"
            ]
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
    "Capsaicin": {
        "group": "Dermatology - Topical Analgesic (TRPV1 Agonist)",
        "vietnamese_name": "Capsaicin, Zostrix, Capzasin",
        "administration": ["Topical"],
        "indications": [
            "Đau thần kinh ngoại biên (postherpetic neuralgia, diabetic neuropathy)",
            "Đau cơ xương khớp tại chỗ",
            "Đau khớp (osteoarthritis, rheumatoid arthritis)",
            "Đau cơ (fibromyalgia - off-label)"
        ],
        "contraindications": {
            "tuyệt_đối": [
                "Dị ứng capsaicin hoặc ớt",
                "Vùng da bị tổn thương, loét, hoặc viêm",
                "Trẻ em <18 tuổi (cho một số chỉ định)"
            ],
            "tương_đối": [
                "Da nhạy cảm - thận trọng",
                "Phụ nữ có thai - thận trọng",
                "Đang cho con bú - thận trọng"
            ]
        },
        "dosage": {
            "adult_topical": "Bôi mỏng 3-4 lần/ngày lên vùng da bị ảnh hưởng",
            "adult_patch": "Patch 8%: dán 1 lần/ngày, giữ 30-60 phút (cho postherpetic neuralgia)",
            "notes": "Capsaicin gây cảm giác nóng, rát ban đầu (có thể kéo dài vài tuần). Tác dụng giảm đau xuất hiện sau vài tuần sử dụng. Tránh tiếp xúc với mắt, niêm mạc."
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "Không đổi",
            "under_30": "Không đổi",
            "notes": "Hấp thu toàn thân tối thiểu từ dạng tại chỗ. Không cần điều chỉnh liều ở suy thận."
        },
        "side_effects": [
            "Cảm giác nóng, rát tại chỗ (phổ biến, có thể kéo dài vài tuần)",
            "Đỏ da, kích ứng da",
            "Ngứa",
            "Ho, hắt hơi (nếu hít phải)",
            "Kích ứng mắt (nếu dính vào mắt)"
        ],
        "interactions": [
            "Không có tương tác đáng kể khi dùng tại chỗ"
        ],
        "pregnancy": "C",
        "mechanism_of_action": "Capsaicin là chất chiết xuất từ ớt, kích thích thụ thể TRPV1 (Transient Receptor Potential Vanilloid 1) trên các sợi thần kinh cảm giác. Ban đầu gây cảm giác nóng, rát (do giải phóng substance P và các chất dẫn truyền đau khác). Sau khi sử dụng kéo dài, capsaicin làm cạn kiệt substance P và làm giảm độ nhạy cảm của các sợi thần kinh cảm giác, dẫn đến giảm đau thần kinh. Được dùng cho đau thần kinh ngoại biên (đau sau zona, đau thần kinh do tiểu đường) và đau cơ xương khớp tại chỗ.",
        "monitoring": [
            "Đáp ứng điều trị: giảm đau (sau vài tuần sử dụng)",
            "Kích ứng da tại chỗ (đỏ, rát, ngứa)",
            "Dấu hiệu dị ứng"
        ],
        "precautions": [
            "Cảm giác nóng, rát ban đầu - phổ biến, có thể kéo dài vài tuần, thường tự khỏi",
            "Tránh tiếp xúc với mắt, niêm mạc - gây kích ứng nặng",
            "Rửa tay kỹ sau khi bôi",
            "Tránh dùng trên vùng da bị tổn thương, loét, hoặc viêm",
            "Tác dụng giảm đau xuất hiện sau vài tuần sử dụng - cần kiên nhẫn",
            "Có thể gây ho, hắt hơi nếu hít phải - thận trọng khi bôi gần mũi, miệng"
        ],
        "pharmacokinetics": {
            "half_life": "Không áp dụng (topical)",
            "onset": "Cảm giác nóng, rát: ngay lập tức; Tác dụng giảm đau: vài tuần",
            "duration": "4-6 giờ (dùng 3-4 lần/ngày)",
            "protein_binding": "Không áp dụng (topical)",
            "clearance": "Hấp thu toàn thân tối thiểu từ dạng tại chỗ."
        },
        "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm, tránh ánh sáng. Để xa tầm tay trẻ em.",
        "black_box_warnings": "Tránh tiếp xúc với mắt, niêm mạc - gây kích ứng nặng. Cảm giác nóng, rát ban đầu là bình thường và thường tự khỏi sau vài tuần.",
        "drug_interactions": {
            "major": [],
            "moderate": [],
            "minor": []
        },
        "pregnancy_lactation": {
            "fda_category": "C",
            "pregnancy_details": "Category C - có nguy cơ cho thai nhi. Hấp thu toàn thân tối thiểu từ dạng tại chỗ.",
            "lactation": {
                "safety": "Caution",
                "details": "Hấp thu toàn thân tối thiểu từ dạng tại chỗ. Có thể gây kích ứng nếu trẻ tiếp xúc với vùng da bôi thuốc.",
                "recommendation": "Thận trọng khi cho con bú. Tránh để trẻ tiếp xúc với vùng da bôi thuốc."
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
                "Bỏng da (nếu dùng nồng độ cao hoặc diện rộng)",
                "Kích ứng mắt nặng (nếu dính vào mắt)"
            ],
            "antidote": "Không có antidote đặc hiệu",
            "treatment": [
                "Rửa sạch vùng da bằng xà phòng và nước",
                "Nếu dính vào mắt: rửa mắt bằng nước sạch nhiều lần, đi khám bác sĩ",
                "Chườm lạnh để giảm cảm giác nóng, rát",
                "Điều trị hỗ trợ và điều trị triệu chứng"
            ],
            "monitoring": "Theo dõi vùng da bị ảnh hưởng, dấu hiệu kích ứng mắt nếu dính vào mắt."
        },
        "reversal_agents": {
            "available": False,
            "agents": []
        },
        "administration_instructions": {
            "topical": {
                "technique": "Rửa sạch và lau khô vùng da. Bôi mỏng lên vùng da bị ảnh hưởng, tránh vùng da lành. Rửa tay kỹ sau khi bôi. Tránh tiếp xúc với mắt, niêm mạc.",
                "timing": "3-4 lần/ngày. Tác dụng giảm đau xuất hiện sau vài tuần sử dụng."
            },
            "patch": {
                "technique": "Dán patch lên vùng da bị ảnh hưởng, giữ 30-60 phút. Rửa sạch vùng da sau khi tháo patch.",
                "timing": "1 lần/ngày (cho postherpetic neuralgia)"
            }
        },
        "references": {
            "primary_sources": [
                "FDA Drug Label - Capsaicin (Zostrix, Capzasin)",
                "UpToDate - Topical analgesics: Drug information",
                "AAN Guidelines - Neuropathic Pain Treatment"
            ],
            "last_updated": "2025-02-18",
            "evidence_level": "High - FDA-approved, extensive clinical data"
        },
        "risk_flags": {
            "high_alert": False,
            "narrow_therapeutic_index": False,
            "bleeding_risk": False,
            "organ_toxicity": ["skin"],
            "qt_prolongation": False,
            "hepatotoxicity": False,
            "nephrotoxicity": False,
            "requires_monitoring": ["Skin irritation", "Clinical response"]
        },
        "guideline_tags": [
            "FDA Drug Information",
            "UpToDate Drug Information",
            "AAN Guidelines - Neuropathic Pain Treatment"
        ]
    },
    "Menthol": {
        "group": "Dermatology - Topical Analgesic (Cooling Agent)",
        "vietnamese_name": "Menthol, Mentholatum",
        "administration": ["Topical"],
        "indications": [
            "Đau cơ xương khớp tại chỗ",
            "Đau khớp (osteoarthritis)",
            "Đau cơ (muscle pain)",
            "Ngứa da (itch relief)",
            "Nghẹt mũi (nasal congestion - dạng xịt mũi)"
        ],
        "contraindications": {
            "tuyệt_đối": [
                "Dị ứng menthol hoặc bạc hà",
                "Vùng da bị tổn thương, loét, hoặc viêm nặng",
                "Trẻ em <2 tuổi (cho một số chỉ định)"
            ],
            "tương_đối": [
                "Da nhạy cảm - thận trọng",
                "Phụ nữ có thai - thận trọng",
                "Đang cho con bú - thận trọng"
            ]
        },
        "dosage": {
            "adult_topical": "Bôi mỏng 3-4 lần/ngày lên vùng da bị ảnh hưởng",
            "adult_nasal": "Xịt mũi 2-3 lần/ngày (cho nghẹt mũi)",
            "notes": "Menthol gây cảm giác mát lạnh, giảm đau tạm thời. Tác dụng ngắn (1-2 giờ). Tránh tiếp xúc với mắt, niêm mạc."
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "Không đổi",
            "under_30": "Không đổi",
            "notes": "Hấp thu toàn thân tối thiểu từ dạng tại chỗ. Không cần điều chỉnh liều ở suy thận."
        },
        "side_effects": [
            "Kích ứng da tại chỗ (đỏ, rát) - hiếm",
            "Cảm giác mát lạnh quá mức",
            "Kích ứng mắt (nếu dính vào mắt)",
            "Kích ứng mũi, họng (nếu dùng dạng xịt mũi)"
        ],
        "interactions": [
            "Không có tương tác đáng kể khi dùng tại chỗ"
        ],
        "pregnancy": "C",
        "mechanism_of_action": "Menthol là chất chiết xuất từ bạc hà, kích thích thụ thể TRPM8 (Transient Receptor Potential Melastatin 8) trên các sợi thần kinh cảm giác. Gây cảm giác mát lạnh, làm giảm cảm giác đau và ngứa. Menthol cũng có tác dụng gây tê nhẹ tại chỗ. Được dùng cho đau cơ xương khớp tại chỗ, đau khớp, đau cơ, và ngứa da. Dạng xịt mũi: gây cảm giác mát lạnh, giảm nghẹt mũi tạm thời.",
        "monitoring": [
            "Đáp ứng điều trị: giảm đau, giảm ngứa",
            "Kích ứng da tại chỗ (đỏ, rát)",
            "Dấu hiệu dị ứng"
        ],
        "precautions": [
            "Tránh tiếp xúc với mắt, niêm mạc - gây kích ứng",
            "Rửa tay kỹ sau khi bôi",
            "Tránh dùng trên vùng da bị tổn thương, loét, hoặc viêm nặng",
            "Tác dụng ngắn (1-2 giờ) - có thể cần bôi lại nhiều lần",
            "Cảm giác mát lạnh là bình thường - không phải tác dụng phụ"
        ],
        "pharmacokinetics": {
            "half_life": "Không áp dụng (topical)",
            "onset": "Ngay lập tức (cảm giác mát lạnh)",
            "duration": "1-2 giờ",
            "protein_binding": "Không áp dụng (topical)",
            "clearance": "Hấp thu toàn thân tối thiểu từ dạng tại chỗ."
        },
        "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm, tránh ánh sáng. Để xa tầm tay trẻ em.",
        "black_box_warnings": "Tránh tiếp xúc với mắt, niêm mạc - gây kích ứng. Không dùng cho trẻ em <2 tuổi (cho một số chỉ định).",
        "drug_interactions": {
            "major": [],
            "moderate": [],
            "minor": []
        },
        "pregnancy_lactation": {
            "fda_category": "C",
            "pregnancy_details": "Category C - có nguy cơ cho thai nhi. Hấp thu toàn thân tối thiểu từ dạng tại chỗ.",
            "lactation": {
                "safety": "Caution",
                "details": "Hấp thu toàn thân tối thiểu từ dạng tại chỗ. Có thể gây kích ứng nếu trẻ tiếp xúc với vùng da bôi thuốc.",
                "recommendation": "Thận trọng khi cho con bú. Tránh để trẻ tiếp xúc với vùng da bôi thuốc."
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
                "Kích ứng mắt nặng (nếu dính vào mắt)",
                "Kích ứng mũi, họng nặng (nếu dùng dạng xịt mũi quá nhiều)"
            ],
            "antidote": "Không có antidote đặc hiệu",
            "treatment": [
                "Rửa sạch vùng da bằng xà phòng và nước",
                "Nếu dính vào mắt: rửa mắt bằng nước sạch nhiều lần, đi khám bác sĩ",
                "Chườm lạnh để giảm kích ứng",
                "Điều trị hỗ trợ và điều trị triệu chứng"
            ],
            "monitoring": "Theo dõi vùng da bị ảnh hưởng, dấu hiệu kích ứng mắt nếu dính vào mắt."
        },
        "reversal_agents": {
            "available": False,
            "agents": []
        },
        "administration_instructions": {
            "topical": {
                "technique": "Rửa sạch và lau khô vùng da. Bôi mỏng lên vùng da bị ảnh hưởng, tránh vùng da lành. Rửa tay kỹ sau khi bôi. Tránh tiếp xúc với mắt, niêm mạc.",
                "timing": "3-4 lần/ngày. Tác dụng ngắn (1-2 giờ)."
            },
            "nasal": {
                "technique": "Xịt vào mỗi lỗ mũi, hít nhẹ. Tránh xịt quá nhiều.",
                "timing": "2-3 lần/ngày (cho nghẹt mũi)"
            }
        },
        "references": {
            "primary_sources": [
                "FDA Drug Label - Menthol (Mentholatum)",
                "UpToDate - Topical analgesics: Drug information"
            ],
            "last_updated": "2025-02-18",
            "evidence_level": "Moderate - FDA-approved, limited clinical data"
        },
        "risk_flags": {
            "high_alert": False,
            "narrow_therapeutic_index": False,
            "bleeding_risk": False,
            "organ_toxicity": ["skin"],
            "qt_prolongation": False,
            "hepatotoxicity": False,
            "nephrotoxicity": False,
            "requires_monitoring": ["Skin irritation", "Clinical response"]
        },
        "guideline_tags": [
            "FDA Drug Information",
            "UpToDate Drug Information"
        ]
    },
    "Livmarli": {
        "group": "FDA Approved 9/29/2021",
        "vietnamese_name": "Maralixibat, Livmarli",
        "administration": ["PO"],
        "indications": [
            "Ngứa do ứ mật (cholestatic pruritus) ở bệnh nhân hội chứng Alagille",
            "Điều trị ngứa liên quan đến bệnh gan ứ mật ở trẻ em từ 3 tháng tuổi trở lên"
        ],
        "contraindications": {
            "tuyệt_đối": [
                "Dị ứng maralixibat hoặc bất kỳ thành phần nào"
            ],
            "tương_đối": [
                "Tắc nghẽn đường mật hoàn toàn - thận trọng",
                "Suy gan nặng - thận trọng",
                "Rối loạn hấp thu mỡ nặng - thận trọng"
            ]
        },
        "dosage": {
            "pediatric_3mo_12mo": "380 mcg/kg PO x 1 lần/ngày, tăng dần lên 380 mcg/kg x 2 lần/ngày nếu dung nạp",
            "pediatric_1yr_18yr": "380 mcg/kg PO x 1 lần/ngày, tăng dần lên 380 mcg/kg x 2 lần/ngày nếu dung nạp (tối đa 10.5mg x 2 lần/ngày)",
            "adult": "10.5mg PO x 2 lần/ngày (dựa trên cân nặng)",
            "notes": "Uống với thức ăn để giảm tác dụng phụ đường tiêu hóa. Bắt đầu với liều thấp, tăng dần theo đáp ứng và dung nạp. FDA phê duyệt 9/29/2021 cho bệnh nhân từ 3 tháng tuổi trở lên."
        },
        "renal_adjustment": {
            "normal": "Không cần chỉnh liều",
            "30_60": "Thận trọng, không cần chỉnh liều",
            "under_30": "Thận trọng, dữ liệu hạn chế"
        },
        "side_effects": [
            "Tiêu chảy - rất phổ biến (có thể nặng)",
            "Đau bụng - phổ biến",
            "Nôn - phổ biến",
            "Buồn nôn - phổ biến",
            "Giảm cân - phổ biến",
            "Mệt mỏi - phổ biến",
            "Đau đầu - phổ biến",
            "Tăng men gan (ALT, AST) - phổ biến",
            "Giảm hấp thu vitamin tan trong dầu (A, D, E, K) - do giảm hấp thu mỡ",
            "Phát ban - không phổ biến",
            "Ngứa - không phổ biến"
        ],
        "interactions": [
            "Cholestyramine, colestipol: giảm hấp thu maralixibat - dùng cách xa ít nhất 4 giờ",
            "Vitamin tan trong dầu (A, D, E, K): giảm hấp thu - cần bổ sung",
            "Thuốc hấp thu phụ thuộc mỡ: có thể giảm hấp thu"
        ],
        "pregnancy": "C",
        "mechanism_of_action": "Maralixibat là chất ức chế vận chuyển acid mật ở hồi tràng (IBAT - ileal bile acid transporter). Ức chế ASBT (apical sodium-dependent bile acid transporter) ở hồi tràng, ngăn chặn tái hấp thu acid mật từ ruột vào máu. Dẫn đến: (1) Giảm nồng độ acid mật trong huyết thanh, (2) Giảm ngứa do ứ mật (cholestatic pruritus), (3) Tăng thải trừ acid mật qua phân. Được dùng cho ngứa do ứ mật ở bệnh nhân hội chứng Alagille. ĐẶC ĐIỂM: (1) IBAT inhibitor, (2) Giảm ngứa do ứ mật hiệu quả, (3) Tác dụng phụ đường tiêu hóa phổ biến (tiêu chảy, đau bụng, nôn), (4) Có thể gây giảm hấp thu vitamin tan trong dầu, (5) FDA phê duyệt 9/29/2021 cho bệnh nhân từ 3 tháng tuổi trở lên.",
        "monitoring": [
            "Đáp ứng điều trị: giảm ngứa (đánh giá bằng thang điểm ngứa)",
            "Tác dụng phụ đường tiêu hóa: tiêu chảy, đau bụng, nôn - QUAN TRỌNG",
            "Cân nặng (đặc biệt ở trẻ em) - giảm cân phổ biến",
            "Chức năng gan: ALT, AST, bilirubin (tăng men gan phổ biến)",
            "Vitamin tan trong dầu: vitamin A, D, E, K (giảm hấp thu)",
            "Dấu hiệu mất nước (nếu tiêu chảy nặng)",
            "Dấu hiệu tắc nghẽn đường mật"
        ],
        "precautions": [
            "TIÊU CHẢY - rất phổ biến, có thể nặng. Có thể cần giảm liều hoặc ngừng tạm thời nếu tiêu chảy nặng.",
            "GIẢM HẤP THU VITAMIN TAN TRONG DẦU - cần bổ sung vitamin A, D, E, K định kỳ",
            "GIẢM CÂN - phổ biến, đặc biệt ở trẻ em. Theo dõi cân nặng chặt chẽ.",
            "Tăng men gan - phổ biến. Theo dõi chức năng gan định kỳ.",
            "Uống với thức ăn để giảm tác dụng phụ đường tiêu hóa",
            "Bắt đầu với liều thấp, tăng dần theo đáp ứng và dung nạp",
            "Thận trọng ở bệnh nhân tắc nghẽn đường mật hoàn toàn",
            "Thận trọng ở bệnh nhân suy gan nặng",
            "Dùng cách xa cholestyramine, colestipol ít nhất 4 giờ"
        ],
        "pharmacokinetics": {
            "half_life": "Khoảng 10-15 giờ",
            "onset": "Vài tuần (tác dụng giảm ngứa)",
            "duration": "12 giờ (dùng 2 lần/ngày)",
            "protein_binding": ">99%",
            "metabolism": "Chuyển hóa tối thiểu, chủ yếu thải trừ nguyên dạng",
            "clearance": "Thải trừ chủ yếu qua phân (không hấp thu), một phần qua nước tiểu"
        },
        "storage": "Bảo quản ở nhiệt độ phòng (20-25°C), tránh ẩm. Bảo quản trong hộp kín gốc. Để xa tầm tay trẻ em.",
        "black_box_warnings": "Không có black box warning. Tuy nhiên, cần cảnh báo về: (1) Tiêu chảy có thể nặng và cần điều trị, (2) Giảm hấp thu vitamin tan trong dầu cần bổ sung, (3) Giảm cân phổ biến, đặc biệt ở trẻ em.",
        "drug_interactions": {
            "major": [],
            "moderate": [
                {
                    "drug": "Cholestyramine, Colestipol",
                    "mechanism": "Giảm hấp thu maralixibat",
                    "effect": "Giảm hiệu quả điều trị",
                    "management": "Dùng cách xa ít nhất 4 giờ. Nếu có thể, tránh dùng cùng."
                },
                {
                    "drug": "Vitamin tan trong dầu (A, D, E, K)",
                    "mechanism": "Maralixibat giảm hấp thu mỡ, dẫn đến giảm hấp thu vitamin tan trong dầu",
                    "effect": "Giảm nồng độ vitamin tan trong dầu, có thể gây thiếu hụt",
                    "management": "Bổ sung vitamin tan trong dầu định kỳ. Theo dõi nồng độ vitamin."
                }
            ],
            "minor": [
                {
                    "drug": "Thuốc hấp thu phụ thuộc mỡ",
                    "mechanism": "Maralixibat giảm hấp thu mỡ",
                    "effect": "Có thể giảm hấp thu các thuốc hấp thu phụ thuộc mỡ",
                    "management": "Thận trọng. Có thể cần điều chỉnh liều hoặc thời điểm dùng."
                }
            ]
        },
        "contraindications_detail": {
            "tuyệt_đối": [
                "Dị ứng maralixibat hoặc bất kỳ thành phần nào"
            ],
            "tương_đối": [
                "Tắc nghẽn đường mật hoàn toàn - thận trọng, có thể không hiệu quả",
                "Suy gan nặng - thận trọng, tăng nguy cơ tác dụng phụ",
                "Rối loạn hấp thu mỡ nặng - thận trọng, có thể làm nặng thêm",
                "Trẻ em <3 tháng tuổi - chưa có dữ liệu an toàn"
            ]
        },
        "pregnancy_lactation": {
            "fda_category": "C",
            "pregnancy_details": "Category C - có nguy cơ cho thai nhi. Không có nghiên cứu đầy đủ trên phụ nữ có thai. Maralixibat có thể ảnh hưởng đến hấp thu vitamin tan trong dầu, có thể ảnh hưởng đến sự phát triển thai nhi. Có thể dùng khi lợi ích vượt quá nguy cơ.",
            "lactation": {
                "safety": "Unknown",
                "details": "Chưa biết maralixibat có bài tiết vào sữa mẹ hay không. Maralixibat hấp thu tối thiểu vào máu, nhưng không có dữ liệu về bài tiết vào sữa mẹ.",
                "recommendation": "Thận trọng khi cho con bú. Cân nhắc ngừng cho con bú hoặc ngừng thuốc. Nếu dùng, theo dõi trẻ sơ sinh về dấu hiệu tác dụng phụ."
            }
        },
        "hepatic_adjustment": {
            "mild": "Không đổi",
            "moderate": "Thận trọng, không cần chỉnh liều",
            "severe": "Thận trọng, có thể cần giảm liều hoặc tránh dùng",
            "notes": "Maralixibat chuyển hóa tối thiểu. Tuy nhiên, ở bệnh nhân suy gan nặng, tăng nguy cơ tác dụng phụ và có thể không hiệu quả. Theo dõi chặt chẽ."
        },
        "overdose_management": {
            "symptoms": [
                "Tiêu chảy nặng",
                "Đau bụng nặng",
                "Nôn nhiều",
                "Mất nước",
                "Rối loạn điện giải"
            ],
            "antidote": "Không có antidote đặc hiệu",
            "treatment": [
                "Ngừng ngay maralixibat",
                "Điều trị hỗ trợ: bù nước và điện giải (truyền dịch nếu cần)",
                "Theo dõi dấu hiệu sinh tồn",
                "Theo dõi cân bằng nước và điện giải",
                "Điều trị triệu chứng (giảm đau nếu cần)"
            ],
            "monitoring": "Theo dõi dấu hiệu sinh tồn, cân bằng nước và điện giải, chức năng gan cho đến khi hồi phục."
        },
        "reversal_agents": {
            "available": False,
            "agents": []
        },
        "administration_instructions": {
            "oral": {
                "with_food": "Uống với thức ăn để giảm tác dụng phụ đường tiêu hóa (tiêu chảy, đau bụng, nôn)",
                "timing": "Uống 2 lần/ngày với bữa ăn. Bắt đầu với liều thấp (1 lần/ngày), tăng dần lên 2 lần/ngày nếu dung nạp.",
                "notes": "QUAN TRỌNG: (1) Uống với thức ăn, (2) Bắt đầu với liều thấp, tăng dần, (3) Nếu tiêu chảy nặng, có thể cần giảm liều hoặc ngừng tạm thời, (4) Bổ sung vitamin tan trong dầu định kỳ, (5) Theo dõi cân nặng chặt chẽ, đặc biệt ở trẻ em."
            }
        },
        "references": {
            "primary_sources": [
                "FDA Drug Label - Maralixibat (Livmarli)",
                "FDA Approval Date: 9/29/2021",
                "FDA-approved use: To treat cholestatic pruritus associated with Alagille syndrome",
                "UpToDate - Maralixibat: Drug information",
                "Lexicomp - Maralixibat monograph"
            ],
            "last_updated": "2025-02-18",
            "evidence_level": "A - FDA-approved 9/29/2021, dựa trên dữ liệu lâm sàng từ các thử nghiệm lâm sàng"
        },
        "risk_flags": {
            "high_alert": False,
            "narrow_therapeutic_index": False,
            "bleeding_risk": False,
            "organ_toxicity": ["Hepatotoxicity (elevated liver enzymes) - common"],
            "qt_prolongation": False,
            "hepatotoxicity": True,
            "nephrotoxicity": False,
            "requires_monitoring": ["Clinical response (reduction in pruritus)", "GI side effects (diarrhea, abdominal pain, vomiting) - CRITICAL", "Weight (especially in children) - CRITICAL", "Liver function (ALT, AST, bilirubin)", "Fat-soluble vitamins (A, D, E, K)", "Signs of dehydration", "Signs of bile duct obstruction"]
        },
        "guideline_tags": [
            "FDA Drug Information - Maralixibat (Livmarli)",
            "UpToDate - Cholestatic Pruritus Treatment",
            "AASLD Guidelines - Cholestatic Liver Disease"
        ],
        "last_updated": "2025-02-18"
    },
    "Korsuva": {
        "group": "FDA Approved 8/23/2021",
        "vietnamese_name": "Difelikefalin, Korsuva",
        "administration": ["IV"],
        "indications": [
            "Ngứa trung bình đến nặng liên quan đến bệnh thận mạn tính (CKD) ở bệnh nhân đang lọc máu",
            "Điều trị ngứa ở bệnh nhân CKD giai đoạn 4-5 đang lọc máu"
        ],
        "contraindications": {
            "tuyệt_đối": [
                "Dị ứng difelikefalin hoặc bất kỳ thành phần nào"
            ],
            "tương_đối": [
                "Bệnh nhân không lọc máu - chưa được nghiên cứu",
                "Suy gan nặng - thận trọng",
                "Suy thận không lọc máu - thận trọng"
            ]
        },
        "dosage": {
            "adult_iv": "0.5 mcg/kg IV x 1 lần/ngày vào cuối mỗi buổi lọc máu",
            "notes": "Truyền tĩnh mạch trong 30 giây vào cuối mỗi buổi lọc máu. Chỉ dùng cho bệnh nhân đang lọc máu. FDA phê duyệt 8/23/2021."
        },
        "renal_adjustment": {
            "normal": "Không áp dụng (chỉ dùng cho bệnh nhân lọc máu)",
            "30_60": "Không áp dụng (chỉ dùng cho bệnh nhân lọc máu)",
            "under_30": "Không áp dụng (chỉ dùng cho bệnh nhân lọc máu)"
        },
        "side_effects": [
            "Buồn nôn - phổ biến",
            "Chóng mặt - phổ biến",
            "Mệt mỏi - phổ biến",
            "Ngủ gà - phổ biến",
            "Đau đầu - phổ biến",
            "Táo bón - phổ biến",
            "Ngứa - không phổ biến (có thể tăng tạm thời)",
            "Phản ứng tại chỗ tiêm - không phổ biến",
            "Hạ huyết áp - không phổ biến",
            "Tăng men gan - không phổ biến"
        ],
        "interactions": [
            "Thuốc an thần, thuốc ngủ: tăng tác dụng an thần",
            "Rượu: tăng tác dụng an thần",
            "Thuốc ức chế CNS: tăng tác dụng ức chế CNS"
        ],
        "pregnancy": "C",
        "mechanism_of_action": "Difelikefalin là chất chủ vận thụ thể kappa-opioid (KOR - kappa-opioid receptor) chọn lọc. Kích thích thụ thể kappa-opioid ở hệ thần kinh trung ương và ngoại biên, dẫn đến: (1) Ức chế dẫn truyền tín hiệu ngứa, (2) Giảm cảm giác ngứa, (3) Tác dụng giảm đau nhẹ. Khác với mu-opioid agonists (như morphine), kappa-opioid agonists không gây nghiện và ít tác dụng phụ hơn. Được dùng cho ngứa trung bình đến nặng liên quan đến bệnh thận mạn tính ở bệnh nhân đang lọc máu. ĐẶC ĐIỂM: (1) Kappa-opioid receptor agonist, (2) Chỉ dùng cho bệnh nhân đang lọc máu, (3) Truyền IV vào cuối mỗi buổi lọc máu, (4) Tác dụng an thần phổ biến, (5) FDA phê duyệt 8/23/2021.",
        "monitoring": [
            "Đáp ứng điều trị: giảm ngứa (đánh giá bằng thang điểm ngứa)",
            "Tác dụng an thần: buồn ngủ, mệt mỏi - QUAN TRỌNG",
            "Chức năng gan: ALT, AST (tăng men gan không phổ biến)",
            "Huyết áp (hạ huyết áp không phổ biến)",
            "Dấu hiệu quá liều: buồn ngủ nặng, ức chế hô hấp (hiếm)"
        ],
        "precautions": [
            "TÁC DỤNG AN THẦN - phổ biến. Thận trọng khi lái xe hoặc vận hành máy móc.",
            "CHỈ DÙNG CHO BỆNH NHÂN ĐANG LỌC MÁU - chưa được nghiên cứu ở bệnh nhân không lọc máu",
            "Truyền IV trong 30 giây vào cuối mỗi buổi lọc máu",
            "Thận trọng với thuốc an thần, thuốc ngủ, rượu (tăng tác dụng an thần)",
            "Thận trọng ở bệnh nhân suy gan nặng",
            "Có thể gây buồn nôn, chóng mặt - phổ biến"
        ],
        "pharmacokinetics": {
            "half_life": "Khoảng 37-43 giờ",
            "onset": "Vài giờ đến vài ngày (tác dụng giảm ngứa)",
            "duration": "24 giờ (dùng 1 lần/ngày sau lọc máu)",
            "protein_binding": "Khoảng 91-93%",
            "metabolism": "Chuyển hóa qua gan (CYP3A4, CYP2C8)",
            "clearance": "Thải trừ chủ yếu qua gan, một phần qua thận. Được loại bỏ một phần qua lọc máu."
        },
        "storage": "Bảo quản ở nhiệt độ phòng (20-25°C), tránh đông lạnh. Bảo quản trong hộp kín gốc. Để xa tầm tay trẻ em.",
        "black_box_warnings": "Không có black box warning. Tuy nhiên, cần cảnh báo về: (1) Tác dụng an thần phổ biến, cần thận trọng khi lái xe, (2) Chỉ dùng cho bệnh nhân đang lọc máu.",
        "drug_interactions": {
            "major": [
                {
                    "drug": "Thuốc an thần, thuốc ngủ, benzodiazepine",
                    "mechanism": "Tăng ức chế hệ thần kinh trung ương",
                    "effect": "Tăng tác dụng an thần, tăng nguy cơ buồn ngủ nặng",
                    "management": "Thận trọng. Có thể cần giảm liều thuốc an thần. Theo dõi dấu hiệu an thần nặng."
                },
                {
                    "drug": "Rượu",
                    "mechanism": "Tăng ức chế hệ thần kinh trung ương",
                    "effect": "Tăng tác dụng an thần",
                    "management": "Tránh uống rượu khi dùng difelikefalin."
                }
            ],
            "moderate": [
                {
                    "drug": "CYP3A4 inhibitors (ketoconazole, itraconazole, ritonavir)",
                    "mechanism": "Ức chế CYP3A4, tăng nồng độ difelikefalin",
                    "effect": "Tăng nồng độ difelikefalin, tăng nguy cơ tác dụng phụ",
                    "management": "Thận trọng. Có thể cần giảm liều difelikefalin."
                }
            ],
            "minor": []
        },
        "contraindications_detail": {
            "tuyệt_đối": [
                "Dị ứng difelikefalin hoặc bất kỳ thành phần nào"
            ],
            "tương_đối": [
                "Bệnh nhân không lọc máu - chưa được nghiên cứu, không khuyến cáo",
                "Suy gan nặng - thận trọng, có thể tăng nồng độ",
                "Suy thận không lọc máu - thận trọng, chưa được nghiên cứu",
                "Tiền sử lạm dụng chất - thận trọng"
            ]
        },
        "pregnancy_lactation": {
            "fda_category": "C",
            "pregnancy_details": "Category C - có nguy cơ cho thai nhi. Không có nghiên cứu đầy đủ trên phụ nữ có thai. Difelikefalin có thể ảnh hưởng đến thai nhi. Có thể dùng khi lợi ích vượt quá nguy cơ.",
            "lactation": {
                "safety": "Unknown",
                "details": "Chưa biết difelikefalin có bài tiết vào sữa mẹ hay không. Difelikefalin có thể bài tiết vào sữa mẹ dựa trên tính chất dược động học.",
                "recommendation": "Thận trọng khi cho con bú. Cân nhắc ngừng cho con bú hoặc ngừng thuốc. Nếu dùng, theo dõi trẻ sơ sinh về dấu hiệu an thần."
            }
        },
        "hepatic_adjustment": {
            "mild": "Không đổi",
            "moderate": "Thận trọng, không cần chỉnh liều",
            "severe": "Thận trọng, có thể cần giảm liều",
            "notes": "Difelikefalin chuyển hóa qua gan (CYP3A4, CYP2C8). Suy gan có thể làm giảm chuyển hóa, tăng nồng độ và độc tính. Theo dõi chặt chẽ."
        },
        "overdose_management": {
            "symptoms": [
                "Buồn ngủ nặng",
                "Ức chế hô hấp (hiếm)",
                "Chóng mặt nặng",
                "Buồn nôn nặng",
                "Hạ huyết áp"
            ],
            "antidote": "Naloxone có thể đảo ngược một phần tác dụng (do tác động lên opioid receptors)",
            "treatment": [
                "Ngừng ngay difelikefalin",
                "Nếu ức chế hô hấp: naloxone (có thể cần liều cao hơn so với mu-opioid)",
                "Hỗ trợ hô hấp nếu cần",
                "Hỗ trợ huyết động nếu hạ huyết áp",
                "Theo dõi dấu hiệu sinh tồn",
                "Điều trị hỗ trợ và điều trị triệu chứng"
            ],
            "monitoring": "Theo dõi dấu hiệu sinh tồn, mức độ ý thức, hô hấp, huyết áp cho đến khi hồi phục."
        },
        "reversal_agents": {
            "available": True,
            "agents": [
                {
                    "name": "Naloxone",
                    "indication": "Đảo ngược tác dụng ức chế hô hấp (nếu có)",
                    "dose": "0.4-2mg IV, có thể lặp lại mỗi 2-3 phút",
                    "notes": "Naloxone có thể đảo ngược một phần tác dụng của difelikefalin do tác động lên opioid receptors, nhưng có thể cần liều cao hơn so với mu-opioid agonists."
                }
            ]
        },
        "administration_instructions": {
            "iv": {
                "reconstitution": "Dùng trực tiếp từ lọ, không cần pha loãng",
                "infusion_rate": "Truyền tĩnh mạch trong 30 giây",
                "timing": "Truyền vào cuối mỗi buổi lọc máu, 1 lần/ngày",
                "compatibility": ["0.9% NaCl", "D5W"],
                "incompatibility": [],
                "notes": "QUAN TRỌNG: (1) Chỉ dùng cho bệnh nhân đang lọc máu, (2) Truyền IV trong 30 giây vào cuối mỗi buổi lọc máu, (3) Không truyền trước hoặc trong lọc máu, (4) Theo dõi tác dụng an thần sau truyền."
            }
        },
        "references": {
            "primary_sources": [
                "FDA Drug Label - Difelikefalin (Korsuva)",
                "FDA Approval Date: 8/23/2021",
                "FDA-approved use: To treat moderate-to-severe pruritus associated with chronic kidney disease in certain populations",
                "UpToDate - Difelikefalin: Drug information",
                "Lexicomp - Difelikefalin monograph"
            ],
            "last_updated": "2025-02-18",
            "evidence_level": "A - FDA-approved 8/23/2021, dựa trên dữ liệu lâm sàng từ các thử nghiệm lâm sàng"
        },
        "risk_flags": {
            "high_alert": False,
            "narrow_therapeutic_index": False,
            "bleeding_risk": False,
            "organ_toxicity": [],
            "qt_prolongation": False,
            "hepatotoxicity": False,
            "nephrotoxicity": False,
            "requires_monitoring": ["Clinical response (reduction in pruritus)", "Sedation (drowsiness, fatigue) - CRITICAL", "Liver function (ALT, AST)", "Blood pressure", "Signs of overdose: severe drowsiness, respiratory depression"]
        },
        "guideline_tags": [
            "FDA Drug Information - Difelikefalin (Korsuva)",
            "UpToDate - CKD-Associated Pruritus Treatment",
            "KDIGO Guidelines - CKD Management"
        ],
        "last_updated": "2025-02-18"
    },
    "Bylvay": {
        "group": "FDA Approved 7/20/2021",
        "vietnamese_name": "Odevixibat, Bylvay",
        "administration": ["PO"],
        "indications": [
            "Ngứa do ứ mật (cholestatic pruritus) ở bệnh nhân bệnh gan ứ mật tiến triển ở gia đình (PFIC - Progressive Familial Intrahepatic Cholestasis)",
            "Điều trị ngứa ở bệnh nhân PFIC từ 3 tháng tuổi trở lên"
        ],
        "contraindications": {
            "tuyệt_đối": [
                "Dị ứng odevixibat hoặc bất kỳ thành phần nào"
            ],
            "tương_đối": [
                "Tắc nghẽn đường mật hoàn toàn - thận trọng",
                "Suy gan nặng - thận trọng",
                "Rối loạn hấp thu mỡ nặng - thận trọng"
            ]
        },
        "dosage": {
            "pediatric_3mo_12mo": "40 mcg/kg PO x 1 lần/ngày, tăng dần lên 120 mcg/kg x 1 lần/ngày nếu dung nạp",
            "pediatric_1yr_18yr": "40 mcg/kg PO x 1 lần/ngày, tăng dần lên 120 mcg/kg x 1 lần/ngày nếu dung nạp (tối đa 6mg x 1 lần/ngày)",
            "adult": "6mg PO x 1 lần/ngày (dựa trên cân nặng)",
            "notes": "Uống với thức ăn để giảm tác dụng phụ đường tiêu hóa. Bắt đầu với liều thấp (40 mcg/kg), tăng dần theo đáp ứng và dung nạp. FDA phê duyệt 7/20/2021 cho bệnh nhân từ 3 tháng tuổi trở lên."
        },
        "renal_adjustment": {
            "normal": "Không cần chỉnh liều",
            "30_60": "Thận trọng, không cần chỉnh liều",
            "under_30": "Thận trọng, dữ liệu hạn chế"
        },
        "side_effects": [
            "Tiêu chảy - rất phổ biến (có thể nặng)",
            "Đau bụng - phổ biến",
            "Nôn - phổ biến",
            "Buồn nôn - phổ biến",
            "Giảm cân - phổ biến",
            "Mệt mỏi - phổ biến",
            "Đau đầu - phổ biến",
            "Tăng men gan (ALT, AST) - phổ biến",
            "Giảm hấp thu vitamin tan trong dầu (A, D, E, K) - do giảm hấp thu mỡ",
            "Phát ban - không phổ biến",
            "Ngứa - không phổ biến"
        ],
        "interactions": [
            "Cholestyramine, colestipol: giảm hấp thu odevixibat - dùng cách xa ít nhất 4 giờ",
            "Vitamin tan trong dầu (A, D, E, K): giảm hấp thu - cần bổ sung",
            "Thuốc hấp thu phụ thuộc mỡ: có thể giảm hấp thu"
        ],
        "pregnancy": "C",
        "mechanism_of_action": "Odevixibat là chất ức chế vận chuyển acid mật ở hồi tràng (IBAT - ileal bile acid transporter). Ức chế ASBT (apical sodium-dependent bile acid transporter) ở hồi tràng, ngăn chặn tái hấp thu acid mật từ ruột vào máu. Dẫn đến: (1) Giảm nồng độ acid mật trong huyết thanh, (2) Giảm ngứa do ứ mật (cholestatic pruritus), (3) Tăng thải trừ acid mật qua phân. Được dùng cho ngứa do ứ mật ở bệnh nhân PFIC (Progressive Familial Intrahepatic Cholestasis). ĐẶC ĐIỂM: (1) IBAT inhibitor, tương tự maralixibat, (2) Giảm ngứa do ứ mật hiệu quả, (3) Tác dụng phụ đường tiêu hóa phổ biến (tiêu chảy, đau bụng, nôn), (4) Có thể gây giảm hấp thu vitamin tan trong dầu, (5) FDA phê duyệt 7/20/2021 cho bệnh nhân từ 3 tháng tuổi trở lên.",
        "monitoring": [
            "Đáp ứng điều trị: giảm ngứa (đánh giá bằng thang điểm ngứa)",
            "Tác dụng phụ đường tiêu hóa: tiêu chảy, đau bụng, nôn - QUAN TRỌNG",
            "Cân nặng (đặc biệt ở trẻ em) - giảm cân phổ biến",
            "Chức năng gan: ALT, AST, bilirubin (tăng men gan phổ biến)",
            "Vitamin tan trong dầu: vitamin A, D, E, K (giảm hấp thu)",
            "Dấu hiệu mất nước (nếu tiêu chảy nặng)",
            "Dấu hiệu tắc nghẽn đường mật"
        ],
        "precautions": [
            "TIÊU CHẢY - rất phổ biến, có thể nặng. Có thể cần giảm liều hoặc ngừng tạm thời nếu tiêu chảy nặng.",
            "GIẢM HẤP THU VITAMIN TAN TRONG DẦU - cần bổ sung vitamin A, D, E, K định kỳ",
            "GIẢM CÂN - phổ biến, đặc biệt ở trẻ em. Theo dõi cân nặng chặt chẽ.",
            "Tăng men gan - phổ biến. Theo dõi chức năng gan định kỳ.",
            "Uống với thức ăn để giảm tác dụng phụ đường tiêu hóa",
            "Bắt đầu với liều thấp (40 mcg/kg), tăng dần theo đáp ứng và dung nạp",
            "Thận trọng ở bệnh nhân tắc nghẽn đường mật hoàn toàn",
            "Thận trọng ở bệnh nhân suy gan nặng",
            "Dùng cách xa cholestyramine, colestipol ít nhất 4 giờ"
        ],
        "pharmacokinetics": {
            "half_life": "Khoảng 10-15 giờ",
            "onset": "Vài tuần (tác dụng giảm ngứa)",
            "duration": "24 giờ (dùng 1 lần/ngày)",
            "protein_binding": ">99%",
            "metabolism": "Chuyển hóa tối thiểu, chủ yếu thải trừ nguyên dạng",
            "clearance": "Thải trừ chủ yếu qua phân (không hấp thu), một phần qua nước tiểu"
        },
        "storage": "Bảo quản ở nhiệt độ phòng (20-25°C), tránh ẩm. Bảo quản trong hộp kín gốc. Để xa tầm tay trẻ em.",
        "black_box_warnings": "Không có black box warning. Tuy nhiên, cần cảnh báo về: (1) Tiêu chảy có thể nặng và cần điều trị, (2) Giảm hấp thu vitamin tan trong dầu cần bổ sung, (3) Giảm cân phổ biến, đặc biệt ở trẻ em.",
        "drug_interactions": {
            "major": [],
            "moderate": [
                {
                    "drug": "Cholestyramine, Colestipol",
                    "mechanism": "Giảm hấp thu odevixibat",
                    "effect": "Giảm hiệu quả điều trị",
                    "management": "Dùng cách xa ít nhất 4 giờ. Nếu có thể, tránh dùng cùng."
                },
                {
                    "drug": "Vitamin tan trong dầu (A, D, E, K)",
                    "mechanism": "Odevixibat giảm hấp thu mỡ, dẫn đến giảm hấp thu vitamin tan trong dầu",
                    "effect": "Giảm nồng độ vitamin tan trong dầu, có thể gây thiếu hụt",
                    "management": "Bổ sung vitamin tan trong dầu định kỳ. Theo dõi nồng độ vitamin."
                }
            ],
            "minor": [
                {
                    "drug": "Thuốc hấp thu phụ thuộc mỡ",
                    "mechanism": "Odevixibat giảm hấp thu mỡ",
                    "effect": "Có thể giảm hấp thu các thuốc hấp thu phụ thuộc mỡ",
                    "management": "Thận trọng. Có thể cần điều chỉnh liều hoặc thời điểm dùng."
                }
            ]
        },
        "contraindications_detail": {
            "tuyệt_đối": [
                "Dị ứng odevixibat hoặc bất kỳ thành phần nào"
            ],
            "tương_đối": [
                "Tắc nghẽn đường mật hoàn toàn - thận trọng, có thể không hiệu quả",
                "Suy gan nặng - thận trọng, tăng nguy cơ tác dụng phụ",
                "Rối loạn hấp thu mỡ nặng - thận trọng, có thể làm nặng thêm",
                "Trẻ em <3 tháng tuổi - chưa có dữ liệu an toàn"
            ]
        },
        "pregnancy_lactation": {
            "fda_category": "C",
            "pregnancy_details": "Category C - có nguy cơ cho thai nhi. Không có nghiên cứu đầy đủ trên phụ nữ có thai. Odevixibat có thể ảnh hưởng đến hấp thu vitamin tan trong dầu, có thể ảnh hưởng đến sự phát triển thai nhi. Có thể dùng khi lợi ích vượt quá nguy cơ.",
            "lactation": {
                "safety": "Unknown",
                "details": "Chưa biết odevixibat có bài tiết vào sữa mẹ hay không. Odevixibat hấp thu tối thiểu vào máu, nhưng không có dữ liệu về bài tiết vào sữa mẹ.",
                "recommendation": "Thận trọng khi cho con bú. Cân nhắc ngừng cho con bú hoặc ngừng thuốc. Nếu dùng, theo dõi trẻ sơ sinh về dấu hiệu tác dụng phụ."
            }
        },
        "hepatic_adjustment": {
            "mild": "Không đổi",
            "moderate": "Thận trọng, không cần chỉnh liều",
            "severe": "Thận trọng, có thể cần giảm liều hoặc tránh dùng",
            "notes": "Odevixibat chuyển hóa tối thiểu. Tuy nhiên, ở bệnh nhân suy gan nặng, tăng nguy cơ tác dụng phụ và có thể không hiệu quả. Theo dõi chặt chẽ."
        },
        "overdose_management": {
            "symptoms": [
                "Tiêu chảy nặng",
                "Đau bụng nặng",
                "Nôn nhiều",
                "Mất nước",
                "Rối loạn điện giải"
            ],
            "antidote": "Không có antidote đặc hiệu",
            "treatment": [
                "Ngừng ngay odevixibat",
                "Điều trị hỗ trợ: bù nước và điện giải (truyền dịch nếu cần)",
                "Theo dõi dấu hiệu sinh tồn",
                "Theo dõi cân bằng nước và điện giải",
                "Điều trị triệu chứng (giảm đau nếu cần)"
            ],
            "monitoring": "Theo dõi dấu hiệu sinh tồn, cân bằng nước và điện giải, chức năng gan cho đến khi hồi phục."
        },
        "reversal_agents": {
            "available": False,
            "agents": []
        },
        "administration_instructions": {
            "oral": {
                "with_food": "Uống với thức ăn để giảm tác dụng phụ đường tiêu hóa (tiêu chảy, đau bụng, nôn)",
                "timing": "Uống 1 lần/ngày với bữa ăn. Bắt đầu với liều thấp (40 mcg/kg), tăng dần lên 120 mcg/kg nếu dung nạp.",
                "notes": "QUAN TRỌNG: (1) Uống với thức ăn, (2) Bắt đầu với liều thấp, tăng dần, (3) Nếu tiêu chảy nặng, có thể cần giảm liều hoặc ngừng tạm thời, (4) Bổ sung vitamin tan trong dầu định kỳ, (5) Theo dõi cân nặng chặt chẽ, đặc biệt ở trẻ em."
            }
        },
        "references": {
            "primary_sources": [
                "FDA Drug Label - Odevixibat (Bylvay)",
                "FDA Approval Date: 7/20/2021",
                "FDA-approved use: To treat pruritus in patients with PFIC",
                "UpToDate - Odevixibat: Drug information",
                "Lexicomp - Odevixibat monograph"
            ],
            "last_updated": "2025-02-18",
            "evidence_level": "A - FDA-approved 7/20/2021, dựa trên dữ liệu lâm sàng từ các thử nghiệm lâm sàng"
        },
        "risk_flags": {
            "high_alert": False,
            "narrow_therapeutic_index": False,
            "bleeding_risk": False,
            "organ_toxicity": ["Hepatotoxicity (elevated liver enzymes) - common"],
            "qt_prolongation": False,
            "hepatotoxicity": True,
            "nephrotoxicity": False,
            "requires_monitoring": ["Clinical response (reduction in pruritus)", "GI side effects (diarrhea, abdominal pain, vomiting) - CRITICAL", "Weight (especially in children) - CRITICAL", "Liver function (ALT, AST, bilirubin)", "Fat-soluble vitamins (A, D, E, K)", "Signs of dehydration", "Signs of bile duct obstruction"]
        },
        "guideline_tags": [
            "FDA Drug Information - Odevixibat (Bylvay)",
            "UpToDate - Cholestatic Pruritus Treatment",
            "AASLD Guidelines - Cholestatic Liver Disease"
        ],
        "last_updated": "2025-02-18"
    },
}

__all__ = ['OTHER_TOPICAL_DRUGS']
