"""
Ophthalmology - Eye Medications
"""

OPHTHALMOLOGY_DRUGS = {
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
        "pregnancy": "C - Thận trọng",
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
        }
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
        }
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
        }
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
        }
    },
    
    "Dexamethasone eye drops": {
        "group": "Ophthalmology - Corticosteroid (Anti-inflammatory)",
        "vietnamese_name": "Dexamethasone nhỏ mắt, Maxidex",
        "administration": ["Ophthalmic"],
        "indications": [
            "Viêm kết mạc dị ứng (allergic conjunctivitis)",
            "Viêm màng bồ đào (uveitis)",
            "Viêm giác mạc (keratitis)",
            "Viêm sau phẫu thuật mắt (postoperative inflammation)",
            "Viêm màng bồ đào do miễn dịch (immune-mediated uveitis)"
        ],
        "contraindications": [
            "Dị ứng dexamethasone hoặc corticosteroid",
            "Nhiễm trùng mắt do virus (herpes simplex, varicella) - CHỐNG CHỈ ĐỊNH",
            "Nhiễm trùng mắt do nấm - CHỐNG CHỈ ĐỊNH",
            "Nhiễm trùng mắt do vi khuẩn chưa điều trị - CHỐNG CHỈ ĐỊNH",
            "Tăng nhãn áp (glaucoma) - thận trọng",
            "Đục thủy tinh thể (cataract) - thận trọng"
        ],
        "dosage": {
            "adult_conjunctivitis": "1-2 giọt vào mắt bị ảnh hưởng 4-6 lần/ngày, giảm dần khi cải thiện",
            "adult_uveitis": "1-2 giọt vào mắt bị ảnh hưởng mỗi giờ trong 24-48 giờ đầu, sau đó giảm dần",
            "adult_postoperative": "1-2 giọt vào mắt bị ảnh hưởng 4-6 lần/ngày trong 1-2 tuần",
            "notes": "Dexamethasone là corticosteroid mạnh, chống viêm hiệu quả. Dùng thường xuyên trong giai đoạn đầu, sau đó giảm dần. Điều trị thường 1-4 tuần. Nguy cơ tăng nhãn áp và đục thủy tinh thể nếu dùng kéo dài."
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "Không đổi",
            "under_30": "Không đổi"
        },
        "side_effects": [
            "Tăng nhãn áp (glaucoma) - phổ biến nếu dùng kéo dài",
            "Đục thủy tinh thể (cataract) - phổ biến nếu dùng kéo dài",
            "Kích ứng mắt (đỏ, rát, ngứa) - phổ biến",
            "Nhìn mờ",
            "Nhiễm trùng mắt (nếu dùng kéo dài, ức chế miễn dịch) - nguy hiểm",
            "Chậm lành vết thương",
            "Phản ứng dị ứng - hiếm"
        ],
        "interactions": [
            "Không có tương tác đáng kể với thuốc khác (ophthalmic)"
        ],
        "pregnancy": "C - Thận trọng",
        "mechanism_of_action": "Dexamethasone là corticosteroid tổng hợp mạnh. Gắn với thụ thể glucocorticoid trong tế bào, ức chế quá trình viêm bằng cách: (1) Ức chế giải phóng các chất trung gian viêm (prostaglandin, leukotriene, cytokine), (2) Ức chế di chuyển và hoạt động của bạch cầu, (3) Ức chế sản xuất kháng thể, (4) Ổn định màng tế bào. Dẫn đến: giảm viêm, giảm đỏ, giảm sưng, giảm đau. ĐẶC ĐIỂM: (1) Corticosteroid mạnh, chống viêm hiệu quả, (2) Dùng thường xuyên trong giai đoạn đầu, sau đó giảm dần, (3) Nguy cơ tăng nhãn áp và đục thủy tinh thể nếu dùng kéo dài, (4) CHỐNG CHỈ ĐỊNH ở nhiễm trùng mắt do virus/nấm, (5) Ức chế miễn dịch, tăng nguy cơ nhiễm trùng nếu dùng kéo dài.",
        "monitoring": [
            "Nhãn áp (intraocular pressure - IOP) - QUAN TRỌNG: theo dõi định kỳ, đặc biệt nếu dùng kéo dài",
            "Thị lực và khám mắt định kỳ",
            "Dấu hiệu đục thủy tinh thể (giảm thị lực, nhìn mờ) - nếu dùng kéo dài",
            "Dấu hiệu nhiễm trùng mắt (đỏ, chảy mủ, đau) - nguy hiểm nếu dùng kéo dài",
            "Dấu hiệu kích ứng mắt (đỏ, rát, ngứa)",
            "Dấu hiệu viêm (đỏ, sưng) - cải thiện sau vài ngày"
        ],
        "precautions": [
            "CHỐNG CHỈ ĐỊNH ở nhiễm trùng mắt do virus (herpes simplex, varicella) - có thể làm nặng",
            "CHỐNG CHỈ ĐỊNH ở nhiễm trùng mắt do nấm - có thể làm nặng",
            "CHỐNG CHỈ ĐỊNH ở nhiễm trùng mắt do vi khuẩn chưa điều trị - có thể làm nặng",
            "NGUY CƠ TĂNG NHÃN ÁP - theo dõi định kỳ, đặc biệt nếu dùng kéo dài",
            "NGUY CƠ ĐỤC THỦY TINH THỂ - theo dõi định kỳ, đặc biệt nếu dùng kéo dài",
            "Nguy cơ nhiễm trùng mắt nếu dùng kéo dài (ức chế miễn dịch)",
            "Chậm lành vết thương",
            "Dùng đủ liều và đủ thời gian, nhưng tránh dùng kéo dài không cần thiết",
            "Giảm dần liều khi cải thiện để tránh tái phát",
            "Thận trọng ở bệnh nhân đeo kính áp tròng (benzalkonium chloride có thể làm hỏng kính)",
            "Tránh chạm đầu lọ vào mắt hoặc bất kỳ bề mặt nào (nguy cơ nhiễm trùng)"
        ],
        "pharmacokinetics": {
            "half_life": "3-4 giờ (huyết tương, nếu hấp thu toàn thân), nhưng tác dụng tại mắt kéo dài",
            "onset": "Vài giờ",
            "duration": "4-6 giờ (dùng 4-6 lần/ngày)",
            "protein_binding": "77%",
            "metabolism": "Chuyển hóa tại mắt và gan (nếu hấp thu toàn thân)",
            "clearance": "Thải trừ qua thận (nếu hấp thu toàn thân)"
        },
        "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ánh sáng. Đóng nắp kín sau khi dùng. Dùng trong 4 tuần sau khi mở.",
        "black_box_warnings": "NGUY CƠ TĂNG NHÃN ÁP VÀ ĐỤC THỦY TINH THỂ nếu dùng kéo dài. CHỐNG CHỈ ĐỊNH ở nhiễm trùng mắt do virus/nấm. Ức chế miễn dịch, tăng nguy cơ nhiễm trùng nếu dùng kéo dài. Phải theo dõi nhãn áp định kỳ.",
        "drug_interactions": {
            "major": [],
            "moderate": [],
            "minor": []
        },
        "contraindications": {
            "tuyệt_đối": [
                "Dị ứng dexamethasone hoặc corticosteroid",
                "Nhiễm trùng mắt do virus (herpes simplex, varicella) - CHỐNG CHỈ ĐỊNH (có thể làm nặng)",
                "Nhiễm trùng mắt do nấm - CHỐNG CHỈ ĐỊNH (có thể làm nặng)",
                "Nhiễm trùng mắt do vi khuẩn chưa điều trị - CHỐNG CHỈ ĐỊNH (có thể làm nặng)"
            ],
            "tương_đối": [
                "Tăng nhãn áp (glaucoma) - thận trọng, theo dõi nhãn áp định kỳ",
                "Đục thủy tinh thể (cataract) - thận trọng, có thể làm nặng",
                "Bệnh nhân đeo kính áp tròng - thận trọng (benzalkonium chloride)",
                "Có thai (category C) - thận trọng"
            ]
        },
        "pregnancy_lactation": {
            "fda_category": "C",
            "pregnancy_details": "Dexamethasone là thuốc phân loại C. Dexamethasone có thể hấp thu toàn thân và qua nhau thai. Corticosteroid có thể gây dị tật bẩm sinh ở động vật. Có thể dùng khi lợi ích vượt quá nguy cơ, đặc biệt khi không có lựa chọn khác.",
            "lactation": {
                "safety": "Compatible with Caution",
                "details": "Dexamethasone có thể hấp thu toàn thân và bài tiết vào sữa mẹ. Tuy nhiên, nồng độ trong sữa mẹ thấp khi dùng tại mắt và không có báo cáo về tác dụng phụ đáng kể ở trẻ bú mẹ.",
                "recommendation": "Có thể dùng khi cho con bú, nhưng thận trọng. Nồng độ trong sữa mẹ thấp."
            }
        },
        "hepatic_adjustment": {
            "mild": "Không cần điều chỉnh liều",
            "moderate": "Không cần điều chỉnh liều",
            "severe": "Không cần điều chỉnh liều (ophthalmic, hấp thu tối thiểu)",
            "notes": "Dexamethasone dùng tại mắt, hấp thu toàn thân tối thiểu. Không cần điều chỉnh liều ở bệnh nhân suy gan."
        },
        "overdose_management": {
            "symptoms": [
                "Kích ứng mắt nặng",
                "Tăng nhãn áp nặng (nếu dùng kéo dài)",
                "Đục thủy tinh thể (nếu dùng kéo dài)",
                "Nhiễm trùng mắt (nếu dùng kéo dài)"
            ],
            "antidote": "Không có antidote đặc hiệu. Rửa mắt, điều trị hỗ trợ. Giảm liều hoặc ngừng nếu có tác dụng phụ nặng.",
            "treatment": [
                "Rửa mắt ngay với nước sạch hoặc nước muối sinh lý",
                "Nếu kích ứng mắt nặng:",
                "  - Khám mắt ngay",
                "  - Điều trị hỗ trợ (nước mắt nhân tạo)",
                "Nếu tăng nhãn áp nặng:",
                "  - Ngừng dexamethasone",
                "  - Điều trị tăng nhãn áp (thuốc giảm nhãn áp)",
                "Nếu nhiễm trùng mắt:",
                "  - Ngừng dexamethasone",
                "  - Điều trị nhiễm trùng (kháng sinh, kháng virus, kháng nấm)",
                "Theo dõi: Thị lực, nhãn áp, dấu hiệu viêm, dấu hiệu nhiễm trùng"
            ],
            "monitoring": "Theo dõi thị lực, nhãn áp, dấu hiệu viêm, dấu hiệu nhiễm trùng cho đến khi hồi phục. Theo dõi lâu hơn nếu có biến chứng (tăng nhãn áp, đục thủy tinh thể, nhiễm trùng)."
        },
        "reversal_agents": None,
        "administration_instructions": {
            "oral": None,
            "ophthalmic": {
                "preparation": "Dạng dung dịch nhỏ mắt 0.1% (1 mg/ml).",
                "application": "1-2 giọt vào mắt bị ảnh hưởng theo lịch trình (xem dosage). Nhắm mắt nhẹ 1-2 phút sau khi nhỏ. Nhấn nhẹ vào góc trong mắt (lacrimal sac) trong 1-2 phút để giảm hấp thu toàn thân.",
                "timing": "Tùy theo chỉ định: 4-6 lần/ngày (conjunctivitis, postoperative) hoặc mỗi giờ (uveitis).",
                "contact_lenses": "Tháo kính áp tròng trước khi nhỏ. Đợi 15 phút trước khi đeo lại.",
                "notes": "QUAN TRỌNG: 1) CHỐNG CHỈ ĐỊNH ở nhiễm trùng mắt do virus/nấm, 2) NGUY CƠ TĂNG NHÃN ÁP VÀ ĐỤC THỦY TINH THỂ nếu dùng kéo dài, 3) Theo dõi nhãn áp định kỳ, 4) Giảm dần liều khi cải thiện, 5) Tránh chạm đầu lọ vào mắt hoặc bất kỳ bề mặt nào."
            }
        },
        "references": {
            "primary_sources": [
                "FDA Drug Label - Dexamethasone (Maxidex)",
                "UpToDate - Dexamethasone: Drug Information",
                "Medscape - Dexamethasone Drug Reference",
                "AAO Guidelines - Uveitis"
            ],
            "last_updated": "2025-02-18",
            "evidence_level": "A - Dựa trên FDA drug labels, clinical guidelines, và dữ liệu lâm sàng từ nhiều nguồn"
        }
    },
    
    "Artificial tears (Carboxymethylcellulose)": {
        "group": "Ophthalmology - Lubricant (Dry Eye)",
        "vietnamese_name": "Nước mắt nhân tạo, Carboxymethylcellulose",
        "administration": ["Ophthalmic"],
        "indications": [
            "Khô mắt (dry eye syndrome)",
            "Kích ứng mắt do môi trường (không khí khô, gió, máy điều hòa)",
            "Kích ứng mắt do đeo kính áp tròng",
            "Kích ứng mắt sau phẫu thuật mắt",
            "Kích ứng mắt do thuốc nhỏ mắt khác"
        ],
        "contraindications": [
            "Dị ứng carboxymethylcellulose hoặc bất kỳ thành phần nào"
        ],
        "dosage": {
            "adult_ophthalmic": "1-2 giọt vào mắt bị ảnh hưởng khi cần, thường 3-4 lần/ngày hoặc nhiều hơn",
            "notes": "Nước mắt nhân tạo là thuốc bôi trơn, không có tác dụng điều trị bệnh. Dùng khi cần để giảm khô mắt và kích ứng. Có thể dùng nhiều lần/ngày tùy theo nhu cầu. Không có giới hạn số lần dùng."
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "Không đổi",
            "under_30": "Không đổi"
        },
        "side_effects": [
            "Kích ứng mắt nhẹ (đỏ, rát) - hiếm",
            "Nhìn mờ tạm thời - phổ biến ngay sau khi nhỏ",
            "Dị ứng - hiếm"
        ],
        "interactions": [
            "Không có tương tác đáng kể với thuốc khác"
        ],
        "pregnancy": "Không phân loại - An toàn",
        "mechanism_of_action": "Carboxymethylcellulose là polymer tổng hợp, tạo thành lớp màng bảo vệ trên bề mặt mắt, giữ ẩm và bôi trơn. Carboxymethylcellulose có khả năng giữ nước cao, tạo thành gel trong nước mắt, dẫn đến: (1) Bôi trơn bề mặt mắt, (2) Giữ ẩm, giảm khô mắt, (3) Bảo vệ giác mạc và kết mạc, (4) Giảm kích ứng. Nước mắt nhân tạo không có tác dụng điều trị bệnh, chỉ có tác dụng hỗ trợ và bôi trơn. ĐẶC ĐIỂM: (1) Thuốc bôi trơn, không có tác dụng điều trị bệnh, (2) Dùng khi cần, không có giới hạn số lần dùng, (3) An toàn, ít tác dụng phụ, (4) Có thể dùng với thuốc nhỏ mắt khác (đợi 5-10 phút giữa các thuốc), (5) Nhìn mờ tạm thời ngay sau khi nhỏ - phổ biến.",
        "monitoring": [
            "Dấu hiệu khô mắt (khô, rát, ngứa) - cải thiện sau khi nhỏ",
            "Dấu hiệu kích ứng mắt (đỏ, rát, ngứa) - cải thiện sau khi nhỏ",
            "Thị lực - nhìn mờ tạm thời ngay sau khi nhỏ là bình thường"
        ],
        "precautions": [
            "Nhìn mờ tạm thời ngay sau khi nhỏ - phổ biến, thường hết sau vài phút",
            "Nếu dùng với thuốc nhỏ mắt khác, đợi 5-10 phút giữa các thuốc",
            "Thận trọng ở bệnh nhân đeo kính áp tròng (một số chế phẩm có thể tương thích, một số không)",
            "Tránh chạm đầu lọ vào mắt hoặc bất kỳ bề mặt nào (nguy cơ nhiễm trùng)",
            "Nếu khô mắt nặng hoặc kéo dài, cần khám mắt để tìm nguyên nhân"
        ],
        "pharmacokinetics": {
            "half_life": "Không áp dụng (bôi trơn tại chỗ)",
            "onset": "Ngay lập tức",
            "duration": "1-2 giờ (tùy theo chế phẩm)",
            "protein_binding": "Không áp dụng",
            "metabolism": "Không chuyển hóa, thải trừ qua nước mắt",
            "clearance": "Thải trừ qua nước mắt"
        },
        "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ánh sáng. Đóng nắp kín sau khi dùng. Dùng trong 4 tuần sau khi mở (một số chế phẩm có thể dùng lâu hơn).",
        "black_box_warnings": None,
        "drug_interactions": {
            "major": [],
            "moderate": [],
            "minor": []
        },
        "contraindications": {
            "tuyệt_đối": [
                "Dị ứng carboxymethylcellulose hoặc bất kỳ thành phần nào"
            ],
            "tương_đối": [
                "Bệnh nhân đeo kính áp tròng - thận trọng (một số chế phẩm có thể tương thích, một số không)"
            ]
        },
        "pregnancy_lactation": {
            "fda_category": "Not classified",
            "pregnancy_details": "Nước mắt nhân tạo không có phân loại FDA vì không có tác dụng toàn thân. Carboxymethylcellulose là polymer tổng hợp, không hấp thu toàn thân, an toàn trong thai kỳ.",
            "lactation": {
                "safety": "Compatible",
                "details": "Nước mắt nhân tạo không hấp thu toàn thân, không bài tiết vào sữa mẹ. An toàn khi cho con bú.",
                "recommendation": "Có thể dùng khi cho con bú. An toàn, không có tác dụng phụ."
            }
        },
        "hepatic_adjustment": {
            "mild": "Không cần điều chỉnh liều",
            "moderate": "Không cần điều chỉnh liều",
            "severe": "Không cần điều chỉnh liều (ophthalmic, không hấp thu toàn thân)",
            "notes": "Nước mắt nhân tạo không hấp thu toàn thân. Không cần điều chỉnh liều ở bệnh nhân suy gan."
        },
        "overdose_management": {
            "symptoms": [
                "Nhìn mờ tạm thời",
                "Kích ứng mắt nhẹ"
            ],
            "antidote": "Không có antidote đặc hiệu. Rửa mắt nếu cần.",
            "treatment": [
                "Rửa mắt với nước sạch hoặc nước muối sinh lý nếu cần",
                "Nhìn mờ tạm thời thường hết sau vài phút",
                "Nếu kích ứng mắt nặng:",
                "  - Khám mắt nếu cần",
                "  - Ngừng dùng nếu dị ứng"
            ],
            "monitoring": "Theo dõi thị lực và dấu hiệu kích ứng cho đến khi hồi phục."
        },
        "reversal_agents": None,
        "administration_instructions": {
            "oral": None,
            "ophthalmic": {
                "preparation": "Dạng dung dịch nhỏ mắt 0.5% hoặc 1% (carboxymethylcellulose).",
                "application": "1-2 giọt vào mắt bị ảnh hưởng khi cần, thường 3-4 lần/ngày hoặc nhiều hơn. Nhắm mắt nhẹ 1-2 phút sau khi nhỏ.",
                "timing": "Khi cần, không có giới hạn số lần dùng. Thường 3-4 lần/ngày hoặc nhiều hơn.",
                "contact_lenses": "Có thể dùng với kính áp tròng (một số chế phẩm), nhưng thận trọng. Đợi 15 phút trước khi đeo lại.",
                "notes": "QUAN TRỌNG: 1) Dùng khi cần, không có giới hạn số lần dùng, 2) Nhìn mờ tạm thời ngay sau khi nhỏ là bình thường, 3) Nếu dùng với thuốc nhỏ mắt khác, đợi 5-10 phút giữa các thuốc, 4) Tránh chạm đầu lọ vào mắt hoặc bất kỳ bề mặt nào, 5) Nếu khô mắt nặng hoặc kéo dài, cần khám mắt để tìm nguyên nhân."
            }
        },
        "references": {
            "primary_sources": [
                "FDA Drug Label - Artificial Tears (Carboxymethylcellulose)",
                "UpToDate - Dry Eye Syndrome: Treatment",
                "AAO Guidelines - Dry Eye Syndrome",
                "TFOS DEWS II Report"
            ],
            "last_updated": "2025-02-18",
            "evidence_level": "A - Dựa trên FDA drug labels, clinical guidelines, và dữ liệu lâm sàng từ nhiều nguồn"
        }
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
        }
    },
    
    "Tropicamide eye drops": {
        "group": "Ophthalmology - Mydriatic (Pupil Dilation)",
        "vietnamese_name": "Tropicamide nhỏ mắt, Mydriacyl",
        "administration": ["Ophthalmic"],
        "indications": [
            "Giãn đồng tử để khám mắt (pupil dilation for eye examination)",
            "Khám đáy mắt (fundoscopy)",
            "Khám thủy tinh thể (lens examination)",
            "Đo khúc xạ (refraction) - ở trẻ em"
        ],
        "contraindications": [
            "Dị ứng tropicamide hoặc anticholinergic",
            "Tăng nhãn áp góc đóng (angle-closure glaucoma) - CHỐNG CHỈ ĐỊNH",
            "Bệnh nhân có tiền sử tăng nhãn áp góc đóng - CHỐNG CHỈ ĐỊNH",
            "Trẻ em <3 tháng tuổi - thận trọng"
        ],
        "dosage": {
            "adult_ophthalmic_0.5%": "1-2 giọt vào mắt cần khám, lặp lại sau 5 phút nếu cần",
            "adult_ophthalmic_1%": "1-2 giọt vào mắt cần khám, lặp lại sau 5 phút nếu cần",
            "pediatric_ophthalmic": "1 giọt vào mắt cần khám, lặp lại sau 5 phút nếu cần (thận trọng ở trẻ nhỏ)",
            "notes": "Tropicamide là anticholinergic, giãn đồng tử và liệt điều tiết. Tác dụng nhanh (15-30 phút), kéo dài 4-6 giờ. CHỐNG CHỈ ĐỊNH ở tăng nhãn áp góc đóng (có thể gây tăng nhãn áp cấp tính)."
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "Không đổi",
            "under_30": "Không đổi"
        },
        "side_effects": [
            "Nhìn mờ (do liệt điều tiết) - phổ biến, kéo dài 4-6 giờ",
            "Nhạy cảm với ánh sáng (do giãn đồng tử) - phổ biến, kéo dài 4-6 giờ",
            "Kích ứng mắt (đỏ, rát) - phổ biến",
            "Tăng nhãn áp (ở bệnh nhân tăng nhãn áp góc đóng) - NGUY HIỂM",
            "Tăng nhãn áp cấp tính (angle-closure glaucoma) - NGUY HIỂM",
            "Hấp thu toàn thân: khô miệng, nhịp nhanh - hiếm",
            "Phản ứng dị ứng - hiếm"
        ],
        "interactions": [
            "Anticholinergic đường uống: tăng nguy cơ tác dụng phụ toàn thân",
            "Thuốc chống trầm cảm ba vòng: tăng nguy cơ tác dụng phụ toàn thân"
        ],
        "pregnancy": "C - Thận trọng",
        "mechanism_of_action": "Tropicamide là anticholinergic (muscarinic receptor antagonist). Ức chế muscarinic receptors trên cơ vòng mống mắt (sphincter pupillae) và cơ thể mi (ciliary muscle), dẫn đến: (1) Giãn đồng tử (mydriasis) - cơ vòng mống mắt giãn, cơ giãn mống mắt co, (2) Liệt điều tiết (cycloplegia) - cơ thể mi giãn, thủy tinh thể phẳng, không thể điều tiết. Dẫn đến: giãn đồng tử và liệt điều tiết, cho phép khám mắt tốt hơn. Tropicamide tác dụng nhanh (15-30 phút), kéo dài 4-6 giờ. ĐẶC ĐIỂM: (1) Anticholinergic, giãn đồng tử và liệt điều tiết, (2) Tác dụng nhanh (15-30 phút), kéo dài 4-6 giờ, (3) CHỐNG CHỈ ĐỊNH ở tăng nhãn áp góc đóng (có thể gây tăng nhãn áp cấp tính), (4) Nhìn mờ và nhạy cảm với ánh sáng kéo dài 4-6 giờ, (5) Có thể hấp thu toàn thân và gây tác dụng phụ (khô miệng, nhịp nhanh).",
        "monitoring": [
            "Nhãn áp (intraocular pressure - IOP) - QUAN TRỌNG: kiểm tra trước và sau khi dùng, đặc biệt ở bệnh nhân có nguy cơ",
            "Dấu hiệu tăng nhãn áp cấp tính (đau mắt nặng, đau đầu, buồn nôn, nhìn mờ) - NGUY HIỂM",
            "Thị lực - nhìn mờ kéo dài 4-6 giờ là bình thường",
            "Dấu hiệu nhạy cảm với ánh sáng - kéo dài 4-6 giờ là bình thường",
            "Dấu hiệu kích ứng mắt (đỏ, rát)"
        ],
        "precautions": [
            "CHỐNG CHỈ ĐỊNH ở tăng nhãn áp góc đóng (có thể gây tăng nhãn áp cấp tính) - NGUY HIỂM",
            "CHỐNG CHỈ ĐỊNH ở bệnh nhân có tiền sử tăng nhãn áp góc đóng",
            "Kiểm tra nhãn áp trước khi dùng ở bệnh nhân có nguy cơ",
            "Nhìn mờ kéo dài 4-6 giờ - bệnh nhân không nên lái xe hoặc vận hành máy móc",
            "Nhạy cảm với ánh sáng kéo dài 4-6 giờ - bệnh nhân nên đeo kính râm",
            "Có thể hấp thu toàn thân và gây tác dụng phụ (khô miệng, nhịp nhanh) - hiếm",
            "Thận trọng ở trẻ em <3 tháng tuổi",
            "Thận trọng ở bệnh nhân đeo kính áp tròng (benzalkonium chloride có thể làm hỏng kính)",
            "Tránh chạm đầu lọ vào mắt hoặc bất kỳ bề mặt nào (nguy cơ nhiễm trùng)"
        ],
        "pharmacokinetics": {
            "half_life": "2-4 giờ (huyết tương, nếu hấp thu toàn thân), nhưng tác dụng tại mắt kéo dài",
            "onset": "15-30 phút",
            "duration": "4-6 giờ",
            "protein_binding": "Không rõ",
            "metabolism": "Chuyển hóa tại mắt và gan (nếu hấp thu toàn thân)",
            "clearance": "Thải trừ qua thận (nếu hấp thu toàn thân)"
        },
        "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ánh sáng. Đóng nắp kín sau khi dùng. Dùng trong 4 tuần sau khi mở.",
        "black_box_warnings": "NGUY CƠ TĂNG NHÃN ÁP CẤP TÍNH (angle-closure glaucoma) ở bệnh nhân tăng nhãn áp góc đóng. CHỐNG CHỈ ĐỊNH ở tăng nhãn áp góc đóng và bệnh nhân có tiền sử tăng nhãn áp góc đóng. Phải kiểm tra nhãn áp trước khi dùng ở bệnh nhân có nguy cơ.",
        "drug_interactions": {
            "major": [
                {
                    "drug": "Anticholinergic đường uống (Atropine, Scopolamine, Oxybutynin)",
                    "mechanism": "Tác dụng hiệp đồng ức chế muscarinic receptors",
                    "effect": "Tăng nguy cơ tác dụng phụ toàn thân (khô miệng, nhịp nhanh, táo bón, bí tiểu)",
                    "management": "Thận trọng. Theo dõi dấu hiệu tác dụng phụ toàn thân."
                },
                {
                    "drug": "Thuốc chống trầm cảm ba vòng (Amitriptyline, Imipramine)",
                    "mechanism": "Có tác dụng anticholinergic, tác dụng hiệp đồng",
                    "effect": "Tăng nguy cơ tác dụng phụ toàn thân",
                    "management": "Thận trọng. Theo dõi dấu hiệu tác dụng phụ toàn thân."
                }
            ],
            "moderate": [],
            "minor": []
        },
        "contraindications": {
            "tuyệt_đối": [
                "Dị ứng tropicamide hoặc anticholinergic",
                "Tăng nhãn áp góc đóng (angle-closure glaucoma) - CHỐNG CHỈ ĐỊNH (nguy cơ tăng nhãn áp cấp tính)",
                "Bệnh nhân có tiền sử tăng nhãn áp góc đóng - CHỐNG CHỈ ĐỊNH"
            ],
            "tương_đối": [
                "Trẻ em <3 tháng tuổi - thận trọng",
                "Bệnh nhân có nguy cơ tăng nhãn áp góc đóng - kiểm tra nhãn áp trước khi dùng",
                "Bệnh nhân đeo kính áp tròng - thận trọng (benzalkonium chloride)",
                "Có thai (category C) - thận trọng"
            ]
        },
        "pregnancy_lactation": {
            "fda_category": "C",
            "pregnancy_details": "Tropicamide là thuốc phân loại C. Tropicamide có thể hấp thu toàn thân và qua nhau thai. Anticholinergic có thể gây tác dụng phụ ở thai nhi. Có thể dùng khi lợi ích vượt quá nguy cơ, đặc biệt khi không có lựa chọn khác.",
            "lactation": {
                "safety": "Compatible with Caution",
                "details": "Tropicamide có thể hấp thu toàn thân và bài tiết vào sữa mẹ. Tuy nhiên, nồng độ trong sữa mẹ thấp khi dùng tại mắt và không có báo cáo về tác dụng phụ đáng kể ở trẻ bú mẹ.",
                "recommendation": "Có thể dùng khi cho con bú, nhưng thận trọng. Nồng độ trong sữa mẹ thấp."
            }
        },
        "hepatic_adjustment": {
            "mild": "Không cần điều chỉnh liều",
            "moderate": "Không cần điều chỉnh liều",
            "severe": "Không cần điều chỉnh liều (ophthalmic, hấp thu tối thiểu)",
            "notes": "Tropicamide dùng tại mắt, hấp thu toàn thân tối thiểu. Không cần điều chỉnh liều ở bệnh nhân suy gan."
        },
        "overdose_management": {
            "symptoms": [
                "Tăng nhãn áp cấp tính (angle-closure glaucoma) - NGUY HIỂM",
                "Nhìn mờ nặng",
                "Nhạy cảm với ánh sáng nặng",
                "Hấp thu toàn thân: khô miệng nặng, nhịp nhanh, táo bón, bí tiểu"
            ],
            "antidote": "Pilocarpine (cholinergic) để co đồng tử và giảm nhãn áp. Physostigmine cho tác dụng phụ toàn thân.",
            "treatment": [
                "Nếu tăng nhãn áp cấp tính:",
                "  - Pilocarpine 1-2% nhỏ mắt để co đồng tử",
                "  - Thuốc giảm nhãn áp (timolol, dorzolamide)",
                "  - Acetazolamide uống hoặc IV nếu cần",
                "  - Khám mắt ngay",
                "Nếu hấp thu toàn thân nặng:",
                "  - Physostigmine 1-2mg IV (đối kháng anticholinergic)",
                "  - Hỗ trợ hô hấp nếu cần",
                "Theo dõi: Thị lực, nhãn áp, nhịp tim, huyết áp, hô hấp"
            ],
            "monitoring": "Theo dõi thị lực, nhãn áp, nhịp tim, huyết áp, hô hấp cho đến khi hồi phục. Theo dõi lâu hơn nếu có biến chứng (tăng nhãn áp cấp tính)."
        },
        "reversal_agents": {
            "available": True,
            "agents": [
                {
                    "agent": "Pilocarpine",
                    "mechanism": "Cholinergic (muscarinic agonist), co đồng tử và giảm nhãn áp",
                    "indication": "Tăng nhãn áp cấp tính do tropicamide",
                    "dose": "1-2% nhỏ mắt, 1 giọt mỗi 15 phút cho đến khi co đồng tử"
                },
                {
                    "agent": "Physostigmine",
                    "mechanism": "Cholinesterase inhibitor, đối kháng tác dụng anticholinergic",
                    "indication": "Tác dụng phụ toàn thân nặng do tropicamide",
                    "dose": "1-2mg IV, lặp lại mỗi 30-60 phút nếu cần"
                }
            ],
            "notes": "Pilocarpine co đồng tử và giảm nhãn áp cho tăng nhãn áp cấp tính. Physostigmine đối kháng tác dụng anticholinergic cho tác dụng phụ toàn thân."
        },
        "administration_instructions": {
            "oral": None,
            "ophthalmic": {
                "preparation": "Dạng dung dịch nhỏ mắt 0.5% hoặc 1%.",
                "application": "1-2 giọt vào mắt cần khám, lặp lại sau 5 phút nếu cần. Nhắm mắt nhẹ 1-2 phút sau khi nhỏ. Nhấn nhẹ vào góc trong mắt (lacrimal sac) trong 1-2 phút để giảm hấp thu toàn thân.",
                "timing": "Trước khi khám mắt. Tác dụng sau 15-30 phút, kéo dài 4-6 giờ.",
                "contact_lenses": "Tháo kính áp tròng trước khi nhỏ. Đợi 15 phút trước khi đeo lại.",
                "notes": "QUAN TRỌNG: 1) CHỐNG CHỈ ĐỊNH ở tăng nhãn áp góc đóng, 2) Nhìn mờ và nhạy cảm với ánh sáng kéo dài 4-6 giờ, 3) Bệnh nhân không nên lái xe hoặc vận hành máy móc, 4) Bệnh nhân nên đeo kính râm, 5) Tránh chạm đầu lọ vào mắt hoặc bất kỳ bề mặt nào."
            }
        },
        "references": {
            "primary_sources": [
                "FDA Drug Label - Tropicamide (Mydriacyl)",
                "UpToDate - Tropicamide: Drug Information",
                "Medscape - Tropicamide Drug Reference",
                "AAO Guidelines - Eye Examination"
            ],
            "last_updated": "2025-02-18",
            "evidence_level": "A - Dựa trên FDA drug labels, clinical guidelines, và dữ liệu lâm sàng từ nhiều nguồn"
        }
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
        }
    },
    
    "Prednisolone eye drops": {
        "group": "Ophthalmology - Corticosteroid (Anti-inflammatory)",
        "vietnamese_name": "Prednisolone nhỏ mắt, Pred Forte",
        "administration": ["Ophthalmic"],
        "indications": [
            "Viêm kết mạc dị ứng (allergic conjunctivitis)",
            "Viêm màng bồ đào (uveitis)",
            "Viêm giác mạc (keratitis)",
            "Viêm sau phẫu thuật mắt (postoperative inflammation)",
            "Viêm màng bồ đào do miễn dịch (immune-mediated uveitis)"
        ],
        "contraindications": [
            "Dị ứng prednisolone hoặc corticosteroid",
            "Nhiễm trùng mắt do virus (herpes simplex, varicella) - CHỐNG CHỈ ĐỊNH",
            "Nhiễm trùng mắt do nấm - CHỐNG CHỈ ĐỊNH",
            "Nhiễm trùng mắt do vi khuẩn chưa điều trị - CHỐNG CHỈ ĐỊNH",
            "Tăng nhãn áp (glaucoma) - thận trọng",
            "Đục thủy tinh thể (cataract) - thận trọng"
        ],
        "dosage": {
            "adult_conjunctivitis": "1-2 giọt vào mắt bị ảnh hưởng 4-6 lần/ngày, giảm dần khi cải thiện",
            "adult_uveitis": "1-2 giọt vào mắt bị ảnh hưởng mỗi giờ trong 24-48 giờ đầu, sau đó giảm dần",
            "adult_postoperative": "1-2 giọt vào mắt bị ảnh hưởng 4-6 lần/ngày trong 1-2 tuần",
            "notes": "Prednisolone là corticosteroid mạnh, chống viêm hiệu quả. Dùng thường xuyên trong giai đoạn đầu, sau đó giảm dần. Điều trị thường 1-4 tuần. Nguy cơ tăng nhãn áp và đục thủy tinh thể nếu dùng kéo dài."
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "Không đổi",
            "under_30": "Không đổi"
        },
        "side_effects": [
            "Tăng nhãn áp (glaucoma) - phổ biến nếu dùng kéo dài",
            "Đục thủy tinh thể (cataract) - phổ biến nếu dùng kéo dài",
            "Kích ứng mắt (đỏ, rát, ngứa) - phổ biến",
            "Nhìn mờ",
            "Nhiễm trùng mắt (nếu dùng kéo dài, ức chế miễn dịch) - nguy hiểm",
            "Chậm lành vết thương",
            "Phản ứng dị ứng - hiếm"
        ],
        "interactions": [
            "Không có tương tác đáng kể với thuốc khác (ophthalmic)"
        ],
        "pregnancy": "C - Thận trọng",
        "mechanism_of_action": "Prednisolone là corticosteroid tổng hợp mạnh. Gắn với thụ thể glucocorticoid trong tế bào, ức chế quá trình viêm bằng cách: (1) Ức chế giải phóng các chất trung gian viêm (prostaglandin, leukotriene, cytokine), (2) Ức chế di chuyển và hoạt động của bạch cầu, (3) Ức chế sản xuất kháng thể, (4) Ổn định màng tế bào. Dẫn đến: giảm viêm, giảm đỏ, giảm sưng, giảm đau. ĐẶC ĐIỂM: (1) Corticosteroid mạnh, chống viêm hiệu quả, (2) Dùng thường xuyên trong giai đoạn đầu, sau đó giảm dần, (3) Nguy cơ tăng nhãn áp và đục thủy tinh thể nếu dùng kéo dài, (4) CHỐNG CHỈ ĐỊNH ở nhiễm trùng mắt do virus/nấm, (5) Ức chế miễn dịch, tăng nguy cơ nhiễm trùng nếu dùng kéo dài.",
        "monitoring": [
            "Nhãn áp (intraocular pressure - IOP) - QUAN TRỌNG: theo dõi định kỳ, đặc biệt nếu dùng kéo dài",
            "Thị lực và khám mắt định kỳ",
            "Dấu hiệu đục thủy tinh thể (giảm thị lực, nhìn mờ) - nếu dùng kéo dài",
            "Dấu hiệu nhiễm trùng mắt (đỏ, chảy mủ, đau) - nguy hiểm nếu dùng kéo dài",
            "Dấu hiệu kích ứng mắt (đỏ, rát, ngứa)",
            "Dấu hiệu viêm (đỏ, sưng) - cải thiện sau vài ngày"
        ],
        "precautions": [
            "CHỐNG CHỈ ĐỊNH ở nhiễm trùng mắt do virus (herpes simplex, varicella) - có thể làm nặng",
            "CHỐNG CHỈ ĐỊNH ở nhiễm trùng mắt do nấm - có thể làm nặng",
            "CHỐNG CHỈ ĐỊNH ở nhiễm trùng mắt do vi khuẩn chưa điều trị - có thể làm nặng",
            "NGUY CƠ TĂNG NHÃN ÁP - theo dõi định kỳ, đặc biệt nếu dùng kéo dài",
            "NGUY CƠ ĐỤC THỦY TINH THỂ - theo dõi định kỳ, đặc biệt nếu dùng kéo dài",
            "Nguy cơ nhiễm trùng mắt nếu dùng kéo dài (ức chế miễn dịch)",
            "Chậm lành vết thương",
            "Dùng đủ liều và đủ thời gian, nhưng tránh dùng kéo dài không cần thiết",
            "Giảm dần liều khi cải thiện để tránh tái phát",
            "Thận trọng ở bệnh nhân đeo kính áp tròng (benzalkonium chloride có thể làm hỏng kính)",
            "Tránh chạm đầu lọ vào mắt hoặc bất kỳ bề mặt nào (nguy cơ nhiễm trùng)"
        ],
        "pharmacokinetics": {
            "half_life": "2-3 giờ (huyết tương, nếu hấp thu toàn thân), nhưng tác dụng tại mắt kéo dài",
            "onset": "Vài giờ",
            "duration": "4-6 giờ (dùng 4-6 lần/ngày)",
            "protein_binding": "90-95%",
            "metabolism": "Chuyển hóa tại mắt và gan (nếu hấp thu toàn thân)",
            "clearance": "Thải trừ qua thận (nếu hấp thu toàn thân)"
        },
        "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ánh sáng. Đóng nắp kín sau khi dùng. Dùng trong 4 tuần sau khi mở.",
        "black_box_warnings": "NGUY CƠ TĂNG NHÃN ÁP VÀ ĐỤC THỦY TINH THỂ nếu dùng kéo dài. CHỐNG CHỈ ĐỊNH ở nhiễm trùng mắt do virus/nấm. Ức chế miễn dịch, tăng nguy cơ nhiễm trùng nếu dùng kéo dài. Phải theo dõi nhãn áp định kỳ.",
        "drug_interactions": {
            "major": [],
            "moderate": [],
            "minor": []
        },
        "contraindications": {
            "tuyệt_đối": [
                "Dị ứng prednisolone hoặc corticosteroid",
                "Nhiễm trùng mắt do virus (herpes simplex, varicella) - CHỐNG CHỈ ĐỊNH (có thể làm nặng)",
                "Nhiễm trùng mắt do nấm - CHỐNG CHỈ ĐỊNH (có thể làm nặng)",
                "Nhiễm trùng mắt do vi khuẩn chưa điều trị - CHỐNG CHỈ ĐỊNH (có thể làm nặng)"
            ],
            "tương_đối": [
                "Tăng nhãn áp (glaucoma) - thận trọng, theo dõi nhãn áp định kỳ",
                "Đục thủy tinh thể (cataract) - thận trọng, có thể làm nặng",
                "Bệnh nhân đeo kính áp tròng - thận trọng (benzalkonium chloride)",
                "Có thai (category C) - thận trọng"
            ]
        },
        "pregnancy_lactation": {
            "fda_category": "C",
            "pregnancy_details": "Prednisolone là thuốc phân loại C. Prednisolone có thể hấp thu toàn thân và qua nhau thai. Corticosteroid có thể gây dị tật bẩm sinh ở động vật. Có thể dùng khi lợi ích vượt quá nguy cơ, đặc biệt khi không có lựa chọn khác.",
            "lactation": {
                "safety": "Compatible with Caution",
                "details": "Prednisolone có thể hấp thu toàn thân và bài tiết vào sữa mẹ. Tuy nhiên, nồng độ trong sữa mẹ thấp khi dùng tại mắt và không có báo cáo về tác dụng phụ đáng kể ở trẻ bú mẹ.",
                "recommendation": "Có thể dùng khi cho con bú, nhưng thận trọng. Nồng độ trong sữa mẹ thấp."
            }
        },
        "hepatic_adjustment": {
            "mild": "Không cần điều chỉnh liều",
            "moderate": "Không cần điều chỉnh liều",
            "severe": "Không cần điều chỉnh liều (ophthalmic, hấp thu tối thiểu)",
            "notes": "Prednisolone dùng tại mắt, hấp thu toàn thân tối thiểu. Không cần điều chỉnh liều ở bệnh nhân suy gan."
        },
        "overdose_management": {
            "symptoms": [
                "Kích ứng mắt nặng",
                "Tăng nhãn áp nặng (nếu dùng kéo dài)",
                "Đục thủy tinh thể (nếu dùng kéo dài)",
                "Nhiễm trùng mắt (nếu dùng kéo dài)"
            ],
            "antidote": "Không có antidote đặc hiệu. Rửa mắt, điều trị hỗ trợ. Giảm liều hoặc ngừng nếu có tác dụng phụ nặng.",
            "treatment": [
                "Rửa mắt ngay với nước sạch hoặc nước muối sinh lý",
                "Nếu kích ứng mắt nặng:",
                "  - Khám mắt ngay",
                "  - Điều trị hỗ trợ (nước mắt nhân tạo)",
                "Nếu tăng nhãn áp nặng:",
                "  - Ngừng prednisolone",
                "  - Điều trị tăng nhãn áp (thuốc giảm nhãn áp)",
                "Nếu nhiễm trùng mắt:",
                "  - Ngừng prednisolone",
                "  - Điều trị nhiễm trùng (kháng sinh, kháng virus, kháng nấm)",
                "Theo dõi: Thị lực, nhãn áp, dấu hiệu viêm, dấu hiệu nhiễm trùng"
            ],
            "monitoring": "Theo dõi thị lực, nhãn áp, dấu hiệu viêm, dấu hiệu nhiễm trùng cho đến khi hồi phục. Theo dõi lâu hơn nếu có biến chứng (tăng nhãn áp, đục thủy tinh thể, nhiễm trùng)."
        },
        "reversal_agents": None,
        "administration_instructions": {
            "oral": None,
            "ophthalmic": {
                "preparation": "Dạng dung dịch nhỏ mắt 0.12%, 0.5%, hoặc 1%.",
                "application": "1-2 giọt vào mắt bị ảnh hưởng theo lịch trình (xem dosage). Nhắm mắt nhẹ 1-2 phút sau khi nhỏ. Nhấn nhẹ vào góc trong mắt (lacrimal sac) trong 1-2 phút để giảm hấp thu toàn thân.",
                "timing": "Tùy theo chỉ định: 4-6 lần/ngày (conjunctivitis, postoperative) hoặc mỗi giờ (uveitis).",
                "contact_lenses": "Tháo kính áp tròng trước khi nhỏ. Đợi 15 phút trước khi đeo lại.",
                "notes": "QUAN TRỌNG: 1) CHỐNG CHỈ ĐỊNH ở nhiễm trùng mắt do virus/nấm, 2) NGUY CƠ TĂNG NHÃN ÁP VÀ ĐỤC THỦY TINH THỂ nếu dùng kéo dài, 3) Theo dõi nhãn áp định kỳ, 4) Giảm dần liều khi cải thiện, 5) Tránh chạm đầu lọ vào mắt hoặc bất kỳ bề mặt nào."
            }
        },
        "references": {
            "primary_sources": [
                "FDA Drug Label - Prednisolone (Pred Forte)",
                "UpToDate - Prednisolone: Drug Information",
                "Medscape - Prednisolone Drug Reference",
                "AAO Guidelines - Uveitis"
            ],
            "last_updated": "2025-02-18",
            "evidence_level": "A - Dựa trên FDA drug labels, clinical guidelines, và dữ liệu lâm sàng từ nhiều nguồn"
        }
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
        }
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
        }
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
        }
    },
    
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
        }
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
        "pregnancy": "C - Thận trọng",
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
        }
    },
    
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
        }
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
        }
    },
    
    "Bimatoprost eye drops": {
        "group": "Ophthalmology - Prostaglandin Analog (Glaucoma)",
        "vietnamese_name": "Bimatoprost nhỏ mắt, Lumigan",
        "administration": ["Ophthalmic"],
        "indications": [
            "Tăng nhãn áp góc mở (open-angle glaucoma)",
            "Tăng nhãn áp (ocular hypertension)",
            "Giảm nhãn áp (first-line treatment)",
            "Tăng trưởng lông mi (eyelash growth) - off-label"
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
            "Viêm mi mắt (blepharitis)",
            "Viêm màng bồ đào (hiếm)",
            "Viêm giác mạc (hiếm)",
            "Phù hoàng điểm (macular edema) - hiếm, ở bệnh nhân có tiền sử"
        ],
        "interactions": [
            "Không có tương tác đáng kể với thuốc khác (ophthalmic)"
        ],
        "pregnancy": "C - Thận trọng",
        "mechanism_of_action": "Bimatoprost là prostaglandin analog (prostamide), tương tự prostaglandin F2-alpha (PGF2α). Gắn với thụ thể prostaglandin F trên cơ trơn mống mắt và cơ thể mi, dẫn đến: (1) Tăng dẫn lưu thủy dịch qua đường uveoscleral (tăng outflow), (2) Giảm sản xuất thủy dịch (nhẹ), (3) Giảm nhãn áp. Bimatoprost là thuốc first-line cho tăng nhãn áp, tác dụng mạnh (giảm nhãn áp 25-35%), dùng 1 lần/ngày. ĐẶC ĐIỂM: (1) Tác dụng mạnh, giảm nhãn áp 25-35%, (2) Dùng 1 lần/ngày (buổi tối), (3) Thay đổi màu mắt (tăng sắc tố mống mắt) - vĩnh viễn, phổ biến, (4) Thay đổi lông mi (dài, đậm, đổi màu) - phổ biến, (5) Nguy cơ phù hoàng điểm ở bệnh nhân có tiền sử (viêm màng bồ đào, đái tháo đường, phẫu thuật mắt), (6) Có thể dùng để tăng trưởng lông mi (off-label).",
        "monitoring": [
            "Nhãn áp (intraocular pressure - IOP) - mục tiêu: <21 mmHg",
            "Thị lực và khám mắt định kỳ",
            "Dấu hiệu thay đổi màu mắt (tăng sắc tố mống mắt)",
            "Dấu hiệu thay đổi lông mi (dài, đậm, đổi màu)",
            "Dấu hiệu phù hoàng điểm (giảm thị lực, nhìn mờ) - ở bệnh nhân có tiền sử",
            "Dấu hiệu viêm màng bồ đào, viêm giác mạc - hiếm"
        ],
        "precautions": [
            "Thay đổi màu mắt (tăng sắc tố mống mắt) - vĩnh viễn, phổ biến, cần tư vấn bệnh nhân",
            "Thay đổi lông mi (dài, đậm, đổi màu) - phổ biến, có thể là tác dụng mong muốn (off-label)",
            "Nguy cơ phù hoàng điểm ở bệnh nhân có tiền sử (viêm màng bồ đào, đái tháo đường, phẫu thuật mắt) - cần theo dõi chặt chẽ",
            "Dùng buổi tối để tối ưu hiệu quả",
            "Tránh chạm đầu lọ vào mắt hoặc bất kỳ bề mặt nào (nguy cơ nhiễm trùng)",
            "Tháo kính áp tròng trước khi nhỏ (benzalkonium chloride có thể làm hỏng kính)",
            "Đợi 15 phút trước khi đeo lại kính áp tròng",
            "Không dùng chung lọ với người khác"
        ],
        "pharmacokinetics": {
            "half_life": "Không áp dụng (ophthalmic)",
            "onset": "Vài giờ",
            "duration": "24 giờ (dùng 1 lần/ngày)",
            "protein_binding": "Không áp dụng (ophthalmic)",
            "metabolism": "Chuyển hóa tại mắt",
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
                "Dị ứng bimatoprost hoặc benzalkonium chloride",
                "Viêm màng bồ đào (uveitis) hoạt động - CHỐNG CHỈ ĐỊNH",
                "Viêm giác mạc (keratitis) hoạt động - CHỐNG CHỈ ĐỊNH"
            ],
            "tương_đối": [
                "Trẻ em <18 tuổi - thận trọng",
                "Bệnh nhân có tiền sử phù hoàng điểm - thận trọng, theo dõi chặt chẽ",
                "Bệnh nhân có tiền sử viêm màng bồ đào, đái tháo đường, phẫu thuật mắt - thận trọng"
            ]
        },
        "pregnancy_lactation": {
            "fda_category": "C",
            "pregnancy_details": "Bimatoprost là thuốc phân loại C. Không hấp thu toàn thân khi dùng tại mắt. Có thể dùng trong thai kỳ khi lợi ích vượt quá nguy cơ.",
            "lactation": {
                "safety": "Compatible",
                "details": "Bimatoprost không hấp thu toàn thân khi dùng tại mắt, không bài tiết vào sữa mẹ. An toàn khi cho con bú.",
                "recommendation": "Có thể dùng khi cho con bú. An toàn, không có tác dụng phụ."
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
                "Đỏ mắt nặng",
                "Phù hoàng điểm (nếu có tiền sử)"
            ],
            "antidote": "Không có antidote đặc hiệu. Ngừng thuốc, điều trị hỗ trợ.",
            "treatment": [
                "Ngừng ngay bimatoprost",
                "Rửa mắt ngay với nước sạch hoặc nước muối sinh lý",
                "Nếu kích ứng mắt nặng:",
                "  - Khám mắt ngay",
                "  - Điều trị hỗ trợ (nước mắt nhân tạo, thuốc chống viêm nếu cần)",
                "Nếu phù hoàng điểm:",
                "  - Khám mắt ngay",
                "  - Điều trị phù hoàng điểm (corticosteroid tại chỗ, nếu cần)",
                "Theo dõi: Thị lực, nhãn áp, dấu hiệu kích ứng mắt, dấu hiệu phù hoàng điểm"
            ],
            "monitoring": "Theo dõi thị lực, nhãn áp, dấu hiệu kích ứng mắt, dấu hiệu phù hoàng điểm cho đến khi hồi phục."
        },
        "reversal_agents": None,
        "administration_instructions": {
            "oral": None,
            "ophthalmic": {
                "preparation": "Dạng dung dịch nhỏ mắt 0.01% hoặc 0.03%.",
                "application": "1 giọt vào mắt bị ảnh hưởng 1 lần/ngày (buổi tối). Nhắm mắt nhẹ 1-2 phút sau khi nhỏ. Nhấn nhẹ vào góc trong mắt (lacrimal sac) trong 1-2 phút để giảm hấp thu toàn thân.",
                "timing": "1 lần/ngày (buổi tối) để tối ưu hiệu quả.",
                "contact_lenses": "Tháo kính áp tròng trước khi nhỏ. Đợi 15 phút trước khi đeo lại.",
                "notes": "QUAN TRỌNG: 1) Dùng buổi tối để tối ưu hiệu quả, 2) Thay đổi màu mắt (tăng sắc tố mống mắt) - vĩnh viễn, phổ biến, 3) Thay đổi lông mi (dài, đậm, đổi màu) - phổ biến, 4) Nguy cơ phù hoàng điểm ở bệnh nhân có tiền sử, 5) Tránh chạm đầu lọ vào mắt, 6) Tháo kính áp tròng trước khi nhỏ."
            }
        },
        "references": {
            "primary_sources": [
                "FDA Drug Label - Bimatoprost (Lumigan)",
                "UpToDate - Bimatoprost: Drug Information",
                "Medscape - Bimatoprost Drug Reference",
                "AAO Guidelines - Glaucoma Treatment"
            ],
            "last_updated": "2025-02-18",
            "evidence_level": "A - Dựa trên FDA drug labels, clinical guidelines, và dữ liệu lâm sàng từ nhiều nguồn"
        }
    },
    
    "Travoprost eye drops": {
        "group": "Ophthalmology - Prostaglandin Analog (Glaucoma)",
        "vietnamese_name": "Travoprost nhỏ mắt, Travatan",
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
            "notes": "Travoprost là prostaglandin F2-alpha (PGF2α) analog, tương tự latanoprost. Tác dụng mạnh, giảm nhãn áp 25-35%. Dùng buổi tối để tối ưu hiệu quả. Có thể gây thay đổi màu mắt (tăng sắc tố mống mắt) và lông mi (dài, đậm, đổi màu)."
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
            "Viêm mi mắt (blepharitis)",
            "Viêm màng bồ đào (hiếm)",
            "Viêm giác mạc (hiếm)",
            "Phù hoàng điểm (macular edema) - hiếm, ở bệnh nhân có tiền sử"
        ],
        "interactions": [
            "Không có tương tác đáng kể với thuốc khác (ophthalmic)"
        ],
        "pregnancy": "C - Thận trọng",
        "mechanism_of_action": "Travoprost là prostaglandin F2-alpha (PGF2α) analog. Gắn với thụ thể prostaglandin F trên cơ trơn mống mắt và cơ thể mi, dẫn đến: (1) Tăng dẫn lưu thủy dịch qua đường uveoscleral (tăng outflow), (2) Giảm sản xuất thủy dịch (nhẹ), (3) Giảm nhãn áp. Travoprost là thuốc first-line cho tăng nhãn áp, tác dụng mạnh (giảm nhãn áp 25-35%), dùng 1 lần/ngày. ĐẶC ĐIỂM: (1) Tác dụng mạnh, giảm nhãn áp 25-35%, (2) Dùng 1 lần/ngày (buổi tối), (3) Thay đổi màu mắt (tăng sắc tố mống mắt) - vĩnh viễn, phổ biến, (4) Thay đổi lông mi (dài, đậm, đổi màu) - phổ biến, (5) Nguy cơ phù hoàng điểm ở bệnh nhân có tiền sử (viêm màng bồ đào, đái tháo đường, phẫu thuật mắt), (6) Tương tự latanoprost và bimatoprost.",
        "monitoring": [
            "Nhãn áp (intraocular pressure - IOP) - mục tiêu: <21 mmHg",
            "Thị lực và khám mắt định kỳ",
            "Dấu hiệu thay đổi màu mắt (tăng sắc tố mống mắt)",
            "Dấu hiệu thay đổi lông mi (dài, đậm, đổi màu)",
            "Dấu hiệu phù hoàng điểm (giảm thị lực, nhìn mờ) - ở bệnh nhân có tiền sử",
            "Dấu hiệu viêm màng bồ đào, viêm giác mạc - hiếm"
        ],
        "precautions": [
            "Thay đổi màu mắt (tăng sắc tố mống mắt) - vĩnh viễn, phổ biến, cần tư vấn bệnh nhân",
            "Thay đổi lông mi (dài, đậm, đổi màu) - phổ biến",
            "Nguy cơ phù hoàng điểm ở bệnh nhân có tiền sử (viêm màng bồ đào, đái tháo đường, phẫu thuật mắt) - cần theo dõi chặt chẽ",
            "Dùng buổi tối để tối ưu hiệu quả",
            "Tránh chạm đầu lọ vào mắt hoặc bất kỳ bề mặt nào (nguy cơ nhiễm trùng)",
            "Tháo kính áp tròng trước khi nhỏ (benzalkonium chloride có thể làm hỏng kính)",
            "Đợi 15 phút trước khi đeo lại kính áp tròng",
            "Không dùng chung lọ với người khác"
        ],
        "pharmacokinetics": {
            "half_life": "Không áp dụng (ophthalmic)",
            "onset": "Vài giờ",
            "duration": "24 giờ (dùng 1 lần/ngày)",
            "protein_binding": "Không áp dụng (ophthalmic)",
            "metabolism": "Chuyển hóa tại mắt",
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
                "Dị ứng travoprost hoặc benzalkonium chloride",
                "Viêm màng bồ đào (uveitis) hoạt động - CHỐNG CHỈ ĐỊNH",
                "Viêm giác mạc (keratitis) hoạt động - CHỐNG CHỈ ĐỊNH"
            ],
            "tương_đối": [
                "Trẻ em <18 tuổi - thận trọng",
                "Bệnh nhân có tiền sử phù hoàng điểm - thận trọng, theo dõi chặt chẽ",
                "Bệnh nhân có tiền sử viêm màng bồ đào, đái tháo đường, phẫu thuật mắt - thận trọng"
            ]
        },
        "pregnancy_lactation": {
            "fda_category": "C",
            "pregnancy_details": "Travoprost là thuốc phân loại C. Không hấp thu toàn thân khi dùng tại mắt. Có thể dùng trong thai kỳ khi lợi ích vượt quá nguy cơ.",
            "lactation": {
                "safety": "Compatible",
                "details": "Travoprost không hấp thu toàn thân khi dùng tại mắt, không bài tiết vào sữa mẹ. An toàn khi cho con bú.",
                "recommendation": "Có thể dùng khi cho con bú. An toàn, không có tác dụng phụ."
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
                "Đỏ mắt nặng",
                "Phù hoàng điểm (nếu có tiền sử)"
            ],
            "antidote": "Không có antidote đặc hiệu. Ngừng thuốc, điều trị hỗ trợ.",
            "treatment": [
                "Ngừng ngay travoprost",
                "Rửa mắt ngay với nước sạch hoặc nước muối sinh lý",
                "Nếu kích ứng mắt nặng:",
                "  - Khám mắt ngay",
                "  - Điều trị hỗ trợ (nước mắt nhân tạo, thuốc chống viêm nếu cần)",
                "Nếu phù hoàng điểm:",
                "  - Khám mắt ngay",
                "  - Điều trị phù hoàng điểm (corticosteroid tại chỗ, nếu cần)",
                "Theo dõi: Thị lực, nhãn áp, dấu hiệu kích ứng mắt, dấu hiệu phù hoàng điểm"
            ],
            "monitoring": "Theo dõi thị lực, nhãn áp, dấu hiệu kích ứng mắt, dấu hiệu phù hoàng điểm cho đến khi hồi phục."
        },
        "reversal_agents": None,
        "administration_instructions": {
            "oral": None,
            "ophthalmic": {
                "preparation": "Dạng dung dịch nhỏ mắt 0.004%.",
                "application": "1 giọt vào mắt bị ảnh hưởng 1 lần/ngày (buổi tối). Nhắm mắt nhẹ 1-2 phút sau khi nhỏ. Nhấn nhẹ vào góc trong mắt (lacrimal sac) trong 1-2 phút để giảm hấp thu toàn thân.",
                "timing": "1 lần/ngày (buổi tối) để tối ưu hiệu quả.",
                "contact_lenses": "Tháo kính áp tròng trước khi nhỏ. Đợi 15 phút trước khi đeo lại.",
                "notes": "QUAN TRỌNG: 1) Dùng buổi tối để tối ưu hiệu quả, 2) Thay đổi màu mắt (tăng sắc tố mống mắt) - vĩnh viễn, phổ biến, 3) Thay đổi lông mi (dài, đậm, đổi màu) - phổ biến, 4) Nguy cơ phù hoàng điểm ở bệnh nhân có tiền sử, 5) Tránh chạm đầu lọ vào mắt, 6) Tháo kính áp tròng trước khi nhỏ."
            }
        },
        "references": {
            "primary_sources": [
                "FDA Drug Label - Travoprost (Travatan)",
                "UpToDate - Travoprost: Drug Information",
                "Medscape - Travoprost Drug Reference",
                "AAO Guidelines - Glaucoma Treatment"
            ],
            "last_updated": "2025-02-18",
            "evidence_level": "A - Dựa trên FDA drug labels, clinical guidelines, và dữ liệu lâm sàng từ nhiều nguồn"
        }
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
        }
    },
    
    "Ketorolac eye drops": {
        "group": "Ophthalmology - NSAID (Anti-inflammatory)",
        "vietnamese_name": "Ketorolac, Acular",
        "administration": ["Ophthalmic"],
        "indications": [
            "Điều trị viêm sau phẫu thuật mắt (postoperative inflammation)",
            "Giảm đau sau phẫu thuật mắt (postoperative pain)",
            "Điều trị viêm kết mạc dị ứng (allergic conjunctivitis)",
            "Giảm đau và viêm trong viêm màng bồ đào (uveitis)",
            "Dự phòng và điều trị phù hoàng điểm dạng nang (cystoid macular edema - CME) sau phẫu thuật mắt"
        ],
        "contraindications": [
            "Dị ứng ketorolac hoặc NSAID",
            "Loét dạ dày tá tràng hoạt động",
            "Xuất huyết tiêu hóa gần đây",
            "Suy thận nặng",
            "Suy gan nặng",
            "Rối loạn đông máu nặng",
            "Trẻ em <3 tuổi (thận trọng)"
        ],
        "dosage": {
            "adult_postop_inflammation": "1 giọt vào mắt phẫu thuật x 4 lần/ngày bắt đầu 24 giờ sau phẫu thuật, trong 2 tuần",
            "adult_allergic_conjunctivitis": "1 giọt vào mắt bị ảnh hưởng x 4 lần/ngày",
            "adult_cme_prophylaxis": "1 giọt vào mắt phẫu thuật x 4 lần/ngày bắt đầu 24 giờ sau phẫu thuật, trong 4 tuần",
            "notes": "Ketorolac là NSAID tại chỗ, ức chế cyclooxygenase (COX), giảm viêm và đau. Dùng 4 lần/ngày. Có thể hấp thu toàn thân và gây tác dụng phụ hệ thống (loét dạ dày, suy thận)."
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "Thận trọng, theo dõi chức năng thận",
            "under_30": "CHỐNG CHỈ ĐỊNH hoặc dùng rất thận trọng"
        },
        "side_effects": [
            "Kích ứng mắt tại chỗ (đỏ, rát, ngứa, châm chích) - phổ biến",
            "Nhìn mờ tạm thời",
            "Khô mắt",
            "Đau mắt",
            "Hấp thu toàn thân: loét dạ dày tá tràng - hiếm nhưng nghiêm trọng",
            "Hấp thu toàn thân: suy thận cấp - hiếm nhưng nghiêm trọng",
            "Hấp thu toàn thân: xuất huyết tiêu hóa - hiếm nhưng nghiêm trọng",
            "Hấp thu toàn thân: rối loạn đông máu - hiếm",
            "Phản ứng dị ứng (phát ban, ngứa) - hiếm"
        ],
        "interactions": [
            "NSAID đường uống (aspirin, ibuprofen, naproxen): tăng nguy cơ loét dạ dày, suy thận",
            "Warfarin, thuốc chống đông: tăng nguy cơ xuất huyết",
            "ACE inhibitors, ARBs: tăng nguy cơ suy thận",
            "Corticosteroid: tăng nguy cơ loét dạ dày",
            "Lithium: tăng nồng độ lithium"
        ],
        "pregnancy": "C - Thận trọng",
        "mechanism_of_action": "Ketorolac là NSAID (nonsteroidal anti-inflammatory drug). Ức chế enzyme cyclooxygenase (COX-1 và COX-2), ngăn chặn sự tổng hợp prostaglandin từ arachidonic acid. Prostaglandin là chất trung gian gây viêm, đau, và sốt. Giảm prostaglandin dẫn đến: (1) Giảm viêm (giảm đỏ, sưng), (2) Giảm đau, (3) Giảm phù hoàng điểm dạng nang (CME) sau phẫu thuật mắt. ĐẶC ĐIỂM: (1) NSAID tại chỗ, ức chế COX, (2) Dùng 4 lần/ngày, (3) Có thể hấp thu toàn thân và gây tác dụng phụ hệ thống (loét dạ dày, suy thận), (4) CHỐNG CHỈ ĐỊNH ở suy thận nặng, loét dạ dày hoạt động, (5) Kích ứng mắt phổ biến, (6) Hiệu quả cho viêm và đau sau phẫu thuật mắt, CME.",
        "monitoring": [
            "Đáp ứng lâm sàng (giảm đỏ, sưng, đau) - cải thiện sau 2-3 ngày",
            "Dấu hiệu kích ứng mắt (đỏ, rát, ngứa, châm chích tăng)",
            "Dấu hiệu hấp thu toàn thân: đau bụng, xuất huyết tiêu hóa (phân đen, nôn ra máu) - NGUY HIỂM",
            "Dấu hiệu hấp thu toàn thân: suy thận (giảm lượng nước tiểu, phù) - NGUY HIỂM",
            "Chức năng thận (creatinine, eGFR) - nếu dùng kéo dài hoặc có nguy cơ",
            "Thị lực (nhìn mờ tạm thời)"
        ],
        "precautions": [
            "CHỐNG CHỈ ĐỊNH ở suy thận nặng, loét dạ dày hoạt động, xuất huyết tiêu hóa gần đây",
            "Kích ứng mắt - phổ biến, thường giảm sau vài ngày",
            "Hấp thu toàn thân - có thể gây loét dạ dày, suy thận, xuất huyết tiêu hóa",
            "TRÁNH DÙNG với NSAID đường uống - tăng nguy cơ loét dạ dày, suy thận",
            "Thận trọng ở bệnh nhân dùng warfarin, thuốc chống đông - tăng nguy cơ xuất huyết",
            "Thận trọng ở bệnh nhân dùng ACE inhibitors, ARBs - tăng nguy cơ suy thận",
            "Thận trọng ở bệnh nhân cao tuổi - tăng nguy cơ tác dụng phụ",
            "Tránh chạm đầu lọ vào mắt hoặc bất kỳ bề mặt nào (nguy cơ nhiễm trùng)",
            "Nhìn mờ tạm thời - bệnh nhân không nên lái xe ngay sau khi nhỏ"
        ],
        "pharmacokinetics": {
            "half_life": "Không áp dụng (ophthalmic)",
            "onset": "Vài giờ",
            "duration": "4-6 giờ (dùng 4 lần/ngày)",
            "protein_binding": "Không áp dụng (ophthalmic)",
            "metabolism": "Chuyển hóa tại mắt và gan (nếu hấp thu toàn thân, CYP2C9, CYP3A4)",
            "clearance": "Thải trừ tại chỗ, hấp thu toàn thân tối thiểu"
        },
        "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ánh sáng. Đóng nắp kín sau khi dùng. Dùng trong 4 tuần sau khi mở.",
        "black_box_warnings": "Nguy cơ loét dạ dày tá tràng, xuất huyết tiêu hóa, suy thận cấp nếu hấp thu toàn thân. CHỐNG CHỈ ĐỊNH ở suy thận nặng, loét dạ dày hoạt động, xuất huyết tiêu hóa gần đây. TRÁNH DÙNG với NSAID đường uống.",
        "drug_interactions": {
            "major": [
                {
                    "drug": "NSAID đường uống (Aspirin, Ibuprofen, Naproxen, Diclofenac)",
                    "mechanism": "Cả hai đều ức chế COX, tác dụng cộng dồn",
                    "effect": "Tăng nguy cơ loét dạ dày tá tràng, xuất huyết tiêu hóa, suy thận cấp",
                    "management": "TRÁNH DÙNG CHUNG. Nếu bắt buộc, theo dõi dấu hiệu loét dạ dày, suy thận sát."
                },
                {
                    "drug": "Warfarin, Thuốc chống đông (Heparin, Enoxaparin, Dabigatran, Rivaroxaban)",
                    "mechanism": "NSAID ức chế COX-1, giảm sản xuất thromboxane, tăng nguy cơ xuất huyết",
                    "effect": "Tăng nguy cơ xuất huyết (đặc biệt xuất huyết tiêu hóa)",
                    "management": "Thận trọng. Theo dõi INR, dấu hiệu xuất huyết sát."
                }
            ],
            "moderate": [
                {
                    "drug": "ACE Inhibitors, ARBs (Lisinopril, Losartan, Valsartan)",
                    "mechanism": "NSAID giảm sản xuất prostaglandin, giảm lưu lượng máu thận, tác dụng cộng dồn với ACE inhibitors/ARBs",
                    "effect": "Tăng nguy cơ suy thận cấp",
                    "management": "Thận trọng. Theo dõi chức năng thận sát."
                },
                {
                    "drug": "Corticosteroid (Prednisone, Dexamethasone)",
                    "mechanism": "Cả hai đều tăng nguy cơ loét dạ dày",
                    "effect": "Tăng nguy cơ loét dạ dày tá tràng, xuất huyết tiêu hóa",
                    "management": "Thận trọng. Có thể cần dùng PPI (proton pump inhibitor) để bảo vệ dạ dày."
                }
            ],
            "minor": []
        },
        "contraindications": {
            "tuyệt_đối": [
                "Dị ứng ketorolac hoặc NSAID",
                "Loét dạ dày tá tràng hoạt động - CHỐNG CHỈ ĐỊNH",
                "Xuất huyết tiêu hóa gần đây - CHỐNG CHỈ ĐỊNH",
                "Suy thận nặng (CrCl <30 mL/min) - CHỐNG CHỈ ĐỊNH",
                "Suy gan nặng - CHỐNG CHỈ ĐỊNH",
                "Rối loạn đông máu nặng - CHỐNG CHỈ ĐỊNH"
            ],
            "tương_đối": [
                "Suy thận trung bình (CrCl 30-60 mL/min) - thận trọng, theo dõi chức năng thận",
                "Bệnh nhân cao tuổi - tăng nguy cơ tác dụng phụ",
                "Dùng với NSAID đường uống - tăng nguy cơ loét dạ dày, suy thận",
                "Dùng với warfarin, thuốc chống đông - tăng nguy cơ xuất huyết",
                "Dùng với ACE inhibitors, ARBs - tăng nguy cơ suy thận",
                "Trẻ em <3 tuổi - thận trọng"
            ]
        },
        "pregnancy_lactation": {
            "fda_category": "C",
            "pregnancy_details": "Ketorolac là thuốc phân loại C. NSAID có thể qua nhau thai và gây tác dụng phụ ở thai nhi (đóng sớm ống động mạch, suy thận). Tránh dùng trong tam cá nguyệt thứ ba. Có thể dùng khi lợi ích vượt quá nguy cơ, đặc biệt trong tam cá nguyệt thứ nhất và thứ hai.",
            "lactation": {
                "safety": "Compatible with Caution",
                "details": "Ketorolac có thể hấp thu toàn thân và bài tiết vào sữa mẹ ở nồng độ thấp. Tuy nhiên, nồng độ trong sữa mẹ thấp khi dùng tại mắt và không có báo cáo về tác dụng phụ đáng kể ở trẻ bú mẹ.",
                "recommendation": "Có thể dùng khi cho con bú, nhưng thận trọng. Nồng độ trong sữa mẹ thấp."
            }
        },
        "hepatic_adjustment": {
            "mild": "Không cần điều chỉnh liều",
            "moderate": "Thận trọng. Chuyển hóa qua gan có thể giảm, tăng nồng độ ketorolac và nguy cơ tác dụng phụ.",
            "severe": "CHỐNG CHỈ ĐỊNH. Chuyển hóa qua gan giảm đáng kể, tăng nguy cơ bệnh gan và tác dụng phụ nặng.",
            "notes": "Ketorolac chuyển hóa qua gan (CYP2C9, CYP3A4). Suy gan có thể làm giảm chuyển hóa, tăng nồng độ và nguy cơ bệnh gan, tác dụng phụ nặng."
        },
        "overdose_management": {
            "symptoms": [
                "Kích ứng mắt nặng",
                "Hấp thu toàn thân: đau bụng nặng, xuất huyết tiêu hóa (phân đen, nôn ra máu) - NGUY HIỂM",
                "Hấp thu toàn thân: suy thận cấp (giảm lượng nước tiểu, phù) - NGUY HIỂM",
                "Hấp thu toàn thân: rối loạn đông máu (xuất huyết) - NGUY HIỂM"
            ],
            "antidote": "Không có antidote đặc hiệu. Điều trị hỗ trợ.",
            "treatment": [
                "Rửa mắt ngay với nước sạch hoặc nước muối sinh lý",
                "Nếu hấp thu toàn thân nặng:",
                "  - Ngừng ngay ketorolac",
                "  - Nếu xuất huyết tiêu hóa:",
                "    - Hỗ trợ huyết động (truyền dịch, máu nếu cần)",
                "    - Nội soi dạ dày nếu cần",
                "    - PPI (omeprazole, pantoprazole) để giảm acid dạ dày",
                "  - Nếu suy thận cấp:",
                "    - Hỗ trợ huyết động",
                "    - Lọc máu nếu cần",
                "  - Theo dõi dấu hiệu sinh tồn, chức năng thận, đông máu",
                "Theo dõi: Dấu hiệu sinh tồn, lượng nước tiểu, chức năng thận, dấu hiệu xuất huyết"
            ],
            "monitoring": "Theo dõi dấu hiệu sinh tồn, lượng nước tiểu, chức năng thận, dấu hiệu xuất huyết cho đến khi hồi phục. Theo dõi lâu hơn nếu có biến chứng (xuất huyết tiêu hóa, suy thận cấp)."
        },
        "reversal_agents": None,
        "administration_instructions": {
            "ophthalmic": {
                "preparation": "Dạng dung dịch nhỏ mắt 0.4% hoặc 0.5%.",
                "application": "1 giọt vào mắt bị ảnh hưởng x 4 lần/ngày. Nhắm mắt nhẹ 1-2 phút sau khi nhỏ. Nhấn nhẹ vào góc trong mắt (lacrimal sac) trong 1-2 phút để giảm hấp thu toàn thân.",
                "timing": "4 lần/ngày. Bắt đầu 24 giờ sau phẫu thuật mắt cho điều trị viêm sau phẫu thuật.",
                "contact_lenses": "Tháo kính áp tròng trước khi nhỏ. Đợi 15 phút trước khi đeo lại.",
                "notes": "QUAN TRỌNG: 1) CHỐNG CHỈ ĐỊNH ở suy thận nặng, loét dạ dày hoạt động, 2) TRÁNH DÙNG với NSAID đường uống, 3) Kích ứng mắt phổ biến, 4) Hấp thu toàn thân có thể gây loét dạ dày, suy thận, 5) Nhìn mờ tạm thời - không lái xe ngay."
            }
        },
        "references": {
            "primary_sources": [
                "FDA Drug Label - Ketorolac (Acular)",
                "UpToDate - Ketorolac: Drug Information",
                "Medscape - Ketorolac Drug Reference",
                "AAO Guidelines - Postoperative Inflammation, CME"
            ],
            "last_updated": "2025-02-18",
            "evidence_level": "A - Dựa trên FDA drug labels, clinical guidelines, và dữ liệu lâm sàng từ nhiều nguồn"
        }
    }
}

__all__ = ['OPHTHALMOLOGY_DRUGS']

