"""
SSRI (Selective Serotonin Reuptake Inhibitor) Drugs
"""

SSRI_DRUGS = {
    "Sertraline": {
        "group": "Psychiatry - SSRI (Selective Serotonin Reuptake Inhibitor)",
        "vietnamese_name": "Sertraline, Zoloft",
        "administration": ["PO"],
        "indications": [
            "Trầm cảm",
            "Rối loạn lo âu",
            "Rối loạn ám ảnh cưỡng chế (OCD)",
            "Rối loạn stress sau sang chấn (PTSD)",
            "Rối loạn hoảng sợ"
        ],
        "contraindications": [
            "Dùng MAO inhibitor",
            "Dị ứng"
        ],
        "dosage": {
            "adult_depression": "50mg x 1 lần/ngày, tăng đến 50-200mg/ngày",
            "adult_ocd": "50-200mg/ngày",
            "adult_max": "200mg/ngày",
            "notes": "Khởi đầu 25-50mg/ngày, tăng dần. Uống buổi sáng hoặc tối"
        },
        "side_effects": [
            "Buồn nôn",
            "Tiêu chảy",
            "Mất ngủ",
            "Giảm ham muốn tình dục",
            "Nhức đầu",
            "Khô miệng",
            "Hội chứng serotonin (với thuốc khác)"
        ],
        "interactions": [
            "MAO inhibitor: chống chỉ định",
            "Warfarin: có thể tăng tác dụng chống đông",
            "Tramadol: tăng nguy cơ co giật",
            "Triptans: tăng nguy cơ hội chứng serotonin"
        ],
        "pregnancy": "C",
        "mechanism_of_action": "Sertraline là SSRI ức chế tái hấp thu serotonin ở synap thần kinh, tăng nồng độ serotonin và dẫn đến tác dụng chống trầm cảm, chống lo âu. Có tính chọn lọc cao với serotonin. Cũng có tác dụng ức chế nhẹ tái hấp thu dopamine ở liều cao. Tác dụng trên nhiều chỉ định: trầm cảm, lo âu, OCD, PTSD, hoảng sợ. Ưu điểm: half-life trung bình, ít tương tác thuốc hơn fluoxetine, dùng 1 lần/ngày",
        "monitoring": [
            "Tâm trạng và triệu chứng trầm cảm, lo âu (đánh giá định kỳ)",
            "Dấu hiệu tự tử (tăng nguy cơ trong vài tuần đầu, đặc biệt ở <24 tuổi)",
            "Dấu hiệu hội chứng serotonin (nếu dùng với thuốc khác)",
            "INR nếu dùng với warfarin (tăng nguy cơ chảy máu)",
            "Triệu chứng tiêu hóa: buồn nôn, tiêu chảy (phổ biến)",
            "Dấu hiệu rút thuốc khi ngừng (chóng mặt, buồn nôn)"
        ],
        "precautions": [
            "KHÔNG dùng với MAO inhibitor (chống chỉ định tuyệt đối)",
            "Ngừng sertraline ít nhất 2 tuần trước khi bắt đầu MAO inhibitor",
            "Theo dõi sát dấu hiệu tự tử trong vài tuần đầu (tăng nguy cơ ở <24 tuổi)",
            "Giảm liều dần khi ngừng (tránh hội chứng rút thuốc)",
            "Thận trọng khi dùng với tramadol, triptans (tăng nguy cơ hội chứng serotonin)",
            "Thận trọng khi dùng với warfarin (tăng nguy cơ chảy máu)",
            "Có thể gây tiêu chảy (phổ biến) - thường tự hết sau vài tuần",
            "Khởi đầu với liều thấp (25-50mg), tăng dần"
        ],
        "pharmacokinetics": {
            "half_life": "26 giờ (trung bình)",
            "onset": "2-4 tuần (tác dụng chống trầm cảm)",
            "duration": "Dài (do half-life trung bình)",
            "protein_binding": "98% (rất cao)",
            "clearance": "Gan (chuyển hóa qua CYP2C9, CYP2C19, CYP2D6, CYP3A4), thận (thải trừ)"
        },
        "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm",
        "black_box_warnings": "Tăng nguy cơ tự tử ở trẻ em, thanh thiếu niên, và thanh niên <24 tuổi trong vài tháng đầu điều trị. Chống chỉ định với MAO inhibitor",
        "drug_interactions": {
            "major": [
                {
                    "drug": "MAO inhibitors",
                    "mechanism": "Tăng nồng độ serotonin",
                    "effect": "Hội chứng serotonin nghiêm trọng",
                    "management": "CHỐNG CHỈ ĐỊNH TUYỆT ĐỐI. Ngừng sertraline ít nhất 2 tuần trước khi bắt đầu MAO inhibitor."
                },
                {
                    "drug": "Tramadol",
                    "mechanism": "Tăng nồng độ serotonin, tăng nguy cơ co giật",
                    "effect": "Hội chứng serotonin, tăng nguy cơ co giật",
                    "management": "Tránh dùng cùng. Nếu bắt buộc, giảm liều tramadol và theo dõi sát."
                }
            ],
            "moderate": [
                {
                    "drug": "Warfarin",
                    "mechanism": "Có thể tăng nồng độ warfarin",
                    "effect": "Tăng INR, tăng nguy cơ chảy máu",
                    "management": "Theo dõi INR thường xuyên. Điều chỉnh liều warfarin nếu cần."
                },
                {
                    "drug": "Triptans",
                    "mechanism": "Tăng nồng độ serotonin",
                    "effect": "Hội chứng serotonin",
                    "management": "Thận trọng. Dùng cách xa ít nhất 24 giờ."
                }
            ],
            "minor": [
                {
                    "drug": "CYP2D6 substrates",
                    "mechanism": "Ức chế CYP2D6 nhẹ",
                    "effect": "Tăng nhẹ nồng độ các thuốc chuyển hóa qua CYP2D6",
                    "management": "Thận trọng. Điều chỉnh liều nếu cần."
                }
            ]
        },
        "contraindications": {
            "tuyệt_đối": [
                "Dùng MAO inhibitor (chống chỉ định tuyệt đối)",
                "Dị ứng sertraline"
            ],
            "tương_đối": [
                "Suy gan nặng - giảm liều",
                "Suy thận nặng (CrCl <30) - giảm liều",
                "Trẻ em <18 tuổi - tăng nguy cơ tự tử",
                "Có ý định tự tử - chỉ kê đơn số lượng ít",
                "Dùng với tramadol, triptans - tăng nguy cơ hội chứng serotonin"
            ]
        },
        "pregnancy_lactation": {
            "fda_category": "C",
            "pregnancy_details": "Dùng được trong thai kỳ nếu lợi ích > nguy cơ. Một số nghiên cứu gợi ý tăng nguy cơ dị tật thai nhi (dị tật tim) khi dùng trong 3 tháng đầu, nhưng chứng cứ không rõ ràng. Có thể gây tăng huyết áp phổi ở trẻ sơ sinh (PPHN) - nguy cơ thấp. Có thể gây hội chứng cai ở trẻ sơ sinh nếu dùng gần ngày sinh. Theo dõi trẻ sơ sinh sau sinh.",
            "lactation": {
                "safety": "Compatible",
                "details": "Sertraline bài tiết vào sữa mẹ ở nồng độ thấp. Nồng độ trong máu trẻ bú mẹ thường <1% nồng độ mẹ. An toàn cho trẻ bú mẹ. Ít báo cáo về tác dụng phụ ở trẻ.",
                "recommendation": "Có thể dùng khi cho con bú. Sertraline là SSRI được lựa chọn khi cho con bú do nồng độ trong sữa mẹ thấp. Theo dõi dấu hiệu buồn ngủ, bú kém ở trẻ."
            }
        },
        "hepatic_adjustment": {
            "mild": "Không đổi hoặc giảm liều nhẹ",
            "moderate": "Giảm liều 25-50%. Theo dõi chức năng gan",
            "severe": "Tránh dùng hoặc dùng liều rất thấp dưới sự giám sát chặt chẽ",
            "notes": "Sertraline chuyển hóa ở gan qua CYP2C9, CYP2C19, CYP2D6, CYP3A4. Suy gan làm giảm chuyển hóa, tăng nguy cơ tích lũy."
        },
        "overdose_management": {
            "symptoms": [
                "Buồn nôn, nôn, tiêu chảy",
                "Kích động, lú lẫn",
                "Nhịp tim nhanh",
                "Co giật",
                "Hôn mê",
                "Hội chứng serotonin (nếu dùng với thuốc khác)"
            ],
            "antidote": "Không có antidote đặc hiệu. Điều trị hỗ trợ",
            "treatment": [
                "Hỗ trợ hô hấp và tuần hoàn nếu cần",
                "Rửa dạ dày nếu uống trong vòng 1-2 giờ",
                "Than hoạt tính nếu uống trong vòng 1-2 giờ",
                "Theo dõi ECG, huyết áp, nhịp tim",
                "Điều trị hội chứng serotonin: Cyproheptadine, benzodiazepines",
                "Điều trị co giật: Benzodiazepines",
                "Truyền dịch",
                "Theo dõi ít nhất 24 giờ"
            ],
            "monitoring": "ECG, huyết áp, nhịp tim, ý thức, dấu hiệu co giật"
        },
        "reversal_agents": {
            "available": False,
            "agents": []
        },
        "administration_instructions": {
            "oral": {
                "with_food": "Có thể dùng với hoặc không có thức ăn. Dùng với thức ăn có thể giảm buồn nôn",
                "timing": "Dùng 1 lần/ngày (buổi sáng hoặc tối). Có thể dùng cùng bữa ăn để giảm tiêu chảy."
            },
            "iv": {
                "reconstitution": "Không có dạng IV",
                "infusion_rate": "N/A",
                "compatibility": [],
                "incompatibility": [],
                "notes": "Chỉ có dạng uống"
            }
        },
        "references": {
            "primary_sources": [
                "FDA Drug Label - Zoloft (sertraline)",
                "UpToDate - Sertraline: Drug information",
                "American Psychiatric Association guidelines"
            ],
            "last_updated": "2024-12-19",
            "evidence_level": "High - Multiple RCTs and systematic reviews"
        }
    },

    "Citalopram": {
        "group": "Psychiatry - SSRI",
        "vietnamese_name": "Citalopram, Celexa",
        "administration": ["PO"],
        "indications": [
            "Trầm cảm",
            "Rối loạn lo âu"
        ],
        "contraindications": [
            "Dùng MAO inhibitor",
            "QT prolongation",
            "Dị ứng"
        ],
        "dosage": {
            "adult_standard": "20mg x 1 lần/ngày, tăng đến 20-40mg/ngày",
            "adult_max": "40mg/ngày (20mg nếu >60 tuổi)",
            "notes": "Giới hạn 40mg/ngày do nguy cơ QT prolongation. Người già: max 20mg/ngày"
        },
        "side_effects": [
            "Buồn nôn",
            "Mất ngủ",
            "Nhức đầu",
            "QT prolongation (liều cao)",
            "Giảm ham muốn tình dục"
        ],
        "interactions": [
            "MAO inhibitor: chống chỉ định",
            "QT prolonging drugs: tăng nguy cơ rối loạn nhịp",
            "Warfarin: có thể tăng tác dụng"
        ],
        "pregnancy": "C",
        "mechanism_of_action": "Citalopram là SSRI ức chế tái hấp thu serotonin ở synap thần kinh, tăng nồng độ serotonin và dẫn đến tác dụng chống trầm cảm, chống lo âu. Có tính chọn lọc cao với serotonin. Citalopram là racemic mixture (R- và S-enantiomer). S-enantiomer (escitalopram) là chất hoạt động chính. Tác dụng: trầm cảm, lo âu. CẢNH BÁO: Có thể gây QT kéo dài ở liều >40mg/ngày, đặc biệt ở người già",
        "monitoring": [
            "Tâm trạng và triệu chứng trầm cảm, lo âu (đánh giá định kỳ)",
            "Dấu hiệu tự tử (tăng nguy cơ trong vài tuần đầu, đặc biệt ở <24 tuổi)",
            "ECG nếu dùng liều cao >40mg/ngày hoặc ở người già (QT kéo dài)",
            "Dấu hiệu hội chứng serotonin (nếu dùng với thuốc khác)",
            "INR nếu dùng với warfarin (tăng nguy cơ chảy máu)",
            "Dấu hiệu rút thuốc khi ngừng"
        ],
        "precautions": [
            "KHÔNG dùng với MAO inhibitor (chống chỉ định tuyệt đối)",
            "GIỚI HẠN LIỀU 40mg/ngày (nguy cơ QT kéo dài, rối loạn nhịp)",
            "Người già >60 tuổi: GIỚI HẠN 20mg/ngày (tăng nguy cơ QT kéo dài)",
            "Theo dõi ECG nếu dùng liều cao hoặc ở người già",
            "Tránh dùng với các thuốc kéo dài QT khác",
            "Theo dõi sát dấu hiệu tự tử trong vài tuần đầu",
            "Giảm liều dần khi ngừng (tránh hội chứng rút thuốc)",
            "Thận trọng khi dùng với warfarin (tăng nguy cơ chảy máu)",
            "Khởi đầu với liều thấp (20mg), tăng dần"
        ],
        "pharmacokinetics": {
            "half_life": "35 giờ (dài)",
            "onset": "2-4 tuần (tác dụng chống trầm cảm)",
            "duration": "Dài (do half-life dài)",
            "protein_binding": "80%",
            "clearance": "Gan (chuyển hóa qua CYP2C19, CYP3A4, CYP2D6), thận (thải trừ)"
        },
        "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm",
        "black_box_warnings": "Tăng nguy cơ tự tử ở trẻ em, thanh thiếu niên, và thanh niên <24 tuổi trong vài tháng đầu điều trị. QT kéo dài có thể xảy ra ở liều >40mg/ngày, đặc biệt ở người già - giới hạn liều 40mg/ngày (20mg ở người già). Chống chỉ định với MAO inhibitor",
        "drug_interactions": {
            "major": [
                {
                    "drug": "MAO inhibitors",
                    "mechanism": "Tăng nồng độ serotonin",
                    "effect": "Hội chứng serotonin nghiêm trọng",
                    "management": "CHỐNG CHỈ ĐỊNH TUYỆT ĐỐI. Ngừng citalopram ít nhất 2 tuần trước khi bắt đầu MAO inhibitor."
                },
                {
                    "drug": "QT prolonging drugs (amiodarone, sotalol, quetiapine)",
                    "mechanism": "Tăng nguy cơ QT prolongation",
                    "effect": "QT kéo dài, rối loạn nhịp tim (torsades de pointes)",
                    "management": "Tránh dùng cùng. Nếu bắt buộc, giới hạn liều citalopram 20mg/ngày và theo dõi ECG."
                }
            ],
            "moderate": [
                {
                    "drug": "Warfarin",
                    "mechanism": "Có thể tăng nồng độ warfarin",
                    "effect": "Tăng INR, tăng nguy cơ chảy máu",
                    "management": "Theo dõi INR thường xuyên. Điều chỉnh liều warfarin nếu cần."
                },
                {
                    "drug": "Triptans, Tramadol",
                    "mechanism": "Tăng nồng độ serotonin",
                    "effect": "Hội chứng serotonin",
                    "management": "Thận trọng. Dùng cách xa ít nhất 24 giờ."
                }
            ],
            "minor": []
        },
        "contraindications": {
            "tuyệt_đối": [
                "Dùng MAO inhibitor (chống chỉ định tuyệt đối)",
                "QT prolongation",
                "Dị ứng citalopram",
                "Liều >40mg/ngày (chống chỉ định do QT prolongation)"
            ],
            "tương_đối": [
                "Người già >60 tuổi - giới hạn 20mg/ngày",
                "Bệnh tim - tăng nguy cơ QT prolongation",
                "Rối loạn điện giải (hạ kali, hạ magne) - tăng nguy cơ QT prolongation",
                "Suy gan nặng - giảm liều",
                "Suy thận nặng (CrCl <30) - giảm liều",
                "Trẻ em <18 tuổi - tăng nguy cơ tự tử"
            ]
        },
        "pregnancy_lactation": {
            "fda_category": "C",
            "pregnancy_details": "Dùng được trong thai kỳ nếu lợi ích > nguy cơ. Một số nghiên cứu gợi ý tăng nguy cơ dị tật thai nhi (dị tật tim) khi dùng trong 3 tháng đầu, nhưng chứng cứ không rõ ràng. Có thể gây tăng huyết áp phổi ở trẻ sơ sinh (PPHN) - nguy cơ thấp. Có thể gây hội chứng cai ở trẻ sơ sinh nếu dùng gần ngày sinh. Theo dõi trẻ sơ sinh sau sinh.",
            "lactation": {
                "safety": "Compatible",
                "details": "Citalopram bài tiết vào sữa mẹ ở nồng độ thấp đến trung bình. Nồng độ trong máu trẻ bú mẹ thường <10% nồng độ mẹ. Có thể gây buồn ngủ, bú kém ở trẻ. Ít báo cáo về tác dụng phụ nghiêm trọng.",
                "recommendation": "Có thể dùng khi cho con bú với theo dõi chặt chẽ trẻ. Theo dõi dấu hiệu buồn ngủ, bú kém ở trẻ. Nếu trẻ có dấu hiệu bất thường, cân nhắc ngừng cho con bú hoặc chuyển sang SSRI khác (sertraline)."
            }
        },
        "hepatic_adjustment": {
            "mild": "Không đổi hoặc giảm liều nhẹ",
            "moderate": "Giảm liều 25-50%. Theo dõi chức năng gan",
            "severe": "Tránh dùng hoặc dùng liều rất thấp dưới sự giám sát chặt chẽ",
            "notes": "Citalopram chuyển hóa ở gan qua CYP2C19, CYP3A4, CYP2D6. Suy gan làm giảm chuyển hóa, tăng nguy cơ tích lũy. Tuy nhiên, ít gây độc gan trực tiếp."
        },
        "overdose_management": {
            "symptoms": [
                "Buồn nôn, nôn",
                "Kích động, lú lẫn",
                "QT prolongation, rối loạn nhịp tim (torsades de pointes)",
                "Nhịp tim nhanh",
                "Co giật",
                "Hôn mê",
                "Hội chứng serotonin (nếu dùng với thuốc khác)"
            ],
            "antidote": "Không có antidote đặc hiệu. Điều trị hỗ trợ",
            "treatment": [
                "Hỗ trợ hô hấp và tuần hoàn nếu cần",
                "Rửa dạ dày nếu uống trong vòng 1-2 giờ",
                "Than hoạt tính nếu uống trong vòng 1-2 giờ",
                "Theo dõi ECG liên tục - QT prolongation là nguy hiểm nhất",
                "Điều trị QT prolongation: Magnesium sulfate (2g IV), isoproterenol nếu cần",
                "Điều trị torsades de pointes: Magnesium sulfate, overdrive pacing",
                "Điều trị hội chứng serotonin: Cyproheptadine, benzodiazepines",
                "Điều trị co giật: Benzodiazepines",
                "Truyền dịch",
                "Theo dõi ít nhất 24-48 giờ"
            ],
            "monitoring": "ECG liên tục (QT interval), huyết áp, nhịp tim, ý thức, dấu hiệu co giật, điện giải"
        },
        "reversal_agents": {
            "available": False,
            "agents": []
        },
        "administration_instructions": {
            "oral": {
                "with_food": "Có thể dùng với hoặc không có thức ăn. Dùng với thức ăn có thể giảm buồn nôn",
                "timing": "Dùng 1 lần/ngày (buổi sáng hoặc tối). GIỚI HẠN 40mg/ngày (20mg ở người già >60 tuổi) do nguy cơ QT prolongation."
            },
            "iv": {
                "reconstitution": "Không có dạng IV",
                "infusion_rate": "N/A",
                "compatibility": [],
                "incompatibility": [],
                "notes": "Chỉ có dạng uống"
            }
        },
        "references": {
            "primary_sources": [
                "FDA Drug Label - Celexa (citalopram)",
                "UpToDate - Citalopram: Drug information",
                "American Psychiatric Association guidelines"
            ],
            "last_updated": "2024-12-19",
            "evidence_level": "High - Multiple RCTs and systematic reviews"
        }
    },

    "Escitalopram": {
        "group": "Psychiatry - SSRI",
        "vietnamese_name": "Escitalopram, Lexapro",
        "administration": ["PO"],
        "indications": [
            "Trầm cảm",
            "Rối loạn lo âu tổng quát (GAD)",
            "Rối loạn hoảng sợ"
        ],
        "contraindications": [
            "Dùng MAO inhibitor",
            "Dị ứng"
        ],
        "dosage": {
            "adult_standard": "10mg x 1 lần/ngày, tăng đến 10-20mg/ngày",
            "adult_max": "20mg/ngày",
            "notes": "Là S-enantiomer của citalopram, ít tác dụng phụ hơn"
        },
        "side_effects": [
            "Buồn nôn",
            "Mất ngủ",
            "Nhức đầu",
            "Giảm ham muốn tình dục",
            "Ít tác dụng phụ hơn citalopram"
        ],
        "interactions": [
            "MAO inhibitor: chống chỉ định",
            "Warfarin: có thể tăng tác dụng",
            "Tramadol: tăng nguy cơ co giật"
        ],
        "pregnancy": "C",
        "mechanism_of_action": "Escitalopram là S-enantiomer (chất hoạt động) của citalopram, SSRI ức chế tái hấp thu serotonin ở synap thần kinh. Tăng nồng độ serotonin dẫn đến tác dụng chống trầm cảm, chống lo âu. Là chất hoạt động chính của citalopram, nên hiệu quả tương đương với citalopram nhưng liều thấp hơn (10mg escitalopram ≈ 20mg citalopram). Ưu điểm: ít tác dụng phụ hơn citalopram, không có R-enantiomer (ít gây QT kéo dài hơn), dùng 1 lần/ngày",
        "monitoring": [
            "Tâm trạng và triệu chứng trầm cảm, lo âu (đánh giá định kỳ)",
            "Dấu hiệu tự tử (tăng nguy cơ trong vài tuần đầu, đặc biệt ở <24 tuổi)",
            "Dấu hiệu hội chứng serotonin (nếu dùng với thuốc khác)",
            "INR nếu dùng với warfarin (tăng nguy cơ chảy máu)",
            "Triệu chứng tiêu hóa: buồn nôn (phổ biến)",
            "Dấu hiệu rút thuốc khi ngừng"
        ],
        "precautions": [
            "KHÔNG dùng với MAO inhibitor (chống chỉ định tuyệt đối)",
            "Ngừng escitalopram ít nhất 2 tuần trước khi bắt đầu MAO inhibitor",
            "Theo dõi sát dấu hiệu tự tử trong vài tuần đầu (tăng nguy cơ ở <24 tuổi)",
            "Giảm liều dần khi ngừng (tránh hội chứng rút thuốc)",
            "Thận trọng khi dùng với tramadol, triptans (tăng nguy cơ hội chứng serotonin)",
            "Thận trọng khi dùng với warfarin (tăng nguy cơ chảy máu)",
            "Khởi đầu với liều thấp (10mg), tăng dần",
            "Ưu điểm: ít tác dụng phụ hơn citalopram, ít nguy cơ QT kéo dài hơn"
        ],
        "pharmacokinetics": {
            "half_life": "27-32 giờ (dài)",
            "onset": "2-4 tuần (tác dụng chống trầm cảm)",
            "duration": "Dài (do half-life dài)",
            "protein_binding": "56% (thấp hơn citalopram)",
            "clearance": "Gan (chuyển hóa qua CYP2C19, CYP3A4, CYP2D6), thận (thải trừ)"
        },
        "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm",
        "black_box_warnings": "Tăng nguy cơ tự tử ở trẻ em, thanh thiếu niên, và thanh niên <24 tuổi trong vài tháng đầu điều trị. Chống chỉ định với MAO inhibitor",
        "drug_interactions": {
            "major": [
                {
                    "drug": "MAO inhibitors",
                    "mechanism": "Tăng nồng độ serotonin",
                    "effect": "Hội chứng serotonin nghiêm trọng",
                    "management": "CHỐNG CHỈ ĐỊNH TUYỆT ĐỐI. Ngừng escitalopram ít nhất 2 tuần trước khi bắt đầu MAO inhibitor."
                }
            ],
            "moderate": [
                {
                    "drug": "Warfarin",
                    "mechanism": "Có thể tăng nồng độ warfarin",
                    "effect": "Tăng INR, tăng nguy cơ chảy máu",
                    "management": "Theo dõi INR thường xuyên. Điều chỉnh liều warfarin nếu cần."
                },
                {
                    "drug": "Tramadol, Triptans",
                    "mechanism": "Tăng nồng độ serotonin",
                    "effect": "Hội chứng serotonin",
                    "management": "Thận trọng. Dùng cách xa ít nhất 24 giờ."
                }
            ],
            "minor": []
        },
        "contraindications": {
            "tuyệt_đối": [
                "Dùng MAO inhibitor (chống chỉ định tuyệt đối)",
                "Dị ứng escitalopram"
            ],
            "tương_đối": [
                "Suy gan nặng - giảm liều",
                "Suy thận nặng (CrCl <30) - giảm liều",
                "Trẻ em <18 tuổi - tăng nguy cơ tự tử",
                "Dùng với tramadol, triptans - tăng nguy cơ hội chứng serotonin"
            ]
        },
        "pregnancy_lactation": {
            "fda_category": "C",
            "pregnancy_details": "Dùng được trong thai kỳ nếu lợi ích > nguy cơ. Một số nghiên cứu gợi ý tăng nguy cơ dị tật thai nhi (dị tật tim) khi dùng trong 3 tháng đầu, nhưng chứng cứ không rõ ràng. Có thể gây tăng huyết áp phổi ở trẻ sơ sinh (PPHN) - nguy cơ thấp. Có thể gây hội chứng cai ở trẻ sơ sinh nếu dùng gần ngày sinh. Theo dõi trẻ sơ sinh sau sinh.",
            "lactation": {
                "safety": "Compatible",
                "details": "Escitalopram bài tiết vào sữa mẹ ở nồng độ thấp. Nồng độ trong máu trẻ bú mẹ thường <5% nồng độ mẹ. An toàn cho trẻ bú mẹ. Ít báo cáo về tác dụng phụ ở trẻ.",
                "recommendation": "Có thể dùng khi cho con bú với theo dõi chặt chẽ trẻ. Theo dõi dấu hiệu buồn ngủ, bú kém ở trẻ."
            }
        },
        "hepatic_adjustment": {
            "mild": "Không đổi hoặc giảm liều nhẹ",
            "moderate": "Giảm liều 25-50%. Theo dõi chức năng gan",
            "severe": "Tránh dùng hoặc dùng liều rất thấp dưới sự giám sát chặt chẽ",
            "notes": "Escitalopram chuyển hóa ở gan qua CYP2C19, CYP3A4, CYP2D6. Suy gan làm giảm chuyển hóa, tăng nguy cơ tích lũy. Tuy nhiên, ít gây độc gan trực tiếp."
        },
        "overdose_management": {
            "symptoms": [
                "Buồn nôn, nôn",
                "Kích động, lú lẫn",
                "Nhịp tim nhanh",
                "Co giật",
                "Hôn mê",
                "Hội chứng serotonin (nếu dùng với thuốc khác)"
            ],
            "antidote": "Không có antidote đặc hiệu. Điều trị hỗ trợ",
            "treatment": [
                "Hỗ trợ hô hấp và tuần hoàn nếu cần",
                "Rửa dạ dày nếu uống trong vòng 1-2 giờ",
                "Than hoạt tính nếu uống trong vòng 1-2 giờ",
                "Theo dõi ECG, huyết áp, nhịp tim",
                "Điều trị hội chứng serotonin: Cyproheptadine, benzodiazepines",
                "Điều trị co giật: Benzodiazepines",
                "Truyền dịch",
                "Theo dõi ít nhất 24-48 giờ"
            ],
            "monitoring": "ECG, huyết áp, nhịp tim, ý thức, dấu hiệu co giật"
        },
        "reversal_agents": {
            "available": False,
            "agents": []
        },
        "administration_instructions": {
            "oral": {
                "with_food": "Có thể dùng với hoặc không có thức ăn. Dùng với thức ăn có thể giảm buồn nôn",
                "timing": "Dùng 1 lần/ngày (buổi sáng hoặc tối). Ưu điểm: ít tác dụng phụ hơn citalopram, ít nguy cơ QT kéo dài hơn."
            },
            "iv": {
                "reconstitution": "Không có dạng IV",
                "infusion_rate": "N/A",
                "compatibility": [],
                "incompatibility": [],
                "notes": "Chỉ có dạng uống"
            }
        },
        "references": {
            "primary_sources": [
                "FDA Drug Label - Lexapro (escitalopram)",
                "UpToDate - Escitalopram: Drug information",
                "American Psychiatric Association guidelines"
            ],
            "last_updated": "2024-12-19",
            "evidence_level": "High - Multiple RCTs and systematic reviews"
        }
    },

    "Paroxetine": {
        "group": "Psychiatry - SSRI (Selective Serotonin Reuptake Inhibitor)",
        "vietnamese_name": "Paroxetine, Paxil",
        "administration": ["PO"],
        "indications": [
            "Trầm cảm",
            "Rối loạn lo âu tổng quát (GAD)",
            "Rối loạn hoảng sợ",
            "Rối loạn ám ảnh cưỡng chế (OCD)",
            "Rối loạn stress sau sang chấn (PTSD)",
            "Rối loạn lo âu xã hội"
        ],
        "contraindications": [
            "Dùng MAO inhibitor",
            "Dị ứng"
        ],
        "dosage": {
            "adult_depression": "20mg x 1 lần/ngày, tăng đến 20-50mg/ngày",
            "adult_ocd": "20-60mg/ngày",
            "adult_max": "60mg/ngày",
            "notes": "Khởi đầu 20mg/ngày, tăng dần. Uống buổi sáng hoặc tối"
        },
        "side_effects": [
            "Buồn nôn",
            "Mất ngủ",
            "Buồn ngủ (phổ biến hơn các SSRI khác)",
            "Giảm ham muốn tình dục",
            "Nhức đầu",
            "Khó chịu khi ngừng (withdrawal - phổ biến hơn các SSRI khác)",
            "Tăng cân (phổ biến hơn các SSRI khác)"
        ],
        "interactions": [
            "MAO inhibitor: chống chỉ định",
            "Warfarin: có thể tăng tác dụng chống đông",
            "Tramadol: tăng nguy cơ co giật",
            "Triptans: tăng nguy cơ hội chứng serotonin",
            "CYP2D6 substrates: ức chế CYP2D6 mạnh, tăng nồng độ nhiều thuốc"
        ],
        "pregnancy": "D",
        "mechanism_of_action": "Paroxetine là SSRI ức chế tái hấp thu serotonin ở synap thần kinh, tăng nồng độ serotonin và dẫn đến tác dụng chống trầm cảm, chống lo âu. Có tính chọn lọc cao với serotonin. Paroxetine cũng ức chế CYP2D6 mạnh (mạnh hơn các SSRI khác), dẫn đến nhiều tương tác thuốc. Paroxetine có half-life ngắn (21 giờ), nhưng tác dụng kéo dài do gắn chặt với serotonin transporter. Tác dụng trên nhiều chỉ định: trầm cảm, lo âu, OCD, PTSD, hoảng sợ. Tác dụng phụ: buồn ngủ (phổ biến hơn các SSRI khác), tăng cân, khó chịu khi ngừng (withdrawal - phổ biến hơn do half-life ngắn). Phân loại D trong thai kỳ (nguy cơ dị tật bẩm sinh).",
        "monitoring": [
            "Tâm trạng và triệu chứng trầm cảm, lo âu (đánh giá định kỳ)",
            "Dấu hiệu tự tử (tăng nguy cơ trong vài tuần đầu, đặc biệt ở <24 tuổi)",
            "Dấu hiệu hội chứng serotonin (nếu dùng với thuốc khác)",
            "INR nếu dùng với warfarin (tăng nguy cơ chảy máu)",
            "Dấu hiệu rút thuốc khi ngừng (chóng mặt, buồn nôn, lo âu, mất ngủ) - phổ biến hơn các SSRI khác",
            "Cân nặng (tăng cân - phổ biến hơn các SSRI khác)"
        ],
        "precautions": [
            "KHÔNG dùng với MAO inhibitor (chống chỉ định tuyệt đối)",
            "Ngừng paroxetine ít nhất 2 tuần trước khi bắt đầu MAO inhibitor",
            "Theo dõi sát dấu hiệu tự tử trong vài tuần đầu (tăng nguy cơ ở <24 tuổi)",
            "Giảm liều dần dần khi ngừng (tránh hội chứng rút thuốc) - QUAN TRỌNG vì withdrawal phổ biến hơn các SSRI khác",
            "Buồn ngủ - phổ biến hơn các SSRI khác, có thể cần dùng buổi tối",
            "Tăng cân - phổ biến hơn các SSRI khác, theo dõi cân nặng",
            "Thận trọng khi dùng với tramadol, triptans (tăng nguy cơ hội chứng serotonin)",
            "Thận trọng khi dùng với warfarin (tăng nguy cơ chảy máu)",
            "Ức chế CYP2D6 mạnh - tăng nồng độ nhiều thuốc (codeine, metoprolol, tamoxifen, etc.)",
            "Khởi đầu với liều thấp (20mg), tăng dần",
            "Phân loại D trong thai kỳ - nguy cơ dị tật bẩm sinh, tránh dùng trong thai kỳ nếu có thể"
        ],
        "pharmacokinetics": {
            "half_life": "21 giờ (trung bình, ngắn hơn fluoxetine)",
            "onset": "2-4 tuần (tác dụng chống trầm cảm)",
            "duration": "Dài (do gắn chặt với serotonin transporter)",
            "protein_binding": "95% (rất cao)",
            "clearance": "Gan (chuyển hóa qua CYP2D6 - paroxetine ức chế CYP2D6 mạnh), thận (thải trừ)"
        },
        "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm",
        "black_box_warnings": "Tăng nguy cơ tự tử ở trẻ em, thanh thiếu niên, và thanh niên <24 tuổi trong vài tháng đầu điều trị. Chống chỉ định với MAO inhibitor. Phân loại D trong thai kỳ - nguy cơ dị tật bẩm sinh (tim, sứt môi/hà ếch).",
        "drug_interactions": {
            "major": [
                {
                    "drug": "MAO inhibitors",
                    "mechanism": "Tăng nồng độ serotonin",
                    "effect": "Hội chứng serotonin nghiêm trọng",
                    "management": "CHỐNG CHỈ ĐỊNH TUYỆT ĐỐI. Ngừng paroxetine ít nhất 2 tuần trước khi bắt đầu MAO inhibitor."
                },
                {
                    "drug": "Tramadol",
                    "mechanism": "Tăng nồng độ serotonin, tăng nguy cơ co giật",
                    "effect": "Hội chứng serotonin, tăng nguy cơ co giật",
                    "management": "Tránh dùng cùng. Nếu bắt buộc, giảm liều tramadol và theo dõi sát."
                },
                {
                    "drug": "CYP2D6 substrates (codeine, metoprolol, tamoxifen, etc.)",
                    "mechanism": "Paroxetine ức chế CYP2D6 mạnh, tăng nồng độ các thuốc chuyển hóa qua CYP2D6",
                    "effect": "Tăng nồng độ các thuốc, tăng tác dụng phụ",
                    "management": "Thận trọng. Điều chỉnh liều các thuốc chuyển hóa qua CYP2D6. Đặc biệt quan trọng với tamoxifen (giảm hiệu quả điều trị ung thư vú)."
                }
            ],
            "moderate": [
                {
                    "drug": "Warfarin",
                    "mechanism": "Có thể tăng nồng độ warfarin",
                    "effect": "Tăng INR, tăng nguy cơ chảy máu",
                    "management": "Theo dõi INR thường xuyên. Điều chỉnh liều warfarin nếu cần."
                },
                {
                    "drug": "Triptans",
                    "mechanism": "Tăng nồng độ serotonin",
                    "effect": "Hội chứng serotonin",
                    "management": "Thận trọng. Dùng cách xa ít nhất 24 giờ."
                }
            ],
            "minor": []
        },
        "contraindications": {
            "tuyệt_đối": [
                "Dùng MAO inhibitor (chống chỉ định tuyệt đối)",
                "Dị ứng paroxetine"
            ],
            "tương_đối": [
                "Mang thai (phân loại D - nguy cơ dị tật bẩm sinh) - tránh dùng nếu có thể",
                "Suy gan nặng - giảm liều",
                "Suy thận nặng (CrCl <30) - giảm liều",
                "Trẻ em <18 tuổi - tăng nguy cơ tự tử",
                "Dùng với tramadol, triptans - tăng nguy cơ hội chứng serotonin",
                "Dùng với CYP2D6 substrates - tăng nồng độ các thuốc"
            ]
        },
        "pregnancy_lactation": {
            "fda_category": "D",
            "pregnancy_details": "Paroxetine có nguy cơ dị tật bẩm sinh cao (dị tật tim, sứt môi/hà ếch) khi dùng trong 3 tháng đầu thai kỳ. Nguy cơ dị tật tim tăng 1.5-2 lần. Nguy cơ sứt môi/hà ếch tăng 2-3 lần. Phân loại D - chỉ dùng nếu lợi ích điều trị vượt trội nguy cơ. Nếu có thể, chuyển sang SSRI khác (sertraline, citalopram) trước khi mang thai. Nếu dùng trong thai kỳ, cần tư vấn di truyền, siêu âm chi tiết, và theo dõi chặt chẽ.",
            "lactation": {
                "safety": "Compatible with monitoring",
                "details": "Paroxetine bài tiết vào sữa mẹ ở nồng độ thấp đến trung bình. Nồng độ trong máu trẻ bú mẹ thường <5% nồng độ mẹ. Có thể gây buồn ngủ, bú kém ở trẻ. Ít báo cáo về tác dụng phụ nghiêm trọng.",
                "recommendation": "Có thể dùng khi cho con bú với theo dõi chặt chẽ trẻ. Theo dõi dấu hiệu buồn ngủ, bú kém ở trẻ. Nếu trẻ có dấu hiệu bất thường, cân nhắc ngừng cho con bú hoặc chuyển sang SSRI khác (sertraline)."
            }
        },
        "hepatic_adjustment": {
            "mild": "Không đổi hoặc giảm liều nhẹ",
            "moderate": "Giảm liều 25-50%. Theo dõi chức năng gan",
            "severe": "Tránh dùng hoặc dùng liều rất thấp dưới sự giám sát chặt chẽ",
            "notes": "Paroxetine chuyển hóa ở gan qua CYP2D6 (paroxetine cũng ức chế CYP2D6 mạnh). Suy gan làm giảm chuyển hóa, tăng nguy cơ tích lũy."
        },
        "overdose_management": {
            "symptoms": [
                "Buồn nôn, nôn",
                "Kích động, lú lẫn",
                "Nhịp tim nhanh",
                "Co giật",
                "Hôn mê",
                "Hội chứng serotonin (nếu dùng với thuốc khác)"
            ],
            "antidote": "Không có antidote đặc hiệu. Điều trị hỗ trợ",
            "treatment": [
                "Hỗ trợ hô hấp và tuần hoàn nếu cần",
                "Rửa dạ dày nếu uống trong vòng 1-2 giờ",
                "Than hoạt tính nếu uống trong vòng 1-2 giờ",
                "Theo dõi ECG, huyết áp, nhịp tim",
                "Điều trị hội chứng serotonin: Cyproheptadine, benzodiazepines",
                "Điều trị co giật: Benzodiazepines",
                "Truyền dịch",
                "Theo dõi ít nhất 24 giờ"
            ],
            "monitoring": "ECG, huyết áp, nhịp tim, ý thức, dấu hiệu co giật"
        },
        "reversal_agents": {
            "available": False,
            "agents": []
        },
        "administration_instructions": {
            "oral": {
                "with_food": "Có thể dùng với hoặc không có thức ăn. Dùng với thức ăn có thể giảm buồn nôn",
                "timing": "Dùng 1 lần/ngày (buổi sáng hoặc tối). Có thể dùng buổi tối nếu gây buồn ngủ. Giảm liều dần dần khi ngừng (tránh withdrawal)."
            },
            "iv": {
                "reconstitution": "Không có dạng IV",
                "infusion_rate": "N/A",
                "compatibility": [],
                "incompatibility": [],
                "notes": "Chỉ có dạng uống"
            }
        },
        "references": {
            "primary_sources": [
                "FDA Drug Label - Paxil (paroxetine)",
                "UpToDate - Paroxetine: Drug information",
                "American Psychiatric Association guidelines"
            ],
            "last_updated": "2024-12-19",
            "evidence_level": "High - Multiple RCTs and systematic reviews"
        }
    }
}

__all__ = ['SSRI_DRUGS']

