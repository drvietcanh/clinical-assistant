"""
Psychiatry Drugs (Other) - SSRIs, SNRIs, TCAs
"""

PSYCHIATRY_OTHER_DRUGS = {
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

    "Venlafaxine": {
        "group": "Psychiatry - SNRI (Serotonin-Norepinephrine Reuptake Inhibitor)",
        "vietnamese_name": "Venlafaxine, Effexor",
        "administration": ["PO"],
        "indications": [
            "Trầm cảm",
            "Rối loạn lo âu tổng quát (GAD)",
            "Rối loạn hoảng sợ",
            "Rối loạn lo âu xã hội"
        ],
        "contraindications": [
            "Dùng MAO inhibitor",
            "Tăng huyết áp không kiểm soát",
            "Dị ứng"
        ],
        "dosage": {
            "adult_standard": "37.5-75mg x 2 lần/ngày (immediate) hoặc 75-150mg x 1 lần/ngày (extended release)",
            "adult_max": "225mg/ngày (immediate) hoặc 225mg/ngày (extended release)",
            "notes": "Extended release: uống 1 lần/ngày, thuận tiện hơn"
        },
        "side_effects": [
            "Buồn nôn",
            "Tăng huyết áp (liều cao)",
            "Mất ngủ",
            "Chóng mặt",
            "Giảm ham muốn tình dục",
            "Tăng nhịp tim",
            "Khó chịu khi ngừng (withdrawal)"
        ],
        "interactions": [
            "MAO inhibitor: chống chỉ định",
            "Warfarin: có thể tăng tác dụng",
            "Tramadol: tăng nguy cơ co giật và hội chứng serotonin"
        ],
        "pregnancy": "C",
        "mechanism_of_action": "Venlafaxine là thuốc chống trầm cảm thuộc nhóm SNRI (serotonin-norepinephrine reuptake inhibitor), ức chế tái hấp thu serotonin và norepinephrine ở synap thần kinh. Ở liều thấp (<75mg/ngày), venlafaxine chủ yếu ức chế tái hấp thu serotonin (giống SSRI). Ở liều trung bình (75-225mg/ngày), venlafaxine ức chế cả serotonin và norepinephrine. Ở liều cao (>225mg/ngày), venlafaxine cũng có thể ức chế tái hấp thu dopamine nhẹ. Bằng cách ức chế tái hấp thu, venlafaxine làm tăng nồng độ serotonin và norepinephrine trong synap, dẫn đến tăng hoạt động của các chất dẫn truyền thần kinh này và cải thiện triệu chứng trầm cảm và lo âu. Venlafaxine có tác dụng mạnh hơn SSRI trong một số trường hợp, đặc biệt trầm cảm nặng và kháng trị. Tác dụng phụ chính: tăng huyết áp ở liều cao do ức chế norepinephrine. Venlafaxine có dạng extended release (ER) cho phép dùng 1 lần/ngày.",
        "monitoring": [
            "Đáp ứng điều trị (giảm triệu chứng trầm cảm, lo âu) - đánh giá sau 2-4 tuần",
            "Huyết áp - tăng huyết áp ở liều cao (>150mg/ngày), đặc biệt ở bệnh nhân có tăng huyết áp",
            "Nhịp tim - tăng nhịp tim có thể xảy ra",
            "Dấu hiệu hội chứng serotonin (sốt, kích động, run, nhịp tim nhanh, co giật) - đặc biệt khi dùng với tramadol, MAO inhibitor",
            "Dấu hiệu withdrawal (khó chịu, buồn nôn, chóng mặt, lo âu, mất ngủ) - khi ngừng đột ngột",
            "Tác dụng phụ (buồn nôn, mất ngủ, chóng mặt, giảm ham muốn tình dục)",
            "Tương tác với MAO inhibitor (chống chỉ định), warfarin (tăng INR), tramadol (tăng nguy cơ co giật và hội chứng serotonin)"
        ],
        "precautions": [
            "CHỐNG CHỈ ĐỊNH với MAO inhibitor - phải ngừng MAO inhibitor ít nhất 14 ngày trước khi bắt đầu venlafaxine (nguy cơ hội chứng serotonin nghiêm trọng)",
            "Không ngừng đột ngột - giảm liều dần dần trong ít nhất 2 tuần (nguy cơ withdrawal syndrome: khó chịu, buồn nôn, chóng mặt, lo âu, mất ngủ)",
            "Tăng huyết áp - nguy cơ tăng ở liều cao (>150mg/ngày), đặc biệt ở bệnh nhân có tăng huyết áp, cần theo dõi huyết áp",
            "Tăng nhịp tim - có thể xảy ra, thận trọng ở bệnh nhân có bệnh tim",
            "Nguy cơ hội chứng serotonin - đặc biệt khi dùng với tramadol, triptans, MAO inhibitor, SSRI",
            "Tăng nguy cơ tự sát - đặc biệt ở trẻ em, thanh thiếu niên, và người trẻ tuổi (<25 tuổi) trong vài tuần đầu",
            "Buồn nôn - tác dụng phụ phổ biến nhất, thường tự khỏi sau vài tuần, có thể giảm bằng cách uống với thức ăn",
            "Mất ngủ - có thể xảy ra, cân nhắc dùng vào buổi sáng",
            "Giảm ham muốn tình dục - tác dụng phụ phổ biến, có thể kéo dài",
            "Dạng extended release (ER) - uống 1 lần/ngày, thuận tiện hơn, ít tác dụng phụ hơn",
            "Dùng với thức ăn để giảm buồn nôn",
            "Thận trọng ở bệnh nhân có bệnh gan, suy thận (có thể cần giảm liều)"
        ],
        "pharmacokinetics": {
            "half_life": "5 giờ (venlafaxine), 11 giờ (desvenlafaxine - metabolite hoạt động)",
            "onset": "2-4 tuần (tác dụng chống trầm cảm)",
            "duration": "12-24 giờ (dùng 1-2 lần/ngày)",
            "protein_binding": "27-30%",
            "clearance": "Gan: chuyển hóa qua CYP2D6 thành desvenlafaxine (metabolite hoạt động, mạnh hơn venlafaxine). Thận: bài tiết một phần nguyên dạng và metabolites. Cần điều chỉnh liều ở suy thận và suy gan nặng."
        },
        "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm, tránh ánh sáng. Viên nén: bảo quản trong bao bì kín. Dạng extended release: bảo quản tương tự, không nghiền hoặc nhai (phải uống nguyên viên).",
        "black_box_warnings": "Nguy cơ tự sát và hành vi tự sát ở trẻ em, thanh thiếu niên, và người trẻ tuổi (<25 tuổi) với các thuốc chống trầm cảm. Nguy cơ tăng trong vài tháng đầu điều trị và khi tăng liều. Theo dõi chặt chẽ dấu hiệu tự sát, thay đổi hành vi, lo âu, kích động, mất ngủ, hoặc các triệu chứng mới hoặc nặng hơn. Nguy cơ hội chứng serotonin khi dùng với MAO inhibitor, tramadol, triptans.",
        "drug_interactions": {
            "major": [
                {
                    "drug": "MAO inhibitors (phenelzine, tranylcypromine, selegiline)",
                    "mechanism": "Ức chế chuyển hóa serotonin, tăng nồng độ serotonin",
                    "effect": "Nguy cơ hội chứng serotonin nghiêm trọng, có thể tử vong (sốt, kích động, run, nhịp tim nhanh, co giật, hôn mê)",
                    "management": "CHỐNG CHỈ ĐỊNH. Phải ngừng MAO inhibitor ít nhất 14 ngày trước khi bắt đầu venlafaxine. Phải ngừng venlafaxine ít nhất 7 ngày trước khi bắt đầu MAO inhibitor."
                },
                {
                    "drug": "Tramadol",
                    "mechanism": "Cả hai đều tăng serotonin, tăng nguy cơ hội chứng serotonin",
                    "effect": "Nguy cơ hội chứng serotonin và co giật",
                    "management": "Tránh dùng chung nếu có thể. Nếu phải dùng, theo dõi chặt chẽ dấu hiệu hội chứng serotonin. Giảm liều tramadol."
                },
                {
                    "drug": "Warfarin",
                    "mechanism": "Venlafaxine có thể ức chế CYP2C9 nhẹ, tăng nồng độ warfarin",
                    "effect": "Tăng INR, tăng nguy cơ chảy máu",
                    "management": "Theo dõi INR thường xuyên. Có thể cần giảm liều warfarin."
                }
            ],
            "moderate": [
                {
                    "drug": "Triptans (sumatriptan, rizatriptan)",
                    "mechanism": "Cả hai đều tăng serotonin",
                    "effect": "Tăng nguy cơ hội chứng serotonin",
                    "management": "Thận trọng, theo dõi dấu hiệu hội chứng serotonin. Có thể cần giảm liều triptan hoặc tăng khoảng cách giữa các liều."
                },
                {
                    "drug": "Lithium",
                    "mechanism": "Tăng serotonin",
                    "effect": "Tăng nguy cơ hội chứng serotonin",
                    "management": "Theo dõi dấu hiệu hội chứng serotonin. Có thể cần giảm liều lithium."
                },
                {
                    "drug": "Cimetidine",
                    "mechanism": "Ức chế CYP2D6, giảm chuyển hóa venlafaxine",
                    "effect": "Tăng nồng độ venlafaxine",
                    "management": "Giảm liều venlafaxine 25-50%. Theo dõi tác dụng phụ."
                }
            ],
            "minor": [
                {
                    "drug": "Metoclopramide",
                    "mechanism": "Cả hai đều tăng serotonin nhẹ",
                    "effect": "Tăng nhẹ nguy cơ hội chứng serotonin",
                    "management": "Theo dõi dấu hiệu hội chứng serotonin. Thường không cần điều chỉnh liều."
                }
            ]
        },
        "contraindications": {
            "tuyệt_đối": [
                "Dùng MAO inhibitor (trong vòng 14 ngày)",
                "Dị ứng venlafaxine hoặc các thành phần khác"
            ],
            "tương_đối": [
                "Tăng huyết áp không kiểm soát - nguy cơ tăng huyết áp ở liều cao",
                "Bệnh tim mạch (loạn nhịp, suy tim) - tăng nhịp tim, tăng huyết áp",
                "Suy gan nặng - giảm chuyển hóa, tăng nguy cơ tích lũy",
                "Suy thận nặng (CrCl <30) - giảm thải trừ, tăng nguy cơ tích lũy",
                "Mang thai (nguy cơ dị tật bẩm sinh, withdrawal ở trẻ sơ sinh) - chỉ dùng nếu lợi ích > nguy cơ",
                "Tiền sử co giật - tăng nguy cơ co giật",
                "Glaucoma góc hẹp - tăng nguy cơ tăng nhãn áp",
                "Bệnh nhân lớn tuổi - tăng nguy cơ tác dụng phụ"
            ]
        },
        "pregnancy_lactation": {
            "fda_category": "C",
            "pregnancy_details": "Chứng cứ về an toàn trong thai kỳ còn hạn chế. Một số nghiên cứu gợi ý tăng nhẹ nguy cơ dị tật bẩm sinh (tim, sứt môi/hà ếch), nhưng chứng cứ không rõ ràng. Trẻ sơ sinh có thể có withdrawal syndrome (khó chịu, run, khó thở, co giật) nếu mẹ dùng venlafaxine trong thai kỳ, đặc biệt gần cuối thai kỳ. Chỉ dùng nếu lợi ích điều trị vượt trội nguy cơ. Nếu dùng trong thai kỳ, cần tư vấn di truyền và theo dõi chặt chẽ. Theo dõi trẻ sơ sinh về dấu hiệu withdrawal.",
            "lactation": {
                "safety": "Compatible with monitoring",
                "details": "Venlafaxine và desvenlafaxine bài tiết vào sữa mẹ ở nồng độ thấp đến trung bình. Nồng độ trong máu trẻ sơ sinh rất thấp (<5% nồng độ trong máu mẹ). Tác dụng phụ ở trẻ rất hiếm nhưng có thể có buồn ngủ nhẹ, kích động nhẹ.",
                "recommendation": "Có thể cho con bú nhưng cần theo dõi trẻ về dấu hiệu tác dụng phụ (buồn ngủ, kích động, bú kém)."
            }
        },
        "hepatic_adjustment": {
            "mild": "Không cần điều chỉnh liều",
            "moderate": "Giảm liều 25-50%, theo dõi tác dụng phụ",
            "severe": "Giảm liều 50%, theo dõi tác dụng phụ chặt chẽ. Hoặc tránh dùng nếu có thể.",
            "notes": "Venlafaxine chuyển hóa ở gan qua CYP2D6 thành desvenlafaxine. Suy gan làm giảm chuyển hóa, tăng nguy cơ tích lũy venlafaxine và tác dụng phụ."
        },
        "overdose_management": {
            "symptoms": [
                "Triệu chứng thần kinh: buồn ngủ, chóng mặt, lú lẫn, co giật, hôn mê",
                "Hội chứng serotonin: sốt, kích động, run, nhịp tim nhanh, tăng huyết áp, co giật",
                "Rối loạn tim mạch: nhịp nhanh, tăng huyết áp, rối loạn nhịp, QT kéo dài",
                "Rối loạn hô hấp: suy hô hấp",
                "Rối loạn tiêu hóa: buồn nôn, nôn",
                "Triệu chứng khác: giãn đồng tử, sốt"
            ],
            "antidote": "Không có antidote đặc hiệu. Cyproheptadine có thể được dùng để điều trị hội chứng serotonin (không được FDA chấp thuận).",
            "treatment": [
                "Đánh giá đường thở, hô hấp, tuần hoàn. Hỗ trợ hô hấp nếu cần",
                "Rửa dạ dày nếu trong vòng 1-2 giờ sau uống (nếu bệnh nhân tỉnh táo)",
                "Than hoạt tính: 1g/kg (tối đa 50-100g) nếu trong vòng 1-2 giờ",
                "Theo dõi liên tục: ý thức, hô hấp, tim mạch, điện tâm đồ (QT kéo dài)",
                "Xử trí hội chứng serotonin: cyproheptadine (antagonist serotonin), hạ nhiệt, benzodiazepine cho kích động, co giật",
                "Xử trí co giật: benzodiazepine (diazepam, lorazepam)",
                "Xử trí tăng huyết áp: labetalol, esmolol (beta-blocker)",
                "Hỗ trợ hô hấp: thở máy nếu suy hô hấp",
                "Theo dõi điện tâm đồ: QT kéo dài, rối loạn nhịp"
            ],
            "monitoring": "Theo dõi ý thức, hô hấp, tim mạch, điện tâm đồ (QT, nhịp tim), dấu hiệu hội chứng serotonin, nhiệt độ cơ thể"
        },
        "reversal_agents": None,
        "administration_instructions": {
            "oral": {
                "with_food": "Uống với thức ăn để giảm buồn nôn (tác dụng phụ phổ biến nhất)",
                "timing": "Dạng immediate release: chia 2-3 lần/ngày. Dạng extended release (ER): uống 1 lần/ngày vào buổi sáng hoặc tối. Uống cùng thời điểm mỗi ngày. KHÔNG nghiền hoặc nhai viên ER (phải uống nguyên viên). Không ngừng đột ngột - giảm liều dần dần trong ít nhất 2 tuần."
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
                "Lexicomp - Venlafaxine",
                "UpToDate - Venlafaxine: Drug information",
                "FDA - Effexor (venlafaxine) prescribing information",
                "Goodman & Gilman's The Pharmacological Basis of Therapeutics, 13th ed."
            ],
            "last_updated": "2024-12-19",
            "evidence_level": "A - Evidence from well-designed randomized controlled trials and systematic reviews"
        }
    },

    "Amitriptyline": {
        "group": "Psychiatry - Tricyclic Antidepressant (TCA)",
        "vietnamese_name": "Amitriptyline, Elavil",
        "administration": ["PO"],
        "indications": [
            "Trầm cảm",
            "Đau thần kinh (neuropathic pain)",
            "Migraine phòng ngừa",
            "Rối loạn giấc ngủ",
            "Đau cơ xơ hóa"
        ],
        "contraindications": [
            "Dùng MAO inhibitor",
            "Nhồi máu cơ tim gần đây",
            "Block nhĩ thất độ 2-3",
            "Rối loạn nhịp tim",
            "Suy tim nặng"
        ],
        "dosage": {
            "adult_depression": "25-75mg x 1 lần/ngày buổi tối, tăng đến 50-150mg/ngày",
            "adult_neuropathic": "10-25mg buổi tối, tăng đến 25-100mg/ngày",
            "adult_max": "150-300mg/ngày",
            "notes": "Dùng buổi tối để tránh buồn ngủ ban ngày. Nguy cơ quá liều cao"
        },
        "side_effects": [
            "Buồn ngủ (phổ biến)",
            "Khô miệng",
            "Táo bón",
            "Rối loạn nhịp tim",
            "Hạ huyết áp tư thế",
            "Nhìn mờ",
            "Tăng cân",
            "Nguy cơ quá liều (cardiotoxic)"
        ],
        "interactions": [
            "MAO inhibitor: chống chỉ định (nguy hiểm)",
            "Quinidine: tăng nồng độ amitriptyline",
            "Cimetidine: tăng nồng độ",
            "Alcohol: tăng tác dụng an thần",
            "Sympathomimetics: tăng nguy cơ tăng huyết áp"
        ],
        "pregnancy": "C - D trong 3 tháng đầu",
        "mechanism_of_action": "Amitriptyline là tricyclic antidepressant (TCA) ức chế tái hấp thu norepinephrine và serotonin ở synap thần kinh, tăng nồng độ các chất dẫn truyền thần kinh này. Cũng có tác dụng chẹn muscarinic (kháng cholinergic), histamine H1 (an thần), và alpha-1 adrenergic (hạ huyết áp). Tác dụng chống trầm cảm, giảm đau thần kinh (cơ chế chưa rõ hoàn toàn), phòng ngừa migraine. Có tác dụng an thần mạnh do chẹn histamine H1",
        "monitoring": [
            "ECG trước khi bắt đầu và định kỳ (đặc biệt ở bệnh nhân có bệnh tim, cao tuổi) - QT kéo dài, block nhĩ thất",
            "Nhịp tim, huyết áp (hạ huyết áp tư thế, rối loạn nhịp)",
            "Dấu hiệu quá liều: nhịp tim nhanh, loạn nhịp, co giật, hôn mê (cấp cứu)",
            "Triệu chứng kháng cholinergic: khô miệng, táo bón, nhìn mờ, bí tiểu",
            "Tâm trạng và triệu chứng trầm cảm",
            "Chức năng gan nếu có triệu chứng (hiếm)"
        ],
        "precautions": [
            "NGUY CƠ QUÁ LIỀU CAO - cardiotoxic (rối loạn nhịp, block nhĩ thất), có thể tử vong",
            "Chỉ kê đơn số lượng ít, theo dõi sát bệnh nhân có ý định tự tử",
            "Không dùng với MAO inhibitor (chống chỉ định tuyệt đối - nguy cơ cao huyết áp, sốt, co giật, tử vong)",
            "Thận trọng ở bệnh nhân có bệnh tim, block nhĩ thất (chống chỉ định block độ 2-3)",
            "Dùng buổi tối để tránh buồn ngủ ban ngày (tác dụng an thần mạnh)",
            "Khởi đầu với liều thấp (10-25mg), tăng dần",
            "Giảm liều dần khi ngừng (tránh hội chứng cai)",
            "Tránh rượu (tăng tác dụng an thần, nguy cơ quá liều)",
            "Thận trọng khi lái xe hoặc vận hành máy móc (buồn ngủ, nhìn mờ)",
            "Theo dõi sát bệnh nhân có ý định tự tử (tăng nguy cơ trong vài tuần đầu)"
        ],
        "pharmacokinetics": {
            "half_life": "10-28 giờ (dài)",
            "onset": "2-4 tuần (tác dụng chống trầm cảm), nhanh hơn (giảm đau, an thần)",
            "duration": "Dài (do half-life dài)",
            "protein_binding": "82-96% (cao)",
            "clearance": "Gan (chuyển hóa qua CYP2D6, CYP2C19, CYP1A2), thận (thải trừ)"
        },
        "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm, tránh ánh sáng",
        "black_box_warnings": "Tăng nguy cơ tự tử ở trẻ em, thanh thiếu niên, và thanh niên <24 tuổi trong vài tháng đầu điều trị. Quá liều có thể gây rối loạn nhịp tim nghiêm trọng, block nhĩ thất, co giật, hôn mê, tử vong. Chống chỉ định với MAO inhibitor",
        "drug_interactions": {
            "major": [
                {
                    "drug": "MAO inhibitors (phenelzine, tranylcypromine, selegiline)",
                    "mechanism": "Ức chế chuyển hóa catecholamines, tăng nồng độ serotonin và norepinephrine",
                    "effect": "Hội chứng serotonin, tăng huyết áp nghiêm trọng, sốt cao, co giật, tử vong",
                    "management": "CHỐNG CHỈ ĐỊNH TUYỆT ĐỐI. Ngừng MAO inhibitor ít nhất 14 ngày trước khi bắt đầu amitriptyline."
                },
                {
                    "drug": "Quinidine, Cimetidine",
                    "mechanism": "Ức chế CYP2D6, giảm chuyển hóa amitriptyline",
                    "effect": "Tăng nồng độ amitriptyline, tăng nguy cơ độc tính (rối loạn nhịp, block nhĩ thất)",
                    "management": "Giảm liều amitriptyline 50%. Theo dõi ECG. Thận trọng."
                },
                {
                    "drug": "Sympathomimetics (epinephrine, norepinephrine)",
                    "mechanism": "Tăng tác dụng alpha-adrenergic",
                    "effect": "Tăng huyết áp nghiêm trọng, rối loạn nhịp tim",
                    "management": "Tránh dùng. Nếu cần, dùng liều thấp và theo dõi huyết áp chặt chẽ."
                }
            ],
            "moderate": [
                {
                    "drug": "Alcohol",
                    "mechanism": "Tăng tác dụng ức chế hệ thần kinh trung ương",
                    "effect": "Tăng an thần, suy hô hấp, nguy cơ quá liều",
                    "management": "Tránh rượu. Cảnh báo bệnh nhân về nguy cơ."
                },
                {
                    "drug": "Warfarin",
                    "mechanism": "Có thể ức chế chuyển hóa warfarin",
                    "effect": "Tăng INR, tăng nguy cơ chảy máu",
                    "management": "Theo dõi INR thường xuyên. Điều chỉnh liều warfarin nếu cần."
                },
                {
                    "drug": "Anticholinergics (atropine, benztropine)",
                    "mechanism": "Tăng tác dụng kháng cholinergic",
                    "effect": "Tăng khô miệng, táo bón, bí tiểu, nhìn mờ, lú lẫn",
                    "management": "Thận trọng. Giảm liều hoặc tránh dùng cùng."
                }
            ],
            "minor": [
                {
                    "drug": "Phenytoin, Carbamazepine",
                    "mechanism": "Cảm ứng enzyme chuyển hóa",
                    "effect": "Giảm nồng độ amitriptyline",
                    "management": "Tăng liều amitriptyline nếu cần"
                }
            ]
        },
        "contraindications": {
            "tuyệt_đối": [
                "Dùng MAO inhibitor (chống chỉ định tuyệt đối)",
                "Nhồi máu cơ tim gần đây (<6 tháng)",
                "Block nhĩ thất độ 2-3",
                "Rối loạn nhịp tim nặng",
                "Suy tim nặng (NYHA class IV)",
                "Dị ứng amitriptyline hoặc TCA"
            ],
            "tương_đối": [
                "Bệnh tim (thiếu máu cơ tim, suy tim nhẹ-trung bình) - thận trọng, theo dõi ECG",
                "Block nhĩ thất độ 1 - thận trọng",
                "Tăng nhãn áp (glaucoma) - tăng nguy cơ",
                "Bí tiểu - tăng nguy cơ",
                "Suy gan nặng - giảm liều",
                "Suy thận nặng (CrCl <30) - giảm liều",
                "Trẻ em <18 tuổi - tăng nguy cơ tự tử",
                "Có ý định tự tử - chỉ kê đơn số lượng ít"
            ]
        },
        "pregnancy_lactation": {
            "fda_category": "C",
            "pregnancy_details": "Dùng được trong thai kỳ nếu lợi ích > nguy cơ. Có nguy cơ dị tật thai nhi (dị tật tim, dị tật chi) khi dùng trong 3 tháng đầu, đặc biệt liều cao. Có thể gây hội chứng cai ở trẻ sơ sinh (kích động, khó thở, run, co giật) nếu dùng gần ngày sinh. Theo dõi trẻ sơ sinh sau sinh. Nguy cơ rối loạn phát triển thần kinh thấp.",
            "lactation": {
                "safety": "Compatible with caution",
                "details": "Amitriptyline bài tiết vào sữa mẹ ở nồng độ thấp (<5% liều mẹ). Nồng độ trong máu trẻ bú mẹ thường rất thấp. Có thể gây buồn ngủ, bú kém ở trẻ. Ít báo cáo về tác dụng phụ nghiêm trọng.",
                "recommendation": "Có thể dùng khi cho con bú với theo dõi chặt chẽ trẻ. Theo dõi dấu hiệu buồn ngủ, bú kém, táo bón ở trẻ. Nếu trẻ có dấu hiệu bất thường, cân nhắc ngừng cho con bú hoặc giảm liều."
            }
        },
        "hepatic_adjustment": {
            "mild": "Không đổi hoặc giảm liều nhẹ",
            "moderate": "Giảm liều 25-50%. Theo dõi chức năng gan",
            "severe": "Tránh dùng hoặc dùng liều rất thấp dưới sự giám sát chặt chẽ",
            "notes": "Amitriptyline chuyển hóa ở gan qua CYP2D6, CYP2C19, CYP1A2. Suy gan làm giảm chuyển hóa, tăng nguy cơ tích lũy và độc tính. Tuy nhiên, ít gây độc gan trực tiếp."
        },
        "overdose_management": {
            "symptoms": [
                "Giai đoạn sớm: Buồn ngủ, lú lẫn, chóng mặt, nhìn mờ",
                "Giai đoạn nặng: Rối loạn nhịp tim (nhịp nhanh, rung nhĩ, block nhĩ thất), hạ huyết áp hoặc tăng huyết áp",
                "Co giật, hôn mê",
                "Suy hô hấp",
                "Triệu chứng kháng cholinergic: khô miệng, bí tiểu, nhịp tim nhanh, sốt",
                "Tử vong do rối loạn nhịp tim hoặc suy hô hấp"
            ],
            "antidote": "Không có antidote đặc hiệu. Có thể dùng sodium bicarbonate cho rối loạn nhịp",
            "treatment": [
                "Hỗ trợ hô hấp và tuần hoàn ngay lập tức (quan trọng nhất)",
                "Rửa dạ dày nếu uống trong vòng 1-2 giờ (thận trọng nếu đã hôn mê)",
                "Than hoạt tính nếu uống trong vòng 1-2 giờ",
                "Theo dõi ECG liên tục - rối loạn nhịp là nguy hiểm nhất",
                "Điều trị rối loạn nhịp: Sodium bicarbonate (1-2 mEq/kg IV bolus) để điều chỉnh QT kéo dài và block nhĩ thất",
                "Điều trị co giật: Benzodiazepines (lorazepam, diazepam)",
                "Điều trị hạ huyết áp: Truyền dịch, vận mạch nếu cần",
                "Theo dõi điện giải, đường huyết",
                "Lọc máu (hemodialysis) KHÔNG hiệu quả do protein binding cao",
                "Theo dõi ít nhất 24-48 giờ (do half-life dài)"
            ],
            "monitoring": "ECG liên tục (rối loạn nhịp), huyết áp, nhịp tim, ý thức, hô hấp, điện giải, đường huyết, nhiệt độ"
        },
        "reversal_agents": {
            "available": False,
            "agents": []
        },
        "administration_instructions": {
            "oral": {
                "with_food": "Có thể dùng với hoặc không có thức ăn. Dùng với thức ăn có thể giảm kích ứng dạ dày",
                "timing": "Dùng buổi tối (1 lần/ngày) để tránh buồn ngủ ban ngày. Có thể chia 2-3 lần nếu liều cao hoặc tác dụng phụ nhiều"
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
                "FDA Drug Label - Elavil (amitriptyline)",
                "UpToDate - Amitriptyline: Drug information",
                "Goodman & Gilman's The Pharmacological Basis of Therapeutics",
                "American Psychiatric Association guidelines"
            ],
            "last_updated": "2024-12-19",
            "evidence_level": "High - Multiple RCTs and systematic reviews"
        }
    },

}

__all__ = ['PSYCHIATRY_OTHER_DRUGS']
