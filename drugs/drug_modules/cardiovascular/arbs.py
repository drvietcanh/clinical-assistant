"""
ARBs - Angiotensin Receptor Blockers
"""

ARBS = {
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
            "tuyệt_đối": [
                "Dị ứng ARB",
                "Có thai",
                "Hẹp động mạch thận 2 bên",
                "Phù mạch trước đây với ARB"
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
        "pediatric_dosing": {
            "neonates": "Không khuyến cáo cho trẻ <6 tuổi (dữ liệu hạn chế)",
            "infants": "Không khuyến cáo cho trẻ <6 tuổi (dữ liệu hạn chế)",
            "children": "6-16 tuổi: 0.7mg/kg/ngày x 1 lần (tối đa 50mg/ngày). Chỉ dùng cho tăng huyết áp. Theo dõi huyết áp, chức năng thận, kali máu",
            "adolescents": "25-50mg x 1 lần/ngày, tăng dần đến 50-100mg/ngày nếu cần. Liều người lớn",
            "notes": "Dữ liệu hạn chế ở trẻ em. Chỉ dùng cho tăng huyết áp ở trẻ ≥6 tuổi. Khởi đầu với liều thấp, tăng dần. Theo dõi huyết áp, chức năng thận, kali máu"
        },
        "geriatric_dosing": {
            "considerations": "Người cao tuổi nhạy cảm hơn với tác dụng hạ huyết áp. Suy thận phổ biến hơn",
            "dose_adjustment": "Khởi đầu với liều thấp hơn (25mg x 1 lần/ngày). Tăng dần chậm hơn. Điều chỉnh theo CrCl",
            "monitoring": "Theo dõi huyết áp sát hơn (nguy cơ hạ huyết áp quá mức). Theo dõi chức năng thận, kali máu thường xuyên"
        },
        "brand_names": {
            "vietnam": ["Cozaar", "Losartan Stada", "Losartan", "Losar"],
            "common": ["Cozaar", "Losartan"]
        },
        "cost_estimate": {
            "unit": "VND",
            "range": "15,000 - 40,000 VND/viên (tùy hàm lượng và thương hiệu)",
            "note": "Giá thay đổi theo thương hiệu và nhà thuốc. Losartan generic thường rẻ hơn (15,000-25,000 VND/viên 50mg)."
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

}

__all__ = ['ARBS']
