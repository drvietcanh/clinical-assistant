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

}

__all__ = ['OTHER_TOPICAL_DRUGS']
