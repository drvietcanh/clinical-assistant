"""
Dermatology Drugs - Topical Antiacne
"""
from typing import Dict, Any


TOPICAL_ANTIACNE_DRUGS: Dict[str, Dict[str, Any]] = {
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
            },
            "risk_flags": {
                "high_alert": False,
                "narrow_therapeutic_index": False,
                "bleeding_risk": False,
                "organ_toxicity": [],
                "qt_prolongation": False,
                "hepatotoxicity": False,
                "nephrotoxicity": False,
                "requires_monitoring": ["Clinical response (reduction in acne, rosacea, melasma)", "Signs of skin irritation (redness, dryness, peeling) - common at start"]
            },
            "guideline_tags": [
                "AAD Guidelines - Acne Treatment",
                "AAD Guidelines - Rosacea Treatment",
                "FDA Drug Information - Azelaic Acid",
                "UpToDate - Acne Treatment"
            ]
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

}

__all__ = ['TOPICAL_ANTIACNE_DRUGS']
