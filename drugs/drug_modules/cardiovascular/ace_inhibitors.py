"""
ACE Inhibitors - Angiotensin Converting Enzyme Inhibitors
"""

ACE_INHIBITORS = {
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
            "tuyệt_đối": [
                "Dị ứng ACE inhibitor",
                "Có thai",
                "Hẹp động mạch thận 2 bên",
                "Phù mạch trước đây với ACE inhibitor"
            ],
            "tương_đối": [
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
        "pediatric_dosing": {
            "neonates": "Không khuyến cáo cho trẻ <1 tháng tuổi",
            "infants": "0.15-0.3mg/kg x 3 lần/ngày (tối đa 6mg/kg/ngày). Khởi đầu với liều thấp, tăng dần",
            "children": "0.5-2mg/kg/ngày chia 2-3 lần (tối đa 6mg/kg/ngày). Khởi đầu với liều thấp, tăng dần",
            "adolescents": "6.25-25mg x 2-3 lần/ngày, tăng dần đến 50mg x 3 lần/ngày nếu cần",
            "notes": "Dùng cho tăng huyết áp và suy tim ở trẻ em. Khởi đầu với liều thấp, tăng dần. Uống 1 giờ trước bữa ăn. Theo dõi huyết áp, chức năng thận, kali máu"
        },
        "geriatric_dosing": {
            "considerations": "Người cao tuổi nhạy cảm hơn với tác dụng hạ huyết áp. Suy thận phổ biến hơn",
            "dose_adjustment": "Khởi đầu với liều thấp hơn (6.25mg x 2 lần/ngày). Tăng dần chậm hơn. Điều chỉnh theo CrCl",
            "monitoring": "Theo dõi huyết áp sát hơn (nguy cơ hạ huyết áp quá mức). Theo dõi chức năng thận, kali máu thường xuyên"
        },
        "brand_names": {
            "vietnam": ["Capoten", "Captopril Stada", "Captopril", "Acepril"],
            "common": ["Capoten", "Captopril"]
        },
        "cost_estimate": {
            "unit": "VND",
            "range": "15,000 - 40,000 VND/viên (tùy hàm lượng và thương hiệu)",
            "note": "Giá thay đổi theo thương hiệu và nhà thuốc. Captopril generic thường rẻ hơn (15,000-25,000 VND/viên 25mg)."
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
            "tuyệt_đối": [
                "Dị ứng ACE inhibitor",
                "Có thai",
                "Hẹp động mạch thận 2 bên",
                "Phù mạch trước đây với ACE inhibitor"
            ],
            "tương_đối": [
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
        "pediatric_dosing": {
            "neonates": "Không khuyến cáo cho trẻ <1 tháng tuổi",
            "infants": "0.1-0.5mg/kg/ngày chia 1-2 lần. Khởi đầu với liều thấp, tăng dần",
            "children": "0.1-0.5mg/kg/ngày chia 1-2 lần (tối đa 40mg/ngày). Khởi đầu với liều thấp, tăng dần",
            "adolescents": "2.5-10mg x 1-2 lần/ngày, tăng dần đến 20-40mg/ngày nếu cần",
            "notes": "Dùng cho tăng huyết áp và suy tim ở trẻ em. Khởi đầu với liều thấp, tăng dần. Có thể dùng 1-2 lần/ngày. Theo dõi huyết áp, chức năng thận, kali máu"
        },
        "geriatric_dosing": {
            "considerations": "Người cao tuổi nhạy cảm hơn với tác dụng hạ huyết áp. Suy thận phổ biến hơn",
            "dose_adjustment": "Khởi đầu với liều thấp hơn (2.5mg x 1 lần/ngày). Tăng dần chậm hơn. Điều chỉnh theo CrCl",
            "monitoring": "Theo dõi huyết áp sát hơn (nguy cơ hạ huyết áp quá mức). Theo dõi chức năng thận, kali máu thường xuyên"
        },
        "brand_names": {
            "vietnam": ["Renitec", "Enalapril Stada", "Enalapril", "Vasotec"],
            "common": ["Vasotec", "Enalapril", "Renitec"]
        },
        "cost_estimate": {
            "unit": "VND",
            "range": "20,000 - 50,000 VND/viên (tùy hàm lượng và thương hiệu)",
            "note": "Giá thay đổi theo thương hiệu và nhà thuốc. Enalapril generic thường rẻ hơn (20,000-35,000 VND/viên 5mg)."
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
            "tuyệt_đối": [
                "Dị ứng ACE inhibitor",
                "Có thai",
                "Hẹp động mạch thận 2 bên",
                "Phù mạch trước đây với ACE inhibitor"
            ],
            "tương_đối": [
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
        "pediatric_dosing": {
            "neonates": "Không khuyến cáo cho trẻ <6 tuổi (dữ liệu hạn chế)",
            "infants": "Không khuyến cáo cho trẻ <6 tuổi (dữ liệu hạn chế)",
            "children": "0.07-0.6mg/kg/ngày x 1 lần/ngày (tối đa 40mg/ngày). Khởi đầu với liều thấp, tăng dần. Chỉ dùng cho trẻ ≥6 tuổi",
            "adolescents": "5-10mg x 1 lần/ngày, tăng dần đến 20-40mg/ngày nếu cần",
            "notes": "Dùng cho tăng huyết áp ở trẻ em ≥6 tuổi. Khởi đầu với liều thấp, tăng dần. Ưu điểm: dùng 1 lần/ngày (compliance tốt). Theo dõi huyết áp, chức năng thận, kali máu"
        },
        "geriatric_dosing": {
            "considerations": "Người cao tuổi nhạy cảm hơn với tác dụng hạ huyết áp. Suy thận phổ biến hơn",
            "dose_adjustment": "Khởi đầu với liều thấp hơn (2.5-5mg x 1 lần/ngày). Tăng dần chậm hơn. Điều chỉnh theo CrCl",
            "monitoring": "Theo dõi huyết áp sát hơn (nguy cơ hạ huyết áp quá mức). Theo dõi chức năng thận, kali máu thường xuyên"
        },
        "brand_names": {
            "vietnam": ["Zestril", "Lisinopril Stada", "Lisinopril", "Prinivil"],
            "common": ["Zestril", "Prinivil", "Lisinopril"]
        },
        "cost_estimate": {
            "unit": "VND",
            "range": "25,000 - 60,000 VND/viên (tùy hàm lượng và thương hiệu)",
            "note": "Giá thay đổi theo thương hiệu và nhà thuốc. Lisinopril generic thường rẻ hơn (25,000-40,000 VND/viên 10mg)."
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

}

__all__ = ['ACE_INHIBITORS']
