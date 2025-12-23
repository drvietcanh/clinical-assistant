"""
Cerebral Circulation and Neurometabolic Drugs
Thuốc tuần hoàn não / tăng chuyển hóa thần kinh
Piracetam, Citicoline, Vinpocetine, Ginkgo biloba
"""

CEREBRAL_CIRCULATION_DRUGS = {
    "Piracetam": {
        "group": "Neurology - Nootropic / Cerebral circulation enhancer",
        "vietnamese_name": "Piracetam",
        "administration": ["PO", "IV"],
        "indications": [
            "Thiếu máu não mạn tính, chóng mặt, suy giảm trí nhớ nhẹ",
            "Hỗ trợ phục hồi sau đột quỵ (bằng chứng hạn chế)",
            "Một số rối loạn nhận thức ở người cao tuổi (off-label)",
        ],
        "contraindications": [
            "Suy thận nặng (CrCl <20 ml/phút)",
            "Xuất huyết não đang hoạt động",
            "Mẫn cảm với piracetam hoặc dẫn xuất pyrrolidone",
        ],
        "dosage": {
            "adult_po": "2.4-4.8g/ngày chia 2-3 lần",
            "adult_iv": "2-4g IV/ngày chia 1-2 lần",
            "notes": "Điều chỉnh liều theo chức năng thận; không dùng kéo dài nếu không có lợi rõ ràng.",
        },
        "renal_adjustment": {
            "normal": "Không cần chỉnh liều",
            "30_60": "Giảm 1/2 liều",
            "under_30": "Tránh hoặc giảm 2/3 liều",
        },
        "side_effects": [
            "Kích thích nhẹ, mất ngủ",
            "Buồn nôn, nôn",
            "Nhức đầu",
            "Rối loạn tiêu hóa",
        ],
        "interactions": [
            "Thuốc chống đông/kháng tiểu cầu: lý thuyết tăng nguy cơ chảy máu",
        ],
        "pregnancy": "C - tránh dùng nếu không thực sự cần",
        "mechanism_of_action": "Piracetam là dẫn xuất pyrrolidone, được cho là cải thiện tính linh động của màng tế bào thần kinh, tăng dẫn truyền thần kinh (đặc biệt acetylcholinergic và glutamatergic) và cải thiện vi tuần hoàn não thông qua giảm kết tụ hồng cầu và tăng biến dạng hồng cầu.",
        "monitoring": [
            "Đánh giá lâm sàng (chóng mặt, trí nhớ, tập trung)",
            "Chức năng thận ở người cao tuổi",
        ],
        "precautions": [
            "Hiệu quả trên nhận thức còn gây tranh cãi, tránh dùng kéo dài không cần thiết",
            "Điều chỉnh liều ở suy thận",
            "Thận trọng ở bệnh nhân có nguy cơ chảy máu",
        ],
        "pharmacokinetics": {
            "half_life": "4-5 giờ (kéo dài ở suy thận)",
            "onset": "Vài ngày đến vài tuần",
            "duration": "24 giờ",
            "protein_binding": "<10%",
            "clearance": "Thải trừ thận gần như hoàn toàn ở dạng không đổi",
        },
        "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm.",
        "black_box_warnings": None,
        "drug_interactions": {
            "major": [],
            "moderate": [],
            "minor": [],
        },
        "contraindications_detail": {
            "tuyệt_đối": ["Suy thận nặng", "Xuất huyết não đang hoạt động"],
            "tương_đối": ["Rối loạn đông máu", "Đang dùng chống đông/kháng tiểu cầu liều cao"],
        },
        "pregnancy_lactation": {
            "fda_category": "C",
            "pregnancy_details": "Dữ liệu hạn chế, tránh dùng trừ khi thực sự cần.",
            "lactation": {
                "safety": "Caution",
                "details": "Chưa rõ bài tiết vào sữa; thận trọng khi cho con bú.",
                "recommendation": "Tránh nếu có thể; nếu dùng cần theo dõi trẻ.",
            },
        },
        "hepatic_adjustment": {
            "mild": "Không cần chỉnh",
            "moderate": "Không cần chỉnh",
            "severe": "Không cần chỉnh (thải trừ chủ yếu qua thận)",
            "notes": "Chủ yếu thải trừ thận, suy gan ít ảnh hưởng.",
        },
        "overdose_management": {
            "symptoms": ["Kích thích, mất ngủ, rối loạn tiêu hóa"],
            "antidote": "Không có antidote đặc hiệu",
            "treatment": [
                "Điều trị triệu chứng",
                "Lọc máu có thể loại bỏ một phần piracetam (do thải trừ qua thận)",
            ],
            "monitoring": "Triệu chứng lâm sàng, chức năng thận.",
        },
        "reversal_agents": None,
        "administration_instructions": {
            "oral": {
                "with_food": "Có thể uống cùng hoặc không cùng thức ăn",
                "timing": "Chia 2-3 lần/ngày, tránh uống muộn buổi tối (nguy cơ mất ngủ).",
            }
        },
        "references": {
            "primary_sources": [
                "Cochrane reviews on piracetam for cognitive impairment (kết quả không nhất quán)",
                "Drug monographs (Micromedex, UpToDate)",
            ],
            "last_updated": "2025-02-18",
            "evidence_level": "Low–Moderate (bằng chứng hạn chế, không phải chuẩn điều trị chính)",
        },
    },

    "Citicoline": {
        "group": "Neurology - Neuroprotective / Nootropic",
        "vietnamese_name": "Citicoline, CDP-choline",
        "administration": ["PO", "IV"],
        "indications": [
            "Hỗ trợ phục hồi sau đột quỵ thiếu máu não (bằng chứng mức trung bình)",
            "Rối loạn nhận thức nhẹ ở người cao tuổi (off-label)",
            "Chấn thương sọ não (TBI) – hỗ trợ"
        ],
        "contraindications": [
            "Dị ứng với citicoline hoặc thành phần thuốc",
        ],
        "dosage": {
            "adult_po": "500-1000mg x 1-2 lần/ngày",
            "adult_iv": "500-1000mg IV x 1-2 lần/ngày",
            "notes": "Có thể dùng đường uống hoặc IV; nhiều guideline xem là thuốc hỗ trợ, không thay thế điều trị chuẩn (tái tưới máu, chống đông, statin…)."
        },
        "renal_adjustment": {
            "normal": "Không cần chỉnh liều",
            "30_60": "Không cần chỉnh liều",
            "under_30": "Thận trọng, dữ liệu hạn chế"
        },
        "side_effects": [
            "Đau đầu",
            "Mất ngủ nhẹ",
            "Buồn nôn",
            "Hạ huyết áp nhẹ (hiếm)",
        ],
        "interactions": [
            "Ít tương tác đáng kể; thận trọng khi phối hợp với các nootropic khác (kích thích nhẹ)."
        ],
        "pregnancy": "C - dữ liệu hạn chế, tránh dùng nếu không thực sự cần",
        "mechanism_of_action": (
            "Citicoline (CDP-choline) là tiền chất tổng hợp phosphatidylcholine của màng tế bào thần kinh, "
            "có thể ổn định màng, giảm chết tế bào do thiếu máu, tăng tổng hợp acetylcholine và cải thiện dẫn truyền thần kinh. "
            "Cơ chế được xem là bảo vệ tế bào thần kinh trong thiếu máu não và TBI."
        ),
        "monitoring": [
            "Đánh giá lâm sàng (tri giác, chức năng thần kinh, nhận thức)",
            "Huyết áp ở bệnh nhân có bệnh mạch máu não",
        ],
        "precautions": [
            "Chỉ là thuốc hỗ trợ; không trì hoãn điều trị chuẩn đột quỵ (tái tưới máu, chống đông, kiểm soát HA…).",
            "Thận trọng ở bệnh nhân có rối loạn giấc ngủ (có thể gây mất ngủ nhẹ).",
        ],
        "pharmacokinetics": {
            "half_life": "tổng hợp 50-70 giờ (dựa trên chuyển hóa thành choline và cytidine)",
            "onset": "vài ngày",
            "duration": "tích lũy dần trong mô thần kinh",
            "protein_binding": "N/A (tiền chất nucleotide)",
            "clearance": "Chuyển hóa thành choline và cytidine; thải qua CO2, nước tiểu."
        },
        "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm, tránh ánh sáng.",
        "black_box_warnings": None,
        "drug_interactions": {
            "major": [],
            "moderate": [],
            "minor": [],
        },
        "contraindications_detail": {
            "tuyệt_đối": ["Dị ứng citicoline"],
            "tương_đối": ["Rối loạn giấc ngủ, kích thích thần kinh trung ương"]
        },
        "pregnancy_lactation": {
            "fda_category": "C",
            "pregnancy_details": "Chưa có dữ liệu RCT lớn; tránh dùng thường quy trong thai kỳ.",
            "lactation": {
                "safety": "Caution",
                "details": "Chưa rõ bài tiết vào sữa mẹ.",
                "recommendation": "Tránh nếu có thể.",
            },
        },
        "hepatic_adjustment": {
            "mild": "Không cần chỉnh",
            "moderate": "Thận trọng",
            "severe": "Thận trọng, dữ liệu hạn chế",
            "notes": "Chuyển hóa qua gan nhưng ít độc gan được báo cáo."
        },
        "overdose_management": {
            "symptoms": ["Đau đầu, kích thích, mất ngủ, rối loạn tiêu hóa"],
            "antidote": "Không có antidote đặc hiệu",
            "treatment": ["Điều trị triệu chứng"],
            "monitoring": "Triệu chứng lâm sàng."
        },
        "reversal_agents": None,
        "administration_instructions": {
            "oral": {
                "with_food": "Có thể uống với hoặc không thức ăn",
                "timing": "1-2 lần/ngày, tránh dùng tối nếu gây mất ngủ."
            }
        },
        "references": {
            "primary_sources": [
                "Stroke and TBI trials with citicoline (bằng chứng không đồng nhất)",
                "ESO/ASA stroke guidelines (citicoline không phải điều trị chuẩn)",
            ],
            "last_updated": "2025-02-18",
            "evidence_level": "Low–Moderate (thuốc hỗ trợ, không thay thế điều trị chuẩn)"
        },
    },

    "Vinpocetine": {
        "group": "Neurology - Cerebral vasodilator (controversial evidence)",
        "vietnamese_name": "Vinpocetine",
        "administration": ["PO", "IV"],
        "indications": [
            "Thiếu máu não mạn, chóng mặt, ù tai (dùng phổ biến tại VN, bằng chứng hạn chế)",
        ],
        "contraindications": [
            "Xuất huyết não cấp",
            "Thai kỳ (một số dữ liệu tiền lâm sàng gợi ý độc tính trên thai)",
        ],
        "dosage": {
            "adult_po": "5-10mg x 3 lần/ngày",
            "adult_iv": "20mg IV/ngày (pha truyền chậm)",
            "notes": "Không dùng đường IV bolus nhanh. Thường chỉ dùng ngắn hạn."
        },
        "renal_adjustment": {
            "normal": "Không cần chỉnh",
            "30_60": "Không cần chỉnh",
            "under_30": "Thận trọng, dữ liệu hạn chế"
        },
        "side_effects": [
            "Đỏ mặt, nóng bừng",
            "Đánh trống ngực, hạ huyết áp nhẹ",
            "Nhức đầu",
            "Rối loạn tiêu hóa",
        ],
        "interactions": [
            "Thuốc chống đông/kháng tiểu cầu: lý thuyết tăng nguy cơ chảy máu",
        ],
        "pregnancy": "X (tránh dùng trong thai kỳ)",
        "mechanism_of_action": (
            "Vinpocetine là dẫn xuất bán tổng hợp của vincamine, được cho là gây giãn mạch chọn lọc tại tuần hoàn não, "
            "ức chế kênh Ca2+ và tăng sử dụng glucose/oxygen tại mô não thiếu máu. Bằng chứng lâm sàng về cải thiện "
            "kết cục đột quỵ hoặc sa sút trí tuệ còn yếu và không được khuyến cáo trong guideline phương Tây."
        ),
        "monitoring": [
            "Huyết áp, nhịp tim (nguy cơ hạ HA, đánh trống ngực)",
            "Triệu chứng thần kinh chủ quan (chóng mặt, đau đầu)"
        ],
        "precautions": [
            "Không thay thế điều trị chuẩn cho đột quỵ hoặc bệnh mạch máu não.",
            "Thận trọng ở bệnh nhân tụt huyết áp hoặc rối loạn nhịp tim.",
            "Tránh dùng trong thai kỳ và cho con bú."
        ],
        "pharmacokinetics": {
            "half_life": "4-5 giờ",
            "onset": "vài giờ",
            "duration": "8-12 giờ",
            "protein_binding": "~66%",
            "clearance": "Gan chuyển hóa, thải qua thận."
        },
        "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm, tránh ánh sáng.",
        "black_box_warnings": None,
        "drug_interactions": {
            "major": [],
            "moderate": [
                {
                    "drug": "Warfarin, DOACs, Aspirin, Clopidogrel",
                    "mechanism": "Tác dụng giãn mạch/giảm độ nhớt máu có thể cộng hưởng với chống đông/kháng tiểu cầu",
                    "effect": "Lý thuyết tăng nguy cơ chảy máu",
                    "management": "Thận trọng; theo dõi chảy máu."
                }
            ],
            "minor": [],
        },
        "contraindications_detail": {
            "tuyệt_đối": ["Xuất huyết não cấp", "Thai kỳ"],
            "tương_đối": ["Huyết áp thấp", "Rối loạn nhịp tim", "Đang dùng chống đông/kháng tiểu cầu"]
        },
        "pregnancy_lactation": {
            "fda_category": "X (tránh dùng)",
            "pregnancy_details": "Một số dữ liệu tiền lâm sàng gợi ý độc tính phôi thai; không dùng cho phụ nữ mang thai hoặc có khả năng mang thai.",
            "lactation": {
                "safety": "Incompatible",
                "details": "Chưa rõ bài tiết vào sữa; tránh dùng khi cho con bú.",
                "recommendation": "Không dùng trong thời kỳ cho con bú."
            },
        },
        "hepatic_adjustment": {
            "mild": "Không cần chỉnh",
            "moderate": "Thận trọng (chuyển hóa qua gan)",
            "severe": "Tránh dùng do thiếu dữ liệu",
            "notes": "Suy gan có thể tăng nồng độ vinpocetine."
        },
        "overdose_management": {
            "symptoms": ["Hạ huyết áp, đánh trống ngực, nhức đầu"],
            "antidote": "Không có antidote đặc hiệu",
            "treatment": ["Điều trị hỗ trợ, bù dịch, theo dõi huyết áp, nhịp tim"],
            "monitoring": "Huyết áp, nhịp tim, ECG nếu cần."
        },
        "reversal_agents": None,
        "administration_instructions": {
            "oral": {
                "with_food": "Có thể uống với hoặc không thức ăn",
                "timing": "Chia 2-3 lần/ngày."
            }
        },
        "references": {
            "primary_sources": [
                "Một số RCT nhỏ về vinpocetine trong thiếu máu não mạn (kết quả không nhất quán)",
                "Không được khuyến cáo trong guideline AHA/ASA như điều trị chuẩn",
            ],
            "last_updated": "2025-02-18",
            "evidence_level": "Low (bằng chứng yếu, chủ yếu dùng theo thói quen lâm sàng tại một số nước)"
        },
    },

    "Ginkgo biloba extract": {
        "group": "Neurology - Herbal cerebral vasomodulator (Ginkgo biloba)",
        "vietnamese_name": "Chiết xuất Ginkgo biloba",
        "administration": ["PO"],
        "indications": [
            "Rối loạn tuần hoàn não, suy giảm trí nhớ nhẹ (bằng chứng hạn chế)",
            "Chóng mặt, ù tai do nguyên nhân mạch máu (off-label)"
        ],
        "contraindications": [
            "Dị ứng Ginkgo biloba",
            "Đang dùng chống đông/kháng tiểu cầu liều cao (nguy cơ chảy máu)",
            "Tiền sử động kinh (một số chế phẩm có thể gây co giật)"
        ],
        "dosage": {
            "adult_po": "120-240mg/ngày chia 2-3 lần (chiết xuất chuẩn hóa EGb 761 24%)",
            "notes": "Nên dùng dạng chiết xuất chuẩn hóa; tránh dùng hạt hoặc chế phẩm không chuẩn."
        },
        "renal_adjustment": {
            "normal": "Không cần chỉnh",
            "30_60": "Không cần chỉnh",
            "under_30": "Thận trọng, dữ liệu hạn chế"
        },
        "side_effects": [
            "Rối loạn tiêu hóa nhẹ",
            "Đau đầu",
            "Phát ban da",
            "Chảy máu (hiếm, thường khi phối hợp chống đông/kháng tiểu cầu)"
        ],
        "interactions": [
            "Warfarin, DOACs, Aspirin, Clopidogrel: tăng nguy cơ chảy máu",
            "NSAIDs: tăng nguy cơ chảy máu tiêu hóa"
        ],
        "pregnancy": "C/X (tránh gần ngày sinh do nguy cơ chảy máu)",
        "mechanism_of_action": (
            "Chiết xuất Ginkgo biloba (EGb 761) chứa flavonoid và terpenoid có tác dụng "
            "chống oxy hóa, điều hòa trương lực mạch (bao gồm mạch não), "
            "điều biến dẫn truyền thần kinh và giảm kết tập tiểu cầu nhẹ (ức chế PAF). "
            "Bằng chứng về cải thiện nhận thức và phòng ngừa sa sút trí tuệ còn hạn chế và không đồng nhất."
        ),
        "monitoring": [
            "Dấu hiệu chảy máu (chấm xuất huyết, bầm tím, chảy máu cam…) đặc biệt nếu dùng kèm chống đông/kháng tiểu cầu.",
            "Đánh giá triệu chứng chủ quan (chóng mặt, trí nhớ)."
        ],
        "precautions": [
            "Không dùng thay thế thuốc chuẩn cho đột quỵ hoặc sa sút trí tuệ.",
            "Ngừng trước phẫu thuật ít nhất 5-7 ngày (giảm nguy cơ chảy máu).",
            "Tránh dùng cùng nhiều thuốc chống đông/kháng tiểu cầu.",
        ],
        "pharmacokinetics": {
            "half_life": "khoảng 4-10 giờ (tùy thành phần flavonoid/terpenoid)",
            "onset": "vài tuần",
            "duration": "tích lũy dần; đánh giá sau 4-12 tuần",
            "protein_binding": "khác nhau giữa các thành phần",
            "clearance": "Chuyển hóa gan, thải qua thận và mật."
        },
        "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm, tránh ánh sáng.",
        "black_box_warnings": None,
        "drug_interactions": {
            "major": [
                {
                    "drug": "Warfarin, DOACs, Heparin",
                    "mechanism": "Ức chế kết tập tiểu cầu nhẹ (PAF) cộng hưởng với chống đông",
                    "effect": "Tăng nguy cơ chảy máu nghiêm trọng",
                    "management": "Thường nên tránh phối hợp; nếu bắt buộc, theo dõi sát dấu hiệu chảy máu và INR (nếu dùng warfarin)."
                }
            ],
            "moderate": [
                {
                    "drug": "Aspirin, Clopidogrel, NSAIDs",
                    "mechanism": "Tác dụng chống kết tập tiểu cầu nhẹ + NSAIDs gây loét",
                    "effect": "Tăng nguy cơ chảy máu tiêu hóa",
                    "management": "Thận trọng; cân nhắc PPI bảo vệ dạ dày; tránh phối hợp nếu không cần thiết."
                }
            ],
            "minor": [],
        },
        "contraindications_detail": {
            "tuyệt_đối": ["Dị ứng Ginkgo biloba", "Đang xuất huyết hoạt động"],
            "tương_đối": ["Đang dùng chống đông/kháng tiểu cầu", "Chuẩn bị phẫu thuật", "Tiền sử động kinh"]
        },
        "pregnancy_lactation": {
            "fda_category": "C (tránh dùng gần ngày sinh)",
            "pregnancy_details": "Có thể tăng nguy cơ chảy máu trong chuyển dạ; không nên dùng gần ngày sinh.",
            "lactation": {
                "safety": "Caution",
                "details": "Dữ liệu hạn chế; thận trọng khi cho con bú.",
                "recommendation": "Tránh dùng thường quy ở mẹ cho con bú."
            },
        },
        "hepatic_adjustment": {
            "mild": "Không cần chỉnh",
            "moderate": "Thận trọng",
            "severe": "Thận trọng, dữ liệu hạn chế",
            "notes": "Chuyển hóa qua gan; suy gan có thể thay đổi dược động học."
        },
        "overdose_management": {
            "symptoms": ["Buồn nôn, nôn, tiêu chảy, nhức đầu, chảy máu"],
            "antidote": "Không có antidote đặc hiệu",
            "treatment": ["Ngừng thuốc, điều trị hỗ trợ", "Điều trị chảy máu nếu có"],
            "monitoring": "Dấu hiệu chảy máu, huyết đồ, chức năng gan/thận nếu cần."
        },
        "reversal_agents": None,
        "administration_instructions": {
            "oral": {
                "with_food": "Có thể uống với hoặc không thức ăn.",
                "timing": "Chia 2-3 lần/ngày; đánh giá lại sau 4-12 tuần."
            }
        },
        "references": {
            "primary_sources": [
                "Ginkgo Evaluation of Memory (GEM) Study – không chứng minh lợi ích rõ rệt trong phòng ngừa sa sút trí tuệ",
                "Các hướng dẫn châu Âu/US nhìn chung không khuyến cáo thường quy",
            ],
            "last_updated": "2025-02-18",
            "evidence_level": "Low–Moderate (herbal, bằng chứng hạn chế)"
        },
    },
}

__all__ = ["CEREBRAL_CIRCULATION_DRUGS"]