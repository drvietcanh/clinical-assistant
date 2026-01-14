"""
Ophthalmology Drugs - Anti Infective
"""
from typing import Dict, Any


ANTI_INFECTIVE_DRUGS: Dict[str, Dict[str, Any]] = {
        "Acyclovir eye drops": {
            "group": "Ophthalmology - Antiviral",
            "vietnamese_name": "Acyclovir nhỏ mắt, Zovirax",
            "administration": ["Ophthalmic"],
            "indications": [
                "Viêm giác mạc do Herpes simplex (herpetic keratitis)",
                "Viêm kết mạc do Herpes simplex (herpetic conjunctivitis)",
                "Viêm màng bồ đào do Herpes simplex (herpetic uveitis)",
                "Dự phòng tái phát viêm giác mạc do Herpes simplex"
            ],
            "contraindications": [
                "Dị ứng acyclovir hoặc valacyclovir",
                "Dị ứng benzalkonium chloride"
            ],
            "dosage": {
                "adult_keratitis": "1 giọt dung dịch 3% vào mắt bị ảnh hưởng 5 lần/ngày (mỗi 3 giờ khi thức) trong 7-10 ngày",
                "adult_conjunctivitis": "1 giọt dung dịch 3% vào mắt bị ảnh hưởng 5 lần/ngày trong 7-10 ngày",
                "adult_prophylaxis": "1 giọt dung dịch 3% vào mắt bị ảnh hưởng 3-5 lần/ngày để dự phòng tái phát",
                "notes": "Acyclovir là thuốc kháng virus, hiệu quả với Herpes simplex. Dùng 5 lần/ngày (mỗi 3 giờ khi thức) cho viêm giác mạc. Có thể dùng kéo dài để dự phòng tái phát."
            },
            "renal_adjustment": {
                "normal": "Không đổi",
                "30_60": "Không đổi",
                "under_30": "Không đổi"
            },
            "side_effects": [
                "Kích ứng mắt (đỏ, rát, ngứa) - phổ biến",
                "Khô mắt",
                "Nhìn mờ tạm thời",
                "Đau mắt",
                "Chảy nước mắt",
                "Phản ứng dị ứng (phát ban, ngứa) - hiếm",
                "Viêm mi mắt (blepharitis) - hiếm"
            ],
            "interactions": [
                "Không có tương tác đáng kể với thuốc khác (ophthalmic)"
            ],
            "pregnancy": "B - An toàn",
            "mechanism_of_action": "Acyclovir là thuốc kháng virus, ức chế DNA polymerase của virus Herpes simplex. Acyclovir được phosphoryl hóa bởi thymidine kinase của virus (chỉ có trong tế bào nhiễm virus) thành acyclovir monophosphate, sau đó được phosphoryl hóa tiếp thành acyclovir triphosphate. Acyclovir triphosphate gắn với DNA polymerase của virus, ngăn chặn sự tổng hợp DNA virus, dẫn đến ức chế sự nhân lên của virus. Dẫn đến: giảm viêm giác mạc, viêm kết mạc do Herpes simplex. ĐẶC ĐIỂM: (1) Kháng virus Herpes simplex, (2) Dùng 5 lần/ngày (mỗi 3 giờ khi thức) cho viêm giác mạc, (3) Có thể dùng kéo dài để dự phòng tái phát, (4) Kích ứng mắt phổ biến, (5) An toàn trong thai kỳ (category B), (6) An toàn, ít tác dụng phụ toàn thân.",
            "monitoring": [
                "Đáp ứng lâm sàng (giảm đỏ, sưng, loét giác mạc) - cải thiện sau 3-5 ngày",
                "Dấu hiệu kích ứng mắt (đỏ, rát, ngứa tăng)",
                "Dấu hiệu nhiễm trùng (loét giác mạc tăng, mủ) - nếu không cải thiện",
                "Dấu hiệu phản ứng dị ứng (phát ban, ngứa)",
                "Thị lực và khám mắt định kỳ",
                "Dấu hiệu tái phát (loét giác mạc mới)"
            ],
            "precautions": [
                "Kích ứng mắt phổ biến - thường giảm sau vài ngày",
                "Dùng đủ liều và đủ thời gian (7-10 ngày) để tránh tái phát",
                "Có thể dùng kéo dài để dự phòng tái phát",
                "Tránh chạm đầu lọ vào mắt hoặc bất kỳ bề mặt nào (nguy cơ nhiễm trùng)",
                "Tháo kính áp tròng trước khi nhỏ (benzalkonium chloride có thể làm hỏng kính)",
                "Đợi 15 phút trước khi đeo lại kính áp tròng",
                "Không dùng chung lọ với người khác",
                "Kết hợp với acyclovir đường uống nếu có nhiễm trùng toàn thân"
            ],
            "pharmacokinetics": {
                "half_life": "Không áp dụng (ophthalmic)",
                "onset": "Ngay lập tức",
                "duration": "3 giờ (dùng 5 lần/ngày)",
                "protein_binding": "Không áp dụng (ophthalmic)",
                "metabolism": "Chuyển hóa tại mắt (thymidine kinase của virus)",
                "clearance": "Thải trừ tại chỗ, hấp thu toàn thân tối thiểu"
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
                    "Dị ứng acyclovir hoặc valacyclovir",
                    "Dị ứng benzalkonium chloride"
                ],
                "tương_đối": [
                    "Da nhạy cảm - thận trọng, theo dõi dấu hiệu kích ứng"
                ]
            },
            "pregnancy_lactation": {
                "fda_category": "B",
                "pregnancy_details": "Acyclovir là thuốc phân loại B. Không hấp thu toàn thân khi dùng tại mắt. An toàn trong thai kỳ.",
                "lactation": {
                    "safety": "Compatible",
                    "details": "Acyclovir không hấp thu toàn thân khi dùng tại mắt, không bài tiết vào sữa mẹ. An toàn khi cho con bú.",
                    "recommendation": "Có thể dùng khi cho con bú. An toàn, không có tác dụng phụ."
                }
            },
            "hepatic_adjustment": {
                "mild": "Không cần điều chỉnh liều",
                "moderate": "Không cần điều chỉnh liều",
                "severe": "Không cần điều chỉnh liều (ophthalmic, hấp thu tối thiểu)",
                "notes": "Acyclovir dùng tại mắt, hấp thu toàn thân tối thiểu. Không cần điều chỉnh liều ở bệnh nhân suy gan."
            },
            "overdose_management": {
                "symptoms": [
                    "Kích ứng mắt nặng",
                    "Đỏ mắt nặng"
                ],
                "antidote": "Không có antidote đặc hiệu. Rửa mắt, điều trị hỗ trợ.",
                "treatment": [
                    "Rửa mắt ngay với nước sạch hoặc nước muối sinh lý",
                    "Nếu kích ứng mắt nặng:",
                    "  - Khám mắt ngay",
                    "  - Điều trị hỗ trợ (nước mắt nhân tạo, thuốc chống viêm nếu cần)",
                    "Theo dõi: Thị lực, dấu hiệu kích ứng mắt"
                ],
                "monitoring": "Theo dõi thị lực, dấu hiệu kích ứng mắt cho đến khi hồi phục."
            },
            "reversal_agents": None,
            "administration_instructions": {
                "oral": None,
                "ophthalmic": {
                    "preparation": "Dạng dung dịch nhỏ mắt 3%.",
                    "application": "1 giọt vào mắt bị ảnh hưởng 5 lần/ngày (mỗi 3 giờ khi thức) cho viêm giác mạc, hoặc 3-5 lần/ngày cho dự phòng. Nhắm mắt nhẹ 1-2 phút sau khi nhỏ.",
                    "timing": "5 lần/ngày (mỗi 3 giờ khi thức) cho viêm giác mạc. 3-5 lần/ngày cho dự phòng.",
                    "contact_lenses": "Tháo kính áp tròng trước khi nhỏ. Đợi 15 phút trước khi đeo lại.",
                    "notes": "QUAN TRỌNG: 1) Dùng đủ liều và đủ thời gian (7-10 ngày), 2) Có thể dùng kéo dài để dự phòng tái phát, 3) Tránh chạm đầu lọ vào mắt, 4) Tháo kính áp tròng trước khi nhỏ, 5) Không dùng chung lọ với người khác."
                }
            },
            "references": {
                "primary_sources": [
                    "FDA Drug Label - Acyclovir (Zovirax)",
                    "UpToDate - Acyclovir: Drug Information",
                    "Medscape - Acyclovir Drug Reference",
                    "AAO Guidelines - Herpetic Keratitis"
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
                "requires_monitoring": ["Clinical response (reduction in redness, swelling, corneal ulcer)", "Signs of eye irritation", "Visual acuity", "Signs of recurrence"]
            },
            "guideline_tags": [
                "AAO Guidelines - Herpetic Keratitis",
                "FDA Drug Information - Acyclovir Ophthalmic",
                "UpToDate - Herpetic Keratitis Treatment"
            ],
            "black_box_warnings": "Cần xem xét black box warnings",
            "reversal_agents": {
                "available": False,
                "agents": [],
            },
        },

        "Acyclovir eye ointment": {
            "group": "Ophthalmology - Antiviral (Herpes)",
            "vietnamese_name": "Acyclovir, Zovirax",
            "administration": ["Ophthalmic"],
            "indications": [
                "Viêm giác mạc do herpes simplex (herpetic keratitis)",
                "Viêm giác mạc do herpes zoster (herpetic zoster keratitis)",
                "Dự phòng tái phát viêm giác mạc do herpes"
            ],
            "contraindications": [
                "Dị ứng acyclovir hoặc valacyclovir",
                "Nhiễm trùng do vi khuẩn hoặc nấm (không hiệu quả)"
            ],
            "dosage": {
                "adult_keratitis": "Bôi mỏng vào mắt bị ảnh hưởng x 5 lần/ngày (mỗi 3-4 giờ) trong 7-10 ngày",
                "adult_prophylaxis": "Bôi mỏng vào mắt bị ảnh hưởng x 3 lần/ngày trong vài tuần đến vài tháng",
                "notes": "Acyclovir là thuốc kháng virus, hiệu quả với herpes simplex và herpes zoster. Dùng 5 lần/ngày cho điều trị, 3 lần/ngày cho dự phòng. Có thể gây nhìn mờ tạm thời sau khi bôi."
            },
            "renal_adjustment": {
                "normal": "Không đổi",
                "30_60": "Không đổi",
                "under_30": "Không đổi"
            },
            "side_effects": [
                "Nhìn mờ tạm thời sau khi bôi - phổ biến",
                "Kích ứng mắt tại chỗ (đỏ, rát, ngứa) - phổ biến",
                "Khô mắt",
                "Phản ứng dị ứng (phát ban, ngứa) - hiếm",
                "Viêm kết mạc (conjunctivitis) - hiếm"
            ],
            "interactions": [
                "Không có tương tác đáng kể với thuốc khác (ophthalmic)"
            ],
            "pregnancy": "B - An toàn",
            "mechanism_of_action": "Acyclovir là thuốc kháng virus, ức chế DNA polymerase của virus herpes, ngăn chặn sự tổng hợp DNA virus, dẫn đến ức chế sự nhân lên của virus. Hiệu quả với herpes simplex và herpes zoster. ĐẶC ĐIỂM: (1) Kháng virus, hiệu quả với herpes simplex và herpes zoster, (2) Dùng 5 lần/ngày cho điều trị, 3 lần/ngày cho dự phòng, (3) Nhìn mờ tạm thời sau khi bôi - phổ biến, (4) An toàn trong thai kỳ (category B), (5) Kích ứng mắt phổ biến.",
            "monitoring": [
                "Đáp ứng lâm sàng (giảm đỏ, sưng, đau) - cải thiện sau 2-3 ngày",
                "Dấu hiệu kích ứng mắt (đỏ, rát, ngứa tăng)",
                "Dấu hiệu nhiễm trùng (mủ, đỏ, sưng tăng) - nếu không cải thiện",
                "Thị lực (nhìn mờ tạm thời sau khi bôi)"
            ],
            "precautions": [
                "CHỈ DÙNG CHO NHIỄM TRÙNG DO VIRUS HERPES - không hiệu quả với vi khuẩn hoặc nấm",
                "Dùng đủ liều và đủ thời gian (7-10 ngày) để tránh tái phát",
                "Nhìn mờ tạm thời sau khi bôi - phổ biến, bệnh nhân không nên lái xe ngay sau khi bôi",
                "Kích ứng mắt - phổ biến, thường giảm sau vài ngày",
                "Tránh chạm đầu ống vào mắt hoặc bất kỳ bề mặt nào (nguy cơ nhiễm trùng)",
                "Không đeo kính áp tròng khi đang điều trị"
            ],
            "pharmacokinetics": {
                "half_life": "Không áp dụng (ophthalmic)",
                "onset": "Ngay lập tức",
                "duration": "3-4 giờ (dùng 5 lần/ngày)",
                "protein_binding": "Không áp dụng (ophthalmic)",
                "metabolism": "Chuyển hóa tại mắt và gan (nếu hấp thu toàn thân)",
                "clearance": "Thải trừ tại chỗ, hấp thu toàn thân tối thiểu"
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
                    "Dị ứng acyclovir hoặc valacyclovir",
                    "Nhiễm trùng do vi khuẩn hoặc nấm - không hiệu quả"
                ],
                "tương_đối": [
                    "Dùng kéo dài - nguy cơ tái phát"
                ]
            },
            "pregnancy_lactation": {
                "fda_category": "B",
                "pregnancy_details": "Acyclovir là thuốc phân loại B. Không hấp thu toàn thân khi dùng tại mắt. An toàn trong thai kỳ.",
                "lactation": {
                    "safety": "Compatible",
                    "details": "Acyclovir không hấp thu toàn thân khi dùng tại mắt, không bài tiết vào sữa mẹ. An toàn khi cho con bú.",
                    "recommendation": "Có thể dùng khi cho con bú. An toàn, không có tác dụng phụ."
                }
            },
            "hepatic_adjustment": {
                "mild": "Không cần điều chỉnh liều",
                "moderate": "Không cần điều chỉnh liều",
                "severe": "Không cần điều chỉnh liều (ophthalmic, hấp thu tối thiểu)",
                "notes": "Acyclovir dùng tại mắt, hấp thu toàn thân tối thiểu. Không cần điều chỉnh liều ở bệnh nhân suy gan."
            },
            "overdose_management": {
                "symptoms": [
                    "Kích ứng mắt nặng",
                    "Nhìn mờ nặng"
                ],
                "antidote": "Không có antidote đặc hiệu. Rửa mắt, điều trị hỗ trợ.",
                "treatment": [
                    "Rửa mắt ngay với nước sạch hoặc nước muối sinh lý",
                    "Nếu kích ứng mắt nặng:",
                    "  - Khám mắt ngay",
                    "  - Điều trị hỗ trợ (nước mắt nhân tạo)",
                    "Theo dõi: Thị lực, dấu hiệu kích ứng mắt"
                ],
                "monitoring": "Theo dõi thị lực, dấu hiệu kích ứng mắt cho đến khi hồi phục."
            },
            "reversal_agents": None,
            "administration_instructions": {
                "ophthalmic": {
                    "preparation": "Dạng ointment 3%.",
                    "application": "Bôi mỏng vào mắt bị ảnh hưởng x 5 lần/ngày (mỗi 3-4 giờ) trong 7-10 ngày. Bôi vào túi kết mạc dưới.",
                    "timing": "5 lần/ngày cho điều trị, 3 lần/ngày cho dự phòng.",
                    "contact_lenses": "Không đeo kính áp tròng khi đang điều trị.",
                    "notes": "QUAN TRỌNG: 1) CHỈ DÙNG CHO NHIỄM TRÙNG DO VIRUS HERPES, 2) Dùng đủ liều và đủ thời gian, 3) Nhìn mờ tạm thời sau khi bôi - không lái xe ngay, 4) Tránh chạm đầu ống vào mắt."
                }
            },
            "references": {
                "primary_sources": [
                    "FDA Drug Label - Acyclovir (Zovirax)",
                    "UpToDate - Acyclovir: Drug Information",
                    "Medscape - Acyclovir Drug Reference",
                    "AAO Guidelines - Herpetic Keratitis"
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
                "requires_monitoring": ["Clinical response (reduction in redness, swelling, pain)", "Signs of eye irritation", "Visual acuity (temporary blurring after application)"]
            },
            "guideline_tags": [
                "AAO Guidelines - Herpetic Keratitis",
                "FDA Drug Information - Acyclovir Ophthalmic",
                "UpToDate - Herpetic Keratitis Treatment"
            ],
            "black_box_warnings": "Cần xem xét black box warnings",
            "reversal_agents": {
                "available": False,
                "agents": [],
            },
        },

        "Ciprofloxacin eye drops": {
            "group": "Ophthalmology - Antibiotic (Fluoroquinolone)",
            "vietnamese_name": "Ciprofloxacin nhỏ mắt, Ciloxan",
            "administration": ["Ophthalmic"],
            "indications": [
                "Viêm kết mạc do vi khuẩn (bacterial conjunctivitis)",
                "Viêm giác mạc do vi khuẩn (bacterial keratitis)",
                "Loét giác mạc do vi khuẩn (bacterial corneal ulcer)",
                "Dự phòng nhiễm trùng sau phẫu thuật mắt"
            ],
            "contraindications": [
                "Dị ứng ciprofloxacin hoặc fluoroquinolone",
                "Nhiễm trùng do virus hoặc nấm (không hiệu quả)"
            ],
            "dosage": {
                "adult_conjunctivitis": "1-2 giọt vào mắt bị ảnh hưởng mỗi 2-4 giờ trong 2 ngày đầu, sau đó mỗi 4 giờ trong 5 ngày",
                "adult_keratitis": "1-2 giọt vào mắt bị ảnh hưởng mỗi 15 phút trong 6 giờ đầu, sau đó mỗi 30 phút trong 18 giờ tiếp theo, sau đó mỗi giờ trong 24 giờ, sau đó mỗi 4 giờ",
                "adult_corneal_ulcer": "1-2 giọt vào mắt bị ảnh hưởng mỗi 15 phút trong 6 giờ đầu, sau đó mỗi 30 phút trong 18 giờ tiếp theo, sau đó mỗi giờ",
                "notes": "Ciprofloxacin là fluoroquinolone phổ rộng, hiệu quả với nhiều vi khuẩn Gram-dương và Gram-âm. Dùng thường xuyên trong giai đoạn đầu, sau đó giảm tần suất. Điều trị thường 7-14 ngày."
            },
            "renal_adjustment": {
                "normal": "Không đổi",
                "30_60": "Không đổi",
                "under_30": "Không đổi"
            },
            "side_effects": [
                "Kích ứng mắt (đỏ, rát, ngứa) - phổ biến",
                "Nhìn mờ",
                "Vị đắng trong miệng (do hấp thu toàn thân) - phổ biến",
                "Phản ứng dị ứng (phát ban, ngứa) - hiếm",
                "Nhạy cảm với ánh sáng - hiếm"
            ],
            "interactions": [
                "Không có tương tác đáng kể với thuốc khác (ophthalmic)"
            ],
            "pregnancy": "C - Thận trọng",
            "mechanism_of_action": "Ciprofloxacin là fluoroquinolone (kháng sinh phổ rộng). Ức chế DNA gyrase và topoisomerase IV của vi khuẩn, ngăn chặn sự sao chép DNA và phân chia tế bào vi khuẩn, dẫn đến tiêu diệt vi khuẩn (bactericidal). Ciprofloxacin hiệu quả với nhiều vi khuẩn Gram-dương (Staphylococcus, Streptococcus) và Gram-âm (Pseudomonas, Haemophilus, Neisseria). ĐẶC ĐIỂM: (1) Phổ rộng, hiệu quả với nhiều vi khuẩn, (2) Bactericidal (tiêu diệt vi khuẩn), (3) Dùng thường xuyên trong giai đoạn đầu, (4) Điều trị thường 7-14 ngày, (5) Vị đắng trong miệng do hấp thu toàn thân - phổ biến.",
            "monitoring": [
                "Dấu hiệu nhiễm trùng (đỏ mắt, chảy mủ, đau) - cải thiện sau 24-48 giờ",
                "Thị lực và khám mắt định kỳ",
                "Dấu hiệu kích ứng mắt (đỏ, rát, ngứa)",
                "Dấu hiệu phản ứng dị ứng (phát ban, ngứa)",
                "Dấu hiệu nhạy cảm với ánh sáng"
            ],
            "precautions": [
                "CHỈ DÙNG CHO NHIỄM TRÙNG DO VI KHUẨN - không hiệu quả với virus hoặc nấm",
                "Dùng đủ liều và đủ thời gian (thường 7-14 ngày) để tránh kháng thuốc",
                "Vị đắng trong miệng - phổ biến, do hấp thu toàn thân",
                "Kích ứng mắt - phổ biến, thường giảm sau vài ngày",
                "Thận trọng ở bệnh nhân đeo kính áp tròng (benzalkonium chloride có thể làm hỏng kính)",
                "Tránh chạm đầu lọ vào mắt hoặc bất kỳ bề mặt nào (nguy cơ nhiễm trùng)",
                "Không dùng chung với người khác (nguy cơ lây nhiễm)"
            ],
            "pharmacokinetics": {
                "half_life": "3-4 giờ (huyết tương, nếu hấp thu toàn thân), nhưng tác dụng tại mắt kéo dài",
                "onset": "Ngay lập tức",
                "duration": "2-4 giờ (dùng mỗi 2-4 giờ)",
                "protein_binding": "20-40%",
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
                    "Dị ứng ciprofloxacin hoặc fluoroquinolone",
                    "Nhiễm trùng do virus hoặc nấm - không hiệu quả"
                ],
                "tương_đối": [
                    "Bệnh nhân đeo kính áp tròng - thận trọng (benzalkonium chloride)",
                    "Có thai (category C) - thận trọng"
                ]
            },
            "pregnancy_lactation": {
                "fda_category": "C",
                "pregnancy_details": "Ciprofloxacin là thuốc phân loại C. Ciprofloxacin có thể hấp thu toàn thân và qua nhau thai. Fluoroquinolone có thể gây tổn thương sụn ở động vật. Có thể dùng khi lợi ích vượt quá nguy cơ, đặc biệt khi không có lựa chọn khác.",
                "lactation": {
                    "safety": "Compatible with Caution",
                    "details": "Ciprofloxacin có thể hấp thu toàn thân và bài tiết vào sữa mẹ. Tuy nhiên, nồng độ trong sữa mẹ thấp khi dùng tại mắt và không có báo cáo về tác dụng phụ đáng kể ở trẻ bú mẹ.",
                    "recommendation": "Có thể dùng khi cho con bú, nhưng thận trọng. Nồng độ trong sữa mẹ thấp."
                }
            },
            "hepatic_adjustment": {
                "mild": "Không cần điều chỉnh liều",
                "moderate": "Không cần điều chỉnh liều",
                "severe": "Không cần điều chỉnh liều (ophthalmic, hấp thu tối thiểu)",
                "notes": "Ciprofloxacin dùng tại mắt, hấp thu toàn thân tối thiểu. Không cần điều chỉnh liều ở bệnh nhân suy gan."
            },
            "overdose_management": {
                "symptoms": [
                    "Kích ứng mắt nặng",
                    "Đỏ mắt, đau mắt",
                    "Nhìn mờ"
                ],
                "antidote": "Không có antidote đặc hiệu. Rửa mắt, điều trị hỗ trợ.",
                "treatment": [
                    "Rửa mắt ngay với nước sạch hoặc nước muối sinh lý",
                    "Nếu kích ứng mắt nặng:",
                    "  - Khám mắt ngay",
                    "  - Điều trị hỗ trợ (nước mắt nhân tạo, thuốc chống viêm nếu cần)",
                    "Theo dõi: Thị lực, dấu hiệu viêm"
                ],
                "monitoring": "Theo dõi thị lực, dấu hiệu viêm cho đến khi hồi phục."
            },
            "reversal_agents": None,
            "administration_instructions": {
                "oral": None,
                "ophthalmic": {
                    "preparation": "Dạng dung dịch nhỏ mắt 0.3% (3 mg/ml).",
                    "application": "1-2 giọt vào mắt bị ảnh hưởng theo lịch trình (xem dosage). Nhắm mắt nhẹ 1-2 phút sau khi nhỏ. Nhấn nhẹ vào góc trong mắt (lacrimal sac) trong 1-2 phút để giảm hấp thu toàn thân.",
                    "timing": "Tùy theo chỉ định: mỗi 2-4 giờ (conjunctivitis) hoặc mỗi 15-30 phút (keratitis, corneal ulcer).",
                    "contact_lenses": "Tháo kính áp tròng trước khi nhỏ. Đợi 15 phút trước khi đeo lại.",
                    "notes": "QUAN TRỌNG: 1) CHỈ DÙNG CHO NHIỄM TRÙNG DO VI KHUẨN, 2) Dùng đủ liều và đủ thời gian (thường 7-14 ngày), 3) Vị đắng trong miệng là phổ biến, 4) Tránh chạm đầu lọ vào mắt hoặc bất kỳ bề mặt nào, 5) Không dùng chung với người khác."
                }
            },
            "references": {
                "primary_sources": [
                    "FDA Drug Label - Ciprofloxacin (Ciloxan)",
                    "UpToDate - Ciprofloxacin: Drug Information",
                    "Medscape - Ciprofloxacin Drug Reference",
                    "AAO Guidelines - Bacterial Keratitis"
                ],
                "last_updated": "2025-02-18",
                "evidence_level": "A - Dựa trên FDA drug labels, clinical guidelines, và dữ liệu lâm sàng từ nhiều nguồn"
            },
            "risk_flags": {
                "high_alert": False,
                "narrow_therapeutic_index": False,
                "bleeding_risk": False,
                "organ_toxicity": ["Tendon rupture (rare, if systemic absorption occurs)", "QT prolongation (rare, if systemic absorption occurs)"],
                "qt_prolongation": True,
                "hepatotoxicity": False,
                "nephrotoxicity": False,
                "requires_monitoring": ["Clinical response (reduction in redness, discharge, pain)", "Signs of eye irritation (increased redness, burning, itching)", "Visual acuity (temporary blurring after application)", "Signs of infection (pus, increased redness/swelling) - if no improvement"]
            },
            "guideline_tags": [
                "AAO Guidelines - Bacterial Keratitis",
                "AAO Guidelines - Bacterial Conjunctivitis",
                "FDA Drug Information - Ciprofloxacin Eye Drops",
                "UpToDate - Bacterial Eye Infections"
            ],
            "black_box_warnings": "Cần xem xét black box warnings",
            "reversal_agents": {
                "available": False,
                "agents": [],
            },
        },

        "Erythromycin eye ointment": {
            "group": "Ophthalmology - Antibiotic (Macrolide)",
            "vietnamese_name": "Erythromycin, Ilotycin",
            "administration": ["Ophthalmic"],
            "indications": [
                "Viêm kết mạc do vi khuẩn (bacterial conjunctivitis)",
                "Viêm giác mạc do vi khuẩn (bacterial keratitis)",
                "Dự phòng nhiễm trùng mắt ở trẻ sơ sinh (ophthalmia neonatorum prophylaxis)",
                "Điều trị viêm bờ mi (blepharitis) do vi khuẩn"
            ],
            "contraindications": [
                "Dị ứng erythromycin hoặc macrolide",
                "Nhiễm trùng do virus hoặc nấm (không hiệu quả)"
            ],
            "dosage": {
                "adult_conjunctivitis": "Bôi mỏng vào mắt bị ảnh hưởng x 2-4 lần/ngày trong 7-10 ngày",
                "adult_keratitis": "Bôi mỏng vào mắt bị ảnh hưởng x 4-6 lần/ngày trong 7-14 ngày",
                "neonatal_prophylaxis": "Bôi mỏng vào mắt trẻ sơ sinh x 1 lần ngay sau sinh",
                "adult_blepharitis": "Bôi mỏng lên bờ mi x 2 lần/ngày trong 2-4 tuần",
                "notes": "Erythromycin là macrolide, phổ rộng, hiệu quả với nhiều vi khuẩn Gram-dương và một số Gram-âm. Dùng 2-4 lần/ngày. Có thể gây nhìn mờ tạm thời sau khi bôi. An toàn cho trẻ sơ sinh (dự phòng ophthalmia neonatorum)."
            },
            "renal_adjustment": {
                "normal": "Không đổi",
                "30_60": "Không đổi",
                "under_30": "Không đổi"
            },
            "side_effects": [
                "Nhìn mờ tạm thời sau khi bôi - phổ biến",
                "Kích ứng mắt tại chỗ (đỏ, rát, ngứa) - phổ biến",
                "Khô mắt",
                "Phản ứng dị ứng (phát ban, ngứa) - hiếm",
                "Hấp thu toàn thân (hiếm): rối loạn tiêu hóa, rối loạn nhịp tim"
            ],
            "interactions": [
                "Không có tương tác đáng kể với thuốc khác (ophthalmic)",
                "Erythromycin đường uống: không dùng cùng lúc (tăng nguy cơ tác dụng phụ)"
            ],
            "pregnancy": "B - An toàn",
            "mechanism_of_action": "Erythromycin là macrolide, ức chế tổng hợp protein của vi khuẩn bằng cách gắn với ribosome 50S, ngăn chặn sự tổng hợp protein, dẫn đến ức chế sự nhân lên của vi khuẩn (bacteriostatic). Phổ rộng, hiệu quả với nhiều vi khuẩn Gram-dương (Staphylococcus, Streptococcus) và một số Gram-âm. ĐẶC ĐIỂM: (1) Macrolide, phổ rộng, (2) Bacteriostatic (ức chế sự nhân lên của vi khuẩn), (3) Dùng 2-4 lần/ngày, (4) Nhìn mờ tạm thời sau khi bôi - phổ biến, (5) An toàn cho trẻ sơ sinh (dự phòng ophthalmia neonatorum), (6) Kích ứng mắt phổ biến.",
            "monitoring": [
                "Đáp ứng lâm sàng (giảm đỏ, sưng, mủ) - cải thiện sau 2-3 ngày",
                "Dấu hiệu kích ứng mắt (đỏ, rát, ngứa tăng)",
                "Dấu hiệu nhiễm trùng (mủ, đỏ, sưng tăng) - nếu không cải thiện",
                "Dấu hiệu kháng thuốc (nhiễm trùng không cải thiện sau 5-7 ngày)"
            ],
            "precautions": [
                "CHỈ DÙNG CHO NHIỄM TRÙNG DO VI KHUẨN - không hiệu quả với virus hoặc nấm",
                "Dùng đủ liều và đủ thời gian (7-10 ngày) để tránh kháng thuốc",
                "Nhìn mờ tạm thời sau khi bôi - phổ biến, bệnh nhân không nên lái xe ngay sau khi bôi",
                "Kích ứng mắt - phổ biến, thường giảm sau vài ngày",
                "Tránh chạm đầu ống vào mắt hoặc bất kỳ bề mặt nào (nguy cơ nhiễm trùng)",
                "Không đeo kính áp tròng khi đang điều trị",
                "An toàn cho trẻ sơ sinh (dự phòng ophthalmia neonatorum)"
            ],
            "pharmacokinetics": {
                "half_life": "Không áp dụng (ophthalmic)",
                "onset": "Ngay lập tức",
                "duration": "4-6 giờ (dùng 2-4 lần/ngày)",
                "protein_binding": "Không áp dụng (ophthalmic)",
                "metabolism": "Chuyển hóa tại mắt",
                "clearance": "Thải trừ tại chỗ, hấp thu toàn thân tối thiểu"
            },
            "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ánh sáng. Đóng nắp kín sau khi dùng. Dùng trong 4 tuần sau khi mở.",
            "black_box_warnings": None,
            "drug_interactions": {
                "major": [],
                "moderate": [
                    {
                        "drug": "Erythromycin đường uống",
                        "mechanism": "Cả hai đều là erythromycin, tác dụng cộng dồn",
                        "effect": "Tăng nguy cơ tác dụng phụ toàn thân (rối loạn tiêu hóa, rối loạn nhịp tim)",
                        "management": "Không dùng cùng lúc. Chọn một trong hai."
                    }
                ],
                "minor": []
            },
            "contraindications": {
                "tuyệt_đối": [
                    "Dị ứng erythromycin hoặc macrolide",
                    "Nhiễm trùng do virus hoặc nấm - không hiệu quả"
                ],
                "tương_đối": [
                    "Dùng kéo dài - nguy cơ kháng thuốc",
                    "Dùng với erythromycin đường uống - tăng nguy cơ tác dụng phụ"
                ]
            },
            "pregnancy_lactation": {
                "fda_category": "B",
                "pregnancy_details": "Erythromycin là thuốc phân loại B. Không hấp thu toàn thân khi dùng tại mắt. An toàn trong thai kỳ.",
                "lactation": {
                    "safety": "Compatible",
                    "details": "Erythromycin không hấp thu toàn thân khi dùng tại mắt, không bài tiết vào sữa mẹ. An toàn khi cho con bú.",
                    "recommendation": "Có thể dùng khi cho con bú. An toàn, không có tác dụng phụ."
                }
            },
            "hepatic_adjustment": {
                "mild": "Không cần điều chỉnh liều",
                "moderate": "Không cần điều chỉnh liều",
                "severe": "Không cần điều chỉnh liều (ophthalmic, hấp thu tối thiểu)",
                "notes": "Erythromycin dùng tại mắt, hấp thu toàn thân tối thiểu. Không cần điều chỉnh liều ở bệnh nhân suy gan."
            },
            "overdose_management": {
                "symptoms": [
                    "Kích ứng mắt nặng",
                    "Nhìn mờ nặng"
                ],
                "antidote": "Không có antidote đặc hiệu. Rửa mắt, điều trị hỗ trợ.",
                "treatment": [
                    "Rửa mắt ngay với nước sạch hoặc nước muối sinh lý",
                    "Nếu kích ứng mắt nặng:",
                    "  - Khám mắt ngay",
                    "  - Điều trị hỗ trợ (nước mắt nhân tạo)",
                    "Theo dõi: Thị lực, dấu hiệu kích ứng mắt"
                ],
                "monitoring": "Theo dõi thị lực, dấu hiệu kích ứng mắt cho đến khi hồi phục."
            },
            "reversal_agents": None,
            "administration_instructions": {
                "ophthalmic": {
                    "preparation": "Dạng ointment 0.5%.",
                    "application": "Bôi mỏng vào mắt bị ảnh hưởng x 2-4 lần/ngày. Bôi vào túi kết mạc dưới.",
                    "timing": "2-4 lần/ngày cho viêm kết mạc, 4-6 lần/ngày cho viêm giác mạc.",
                    "contact_lenses": "Không đeo kính áp tròng khi đang điều trị.",
                    "notes": "QUAN TRỌNG: 1) CHỈ DÙNG CHO NHIỄM TRÙNG DO VI KHUẨN, 2) Dùng đủ liều và đủ thời gian, 3) Nhìn mờ tạm thời sau khi bôi - không lái xe ngay, 4) Tránh chạm đầu ống vào mắt, 5) An toàn cho trẻ sơ sinh."
                }
            },
            "references": {
                "primary_sources": [
                    "FDA Drug Label - Erythromycin (Ilotycin)",
                    "UpToDate - Erythromycin: Drug Information",
                    "Medscape - Erythromycin Drug Reference",
                    "AAO Guidelines - Bacterial Conjunctivitis, Keratitis, Ophthalmia Neonatorum"
                ],
                "last_updated": "2025-02-18",
                "evidence_level": "A - Dựa trên FDA drug labels, clinical guidelines, và dữ liệu lâm sàng từ nhiều nguồn"
            },
            "risk_flags": {
                "high_alert": False,
                "narrow_therapeutic_index": False,
                "bleeding_risk": False,
                "organ_toxicity": ["Antibiotic resistance (if used long-term)"],
                "qt_prolongation": False,
                "hepatotoxicity": False,
                "nephrotoxicity": False,
                "requires_monitoring": ["Clinical response (reduction in redness, discharge, pain)", "Signs of eye irritation (increased redness, burning, itching)", "Visual acuity (temporary blurring after application)", "Signs of infection (pus, increased redness/swelling) - if no improvement"]
            },
            "guideline_tags": [
                "AAO Guidelines - Bacterial Conjunctivitis",
                "AAO Guidelines - Ophthalmia Neonatorum",
                "FDA Drug Information - Erythromycin Eye Ointment",
                "UpToDate - Bacterial Eye Infections"
            ],
            "black_box_warnings": "Cần xem xét black box warnings",
            "reversal_agents": {
                "available": False,
                "agents": [],
            },
        },

        "Ganciclovir eye drops": {
            "group": "Ophthalmology - Antiviral (CMV)",
            "vietnamese_name": "Ganciclovir nhỏ mắt, Zirgan",
            "administration": ["Ophthalmic"],
            "indications": [
                "Viêm võng mạc do Cytomegalovirus (CMV retinitis) - dạng gel",
                "Viêm giác mạc do Herpes simplex (herpetic keratitis) - dạng gel",
                "Nhiễm trùng mắt do CMV ở bệnh nhân suy giảm miễn dịch"
            ],
            "contraindications": [
                "Dị ứng ganciclovir hoặc valganciclovir",
                "Dị ứng benzalkonium chloride"
            ],
            "dosage": {
                "adult_keratitis": "1 giọt gel 0.15% vào mắt bị ảnh hưởng 5 lần/ngày (mỗi 3 giờ khi thức) trong 7 ngày",
                "adult_cmv_retinitis": "1 giọt gel 0.15% vào mắt bị ảnh hưởng 5 lần/ngày (mỗi 3 giờ khi thức) trong 14-21 ngày",
                "adult_maintenance": "1 giọt gel 0.15% vào mắt bị ảnh hưởng 3 lần/ngày để duy trì",
                "notes": "Ganciclovir là thuốc kháng virus, hiệu quả với CMV và Herpes simplex. Dùng 5 lần/ngày (mỗi 3 giờ khi thức) cho điều trị ban đầu. Có thể dùng kéo dài để duy trì. Dạng gel - nhìn mờ tạm thời."
            },
            "renal_adjustment": {
                "normal": "Không đổi",
                "30_60": "Không đổi",
                "under_30": "Không đổi"
            },
            "side_effects": [
                "Kích ứng mắt (đỏ, rát, ngứa) - phổ biến",
                "Khô mắt",
                "Nhìn mờ tạm thời (do gel) - phổ biến",
                "Đau mắt",
                "Chảy nước mắt",
                "Phản ứng dị ứng (phát ban, ngứa) - hiếm",
                "Viêm mi mắt (blepharitis) - hiếm"
            ],
            "interactions": [
                "Không có tương tác đáng kể với thuốc khác (ophthalmic)"
            ],
            "pregnancy": "C - Thận trọng",
            "mechanism_of_action": "Ganciclovir là thuốc kháng virus, ức chế DNA polymerase của virus CMV và Herpes simplex. Ganciclovir được phosphoryl hóa bởi kinase của virus (UL97 cho CMV, thymidine kinase cho Herpes simplex) thành ganciclovir monophosphate, sau đó được phosphoryl hóa tiếp thành ganciclovir triphosphate. Ganciclovir triphosphate gắn với DNA polymerase của virus, ngăn chặn sự tổng hợp DNA virus, dẫn đến ức chế sự nhân lên của virus. Dẫn đến: giảm viêm võng mạc do CMV, viêm giác mạc do Herpes simplex. ĐẶC ĐIỂM: (1) Kháng virus CMV và Herpes simplex, (2) Dùng 5 lần/ngày (mỗi 3 giờ khi thức) cho điều trị ban đầu, (3) Có thể dùng kéo dài để duy trì, (4) Dạng gel - nhìn mờ tạm thời, (5) Kích ứng mắt phổ biến, (6) An toàn, ít tác dụng phụ toàn thân.",
            "monitoring": [
                "Đáp ứng lâm sàng (giảm đỏ, sưng, loét giác mạc) - cải thiện sau 3-5 ngày",
                "Dấu hiệu kích ứng mắt (đỏ, rát, ngứa tăng)",
                "Dấu hiệu nhiễm trùng (loét giác mạc tăng, mủ) - nếu không cải thiện",
                "Dấu hiệu phản ứng dị ứng (phát ban, ngứa)",
                "Thị lực và khám mắt định kỳ",
                "Dấu hiệu tái phát (loét giác mạc mới, viêm võng mạc mới)"
            ],
            "precautions": [
                "Kích ứng mắt phổ biến - thường giảm sau vài ngày",
                "Nhìn mờ tạm thời do gel - không lái xe ngay sau khi nhỏ",
                "Dùng đủ liều và đủ thời gian (7-21 ngày) để tránh tái phát",
                "Có thể dùng kéo dài để duy trì",
                "Tránh chạm đầu lọ vào mắt hoặc bất kỳ bề mặt nào (nguy cơ nhiễm trùng)",
                "Tháo kính áp tròng trước khi nhỏ (benzalkonium chloride có thể làm hỏng kính)",
                "Đợi 15 phút trước khi đeo lại kính áp tròng",
                "Không dùng chung lọ với người khác",
                "Kết hợp với ganciclovir đường uống/IV nếu có nhiễm trùng toàn thân"
            ],
            "pharmacokinetics": {
                "half_life": "Không áp dụng (ophthalmic)",
                "onset": "Ngay lập tức",
                "duration": "3 giờ (dùng 5 lần/ngày)",
                "protein_binding": "Không áp dụng (ophthalmic)",
                "metabolism": "Chuyển hóa tại mắt (kinase của virus)",
                "clearance": "Thải trừ tại chỗ, hấp thu toàn thân tối thiểu"
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
                    "Dị ứng ganciclovir hoặc valganciclovir",
                    "Dị ứng benzalkonium chloride"
                ],
                "tương_đối": [
                    "Da nhạy cảm - thận trọng, theo dõi dấu hiệu kích ứng"
                ]
            },
            "pregnancy_lactation": {
                "fda_category": "C",
                "pregnancy_details": "Ganciclovir là thuốc phân loại C. Không hấp thu toàn thân khi dùng tại mắt. An toàn trong thai kỳ.",
                "lactation": {
                    "safety": "Compatible",
                    "details": "Ganciclovir không hấp thu toàn thân khi dùng tại mắt, không bài tiết vào sữa mẹ. An toàn khi cho con bú.",
                    "recommendation": "Có thể dùng khi cho con bú. An toàn, không có tác dụng phụ."
                }
            },
            "hepatic_adjustment": {
                "mild": "Không cần điều chỉnh liều",
                "moderate": "Không cần điều chỉnh liều",
                "severe": "Không cần điều chỉnh liều (ophthalmic, hấp thu tối thiểu)",
                "notes": "Ganciclovir dùng tại mắt, hấp thu toàn thân tối thiểu. Không cần điều chỉnh liều ở bệnh nhân suy gan."
            },
            "overdose_management": {
                "symptoms": [
                    "Kích ứng mắt nặng",
                    "Đỏ mắt nặng",
                    "Nhìn mờ nặng"
                ],
                "antidote": "Không có antidote đặc hiệu. Rửa mắt, điều trị hỗ trợ.",
                "treatment": [
                    "Rửa mắt ngay với nước sạch hoặc nước muối sinh lý",
                    "Nếu kích ứng mắt nặng:",
                    "  - Khám mắt ngay",
                    "  - Điều trị hỗ trợ (nước mắt nhân tạo, thuốc chống viêm nếu cần)",
                    "Theo dõi: Thị lực, dấu hiệu kích ứng mắt"
                ],
                "monitoring": "Theo dõi thị lực, dấu hiệu kích ứng mắt cho đến khi hồi phục."
            },
            "reversal_agents": None,
            "administration_instructions": {
                "oral": None,
                "ophthalmic": {
                    "preparation": "Dạng gel nhỏ mắt 0.15%.",
                    "application": "1 giọt gel vào mắt bị ảnh hưởng 5 lần/ngày (mỗi 3 giờ khi thức) cho điều trị ban đầu, hoặc 3 lần/ngày cho duy trì. Nhắm mắt nhẹ 1-2 phút sau khi nhỏ.",
                    "timing": "5 lần/ngày (mỗi 3 giờ khi thức) cho điều trị ban đầu. 3 lần/ngày cho duy trì.",
                    "contact_lenses": "Tháo kính áp tròng trước khi nhỏ. Đợi 15 phút trước khi đeo lại.",
                    "notes": "QUAN TRỌNG: 1) Dạng gel - nhìn mờ tạm thời, không lái xe ngay sau khi nhỏ, 2) Dùng đủ liều và đủ thời gian (7-21 ngày), 3) Có thể dùng kéo dài để duy trì, 4) Tránh chạm đầu lọ vào mắt, 5) Tháo kính áp tròng trước khi nhỏ, 6) Không dùng chung lọ với người khác."
                }
            },
            "references": {
                "primary_sources": [
                    "FDA Drug Label - Ganciclovir (Zirgan)",
                    "UpToDate - Ganciclovir: Drug Information",
                    "Medscape - Ganciclovir Drug Reference",
                    "AAO Guidelines - CMV Retinitis, Herpetic Keratitis"
                ],
                "last_updated": "2025-02-18",
                "evidence_level": "A - Dựa trên FDA drug labels, clinical guidelines, và dữ liệu lâm sàng từ nhiều nguồn"
            },
            "risk_flags": {
                "high_alert": False,
                "narrow_therapeutic_index": False,
                "bleeding_risk": False,
                "organ_toxicity": ["Local eye irritation", "Temporary blurred vision (due to gel)"],
                "qt_prolongation": False,
                "hepatotoxicity": False,
                "nephrotoxicity": False,
                "requires_monitoring": ["Clinical response (reduction in redness, swelling, corneal ulcer)", "Signs of eye irritation", "Signs of infection (if not improving)", "Vision and eye examination"]
            },
            "guideline_tags": [
                "AAO Guidelines - CMV Retinitis",
                "AAO Guidelines - Herpetic Keratitis",
                "IDSA Guidelines - Cytomegalovirus Infection",
                "FDA Drug Information - Ganciclovir Eye Drops"
            ],
            "black_box_warnings": "Cần xem xét black box warnings",
            "reversal_agents": {
                "available": False,
                "agents": [],
            },
        },

        "Gentamicin eye drops": {
            "group": "Ophthalmology - Antibiotic (Aminoglycoside)",
            "vietnamese_name": "Gentamicin, Garamycin",
            "administration": ["Ophthalmic"],
            "indications": [
                "Viêm kết mạc do vi khuẩn (bacterial conjunctivitis)",
                "Viêm giác mạc do vi khuẩn (bacterial keratitis)",
                "Viêm màng bồ đào do vi khuẩn (bacterial uveitis)",
                "Dự phòng nhiễm trùng sau phẫu thuật mắt"
            ],
            "contraindications": [
                "Dị ứng gentamicin hoặc aminoglycoside",
                "Nhiễm trùng do virus hoặc nấm (không hiệu quả)"
            ],
            "dosage": {
                "adult_conjunctivitis": "1-2 giọt vào mắt bị ảnh hưởng x 4-6 lần/ngày trong 7-10 ngày",
                "adult_keratitis": "1 giọt vào mắt bị ảnh hưởng x mỗi 1-2 giờ trong ngày đầu, sau đó giảm dần",
                "adult_postop_prophylaxis": "1 giọt vào mắt phẫu thuật x 3-4 lần/ngày trong vài ngày sau phẫu thuật",
                "notes": "Gentamicin là aminoglycoside, phổ rộng, hiệu quả với nhiều vi khuẩn Gram-dương và Gram-âm. Dùng 4-6 lần/ngày cho viêm kết mạc, thường xuyên hơn cho viêm giác mạc. Tránh chạm đầu lọ vào mắt hoặc bất kỳ bề mặt nào."
            },
            "renal_adjustment": {
                "normal": "Không đổi",
                "30_60": "Không đổi",
                "under_30": "Không đổi"
            },
            "side_effects": [
                "Kích ứng mắt tại chỗ (đỏ, rát, ngứa) - phổ biến",
                "Nhìn mờ tạm thời",
                "Khô mắt",
                "Phản ứng dị ứng (phát ban, ngứa) - hiếm",
                "Hấp thu toàn thân (hiếm): độc tính thận, độc tính thần kinh thính giác"
            ],
            "interactions": [
                "Không có tương tác đáng kể với thuốc khác (ophthalmic)",
                "Gentamicin đường tiêm: không dùng cùng lúc (tăng nguy cơ độc tính)"
            ],
            "pregnancy": "C - Thận trọng",
            "mechanism_of_action": "Gentamicin là aminoglycoside, ức chế tổng hợp protein của vi khuẩn bằng cách gắn với ribosome 30S, ngăn chặn sự tổng hợp protein, dẫn đến tiêu diệt vi khuẩn (bactericidal). Phổ rộng, hiệu quả với nhiều vi khuẩn Gram-dương và Gram-âm (Staphylococcus, Streptococcus, Pseudomonas, Enterobacteriaceae). ĐẶC ĐIỂM: (1) Aminoglycoside, phổ rộng, (2) Bactericidal (tiêu diệt vi khuẩn), (3) Dùng 4-6 lần/ngày cho viêm kết mạc, thường xuyên hơn cho viêm giác mạc, (4) Kích ứng mắt phổ biến, (5) Hấp thu toàn thân hiếm nhưng có thể gây độc tính thận, độc tính thần kinh thính giác.",
            "monitoring": [
                "Đáp ứng lâm sàng (giảm đỏ, sưng, mủ) - cải thiện sau 2-3 ngày",
                "Dấu hiệu kích ứng mắt (đỏ, rát, ngứa tăng)",
                "Dấu hiệu nhiễm trùng (mủ, đỏ, sưng tăng) - nếu không cải thiện",
                "Dấu hiệu kháng thuốc (nhiễm trùng không cải thiện sau 5-7 ngày)",
                "Chức năng thận, thính giác (nếu hấp thu toàn thân, hiếm)"
            ],
            "precautions": [
                "CHỈ DÙNG CHO NHIỄM TRÙNG DO VI KHUẨN - không hiệu quả với virus hoặc nấm",
                "Dùng đủ liều và đủ thời gian (7-10 ngày) để tránh kháng thuốc",
                "Kích ứng mắt - phổ biến, thường giảm sau vài ngày",
                "Tránh chạm đầu lọ vào mắt hoặc bất kỳ bề mặt nào (nguy cơ nhiễm trùng)",
                "Tháo kính áp tròng trước khi nhỏ, đợi 15 phút trước khi đeo lại",
                "Hấp thu toàn thân hiếm nhưng có thể gây độc tính thận, độc tính thần kinh thính giác",
                "Không dùng với gentamicin đường tiêm cùng lúc"
            ],
            "pharmacokinetics": {
                "half_life": "Không áp dụng (ophthalmic)",
                "onset": "Ngay lập tức",
                "duration": "4-6 giờ (dùng 4-6 lần/ngày)",
                "protein_binding": "Không áp dụng (ophthalmic)",
                "metabolism": "Chuyển hóa tại mắt",
                "clearance": "Thải trừ tại chỗ, hấp thu toàn thân tối thiểu"
            },
            "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ánh sáng. Đóng nắp kín sau khi dùng. Dùng trong 4 tuần sau khi mở.",
            "black_box_warnings": None,
            "drug_interactions": {
                "major": [],
                "moderate": [
                    {
                        "drug": "Gentamicin đường tiêm",
                        "mechanism": "Cả hai đều là gentamicin, tác dụng cộng dồn",
                        "effect": "Tăng nguy cơ độc tính thận, độc tính thần kinh thính giác",
                        "management": "Không dùng cùng lúc. Chọn một trong hai."
                    }
                ],
                "minor": []
            },
            "contraindications": {
                "tuyệt_đối": [
                    "Dị ứng gentamicin hoặc aminoglycoside",
                    "Nhiễm trùng do virus hoặc nấm - không hiệu quả"
                ],
                "tương_đối": [
                    "Dùng kéo dài - nguy cơ kháng thuốc",
                    "Dùng với gentamicin đường tiêm - tăng nguy cơ độc tính"
                ]
            },
            "pregnancy_lactation": {
                "fda_category": "C",
                "pregnancy_details": "Gentamicin là thuốc phân loại C. Aminoglycoside có thể qua nhau thai và gây độc tính thần kinh thính giác ở thai nhi. Có thể dùng khi lợi ích vượt quá nguy cơ, đặc biệt khi không có lựa chọn khác.",
                "lactation": {
                    "safety": "Compatible with Caution",
                    "details": "Gentamicin có thể hấp thu toàn thân và bài tiết vào sữa mẹ ở nồng độ thấp. Tuy nhiên, nồng độ trong sữa mẹ thấp khi dùng tại mắt và không có báo cáo về tác dụng phụ đáng kể ở trẻ bú mẹ.",
                    "recommendation": "Có thể dùng khi cho con bú, nhưng thận trọng. Nồng độ trong sữa mẹ thấp."
                }
            },
            "hepatic_adjustment": {
                "mild": "Không cần điều chỉnh liều",
                "moderate": "Không cần điều chỉnh liều",
                "severe": "Không cần điều chỉnh liều (ophthalmic, hấp thu tối thiểu)",
                "notes": "Gentamicin dùng tại mắt, hấp thu toàn thân tối thiểu. Không cần điều chỉnh liều ở bệnh nhân suy gan."
            },
            "overdose_management": {
                "symptoms": [
                    "Kích ứng mắt nặng",
                    "Hấp thu toàn thân (hiếm): độc tính thận, độc tính thần kinh thính giác"
                ],
                "antidote": "Không có antidote đặc hiệu. Rửa mắt, điều trị hỗ trợ.",
                "treatment": [
                    "Rửa mắt ngay với nước sạch hoặc nước muối sinh lý",
                    "Nếu kích ứng mắt nặng:",
                    "  - Khám mắt ngay",
                    "  - Điều trị hỗ trợ (nước mắt nhân tạo)",
                    "Nếu hấp thu toàn thân:",
                    "  - Theo dõi chức năng thận, thính giác",
                    "  - Điều trị hỗ trợ nếu cần",
                    "Theo dõi: Thị lực, dấu hiệu kích ứng mắt, chức năng thận, thính giác"
                ],
                "monitoring": "Theo dõi thị lực, dấu hiệu kích ứng mắt, chức năng thận, thính giác (nếu hấp thu toàn thân) cho đến khi hồi phục."
            },
            "reversal_agents": None,
            "administration_instructions": {
                "ophthalmic": {
                    "preparation": "Dạng dung dịch nhỏ mắt 0.3%.",
                    "application": "1-2 giọt vào mắt bị ảnh hưởng x 4-6 lần/ngày. Nhắm mắt nhẹ 1-2 phút sau khi nhỏ. Nhấn nhẹ vào góc trong mắt (lacrimal sac) trong 1-2 phút để giảm hấp thu toàn thân.",
                    "timing": "4-6 lần/ngày cho viêm kết mạc, thường xuyên hơn cho viêm giác mạc.",
                    "contact_lenses": "Tháo kính áp tròng trước khi nhỏ. Đợi 15 phút trước khi đeo lại.",
                    "notes": "QUAN TRỌNG: 1) CHỈ DÙNG CHO NHIỄM TRÙNG DO VI KHUẨN, 2) Dùng đủ liều và đủ thời gian, 3) Kích ứng mắt phổ biến, 4) Tránh chạm đầu lọ vào mắt, 5) Không dùng với gentamicin đường tiêm cùng lúc."
                }
            },
            "references": {
                "primary_sources": [
                    "FDA Drug Label - Gentamicin (Garamycin)",
                    "UpToDate - Gentamicin: Drug Information",
                    "Medscape - Gentamicin Drug Reference",
                    "AAO Guidelines - Bacterial Conjunctivitis, Keratitis"
                ],
                "last_updated": "2025-02-18",
                "evidence_level": "A - Dựa trên FDA drug labels, clinical guidelines, và dữ liệu lâm sàng từ nhiều nguồn"
            },
            "risk_flags": {
                "high_alert": True,
                "narrow_therapeutic_index": True,
                "bleeding_risk": False,
                "organ_toxicity": ["Nephrotoxicity (if systemic absorption occurs) - CRITICAL", "Ototoxicity (if systemic absorption occurs) - CRITICAL"],
                "qt_prolongation": False,
                "hepatotoxicity": False,
                "nephrotoxicity": True,
                "requires_monitoring": ["Clinical response (reduction in redness, discharge, pain)", "Signs of eye irritation (increased redness, burning, itching)", "Visual acuity (temporary blurring after application)", "Renal function (if systemic absorption) - CRITICAL", "Hearing (if systemic absorption) - CRITICAL"]
            },
            "guideline_tags": [
                "AAO Guidelines - Bacterial Conjunctivitis",
                "AAO Guidelines - Bacterial Keratitis",
                "FDA Black Box Warning - Gentamicin and Nephrotoxicity/Ototoxicity",
                "FDA Drug Information - Gentamicin Eye Drops",
                "ISMP High Alert Medications - Aminoglycosides"
            ],
            "black_box_warnings": "Cần xem xét black box warnings",
            "reversal_agents": {
                "available": False,
                "agents": [],
            },
        },

        "Moxifloxacin eye drops": {
            "group": "Ophthalmology - Fluoroquinolone Antibiotic",
            "vietnamese_name": "Moxifloxacin, Vigamox",
            "administration": ["Ophthalmic"],
            "indications": [
                "Viêm kết mạc do vi khuẩn (bacterial conjunctivitis)",
                "Viêm giác mạc do vi khuẩn (bacterial keratitis)",
                "Dự phòng nhiễm trùng sau phẫu thuật mắt"
            ],
            "contraindications": [
                "Dị ứng moxifloxacin hoặc fluoroquinolone",
                "Nhiễm trùng do virus hoặc nấm (không hiệu quả)"
            ],
            "dosage": {
                "adult_conjunctivitis": "1 giọt vào mắt bị ảnh hưởng x 3 lần/ngày trong 7 ngày",
                "adult_keratitis": "1 giọt vào mắt bị ảnh hưởng x 3-4 lần/ngày trong 7-14 ngày",
                "adult_postop_prophylaxis": "1 giọt vào mắt phẫu thuật x 3 lần/ngày trong vài ngày sau phẫu thuật",
                "notes": "Moxifloxacin là fluoroquinolone thế hệ 4, phổ rộng, hiệu quả với nhiều vi khuẩn Gram-dương và Gram-âm. Dùng 3-4 lần/ngày. Tránh chạm đầu lọ vào mắt hoặc bất kỳ bề mặt nào."
            },
            "renal_adjustment": {
                "normal": "Không đổi",
                "30_60": "Không đổi",
                "under_30": "Không đổi"
            },
            "side_effects": [
                "Kích ứng mắt tại chỗ (đỏ, rát, ngứa) - phổ biến",
                "Nhìn mờ tạm thời",
                "Khô mắt",
                "Phản ứng dị ứng (phát ban, ngứa) - hiếm",
                "Hấp thu toàn thân (hiếm): nhạy cảm ánh sáng, rối loạn gân"
            ],
            "interactions": [
                "Không có tương tác đáng kể với thuốc khác (ophthalmic)"
            ],
            "pregnancy": "C - Thận trọng",
            "mechanism_of_action": "Moxifloxacin là fluoroquinolone thế hệ 4, ức chế DNA gyrase và topoisomerase IV của vi khuẩn, ngăn chặn sự tổng hợp DNA, dẫn đến tiêu diệt vi khuẩn (bactericidal). Phổ rộng, hiệu quả với nhiều vi khuẩn Gram-dương và Gram-âm. ĐẶC ĐIỂM: (1) Fluoroquinolone thế hệ 4, phổ rộng, (2) Bactericidal (tiêu diệt vi khuẩn), (3) Dùng 3-4 lần/ngày, (4) Kích ứng mắt phổ biến, (5) Hấp thu toàn thân hiếm nhưng có thể gây nhạy cảm ánh sáng, rối loạn gân.",
            "monitoring": [
                "Đáp ứng lâm sàng (giảm đỏ, sưng, mủ) - cải thiện sau 2-3 ngày",
                "Dấu hiệu kích ứng mắt (đỏ, rát, ngứa tăng)",
                "Dấu hiệu nhiễm trùng (mủ, đỏ, sưng tăng) - nếu không cải thiện",
                "Dấu hiệu nhạy cảm ánh sáng (nếu hấp thu toàn thân)"
            ],
            "precautions": [
                "CHỈ DÙNG CHO NHIỄM TRÙNG DO VI KHUẨN - không hiệu quả với virus hoặc nấm",
                "Dùng đủ liều và đủ thời gian (7-14 ngày) để tránh kháng thuốc",
                "Kích ứng mắt - phổ biến, thường giảm sau vài ngày",
                "Tránh chạm đầu lọ vào mắt hoặc bất kỳ bề mặt nào (nguy cơ nhiễm trùng)",
                "Tháo kính áp tròng trước khi nhỏ, đợi 15 phút trước khi đeo lại",
                "Hấp thu toàn thân hiếm nhưng có thể gây nhạy cảm ánh sáng, rối loạn gân"
            ],
            "pharmacokinetics": {
                "half_life": "Không áp dụng (ophthalmic)",
                "onset": "Ngay lập tức",
                "duration": "4-6 giờ (dùng 3-4 lần/ngày)",
                "protein_binding": "Không áp dụng (ophthalmic)",
                "metabolism": "Chuyển hóa tại mắt và gan (nếu hấp thu toàn thân)",
                "clearance": "Thải trừ tại chỗ, hấp thu toàn thân tối thiểu"
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
                    "Dị ứng moxifloxacin hoặc fluoroquinolone",
                    "Nhiễm trùng do virus hoặc nấm - không hiệu quả"
                ],
                "tương_đối": [
                    "Dùng kéo dài - nguy cơ kháng thuốc"
                ]
            },
            "pregnancy_lactation": {
                "fda_category": "C",
                "pregnancy_details": "Moxifloxacin là thuốc phân loại C. Không có nghiên cứu đầy đủ trên phụ nữ có thai. Moxifloxacin có thể hấp thu toàn thân và qua nhau thai. Có thể dùng khi lợi ích vượt quá nguy cơ, đặc biệt khi không có lựa chọn khác.",
                "lactation": {
                    "safety": "Compatible with Caution",
                    "details": "Moxifloxacin có thể hấp thu toàn thân và bài tiết vào sữa mẹ ở nồng độ thấp. Tuy nhiên, nồng độ trong sữa mẹ thấp khi dùng tại mắt và không có báo cáo về tác dụng phụ đáng kể ở trẻ bú mẹ.",
                    "recommendation": "Có thể dùng khi cho con bú, nhưng thận trọng. Nồng độ trong sữa mẹ thấp."
                }
            },
            "hepatic_adjustment": {
                "mild": "Không cần điều chỉnh liều",
                "moderate": "Không cần điều chỉnh liều",
                "severe": "Không cần điều chỉnh liều (ophthalmic, hấp thu tối thiểu)",
                "notes": "Moxifloxacin dùng tại mắt, hấp thu toàn thân tối thiểu. Không cần điều chỉnh liều ở bệnh nhân suy gan."
            },
            "overdose_management": {
                "symptoms": [
                    "Kích ứng mắt nặng",
                    "Hấp thu toàn thân (hiếm): nhạy cảm ánh sáng, rối loạn gân"
                ],
                "antidote": "Không có antidote đặc hiệu. Rửa mắt, điều trị hỗ trợ.",
                "treatment": [
                    "Rửa mắt ngay với nước sạch hoặc nước muối sinh lý",
                    "Nếu kích ứng mắt nặng:",
                    "  - Khám mắt ngay",
                    "  - Điều trị hỗ trợ (nước mắt nhân tạo)",
                    "Nếu hấp thu toàn thân:",
                    "  - Tránh ánh nắng mặt trời",
                    "  - Theo dõi dấu hiệu rối loạn gân",
                    "Theo dõi: Thị lực, dấu hiệu kích ứng mắt"
                ],
                "monitoring": "Theo dõi thị lực, dấu hiệu kích ứng mắt cho đến khi hồi phục."
            },
            "reversal_agents": None,
            "administration_instructions": {
                "ophthalmic": {
                    "preparation": "Dạng dung dịch nhỏ mắt 0.5%.",
                    "application": "1 giọt vào mắt bị ảnh hưởng x 3-4 lần/ngày. Nhắm mắt nhẹ 1-2 phút sau khi nhỏ. Nhấn nhẹ vào góc trong mắt (lacrimal sac) trong 1-2 phút để giảm hấp thu toàn thân.",
                    "timing": "3-4 lần/ngày trong 7-14 ngày tùy chỉ định.",
                    "contact_lenses": "Tháo kính áp tròng trước khi nhỏ. Đợi 15 phút trước khi đeo lại.",
                    "notes": "QUAN TRỌNG: 1) CHỈ DÙNG CHO NHIỄM TRÙNG DO VI KHUẨN, 2) Dùng đủ liều và đủ thời gian, 3) Tránh chạm đầu lọ vào mắt, 4) Kích ứng mắt phổ biến."
                }
            },
            "references": {
                "primary_sources": [
                    "FDA Drug Label - Moxifloxacin (Vigamox)",
                    "UpToDate - Moxifloxacin: Drug Information",
                    "Medscape - Moxifloxacin Drug Reference",
                    "AAO Guidelines - Bacterial Conjunctivitis, Keratitis"
                ],
                "last_updated": "2025-02-18",
                "evidence_level": "A - Dựa trên FDA drug labels, clinical guidelines, và dữ liệu lâm sàng từ nhiều nguồn"
            },
            "risk_flags": {
                "high_alert": False,
                "narrow_therapeutic_index": False,
                "bleeding_risk": False,
                "organ_toxicity": ["Tendon rupture (rare, if systemic absorption occurs)", "QT prolongation (rare, if systemic absorption occurs)"],
                "qt_prolongation": True,
                "hepatotoxicity": False,
                "nephrotoxicity": False,
                "requires_monitoring": ["Clinical response (reduction in redness, discharge, pain)", "Signs of eye irritation (increased redness, burning, itching)", "Visual acuity (temporary blurring after application)", "Signs of infection (pus, increased redness/swelling) - if no improvement"]
            },
            "guideline_tags": [
                "AAO Guidelines - Bacterial Conjunctivitis",
                "AAO Guidelines - Bacterial Keratitis",
                "FDA Drug Information - Moxifloxacin Eye Drops",
                "UpToDate - Bacterial Eye Infections"
            ],
            "black_box_warnings": "Cần xem xét black box warnings",
            "reversal_agents": {
                "available": False,
                "agents": [],
            },
        },

        "Polymyxin B/Trimethoprim eye drops": {
            "group": "Ophthalmology - Combination Antibiotic",
            "vietnamese_name": "Polymyxin B/Trimethoprim, Polytrim",
            "administration": ["Ophthalmic"],
            "indications": [
                "Viêm kết mạc do vi khuẩn (bacterial conjunctivitis)",
                "Viêm giác mạc do vi khuẩn (bacterial keratitis)",
                "Viêm bờ mi do vi khuẩn (bacterial blepharitis)",
                "Dự phòng nhiễm trùng sau phẫu thuật mắt"
            ],
            "contraindications": [
                "Dị ứng polymyxin B, trimethoprim, hoặc sulfonamide",
                "Nhiễm trùng do virus hoặc nấm (không hiệu quả)"
            ],
            "dosage": {
                "adult_conjunctivitis": "1 giọt vào mắt bị ảnh hưởng x 4 lần/ngày trong 7-10 ngày",
                "adult_keratitis": "1 giọt vào mắt bị ảnh hưởng x mỗi 1-2 giờ trong ngày đầu, sau đó giảm dần",
                "adult_blepharitis": "1 giọt vào mắt bị ảnh hưởng x 4 lần/ngày trong 7-10 ngày",
                "adult_postop_prophylaxis": "1 giọt vào mắt phẫu thuật x 3-4 lần/ngày trong vài ngày sau phẫu thuật",
                "notes": "Polymyxin B/Trimethoprim là kháng sinh kết hợp. Polymyxin B: hiệu quả với vi khuẩn Gram-âm (Pseudomonas, Enterobacteriaceae). Trimethoprim: hiệu quả với vi khuẩn Gram-dương và Gram-âm. Phổ rộng, hiệu quả với nhiều vi khuẩn. Dùng 4 lần/ngày."
            },
            "renal_adjustment": {
                "normal": "Không đổi",
                "30_60": "Không đổi",
                "under_30": "Không đổi"
            },
            "side_effects": [
                "Kích ứng mắt tại chỗ (đỏ, rát, ngứa) - phổ biến",
                "Nhìn mờ tạm thời",
                "Khô mắt",
                "Phản ứng dị ứng (phát ban, ngứa) - hiếm",
                "Hấp thu toàn thân (hiếm): độc tính thận (polymyxin B), rối loạn máu (trimethoprim)"
            ],
            "interactions": [
                "Không có tương tác đáng kể với thuốc khác (ophthalmic)",
                "Trimethoprim đường uống: không dùng cùng lúc (tăng nguy cơ tác dụng phụ)"
            ],
            "pregnancy": "C - Thận trọng",
            "mechanism_of_action": "Polymyxin B/Trimethoprim là kháng sinh kết hợp. Polymyxin B: gắn với lipopolysaccharide (LPS) trong màng ngoài của vi khuẩn Gram-âm, phá vỡ tính toàn vẹn màng tế bào, dẫn đến tiêu diệt vi khuẩn (bactericidal). Hiệu quả với vi khuẩn Gram-âm (Pseudomonas, Enterobacteriaceae). Trimethoprim: ức chế enzyme dihydrofolate reductase (DHFR), ngăn chặn sự tổng hợp tetrahydrofolate, dẫn đến ức chế sự tổng hợp DNA và protein, tiêu diệt vi khuẩn (bactericidal). Hiệu quả với vi khuẩn Gram-dương và Gram-âm. Kết hợp hai thuốc tạo phổ rộng, hiệu quả với nhiều vi khuẩn. ĐẶC ĐIỂM: (1) Kháng sinh kết hợp, phổ rộng, (2) Bactericidal (tiêu diệt vi khuẩn), (3) Dùng 4 lần/ngày, (4) Kích ứng mắt phổ biến, (5) Hấp thu toàn thân hiếm nhưng có thể gây độc tính thận (polymyxin B), rối loạn máu (trimethoprim).",
            "monitoring": [
                "Đáp ứng lâm sàng (giảm đỏ, sưng, mủ) - cải thiện sau 2-3 ngày",
                "Dấu hiệu kích ứng mắt (đỏ, rát, ngứa tăng)",
                "Dấu hiệu nhiễm trùng (mủ, đỏ, sưng tăng) - nếu không cải thiện",
                "Dấu hiệu kháng thuốc (nhiễm trùng không cải thiện sau 5-7 ngày)",
                "Chức năng thận, công thức máu (nếu hấp thu toàn thân, hiếm)"
            ],
            "precautions": [
                "CHỈ DÙNG CHO NHIỄM TRÙNG DO VI KHUẨN - không hiệu quả với virus hoặc nấm",
                "Dùng đủ liều và đủ thời gian (7-10 ngày) để tránh kháng thuốc",
                "Kích ứng mắt - phổ biến, thường giảm sau vài ngày",
                "Tránh chạm đầu lọ vào mắt hoặc bất kỳ bề mặt nào (nguy cơ nhiễm trùng)",
                "Tháo kính áp tròng trước khi nhỏ, đợi 15 phút trước khi đeo lại",
                "Hấp thu toàn thân hiếm nhưng có thể gây độc tính thận (polymyxin B), rối loạn máu (trimethoprim)",
                "Không dùng với trimethoprim đường uống cùng lúc"
            ],
            "pharmacokinetics": {
                "half_life": "Không áp dụng (ophthalmic)",
                "onset": "Ngay lập tức",
                "duration": "4-6 giờ (dùng 4 lần/ngày)",
                "protein_binding": "Không áp dụng (ophthalmic)",
                "metabolism": "Chuyển hóa tại mắt",
                "clearance": "Thải trừ tại chỗ, hấp thu toàn thân tối thiểu"
            },
            "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ánh sáng. Đóng nắp kín sau khi dùng. Dùng trong 4 tuần sau khi mở.",
            "black_box_warnings": None,
            "drug_interactions": {
                "major": [],
                "moderate": [
                    {
                        "drug": "Trimethoprim đường uống",
                        "mechanism": "Cả hai đều là trimethoprim, tác dụng cộng dồn",
                        "effect": "Tăng nguy cơ tác dụng phụ toàn thân (rối loạn máu)",
                        "management": "Không dùng cùng lúc. Chọn một trong hai."
                    }
                ],
                "minor": []
            },
            "contraindications": {
                "tuyệt_đối": [
                    "Dị ứng polymyxin B, trimethoprim, hoặc sulfonamide",
                    "Nhiễm trùng do virus hoặc nấm - không hiệu quả"
                ],
                "tương_đối": [
                    "Dùng kéo dài - nguy cơ kháng thuốc",
                    "Dùng với trimethoprim đường uống - tăng nguy cơ tác dụng phụ",
                    "Suy thận nặng - thận trọng (nguy cơ độc tính thận nếu hấp thu toàn thân)"
                ]
            },
            "pregnancy_lactation": {
                "fda_category": "C",
                "pregnancy_details": "Polymyxin B/Trimethoprim là thuốc phân loại C. Trimethoprim có thể qua nhau thai và gây tác dụng phụ ở thai nhi (dị tật bẩm sinh). Có thể dùng khi lợi ích vượt quá nguy cơ, đặc biệt khi không có lựa chọn khác.",
                "lactation": {
                    "safety": "Compatible with Caution",
                    "details": "Polymyxin B và trimethoprim có thể hấp thu toàn thân và bài tiết vào sữa mẹ ở nồng độ thấp. Tuy nhiên, nồng độ trong sữa mẹ thấp khi dùng tại mắt và không có báo cáo về tác dụng phụ đáng kể ở trẻ bú mẹ.",
                    "recommendation": "Có thể dùng khi cho con bú, nhưng thận trọng. Nồng độ trong sữa mẹ thấp."
                }
            },
            "hepatic_adjustment": {
                "mild": "Không cần điều chỉnh liều",
                "moderate": "Không cần điều chỉnh liều",
                "severe": "Không cần điều chỉnh liều (ophthalmic, hấp thu tối thiểu)",
                "notes": "Polymyxin B/Trimethoprim dùng tại mắt, hấp thu toàn thân tối thiểu. Không cần điều chỉnh liều ở bệnh nhân suy gan."
            },
            "overdose_management": {
                "symptoms": [
                    "Kích ứng mắt nặng",
                    "Hấp thu toàn thân (hiếm): độc tính thận, rối loạn máu"
                ],
                "antidote": "Không có antidote đặc hiệu. Rửa mắt, điều trị hỗ trợ.",
                "treatment": [
                    "Rửa mắt ngay với nước sạch hoặc nước muối sinh lý",
                    "Nếu kích ứng mắt nặng:",
                    "  - Khám mắt ngay",
                    "  - Điều trị hỗ trợ (nước mắt nhân tạo)",
                    "Nếu hấp thu toàn thân:",
                    "  - Theo dõi chức năng thận, công thức máu",
                    "  - Điều trị hỗ trợ nếu cần",
                    "Theo dõi: Thị lực, dấu hiệu kích ứng mắt, chức năng thận, công thức máu"
                ],
                "monitoring": "Theo dõi thị lực, dấu hiệu kích ứng mắt, chức năng thận, công thức máu (nếu hấp thu toàn thân) cho đến khi hồi phục."
            },
            "reversal_agents": None,
            "administration_instructions": {
                "ophthalmic": {
                    "preparation": "Dạng dung dịch nhỏ mắt: Polymyxin B 10,000 units/mL + Trimethoprim 1mg/mL.",
                    "application": "1 giọt vào mắt bị ảnh hưởng x 4 lần/ngày. Nhắm mắt nhẹ 1-2 phút sau khi nhỏ. Nhấn nhẹ vào góc trong mắt (lacrimal sac) trong 1-2 phút để giảm hấp thu toàn thân.",
                    "timing": "4 lần/ngày cho viêm kết mạc, thường xuyên hơn cho viêm giác mạc.",
                    "contact_lenses": "Tháo kính áp tròng trước khi nhỏ. Đợi 15 phút trước khi đeo lại.",
                    "notes": "QUAN TRỌNG: 1) CHỈ DÙNG CHO NHIỄM TRÙNG DO VI KHUẨN, 2) Dùng đủ liều và đủ thời gian, 3) Kích ứng mắt phổ biến, 4) Tránh chạm đầu lọ vào mắt, 5) Không dùng với trimethoprim đường uống cùng lúc."
                }
            },
            "references": {
                "primary_sources": [
                    "FDA Drug Label - Polymyxin B/Trimethoprim (Polytrim)",
                    "UpToDate - Polymyxin B/Trimethoprim: Drug Information",
                    "Medscape - Polymyxin B/Trimethoprim Drug Reference",
                    "AAO Guidelines - Bacterial Conjunctivitis, Keratitis"
                ],
                "last_updated": "2025-02-18",
                "evidence_level": "A - Dựa trên FDA drug labels, clinical guidelines, và dữ liệu lâm sàng từ nhiều nguồn"
            },
            "risk_flags": {
                "high_alert": False,
                "narrow_therapeutic_index": False,
                "bleeding_risk": False,
                "organ_toxicity": ["Antibiotic resistance (if used long-term)"],
                "qt_prolongation": False,
                "hepatotoxicity": False,
                "nephrotoxicity": False,
                "requires_monitoring": ["Clinical response (reduction in redness, discharge, pain)", "Signs of eye irritation (increased redness, burning, itching)", "Visual acuity (temporary blurring after application)", "Signs of infection (pus, increased redness/swelling) - if no improvement"]
            },
            "guideline_tags": [
                "AAO Guidelines - Bacterial Conjunctivitis",
                "AAO Guidelines - Bacterial Keratitis",
                "FDA Drug Information - Polymyxin B/Trimethoprim Eye Drops",
                "UpToDate - Bacterial Eye Infections"
            ]
        },

        "Tobramycin eye drops": {
            "group": "Ophthalmology - Antibiotic (Aminoglycoside)",
            "vietnamese_name": "Tobramycin nhỏ mắt, Tobrex",
            "administration": ["Ophthalmic"],
            "indications": [
                "Viêm kết mạc do vi khuẩn (bacterial conjunctivitis)",
                "Viêm giác mạc do vi khuẩn (bacterial keratitis)",
                "Loét giác mạc do vi khuẩn (bacterial corneal ulcer)",
                "Dự phòng nhiễm trùng sau phẫu thuật mắt"
            ],
            "contraindications": [
                "Dị ứng tobramycin hoặc aminoglycoside",
                "Nhiễm trùng do virus hoặc nấm (không hiệu quả)"
            ],
            "dosage": {
                "adult_conjunctivitis": "1-2 giọt vào mắt bị ảnh hưởng mỗi 4 giờ trong 7-10 ngày",
                "adult_keratitis": "1-2 giọt vào mắt bị ảnh hưởng mỗi giờ trong 24-48 giờ đầu, sau đó mỗi 4 giờ",
                "adult_corneal_ulcer": "1-2 giọt vào mắt bị ảnh hưởng mỗi giờ trong 24-48 giờ đầu, sau đó mỗi 4 giờ",
                "notes": "Tobramycin là aminoglycoside, hiệu quả với nhiều vi khuẩn Gram-âm (Pseudomonas, E. coli) và một số Gram-dương. Dùng thường xuyên trong giai đoạn đầu, sau đó giảm tần suất. Điều trị thường 7-14 ngày."
            },
            "renal_adjustment": {
                "normal": "Không đổi",
                "30_60": "Không đổi",
                "under_30": "Không đổi"
            },
            "side_effects": [
                "Kích ứng mắt (đỏ, rát, ngứa) - phổ biến",
                "Nhìn mờ",
                "Vị đắng trong miệng (do hấp thu toàn thân) - hiếm",
                "Phản ứng dị ứng (phát ban, ngứa) - hiếm",
                "Độc tính thận (nếu hấp thu toàn thân nhiều) - hiếm"
            ],
            "interactions": [
                "Không có tương tác đáng kể với thuốc khác (ophthalmic)"
            ],
            "pregnancy": "D - Thận trọng",
            "mechanism_of_action": "Tobramycin là aminoglycoside (kháng sinh). Gắn với ribosome 30S của vi khuẩn, ngăn chặn sự tổng hợp protein, dẫn đến tiêu diệt vi khuẩn (bactericidal). Tobramycin hiệu quả với nhiều vi khuẩn Gram-âm (Pseudomonas aeruginosa, E. coli, Klebsiella, Proteus) và một số Gram-dương (Staphylococcus). ĐẶC ĐIỂM: (1) Aminoglycoside, hiệu quả với nhiều vi khuẩn Gram-âm, (2) Bactericidal (tiêu diệt vi khuẩn), (3) Dùng thường xuyên trong giai đoạn đầu, (4) Điều trị thường 7-14 ngày, (5) Nguy cơ độc tính thận nếu hấp thu toàn thân nhiều.",
            "monitoring": [
                "Dấu hiệu nhiễm trùng (đỏ mắt, chảy mủ, đau) - cải thiện sau 24-48 giờ",
                "Thị lực và khám mắt định kỳ",
                "Dấu hiệu kích ứng mắt (đỏ, rát, ngứa)",
                "Dấu hiệu phản ứng dị ứng (phát ban, ngứa)",
                "Chức năng thận (nếu hấp thu toàn thân nhiều) - hiếm"
            ],
            "precautions": [
                "CHỈ DÙNG CHO NHIỄM TRÙNG DO VI KHUẨN - không hiệu quả với virus hoặc nấm",
                "Dùng đủ liều và đủ thời gian (thường 7-14 ngày) để tránh kháng thuốc",
                "Kích ứng mắt - phổ biến, thường giảm sau vài ngày",
                "Thận trọng ở bệnh nhân đeo kính áp tròng (benzalkonium chloride có thể làm hỏng kính)",
                "Tránh chạm đầu lọ vào mắt hoặc bất kỳ bề mặt nào (nguy cơ nhiễm trùng)",
                "Không dùng chung với người khác (nguy cơ lây nhiễm)"
            ],
            "pharmacokinetics": {
                "half_life": "2-3 giờ (huyết tương, nếu hấp thu toàn thân), nhưng tác dụng tại mắt kéo dài",
                "onset": "Ngay lập tức",
                "duration": "4 giờ (dùng mỗi 4 giờ)",
                "protein_binding": "<10%",
                "metabolism": "Chuyển hóa tại mắt và thận (nếu hấp thu toàn thân)",
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
                    "Dị ứng tobramycin hoặc aminoglycoside",
                    "Nhiễm trùng do virus hoặc nấm - không hiệu quả"
                ],
                "tương_đối": [
                    "Bệnh nhân đeo kính áp tròng - thận trọng (benzalkonium chloride)",
                    "Có thai (category D) - thận trọng"
                ]
            },
            "pregnancy_lactation": {
                "fda_category": "D",
                "pregnancy_details": "Tobramycin là thuốc phân loại D. Tobramycin có thể hấp thu toàn thân và qua nhau thai. Aminoglycoside có thể gây độc tính thận và thính giác ở thai nhi. Có thể dùng khi lợi ích vượt quá nguy cơ, đặc biệt khi không có lựa chọn khác.",
                "lactation": {
                    "safety": "Compatible with Caution",
                    "details": "Tobramycin có thể hấp thu toàn thân và bài tiết vào sữa mẹ. Tuy nhiên, nồng độ trong sữa mẹ thấp khi dùng tại mắt và không có báo cáo về tác dụng phụ đáng kể ở trẻ bú mẹ.",
                    "recommendation": "Có thể dùng khi cho con bú, nhưng thận trọng. Nồng độ trong sữa mẹ thấp."
                }
            },
            "hepatic_adjustment": {
                "mild": "Không cần điều chỉnh liều",
                "moderate": "Không cần điều chỉnh liều",
                "severe": "Không cần điều chỉnh liều (ophthalmic, hấp thu tối thiểu)",
                "notes": "Tobramycin dùng tại mắt, hấp thu toàn thân tối thiểu. Không cần điều chỉnh liều ở bệnh nhân suy gan."
            },
            "overdose_management": {
                "symptoms": [
                    "Kích ứng mắt nặng",
                    "Đỏ mắt, đau mắt",
                    "Nhìn mờ"
                ],
                "antidote": "Không có antidote đặc hiệu. Rửa mắt, điều trị hỗ trợ.",
                "treatment": [
                    "Rửa mắt ngay với nước sạch hoặc nước muối sinh lý",
                    "Nếu kích ứng mắt nặng:",
                    "  - Khám mắt ngay",
                    "  - Điều trị hỗ trợ (nước mắt nhân tạo, thuốc chống viêm nếu cần)",
                    "Theo dõi: Thị lực, dấu hiệu viêm"
                ],
                "monitoring": "Theo dõi thị lực, dấu hiệu viêm cho đến khi hồi phục."
            },
            "reversal_agents": None,
            "administration_instructions": {
                "oral": None,
                "ophthalmic": {
                    "preparation": "Dạng dung dịch nhỏ mắt 0.3% (3 mg/ml).",
                    "application": "1-2 giọt vào mắt bị ảnh hưởng theo lịch trình (xem dosage). Nhắm mắt nhẹ 1-2 phút sau khi nhỏ. Nhấn nhẹ vào góc trong mắt (lacrimal sac) trong 1-2 phút để giảm hấp thu toàn thân.",
                    "timing": "Tùy theo chỉ định: mỗi 4 giờ (conjunctivitis) hoặc mỗi giờ (keratitis, corneal ulcer).",
                    "contact_lenses": "Tháo kính áp tròng trước khi nhỏ. Đợi 15 phút trước khi đeo lại.",
                    "notes": "QUAN TRỌNG: 1) CHỈ DÙNG CHO NHIỄM TRÙNG DO VI KHUẨN, 2) Dùng đủ liều và đủ thời gian (thường 7-14 ngày), 3) Tránh chạm đầu lọ vào mắt hoặc bất kỳ bề mặt nào, 4) Không dùng chung với người khác."
                }
            },
            "references": {
                "primary_sources": [
                    "FDA Drug Label - Tobramycin (Tobrex)",
                    "UpToDate - Tobramycin: Drug Information",
                    "Medscape - Tobramycin Drug Reference",
                    "AAO Guidelines - Bacterial Keratitis"
                ],
                "last_updated": "2025-02-18",
                "evidence_level": "A - Dựa trên FDA drug labels, clinical guidelines, và dữ liệu lâm sàng từ nhiều nguồn"
            },
            "risk_flags": {
                "high_alert": True,
                "narrow_therapeutic_index": True,
                "bleeding_risk": False,
                "organ_toxicity": ["Nephrotoxicity (if systemic absorption occurs) - CRITICAL", "Ototoxicity (if systemic absorption occurs) - CRITICAL"],
                "qt_prolongation": False,
                "hepatotoxicity": False,
                "nephrotoxicity": True,
                "requires_monitoring": ["Clinical response (reduction in redness, discharge, pain)", "Signs of eye irritation (increased redness, burning, itching)", "Visual acuity (temporary blurring after application)", "Renal function (if systemic absorption) - CRITICAL", "Hearing (if systemic absorption) - CRITICAL"]
            },
            "guideline_tags": [
                "AAO Guidelines - Bacterial Conjunctivitis",
                "AAO Guidelines - Bacterial Keratitis",
                "FDA Black Box Warning - Tobramycin and Nephrotoxicity/Ototoxicity",
                "FDA Drug Information - Tobramycin Eye Drops",
                "ISMP High Alert Medications - Aminoglycosides"
            ],
            "black_box_warnings": "Cần xem xét black box warnings",
            "reversal_agents": {
                "available": False,
                "agents": [],
            },
        },

}

__all__ = ['ANTI_INFECTIVE_DRUGS']
