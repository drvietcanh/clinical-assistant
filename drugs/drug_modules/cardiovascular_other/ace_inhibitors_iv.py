"""
Cardiovascular ACE Inhibitors (IV)
Enalaprilat
"""

ACE_INHIBITORS_IV_DRUGS = {
    "Enalaprilat": {
        "group": "Cardiovascular - ACE Inhibitor (IV)",
        "vietnamese_name": "Enalaprilat, Enalapril IV",
        "administration": ["IV"],
        "indications": [
            "Tăng huyết áp cấp cứu",
            "Suy tim cấp",
            "Khi không uống được"
        ],
        "contraindications": [
            "Dị ứng ACE inhibitor",
            "Có thai",
            "Hẹp động mạch thận 2 bên"
        ],
        "dosage": {
            "adult_htn": "0.625-1.25mg IV mỗi 6 giờ",
            "adult_heart_failure": "0.625mg IV mỗi 6 giờ, tăng dần đến 1.25mg mỗi 6 giờ",
            "notes": "Khởi đầu với liều thấp, theo dõi huyết áp"
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "Giảm liều 25%",
            "under_30": "Thận trọng, giảm liều 50%"
        },
        "side_effects": [
            "Hạ huyết áp (phổ biến)",
            "Ho khan",
            "Tăng kali máu",
            "Phù mạch",
            "Suy thận cấp"
        ],
        "interactions": [
            "Kali: tăng kali máu",
            "Diuretics: tăng nguy cơ hạ huyết áp",
            "NSAID: giảm hiệu quả"
        ],
        "pregnancy": "D - Chống chỉ định",
        "mechanism_of_action": "Enalaprilat là dạng hoạt chất của enalapril (enalapril là prodrug, chuyển hóa thành enalaprilat trong gan). Enalaprilat ức chế angiotensin converting enzyme (ACE), enzyme chuyển angiotensin I thành angiotensin II. Angiotensin II là chất co mạch mạnh và kích thích tiết aldosterone. Bằng cách ức chế ACE, enalaprilat giảm nồng độ angiotensin II, dẫn đến: giãn mạch (giảm sức cản mạch máu ngoại biên), giảm aldosterone (giảm tái hấp thu natri và nước ở thận, tăng bài tiết kali), giảm tiền gánh và hậu gánh tim, và giảm huyết áp. Enalaprilat cũng ức chế phân hủy bradykinin (chất giãn mạch), có thể góp phần vào tác dụng hạ huyết áp nhưng cũng gây ho khan (tác dụng phụ). Dạng IV tác dụng nhanh hơn enalapril uống, phù hợp cho cấp cứu tăng huyết áp và suy tim cấp.",
        "monitoring": [
            "Huyết áp liên tục (đặc biệt trong 30-60 phút đầu sau liều đầu tiên) - nguy cơ hạ huyết áp đột ngột",
            "Kali máu (tăng kali máu do giảm aldosterone) - theo dõi định kỳ",
            "Creatinine và eGFR (suy thận cấp có thể xảy ra, đặc biệt ở bệnh nhân hẹp động mạch thận)",
            "Dấu hiệu phù mạch (angioedema): sưng mặt, môi, lưỡi, họng - cấp cứu, cần ngừng ngay",
            "Dấu hiệu ho khan (tác dụng phụ phổ biến, có thể dai dẳng)",
            "Nhịp tim và ECG (đặc biệt nếu có tiền sử rối loạn nhịp)",
            "Dấu hiệu suy tim: khó thở, phù, tăng cân"
        ],
        "precautions": [
            "Khởi đầu với liều thấp (0.625mg) và theo dõi huyết áp sát trong 30-60 phút đầu",
            "Nguy cơ hạ huyết áp đột ngột cao hơn so với enalapril uống (tác dụng nhanh hơn)",
            "Thận trọng ở bệnh nhân đang dùng diuretics (tăng nguy cơ hạ huyết áp) - có thể tạm ngừng diuretic trước khi bắt đầu",
            "Thận trọng ở bệnh nhân hẹp động mạch thận (có thể gây suy thận cấp)",
            "Thận trọng ở bệnh nhân suy thận (giảm liều, theo dõi creatinine)",
            "Thận trọng ở bệnh nhân đang dùng kali hoặc kali-sparing diuretics (tăng nguy cơ tăng kali máu)",
            "Tránh dùng với NSAID (giảm hiệu quả, tăng nguy cơ suy thận)",
            "Theo dõi phù mạch (angioedema) - có thể xảy ra ngay sau liều đầu tiên hoặc sau vài giờ",
            "Chuyển sang enalapril uống khi bệnh nhân có thể uống được",
            "Không dùng trong thai kỳ (chống chỉ định tuyệt đối - gây dị tật thai nhi)",
            "Thận trọng ở bệnh nhân có tiền sử phù mạch với ACE inhibitor khác"
        ],
        "pharmacokinetics": {
            "half_life": "11 giờ (enalaprilat, dài hơn enalapril)",
            "onset": "15 phút (IV, nhanh hơn enalapril uống)",
            "duration": "6 giờ (tiêm mỗi 6 giờ)",
            "protein_binding": "50-60%",
            "clearance": "Thận: bài tiết chủ yếu qua nước tiểu (không cần chuyển hóa như enalapril). Thời gian bán thải dài (11 giờ) so với enalapril (1 giờ) vì enalaprilat là chất chuyển hóa cuối cùng."
        },
        "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ánh sáng. Sau khi pha: dùng ngay, không bảo quản lâu. Theo hướng dẫn của nhà sản xuất về thời gian sử dụng sau khi pha.",
        "black_box_warnings": "Chống chỉ định trong thai kỳ - có thể gây tổn thương thai nhi và tử vong khi dùng trong tam cá nguyệt thứ hai và thứ ba. Phù mạch (angioedema) có thể xảy ra bất cứ lúc nào, có thể đe dọa tính mạng, cần ngừng ngay và điều trị cấp cứu.",
        "drug_interactions": {
            "major": [
                {
                    "drug": "Kali bổ sung, Kali-sparing diuretics (spironolactone, eplerenone, amiloride, triamterene)",
                    "mechanism": "Tác dụng hiệp đồng tăng kali máu.",
                    "effect": "Tăng kali máu nghiêm trọng, có thể gây rối loạn nhịp tim",
                    "management": "Thận trọng. Theo dõi kali máu thường xuyên. Tránh dùng cùng nếu có thể."
                },
                {
                    "drug": "NSAIDs (ibuprofen, naproxen, diclofenac)",
                    "mechanism": "Giảm tác dụng giãn mạch, giảm lưu lượng máu thận.",
                    "effect": "Giảm hiệu quả hạ huyết áp, tăng nguy cơ suy thận cấp",
                    "management": "Thận trọng. Theo dõi chức năng thận, huyết áp. Tránh dùng lâu dài cùng."
                }
            ],
            "moderate": [
                {
                    "drug": "Diuretics (furosemide, hydrochlorothiazide)",
                    "mechanism": "Tác dụng hiệp đồng hạ huyết áp.",
                    "effect": "Tăng nguy cơ hạ huyết áp quá mức",
                    "management": "Thận trọng khi bắt đầu. Có thể cần giảm liều diuretic hoặc tạm ngừng trước khi bắt đầu enalaprilat."
                },
                {
                    "drug": "Lithium",
                    "mechanism": "ACE inhibitor giảm thải trừ lithium qua thận.",
                    "effect": "Tăng nồng độ lithium, tăng nguy cơ độc tính",
                    "management": "Theo dõi nồng độ lithium. Giảm liều lithium nếu cần."
                }
            ],
            "minor": []
        },
        "contraindications": {
            "tuyệt_đối": [
                "Có thai - CHỐNG CHỈ ĐỊNH TUYỆT ĐỐI (gây dị tật thai nhi, tử vong thai nhi)",
                "Hẹp động mạch thận 2 bên - có thể gây suy thận cấp",
                "Phù mạch (angioedema) trước đây với ACE inhibitor",
                "Dị ứng enalaprilat hoặc ACE inhibitor"
            ],
            "tương_đối": [
                "Hẹp động mạch thận 1 bên - thận trọng, theo dõi chức năng thận",
                "Suy thận nặng - giảm liều, theo dõi creatinine",
                "Đang dùng diuretics - tăng nguy cơ hạ huyết áp",
                "Đang dùng kali hoặc kali-sparing diuretics - tăng nguy cơ tăng kali máu"
            ]
        },
        "pregnancy_lactation": {
            "fda_category": "D",
            "pregnancy_details": "Enalaprilat là category D - CHỐNG CHỈ ĐỊNH TUYỆT ĐỐI trong thai kỳ. Có thể gây tổn thương thai nhi và tử vong khi dùng trong tam cá nguyệt thứ hai và thứ ba. Có thể gây dị tật thai nhi (hội chứng ACE inhibitor: thiểu ối, suy thận, hạ huyết áp, thiểu sản phổi, gãy xương sọ, tử vong). Ngừng ngay nếu phát hiện có thai.",
            "lactation": {
                "safety": "Unknown",
                "details": "Không biết enalaprilat có bài tiết vào sữa mẹ hay không. Thận trọng khi dùng khi cho con bú.",
                "recommendation": "Thận trọng khi dùng khi cho con bú. Cân nhắc ngừng cho con bú hoặc ngừng thuốc."
            }
        },
        "hepatic_adjustment": {
            "mild": "Không cần điều chỉnh liều. Enalaprilat không cần chuyển hóa ở gan (là dạng hoạt động).",
            "moderate": "Không cần điều chỉnh liều. Enalaprilat không cần chuyển hóa ở gan.",
            "severe": "Không cần điều chỉnh liều. Enalaprilat không cần chuyển hóa ở gan.",
            "notes": "Enalaprilat là dạng hoạt động, không cần chuyển hóa ở gan (khác với enalapril uống là prodrug). Suy gan không ảnh hưởng đến nồng độ enalaprilat."
        },
        "overdose_management": {
            "symptoms": [
                "Hạ huyết áp nghiêm trọng, sốc",
                "Tăng kali máu nặng (rối loạn nhịp tim)",
                "Suy thận cấp",
                "Phù mạch (angioedema) - sưng mặt, môi, lưỡi, họng",
                "Ho khan nặng"
            ],
            "antidote": "Không có antidote đặc hiệu. Điều trị hỗ trợ.",
            "treatment": [
                "Ngừng enalaprilat ngay lập tức",
                "Nếu hạ huyết áp: đặt bệnh nhân nằm ngửa, nâng chân cao, truyền dịch (normal saline), thuốc vận mạch nếu cần (norepinephrine)",
                "Nếu tăng kali máu: điều chỉnh kali (calcium gluconate, insulin+glucose, sodium bicarbonate, kayexalate)",
                "Nếu phù mạch: epinephrine, corticosteroids, antihistamines, hỗ trợ hô hấp nếu cần",
                "Nếu suy thận cấp: điều trị hỗ trợ, có thể cần lọc máu",
                "Theo dõi huyết áp, nhịp tim, kali máu, creatinine liên tục"
            ],
            "monitoring": "Huyết áp, nhịp tim, kali máu, creatinine, dấu hiệu phù mạch, dấu hiệu sinh tồn"
        },
        "reversal_agents": {
            "available": False,
            "agents": []
        },
        "administration_instructions": {
            "oral": {
                "with_food": "N/A - chỉ có dạng IV",
                "timing": "N/A - chỉ có dạng IV"
            },
            "iv": {
                "reconstitution": "Pha với normal saline hoặc D5W. Dùng ngay sau khi pha.",
                "infusion_rate": "Tiêm tĩnh mạch chậm trong 5 phút. Không truyền nhanh.",
                "compatibility": ["Normal saline", "D5W"],
                "incompatibility": ["Không trộn với các thuốc khác"],
                "notes": "Tiêm tĩnh mạch chậm trong 5 phút. Theo dõi huyết áp sát trong 30-60 phút đầu. Chuyển sang enalapril uống khi bệnh nhân có thể uống được."
            }
        },
        "references": {
            "primary_sources": [
                "FDA Drug Label - Enalaprilat (Vasotec IV)",
                "UpToDate - Enalaprilat: Drug Information",
                "Goodman & Gilman's The Pharmacological Basis of Therapeutics (14th ed)"
            ],
            "last_updated": "2025-02-04",
            "evidence_level": "A - Dựa trên FDA drug labels và dữ liệu lâm sàng"
        }
    }
}

__all__ = ['ACE_INHIBITORS_IV_DRUGS']

