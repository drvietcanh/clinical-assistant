"""
Cardiovascular Drugs
Active module - contains all cardiovascular drug data
"""

CARDIOVASCULAR_DRUGS = {
# ACE Inhibitors
    "Captopril": {
        "group": "Cardiovascular - ACE Inhibitor",
        "vietnamese_name": "Captopril, Capoten",
        "administration": ["PO"],
        "indications": [
            "Tăng huyết áp",
            "Suy tim",
            "Bảo vệ thận trong đái tháo đường",
            "Sau nhồi máu cơ tim"
        ],
        "contraindications": [
            "Dị ứng ACE inhibitor",
            "Có thai",
            "Hẹp động mạch thận 2 bên",
            "Phù mạch trước đây với ACE inhibitor"
        ],
        "dosage": {
            "adult_htn": "12.5-50mg x 2-3 lần/ngày",
            "adult_heart_failure": "6.25mg x 3 lần/ngày, tăng dần đến 50mg x 3 lần/ngày",
            "adult_post_mi": "6.25mg x 3 lần/ngày, tăng đến 50mg x 3 lần/ngày",
            "notes": "Khởi đầu với liều thấp, tăng dần. Uống 1 giờ trước bữa ăn"
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "Giảm liều 25%",
            "under_30": "Không dùng nếu CrCl <10"
        },
        "side_effects": [
            "Ho khan (phổ biến)",
            "Tăng kali máu",
            "Hạ huyết áp",
            "Phù mạch (hiếm nhưng nguy hiểm)",
            "Suy thận cấp (hẹp ĐM thận)"
        ],
        "interactions": [
            "Kali bổ sung: tăng nguy cơ tăng kali máu",
            "Spironolactone: tăng kali máu",
            "NSAID: giảm hiệu quả, tăng nguy cơ suy thận",
            "Lithium: tăng nồng độ lithium"
        ],
        "pregnancy": "D - Chống chỉ định trong thai kỳ",
        "mechanism_of_action": "Ức chế angiotensin converting enzyme (ACE), giảm chuyển angiotensin I thành angiotensin II, giảm aldosterone, gây giãn mạch và giảm huyết áp",
        "monitoring": [
            "Creatinine, BUN sau 1-2 tuần khi bắt đầu",
            "Kali máu định kỳ",
            "Huyết áp",
            "Ho khan (tác dụng phụ thường gặp)",
            "Dấu hiệu phù mạch (sưng mặt, lưỡi, họng - cấp cứu)"
        ],
        "precautions": [
            "Khởi đầu với liều thấp, tăng dần",
            "Uống 1 giờ trước bữa ăn (giảm hấp thu nếu dùng với thức ăn)",
            "Theo dõi sát creatinine khi bắt đầu (có thể tăng nhẹ)",
            "Tránh dùng với NSAID (giảm hiệu quả, tăng nguy cơ suy thận)",
            "Ngừng ngay nếu có phù mạch (có thể nguy hiểm tính mạng)",
            "Ho khan có thể kéo dài, thường tự hết khi ngừng thuốc"
        ],
        "pharmacokinetics": {
            "half_life": "2 giờ (ngắn)",
            "onset": "15-30 phút",
            "duration": "6-12 giờ",
            "protein_binding": "25-30%",
            "clearance": "Thận (50-75%)"
        },
        "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm, tránh ánh sáng",
        "black_box_warnings": "Chống chỉ định trong thai kỳ - có thể gây dị tật thai nhi và tử vong thai nhi. Phù mạch có thể đe dọa tính mạng",
        "drug_interactions": {
            "major": [
                {
                    "drug": "Kali bổ sung, Kali-sparing diuretics (spironolactone, eplerenone, amiloride, triamterene)",
                    "mechanism": "Tác dụng hiệp đồng tăng kali máu",
                    "effect": "Tăng kali máu nghiêm trọng, có thể gây rối loạn nhịp tim",
                    "management": "Thận trọng. Theo dõi kali máu thường xuyên. Tránh dùng cùng nếu có thể."
                },
                {
                    "drug": "NSAIDs (ibuprofen, naproxen, diclofenac)",
                    "mechanism": "Giảm tác dụng giãn mạch, giảm lưu lượng máu thận",
                    "effect": "Giảm hiệu quả hạ huyết áp, tăng nguy cơ suy thận cấp",
                    "management": "Thận trọng. Theo dõi chức năng thận, huyết áp. Tránh dùng lâu dài cùng."
                }
            ],
            "moderate": [
                {
                    "drug": "Lithium",
                    "mechanism": "ACE inhibitor giảm thải trừ lithium qua thận",
                    "effect": "Tăng nồng độ lithium, tăng nguy cơ độc tính",
                    "management": "Theo dõi nồng độ lithium. Giảm liều lithium nếu cần."
                },
                {
                    "drug": "Diuretics (furosemide, hydrochlorothiazide)",
                    "mechanism": "Tác dụng hiệp đồng hạ huyết áp",
                    "effect": "Tăng nguy cơ hạ huyết áp quá mức",
                    "management": "Thận trọng khi bắt đầu. Có thể cần giảm liều diuretic."
                }
            ],
            "minor": [
                {
                    "drug": "Allopurinol",
                    "mechanism": "Tăng nguy cơ phản ứng dị ứng",
                    "effect": "Tăng nguy cơ hội chứng Stevens-Johnson",
                    "management": "Thận trọng. Theo dõi dấu hiệu dị ứng."
                }
            ]
        },
        "contraindications": {
            "absolute": [
                "Dị ứng ACE inhibitor",
                "Có thai",
                "Hẹp động mạch thận 2 bên",
                "Phù mạch trước đây với ACE inhibitor"
            ],
            "relative": [
                "Suy thận nặng (CrCl <10) - không dùng",
                "Suy thận trung bình (CrCl 10-30) - giảm liều, theo dõi sát",
                "Tăng kali máu - điều chỉnh trước khi dùng",
                "Hẹp động mạch thận 1 bên - thận trọng",
                "Dùng kali-sparing diuretics - tăng nguy cơ tăng kali máu",
                "Dùng NSAID - tăng nguy cơ suy thận"
            ]
        },
        "pregnancy_lactation": {
            "fda_category": "D",
            "pregnancy_details": "CHỐNG CHỈ ĐỊNH TUYỆT ĐỐI trong thai kỳ. Có thể gây dị tật thai nhi (dị tật thận, xương sọ, phổi), thiểu ối, chậm phát triển thai nhi, và tử vong thai nhi. Nguy cơ cao nhất trong 3 tháng đầu và 3 tháng cuối. Ngừng ngay khi phát hiện có thai.",
            "lactation": {
                "safety": "Compatible",
                "details": "Captopril bài tiết vào sữa mẹ ở nồng độ thấp. Nồng độ trong máu trẻ bú mẹ thường rất thấp. Không có báo cáo về tác dụng phụ nghiêm trọng ở trẻ bú mẹ.",
                "recommendation": "Có thể dùng khi cho con bú. Theo dõi trẻ nếu có dấu hiệu bất thường."
            }
        },
        "hepatic_adjustment": {
            "mild": "Không đổi",
            "moderate": "Không đổi",
            "severe": "Không đổi (chủ yếu thải qua thận)",
            "notes": "Captopril chủ yếu thải qua thận (50-75%). Không cần điều chỉnh liều ở suy gan."
        },
        "overdose_management": {
            "symptoms": [
                "Hạ huyết áp nghiêm trọng",
                "Nhịp tim chậm",
                "Suy thận cấp",
                "Tăng kali máu",
                "Ho khan",
                "Phù mạch"
            ],
            "antidote": "Không có antidote đặc hiệu. Điều trị hỗ trợ",
            "treatment": [
                "Điều trị hạ huyết áp: Truyền dịch (normal saline), nâng chân, nếu cần: dopamine, norepinephrine",
                "Rửa dạ dày nếu uống trong vòng 1-2 giờ",
                "Than hoạt tính",
                "Theo dõi huyết áp, nhịp tim, chức năng thận, điện giải",
                "Điều trị tăng kali máu nếu có: Calcium gluconate, insulin + glucose, sodium bicarbonate",
                "Nếu có phù mạch: Epinephrine, corticosteroids, antihistamines",
                "Hỗ trợ hô hấp và tuần hoàn nếu cần",
                "Theo dõi ít nhất 6-12 giờ (do half-life ngắn)"
            ],
            "monitoring": "Huyết áp, nhịp tim, chức năng thận (creatinine, BUN), điện giải (kali), dấu hiệu phù mạch, ý thức"
        },
        "reversal_agents": {
            "available": False,
            "agents": []
        },
        "administration_instructions": {
            "oral": {
                "with_food": "Uống 1 giờ trước bữa ăn để tăng hấp thu. Dùng với thức ăn có thể giảm hấp thu 30-40%.",
                "timing": "Uống 2-3 lần/ngày (do half-life ngắn). Khởi đầu với liều thấp (6.25-12.5mg), tăng dần. Uống đúng giờ mỗi ngày."
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
                "FDA Drug Label - Capoten (captopril)",
                "UpToDate - Captopril: Drug information",
                "SOLVD Study - New England Journal of Medicine",
                "SAVE Study - New England Journal of Medicine",
                "American Heart Association/American College of Cardiology guidelines"
            ],
            "last_updated": "2024-12-19",
            "evidence_level": "High - Multiple large RCTs (SOLVD, SAVE) and extensive clinical experience"
        }
    },
    "Enalapril": {
        "group": "Cardiovascular - ACE Inhibitor",
        "vietnamese_name": "Enalapril, Renitec",
        "administration": ["PO"],
        "indications": [
            "Tăng huyết áp",
            "Suy tim",
            "Bảo vệ thận trong đái tháo đường"
        ],
        "contraindications": [
            "Dị ứng ACE inhibitor",
            "Có thai",
            "Hẹp động mạch thận 2 bên"
        ],
        "dosage": {
            "adult_htn": "5-40mg x 1-2 lần/ngày",
            "adult_heart_failure": "2.5mg x 2 lần/ngày, tăng dần đến 10-20mg x 2 lần/ngày",
            "notes": "Khởi đầu với liều thấp, tăng dần"
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "Liều khởi đầu 2.5mg/ngày",
            "under_30": "Liều khởi đầu 2.5mg/ngày, theo dõi sát"
        },
        "side_effects": [
            "Ho khan",
            "Tăng kali máu",
            "Hạ huyết áp",
            "Phù mạch"
        ],
        "interactions": [
            "Kali: tăng kali máu",
            "Diuretics: tăng nguy cơ hạ huyết áp",
            "NSAID: giảm hiệu quả"
        ],
        "pregnancy": "D",
        "mechanism_of_action": "Enalapril là prodrug, chuyển hóa thành enalaprilat (hoạt chất) trong gan. Ức chế angiotensin converting enzyme (ACE), giảm chuyển angiotensin I thành angiotensin II, giảm aldosterone, gây giãn mạch và giảm huyết áp",
        "monitoring": [
            "Creatinine, BUN sau 1-2 tuần khi bắt đầu",
            "Kali máu định kỳ",
            "Huyết áp",
            "Ho khan (tác dụng phụ thường gặp)",
            "Dấu hiệu phù mạch (sưng mặt, lưỡi, họng - cấp cứu)"
        ],
        "precautions": [
            "Khởi đầu với liều thấp (2.5-5mg), tăng dần",
            "Có thể dùng 1-2 lần/ngày (khác với captopril 2-3 lần/ngày)",
            "Theo dõi sát creatinine khi bắt đầu (có thể tăng nhẹ)",
            "Tránh dùng với NSAID (giảm hiệu quả, tăng nguy cơ suy thận)",
            "Ngừng ngay nếu có phù mạch (có thể nguy hiểm tính mạng)",
            "Ít tác dụng phụ hơn captopril, nhưng vẫn có thể gây ho khan"
        ],
        "pharmacokinetics": {
            "half_life": "Enalapril: 11 giờ; Enalaprilat: 30-35 giờ (dài)",
            "onset": "1 giờ (PO), 15 phút (enalaprilat IV)",
            "duration": "12-24 giờ",
            "protein_binding": "50-60%",
            "clearance": "Thận (60%), một phần qua gan"
        },
        "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm, tránh ánh sáng",
        "black_box_warnings": "Chống chỉ định trong thai kỳ - có thể gây dị tật thai nhi và tử vong thai nhi. Phù mạch có thể đe dọa tính mạng",
        "drug_interactions": {
            "major": [
                {
                    "drug": "Kali bổ sung, Kali-sparing diuretics (spironolactone, eplerenone, amiloride, triamterene)",
                    "mechanism": "Tác dụng hiệp đồng tăng kali máu",
                    "effect": "Tăng kali máu nghiêm trọng, có thể gây rối loạn nhịp tim",
                    "management": "Thận trọng. Theo dõi kali máu thường xuyên. Tránh dùng cùng nếu có thể."
                },
                {
                    "drug": "NSAIDs (ibuprofen, naproxen, diclofenac)",
                    "mechanism": "Giảm tác dụng giãn mạch, giảm lưu lượng máu thận",
                    "effect": "Giảm hiệu quả hạ huyết áp, tăng nguy cơ suy thận cấp",
                    "management": "Thận trọng. Theo dõi chức năng thận, huyết áp. Tránh dùng lâu dài cùng."
                }
            ],
            "moderate": [
                {
                    "drug": "Lithium",
                    "mechanism": "ACE inhibitor giảm thải trừ lithium qua thận",
                    "effect": "Tăng nồng độ lithium, tăng nguy cơ độc tính",
                    "management": "Theo dõi nồng độ lithium. Giảm liều lithium nếu cần."
                },
                {
                    "drug": "Diuretics (furosemide, hydrochlorothiazide)",
                    "mechanism": "Tác dụng hiệp đồng hạ huyết áp",
                    "effect": "Tăng nguy cơ hạ huyết áp quá mức",
                    "management": "Thận trọng khi bắt đầu. Có thể cần giảm liều diuretic."
                }
            ],
            "minor": [
                {
                    "drug": "Allopurinol",
                    "mechanism": "Tăng nguy cơ phản ứng dị ứng",
                    "effect": "Tăng nguy cơ hội chứng Stevens-Johnson",
                    "management": "Thận trọng. Theo dõi dấu hiệu dị ứng."
                }
            ]
        },
        "contraindications": {
            "absolute": [
                "Dị ứng ACE inhibitor",
                "Có thai",
                "Hẹp động mạch thận 2 bên",
                "Phù mạch trước đây với ACE inhibitor"
            ],
            "relative": [
                "Suy thận nặng (CrCl <10) - không dùng",
                "Suy thận trung bình (CrCl 10-30) - giảm liều, theo dõi sát",
                "Tăng kali máu - điều chỉnh trước khi dùng",
                "Hẹp động mạch thận 1 bên - thận trọng",
                "Dùng kali-sparing diuretics - tăng nguy cơ tăng kali máu",
                "Dùng NSAID - tăng nguy cơ suy thận"
            ]
        },
        "pregnancy_lactation": {
            "fda_category": "D",
            "pregnancy_details": "CHỐNG CHỈ ĐỊNH TUYỆT ĐỐI trong thai kỳ. Có thể gây dị tật thai nhi (dị tật thận, xương sọ, phổi), thiểu ối, chậm phát triển thai nhi, và tử vong thai nhi. Nguy cơ cao nhất trong 3 tháng đầu và 3 tháng cuối. Ngừng ngay khi phát hiện có thai.",
            "lactation": {
                "safety": "Compatible",
                "details": "Enalaprilat (hoạt chất) bài tiết vào sữa mẹ ở nồng độ thấp. Nồng độ trong máu trẻ bú mẹ thường rất thấp. Không có báo cáo về tác dụng phụ nghiêm trọng ở trẻ bú mẹ.",
                "recommendation": "Có thể dùng khi cho con bú. Theo dõi trẻ nếu có dấu hiệu bất thường."
            }
        },
        "hepatic_adjustment": {
            "mild": "Không đổi",
            "moderate": "Thận trọng (chuyển hóa một phần qua gan)",
            "severe": "Thận trọng, giảm liều (chuyển hóa một phần qua gan)",
            "notes": "Enalapril là prodrug chuyển hóa thành enalaprilat trong gan. Chủ yếu thải qua thận (60%) nhưng cần gan để chuyển hóa. Suy gan có thể làm giảm chuyển hóa thành hoạt chất."
        },
        "overdose_management": {
            "symptoms": [
                "Hạ huyết áp nghiêm trọng",
                "Nhịp tim chậm",
                "Suy thận cấp",
                "Tăng kali máu",
                "Ho khan",
                "Phù mạch"
            ],
            "antidote": "Không có antidote đặc hiệu. Điều trị hỗ trợ",
            "treatment": [
                "Điều trị hạ huyết áp: Truyền dịch (normal saline), nâng chân, nếu cần: dopamine, norepinephrine",
                "Rửa dạ dày nếu uống trong vòng 1-2 giờ",
                "Than hoạt tính",
                "Theo dõi huyết áp, nhịp tim, chức năng thận, điện giải",
                "Điều trị tăng kali máu nếu có: Calcium gluconate, insulin + glucose, sodium bicarbonate",
                "Nếu có phù mạch: Epinephrine, corticosteroids, antihistamines",
                "Hỗ trợ hô hấp và tuần hoàn nếu cần",
                "Theo dõi ít nhất 12-24 giờ (do half-life của enalaprilat dài: 30-35 giờ)"
            ],
            "monitoring": "Huyết áp, nhịp tim, chức năng thận (creatinine, BUN), điện giải (kali), dấu hiệu phù mạch, ý thức"
        },
        "reversal_agents": {
            "available": False,
            "agents": []
        },
        "administration_instructions": {
            "oral": {
                "with_food": "Có thể uống với hoặc không có thức ăn. Không ảnh hưởng đáng kể đến hấp thu.",
                "timing": "Uống 1-2 lần/ngày (do half-life dài). Khởi đầu với liều thấp (2.5-5mg), tăng dần. Uống đúng giờ mỗi ngày."
            },
            "iv": {
                "reconstitution": "Enalaprilat IV: Pha với D5W hoặc normal saline. Nồng độ cuối: 0.25mg/ml",
                "infusion_rate": "Tiêm trực tiếp qua 5 phút hoặc pha trong 50ml dịch truyền trong 15 phút",
                "compatibility": ["D5W", "Normal saline"],
                "incompatibility": [],
                "notes": "Dạng IV (enalaprilat) chỉ dùng khi cần hạ huyết áp cấp. Theo dõi huyết áp sát."
            }
        },
        "references": {
            "primary_sources": [
                "FDA Drug Label - Vasotec (enalapril)",
                "UpToDate - Enalapril: Drug information",
                "SOLVD Study - New England Journal of Medicine",
                "CONSENSUS Study - New England Journal of Medicine",
                "American Heart Association/American College of Cardiology guidelines"
            ],
            "last_updated": "2024-12-19",
            "evidence_level": "High - Multiple large RCTs (SOLVD, CONSENSUS) and extensive clinical experience"
        }
    },
    "Lisinopril": {
        "group": "Cardiovascular - ACE Inhibitor",
        "vietnamese_name": "Lisinopril, Zestril",
        "administration": ["PO"],
        "indications": [
            "Tăng huyết áp",
            "Suy tim",
            "Sau nhồi máu cơ tim"
        ],
        "contraindications": [
            "Dị ứng ACE inhibitor",
            "Có thai",
            "Hẹp động mạch thận 2 bên"
        ],
        "dosage": {
            "adult_htn": "10-40mg x 1 lần/ngày",
            "adult_heart_failure": "5mg x 1 lần/ngày, tăng đến 20-40mg x 1 lần/ngày",
            "notes": "Liều hàng ngày 1 lần"
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "Liều khởi đầu 5-10mg/ngày",
            "under_30": "Liều khởi đầu 2.5-5mg/ngày"
        },
        "side_effects": [
            "Ho khan",
            "Tăng kali máu",
            "Hạ huyết áp"
        ],
        "interactions": [
            "Kali: tăng kali máu",
            "NSAID: giảm hiệu quả"
        ],
        "pregnancy": "D",
        "mechanism_of_action": "Ức chế angiotensin converting enzyme (ACE), giảm chuyển angiotensin I thành angiotensin II, giảm aldosterone, gây giãn mạch và giảm huyết áp. Không phải prodrug (khác với enalapril), tác dụng trực tiếp",
        "monitoring": [
            "Creatinine, BUN sau 1-2 tuần khi bắt đầu",
            "Kali máu định kỳ",
            "Huyết áp",
            "Ho khan (tác dụng phụ thường gặp)",
            "Dấu hiệu phù mạch (sưng mặt, lưỡi, họng - cấp cứu)"
        ],
        "precautions": [
            "Khởi đầu với liều thấp (5-10mg), tăng dần",
            "Ưu điểm: dùng 1 lần/ngày (compliance tốt hơn)",
            "Không phải prodrug nên tác dụng nhanh hơn enalapril",
            "Theo dõi sát creatinine khi bắt đầu (có thể tăng nhẹ)",
            "Tránh dùng với NSAID (giảm hiệu quả, tăng nguy cơ suy thận)",
            "Ngừng ngay nếu có phù mạch (có thể nguy hiểm tính mạng)"
        ],
        "pharmacokinetics": {
            "half_life": "12 giờ (dài)",
            "onset": "1 giờ",
            "duration": "24 giờ (dài nhất trong các ACE inhibitor)",
            "protein_binding": "25%",
            "clearance": "Thận (100%), không chuyển hóa qua gan"
        },
        "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm, tránh ánh sáng",
        "black_box_warnings": "Chống chỉ định trong thai kỳ - có thể gây dị tật thai nhi và tử vong thai nhi. Phù mạch có thể đe dọa tính mạng",
        "drug_interactions": {
            "major": [
                {
                    "drug": "Kali bổ sung, Kali-sparing diuretics (spironolactone, eplerenone, amiloride, triamterene)",
                    "mechanism": "Tác dụng hiệp đồng tăng kali máu",
                    "effect": "Tăng kali máu nghiêm trọng, có thể gây rối loạn nhịp tim",
                    "management": "Thận trọng. Theo dõi kali máu thường xuyên. Tránh dùng cùng nếu có thể."
                },
                {
                    "drug": "NSAIDs (ibuprofen, naproxen, diclofenac)",
                    "mechanism": "Giảm tác dụng giãn mạch, giảm lưu lượng máu thận",
                    "effect": "Giảm hiệu quả hạ huyết áp, tăng nguy cơ suy thận cấp",
                    "management": "Thận trọng. Theo dõi chức năng thận, huyết áp. Tránh dùng lâu dài cùng."
                }
            ],
            "moderate": [
                {
                    "drug": "Lithium",
                    "mechanism": "ACE inhibitor giảm thải trừ lithium qua thận",
                    "effect": "Tăng nồng độ lithium, tăng nguy cơ độc tính",
                    "management": "Theo dõi nồng độ lithium. Giảm liều lithium nếu cần."
                },
                {
                    "drug": "Diuretics (furosemide, hydrochlorothiazide)",
                    "mechanism": "Tác dụng hiệp đồng hạ huyết áp",
                    "effect": "Tăng nguy cơ hạ huyết áp quá mức",
                    "management": "Thận trọng khi bắt đầu. Có thể cần giảm liều diuretic."
                }
            ],
            "minor": [
                {
                    "drug": "Allopurinol",
                    "mechanism": "Tăng nguy cơ phản ứng dị ứng",
                    "effect": "Tăng nguy cơ hội chứng Stevens-Johnson",
                    "management": "Thận trọng. Theo dõi dấu hiệu dị ứng."
                }
            ]
        },
        "contraindications": {
            "absolute": [
                "Dị ứng ACE inhibitor",
                "Có thai",
                "Hẹp động mạch thận 2 bên",
                "Phù mạch trước đây với ACE inhibitor"
            ],
            "relative": [
                "Suy thận nặng (CrCl <10) - không dùng",
                "Suy thận trung bình (CrCl 10-30) - giảm liều, theo dõi sát",
                "Tăng kali máu - điều chỉnh trước khi dùng",
                "Hẹp động mạch thận 1 bên - thận trọng",
                "Dùng kali-sparing diuretics - tăng nguy cơ tăng kali máu",
                "Dùng NSAID - tăng nguy cơ suy thận"
            ]
        },
        "pregnancy_lactation": {
            "fda_category": "D",
            "pregnancy_details": "CHỐNG CHỈ ĐỊNH TUYỆT ĐỐI trong thai kỳ. Có thể gây dị tật thai nhi (dị tật thận, xương sọ, phổi), thiểu ối, chậm phát triển thai nhi, và tử vong thai nhi. Nguy cơ cao nhất trong 3 tháng đầu và 3 tháng cuối. Ngừng ngay khi phát hiện có thai.",
            "lactation": {
                "safety": "Compatible",
                "details": "Lisinopril bài tiết vào sữa mẹ ở nồng độ thấp. Nồng độ trong máu trẻ bú mẹ thường rất thấp. Không có báo cáo về tác dụng phụ nghiêm trọng ở trẻ bú mẹ.",
                "recommendation": "Có thể dùng khi cho con bú. Theo dõi trẻ nếu có dấu hiệu bất thường."
            }
        },
        "hepatic_adjustment": {
            "mild": "Không đổi",
            "moderate": "Không đổi",
            "severe": "Không đổi (100% thải qua thận, không chuyển hóa qua gan)",
            "notes": "Lisinopril 100% thải qua thận, không chuyển hóa qua gan. Không cần điều chỉnh liều ở suy gan."
        },
        "overdose_management": {
            "symptoms": [
                "Hạ huyết áp nghiêm trọng",
                "Nhịp tim chậm",
                "Suy thận cấp",
                "Tăng kali máu",
                "Ho khan",
                "Phù mạch"
            ],
            "antidote": "Không có antidote đặc hiệu. Điều trị hỗ trợ",
            "treatment": [
                "Điều trị hạ huyết áp: Truyền dịch (normal saline), nâng chân, nếu cần: dopamine, norepinephrine",
                "Rửa dạ dày nếu uống trong vòng 1-2 giờ",
                "Than hoạt tính",
                "Theo dõi huyết áp, nhịp tim, chức năng thận, điện giải",
                "Điều trị tăng kali máu nếu có: Calcium gluconate, insulin + glucose, sodium bicarbonate",
                "Nếu có phù mạch: Epinephrine, corticosteroids, antihistamines",
                "Hỗ trợ hô hấp và tuần hoàn nếu cần",
                "Theo dõi ít nhất 12-24 giờ (do half-life 12 giờ)"
            ],
            "monitoring": "Huyết áp, nhịp tim, chức năng thận (creatinine, BUN), điện giải (kali), dấu hiệu phù mạch, ý thức"
        },
        "reversal_agents": {
            "available": False,
            "agents": []
        },
        "administration_instructions": {
            "oral": {
                "with_food": "Có thể uống với hoặc không có thức ăn. Không ảnh hưởng đáng kể đến hấp thu.",
                "timing": "Uống 1 lần/ngày (do half-life dài và duration 24 giờ). Khởi đầu với liều thấp (5-10mg), tăng dần. Uống đúng giờ mỗi ngày. Ưu điểm: compliance tốt hơn do chỉ uống 1 lần/ngày."
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
                "FDA Drug Label - Zestril (lisinopril)",
                "UpToDate - Lisinopril: Drug information",
                "ATLAS Study - Circulation",
                "GISSI-3 Study - The Lancet",
                "American Heart Association/American College of Cardiology guidelines"
            ],
            "last_updated": "2024-12-19",
            "evidence_level": "High - Multiple large RCTs (ATLAS, GISSI-3) and extensive clinical experience"
        }
    },
    # ARBs
    "Losartan": {
        "group": "Cardiovascular - ARB (Angiotensin Receptor Blocker)",
        "vietnamese_name": "Losartan, Cozaar",
        "administration": ["PO"],
        "indications": [
            "Tăng huyết áp",
            "Suy tim (không dung nạp ACE inhibitor)",
            "Bảo vệ thận trong đái tháo đường"
        ],
        "contraindications": [
            "Dị ứng ARB",
            "Có thai",
            "Hẹp động mạch thận 2 bên"
        ],
        "dosage": {
            "adult_htn": "50-100mg x 1-2 lần/ngày",
            "adult_heart_failure": "25-50mg x 1 lần/ngày, tăng đến 50-100mg x 1 lần/ngày",
            "notes": "Ít gây ho hơn ACE inhibitor"
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "Liều khởi đầu 25mg/ngày",
            "under_30": "Thận trọng, theo dõi sát"
        },
        "side_effects": [
            "Ít tác dụng phụ hơn ACE inhibitor",
            "Ho ít hơn ACE inhibitor",
            "Tăng kali máu (ít hơn ACE)",
            "Hạ huyết áp"
        ],
        "interactions": [
            "Kali: tăng kali máu",
            "NSAID: giảm hiệu quả"
        ],
        "pregnancy": "D",
        "mechanism_of_action": "Losartan là prodrug, chuyển hóa thành EXP-3174 (hoạt chất) trong gan. Ức chế thụ thể angiotensin II type 1 (AT1), ngăn chặn tác dụng của angiotensin II (giãn mạch, giảm aldosterone). Ít gây ho hơn ACE inhibitor vì không ảnh hưởng đến bradykinin",
        "monitoring": [
            "Creatinine, BUN sau 1-2 tuần khi bắt đầu",
            "Kali máu định kỳ (ít hơn ACE inhibitor)",
            "Huyết áp",
            "Ít phải theo dõi ho khan (không gây ho như ACE inhibitor)"
        ],
        "precautions": [
            "Khởi đầu với liều thấp (25-50mg), tăng dần",
            "Ưu điểm: ít gây ho hơn ACE inhibitor (thay thế tốt cho bệnh nhân không dung nạp ACE inhibitor)",
            "Vẫn có thể gây tăng kali máu và suy thận cấp (nhưng ít hơn ACE inhibitor)",
            "Theo dõi sát creatinine khi bắt đầu",
            "Tránh dùng với NSAID (giảm hiệu quả, tăng nguy cơ suy thận)",
            "Ngừng ngay nếu có phù mạch (hiếm hơn ACE inhibitor nhưng vẫn có thể xảy ra)"
        ],
        "pharmacokinetics": {
            "half_life": "Losartan: 2 giờ; EXP-3174 (active): 6-9 giờ",
            "onset": "1 giờ",
            "duration": "24 giờ",
            "protein_binding": "98.7%",
            "clearance": "Gan (chuyển hóa), thận (EXP-3174)"
        },
        "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm, tránh ánh sáng",
        "black_box_warnings": "Chống chỉ định trong thai kỳ - có thể gây dị tật thai nhi và tử vong thai nhi",
        "drug_interactions": {
            "major": [
                {
                    "drug": "Kali bổ sung, Kali-sparing diuretics (spironolactone, eplerenone, amiloride, triamterene)",
                    "mechanism": "Tác dụng hiệp đồng tăng kali máu",
                    "effect": "Tăng kali máu nghiêm trọng, có thể gây rối loạn nhịp tim",
                    "management": "Thận trọng. Theo dõi kali máu thường xuyên. Tránh dùng cùng nếu có thể."
                },
                {
                    "drug": "NSAIDs (ibuprofen, naproxen, diclofenac)",
                    "mechanism": "Giảm tác dụng giãn mạch, giảm lưu lượng máu thận",
                    "effect": "Giảm hiệu quả hạ huyết áp, tăng nguy cơ suy thận cấp",
                    "management": "Thận trọng. Theo dõi chức năng thận, huyết áp. Tránh dùng lâu dài cùng."
                }
            ],
            "moderate": [
                {
                    "drug": "Lithium",
                    "mechanism": "ARB giảm thải trừ lithium qua thận",
                    "effect": "Tăng nồng độ lithium, tăng nguy cơ độc tính",
                    "management": "Theo dõi nồng độ lithium. Giảm liều lithium nếu cần."
                },
                {
                    "drug": "Diuretics (furosemide, hydrochlorothiazide)",
                    "mechanism": "Tác dụng hiệp đồng hạ huyết áp",
                    "effect": "Tăng nguy cơ hạ huyết áp quá mức",
                    "management": "Thận trọng khi bắt đầu. Có thể cần giảm liều diuretic."
                }
            ],
            "minor": [
                {
                    "drug": "Rifampin",
                    "mechanism": "CYP2C9 inducer làm giảm chuyển hóa losartan",
                    "effect": "Giảm hiệu quả hạ huyết áp",
                    "management": "Theo dõi huyết áp. Có thể cần tăng liều losartan."
                }
            ]
        },
        "contraindications": {
            "absolute": [
                "Dị ứng ARB",
                "Có thai",
                "Hẹp động mạch thận 2 bên",
                "Phù mạch trước đây với ARB"
            ],
            "relative": [
                "Suy thận nặng (CrCl <10) - không dùng",
                "Suy thận trung bình (CrCl 10-30) - giảm liều, theo dõi sát",
                "Tăng kali máu - điều chỉnh trước khi dùng",
                "Hẹp động mạch thận 1 bên - thận trọng",
                "Dùng kali-sparing diuretics - tăng nguy cơ tăng kali máu",
                "Dùng NSAID - tăng nguy cơ suy thận"
            ]
        },
        "pregnancy_lactation": {
            "fda_category": "D",
            "pregnancy_details": "CHỐNG CHỈ ĐỊNH TUYỆT ĐỐI trong thai kỳ. Có thể gây dị tật thai nhi (dị tật thận, xương sọ, phổi), thiểu ối, chậm phát triển thai nhi, và tử vong thai nhi. Nguy cơ cao nhất trong 3 tháng đầu và 3 tháng cuối. Ngừng ngay khi phát hiện có thai.",
            "lactation": {
                "safety": "Compatible",
                "details": "Losartan và EXP-3174 bài tiết vào sữa mẹ ở nồng độ thấp. Nồng độ trong máu trẻ bú mẹ thường rất thấp. Không có báo cáo về tác dụng phụ nghiêm trọng ở trẻ bú mẹ.",
                "recommendation": "Có thể dùng khi cho con bú. Theo dõi trẻ nếu có dấu hiệu bất thường."
            }
        },
        "hepatic_adjustment": {
            "mild": "Không đổi",
            "moderate": "Thận trọng, có thể giảm liều (chuyển hóa qua gan)",
            "severe": "Giảm liều 50% (chuyển hóa qua gan)",
            "notes": "Losartan là prodrug chuyển hóa thành EXP-3174 trong gan (CYP2C9). Suy gan có thể làm giảm chuyển hóa thành hoạt chất. EXP-3174 thải qua thận."
        },
        "overdose_management": {
            "symptoms": [
                "Hạ huyết áp nghiêm trọng",
                "Nhịp tim chậm",
                "Suy thận cấp",
                "Tăng kali máu",
                "Phù mạch (hiếm)"
            ],
            "antidote": "Không có antidote đặc hiệu. Điều trị hỗ trợ",
            "treatment": [
                "Điều trị hạ huyết áp: Truyền dịch (normal saline), nâng chân, nếu cần: dopamine, norepinephrine",
                "Rửa dạ dày nếu uống trong vòng 1-2 giờ",
                "Than hoạt tính",
                "Theo dõi huyết áp, nhịp tim, chức năng thận, điện giải",
                "Điều trị tăng kali máu nếu có: Calcium gluconate, insulin + glucose, sodium bicarbonate",
                "Nếu có phù mạch: Epinephrine, corticosteroids, antihistamines",
                "Hỗ trợ hô hấp và tuần hoàn nếu cần",
                "Theo dõi ít nhất 12-24 giờ (do half-life của EXP-3174: 6-9 giờ)"
            ],
            "monitoring": "Huyết áp, nhịp tim, chức năng thận (creatinine, BUN), điện giải (kali), dấu hiệu phù mạch, ý thức"
        },
        "reversal_agents": {
            "available": False,
            "agents": []
        },
        "administration_instructions": {
            "oral": {
                "with_food": "Có thể uống với hoặc không có thức ăn. Không ảnh hưởng đáng kể đến hấp thu.",
                "timing": "Uống 1-2 lần/ngày (do half-life của EXP-3174: 6-9 giờ). Khởi đầu với liều thấp (25-50mg), tăng dần. Uống đúng giờ mỗi ngày. Ưu điểm: ít gây ho hơn ACE inhibitor."
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
                "FDA Drug Label - Cozaar (losartan)",
                "UpToDate - Losartan: Drug information",
                "ELITE-2 Study - The Lancet",
                "LIFE Study - The Lancet",
                "American Heart Association/American College of Cardiology guidelines"
            ],
            "last_updated": "2024-12-19",
            "evidence_level": "High - Multiple large RCTs (ELITE-2, LIFE) and extensive clinical experience"
        }
    },
    # Beta-blockers
    "Metoprolol": {
        "group": "Cardiovascular - Beta-blocker",
        "vietnamese_name": "Metoprolol, Betaloc",
        "administration": ["PO", "IV"],
        "indications": [
            "Tăng huyết áp",
            "Suy tim",
            "Rối loạn nhịp tim",
            "Sau nhồi máu cơ tim",
            "Đau thắt ngực"
        ],
        "contraindications": [
            "Hen phế quản nặng",
            "Block nhĩ thất độ 2-3",
            "Suy tim cấp không bù",
            "Nhịp tim chậm nặng"
        ],
        "dosage": {
            "adult_po": "25-200mg x 2 lần/ngày (tartrate) hoặc 50-200mg x 1 lần/ngày (succinate)",
            "adult_iv": "2.5-5mg IV mỗi 5 phút x 3 lần (tối đa 15mg)",
            "heart_failure": "12.5-25mg x 2 lần/ngày, tăng dần đến 200mg x 2 lần/ngày",
            "notes": "Tartrate: ngắn tác dụng, Succinate: dài tác dụng"
        },
        "side_effects": [
            "Mệt mỏi",
            "Lạnh tay chân",
            "Nhịp tim chậm",
            "Rối loạn giấc ngủ",
            "Khó thở ở bệnh nhân hen/COPD"
        ],
        "interactions": [
            "Verapamil/Diltiazem: tăng nguy cơ block nhĩ thất",
            "Insulin: che dấu triệu chứng hạ đường huyết",
            "NSAID: giảm hiệu quả"
        ],
        "pregnancy": "C",
        "mechanism_of_action": "Ức chế thụ thể beta-1 chọn lọc, giảm nhịp tim, lực co bóp cơ tim, và dẫn truyền nhĩ thất",
        "monitoring": [
            "Huyết áp, nhịp tim mỗi lần khám",
            "ECG nếu có triệu chứng block nhĩ thất",
            "Đường huyết ở bệnh nhân đái tháo đường (che dấu triệu chứng hạ đường huyết)",
            "Chức năng gan, thận định kỳ"
        ],
        "precautions": [
            "Không ngừng đột ngột (có thể gây cơn tăng huyết áp phản hồi)",
            "Giảm liều từ từ khi ngừng",
            "Thận trọng với bệnh nhân hen/COPD (có thể gây co thắt phế quản)",
            "Theo dõi suy tim mới xuất hiện"
        ],
        "pharmacokinetics": {
            "half_life": "3-7 giờ (tartrate), 3-4 giờ (succinate)",
            "onset": "1-2 giờ (PO), 15 phút (IV)",
            "duration": "6-12 giờ (tartrate), 24 giờ (succinate)",
            "protein_binding": "12%",
            "clearance": "Gan (CYP2D6)"
                },
        "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm",
        "black_box_warnings": "Không ngừng đột ngột - có thể gây tăng huyết áp phản hồi, đau thắt ngực, nhồi máu cơ tim. Giảm liều từ từ trong 1-2 tuần. Suy tim cấp có thể xảy ra nếu dùng ở bệnh nhân suy tim không bù trừ",
        "drug_interactions": {
            "major": [
                {
                    "drug": "Verapamil, Diltiazem",
                    "mechanism": "Tác dụng hiệp đồng ức chế dẫn truyền nhĩ thất và co bóp tim",
                    "effect": "Tăng nguy cơ block nhĩ thất độ 2-3, nhịp tim chậm nặng, suy tim",
                    "management": "Thận trọng. Tránh dùng cùng nếu có thể. Nếu cần, dùng liều thấp và theo dõi ECG sát."
                }
            ],
            "moderate": [
                {
                    "drug": "Insulin, các thuốc hạ đường huyết",
                    "mechanism": "Che dấu triệu chứng hạ đường huyết (nhịp tim nhanh, run rẩy)",
                    "effect": "Tăng nguy cơ hạ đường huyết không được phát hiện, nguy hiểm",
                    "management": "Theo dõi đường huyết thường xuyên. Bệnh nhân đái tháo đường nên biết các triệu chứng khác của hạ đường huyết."
                },
                {
                    "drug": "NSAIDs (ibuprofen, naproxen)",
                    "mechanism": "Giảm tác dụng hạ huyết áp",
                    "effect": "Giảm hiệu quả điều trị tăng huyết áp",
                    "management": "Thận trọng. Theo dõi huyết áp. Tránh dùng lâu dài cùng."
                },
                {
                    "drug": "CYP2D6 inhibitors (fluoxetine, paroxetine, quinidine)",
                    "mechanism": "Ức chế chuyển hóa metoprolol",
                    "effect": "Tăng nồng độ metoprolol, tăng tác dụng phụ",
                    "management": "Theo dõi nhịp tim, huyết áp. Có thể cần giảm liều metoprolol."
                }
            ],
            "minor": [
                {
                    "drug": "Diphenhydramine",
                    "mechanism": "Tăng nguy cơ an thần",
                    "effect": "Tăng tác dụng an thần",
                    "management": "Thận trọng. Tránh lái xe hoặc vận hành máy móc."
                }
            ]
        },
        "contraindications": {
            "absolute": [
                "Hen phế quản nặng",
                "Block nhĩ thất độ 2-3",
                "Suy tim cấp không bù",
                "Nhịp tim chậm nặng (<50 bpm)",
                "Sốc tim",
                "Hội chứng sick sinus (trừ khi có máy tạo nhịp)"
            ],
            "relative": [
                "COPD (thận trọng, có thể dùng liều thấp)",
                "Đái tháo đường (che dấu triệu chứng hạ đường huyết)",
                "Bệnh mạch máu ngoại biên (có thể làm nặng)",
                "Suy gan (giảm chuyển hóa)",
                "Dùng với verapamil/diltiazem (tăng nguy cơ block AV)"
            ]
        },
        "pregnancy_lactation": {
            "fda_category": "C",
            "pregnancy_details": "Có thể dùng khi cần thiết. Có thể gây nhịp tim chậm thai nhi, hạ đường huyết, giảm thông khí. Theo dõi sát thai nhi. Ưu tiên dùng trong 3 tháng cuối nếu có thể.",
            "lactation": {
                "safety": "Compatible",
                "details": "Metoprolol bài tiết vào sữa mẹ ở nồng độ thấp. Nồng độ trong máu trẻ bú mẹ thường rất thấp. Không có báo cáo về tác dụng phụ nghiêm trọng ở trẻ bú mẹ.",
                "recommendation": "Có thể dùng khi cho con bú. Theo dõi trẻ nếu có dấu hiệu nhịp tim chậm hoặc hạ đường huyết."
            }
        },
        "hepatic_adjustment": {
            "mild": "Không đổi",
            "moderate": "Thận trọng, có thể giảm liều (chuyển hóa qua gan)",
            "severe": "Giảm liều 50% (chuyển hóa qua gan CYP2D6)",
            "notes": "Metoprolol chuyển hóa qua gan (CYP2D6). Suy gan có thể làm giảm chuyển hóa, tăng nồng độ và tác dụng phụ."
        },
        "overdose_management": {
            "symptoms": [
                "Nhịp tim chậm nặng (<40 bpm)",
                "Block nhĩ thất độ 2-3",
                "Hạ huyết áp nặng",
                "Suy tim cấp",
                "Co thắt phế quản",
                "Hạ đường huyết",
                "Ngất"
            ],
            "antidote": "Atropine (cho nhịp tim chậm), Glucagon (cho suy tim), Epinephrine (cho hạ huyết áp nặng)",
            "treatment": [
                "Rửa dạ dày nếu uống trong vòng 1-2 giờ",
                "Than hoạt tính",
                "Điều trị nhịp tim chậm: Atropine 0.5-1mg IV, có thể lặp lại",
                "Nếu atropine không hiệu quả: Glucagon 1-5mg IV (kích thích tim qua cơ chế không phụ thuộc beta-receptor)",
                "Điều trị hạ huyết áp: Truyền dịch, nâng chân, nếu cần: dopamine, norepinephrine",
                "Điều trị block AV: Atropine, nếu cần: máy tạo nhịp tạm thời",
                "Điều trị co thắt phế quản: Albuterol, ipratropium",
                "Điều trị hạ đường huyết: Glucose IV",
                "Hỗ trợ hô hấp và tuần hoàn nếu cần",
                "Theo dõi ít nhất 12-24 giờ (do half-life 3-7 giờ)"
            ],
            "monitoring": "Nhịp tim, huyết áp, ECG (block AV, rối loạn nhịp), đường huyết, chức năng hô hấp, ý thức"
        },
        "reversal_agents": {
            "available": True,
            "agents": [
                {
                    "name": "Glucagon",
                    "mechanism": "Kích thích tim qua cơ chế không phụ thuộc beta-receptor (tăng cAMP)",
                    "indication": "Suy tim, nhịp tim chậm nặng do beta-blocker",
                    "dose": "1-5mg IV, có thể lặp lại"
                },
                {
                    "name": "Atropine",
                    "mechanism": "Ức chế phó giao cảm, tăng nhịp tim",
                    "indication": "Nhịp tim chậm, block nhĩ thất",
                    "dose": "0.5-1mg IV, có thể lặp lại"
                }
            ]
        },
        "administration_instructions": {
            "oral": {
                "with_food": "Có thể uống với hoặc không có thức ăn. Uống với thức ăn có thể giảm tác dụng phụ đầu tiên.",
                "timing": "Tartrate: 2 lần/ngày. Succinate: 1 lần/ngày. Uống cùng giờ mỗi ngày. KHÔNG ngừng đột ngột - giảm liều dần dần trong 1-2 tuần."
            },
            "iv": {
                "reconstitution": "Dùng trực tiếp từ lọ. Không pha loãng.",
                "infusion_rate": "Tiêm trực tiếp 2.5-5mg mỗi 5 phút, tối đa 15mg. Theo dõi ECG và huyết áp sát.",
                "compatibility": ["D5W", "Normal saline"],
                "incompatibility": [],
                "notes": "Dùng cho cấp cứu. Theo dõi ECG và huyết áp liên tục. Chuyển sang PO càng sớm càng tốt."
            }
        },
        "references": {
            "primary_sources": [
                "FDA Drug Label - Lopressor (metoprolol tartrate), Toprol-XL (metoprolol succinate)",
                "UpToDate - Metoprolol: Drug information",
                "MERIT-HF Study - The Lancet",
                "Goteborg Metoprolol Trial - The Lancet",
                "American Heart Association/American College of Cardiology guidelines"
            ],
            "last_updated": "2024-12-19",
            "evidence_level": "High - Multiple large RCTs (MERIT-HF, Goteborg) and extensive clinical experience"
        }
    },
    "Propranolol": {
        "group": "Cardiovascular - Beta-blocker (non-selective)",
        "vietnamese_name": "Propranolol, Inderal",
        "administration": ["PO"],
        "indications": [
            "Tăng huyết áp",
            "Đau thắt ngực",
            "Rối loạn nhịp tim",
            "Migraine phòng ngừa",
            "Run cơ",
            "Lo âu"
        ],
        "contraindications": [
            "Hen phế quản",
            "Suy tim cấp",
            "Block nhĩ thất độ 2-3",
            "Nhịp tim chậm nặng"
        ],
        "dosage": {
            "adult_htn": "40-160mg x 2 lần/ngày",
            "adult_angina": "80-320mg x 2-3 lần/ngày",
            "adult_migraine": "20-40mg x 2-3 lần/ngày",
            "notes": "Non-selective, ức chế cả beta1 và beta2"
        },
        "side_effects": [
            "Mệt mỏi",
            "Lạnh tay chân",
            "Nhịp tim chậm",
            "Co thắt phế quản",
            "Giảm libido"
        ],
                  "interactions": [
              "Verapamil: tăng nguy cơ block nhĩ thất",
              "Insulin: che dấu triệu chứng hạ đường huyết"
          ],
          "pregnancy": "C",
          "mechanism_of_action": "Non-selective beta-adrenergic receptor blocker (beta1 và beta2). Ức chế tác dụng của catecholamines (epinephrine, norepinephrine), giảm nhịp tim, giảm co bóp cơ tim, giảm huyết áp, giảm nhu cầu oxy cơ tim. Ức chế renin-angiotensin system. Có tác dụng chống loạn nhịp (class II antiarrhythmic).",
          "monitoring": [
              "Nhịp tim và huyết áp (trước và sau khi bắt đầu)",
              "Dấu hiệu suy tim (khó thở, phù, tăng cân)",
              "Chức năng phổi (nếu có bệnh phổi tắc nghẽn)",
              "Đường huyết (đặc biệt ở bệnh nhân đái tháo đường - che dấu triệu chứng hạ đường huyết)",
              "Triệu chứng mệt mỏi, lạnh tay chân, rối loạn cương dương"
          ],
          "precautions": [
              "KHÔNG được ngừng đột ngột (có thể gây rebound hypertension, đau thắt ngực nặng, nhồi máu cơ tim). Phải giảm liều dần trong 1-2 tuần",
              "Thận trọng ở bệnh nhân hen phế quản/COPD (có thể gây co thắt phế quản nặng)",
              "Tránh dùng trong suy tim cấp, block AV độ 2-3, nhịp tim chậm <50 bpm",
              "Thận trọng ở bệnh nhân đái tháo đường (che dấu triệu chứng hạ đường huyết)",
              "Có thể gây mệt mỏi, giảm khả năng tập luyện",
              "Thận trọng khi dùng với verapamil/diltiazem (tăng nguy cơ block AV, suy tim)"
          ],
          "pharmacokinetics": {
              "half_life": "3-5 giờ (ngắn), nhưng tác dụng kéo dài hơn do tác dụng trên receptor",
              "onset": "1-2 giờ (PO)",
              "duration": "6-12 giờ",
              "protein_binding": "90-95%",
              "clearance": "Gan (extensive first-pass metabolism), CYP2D6, CYP1A2"
          },
          "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm, tránh ánh sáng",
          "black_box_warnings": "KHÔNG được ngừng đột ngột ở bệnh nhân đau thắt ngực - có thể gây đau thắt ngực nặng, nhồi máu cơ tim, rối loạn nhịp tim nặng. Phải giảm liều dần dần trong 1-2 tuần",
          "drug_interactions": {
              "major": [
                  {
                      "drug": "Verapamil, Diltiazem",
                      "mechanism": "Tác dụng hiệp đồng ức chế dẫn truyền nhĩ thất và co bóp tim",
                      "effect": "Tăng nguy cơ block nhĩ thất độ 2-3, nhịp tim chậm nặng, suy tim",
                      "management": "Thận trọng. Tránh dùng cùng nếu có thể. Nếu cần, dùng liều thấp và theo dõi ECG sát."
                  }
              ],
              "moderate": [
                  {
                      "drug": "Insulin, các thuốc hạ đường huyết",
                      "mechanism": "Che dấu triệu chứng hạ đường huyết (nhịp tim nhanh, run rẩy)",
                      "effect": "Tăng nguy cơ hạ đường huyết không được phát hiện, nguy hiểm",
                      "management": "Theo dõi đường huyết thường xuyên. Bệnh nhân đái tháo đường nên biết các triệu chứng khác của hạ đường huyết."
                  },
                  {
                      "drug": "NSAIDs (ibuprofen, naproxen)",
                      "mechanism": "Giảm tác dụng hạ huyết áp",
                      "effect": "Giảm hiệu quả điều trị tăng huyết áp",
                      "management": "Thận trọng. Theo dõi huyết áp. Tránh dùng lâu dài cùng."
                  },
                  {
                      "drug": "CYP2D6, CYP1A2 inhibitors (fluoxetine, cimetidine, ciprofloxacin)",
                      "mechanism": "Ức chế chuyển hóa propranolol",
                      "effect": "Tăng nồng độ propranolol, tăng tác dụng phụ",
                      "management": "Theo dõi nhịp tim, huyết áp. Có thể cần giảm liều propranolol."
                  }
              ],
              "minor": [
                  {
                      "drug": "Chlorpromazine",
                      "mechanism": "Tăng nguy cơ an thần",
                      "effect": "Tăng tác dụng an thần",
                      "management": "Thận trọng. Tránh lái xe hoặc vận hành máy móc."
                  }
              ]
          },
          "contraindications": {
              "absolute": [
                  "Hen phế quản",
                  "Suy tim cấp",
                  "Block nhĩ thất độ 2-3",
                  "Nhịp tim chậm nặng (<50 bpm)",
                  "Sốc tim",
                  "Hội chứng sick sinus (trừ khi có máy tạo nhịp)"
              ],
              "relative": [
                  "COPD (thận trọng, có thể dùng liều thấp nhưng nguy cơ co thắt phế quản cao hơn)",
                  "Đái tháo đường (che dấu triệu chứng hạ đường huyết)",
                  "Bệnh mạch máu ngoại biên (có thể làm nặng)",
                  "Suy gan (giảm chuyển hóa, extensive first-pass)",
                  "Dùng với verapamil/diltiazem (tăng nguy cơ block AV)"
              ]
          },
          "pregnancy_lactation": {
              "fda_category": "C",
              "pregnancy_details": "Có thể dùng khi cần thiết. Có thể gây nhịp tim chậm thai nhi, hạ đường huyết, giảm thông khí. Theo dõi sát thai nhi. Ưu tiên dùng trong 3 tháng cuối nếu có thể.",
              "lactation": {
                  "safety": "Compatible",
                  "details": "Propranolol bài tiết vào sữa mẹ ở nồng độ thấp. Nồng độ trong máu trẻ bú mẹ thường rất thấp. Không có báo cáo về tác dụng phụ nghiêm trọng ở trẻ bú mẹ.",
                  "recommendation": "Có thể dùng khi cho con bú. Theo dõi trẻ nếu có dấu hiệu nhịp tim chậm hoặc hạ đường huyết."
              }
          },
          "hepatic_adjustment": {
              "mild": "Không đổi",
              "moderate": "Thận trọng, có thể giảm liều (extensive first-pass metabolism)",
              "severe": "Giảm liều 50% (extensive first-pass metabolism qua gan)",
              "notes": "Propranolol có extensive first-pass metabolism qua gan (CYP2D6, CYP1A2). Suy gan có thể làm giảm chuyển hóa, tăng nồng độ và tác dụng phụ."
          },
          "overdose_management": {
              "symptoms": [
                  "Nhịp tim chậm nặng (<40 bpm)",
                  "Block nhĩ thất độ 2-3",
                  "Hạ huyết áp nặng",
                  "Suy tim cấp",
                  "Co thắt phế quản nặng",
                  "Hạ đường huyết",
                  "Ngất",
                  "Sốc tim"
              ],
              "antidote": "Atropine (cho nhịp tim chậm), Glucagon (cho suy tim), Epinephrine (cho hạ huyết áp nặng)",
              "treatment": [
                  "Rửa dạ dày nếu uống trong vòng 1-2 giờ",
                  "Than hoạt tính",
                  "Điều trị nhịp tim chậm: Atropine 0.5-1mg IV, có thể lặp lại",
                  "Nếu atropine không hiệu quả: Glucagon 1-5mg IV (kích thích tim qua cơ chế không phụ thuộc beta-receptor)",
                  "Điều trị hạ huyết áp: Truyền dịch, nâng chân, nếu cần: dopamine, norepinephrine",
                  "Điều trị block AV: Atropine, nếu cần: máy tạo nhịp tạm thời",
                  "Điều trị co thắt phế quản: Albuterol, ipratropium (quan trọng vì non-selective)",
                  "Điều trị hạ đường huyết: Glucose IV",
                  "Hỗ trợ hô hấp và tuần hoàn nếu cần",
                  "Theo dõi ít nhất 12-24 giờ (do half-life 3-5 giờ nhưng tác dụng kéo dài)"
              ],
              "monitoring": "Nhịp tim, huyết áp, ECG (block AV, rối loạn nhịp), đường huyết, chức năng hô hấp (đặc biệt quan trọng), ý thức"
          },
          "reversal_agents": {
              "available": True,
              "agents": [
                  {
                      "name": "Glucagon",
                      "mechanism": "Kích thích tim qua cơ chế không phụ thuộc beta-receptor (tăng cAMP)",
                      "indication": "Suy tim, nhịp tim chậm nặng do beta-blocker",
                      "dose": "1-5mg IV, có thể lặp lại"
                  },
                  {
                      "name": "Atropine",
                      "mechanism": "Ức chế phó giao cảm, tăng nhịp tim",
                      "indication": "Nhịp tim chậm, block nhĩ thất",
                      "dose": "0.5-1mg IV, có thể lặp lại"
                  }
              ]
          },
          "administration_instructions": {
              "oral": {
                  "with_food": "Uống với thức ăn để giảm tác dụng phụ và tăng hấp thu (giảm first-pass metabolism).",
                  "timing": "Uống 2-3 lần/ngày (do half-life ngắn). Uống cùng giờ mỗi ngày. KHÔNG ngừng đột ngột - giảm liều dần dần trong 1-2 tuần."
              },
              "iv": {
                  "reconstitution": "Không có dạng IV thường dùng",
                  "infusion_rate": "N/A",
                  "compatibility": [],
                  "incompatibility": [],
                  "notes": "Chỉ có dạng uống thường dùng"
              }
          },
          "references": {
              "primary_sources": [
                  "FDA Drug Label - Inderal (propranolol)",
                  "UpToDate - Propranolol: Drug information",
                  "Beta-Blocker Heart Attack Trial - JAMA",
                  "ISIS-1 Study - The Lancet",
                  "American Heart Association/American College of Cardiology guidelines"
              ],
              "last_updated": "2024-12-19",
              "evidence_level": "High - Multiple large RCTs (BHAT, ISIS-1) and extensive clinical experience"
          }
      },
    # Calcium Channel Blockers
    "Amlodipine": {
        "group": "Cardiovascular - Calcium Channel Blocker (Dihydropyridine)",
        "vietnamese_name": "Amlodipine, Norvasc",
        "administration": ["PO"],
        "indications": [
            "Tăng huyết áp",
            "Đau thắt ngực"
        ],
        "contraindications": [
            "Dị ứng",
            "Sốc tim"
        ],
        "dosage": {
            "adult_htn": "2.5-10mg x 1 lần/ngày",
            "adult_angina": "5-10mg x 1 lần/ngày",
            "notes": "Tác dụng dài, uống 1 lần/ngày"
        },
        "side_effects": [
            "Phù chân",
            "Đỏ mặt",
            "Nhức đầu",
            "Chóng mặt",
            "Tim đập nhanh (phản ứng)"
        ],
        "interactions": [
            "Simvastatin: tăng nồng độ simvastatin",
            "Grapefruit juice: tăng nồng độ"
        ],
        "pregnancy": "C",
        "mechanism_of_action": "Ức chế dòng calci vào tế bào cơ trơn mạch máu, gây giãn mạch, giảm kháng lực mạch máu ngoại biên",
        "monitoring": [
            "Huyết áp mỗi lần khám",
            "Nhịp tim (có thể tăng nhẹ phản ứng)",
            "Phù chân (dấu hiệu tác dụng phụ)",
            "Chức năng gan định kỳ"
        ],
        "precautions": [
            "Phù chân thường gặp, thường không nghiêm trọng nhưng có thể khó chịu",
            "Tránh grapefruit juice (tăng nồng độ)",
            "Có thể dùng với thức ăn hoặc không",
            "Tác dụng chậm, đạt đỉnh sau 6-12 giờ"
        ],
        "pharmacokinetics": {
            "half_life": "30-50 giờ (rất dài)",
            "onset": "2-4 giờ",
            "duration": "24 giờ",
            "protein_binding": ">93%",
            "clearance": "Gan (CYP3A4)"
                },
        "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm",
        "black_box_warnings": "Không có black box warning cụ thể. Thận trọng với bệnh nhân suy tim mất bù, hẹp van động mạch chủ nặng. Phù ngoại biên có thể xảy ra và thường không phản ánh suy tim",
        "drug_interactions": {
            "major": [
                {
                    "drug": "Simvastatin, Lovastatin",
                    "mechanism": "Ức chế CYP3A4 chung, tăng nồng độ statin",
                    "effect": "Tăng nguy cơ tiêu cơ vân, tăng men gan",
                    "management": "Giảm liều simvastatin/lovastatin. Theo dõi CK, men gan. Có thể dùng atorvastatin hoặc rosuvastatin thay thế."
                }
            ],
            "moderate": [
                {
                    "drug": "Grapefruit juice",
                    "mechanism": "Ức chế CYP3A4",
                    "effect": "Tăng nồng độ amlodipine, tăng tác dụng phụ",
                    "management": "Tránh uống grapefruit juice. Có thể dùng nước cam thay thế."
                },
                {
                    "drug": "CYP3A4 inhibitors (ketoconazole, itraconazole, erythromycin, clarithromycin)",
                    "mechanism": "Ức chế chuyển hóa amlodipine",
                    "effect": "Tăng nồng độ amlodipine, tăng tác dụng phụ",
                    "management": "Thận trọng. Theo dõi huyết áp, phù chân. Có thể cần giảm liều amlodipine."
                }
            ],
            "minor": [
                {
                    "drug": "Sildenafil, Tadalafil",
                    "mechanism": "Tác dụng hiệp đồng hạ huyết áp",
                    "effect": "Tăng nguy cơ hạ huyết áp",
                    "management": "Thận trọng. Theo dõi huyết áp. Không phải chống chỉ định."
                }
            ]
        },
        "contraindications": {
            "absolute": [
                "Dị ứng amlodipine hoặc dihydropyridine calcium channel blockers",
                "Sốc tim",
                "Suy tim mất bù nặng (NYHA class IV)"
            ],
            "relative": [
                "Hẹp van động mạch chủ nặng - có thể gây suy tim",
                "Suy gan - giảm chuyển hóa, tăng nồng độ",
                "Suy tim nhẹ đến trung bình - thận trọng",
                "Phù ngoại biên - tác dụng phụ thường gặp nhưng không nguy hiểm"
            ]
        },
        "pregnancy_lactation": {
            "fda_category": "C",
            "pregnancy_details": "Có thể dùng khi cần thiết. Nghiên cứu trên động vật cho thấy có thể gây hại cho thai nhi. Không có nghiên cứu đầy đủ trên người. Ưu tiên dùng trong 3 tháng cuối nếu có thể. Theo dõi sát thai nhi.",
            "lactation": {
                "safety": "Compatible",
                "details": "Amlodipine bài tiết vào sữa mẹ ở nồng độ thấp. Nồng độ trong máu trẻ bú mẹ thường rất thấp. Không có báo cáo về tác dụng phụ nghiêm trọng ở trẻ bú mẹ.",
                "recommendation": "Có thể dùng khi cho con bú. Theo dõi trẻ nếu có dấu hiệu bất thường."
            }
        },
        "hepatic_adjustment": {
            "mild": "Không đổi",
            "moderate": "Thận trọng, có thể cần giảm liều (chuyển hóa qua gan)",
            "severe": "Giảm liều 50% (chuyển hóa qua gan CYP3A4)",
            "notes": "Amlodipine chuyển hóa qua gan (CYP3A4). Suy gan có thể làm giảm chuyển hóa, tăng nồng độ và tác dụng phụ. Giảm liều ở suy gan nặng."
        },
        "overdose_management": {
            "symptoms": [
                "Hạ huyết áp nặng",
                "Nhịp tim nhanh phản xạ",
                "Phù ngoại biên",
                "Chóng mặt, ngất",
                "Sốc tim (hiếm)"
            ],
            "antidote": "Không có antidote đặc hiệu. Điều trị hỗ trợ. Calcium (cho block calci)",
            "treatment": [
                "Rửa dạ dày nếu uống trong vòng 1-2 giờ",
                "Than hoạt tính",
                "Điều trị hạ huyết áp: Truyền dịch (normal saline), nâng chân, nếu cần: dopamine, norepinephrine",
                "Calcium gluconate hoặc calcium chloride IV (đối kháng với calcium channel blocker)",
                "Atropine nếu có nhịp tim chậm",
                "Hỗ trợ hô hấp và tuần hoàn nếu cần",
                "Theo dõi ít nhất 24-48 giờ (do half-life rất dài: 30-50 giờ)"
            ],
            "monitoring": "Huyết áp, nhịp tim, ECG, dấu hiệu sống, ý thức"
        },
        "reversal_agents": {
            "available": True,
            "agents": [
                {
                    "name": "Calcium gluconate hoặc Calcium chloride",
                    "mechanism": "Đối kháng với calcium channel blocker bằng cách tăng nồng độ calci ngoại bào",
                    "indication": "Hạ huyết áp nặng, block calci",
                    "dose": "Calcium gluconate 10%: 10-30ml IV, hoặc Calcium chloride 10%: 5-10ml IV"
                }
            ]
        },
        "administration_instructions": {
            "oral": {
                "with_food": "Có thể uống với hoặc không có thức ăn. Không ảnh hưởng đáng kể đến hấp thu.",
                "timing": "Uống 1 lần/ngày (do half-life rất dài: 30-50 giờ). Uống cùng giờ mỗi ngày. Tác dụng chậm, đạt đỉnh sau 6-12 giờ."
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
                "FDA Drug Label - Norvasc (amlodipine)",
                "UpToDate - Amlodipine: Drug information",
                "ALLHAT Study - JAMA",
                "ASCOT Study - The Lancet",
                "American Heart Association/American College of Cardiology guidelines"
            ],
            "last_updated": "2024-12-19",
            "evidence_level": "High - Multiple large RCTs (ALLHAT, ASCOT) and extensive clinical experience"
        }
    },
    "Nifedipine": {
        "group": "Cardiovascular - Calcium Channel Blocker (Dihydropyridine)",
        "vietnamese_name": "Nifedipine, Adalat",
        "administration": ["PO"],
        "indications": [
            "Tăng huyết áp",
            "Đau thắt ngực",
            "Raynaud's phenomenon",
            "Co thắt mạch vành"
        ],
        "contraindications": [
            "Dị ứng",
            "Sốc tim",
            "Suy tim nặng",
            "Hẹp van động mạch chủ nặng"
        ],
        "dosage": {
            "adult_htn_immediate": "10-20mg x 3 lần/ngày",
            "adult_htn_extended": "30-90mg x 1 lần/ngày (XL/retard)",
            "adult_angina": "10-20mg x 3 lần/ngày",
            "notes": "Tránh dùng immediate-release cho tăng huyết áp (nguy cơ hạ HA đột ngột). Ưu tiên extended-release"
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "Không đổi",
            "under_30": "Thận trọng"
        },
        "side_effects": [
            "Phù chân",
            "Đỏ mặt",
            "Nhức đầu",
            "Chóng mặt",
            "Tim đập nhanh (phản ứng)",
            "Hạ huyết áp đột ngột (immediate-release)"
        ],
        "interactions": [
            "Grapefruit juice: tăng nồng độ",
            "Beta-blocker: có thể gây block nhĩ thất",
            "Digoxin: tăng nồng độ digoxin"
        ],
        "pregnancy": "C",
        "mechanism_of_action": "Dihydropyridine calcium channel blocker. Ức chế kênh calci L-type voltage-gated trong màng tế bào cơ trơn mạch máu, ngăn cản dòng calci vào trong tế bào, dẫn đến giãn mạch. Giãn mạch ngoại vi → giảm sức cản mạch máu hệ thống → giảm huyết áp. Giãn mạch vành → tăng tưới máu vành. Ít ảnh hưởng đến tim (không giảm co bóp, không làm chậm nhịp như verapamil/diltiazem). Được dùng trong tăng huyết áp, đau thắt ngực, và co thắt mạch vành.",
        "monitoring": [
            "Huyết áp (theo dõi chặt chẽ khi bắt đầu điều trị)",
            "Nhịp tim (có thể tăng phản xạ do giãn mạch)",
            "Dấu hiệu phù ngoại vi (mắt cá chân, cẳng chân) - tác dụng phụ thường gặp",
            "Đau thắt ngực (nếu dùng cho đau thắt ngực)",
            "Chức năng gan (ALT, AST) - hiếm viêm gan",
            "Dấu hiệu quá liều (hạ huyết áp nặng, nhịp tim nhanh)",
            "Dấu hiệu thiếu máu cục bộ (đau chân khi đi bộ) - hiếm"
        ],
        "precautions": [
            "Dạng tác dụng nhanh (immediate-release) KHÔNG được dùng để điều trị tăng huyết áp hoặc đau thắt ngực (nguy cơ nhồi máu cơ tim, đột quỵ) - chỉ dùng extended-release",
            "Dạng extended-release: không nghiền, không nhai (phá hủy lớp bọc)",
            "Nguy cơ phù ngoại vi (mắt cá chân, cẳng chân) - thường gặp, không nguy hiểm nhưng khó chịu",
            "Có thể gây nhịp tim nhanh phản xạ (do giãn mạch) - thận trọng ở bệnh nhân đau thắt ngực",
            "Hạ huyết áp tư thế đứng - đứng dậy chậm",
            "Thận trọng ở suy gan (giảm chuyển hóa)",
            "Tương tác với nhiều thuốc: tăng nồng độ với CYP3A4 inhibitors (ketoconazole, erythromycin), giảm với inducers",
            "Tránh bưởi chùm (grapefruit) - ức chế CYP3A4 → tăng nồng độ",
            "Không dùng trong hẹp van động mạch chủ nặng (có thể gây suy tim)",
            "Uống với thức ăn hoặc không (tùy dạng)"
        ],
        "pharmacokinetics": {
            "half_life": "2 giờ (immediate-release), 17 giờ (extended-release)",
            "onset": "20 phút (immediate-release), 2-6 giờ (extended-release)",
            "duration": "6-8 giờ (immediate-release), 24 giờ (extended-release)",
            "protein_binding": "92-98%",
            "metabolism": "Gan (CYP3A4) - chuyển hóa mạnh",
            "clearance": "Chủ yếu qua gan, cần điều chỉnh ở suy gan"
        },
        "storage": "Bảo quản ở nhiệt độ phòng (20-25°C), tránh ẩm, tránh ánh sáng. Viên nén extended-release: không nghiền, không nhai.",
        "black_box_warnings": "Dạng immediate-release KHÔNG được dùng để điều trị tăng huyết áp hoặc đau thắt ngực - có thể làm tăng nguy cơ nhồi máu cơ tim và tử vong. Chỉ dùng dạng extended-release cho các chỉ định này.",
        "drug_interactions": {
            "major": [
                {
                    "drug": "Grapefruit juice",
                    "mechanism": "Ức chế CYP3A4, giảm chuyển hóa nifedipine",
                    "effect": "Tăng nồng độ nifedipine đáng kể (có thể tăng 2-3 lần), tăng tác dụng phụ (hạ huyết áp, nhức đầu, phù)",
                    "management": "TRÁNH hoàn toàn bưởi chùm và nước ép bưởi chùm khi dùng nifedipine."
                },
                {
                    "drug": "CYP3A4 inhibitors mạnh (ketoconazole, itraconazole, clarithromycin, erythromycin, ritonavir)",
                    "mechanism": "Ức chế chuyển hóa nifedipine qua CYP3A4",
                    "effect": "Tăng nồng độ nifedipine đáng kể, tăng tác dụng phụ",
                    "management": "Thận trọng. Giảm liều nifedipine. Theo dõi huyết áp, nhịp tim sát. Tránh dùng cùng nếu có thể."
                }
            ],
            "moderate": [
                {
                    "drug": "Beta-blockers",
                    "mechanism": "Tác dụng hiệp đồng giảm nhịp tim, giảm co bóp",
                    "effect": "Tăng nguy cơ block nhĩ thất, suy tim, nhịp tim chậm",
                    "management": "Thận trọng. Theo dõi ECG, nhịp tim. Thường dùng được nhưng cần theo dõi sát."
                },
                {
                    "drug": "Digoxin",
                    "mechanism": "Nifedipine có thể tăng nồng độ digoxin",
                    "effect": "Tăng nguy cơ ngộ độc digoxin",
                    "management": "Theo dõi nồng độ digoxin. Có thể cần giảm liều digoxin."
                },
                {
                    "drug": "CYP3A4 inducers (rifampin, phenytoin, carbamazepine)",
                    "mechanism": "Tăng chuyển hóa nifedipine qua CYP3A4",
                    "effect": "Giảm nồng độ nifedipine, giảm hiệu quả",
                    "management": "Có thể cần tăng liều nifedipine. Theo dõi huyết áp."
                }
            ],
            "minor": [
                {
                    "drug": "Cimetidine",
                    "mechanism": "Có thể ức chế nhẹ chuyển hóa",
                    "effect": "Tăng nhẹ nồng độ nifedipine",
                    "management": "Theo dõi huyết áp."
                }
            ]
        },
        "contraindications": {
            "absolute": [
                "Dị ứng nifedipine hoặc dihydropyridine calcium channel blockers",
                "Sốc tim",
                "Suy tim nặng (EF <30%)",
                "Hẹp van động mạch chủ nặng",
                "Dạng immediate-release cho tăng huyết áp hoặc đau thắt ngực"
            ],
            "relative": [
                "Suy tim trung bình - thận trọng (EF 30-40%)",
                "Suy gan nặng - giảm liều, thận trọng (chuyển hóa qua CYP3A4)",
                "Hẹp van động mạch chủ trung bình - thận trọng",
                "Dùng với beta-blockers - tăng nguy cơ block AV",
                "Dùng với CYP3A4 inhibitors mạnh - tăng nồng độ nifedipine"
            ]
        },
        "pregnancy_lactation": {
            "fda_category": "C",
            "pregnancy_details": "Có thể gây hạ huyết áp, nhịp tim nhanh ở thai nhi. Có thể gây chậm phát triển thai nhi. Cân nhắc lợi ích/nguy cơ. Thường dùng được trong tăng huyết áp thai kỳ nếu lợi ích vượt trội nguy cơ.",
            "lactation": {
                "safety": "Compatible",
                "details": "Nifedipine bài tiết vào sữa mẹ ở nồng độ thấp. Nồng độ trong máu trẻ bú mẹ thường rất thấp. Không có báo cáo về tác dụng phụ nghiêm trọng ở trẻ bú mẹ.",
                "recommendation": "Có thể dùng khi cho con bú. Theo dõi trẻ nếu có dấu hiệu bất thường."
            }
        },
        "hepatic_adjustment": {
            "mild": "Không đổi",
            "moderate": "Thận trọng, giảm liều 25-50% (chuyển hóa qua CYP3A4)",
            "severe": "Thận trọng, giảm liều 50-75% hoặc tránh dùng (chuyển hóa qua CYP3A4)",
            "notes": "Nifedipine chuyển hóa mạnh qua gan (CYP3A4). Suy gan làm giảm chuyển hóa, tăng nồng độ nifedipine. Cần giảm liều ở suy gan."
        },
        "overdose_management": {
            "symptoms": [
                "Hạ huyết áp nặng",
                "Nhịp tim nhanh phản xạ",
                "Chóng mặt, ngất",
                "Suy tim cấp",
                "Phù phổi",
                "Rối loạn nhịp tim"
            ],
            "antidote": "Calcium gluconate hoặc calcium chloride (có thể đảo ngược tác dụng calcium channel blocker)",
            "treatment": [
                "Rửa dạ dày nếu uống trong vòng 1-2 giờ",
                "Than hoạt tính",
                "Điều trị hạ huyết áp: Truyền dịch (normal saline), nâng chân, nếu cần: dopamine, norepinephrine",
                "Calcium gluconate 1-3g IV hoặc calcium chloride 1g IV (có thể đảo ngược tác dụng)",
                "Theo dõi ECG liên tục",
                "Theo dõi huyết áp, nhịp tim, ý thức",
                "Hỗ trợ hô hấp nếu cần",
                "Theo dõi ít nhất 12-24 giờ (do half-life dài với extended-release: 17 giờ)"
            ],
            "monitoring": "ECG liên tục, huyết áp, nhịp tim, ý thức, dấu hiệu suy tim, dấu hiệu suy hô hấp"
        },
        "reversal_agents": {
            "available": True,
            "agents": [
                {
                    "name": "Calcium gluconate / Calcium chloride",
                    "mechanism": "Tăng nồng độ calci trong máu, đảo ngược tác dụng calcium channel blocker",
                    "dose": "Calcium gluconate 1-3g IV hoặc Calcium chloride 1g IV",
                    "indication": "Hạ huyết áp, rối loạn nhịp do quá liều calcium channel blocker"
                }
            ]
        },
        "administration_instructions": {
            "oral": {
                "with_food": "Có thể uống với hoặc không có thức ăn. Dạng extended-release: có thể uống với thức ăn để giảm kích ứng dạ dày.",
                "timing": "Dạng extended-release: uống 1 lần/ngày vào cùng một giờ mỗi ngày. KHÔNG nghiền, KHÔNG nhai viên extended-release (phá hủy lớp bọc, gây phóng thích nhanh nguy hiểm). Dạng immediate-release: KHÔNG dùng cho tăng huyết áp hoặc đau thắt ngực."
            },
            "iv": {
                "reconstitution": "Không có dạng IV",
                "infusion_rate": "Không áp dụng",
                "compatibility": [],
                "incompatibility": [],
                "notes": "Nifedipine chỉ có dạng uống (PO)."
            }
        },
        "references": {
            "primary_sources": [
                "FDA Drug Label - Procardia (nifedipine)",
                "UpToDate - Nifedipine: Drug information",
                "ACCORD Study - New England Journal of Medicine (2010) - Intensive blood pressure control",
                "SPRINT Study - New England Journal of Medicine (2015) - Blood pressure targets",
                "American Heart Association/American College of Cardiology guidelines - Hypertension"
            ],
            "last_updated": "2024-12-19",
            "evidence_level": "High - Multiple large RCTs and extensive clinical experience. Strong warning against immediate-release formulation."
        }
    },
    "Diltiazem": {
        "group": "Cardiovascular - Calcium Channel Blocker (Non-dihydropyridine)",
        "vietnamese_name": "Diltiazem, Cardizem",
        "administration": ["PO", "IV"],
        "indications": [
            "Tăng huyết áp",
            "Đau thắt ngực",
            "Rối loạn nhịp tim trên thất (SVT)",
            "Rung nhĩ",
            "Nhịp nhanh trên thất"
        ],
        "contraindications": [
            "Block nhĩ thất độ 2-3",
            "Suy tim nặng",
            "Sick sinus syndrome",
            "Hạ huyết áp nặng",
            "Hội chứng Wolff-Parkinson-White với rung nhĩ"
        ],
        "dosage": {
            "adult_htn": "120-360mg/ngày chia 1-3 lần",
            "adult_htn_extended": "180-360mg x 1 lần/ngày (CD/XR)",
            "adult_angina": "120-360mg/ngày chia 1-3 lần",
            "adult_svt_iv": "0.25mg/kg IV bolus, có thể lặp 0.35mg/kg sau 15 phút",
            "adult_svt_iv_continuous": "5-15mg/giờ truyền liên tục",
            "notes": "Non-dihydropyridine, có tác dụng ức chế dẫn truyền nhĩ thất"
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "Thận trọng, giảm liều 50%",
            "under_30": "Thận trọng, giảm liều 50%"
        },
        "side_effects": [
            "Nhịp tim chậm",
            "Block nhĩ thất",
            "Chóng mặt",
            "Mệt mỏi",
            "Phù chân (ít hơn dihydropyridine)",
            "Táo bón"
        ],
        "interactions": [
            "Beta-blocker: tăng nguy cơ block nhĩ thất, nhịp chậm",
            "Digoxin: tăng nồng độ digoxin",
            "Simvastatin: tăng nồng độ simvastatin",
            "Cyclosporine: tăng nồng độ cyclosporine"
        ],
        "pregnancy": "C",
        "mechanism_of_action": "Non-dihydropyridine calcium channel blocker (benzothiazepine). Ức chế kênh calci L-type trong cả màng tế bào cơ trơn mạch máu và màng tế bào cơ tim. Giãn mạch ngoại vi → giảm huyết áp. Ức chế dẫn truyền nhĩ thất và làm chậm nhịp tim → giảm nhịp tim. Giảm co bóp cơ tim nhẹ. Giãn mạch vành → tăng tưới máu vành. Được dùng trong tăng huyết áp, đau thắt ngực, rối loạn nhịp trên thất (như rung nhĩ), và kiểm soát nhịp tim.",
        "monitoring": [
            "Huyết áp và nhịp tim",
            "ECG (theo dõi block nhĩ thất, nhịp tim chậm)",
            "Dấu hiệu block nhĩ thất (nhịp tim chậm, chóng mặt, ngất) - đặc biệt quan trọng",
            "Dấu hiệu suy tim (khó thở, phù) - có thể làm nặng suy tim",
            "Chức năng gan (ALT, AST) - hiếm viêm gan",
            "Dấu hiệu quá liều (block nhĩ thất nặng, nhịp tim chậm nặng, hạ huyết áp)"
        ],
        "precautions": [
            "KHÔNG dùng ở block nhĩ thất độ 2-3 hoặc sick sinus syndrome (trừ khi có máy tạo nhịp)",
            "KHÔNG dùng ở suy tim nặng (có thể làm nặng suy tim do giảm co bóp)",
            "Thận trọng ở suy gan (giảm chuyển hóa → tích lũy)",
            "Tương tác với nhiều thuốc: tăng nồng độ với CYP3A4 inhibitors, giảm với inducers",
            "Tránh bưởi chùm (grapefruit) - ức chế CYP3A4 → tăng nồng độ",
            "Tương tác với beta-blockers → tăng nguy cơ block nhĩ thất, nhịp tim chậm",
            "Tương tác với digoxin → tăng nồng độ digoxin (theo dõi nồng độ digoxin)",
            "Giảm liều ở suy gan",
            "Dạng extended-release: không nghiền, không nhai",
            "Uống với thức ăn hoặc không (tùy dạng)"
        ],
        "pharmacokinetics": {
            "half_life": "3-4.5 giờ (immediate-release), 5-10 giờ (extended-release)",
            "onset": "30-60 phút (PO)",
            "duration": "6-8 giờ (immediate-release), 12-24 giờ (extended-release)",
            "protein_binding": "70-80%",
            "metabolism": "Gan (CYP3A4, CYP2D6) - chuyển hóa mạnh",
            "clearance": "Chủ yếu qua gan, cần điều chỉnh ở suy gan"
        },
        "storage": "Bảo quản ở nhiệt độ phòng (20-25°C), tránh ẩm, tránh ánh sáng. Viên nén extended-release: không nghiền, không nhai.",
        "black_box_warnings": "Không có black box warning. Tuy nhiên, block nhĩ thất và nhịp tim chậm có thể nặng, đặc biệt khi dùng với beta-blockers. Suy tim có thể nặng lên. Không dùng ở block nhĩ thất độ 2-3 hoặc sick sinus syndrome (trừ khi có máy tạo nhịp).",
        "drug_interactions": {
            "major": [
                {
                    "drug": "Beta-blockers (atenolol, metoprolol, propranolol, bisoprolol, carvedilol)",
                    "mechanism": "Tác dụng hiệp đồng ức chế dẫn truyền nhĩ thất, giảm nhịp tim, giảm co bóp",
                    "effect": "Tăng nguy cơ block nhĩ thất độ 2-3, nhịp tim chậm nặng, suy tim",
                    "management": "Thận trọng. Theo dõi ECG, nhịp tim, huyết áp sát. Tránh dùng cùng nếu có thể. Nếu cần dùng cùng: giảm liều cả hai, theo dõi sát."
                },
                {
                    "drug": "Grapefruit juice",
                    "mechanism": "Ức chế CYP3A4, giảm chuyển hóa diltiazem",
                    "effect": "Tăng nồng độ diltiazem đáng kể, tăng tác dụng phụ",
                    "management": "TRÁNH hoàn toàn bưởi chùm và nước ép bưởi chùm khi dùng diltiazem."
                },
                {
                    "drug": "CYP3A4 inhibitors mạnh (ketoconazole, itraconazole, clarithromycin, erythromycin, ritonavir)",
                    "mechanism": "Ức chế chuyển hóa diltiazem qua CYP3A4",
                    "effect": "Tăng nồng độ diltiazem đáng kể, tăng tác dụng phụ",
                    "management": "Thận trọng. Giảm liều diltiazem. Theo dõi ECG, nhịp tim, huyết áp sát. Tránh dùng cùng nếu có thể."
                }
            ],
            "moderate": [
                {
                    "drug": "Digoxin",
                    "mechanism": "Diltiazem giảm thải trừ digoxin qua thận, tăng nồng độ digoxin",
                    "effect": "Tăng nồng độ digoxin 20-50%, tăng nguy cơ ngộ độc digoxin",
                    "management": "Theo dõi nồng độ digoxin. Giảm liều digoxin 25-50% khi bắt đầu diltiazem."
                },
                {
                    "drug": "Simvastatin, Lovastatin",
                    "mechanism": "Diltiazem ức chế CYP3A4, tăng nồng độ statin",
                    "effect": "Tăng nồng độ statin, tăng nguy cơ tiêu cơ vân",
                    "management": "Giảm liều simvastatin/lovastatin. Hoặc đổi sang statin không chuyển hóa qua CYP3A4 (pravastatin, rosuvastatin)."
                },
                {
                    "drug": "Cyclosporine, Tacrolimus",
                    "mechanism": "Diltiazem ức chế CYP3A4, tăng nồng độ immunosuppressant",
                    "effect": "Tăng nồng độ cyclosporine/tacrolimus, tăng nguy cơ độc tính",
                    "management": "Theo dõi nồng độ cyclosporine/tacrolimus. Giảm liều nếu cần."
                },
                {
                    "drug": "CYP3A4 inducers (rifampin, phenytoin, carbamazepine)",
                    "mechanism": "Tăng chuyển hóa diltiazem qua CYP3A4",
                    "effect": "Giảm nồng độ diltiazem, giảm hiệu quả",
                    "management": "Có thể cần tăng liều diltiazem. Theo dõi huyết áp, nhịp tim."
                }
            ],
            "minor": [
                {
                    "drug": "Cimetidine",
                    "mechanism": "Có thể ức chế nhẹ chuyển hóa",
                    "effect": "Tăng nhẹ nồng độ diltiazem",
                    "management": "Theo dõi nhịp tim, huyết áp."
                }
            ]
        },
        "contraindications": {
            "absolute": [
                "Block nhĩ thất độ 2-3 không có máy tạo nhịp",
                "Sick sinus syndrome không có máy tạo nhịp",
                "Suy tim nặng (EF <30%)",
                "Hạ huyết áp nặng",
                "Hội chứng Wolff-Parkinson-White với rung nhĩ",
                "Dị ứng diltiazem"
            ],
            "relative": [
                "Suy tim trung bình - thận trọng (EF 30-40%, có thể làm nặng suy tim)",
                "Suy gan nặng - giảm liều 50%, thận trọng (chuyển hóa qua CYP3A4)",
                "Suy thận nặng - giảm liều 50%, thận trọng",
                "Dùng với beta-blockers - tăng nguy cơ block AV đáng kể",
                "Dùng với digoxin - tăng nồng độ digoxin",
                "Dùng với CYP3A4 inhibitors mạnh - tăng nồng độ diltiazem"
            ]
        },
        "pregnancy_lactation": {
            "fda_category": "C",
            "pregnancy_details": "Có thể gây hạ huyết áp, nhịp tim chậm ở thai nhi. Có thể gây chậm phát triển thai nhi, nhịp tim chậm ở trẻ sơ sinh. Cân nhắc lợi ích/nguy cơ. Thường dùng được trong tăng huyết áp thai kỳ hoặc rối loạn nhịp nếu lợi ích vượt trội nguy cơ.",
            "lactation": {
                "safety": "Compatible",
                "details": "Diltiazem bài tiết vào sữa mẹ ở nồng độ thấp. Nồng độ trong máu trẻ bú mẹ thường rất thấp. Không có báo cáo về tác dụng phụ nghiêm trọng ở trẻ bú mẹ.",
                "recommendation": "Có thể dùng khi cho con bú. Theo dõi trẻ nếu có nhịp tim chậm, mệt mỏi."
            }
        },
        "hepatic_adjustment": {
            "mild": "Không đổi",
            "moderate": "Thận trọng, giảm liều 25-50% (chuyển hóa qua CYP3A4, CYP2D6)",
            "severe": "Thận trọng, giảm liều 50% hoặc tránh dùng (chuyển hóa qua CYP3A4, CYP2D6)",
            "notes": "Diltiazem chuyển hóa mạnh qua gan (CYP3A4, CYP2D6). Suy gan làm giảm chuyển hóa, tăng nồng độ diltiazem, tích lũy. Cần giảm liều ở suy gan."
        },
        "overdose_management": {
            "symptoms": [
                "Block nhĩ thất độ 2-3",
                "Nhịp tim chậm nặng (<40 bpm)",
                "Hạ huyết áp nặng",
                "Suy tim cấp",
                "Sick sinus syndrome",
                "Chóng mặt, ngất",
                "Rối loạn nhịp tim"
            ],
            "antidote": "Calcium gluconate hoặc calcium chloride (có thể đảo ngược tác dụng calcium channel blocker), Atropine (cho nhịp tim chậm, block AV)",
            "treatment": [
                "Rửa dạ dày nếu uống trong vòng 1-2 giờ",
                "Than hoạt tính",
                "Điều trị block nhĩ thất/nhịp tim chậm: Atropine 0.5-1mg IV, có thể lặp lại. Nếu không hiệu quả: Calcium gluconate 1-3g IV, Isoproterenol, hoặc máy tạo nhịp tạm thời",
                "Điều trị hạ huyết áp: Truyền dịch (normal saline), nâng chân, Calcium gluconate 1-3g IV, nếu cần: dopamine, norepinephrine",
                "Theo dõi ECG liên tục",
                "Theo dõi huyết áp, nhịp tim, ý thức",
                "Hỗ trợ hô hấp nếu cần",
                "Theo dõi ít nhất 12-24 giờ (do half-life 3-4.5 giờ với immediate-release, 5-10 giờ với extended-release)"
            ],
            "monitoring": "ECG liên tục, huyết áp, nhịp tim, ý thức, dấu hiệu block AV, dấu hiệu suy tim, dấu hiệu suy hô hấp"
        },
        "reversal_agents": {
            "available": True,
            "agents": [
                {
                    "name": "Calcium gluconate / Calcium chloride",
                    "mechanism": "Tăng nồng độ calci trong máu, đảo ngược tác dụng calcium channel blocker",
                    "dose": "Calcium gluconate 1-3g IV hoặc Calcium chloride 1g IV",
                    "indication": "Hạ huyết áp, block AV, rối loạn nhịp do quá liều calcium channel blocker"
                },
                {
                    "name": "Atropine",
                    "mechanism": "Chẹn muscarinic, tăng nhịp tim, cải thiện dẫn truyền AV",
                    "dose": "0.5-1mg IV, có thể lặp lại",
                    "indication": "Nhịp tim chậm, block AV do quá liều diltiazem"
                },
                {
                    "name": "Isoproterenol",
                    "mechanism": "Beta-agonist, tăng nhịp tim, cải thiện dẫn truyền AV",
                    "dose": "Theo protocol",
                    "indication": "Block AV, nhịp tim chậm không đáp ứng với atropine và calcium"
                }
            ]
        },
        "administration_instructions": {
            "oral": {
                "with_food": "Có thể uống với hoặc không có thức ăn. Dạng extended-release: có thể uống với thức ăn để giảm kích ứng dạ dày.",
                "timing": "Dạng immediate-release: uống 3-4 lần/ngày. Dạng extended-release: uống 1-2 lần/ngày vào cùng một giờ mỗi ngày. KHÔNG nghiền, KHÔNG nhai viên extended-release."
            },
            "iv": {
                "reconstitution": "Diltiazem IV: Pha với D5W hoặc normal saline. Nồng độ: 1mg/ml",
                "infusion_rate": "Bolus: 0.25mg/kg trong 2 phút. Có thể lặp lại 0.35mg/kg sau 15 phút nếu cần. Continuous infusion: 5-15mg/giờ, điều chỉnh theo đáp ứng.",
                "compatibility": ["D5W", "Normal saline"],
                "incompatibility": ["Không trộn với các thuốc khác"],
                "notes": "Diltiazem IV dùng cho cấp cứu rối loạn nhịp trên thất (SVT). Theo dõi ECG liên tục. Theo dõi huyết áp, nhịp tim sát. Chống chỉ định trong block AV độ 2-3, sick sinus syndrome."
            }
        },
        "references": {
            "primary_sources": [
                "FDA Drug Label - Cardizem (diltiazem)",
                "UpToDate - Diltiazem: Drug information",
                "American Heart Association/American College of Cardiology guidelines - Atrial fibrillation rate control",
                "American Heart Association/American College of Cardiology guidelines - Hypertension"
            ],
            "last_updated": "2024-12-19",
            "evidence_level": "High - Extensive clinical experience and multiple RCTs in atrial fibrillation rate control and hypertension"
        }
    },
    "Verapamil": {
        "group": "Cardiovascular - Calcium Channel Blocker (Non-dihydropyridine)",
        "vietnamese_name": "Verapamil, Isoptin",
        "administration": ["PO", "IV"],
        "indications": [
            "Tăng huyết áp",
            "Đau thắt ngực",
            "Rối loạn nhịp tim trên thất",
            "Rung nhĩ",
            "Nhịp nhanh trên thất",
            "Migraine phòng ngừa"
        ],
        "contraindications": [
            "Block nhĩ thất độ 2-3",
            "Suy tim nặng",
            "Sick sinus syndrome",
            "Hạ huyết áp nặng",
            "Hội chứng Wolff-Parkinson-White với rung nhĩ"
        ],
        "dosage": {
            "adult_htn": "80-320mg x 2-3 lần/ngày",
            "adult_htn_extended": "120-480mg x 1 lần/ngày (SR)",
            "adult_angina": "80-160mg x 3 lần/ngày",
            "adult_migraine": "80-160mg x 3 lần/ngày",
            "adult_svt_iv": "2.5-5mg IV bolus, có thể lặp 5-10mg sau 15-30 phút",
            "notes": "Mạnh hơn diltiazem trong ức chế dẫn truyền nhĩ thất"
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "Giảm liều 25-50%",
            "under_30": "Giảm liều 50%"
        },
        "side_effects": [
            "Nhịp tim chậm",
            "Block nhĩ thất",
            "Táo bón (thường gặp)",
            "Chóng mặt",
            "Mệt mỏi",
            "Phù chân (ít)"
        ],
        "interactions": [
            "Beta-blocker: tăng nguy cơ block nhĩ thất, suy tim",
            "Digoxin: tăng nồng độ digoxin đáng kể",
            "Simvastatin: tăng nồng độ simvastatin",
            "Theophylline: tăng nồng độ theophylline",
            "Carbamazepine: tăng nồng độ carbamazepine"
        ],
        "pregnancy": "C",
        "mechanism_of_action": "Non-dihydropyridine calcium channel blocker (phenylalkylamine). Ức chế kênh calci L-type trong cả màng tế bào cơ trơn mạch máu và màng tế bào cơ tim. Giãn mạch ngoại vi → giảm huyết áp. Ức chế dẫn truyền nhĩ thất và làm chậm nhịp tim → giảm nhịp tim. Giảm co bóp cơ tim. Giãn mạch vành → tăng tưới máu vành. Được dùng trong tăng huyết áp, đau thắt ngực, rối loạn nhịp trên thất (như rung nhĩ), và migraine. Tương tự diltiazem nhưng mạnh hơn về ức chế co bóp.",
        "monitoring": [
            "Huyết áp và nhịp tim",
            "ECG (theo dõi block nhĩ thất, nhịp tim chậm)",
            "Dấu hiệu block nhĩ thất (nhịp tim chậm, chóng mặt, ngất) - đặc biệt quan trọng",
            "Dấu hiệu suy tim (khó thở, phù) - có thể làm nặng suy tim",
            "Chức năng gan (ALT, AST) - hiếm viêm gan",
            "Dấu hiệu quá liều (block nhĩ thất nặng, nhịp tim chậm nặng, hạ huyết áp)"
        ],
        "precautions": [
            "KHÔNG dùng ở block nhĩ thất độ 2-3 hoặc sick sinus syndrome (trừ khi có máy tạo nhịp)",
            "KHÔNG dùng ở suy tim nặng (có thể làm nặng suy tim do giảm co bóp)",
            "Thận trọng ở suy gan (giảm chuyển hóa → tích lũy)",
            "Tương tác với nhiều thuốc: tăng nồng độ với CYP3A4 inhibitors, giảm với inducers",
            "Tránh bưởi chùm (grapefruit) - ức chế CYP3A4 → tăng nồng độ",
            "Tương tác với beta-blockers → tăng nguy cơ block nhĩ thất, nhịp tim chậm",
            "Tương tác với digoxin → tăng nồng độ digoxin (theo dõi nồng độ digoxin)",
            "Tương tác với statin → tăng nguy cơ tiêu cơ vân",
            "Giảm liều ở suy gan",
            "Dạng extended-release: không nghiền, không nhai",
            "Uống với thức ăn hoặc không (tùy dạng)"
        ],
        "pharmacokinetics": {
            "half_life": "2-7 giờ (immediate-release), 12 giờ (extended-release)",
            "onset": "1-2 giờ (PO)",
            "duration": "6-8 giờ (immediate-release), 24 giờ (extended-release)",
            "protein_binding": "90%",
            "metabolism": "Gan (CYP3A4) - chuyển hóa mạnh",
            "clearance": "Chủ yếu qua gan, cần điều chỉnh ở suy gan"
        },
        "storage": "Bảo quản ở nhiệt độ phòng (20-25°C), tránh ẩm, tránh ánh sáng. Viên nén extended-release: không nghiền, không nhai.",
        "black_box_warnings": "Không có black box warning. Tuy nhiên, block nhĩ thất và nhịp tim chậm có thể nặng, đặc biệt khi dùng với beta-blockers. Suy tim có thể nặng lên. Không dùng ở block nhĩ thất độ 2-3 hoặc sick sinus syndrome (trừ khi có máy tạo nhịp).",
        "drug_interactions": {
            "major": [
                {
                    "drug": "Beta-blockers (atenolol, metoprolol, propranolol, bisoprolol, carvedilol)",
                    "mechanism": "Tác dụng hiệp đồng ức chế dẫn truyền nhĩ thất, giảm nhịp tim, giảm co bóp",
                    "effect": "Tăng nguy cơ block nhĩ thất độ 2-3, nhịp tim chậm nặng, suy tim",
                    "management": "Thận trọng. Theo dõi ECG, nhịp tim, huyết áp sát. Tránh dùng cùng nếu có thể. Nếu cần dùng cùng: giảm liều cả hai, theo dõi sát."
                },
                {
                    "drug": "Grapefruit juice",
                    "mechanism": "Ức chế CYP3A4, giảm chuyển hóa verapamil",
                    "effect": "Tăng nồng độ verapamil đáng kể, tăng tác dụng phụ",
                    "management": "TRÁNH hoàn toàn bưởi chùm và nước ép bưởi chùm khi dùng verapamil."
                },
                {
                    "drug": "CYP3A4 inhibitors mạnh (ketoconazole, itraconazole, clarithromycin, erythromycin, ritonavir)",
                    "mechanism": "Ức chế chuyển hóa verapamil qua CYP3A4",
                    "effect": "Tăng nồng độ verapamil đáng kể, tăng tác dụng phụ",
                    "management": "Thận trọng. Giảm liều verapamil. Theo dõi ECG, nhịp tim, huyết áp sát. Tránh dùng cùng nếu có thể."
                }
            ],
            "moderate": [
                {
                    "drug": "Digoxin",
                    "mechanism": "Verapamil giảm thải trừ digoxin qua thận và tăng hấp thu, tăng nồng độ digoxin",
                    "effect": "Tăng nồng độ digoxin 50-75%, tăng nguy cơ ngộ độc digoxin đáng kể",
                    "management": "Theo dõi nồng độ digoxin. Giảm liều digoxin 50% khi bắt đầu verapamil."
                },
                {
                    "drug": "Simvastatin, Lovastatin",
                    "mechanism": "Verapamil ức chế CYP3A4, tăng nồng độ statin",
                    "effect": "Tăng nồng độ statin, tăng nguy cơ tiêu cơ vân",
                    "management": "Giảm liều simvastatin/lovastatin. Hoặc đổi sang statin không chuyển hóa qua CYP3A4 (pravastatin, rosuvastatin)."
                },
                {
                    "drug": "Carbamazepine, Theophylline",
                    "mechanism": "Verapamil ức chế chuyển hóa, tăng nồng độ",
                    "effect": "Tăng nồng độ carbamazepine/theophylline, tăng nguy cơ độc tính",
                    "management": "Theo dõi nồng độ. Giảm liều nếu cần."
                },
                {
                    "drug": "Cyclosporine, Tacrolimus",
                    "mechanism": "Verapamil ức chế CYP3A4, tăng nồng độ immunosuppressant",
                    "effect": "Tăng nồng độ cyclosporine/tacrolimus, tăng nguy cơ độc tính",
                    "management": "Theo dõi nồng độ cyclosporine/tacrolimus. Giảm liều nếu cần."
                },
                {
                    "drug": "CYP3A4 inducers (rifampin, phenytoin)",
                    "mechanism": "Tăng chuyển hóa verapamil qua CYP3A4",
                    "effect": "Giảm nồng độ verapamil, giảm hiệu quả",
                    "management": "Có thể cần tăng liều verapamil. Theo dõi huyết áp, nhịp tim."
                }
            ],
            "minor": [
                {
                    "drug": "Cimetidine",
                    "mechanism": "Có thể ức chế nhẹ chuyển hóa",
                    "effect": "Tăng nhẹ nồng độ verapamil",
                    "management": "Theo dõi nhịp tim, huyết áp."
                }
            ]
        },
        "contraindications": {
            "absolute": [
                "Block nhĩ thất độ 2-3 không có máy tạo nhịp",
                "Sick sinus syndrome không có máy tạo nhịp",
                "Suy tim nặng (EF <30%)",
                "Hạ huyết áp nặng",
                "Hội chứng Wolff-Parkinson-White với rung nhĩ",
                "Dị ứng verapamil"
            ],
            "relative": [
                "Suy tim trung bình - thận trọng (EF 30-40%, có thể làm nặng suy tim - verapamil mạnh hơn diltiazem về giảm co bóp)",
                "Suy gan nặng - giảm liều 50%, thận trọng (chuyển hóa qua CYP3A4)",
                "Suy thận nặng - giảm liều 50%, thận trọng",
                "Dùng với beta-blockers - tăng nguy cơ block AV đáng kể",
                "Dùng với digoxin - tăng nồng độ digoxin đáng kể (50-75%)",
                "Dùng với CYP3A4 inhibitors mạnh - tăng nồng độ verapamil"
            ]
        },
        "pregnancy_lactation": {
            "fda_category": "C",
            "pregnancy_details": "Có thể gây hạ huyết áp, nhịp tim chậm ở thai nhi. Có thể gây chậm phát triển thai nhi, nhịp tim chậm ở trẻ sơ sinh. Cân nhắc lợi ích/nguy cơ. Thường dùng được trong tăng huyết áp thai kỳ hoặc rối loạn nhịp nếu lợi ích vượt trội nguy cơ.",
            "lactation": {
                "safety": "Compatible",
                "details": "Verapamil bài tiết vào sữa mẹ ở nồng độ thấp. Nồng độ trong máu trẻ bú mẹ thường rất thấp. Không có báo cáo về tác dụng phụ nghiêm trọng ở trẻ bú mẹ.",
                "recommendation": "Có thể dùng khi cho con bú. Theo dõi trẻ nếu có nhịp tim chậm, mệt mỏi."
            }
        },
        "hepatic_adjustment": {
            "mild": "Không đổi",
            "moderate": "Thận trọng, giảm liều 25-50% (chuyển hóa qua CYP3A4)",
            "severe": "Thận trọng, giảm liều 50% hoặc tránh dùng (chuyển hóa qua CYP3A4)",
            "notes": "Verapamil chuyển hóa mạnh qua gan (CYP3A4). Suy gan làm giảm chuyển hóa, tăng nồng độ verapamil, tích lũy. Cần giảm liều ở suy gan."
        },
        "overdose_management": {
            "symptoms": [
                "Block nhĩ thất độ 2-3",
                "Nhịp tim chậm nặng (<40 bpm)",
                "Hạ huyết áp nặng",
                "Suy tim cấp",
                "Sick sinus syndrome",
                "Chóng mặt, ngất",
                "Rối loạn nhịp tim"
            ],
            "antidote": "Calcium gluconate hoặc calcium chloride (có thể đảo ngược tác dụng calcium channel blocker), Atropine (cho nhịp tim chậm, block AV)",
            "treatment": [
                "Rửa dạ dày nếu uống trong vòng 1-2 giờ",
                "Than hoạt tính",
                "Điều trị block nhĩ thất/nhịp tim chậm: Atropine 0.5-1mg IV, có thể lặp lại. Nếu không hiệu quả: Calcium gluconate 1-3g IV, Isoproterenol, hoặc máy tạo nhịp tạm thời",
                "Điều trị hạ huyết áp: Truyền dịch (normal saline), nâng chân, Calcium gluconate 1-3g IV, nếu cần: dopamine, norepinephrine",
                "Theo dõi ECG liên tục",
                "Theo dõi huyết áp, nhịp tim, ý thức",
                "Hỗ trợ hô hấp nếu cần",
                "Theo dõi ít nhất 12-24 giờ (do half-life 2-7 giờ với immediate-release, 12 giờ với extended-release)"
            ],
            "monitoring": "ECG liên tục, huyết áp, nhịp tim, ý thức, dấu hiệu block AV, dấu hiệu suy tim, dấu hiệu suy hô hấp"
        },
        "reversal_agents": {
            "available": True,
            "agents": [
                {
                    "name": "Calcium gluconate / Calcium chloride",
                    "mechanism": "Tăng nồng độ calci trong máu, đảo ngược tác dụng calcium channel blocker",
                    "dose": "Calcium gluconate 1-3g IV hoặc Calcium chloride 1g IV",
                    "indication": "Hạ huyết áp, block AV, rối loạn nhịp do quá liều calcium channel blocker"
                },
                {
                    "name": "Atropine",
                    "mechanism": "Chẹn muscarinic, tăng nhịp tim, cải thiện dẫn truyền AV",
                    "dose": "0.5-1mg IV, có thể lặp lại",
                    "indication": "Nhịp tim chậm, block AV do quá liều verapamil"
                },
                {
                    "name": "Isoproterenol",
                    "mechanism": "Beta-agonist, tăng nhịp tim, cải thiện dẫn truyền AV",
                    "dose": "Theo protocol",
                    "indication": "Block AV, nhịp tim chậm không đáp ứng với atropine và calcium"
                }
            ]
        },
        "administration_instructions": {
            "oral": {
                "with_food": "Có thể uống với hoặc không có thức ăn. Dạng extended-release: có thể uống với thức ăn để giảm kích ứng dạ dày.",
                "timing": "Dạng immediate-release: uống 2-3 lần/ngày. Dạng extended-release: uống 1 lần/ngày vào cùng một giờ mỗi ngày. KHÔNG nghiền, KHÔNG nhai viên extended-release."
            },
            "iv": {
                "reconstitution": "Verapamil IV: Pha với D5W hoặc normal saline. Nồng độ: 0.25mg/ml",
                "infusion_rate": "Bolus: 2.5-5mg trong 2 phút. Có thể lặp lại 5-10mg sau 15-30 phút nếu cần. Tối đa 20mg.",
                "compatibility": ["D5W", "Normal saline"],
                "incompatibility": ["Không trộn với các thuốc khác"],
                "notes": "Verapamil IV dùng cho cấp cứu rối loạn nhịp trên thất (SVT). Theo dõi ECG liên tục. Theo dõi huyết áp, nhịp tim sát. Chống chỉ định trong block AV độ 2-3, sick sinus syndrome. Verapamil mạnh hơn diltiazem về ức chế dẫn truyền AV."
            }
        },
        "references": {
            "primary_sources": [
                "FDA Drug Label - Calan (verapamil)",
                "UpToDate - Verapamil: Drug information",
                "American Heart Association/American College of Cardiology guidelines - Atrial fibrillation rate control",
                "American Heart Association/American College of Cardiology guidelines - Hypertension"
            ],
            "last_updated": "2024-12-19",
            "evidence_level": "High - Extensive clinical experience and multiple RCTs in atrial fibrillation rate control and hypertension"
        }
    },
    "Isosorbide mononitrate": {
        "group": "Cardiovascular - Nitrate",
        "vietnamese_name": "Isosorbide mononitrate, Imdur",
        "administration": ["PO"],
        "indications": [
            "Đau thắt ngực (phòng ngừa)",
            "Suy tim (giảm tiền gánh)",
            "Đau thắt ngực ổn định"
        ],
        "contraindications": [
            "Dị ứng nitrate",
            "Hạ huyết áp nặng",
            "Shock",
            "Dùng sildenafil/tadalafil/vardenafil (trong 24-48h)",
            "Tăng áp lực nội sọ",
            "Thiếu máu nặng"
        ],
        "dosage": {
            "adult_angina_immediate": "10-20mg x 2-3 lần/ngày",
            "adult_angina_extended": "30-120mg x 1 lần/ngày (buổi sáng)",
            "adult_heart_failure": "10-40mg x 2-3 lần/ngày",
            "notes": "Tolerance với nitrate nếu dùng liên tục. Cần khoảng nghỉ nitrate-free 10-14h mỗi ngày"
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "Không đổi",
            "under_30": "Không đổi"
        },
        "side_effects": [
            "Nhức đầu (thường gặp, giảm sau vài ngày)",
            "Hạ huyết áp",
            "Chóng mặt",
            "Đỏ mặt",
            "Nhịp tim nhanh phản ứng",
            "Ngất (hiếm)"
        ],
        "interactions": [
            "Sildenafil/Tadalafil/Vardenafil: hạ huyết áp nguy hiểm - chống chỉ định",
            "Rượu: tăng tác dụng hạ huyết áp",
            "Thuốc hạ huyết áp khác: tăng tác dụng"
        ],
        "pregnancy": "C",
        "mechanism_of_action": "Isosorbide mononitrate là thuốc nitrate, được chuyển hóa thành nitric oxide (NO) trong tế bào cơ trơn mạch máu. NO kích hoạt guanylate cyclase, làm tăng cGMP (cyclic guanosine monophosphate), dẫn đến thư giãn cơ trơn mạch máu. Isosorbide mononitrate chủ yếu giãn tĩnh mạch (giảm tiền gánh), giảm áp lực đổ đầy thất trái, giảm thể tích tâm thất, và giảm nhu cầu oxy của cơ tim. Giãn động mạch nhẹ (giảm hậu gánh) cũng xảy ra. Kết quả: giảm đau thắt ngực, giảm triệu chứng suy tim, và cải thiện khả năng gắng sức. Isosorbide mononitrate là dẫn xuất mononitrate của isosorbide dinitrate, có thời gian bán thải dài hơn và ít tolerance hơn. Tuy nhiên, tolerance với nitrate vẫn xảy ra nếu dùng liên tục, cần khoảng nghỉ nitrate-free 10-14 giờ mỗi ngày.",
        "monitoring": [
            "Huyết áp - hạ huyết áp là tác dụng phụ phổ biến, đặc biệt khi đứng (hạ huyết áp tư thế)",
            "Nhịp tim - nhịp tim nhanh phản ứng có thể xảy ra (do hạ huyết áp)",
            "Triệu chứng đau thắt ngực - đánh giá hiệu quả phòng ngừa",
            "Triệu chứng suy tim - đánh giá hiệu quả giảm tiền gánh",
            "Nhức đầu - tác dụng phụ phổ biến nhất, thường giảm sau vài ngày",
            "Dấu hiệu tolerance - giảm hiệu quả sau vài tuần dùng liên tục (cần khoảng nghỉ nitrate-free)",
            "Tương tác với sildenafil, tadalafil, vardenafil (chống chỉ định - hạ huyết áp nguy hiểm)"
        ],
        "precautions": [
            "CHỐNG CHỈ ĐỊNH với sildenafil, tadalafil, vardenafil trong 24-48 giờ - hạ huyết áp nguy hiểm, có thể gây tử vong",
            "Tolerance với nitrate - nếu dùng liên tục, hiệu quả giảm sau vài tuần, cần khoảng nghỉ nitrate-free 10-14 giờ mỗi ngày",
            "Dạng extended release - dùng 1 lần/ngày vào buổi sáng để có khoảng nghỉ nitrate-free tự nhiên",
            "Dạng immediate release - dùng 2-3 lần/ngày, đảm bảo khoảng nghỉ 10-14 giờ giữa các liều cuối và liều đầu ngày hôm sau",
            "Hạ huyết áp - phổ biến, đặc biệt khi đứng (hạ huyết áp tư thế), tránh đứng dậy đột ngột",
            "Nhức đầu - tác dụng phụ phổ biến nhất, thường tự khỏi sau vài ngày, có thể dùng acetaminophen",
            "Không dùng nếu hạ huyết áp nặng, shock, tăng áp lực nội sọ, thiếu máu nặng",
            "Tránh rượu - tăng tác dụng hạ huyết áp",
            "Thận trọng khi dùng với các thuốc hạ huyết áp khác (tăng tác dụng)",
            "Ngừng đột ngột - có thể gây rebound angina (tăng nguy cơ đau thắt ngực), giảm liều dần dần",
            "Dùng với thức ăn hoặc không (không ảnh hưởng hấp thu)",
            "Không nghiền hoặc nhai dạng extended release (phải uống nguyên viên)"
        ],
        "pharmacokinetics": {
            "half_life": "4-5 giờ (immediate release), 8-10 giờ (extended release)",
            "onset": "15-30 phút (immediate release), 30-60 phút (extended release)",
            "duration": "6-8 giờ (immediate release), 12-24 giờ (extended release)",
            "protein_binding": "<5%",
            "clearance": "Gan: chuyển hóa thành isosorbide và các metabolites không hoạt động. Thận: bài tiết một phần metabolites. Không cần điều chỉnh liều ở suy thận hoặc suy gan."
        },
        "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm, tránh ánh sáng. Viên nén: bảo quản trong bao bì kín. Dạng extended release: bảo quản tương tự, không nghiền hoặc nhai.",
        "black_box_warnings": "CHỐNG CHỈ ĐỊNH với sildenafil, tadalafil, vardenafil trong 24-48 giờ. Kết hợp có thể gây hạ huyết áp nghiêm trọng, có thể gây tử vong. Nguy cơ hạ huyết áp nặng, ngất, nhồi máu cơ tim, đột quỵ."
    },
    # Diuretics
    "Furosemide": {
        "group": "Cardiovascular - Loop Diuretic",
        "vietnamese_name": "Furosemide, Lasix",
        "administration": ["PO", "IV", "IM"],
        "indications": [
            "Phù (suy tim, xơ gan, suy thận)",
            "Tăng huyết áp",
            "Suy tim cấp",
            "Tăng kali máu"
        ],
        "contraindications": [
            "Vô niệu",
            "Mất nước nặng",
            "Hạ kali máu nặng",
            "Dị ứng sulfonamide"
        ],
        "dosage": {
            "adult_po": "20-80mg x 1-2 lần/ngày",
            "adult_iv": "20-80mg IV (có thể lặp lại)",
            "adult_iv_continuous": "5-40mg/giờ truyền liên tục",
            "heart_failure_acute": "20-40mg IV, có thể lặp lại",
            "notes": "Theo dõi cân bằng dịch, điện giải"
        },
        "side_effects": [
            "Hạ kali máu",
            "Hạ natri máu",
            "Mất nước",
            "Tăng acid uric",
            "Điếc tạm thời (IV liều cao)",
            "Tăng đường huyết"
        ],
        "interactions": [
            "Digoxin: tăng nguy cơ ngộ độc digoxin (hạ kali)",
            "Aminoglycosides: tăng độc tính thính giác",
            "NSAID: giảm hiệu quả",
            "Lithium: tăng nồng độ lithium"
        ],
        "pregnancy": "C",
        "mechanism_of_action": "Ức chế đồng vận chuyển Na-K-2Cl ở quai Henle, tăng thải natri, kali, clo, và nước",
        "monitoring": [
            "Điện giải (K, Na, Cl) trước điều trị và định kỳ",
            "Cân bằng dịch vào-ra, cân nặng",
            "Creatinine, BUN",
            "Acid uric nếu dùng lâu dài",
            "Thính giác nếu IV liều cao hoặc suy thận"
        ],
        "precautions": [
            "Theo dõi sát điện giải, đặc biệt kali",
            "Bù kali nếu cần",
            "Tránh dùng quá liều (gây mất nước, suy thận)",
            "Thận trọng với bệnh nhân suy thận (có thể cần liều cao hơn)",
            "Tránh dùng IV liều cao ở bệnh nhân suy thận (nguy cơ điếc)"
        ],
        "pharmacokinetics": {
            "half_life": "2 giờ (PO), 1 giờ (IV)",
            "onset": "30-60 phút (PO), 5 phút (IV)",
            "duration": "6-8 giờ",
            "protein_binding": ">98%",
            "clearance": "Thận (50%) và gan"
                },
        "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ánh sáng",
        "black_box_warnings": "Có thể gây mất nước và rối loạn điện giải nghiêm trọng. Điếc có thể xảy ra với liều IV cao hoặc dùng nhanh. Hạ kali máu có thể làm tăng nguy cơ ngộ độc digoxin và rối loạn nhịp tim",
        "drug_interactions": {
            "major": [
                {
                    "drug": "Digoxin",
                    "mechanism": "Furosemide gây hạ kali máu, tăng nguy cơ ngộ độc digoxin",
                    "effect": "Tăng nguy cơ ngộ độc digoxin (nhịp tim chậm, block AV, rối loạn nhịp tim)",
                    "management": "Theo dõi kali máu thường xuyên. Bù kali nếu cần. Theo dõi nồng độ digoxin. Theo dõi ECG."
                },
                {
                    "drug": "Aminoglycosides (gentamicin, tobramycin, amikacin)",
                    "mechanism": "Cả hai đều gây độc tính thính giác, tác dụng hiệp đồng",
                    "effect": "Tăng nguy cơ điếc vĩnh viễn, đặc biệt với furosemide IV liều cao",
                    "management": "Thận trọng. Tránh dùng furosemide IV liều cao cùng aminoglycosides. Theo dõi thính giác nếu cần dùng cùng."
                },
                {
                    "drug": "Lithium",
                    "mechanism": "Furosemide giảm thải trừ lithium qua thận (do giảm thể tích máu), tăng nồng độ lithium",
                    "effect": "Tăng nồng độ lithium, tăng nguy cơ độc tính lithium",
                    "management": "Theo dõi nồng độ lithium. Có thể cần giảm liều lithium. Theo dõi dấu hiệu độc tính lithium."
                }
            ],
            "moderate": [
                {
                    "drug": "NSAIDs (ibuprofen, naproxen, diclofenac, indomethacin)",
                    "mechanism": "NSAID giảm tác dụng lợi tiểu của furosemide (do giảm prostaglandin, giảm lưu lượng máu thận)",
                    "effect": "Giảm hiệu quả lợi tiểu, giảm hạ huyết áp",
                    "management": "Thận trọng. Theo dõi đáp ứng lợi tiểu. Có thể cần tăng liều furosemide. Tránh dùng lâu dài cùng."
                },
                {
                    "drug": "ACE inhibitors, ARBs",
                    "mechanism": "Tác dụng hiệp đồng hạ huyết áp, tăng nguy cơ hạ huyết áp quá mức",
                    "effect": "Tăng nguy cơ hạ huyết áp, suy thận cấp",
                    "management": "Thận trọng khi bắt đầu. Có thể cần giảm liều furosemide hoặc ACE inhibitor. Theo dõi huyết áp, chức năng thận."
                },
                {
                    "drug": "Corticosteroids",
                    "mechanism": "Corticosteroid gây giữ natri, giảm hiệu quả lợi tiểu",
                    "effect": "Giảm hiệu quả lợi tiểu",
                    "management": "Theo dõi đáp ứng lợi tiểu. Có thể cần tăng liều furosemide."
                }
            ],
            "minor": [
                {
                    "drug": "Probenecid",
                    "mechanism": "Probenecid ức chế bài tiết furosemide qua thận",
                    "effect": "Giảm hiệu quả lợi tiểu",
                    "management": "Có thể cần tăng liều furosemide."
                }
            ]
        },
        "contraindications": {
            "absolute": [
                "Vô niệu",
                "Mất nước nặng",
                "Hạ kali máu nặng",
                "Dị ứng sulfonamide",
                "Dị ứng furosemide"
            ],
            "relative": [
                "Suy thận nặng - có thể cần liều cao hơn (nhưng thận trọng với IV liều cao - nguy cơ điếc)",
                "Suy gan nặng - thận trọng (thải một phần qua gan)",
                "Hạ natri máu - điều chỉnh trước khi dùng",
                "Hạ magie máu - bù magie trước khi dùng",
                "Dùng với digoxin - tăng nguy cơ ngộ độc digoxin",
                "Dùng với aminoglycosides - tăng nguy cơ điếc",
                "Dùng với lithium - tăng nồng độ lithium"
            ]
        },
        "pregnancy_lactation": {
            "fda_category": "C",
            "pregnancy_details": "Có thể gây giảm thể tích máu, giảm tưới máu nhau thai. Có thể gây giảm nước ối, thiếu máu thai nhi. Cân nhắc lợi ích/nguy cơ. Thường dùng được trong suy tim thai kỳ hoặc phù nếu lợi ích vượt trội nguy cơ.",
            "lactation": {
                "safety": "Compatible",
                "details": "Furosemide bài tiết vào sữa mẹ ở nồng độ thấp. Nồng độ trong máu trẻ bú mẹ thường rất thấp. Không có báo cáo về tác dụng phụ nghiêm trọng ở trẻ bú mẹ.",
                "recommendation": "Có thể dùng khi cho con bú. Theo dõi trẻ nếu có dấu hiệu mất nước, rối loạn điện giải."
            }
        },
        "hepatic_adjustment": {
            "mild": "Không đổi",
            "moderate": "Thận trọng (thải một phần qua gan)",
            "severe": "Thận trọng (thải một phần qua gan)",
            "notes": "Furosemide thải qua cả thận (50%) và gan (50%). Suy gan có thể ảnh hưởng một phần đến dược động học nhưng thường không cần điều chỉnh liều đáng kể."
        },
        "overdose_management": {
            "symptoms": [
                "Mất nước nặng",
                "Hạ kali máu nặng (yếu cơ, rối loạn nhịp tim)",
                "Hạ natri máu nặng (lú lẫn, co giật)",
                "Hạ magie máu",
                "Hạ canxi máu",
                "Suy thận cấp (do mất nước)",
                "Điếc (với IV liều cao)",
                "Hạ huyết áp"
            ],
            "antidote": "Không có antidote đặc hiệu. Điều trị hỗ trợ: bù dịch, điện giải",
            "treatment": [
                "Rửa dạ dày nếu uống trong vòng 1-2 giờ",
                "Than hoạt tính",
                "Bù dịch: Truyền normal saline hoặc lactated Ringer's để bù mất nước",
                "Bù điện giải: Kali chloride (nếu hạ kali máu), Magie sulfate (nếu hạ magie máu), Calcium (nếu hạ canxi máu)",
                "Theo dõi điện giải thường xuyên (K, Na, Mg, Ca, Cl)",
                "Theo dõi chức năng thận (creatinine, BUN, nước tiểu)",
                "Theo dõi huyết áp, nhịp tim, ECG",
                "Nếu có điếc (với IV): Ngừng ngay, có thể không hồi phục",
                "Theo dõi ít nhất 12-24 giờ"
            ],
            "monitoring": "Điện giải (K, Na, Mg, Ca, Cl), chức năng thận (creatinine, BUN, nước tiểu), huyết áp, nhịp tim, ECG, cân bằng dịch, thính giác (nếu IV liều cao)"
        },
        "reversal_agents": {
            "available": False,
            "agents": []
        },
        "administration_instructions": {
            "oral": {
                "with_food": "Có thể uống với hoặc không có thức ăn. Uống với thức ăn có thể giảm kích ứng dạ dày.",
                "timing": "Uống 1-2 lần/ngày (sáng và chiều). Uống buổi sáng để tránh đi tiểu đêm. Theo dõi cân bằng dịch, cân nặng."
            },
            "iv": {
                "reconstitution": "Furosemide IV: Pha với D5W hoặc normal saline. Nồng độ: 10mg/ml. KHÔNG pha với các dung dịch có pH <5.5 (kết tủa).",
                "infusion_rate": "Bolus: 20-80mg IV qua 1-2 phút. Có thể lặp lại mỗi 2 giờ nếu cần. Continuous infusion: 5-40mg/giờ, điều chỉnh theo đáp ứng. KHÔNG truyền quá nhanh (nguy cơ điếc).",
                "compatibility": ["D5W", "Normal saline", "Lactated Ringer's"],
                "incompatibility": ["Không trộn với các thuốc khác (pH <5.5 gây kết tủa)"],
                "notes": "Furosemide IV dùng cho suy tim cấp, phù nặng. Theo dõi điện giải, cân bằng dịch sát. KHÔNG truyền quá nhanh (nguy cơ điếc). Thận trọng ở suy thận (có thể cần liều cao nhưng tránh tốc độ cao - nguy cơ điếc)."
            }
        },
        "references": {
            "primary_sources": [
                "FDA Drug Label - Lasix (furosemide)",
                "UpToDate - Furosemide: Drug information",
                "DOSE Study - New England Journal of Medicine (2011) - Furosemide trong suy tim cấp",
                "American Heart Association/American College of Cardiology guidelines - Heart failure"
            ],
            "last_updated": "2024-12-19",
            "evidence_level": "High - Extensive clinical experience and RCTs (DOSE study) in acute heart failure"
        }
    },
    "Hydrochlorothiazide": {
        "group": "Cardiovascular - Thiazide Diuretic",
        "vietnamese_name": "Hydrochlorothiazide, HCTZ",
        "administration": ["PO"],
        "indications": [
            "Tăng huyết áp",
            "Phù (suy tim nhẹ)",
            "Sỏi thận canxi"
        ],
        "contraindications": [
            "Dị ứng sulfonamide",
            "Vô niệu",
            "Hạ kali máu nặng"
        ],
        "dosage": {
            "adult_htn": "12.5-50mg x 1 lần/ngày",
            "adult_edema": "25-100mg x 1-2 lần/ngày",
            "notes": "Liều thấp (12.5-25mg) đủ cho tăng huyết áp"
        },
        "side_effects": [
            "Hạ kali máu",
            "Hạ natri máu",
            "Tăng đường huyết",
            "Tăng acid uric",
            "Tăng cholesterol"
        ],
                  "interactions": [
              "Digoxin: tăng nguy cơ ngộ độc digoxin",
              "Lithium: tăng nồng độ lithium",
              "NSAID: giảm hiệu quả"
          ],
          "pregnancy": "C",
          "mechanism_of_action": "Thiazide diuretic. Ức chế Na+/Cl- cotransporter ở đoạn xa của ống thận (distal convoluted tubule), tăng bài tiết Na+, Cl-, và nước, gây lợi tiểu. Giảm thể tích máu và giảm huyết áp. Tăng bài tiết K+, Mg2+, nhưng giữ lại Ca2+ (khác với loop diuretics).",
          "monitoring": [
              "Kali máu (mỗi 1-3 tháng, đặc biệt khi bắt đầu) - HCTZ gây hạ kali máu",
              "Natri máu - có thể gây hạ natri máu, đặc biệt ở người già",
              "Creatinine, BUN - có thể tăng nhẹ (không phải suy thận thật)",
              "Đường huyết - có thể tăng đường huyết, đặc biệt ở bệnh nhân đái tháo đường",
              "Acid uric - HCTZ gây tăng acid uric, có thể gây gout",
              "Lipid máu - có thể tăng cholesterol, triglycerides nhẹ",
              "Canxi máu - HCTZ có thể gây tăng canxi máu nhẹ (do giữ lại Ca2+)"
          ],
          "precautions": [
              "Liều thấp (12.5-25mg/ngày) đủ cho tăng huyết áp, ít tác dụng phụ hơn liều cao",
              "Thường cần bổ sung kali hoặc dùng với kali-sparing diuretic (spironolactone, amiloride)",
              "Thận trọng ở người già (tăng nguy cơ hạ natri máu)",
              "Thận trọng ở bệnh nhân đái tháo đường (tăng đường huyết)",
              "Thận trọng ở bệnh nhân gout (tăng acid uric)",
              "Tránh dùng với lithium (tăng nguy cơ độc tính lithium)",
              "Dị ứng sulfonamide - không dùng nếu dị ứng"
          ],
          "pharmacokinetics": {
              "half_life": "6-15 giờ",
              "onset": "2 giờ (PO)",
              "duration": "6-12 giờ",
              "protein_binding": "40-70%",
              "clearance": "Thận (không chuyển hóa, thải nguyên dạng)"
          },
          "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm, tránh ánh sáng",
          "black_box_warnings": "",
          "drug_interactions": {
              "major": [
                  {
                      "drug": "Lithium",
                      "mechanism": "HCTZ làm giảm thải trừ lithium qua thận",
                      "effect": "Tăng nồng độ lithium trong máu, tăng nguy cơ độc tính lithium (buồn nôn, run, lú lẫn, co giật)",
                      "management": "TRÁNH DÙNG CHUNG. Nếu bắt buộc: giảm liều lithium 50%, theo dõi nồng độ lithium chặt chẽ, bổ sung kali."
                  },
                  {
                      "drug": "Digoxin",
                      "mechanism": "HCTZ gây hạ kali máu, tăng độc tính digoxin",
                      "effect": "Tăng nguy cơ ngộ độc digoxin (rối loạn nhịp, block AV)",
                      "management": "Theo dõi kali máu chặt chẽ, duy trì kali >4.0 mEq/L. Theo dõi nồng độ digoxin. Cân nhắc dùng kali-sparing diuretic."
                  }
              ],
              "moderate": [
                  {
                      "drug": "NSAIDs (ibuprofen, naproxen, indomethacin)",
                      "mechanism": "NSAIDs giảm tác dụng lợi tiểu và hạ huyết áp của HCTZ, có thể gây suy thận",
                      "effect": "Giảm hiệu quả hạ huyết áp, tăng nguy cơ suy thận cấp",
                      "management": "Thận trọng. Theo dõi huyết áp, chức năng thận. Tránh dùng lâu dài cùng."
                  },
                  {
                      "drug": "Corticosteroids (prednisone, hydrocortisone)",
                      "mechanism": "Corticosteroids gây giữ natri, giảm kali (tương tự HCTZ)",
                      "effect": "Tăng nguy cơ hạ kali máu nặng",
                      "management": "Bổ sung kali. Theo dõi kali máu thường xuyên."
                  },
                  {
                      "drug": "ACE inhibitors, ARBs",
                      "mechanism": "Tác dụng hiệp đồng hạ huyết áp, tăng nguy cơ hạ kali máu (với ACE/ARB) hoặc tăng kali máu (ít gặp)",
                      "effect": "Tăng nguy cơ hạ huyết áp quá mức, tăng kali máu (hiếm)",
                      "management": "Theo dõi huyết áp khi bắt đầu. Theo dõi kali máu định kỳ."
                  },
                  {
                      "drug": "Insulin, các thuốc hạ đường huyết",
                      "mechanism": "HCTZ có thể tăng đường huyết",
                      "effect": "Có thể cần tăng liều insulin hoặc thuốc hạ đường huyết",
                      "management": "Theo dõi đường huyết. Có thể cần điều chỉnh liều thuốc đái tháo đường."
                  }
              ],
              "minor": [
                  {
                      "drug": "Cholestyramine, colestipol",
                      "mechanism": "Giảm hấp thu HCTZ",
                      "effect": "Giảm hiệu quả HCTZ",
                      "management": "Dùng HCTZ ít nhất 2 giờ trước hoặc sau các thuốc này."
                  },
                  {
                      "drug": "Allopurinol",
                      "mechanism": "Tăng nguy cơ phản ứng dị ứng (hiếm)",
                      "effect": "Tăng nguy cơ phản ứng dị ứng",
                      "management": "Thận trọng. Theo dõi dấu hiệu dị ứng."
                  }
              ]
          },
          "contraindications": {
              "absolute": [
                  "Dị ứng sulfonamide (phản ứng nghiêm trọng)",
                  "Vô niệu (không có nước tiểu)",
                  "Hạ kali máu nặng không kiểm soát được"
              ],
              "relative": [
                  "Suy thận nặng (eGFR <30 ml/min/1.73m²) - kém hiệu quả",
                  "Suy gan nặng (tăng nguy cơ hạ natri máu)",
                  "Bệnh gout (tăng acid uric)",
                  "Đái tháo đường (tăng đường huyết)",
                  "Lupus ban đỏ hệ thống (có thể làm nặng)",
                  "Đang dùng lithium (tăng nồng độ lithium nguy hiểm)"
              ]
          },
          "pregnancy_lactation": {
              "fda_category": "C",
              "pregnancy_details": "HCTZ có thể gây giảm thể tích máu, giảm tưới máu nhau thai, giảm nước ối. Có thể gây giảm cân nặng thai nhi, thiếu máu thai nhi. Cân nhắc lợi ích/nguy cơ. Thường dùng được trong tăng huyết áp thai kỳ nếu lợi ích vượt trội nguy cơ. Tránh dùng trong 3 tháng đầu nếu có thể.",
              "lactation": {
                  "safety": "Compatible",
                  "details": "HCTZ bài tiết vào sữa mẹ ở nồng độ thấp. Nồng độ trong máu trẻ bú mẹ thường rất thấp. Không có báo cáo về tác dụng phụ nghiêm trọng ở trẻ bú mẹ.",
                  "recommendation": "Có thể dùng khi cho con bú. Theo dõi trẻ nếu có dấu hiệu mất nước, rối loạn điện giải."
              }
          },
          "hepatic_adjustment": {
              "mild": "Không đổi",
              "moderate": "Thận trọng (tăng nguy cơ hạ natri máu)",
              "severe": "Thận trọng, có thể tránh dùng (tăng nguy cơ hạ natri máu, giữ natri)",
              "notes": "HCTZ thải qua thận, không chuyển hóa qua gan. Tuy nhiên, suy gan có thể gây giữ natri, tăng nguy cơ hạ natri máu khi dùng HCTZ. Thận trọng ở bệnh nhân suy gan."
          },
          "overdose_management": {
              "symptoms": [
                  "Mất nước nặng",
                  "Hạ kali máu nặng (yếu cơ, rối loạn nhịp tim, có thể gây tử vong)",
                  "Hạ natri máu nặng (lú lẫn, co giật, hôn mê)",
                  "Hạ magie máu",
                  "Hạ huyết áp nặng",
                  "Suy thận cấp (do mất nước)",
                  "Rối loạn nhịp tim (do hạ kali máu)"
              ],
              "antidote": "Không có antidote đặc hiệu. Điều trị hỗ trợ: bù dịch, điện giải",
              "treatment": [
                  "Rửa dạ dày nếu uống trong vòng 1-2 giờ",
                  "Than hoạt tính",
                  "Bù dịch: Truyền normal saline hoặc lactated Ringer's để bù mất nước",
                  "Bù điện giải: Kali chloride (nếu hạ kali máu nặng - cần truyền IV), Magie sulfate (nếu hạ magie máu)",
                  "Điều trị hạ natri máu: Nếu nặng và có triệu chứng thần kinh: Sodium chloride 3% IV (thận trọng, từ từ)",
                  "Theo dõi điện giải thường xuyên (K, Na, Mg, Cl)",
                  "Theo dõi chức năng thận (creatinine, BUN, nước tiểu)",
                  "Theo dõi huyết áp, nhịp tim, ECG",
                  "Theo dõi ít nhất 12-24 giờ"
              ],
              "monitoring": "Điện giải (K, Na, Mg, Cl), chức năng thận (creatinine, BUN, nước tiểu), huyết áp, nhịp tim, ECG, cân bằng dịch, ý thức"
          },
          "reversal_agents": {
              "available": False,
              "agents": []
          },
          "administration_instructions": {
              "oral": {
                  "with_food": "Có thể uống với hoặc không có thức ăn. Uống với thức ăn có thể giảm kích ứng dạ dày.",
                  "timing": "Uống 1 lần/ngày vào buổi sáng (để tránh đi tiểu đêm). Liều thấp (12.5-25mg) đủ cho tăng huyết áp. Uống cùng giờ mỗi ngày. Theo dõi cân bằng dịch, cân nặng."
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
                  "FDA Drug Label - Hydrochlorothiazide",
                  "UpToDate - Hydrochlorothiazide: Drug information",
                  "ALLHAT Study - JAMA (2002) - Thiazide trong tăng huyết áp",
                  "American Heart Association/American College of Cardiology guidelines - Hypertension"
              ],
              "last_updated": "2024-12-19",
              "evidence_level": "High - Extensive clinical experience and large RCTs (ALLHAT) in hypertension"
          }
      },
    # Antiarrhythmics
    "Amiodarone": {
        "group": "Cardiovascular - Antiarrhythmic (Class III)",
        "vietnamese_name": "Amiodarone, Cordarone",
        "administration": ["PO", "IV"],
        "indications": [
            "Rối loạn nhịp thất",
            "Rung nhĩ",
            "Nhịp nhanh trên thất",
            "Rối loạn nhịp kháng trị"
        ],
        "contraindications": [
            "Block nhĩ thất độ 2-3 không có máy tạo nhịp",
            "Rối loạn chức năng tuyến giáp",
            "Bệnh phổi mạn tính",
            "Bệnh gan nặng"
        ],
        "dosage": {
            "adult_po_loading": "800-1600mg/ngày chia 2 lần x 1-2 tuần",
            "adult_po_maintenance": "200-400mg x 1 lần/ngày",
            "adult_iv_loading": "150mg IV trong 10 phút, sau đó 1mg/phút x 6 giờ, 0.5mg/phút x 18 giờ",
            "notes": "Theo dõi chức năng gan, phổi, tuyến giáp định kỳ"
        },
        "side_effects": [
            "Bệnh phổi do amiodarone (nguy hiểm)",
            "Rối loạn chức năng tuyến giáp",
            "Bệnh gan",
            "Tích tụ ở da (màu xanh xám)",
            "Nhạy cảm với ánh sáng",
            "Corneal deposits",
            "Block nhĩ thất"
        ],
        "interactions": [
            "Digoxin: tăng nồng độ digoxin (giảm liều digoxin 50%)",
            "Warfarin: tăng tác dụng chống đông",
            "Statins: tăng nguy cơ tiêu cơ vân"
        ],
        "pregnancy": "D",
        "mechanism_of_action": "Class III antiarrhythmic (chủ yếu) với tác dụng bổ sung class I, II, IV. Chủ yếu ức chế kênh K+ (delayed rectifier), kéo dài phase 3 của action potential, kéo dài QT interval. Cũng có tác dụng ức chế Na+ channels (class I), chẹn beta (class II), và chẹn Ca2+ (class IV). Rất hiệu quả cho rối loạn nhịp nhưng có nhiều tác dụng phụ.",
        "monitoring": [
            "ECG: QT interval (kéo dài QT là bình thường, nhưng QT >500ms hoặc tăng >60ms nguy hiểm)",
            "Chức năng phổi: X-quang phổi, PFT (6 tháng/lần), đặc biệt chú ý dấu hiệu viêm phổi mô kẽ",
            "Chức năng gan: ALT, AST, bilirubin (mỗi 3-6 tháng)",
            "Chức năng tuyến giáp: TSH, FT4, FT3 (mỗi 6 tháng) - có thể gây cường giáp hoặc suy giáp",
            "Khám mắt: Soi đáy mắt (mỗi 6-12 tháng) - có thể gây viêm giác mạc, đục thủy tinh thể",
            "Da: Dấu hiệu nhạy cảm ánh sáng, xám da (blue-gray discoloration)",
            "Electrolytes: K+, Mg2+ (phải đảm bảo bình thường trước khi dùng)"
        ],
        "precautions": [
            "CẦN LOADING DOSE (thường 800-1600mg/ngày trong 1-2 tuần) trước khi dùng liều duy trì",
            "Tác dụng phụ nhiều và nghiêm trọng - chỉ dùng cho rối loạn nhịp đe dọa tính mạng hoặc không đáp ứng với thuốc khác",
            "Bắt buộc monitor chức năng phổi, gan, tuyến giáp, mắt định kỳ",
            "Tương tác thuốc rất nhiều - kiểm tra kỹ trước khi dùng",
            "Tránh dùng ở phụ nữ có thai (category D)",
            "Thời gian bán hủy rất dài (50-60 ngày) - tác dụng phụ có thể kéo dài sau khi ngừng",
            "Phải đảm bảo K+ và Mg2+ bình thường (giảm K+/Mg2+ tăng nguy cơ torsades de pointes)",
            "Tránh ánh nắng mặt trời (nhạy cảm ánh sáng nặng)"
        ],
        "pharmacokinetics": {
            "half_life": "50-60 ngày (RẤT DÀI - do tích lũy trong mô mỡ)",
            "onset": "1-3 tuần (do loading period)",
            "duration": "Rất lâu sau khi ngừng (do half-life dài)",
            "protein_binding": "96%",
            "clearance": "Gan (CYP3A4, CYP2C8), thải qua phân và nước tiểu (chậm)"
        },
        "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm, tránh ánh sáng",
        "black_box_warnings": "Có thể gây tử vong do viêm phổi mô kẽ, suy gan, rối loạn nhịp tim nặng. Chỉ dùng cho rối loạn nhịp đe dọa tính mạng không đáp ứng với thuốc khác. Phải monitor chức năng phổi, gan, tuyến giáp định kỳ. Chống chỉ định trong thai kỳ",
        "drug_interactions": {
            "major": [
                {
                    "drug": "Digoxin",
                    "mechanism": "Amiodarone ức chế P-glycoprotein và giảm thải trừ digoxin, tăng nồng độ digoxin",
                    "effect": "Tăng nồng độ digoxin 50-100%, tăng nguy cơ ngộ độc digoxin (rối loạn nhịp, block AV, buồn nôn)",
                    "management": "GIẢM LIỀU DIGOXIN 50% ngay khi bắt đầu amiodarone. Theo dõi nồng độ digoxin chặt chẽ. Có thể cần giảm liều digoxin thêm."
                },
                {
                    "drug": "Warfarin",
                    "mechanism": "Amiodarone ức chế CYP2C9 (chuyển hóa warfarin), tăng nồng độ warfarin",
                    "effect": "Tăng tác dụng chống đông mạnh, tăng INR, tăng nguy cơ chảy máu nặng",
                    "management": "GIẢM LIỀU WARFARIN 30-50% ngay khi bắt đầu amiodarone. Theo dõi INR thường xuyên (mỗi 1-2 tuần đầu). Có thể cần giảm liều warfarin thêm khi tác dụng amiodarone ổn định."
                },
                {
                    "drug": "Quinidine, Procainamide, Disopyramide",
                    "mechanism": "Tác dụng hiệp đồng kéo dài QT interval",
                    "effect": "Tăng nguy cơ torsades de pointes, rối loạn nhịp tim đe dọa tính mạng",
                    "management": "TRÁNH DÙNG CHUNG. Nếu bắt buộc: theo dõi ECG sát, đảm bảo K+ và Mg2+ bình thường."
                }
            ],
            "moderate": [
                {
                    "drug": "Statins (simvastatin, atorvastatin, lovastatin)",
                    "mechanism": "Amiodarone ức chế CYP3A4, tăng nồng độ statin",
                    "effect": "Tăng nguy cơ tiêu cơ vân (rhabdomyolysis), suy thận cấp",
                    "management": "Giảm liều statin 50% hoặc tránh dùng simvastatin/atorvastatin. Ưu tiên pravastatin, rosuvastatin (ít chuyển hóa qua CYP3A4). Theo dõi CK, triệu chứng đau cơ."
                },
                {
                    "drug": "Beta-blockers (metoprolol, propranolol)",
                    "mechanism": "Tác dụng hiệp đồng ức chế dẫn truyền nhĩ thất",
                    "effect": "Tăng nguy cơ block nhĩ thất, nhịp tim chậm nặng",
                    "management": "Thận trọng. Giảm liều beta-blocker. Theo dõi ECG, nhịp tim."
                },
                {
                    "drug": "Verapamil, Diltiazem",
                    "mechanism": "Tác dụng hiệp đồng ức chế dẫn truyền nhĩ thất và kéo dài QT",
                    "effect": "Tăng nguy cơ block nhĩ thất, nhịp tim chậm nặng",
                    "management": "Thận trọng. Giảm liều verapamil/diltiazem. Theo dõi ECG sát."
                },
                {
                    "drug": "Phenytoin",
                    "mechanism": "Amiodarone ức chế chuyển hóa phenytoin, phenytoin tăng chuyển hóa amiodarone",
                    "effect": "Tăng nồng độ phenytoin (ngộ độc), giảm nồng độ amiodarone (mất hiệu quả)",
                    "management": "Theo dõi nồng độ cả hai thuốc. Có thể cần điều chỉnh liều."
                },
                {
                    "drug": "Fentanyl",
                    "mechanism": "Amiodarone ức chế CYP3A4, tăng nồng độ fentanyl",
                    "effect": "Tăng nguy cơ ức chế hô hấp, ngừng thở",
                    "management": "Thận trọng. Giảm liều fentanyl. Theo dõi hô hấp sát."
                }
            ],
            "minor": [
                {
                    "drug": "Cyclosporine, Tacrolimus",
                    "mechanism": "Amiodarone ức chế CYP3A4, tăng nồng độ cyclosporine/tacrolimus",
                    "effect": "Tăng nguy cơ độc tính",
                    "management": "Theo dõi nồng độ. Có thể cần giảm liều."
                },
                {
                    "drug": "Theophylline",
                    "mechanism": "Amiodarone ức chế chuyển hóa theophylline",
                    "effect": "Tăng nồng độ theophylline",
                    "management": "Theo dõi nồng độ theophylline. Có thể cần giảm liều."
                }
            ]
        },
        "contraindications": {
            "absolute": [
                "Block nhĩ thất độ 2-3 không có máy tạo nhịp",
                "Rối loạn chức năng tuyến giáp không kiểm soát được",
                "Bệnh phổi mạn tính nặng (COPD, ILD)",
                "Bệnh gan nặng (Child-Pugh C)",
                "Có thai (category D)",
                "Hạ K+ hoặc Mg2+ nặng (tăng nguy cơ torsades de pointes)"
            ],
            "relative": [
                "Suy thận nặng (thận trọng, theo dõi chức năng thận)",
                "Nhịp tim chậm (tăng nguy cơ block AV)",
                "Bệnh phổi nhẹ (theo dõi chức năng phổi chặt chẽ)",
                "Rối loạn chức năng tuyến giáp nhẹ (theo dõi TSH chặt chẽ)",
                "Đang dùng warfarin hoặc digoxin (cần giảm liều)"
            ]
        },
        "pregnancy_lactation": {
            "fda_category": "D",
            "pregnancy_details": "CHỐNG CHỈ ĐỊNH TUYỆT ĐỐI trong thai kỳ. Amiodarone có thể gây dị tật thai nhi (hypothyroidism, goiter, bất thường tim mạch, chậm phát triển), chậm phát triển thai nhi, và tử vong thai nhi. Nguy cơ cao nhất trong 3 tháng đầu. Chỉ dùng trong trường hợp đe dọa tính mạng của mẹ và không có lựa chọn khác.",
            "lactation": {
                "safety": "Incompatible",
                "details": "Amiodarone bài tiết vào sữa mẹ ở nồng độ cao. Nồng độ trong máu trẻ bú mẹ có thể đạt 25% nồng độ mẹ. Có thể gây rối loạn chức năng tuyến giáp, nhịp tim chậm ở trẻ bú mẹ.",
                "recommendation": "KHÔNG KHUYẾN NGHỊ dùng khi cho con bú. Nếu bắt buộc: ngừng cho con bú hoặc ngừng amiodarone."
            }
        },
        "hepatic_adjustment": {
            "mild": "Không đổi",
            "moderate": "Giảm liều 25-50% (chuyển hóa qua gan)",
            "severe": "TRÁNH DÙNG (Child-Pugh C) hoặc giảm liều 50% (nếu bắt buộc), theo dõi chức năng gan chặt chẽ",
            "notes": "Amiodarone chuyển hóa qua gan (CYP3A4, CYP2C8). Suy gan làm giảm chuyển hóa, tăng nồng độ và tác dụng phụ. Bắt buộc theo dõi ALT, AST, bilirubin định kỳ."
        },
        "overdose_management": {
            "symptoms": [
                "Block nhĩ thất độ 2-3",
                "Nhịp tim chậm nặng",
                "Torsades de pointes (do QT kéo dài)",
                "Hạ huyết áp nặng",
                "Suy tim cấp",
                "Rối loạn nhịp tim đe dọa tính mạng"
            ],
            "antidote": "Không có antidote đặc hiệu. Điều trị hỗ trợ: máy tạo nhịp, hỗ trợ tuần hoàn",
            "treatment": [
                "Rửa dạ dày nếu uống trong vòng 1-2 giờ (nhưng thận trọng - có thể gây block AV)",
                "Than hoạt tính",
                "Điều trị block AV/nhịp tim chậm: Atropine 0.5-1mg IV, máy tạo nhịp tạm thời nếu cần",
                "Điều trị torsades de pointes: Magnesium sulfate 1-2g IV, nếu cần: pacing, isoproterenol",
                "Điều trị hạ huyết áp: Truyền dịch, nếu cần: dopamine, norepinephrine",
                "Hỗ trợ hô hấp và tuần hoàn nếu cần",
                "Theo dõi ECG liên tục (block AV, QT interval, rối loạn nhịp)",
                "Theo dõi ít nhất 24-48 giờ (do half-life rất dài 50-60 ngày)"
            ],
            "monitoring": "ECG liên tục (block AV, QT interval, rối loạn nhịp), huyết áp, nhịp tim, chức năng hô hấp, ý thức, điện giải (K+, Mg2+)"
        },
        "reversal_agents": {
            "available": False,
            "agents": []
        },
        "administration_instructions": {
            "oral": {
                "with_food": "Nên uống với thức ăn để giảm kích ứng dạ dày và tăng hấp thu.",
                "timing": "Loading dose: 800-1600mg/ngày chia 2 lần trong 1-2 tuần. Maintenance: 200-400mg x 1 lần/ngày. Uống cùng giờ mỗi ngày. KHÔNG ngừng đột ngột (half-life dài, nhưng có thể gây rối loạn nhịp)."
            },
            "iv": {
                "reconstitution": "Amiodarone IV: Dùng trực tiếp từ lọ. KHÔNG pha với các dung dịch khác trong cùng bơm tiêm (kết tủa).",
                "infusion_rate": "Loading: 150mg IV trong 10 phút, sau đó 1mg/phút x 6 giờ, 0.5mg/phút x 18 giờ. Maintenance: 0.5mg/phút. Theo dõi ECG và huyết áp liên tục. Chuyển sang PO càng sớm càng tốt.",
                "compatibility": ["D5W", "Normal saline"],
                "incompatibility": ["KHÔNG trộn với các thuốc khác trong cùng bơm tiêm (kết tủa)"],
                "notes": "Dùng cho cấp cứu rối loạn nhịp. Theo dõi ECG và huyết áp liên tục. Chuyển sang PO càng sớm càng tốt (trong vòng 24-48 giờ)."
            }
        },
        "references": {
            "primary_sources": [
                "FDA Drug Label - Cordarone (amiodarone)",
                "UpToDate - Amiodarone: Drug information",
                "EMERALD Study - Circulation",
                "ARREST Study - New England Journal of Medicine",
                "American Heart Association/American College of Cardiology guidelines - Arrhythmias"
            ],
            "last_updated": "2024-12-19",
            "evidence_level": "High - Multiple RCTs (EMERALD, ARREST) and extensive clinical experience in life-threatening arrhythmias"
        }
      },
      "Digoxin": {
        "group": "Cardiovascular - Cardiac Glycoside",
        "vietnamese_name": "Digoxin, Lanoxin",
        "administration": ["PO", "IV"],
        "indications": [
            "Suy tim với rung nhĩ",
            "Rung nhĩ kiểm soát tần số",
            "Suy tim không rung nhĩ (ít dùng)"
        ],
        "contraindications": [
            "Block nhĩ thất độ 2-3",
            "Nhịp tim chậm nặng",
            "Hội chứng Wolff-Parkinson-White",
            "Ngộ độc digoxin"
        ],
        "dosage": {
            "adult_po_loading": "0.5-1mg chia 2-3 lần/ngày x 1 ngày",
            "adult_po_maintenance": "0.125-0.25mg x 1 lần/ngày",
            "adult_iv": "0.25-0.5mg IV x 1 lần",
            "elderly": "Liều thấp hơn (0.0625-0.125mg/ngày)",
            "notes": "Theo dõi nồng độ digoxin (mục tiêu 0.8-2 ng/mL)"
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "Giảm liều 25-50%",
            "under_30": "Giảm liều 50-75%",
            "hemodialysis": "Bổ sung sau lọc máu"
        },
        "side_effects": [
            "Ngộ độc digoxin (buồn nôn, rối loạn nhịp, rối loạn thị giác)",
            "Nhịp tim chậm",
            "Block nhĩ thất",
            "Rối loạn nhịp (ngoại tâm thu, nhịp nhanh thất)"
        ],
        "interactions": [
            "Amiodarone: tăng nồng độ digoxin (giảm liều 50%)",
            "Furosemide: tăng nguy cơ ngộ độc (hạ kali)",
            "Verapamil: tăng nồng độ digoxin",
            "Quinine: tăng nồng độ digoxin"
        ],
        "pregnancy": "C",
        "mechanism_of_action": "Ức chế Na+/K+-ATPase ở màng tế bào cơ tim, tăng nồng độ Na+ nội bào, kích thích Na+/Ca2+ exchanger, tăng Ca2+ nội bào → tăng lực co bóp cơ tim (inotropy dương). Ở nút AV: tăng trương lực phế vị, giảm dẫn truyền AV (làm chậm tần số thất trong AF)",
        "monitoring": [
            "Nồng độ digoxin trong máu (BẮT BUỘC): Mục tiêu 0.8-2 ng/mL (1.0-2.6 nmol/L)",
            "Đo nồng độ ít nhất 6-8 giờ sau liều (sau khi phân bố)",
            "Điện giải: K+, Mg2+ (quan trọng - hạ K+, hạ Mg2+ → tăng nguy cơ ngộ độc)",
            "Creatinine, eGFR (digoxin thải qua thận)",
            "ECG: nhịp tim, block AV, rối loạn nhịp",
            "Triệu chứng ngộ độc: buồn nôn, nôn, rối loạn thị giác (nhìn vàng xanh), rối loạn nhịp"
        ],
        "precautions": [
            "LUÔN theo dõi nồng độ trong máu (therapeutic window hẹp)",
            "Hạ K+ và hạ Mg2+ làm tăng nguy cơ ngộ độc mạnh → phải bù điện giải trước",
            "Giảm liều ở suy thận (half-life tăng từ 36h lên 4-6 ngày)",
            "Ở người già: dùng liều thấp hơn (0.0625-0.125mg/ngày)",
            "Tránh loading dose nhanh ở suy thận (nguy cơ ngộ độc)",
            "Nhiều thuốc tương tác làm tăng nồng độ: amiodarone, verapamil, diltiazem, quinidine, macrolides, cyclosporine",
            "Ngộ độc digoxin có thể đe dọa tính mạng → cần điều trị ngay (Digibind/digoxin immune fab)"
        ],
        "pharmacokinetics": {
            "half_life": "36-48 giờ (bình thường), 4-6 ngày (suy thận)",
            "onset": "1-2 giờ (PO), 5-30 phút (IV)",
            "duration": "3-4 ngày (vì half-life dài)",
            "protein_binding": "20-25%",
            "clearance": "Thận (75-80%), không chuyển hóa"
        },
        "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm, tránh ánh sáng. Viên nén: ổn định",
        "black_box_warnings": "Không dùng trong WPW với AF (có thể gây nhịp nhanh thất nguy hiểm). Ngộ độc digoxin có thể gây rối loạn nhịp đe dọa tính mạng và tử vong",
        "drug_interactions": {
            "major": [
                {
                    "drug": "Amiodarone",
                    "mechanism": "Amiodarone ức chế P-glycoprotein và giảm thải trừ digoxin, tăng nồng độ digoxin",
                    "effect": "Tăng nồng độ digoxin 50-100%, tăng nguy cơ ngộ độc digoxin (rối loạn nhịp, block AV, buồn nôn)",
                    "management": "GIẢM LIỀU DIGOXIN 50% ngay khi bắt đầu amiodarone. Theo dõi nồng độ digoxin chặt chẽ. Có thể cần giảm liều digoxin thêm."
                },
                {
                    "drug": "Verapamil, Diltiazem",
                    "mechanism": "Verapamil/diltiazem ức chế P-glycoprotein, giảm thải trừ digoxin",
                    "effect": "Tăng nồng độ digoxin 50-70%, tăng nguy cơ ngộ độc",
                    "management": "Giảm liều digoxin 25-50%. Theo dõi nồng độ digoxin. Theo dõi ECG."
                },
                {
                    "drug": "Quinidine, Quinine",
                    "mechanism": "Quinidine/quinine ức chế P-glycoprotein, giảm thải trừ digoxin",
                    "effect": "Tăng nồng độ digoxin 50-100%, tăng nguy cơ ngộ độc",
                    "management": "Giảm liều digoxin 50%. Theo dõi nồng độ digoxin chặt chẽ."
                },
                {
                    "drug": "Macrolides (clarithromycin, erythromycin)",
                    "mechanism": "Macrolides ức chế P-glycoprotein và có thể giảm chuyển hóa digoxin bởi vi khuẩn ruột",
                    "effect": "Tăng nồng độ digoxin, tăng nguy cơ ngộ độc",
                    "management": "Thận trọng. Theo dõi nồng độ digoxin. Có thể cần giảm liều digoxin."
                },
                {
                    "drug": "Diuretics (furosemide, hydrochlorothiazide)",
                    "mechanism": "Diuretics gây hạ kali máu, tăng độc tính digoxin",
                    "effect": "Tăng nguy cơ ngộ độc digoxin mạnh (rối loạn nhịp, block AV) ngay cả khi nồng độ digoxin bình thường",
                    "management": "Duy trì kali máu >4.0 mEq/L. Theo dõi kali máu thường xuyên. Cân nhắc dùng kali-sparing diuretic hoặc bổ sung kali."
                }
            ],
            "moderate": [
                {
                    "drug": "Cyclosporine, Tacrolimus",
                    "mechanism": "Cyclosporine/tacrolimus ức chế P-glycoprotein",
                    "effect": "Tăng nồng độ digoxin",
                    "management": "Theo dõi nồng độ digoxin. Có thể cần giảm liều digoxin."
                },
                {
                    "drug": "Propafenone, Flecainide",
                    "mechanism": "Propafenone/flecainide có thể tăng nồng độ digoxin",
                    "effect": "Tăng nguy cơ ngộ độc digoxin",
                    "management": "Theo dõi nồng độ digoxin. Có thể cần giảm liều digoxin."
                },
                {
                    "drug": "Spironolactone, Eplerenone",
                    "mechanism": "Spironolactone/eplerenone ức chế thải trừ digoxin, có thể tăng kali máu",
                    "effect": "Tăng nồng độ digoxin (nhẹ), có thể tăng kali máu",
                    "management": "Theo dõi nồng độ digoxin và kali máu. Thường không cần giảm liều digoxin."
                },
                {
                    "drug": "Cholestyramine, Colestipol",
                    "mechanism": "Giảm hấp thu digoxin",
                    "effect": "Giảm nồng độ digoxin, giảm hiệu quả",
                    "management": "Dùng digoxin ít nhất 2 giờ trước hoặc sau các thuốc này."
                },
                {
                    "drug": "Rifampin",
                    "mechanism": "Rifampin tăng chuyển hóa digoxin (hiếm)",
                    "effect": "Giảm nồng độ digoxin",
                    "management": "Theo dõi nồng độ digoxin. Có thể cần tăng liều digoxin."
                }
            ],
            "minor": [
                {
                    "drug": "NSAIDs",
                    "mechanism": "Có thể giảm thải trừ digoxin nhẹ",
                    "effect": "Tăng nồng độ digoxin nhẹ",
                    "management": "Thận trọng. Theo dõi nồng độ digoxin."
                },
                {
                    "drug": "Calcium",
                    "mechanism": "Tăng Ca2+ nội bào (tương tự digoxin)",
                    "effect": "Tăng nguy cơ ngộ độc digoxin (tăng lực co bóp tim quá mức)",
                    "management": "Thận trọng khi dùng calcium IV. Theo dõi ECG."
                }
            ]
        },
        "contraindications": {
            "absolute": [
                "Block nhĩ thất độ 2-3",
                "Nhịp tim chậm nặng (<50 bpm)",
                "Hội chứng Wolff-Parkinson-White với rung nhĩ (tăng nguy cơ nhịp nhanh thất nguy hiểm)",
                "Ngộ độc digoxin đang hoạt động",
                "Hạ kali máu nặng không kiểm soát được",
                "Hạ magie máu nặng không kiểm soát được"
            ],
            "relative": [
                "Suy thận nặng (half-life tăng lên 4-6 ngày, tăng nguy cơ tích lũy)",
                "Suy gan (thận trọng, theo dõi chức năng gan)",
                "Người già (tăng nhạy cảm, giảm chức năng thận)",
                "Bệnh phổi nặng (tăng nhạy cảm)",
                "Rối loạn điện giải (hạ K+, hạ Mg2+)"
            ]
        },
        "pregnancy_lactation": {
            "fda_category": "C",
            "pregnancy_details": "Có thể dùng khi cần thiết. Digoxin đi qua nhau thai. Nồng độ trong máu thai nhi thường thấp hơn mẹ. Có thể gây nhịp tim chậm thai nhi, nhưng thường an toàn. Theo dõi sát thai nhi. Cân nhắc lợi ích/nguy cơ.",
            "lactation": {
                "safety": "Compatible",
                "details": "Digoxin bài tiết vào sữa mẹ ở nồng độ thấp. Nồng độ trong máu trẻ bú mẹ thường rất thấp (<1 ng/mL). Không có báo cáo về tác dụng phụ nghiêm trọng ở trẻ bú mẹ.",
                "recommendation": "Có thể dùng khi cho con bú. Theo dõi trẻ nếu có dấu hiệu nhịp tim chậm hoặc triệu chứng ngộ độc digoxin."
            }
        },
        "hepatic_adjustment": {
            "mild": "Không đổi",
            "moderate": "Thận trọng (digoxin không chuyển hóa qua gan, nhưng suy gan có thể ảnh hưởng đến protein binding)",
            "severe": "Thận trọng, có thể giảm liều nhẹ",
            "notes": "Digoxin thải chủ yếu qua thận (75-80%), không chuyển hóa qua gan. Tuy nhiên, suy gan có thể ảnh hưởng đến protein binding và có thể tăng nhạy cảm. Thận trọng ở bệnh nhân suy gan."
        },
        "overdose_management": {
            "symptoms": [
                "Buồn nôn, nôn",
                "Rối loạn thị giác (nhìn vàng xanh, halos, blur)",
                "Nhịp tim chậm nặng",
                "Block nhĩ thất độ 2-3",
                "Rối loạn nhịp tim (ngoại tâm thu, nhịp nhanh thất, VT, VF)",
                "Hạ kali máu (do ngộ độc digoxin)",
                "Tử vong"
            ],
            "antidote": "Digoxin Immune Fab (Digibind, DigiFab) - ANTIDOTE ĐẶC HIỆU",
            "treatment": [
                "NGỪNG DIGOXIN NGAY LẬP TỨC",
                "Rửa dạ dày nếu uống trong vòng 1-2 giờ",
                "Than hoạt tính",
                "Điều trị ngộ độc nặng: Digoxin Immune Fab (Digibind/DigiFab) - liều theo nồng độ digoxin hoặc liều uống",
                "Công thức: Số lọ Digibind = (nồng độ digoxin ng/mL × cân nặng kg) / 100 (hoặc liều uống mg / 0.6)",
                "Điều trị hạ kali máu: Kali chloride IV (THẬN TRỌNG - có thể làm nặng block AV nếu ngộ độc nặng)",
                "Điều trị block AV/nhịp tim chậm: Atropine 0.5-1mg IV, máy tạo nhịp tạm thời nếu cần",
                "Điều trị rối loạn nhịp: Phenytoin, lidocaine (tránh dùng quinidine, procainamide - có thể làm nặng)",
                "Điều trị hạ magie máu: Magie sulfate IV",
                "Hỗ trợ hô hấp và tuần hoàn nếu cần",
                "Theo dõi ít nhất 24-48 giờ (do half-life dài 36-48 giờ)"
            ],
            "monitoring": "Nồng độ digoxin (trước và sau Digibind), ECG liên tục (block AV, rối loạn nhịp), huyết áp, nhịp tim, điện giải (K+, Mg2+), chức năng thận, ý thức"
        },
        "reversal_agents": {
            "available": True,
            "agents": [
                {
                    "name": "Digoxin Immune Fab (Digibind, DigiFab)",
                    "mechanism": "Kháng thể đặc hiệu gắn với digoxin, tạo phức hợp không hoạt động, tăng thải trừ qua thận",
                    "indication": "Ngộ độc digoxin nặng (rối loạn nhịp đe dọa tính mạng, block AV, nồng độ >2 ng/mL với triệu chứng)",
                    "dose": "Liều tính theo: (nồng độ digoxin ng/mL × cân nặng kg) / 100, HOẶC (liều uống mg) / 0.6. Thường 10-20 lọ (380mg/lọ). Tiêm IV từ từ."
                }
            ]
        },
        "administration_instructions": {
            "oral": {
                "with_food": "Có thể uống với hoặc không có thức ăn. Không ảnh hưởng đáng kể đến hấp thu.",
                "timing": "Uống 1 lần/ngày, cùng giờ mỗi ngày. Uống cùng thời điểm để duy trì nồng độ ổn định. KHÔNG bỏ liều. Nếu quên: uống ngay khi nhớ, nhưng không uống gấp đôi."
            },
            "iv": {
                "reconstitution": "Digoxin IV: Pha với D5W hoặc normal saline. Nồng độ: 0.25mg/ml. KHÔNG pha với các thuốc khác.",
                "infusion_rate": "Bolus: 0.25-0.5mg IV qua 5-10 phút. KHÔNG tiêm trực tiếp (nguy cơ block AV). Theo dõi ECG và huyết áp liên tục trong khi tiêm.",
                "compatibility": ["D5W", "Normal saline"],
                "incompatibility": ["KHÔNG trộn với các thuốc khác"],
                "notes": "Dùng cho cấp cứu. Tiêm CHẬM qua 5-10 phút. Theo dõi ECG và huyết áp liên tục. Chuyển sang PO càng sớm càng tốt."
            }
        },
        "references": {
            "primary_sources": [
                "FDA Drug Label - Lanoxin (digoxin)",
                "UpToDate - Digoxin: Drug information",
                "DIG Study - New England Journal of Medicine (1997) - Digoxin trong suy tim",
                "AFFIRM Study - New England Journal of Medicine (2002) - Digoxin trong rung nhĩ",
                "American Heart Association/American College of Cardiology guidelines - Heart failure, Atrial fibrillation"
            ],
            "last_updated": "2024-12-19",
            "evidence_level": "High - Multiple large RCTs (DIG, AFFIRM) and extensive clinical experience"
        }
    },
    # Anticoagulants
    "Warfarin": {
        "group": "Cardiovascular - Anticoagulant (Vitamin K Antagonist)",
        "vietnamese_name": "Warfarin, Coumadin",
        "administration": ["PO"],
        "indications": [
            "Phòng ngừa đột quỵ trong rung nhĩ",
            "Huyết khối tĩnh mạch sâu (DVT)",
            "Thuyên tắc phổi (PE)",
            "Sau phẫu thuật tim mạch",
            "Thay van tim cơ học"
        ],
        "contraindications": [
            "Chảy máu đang hoạt động",
            "Có thai (3 tháng đầu và cuối)",
            "Bệnh gan nặng",
            "Không tuân thủ điều trị"
        ],
        "dosage": {
            "adult_loading": "5-10mg x 1 lần/ngày x 2-3 ngày",
            "adult_maintenance": "2-10mg x 1 lần/ngày (theo INR)",
            "target_inr": "2.0-3.0 (hầu hết), 2.5-3.5 (van tim cơ học)",
            "notes": "Theo dõi INR thường xuyên, điều chỉnh liều theo INR"
        },
        "side_effects": [
            "Chảy máu (nặng có thể tử vong)",
            "Hoại tử da (hiếm, ngày 3-10)",
            "Dị tật thai nhi",
            "Tăng nguy cơ loãng xương"
        ],
        "interactions": [
            "Aspirin/NSAID: tăng nguy cơ chảy máu",
            "Metronidazole: tăng tác dụng warfarin",
            "Vitamin K: giảm tác dụng",
            "Nhiều thuốc khác (xem interaction checker)"
        ],
        "pregnancy": "X - Chống chỉ định (trừ trường hợp đặc biệt)",
        "mechanism_of_action": "Ức chế enzyme vitamin K epoxide reductase, giảm tổng hợp các yếu tố đông máu phụ thuộc vitamin K (II, VII, IX, X)",
        "monitoring": [
            "INR mỗi 1-4 tuần khi ổn định, thường xuyên hơn khi mới bắt đầu hoặc thay đổi liều",
            "INR mỗi 2-3 ngày trong tuần đầu",
            "Công thức máu (Hct, Hb) nếu nghi ngờ chảy máu",
            "Theo dõi dấu hiệu chảy máu (chảy máu chân răng, chảy máu mũi, vết bầm tím)"
        ],
        "precautions": [
            "Uống cùng thời điểm mỗi ngày",
            "Tránh thay đổi đột ngột chế độ ăn (vitamin K)",
            "Giữ chế độ ăn ổn định vitamin K",
            "Tránh rượu (tăng nguy cơ chảy máu)",
            "Thông báo bác sĩ trước khi phẫu thuật",
            "Theo dõi hoại tử da (ngày 3-10, thường ở bệnh nhân thiếu protein C)"
        ],
        "pharmacokinetics": {
            "half_life": "40 giờ (dài)",
            "onset": "24-72 giờ",
            "duration": "2-5 ngày sau khi ngừng",
            "protein_binding": "99%",
            "clearance": "Gan (CYP2C9, CYP1A2)"
        },
        "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ánh sáng",
        "black_box_warnings": "Chảy máu nặng có thể dẫn đến tử vong. Cần theo dõi INR chặt chẽ. Hoại tử da hiếm nhưng nguy hiểm",
        "drug_interactions": {
            "major": [
                {
                    "drug": "Aspirin, NSAIDs (ibuprofen, naproxen)",
                    "mechanism": "Aspirin/NSAIDs ức chế kết tập tiểu cầu và gây loét dạ dày",
                    "effect": "Tăng nguy cơ chảy máu nặng, đặc biệt chảy máu dạ dày ruột",
                    "management": "TRÁNH DÙNG CHUNG nếu có thể. Nếu cần: dùng liều thấp aspirin (75-100mg), cân nhắc dùng PPI, theo dõi dấu hiệu chảy máu chặt chẽ."
                },
                {
                    "drug": "Amiodarone",
                    "mechanism": "Amiodarone ức chế CYP2C9 (chuyển hóa warfarin), tăng nồng độ warfarin",
                    "effect": "Tăng tác dụng chống đông mạnh, tăng INR, tăng nguy cơ chảy máu nặng",
                    "management": "GIẢM LIỀU WARFARIN 30-50% ngay khi bắt đầu amiodarone. Theo dõi INR thường xuyên (mỗi 1-2 tuần đầu). Có thể cần giảm liều warfarin thêm."
                },
                {
                    "drug": "Metronidazole, Fluconazole, Ketoconazole",
                    "mechanism": "Ức chế CYP2C9, tăng nồng độ warfarin",
                    "effect": "Tăng tác dụng chống đông, tăng INR",
                    "management": "Giảm liều warfarin 30-50%. Theo dõi INR thường xuyên. Tăng liều warfarin khi ngừng các thuốc này."
                },
                {
                    "drug": "Rifampin",
                    "mechanism": "Rifampin tăng chuyển hóa warfarin (CYP2C9 induction)",
                    "effect": "Giảm tác dụng chống đông, giảm INR",
                    "management": "Tăng liều warfarin khi bắt đầu rifampin. Giảm liều warfarin khi ngừng rifampin. Theo dõi INR thường xuyên."
                }
            ],
            "moderate": [
                {
                    "drug": "Clopidogrel, Ticagrelor, Prasugrel",
                    "mechanism": "Tác dụng hiệp đồng ức chế kết tập tiểu cầu",
                    "effect": "Tăng nguy cơ chảy máu",
                    "management": "Thận trọng. Theo dõi dấu hiệu chảy máu chặt chẽ. Thường TRÁNH dùng chung (trừ chỉ định đặc biệt)."
                },
                {
                    "drug": "SSRIs (fluoxetine, sertraline, paroxetine)",
                    "mechanism": "SSRIs ức chế kết tập tiểu cầu nhẹ, có thể ức chế CYP2C9",
                    "effect": "Tăng nguy cơ chảy máu nhẹ",
                    "management": "Thận trọng. Theo dõi dấu hiệu chảy máu."
                },
                {
                    "drug": "Antibiotics (sulfamethoxazole-trimethoprim, ciprofloxacin)",
                    "mechanism": "Ức chế CYP2C9, tăng nồng độ warfarin",
                    "effect": "Tăng tác dụng chống đông",
                    "management": "Theo dõi INR thường xuyên. Có thể cần giảm liều warfarin tạm thời."
                },
                {
                    "drug": "Vitamin K",
                    "mechanism": "Đối kháng với warfarin (tăng tổng hợp yếu tố đông máu)",
                    "effect": "Giảm tác dụng chống đông, giảm INR",
                    "management": "Thận trọng với chế độ ăn giàu vitamin K (rau xanh). Giữ chế độ ăn ổn định. Nếu cần đối kháng: Vitamin K IV hoặc PO."
                },
                {
                    "drug": "Statins (simvastatin, atorvastatin)",
                    "mechanism": "Có thể ức chế CYP2C9 nhẹ",
                    "effect": "Tăng tác dụng chống đông nhẹ",
                    "management": "Thận trọng. Theo dõi INR."
                }
            ],
            "minor": [
                {
                    "drug": "Acetaminophen (liều cao >2g/ngày)",
                    "mechanism": "Có thể ức chế CYP2C9",
                    "effect": "Tăng tác dụng chống đông nhẹ",
                    "management": "Thận trọng với liều cao. Theo dõi INR."
                },
                {
                    "drug": "Omeprazole",
                    "mechanism": "Có thể ức chế CYP2C9 nhẹ",
                    "effect": "Tăng tác dụng chống đông nhẹ",
                    "management": "Thận trọng. Theo dõi INR."
                }
            ]
        },
        "contraindications": {
            "absolute": [
                "Chảy máu đang hoạt động",
                "Có thai (3 tháng đầu và cuối - category X)",
                "Bệnh gan nặng (Child-Pugh C)",
                "Thiếu protein C hoặc S bẩm sinh (tăng nguy cơ hoại tử da)",
                "Không tuân thủ điều trị"
            ],
            "relative": [
                "Bệnh gan nhẹ-trung bình (thận trọng, theo dõi chức năng gan)",
                "Suy thận nặng (thận trọng)",
                "Người già (>75 tuổi - tăng nguy cơ chảy máu)",
                "Tiền sử loét dạ dày tá tràng (tăng nguy cơ chảy máu)",
                "Đang dùng aspirin/NSAIDs (tăng nguy cơ chảy máu)",
                "Rối loạn đông máu (hemophilia, von Willebrand disease)"
            ]
        },
        "pregnancy_lactation": {
            "fda_category": "X",
            "pregnancy_details": "CHỐNG CHỈ ĐỊNH TUYỆT ĐỐI trong thai kỳ (trừ trường hợp van tim cơ học - lợi ích vượt trội nguy cơ). Warfarin đi qua nhau thai và có thể gây dị tật thai nhi (warfarin embryopathy: hypoplastic nose, chondrodysplasia punctata), chảy máu thai nhi, chảy máu nhau thai, sẩy thai, và tử vong thai nhi. Nguy cơ cao nhất trong 3 tháng đầu (dị tật) và 3 tháng cuối (chảy máu). Nếu đang dùng warfarin và có thai: ngừng ngay và chuyển sang heparin/LMWH.",
            "lactation": {
                "safety": "Compatible",
                "details": "Warfarin bài tiết vào sữa mẹ ở nồng độ thấp. Nồng độ trong máu trẻ bú mẹ thường rất thấp (do protein binding 99%). Không có báo cáo về tác dụng phụ nghiêm trọng ở trẻ bú mẹ.",
                "recommendation": "Có thể dùng khi cho con bú. Theo dõi trẻ nếu có dấu hiệu chảy máu."
            }
        },
        "hepatic_adjustment": {
            "mild": "Không đổi",
            "moderate": "Thận trọng (warfarin chuyển hóa qua gan)",
            "severe": "TRÁNH DÙNG (Child-Pugh C) hoặc thận trọng (nếu bắt buộc), theo dõi chức năng gan và INR chặt chẽ",
            "notes": "Warfarin chuyển hóa qua gan (CYP2C9, CYP1A2). Suy gan làm giảm tổng hợp yếu tố đông máu và có thể ảnh hưởng đến chuyển hóa warfarin. Bắt buộc theo dõi chức năng gan và INR chặt chẽ."
        },
        "overdose_management": {
            "symptoms": [
                "Chảy máu (chảy máu chân răng, chảy máu mũi, vết bầm tím, phân đen, nôn ra máu)",
                "Chảy máu nặng (xuất huyết nội sọ, xuất huyết tiêu hóa, chảy máu nội tạng)",
                "INR tăng cao (>5.0)",
                "Hoại tử da (hiếm, ngày 3-10, thường ở bệnh nhân thiếu protein C)"
            ],
            "antidote": "Vitamin K (phytomenadione) - ANTIDOTE",
            "treatment": [
                "NGỪNG WARFARIN NGAY LẬP TỨC",
                "Đánh giá mức độ chảy máu: Nếu chảy máu nặng hoặc INR >10: Vitamin K + Fresh Frozen Plasma (FFP) hoặc Prothrombin Complex Concentrate (PCC)",
                "Nếu INR 4.5-10, không chảy máu: Giảm liều warfarin hoặc bỏ 1-2 liều, theo dõi INR",
                "Nếu INR >10, không chảy máu: Vitamin K 1-5mg PO, theo dõi INR",
                "Nếu chảy máu nhẹ: Vitamin K 1-2mg PO, theo dõi INR",
                "Nếu chảy máu nặng: Vitamin K 5-10mg IV + FFP hoặc PCC + hỗ trợ hô hấp và tuần hoàn",
                "Theo dõi INR thường xuyên (mỗi 6-12 giờ khi chảy máu nặng)",
                "Điều trị nguyên nhân chảy máu nếu có"
            ],
            "monitoring": "INR (mỗi 6-12 giờ khi chảy máu nặng), công thức máu (Hct, Hb, tiểu cầu), dấu hiệu chảy máu (chảy máu chân răng, chảy máu mũi, vết bầm tím, phân đen, nôn ra máu), chức năng thận, gan, ý thức"
        },
        "reversal_agents": {
            "available": True,
            "agents": [
                {
                    "name": "Vitamin K (Phytomenadione)",
                    "mechanism": "Kích thích tổng hợp các yếu tố đông máu phụ thuộc vitamin K (II, VII, IX, X)",
                    "indication": "INR tăng cao (>5.0) hoặc chảy máu do warfarin",
                    "dose": "PO: 1-5mg (INR >10, không chảy máu). IV: 5-10mg (chảy máu nặng). Tác dụng sau 6-12 giờ (PO) hoặc 1-2 giờ (IV)."
                },
                {
                    "name": "Fresh Frozen Plasma (FFP)",
                    "mechanism": "Cung cấp các yếu tố đông máu",
                    "indication": "Chảy máu nặng do warfarin",
                    "dose": "10-15ml/kg IV. Tác dụng ngay lập tức."
                },
                {
                    "name": "Prothrombin Complex Concentrate (PCC)",
                    "mechanism": "Cung cấp nồng độ cao các yếu tố đông máu II, VII, IX, X",
                    "indication": "Chảy máu nặng do warfarin (ưu tiên hơn FFP)",
                    "dose": "25-50 units/kg IV. Tác dụng ngay lập tức."
                }
            ]
        },
        "administration_instructions": {
            "oral": {
                "with_food": "Có thể uống với hoặc không có thức ăn. Không ảnh hưởng đáng kể đến hấp thu.",
                "timing": "Uống 1 lần/ngày, CÙNG THỜI ĐIỂM mỗi ngày (ví dụ: 6 giờ tối). Rất quan trọng để duy trì nồng độ ổn định. KHÔNG bỏ liều. Nếu quên: uống ngay khi nhớ, nhưng không uống gấp đôi. Giữ chế độ ăn ổn định (vitamin K)."
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
                "FDA Drug Label - Coumadin (warfarin)",
                "UpToDate - Warfarin: Drug information",
                "WARCEF Study - New England Journal of Medicine (2012)",
                "RE-LY Study - New England Journal of Medicine (2009) - So sánh warfarin với dabigatran",
                "American Heart Association/American College of Cardiology guidelines - Anticoagulation"
            ],
            "last_updated": "2024-12-19",
            "evidence_level": "High - Extensive clinical experience and multiple large RCTs (WARCEF, RE-LY) in anticoagulation"
        }
    },
    # Antiplatelets
    "Aspirin": {
        "group": "Cardiovascular - Antiplatelet",
        "vietnamese_name": "Aspirin, Acetylsalicylic acid",
        "administration": ["PO"],
        "indications": [
            "Dự phòng nhồi máu cơ tim",
            "Dự phòng đột quỵ",
            "Sau đặt stent",
            "Đau, sốt, viêm",
            "Viêm khớp dạng thấp"
        ],
        "contraindications": [
            "Loét dạ dày tá tràng đang hoạt động",
            "Chảy máu đang hoạt động",
            "Dị ứng aspirin",
            "Trẻ em <12 tuổi (hội chứng Reye)"
        ],
        "dosage": {
            "adult_cardioprotective": "75-100mg x 1 lần/ngày",
            "adult_pain": "325-650mg mỗi 4-6 giờ",
            "adult_arthritis": "325-650mg x 4 lần/ngày",
            "notes": "Liều thấp (75-100mg) cho dự phòng tim mạch"
        },
        "side_effects": [
            "Chảy máu dạ dày",
            "Loét dạ dày tá tràng",
            "Chảy máu nói chung",
            "Ù tai (liều cao)",
            "Co thắt phế quản (ở bệnh nhân hen)"
        ],
        "interactions": [
            "Warfarin: tăng nguy cơ chảy máu nặng",
            "NSAID khác: tăng nguy cơ chảy máu dạ dày",
            "ACE inhibitor: giảm hiệu quả hạ huyết áp"
        ],
        "pregnancy": "C - D trong 3 tháng cuối",
        "mechanism_of_action": "Ức chế không hồi phục enzyme cyclooxygenase (COX-1), ức chế kết tập tiểu cầu và tổng hợp prostaglandin. Với liều cao: giảm đau, hạ sốt, kháng viêm",
        "monitoring": [
            "Dấu hiệu chảy máu (phân đen, nôn ra máu, chảy máu chân răng)",
            "Hemoglobin nếu nghi ngờ chảy máu",
            "Chức năng thận nếu dùng lâu dài",
            "Ù tai nếu dùng liều cao (dấu hiệu độc tính)"
        ],
        "precautions": [
            "Dùng với thức ăn hoặc sau ăn để giảm kích ứng dạ dày",
            "Cân nhắc dùng PPI nếu có nguy cơ loét dạ dày",
            "Ngừng 5-7 ngày trước phẫu thuật lớn (nếu có thể)",
            "Không dùng cho trẻ <12 tuổi (hội chứng Reye)",
            "Không dùng với rượu (tăng nguy cơ chảy máu dạ dày)"
        ],
        "pharmacokinetics": {
            "half_life": "2-3 giờ (liều thấp), 15-20 giờ (liều cao)",
            "onset": "30 phút",
            "duration": "7-10 ngày (tiểu cầu, liều thấp), 4-6 giờ (giảm đau)",
            "protein_binding": "50-80%",
            "clearance": "Gan (thủy phân) và thận"
        },
        "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm",
        "black_box_warnings": "Tăng nguy cơ chảy máu, đặc biệt chảy máu dạ dày ruột. Nguy cơ tăng ở người già và dùng chung với thuốc khác",
        "drug_interactions": {
            "major": [
                {
                    "drug": "Warfarin",
                    "mechanism": "Tác dụng hiệp đồng ức chế đông máu",
                    "effect": "Tăng nguy cơ chảy máu nặng",
                    "management": "TRÁNH DÙNG CHUNG nếu có thể. Nếu cần: theo dõi INR và dấu hiệu chảy máu chặt chẽ."
                },
                {
                    "drug": "NSAIDs (ibuprofen, naproxen, diclofenac)",
                    "mechanism": "NSAIDs cũng ức chế COX-1 và gây loét dạ dày",
                    "effect": "Tăng nguy cơ chảy máu dạ dày ruột, loét dạ dày tá tràng",
                    "management": "Thận trọng. Cân nhắc dùng PPI. Theo dõi dấu hiệu chảy máu dạ dày. Tránh dùng lâu dài cùng."
                },
                {
                    "drug": "Clopidogrel, Ticagrelor, Prasugrel",
                    "mechanism": "Tác dụng hiệp đồng ức chế kết tập tiểu cầu",
                    "effect": "Tăng nguy cơ chảy máu (nhưng có chỉ định trong DAPT sau ACS/stent)",
                    "management": "Dùng kèm sau ACS/stent: DAPT 12 tháng (hoặc theo hướng dẫn). Theo dõi dấu hiệu chảy máu chặt chẽ."
                }
            ],
            "moderate": [
                {
                    "drug": "ACE inhibitors, ARBs",
                    "mechanism": "Aspirin có thể giảm hiệu quả hạ huyết áp của ACE/ARB (ức chế prostaglandin)",
                    "effect": "Giảm hiệu quả hạ huyết áp",
                    "management": "Thận trọng. Theo dõi huyết áp. Thường không cần điều chỉnh (lợi ích dự phòng tim mạch của aspirin)."
                },
                {
                    "drug": "Corticosteroids (prednisone, hydrocortisone)",
                    "mechanism": "Corticosteroids cũng gây loét dạ dày",
                    "effect": "Tăng nguy cơ loét dạ dày tá tràng",
                    "management": "Cân nhắc dùng PPI. Theo dõi dấu hiệu loét dạ dày."
                },
                {
                    "drug": "SSRIs (fluoxetine, sertraline)",
                    "mechanism": "SSRIs ức chế kết tập tiểu cầu nhẹ",
                    "effect": "Tăng nguy cơ chảy máu nhẹ",
                    "management": "Thận trọng. Theo dõi dấu hiệu chảy máu."
                },
                {
                    "drug": "Methotrexate",
                    "mechanism": "Aspirin giảm thải trừ methotrexate",
                    "effect": "Tăng nồng độ methotrexate, tăng độc tính",
                    "management": "Thận trọng. Theo dõi chức năng thận, công thức máu. Có thể cần giảm liều methotrexate."
                }
            ],
            "minor": [
                {
                    "drug": "Acetaminophen",
                    "mechanism": "Có thể tăng nguy cơ chảy máu nhẹ",
                    "effect": "Tăng nguy cơ chảy máu nhẹ",
                    "management": "Thận trọng với liều cao. Theo dõi dấu hiệu chảy máu."
                },
                {
                    "drug": "Ginkgo biloba",
                    "mechanism": "Ginkgo ức chế kết tập tiểu cầu",
                    "effect": "Tăng nguy cơ chảy máu",
                    "management": "Thận trọng. Theo dõi dấu hiệu chảy máu."
                }
            ]
        },
        "contraindications": {
            "absolute": [
                "Loét dạ dày tá tràng đang hoạt động",
                "Chảy máu đang hoạt động",
                "Dị ứng aspirin (phản ứng nghiêm trọng: phù mạch, sốc phản vệ)",
                "Trẻ em <12 tuổi (hội chứng Reye - nguy hiểm tính mạng)",
                "Hemophilia, von Willebrand disease (rối loạn đông máu)"
            ],
            "relative": [
                "Tiền sử loét dạ dày tá tràng (tăng nguy cơ tái phát)",
                "Suy gan nặng (tăng nguy cơ chảy máu)",
                "Suy thận nặng (thận trọng)",
                "Hen phế quản (có thể gây co thắt phế quản - aspirin-sensitive asthma)",
                "Người già (>75 tuổi - tăng nguy cơ chảy máu)",
                "Đang dùng warfarin hoặc thuốc chống đông khác (tăng nguy cơ chảy máu)"
            ]
        },
        "pregnancy_lactation": {
            "fda_category": "C (D trong 3 tháng cuối)",
            "pregnancy_details": "Có thể dùng khi cần thiết trong 3 tháng đầu và giữa. Tránh dùng trong 3 tháng cuối (category D) - có thể gây đóng sớm ống động mạch, chảy máu thai nhi, chảy máu nhau thai, kéo dài chuyển dạ, tăng nguy cơ chảy máu sau sinh. Nếu cần dùng trong 3 tháng cuối: dùng liều thấp (75-100mg) và theo dõi sát.",
            "lactation": {
                "safety": "Compatible",
                "details": "Aspirin bài tiết vào sữa mẹ ở nồng độ thấp. Với liều thấp (75-100mg): an toàn. Với liều cao: có thể gây hội chứng Reye ở trẻ (hiếm).",
                "recommendation": "Có thể dùng liều thấp (75-100mg) khi cho con bú. Tránh liều cao. Theo dõi trẻ nếu có dấu hiệu chảy máu hoặc hội chứng Reye."
            }
        },
        "hepatic_adjustment": {
            "mild": "Không đổi",
            "moderate": "Thận trọng (tăng nguy cơ chảy máu)",
            "severe": "TRÁNH DÙNG hoặc thận trọng (nếu bắt buộc), theo dõi chức năng gan và dấu hiệu chảy máu chặt chẽ",
            "notes": "Aspirin chuyển hóa qua gan. Suy gan làm giảm tổng hợp yếu tố đông máu và có thể ảnh hưởng đến chuyển hóa aspirin. Thận trọng ở bệnh nhân suy gan."
        },
        "overdose_management": {
            "symptoms": [
                "Ù tai, mất thính giác",
                "Buồn nôn, nôn",
                "Chóng mặt",
                "Lú lẫn",
                "Sốt",
                "Thở nhanh",
                "Nhiễm toan chuyển hóa",
                "Hạ đường huyết",
                "Co giật",
                "Hôn mê",
                "Chảy máu (đặc biệt dạ dày ruột)",
                "Suy thận cấp",
                "Tử vong"
            ],
            "antidote": "Không có antidote đặc hiệu. Điều trị hỗ trợ: bù dịch, điện giải, điều chỉnh toan",
            "treatment": [
                "Rửa dạ dày nếu uống trong vòng 1-2 giờ",
                "Than hoạt tính",
                "Điều trị nhiễm toan chuyển hóa: Sodium bicarbonate IV (nếu pH <7.2)",
                "Điều trị hạ đường huyết: Glucose IV",
                "Điều trị co giật: Benzodiazepines (lorazepam, diazepam)",
                "Hỗ trợ hô hấp và tuần hoàn nếu cần",
                "Theo dõi điện giải, glucose, chức năng thận, công thức máu",
                "Theo dõi ít nhất 12-24 giờ"
            ],
            "monitoring": "Điện giải, glucose, khí máu (pH, bicarbonate), chức năng thận (creatinine, BUN), công thức máu (Hct, Hb, tiểu cầu), chức năng gan, ý thức, dấu hiệu chảy máu"
        },
        "reversal_agents": {
            "available": False,
            "agents": []
        },
        "administration_instructions": {
            "oral": {
                "with_food": "Nên uống với thức ăn hoặc sau ăn để giảm kích ứng dạ dày. Uống với nhiều nước.",
                "timing": "Liều thấp (75-100mg): Uống 1 lần/ngày, cùng giờ mỗi ngày. Liều cao (đau, viêm): Uống 3-4 lần/ngày, cách nhau 4-6 giờ. KHÔNG ngừng đột ngột nếu dùng lâu dài (có thể tăng nguy cơ biến cố tim mạch)."
            },
            "iv": {
                "reconstitution": "Không có dạng IV thông thường",
                "infusion_rate": "N/A",
                "compatibility": [],
                "incompatibility": [],
                "notes": "Chỉ có dạng uống"
            }
        },
        "references": {
            "primary_sources": [
                "FDA Drug Label - Aspirin",
                "UpToDate - Aspirin: Drug information",
                "ANTITHROMBOTIC Trialists' Collaboration - The Lancet (2002) - Aspirin trong dự phòng tim mạch",
                "CHARISMA Study - New England Journal of Medicine (2006)",
                "American Heart Association/American College of Cardiology guidelines - Antiplatelet therapy"
            ],
            "last_updated": "2024-12-19",
            "evidence_level": "High - Multiple large RCTs (ANTITHROMBOTIC, CHARISMA) and extensive clinical experience in cardiovascular prevention"
        }
    },
    "Clopidogrel": {
        "group": "Cardiovascular - Antiplatelet (P2Y12 Inhibitor)",
        "vietnamese_name": "Clopidogrel, Plavix",
        "administration": ["PO"],
        "indications": [
            "Sau nhồi máu cơ tim",
            "Sau đặt stent",
            "Hội chứng mạch vành cấp",
            "Đột quỵ/TIA",
            "Bệnh động mạch ngoại biên"
        ],
        "contraindications": [
            "Chảy máu đang hoạt động",
            "Loét dạ dày tá tràng nặng",
            "Dị ứng"
        ],
        "dosage": {
            "adult_loading": "300-600mg x 1 lần",
            "adult_maintenance": "75mg x 1 lần/ngày",
            "notes": "Dùng kèm aspirin sau ACS/stent (dual antiplatelet therapy)"
        },
        "side_effects": [
            "Chảy máu",
            "Giảm tiểu cầu",
            "Tăng nguy cơ xuất huyết",
            "Ban xuất huyết giảm tiểu cầu huyết khối (TTP) - hiếm"
        ],
        "interactions": [
            "Omeprazole: giảm hiệu quả clopidogrel",
            "Aspirin: tăng nguy cơ chảy máu (nhưng có chỉ định)",
            "Warfarin: tăng nguy cơ chảy máu"
        ],
        "pregnancy": "B",
        "mechanism_of_action": "Clopidogrel là prodrug, chuyển hóa thành chất chuyển hóa hoạt tính bởi CYP2C19 (và các CYP khác). Ức chế không hồi phục thụ thể P2Y12 trên tiểu cầu, ngăn chặn kích hoạt tiểu cầu bởi ADP, giảm kết tập tiểu cầu",
        "monitoring": [
            "Dấu hiệu chảy máu (chảy máu chân răng, chảy máu mũi, vết bầm tím, phân đen, nôn ra máu)",
            "Công thức máu nếu nghi ngờ giảm tiểu cầu",
            "Xét nghiệm chức năng tiểu cầu (nếu cần - để đánh giá hiệu quả)",
            "Lưu ý: Một số bệnh nhân có thể kháng clopidogrel do đa hình CYP2C19"
        ],
        "precautions": [
            "Tránh dùng với PPIs mạnh (omeprazole, esomeprazole) - giảm hiệu quả do ức chế CYP2C19",
            "Có thể dùng với pantoprazole, lansoprazole (ít ức chế CYP2C19 hơn)",
            "Dùng kèm aspirin sau ACS/stent: DAPT 12 tháng (hoặc theo hướng dẫn)",
            "Ngừng 5-7 ngày trước phẫu thuật lớn (nếu có thể)",
            "Không ngừng đột ngột sau stent (nguy cơ huyết khối stent)",
            "Một số bệnh nhân kháng clopidogrel: xem xét thay bằng ticagrelor hoặc prasugrel"
        ],
        "pharmacokinetics": {
            "half_life": "Clopidogrel: 6 giờ; Metabolite hoạt tính: 30 phút (nhưng tác dụng kéo dài do ức chế không hồi phục)",
            "onset": "2-8 giờ (sau loading dose 300-600mg)",
            "duration": "5-10 ngày (cho đến khi tiểu cầu mới được tạo ra)",
            "protein_binding": "98%",
            "clearance": "Gan (chuyển hóa qua CYP2C19, CYP3A4, CYP2B6, CYP1A2)"
        },
        "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm",
        "black_box_warnings": "Không ngừng clopidogrel sớm sau đặt stent (đặc biệt drug-eluting stent) - nguy cơ huyết khối stent và tử vong do tim. Chảy máu có thể đe dọa tính mạng",
        "drug_interactions": {
            "major": [
                {
                    "drug": "Omeprazole, Esomeprazole",
                    "mechanism": "Omeprazole/esomeprazole ức chế CYP2C19 (enzyme chuyển hóa clopidogrel thành chất hoạt tính)",
                    "effect": "Giảm hiệu quả clopidogrel mạnh (giảm 40-50% tác dụng), tăng nguy cơ biến cố tim mạch",
                    "management": "TRÁNH DÙNG CHUNG. Thay bằng pantoprazole, lansoprazole (ít ức chế CYP2C19 hơn) hoặc H2 blockers (ranitidine, famotidine)."
                },
                {
                    "drug": "Aspirin",
                    "mechanism": "Tác dụng hiệp đồng ức chế kết tập tiểu cầu",
                    "effect": "Tăng nguy cơ chảy máu (nhưng có chỉ định trong DAPT sau ACS/stent)",
                    "management": "Dùng kèm sau ACS/stent: DAPT 12 tháng (hoặc theo hướng dẫn). Theo dõi dấu hiệu chảy máu chặt chẽ. Cân nhắc dùng PPI (pantoprazole, lansoprazole)."
                },
                {
                    "drug": "Warfarin",
                    "mechanism": "Tác dụng hiệp đồng ức chế đông máu",
                    "effect": "Tăng nguy cơ chảy máu nặng",
                    "management": "TRÁNH DÙNG CHUNG nếu có thể. Nếu cần: theo dõi INR và dấu hiệu chảy máu chặt chẽ."
                }
            ],
            "moderate": [
                {
                    "drug": "Fluconazole, Voriconazole",
                    "mechanism": "Ức chế CYP2C19, giảm chuyển hóa clopidogrel",
                    "effect": "Giảm hiệu quả clopidogrel",
                    "management": "Thận trọng. Theo dõi hiệu quả. Có thể cần tăng liều clopidogrel hoặc thay bằng ticagrelor/prasugrel."
                },
                {
                    "drug": "Ciprofloxacin, Fluoroquinolones",
                    "mechanism": "Có thể ức chế CYP2C19 nhẹ",
                    "effect": "Giảm hiệu quả clopidogrel nhẹ",
                    "management": "Thận trọng. Theo dõi hiệu quả."
                },
                {
                    "drug": "NSAIDs (ibuprofen, naproxen)",
                    "mechanism": "NSAIDs gây loét dạ dày, tăng nguy cơ chảy máu",
                    "effect": "Tăng nguy cơ chảy máu dạ dày ruột",
                    "management": "Thận trọng. Cân nhắc dùng PPI. Theo dõi dấu hiệu chảy máu dạ dày."
                },
                {
                    "drug": "SSRIs (fluoxetine, sertraline)",
                    "mechanism": "SSRIs ức chế kết tập tiểu cầu nhẹ",
                    "effect": "Tăng nguy cơ chảy máu nhẹ",
                    "management": "Thận trọng. Theo dõi dấu hiệu chảy máu."
                }
            ],
            "minor": [
                {
                    "drug": "Atorvastatin (liều cao)",
                    "mechanism": "Có thể ức chế CYP3A4 nhẹ",
                    "effect": "Giảm hiệu quả clopidogrel nhẹ (không rõ ràng)",
                    "management": "Thận trọng. Theo dõi hiệu quả."
                },
                {
                    "drug": "Ginkgo biloba",
                    "mechanism": "Ginkgo ức chế kết tập tiểu cầu",
                    "effect": "Tăng nguy cơ chảy máu",
                    "management": "Thận trọng. Theo dõi dấu hiệu chảy máu."
                }
            ]
        },
        "contraindications": {
            "absolute": [
                "Chảy máu đang hoạt động",
                "Loét dạ dày tá tràng nặng đang hoạt động",
                "Dị ứng clopidogrel (phản ứng nghiêm trọng: phù mạch, sốc phản vệ)",
                "Hemophilia, von Willebrand disease (rối loạn đông máu)"
            ],
            "relative": [
                "Tiền sử loét dạ dày tá tràng (tăng nguy cơ chảy máu)",
                "Suy gan nặng (tăng nguy cơ chảy máu)",
                "Suy thận nặng (thận trọng)",
                "Người già (>75 tuổi - tăng nguy cơ chảy máu)",
                "Đang dùng warfarin hoặc thuốc chống đông khác (tăng nguy cơ chảy máu)",
                "Đa hình CYP2C19 poor metabolizer (giảm hiệu quả - xem xét thay bằng ticagrelor/prasugrel)"
            ]
        },
        "pregnancy_lactation": {
            "fda_category": "B",
            "pregnancy_details": "Có thể dùng khi cần thiết. Clopidogrel đi qua nhau thai. Không có dữ liệu đầy đủ về an toàn trong thai kỳ. Có thể tăng nguy cơ chảy máu thai nhi, chảy máu nhau thai. Cân nhắc lợi ích/nguy cơ. Nếu cần dùng: theo dõi sát thai nhi và dấu hiệu chảy máu.",
            "lactation": {
                "safety": "Compatible (có thể)",
                "details": "Clopidogrel bài tiết vào sữa mẹ ở nồng độ thấp. Nồng độ trong máu trẻ bú mẹ thường rất thấp. Không có báo cáo về tác dụng phụ nghiêm trọng ở trẻ bú mẹ.",
                "recommendation": "Có thể dùng khi cho con bú. Theo dõi trẻ nếu có dấu hiệu chảy máu."
            }
        },
        "hepatic_adjustment": {
            "mild": "Không đổi",
            "moderate": "Thận trọng (clopidogrel chuyển hóa qua gan)",
            "severe": "Thận trọng (nếu bắt buộc), theo dõi chức năng gan và dấu hiệu chảy máu chặt chẽ",
            "notes": "Clopidogrel chuyển hóa qua gan (CYP2C19, CYP3A4, CYP2B6, CYP1A2) thành chất hoạt tính. Suy gan có thể ảnh hưởng đến chuyển hóa. Thận trọng ở bệnh nhân suy gan."
        },
        "overdose_management": {
            "symptoms": [
                "Chảy máu (chảy máu chân răng, chảy máu mũi, vết bầm tím, phân đen, nôn ra máu)",
                "Chảy máu nặng (xuất huyết nội sọ, xuất huyết tiêu hóa, chảy máu nội tạng)",
                "Giảm tiểu cầu",
                "Ban xuất huyết giảm tiểu cầu huyết khối (TTP) - hiếm nhưng nguy hiểm"
            ],
            "antidote": "Không có antidote đặc hiệu. Điều trị hỗ trợ: truyền tiểu cầu (nếu chảy máu nặng), hỗ trợ hô hấp và tuần hoàn",
            "treatment": [
                "Rửa dạ dày nếu uống trong vòng 1-2 giờ",
                "Than hoạt tính",
                "Điều trị chảy máu nặng: Truyền tiểu cầu (nếu cần), Fresh Frozen Plasma (FFP), hỗ trợ hô hấp và tuần hoàn",
                "Theo dõi công thức máu (Hct, Hb, tiểu cầu), dấu hiệu chảy máu",
                "Theo dõi ít nhất 5-10 ngày (do tác dụng kéo dài 5-10 ngày cho đến khi tiểu cầu mới được tạo ra)"
            ],
            "monitoring": "Công thức máu (Hct, Hb, tiểu cầu), dấu hiệu chảy máu (chảy máu chân răng, chảy máu mũi, vết bầm tím, phân đen, nôn ra máu), chức năng thận, gan, ý thức"
        },
        "reversal_agents": {
            "available": False,
            "agents": []
        },
        "administration_instructions": {
            "oral": {
                "with_food": "Có thể uống với hoặc không có thức ăn. Không ảnh hưởng đáng kể đến hấp thu.",
                "timing": "Uống 1 lần/ngày, cùng giờ mỗi ngày. Loading dose: 300-600mg x 1 lần (sau ACS/stent). Maintenance: 75mg x 1 lần/ngày. KHÔNG ngừng đột ngột sau stent (nguy cơ huyết khối stent). Nếu cần ngừng: ngừng 5-7 ngày trước phẫu thuật lớn."
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
                "FDA Drug Label - Plavix (clopidogrel)",
                "UpToDate - Clopidogrel: Drug information",
                "CURE Study - New England Journal of Medicine (2001) - Clopidogrel trong ACS",
                "CREDO Study - JAMA (2002) - Clopidogrel sau PCI",
                "American Heart Association/American College of Cardiology guidelines - Antiplatelet therapy"
            ],
            "last_updated": "2024-12-19",
            "evidence_level": "High - Multiple large RCTs (CURE, CREDO) and extensive clinical experience in cardiovascular disease"
        }
    },
    # Statins
    "Atorvastatin": {
        "group": "Cardiovascular - Statin (HMG-CoA Reductase Inhibitor)",
        "vietnamese_name": "Atorvastatin, Lipitor",
        "administration": ["PO"],
        "indications": [
            "Tăng cholesterol máu",
            "Dự phòng biến cố tim mạch",
            "Sau nhồi máu cơ tim",
            "Bệnh động mạch vành"
        ],
        "contraindications": [
            "Bệnh gan hoạt động",
            "Có thai",
            "Cho con bú",
            "Tiêu cơ vân đang hoạt động"
        ],
        "dosage": {
            "adult_standard": "10-80mg x 1 lần/ngày",
            "adult_high_intensity": "40-80mg x 1 lần/ngày",
            "notes": "Uống bất kỳ lúc nào trong ngày, có thể uống với thức ăn"
        },
        "side_effects": [
            "Đau cơ",
            "Tiêu cơ vân (hiếm nhưng nguy hiểm)",
            "Tăng men gan",
            "Tăng đường huyết",
            "Suy giảm trí nhớ (hiếm)"
        ],
        "interactions": [
            "Clarithromycin/Erythromycin: tăng nguy cơ tiêu cơ vân",
            "Grapefruit juice: tăng nồng độ (với liều cao)",
            "Cyclosporine: tăng nguy cơ tiêu cơ vân"
        ],
        "pregnancy": "X",
        "mechanism_of_action": "Ức chế HMG-CoA reductase, enzyme chính trong tổng hợp cholesterol, dẫn đến giảm LDL-cholesterol và tăng HDL-cholesterol",
        "monitoring": [
            "Lipid profile (LDL, HDL, TG) sau 6-8 tuần, sau đó mỗi 3-6 tháng",
            "AST/ALT trước điều trị, sau 12 tuần, sau đó mỗi 6-12 tháng",
            "CK nếu có đau cơ, yếu cơ",
            "HbA1c/đường huyết (statin có thể tăng đường huyết)"
        ],
        "precautions": [
            "Kiểm tra CK nếu đau cơ hoặc yếu cơ (ngừng nếu CK >10 lần ULN)",
            "Ngừng nếu ALT >3 lần ULN",
            "Thận trọng với bệnh nhân đái tháo đường (có thể tăng đường huyết)",
            "Tránh grapefruit juice với liều cao"
        ],
        "pharmacokinetics": {
            "half_life": "14 giờ",
            "onset": "1-2 tuần",
            "duration": "24 giờ",
            "protein_binding": ">98%",
            "clearance": "Gan (CYP3A4)"
        },
        "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm",
        "black_box_warnings": "Tiêu cơ vân - có thể gây suy thận cấp và tử vong. Nguy cơ tăng khi dùng chung với thuốc khác hoặc liều cao",
        "drug_interactions": {
            "major": [
                {
                    "drug": "Cyclosporine, Tacrolimus",
                    "mechanism": "Cyclosporine ức chế CYP3A4 và P-glycoprotein, tăng nồng độ atorvastatin đáng kể",
                    "effect": "Tăng nguy cơ tiêu cơ vân (rhabdomyolysis) nghiêm trọng, có thể gây suy thận cấp, tử vong",
                    "management": "CHỐNG CHỈ ĐỊNH dùng cùng. Nếu cần: giảm liều atorvastatin tối đa 10mg/ngày, theo dõi CK và men gan thường xuyên. Cân nhắc dùng pravastatin hoặc rosuvastatin (ít chuyển hóa qua CYP3A4)."
                },
                {
                    "drug": "Clarithromycin, Erythromycin, Telithromycin",
                    "mechanism": "Macrolide ức chế CYP3A4, tăng nồng độ atorvastatin",
                    "effect": "Tăng nguy cơ tiêu cơ vân, đặc biệt ở liều cao atorvastatin",
                    "management": "Tránh dùng cùng nếu có thể. Nếu cần: giảm liều atorvastatin 50-75%, theo dõi CK và dấu hiệu đau cơ. Tạm ngừng atorvastatin nếu có đau cơ hoặc CK tăng."
                },
                {
                    "drug": "Itraconazole, Ketoconazole, Voriconazole, Posaconazole",
                    "mechanism": "Azole antifungals ức chế CYP3A4 mạnh, tăng nồng độ atorvastatin",
                    "effect": "Tăng nguy cơ tiêu cơ vân nghiêm trọng",
                    "management": "CHỐNG CHỈ ĐỊNH dùng cùng. Tạm ngừng atorvastatin trong thời gian dùng azole antifungal. Hoặc dùng pravastatin/rosuvastatin (ít chuyển hóa qua CYP3A4)."
                },
                {
                    "drug": "Grapefruit juice (lớn hơn 1.2L/ngày hoặc liều cao atorvastatin)",
                    "mechanism": "Grapefruit juice ức chế CYP3A4 ở ruột, tăng hấp thu atorvastatin",
                    "effect": "Tăng nồng độ atorvastatin, tăng nguy cơ tiêu cơ vân",
                    "management": "Tránh grapefruit juice khi dùng atorvastatin, đặc biệt ở liều cao (40-80mg). Nước ép cam, táo không có vấn đề."
                }
            ],
            "moderate": [
                {
                    "drug": "Amiodarone, Diltiazem, Verapamil",
                    "mechanism": "Ức chế CYP3A4, tăng nồng độ atorvastatin",
                    "effect": "Tăng nguy cơ tiêu cơ vân",
                    "management": "Giảm liều atorvastatin 50% hoặc tối đa 20mg/ngày. Theo dõi CK và dấu hiệu đau cơ. Cân nhắc dùng pravastatin/rosuvastatin."
                },
                {
                    "drug": "Ritonavir, Lopinavir, Saquinavir (HIV protease inhibitors)",
                    "mechanism": "Ức chế CYP3A4 mạnh, tăng nồng độ atorvastatin",
                    "effect": "Tăng nguy cơ tiêu cơ vân",
                    "management": "Giảm liều atorvastatin. Theo dõi CK. Cân nhắc dùng pravastatin hoặc rosuvastatin."
                },
                {
                    "drug": "Warfarin",
                    "mechanism": "Atorvastatin có thể tăng tác dụng chống đông của warfarin",
                    "effect": "Tăng INR, tăng nguy cơ chảy máu",
                    "management": "Theo dõi INR thường xuyên khi bắt đầu hoặc thay đổi liều atorvastatin. Có thể cần giảm liều warfarin."
                },
                {
                    "drug": "Digoxin",
                    "mechanism": "Atorvastatin có thể tăng nhẹ nồng độ digoxin qua P-glycoprotein",
                    "effect": "Tăng nhẹ nồng độ digoxin",
                    "management": "Theo dõi nồng độ digoxin và dấu hiệu ngộ độc digoxin. Có thể cần giảm liều digoxin."
                },
                {
                    "drug": "Colchicine",
                    "mechanism": "Cả hai đều chuyển hóa qua CYP3A4, có thể tăng tác dụng phụ",
                    "effect": "Tăng nguy cơ độc cơ, đặc biệt ở bệnh nhân suy thận",
                    "management": "Thận trọng, đặc biệt ở bệnh nhân suy thận. Theo dõi CK và dấu hiệu đau cơ. Có thể cần giảm liều một trong hai thuốc."
                }
            ],
            "minor": [
                {
                    "drug": "Rifampin, Phenytoin",
                    "mechanism": "Cảm ứng CYP3A4, tăng chuyển hóa atorvastatin",
                    "effect": "Giảm hiệu quả atorvastatin",
                    "management": "Có thể cần tăng liều atorvastatin. Theo dõi lipid profile."
                },
                {
                    "drug": "Oral contraceptives",
                    "mechanism": "Atorvastatin có thể tăng nhẹ nồng độ estrogen",
                    "effect": "Tăng nhẹ tác dụng phụ của thuốc tránh thai",
                    "management": "Thường không cần điều chỉnh. Theo dõi tác dụng phụ."
                }
            ]
        },
        "contraindications": {
            "absolute": [
                "Bệnh gan hoạt động (active liver disease) - tăng men gan kéo dài, viêm gan",
                "Có thai (pregnancy) - FDA category X, gây dị tật thai nhi",
                "Cho con bú (lactation) - bài tiết vào sữa mẹ",
                "Tiêu cơ vân đang hoạt động (active myopathy/rhabdomyolysis)",
                "Dị ứng với atorvastatin hoặc bất kỳ thành phần nào",
                "Dùng cùng cyclosporine, itraconazole, ketoconazole (tăng nguy cơ tiêu cơ vân nghiêm trọng)"
            ],
            "relative": [
                "Suy thận - thận trọng, giảm liều nếu cần",
                "Suy gan - thận trọng, theo dõi men gan thường xuyên",
                "Uống rượu nhiều - tăng nguy cơ viêm gan",
                "Bệnh nhân Châu Á - tăng nồng độ atorvastatin, có thể cần liều thấp hơn",
                "Người cao tuổi - tăng nguy cơ đau cơ, tiêu cơ vân",
                "Đái tháo đường - statins có thể tăng đường huyết nhẹ",
                "Bệnh tuyến giáp - tăng nguy cơ đau cơ",
                "Dùng cùng thuốc ức chế CYP3A4 - giảm liều atorvastatin"
            ]
        },
        "pregnancy_lactation": {
            "fda_category": "X",
            "pregnancy_details": "CHỐNG CHỈ ĐỊNH trong thai kỳ. Atorvastatin gây dị tật thai nhi, đặc biệt trong tam cá nguyệt đầu tiên. Statins ức chế tổng hợp cholesterol, cần thiết cho sự phát triển của thai nhi. Có thể gây dị tật bẩm sinh, chậm phát triển. Phải ngừng atorvastatin ít nhất 1-2 tháng trước khi có thai. Nếu có thai khi đang dùng, ngừng ngay lập tức.",
            "lactation": {
                "safety": "Incompatible",
                "details": "Atorvastatin bài tiết vào sữa mẹ. Có thể gây tác dụng phụ trên trẻ bú mẹ. Chưa có dữ liệu đầy đủ về an toàn. Statins có thể ảnh hưởng đến sự phát triển của trẻ.",
                "recommendation": "CHỐNG CHỈ ĐỊNH khi cho con bú. Ngừng atorvastatin hoặc ngừng cho con bú. Cân nhắc thuốc thay thế nếu cần."
            }
        },
        "hepatic_adjustment": {
            "mild": "Không đổi liều. Theo dõi men gan thường xuyên.",
            "moderate": "Thận trọng. Giảm liều hoặc dùng liều thấp hơn. Theo dõi men gan mỗi 3-6 tháng. Ngừng nếu ALT >3 lần ULN.",
            "severe": "CHỐNG CHỈ ĐỊNH. Không dùng ở bệnh nhân suy gan nặng hoặc bệnh gan hoạt động.",
            "notes": "Atorvastatin chuyển hóa qua gan (CYP3A4). Suy gan có thể làm tăng nồng độ atorvastatin và tăng nguy cơ độc tính. Kiểm tra men gan trước điều trị. Ngừng nếu ALT >3 lần ULN hoặc có dấu hiệu viêm gan."
        },
        "overdose_management": {
            "symptoms": [
                "Tiêu cơ vân (rhabdomyolysis) - triệu chứng chính và nguy hiểm nhất",
                "Đau cơ dữ dội, yếu cơ",
                "Nước tiểu sẫm màu (myoglobinuria)",
                "Suy thận cấp (do myoglobin)",
                "Tăng men gan (ALT, AST)",
                "Tăng CK (creatine kinase)",
                "Mệt mỏi, buồn nôn",
                "Rối loạn tiêu hóa"
            ],
            "antidote": "Không có antidote đặc hiệu. Điều trị hỗ trợ: ngừng atorvastatin, truyền dịch tích cực để phòng suy thận, lọc máu nếu cần",
            "treatment": [
                "Ngừng atorvastatin ngay lập tức",
                "Đo CK, men gan, chức năng thận ngay",
                "Nếu có tiêu cơ vân:",
                "  - Truyền dịch tích cực (normal saline 1-2L/giờ) để duy trì lượng nước tiểu >100-200ml/giờ",
                "  - Kiềm hóa nước tiểu (sodium bicarbonate) để giảm độc tính myoglobin trên thận",
                "  - Theo dõi chức năng thận (creatinine, BUN, lượng nước tiểu)",
                "  - Hemodialysis nếu suy thận cấp, tăng kali máu, hoặc quá tải dịch",
                "  - Theo dõi điện giải (natri, kali, canxi, phosphate)",
                "Điều trị hỗ trợ:",
                "  - Điều chỉnh rối loạn điện giải",
                "  - Hỗ trợ hô hấp và tuần hoàn nếu cần",
                "  - Giảm đau (opioids) nếu đau cơ nặng",
                "Theo dõi CK, men gan, chức năng thận hàng ngày cho đến khi ổn định",
                "Theo dõi ít nhất 48-72 giờ do half-life 14 giờ"
            ],
            "monitoring": "CK, ALT, AST, creatinine, BUN, kali, canxi, phosphate, lượng nước tiểu, ECG (nếu có rối loạn điện giải), dấu hiệu suy thận"
        },
        "reversal_agents": {
            "available": False,
            "agents": []
        },
        "administration_instructions": {
            "oral": {
                "with_food": "Có thể uống với hoặc không có thức ăn. Không ảnh hưởng đáng kể đến hấp thu.",
                "timing": "Uống 1 lần/ngày, bất kỳ lúc nào trong ngày (sáng, trưa, hoặc tối). Uống cùng một giờ mỗi ngày để nhớ. Có thể uống trước hoặc sau bữa ăn."
            },
            "iv": {
                "reconstitution": "Không có dạng IV",
                "infusion_rate": "Không áp dụng",
                "compatibility": [],
                "incompatibility": [],
                "notes": "Atorvastatin chỉ có dạng uống (PO)."
            }
        },
        "references": {
            "primary_sources": [
                "FDA Drug Label - Lipitor (atorvastatin)",
                "UpToDate - Atorvastatin: Drug information",
                "ACC/AHA Guidelines - Cholesterol Management (2018)",
                "NLA Guidelines - Statin Safety (2014)",
                "Goodman & Gilman's Pharmacological Basis of Therapeutics - Lipid-lowering drugs"
            ],
            "last_updated": "2024-12-19",
            "evidence_level": "High - Multiple large RCTs (ASCOT, CARDS, PROVE-IT) showing cardiovascular benefit"
        }
    },
    "Simvastatin": {
        "group": "Cardiovascular - Statin",
        "vietnamese_name": "Simvastatin, Zocor",
        "administration": ["PO"],
        "indications": [
            "Tăng cholesterol máu",
            "Dự phòng biến cố tim mạch"
        ],
        "contraindications": [
            "Bệnh gan hoạt động",
            "Có thai",
            "Cho con bú"
        ],
        "dosage": {
            "adult_standard": "10-40mg x 1 lần/ngày",
            "adult_max": "80mg x 1 lần/ngày (hiếm dùng)",
            "notes": "Uống buổi tối, tránh grapefruit juice"
        },
        "side_effects": [
            "Đau cơ",
            "Tiêu cơ vân",
            "Tăng men gan"
        ],
                  "interactions": [
              "Amiodarone: giảm liều simvastatin xuống tối đa 20mg/ngày",
              "Verapamil: giảm liều simvastatin",
              "Grapefruit juice: tăng nồng độ"
          ],
          "pregnancy": "X",
          "mechanism_of_action": "HMG-CoA reductase inhibitor (statin). Ức chế enzyme HMG-CoA reductase - enzyme quan trọng trong tổng hợp cholesterol ở gan. Giảm sản xuất cholesterol nội sinh, tăng biểu hiện LDL receptor ở gan, giảm LDL cholesterol. Cũng có tác dụng chống viêm, ổn định mảng xơ vữa (pleiotropic effects).",
          "monitoring": [
              "Lipid panel: Cholesterol toàn phần, LDL, HDL, triglycerides (sau 4-8 tuần, sau đó mỗi 3-6 tháng)",
              "Chức năng gan: ALT, AST (trước khi bắt đầu, sau 12 tuần, sau đó mỗi 6-12 tháng hoặc khi có triệu chứng)",
              "CK (creatine kinase) - nếu có đau cơ, yếu cơ (để phát hiện tiêu cơ vân)",
              "Glucose/HbA1c - statins có thể tăng đường huyết nhẹ",
              "Dấu hiệu đau cơ, yếu cơ, nước tiểu sẫm màu (dấu hiệu tiêu cơ vân)"
          ],
          "precautions": [
              "Uống buổi tối (cholesterol được tổng hợp nhiều vào ban đêm)",
              "TRÁNH grapefruit juice (ức chế CYP3A4, tăng nồng độ, tăng nguy cơ tác dụng phụ)",
              "Kiểm tra CK nếu có đau cơ/yếu cơ - ngừng ngay nếu CK >10x ULN hoặc có dấu hiệu tiêu cơ vân",
              "Thận trọng với liều cao (>40mg/ngày) - tăng nguy cơ tiêu cơ vân",
              "Giảm liều khi dùng với amiodarone, verapamil, diltiazem, macrolides, azole antifungals (tương tác CYP3A4)",
              "CHỐNG CHỈ ĐỊNH trong thai kỳ và cho con bú (category X)",
              "Thận trọng ở bệnh nhân có bệnh gan - kiểm tra ALT/AST trước khi bắt đầu",
              "Có thể tăng đường huyết nhẹ (đặc biệt ở bệnh nhân đái tháo đường)"
          ],
          "pharmacokinetics": {
              "half_life": "2-3 giờ (ngắn), nhưng tác dụng kéo dài do ức chế enzyme)",
              "onset": "1-2 tuần (giảm LDL)",
              "duration": "Kéo dài sau khi ngừng",
              "protein_binding": "95%",
              "clearance": "Gan (CYP3A4) - extensive first-pass metabolism"
          },
          "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm, tránh ánh sáng",
          "black_box_warnings": "CHỐNG CHỈ ĐỊNH trong thai kỳ - có thể gây dị tật thai nhi. Phụ nữ trong độ tuổi sinh đẻ phải dùng biện pháp tránh thai hiệu quả. Tiêu cơ vân có thể gây suy thận cấp và tử vong - ngừng ngay nếu có đau cơ, yếu cơ, nước tiểu sẫm màu",
          "drug_interactions": {
              "major": [
                  {
                      "drug": "Cyclosporine, Tacrolimus",
                      "mechanism": "Cyclosporine ức chế CYP3A4 và P-glycoprotein, tăng nồng độ simvastatin đáng kể",
                      "effect": "Tăng nguy cơ tiêu cơ vân nghiêm trọng, có thể gây suy thận cấp, tử vong",
                      "management": "CHỐNG CHỈ ĐỊNH dùng cùng. Nếu cần: giảm liều simvastatin tối đa 10mg/ngày, theo dõi CK và men gan thường xuyên. Cân nhắc dùng pravastatin hoặc rosuvastatin (ít chuyển hóa qua CYP3A4)."
                  },
                  {
                      "drug": "Itraconazole, Ketoconazole, Voriconazole, Posaconazole",
                      "mechanism": "Azole antifungals ức chế CYP3A4 mạnh, tăng nồng độ simvastatin",
                      "effect": "Tăng nguy cơ tiêu cơ vân nghiêm trọng",
                      "management": "CHỐNG CHỈ ĐỊNH dùng cùng. Tạm ngừng simvastatin trong thời gian dùng azole antifungal. Hoặc dùng pravastatin/rosuvastatin (ít chuyển hóa qua CYP3A4)."
                  },
                  {
                      "drug": "Clarithromycin, Erythromycin, Telithromycin",
                      "mechanism": "Macrolide ức chế CYP3A4, tăng nồng độ simvastatin",
                      "effect": "Tăng nguy cơ tiêu cơ vân, đặc biệt ở liều cao simvastatin",
                      "management": "Tránh dùng cùng nếu có thể. Nếu cần: giảm liều simvastatin hoặc tạm ngừng. Theo dõi CK và dấu hiệu đau cơ. Tạm ngừng simvastatin nếu có đau cơ hoặc CK tăng."
                  },
                  {
                      "drug": "Grapefruit juice",
                      "mechanism": "Grapefruit juice ức chế CYP3A4 ở ruột, tăng hấp thu simvastatin",
                      "effect": "Tăng nồng độ simvastatin đáng kể, tăng nguy cơ tiêu cơ vân",
                      "management": "CHỐNG CHỈ ĐỊNH dùng grapefruit juice khi dùng simvastatin. Tránh hoàn toàn, kể cả lượng nhỏ. Nước ép cam, táo không có vấn đề."
                  },
                  {
                      "drug": "Amiodarone",
                      "mechanism": "Amiodarone ức chế CYP3A4, tăng nồng độ simvastatin",
                      "effect": "Tăng nguy cơ tiêu cơ vân, đặc biệt ở liều cao simvastatin",
                      "management": "Giảm liều simvastatin xuống TỐI ĐA 20mg/ngày. Theo dõi CK và dấu hiệu đau cơ. Cân nhắc dùng pravastatin hoặc rosuvastatin (ít chuyển hóa qua CYP3A4)."
                  }
              ],
              "moderate": [
                  {
                      "drug": "Diltiazem, Verapamil",
                      "mechanism": "Ức chế CYP3A4, tăng nồng độ simvastatin",
                      "effect": "Tăng nguy cơ tiêu cơ vân",
                      "management": "Giảm liều simvastatin 50% hoặc tối đa 20mg/ngày. Theo dõi CK và dấu hiệu đau cơ. Cân nhắc dùng pravastatin/rosuvastatin."
                  },
                  {
                      "drug": "Ritonavir, Lopinavir, Saquinavir (HIV protease inhibitors)",
                      "mechanism": "Ức chế CYP3A4 mạnh, tăng nồng độ simvastatin",
                      "effect": "Tăng nguy cơ tiêu cơ vân",
                      "management": "CHỐNG CHỈ ĐỊNH dùng cùng. Cân nhắc dùng pravastatin hoặc rosuvastatin."
                  },
                  {
                      "drug": "Warfarin",
                      "mechanism": "Simvastatin có thể tăng tác dụng chống đông của warfarin",
                      "effect": "Tăng INR, tăng nguy cơ chảy máu",
                      "management": "Theo dõi INR thường xuyên khi bắt đầu hoặc thay đổi liều simvastatin. Có thể cần giảm liều warfarin."
                  },
                  {
                      "drug": "Colchicine",
                      "mechanism": "Cả hai đều chuyển hóa qua CYP3A4, có thể tăng tác dụng phụ",
                      "effect": "Tăng nguy cơ độc cơ, đặc biệt ở bệnh nhân suy thận",
                      "management": "Thận trọng, đặc biệt ở bệnh nhân suy thận. Theo dõi CK và dấu hiệu đau cơ. Có thể cần giảm liều một trong hai thuốc."
                  }
              ],
              "minor": [
                  {
                      "drug": "Rifampin, Phenytoin",
                      "mechanism": "Cảm ứng CYP3A4, tăng chuyển hóa simvastatin",
                      "effect": "Giảm hiệu quả simvastatin",
                      "management": "Có thể cần tăng liều simvastatin. Theo dõi lipid profile."
                  }
              ]
          },
          "contraindications": {
              "absolute": [
                  "Bệnh gan hoạt động (active liver disease) - tăng men gan kéo dài, viêm gan",
                  "Có thai (pregnancy) - FDA category X, gây dị tật thai nhi",
                  "Cho con bú (lactation) - bài tiết vào sữa mẹ",
                  "Tiêu cơ vân đang hoạt động (active myopathy/rhabdomyolysis)",
                  "Dị ứng với simvastatin hoặc bất kỳ thành phần nào",
                  "Dùng cùng cyclosporine, itraconazole, ketoconazole (tăng nguy cơ tiêu cơ vân nghiêm trọng)",
                  "Dùng grapefruit juice"
              ],
              "relative": [
                  "Suy thận - thận trọng, giảm liều nếu cần",
                  "Suy gan - thận trọng, theo dõi men gan thường xuyên",
                  "Uống rượu nhiều - tăng nguy cơ viêm gan",
                  "Người cao tuổi - tăng nguy cơ đau cơ, tiêu cơ vân",
                  "Đái tháo đường - statins có thể tăng đường huyết nhẹ",
                  "Bệnh tuyến giáp - tăng nguy cơ đau cơ",
                  "Dùng cùng thuốc ức chế CYP3A4 - giảm liều simvastatin",
                  "Liều cao (>40mg/ngày) - tăng nguy cơ tiêu cơ vân"
              ]
          },
          "pregnancy_lactation": {
              "fda_category": "X",
              "pregnancy_details": "CHỐNG CHỈ ĐỊNH trong thai kỳ. Simvastatin gây dị tật thai nhi, đặc biệt trong tam cá nguyệt đầu tiên. Statins ức chế tổng hợp cholesterol, cần thiết cho sự phát triển của thai nhi. Có thể gây dị tật bẩm sinh, chậm phát triển. Phụ nữ trong độ tuổi sinh đẻ phải dùng biện pháp tránh thai hiệu quả. Phải ngừng simvastatin ít nhất 1-2 tháng trước khi có thai. Nếu có thai khi đang dùng, ngừng ngay lập tức.",
              "lactation": {
                  "safety": "Incompatible",
                  "details": "Simvastatin bài tiết vào sữa mẹ. Có thể gây tác dụng phụ trên trẻ bú mẹ. Chưa có dữ liệu đầy đủ về an toàn. Statins có thể ảnh hưởng đến sự phát triển của trẻ.",
                  "recommendation": "CHỐNG CHỈ ĐỊNH khi cho con bú. Ngừng simvastatin hoặc ngừng cho con bú. Cân nhắc thuốc thay thế nếu cần."
              }
          },
          "hepatic_adjustment": {
              "mild": "Không đổi liều. Theo dõi men gan thường xuyên.",
              "moderate": "Thận trọng. Giảm liều hoặc dùng liều thấp hơn. Theo dõi men gan mỗi 3-6 tháng. Ngừng nếu ALT >3 lần ULN.",
              "severe": "CHỐNG CHỈ ĐỊNH. Không dùng ở bệnh nhân suy gan nặng hoặc bệnh gan hoạt động.",
              "notes": "Simvastatin chuyển hóa qua gan (CYP3A4) - extensive first-pass metabolism. Suy gan có thể làm tăng nồng độ simvastatin và tăng nguy cơ độc tính. Kiểm tra men gan trước điều trị. Ngừng nếu ALT >3 lần ULN hoặc có dấu hiệu viêm gan."
          },
          "overdose_management": {
              "symptoms": [
                  "Tiêu cơ vân (rhabdomyolysis) - triệu chứng chính và nguy hiểm nhất",
                  "Đau cơ dữ dội, yếu cơ",
                  "Nước tiểu sẫm màu (myoglobinuria)",
                  "Suy thận cấp (do myoglobin)",
                  "Tăng men gan (ALT, AST)",
                  "Tăng CK (creatine kinase)",
                  "Mệt mỏi, buồn nôn",
                  "Rối loạn tiêu hóa"
              ],
              "antidote": "Không có antidote đặc hiệu. Điều trị hỗ trợ: ngừng simvastatin, truyền dịch tích cực để phòng suy thận, lọc máu nếu cần",
              "treatment": [
                  "Ngừng simvastatin ngay lập tức",
                  "Đo CK, men gan, chức năng thận ngay",
                  "Nếu có tiêu cơ vân:",
                  "  - Truyền dịch tích cực (normal saline 1-2L/giờ) để duy trì lượng nước tiểu >100-200ml/giờ",
                  "  - Kiềm hóa nước tiểu (sodium bicarbonate) để giảm độc tính myoglobin trên thận",
                  "  - Theo dõi chức năng thận (creatinine, BUN, lượng nước tiểu)",
                  "  - Hemodialysis nếu suy thận cấp, tăng kali máu, hoặc quá tải dịch",
                  "  - Theo dõi điện giải (natri, kali, canxi, phosphate)",
                  "Điều trị hỗ trợ:",
                  "  - Điều chỉnh rối loạn điện giải",
                  "  - Hỗ trợ hô hấp và tuần hoàn nếu cần",
                  "  - Giảm đau (opioids) nếu đau cơ nặng",
                  "Theo dõi CK, men gan, chức năng thận hàng ngày cho đến khi ổn định",
                  "Theo dõi ít nhất 24-48 giờ do half-life 2-3 giờ (nhưng tác dụng kéo dài)"
              ],
              "monitoring": "CK, ALT, AST, creatinine, BUN, kali, canxi, phosphate, lượng nước tiểu, ECG (nếu có rối loạn điện giải), dấu hiệu suy thận"
          },
          "reversal_agents": {
              "available": False,
              "agents": []
          },
          "administration_instructions": {
              "oral": {
                  "with_food": "Có thể uống với hoặc không có thức ăn. Không ảnh hưởng đáng kể đến hấp thu.",
                  "timing": "Uống 1 lần/ngày vào BUỔI TỐI (cholesterol được tổng hợp nhiều vào ban đêm). Uống cùng một giờ mỗi ngày để nhớ. TRÁNH grapefruit juice hoàn toàn."
              },
              "iv": {
                  "reconstitution": "Không có dạng IV",
                  "infusion_rate": "Không áp dụng",
                  "compatibility": [],
                  "incompatibility": [],
                  "notes": "Simvastatin chỉ có dạng uống (PO)."
              }
          },
          "references": {
              "primary_sources": [
                  "FDA Drug Label - Zocor (simvastatin)",
                  "UpToDate - Simvastatin: Drug information",
                  "ACC/AHA Guidelines - Cholesterol Management (2018)",
                  "NLA Guidelines - Statin Safety (2014)",
                  "4S Study - Lancet (1994) - Simvastatin trong dự phòng biến cố tim mạch",
                  "Goodman & Gilman's Pharmacological Basis of Therapeutics - Lipid-lowering drugs"
              ],
              "last_updated": "2024-12-19",
              "evidence_level": "High - Multiple large RCTs (4S, HPS) showing cardiovascular benefit"
          }
      },

"Spironolactone": {
    "group": "Cardiovascular - Aldosterone Antagonist (Potassium-sparing Diuretic)",
    "vietnamese_name": "Spironolactone, Aldactone",
    "administration": ["PO"],
    "indications": [
        "Suy tim (NYHA class II-IV)",
        "Xơ gan với cổ trướng",
        "Hội chứng Conn (tăng aldosterone)",
        "Tăng huyết áp (liều thấp)"
    ],
    "contraindications": [
        "Tăng kali máu",
        "Suy thận nặng (CrCl <30)",
        "Vô niệu",
        "Bệnh Addison"
    ],
    "dosage": {
        "adult_heart_failure": "12.5-25mg x 1 lần/ngày, tăng đến 25-50mg x 1 lần/ngày",
        "adult_ascites": "100-400mg/ngày chia 1-2 lần",
        "adult_htn": "25-100mg/ngày chia 1-2 lần",
        "notes": "Khởi đầu với liều thấp. Theo dõi kali máu"
    },
    "renal_adjustment": {
        "normal": "Không đổi",
        "30_60": "Thận trọng",
        "under_30": "Chống chỉ định"
    },
    "side_effects": [
        "Tăng kali máu",
        "Vú to ở nam (gynecomastia)",
        "Rối loạn kinh nguyệt",
        "Buồn nôn",
        "Chóng mặt"
    ],
    "interactions": [
        "ACE inhibitor/ARB: tăng kali máu đáng kể",
        "Kali bổ sung: tăng kali máu",
        "Digoxin: tăng nồng độ digoxin"
    ],
    "pregnancy": "D",
        "mechanism_of_action": "Potassium-sparing diuretic, aldosterone antagonist. Đối kháng cạnh tranh với aldosterone tại mineralocorticoid receptor trong ống lượn xa và ống góp. Ngăn cản tác dụng của aldosterone (tái hấp thu natri, bài tiết kali). Dẫn đến tăng bài tiết natri và nước, giữ kali (không gây hạ kali). Có tác dụng chống androgen nhẹ (gây tác dụng phụ ở nam giới). Được dùng trong suy tim (giảm tử vong), xơ gan với cổ trướng, hội chứng Conn (cường aldosterone nguyên phát), và tăng huyết áp. Thường dùng kết hợp với loop diuretic hoặc thiazide để tránh hạ kali.",
        "monitoring": [
            "Điện giải (natri, kali) - tăng kali máu là tác dụng phụ chính (nguy hiểm)",
            "Chức năng thận (creatinine, eGFR) - không dùng nếu eGFR < 30",
            "Huyết áp",
            "Cân nặng và dấu hiệu phù",
            "Tác dụng phụ nội tiết (ở nam: vú to, rối loạn cương dương; ở nữ: rối loạn kinh nguyệt)",
            "Dấu hiệu quá liều (tăng kali nặng: yếu cơ, rối loạn nhịp tim)"
        ],
        "precautions": [
            "Tăng kali MÁU là tác dụng phụ chính - KHÔNG dùng nếu kali > 5 mEq/L hoặc eGFR < 30",
            "KHÔNG dùng với kali bổ sung hoặc các thuốc tăng kali khác (ACE inhibitor, ARB, trimethoprim) trừ khi được giám sát chặt chẽ",
            "Theo dõi kali thường xuyên, đặc biệt khi bắt đầu điều trị và tăng liều",
            "Tác dụng phụ nội tiết: vú to ở nam giới (gynecomastia), rối loạn cương dương, rối loạn kinh nguyệt ở nữ",
            "Liều thường: 25-100mg/ngày (PO), liều cao hơn cho hội chứng Conn",
            "Tác dụng chậm (vài ngày đến vài tuần)",
            "Không dùng ở suy thận nặng (eGFR < 30) hoặc tăng kali máu",
            "Thận trọng ở người cao tuổi (tăng nguy cơ tăng kali)",
            "Uống với thức ăn để tăng hấp thu"
        ],
        "pharmacokinetics": {
            "half_life": "10-35 giờ (dài)",
            "onset": "Vài ngày",
            "duration": "2-3 ngày sau khi ngừng",
            "protein_binding": "> 90%",
            "metabolism": "Gan (chuyển đổi thành active metabolites: canrenone)",
            "clearance": "Chủ yếu qua thận và gan"
        },
        "storage": "Bảo quản ở nhiệt độ phòng (20-25°C), tránh ẩm, tránh ánh sáng. Viên nén: tránh ẩm.",
        "black_box_warnings": "Không có black box warning. Tuy nhiên, tăng kali máu có thể gây rối loạn nhịp tim nghiêm trọng, có thể tử vong, đặc biệt ở bệnh nhân suy thận hoặc dùng với các thuốc tăng kali khác. Phải theo dõi kali thường xuyên.",
        "drug_interactions": {
            "major": [
                {
                    "drug": "ACE inhibitors (captopril, enalapril, lisinopril), ARB (losartan, valsartan)",
                    "mechanism": "Cả hai đều làm giảm bài tiết kali qua thận, tác dụng hiệp đồng gây tăng kali máu",
                    "effect": "Tăng kali máu nặng (hyperkalemia), có thể gây rối loạn nhịp tim, ngừng tim",
                    "management": "Thận trọng. Theo dõi kali máu thường xuyên (1-2 tuần sau khi bắt đầu, sau đó mỗi 1-3 tháng). KHÔNG dùng cùng nếu kali > 5 mEq/L hoặc eGFR < 30. Cân nhắc giảm liều hoặc ngừng một trong hai thuốc nếu kali tăng."
                },
                {
                    "drug": "Kali bổ sung (potassium supplements), muối kali (potassium chloride)",
                    "mechanism": "Spironolactone giữ kali, kali bổ sung tăng kali máu",
                    "effect": "Tăng kali máu nặng, nguy hiểm",
                    "management": "CHỐNG CHỈ ĐỊNH dùng cùng. KHÔNG dùng kali bổ sung khi đang dùng spironolactone trừ khi được giám sát chặt chẽ và có chỉ định đặc biệt."
                },
                {
                    "drug": "Trimethoprim, Trimethoprim-sulfamethoxazole",
                    "mechanism": "Trimethoprim ức chế bài tiết kali ở ống lượn xa, tương tự spironolactone",
                    "effect": "Tăng kali máu nặng, đặc biệt ở người cao tuổi, suy thận",
                    "management": "Thận trọng. Theo dõi kali máu thường xuyên. Cân nhắc tránh dùng cùng, đặc biệt ở người cao tuổi hoặc suy thận."
                }
            ],
            "moderate": [
                {
                    "drug": "Digoxin",
                    "mechanism": "Spironolactone ức chế thải trừ digoxin qua thận, tăng nồng độ digoxin trong máu",
                    "effect": "Tăng nồng độ digoxin, tăng nguy cơ ngộ độc digoxin (buồn nôn, rối loạn nhịp tim, block AV)",
                    "management": "Theo dõi nồng độ digoxin trong máu. Có thể cần giảm liều digoxin. Theo dõi dấu hiệu ngộ độc digoxin."
                },
                {
                    "drug": "NSAIDs (ibuprofen, naproxen, diclofenac)",
                    "mechanism": "NSAID làm giảm lưu lượng máu thận, giảm bài tiết natri và kali",
                    "effect": "Tăng nguy cơ tăng kali máu, suy thận cấp",
                    "management": "Thận trọng, đặc biệt ở người cao tuổi hoặc suy thận. Theo dõi kali máu và chức năng thận. Tránh dùng lâu dài cùng."
                },
                {
                    "drug": "Amiloride, Triamterene (các kali-sparing diuretics khác)",
                    "mechanism": "Tác dụng hiệp đồng giữ kali",
                    "effect": "Tăng kali máu nặng",
                    "management": "KHÔNG dùng cùng. Chọn một trong các kali-sparing diuretics."
                },
                {
                    "drug": "Heparin (liều cao)",
                    "mechanism": "Heparin ức chế sản xuất aldosterone, có thể làm giảm bài tiết kali",
                    "effect": "Tăng nguy cơ tăng kali máu",
                    "management": "Theo dõi kali máu khi dùng heparin liều cao cùng spironolactone."
                }
            ],
            "minor": [
                {
                    "drug": "Aspirin liều thấp",
                    "mechanism": "Có thể làm giảm tác dụng lợi tiểu của spironolactone",
                    "effect": "Giảm nhẹ hiệu quả lợi tiểu",
                    "management": "Thường không cần điều chỉnh. Theo dõi đáp ứng điều trị."
                }
            ]
        },
        "contraindications": {
            "absolute": [
                "Tăng kali máu (hyperkalemia) - kali > 5 mEq/L",
                "Suy thận nặng (CrCl < 30 mL/min, eGFR < 30)",
                "Vô niệu (anuria)",
                "Bệnh Addison (suy thượng thận nguyên phát)",
                "Dùng cùng kali bổ sung hoặc kali-sparing diuretics khác (amiloride, triamterene)"
            ],
            "relative": [
                "Suy thận trung bình (CrCl 30-60) - thận trọng, theo dõi kali thường xuyên",
                "Dùng cùng ACE inhibitor/ARB - thận trọng, theo dõi kali thường xuyên",
                "Người cao tuổi - tăng nguy cơ tăng kali máu",
                "Suy gan - thận trọng (chuyển hóa qua gan)",
                "Tiểu đường - thận trọng (tăng nguy cơ tăng kali máu ở bệnh nhân đái tháo đường type 4)",
                "Thai kỳ - FDA category D, cân nhắc lợi ích/nguy cơ"
            ]
        },
        "pregnancy_lactation": {
            "fda_category": "D",
            "pregnancy_details": "Spironolactone có thể gây tác dụng phụ trên thai nhi. Có thể gây tác dụng chống androgen (anti-androgen) trên thai nhi nam, dẫn đến dị tật bộ phận sinh dục. Có thể gây tác dụng phụ trên thai nhi nữ. Cân nhắc lợi ích/nguy cơ. Chỉ dùng khi lợi ích rõ ràng vượt trội nguy cơ. Tránh dùng trong tam cá nguyệt đầu tiên nếu có thể.",
            "lactation": {
                "safety": "Caution",
                "details": "Spironolactone và các metabolites bài tiết vào sữa mẹ. Nồng độ trong sữa mẹ thấp nhưng có thể gây tác dụng phụ trên trẻ bú mẹ. Có thể gây tác dụng chống androgen nhẹ. Có thể gây tăng kali máu ở trẻ bú mẹ (hiếm).",
                "recommendation": "Thận trọng khi dùng khi cho con bú. Cân nhắc lợi ích/nguy cơ. Theo dõi trẻ bú mẹ nếu có dấu hiệu bất thường. Có thể cân nhắc ngừng cho con bú hoặc dùng thuốc thay thế nếu có thể."
            }
        },
        "hepatic_adjustment": {
            "mild": "Không đổi liều",
            "moderate": "Thận trọng, có thể cần giảm liều do chuyển hóa qua gan",
            "severe": "Thận trọng, giảm liều hoặc tránh dùng. Spironolactone chuyển hóa qua gan thành canrenone (active metabolite). Suy gan nặng có thể làm tăng nồng độ spironolactone.",
            "notes": "Spironolactone chuyển hóa qua gan (chuyển đổi thành canrenone). Suy gan có thể làm giảm chuyển hóa, tăng nồng độ spironolactone và tăng tác dụng phụ. Tuy nhiên, spironolactone thường được dùng trong xơ gan với cổ trướng, nên cần cân nhắc lợi ích/nguy cơ."
        },
        "overdose_management": {
            "symptoms": [
                "Tăng kali máu nặng (hyperkalemia) - triệu chứng chính và nguy hiểm nhất",
                "Yếu cơ, liệt cơ",
                "Rối loạn nhịp tim (arrhythmias), đặc biệt là rối loạn nhịp chậm",
                "Block nhĩ thất",
                "Ngừng tim (cardiac arrest)",
                "Rối loạn điện giải (hạ natri máu có thể xảy ra)",
                "Mất nước (dehydration) do lợi tiểu quá mức",
                "Hạ huyết áp",
                "Buồn nôn, nôn",
                "Chóng mặt, mệt mỏi"
            ],
            "antidote": "Không có antidote đặc hiệu. Xử trí tăng kali máu: Calcium gluconate/calcium chloride (bảo vệ tim), Insulin + glucose (chuyển kali vào tế bào), Sodium bicarbonate (nếu có nhiễm toan), Beta-2 agonist (salbutamol) - chuyển kali vào tế bào, Furosemide (tăng bài tiết kali) nếu chức năng thận bình thường, Hemodialysis nếu tăng kali nặng không đáp ứng",
            "treatment": [
                "Ngừng spironolactone ngay lập tức",
                "Đo kali máu ngay (ECG nếu có thể)",
                "Xử trí tăng kali máu:",
                "  - Nếu kali > 6.5 mEq/L hoặc có dấu hiệu tim mạch: Calcium gluconate 1-3g IV (bảo vệ tim, tác dụng nhanh)",
                "  - Insulin regular 10 đơn vị + Dextrose 50% 50ml IV (chuyển kali vào tế bào, tác dụng trong 15-30 phút)",
                "  - Sodium bicarbonate 50-100 mEq IV nếu có nhiễm toan (pH < 7.35)",
                "  - Salbutamol nebulizer 10-20mg (beta-2 agonist, chuyển kali vào tế bào)",
                "  - Furosemide 40-80mg IV nếu chức năng thận bình thường (tăng bài tiết kali)",
                "  - Hemodialysis nếu kali > 6.5 mEq/L và không đáp ứng với điều trị trên",
                "Theo dõi ECG liên tục (tăng kali gây thay đổi ECG: sóng T cao nhọn, kéo dài PR, mất sóng P, giãn QRS, rối loạn nhịp)",
                "Theo dõi kali máu thường xuyên (mỗi 1-2 giờ cho đến khi ổn định)",
                "Điều chỉnh các rối loạn điện giải khác (natri, canxi, magie)",
                "Hỗ trợ hô hấp và tuần hoàn nếu cần",
                "Rửa dạ dày và than hoạt tính nếu uống quá liều trong vòng 1-2 giờ (tuy nhiên spironolactone hấp thu chậm)",
                "Theo dõi ít nhất 24-48 giờ do half-life dài (10-35 giờ)"
            ],
            "monitoring": "ECG liên tục, kali máu (mỗi 1-2 giờ), natri máu, chức năng thận (creatinine, BUN), huyết áp, nhịp tim, dấu hiệu rối loạn nhịp tim, dấu hiệu suy hô hấp, dấu hiệu yếu cơ"
        },
        "reversal_agents": {
            "available": False,
            "agents": []
        },
        "administration_instructions": {
            "oral": {
                "with_food": "Nên uống với thức ăn để tăng hấp thu và giảm kích ứng dạ dày",
                "timing": "Uống 1-2 lần/ngày vào cùng một giờ mỗi ngày. Có thể uống vào buổi sáng hoặc chia 2 lần (sáng và trưa). Tránh uống vào buổi tối muộn để tránh đi tiểu đêm. Tác dụng chậm (vài ngày đến vài tuần), cần kiên nhẫn."
            },
            "iv": {
                "reconstitution": "Không có dạng IV",
                "infusion_rate": "Không áp dụng",
                "compatibility": [],
                "incompatibility": [],
                "notes": "Spironolactone chỉ có dạng uống (PO)."
            }
        },
        "references": {
            "primary_sources": [
                "FDA Drug Label - Aldactone (spironolactone)",
                "UpToDate - Spironolactone: Drug information",
                "RALES Study - New England Journal of Medicine (1999) - Spironolactone trong suy tim",
                "EPHESUS Study - New England Journal of Medicine (2003) - Eplerenone sau nhồi máu cơ tim",
                "American Heart Association/American College of Cardiology guidelines - Heart failure management",
                "Goodman & Gilman's Pharmacological Basis of Therapeutics - Diuretics"
            ],
            "last_updated": "2024-12-19",
            "evidence_level": "High - Multiple large RCTs (RALES, EPHESUS) showing mortality benefit in heart failure"
        }

},

"Atenolol": {
    "group": "Cardiovascular - Beta-blocker (Selective)",
    "vietnamese_name": "Atenolol, Tenormin",
    "administration": ["PO"],
    "indications": [
        "Tăng huyết áp",
        "Đau thắt ngực",
        "Sau nhồi máu cơ tim",
        "Rối loạn nhịp tim"
    ],
    "contraindications": [
        "Hen phế quản nặng",
        "Block nhĩ thất độ 2-3",
        "Suy tim cấp không bù",
        "Nhịp tim chậm nặng"
    ],
    "dosage": {
        "adult_htn": "25-100mg x 1 lần/ngày",
        "adult_angina": "50-100mg x 1 lần/ngày",
        "adult_post_mi": "50-100mg x 1 lần/ngày",
        "notes": "Uống 1 lần/ngày. Chọn lọc beta-1"
    },
    "renal_adjustment": {
        "normal": "Không đổi",
        "30_60": "Giảm liều 50%",
        "under_30": "Giảm liều 75%, hoặc dùng mỗi 2 ngày"
    },
    "side_effects": [
        "Mệt mỏi",
        "Lạnh tay chân",
        "Nhịp tim chậm",
        "Rối loạn giấc ngủ",
        "Khó thở ở bệnh nhân hen/COPD"
    ],
          "interactions": [
          "Verapamil/Diltiazem: tăng nguy cơ block nhĩ thất",
          "Insulin: che dấu triệu chứng hạ đường huyết"
      ],
      "pregnancy": "D",
      "mechanism_of_action": "Selective beta-1 adrenergic receptor blocker. Ức chế tác dụng của catecholamines (epinephrine, norepinephrine) trên beta-1 receptors ở tim, giảm nhịp tim, giảm co bóp cơ tim, giảm huyết áp, giảm nhu cầu oxy cơ tim. Chọn lọc beta-1 hơn metoprolol, ít tác dụng trên beta-2 (ít gây co thắt phế quản hơn propranolol). Thải chủ yếu qua thận (khác với metoprolol - thải qua gan).",
      "monitoring": [
          "Nhịp tim và huyết áp (trước và sau khi bắt đầu)",
          "Chức năng thận: creatinine, BUN (thải chủ yếu qua thận - cần điều chỉnh liều)",
          "Dấu hiệu suy tim (khó thở, phù, tăng cân)",
          "Đường huyết (ở bệnh nhân đái tháo đường - che dấu triệu chứng hạ đường huyết)",
          "Triệu chứng mệt mỏi, lạnh tay chân"
      ],
      "precautions": [
          "KHÔNG được ngừng đột ngột (có thể gây rebound hypertension, đau thắt ngực nặng). Phải giảm liều dần trong 1-2 tuần",
          "Thải chủ yếu qua thận - cần giảm liều ở bệnh nhân suy thận (CrCl <30: giảm 75% hoặc dùng mỗi 2 ngày)",
          "Thận trọng ở bệnh nhân hen phế quản/COPD (mặc dù chọn lọc beta-1, vẫn có thể gây co thắt phế quản ở liều cao)",
          "Tránh dùng trong suy tim cấp không bù, block AV độ 2-3, nhịp tim chậm <50 bpm",
          "Thận trọng ở bệnh nhân đái tháo đường (che dấu triệu chứng hạ đường huyết)",
          "Thận trọng khi dùng với verapamil/diltiazem (tăng nguy cơ block AV, suy tim)"
      ],
      "pharmacokinetics": {
          "half_life": "6-7 giờ (dài hơn metoprolol)",
          "onset": "1 giờ (PO)",
          "duration": "24 giờ (uống 1 lần/ngày)",
          "protein_binding": "5-15% (thấp, ít protein binding)",
          "clearance": "Thận (chủ yếu, 85-100% thải nguyên dạng qua nước tiểu). Không chuyển hóa qua gan"
      },
      "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm, tránh ánh sáng",
      "black_box_warnings": "KHÔNG được ngừng đột ngột ở bệnh nhân đau thắt ngực hoặc sau nhồi máu cơ tim - có thể gây đau thắt ngực nặng, nhồi máu cơ tim, rối loạn nhịp tim nặng. Phải giảm liều dần dần trong 1-2 tuần",
      "drug_interactions": {
          "major": [
              {
                  "drug": "Verapamil, Diltiazem",
                  "mechanism": "Tác dụng hiệp đồng ức chế dẫn truyền nhĩ thất",
                  "effect": "Tăng nguy cơ block nhĩ thất độ 2-3, suy tim, nhịp tim chậm nặng",
                  "management": "Thận trọng. Theo dõi ECG, nhịp tim, huyết áp. Tránh dùng cùng nếu có thể."
              },
              {
                  "drug": "Clonidine (khi ngừng đột ngột)",
                  "mechanism": "Cả hai đều ức chế giao cảm, ngừng clonidine đột ngột gây rebound hypertension",
                  "effect": "Tăng huyết áp nghiêm trọng, có thể gây đột quỵ",
                  "management": "Không ngừng clonidine đột ngột khi đang dùng atenolol. Giảm liều clonidine dần."
              }
          ],
          "moderate": [
              {
                  "drug": "Insulin, Sulfonylureas (thuốc điều trị đái tháo đường)",
                  "mechanism": "Che dấu triệu chứng hạ đường huyết (nhịp tim nhanh, run), tăng nguy cơ hạ đường huyết kéo dài",
                  "effect": "Hạ đường huyết nặng, khó nhận biết triệu chứng",
                  "management": "Theo dõi đường huyết thường xuyên. Bệnh nhân đái tháo đường nên biết triệu chứng hạ đường huyết khác (đổ mồ hôi, lú lẫn)."
              },
              {
                  "drug": "Digoxin",
                  "mechanism": "Tăng nguy cơ block nhĩ thất",
                  "effect": "Nhịp tim chậm nặng, block AV",
                  "management": "Theo dõi nhịp tim, ECG. Có thể cần giảm liều digoxin."
              },
              {
                  "drug": "NSAIDs (ibuprofen, naproxen)",
                  "mechanism": "NSAID làm giảm tác dụng hạ huyết áp của beta-blocker",
                  "effect": "Giảm hiệu quả hạ huyết áp",
                  "management": "Thận trọng. Theo dõi huyết áp. Tránh dùng lâu dài cùng."
              }
          ],
          "minor": [
              {
                  "drug": "Rifampin",
                  "mechanism": "Có thể tăng chuyển hóa atenolol (mặc dù thải chủ yếu qua thận)",
                  "effect": "Giảm hiệu quả atenolol",
                  "management": "Theo dõi huyết áp, nhịp tim. Có thể cần tăng liều atenolol."
              }
          ]
      },
      "contraindications": {
          "absolute": [
              "Hen phế quản nặng",
              "Block nhĩ thất độ 2-3 không có máy tạo nhịp",
              "Suy tim cấp không bù",
              "Nhịp tim chậm nặng (<50 bpm)",
              "Sốc tim"
          ],
          "relative": [
              "COPD - thận trọng (mặc dù chọn lọc beta-1, vẫn có thể gây co thắt phế quản)",
              "Suy thận nặng (CrCl <30) - giảm liều 75% hoặc dùng mỗi 2 ngày",
              "Suy thận trung bình (CrCl 30-60) - giảm liều 50%",
              "Đái tháo đường - thận trọng (che dấu triệu chứng hạ đường huyết)",
              "Bệnh mạch máu ngoại vi (Raynaud) - có thể làm nặng thêm",
              "Dùng với verapamil/diltiazem - tăng nguy cơ block AV"
          ]
      },
      "pregnancy_lactation": {
          "fda_category": "D",
          "pregnancy_details": "Có thể gây hạ huyết áp, nhịp tim chậm, suy hô hấp ở thai nhi. Có thể gây chậm phát triển thai nhi, nhịp tim chậm, hạ đường huyết ở trẻ sơ sinh. Cân nhắc lợi ích/nguy cơ. Thường dùng được nếu lợi ích vượt trội nguy cơ.",
          "lactation": {
              "safety": "Compatible",
              "details": "Atenolol bài tiết vào sữa mẹ ở nồng độ thấp. Nồng độ trong máu trẻ bú mẹ thường rất thấp. Có thể gây nhịp tim chậm nhẹ ở trẻ bú mẹ nhưng hiếm.",
              "recommendation": "Có thể dùng khi cho con bú. Theo dõi trẻ nếu có nhịp tim chậm, mệt mỏi, tăng cân kém."
          }
      },
      "hepatic_adjustment": {
          "mild": "Không đổi",
          "moderate": "Không đổi (thải chủ yếu qua thận)",
          "severe": "Không đổi (thải chủ yếu qua thận)",
          "notes": "Atenolol thải chủ yếu qua thận (85-100% thải nguyên dạng qua nước tiểu), không chuyển hóa qua gan. Suy gan không ảnh hưởng đến dược động học của atenolol."
      },
      "overdose_management": {
          "symptoms": [
              "Nhịp tim chậm nặng (<40 bpm)",
              "Block nhĩ thất độ 2-3",
              "Hạ huyết áp nặng",
              "Suy tim cấp",
              "Co giật",
              "Hôn mê",
              "Suy hô hấp"
          ],
          "antidote": "Glucagon (có thể đảo ngược tác dụng beta-blocker), Atropine (cho nhịp tim chậm), Epinephrine (cho hạ huyết áp nặng)",
          "treatment": [
              "Rửa dạ dày nếu uống trong vòng 1-2 giờ",
              "Than hoạt tính",
              "Điều trị nhịp tim chậm: Atropine 0.5-1mg IV, có thể lặp lại. Nếu không hiệu quả: Glucagon 1-5mg IV, Isoproterenol, hoặc máy tạo nhịp tạm thời",
              "Điều trị hạ huyết áp: Truyền dịch (normal saline), nâng chân, Glucagon 1-5mg IV, Epinephrine (thận trọng - có thể gây tăng huyết áp quá mức)",
              "Theo dõi ECG liên tục",
              "Theo dõi huyết áp, nhịp tim, ý thức",
              "Hỗ trợ hô hấp nếu cần",
              "Theo dõi ít nhất 12-24 giờ (do half-life 6-7 giờ)"
          ],
          "monitoring": "ECG liên tục, huyết áp, nhịp tim, ý thức, dấu hiệu suy tim, dấu hiệu suy hô hấp"
      },
      "reversal_agents": {
          "available": True,
          "agents": [
              {
                  "name": "Glucagon",
                  "mechanism": "Kích thích cAMP, đảo ngược tác dụng beta-blocker",
                  "dose": "1-5mg IV, có thể lặp lại",
                  "indication": "Nhịp tim chậm, hạ huyết áp do quá liều beta-blocker"
              },
              {
                  "name": "Atropine",
                  "mechanism": "Chẹn muscarinic, tăng nhịp tim",
                  "dose": "0.5-1mg IV, có thể lặp lại",
                  "indication": "Nhịp tim chậm, block AV"
              },
              {
                  "name": "Epinephrine",
                  "mechanism": "Agonist alpha và beta, tăng nhịp tim và huyết áp",
                  "dose": "Theo protocol ACLS",
                  "indication": "Hạ huyết áp nặng không đáp ứng với glucagon"
              }
          ]
      },
      "administration_instructions": {
          "oral": {
              "with_food": "Có thể uống với hoặc không có thức ăn. Không ảnh hưởng đáng kể đến hấp thu.",
              "timing": "Uống 1 lần/ngày vào cùng một giờ mỗi ngày. Không ngừng đột ngột - phải giảm liều dần trong 1-2 tuần."
          },
          "iv": {
              "reconstitution": "Không có dạng IV",
              "infusion_rate": "Không áp dụng",
              "compatibility": [],
              "incompatibility": [],
              "notes": "Atenolol chỉ có dạng uống (PO)."
          }
      },
      "references": {
          "primary_sources": [
              "FDA Drug Label - Tenormin (atenolol)",
              "UpToDate - Atenolol: Drug information",
              "ISIS-1 Study - Lancet (1986) - Beta-blocker sau nhồi máu cơ tim",
              "American Heart Association/American College of Cardiology guidelines - Beta-blockers in hypertension and heart failure"
          ],
          "last_updated": "2024-12-19",
          "evidence_level": "High - Multiple large RCTs (ISIS-1) and extensive clinical experience"
      }
  },

"Bisoprolol": {
    "group": "Cardiovascular - Beta-blocker (Selective)",
    "vietnamese_name": "Bisoprolol, Concor",
    "administration": ["PO"],
    "indications": [
        "Tăng huyết áp",
        "Suy tim (NYHA class II-IV)",
        "Đau thắt ngực"
    ],
    "contraindications": [
        "Hen phế quản nặng",
        "Block nhĩ thất độ 2-3",
        "Suy tim cấp không bù",
        "Nhịp tim chậm nặng (<60 bpm)"
    ],
    "dosage": {
        "adult_htn": "2.5-10mg x 1 lần/ngày",
        "adult_heart_failure": "1.25mg x 1 lần/ngày, tăng dần đến 10mg x 1 lần/ngày",
        "adult_angina": "5-10mg x 1 lần/ngày",
        "notes": "Uống 1 lần/ngày. Có bằng chứng giảm tỷ lệ tử vong trong suy tim"
    },
    "renal_adjustment": {
        "normal": "Không đổi",
        "30_60": "Thận trọng, có thể giảm liều",
        "under_30": "Thận trọng, giảm liều"
    },
    "side_effects": [
        "Mệt mỏi",
        "Lạnh tay chân",
        "Nhịp tim chậm",
        "Chóng mặt",
        "Khó thở ở bệnh nhân hen/COPD"
    ],
          "interactions": [
          "Verapamil/Diltiazem: tăng nguy cơ block nhĩ thất",
          "Insulin: che dấu triệu chứng hạ đường huyết"
      ],
      "pregnancy": "C",
      "mechanism_of_action": "Selective beta-1 adrenergic receptor blocker. Ức chế tác dụng của catecholamines trên beta-1 receptors ở tim, giảm nhịp tim, giảm co bóp cơ tim, giảm huyết áp. Có bằng chứng mạnh làm giảm tỷ lệ tử vong và nhập viện trong suy tim mạn tính (NYHA class II-IV). Thải qua cả thận và gan (50-50%).",
      "monitoring": [
          "Nhịp tim và huyết áp (trước và sau khi bắt đầu, đặc biệt ở bệnh nhân suy tim)",
          "Dấu hiệu suy tim: khó thở, phù, tăng cân, giảm khả năng gắng sức",
          "Chức năng thận và gan (thải qua cả hai)",
          "Đường huyết (ở bệnh nhân đái tháo đường)",
          "Triệu chứng mệt mỏi, chóng mặt, lạnh tay chân"
      ],
      "precautions": [
          "KHÔNG được ngừng đột ngột (có thể gây rebound hypertension, đau thắt ngực nặng, suy tim nặng). Phải giảm liều dần trong 1-2 tuần",
          "Khởi đầu với liều thấp (1.25mg/ngày) ở bệnh nhân suy tim, tăng dần mỗi 2-4 tuần",
          "Thận trọng ở bệnh nhân hen phế quản/COPD (mặc dù chọn lọc beta-1, vẫn có thể gây co thắt phế quản)",
          "Tránh dùng trong suy tim cấp không bù, block AV độ 2-3, nhịp tim chậm <60 bpm",
          "Thận trọng ở bệnh nhân suy thận hoặc suy gan nặng",
          "Thận trọng khi dùng với verapamil/diltiazem (tăng nguy cơ block AV, suy tim)"
      ],
      "pharmacokinetics": {
          "half_life": "9-12 giờ (dài, cho phép uống 1 lần/ngày)",
          "onset": "1-2 giờ (PO)",
          "duration": "24 giờ",
          "protein_binding": "30%",
          "clearance": "Thận (50%) và gan (50%) - chuyển hóa qua CYP3A4 và CYP2D6"
      },
      "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm, tránh ánh sáng",
      "black_box_warnings": "KHÔNG được ngừng đột ngột ở bệnh nhân đau thắt ngực hoặc suy tim - có thể gây đau thắt ngực nặng, nhồi máu cơ tim, suy tim nặng. Phải giảm liều dần dần trong 1-2 tuần",
      "drug_interactions": {
          "major": [
              {
                  "drug": "Verapamil, Diltiazem",
                  "mechanism": "Tác dụng hiệp đồng ức chế dẫn truyền nhĩ thất",
                  "effect": "Tăng nguy cơ block nhĩ thất độ 2-3, suy tim, nhịp tim chậm nặng",
                  "management": "Thận trọng. Theo dõi ECG, nhịp tim, huyết áp. Tránh dùng cùng nếu có thể."
              },
              {
                  "drug": "Clonidine (khi ngừng đột ngột)",
                  "mechanism": "Cả hai đều ức chế giao cảm, ngừng clonidine đột ngột gây rebound hypertension",
                  "effect": "Tăng huyết áp nghiêm trọng, có thể gây đột quỵ",
                  "management": "Không ngừng clonidine đột ngột khi đang dùng bisoprolol. Giảm liều clonidine dần."
              }
          ],
          "moderate": [
              {
                  "drug": "CYP3A4 inhibitors (ketoconazole, itraconazole, clarithromycin, erythromycin)",
                  "mechanism": "Ức chế chuyển hóa bisoprolol qua CYP3A4",
                  "effect": "Tăng nồng độ bisoprolol, tăng tác dụng phụ",
                  "management": "Thận trọng. Theo dõi nhịp tim, huyết áp. Có thể cần giảm liều bisoprolol."
              },
              {
                  "drug": "CYP2D6 inhibitors (fluoxetine, paroxetine, quinidine)",
                  "mechanism": "Ức chế chuyển hóa bisoprolol qua CYP2D6",
                  "effect": "Tăng nồng độ bisoprolol, tăng tác dụng phụ",
                  "management": "Thận trọng. Theo dõi nhịp tim, huyết áp. Có thể cần giảm liều bisoprolol."
              },
              {
                  "drug": "Insulin, Sulfonylureas",
                  "mechanism": "Che dấu triệu chứng hạ đường huyết",
                  "effect": "Hạ đường huyết nặng, khó nhận biết triệu chứng",
                  "management": "Theo dõi đường huyết thường xuyên."
              },
              {
                  "drug": "Digoxin",
                  "mechanism": "Tăng nguy cơ block nhĩ thất",
                  "effect": "Nhịp tim chậm nặng, block AV",
                  "management": "Theo dõi nhịp tim, ECG. Có thể cần giảm liều digoxin."
              }
          ],
          "minor": [
              {
                  "drug": "NSAIDs",
                  "mechanism": "Giảm tác dụng hạ huyết áp",
                  "effect": "Giảm hiệu quả hạ huyết áp",
                  "management": "Theo dõi huyết áp."
              }
          ]
      },
      "contraindications": {
          "absolute": [
              "Hen phế quản nặng",
              "Block nhĩ thất độ 2-3 không có máy tạo nhịp",
              "Suy tim cấp không bù",
              "Nhịp tim chậm nặng (<60 bpm)",
              "Sốc tim"
          ],
          "relative": [
              "COPD - thận trọng (mặc dù chọn lọc beta-1, vẫn có thể gây co thắt phế quản)",
              "Suy thận nặng (CrCl <30) - giảm liều, thận trọng",
              "Suy gan nặng - giảm liều, thận trọng (thải qua cả thận và gan)",
              "Đái tháo đường - thận trọng (che dấu triệu chứng hạ đường huyết)",
              "Dùng với verapamil/diltiazem - tăng nguy cơ block AV",
              "Dùng với CYP3A4 hoặc CYP2D6 inhibitors - tăng nồng độ bisoprolol"
          ]
      },
      "pregnancy_lactation": {
          "fda_category": "C",
          "pregnancy_details": "Có thể gây hạ huyết áp, nhịp tim chậm ở thai nhi. Có thể gây chậm phát triển thai nhi, nhịp tim chậm ở trẻ sơ sinh. Cân nhắc lợi ích/nguy cơ. Thường dùng được nếu lợi ích vượt trội nguy cơ, đặc biệt trong suy tim.",
          "lactation": {
              "safety": "Compatible",
              "details": "Bisoprolol bài tiết vào sữa mẹ ở nồng độ thấp. Nồng độ trong máu trẻ bú mẹ thường rất thấp. Có thể gây nhịp tim chậm nhẹ ở trẻ bú mẹ nhưng hiếm.",
              "recommendation": "Có thể dùng khi cho con bú. Theo dõi trẻ nếu có nhịp tim chậm, mệt mỏi, tăng cân kém."
          }
      },
      "hepatic_adjustment": {
          "mild": "Không đổi",
          "moderate": "Thận trọng, giảm liều (thải 50% qua gan)",
          "severe": "Thận trọng, giảm liều (thải 50% qua gan)",
          "notes": "Bisoprolol thải qua cả thận (50%) và gan (50%, chuyển hóa qua CYP3A4 và CYP2D6). Suy gan có thể làm tăng nồng độ bisoprolol."
      },
      "overdose_management": {
          "symptoms": [
              "Nhịp tim chậm nặng (<40 bpm)",
              "Block nhĩ thất độ 2-3",
              "Hạ huyết áp nặng",
              "Suy tim cấp",
              "Co giật",
              "Hôn mê",
              "Suy hô hấp"
          ],
          "antidote": "Glucagon (có thể đảo ngược tác dụng beta-blocker), Atropine (cho nhịp tim chậm), Epinephrine (cho hạ huyết áp nặng)",
          "treatment": [
              "Rửa dạ dày nếu uống trong vòng 1-2 giờ",
              "Than hoạt tính",
              "Điều trị nhịp tim chậm: Atropine 0.5-1mg IV, có thể lặp lại. Nếu không hiệu quả: Glucagon 1-5mg IV, Isoproterenol, hoặc máy tạo nhịp tạm thời",
              "Điều trị hạ huyết áp: Truyền dịch (normal saline), nâng chân, Glucagon 1-5mg IV, Epinephrine (thận trọng)",
              "Theo dõi ECG liên tục",
              "Theo dõi huyết áp, nhịp tim, ý thức",
              "Hỗ trợ hô hấp nếu cần",
              "Theo dõi ít nhất 24-48 giờ (do half-life 9-12 giờ)"
          ],
          "monitoring": "ECG liên tục, huyết áp, nhịp tim, ý thức, dấu hiệu suy tim, dấu hiệu suy hô hấp"
      },
      "reversal_agents": {
          "available": True,
          "agents": [
              {
                  "name": "Glucagon",
                  "mechanism": "Kích thích cAMP, đảo ngược tác dụng beta-blocker",
                  "dose": "1-5mg IV, có thể lặp lại",
                  "indication": "Nhịp tim chậm, hạ huyết áp do quá liều beta-blocker"
              },
              {
                  "name": "Atropine",
                  "mechanism": "Chẹn muscarinic, tăng nhịp tim",
                  "dose": "0.5-1mg IV, có thể lặp lại",
                  "indication": "Nhịp tim chậm, block AV"
              },
              {
                  "name": "Epinephrine",
                  "mechanism": "Agonist alpha và beta, tăng nhịp tim và huyết áp",
                  "dose": "Theo protocol ACLS",
                  "indication": "Hạ huyết áp nặng không đáp ứng với glucagon"
              }
          ]
      },
      "administration_instructions": {
          "oral": {
              "with_food": "Có thể uống với hoặc không có thức ăn. Không ảnh hưởng đáng kể đến hấp thu.",
              "timing": "Uống 1 lần/ngày vào cùng một giờ mỗi ngày. Ở bệnh nhân suy tim: khởi đầu với liều thấp (1.25mg/ngày), tăng dần mỗi 2-4 tuần. KHÔNG ngừng đột ngột - phải giảm liều dần trong 1-2 tuần."
          },
          "iv": {
              "reconstitution": "Không có dạng IV",
              "infusion_rate": "Không áp dụng",
              "compatibility": [],
              "incompatibility": [],
              "notes": "Bisoprolol chỉ có dạng uống (PO)."
          }
      },
      "references": {
          "primary_sources": [
              "FDA Drug Label - Zebeta (bisoprolol)",
              "UpToDate - Bisoprolol: Drug information",
              "CIBIS-II Study - Lancet (1999) - Bisoprolol trong suy tim",
              "American Heart Association/American College of Cardiology guidelines - Beta-blockers in heart failure"
          ],
          "last_updated": "2024-12-19",
          "evidence_level": "High - Large RCT (CIBIS-II) showing mortality benefit in heart failure and extensive clinical experience"
      }
  },

"Carvedilol": {
    "group": "Cardiovascular - Beta-blocker (Non-selective with Alpha-blocking)",
    "vietnamese_name": "Carvedilol, Dilatrend",
    "administration": ["PO"],
    "indications": [
        "Suy tim (NYHA class II-IV)",
        "Tăng huyết áp",
        "Sau nhồi máu cơ tim"
    ],
    "contraindications": [
        "Hen phế quản nặng",
        "Block nhĩ thất độ 2-3",
        "Suy tim cấp không bù",
        "Nhịp tim chậm nặng",
        "Suy gan nặng"
    ],
    "dosage": {
        "adult_heart_failure": "3.125mg x 2 lần/ngày, tăng dần mỗi 2 tuần đến 25mg x 2 lần/ngày",
        "adult_htn": "6.25-25mg x 2 lần/ngày",
        "adult_post_mi": "6.25-25mg x 2 lần/ngày",
        "notes": "Có bằng chứng giảm tỷ lệ tử vong trong suy tim. Có tác dụng giãn mạch"
    },
    "renal_adjustment": {
        "normal": "Không đổi",
        "30_60": "Thận trọng",
        "under_30": "Thận trọng"
    },
    "side_effects": [
        "Mệt mỏi",
        "Chóng mặt",
        "Hạ huyết áp",
        "Nhịp tim chậm",
        "Phù chân (ít)"
    ],
          "interactions": [
          "Digoxin: tăng nồng độ digoxin",
          "Insulin: che dấu triệu chứng hạ đường huyết",
          "CYP2D6 inhibitors: tăng nồng độ carvedilol"
      ],
      "pregnancy": "C",
      "mechanism_of_action": "Non-selective beta-adrenergic receptor blocker (beta1 và beta2) kết hợp với alpha-1 adrenergic receptor blocker. Ức chế beta receptors làm giảm nhịp tim, giảm co bóp cơ tim, giảm huyết áp. Block alpha-1 receptors gây giãn mạch, giảm hậu gánh, cải thiện tuần hoàn. Có bằng chứng mạnh làm giảm tỷ lệ tử vong và nhập viện trong suy tim mạn tính (NYHA class II-IV).",
      "monitoring": [
          "Nhịp tim và huyết áp (trước và sau khi bắt đầu, đặc biệt ở bệnh nhân suy tim - có thể gây hạ huyết áp)",
          "Dấu hiệu suy tim: khó thở, phù, tăng cân, giảm khả năng gắng sức",
          "Chức năng gan (chống chỉ định trong suy gan nặng)",
          "Đường huyết (ở bệnh nhân đái tháo đường)",
          "Triệu chứng mệt mỏi, chóng mặt, hạ huyết áp, phù chân"
      ],
      "precautions": [
          "KHÔNG được ngừng đột ngột (có thể gây rebound hypertension, đau thắt ngực nặng, suy tim nặng). Phải giảm liều dần trong 1-2 tuần",
          "Khởi đầu với liều rất thấp (3.125mg x 2 lần/ngày) ở bệnh nhân suy tim, tăng dần mỗi 2 tuần",
          "CHỐNG CHỈ ĐỊNH trong suy gan nặng",
          "Thận trọng ở bệnh nhân hen phế quản/COPD (non-selective, có thể gây co thắt phế quản nặng)",
          "Tránh dùng trong suy tim cấp không bù, block AV độ 2-3, nhịp tim chậm <60 bpm",
          "Có thể gây hạ huyết áp nặng (do tác dụng alpha-blocking) - theo dõi sát khi bắt đầu",
          "Thận trọng khi dùng với digoxin (tăng nồng độ digoxin)",
          "Thận trọng với CYP2D6 inhibitors (tăng nồng độ carvedilol)"
      ],
      "pharmacokinetics": {
          "half_life": "7-10 giờ",
          "onset": "1-2 giờ (PO)",
          "duration": "12-24 giờ (uống 2 lần/ngày)",
          "protein_binding": "98% (rất cao)",
          "clearance": "Gan (chủ yếu, chuyển hóa qua CYP2D6, CYP2C9, CYP3A4). Thải qua phân và nước tiểu"
      },
      "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm, tránh ánh sáng",
      "black_box_warnings": "KHÔNG được ngừng đột ngột ở bệnh nhân đau thắt ngực hoặc suy tim - có thể gây đau thắt ngực nặng, nhồi máu cơ tim, suy tim nặng. Phải giảm liều dần dần trong 1-2 tuần",
      "drug_interactions": {
          "major": [
              {
                  "drug": "Verapamil, Diltiazem",
                  "mechanism": "Tác dụng hiệp đồng ức chế dẫn truyền nhĩ thất",
                  "effect": "Tăng nguy cơ block nhĩ thất độ 2-3, suy tim, nhịp tim chậm nặng",
                  "management": "Thận trọng. Theo dõi ECG, nhịp tim, huyết áp. Tránh dùng cùng nếu có thể."
              },
              {
                  "drug": "CYP2D6 inhibitors (fluoxetine, paroxetine, quinidine)",
                  "mechanism": "Ức chế chuyển hóa carvedilol qua CYP2D6",
                  "effect": "Tăng nồng độ carvedilol đáng kể, tăng tác dụng phụ (hạ huyết áp, nhịp tim chậm)",
                  "management": "Thận trọng. Giảm liều carvedilol. Theo dõi nhịp tim, huyết áp sát."
              }
          ],
          "moderate": [
              {
                  "drug": "Digoxin",
                  "mechanism": "Carvedilol tăng nồng độ digoxin",
                  "effect": "Tăng nguy cơ ngộ độc digoxin (nhịp tim chậm, block AV, rối loạn nhịp)",
                  "management": "Theo dõi nồng độ digoxin. Có thể cần giảm liều digoxin."
              },
              {
                  "drug": "CYP3A4 inhibitors (ketoconazole, itraconazole, clarithromycin)",
                  "mechanism": "Ức chế chuyển hóa carvedilol qua CYP3A4",
                  "effect": "Tăng nồng độ carvedilol, tăng tác dụng phụ",
                  "management": "Thận trọng. Theo dõi nhịp tim, huyết áp. Có thể cần giảm liều carvedilol."
              },
              {
                  "drug": "Insulin, Sulfonylureas",
                  "mechanism": "Che dấu triệu chứng hạ đường huyết",
                  "effect": "Hạ đường huyết nặng, khó nhận biết triệu chứng",
                  "management": "Theo dõi đường huyết thường xuyên."
              }
          ],
          "minor": [
              {
                  "drug": "NSAIDs",
                  "mechanism": "Giảm tác dụng hạ huyết áp",
                  "effect": "Giảm hiệu quả hạ huyết áp",
                  "management": "Theo dõi huyết áp."
              }
          ]
      },
      "contraindications": {
          "absolute": [
              "Hen phế quản nặng",
              "Block nhĩ thất độ 2-3 không có máy tạo nhịp",
              "Suy tim cấp không bù",
              "Nhịp tim chậm nặng (<60 bpm)",
              "Suy gan nặng",
              "Sốc tim"
          ],
          "relative": [
              "COPD - thận trọng (non-selective beta-blocker, có thể gây co thắt phế quản nặng)",
              "Suy gan trung bình - thận trọng, giảm liều (thải chủ yếu qua gan)",
              "Suy thận nặng - thận trọng",
              "Đái tháo đường - thận trọng (che dấu triệu chứng hạ đường huyết)",
              "Dùng với verapamil/diltiazem - tăng nguy cơ block AV",
              "Dùng với CYP2D6 inhibitors - tăng nồng độ carvedilol đáng kể"
          ]
      },
      "pregnancy_lactation": {
          "fda_category": "C",
          "pregnancy_details": "Có thể gây hạ huyết áp, nhịp tim chậm ở thai nhi. Có thể gây chậm phát triển thai nhi, nhịp tim chậm ở trẻ sơ sinh. Cân nhắc lợi ích/nguy cơ. Thường dùng được nếu lợi ích vượt trội nguy cơ, đặc biệt trong suy tim.",
          "lactation": {
              "safety": "Compatible",
              "details": "Carvedilol bài tiết vào sữa mẹ ở nồng độ thấp. Nồng độ trong máu trẻ bú mẹ thường rất thấp. Có thể gây nhịp tim chậm nhẹ ở trẻ bú mẹ nhưng hiếm.",
              "recommendation": "Có thể dùng khi cho con bú. Theo dõi trẻ nếu có nhịp tim chậm, mệt mỏi, tăng cân kém."
          }
      },
      "hepatic_adjustment": {
          "mild": "Không đổi",
          "moderate": "Thận trọng, giảm liều (thải chủ yếu qua gan)",
          "severe": "CHỐNG CHỈ ĐỊNH (thải chủ yếu qua gan, chuyển hóa qua CYP2D6, CYP2C9, CYP3A4)",
          "notes": "Carvedilol thải chủ yếu qua gan (chuyển hóa qua CYP2D6, CYP2C9, CYP3A4). Suy gan nặng là chống chỉ định tuyệt đối. Suy gan trung bình cần giảm liều và theo dõi sát."
      },
      "overdose_management": {
          "symptoms": [
              "Nhịp tim chậm nặng (<40 bpm)",
              "Block nhĩ thất độ 2-3",
              "Hạ huyết áp nặng (do cả beta và alpha-blocking)",
              "Suy tim cấp",
              "Co giật",
              "Hôn mê",
              "Suy hô hấp"
          ],
          "antidote": "Glucagon (có thể đảo ngược tác dụng beta-blocker), Atropine (cho nhịp tim chậm), Epinephrine (cho hạ huyết áp nặng)",
          "treatment": [
              "Rửa dạ dày nếu uống trong vòng 1-2 giờ",
              "Than hoạt tính",
              "Điều trị nhịp tim chậm: Atropine 0.5-1mg IV, có thể lặp lại. Nếu không hiệu quả: Glucagon 1-5mg IV, Isoproterenol, hoặc máy tạo nhịp tạm thời",
              "Điều trị hạ huyết áp: Truyền dịch (normal saline), nâng chân, Glucagon 1-5mg IV, Epinephrine (thận trọng - có thể gây tăng huyết áp quá mức)",
              "Theo dõi ECG liên tục",
              "Theo dõi huyết áp, nhịp tim, ý thức",
              "Hỗ trợ hô hấp nếu cần",
              "Theo dõi ít nhất 24-48 giờ (do half-life 7-10 giờ)"
          ],
          "monitoring": "ECG liên tục, huyết áp, nhịp tim, ý thức, dấu hiệu suy tim, dấu hiệu suy hô hấp"
      },
      "reversal_agents": {
          "available": True,
          "agents": [
              {
                  "name": "Glucagon",
                  "mechanism": "Kích thích cAMP, đảo ngược tác dụng beta-blocker",
                  "dose": "1-5mg IV, có thể lặp lại",
                  "indication": "Nhịp tim chậm, hạ huyết áp do quá liều beta-blocker"
              },
              {
                  "name": "Atropine",
                  "mechanism": "Chẹn muscarinic, tăng nhịp tim",
                  "dose": "0.5-1mg IV, có thể lặp lại",
                  "indication": "Nhịp tim chậm, block AV"
              },
              {
                  "name": "Epinephrine",
                  "mechanism": "Agonist alpha và beta, tăng nhịp tim và huyết áp",
                  "dose": "Theo protocol ACLS",
                  "indication": "Hạ huyết áp nặng không đáp ứng với glucagon"
              }
          ]
      },
      "administration_instructions": {
          "oral": {
              "with_food": "Nên uống với thức ăn để giảm nguy cơ hạ huyết áp và tăng hấp thu.",
              "timing": "Uống 2 lần/ngày (sáng và tối). Ở bệnh nhân suy tim: khởi đầu với liều rất thấp (3.125mg x 2 lần/ngày), tăng dần mỗi 2 tuần. KHÔNG ngừng đột ngột - phải giảm liều dần trong 1-2 tuần."
          },
          "iv": {
              "reconstitution": "Không có dạng IV",
              "infusion_rate": "Không áp dụng",
              "compatibility": [],
              "incompatibility": [],
              "notes": "Carvedilol chỉ có dạng uống (PO)."
          }
      },
      "references": {
          "primary_sources": [
              "FDA Drug Label - Coreg (carvedilol)",
              "UpToDate - Carvedilol: Drug information",
              "COPERNICUS Study - New England Journal of Medicine (2001) - Carvedilol trong suy tim nặng",
              "CAPRICORN Study - Lancet (2001) - Carvedilol sau nhồi máu cơ tim",
              "American Heart Association/American College of Cardiology guidelines - Beta-blockers in heart failure"
          ],
          "last_updated": "2024-12-19",
          "evidence_level": "High - Multiple large RCTs (COPERNICUS, CAPRICORN) showing mortality benefit in heart failure and extensive clinical experience"
      }
  }
}

__all__ = ['CARDIOVASCULAR_DRUGS']
