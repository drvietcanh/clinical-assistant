"""
Ophthalmology Drugs - Antihistamines
"""
from typing import Dict, Any


ANTIHISTAMINES_DRUGS: Dict[str, Dict[str, Any]] = {
        "Azelastine eye drops": {
            "group": "Ophthalmology - Antihistamine (Allergic Conjunctivitis)",
            "vietnamese_name": "Azelastine, Optivar",
            "administration": ["Ophthalmic"],
            "indications": [
                "Viêm kết mạc dị ứng (allergic conjunctivitis)",
                "Viêm kết mạc dị ứng theo mùa (seasonal allergic conjunctivitis)",
                "Viêm kết mạc dị ứng quanh năm (perennial allergic conjunctivitis)",
                "Ngứa mắt do dị ứng",
                "Đỏ mắt do dị ứng"
            ],
            "contraindications": [
                "Dị ứng azelastine",
                "Nhiễm trùng mắt do vi khuẩn, virus, hoặc nấm (không hiệu quả)"
            ],
            "dosage": {
                "adult_allergic_conjunctivitis": "1 giọt vào mắt bị ảnh hưởng x 2 lần/ngày (cách nhau 8-12 giờ)",
                "pediatric_≥3_years": "1 giọt vào mắt bị ảnh hưởng x 2 lần/ngày (cách nhau 8-12 giờ)",
                "notes": "Azelastine là antihistamine thế hệ 2, đối kháng thụ thể H1. Tác dụng nhanh, giảm ngứa và đỏ mắt. Dùng 2 lần/ngày. Có thể dùng kéo dài. An toàn cho trẻ em ≥3 tuổi."
            },
            "renal_adjustment": {
                "normal": "Không đổi",
                "30_60": "Không đổi",
                "under_30": "Không đổi"
            },
            "side_effects": [
                "Kích ứng mắt tại chỗ (đỏ, rát, ngứa, châm chích) - phổ biến",
                "Nhìn mờ tạm thời",
                "Khô mắt",
                "Vị đắng trong miệng (do hấp thu toàn thân) - phổ biến",
                "Đau đầu",
                "Hấp thu toàn thân (hiếm): buồn ngủ, mệt mỏi"
            ],
            "interactions": [
                "Không có tương tác đáng kể với thuốc khác (ophthalmic)",
                "Thuốc an thần, thuốc ngủ: có thể tăng nguy cơ buồn ngủ nếu hấp thu toàn thân"
            ],
        "pregnancy": "C - Thận trọng",
            "mechanism_of_action": "Azelastine là antihistamine thế hệ 2, đối kháng thụ thể H1. Ngăn chặn tác dụng của histamine (chất trung gian gây viêm trong phản ứng dị ứng), dẫn đến: (1) Giảm ngứa, (2) Giảm đỏ, (3) Giảm sưng, (4) Giảm chảy nước mắt. Azelastine cũng có tác dụng ức chế giải phóng histamine từ mast cells (mast cell stabilizer nhẹ). ĐẶC ĐIỂM: (1) Antihistamine thế hệ 2, đối kháng H1, (2) Tác dụng nhanh, (3) Dùng 2 lần/ngày, (4) Có thể dùng kéo dài, (5) Kích ứng mắt phổ biến, (6) Vị đắng trong miệng do hấp thu toàn thân - phổ biến, (7) An toàn cho trẻ em ≥3 tuổi, (8) Ít gây buồn ngủ hơn antihistamine thế hệ 1.",
            "monitoring": [
                "Đáp ứng lâm sàng (giảm ngứa, đỏ, sưng) - cải thiện sau vài giờ đến 1 ngày",
                "Dấu hiệu kích ứng mắt (đỏ, rát, ngứa, châm chích tăng)",
                "Dấu hiệu hấp thu toàn thân: buồn ngủ, mệt mỏi"
            ],
            "precautions": [
                "CHỈ DÙNG CHO VIÊM KẾT MẠC DỊ ỨNG - không hiệu quả với nhiễm trùng do vi khuẩn, virus, hoặc nấm",
                "Kích ứng mắt - phổ biến, thường giảm sau vài ngày",
                "Vị đắng trong miệng - phổ biến, do hấp thu toàn thân",
                "Có thể dùng kéo dài để duy trì hiệu quả",
                "Hấp thu toàn thân hiếm nhưng có thể gây buồn ngủ - bệnh nhân không nên lái xe nếu có buồn ngủ",
                "Tránh chạm đầu lọ vào mắt hoặc bất kỳ bề mặt nào (nguy cơ nhiễm trùng)",
                "Tháo kính áp tròng trước khi nhỏ, đợi 10 phút trước khi đeo lại"
            ],
            "pharmacokinetics": {
                "half_life": "Không áp dụng (ophthalmic)",
                "onset": "Vài phút đến vài giờ",
                "duration": "8-12 giờ (dùng 2 lần/ngày)",
                "protein_binding": "Không áp dụng (ophthalmic)",
                "metabolism": "Chuyển hóa tại mắt và gan (nếu hấp thu toàn thân, CYP2D6)",
                "clearance": "Thải trừ tại chỗ, hấp thu toàn thân tối thiểu"
            },
            "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ánh sáng. Đóng nắp kín sau khi dùng. Dùng trong 4 tuần sau khi mở.",
            "black_box_warnings": None,
            "drug_interactions": {
                "major": [],
                "moderate": [
                    {
                        "drug": "Thuốc an thần, thuốc ngủ (Benzodiazepines, Opioids, Alcohol)",
                        "mechanism": "Tác dụng ức chế hệ thần kinh trung ương cộng dồn nếu hấp thu toàn thân",
                        "effect": "Tăng nguy cơ buồn ngủ, mệt mỏi",
                        "management": "Thận trọng. Bệnh nhân không nên lái xe nếu có buồn ngủ."
                    }
                ],
                "minor": []
            },
            "contraindications": {
                "tuyệt_đối": [
                    "Dị ứng azelastine",
                    "Nhiễm trùng mắt do vi khuẩn, virus, hoặc nấm - không hiệu quả"
                ],
                "tương_đối": [
                    "Trẻ em <3 tuổi - thận trọng (chưa có dữ liệu đầy đủ)"
                ]
            },
            "pregnancy_lactation": {
                "fda_category": "C",
                "pregnancy_details": "Azelastine là thuốc phân loại C. Không có nghiên cứu đầy đủ trên phụ nữ có thai. Azelastine có thể hấp thu toàn thân và qua nhau thai. Có thể dùng khi lợi ích vượt quá nguy cơ.",
                "lactation": {
                    "safety": "Compatible with Caution",
                    "details": "Azelastine có thể hấp thu toàn thân và bài tiết vào sữa mẹ ở nồng độ thấp. Tuy nhiên, nồng độ trong sữa mẹ thấp khi dùng tại mắt và không có báo cáo về tác dụng phụ đáng kể ở trẻ bú mẹ.",
                    "recommendation": "Có thể dùng khi cho con bú, nhưng thận trọng. Nồng độ trong sữa mẹ thấp."
                }
            },
            "hepatic_adjustment": {
                "mild": "Không cần điều chỉnh liều",
                "moderate": "Không cần điều chỉnh liều",
                "severe": "Không cần điều chỉnh liều (ophthalmic, hấp thu tối thiểu)",
                "notes": "Azelastine dùng tại mắt, hấp thu toàn thân tối thiểu. Không cần điều chỉnh liều ở bệnh nhân suy gan."
            },
            "overdose_management": {
                "symptoms": [
                    "Kích ứng mắt nặng",
                    "Hấp thu toàn thân (hiếm): buồn ngủ nặng, mệt mỏi"
                ],
                "antidote": "Không có antidote đặc hiệu. Rửa mắt, điều trị hỗ trợ.",
                "treatment": [
                    "Rửa mắt ngay với nước sạch hoặc nước muối sinh lý",
                    "Nếu kích ứng mắt nặng:",
                    "  - Khám mắt ngay",
                    "  - Điều trị hỗ trợ (nước mắt nhân tạo)",
                    "Nếu hấp thu toàn thân:",
                    "  - Theo dõi sát",
                    "  - Tránh lái xe hoặc vận hành máy móc",
                    "Theo dõi: Thị lực, dấu hiệu kích ứng mắt, tình trạng thần kinh"
                ],
                "monitoring": "Theo dõi thị lực, dấu hiệu kích ứng mắt, tình trạng thần kinh (nếu hấp thu toàn thân) cho đến khi hồi phục."
            },
            "reversal_agents": None,
            "administration_instructions": {
                "ophthalmic": {
                    "preparation": "Dạng dung dịch nhỏ mắt 0.05%.",
                    "application": "1 giọt vào mắt bị ảnh hưởng x 2 lần/ngày (cách nhau 8-12 giờ). Nhắm mắt nhẹ 1-2 phút sau khi nhỏ. Nhấn nhẹ vào góc trong mắt (lacrimal sac) trong 1-2 phút để giảm hấp thu toàn thân.",
                    "timing": "2 lần/ngày (cách nhau 8-12 giờ). Có thể dùng kéo dài.",
                    "contact_lenses": "Tháo kính áp tròng trước khi nhỏ. Đợi 10 phút trước khi đeo lại.",
                    "notes": "QUAN TRỌNG: 1) CHỈ DÙNG CHO VIÊM KẾT MẠC DỊ ỨNG, 2) Dùng 2 lần/ngày, 3) Kích ứng mắt và vị đắng trong miệng phổ biến, 4) Có thể dùng kéo dài, 5) Tránh chạm đầu lọ vào mắt."
                }
            },
            "references": {
                "primary_sources": [
                    "FDA Drug Label - Azelastine (Optivar)",
                    "UpToDate - Azelastine: Drug Information",
                    "Medscape - Azelastine Drug Reference",
                    "AAO Guidelines - Allergic Conjunctivitis"
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
                "requires_monitoring": ["Clinical response (reduction in itching, redness, swelling)", "Signs of eye irritation", "Systemic effects (drowsiness, fatigue) if systemic absorption"]
            },
            "guideline_tags": [
                "AAO Guidelines - Allergic Conjunctivitis",
                "EAACI Guidelines - Allergic Conjunctivitis",
                "FDA Drug Information - Azelastine Ophthalmic"
            ],
            "black_box_warnings": "Cần xem xét black box warnings",
            "reversal_agents": {
                "available": False,
                "agents": [],
            },
        },

        "Ketotifen eye drops": {
            "group": "Ophthalmology - Antihistamine/Mast Cell Stabilizer (Allergic Conjunctivitis)",
            "vietnamese_name": "Ketotifen, Zaditor, Alaway",
            "administration": ["Ophthalmic"],
            "indications": [
                "Viêm kết mạc dị ứng (allergic conjunctivitis)",
                "Viêm kết mạc dị ứng theo mùa (seasonal allergic conjunctivitis)",
                "Viêm kết mạc dị ứng quanh năm (perennial allergic conjunctivitis)",
                "Ngứa mắt do dị ứng",
                "Đỏ mắt do dị ứng"
            ],
            "contraindications": [
                "Dị ứng ketotifen",
                "Nhiễm trùng mắt do vi khuẩn, virus, hoặc nấm (không hiệu quả)"
            ],
            "dosage": {
                "adult_allergic_conjunctivitis": "1 giọt vào mắt bị ảnh hưởng x 2 lần/ngày (cách nhau 8-12 giờ)",
                "pediatric_≥3_years": "1 giọt vào mắt bị ảnh hưởng x 2 lần/ngày (cách nhau 8-12 giờ)",
                "notes": "Ketotifen là antihistamine và mast cell stabilizer. Ức chế giải phóng histamine và các chất trung gian gây viêm từ mast cells, và đối kháng thụ thể H1. Dùng 2 lần/ngày. Có thể dùng kéo dài. An toàn cho trẻ em ≥3 tuổi."
            },
            "renal_adjustment": {
                "normal": "Không đổi",
                "30_60": "Không đổi",
                "under_30": "Không đổi"
            },
            "side_effects": [
                "Kích ứng mắt tại chỗ (đỏ, rát, ngứa, châm chích) - phổ biến trong vài ngày đầu",
                "Nhìn mờ tạm thời",
                "Khô mắt",
                "Đau đầu",
                "Chảy nước mũi (rhinorrhea)",
                "Hấp thu toàn thân (hiếm): buồn ngủ, mệt mỏi"
            ],
            "interactions": [
                "Không có tương tác đáng kể với thuốc khác (ophthalmic)",
                "Thuốc an thần, thuốc ngủ: có thể tăng nguy cơ buồn ngủ nếu hấp thu toàn thân"
            ],
        "pregnancy": "C - Thận trọng",
            "mechanism_of_action": "Ketotifen là antihistamine và mast cell stabilizer. Tác dụng kép: (1) Mast cell stabilizer - ức chế giải phóng histamine và các chất trung gian gây viêm (leukotrienes, prostaglandins) từ mast cells, (2) Antihistamine - đối kháng thụ thể H1, ngăn chặn tác dụng của histamine. Dẫn đến: giảm ngứa, giảm đỏ, giảm sưng trong viêm kết mạc dị ứng. ĐẶC ĐIỂM: (1) Tác dụng kép: mast cell stabilizer + antihistamine, (2) Dùng 2 lần/ngày, (3) Có thể dùng kéo dài, (4) Kích ứng mắt phổ biến trong vài ngày đầu, (5) An toàn cho trẻ em ≥3 tuổi, (6) Hấp thu toàn thân hiếm nhưng có thể gây buồn ngủ.",
            "monitoring": [
                "Đáp ứng lâm sàng (giảm ngứa, đỏ, sưng) - cải thiện sau 2-3 ngày",
                "Dấu hiệu kích ứng mắt (đỏ, rát, ngứa, châm chích tăng)",
                "Dấu hiệu hấp thu toàn thân: buồn ngủ, mệt mỏi"
            ],
            "precautions": [
                "CHỈ DÙNG CHO VIÊM KẾT MẠC DỊ ỨNG - không hiệu quả với nhiễm trùng do vi khuẩn, virus, hoặc nấm",
                "Kích ứng mắt - phổ biến trong vài ngày đầu, thường giảm sau vài ngày",
                "Có thể dùng kéo dài để duy trì hiệu quả",
                "Hấp thu toàn thân hiếm nhưng có thể gây buồn ngủ - bệnh nhân không nên lái xe nếu có buồn ngủ",
                "Tránh chạm đầu lọ vào mắt hoặc bất kỳ bề mặt nào (nguy cơ nhiễm trùng)",
                "Tháo kính áp tròng trước khi nhỏ, đợi 10 phút trước khi đeo lại"
            ],
            "pharmacokinetics": {
                "half_life": "Không áp dụng (ophthalmic)",
                "onset": "Vài phút đến vài giờ",
                "duration": "8-12 giờ (dùng 2 lần/ngày)",
                "protein_binding": "Không áp dụng (ophthalmic)",
                "metabolism": "Chuyển hóa tại mắt và gan (nếu hấp thu toàn thân)",
                "clearance": "Thải trừ tại chỗ, hấp thu toàn thân tối thiểu"
            },
            "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ánh sáng. Đóng nắp kín sau khi dùng. Dùng trong 4 tuần sau khi mở.",
            "black_box_warnings": None,
            "drug_interactions": {
                "major": [],
                "moderate": [
                    {
                        "drug": "Thuốc an thần, thuốc ngủ (Benzodiazepines, Opioids, Alcohol)",
                        "mechanism": "Tác dụng ức chế hệ thần kinh trung ương cộng dồn nếu hấp thu toàn thân",
                        "effect": "Tăng nguy cơ buồn ngủ, mệt mỏi",
                        "management": "Thận trọng. Bệnh nhân không nên lái xe nếu có buồn ngủ."
                    }
                ],
                "minor": []
            },
            "contraindications": {
                "tuyệt_đối": [
                    "Dị ứng ketotifen",
                    "Nhiễm trùng mắt do vi khuẩn, virus, hoặc nấm - không hiệu quả"
                ],
                "tương_đối": [
                    "Trẻ em <3 tuổi - thận trọng (chưa có dữ liệu đầy đủ)"
                ]
            },
            "pregnancy_lactation": {
                "fda_category": "C",
                "pregnancy_details": "Ketotifen là thuốc phân loại C. Không có nghiên cứu đầy đủ trên phụ nữ có thai. Ketotifen có thể hấp thu toàn thân và qua nhau thai. Có thể dùng khi lợi ích vượt quá nguy cơ.",
                "lactation": {
                    "safety": "Compatible with Caution",
                    "details": "Ketotifen có thể hấp thu toàn thân và bài tiết vào sữa mẹ ở nồng độ thấp. Tuy nhiên, nồng độ trong sữa mẹ thấp khi dùng tại mắt và không có báo cáo về tác dụng phụ đáng kể ở trẻ bú mẹ.",
                    "recommendation": "Có thể dùng khi cho con bú, nhưng thận trọng. Nồng độ trong sữa mẹ thấp."
                }
            },
            "hepatic_adjustment": {
                "mild": "Không cần điều chỉnh liều",
                "moderate": "Không cần điều chỉnh liều",
                "severe": "Không cần điều chỉnh liều (ophthalmic, hấp thu tối thiểu)",
                "notes": "Ketotifen dùng tại mắt, hấp thu toàn thân tối thiểu. Không cần điều chỉnh liều ở bệnh nhân suy gan."
            },
            "overdose_management": {
                "symptoms": [
                    "Kích ứng mắt nặng",
                    "Hấp thu toàn thân (hiếm): buồn ngủ nặng, mệt mỏi"
                ],
                "antidote": "Không có antidote đặc hiệu. Rửa mắt, điều trị hỗ trợ.",
                "treatment": [
                    "Rửa mắt ngay với nước sạch hoặc nước muối sinh lý",
                    "Nếu kích ứng mắt nặng:",
                    "  - Khám mắt ngay",
                    "  - Điều trị hỗ trợ (nước mắt nhân tạo)",
                    "Nếu hấp thu toàn thân:",
                    "  - Theo dõi sát",
                    "  - Tránh lái xe hoặc vận hành máy móc",
                    "Theo dõi: Thị lực, dấu hiệu kích ứng mắt, tình trạng thần kinh"
                ],
                "monitoring": "Theo dõi thị lực, dấu hiệu kích ứng mắt, tình trạng thần kinh (nếu hấp thu toàn thân) cho đến khi hồi phục."
            },
            "reversal_agents": None,
            "administration_instructions": {
                "ophthalmic": {
                    "preparation": "Dạng dung dịch nhỏ mắt 0.025% hoặc 0.035%.",
                    "application": "1 giọt vào mắt bị ảnh hưởng x 2 lần/ngày (cách nhau 8-12 giờ). Nhắm mắt nhẹ 1-2 phút sau khi nhỏ. Nhấn nhẹ vào góc trong mắt (lacrimal sac) trong 1-2 phút để giảm hấp thu toàn thân.",
                    "timing": "2 lần/ngày (cách nhau 8-12 giờ). Có thể dùng kéo dài.",
                    "contact_lenses": "Tháo kính áp tròng trước khi nhỏ. Đợi 10 phút trước khi đeo lại.",
                    "notes": "QUAN TRỌNG: 1) CHỈ DÙNG CHO VIÊM KẾT MẠC DỊ ỨNG, 2) Dùng 2 lần/ngày, 3) Kích ứng mắt phổ biến trong vài ngày đầu, 4) Có thể dùng kéo dài, 5) Tránh chạm đầu lọ vào mắt."
                }
            },
            "references": {
                "primary_sources": [
                    "FDA Drug Label - Ketotifen (Zaditor, Alaway)",
                    "UpToDate - Ketotifen: Drug Information",
                    "Medscape - Ketotifen Drug Reference",
                    "AAO Guidelines - Allergic Conjunctivitis"
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
                "requires_monitoring": ["Clinical response (reduction in itching, redness, swelling)", "Signs of eye irritation", "Systemic effects (drowsiness, fatigue) if systemic absorption"]
            },
            "guideline_tags": [
                "AAO Guidelines - Allergic Conjunctivitis",
                "EAACI Guidelines - Allergic Conjunctivitis",
                "FDA Drug Information - Ketotifen Ophthalmic"
            ],
            "black_box_warnings": "Cần xem xét black box warnings",
            "reversal_agents": {
                "available": False,
                "agents": [],
            },
        },

        "Olopatadine eye drops": {
            "group": "Ophthalmology - Antihistamine/Mast Cell Stabilizer (Allergic Conjunctivitis)",
            "vietnamese_name": "Olopatadine nhỏ mắt, Patanol, Pataday",
            "administration": ["Ophthalmic"],
            "indications": [
                "Viêm kết mạc dị ứng (allergic conjunctivitis)",
                "Ngứa mắt do dị ứng",
                "Đỏ mắt do dị ứng"
            ],
            "contraindications": [
                "Dị ứng olopatadine hoặc bất kỳ thành phần nào"
            ],
            "dosage": {
                "adult_ophthalmic_0.1%": "1 giọt vào mắt bị ảnh hưởng 2 lần/ngày (cách nhau 6-8 giờ)",
                "adult_ophthalmic_0.2%": "1 giọt vào mắt bị ảnh hưởng 1 lần/ngày",
                "pediatric_3_17": "1 giọt vào mắt bị ảnh hưởng 2 lần/ngày (0.1%) hoặc 1 lần/ngày (0.2%)",
                "notes": "Olopatadine là thuốc kép: vừa là antihistamine (ức chế H1 receptor), vừa là mast cell stabilizer (ngăn chặn giải phóng histamine). Hiệu quả với viêm kết mạc dị ứng. Dùng 1-2 lần/ngày tùy theo nồng độ."
            },
            "renal_adjustment": {
                "normal": "Không đổi",
                "30_60": "Không đổi",
                "under_30": "Không đổi"
            },
            "side_effects": [
                "Kích ứng mắt nhẹ (đỏ, rát, ngứa) - phổ biến",
                "Nhìn mờ tạm thời - phổ biến ngay sau khi nhỏ",
                "Đau đầu - hiếm",
                "Khô mắt - hiếm",
                "Vị đắng trong miệng (do hấp thu toàn thân) - hiếm",
                "Phản ứng dị ứng - hiếm"
            ],
            "interactions": [
                "Không có tương tác đáng kể với thuốc khác (ophthalmic)"
            ],
        "pregnancy": "C - Thận trọng",
            "mechanism_of_action": "Olopatadine là thuốc kép: (1) Antihistamine - ức chế H1 receptor trên tế bào, ngăn chặn tác dụng của histamine (giảm ngứa, giảm đỏ, giảm sưng), (2) Mast cell stabilizer - ổn định màng tế bào mast, ngăn chặn giải phóng histamine và các chất trung gian viêm khác. Dẫn đến: giảm ngứa, giảm đỏ, giảm sưng, giảm chảy nước mắt trong viêm kết mạc dị ứng. Olopatadine hiệu quả với cả triệu chứng cấp tính (antihistamine) và phòng ngừa (mast cell stabilizer). ĐẶC ĐIỂM: (1) Thuốc kép: antihistamine + mast cell stabilizer, (2) Hiệu quả với viêm kết mạc dị ứng, (3) Dùng 1-2 lần/ngày tùy theo nồng độ, (4) An toàn, ít tác dụng phụ, (5) Nhìn mờ tạm thời ngay sau khi nhỏ - phổ biến.",
            "monitoring": [
                "Dấu hiệu viêm kết mạc dị ứng (ngứa, đỏ, chảy nước mắt) - cải thiện sau vài ngày",
                "Dấu hiệu kích ứng mắt (đỏ, rát, ngứa)",
                "Thị lực - nhìn mờ tạm thời ngay sau khi nhỏ là bình thường"
            ],
            "precautions": [
                "Nhìn mờ tạm thời ngay sau khi nhỏ - phổ biến, thường hết sau vài phút",
                "Kích ứng mắt nhẹ - phổ biến, thường giảm sau vài ngày",
                "Thận trọng ở bệnh nhân đeo kính áp tròng (benzalkonium chloride có thể làm hỏng kính)",
                "Tránh chạm đầu lọ vào mắt hoặc bất kỳ bề mặt nào (nguy cơ nhiễm trùng)",
                "Nếu viêm kết mạc dị ứng nặng hoặc kéo dài, cần khám mắt để tìm nguyên nhân"
            ],
            "pharmacokinetics": {
                "half_life": "3 giờ (huyết tương, nếu hấp thu toàn thân), nhưng tác dụng tại mắt kéo dài",
                "onset": "Vài phút",
                "duration": "8-12 giờ (dùng 1-2 lần/ngày)",
                "protein_binding": "55%",
                "metabolism": "Chuyển hóa tại mắt và gan (nếu hấp thu toàn thân)",
                "clearance": "Thải trừ qua thận (nếu hấp thu toàn thân)"
            },
            "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ánh sáng. Đóng nắp kín sau khi dùng. Dùng trong 4 tuần sau khi mở.",
            "black_box_warnings": None,
            "drug_interactions": {
                "major": [],
                "moderate": [],
                "minor": []
            },
            "contraindications": {
                "tuyệt_đối": [
                    "Dị ứng olopatadine hoặc bất kỳ thành phần nào"
                ],
                "tương_đối": [
                    "Bệnh nhân đeo kính áp tròng - thận trọng (benzalkonium chloride)",
                    "Có thai (category C) - thận trọng"
                ]
            },
            "pregnancy_lactation": {
                "fda_category": "C",
                "pregnancy_details": "Olopatadine là thuốc phân loại C. Olopatadine có thể hấp thu toàn thân và qua nhau thai. Không có nghiên cứu đầy đủ trên phụ nữ có thai. Có thể dùng khi lợi ích vượt quá nguy cơ, đặc biệt khi không có lựa chọn khác.",
                "lactation": {
                    "safety": "Compatible with Caution",
                    "details": "Olopatadine có thể hấp thu toàn thân và bài tiết vào sữa mẹ. Tuy nhiên, nồng độ trong sữa mẹ thấp khi dùng tại mắt và không có báo cáo về tác dụng phụ đáng kể ở trẻ bú mẹ.",
                    "recommendation": "Có thể dùng khi cho con bú, nhưng thận trọng. Nồng độ trong sữa mẹ thấp."
                }
            },
            "hepatic_adjustment": {
                "mild": "Không cần điều chỉnh liều",
                "moderate": "Không cần điều chỉnh liều",
                "severe": "Không cần điều chỉnh liều (ophthalmic, hấp thu tối thiểu)",
                "notes": "Olopatadine dùng tại mắt, hấp thu toàn thân tối thiểu. Không cần điều chỉnh liều ở bệnh nhân suy gan."
            },
            "overdose_management": {
                "symptoms": [
                    "Kích ứng mắt nặng",
                    "Nhìn mờ tạm thời"
                ],
                "antidote": "Không có antidote đặc hiệu. Rửa mắt, điều trị hỗ trợ.",
                "treatment": [
                    "Rửa mắt ngay với nước sạch hoặc nước muối sinh lý",
                    "Nhìn mờ tạm thời thường hết sau vài phút",
                    "Nếu kích ứng mắt nặng:",
                    "  - Khám mắt nếu cần",
                    "  - Điều trị hỗ trợ (nước mắt nhân tạo)",
                    "Theo dõi: Thị lực, dấu hiệu kích ứng"
                ],
                "monitoring": "Theo dõi thị lực và dấu hiệu kích ứng cho đến khi hồi phục."
            },
            "reversal_agents": None,
            "administration_instructions": {
                "oral": None,
                "ophthalmic": {
                    "preparation": "Dạng dung dịch nhỏ mắt 0.1% hoặc 0.2%.",
                    "application": "1 giọt vào mắt bị ảnh hưởng 1-2 lần/ngày tùy theo nồng độ (xem dosage). Nhắm mắt nhẹ 1-2 phút sau khi nhỏ. Nhấn nhẹ vào góc trong mắt (lacrimal sac) trong 1-2 phút để giảm hấp thu toàn thân.",
                    "timing": "1-2 lần/ngày tùy theo nồng độ (0.1%: 2 lần/ngày, 0.2%: 1 lần/ngày).",
                    "contact_lenses": "Tháo kính áp tròng trước khi nhỏ. Đợi 15 phút trước khi đeo lại.",
                    "notes": "QUAN TRỌNG: 1) Dùng 1-2 lần/ngày tùy theo nồng độ, 2) Nhìn mờ tạm thời ngay sau khi nhỏ là bình thường, 3) Tránh chạm đầu lọ vào mắt hoặc bất kỳ bề mặt nào, 4) Nếu viêm kết mạc dị ứng nặng hoặc kéo dài, cần khám mắt để tìm nguyên nhân."
                }
            },
            "references": {
                "primary_sources": [
                    "FDA Drug Label - Olopatadine (Patanol, Pataday)",
                    "UpToDate - Olopatadine: Drug Information",
                    "Medscape - Olopatadine Drug Reference",
                    "AAO Guidelines - Allergic Conjunctivitis"
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
                "requires_monitoring": ["Clinical response (improvement in allergic conjunctivitis symptoms)", "Signs of eye irritation", "Visual acuity (temporary blurring after instillation is normal)"]
            },
            "guideline_tags": [
                "AAO Guidelines - Allergic Conjunctivitis",
                "EAACI Guidelines - Allergic Conjunctivitis",
                "FDA Drug Information - Olopatadine Ophthalmic"
            ],
            "black_box_warnings": "Cần xem xét black box warnings",
            "reversal_agents": {
                "available": False,
                "agents": [],
            },
        },

}

__all__ = ['ANTIHISTAMINES_DRUGS']
