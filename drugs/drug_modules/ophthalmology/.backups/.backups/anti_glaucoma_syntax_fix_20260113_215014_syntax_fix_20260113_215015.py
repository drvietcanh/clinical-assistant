"""
Ophthalmology Drugs - Anti Glaucoma
"""
from typing import Dict, Any


ANTI_GLAUCOMA_DRUGS: Dict[str, Dict[str, Any]] = {
        "Bimatoprost": {
            "group": "Ophthalmology - Prostaglandin Analog (Glaucoma)",
            "vietnamese_name": "Bimatoprost, Lumigan",
            "administration": ["Ophthalmic"],
            "indications": [
                "Tăng nhãn áp góc mở (open-angle glaucoma)",
                "Tăng nhãn áp (ocular hypertension)",
                "Giảm nhãn áp (first-line treatment)"
            ],
            "contraindications": [
                "Dị ứng bimatoprost hoặc benzalkonium chloride",
                "Viêm màng bồ đào (uveitis) hoạt động",
                "Viêm giác mạc (keratitis) hoạt động",
                "Trẻ em <18 tuổi (thận trọng)"
            ],
            "dosage": {
                "adult_ophthalmic": "1 giọt vào mắt bị ảnh hưởng 1 lần/ngày (buổi tối)",
                "adult_eyelash": "1 giọt vào lông mi trên 1 lần/ngày (buổi tối) - off-label",
                "notes": "Bimatoprost là prostaglandin analog, tương tự latanoprost. Tác dụng mạnh, giảm nhãn áp 25-35%. Dùng buổi tối để tối ưu hiệu quả. Có thể gây thay đổi màu mắt (tăng sắc tố mống mắt) và lông mi (dài, đậm, đổi màu)."
            },
            "renal_adjustment": {
                "normal": "Không đổi",
                "30_60": "Không đổi",
                "under_30": "Không đổi"
            },
            "side_effects": [
                "Thay đổi màu mắt (tăng sắc tố mống mắt) - vĩnh viễn, phổ biến",
                "Thay đổi lông mi (dài, đậm, đổi màu) - phổ biến",
                "Đỏ mắt, kích ứng mắt",
                "Khô mắt",
                "Nhìn mờ",
                "Đau mắt",
                "Viêm màng bồ đào (hiếm)",
                "Viêm giác mạc (hiếm)",
                "Phù hoàng điểm (macular edema) - hiếm, ở bệnh nhân có tiền sử"
            ],
            "interactions": [
                "Không có tương tác đáng kể với thuốc khác (ophthalmic)"
            ],
            "pregnancy": "C - Thận trọng",
            "mechanism_of_action": "Bimatoprost là prostaglandin analog. Gắn với thụ thể prostaglandin F trên cơ trơn mống mắt và cơ thể mi, dẫn đến: (1) Tăng dẫn lưu thủy dịch qua đường uveoscleral (tăng outflow), (2) Giảm sản xuất thủy dịch (nhẹ), (3) Giảm nhãn áp. Bimatoprost tương tự latanoprost, tác dụng mạnh (giảm nhãn áp 25-35%), dùng 1 lần/ngày. ĐẶC ĐIỂM: (1) Tác dụng mạnh, giảm nhãn áp 25-35%, (2) Dùng 1 lần/ngày (buổi tối), (3) Thay đổi màu mắt (tăng sắc tố mống mắt) - vĩnh viễn, phổ biến, (4) Thay đổi lông mi (dài, đậm, đổi màu) - phổ biến, (5) Nguy cơ phù hoàng điểm ở bệnh nhân có tiền sử.",
            "monitoring": [
                "Nhãn áp (intraocular pressure - IOP) - mục tiêu: <21 mmHg",
                "Thị lực và khám mắt định kỳ",
                "Dấu hiệu thay đổi màu mắt (tăng sắc tố mống mắt)",
                "Dấu hiệu thay đổi lông mi (dài, đậm, đổi màu)",
                "Dấu hiệu viêm màng bồ đào (đỏ mắt, đau, nhìn mờ)",
                "Dấu hiệu phù hoàng điểm (giảm thị lực, nhìn mờ) - ở bệnh nhân có tiền sử"
            ],
            "precautions": [
                "Thay đổi màu mắt (tăng sắc tố mống mắt) - vĩnh viễn, phổ biến, đặc biệt ở mắt nâu/xanh",
                "Thay đổi lông mi (dài, đậm, đổi màu) - phổ biến, có thể vĩnh viễn",
                "Nguy cơ phù hoàng điểm ở bệnh nhân có tiền sử (viêm màng bồ đào, đái tháo đường, phẫu thuật mắt)",
                "CHỐNG CHỈ ĐỊNH ở viêm màng bồ đào hoạt động",
                "CHỐNG CHỈ ĐỊNH ở viêm giác mạc hoạt động",
                "Thận trọng ở trẻ em <18 tuổi",
                "Thận trọng ở bệnh nhân đeo kính áp tròng (benzalkonium chloride có thể làm hỏng kính)",
                "Dùng buổi tối để tối ưu hiệu quả",
                "Tránh chạm đầu lọ vào mắt hoặc bất kỳ bề mặt nào (nguy cơ nhiễm trùng)"
            ],
            "pharmacokinetics": {
                "half_life": "45 phút (huyết tương), nhưng tác dụng tại mắt kéo dài",
                "onset": "3-4 giờ",
                "duration": "24 giờ (dùng 1 lần/ngày)",
                "protein_binding": "88%",
                "metabolism": "Chuyển hóa tại mắt và gan (nếu hấp thu toàn thân)",
                "clearance": "Thải trừ qua nước tiểu (nếu hấp thu toàn thân)"
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
                    "Dị ứng bimatoprost hoặc benzalkonium chloride",
                    "Viêm màng bồ đào (uveitis) hoạt động - CHỐNG CHỈ ĐỊNH",
                    "Viêm giác mạc (keratitis) hoạt động - CHỐNG CHỈ ĐỊNH"
                ],
                "tương_đối": [
                    "Trẻ em <18 tuổi - thận trọng",
                    "Bệnh nhân có tiền sử viêm màng bồ đào - nguy cơ phù hoàng điểm",
                    "Bệnh nhân đái tháo đường - nguy cơ phù hoàng điểm",
                    "Bệnh nhân có tiền sử phẫu thuật mắt - nguy cơ phù hoàng điểm",
                    "Bệnh nhân đeo kính áp tròng - thận trọng (benzalkonium chloride)"
                ]
            },
            "pregnancy_lactation": {
                "fda_category": "C",
                "pregnancy_details": "Bimatoprost là thuốc phân loại C. Không có nghiên cứu đầy đủ trên phụ nữ có thai. Bimatoprost có thể hấp thu toàn thân và qua nhau thai. Có thể dùng khi lợi ích vượt quá nguy cơ, đặc biệt khi không có lựa chọn khác.",
                "lactation": {
                    "safety": "Compatible with Caution",
                    "details": "Bimatoprost có thể hấp thu toàn thân và bài tiết vào sữa mẹ ở nồng độ thấp. Tuy nhiên, nồng độ trong sữa mẹ thấp và không có báo cáo về tác dụng phụ đáng kể ở trẻ bú mẹ khi dùng tại mắt.",
                    "recommendation": "Có thể dùng khi cho con bú, nhưng thận trọng. Nồng độ trong sữa mẹ thấp."
                }
            },
            "hepatic_adjustment": {
                "mild": "Không cần điều chỉnh liều",
                "moderate": "Không cần điều chỉnh liều",
                "severe": "Không cần điều chỉnh liều (ophthalmic, hấp thu tối thiểu)",
                "notes": "Bimatoprost dùng tại mắt, hấp thu toàn thân tối thiểu. Không cần điều chỉnh liều ở bệnh nhân suy gan."
            },
            "overdose_management": {
                "symptoms": [
                    "Kích ứng mắt nặng",
                    "Nhìn mờ nặng",
                    "Đau mắt nặng"
                ],
                "antidote": "Không có antidote đặc hiệu. Rửa mắt, điều trị hỗ trợ.",
                "treatment": [
                    "Rửa mắt ngay với nước sạch hoặc nước muối sinh lý",
                    "Nếu kích ứng mắt nặng:",
                    "  - Khám mắt ngay",
                    "  - Điều trị hỗ trợ (nước mắt nhân tạo)",
                    "Theo dõi: Thị lực, nhãn áp, dấu hiệu kích ứng mắt"
                ],
                "monitoring": "Theo dõi thị lực, nhãn áp, dấu hiệu kích ứng mắt cho đến khi hồi phục."
            },
            "reversal_agents": None,
            "administration_instructions": {
                "ophthalmic": {
                    "preparation": "Dạng dung dịch nhỏ mắt 0.01% hoặc 0.03%.",
                    "application": "1 giọt vào mắt bị ảnh hưởng 1 lần/ngày (buổi tối). Nhắm mắt nhẹ 1-2 phút sau khi nhỏ. Nhấn nhẹ vào góc trong mắt (lacrimal sac) trong 1-2 phút để giảm hấp thu toàn thân.",
                    "timing": "1 lần/ngày (buổi tối) để tối ưu hiệu quả.",
                    "contact_lenses": "Tháo kính áp tròng trước khi nhỏ. Đợi 15 phút trước khi đeo lại.",
                    "notes": "QUAN TRỌNG: 1) Dùng buổi tối để tối ưu hiệu quả, 2) Thay đổi màu mắt và lông mi phổ biến, 3) Tránh chạm đầu lọ vào mắt, 4) Nguy cơ phù hoàng điểm ở bệnh nhân có tiền sử."
                }
            },
            "references": {
                "primary_sources": [
                    "FDA Drug Label - Bimatoprost (Lumigan)",
                    "UpToDate - Bimatoprost: Drug Information",
                    "Medscape - Bimatoprost Drug Reference",
                    "AAO Guidelines - Glaucoma"
                ],
                "last_updated": "2025-02-18",
                "evidence_level": "A - Dựa trên FDA drug labels, clinical guidelines, và dữ liệu lâm sàng từ nhiều nguồn"
            },
            "risk_flags": {
                "high_alert": False,
                "narrow_therapeutic_index": False,
                "bleeding_risk": False,
                "organ_toxicity": ["Permanent iris color change (increased pigmentation)", "Macular edema (rare, in patients with history)"],
                "qt_prolongation": False,
                "hepatotoxicity": False,
                "nephrotoxicity": False,
                "requires_monitoring": ["Intraocular pressure (IOP) - target <21 mmHg", "Eye examination (iris color changes, eyelash changes)", "Visual acuity", "Signs of macular edema (in patients with history)"]
            },
            "guideline_tags": [
                "AAO Guidelines - Glaucoma",
                "FDA Drug Information - Bimatoprost",
                "European Glaucoma Society Guidelines"
            ],
            "black_box_warnings": "Cần xem xét black box warnings",
            "reversal_agents": {
                "available": False,
                "agents": [],
            },
        },

        "Brimonidine": {
            "group": "Ophthalmology - Alpha-2 Adrenergic Agonist (Glaucoma)",
            "vietnamese_name": "Brimonidine, Alphagan",
            "administration": ["Ophthalmic"],
            "indications": [
                "Tăng nhãn áp góc mở (open-angle glaucoma)",
                "Tăng nhãn áp (ocular hypertension)",
                "Giảm nhãn áp (first-line hoặc bổ sung)",
                "Tăng nhãn áp góc đóng (angle-closure glaucoma) - bổ sung"
            ],
            "contraindications": [
                "Dị ứng brimonidine hoặc alpha-2 agonist",
                "Trẻ em <2 tuổi - CHỐNG CHỈ ĐỊNH (nguy cơ ức chế hệ thần kinh trung ương)",
                "Trẻ em 2-5 tuổi - thận trọng (nguy cơ ức chế hệ thần kinh trung ương)",
                "Bệnh nhân dùng MAO inhibitors - CHỐNG CHỈ ĐỊNH",
                "Bệnh tim mạch nặng không ổn định"
            ],
            "dosage": {
                "adult_ophthalmic_0.2%": "1 giọt vào mắt bị ảnh hưởng 3 lần/ngày (0.2% solution)",
                "adult_ophthalmic_0.15%": "1 giọt vào mắt bị ảnh hưởng 2-3 lần/ngày (0.15% solution)",
                "adult_ophthalmic_0.1%": "1 giọt vào mắt bị ảnh hưởng 2-3 lần/ngày (0.1% solution)",
                "notes": "Brimonidine là alpha-2 adrenergic agonist. Giảm sản xuất thủy dịch và tăng dẫn lưu thủy dịch, giảm nhãn áp 20-27%. Có thể hấp thu toàn thân và gây tác dụng phụ hệ thống (buồn ngủ, mệt mỏi, hạ huyết áp). CHỐNG CHỈ ĐỊNH ở trẻ em <2 tuổi (nguy cơ ức chế hệ thần kinh trung ương nặng)."
            },
            "renal_adjustment": {
                "normal": "Không đổi",
                "30_60": "Không cần điều chỉnh đáng kể",
                "under_30": "Không cần điều chỉnh đáng kể"
            },
            "side_effects": [
                "Kích ứng mắt (đỏ, rát, ngứa) - phổ biến",
                "Nhìn mờ",
                "Khô mắt",
                "Dị ứng mắt (allergic conjunctivitis) - phổ biến sau vài tháng sử dụng",
                "Hấp thu toàn thân: buồn ngủ, mệt mỏi - phổ biến",
                "Hấp thu toàn thân: hạ huyết áp, nhịp chậm - hiếm",
                "Hấp thu toàn thân: ức chế hệ thần kinh trung ương (trẻ em) - nguy hiểm",
                "Đau đầu",
                "Chóng mặt"
            ],
            "interactions": [
                "MAO inhibitors: CHỐNG CHỈ ĐỊNH - tăng nguy cơ tăng huyết áp nặng",
                "Thuốc hạ huyết áp: tăng nguy cơ hạ huyết áp",
                "Thuốc an thần, thuốc ngủ: tăng nguy cơ buồn ngủ, mệt mỏi",
                "Thuốc ức chế hệ thần kinh trung ương: tăng nguy cơ ức chế hệ thần kinh trung ương"
            ],
            "pregnancy": "B - An toàn",
            "mechanism_of_action": "Brimonidine là alpha-2 adrenergic receptor agonist. Kích thích alpha-2 receptors trong cơ thể mi (ciliary body) và màng bồ đào (uvea), dẫn đến: (1) Giảm sản xuất thủy dịch (ức chế cơ thể mi), (2) Tăng dẫn lưu thủy dịch qua đường uveoscleral (tăng outflow), (3) Giảm nhãn áp. Brimonidine cũng có tác dụng bảo vệ thần kinh (neuroprotective) - bảo vệ tế bào hạch võng mạc. ĐẶC ĐIỂM: (1) Giảm nhãn áp 20-27%, (2) Dùng 2-3 lần/ngày, (3) Có thể hấp thu toàn thân và gây buồn ngủ, mệt mỏi, (4) CHỐNG CHỈ ĐỊNH ở trẻ em <2 tuổi (nguy cơ ức chế hệ thần kinh trung ương nặng), (5) Dị ứng mắt phổ biến sau vài tháng sử dụng, (6) CHỐNG CHỈ ĐỊNH với MAO inhibitors, (7) Tác dụng bảo vệ thần kinh (neuroprotective).",
            "monitoring": [
                "Nhãn áp (intraocular pressure - IOP) - mục tiêu: <21 mmHg",
                "Thị lực và khám mắt định kỳ",
                "Dấu hiệu kích ứng mắt (đỏ, rát, ngứa)",
                "Dấu hiệu dị ứng mắt (đỏ, ngứa, chảy nước mắt tăng) - sau vài tháng sử dụng",
                "Dấu hiệu hấp thu toàn thân: buồn ngủ, mệt mỏi, hạ huyết áp",
                "Ở trẻ em: dấu hiệu ức chế hệ thần kinh trung ương (buồn ngủ nặng, hôn mê) - NGUY HIỂM"
            ],
            "precautions": [
                "CHỐNG CHỈ ĐỊNH ở trẻ em <2 tuổi - nguy cơ ức chế hệ thần kinh trung ương nặng, hôn mê",
                "Thận trọng ở trẻ em 2-5 tuổi - nguy cơ ức chế hệ thần kinh trung ương",
                "CHỐNG CHỈ ĐỊNH với MAO inhibitors - tăng nguy cơ tăng huyết áp nặng",
                "Buồn ngủ, mệt mỏi - phổ biến, bệnh nhân không nên lái xe hoặc vận hành máy móc",
                "Dị ứng mắt - phổ biến sau vài tháng sử dụng, có thể cần ngừng thuốc",
                "Hấp thu toàn thân - có thể gây hạ huyết áp, nhịp chậm",
                "Thận trọng ở bệnh nhân dùng thuốc hạ huyết áp",
                "Thận trọng ở bệnh nhân dùng thuốc an thần, thuốc ngủ",
                "Tránh chạm đầu lọ vào mắt hoặc bất kỳ bề mặt nào (nguy cơ nhiễm trùng)"
            ],
            "pharmacokinetics": {
                "half_life": "2 giờ (huyết tương), nhưng tác dụng tại mắt kéo dài",
                "onset": "1-2 giờ",
                "duration": "8-12 giờ (dùng 2-3 lần/ngày)",
                "protein_binding": "29%",
                "metabolism": "Gan (CYP2D6, UGT1A4)",
                "clearance": "Gan, thận (bài tiết qua nước tiểu)"
            },
            "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ánh sáng. Đóng nắp kín sau khi dùng. Dùng trong 4 tuần sau khi mở.",
            "black_box_warnings": "CHỐNG CHỈ ĐỊNH ở trẻ em <2 tuổi. Nguy cơ ức chế hệ thần kinh trung ương nặng, hôn mê, có thể tử vong. CHỐNG CHỈ ĐỊNH với MAO inhibitors.",
            "drug_interactions": {
                "major": [
                    {
                        "drug": "MAO Inhibitors (Phenelzine, Tranylcypromine, Isocarboxazid, Selegiline)",
                        "mechanism": "Ức chế MAO, tăng nồng độ catecholamine, tác dụng cộng dồn với alpha-2 agonist",
                        "effect": "Tăng nguy cơ tăng huyết áp nặng, đột quỵ, nhồi máu cơ tim, tử vong",
                        "management": "CHỐNG CHỈ ĐỊNH tuyệt đối. KHÔNG được dùng đồng thời. Cách xa ít nhất 14 ngày sau khi ngừng MAO inhibitor."
                    }
                ],
                "moderate": [
                    {
                        "drug": "Thuốc hạ huyết áp (ACE inhibitors, ARBs, Beta-blockers, Diuretics)",
                        "mechanism": "Tác dụng hạ huyết áp cộng dồn",
                        "effect": "Tăng nguy cơ hạ huyết áp nặng",
                        "management": "Thận trọng. Theo dõi huyết áp sát."
                    },
                    {
                        "drug": "Thuốc an thần, thuốc ngủ (Benzodiazepines, Opioids, Alcohol)",
                        "mechanism": "Tác dụng ức chế hệ thần kinh trung ương cộng dồn",
                        "effect": "Tăng nguy cơ buồn ngủ, mệt mỏi, ức chế hệ thần kinh trung ương",
                        "management": "Thận trọng. Bệnh nhân không nên lái xe hoặc vận hành máy móc."
                    }
                ],
                "minor": []
            },
            "contraindications": {
                "tuyệt_đối": [
                    "Dị ứng brimonidine hoặc alpha-2 agonist",
                    "Trẻ em <2 tuổi - CHỐNG CHỈ ĐỊNH (nguy cơ ức chế hệ thần kinh trung ương nặng, hôn mê)",
                    "Dùng với MAO inhibitors - CHỐNG CHỈ ĐỊNH (nguy cơ tăng huyết áp nặng)"
                ],
                "tương_đối": [
                    "Trẻ em 2-5 tuổi - thận trọng (nguy cơ ức chế hệ thần kinh trung ương)",
                    "Bệnh tim mạch nặng không ổn định - thận trọng",
                    "Dùng với thuốc hạ huyết áp - tăng nguy cơ hạ huyết áp",
                    "Dùng với thuốc an thần, thuốc ngủ - tăng nguy cơ buồn ngủ"
                ]
            },
            "pregnancy_lactation": {
                "fda_category": "B",
                "pregnancy_details": "Brimonidine là thuốc phân loại B. Không có nghiên cứu đầy đủ trên phụ nữ có thai. Brimonidine có thể hấp thu toàn thân và qua nhau thai. Có thể dùng khi lợi ích vượt quá nguy cơ.",
                "lactation": {
                    "safety": "Compatible with Caution",
                    "details": "Brimonidine có thể hấp thu toàn thân và bài tiết vào sữa mẹ ở nồng độ thấp. Tuy nhiên, nồng độ trong sữa mẹ thấp và không có báo cáo về tác dụng phụ đáng kể ở trẻ bú mẹ khi dùng tại mắt.",
                    "recommendation": "Có thể dùng khi cho con bú, nhưng thận trọng. Nồng độ trong sữa mẹ thấp."
                }
            },
            "hepatic_adjustment": {
                "mild": "Không cần điều chỉnh liều",
                "moderate": "Thận trọng. Chuyển hóa qua gan có thể giảm, tăng nồng độ brimonidine và nguy cơ tác dụng phụ.",
                "severe": "Thận trọng. Chuyển hóa qua gan giảm đáng kể, tăng nồng độ brimonidine và nguy cơ tác dụng phụ nặng.",
                "notes": "Brimonidine chuyển hóa qua gan (CYP2D6, UGT1A4). Suy gan có thể làm giảm chuyển hóa, tăng nồng độ và nguy cơ tác dụng phụ."
            },
            "overdose_management": {
                "symptoms": [
                    "Kích ứng mắt nặng",
                    "Hấp thu toàn thân: buồn ngủ nặng, hôn mê - NGUY HIỂM",
                    "Hấp thu toàn thân: hạ huyết áp nặng, nhịp chậm",
                    "Hấp thu toàn thân: ức chế hệ thần kinh trung ương nặng (đặc biệt ở trẻ em)"
                ],
                "antidote": "Không có antidote đặc hiệu. Điều trị hỗ trợ. Atipamezole (alpha-2 antagonist) có thể đối kháng tác dụng.",
                "treatment": [
                    "Rửa mắt ngay với nước sạch hoặc nước muối sinh lý",
                    "Nếu hấp thu toàn thân nặng:",
                    "  - Theo dõi dấu hiệu sinh tồn liên tục",
                    "  - Hỗ trợ hô hấp nếu cần",
                    "  - Hỗ trợ tuần hoàn nếu hạ huyết áp nặng",
                    "  - Atipamezole (nếu có) để đối kháng alpha-2",
                    "Nếu ức chế hệ thần kinh trung ương nặng:",
                    "  - Hỗ trợ hô hấp, tuần hoàn",
                    "  - Theo dõi sát trong ICU nếu cần",
                    "Theo dõi: Dấu hiệu sinh tồn, tình trạng thần kinh, huyết áp, nhịp tim"
                ],
                "monitoring": "Theo dõi dấu hiệu sinh tồn, tình trạng thần kinh, huyết áp, nhịp tim cho đến khi hồi phục. Theo dõi lâu hơn nếu có biến chứng (ức chế hệ thần kinh trung ương nặng)."
            },
            "reversal_agents": {
                "available": True,
                "agents": [
                    {
                        "agent": "Atipamezole",
                        "mechanism": "Alpha-2 antagonist, đối kháng tác dụng alpha-2 của brimonidine",
                        "indication": "Tác dụng phụ toàn thân nặng do brimonidine (buồn ngủ nặng, hạ huyết áp)",
                        "dose": "Theo phác đồ, thường 50-200mcg/kg IM hoặc IV"
                    }
                ],
                "notes": "Atipamezole đối kháng tác dụng alpha-2 của brimonidine cho tác dụng phụ toàn thân nặng."
            },
            "administration_instructions": {
                "ophthalmic": {
                    "preparation": "Dạng dung dịch nhỏ mắt 0.1%, 0.15%, hoặc 0.2%.",
                    "application": "1 giọt vào mắt bị ảnh hưởng 2-3 lần/ngày. Nhắm mắt nhẹ 1-2 phút sau khi nhỏ. Nhấn nhẹ vào góc trong mắt (lacrimal sac) trong 1-2 phút để giảm hấp thu toàn thân.",
                    "timing": "2-3 lần/ngày tùy theo nồng độ và chỉ định.",
                    "contact_lenses": "Tháo kính áp tròng trước khi nhỏ. Đợi 15 phút trước khi đeo lại.",
                    "notes": "QUAN TRỌNG: 1) CHỐNG CHỈ ĐỊNH ở trẻ em <2 tuổi, 2) CHỐNG CHỈ ĐỊNH với MAO inhibitors, 3) Buồn ngủ, mệt mỏi phổ biến - không lái xe, 4) Dị ứng mắt phổ biến sau vài tháng, 5) Tránh chạm đầu lọ vào mắt."
                }
            },
            "references": {
                "primary_sources": [
                    "FDA Drug Label - Brimonidine (Alphagan)",
                    "UpToDate - Brimonidine: Drug Information",
                    "Medscape - Brimonidine Drug Reference",
                    "AAO Guidelines - Glaucoma"
                ],
                "last_updated": "2025-02-18",
                "evidence_level": "A - Dựa trên FDA drug labels, clinical guidelines, và dữ liệu lâm sàng từ nhiều nguồn"
            },
            "risk_flags": {
                "high_alert": True,
                "narrow_therapeutic_index": False,
                "bleeding_risk": False,
                "organ_toxicity": ["CNS depression (especially in children <2 years)", "Hypotension", "Bradycardia"],
                "qt_prolongation": False,
                "hepatotoxicity": False,
                "nephrotoxicity": False,
                "requires_monitoring": ["Intraocular pressure (IOP) - target <21 mmHg", "Signs of CNS depression (especially in children <2 years) - CRITICAL", "Blood pressure", "Heart rate", "Signs of allergic conjunctivitis (after months of use)"]
            },
            "guideline_tags": [
                "AAO Guidelines - Glaucoma",
                "FDA Black Box Warning - Brimonidine and CNS Depression in Children",
                "FDA Drug Information - Brimonidine Ophthalmic"
            ]
        },

        "Brinzolamide": {
            "group": "Ophthalmology - Carbonic Anhydrase Inhibitor (Glaucoma)",
            "vietnamese_name": "Brinzolamide, Azopt",
            "administration": ["Ophthalmic"],
            "indications": [
                "Tăng nhãn áp góc mở (open-angle glaucoma)",
                "Tăng nhãn áp (ocular hypertension)",
                "Tăng nhãn áp góc đóng (angle-closure glaucoma) - bổ sung",
                "Kết hợp với thuốc khác để giảm nhãn áp"
            ],
            "contraindications": [
                "Dị ứng brinzolamide hoặc sulfonamide",
                "Suy thận nặng (CrCl <30)",
                "Bệnh gan nặng",
                "Toan chuyển hóa nặng"
            ],
            "dosage": {
                "adult_ophthalmic": "1 giọt vào mắt bị ảnh hưởng 3 lần/ngày",
                "notes": "Brinzolamide là carbonic anhydrase inhibitor tại chỗ. Giảm sản xuất thủy dịch, giảm nhãn áp 15-20%. Có thể dùng kết hợp với thuốc khác. Nguy cơ toan chuyển hóa nếu dùng với carbonic anhydrase inhibitor đường uống (acetazolamide)."
            },
            "renal_adjustment": {
                "normal": "Không đổi",
                "30_60": "Thận trọng, theo dõi chức năng thận",
                "under_30": "CHỐNG CHỈ ĐỊNH hoặc dùng rất thận trọng"
            },
            "side_effects": [
                "Kích ứng mắt (đỏ, rát, ngứa) - phổ biến",
                "Nhìn mờ",
                "Vị đắng trong miệng (do hấp thu toàn thân) - phổ biến",
                "Khô mắt",
                "Đau mắt",
                "Toan chuyển hóa (nếu dùng với carbonic anhydrase inhibitor đường uống)",
                "Dị ứng sulfonamide (hiếm nhưng nghiêm trọng)"
            ],
            "interactions": [
                "Acetazolamide (carbonic anhydrase inhibitor đường uống): tăng nguy cơ toan chuyển hóa",
                "Dorzolamide (carbonic anhydrase inhibitor tại chỗ): tăng nguy cơ toan chuyển hóa"
            ],
            "pregnancy": "C - Thận trọng",
            "mechanism_of_action": "Brinzolamide là carbonic anhydrase inhibitor tại chỗ. Ức chế enzyme carbonic anhydrase trong cơ thể mi (ciliary body), ngăn chặn chuyển đổi CO2 và H2O thành HCO3- và H+, dẫn đến giảm sản xuất thủy dịch và giảm nhãn áp. Brinzolamide ức chế cả carbonic anhydrase II (trong cơ thể mi) và carbonic anhydrase IV (trong màng tế bào). ĐẶC ĐIỂM: (1) Giảm sản xuất thủy dịch (giảm nhãn áp 15-20%), (2) Dùng 3 lần/ngày, (3) Có thể dùng kết hợp với thuốc khác, (4) Nguy cơ toan chuyển hóa nếu dùng với carbonic anhydrase inhibitor đường uống (acetazolamide), (5) Vị đắng trong miệng do hấp thu toàn thân - phổ biến, (6) CHỐNG CHỈ ĐỊNH ở suy thận nặng (CrCl <30).",
            "monitoring": [
                "Nhãn áp (intraocular pressure - IOP) - mục tiêu: <21 mmHg",
                "Thị lực và khám mắt định kỳ",
                "Dấu hiệu kích ứng mắt (đỏ, rát, ngứa)",
                "Chức năng thận (creatinine, eGFR) - nếu dùng kéo dài hoặc có nguy cơ",
                "Acid-base balance (nếu dùng với carbonic anhydrase inhibitor đường uống)",
                "Dấu hiệu dị ứng sulfonamide (phát ban, khó thở)"
            ],
            "precautions": [
                "CHỐNG CHỈ ĐỊNH ở suy thận nặng (CrCl <30)",
                "CHỐNG CHỈ ĐỊNH ở bệnh gan nặng",
                "CHỐNG CHỈ ĐỊNH ở toan chuyển hóa nặng",
                "TRÁNH DÙNG với carbonic anhydrase inhibitor đường uống (acetazolamide) - tăng nguy cơ toan chuyển hóa",
                "Vị đắng trong miệng - phổ biến, do hấp thu toàn thân",
                "Kích ứng mắt - phổ biến, thường giảm sau vài ngày",
                "Thận trọng ở bệnh nhân dị ứng sulfonamide",
                "Thận trọng ở bệnh nhân đeo kính áp tròng (benzalkonium chloride có thể làm hỏng kính)",
                "Tránh chạm đầu lọ vào mắt hoặc bất kỳ bề mặt nào (nguy cơ nhiễm trùng)"
            ],
            "pharmacokinetics": {
                "half_life": "111 ngày (trong hồng cầu), nhưng tác dụng tại mắt ngắn hơn",
                "onset": "2 giờ",
                "duration": "8-12 giờ (dùng 3 lần/ngày)",
                "protein_binding": "60%",
                "metabolism": "Chuyển hóa tại mắt và gan (nếu hấp thu toàn thân)",
                "clearance": "Thải trừ qua thận (nếu hấp thu toàn thân)"
            },
            "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ánh sáng. Đóng nắp kín sau khi dùng.",
            "black_box_warnings": None,
            "drug_interactions": {
                "major": [
                    {
                        "drug": "Acetazolamide (carbonic anhydrase inhibitor đường uống)",
                        "mechanism": "Cả hai đều ức chế carbonic anhydrase, tác dụng cộng dồn",
                        "effect": "Tăng nguy cơ toan chuyển hóa nặng, rối loạn điện giải",
                        "management": "TRÁNH DÙNG CHUNG. Nếu bắt buộc, theo dõi acid-base balance và điện giải chặt chẽ."
                    },
                    {
                        "drug": "Dorzolamide (carbonic anhydrase inhibitor tại chỗ)",
                        "mechanism": "Cả hai đều ức chế carbonic anhydrase, tác dụng cộng dồn",
                        "effect": "Tăng nguy cơ toan chuyển hóa",
                        "management": "TRÁNH DÙNG CHUNG. Chọn một trong hai."
                    }
                ],
                "moderate": [],
                "minor": []
            },
            "contraindications": {
                "tuyệt_đối": [
                    "Dị ứng brinzolamide hoặc sulfonamide",
                    "Suy thận nặng (CrCl <30) - CHỐNG CHỈ ĐỊNH",
                    "Bệnh gan nặng - CHỐNG CHỈ ĐỊNH",
                    "Toan chuyển hóa nặng - CHỐNG CHỈ ĐỊNH"
                ],
                "tương_đối": [
                    "Suy thận (CrCl 30-60) - thận trọng, theo dõi chức năng thận",
                    "Bệnh gan nhẹ đến trung bình - thận trọng",
                    "Dùng với carbonic anhydrase inhibitor đường uống - tăng nguy cơ toan chuyển hóa",
                    "Bệnh nhân dị ứng sulfonamide - thận trọng",
                    "Bệnh nhân đeo kính áp tròng - thận trọng (benzalkonium chloride)"
                ]
            },
            "pregnancy_lactation": {
                "fda_category": "C",
                "pregnancy_details": "Brinzolamide là thuốc phân loại C. Không có nghiên cứu đầy đủ trên phụ nữ có thai. Brinzolamide có thể hấp thu toàn thân và qua nhau thai. Có thể dùng khi lợi ích vượt quá nguy cơ, đặc biệt khi không có lựa chọn khác.",
                "lactation": {
                    "safety": "Compatible with Caution",
                    "details": "Brinzolamide có thể hấp thu toàn thân và bài tiết vào sữa mẹ ở nồng độ thấp. Tuy nhiên, nồng độ trong sữa mẹ thấp và không có báo cáo về tác dụng phụ đáng kể ở trẻ bú mẹ khi dùng tại mắt.",
                    "recommendation": "Có thể dùng khi cho con bú, nhưng thận trọng. Nồng độ trong sữa mẹ thấp."
                }
            },
            "hepatic_adjustment": {
                "mild": "Không cần điều chỉnh liều",
                "moderate": "Thận trọng. Brinzolamide chuyển hóa qua gan, có thể tích lũy ở suy gan.",
                "severe": "CHỐNG CHỈ ĐỊNH. Brinzolamide chuyển hóa qua gan, tích lũy ở suy gan nặng.",
                "notes": "Brinzolamide chuyển hóa qua gan. Suy gan nặng có thể làm tích lũy brinzolamide, tăng nguy cơ tác dụng phụ. CHỐNG CHỈ ĐỊNH ở suy gan nặng."
            },
            "overdose_management": {
                "symptoms": [
                    "Kích ứng mắt nặng",
                    "Toan chuyển hóa (nếu hấp thu toàn thân)",
                    "Rối loạn điện giải"
                ],
                "antidote": "Không có antidote đặc hiệu. Rửa mắt, điều trị hỗ trợ.",
                "treatment": [
                    "Rửa mắt ngay với nước sạch hoặc nước muối sinh lý",
                    "Nếu kích ứng mắt nặng:",
                    "  - Khám mắt ngay",
                    "  - Điều trị hỗ trợ (nước mắt nhân tạo, thuốc chống viêm nếu cần)",
                    "Nếu toan chuyển hóa (nếu hấp thu toàn thân):",
                    "  - Điều chỉnh acid-base balance",
                    "  - Điều chỉnh điện giải",
                    "Theo dõi: Thị lực, nhãn áp, acid-base balance, điện giải"
                ],
                "monitoring": "Theo dõi thị lực, nhãn áp, acid-base balance, điện giải (nếu có hấp thu toàn thân) cho đến khi hồi phục."
            },
            "reversal_agents": None,
            "administration_instructions": {
                "oral": None,
                "ophthalmic": {
                    "preparation": "Dạng dung dịch nhỏ mắt 1% (10 mg/ml).",
                    "application": "1 giọt vào mắt bị ảnh hưởng 3 lần/ngày. Nhắm mắt nhẹ 1-2 phút sau khi nhỏ. Nhấn nhẹ vào góc trong mắt (lacrimal sac) trong 1-2 phút để giảm hấp thu toàn thân.",
                    "timing": "3 lần/ngày (sáng, trưa, tối).",
                    "contact_lenses": "Tháo kính áp tròng trước khi nhỏ. Đợi 15 phút trước khi đeo lại.",
                    "notes": "QUAN TRỌNG: 1) Dùng 3 lần/ngày, 2) TRÁNH DÙNG với carbonic anhydrase inhibitor đường uống (acetazolamide), 3) CHỐNG CHỈ ĐỊNH ở suy thận nặng (CrCl <30), 4) Vị đắng trong miệng là phổ biến, 5) Tránh chạm đầu lọ vào mắt hoặc bất kỳ bề mặt nào."
                }
            },
            "references": {
                "primary_sources": [
                    "FDA Drug Label - Brinzolamide (Azopt)",
                    "UpToDate - Brinzolamide: Drug Information",
                    "Medscape - Brinzolamide Drug Reference",
                    "Goodman & Gilman's The Pharmacological Basis of Therapeutics (14th ed)"
                ],
                "last_updated": "2025-02-18",
                "evidence_level": "A - Dựa trên FDA drug labels, clinical guidelines, và dữ liệu lâm sàng từ nhiều nguồn"
            },
            "risk_flags": {
                "high_alert": False,
                "narrow_therapeutic_index": False,
                "bleeding_risk": False,
                "organ_toxicity": ["Metabolic acidosis (if systemic absorption)", "Hepatotoxicity (contraindicated in severe hepatic impairment)"],
                "qt_prolongation": False,
                "hepatotoxicity": True,
                "nephrotoxicity": False,
                "requires_monitoring": ["Intraocular pressure (IOP)", "Renal function (CrCl) - contraindicated if CrCl <30", "Hepatic function - contraindicated in severe impairment", "Electrolytes (if systemic absorption)"]
            },
            "guideline_tags": [
                "AAO Guidelines - Glaucoma",
                "FDA Drug Information - Brinzolamide",
                "European Glaucoma Society Guidelines"
            ],
            "black_box_warnings": "Cần xem xét black box warnings",
            "reversal_agents": {
                "available": False,
                "agents": [],
            },
        },

        "Dorzolamide": {
            "group": "Ophthalmology - Carbonic Anhydrase Inhibitor (Glaucoma)",
            "vietnamese_name": "Dorzolamide, Trusopt",
            "administration": ["Ophthalmic"],
            "indications": [
                "Tăng nhãn áp góc mở (open-angle glaucoma)",
                "Tăng nhãn áp (ocular hypertension)",
                "Tăng nhãn áp góc đóng (angle-closure glaucoma) - bổ sung",
                "Kết hợp với thuốc khác để giảm nhãn áp"
            ],
            "contraindications": [
                "Dị ứng dorzolamide hoặc sulfonamide",
                "Suy thận nặng (CrCl <30)",
                "Bệnh gan nặng",
                "Toan chuyển hóa nặng"
            ],
            "dosage": {
                "adult_ophthalmic": "1 giọt vào mắt bị ảnh hưởng 3 lần/ngày",
                "adult_combination_timolol": "1 giọt vào mắt bị ảnh hưởng 2 lần/ngày (kết hợp với timolol)",
                "notes": "Dorzolamide là carbonic anhydrase inhibitor tại chỗ, tương tự brinzolamide. Giảm sản xuất thủy dịch, giảm nhãn áp 15-20%. Có thể dùng kết hợp với thuốc khác. Nguy cơ toan chuyển hóa nếu dùng với carbonic anhydrase inhibitor đường uống (acetazolamide)."
            },
            "renal_adjustment": {
                "normal": "Không đổi",
                "30_60": "Thận trọng, theo dõi chức năng thận",
                "under_30": "CHỐNG CHỈ ĐỊNH hoặc dùng rất thận trọng"
            },
            "side_effects": [
                "Kích ứng mắt (đỏ, rát, ngứa, châm chích) - phổ biến",
                "Nhìn mờ",
                "Vị đắng trong miệng (do hấp thu toàn thân) - phổ biến",
                "Khô mắt",
                "Đau mắt",
                "Toan chuyển hóa (nếu dùng với carbonic anhydrase inhibitor đường uống)",
                "Dị ứng sulfonamide (hiếm nhưng nghiêm trọng)",
                "Viêm kết mạc (conjunctivitis) - hiếm"
            ],
            "interactions": [
                "Acetazolamide (carbonic anhydrase inhibitor đường uống): tăng nguy cơ toan chuyển hóa",
                "Brinzolamide (carbonic anhydrase inhibitor tại chỗ): tăng nguy cơ toan chuyển hóa"
            ],
            "pregnancy": "C - Thận trọng",
            "mechanism_of_action": "Dorzolamide là carbonic anhydrase inhibitor tại chỗ. Ức chế enzyme carbonic anhydrase trong cơ thể mi (ciliary body), ngăn chặn chuyển đổi CO2 và H2O thành HCO3- và H+, dẫn đến giảm sản xuất thủy dịch và giảm nhãn áp. Dorzolamide ức chế carbonic anhydrase II (trong cơ thể mi). Tương tự brinzolamide nhưng có thể gây kích ứng mắt nhiều hơn. ĐẶC ĐIỂM: (1) Giảm sản xuất thủy dịch (giảm nhãn áp 15-20%), (2) Dùng 3 lần/ngày, (3) Có thể dùng kết hợp với thuốc khác, (4) Nguy cơ toan chuyển hóa nếu dùng với carbonic anhydrase inhibitor đường uống (acetazolamide), (5) Vị đắng trong miệng do hấp thu toàn thân - phổ biến, (6) CHỐNG CHỈ ĐỊNH ở suy thận nặng (CrCl <30), (7) Kích ứng mắt phổ biến hơn brinzolamide.",
            "monitoring": [
                "Nhãn áp (intraocular pressure - IOP) - mục tiêu: <21 mmHg",
                "Thị lực và khám mắt định kỳ",
                "Dấu hiệu kích ứng mắt (đỏ, rát, ngứa, châm chích)",
                "Chức năng thận (creatinine, eGFR) - nếu dùng kéo dài hoặc có nguy cơ",
                "Acid-base balance (nếu dùng với carbonic anhydrase inhibitor đường uống)",
                "Dấu hiệu dị ứng sulfonamide (phát ban, khó thở)"
            ],
            "precautions": [
                "CHỐNG CHỈ ĐỊNH ở suy thận nặng (CrCl <30)",
                "CHỐNG CHỈ ĐỊNH ở bệnh gan nặng",
                "CHỐNG CHỈ ĐỊNH ở toan chuyển hóa nặng",
                "TRÁNH DÙNG với carbonic anhydrase inhibitor đường uống (acetazolamide) - tăng nguy cơ toan chuyển hóa",
                "Kích ứng mắt - phổ biến, có thể giảm sau vài tuần",
                "Vị đắng trong miệng - phổ biến, do hấp thu toàn thân",
                "Thận trọng ở bệnh nhân dị ứng sulfonamide",
                "Tránh chạm đầu lọ vào mắt hoặc bất kỳ bề mặt nào (nguy cơ nhiễm trùng)"
            ],
            "pharmacokinetics": {
                "half_life": "Không áp dụng (ophthalmic)",
                "onset": "2 giờ",
                "duration": "8-12 giờ (dùng 3 lần/ngày)",
                "protein_binding": "Không áp dụng (ophthalmic)",
                "metabolism": "Chuyển hóa tại mắt và gan (nếu hấp thu toàn thân)",
                "clearance": "Thải trừ tại chỗ, hấp thu toàn thân tối thiểu"
            },
            "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ánh sáng. Đóng nắp kín sau khi dùng. Dùng trong 4 tuần sau khi mở.",
            "black_box_warnings": None,
            "drug_interactions": {
                "major": [
                    {
                        "drug": "Acetazolamide (Carbonic Anhydrase Inhibitor đường uống)",
                        "mechanism": "Cả hai đều ức chế carbonic anhydrase, tác dụng cộng dồn",
                        "effect": "Tăng nguy cơ toan chuyển hóa nặng, suy thận",
                        "management": "TRÁNH DÙNG CHUNG. Nếu bắt buộc, theo dõi acid-base balance sát."
                    },
                    {
                        "drug": "Brinzolamide (Carbonic Anhydrase Inhibitor tại chỗ)",
                        "mechanism": "Cả hai đều ức chế carbonic anhydrase, tác dụng cộng dồn",
                        "effect": "Tăng nguy cơ toan chuyển hóa",
                        "management": "TRÁNH DÙNG CHUNG. Chọn một trong hai."
                    }
                ],
                "moderate": [],
                "minor": []
            },
            "contraindications": {
                "tuyệt_đối": [
                    "Dị ứng dorzolamide hoặc sulfonamide",
                    "Suy thận nặng (CrCl <30 mL/min) - CHỐNG CHỈ ĐỊNH",
                    "Bệnh gan nặng - CHỐNG CHỈ ĐỊNH",
                    "Toan chuyển hóa nặng - CHỐNG CHỈ ĐỊNH"
                ],
                "tương_đối": [
                    "Suy thận trung bình (CrCl 30-60 mL/min) - thận trọng, theo dõi chức năng thận",
                    "Bệnh nhân dị ứng sulfonamide - thận trọng",
                    "Dùng với carbonic anhydrase inhibitor đường uống - tăng nguy cơ toan chuyển hóa"
                ]
            },
            "pregnancy_lactation": {
                "fda_category": "C",
                "pregnancy_details": "Dorzolamide là thuốc phân loại C. Không có nghiên cứu đầy đủ trên phụ nữ có thai. Dorzolamide có thể hấp thu toàn thân và qua nhau thai. Carbonic anhydrase inhibitor có thể gây dị tật bẩm sinh ở động vật. Có thể dùng khi lợi ích vượt quá nguy cơ, đặc biệt khi không có lựa chọn khác.",
                "lactation": {
                    "safety": "Compatible with Caution",
                    "details": "Dorzolamide có thể hấp thu toàn thân và bài tiết vào sữa mẹ ở nồng độ thấp. Tuy nhiên, nồng độ trong sữa mẹ thấp khi dùng tại mắt và không có báo cáo về tác dụng phụ đáng kể ở trẻ bú mẹ.",
                    "recommendation": "Có thể dùng khi cho con bú, nhưng thận trọng. Nồng độ trong sữa mẹ thấp."
                }
            },
            "hepatic_adjustment": {
                "mild": "Không cần điều chỉnh liều",
                "moderate": "Thận trọng. Chuyển hóa qua gan có thể giảm, tăng nồng độ dorzolamide và nguy cơ tác dụng phụ.",
                "severe": "CHỐNG CHỈ ĐỊNH. Chuyển hóa qua gan giảm đáng kể, tăng nguy cơ bệnh gan và tác dụng phụ nặng.",
                "notes": "Dorzolamide chuyển hóa qua gan. Suy gan có thể làm giảm chuyển hóa, tăng nồng độ và nguy cơ bệnh gan, tác dụng phụ nặng."
            },
            "overdose_management": {
                "symptoms": [
                    "Kích ứng mắt nặng",
                    "Hấp thu toàn thân: toan chuyển hóa nặng - NGUY HIỂM",
                    "Hấp thu toàn thân: suy thận cấp - NGUY HIỂM"
                ],
                "antidote": "Không có antidote đặc hiệu. Điều trị hỗ trợ. Bicarbonate để điều chỉnh toan chuyển hóa.",
                "treatment": [
                    "Rửa mắt ngay với nước sạch hoặc nước muối sinh lý",
                    "Nếu hấp thu toàn thân nặng:",
                    "  - Nếu toan chuyển hóa nặng:",
                    "    - Bicarbonate IV để điều chỉnh pH",
                    "    - Theo dõi acid-base balance",
                    "  - Nếu suy thận cấp:",
                    "    - Hỗ trợ huyết động",
                    "    - Lọc máu nếu cần",
                    "  - Theo dõi chức năng thận, acid-base balance",
                    "Theo dõi: Dấu hiệu sinh tồn, chức năng thận, acid-base balance"
                ],
                "monitoring": "Theo dõi dấu hiệu sinh tồn, chức năng thận, acid-base balance cho đến khi hồi phục. Theo dõi lâu hơn nếu có biến chứng (toan chuyển hóa, suy thận cấp)."
            },
            "reversal_agents": None,
            "administration_instructions": {
                "ophthalmic": {
                    "preparation": "Dạng dung dịch nhỏ mắt 2%.",
                    "application": "1 giọt vào mắt bị ảnh hưởng 3 lần/ngày. Nhắm mắt nhẹ 1-2 phút sau khi nhỏ. Nhấn nhẹ vào góc trong mắt (lacrimal sac) trong 1-2 phút để giảm hấp thu toàn thân.",
                    "timing": "3 lần/ngày. Có thể dùng kết hợp với timolol (2 lần/ngày).",
                    "contact_lenses": "Tháo kính áp tròng trước khi nhỏ. Đợi 15 phút trước khi đeo lại.",
                    "notes": "QUAN TRỌNG: 1) CHỐNG CHỈ ĐỊNH ở suy thận nặng, 2) TRÁNH DÙNG với carbonic anhydrase inhibitor đường uống, 3) Kích ứng mắt phổ biến, 4) Vị đắng trong miệng phổ biến."
                }
            },
            "references": {
                "primary_sources": [
                    "FDA Drug Label - Dorzolamide (Trusopt)",
                    "UpToDate - Dorzolamide: Drug Information",
                    "Medscape - Dorzolamide Drug Reference",
                    "AAO Guidelines - Glaucoma"
                ],
                "last_updated": "2025-02-18",
                "evidence_level": "A - Dựa trên FDA drug labels, clinical guidelines, và dữ liệu lâm sàng từ nhiều nguồn"
            },
            "risk_flags": {
                "high_alert": True,
                "narrow_therapeutic_index": False,
                "bleeding_risk": False,
                "organ_toxicity": ["Metabolic acidosis (if used with oral CAI) - CRITICAL", "Renal failure (if used with oral CAI or in renal impairment) - CRITICAL"],
                "qt_prolongation": False,
                "hepatotoxicity": False,
                "nephrotoxicity": True,
                "requires_monitoring": ["IOP (target <21 mmHg)", "Vision and periodic eye exams", "Signs of eye irritation (redness, burning, itching, stinging)", "Renal function (creatinine, eGFR) if used long-term or at risk - CRITICAL", "Acid-base balance if used with oral CAI - CRITICAL", "Signs of sulfonamide allergy (rash, difficulty breathing)"]
            },
            "guideline_tags": [
                "AAO Guidelines - Glaucoma",
                "FDA Drug Information - Dorzolamide",
                "FDA Black Box Warning - Dorzolamide and Renal Impairment",
                "UpToDate - Glaucoma Treatment"
            ],
            "black_box_warnings": "Cần xem xét black box warnings",
            "reversal_agents": {
                "available": False,
                "agents": [],
            },
        },

        "Latanoprost": {
            "group": "Ophthalmology - Prostaglandin Analog (Glaucoma)",
            "vietnamese_name": "Latanoprost, Xalatan",
            "administration": ["Ophthalmic"],
            "indications": [
                "Tăng nhãn áp góc mở (open-angle glaucoma)",
                "Tăng nhãn áp (ocular hypertension)",
                "Giảm nhãn áp (first-line treatment)"
            ],
            "contraindications": [
                "Dị ứng latanoprost hoặc benzalkonium chloride",
                "Viêm màng bồ đào (uveitis) hoạt động",
                "Viêm giác mạc (keratitis) hoạt động",
                "Trẻ em <18 tuổi (thận trọng)"
            ],
            "dosage": {
                "adult_ophthalmic": "1 giọt vào mắt bị ảnh hưởng 1 lần/ngày (buổi tối)",
                "notes": "Latanoprost là thuốc first-line cho tăng nhãn áp. Tác dụng mạnh, giảm nhãn áp 25-35%. Dùng buổi tối để tối ưu hiệu quả. Có thể gây thay đổi màu mắt (tăng sắc tố mống mắt) và lông mi (dài, đậm, đổi màu)."
            },
            "renal_adjustment": {
                "normal": "Không đổi",
                "30_60": "Không đổi",
                "under_30": "Không đổi"
            },
            "side_effects": [
                "Thay đổi màu mắt (tăng sắc tố mống mắt) - vĩnh viễn, phổ biến",
                "Thay đổi lông mi (dài, đậm, đổi màu) - phổ biến",
                "Đỏ mắt, kích ứng mắt",
                "Khô mắt",
                "Nhìn mờ",
                "Đau mắt",
                "Viêm màng bồ đào (hiếm)",
                "Viêm giác mạc (hiếm)",
                "Phù hoàng điểm (macular edema) - hiếm, ở bệnh nhân có tiền sử"
            ],
            "interactions": [
                "Không có tương tác đáng kể với thuốc khác (ophthalmic)"
            ],
            ',
        "pregnancy": "C - Thận trọng",
        ',
            "mechanism_of_action": "Latanoprost là prostaglandin F2-alpha (PGF2α) analog. Gắn với thụ thể prostaglandin F trên cơ trơn mống mắt và cơ thể mi, dẫn đến: (1) Tăng dẫn lưu thủy dịch qua đường uveoscleral (tăng outflow), (2) Giảm sản xuất thủy dịch (nhẹ), (3) Giảm nhãn áp. Latanoprost là thuốc first-line cho tăng nhãn áp, tác dụng mạnh (giảm nhãn áp 25-35%), dùng 1 lần/ngày. ĐẶC ĐIỂM: (1) Tác dụng mạnh, giảm nhãn áp 25-35%, (2) Dùng 1 lần/ngày (buổi tối), (3) Thay đổi màu mắt (tăng sắc tố mống mắt) - vĩnh viễn, phổ biến, (4) Thay đổi lông mi (dài, đậm, đổi màu) - phổ biến, (5) Nguy cơ phù hoàng điểm ở bệnh nhân có tiền sử (viêm màng bồ đào, đái tháo đường, phẫu thuật mắt).",
            "monitoring": [
                "Nhãn áp (intraocular pressure - IOP) - mục tiêu: <21 mmHg",
                "Thị lực và khám mắt định kỳ",
                "Dấu hiệu thay đổi màu mắt (tăng sắc tố mống mắt)",
                "Dấu hiệu thay đổi lông mi (dài, đậm, đổi màu)",
                "Dấu hiệu viêm màng bồ đào (đỏ mắt, đau, nhìn mờ)",
                "Dấu hiệu phù hoàng điểm (giảm thị lực, nhìn mờ) - ở bệnh nhân có tiền sử"
            ],
            "precautions": [
                "Thay đổi màu mắt (tăng sắc tố mống mắt) - vĩnh viễn, phổ biến, đặc biệt ở mắt nâu/xanh",
                "Thay đổi lông mi (dài, đậm, đổi màu) - phổ biến, có thể vĩnh viễn",
                "Nguy cơ phù hoàng điểm ở bệnh nhân có tiền sử (viêm màng bồ đào, đái tháo đường, phẫu thuật mắt)",
                "CHỐNG CHỈ ĐỊNH ở viêm màng bồ đào hoạt động",
                "CHỐNG CHỈ ĐỊNH ở viêm giác mạc hoạt động",
                "Thận trọng ở trẻ em <18 tuổi",
                "Thận trọng ở bệnh nhân đeo kính áp tròng (benzalkonium chloride có thể làm hỏng kính)",
                "Dùng buổi tối để tối ưu hiệu quả",
                "Tránh chạm đầu lọ vào mắt hoặc bất kỳ bề mặt nào (nguy cơ nhiễm trùng)"
            ],
            "pharmacokinetics": {
                "half_life": "17 phút (huyết tương), nhưng tác dụng tại mắt kéo dài",
                "onset": "3-4 giờ",
                "duration": "24 giờ (dùng 1 lần/ngày)",
                "protein_binding": "Không áp dụng (ophthalmic)",
                "metabolism": "Chuyển hóa tại mắt và gan (nếu hấp thu toàn thân)",
                "clearance": "Thải trừ qua nước tiểu (nếu hấp thu toàn thân)"
            },
            "storage": "Bảo quản trong tủ lạnh (2-8°C) trước khi mở. Sau khi mở: bảo quản ở nhiệt độ phòng (15-30°C), tránh ánh sáng. Dùng trong 4 tuần sau khi mở.",
            "black_box_warnings": None,
            "drug_interactions": {
                "major": [],
                "moderate": [],
                "minor": []
            },
            "contraindications": {
                "tuyệt_đối": [
                    "Dị ứng latanoprost hoặc benzalkonium chloride",
                    "Viêm màng bồ đào (uveitis) hoạt động - CHỐNG CHỈ ĐỊNH",
                    "Viêm giác mạc (keratitis) hoạt động - CHỐNG CHỈ ĐỊNH"
                ],
                "tương_đối": [
                    "Trẻ em <18 tuổi - thận trọng",
                    "Bệnh nhân có tiền sử viêm màng bồ đào - nguy cơ phù hoàng điểm",
                    "Bệnh nhân đái tháo đường - nguy cơ phù hoàng điểm",
                    "Bệnh nhân có tiền sử phẫu thuật mắt - nguy cơ phù hoàng điểm",
                    "Bệnh nhân đeo kính áp tròng - thận trọng (benzalkonium chloride)"
                ]
            },
            "pregnancy_lactation": {
                "fda_category": "C",
                "pregnancy_details": "Latanoprost là thuốc phân loại C. Không có nghiên cứu đầy đủ trên phụ nữ có thai. Latanoprost có thể hấp thu toàn thân và qua nhau thai. Có thể dùng khi lợi ích vượt quá nguy cơ, đặc biệt khi không có lựa chọn khác.",
                "lactation": {
                    "safety": "Compatible with Caution",
                    "details": "Latanoprost có thể hấp thu toàn thân và bài tiết vào sữa mẹ ở nồng độ thấp. Tuy nhiên, nồng độ trong sữa mẹ thấp và không có báo cáo về tác dụng phụ đáng kể ở trẻ bú mẹ khi dùng tại mắt.",
                    "recommendation": "Có thể dùng khi cho con bú, nhưng thận trọng. Nồng độ trong sữa mẹ thấp."
                }
            },
            "hepatic_adjustment": {
                "mild": "Không cần điều chỉnh liều",
                "moderate": "Không cần điều chỉnh liều",
                "severe": "Không cần điều chỉnh liều (ophthalmic, hấp thu tối thiểu)",
                "notes": "Latanoprost dùng tại mắt, hấp thu toàn thân tối thiểu. Không cần điều chỉnh liều ở bệnh nhân suy gan."
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
                    "Theo dõi: Thị lực, nhãn áp, dấu hiệu viêm"
                ],
                "monitoring": "Theo dõi thị lực, nhãn áp, dấu hiệu viêm cho đến khi hồi phục."
            },
            "reversal_agents": None,
            "administration_instructions": {
                "oral": None,
                "ophthalmic": {
                    "preparation": "Dạng dung dịch nhỏ mắt 0.005% (50 mcg/ml).",
                    "application": "1 giọt vào mắt bị ảnh hưởng 1 lần/ngày (buổi tối). Nhắm mắt nhẹ 1-2 phút sau khi nhỏ. Nhấn nhẹ vào góc trong mắt (lacrimal sac) trong 1-2 phút để giảm hấp thu toàn thân.",
                    "timing": "Buổi tối để tối ưu hiệu quả.",
                    "contact_lenses": "Tháo kính áp tròng trước khi nhỏ. Đợi 15 phút trước khi đeo lại.",
                    "notes": "QUAN TRỌNG: 1) Dùng 1 lần/ngày (buổi tối), 2) Tránh chạm đầu lọ vào mắt hoặc bất kỳ bề mặt nào, 3) Thay đổi màu mắt và lông mi là phổ biến và có thể vĩnh viễn, 4) Bảo quản trong tủ lạnh trước khi mở, 5) Dùng trong 4 tuần sau khi mở."
                }
            },
            "references": {
                "primary_sources": [
                    "FDA Drug Label - Latanoprost (Xalatan)",
                    "UpToDate - Latanoprost: Drug Information",
                    "Medscape - Latanoprost Drug Reference",
                    "Goodman & Gilman's The Pharmacological Basis of Therapeutics (14th ed)"
                ],
                "last_updated": "2025-02-18",
                "evidence_level": "A - Dựa trên FDA drug labels, clinical guidelines, và dữ liệu lâm sàng từ nhiều nguồn"
            },
            "risk_flags": {
                "high_alert": False,
                "narrow_therapeutic_index": False,
                "bleeding_risk": False,
                "organ_toxicity": ["Iris color change (permanent) - common", "Macular edema (rare, in patients with history)"],
                "qt_prolongation": False,
                "hepatotoxicity": False,
                "nephrotoxicity": False,
                "requires_monitoring": ["IOP (target <21 mmHg)", "Vision and periodic eye exams", "Iris color changes (permanent) - common", "Eyelash changes (longer, darker, color change) - common", "Signs of eye irritation (redness, burning)", "Signs of macular edema (rare, in patients with history)"]
            },
            "guideline_tags": [
                "AAO Guidelines - Glaucoma",
                "FDA Drug Information - Latanoprost",
                "UpToDate - Glaucoma Treatment"
            ],
            "black_box_warnings": "Cần xem xét black box warnings",
            "reversal_agents": {
                "available": False,
                "agents": [],
            },
        },

        "Pilocarpine eye drops": {
            "group": "Ophthalmology - Miotic (Pupil Constriction, Glaucoma)",
            "vietnamese_name": "Pilocarpine nhỏ mắt, Isopto Carpine",
            "administration": ["Ophthalmic"],
            "indications": [
                "Tăng nhãn áp góc đóng (angle-closure glaucoma) - cấp cứu",
                "Tăng nhãn áp góc mở (open-angle glaucoma) - bổ sung",
                "Co đồng tử để khám mắt (pupil constriction for eye examination)",
                "Điều trị tăng nhãn áp cấp tính (acute glaucoma)"
            ],
            "contraindications": [
                "Dị ứng pilocarpine hoặc cholinergic",
                "Bệnh nhân có tiền sử viêm màng bồ đào (uveitis) - thận trọng",
                "Bệnh nhân có tiền sử bong võng mạc (retinal detachment) - thận trọng"
            ],
            "dosage": {
                "adult_acute_glaucoma": "1-2 giọt vào mắt bị ảnh hưởng mỗi 15 phút trong 1 giờ đầu, sau đó mỗi giờ trong 4 giờ, sau đó mỗi 6 giờ",
                "adult_chronic_glaucoma": "1-2 giọt vào mắt bị ảnh hưởng 3-4 lần/ngày",
                "adult_ophthalmic_1%": "1-2 giọt vào mắt cần khám",
                "adult_ophthalmic_2%": "1-2 giọt vào mắt cần khám",
                "notes": "Pilocarpine là cholinergic (muscarinic agonist), co đồng tử và giảm nhãn áp. Dùng thường xuyên trong tăng nhãn áp cấp tính. Tác dụng nhanh (10-30 phút), kéo dài 4-8 giờ. Nguy cơ nhìn mờ do co đồng tử."
            },
            "renal_adjustment": {
                "normal": "Không đổi",
                "30_60": "Không đổi",
                "under_30": "Không đổi"
            },
            "side_effects": [
                "Nhìn mờ (do co đồng tử) - phổ biến, kéo dài 4-8 giờ",
                "Nhạy cảm với ánh sáng (do co đồng tử) - phổ biến",
                "Kích ứng mắt (đỏ, rát, ngứa) - phổ biến",
                "Đau mắt",
                "Đau đầu",
                "Hấp thu toàn thân: buồn nôn, nôn, tiêu chảy - hiếm",
                "Hấp thu toàn thân: co thắt phế quản (hen) - hiếm",
                "Hấp thu toàn thân: nhịp chậm - hiếm",
                "Phản ứng dị ứng - hiếm"
            ],
            "interactions": [
                "Anticholinergic đường uống: đối kháng tác dụng của pilocarpine",
                "Beta-blocker: có thể tăng hiệu quả giảm nhãn áp"
            ],
            "pregnancy": "C - Thận trọng",
            "mechanism_of_action": "Pilocarpine là cholinergic (muscarinic receptor agonist). Kích hoạt muscarinic receptors trên cơ vòng mống mắt (sphincter pupillae) và cơ thể mi (ciliary muscle), dẫn đến: (1) Co đồng tử (miosis) - cơ vòng mống mắt co, (2) Co cơ thể mi - tăng dẫn lưu thủy dịch qua trabecular meshwork, giảm nhãn áp. Dẫn đến: co đồng tử và giảm nhãn áp. Pilocarpine tác dụng nhanh (10-30 phút), kéo dài 4-8 giờ. ĐẶC ĐIỂM: (1) Cholinergic, co đồng tử và giảm nhãn áp, (2) Tác dụng nhanh (10-30 phút), kéo dài 4-8 giờ, (3) Dùng thường xuyên trong tăng nhãn áp cấp tính, (4) Nhìn mờ do co đồng tử - phổ biến, kéo dài 4-8 giờ, (5) Có thể hấp thu toàn thân và gây tác dụng phụ (buồn nôn, nôn, co thắt phế quản, nhịp chậm).",
            "monitoring": [
                "Nhãn áp (intraocular pressure - IOP) - QUAN TRỌNG: kiểm tra trước và sau khi dùng",
                "Dấu hiệu co đồng tử (miosis) - bình thường",
                "Thị lực - nhìn mờ kéo dài 4-8 giờ là bình thường",
                "Dấu hiệu nhạy cảm với ánh sáng - bình thường",
                "Dấu hiệu kích ứng mắt (đỏ, rát, ngứa)",
                "Dấu hiệu hấp thu toàn thân (buồn nôn, nôn, co thắt phế quản, nhịp chậm) - hiếm"
            ],
            "precautions": [
                "Nhìn mờ kéo dài 4-8 giờ - bệnh nhân không nên lái xe hoặc vận hành máy móc",
                "Nhạy cảm với ánh sáng kéo dài 4-8 giờ - bệnh nhân nên đeo kính râm",
                "Kích ứng mắt - phổ biến, thường giảm sau vài ngày",
                "Có thể hấp thu toàn thân và gây tác dụng phụ (buồn nôn, nôn, co thắt phế quản, nhịp chậm) - hiếm",
                "Thận trọng ở bệnh nhân hen phế quản (nguy cơ co thắt phế quản)",
                "Thận trọng ở bệnh nhân có tiền sử viêm màng bồ đào (có thể làm nặng)",
                "Thận trọng ở bệnh nhân có tiền sử bong võng mạc (có thể làm nặng)",
                "Thận trọng ở bệnh nhân đeo kính áp tròng (benzalkonium chloride có thể làm hỏng kính)",
                "Tránh chạm đầu lọ vào mắt hoặc bất kỳ bề mặt nào (nguy cơ nhiễm trùng)"
            ],
            "pharmacokinetics": {
                "half_life": "1-2 giờ (huyết tương, nếu hấp thu toàn thân), nhưng tác dụng tại mắt kéo dài",
                "onset": "10-30 phút",
                "duration": "4-8 giờ",
                "protein_binding": "Không rõ",
                "metabolism": "Chuyển hóa tại mắt và gan (nếu hấp thu toàn thân)",
                "clearance": "Thải trừ qua thận (nếu hấp thu toàn thân)"
            },
            "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ánh sáng. Đóng nắp kín sau khi dùng. Dùng trong 4 tuần sau khi mở.",
            "black_box_warnings": None,
            "drug_interactions": {
                "major": [
                    {
                        "drug": "Anticholinergic đường uống (Atropine, Scopolamine, Oxybutynin)",
                        "mechanism": "Đối kháng tác dụng cholinergic của pilocarpine",
                        "effect": "Giảm hiệu quả giảm nhãn áp của pilocarpine",
                        "management": "Thận trọng. Có thể cần tăng liều pilocarpine hoặc tránh dùng anticholinergic."
                    }
                ],
                "moderate": [
                    {
                        "drug": "Beta-blocker (Timolol, Betaxolol)",
                        "mechanism": "Tác dụng hiệp đồng giảm nhãn áp",
                        "effect": "Tăng hiệu quả giảm nhãn áp",
                        "management": "Có thể dùng kết hợp, nhưng theo dõi nhãn áp chặt chẽ."
                    }
                ],
                "minor": []
            },
            "contraindications": {
                "tuyệt_đối": [
                    "Dị ứng pilocarpine hoặc cholinergic"
                ],
                "tương_đối": [
                    "Bệnh nhân có tiền sử viêm màng bồ đào - thận trọng, có thể làm nặng",
                    "Bệnh nhân có tiền sử bong võng mạc - thận trọng, có thể làm nặng",
                    "Bệnh nhân hen phế quản - thận trọng, nguy cơ co thắt phế quản",
                    "Bệnh nhân đeo kính áp tròng - thận trọng (benzalkonium chloride)",
                    "Có thai (category C) - thận trọng"
                ]
            },
            "contraindications_detail": {
                "tuyệt_đối": [
                    "Dị ứng pilocarpine hoặc cholinergic"
                ],
                "tương_đối": [
                    "Bệnh nhân có tiền sử viêm màng bồ đào - thận trọng, có thể làm nặng",
                    "Bệnh nhân có tiền sử bong võng mạc - thận trọng, có thể làm nặng",
                    "Bệnh nhân hen phế quản - thận trọng, nguy cơ co thắt phế quản",
                    "Bệnh nhân đeo kính áp tròng - thận trọng (benzalkonium chloride)",
                    "Có thai (category C) - thận trọng"
                ]
            },
            "pregnancy_lactation": {
                "fda_category": "C",
                "pregnancy_details": "Pilocarpine là thuốc phân loại C. Pilocarpine có thể hấp thu toàn thân và qua nhau thai. Cholinergic có thể gây tác dụng phụ ở thai nhi. Có thể dùng khi lợi ích vượt quá nguy cơ, đặc biệt khi không có lựa chọn khác.",
                "lactation": {
                    "safety": "Compatible with Caution",
                    "details": "Pilocarpine có thể hấp thu toàn thân và bài tiết vào sữa mẹ. Tuy nhiên, nồng độ trong sữa mẹ thấp khi dùng tại mắt và không có báo cáo về tác dụng phụ đáng kể ở trẻ bú mẹ.",
                    "recommendation": "Có thể dùng khi cho con bú, nhưng thận trọng. Nồng độ trong sữa mẹ thấp."
                }
            },
            "hepatic_adjustment": {
                "mild": "Không cần điều chỉnh liều",
                "moderate": "Không cần điều chỉnh liều",
                "severe": "Không cần điều chỉnh liều (ophthalmic, hấp thu tối thiểu)",
                "notes": "Pilocarpine dùng tại mắt, hấp thu toàn thân tối thiểu. Không cần điều chỉnh liều ở bệnh nhân suy gan."
            },
            "overdose_management": {
                "symptoms": [
                    "Nhìn mờ nặng",
                    "Kích ứng mắt nặng",
                    "Hấp thu toàn thân: buồn nôn nặng, nôn, tiêu chảy",
                    "Hấp thu toàn thân: co thắt phế quản nặng (hen)",
                    "Hấp thu toàn thân: nhịp chậm nặng"
                ],
                "antidote": "Atropine (anticholinergic) để đối kháng tác dụng cholinergic.",
                "treatment": [
                    "Rửa mắt ngay với nước sạch hoặc nước muối sinh lý",
                    "Nếu kích ứng mắt nặng:",
                    "  - Khám mắt ngay",
                    "  - Điều trị hỗ trợ (nước mắt nhân tạo)",
                    "Nếu hấp thu toàn thân nặng:",
                    "  - Atropine 0.5-1mg IV (đối kháng cholinergic)",
                    "  - Hỗ trợ hô hấp nếu có co thắt phế quản",
                    "  - Hỗ trợ tuần hoàn nếu có nhịp chậm",
                    "Theo dõi: Thị lực, nhãn áp, nhịp tim, huyết áp, hô hấp"
                ],
                "monitoring": "Theo dõi thị lực, nhãn áp, nhịp tim, huyết áp, hô hấp cho đến khi hồi phục. Theo dõi lâu hơn nếu có biến chứng (co thắt phế quản, nhịp chậm)."
            },
            "reversal_agents": {
                "available": True,
                "agents": [
                    {
                        "agent": "Atropine",
                        "mechanism": "Anticholinergic, đối kháng tác dụng cholinergic của pilocarpine",
                        "indication": "Tác dụng phụ toàn thân nặng do pilocarpine",
                        "dose": "0.5-1mg IV, lặp lại mỗi 30-60 phút nếu cần"
                    }
                ],
                "notes": "Atropine đối kháng tác dụng cholinergic của pilocarpine cho tác dụng phụ toàn thân."
            },
            "administration_instructions": {
                "oral": None,
                "ophthalmic": {
                    "preparation": "Dạng dung dịch nhỏ mắt 1%, 2%, hoặc 4%.",
                    "application": "1-2 giọt vào mắt bị ảnh hưởng theo lịch trình (xem dosage). Nhắm mắt nhẹ 1-2 phút sau khi nhỏ. Nhấn nhẹ vào góc trong mắt (lacrimal sac) trong 1-2 phút để giảm hấp thu toàn thân.",
                    "timing": "Tùy theo chỉ định: mỗi 15 phút (acute glaucoma) hoặc 3-4 lần/ngày (chronic glaucoma).",
                    "contact_lenses": "Tháo kính áp tròng trước khi nhỏ. Đợi 15 phút trước khi đeo lại.",
                    "notes": "QUAN TRỌNG: 1) Dùng thường xuyên trong tăng nhãn áp cấp tính, 2) Nhìn mờ kéo dài 4-8 giờ, 3) Bệnh nhân không nên lái xe hoặc vận hành máy móc, 4) Tránh chạm đầu lọ vào mắt hoặc bất kỳ bề mặt nào, 5) Có thể hấp thu toàn thân và gây tác dụng phụ."
                }
            },
            "references": {
                "primary_sources": [
                    "FDA Drug Label - Pilocarpine (Isopto Carpine)",
                    "UpToDate - Pilocarpine: Drug Information",
                    "Medscape - Pilocarpine Drug Reference",
                    "AAO Guidelines - Glaucoma"
                ],
                "last_updated": "2025-02-18",
                "evidence_level": "A - Dựa trên FDA drug labels, clinical guidelines, và dữ liệu lâm sàng từ nhiều nguồn"
            },
            "risk_flags": {
                "high_alert": True,
                "narrow_therapeutic_index": False,
                "bleeding_risk": False,
                "organ_toxicity": ["Systemic cholinergic effects (if systemic absorption occurs) - CRITICAL"],
                "qt_prolongation": False,
                "hepatotoxicity": False,
                "nephrotoxicity": False,
                "requires_monitoring": ["IOP (target <21 mmHg)", "Vision and periodic eye exams", "Blurred vision (lasts 4-8 hours)", "Signs of eye irritation (redness, burning)", "Signs of systemic cholinergic effects (if systemic absorption): salivation, sweating, nausea, vomiting, diarrhea, bradycardia - CRITICAL"]
            },
            "guideline_tags": [
                "AAO Guidelines - Glaucoma",
                "AAO Guidelines - Acute Angle-Closure Glaucoma",
                "FDA Drug Information - Pilocarpine",
                "ISMP High Alert Medications - Cholinergic Medications"
            ],
            "black_box_warnings": "Cần xem xét black box warnings",
        },

        "Timolol eye drops": {
            "group": "Ophthalmology - Beta-blocker (Glaucoma)",
            "vietnamese_name": "Timolol, Timoptic",
            "administration": ["Ophthalmic"],
            "indications": [
                "Tăng nhãn áp góc mở (open-angle glaucoma)",
                "Tăng nhãn áp (ocular hypertension)",
                "Giảm nhãn áp (first-line treatment)",
                "Tăng nhãn áp góc đóng (angle-closure glaucoma) - bổ sung"
            ],
            "contraindications": [
                "Dị ứng timolol hoặc beta-blocker",
                "Hen phế quản nặng - CHỐNG CHỈ ĐỊNH",
                "COPD nặng - CHỐNG CHỈ ĐỊNH",
                "Block nhĩ thất độ 2-3 - CHỐNG CHỈ ĐỊNH",
                "Suy tim nặng (NYHA class IV) - CHỐNG CHỈ ĐỊNH",
                "Nhịp tim chậm nặng (<50 bpm) - CHỐNG CHỈ ĐỊNH"
            ],
            "dosage": {
                "adult_ophthalmic_0.25%": "1 giọt vào mắt bị ảnh hưởng 2 lần/ngày (0.25% solution)",
                "adult_ophthalmic_0.5%": "1 giọt vào mắt bị ảnh hưởng 2 lần/ngày (0.5% solution)",
                "adult_ophthalmic_gel": "1 giọt vào mắt bị ảnh hưởng 1 lần/ngày (0.25% hoặc 0.5% gel, buổi tối)",
                "notes": "Timolol là thuốc first-line cho tăng nhãn áp. Giảm sản xuất thủy dịch, giảm nhãn áp 20-30%. Có thể hấp thu toàn thân và gây tác dụng phụ hệ thống (nhịp chậm, block AV, co thắt phế quản)."
            },
            "renal_adjustment": {
                "normal": "Không đổi",
                "30_60": "Không đổi",
                "under_30": "Không đổi"
            },
            "side_effects": [
                "Kích ứng mắt (đỏ, rát, ngứa) - phổ biến",
                "Nhìn mờ",
                "Khô mắt",
                "Hấp thu toàn thân: nhịp chậm, block AV - phổ biến",
                "Hấp thu toàn thân: co thắt phế quản (hen, COPD) - nguy hiểm",
                "Hấp thu toàn thân: suy tim, hạ huyết áp - hiếm",
                "Hấp thu toàn thân: mệt mỏi, trầm cảm - hiếm"
            ],
            "interactions": [
                "Beta-blocker đường uống: tăng nguy cơ nhịp chậm, block AV",
                "Calcium channel blockers (verapamil, diltiazem): tăng nguy cơ block AV, nhịp chậm",
                "Digoxin: tăng nguy cơ block AV, nhịp chậm"
            ],
            "pregnancy": "C - Thận trọng",
            "mechanism_of_action": "Timolol là non-selective beta-blocker (ức chế cả beta-1 và beta-2 receptors). Khi dùng tại mắt, timolol ức chế beta-2 receptors trên cơ thể mi (ciliary body), giảm sản xuất thủy dịch (aqueous humor production), dẫn đến giảm nhãn áp. Timolol là thuốc first-line cho tăng nhãn áp, tác dụng mạnh (giảm nhãn áp 20-30%), dùng 1-2 lần/ngày. ĐẶC ĐIỂM: (1) Giảm sản xuất thủy dịch (giảm nhãn áp 20-30%), (2) Dùng 1-2 lần/ngày (gel: 1 lần/ngày), (3) Có thể hấp thu toàn thân và gây tác dụng phụ hệ thống (nhịp chậm, block AV, co thắt phế quản, suy tim), (4) CHỐNG CHỈ ĐỊNH ở bệnh nhân hen/COPD nặng, block AV, suy tim nặng, (5) Non-selective beta-blocker (ức chế cả beta-1 và beta-2).",
            "monitoring": [
                "Nhãn áp (intraocular pressure - IOP) - mục tiêu: <21 mmHg",
                "Thị lực và khám mắt định kỳ",
                "Dấu hiệu kích ứng mắt (đỏ, rát, ngứa)",
                "Nhịp tim và ECG (nếu có nguy cơ hấp thu toàn thân)",
                "Dấu hiệu block AV (nhịp chậm, block nhĩ thất)",
                "Dấu hiệu co thắt phế quản (khó thở, thở khò khè) - ở bệnh nhân hen/COPD",
                "Dấu hiệu suy tim (khó thở, phù) - hiếm"
            ],
            "precautions": [
                "CHỐNG CHỈ ĐỊNH ở bệnh nhân hen/COPD nặng (nguy cơ co thắt phế quản nặng)",
                "CHỐNG CHỈ ĐỊNH ở block AV độ 2-3 (nguy cơ block AV nặng)",
                "CHỐNG CHỈ ĐỊNH ở suy tim nặng (NYHA class IV)",
                "CHỐNG CHỈ ĐỊNH ở nhịp tim chậm nặng (<50 bpm)",
                "Có thể hấp thu toàn thân và gây tác dụng phụ hệ thống - cần thận trọng",
                "Nhấn nhẹ vào góc trong mắt (lacrimal sac) sau khi nhỏ để giảm hấp thu toàn thân",
                "Thận trọng ở bệnh nhân đang dùng beta-blocker đường uống (tăng nguy cơ tác dụng phụ)",
                "Thận trọng ở bệnh nhân đeo kính áp tròng (benzalkonium chloride có thể làm hỏng kính)",
                "Tránh chạm đầu lọ vào mắt hoặc bất kỳ bề mặt nào (nguy cơ nhiễm trùng)"
            ],
            "pharmacokinetics": {
                "half_life": "4 giờ (huyết tương, nếu hấp thu toàn thân), nhưng tác dụng tại mắt kéo dài",
                "onset": "30 phút",
                "duration": "12-24 giờ (dùng 1-2 lần/ngày)",
                "protein_binding": "10%",
                "metabolism": "Chuyển hóa tại mắt và gan (nếu hấp thu toàn thân)",
                "clearance": "Thải trừ qua thận (nếu hấp thu toàn thân)"
            },
            "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ánh sáng. Đóng nắp kín sau khi dùng.",
            "black_box_warnings": "Có thể hấp thu toàn thân và gây tác dụng phụ hệ thống nghiêm trọng (nhịp chậm, block AV, co thắt phế quản, suy tim). CHỐNG CHỈ ĐỊNH ở bệnh nhân hen/COPD nặng, block AV độ 2-3, suy tim nặng, nhịp tim chậm nặng. Nhấn nhẹ vào góc trong mắt sau khi nhỏ để giảm hấp thu toàn thân.",
            "drug_interactions": {
                "major": [
                    {
                        "drug": "Beta-blocker đường uống (Metoprolol, Atenolol, Propranolol)",
                        "mechanism": "Tác dụng hiệp đồng ức chế beta receptors",
                        "effect": "Tăng nguy cơ nhịp chậm, block AV, suy tim, co thắt phế quản",
                        "management": "Thận trọng. Theo dõi nhịp tim, ECG, dấu hiệu suy tim, co thắt phế quản chặt chẽ. Có thể cần giảm liều beta-blocker đường uống."
                    },
                    {
                        "drug": "Calcium Channel Blockers (Verapamil, Diltiazem)",
                        "mechanism": "Cả hai đều làm chậm nhịp tim và dẫn truyền AV",
                        "effect": "Tăng nguy cơ block AV, nhịp chậm nặng, suy tim",
                        "management": "Thận trọng. Theo dõi ECG và huyết động chặt chẽ."
                    },
                    {
                        "drug": "Digoxin",
                        "mechanism": "Cả hai đều làm chậm nhịp tim và dẫn truyền AV",
                        "effect": "Tăng nguy cơ block AV, nhịp chậm nặng",
                        "management": "Thận trọng. Theo dõi ECG chặt chẽ. Có thể cần giảm liều digoxin."
                    }
                ],
                "moderate": [],
                "minor": []
            },
            "contraindications": {
                "tuyệt_đối": [
                    "Dị ứng timolol hoặc beta-blocker",
                    "Hen phế quản nặng - CHỐNG CHỈ ĐỊNH (nguy cơ co thắt phế quản nặng)",
                    "COPD nặng - CHỐNG CHỈ ĐỊNH (nguy cơ co thắt phế quản nặng)",
                    "Block nhĩ thất độ 2-3 - CHỐNG CHỈ ĐỊNH (nguy cơ block AV nặng)",
                    "Suy tim nặng (NYHA class IV) - CHỐNG CHỈ ĐỊNH",
                    "Nhịp tim chậm nặng (<50 bpm) - CHỐNG CHỈ ĐỊNH"
                ],
                "tương_đối": [
                    "Hen phế quản nhẹ - thận trọng, theo dõi dấu hiệu co thắt phế quản",
                    "COPD nhẹ - thận trọng, theo dõi dấu hiệu co thắt phế quản",
                    "Block nhĩ thất độ 1 - thận trọng, theo dõi ECG",
                    "Suy tim (NYHA class I-III) - thận trọng, có thể làm nặng",
                    "Dùng với beta-blocker đường uống - tăng nguy cơ tác dụng phụ",
                    "Bệnh nhân đeo kính áp tròng - thận trọng (benzalkonium chloride)"
                ]
            },
            "pregnancy_lactation": {
                "fda_category": "C",
                "pregnancy_details": "Timolol là thuốc phân loại C. Timolol có thể hấp thu toàn thân và qua nhau thai. Beta-blocker có thể gây nhịp chậm, hạ đường huyết, hạ huyết áp ở thai nhi. Có thể dùng khi lợi ích vượt quá nguy cơ, đặc biệt khi không có lựa chọn khác.",
                "lactation": {
                    "safety": "Compatible with Caution",
                    "details": "Timolol có thể hấp thu toàn thân và bài tiết vào sữa mẹ. Beta-blocker có thể gây nhịp chậm, hạ đường huyết ở trẻ bú mẹ. Tuy nhiên, nồng độ trong sữa mẹ thấp khi dùng tại mắt.",
                    "recommendation": "Có thể dùng khi cho con bú, nhưng thận trọng. Theo dõi trẻ bú mẹ về dấu hiệu nhịp chậm, hạ đường huyết."
                }
            },
            "hepatic_adjustment": {
                "mild": "Không cần điều chỉnh liều",
                "moderate": "Không cần điều chỉnh liều",
                "severe": "Không cần điều chỉnh liều (ophthalmic, hấp thu tối thiểu)",
                "notes": "Timolol dùng tại mắt, hấp thu toàn thân tối thiểu. Không cần điều chỉnh liều ở bệnh nhân suy gan."
            },
            "overdose_management": {
                "symptoms": [
                    "Kích ứng mắt nặng",
                    "Hấp thu toàn thân: nhịp chậm nặng, block AV",
                    "Hấp thu toàn thân: co thắt phế quản nặng (hen, COPD)",
                    "Hấp thu toàn thân: suy tim, hạ huyết áp"
                ],
                "antidote": "Glucagon, isoproterenol cho nhịp chậm/block AV. Beta-agonist (albuterol) cho co thắt phế quản.",
                "treatment": [
                    "Rửa mắt ngay với nước sạch hoặc nước muối sinh lý",
                    "Nếu kích ứng mắt nặng:",
                    "  - Khám mắt ngay",
                    "  - Điều trị hỗ trợ (nước mắt nhân tạo, thuốc chống viêm nếu cần)",
                    "Nếu hấp thu toàn thân - nhịp chậm/block AV:",
                    "  - Atropine 0.5-1mg IV (có thể không hiệu quả do chẹn beta)",
                    "  - Glucagon 1-5mg IV (đối kháng chẹn beta)",
                    "  - Isoproterenol IV (đối kháng chẹn beta)",
                    "  - Máy tạo nhịp tạm thời nếu cần",
                    "Nếu hấp thu toàn thân - co thắt phế quản:",
                    "  - Beta-2 agonist (albuterol) khí dung hoặc IV",
                    "  - Hỗ trợ hô hấp nếu cần",
                    "Nếu hấp thu toàn thân - suy tim/hạ huyết áp:",
                    "  - Inotrope (dobutamine, milrinone)",
                    "  - Hỗ trợ hô hấp",
                    "Theo dõi: Thị lực, nhãn áp, nhịp tim, ECG, huyết áp, hô hấp"
                ],
                "monitoring": "Theo dõi thị lực, nhãn áp, nhịp tim, ECG, huyết áp, hô hấp cho đến khi hồi phục. Theo dõi lâu hơn nếu có biến chứng (block AV, co thắt phế quản, suy tim)."
            },
            "reversal_agents": {
                "available": True,
                "agents": [
                    {
                        "agent": "Glucagon",
                        "mechanism": "Đối kháng tác dụng chẹn beta (cơ chế không rõ ràng)",
                        "indication": "Nhịp chậm nặng, block AV do timolol",
                        "dose": "1-5mg IV bolus, sau đó 1-5mg/giờ IV infusion"
                    },
                    {
                        "agent": "Isoproterenol",
                        "mechanism": "Beta-agonist, đối kháng tác dụng chẹn beta",
                        "indication": "Nhịp chậm nặng, block AV do timolol",
                        "dose": "1-5 mcg/phút IV infusion, tăng dần đến khi đạt nhịp tim mục tiêu"
                    },
                    {
                        "agent": "Albuterol",
                        "mechanism": "Beta-2 agonist, đối kháng tác dụng chẹn beta-2",
                        "indication": "Co thắt phế quản do timolol",
                        "dose": "2.5-5mg khí dung hoặc 0.5mg IV"
                    }
                ],
                "notes": "Glucagon và isoproterenol đối kháng tác dụng chẹn beta cho nhịp chậm/block AV. Albuterol đối kháng tác dụng chẹn beta-2 cho co thắt phế quản."
            },
            "administration_instructions": {
                "oral": None,
                "ophthalmic": {
                    "preparation": "Dạng dung dịch nhỏ mắt 0.25% hoặc 0.5%, hoặc gel 0.25% hoặc 0.5%.",
                    "application": "Solution: 1 giọt vào mắt bị ảnh hưởng 2 lần/ngày. Gel: 1 giọt vào mắt bị ảnh hưởng 1 lần/ngày (buổi tối). Nhắm mắt nhẹ 1-2 phút sau khi nhỏ. Nhấn nhẹ vào góc trong mắt (lacrimal sac) trong 1-2 phút để giảm hấp thu toàn thân.",
                    "timing": "Solution: 2 lần/ngày (sáng, tối). Gel: 1 lần/ngày (buổi tối).",
                    "contact_lenses": "Tháo kính áp tròng trước khi nhỏ. Đợi 15 phút trước khi đeo lại.",
                    "notes": "QUAN TRỌNG: 1) CHỐNG CHỈ ĐỊNH ở bệnh nhân hen/COPD nặng, block AV, suy tim nặng, 2) Nhấn nhẹ vào góc trong mắt sau khi nhỏ để giảm hấp thu toàn thân, 3) Có thể hấp thu toàn thân và gây tác dụng phụ hệ thống, 4) Tránh chạm đầu lọ vào mắt hoặc bất kỳ bề mặt nào, 5) Thận trọng ở bệnh nhân đang dùng beta-blocker đường uống."
                }
            },
            "references": {
                "primary_sources": [
                    "FDA Drug Label - Timolol (Timoptic)",
                    "UpToDate - Timolol: Drug Information",
                    "Medscape - Timolol Drug Reference",
                    "Goodman & Gilman's The Pharmacological Basis of Therapeutics (14th ed)"
                ],
                "last_updated": "2025-02-18",
                "evidence_level": "A - Dựa trên FDA drug labels, clinical guidelines, và dữ liệu lâm sàng từ nhiều nguồn"
            },
            "risk_flags": {
                "high_alert": True,
                "narrow_therapeutic_index": False,
                "bleeding_risk": False,
                "organ_toxicity": ["Bronchospasm (in asthma/COPD) - CRITICAL", "Bradycardia/AV block (in heart disease) - CRITICAL", "Heart failure exacerbation - CRITICAL"],
                "qt_prolongation": False,
                "hepatotoxicity": False,
                "nephrotoxicity": False,
                "requires_monitoring": ["IOP (target <21 mmHg)", "Vision and periodic eye exams", "Signs of eye irritation (redness, burning)", "Heart rate and blood pressure (if systemic absorption) - CRITICAL", "Signs of bronchospasm (wheezing, shortness of breath) - CRITICAL", "Signs of bradycardia/AV block - CRITICAL"]
            },
            "guideline_tags": [
                "AAO Guidelines - Glaucoma",
                "FDA Black Box Warning - Timolol and Asthma/COPD",
                "FDA Black Box Warning - Timolol and Heart Block",
                "FDA Drug Information - Timolol",
                "ISMP High Alert Medications - Beta-Blockers"
            ]
        },

        "Travoprost": {
            "group": "Ophthalmology - Prostaglandin Analog (Glaucoma)",
            "vietnamese_name": "Travoprost, Travatan",
            "administration": ["Ophthalmic"],
            "indications": [
                "Tăng nhãn áp góc mở (open-angle glaucoma)",
                "Tăng nhãn áp (ocular hypertension)",
                "Giảm nhãn áp (first-line treatment)"
            ],
            "contraindications": [
                "Dị ứng travoprost hoặc benzalkonium chloride",
                "Viêm màng bồ đào (uveitis) hoạt động",
                "Viêm giác mạc (keratitis) hoạt động",
                "Trẻ em <18 tuổi (thận trọng)"
            ],
            "dosage": {
                "adult_ophthalmic": "1 giọt vào mắt bị ảnh hưởng 1 lần/ngày (buổi tối)",
                "notes": "Travoprost là prostaglandin analog, tương tự latanoprost và bimatoprost. Tác dụng mạnh, giảm nhãn áp 25-35%. Dùng buổi tối để tối ưu hiệu quả. Có thể gây thay đổi màu mắt (tăng sắc tố mống mắt) và lông mi (dài, đậm, đổi màu)."
            },
            "renal_adjustment": {
                "normal": "Không đổi",
                "30_60": "Không đổi",
                "under_30": "Không đổi"
            },
            "side_effects": [
                "Thay đổi màu mắt (tăng sắc tố mống mắt) - vĩnh viễn, phổ biến",
                "Thay đổi lông mi (dài, đậm, đổi màu) - phổ biến",
                "Đỏ mắt, kích ứng mắt",
                "Khô mắt",
                "Nhìn mờ",
                "Đau mắt",
                "Viêm màng bồ đào (hiếm)",
                "Viêm giác mạc (hiếm)",
                "Phù hoàng điểm (macular edema) - hiếm, ở bệnh nhân có tiền sử"
            ],
            "interactions": [
                "Không có tương tác đáng kể với thuốc khác (ophthalmic)"
            ],
            ',
        "pregnancy": "C - Thận trọng",
        ',
            "mechanism_of_action": "Travoprost là prostaglandin analog. Gắn với thụ thể prostaglandin F trên cơ trơn mống mắt và cơ thể mi, dẫn đến: (1) Tăng dẫn lưu thủy dịch qua đường uveoscleral (tăng outflow), (2) Giảm sản xuất thủy dịch (nhẹ), (3) Giảm nhãn áp. Travoprost tương tự latanoprost và bimatoprost, tác dụng mạnh (giảm nhãn áp 25-35%), dùng 1 lần/ngày. ĐẶC ĐIỂM: (1) Tác dụng mạnh, giảm nhãn áp 25-35%, (2) Dùng 1 lần/ngày (buổi tối), (3) Thay đổi màu mắt (tăng sắc tố mống mắt) - vĩnh viễn, phổ biến, (4) Thay đổi lông mi (dài, đậm, đổi màu) - phổ biến, (5) Nguy cơ phù hoàng điểm ở bệnh nhân có tiền sử.",
            "monitoring": [
                "Nhãn áp (intraocular pressure - IOP) - mục tiêu: <21 mmHg",
                "Thị lực và khám mắt định kỳ",
                "Dấu hiệu thay đổi màu mắt (tăng sắc tố mống mắt)",
                "Dấu hiệu thay đổi lông mi (dài, đậm, đổi màu)",
                "Dấu hiệu viêm màng bồ đào (đỏ mắt, đau, nhìn mờ)",
                "Dấu hiệu phù hoàng điểm (giảm thị lực, nhìn mờ) - ở bệnh nhân có tiền sử"
            ],
            "precautions": [
                "Thay đổi màu mắt (tăng sắc tố mống mắt) - vĩnh viễn, phổ biến, đặc biệt ở mắt nâu/xanh",
                "Thay đổi lông mi (dài, đậm, đổi màu) - phổ biến, có thể vĩnh viễn",
                "Nguy cơ phù hoàng điểm ở bệnh nhân có tiền sử (viêm màng bồ đào, đái tháo đường, phẫu thuật mắt)",
                "CHỐNG CHỈ ĐỊNH ở viêm màng bồ đào hoạt động",
                "CHỐNG CHỈ ĐỊNH ở viêm giác mạc hoạt động",
                "Thận trọng ở trẻ em <18 tuổi",
                "Thận trọng ở bệnh nhân đeo kính áp tròng (benzalkonium chloride có thể làm hỏng kính)",
                "Dùng buổi tối để tối ưu hiệu quả",
                "Tránh chạm đầu lọ vào mắt hoặc bất kỳ bề mặt nào (nguy cơ nhiễm trùng)"
            ],
            "pharmacokinetics": {
                "half_life": "45 phút (huyết tương), nhưng tác dụng tại mắt kéo dài",
                "onset": "3-4 giờ",
                "duration": "24 giờ (dùng 1 lần/ngày)",
                "protein_binding": "Không đáng kể",
                "metabolism": "Chuyển hóa tại mắt và gan (nếu hấp thu toàn thân)",
                "clearance": "Thải trừ qua nước tiểu (nếu hấp thu toàn thân)"
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
                    "Dị ứng travoprost hoặc benzalkonium chloride",
                    "Viêm màng bồ đào (uveitis) hoạt động - CHỐNG CHỈ ĐỊNH",
                    "Viêm giác mạc (keratitis) hoạt động - CHỐNG CHỈ ĐỊNH"
                ],
                "tương_đối": [
                    "Trẻ em <18 tuổi - thận trọng",
                    "Bệnh nhân có tiền sử viêm màng bồ đào - nguy cơ phù hoàng điểm",
                    "Bệnh nhân đái tháo đường - nguy cơ phù hoàng điểm",
                    "Bệnh nhân có tiền sử phẫu thuật mắt - nguy cơ phù hoàng điểm",
                    "Bệnh nhân đeo kính áp tròng - thận trọng (benzalkonium chloride)"
                ]
            },
            "pregnancy_lactation": {
                "fda_category": "C",
                "pregnancy_details": "Travoprost là thuốc phân loại C. Không có nghiên cứu đầy đủ trên phụ nữ có thai. Travoprost có thể hấp thu toàn thân và qua nhau thai. Có thể dùng khi lợi ích vượt quá nguy cơ, đặc biệt khi không có lựa chọn khác.",
                "lactation": {
                    "safety": "Compatible with Caution",
                    "details": "Travoprost có thể hấp thu toàn thân và bài tiết vào sữa mẹ ở nồng độ thấp. Tuy nhiên, nồng độ trong sữa mẹ thấp và không có báo cáo về tác dụng phụ đáng kể ở trẻ bú mẹ khi dùng tại mắt.",
                    "recommendation": "Có thể dùng khi cho con bú, nhưng thận trọng. Nồng độ trong sữa mẹ thấp."
                }
            },
            "hepatic_adjustment": {
                "mild": "Không cần điều chỉnh liều",
                "moderate": "Không cần điều chỉnh liều",
                "severe": "Không cần điều chỉnh liều (ophthalmic, hấp thu tối thiểu)",
                "notes": "Travoprost dùng tại mắt, hấp thu toàn thân tối thiểu. Không cần điều chỉnh liều ở bệnh nhân suy gan."
            },
            "overdose_management": {
                "symptoms": [
                    "Kích ứng mắt nặng",
                    "Nhìn mờ nặng",
                    "Đau mắt nặng"
                ],
                "antidote": "Không có antidote đặc hiệu. Rửa mắt, điều trị hỗ trợ.",
                "treatment": [
                    "Rửa mắt ngay với nước sạch hoặc nước muối sinh lý",
                    "Nếu kích ứng mắt nặng:",
                    "  - Khám mắt ngay",
                    "  - Điều trị hỗ trợ (nước mắt nhân tạo)",
                    "Theo dõi: Thị lực, nhãn áp, dấu hiệu kích ứng mắt"
                ],
                "monitoring": "Theo dõi thị lực, nhãn áp, dấu hiệu kích ứng mắt cho đến khi hồi phục."
            },
            "reversal_agents": None,
            "administration_instructions": {
                "ophthalmic": {
                    "preparation": "Dạng dung dịch nhỏ mắt 0.004%.",
                    "application": "1 giọt vào mắt bị ảnh hưởng 1 lần/ngày (buổi tối). Nhắm mắt nhẹ 1-2 phút sau khi nhỏ. Nhấn nhẹ vào góc trong mắt (lacrimal sac) trong 1-2 phút để giảm hấp thu toàn thân.",
                    "timing": "1 lần/ngày (buổi tối) để tối ưu hiệu quả.",
                    "contact_lenses": "Tháo kính áp tròng trước khi nhỏ. Đợi 15 phút trước khi đeo lại.",
                    "notes": "QUAN TRỌNG: 1) Dùng buổi tối để tối ưu hiệu quả, 2) Thay đổi màu mắt và lông mi phổ biến, 3) Tránh chạm đầu lọ vào mắt, 4) Nguy cơ phù hoàng điểm ở bệnh nhân có tiền sử."
                }
            },
            "references": {
                "primary_sources": [
                    "FDA Drug Label - Travoprost (Travatan)",
                    "UpToDate - Travoprost: Drug Information",
                    "Medscape - Travoprost Drug Reference",
                    "AAO Guidelines - Glaucoma"
                ],
                "last_updated": "2025-02-18",
                "evidence_level": "A - Dựa trên FDA drug labels, clinical guidelines, và dữ liệu lâm sàng từ nhiều nguồn"
            },
            "risk_flags": {
                "high_alert": False,
                "narrow_therapeutic_index": False,
                "bleeding_risk": False,
                "organ_toxicity": ["Iris color change (permanent) - common", "Macular edema (rare, in patients with history)"],
                "qt_prolongation": False,
                "hepatotoxicity": False,
                "nephrotoxicity": False,
                "requires_monitoring": ["IOP (target <21 mmHg)", "Vision and periodic eye exams", "Iris color changes (permanent) - common", "Eyelash changes (longer, darker, color change) - common", "Signs of eye irritation (redness, burning)", "Signs of macular edema (rare, in patients with history)"]
            },
            "guideline_tags": [
                "AAO Guidelines - Glaucoma",
                "FDA Drug Information - Travoprost",
                "UpToDate - Glaucoma Treatment"
            ],
            "black_box_warnings": "Cần xem xét black box warnings",
            "reversal_agents": {
                "available": False,
                "agents": [],
            },
        },

}

__all__ = ['ANTI_GLAUCOMA_DRUGS']
