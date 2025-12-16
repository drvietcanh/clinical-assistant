"""
Cholesterol Absorption Inhibitors
"""

CHOLESTEROL_ABSORPTION_INHIBITORS = {
    "Ezetimibe": {
        "group": "Cardiovascular - Cholesterol Absorption Inhibitor",
        "vietnamese_name": "Ezetimibe, Ezetrol, Zetia",
        "administration": ["PO"],
        "indications": [
            "Tăng cholesterol máu (đơn trị hoặc kết hợp với statin)",
            "Tăng cholesterol máu gia đình (familial hypercholesterolemia)",
            "Kết hợp với statin để tăng hiệu quả giảm LDL",
            "Bệnh nhân không dung nạp statin (dùng đơn trị)"
        ],
        "contraindications": [
            "Dị ứng ezetimibe",
            "Bệnh gan hoạt động (khi dùng với statin)",
            "Có thai (khi dùng với statin)"
        ],
        "dosage": {
            "adult_monotherapy": "10mg x 1 lần/ngày",
            "adult_with_statin": "10mg x 1 lần/ngày (kết hợp với statin)",
            "adult_with_fenofibrate": "10mg x 1 lần/ngày (kết hợp với fenofibrate)",
            "notes": "Uống bất kỳ lúc nào trong ngày, có thể uống với hoặc không thức ăn. Có thể dùng cùng lúc với statin hoặc cách xa."
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "Không đổi",
            "under_30": "Không đổi"
        },
        "side_effects": [
            "Rối loạn tiêu hóa (tiêu chảy, đau bụng) - nhẹ",
            "Đau khớp",
            "Mệt mỏi",
            "Tăng men gan (khi dùng với statin)",
            "Đau cơ (khi dùng với statin, ít hơn statin đơn trị)"
        ],
        "interactions": [
            "Cholestyramine: giảm hấp thu ezetimibe - dùng cách xa ít nhất 2 giờ",
            "Fibrates: tăng nguy cơ sỏi mật",
            "Cyclosporine: tăng nồng độ ezetimibe - giảm liều ezetimibe xuống 5mg/ngày"
        ],
        "pregnancy": "C",
        "mechanism_of_action": "Ezetimibe ức chế hấp thu cholesterol ở ruột non bằng cách ức chế protein NPC1L1 (Niemann-Pick C1-Like 1) ở bờ bàn chải của tế bào ruột. NPC1L1 chịu trách nhiệm vận chuyển cholesterol từ lòng ruột vào tế bào ruột. Bằng cách ức chế protein này, ezetimibe làm giảm hấp thu cholesterol từ thức ăn và từ mật (cholesterol được tái hấp thu), dẫn đến giảm cholesterol toàn phần và LDL cholesterol. Ezetimibe giảm LDL cholesterol khoảng 15-20% khi dùng đơn trị, và giảm thêm 15-20% khi kết hợp với statin (tác dụng cộng dồn). Ezetimibe không ảnh hưởng đến hấp thu triglyceride, vitamin tan trong dầu, hoặc acid mật. Thuốc tác dụng tại ruột, ít hấp thu vào máu (chuyển hóa thành ezetimibe-glucuronide ở ruột và gan).",
        "monitoring": [
            "Lipid profile (LDL, HDL, TG, total cholesterol) sau 4-8 tuần, sau đó mỗi 3-6 tháng",
            "Chức năng gan (ALT, AST) - trước và trong điều trị, đặc biệt khi dùng với statin",
            "Dấu hiệu tác dụng phụ tiêu hóa (tiêu chảy, đau bụng) - nhẹ",
            "Dấu hiệu sỏi mật (đau bụng phải trên) - khi dùng với fibrates",
            "CK nếu có đau cơ (khi dùng với statin)"
        ],
        "precautions": [
            "Uống bất kỳ lúc nào trong ngày, có thể uống với hoặc không thức ăn",
            "Có thể dùng cùng lúc với statin hoặc cách xa",
            "Giảm LDL cholesterol khoảng 15-20% khi dùng đơn trị",
            "Kết hợp với statin: giảm thêm 15-20% LDL (tác dụng cộng dồn)",
            "Ít tác dụng phụ hơn statin (đặc biệt đau cơ)",
            "Dùng cách xa cholestyramine ít nhất 2 giờ (giảm hấp thu ezetimibe)",
            "Thận trọng khi dùng với fibrates (tăng nguy cơ sỏi mật)",
            "Giảm liều xuống 5mg/ngày khi dùng với cyclosporine",
            "Theo dõi men gan khi dùng với statin (tăng nguy cơ tăng men gan)"
        ],
        "pharmacokinetics": {
            "half_life": "22 giờ (ezetimibe), 24 giờ (ezetimibe-glucuronide)",
            "onset": "2 tuần",
            "duration": "24 giờ (dùng 1 lần/ngày)",
            "protein_binding": ">90%",
            "metabolism": "Chuyển hóa ở ruột và gan thành ezetimibe-glucuronide (hoạt chất)",
            "clearance": "Chủ yếu qua phân (78%), một phần qua thận (11%)"
        },
        "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm, tránh ánh sáng",
        "black_box_warnings": None,
        "drug_interactions": {
            "major": [
                {
                    "drug": "Cholestyramine, Colestipol, Colesevelam",
                    "mechanism": "Cholestyramine giảm hấp thu ezetimibe",
                    "effect": "Giảm nồng độ ezetimibe, giảm hiệu quả",
                    "management": "Dùng cách xa ít nhất 2 giờ. Dùng ezetimibe trước hoặc sau cholestyramine ít nhất 2 giờ."
                }
            ],
            "moderate": [
                {
                    "drug": "Cyclosporine",
                    "mechanism": "Cyclosporine tăng nồng độ ezetimibe",
                    "effect": "Tăng nồng độ ezetimibe, tăng nguy cơ tác dụng phụ",
                    "management": "Giảm liều ezetimibe xuống 5mg/ngày khi dùng với cyclosporine. Theo dõi lipid profile và tác dụng phụ."
                },
                {
                    "drug": "Fibrates (Fenofibrate, Gemfibrozil)",
                    "mechanism": "Cả hai đều ảnh hưởng đến chuyển hóa cholesterol và mật",
                    "effect": "Tăng nguy cơ sỏi mật",
                    "management": "Thận trọng. Theo dõi dấu hiệu sỏi mật (đau bụng phải trên). Có thể dùng với fenofibrate (đã được nghiên cứu), nhưng thận trọng với gemfibrozil."
                }
            ],
            "minor": []
        },
        "contraindications": {
            "tuyệt_đối": [
                "Dị ứng ezetimibe"
            ],
            "tương_đối": [
                "Bệnh gan hoạt động (khi dùng với statin) - chống chỉ định statin, nhưng có thể dùng ezetimibe đơn trị",
                "Có thai (khi dùng với statin) - statin chống chỉ định trong thai kỳ",
                "Dùng với cyclosporine - giảm liều ezetimibe xuống 5mg/ngày",
                "Dùng với fibrates - tăng nguy cơ sỏi mật"
            ]
        },
        "pregnancy_lactation": {
            "fda_category": "C",
            "pregnancy_details": "Ezetimibe phân loại C - thận trọng trong thai kỳ. Các nghiên cứu trên động vật cho thấy một số nguy cơ. Không có nghiên cứu đầy đủ trên phụ nữ có thai. Cân nhắc lợi ích/nguy cơ. Nếu dùng với statin: statin chống chỉ định trong thai kỳ (category X).",
            "lactation": {
                "safety": "Compatible",
                "details": "Ezetimibe và ezetimibe-glucuronide bài tiết vào sữa mẹ ở nồng độ thấp. Nồng độ trong máu trẻ bú mẹ thường rất thấp. Không có báo cáo về tác dụng phụ nghiêm trọng ở trẻ bú mẹ.",
                "recommendation": "Có thể dùng khi cho con bú. Theo dõi trẻ nếu có dấu hiệu bất thường."
            }
        },
        "hepatic_adjustment": {
            "mild": "Không đổi",
            "moderate": "Không đổi",
            "severe": "Thận trọng (khi dùng với statin - statin chống chỉ định ở bệnh gan hoạt động)",
            "notes": "Ezetimibe chuyển hóa ở ruột và gan. Suy gan có thể ảnh hưởng nhẹ đến chuyển hóa, nhưng thường không cần điều chỉnh liều. Khi dùng với statin: statin chống chỉ định ở bệnh gan hoạt động."
        },
        "overdose_management": {
            "symptoms": [
                "Rối loạn tiêu hóa (tiêu chảy, đau bụng)",
                "Mệt mỏi",
                "Đau khớp"
            ],
            "antidote": "Không có antidote đặc hiệu. Điều trị hỗ trợ.",
            "treatment": [
                "Ngừng ezetimibe nếu cần",
                "Rửa dạ dày nếu mới uống <1 giờ",
                "Than hoạt tính",
                "Supportive care",
                "Theo dõi triệu chứng"
            ],
            "monitoring": "Triệu chứng lâm sàng, lipid profile"
        },
        "reversal_agents": {
            "available": False,
            "agents": []
        },
        "administration_instructions": {
            "oral": {
                "with_food": "Có thể uống với hoặc không có thức ăn. Không ảnh hưởng đáng kể đến hấp thu.",
                "timing": "Uống 1 lần/ngày, bất kỳ lúc nào trong ngày. Có thể dùng cùng lúc với statin hoặc cách xa. Dùng cách xa cholestyramine ít nhất 2 giờ."
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
                "FDA Drug Label - Ezetimibe (Zetia)",
                "UpToDate - Ezetimibe: Drug information",
                "IMPROVE-IT Study - New England Journal of Medicine (2015) - Ezetimibe + Simvastatin trong ACS",
                "SHARP Study - The Lancet (2011) - Ezetimibe + Simvastatin trong CKD",
                "ACC/AHA Guidelines - Cholesterol Management (2018)"
            ],
            "last_updated": "2025-02-05",
            "evidence_level": "High - Multiple large RCTs (IMPROVE-IT, SHARP) showing cardiovascular benefit when combined with statin"
        }
    }
}

__all__ = ['CHOLESTEROL_ABSORPTION_INHIBITORS']


















