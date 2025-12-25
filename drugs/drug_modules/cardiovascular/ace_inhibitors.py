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
        "risk_flags": {
            "high_alert": False,
            "narrow_therapeutic_index": False,
            "icu_critical_care_only": False,
            "bleeding_risk": "Low",
            "organ_toxicity": ["hyperkalemia", "renal_impairment", "angioedema"]
        },
        "guideline_tags": [
            "ACC/AHA/HFSA HFrEF ACEi Class I",
            "ESC HFrEF ACEi Class I"
        ],
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
        "risk_flags": {
            "high_alert": False,
            "narrow_therapeutic_index": False,
            "icu_critical_care_only": False,
            "bleeding_risk": "Low",
            "organ_toxicity": ["hyperkalemia", "renal_impairment", "angioedema"]
        },
        "guideline_tags": [
            "ACC/AHA/HFSA HFrEF ACEi Class I",
            "ESC HFrEF ACEi Class I"
        ],
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

    "Benazepril": {
        "group": "Cardiovascular - ACE Inhibitor",
        "vietnamese_name": "Benazepril, Lotensin",
        "administration": ["PO"],
        "indications": [
            "Tăng huyết áp (đơn trị hoặc phối hợp)",
            "Suy tim (off-label, khi không dung nạp ACE khác)",
            "Bảo vệ thận trong đái tháo đường (off-label)"
        ],
        "contraindications": [
            "Dị ứng ACE inhibitor hoặc benazepril",
            "Có thai",
            "Hẹp động mạch thận 2 bên hoặc hẹp đơn thận còn lại",
            "Tiền sử phù mạch do ACE inhibitor"
        ],
        "dosage": {
            "adult_htn": "10-40mg x 1-2 lần/ngày",
            "adult_htn_initial": "10mg x 1 lần/ngày (không dùng lợi tiểu) hoặc 5mg nếu đang dùng lợi tiểu",
            "adult_heart_failure_off_label": "2.5-5mg x 1-2 lần/ngày, tăng dần đến 20-40mg/ngày",
            "notes": "Có thể dùng 1 hoặc 2 lần/ngày. Điều chỉnh liều theo đáp ứng huyết áp và chức năng thận."
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "Liều khởi đầu 5mg/ngày",
            "under_30": "Liều khởi đầu 2.5-5mg/ngày, theo dõi sát creatinine và kali"
        },
        "side_effects": [
            "Ho khan",
            "Tăng kali máu",
            "Hạ huyết áp (đặc biệt liều đầu hoặc khi có lợi tiểu)",
            "Suy thận cấp (hẹp động mạch thận, mất nước)",
            "Phù mạch (hiếm nhưng đe dọa tính mạng)",
            "Đau đầu, chóng mặt"
        ],
        "interactions": [
            "Kali bổ sung và lợi tiểu giữ kali (spironolactone, eplerenone, amiloride, triamterene): tăng nguy cơ tăng kali máu",
            "NSAID: giảm hiệu quả hạ huyết áp, tăng nguy cơ suy thận",
            "Lithium: tăng nồng độ lithium",
            "Diuretics: hiệp đồng hạ huyết áp, tăng nguy cơ tụt huyết áp liều đầu"
        ],
        "pregnancy": "D - Chống chỉ định trong thai kỳ",
        "mechanism_of_action": "Benazepril là prodrug, chuyển hóa tại gan thành benazeprilat (hoạt chất). Ức chế men chuyển angiotensin (ACE), giảm chuyển angiotensin I thành angiotensin II, giảm tiết aldosterone → giãn mạch, giảm hậu tải và tiền tải, giảm huyết áp và bảo vệ thận. Giống ACE khác, làm tăng bradykinin nên gây ho khan/phù mạch.",
        "monitoring": [
            "Huyết áp (đặc biệt 2-4 giờ sau liều đầu/ tăng liều)",
            "Creatinine, BUN trước điều trị và 1-2 tuần sau khi bắt đầu/tăng liều",
            "Kali máu định kỳ",
            "Dấu hiệu ho khan kéo dài",
            "Dấu hiệu phù mạch (sưng mặt, môi, lưỡi, khó thở) – cấp cứu"
        ],
        "precautions": [
            "Khởi đầu liều thấp ở bệnh nhân đang dùng lợi tiểu, suy tim, người già, hạ thể tích tuần hoàn.",
            "Tránh dùng đồng thời với aliskiren ở bệnh nhân đái tháo đường (tăng biến cố thận, tăng kali, hạ HA).",
            "Ngừng ngay nếu có phù mạch hoặc nghi ngờ phù mạch.",
            "Thận trọng khi phối hợp với NSAID (giảm hiệu quả, tăng nguy cơ suy thận).",
            "Không dùng chung với sacubitril-valsartan trong vòng 36 giờ (nguy cơ phù mạch tăng cao)."
        ],
        "pharmacokinetics": {
            "half_life": "Benazepril: ~2 giờ; Benazeprilat: 10-12 giờ",
            "onset": "1 giờ",
            "duration": "24 giờ (cho phép dùng 1 lần/ngày)",
            "protein_binding": "~96%",
            "clearance": "Thận (chủ yếu) và mật (một phần) dưới dạng benazeprilat"
        },
        "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm, tránh ánh sáng.",
        "black_box_warnings": "CHỐNG CHỈ ĐỊNH trong thai kỳ. ACE inhibitor (bao gồm benazepril) có thể gây dị tật và tử vong thai nhi (thiểu ối, thiểu sản sọ, suy thận thai, tử vong sơ sinh). Ngừng ngay khi phát hiện có thai. Phù mạch có thể đe dọa tính mạng.",
        "drug_interactions": {
            "major": [
                {
                    "drug": "Kali bổ sung, Lợi tiểu giữ kali (spironolactone, eplerenone, amiloride, triamterene)",
                    "mechanism": "Giảm thải trừ kali do ức chế aldosterone + cung cấp thêm kali",
                    "effect": "Tăng kali máu nặng, nguy cơ loạn nhịp",
                    "management": "Tránh phối hợp nếu có thể, hoặc theo dõi kali chặt chẽ, chỉnh liều."
                },
                {
                    "drug": "NSAIDs",
                    "mechanism": "Ức chế prostaglandin thận, giảm dòng máu thận",
                    "effect": "Giảm hiệu quả hạ huyết áp, tăng nguy cơ suy thận cấp (đặc biệt ở người cao tuổi, mất nước).",
                    "management": "Hạn chế dùng lâu dài, theo dõi creatinine/kali khi bắt đầu hoặc thay đổi liều."
                }
            ],
            "moderate": [
                {
                    "drug": "Lithium",
                    "mechanism": "Giảm thải trừ lithium qua thận",
                    "effect": "Tăng nồng độ lithium, nguy cơ độc tính thần kinh",
                    "management": "Theo dõi nồng độ lithium, cân nhắc giảm liều hoặc tránh phối hợp."
                },
                {
                    "drug": "Diuretics",
                    "mechanism": "Hiệp đồng giảm thể tích và giãn mạch",
                    "effect": "Tụt huyết áp liều đầu, chóng mặt, ngất",
                    "management": "Giảm/ ngừng tạm lợi tiểu trước khi khởi đầu benazepril, tăng liều từ từ."
                }
            ],
            "minor": []
        },
        "contraindications": {
            "tuyệt_đối": [
                "Dị ứng với benazepril hoặc ACE inhibitor",
                "Có thai hoặc dự định có thai",
                "Hẹp động mạch thận 2 bên hoặc hẹp động mạch thận của thận độc nhất",
                "Tiền sử phù mạch do ACE inhibitor hoặc phù mạch di truyền/vô căn"
            ],
            "tương_đối": [
                "Suy thận trung bình-nặng",
                "Tăng kali máu",
                "Mất nước, hạ thể tích tuần hoàn",
                "Hẹp van động mạch chủ nặng",
                "Phối hợp ARB hoặc aliskiren (triple blockade RAAS)"
            ]
        },
        "pregnancy_lactation": {
            "fda_category": "D",
            "pregnancy_details": "CHỐNG CHỈ ĐỊNH tuyệt đối trong thai kỳ. Nguy cơ dị tật và tử vong thai nhi, đặc biệt ở tam cá nguyệt 2-3.",
            "lactation": {
                "safety": "Caution",
                "details": "Benazepril/benazeprilat bài tiết một phần vào sữa; dữ liệu còn hạn chế.",
                "recommendation": "Ưu tiên ACE khác đã có dữ liệu hơn (captopril/enalapril) ở mẹ cho con bú; nếu dùng benazepril, theo dõi trẻ."
            }
        },
        "hepatic_adjustment": {
            "mild": "Thường không cần chỉnh liều",
            "moderate": "Thận trọng, có thể cần liều khởi đầu thấp hơn (5mg/ngày)",
            "severe": "Thận trọng, cân nhắc ACE khác; dữ liệu hạn chế",
            "notes": "Benazepril là prodrug chuyển hóa ở gan thành benazeprilat; suy gan có thể làm chậm chuyển hóa, nhưng thuốc vẫn chủ yếu thải trừ qua thận."
        },
        "overdose_management": {
            "symptoms": [
                "Hạ huyết áp nặng",
                "Chóng mặt, ngất",
                "Suy thận cấp",
                "Tăng kali máu"
            ],
            "antidote": "Không có antidote đặc hiệu",
            "treatment": [
                "Đặt bệnh nhân tư thế nằm, nâng chân, truyền dịch (NaCl 0.9%)",
                "Vasopressor (norepinephrine) nếu tụt HA dai dẳng",
                "Điều trị tăng kali máu nếu có (calcium gluconate, insulin + glucose, bicarbonate)",
                "Theo dõi huyết áp, nhịp tim, chức năng thận, điện giải"
            ],
            "monitoring": "Huyết áp, nhịp tim, creatinine, kali, ý thức."
        },
        "reversal_agents": {
            "available": False,
            "agents": []
        },
        "administration_instructions": {
            "oral": {
                "with_food": "Có thể uống với hoặc không cùng thức ăn.",
                "timing": "Uống 1-2 lần/ngày, cùng giờ mỗi ngày. Khởi đầu liều thấp, tăng dần."
            }
        },
        "references": {
            "primary_sources": [
                "FDA Drug Label - Lotensin (benazepril)",
                "UpToDate - Benazepril: Drug information",
                "ACC/AHA Hypertension Guidelines 2024"
            ],
            "last_updated": "2025-02-18",
            "evidence_level": "High – FDA-approved, sử dụng rộng rãi trong tăng huyết áp"
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
        "risk_flags": {
            "high_alert": False,
            "narrow_therapeutic_index": False,
            "icu_critical_care_only": False,
            "bleeding_risk": "Low",
            "organ_toxicity": ["hyperkalemia", "renal_impairment", "angioedema"]
        },
        "guideline_tags": [
            "ACC/AHA/HFSA HFrEF ACEi Class I",
            "ESC HFrEF ACEi Class I"
        ],
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
    
    "Ramipril": {
        "group": "Cardiovascular - ACE Inhibitor",
        "vietnamese_name": "Ramipril, Altace, Tritace",
        "administration": ["PO"],
        "indications": [
            "Tăng huyết áp",
            "Suy tim",
            "Bảo vệ thận trong đái tháo đường",
            "Dự phòng biến cố tim mạch sau nhồi máu cơ tim",
            "Dự phòng đột quỵ ở bệnh nhân nguy cơ cao"
        ],
        "contraindications": [
            "Dị ứng ACE inhibitor",
            "Có thai",
            "Hẹp động mạch thận 2 bên",
            "Phù mạch trước đây với ACE inhibitor"
        ],
        "dosage": {
            "adult_htn": "2.5-10mg x 1 lần/ngày",
            "adult_heart_failure": "1.25-2.5mg x 1 lần/ngày, tăng dần đến 10mg x 1 lần/ngày",
            "adult_post_mi": "2.5mg x 2 lần/ngày, tăng đến 5mg x 2 lần/ngày",
            "adult_cvd_prevention": "10mg x 1 lần/ngày",
            "notes": "Khởi đầu với liều thấp, tăng dần. Uống với hoặc không có thức ăn"
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "Giảm liều 25-50%",
            "under_30": "Khởi đầu 1.25mg/ngày, tối đa 5mg/ngày"
        },
        "side_effects": [
            "Ho khan (phổ biến)",
            "Tăng kali máu",
            "Hạ huyết áp",
            "Phù mạch (hiếm nhưng nguy hiểm)",
            "Suy thận cấp (hẹp ĐM thận)",
            "Tăng creatinine nhẹ"
        ],
        "interactions": [
            "Kali bổ sung: tăng nguy cơ tăng kali máu",
            "Spironolactone: tăng kali máu",
            "NSAID: giảm hiệu quả, tăng nguy cơ suy thận",
            "Lithium: tăng nồng độ lithium",
            "Diuretics: tăng nguy cơ hạ huyết áp"
        ],
        "pregnancy": "D - Chống chỉ định trong thai kỳ",
        "risk_flags": {
            "high_alert": False,
            "narrow_therapeutic_index": False,
            "icu_critical_care_only": False,
            "bleeding_risk": "Low",
            "organ_toxicity": ["hyperkalemia", "renal_impairment", "angioedema"]
        },
        "guideline_tags": [
            "ACC/AHA/HFSA HFrEF ACEi Class I",
            "ESC HFrEF ACEi Class I"
        ],
        "mechanism_of_action": "Ramipril là prodrug, được chuyển hóa thành ramiprilat (hoạt chất). Ức chế angiotensin converting enzyme (ACE), giảm chuyển angiotensin I thành angiotensin II, giảm aldosterone, gây giãn mạch và giảm huyết áp. Ramipril có half-life dài hơn so với captopril và enalapril, cho phép dùng 1 lần/ngày. Có bằng chứng mạnh về bảo vệ tim mạch và thận (HOPE study).",
        "monitoring": [
            "Creatinine, BUN sau 1-2 tuần khi bắt đầu",
            "Kali máu định kỳ",
            "Huyết áp",
            "Ho khan (tác dụng phụ thường gặp)",
            "Dấu hiệu phù mạch (sưng mặt, lưỡi, họng - cấp cứu)"
        ],
        "precautions": [
            "Khởi đầu với liều thấp, tăng dần",
            "Theo dõi sát creatinine khi bắt đầu (có thể tăng nhẹ)",
            "Tránh dùng với NSAID (giảm hiệu quả, tăng nguy cơ suy thận)",
            "Ngừng ngay nếu có phù mạch (có thể nguy hiểm tính mạng)",
            "Ho khan có thể kéo dài, thường tự hết khi ngừng thuốc",
            "Thận trọng với kali bổ sung và kali-sparing diuretics"
        ],
        "pharmacokinetics": {
            "half_life": "13-17 giờ (ramiprilat - metabolite hoạt động)",
            "onset": "1-2 giờ",
            "duration": "24 giờ (cho phép dùng 1 lần/ngày)",
            "protein_binding": "73% (ramiprilat)",
            "clearance": "Thận (60% bài tiết qua nước tiểu)"
        },
        "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm, tránh ánh sáng",
        "black_box_warnings": "Chống chỉ định trong thai kỳ - có thể gây dị tật thai nhi và tử vong thai nhi. Phù mạch có thể đe dọa tính mạng.",
        "drug_interactions": {
            "major": [
                {
                    "drug": "Kali bổ sung, Kali-sparing diuretics (spironolactone, eplerenone, amiloride, triamterene)",
                    "mechanism": "Tác dụng hiệp đồng tăng kali máu",
                    "effect": "Tăng kali máu nghiêm trọng, có thể gây rối loạn nhịp tim",
                    "management": "Thận trọng. Theo dõi kali máu thường xuyên. Tránh dùng cùng nếu có thể."
                },
                {
                    "drug": "NSAIDs (ibuprofen, naproxen, diclofenac, etc.)",
                    "mechanism": "NSAIDs ức chế prostaglandin, làm giảm lưu lượng máu thận, giảm hiệu quả ACE inhibitor. NSAIDs cũng có thể gây giữ natri và nước.",
                    "effect": "Giảm hiệu quả hạ huyết áp của ramipril, tăng nguy cơ suy thận cấp, đặc biệt ở bệnh nhân suy thận, suy tim, hoặc dùng diuretics",
                    "management": "Tránh dùng đồng thời nếu có thể. Nếu bắt buộc, theo dõi chặt chẽ huyết áp, chức năng thận (creatinine, BUN). Giảm liều NSAID hoặc ngừng nếu có dấu hiệu suy thận."
                }
            ],
            "moderate": [
                {
                    "drug": "Lithium",
                    "mechanism": "ACE inhibitors làm giảm thải trừ lithium qua thận, tăng nồng độ lithium.",
                    "effect": "Tăng nồng độ lithium, tăng độc tính (buồn nôn, run, lú lẫn, co giật)",
                    "management": "Theo dõi nồng độ lithium thường xuyên. Giảm liều lithium khi bắt đầu ramipril. Theo dõi dấu hiệu độc tính lithium."
                },
                {
                    "drug": "Diuretics (thiazide, loop diuretics)",
                    "mechanism": "Tác dụng hiệp đồng hạ huyết áp, có thể gây hạ huyết áp quá mức.",
                    "effect": "Hạ huyết áp quá mức, chóng mặt, ngất",
                    "management": "Giảm liều diuretic hoặc ngừng tạm thời khi bắt đầu ramipril. Khởi đầu ramipril với liều thấp."
                }
            ],
            "minor": []
        },
        "contraindications": {
            "tuyệt_đối": [
                "Dị ứng ramipril hoặc các ACE inhibitor khác",
                "Có thai (tất cả các tam cá nguyệt) - gây dị tật thai nhi",
                "Hẹp động mạch thận 2 bên hoặc hẹp động mạch thận ở thận đơn độc",
                "Phù mạch trước đây với ACE inhibitor"
            ],
            "tương_đối": [
                "Suy thận nặng (CrCl <30) - cần giảm liều",
                "Suy gan - thận trọng",
                "Hẹp van động mạch chủ nặng",
                "Tăng kali máu",
                "Dùng với kali-sparing diuretics hoặc kali bổ sung"
            ]
        },
        "pregnancy_lactation": {
            "fda_category": "D",
            "pregnancy_details": "Chống chỉ định trong thai kỳ - có thể gây dị tật thai nhi (hệ thần kinh, hệ tim mạch) và tử vong thai nhi. Ngừng ngay khi phát hiện có thai.",
            "lactation": {
                "safety": "Compatible",
                "details": "Ramipril bài tiết vào sữa mẹ ở nồng độ thấp. An toàn cho trẻ bú mẹ.",
                "recommendation": "Có thể dùng khi cho con bú. Theo dõi trẻ sơ sinh nếu dùng liều cao."
            }
        },
        "hepatic_adjustment": {
            "mild": "Không cần điều chỉnh liều",
            "moderate": "Thận trọng, có thể cần giảm liều nhẹ",
            "severe": "Thận trọng, giảm liều hoặc tránh dùng",
            "notes": "Ramipril chuyển hóa một phần ở gan thành ramiprilat (hoạt chất). Suy gan có thể giảm chuyển hóa nhưng không đáng kể."
        },
        "overdose_management": {
            "symptoms": [
                "Hạ huyết áp nghiêm trọng",
                "Chóng mặt, ngất",
                "Tăng kali máu",
                "Suy thận cấp",
                "Nhịp tim chậm"
            ],
            "antidote": "Không có antidote đặc hiệu. Điều trị hỗ trợ.",
            "treatment": [
                "Ngừng ngay ramipril",
                "Nằm đầu thấp, nâng chân",
                "Truyền dịch nếu hạ huyết áp",
                "Theo dõi huyết áp, nhịp tim, điện giải",
                "Điều trị tăng kali máu nếu có",
                "Lọc máu nếu suy thận nặng"
            ],
            "monitoring": "Huyết áp, nhịp tim, kali máu, chức năng thận trong ít nhất 24 giờ"
        },
        "reversal_agents": None,
        "administration_instructions": {
            "oral": {
                "with_food": "Có thể uống với hoặc không có thức ăn. Hấp thu tốt trong cả hai trường hợp.",
                "timing": "Uống 1 lần/ngày (do half-life dài). Có thể uống buổi sáng hoặc tối. Uống đều đặn cùng một thời điểm mỗi ngày."
            },
            "iv": {
                "reconstitution": "N/A - Chỉ có dạng uống",
                "infusion_rate": "N/A",
                "compatibility": [],
                "incompatibility": [],
                "notes": "Ramipril chỉ có dạng uống. Nếu cần dạng IV, dùng enalaprilat."
            }
        },
        "references": {
            "primary_sources": [
                "FDA Drug Label - Altace (ramipril)",
                "UpToDate - Ramipril: Drug information",
                "HOPE Study - New England Journal of Medicine",
                "American Heart Association/American College of Cardiology guidelines"
            ],
            "last_updated": "2025-02-05",
            "evidence_level": "High - HOPE study (large RCT) and extensive clinical experience"
        }
    },
    
    "Perindopril": {
        "group": "Cardiovascular - ACE Inhibitor",
        "vietnamese_name": "Perindopril, Coversyl, Aceon",
        "administration": ["PO"],
        "indications": [
            "Tăng huyết áp",
            "Suy tim",
            "Dự phòng biến cố tim mạch sau nhồi máu cơ tim",
            "Dự phòng đột quỵ ở bệnh nhân nguy cơ cao"
        ],
        "contraindications": [
            "Dị ứng ACE inhibitor",
            "Có thai",
            "Hẹp động mạch thận 2 bên",
            "Phù mạch trước đây với ACE inhibitor"
        ],
        "dosage": {
            "adult_htn": "4-8mg x 1 lần/ngày",
            "adult_heart_failure": "2mg x 1 lần/ngày, tăng dần đến 8mg x 1 lần/ngày",
            "adult_post_mi": "4mg x 1 lần/ngày, tăng đến 8mg x 1 lần/ngày",
            "adult_cvd_prevention": "8mg x 1 lần/ngày",
            "notes": "Khởi đầu với liều thấp, tăng dần. Uống với hoặc không có thức ăn"
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "Giảm liều 25-50%",
            "under_30": "Khởi đầu 2mg/ngày, tối đa 4mg/ngày"
        },
        "side_effects": [
            "Ho khan (phổ biến)",
            "Tăng kali máu",
            "Hạ huyết áp",
            "Phù mạch (hiếm nhưng nguy hiểm)",
            "Suy thận cấp (hẹp ĐM thận)",
            "Tăng creatinine nhẹ"
        ],
        "interactions": [
            "Kali bổ sung: tăng nguy cơ tăng kali máu",
            "Spironolactone: tăng kali máu",
            "NSAID: giảm hiệu quả, tăng nguy cơ suy thận",
            "Lithium: tăng nồng độ lithium",
            "Diuretics: tăng nguy cơ hạ huyết áp"
        ],
        "pregnancy": "D - Chống chỉ định trong thai kỳ",
        "mechanism_of_action": "Perindopril là prodrug, được chuyển hóa thành perindoprilat (hoạt chất). Ức chế angiotensin converting enzyme (ACE), giảm chuyển angiotensin I thành angiotensin II, giảm aldosterone, gây giãn mạch và giảm huyết áp. Perindopril có half-life dài, cho phép dùng 1 lần/ngày. Có bằng chứng mạnh về bảo vệ tim mạch và thận (PROGRESS study, EUROPA study).",
        "monitoring": [
            "Creatinine, BUN sau 1-2 tuần khi bắt đầu",
            "Kali máu định kỳ",
            "Huyết áp",
            "Ho khan (tác dụng phụ thường gặp)",
            "Dấu hiệu phù mạch (sưng mặt, lưỡi, họng - cấp cứu)"
        ],
        "precautions": [
            "Khởi đầu với liều thấp, tăng dần",
            "Theo dõi sát creatinine khi bắt đầu (có thể tăng nhẹ)",
            "Tránh dùng với NSAID (giảm hiệu quả, tăng nguy cơ suy thận)",
            "Ngừng ngay nếu có phù mạch (có thể nguy hiểm tính mạng)",
            "Ho khan có thể kéo dài, thường tự hết khi ngừng thuốc",
            "Thận trọng với kali bổ sung và kali-sparing diuretics"
        ],
        "pharmacokinetics": {
            "half_life": "17 giờ (perindoprilat - metabolite hoạt động)",
            "onset": "1-2 giờ",
            "duration": "24 giờ (cho phép dùng 1 lần/ngày)",
            "protein_binding": "20% (perindoprilat)",
            "clearance": "Thận (75% bài tiết qua nước tiểu)"
        },
        "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm, tránh ánh sáng",
        "black_box_warnings": "Chống chỉ định trong thai kỳ - có thể gây dị tật thai nhi và tử vong thai nhi. Phù mạch có thể đe dọa tính mạng.",
        "drug_interactions": {
            "major": [
                {
                    "drug": "Kali bổ sung, Kali-sparing diuretics (spironolactone, eplerenone, amiloride, triamterene)",
                    "mechanism": "Tác dụng hiệp đồng tăng kali máu",
                    "effect": "Tăng kali máu nghiêm trọng, có thể gây rối loạn nhịp tim",
                    "management": "Thận trọng. Theo dõi kali máu thường xuyên. Tránh dùng cùng nếu có thể."
                },
                {
                    "drug": "NSAIDs (ibuprofen, naproxen, diclofenac, etc.)",
                    "mechanism": "NSAIDs ức chế prostaglandin, làm giảm lưu lượng máu thận, giảm hiệu quả ACE inhibitor.",
                    "effect": "Giảm hiệu quả hạ huyết áp của perindopril, tăng nguy cơ suy thận cấp",
                    "management": "Tránh dùng đồng thời nếu có thể. Nếu bắt buộc, theo dõi chặt chẽ huyết áp, chức năng thận."
                }
            ],
            "moderate": [
                {
                    "drug": "Lithium",
                    "mechanism": "ACE inhibitors làm giảm thải trừ lithium qua thận, tăng nồng độ lithium.",
                    "effect": "Tăng nồng độ lithium, tăng độc tính",
                    "management": "Theo dõi nồng độ lithium thường xuyên. Giảm liều lithium khi bắt đầu perindopril."
                },
                {
                    "drug": "Diuretics (thiazide, loop diuretics)",
                    "mechanism": "Tác dụng hiệp đồng hạ huyết áp",
                    "effect": "Hạ huyết áp quá mức",
                    "management": "Giảm liều diuretic hoặc ngừng tạm thời khi bắt đầu perindopril."
                }
            ],
            "minor": []
        },
        "contraindications": {
            "tuyệt_đối": [
                "Dị ứng perindopril hoặc các ACE inhibitor khác",
                "Có thai (tất cả các tam cá nguyệt)",
                "Hẹp động mạch thận 2 bên",
                "Phù mạch trước đây với ACE inhibitor"
            ],
            "tương_đối": [
                "Suy thận nặng (CrCl <30) - cần giảm liều",
                "Suy gan - thận trọng",
                "Tăng kali máu",
                "Dùng với kali-sparing diuretics"
            ]
        },
        "pregnancy_lactation": {
            "fda_category": "D",
            "pregnancy_details": "Chống chỉ định trong thai kỳ - có thể gây dị tật thai nhi và tử vong thai nhi.",
            "lactation": {
                "safety": "Compatible",
                "details": "Perindopril bài tiết vào sữa mẹ ở nồng độ thấp. An toàn cho trẻ bú mẹ.",
                "recommendation": "Có thể dùng khi cho con bú."
            }
        },
        "hepatic_adjustment": {
            "mild": "Không cần điều chỉnh liều",
            "moderate": "Thận trọng, có thể cần giảm liều nhẹ",
            "severe": "Thận trọng, giảm liều hoặc tránh dùng",
            "notes": "Perindopril chuyển hóa một phần ở gan thành perindoprilat. Suy gan có thể giảm chuyển hóa nhưng không đáng kể."
        },
        "overdose_management": {
            "symptoms": [
                "Hạ huyết áp nghiêm trọng",
                "Chóng mặt, ngất",
                "Tăng kali máu",
                "Suy thận cấp"
            ],
            "antidote": "Không có antidote đặc hiệu. Điều trị hỗ trợ.",
            "treatment": [
                "Ngừng ngay perindopril",
                "Nằm đầu thấp, nâng chân",
                "Truyền dịch nếu hạ huyết áp",
                "Theo dõi huyết áp, nhịp tim, điện giải",
                "Điều trị tăng kali máu nếu có"
            ],
            "monitoring": "Huyết áp, nhịp tim, kali máu, chức năng thận trong ít nhất 24 giờ"
        },
        "reversal_agents": None,
        "administration_instructions": {
            "oral": {
                "with_food": "Có thể uống với hoặc không có thức ăn. Hấp thu tốt trong cả hai trường hợp.",
                "timing": "Uống 1 lần/ngày (do half-life dài). Có thể uống buổi sáng hoặc tối."
            },
            "iv": {
                "reconstitution": "N/A - Chỉ có dạng uống",
                "infusion_rate": "N/A",
                "compatibility": [],
                "incompatibility": [],
                "notes": "Perindopril chỉ có dạng uống. Nếu cần dạng IV, dùng enalaprilat."
            }
        },
        "references": {
            "primary_sources": [
                "FDA Drug Label - Aceon (perindopril)",
                "UpToDate - Perindopril: Drug information",
                "PROGRESS Study - The Lancet",
                "EUROPA Study - The Lancet",
                "American Heart Association/American College of Cardiology guidelines"
            ],
            "last_updated": "2025-02-05",
            "evidence_level": "High - PROGRESS and EUROPA studies (large RCTs) and extensive clinical experience"
        }
    }

}

__all__ = ['ACE_INHIBITORS']
